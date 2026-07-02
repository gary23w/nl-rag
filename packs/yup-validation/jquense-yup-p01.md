---
title: "GitHub (part 1/2)"
source: https://github.com/jquense/yup
domain: yup-validation
license: CC-BY-SA-4.0
tags: yup validation, object schema validation, form schema, javascript validator
fetched: 2026-07-02
part: 1/2
---

# GitHub

jquense

/

yup

Public

- Notifications You must be signed in to change notification settings
- Fork 945
- Star

Branches

Tags

Open more actions menu


## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History805 Commits805 Commits |   |   |   |
| .github | .github |   |   |
| .yarn/patches | .yarn/patches |   |   |
| docs | docs |   |   |
| src | src |   |   |
| test | test |   |   |
| .babelrc.js | .babelrc.js |   |   |
| .eslintignore | .eslintignore |   |   |
| .eslintrc | .eslintrc |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .nvmrc | .nvmrc |   |   |
| .yarnrc.yml | .yarnrc.yml |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| LICENSE.md | LICENSE.md |   |   |
| README.md | README.md |   |   |
| package.json | package.json |   |   |
| renovate.json | renovate.json |   |   |
| rollup.config.js | rollup.config.js |   |   |
| test-setup.mjs | test-setup.mjs |   |   |
| tsconfig.json | tsconfig.json |   |   |
| vitest.config.ts | vitest.config.ts |   |   |
| yarn.lock | yarn.lock |   |   |
|   |   |   |   |


## Repository files navigation

# Yup

Yup is a schema builder for runtime value parsing and validation. Define a schema, transform a value to match, assert the shape of an existing value, or both. Yup schema are extremely expressive and allow modeling complex, interdependent validations, or value transformation.

> **You are viewing docs for the v1.0.0 of yup, pre-v1 docs are available: here**

**Killer Features**:

- Concise yet expressive schema interface, equipped to model simple to complex data models
- Powerful TypeScript support. Infer static types from schema, or ensure schema correctly implement a type
- Built-in async validation support. Model server-side and client-side validation equally well
- Extensible: add your own type-safe methods and schema
- Rich error details, make debugging a breeze
- Compatible with Standard Schema


## Getting Started

Schema are comprised of parsing actions (transforms) as well as assertions (tests) about the input value. Validate an input value to parse it and run the configured set of assertions. Chain together methods to build a schema.

```highlight
import { object, string, number, date, InferType } from 'yup';

let userSchema = object({
  name: string().required(),
  age: number().required().positive().integer(),
  email: string().email(),
  website: string().url().nullable(),
  createdOn: date().default(() => new Date()),
});

// parse and assert validity
let user = await userSchema.validate(await fetchUser());

type User = InferType<typeof userSchema>;
/* {
  name: string;
  age: number;
  email?: string | undefined
  website?: string | null | undefined
  createdOn: Date
}*/
```

Use a schema to coerce or "cast" an input value into the correct type, and optionally transform that value into more concrete and specific values, without making further assertions.

```highlight
// Attempts to coerce values to the correct type
let parsedUser = userSchema.cast({
  name: 'jimmy',
  age: '24',
  createdOn: '2014-09-23T19:25:25Z',
});
// ✅  { name: 'jimmy', age: 24, createdOn: Date }
```

Know that your input value is already parsed? You can "strictly" validate an input, and avoid the overhead of running parsing logic.

```highlight
// ❌  ValidationError "age is not a number"
let parsedUser = await userSchema.validate(
  {
    name: 'jimmy',
    age: '24',
  },
  { strict: true },
);
```


## Table of Contents

- Schema basics
  - Parsing: Transforms
  - Validation: Tests
    - Customizing errors
  - Composition and Reuse
- TypeScript integration
  - Schema defaults
  - Ensuring a schema matches an existing type
  - Extending built-in schema with new methods
  - TypeScript configuration
- Error message customization
  - localization and i18n
- Standard Schema Support
- API
  - `yup`
    - `reach(schema: Schema, path: string, value?: object, context?: object): Schema`
    - `addMethod(schemaType: Schema, name: string, method: ()=> Schema): void`
    - `ref(path: string, options: { contextPrefix: string }): Ref`
    - `lazy((value: any) => Schema): Lazy`
    - `ValidationError(errors: string | Array<string>, value: any, path: string)`
  - `Schema`
    - `Schema.clone(): Schema`
    - `Schema.label(label: string): Schema`
    - `Schema.meta(metadata: SchemaMetadata): Schema`
    - `Schema.describe(options?: ResolveOptions): SchemaDescription`
    - `Schema.concat(schema: Schema): Schema`
    - `Schema.validate(value: any, options?: object): Promise<InferType<Schema>, ValidationError>`
    - `Schema.validateSync(value: any, options?: object): InferType<Schema>`
    - `Schema.validateAt(path: string, value: any, options?: object): Promise<InferType<Schema>, ValidationError>`
    - `Schema.validateSyncAt(path: string, value: any, options?: object): InferType<Schema>`
    - `Schema.isValid(value: any, options?: object): Promise<boolean>`
    - `Schema.isValidSync(value: any, options?: object): boolean`
    - `Schema.cast(value: any, options = {}): InferType<Schema>`
    - `Schema.isType(value: any): value is InferType<Schema>`
    - `Schema.strict(enabled: boolean = false): Schema`
    - `Schema.strip(enabled: boolean = true): Schema`
    - `Schema.withMutation(builder: (current: Schema) => void): void`
    - `Schema.default(value: any): Schema`
    - `Schema.getDefault(options?: object): Any`
    - `Schema.nullable(message?: string | function): Schema`
    - `Schema.nonNullable(message?: string | function): Schema`
    - `Schema.defined(): Schema`
    - `Schema.optional(): Schema`
    - `Schema.required(message?: string | function): Schema`
    - `Schema.notRequired(): Schema`
    - `Schema.typeError(message: string): Schema`
    - `Schema.oneOf(arrayOfValues: Array<any>, message?: string | function): Schema` Alias: `equals`
    - `Schema.notOneOf(arrayOfValues: Array<any>, message?: string | function)`
    - `Schema.when(keys: string | string[], builder: object | (values: any[], schema) => Schema): Schema`
    - `Schema.test(name: string, message: string | function | any, test: function): Schema`
    - `Schema.test(options: object): Schema`
    - `Schema.transform((currentValue: any, originalValue: any, schema: Schema, options: object) => any): Schema`
  - mixed
  - string
    - `string.required(message?: string | function): Schema`
    - `string.length(limit: number | Ref, message?: string | function): Schema`
    - `string.min(limit: number | Ref, message?: string | function): Schema`
    - `string.max(limit: number | Ref, message?: string | function): Schema`
    - `string.matches(regex: Regex, message?: string | function): Schema`
    - `string.matches(regex: Regex, options: { message: string, excludeEmptyString: bool }): Schema`
    - `string.email(message?: string | function): Schema`
    - `string.url(message?: string | function): Schema`
    - `string.uuid(message?: string | function): Schema`
    - `string.datetime(options?: {message?: string | function, allowOffset?: boolean, precision?: number})`
    - `string.datetime(message?: string | function)`
    - `string.ensure(): Schema`
    - `string.trim(message?: string | function): Schema`
    - `string.lowercase(message?: string | function): Schema`
    - `string.uppercase(message?: string | function): Schema`
  - number
    - `number.min(limit: number | Ref, message?: string | function): Schema`
    - `number.max(limit: number | Ref, message?: string | function): Schema`
    - `number.lessThan(max: number | Ref, message?: string | function): Schema`
    - `number.moreThan(min: number | Ref, message?: string | function): Schema`
    - `number.positive(message?: string | function): Schema`
    - `number.negative(message?: string | function): Schema`
    - `number.integer(message?: string | function): Schema`
    - `number.truncate(): Schema`
    - `number.round(type: 'floor' | 'ceil' | 'trunc' | 'round' = 'round'): Schema`
  - boolean
  - date
    - `date.min(limit: Date | string | Ref, message?: string | function): Schema`
    - `date.max(limit: Date | string | Ref, message?: string | function): Schema`
  - array
    - `array.of(type: Schema): this`
    - `array.json(): this`
    - `array.length(length: number | Ref, message?: string | function): this`
    - `array.min(limit: number | Ref, message?: string | function): this`
    - `array.max(limit: number | Ref, message?: string | function): this`
    - `array.ensure(): this`
    - `array.compact(rejector: (value) => boolean): Schema`
  - tuple
  - object
    - Object schema defaults
    - `object.shape(fields: object, noSortEdges?: Array<[string, string]>): Schema`
    - `object.json(): this`
    - `object.concat(schemaB: ObjectSchema): ObjectSchema`
    - `object.pick(keys: string[]): Schema`
    - `object.omit(keys: string[]): Schema`
    - `object.from(fromKey: string, toKey: string, alias: boolean = false): this`
    - `object.exact(message?: string | function): Schema`
    - `object.stripUnknown(): Schema`
    - `object.noUnknown(onlyKnownKeys: boolean = true, message?: string | function): Schema`
    - `object.camelCase(): Schema`
    - `object.constantCase(): Schema`


## Schema basics

Schema definitions, are comprised of parsing "transforms" which manipulate inputs into the desired shape and type, "tests", which make assertions over parsed data. Schema also store a bunch of "metadata", details about the schema itself, which can be used to improve error messages, build tools that dynamically consume schema, or serialize schema into another format.

In order to be maximally flexible yup allows running both parsing and assertions separately to match specific needs

### Parsing: Transforms

Each built-in type implements basic type parsing, which comes in handy when parsing serialized data, such as JSON. Additionally types implement type specific transforms that can be enabled.

```highlight
let num = number().cast('1'); // 1

let obj = object({
  firstName: string().lowercase().trim(),
})
  .json()
  .camelCase()
  .cast('{"first_name": "jAnE "}'); // { firstName: 'jane' }
```

Custom transforms can be added

```highlight
let reversedString = string()
  .transform((currentValue) => currentValue.split('').reverse().join(''))
  .cast('dlrow olleh'); // "hello world"
```

Transforms form a "pipeline", where the value of a previous transform is piped into the next one. When an input value is `undefined` yup will apply the schema default if it's configured.

> Watch out! values are not guaranteed to be valid types in transform functions. Previous transforms may have failed. For example a number transform may be receive the input value, `NaN`, or a number.

### Validation: Tests

Yup schema run "tests" over input values. Tests assert that inputs conform to some criteria. Tests are distinct from transforms, in that they do not change or alter the input (or its type) and are usually reserved for checks that are hard, if not impossible, to represent in static types.

```highlight
string()
  .min(3, 'must be at least 3 characters long')
  .email('must be a valid email')
  .validate('no'); // ValidationError
```

As with transforms, tests can be customized on the fly

```highlight
let jamesSchema = string().test(
  'is-james',
  (d) => `${d.path} is not James`,
  (value) => value == null || value === 'James',
);

jamesSchema.validateSync('James'); // "James"

jamesSchema.validateSync('Jane'); // ValidationError "this is not James"
```

> Heads up: unlike transforms, `value` in a custom test is guaranteed to be the correct type (in this case an optional string). It still may be `undefined` or `null` depending on your schema in those cases, you may want to return `true` for absent values unless your transform makes presence related assertions. The test option `skipAbsent` will do this for you if set.

#### Customizing errors

In the simplest case a test function returns `true` or `false` depending on the whether the check passed. In the case of a failing test, yup will throw a `ValidationError` with your (or the default) message for that test. ValidationErrors also contain a bunch of other metadata about the test, including it's name, what arguments (if any) it was called with, and the path to the failing field in the case of a nested validation.

Error messages can also be constructed on the fly to customize how the schema fails.

```highlight
let order = object({
  no: number().required(),
  sku: string().test({
    name: 'is-sku',
    skipAbsent: true,
    test(value, ctx) {
      if (!value.startsWith('s-')) {
        return ctx.createError({ message: 'SKU missing correct prefix' });
      }
      if (!value.endsWith('-42a')) {
        return ctx.createError({ message: 'SKU missing correct suffix' });
      }
      if (value.length < 10) {
        return ctx.createError({ message: 'SKU is not the right length' });
      }
      return true;
    },
  }),
});

order.validate({ no: 1234, sku: 's-1a45-14a' });
```

### Composition and Reuse

Schema are immutable, each method call returns a new schema object. Reuse and pass them around without fear of mutating another instance.

```highlight
let optionalString = string().optional();

let definedString = optionalString.defined();

let value = undefined;
optionalString.isValid(value); // true
definedString.isValid(value); // false
```


## TypeScript integration

Yup schema produce static TypeScript interfaces. Use `InferType` to extract that interface:

```highlight
import * as yup from 'yup';

let personSchema = yup.object({
  firstName: yup.string().defined(),
  nickName: yup.string().default('').nullable(),
  sex: yup
    .mixed()
    .oneOf(['male', 'female', 'other'] as const)
    .defined(),
  email: yup.string().nullable().email(),
  birthDate: yup.date().nullable().min(new Date(1900, 0, 1)),
});

interface Person extends yup.InferType<typeof personSchema> {
  // using interface instead of type generally gives nicer editor feedback
}
```

### Schema defaults

A schema's default is used when casting produces an `undefined` output value. Because of this, setting a default affects the output type of the schema, essentially marking it as "defined()".

```highlight
import { string } from 'yup';

let value: string = string().default('hi').validate(undefined);

// vs

let value: string | undefined = string().validate(undefined);
```

### Ensuring a schema matches an existing type

In some cases a TypeScript type already exists, and you want to ensure that your schema produces a compatible type:

```highlight
import { object, number, string, ObjectSchema } from 'yup';

interface Person {
  name: string;
  age?: number;
  sex: 'male' | 'female' | 'other' | null;
}

// will raise a compile-time type error if the schema does not produce a valid Person
let schema: ObjectSchema<Person> = object({
  name: string().defined(),
  age: number().optional(),
  sex: string<'male' | 'female' | 'other'>().nullable().defined(),
});

// ❌ errors:
// "Type 'number | undefined' is not assignable to type 'string'."
let badSchema: ObjectSchema<Person> = object({
  name: number(),
});
```

### Extending built-in schema with new methods

You can use TypeScript's interface merging behavior to extend the schema types if needed. Type extensions should go in an "ambient" type definition file such as your `globals.d.ts`. Remember to actually extend the yup type in your application code!

> Watch out! merging only works if the type definition is *exactly* the same, including generics. Consult the yup source code for each type to ensure you are defining it correctly

```highlight
// globals.d.ts
declare module 'yup' {
  interface StringSchema<TType, TContext, TDefault, TFlags> {
    append(appendStr: string): this;
  }
}

// app.ts
import { addMethod, string } from 'yup';

addMethod(string, 'append', function append(appendStr: string) {
  return this.transform((value) => `${value}${appendStr}`);
});

string().append('~~~~').cast('hi'); // 'hi~~~~'
```

### TypeScript configuration

You **must** have the `strictNullChecks` compiler option enabled for type inference to work.

We also recommend settings `strictFunctionTypes` to `false`, for functionally better types. Yes this reduces overall soundness, however TypeScript already disables this check for methods and constructors (note from TS docs):

> During development of this feature, we discovered a large number of inherently unsafe class hierarchies, including some in the DOM. Because of this, the setting only applies to functions written in function syntax, not to those in method syntax:

Your mileage will vary, but we've found that this check doesn't prevent many of real bugs, while increasing the amount of onerous explicit type casting in apps.


## Error message customization

Default error messages can be customized for when no message is provided with a validation test. If any message is missing in the custom dictionary the error message will default to Yup's one.

```highlight
import { setLocale } from 'yup';

setLocale({
  mixed: {
    default: 'Não é válido',
  },
  number: {
    min: 'Deve ser maior que ${min}',
  },
});

// now use Yup schemas AFTER you defined your custom dictionary
let schema = yup.object().shape({
  name: yup.string(),
  age: yup.number().min(18),
});

try {
  await schema.validate({ name: 'jimmy', age: 11 });
} catch (err) {
  err.name; // => 'ValidationError'
  err.errors; // => ['Deve ser maior que 18']
}
```

### localization and i18n

If you need multi-language support, yup has got you covered. The function `setLocale` accepts functions that can be used to generate error objects with translation keys and values. These can be fed it into your favorite i18n library.

```highlight
import { setLocale } from 'yup';

setLocale({
  // use constant translation keys for messages without values
  mixed: {
    default: 'field_invalid',
  },
  // use functions to generate an error object that includes the value from the schema
  number: {
    min: ({ min }) => ({ key: 'field_too_short', values: { min } }),
    max: ({ max }) => ({ key: 'field_too_big', values: { max } }),
  },
});

// ...

let schema = yup.object().shape({
  name: yup.string(),
  age: yup.number().min(18),
});

try {
  await schema.validate({ name: 'jimmy', age: 11 });
} catch (err) {
  messages = err.errors.map((err) => i18next.t(err.key));
}
```


## Standard Schema Support

Yup is compatible with Standard Schema.
