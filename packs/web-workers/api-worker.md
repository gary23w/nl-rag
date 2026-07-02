---
title: "Worker - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Worker
domain: web-workers
license: CC-BY-SA-4.0
tags: web workers, background threads browser, worker global scope, dedicated worker thread
fetched: 2026-07-02
---

# Worker

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers, except for Service Workers.

The **`Worker`** interface of the Web Workers API represents a background task that can be created via script, which can send messages back to its creator.

Creating a worker is done by calling the `Worker("path/to/worker/script")` constructor.

Workers may themselves spawn new workers, as long as those workers are hosted at the same origin as the parent page.

Note that not all interfaces and functions are available to web workers. See Functions and classes available to Web Workers for details.

## Constructors

**`Worker()`**

Creates a dedicated web worker that executes the script at the specified URL. This also works for Blob URLs.

## Instance properties

*Inherits properties from its parent, `EventTarget`.*

## Instance methods

*Inherits methods from its parent, `EventTarget`.*

**`Worker.postMessage()`**

Sends a message — consisting of any JavaScript object — to the worker's inner scope.

**`Worker.terminate()`**

Immediately terminates the worker. This does not let worker finish its operations; it is halted at once. `ServiceWorker` instances do not support this method.

## Events

**`error`**

Fires when an error occurs in the worker.

**`message`**

Fires when the worker's parent receives a message from that worker.

**`messageerror`**

Fires when a `Worker` object receives a message that can't be deserialized.

## Example

The following code snippet creates a `Worker` object using the `Worker()` constructor, then uses the worker object:

```js
const myWorker = new Worker("/worker.js");
const first = document.querySelector("input#number1");
const second = document.querySelector("input#number2");

first.onchange = () => {
  myWorker.postMessage([first.value, second.value]);
  console.log("Message posted to worker");
};
```

For a full example, see our Basic dedicated worker example (run dedicated worker).

## Specifications

| Specification |
|---|
| HTML # dedicated-workers-and-the-worker-interface |

## Browser compatibility

Support varies for different types of workers. See each worker type's page for specifics.

### Cross-origin worker error behavior

In early versions of the spec, loading a cross-origin worker script threw a `SecurityError`. Nowadays, an `error` event is thrown instead.
