---
title: "Memory-mapped file"
source: https://en.wikipedia.org/wiki/Memory-mapped_file
domain: memory-mapped-files
license: CC-BY-SA-4.0
tags: memory-mapped files, mmap, madvise, msync
fetched: 2026-07-02
---

# Memory-mapped file

A **memory-mapped file** is a segment of virtual memory that has been assigned a direct byte-for-byte correlation with some portion of a file or file-like resource. This resource is typically a file that is physically present on disk, but can also be a device, shared memory object, or other resource that an operating system can reference through a file descriptor. Once present, this correlation between the file and the memory space permits applications to treat the mapped portion as if it were primary memory.

## History

### TOPS-20 PMAP

An early (c. 1969) implementation of this was the **PMAP** system call on the DEC-20's TOPS-20 operating system, a feature used by Software House's System-1022 database system.

### SunOS 4 mmap

SunOS 4 introduced Unix's `mmap`, which permitted programs "to map files into memory."

### Windows Growable Memory-Mapped Files (GMMF)

Two decades after the release of TOPS-20's PMAP, Windows NT was given Growable Memory-Mapped Files (GMMF).

Since "`CreateFileMapping` function requires a size to be passed to it" and altering a file's size is not readily accommodated, a GMMF API was developed. Use of GMMF requires declaring the maximum to which the file size can grow, but no unused space is wasted.

## Benefits

The benefit of memory mapping a file is increasing I/O performance, especially when used on large files. For small files, memory-mapped files can result in a waste of slack space as memory maps are always aligned to the page size, which is mostly 4 KiB. Therefore, a 5 KiB file will allocate 8 KiB and thus 3 KiB are wasted. Accessing memory mapped files is faster than using direct read and write operations for two reasons. Firstly, a system call is orders of magnitude slower than a simple change to a program's local memory. Secondly, in most operating systems the memory region mapped actually *is* the kernel's page cache (file cache), meaning that no copies need to be created in user space.

Certain application-level memory-mapped file operations also perform better than their physical file counterparts. Applications can access and update data in the file directly and in-place, as opposed to seeking from the start of the file or rewriting the entire edited contents to a temporary location. Since the memory-mapped file is handled internally in pages, linear file access (as seen, for example, in flat file data storage or configuration files) requires disk access only when a new page boundary is crossed, and can write larger sections of the file to disk in a single operation.

A possible benefit of memory-mapped files is a "lazy loading", thus using small amounts of RAM even for a very large file. Trying to load the entire contents of a file that is significantly larger than the amount of memory available can cause severe thrashing as the operating system reads from disk into memory and simultaneously writes pages from memory back to disk. Memory-mapping may not only bypass the page file completely, but also allow smaller page-sized sections to be loaded as data is being edited, similarly to demand paging used for programs.

The memory mapping process is handled by the virtual memory manager, which is the same subsystem responsible for dealing with the page file. Memory mapped files are loaded into memory one entire page at a time. The page size is selected by the operating system for maximum performance. Since page file management is one of the most critical elements of a virtual memory system, loading page sized sections of a file into physical memory is typically a very highly optimized system function.

## Types

There are two types of memory-mapped files:

### Persisted

Persisted files are associated with a source file on a disk. The data is saved to the source file on the disk once the last process is finished. These memory-mapped files are suitable for working with extremely large source files.

### Non-persisted

Non-persisted files are not associated with a file on a disk. When the last process has finished working with the file, the data is lost. These files are suitable for creating shared memory for inter-process communications (IPC).

## Drawbacks

The major reason to choose memory mapped file I/O is performance. Nevertheless, there can be tradeoffs. The standard I/O approach is costly due to system call overhead and memory copying. The memory-mapped approach has its cost in minor page faults—when a block of data is loaded in page cache, but is not yet mapped into the process's virtual memory space. In some circumstances, memory mapped file I/O can be substantially slower than standard file I/O.

Another drawback of memory-mapped files relates to a given architecture's address space: a file larger than the addressable space can have only portions mapped at a time, complicating reading it. For example, a 32-bit architecture such as Intel's IA-32 can only directly address 4 GiB or smaller portions of files. An even smaller amount of addressable space is available to individual programs—typically in the range of 2 to 3 GiB, depending on the operating system kernel. This drawback however is virtually eliminated on modern 64-bit architecture.

mmap also tends to be less scalable than standard means of file I/O, since many operating systems, including Linux, have a cap on the number of cores handling page faults. Extremely fast devices, such as modern NVM Express SSDs, are capable of making the overhead a real concern.

I/O errors on the underlying file (e.g. its removable drive is unplugged or optical media is ejected, disk full when writing, etc.) while accessing its mapped memory are reported to the application as the SIGSEGV/SIGBUS signals on POSIX, and the EXECUTE_IN_PAGE_ERROR structured exception on Windows. All code accessing mapped memory must be prepared to handle these errors, which don't normally occur when accessing memory.

Only hardware architectures with an MMU can support memory-mapped files. On architectures without an MMU, the operating system can copy the entire file into memory when the request to map it is made, but this is extremely wasteful and slow if only a little bit of the file will be accessed, and can only work for files that will fit in available memory.

## Common uses

Perhaps the most common use for a memory-mapped file is the process loader in most modern operating systems (including Windows and Unix-like systems.) When a process is started, the operating system uses a memory mapped file to bring the executable file, along with any loadable modules, into memory for execution. Most memory-mapping systems use a technique called demand paging, where the file is loaded into physical memory in subsets (one page each), and only when that page is actually referenced. In the specific case of executable files, this permits the OS to selectively load only those portions of a process image that actually need to execute.

Another common use for memory-mapped files is to share memory between multiple processes. In modern protected mode operating systems, processes are generally not permitted to access memory space that is allocated for use by another process. (A program's attempt to do so causes invalid page faults or segmentation violations.) There are a number of techniques available to safely share memory, and memory-mapped file I/O is one of the most popular. Two or more applications can simultaneously map a single physical file into memory and access this memory. For example, the Microsoft Windows operating system provides a mechanism for applications to memory-map a shared segment of the system's page file itself and share data via this section.

## Platform support

Most modern operating systems or runtime environments support some form of memory-mapped file access. The function mmap(), which creates a mapping of a file given a file descriptor, starting location in the file, and a length, is part of the POSIX specification, so the wide variety of POSIX-compliant systems, such as UNIX, Linux, Mac OS X or OpenVMS, support a common mechanism for memory mapping files. The Microsoft Windows operating systems also support a group of API functions for this purpose, such as CreateFileMapping().

Some free portable implementations of memory-mapped files for Microsoft Windows and POSIX-compliant platforms are:

- Boost.Interprocess, in Boost C++ Libraries
- Boost.Iostreams, also in Boost C++ Libraries
- Fmstream
- Cpp-mmf

The Java programming language provides classes and methods to access memory mapped files, such as `FileChannel`. Furthermore, Java uses memory-mapped approach to load specific classes to decrease the class loading time in JVM - Java Class Data Sharing.

The D programming language supports memory mapped files in its standard library (std.mmfile module)..

Ruby has a gem (library) called Mmap, which implements memory-mapped file objects.

Rust does not provide any mmap functionality in the standard library but there exists a third-party crate (library) called memmap2.

Since version 1.6, Python has included a mmap module in its Standard Library. Details of the module vary according to whether the host platform is Windows or Unix-like.

For Perl there are several modules available for memory mapping files on the CPAN, such as Sys::Mmap and File::Map.

In the Microsoft .NET runtime, P/Invoke can be used to use memory mapped files directly through the Windows API. Managed access (P/Invoke not necessary) to memory mapped files was introduced in version 4 of the runtime (see Memory-Mapped Files). For previous versions, there are third-party libraries which provide managed API's. .NET have the `MemoryMappedFile` class.

PHP supported memory-mapping techniques in a number of native file access functions such as `file_get_contents()` but has removed this in 5.3 (see revision log).

For the R programming language there exists a library on CRAN called bigmemory which uses the Boost library and provides memory-mapped backed arrays directly in R. The package ff offers memory-mapped vectors, matrices, arrays and data frames.

The J programming language has supported memory-mapped files since at least 2005. It includes support for boxed array data, and single datatype files. Support can be loaded from 'data/jmf' J's Jdb and JD database engines use memory-mapped files for column stores.

The Julia programming language has support for I/O of memory-mapped binary files through the `Mmap` module within the Standard Library.
