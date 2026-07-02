---
title: "File system (part 1/3)"
source: https://nodejs.org/api/fs.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 1/3
---

# File system

Node.js

# Node.js v26.4.0 documentation

- Node.js v26.4.0
- Table of contents
- IndexIndex
- Other versions26.x 25.x 24.x **LTS**23.x 22.x **LTS**21.x 20.x 19.x 18.x 17.x 16.x 15.x 14.x 13.x 12.x 11.x 10.x 9.x 8.x 7.x 6.x 5.x 4.x 0.12.x 0.10.x
- Options View on single page View as JSON

## File system

Stability: 2 - Stable

The `node:fs` module enables interacting with the file system in a way modeled on standard POSIX functions.To use the promise-based APIs:`import * as fs from 'node:fs/promises';``const fs = require('node:fs/promises');`To use the callback and sync APIs:`import * as fs from 'node:fs';``const fs = require('node:fs');`All file system operations have synchronous, callback, and promise-based forms, and are accessible using both CommonJS syntax and ES6 Modules (ESM).

### Promise example

Promise-based operations return a promise that is fulfilled when the asynchronous operation is complete.`import { unlink } from 'node:fs/promises'; try { await unlink('/tmp/hello'); console.log('successfully deleted /tmp/hello'); } catch (error) { console.error('there was an error:', error.message); }`const { unlink } = require('node:fs/promises'); (async function(path) { try { await unlink(path); console.log(`successfully deleted ${path}`); } catch (error) { console.error('there was an error:', error.message); } })('/tmp/hello');

### Callback example

The callback form takes a completion callback function as its last argument and invokes the operation asynchronously. The arguments passed to the completion callback depend on the method, but the first argument is always reserved for an exception. If the operation is completed successfully, then the first argument is `null` or `undefined`.`import { unlink } from 'node:fs'; unlink('/tmp/hello', (err) => { if (err) throw err; console.log('successfully deleted /tmp/hello'); });``const { unlink } = require('node:fs'); unlink('/tmp/hello', (err) => { if (err) throw err; console.log('successfully deleted /tmp/hello'); });`The callback-based versions of the `node:fs` module APIs are preferable over the use of the promise APIs when maximal performance (both in terms of execution time and memory allocation) is required.

### Synchronous example

The synchronous APIs block the Node.js event loop and further JavaScript execution until the operation is complete. Exceptions are thrown immediately and can be handled using `try…catch`, or can be allowed to bubble up.`import { unlinkSync } from 'node:fs'; try { unlinkSync('/tmp/hello'); console.log('successfully deleted /tmp/hello'); } catch (err) { // handle the error }``const { unlinkSync } = require('node:fs'); try { unlinkSync('/tmp/hello'); console.log('successfully deleted /tmp/hello'); } catch (err) { // handle the error }`

### Promises API

The `fs/promises` API provides asynchronous file system methods that return promises.The promise APIs use the underlying Node.js threadpool to perform file system operations off the event loop thread. These operations are not synchronized or threadsafe. Care must be taken when performing multiple concurrent modifications on the same file or data corruption may occur.

#### Class: `FileHandle`

A `<FileHandle>` object is an object wrapper for a numeric file descriptor.Instances of the `<FileHandle>` object are created by the `fsPromises.open()` method.All `<FileHandle>` objects are `<EventEmitter>`s.If a `<FileHandle>` is not closed using the `filehandle.close()` method, it will try to automatically close the file descriptor and emit a process warning, helping to prevent memory leaks. Please do not rely on this behavior because it can be unreliable and the file may not be closed. Instead, always explicitly close `<FileHandle>`s. Node.js may change this behavior in the future.

##### Event: `'close'`

The `'close'` event is emitted when the `<FileHandle>` has been closed and can no longer be used.

##### `filehandle.appendFile(data[, options])`

- `data` `<string>` | `<Buffer>` | `<TypedArray>` | `<DataView>` | `<AsyncIterable>` | `<Iterable>` | `<Stream>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `signal` `<AbortSignal>` | `<undefined>` allows aborting an in-progress writeFile. **Default:** `undefined`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Alias of `filehandle.writeFile()`.When operating on file handles, the mode cannot be changed from what it was set to with `fsPromises.open()`. Therefore, this is equivalent to `filehandle.writeFile()`.

##### `filehandle.chmod(mode)`

- `mode` `<integer>` the file mode bit mask.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Modifies the permissions on the file. See `chmod(2)`.

##### `filehandle.chown(uid, gid)`

- `uid` `<integer>` The file's new owner's user id.
- `gid` `<integer>` The file's new group's group id.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the ownership of the file. A wrapper for `chown(2)`.

##### `filehandle.close()`

- Returns: `<Promise>` Fulfills with `undefined` upon success.

Closes the file handle after waiting for any pending operation on the handle to complete.`import { open } from 'node:fs/promises'; let filehandle; try { filehandle = await open('thefile.txt', 'r'); } finally { await filehandle?.close(); }`

##### `filehandle.createReadStream([options])`

- `options` `<Object>`
  - `encoding` `<string>` **Default:** `null`
  - `autoClose` `<boolean>` **Default:** `true`
  - `emitClose` `<boolean>` **Default:** `true`
  - `start` `<integer>`
  - `end` `<integer>` **Default:** `Infinity`
  - `highWaterMark` `<integer>` **Default:** `64 * 1024`
  - `signal` `<AbortSignal>` | `<undefined>` **Default:** `undefined`
- Returns: `<fs.ReadStream>`

`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the [0, `Number.MAX_SAFE_INTEGER`] range. If `start` is omitted or `undefined`, `filehandle.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by `<Buffer>`.If the `FileHandle` points to a character device that only supports blocking reads (such as keyboard or sound card), read operations do not finish until data is available. This can prevent the process from exiting and the stream from closing naturally.By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.`import { open } from 'node:fs/promises'; const fd = await open('/dev/input/event0'); // Create a stream from some character device. const stream = fd.createReadStream(); setTimeout(() => { stream.close(); // This may not close the stream. // Artificially marking end-of-stream, as if the underlying resource had // indicated end-of-file by itself, allows the stream to close. // This does not cancel pending read operations, and if there is such an // operation, the process may still not be able to exit successfully // until it finishes. stream.push(null); stream.read(0); }, 100);`If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak. If `autoClose` is set to true (default behavior), on `'error'` or `'end'` the file descriptor will be closed automatically.An example to read the last 10 bytes of a file which is 100 bytes long:`import { open } from 'node:fs/promises'; const fd = await open('sample.txt'); fd.createReadStream({ start: 90, end: 99 });`

##### `filehandle.createWriteStream([options])`

- `options` `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
  - `autoClose` `<boolean>` **Default:** `true`
  - `emitClose` `<boolean>` **Default:** `true`
  - `start` `<integer>`
  - `highWaterMark` `<number>` **Default:** `16384`
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
- Returns: `<fs.WriteStream>`

`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the [0, `Number.MAX_SAFE_INTEGER`] range. Modifying a file rather than replacing it may require the `flags` `open` option to be set to `r+` rather than the default `r`. The `encoding` can be any one of those accepted by `<Buffer>`.If `autoClose` is set to true (default behavior) on `'error'` or `'finish'` the file descriptor will be closed automatically. If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak.By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.

##### `filehandle.datasync()`

- Returns: `<Promise>` Fulfills with `undefined` upon success.

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX `fdatasync(2)` documentation for details.Unlike `filehandle.sync` this method does not flush modified metadata.

##### `filehandle.fd`

- Type: `<number>` The numeric file descriptor managed by the `<FileHandle>` object.

##### `filehandle.pull([...transforms][, options])`

Stability: 1 - Experimental

- `...transforms` `<Function>` | `<Object>` Optional transforms to apply via `stream/iter pull()`.
- `options` `<Object>`
  - `signal` `<AbortSignal>`
  - `autoClose` `<boolean>` Close the file handle when the stream ends. **Default:** `false`.
  - `start` `<number>` Byte offset to begin reading from. When specified, reads use explicit positioning (`pread` semantics). **Default:** current file position.
  - `limit` `<number>` Maximum number of bytes to read before ending the iterator. Reads stop when `limit` bytes have been delivered or EOF is reached, whichever comes first. **Default:** read until EOF.
  - `chunkSize` `<number>` Size in bytes of the buffer allocated for each read operation. **Default:** `131072` (128 KB).
- Returns: `<AsyncIterable>`<`<Uint8Array>`[]>

Return the file contents as an async iterable using the `node:stream/iter` pull model. Reads are performed in `chunkSize`-byte chunks (default 128 KB). If transforms are provided, they are applied via `stream/iter pull()`.The file handle is locked while the iterable is being consumed and unlocked when iteration completes, an error occurs, or the consumer breaks.This function is only available when the `--experimental-stream-iter` flag is enabled.`import { open } from 'node:fs/promises'; import { text } from 'node:stream/iter'; import { compressGzip } from 'node:zlib/iter'; const fh = await open('input.txt', 'r'); // Read as text console.log(await text(fh.pull({ autoClose: true }))); // Read 1 KB starting at byte 100 const fh2 = await open('input.txt', 'r'); console.log(await text(fh2.pull({ start: 100, limit: 1024, autoClose: true }))); // Read with compression const fh3 = await open('input.txt', 'r'); const compressed = fh3.pull(compressGzip(), { autoClose: true });``const { open } = require('node:fs/promises'); const { text } = require('node:stream/iter'); const { compressGzip } = require('node:zlib/iter'); async function run() { const fh = await open('input.txt', 'r'); // Read as text console.log(await text(fh.pull({ autoClose: true }))); // Read 1 KB starting at byte 100 const fh2 = await open('input.txt', 'r'); console.log(await text(fh2.pull({ start: 100, limit: 1024, autoClose: true }))); // Read with compression const fh3 = await open('input.txt', 'r'); const compressed = fh3.pull(compressGzip(), { autoClose: true }); } run().catch(console.error);`

##### `filehandle.pullSync([...transforms][, options])`

Stability: 1 - Experimental

- `...transforms` `<Function>` | `<Object>` Optional transforms to apply via `stream/iter pullSync()`.
- `options` `<Object>`
  - `autoClose` `<boolean>` Close the file handle when the stream ends. **Default:** `false`.
  - `start` `<number>` Byte offset to begin reading from. When specified, reads use explicit positioning. **Default:** current file position.
  - `limit` `<number>` Maximum number of bytes to read before ending the iterator. **Default:** read until EOF.
  - `chunkSize` `<number>` Size in bytes of the buffer allocated for each read operation. **Default:** `131072` (128 KB).
- Returns: `<Iterable>`<`<Uint8Array>`[]>

Synchronous counterpart of `filehandle.pull()`. Returns a sync iterable that reads the file using synchronous I/O on the main thread. Reads are performed in `chunkSize`-byte chunks (default 128 KB).The file handle is locked while the iterable is being consumed. Unlike the async `pull()`, this method does not support `AbortSignal` since all operations are synchronous.This function is only available when the `--experimental-stream-iter` flag is enabled.`import { open } from 'node:fs/promises'; import { textSync, pipeToSync } from 'node:stream/iter'; import { compressGzipSync, decompressGzipSync } from 'node:zlib/iter'; const fh = await open('input.txt', 'r'); // Read as text (sync) console.log(textSync(fh.pullSync({ autoClose: true }))); // Sync compress pipeline: file -> gzip -> file const src = await open('input.txt', 'r'); const dst = await open('output.gz', 'w'); pipeToSync(src.pullSync(compressGzipSync(), { autoClose: true }), dst.writer({ autoClose: true }));``const { open } = require('node:fs/promises'); const { textSync, pipeToSync } = require('node:stream/iter'); const { compressGzipSync, decompressGzipSync } = require('node:zlib/iter'); async function run() { const fh = await open('input.txt', 'r'); // Read as text (sync) console.log(textSync(fh.pullSync({ autoClose: true }))); // Sync compress pipeline: file -> gzip -> file const src = await open('input.txt', 'r'); const dst = await open('output.gz', 'w'); pipeToSync( src.pullSync(compressGzipSync(), { autoClose: true }), dst.writer({ autoClose: true }), ); } run().catch(console.error);`

##### `filehandle.read(buffer, offset, length, position)`

- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A buffer that will be filled with the file data read.
- `offset` `<integer>` The location in the buffer at which to start filling. **Default:** `0`
- `length` `<integer>` The number of bytes to read. **Default:** `buffer.byteLength - offset`
- `position` `<integer>` | `<bigint>` | `<null>` The location where to begin reading data from the file. If `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:** `null`
- Returns: `<Promise>` Fulfills upon success with an object with two properties:
  - `bytesRead` `<integer>` The number of bytes read
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A reference to the passed in `buffer` argument.

Reads data from the file and stores that in the given buffer.If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.

##### `filehandle.read([options])`

- `options` `<Object>`
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A buffer that will be filled with the file data read. **Default:** `Buffer.alloc(16384)`
  - `offset` `<integer>` The location in the buffer at which to start filling. **Default:** `0`
  - `length` `<integer>` The number of bytes to read. **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` | `<null>` The location where to begin reading data from the file. If `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:**: `null`
- Returns: `<Promise>` Fulfills upon success with an object with two properties:
  - `bytesRead` `<integer>` The number of bytes read
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A reference to the passed in `buffer` argument.

Reads data from the file and stores that in the given buffer.If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.

##### `filehandle.read(buffer[, options])`

- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A buffer that will be filled with the file data read.
- `options` `<Object>`
  - `offset` `<integer>` The location in the buffer at which to start filling. **Default:** `0`
  - `length` `<integer>` The number of bytes to read. **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` | `<null>` The location where to begin reading data from the file. If `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:**: `null`
- Returns: `<Promise>` Fulfills upon success with an object with two properties:
  - `bytesRead` `<integer>` The number of bytes read
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` A reference to the passed in `buffer` argument.

Reads data from the file and stores that in the given buffer.If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.

##### `filehandle.readableWebStream([options])`

- `options` `<Object>`
  - `autoClose` `<boolean>` When true, causes the `<FileHandle>` to be closed when the stream is closed. **Default:** `false`
- Returns: `<ReadableStream>`

Returns a byte-oriented `ReadableStream` that may be used to read the file's contents.An error will be thrown if this method is called more than once or is called after the `FileHandle` is closed or closing.`import { open, } from 'node:fs/promises'; const file = await open('./some/file/to/read'); for await (const chunk of file.readableWebStream()) console.log(chunk); await file.close();``const { open, } = require('node:fs/promises'); (async () => { const file = await open('./some/file/to/read'); for await (const chunk of file.readableWebStream()) console.log(chunk); await file.close(); })();`While the `ReadableStream` will read the file to completion, it will not close the `FileHandle` automatically. User code must still call the `fileHandle.close()` method unless the `autoClose` option is set to `true`.

##### `filehandle.readFile(options)`

- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `null`
  - `signal` `<AbortSignal>` allows aborting an in-progress readFile
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<Function>` A buffer to read into, or a function called with the file size that returns the buffer.
- Returns: `<Promise>` Fulfills upon a successful read with the contents of the file. If no encoding is specified (using `options.encoding`), the data is returned as a `<Buffer>` object. Otherwise, the data will be a string.

Asynchronously reads the entire contents of a file.If `options` is a string, then it specifies the `encoding`.If `buffer` is provided and no encoding is specified, the returned `<Buffer>` is a view over the supplied buffer containing only the bytes read. If the supplied buffer is too small to contain the entire file, the operation will fail.The `<FileHandle>` has to support reading.If one or more `filehandle.read()` calls are made on a file handle and then a `filehandle.readFile()` call is made, the data will be read from the current position till the end of the file. It doesn't always read from the beginning of the file.An example using the `buffer` option with a pre-allocated buffer:import { Buffer } from 'node:buffer'; import { open } from 'node:fs/promises'; const file = await open('./some/file/to/read'); try { const buf = Buffer.alloc(16384); const contents = await file.readFile({ buffer: buf }); console.log(contents); // A view over `buf` containing only the bytes read } finally { await file.close(); }An example using the `buffer` option with a function returning a buffer:`import { Buffer } from 'node:buffer'; import { open } from 'node:fs/promises'; const file = await open('./some/file/to/read'); try { const contents = await file.readFile({ buffer: (size) => Buffer.alloc(size), }); console.log(contents); } finally { await file.close(); }`

##### `filehandle.readLines([options])`

- `options` `<Object>`
  - `encoding` `<string>` **Default:** `null`
  - `autoClose` `<boolean>` **Default:** `true`
  - `emitClose` `<boolean>` **Default:** `true`
  - `start` `<integer>`
  - `end` `<integer>` **Default:** `Infinity`
  - `highWaterMark` `<integer>` **Default:** `64 * 1024`
- Returns: `<readline.InterfaceConstructor>`

Convenience method to create a `readline` interface and stream over the file. See `filehandle.createReadStream()` for the options.`import { open } from 'node:fs/promises'; const file = await open('./some/file/to/read'); for await (const line of file.readLines()) { console.log(line); }``const { open } = require('node:fs/promises'); (async () => { const file = await open('./some/file/to/read'); for await (const line of file.readLines()) { console.log(line); } })();`

##### `filehandle.readv(buffers[, position])`

- `buffers` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[]
- `position` `<integer>` | `<null>` The offset from the beginning of the file where the data should be read from. If `position` is not a `number`, the data will be read from the current position. **Default:** `null`
- Returns: `<Promise>` Fulfills upon success an object containing two properties:
  - `bytesRead` `<integer>` the number of bytes read
  - `buffers` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[] property containing a reference to the `buffers` input.

Read from a file and write to an array of {ArrayBufferView}s

##### `filehandle.stat([options])`

- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
  - `signal` `<AbortSignal>` An AbortSignal to cancel the operation. **Default:** `undefined`.
- Returns: `<Promise>` Fulfills with an `<fs.Stats>` for the file.

##### `filehandle.sync()`

- Returns: `<Promise>` Fulfills with `undefined` upon success.

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX `fsync(2)` documentation for more detail.

##### `filehandle.truncate(len)`

- `len` `<integer>` **Default:** `0`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Truncates the file.If the file was larger than `len` bytes, only the first `len` bytes will be retained in the file.The following example retains only the first four bytes of the file:`import { open } from 'node:fs/promises'; let filehandle = null; try { filehandle = await open('temp.txt', 'r+'); await filehandle.truncate(4); } finally { await filehandle?.close(); }`If the file previously was shorter than `len` bytes, it is extended, and the extended part is filled with null bytes (`'\0'`):If `len` is negative then `0` will be used.

##### `filehandle.utimes(atime, mtime)`

- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- Returns: `<Promise>`

Change the file system timestamps of the object referenced by the `<FileHandle>` then fulfills the promise with no arguments upon success.

##### `filehandle.write(buffer, offset[, length[, position]])`

- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `offset` `<integer>` The start position from within `buffer` where the data to write begins.
- `length` `<integer>` The number of bytes from `buffer` to write. **Default:** `buffer.byteLength - offset`
- `position` `<integer>` | `<null>` The offset from the beginning of the file where the data from `buffer` should be written. If `position` is not a `number`, the data will be written at the current position. See the POSIX `pwrite(2)` documentation for more detail. **Default:** `null`
- Returns: `<Promise>`

Write `buffer` to the file.The promise is fulfilled with an object containing two properties: `bytesWritten` `<integer>` the number of bytes written `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` a reference to the `buffer` written. It is unsafe to use `filehandle.write()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected). For this scenario, use `filehandle.createWriteStream()`.On Linux, positional writes do not work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

##### `filehandle.write(buffer[, options])`

- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<null>` **Default:** `null`
- Returns: `<Promise>`

Write `buffer` to the file.Similar to the above `filehandle.write` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

##### `filehandle.write(string[, position[, encoding]])`

- `string` `<string>`
- `position` `<integer>` | `<null>` The offset from the beginning of the file where the data from `string` should be written. If `position` is not a `number` the data will be written at the current position. See the POSIX `pwrite(2)` documentation for more detail. **Default:** `null`
- `encoding` `<string>` The expected string encoding. **Default:** `'utf8'`
- Returns: `<Promise>`

Write `string` to the file. If `string` is not a string, the promise is rejected with an error.The promise is fulfilled with an object containing two properties: `bytesWritten` `<integer>` the number of bytes written `buffer` `<string>` a reference to the `string` written. It is unsafe to use `filehandle.write()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected). For this scenario, use `filehandle.createWriteStream()`.On Linux, positional writes do not work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

##### `filehandle.writeFile(data, options)`

- `data` `<string>` | `<Buffer>` | `<TypedArray>` | `<DataView>` | `<AsyncIterable>` | `<Iterable>` | `<Stream>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` The expected character encoding when `data` is a string. **Default:** `'utf8'`
  - `signal` `<AbortSignal>` | `<undefined>` allows aborting an in-progress writeFile. **Default:** `undefined`
- Returns: `<Promise>`

Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an `<AsyncIterable>`, or an {Iterable} object. The promise is fulfilled with no arguments upon success.If `options` is a string, then it specifies the `encoding`.The `<FileHandle>` has to support writing.It is unsafe to use `filehandle.writeFile()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected).If one or more `filehandle.write()` calls are made on a file handle and then a `filehandle.writeFile()` call is made, the data will be written from the current position till the end of the file. It doesn't always write from the beginning of the file.

##### `filehandle.writev(buffers[, position])`

- `buffers` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[]
- `position` `<integer>` | `<null>` The offset from the beginning of the file where the data from `buffers` should be written. If `position` is not a `number`, the data will be written at the current position. **Default:** `null`
- Returns: `<Promise>`

Write an array of {ArrayBufferView}s to the file.The promise is fulfilled with an object containing a two properties: `bytesWritten` `<integer>` the number of bytes written `buffers` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[] a reference to the `buffers` input. It is unsafe to call `writev()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected).On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

##### `filehandle.writer([options])`

Stability: 1 - Experimental

- `options` `<Object>`
  - `autoClose` `<boolean>` Close the file handle when the writer ends or fails. **Default:** `false`.
  - `start` `<number>` Byte offset to start writing at. When specified, writes use explicit positioning. **Default:** current file position.
  - `limit` `<number>` Maximum number of bytes the writer will accept. Async writes (`write()`, `writev()`) that would exceed the limit reject with `ERR_OUT_OF_RANGE`. Sync writes (`writeSync()`, `writevSync()`) return `false`. **Default:** no limit.
  - `chunkSize` `<number>` Maximum chunk size in bytes for synchronous write operations. Writes larger than this threshold fall back to async I/O. Set this to match the reader's `chunkSize` for optimal `pipeTo()` performance. **Default:** `131072` (128 KB).
- Returns: `<Object>`
  - `write(chunk[, options])` `<Function>` Returns `<Promise>`. Accepts `Uint8Array`, `Buffer`, or string (UTF-8 encoded).
    - `chunk` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<string>`
    - `options` `<Object>`
      - `signal` `<AbortSignal>` If the signal is already aborted, the write rejects with `AbortError` without performing I/O.
  - `writev(chunks[, options])` `<Function>` Returns `<Promise>`. Uses scatter/gather I/O via a single `writev()` syscall. Accepts mixed `Uint8Array`/string arrays.
    - `chunks` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[] | `<string>`[]
    - `options` `<Object>`
      - `signal` `<AbortSignal>` If the signal is already aborted, the write rejects with `AbortError` without performing I/O.
  - `writeSync(chunk)` `<Function>` Returns `<boolean>`. Attempts a synchronous write. Returns `true` if the write succeeded, `false` if the caller should fall back to async `write()`. Returns `false` when: the writer is closed/errored, an async operation is in flight, the chunk exceeds `chunkSize`, or the write would exceed `limit`.
    - `chunk` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<string>`
  - `writevSync(chunks)` `<Function>` Returns `<boolean>`. Synchronous batch write. Same fallback semantics as `writeSync()`.
    - `chunks` `<Buffer>`[] | `<TypedArray>`[] | `<DataView>`[] | `<string>`[]
  - `end([options])` `<Function>` Returns `<Promise>`, fulfills with the total number of bytes written. Idempotent: returns `totalBytesWritten` if already closed, returns the pending promise if already closing. Rejects if the writer is in an errored state.
    - `options` `<Object>`
      - `signal` `<AbortSignal>` If the signal is already aborted, `end()` rejects with `AbortError` and the writer remains open.
  - `endSync()` `<Function>` Returns `<number>` | `<number>` total bytes written on success, `-1` if the writer is errored or an async operation is in flight. Idempotent when already closed.
  - `fail(reason)` `<Function>` Puts the writer into a terminal error state. Synchronous. If the writer is already closed or errored, this is a no-op. If `autoClose` is true, closes the file handle synchronously.

Return a `node:stream/iter` writer backed by this file handle.The writer supports both `Symbol.asyncDispose` and `Symbol.dispose`: `await using w = fh.writer()` — if the writer is still open (no `end()` called), `asyncDispose` calls `fail()`. If `end()` is pending, it waits for it to complete. `using w = fh.writer()` — calls `fail()` unconditionally. The `writeSync()` and `writevSync()` methods enable the try-sync fast path used by `stream/iter pipeTo()`. When the reader's chunk size matches the writer's `chunkSize`, all writes in a `pipeTo()` pipeline complete synchronously with zero promise overhead.This function is only available when the `--experimental-stream-iter` flag is enabled.`import { open } from 'node:fs/promises'; import { from, pipeTo } from 'node:stream/iter'; import { compressGzip } from 'node:zlib/iter'; // Async pipeline const fh = await open('output.gz', 'w'); await pipeTo(from('Hello!'), compressGzip(), fh.writer({ autoClose: true })); // Sync pipeline with limit const src = await open('input.txt', 'r'); const dst = await open('output.txt', 'w'); const w = dst.writer({ limit: 1024 * 1024 }); // Max 1 MB await pipeTo(src.pull({ autoClose: true }), w); await w.end(); await dst.close();``const { open } = require('node:fs/promises'); const { from, pipeTo } = require('node:stream/iter'); const { compressGzip } = require('node:zlib/iter'); async function run() { // Async pipeline const fh = await open('output.gz', 'w'); await pipeTo(from('Hello!'), compressGzip(), fh.writer({ autoClose: true })); // Sync pipeline with limit const src = await open('input.txt', 'r'); const dst = await open('output.txt', 'w'); const w = dst.writer({ limit: 1024 * 1024 }); // Max 1 MB await pipeTo(src.pull({ autoClose: true }), w); await w.end(); await dst.close(); } run().catch(console.error);`

##### `filehandle[Symbol.asyncDispose]()`

Calls `filehandle.close()` and returns a promise that fulfills when the filehandle is closed.

#### `fsPromises.access(path[, mode])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>` **Default:** `fs.constants.F_OK`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check File access constants for possible values of `mode`.If the accessibility check is successful, the promise is fulfilled with no value. If any of the accessibility checks fail, the promise is rejected with an `<Error>` object. The following example checks if the file `/etc/passwd` can be read and written by the current process.`import { access, constants } from 'node:fs/promises'; try { await access('/etc/passwd', constants.R_OK | constants.W_OK); console.log('can access'); } catch { console.error('cannot access'); }`Using `fsPromises.access()` to check for the accessibility of a file before calling `fsPromises.open()` is not recommended. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file is not accessible.

#### `fsPromises.appendFile(path, data[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<FileHandle>` filename or `<FileHandle>`
- `data` `<string>` | `<Buffer>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'a'`.
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `<Buffer>`.If `options` is a string, then it specifies the `encoding`.The `mode` option only affects the newly created file. See `fs.open()` for more details.The `path` may be specified as a `<FileHandle>` that has been opened for appending (using `fsPromises.open()`).

#### `fsPromises.chmod(path, mode)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<string>` | `<integer>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the permissions of a file.

#### `fsPromises.chown(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the ownership of a file.

#### `fsPromises.copyFile(src, dest[, mode])`

- `src` `<string>` | `<Buffer>` | `<URL>` source filename to copy
- `dest` `<string>` | `<Buffer>` | `<URL>` destination filename of the copy operation
- `mode` `<integer>` Optional modifiers that specify the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`) **Default:** `0`.
  - `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists.
  - `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used.
  - `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists.No guarantees are made about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, an attempt will be made to remove the destination.`import { copyFile, constants } from 'node:fs/promises'; try { await copyFile('source.txt', 'destination.txt'); console.log('source.txt was copied to destination.txt'); } catch { console.error('The file could not be copied'); } // By using COPYFILE_EXCL, the operation will fail if destination.txt exists. try { await copyFile('source.txt', 'destination.txt', constants.COPYFILE_EXCL); console.log('source.txt was copied to destination.txt'); } catch { console.error('The file could not be copied'); }`

#### `fsPromises.cp(src, dest[, options])`

- `src` `<string>` | `<URL>` source path to copy.
- `dest` `<string>` | `<URL>` destination path to copy to.
- `options` `<Object>`
  - `dereference` `<boolean>` dereference symlinks. **Default:** `false`.
  - `errorOnExist` `<boolean>` when `force` is `false`, and the destination exists, throw an error. **Default:** `false`.
  - `filter` `<Function>` Function to filter copied files/directories. Return `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. Can also return a `Promise` that resolves to `true` or `false` **Default:** `undefined`.
    - `src` `<string>` source path to copy.
    - `dest` `<string>` destination path to copy to.
    - Returns: `<boolean>` | `<Promise>` A value that is coercible to `boolean` or a `Promise` that fulfils with such value.
  - `force` `<boolean>` overwrite existing file or directory. The copy operation will ignore errors if you set this to false and the destination exists. Use the `errorOnExist` option to change this behavior. **Default:** `true`.
  - `mode` `<integer>` modifiers for copy operation. **Default:** `0`. See `mode` flag of `fsPromises.copyFile()`.
  - `preserveTimestamps` `<boolean>` When `true` timestamps from `src` will be preserved. **Default:** `false`.
  - `recursive` `<boolean>` copy directories recursively **Default:** `false`
  - `verbatimSymlinks` `<boolean>` When `true`, path resolution for symlinks will be skipped. **Default:** `false`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.

#### `fsPromises.glob(pattern[, options])`

- `pattern` `<string>` | `<string>`[]
- `options` `<Object>`
  - `cwd` `<string>` | `<URL>` current working directory. **Default:** `process.cwd()`
  - `exclude` `<Function>` | `<string>`[] Function to filter out files/directories or a list of glob patterns to be excluded. If a function is provided, return `true` to exclude the item, `false` to include it. **Default:** `undefined`. If a string array is provided, each string should be a glob pattern that specifies paths to exclude. Note: Negation patterns (e.g., '!foo.js') are not supported.
  - `followSymlinks` `<boolean>` When `true`, symbolic links to directories are followed while expanding `**` patterns. **Default:** `false`.
  - `withFileTypes` `<boolean>` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
- Returns: `<AsyncIterator>` An AsyncIterator that yields the paths of files that match the pattern.

When `followSymlinks` is enabled, detected symbolic link cycles are not traversed recursively.`import { glob } from 'node:fs/promises'; for await (const entry of glob('**/*.js')) console.log(entry);``const { glob } = require('node:fs/promises'); (async () => { for await (const entry of glob('**/*.js')) console.log(entry); })();`

#### `fsPromises.lchmod(path, mode)`

Stability: 0 - Deprecated

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the permissions on a symbolic link.This method is only implemented on macOS.

#### `fsPromises.lchown(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the ownership on a symbolic link.

#### `fsPromises.lutimes(path, atime, mtime)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Changes the access and modification times of a file in the same way as `fsPromises.utimes()`, with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

#### `fsPromises.link(existingPath, newPath)`

- `existingPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Creates a new link from the `existingPath` to the `newPath`. See the POSIX `link(2)` documentation for more detail.

#### `fsPromises.lstat(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
- Returns: `<Promise>` Fulfills with the `<fs.Stats>` object for the given symbolic link `path`.

Equivalent to `fsPromises.stat()` unless `path` refers to a symbolic link, in which case the link itself is stat-ed, not the file that it refers to. Refer to the POSIX `lstat(2)` document for more detail.

#### `fsPromises.mkdir(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` | `<integer>`
  - `recursive` `<boolean>` **Default:** `false`
  - `mode` `<string>` | `<integer>` Not supported on Windows. See File modes for more details. **Default:** `0o777`.
- Returns: `<Promise>` Upon success, fulfills with `undefined` if `recursive` is `false`, or the first directory path created if `recursive` is `true`.

Asynchronously creates a directory.The optional `options` argument can be an integer specifying `mode` (permission and sticky bits), or an object with a `mode` property and a `recursive` property indicating whether parent directories should be created. Calling `fsPromises.mkdir()` when `path` is a directory that exists results in a rejection only when `recursive` is false.import { mkdir } from 'node:fs/promises'; try { const projectFolder = new URL('./test/project/', import.meta.url); const createDir = await mkdir(projectFolder, { recursive: true }); console.log(`created ${createDir}`); } catch (err) { console.error(err.message); }`const { mkdir } = require('node:fs/promises'); const { join } = require('node:path'); async function makeDirectory() { const projectFolder = join(__dirname, 'test', 'project'); const dirCreation = await mkdir(projectFolder, { recursive: true }); console.log(dirCreation); return dirCreation; } makeDirectory().catch(console.error);`

#### `fsPromises.mkdtemp(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Promise>` Fulfills with a string containing the file system path of the newly created temporary directory.

Creates a unique temporary directory. A unique directory name is generated by appending six random characters to the end of the provided `prefix`. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.`import { mkdtemp } from 'node:fs/promises'; import { join } from 'node:path'; import { tmpdir } from 'node:os'; try { await mkdtemp(join(tmpdir(), 'foo-')); } catch (err) { console.error(err); }`The `fsPromises.mkdtemp()` method will append the six randomly selected characters directly to the `prefix` string. For instance, given a directory `/tmp`, if the intention is to create a temporary directory *within* `/tmp`, the `prefix` must end with a trailing platform-specific path separator (`require('node:path').sep`).

#### `fsPromises.mkdtempDisposable(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Promise>` Fulfills with a Promise for an async-disposable Object:
  - `path` `<string>` The path of the created directory.
  - `remove` `<AsyncFunction>` A function which removes the created directory.
  - `[Symbol.asyncDispose]` `<AsyncFunction>` The same as `remove`.

The resulting Promise holds an async-disposable object whose `path` property holds the created directory path. When the object is disposed, the directory and its contents will be removed asynchronously if it still exists. If the directory cannot be deleted, disposal will throw an error. The object has an async `remove()` method which will perform the same task.Both this function and the disposal function on the resulting object are async, so it should be used with `await` + `await using` as in `await using dir = await fsPromises.mkdtempDisposable('prefix')`.For detailed information, see the documentation of `fsPromises.mkdtemp()`.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.

#### `fsPromises.open(path, flags[, mode])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `flags` `<string>` | `<number>` See support of file system `flags`. **Default:** `'r'`.
- `mode` `<string>` | `<integer>` Sets the file mode (permission and sticky bits) if the file is created. See File modes for more details. **Default:** `0o666` (readable and writable)
- Returns: `<Promise>` Fulfills with a `<FileHandle>` object.

Opens a `<FileHandle>`.Refer to the POSIX `open(2)` documentation for more detail.Some characters (`< > : " / \ | ? *`) are reserved under Windows as documented by Naming Files, Paths, and Namespaces. Under NTFS, if the filename contains a colon, Node.js will open a file system stream, as described by this MSDN page.

#### `fsPromises.opendir(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `bufferSize` `<number>` Number of directory entries that are buffered internally when reading from the directory. Higher values lead to better performance but higher memory usage. **Default:** `32`
  - `recursive` `<boolean>` Resolved `Dir` will be an `<AsyncIterable>` containing all sub files and directories. **Default:** `false`
- Returns: `<Promise>` Fulfills with an `<fs.Dir>`.

Asynchronously open a directory for iterative scanning. See the POSIX `opendir(3)` documentation for more detail.Creates an `<fs.Dir>`, which contains all further functions for reading from and cleaning up the directory.The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.Example using async iteration:`import { opendir } from 'node:fs/promises'; try { const dir = await opendir('./'); for await (const dirent of dir) console.log(dirent.name); } catch (err) { console.error(err); }`When using the async iterator, the `<fs.Dir>` object will be automatically closed after the iterator exits.

#### `fsPromises.readdir(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
  - `withFileTypes` `<boolean>` **Default:** `false`
  - `recursive` `<boolean>` If `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files, and directories. **Default:** `false`.
- Returns: `<Promise>` Fulfills with an array of the names of the files in the directory excluding `'.'` and `'..'`.

Reads the contents of a directory.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as `<Buffer>` objects.If `options.withFileTypes` is set to `true`, the returned array will contain `<fs.Dirent>` objects.`import { readdir } from 'node:fs/promises'; try { const files = await readdir(path); for (const file of files) console.log(file); } catch (err) { console.error(err); }`

#### `fsPromises.readFile(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<FileHandle>` filename or `FileHandle`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `null`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'r'`.
  - `signal` `<AbortSignal>` allows aborting an in-progress readFile
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<Function>` A buffer to read into, or a function called with the file size that returns the buffer.
- Returns: `<Promise>` Fulfills with the contents of the file.

Asynchronously reads the entire contents of a file.If no encoding is specified (using `options.encoding`), the data is returned as a `<Buffer>` object. Otherwise, the data will be a string.If `options` is a string, then it specifies the encoding.If `buffer` is provided and no encoding is specified, the returned `<Buffer>` is a view over the supplied buffer containing only the bytes read. If the supplied buffer is too small to contain the entire file, the promise will be rejected.When the `path` is a directory, the behavior of `fsPromises.readFile()` is platform-specific. On macOS, Linux, and Windows, the promise will be rejected with an error. On FreeBSD, a representation of the directory's contents will be returned.An example of reading a `package.json` file located in the same directory of the running code:`import { readFile } from 'node:fs/promises'; try { const filePath = new URL('./package.json', import.meta.url); const contents = await readFile(filePath, { encoding: 'utf8' }); console.log(contents); } catch (err) { console.error(err.message); }``const { readFile } = require('node:fs/promises'); const { resolve } = require('node:path'); async function logFile() { try { const filePath = resolve('./package.json'); const contents = await readFile(filePath, { encoding: 'utf8' }); console.log(contents); } catch (err) { console.error(err.message); } } logFile();`It is possible to abort an ongoing `readFile` using an `<AbortSignal>`. If a request is aborted the promise returned is rejected with an `AbortError`:`import { readFile } from 'node:fs/promises'; try { const controller = new AbortController(); const { signal } = controller; const promise = readFile(fileName, { signal }); // Abort the request before the promise settles. controller.abort(); await promise; } catch (err) { // When a request is aborted - err is an AbortError console.error(err); }`Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.readFile` performs.Any specified `<FileHandle>` has to support reading.An example using the `buffer` option with a pre-allocated buffer:import { Buffer } from 'node:buffer'; import { readFile } from 'node:fs/promises'; const buf = Buffer.alloc(16384); const contents = await readFile('/path/to/file', { buffer: buf }); console.log(contents); // A view over `buf` containing only the bytes readAn example using the `buffer` option with a function returning a buffer:`import { Buffer } from 'node:buffer'; import { readFile } from 'node:fs/promises'; const contents = await readFile('/path/to/file', { buffer: (size) => Buffer.alloc(size), }); console.log(contents);`

#### `fsPromises.readlink(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Promise>` Fulfills with the `linkString` upon success.

Reads the contents of the symbolic link referred to by `path`. See the POSIX `readlink(2)` documentation for more detail. The promise is fulfilled with the `linkString` upon success.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path returned. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a `<Buffer>` object.

#### `fsPromises.realpath(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Promise>` Fulfills with the resolved path upon success.

Determines the actual location of `path` using the same semantics as the `fs.realpath.native()` function.Only paths that can be converted to UTF8 strings are supported.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path. If the `encoding` is set to `'buffer'`, the path returned will be passed as a `<Buffer>` object.On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.

#### `fsPromises.rename(oldPath, newPath)`

- `oldPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Renames `oldPath` to `newPath`.

#### `fsPromises.rmdir(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` There are currently no options exposed. There used to be options for `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Removes the directory identified by `path`.Using `fsPromises.rmdir()` on a file (not a directory) results in the promise being rejected with an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.To get a behavior similar to the `rm -rf` Unix command, use `fsPromises.rm()` with options `{ recursive: true, force: true }`.

#### `fsPromises.rm(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `force` `<boolean>` When `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
  - `maxRetries` `<integer>` If an `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
  - `recursive` `<boolean>` If `true`, perform a recursive directory removal. In recursive mode operations are retried on failure. **Default:** `false`.
  - `retryDelay` `<integer>` The amount of time in milliseconds to wait between retries. This option is ignored if the `recursive` option is not `true`. **Default:** `100`.
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Removes files and directories (modeled on the standard POSIX `rm` utility).

#### `fsPromises.stat(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
  - `throwIfNoEntry` `<boolean>` Whether an exception will be thrown if no file system entry exists, rather than returning `undefined`. **Default:** `true`.
- Returns: `<Promise>` Fulfills with the `<fs.Stats>` object for the given `path`.

#### `fsPromises.statfs(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.StatFs>` object should be `bigint`. **Default:** `false`.
- Returns: `<Promise>` Fulfills with the `<fs.StatFs>` object for the given `path`.

#### `fsPromises.symlink(target, path[, type])`

- `target` `<string>` | `<Buffer>` | `<URL>`
- `path` `<string>` | `<Buffer>` | `<URL>`
- `type` `<string>` | `<null>` **Default:** `null`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Creates a symbolic link.The `type` argument is only used on Windows platforms and can be one of `'dir'`, `'file'`, or `'junction'`. If the `type` argument is `null`, Node.js will autodetect `target` type and use `'file'` or `'dir'`. If the `target` does not exist, `'file'` will be used. Windows junction points require the destination path to be absolute. When using `'junction'`, the `target` argument will automatically be normalized to absolute path. Junction points on NTFS volumes can only point to directories.

#### `fsPromises.truncate(path[, len])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `len` `<integer>` **Default:** `0`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Truncates (shortens or extends the length) of the content at `path` to `len` bytes.

#### `fsPromises.unlink(path)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

If `path` refers to a symbolic link, then the link is removed without affecting the file or directory to which that link refers. If the `path` refers to a file path that is not a symbolic link, the file is deleted. See the POSIX `unlink(2)` documentation for more detail.

#### `fsPromises.utimes(path, atime, mtime)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Change the file system timestamps of the object referenced by `path`.The `atime` and `mtime` arguments follow these rules: Values can be either numbers representing Unix epoch time, `Date`s, or a numeric string like `'123456789.0'`. If the value can not be converted to a number, or is `NaN`, `Infinity`, or `-Infinity`, an `Error` will be thrown.

#### `fsPromises.watch(filename[, options])`

- `filename` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `persistent` `<boolean>` Indicates whether the process should continue to run as long as files are being watched. **Default:** `true`.
  - `recursive` `<boolean>` Indicates whether all subdirectories should be watched, or only the current directory. This applies when a directory is specified, and only on supported platforms (See caveats). **Default:** `false`.
  - `encoding` `<string>` Specifies the character encoding to be used for the filename passed to the listener. **Default:** `'utf8'`.
  - `signal` `<AbortSignal>` An `<AbortSignal>` used to signal when the watcher should stop.
  - `maxQueue` `<number>` Specifies the number of events to queue between iterations of the `<AsyncIterator>` returned. **Default:** `2048`.
  - `overflow` `<string>` Either `'ignore'` or `'throw'` when there are more events to be queued than `maxQueue` allows. `'ignore'` means overflow events are dropped and a warning is emitted, while `'throw'` means to throw an exception. **Default:** `'ignore'`.
  - `ignore` `<string>` | `<RegExp>` | `<Function>` | `<Array>` Pattern(s) to ignore. Strings are glob patterns (using `minimatch`), RegExp patterns are tested against the filename, and functions receive the filename and return `true` to ignore. **Default:** `undefined`.
- Returns: `<AsyncIterator>` of objects with the properties:
  - `eventType` `<string>` The type of change
  - `filename` `<string>` | `<Buffer>` | `<null>` The name of the file changed.

Returns an async iterator that watches for changes on `filename`, where `filename` is either a file or a directory.`const { watch } = require('node:fs/promises'); const ac = new AbortController(); const { signal } = ac; setTimeout(() => ac.abort(), 10000); (async () => { try { const watcher = watch(__filename, { signal }); for await (const event of watcher) console.log(event); } catch (err) { if (err.name === 'AbortError') return; throw err; } })();`On most platforms, `'rename'` is emitted whenever a filename appears or disappears in the directory.All the caveats for `fs.watch()` also apply to `fsPromises.watch()`.

#### `fsPromises.writeFile(file, data[, options])`

- `file` `<string>` | `<Buffer>` | `<URL>` | `<FileHandle>` filename or `FileHandle`
- `data` `<string>` | `<Buffer>` | `<TypedArray>` | `<DataView>` | `<AsyncIterable>` | `<Iterable>` | `<Stream>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'w'`.
  - `flush` `<boolean>` If all data is successfully written to the file, and `flush` is `true`, `filehandle.sync()` is used to flush the data. **Default:** `false`.
  - `signal` `<AbortSignal>` allows aborting an in-progress writeFile
- Returns: `<Promise>` Fulfills with `undefined` upon success.

Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an `<AsyncIterable>`, or an {Iterable} object.The `encoding` option is ignored if `data` is a buffer.If `options` is a string, then it specifies the encoding.The `mode` option only affects the newly created file. See `fs.open()` for more details.Any specified `<FileHandle>` has to support writing.It is unsafe to use `fsPromises.writeFile()` multiple times on the same file without waiting for the promise to be settled.Similarly to `fsPromises.readFile` - `fsPromises.writeFile` is a convenience method that performs multiple `write` calls internally to write the buffer passed to it. For performance sensitive code consider using `fs.createWriteStream()` or `filehandle.createWriteStream()`.It is possible to use an `<AbortSignal>` to cancel an `fsPromises.writeFile()`. Cancelation is "best effort", and some amount of data is likely still to be written.`import { writeFile } from 'node:fs/promises'; import { Buffer } from 'node:buffer'; try { const controller = new AbortController(); const { signal } = controller; const data = new Uint8Array(Buffer.from('Hello Node.js')); const promise = writeFile('message.txt', data, { signal }); // Abort the request before the promise settles. controller.abort(); await promise; } catch (err) { // When a request is aborted - err is an AbortError console.error(err); }`Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.writeFile` performs.

#### `fsPromises.constants`

- Type: `<Object>`

Returns an object containing commonly used constants for file system operations. The object is the same as `fs.constants`. See FS constants for more details.

### Callback API

The callback APIs perform all operations asynchronously, without blocking the event loop, then invoke a callback function upon completion or error.The callback APIs use the underlying Node.js threadpool to perform file system operations off the event loop thread. These operations are not synchronized or threadsafe. Care must be taken when performing multiple concurrent modifications on the same file or data corruption may occur.

#### `fs.access(path[, mode], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>` **Default:** `fs.constants.F_OK`
- `callback` `<Function>`
  - `err` `<Error>`

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check File access constants for possible values of `mode`.The final argument, `callback`, is a callback function that is invoked with a possible error argument. If any of the accessibility checks fail, the error argument will be an `Error` object. The following examples check if `package.json` exists, and if it is readable or writable.import { access, constants } from 'node:fs'; const file = 'package.json'; // Check if the file exists in the current directory. access(file, constants.F_OK, (err) => { console.log(`${file} ${err ? 'does not exist' : 'exists'}`); }); // Check if the file is readable. access(file, constants.R_OK, (err) => { console.log(`${file} ${err ? 'is not readable' : 'is readable'}`); }); // Check if the file is writable. access(file, constants.W_OK, (err) => { console.log(`${file} ${err ? 'is not writable' : 'is writable'}`); }); // Check if the file is readable and writable. access(file, constants.R_OK | constants.W_OK, (err) => { console.log(`${file} ${err ? 'is not' : 'is'} readable and writable`); });Do not use `fs.access()` to check for the accessibility of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()`. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file is not accessible.**write (NOT RECOMMENDED)**`import { access, open, close } from 'node:fs'; access('myfile', (err) => { if (!err) { console.error('myfile already exists'); return; } open('myfile', 'wx', (err, fd) => { if (err) throw err; try { writeMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } }); });`**write (RECOMMENDED)**`import { open, close } from 'node:fs'; open('myfile', 'wx', (err, fd) => { if (err) { if (err.code === 'EEXIST') { console.error('myfile already exists'); return; } throw err; } try { writeMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } });`**read (NOT RECOMMENDED)**`import { access, open, close } from 'node:fs'; access('myfile', (err) => { if (err) { if (err.code === 'ENOENT') { console.error('myfile does not exist'); return; } throw err; } open('myfile', 'r', (err, fd) => { if (err) throw err; try { readMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } }); });`**read (RECOMMENDED)**`import { open, close } from 'node:fs'; open('myfile', 'r', (err, fd) => { if (err) { if (err.code === 'ENOENT') { console.error('myfile does not exist'); return; } throw err; } try { readMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } });`The "not recommended" examples above check for accessibility and then use the file; the "recommended" examples are better because they use the file directly and handle the error, if any.In general, check for the accessibility of a file only if the file will not be used directly, for example when its accessibility is a signal from another process.On Windows, access-control policies (ACLs) on a directory may limit access to a file or directory. The `fs.access()` function, however, does not check the ACL and therefore may report that a path is accessible even if the ACL restricts the user from reading or writing to it.

#### `fs.appendFile(path, data[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<number>` filename or file descriptor
- `data` `<string>` | `<Buffer>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'a'`.
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `<Buffer>`.The `mode` option only affects the newly created file. See `fs.open()` for more details.`import { appendFile } from 'node:fs'; appendFile('message.txt', 'data to append', (err) => { if (err) throw err; console.log('The "data to append" was appended to file!'); });`If `options` is a string, then it specifies the encoding:`import { appendFile } from 'node:fs'; appendFile('message.txt', 'data to append', 'utf8', callback);`The `path` may be specified as a numeric file descriptor that has been opened for appending (using `fs.open()` or `fs.openSync()`). The file descriptor will not be closed automatically.`import { open, close, appendFile } from 'node:fs'; function closeFd(fd) { close(fd, (err) => { if (err) throw err; }); } open('message.txt', 'a', (err, fd) => { if (err) throw err; try { appendFile(fd, 'data to append', 'utf8', (err) => { closeFd(fd); if (err) throw err; }); } catch (err) { closeFd(fd); throw err; } });`

#### `fs.chmod(path, mode, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<string>` | `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously changes the permissions of a file. No arguments other than a possible exception are given to the completion callback.See the POSIX `chmod(2)` documentation for more detail.`import { chmod } from 'node:fs'; chmod('my_file.txt', 0o775, (err) => { if (err) throw err; console.log('The permissions for file "my_file.txt" have been changed!'); });`

##### File modes

The `mode` argument used in both the `fs.chmod()` and `fs.chmodSync()` methods is a numeric bitmask created using a logical OR of the following constants: Constant Octal Description `fs.constants.S_IRUSR` `0o400` read by owner `fs.constants.S_IWUSR` `0o200` write by owner `fs.constants.S_IXUSR` `0o100` execute/search by owner `fs.constants.S_IRGRP` `0o40` read by group `fs.constants.S_IWGRP` `0o20` write by group `fs.constants.S_IXGRP` `0o10` execute/search by group `fs.constants.S_IROTH` `0o4` read by others `fs.constants.S_IWOTH` `0o2` write by others `fs.constants.S_IXOTH` `0o1` execute/search by others An easier method of constructing the `mode` is to use a sequence of three octal digits (e.g. `765`). The left-most digit (`7` in the example), specifies the permissions for the file owner. The middle digit (`6` in the example), specifies permissions for the group. The right-most digit (`5` in the example), specifies the permissions for others. Number Description `7` read, write, and execute `6` read and write `5` read and execute `4` read only `3` write and execute `2` write only `1` execute only `0` no permission For example, the octal value `0o765` means: The owner may read, write, and execute the file. The group may read and write the file. Others may read and execute the file. When using raw numbers where file modes are expected, any value larger than `0o777` may result in platform-specific behaviors that are not supported to work consistently. Therefore constants like `S_ISVTX`, `S_ISGID`, or `S_ISUID` are not exposed in `fs.constants`.Caveats: on Windows only the write permission can be changed, and the distinction among the permissions of group, owner, or others is not implemented.

#### `fs.chown(path, uid, gid, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously changes owner and group of a file. No arguments other than a possible exception are given to the completion callback.See the POSIX `chown(2)` documentation for more detail.

#### `fs.close(fd[, callback])`

- `fd` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Closes the file descriptor. No arguments other than a possible exception are given to the completion callback.Calling `fs.close()` on any file descriptor (`fd`) that is currently in use through any other `fs` operation may lead to undefined behavior.See the POSIX `close(2)` documentation for more detail.

#### `fs.copyFile(src, dest[, mode], callback)`

- `src` `<string>` | `<Buffer>` | `<URL>` source filename to copy
- `dest` `<string>` | `<Buffer>` | `<URL>` destination filename of the copy operation
- `mode` `<integer>` modifiers for copy operation. **Default:** `0`.
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. No arguments other than a possible exception are given to the callback function. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.`mode` is an optional integer that specifies the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`). `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists. `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used. `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail. `import { copyFile, constants } from 'node:fs'; function callback(err) { if (err) throw err; console.log('source.txt was copied to destination.txt'); } // destination.txt will be created or overwritten by default. copyFile('source.txt', 'destination.txt', callback); // By using COPYFILE_EXCL, the operation will fail if destination.txt exists. copyFile('source.txt', 'destination.txt', constants.COPYFILE_EXCL, callback);`

#### `fs.cp(src, dest[, options], callback)`

- `src` `<string>` | `<URL>` source path to copy.
- `dest` `<string>` | `<URL>` destination path to copy to.
- `options` `<Object>`
  - `dereference` `<boolean>` dereference symlinks. **Default:** `false`.
  - `errorOnExist` `<boolean>` when `force` is `false`, and the destination exists, throw an error. **Default:** `false`.
  - `filter` `<Function>` Function to filter copied files/directories. Return `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. Can also return a `Promise` that fulfills with `true` or `false`. **Default:** `undefined`.
    - `src` `<string>` source path to copy.
    - `dest` `<string>` destination path to copy to.
    - Returns: `<boolean>` | `<Promise>` A value that is coercible to `boolean` or a `Promise` that fulfils with such value.
  - `force` `<boolean>` overwrite existing file or directory. The copy operation will ignore errors if you set this to false and the destination exists. Use the `errorOnExist` option to change this behavior. **Default:** `true`.
  - `mode` `<integer>` modifiers for copy operation. **Default:** `0`. See `mode` flag of `fs.copyFile()`.
  - `preserveTimestamps` `<boolean>` When `true` timestamps from `src` will be preserved. **Default:** `false`.
  - `recursive` `<boolean>` copy directories recursively **Default:** `false`
  - `verbatimSymlinks` `<boolean>` When `true`, path resolution for symlinks will be skipped. **Default:** `false`
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.

#### `fs.createReadStream(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `flags` `<string>` See support of file system `flags`. **Default:** `'r'`.
  - `encoding` `<string>` **Default:** `null`
  - `fd` `<integer>` | `<FileHandle>` **Default:** `null`
  - `mode` `<integer>` **Default:** `0o666`
  - `autoClose` `<boolean>` **Default:** `true`
  - `emitClose` `<boolean>` **Default:** `true`
  - `start` `<integer>`
  - `end` `<integer>` **Default:** `Infinity`
  - `highWaterMark` `<integer>` **Default:** `64 * 1024`
  - `fs` `<Object>` | `<null>` **Default:** `null`
  - `signal` `<AbortSignal>` | `<null>` **Default:** `null`
- Returns: `<fs.ReadStream>`

`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the [0, `Number.MAX_SAFE_INTEGER`] range. If `fd` is specified and `start` is omitted or `undefined`, `fs.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by `<Buffer>`.If `fd` is specified, `ReadStream` will ignore the `path` argument and will use the specified file descriptor. This means that no `'open'` event will be emitted. `fd` should be blocking; non-blocking `fd`s should be passed to `<net.Socket>`.If `fd` points to a character device that only supports blocking reads (such as keyboard or sound card), read operations do not finish until data is available. This can prevent the process from exiting and the stream from closing naturally.By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.By providing the `fs` option, it is possible to override the corresponding `fs` implementations for `open`, `read`, and `close`. When providing the `fs` option, an override for `read` is required. If no `fd` is provided, an override for `open` is also required. If `autoClose` is `true`, an override for `close` is also required.`import { createReadStream } from 'node:fs'; // Create a stream from some character device. const stream = createReadStream('/dev/input/event0'); setTimeout(() => { stream.close(); // This may not close the stream. // Artificially marking end-of-stream, as if the underlying resource had // indicated end-of-file by itself, allows the stream to close. // This does not cancel pending read operations, and if there is such an // operation, the process may still not be able to exit successfully // until it finishes. stream.push(null); stream.read(0); }, 100);`If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak. If `autoClose` is set to true (default behavior), on `'error'` or `'end'` the file descriptor will be closed automatically.`mode` sets the file mode (permission and sticky bits), but only if the file was created.An example to read the last 10 bytes of a file which is 100 bytes long:`import { createReadStream } from 'node:fs'; createReadStream('sample.txt', { start: 90, end: 99 });`If `options` is a string, then it specifies the encoding.

#### `fs.createWriteStream(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `flags` `<string>` See support of file system `flags`. **Default:** `'w'`.
  - `encoding` `<string>` **Default:** `'utf8'`
  - `fd` `<integer>` | `<FileHandle>` **Default:** `null`
  - `mode` `<integer>` **Default:** `0o666`
  - `autoClose` `<boolean>` **Default:** `true`
  - `emitClose` `<boolean>` **Default:** `true`
  - `start` `<integer>`
  - `fs` `<Object>` | `<null>` **Default:** `null`
  - `signal` `<AbortSignal>` | `<null>` **Default:** `null`
  - `highWaterMark` `<number>` **Default:** `16384`
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
- Returns: `<fs.WriteStream>`

`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the [0, `Number.MAX_SAFE_INTEGER`] range. Modifying a file rather than replacing it may require the `flags` option to be set to `r+` rather than the default `w`. The `encoding` can be any one of those accepted by `<Buffer>`.If `autoClose` is set to true (default behavior) on `'error'` or `'finish'` the file descriptor will be closed automatically. If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak.By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.By providing the `fs` option it is possible to override the corresponding `fs` implementations for `open`, `write`, `writev`, and `close`. Overriding `write()` without `writev()` can reduce performance as some optimizations (`_writev()`) will be disabled. When providing the `fs` option, overrides for at least one of `write` and `writev` are required. If no `fd` option is supplied, an override for `open` is also required. If `autoClose` is `true`, an override for `close` is also required.Like `<fs.ReadStream>`, if `fd` is specified, `<fs.WriteStream>` will ignore the `path` argument and will use the specified file descriptor. This means that no `'open'` event will be emitted. `fd` should be blocking; non-blocking `fd`s should be passed to `<net.Socket>`.If `options` is a string, then it specifies the encoding.

#### `fs.exists(path, callback)`

Stability: 0 - Deprecated: Use `fs.stat()` or `fs.access()` instead.

- `path` `<string>` | `<Buffer>` | `<URL>`
- `callback` `<Function>`
  - `exists` `<boolean>`

Test whether or not the element at the given `path` exists by checking with the file system. Then call the `callback` argument with either true or false:`import { exists } from 'node:fs'; exists('/etc/passwd', (e) => { console.log(e ? 'it exists' : 'no passwd!'); });`**The parameters for this callback are not consistent with other Node.js callbacks.** Normally, the first parameter to a Node.js callback is an `err` parameter, optionally followed by other parameters. The `fs.exists()` callback has only one boolean parameter. This is one reason `fs.access()` is recommended instead of `fs.exists()`.If `path` is a symbolic link, it is followed. Thus, if `path` exists but points to a non-existent element, the callback will receive the value `false`.Using `fs.exists()` to check for the existence of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()` is not recommended. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file does not exist.**write (NOT RECOMMENDED)**`import { exists, open, close } from 'node:fs'; exists('myfile', (e) => { if (e) { console.error('myfile already exists'); } else { open('myfile', 'wx', (err, fd) => { if (err) throw err; try { writeMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } }); } });`**write (RECOMMENDED)**`import { open, close } from 'node:fs'; open('myfile', 'wx', (err, fd) => { if (err) { if (err.code === 'EEXIST') { console.error('myfile already exists'); return; } throw err; } try { writeMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } });`**read (NOT RECOMMENDED)**`import { open, close, exists } from 'node:fs'; exists('myfile', (e) => { if (e) { open('myfile', 'r', (err, fd) => { if (err) throw err; try { readMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } }); } else { console.error('myfile does not exist'); } });`**read (RECOMMENDED)**`import { open, close } from 'node:fs'; open('myfile', 'r', (err, fd) => { if (err) { if (err.code === 'ENOENT') { console.error('myfile does not exist'); return; } throw err; } try { readMyData(fd); } finally { close(fd, (err) => { if (err) throw err; }); } });`The "not recommended" examples above check for existence and then use the file; the "recommended" examples are better because they use the file directly and handle the error, if any.In general, check for the existence of a file only if the file won't be used directly, for example when its existence is a signal from another process.

#### `fs.fchmod(fd, mode, callback)`

- `fd` `<integer>`
- `mode` `<string>` | `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Sets the permissions on the file. No arguments other than a possible exception are given to the completion callback.See the POSIX `fchmod(2)` documentation for more detail.

#### `fs.fchown(fd, uid, gid, callback)`

- `fd` `<integer>`
- `uid` `<integer>`
- `gid` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Sets the owner of the file. No arguments other than a possible exception are given to the completion callback.See the POSIX `fchown(2)` documentation for more detail.

#### `fs.fdatasync(fd, callback)`

- `fd` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX `fdatasync(2)` documentation for details. No arguments other than a possible exception are given to the completion callback.

#### `fs.fstat(fd[, options], callback)`

- `fd` `<integer>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `stats` `<fs.Stats>`

Invokes the callback with the `<fs.Stats>` for the file descriptor.See the POSIX `fstat(2)` documentation for more detail.

#### `fs.fsync(fd, callback)`

- `fd` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX `fsync(2)` documentation for more detail. No arguments other than a possible exception are given to the completion callback.

#### `fs.ftruncate(fd[, len], callback)`

- `fd` `<integer>`
- `len` `<integer>` **Default:** `0`
- `callback` `<Function>`
  - `err` `<Error>`

Truncates the file descriptor. No arguments other than a possible exception are given to the completion callback.See the POSIX `ftruncate(2)` documentation for more detail.If the file referred to by the file descriptor was larger than `len` bytes, only the first `len` bytes will be retained in the file.For example, the following program retains only the first four bytes of the file:`import { open, close, ftruncate } from 'node:fs'; function closeFd(fd) { close(fd, (err) => { if (err) throw err; }); } open('temp.txt', 'r+', (err, fd) => { if (err) throw err; try { ftruncate(fd, 4, (err) => { closeFd(fd); if (err) throw err; }); } catch (err) { closeFd(fd); if (err) throw err; } });`If the file previously was shorter than `len` bytes, it is extended, and the extended part is filled with null bytes (`'\0'`):If `len` is negative then `0` will be used.

#### `fs.futimes(fd, atime, mtime, callback)`

- `fd` `<integer>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- `callback` `<Function>`
  - `err` `<Error>`

Change the file system timestamps of the object referenced by the supplied file descriptor. See `fs.utimes()`.

#### `fs.glob(pattern[, options], callback)`

- `pattern` `<string>` | `<string>`[]
- `options` `<Object>`
  - `cwd` `<string>` | `<URL>` current working directory. **Default:** `process.cwd()`
  - `exclude` `<Function>` | `<string>`[] Function to filter out files/directories or a list of glob patterns to be excluded. If a function is provided, return `true` to exclude the item, `false` to include it. **Default:** `undefined`.
  - `followSymlinks` `<boolean>` When `true`, symbolic links to directories are followed while expanding `**` patterns. **Default:** `false`.
  - `withFileTypes` `<boolean>` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`
- Retrieves the files matching the specified pattern.

When `followSymlinks` is enabled, detected symbolic link cycles are not traversed recursively.`import { glob } from 'node:fs'; glob('**/*.js', (err, matches) => { if (err) throw err; console.log(matches); });``const { glob } = require('node:fs'); glob('**/*.js', (err, matches) => { if (err) throw err; console.log(matches); });`

#### `fs.lchmod(path, mode, callback)`

Stability: 0 - Deprecated

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>` | `<AggregateError>`

Changes the permissions on a symbolic link. No arguments other than a possible exception are given to the completion callback.This method is only implemented on macOS.See the POSIX `lchmod(2)` documentation for more detail.

#### `fs.lchown(path, uid, gid, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`
- `callback` `<Function>`
  - `err` `<Error>`

Set the owner of the symbolic link. No arguments other than a possible exception are given to the completion callback.See the POSIX `lchown(2)` documentation for more detail.

#### `fs.lutimes(path, atime, mtime, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- `callback` `<Function>`
  - `err` `<Error>`

Changes the access and modification times of a file in the same way as `fs.utimes()`, with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.No arguments other than a possible exception are given to the completion callback.

#### `fs.link(existingPath, newPath, callback)`

- `existingPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`
- `callback` `<Function>`
  - `err` `<Error>`

Creates a new link from the `existingPath` to the `newPath`. See the POSIX `link(2)` documentation for more detail. No arguments other than a possible exception are given to the completion callback.

#### `fs.lstat(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `stats` `<fs.Stats>`

Retrieves the `<fs.Stats>` for the symbolic link referred to by the path. The callback gets two arguments `(err, stats)` where `stats` is a `<fs.Stats>` object. `lstat()` is identical to `stat()`, except that if `path` is a symbolic link, then the link itself is stat-ed, not the file that it refers to.See the POSIX `lstat(2)` documentation for more details.

#### `fs.mkdir(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` | `<integer>`
  - `recursive` `<boolean>` **Default:** `false`
  - `mode` `<string>` | `<integer>` Not supported on Windows. See File modes for more details. **Default:** `0o777`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `path` `<string>` | `<undefined>` Present only if a directory is created with `recursive` set to `true`.

Asynchronously creates a directory.The callback is given a possible exception and, if `recursive` is `true`, the first directory path created, `(err[, path])`. `path` can still be `undefined` when `recursive` is `true`, if no directory was created (for instance, if it was previously created).The optional `options` argument can be an integer specifying `mode` (permission and sticky bits), or an object with a `mode` property and a `recursive` property indicating whether parent directories should be created. Calling `fs.mkdir()` when `path` is a directory that exists results in an error only when `recursive` is false. If `recursive` is false and the directory exists, an `EEXIST` error occurs.`import { mkdir } from 'node:fs'; // Create ./tmp/a/apple, regardless of whether ./tmp and ./tmp/a exist. mkdir('./tmp/a/apple', { recursive: true }, (err) => { if (err) throw err; });`On Windows, using `fs.mkdir()` on the root directory even with recursion will result in an error:`import { mkdir } from 'node:fs'; mkdir('/', { recursive: true }, (err) => { // => [Error: EPERM: operation not permitted, mkdir 'C:\'] });`See the POSIX `mkdir(2)` documentation for more details.

#### `fs.mkdtemp(prefix[, options], callback)`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `directory` `<string>`

Creates a unique temporary directory.Generates six random characters to be appended behind a required `prefix` to create a unique temporary directory. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.The created directory path is passed as a string to the callback's second parameter.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.`import { mkdtemp } from 'node:fs'; import { join } from 'node:path'; import { tmpdir } from 'node:os'; mkdtemp(join(tmpdir(), 'foo-'), (err, directory) => { if (err) throw err; console.log(directory); // Prints: /tmp/foo-itXde2 or C:\Users\...\AppData\Local\Temp\foo-itXde2 });`The `fs.mkdtemp()` method will append the six randomly selected characters directly to the `prefix` string. For instance, given a directory `/tmp`, if the intention is to create a temporary directory *within* `/tmp`, the `prefix` must end with a trailing platform-specific path separator (`require('node:path').sep`).import { tmpdir } from 'node:os'; import { mkdtemp } from 'node:fs'; // The parent directory for the new temporary directory const tmpDir = tmpdir(); // This method is *INCORRECT*: mkdtemp(tmpDir, (err, directory) => { if (err) throw err; console.log(directory); // Will print something similar to `/tmpabc123`. // A new temporary directory is created at the file system root // rather than *within* the /tmp directory. }); // This method is *CORRECT*: import { sep } from 'node:path'; mkdtemp(`${tmpDir}${sep}`, (err, directory) => { if (err) throw err; console.log(directory); // Will print something similar to `/tmp/abc123`. // A new temporary directory is created within // the /tmp directory. });

#### `fs.open(path[, flags[, mode]], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `flags` `<string>` | `<number>` See support of file system `flags`. **Default:** `'r'`.
- `mode` `<string>` | `<integer>` **Default:** `0o666` (readable and writable)
- `callback` `<Function>`
  - `err` `<Error>`
  - `fd` `<integer>`

Asynchronous file open. See the POSIX `open(2)` documentation for more details.`mode` sets the file mode (permission and sticky bits), but only if the file was created. On Windows, only the write permission can be manipulated; see `fs.chmod()`.The callback gets two arguments `(err, fd)`.Some characters (`< > : " / \ | ? *`) are reserved under Windows as documented by Naming Files, Paths, and Namespaces. Under NTFS, if the filename contains a colon, Node.js will open a file system stream, as described by this MSDN page.Functions based on `fs.open()` exhibit this behavior as well: `fs.writeFile()`, `fs.readFile()`, etc.

#### `fs.openAsBlob(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `type` `<string>` An optional mime type for the blob.
- Returns: `<Promise>` Fulfills with a `<Blob>` upon success.

Returns a `<Blob>` whose data is backed by the given file.The file must not be modified after the `<Blob>` is created. Any modifications will cause reading the `<Blob>` data to fail with a `DOMException` error. Synchronous stat operations on the file when the `Blob` is created, and before each read in order to detect whether the file data has been modified on disk.`import { openAsBlob } from 'node:fs'; const blob = await openAsBlob('the.file.txt'); const ab = await blob.arrayBuffer(); blob.stream();``const { openAsBlob } = require('node:fs'); (async () => { const blob = await openAsBlob('the.file.txt'); const ab = await blob.arrayBuffer(); blob.stream(); })();`

#### `fs.opendir(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `bufferSize` `<number>` Number of directory entries that are buffered internally when reading from the directory. Higher values lead to better performance but higher memory usage. **Default:** `32`
  - `recursive` `<boolean>` **Default:** `false`
- `callback` `<Function>`
  - `err` `<Error>`
  - `dir` `<fs.Dir>`

Asynchronously open a directory. See the POSIX `opendir(3)` documentation for more details.Creates an `<fs.Dir>`, which contains all further functions for reading from and cleaning up the directory.The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.

#### `fs.read(fd, buffer, offset, length, position, callback)`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` The buffer that the data will be written to.
- `offset` `<integer>` The position in `buffer` to write the data to.
- `length` `<integer>` The number of bytes to read.
- `position` `<integer>` | `<bigint>` | `<null>` Specifies where to begin reading from in the file. If `position` is `null` or `-1`, data will be read from the current file position, and the file position will be updated. If `position` is a non-negative integer, the file position will be unchanged.
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesRead` `<integer>`
  - `buffer` `<Buffer>`

Read data from the file specified by `fd`.The callback is given the three arguments, `(err, bytesRead, buffer)`.If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.If this method is invoked as its `util.promisify()`ed version, it returns a promise for an `Object` with `bytesRead` and `buffer` properties.The `fs.read()` method reads data from the file specified by the file descriptor (`fd`). The `length` argument indicates the maximum number of bytes that Node.js will attempt to read from the kernel. However, the actual number of bytes read (`bytesRead`) can be lower than the specified `length` for various reasons.For example: If the file is shorter than the specified `length`, `bytesRead` will be set to the actual number of bytes read. If the file encounters EOF (End of File) before the buffer could be filled, Node.js will read all available bytes until EOF is encountered, and the `bytesRead` parameter in the callback will indicate the actual number of bytes read, which may be less than the specified `length`. If the file is on a slow network `filesystem` or encounters any other issue during reading, `bytesRead` can be lower than the specified `length`. Therefore, when using `fs.read()`, it's important to check the `bytesRead` value to determine how many bytes were actually read from the file. Depending on your application logic, you may need to handle cases where `bytesRead` is lower than the specified `length`, such as by wrapping the read call in a loop if you require a minimum amount of bytes.This behavior is similar to the POSIX `preadv2` function.

#### `fs.read(fd[, options], callback)`

- `fd` `<integer>`
- `options` `<Object>`
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` **Default:** `Buffer.alloc(16384)`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesRead` `<integer>`
  - `buffer` `<Buffer>`

Similar to the `fs.read()` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

#### `fs.read(fd, buffer[, options], callback)`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` The buffer that the data will be written to.
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesRead` `<integer>`
  - `buffer` `<Buffer>`

Similar to the `fs.read()` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

#### `fs.readdir(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
  - `withFileTypes` `<boolean>` **Default:** `false`
  - `recursive` `<boolean>` If `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files and directories. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `files` `<string>`[] | `<Buffer>`[] | `<fs.Dirent>`[]

Reads the contents of a directory. The callback gets two arguments `(err, files)` where `files` is an array of the names of the files in the directory excluding `'.'` and `'..'`.See the POSIX `readdir(3)` documentation for more details.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames passed to the callback. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as `<Buffer>` objects.If `options.withFileTypes` is set to `true`, the `files` array will contain `<fs.Dirent>` objects.

#### `fs.readFile(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<integer>` filename or file descriptor
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `null`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'r'`.
  - `signal` `<AbortSignal>` allows aborting an in-progress readFile
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<Function>` A buffer to read into, or a function called with the file size that returns the buffer.
- `callback` `<Function>`
  - `err` `<Error>` | `<AggregateError>`
  - `data` `<string>` | `<Buffer>`

Asynchronously reads the entire contents of a file.`import { readFile } from 'node:fs'; readFile('/etc/passwd', (err, data) => { if (err) throw err; console.log(data); });`The callback is passed two arguments `(err, data)`, where `data` is the contents of the file.If no encoding is specified, then the raw buffer is returned.If `buffer` is provided and no encoding is specified, the returned `<Buffer>` is a view over the supplied buffer containing only the bytes read. If the supplied buffer is too small to contain the entire file, the callback is called with an error.If `options` is a string, then it specifies the encoding:`import { readFile } from 'node:fs'; readFile('/etc/passwd', 'utf8', callback);`When the path is a directory, the behavior of `fs.readFile()` and `fs.readFileSync()` is platform-specific. On macOS, Linux, and Windows, an error will be returned. On FreeBSD, a representation of the directory's contents will be returned.`import { readFile } from 'node:fs'; // macOS, Linux, and Windows readFile('<directory>', (err, data) => { // => [Error: EISDIR: illegal operation on a directory, read <directory>] }); // FreeBSD readFile('<directory>', (err, data) => { // => null, <data> });`It is possible to abort an ongoing request using an `AbortSignal`. If a request is aborted the callback is called with an `AbortError`:`import { readFile } from 'node:fs'; const controller = new AbortController(); const signal = controller.signal; readFile(fileInfo[0].name, { signal }, (err, buf) => { // ... }); // When you want to abort the request controller.abort();`The `fs.readFile()` function buffers the entire file. To minimize memory costs, when possible prefer streaming via `fs.createReadStream()`.Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.readFile` performs.An example using the `buffer` option with a pre-allocated buffer:import { Buffer } from 'node:buffer'; import { readFile } from 'node:fs'; const buf = Buffer.alloc(16384); readFile('/path/to/file', { buffer: buf }, (err, data) => { if (err) throw err; console.log(data); // A view over `buf` containing only the bytes read });An example using the `buffer` option with a function returning a buffer:`import { Buffer } from 'node:buffer'; import { readFile } from 'node:fs'; readFile('/path/to/file', { buffer: (size) => Buffer.alloc(size), }, (err, data) => { if (err) throw err; console.log(data); });`

##### File descriptors

1. Any specified file descriptor has to support reading.
2. If a file descriptor is specified as the `path`, it will not be closed automatically.
3. The reading will begin at the current position. For example, if the file already had `'Hello World'` and six bytes are read with the file descriptor, the call to `fs.readFile()` with the same file descriptor, would give `'World'`, rather than `'Hello World'`.

##### Performance Considerations

The `fs.readFile()` method asynchronously reads the contents of a file into memory one chunk at a time, allowing the event loop to turn between each chunk. This allows the read operation to have less impact on other activity that may be using the underlying libuv thread pool but means that it will take longer to read a complete file into memory.The additional read overhead can vary broadly on different systems and depends on the type of file being read. If the file type is not a regular file (a pipe for instance) and Node.js is unable to determine an actual file size, each read operation will load on 64 KiB of data. For regular files, each read will process 512 KiB of data.For applications that require as-fast-as-possible reading of file contents, it is better to use `fs.read()` directly and for application code to manage reading the full contents of the file itself.The Node.js GitHub issue #25741 provides more information and a detailed analysis on the performance of `fs.readFile()` for multiple file sizes in different Node.js versions.

#### `fs.readlink(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `linkString` `<string>` | `<Buffer>`

Reads the contents of the symbolic link referred to by `path`. The callback gets two arguments `(err, linkString)`.See the POSIX `readlink(2)` documentation for more details.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path passed to the callback. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a `<Buffer>` object.

#### `fs.readv(fd, buffers[, position], callback)`

- `fd` `<integer>`
- `buffers` {ArrayBufferView[]}
- `position` `<integer>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesRead` `<integer>`
  - `buffers` {ArrayBufferView[]}

Read from a file specified by `fd` and write to an array of `ArrayBufferView`s using `readv()`.`position` is the offset from the beginning of the file from where data should be read. If `typeof position !== 'number'`, the data will be read from the current position.The callback will be given three arguments: `err`, `bytesRead`, and `buffers`. `bytesRead` is how many bytes were read from the file.If this method is invoked as its `util.promisify()`ed version, it returns a promise for an `Object` with `bytesRead` and `buffers` properties.

#### `fs.realpath(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `resolvedPath` `<string>` | `<Buffer>`

Asynchronously computes the canonical pathname by resolving `.`, `..`, and symbolic links.A canonical pathname is not necessarily unique. Hard links and bind mounts can expose a file system entity through many pathnames.This function behaves like `realpath(3)`, with some exceptions: No case conversion is performed on case-insensitive file systems. The maximum number of symbolic links is platform-independent and generally (much) higher than what the native `realpath(3)` implementation supports. The `callback` gets two arguments `(err, resolvedPath)`. May use `process.cwd` to resolve relative paths.Only paths that can be converted to UTF8 strings are supported.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path passed to the callback. If the `encoding` is set to `'buffer'`, the path returned will be passed as a `<Buffer>` object.If `path` resolves to a socket or a pipe, the function will return a system dependent name for that object.A path that does not exist results in an ENOENT error. `error.path` is the absolute file path.

#### `fs.realpath.native(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `resolvedPath` `<string>` | `<Buffer>`

Asynchronous `realpath(3)`.The `callback` gets two arguments `(err, resolvedPath)`.Only paths that can be converted to UTF8 strings are supported.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path passed to the callback. If the `encoding` is set to `'buffer'`, the path returned will be passed as a `<Buffer>` object.On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.

#### `fs.rename(oldPath, newPath, callback)`

- `oldPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously rename file at `oldPath` to the pathname provided as `newPath`. In the case that `newPath` already exists, it will be overwritten. If there is a directory at `newPath`, an error will be raised instead. No arguments other than a possible exception are given to the completion callback.See also: `rename(2)`.`import { rename } from 'node:fs'; rename('oldFile.txt', 'newFile.txt', (err) => { if (err) throw err; console.log('Rename complete!'); });`

#### `fs.rmdir(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` There are currently no options exposed. There used to be options for `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronous `rmdir(2)`. No arguments other than a possible exception are given to the completion callback.Using `fs.rmdir()` on a file (not a directory) results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.To get a behavior similar to the `rm -rf` Unix command, use `fs.rm()` with options `{ recursive: true, force: true }`.

#### `fs.rm(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `force` `<boolean>` When `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
  - `maxRetries` `<integer>` If an `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
  - `recursive` `<boolean>` If `true`, perform a recursive removal. In recursive mode operations are retried on failure. **Default:** `false`.
  - `retryDelay` `<integer>` The amount of time in milliseconds to wait between retries. This option is ignored if the `recursive` option is not `true`. **Default:** `100`.
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously removes files and directories (modeled on the standard POSIX `rm` utility). No arguments other than a possible exception are given to the completion callback.

#### `fs.stat(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
  - `throwIfNoEntry` `<boolean>` Whether an exception will be thrown if no file system entry exists, rather than returning `undefined`. **Default:** `true`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `stats` `<fs.Stats>`

Asynchronous `stat(2)`. The callback gets two arguments `(err, stats)` where `stats` is an `<fs.Stats>` object.In case of an error, the `err.code` will be one of Common System Errors.`fs.stat()` follows symbolic links. Use `fs.lstat()` to look at the links themselves.Using `fs.stat()` to check for the existence of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()` is not recommended. Instead, user code should open/read/write the file directly and handle the error raised if the file is not available.To check if a file exists without manipulating it afterwards, `fs.access()` is recommended.For example, given the following directory structure:`- txtDir -- file.txt - app.js`The next program will check for the stats of the given paths:`import { stat } from 'node:fs'; const pathsToCheck = ['./txtDir', './txtDir/file.txt']; for (let i = 0; i < pathsToCheck.length; i++) { stat(pathsToCheck[i], (err, stats) => { console.log(stats.isDirectory()); console.log(stats); }); }`The resulting output will resemble:`true Stats { dev: 16777220, mode: 16877, nlink: 3, uid: 501, gid: 20, rdev: 0, blksize: 4096, ino: 14214262, size: 96, blocks: 0, atimeMs: 1561174653071.963, mtimeMs: 1561174614583.3518, ctimeMs: 1561174626623.5366, birthtimeMs: 1561174126937.2893, atime: 2019-06-22T03:37:33.072Z, mtime: 2019-06-22T03:36:54.583Z, ctime: 2019-06-22T03:37:06.624Z, birthtime: 2019-06-22T03:28:46.937Z, atimeInstant: 2019-06-22T03:37:33.071963Z, mtimeInstant: 2019-06-22T03:36:54.5833518Z, ctimeInstant: 2019-06-22T03:37:06.6235366Z, birthtimeInstant: 2019-06-22T03:28:46.9372893Z } false Stats { dev: 16777220, mode: 33188, nlink: 1, uid: 501, gid: 20, rdev: 0, blksize: 4096, ino: 14214074, size: 8, blocks: 8, atimeMs: 1561174616618.8555, mtimeMs: 1561174614584, ctimeMs: 1561174614583.8145, birthtimeMs: 1561174007710.7478, atime: 2019-06-22T03:36:56.619Z, mtime: 2019-06-22T03:36:54.584Z, ctime: 2019-06-22T03:36:54.584Z, birthtime: 2019-06-22T03:26:47.711Z, atimeInstant: 2019-06-22T03:36:56.6188555Z, mtimeInstant: 2019-06-22T03:36:54.584Z, ctimeInstant: 2019-06-22T03:36:54.5838145Z, birthtimeInstant: 2019-06-22T03:26:47.7107478Z }`

#### `fs.statfs(path[, options], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.StatFs>` object should be `bigint`. **Default:** `false`.
- `callback` `<Function>`
  - `err` `<Error>`
  - `stats` `<fs.StatFs>`

Asynchronous `statfs(2)`. Returns information about the mounted file system which contains `path`. The callback gets two arguments `(err, stats)` where `stats` is an `<fs.StatFs>` object.In case of an error, the `err.code` will be one of Common System Errors.

#### `fs.symlink(target, path[, type], callback)`

- `target` `<string>` | `<Buffer>` | `<URL>`
- `path` `<string>` | `<Buffer>` | `<URL>`
- `type` `<string>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`

Creates the link called `path` pointing to `target`. No arguments other than a possible exception are given to the completion callback.See the POSIX `symlink(2)` documentation for more details.The `type` argument is only available on Windows and ignored on other platforms. It can be set to `'dir'`, `'file'`, or `'junction'`. If the `type` argument is `null`, Node.js will autodetect `target` type and use `'file'` or `'dir'`. If the `target` does not exist, `'file'` will be used. Windows junction points require the destination path to be absolute. When using `'junction'`, the `target` argument will automatically be normalized to absolute path. Junction points on NTFS volumes can only point to directories.Relative targets are relative to the link's parent directory.`import { symlink } from 'node:fs'; symlink('./mew', './mewtwo', callback);`The above example creates a symbolic link `mewtwo` which points to `mew` in the same directory:`$ tree . . ├── mew └── mewtwo -> ./mew`

#### `fs.truncate(path[, len], callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `len` `<integer>` **Default:** `0`
- `callback` `<Function>`
  - `err` `<Error>` | `<AggregateError>`

Truncates the file. No arguments other than a possible exception are given to the completion callback. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncate()` is called.`import { truncate } from 'node:fs'; // Assuming that 'path/file.txt' is a regular file. truncate('path/file.txt', (err) => { if (err) throw err; console.log('path/file.txt was truncated'); });``const { truncate } = require('node:fs'); // Assuming that 'path/file.txt' is a regular file. truncate('path/file.txt', (err) => { if (err) throw err; console.log('path/file.txt was truncated'); });`Passing a file descriptor is deprecated and may result in an error being thrown in the future.See the POSIX `truncate(2)` documentation for more details.

#### `fs.unlink(path, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously removes a file or symbolic link. No arguments other than a possible exception are given to the completion callback.`import { unlink } from 'node:fs'; // Assuming that 'path/file.txt' is a regular file. unlink('path/file.txt', (err) => { if (err) throw err; console.log('path/file.txt was deleted'); });``fs.unlink()` will not work on a directory, empty or otherwise. To remove a directory, use `fs.rmdir()`.See the POSIX `unlink(2)` documentation for more details.

#### `fs.unwatchFile(filename[, listener])`

- `filename` `<string>` | `<Buffer>` | `<URL>`
- `listener` `<Function>` Optional, a listener previously attached using `fs.watchFile()`

Stop watching for changes on `filename`. If `listener` is specified, only that particular listener is removed. Otherwise, *all* listeners are removed, effectively stopping watching of `filename`.Calling `fs.unwatchFile()` with a filename that is not being watched is a no-op, not an error.Using `fs.watch()` is more efficient than `fs.watchFile()` and `fs.unwatchFile()`. `fs.watch()` should be used instead of `fs.watchFile()` and `fs.unwatchFile()` when possible.

#### `fs.utimes(path, atime, mtime, callback)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- `callback` `<Function>`
  - `err` `<Error>`

Change the file system timestamps of the object referenced by `path`.The `atime` and `mtime` arguments follow these rules: Values can be either numbers representing Unix epoch time in seconds, `Date`s, or a numeric string like `'123456789.0'`. If the value can not be converted to a number, or is `NaN`, `Infinity`, or `-Infinity`, an `Error` will be thrown.

#### `fs.watch(filename[, options][, listener])`

- `filename` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `persistent` `<boolean>` Indicates whether the process should continue to run as long as files are being watched. **Default:** `true`.
  - `recursive` `<boolean>` Indicates whether all subdirectories should be watched, or only the current directory. This applies when a directory is specified, and only on supported platforms (See caveats). **Default:** `false`.
  - `encoding` `<string>` Specifies the character encoding to be used for the filename passed to the listener. **Default:** `'utf8'`.
  - `signal` `<AbortSignal>` allows closing the watcher with an AbortSignal.
  - `throwIfNoEntry` `<boolean>` Indicates whether an exception should be thrown when the path does not exist. **Default:** `true`.
  - `ignore` `<string>` | `<RegExp>` | `<Function>` | `<Array>` Pattern(s) to ignore. Strings are glob patterns (using `minimatch`), RegExp patterns are tested against the filename, and functions receive the filename and return `true` to ignore. **Default:** `undefined`.
- `listener` `<Function>` | `<undefined>` **Default:** `undefined`
  - `eventType` `<string>`
  - `filename` `<string>` | `<Buffer>` | `<null>`
- Returns: `<fs.FSWatcher>`

Watch for changes on `filename`, where `filename` is either a file or a directory.The second argument is optional. If `options` is provided as a string, it specifies the `encoding`. Otherwise `options` should be passed as an object.The listener callback gets two arguments `(eventType, filename)`. `eventType` is either `'rename'` or `'change'`, and `filename` is the name of the file which triggered the event.On most platforms, `'rename'` is emitted whenever a filename appears or disappears in the directory.The listener callback is attached to the `'change'` event fired by `<fs.FSWatcher>`, but it is not the same thing as the `'change'` value of `eventType`.If a `signal` is passed, aborting the corresponding AbortController will close the returned `<fs.FSWatcher>`.

##### Caveats

The `fs.watch` API is not 100% consistent across platforms, and is unavailable in some situations.On Windows, no events will be emitted if the watched directory is moved or renamed. An `EPERM` error is reported when the watched directory is deleted.The `fs.watch` API does not provide any protection with respect to malicious actions on the file system. For example, on Windows it is implemented by monitoring changes in a directory versus specific files. This allows substitution of a file and fs reporting changes on the new file with the same filename.

###### Availability

This feature depends on the underlying operating system providing a way to be notified of file system changes. On Linux systems, this uses `inotify(7)`. On BSD systems, this uses `kqueue(2)`. On macOS, this uses `kqueue(2)` for files and `FSEvents` for directories. On SunOS systems (including Solaris and SmartOS), this uses `event ports`. On Windows systems, this feature depends on `ReadDirectoryChangesW`. On AIX systems, this feature depends on `AHAFS`, which must be enabled. On IBM i systems, this feature is not supported. If the underlying functionality is not available for some reason, then `fs.watch()` will not be able to function and may throw an exception. For example, watching files or directories can be unreliable, and in some cases impossible, on network file systems (NFS, SMB, etc) or host file systems when using virtualization software such as Vagrant or Docker.It is still possible to use `fs.watchFile()`, which uses stat polling, but this method is slower and less reliable.

###### Inodes

On Linux and macOS systems, `fs.watch()` resolves the path to an inode and watches the inode. If the watched path is deleted and recreated, it is assigned a new inode. The watch will emit an event for the delete but will continue watching the *original* inode. Events for the new inode will not be emitted. This is expected behavior.AIX files retain the same inode for the lifetime of a file. Saving and closing a watched file on AIX will result in two notifications (one for adding new content, and one for truncation).

###### Filename argument

Providing `filename` argument in the callback is only supported on Linux, macOS, Windows, and AIX. Even on supported platforms, `filename` is not always guaranteed to be provided. Therefore, don't assume that `filename` argument is always provided in the callback, and have some fallback logic if it is `null`.import { watch } from 'node:fs'; watch('somedir', (eventType, filename) => { console.log(`event type is: ${eventType}`); if (filename) { console.log(`filename provided: ${filename}`); } else { console.log('filename not provided'); } });

#### `fs.watchFile(filename[, options], listener)`

- `filename` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` **Default:** `false`
  - `persistent` `<boolean>` **Default:** `true`
  - `interval` `<integer>` **Default:** `5007`
- `listener` `<Function>`
  - `current` `<fs.Stats>`
  - `previous` `<fs.Stats>`
- Returns: `<fs.StatWatcher>`

Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.The `options` argument may be omitted. If provided, it should be an object. The `options` object may contain a boolean named `persistent` that indicates whether the process should continue to run as long as files are being watched. The `options` object may specify an `interval` property indicating how often the target should be polled in milliseconds.The `listener` gets two arguments the current stat object and the previous stat object:import { watchFile } from 'node:fs'; watchFile('message.text', (curr, prev) => { console.log(`the current mtime is: ${curr.mtime}`); console.log(`the previous mtime was: ${prev.mtime}`); });These stat objects are instances of `fs.Stat`. If the `bigint` option is `true`, the numeric values in these objects are specified as `BigInt`s.To be notified when the file was modified, not just accessed, it is necessary to compare `curr.mtimeMs` and `prev.mtimeMs`.When an `fs.watchFile` operation results in an `ENOENT` error, it will invoke the listener once, with all the fields zeroed (or, for dates, the Unix Epoch). If the file is created later on, the listener will be called again, with the latest stat objects. This is a change in functionality since v0.10.Using `fs.watch()` is more efficient than `fs.watchFile` and `fs.unwatchFile`. `fs.watch` should be used instead of `fs.watchFile` and `fs.unwatchFile` when possible.When a file being watched by `fs.watchFile()` disappears and reappears, then the contents of `previous` in the second callback event (the file's reappearance) will be the same as the contents of `previous` in the first callback event (its disappearance).This happens when: the file is deleted, followed by a restore the file is renamed and then renamed a second time back to its original name

#### `fs.write(fd, buffer, offset[, length[, position]], callback)`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `offset` `<integer>` **Default:** `0`
- `length` `<integer>` **Default:** `buffer.byteLength - offset`
- `position` `<integer>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesWritten` `<integer>`
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`

Write `buffer` to the file specified by `fd`.`offset` determines the part of the buffer to be written, and `length` is an integer specifying the number of bytes to write.`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position. See `pwrite(2)`.The callback will be given three arguments `(err, bytesWritten, buffer)` where `bytesWritten` specifies how many *bytes* were written from `buffer`.If this method is invoked as its `util.promisify()`ed version, it returns a promise for an `Object` with `bytesWritten` and `buffer` properties.It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

#### `fs.write(fd, buffer[, options], callback)`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesWritten` `<integer>`
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`

Write `buffer` to the file specified by `fd`.Similar to the above `fs.write` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

#### `fs.write(fd, string[, position[, encoding]], callback)`

- `fd` `<integer>`
- `string` `<string>`
- `position` `<integer>` | `<null>` **Default:** `null`
- `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `written` `<integer>`
  - `string` `<string>`

Write `string` to the file specified by `fd`. If `string` is not a string, an exception is thrown.`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'` the data will be written at the current position. See `pwrite(2)`.`encoding` is the expected string encoding.The callback will receive the arguments `(err, written, string)` where `written` specifies how many *bytes* the passed string required to be written. Bytes written is not necessarily the same as string characters written. See `Buffer.byteLength`.It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.On Windows, if the file descriptor is connected to the console (e.g. `fd == 1` or `stdout`) a string containing non-ASCII characters will not be rendered properly by default, regardless of the encoding used. It is possible to configure the console to render UTF-8 properly by changing the active codepage with the `chcp 65001` command. See the chcp docs for more details.

#### `fs.writeFile(file, data[, options], callback)`

- `file` `<string>` | `<Buffer>` | `<URL>` | `<integer>` filename or file descriptor
- `data` `<string>` | `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'w'`.
  - `flush` `<boolean>` If all data is successfully written to the file, and `flush` is `true`, `fs.fsync()` is used to flush the data. **Default:** `false`.
  - `signal` `<AbortSignal>` allows aborting an in-progress writeFile
- `callback` `<Function>`
  - `err` `<Error>` | `<AggregateError>`

When `file` is a filename, asynchronously writes data to the file, replacing the file if it already exists. `data` can be a string or a buffer.When `file` is a file descriptor, the behavior is similar to calling `fs.write()` directly (which is recommended). See the notes below on using a file descriptor.The `encoding` option is ignored if `data` is a buffer.The `mode` option only affects the newly created file. See `fs.open()` for more details.`import { writeFile } from 'node:fs'; import { Buffer } from 'node:buffer'; const data = new Uint8Array(Buffer.from('Hello Node.js')); writeFile('message.txt', data, (err) => { if (err) throw err; console.log('The file has been saved!'); });`If `options` is a string, then it specifies the encoding:`import { writeFile } from 'node:fs'; writeFile('message.txt', 'Hello Node.js', 'utf8', callback);`It is unsafe to use `fs.writeFile()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.Similarly to `fs.readFile` - `fs.writeFile` is a convenience method that performs multiple `write` calls internally to write the buffer passed to it. For performance sensitive code consider using `fs.createWriteStream()`.It is possible to use an `<AbortSignal>` to cancel an `fs.writeFile()`. Cancelation is "best effort", and some amount of data is likely still to be written.`import { writeFile } from 'node:fs'; import { Buffer } from 'node:buffer'; const controller = new AbortController(); const { signal } = controller; const data = new Uint8Array(Buffer.from('Hello Node.js')); writeFile('message.txt', data, { signal }, (err) => { // When a request is aborted - the callback is called with an AbortError }); // When the request should be aborted controller.abort();`Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.writeFile` performs.

##### Using `fs.writeFile()` with file descriptors

When `file` is a file descriptor, the behavior is almost identical to directly calling `fs.write()` like:`import { write } from 'node:fs'; import { Buffer } from 'node:buffer'; write(fd, Buffer.from(data, options.encoding), callback);`The difference from directly calling `fs.write()` is that under some unusual conditions, `fs.write()` might write only part of the buffer and need to be retried to write the remaining data, whereas `fs.writeFile()` retries until the data is entirely written (or an error occurs).The implications of this are a common source of confusion. In the file descriptor case, the file is not replaced! The data is not necessarily written to the beginning of the file, and the file's original data may remain before and/or after the newly written data.For example, if `fs.writeFile()` is called twice in a row, first to write the string `'Hello'`, then to write the string `', World'`, the file would contain `'Hello, World'`, and might contain some of the file's original data (depending on the size of the original file, and the position of the file descriptor). If a file name had been used instead of a descriptor, the file would be guaranteed to contain only `', World'`.

#### `fs.writev(fd, buffers[, position], callback)`

- `fd` `<integer>`
- `buffers` {ArrayBufferView[]}
- `position` `<integer>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesWritten` `<integer>`
  - `buffers` {ArrayBufferView[]}

Write an array of `ArrayBufferView`s to the file specified by `fd` using `writev()`.`position` is the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position.The callback will be given three arguments: `err`, `bytesWritten`, and `buffers`. `bytesWritten` is how many bytes were written from `buffers`.If this method is `util.promisify()`ed, it returns a promise for an `Object` with `bytesWritten` and `buffers` properties.It is unsafe to use `fs.writev()` multiple times on the same file without waiting for the callback. For this scenario, use `fs.createWriteStream()`.On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

### Synchronous API

The synchronous APIs perform all operations synchronously, blocking the event loop until the operation completes or fails.

#### `fs.accessSync(path[, mode])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>` **Default:** `fs.constants.F_OK`

Synchronously tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check File access constants for possible values of `mode`.If any of the accessibility checks fail, an `Error` will be thrown. Otherwise, the method will return `undefined`.`import { accessSync, constants } from 'node:fs'; try { accessSync('etc/passwd', constants.R_OK | constants.W_OK); console.log('can read/write'); } catch (err) { console.error('no access!'); }`

#### `fs.appendFileSync(path, data[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<number>` filename or file descriptor
- `data` `<string>` | `<Buffer>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'a'`.
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.

Synchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `<Buffer>`.The `mode` option only affects the newly created file. See `fs.open()` for more details.`import { appendFileSync } from 'node:fs'; try { appendFileSync('message.txt', 'data to append'); console.log('The "data to append" was appended to file!'); } catch (err) { /* Handle the error */ }`If `options` is a string, then it specifies the encoding:`import { appendFileSync } from 'node:fs'; appendFileSync('message.txt', 'data to append', 'utf8');`The `path` may be specified as a numeric file descriptor that has been opened for appending (using `fs.open()` or `fs.openSync()`). The file descriptor will not be closed automatically.`import { openSync, closeSync, appendFileSync } from 'node:fs'; let fd; try { fd = openSync('message.txt', 'a'); appendFileSync(fd, 'data to append', 'utf8'); } catch (err) { /* Handle the error */ } finally { if (fd !== undefined) closeSync(fd); }`

#### `fs.chmodSync(path, mode)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<string>` | `<integer>`

For detailed information, see the documentation of the asynchronous version of this API: `fs.chmod()`.See the POSIX `chmod(2)` documentation for more detail.

#### `fs.chownSync(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`

Synchronously changes owner and group of a file. Returns `undefined`. This is the synchronous version of `fs.chown()`.See the POSIX `chown(2)` documentation for more detail.

#### `fs.closeSync(fd)`

- `fd` `<integer>`

Closes the file descriptor. Returns `undefined`.Calling `fs.closeSync()` on any file descriptor (`fd`) that is currently in use through any other `fs` operation may lead to undefined behavior.See the POSIX `close(2)` documentation for more detail.

#### `fs.copyFileSync(src, dest[, mode])`

- `src` `<string>` | `<Buffer>` | `<URL>` source filename to copy
- `dest` `<string>` | `<Buffer>` | `<URL>` destination filename of the copy operation
- `mode` `<integer>` modifiers for copy operation. **Default:** `0`.

Synchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. Returns `undefined`. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.`mode` is an optional integer that specifies the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`). `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists. `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used. `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail. `import { copyFileSync, constants } from 'node:fs'; // destination.txt will be created or overwritten by default. copyFileSync('source.txt', 'destination.txt'); console.log('source.txt was copied to destination.txt'); // By using COPYFILE_EXCL, the operation will fail if destination.txt exists. copyFileSync('source.txt', 'destination.txt', constants.COPYFILE_EXCL);`

#### `fs.cpSync(src, dest[, options])`

- `src` `<string>` | `<URL>` source path to copy.
- `dest` `<string>` | `<URL>` destination path to copy to.
- `options` `<Object>`
  - `dereference` `<boolean>` dereference symlinks. **Default:** `false`.
  - `errorOnExist` `<boolean>` when `force` is `false`, and the destination exists, throw an error. **Default:** `false`.
  - `filter` `<Function>` Function to filter copied files/directories. Return `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. **Default:** `undefined`
    - `src` `<string>` source path to copy.
    - `dest` `<string>` destination path to copy to.
    - Returns: `<boolean>` Any non-`Promise` value that is coercible to `boolean`.
  - `force` `<boolean>` overwrite existing file or directory. The copy operation will ignore errors if you set this to false and the destination exists. Use the `errorOnExist` option to change this behavior. **Default:** `true`.
  - `mode` `<integer>` modifiers for copy operation. **Default:** `0`. See `mode` flag of `fs.copyFileSync()`.
  - `preserveTimestamps` `<boolean>` When `true` timestamps from `src` will be preserved. **Default:** `false`.
  - `recursive` `<boolean>` copy directories recursively **Default:** `false`
  - `verbatimSymlinks` `<boolean>` When `true`, path resolution for symlinks will be skipped. **Default:** `false`

Synchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.

#### `fs.existsSync(path)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- Returns: `<boolean>`

Returns `true` if the path exists, `false` otherwise.For detailed information, see the documentation of the asynchronous version of this API: `fs.exists()`.`fs.exists()` is deprecated, but `fs.existsSync()` is not. The `callback` parameter to `fs.exists()` accepts parameters that are inconsistent with other Node.js callbacks. `fs.existsSync()` does not use a callback.`import { existsSync } from 'node:fs'; if (existsSync('/etc/passwd')) console.log('The path exists.');`

#### `fs.fchmodSync(fd, mode)`

- `fd` `<integer>`
- `mode` `<string>` | `<integer>`

Sets the permissions on the file. Returns `undefined`.See the POSIX `fchmod(2)` documentation for more detail.

#### `fs.fchownSync(fd, uid, gid)`

- `fd` `<integer>`
- `uid` `<integer>` The file's new owner's user id.
- `gid` `<integer>` The file's new group's group id.

Sets the owner of the file. Returns `undefined`.See the POSIX `fchown(2)` documentation for more detail.

#### `fs.fdatasyncSync(fd)`

- `fd` `<integer>`

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX `fdatasync(2)` documentation for details. Returns `undefined`.

#### `fs.fstatSync(fd[, options])`

- `fd` `<integer>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
- Returns: `<fs.Stats>`

Retrieves the `<fs.Stats>` for the file descriptor.See the POSIX `fstat(2)` documentation for more detail.

#### `fs.fsyncSync(fd)`

- `fd` `<integer>`

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX `fsync(2)` documentation for more detail. Returns `undefined`.

#### `fs.ftruncateSync(fd[, len])`

- `fd` `<integer>`
- `len` `<integer>` **Default:** `0`
