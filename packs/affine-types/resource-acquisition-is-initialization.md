---
title: "Resource acquisition is initialization"
source: https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization
domain: affine-types
license: CC-BY-SA-4.0
tags: affine type system, affine logic, move semantics, borrow checker
fetched: 2026-07-02
---

# Resource acquisition is initialization

**Resource acquisition is initialization** (**RAII**) is a programming idiom used in several object-oriented, statically typed programming languages to describe a particular language behavior. In RAII, holding a resource is a class invariant, and is tied to object lifetime. Resource allocation (or acquisition) is done during object creation (specifically initialization), by the constructor, while resource deallocation (release) is done during object destruction (specifically finalization), by the destructor. In other words, resource acquisition must succeed for initialization to succeed. Thus, the resource is guaranteed to be held between when initialization finishes and finalization starts (holding the resources is a class invariant), and to be held only when the object is alive. Thus, if there are no object leaks, there are no resource leaks.

RAII is associated most prominently with C++, where it originated, but also Ada, Vala, and Rust. The technique was developed for exception-safe resource management in C++ during 1984–1989, primarily by Bjarne Stroustrup and Andrew Koenig, and the term itself was coined by Stroustrup.

Other names for this idiom include *Constructor Acquires, Destructor Releases* (CADRe) and one particular style of use is called *Scope-based Resource Management* (SBRM). This latter term is for the special case of automatic variables. RAII ties resources to object *lifetime,* which may not coincide with entry and exit of a scope. (Notably variables allocated on the free store have lifetimes unrelated to any given scope.) However, using RAII for automatic variables (SBRM) is the most common use case.

## C++ example

The following example demonstrates usage of RAII for file access and mutex locking:

```mw
import std;

using std::mutex;
using std::ofstream;
using std::runtime_error;
using std::scoped_lock;
using std::string;

void writeToFile(const string& message) {
    // mutex is to protect access to file (which is shared across threads).
    static mutex m;

    // Lock mutex before accessing file.
    scoped_lock<mutex> lock(m);

    // Try to open file.
    ofstream f{"example.txt"};
    if (!f.is_open()) {
        throw runtime_error("unable to open file");
    }

    // Write message to file.
    std::println(f, message);

    // file will be closed first when leaving scope (regardless of exception)
    // mutex will be unlocked second (from lock destructor) when leaving scope
    // (regardless of exception).
}
```

This code is exception-safe because C++ guarantees that all objects with automatic storage duration (local variables) are destroyed at the end of the enclosing scope in the reverse order of their construction. The destructors of both the *lock* and *file* objects are therefore guaranteed to be called when returning from the function, whether an exception has been thrown or not.

Local variables allow easy management of multiple resources within a single function: they are destroyed in the reverse order of their construction, and an object is destroyed only if fully constructed—that is, if no exception propagates from its constructor.

Using RAII greatly simplifies resource management, reduces overall code size and helps ensure program correctness. RAII is therefore recommended by industry-standard guidelines, and most of the C++ standard library follows the idiom.

## Benefits

The advantages of RAII as a resource management technique are that it provides encapsulation, exception safety (for stack resources), and locality (it allows acquisition and release logic to be written next to each other).

Encapsulation is provided because resource management logic is defined once in the class, not at each call site. Exception safety is provided for stack resources (resources that are released in the same scope as they are acquired) by tying the resource to the lifetime of a stack variable (a local variable declared in a given scope): if an exception is thrown, and proper exception handling is in place, the only code that will be executed when exiting the current scope are the destructors of objects declared in that scope. Finally, locality of definition is provided by writing the constructor and destructor definitions next to each other in the class definition.

Resource management therefore needs to be tied to the lifespan of suitable objects in order to gain automatic allocation and reclamation. Resources are acquired during initialization, when there is no chance of them being used before they are available, and released with the destruction of the same objects, which is guaranteed to take place even in case of errors.

Comparing RAII with the `finally` construct used in Java, Stroustrup wrote that “In realistic systems, there are far more resource acquisitions than kinds of resources, so the 'resource acquisition is initialization' technique leads to less code than use of a 'finally' construct.”

As a class invariant, RAII provides guarantees that an object instance that is supposed to have acquired a resource has in fact done so. This eliminates the need for additional "setup" methods to get a newly-created object into a usable state (all such work is performed in the constructor; similarly, "shutdown" tasks to release resources occur in the object's destructor), and the need to test instances to verify that they have been properly set up before every use.

## Typical uses

The RAII design is often used for controlling mutex locks in multi-threaded applications. In that use, the object releases the lock when destroyed. Without RAII in this scenario the potential for deadlock would be high and the logic to lock the mutex would be far from the logic to unlock it. With RAII, the code that locks the mutex essentially includes the logic that the lock will be released when execution leaves the scope of the RAII object.

Another typical example is interacting with files: We could have an object that represents a file that is open for writing, wherein the file is opened in the constructor and closed when execution leaves the object's scope. In both cases, RAII ensures only that the resource in question is released appropriately; care must still be taken to maintain exception safety. If the code modifying the data structure or file is not exception-safe, the mutex could be unlocked or the file closed with the data structure or file corrupted.

Ownership of dynamically allocated objects (memory allocated with `new` in C++) can also be controlled with RAII, such that the object is released when the RAII (stack-based) object is destroyed. For this purpose, the C++11 standard library defines the smart pointer classes `std::unique_ptr` for single-owned objects and `std::shared_ptr` for objects with shared ownership. Similar classes are also available through `std::auto_ptr` in C++98, and `boost::shared_ptr` in the Boost libraries.

Also, messages can be sent to network resources using RAII. In this case, the RAII object would send a message to a socket at the end of the constructor, when its initialization is completed. It would also send a message at the beginning of the destructor, when the object is about to be destroyed. Such a construct might be used in a client object to establish a connection with a server running in another process.

## Dispose

In many languages that lack direct memory management or discourage its use, a similar mechanism called the "dispose pattern" is used to call a `dispose` method that performs relevant resource cleanup on the object at the end of scope.

### C

For versions of C prior to the introduction of `defer` Clang and the GNU Compiler Collection implement a `[[gnu::cleanup]]` attribute as a non-standard extension to C. The following annotates a variable with a given destructor function that it will call when the variable goes out of scope:

```mw
#include <stdio.h>
#include <time.h>

void writeLogFile() {
    const char* logFileName = "logfile.txt";

    [[gnu::cleanup(fclosep)]]
    FILE* logFile = fopen(logFileName, "w+");

    time_t now = time(NULL);

    fprintf(logFile, "Beginning log in %s at %s", filename, ctime(&now));
}
```

In this example, the compiler arranges for the `fclosep` function to be called on `logFile` before `writeLogFile` returns.

### C++

In C++, disposing is done directly with a destructor. In C++, a class `X` will automatically call its destructor `~X()` when it reaches the end of scope. The dispose pattern is essentially equivalent to RAII in C++.

```mw
import std;

using std::ifstream;
using std::string;

void readFile() {
    if (ifstream reader{"story.txt"}; reader) {
        string line;
        while (std::getline(reader, line)) {
            std::println("{}", line);
        }
    } else {
        std::println(stderr, "Failed to open file");
    }
    // reader is destroyed, after the if/else block
}
```

### C

C# features a `using`-with-resources block, which can be used if the object implements `System.IDisposable`. It will call a `Dispose()` method at the end of the resource.

```mw
using System;
using System.IO;

using (StreamReader reader = new StreamReader("story.txt"))
{
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        Console.WriteLine(line);
    }
} // reader is automatically disposed here
```

### Java

Java features a `try`-with-resources block, which can be used if the object implements `java.lang.AutoCloseable`. It will call a `close()` method at the end of the resource.

```mw
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

try (BufferedReader reader = new BufferedReader(new FileReader("story.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### Python

Python features a `with` block, which can be used if the object implements `__enter__` and `__exit__` methods.

```mw
with open("story.txt", "r") as file:
    print(file.readline()) # print the first line in the file2
```

This is also used for managing resources such as locks.

```mw
from threading import Lock

balance_lock: Lock = Lock()
with balance_lock:
    # Critical section: update the account balance here...
```

### Rust

Rust allows defining custom cleanup logic, if an object implements `std::ops::Drop`, which will call a `drop()` method after the object leaves scope. This can also be manually called by `std::mem::drop()`.

## Limitations

RAII only works for resources acquired and released (directly or indirectly) by stack-allocated objects, where there *is* a well-defined static object lifetime. Heap-allocated objects which themselves acquire and release resources are common in many languages, including C++. RAII depends on heap-based objects to be implicitly or explicitly deleted along all possible execution paths, in order to trigger its resource-releasing destructor (or equivalent). This can be achieved by using smart pointers to manage all heap objects, with weak pointers for cyclically referenced objects.

In C++, stack unwinding is only guaranteed to occur if the exception is caught somewhere. This is because "If no matching handler is found in a program, the function terminate() is called; whether or not the stack is unwound before this call to terminate() is implementation-defined (15.5.1)." (C++03 standard, §15.3/9). This behavior is usually acceptable, since the operating system releases remaining resources like memory, files, sockets, etc. at program termination.

At the 2018 Gamelab conference, Jonathan Blow claimed that use of RAII can cause memory fragmentation which in turn can cause cache misses and a 100 times or worse hit on performance.

## Reference counting

Perl, Python (in the CPython implementation), and PHP manage object lifetime by reference counting, which makes it possible to use RAII. Objects that are no longer referenced are immediately destroyed or finalized and released, so a destructor or finalizer can release the resource at that time. However, it is not always idiomatic in such languages, and is specifically discouraged in Python (in favor of context managers and *finalizers* from the *weakref* package).

However, object lifetimes are not necessarily bound to any scope, and objects may be destroyed non-deterministically or not at all. This makes it possible to accidentally leak resources that should have been released at the end of some scope. Objects stored in a static variable (notably a global variable) may not be finalized when the program terminates, so their resources are not released; CPython makes no guarantee of finalizing such objects, for instance. Further, objects with circular references will not be collected by a simple reference counter, and will live indeterminately long; even if collected (by more sophisticated garbage collection), destruction time and destruction order will be non-deterministic. In CPython there is a cycle detector which detects cycles and finalizes the objects in the cycle, though prior to CPython 3.4, cycles are not collected if any object in the cycle has a finalizer.
