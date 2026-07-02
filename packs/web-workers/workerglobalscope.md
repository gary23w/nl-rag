---
title: "WorkerGlobalScope - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope
domain: web-workers
license: CC-BY-SA-4.0
tags: web workers, background threads browser, worker global scope, dedicated worker thread
fetched: 2026-07-02
---

# WorkerGlobalScope

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is only available in Web Workers.

The **`WorkerGlobalScope`** interface of the Web Workers API is an interface representing the scope of any worker. Workers have no browsing context; this scope contains the information usually conveyed by `Window` objects — in this case event handlers, the console or the associated `WorkerNavigator` object. Each `WorkerGlobalScope` has its own event loop.

This interface is usually specialized by each worker type: `DedicatedWorkerGlobalScope` for dedicated workers, `SharedWorkerGlobalScope` for shared workers, and `ServiceWorkerGlobalScope` for ServiceWorker. The `self` property returns the specialized scope for each context.

## Instance properties

*This interface inherits properties from the `EventTarget` interface.*

**`WorkerGlobalScope.caches` Read only Secure context**

Returns the `CacheStorage` object associated with the current context. This object enables functionality such as storing assets for offline use, and generating custom responses to requests.

**`WorkerGlobalScope.crossOriginIsolated` Read only**

Returns a boolean value that indicates whether the website is in a cross-origin isolation state.

**`WorkerGlobalScope.crypto` Read only**

Returns the `Crypto` object associated to the global object.

**`WorkerGlobalScope.fonts` Read only**

Returns the `FontFaceSet` associated with the worker.

**`WorkerGlobalScope.indexedDB` Read only**

Provides a mechanism for workers to asynchronously access capabilities of indexed databases; returns an `IDBFactory` object.

**`WorkerGlobalScope.isSecureContext` Read only**

Returns a boolean indicating whether the current context is secure (`true`) or not (`false`).

**`WorkerGlobalScope.location` Read only**

Returns the `WorkerLocation` associated with the worker. It is a specific location object, mostly a subset of the `Location` for browsing scopes, but adapted to workers.

**`WorkerGlobalScope.navigator` Read only**

Returns the `WorkerNavigator` associated with the worker. It is a specific navigator object, mostly a subset of the `Navigator` for browsing scopes, but adapted to workers.

**`WorkerGlobalScope.origin` Read only**

Returns the global object's origin, serialized as a string.

**`WorkerGlobalScope.performance` Read only**

Returns the `Performance` associated with the worker. Only a subset of the properties and methods of the `Performance` interface are available to workers.

**`WorkerGlobalScope.scheduler` Read only**

Returns the `Scheduler` object associated with the current context. This is the entry point for using the Prioritized Task Scheduling API.

**`WorkerGlobalScope.trustedTypes` Read only**

Returns the `TrustedTypePolicyFactory` object associated with the global object, providing the entry point for using the Trusted Types API.

**`WorkerGlobalScope.self` Read only**

Returns a reference to the `WorkerGlobalScope` itself. Most of the time it is a specific scope like `DedicatedWorkerGlobalScope`, `SharedWorkerGlobalScope` or `ServiceWorkerGlobalScope`.

## Instance methods

*This interface inherits methods from the `EventTarget` interface.*

**`WorkerGlobalScope.atob()`**

Decodes a string of data which has been encoded using base-64 encoding.

**`WorkerGlobalScope.btoa()`**

Creates a base-64 encoded ASCII string from a string of binary data.

**`WorkerGlobalScope.clearInterval()`**

Cancels the repeated execution set using `WorkerGlobalScope.setInterval()`.

**`WorkerGlobalScope.clearTimeout()`**

Cancels the delayed execution set using `WorkerGlobalScope.setTimeout()`.

**`WorkerGlobalScope.createImageBitmap()`**

Accepts a variety of different image sources, and returns a `Promise` which resolves to an `ImageBitmap`. Optionally the source is cropped to the rectangle of pixels originating at *(sx, sy)* with width sw, and height sh.

**`WorkerGlobalScope.dump()`**

Allows you to write a message to stdout — i.e., in your terminal. This is the same as Firefox's `window.dump`, but for workers.

**`WorkerGlobalScope.fetch()`**

Starts the process of fetching a resource from the network.

**`WorkerGlobalScope.importScripts()`**

Imports one or more scripts into the worker's scope. You can specify as many as you'd like, separated by commas. For example: `importScripts('foo.js', 'bar.js');`.

**`WorkerGlobalScope.queueMicrotask()`**

Queues a microtask to be executed at a safe time prior to control returning to the browser's event loop.

**`WorkerGlobalScope.setInterval()`**

Schedules a function to execute every time a given number of milliseconds elapses.

**`WorkerGlobalScope.setTimeout()`**

Schedules a function to execute in a given amount of time.

**`WorkerGlobalScope.structuredClone()`**

Creates a deep clone of a given value using the structured clone algorithm.

**`WorkerGlobalScope.reportError()`**

Reports an error in a script, emulating an unhandled exception.

## Events

**`error`**

Fired when an error occurred.

**`languagechange`**

Fired at the global/worker scope object when the user's preferred languages change.

**`offline`**

Fired when the browser has lost access to the network and the value of `navigator.onLine` switched to `false`.

**`online`**

Fired when the browser has gained access to the network and the value of `navigator.onLine` switched to `true`.

**`rejectionhandled`**

Fired on handled `Promise` rejection events.

**`securitypolicyviolation`**

Fired when a Content Security Policy is violated.

**`unhandledrejection`**

Fired on unhandled `Promise` rejection events.

## Example

You won't access `WorkerGlobalScope` directly in your code; however, its properties and methods are inherited by more specific global scopes such as `DedicatedWorkerGlobalScope` and `SharedWorkerGlobalScope`. For example, you could import another script into the worker and print out the contents of the worker scope's `navigator` object using the following two lines:

```js
importScripts("foo.js");
console.log(navigator);
```

**Note:** Since the global scope of the worker script is effectively the global scope of the worker you are running (`DedicatedWorkerGlobalScope` or whatever) and all worker global scopes inherit methods, properties, etc. from `WorkerGlobalScope`, you can run lines such as those above without specifying a parent object.

## Specifications

| Specification |
|---|
| HTML # the-workerglobalscope-common-interface |

## Browser compatibility
