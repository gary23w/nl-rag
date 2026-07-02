---
title: "GitHub"
source: https://github.com/trpc/trpc
domain: trpc-typesafe
license: CC-BY-SA-4.0
tags: trpc typesafe, end-to-end type safety, typescript rpc, typed api procedure
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

trpc

/

trpc

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 1.6k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History4,898 Commits4,898 Commits |   |   |   |
| .cursor/rules | .cursor/rules |   |   |
| .github | .github |   |   |
| .superset | .superset |   |   |
| .vscode | .vscode |   |   |
| _artifacts | _artifacts |   |   |
| examples | examples |   |   |
| packages | packages |   |   |
| scripts | scripts |   |   |
| www | www |   |   |
| .coderabbit.yaml | .coderabbit.yaml |   |   |
| .dockerignore | .dockerignore |   |   |
| .gitignore | .gitignore |   |   |
| .kodiak.toml | .kodiak.toml |   |   |
| .npmrc | .npmrc |   |   |
| .nvmrc | .nvmrc |   |   |
| .prettierignore | .prettierignore |   |   |
| .tool-versions | .tool-versions |   |   |
| .ts-prunerc | .ts-prunerc |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| codecov.yml | codecov.yml |   |   |
| eslint.config.js | eslint.config.js |   |   |
| lerna.json | lerna.json |   |   |
| package.json | package.json |   |   |
| pnpm-lock.yaml | pnpm-lock.yaml |   |   |
| pnpm-workspace.yaml | pnpm-workspace.yaml |   |   |
| prettier.config.js | prettier.config.js |   |   |
| tsconfig.build.json | tsconfig.build.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
| turbo.json | turbo.json |   |   |
| vitest.config.ts | vitest.config.ts |   |   |
|   |   |   |   |

## Repository files navigation

# tRPC

### Move fast and break nothing. End-to-end typesafe APIs made easy.

The client above is **not** importing any code from the server, only its type declarations.

## Intro

tRPC allows you to easily build & consume fully typesafe APIs without schemas or code generation.

### Features

- ✅  Well-tested and production ready.
- 🧙‍♂️  Full static typesafety & autocompletion on the client, for inputs, outputs, and errors.
- 🐎  Snappy DX - No code generation, run-time bloat, or build pipeline.
- 🍃  Light - tRPC has zero deps and a tiny client-side footprint.
- 🐻  Easy to add to your existing brownfield project.
- 🔋  Batteries included - React.js/Next.js/Express.js/Fastify adapters. *(But tRPC is not tied to React, and there are many community adapters for other libraries)*
- 🥃  Subscriptions support.
- ⚡️  Request batching - requests made at the same time can be automatically combined into one
- 👀  Quite a few examples in the ./examples-folder

## Quickstart

There are a few examples that you can use for playing out with tRPC or bootstrapping your new project. For example, if you want a Next.js app, you can use the full-stack Next.js example:

**Quick start with a full-stack Next.js example:**

```highlight
# yarn
yarn create next-app --example https://github.com/trpc/trpc --example-path examples/next-prisma-starter trpc-prisma-starter

# npm
npx create-next-app --example https://github.com/trpc/trpc --example-path examples/next-prisma-starter trpc-prisma-starter

# pnpm
pnpm create next-app --example https://github.com/trpc/trpc --example-path examples/next-prisma-starter trpc-prisma-starter

# bun
bunx create-next-app --example https://github.com/trpc/trpc --example-path examples/next-prisma-starter trpc-prisma-starter

# deno
deno init --npm next-app --example https://github.com/trpc/trpc --example-path examples/next-prisma-starter trpc-prisma-starter
```

**👉 See full documentation on tRPC.io. 👈**

## AI Agents

If you use an AI coding agent (Claude Code, Cursor, Windsurf, etc.), install tRPC skills for better code generation:

```highlight
npx @tanstack/intent@latest install
```

## Star History

(Star History Chart)

## Core Team

> Do you want to contribute? First, read the Contributing Guidelines before opening an issue or PR so you understand the branching strategy and local development environment. If you need any more guidance or want to ask more questions, feel free to write to us on Discord!

### Project leads

> The people who lead the API-design decisions and have the most active role in the development

| Alex / KATT | Julius Marminge | Nick Lucas |
|---|---|---|

### Active contributors

> People who actively help out improving the codebase by making PRs and reviewing code

| Matthieu Hocquart |
|---|

### Special shout-outs

> Individuals who have made exceptional contributions to tRPC through code, documentation, community building, and other valuable efforts

| Theo Browne | Sachin Raja |
|---|---|

## Sponsors

If you enjoy working with tRPC and want to support us, consider giving a token appreciation by GitHub Sponsors!

### 🥈 Silver Sponsors

| (Greptile) Greptile | (CodeRabbit) CodeRabbit | (SerpApi) SerpApi |
|---|---|---|

### 😻 Smaller Backers

| (Ahoy%20Labs) Ahoy Labs | (Unkey) Unkey | (Dr.%20B) Dr. B | (Proxidize) Proxidize | (Ferry%20Health) Ferry Health | (Liminity%20AB) Liminity AB |
|---|---|---|---|---|---|
| (Ryan%20Magoon) Ryan Magoon | (BestKru) BestKru | (Max%20Greenwald) Max Greenwald | (Dmitry%20Maykov) Dmitry Maykov | (Chris%20Bradley) Chris Bradley | (fanvue) fanvue |
| (Drew%20Powers) Drew Powers | (Drizzle%20Team) Drizzle Team | (Spencer%20McKenney) Spencer McKenney | (Kalle) Kalle | (Maicon%20Carraro) Maicon Carraro | (Andrei%20Karushev) Andrei Karushev |
| (Stefan%20Wallin) Stefan Wallin | (Venue%20Ink) Venue Ink | (Aerius%20Ventilation%20AB) Aerius Ventilation AB | (Stefan%20Smiljkovic) Stefan Smiljkovic | (Netrouting.com) Netrouting.com | (Erik%20Bj%C3%A4reholt) Erik Bjäreholt |

## All contributors ✨

(A table of avatars from the project's contributors)

(Powered by Vercel)
