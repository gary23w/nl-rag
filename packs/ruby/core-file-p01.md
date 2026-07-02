---
title: "class File (part 1/3)"
source: https://ruby-doc.org/core/File.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/3
---

# class File

A File object is a representation of a file in the underlying platform.

Class File extends module `FileTest`, supporting such singleton methods as `File.exist?`.


## About the Examples¶ ↑

Many examples here use these variables:

```
text = <<~EOT
  First line
  Second line

  Fourth line
  Fifth line
EOT

russian = "\u{442 435 441 442}" 

data = "\u9990\u9991\u9992\u9993\u9994"

File.write('t.txt', text)

File.write('t.rus', russian)

f = File.new('t.dat', 'wb:UTF-16')
f.write(data)
f.close
```


## Access Modes¶ ↑

Methods `File.new` and `File.open` each create a File object for a given file path.

### String Access Modes¶ ↑

Methods `File.new` and `File.open` each may take string argument `mode`, which:

- Begins with a 1- or 2-character read/write mode.
- May also contain a 1-character data mode.
- May also contain a 1-character file-create mode.

#### Read/Write Mode¶ ↑

The read/write `mode` determines:

- Whether the file is to be initially truncated.
- Whether reading is allowed, and if so:
  - The initial read position in the file.
  - Where in the file reading can occur.
- Whether writing is allowed, and if so:
  - The initial write position in the file.
  - Where in the file writing can occur.

These tables summarize:

```
Read/Write Modes for Existing File

|------|-----------|----------|----------|----------|-----------|
| R/W  | Initial   |          | Initial  |          | Initial   |
| Mode | Truncate? |  Read    | Read Pos |  Write   | Write Pos |
|------|-----------|----------|----------|----------|-----------|
| 'r'  |    No     | Anywhere |    0     |   Error  |     -     |
| 'w'  |    Yes    |   Error  |    -     | Anywhere |     0     |
| 'a'  |    No     |   Error  |    -     | End only |    End    |
| 'r+' |    No     | Anywhere |    0     | Anywhere |     0     |
| 'w+' |    Yes    | Anywhere |    0     | Anywhere |     0     |
| 'a+' |    No     | Anywhere |   End    | End only |    End    |
|------|-----------|----------|----------|----------|-----------|

Read/Write Modes for \File To Be Created

|------|----------|----------|----------|-----------|
| R/W  |          | Initial  |          | Initial   |
| Mode |  Read    | Read Pos |  Write   | Write Pos |
|------|----------|----------|----------|-----------|
| 'w'  |   Error  |    -     | Anywhere |     0     |
| 'a'  |   Error  |    -     | End only |     0     |
| 'w+' | Anywhere |    0     | Anywhere |     0     |
| 'a+' | Anywhere |    0     | End only |    End    |
|------|----------|----------|----------|-----------|
```

Note that modes `'r'` and `'r+'` are not allowed for a non-existent file (exception raised).

In the tables:

- `Anywhere` means that methods `IO#rewind`, `IO#pos=`, and `IO#seek` may be used to change the file’s position, so that allowed reading or writing may occur anywhere in the file.
- `End only` means that writing can occur only at end-of-file, and that methods `IO#rewind`, `IO#pos=`, and `IO#seek` do not affect writing.
- `Error` means that an exception is raised if disallowed reading or writing is attempted.

##### Read/Write Modes for Existing File¶ ↑

- `'r'`:
  - File is not initially truncated:
    ```
f = File.new('t.txt') 
f.size == 0           
    ```
  - File’s initial read position is 0:
    ```
f.pos 
    ```
  - File may be read anywhere; see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.readline 
f.readline 

f.rewind
f.readline 

f.pos = 1
f.readline 

f.seek(1, :CUR)
f.readline 
    ```
  - Writing is not allowed:
    ```
f.write('foo') 
    ```
- `'w'`:
  - File is initially truncated:
    ```
path = 't.tmp'
File.write(path, text)
f = File.new(path, 'w')
f.size == 0 
    ```
  - File’s initial write position is 0:
    ```
f.pos 
    ```
  - File may be written anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.write('bar')
f.flush
File.read(path) 
f.pos 

f.rewind
f.write('baz')
f.flush
File.read(path) 
f.pos 

f.pos = 3
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.seek(-3, :END)
f.write('bam')
f.flush
File.read(path) 
f.pos 

f.pos = 8
f.write('bah')  
f.flush
File.read(path) 
f.pos 
    ```
  - Reading is not allowed:
    ```
f.read 
    ```
- `'a'`:
  - File is not initially truncated:
    ```
path = 't.tmp'
File.write(path, 'foo')
f = File.new(path, 'a')
f.size == 0 
    ```
  - File’s initial position is 0 (but is ignored):
    ```
f.pos 
    ```
  - File may be written only at end-of-file; `IO#rewind`, `IO#pos=`, `IO#seek` do not affect writing:
    ```
f.write('bar')
f.flush
File.read(path) 
f.write('baz')
f.flush
File.read(path) 

f.rewind
f.write('bat')
f.flush
File.read(path) 
    ```
  - Reading is not allowed:
    ```
f.read 
    ```
- `'r+'`:
  - File is not initially truncated:
    ```
path = 't.tmp'
File.write(path, text)
f = File.new(path, 'r+')
f.size == 0 
    ```
  - File’s initial read position is 0:
    ```
f.pos 
    ```
  - File may be read or written anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.readline 
f.readline 

f.rewind
f.readline 

f.pos = 1
f.readline 

f.seek(1, :CUR)
f.readline 

f.rewind
f.write('WWW')
f.flush
File.read(path)

f.pos = 10
f.write('XXX')
f.flush
File.read(path)

f.seek(-6, :END)

f.write('YYY')

f.flush

File.read(path)

f.seek(2, :END)
f.write('ZZZ') 
f.flush
File.read(path)
    ```
- `'a+'`:
  - File is not initially truncated:
    ```
path = 't.tmp'
File.write(path, 'foo')
f = File.new(path, 'a+')
f.size == 0 
    ```
  - File’s initial read position is 0:
    ```
f.pos 
    ```
  - File may be written only at end-of-file; `IO#rewind`, `IO#pos=`, `IO#seek` do not affect writing:
    ```
f.write('bar')
f.flush
File.read(path)      
f.write('baz')
f.flush
File.read(path)      

f.rewind
f.write('bat')
f.flush
File.read(path) 
    ```
  - File may be read anywhere; see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.rewind
f.read 

f.pos = 3
f.read 

f.seek(-3, :END)
f.read 
    ```

##### Read/Write Modes for File To Be Created¶ ↑

Note that modes `'r'` and `'r+'` are not allowed for a non-existent file (exception raised).

- `'w'`:
  - File’s initial write position is 0:
    ```
path = 't.tmp'
FileUtils.rm_f(path)
f = File.new(path, 'w')
f.pos 
    ```
  - File may be written anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.write('bar')
f.flush
File.read(path) 
f.pos 

f.rewind
f.write('baz')
f.flush
File.read(path) 
f.pos 

f.pos = 3
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.seek(-3, :END)
f.write('bam')
f.flush
File.read(path) 
f.pos 

f.pos = 8
f.write('bah')  
f.flush
File.read(path) 
f.pos 
    ```
  - Reading is not allowed:
    ```
f.read 
    ```
- `'a'`:
  - File’s initial write position is 0:
    ```
path = 't.tmp'
FileUtils.rm_f(path)
f = File.new(path, 'a')
f.pos 
    ```
  - Writing occurs only at end-of-file:
    ```
f.write('foo')
f.pos 
f.write('bar')
f.pos 
f.flush
File.read(path) 

f.rewind
f.write('baz')
f.flush
File.read(path) 
    ```
  - Reading is not allowed:
    ```
f.read 
    ```
- `'w+'`:
  - File’s initial position is 0:
    ```
path = 't.tmp'
FileUtils.rm_f(path)
f = File.new(path, 'w+')
f.pos 
    ```
  - File may be written anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.write('bar')
f.flush
File.read(path) 
f.pos 

f.rewind
f.write('baz')
f.flush
File.read(path) 
f.pos 

f.pos = 3
f.write('foo')
f.flush
File.read(path) 
f.pos 

f.seek(-3, :END)
f.write('bam')
f.flush
File.read(path) 
f.pos 

f.pos = 8
f.write('bah')  
f.flush
File.read(path) 
f.pos 
    ```
  - File may be read anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.rewind

f.read

f.pos = 3

f.read

f.seek(-3, :END)

f.read
    ```
- `'a+'`:
  - File’s initial write position is 0:
    ```
path = 't.tmp'
FileUtils.rm_f(path)
f = File.new(path, 'a+')
f.pos 
    ```
  - Writing occurs only at end-of-file:
    ```
f.write('foo')
f.pos 
f.write('bar')
f.pos 
f.flush
File.read(path) 

f.rewind
f.write('baz')
f.flush
File.read(path) 
    ```
  - File may be read anywhere (even past end-of-file); see `IO#rewind`, `IO#pos=`, `IO#seek`:
    ```
f.rewind
f.read 

f.pos = 3
f.read 

f.seek(-3, :END)
f.read 

f.pos = 800
f.read 
    ```

#### Data Mode¶ ↑

To specify whether data is to be treated as text or as binary data, either of the following may be suffixed to any of the string read/write modes above:

- `'t'`: Text data; sets the default external encoding to `Encoding::UTF_8`; on Windows, enables conversion between EOL and CRLF and enables interpreting `0x1A` as an end-of-file marker.
- `'b'`: Binary data; sets the default external encoding to `Encoding::ASCII_8BIT`; on Windows, suppresses conversion between EOL and CRLF and disables interpreting `0x1A` as an end-of-file marker.

If neither is given, the stream defaults to text data.

Examples:

```
File.new('t.txt', 'rt')
File.new('t.dat', 'rb')
```

When the data mode is specified, the read/write mode may not be omitted, and the data mode must precede the file-create mode, if given:

```
File.new('t.dat', 'b')   
File.new('t.dat', 'rxb') 
```

#### File-Create Mode¶ ↑

The following may be suffixed to any writable string mode above:

- `'x'`: Creates the file if it does not exist; raises an exception if the file exists.

Example:

```
File.new('t.tmp', 'wx')
```

When the file-create mode is specified, the read/write mode may not be omitted, and the file-create mode must follow the data mode:

```
File.new('t.dat', 'x')   
File.new('t.dat', 'rxb') 
```

### Integer Access Modes¶ ↑

When mode is an integer it must be one or more of the following constants, which may be combined by the bitwise OR operator `|`:

- `File::RDONLY`: Open for reading only.
- `File::WRONLY`: Open for writing only.
- `File::RDWR`: Open for reading and writing.
- `File::APPEND`: Open for appending only.

Examples:

```
File.new('t.txt', File::RDONLY)
File.new('t.tmp', File::RDWR | File::CREAT | File::EXCL)
```

Note: `Method` `IO#set_encoding` does not allow the mode to be specified as an integer.

### File-Create Mode Specified as an Integer¶ ↑

These constants may also be ORed into the integer mode:

- `File::CREAT`: Create file if it does not exist.
- `File::EXCL`: Raise an exception if `File::CREAT` is given and the file exists.

### Data Mode Specified as an Integer¶ ↑

Data mode cannot be specified as an integer. When the stream access mode is given as an integer, the data mode is always text, never binary.

Note that although there is a constant `File::BINARY`, setting its value in an integer stream mode has no effect; this is because, as documented in `File::Constants`, the `File::BINARY` value disables line code conversion, but does not change the external encoding.

### Encodings¶ ↑

Any of the string modes above may specify encodings - either external encoding only or both external and internal encodings - by appending one or both encoding names, separated by colons:

```
f = File.new('t.dat', 'rb')
f.external_encoding 
f.internal_encoding 
f = File.new('t.dat', 'rb:UTF-16')
f.external_encoding 
f.internal_encoding 
f = File.new('t.dat', 'rb:UTF-16:UTF-16')
f.external_encoding 
f.internal_encoding 
f.close
```

The numerous encoding names are available in array `Encoding.name_list`:

```
Encoding.name_list.take(3) 
```

When the external encoding is set, strings read are tagged by that encoding when reading, and strings written are converted to that encoding when writing.

When both external and internal encodings are set, strings read are converted from external to internal encoding, and strings written are converted from internal to external encoding. For further details about transcoding input and output, see Encodings.

If the external encoding is `'BOM|UTF-8'`, `'BOM|UTF-16LE'` or `'BOM|UTF16-BE'`, Ruby checks for a Unicode BOM in the input document to help determine the encoding. For UTF-16 encodings the file open mode must be binary. If the BOM is found, it is stripped and the external encoding from the BOM is used.

Note that the BOM-style encoding option is case insensitive, so `'bom|utf-8'` is also valid.


## File Permissions¶ ↑

A File object has *permissions*, an octal integer representing the permissions of an actual file in the underlying platform.

Note that file permissions are quite different from the *mode* of a file stream (File object).

In a File object, the permissions are available thus, where method `mode`, despite its name, returns permissions:

```
f = File.new('t.txt')
f.lstat.mode.to_s(8) 
```

On a Unix-based operating system, the three low-order octal digits represent the permissions for owner (6), group (4), and world (4). The triplet of bits in each octal digit represent, respectively, read, write, and execute permissions.

Permissions `0644` thus represent read-write access for owner and read-only access for group and world. See man pages open(2) and chmod(2).

For a directory, the meaning of the execute bit changes: when set, the directory can be searched.

Higher-order bits in permissions may indicate the type of file (plain, directory, pipe, socket, etc.) and various other special features.

On non-Posix operating systems, permissions may include only read-only or read-write, in which case, the remaining permission will resemble typical values. On Windows, for instance, the default permissions are `0644`; The only change that can be made is to make the file read-only, which is reported as `0444`.

For a method that actually creates a file in the underlying platform (as opposed to merely creating a File object), permissions may be specified:

```
File.new('t.tmp', File::CREAT, 0644)
File.new('t.tmp', File::CREAT, 0444)
```

Permissions may also be changed:

```
f = File.new('t.tmp', File::CREAT, 0444)
f.chmod(0644)
f.chmod(0444)
```


## File Constants¶ ↑

Various constants for use in File and `IO` methods may be found in module `File::Constants`; an array of their names is returned by `File::Constants.constants`.
