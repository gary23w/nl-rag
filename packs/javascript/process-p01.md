---
title: "Process (part 1/3)"
source: https://nodejs.org/api/process.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 1/3
---

# Process

Node.js

# Node.js v26.4.0 documentation

- Node.js v26.4.0
- Table of contents
- IndexIndex
- Other versions26.x 25.x 24.x **LTS**23.x 22.x **LTS**21.x 20.x 19.x 18.x 17.x 16.x 15.x 14.x 13.x 12.x 11.x 10.x 9.x 8.x 7.x 6.x 5.x 4.x 0.12.x 0.10.x
- Options View on single page View as JSON

## Process

The `process` object provides information about, and control over, the current Node.js process.`import process from 'node:process';``const process = require('node:process');`

### Process events

The `process` object is an instance of `EventEmitter`.

#### Event: `'beforeExit'`

The `'beforeExit'` event is emitted when Node.js empties its event loop and has no additional work to schedule. Normally, the Node.js process will exit when there is no work scheduled, but a listener registered on the `'beforeExit'` event can make asynchronous calls, and thereby cause the Node.js process to continue.The listener callback function is invoked with the value of `process.exitCode` passed as the only argument.The `'beforeExit'` event is *not* emitted for conditions causing explicit termination, such as calling `process.exit()` or uncaught exceptions.The `'beforeExit'` should *not* be used as an alternative to the `'exit'` event unless the intention is to schedule additional work.`import process from 'node:process'; process.on('beforeExit', (code) => { console.log('Process beforeExit event with code: ', code); }); process.on('exit', (code) => { console.log('Process exit event with code: ', code); }); console.log('This message is displayed first.'); // Prints: // This message is displayed first. // Process beforeExit event with code: 0 // Process exit event with code: 0``process.on('beforeExit', (code) => { console.log('Process beforeExit event with code: ', code); }); process.on('exit', (code) => { console.log('Process exit event with code: ', code); }); console.log('This message is displayed first.'); // Prints: // This message is displayed first. // Process beforeExit event with code: 0 // Process exit event with code: 0`

#### Event: `'disconnect'`

If the Node.js process is spawned with an IPC channel (see the Child Process and Cluster documentation), the `'disconnect'` event will be emitted when the IPC channel is closed.

#### Event: `'exit'`

- `code` `<integer>`

The `'exit'` event is emitted when the Node.js process is about to exit as a result of either: The `process.exit()` method being called explicitly; The Node.js event loop no longer having any additional work to perform. There is no way to prevent the exiting of the event loop at this point, and once all `'exit'` listeners have finished running the Node.js process will terminate.The listener callback function is invoked with the exit code specified either by the `process.exitCode` property, or the `exitCode` argument passed to the `process.exit()` method.import process from 'node:process'; process.on('exit', (code) => { console.log(`About to exit with code: ${code}`); });process.on('exit', (code) => { console.log(`About to exit with code: ${code}`); });Listener functions **must** only perform **synchronous** operations. The Node.js process will exit immediately after calling the `'exit'` event listeners causing any additional work still queued in the event loop to be abandoned. In the following example, for instance, the timeout will never occur:`import process from 'node:process'; process.on('exit', (code) => { setTimeout(() => { console.log('This will not run'); }, 0); });``process.on('exit', (code) => { setTimeout(() => { console.log('This will not run'); }, 0); });`

#### Event: `'message'`

- `message` `<Object>` | `<boolean>` | `<number>` | `<string>` | `<null>` a parsed JSON object or a serializable primitive value.
- `sendHandle` `<net.Server>` | `<net.Socket>` a `net.Server` or `net.Socket` object, or undefined.

If the Node.js process is spawned with an IPC channel (see the Child Process and Cluster documentation), the `'message'` event is emitted whenever a message sent by a parent process using `childprocess.send()` is received by the child process.The message goes through serialization and parsing. The resulting message might not be the same as what is originally sent.If the `serialization` option was set to `advanced` used when spawning the process, the `message` argument can contain data that JSON is not able to represent. See Advanced serialization for `child_process` for more details.

#### Event: `'rejectionHandled'`

- `promise` `<Promise>` The late handled promise.

The `'rejectionHandled'` event is emitted whenever a `Promise` has been rejected and an error handler was attached to it (using `promise.catch()`, for example) later than one turn of the Node.js event loop.The `Promise` object would have previously been emitted in an `'unhandledRejection'` event, but during the course of processing gained a rejection handler.There is no notion of a top level for a `Promise` chain at which rejections can always be handled. Being inherently asynchronous in nature, a `Promise` rejection can be handled at a future point in time, possibly much later than the event loop turn it takes for the `'unhandledRejection'` event to be emitted.Another way of stating this is that, unlike in synchronous code where there is an ever-growing list of unhandled exceptions, with Promises there can be a growing-and-shrinking list of unhandled rejections.In synchronous code, the `'uncaughtException'` event is emitted when the list of unhandled exceptions grows.In asynchronous code, the `'unhandledRejection'` event is emitted when the list of unhandled rejections grows, and the `'rejectionHandled'` event is emitted when the list of unhandled rejections shrinks.`import process from 'node:process'; const unhandledRejections = new Map(); process.on('unhandledRejection', (reason, promise) => { unhandledRejections.set(promise, reason); }); process.on('rejectionHandled', (promise) => { unhandledRejections.delete(promise); });``const unhandledRejections = new Map(); process.on('unhandledRejection', (reason, promise) => { unhandledRejections.set(promise, reason); }); process.on('rejectionHandled', (promise) => { unhandledRejections.delete(promise); });`In this example, the `unhandledRejections` `Map` will grow and shrink over time, reflecting rejections that start unhandled and then become handled. It is possible to record such errors in an error log, either periodically (which is likely best for long-running application) or upon process exit (which is likely most convenient for scripts).

#### Event: `'workerMessage'`

- `value` `<any>` A value transmitted using `postMessageToThread()`.
- `source` `<number>` The transmitting worker thread ID or `0` for the main thread.

The `'workerMessage'` event is emitted for any incoming message send by the other party by using `postMessageToThread()`.

#### Event: `'uncaughtException'`

- `err` `<Error>` The uncaught exception.
- `origin` `<string>` Indicates if the exception originates from an unhandled rejection or from a synchronous error. Can either be `'uncaughtException'` or `'unhandledRejection'`. The latter is used when an exception happens in a `Promise` based async context (or if a `Promise` is rejected) and `--unhandled-rejections` flag set to `strict` or `throw` (which is the default) and the rejection is not handled, or when a rejection happens during the command line entry point's ES module static loading phase.

The `'uncaughtException'` event is emitted when an uncaught JavaScript exception bubbles all the way back to the event loop. By default, Node.js handles such exceptions by printing the stack trace to `stderr` and exiting with code 1, overriding any previously set `process.exitCode`. Adding a handler for the `'uncaughtException'` event overrides this default behavior. Alternatively, change the `process.exitCode` in the `'uncaughtException'` handler which will result in the process exiting with the provided exit code. Otherwise, in the presence of such handler the process will exit with 0.import process from 'node:process'; import fs from 'node:fs'; process.on('uncaughtException', (err, origin) => { fs.writeSync( process.stderr.fd, `Caught exception: ${err}\n` + `Exception origin: ${origin}\n`, ); }); setTimeout(() => { console.log('This will still run.'); }, 500); // Intentionally cause an exception, but don't catch it. nonexistentFunc(); console.log('This will not run.');const fs = require('node:fs'); process.on('uncaughtException', (err, origin) => { fs.writeSync( process.stderr.fd, `Caught exception: ${err}\n` + `Exception origin: ${origin}\n`, ); }); setTimeout(() => { console.log('This will still run.'); }, 500); // Intentionally cause an exception, but don't catch it. nonexistentFunc(); console.log('This will not run.');It is possible to monitor `'uncaughtException'` events without overriding the default behavior to exit the process by installing a `'uncaughtExceptionMonitor'` listener.

##### Warning: Using `'uncaughtException'` correctly

`'uncaughtException'` is a crude mechanism for exception handling intended to be used only as a last resort. The event *should not* be used as an equivalent to `On Error Resume Next`. Unhandled exceptions inherently mean that an application is in an undefined state. Attempting to resume application code without properly recovering from the exception can cause additional unforeseen and unpredictable issues.Exceptions thrown from within the event handler will not be caught. Instead the process will exit with a non-zero exit code and the stack trace will be printed. This is to avoid infinite recursion.Attempting to resume normally after an uncaught exception can be similar to pulling out the power cord when upgrading a computer. Nine out of ten times, nothing happens. But the tenth time, the system becomes corrupted.The correct use of `'uncaughtException'` is to perform synchronous cleanup of allocated resources (e.g. file descriptors, handles, etc) before shutting down the process. **It is not safe to resume normal operation after `'uncaughtException'`.**To restart a crashed application in a more reliable way, whether `'uncaughtException'` is emitted or not, an external monitor should be employed in a separate process to detect application failures and recover or restart as needed.

#### Event: `'uncaughtExceptionMonitor'`

- `err` `<Error>` The uncaught exception.
- `origin` `<string>` Indicates if the exception originates from an unhandled rejection or from synchronous errors. Can either be `'uncaughtException'` or `'unhandledRejection'`. The latter is used when an exception happens in a `Promise` based async context (or if a `Promise` is rejected) and `--unhandled-rejections` flag set to `strict` or `throw` (which is the default) and the rejection is not handled, or when a rejection happens during the command line entry point's ES module static loading phase.

The `'uncaughtExceptionMonitor'` event is emitted before an `'uncaughtException'` event is emitted or a hook installed via `process.setUncaughtExceptionCaptureCallback()` is called.Installing an `'uncaughtExceptionMonitor'` listener does not change the behavior once an `'uncaughtException'` event is emitted. The process will still crash if no `'uncaughtException'` listener is installed.`import process from 'node:process'; process.on('uncaughtExceptionMonitor', (err, origin) => { MyMonitoringTool.logSync(err, origin); }); // Intentionally cause an exception, but don't catch it. nonexistentFunc(); // Still crashes Node.js``process.on('uncaughtExceptionMonitor', (err, origin) => { MyMonitoringTool.logSync(err, origin); }); // Intentionally cause an exception, but don't catch it. nonexistentFunc(); // Still crashes Node.js`

#### Event: `'unhandledRejection'`

- `reason` `<Error>` | `<any>` The object with which the promise was rejected (typically an `Error` object).
- `promise` `<Promise>` The rejected promise.

The `'unhandledRejection'` event is emitted whenever a `Promise` is rejected and no error handler is attached to the promise within a turn of the event loop. When programming with Promises, exceptions are encapsulated as "rejected promises". Rejections can be caught and handled using `promise.catch()` and are propagated through a `Promise` chain. The `'unhandledRejection'` event is useful for detecting and keeping track of promises that were rejected whose rejections have not yet been handled.import process from 'node:process'; process.on('unhandledRejection', (reason, promise) => { console.log('Unhandled Rejection at:', promise, 'reason:', reason); // Application specific logging, throwing an error, or other logic here }); somePromise.then((res) => { return reportToUser(JSON.pasre(res)); // Note the typo (`pasre`) }); // No `.catch()` or `.then()`process.on('unhandledRejection', (reason, promise) => { console.log('Unhandled Rejection at:', promise, 'reason:', reason); // Application specific logging, throwing an error, or other logic here }); somePromise.then((res) => { return reportToUser(JSON.pasre(res)); // Note the typo (`pasre`) }); // No `.catch()` or `.then()`The following will also trigger the `'unhandledRejection'` event to be emitted:`import process from 'node:process'; function SomeResource() { // Initially set the loaded status to a rejected promise this.loaded = Promise.reject(new Error('Resource not yet loaded!')); } const resource = new SomeResource(); // no .catch or .then on resource.loaded for at least a turn``function SomeResource() { // Initially set the loaded status to a rejected promise this.loaded = Promise.reject(new Error('Resource not yet loaded!')); } const resource = new SomeResource(); // no .catch or .then on resource.loaded for at least a turn`In this example case, it is possible to track the rejection as a developer error as would typically be the case for other `'unhandledRejection'` events. To address such failures, a non-operational `.catch(() => { })` handler may be attached to `resource.loaded`, which would prevent the `'unhandledRejection'` event from being emitted.If an `'unhandledRejection'` event is emitted but not handled it will be raised as an uncaught exception. This alongside other behaviors of `'unhandledRejection'` events can changed via the `--unhandled-rejections` flag.

#### Event: `'warning'`

- `warning` `<Error>` Key properties of the warning are:
  - `name` `<string>` The name of the warning. **Default:** `'Warning'`.
  - `message` `<string>` A system-provided description of the warning.
  - `stack` `<string>` A stack trace to the location in the code where the warning was issued.

The `'warning'` event is emitted whenever Node.js emits a process warning.A process warning is similar to an error in that it describes exceptional conditions that are being brought to the user's attention. However, warnings are not part of the normal Node.js and JavaScript error handling flow. Node.js can emit warnings whenever it detects bad coding practices that could lead to sub-optimal application performance, bugs, or security vulnerabilities.`import process from 'node:process'; process.on('warning', (warning) => { console.warn(warning.name); // Print the warning name console.warn(warning.message); // Print the warning message console.warn(warning.stack); // Print the stack trace });``process.on('warning', (warning) => { console.warn(warning.name); // Print the warning name console.warn(warning.message); // Print the warning message console.warn(warning.stack); // Print the stack trace });`By default, Node.js will print process warnings to `stderr`. The `--no-warnings` command-line option can be used to suppress the default console output but the `'warning'` event will still be emitted by the `process` object. Currently, it is not possible to suppress specific warning types other than deprecation warnings. To suppress deprecation warnings, check out the `--no-deprecation` flag.The following example illustrates the warning that is printed to `stderr` when too many listeners have been added to an event:`$ node > events.defaultMaxListeners = 1; > process.on('foo', () => {}); > process.on('foo', () => {}); > (node:38638) MaxListenersExceededWarning: Possible EventEmitter memory leak detected. 2 foo listeners added. Use emitter.setMaxListeners() to increase limit`In contrast, the following example turns off the default warning output and adds a custom handler to the `'warning'` event:`$ node --no-warnings > const p = process.on('warning', (warning) => console.warn('Do not do that!')); > events.defaultMaxListeners = 1; > process.on('foo', () => {}); > process.on('foo', () => {}); > Do not do that!`The `--trace-warnings` command-line option can be used to have the default console output for warnings include the full stack trace of the warning.Launching Node.js using the `--throw-deprecation` command-line flag will cause custom deprecation warnings to be thrown as exceptions.Using the `--trace-deprecation` command-line flag will cause the custom deprecation to be printed to `stderr` along with the stack trace.Using the `--no-deprecation` command-line flag will suppress all reporting of the custom deprecation.The `*-deprecation` command-line flags only affect warnings that use the name `'DeprecationWarning'`.

##### Emitting custom warnings

See the `process.emitWarning()` method for issuing custom or application-specific warnings.

##### Node.js warning names

There are no strict guidelines for warning types (as identified by the `name` property) emitted by Node.js. New types of warnings can be added at any time. A few of the warning types that are most common include: `'DeprecationWarning'` - Indicates use of a deprecated Node.js API or feature. Such warnings must include a `'code'` property identifying the deprecation code. `'ExperimentalWarning'` - Indicates use of an experimental Node.js API or feature. Such features must be used with caution as they may change at any time and are not subject to the same strict semantic-versioning and long-term support policies as supported features. `'MaxListenersExceededWarning'` - Indicates that too many listeners for a given event have been registered on either an `EventEmitter` or `EventTarget`. This is often an indication of a memory leak. `'TimeoutOverflowWarning'` - Indicates that a numeric value that cannot fit within a 32-bit signed integer has been provided to either the `setTimeout()` or `setInterval()` functions. `'TimeoutNegativeWarning'` - Indicates that a negative number has provided to either the `setTimeout()` or `setInterval()` functions. `'TimeoutNaNWarning'` - Indicates that a value which is not a number has provided to either the `setTimeout()` or `setInterval()` functions. `'UnsupportedWarning'` - Indicates use of an unsupported option or feature that will be ignored rather than treated as an error. One example is use of the HTTP response status message when using the HTTP/2 compatibility API.

#### Event: `'worker'`

- `worker` `<Worker>` The `<Worker>` that was created.

The `'worker'` event is emitted after a new `<Worker>` thread has been created.

#### Signal events

Signal events will be emitted when the Node.js process receives a signal. Please refer to `signal(7)` for a listing of standard POSIX signal names such as `'SIGINT'`, `'SIGHUP'`, etc.Signals are not available on `Worker` threads.The signal handler will receive the signal's name (`'SIGINT'`, `'SIGTERM'`, etc.) as the first argument.The name of each event will be the uppercase common name for the signal (e.g. `'SIGINT'` for `SIGINT` signals).import process from 'node:process'; // Begin reading from stdin so the process does not exit. process.stdin.resume(); process.on('SIGINT', () => { console.log('Received SIGINT. Press Control-D to exit.'); }); // Using a single function to handle multiple signals function handle(signal) { console.log(`Received ${signal}`); } process.on('SIGINT', handle); process.on('SIGTERM', handle);// Begin reading from stdin so the process does not exit. process.stdin.resume(); process.on('SIGINT', () => { console.log('Received SIGINT. Press Control-D to exit.'); }); // Using a single function to handle multiple signals function handle(signal) { console.log(`Received ${signal}`); } process.on('SIGINT', handle); process.on('SIGTERM', handle); `'SIGUSR1'` is reserved by Node.js to start the debugger. It's possible to install a listener but doing so might interfere with the debugger. `'SIGTERM'` and `'SIGINT'` have default handlers on non-Windows platforms that reset the terminal mode before exiting with code `128 + signal number`. If one of these signals has a listener installed, its default behavior will be removed (Node.js will no longer exit). `'SIGPIPE'` is ignored by default. It can have a listener installed. `'SIGHUP'` is generated on Windows when the console window is closed, and on other platforms under various similar conditions. See `signal(7)`. It can have a listener installed, however Node.js will be unconditionally terminated by Windows about 10 seconds later. On non-Windows platforms, the default behavior of `SIGHUP` is to terminate Node.js, but once a listener has been installed its default behavior will be removed. `'SIGTERM'` is not supported on Windows, it can be listened on. `'SIGINT'` from the terminal is supported on all platforms, and can usually be generated with Ctrl+C (though this may be configurable). It is not generated when terminal raw mode is enabled and Ctrl+C is used. `'SIGBREAK'` is delivered on Windows when Ctrl+Break is pressed. On non-Windows platforms, it can be listened on, but there is no way to send or generate it. `'SIGWINCH'` is delivered when the console has been resized. On Windows, this will only happen on write to the console when the cursor is being moved, or when a readable tty is used in raw mode. `'SIGKILL'` cannot have a listener installed, it will unconditionally terminate Node.js on all platforms. `'SIGSTOP'` cannot have a listener installed. `'SIGBUS'`, `'SIGFPE'`, `'SIGSEGV'`, and `'SIGILL'`, when not raised artificially using `kill(2)`, inherently leave the process in a state from which it is not safe to call JS listeners. Doing so might cause the process to stop responding. `0` can be sent to test for the existence of a process, it has no effect if the process exists, but will throw an error if the process does not exist. Windows does not support signals so has no equivalent to termination by signal, but Node.js offers some emulation with `process.kill()`, and `subprocess.kill()`: Sending `SIGINT`, `SIGTERM`, and `SIGKILL` will cause the unconditional termination of the target process, and afterwards, subprocess will report that the process was terminated by signal. Sending signal `0` can be used as a platform independent way to test for the existence of a process.

### `process.abort()`

The `process.abort()` method causes the Node.js process to exit immediately and generate a core file.This feature is not available in `Worker` threads.

### `process.addUncaughtExceptionCaptureCallback(fn)`

Stability: 1 - Experimental

- `fn` `<Function>`

The `process.addUncaughtExceptionCaptureCallback()` function adds a callback that will be invoked when an uncaught exception occurs, receiving the exception value as its first argument.Unlike `process.setUncaughtExceptionCaptureCallback()`, this function allows multiple callbacks to be registered and does not conflict with the `domain` module. Callbacks are called in reverse order of registration (most recent first). If a callback returns `true`, subsequent callbacks and the default uncaught exception handling are skipped.`import process from 'node:process'; process.addUncaughtExceptionCaptureCallback((err) => { console.error('Caught exception:', err.message); return true; // Indicates exception was handled });``process.addUncaughtExceptionCaptureCallback((err) => { console.error('Caught exception:', err.message); return true; // Indicates exception was handled });`

### `process.allowedNodeEnvironmentFlags`

- Type: `<Set>`

The `process.allowedNodeEnvironmentFlags` property is a special, read-only `Set` of flags allowable within the `NODE_OPTIONS` environment variable.`process.allowedNodeEnvironmentFlags` extends `Set`, but overrides `Set.prototype.has` to recognize several different possible flag representations. `process.allowedNodeEnvironmentFlags.has()` will return `true` in the following cases: Flags may omit leading single (`-`) or double (`--`) dashes; e.g., `inspect-brk` for `--inspect-brk`, or `r` for `-r`. Flags passed through to V8 (as listed in `--v8-options`) may replace one or more *non-leading* dashes for an underscore, or vice-versa; e.g., `--perf_basic_prof`, `--perf-basic-prof`, `--perf_basic-prof`, etc. Flags may contain one or more equals (`=`) characters; all characters after and including the first equals will be ignored; e.g., `--stack-trace-limit=100`. Flags *must* be allowable within `NODE_OPTIONS`. When iterating over `process.allowedNodeEnvironmentFlags`, flags will appear only *once*; each will begin with one or more dashes. Flags passed through to V8 will contain underscores instead of non-leading dashes:`import { allowedNodeEnvironmentFlags } from 'node:process'; allowedNodeEnvironmentFlags.forEach((flag) => { // -r // --inspect-brk // --abort_on_uncaught_exception // ... });``const { allowedNodeEnvironmentFlags } = require('node:process'); allowedNodeEnvironmentFlags.forEach((flag) => { // -r // --inspect-brk // --abort_on_uncaught_exception // ... });`The methods `add()`, `clear()`, and `delete()` of `process.allowedNodeEnvironmentFlags` do nothing, and will fail silently.If Node.js was compiled *without* `NODE_OPTIONS` support (shown in `process.config`), `process.allowedNodeEnvironmentFlags` will contain what *would have* been allowable.

### `process.arch`

- Type: `<string>`

The operating system CPU architecture for which the Node.js binary was compiled. Possible values are: `'arm'`, `'arm64'`, `'ia32'`, `'loong64'`, `'mips'`, `'mipsel'`, `'ppc64'`, `'riscv64'`, `'s390'`, `'s390x'`, and `'x64'`.import { arch } from 'node:process'; console.log(`This processor architecture is ${arch}`);const { arch } = require('node:process'); console.log(`This processor architecture is ${arch}`);

### `process.argv`

- Type: `<string>`[]

The `process.argv` property returns an array containing the command-line arguments passed when the Node.js process was launched. The first element will be `process.execPath`. See `process.argv0` if access to the original value of `argv[0]` is needed. If a program entry point was provided, the second element will be the absolute path to it. The remaining elements are additional command-line arguments.For example, assuming the following script for `process-args.js`:import { argv } from 'node:process'; // print process.argv argv.forEach((val, index) => { console.log(`${index}: ${val}`); });const { argv } = require('node:process'); // print process.argv argv.forEach((val, index) => { console.log(`${index}: ${val}`); });Launching the Node.js process as:`node process-args.js one two=three four`Would generate the output:`0: /usr/local/bin/node 1: /Users/mjr/work/node/process-args.js 2: one 3: two=three 4: four`

### `process.argv0`

- Type: `<string>`

The `process.argv0` property stores a read-only copy of the original value of `argv[0]` passed when Node.js starts.`$ bash -c 'exec -a customArgv0 ./node' > process.argv[0] '/Volumes/code/external/node/out/Release/node' > process.argv0 'customArgv0'`

### `process.availableMemory()`

- Returns: `<number>`

Gets the amount of free memory that is still available to the process (in bytes).See `uv_get_available_memory` for more information.

### `process.channel`

- Type: `<Object>`

If the Node.js process was spawned with an IPC channel (see the Child Process documentation), the `process.channel` property is a reference to the IPC channel. If no IPC channel exists, this property is `undefined`.

#### `process.channel.ref()`

This method makes the IPC channel keep the event loop of the process running if `.unref()` has been called before.Typically, this is managed through the number of `'disconnect'` and `'message'` listeners on the `process` object. However, this method can be used to explicitly request a specific behavior.

#### `process.channel.unref()`

This method makes the IPC channel not keep the event loop of the process running, and lets it finish even while the channel is open.Typically, this is managed through the number of `'disconnect'` and `'message'` listeners on the `process` object. However, this method can be used to explicitly request a specific behavior.

### `process.chdir(directory)`

- `directory` `<string>`

The `process.chdir()` method changes the current working directory of the Node.js process or throws an exception if doing so fails (for instance, if the specified `directory` does not exist).import { chdir, cwd } from 'node:process'; console.log(`Starting directory: ${cwd()}`); try { chdir('/tmp'); console.log(`New directory: ${cwd()}`); } catch (err) { console.error(`chdir: ${err}`); }const { chdir, cwd } = require('node:process'); console.log(`Starting directory: ${cwd()}`); try { chdir('/tmp'); console.log(`New directory: ${cwd()}`); } catch (err) { console.error(`chdir: ${err}`); }This feature is not available in `Worker` threads.

### `process.config`

- Type: `<Object>`

The `process.config` property returns a frozen `Object` containing the JavaScript representation of the configure options used to compile the current Node.js executable. This is the same as the `config.gypi` file that was produced when running the `./configure` script.An example of the possible output looks like:`{ "target_defaults": { "cflags": [], "default_configuration": "Release", "defines": [], "include_dirs": [], "libraries": [] }, "variables": { "host_arch": "x64", "napi_build_version": 5, "node_install_npm": "true", "node_prefix": "", "node_shared_cares": "false", "node_shared_http_parser": "false", "node_shared_libuv": "false", "node_shared_zlib": "false", "node_use_openssl": "true", "node_shared_openssl": "false", "target_arch": "x64", "v8_use_snapshot": 1 } }`

### `process.connected`

- Type: `<boolean>`

If the Node.js process is spawned with an IPC channel (see the Child Process and Cluster documentation), the `process.connected` property will return `true` so long as the IPC channel is connected and will return `false` after `process.disconnect()` is called.Once `process.connected` is `false`, it is no longer possible to send messages over the IPC channel using `process.send()`.

### `process.constrainedMemory()`

- Returns: `<number>`

Gets the amount of memory available to the process (in bytes) based on limits imposed by the OS. If there is no such constraint, or the constraint is unknown, `0` is returned.See `uv_get_constrained_memory` for more information.

### `process.cpuUsage([previousValue])`

- `previousValue` `<Object>` A previous return value from calling `process.cpuUsage()`
- Returns: `<Object>`
  - `user` `<integer>`
  - `system` `<integer>`

The `process.cpuUsage()` method returns the user and system CPU time usage of the current process, in an object with properties `user` and `system`, whose values are microsecond values (millionth of a second). These values measure time spent in user and system code respectively, and may end up being greater than actual elapsed time if multiple CPU cores are performing work for this process.The result of a previous call to `process.cpuUsage()` can be passed as the argument to the function, to get a diff reading.`import { cpuUsage } from 'node:process'; const startUsage = cpuUsage(); // { user: 38579, system: 6986 } // spin the CPU for 500 milliseconds const now = Date.now(); while (Date.now() - now < 500); console.log(cpuUsage(startUsage)); // { user: 514883, system: 11226 }``const { cpuUsage } = require('node:process'); const startUsage = cpuUsage(); // { user: 38579, system: 6986 } // spin the CPU for 500 milliseconds const now = Date.now(); while (Date.now() - now < 500); console.log(cpuUsage(startUsage)); // { user: 514883, system: 11226 }`

### `process.cwd()`

- Returns: `<string>`

The `process.cwd()` method returns the current working directory of the Node.js process.import { cwd } from 'node:process'; console.log(`Current directory: ${cwd()}`);const { cwd } = require('node:process'); console.log(`Current directory: ${cwd()}`);

### `process.debugPort`

- Type: `<number>`

The port used by the Node.js debugger when enabled.`import process from 'node:process'; process.debugPort = 5858;``process.debugPort = 5858;`

### `process.disconnect()`

If the Node.js process is spawned with an IPC channel (see the Child Process and Cluster documentation), the `process.disconnect()` method will close the IPC channel to the parent process, allowing the child process to exit gracefully once there are no other connections keeping it alive.The effect of calling `process.disconnect()` is the same as calling `ChildProcess.disconnect()` from the parent process.If the Node.js process was not spawned with an IPC channel, `process.disconnect()` will be `undefined`.

### `process.dlopen(module, filename[, flags])`

- `module` `<Object>`
- `filename` `<string>`
- `flags` `<os.constants.dlopen>` **Default:** `os.constants.dlopen.RTLD_LAZY`

The `process.dlopen()` method allows dynamically loading shared objects. It is primarily used by `require()` to load C++ Addons, and should not be used directly, except in special cases. In other words, `require()` should be preferred over `process.dlopen()` unless there are specific reasons such as custom dlopen flags or loading from ES modules.The `flags` argument is an integer that allows to specify dlopen behavior. See the `os.constants.dlopen` documentation for details.An important requirement when calling `process.dlopen()` is that the `module` instance must be passed. Functions exported by the C++ Addon are then accessible via `module.exports`.The example below shows how to load a C++ Addon, named `local.node`, that exports a `foo` function. All the symbols are loaded before the call returns, by passing the `RTLD_NOW` constant. In this example the constant is assumed to be available.`import { dlopen } from 'node:process'; import { constants } from 'node:os'; import { fileURLToPath } from 'node:url'; const module = { exports: {} }; dlopen(module, fileURLToPath(new URL('local.node', import.meta.url)), constants.dlopen.RTLD_NOW); module.exports.foo();``const { dlopen } = require('node:process'); const { constants } = require('node:os'); const { join } = require('node:path'); const module = { exports: {} }; dlopen(module, join(__dirname, 'local.node'), constants.dlopen.RTLD_NOW); module.exports.foo();`

### `process.emitWarning(warning[, options])`

- `warning` `<string>` | `<Error>` The warning to emit.
- `options` `<Object>`
  - `type` `<string>` When `warning` is a `String`, `type` is the name to use for the *type* of warning being emitted. **Default:** `'Warning'`.
  - `code` `<string>` A unique identifier for the warning instance being emitted.
  - `ctor` `<Function>` When `warning` is a `String`, `ctor` is an optional function used to limit the generated stack trace. **Default:** `process.emitWarning`.
  - `detail` `<string>` Additional text to include with the error.

The `process.emitWarning()` method can be used to emit custom or application specific process warnings. These can be listened for by adding a handler to the `'warning'` event.`import { emitWarning } from 'node:process'; // Emit a warning with a code and additional detail. emitWarning('Something happened!', { code: 'MY_WARNING', detail: 'This is some additional information', }); // Emits: // (node:56338) [MY_WARNING] Warning: Something happened! // This is some additional information``const { emitWarning } = require('node:process'); // Emit a warning with a code and additional detail. emitWarning('Something happened!', { code: 'MY_WARNING', detail: 'This is some additional information', }); // Emits: // (node:56338) [MY_WARNING] Warning: Something happened! // This is some additional information`In this example, an `Error` object is generated internally by `process.emitWarning()` and passed through to the `'warning'` handler.`import process from 'node:process'; process.on('warning', (warning) => { console.warn(warning.name); // 'Warning' console.warn(warning.message); // 'Something happened!' console.warn(warning.code); // 'MY_WARNING' console.warn(warning.stack); // Stack trace console.warn(warning.detail); // 'This is some additional information' });``process.on('warning', (warning) => { console.warn(warning.name); // 'Warning' console.warn(warning.message); // 'Something happened!' console.warn(warning.code); // 'MY_WARNING' console.warn(warning.stack); // Stack trace console.warn(warning.detail); // 'This is some additional information' });`If `warning` is passed as an `Error` object, the `options` argument is ignored.

### `process.emitWarning(warning[, type[, code]][, ctor])`

- `warning` `<string>` | `<Error>` The warning to emit.
- `type` `<string>` When `warning` is a `String`, `type` is the name to use for the *type* of warning being emitted. **Default:** `'Warning'`.
- `code` `<string>` A unique identifier for the warning instance being emitted.
- `ctor` `<Function>` When `warning` is a `String`, `ctor` is an optional function used to limit the generated stack trace. **Default:** `process.emitWarning`.

The `process.emitWarning()` method can be used to emit custom or application specific process warnings. These can be listened for by adding a handler to the `'warning'` event.`import { emitWarning } from 'node:process'; // Emit a warning using a string. emitWarning('Something happened!'); // Emits: (node: 56338) Warning: Something happened!``const { emitWarning } = require('node:process'); // Emit a warning using a string. emitWarning('Something happened!'); // Emits: (node: 56338) Warning: Something happened!``import { emitWarning } from 'node:process'; // Emit a warning using a string and a type. emitWarning('Something Happened!', 'CustomWarning'); // Emits: (node:56338) CustomWarning: Something Happened!``const { emitWarning } = require('node:process'); // Emit a warning using a string and a type. emitWarning('Something Happened!', 'CustomWarning'); // Emits: (node:56338) CustomWarning: Something Happened!``import { emitWarning } from 'node:process'; emitWarning('Something happened!', 'CustomWarning', 'WARN001'); // Emits: (node:56338) [WARN001] CustomWarning: Something happened!``const { emitWarning } = require('node:process'); process.emitWarning('Something happened!', 'CustomWarning', 'WARN001'); // Emits: (node:56338) [WARN001] CustomWarning: Something happened!`In each of the previous examples, an `Error` object is generated internally by `process.emitWarning()` and passed through to the `'warning'` handler.`import process from 'node:process'; process.on('warning', (warning) => { console.warn(warning.name); console.warn(warning.message); console.warn(warning.code); console.warn(warning.stack); });``process.on('warning', (warning) => { console.warn(warning.name); console.warn(warning.message); console.warn(warning.code); console.warn(warning.stack); });`If `warning` is passed as an `Error` object, it will be passed through to the `'warning'` event handler unmodified (and the optional `type`, `code` and `ctor` arguments will be ignored):`import { emitWarning } from 'node:process'; // Emit a warning using an Error object. const myWarning = new Error('Something happened!'); // Use the Error name property to specify the type name myWarning.name = 'CustomWarning'; myWarning.code = 'WARN001'; emitWarning(myWarning); // Emits: (node:56338) [WARN001] CustomWarning: Something happened!``const { emitWarning } = require('node:process'); // Emit a warning using an Error object. const myWarning = new Error('Something happened!'); // Use the Error name property to specify the type name myWarning.name = 'CustomWarning'; myWarning.code = 'WARN001'; emitWarning(myWarning); // Emits: (node:56338) [WARN001] CustomWarning: Something happened!`A `TypeError` is thrown if `warning` is anything other than a string or `Error` object.While process warnings use `Error` objects, the process warning mechanism is **not** a replacement for normal error handling mechanisms.The following additional handling is implemented if the warning `type` is `'DeprecationWarning'`: If the `--throw-deprecation` command-line flag is used, the deprecation warning is thrown as an exception rather than being emitted as an event. If the `--no-deprecation` command-line flag is used, the deprecation warning is suppressed. If the `--trace-deprecation` command-line flag is used, the deprecation warning is printed to `stderr` along with the full stack trace.

#### Avoiding duplicate warnings

As a best practice, warnings should be emitted only once per process. To do so, place the `emitWarning()` behind a boolean.`import { emitWarning } from 'node:process'; function emitMyWarning() { if (!emitMyWarning.warned) { emitMyWarning.warned = true; emitWarning('Only warn once!'); } } emitMyWarning(); // Emits: (node: 56339) Warning: Only warn once! emitMyWarning(); // Emits nothing``const { emitWarning } = require('node:process'); function emitMyWarning() { if (!emitMyWarning.warned) { emitMyWarning.warned = true; emitWarning('Only warn once!'); } } emitMyWarning(); // Emits: (node: 56339) Warning: Only warn once! emitMyWarning(); // Emits nothing`

### `process.env`

- Type: `<Object>`

The `process.env` property returns an object containing the user environment. See `environ(7)`.An example of this object looks like:`{ "TERM": "xterm-256color", "SHELL": "/usr/local/bin/bash", "USER": "maciej", "PATH": "~/.bin/:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin", "PWD": "/Users/maciej", "EDITOR": "vim", "SHLVL": "1", "HOME": "/Users/maciej", "LOGNAME": "maciej", "_": "/usr/local/bin/node" }`It is possible to modify this object, but such modifications will not be reflected outside the Node.js process, or (unless explicitly requested) to other `Worker` threads. In other words, the following example would not work:`node -e 'process.env.foo = "bar"' && echo $foo`While the following will:`import { env } from 'node:process'; env.foo = 'bar'; console.log(env.foo);``const { env } = require('node:process'); env.foo = 'bar'; console.log(env.foo);`Assigning a property on `process.env` will implicitly convert the value to a string. **This behavior is deprecated.** Future versions of Node.js may throw an error when the value is not a string, number, or boolean.`import { env } from 'node:process'; env.test = null; console.log(env.test); // => 'null' env.test = undefined; console.log(env.test); // => 'undefined'``const { env } = require('node:process'); env.test = null; console.log(env.test); // => 'null' env.test = undefined; console.log(env.test); // => 'undefined'`Use `delete` to delete a property from `process.env`.`import { env } from 'node:process'; env.TEST = 1; delete env.TEST; console.log(env.TEST); // => undefined``const { env } = require('node:process'); env.TEST = 1; delete env.TEST; console.log(env.TEST); // => undefined`On Windows operating systems, environment variables are case-insensitive.`import { env } from 'node:process'; env.TEST = 1; console.log(env.test); // => 1``const { env } = require('node:process'); env.TEST = 1; console.log(env.test); // => 1`Unless explicitly specified when creating a `Worker` instance, each `Worker` thread has its own copy of `process.env`, based on its parent thread's `process.env`, or whatever was specified as the `env` option to the `Worker` constructor. Changes to `process.env` will not be visible across `Worker` threads, and only the main thread can make changes that are visible to the operating system or to native add-ons. On Windows, a copy of `process.env` on a `Worker` instance operates in a case-sensitive manner unlike the main thread.

### `process.execArgv`

- Type: `<string>`[]

The `process.execArgv` property returns the set of Node.js-specific command-line options passed when the Node.js process was launched. These options do not appear in the array returned by the `process.argv` property, and do not include the Node.js executable, the name of the script, or any options following the script name. These options are useful in order to spawn child processes with the same execution environment as the parent.`node --icu-data-dir=./foo --require ./bar.js script.js --version`Results in `process.execArgv`:`["--icu-data-dir=./foo", "--require", "./bar.js"]`And `process.argv`:`["/usr/local/bin/node", "script.js", "--version"]`Refer to `Worker` constructor for the detailed behavior of worker threads with this property.

### `process.execPath`

- Type: `<string>`

The `process.execPath` property returns the absolute pathname of the executable that started the Node.js process. Symbolic links, if any, are resolved.`"/usr/local/bin/node"`

### `process.execve(file[, args[, env]])`

Stability: 1 - Experimental

- `file` `<string>` The name or path of the executable file to run.
- `args` `<string>`[] List of string arguments. No argument can contain a null-byte (`\u0000`).
- `env` `<Object>` Environment key-value pairs. No key or value can contain a null-byte (`\u0000`). **Default:** `process.env`.

Replaces the current process with a new process.This is achieved by using the `execve` POSIX function and therefore no memory or other resources from the current process are preserved, except for the standard input, standard output and standard error file descriptor.On success, all other resources are discarded by the system when the processes are swapped, without triggering any exit or close events, without running any JavaScript cleanup handler (for example `process.on('exit')`), and without invoking native `AtExit` callbacks registered through the embedder API. Callers that need to run cleanup logic should do so before calling `process.execve()`.This function does not return on success. If the underlying `execve(2)` system call fails, an `Error` is thrown whose `code` property is set to the corresponding `errno` string (for example, `'ENOENT'` when `file` does not exist), with `syscall` set to `'execve'` and `path` set to `file`. When `execve(2)` fails the current process continues to run with its state unchanged, so a caller may handle the error and take another action.This function is not available on Windows or IBM i.

### `process.exit([code])`

- `code` `<integer>` | `<string>` | `<null>` | `<undefined>` The exit code. For string type, only integer strings (e.g.,'1') are allowed. **Default:** `0`.

The `process.exit()` method instructs Node.js to terminate the process synchronously with an exit status of `code`. If `code` is omitted, exit uses either the 'success' code `0` or the value of `process.exitCode` if it has been set. Node.js will not terminate until all the `'exit'` event listeners are called.To exit with a 'failure' code:`import { exit } from 'node:process'; exit(1);``const { exit } = require('node:process'); exit(1);`The shell that executed Node.js should see the exit code as `1`.Calling `process.exit()` will force the process to exit as quickly as possible even if there are still asynchronous operations pending that have not yet completed fully, including I/O operations to `process.stdout` and `process.stderr`.In most situations, it is not actually necessary to call `process.exit()` explicitly. The Node.js process will exit on its own *if there is no additional work pending* in the event loop. The `process.exitCode` property can be set to tell the process which exit code to use when the process exits gracefully.For instance, the following example illustrates a *misuse* of the `process.exit()` method that could lead to data printed to stdout being truncated and lost:`import { exit } from 'node:process'; // This is an example of what *not* to do: if (someConditionNotMet()) { printUsageToStdout(); exit(1); }``const { exit } = require('node:process'); // This is an example of what *not* to do: if (someConditionNotMet()) { printUsageToStdout(); exit(1); }`The reason this is problematic is because writes to `process.stdout` in Node.js are sometimes *asynchronous* and may occur over multiple ticks of the Node.js event loop. Calling `process.exit()`, however, forces the process to exit *before* those additional writes to `stdout` can be performed.Rather than calling `process.exit()` directly, the code *should* set the `process.exitCode` and allow the process to exit naturally by avoiding scheduling any additional work for the event loop:`import process from 'node:process'; // How to properly set the exit code while letting // the process exit gracefully. if (someConditionNotMet()) { printUsageToStdout(); process.exitCode = 1; }``// How to properly set the exit code while letting // the process exit gracefully. if (someConditionNotMet()) { printUsageToStdout(); process.exitCode = 1; }`If it is necessary to terminate the Node.js process due to an error condition, throwing an *uncaught* error and allowing the process to terminate accordingly is safer than calling `process.exit()`.In `Worker` threads, this function stops the current thread rather than the current process.

### `process.exitCode`

- Type: `<integer>` | `<string>` | `<null>` | `<undefined>` The exit code. For string type, only integer strings (e.g.,'1') are allowed. **Default:** `undefined`.

A number which will be the process exit code, when the process either exits gracefully, or is exited via `process.exit()` without specifying a code.The value of `process.exitCode` can be updated by either assigning a value to `process.exitCode` or by passing an argument to `process.exit()`:`$ node -e 'process.exitCode = 9'; echo $? 9 $ node -e 'process.exit(42)'; echo $? 42 $ node -e 'process.exitCode = 9; process.exit(42)'; echo $? 42`The value can also be set implicitly by Node.js when unrecoverable errors occur (e.g. such as the encountering of an unsettled top-level await). However explicit manipulations of the exit code always take precedence over implicit ones:`$ node --input-type=module -e 'await new Promise(() => {})'; echo $? 13 $ node --input-type=module -e 'process.exitCode = 9; await new Promise(() => {})'; echo $? 9`

### `process.features.cached_builtins`

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build is caching builtin modules.

### `process.features.debug`

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build is a debug build.

### `process.features.inspector`

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes the inspector.

### `process.features.ipv6`

Stability: 0 - Deprecated. This property is always true, and any checks based on it are redundant.

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for IPv6.Since all Node.js builds have IPv6 support, this value is always `true`.

### `process.features.require_module`

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build supports loading ECMAScript modules using `require()`.

### `process.features.tls`

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for TLS.

### `process.features.tls_alpn`

Stability: 0 - Deprecated. Use `process.features.tls` instead.

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for ALPN in TLS.In Node.js 11.0.0 and later versions, the OpenSSL dependencies feature unconditional ALPN support. This value is therefore identical to that of `process.features.tls`.

### `process.features.tls_ocsp`

Stability: 0 - Deprecated. Use `process.features.tls` instead.

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for OCSP in TLS.In Node.js 11.0.0 and later versions, the OpenSSL dependencies feature unconditional OCSP support. This value is therefore identical to that of `process.features.tls`.

### `process.features.tls_sni`

Stability: 0 - Deprecated. Use `process.features.tls` instead.

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for SNI in TLS.In Node.js 11.0.0 and later versions, the OpenSSL dependencies feature unconditional SNI support. This value is therefore identical to that of `process.features.tls`.

### `process.features.typescript`

Stability: 1.2 - Release candidate

- Type: `<boolean>` | `<string>`

A value that is `"strip"` by default, and `false` if Node.js is run with `--no-strip-types`.

### `process.features.uv`

Stability: 0 - Deprecated. This property is always true, and any checks based on it are redundant.

- Type: `<boolean>`

A boolean value that is `true` if the current Node.js build includes support for libuv.Since it's not possible to build Node.js without libuv, this value is always `true`.

### `process.finalization.register(ref, callback)`

Stability: 1.1 - Active Development

- `ref` `<Object>` | `<Function>` The reference to the resource that is being tracked.
- `callback` `<Function>` The callback function to be called when the resource is finalized.
  - `ref` `<Object>` | `<Function>` The reference to the resource that is being tracked.
  - `event` `<string>` The event that triggered the finalization. Defaults to 'exit'.

This function registers a callback to be called when the process emits the `exit` event if the `ref` object was not garbage collected. If the object `ref` was garbage collected before the `exit` event is emitted, the callback will be removed from the finalization registry, and it will not be called on process exit.Inside the callback you can release the resources allocated by the `ref` object. Be aware that all limitations applied to the `beforeExit` event are also applied to the `callback` function, this means that there is a possibility that the callback will not be called under special circumstances.The idea of this function is to help you free up resources when the starts process exiting, but also let the object be garbage collected if it is no longer being used.Eg: you can register an object that contains a buffer, you want to make sure that buffer is released when the process exit, but if the object is garbage collected before the process exit, we no longer need to release the buffer, so in this case we just remove the callback from the finalization registry.`const { finalization } = require('node:process'); // Please make sure that the function passed to finalization.register() // does not create a closure around unnecessary objects. function onFinalize(obj, event) { // You can do whatever you want with the object obj.dispose(); } function setup() { // This object can be safely garbage collected, // and the resulting shutdown function will not be called. // There are no leaks. const myDisposableObject = { dispose() { // Free your resources synchronously }, }; finalization.register(myDisposableObject, onFinalize); } setup();``import { finalization } from 'node:process'; // Please make sure that the function passed to finalization.register() // does not create a closure around unnecessary objects. function onFinalize(obj, event) { // You can do whatever you want with the object obj.dispose(); } function setup() { // This object can be safely garbage collected, // and the resulting shutdown function will not be called. // There are no leaks. const myDisposableObject = { dispose() { // Free your resources synchronously }, }; finalization.register(myDisposableObject, onFinalize); } setup();`The code above relies on the following assumptions: arrow functions are avoided regular functions are recommended to be within the global context (root) Regular functions *could* reference the context where the `obj` lives, making the `obj` not garbage collectible.Arrow functions will hold the previous context. Consider, for example:`class Test { constructor() { finalization.register(this, (ref) => ref.dispose()); // Even something like this is highly discouraged // finalization.register(this, () => this.dispose()); } dispose() {} }`It is very unlikely (not impossible) that this object will be garbage collected, but if it is not, `dispose` will be called when `process.exit` is called.Be careful and avoid relying on this feature for the disposal of critical resources, as it is not guaranteed that the callback will be called under all circumstances.

### `process.finalization.registerBeforeExit(ref, callback)`

Stability: 1.1 - Active Development

- `ref` `<Object>` | `<Function>` The reference to the resource that is being tracked.
- `callback` `<Function>` The callback function to be called when the resource is finalized.
  - `ref` `<Object>` | `<Function>` The reference to the resource that is being tracked.
  - `event` `<string>` The event that triggered the finalization. Defaults to 'beforeExit'.

This function behaves exactly like the `register`, except that the callback will be called when the process emits the `beforeExit` event if `ref` object was not garbage collected.Be aware that all limitations applied to the `beforeExit` event are also applied to the `callback` function, this means that there is a possibility that the callback will not be called under special circumstances.

### `process.finalization.unregister(ref)`

Stability: 1.1 - Active Development

- `ref` `<Object>` | `<Function>` The reference to the resource that was registered previously.

This function remove the register of the object from the finalization registry, so the callback will not be called anymore.`const { finalization } = require('node:process'); // Please make sure that the function passed to finalization.register() // does not create a closure around unnecessary objects. function onFinalize(obj, event) { // You can do whatever you want with the object obj.dispose(); } function setup() { // This object can be safely garbage collected, // and the resulting shutdown function will not be called. // There are no leaks. const myDisposableObject = { dispose() { // Free your resources synchronously }, }; finalization.register(myDisposableObject, onFinalize); // Do something myDisposableObject.dispose(); finalization.unregister(myDisposableObject); } setup();``import { finalization } from 'node:process'; // Please make sure that the function passed to finalization.register() // does not create a closure around unnecessary objects. function onFinalize(obj, event) { // You can do whatever you want with the object obj.dispose(); } function setup() { // This object can be safely garbage collected, // and the resulting shutdown function will not be called. // There are no leaks. const myDisposableObject = { dispose() { // Free your resources synchronously }, }; // Please make sure that the function passed to finalization.register() // does not create a closure around unnecessary objects. function onFinalize(obj, event) { // You can do whatever you want with the object obj.dispose(); } finalization.register(myDisposableObject, onFinalize); // Do something myDisposableObject.dispose(); finalization.unregister(myDisposableObject); } setup();`

### `process.getActiveResourcesInfo()`

- Returns: `<string>`[]

The `process.getActiveResourcesInfo()` method returns an array of strings containing the types of the active resources that are currently keeping the event loop alive.`import { getActiveResourcesInfo } from 'node:process'; import { setTimeout } from 'node:timers'; console.log('Before:', getActiveResourcesInfo()); setTimeout(() => {}, 1000); console.log('After:', getActiveResourcesInfo()); // Prints: // Before: [ 'CloseReq', 'TTYWrap', 'TTYWrap', 'TTYWrap' ] // After: [ 'CloseReq', 'TTYWrap', 'TTYWrap', 'TTYWrap', 'Timeout' ]``const { getActiveResourcesInfo } = require('node:process'); const { setTimeout } = require('node:timers'); console.log('Before:', getActiveResourcesInfo()); setTimeout(() => {}, 1000); console.log('After:', getActiveResourcesInfo()); // Prints: // Before: [ 'TTYWrap', 'TTYWrap', 'TTYWrap' ] // After: [ 'TTYWrap', 'TTYWrap', 'TTYWrap', 'Timeout' ]`

### `process.getBuiltinModule(id)`

- `id` `<string>` ID of the built-in module being requested.
- Returns: `<Object>` | `<undefined>`

`process.getBuiltinModule(id)` provides a way to load built-in modules in a globally available function. ES Modules that need to support other environments can use it to conditionally load a Node.js built-in when it is run in Node.js, without having to deal with the resolution error that can be thrown by `import` in a non-Node.js environment or having to use dynamic `import()` which either turns the module into an asynchronous module, or turns a synchronous API into an asynchronous one.if (globalThis.process?.getBuiltinModule) { // Run in Node.js, use the Node.js fs module. const fs = globalThis.process.getBuiltinModule('fs'); // If `require()` is needed to load user-modules, use createRequire() const module = globalThis.process.getBuiltinModule('module'); const require = module.createRequire(import.meta.url); const foo = require('foo'); }If `id` specifies a built-in module available in the current Node.js process, `process.getBuiltinModule(id)` method returns the corresponding built-in module. If `id` does not correspond to any built-in module, `undefined` is returned.`process.getBuiltinModule(id)` accepts built-in module IDs that are recognized by `module.isBuiltin(id)`. Some built-in modules must be loaded with the `node:` prefix, see built-in modules with mandatory `node:` prefix. The references returned by `process.getBuiltinModule(id)` always point to the built-in module corresponding to `id` even if users modify `require.cache` so that `require(id)` returns something else.

### `process.getegid()`

The `process.getegid()` method returns the numerical effective group identity of the Node.js process. (See `getegid(2)`.)import process from 'node:process'; if (process.getegid) { console.log(`Current gid: ${process.getegid()}`); }if (process.getegid) { console.log(`Current gid: ${process.getegid()}`); }This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.geteuid()`

- Returns: `<Object>`

The `process.geteuid()` method returns the numerical effective user identity of the process. (See `geteuid(2)`.)import process from 'node:process'; if (process.geteuid) { console.log(`Current uid: ${process.geteuid()}`); }if (process.geteuid) { console.log(`Current uid: ${process.geteuid()}`); }This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.getgid()`

- Returns: `<Object>`

The `process.getgid()` method returns the numerical group identity of the process. (See `getgid(2)`.)import process from 'node:process'; if (process.getgid) { console.log(`Current gid: ${process.getgid()}`); }if (process.getgid) { console.log(`Current gid: ${process.getgid()}`); }This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.getgroups()`

- Returns: `<integer>`[]

The `process.getgroups()` method returns an array with the supplementary group IDs. POSIX leaves it unspecified if the effective group ID is included but Node.js ensures it always is.`import process from 'node:process'; if (process.getgroups) { console.log(process.getgroups()); // [ 16, 21, 297 ] }``if (process.getgroups) { console.log(process.getgroups()); // [ 16, 21, 297 ] }`This function is only available on POSIX platforms (i.e. not Windows or Android).
