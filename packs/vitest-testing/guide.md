---
title: "Getting Started"
source: https://vitest.dev/guide/
domain: vitest-testing
license: CC-BY-SA-4.0
tags: vitest testing, vite-native test runner, unit test framework, javascript test assertions
fetched: 2026-07-02
---

# Getting Started

Are you an LLM? You can read better optimized documentation at /guide.md for this page in Markdown format

# Getting Started 

## Overview 

Vitest (pronounced as *"veetest"*) is a next generation testing framework powered by Vite.

You can learn more about the rationale behind the project in the Why Vitest section.

## Trying Vitest Online 

You can try Vitest online on StackBlitz. It runs Vitest directly in the browser, and it is almost identical to the local setup but doesn't require installing anything on your machine.

## Adding Vitest to Your Project 

Learn how to install by Video

bash

```bash
npm install -D vitest
```

bash

```bash
yarn add -D vitest
```

bash

```bash
pnpm add -D vitest
```

bash

```bash
bun add -D vitest
```

TIP

Vitest requires Vite >=v6.0.0 and Node >=v20.0.0

It is recommended that you install a copy of `vitest` in your `package.json`, using one of the methods listed above. However, if you would prefer to run `vitest` directly, you can use `npx vitest` (the `npx` tool comes with npm and Node.js).

The `npx` tool will execute the specified command. By default, `npx` will first check if the command exists in the local project's binaries. If it is not found there, `npx` will look in the system's `$PATH` and execute it if found. If the command is not found in either location, `npx` will install it in a temporary location prior to execution.

## Writing Tests 

As an example, we will write a simple test that verifies the output of a function that adds two numbers.

sum.js

```
export function sum(a, b) {
  return a + b
}
```

sum.test.js

```
import { expect, test } from 'vitest'
import { sum } from './sum.js'

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3)
})
```

TIP

By default, tests must contain `.test.` or `.spec.` in their file name.

Next, in order to execute the test, add the following section to your `package.json`:

package.json

json

```json
{
  "scripts": {
    "test": "vitest"
  }
}
```

Finally, run `npm run test`, `yarn test` or `pnpm test`, depending on your package manager, and Vitest will print this message:

txt

```txt
✓ sum.test.js (1)
  ✓ adds 1 + 2 to equal 3

Test Files  1 passed (1)
     Tests  1 passed (1)
  Start at  02:15:44
  Duration  311ms
```

WARNING

If you are using Bun as your package manager, make sure to use `bun run test` command instead of `bun test`, otherwise Bun will run its own test runner.

Your first test is passing! Continue to Writing Tests to learn about organizing tests, reading test output, and the core testing patterns you'll use every day.

To run tests once without watching for file changes, use `vitest run`. You can also pass additional flags like `--reporter` or `--coverage`. For a full list of CLI options, run `npx vitest --help` or see the CLI guide.

## Configuring Vitest 

Vitest reads your `vite.config.*` by default, so your existing Vite plugins and configuration work out-of-the-box. You can also create a dedicated `vitest.config.*` for test-specific settings. See the Config Reference for details.

## IDE Integrations 

We also provided an official extension for Visual Studio Code to enhance your testing experience with Vitest.

Install from VS Code Marketplace

Learn more about IDE Integrations

## Examples 

| Example | Source | Playground |
|---|---|---|
| `basic` | GitHub | Play Online |
| `fastify` | GitHub | Play Online |
| `in-source-test` | GitHub | Play Online |
| `lit` | GitHub | Play Online |
| `vue` | GitHub | Play Online |
| `marko` | GitHub | Play Online |
| `preact` | GitHub | Play Online |
| `qwik` | GitHub | Play Online |
| `react` | GitHub | Play Online |
| `solid` | GitHub | Play Online |
| `svelte` | GitHub | Play Online |
| `profiling` | GitHub | Not Available |
| `typecheck` | GitHub | Play Online |
| `projects` | GitHub | Play Online |

## Community 

If you have questions or need help, reach out to the community at Discord and GitHub Discussions.
