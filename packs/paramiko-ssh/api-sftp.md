---
title: "SFTP"
source: https://docs.paramiko.org/en/latest/api/sftp.html
domain: paramiko-ssh
license: CC-BY-SA-4.0
tags: python paramiko, paramiko ssh client, sftp python
fetched: 2026-07-02
---

# SFTP

***exception*paramiko.sftp.SFTPError**

**__weakref__**

list of weak references to the object (if defined)

***class*paramiko.sftp.int64**

***class*paramiko.sftp_client.SFTP(*sock*)**

An alias for `SFTPClient` for backwards compatibility.

***class*paramiko.sftp_client.SFTPClient(*sock*)**

SFTP client object.

Used to open an SFTP session across an open SSH `Transport` and perform remote file operations.

Instances of this class may be used as context managers.

**__init__(*sock*)**

Create an SFTP client from an existing `Channel`. The channel should already have requested the `"sftp"` subsystem.

An alternate way to create an SFTP client context is by using `from_transport`.

**Parameters:**

**sock** (*.Channel*) – an open `Channel` using the `"sftp"` subsystem

**Raises:**

`SSHException` – if there’s an exception while negotiating sftp

**chdir(*path=None*)**

Change the “current directory” of this SFTP session. Since SFTP doesn’t really have the concept of a current working directory, this is emulated by Paramiko. Once you use this method to set a working directory, all operations on this `SFTPClient` object will be relative to that path. You can pass in `None` to stop using a current working directory.

**Parameters:**

**path** (*str*) – new current working directory

**Raises:**

`IOError` – if the requested path doesn’t exist on the server

New in version 1.4.

**chmod(*path*, *mode*)**

Change the mode (permissions) of a file. The permissions are unix-style and identical to those used by Python’s `os.chmod` function.

**Parameters:**

- **path** (*str*) – path of the file to change the permissions of
- **mode** (*int*) – new permissions

**chown(*path*, *uid*, *gid*)**

Change the owner (`uid`) and group (`gid`) of a file. As with Python’s `os.chown` function, you must pass both arguments, so if you only want to change one, use `stat` first to retrieve the current owner and group.

**Parameters:**

- **path** (*str*) – path of the file to change the owner and group of
- **uid** (*int*) – new owner’s uid
- **gid** (*int*) – new group id

**close()**

Close the SFTP session and its underlying channel.

New in version 1.4.

**file(*filename*, *mode='r'*, *bufsize=-1*)**

Open a file on the remote server. The arguments are the same as for Python’s built-in `python:file` (aka `open`). A file-like object is returned, which closely mimics the behavior of a normal Python file object, including the ability to be used as a context manager.

The mode indicates how the file is to be opened: `'r'` for reading, `'w'` for writing (truncating an existing file), `'a'` for appending, `'r+'` for reading/writing, `'w+'` for reading/writing (truncating an existing file), `'a+'` for reading/appending. The Python `'b'` flag is ignored, since SSH treats all files as binary. The `'U'` flag is supported in a compatible way.

Since 1.5.2, an `'x'` flag indicates that the operation should only succeed if the file was created and did not previously exist. This has no direct mapping to Python’s file flags, but is commonly known as the `O_EXCL` flag in posix.

The file will be buffered in standard Python style by default, but can be altered with the `bufsize` parameter. `<=0` turns off buffering, `1` uses line buffering, and any number greater than 1 (`>1`) uses that specific buffer size.

**Parameters:**

- **filename** (*str*) – name of the file to open
- **mode** (*str*) – mode (Python-style) to open in
- **bufsize** (*int*) – desired buffering (default: `-1`)

**Returns:**

an `SFTPFile` object representing the open file

**Raises:**

`IOError` – if the file could not be opened.

***classmethod*from_transport(*t*, *window_size=None*, *max_packet_size=None*)**

Create an SFTP client channel from an open `Transport`.

Setting the window and packet sizes might affect the transfer speed. The default settings in the `Transport` class are the same as in OpenSSH and should work adequately for both files transfers and interactive sessions.

**Parameters:**

- **t** (*.Transport*) – an open `Transport` which is already authenticated
- **window_size** (*int*) – optional window size for the `SFTPClient` session.
- **max_packet_size** (*int*) – optional max packet size for the `SFTPClient` session..

**Returns:**

a new `SFTPClient` object, referring to an sftp session (channel) across the transport

Changed in version 1.15: Added the `window_size` and `max_packet_size` arguments.

**get(*remotepath*, *localpath*, *callback=None*, *prefetch=True*, *max_concurrent_prefetch_requests=None*)**

Copy a remote file (`remotepath`) from the SFTP server to the local host as `localpath`. Any exception raised by operations will be passed through. This method is primarily provided as a convenience.

**Parameters:**

- **remotepath** (*str*) – the remote file to copy
- **localpath** (*str*) – the destination path on the local host
- **callback** (*callable*) – optional callback function (form: `func(int, int)`) that accepts the bytes transferred so far and the total bytes to be transferred
- **prefetch** (*bool*) – controls whether prefetching is performed (default: True)
- **max_concurrent_prefetch_requests** (*int*) – The maximum number of concurrent read requests to prefetch. When this is `None` (the default), do not limit the number of concurrent prefetch requests. Note: OpenSSH’s sftp internally imposes a limit of 64 concurrent requests, while Paramiko imposes no limit by default; consider setting a limit if a file can be successfully received with sftp but hangs with Paramiko.

New in version 1.4.

Changed in version 1.7.4: Added the `callback` param

Changed in version 2.8: Added the `prefetch` keyword argument.

Changed in version 3.3: Added `max_concurrent_prefetch_requests`.

**get_channel()**

Return the underlying `Channel` object for this SFTP session. This might be useful for doing things like setting a timeout on the channel.

New in version 1.7.1.

**getcwd()**

Return the “current working directory” for this SFTP session, as emulated by Paramiko. If no directory has been set with `chdir`, this method will return `None`.

New in version 1.4.

**getfo(*remotepath*, *fl*, *callback=None*, *prefetch=True*, *max_concurrent_prefetch_requests=None*)**

Copy a remote file (`remotepath`) from the SFTP server and write to an open file or file-like object, `fl`. Any exception raised by operations will be passed through. This method is primarily provided as a convenience.

**Parameters:**

- **remotepath** (*object*) – opened file or file-like object to copy to
- **fl** (*str*) – the destination path on the local host or open file object
- **callback** (*callable*) – optional callback function (form: `func(int, int)`) that accepts the bytes transferred so far and the total bytes to be transferred
- **prefetch** (*bool*) – controls whether prefetching is performed (default: True)
- **max_concurrent_prefetch_requests** (*int*) – The maximum number of concurrent read requests to prefetch. See `SFTPClient.get` (its `max_concurrent_prefetch_requests` param) for details.

**Returns:**

the `number` of bytes written to the opened file object

New in version 1.10.

Changed in version 2.8: Added the `prefetch` keyword argument.

Changed in version 3.3: Added `max_concurrent_prefetch_requests`.

**listdir(*path='.'*)**

Return a list containing the names of the entries in the given `path`.

The list is in arbitrary order. It does not include the special entries `'.'` and `'..'` even if they are present in the folder. This method is meant to mirror `os.listdir` as closely as possible. For a list of full `SFTPAttributes` objects, see `listdir_attr`.

**Parameters:**

**path** (*str*) – path to list (defaults to `'.'`)

**listdir_attr(*path='.'*)**

Return a list containing `SFTPAttributes` objects corresponding to files in the given `path`. The list is in arbitrary order. It does not include the special entries `'.'` and `'..'` even if they are present in the folder.

The returned `SFTPAttributes` objects will each have an additional field: `longname`, which may contain a formatted string of the file’s attributes, in unix format. The content of this string will probably depend on the SFTP server implementation.

**Parameters:**

**path** (*str*) – path to list (defaults to `'.'`)

**Returns:**

list of `SFTPAttributes` objects

New in version 1.2.

**listdir_iter(*path='.'*, *read_aheads=50*)**

Generator version of `listdir_attr`.

See the API docs for `listdir_attr` for overall details.

This function adds one more kwarg on top of `listdir_attr`: `read_aheads`, an integer controlling how many `SSH_FXP_READDIR` requests are made to the server. The default of 50 should suffice for most file listings as each request/response cycle may contain multiple files (dependent on server implementation.)

New in version 1.15.

**lstat(*path*)**

Retrieve information about a file on the remote system, without following symbolic links (shortcuts). This otherwise behaves exactly the same as `stat`.

**Parameters:**

**path** (*str*) – the filename to stat

**Returns:**

an `SFTPAttributes` object containing attributes about the given file

**mkdir(*path*, *mode=511*)**

Create a folder (directory) named `path` with numeric mode `mode`. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out.

**Parameters:**

- **path** (*str*) – name of the folder to create
- **mode** (*int*) – permissions (posix-style) for the newly-created folder

**normalize(*path*)**

Return the normalized path (on the server) of a given path. This can be used to quickly resolve symbolic links or determine what the server is considering to be the “current folder” (by passing `'.'` as `path`).

**Parameters:**

**path** (*str*) – path to be normalized

**Returns:**

normalized form of the given path (as a `str`)

**Raises:**

`IOError` – if the path can’t be resolved on the server

**open(*filename*, *mode='r'*, *bufsize=-1*)**

Open a file on the remote server. The arguments are the same as for Python’s built-in `python:file` (aka `open`). A file-like object is returned, which closely mimics the behavior of a normal Python file object, including the ability to be used as a context manager.

The mode indicates how the file is to be opened: `'r'` for reading, `'w'` for writing (truncating an existing file), `'a'` for appending, `'r+'` for reading/writing, `'w+'` for reading/writing (truncating an existing file), `'a+'` for reading/appending. The Python `'b'` flag is ignored, since SSH treats all files as binary. The `'U'` flag is supported in a compatible way.

Since 1.5.2, an `'x'` flag indicates that the operation should only succeed if the file was created and did not previously exist. This has no direct mapping to Python’s file flags, but is commonly known as the `O_EXCL` flag in posix.

The file will be buffered in standard Python style by default, but can be altered with the `bufsize` parameter. `<=0` turns off buffering, `1` uses line buffering, and any number greater than 1 (`>1`) uses that specific buffer size.

**Parameters:**

- **filename** (*str*) – name of the file to open
- **mode** (*str*) – mode (Python-style) to open in
- **bufsize** (*int*) – desired buffering (default: `-1`)

**Returns:**

an `SFTPFile` object representing the open file

**Raises:**

`IOError` – if the file could not be opened.

**posix_rename(*oldpath*, *newpath*)**

Rename a file or folder from `oldpath` to `newpath`, following posix conventions.

**Parameters:**

- **oldpath** (*str*) – existing name of the file or folder
- **newpath** (*str*) – new name for the file or folder, will be overwritten if it already exists

**Raises:**

`IOError` – if `newpath` is a folder, posix-rename is not supported by the server or something else goes wrong

**Versionadded:**

2.2

**put(*localpath*, *remotepath*, *callback=None*, *confirm=True*)**

Copy a local file (`localpath`) to the SFTP server as `remotepath`. Any exception raised by operations will be passed through. This method is primarily provided as a convenience.

The SFTP operations use pipelining for speed.

**Parameters:**

- **localpath** (*str*) – the local file to copy
- **remotepath** (*str*) – the destination path on the SFTP server. Note that the filename should be included. Only specifying a directory may result in an error.
- **callback** (*callable*) – optional callback function (form: `func(int, int)`) that accepts the bytes transferred so far and the total bytes to be transferred
- **confirm** (*bool*) – whether to do a stat() on the file afterwards to confirm the file size

**Returns:**

an `SFTPAttributes` object containing attributes about the given file

New in version 1.4.

Changed in version 1.7.4: `callback` and rich attribute return value added.

Changed in version 1.7.7: `confirm` param added.

**putfo(*fl*, *remotepath*, *file_size=0*, *callback=None*, *confirm=True*)**

Copy the contents of an open file object (`fl`) to the SFTP server as `remotepath`. Any exception raised by operations will be passed through.

The SFTP operations use pipelining for speed.

**Parameters:**

- **fl** – opened file or file-like object to copy
- **remotepath** (*str*) – the destination path on the SFTP server
- **file_size** (*int*) – optional size parameter passed to callback. If none is specified, size defaults to 0
- **callback** (*callable*) – optional callback function (form: `func(int, int)`) that accepts the bytes transferred so far and the total bytes to be transferred (since 1.7.4)
- **confirm** (*bool*) – whether to do a stat() on the file afterwards to confirm the file size (since 1.7.7)

**Returns:**

an `SFTPAttributes` object containing attributes about the given file.

New in version 1.10.

**readlink(*path*)**

Return the target of a symbolic link (shortcut). You can use `symlink` to create these. The result may be either an absolute or relative pathname.

**Parameters:**

**path** (*str*) – path of the symbolic link file

**Returns:**

target path, as a `str`

**remove(*path*)**

Remove the file at the given path. This only works on files; for removing folders (directories), use `rmdir`.

**Parameters:**

**path** (*str*) – path (absolute or relative) of the file to remove

**Raises:**

`IOError` – if the path refers to a folder (directory)

**rename(*oldpath*, *newpath*)**

Rename a file or folder from `oldpath` to `newpath`.

Note

This method implements ‘standard’ SFTP `RENAME` behavior; those seeking the OpenSSH “POSIX rename” extension behavior should use `posix_rename`.

**Parameters:**

- **oldpath** (*str*) – existing name of the file or folder
- **newpath** (*str*) – new name for the file or folder, must not exist already

**Raises:**

`IOError` – if `newpath` is a folder, or something else goes wrong

**rmdir(*path*)**

Remove the folder named `path`.

**Parameters:**

**path** (*str*) – name of the folder to remove

**stat(*path*)**

Retrieve information about a file on the remote system. The return value is an object whose attributes correspond to the attributes of Python’s `stat` structure as returned by `os.stat`, except that it contains fewer fields. An SFTP server may return as much or as little info as it wants, so the results may vary from server to server.

Unlike a Python `stat` object, the result may not be accessed as a tuple. This is mostly due to the author’s slack factor.

The fields supported are: `st_mode`, `st_size`, `st_uid`, `st_gid`, `st_atime`, and `st_mtime`.

**Parameters:**

**path** (*str*) – the filename to stat

**Returns:**

an `SFTPAttributes` object containing attributes about the given file

**symlink(*source*, *dest*)**

Create a symbolic link to the `source` path at `destination`.

**Parameters:**

- **source** (*str*) – path of the original file
- **dest** (*str*) – path of the newly created symlink

**truncate(*path*, *size*)**

Change the size of the file specified by `path`. This usually extends or shrinks the size of the file, just like the `truncate` method on Python file objects.

**Parameters:**

- **path** (*str*) – path of the file to modify
- **size** (*int*) – the new size of the file

**unlink(*path*)**

Remove the file at the given path. This only works on files; for removing folders (directories), use `rmdir`.

**Parameters:**

**path** (*str*) – path (absolute or relative) of the file to remove

**Raises:**

`IOError` – if the path refers to a folder (directory)

**utime(*path*, *times*)**

Set the access and modified times of the file specified by `path`. If `times` is `None`, then the file’s access and modified times are set to the current time. Otherwise, `times` must be a 2-tuple of numbers, of the form `(atime, mtime)`, which is used to set the access and modified times, respectively. This bizarre API is mimicked from Python for the sake of consistency – I apologize.

**Parameters:**

- **path** (*str*) – path of the file to modify
- **times** (*tuple*) – `None` or a tuple of (access time, modified time) in standard internet epoch time (seconds since 01 January 1970 GMT)

Server-mode SFTP support.

***class*paramiko.sftp_server.SFTPServer(*channel*, *name*, *server*, *sftp_si=<class 'paramiko.sftp_si.SFTPServerInterface'>*, **args*, ***kwargs*)**

Server-side SFTP subsystem support. Since this is a `SubsystemHandler`, it can be (and is meant to be) set as the handler for `"sftp"` requests. Use `Transport.set_subsystem_handler` to activate this class.

**__init__(*channel*, *name*, *server*, *sftp_si=<class 'paramiko.sftp_si.SFTPServerInterface'>*, **args*, ***kwargs*)**

The constructor for SFTPServer is meant to be called from within the `Transport` as a subsystem handler. `server` and any additional parameters or keyword parameters are passed from the original call to `Transport.set_subsystem_handler`.

**Parameters:**

- **channel** (*.Channel*) – channel passed from the `Transport`.
- **name** (*str*) – name of the requested subsystem.
- **server** (*.ServerInterface*) – the server object associated with this channel and subsystem
- **sftp_si** – a subclass of `SFTPServerInterface` to use for handling individual requests.

***static*convert_errno(*e*)**

Convert an errno value (as from an `OSError` or `IOError`) into a standard SFTP result code. This is a convenience function for trapping exceptions in server code and returning an appropriate result.

**Parameters:**

**e** (*int*) – an errno code, as from `OSError.errno`.

**Returns:**

an `int` SFTP error code like `SFTP_NO_SUCH_FILE`.

**finish_subsystem()**

Perform any cleanup at the end of a subsystem. The default implementation just closes the channel.

New in version 1.1.

***static*set_file_attr(*filename*, *attr*)**

Change a file’s attributes on the local filesystem. The contents of `attr` are used to change the permissions, owner, group ownership, and/or modification & access time of the file, depending on which attributes are present in `attr`.

This is meant to be a handy helper function for translating SFTP file requests into local file operations.

**Parameters:**

- **filename** (*str*) – name of the file to alter (should usually be an absolute path).
- **attr** (*.SFTPAttributes*) – attributes to change.

**start_subsystem(*name*, *transport*, *channel*)**

Process an ssh subsystem in server mode. This method is called on a new object (and in a new thread) for each subsystem request. It is assumed that all subsystem logic will take place here, and when the subsystem is finished, this method will return. After this method returns, the channel is closed.

The combination of `transport` and `channel` are unique; this handler corresponds to exactly one `Channel` on one `Transport`.

Note

It is the responsibility of this method to exit if the underlying `Transport` is closed. This can be done by checking `Transport.is_active` or noticing an EOF on the `Channel`. If this method loops forever without checking for this case, your Python interpreter may refuse to exit because this thread will still be running.

**Parameters:**

- **name** (*str*) – name of the requested subsystem.
- **transport** (*.Transport*) – the server-mode `Transport`.
- **channel** (*.Channel*) – the channel associated with this subsystem request.

***class*paramiko.sftp_attr.SFTPAttributes**

Representation of the attributes of a file (or proxied file) for SFTP in client or server mode. It attempts to mirror the object returned by `os.stat` as closely as possible, so it may have the following fields, with the same meanings as those returned by an `os.stat` object:

> - `st_size`
> - `st_uid`
> - `st_gid`
> - `st_mode`
> - `st_atime`
> - `st_mtime`

Because SFTP allows flags to have other arbitrary named attributes, these are stored in a dict named `attr`. Occasionally, the filename is also stored, in `filename`.

**__init__()**

Create a new (empty) SFTPAttributes object. All fields will be empty.

**__repr__()**

Return repr(self).

**__str__()**

create a unix-style long description of the file (like ls -l)

**__weakref__**

list of weak references to the object (if defined)

***classmethod*from_stat(*obj*, *filename=None*)**

Create an `SFTPAttributes` object from an existing `stat` object (an object returned by `os.stat`).

**Parameters:**

- **obj** (*object*) – an object returned by `os.stat` (or equivalent).
- **filename** (*str*) – the filename associated with this file.

**Returns:**

new `SFTPAttributes` object with the same attribute fields.

SFTP file object

***class*paramiko.sftp_file.SFTPFile(*sftp*, *handle*, *mode='r'*, *bufsize=-1*)**

Bases: `BufferedFile`

Proxy object for a file on the remote server, in client mode SFTP.

Instances of this class may be used as context managers in the same way that built-in Python file objects are.

**check(*hash_algorithm*, *offset=0*, *length=0*, *block_size=0*)**

Ask the server for a hash of a section of this file. This can be used to verify a successful upload or download, or for various rsync-like operations.

The file is hashed from `offset`, for `length` bytes. If `length` is 0, the remainder of the file is hashed. Thus, if both `offset` and `length` are zero, the entire file is hashed.

Normally, `block_size` will be 0 (the default), and this method will return a byte string representing the requested hash (for example, a string of length 16 for MD5, or 20 for SHA-1). If a non-zero `block_size` is given, each chunk of the file (from `offset` to `offset + length`) of `block_size` bytes is computed as a separate hash. The hash results are all concatenated and returned as a single string.

For example, `check('sha1', 0, 1024, 512)` will return a string of length 40. The first 20 bytes will be the SHA-1 of the first 512 bytes of the file, and the last 20 bytes will be the SHA-1 of the next 512 bytes.

**Parameters:**

- **hash_algorithm** (*str*) – the name of the hash algorithm to use (normally `"sha1"` or `"md5"`)
- **offset** – offset into the file to begin hashing (0 means to start from the beginning)
- **length** – number of bytes to hash (0 means continue to the end of the file)
- **block_size** (*int*) – number of bytes to hash per result (must not be less than 256; 0 means to compute only one hash of the entire segment)

**Returns:**

`str` of bytes representing the hash of each block, concatenated together

**Raises:**

`IOError` – if the server doesn’t support the “check-file” extension, or possibly doesn’t support the hash algorithm requested

Note

Many (most?) servers don’t support this extension yet.

New in version 1.4.

**chmod(*mode*)**

Change the mode (permissions) of this file. The permissions are unix-style and identical to those used by Python’s `os.chmod` function.

**Parameters:**

**mode** (*int*) – new permissions

**chown(*uid*, *gid*)**

Change the owner (`uid`) and group (`gid`) of this file. As with Python’s `os.chown` function, you must pass both arguments, so if you only want to change one, use `stat` first to retrieve the current owner and group.

**Parameters:**

- **uid** (*int*) – new owner’s uid
- **gid** (*int*) – new group id

**close()**

Close the file.

**flush()**

Write out any data in the write buffer. This may do nothing if write buffering is not turned on.

**gettimeout()**

Returns the timeout in seconds (as a `float`) associated with the socket or ssh `Channel` used for this file.

See also

`Channel.gettimeout`

**prefetch(*file_size=None*, *max_concurrent_requests=None*)**

Pre-fetch the remaining contents of this file in anticipation of future `read` calls. If reading the entire file, pre-fetching can dramatically improve the download speed by avoiding roundtrip latency. The file’s contents are incrementally buffered in a background thread.

The prefetched data is stored in a buffer until read via the `read` method. Once data has been read, it’s removed from the buffer. The data may be read in a random order (using `seek`); chunks of the buffer that haven’t been read will continue to be buffered.

**Parameters:**

- **file_size** (*int*) – When this is `None` (the default), this method calls `stat` to determine the remote file size. In some situations, doing so can cause exceptions or hangs (see #562); as a workaround, one may call `stat` explicitly and pass its value in via this parameter.
- **max_concurrent_requests** (*int*) – The maximum number of concurrent read requests to prefetch. See `SFTPClient.get` (its `max_concurrent_prefetch_requests` param) for details.

New in version 1.5.1.

Changed in version 1.16.0: The `file_size` parameter was added (with no default value).

Changed in version 1.16.1: The `file_size` parameter was made optional for backwards compatibility.

Changed in version 3.3: Added `max_concurrent_requests`.

**read(*size=None*)**

Read at most `size` bytes from the file (less if we hit the end of the file first). If the `size` argument is negative or omitted, read all the remaining data in the file.

Note

`'b'` mode flag is ignored (`self.FLAG_BINARY` in `self._flags`), because SSH treats all files as binary, since we have no idea what encoding the file is in, or even if the file is text data.

**Parameters:**

**size** (*int*) – maximum number of bytes to read

**Returns:**

data read from the file (as bytes), or an empty string if EOF was encountered immediately

**readable()**

Check if the file can be read from.

**Returns:**

`True` if the file can be read from. If `False`, `read` will raise an exception.

**readinto(*buff*)**

Read up to `len(buff)` bytes into `bytearray` *buff* and return the number of bytes read.

**Returns:**

The number of bytes read.

**readline(*size=None*)**

Read one entire line from the file. A trailing newline character is kept in the string (but may be absent when a file ends with an incomplete line). If the size argument is present and non-negative, it is a maximum byte count (including the trailing newline) and an incomplete line may be returned. An empty string is returned only when EOF is encountered immediately.

Note

Unlike stdio’s `fgets`, the returned string contains null characters (`'\0'`) if they occurred in the input.

**Parameters:**

**size** (*int*) – maximum length of returned string.

**Returns:**

next line of the file, or an empty string if the end of the file has been reached.

If the file was opened in binary (`'b'`) mode: bytes are returned Else: the encoding of the file is assumed to be UTF-8 and character strings (`str`) are returned

**readlines(*sizehint=None*)**

Read all remaining lines using `readline` and return them as a list. If the optional `sizehint` argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

**Parameters:**

**sizehint** (*int*) – desired maximum number of bytes to read.

**Returns:**

list of lines read from the file.

**readv(*chunks*, *max_concurrent_prefetch_requests=None*)**

Read a set of blocks from the file by (offset, length). This is more efficient than doing a series of `seek` and `read` calls, since the prefetch machinery is used to retrieve all the requested blocks at once.

**Parameters:**

- **chunks** – a list of `(offset, length)` tuples indicating which sections of the file to read
- **max_concurrent_prefetch_requests** (*int*) – The maximum number of concurrent read requests to prefetch. See `SFTPClient.get` (its `max_concurrent_prefetch_requests` param) for details.

**Returns:**

a list of blocks read, in the same order as in `chunks`

New in version 1.5.4.

Changed in version 3.3: Added `max_concurrent_prefetch_requests`.

**seek(*offset*, *whence=0*)**

Set the file’s current position.

See `file.seek` for details.

**seekable()**

Check if the file supports random access.

**Returns:**

`True` if the file supports random access. If `False`, `seek()` will raise an exception

**set_pipelined(*pipelined=True*)**

Turn on/off the pipelining of write operations to this file. When pipelining is on, paramiko won’t wait for the server response after each write operation. Instead, they’re collected as they come in. At the first non-write operation (including `close`), all remaining server responses are collected. This means that if there was an error with one of your later writes, an exception might be thrown from within `close` instead of `write`.

By default, files are not pipelined.

**Parameters:**

**pipelined** (*bool*) – `True` if pipelining should be turned on for this file; `False` otherwise

New in version 1.5.

**setblocking(*blocking*)**

Set blocking or non-blocking mode on the underiying socket or ssh `Channel`.

**Parameters:**

**blocking** (*int*) – 0 to set non-blocking mode; non-0 to set blocking mode.

See also

`Channel.setblocking`

**settimeout(*timeout*)**

Set a timeout on read/write operations on the underlying socket or ssh `Channel`.

**Parameters:**

**timeout** (*float*) – seconds to wait for a pending read/write operation before raising `socket.timeout`, or `None` for no timeout

See also

`Channel.settimeout`

**stat()**

Retrieve information about this file from the remote system. This is exactly like `SFTPClient.stat`, except that it operates on an already-open file.

**Returns:**

an `SFTPAttributes` object containing attributes about this file.

**tell()**

Return the file’s current position. This may not be accurate or useful if the underlying file doesn’t support random access, or was opened in append mode.

**Returns:**

file position (`number` of bytes).

**truncate(*size*)**

Change the size of this file. This usually extends or shrinks the size of the file, just like the `truncate()` method on Python file objects.

**Parameters:**

**size** – the new size of the file

**utime(*times*)**

Set the access and modified times of this file. If `times` is `None`, then the file’s access and modified times are set to the current time. Otherwise, `times` must be a 2-tuple of numbers, of the form `(atime, mtime)`, which is used to set the access and modified times, respectively. This bizarre API is mimicked from Python for the sake of consistency – I apologize.

**Parameters:**

**times** (*tuple*) – `None` or a tuple of (access time, modified time) in standard internet epoch time (seconds since 01 January 1970 GMT)

**writable()**

Check if the file can be written to.

**Returns:**

`True` if the file can be written to. If `False`, `write` will raise an exception.

**write(*data*)**

Write data to the file. If write buffering is on (`bufsize` was specified and non-zero), some or all of the data may not actually be written yet. (Use `flush` or `close` to force buffered data to be written out.)

**Parameters:**

**data** – `str`/`bytes` data to write

**writelines(*sequence*)**

Write a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings. (The name is intended to match `readlines`; `writelines` does not add line separators.)

**Parameters:**

**sequence** – an iterable sequence of strings.

**xreadlines()**

Identical to `iter(f)`. This is a deprecated file interface that predates Python iterator support.

Abstraction of an SFTP file handle (for server mode).

***class*paramiko.sftp_handle.SFTPHandle(*flags=0*)**

Abstract object representing a handle to an open file (or folder) in an SFTP server implementation. Each handle has a string representation used by the client to refer to the underlying file.

Server implementations can (and should) subclass SFTPHandle to implement features of a file handle, like `stat` or `chattr`.

Instances of this class may be used as context managers.

**__init__(*flags=0*)**

Create a new file handle representing a local file being served over SFTP. If `flags` is passed in, it’s used to determine if the file is open in append mode.

**Parameters:**

**flags** (*int*) – optional flags as passed to `SFTPServerInterface.open`

**chattr(*attr*)**

Change the attributes of this file. The `attr` object will contain only those fields provided by the client in its request, so you should check for the presence of fields before using them.

**Parameters:**

**attr** (*.SFTPAttributes*) – the attributes to change on this file.

**Returns:**

an `int` error code like `SFTP_OK`.

**close()**

When a client closes a file, this method is called on the handle. Normally you would use this method to close the underlying OS level file object(s).

The default implementation checks for attributes on `self` named `readfile` and/or `writefile`, and if either or both are present, their `close()` methods are called. This means that if you are using the default implementations of `read` and `write`, this method’s default implementation should be fine also.

**read(*offset*, *length*)**

Read up to `length` bytes from this file, starting at position `offset`. The offset may be a Python long, since SFTP allows it to be 64 bits.

If the end of the file has been reached, this method may return an empty string to signify EOF, or it may also return `SFTP_EOF`.

The default implementation checks for an attribute on `self` named `readfile`, and if present, performs the read operation on the Python file-like object found there. (This is meant as a time saver for the common case where you are wrapping a Python file object.)

**Parameters:**

- **offset** – position in the file to start reading from.
- **length** (*int*) – number of bytes to attempt to read.

**Returns:**

the `bytes` read, or an error code `int`.

**stat()**

Return an `SFTPAttributes` object referring to this open file, or an error code. This is equivalent to `SFTPServerInterface.stat`, except it’s called on an open file instead of a path.

**Returns:**

an attributes object for the given file, or an SFTP error code (like `SFTP_PERMISSION_DENIED`).

**Return type:**

`SFTPAttributes` or error code

**write(*offset*, *data*)**

Write `data` into this file at position `offset`. Extending the file past its original end is expected. Unlike Python’s normal `write()` methods, this method cannot do a partial write: it must write all of `data` or else return an error.

The default implementation checks for an attribute on `self` named `writefile`, and if present, performs the write operation on the Python file-like object found there. The attribute is named differently from `readfile` to make it easy to implement read-only (or write-only) files, but if both attributes are present, they should refer to the same file.

**Parameters:**

- **offset** – position in the file to start reading from.
- **data** (*bytes*) – data to write into the file.

**Returns:**

an SFTP error code like `SFTP_OK`.

An interface to override for SFTP server support.

***class*paramiko.sftp_si.SFTPServerInterface(*server*, **args*, ***kwargs*)**

This class defines an interface for controlling the behavior of paramiko when using the `SFTPServer` subsystem to provide an SFTP server.

Methods on this class are called from the SFTP session’s thread, so you can block as long as necessary without affecting other sessions (even other SFTP sessions). However, raising an exception will usually cause the SFTP session to abruptly end, so you will usually want to catch exceptions and return an appropriate error code.

All paths are in string form instead of unicode because not all SFTP clients & servers obey the requirement that paths be encoded in UTF-8.

**__init__(*server*, **args*, ***kwargs*)**

Create a new SFTPServerInterface object. This method does nothing by default and is meant to be overridden by subclasses.

**Parameters:**

**server** (*.ServerInterface*) – the server object associated with this channel and SFTP subsystem

**__weakref__**

list of weak references to the object (if defined)

**canonicalize(*path*)**

Return the canonical form of a path on the server. For example, if the server’s home folder is `/home/foo`, the path `"../betty"` would be canonicalized to `"/home/betty"`. Note the obvious security issues: if you’re serving files only from a specific folder, you probably don’t want this method to reveal path names outside that folder.

You may find the Python methods in `os.path` useful, especially `os.path.normpath` and `os.path.realpath`.

The default implementation returns `os.path.normpath('/' + path)`.

**chattr(*path*, *attr*)**

Change the attributes of a file. The `attr` object will contain only those fields provided by the client in its request, so you should check for the presence of fields before using them.

**Parameters:**

- **path** (*str*) – requested path (relative or absolute) of the file to change.
- **attr** – requested attributes to change on the file (an `SFTPAttributes` object)

**Returns:**

an error code `int` like `SFTP_OK`.

**list_folder(*path*)**

Return a list of files within a given folder. The `path` will use posix notation (`"/"` separates folder names) and may be an absolute or relative path.

The list of files is expected to be a list of `SFTPAttributes` objects, which are similar in structure to the objects returned by `os.stat`. In addition, each object should have its `filename` field filled in, since this is important to a directory listing and not normally present in `os.stat` results. The method `SFTPAttributes.from_stat` will usually do what you want.

In case of an error, you should return one of the `SFTP_*` error codes, such as `SFTP_PERMISSION_DENIED`.

**Parameters:**

**path** (*str*) – the requested path (relative or absolute) to be listed.

**Returns:**

a list of the files in the given folder, using `SFTPAttributes` objects.

Note

You should normalize the given `path` first (see the `os.path` module) and check appropriate permissions before returning the list of files. Be careful of malicious clients attempting to use relative paths to escape restricted folders, if you’re doing a direct translation from the SFTP server path to your local filesystem.

**lstat(*path*)**

Return an `SFTPAttributes` object for a path on the server, or an error code. If your server supports symbolic links (also known as “aliases”), you should not follow them – instead, you should return data on the symlink or alias itself. (`stat` is the corresponding call that follows symlinks/aliases.)

**Parameters:**

**path** (*str*) – the requested path (relative or absolute) to fetch file statistics for.

**Returns:**

an `SFTPAttributes` object for the given file, or an SFTP error code (like `SFTP_PERMISSION_DENIED`).

**mkdir(*path*, *attr*)**

Create a new directory with the given attributes. The `attr` object may be considered a “hint” and ignored.

The `attr` object will contain only those fields provided by the client in its request, so you should use `hasattr` to check for the presence of fields before using them. In some cases, the `attr` object may be completely empty.

**Parameters:**

- **path** (*str*) – requested path (relative or absolute) of the new folder.
- **attr** (*.SFTPAttributes*) – requested attributes of the new folder.

**Returns:**

an SFTP error code `int` like `SFTP_OK`.

**open(*path*, *flags*, *attr*)**

Open a file on the server and create a handle for future operations on that file. On success, a new object subclassed from `SFTPHandle` should be returned. This handle will be used for future operations on the file (read, write, etc). On failure, an error code such as `SFTP_PERMISSION_DENIED` should be returned.

`flags` contains the requested mode for opening (read-only, write-append, etc) as a bitset of flags from the `os` module:

> - `os.O_RDONLY`
> - `os.O_WRONLY`
> - `os.O_RDWR`
> - `os.O_APPEND`
> - `os.O_CREAT`
> - `os.O_TRUNC`
> - `os.O_EXCL`

(One of `os.O_RDONLY`, `os.O_WRONLY`, or `os.O_RDWR` will always be set.)

The `attr` object contains requested attributes of the file if it has to be created. Some or all attribute fields may be missing if the client didn’t specify them.

Note

The SFTP protocol defines all files to be in “binary” mode. There is no equivalent to Python’s “text” mode.

**Parameters:**

- **path** (*str*) – the requested path (relative or absolute) of the file to be opened.
- **flags** (*int*) – flags or’d together from the `os` module indicating the requested mode for opening the file.
- **attr** (*.SFTPAttributes*) – requested attributes of the file if it is newly created.

**Returns:**

a new `SFTPHandle` or error code.

**posix_rename(*oldpath*, *newpath*)**

Rename (or move) a file, following posix conventions. If newpath already exists, it will be overwritten.

**Parameters:**

- **oldpath** (*str*) – the requested path (relative or absolute) of the existing file.
- **newpath** (*str*) – the requested new path of the file.

**Returns:**

an SFTP error code `int` like `SFTP_OK`.

**Versionadded:**

2.2

**readlink(*path*)**

Return the target of a symbolic link (or shortcut) on the server. If the specified path doesn’t refer to a symbolic link, an error should be returned.

**Parameters:**

**path** (*str*) – path (relative or absolute) of the symbolic link.

**Returns:**

the target `str` path of the symbolic link, or an error code like `SFTP_NO_SUCH_FILE`.

**remove(*path*)**

Delete a file, if possible.

**Parameters:**

**path** (*str*) – the requested path (relative or absolute) of the file to delete.

**Returns:**

an SFTP error code `int` like `SFTP_OK`.

**rename(*oldpath*, *newpath*)**

Rename (or move) a file. The SFTP specification implies that this method can be used to move an existing file into a different folder, and since there’s no other (easy) way to move files via SFTP, it’s probably a good idea to implement “move” in this method too, even for files that cross disk partition boundaries, if at all possible.

Note

You should return an error if a file with the same name as `newpath` already exists. (The rename operation should be non-desctructive.)

Note

This method implements ‘standard’ SFTP `RENAME` behavior; those seeking the OpenSSH “POSIX rename” extension behavior should use `posix_rename`.

**Parameters:**

- **oldpath** (*str*) – the requested path (relative or absolute) of the existing file.
- **newpath** (*str*) – the requested new path of the file.

**Returns:**

an SFTP error code `int` like `SFTP_OK`.

**rmdir(*path*)**

Remove a directory if it exists. The `path` should refer to an existing, empty folder – otherwise this method should return an error.

**Parameters:**

**path** (*str*) – requested path (relative or absolute) of the folder to remove.

**Returns:**

an SFTP error code `int` like `SFTP_OK`.

**session_ended()**

The SFTP server session has just ended, either cleanly or via an exception. This method is meant to be overridden to perform any necessary cleanup before this `SFTPServerInterface` object is destroyed.

**session_started()**

The SFTP server session has just started. This method is meant to be overridden to perform any necessary setup before handling callbacks from SFTP operations.

**stat(*path*)**

Return an `SFTPAttributes` object for a path on the server, or an error code. If your server supports symbolic links (also known as “aliases”), you should follow them. (`lstat` is the corresponding call that doesn’t follow symlinks/aliases.)

**Parameters:**

**path** (*str*) – the requested path (relative or absolute) to fetch file statistics for.

**Returns:**

an `SFTPAttributes` object for the given file, or an SFTP error code (like `SFTP_PERMISSION_DENIED`).

**symlink(*target_path*, *path*)**

Create a symbolic link on the server, as new pathname `path`, with `target_path` as the target of the link.

**Parameters:**

- **target_path** (*str*) – path (relative or absolute) of the target for this new symbolic link.
- **path** (*str*) – path (relative or absolute) of the symbolic link to create.

**Returns:**

an error code `int` like `SFTP_OK`.
