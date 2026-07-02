---
title: "File system (part 3/3)"
source: https://nodejs.org/api/fs.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 3/3
---

#### Class: `fs.Stats`

A `<fs.Stats>` object provides information about a file.Objects returned from `fs.stat()`, `fs.lstat()`, `fs.fstat()`, and their synchronous counterparts are of this type. If `bigint` in the `options` passed to those methods is true, the numeric values will be `bigint` instead of `number`, and the object will contain additional nanosecond-precision properties suffixed with `Ns`. `Stat` objects are not to be created directly using the `new` keyword.`Stats { dev: 2114, ino: 48064969, mode: 33188, nlink: 1, uid: 85, gid: 100, rdev: 0, size: 527, blksize: 4096, blocks: 8, atimeMs: 1318289051000.1, mtimeMs: 1318289051000.1, ctimeMs: 1318289051000.1, birthtimeMs: 1318289051000.1, // Instances of Date atime: Mon, 10 Oct 2011 23:24:11 GMT, mtime: Mon, 10 Oct 2011 23:24:11 GMT, ctime: Mon, 10 Oct 2011 23:24:11 GMT, birthtime: Mon, 10 Oct 2011 23:24:11 GMT, // Instances of Temporal.Instant atimeInstant: 2011-10-10T23:24:11.0001Z, mtimeInstant: 2011-10-10T23:24:11.0001Z, ctimeInstant: 2011-10-10T23:24:11.0001Z, birthtimeInstant: 2011-10-10T23:24:11.0001Z }``bigint` version:`BigIntStats { dev: 2114n, ino: 48064969n, mode: 33188n, nlink: 1n, uid: 85n, gid: 100n, rdev: 0n, size: 527n, blksize: 4096n, blocks: 8n, atimeMs: 1318289051000n, mtimeMs: 1318289051000n, ctimeMs: 1318289051000n, birthtimeMs: 1318289051000n, atimeNs: 1318289051000000000n, mtimeNs: 1318289051000000000n, ctimeNs: 1318289051000000000n, birthtimeNs: 1318289051000000000n, // Instances of Date atime: Mon, 10 Oct 2011 23:24:11 GMT, mtime: Mon, 10 Oct 2011 23:24:11 GMT, ctime: Mon, 10 Oct 2011 23:24:11 GMT, birthtime: Mon, 10 Oct 2011 23:24:11 GMT, // Instances of Temporal.Instant atimeInstant: 2011-10-10T23:24:11Z, mtimeInstant: 2011-10-10T23:24:11Z, ctimeInstant: 2011-10-10T23:24:11Z, birthtimeInstant: 2011-10-10T23:24:11Z }`

##### `stats.isBlockDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a block device.

##### `stats.isCharacterDevice()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a character device.

##### `stats.isDirectory()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a file system directory.If the `<fs.Stats>` object was obtained from calling `fs.lstat()` on a symbolic link which resolves to a directory, this method will return `false`. This is because `fs.lstat()` returns information about a symbolic link itself and not the path it resolves to.

##### `stats.isFIFO()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a first-in-first-out (FIFO) pipe.

##### `stats.isFile()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a regular file.

##### `stats.isSocket()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a socket.

##### `stats.isSymbolicLink()`

- Returns: `<boolean>`

Returns `true` if the `<fs.Stats>` object describes a symbolic link.This method is only valid when using `fs.lstat()`.

##### `stats.dev`

- Type: `<number>` | `<bigint>`

The numeric identifier of the device containing the file.

##### `stats.ino`

- Type: `<number>` | `<bigint>`

The file system specific "Inode" number for the file.

##### `stats.mode`

- Type: `<number>` | `<bigint>`

A bit-field describing the file type and mode.

##### `stats.nlink`

- Type: `<number>` | `<bigint>`

The number of hard-links that exist for the file.

##### `stats.uid`

- Type: `<number>` | `<bigint>`

The numeric user identifier of the user that owns the file (POSIX).

##### `stats.gid`

- Type: `<number>` | `<bigint>`

The numeric group identifier of the group that owns the file (POSIX).

##### `stats.rdev`

- Type: `<number>` | `<bigint>`

A numeric device identifier if the file represents a device.

##### `stats.size`

- Type: `<number>` | `<bigint>`

The size of the file in bytes.If the underlying file system does not support getting the size of the file, this will be `0`.

##### `stats.blksize`

- Type: `<number>` | `<bigint>`

The file system block size for i/o operations.

##### `stats.blocks`

- Type: `<number>` | `<bigint>`

The number of blocks allocated for this file.

##### `stats.atimeMs`

- Type: `<number>` | `<bigint>`

The timestamp indicating the last time this file was accessed expressed in milliseconds since the POSIX Epoch.

##### `stats.mtimeMs`

- Type: `<number>` | `<bigint>`

The timestamp indicating the last time this file was modified expressed in milliseconds since the POSIX Epoch.

##### `stats.ctimeMs`

- Type: `<number>` | `<bigint>`

The timestamp indicating the last time the file status was changed expressed in milliseconds since the POSIX Epoch.

##### `stats.birthtimeMs`

- Type: `<number>` | `<bigint>`

The timestamp indicating the creation time of this file expressed in milliseconds since the POSIX Epoch.

##### `stats.atimeNs`

- Type: `<bigint>`

Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time this file was accessed expressed in nanoseconds since the POSIX Epoch.

##### `stats.mtimeNs`

- Type: `<bigint>`

Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time this file was modified expressed in nanoseconds since the POSIX Epoch.

##### `stats.ctimeNs`

- Type: `<bigint>`

Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time the file status was changed expressed in nanoseconds since the POSIX Epoch.

##### `stats.birthtimeNs`

- Type: `<bigint>`

Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the creation time of this file expressed in nanoseconds since the POSIX Epoch.

##### `stats.atime`

- Type: `<Date>`

The timestamp indicating the last time this file was accessed.

##### `stats.mtime`

- Type: `<Date>`

The timestamp indicating the last time this file was modified.

##### `stats.ctime`

- Type: `<Date>`

The timestamp indicating the last time the file status was changed.

##### `stats.birthtime`

- Type: `<Date>`

The timestamp indicating the creation time of this file.

##### Stat time values

The `atimeMs`, `mtimeMs`, `ctimeMs`, `birthtimeMs` properties are numeric values that hold the corresponding times in milliseconds. Their precision is platform specific. When `bigint: true` is passed into the method that generates the object, the properties will be bigints, otherwise they will be numbers.The `atimeNs`, `mtimeNs`, `ctimeNs`, `birthtimeNs` properties are bigints that hold the corresponding times in nanoseconds. They are only present when `bigint: true` is passed into the method that generates the object. Their precision is platform specific.`atime`, `mtime`, `ctime`, and `birthtime` are `Date` object alternate representations of the various times. The `Date` and number values are not connected. Assigning a new number value, or mutating the `Date` value, will not be reflected in the corresponding alternate representation.The times in the stat object have the following semantics: `atime` "Access Time": Time when file data last accessed. Changed by the `mknod(2)`, `utimes(2)`, and `read(2)` system calls. `mtime` "Modified Time": Time when file data last modified. Changed by the `mknod(2)`, `utimes(2)`, and `write(2)` system calls. `ctime` "Change Time": Time when file status was last changed (inode data modification). Changed by the `chmod(2)`, `chown(2)`, `link(2)`, `mknod(2)`, `rename(2)`, `unlink(2)`, `utimes(2)`, `read(2)`, and `write(2)` system calls. `birthtime` "Birth Time": Time of file creation. Set once when the file is created. On file systems where birthtime is not available, this field may instead hold either the `ctime` or `1970-01-01T00:00Z` (ie, Unix epoch timestamp `0`). This value may be greater than `atime` or `mtime` in this case. On Darwin and other FreeBSD variants, also set if the `atime` is explicitly set to an earlier value than the current `birthtime` using the `utimes(2)` system call. Prior to Node.js 0.12, the `ctime` held the `birthtime` on Windows systems. As of 0.12, `ctime` is not "creation time", and on Unix systems, it never was.

#### Class: `fs.StatFs`

Provides information about a mounted file system.Objects returned from `fs.statfs()` and its synchronous counterpart are of this type. If `bigint` in the `options` passed to those methods is `true`, the numeric values will be `bigint` instead of `number`.`StatFs { type: 1397114950, bsize: 4096, frsize: 4096, blocks: 121938943, bfree: 61058895, bavail: 61058895, files: 999, ffree: 1000000 }``bigint` version:`StatFs { type: 1397114950n, bsize: 4096n, frsize: 4096n, blocks: 121938943n, bfree: 61058895n, bavail: 61058895n, files: 999n, ffree: 1000000n }`

##### `statfs.bavail`

- Type: `<number>` | `<bigint>`

Free blocks available to unprivileged users. Multiply by `statfs.bsize` to get the number of available bytes.import { statfs } from 'node:fs/promises'; const stats = await statfs('/'); const availableBytes = stats.bsize * stats.bavail; console.log(`Available space: ${availableBytes} bytes`);const { statfs } = require('node:fs/promises'); (async () => { const stats = await statfs('/'); const availableBytes = stats.bsize * stats.bavail; console.log(`Available space: ${availableBytes} bytes`); })();

##### `statfs.bfree`

- Type: `<number>` | `<bigint>`

Free blocks in file system. Multiply by `statfs.bsize` to get the number of free bytes.import { statfs } from 'node:fs/promises'; const stats = await statfs('/'); const freeBytes = stats.bsize * stats.bfree; console.log(`Free space: ${freeBytes} bytes`);const { statfs } = require('node:fs/promises'); (async () => { const stats = await statfs('/'); const freeBytes = stats.bsize * stats.bfree; console.log(`Free space: ${freeBytes} bytes`); })();

##### `statfs.blocks`

- Type: `<number>` | `<bigint>`

Total data blocks in file system. Multiply by `statfs.bsize` to get the total size in bytes.import { statfs } from 'node:fs/promises'; const stats = await statfs('/'); const totalBytes = stats.bsize * stats.blocks; console.log(`Total space: ${totalBytes} bytes`);const { statfs } = require('node:fs/promises'); (async () => { const stats = await statfs('/'); const totalBytes = stats.bsize * stats.blocks; console.log(`Total space: ${totalBytes} bytes`); })();

##### `statfs.bsize`

- Type: `<number>` | `<bigint>`

Optimal transfer block size in bytes.

##### `statfs.frsize`

- Type: `<number>` | `<bigint>`

Fundamental file system block size.

##### `statfs.ffree`

- Type: `<number>` | `<bigint>`

Free file nodes in file system.

##### `statfs.files`

- Type: `<number>` | `<bigint>`

Total file nodes in file system.

##### `statfs.type`

- Type: `<number>` | `<bigint>`

Type of file system. A platform-specific numeric identifier for the type of file system. This value corresponds to the `f_type` field returned by `statfs(2)` on POSIX systems (for example, `0xEF53` for ext4 on Linux). Its meaning is OS-dependent and is not guaranteed to be consistent across platforms.

#### Class: `fs.Utf8Stream`

Stability: 1 - Experimental

An optimized UTF-8 stream writer that allows for flushing all the internal buffering on demand. It handles `EAGAIN` errors correctly, allowing for customization, for example, by dropping content if the disk is busy.

##### Event: `'close'`

The `'close'` event is emitted when the stream is fully closed.

##### Event: `'drain'`

The `'drain'` event is emitted when the internal buffer has drained sufficiently to allow continued writing.

##### Event: `'drop'`

The `'drop'` event is emitted when the maximal length is reached and that data will not be written. The data that was dropped is passed as the first argument to the event handler.

##### Event: `'error'`

The `'error'` event is emitted when an error occurs.

##### Event: `'finish'`

The `'finish'` event is emitted when the stream has been ended and all data has been flushed to the underlying file.

##### Event: `'ready'`

The `'ready'` event is emitted when the stream is ready to accept writes.

##### Event: `'write'`

The `'write'` event is emitted when a write operation has completed. The number of bytes written is passed as the first argument to the event handler.

##### `new fs.Utf8Stream([options])`

- `options` `<Object>`
  - `append`: `<boolean>` Appends writes to dest file instead of truncating it. **Default**: `true`.
  - `contentMode`: `<string>` Which type of data you can send to the write function, supported values are `'utf8'` or `'buffer'`. **Default**: `'utf8'`.
  - `dest`: `<string>` A path to a file to be written to (mode controlled by the append option).
  - `fd`: `<number>` A file descriptor, something that is returned by `fs.open()` or `fs.openSync()`.
  - `fs`: `<Object>` An object that has the same API as the `fs` module, useful for mocking, testing, or customizing the behavior of the stream.
  - `fsync`: `<boolean>` Perform a `fs.fsyncSync()` every time a write is completed.
  - `maxLength`: `<number>` The maximum length of the internal buffer. If a write operation would cause the buffer to exceed `maxLength`, the data written is dropped and a drop event is emitted with the dropped data
  - `maxWrite`: `<number>` The maximum number of bytes that can be written; **Default**: `16384`
  - `minLength`: `<number>` The minimum length of the internal buffer that is required to be full before flushing.
  - `mkdir`: `<boolean>` Ensure directory for `dest` file exists when true. **Default**: `false`.
  - `mode`: `<number>` | `<string>` Specify the creating file mode (see `fs.open()`).
  - `periodicFlush`: `<number>` Calls flush every `periodicFlush` milliseconds.
  - `retryEAGAIN` `<Function>` A function that will be called when `write()`, `writeSync()`, or `flushSync()` encounters an `EAGAIN` or `EBUSY` error. If the return value is `true` the operation will be retried, otherwise it will bubble the error. The `err` is the error that caused this function to be called, `writeBufferLen` is the length of the buffer that was written, and `remainingBufferLen` is the length of the remaining buffer that the stream did not try to write.
    - `err` `<any>` An error or `null`.
    - `writeBufferLen` `<number>`
    - `remainingBufferLen`: `<number>`
  - `sync`: `<boolean>` Perform writes synchronously.

##### `utf8Stream.append`

- `<boolean>` Whether the stream is appending to the file or truncating it.

##### `utf8Stream.contentMode`

- `<string>` The type of data that can be written to the stream. Supported values are `'utf8'` or `'buffer'`. **Default**: `'utf8'`.

##### `utf8Stream.destroy()`

Close the stream immediately, without flushing the internal buffer.

##### `utf8Stream.end()`

Close the stream gracefully, flushing the internal buffer before closing.

##### `utf8Stream.fd`

- `<number>` The file descriptor that is being written to.

##### `utf8Stream.file`

- `<string>` The file that is being written to.

##### `utf8Stream.flush(callback)`

- `callback` `<Function>`
  - `err` `<Error>` | `<null>` An error if the flush failed, otherwise `null`.

Writes the current buffer to the file if a write was not in progress. Do nothing if `minLength` is zero or if it is already writing.

##### `utf8Stream.flushSync()`

Flushes the buffered data synchronously. This is a costly operation.

##### `utf8Stream.fsync`

- `<boolean>` Whether the stream is performing a `fs.fsyncSync()` after every write operation.

##### `utf8Stream.maxLength`

- `<number>` The maximum length of the internal buffer. If a write operation would cause the buffer to exceed `maxLength`, the data written is dropped and a drop event is emitted with the dropped data.

##### `utf8Stream.minLength`

- `<number>` The minimum length of the internal buffer that is required to be full before flushing.

##### `utf8Stream.mkdir`

- `<boolean>` Whether the stream should ensure that the directory for the `dest` file exists. If `true`, it will create the directory if it does not exist. **Default**: `false`.

##### `utf8Stream.mode`

- `<number>` | `<string>` The mode of the file that is being written to.

##### `utf8Stream.periodicFlush`

- `<number>` The number of milliseconds between flushes. If set to `0`, no periodic flushes will be performed.

##### `utf8Stream.reopen(file)`

- `file`: `<string>` | `<Buffer>` | `<URL>` A path to a file to be written to (mode controlled by the append option).

Reopen the file in place, useful for log rotation.

##### `utf8Stream.sync`

- `<boolean>` Whether the stream is writing synchronously or asynchronously.

##### `utf8Stream.write(data)`

- `data` `<string>` | `<Buffer>` The data to write.
- Returns `<boolean>`

When the `options.contentMode` is set to `'utf8'` when the stream is created, the `data` argument must be a string. If the `contentMode` is set to `'buffer'`, the `data` argument must be a `<Buffer>`.

##### `utf8Stream.writing`

- `<boolean>` Whether the stream is currently writing data to the file.

##### `utf8Stream[Symbol.dispose]()`

Calls `utf8Stream.destroy()`.

#### Class: `fs.WriteStream`

- Extends `<stream.Writable>`

Instances of `<fs.WriteStream>` cannot be constructed directly. They are created and returned using the `fs.createWriteStream()` function.

##### Event: `'close'`

Emitted when the `<fs.WriteStream>`'s underlying file descriptor has been closed.

##### Event: `'open'`

- `fd` `<integer>` Integer file descriptor used by the `<fs.WriteStream>`.

Emitted when the `<fs.WriteStream>`'s file is opened.

##### Event: `'ready'`

Emitted when the `<fs.WriteStream>` is ready to be used.Fires immediately after `'open'`.

##### `writeStream.bytesWritten`

The number of bytes written so far. Does not include data that is still queued for writing.

##### `writeStream.close([callback])`

- `callback` `<Function>`
  - `err` `<Error>`

Closes `writeStream`. Optionally accepts a callback that will be executed once the `writeStream` is closed.

##### `writeStream.path`

The path to the file the stream is writing to as specified in the first argument to `fs.createWriteStream()`. If `path` is passed as a string, then `writeStream.path` will be a string. If `path` is passed as a `<Buffer>`, then `writeStream.path` will be a `<Buffer>`.

##### `writeStream.pending`

- Type: `<boolean>`

This property is `true` if the underlying file has not been opened yet, i.e. before the `'ready'` event is emitted.

#### `fs.constants`

- Type: `<Object>`

Returns an object containing commonly used constants for file system operations.

##### FS constants

The following constants are exported by `fs.constants` and `fsPromises.constants`.Not every constant will be available on every operating system; this is especially important for Windows, where many of the POSIX specific definitions are not available. For portable applications it is recommended to check for their presence before use.To use more than one constant, use the bitwise OR `|` operator.Example:`import { open, constants } from 'node:fs'; const { O_RDWR, O_CREAT, O_EXCL, } = constants; open('/path/to/my/file', O_RDWR | O_CREAT | O_EXCL, (err, fd) => { // ... });`

###### File access constants

The following constants are meant for use as the `mode` parameter passed to `fsPromises.access()`, `fs.access()`, and `fs.accessSync()`. Constant Description `F_OK` Flag indicating that the file is visible to the calling process. This is useful for determining if a file exists, but says nothing about `rwx` permissions. Default if no mode is specified. `R_OK` Flag indicating that the file can be read by the calling process. `W_OK` Flag indicating that the file can be written by the calling process. `X_OK` Flag indicating that the file can be executed by the calling process. This has no effect on Windows (will behave like `fs.constants.F_OK`). The definitions are also available on Windows.

###### File copy constants

The following constants are meant for use with `fs.copyFile()`. Constant Description `COPYFILE_EXCL` If present, the copy operation will fail with an error if the destination path already exists. `COPYFILE_FICLONE` If present, the copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then a fallback copy mechanism is used. `COPYFILE_FICLONE_FORCE` If present, the copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then the operation will fail with an error. The definitions are also available on Windows.

###### File open constants

The following constants are meant for use with `fs.open()`. Constant Description `O_RDONLY` Flag indicating to open a file for read-only access. `O_WRONLY` Flag indicating to open a file for write-only access. `O_RDWR` Flag indicating to open a file for read-write access. `O_CREAT` Flag indicating to create the file if it does not already exist. `O_EXCL` Flag indicating that opening a file should fail if the `O_CREAT` flag is set and the file already exists. `O_NOCTTY` Flag indicating that if path identifies a terminal device, opening the path shall not cause that terminal to become the controlling terminal for the process (if the process does not already have one). `O_TRUNC` Flag indicating that if the file exists and is a regular file, and the file is opened successfully for write access, its length shall be truncated to zero. `O_APPEND` Flag indicating that data will be appended to the end of the file. `O_DIRECTORY` Flag indicating that the open should fail if the path is not a directory. `O_NOATIME` Flag indicating reading accesses to the file system will no longer result in an update to the `atime` information associated with the file. This flag is available on Linux operating systems only. `O_NOFOLLOW` Flag indicating that the open should fail if the path is a symbolic link. `O_SYNC` Flag indicating that the file is opened for synchronized I/O with write operations waiting for file integrity. `O_DSYNC` Flag indicating that the file is opened for synchronized I/O with write operations waiting for data integrity. `O_SYMLINK` Flag indicating to open the symbolic link itself rather than the resource it is pointing to. `O_DIRECT` When set, an attempt will be made to minimize caching effects of file I/O. `O_NONBLOCK` Flag indicating to open the file in nonblocking mode when possible. `UV_FS_O_FILEMAP` When set, a memory file mapping is used to access the file. This flag is available on Windows operating systems only. On other operating systems, this flag is ignored. On Windows, only `O_APPEND`, `O_CREAT`, `O_EXCL`, `O_RDONLY`, `O_RDWR`, `O_TRUNC`, `O_WRONLY`, and `UV_FS_O_FILEMAP` are available.

###### File type constants

The following constants are meant for use with the `<fs.Stats>` object's `mode` property for determining a file's type. Constant Description `S_IFMT` Bit mask used to extract the file type code. `S_IFREG` File type constant for a regular file. `S_IFDIR` File type constant for a directory. `S_IFCHR` File type constant for a character-oriented device file. `S_IFBLK` File type constant for a block-oriented device file. `S_IFIFO` File type constant for a FIFO/pipe. `S_IFLNK` File type constant for a symbolic link. `S_IFSOCK` File type constant for a socket. On Windows, only `S_IFCHR`, `S_IFDIR`, `S_IFLNK`, `S_IFMT`, and `S_IFREG`, are available.

###### File mode constants

The following constants are meant for use with the `<fs.Stats>` object's `mode` property for determining the access permissions for a file. Constant Description `S_IRWXU` File mode indicating readable, writable, and executable by owner. `S_IRUSR` File mode indicating readable by owner. `S_IWUSR` File mode indicating writable by owner. `S_IXUSR` File mode indicating executable by owner. `S_IRWXG` File mode indicating readable, writable, and executable by group. `S_IRGRP` File mode indicating readable by group. `S_IWGRP` File mode indicating writable by group. `S_IXGRP` File mode indicating executable by group. `S_IRWXO` File mode indicating readable, writable, and executable by others. `S_IROTH` File mode indicating readable by others. `S_IWOTH` File mode indicating writable by others. `S_IXOTH` File mode indicating executable by others. On Windows, only `S_IRUSR` and `S_IWUSR` are available.
