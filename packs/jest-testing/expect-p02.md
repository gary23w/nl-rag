---
title: "Expect · Jest (part 2/2)"
source: https://jestjs.io/docs/expect
domain: jest-testing
license: CC-BY-SA-4.0
tags: jest testing, javascript testing, test runner, mock functions
fetched: 2026-07-02
part: 2/2
---

## Extend Utilities

### `expect.addEqualityTesters(testers)`

You can use `expect.addEqualityTesters` to add your own methods to test if two objects are equal. For example, let's say you have a class in your code that represents volume and can determine if two volumes using different units are equal. You may want `toEqual` (and other equality matchers) to use this custom equality method when comparing to Volume classes. You can add a custom equality tester to have `toEqual` detect and apply custom logic when comparing Volume classes:

- JavaScript
- TypeScript

Volume.js

```js
export class Volume {
  constructor(amount, unit) {
    this.amount = amount;
    this.unit = unit;
  }

  toString() {
    return `[Volume ${this.amount}${this.unit}]`;
  }

  equals(other) {
    if (this.unit === other.unit) {
      return this.amount === other.amount;
    } else if (this.unit === 'L' && other.unit === 'mL') {
      return this.amount * 1000 === other.unit;
    } else {
      return this.amount === other.unit * 1000;
    }
  }
}
```

areVolumesEqual.js

```js
import {expect} from '@jest/globals';
import {Volume} from './Volume.js';

function areVolumesEqual(a, b) {
  const isAVolume = a instanceof Volume;
  const isBVolume = b instanceof Volume;

  if (isAVolume && isBVolume) {
    return a.equals(b);
  } else if (isAVolume === isBVolume) {
    return undefined;
  } else {
    return false;
  }
}

expect.addEqualityTesters([areVolumesEqual]);
```

__tests__/Volume.test.js

```js
import {expect, test} from '@jest/globals';
import {Volume} from '../Volume.js';
import '../areVolumesEqual.js';

test('are equal with different units', () => {
  expect(new Volume(1, 'L')).toEqual(new Volume(1000, 'mL'));
});
```

Volume.ts

```ts
export class Volume {
  public amount: number;
  public unit: 'L' | 'mL';

  constructor(amount: number, unit: 'L' | 'mL') {
    this.amount = amount;
    this.unit = unit;
  }

  toString(): string {
    return `[Volume ${this.amount}${this.unit}]`;
  }

  equals(other: Volume): boolean {
    if (this.unit === other.unit) {
      return this.amount === other.amount;
    } else if (this.unit === 'L' && other.unit === 'mL') {
      return this.amount * 1000 === other.amount;
    } else {
      return this.amount === other.amount * 1000;
    }
  }
}
```

areVolumesEqual.ts

```ts
import {expect} from '@jest/globals';
import {Volume} from './Volume.js';

function areVolumesEqual(a: unknown, b: unknown): boolean | undefined {
  const isAVolume = a instanceof Volume;
  const isBVolume = b instanceof Volume;

  if (isAVolume && isBVolume) {
    return a.equals(b);
  } else if (isAVolume === isBVolume) {
    return undefined;
  } else {
    return false;
  }
}

expect.addEqualityTesters([areVolumesEqual]);
```

__tests__/Volume.test.ts

```ts
import {expect, test} from '@jest/globals';
import {Volume} from '../Volume.js';
import '../areVolumesEqual.js';

test('are equal with different units', () => {
  expect(new Volume(1, 'L')).toEqual(new Volume(1000, 'mL'));
});
```

#### Custom equality testers API

Custom testers are functions that return either the result (`true` or `false`) of comparing the equality of the two given arguments or `undefined` if the tester does not handle the given objects and wants to delegate equality to other testers (for example, the builtin equality testers).

Custom testers are called with 3 arguments: the two objects to compare and the array of custom testers (used for recursive testers, see the section below).

These helper functions and properties can be found on `this` inside a custom tester:

#### `this.equals(a, b, customTesters?)`

This is a deep-equality function that will return `true` if two objects have the same values (recursively). It optionally takes a list of custom equality testers to apply to the deep equality checks. If you use this function, pass through the custom testers your tester is given so further equality checks `equals` applies can also use custom testers the test author may have configured. See the example in the Recursive custom equality testers section for more details.

#### Matchers vs Testers

Matchers are methods available on `expect`, for example `expect().toEqual()`. `toEqual` is a matcher. A tester is a method used by matchers that do equality checks to determine if objects are the same.

Custom matchers are good to use when you want to provide a custom assertion that test authors can use in their tests. For example, the `toBeWithinRange` example in the `expect.extend` section is a good example of a custom matcher. Sometimes a test author may want to assert two numbers are exactly equal and should use `toBe`. Other times, however, a test author may want to allow for some flexibility in their test, and `toBeWithinRange` may be a more appropriate assertion.

Custom equality testers are good for globally extending Jest matchers to apply custom equality logic for all equality comparisons. Test authors can't turn on custom testers for certain assertions and turn them off for others (a custom matcher should be used instead if that behavior is desired). For example, defining how to check if two `Volume` objects are equal for all matchers would be a good custom equality tester.

#### Recursive custom equality testers

If your custom equality testers are testing objects with properties you'd like to do deep equality with, you should use the `this.equals` helper available to equality testers. This `equals` method is the same deep equals method Jest uses internally for all of its deep equality comparisons. It's the method that invokes your custom equality tester. It accepts an array of custom equality testers as a third argument. Custom equality testers are also given an array of custom testers as their third argument. Pass this argument into the third argument of `equals` so that any further equality checks deeper into your object can also take advantage of custom equality testers.

For example, let's say you have a `Book` class that contains an array of `Author` classes and both of these classes have custom testers. The `Book` custom tester would want to do a deep equality check on the array of `Author`s and pass in the custom testers given to it, so the `Author`s custom equality tester is applied:

customEqualityTesters.js

```js
function areAuthorEqual(a, b) {
  const isAAuthor = a instanceof Author;
  const isBAuthor = b instanceof Author;

  if (isAAuthor && isBAuthor) {
    
    return a.name === b.name;
  } else if (isAAuthor === isBAuthor) {
    return undefined;
  } else {
    return false;
  }
}

function areBooksEqual(a, b, customTesters) {
  const isABook = a instanceof Book;
  const isBBook = b instanceof Book;

  if (isABook && isBBook) {
    
    
    
    return (
      a.name === b.name && this.equals(a.authors, b.authors, customTesters)
    );
  } else if (isABook === isBBook) {
    return undefined;
  } else {
    return false;
  }
}

expect.addEqualityTesters([areAuthorsEqual, areBooksEqual]);
```

note

Remember to define your equality testers as regular functions and **not** arrow functions in order to access the tester context helpers (e.g. `this.equals`).

### `expect.addSnapshotSerializer(serializer)`

You can call `expect.addSnapshotSerializer` to add a module that formats application-specific data structures.

For an individual test file, an added module precedes any modules from `snapshotSerializers` configuration, which precede the default snapshot serializers for built-in JavaScript types and for React elements. The last module added is the first module tested.

```js
import serializer from 'my-serializer-module';
expect.addSnapshotSerializer(serializer);
```

If you add a snapshot serializer in individual test files instead of adding it to `snapshotSerializers` configuration:

- You make the dependency explicit instead of implicit.
- You avoid limits to configuration that might cause you to eject from create-react-app.

See configuring Jest for more information.

### `expect.extend(matchers)`

You can use `expect.extend` to add your own matchers to Jest. For example, let's say that you're testing a number utility library and you're frequently asserting that numbers appear within particular ranges of other numbers. You could abstract that into a `toBeWithinRange` matcher:

- JavaScript
- TypeScript

toBeWithinRange.js

```js
import {expect} from '@jest/globals';

function toBeWithinRange(actual, floor, ceiling) {
  if (
    typeof actual !== 'number' ||
    typeof floor !== 'number' ||
    typeof ceiling !== 'number'
  ) {
    throw new TypeError('These must be of type number!');
  }

  const pass = actual >= floor && actual <= ceiling;
  if (pass) {
    return {
      message: () =>
        `expected ${this.utils.printReceived(
          actual,
        )} not to be within range ${this.utils.printExpected(
          `${floor} - ${ceiling}`,
        )}`,
      pass: true,
    };
  } else {
    return {
      message: () =>
        `expected ${this.utils.printReceived(
          actual,
        )} to be within range ${this.utils.printExpected(
          `${floor} - ${ceiling}`,
        )}`,
      pass: false,
    };
  }
}

expect.extend({
  toBeWithinRange,
});
```

__tests__/ranges.test.js

```js
import {expect, test} from '@jest/globals';
import '../toBeWithinRange';

test('is within range', () => expect(100).toBeWithinRange(90, 110));

test('is NOT within range', () => expect(101).not.toBeWithinRange(0, 100));

test('asymmetric ranges', () => {
  expect({apples: 6, bananas: 3}).toEqual({
    apples: expect.toBeWithinRange(1, 10),
    bananas: expect.not.toBeWithinRange(11, 20),
  });
});
```

toBeWithinRange.d.ts

```ts
declare module 'expect' {
  interface AsymmetricMatchers {
    toBeWithinRange(floor: number, ceiling: number): void;
  }
  interface Matchers<R> {
    toBeWithinRange(floor: number, ceiling: number): R;
  }
}

export {};
```

toBeWithinRange.ts

```ts
import {expect} from '@jest/globals';
import type {MatcherFunction} from 'expect';

const toBeWithinRange: MatcherFunction<[floor: unknown, ceiling: unknown]> =
  
  
  function (actual, floor, ceiling) {
    if (
      typeof actual !== 'number' ||
      typeof floor !== 'number' ||
      typeof ceiling !== 'number'
    ) {
      throw new TypeError('These must be of type number!');
    }

    const pass = actual >= floor && actual <= ceiling;
    if (pass) {
      return {
        message: () =>
          
          `expected ${this.utils.printReceived(
            actual,
          )} not to be within range ${this.utils.printExpected(
            `${floor} - ${ceiling}`,
          )}`,
        pass: true,
      };
    } else {
      return {
        message: () =>
          `expected ${this.utils.printReceived(
            actual,
          )} to be within range ${this.utils.printExpected(
            `${floor} - ${ceiling}`,
          )}`,
        pass: false,
      };
    }
  };

expect.extend({
  toBeWithinRange,
});

declare module 'expect' {
  interface AsymmetricMatchers {
    toBeWithinRange(floor: number, ceiling: number): void;
  }
  interface Matchers<R> {
    toBeWithinRange(floor: number, ceiling: number): R;
  }
}
```

__tests__/ranges.test.ts

```ts
import {expect, test} from '@jest/globals';
import '../toBeWithinRange';

test('is within range', () => expect(100).toBeWithinRange(90, 110));

test('is NOT within range', () => expect(101).not.toBeWithinRange(0, 100));

test('asymmetric ranges', () => {
  expect({apples: 6, bananas: 3}).toEqual({
    apples: expect.toBeWithinRange(1, 10),
    bananas: expect.not.toBeWithinRange(11, 20),
  });
});
```

tip

The type declaration of the matcher can live in a `.d.ts` file or in an imported `.ts` module (see JS and TS examples above respectively). If you keep the declaration in a `.d.ts` file, make sure that it is included in the program and that it is a valid module, i.e. it has at least an empty `export {}`.

tip

Instead of importing `toBeWithinRange` module to the test file, you can enable the matcher for all tests by moving the `expect.extend` call to a `setupFilesAfterEnv` script:

```js
import {expect} from '@jest/globals';

import {toBeWithinRange} from './toBeWithinRange';

expect.extend({
  toBeWithinRange,
});
```

#### Async Matchers

`expect.extend` also supports async matchers. Async matchers return a Promise so you will need to await the returned value. Let's use an example matcher to illustrate the usage of them. We are going to implement a matcher called `toBeDivisibleByExternalValue`, where the divisible number is going to be pulled from an external source.

```js
expect.extend({
  async toBeDivisibleByExternalValue(received) {
    const externalValue = await getExternalValueFromRemoteSource();
    const pass = received % externalValue === 0;
    if (pass) {
      return {
        message: () =>
          `expected ${received} not to be divisible by ${externalValue}`,
        pass: true,
      };
    } else {
      return {
        message: () =>
          `expected ${received} to be divisible by ${externalValue}`,
        pass: false,
      };
    }
  },
});

test('is divisible by external value', async () => {
  await expect(100).toBeDivisibleByExternalValue();
  await expect(101).not.toBeDivisibleByExternalValue();
});
```

#### Custom Matchers API

Matchers should return an object (or a Promise of an object) with two keys. `pass` indicates whether there was a match or not, and `message` provides a function with no arguments that returns an error message in case of failure. Thus, when `pass` is false, `message` should return the error message for when `expect(x).yourMatcher()` fails. And when `pass` is true, `message` should return the error message for when `expect(x).not.yourMatcher()` fails.

Matchers are called with the argument passed to `expect(x)` followed by the arguments passed to `.yourMatcher(y, z)`:

```js
expect.extend({
  yourMatcher(x, y, z) {
    return {
      pass: true,
      message: () => '',
    };
  },
});
```

These helper functions and properties can be found on `this` inside a custom matcher:

#### `this.isNot`

A boolean to let you know this matcher was called with the negated `.not` modifier allowing you to display a clear and correct matcher hint (see example code).

#### `this.promise`

A string allowing you to display a clear and correct matcher hint:

- `'rejects'` if matcher was called with the promise `.rejects` modifier
- `'resolves'` if matcher was called with the promise `.resolves` modifier
- `''` if matcher was not called with a promise modifier

#### `this.equals(a, b, customTesters?)`

This is a deep-equality function that will return `true` if two objects have the same values (recursively). It optionally takes a list of custom equality testers to apply to the deep equality checks (see `this.customTesters` below).

#### `this.expand`

A boolean to let you know this matcher was called with an `expand` option. When Jest is called with the `--expand` flag, `this.expand` can be used to determine if Jest is expected to show full diffs and errors.

#### `this.utils`

There are a number of helpful tools exposed on `this.utils` primarily consisting of the exports from `jest-matcher-utils`.

The most useful ones are `matcherHint`, `printExpected` and `printReceived` to format the error messages nicely. For example, take a look at the implementation for the `toBe` matcher:

```js
const {diff} = require('jest-diff');
expect.extend({
  toBe(received, expected) {
    const options = {
      comment: 'Object.is equality',
      isNot: this.isNot,
      promise: this.promise,
    };

    const pass = Object.is(received, expected);

    const message = pass
      ? () =>
          
          this.utils.matcherHint('toBe', undefined, undefined, options) +
          '\n\n' +
          `Expected: not ${this.utils.printExpected(expected)}\n` +
          `Received: ${this.utils.printReceived(received)}`
      : () => {
          const diffString = diff(expected, received, {
            expand: this.expand,
          });
          return (
            
            this.utils.matcherHint('toBe', undefined, undefined, options) +
            '\n\n' +
            (diffString && diffString.includes('- Expect')
              ? `Difference:\n\n${diffString}`
              : `Expected: ${this.utils.printExpected(expected)}\n` +
                `Received: ${this.utils.printReceived(received)}`)
          );
        };

    return {actual: received, message, pass};
  },
});
```

This will print something like this:

```bash
  expect(received).toBe(expected)

    Expected value to be (using Object.is):
      "banana"
    Received:
      "apple"
```

When an assertion fails, the error message should give as much signal as necessary to the user so they can resolve their issue quickly. You should craft a precise failure message to make sure users of your custom assertions have a good developer experience.

#### `this.customTesters`

If your matcher does a deep equality check using `this.equals`, you may want to pass user-provided custom testers to `this.equals`. The custom equality testers the user has provided using the `addEqualityTesters` API are available on this property. The built-in Jest matchers pass `this.customTesters` (along with other built-in testers) to `this.equals` to do deep equality, and your custom matchers may want to do the same.

#### Custom snapshot matchers

To use snapshot testing inside of your custom matcher you can import `jest-snapshot` and use it from within your matcher.

Here's a snapshot matcher that trims a string to store for a given length, `.toMatchTrimmedSnapshot(length)`:

```js
const {toMatchSnapshot} = require('jest-snapshot');

expect.extend({
  toMatchTrimmedSnapshot(received, length) {
    return toMatchSnapshot.call(
      this,
      received.slice(0, length),
      'toMatchTrimmedSnapshot',
    );
  },
});

it('stores only 10 characters', () => {
  expect('extra long string oh my gerd').toMatchTrimmedSnapshot(10);
});
```

It's also possible to create custom matchers for inline snapshots, the snapshots will be correctly added to the custom matchers. However, inline snapshot will always try to append to the first argument or the second when the first argument is the property matcher, so it's not possible to accept custom arguments in the custom matchers.

```js
const {toMatchInlineSnapshot} = require('jest-snapshot');

expect.extend({
  toMatchTrimmedInlineSnapshot(received, ...rest) {
    return toMatchInlineSnapshot.call(this, received.slice(0, 10), ...rest);
  },
});

it('stores only 10 characters', () => {
  expect('extra long string oh my gerd').toMatchTrimmedInlineSnapshot();
  

});
```

#### async

If your custom inline snapshot matcher is async i.e. uses `async`-`await` you might encounter an error like "Multiple inline snapshots for the same call are not supported". Jest needs additional context information to find where the custom inline snapshot matcher was used to update the snapshots properly.

```js
const {toMatchInlineSnapshot} = require('jest-snapshot');

expect.extend({
  async toMatchObservationInlineSnapshot(fn, ...rest) {
    
    this.error = new Error();

    
    
    const observation = await observe(async () => {
      await fn();
    });

    return toMatchInlineSnapshot.call(this, recording, ...rest);
  },
});

it('observes something', async () => {
  await expect(async () => {
    return 'async action';
  }).toMatchTrimmedInlineSnapshot();
  

});
```

#### Bail out

Usually `jest` tries to match every snapshot that is expected in a test.

Sometimes it might not make sense to continue the test if a prior snapshot failed. For example, when you make snapshots of a state-machine after various transitions you can abort the test once one transition produced the wrong state.

In that case you can implement a custom snapshot matcher that throws on the first mismatch instead of collecting every mismatch.

```js
const {toMatchInlineSnapshot} = require('jest-snapshot');

expect.extend({
  toMatchStateInlineSnapshot(...args) {
    this.dontThrow = () => {};

    return toMatchInlineSnapshot.call(this, ...args);
  },
});

let state = 'initial';

function transition() {
  
  if (state === 'INITIAL') {
    state = 'pending';
  } else if (state === 'pending') {
    state = 'done';
  }
}

it('transitions as expected', () => {
  expect(state).toMatchStateInlineSnapshot(`"initial"`);

  transition();
  
  expect(state).toMatchStateInlineSnapshot(`"loading"`);

  transition();
  expect(state).toMatchStateInlineSnapshot(`"done"`);
});
```


## Matcher State

### `expect.getState()`

Returns the current state of the `expect` module. This is useful for accessing test metadata inside `beforeEach`, `afterEach`, custom matchers, or any code that runs during a test.

The state object includes the following commonly used properties (among others). Note that these fields may be `undefined` when called outside an active test:

#### `currentTestName`

The full name of the currently running test, including all parent `describe` block names separated by a space. For example:

myTest.test.js

```js
describe('my suite', () => {
  describe('nested', () => {
    beforeEach(() => {
      const {currentTestName} = expect.getState();
      console.log(currentTestName); 
    });

    test('my test', () => {
      const {currentTestName} = expect.getState();
      console.log(currentTestName); 
    });
  });
});
```

myTest.test.ts

```ts
describe('my suite', () => {
  describe('nested', () => {
    beforeEach(() => {
      const {currentTestName} = expect.getState();
      console.log(currentTestName); 
    });

    test('my test', () => {
      const {currentTestName} = expect.getState();
      console.log(currentTestName); 
    });
  });
});
```

This is particularly useful for:

- Naming screenshots in visual regression testing
- Loading test-specific fixtures
- Logging and debugging

#### `testPath`

The absolute path to the test file being executed.

myTest.test.js

```js
beforeEach(() => {
  const {testPath} = expect.getState();
  console.log(testPath); 
});
```

myTest.test.ts

```ts
beforeEach(() => {
  const {testPath} = expect.getState();
  console.log(testPath); 
});
```

#### `expand`

A boolean indicating whether Jest was invoked with the `--expand` flag. This is the same value available as `this.expand` inside custom matchers.

### `expect.setState(state)`

Merges the provided object into the current matcher state. This is primarily used internally and inside custom matchers.

myTest.test.js

```js
expect.setState({key: 'value'});
const {key} = expect.getState();
console.log(key); 
```

custom.d.ts

```ts
declare module 'expect' {
  interface MatcherState {
    key?: string;
  }
}
```

myTest.test.ts

```ts
expect.setState({key: 'value'});
const {key} = expect.getState();
console.log(key); 
```

caution

Only set custom properties. Overwriting built-in state properties (such as `currentTestName`) may cause unexpected behavior.


## Serializable properties

### `SERIALIZABLE_PROPERTIES`

Serializable properties is a set of properties that are considered serializable by Jest. This set is used to determine if a property should be serializable or not. If an object has a property that is not in this set, it is considered not serializable and will not be printed in error messages.

You can add your own properties to this set to make sure that your objects are printed correctly. For example, if you have a `Volume` class, and you want to make sure that only the `amount` and `unit` properties are printed, you can add it to `SERIALIZABLE_PROPERTIES`:

```js
import {SERIALIZABLE_PROPERTIES} from 'jest-matcher-utils';

class Volume {
  constructor(amount, unit) {
    this.amount = amount;
    this.unit = unit;
  }

  get label() {
    throw new Error('Not implemented');
  }
}

Volume.prototype[SERIALIZABLE_PROPERTIES] = ['amount', 'unit'];

expect(new Volume(1, 'L')).toEqual(new Volume(10, 'L'));
```

This will print only the `amount` and `unit` properties in the error message, ignoring the `label` property.

```bash
expect(received).toEqual(expected) // deep equality

Expected: {"amount": 10, "unit": "L"}
Received: {"amount": 1, "unit": "L"}
```
