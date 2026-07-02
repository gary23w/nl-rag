---
title: "GitHub (part 2/2)"
source: https://github.com/jquense/yup
domain: yup-validation
license: CC-BY-SA-4.0
tags: yup validation, object schema validation, form schema, javascript validator
fetched: 2026-07-02
part: 2/2
---

## API

### `yup`

The module export.

```highlight
// core schema
import {
  mixed,
  string,
  number,
  boolean,
  bool,
  date,
  object,
  array,
  ref,
  lazy,
} from 'yup';

// Classes
import {
  Schema,
  MixedSchema,
  StringSchema,
  NumberSchema,
  BooleanSchema,
  DateSchema,
  ArraySchema,
  ObjectSchema,
} from 'yup';

// Types
import type { InferType, ISchema, AnySchema, AnyObjectSchema } from 'yup';
```

#### `reach(schema: Schema, path: string, value?: object, context?: object): Schema`

For nested schemas, `reach` will retrieve an inner schema based on the provided path.

For nested schemas that need to resolve dynamically, you can provide a `value` and optionally a `context` object.

```highlight
import { reach } from 'yup';

let schema = object({
  nested: object({
    arr: array(object({ num: number().max(4) })),
  }),
});

reach(schema, 'nested.arr.num');
reach(schema, 'nested.arr[].num');
reach(schema, 'nested.arr[1].num');
reach(schema, 'nested["arr"][1].num');
```

#### `addMethod(schemaType: Schema, name: string, method: ()=> Schema): void`

Adds a new method to the core schema types. A friendlier convenience method for `schemaType.prototype[name] = method`.

```highlight
import { addMethod, date } from 'yup';

addMethod(date, 'format', function format(formats, parseStrict) {
  return this.transform((value, originalValue, ctx) => {
    if (ctx.isType(value)) return value;

    value = Moment(originalValue, formats, parseStrict);

    return value.isValid() ? value.toDate() : new Date('');
  });
});
```

If you want to add a method to ALL schema types, extend the abstract base class: `Schema`

```highlight
import { addMethod, Schema } from 'yup';

addMethod(Schema, 'myMethod', ...)
```

#### `ref(path: string, options: { contextPrefix: string }): Ref`

Creates a reference to another sibling or sibling descendant field. Refs are resolved at *validation/cast time* and supported where specified. Refs are evaluated in the proper order so that the ref value is resolved before the field using the ref (be careful of circular dependencies!).

```highlight
import { ref, object, string } from 'yup';

let schema = object({
  baz: ref('foo.bar'),
  foo: object({
    bar: string(),
  }),
  x: ref('$x'),
});

schema.cast({ foo: { bar: 'boom' } }, { context: { x: 5 } });
// => { baz: 'boom',  x: 5, foo: { bar: 'boom' } }
```

#### `lazy((value: any) => Schema): Lazy`

Creates a schema that is evaluated at validation/cast time. Useful for creating recursive schema like Trees, for polymorphic fields and arrays.

**CAUTION!** When defining parent-child recursive object schema, you want to reset the `default()` to `null` on the child—otherwise the object will infinitely nest itself when you cast it!

```highlight
let node = object({
  id: number(),
  child: yup.lazy(() => node.default(undefined)),
});

let renderable = yup.lazy((value) => {
  switch (typeof value) {
    case 'number':
      return number();
    case 'string':
      return string();
    default:
      return mixed();
  }
});

let renderables = array().of(renderable);
```

#### `ValidationError(errors: string | Array<string>, value: any, path: string)`

Thrown on failed validations, with the following properties

- `name`: "ValidationError"
- `type`: the specific test type or test "name", that failed.
- `value`: The field value that was tested;
- `params`?: The test inputs, such as max value, regex, etc;
- `path`: a string, indicating where there error was thrown. `path` is empty at the root level.
- `errors`: array of error messages
- `inner`: in the case of aggregate errors, inner is an array of `ValidationErrors` throw earlier in the validation chain. When the `abortEarly` option is `false` this is where you can inspect each error thrown, alternatively, `errors` will have all of the messages from each inner error.

### `Schema`

`Schema` is the abstract base class that all schema type inherit from. It provides a number of base methods and properties to all other schema types.

> Note: unless you are creating a custom schema type, Schema should never be used directly. For unknown/any types use `mixed()`

#### `Schema.clone(): Schema`

Creates a deep copy of the schema. Clone is used internally to return a new schema with every schema state change.

#### `Schema.label(label: string): Schema`

Overrides the key name which is used in error messages.

#### `Schema.meta(metadata: SchemaMetadata): Schema`

Adds to a metadata object, useful for storing data with a schema, that doesn't belong to the cast object itself.

A custom `SchemaMetadata` interface can be defined through merging with the `CustomSchemaMetadata` interface. Start by creating a `yup.d.ts` file in your package and creating your desired `CustomSchemaMetadata` interface:

```highlight
// yup.d.ts
import 'yup';

declare module 'yup' {
  // Define your desired `SchemaMetadata` interface by merging the
  // `CustomSchemaMetadata` interface.
  export interface CustomSchemaMetadata {
    placeholderText?: string;
    tooltipText?: string;
    // …
  }
}
```

#### `Schema.describe(options?: ResolveOptions): SchemaDescription`

Collects schema details (like meta, labels, and active tests) into a serializable description object.

```highlight
let schema = object({
  name: string().required(),
});

let description = schema.describe();
```

For schema with dynamic components (references, lazy, or conditions), describe requires more context to accurately return the schema description. In these cases provide `options`

```highlight
import { ref, object, string, boolean } from 'yup';

let schema = object({
  isBig: boolean(),
  count: number().when('isBig', {
    is: true,
    then: (schema) => schema.min(5),
    otherwise: (schema) => schema.min(0),
  }),
});

schema.describe({ value: { isBig: true } });
```

And below are the description types, which differ a bit depending on the schema type.

```highlight
interface SchemaDescription {
  type: string;
  label?: string;
  meta: object | undefined;
  oneOf: unknown[];
  notOneOf: unknown[];
  default?: unknown;
  nullable: boolean;
  optional: boolean;
  tests: Array<{ name?: string; params: ExtraParams | undefined }>;

  // Present on object schema descriptions
  fields: Record<string, SchemaFieldDescription>;

  // Present on array schema descriptions
  innerType?: SchemaFieldDescription;
}

type SchemaFieldDescription =
  | SchemaDescription
  | SchemaRefDescription
  | SchemaLazyDescription;

interface SchemaRefDescription {
  type: 'ref';
  key: string;
}

interface SchemaLazyDescription {
  type: string;
  label?: string;
  meta: object | undefined;
}
```

#### `Schema.concat(schema: Schema): Schema`

Creates a new instance of the schema by combining two schemas. Only schemas of the same type can be concatenated. `concat` is not a "merge" function in the sense that all settings from the provided schema, override ones in the base, including type, presence and nullability.

```highlight
mixed<string>().defined().concat(mixed<number>().nullable());

// produces the equivalent to:

mixed<number>().defined().nullable();
```

#### `Schema.validate(value: any, options?: object): Promise<InferType<Schema>, ValidationError>`

Returns the parses and validates an input value, returning the parsed value or throwing an error. This method is **asynchronous** and returns a Promise object, that is fulfilled with the value, or rejected with a `ValidationError`.

```highlight
value = await schema.validate({ name: 'jimmy', age: 24 });
```

Provide `options` to more specifically control the behavior of `validate`.

```highlight
interface Options {
  // when true, parsing is skipped and the input is validated "as-is"
  strict: boolean = false;
  // Throw on the first error or collect and return all
  abortEarly: boolean = true;
  // Remove unspecified keys from objects
  stripUnknown: boolean = false;
  // when `false` validations will be performed shallowly
  recursive: boolean = true;
  // External values that can be provided to validations and conditionals
  context?: object;
}
```

#### `Schema.validateSync(value: any, options?: object): InferType<Schema>`

Runs validatations synchronously *if possible* and returns the resulting value, or throws a ValidationError. Accepts all the same options as `validate`.

Synchronous validation only works if there are no configured async tests, e.g tests that return a Promise. For instance this will work:

```highlight
let schema = number().test(
  'is-42',
  "this isn't the number i want",
  (value) => value != 42,
);

schema.validateSync(23); // throws ValidationError
```

however this will not:

```highlight
let schema = number().test('is-42', "this isn't the number i want", (value) =>
  Promise.resolve(value != 42),
);

schema.validateSync(42); // throws Error
```

#### `Schema.validateAt(path: string, value: any, options?: object): Promise<InferType<Schema>, ValidationError>`

Validate a deeply nested path within the schema. Similar to how `reach` works, but uses the resulting schema as the subject for validation.

> Note! The `value` here is the *root* value relative to the starting schema, not the value at the nested path.

```highlight
let schema = object({
  foo: array().of(
    object({
      loose: boolean(),
      bar: string().when('loose', {
        is: true,
        otherwise: (schema) => schema.strict(),
      }),
    }),
  ),
});

let rootValue = {
  foo: [{ bar: 1 }, { bar: 1, loose: true }],
};

await schema.validateAt('foo[0].bar', rootValue); // => ValidationError: must be a string

await schema.validateAt('foo[1].bar', rootValue); // => '1'
```

#### `Schema.validateSyncAt(path: string, value: any, options?: object): InferType<Schema>`

Same as `validateAt` but synchronous.

#### `Schema.isValid(value: any, options?: object): Promise<boolean>`

Returns `true` when the passed in value matches the schema. `isValid` is **asynchronous** and returns a Promise object.

Takes the same options as `validate()`.

#### `Schema.isValidSync(value: any, options?: object): boolean`

Synchronously returns `true` when the passed in value matches the schema.

Takes the same options as `validateSync()` and has the same caveats around async tests.

#### `Schema.cast(value: any, options = {}): InferType<Schema>`

Attempts to coerce the passed in value to a value that matches the schema. For example: `'5'` will cast to `5` when using the `number()` type. Failed casts generally return `null`, but may also return results like `NaN` and unexpected strings.

Provide `options` to more specifically control the behavior of `validate`.

```highlight
interface CastOptions<TContext extends {}> {
  // Remove undefined properties from objects
  stripUnknown: boolean = false;

  // Throws a TypeError if casting doesn't produce a valid type
  // note that the TS return type is inaccurate when this is `false`, use with caution
  assert?: boolean = true;

  // External values that used to resolve conditions and references
  context?: TContext;
}
```

#### `Schema.isType(value: any): value is InferType<Schema>`

Runs a type check against the passed in `value`. It returns true if it matches, it does not cast the value. When `nullable()` is set `null` is considered a valid value of the type. You should use `isType` for all Schema type checks.

#### `Schema.strict(enabled: boolean = false): Schema`

Sets the `strict` option to `true`. Strict schemas skip coercion and transformation attempts, validating the value "as is".

#### `Schema.strip(enabled: boolean = true): Schema`

Marks a schema to be removed from an output object. Only works as a nested schema.

```highlight
let schema = object({
  useThis: number(),
  notThis: string().strip(),
});

schema.cast({ notThis: 'foo', useThis: 4 }); // => { useThis: 4 }
```

Schema with `strip` enabled have an inferred type of `never`, allowing them to be removed from the overall type:

```highlight
let schema = object({
  useThis: number(),
  notThis: string().strip(),
});

InferType<typeof schema>; /*
{
   useThis?: number | undefined
}
*/
```

#### `Schema.withMutation(builder: (current: Schema) => void): void`

First the legally required Rich Hickey quote:

> If a tree falls in the woods, does it make a sound?
> 
> If a pure function mutates some local data in order to produce an immutable return value, is that ok?

`withMutation` allows you to mutate the schema in place, instead of the default behavior which clones before each change. Generally this isn't necessary since the vast majority of schema changes happen during the initial declaration, and only happen once over the lifetime of the schema, so performance isn't an issue. However certain mutations *do* occur at cast/validation time, (such as conditional schema using `when()`), or when instantiating a schema object.

```highlight
object()
  .shape({ key: string() })
  .withMutation((schema) => {
    return arrayOfObjectTests.forEach((test) => {
      schema.test(test);
    });
  });
```

#### `Schema.default(value: any): Schema`

Sets a default value to use when the value is `undefined`. Defaults are created after transformations are executed, but before validations, to help ensure that safe defaults are specified. The default value will be cloned on each use, which can incur performance penalty for objects and arrays. To avoid this overhead you can also pass a function that returns a new default. Note that `null` is considered a separate non-empty value.

```highlight
yup.string.default('nothing');

yup.object.default({ number: 5 }); // object will be cloned every time a default is needed

yup.object.default(() => ({ number: 5 })); // this is cheaper

yup.date.default(() => new Date()); // also helpful for defaults that change over time
```

#### `Schema.getDefault(options?: object): Any`

Retrieve a previously set default value. `getDefault` will resolve any conditions that may alter the default. Optionally pass `options` with `context` (for more info on `context` see `Schema.validate`).

#### `Schema.nullable(message?: string | function): Schema`

Indicates that `null` is a valid value for the schema. Without `nullable()` `null` is treated as a different type and will fail `Schema.isType()` checks.

```highlight
let schema = number().nullable();

schema.cast(null); // null

InferType<typeof schema>; // number | null
```

#### `Schema.nonNullable(message?: string | function): Schema`

The opposite of `nullable`, removes `null` from valid type values for the schema. **Schema are non nullable by default**.

```highlight
let schema = number().nonNullable();

schema.cast(null); // TypeError

InferType<typeof schema>; // number
```

#### `Schema.defined(): Schema`

Require a value for the schema. All field values apart from `undefined` meet this requirement.

```highlight
let schema = string().defined();

schema.cast(undefined); // TypeError

InferType<typeof schema>; // string
```

#### `Schema.optional(): Schema`

The opposite of `defined()` allows `undefined` values for the given type.

```highlight
let schema = string().optional();

schema.cast(undefined); // undefined

InferType<typeof schema>; // string | undefined
```

#### `Schema.required(message?: string | function): Schema`

Mark the schema as required, which will not allow `undefined` or `null` as a value. `required` negates the effects of calling `optional()` and `nullable()`

> Watch out! `string().required`) works a little different and additionally prevents empty string values (`''`) when required.

#### `Schema.notRequired(): Schema`

Mark the schema as not required. This is a shortcut for `schema.nullable().optional()`;

#### `Schema.typeError(message: string): Schema`

Define an error message for failed type checks. The `${value}` and `${type}` interpolation can be used in the `message` argument.

#### `Schema.oneOf(arrayOfValues: Array<any>, message?: string | function): Schema` Alias: `equals`

Only allow values from set of values. Values added are removed from any `notOneOf` values if present. The `${values}` interpolation can be used in the `message` argument. If a ref or refs are provided, the `${resolved}` interpolation can be used in the message argument to get the resolved values that were checked at validation time.

Note that `undefined` does not fail this validator, even when `undefined` is not included in `arrayOfValues`. If you don't want `undefined` to be a valid value, you can use `Schema.required`.

```highlight
let schema = yup.mixed().oneOf(['jimmy', 42]);

await schema.isValid(42); // => true
await schema.isValid('jimmy'); // => true
await schema.isValid(new Date()); // => false
```

#### `Schema.notOneOf(arrayOfValues: Array<any>, message?: string | function)`

Disallow values from a set of values. Values added are removed from `oneOf` values if present. The `${values}` interpolation can be used in the `message` argument. If a ref or refs are provided, the `${resolved}` interpolation can be used in the message argument to get the resolved values that were checked at validation time.

```highlight
let schema = yup.mixed().notOneOf(['jimmy', 42]);

await schema.isValid(42); // => false
await schema.isValid(new Date()); // => true
```

#### `Schema.when(keys: string | string[], builder: object | (values: any[], schema) => Schema): Schema`

Adjust the schema based on a sibling or sibling children fields. You can provide an object literal where the key `is` is value or a matcher function, `then` provides the true schema and/or `otherwise` for the failure condition.

`is` conditions are strictly compared (`===`) if you want to use a different form of equality you can provide a function like: `is: (value) => value == true`.

You can also prefix properties with `$` to specify a property that is dependent on `context` passed in by `validate()` or `cast` instead of the input value.

`when` conditions are additive.

`then` and `otherwise` are specified functions `(schema: Schema) => Schema`.

```highlight
let schema = object({
  isBig: boolean(),
  count: number()
    .when('isBig', {
      is: true, // alternatively: (val) => val == true
      then: (schema) => schema.min(5),
      otherwise: (schema) => schema.min(0),
    })
    .when('$other', ([other], schema) =>
      other === 4 ? schema.max(6) : schema,
    ),
});

await schema.validate(value, { context: { other: 4 } });
```

You can also specify more than one dependent key, in which case each value will be spread as an argument.

```highlight
let schema = object({
  isSpecial: boolean(),
  isBig: boolean(),
  count: number().when(['isBig', 'isSpecial'], {
    is: true, // alternatively: (isBig, isSpecial) => isBig && isSpecial
    then: (schema) => schema.min(5),
    otherwise: (schema) => schema.min(0),
  }),
});

await schema.validate({
  isBig: true,
  isSpecial: true,
  count: 10,
});
```

Alternatively you can provide a function that returns a schema, called with an array of values for each provided key the current schema.

```highlight
let schema = yup.object({
  isBig: yup.boolean(),
  count: yup.number().when('isBig', ([isBig], schema) => {
    return isBig ? schema.min(5) : schema.min(0);
  }),
});

await schema.validate({ isBig: false, count: 4 });
```

#### `Schema.test(name: string, message: string | function | any, test: function): Schema`

Adds a test function to the validation chain. Tests are run after any object is cast. Many types have some tests built in, but you can create custom ones easily. In order to allow asynchronous custom validations *all* (or no) tests are run asynchronously. A consequence of this is that test execution order cannot be guaranteed.

All tests must provide a `name`, an error `message` and a validation function that must return `true` when the current `value` is valid and `false` or a `ValidationError` otherwise. To make a test async return a promise that resolves `true` or `false` or a `ValidationError`.

For the `message` argument you can provide a string which will interpolate certain values if specified using the `${param}` syntax. By default all test messages are passed a `path` value which is valuable in nested schemas.

The `test` function is called with the current `value`. For more advanced validations you can use the alternate signature to provide more options (see below):

```highlight
let jimmySchema = string().test(
  'is-jimmy',
  '${path} is not Jimmy',
  (value, context) => value === 'jimmy',
);

// or make it async by returning a promise
let asyncJimmySchema = string()
  .label('First name')
  .test(
    'is-jimmy',
    ({ label }) => `${label} is not Jimmy`, // a message can also be a function
    async (value, testContext) =>
      (await fetch('/is-jimmy/' + value)).responseText === 'true',
  );

await schema.isValid('jimmy'); // => true
await schema.isValid('john'); // => false
```

Test functions are called with a special context value, as the second argument, that exposes some useful metadata and functions. For non arrow functions, the test context is also set as the function `this`. Watch out, if you access it via `this` it won't work in an arrow function.

- `testContext.path`: the string path of the current validation
- `testContext.schema`: the resolved schema object that the test is running against.
- `testContext.options`: the `options` object that validate() or isValid() was called with
- `testContext.parent`: in the case of nested schema, this is the value of the parent object
- `testContext.originalValue`: the original value that is being tested
- `testContext.createError(Object: { path: String, message: String, params: Object })`: create and return a validation error. Useful for dynamically setting the `path`, `params`, or more likely, the error `message`. If either option is omitted it will use the current path, or default message.

#### `Schema.test(options: object): Schema`

Alternative `test(..)` signature. `options` is an object containing some of the following options:

```highlight
Options = {
  // unique name identifying the test
  name: string;
  // test function, determines schema validity
  test: (value: any) => boolean;
  // the validation error message
  message: string;
  // values passed to message for interpolation
  params: ?object;
  // mark the test as exclusive, meaning only one test of the same name can be active at once
  exclusive: boolean = false;
}
```

In the case of mixing exclusive and non-exclusive tests the following logic is used. If a non-exclusive test is added to a schema with an exclusive test of the same name the exclusive test is removed and further tests of the same name will be stacked.

If an exclusive test is added to a schema with non-exclusive tests of the same name the previous tests are removed and further tests of the same name will replace each other.

```highlight
let max = 64;
let schema = yup.string().test({
  name: 'max',
  exclusive: true,
  params: { max },
  message: '${path} must be less than ${max} characters',
  test: (value) => value == null || value.length <= max,
});
```

#### `Schema.transform((currentValue: any, originalValue: any, schema: Schema, options: object) => any): Schema`

Adds a transformation to the transform chain. Transformations are central to the casting process, default transforms for each type coerce values to the specific type (as verified by `isType()`). transforms are run before validations and only applied when the schema is not marked as `strict` (the default). Some types have built in transformations.

Transformations are useful for arbitrarily altering how the object is cast, **however, you should take care not to mutate the passed in value.** Transforms are run sequentially so each `value` represents the current state of the cast, you can use the `originalValue` param if you need to work on the raw initial value.

```highlight
let schema = string().transform((value, originalValue) => {
  return this.isType(value) && value !== null ? value.toUpperCase() : value;
});

schema.cast('jimmy'); // => 'JIMMY'
```

Each types will handle basic coercion of values to the proper type for you, but occasionally you may want to adjust or refine the default behavior. For example, if you wanted to use a different date parsing strategy than the default one you could do that with a transform.

```highlight
module.exports = function (formats = 'MMM dd, yyyy') {
  return date().transform((value, originalValue, context) => {
    // check to see if the previous transform already parsed the date
    if (context.isType(value)) return value;

    // the default coercion failed so let's try it with Moment.js instead
    value = Moment(originalValue, formats);

    // if it's valid return the date object, otherwise return an `InvalidDate`
    return value.isValid() ? value.toDate() : new Date('');
  });
};
```

### mixed

Creates a schema that matches all types, or just the ones you configure. Inherits from `Schema`. Mixed types extends `{}` by default instead of `any` or `unknown`. This is because in TypeScript `{}` means anything that isn't `null` or `undefined` which yup treats distinctly.

```highlight
import { mixed, InferType } from 'yup';

let schema = mixed().nullable();

schema.validateSync('string'); // 'string';

schema.validateSync(1); // 1;

schema.validateSync(new Date()); // Date;

InferType<typeof schema>; // {} | undefined

InferType<typeof schema.nullable().defined()>; // {} | null
```

Custom types can be implemented by passing a type `check` function. This will also narrow the TypeScript type for the schema.

```highlight
import { mixed, InferType } from 'yup';

let objectIdSchema = yup
  .mixed((input): input is ObjectId => input instanceof ObjectId)
  .transform((value: any, input, ctx) => {
    if (ctx.isType(value)) return value;
    return new ObjectId(value);
  });

await objectIdSchema.validate(ObjectId('507f1f77bcf86cd799439011')); // ObjectId("507f1f77bcf86cd799439011")

await objectIdSchema.validate('507f1f77bcf86cd799439011'); // ObjectId("507f1f77bcf86cd799439011")

InferType<typeof objectIdSchema>; // ObjectId
```

### string

Define a string schema. Inherits from `Schema`.

```highlight
let schema = yup.string();

await schema.isValid('hello'); // => true
```

By default, the `cast` logic of `string` is to call `toString` on the value if it exists.

empty values are not coerced (use `ensure()` to coerce empty values to empty strings).

Failed casts return the input value.

#### `string.required(message?: string | function): Schema`

The same as the `mixed()` schema required, **except** that empty strings are also considered 'missing' values.

#### `string.length(limit: number | Ref, message?: string | function): Schema`

Set a required length for the string value. The `${length}` interpolation can be used in the `message` argument

#### `string.min(limit: number | Ref, message?: string | function): Schema`

Set a minimum length limit for the string value. The `${min}` interpolation can be used in the `message` argument

#### `string.max(limit: number | Ref, message?: string | function): Schema`

Set a maximum length limit for the string value. The `${max}` interpolation can be used in the `message` argument

#### `string.matches(regex: Regex, message?: string | function): Schema`

Provide an arbitrary `regex` to match the value against.

```highlight
let schema = string().matches(/(hi|bye)/);

await schema.isValid('hi'); // => true
await schema.isValid('nope'); // => false
```

#### `string.matches(regex: Regex, options: { message: string, excludeEmptyString: bool }): Schema`

An alternate signature for `string.matches` with an options object. `excludeEmptyString`, when true, short circuits the regex test when the value is an empty string, making it a easier to avoid matching nothing without complicating the regex.

```highlight
let schema = string().matches(/(hi|bye)/, { excludeEmptyString: true });

await schema.isValid(''); // => true
```

#### `string.email(message?: string | function): Schema`

Validates the value as an email address using the same regex as defined by the HTML spec.

WATCH OUT: Validating email addresses is nearly impossible with just code. Different clients and servers accept different things and many diverge from the various specs defining "valid" emails. The ONLY real way to validate an email address is to send a verification email to it and check that the user got it. With that in mind, yup picks a relatively simple regex that does not cover all cases, but aligns with browser input validation behavior since HTML forms are a common use case for yup.

If you have more specific needs please override the email method with your own logic or regex:

```highlight
yup.addMethod(yup.string, 'email', function validateEmail(message) {
  return this.matches(myEmailRegex, {
    message,
    name: 'email',
    excludeEmptyString: true,
  });
});
```

#### `string.url(message?: string | function): Schema`

Validates the value as a valid URL via a regex.

#### `string.uuid(message?: string | function): Schema`

Validates the value as a valid UUID via a regex.

#### `string.datetime(options?: {message?: string | function, allowOffset?: boolean, precision?: number})`

Validates the value as an ISO datetime via a regex. Defaults to UTC validation; timezone offsets are not permitted (see `options.allowOffset`).

Unlike `.date()`, `datetime` will not convert the string to a `Date` object. `datetime` also provides greater customization over the required format of the datetime string than `date` does.

`options.allowOffset`: Allow a time zone offset. False requires UTC 'Z' timezone. *(default: false)* `options.precision`: Require a certain sub-second precision on the date. *(default: null -- any (or no) sub-second precision)*

#### `string.datetime(message?: string | function)`

An alternate signature for `string.datetime` that can be used when you don't need to pass options other than `message`.

#### `string.ensure(): Schema`

Transforms `undefined` and `null` values to an empty string along with setting the `default` to an empty string.

#### `string.trim(message?: string | function): Schema`

Transforms string values by removing leading and trailing whitespace. If `strict()` is set it will only validate that the value is trimmed.

#### `string.lowercase(message?: string | function): Schema`

Transforms the string value to lowercase. If `strict()` is set it will only validate that the value is lowercase.

#### `string.uppercase(message?: string | function): Schema`

Transforms the string value to uppercase. If `strict()` is set it will only validate that the value is uppercase.

### number

Define a number schema. Inherits from `Schema`.

```highlight
let schema = yup.number();

await schema.isValid(10); // => true
```

The default `cast` logic of `number` is: `parseFloat`.

Failed casts return `NaN`.

#### `number.min(limit: number | Ref, message?: string | function): Schema`

Set the minimum value allowed. The `${min}` interpolation can be used in the `message` argument.

#### `number.max(limit: number | Ref, message?: string | function): Schema`

Set the maximum value allowed. The `${max}` interpolation can be used in the `message` argument.

#### `number.lessThan(max: number | Ref, message?: string | function): Schema`

Value must be less than `max`. The `${less}` interpolation can be used in the `message` argument.

#### `number.moreThan(min: number | Ref, message?: string | function): Schema`

Value must be strictly greater than `min`. The `${more}` interpolation can be used in the `message` argument.

#### `number.positive(message?: string | function): Schema`

Value must be a positive number.

#### `number.negative(message?: string | function): Schema`

Value must be a negative number.

#### `number.integer(message?: string | function): Schema`

Validates that a number is an integer.

#### `number.truncate(): Schema`

Transformation that coerces the value to an integer by stripping off the digits to the right of the decimal point.

#### `number.round(type: 'floor' | 'ceil' | 'trunc' | 'round' = 'round'): Schema`

Adjusts the value via the specified method of `Math` (defaults to 'round').

### boolean

Define a boolean schema. Inherits from `Schema`.

```highlight
let schema = yup.boolean();

await schema.isValid(true); // => true
```

### date

Define a Date schema. By default ISO date strings will parse correctly, for more robust parsing options see the extending schema types at the end of the readme. Inherits from `Schema`.

```highlight
let schema = yup.date();

await schema.isValid(new Date()); // => true
```

The default `cast` logic of `date` is pass the value to the `Date` constructor, failing that, it will attempt to parse the date as an ISO date string.

> If you would like ISO strings to not be cast to a `Date` object, use `.datetime()` instead.

Failed casts return an invalid Date.

#### `date.min(limit: Date | string | Ref, message?: string | function): Schema`

Set the minimum date allowed. When a string is provided it will attempt to cast to a date first and use the result as the limit.

#### `date.max(limit: Date | string | Ref, message?: string | function): Schema`

Set the maximum date allowed, When a string is provided it will attempt to cast to a date first and use the result as the limit.

### array

Define an array schema. Arrays can be typed or not, When specifying the element type, `cast` and `isValid` will apply to the elements as well. Options passed into `isValid` are also passed to child schemas.

Inherits from `Schema`.

```highlight
let schema = yup.array().of(yup.number().min(2));

await schema.isValid([2, 3]); // => true
await schema.isValid([1, -24]); // => false

schema.cast(['2', '3']); // => [2, 3]
```

You can also pass a subtype schema to the array constructor as a convenience.

```highlight
array().of(yup.number());
// or
array(yup.number());
```

Arrays have no default casting behavior.

#### `array.of(type: Schema): this`

Specify the schema of array elements. `of()` is optional and when omitted the array schema will not validate its contents.

#### `array.json(): this`

Attempt to parse input string values as JSON using `JSON.parse`.

#### `array.length(length: number | Ref, message?: string | function): this`

Set a specific length requirement for the array. The `${length}` interpolation can be used in the `message` argument.

#### `array.min(limit: number | Ref, message?: string | function): this`

Set a minimum length limit for the array. The `${min}` interpolation can be used in the `message` argument.

#### `array.max(limit: number | Ref, message?: string | function): this`

Set a maximum length limit for the array. The `${max}` interpolation can be used in the `message` argument.

#### `array.ensure(): this`

Ensures that the value is an array, by setting the default to `[]` and transforming `null` and `undefined` values to an empty array as well. Any non-empty, non-array value will be wrapped in an array.

```highlight
array().ensure().cast(null); // => []
array().ensure().cast(1); // => [1]
array().ensure().cast([1]); // => [1]
```

#### `array.compact(rejector: (value) => boolean): Schema`

Removes falsey values from the array. Providing a rejecter function lets you specify the rejection criteria yourself.

```highlight
array().compact().cast(['', 1, 0, 4, false, null]); // => [1, 4]

array()
  .compact(function (v) {
    return v == null;
  })
  .cast(['', 1, 0, 4, false, null]); // => ['', 1, 0, 4, false]
```

### tuple

Tuples, are fixed length arrays where each item has a distinct type.

Inherits from `Schema`.

```highlight
import { tuple, string, number, InferType } from 'yup';

let schema = tuple([
  string().label('name'),
  number().label('age').positive().integer(),
]);

await schema.validate(['James', 3]); // ['James', 3]

await schema.validate(['James', -24]); // => ValidationError: age must be a positive number

InferType<typeof schema> // [string, number] | undefined
```

tuples have no default casting behavior.

### object

Define an object schema. Options passed into `isValid` are also passed to child schemas. Inherits from `Schema`.

```highlight
yup.object({
  name: string().required(),
  age: number().required().positive().integer(),
  email: string().email(),
  website: string().url(),
});
```

object schema do not have any default transforms applied.

#### Object schema defaults

Object schema come with a default value already set, which "builds" out the object shape, a sets any defaults for fields:

```highlight
let schema = object({
  name: string().default(''),
});

schema.default(); // -> { name: '' }
```

This may be a bit surprising, but is usually helpful since it allows large, nested schema to create default values that fill out the whole shape and not just the root object. There is one gotcha! though. For nested object schema that are optional but include non optional fields may fail in unexpected ways:

```highlight
let schema = object({
  id: string().required(),
  names: object({
    first: string().required(),
  }),
});

schema.isValid({ id: 1 }); // false! names.first is required
```

This is because yup casts the input object before running validation which will produce:

> `{ id: '1', names: { first: undefined }}`

During the validation phase `names` exists, and is validated, finding `names.first` missing. If you wish to avoid this behavior do one of the following:

- Set the nested default to undefined: `names.default(undefined)`
- mark it nullable and default to null: `names.nullable().default(null)`

#### `object.shape(fields: object, noSortEdges?: Array<[string, string]>): Schema`

Define the keys of the object and the schemas for said keys.

Note that you can chain `shape` method, which acts like `Object.assign`.

```highlight
object({
  a: string(),
  b: number(),
}).shape({
  b: string(),
  c: number(),
});
```

would be exactly the same as:

```highlight
object({
  a: string(),
  b: string(),
  c: number(),
});
```

#### `object.json(): this`

Attempt to parse input string values as JSON using `JSON.parse`.

#### `object.concat(schemaB: ObjectSchema): ObjectSchema`

Creates a object schema, by applying all settings and fields from `schemaB` to the base, producing a new schema. The object shape is shallowly merged with common fields from `schemaB` taking precedence over the base fields.

#### `object.pick(keys: string[]): Schema`

Create a new schema from a subset of the original's fields.

```highlight
let person = object({
  age: number().default(30).required(),
  name: string().default('pat').required(),
  color: string().default('red').required(),
});

let nameAndAge = person.pick(['name', 'age']);
nameAndAge.getDefault(); // => { age: 30, name: 'pat'}
```

#### `object.omit(keys: string[]): Schema`

Create a new schema with fields omitted.

```highlight
let person = object({
  age: number().default(30).required(),
  name: string().default('pat').required(),
  color: string().default('red').required(),
});

let nameAndAge = person.omit(['color']);
nameAndAge.getDefault(); // => { age: 30, name: 'pat'}
```

#### `object.from(fromKey: string, toKey: string, alias: boolean = false): this`

Transforms the specified key to a new key. If `alias` is `true` then the old key will be left.

```highlight
let schema = object({
  myProp: mixed(),
  Other: mixed(),
})
  .from('prop', 'myProp')
  .from('other', 'Other', true);

schema.cast({ prop: 5, other: 6 }); // => { myProp: 5, other: 6, Other: 6 }
```

#### `object.exact(message?: string | function): Schema`

Validates that the object does not contain extra or unknown properties

#### `object.stripUnknown(): Schema`

The same as `object().validate(value, { stripUnknown: true})`, but as a transform method. When set any unknown properties will be removed.

#### `object.noUnknown(onlyKnownKeys: boolean = true, message?: string | function): Schema`

Validate that the object value only contains keys specified in `shape`, pass `false` as the first argument to disable the check. Restricting keys to known, also enables `stripUnknown` option, when not in strict mode.

> Watch Out!: this method performs a transform and a validation, which may produce unexpected results. For more explicit behavior use `object().stripUnknown` and `object().exact()`

#### `object.camelCase(): Schema`

Transforms all object keys to camelCase

#### `object.constantCase(): Schema`

Transforms all object keys to CONSTANT_CASE.
