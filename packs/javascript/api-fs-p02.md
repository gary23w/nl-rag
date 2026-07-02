---
title: "File system (part 2/3)"
source: https://nodejs.org/api/fs.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 2/3
---

# File system

Truncates the file descriptor. Returns `undefined`.For detailed information, see the documentation of the asynchronous version of this API: `fs.ftruncate()`.

#### `fs.futimesSync(fd, atime, mtime)`

- `fd` `<integer>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`

Synchronous version of `fs.futimes()`. Returns `undefined`.

#### `fs.globSync(pattern[, options])`

- `pattern` `<string>` | `<string>`[]
- `options` `<Object>`
  - `cwd` `<string>` | `<URL>` current working directory. **Default:** `process.cwd()`
  - `exclude` `<Function>` | `<string>`[] Function to filter out files/directories or a list of glob patterns to be excluded. If a function is provided, return `true` to exclude the item, `false` to include it. **Default:** `undefined`.
  - `followSymlinks` `<boolean>` When `true`, symbolic links to directories are followed while expanding `**` patterns. **Default:** `false`.
  - `withFileTypes` `<boolean>` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
- Returns: `<string>`[] paths of files that match the pattern.

When `followSymlinks` is enabled, detected symbolic link cycles are not traversed recursively.`import { globSync } from 'node:fs'; console.log(globSync('**/*.js'));``const { globSync } = require('node:fs'); console.log(globSync('**/*.js'));`

#### `fs.lchmodSync(path, mode)`

Stability: 0 - Deprecated

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>`

Changes the permissions on a symbolic link. Returns `undefined`.This method is only implemented on macOS.See the POSIX `lchmod(2)` documentation for more detail.

#### `fs.lchownSync(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>` The file's new owner's user id.
- `gid` `<integer>` The file's new group's group id.

Set the owner for the path. Returns `undefined`.See the POSIX `lchown(2)` documentation for more details.

#### `fs.lutimesSync(path, atime, mtime)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`

Change the file system timestamps of the symbolic link referenced by `path`. Returns `undefined`, or throws an exception when parameters are incorrect or the operation fails. This is the synchronous version of `fs.lutimes()`.

#### `fs.linkSync(existingPath, newPath)`

- `existingPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`

Creates a new link from the `existingPath` to the `newPath`. See the POSIX `link(2)` documentation for more detail. Returns `undefined`.

#### `fs.lstatSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
  - `throwIfNoEntry` `<boolean>` Whether an exception will be thrown if no file system entry exists, rather than returning `undefined`. **Default:** `true`.
- Returns: `<fs.Stats>`

Retrieves the `<fs.Stats>` for the symbolic link referred to by `path`.See the POSIX `lstat(2)` documentation for more details.

#### `fs.mkdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` | `<integer>`
  - `recursive` `<boolean>` **Default:** `false`
  - `mode` `<string>` | `<integer>` Not supported on Windows. **Default:** `0o777`.
- Returns: `<string>` | `<undefined>`

Synchronously creates a directory. Returns `undefined`, or if `recursive` is `true`, the first directory path created. This is the synchronous version of `fs.mkdir()`.See the POSIX `mkdir(2)` documentation for more details.

#### `fs.mkdtempSync(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>`

Returns the created directory path.For detailed information, see the documentation of the asynchronous version of this API: `fs.mkdtemp()`.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.

#### `fs.mkdtempDisposableSync(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Object>` A disposable object:
  - `path` `<string>` The path of the created directory.
  - `remove` `<Function>` A function which removes the created directory.
  - `[Symbol.dispose]` `<Function>` The same as `remove`.

Returns a disposable object whose `path` property holds the created directory path. When the object is disposed, the directory and its contents will be removed if it still exists. If the directory cannot be deleted, disposal will throw an error. The object has a `remove()` method which will perform the same task.For detailed information, see the documentation of `fs.mkdtemp()`.There is no callback-based version of this API because it is designed for use with the `using` syntax.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.

#### `fs.opendirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `bufferSize` `<number>` Number of directory entries that are buffered internally when reading from the directory. Higher values lead to better performance but higher memory usage. **Default:** `32`
  - `recursive` `<boolean>` **Default:** `false`
- Returns: `<fs.Dir>`

Synchronously open a directory. See `opendir(3)`.Creates an `<fs.Dir>`, which contains all further functions for reading from and cleaning up the directory.The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.

#### `fs.openSync(path[, flags[, mode]])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `flags` `<string>` | `<number>` **Default:** `'r'`. See support of file system `flags`.
- `mode` `<string>` | `<integer>` **Default:** `0o666`
- Returns: `<number>`

Returns an integer representing the file descriptor.For detailed information, see the documentation of the asynchronous version of this API: `fs.open()`.

#### `fs.readdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
  - `withFileTypes` `<boolean>` **Default:** `false`
  - `recursive` `<boolean>` If `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files, and directories. **Default:** `false`.
- Returns: `<string>`[] | `<Buffer>`[] | `<fs.Dirent>`[]

Reads the contents of the directory.See the POSIX `readdir(3)` documentation for more details.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames returned. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as `<Buffer>` objects.If `options.withFileTypes` is set to `true`, the result will contain `<fs.Dirent>` objects.

#### `fs.readFileSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<integer>` filename or file descriptor
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `null`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'r'`.
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<Function>` A buffer to read into, or a function called with the file size that returns the buffer.
- Returns: `<string>` | `<Buffer>`

Returns the contents of the `path`.For detailed information, see the documentation of the asynchronous version of this API: `fs.readFile()`.If the `encoding` option is specified then this function returns a string. Otherwise it returns a buffer.If `buffer` is provided and no encoding is specified, the returned `<Buffer>` is a view over the supplied buffer containing only the bytes read. If the supplied buffer is too small to contain the entire file, an error will be thrown.Similar to `fs.readFile()`, when the path is a directory, the behavior of `fs.readFileSync()` is platform-specific.`import { readFileSync } from 'node:fs'; // macOS, Linux, and Windows readFileSync('<directory>'); // => [Error: EISDIR: illegal operation on a directory, read <directory>] // FreeBSD readFileSync('<directory>'); // => <data>`

#### `fs.readlinkSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>` | `<Buffer>`

Returns the symbolic link's string value.See the POSIX `readlink(2)` documentation for more details.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path returned. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a `<Buffer>` object.

#### `fs.readSync(fd, buffer, offset, length[, position])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `offset` `<integer>`
- `length` `<integer>`
- `position` `<integer>` | `<bigint>` | `<null>` **Default:** `null`
- Returns: `<number>`

Returns the number of `bytesRead`.For detailed information, see the documentation of the asynchronous version of this API: `fs.read()`.

#### `fs.readSync(fd, buffer[, options])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` | `<null>` **Default:** `null`
- Returns: `<number>`

Returns the number of `bytesRead`.Similar to the above `fs.readSync` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.For detailed information, see the documentation of the asynchronous version of this API: `fs.read()`.

#### `fs.readvSync(fd, buffers[, position])`

- `fd` `<integer>`
- `buffers` {ArrayBufferView[]}
- `position` `<integer>` | `<null>` **Default:** `null`
- Returns: `<number>` The number of bytes read.

For detailed information, see the documentation of the asynchronous version of this API: `fs.readv()`.

#### `fs.realpathSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>` | `<Buffer>`

Returns the resolved pathname.For detailed information, see the documentation of the asynchronous version of this API: `fs.realpath()`.

#### `fs.realpathSync.native(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>` | `<Buffer>`

Synchronous `realpath(3)`.Only paths that can be converted to UTF8 strings are supported.The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path returned. If the `encoding` is set to `'buffer'`, the path returned will be passed as a `<Buffer>` object.On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.

#### `fs.renameSync(oldPath, newPath)`

- `oldPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`

Renames the file from `oldPath` to `newPath`. Returns `undefined`.See the POSIX `rename(2)` documentation for more details.

#### `fs.rmdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` There are currently no options exposed. There used to be options for `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.

Synchronous `rmdir(2)`. Returns `undefined`.Using `fs.rmdirSync()` on a file (not a directory) results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.To get a behavior similar to the `rm -rf` Unix command, use `fs.rmSync()` with options `{ recursive: true, force: true }`.

#### `fs.rmSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `force` `<boolean>` When `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
  - `maxRetries` `<integer>` If an `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
  - `recursive` `<boolean>` If `true`, perform a recursive directory removal. In recursive mode operations are retried on failure. **Default:** `false`.
  - `retryDelay` `<integer>` The amount of time in milliseconds to wait between retries. This option is ignored if the `recursive` option is not `true`. **Default:** `100`.

Synchronously removes files and directories (modeled on the standard POSIX `rm` utility). Returns `undefined`.

#### `fs.statSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
  - `throwIfNoEntry` `<boolean>` Whether an exception will be thrown if no file system entry exists, rather than returning `undefined`. **Default:** `true`.
- Returns: `<fs.Stats>`

Retrieves the `<fs.Stats>` for the path.

#### `fs.statfsSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.StatFs>` object should be `bigint`. **Default:** `false`.
- Returns: `<fs.StatFs>`

Synchronous `statfs(2)`. Returns information about the mounted file system which contains `path`.In case of an error, the `err.code` will be one of Common System Errors.

#### `fs.symlinkSync(target, path[, type])`

- `target` `<string>` | `<Buffer>` | `<URL>`
- `path` `<string>` | `<Buffer>` | `<URL>`
- `type` `<string>` | `<null>` **Default:** `null`
- Returns: `undefined`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.symlink()`.

#### `fs.truncateSync(path[, len])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `len` `<integer>` **Default:** `0`

Truncates the file. Returns `undefined`. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncateSync()` is called.Passing a file descriptor is deprecated and may result in an error being thrown in the future.

#### `fs.unlinkSync(path)`

- `path` `<string>` | `<Buffer>` | `<URL>`

Synchronous `unlink(2)`. Returns `undefined`.

#### `fs.utimesSync(path, atime, mtime)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `atime` `<number>` | `<string>` | `<Date>`
- `mtime` `<number>` | `<string>` | `<Date>`
- Returns: `undefined`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.utimes()`.

#### `fs.writeFileSync(file, data[, options])`

- `file` `<string>` | `<Buffer>` | `<URL>` | `<integer>` filename or file descriptor
- `data` `<string>` | `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'w'`.
  - `flush` `<boolean>` If all data is successfully written to the file, and `flush` is `true`, `fs.fsyncSync()` is used to flush the data.
- Returns: `undefined`.

The `mode` option only affects the newly created file. See `fs.open()` for more details.For detailed information, see the documentation of the asynchronous version of this API: `fs.writeFile()`.

#### `fs.writeSync(fd, buffer, offset[, length[, position]])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `offset` `<integer>` **Default:** `0`
- `length` `<integer>` **Default:** `buffer.byteLength - offset`
- `position` `<integer>` | `<null>` **Default:** `null`
- Returns: `<number>` The number of bytes written.

For detailed information, see the documentation of the asynchronous version of this API: `fs.write(fd, buffer...)`.

#### `fs.writeSync(fd, buffer[, options])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<null>` **Default:** `null`
- Returns: `<number>` The number of bytes written.

For detailed information, see the documentation of the asynchronous version of this API: `fs.write(fd, buffer...)`.

#### `fs.writeSync(fd, string[, position[, encoding]])`

- `fd` `<integer>`
- `string` `<string>`
- `position` `<integer>` | `<null>` **Default:** `null`
- `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<number>` The number of bytes written.

For detailed information, see the documentation of the asynchronous version of this API: `fs.write(fd, string...)`.

#### `fs.writevSync(fd, buffers[, position])`

- `fd` `<integer>`
- `buffers` {ArrayBufferView[]}
- `position` `<integer>` | `<null>` **Default:** `null`
- Returns: `<number>` The number of bytes written.

For detailed information, see the documentation of the asynchronous version of this API: `fs.writev()`.

### Common Objects

The common objects are shared by all of the file system API variants (promise, callback, and synchronous).

#### Class: `fs.Dir`

A class representing a directory stream.Created by `fs.opendir()`, `fs.opendirSync()`, or `fsPromises.opendir()`.`import { opendir } from 'node:fs/promises'; try { const dir = await opendir('./'); for await (const dirent of dir) console.log(dirent.name); } catch (err) { console.error(err); }`When using the async iterator, the `<fs.Dir>` object will be automatically closed after the iterator exits.

##### `dir.close()`

- Returns: `<Promise>`

Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.A promise is returned that will be fulfilled after the resource has been closed.

##### `dir.close(callback)`

- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.The `callback` will be called after the resource handle has been closed.

##### `dir.closeSync()`

Synchronously close the directory's underlying resource handle. Subsequent reads will result in errors.

##### `dir.path`

- Type: `<string>`

The read-only path of this directory as was provided to `fs.opendir()`, `fs.opendirSync()`, or `fsPromises.opendir()`.

##### `dir.read()`

- Returns: `<Promise>` Fulfills with a `<fs.Dirent>` | `<null>`

Asynchronously read the next directory entry via `readdir(3)` as an `<fs.Dirent>`.A promise is returned that will be fulfilled with an `<fs.Dirent>`, or `null` if there are no more directory entries to read.Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir.read(callback)`

- `callback` `<Function>`
  - `err` `<Error>`
  - `dirent` `<fs.Dirent>` | `<null>`

Asynchronously read the next directory entry via `readdir(3)` as an `<fs.Dirent>`.After the read is completed, the `callback` will be called with an `<fs.Dirent>`, or `null` if there are no more directory entries to read.Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir.readSync()`

- Returns: `<fs.Dirent>` | `<null>`

Synchronously read the next directory entry as an `<fs.Dirent>`. See the POSIX `readdir(3)` documentation for more detail.If there are no more directory entries to read, `null` will be returned.Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir[Symbol.asyncIterator]()`

- Returns: `<AsyncIterator>` An AsyncIterator of `<fs.Dirent>`

Asynchronously iterates over the directory until all entries have been read. Refer to the POSIX `readdir(3)` documentation for more detail.Entries returned by the async iterator are always an `<fs.Dirent>`. The `null` case from `dir.read()` is handled internally.See `<fs.Dir>` for an example.Directory entries returned by this iterator are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir[Symbol.asyncDispose]()`

Calls `dir.close()` if the directory handle is open, and returns a promise that fulfills when disposal is complete.

##### `dir[Symbol.dispose]()`

Calls `dir.closeSync()` if the directory handle is open, and returns `undefined`.

#### Class: `fs.Dirent`

A representation of a directory entry, which can be a file or a subdirectory within the directory, as returned by reading from an `<fs.Dir>`. The directory entry is a combination of the file name and file type pairs.Additionally, when `fs.readdir()` or `fs.readdirSync()` is called with the `withFileTypes` option set to `true`, the resulting array is filled with `<fs.Dirent>` objects, rather than strings or `<Buffer>`s.

##### `dirent.isBlockDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a block device.

##### `dirent.isCharacterDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a character device.

##### `dirent.isDirectory()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a file system directory.

##### `dirent.isFIFO()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a first-in-first-out (FIFO) pipe.

##### `dirent.isFile()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a regular file.

##### `dirent.isSocket()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a socket.

##### `dirent.isSymbolicLink()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a symbolic link.

##### `dirent.name`

- Type: `<string>` | `<Buffer>`

The file name that this `<fs.Dirent>` object refers to. The type of this value is determined by the `options.encoding` passed to `fs.readdir()` or `fs.readdirSync()`.

##### `dirent.parentPath`

- Type: `<string>`

The path to the parent directory of the file this `<fs.Dirent>` object refers to.

#### Class: `fs.FSWatcher`

- Extends `<EventEmitter>`

A successful call to `fs.watch()` method will return a new `<fs.FSWatcher>` object.All `<fs.FSWatcher>` objects emit a `'change'` event whenever a specific watched file is modified.

##### Event: `'change'`

- `eventType` `<string>` The type of change event that has occurred
- `filename` `<string>` | `<Buffer>` The filename that changed (if relevant/available)

Emitted when something changes in a watched directory or file. See more details in `fs.watch()`.The `filename` argument may not be provided depending on operating system support. If `filename` is provided, it will be provided as a `<Buffer>` if `fs.watch()` is called with its `encoding` option set to `'buffer'`, otherwise `filename` will be a UTF-8 string.`import { watch } from 'node:fs'; // Example when handled through fs.watch() listener watch('./tmp', { encoding: 'buffer' }, (eventType, filename) => { if (filename) { console.log(filename); // Prints: <Buffer ...> } });`

##### Event: `'close'`

Emitted when the watcher stops watching for changes. The closed `<fs.FSWatcher>` object is no longer usable in the event handler.

##### Event: `'error'`

- `error` `<Error>`

Emitted when an error occurs while watching the file. The errored `<fs.FSWatcher>` object is no longer usable in the event handler.

##### `watcher.close()`

Stop watching for changes on the given `<fs.FSWatcher>`. Once stopped, the `<fs.FSWatcher>` object is no longer usable.

##### `watcher.ref()`

- Returns: `<fs.FSWatcher>`

When called, requests that the Node.js event loop *not* exit so long as the `<fs.FSWatcher>` is active. Calling `watcher.ref()` multiple times will have no effect.By default, all `<fs.FSWatcher>` objects are "ref'ed", making it normally unnecessary to call `watcher.ref()` unless `watcher.unref()` had been called previously.

##### `watcher.unref()`

- Returns: `<fs.FSWatcher>`

When called, the active `<fs.FSWatcher>` object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the `<fs.FSWatcher>` object's callback is invoked. Calling `watcher.unref()` multiple times will have no effect.

#### Class: `fs.StatWatcher`

- Extends `<EventEmitter>`

A successful call to `fs.watchFile()` method will return a new `<fs.StatWatcher>` object.

##### `watcher.ref()`

- Returns: `<fs.StatWatcher>`

When called, requests that the Node.js event loop *not* exit so long as the `<fs.StatWatcher>` is active. Calling `watcher.ref()` multiple times will have no effect.By default, all `<fs.StatWatcher>` objects are "ref'ed", making it normally unnecessary to call `watcher.ref()` unless `watcher.unref()` had been called previously.

##### `watcher.unref()`

- Returns: `<fs.StatWatcher>`

When called, the active `<fs.StatWatcher>` object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the `<fs.StatWatcher>` object's callback is invoked. Calling `watcher.unref()` multiple times will have no effect.

#### Class: `fs.ReadStream`

- Extends: `<stream.Readable>`

Instances of `<fs.ReadStream>` cannot be constructed directly. They are created and returned using the `fs.createReadStream()` function.

##### Event: `'close'`

Emitted when the `<fs.ReadStream>`'s underlying file descriptor has been closed.

##### Event: `'open'`

- `fd` `<integer>` Integer file descriptor used by the `<fs.ReadStream>`.

Emitted when the `<fs.ReadStream>`'s file descriptor has been opened.

##### Event: `'ready'`

Emitted when the `<fs.ReadStream>` is ready to be used.Fires immediately after `'open'`.

##### `readStream.bytesRead`

- Type: `<number>`

The number of bytes that have been read so far.

##### `readStream.path`

- Type: `<string>` | `<Buffer>`

The path to the file the stream is reading from as specified in the first argument to `fs.createReadStream()`. If `path` is passed as a string, then `readStream.path` will be a string. If `path` is passed as a `<Buffer>`, then `readStream.path` will be a `<Buffer>`. If `fd` is specified, then `readStream.path` will be `undefined`.

##### `readStream.pending`

- Type: `<boolean>`

This property is `true` if the underlying file has not been opened yet, i.e. before the `'ready'` event is emitted.
