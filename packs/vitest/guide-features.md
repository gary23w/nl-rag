---
title: "Features"
source: https://vitest.dev/guide/features
domain: vitest
license: CC-BY-SA-4.0
tags: vitest runner, vite testing, javascript testing, test mocking
fetched: 2026-07-02
---

# Features

Are you an LLM? You can read better optimized documentation at /guide/features.md for this page in Markdown format

# Features 

- Vite's config, transformers, resolvers, and plugins
- Use the same setup from your app to run the tests!
- Smart & instant watch mode, like HMR for tests!
- Component testing for Vue, React, Svelte, Lit, Marko and more
- Out-of-the-box TypeScript / JSX support
- ESM first, top level await
- Benchmarking support with Tinybench
- Filtering, timeouts, concurrent for suite and tests
- Projects support
- Jest-compatible Snapshot
- Chai built-in for assertions + Jest expect compatible APIs
- Jest-compatible mocking
- happy-dom or jsdom for DOM mocking
- Browser Mode for running component tests in the browser
- Code coverage via v8 or istanbul
- Rust-like in-source testing
- Type Testing via expect-type
- Sharding Support
- Reporting Uncaught Errors

Learn how to write your first test by Video

TIP

This page is a high-level overview of Vitest's capabilities. If you're new to Vitest, we recommend reading the Learn tutorial first for a hands-on introduction.

## Shared Config between Test, Dev and Build 

Vite's config, transformers, resolvers, and plugins. Use the same setup from your app to run the tests.

Learn more at Configuring Vitest.

## Watch Mode 

bash

```bash
$ vitest
```

When you modify your source code or the test files, Vitest smartly searches the module graph and only reruns the related tests, just like how HMR works in Vite!

`vitest` starts in `watch mode` **by default in development environment** and `run mode` in CI environment (when `process.env.CI` presents) smartly. You can use `vitest watch` or `vitest run` to explicitly specify the desired mode.

Start Vitest with the `--standalone` flag to keep it running in the background. It won't run any tests until they change. Vitest will not run tests if the source code is changed until the test that imports the source has been run

## Common Web Idioms Out-Of-The-Box 

Out-of-the-box ES Module / TypeScript / JSX support / PostCSS

## Threads 

By default Vitest runs test files in multiple processes using `node:child_process`, allowing tests to run simultaneously. If you want to speed up your test suite even further, consider enabling `--pool=threads` to run tests using `node:worker_threads` (beware that some packages might not work with this setup). To run tests in a single thread or process, see `fileParallelism`.

Vitest also isolates each file's environment so env mutations in one file don't affect others. Isolation can be disabled by passing `--no-isolate` to the CLI (trading correctness for run performance).

## Test Filtering 

Vitest provides many ways to narrow down the tests to run in order to speed up testing so you can focus on development.

Learn more about Test Filtering.

## Running Tests Concurrently 

Use `.concurrent` in consecutive tests to start them in parallel.

ts

```ts
import { describe, it } from 'vitest'

// The two tests marked with concurrent will be started in parallel
describe('suite', () => {
  it('serial test', async () => { /* ... */ })
  it.concurrent('concurrent test 1', async ({ expect }) => { /* ... */ })
  it.concurrent('concurrent test 2', async ({ expect }) => { /* ... */ })
})
```

If you use `.concurrent` on a suite, every test in it will be started in parallel.

ts

```ts
import { describe, it } from 'vitest'

// All tests within this suite will be started in parallel
describe.concurrent('suite', () => {
  it('concurrent test 1', async ({ expect }) => { /* ... */ })
  it('concurrent test 2', async ({ expect }) => { /* ... */ })
  it.concurrent('concurrent test 3', async ({ expect }) => { /* ... */ })
})
```

You can also use `.skip`, `.only`, and `.todo` with concurrent suites and tests. Read more in the API Reference.

WARNING

When running concurrent tests, Snapshots and Assertions must use `expect` from the local Test Context to ensure the right test is detected.

## Snapshot 

Jest-compatible snapshot support.

ts

```ts
import { expect, it } from 'vitest'

it('renders correctly', () => {
  const result = render()
  expect(result).toMatchSnapshot()
})
```

Learn more at Snapshot.

## Chai and Jest `expect` Compatibility 

Chai is built-in for assertions with Jest `expect`-compatible APIs.

Notice that if you are using third-party libraries that add matchers, setting `test.globals` to `true` will provide better compatibility.

## Mocking 

Vitest provides `jest`-compatible APIs on `vi` object.

ts

```ts
import { expect, vi } from 'vitest'

const fn = vi.fn()

fn('hello', 1)

expect(vi.isMockFunction(fn)).toBe(true)
expect(fn.mock.calls[0]).toEqual(['hello', 1])

fn.mockImplementation((arg: string) => arg)

fn('world', 2)

expect(fn.mock.results[1].value).toBe('world')
```

Vitest supports both happy-dom or jsdom for mocking DOM and browser APIs. They don't come with Vitest, you will need to install them separately:

bash

```bash
$ npm i -D happy-dom
```

bash

```bash
$ npm i -D jsdom
```

After that, change the `environment` option in your config file:

vitest.config.ts

ts

```ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'happy-dom', // or 'jsdom', 'node'
  },
})
```

Learn more at Mocking.

## Coverage 

Vitest supports Native code coverage via `v8` and instrumented code coverage via `istanbul`.

package.json

json

```json
{
  "scripts": {
    "test": "vitest",
    "coverage": "vitest run --coverage"
  }
}
```

Learn more at Coverage.

## In-Source Testing 

Vitest also provides a way to run tests within your source code along with the implementation, similar to Rust's module tests.

This makes the tests share the same closure as the implementations and able to test against private states without exporting. Meanwhile, it also brings the feedback loop closer for development.

src/index.ts

ts

```ts
// the implementation
export function add(...args: number[]): number {
  return args.reduce((a, b) => a + b, 0)
}

// in-source test suites
if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest
  it('add', () => {
    expect(add()).toBe(0)
    expect(add(1)).toBe(1)
    expect(add(1, 2, 3)).toBe(6)
  })
}
```

Learn more at In-source testing.

## Benchmarking Experimental 

You can run benchmark tests with `bench` function via Tinybench to compare performance results.

sort.bench.ts

ts

```ts
import { bench, describe } from 'vitest'

describe('sort', () => {
  bench('normal', () => {
    const x = [1, 5, 4, 2, 3]
    x.sort((a, b) => {
      return a - b
    })
  })

  bench('reverse', () => {
    const x = [1, 5, 4, 2, 3]
    x.reverse().sort((a, b) => {
      return a - b
    })
  })
})
```

## Type Testing Experimental 

You can write tests to catch type regressions. Vitest comes with `expect-type` package to provide you with a similar and easy to understand API.

types.test-d.ts

ts

```ts
import { assertType, expectTypeOf, test } from 'vitest'
import { mount } from './mount.js'

test('my types work properly', () => {
  expectTypeOf(mount).toBeFunction()
  expectTypeOf(mount).parameter(0).toExtend<{ name: string }>()

  // @ts-expect-error name is a string
  assertType(mount({ name: 42 }))
})
```

## Sharding 

Run tests on different machines using `--shard` and `--reporter=blob` flags. All test and coverage results can be merged at the end of your CI pipeline using `--merge-reports` command:

bash

```bash
vitest --shard=1/2 --reporter=blob --coverage
vitest --shard=2/2 --reporter=blob --coverage
vitest --merge-reports --reporter=junit --coverage
```

See `Improving Performance | Sharding` for more information.

## Environment Variables 

Vitest exclusively autoloads environment variables prefixed with `VITE_` from `.env` files to maintain compatibility with frontend-related tests, adhering to Vite's established convention. To load every environmental variable from `.env` files anyway, you can use `loadEnv` method imported from `vite`:

vitest.config.ts

ts

```ts
import { loadEnv } from 'vite'
import { defineConfig } from 'vitest/config'

export default defineConfig(({ mode }) => ({
  test: {
    // mode defines what ".env.{mode}" file to choose if exists
    env: loadEnv(mode, process.cwd(), ''),
  },
}))
```

## Unhandled Errors 

By default, Vitest catches and reports all unhandled rejections, uncaught exceptions (in Node.js) and error events (in the browser).

You can disable this behaviour by catching them manually. Vitest assumes the callback is handled by you and won't report the error.

ts

```ts
// in Node.js
process.on('unhandledRejection', () => {
  // your own handler
})

process.on('uncaughtException', () => {
  // your own handler
})
```

ts

```ts
// in the browser
window.addEventListener('error', () => {
  // your own handler
})

window.addEventListener('unhandledrejection', () => {
  // your own handler
})
```

Alternatively, you can also ignore reported errors with a `dangerouslyIgnoreUnhandledErrors` option. Vitest will still report them, but they won't affect the test result (exit code won't be changed).

If you need to test that error was not caught, you can create a test that looks like this:

ts

```ts
test('my function throws uncaught error', async ({ onTestFinished }) => {
  const unhandledRejectionListener = vi.fn()
  process.on('unhandledRejection', unhandledRejectionListener)
  onTestFinished(() => {
    process.off('unhandledRejection', unhandledRejectionListener)
  })

  callMyFunctionThatRejectsError()

  await expect.poll(unhandledRejectionListener).toHaveBeenCalled()
})
```
