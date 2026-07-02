---
title: "Mocking"
source: https://vitest.dev/guide/mocking
domain: vitest
license: CC-BY-SA-4.0
tags: vitest runner, vite testing, javascript testing, test mocking
fetched: 2026-07-02
---

# Mocking

Are you an LLM? You can read better optimized documentation at /guide/mocking.md for this page in Markdown format

# Mocking 

TIP

New to mocking? Start with the Mock Functions tutorial for a hands-on introduction to `vi.fn`, `vi.spyOn`, and `vi.mock`.

When writing tests it's only a matter of time before you need to create a "fake" version of an internal — or external — service. This is commonly referred to as **mocking**. Vitest provides utility functions to help you out through its `vi` helper. You can import it from `vitest` or access it globally if `global` configuration is enabled.

WARNING

Always remember to clear or restore mocks before or after each test run to undo mock state changes between runs! See `mockReset` docs for more info.

If you are not familiar with `vi.fn`, `vi.mock` or `vi.spyOn` methods, check the API section first.

Vitest has a comprehensive list of guides regarding mocking:

- Mocking Classes
- Mocking Dates
- Mocking the File System
- Mocking Functions
- Mocking Globals
- Mocking Modules
- Mocking Requests
- Mocking Timers

For a simpler and quicker way to get started with mocking, you can check the Cheat Sheet below.

## Cheat Sheet 

I want to…

### Mock exported variables 

example.js

js

```js
export const getter = 'variable'
```

example.test.ts

ts

```ts
import * as exports from './example.js'

vi.spyOn(exports, 'getter', 'get').mockReturnValue('mocked')
```

WARNING

This will not work in the Browser Mode. For a workaround, see Limitations.

### Mock an exported function 

1. Example with `vi.mock`:

WARNING

Don't forget that a `vi.mock` call is hoisted to top of the file. It will always be executed before all imports.

example.js

ts

```ts
export function method() {}
```

ts

```ts
import { method } from './example.js'

vi.mock('./example.js', () => ({
  method: vi.fn()
}))
```

1. Example with `vi.spyOn`:

ts

```ts
import * as exports from './example.js'

vi.spyOn(exports, 'method').mockImplementation(() => {})
```

WARNING

`vi.spyOn` example will not work in the Browser Mode. For a workaround, see Limitations.

### Mock an exported class implementation 

1. Example with a fake `class`:

example.js

ts

```ts
export class SomeClass {}
```

ts

```ts
import { SomeClass } from './example.js'

vi.mock(import('./example.js'), () => {
  const SomeClass = vi.fn(class FakeClass {
    someMethod = vi.fn()
  })
  return { SomeClass }
})
```

1. Example with `vi.spyOn`:

ts

```ts
import * as mod from './example.js'

vi.spyOn(mod, 'SomeClass').mockImplementation(class FakeClass {
  someMethod = vi.fn()
})
```

WARNING

`vi.spyOn` example will not work in the Browser Mode. For a workaround, see Limitations.

### Spy on an object returned from a function 

1. Example using cache:

example.js

ts

```ts
export function useObject() {
  return { method: () => true }
}
```

useObject.js

ts

```ts
import { useObject } from './example.js'

const obj = useObject()
obj.method()
```

useObject.test.js

ts

```ts
import { useObject } from './example.js'

vi.mock(import('./example.js'), () => {
  let _cache
  const useObject = () => {
    if (!_cache) {
      _cache = {
        method: vi.fn(),
      }
    }
    // now every time that useObject() is called it will
    // return the same object reference
    return _cache
  }
  return { useObject }
})

const obj = useObject()
// obj.method was called inside some-path
expect(obj.method).toHaveBeenCalled()
```

### Mock part of a module 

ts

```ts
import { mocked, original } from './some-path.js'

vi.mock(import('./some-path.js'), async (importOriginal) => {
  const mod = await importOriginal()
  return {
    ...mod,
    mocked: vi.fn()
  }
})
original() // has original behaviour
mocked() // is a spy function
```

WARNING

Don't forget that this only mocks *external* access. In this example, if `original` calls `mocked` internally, it will always call the function defined in the module, not in the mock factory.

### Mock the current date 

To mock `Date`'s time, you can use `vi.setSystemTime` helper function. This value will **not** automatically reset between different tests.

Beware that using `vi.useFakeTimers` also changes the `Date`'s time.

ts

```ts
const mockDate = new Date(2022, 0, 1)
vi.setSystemTime(mockDate)
const now = new Date()
expect(now.valueOf()).toBe(mockDate.valueOf())
// reset mocked time
vi.useRealTimers()
```

### Mock a global variable 

You can set global variable by assigning a value to `globalThis` or using `vi.stubGlobal` helper. When using `vi.stubGlobal`, it will **not** automatically reset between different tests, unless you enable `unstubGlobals` config option or call `vi.unstubAllGlobals`.

ts

```ts
vi.stubGlobal('__VERSION__', '1.0.0')
expect(__VERSION__).toBe('1.0.0')
```

### Mock `import.meta.env` 

1. To change environmental variable, you can just assign a new value to it.

WARNING

The environmental variable value will ***not*** automatically reset between different tests.

ts

```ts
import { beforeEach, expect, it } from 'vitest'

// you can reset it in beforeEach hook manually
const originalViteEnv = import.meta.env.VITE_ENV

beforeEach(() => {
  import.meta.env.VITE_ENV = originalViteEnv
})

it('changes value', () => {
  import.meta.env.VITE_ENV = 'staging'
  expect(import.meta.env.VITE_ENV).toBe('staging')
})
```

1. If you want to automatically reset the value(s), you can use the `vi.stubEnv` helper with the `unstubEnvs` config option enabled (or call `vi.unstubAllEnvs` manually in a `beforeEach` hook):

ts

```ts
import { expect, it, vi } from 'vitest'

// before running tests "VITE_ENV" is "test"
import.meta.env.VITE_ENV === 'test'

it('changes value', () => {
  vi.stubEnv('VITE_ENV', 'staging')
  expect(import.meta.env.VITE_ENV).toBe('staging')
})

it('the value is restored before running an other test', () => {
  expect(import.meta.env.VITE_ENV).toBe('test')
})
```

vitest.config.ts

ts

```ts
export default defineConfig({
  test: {
    unstubEnvs: true,
  },
})
```
