---
title: "Policy Language (part 2/3)"
source: https://www.openpolicyagent.org/docs/latest/policy-language/
domain: opa-rego-policy
license: CC-BY-SA-4.0
tags: open policy agent, rego policy language, declarative authorization query, policy decision point
fetched: 2026-07-02
part: 2/3
---

## With Keyword

The `with` keyword allows queries to programmatically specify values nested under the input document or the data document, or built-in functions.

For example, given the simple authorization policy in the imports section, a query can check whether a particular request would be allowed:

```rego
package authz

import data.examples.allow

result := true if {
    allow with input as {"user": "alice", "method": "POST"}
}
```

Loading...

```rego
package authz

import data.examples.allow

result := true if {
    allow with input as {"user": "bob", "method": "GET"}
}
```

Loading...

```rego
package authz

import data.examples.allow

result := true if {
    not allow with input as {"user": "bob", "method": "DELETE"}
}
```

Loading...

It's also possible to use `with` multiple times in the same query. `dev` role allows `GET`, even for an unknown user in the policy.

```rego
package authz

import data.examples.allow

result := true if {
    allow with input as {"user": "charlie", "method": "GET"}
          with data.roles as {"dev": ["charlie"]}
}
```

Loading...

Catherine is only allowed access at weekends. The following query uses `with` to test this functionality:

```rego
package authz

import data.examples.allow

result := true if {
    allow with input as {"user": "catherine", "method": "GET"}
        with data.roles as {"dev": ["bob"]}
        with time.weekday as "Sunday"
}
```

Loading...

The `with` keyword acts as a modifier on expressions. A single expression is allowed to have zero or more `with` modifiers. The `with` keyword has the following syntax:

```
<expr> with <target-1> as <value-1> [with <target-2> as <value-2> [...]]
```

The `<target>`s must be references to values in the input document (or the input document itself) or data document, or references to functions (built-in or not).

info

When applied to the `data` document, the `<target>` must not attempt to partially define virtual documents. For example, given a virtual document at path `data.foo.bar`, the compiler will generate an error if the policy attempts to replace `data.foo.bar.baz`.

The `with` keyword only affects the attached expression. Subsequent expressions will see the unmodified value. The exception to this rule is when multiple `with` keywords are in-scope like below:

```rego
inner := [x, y] if {
    x := input.foo
    y := input.bar
}

middle := [a, b] if {
    a := inner with input.foo as 100
    b := input
}

outer := result if {
    result := middle with input as {"foo": 200, "bar": 300}
}
```

When `<target>` is a reference to a function, like `http.send`, then its `<value>` can be any of the following:

1. a value: `with http.send as {"body": {"success": true }}`
2. a reference to another function: `with http.send as mock_http_send`
3. a reference to another (possibly custom) built-in function: `with custom_builtin as less_strict_custom_builtin`
4. a reference to a rule that will be used as the *value*.

When the replacement value is a function, its arity needs to match the replaced function's arity; and the types must be compatible.

Replacement functions can call the function they're replacing **without causing recursion**. See the following example:

```rego
package mock

f(x) := count(x)

mock_count(x) := 0 if "x" in x
mock_count(x) := count(x) if not "x" in x

result := v if {
    v := f(["x", 2, 3]) with count as mock_count
}
```

Loading...

Each replacement function evaluation will start a new scope: it's valid to use `with <builtin1> as ...` in the body of the replacement function -- for example:

```rego
package mocks

f(x) := count(x) if {
    rule_using_concat with concat as "foo,bar"
}
```

Note that function replacement via `with` does not affect the evaluation of the function arguments: if running `f(input.x), and`input.x`is undefined, the replacement of`concat` does not change the result of the evaluation.


## Default Keyword

The `default` keyword allows policies to define a default value for documents produced by rules with complete definitions. The default value is used when all the rules sharing the same name are undefined.

For example:

```rego
package example

default allow := false

allow if {
    input.user == "bob"
    input.method == "GET"
}
```

Loading...

If this is run with the following input:

```json
{
  "user": "bob",
  "method": "GET"
}
```

```rego
package example

default allow := false

allow if {
    input.user == "bob"
    input.method == "GET"
}
```

Loading...

Without the default definition, the `allow` document would be undefined for the same input.

When the `default` keyword is used, the rule syntax is restricted to:

```rego
default <name> := <term>
```

The term may be any scalar, composite, or comprehension value but it may not be a variable or reference. If the value is a composite then it may not contain variables or references. Comprehensions however may, as the result of a comprehension is never undefined.

Similar to rules, the `default` keyword can be applied to functions as well. For example:

```rego
default clamp_positive(_) := 0

clamp_positive(x) := x if {
    x > 0
}
```

When `clamp_positive` is queried, the return value will be either the argument provided to the function or `0`.

The value of a `default` function follows the same conditions as that of a `default` rule. In addition, a `default` function satisfies the following properties:

- same arity as other functions with the same name
- arguments should only be plain variables i.e. no composite values
- argument names should not be repeated

info

A `default` function will still fail (as in not evaluate, even to the default value) if any of the arguments provided in the call are **undefined**. The reason for this is that the arguments are evaluated before the function is even called, and an undefined argument halts evaluation at that point.

tip

Have a look at the other examples for `default` in the examples section to learn more.


## Else Keyword

The `else` keyword is a basic control flow construct that gives you control over rule evaluation order.

Rules grouped together with the `else` keyword are evaluated until a match is found. Once a match is found, rule evaluation does not proceed to rules further in the chain.

The `else` keyword is useful if you are porting policies into Rego from an order-sensitive system like iptables.

```rego
package else_example

authorize := "allow" if {
    input.user == "superuser"           
} else := "deny" if {
    input.path[0] == "admin"            
    input.source_network == "external"  
} 
```

In the example below, evaluation stops immediately after the first rule even though the input matches the second rule as well.

```json
{
  "path": [
    "admin",
    "exec_shell"
  ],
  "source_network": "external",
  "user": "superuser"
}
```

```rego
package else_example

superuser_result := authorize
```

Loading...

In the next example, the input matches the second rule (but not the first) so evaluation continues to the second rule before stopping.

```json
{
  "path": [
    "admin",
    "exec_shell"
  ],
  "source_network": "external",
  "user": "alice"
}
```

```rego
package else_example

alice_result := authorize
```

Loading...

The `else` keyword may be used repeatedly on the same rule and there is no limit imposed on the number of `else` clauses on a rule. However, it is recommended that policy authors use the `else` keyword sparingly to avoid tightly coupled rules.


## Operators

### Membership and iteration: `in`

The membership operator `in` lets you check if an element is part of a collection (array, set, or object). It always evaluates to `true` or `false`:

```rego
package example

result := {
    "array": 3 in [1, 2, 3],
    "set": 3 in {1, 2, 3},
    "object": 3 in {"foo": 1, "bar": 3},
    "object_key": "foo" in {"foo": 1, "bar": 3}, 
}
```

Loading...

When providing two arguments on the left-hand side of the `in` operator, and an object or an array on the right-hand side, the first argument is taken to be the key (object) or index (array), respectively:

```rego
package example

result.object := "foo", "bar" in {"foo": "bar"} 
result.array := 2, "baz" in ["foo", "bar", "baz"] 
```

Loading...

**Note** that in list contexts, like set or array definitions and function arguments, parentheses are required to use the form with two left-hand side arguments -- compare:

```rego
package list_in

p := x if {
    x := [ 0, 2 in [2] ]
}
q := x if {
    x := [ (0, 2 in [2]) ]
}
w := x if {
    x := g((0, 2 in [2]))
}
z := x if {
    x := f(0, 2 in [2])
}

f(x, y) := sprintf("two function arguments: %v, %v", [x, y])
g(x) := sprintf("one function argument: %v", [x])
```

Loading...

Combined with `not`, the operator can be handy when asserting that an element is *not* member of an array:

```rego
package not_in

deny if not "admin" in input.user.roles

test_deny if {
    deny with input.user.roles as ["operator", "user"]
}
```

Loading...

**Note** that expressions using the `in` operator *always return `true` or `false`*, even when called in non-collection arguments:

```rego
package boolean_in

q := x if {
    x := 3 in "three"
}
```

Loading...

Using the `some` variant, it can be used to introduce new variables based on a collections' items:

```rego
package some_in

p contains x if {
    some x in ["a", "r", "r", "a", "y"]
}

q contains x if {
    some x in {"s", "e", "t"}
}

r contains x if {
    some x in {"foo": "bar", "baz": "quz"}
}
```

Loading...

Furthermore, passing a second argument allows you to work with *object keys* and *array indices*:

```rego
package some_in

p contains x if {
    some x, "r" in ["a", "r", "r", "a", "y"] 
}

q[x] := y if {
    some x, y in ["a", "r", "r", "a", "y"] 
}

r[y] := x if {
    some x, y in {"foo": "bar", "baz": "quz"}
}
```

Loading...

Any argument to the `some` variant can be a composite, non-ground value:

```rego
package some_in

p[x] = y if {
    some x, {"foo": y} in [{"foo": 100}, {"bar": 200}]
}

p[x] = y if {
    some {"bar": x}, {"foo": y} in {{"bar": "b"}: {"foo": "f"}}
}
```

Loading...

Non-ground values

A "non-ground value" is a value that contains variables - like `{"foo": y}` where `y` is a variable that gets bound during evaluation. This is the opposite of a "ground value" which contains no variables. For a formal definition, see ground term.

### Assignment (`:=`)

The assignment operator `:=` is used to assign values to variables. Variables assigned inside a rule are locally scoped to that rule and shadow global variables.

```rego
package assignment

x := 100

p if {
    x := 1     
    x != 100   
}
```

Loading...

Assigned variables are not allowed to appear before the assignment in the query. For example, the following policy will not compile:

```rego
package assignment

p if {
    x != 100
    x := 1     
}

q if {
    x := 1
    x := 2     
}
```

Loading...

A simple form of destructuring can be used to unpack values from arrays and assign them to variables:

```rego
package assignment

address := ["3 Abbey Road", "NW8 9AY", "London", "England"]

in_london if {
    [_, _, city, country] := address
    city == "London"
    country == "England"
}
```

Loading...

### Equality: Comparison, and Unification

Rego supports two kinds of equality: comparison (`==`) and unification `=`. Generally, to test equality, using `==` for the comparison is recommended. The unification operator `=` can be thought of as a combination of `:=` and `==`, and is generally suited to some more advanced use cases.

#### Comparison `==`

Comparison checks if two values are equal within a rule. If the left or right hand side contains a variable that has not been assigned a value, the compiler throws an error.

```rego
package comparison

p if {
    x := 100
    x == 100   
}

y := 100

q if {
    y == 100   
}
```

Loading...

Values used in comparison must be assigned before the comparison is made. For example, the following policy will not compile:

```rego
package comparison

p if {
    z == 100 
}
```

Loading...

#### Unification `=`

Unification (`=`) combines assignment and comparison. Rego will assign variables to values that make the comparison true. Unification lets you ask for values for variables that make an expression true.

```rego
package unification

result := [x, y] if {
    [x, "world"] = ["hello", y]
}
```

Loading...

```rego
package unification

import data.example.sites
import data.example.apps

result contains sites[i].servers[j].name if {
    sites[i].servers[j].name = apps[k].servers[m]
}
```

Loading...

As opposed to when assignment (`:=`) is used, the order of expressions in a rule does not affect the document’s content.

```rego
package unification

s if {
    x > y
    y = 41
    x = 42
}
```

Loading...

#### Best Practices for Equality and Assignment

Best practice is to use assignment `:=` and comparison `==` unless you know you need to use unification. The additional compiler checks help avoid errors when writing policy, and the additional syntax helps make the intent clearer when reading policy.

| Equality | Compiler Errors | Use Case |
|---|---|---|
| `:=` | Var already assigned | Assign variable |
| `==` | Var not assigned | Compare values |
| `=` | Values would not be computed | Express query |

Further Reading

There are some Regal rules to help authors make the right decisions:

- `use-assignment-operator`
- `prefer-equals-comparison`

Under the hood `:=` and `==` are syntactic sugar for `=`, local variable creation, and additional compiler checks.

### Comparison Operators

The following comparison operators are supported:

```rego
a  ==  b  
a  !=  b  
a  <   b  
a  <=  b  
a  >   b  
a  >=  b  
```

None of these operators bind variables contained in the expression. As a result, if either operand is a variable, the variable must appear in another expression in the same rule that would cause the variable to be bound, i.e., an equality expression or the target position of a built-in function.


## Built-in Functions

In some cases, rules must perform simple arithmetic, aggregation, and so on. Rego provides a number of built-in functions (or “built-ins”) for performing these tasks.

Built-ins can be easily recognized by their syntax. All built-ins have the following form:

```
<name>(<arg-1>, <arg-2>, ..., <arg-n>)
```

Built-ins usually take one or more input values and produce one output value. Unless stated otherwise, all built-ins accept values or variables as output arguments.

If a built-in function is invoked with a variable as input, the variable must be *safe*, i.e., it must be assigned elsewhere in the query.

Built-ins can include "." characters in the name. This allows them to be namespaced. If you are adding custom built-ins to OPA, consider namespacing them to avoid naming conflicts, e.g., `org.example.special_func`.

See the Policy Reference document for details on each built-in function.

### Errors

By default, built-in function calls that encounter runtime errors evaluate to undefined (which can usually be treated as `false`) and do not halt policy evaluation. This ensures that built-in functions can be called with invalid inputs without causing the entire policy to stop evaluating.

In most cases, policies do not have to implement any kind of error handling logic. If error handling is required, the built-in function call can be negated to test for undefined. For example:

input.json

```json
{
  "token": "a poorly formatted token"
}
```

```rego
package errors

allow if {
    io.jwt.verify_hs256(input.token, "secret")
    [_, payload, _] := io.jwt.decode(input.token)
    payload.role == "admin"
}

reason contains "invalid JWT supplied as input" if {
    not io.jwt.decode(input.token)
}
```

Loading...

If you wish to disable this behaviour and instead have built-in function call errors treated as exceptions that halt policy evaluation enable "strict built-in errors" in the caller:

| API | Flag |
|---|---|
| `POST v1/data` (HTTP) | `strict-builtin-errors` query parameter |
| `GET v1/data` (HTTP) | `strict-builtin-errors` query parameter |
| `opa eval` (CLI) | `--strict-builtin-errors` |
| `opa run` (REPL) | `> strict-builtin-errors` |
| `rego` Go module | `rego.StrictBuiltinErrors(true)` option |
| Wasm | Not Available |

The package and individual rules in a module can be annotated with a rich set of metadata.

```rego
package metadata

allow if {
  ...
}
```

Annotations are grouped within a *metadata block*, and must be specified as YAML within a comment block that **must** start with `# METADATA`. Also, every line in the comment block containing the annotation **must** start at Column 1 in the module/file, or otherwise, they will be ignored.

danger

OPA will attempt to parse the YAML document in comments following the initial `# METADATA` comment. If the YAML document cannot be parsed, OPA will return an error. If you need to include additional comments between the comment block and the next statement, include a blank line immediately after the comment block containing the YAML document. This tells OPA that the comment block containing the YAML document is finished

### Annotations

| Name | Type | Description |
|---|---|---|
| scope | string; one of `package`, `rule`, `document`, `subpackages` | The scope for which the metadata applies. Read more in the Metadata Scope section below. |
| `labels` | mapping of key-value pairs | Arbitrary labels attached to a rule, recorded in decision logs when the rule is evaluated. Read more in the Metadata Labels section below. |
| `title` | string | A human-readable name for the annotation target. Read more in the Metadata Title section below. |
| `description` | string | A description of the annotation target. Read more in the Metadata Description section below. |
| `related_resources` | list of URLs | A list of URLs pointing to related resources/documentation. Read more in the Metadata Related Resources section below. |
| `authors` | list of strings | A list of authors for the annotation target. Read more in the Metadata Authors section below. |
| `organizations` | list of strings | A list of organizations related to the annotation target. Read more in the Metadata Organizations section below. |
| `schemas` | list of object | A list of associations between value paths and schema definitions. Read more in the Metadata Schemas section below. |
| `entrypoint` | boolean | Whether or not the annotation target is to be used as a policy entrypoint. Read more in the Metadata Entrypoint section below. |
| `custom` | mapping of arbitrary data | A custom mapping of named parameters holding arbitrary data. Read more in the Metadata Custom section below. |

Annotations can be defined at the rule or package level. The `scope` annotation in a metadata block determines how that metadata block will be applied. If the `scope` field is omitted, it defaults to the scope for the statement that immediately follows the annotation. The `scope` values that are currently supported are:

- `rule` - applies to the individual rule statement (within the same file). Default, when metadata block precedes rule.
- `document` - applies to all of the rules with the same name in the same package (across multiple files)
- `package` - applies to all of the rules in the package (across multiple files). Default, when metadata block precedes package.
- `subpackages` - applies to all of the rules in the package and all subpackages (recursively, across multiple files)

Since the `document` scope annotation applies to all rules with the same name in the same package and the `package` and `subpackages` scope annotations apply to all packages with a matching path, metadata blocks with these scopes are applied over all files with applicable package- and rule paths. As there is no ordering across files in the same package, the `document`, `package`, and `subpackages` scope annotations can only be specified **once** per path. The `document` scope annotation can be applied to any rule in the set (i.e., ordering does not matter.)

An `entrypoint` annotation implies a `scope` of either `package` or `document`. When `entrypoint` is set to `true` on a rule, the `scope` is automatically set to `document` if not explicitly provided. Setting the `scope` to `rule` will result in an error, as an entrypoint always applies to the whole document.

```rego
package metadata

allow if {
    x == 1
}

allow if {
    x == 2
}

message := "welcome!" if allow
```

The `labels` annotation is a map of arbitrary key-value pairs attached to a rule (or document, package, or subpackages scope). When rules with `labels` are successfully evaluated, a merged label map is recorded in decision log events under the `rule_labels` field. Labels from subpackages-scoped, package-scoped, document-scoped, and rule-scoped annotations are folded into a single map per rule with inner-scope-wins precedence (on conflicting keys, a rule-scope label overrides document, which overrides package, which overrides subpackages). Identical merged maps across rules are deduplicated.

```rego
allow if input.role == "admin"
```

The `title` annotation is a string value giving a human-readable name to the annotation target.

```rego
allow if {
  x == 1
}

allow if {
  x == 2
}
```

The `description` annotation is a string value describing the annotation target, such as its purpose.

```rego
allow if {
  ...
}
```

The `related_resources` annotation is a list of *related-resource* entries, where each links to some related external resource; such as RFCs and other reading material. A *related-resource* entry can either be an object or a short-form string holding a single URL.

When a *related-resource* entry is presented as an object, it has two fields:

- `ref`: a URL pointing to the resource (required).
- `description`: a text describing the resource.

When a *related-resource* entry is presented as a string, it needs to be a valid URL.

#### Examples

```rego
allow if {
  ...
}
```

```rego
allow if {
  ...
}
```

The `authors` annotation is a list of author entries, where each entry denotes an *author*. An *author* entry can either be an object or a short-form string.

#### Object Author Format

When an *author* entry is presented as an object, it has two fields:

- `name`: the name of the author
- `email`: the email of the author

At least one of the above fields are required for a valid `author` entry.

#### String Author Format

When an *author* entry is presented as a string, it has the format `{ name } [ "<" email ">"]`; where the name of the author is a sequence of whitespace-separated words. Optionally, the last word may represent an email, if enclosed with `<>`.

#### Examples

```rego
allow if {
  ...
}
```

```rego
allow if {
  ...
}
```

The `organizations` annotation is a list of string values representing the organizations associated with the annotation target.

#### Example

```rego
allow if {
  ...
}
```

The `schemas` annotation is a list of key value pairs, associating schemas to data values. In-depth information on this topic can be found in the Annotations section.

#### Schema Reference Format

Schema files can be referenced by path, where each path starts with the `schema` namespace, and trailing components specify the path of the schema file (sans file-ending) relative to the root directory specified by the `--schema` flag on applicable commands. If the `--schema` flag is not present, referenced schemas are ignored during type checking.

```rego
allow if {
    access := data.acl["alice"]
    access[_] == input.operation
}
```

#### Inlined Schema Format

Schema definitions can be inlined by specifying the schema structure as a YAML or JSON map. Inlined schemas are always used to inform type checking for the `eval`, `check`, and `test` commands; in contrast to by-reference schema annotations, which require the `--schema` flag to be present in order to be evaluated.

```rego
allow if {
    input.x == 42
}
```

The `entrypoint` annotation is a boolean used to mark rules and packages that should be used as entrypoints for a policy. This value is false by default, and can only be used at `document` or `package` scope. When used on a rule with no explicit `scope` set, the presence of an `entrypoint` annotation will automatically set the scope to `document`.

The `build` and `eval` CLI commands will automatically pick up annotated entrypoints; you do not have to specify them with `--entrypoint`.

info

Unless the `--prune-unused` flag is used, any rule transitively referring to a package or rule declared as an entrypoint will also be enumerated as an entrypoint.

The `custom` annotation is a mapping of user-defined data, mapping string keys to arbitrarily typed values.

#### Example

```rego
allow if {
  ...
}
```

### Accessing annotations

Information in metadata blocks can be accessed in a number of ways.

#### From Rego Rules

In the example below, you can see how to access an annotation from within a policy.

input.json

```json
{
  "number": 11
}
```

The following policy uses the `rego.metadata.rule()` function to access the metadata from the rule to show in the output message.

```rego
package example

output := decision if {
    input.number > 5

    annotation := rego.metadata.rule()
    decision := {
        "severity": annotation.custom.severity,
        "message": annotation.description,
    }
}
```

Loading...

If you'd like more examples and information on this, you can see more here under the Rego policy reference.

#### From the `inspect` command

Annotations can be listed through the `inspect` command by using the `-a` flag:

```shell
opa inspect -a
```

#### From the Go API

The `ast.AnnotationSet` is a collection of all `ast.Annotations` declared in a set of modules. An `ast.AnnotationSet` can be created from a slice of compiled modules:

```go
var modules []*ast.Module
...
as, err := ast.BuildAnnotationSet(modules)
if err != nil {
    
}
```

or can be retrieved from an `ast.Compiler` instance:

```go
var modules []*ast.Module
...
compiler := ast.NewCompiler()
compiler.Compile(modules)
as := compiler.GetAnnotationSet()
```

The `ast.AnnotationSet` can be flattened into a slice of `ast.AnnotationsRef`, which is a complete, sorted list of all annotations, grouped by the path and location of their targeted package or -rule.

```go
flattened := as.Flatten()
for _, entry := range flattened {
    fmt.Printf("%v at %v has annotations %v\n",
        entry.Path,
        entry.Location,
        entry.Annotations)
}
```

Given an `ast.Rule`, the `ast.AnnotationSet` can return the chain of annotations declared for that rule, and its path ancestry. The returned slice is ordered starting with the annotations for the rule, going outward to the farthest node with declared annotations in the rule's path ancestry.

```go
var rule *ast.Rule
...
chain := ast.Chain(rule)
for _, link := range chain {
    fmt.Printf("link at %v has annotations %v\n",
        link.Path,
        link.Annotations)
}
```
