---
title: "Handle (computing)"
source: https://en.wikipedia.org/wiki/Handle_(computing)
domain: win32-api
license: CC-BY-SA-4.0
tags: win32 api, windows api, windows programming, dynamic-link library
fetched: 2026-07-02
---

# Handle (computing)

In computer programming, a **handle** is an abstract reference to a resource that is used when application software references blocks of memory or objects that are managed by another system like a database or an operating system.

A resource handle can be an opaque identifier, in which case it is often an integer number (often an array index in an array or "table" that is used to manage that type of resource), or it can be a pointer that allows access to further information. Common resource handles include file descriptors, network sockets, database connections, process identifiers (PIDs), and job IDs. PIDs and job IDs are explicitly visible integers; while file descriptors and sockets (which are often implemented as a form of file descriptor) are represented as integers, they are typically considered opaque. In traditional implementations, file descriptors are indices into a (per-process) file descriptor table, thence a (system-wide) file table.

## Comparison to pointers

While a pointer contains the address of the item to which it refers, a handle is an abstraction of a reference which is managed externally; its opacity allows the referent to be relocated in memory by the system without invalidating the handle, making it similar to virtual memory for pointers, but even more abstracted. Similarly, the extra layer of indirection also increases the control that the managing system has over the operations performed on the referent. Typically the handle is an index or a pointer into a global array of tombstones.

A handle leak is a type of software bug that occurs when a computer program does not free a handle that it previously allocated. This is a form of resource leak, analogous to a memory leak for previously allocated memory.

## Security

In secure computing terms, because access to a resource via a handle is mediated by another system, a handle functions as a *capability*: it not only identifies an object, but also associates access rights. For example, while a filename is forgeable (it is just a guessable identifier), a handle is *given* to a user by an external system, and thus represents not just identity, but also *granted* access.

For example, if a program wishes to read the system password file (`/etc/passwd`) in read/write mode (`O_RDWR`), it could try to open the file via the following call:

```mw
int fd = open("/etc/passwd", O_RDWR);
```

This call asks the operating system to open the specified file with the specified access rights. If the OS allows this, then it opens the file (creates an entry in the per-process file descriptor table) and returns a handle (file descriptor, index into this table) to the user: the actual access is controlled by the OS, and the handle is a token of that. Conversely, the OS may deny access, and thus neither open the file nor return a handle.

In a capability-based system, handles can be passed between processes, with associated access rights. Note that in these cases the handle must be something other than a systemwide-unique small integer, otherwise it is forgeable. Such an integer may nevertheless be used to identify a capability inside a process; e.g., file descriptor in Linux is unforgeable because its numerical value alone is meaningless, and only in the process context may refer to anything. Transferring such a handle requires special care though, as its value often has to be different in the sending and receiving processes.

In non-capability-based systems, on the other hand, each process must acquire its own separate handle, by specifying the identity of the resource and the desired access rights (e.g., each process must open a file itself, by giving the filename and access mode). Such usage is more common even in modern systems that do support passing handles, but it is subject to vulnerabilities like the confused deputy problem.

## Examples

Handles were a popular solution to memory management in operating systems of the 1990s, such as Mac OS and Windows. The FILE data structure in the C standard I/O library is a file handle, abstracting from the underlying file representation (on Unix these are file descriptors). Like other desktop environments, the Windows API heavily uses handles to represent objects in the system and to provide a communication pathway between the operating system and user space. For example, a window on the desktop is represented by a handle of type `HWND` (handle, window).

Doubly indirect handles (where the handle is not necessarily a pointer but might be, for example, an integer) have fallen out of favor in recent times, as increases in available memory and improved virtual memory algorithms have made the use of the simpler pointer more attractive. However, many operating systems still apply the term to pointers to opaque, "private" data structures—opaque pointers—or to indexes into internal arrays passed from one process to its client.
