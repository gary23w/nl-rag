---
title: "C dynamic memory allocation"
source: https://en.wikipedia.org/wiki/C_dynamic_memory_allocation
domain: use-after-free-defense
license: CC-BY-SA-4.0
tags: use after free defense, dangling pointer mitigation, temporal memory safety, quarantine allocator hardening
fetched: 2026-07-02
---

# C dynamic memory allocation

**C dynamic memory allocation** refers to performing manual memory management for dynamic memory allocation in the C programming language via a group of functions in the C standard library, mainly `malloc`, `realloc`, `calloc`, `aligned_alloc` and `free`.

The C++ programming language includes these functions; however, the operators new and delete provide similar functionality and are recommended by that language's authors. Still, there are several situations in which using `new`/`delete` is not applicable, such as garbage collection code or performance-sensitive code, and a combination of `malloc` and `new` may be required instead of the higher-level `new` operator.

Many different implementations of the actual memory allocation mechanism, used by malloc, are available. Their performance varies in both execution time and required memory.

## Rationale

The C programming language manages memory statically, automatically, or dynamically. Static-duration variables are allocated in main memory, usually along with the executable code of the program, and persist for the lifetime of the program; automatic-duration variables are allocated on the stack and come and go as functions are called and return. For static-duration and automatic-duration variables, the size of the allocation must be compile-time constant (except for the case of variable-length automatic arrays). If the required size is not known until run-time (for example, if data of arbitrary size is being read from the user or from a disk file), then using fixed-size data objects is inadequate.

The lifetime of allocated memory can also cause concern. Neither static- nor automatic-duration memory is adequate for all situations. Automatic-allocated data cannot persist across multiple function calls, while static data persists for the life of the program whether it is needed or not. In many situations the programmer requires greater flexibility in managing the lifetime of allocated memory.

These limitations are avoided by using dynamic memory allocation, in which memory is more explicitly (but more flexibly) managed, typically by allocating it from the heap (free storage), an area of memory structured for this purpose. In C, the library function `malloc` is used to allocate a block of memory on the heap. The program accesses this block of memory via a pointer that `malloc` returns. When the memory is no longer needed, the pointer is passed to `free` which deallocates the memory so that it can be used for other purposes.

The original description of C indicated that `calloc` and `cfree` were in the standard library, but not `malloc`. Code for a simple model implementation of a storage manager for Unix was given with `alloc` and `free` as the user interface functions, and using the `sbrk` system call to request memory from the operating system. The 6th Edition Unix documentation gives `alloc` and `free` as the low-level memory allocation functions. The `malloc` and `free` routines in their modern form are completely described in the 7th Edition Unix manual.

Some platforms provide library or intrinsic function calls which allow run-time dynamic allocation from the C stack rather than the heap (e.g. `alloca()`). This memory is automatically freed when the calling function ends.

## Overview of functions

The C dynamic memory allocation functions are defined in `<stdlib.h>` header (`<cstdlib>` header in C++).

| Function | Description |
|---|---|
| `malloc` | allocates the specified number of bytes |
| `aligned_alloc` | allocates the specified number of bytes at the specified alignment |
| `realloc` | increases or decreases the size of the specified block of memory, moving it if necessary |
| `calloc` | allocates the specified number of bytes and initializes them to zero |
| `free` | releases the specified block of memory back to the system |

### Differences between `malloc()` and `calloc()`

- `malloc()` takes a single argument (the amount of memory to allocate in bytes), while `calloc()` takes two arguments — the number of elements and the size of each element.
- `malloc()` only allocates memory, while `calloc()` allocates and sets the bytes in the allocated region to zero.

## Usage example

Creating an array of ten integers with automatic scope is straightforward in C:

```mw
int a[10];
```

However, the size of the array is fixed at compile time. If one wishes to allocate a similar array dynamically without using a variable-length array, which is not guaranteed to be supported in all C11 implementations, an array can be allocated using `malloc`, which returns a void pointer (indicating that it is a pointer to a region of unknown data type), which can be cast for safety.

```mw
int* a = (int*)malloc(10 * sizeof(int));
```

This computes the number of bytes that ten integers occupy in memory, then requests that many bytes from `malloc` and assigns the result to a pointer named `a` (due to C syntax, pointers and arrays can be used interchangeably in some situations).

Because `malloc` might not be able to service the request, it might return a null pointer and it is good programming practice to check for this:

```mw
int* a = (int*)malloc(10 * sizeof(int));
if (!a) {
    fprintf(stderr, "malloc failed\n");
    return -1;
}
```

When the program no longer needs the dynamic array, it must eventually call `free` to return the memory it occupies to the free store:

```mw
free(a);
```

The memory set aside by `malloc` is not initialized and may contain cruft: the remnants of previously used and discarded data. After allocation with `malloc`, elements of the array are uninitialized variables. The command `calloc` will return an allocation that has already been cleared:

```mw
int* a = (int*)calloc(10, sizeof(int));
```

With realloc we can resize the amount of memory a pointer points to. For example, if we have a pointer acting as an array of size n and we want to change it to an array of size m , we can use realloc.

```mw
int* a = (int*)malloc(2 * sizeof(int));
a[0] = 1;
a[1] = 2;
a = (int*)realloc(a, 3 * sizeof(int));
a[2] = 3;
```

Note that realloc must be assumed to have changed the base address of the block (i.e. if it has failed to extend the size of the original block, and has therefore allocated a new larger block elsewhere and copied the old contents into it). Therefore, any pointers to addresses within the original block are also no longer valid.

## Type safety

As stated earlier, `malloc` returns a void pointer (`void*`), which indicates that it is a pointer to a region of unknown data type. The use of casting is required in C++ due to the strong type system, whereas this is not the case in C. One may "cast" (see type conversion) this pointer to a specific type:

```mw
// without a cast
int* ptr1 = malloc(10 * sizeof(*ptr));

// with a cast
int* ptr2 = (int*)malloc(10 * sizeof(*ptr));
```

There are advantages and disadvantages to performing such a cast. Including the cast improves interoperability between C and C++, allowing C code to be compiled or used as C++. Furthermore, the cast allows for pre-1989 versions of `malloc` that originally returned a `char*`. Additionally, casting can help the developer identify inconsistencies in type sizing should the destination pointer type change, particularly if the pointer is declared far from the `malloc()` call (although modern compilers and static analysers can warn on such behaviour without requiring the cast).

However, under the C standard, the cast is not necessary, and adding the cast may mask failure to include the header `<stdlib.h>`, in which the function prototype for `malloc` is found. In the absence of a prototype for `malloc`, the C90 standard requires that the C compiler assume `malloc` returns an `int`. If there is no cast, C90 requires a diagnostic when this integer is assigned to the pointer; however, with the cast, this diagnostic would not be produced, hiding a bug. On certain architectures and data models (such as LP64 on 64-bit systems, where `long` and pointers are 64-bit and `int` is 32-bit), this error can actually result in undefined behaviour, as the implicitly declared `malloc` returns a 32-bit value whereas the actually defined function returns a 64-bit value. Depending on calling conventions and memory layout, this may result in stack smashing. This issue is less likely to go unnoticed in modern compilers, as C99 does not permit implicit declarations, so the compiler must produce a diagnostic even if it does assume `int` return. Additionally, if the type of the pointer is changed at its declaration, the lines where `malloc` is called and the cast will have to be updated as well.

In C++, if `std::malloc` must be used, it is preferable to `static_cast` it, rather than use a raw cast:

```mw
int* p = static_cast<int*>(malloc(10 * sizeof(*ptr)));
```

## Common errors

The improper use of dynamic memory allocation can frequently be a source of bugs. These can include security bugs or program crashes, most often due to segmentation faults.

Most common errors are as follows:

**Not checking for allocation failures**

Memory allocation is not guaranteed to succeed, and may instead return a null pointer. Using the returned value, without checking if the allocation is successful, invokes

undefined behavior

. This usually leads to crash (due to the resulting segmentation fault on the null pointer dereference), but there is no guarantee that a crash will happen so relying on that can also lead to problems.

**Memory leaks**

Failure to deallocate memory using

free

leads to the buildup of non-reusable memory, which is no longer used by the program. This wastes memory resources and can lead to allocation failures when these resources are exhausted.

**Logical errors**

All allocations must follow the same pattern: allocation using

malloc

, usage to store data, deallocation using

free

. Failures to adhere to this pattern, such as memory usage after a call to

free

(

dangling pointer

) or before a call to

malloc

(

wild pointer

), calling

free

twice ("double free"), etc., usually causes a segmentation fault and results in a crash of the program. These errors can be transient and hard to debug – for example, freed memory is usually not immediately reclaimed by the OS, and thus dangling pointers may persist for a while and appear to work.

In addition, as an interface that precedes ANSI C standardization, `malloc` and its associated functions have behaviors that were intentionally left to the implementation to define for themselves. One of them is the zero-length allocation, which is more of a problem with `realloc` since it is more common to resize to zero. Although both POSIX and the Single Unix Specification require proper handling of 0-size allocations by either returning `NULL` or something else that can be safely freed, not all platforms are required to abide by these rules. Among the many double-free errors that it has led to, the 2019 WhatsApp RCE was especially prominent. A way to wrap these functions to make them safer is by simply checking for 0-size allocations and turning them into those of size 1. (Returning `NULL` has its own problems: it otherwise indicates an out-of-memory failure. In the case of `realloc` it would have signaled that the original memory was not moved and freed, which again is not the case for size 0, leading to the double-free.)

## Implementations

The implementation of memory management depends greatly upon operating system and architecture. Some operating systems supply an allocator for malloc, while others supply functions to control certain regions of data. The same dynamic memory allocator is often used to implement both `malloc` and the operator `new` in C++.

### Heap-based

Implementation of legacy allocators was commonly done using the heap segment. The allocator would usually expand and contract the heap to fulfill allocation requests.

The heap method suffers from a few inherent flaws:

- A linear allocator can only shrink if the last allocation is released. Even if largely unused, the heap can get "stuck" at a very large size because of a small but long-lived allocation at its tip which could waste any amount of address space, although some allocators on some systems may be able to release entirely empty intermediate pages to the OS.
- A linear allocator is sensitive to fragmentation. A good allocator will attempt to track and reuse free slots through the entire heap, but as allocation sizes and lifetimes get mixed it can be difficult and expensive to find or coalesce free segments large enough to hold new allocation requests.
- A linear allocator has extremely poor concurrency characteristics, as the heap segment is per-process every thread has to synchronise on allocation, and concurrent allocations from threads which may have very different work loads amplifies the previous two issues.

### dlmalloc and ptmalloc

Doug Lea has developed the public domain dlmalloc ("Doug Lea's Malloc") as a general-purpose allocator, starting in 1987. The GNU C library (glibc) is derived from Wolfram Gloger's ptmalloc ("pthreads malloc"), a fork of dlmalloc with threading-related improvements. As of November 2023, the latest version of dlmalloc is version 2.8.6 from August 2012. In 2023 it was relicensed from CC0 to MIT-0.

dlmalloc is a boundary tag allocator. Memory on the heap is allocated as "chunks", an 8-byte aligned data structure which contains a header, and usable memory. Allocated memory contains an 8- or 16-byte overhead for the size of the chunk and usage flags (similar to a dope vector). Unallocated chunks also store pointers to other free chunks in the usable space area, making the minimum chunk size 16 bytes on 32-bit systems and 24/32 (depends on alignment) bytes on 64-bit systems.

Unallocated memory is grouped into "bins" of similar sizes, implemented by using a double-linked list of chunks (with pointers stored in the unallocated space inside the chunk). Bins are sorted by size into three classes:

- For requests below 256 bytes (a "smallbin" request), a simple two power best fit allocator is used. If there are no free blocks in that bin, a block from the next highest bin is split in two.
- For requests of 256 bytes or above but below the mmap threshold, dlmalloc since v2.8.0 use an in-place *bitwise trie* algorithm ("treebin"). If there is no free space left to satisfy the request, dlmalloc tries to increase the size of the heap, usually via the brk system call. This feature was introduced way after ptmalloc was created (from v2.7.x), and as a result is not a part of glibc, which inherits the old best-fit allocator.
- For requests above the mmap threshold (a "largebin" request), the memory is always allocated using the mmap system call. The threshold is usually 128 KB. The mmap method averts problems with huge buffers trapping a small allocation at the end after their expiration, but always allocates an entire page of memory, which on many architectures is 4096 bytes in size.

Game developer Adrian Stone argues that `dlmalloc`, as a boundary-tag allocator, is unfriendly for console systems that have virtual memory but do not have demand paging. This is because its pool-shrinking and growing callbacks (`sysmalloc`/`systrim`) cannot be used to allocate and commit individual pages of virtual memory. In the absence of demand paging, fragmentation becomes a greater concern.

### FreeBSD's and NetBSD's jemalloc

Since FreeBSD 7.0 and NetBSD 5.0, the old `malloc` implementation (`phkmalloc` by Poul-Henning Kamp) was replaced by jemalloc, written by Jason Evans. The main reason for this was a lack of scalability of `phkmalloc` in terms of multithreading. In order to avoid lock contention, `jemalloc` uses separate "arenas" for each CPU. Experiments measuring number of allocations per second in multithreading application have shown that this makes it scale linearly with the number of threads, while for both phkmalloc and dlmalloc performance was inversely proportional to the number of threads.

### OpenBSD's malloc

OpenBSD's implementation of the `malloc` function makes use of mmap. For requests greater in size than one page, the entire allocation is retrieved using `mmap`; smaller sizes are assigned from memory pools maintained by `malloc` within a number of "bucket pages", also allocated with `mmap`. On a call to `free`, memory is released and unmapped from the process address space using `munmap`. This system is designed to improve security by taking advantage of the address space layout randomization and gap page features implemented as part of OpenBSD's `mmap` system call, and to detect use-after-free bugs—as a large memory allocation is completely unmapped after it is freed, further use causes a segmentation fault and termination of the program.

The GrapheneOS project initially started out by porting OpenBSD's memory allocator to Android's Bionic C Library.

### Hoard malloc

Hoard is an allocator whose goal is scalable memory allocation performance. Like OpenBSD's allocator, Hoard uses `mmap` exclusively, but manages memory in chunks of 64 kilobytes called superblocks. Hoard's heap is logically divided into a single global heap and a number of per-processor heaps. In addition, there is a thread-local cache that can hold a limited number of superblocks. By allocating only from superblocks on the local per-thread or per-processor heap, and moving mostly-empty superblocks to the global heap so they can be reused by other processors, Hoard keeps fragmentation low while achieving near linear scalability with the number of threads.

### mimalloc

An open-source compact general-purpose memory allocator from Microsoft Research with focus on performance. The library is about 11,000 lines of code.

### Thread-caching malloc (tcmalloc)

Every thread has a thread-local storage for small allocations. For large allocations mmap or sbrk can be used. TCMalloc, a *malloc* developed by Google, has garbage-collection for local storage of dead threads. The TCMalloc is considered to be more than twice as fast as glibc's ptmalloc for multithreaded programs.

### In-kernel

Operating system kernels need to allocate memory just as application programs do. The implementation of `malloc` within a kernel often differs significantly from the implementations used by C libraries, however. For example, memory buffers might need to conform to special restrictions imposed by DMA, or the memory allocation function might be called from interrupt context. This necessitates a `malloc` implementation tightly integrated with the virtual memory subsystem of the operating system kernel.

## Overriding malloc

Because `malloc` and its relatives can have a strong impact on the performance of a program, it is not uncommon to override the functions for a specific application by custom implementations that are optimized for application's allocation patterns. The C standard does not specify a way of doing this, but operating systems have found various ways to do this by exploiting dynamic linking. One way is to simply link in a different library to override the symbols. Another, employed by Unix System V.3, is to make `malloc` and `free` function pointers that an application can reset to custom functions.

In the source code the function can easily be replaced by using preprocessor macros, such as

```
#define malloc custom_malloc
#define realloc custom_realloc
#define free custom_free
```

which get defined in a header that all files that use memory allocation functions must include. Theese macros should also replace the function `strdup`, since its result is passed to `free` too. Data allocated inside of library functions (like `FILE` structures in the `stdio.h`) still get directly handled without using the wrappers.

The most common form on POSIX-like systems is to set the environment variable LD_PRELOAD with the path of the allocator, so that the dynamic linker uses that version of malloc/calloc/free instead of the libc implementation.

## Allocation size limits

The largest possible memory block `malloc` can allocate depends on the host system, particularly the size of physical memory and the operating system implementation.

Theoretically, the largest number should be the maximum value that can be held in a `size_t` type, which is an implementation-dependent unsigned integer representing the size of an area of memory. In the C99 standard and later, it is available as the `SIZE_MAX` constant from `<stdint.h>`. Although not guaranteed by ISO C, it is usually `2^(CHAR_BIT * sizeof(size_t)) - 1`.

On glibc systems, the largest possible memory block `malloc` can allocate is only half this size, namely `2^(CHAR_BIT * sizeof(ptrdiff_t) - 1) - 1`.

On systems that use segmentation, like some memory models under MS-DOS, the largest possible memory block is typically one segment or less and thus significant smaller than the total address space, and `size_t` might be a smaller type than `ptrdiff_t`.

## Extensions and alternatives

The C library implementations shipping with various operating systems and compilers may come with alternatives and extensions to the standard `malloc` interface. Notable among these is:

- `alloca`, which allocates a requested number of bytes on the call stack. No corresponding deallocation function exists, as typically the memory is deallocated as soon as the calling function returns. `alloca` was present on Unix systems as early as 32/V (1978), but its use can be problematic in some (e.g., embedded) contexts. While supported by many compilers, it is not part of the ANSI-C standard and therefore may not always be portable. It may also cause minor performance problems: it leads to variable-size stack frames, so that both stack and frame pointers need to be managed (with fixed-size stack frames, one of these is redundant). Larger allocations may also increase the risk of undefined behavior due to a stack overflow. C99 offered variable-length arrays as an alternative stack allocation mechanism – however, this feature was relegated to optional in the later C11 standard.
- POSIX defines a function `posix_memalign` that allocates memory with caller-specified alignment. Its allocations are deallocated with `free`, so the implementation usually needs to be a part of the malloc library.
