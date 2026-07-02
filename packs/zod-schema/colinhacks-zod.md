---
title: "GitHub"
source: https://github.com/colinhacks/zod
domain: zod-schema
license: CC-BY-SA-4.0
tags: zod schema, typescript validation, schema inference, runtime type checking
fetched: 2026-07-02
---

# GitHub

colinhacks

/

zod

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 2k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History2,927 Commits2,927 Commits |   |   |   |
| .configs | .configs |   |   |
| .devcontainer | .devcontainer |   |   |
| .github/workflows | .github/workflows |   |   |
| .husky | .husky |   |   |
| .vscode | .vscode |   |   |
| logo | logo |   |   |
| packages | packages |   |   |
| rfcs | rfcs |   |   |
| scripts | scripts |   |   |
| wiki | wiki |   |   |
| .cursorrules | .cursorrules |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| .mcp.json | .mcp.json |   |   |
| .nojekyll | .nojekyll |   |   |
| .npmrc | .npmrc |   |   |
| .nvmrc | .nvmrc |   |   |
| AGENTS.md | AGENTS.md |   |   |
| CLAUDE.md | CLAUDE.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| FUNDING.yml | FUNDING.yml |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| biome.jsonc | biome.jsonc |   |   |
| logo.svg | logo.svg |   |   |
| package.json | package.json |   |   |
| play.ts | play.ts |   |   |
| pnpm-lock.yaml | pnpm-lock.yaml |   |   |
| pnpm-workspace.yaml | pnpm-workspace.yaml |   |   |
| tea.yaml | tea.yaml |   |   |
| tsconfig.json | tsconfig.json |   |   |
| vitest.config.ts | vitest.config.ts |   |   |
| vitest.root.mjs | vitest.root.mjs |   |   |
|   |   |   |   |

## Repository files navigation

(Zod logo)

# Zod

TypeScript-first schema validation with static type inference by @colinhacks

(Zod CI status) (License) (npm) (discord server) (stars)

Docs

•

Discord

•

𝕏

•

Bluesky

### Read the docs →

## What is Zod?

Zod is a TypeScript-first validation library. Define a schema and parse some data with it. You'll get back a strongly typed, validated result.

```highlight
import * as z from "zod";

const User = z.object({
  name: z.string(),
});

// some untrusted data...
const input = {
  /* stuff */
};

// the parsed result is validated and type safe!
const data = User.parse(input);

// so you can use it with confidence :)
console.log(data.name);
```

## Features

- Zero external dependencies
- Works in Node.js and all modern browsers
- Tiny: `2kb` core bundle (gzipped)
- Immutable API: methods return a new instance
- Concise interface
- Works with TypeScript and plain JS
- Built-in JSON Schema conversion
- Extensive ecosystem

## Installation

```highlight
npm install zod
```

## Basic usage

Before you can do anything else, you need to define a schema. For the purposes of this guide, we'll use a simple object schema.

```highlight
import * as z from "zod";

const Player = z.object({
  username: z.string(),
  xp: z.number(),
});
```

### Parsing data

Given any Zod schema, use `.parse` to validate an input. If it's valid, Zod returns a strongly-typed *deep clone* of the input.

```highlight
Player.parse({ username: "billie", xp: 100 });
// => returns { username: "billie", xp: 100 }
```

**Note** — If your schema uses certain asynchronous APIs like `async` refinements or transforms, you'll need to use the `.parseAsync()` method instead.

```highlight
const schema = z.string().refine(async (val) => val.length <= 8);

await schema.parseAsync("hello");
// => "hello"
```

### Handling errors

When validation fails, the `.parse()` method will throw a `ZodError` instance with granular information about the validation issues.

```highlight
try {
  Player.parse({ username: 42, xp: "100" });
} catch (err) {
  if (err instanceof z.ZodError) {
    err.issues;
    /* [
      {
        expected: 'string',
        code: 'invalid_type',
        path: [ 'username' ],
        message: 'Invalid input: expected string'
      },
      {
        expected: 'number',
        code: 'invalid_type',
        path: [ 'xp' ],
        message: 'Invalid input: expected number'
      }
    ] */
  }
}
```

To avoid a `try/catch` block, you can use the `.safeParse()` method to get back a plain result object containing either the successfully parsed data or a `ZodError`. The result type is a discriminated union, so you can handle both cases conveniently.

```highlight
const result = Player.safeParse({ username: 42, xp: "100" });
if (!result.success) {
  result.error; // ZodError instance
} else {
  result.data; // { username: string; xp: number }
}
```

**Note** — If your schema uses certain asynchronous APIs like `async` refinements or transforms, you'll need to use the `.safeParseAsync()` method instead.

```highlight
const schema = z.string().refine(async (val) => val.length <= 8);

await schema.safeParseAsync("hello");
// => { success: true; data: "hello" }
```

### Inferring types

Zod infers a static type from your schema definitions. You can extract this type with the `z.infer<>` utility and use it however you like.

```highlight
const Player = z.object({
  username: z.string(),
  xp: z.number(),
});

// extract the inferred type
type Player = z.infer<typeof Player>;

// use it in your code
const player: Player = { username: "billie", xp: 100 };
```

In some cases, the input & output types of a schema can diverge. For instance, the `.transform()` API can convert the input from one type to another. In these cases, you can extract the input and output types independently:

```highlight
const mySchema = z.string().transform((val) => val.length);

type MySchemaIn = z.input<typeof mySchema>;
// => string

type MySchemaOut = z.output<typeof mySchema>; // equivalent to z.infer<typeof mySchema>
// number
```
