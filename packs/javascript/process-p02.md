---
title: "Process (part 2/3)"
source: https://nodejs.org/api/process.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 2/3
---

# Process

`process.getBuiltinModule(id)` provides a way to load built-in modules in a globally available function. ES Modules that need to support other environments can use it to conditionally load a Node.js built-in when it is run in Node.js, without having to deal with the resolution error that can be thrown by `import` in a non-Node.js environment or having to use dynamic `import()` which either turns the module into an asynchronous module, or turns a synchronous API into an asynchronous one.if (globalThis.process?.getBuiltinModule) { // Run in Node.js, use the Node.js fs module. const fs = globalThis.process.getBuiltinModule('fs'); // If `require()` is needed to load user-modules, use createRequire() const module = globalThis.process.getBuiltinModule('module'); const require = module.createRequire(import.meta.url); const foo = require('foo'); }

If `id` specifies a built-in module available in the current Node.js process, `process.getBuiltinModule(id)` method returns the corresponding built-in module. If `id` does not correspond to any built-in module, `undefined` is returned.

`process.getBuiltinModule(id)` accepts built-in module IDs that are recognized by `module.isBuiltin(id)`. Some built-in modules must be loaded with the `node:` prefix, see built-in modules with mandatory `node:` prefix. The references returned by `process.getBuiltinModule(id)` always point to the built-in module corresponding to `id` even if users modify `require.cache` so that `require(id)` returns something else.

### `process.getegid()`

The `process.getegid()` method returns the numerical effective group identity of the Node.js process. (See `getegid(2)`.)import process from 'node:process'; if (process.getegid) { console.log(`Current gid: ${process.getegid()}`); }if (process.getegid) { console.log(`Current gid: ${process.getegid()}`); }

This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.geteuid()`

- Returns: `<Object>`

The `process.geteuid()` method returns the numerical effective user identity of the process. (See `geteuid(2)`.)import process from 'node:process'; if (process.geteuid) { console.log(`Current uid: ${process.geteuid()}`); }if (process.geteuid) { console.log(`Current uid: ${process.geteuid()}`); }

This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.getgid()`

- Returns: `<Object>`

The `process.getgid()` method returns the numerical group identity of the process. (See `getgid(2)`.)import process from 'node:process'; if (process.getgid) { console.log(`Current gid: ${process.getgid()}`); }if (process.getgid) { console.log(`Current gid: ${process.getgid()}`); }

This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.getgroups()`

- Returns: `<integer>`[]

The `process.getgroups()` method returns an array with the supplementary group IDs. POSIX leaves it unspecified if the effective group ID is included but Node.js ensures it always is.`import process from 'node:process'; if (process.getgroups) { console.log(process.getgroups()); // [ 16, 21, 297 ] }``if (process.getgroups) { console.log(process.getgroups()); // [ 16, 21, 297 ] }`

This function is only available on POSIX platforms (i.e. not Windows or Android).

### `process.getuid()`

- Returns: `<integer>`

The `process.getuid()` method returns the numeric user identity of the process. (See `getuid(2)`.)import process from 'node:process'; if (process.getuid) { console.log(`Current uid: ${process.getuid()}`); }if (process.getuid) { console.log(`Current uid: ${process.getuid()}`); }

This function not available on Windows.

### `process.hasUncaughtExceptionCaptureCallback()`

- Returns: `<boolean>`

Indicates whether a callback has been set using `process.setUncaughtExceptionCaptureCallback()`.

### `process.hrtime([time])`

Stability: 3 - Legacy. Use `process.hrtime.bigint()` instead.

- `time` `<integer>`[] The result of a previous call to `process.hrtime()`
- Returns: `<integer>`[]

This is the legacy version of `process.hrtime.bigint()` before `bigint` was introduced in JavaScript.

The `process.hrtime()` method returns the current high-resolution real time in a `[seconds, nanoseconds]` tuple `Array`, where `nanoseconds` is the remaining part of the real time that can't be represented in second precision.

`time` is an optional parameter that must be the result of a previous `process.hrtime()` call to diff with the current time. If the parameter passed in is not a tuple `Array`, a `TypeError` will be thrown. Passing in a user-defined array instead of the result of a previous call to `process.hrtime()` will lead to undefined behavior.

These times are relative to an arbitrary time in the past, and not related to the time of day and therefore not subject to clock drift. The primary use is for measuring performance between intervals:import { hrtime } from 'node:process'; const NS_PER_SEC = 1e9; const time = hrtime(); // [ 1800216, 25 ] setTimeout(() => { const diff = hrtime(time); // [ 1, 552 ] console.log(`Benchmark took ${diff[0] * NS_PER_SEC + diff[1]} nanoseconds`); // Benchmark took 1000000552 nanoseconds }, 1000);const { hrtime } = require('node:process'); const NS_PER_SEC = 1e9; const time = hrtime(); // [ 1800216, 25 ] setTimeout(() => { const diff = hrtime(time); // [ 1, 552 ] console.log(`Benchmark took ${diff[0] * NS_PER_SEC + diff[1]} nanoseconds`); // Benchmark took 1000000552 nanoseconds }, 1000);

### `process.hrtime.bigint()`

- Returns: `<bigint>`

The `bigint` version of the `process.hrtime()` method returning the current high-resolution real time in nanoseconds as a `bigint`.

Unlike `process.hrtime()`, it does not support an additional `time` argument since the difference can just be computed directly by subtraction of the two `bigint`s.import { hrtime } from 'node:process'; const start = hrtime.bigint(); // 191051479007711n setTimeout(() => { const end = hrtime.bigint(); // 191052633396993n console.log(`Benchmark took ${end - start} nanoseconds`); // Benchmark took 1154389282 nanoseconds }, 1000);const { hrtime } = require('node:process'); const start = hrtime.bigint(); // 191051479007711n setTimeout(() => { const end = hrtime.bigint(); // 191052633396993n console.log(`Benchmark took ${end - start} nanoseconds`); // Benchmark took 1154389282 nanoseconds }, 1000);

### `process.initgroups(user, extraGroup)`

- `user` `<string>` | `<number>` The user name or numeric identifier.
- `extraGroup` `<string>` | `<number>` A group name or numeric identifier.

The `process.initgroups()` method reads the `/etc/group` file and initializes the group access list, using all groups of which the user is a member. This is a privileged operation that requires that the Node.js process either have `root` access or the `CAP_SETGID` capability.

Use care when dropping privileges:`import { getgroups, initgroups, setgid } from 'node:process'; console.log(getgroups()); // [ 0 ] initgroups('nodeuser', 1000); // switch user console.log(getgroups()); // [ 27, 30, 46, 1000, 0 ] setgid(1000); // drop root gid console.log(getgroups()); // [ 27, 30, 46, 1000 ]``const { getgroups, initgroups, setgid } = require('node:process'); console.log(getgroups()); // [ 0 ] initgroups('nodeuser', 1000); // switch user console.log(getgroups()); // [ 27, 30, 46, 1000, 0 ] setgid(1000); // drop root gid console.log(getgroups()); // [ 27, 30, 46, 1000 ]`

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.kill(pid[, signal])`

- `pid` `<number>` A process ID
- `signal` `<string>` | `<number>` The signal to send, either as a string or number. **Default:** `'SIGTERM'`.

The `process.kill()` method sends the `signal` to the process identified by `pid`.

Signal names are strings such as `'SIGINT'` or `'SIGHUP'`. See Signal Events and `kill(2)` for more information.

This method will throw an error if the target `pid` does not exist. As a special case, a signal of `0` can be used to test for the existence of a process. Windows platforms will throw an error if the `pid` is used to kill a process group.

Even though the name of this function is `process.kill()`, it is really just a signal sender, like the `kill` system call. The signal sent may do something other than kill the target process.`import process, { kill } from 'node:process'; process.on('SIGHUP', () => { console.log('Got SIGHUP signal.'); }); setTimeout(() => { console.log('Exiting.'); process.exit(0); }, 100); kill(process.pid, 'SIGHUP');``process.on('SIGHUP', () => { console.log('Got SIGHUP signal.'); }); setTimeout(() => { console.log('Exiting.'); process.exit(0); }, 100); process.kill(process.pid, 'SIGHUP');`

When `SIGUSR1` is received by a Node.js process, Node.js will start the debugger. See Signal Events.

### `process.loadEnvFile(path)`

- `path` `<string>` | `<URL>` | `<Buffer>` | `<undefined>`. **Default:** `'./.env'`

Loads the `.env` file into `process.env`. Usage of `NODE_OPTIONS` in the `.env` file will not have any effect on Node.js.`const { loadEnvFile } = require('node:process'); loadEnvFile();``import { loadEnvFile } from 'node:process'; loadEnvFile();`

### `process.mainModule`

Stability: 0 - Deprecated: Use `require.main` instead.

- Type: `<Object>`

The `process.mainModule` property provides an alternative way of retrieving `require.main`. The difference is that if the main module changes at runtime, `require.main` may still refer to the original main module in modules that were required before the change occurred. Generally, it's safe to assume that the two refer to the same module.

As with `require.main`, `process.mainModule` will be `undefined` if there is no entry script.

### `process.memoryUsage()`

- Returns: `<Object>`
  - `rss` `<integer>`
  - `heapTotal` `<integer>`
  - `heapUsed` `<integer>`
  - `external` `<integer>`
  - `arrayBuffers` `<integer>`

Returns an object describing the memory usage of the Node.js process measured in bytes.`import { memoryUsage } from 'node:process'; console.log(memoryUsage()); // Prints: // { // rss: 4935680, // heapTotal: 1826816, // heapUsed: 650472, // external: 49879, // arrayBuffers: 9386 // }``const { memoryUsage } = require('node:process'); console.log(memoryUsage()); // Prints: // { // rss: 4935680, // heapTotal: 1826816, // heapUsed: 650472, // external: 49879, // arrayBuffers: 9386 // }` `heapTotal` and `heapUsed` refer to V8's memory usage. `external` refers to the memory usage of C++ objects bound to JavaScript objects managed by V8. `rss`, Resident Set Size, is the amount of space occupied in the main memory device (that is a subset of the total allocated memory) for the process, including all C++ and JavaScript objects and code. `arrayBuffers` refers to memory allocated for `ArrayBuffer`s and `SharedArrayBuffer`s, including all Node.js `Buffer`s. This is also included in the `external` value. When Node.js is used as an embedded library, this value may be `0` because allocations for `ArrayBuffer`s may not be tracked in that case.

When using `Worker` threads, `rss` will be a value that is valid for the entire process, while the other fields will only refer to the current thread.

The `process.memoryUsage()` method iterates over each page to gather information about memory usage which might be slow depending on the program memory allocations.

#### A note on process memoryUsage

On Linux or other systems where glibc is commonly used, an application may have sustained `rss` growth despite stable `heapTotal` due to fragmentation caused by the glibc `malloc` implementation. See nodejs/node#21973 on how to switch to an alternative `malloc` implementation to address the performance issue.

### `process.memoryUsage.rss()`

- Returns: `<integer>`

The `process.memoryUsage.rss()` method returns an integer representing the Resident Set Size (RSS) in bytes.

The Resident Set Size, is the amount of space occupied in the main memory device (that is a subset of the total allocated memory) for the process, including all C++ and JavaScript objects and code.

This is the same value as the `rss` property provided by `process.memoryUsage()` but `process.memoryUsage.rss()` is faster.`import { memoryUsage } from 'node:process'; console.log(memoryUsage.rss()); // 35655680``const { memoryUsage } = require('node:process'); console.log(memoryUsage.rss()); // 35655680`

### `process.nextTick(callback[, ...args])`

Stability: 3 - Legacy: Use `queueMicrotask()` instead.

- `callback` `<Function>`
- `...args` `<any>` Additional arguments to pass when invoking the `callback`

`process.nextTick()` adds `callback` to the "next tick queue". This queue is fully drained after the current operation on the JavaScript stack runs to completion and before the event loop is allowed to continue. It's possible to create an infinite loop if one were to recursively call `process.nextTick()`. See the Event Loop guide for more background.`import { nextTick } from 'node:process'; console.log('start'); nextTick(() => { console.log('nextTick callback'); }); console.log('scheduled'); // Output: // start // scheduled // nextTick callback``const { nextTick } = require('node:process'); console.log('start'); nextTick(() => { console.log('nextTick callback'); }); console.log('scheduled'); // Output: // start // scheduled // nextTick callback`

This is important when developing APIs in order to give users the opportunity to assign event handlers *after* an object has been constructed but before any I/O has occurred:`import { nextTick } from 'node:process'; function MyThing(options) { this.setupOptions(options); nextTick(() => { this.startDoingStuff(); }); } const thing = new MyThing(); thing.getReadyForStuff(); // thing.startDoingStuff() gets called now, not before.``const { nextTick } = require('node:process'); function MyThing(options) { this.setupOptions(options); nextTick(() => { this.startDoingStuff(); }); } const thing = new MyThing(); thing.getReadyForStuff(); // thing.startDoingStuff() gets called now, not before.`

It is very important for APIs to be either 100% synchronous or 100% asynchronous. Consider this example:`// WARNING! DO NOT USE! BAD UNSAFE HAZARD! function maybeSync(arg, cb) { if (arg) { cb(); return; } fs.stat('file', cb); }`

This API is hazardous because in the following case:`const maybeTrue = Math.random() > 0.5; maybeSync(maybeTrue, () => { foo(); }); bar();`

It is not clear whether `foo()` or `bar()` will be called first.

The following approach is much better:`import { nextTick } from 'node:process'; function definitelyAsync(arg, cb) { if (arg) { nextTick(cb); return; } fs.stat('file', cb); }``const { nextTick } = require('node:process'); function definitelyAsync(arg, cb) { if (arg) { nextTick(cb); return; } fs.stat('file', cb); }`

#### When to use `queueMicrotask()` vs. `process.nextTick()`

The `queueMicrotask()` API is an alternative to `process.nextTick()` that instead of using the "next tick queue" defers execution of a function using the same microtask queue used to execute the then, catch, and finally handlers of resolved promises.

Within Node.js, every time the "next tick queue" is drained, the microtask queue is drained immediately after.

So in CJS modules `process.nextTick()` callbacks are always run before `queueMicrotask()` ones. However since ESM modules are processed already as part of the microtask queue, there `queueMicrotask()` callbacks are always executed before `process.nextTick()` ones since Node.js is already in the process of draining the microtask queue.`import { nextTick } from 'node:process'; Promise.resolve().then(() => console.log('resolve')); queueMicrotask(() => console.log('microtask')); nextTick(() => console.log('nextTick')); // Output: // resolve // microtask // nextTick``const { nextTick } = require('node:process'); Promise.resolve().then(() => console.log('resolve')); queueMicrotask(() => console.log('microtask')); nextTick(() => console.log('nextTick')); // Output: // nextTick // resolve // microtask`

For *most* userland use cases, the `queueMicrotask()` API provides a portable and reliable mechanism for deferring execution that works across multiple JavaScript platform environments and should be favored over `process.nextTick()`. In simple scenarios, `queueMicrotask()` can be a drop-in replacement for `process.nextTick()`.`console.log('start'); queueMicrotask(() => { console.log('microtask callback'); }); console.log('scheduled'); // Output: // start // scheduled // microtask callback`

One note-worthy difference between the two APIs is that `process.nextTick()` allows specifying additional values that will be passed as arguments to the deferred function when it is called. Achieving the same result with `queueMicrotask()` requires using either a closure or a bound function:`function deferred(a, b) { console.log('microtask', a + b); } console.log('start'); queueMicrotask(deferred.bind(undefined, 1, 2)); console.log('scheduled'); // Output: // start // scheduled // microtask 3`

There are minor differences in the way errors raised from within the next tick queue and microtask queue are handled. Errors thrown within a queued microtask callback should be handled within the queued callback when possible. If they are not, the `process.on('uncaughtException')` event handler can be used to capture and handle the errors.

When in doubt, unless the specific capabilities of `process.nextTick()` are needed, use `queueMicrotask()`.

### `process.noDeprecation`

- Type: `<boolean>`

The `process.noDeprecation` property indicates whether the `--no-deprecation` flag is set on the current Node.js process. See the documentation for the `'warning'` event and the `emitWarning()` method for more information about this flag's behavior.

### `process.permission`

- Type: `<Object>`

This API is available through the `--permission` flag.

`process.permission` is an object whose methods are used to manage permissions for the current process. Additional documentation is available in the Permission Model.

#### `process.permission.has(scope[, reference])`

- `scope` `<string>`
- `reference` `<string>`
- Returns: `<boolean>`

Verifies that the process is able to access the given scope and reference. If no reference is provided, a global scope is assumed, for instance, `process.permission.has('fs.read')` will check if the process has ALL file system read permissions.

The reference has a meaning based on the provided scope. For example, the reference when the scope is File System means files and folders.

The available scopes are: `fs` - All File System `fs.read` - File System read operations `fs.write` - File System write operations `child` - Child process spawning operations `worker` - Worker thread spawning operation `ffi` - Foreign function interface operations `// Check if the process has permission to read the README file process.permission.has('fs.read', './README.md'); // Check if the process has read permission operations process.permission.has('fs.read');`

#### `process.permission.drop(scope[, reference])`

Stability: 1.1 - Active Development

- `scope` `<string>`
- `reference` `<string>`

Drops the specified permission from the current process. This operation is **irreversible** — once a permission is dropped, it cannot be restored through any Node.js API.

If no reference is provided, the entire scope is dropped. For example, `process.permission.drop('fs.read')` will revoke ALL file system read permissions.

When a reference is provided, only the permission for that specific resource is dropped. For example, `process.permission.drop('fs.read', '/etc/myapp')` will revoke read access to that directory while keeping other read permissions intact.

**Important:** You can only drop the exact resource that was explicitly granted. The reference passed to `drop()` must match the original grant: If a permission was granted using a wildcard (`*`), such as `--allow-fs-read=*`, individual paths cannot be dropped - only the entire scope can be dropped (by calling `drop()` without a reference). If a directory was granted (e.g. `--allow-fs-read=/my/folder`), you cannot drop access to individual files inside it. You must drop the same directory that was granted. Any remaining grants continue to apply.

The available scopes are the same as `process.permission.has()`: `fs` - All File System (drops both read and write) `fs.read` - File System read operations `fs.write` - File System write operations `child` - Child process spawning operations `worker` - Worker thread spawning operation `net` - Network operations `inspector` - Inspector operations `wasi` - WASI operations `addon` - Native addon operations `const fs = require('node:fs'); // Read configuration during startup const config = fs.readFileSync('/etc/myapp/config.json', 'utf8'); // Drop read access to the config directory after initialization process.permission.drop('fs.read', '/etc/myapp'); // This will now throw ERR_ACCESS_DENIED fs.readFileSync('/etc/myapp/config.json');`

### `process.pid`

- Type: `<integer>`

The `process.pid` property returns the PID of the process.import { pid } from 'node:process'; console.log(`This process is pid ${pid}`);const { pid } = require('node:process'); console.log(`This process is pid ${pid}`);

### `process.platform`

- Type: `<string>`

The `process.platform` property returns a string identifying the operating system platform for which the Node.js binary was compiled.

Currently possible values are: `'aix'` `'darwin'` `'freebsd'` `'linux'` `'openbsd'` `'sunos'` `'win32'` import { platform } from 'node:process'; console.log(`This platform is ${platform}`);const { platform } = require('node:process'); console.log(`This platform is ${platform}`);

The value `'android'` may also be returned if the Node.js is built on the Android operating system. However, Android support in Node.js is experimental.

### `process.ppid`

- Type: `<integer>`

The `process.ppid` property returns the PID of the parent of the current process.import { ppid } from 'node:process'; console.log(`The parent process is pid ${ppid}`);const { ppid } = require('node:process'); console.log(`The parent process is pid ${ppid}`);

### `process.ref(maybeRefable)`

Stability: 1 - Experimental

- `maybeRefable` `<any>` An object that may be "refable".

An object is "refable" if it implements the Node.js "Refable protocol". Specifically, this means that the object implements the `Symbol.for('nodejs.ref')` and `Symbol.for('nodejs.unref')` methods. "Ref'd" objects will keep the Node.js event loop alive, while "unref'd" objects will not. Historically, this was implemented by using `ref()` and `unref()` methods directly on the objects. This pattern, however, is being deprecated in favor of the "Refable protocol" in order to better support Web Platform API types whose APIs cannot be modified to add `ref()` and `unref()` methods but still need to support that behavior.

### `process.release`

- Type: `<Object>`

The `process.release` property returns an `Object` containing metadata related to the current release, including URLs for the source tarball and headers-only tarball.

`process.release` contains the following properties: `name` `<string>` A value that will always be `'node'`. `sourceUrl` `<string>` an absolute URL pointing to a *`.tar.gz`* file containing the source code of the current release. `headersUrl``<string>` an absolute URL pointing to a *`.tar.gz`* file containing only the source header files for the current release. This file is significantly smaller than the full source file and can be used for compiling Node.js native add-ons. `libUrl` `<string>` | `<undefined>` an absolute URL pointing to a *`node.lib`* file matching the architecture and version of the current release. This file is used for compiling Node.js native add-ons. *This property is only present on Windows builds of Node.js and will be missing on all other platforms.* `lts` `<string>` | `<undefined>` a string label identifying the LTS label for this release. This property only exists for LTS releases and is `undefined` for all other release types, including *Current* releases. Valid values include the LTS Release code names (including those that are no longer supported). `'Fermium'` for the 14.x LTS line beginning with 14.15.0. `'Gallium'` for the 16.x LTS line beginning with 16.13.0. `'Hydrogen'` for the 18.x LTS line beginning with 18.12.0. For other LTS Release code names, see Node.js Changelog Archive `{ "name": "node", "lts": "Hydrogen", "sourceUrl": "https://nodejs.org/download/release/v18.12.0/node-v18.12.0.tar.gz", "headersUrl": "https://nodejs.org/download/release/v18.12.0/node-v18.12.0-headers.tar.gz", "libUrl": "https://nodejs.org/download/release/v18.12.0/win-x64/node.lib" }`

In custom builds from non-release versions of the source tree, only the `name` property may be present. The additional properties should not be relied upon to exist.

### `process.report`

- Type: `<Object>`

`process.report` is an object whose methods are used to generate diagnostic reports for the current process. Additional documentation is available in the report documentation.

#### `process.report.compact`

- Type: `<boolean>`

Write reports in a compact format, single-line JSON, more easily consumable by log processing systems than the default multi-line format designed for human consumption.import { report } from 'node:process'; console.log(`Reports are compact? ${report.compact}`);const { report } = require('node:process'); console.log(`Reports are compact? ${report.compact}`);

#### `process.report.directory`

- Type: `<string>`

Directory where the report is written. The default value is the empty string, indicating that reports are written to the current working directory of the Node.js process.import { report } from 'node:process'; console.log(`Report directory is ${report.directory}`);const { report } = require('node:process'); console.log(`Report directory is ${report.directory}`);

#### `process.report.filename`

- Type: `<string>`

Filename where the report is written. If set to the empty string, the output filename will be comprised of a timestamp, PID, and sequence number. The default value is the empty string.

If the value of `process.report.filename` is set to `'stdout'` or `'stderr'`, the report is written to the stdout or stderr of the process respectively.import { report } from 'node:process'; console.log(`Report filename is ${report.filename}`);const { report } = require('node:process'); console.log(`Report filename is ${report.filename}`);

#### `process.report.getReport([err])`

- `err` `<Error>` A custom error used for reporting the JavaScript stack.
- Returns: `<Object>`

Returns a JavaScript Object representation of a diagnostic report for the running process. The report's JavaScript stack trace is taken from `err`, if present.`import { report } from 'node:process'; import util from 'node:util'; const data = report.getReport(); console.log(data.header.nodejsVersion); // Similar to process.report.writeReport() import fs from 'node:fs'; fs.writeFileSync('my-report.log', util.inspect(data), 'utf8');``const { report } = require('node:process'); const util = require('node:util'); const data = report.getReport(); console.log(data.header.nodejsVersion); // Similar to process.report.writeReport() const fs = require('node:fs'); fs.writeFileSync('my-report.log', util.inspect(data), 'utf8');`

Additional documentation is available in the report documentation.
