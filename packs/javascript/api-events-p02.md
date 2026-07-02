---
title: "Events (part 2/2)"
source: https://nodejs.org/api/events.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 2/2
---

### `events.setMaxListeners(n[, ...eventTargets])`

- `n` `<number>` A non-negative number. The maximum number of listeners per `EventTarget` event.
- `...eventsTargets` `<EventTarget>`[] | `<EventEmitter>`[] Zero or more `<EventTarget>` or `<EventEmitter>` instances. If none are specified, `n` is set as the default max for all newly created `<EventTarget>` and `<EventEmitter>` objects.

```mjs
import { setMaxListeners, EventEmitter } from 'node:events';

const target = new EventTarget();
const emitter = new EventEmitter();

setMaxListeners(5, target, emitter);
const {
  setMaxListeners,
  EventEmitter,
} = require('node:events');

const target = new EventTarget();
const emitter = new EventEmitter();

setMaxListeners(5, target, emitter);
```

### `events.addAbortListener(signal, listener)`

- `signal` `<AbortSignal>`
- `listener` `<Function>` | `<EventListener>`
- Returns: `<Disposable>` A Disposable that removes the `abort` listener.

Listens once to the `abort` event on the provided `signal`.

Listening to the `abort` event on abort signals is unsafe and may lead to resource leaks since another third party with the signal can call `e.stopImmediatePropagation()`. Unfortunately Node.js cannot change this since it would violate the web standard. Additionally, the original API makes it easy to forget to remove listeners.

This API allows safely using `AbortSignal`s in Node.js APIs by solving these two issues by listening to the event such that `stopImmediatePropagation` does not prevent the listener from running.

Returns a disposable so that it may be unsubscribed from more easily.const { addAbortListener } = require('node:events'); function example(signal) { signal.addEventListener('abort', (e) => e.stopImmediatePropagation()); // addAbortListener() returns a disposable, so the `using` keyword ensures // the abort listener is automatically removed when this scope exits. using _ = addAbortListener(signal, (e) => { // Do something when signal is aborted. }); }import { addAbortListener } from 'node:events'; function example(signal) { signal.addEventListener('abort', (e) => e.stopImmediatePropagation()); // addAbortListener() returns a disposable, so the `using` keyword ensures // the abort listener is automatically removed when this scope exits. using _ = addAbortListener(signal, (e) => { // Do something when signal is aborted. }); }

### Class: `events.EventEmitterAsyncResource extends EventEmitter`

Integrates `EventEmitter` with `<AsyncResource>` for `EventEmitter`s that require manual async tracking. Specifically, all events emitted by instances of `events.EventEmitterAsyncResource` will run within its async context.`import { EventEmitterAsyncResource, EventEmitter } from 'node:events'; import { notStrictEqual, strictEqual } from 'node:assert'; import { executionAsyncId, triggerAsyncId } from 'node:async_hooks'; // Async tracking tooling will identify this as 'Q'. const ee1 = new EventEmitterAsyncResource({ name: 'Q' }); // 'foo' listeners will run in the EventEmitters async context. ee1.on('foo', () => { strictEqual(executionAsyncId(), ee1.asyncId); strictEqual(triggerAsyncId(), ee1.triggerAsyncId); }); const ee2 = new EventEmitter(); // 'foo' listeners on ordinary EventEmitters that do not track async // context, however, run in the same async context as the emit(). ee2.on('foo', () => { notStrictEqual(executionAsyncId(), ee2.asyncId); notStrictEqual(triggerAsyncId(), ee2.triggerAsyncId); }); Promise.resolve().then(() => { ee1.emit('foo'); ee2.emit('foo'); });``const { EventEmitterAsyncResource, EventEmitter } = require('node:events'); const { notStrictEqual, strictEqual } = require('node:assert'); const { executionAsyncId, triggerAsyncId } = require('node:async_hooks'); // Async tracking tooling will identify this as 'Q'. const ee1 = new EventEmitterAsyncResource({ name: 'Q' }); // 'foo' listeners will run in the EventEmitters async context. ee1.on('foo', () => { strictEqual(executionAsyncId(), ee1.asyncId); strictEqual(triggerAsyncId(), ee1.triggerAsyncId); }); const ee2 = new EventEmitter(); // 'foo' listeners on ordinary EventEmitters that do not track async // context, however, run in the same async context as the emit(). ee2.on('foo', () => { notStrictEqual(executionAsyncId(), ee2.asyncId); notStrictEqual(triggerAsyncId(), ee2.triggerAsyncId); }); Promise.resolve().then(() => { ee1.emit('foo'); ee2.emit('foo'); });`

The `EventEmitterAsyncResource` class has the same methods and takes the same options as `EventEmitter` and `AsyncResource` themselves.

#### `new events.EventEmitterAsyncResource([options])`

- `options` `<Object>`
  - `captureRejections` `<boolean>` It enables automatic capturing of promise rejection. **Default:** `false`.
  - `name` `<string>` The type of async event. **Default:** `new.target.name`.
  - `triggerAsyncId` `<number>` The ID of the execution context that created this async event. **Default:** `executionAsyncId()`.
  - `requireManualDestroy` `<boolean>` If set to `true`, disables `emitDestroy` when the object is garbage collected. This usually does not need to be set (even if `emitDestroy` is called manually), unless the resource's `asyncId` is retrieved and the sensitive API's `emitDestroy` is called with it. When set to `false`, the `emitDestroy` call on garbage collection will only take place if there is at least one active `destroy` hook. **Default:** `false`.

#### `eventemitterasyncresource.asyncId`

- Type: `<number>` The unique `asyncId` assigned to the resource.

#### `eventemitterasyncresource.asyncResource`

- Type: `<AsyncResource>` The underlying `<AsyncResource>`.

The returned `AsyncResource` object has an additional `eventEmitter` property that provides a reference to this `EventEmitterAsyncResource`.

#### `eventemitterasyncresource.emitDestroy()`

Call all `destroy` hooks. This should only ever be called once. An error will be thrown if it is called more than once. This **must** be manually called. If the resource is left to be collected by the GC then the `destroy` hooks will never be called.

#### `eventemitterasyncresource.triggerAsyncId`

- Type: `<number>` The same `triggerAsyncId` that is passed to the `AsyncResource` constructor.

### `EventTarget` and `Event` API

The `EventTarget` and `Event` objects are a Node.js-specific implementation of the `EventTarget` Web API that are exposed by some Node.js core APIs.`const target = new EventTarget(); target.addEventListener('foo', (event) => { console.log('foo event happened!'); });`

#### Node.js `EventTarget` vs. DOM `EventTarget`

There are two key differences between the Node.js `EventTarget` and the `EventTarget` Web API: Whereas DOM `EventTarget` instances *may* be hierarchical, there is no concept of hierarchy and event propagation in Node.js. That is, an event dispatched to an `EventTarget` does not propagate through a hierarchy of nested target objects that may each have their own set of handlers for the event. In the Node.js `EventTarget`, if an event listener is an async function or returns a `Promise`, and the returned `Promise` rejects, the rejection is automatically captured and handled the same way as a listener that throws synchronously (see `EventTarget` error handling for details).

#### `NodeEventTarget` vs. `EventEmitter`

The `NodeEventTarget` object implements a modified subset of the `EventEmitter` API that allows it to closely *emulate* an `EventEmitter` in certain situations. A `NodeEventTarget` is *not* an instance of `EventEmitter` and cannot be used in place of an `EventEmitter` in most cases. Unlike `EventEmitter`, any given `listener` can be registered at most once per event `type`. Attempts to register a `listener` multiple times are ignored. The `NodeEventTarget` does not emulate the full `EventEmitter` API. Specifically the `prependListener()`, `prependOnceListener()`, `rawListeners()`, and `errorMonitor` APIs are not emulated. The `'newListener'` and `'removeListener'` events will also not be emitted. The `NodeEventTarget` does not implement any special default behavior for events with type `'error'`. The `NodeEventTarget` supports `EventListener` objects as well as functions as handlers for all event types.

#### Event listener

Event listeners registered for an event `type` may either be JavaScript functions or objects with a `handleEvent` property whose value is a function.

In either case, the handler function is invoked with the `event` argument passed to the `eventTarget.dispatchEvent()` function.

Async functions may be used as event listeners. If an async handler function rejects, the rejection is captured and handled as described in `EventTarget` error handling.

An error thrown by one handler function does not prevent the other handlers from being invoked.

The return value of a handler function is ignored.

Handlers are always invoked in the order they were added.

Handler functions may mutate the `event` object.`function handler1(event) { console.log(event.type); // Prints 'foo' event.a = 1; } async function handler2(event) { console.log(event.type); // Prints 'foo' console.log(event.a); // Prints 1 } const handler3 = { handleEvent(event) { console.log(event.type); // Prints 'foo' }, }; const handler4 = { async handleEvent(event) { console.log(event.type); // Prints 'foo' }, }; const target = new EventTarget(); target.addEventListener('foo', handler1); target.addEventListener('foo', handler2); target.addEventListener('foo', handler3); target.addEventListener('foo', handler4, { once: true });`

#### `EventTarget` error handling

When a registered event listener throws (or returns a Promise that rejects), by default the error is treated as an uncaught exception on `process.nextTick()`. This means uncaught exceptions in `EventTarget`s will terminate the Node.js process by default.

Throwing within an event listener will *not* stop the other registered handlers from being invoked.

The `EventTarget` does not implement any special default handling for `'error'` type events like `EventEmitter`.

Currently errors are first forwarded to the `process.on('error')` event before reaching `process.on('uncaughtException')`. This behavior is deprecated and will change in a future release to align `EventTarget` with other Node.js APIs. Any code relying on the `process.on('error')` event should be aligned with the new behavior.

#### Class: `Event`

The `Event` object is an adaptation of the `Event` Web API. Instances are created internally by Node.js.

##### `event.bubbles`

- Type: `<boolean>` Always returns `false`.

This is not used in Node.js and is provided purely for completeness.

##### `event.cancelBubble`

Stability: 3 - Legacy: Use `event.stopPropagation()` instead.

- Type: `<boolean>`

Alias for `event.stopPropagation()` if set to `true`. This is not used in Node.js and is provided purely for completeness.

##### `event.cancelable`

- Type: `<boolean>` True if the event was created with the `cancelable` option.

##### `event.composed`

- Type: `<boolean>` Always returns `false`.

This is not used in Node.js and is provided purely for completeness.

##### `event.composedPath()`

Returns an array containing the current `EventTarget` as the only entry or empty if the event is not being dispatched. This is not used in Node.js and is provided purely for completeness.

##### `event.currentTarget`

- Type: `<EventTarget>` The `EventTarget` dispatching the event.

Alias for `event.target`.

##### `event.defaultPrevented`

- Type: `<boolean>`

Is `true` if `cancelable` is `true` and `event.preventDefault()` has been called.

##### `event.eventPhase`

- Type: `<number>` Returns `0` while an event is not being dispatched, `2` while it is being dispatched.

This is not used in Node.js and is provided purely for completeness.

##### `event.initEvent(type[, bubbles[, cancelable]])`

Stability: 3 - Legacy: The WHATWG spec considers it deprecated and users shouldn't use it at all.

- `type` `<string>`
- `bubbles` `<boolean>`
- `cancelable` `<boolean>`

Redundant with event constructors and incapable of setting `composed`. This is not used in Node.js and is provided purely for completeness.

##### `event.isTrusted`

- Type: `<boolean>`

The `<AbortSignal>` `"abort"` event is emitted with `isTrusted` set to `true`. The value is `false` in all other cases.

##### `event.preventDefault()`

Sets the `defaultPrevented` property to `true` if `cancelable` is `true`.

##### `event.returnValue`

Stability: 3 - Legacy: Use `event.defaultPrevented` instead.

- Type: `<boolean>` True if the event has not been canceled.

The value of `event.returnValue` is always the opposite of `event.defaultPrevented`. This is not used in Node.js and is provided purely for completeness.

##### `event.srcElement`

Stability: 3 - Legacy: Use `event.target` instead.

- Type: `<EventTarget>` The `EventTarget` dispatching the event.

Alias for `event.target`.

##### `event.stopImmediatePropagation()`

Stops the invocation of event listeners after the current one completes.

##### `event.stopPropagation()`

This is not used in Node.js and is provided purely for completeness.

##### `event.target`

- Type: `<EventTarget>` The `EventTarget` dispatching the event.

##### `event.timeStamp`

- Type: `<number>`

The millisecond timestamp when the `Event` object was created.

##### `event.type`

- Type: `<string>`

The event type identifier.

#### Class: `EventTarget`

##### `eventTarget.addEventListener(type, listener[, options])`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- `options` `<Object>`
  - `once` `<boolean>` When `true`, the listener is automatically removed when it is first invoked. **Default:** `false`.
  - `passive` `<boolean>` When `true`, serves as a hint that the listener will not call the `Event` object's `preventDefault()` method. **Default:** `false`.
  - `capture` `<boolean>` Not directly used by Node.js. Added for API completeness. **Default:** `false`.
  - `signal` `<AbortSignal>` The listener will be removed when the given AbortSignal object's `abort()` method is called.

Adds a new handler for the `type` event. Any given `listener` is added only once per `type` and per `capture` option value.

If the `once` option is `true`, the `listener` is removed after the next time a `type` event is dispatched.

The `capture` option is not used by Node.js in any functional way other than tracking registered event listeners per the `EventTarget` specification. Specifically, the `capture` option is used as part of the key when registering a `listener`. Any individual `listener` may be added once with `capture = false`, and once with `capture = true`.`function handler(event) {} const target = new EventTarget(); target.addEventListener('foo', handler, { capture: true }); // first target.addEventListener('foo', handler, { capture: false }); // second // Removes the second instance of handler target.removeEventListener('foo', handler); // Removes the first instance of handler target.removeEventListener('foo', handler, { capture: true });`

##### `eventTarget.dispatchEvent(event)`

- `event` `<Event>`
- Returns: `<boolean>` `true` if either event's `cancelable` attribute value is false or its `preventDefault()` method was not invoked, otherwise `false`.

Dispatches the `event` to the list of handlers for `event.type`.

The registered event listeners is synchronously invoked in the order they were registered.

##### `eventTarget.removeEventListener(type, listener[, options])`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- `options` `<Object>`
  - `capture` `<boolean>`

Removes the `listener` from the list of handlers for event `type`.

#### Class: `CustomEvent`

- Extends: `<Event>`

The `CustomEvent` object is an adaptation of the `CustomEvent` Web API. Instances are created internally by Node.js.

##### `event.detail`

- Type: `<any>` Returns custom data passed when initializing.

Read-only.

#### Class: `NodeEventTarget`

- Extends: `<EventTarget>`

The `NodeEventTarget` is a Node.js-specific extension to `EventTarget` that emulates a subset of the `EventEmitter` API.

##### `nodeEventTarget.addListener(type, listener)`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- Returns: `<EventTarget>` this

Node.js-specific extension to the `EventTarget` class that emulates the equivalent `EventEmitter` API. The only difference between `addListener()` and `addEventListener()` is that `addListener()` will return a reference to the `EventTarget`.

##### `nodeEventTarget.emit(type, arg)`

- `type` `<string>`
- `arg` `<any>`
- Returns: `<boolean>` `true` if event listeners registered for the `type` exist, otherwise `false`.

Node.js-specific extension to the `EventTarget` class that dispatches the `arg` to the list of handlers for `type`.

##### `nodeEventTarget.eventNames()`

- Returns: `<string>`[]

Node.js-specific extension to the `EventTarget` class that returns an array of event `type` names for which event listeners are registered.

##### `nodeEventTarget.listenerCount(type)`

- `type` `<string>`
- Returns: `<number>`

Node.js-specific extension to the `EventTarget` class that returns the number of event listeners registered for the `type`.

##### `nodeEventTarget.setMaxListeners(n)`

- `n` `<number>`

Node.js-specific extension to the `EventTarget` class that sets the number of max event listeners as `n`.

##### `nodeEventTarget.getMaxListeners()`

- Returns: `<number>`

Node.js-specific extension to the `EventTarget` class that returns the number of max event listeners.

##### `nodeEventTarget.off(type, listener[, options])`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- `options` `<Object>`
  - `capture` `<boolean>`
- Returns: `<EventTarget>` this

Node.js-specific alias for `eventTarget.removeEventListener()`.

##### `nodeEventTarget.on(type, listener)`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- Returns: `<EventTarget>` this

Node.js-specific alias for `eventTarget.addEventListener()`.

##### `nodeEventTarget.once(type, listener)`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- Returns: `<EventTarget>` this

Node.js-specific extension to the `EventTarget` class that adds a `once` listener for the given event `type`. This is equivalent to calling `on` with the `once` option set to `true`.

##### `nodeEventTarget.removeAllListeners([type])`

- `type` `<string>`
- Returns: `<EventTarget>` this

Node.js-specific extension to the `EventTarget` class. If `type` is specified, removes all registered listeners for `type`, otherwise removes all registered listeners.

##### `nodeEventTarget.removeListener(type, listener[, options])`

- `type` `<string>`
- `listener` `<Function>` | `<EventListener>`
- `options` `<Object>`
  - `capture` `<boolean>`
- Returns: `<EventTarget>` this

Node.js-specific extension to the `EventTarget` class that removes the `listener` for the given `type`. The only difference between `removeListener()` and `removeEventListener()` is that `removeListener()` will return a reference to the `EventTarget`.
