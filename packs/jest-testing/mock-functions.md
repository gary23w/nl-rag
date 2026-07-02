---
title: "Mock Functions · Jest"
source: https://jestjs.io/docs/mock-functions
domain: jest-testing
license: CC-BY-SA-4.0
tags: jest testing, javascript testing, test runner, mock functions
fetched: 2026-07-02
---

# Mock Functions · Jest

Version: 30.4

# Mock Functions

Mock functions allow you to test the links between code by erasing the actual implementation of a function, capturing calls to the function (and the parameters passed in those calls), capturing instances of constructor functions when instantiated with `new`, and allowing test-time configuration of return values.

There are two ways to mock functions: Either by creating a mock function to use in test code, or writing a `manual mock` to override a module dependency.

## Using a mock function

Let's imagine we're testing an implementation of a function `forEach`, which invokes a callback for each item in a supplied array.

forEach.js

```js
export function forEach(items, callback) {
  for (const item of items) {
    callback(item);
  }
}
```

To test this function, we can use a mock function, and inspect the mock's state to ensure the callback is invoked as expected.

forEach.test.js

```js
import {forEach} from './forEach';

const mockCallback = jest.fn(x => 42 + x);

test('forEach mock function', () => {
  forEach([0, 1], mockCallback);

  
  expect(mockCallback.mock.calls).toHaveLength(2);

  
  expect(mockCallback.mock.calls[0][0]).toBe(0);

  
  expect(mockCallback.mock.calls[1][0]).toBe(1);

  
  expect(mockCallback.mock.results[0].value).toBe(42);
});
```

## `.mock` property

All mock functions have this special `.mock` property, which is where data about how the function has been called and what the function returned is kept. The `.mock` property also tracks the value of `this` for each call, so it is possible to inspect this as well:

```javascript
const myMock1 = jest.fn();
const a = new myMock1();
console.log(myMock1.mock.instances);

const myMock2 = jest.fn();
const b = {};
const bound = myMock2.bind(b);
bound();
console.log(myMock2.mock.contexts);
```

These mock members are very useful in tests to assert how these functions get called, instantiated, or what they returned:

```javascript
expect(someMockFunction.mock.calls).toHaveLength(1);

expect(someMockFunction.mock.calls[0][0]).toBe('first arg');

expect(someMockFunction.mock.calls[0][1]).toBe('second arg');

expect(someMockFunction.mock.results[0].value).toBe('return value');

expect(someMockFunction.mock.contexts[0]).toBe(element);

expect(someMockFunction.mock.instances.length).toBe(2);

expect(someMockFunction.mock.instances[0].name).toBe('test');

expect(someMockFunction.mock.lastCall[0]).toBe('test');
```

## Mock Return Values

Mock functions can also be used to inject test values into your code during a test:

```javascript
const myMock = jest.fn();
console.log(myMock());

myMock.mockReturnValueOnce(10).mockReturnValueOnce('x').mockReturnValue(true);

console.log(myMock(), myMock(), myMock(), myMock());
```

Mock functions are also very effective in code that uses a functional continuation-passing style. Code written in this style helps avoid the need for complicated stubs that recreate the behavior of the real component they're standing in for, in favor of injecting values directly into the test right before they're used.

```javascript
const filterTestFn = jest.fn();

filterTestFn.mockReturnValueOnce(true).mockReturnValueOnce(false);

const result = [11, 12].filter(num => filterTestFn(num));

console.log(result);

console.log(filterTestFn.mock.calls[0][0]); 
console.log(filterTestFn.mock.calls[1][0]); 
```

Most real-world examples actually involve getting ahold of a mock function on a dependent component and configuring that, but the technique is the same. In these cases, try to avoid the temptation to implement logic inside of any function that's not directly being tested.

## Mocking Modules

Suppose we have a class that fetches users from our API. The class uses axios to call the API then returns the `data` attribute which contains all the users:

users.js

```js
import axios from 'axios';

class Users {
  static all() {
    return axios.get('/users.json').then(resp => resp.data);
  }
}

export default Users;
```

Now, in order to test this method without actually hitting the API (and thus creating slow and fragile tests), we can use the `jest.mock(...)` function to automatically mock the axios module.

Once we mock the module we can provide a `mockResolvedValue` for `.get` that returns the data we want our test to assert against. In effect, we are saying that we want `axios.get('/users.json')` to return a fake response.

users.test.js

```js
import axios from 'axios';
import Users from './users';

jest.mock('axios');

test('should fetch users', () => {
  const users = [{name: 'Bob'}];
  const resp = {data: users};
  axios.get.mockResolvedValue(resp);

  
  

  return Users.all().then(data => expect(data).toEqual(users));
});
```

## Mocking Partials

Subsets of a module can be mocked and the rest of the module can keep their actual implementation:

foo-bar-baz.js

```js
export const foo = 'foo';
export const bar = () => 'bar';
export default () => 'baz';
```

```js
import defaultExport, {bar, foo} from '../foo-bar-baz';

jest.mock('../foo-bar-baz', () => {
  const originalModule = jest.requireActual('../foo-bar-baz');

  
  return {
    __esModule: true,
    ...originalModule,
    default: jest.fn(() => 'mocked baz'),
    foo: 'mocked foo',
  };
});

test('should do a partial mock', () => {
  const defaultExportResult = defaultExport();
  expect(defaultExportResult).toBe('mocked baz');
  expect(defaultExport).toHaveBeenCalled();

  expect(foo).toBe('mocked foo');
  expect(bar()).toBe('bar');
});
```

## Mock Implementations

Still, there are cases where it's useful to go beyond the ability to specify return values and full-on replace the implementation of a mock function. This can be done with `jest.fn` or the `mockImplementationOnce` method on mock functions.

```javascript
const myMockFn = jest.fn(cb => cb(null, true));

myMockFn((err, val) => console.log(val));
```

The `mockImplementation` method is useful when you need to define the default implementation of a mock function that is created from another module:

foo.js

```js
module.exports = function () {
  
};
```

test.js

```js
jest.mock('../foo'); 
const foo = require('../foo');

foo.mockImplementation(() => 42);
foo();
```

When you need to recreate a complex behavior of a mock function such that multiple function calls produce different results, use the `mockImplementationOnce` method:

```javascript
const myMockFn = jest
  .fn()
  .mockImplementationOnce(cb => cb(null, true))
  .mockImplementationOnce(cb => cb(null, false));

myMockFn((err, val) => console.log(val));

myMockFn((err, val) => console.log(val));
```

When the mocked function runs out of implementations defined with `mockImplementationOnce`, it will execute the default implementation set with `jest.fn` (if it is defined):

```javascript
const myMockFn = jest
  .fn(() => 'default')
  .mockImplementationOnce(() => 'first call')
  .mockImplementationOnce(() => 'second call');

console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
```

For cases where we have methods that are typically chained (and thus always need to return `this`), we have a sugary API to simplify this in the form of a `.mockReturnThis()` function that also sits on all mocks:

```javascript
const myObj = {
  myMethod: jest.fn().mockReturnThis(),
};

const otherObj = {
  myMethod: jest.fn(function () {
    return this;
  }),
};
```

## Mock Names

You can optionally provide a name for your mock functions, which will be displayed instead of `'jest.fn()'` in the test error output. Use `.mockName()` if you want to be able to quickly identify the mock function reporting an error in your test output.

```javascript
const myMockFn = jest
  .fn()
  .mockReturnValue('default')
  .mockImplementation(scalar => 42 + scalar)
  .mockName('add42');
```

## Custom Matchers

Finally, in order to make it less demanding to assert how mock functions have been called, we've added some custom matcher functions for you:

```javascript
expect(mockFunc).toHaveBeenCalled();

expect(mockFunc).toHaveBeenCalledWith(arg1, arg2);

expect(mockFunc).toHaveBeenLastCalledWith(arg1, arg2);

expect(mockFunc).toMatchSnapshot();
```

These matchers are sugar for common forms of inspecting the `.mock` property. You can always do this manually yourself if that's more to your taste or if you need to do something more specific:

```javascript
expect(mockFunc.mock.calls.length).toBeGreaterThan(0);

expect(mockFunc.mock.calls).toContainEqual([arg1, arg2]);

expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1]).toEqual([
  arg1,
  arg2,
]);

expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1][0]).toBe(42);

expect(mockFunc.mock.calls).toEqual([[arg1, arg2]]);
expect(mockFunc.getMockName()).toBe('a mock name');
```

For a complete list of matchers, check out the reference docs.
