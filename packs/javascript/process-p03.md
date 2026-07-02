---
title: "Process (part 3/3)"
source: https://nodejs.org/api/process.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 3/3
---

#### `process.report.reportOnFatalError`

- Type: `<boolean>`

If `true`, a diagnostic report is generated on fatal errors, such as out of memory errors or failed C++ assertions.import { report } from 'node:process'; console.log(`Report on fatal error: ${report.reportOnFatalError}`);const { report } = require('node:process'); console.log(`Report on fatal error: ${report.reportOnFatalError}`);

#### `process.report.reportOnSignal`

- Type: `<boolean>`

If `true`, a diagnostic report is generated when the process receives the signal specified by `process.report.signal`.import { report } from 'node:process'; console.log(`Report on signal: ${report.reportOnSignal}`);const { report } = require('node:process'); console.log(`Report on signal: ${report.reportOnSignal}`);

#### `process.report.reportOnUncaughtException`

- Type: `<boolean>`

If `true`, a diagnostic report is generated on uncaught exception.import { report } from 'node:process'; console.log(`Report on exception: ${report.reportOnUncaughtException}`);const { report } = require('node:process'); console.log(`Report on exception: ${report.reportOnUncaughtException}`);

#### `process.report.excludeEnv`

- Type: `<boolean>`

If `true`, a diagnostic report is generated without the environment variables.

#### `process.report.signal`

- Type: `<string>`

The signal used to trigger the creation of a diagnostic report. Defaults to `'SIGUSR2'`.import { report } from 'node:process'; console.log(`Report signal: ${report.signal}`);const { report } = require('node:process'); console.log(`Report signal: ${report.signal}`);

#### `process.report.writeReport([filename][, err])`

- `filename` `<string>` Name of the file where the report is written. This should be a relative path, that will be appended to the directory specified in `process.report.directory`, or the current working directory of the Node.js process, if unspecified.
- `err` `<Error>` A custom error used for reporting the JavaScript stack.
- Returns: `<string>` Returns the filename of the generated report.

Writes a diagnostic report to a file. If `filename` is not provided, the default filename includes the date, time, PID, and a sequence number. The report's JavaScript stack trace is taken from `err`, if present.

If the value of `filename` is set to `'stdout'` or `'stderr'`, the report is written to the stdout or stderr of the process respectively.`import { report } from 'node:process'; report.writeReport();``const { report } = require('node:process'); report.writeReport();`

Additional documentation is available in the report documentation.

### `process.resourceUsage()`

- Returns: `<Object>` the resource usage for the current process. All of these values come from the `uv_getrusage` call which returns a `uv_rusage_t` struct.
  - `userCPUTime` `<integer>` maps to `ru_utime` computed in microseconds. It is the same value as `process.cpuUsage().user`.
  - `systemCPUTime` `<integer>` maps to `ru_stime` computed in microseconds. It is the same value as `process.cpuUsage().system`.
  - `maxRSS` `<integer>` maps to `ru_maxrss` which is the maximum resident set size used in kibibytes (1024 bytes).
  - `sharedMemorySize` `<integer>` maps to `ru_ixrss` but is not supported by any platform.
  - `unsharedDataSize` `<integer>` maps to `ru_idrss` but is not supported by any platform.
  - `unsharedStackSize` `<integer>` maps to `ru_isrss` but is not supported by any platform.
  - `minorPageFault` `<integer>` maps to `ru_minflt` which is the number of minor page faults for the process, see this article for more details.
  - `majorPageFault` `<integer>` maps to `ru_majflt` which is the number of major page faults for the process, see this article for more details. This field is not supported on Windows.
  - `swappedOut` `<integer>` maps to `ru_nswap` but is not supported by any platform.
  - `fsRead` `<integer>` maps to `ru_inblock` which is the number of times the file system had to perform input.
  - `fsWrite` `<integer>` maps to `ru_oublock` which is the number of times the file system had to perform output.
  - `ipcSent` `<integer>` maps to `ru_msgsnd` but is not supported by any platform.
  - `ipcReceived` `<integer>` maps to `ru_msgrcv` but is not supported by any platform.
  - `signalsCount` `<integer>` maps to `ru_nsignals` but is not supported by any platform.
  - `voluntaryContextSwitches` `<integer>` maps to `ru_nvcsw` which is the number of times a CPU context switch resulted due to a process voluntarily giving up the processor before its time slice was completed (usually to await availability of a resource). This field is not supported on Windows.
  - `involuntaryContextSwitches` `<integer>` maps to `ru_nivcsw` which is the number of times a CPU context switch resulted due to a higher priority process becoming runnable or because the current process exceeded its time slice. This field is not supported on Windows.

```mjs
import { resourceUsage } from 'node:process';

console.log(resourceUsage());
/*
  Will output:
  {
    userCPUTime: 82872,
    systemCPUTime: 4143,
    maxRSS: 33164,
    sharedMemorySize: 0,
    unsharedDataSize: 0,
    unsharedStackSize: 0,
    minorPageFault: 2469,
    majorPageFault: 0,
    swappedOut: 0,
    fsRead: 0,
    fsWrite: 8,
    ipcSent: 0,
    ipcReceived: 0,
    signalsCount: 0,
    voluntaryContextSwitches: 79,
    involuntaryContextSwitches: 1
  }
*/
const { resourceUsage } = require('node:process');

console.log(resourceUsage());
/*
  Will output:
  {
    userCPUTime: 82872,
    systemCPUTime: 4143,
    maxRSS: 33164,
    sharedMemorySize: 0,
    unsharedDataSize: 0,
    unsharedStackSize: 0,
    minorPageFault: 2469,
    majorPageFault: 0,
    swappedOut: 0,
    fsRead: 0,
    fsWrite: 8,
    ipcSent: 0,
    ipcReceived: 0,
    signalsCount: 0,
    voluntaryContextSwitches: 79,
    involuntaryContextSwitches: 1
  }
*/
```

### `process.send(message[, sendHandle[, options]][, callback])`

- `message` `<Object>`
- `sendHandle` `<net.Server>` | `<net.Socket>`
- `options` `<Object>` used to parameterize the sending of certain types of handles.`options` supports the following properties:
  - `keepOpen` `<boolean>` A value that can be used when passing instances of `net.Socket`. When `true`, the socket is kept open in the sending process. **Default:** `false`.
- `callback` `<Function>`
- Returns: `<boolean>`

If Node.js is spawned with an IPC channel, the `process.send()` method can be used to send messages to the parent process. Messages will be received as a `'message'` event on the parent's `ChildProcess` object.

If Node.js was not spawned with an IPC channel, `process.send` will be `undefined`.

The message goes through serialization and parsing. The resulting message might not be the same as what is originally sent.

### `process.setegid(id)`

- `id` `<string>` | `<number>` A group name or ID

The `process.setegid()` method sets the effective group identity of the process. (See `setegid(2)`.) The `id` can be passed as either a numeric ID or a group name string. If a group name is specified, this method blocks while resolving the associated a numeric ID.import process from 'node:process'; if (process.getegid && process.setegid) { console.log(`Current gid: ${process.getegid()}`); try { process.setegid(501); console.log(`New gid: ${process.getegid()}`); } catch (err) { console.error(`Failed to set gid: ${err}`); } }if (process.getegid && process.setegid) { console.log(`Current gid: ${process.getegid()}`); try { process.setegid(501); console.log(`New gid: ${process.getegid()}`); } catch (err) { console.error(`Failed to set gid: ${err}`); } }

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.seteuid(id)`

- `id` `<string>` | `<number>` A user name or ID

The `process.seteuid()` method sets the effective user identity of the process. (See `seteuid(2)`.) The `id` can be passed as either a numeric ID or a username string. If a username is specified, the method blocks while resolving the associated numeric ID.import process from 'node:process'; if (process.geteuid && process.seteuid) { console.log(`Current uid: ${process.geteuid()}`); try { process.seteuid(501); console.log(`New uid: ${process.geteuid()}`); } catch (err) { console.error(`Failed to set uid: ${err}`); } }if (process.geteuid && process.seteuid) { console.log(`Current uid: ${process.geteuid()}`); try { process.seteuid(501); console.log(`New uid: ${process.geteuid()}`); } catch (err) { console.error(`Failed to set uid: ${err}`); } }

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.setgid(id)`

- `id` `<string>` | `<number>` The group name or ID

The `process.setgid()` method sets the group identity of the process. (See `setgid(2)`.) The `id` can be passed as either a numeric ID or a group name string. If a group name is specified, this method blocks while resolving the associated numeric ID.import process from 'node:process'; if (process.getgid && process.setgid) { console.log(`Current gid: ${process.getgid()}`); try { process.setgid(501); console.log(`New gid: ${process.getgid()}`); } catch (err) { console.error(`Failed to set gid: ${err}`); } }if (process.getgid && process.setgid) { console.log(`Current gid: ${process.getgid()}`); try { process.setgid(501); console.log(`New gid: ${process.getgid()}`); } catch (err) { console.error(`Failed to set gid: ${err}`); } }

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.setgroups(groups)`

- `groups` `<integer>`[]

The `process.setgroups()` method sets the supplementary group IDs for the Node.js process. This is a privileged operation that requires the Node.js process to have `root` or the `CAP_SETGID` capability.

The `groups` array can contain numeric group IDs, group names, or both.import process from 'node:process'; if (process.getgroups && process.setgroups) { try { process.setgroups([501]); console.log(process.getgroups()); // new groups } catch (err) { console.error(`Failed to set groups: ${err}`); } }if (process.getgroups && process.setgroups) { try { process.setgroups([501]); console.log(process.getgroups()); // new groups } catch (err) { console.error(`Failed to set groups: ${err}`); } }

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.setuid(id)`

- `id` `<integer>` | `<string>`

The `process.setuid(id)` method sets the user identity of the process. (See `setuid(2)`.) The `id` can be passed as either a numeric ID or a username string. If a username is specified, the method blocks while resolving the associated numeric ID.import process from 'node:process'; if (process.getuid && process.setuid) { console.log(`Current uid: ${process.getuid()}`); try { process.setuid(501); console.log(`New uid: ${process.getuid()}`); } catch (err) { console.error(`Failed to set uid: ${err}`); } }if (process.getuid && process.setuid) { console.log(`Current uid: ${process.getuid()}`); try { process.setuid(501); console.log(`New uid: ${process.getuid()}`); } catch (err) { console.error(`Failed to set uid: ${err}`); } }

This function is only available on POSIX platforms (i.e. not Windows or Android). This feature is not available in `Worker` threads.

### `process.setSourceMapsEnabled(val)`

Stability: 1 - Experimental: Use `module.setSourceMapsSupport()` instead.

- `val` `<boolean>`

This function enables or disables the Source Map support for stack traces.

It provides same features as launching Node.js process with commandline options `--enable-source-maps`.

Only source maps in JavaScript files that are loaded after source maps has been enabled will be parsed and loaded.

This implies calling `module.setSourceMapsSupport()` with an option `{ nodeModules: true, generatedCode: true }`.

### `process.setUncaughtExceptionCaptureCallback(fn)`

- `fn` `<Function>` | `<null>`

The `process.setUncaughtExceptionCaptureCallback()` function sets a function that will be invoked when an uncaught exception occurs, which will receive the exception value itself as its first argument.

If such a function is set, the `'uncaughtException'` event will not be emitted. If `--abort-on-uncaught-exception` was passed from the command line or set through `v8.setFlagsFromString()`, the process will not abort. Actions configured to take place on exceptions such as report generations will be affected too

To unset the capture function, `process.setUncaughtExceptionCaptureCallback(null)` may be used. Calling this method with a non-`null` argument while another capture function is set will throw an error.

To register multiple callbacks that can coexist, use `process.addUncaughtExceptionCaptureCallback()` instead.

### `process.sourceMapsEnabled`

Stability: 1 - Experimental: Use `module.getSourceMapsSupport()` instead.

- Type: `<boolean>`

The `process.sourceMapsEnabled` property returns whether the Source Map support for stack traces is enabled.

### `process.stderr`

- Type: `<Stream>`

The `process.stderr` property returns a stream connected to `stderr` (fd `2`). It is a `net.Socket` (which is a Duplex stream) unless fd `2` refers to a file, in which case it is a Writable stream.

`process.stderr` differs from other Node.js streams in important ways. See note on process I/O for more information.

#### `process.stderr.fd`

- Type: `<number>`

This property refers to the value of underlying file descriptor of `process.stderr`. The value is fixed at `2`. In `Worker` threads, this field does not exist.

### `process.stdin`

- Type: `<Stream>`

The `process.stdin` property returns a stream connected to `stdin` (fd `0`). It is a `net.Socket` (which is a Duplex stream) unless fd `0` refers to a file, in which case it is a Readable stream.

For details of how to read from `stdin` see `readable.read()`.

As a Duplex stream, `process.stdin` can also be used in "old" mode that is compatible with scripts written for Node.js prior to v0.10. For more information see Stream compatibility.

In "old" streams mode the `stdin` stream is paused by default, so one must call `process.stdin.resume()` to read from it. Note also that calling `process.stdin.resume()` itself would switch stream to "old" mode.

#### `process.stdin.fd`

- Type: `<number>`

This property refers to the value of underlying file descriptor of `process.stdin`. The value is fixed at `0`. In `Worker` threads, this field does not exist.

### `process.stdout`

- Type: `<Stream>`

The `process.stdout` property returns a stream connected to `stdout` (fd `1`). It is a `net.Socket` (which is a Duplex stream) unless fd `1` refers to a file, in which case it is a Writable stream.

For example, to copy `process.stdin` to `process.stdout`:`import { stdin, stdout } from 'node:process'; stdin.pipe(stdout);``const { stdin, stdout } = require('node:process'); stdin.pipe(stdout);`

`process.stdout` differs from other Node.js streams in important ways. See note on process I/O for more information.

#### `process.stdout.fd`

- Type: `<number>`

This property refers to the value of underlying file descriptor of `process.stdout`. The value is fixed at `1`. In `Worker` threads, this field does not exist.

#### A note on process I/O

`process.stdout` and `process.stderr` differ from other Node.js streams in important ways: They are used internally by `console.log()` and `console.error()`, respectively. Writes may be synchronous depending on what the stream is connected to and whether the system is Windows or POSIX: Files: *synchronous* on Windows and POSIX TTYs (Terminals): *asynchronous* on Windows, *synchronous* on POSIX Pipes (and sockets): *synchronous* on Windows, *asynchronous* on POSIX

These behaviors are partly for historical reasons, as changing them would create backward incompatibility, but they are also expected by some users.

Synchronous writes avoid problems such as output written with `console.log()` or `console.error()` being unexpectedly interleaved, or not written at all if `process.exit()` is called before an asynchronous write completes. See `process.exit()` for more information.

***Warning***: Synchronous writes block the event loop until the write has completed. This can be near instantaneous in the case of output to a file, but under high system load, pipes that are not being read at the receiving end, or with slow terminals or file systems, it's possible for the event loop to be blocked often enough and long enough to have severe negative performance impacts. This may not be a problem when writing to an interactive terminal session, but consider this particularly careful when doing production logging to the process output streams.

To check if a stream is connected to a TTY context, check the `isTTY` property.

For instance:`$ node -p "Boolean(process.stdin.isTTY)" true $ echo "foo" | node -p "Boolean(process.stdin.isTTY)" false $ node -p "Boolean(process.stdout.isTTY)" true $ node -p "Boolean(process.stdout.isTTY)" | cat false`

See the TTY documentation for more information.

### `process.throwDeprecation`

- Type: `<boolean>`

The initial value of `process.throwDeprecation` indicates whether the `--throw-deprecation` flag is set on the current Node.js process. `process.throwDeprecation` is mutable, so whether or not deprecation warnings result in errors may be altered at runtime. See the documentation for the `'warning'` event and the `emitWarning()` method for more information.`$ node --throw-deprecation -p "process.throwDeprecation" true $ node -p "process.throwDeprecation" undefined $ node > process.emitWarning('test', 'DeprecationWarning'); undefined > (node:26598) DeprecationWarning: test > process.throwDeprecation = true; true > process.emitWarning('test', 'DeprecationWarning'); Thrown: [DeprecationWarning: test] { name: 'DeprecationWarning' }`

### `process.threadCpuUsage([previousValue])`

- `previousValue` `<Object>` A previous return value from calling `process.threadCpuUsage()`
- Returns: `<Object>`
  - `user` `<integer>`
  - `system` `<integer>`

The `process.threadCpuUsage()` method returns the user and system CPU time usage of the current worker thread, in an object with properties `user` and `system`, whose values are microsecond values (millionth of a second).

The result of a previous call to `process.threadCpuUsage()` can be passed as the argument to the function, to get a diff reading.

### `process.title`

- Type: `<string>`

The `process.title` property returns the current process title (i.e. returns the current value of `ps`). Assigning a new value to `process.title` modifies the current value of `ps`.

When a new value is assigned, different platforms will impose different maximum length restrictions on the title. Usually such restrictions are quite limited. For instance, on Linux and macOS, `process.title` is limited to the size of the binary name plus the length of the command-line arguments because setting the `process.title` overwrites the `argv` memory of the process. Node.js 0.8 allowed for longer process title strings by also overwriting the `environ` memory but that was potentially insecure and confusing in some (rather obscure) cases.

Assigning a value to `process.title` might not result in an accurate label within process manager applications such as macOS Activity Monitor or Windows Services Manager.

### `process.traceDeprecation`

- Type: `<boolean>`

The `process.traceDeprecation` property indicates whether the `--trace-deprecation` flag is set on the current Node.js process. See the documentation for the `'warning'` event and the `emitWarning()` method for more information about this flag's behavior.

### `process.traceProcessWarnings`

- `<boolean>`

The `process.traceProcessWarnings` property indicates whether the `--trace-warnings` flag is set on the current Node.js process. This property allows programmatic control over the tracing of warnings, enabling or disabling stack traces for warnings at runtime.`// Enable trace warnings process.traceProcessWarnings = true; // Emit a warning with a stack trace process.emitWarning('Warning with stack trace'); // Disable trace warnings process.traceProcessWarnings = false;`

### `process.umask()`

Stability: 0 - Deprecated. Calling `process.umask()` with no argument causes the process-wide umask to be written twice. This introduces a race condition between threads, and is a potential security vulnerability. There is no safe, cross-platform alternative API.

`process.umask()` returns the Node.js process's file mode creation mask. Child processes inherit the mask from the parent process.

### `process.umask(mask)`

- `mask` `<string>` | `<integer>`

`process.umask(mask)` sets the Node.js process's file mode creation mask. Child processes inherit the mask from the parent process. Returns the previous mask.import { umask } from 'node:process'; const newmask = 0o022; const oldmask = umask(newmask); console.log( `Changed umask from ${oldmask.toString(8)} to ${newmask.toString(8)}`, );const { umask } = require('node:process'); const newmask = 0o022; const oldmask = umask(newmask); console.log( `Changed umask from ${oldmask.toString(8)} to ${newmask.toString(8)}`, );

In `Worker` threads, `process.umask(mask)` will throw an exception.

### `process.unref(maybeRefable)`

Stability: 1 - Experimental

- `maybeRefable` `<any>` An object that may be "unref'd".

An object is "unrefable" if it implements the Node.js "Refable protocol". Specifically, this means that the object implements the `Symbol.for('nodejs.ref')` and `Symbol.for('nodejs.unref')` methods. "Ref'd" objects will keep the Node.js event loop alive, while "unref'd" objects will not. Historically, this was implemented by using `ref()` and `unref()` methods directly on the objects. This pattern, however, is being deprecated in favor of the "Refable protocol" in order to better support Web Platform API types whose APIs cannot be modified to add `ref()` and `unref()` methods but still need to support that behavior.

### `process.uptime()`

- Returns: `<number>`

The `process.uptime()` method returns the number of seconds the current Node.js process has been running.

The return value includes fractions of a second. Use `Math.floor()` to get whole seconds.

### `process.version`

- Type: `<string>`

The `process.version` property contains the Node.js version string.import { version } from 'node:process'; console.log(`Version: ${version}`); // Version: v14.8.0const { version } = require('node:process'); console.log(`Version: ${version}`); // Version: v14.8.0

To get the version string without the prepended *v*, use `process.versions.node`.

### `process.versions`

- Type: `<Object>`

The `process.versions` property returns an object listing the version strings of Node.js and its dependencies. `process.versions.modules` indicates the current ABI version, which is increased whenever a C++ API changes. Node.js will refuse to load modules that were compiled against a different module ABI version.`import { versions } from 'node:process'; console.log(versions);``const { versions } = require('node:process'); console.log(versions);`

Will generate an object similar to:`{ node: '26.0.0-pre', acorn: '8.15.0', ada: '3.4.1', amaro: '1.1.5', ares: '1.34.6', brotli: '1.2.0', merve: '1.0.0', cldr: '48.0', icu: '78.2', llhttp: '9.3.0', modules: '144', napi: '10', nbytes: '0.1.1', ncrypto: '0.0.1', nghttp2: '1.68.0', nghttp3: '', ngtcp2: '', openssl: '3.5.4', simdjson: '4.2.4', simdutf: '7.3.3', sqlite: '3.51.2', tz: '2025c', undici: '7.18.2', unicode: '17.0', uv: '1.51.0', uvwasi: '0.0.23', v8: '14.3.127.18-node.10', zlib: '1.3.1-e00f703', zstd: '1.5.7' }`

### Exit codes

Node.js will normally exit with a `0` status code when no more async operations are pending. The following status codes are used in other cases: `1` **Uncaught Fatal Exception**: There was an uncaught exception, and it was not handled by a domain or an `'uncaughtException'` event handler. `2`: Unused (reserved by Bash for builtin misuse) `3` **Internal JavaScript Parse Error**: The JavaScript source code internal in the Node.js bootstrapping process caused a parse error. This is extremely rare, and generally can only happen during development of Node.js itself. `4` **Internal JavaScript Evaluation Failure**: The JavaScript source code internal in the Node.js bootstrapping process failed to return a function value when evaluated. This is extremely rare, and generally can only happen during development of Node.js itself. `5` **Fatal Error**: There was a fatal unrecoverable error in V8. Typically a message will be printed to stderr with the prefix `FATAL ERROR`. `6` **Non-function Internal Exception Handler**: There was an uncaught exception, but the internal fatal exception handler function was somehow set to a non-function, and could not be called. `7` **Internal Exception Handler Run-Time Failure**: There was an uncaught exception, and the internal fatal exception handler function itself threw an error while attempting to handle it. This can happen, for example, if an `'uncaughtException'` or `domain.on('error')` handler throws an error. `8`: Unused. In previous versions of Node.js, exit code 8 sometimes indicated an uncaught exception. `9` **Invalid Argument**: Either an unknown option was specified, or an option requiring a value was provided without a value. `10` **Internal JavaScript Run-Time Failure**: The JavaScript source code internal in the Node.js bootstrapping process threw an error when the bootstrapping function was called. This is extremely rare, and generally can only happen during development of Node.js itself. `12` **Invalid Debug Argument**: The `--inspect` and/or `--inspect-brk` options were set, but the port number chosen was invalid or unavailable. `13` **Unsettled Top-Level Await**: `await` was used outside of a function in the top-level code, but the passed `Promise` never settled. `14` **Snapshot Failure**: Node.js was started to build a V8 startup snapshot and it failed because certain requirements of the state of the application were not met. `>128` **Signal Exits**: If Node.js receives a fatal signal such as `SIGKILL` or `SIGHUP`, then its exit code will be `128` plus the value of the signal code. This is a standard POSIX practice, since exit codes are defined to be 7-bit integers, and signal exits set the high-order bit, and then contain the value of the signal code. For example, signal `SIGABRT` has value `6`, so the expected exit code will be `128` + `6`, or `134`.
