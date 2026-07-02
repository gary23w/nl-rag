---
title: "Non-blocking I/O (Java)"
source: https://en.wikipedia.org/wiki/Non-blocking_I/O_(Java)
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
---

# Non-blocking I/O (Java)

**java.nio** (where **nio** stands for "**New Input/Output**") is a collection of Java programming language APIs that offer features for intensive I/O operations. It was introduced with the J2SE 1.4 release of Java by Sun Microsystems to complement an existing standard I/O. NIO was developed under the Java Community Process as JSR 51. An extension to NIO that offers a new file system API, called NIO.2, was released with Java SE 7 ("Dolphin").

## Features and organization

The APIs of NIO were designed to provide access to the low-level I/O operations of modern operating systems. Although the APIs are themselves relatively high-level, the intent is to facilitate an implementation that can directly use the most efficient operations of the underlying platform.

The Java NIO APIs are provided in the `java.nio` package and its subpackages. The documentation by Oracle identifies these features.

- Buffers for data of primitive types
- Character set encoders and decoders
- A pattern-matching facility based on Perl-style regular expressions (in package `java.util.regex`)
- Channels, a new primitive I/O abstraction
- A file interface that supports locks and memory mapping of files up to `Integer.MAX_VALUE` bytes (2 GiB)
- A multiplexed, non-blocking I/O facility for writing scalable servers

### NIO buffers

NIO data transfer is based on buffers (`java.nio.Buffer` and related classes). These classes represent a contiguous extent of memory, together with a small number of data transfer operations. Although theoretically these are general-purpose data structures, the implementation may select memory for alignment or paging characteristics, which are not otherwise accessible in Java. Typically, this would be used to allow the buffer contents to occupy the same physical memory used by the underlying operating system for its native I/O operations, thus allowing the most direct transfer mechanism, and eliminating the need for any additional copying. In most operating systems, provided the particular area of memory has the right properties, transfer can take place without using the CPU at all. The NIO buffer is intentionally limited in features in order to support these goals.

There are buffer classes for all of Java's primitive types except `boolean`, which can share memory with byte buffers and allow arbitrary interpretation of the underlying bytes.

#### Usage

NIO buffers maintain several pointers that dictate the function of their accessor methods. The NIO buffer implementation contains a rich set of methods for modifying these pointers:

- The `flip()` method, rather than performing a "flip" or paging function in the canonical sense, moves the *position* pointer to the origin of the underlying array (if any) and the *limit* pointer to the former position of the *position* pointer.
- Three `get()` methods are supplied for transferring data out of a NIO buffer. The bulk implementation, rather than performing a "get" in the traditional sense, "puts" the data into a specified array. The "offset" argument supplied to this method refers not to the offset from within the buffer from which to read, nor an offset from the *position* pointer, but rather the offset from 0 within the target array.
- Unless using the absolute `get()` and `put()` methods, any `get()` or `put()` is conducted from the *position* pointer. Should one need to read from a different position within the underlying array, whilst not adjusting the *writing* position, the `mark()` and `reset()` methods have been supplied.
- The `mark()` method effectively stores the position of the *position* pointer by setting the *mark* pointer to the position of the *position* pointer. The `reset()` method causes the *position* pointer to move to the *mark* pointer's position.
- Upon invocation of the `clear()` method or the `flip()` method the *mark* pointer is discarded.
- The `clear()` method does not ensure zero-ing of the buffer, but does return the *limit* pointer to the upper boundary of the underlying array, and the *position* pointer to zero.
- `put()` and `get()` operations for NIO buffers are not thread safe.
- `java.nio.MappedByteBuffer` may only `map()` from a `java.nio.channels.FileChannel` up to `Integer.MAX_VALUE` in size (2GiB); regions beyond this limit can be accessed using an offset greater than zero.

### Channels

Channels (classes implementing the interface `java.nio.channels.Channel`) are designed to provide for bulk data transfers to and from NIO buffers. This is a low-level data transfer mechanism that exists in parallel with the classes of the higher-level I/O library (packages `java.io` and `java.net`). A channel implementation can be obtained from a high-level data transfer class such as `java.io.File`, `java.net.ServerSocket`, or `java.net.Socket`, and vice versa. Channels are analogous to "file descriptors" found in Unix-like operating systems.

File channels (`java.nio.channels.FileChannel`) can use arbitrary buffers but can also establish a buffer directly mapped to file contents using memory-mapped file. They can also interact with file system locks. Similarly, socket channels (`java.nio.channels.SocketChannel` and `java.nio.channels.ServerSocketChannel`) allow for data transfer between sockets and NIO buffers.

`FileChannel` can be used to do a file copy, which is potentially far more efficient than using old read/write with a byte array. The typical code for this is:

```mw
import java.nio.channels.FileChannel;
import java.nio.file.StandardOpenOption;

// Getting file channels
try (FileChannel in = FileChannel.open(source, StandardOpenOption.READ); FileChannel out = FileChannel.open(target, StandardOpenOption.WRITE)) {
    // The JVM will attempt to perform this using native I/O operations.
    in.transferTo(0, in.size(), out);
}
```

### Selectors

A selector (`java.nio.channels.Selector` and subclasses) provides a mechanism for waiting on channels and recognizing when one or more become available for data transfer. When a number of channels are registered with the selector, it enables blocking of the program flow until at least one channel is ready for use, or until an interruption condition occurs.

Although this multiplexing behavior could be implemented with threads, the selector can provide a significantly more efficient implementation using lower-level operating system constructs. A POSIX-compliant operating system, for example, would have direct representations of these concepts, select(). A notable application of this design would be the common paradigm in server software which involves simultaneously waiting for responses on a number of sessions.

### Character sets

In Java, a character set is a mapping between Unicode characters (or a subset of them) and bytes. The `java.nio.charset` package of NIO provides facilities for identifying character sets and providing encoding and decoding algorithms for new mappings.

### Reception

It is unexpected that a `java.nio.channels.Channel` associated with a `java.io.RandomAccessFile` closes the file descriptor on an interrupt, whereas `java.io.RandomAccessFile`s' associated `java.nio.channels.FileChannel` does do this.

## JDK 7 and NIO.2

JDK 7 includes a `java.nio.file` package which, with the `Path` class (also new to JDK 7), among other features, provides extended capabilities for filesystem tasks, e.g. can work with symbolic/hard links and dump big directory listings into buffers more quickly than the old File class does. The `java.nio.file` package and its related package, `java.nio.file.attribute`, provide comprehensive support for file I/O and for accessing the file system. A zip file system provider is also available in JDK 7.

The `java.nio.file.LinkOption` is an example of emulating extensible enums with interfaces. In Java, it is not possible to have one `java.lang.Enum` extend another `Enum`. However, it is possible to emulate an extensible `Enum` type by having an `Enum` implement one or more interfaces. `LinkOption` is an enum type that implements both the `java.nio.file.OpenOption` and `java.nio.file.CopyOption` interfaces, which emulates the effects of an extensible `Enum` type. A small down-side to this approach is that implementations cannot be inherited between various `Enum` types.
