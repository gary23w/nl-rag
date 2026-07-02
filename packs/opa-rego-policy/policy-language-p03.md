---
title: "Policy Language (part 3/3)"
source: https://www.openpolicyagent.org/docs/latest/policy-language/
domain: opa-rego-policy
license: CC-BY-SA-4.0
tags: open policy agent, rego policy language, declarative authorization query, policy decision point
fetched: 2026-07-02
part: 3/3
---

## Schema

### Using schemas to enhance the Rego type checker

You can provide one or more input schema files and/or data schema files to `opa eval` to improve static type checking and get more precise error reports as you develop Rego code.

Schemas can be provided to OPA in two main ways: by supplying external JSON Schema files using the `-s` command-line flag (explained below), or by embedding schema definitions directly within your Rego files using schema annotations (detailed further down in this document). Both methods help improve static type checking.

The `-s` flag can be used to upload schemas for input and data documents in JSON Schema format. You can either load a single JSON schema file for the input document or directory of schema files.

```
-s, --schema string set schema file path or directory path
```

#### Passing a single file with -s

When a single file is passed, it is a schema file associated with the input document globally. This means that for all rules in all packages, the `input` has a type derived from that schema. There is no constraint on the name of the file, it could be anything.

Example:

```
opa eval data.envoy.authz.allow -i opa-schema-examples/envoy/input.json -d opa-schema-examples/envoy/policy.rego -s opa-schema-examples/envoy/schemas/my-schema.json
```

#### Passing a directory with -s

When a directory path is passed, annotations will be used in the code to indicate what expressions map to what schemas (see below). Both input schema files and data schema files can be provided in the same directory, with different names. The directory of schemas may have any sub-directories. Notice that when a directory is passed the input document does not have a schema associated with it globally. This must also be indicated via an annotation.

Example:

```
opa eval data.kubernetes.admission -i opa-schema-examples/kubernetes/input.json -d opa-schema-examples/kubernetes/policy.rego -s opa-schema-examples/kubernetes/schemas
```

Schemas can also be provided for policy and data files loaded via `opa eval --bundle`

Example:

```
opa eval data.kubernetes.admission -i opa-schema-examples/kubernetes/input.json -b opa-schema-examples/bundle.tar.gz -s opa-schema-examples/kubernetes/schemas
```

Samples provided at: `github.com/aavarghese/opa-schema-examples`.

### Usage scenario with a single schema file

Consider the following Rego code, which assumes as input a Kubernetes admission review. For resources that are Pods, it checks that the image name starts with a specific prefix.

pod.rego

```rego
package kubernetes.admission

deny contains msg if {
    input.request.kind.kinds == "Pod"
    image := input.request.object.spec.containers[_].image
    not startswith(image, "hooli.com/")
    msg := sprintf("image '%v' comes from untrusted registry", [image])
}
```

Notice that this code has a typo in it: `input.request.kind.kinds` is undefined and should have been `input.request.kind.kind`.

Consider the following input document:

input.json

```json
{
  "kind": "AdmissionReview",
  "request": {
    "kind": {
      "kind": "Pod",
      "version": "v1"
    },
    "object": {
      "metadata": {
        "name": "myapp"
      },
      "spec": {
        "containers": [
          {
            "image": "nginx",
            "name": "nginx-frontend"
          },
          {
            "image": "mysql",
            "name": "mysql-backend"
          }
        ]
      }
    }
  }
}
```

Clearly there are 2 image names that are in violation of the policy. However, evaluating the erroneous Rego code against this input produces:

```shell
$ opa eval data.kubernetes.admission --format pretty -i opa-schema-examples/kubernetes/input.json -d opa-schema-examples/kubernetes/policy.rego
[]
```

The empty value returned is indistinguishable from a situation where the input did not violate the policy. This error is therefore causing the policy not to catch violating inputs appropriately.

Fixing the Rego code and changing `input.request.kind.kinds` to `input.request.kind.kind` produces the expected result:

```json
[
  "image 'nginx' comes from untrusted registry",
  "image 'mysql' comes from untrusted registry"
]
```

With this feature, it is possible to pass a schema to `opa eval`, written in JSON Schema. Consider the admission review schema provided at `schemas/input.json`.

Pass this schema to the evaluator as follows:

```
% opa eval data.kubernetes.admission --format pretty -i opa-schema-examples/kubernetes/input.json -d opa-schema-examples/kubernetes/policy.rego -s opa-schema-examples/kubernetes/schemas/input.json
```

With the erroneous Rego code, the evaluator produces the following type error:

```shell
1 error occurred: ../../aavarghese/opa-schema-examples/kubernetes/policy.rego:5: rego_type_error: undefined ref: input.request.kind.kinds
input.request.kind.kinds
                  ^
                  have: "kinds"
                  want (one of): ["kind" "version"]
```

This indicates the error to the Rego developer right away, without having the need to observe the results of runs on actual data, thereby improving productivity.

### Schema annotations

When passing a directory of schemas to `opa eval`, schema annotations become handy to associate a Rego expression with a corresponding schema within a given scope:

```rego
allow if {
  ...
}
```

See the annotations documentation for general information relating to annotations.

The `schemas` field specifies an array associating schemas to data values. Paths must start with `input` or `data` (i.e., they must be fully-qualified.)

The type checker derives a Rego Object type for the schema and an appropriate entry is added to the type environment before type checking the rule. This entry is removed upon exit from the rule.

Example:

Consider the following Rego code which checks if an operation is allowed by a user, given an ACL data document:

```rego
package policy

import data.acl

default allow := false

allow if {
    access := data.acl.alice
    access[_] == input.operation
}

allow if {
    access := data.acl.bob
    access[_] == input.operation
}
```

Consider a directory named `mySchemasDir` with the following structure, provided via `opa eval --schema opa-schema-examples/mySchemasDir`

```shell
$ tree mySchemasDir/
mySchemasDir/
├── input.json
└── acl-schema.json
```

See here for code samples.

In the first `allow` rule above, the input document has the schema `input.json`, and `data.acl` has the schema `acl-schema.json`. Note that the relative path inside the `mySchemasDir` directory identifies a schema, omitting the `.json` suffix, and uses the global variable `schema` to stand for the top-level of the directory. Schemas in annotations are proper Rego references. So `schema.input` is also valid, but `schema.acl-schema` is not.

The expression `data.acl.foo` in this rule would result in a type error because the schema contained in `acl-schema.json` only defines object properties `"alice"` and `"bob"` in the ACL data document.

On the other hand, this annotation does not constrain other paths under `data`. What it says is that the type of `data.acl` is known statically, but not that of other paths. So for example, `data.foo` is not a type error and gets assigned the type `Any`.

Note that the second `allow` rule doesn't have a METADATA comment block attached to it, and hence will not be type checked with any schemas.

On a different note, schema annotations can also be added to policy files part of a bundle package loaded via `opa eval --bundle` along with the `--schema` parameter for type checking a set of `*.rego` policy files.

The *scope* of the `schema` annotation can be controlled through the scope annotation

In case of overlap, schema annotations override each other as follows:

- `rule` overrides `document`
- `document` overrides `package`
- `package` overrides `subpackages`

The following sections explain how the different scopes affect `schema` annotation overriding for type checking.

#### Rule and Document Scopes

In the example above, the second rule does not include an annotation so type checking of the second rule would not take schemas into account. To enable type checking on the second (or other rules in the same file), specify the annotation multiple times:

```rego
allow if {
    access := data.acl["alice"]
    access[_] == input.operation
}

allow if {
    access := data.acl["bob"]
    access[_] == input.operation
}
```

This is redundant and error-prone. To avoid this problem, define the annotation once on a rule with scope `document`:

```rego
allow if {
    access := data.acl["alice"]
    access[_] == input.operation
}

allow if {
    access := data.acl["bob"]
    access[_] == input.operation
}
```

In this example, the annotation with `document` scope has the same affect as the two `rule` scoped annotations in the previous example.

#### Package and Subpackage Scopes

Annotations can be defined at the `package` level and then applied to all rules within the package:

```rego
package example

allow if {
    access := data.acl["alice"]
    access[_] == input.operation
}

allow if {
    access := data.acl["bob"]
    access[_] == input.operation
}
```

`package` scoped schema annotations are useful when all rules in the same package operate on the same input structure. In some cases, when policies are organized into many sub-packages, it is useful to declare schemas recursively for them using the `subpackages` scope. For example:

```rego
package kubernetes.admission
```

This snippet would declare the top-level schema for `input` for the `kubernetes.admission` package as well as all subpackages. If admission control rules were defined inside packages like `kubernetes.admission.workloads.pods`, they would be able to pick up that one schema declaration.

### Overriding

JSON Schemas are often incomplete specifications of the format of data. For example, a Kubernetes Admission Review resource has a field `object` which can contain any other Kubernetes resource. A schema for Admission Review has a generic type `object` for that field that has no further specification. To allow more precise type checking in such cases, schema overriding is supported.

Consider the following example:

```rego
package kubernetes.admission

deny contains msg if {
    input.request.kind.kind == "Pod"
    image := input.request.object.spec.containers[_].image
    not startswith(image, "hooli.com/")
    msg := sprintf("image '%v' comes from untrusted registry", [image])
}
```

In this example, the `input` is associated with an Admission Review schema, and furthermore `input.request.object` is set to have the schema of a Kubernetes Pod. In effect, the second schema annotation overrides the first one. Overriding is a schema transformation feature and combines existing schemas. In this case, the Admission Review schema is combined with that of a Pod.

Notice that the order of schema annotations matter for overriding to work correctly.

Given a schema annotation, if a prefix of the path already has a type in the environment, then the annotation has the effect of merging and overriding the existing type with the type derived from the schema. In the example above, the prefix `input` already has a type in the type environment, so the second annotation overrides this existing type. Overriding affects the type of the longest prefix that already has a type. If no such prefix exists, the new path and type are added to the type environment for the scope of the rule.

In general, consider the existing Rego type:

```
object{a: object{b: object{c: C, d: D, e: E}}}
```

If this type is overridden with the following type (derived from a schema annotation of the form `a.b.e: schema-for-E1`):

```
object{a: object{b: object{e: E1}}}
```

It results in the following type:

```
object{a: object{b: object{c: C, d: D, e: E1}}}
```

Notice that `b` still has its fields `c` and `d`, so overriding has a merging effect as well. Moreover, the type of expression `a.b.e` is now `E1` instead of `E`.

Overriding can also add new paths to an existing type. If the initial type is overridden with the following:

```
object{a: object{b: object{f: F}}}
```

The result is the following type:

```
object{a: object{b: object{c: C, d: D, e: E, f: F}}}
```

Schemas enhance the type checking capability of OPA, and are not used to validate the input and data documents against desired schemas. This burden is still on the user and care must be taken when using overriding to ensure that the input and data provided are sensible and validated against the transformed schemas.

### Multiple input schemas

It is sometimes useful to have different input schemas for different rules in the same package. This can be achieved as illustrated by the following example:

```rego
package policy

import data.acl

default allow := false

allow if {
    access := data.acl[input.user]
    access[_] == input.operation
}

whocan contains user if {
    access := acl[user]
    access[_] == input.operation
}
```

The directory that is passed to `opa eval` is the following:

```shell
$ tree mySchemasDir/
mySchemasDir/
├── input.json
└── acl-schema.json
└── whocan-input-schema.json
```

In this example, the schema `input.json` is associated with the input document in the rule `allow`, and the schema `whocan-input-schema.json` with the input document for the rule `whocan`.

### Translating schemas to Rego types and dynamicity

Rego has a gradual type system meaning that types can be partially known statically. For example, an object could have certain fields whose types are known and others that are unknown statically. OPA type checks what it knows statically and leaves the unknown parts to be type checked at runtime. An OPA object type has two parts: the static part with the type information known statically, and a dynamic part, which can be nil (meaning everything is known statically) or non-nil and indicating what is unknown.

When deriving a type from a schema, the compiler tries to match what is known and unknown in the schema. For example, an `object` that has no specified fields becomes the Rego type `Object{Any: Any}`. However, currently `additionalProperties` and `additionalItems` are ignored. When a schema is fully specified, the dynamic part is set to nil, meaning that a strict interpretation is used in order to get the most out of static type checking. This is the case even if `additionalProperties` is set to `true` in the schema. In the future, this feature will be taken into account when deriving Rego types.

When overriding existing types, the dynamicity of the overridden prefix is preserved.

### Supporting JSON Schema composition keywords

JSON Schema provides keywords such as `anyOf` and `allOf` to structure a complex schema. For `anyOf`, at least one of the subschemas must be true, and for `allOf`, all subschemas must be true. The type checker is able to identify such keywords and derive a more robust Rego type through more complex schemas.

#### `anyOf`

Specifically, `anyOf` acts as an Rego Or type where at least one (can be more than one) of the subschemas is true. Consider the following Rego and schema file containing `anyOf`:

policy-anyOf.rego

```rego
package kubernetes.admission

deny if {
    input.request.servers.versions == "Pod"
}
```

input-anyOf.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "type": "object",
  "properties": {
    "kind": { "type": "string" },
    "request": {
      "type": "object",
      "anyOf": [
        {
          "properties": {
            "kind": {
              "type": "object",
              "properties": {
                "kind": { "type": "string" },
                "version": { "type": "string" }
              }
            }
          }
        },
        {
          "properties": {
            "server": {
              "type": "object",
              "properties": {
                "accessNum": { "type": "integer" },
                "version": { "type": "string" }
              }
            }
          }
        }
      ]
    }
  }
}
```

The output shows that `request` is an object with two options as indicated by the choices under `anyOf`:

- contains property `kind`, which has properties `kind` and `version`
- contains property `server`, which has properties `accessNum` and `version`

The type checker finds the first error in the Rego code, suggesting that `servers` should be either `kind` or `server`.

```
input.request.servers.versions
              ^
              have: "servers"
              want (one of): ["kind" "server"]
```

Once this is fixed, the second typo is highlighted, prompting the user to choose between `accessNum` and `version`.

```
input.request.server.versions
                     ^
                     have: "versions"
                     want (one of): ["accessNum" "version"]
```

#### `allOf`

Specifically, `allOf` keyword implies that all conditions under `allOf` within a schema must be met by the given data. `allOf` is implemented through merging the types from all of the JSON subSchemas listed under `allOf` before parsing the result to convert it to a Rego type. Merging of the JSON subSchemas essentially combines the passed in subSchemas based on what types they contain. Consider the following Rego and schema file containing `allOf`:

policy-allOf.rego

```rego
package kubernetes.admission

deny if {
    input.request.servers.versions == "Pod"
}
```

input-allOf.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "type": "object",
  "properties": {
    "kind": { "type": "string" },
    "request": {
      "type": "object",
      "allOf": [
        {
          "properties": {
            "kind": {
              "type": "object",
              "properties": {
                "kind": { "type": "string" },
                "version": { "type": "string" }
              }
            }
          }
        },
        {
          "properties": {
            "server": {
              "type": "object",
              "properties": {
                "accessNum": { "type": "integer" },
                "version": { "type": "string" }
              }
            }
          }
        }
      ]
    }
  }
}
```

The output shows that `request` is an object with properties as indicated by the elements listed under `allOf`:

- contains property `kind`, which has properties `kind` and `version`
- contains property `server`, which has properties `accessNum` and `version`

The type checker finds the first error in the Rego code, suggesting that `servers` should be `server`.

```
input.request.servers.versions
              ^
              have: "servers"
              want (one of): ["kind" "server"]
```

Once this is fixed, the second typo is highlighted, informing the user that `versions` should be one of `accessNum` or `version`.

```
input.request.server.versions
                     ^
                     have: "versions"
                     want (one of): ["accessNum" "version"]
```

Because the properties `kind`, `version`, and `accessNum` are all under the `allOf` keyword, the resulting schema that the given data must be validated against will contain the types contained in these properties children (string and integer).

### Remote references in JSON schemas

It is valid for JSON schemas to reference other JSON schemas via URLs, like this:

```json
{
  "description": "Pod is a collection of containers that can run on a host.",
  "type": "object",
  "properties": {
    "metadata": {
      "$ref": "https://kubernetesjsonschema.dev/v1.14.0/_definitions.json#/definitions/io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta",
      "description": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata"
    }
  }
}
```

OPA's type checker will fetch these remote references by default. To control the remote hosts schemas will be fetched from, pass a capabilities file to your `opa eval` or `opa check` call.

Starting from the capabilities.json of your OPA version (which can be found in the repository), add an `allow_net` key to it: its values are the IP addresses or host names that OPA is supposed to connect to for retrieving remote schemas.

```json
{
  "builtins": [ ... ],
  "allow_net": [ "kubernetesjsonschema.dev" ]
}
```

#### Note

- To forbid all network access in schema checking, set `allow_net` to `[]`
- Host names are checked against the list as-is, so adding `127.0.0.1` to `allow_net`, and referencing a schema from `http://localhost/` will *fail*.
- Metaschemas for different JSON Schema draft versions are not subject to this constraint, as they are already provided by OPA's schema checker without requiring network access. These are:
  - `http://json-schema.org/draft-04/schema`
  - `http://json-schema.org/draft-06/schema`
  - `http://json-schema.org/draft-07/schema`

### Limitations

Currently this feature admits schemas written in JSON Schema but does not support every feature available in this format. In particular the following features are not yet supported:

- additional properties for objects
- pattern properties for objects
- additional items for arrays
- contains for arrays
- oneOf, not
- enum
- if/then/else

A note of caution: overriding is a flexible capability that must be used carefully. For example, the user is allowed to write:

```
# METADATA
# scope: rule
# schema:
#  - data: schema["some-schema"]
```

In this case, the root of all documents is being overridden to have some schema. Since all Rego code lives under `data` as virtual documents, this in practice renders all of them inaccessible (resulting in type errors). Similarly, assigning a schema to a package name is not a good idea and can cause problems. Care must also be taken when defining overrides so that the transformation of schemas is sensible and data can be validated against the transformed schema.

### References

For more examples, please see the opa-schema-examples repository.

This contains samples for Envoy, Kubernetes, and Terraform including corresponding JSON Schemas.

See here for the JSON Schema Reference.

For a tool that generates JSON Schema from JSON samples, please see here (Other Tools).


## Strict Mode

The Rego compiler supports `strict mode`, where additional constraints and safety checks are enforced during compilation. Compiler Strict mode is supported by the `check` command, and can be enabled through the `--strict`/`-S` flag.

```
-S, --strict enable compiler strict mode
```

### Strict Mode Constraints and Checks

| Name | Description |
|---|---|
| Unused local assignments | Unused arguments or assignments local to a rule, function or comprehension are prohibited |
| Unused imports | Unused imports are prohibited. |


## Ecosystem Projects

Browse

6

projects related to "

learning-rego

" in the

OPA Ecosystem

.
