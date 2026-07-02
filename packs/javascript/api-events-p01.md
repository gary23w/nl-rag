---
title: "Events (part 1/2)"
source: https://nodejs.org/api/events.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 1/2
---

# Events

Node.js

# Node.js v26.4.0 documentation

- Node.js v26.4.0
- Table of contents
- IndexIndex
- Other versions26.x 25.x 24.x **LTS**23.x 22.x **LTS**21.x 20.x 19.x 18.x 17.x 16.x 15.x 14.x 13.x 12.x 11.x 10.x 9.x 8.x 7.x 6.x 5.x 4.x 0.12.x 0.10.x
- Options View on single page View as JSON

## Events

Stability: 2 - Stable

Much of the Node.js core API is built around an idiomatic asynchronous event-driven architecture in which certain kinds of objects (called "emitters") emit named events that cause `Function` objects ("listeners") to be called.

For instance: a `net.Server` object emits an event each time a peer connects to it; a `fs.ReadStream` emits an event when the file is opened; a stream emits an event whenever data is available to be read.

All objects that emit events are instances of the `EventEmitter` class. These objects expose an `eventEmitter.on()` function that allows one or more functions to be attached to named events emitted by the object. Typically, event names are camel-cased strings but any valid JavaScript property key can be used.

When the `EventEmitter` object emits an event, all of the functions attached to that specific event are called *synchronously*. Any values returned by the called listeners are *ignored* and discarded.

The following example shows a simple `EventEmitter` instance with a single listener. The `eventEmitter.on()` method is used to register listeners, while the `eventEmitter.emit()` method is used to trigger the event.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', () => { console.log('an event occurred!'); }); myEmitter.emit('event');``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', () => { console.log('an event occurred!'); }); myEmitter.emit('event');`

### Passing arguments and `this` to listeners

The `eventEmitter.emit()` method allows an arbitrary set of arguments to be passed to the listener functions. Keep in mind that when an ordinary listener function is called, the standard `this` keyword is intentionally set to reference the `EventEmitter` instance to which the listener is attached.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', function(a, b) { console.log(a, b, this, this === myEmitter); // Prints: // a b MyEmitter { // _events: [Object: null prototype] { event: [Function (anonymous)] }, // _eventsCount: 1, // _maxListeners: undefined, // Symbol(shapeMode): false, // Symbol(kCapture): false // } true }); myEmitter.emit('event', 'a', 'b');``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', function(a, b) { console.log(a, b, this, this === myEmitter); // Prints: // a b MyEmitter { // _events: [Object: null prototype] { event: [Function (anonymous)] }, // _eventsCount: 1, // _maxListeners: undefined, // Symbol(shapeMode): false, // Symbol(kCapture): false // } true }); myEmitter.emit('event', 'a', 'b');`

It is possible to use ES6 Arrow Functions as listeners, however, when doing so, the `this` keyword will no longer reference the `EventEmitter` instance:`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', (a, b) => { console.log(a, b, this); // Prints: a b undefined }); myEmitter.emit('event', 'a', 'b');``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', (a, b) => { console.log(a, b, this); // Prints: a b {} }); myEmitter.emit('event', 'a', 'b');`

### Asynchronous vs. synchronous

The `EventEmitter` calls all listeners synchronously in the order in which they were registered. This ensures the proper sequencing of events and helps avoid race conditions and logic errors. When appropriate, listener functions can switch to an asynchronous mode of operation using the `setImmediate()` or `process.nextTick()` methods:`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', (a, b) => { setImmediate(() => { console.log('this happens asynchronously'); }); }); myEmitter.emit('event', 'a', 'b');``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('event', (a, b) => { setImmediate(() => { console.log('this happens asynchronously'); }); }); myEmitter.emit('event', 'a', 'b');`

### Handling events only once

When a listener is registered using the `eventEmitter.on()` method, that listener is invoked *every time* the named event is emitted.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); let m = 0; myEmitter.on('event', () => { console.log(++m); }); myEmitter.emit('event'); // Prints: 1 myEmitter.emit('event'); // Prints: 2``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); let m = 0; myEmitter.on('event', () => { console.log(++m); }); myEmitter.emit('event'); // Prints: 1 myEmitter.emit('event'); // Prints: 2`

Using the `eventEmitter.once()` method, it is possible to register a listener that is called at most once for a particular event. Once the event is emitted, the listener is unregistered and *then* called.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); let m = 0; myEmitter.once('event', () => { console.log(++m); }); myEmitter.emit('event'); // Prints: 1 myEmitter.emit('event'); // Ignored``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); let m = 0; myEmitter.once('event', () => { console.log(++m); }); myEmitter.emit('event'); // Prints: 1 myEmitter.emit('event'); // Ignored`

### Error events

When an error occurs within an `EventEmitter` instance, the typical action is for an `'error'` event to be emitted. These are treated as special cases within Node.js.

If an `EventEmitter` does *not* have at least one listener registered for the `'error'` event, and an `'error'` event is emitted, the error is thrown, a stack trace is printed, and the Node.js process exits.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.emit('error', new Error('whoops!')); // Throws and crashes Node.js``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.emit('error', new Error('whoops!')); // Throws and crashes Node.js`

To guard against crashing the Node.js process the `domain` module can be used. (Note, however, that the `node:domain` module is deprecated.)

As a best practice, listeners should always be added for the `'error'` events.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('error', (err) => { console.error('whoops! there was an error'); }); myEmitter.emit('error', new Error('whoops!')); // Prints: whoops! there was an error``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); myEmitter.on('error', (err) => { console.error('whoops! there was an error'); }); myEmitter.emit('error', new Error('whoops!')); // Prints: whoops! there was an error`

It is possible to monitor `'error'` events without consuming the emitted error by installing a listener using the symbol `events.errorMonitor`.`import { EventEmitter, errorMonitor } from 'node:events'; const myEmitter = new EventEmitter(); myEmitter.on(errorMonitor, (err) => { MyMonitoringTool.log(err); }); myEmitter.emit('error', new Error('whoops!')); // Still throws and crashes Node.js``const { EventEmitter, errorMonitor } = require('node:events'); const myEmitter = new EventEmitter(); myEmitter.on(errorMonitor, (err) => { MyMonitoringTool.log(err); }); myEmitter.emit('error', new Error('whoops!')); // Still throws and crashes Node.js`

### Capture rejections of promises

Using `async` functions with event handlers is problematic, because it can lead to an unhandled rejection in case of a thrown exception:`import { EventEmitter } from 'node:events'; const ee = new EventEmitter(); ee.on('something', async (value) => { throw new Error('kaboom'); });``const EventEmitter = require('node:events'); const ee = new EventEmitter(); ee.on('something', async (value) => { throw new Error('kaboom'); });`

The `captureRejections` option in the `EventEmitter` constructor or the global setting change this behavior, installing a `.then(undefined, handler)` handler on the `Promise`. This handler routes the exception asynchronously to the `Symbol.for('nodejs.rejection')` method if there is one, or to `'error'` event handler if there is none.`import { EventEmitter } from 'node:events'; const ee1 = new EventEmitter({ captureRejections: true }); ee1.on('something', async (value) => { throw new Error('kaboom'); }); ee1.on('error', console.log); const ee2 = new EventEmitter({ captureRejections: true }); ee2.on('something', async (value) => { throw new Error('kaboom'); }); ee2[Symbol.for('nodejs.rejection')] = console.log;``const EventEmitter = require('node:events'); const ee1 = new EventEmitter({ captureRejections: true }); ee1.on('something', async (value) => { throw new Error('kaboom'); }); ee1.on('error', console.log); const ee2 = new EventEmitter({ captureRejections: true }); ee2.on('something', async (value) => { throw new Error('kaboom'); }); ee2[Symbol.for('nodejs.rejection')] = console.log;`

Setting `events.captureRejections = true` will change the default for all new instances of `EventEmitter`.`import { EventEmitter } from 'node:events'; EventEmitter.captureRejections = true; const ee1 = new EventEmitter(); ee1.on('something', async (value) => { throw new Error('kaboom'); }); ee1.on('error', console.log);``const events = require('node:events'); events.captureRejections = true; const ee1 = new events.EventEmitter(); ee1.on('something', async (value) => { throw new Error('kaboom'); }); ee1.on('error', console.log);`

The `'error'` events that are generated by the `captureRejections` behavior do not have a catch handler to avoid infinite error loops: the recommendation is to **not use `async` functions as `'error'` event handlers**.

### Class: `EventEmitter`

The `EventEmitter` class is defined and exposed by the `node:events` module:`import { EventEmitter } from 'node:events';``const EventEmitter = require('node:events');`

All `EventEmitter`s emit the event `'newListener'` when new listeners are added and `'removeListener'` when existing listeners are removed.

It supports the following option: `captureRejections` `<boolean>` It enables automatic capturing of promise rejection. **Default:** `false`.

#### Event: `'newListener'`

- `eventName` `<string>` | `<symbol>` The name of the event being listened for
- `listener` `<Function>` The event handler function

The `EventEmitter` instance will emit its own `'newListener'` event *before* a listener is added to its internal array of listeners.

Listeners registered for the `'newListener'` event are passed the event name and a reference to the listener being added.

The fact that the event is triggered before adding the listener has a subtle but important side effect: any *additional* listeners registered to the same `name` *within* the `'newListener'` callback are inserted *before* the listener that is in the process of being added.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); // Only do this once so we don't loop forever myEmitter.once('newListener', (event, listener) => { if (event === 'event') { // Insert a new listener in front myEmitter.on('event', () => { console.log('B'); }); } }); myEmitter.on('event', () => { console.log('A'); }); myEmitter.emit('event'); // Prints: // B // A``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); // Only do this once so we don't loop forever myEmitter.once('newListener', (event, listener) => { if (event === 'event') { // Insert a new listener in front myEmitter.on('event', () => { console.log('B'); }); } }); myEmitter.on('event', () => { console.log('A'); }); myEmitter.emit('event'); // Prints: // B // A`

#### Event: `'removeListener'`

- `eventName` `<string>` | `<symbol>` The event name
- `listener` `<Function>` The event handler function

The `'removeListener'` event is emitted *after* the `listener` is removed.

#### `emitter.addListener(eventName, listener)`

- `eventName` `<string>` | `<symbol>`
- `listener` `<Function>`

Alias for `emitter.on(eventName, listener)`.

#### `emitter.emit(eventName[, ...args])`

- `eventName` `<string>` | `<symbol>`
- `...args` `<any>`
- Returns: `<boolean>`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments to each.

Returns `true` if the event had listeners, `false` otherwise.import { EventEmitter } from 'node:events'; const myEmitter = new EventEmitter(); // First listener myEmitter.on('event', function firstListener() { console.log('Helloooo! first listener'); }); // Second listener myEmitter.on('event', function secondListener(arg1, arg2) { console.log(`event with parameters ${arg1}, ${arg2} in second listener`); }); // Third listener myEmitter.on('event', function thirdListener(...args) { const parameters = args.join(', '); console.log(`event with parameters ${parameters} in third listener`); }); console.log(myEmitter.listeners('event')); myEmitter.emit('event', 1, 2, 3, 4, 5); // Prints: // [ // [Function: firstListener], // [Function: secondListener], // [Function: thirdListener] // ] // Helloooo! first listener // event with parameters 1, 2 in second listener // event with parameters 1, 2, 3, 4, 5 in third listenerconst EventEmitter = require('node:events'); const myEmitter = new EventEmitter(); // First listener myEmitter.on('event', function firstListener() { console.log('Helloooo! first listener'); }); // Second listener myEmitter.on('event', function secondListener(arg1, arg2) { console.log(`event with parameters ${arg1}, ${arg2} in second listener`); }); // Third listener myEmitter.on('event', function thirdListener(...args) { const parameters = args.join(', '); console.log(`event with parameters ${parameters} in third listener`); }); console.log(myEmitter.listeners('event')); myEmitter.emit('event', 1, 2, 3, 4, 5); // Prints: // [ // [Function: firstListener], // [Function: secondListener], // [Function: thirdListener] // ] // Helloooo! first listener // event with parameters 1, 2 in second listener // event with parameters 1, 2, 3, 4, 5 in third listener

#### `emitter.eventNames()`

- Returns: `<string>`[] | `<symbol>`[]

Returns an array listing the events for which the emitter has registered listeners.`import { EventEmitter } from 'node:events'; const myEE = new EventEmitter(); myEE.on('foo', () => {}); myEE.on('bar', () => {}); const sym = Symbol('symbol'); myEE.on(sym, () => {}); console.log(myEE.eventNames()); // Prints: [ 'foo', 'bar', Symbol(symbol) ]``const EventEmitter = require('node:events'); const myEE = new EventEmitter(); myEE.on('foo', () => {}); myEE.on('bar', () => {}); const sym = Symbol('symbol'); myEE.on(sym, () => {}); console.log(myEE.eventNames()); // Prints: [ 'foo', 'bar', Symbol(symbol) ]`

#### `emitter.getMaxListeners()`

- Returns: `<integer>`

Returns the current max listener value for the `EventEmitter` which is either set by `emitter.setMaxListeners(n)` or defaults to `events.defaultMaxListeners`.

#### `emitter.listenerCount(eventName[, listener])`

- `eventName` `<string>` | `<symbol>` The name of the event being listened for
- `listener` `<Function>` The event handler function
- Returns: `<integer>`

Returns the number of listeners listening for the event named `eventName`. If `listener` is provided, it will return how many times the listener is found in the list of the listeners of the event.

#### `emitter.listeners(eventName)`

- `eventName` `<string>` | `<symbol>`
- Returns: `<Function>`[]

Returns a copy of the array of listeners for the event named `eventName`.`server.on('connection', (stream) => { console.log('someone connected!'); }); console.log(util.inspect(server.listeners('connection'))); // Prints: [ [Function] ]`

#### `emitter.off(eventName, listener)`

- `eventName` `<string>` | `<symbol>`
- `listener` `<Function>`
- Returns: `<EventEmitter>`

Alias for `emitter.removeListener()`.

#### `emitter.on(eventName, listener)`

- `eventName` `<string>` | `<symbol>` The name of the event.
- `listener` `<Function>` The callback function
- Returns: `<EventEmitter>`

Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.`server.on('connection', (stream) => { console.log('someone connected!'); });`

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.`import { EventEmitter } from 'node:events'; const myEE = new EventEmitter(); myEE.on('foo', () => console.log('a')); myEE.prependListener('foo', () => console.log('b')); myEE.emit('foo'); // Prints: // b // a``const EventEmitter = require('node:events'); const myEE = new EventEmitter(); myEE.on('foo', () => console.log('a')); myEE.prependListener('foo', () => console.log('b')); myEE.emit('foo'); // Prints: // b // a`

#### `emitter.once(eventName, listener)`

- `eventName` `<string>` | `<symbol>` The name of the event.
- `listener` `<Function>` The callback function
- Returns: `<EventEmitter>`

Adds a **one-time** `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.`server.once('connection', (stream) => { console.log('Ah, we have our first user!'); });`

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.`import { EventEmitter } from 'node:events'; const myEE = new EventEmitter(); myEE.once('foo', () => console.log('a')); myEE.prependOnceListener('foo', () => console.log('b')); myEE.emit('foo'); // Prints: // b // a``const EventEmitter = require('node:events'); const myEE = new EventEmitter(); myEE.once('foo', () => console.log('a')); myEE.prependOnceListener('foo', () => console.log('b')); myEE.emit('foo'); // Prints: // b // a`

#### `emitter.prependListener(eventName, listener)`

- `eventName` `<string>` | `<symbol>` The name of the event.
- `listener` `<Function>` The callback function
- Returns: `<EventEmitter>`

Adds the `listener` function to the *beginning* of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.`server.prependListener('connection', (stream) => { console.log('someone connected!'); });`

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### `emitter.prependOnceListener(eventName, listener)`

- `eventName` `<string>` | `<symbol>` The name of the event.
- `listener` `<Function>` The callback function
- Returns: `<EventEmitter>`

Adds a **one-time** `listener` function for the event named `eventName` to the *beginning* of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.`server.prependOnceListener('connection', (stream) => { console.log('Ah, we have our first user!'); });`

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### `emitter.removeAllListeners([eventName])`

- `eventName` `<string>` | `<symbol>`
- Returns: `<EventEmitter>`

Removes all listeners, or those of the specified `eventName`.

It is bad practice to remove listeners added elsewhere in the code, particularly when the `EventEmitter` instance was created by some other component or module (e.g. sockets or file streams).

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### `emitter.removeListener(eventName, listener)`

- `eventName` `<string>` | `<symbol>`
- `listener` `<Function>`
- Returns: `<EventEmitter>`

Removes the specified `listener` from the listener array for the event named `eventName`.`const callback = (stream) => { console.log('someone connected!'); }; server.on('connection', callback); // ... server.removeListener('connection', callback);`

`removeListener()` will remove, at most, one instance of a listener from the listener array. If any single listener has been added multiple times to the listener array for the specified `eventName`, then `removeListener()` must be called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the time of emitting are called in order. This implies that any `removeListener()` or `removeAllListeners()` calls *after* emitting and *before* the last listener finishes execution will not remove them from `emit()` in progress. Subsequent events behave as expected.`import { EventEmitter } from 'node:events'; class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); const callbackA = () => { console.log('A'); myEmitter.removeListener('event', callbackB); }; const callbackB = () => { console.log('B'); }; myEmitter.on('event', callbackA); myEmitter.on('event', callbackB); // callbackA removes listener callbackB but it will still be called. // Internal listener array at time of emit [callbackA, callbackB] myEmitter.emit('event'); // Prints: // A // B // callbackB is now removed. // Internal listener array [callbackA] myEmitter.emit('event'); // Prints: // A``const EventEmitter = require('node:events'); class MyEmitter extends EventEmitter {} const myEmitter = new MyEmitter(); const callbackA = () => { console.log('A'); myEmitter.removeListener('event', callbackB); }; const callbackB = () => { console.log('B'); }; myEmitter.on('event', callbackA); myEmitter.on('event', callbackB); // callbackA removes listener callbackB but it will still be called. // Internal listener array at time of emit [callbackA, callbackB] myEmitter.emit('event'); // Prints: // A // B // callbackB is now removed. // Internal listener array [callbackA] myEmitter.emit('event'); // Prints: // A`

Because listeners are managed using an internal array, calling this will change the position indexes of any listener registered *after* the listener being removed. This will not impact the order in which listeners are called, but it means that any copies of the listener array as returned by the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single event (as in the example below), `removeListener()` will remove the most recently added instance. In the example the `once('ping')` listener is removed:`import { EventEmitter } from 'node:events'; const ee = new EventEmitter(); function pong() { console.log('pong'); } ee.on('ping', pong); ee.once('ping', pong); ee.removeListener('ping', pong); ee.emit('ping'); ee.emit('ping');``const EventEmitter = require('node:events'); const ee = new EventEmitter(); function pong() { console.log('pong'); } ee.on('ping', pong); ee.once('ping', pong); ee.removeListener('ping', pong); ee.emit('ping'); ee.emit('ping');`

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### `emitter.setMaxListeners(n)`

- `n` `<integer>`
- Returns: `<EventEmitter>`

By default `EventEmitter`s will print a warning if more than `10` listeners are added for a particular event. This is a useful default that helps finding memory leaks. The `emitter.setMaxListeners()` method allows the limit to be modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### `emitter.rawListeners(eventName)`

- `eventName` `<string>` | `<symbol>`
- Returns: `<Function>`[]

Returns a copy of the array of listeners for the event named `eventName`, including any wrappers (such as those created by `.once()`).import { EventEmitter } from 'node:events'; const emitter = new EventEmitter(); emitter.once('log', () => console.log('log once')); // Returns a new Array with a function `onceWrapper` which has a property // `listener` which contains the original listener bound above const listeners = emitter.rawListeners('log'); const logFnWrapper = listeners[0]; // Logs "log once" to the console and does not unbind the `once` event logFnWrapper.listener(); // Logs "log once" to the console and removes the listener logFnWrapper(); emitter.on('log', () => console.log('log persistently')); // Will return a new Array with a single function bound by `.on()` above const newListeners = emitter.rawListeners('log'); // Logs "log persistently" twice newListeners[0](); emitter.emit('log');const EventEmitter = require('node:events'); const emitter = new EventEmitter(); emitter.once('log', () => console.log('log once')); // Returns a new Array with a function `onceWrapper` which has a property // `listener` which contains the original listener bound above const listeners = emitter.rawListeners('log'); const logFnWrapper = listeners[0]; // Logs "log once" to the console and does not unbind the `once` event logFnWrapper.listener(); // Logs "log once" to the console and removes the listener logFnWrapper(); emitter.on('log', () => console.log('log persistently')); // Will return a new Array with a single function bound by `.on()` above const newListeners = emitter.rawListeners('log'); // Logs "log persistently" twice newListeners[0](); emitter.emit('log');

#### `emitter[Symbol.for('nodejs.rejection')](err, eventName[, ...args])`

- `err` `<Error>`
- `eventName` `<string>` | `<symbol>`
- `...args` `<any>`

The `Symbol.for('nodejs.rejection')` method is called in case a promise rejection happens when emitting an event and `captureRejections` is enabled on the emitter. It is possible to use `events.captureRejectionSymbol` in place of `Symbol.for('nodejs.rejection')`.`import { EventEmitter, captureRejectionSymbol } from 'node:events'; class MyClass extends EventEmitter { constructor() { super({ captureRejections: true }); } [captureRejectionSymbol](err, event, ...args) { console.log('rejection happened for', event, 'with', err, ...args); this.destroy(err); } destroy(err) { // Tear the resource down here. } }``const { EventEmitter, captureRejectionSymbol } = require('node:events'); class MyClass extends EventEmitter { constructor() { super({ captureRejections: true }); } [captureRejectionSymbol](err, event, ...args) { console.log('rejection happened for', event, 'with', err, ...args); this.destroy(err); } destroy(err) { // Tear the resource down here. } }`

### `events.defaultMaxListeners`

By default, a maximum of `10` listeners can be registered for any single event. This limit can be changed for individual `EventEmitter` instances using the `emitter.setMaxListeners(n)` method. To change the default for *all* `EventEmitter` instances, the `events.defaultMaxListeners` property can be used. If this value is not a positive number, a `RangeError` is thrown.

Take caution when setting the `events.defaultMaxListeners` because the change affects *all* `EventEmitter` instances, including those created before the change is made. However, calling `emitter.setMaxListeners(n)` still has precedence over `events.defaultMaxListeners`.

This is not a hard limit. The `EventEmitter` instance will allow more listeners to be added but will output a trace warning to stderr indicating that a "possible EventEmitter memory leak" has been detected. For any single `EventEmitter`, the `emitter.getMaxListeners()` and `emitter.setMaxListeners()` methods can be used to temporarily avoid this warning:

`defaultMaxListeners` has no effect on `AbortSignal` instances. While it is still possible to use `emitter.setMaxListeners(n)` to set a warning limit for individual `AbortSignal` instances, per default `AbortSignal` instances will not warn.`import { EventEmitter } from 'node:events'; const emitter = new EventEmitter(); emitter.setMaxListeners(emitter.getMaxListeners() + 1); emitter.once('event', () => { // do stuff emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0)); });``const EventEmitter = require('node:events'); const emitter = new EventEmitter(); emitter.setMaxListeners(emitter.getMaxListeners() + 1); emitter.once('event', () => { // do stuff emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0)); });`

The `--trace-warnings` command-line flag can be used to display the stack trace for such warnings.

The emitted warning can be inspected with `process.on('warning')` and will have the additional `emitter`, `type`, and `count` properties, referring to the event emitter instance, the event's name and the number of attached listeners, respectively. Its `name` property is set to `'MaxListenersExceededWarning'`.

### `events.errorMonitor`

This symbol shall be used to install a listener for only monitoring `'error'` events. Listeners installed using this symbol are called before the regular `'error'` listeners are called.

Installing a listener using this symbol does not change the behavior once an `'error'` event is emitted. Therefore, the process will still crash if no regular `'error'` listener is installed.

### `events.getEventListeners(emitterOrTarget, eventName)`

- `emitterOrTarget` `<EventEmitter>` | `<EventTarget>`
- `eventName` `<string>` | `<symbol>`
- Returns: `<Function>`[]

Returns a copy of the array of listeners for the event named `eventName`.

For `EventEmitter`s this behaves exactly the same as calling `.listeners` on the emitter.

For `EventTarget`s this is the only way to get the event listeners for the event target. This is useful for debugging and diagnostic purposes.`import { getEventListeners, EventEmitter } from 'node:events'; { const ee = new EventEmitter(); const listener = () => console.log('Events are fun'); ee.on('foo', listener); console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ] } { const et = new EventTarget(); const listener = () => console.log('Events are fun'); et.addEventListener('foo', listener); console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ] }``const { getEventListeners, EventEmitter } = require('node:events'); { const ee = new EventEmitter(); const listener = () => console.log('Events are fun'); ee.on('foo', listener); console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ] } { const et = new EventTarget(); const listener = () => console.log('Events are fun'); et.addEventListener('foo', listener); console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ] }`

### `events.getMaxListeners(emitterOrTarget)`

- `emitterOrTarget` `<EventEmitter>` | `<EventTarget>`
- Returns: `<number>`

Returns the currently set max amount of listeners.

For `EventEmitter`s this behaves exactly the same as calling `.getMaxListeners` on the emitter.

For `EventTarget`s this is the only way to get the max event listeners for the event target. If the number of event handlers on a single EventTarget exceeds the max set, the EventTarget will print a warning.`import { getMaxListeners, setMaxListeners, EventEmitter } from 'node:events'; { const ee = new EventEmitter(); console.log(getMaxListeners(ee)); // 10 setMaxListeners(11, ee); console.log(getMaxListeners(ee)); // 11 } { const et = new EventTarget(); console.log(getMaxListeners(et)); // 10 setMaxListeners(11, et); console.log(getMaxListeners(et)); // 11 }``const { getMaxListeners, setMaxListeners, EventEmitter } = require('node:events'); { const ee = new EventEmitter(); console.log(getMaxListeners(ee)); // 10 setMaxListeners(11, ee); console.log(getMaxListeners(ee)); // 11 } { const et = new EventTarget(); console.log(getMaxListeners(et)); // 10 setMaxListeners(11, et); console.log(getMaxListeners(et)); // 11 }`

### `events.once(emitter, name[, options])`

- `emitter` `<EventEmitter>`
- `name` `<string>` | `<symbol>`
- `options` `<Object>`
  - `signal` `<AbortSignal>` Can be used to cancel waiting for the event.
- Returns: `<Promise>`

Creates a `Promise` that is fulfilled when the `EventEmitter` emits the given event or that is rejected if the `EventEmitter` emits `'error'` while waiting. The `Promise` will resolve with an array of all the arguments emitted to the given event.

This method is intentionally generic and works with the web platform EventTarget interface, which has no special `'error'` event semantics and does not listen to the `'error'` event.`import { once, EventEmitter } from 'node:events'; import process from 'node:process'; const ee = new EventEmitter(); process.nextTick(() => { ee.emit('myevent', 42); }); const [value] = await once(ee, 'myevent'); console.log(value); const err = new Error('kaboom'); process.nextTick(() => { ee.emit('error', err); }); try { await once(ee, 'myevent'); } catch (err) { console.error('error happened', err); }``const { once, EventEmitter } = require('node:events'); async function run() { const ee = new EventEmitter(); process.nextTick(() => { ee.emit('myevent', 42); }); const [value] = await once(ee, 'myevent'); console.log(value); const err = new Error('kaboom'); process.nextTick(() => { ee.emit('error', err); }); try { await once(ee, 'myevent'); } catch (err) { console.error('error happened', err); } } run();`

The special handling of the `'error'` event is only used when `events.once()` is used to wait for another event. If `events.once()` is used to wait for the '`error'` event itself, then it is treated as any other kind of event without special handling:`import { EventEmitter, once } from 'node:events'; const ee = new EventEmitter(); once(ee, 'error') .then(([err]) => console.log('ok', err.message)) .catch((err) => console.error('error', err.message)); ee.emit('error', new Error('boom')); // Prints: ok boom``const { EventEmitter, once } = require('node:events'); const ee = new EventEmitter(); once(ee, 'error') .then(([err]) => console.log('ok', err.message)) .catch((err) => console.error('error', err.message)); ee.emit('error', new Error('boom')); // Prints: ok boom`

An `<AbortSignal>` can be used to cancel waiting for the event:`import { EventEmitter, once } from 'node:events'; const ee = new EventEmitter(); const ac = new AbortController(); async function foo(emitter, event, signal) { try { await once(emitter, event, { signal }); console.log('event emitted!'); } catch (error) { if (error.name === 'AbortError') { console.error('Waiting for the event was canceled!'); } else { console.error('There was an error', error.message); } } } foo(ee, 'foo', ac.signal); ac.abort(); // Prints: Waiting for the event was canceled!``const { EventEmitter, once } = require('node:events'); const ee = new EventEmitter(); const ac = new AbortController(); async function foo(emitter, event, signal) { try { await once(emitter, event, { signal }); console.log('event emitted!'); } catch (error) { if (error.name === 'AbortError') { console.error('Waiting for the event was canceled!'); } else { console.error('There was an error', error.message); } } } foo(ee, 'foo', ac.signal); ac.abort(); // Prints: Waiting for the event was canceled!`

#### Caveats when awaiting multiple events

It is important to be aware of execution order when using the `events.once()` method to await multiple events.

Conventional event listeners are called synchronously when the event is emitted. This guarantees that execution will not proceed beyond the emitted event until all listeners have finished executing.

The same is *not* true when awaiting Promises returned by `events.once()`. Promise tasks are not handled until after the current execution stack runs to completion, which means that multiple events could be emitted before asynchronous execution continues from the relevant `await` statement.

As a result, events can be "missed" if a series of `await events.once()` statements is used to listen to multiple events, since there might be times where more than one event is emitted during the same phase of the event loop. (The same is true when using `process.nextTick()` to emit events, because the tasks queued by `process.nextTick()` are executed before Promise tasks.)`import { EventEmitter, once } from 'node:events'; import process from 'node:process'; const myEE = new EventEmitter(); async function listen() { await once(myEE, 'foo'); console.log('foo'); // This Promise will never resolve, because the 'bar' event will // have already been emitted before the next line is executed. await once(myEE, 'bar'); console.log('bar'); } process.nextTick(() => { myEE.emit('foo'); myEE.emit('bar'); }); listen().then(() => console.log('done'));``const { EventEmitter, once } = require('node:events'); const myEE = new EventEmitter(); async function listen() { await once(myEE, 'foo'); console.log('foo'); // This Promise will never resolve, because the 'bar' event will // have already been emitted before the next line is executed. await once(myEE, 'bar'); console.log('bar'); } process.nextTick(() => { myEE.emit('foo'); myEE.emit('bar'); }); listen().then(() => console.log('done'));`

To catch multiple events, create all of the Promises *before* awaiting any of them. This is usually made easier by using `Promise.all()`, `Promise.race()`, or `Promise.allSettled()`:`import { EventEmitter, once } from 'node:events'; import process from 'node:process'; const myEE = new EventEmitter(); async function listen() { await Promise.all([ once(myEE, 'foo'), once(myEE, 'bar'), ]); console.log('foo', 'bar'); } process.nextTick(() => { myEE.emit('foo'); myEE.emit('bar'); }); listen().then(() => console.log('done'));``const { EventEmitter, once } = require('node:events'); const myEE = new EventEmitter(); async function listen() { await Promise.all([ once(myEE, 'bar'), once(myEE, 'foo'), ]); console.log('foo', 'bar'); } process.nextTick(() => { myEE.emit('foo'); myEE.emit('bar'); }); listen().then(() => console.log('done'));`

### `events.captureRejections`

- Type: `<boolean>`

Change the default `captureRejections` option on all new `EventEmitter` objects.

### `events.captureRejectionSymbol`

- Type: `<symbol>` `Symbol.for('nodejs.rejection')`

See how to write a custom rejection handler.

### `events.listenerCount(emitterOrTarget, eventName)`

- `emitterOrTarget` `<EventEmitter>` | `<EventTarget>`
- `eventName` `<string>` | `<symbol>`
- Returns: `<integer>`

Returns the number of registered listeners for the event named `eventName`.

For `EventEmitter`s this behaves exactly the same as calling `.listenerCount` on the emitter.

For `EventTarget`s this is the only way to obtain the listener count. This can be useful for debugging and diagnostic purposes.`import { EventEmitter, listenerCount } from 'node:events'; { const ee = new EventEmitter(); ee.on('event', () => {}); ee.on('event', () => {}); console.log(listenerCount(ee, 'event')); // 2 } { const et = new EventTarget(); et.addEventListener('event', () => {}); et.addEventListener('event', () => {}); console.log(listenerCount(et, 'event')); // 2 }``const { EventEmitter, listenerCount } = require('node:events'); { const ee = new EventEmitter(); ee.on('event', () => {}); ee.on('event', () => {}); console.log(listenerCount(ee, 'event')); // 2 } { const et = new EventTarget(); et.addEventListener('event', () => {}); et.addEventListener('event', () => {}); console.log(listenerCount(et, 'event')); // 2 }`

### `events.on(emitter, eventName[, options])`

- `emitter` `<EventEmitter>`
- `eventName` `<string>` | `<symbol>` The name of the event being listened for
- `options` `<Object>`
  - `signal` `<AbortSignal>` Can be used to cancel awaiting events.
  - `close` `<string>`[] Names of events that will end the iteration.
  - `highWaterMark` `<integer>` **Default:** `Number.MAX_SAFE_INTEGER` The high watermark. The emitter is paused every time the size of events being buffered is higher than it. Supported only on emitters implementing `pause()` and `resume()` methods.
  - `lowWaterMark` `<integer>` **Default:** `1` The low watermark. The emitter is resumed every time the size of events being buffered is lower than it. Supported only on emitters implementing `pause()` and `resume()` methods.
- Returns: `<AsyncIterator>` that iterates `eventName` events emitted by the `emitter`

```mjs
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
});

for await (const event of on(ee, 'foo')) {
  // The execution of this inner block is synchronous and it
  // processes one event at a time (even with await). Do not use
  // if concurrent execution is required.
  console.log(event); // prints ['bar'] [42]
}
// Unreachable here
const { on, EventEmitter } = require('node:events');

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo')) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();
```

Returns an `AsyncIterator` that iterates `eventName` events. It will throw if the `EventEmitter` emits `'error'`. It removes all listeners when exiting the loop. The `value` returned by each iteration is an array composed of the emitted event arguments.

An `<AbortSignal>` can be used to cancel waiting on events:`import { on, EventEmitter } from 'node:events'; import process from 'node:process'; const ac = new AbortController(); (async () => { const ee = new EventEmitter(); // Emit later on process.nextTick(() => { ee.emit('foo', 'bar'); ee.emit('foo', 42); }); for await (const event of on(ee, 'foo', { signal: ac.signal })) { // The execution of this inner block is synchronous and it // processes one event at a time (even with await). Do not use // if concurrent execution is required. console.log(event); // prints ['bar'] [42] } // Unreachable here })(); process.nextTick(() => ac.abort());``const { on, EventEmitter } = require('node:events'); const ac = new AbortController(); (async () => { const ee = new EventEmitter(); // Emit later on process.nextTick(() => { ee.emit('foo', 'bar'); ee.emit('foo', 42); }); for await (const event of on(ee, 'foo', { signal: ac.signal })) { // The execution of this inner block is synchronous and it // processes one event at a time (even with await). Do not use // if concurrent execution is required. console.log(event); // prints ['bar'] [42] } // Unreachable here })(); process.nextTick(() => ac.abort());`
