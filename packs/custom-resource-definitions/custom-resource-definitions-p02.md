---
title: "Extend the Kubernetes API with CustomResourceDefinitions (part 2/3)"
source: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
domain: custom-resource-definitions
license: CC-BY-SA-4.0
tags: custom resource definition, extend kubernetes api, declarative crd schema, aggregated api server
fetched: 2026-07-02
part: 2/3
---

## Advanced topics

### Finalizers

*Finalizers* allow controllers to implement asynchronous pre-delete hooks. Custom objects support finalizers similar to built-in objects.

You can add a finalizer to a custom object like this:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  finalizers:
  - stable.example.com/finalizer
```

Identifiers of custom finalizers consist of a domain name, a forward slash and the name of the finalizer. Any controller can add a finalizer to any object's list of finalizers.

The first delete request on an object with finalizers sets a value for the `metadata.deletionTimestamp` field but does not delete it. Once this value is set, entries in the `finalizers` list can only be removed. While any finalizers remain it is also impossible to force the deletion of an object.

When the `metadata.deletionTimestamp` field is set, controllers watching the object execute any finalizers they handle and remove the finalizer from the list after they are done. It is the responsibility of each controller to remove its finalizer from the list.

The value of `metadata.deletionGracePeriodSeconds` controls the interval between polling updates.

Once the list of finalizers is empty, meaning all finalizers have been executed, the resource is deleted by Kubernetes.

### Validation

Custom resources are validated via OpenAPI v3.0 schemas, by x-kubernetes-validations when the Validation Rules feature is enabled, and you can add additional validation using admission webhooks.

Additionally, the following restrictions are applied to the schema:

- These fields cannot be set:
  - `definitions`,
  - `dependencies`,
  - `deprecated`,
  - `discriminator`,
  - `id`,
  - `patternProperties`,
  - `readOnly`,
  - `writeOnly`,
  - `xml`,
  - `$ref`.
- The field `uniqueItems` cannot be set to `true`.
- The field `additionalProperties` cannot be set to `false`.
- The field `additionalProperties` is mutually exclusive with `properties`.

The `x-kubernetes-validations` extension can be used to validate custom resources using Common Expression Language (CEL) expressions when the Validation rules feature is enabled and the CustomResourceDefinition schema is a structural schema.

Refer to the structural schemas section for other restrictions and CustomResourceDefinition features.

The schema is defined in the CustomResourceDefinition. In the following example, the CustomResourceDefinition applies the following validations on the custom object:

- `spec.cronSpec` must be a string and must be of the form described by the regular expression.
- `spec.replicas` must be an integer and must have a minimum value of 1 and a maximum value of 10.

Save the CustomResourceDefinition to `resourcedefinition.yaml`:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        # openAPIV3Schema is the schema for validating custom objects.
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                  pattern: '^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$'
                image:
                  type: string
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 10
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

and create it:

```shell
kubectl apply -f resourcedefinition.yaml
```

A request to create a custom object of kind CronTab is rejected if there are invalid values in its fields. In the following example, the custom object contains fields with invalid values:

- `spec.cronSpec` does not match the regular expression.
- `spec.replicas` is greater than 10.

If you save the following YAML to `my-crontab.yaml`:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * *"
  image: my-awesome-cron-image
  replicas: 15
```

and attempt to create it:

```shell
kubectl apply -f my-crontab.yaml
```

then you get an error:

```console
The CronTab "my-new-cron-object" is invalid: []: Invalid value: map[string]interface {}{"apiVersion":"stable.example.com/v1", "kind":"CronTab", "metadata":map[string]interface {}{"name":"my-new-cron-object", "namespace":"default", "deletionTimestamp":interface {}(nil), "deletionGracePeriodSeconds":(*int64)(nil), "creationTimestamp":"2017-09-05T05:20:07Z", "uid":"e14d79e7-91f9-11e7-a598-f0761cb232d1", "clusterName":""}, "spec":map[string]interface {}{"cronSpec":"* * * *", "image":"my-awesome-cron-image", "replicas":15}}:
validation failure list:
spec.cronSpec in body should match '^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$'
spec.replicas in body should be less than or equal to 10
```

If the fields contain valid values, the object creation request is accepted.

Save the following YAML to `my-crontab.yaml`:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
  replicas: 5
```

And create it:

```shell
kubectl apply -f my-crontab.yaml
crontab "my-new-cron-object" created
```

### Validation ratcheting

FEATURE STATE:

Kubernetes v1.33 [stable]

(enabled by default)

If you are using a version of Kubernetes older than v1.30, you need to explicitly enable the `CRDValidationRatcheting` feature gate to use this behavior, which then applies to all CustomResourceDefinitions in your cluster.

Provided you enabled the feature gate, Kubernetes implements *validation ratcheting* for CustomResourceDefinitions. The API server is willing to accept updates to resources that are not valid after the update, provided that each part of the resource that failed to validate was not changed by the update operation. In other words, any invalid part of the resource that remains invalid must have already been wrong. You cannot use this mechanism to update a valid resource so that it becomes invalid.

This feature allows authors of CRDs to confidently add new validations to the OpenAPIV3 schema under certain conditions. Users can update to the new schema safely without bumping the version of the object or breaking workflows.

While most validations placed in the OpenAPIV3 schema of a CRD support ratcheting, there are a few exceptions. The following OpenAPIV3 schema validations are not supported by ratcheting under the implementation in Kubernetes 1.36 and if violated will continue to throw an error as normally:

- Quantors
  - `allOf`
  - `oneOf`
  - `anyOf`
  - `not`
  - any validations in a descendent of one of these fields
- `x-kubernetes-validations` For Kubernetes 1.28, CRD validation rules are ignored by ratcheting. Starting with Alpha 2 in Kubernetes 1.29, `x-kubernetes-validations` are ratcheted only if they do not refer to `oldSelf`.Transition Rules are never ratcheted: only errors raised by rules that do not use `oldSelf` will be automatically ratcheted if their values are unchanged.To write custom ratcheting logic for CEL expressions, check out optionalOldSelf.
- `x-kubernetes-list-type` Errors arising from changing the list type of a subschema will not be ratcheted. For example adding `set` onto a list with duplicates will always result in an error.
- `x-kubernetes-list-map-keys` Errors arising from changing the map keys of a list schema will not be ratcheted.
- `required` Errors arising from changing the list of required fields will not be ratcheted.
- `properties` Adding/removing/modifying the names of properties is not ratcheted, but changes to validations in each properties' schemas and subschemas may be ratcheted if the name of the property stays the same.
- `additionalProperties` To remove a previously specified `additionalProperties` validation will not be ratcheted.
- `metadata` Errors that come from Kubernetes' built-in validation of an object's `metadata` are not ratcheted (such as object name, or characters in a label value). If you specify your own additional rules for the metadata of a custom resource, that additional validation will be ratcheted.

### Validation rules

FEATURE STATE:

Kubernetes v1.29 [stable]

Validation rules use the Common Expression Language (CEL) to validate custom resource values. Validation rules are included in CustomResourceDefinition schemas using the `x-kubernetes-validations` extension.

The Rule is scoped to the location of the `x-kubernetes-validations` extension in the schema. And `self` variable in the CEL expression is bound to the scoped value.

All validation rules are scoped to the current object: no cross-object or stateful validation rules are supported.

For example:

```yaml
  # ...
  openAPIV3Schema:
    type: object
    properties:
      spec:
        type: object
        x-kubernetes-validations:
          - rule: "self.minReplicas <= self.replicas"
            message: "replicas should be greater than or equal to minReplicas."
          - rule: "self.replicas <= self.maxReplicas"
            message: "replicas should be smaller than or equal to maxReplicas."
        properties:
          # ...
          minReplicas:
            type: integer
          replicas:
            type: integer
          maxReplicas:
            type: integer
        required:
          - minReplicas
          - replicas
          - maxReplicas
```

will reject a request to create this custom resource:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  minReplicas: 0
  replicas: 20
  maxReplicas: 10
```

with the response:

```
The CronTab "my-new-cron-object" is invalid:
* spec: Invalid value: map[string]interface {}{"maxReplicas":10, "minReplicas":0, "replicas":20}: replicas should be smaller than or equal to maxReplicas.
```

`x-kubernetes-validations` could have multiple rules. The `rule` under `x-kubernetes-validations` represents the expression which will be evaluated by CEL. The `message` represents the message displayed when validation fails. If message is unset, the above response would be:

```
The CronTab "my-new-cron-object" is invalid:
* spec: Invalid value: map[string]interface {}{"maxReplicas":10, "minReplicas":0, "replicas":20}: failed rule: self.replicas <= self.maxReplicas
```

#### Note:

You can quickly test CEL expressions in

CEL Playground

.

Validation rules are compiled when CRDs are created/updated. The request of CRDs create/update will fail if compilation of validation rules fail. Compilation process includes type checking as well.

The compilation failure:

- `no_matching_overload`: this function has no overload for the types of the arguments.For example, a rule like `self == true` against a field of integer type will get error:
  ```
Invalid value: apiextensions.ValidationRule{Rule:"self == true", Message:""}: compilation failed: ERROR: \<input>:1:6: found no matching overload for '_==_' applied to '(int, bool)'
  ```
- `no_such_field`: does not contain the desired field.For example, a rule like `self.nonExistingField > 0` against a non-existing field will return the following error:
  ```
Invalid value: apiextensions.ValidationRule{Rule:"self.nonExistingField > 0", Message:""}: compilation failed: ERROR: \<input>:1:5: undefined field 'nonExistingField'
  ```
- `invalid argument`: invalid argument to macros.For example, a rule like `has(self)` will return error:
  ```
Invalid value: apiextensions.ValidationRule{Rule:"has(self)", Message:""}: compilation failed: ERROR: <input>:1:4: invalid argument to has() macro
  ```

Validation Rules Examples:

| Rule | Purpose |
|---|---|
| `self.minReplicas <= self.replicas && self.replicas <= self.maxReplicas` | Validate that the three fields defining replicas are ordered appropriately |
| `'Available' in self.stateCounts` | Validate that an entry with the 'Available' key exists in a map |
| `(size(self.list1) == 0) != (size(self.list2) == 0)` | Validate that one of two lists is non-empty, but not both |
| `!('MY_KEY' in self.map1) \|\| self['MY_KEY'].matches('^[a-zA-Z]*$')` | Validate the value of a map for a specific key, if it is in the map |
| `self.envars.filter(e, e.name == 'MY_ENV').all(e, e.value.matches('^[a-zA-Z]*$')` | Validate the 'value' field of a listMap entry where key field 'name' is 'MY_ENV' |
| `has(self.expired) && self.created + self.ttl < self.expired` | Validate that 'expired' date is after a 'create' date plus a 'ttl' duration |
| `self.health.startsWith('ok')` | Validate a 'health' string field has the prefix 'ok' |
| `self.widgets.exists(w, w.key == 'x' && w.foo < 10)` | Validate that the 'foo' property of a listMap item with a key 'x' is less than 10 |
| `type(self) == string ? self == '100%' : self == 1000` | Validate an int-or-string field for both the int and string cases |
| `self.metadata.name.startsWith(self.prefix)` | Validate that an object's name has the prefix of another field value |
| `self.set1.all(e, !(e in self.set2))` | Validate that two listSets are disjoint |
| `size(self.names) == size(self.details) && self.names.all(n, n in self.details)` | Validate the 'details' map is keyed by the items in the 'names' listSet |
| `size(self.clusters.filter(c, c.name == self.primary)) == 1` | Validate that the 'primary' property has one and only one occurrence in the 'clusters' listMap |

Xref: Supported evaluation on CEL

- If the Rule is scoped to the root of a resource, it may make field selection into any fields declared in the OpenAPIv3 schema of the CRD as well as `apiVersion`, `kind`, `metadata.name` and `metadata.generateName`. This includes selection of fields in both the `spec` and `status` in the same expression:`# ... openAPIV3Schema: type: object x-kubernetes-validations: - rule: "self.status.availableReplicas >= self.spec.minReplicas" properties: spec: type: object properties: minReplicas: type: integer # ... status: type: object properties: availableReplicas: type: integer`
- If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions.`# ... openAPIV3Schema: type: object properties: spec: type: object x-kubernetes-validations: - rule: "has(self.foo)" properties: # ... foo: type: integer`
- If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`.`# ... openAPIV3Schema: type: object properties: spec: type: object x-kubernetes-validations: - rule: "self['xyz'].foo > 0" additionalProperties: # ... type: object properties: foo: type: integer`
- If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions.`# ... openAPIV3Schema: type: object properties: # ... foo: type: array x-kubernetes-validations: - rule: "size(self) == 1" items: type: string`
- If the Rule is scoped to a scalar, `self` is bound to the scalar value.`# ... openAPIV3Schema: type: object properties: spec: type: object properties: # ... foo: type: integer x-kubernetes-validations: - rule: "self > 0"`

Examples:

| type of the field rule scoped to | Rule example |
|---|---|
| root object | `self.status.actual <= self.spec.maxDesired` |
| map of objects | `self.components['Widget'].priority < 10` |
| list of integers | `self.values.all(value, value >= 0 && value < 100)` |
| string | `self.startsWith('kube')` |

The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any `x-kubernetes-embedded-resource` annotated objects. No other metadata properties are accessible.

Unknown data preserved in custom resources via `x-kubernetes-preserve-unknown-fields` is not accessible in CEL expressions. This includes:

- Unknown field values that are preserved by object schemas with `x-kubernetes-preserve-unknown-fields`.
- Object properties where the property schema is of an "unknown type". An "unknown type" is recursively defined as:
  - A schema with no type and x-kubernetes-preserve-unknown-fields set to true
  - An array where the items schema is of an "unknown type"
  - An object where the additionalProperties schema is of an "unknown type"

Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression:

| escape sequence | property name equivalent |
|---|---|
| `__underscores__` | `__` |
| `__dot__` | `.` |
| `__dash__` | `-` |
| `__slash__` | `/` |
| `__{keyword}__` | CEL RESERVED keyword |

Note: CEL RESERVED keyword needs to match the exact property name to be escaped (e.g. int in the word sprint would not be escaped).

Examples on escaping:

| property name | rule with escaped property name |
|---|---|
| namespace | `self.__namespace__ > 0` |
| x-prop | `self.x__dash__prop > 0` |
| redact__d | `self.redact__underscores__d > 0` |
| string | `self.startsWith('kube')` |

Equality on arrays with `x-kubernetes-list-type` of `set` or `map` ignores element order, i.e., `[1, 2] == [2, 1]`. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:

- `set`: `X + Y` performs a union where the array positions of all elements in `X` are preserved and non-intersecting elements in `Y` are appended, retaining their partial order.
- `map`: `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with non-intersecting keys are appended, retaining their partial order.

Here is the declarations type mapping between OpenAPIv3 and CEL type:

| OpenAPIv3 type | CEL type |
|---|---|
| 'object' with Properties | object / "message type" |
| 'object' with AdditionalProperties | map |
| 'object' with x-kubernetes-embedded-type | object / "message type", 'apiVersion', 'kind', 'metadata.name' and 'metadata.generateName' are implicitly included in schema |
| 'object' with x-kubernetes-preserve-unknown-fields | object / "message type", unknown fields are NOT accessible in CEL expression |
| x-kubernetes-int-or-string | dynamic object that is either an int or a string, `type(value)` can be used to check the type |
| 'array | list |
| 'array' with x-kubernetes-list-type=map | list with map based Equality & unique key guarantees |
| 'array' with x-kubernetes-list-type=set | list with set based Equality & unique entry guarantees |
| 'boolean' | boolean |
| 'number' (all formats) | double |
| 'integer' (all formats) | int (64) |
| 'null' | null_type |
| 'string' | string |
| 'string' with format=byte (base64 encoded) | bytes |
| 'string' with format=date | timestamp (google.protobuf.Timestamp) |
| 'string' with format=datetime | timestamp (google.protobuf.Timestamp) |
| 'string' with format=duration | duration (google.protobuf.Duration) |

xref: CEL types, OpenAPI types, Kubernetes Structural Schemas.

#### The messageExpression field

Similar to the `message` field, which defines the string reported for a validation rule failure, `messageExpression` allows you to use a CEL expression to construct the message string. This allows you to insert more descriptive information into the validation failure message. `messageExpression` must evaluate a string and may use the same variables that are available to the `rule` field. For example:

```yaml
x-kubernetes-validations:
- rule: "self.x <= self.maxLimit"
  messageExpression: '"x exceeded max limit of " + string(self.maxLimit)'
```

Keep in mind that CEL string concatenation (`+` operator) does not auto-cast to string. If you have a non-string scalar, use the `string(<value>)` function to cast the scalar to a string like shown in the above example.

`messageExpression` must evaluate to a string, and this is checked while the CRD is being written. Note that it is possible to set `message` and `messageExpression` on the same rule, and if both are present, `messageExpression` will be used. However, if `messageExpression` evaluates to an error, the string defined in `message` will be used instead, and the `messageExpression` error will be logged. This fallback will also occur if the CEL expression defined in `messageExpression` generates an empty string, or a string containing line breaks.

If one of the above conditions are met and no `message` has been set, then the default validation failure message will be used instead.

`messageExpression` is a CEL expression, so the restrictions listed in Resource use by validation functions apply. If evaluation halts due to resource constraints during `messageExpression` execution, then no further validation rules will be executed.

Setting `messageExpression` is optional.

#### The `message` field

If you want to set a static message, you can supply `message` rather than `messageExpression`. The value of `message` is used as an opaque error string if validation fails.

Setting `message` is optional.

#### The `reason` field

You can add a machine-readable validation failure reason within a `validation`, to be returned whenever a request fails this validation rule.

For example:

```yaml
x-kubernetes-validations:
- rule: "self.x <= self.maxLimit"
  reason: "FieldValueInvalid"
```

The HTTP status code returned to the caller will match the reason of the first failed validation rule. The currently supported reasons are: "FieldValueInvalid", "FieldValueForbidden", "FieldValueRequired", "FieldValueDuplicate". If not set or unknown reasons, default to use "FieldValueInvalid".

Setting `reason` is optional.

#### The `fieldPath` field

You can specify the field path returned when the validation fails.

For example:

```yaml
x-kubernetes-validations:
- rule: "self.foo.test.x <= self.maxLimit"
  fieldPath: ".foo.test.x"
```

In the example above, the validation checks the value of field `x` should be less than the value of `maxLimit`. If no `fieldPath` specified, when validation fails, the fieldPath would be default to wherever `self` scoped. With `fieldPath` specified, the returned error will have `fieldPath` properly refer to the location of field `x`.

The `fieldPath` value must be a relative JSON path that is scoped to the location of this x-kubernetes-validations extension in the schema. Additionally, it should refer to an existing field within the schema. For example when validation checks if a specific attribute `foo` under a map `testMap`, you could set `fieldPath` to `".testMap.foo"` or `.testMap['foo']'`. If the validation requires checking for unique attributes in two lists, the fieldPath can be set to either of the lists. For example, it can be set to `.testList1` or `.testList2`. It supports child operation to refer to an existing field currently. Refer to JSONPath support in Kubernetes for more info. The `fieldPath` field does not support indexing arrays numerically.

Setting `fieldPath` is optional.

#### The `optionalOldSelf` field

FEATURE STATE:

Kubernetes v1.33 [stable]

(enabled by default)

If your cluster does not have CRD validation ratcheting enabled, the CustomResourceDefinition API doesn't include this field, and trying to set it may result in an error.

The `optionalOldSelf` field is a boolean field that alters the behavior of Transition Rules described below. Normally, a transition rule will not evaluate if `oldSelf` cannot be determined: during object creation or when a new value is introduced in an update.

If `optionalOldSelf` is set to true, then transition rules will always be evaluated and the type of `oldSelf` be changed to a CEL `Optional` type.

`optionalOldSelf` is useful in cases where schema authors would like a more control tool than provided by the default equality based behavior of to introduce newer, usually stricter constraints on new values, while still allowing old values to be "grandfathered" or ratcheted using the older validation.

Example Usage:

| CEL | Description |
|---|---|
| `self.foo == "foo" \|\| (oldSelf.hasValue() && oldSelf.value().foo != "foo")` | Ratcheted rule. Once a value is set to "foo", it must stay foo. But if it existed before the "foo" constraint was introduced, it may use any value |
| `[oldSelf.orValue(""), self].all(x, ["OldCase1", "OldCase2"].exists(case, x == case)) \|\| ["NewCase1", "NewCase2"].exists(case, self == case) \|\| ["NewCase"].has(self)` | "Ratcheted validation for removed enum cases if oldSelf used them" |
| `oldSelf.optMap(o, o.size()).orValue(0) < 4 \|\| self.size() >= 4` | Ratcheted validation of newly increased minimum map or list size |

#### Validation functions

Functions available include:

- CEL standard functions, defined in the list of standard definitions
- CEL standard macros
- CEL extended string function library
- Kubernetes CEL extension library

#### Transition rules

A rule that contains an expression referencing the identifier `oldSelf` is implicitly considered a *transition rule*. Transition rules allow schema authors to prevent certain transitions between two otherwise valid states. For example:

```yaml
type: string
enum: ["low", "medium", "high"]
x-kubernetes-validations:
- rule: "!(self == 'high' && oldSelf == 'low') && !(self == 'low' && oldSelf == 'high')"
  message: cannot transition directly between 'low' and 'high'
```

Unlike other rules, transition rules apply only to operations meeting the following criteria:

- The operation updates an existing object. Transition rules never apply to create operations.
- Both an old and a new value exist. It remains possible to check if a value has been added or removed by placing a transition rule on the parent node. Transition rules are never applied to custom resource creation. When placed on an optional field, a transition rule will not apply to update operations that set or unset the field.
- The path to the schema node being validated by a transition rule must resolve to a node that is comparable between the old object and the new object. For example, list items and their descendants (`spec.foo[10].bar`) can't necessarily be correlated between an existing object and a later update to the same object.

Errors will be generated on CRD writes if a schema node contains a transition rule that can never be applied, e.g. "oldSelf cannot be used on the uncorrelatable portion of the schema within *path*".

Transition rules are only allowed on *correlatable portions* of a schema. A portion of the schema is correlatable if all `array` parent schemas are of type `x-kubernetes-list-type=map`; any `set`or `atomic`array parent schemas make it impossible to unambiguously correlate a `self` with `oldSelf`.

Here are some examples for transition rules:

| Use Case | Rule |
|---|---|
| Immutability | `self.foo == oldSelf.foo` |
| Prevent modification/removal once assigned | `oldSelf != 'bar' \|\| self == 'bar'` or `!has(oldSelf.field) \|\| has(self.field)` |
| Append-only set | `self.all(element, element in oldSelf)` |
| If previous value was X, new value can only be A or B, not Y or Z | `oldSelf != 'X' \|\| self in ['A', 'B']` |
| Monotonic (non-decreasing) counters | `self >= oldSelf` |

#### Resource use by validation functions

When you create or update a CustomResourceDefinition that uses validation rules, the API server checks the likely impact of running those validation rules. If a rule is estimated to be prohibitively expensive to execute, the API server rejects the create or update operation, and returns an error message. A similar system is used at runtime that observes the actions the interpreter takes. If the interpreter executes too many instructions, execution of the rule will be halted, and an error will result. Each CustomResourceDefinition is also allowed a certain amount of resources to finish executing all of its validation rules. If the sum total of its rules are estimated at creation time to go over that limit, then a validation error will also occur.

You are unlikely to encounter issues with the resource budget for validation if you only specify rules that always take the same amount of time regardless of how large their input is. For example, a rule that asserts that `self.foo == 1` does not by itself have any risk of rejection on validation resource budget groups. But if `foo` is a string and you define a validation rule `self.foo.contains("someString")`, that rule takes longer to execute depending on how long `foo` is. Another example would be if `foo` were an array, and you specified a validation rule `self.foo.all(x, x > 5)`. The cost system always assumes the worst-case scenario if a limit on the length of `foo` is not given, and this will happen for anything that can be iterated over (lists, maps, etc.).

Because of this, it is considered best practice to put a limit via `maxItems`, `maxProperties`, and `maxLength` for anything that will be processed in a validation rule in order to prevent validation errors during cost estimation. For example, given this schema with one rule:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      items:
        type: string
      x-kubernetes-validations:
        - rule: "self.all(x, x.contains('a string'))"
```

then the API server rejects this rule on validation budget grounds with error:

```
spec.validation.openAPIV3Schema.properties[spec].properties[foo].x-kubernetes-validations[0].rule: Forbidden:
CEL rule exceeded budget by more than 100x (try simplifying the rule, or adding maxItems, maxProperties, and
maxLength where arrays, maps, and strings are used)
```

The rejection happens because `self.all` implies calling `contains()` on every string in `foo`, which in turn will check the given string to see if it contains `'a string'`. Without limits, this is a very expensive rule.

If you do not specify any validation limit, the estimated cost of this rule will exceed the per-rule cost limit. But if you add limits in the appropriate places, the rule will be allowed:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      maxItems: 25
      items:
        type: string
        maxLength: 10
      x-kubernetes-validations:
        - rule: "self.all(x, x.contains('a string'))"
```
