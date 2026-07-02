---
title: "os package (part 1/2)"
source: https://pkg.go.dev/os
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 1/2
---

# os

package

standard library

Version:

go1.26.4

Opens a new window with list of versions in this module.

Latest

Latest

This package is not in the latest version of its module.

Go to latest

Published: Jun 2, 2026

License:

BSD-3-Clause

Opens a new window with license information.

Imports:

20

Opens a new window with list of imports.

Imported by:

2,493,160

Opens a new window with list of known importers.

## Documentation

### Overview

Package os provides a platform-independent interface to operating system functionality. The design is Unix-like, although the error handling is Go-like; failing calls return values of type error rather than error numbers. Often, more information is available within the error. For example, if a call that takes a file name fails, such as Open or Stat, the error will include the failing file name when printed and will be of type *PathError, which may be unpacked for more information.

The os interface is intended to be uniform across all operating systems. Features not generally available appear in the system-specific package syscall.

Here is a simple example, opening a file and reading some of it.

```
file, err := os.Open("file.go") // For read access.
if err != nil {
	log.Fatal(err)
}
```

If the open fails, the error string will be self-explanatory, like

```
open file.go: no such file or directory
```

The file's data can then be read into a slice of bytes. Read and Write take their byte counts from the length of the argument slice.

```
data := make([]byte, 100)
count, err := file.Read(data)
if err != nil {
	log.Fatal(err)
}
fmt.Printf("read %d bytes: %q\n", count, data[:count])
```

#### Concurrency

The methods of File correspond to file system operations. All are safe for concurrent use. The maximum number of concurrent operations on a File may be limited by the OS or the system. The number should be high, but exceeding it may degrade performance or cause other issues.

### Index

- Constants
- Variables
- func Chdir(dir string) error
- func Chmod(name string, mode FileMode) error
- func Chown(name string, uid, gid int) error
- func Chtimes(name string, atime time.Time, mtime time.Time) error
- func Clearenv()
- func CopyFS(dir string, fsys fs.FS) error
- func DirFS(dir string) fs.FS
- func Environ() []string
- func Executable() (string, error)
- func Exit(code int)
- func Expand(s string, mapping func(string) string) string
- func ExpandEnv(s string) string
- func Getegid() int
- func Getenv(key string) string
- func Geteuid() int
- func Getgid() int
- func Getgroups() ([]int, error)
- func Getpagesize() int
- func Getpid() int
- func Getppid() int
- func Getuid() int
- func Getwd() (dir string, err error)
- func Hostname() (name string, err error)
- func IsExist(err error) bool
- func IsNotExist(err error) bool
- func IsPathSeparator(c uint8) bool
- func IsPermission(err error) bool
- func IsTimeout(err error) bool
- func Lchown(name string, uid, gid int) error
- func Link(oldname, newname string) error
- func LookupEnv(key string) (string, bool)
- func Mkdir(name string, perm FileMode) error
- func MkdirAll(path string, perm FileMode) error
- func MkdirTemp(dir, pattern string) (string, error)
- func NewSyscallError(syscall string, err error) error
- func Pipe() (r *File, w *File, err error)
- func ReadFile(name string) ([]byte, error)
- func Readlink(name string) (string, error)
- func Remove(name string) error
- func RemoveAll(path string) error
- func Rename(oldpath, newpath string) error
- func SameFile(fi1, fi2 FileInfo) bool
- func Setenv(key, value string) error
- func Symlink(oldname, newname string) error
- func TempDir() string
- func Truncate(name string, size int64) error
- func Unsetenv(key string) error
- func UserCacheDir() (string, error)
- func UserConfigDir() (string, error)
- func UserHomeDir() (string, error)
- func WriteFile(name string, data []byte, perm FileMode) error
- type DirEntry
  - func ReadDir(name string) ([]DirEntry, error)
- type File
  - func Create(name string) (*File, error)
  - func CreateTemp(dir, pattern string) (*File, error)
  - func NewFile(fd uintptr, name string) *File
  - func Open(name string) (*File, error)
  - func OpenFile(name string, flag int, perm FileMode) (*File, error)
  - func OpenInRoot(dir, name string) (*File, error)
  - func (f *File) Chdir() error
  - func (f *File) Chmod(mode FileMode) error
  - func (f *File) Chown(uid, gid int) error
  - func (f *File) Close() error
  - func (f *File) Fd() uintptr
  - func (f *File) Name() string
  - func (f *File) Read(b []byte) (n int, err error)
  - func (f *File) ReadAt(b []byte, off int64) (n int, err error)
  - func (f *File) ReadDir(n int) ([]DirEntry, error)
  - func (f *File) ReadFrom(r io.Reader) (n int64, err error)
  - func (f *File) Readdir(n int) ([]FileInfo, error)
  - func (f *File) Readdirnames(n int) (names []string, err error)
  - func (f *File) Seek(offset int64, whence int) (ret int64, err error)
  - func (f *File) SetDeadline(t time.Time) error
  - func (f *File) SetReadDeadline(t time.Time) error
  - func (f *File) SetWriteDeadline(t time.Time) error
  - func (f *File) Stat() (FileInfo, error)
  - func (f *File) Sync() error
  - func (f *File) SyscallConn() (syscall.RawConn, error)
  - func (f *File) Truncate(size int64) error
  - func (f *File) Write(b []byte) (n int, err error)
  - func (f *File) WriteAt(b []byte, off int64) (n int, err error)
  - func (f *File) WriteString(s string) (n int, err error)
  - func (f *File) WriteTo(w io.Writer) (n int64, err error)
- type FileInfo
  - func Lstat(name string) (FileInfo, error)
  - func Stat(name string) (FileInfo, error)
- type FileMode
- type LinkError
  - func (e *LinkError) Error() string
  - func (e *LinkError) Unwrap() error
- type PathError
- type ProcAttr
- type Process
  - func FindProcess(pid int) (*Process, error)
  - func StartProcess(name string, argv []string, attr *ProcAttr) (*Process, error)
  - func (p *Process) Kill() error
  - func (p *Process) Release() error
  - func (p *Process) Signal(sig Signal) error
  - func (p *Process) Wait() (*ProcessState, error)
  - func (p *Process) WithHandle(f func(handle uintptr)) error
- type ProcessState
  - func (p *ProcessState) ExitCode() int
  - func (p *ProcessState) Exited() bool
  - func (p *ProcessState) Pid() int
  - func (p *ProcessState) String() string
  - func (p *ProcessState) Success() bool
  - func (p *ProcessState) Sys() any
  - func (p *ProcessState) SysUsage() any
  - func (p *ProcessState) SystemTime() time.Duration
  - func (p *ProcessState) UserTime() time.Duration
- type Root
  - func OpenRoot(name string) (*Root, error)
  - func (r *Root) Chmod(name string, mode FileMode) error
  - func (r *Root) Chown(name string, uid, gid int) error
  - func (r *Root) Chtimes(name string, atime time.Time, mtime time.Time) error
  - func (r *Root) Close() error
  - func (r *Root) Create(name string) (*File, error)
  - func (r *Root) FS() fs.FS
  - func (r *Root) Lchown(name string, uid, gid int) error
  - func (r *Root) Link(oldname, newname string) error
  - func (r *Root) Lstat(name string) (FileInfo, error)
  - func (r *Root) Mkdir(name string, perm FileMode) error
  - func (r *Root) MkdirAll(name string, perm FileMode) error
  - func (r *Root) Name() string
  - func (r *Root) Open(name string) (*File, error)
  - func (r *Root) OpenFile(name string, flag int, perm FileMode) (*File, error)
  - func (r *Root) OpenRoot(name string) (*Root, error)
  - func (r *Root) ReadFile(name string) ([]byte, error)
  - func (r *Root) Readlink(name string) (string, error)
  - func (r *Root) Remove(name string) error
  - func (r *Root) RemoveAll(name string) error
  - func (r *Root) Rename(oldname, newname string) error
  - func (r *Root) Stat(name string) (FileInfo, error)
  - func (r *Root) Symlink(oldname, newname string) error
  - func (r *Root) WriteFile(name string, data []byte, perm FileMode) error
- type Signal
- type SyscallError
  - func (e *SyscallError) Error() string
  - func (e *SyscallError) Timeout() bool
  - func (e *SyscallError) Unwrap() error

### Examples

- Chmod
- Chtimes
- CreateTemp
- CreateTemp (Suffix)
- Expand
- ExpandEnv
- FileMode
- Getenv
- LookupEnv
- Mkdir
- MkdirAll
- MkdirTemp
- MkdirTemp (Suffix)
- OpenFile
- OpenFile (Append)
- ReadDir
- ReadFile
- Readlink
- Unsetenv
- UserCacheDir
- UserConfigDir
- WriteFile

### Constants

View Source

```
const (
	
	O_RDONLY int = syscall.O_RDONLY 
	O_WRONLY int = syscall.O_WRONLY 
	O_RDWR   int = syscall.O_RDWR   
	
	O_APPEND int = syscall.O_APPEND 
	O_CREATE int = syscall.O_CREAT  
	O_EXCL   int = syscall.O_EXCL   
	O_SYNC   int = syscall.O_SYNC   
	O_TRUNC  int = syscall.O_TRUNC  
)
```

Flags to OpenFile wrapping those of the underlying system. Not all flags may be implemented on a given system.

View Source

```
const (
	SEEK_SET int = 0 
	SEEK_CUR int = 1 
	SEEK_END int = 2 
)
```

Seek whence values.

Deprecated: Use io.SeekStart, io.SeekCurrent, and io.SeekEnd.

View Source

```
const (
	PathSeparator     = '/' 
	PathListSeparator = ':' 
)
```

View Source

```
const (
	
	
	ModeDir        = fs.ModeDir        
	ModeAppend     = fs.ModeAppend     
	ModeExclusive  = fs.ModeExclusive  
	ModeTemporary  = fs.ModeTemporary  
	ModeSymlink    = fs.ModeSymlink    
	ModeDevice     = fs.ModeDevice     
	ModeNamedPipe  = fs.ModeNamedPipe  
	ModeSocket     = fs.ModeSocket     
	ModeSetuid     = fs.ModeSetuid     
	ModeSetgid     = fs.ModeSetgid     
	ModeCharDevice = fs.ModeCharDevice 
	ModeSticky     = fs.ModeSticky     
	ModeIrregular  = fs.ModeIrregular  

	
	ModeType = fs.ModeType

	ModePerm = fs.ModePerm 
)
```

The defined file mode bits are the most significant bits of the FileMode. The nine least-significant bits are the standard Unix rwxrwxrwx permissions. The values of these bits should be considered part of the public API and may be used in wire protocols or disk representations: they must not be changed, although new bits might be added.

View Source

```
const DevNull = "/dev/null"
```

DevNull is the name of the operating system's “null device.” On Unix-like systems, it is "/dev/null"; on Windows, "NUL".

### Variables

View Source

```
var (
	
	
	ErrInvalid = fs.ErrInvalid 

	ErrPermission = fs.ErrPermission 
	ErrExist      = fs.ErrExist      
	ErrNotExist   = fs.ErrNotExist   
	ErrClosed     = fs.ErrClosed     

	ErrNoDeadline       = errNoDeadline()       
	ErrDeadlineExceeded = errDeadlineExceeded() 
)
```

Portable analogs of some common system call errors.

Errors returned from this package may be tested against these errors with errors.Is.

View Source

```
var (
	
	ErrProcessDone = errors.New("os: process already finished")

	
	ErrNoHandle = errors.New("os: process handle unavailable")
)
```

View Source

```
var (
	Stdin  = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
	Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
	Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
)
```

Stdin, Stdout, and Stderr are open Files pointing to the standard input, standard output, and standard error file descriptors.

Note that the Go runtime writes to standard error for panics and crashes; closing Stderr may cause those messages to go elsewhere, perhaps to a file opened later.

View Source

```
var Args []string
```

Args hold the command-line arguments, starting with the program name.

### Functions

#### func Chdir

```
func Chdir(dir string) error
```

Chdir changes the current working directory to the named directory. If there is an error, it will be of type *PathError.

#### func Chmod

```
func Chmod(name string, mode FileMode) error
```

Chmod changes the mode of the named file to mode. If the file is a symbolic link, it changes the mode of the link's target. If there is an error, it will be of type *PathError.

A different subset of the mode bits are used, depending on the operating system.

On Unix, the mode's permission bits, ModeSetuid, ModeSetgid, and ModeSticky are used.

On Windows, only the 0o200 bit (owner writable) of mode is used; it controls whether the file's read-only attribute is set or cleared. The other bits are currently unused. For compatibility with Go 1.12 and earlier, use a non-zero mode. Use mode 0o400 for a read-only file and 0o600 for a readable+writable file.

On Plan 9, the mode's permission bits, ModeAppend, ModeExclusive, and ModeTemporary are used.

Example

¶

```
package main

import (
	"log"
	"os"
)

func main() {
	if err := os.Chmod("some-filename", 0644); err != nil {
		log.Fatal(err)
	}
}
```

```
Output:
```

#### func Chown

```
func Chown(name string, uid, gid int) error
```

Chown changes the numeric uid and gid of the named file. If the file is a symbolic link, it changes the uid and gid of the link's target. A uid or gid of -1 means to not change that value. If there is an error, it will be of type *PathError.

On Windows or Plan 9, Chown always returns the syscall.EWINDOWS or syscall.EPLAN9 error, wrapped in *PathError.

#### func Chtimes

```
func Chtimes(name string, atime time.Time, mtime time.Time) error
```

Chtimes changes the access and modification times of the named file, similar to the Unix utime() or utimes() functions. A zero time.Time value will leave the corresponding file time unchanged.

The underlying filesystem may truncate or round the values to a less precise time unit. If there is an error, it will be of type *PathError.

Example

¶

```
package main

import (
	"log"
	"os"
	"time"
)

func main() {
	mtime := time.Date(2006, time.February, 1, 3, 4, 5, 0, time.UTC)
	atime := time.Date(2007, time.March, 2, 4, 5, 6, 0, time.UTC)
	if err := os.Chtimes("some-filename", atime, mtime); err != nil {
		log.Fatal(err)
	}
}
```

```
Output:
```

#### func Clearenv

```
func Clearenv()
```

Clearenv deletes all environment variables.

#### func CopyFS ¶ added in go1.23.0

```
func CopyFS(dir string, fsys fs.FS) error
```

CopyFS copies the file system fsys into the directory dir, creating dir if necessary.

Files are created with mode 0o666 plus any execute permissions from the source, and directories are created with mode 0o777 (before umask).

CopyFS will not overwrite existing files. If a file name in fsys already exists in the destination, CopyFS will return an error such that errors.Is(err, fs.ErrExist) will be true.

Symbolic links in dir are followed.

New files added to fsys (including if dir is a subdirectory of fsys) while CopyFS is running are not guaranteed to be copied.

Copying stops at and returns the first error encountered.

#### func DirFS ¶ added in go1.16

```
func DirFS(dir string) fs.FS
```

DirFS returns a file system (an fs.FS) for the tree of files rooted at the directory dir.

Note that DirFS("/prefix") only guarantees that the Open calls it makes to the operating system will begin with "/prefix": DirFS("/prefix").Open("file") is the same as os.Open("/prefix/file"). So if /prefix/file is a symbolic link pointing outside the /prefix tree, then using DirFS does not stop the access any more than using os.Open does. Additionally, the root of the fs.FS returned for a relative path, DirFS("prefix"), will be affected by later calls to Chdir. DirFS is therefore not a general substitute for a chroot-style security mechanism when the directory tree contains arbitrary content.

Use Root.FS to obtain a fs.FS that prevents escapes from the tree via symbolic links.

The directory dir must not be "".

The result implements io/fs.StatFS, io/fs.ReadFileFS, io/fs.ReadDirFS, and io/fs.ReadLinkFS.

#### func Environ

```
func Environ() []string
```

Environ returns a copy of strings representing the environment, in the form "key=value".

#### func Executable ¶ added in go1.8

```
func Executable() (string, error)
```

Executable returns the path name for the executable that started the current process. There is no guarantee that the path is still pointing to the correct executable. If a symlink was used to start the process, depending on the operating system, the result might be the symlink or the path it pointed to. If a stable result is needed, path/filepath.EvalSymlinks might help.

Executable returns an absolute path unless an error occurred.

The main use case is finding resources located relative to an executable.

#### func Exit

```
func Exit(code int)
```

Exit causes the current program to exit with the given status code. Conventionally, code zero indicates success, non-zero an error. The program terminates immediately; deferred functions are not run.

For portability, the status code should be in the range [0, 125].

#### func Expand

```
func Expand(s string, mapping func(string) string) string
```

Expand replaces ${var} or $var in the string based on the mapping function. For example, os.ExpandEnv(s) is equivalent to os.Expand(s, os.Getenv).

Example

¶

```
package main

import (
	"fmt"
	"os"
)

func main() {
	mapper := func(placeholderName string) string {
		switch placeholderName {
		case "DAY_PART":
			return "morning"
		case "NAME":
			return "Gopher"
		}

		return ""
	}

	fmt.Println(os.Expand("Good ${DAY_PART}, $NAME!", mapper))

}
```

```
Output:
Good morning, Gopher!
```

#### func ExpandEnv

```
func ExpandEnv(s string) string
```

ExpandEnv replaces ${var} or $var in the string according to the values of the current environment variables. References to undefined variables are replaced by the empty string.

Example

¶

```
package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")
	os.Setenv("BURROW", "/usr/gopher")

	fmt.Println(os.ExpandEnv("$NAME lives in ${BURROW}."))

}
```

```
Output:
gopher lives in /usr/gopher.
```

#### func Getegid

```
func Getegid() int
```

Getegid returns the numeric effective group id of the caller.

On Windows, it returns -1.

#### func Getenv

```
func Getenv(key string) string
```

Getenv retrieves the value of the environment variable named by the key. It returns the value, which will be empty if the variable is not present. To distinguish between an empty value and an unset value, use LookupEnv.

Example

¶

```
package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")
	os.Setenv("BURROW", "/usr/gopher")

	fmt.Printf("%s lives in %s.\n", os.Getenv("NAME"), os.Getenv("BURROW"))

}
```

```
Output:
gopher lives in /usr/gopher.
```

#### func Geteuid

```
func Geteuid() int
```

Geteuid returns the numeric effective user id of the caller.

On Windows, it returns -1.

#### func Getgid

```
func Getgid() int
```

Getgid returns the numeric group id of the caller.

On Windows, it returns -1.

#### func Getgroups

```
func Getgroups() ([]int, error)
```

Getgroups returns a list of the numeric ids of groups that the caller belongs to.

On Windows, it returns syscall.EWINDOWS. See the os/user package for a possible alternative.

#### func Getpagesize

```
func Getpagesize() int
```

Getpagesize returns the underlying system's memory page size.

#### func Getpid

```
func Getpid() int
```

Getpid returns the process id of the caller.

#### func Getppid

```
func Getppid() int
```

Getppid returns the process id of the caller's parent.

#### func Getuid

```
func Getuid() int
```

Getuid returns the numeric user id of the caller.

On Windows, it returns -1.

#### func Getwd

```
func Getwd() (dir string, err error)
```

Getwd returns an absolute path name corresponding to the current directory. If the current directory can be reached via multiple paths (due to symbolic links), Getwd may return any one of them.

On Unix platforms, if the environment variable PWD provides an absolute name, and it is a name of the current directory, it is returned.

#### func Hostname

```
func Hostname() (name string, err error)
```

Hostname returns the host name reported by the kernel.

#### func IsExist

```
func IsExist(err error) bool
```

IsExist returns a boolean indicating whether its argument is known to report that a file or directory already exists. It is satisfied by ErrExist as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrExist).

#### func IsNotExist

```
func IsNotExist(err error) bool
```

IsNotExist returns a boolean indicating whether its argument is known to report that a file or directory does not exist. It is satisfied by ErrNotExist as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrNotExist).

#### func IsPathSeparator

```
func IsPathSeparator(c uint8) bool
```

IsPathSeparator reports whether c is a directory separator character.

#### func IsPermission

```
func IsPermission(err error) bool
```

IsPermission returns a boolean indicating whether its argument is known to report that permission is denied. It is satisfied by ErrPermission as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrPermission).

#### func IsTimeout ¶ added in go1.10

```
func IsTimeout(err error) bool
```

IsTimeout returns a boolean indicating whether its argument is known to report that a timeout occurred.

This function predates errors.Is, and the notion of whether an error indicates a timeout can be ambiguous. For example, the Unix error EWOULDBLOCK sometimes indicates a timeout and sometimes does not. New code should use errors.Is with a value appropriate to the call returning the error, such as os.ErrDeadlineExceeded.

#### func Lchown

```
func Lchown(name string, uid, gid int) error
```

Lchown changes the numeric uid and gid of the named file. If the file is a symbolic link, it changes the uid and gid of the link itself. If there is an error, it will be of type *PathError.

On Windows, it always returns the syscall.EWINDOWS error, wrapped in *PathError.

#### func Link

```
func Link(oldname, newname string) error
```

Link creates newname as a hard link to the oldname file. If there is an error, it will be of type *LinkError.

#### func LookupEnv ¶ added in go1.5

```
func LookupEnv(key string) (string, bool)
```

LookupEnv retrieves the value of the environment variable named by the key. If the variable is present in the environment the value (which may be empty) is returned and the boolean is true. Otherwise the returned value will be empty and the boolean will be false.

Example

¶

```
package main

import (
	"fmt"
	"os"
)

func main() {
	show := func(key string) {
		val, ok := os.LookupEnv(key)
		if !ok {
			fmt.Printf("%s not set\n", key)
		} else {
			fmt.Printf("%s=%s\n", key, val)
		}
	}

	os.Setenv("SOME_KEY", "value")
	os.Setenv("EMPTY_KEY", "")

	show("SOME_KEY")
	show("EMPTY_KEY")
	show("MISSING_KEY")

}
```

```
Output:
SOME_KEY=value
EMPTY_KEY=
MISSING_KEY not set
```

#### func Mkdir

```
func Mkdir(name string, perm FileMode) error
```

Mkdir creates a new directory with the specified name and permission bits (before umask). If there is an error, it will be of type *PathError.

Example

¶

```
package main

import (
	"log"
	"os"
)

func main() {
	err := os.Mkdir("testdir", 0750)
	if err != nil && !os.IsExist(err) {
		log.Fatal(err)
	}
	err = os.WriteFile("testdir/testfile.txt", []byte("Hello, Gophers!"), 0660)
	if err != nil {
		log.Fatal(err)
	}
}
```

```
Output:
```

#### func MkdirAll

```
func MkdirAll(path string, perm FileMode) error
```

MkdirAll creates a directory named path, along with any necessary parents, and returns nil, or else returns an error. The permission bits perm (before umask) are used for all directories that MkdirAll creates. If path is already a directory, MkdirAll does nothing and returns nil.

Example

¶

```
package main

import (
	"log"
	"os"
)

func main() {
	err := os.MkdirAll("test/subdir", 0750)
	if err != nil {
		log.Fatal(err)
	}
	err = os.WriteFile("test/subdir/testfile.txt", []byte("Hello, Gophers!"), 0660)
	if err != nil {
		log.Fatal(err)
	}
}
```

```
Output:
```

#### func MkdirTemp ¶ added in go1.16

```
func MkdirTemp(dir, pattern string) (string, error)
```

MkdirTemp creates a new temporary directory in the directory dir and returns the pathname of the new directory. The new directory's name is generated by adding a random string to the end of pattern. If pattern includes a "*", the random string replaces the last "*" instead. The directory is created with mode 0o700 (before umask). If dir is the empty string, MkdirTemp uses the default directory for temporary files, as returned by TempDir. Multiple programs or goroutines calling MkdirTemp simultaneously will not choose the same directory. It is the caller's responsibility to remove the directory when it is no longer needed.

Example

¶

```
package main

import (
	"log"
	"os"
	"path/filepath"
)

func main() {
	dir, err := os.MkdirTemp("", "example")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(dir) // clean up

	file := filepath.Join(dir, "tmpfile")
	if err := os.WriteFile(file, []byte("content"), 0666); err != nil {
		log.Fatal(err)
	}
}
```

```
Output:
```

Example (Suffix)

¶

```
package main

import (
	"log"
	"os"
	"path/filepath"
)

func main() {
	logsDir, err := os.MkdirTemp("", "*-logs")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(logsDir) // clean up

	// Logs can be cleaned out earlier if needed by searching
	// for all directories whose suffix ends in *-logs.
	globPattern := filepath.Join(os.TempDir(), "*-logs")
	matches, err := filepath.Glob(globPattern)
	if err != nil {
		log.Fatalf("Failed to match %q: %v", globPattern, err)
	}

	for _, match := range matches {
		if err := os.RemoveAll(match); err != nil {
			log.Printf("Failed to remove %q: %v", match, err)
		}
	}
}
```

```
Output:
```

#### func NewSyscallError

```
func NewSyscallError(syscall string, err error) error
```

NewSyscallError returns, as an error, a new SyscallError with the given system call name and error details. As a convenience, if err is nil, NewSyscallError returns nil.

#### func Pipe

```
func Pipe() (r *File, w *File, err error)
```

Pipe returns a connected pair of Files; reads from r return bytes written to w. It returns the files and an error, if any.

#### func ReadFile ¶ added in go1.16

```
func ReadFile(name string) ([]byte, error)
```

ReadFile reads the named file and returns the contents. A successful call returns err == nil, not err == EOF. Because ReadFile reads the whole file, it does not treat an EOF from Read as an error to be reported.

Example

¶

```
package main

import (
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("testdata/hello")
	if err != nil {
		log.Fatal(err)
	}
	os.Stdout.Write(data)

}
```

```
Output:
Hello, Gophers!
```

#### func Readlink

```
func Readlink(name string) (string, error)
```

Readlink returns the destination of the named symbolic link. If there is an error, it will be of type *PathError.

If the link destination is relative, Readlink returns the relative path without resolving it to an absolute one.

Example

¶

```
package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	// First, we create a relative symlink to a file.
	d, err := os.MkdirTemp("", "")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(d)
	targetPath := filepath.Join(d, "hello.txt")
	if err := os.WriteFile(targetPath, []byte("Hello, Gophers!"), 0644); err != nil {
		log.Fatal(err)
	}
	linkPath := filepath.Join(d, "hello.link")
	if err := os.Symlink("hello.txt", filepath.Join(d, "hello.link")); err != nil {
		if errors.Is(err, errors.ErrUnsupported) {
			// Allow the example to run on platforms that do not support symbolic links.
			fmt.Printf("%s links to %s\n", filepath.Base(linkPath), "hello.txt")
			return
		}
		log.Fatal(err)
	}

	// Readlink returns the relative path as passed to os.Symlink.
	dst, err := os.Readlink(linkPath)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s links to %s\n", filepath.Base(linkPath), dst)

	var dstAbs string
	if filepath.IsAbs(dst) {
		dstAbs = dst
	} else {
		// Symlink targets are relative to the directory containing the link.
		dstAbs = filepath.Join(filepath.Dir(linkPath), dst)
	}

	// Check that the target is correct by comparing it with os.Stat
	// on the original target path.
	dstInfo, err := os.Stat(dstAbs)
	if err != nil {
		log.Fatal(err)
	}
	targetInfo, err := os.Stat(targetPath)
	if err != nil {
		log.Fatal(err)
	}
	if !os.SameFile(dstInfo, targetInfo) {
		log.Fatalf("link destination (%s) is not the same file as %s", dstAbs, targetPath)
	}

}
```

```
Output:
hello.link links to hello.txt
```

#### func Remove

```
func Remove(name string) error
```

Remove removes the named file or (empty) directory. If there is an error, it will be of type *PathError.

#### func RemoveAll

```
func RemoveAll(path string) error
```

RemoveAll removes path and any children it contains. It removes everything it can but returns the first error it encounters. If the path does not exist, RemoveAll returns nil (no error). If there is an error, it will be of type *PathError.

#### func Rename

```
func Rename(oldpath, newpath string) error
```

Rename renames (moves) oldpath to newpath. If newpath already exists and is not a directory, Rename replaces it. If newpath already exists and is a directory, Rename returns an error. OS-specific restrictions may apply when oldpath and newpath are in different directories. Even within the same directory, on non-Unix platforms Rename is not an atomic operation. If there is an error, it will be of type *LinkError.

#### func SameFile

```
func SameFile(fi1, fi2 FileInfo) bool
```

SameFile reports whether fi1 and fi2 describe the same file. For example, on Unix this means that the device and inode fields of the two underlying structures are identical; on other systems the decision may be based on the path names. SameFile only applies to results returned by this package's Stat. It returns false in other cases.

#### func Setenv

```
func Setenv(key, value string) error
```

Setenv sets the value of the environment variable named by the key. It returns an error, if any.

#### func Symlink

```
func Symlink(oldname, newname string) error
```

Symlink creates newname as a symbolic link to oldname. On Windows, a symlink to a non-existent oldname creates a file symlink; if oldname is later created as a directory the symlink will not work. If there is an error, it will be of type *LinkError.

#### func TempDir

```
func TempDir() string
```

TempDir returns the default directory to use for temporary files.

On Unix systems, it returns $TMPDIR if non-empty, else /tmp. On Windows, it uses GetTempPath, returning the first non-empty value from %TMP%, %TEMP%, %USERPROFILE%, or the Windows directory. On Plan 9, it returns /tmp.

The directory is neither guaranteed to exist nor have accessible permissions.

#### func Truncate

```
func Truncate(name string, size int64) error
```

Truncate changes the size of the named file. If the file is a symbolic link, it changes the size of the link's target. If there is an error, it will be of type *PathError.

#### func Unsetenv ¶ added in go1.4

```
func Unsetenv(key string) error
```

Unsetenv unsets a single environment variable.

Example

¶

```
package main

import (
	"os"
)

func main() {
	os.Setenv("TMPDIR", "/my/tmp")
	defer os.Unsetenv("TMPDIR")
}
```

```
Output:
```

#### func UserCacheDir ¶ added in go1.11

```
func UserCacheDir() (string, error)
```

UserCacheDir returns the default root directory to use for user-specific cached data. Users should create their own application-specific subdirectory within this one and use that.

On Unix systems, it returns $XDG_CACHE_HOME as specified by https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html if non-empty, else $HOME/.cache. On Darwin, it returns $HOME/Library/Caches. On Windows, it returns %LocalAppData%. On Plan 9, it returns $home/lib/cache.

If the location cannot be determined (for example, $HOME is not defined) or the path in $XDG_CACHE_HOME is relative, then it will return an error.

Example

¶

```
package main

import (
	"log"
	"os"
	"path/filepath"
	"sync"
)

func main() {
	dir, dirErr := os.UserCacheDir()
	if dirErr == nil {
		dir = filepath.Join(dir, "ExampleUserCacheDir")
	}

	getCache := func(name string) ([]byte, error) {
		if dirErr != nil {
			return nil, &os.PathError{Op: "getCache", Path: name, Err: os.ErrNotExist}
		}
		return os.ReadFile(filepath.Join(dir, name))
	}

	var mkdirOnce sync.Once
	putCache := func(name string, b []byte) error {
		if dirErr != nil {
			return &os.PathError{Op: "putCache", Path: name, Err: dirErr}
		}
		mkdirOnce.Do(func() {
			if err := os.MkdirAll(dir, 0700); err != nil {
				log.Printf("can't create user cache dir: %v", err)
			}
		})
		return os.WriteFile(filepath.Join(dir, name), b, 0600)
	}

	// Read and store cached data.
	// …
	_ = getCache
	_ = putCache

}
```

```
Output:
```

#### func UserConfigDir ¶ added in go1.13

```
func UserConfigDir() (string, error)
```

UserConfigDir returns the default root directory to use for user-specific configuration data. Users should create their own application-specific subdirectory within this one and use that.

On Unix systems, it returns $XDG_CONFIG_HOME as specified by https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html if non-empty, else $HOME/.config. On Darwin, it returns $HOME/Library/Application Support. On Windows, it returns %AppData%. On Plan 9, it returns $home/lib.

If the location cannot be determined (for example, $HOME is not defined) or the path in $XDG_CONFIG_HOME is relative, then it will return an error.

Example

¶

```
package main

import (
	"bytes"
	"log"
	"os"
	"path/filepath"
)

func main() {
	dir, dirErr := os.UserConfigDir()

	var (
		configPath string
		origConfig []byte
	)
	if dirErr == nil {
		configPath = filepath.Join(dir, "ExampleUserConfigDir", "example.conf")
		var err error
		origConfig, err = os.ReadFile(configPath)
		if err != nil && !os.IsNotExist(err) {
			// The user has a config file but we couldn't read it.
			// Report the error instead of ignoring their configuration.
			log.Fatal(err)
		}
	}

	// Use and perhaps make changes to the config.
	config := bytes.Clone(origConfig)
	// …

	// Save changes.
	if !bytes.Equal(config, origConfig) {
		if configPath == "" {
			log.Printf("not saving config changes: %v", dirErr)
		} else {
			err := os.MkdirAll(filepath.Dir(configPath), 0700)
			if err == nil {
				err = os.WriteFile(configPath, config, 0600)
			}
			if err != nil {
				log.Printf("error saving config changes: %v", err)
			}
		}
	}

}
```

```
Output:
```

#### func UserHomeDir ¶ added in go1.12

```
func UserHomeDir() (string, error)
```

UserHomeDir returns the current user's home directory.

On Unix, including macOS, it returns the $HOME environment variable. On Windows, it returns %USERPROFILE%. On Plan 9, it returns the $home environment variable.

If the expected variable is not set in the environment, UserHomeDir returns either a platform-specific default value or a non-nil error.

#### func WriteFile ¶ added in go1.16

```
func WriteFile(name string, data []byte, perm FileMode) error
```

WriteFile writes data to the named file, creating it if necessary. If the file does not exist, WriteFile creates it with permissions perm (before umask); otherwise WriteFile truncates it before writing, without changing permissions. Since WriteFile requires multiple system calls to complete, a failure mid-operation can leave the file in a partially written state.

Example

¶
