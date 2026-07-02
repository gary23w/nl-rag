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

The `listener` gets two arguments the current stat object and the previous stat object:import { watchFile } from 'node:fs'; watchFile('message.text', (curr, prev) => { console.log(`the current mtime is: ${curr.mtime}`); console.log(`the previous mtime was: ${prev.mtime}`); });

These stat objects are instances of `fs.Stat`. If the `bigint` option is `true`, the numeric values in these objects are specified as `BigInt`s.

To be notified when the file was modified, not just accessed, it is necessary to compare `curr.mtimeMs` and `prev.mtimeMs`.

When an `fs.watchFile` operation results in an `ENOENT` error, it will invoke the listener once, with all the fields zeroed (or, for dates, the Unix Epoch). If the file is created later on, the listener will be called again, with the latest stat objects. This is a change in functionality since v0.10.

Using `fs.watch()` is more efficient than `fs.watchFile` and `fs.unwatchFile`. `fs.watch` should be used instead of `fs.watchFile` and `fs.unwatchFile` when possible.

When a file being watched by `fs.watchFile()` disappears and reappears, then the contents of `previous` in the second callback event (the file's reappearance) will be the same as the contents of `previous` in the first callback event (its disappearance).

This happens when: the file is deleted, followed by a restore the file is renamed and then renamed a second time back to its original name

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

Write `buffer` to the file specified by `fd`.

`offset` determines the part of the buffer to be written, and `length` is an integer specifying the number of bytes to write.

`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position. See `pwrite(2)`.

The callback will be given three arguments `(err, bytesWritten, buffer)` where `bytesWritten` specifies how many *bytes* were written from `buffer`.

If this method is invoked as its `util.promisify()`ed version, it returns a promise for an `Object` with `bytesWritten` and `buffer` properties.

It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.

On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

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

Write `buffer` to the file specified by `fd`.

Similar to the above `fs.write` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

#### `fs.write(fd, string[, position[, encoding]], callback)`

- `fd` `<integer>`
- `string` `<string>`
- `position` `<integer>` | `<null>` **Default:** `null`
- `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
  - `err` `<Error>`
  - `written` `<integer>`
  - `string` `<string>`

Write `string` to the file specified by `fd`. If `string` is not a string, an exception is thrown.

`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'` the data will be written at the current position. See `pwrite(2)`.

`encoding` is the expected string encoding.

The callback will receive the arguments `(err, written, string)` where `written` specifies how many *bytes* the passed string required to be written. Bytes written is not necessarily the same as string characters written. See `Buffer.byteLength`.

It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.

On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

On Windows, if the file descriptor is connected to the console (e.g. `fd == 1` or `stdout`) a string containing non-ASCII characters will not be rendered properly by default, regardless of the encoding used. It is possible to configure the console to render UTF-8 properly by changing the active codepage with the `chcp 65001` command. See the chcp docs for more details.

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

When `file` is a filename, asynchronously writes data to the file, replacing the file if it already exists. `data` can be a string or a buffer.

When `file` is a file descriptor, the behavior is similar to calling `fs.write()` directly (which is recommended). See the notes below on using a file descriptor.

The `encoding` option is ignored if `data` is a buffer.

The `mode` option only affects the newly created file. See `fs.open()` for more details.`import { writeFile } from 'node:fs'; import { Buffer } from 'node:buffer'; const data = new Uint8Array(Buffer.from('Hello Node.js')); writeFile('message.txt', data, (err) => { if (err) throw err; console.log('The file has been saved!'); });`

If `options` is a string, then it specifies the encoding:`import { writeFile } from 'node:fs'; writeFile('message.txt', 'Hello Node.js', 'utf8', callback);`

It is unsafe to use `fs.writeFile()` multiple times on the same file without waiting for the callback. For this scenario, `fs.createWriteStream()` is recommended.

Similarly to `fs.readFile` - `fs.writeFile` is a convenience method that performs multiple `write` calls internally to write the buffer passed to it. For performance sensitive code consider using `fs.createWriteStream()`.

It is possible to use an `<AbortSignal>` to cancel an `fs.writeFile()`. Cancelation is "best effort", and some amount of data is likely still to be written.`import { writeFile } from 'node:fs'; import { Buffer } from 'node:buffer'; const controller = new AbortController(); const { signal } = controller; const data = new Uint8Array(Buffer.from('Hello Node.js')); writeFile('message.txt', data, { signal }, (err) => { // When a request is aborted - the callback is called with an AbortError }); // When the request should be aborted controller.abort();`

Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.writeFile` performs.

##### Using `fs.writeFile()` with file descriptors

When `file` is a file descriptor, the behavior is almost identical to directly calling `fs.write()` like:`import { write } from 'node:fs'; import { Buffer } from 'node:buffer'; write(fd, Buffer.from(data, options.encoding), callback);`

The difference from directly calling `fs.write()` is that under some unusual conditions, `fs.write()` might write only part of the buffer and need to be retried to write the remaining data, whereas `fs.writeFile()` retries until the data is entirely written (or an error occurs).

The implications of this are a common source of confusion. In the file descriptor case, the file is not replaced! The data is not necessarily written to the beginning of the file, and the file's original data may remain before and/or after the newly written data.

For example, if `fs.writeFile()` is called twice in a row, first to write the string `'Hello'`, then to write the string `', World'`, the file would contain `'Hello, World'`, and might contain some of the file's original data (depending on the size of the original file, and the position of the file descriptor). If a file name had been used instead of a descriptor, the file would be guaranteed to contain only `', World'`.

#### `fs.writev(fd, buffers[, position], callback)`

- `fd` `<integer>`
- `buffers` {ArrayBufferView[]}
- `position` `<integer>` | `<null>` **Default:** `null`
- `callback` `<Function>`
  - `err` `<Error>`
  - `bytesWritten` `<integer>`
  - `buffers` {ArrayBufferView[]}

Write an array of `ArrayBufferView`s to the file specified by `fd` using `writev()`.

`position` is the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position.

The callback will be given three arguments: `err`, `bytesWritten`, and `buffers`. `bytesWritten` is how many bytes were written from `buffers`.

If this method is `util.promisify()`ed, it returns a promise for an `Object` with `bytesWritten` and `buffers` properties.

It is unsafe to use `fs.writev()` multiple times on the same file without waiting for the callback. For this scenario, use `fs.createWriteStream()`.

On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.

### Synchronous API

The synchronous APIs perform all operations synchronously, blocking the event loop until the operation completes or fails.

#### `fs.accessSync(path[, mode])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<integer>` **Default:** `fs.constants.F_OK`

Synchronously tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check File access constants for possible values of `mode`.

If any of the accessibility checks fail, an `Error` will be thrown. Otherwise, the method will return `undefined`.`import { accessSync, constants } from 'node:fs'; try { accessSync('etc/passwd', constants.R_OK | constants.W_OK); console.log('can read/write'); } catch (err) { console.error('no access!'); }`

#### `fs.appendFileSync(path, data[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<number>` filename or file descriptor
- `data` `<string>` | `<Buffer>`
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `mode` `<integer>` **Default:** `0o666`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'a'`.
  - `flush` `<boolean>` If `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.

Synchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `<Buffer>`.

The `mode` option only affects the newly created file. See `fs.open()` for more details.`import { appendFileSync } from 'node:fs'; try { appendFileSync('message.txt', 'data to append'); console.log('The "data to append" was appended to file!'); } catch (err) { /* Handle the error */ }`

If `options` is a string, then it specifies the encoding:`import { appendFileSync } from 'node:fs'; appendFileSync('message.txt', 'data to append', 'utf8');`

The `path` may be specified as a numeric file descriptor that has been opened for appending (using `fs.open()` or `fs.openSync()`). The file descriptor will not be closed automatically.`import { openSync, closeSync, appendFileSync } from 'node:fs'; let fd; try { fd = openSync('message.txt', 'a'); appendFileSync(fd, 'data to append', 'utf8'); } catch (err) { /* Handle the error */ } finally { if (fd !== undefined) closeSync(fd); }`

#### `fs.chmodSync(path, mode)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `mode` `<string>` | `<integer>`

For detailed information, see the documentation of the asynchronous version of this API: `fs.chmod()`.

See the POSIX `chmod(2)` documentation for more detail.

#### `fs.chownSync(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>`
- `gid` `<integer>`

Synchronously changes owner and group of a file. Returns `undefined`. This is the synchronous version of `fs.chown()`.

See the POSIX `chown(2)` documentation for more detail.

#### `fs.closeSync(fd)`

- `fd` `<integer>`

Closes the file descriptor. Returns `undefined`.

Calling `fs.closeSync()` on any file descriptor (`fd`) that is currently in use through any other `fs` operation may lead to undefined behavior.

See the POSIX `close(2)` documentation for more detail.

#### `fs.copyFileSync(src, dest[, mode])`

- `src` `<string>` | `<Buffer>` | `<URL>` source filename to copy
- `dest` `<string>` | `<Buffer>` | `<URL>` destination filename of the copy operation
- `mode` `<integer>` modifiers for copy operation. **Default:** `0`.

Synchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. Returns `undefined`. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.

`mode` is an optional integer that specifies the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`). `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists. `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used. `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail. `import { copyFileSync, constants } from 'node:fs'; // destination.txt will be created or overwritten by default. copyFileSync('source.txt', 'destination.txt'); console.log('source.txt was copied to destination.txt'); // By using COPYFILE_EXCL, the operation will fail if destination.txt exists. copyFileSync('source.txt', 'destination.txt', constants.COPYFILE_EXCL);`

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

Synchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.

#### `fs.existsSync(path)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- Returns: `<boolean>`

Returns `true` if the path exists, `false` otherwise.

For detailed information, see the documentation of the asynchronous version of this API: `fs.exists()`.

`fs.exists()` is deprecated, but `fs.existsSync()` is not. The `callback` parameter to `fs.exists()` accepts parameters that are inconsistent with other Node.js callbacks. `fs.existsSync()` does not use a callback.`import { existsSync } from 'node:fs'; if (existsSync('/etc/passwd')) console.log('The path exists.');`

#### `fs.fchmodSync(fd, mode)`

- `fd` `<integer>`
- `mode` `<string>` | `<integer>`

Sets the permissions on the file. Returns `undefined`.

See the POSIX `fchmod(2)` documentation for more detail.

#### `fs.fchownSync(fd, uid, gid)`

- `fd` `<integer>`
- `uid` `<integer>` The file's new owner's user id.
- `gid` `<integer>` The file's new group's group id.

Sets the owner of the file. Returns `undefined`.

See the POSIX `fchown(2)` documentation for more detail.

#### `fs.fdatasyncSync(fd)`

- `fd` `<integer>`

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX `fdatasync(2)` documentation for details. Returns `undefined`.

#### `fs.fstatSync(fd[, options])`

- `fd` `<integer>`
- `options` `<Object>`
  - `bigint` `<boolean>` Whether the numeric values in the returned `<fs.Stats>` object should be `bigint`. **Default:** `false`.
- Returns: `<fs.Stats>`

Retrieves the `<fs.Stats>` for the file descriptor.

See the POSIX `fstat(2)` documentation for more detail.

#### `fs.fsyncSync(fd)`

- `fd` `<integer>`

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX `fsync(2)` documentation for more detail. Returns `undefined`.

#### `fs.ftruncateSync(fd[, len])`

- `fd` `<integer>`
- `len` `<integer>` **Default:** `0`

Truncates the file descriptor. Returns `undefined`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.ftruncate()`.

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

Changes the permissions on a symbolic link. Returns `undefined`.

This method is only implemented on macOS.

See the POSIX `lchmod(2)` documentation for more detail.

#### `fs.lchownSync(path, uid, gid)`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `uid` `<integer>` The file's new owner's user id.
- `gid` `<integer>` The file's new group's group id.

Set the owner for the path. Returns `undefined`.

See the POSIX `lchown(2)` documentation for more details.

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

Retrieves the `<fs.Stats>` for the symbolic link referred to by `path`.

See the POSIX `lstat(2)` documentation for more details.

#### `fs.mkdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` | `<integer>`
  - `recursive` `<boolean>` **Default:** `false`
  - `mode` `<string>` | `<integer>` Not supported on Windows. **Default:** `0o777`.
- Returns: `<string>` | `<undefined>`

Synchronously creates a directory. Returns `undefined`, or if `recursive` is `true`, the first directory path created. This is the synchronous version of `fs.mkdir()`.

See the POSIX `mkdir(2)` documentation for more details.

#### `fs.mkdtempSync(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>`

Returns the created directory path.

For detailed information, see the documentation of the asynchronous version of this API: `fs.mkdtemp()`.

The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.

#### `fs.mkdtempDisposableSync(prefix[, options])`

- `prefix` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<Object>` A disposable object:
  - `path` `<string>` The path of the created directory.
  - `remove` `<Function>` A function which removes the created directory.
  - `[Symbol.dispose]` `<Function>` The same as `remove`.

Returns a disposable object whose `path` property holds the created directory path. When the object is disposed, the directory and its contents will be removed if it still exists. If the directory cannot be deleted, disposal will throw an error. The object has a `remove()` method which will perform the same task.

For detailed information, see the documentation of `fs.mkdtemp()`.

There is no callback-based version of this API because it is designed for use with the `using` syntax.

The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.

#### `fs.opendirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>`
  - `encoding` `<string>` | `<null>` **Default:** `'utf8'`
  - `bufferSize` `<number>` Number of directory entries that are buffered internally when reading from the directory. Higher values lead to better performance but higher memory usage. **Default:** `32`
  - `recursive` `<boolean>` **Default:** `false`
- Returns: `<fs.Dir>`

Synchronously open a directory. See `opendir(3)`.

Creates an `<fs.Dir>`, which contains all further functions for reading from and cleaning up the directory.

The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.

#### `fs.openSync(path[, flags[, mode]])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `flags` `<string>` | `<number>` **Default:** `'r'`. See support of file system `flags`.
- `mode` `<string>` | `<integer>` **Default:** `0o666`
- Returns: `<number>`

Returns an integer representing the file descriptor.

For detailed information, see the documentation of the asynchronous version of this API: `fs.open()`.

#### `fs.readdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
  - `withFileTypes` `<boolean>` **Default:** `false`
  - `recursive` `<boolean>` If `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files, and directories. **Default:** `false`.
- Returns: `<string>`[] | `<Buffer>`[] | `<fs.Dirent>`[]

Reads the contents of the directory.

See the POSIX `readdir(3)` documentation for more details.

The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames returned. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as `<Buffer>` objects.

If `options.withFileTypes` is set to `true`, the result will contain `<fs.Dirent>` objects.

#### `fs.readFileSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>` | `<integer>` filename or file descriptor
- `options` `<Object>` | `<string>`
  - `encoding` `<string>` | `<null>` **Default:** `null`
  - `flag` `<string>` See support of file system `flags`. **Default:** `'r'`.
  - `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>` | `<Function>` A buffer to read into, or a function called with the file size that returns the buffer.
- Returns: `<string>` | `<Buffer>`

Returns the contents of the `path`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.readFile()`.

If the `encoding` option is specified then this function returns a string. Otherwise it returns a buffer.

If `buffer` is provided and no encoding is specified, the returned `<Buffer>` is a view over the supplied buffer containing only the bytes read. If the supplied buffer is too small to contain the entire file, an error will be thrown.

Similar to `fs.readFile()`, when the path is a directory, the behavior of `fs.readFileSync()` is platform-specific.`import { readFileSync } from 'node:fs'; // macOS, Linux, and Windows readFileSync('<directory>'); // => [Error: EISDIR: illegal operation on a directory, read <directory>] // FreeBSD readFileSync('<directory>'); // => <data>`

#### `fs.readlinkSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>` | `<Buffer>`

Returns the symbolic link's string value.

See the POSIX `readlink(2)` documentation for more details.

The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path returned. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a `<Buffer>` object.

#### `fs.readSync(fd, buffer, offset, length[, position])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `offset` `<integer>`
- `length` `<integer>`
- `position` `<integer>` | `<bigint>` | `<null>` **Default:** `null`
- Returns: `<number>`

Returns the number of `bytesRead`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.read()`.

#### `fs.readSync(fd, buffer[, options])`

- `fd` `<integer>`
- `buffer` `<Buffer>` | `<TypedArray>` | `<DataView>`
- `options` `<Object>`
  - `offset` `<integer>` **Default:** `0`
  - `length` `<integer>` **Default:** `buffer.byteLength - offset`
  - `position` `<integer>` | `<bigint>` | `<null>` **Default:** `null`
- Returns: `<number>`

Returns the number of `bytesRead`.

Similar to the above `fs.readSync` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.

For detailed information, see the documentation of the asynchronous version of this API: `fs.read()`.

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

Returns the resolved pathname.

For detailed information, see the documentation of the asynchronous version of this API: `fs.realpath()`.

#### `fs.realpathSync.native(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<string>` | `<Object>`
  - `encoding` `<string>` **Default:** `'utf8'`
- Returns: `<string>` | `<Buffer>`

Synchronous `realpath(3)`.

Only paths that can be converted to UTF8 strings are supported.

The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path returned. If the `encoding` is set to `'buffer'`, the path returned will be passed as a `<Buffer>` object.

On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.

#### `fs.renameSync(oldPath, newPath)`

- `oldPath` `<string>` | `<Buffer>` | `<URL>`
- `newPath` `<string>` | `<Buffer>` | `<URL>`

Renames the file from `oldPath` to `newPath`. Returns `undefined`.

See the POSIX `rename(2)` documentation for more details.

#### `fs.rmdirSync(path[, options])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `options` `<Object>` There are currently no options exposed. There used to be options for `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.

Synchronous `rmdir(2)`. Returns `undefined`.

Using `fs.rmdirSync()` on a file (not a directory) results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.

To get a behavior similar to the `rm -rf` Unix command, use `fs.rmSync()` with options `{ recursive: true, force: true }`.

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

Synchronous `statfs(2)`. Returns information about the mounted file system which contains `path`.

In case of an error, the `err.code` will be one of Common System Errors.

#### `fs.symlinkSync(target, path[, type])`

- `target` `<string>` | `<Buffer>` | `<URL>`
- `path` `<string>` | `<Buffer>` | `<URL>`
- `type` `<string>` | `<null>` **Default:** `null`
- Returns: `undefined`.

For detailed information, see the documentation of the asynchronous version of this API: `fs.symlink()`.

#### `fs.truncateSync(path[, len])`

- `path` `<string>` | `<Buffer>` | `<URL>`
- `len` `<integer>` **Default:** `0`

Truncates the file. Returns `undefined`. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncateSync()` is called.

Passing a file descriptor is deprecated and may result in an error being thrown in the future.

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

The `mode` option only affects the newly created file. See `fs.open()` for more details.

For detailed information, see the documentation of the asynchronous version of this API: `fs.writeFile()`.

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

A class representing a directory stream.

Created by `fs.opendir()`, `fs.opendirSync()`, or `fsPromises.opendir()`.`import { opendir } from 'node:fs/promises'; try { const dir = await opendir('./'); for await (const dirent of dir) console.log(dirent.name); } catch (err) { console.error(err); }`

When using the async iterator, the `<fs.Dir>` object will be automatically closed after the iterator exits.

##### `dir.close()`

- Returns: `<Promise>`

Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.

A promise is returned that will be fulfilled after the resource has been closed.

##### `dir.close(callback)`

- `callback` `<Function>`
  - `err` `<Error>`

Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.

The `callback` will be called after the resource handle has been closed.

##### `dir.closeSync()`

Synchronously close the directory's underlying resource handle. Subsequent reads will result in errors.

##### `dir.path`

- Type: `<string>`

The read-only path of this directory as was provided to `fs.opendir()`, `fs.opendirSync()`, or `fsPromises.opendir()`.

##### `dir.read()`

- Returns: `<Promise>` Fulfills with a `<fs.Dirent>` | `<null>`

Asynchronously read the next directory entry via `readdir(3)` as an `<fs.Dirent>`.

A promise is returned that will be fulfilled with an `<fs.Dirent>`, or `null` if there are no more directory entries to read.

Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir.read(callback)`

- `callback` `<Function>`
  - `err` `<Error>`
  - `dirent` `<fs.Dirent>` | `<null>`

Asynchronously read the next directory entry via `readdir(3)` as an `<fs.Dirent>`.

After the read is completed, the `callback` will be called with an `<fs.Dirent>`, or `null` if there are no more directory entries to read.

Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir.readSync()`

- Returns: `<fs.Dirent>` | `<null>`

Synchronously read the next directory entry as an `<fs.Dirent>`. See the POSIX `readdir(3)` documentation for more detail.

If there are no more directory entries to read, `null` will be returned.

Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir[Symbol.asyncIterator]()`

- Returns: `<AsyncIterator>` An AsyncIterator of `<fs.Dirent>`

Asynchronously iterates over the directory until all entries have been read. Refer to the POSIX `readdir(3)` documentation for more detail.

Entries returned by the async iterator are always an `<fs.Dirent>`. The `null` case from `dir.read()` is handled internally.

See `<fs.Dir>` for an example.

Directory entries returned by this iterator are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.

##### `dir[Symbol.asyncDispose]()`

Calls `dir.close()` if the directory handle is open, and returns a promise that fulfills when disposal is complete.

##### `dir[Symbol.dispose]()`

Calls `dir.closeSync()` if the directory handle is open, and returns `undefined`.

#### Class: `fs.Dirent`

A representation of a directory entry, which can be a file or a subdirectory within the directory, as returned by reading from an `<fs.Dir>`. The directory entry is a combination of the file name and file type pairs.

Additionally, when `fs.readdir()` or `fs.readdirSync()` is called with the `withFileTypes` option set to `true`, the resulting array is filled with `<fs.Dirent>` objects, rather than strings or `<Buffer>`s.

##### `dirent.isBlockDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a block device.

##### `dirent.isCharacterDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Dirent>` object describes a character device.
