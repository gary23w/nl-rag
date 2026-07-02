---
title: "Memory leak"
source: https://en.wikipedia.org/wiki/Memory_leak
domain: use-after-free-defense
license: CC-BY-SA-4.0
tags: use after free defense, dangling pointer mitigation, temporal memory safety, quarantine allocator hardening
fetched: 2026-07-02
---

# Memory leak

In computer science, a **memory leak** is a type of resource leak that occurs when a computer program incorrectly manages memory allocations in a way that memory which is no longer needed is not released. A memory leak may also happen when an object is stored in memory but cannot be accessed by the running code (i.e. unreachable memory). A memory leak has symptoms similar to a number of other problems and generally can only be diagnosed by a programmer with access to the program's source code.

A related concept is the "space leak", which is when a program consumes excessive memory but does eventually release it.

Because they can exhaust available system memory as an application runs, memory leaks are often the cause of or a contributing factor to software aging.

## Effects

### Minor leaks

If a program has a memory leak and its memory usage is steadily increasing, there will not usually be an immediate symptom. In modern operating systems, normal memory used by an application is released when the application terminates. This means that a memory leak in a program that only runs for a short time may not be noticed and is rarely serious, and slow leaks can also be covered over by program restarts. Every physical system has a finite amount of memory, and if the memory leak is not contained (for example, by restarting the leaking program) it will eventually cause problems for users.

### Thrashing

Most modern consumer desktop operating systems have both main memory which is physically housed in RAM microchips, and secondary storage such as a hard drive. Memory allocation is dynamic – each process gets as much memory as it requests. Active pages are transferred into main memory for fast access; inactive pages are pushed out to secondary storage to make room, as needed. When a single process starts consuming a large amount of memory, it usually occupies more and more of main memory, pushing other programs out to secondary storage – usually significantly slowing performance of the system. Even if the leaking program is terminated, it may take some time for other programs to swap back into main memory, and for performance to return to normal. The resulting slowness and excessive accessing of secondary storage is known as thrashing.

### Out-of-memory condition

If a program uses all available memory before being terminated (whether there is virtual memory or only main memory, such as on an embedded system) any attempt to allocate more memory will fail. This usually causes the program attempting to allocate the memory to terminate itself, or to generate a segmentation fault. Some programs are designed to recover from this situation (possibly by falling back on pre-reserved memory). The first program to experience the out-of-memory may or may not be the program that has the memory leak.

Some multi-tasking operating systems have special mechanisms to deal with an out-of-memory condition, such as killing processes at random (which may affect "innocent" processes), or killing the largest process in memory (which presumably is the one causing the problem). Some operating systems have a per-process memory limit, to prevent any one program from hogging all of the memory on the system. The disadvantage to this arrangement is that the operating system sometimes must be re-configured to allow proper operation of programs that legitimately require large amounts of memory, such as those dealing with graphics, video, or scientific calculations.

If the memory leak is in the kernel, the operating system itself will likely fail. Computers without sophisticated memory management, such as embedded systems, may also completely fail from a persistent memory leak.

## Causes of serious leaks

Much more serious leaks include those where:

- A program runs for a long time and consumes added memory over time, such as background tasks on servers, and especially in embedded systems which may be left running for many years
- New memory is allocated frequently for one-time tasks, such as when rendering the frames of a computer game or animated video
- A program can request memory, such as shared memory, that is not released, even when the program terminates
- Memory is very limited, such as in an embedded system or portable device, or where the program requires a very large amount of memory to begin with, leaving little margin for leaks
- A leak occurs within the operating system or memory manager
- A system device driver causes a leak
- The operating system does not automatically release memory on program termination

## Programming issues

Memory leaks are a common error in programming, especially when using languages that have no built in automatic garbage collection, such as C and C++. Typically, a memory leak occurs because dynamically allocated memory has become unreachable. The prevalence of memory leak bugs has led to the development of a number of debugging tools to detect unreachable memory. *BoundsChecker*, *Deleaker*, Memory Validator, *IBM Rational Purify*, *Valgrind*, *Parasoft Insure++*, *Dr. Memory* and *memwatch* are some of the more popular memory debuggers for C and C++ programs. "Conservative" garbage collection capabilities can be added to any programming language that lacks it as a built-in feature, and libraries for doing this are available for C and C++ programs. A conservative collector finds and reclaims most, but not all, unreachable memory.

Although the memory manager can recover unreachable memory, it cannot free memory that is still reachable and therefore potentially still useful. Modern memory managers therefore provide techniques for programmers to semantically mark memory with varying levels of usefulness, which correspond to varying levels of *reachability*. The memory manager does not free an object that is strongly reachable. An object is strongly reachable if it is reachable either directly by a strong reference or indirectly by a chain of strong references. (A *strong reference* is a reference that, unlike a weak reference, prevents an object from being garbage collected.) To prevent this, the developer is responsible for cleaning up references after use, typically by setting the reference to null once it is no longer needed and, if necessary, by deregistering any event listeners that maintain strong references to the object.

In general, automatic memory management is more robust and convenient for developers, as they do not need to implement freeing routines or worry about the sequence in which cleanup is performed or be concerned about whether or not an object is still referenced. It is easier for a programmer to know when a reference is no longer needed than to know when an object is no longer referenced. However, automatic memory management can impose a performance overhead, and it does not eliminate all of the programming errors that cause memory leaks.

## Exploitation

Publicly accessible systems such as web servers or routers are prone to denial-of-service attacks if an attacker discovers a sequence of operations which can trigger a leak. Such a sequence is known as an exploit.

## RAII

Resource acquisition is initialization (RAII) is an approach to the problem commonly taken in C++, D, and Ada. It involves associating scoped objects with the acquired resources, and automatically releasing the resources once the objects are out of scope. Unlike garbage collection, RAII has the advantage of knowing when objects exist and when they do not. Compare the following C and C++ examples:

In C:

```mw
#include <stdlib.h>

void someOperation(int* a) {
    // ...
}

void f(int n) {
    int* a = (int*)calloc(n, sizeof(int));
    someOperation(a);
    free(a);
}
```

In C++:

```mw
import std;

using std::vector;

void someOperation(vector<int>& a) {
    // ...
}

void f(int n) {
    vector<int> a(n);
    someOperation(a);
}
```

The C version, as implemented in the example, requires explicit deallocation; the array is dynamically allocated (from the heap in most C implementations), and continues to exist until explicitly freed. (Note that unlike `malloc()`, `calloc()` initializes all elements to `0`.)

The C++ version requires no explicit deallocation; it will always occur automatically as soon as the object `a` goes out of scope, including if an exception is thrown. This avoids some of the overhead of garbage collection schemes. And because object destructors can free resources other than memory, RAII helps to prevent the leaking of input and output resources accessed through a handle, which mark-and-sweep garbage collection does not handle gracefully. These include open files, open windows, user notifications, objects in a graphics drawing library, thread synchronisation primitives such as critical sections, network connections, and connections to the Windows Registry or another database.

However, using RAII correctly is not always easy and has its own pitfalls. For instance, if one is not careful, it is possible to create dangling pointers (or references) by returning data by reference, only to have that data be deleted when its containing object goes out of scope.

D uses a combination of RAII and garbage collection, employing automatic destruction when it is clear that an object cannot be accessed outside its original scope, and garbage collection otherwise.

## Reference counting and cyclic references

More modern garbage collection schemes are often based on a notion of reachability – if you do not have a usable reference to the memory in question, it can be collected. Other garbage collection schemes can be based on reference counting, where an object is responsible for keeping track of how many references are pointing to it. If the number goes down to zero, the object is expected to release itself and allow its memory to be reclaimed. The flaw with this model is that it does not cope with cyclic references, and this is why nowadays most programmers are prepared to accept the burden of the more costly mark and sweep type of systems.

The following Visual Basic code illustrates the canonical reference-counting memory leak:

```mw
Dim A, B
Set A = CreateObject("Some.Thing")
Set B = CreateObject("Some.Thing")
' At this point, the two objects each have one reference,

Set A.member = B
Set B.member = A
' Now they each have two references.

Set A = Nothing   ' You could still get out of it...

Set B = Nothing   ' And now you've got a memory leak!

End
```

In practice, this trivial example would be spotted straight away and fixed. In most real examples, the cycle of references spans more than two objects, and is more difficult to detect.

A well-known example of this kind of leak came to prominence with the rise of AJAX programming techniques in web browsers in the lapsed listener problem. JavaScript code which associated a DOM element with an event handler, and failed to remove the reference before exiting, would leak memory (AJAX web pages keep a given DOM alive for a lot longer than traditional web pages, so this leak was much more apparent).

## External detection

A "sawtooth" pattern of memory utilization may be an indicator of a memory leak within an application, particularly if the vertical drops coincide with reboots or restarts of that application. Care should be taken though because garbage collection points could also cause such a pattern and would show a healthy usage of the heap.

Constantly increasing memory usage is not necessarily evidence of a memory leak. Some applications will store ever increasing amounts of information in memory (e.g. as a cache). If the cache can grow so large as to cause problems, this may be a programming or design error, but is not a memory leak as the information remains nominally in use. In other cases, programs may require an unreasonably large amount of memory because the programmer has assumed memory is always sufficient for a particular task; for example, a graphics file processor might start by reading the entire contents of an image file and storing it all into memory, something that is not viable where a very large image exceeds available memory. Confirmation that excessive memory use is due to a memory leak requires access to the program code.

## Examples

### Pseudocode

The following example, written in pseudocode, is intended to show how a memory leak can come about, and its effects, without needing any programming knowledge. The program in this case is part of some very simple software designed to control an elevator. This part of the program is run whenever anyone inside the elevator presses the button for a floor.

```
When a button is pressed:
  Get some memory, which will be used to remember the floor number
  Put the floor number into the memory
  Are we already on the target floor?
    If so, we have nothing to do: finished
    Otherwise:
      Wait until the lift is idle
      Go to the required floor
      Release the memory we used to remember the floor number
```

The memory leak would occur if the floor number requested is the same floor that the elevator is on; the condition for releasing the memory would be skipped. Each time this case occurs, more memory is leaked.

Cases like this would not usually have any immediate effects. People do not often press the button for the floor they are already on, and in any case, the elevator might have enough spare memory that this could happen hundreds or thousands of times. However, the elevator will eventually run out of memory. This could take months or years, so it might not be discovered despite thorough testing.

The consequences would be unpleasant; at the very least, the elevator would stop responding to requests to move to another floor (such as when an attempt is made to call the elevator or when someone is inside and presses the floor buttons). If other parts of the program need memory (a part assigned to open and close the door, for example), then no one would be able to enter, and if someone happens to be inside, they will become trapped (assuming the doors cannot be opened manually).

The memory leak lasts until the system is reset. For example: if the elevator's power were turned off or in a power outage, the program would stop running. When power was turned on again, the program would restart and all the memory would be available again, but the slow process of memory leak would restart together with the program, eventually prejudicing the correct running of the system.

The leak in the above example can be corrected by bringing the "release" operation outside of the conditional:

```
When a button is pressed:
  Get some memory, which will be used to remember the floor number
  Put the floor number into the memory
  Are we already on the target floor?
    If not:
      Wait until the lift is idle
      Go to the required floor
  Release the memory we used to remember the floor number
```

### C++

The following C++ function deliberately leaks memory by losing the pointer to the allocated memory.

```mw
void causeLeak() {
    int* a = new int[5];
    a = nullptr;
    /**
     * The pointer in the 'a' no longer exists, and therefore cannot be freed,
     * but the memory is still allocated by the system.
     * If the program continues to create such pointers without freeing them, 
     * it will consume memory continuously.
     * Therefore, a leak would occur. 
     * A corresponding delete should match a new call. 
     */
}
```
