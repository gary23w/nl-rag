---
title: "joi.dev"
source: https://joi.dev/
domain: joi-validation
license: CC-BY-SA-4.0
tags: joi validation, object schema description, node validator, input constraint
fetched: 2026-07-02
---

# joi

The most powerful schema description language and data validator for JavaScript

Get started with joi

Try it in the sandbox

## Expressive

**Over 150 built-in validators** across strings, numbers, dates, arrays, objects, binaries, and more — with chainable rules that read like English.

## Declarative

**Describe complex relationships between fields** without writing callback logic. Cross-field references, conditional schemas, and key dependencies — all as one-liners.

## Extensible

**Build your own schema types** with Joi's extension system. Add custom rules, coercions, and chainable methods — then share them as plugins.

## Get started in seconds 

console

```console
npm install joi
```

1

console

```console
yarn add joi
```

1

console

```console
pnpm add joi
```

1

js

```js
import Joi from 'joi';

const schema = Joi.object({
    username: Joi.string().alphanum().min(3).max(30).required(),
    email: Joi.string().email().required(),
    age: Joi.number().integer().min(18),
});

const { error, value } = schema.validate({
    username: 'danilo',
    email: 'danilo@example.com',
    age: 28,
});
```

1

2

3

4

5

6

7

8

9

10

11

12

13

## Built for real-world validation 

### 1. Schema Variants with `.alter()` + `.tailor()` 

Define one schema. Produce specialized versions for different contexts — like separate validation for `GET` vs `POST` — without duplicating anything.

js

```js
const schema = Joi.object({
    id: Joi.number().alter({
        create: (s) => s.forbidden(),
        update: (s) => s.required(),
    }),
    name: Joi.string().required(),
});

const createSchema = schema.tailor('create');
const updateSchema = schema.tailor('update');
```

1

2

3

4

5

6

7

8

9

10

*One source of truth. No drift between schemas.*

### 2. Declarative Field Dependencies 

Express relationships between fields without writing validation logic. Joi handles the permutations.

js

```js
const schema = Joi.object({
    email: Joi.string().email(),
    phone: Joi.string().pattern(/^\+?[0-9]{7,15}$/),
    address: Joi.string(),
})
    .or('email', 'phone') // at least one contact method
    .with('phone', 'address') // phone requires address
    .xor('email', 'phone'); // but not both
```

1

2

3

4

5

6

7

8

*Seven dependency methods: `.with()`, `.without()`, `.or()`, `.and()`, `.xor()`, `.oxor()`, `.nand()`.*

### 3. Cross-Field References 

Reference other fields directly in validation rules. No callbacks, no workarounds.

js

```js
const schema = Joi.object({
    startDate: Joi.date().required(),
    endDate: Joi.date().greater(Joi.ref('startDate')).required(),
    password: Joi.string().min(8).required(),
    confirm: Joi.any().valid(Joi.ref('password')).required(),
});
```

1

2

3

4

5

6

*References support relative paths, value transforms, and even context variables.*

### 4. Rich, Actionable Errors 

Every validation failure includes the exact path, a machine-readable type code, the failing value, and the constraint that was violated. Use `.annotate()` to visualize errors in context.

js

```js
const { error } = schema.validate(data, { abortEarly: false });
// error.details → [
//   {
//     message: '"age" must be greater than or equal to 18',
//     path: ['age'],
//     type: 'number.min',
//     context: { limit: 18, value: 12, label: 'age', key: 'age' }
//   }
// ]
```

1

2

3

4

5

6

7

8

9

*Type codes like `string.email`, `number.min`, `any.required` make programmatic error handling straightforward.*
