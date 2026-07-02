---
title: "Intro"
source: https://zod.dev/
domain: zod-schema
license: CC-BY-SA-4.0
tags: zod schema, typescript validation, schema inference, runtime type checking
fetched: 2026-07-02
---

# Zod

TypeScript-first schema validation with static type inference by @colinhacks

Website

•

Discord

•

𝕏

•

Bluesky

Zod 4 is stable. Read the release notes and migration guide.

## Introduction

Zod is a TypeScript-first validation library. Using Zod, you can define *schemas* you can use to validate data, from a simple `string` to a complex nested object.

```
import * as z from "zod";
 
const User = z.object({
  name: z.string(),
});
 
// some untrusted data...
const input = { /* stuff */ };
 
// the parsed result is validated and type safe!
const data = User.parse(input);
 
// so you can use it with confidence :)
console.log(data.name);
```

## Features

- Zero external dependencies
- Works in Node.js and all modern browsers
- Tiny: 2kb core bundle (gzipped)
- Immutable API: methods return a new instance
- Concise interface
- Works with TypeScript and plain JS
- Built-in JSON Schema conversion
- Extensive ecosystem

## Installation

```
npm install zod
```

Zod is also available as `@zod/zod` on jsr.io.

Zod provides an MCP server that can be used by agents to search Zod's docs. To add to your editor, follow these instructions. Zod also provides an llms.txt file.

## Requirements

Zod is tested against *TypeScript v5.5* and later. Older versions may work but are not officially supported.

### `"strict"`

You must enable `strict` mode in your `tsconfig.json`. This is a best practice for all TypeScript projects.

```
// tsconfig.json
{
  // ...
  "compilerOptions": {
    // ...
    "strict": true
  }
}
```

## Ecosystem

Zod has a thriving ecosystem of libraries, tools, and integrations. Refer to the Ecosystem page for a complete list of libraries that support Zod or are built on top of it.

- Resources
- API Libraries
- Form Integrations
- Zod to X
- X to Zod
- Mocking Libraries
- Powered by Zod

I also contribute to the following projects, which I'd like to highlight:

- tRPC - End-to-end typesafe APIs, with support for Zod schemas
- React Hook Form - Hook-based form validation with a Zod resolver
- zshy - Originally created as Zod's internal build tool. Bundler-free, batteries-included build tool for TypeScript libraries. Powered by `tsc`.

## Sponsors

Sponsorship at any level is appreciated and encouraged. If you built a paid product using Zod, consider one of the corporate tiers.

### Platinum

Cut code review time & bugs in half

coderabbit.ai

### Gold

Social APIs for developers and AI agents

zernio.com

Serverless Postgres — Ship faster

neon.tech

Generate best-in-class SDKs

stainlessapi.com

### Silver

sanity.io

subtotal.com

nitric.io

propelauth.com

cerbos.dev

scalar.com

transloadit.com

whop.com

cryptojobslist.com

plain.com

inngest.com

storyblok.com

mux.link/zod

cybozu.co.jp

9thco.com

ferry.health

### Bronze

github.com/jasonLaster

clipboardhealth.com/engineering

convex.dev

n8n.io
