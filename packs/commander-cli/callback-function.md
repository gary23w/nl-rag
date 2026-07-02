---
title: "Callback function - Glossary"
source: https://developer.mozilla.org/en-US/docs/Glossary/Callback_function
domain: commander-cli
license: CC-BY-SA-4.0
tags: commander.js, cli argument parser, command line framework, subcommand definition
fetched: 2026-07-02
---

# Callback function

A **callback function** is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

The consumer of a callback-based API writes a function that is passed into the API. The provider of the API (called the *caller*) takes the function and calls back (or executes) the function at some point inside the caller's body. The caller is responsible for passing the right parameters into the callback function. The caller may also expect a particular return value from the callback function, which is used to instruct further behavior of the caller.

There are two ways in which the callback may be called: *synchronous* and *asynchronous*. Synchronous callbacks are called immediately after the invocation of the outer function, with no intervening asynchronous tasks, while asynchronous callbacks are called at some point later, after an asynchronous operation has completed.

Understanding whether the callback is synchronously or asynchronously called is particularly important when analyzing side effects. Consider the following example:

```js
let value = 1;

doSomething(() => {
  value = 2;
});

console.log(value); // 1 or 2?
```

If `doSomething` calls the callback synchronously, then the last statement would log `2` because `value = 2` is synchronously executed; otherwise, if the callback is asynchronous, the last statement would log `1` because `value = 2` is only executed after the `console.log` statement.

Examples of synchronous callbacks include the callbacks passed to `Array.prototype.map()`, `Array.prototype.forEach()`, etc. Examples of asynchronous callbacks include the callbacks passed to `setTimeout()` and `Promise.prototype.then()`. Here are example implementations of `doSomething` that call the callback synchronously and asynchronously:

```js
// Synchronous
function doSomething(callback) {
  callback();
}

// Asynchronous
function doSomething(callback) {
  setTimeout(callback, 0);
}
```

The Using promises guide has more information on the timing of asynchronous callbacks.
