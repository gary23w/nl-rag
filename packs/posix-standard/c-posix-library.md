---
title: "C POSIX library"
source: https://en.wikipedia.org/wiki/C_POSIX_library
domain: posix-standard
license: CC-BY-SA-4.0
tags: posix, single unix specification, posix library, filesystem hierarchy standard
fetched: 2026-07-02
---

# C POSIX library

The **C POSIX library** is a specification of a C standard library for POSIX systems. It was developed at the same time as the ANSI C standard. Some effort was made to make POSIX compatible with standard C; POSIX includes additional functions to those introduced in standard C. On the other hand, the 5 headers that were added to the C standard library with C11, were not likewise included in subsequent revisions of POSIX.

It may be included in any C++ project, however the C++ standard library may have its own implementation of certain features, such as `<regex>` rather than `<regex.h>`, `<thread>` rather than `<pthread.h>`, or `<semaphore>` rather than `<semaphore.h>`.

## C POSIX library header files

| Header file | Description | First released | C Standard |
|---|---|---|---|
| **`<aio.h>`** | Asynchronous input and output | Issue 5 |   |
| **`<arpa/inet.h>`** | Functions for manipulating numeric IP addresses (part of Berkeley sockets) | Issue 6 |   |
| **`<assert.h>`** | Verify assumptions | Issue 1 | ANSI (89) |
| **`<complex.h>`** | Complex Arithmetic, see C mathematical functions | Issue 6 | C99 |
| **`<cpio.h>`** | Magic numbers for the cpio archive format | Issue 3 |   |
| **`<ctype.h>`** | Character types | Issue 1 | ANSI (89) |
| **`<devctl.h>`** | Device control | Issue 8 |   |
| **`<dirent.h>`** | Allows the opening and listing of directories | Issue 2 |   |
| **`<dlfcn.h>`** | Dynamic linking | Issue 5 |   |
| **`<errno.h>`** | Retrieving Error Number | Issue 1 | ANSI (89) |
| **`<endian.h>`** | Endianness operations | Issue 8 |   |
| **`<fcntl.h>`** | File opening, locking and other operations | Issue 1 |   |
| **`<fenv.h>`** | Floating-Point Environment (FPE), see C mathematical functions | Issue 6 | C99 |
| **`<float.h>`** | Floating-point types, see C data types | Issue 4 | ANSI (89) |
| **`<fmtmsg.h>`** | Message display structures | Issue 4 |   |
| **`<fnmatch.h>`** | Filename matching | Issue 4 |   |
| **`<ftw.h>`** | File tree traversal | Issue 1 |   |
| **`<glob.h>`** | Pathname "globbing" (pattern-matching) | Issue 4 |   |
| **`<grp.h>`** | User group information and control | Issue 1 |   |
| **`<iconv.h>`** | Codeset conversion facility | Issue 4 |   |
| **`<inttypes.h>`** | Fixed sized integer types, see C data types | Issue 5 | C99 |
| **`<iso646.h>`** | Alternative spellings, see C alternative tokens | Issue 5 | NA1 (95) |
| **`<langinfo.h>`** | Language information constants – builds on C localization functions | Issue 2 |   |
| **`<libgen.h>`** | Pathname manipulation | Issue 4 |   |
| **`<libintl.h>`** | Internationalization | Issue 8 |   |
| **`<limits.h>`** | Implementation-defined constants, see C data types | Issue 1 | ANSI (89) |
| **`<locale.h>`** | Category macros, see C localization functions | Issue 3 | ANSI (89) |
| **`<math.h>`** | Mathematical declarations, see C mathematical functions | Issue 1 | ANSI (89) |
| **`<monetary.h>`** | String formatting of monetary units | Issue 4 |   |
| **`<mqueue.h>`** | Message queue | Issue 5 |   |
| **`<ndbm.h>`** | NDBM database operations | Issue 4 |   |
| **`<net/if.h>`** | Listing of local network interfaces | Issue 6 |   |
| **`<netdb.h>`** | Translating protocol and host names into numeric addresses (part of Berkeley sockets) | Issue 6 |   |
| **`<netinet/in.h>`** | Defines Internet protocol and address family (part of Berkeley sockets) | Issue 6 |   |
| **`<netinet/tcp.h>`** | Additional TCP control options (part of Berkeley sockets) | Issue 6 |   |
| **`<nl_types.h>`** | Localization message catalog functions | Issue 2 |   |
| **`<poll.h>`** | Asynchronous file descriptor multiplexing | Issue 4 |   |
| **`<pthread.h>`** | Defines an API for creating and manipulating POSIX threads | Issue 5 |   |
| **`<pwd.h>`** | passwd (user information) access and control | Issue 1 |   |
| **`<regex.h>`** | Regular expression matching | Issue 4 |   |
| **`<sched.h>`** | Execution scheduling | Issue 5 |   |
| **`<search.h>`** | Search tables | Issue 1 |   |
| **`<semaphore.h>`** | POSIX semaphores | Issue 5 |   |
| **`<setjmp.h>`** | Stack environment declarations | Issue 1 | ANSI (89) |
| **`<signal.h>`** | Signals, see C signal handling | Issue 1 | ANSI (89) |
| **`<spawn.h>`** | Process spawning | Issue 6 |   |
| **`<stdalign.h>`** | Alignment macros | Issue 8 | C11 |
| **`<stdarg.h>`** | Handle Variable Argument List | Issue 4 | ANSI (89) |
| **`<stdatomic.h>`** | Atomic operations | Issue 8 | C11 |
| **`<stdbool.h>`** | Boolean type and values, see C data types | Issue 6 | C99 |
| **`<stddef.h>`** | Standard type definitions, see C data types | Issue 4 | ANSI (89) |
| **`<stdint.h>`** | Integer types, see C data types | Issue 6 | C99 |
| **`<stdio.h>`** | Standard buffered input/output, see C file input/output | Issue 1 | ANSI (89) |
| **`<stdlib.h>`** | Standard library definitions, see C standard library | Issue 3 | ANSI (89) |
| **`<stdnoreturn.h>`** | The `noreturn` macro | Issue 8 | C11 |
| **`<string.h>`** | Several String Operations, see C string handling | Issue 1 | ANSI (89) |
| **`<strings.h>`** | Case-insensitive string comparisons | Issue 4 |   |
| **`<stropts.h>`** | Stream manipulation, including ioctl | Issue 4 |   |
| **`<sys/ipc.h>`** | Inter-process communication (IPC) | Issue 2 |   |
| **`<sys/mman.h>`** | Memory management, including POSIX shared memory and memory mapped files | Issue 4 |   |
| **`<sys/msg.h>`** | POSIX message queues | Issue 2 |   |
| **`<sys/resource.h>`** | Resource usage, priorities, and limiting | Issue 4 |   |
| **`<sys/select.h>`** | Synchronous I/O multiplexing | Issue 6 |   |
| **`<sys/sem.h>`** | XSI (SysV style) semaphores | Issue 2 |   |
| **`<sys/shm.h>`** | XSI (SysV style) shared memory | Issue 2 |   |
| **`<sys/socket.h>`** | Main Berkeley sockets header | Issue 6 |   |
| **`<sys/stat.h>`** | File information (stat et al.) | Issue 1 |   |
| **`<sys/statvfs.h>`** | File System information | Issue 4 |   |
| **`<sys/time.h>`** | Time and date functions and structures | Issue 4 |   |
| **`<sys/times.h>`** | File access and modification times | Issue 1 |   |
| **`<sys/types.h>`** | Various data types used elsewhere | Issue 1 |   |
| **`<sys/uio.h>`** | Vectored I/O operations | Issue 4 |   |
| **`<sys/un.h>`** | Unix domain sockets | Issue 6 |   |
| **`<sys/utsname.h>`** | Operating system information, including uname | Issue 1 |   |
| **`<sys/wait.h>`** | Status of terminated child processes (see wait) | Issue 3 |   |
| **`<syslog.h>`** | System error logging | Issue 4 |   |
| **`<tar.h>`** | Magic numbers for the tar archive format | Issue 3 |   |
| **`<termios.h>`** | Allows terminal I/O interfaces | Issue 3 |   |
| **`<tgmath.h>`** | Type-Generic Macros, see C mathematical functions | Issue 6 | C99 |
| **`<threads.h>`** | ISO C threads | Issue 8 | C11 |
| **`<time.h>`** | Type-Generic Macros, see C date and time functions | Issue 1 | ANSI (89) |
| **`<trace.h>`** | Tracing of runtime behavior (DEPRECATED) | Issue 6 |   |
| **`<ucontext.h>`** | manipulate user context (REMOVED in POSIX.1-2008) |   |   |
| **`<ulimit.h>`** | Resource limiting (DEPRECATED in favor of <sys/resource.h>) | Issue 1 |   |
| **`<unistd.h>`** | Various essential POSIX functions and constants | Issue 1 |   |
| **`<utime.h>`** | inode access and modification times | Issue 3 |   |
| **`<utmpx.h>`** | User accounting database functions | Issue 4 |   |
| **`<wchar.h>`** | Wide-Character Handling, see C string handling | Issue 4 | NA1 (95) |
| **`<wctype.h>`** | Wide-Character Classification and Mapping Utilities, see C character classification | Issue 5 | NA1 (95) |
| **`<wordexp.h>`** | Word-expansion like the shell would perform | Issue 4 |   |
