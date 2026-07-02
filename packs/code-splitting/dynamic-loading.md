---
title: "Dynamic loading"
source: https://en.wikipedia.org/wiki/Dynamic_loading
domain: code-splitting
license: CC-BY-SA-4.0
tags: code splitting, dynamic import expression, javascript module bundle, on-demand chunk loading
fetched: 2026-07-02
---

# Dynamic loading

**Dynamic loading** is a mechanism by which a computer program can, at run time, load a library (or other binary) into memory, retrieve the addresses of functions and variables contained in the library, execute those functions or access those variables, and unload the library from memory. It is one of the three mechanisms by which a computer program can use some other software within the program; the others are static linking and dynamic linking. Unlike static linking and dynamic linking, dynamic loading allows a computer program to start up in the absence of these libraries, to discover available libraries, and to potentially gain additional functionality.

## History

Dynamic loading was a common technique for IBM's operating systems for System/360 such as OS/360, particularly for I/O subroutines, and for COBOL and PL/I runtime libraries, and continues to be used in IBM's operating systems for z/Architecture, such as z/OS. As far as the application programmer is concerned, the loading is largely transparent, since it is mostly handled by the operating system (or its I/O subsystem). The main advantages are:

- Fixes (patches) to the subsystems fixed all programs at once, without the need to relink them
- Libraries could be protected from unauthorized modification

IBM's strategic transaction processing system, CICS (1970s onwards) uses dynamic loading extensively both for its kernel and for normal application program loading. Corrections to application programs could be made offline and new copies of changed programs loaded dynamically without needing to restart CICS (which can, and frequently does, run 24/7).

Shared libraries were added to Unix in the 1980s, but initially without the ability to let a program load additional libraries after startup.

## Uses

Dynamic loading is most frequently used in implementing software plugins. For example, the Apache Web Server's `*.dso` "dynamic shared object" plugin files are libraries which are loaded at runtime with dynamic loading. Dynamic loading is also used in implementing computer programs where multiple different libraries may supply the requisite functionality and where the user has the option to select which library or libraries to provide.

## In C/C++

Not all systems support dynamic loading. Unix-like operating systems such as macOS, Linux, and Solaris provide dynamic loading with the C programming language "dl" library. The Windows operating system provides dynamic loading through the Windows API.

### Summary

| Name | Standard POSIX/Unix API | Microsoft Windows API |
|---|---|---|
| Header file inclusion | `#include <dlfcn.h>` | `#include <windows.h>` |
| Definitions for header | `dl` (`libdl.so`, `libdl.dylib`, etc. depending on the OS) | `kernel32.dll` |
| Loading the library | `dlopen` | `LoadLibrary` `LoadLibraryEx` |
| Extracting contents | `dlsym` | `GetProcAddress` |
| Unloading the library | `dlclose` | `FreeLibrary` |

### Loading the library

Loading the library is accomplished with `LoadLibrary` or `LoadLibraryEx` on Windows and with `dlopen` on Unix-like operating systems. Examples follow:

#### Most Unix-like operating systems (Solaris, Linux, *BSD, etc.)

```mw
void* sdl_library = dlopen("libSDL.so", RTLD_LAZY);
if (!sdl_library) {
   // report error ...
} else {
   // use the result in a call to dlsym
}
```

#### macOS

As a Unix library:

```mw
void* sdl_library = dlopen("libSDL.dylib", RTLD_LAZY);
if (!sdl_library) {
   // report error ...
} else {
   // use the result in a call to dlsym
}
```

As a macOS Framework:

```mw
void* sdl_library = dlopen("/Library/Frameworks/SDL.framework/SDL", RTLD_LAZY);
if (!sdl_library) {
   // report error ...
} else {
   // use the result in a call to dlsym
}
```

Or if the framework or bundle contains Objective-C code:

```mw
NSBundle *bundle = [NSBundle bundleWithPath:@"/Library/Plugins/Plugin.bundle"];
NSError *err = nil;
if ([bundle loadAndReturnError:&err])
{
    // Use the classes and functions in the bundle.
}
else
{
    // Handle error.
}
```

#### Windows

```mw
HMODULE sdl_library = LoadLibrary(TEXT("SDL.dll"));
if (!sdl_library) {
   // report error ...
} else {
   // use the result in a call to GetProcAddress
}
```

Extracting the contents of a dynamically loaded library is achieved with `GetProcAddress` on Windows and with `dlsym` on Unix-like operating systems.

#### Unix-like operating systems (Solaris, Linux, *BSD, macOS, etc.)

```mw
void* initializer = dlsym(sdl_library, "SDL_Init");
if (!initializer) {
   // report error ...
} else {
   // cast initializer to its proper type and use
}
```

On macOS, when using Objective-C bundles, one can also:

```mw
Class rootClass = [bundle principalClass]; // Alternatively, NSClassFromString() can be used to obtain a class by name.
if (rootClass)
{
    id object = [[rootClass alloc] init]; // Use the object.
}
else
{
    // Report error.
}
```

#### Windows

```mw
FARPROC initializer = GetProcAddress(sdl_library, "SDL_Init");
if (!initializer) {
   // report error ...
} else {
   // cast initializer to its proper type and use
}
```

### Converting a library function pointer

The result of `dlsym()` or `GetProcAddress()` has to be converted to a pointer of the appropriate type before it can be used.

#### Windows

In Windows, the conversion is straightforward, since FARPROC is essentially already a function pointer:

```mw
typedef INT_PTR (*FARPROC)(void);
```

This can be problematic when the address of an object is to be retrieved rather than a function. However, usually one wants to extract functions anyway, so this is normally not a problem.

```mw
typedef void (*SDLInitFunctionType)(void);
SDLInitFunctionType init_func = (SDLInitFunctionType)initializer;
```

#### Unix (POSIX)

According to the POSIX specification, the result of `dlsym()` is a `void` pointer. However, a function pointer is not required to even have the same size as a data object pointer, and therefore a valid conversion between type `void*` and a pointer to a function may not be easy to implement on all platforms.

On most systems in use today, function and object pointers are *de facto* convertible. The following code snippet demonstrates one workaround which allows to perform the conversion anyway on many systems:

```mw
typedef void (*SDLInitFunctionType)(void);
SDLInitFunctionType init_func = (SDLInitFunctionType)initializer;
```

The above snippet will give a warning on some compilers: `warning: dereferencing type-punned pointer will break strict-aliasing rules`. Another workaround is:

```mw
typedef void (*SDLInitFunctionType)(void);

union { 
    SDLInitFunctionType func; 
    void* obj; 
} alias;

alias.obj = initializer;
SDLInitFunctionType init_func = alias.func;
```

which disables the warning even if strict aliasing is in effect. This makes use of the fact that reading from a different union member than the one most recently written to (called "type punning") is common, and explicitly allowed even if strict aliasing is in force, provided the memory is accessed through the union type directly. However, this is not strictly the case here, since the function pointer is copied to be used outside the union. Note that this trick may not work on platforms where the size of data pointers and the size of function pointers is not the same.

#### Solving the function pointer problem on POSIX systems

The fact remains that any conversion between function and data object pointers has to be regarded as an (inherently non-portable) implementation extension, and that no "correct" way for a direct conversion exists, since in this regard the POSIX and ISO standards contradict each other.

Because of this problem, the POSIX documentation on `dlsym()` for the outdated issue 6 stated that "a future version may either add a new function to return function pointers, or the current interface may be deprecated in favor of two new functions: one that returns data pointers and the other that returns function pointers".

For the subsequent version of the standard (issue 7, 2008), the problem has been discussed and the conclusion was that function pointers have to be convertible to `void*` for POSIX compliance. This requires compiler makers to implement a working cast for this case.

If the contents of the library can be changed (i.e. in the case of a custom library), in addition to the function itself a pointer to it can be exported. Since a pointer to a function pointer is itself an object pointer, this pointer can always be legally retrieved by call to `dlsym()` and subsequent conversion. However, this approach requires maintaining separate pointers to all functions that are to be used externally, and the benefits are usually small.

### Unloading the library

Loading a library causes memory to be allocated; the library must be deallocated in order to avoid a memory leak. Additionally, failure to unload a library can prevent filesystem operations on the file which contains the library. Unloading the library is accomplished with `FreeLibrary` on Windows and with `dlclose` on Unix-like operating systems. However, unloading a DLL can lead to program crashes if objects in the main application refer to memory allocated within the DLL. For example, if a DLL introduces a new class and the DLL is closed, further operations on instances of that class from the main application will likely cause a memory access violation. Likewise, if the DLL introduces a factory function for instantiating dynamically loaded classes, calling or dereferencing that function after the DLL is closed leads to undefined behaviour.

#### Unix-like operating systems (Solaris, Linux, *BSD, macOS, etc.)

```mw
dlclose(sdl_library);
```

#### Windows

```mw
FreeLibrary(sdl_library);
```

### Special library

The implementations of dynamic loading on Unix-like operating systems and Windows allow programmers to extract symbols from the currently executing process.

Unix-like operating systems allow programmers to access the global symbol table, which includes both the main executable and subsequently loaded dynamic libraries.

Windows allows programmers to access symbols exported by the main executable. Windows does not use a global symbol table and has no API to search across multiple modules to find a symbol by name.

#### Unix-like operating systems (Solaris, Linux, *BSD, macOS, etc.)

```mw
void* this_process = dlopen(NULL, 0);
```

#### Windows

```mw
HMODULE this_process = GetModuleHandle(NULL);

HMODULE this_process_again;
GetModuleHandleEx(0, 0, &this_process_again);
```

## In Java

In the Java programming language, classes can be dynamically loaded using the **`ClassLoader`** object. For example:

```mw
Class type = ClassLoader.getSystemClassLoader().loadClass(name);
Object obj = type.newInstance();
```

The Reflection mechanism also provides a means to load a class if it isn't already loaded. It uses the classloader of the current class:

```mw
Class type = Class.forName(name);
Object obj = type.newInstance();
```

However, there is no simple way to unload a class in a controlled way. Loaded classes can only be unloaded in a controlled way, i.e. when the programmer wants this to happen, if the classloader used to load the class is not the system class loader, and is itself unloaded. When doing so, various details need to be observed to ensure the class is really unloaded. This makes unloading of classes tedious.

Implicit unloading of classes, i.e. in an uncontrolled way by the garbage collector, has changed a few times in Java. Until Java 1.2. the garbage collector could unload a class whenever it felt it needed the space, independent of which class loader was used to load the class. Starting with Java 1.2 classes loaded via the system classloader were never unloaded and classes loaded via other classloaders only when this other classloader was unloaded. Starting with Java 6 classes can contain an internal marker indicating to the garbage collector they can be unloaded if the garbage collector desires to do so, independent of the classloader used to load the class. The garbage collector is free to ignore this hint.

Similarly, libraries implementing native methods are dynamically loaded using the `System.loadLibrary` method. There is no `System.unloadLibrary` method.

## Platforms without dynamic loading

Despite its promulgation in the 1980s through Unix and Windows, some systems still chose not to add—or even to remove—dynamic loading. For example, Plan 9 from Bell Labs and its successor 9front intentionally avoid dynamic linking, as they consider it to be "harmful". The Go programming language, by some of the same developers as Plan 9, also did not support dynamic linking, but plugin loading is available since Go 1.8 (February 2017). The Go runtime and any library functions are statically linked into the compiled binary.
