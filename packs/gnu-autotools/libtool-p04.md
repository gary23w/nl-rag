---
title: "Libtool (part 4/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 4/8
---

## 7 Library interface versions

The most difficult issue introduced by shared libraries is that of creating and resolving runtime dependencies. Dependencies on programs and libraries are often described in terms of a single name, such as `sed`. So, one may say “libtool depends on sed,” and that is good enough for most purposes.

However, when an interface changes regularly, we need to be more specific: “Gnus 5.1 requires Emacs 19.28 or above.” Here, the description of an interface consists of a name, and a “version number.”

Even that sort of description is not accurate enough for some purposes. What if Emacs 20 changes enough to break Gnus 5.1?

The same problem exists in shared libraries: we require a formal version system to describe the sorts of dependencies that programs have on shared libraries, so that the dynamic linker can guarantee that programs are linked only against libraries that provide the interface they require.

### 7.1 What are library interfaces?

Interfaces for libraries may be any of the following (and more):

- global variables: both names and types
- global functions: argument types and number, return types, and function names
- standard input, standard output, standard error, and file formats
- sockets, pipes, and other inter-process communication protocol formats

Note that static functions do not count as interfaces, because they are not directly available to the user of the library.

### 7.2 Libtool’s versioning system

Libtool has its own formal versioning system. It is not as flexible as some, but it is definitely the simplest of the more powerful versioning systems.

Think of a library as exporting several sets of interfaces, arbitrarily represented by integers. When a program is linked against a library, it may use any subset of those interfaces.

Libtool’s description of the interfaces that a program uses is simple: it encodes the least and the greatest interface numbers in the resulting binary (*first-interface*, *last-interface*).

The dynamic linker is guaranteed that if a library supports *every* interface number between *first-interface* and *last-interface*, then the program can be relinked against that library.

Note that this can cause problems because libtool’s compatibility requirements are actually stricter than is necessary.

Say libhello supports interfaces 5, 16, 17, 18, and 19, and that libtool is used to link test against libhello.

Libtool encodes the numbers 5 and 19 in test, and the dynamic linker will only link test against libraries that support *every* interface between 5 and 19. So, the dynamic linker refuses to link test against libhello!

In order to eliminate this problem, libtool only allows libraries to declare consecutive interface numbers. So, libhello can declare at most that it supports interfaces 16 through 19. Then, the dynamic linker will link test against libhello.

So, libtool library versions are described by three integers:

***current***

The most recent interface number that this library implements.

***revision***

The implementation number of the *current* interface.

***age***

The difference between the newest and oldest interfaces that this library implements. In other words, the library implements all the interface numbers in the range from number `*current* - *age*` to `*current*`.

If two libraries have identical *current* and *age* numbers, then the dynamic linker chooses the library with the greater *revision* number.

### 7.3 Updating library version information

If you want to use libtool’s versioning system, then you must specify the version information to libtool using the -version-info flag during link mode (see Link mode).

This flag accepts an argument of the form ‘*current*[:*revision*[:*age*]]’. So, passing -version-info 3:12:1 sets *current* to 3, *revision* to 12, and *age* to 1.

If either *revision* or *age* are omitted, they default to 0. Also note that *age* must be less than or equal to the *current* interface number.

Here are a set of rules to help you update your library version information:

1. Start with version information of ‘0:0:0’ for each libtool library.
2. Update the version information only immediately before a public release of your software. More frequent updates are unnecessary, and only guarantee that the current interface number gets larger faster.
3. If the library source code has changed at all since the last update, then increment *revision* (‘*c*:*r*:*a*’ becomes ‘*c*:*r+1*:*a*’).
4. If any interfaces have been added, removed, or changed since the last update, increment *current*, and set *revision* to 0.
5. If any interfaces have been added since the last public release, then increment *age*.
6. If any interfaces have been removed or changed since the last public release, then set *age* to 0.

***Never*** try to set the interface numbers so that they correspond to the release number of your package. This is an abuse that only fosters misunderstanding of the purpose of library versions. Instead, use the -release flag (see Managing release information), but be warned that every release of your package will not be binary compatible with any other release.

The following explanation may help to understand the above rules a bit better: consider that there are three possible kinds of reactions from users of your library to changes in a shared library:

1. Programs using the previous version may use the new version as drop-in replacement, and programs using the new version can also work with the previous one. In other words, no recompiling nor relinking is needed. In this case, bump *revision* only, don’t touch *current* nor *age*.
2. Programs using the previous version may use the new version as drop-in replacement, but programs using the new version may use APIs not present in the previous one. In other words, a program linking against the new version may fail with “unresolved symbols” if linking against the old version at runtime: set *revision* to 0, bump *current* and *age*.
3. Programs may need to be changed, recompiled, and relinked in order to use the new version. Bump *current*, set *revision* and *age* to 0.

In the above description, *programs* using the library in question may also be replaced by other libraries using it.

### 7.4 Managing release information

Often, people want to encode the name of the package release into the shared library so that it is obvious to the user what package their programs are linked against. This convention is used especially on GNU/Linux:

```
trick$ ls /usr/lib/libbfd*
/usr/lib/libbfd.a           /usr/lib/libbfd.so.2.7.0.2
/usr/lib/libbfd.so
trick$
```

On ‘trick’, /usr/lib/libbfd.so is a symbolic link to libbfd.so.2.7.0.2, which was distributed as a part of ‘binutils-2.7.0.2’.

Unfortunately, this convention conflicts directly with libtool’s idea of library interface versions, because the library interface rarely changes at the same time that the release number does, and the library suffix is never the same across all platforms.

So, to accommodate both views, you can use the -release flag to set release information for libraries for which you do not want to use -version-info. For the libbfd example, the next release that uses libtool should be built with ‘-release 2.9.0’, which will produce the following files on GNU/Linux:

```
trick$ ls /usr/lib/libbfd*
/usr/lib/libbfd-2.9.0.so     /usr/lib/libbfd.a
/usr/lib/libbfd.so
trick$
```

In this case, /usr/lib/libbfd.so is a symbolic link to libbfd-2.9.0.so. This makes it obvious that the user is dealing with ‘binutils-2.9.0’, without compromising libtool’s idea of interface versions.

Note that this option causes a modification of the library name, so do not use it unless you want to break binary compatibility with any past library releases. In general, you should only use -release for package-internal libraries or for ones whose interfaces change very frequently.


## 8 Tips for interface design

Writing a good library interface takes a lot of practice and thorough understanding of the problem that the library is intended to solve.

If you design a good interface, it won’t have to change often, you won’t have to keep updating documentation, and users won’t have to keep relearning how to use the library.

Here is a brief list of tips for library interface design that may help you in your exploits:

**Plan ahead**

Try to make every interface truly minimal, so that you won’t need to delete entry points very often.

**Avoid interface changes ¶**

Some people love redesigning and changing entry points just for the heck of it (note: *renaming* a function is considered changing an entry point). Don’t be one of those people. If you must redesign an interface, then try to leave compatibility functions behind so that users don’t need to rewrite their existing code.

**Use opaque data types ¶**

The fewer data type definitions a library user has access to, the better. If possible, design your functions to accept a generic pointer (that you can cast to an internal data type), and provide access functions rather than allowing the library user to directly manipulate the data. That way, you have the freedom to change the data structures without changing the interface.

This is essentially the same thing as using abstract data types and inheritance in an object-oriented system.

**Use header files ¶**

If you are careful to document each of your library’s global functions and variables in header files, and include them in your library source files, then the compiler will let you know if you make any interface changes by accident (see Writing C header files).

**Use the `static` keyword (or equivalent) whenever possible ¶**

The fewer global functions your library has, the more flexibility you’ll have in changing them. Static functions and variables may change forms as often as you like… your users cannot access them, so they aren’t interface changes.

**Be careful with array dimensions**

The number of elements in a global array is part of an interface, even if the header just declares `extern int foo[];`. This is because on i386 and some other SVR4/ELF systems, when an application references data in a shared library the size of that data (whatever its type) is included in the application executable. If you might want to change the size of an array or string then provide a pointer not the actual array.

### 8.1 Writing C header files

Writing portable C header files can be difficult, since they may be read by different types of compilers:

**C++ compilers**

C++ compilers require that functions be declared with full prototypes, since C++ is more strongly typed than C. C functions and variables also need to be declared with the `extern "C"` directive, so that the names aren’t mangled. See Writing libraries for C`++`, for other issues relevant to using C++ with libtool.

**ANSI C compilers**

ANSI C compilers are not as strict as C++ compilers, but functions should be prototyped to avoid unnecessary warnings when the header file is `#include`d.

**non-ANSI C compilers**

Non-ANSI compilers will report errors if functions are prototyped.

These complications mean that your library interface headers must use some C preprocessor magic to be usable by each of the above compilers.

foo.h, defined in the tests/demo.at Autotest of the libtool distribution, serves as an example for how to write a header file that can be safely installed in a system directory.

Here are the relevant portions of that file:

```
#ifndef FOO_H
#define FOO_H

#ifdef __cplusplus
extern "C" {
#endif

int foo (void);
int hello (void);

#ifdef __cplusplus
}
#endif

#endif /* !FOO_H */
```

This can also be achieved by utilizing macros:

```
/* BEGIN_C_DECLS should be used at the beginning of your declarations,
   so that C++ compilers don't mangle their names.  Use END_C_DECLS at
   the end of C declarations. */
#undef BEGIN_C_DECLS
#undef END_C_DECLS
#ifdef __cplusplus
# define BEGIN_C_DECLS extern "C" {
# define END_C_DECLS }
#else
# define BEGIN_C_DECLS /* empty */
# define END_C_DECLS /* empty */
#endif

/* PARAMS is a macro used to wrap function prototypes, so that
   compilers that don't understand ANSI C prototypes still work,
   and ANSI C compilers can issue warnings about type mismatches. */
#undef PARAMS
#if defined __STDC__ || defined _AIX \
        || (defined __mips && defined _SYSTYPE_SVR4) \
        || defined WIN32 || defined __cplusplus
# define PARAMS(protos) protos
#else
# define PARAMS(protos) ()
#endif
```

These macros can be used in foo.h as follows:

```
#ifndef FOO_H
#define FOO_H

/* The above macro definitions. */
#include "..."

BEGIN_C_DECLS

int foo PARAMS((void));
int hello PARAMS((void));

END_C_DECLS

#endif /* !FOO_H */
```

Note that the #ifndef FOO_H prevents the body of foo.h from being read more than once in a given compilation.

Also the only thing that must go outside the `BEGIN_C_DECLS`/`END_C_DECLS` pair are `#include` lines. Strictly speaking it is only C symbol names that need to be protected, but your header files will be more maintainable if you have a single pair of these macros around the majority of the header contents.

You should use these definitions of `PARAMS`, `BEGIN_C_DECLS`, and `END_C_DECLS` into your own headers. Then, you may use them to create header files that are valid for C++, ANSI, and non-ANSI compilers9.

Do not be naive about writing portable code. Following the tips given above will help you miss the most obvious problems, but there are definitely other subtle portability issues. You may need to cope with some of the following issues:

- Pre-ANSI compilers do not always support the `void *` generic pointer type, and so need to use `char *` in its place.
- The `const`, `inline` and `signed` keywords are not supported by some compilers, especially pre-ANSI compilers.
- The `long double` type is not supported by many compilers.


## 9 Inter-library dependencies

By definition, every shared library system provides a way for executables to depend on libraries, so that symbol resolution is deferred until runtime.

An *inter-library dependency* is where a library depends on other libraries. For example, if the libtool library libhello uses the `cos` function, then it has an inter-library dependency on libm, the math library that implements `cos`.

Some shared library systems provide this feature in an internally-consistent way: these systems allow chains of dependencies of potentially infinite length.

However, most shared library systems are restricted in that they only allow a single level of dependencies. In these systems, programs may depend on shared libraries, but shared libraries may not depend on other shared libraries.

In any event, libtool provides a simple mechanism for you to declare inter-library dependencies: for every library lib*name* that your own library depends on, simply add a corresponding `-l*name*` option to the link line when you create your library. To make an example of our libhello that depends on libm:

```
burger$ libtool --mode=link gcc -g -O -o libhello.la foo.lo hello.lo \
                -rpath /usr/local/lib -lm
burger$
```

When you link a program against libhello, you don’t need to specify the same ‘-l’ options again: libtool will do that for you, to guarantee that all the required libraries are found. This restriction is only necessary to preserve compatibility with static library systems and simple dynamic library systems.

Some platforms, such as Windows, do not even allow you this flexibility. In order to build a shared library, it must be entirely self-contained or it must have dependencies known at link time (that is, have references only to symbols that are found in the .lo files or the specified ‘-l’ libraries), and you need to specify the -no-undefined flag. By default, libtool builds only static libraries on these kinds of platforms.

The simple-minded inter-library dependency tracking code of libtool releases prior to 1.2 was disabled because it was not clear when it was possible to link one library with another, and complex failures would occur. A more complex implementation of this concept was re-introduced before release 1.3, but it has not been ported to all platforms that libtool supports. The default, conservative behavior is to avoid linking one library with another, introducing their inter-dependencies only when a program is linked with them.


## 10 Dlopened modules

It can sometimes be confusing to discuss *dynamic linking*, because the term is used to refer to two different concepts:

1. Compiling and linking a program against a shared library, which is resolved automatically at run time by the dynamic linker. In this process, dynamic linking is transparent to the application.
2. The application calling functions such as `dlopen` that load arbitrary, user-specified modules at runtime. This type of dynamic linking is explicitly controlled by the application.

To mitigate confusion, this manual refers to the second type of dynamic linking as *dlopening* a module.

The main benefit to dlopening object modules is the ability to access compiled object code to extend your program, rather than using an interpreted language. In fact, dlopen calls are frequently used in language interpreters to provide an efficient way to extend the language.

Libtool provides support for dlopened modules. However, you should indicate that your package is willing to use such support, by using the `LT_INIT` option ‘dlopen’ in configure.ac. If this option is not given, libtool will assume no dlopening mechanism is available, and will try to simulate it.

This chapter discusses how you as a dlopen application developer might use libtool to generate dlopen-accessible modules.

### 10.1 Building modules to dlopen

On some operating systems, a program symbol must be specially declared in order to be dynamically resolved with the `dlsym` (or equivalent) function. Libtool provides the -export-dynamic and -module link flags (see Link mode), for you to make that declaration. You need to use these flags if you are linking an application program that dlopens other modules or a libtool library that will also be dlopened.

For example, if we wanted to build a shared library, hello, that would later be dlopened by an application, we would add -module to the other link flags:

```
burger$ libtool --mode=link gcc -module -o hello.la foo.lo \
                hello.lo -rpath /usr/local/lib -lm
burger$
```

If symbols from your *executable* are needed to satisfy unresolved references in a library you want to dlopen you will have to use the flag -export-dynamic. You should use -export-dynamic while linking the executable that calls dlopen:

```
burger$ libtool --mode=link gcc -export-dynamic -o helldl main.o
burger$
```

### 10.2 Dlpreopening

Libtool provides special support for dlopening libtool object and libtool library files, so that their symbols can be resolved *even on platforms without any `dlopen` and `dlsym` functions*.

Consider the following alternative ways of loading code into your program, in order of increasing “laziness”:

1. Linking against object files that become part of the program executable, whether or not they are referenced. If an object file cannot be found, then the compile time linker refuses to create the executable.
2. Declaring a static library to the linker, so that it is searched at link time to satisfy any undefined references in the above object files. If the static library cannot be found, then the compile time linker refuses to create the executable.
3. Declaring a shared library to the runtime linker, so that it is searched at runtime to satisfy any undefined references in the above files. If the shared library cannot be found, then the dynamic linker aborts the program before it runs.
4. Dlopening a module, so that the application can resolve its own, dynamically-computed references. If there is an error opening the module, or the module is not found, then the application can recover without crashing.

Libtool emulates -dlopen on static platforms by linking objects into the program at compile time, and creating data structures that represent the program’s symbol table. In order to use this feature, you must declare the objects you want your application to dlopen by using the -dlopen or -dlpreopen flags when you link your program (see Link mode).

**Data Type: **lt_dlsymlist** *typedef struct { const char *`name`; void *`address`; } lt_dlsymlist* ¶**

The `name` attribute is a null-terminated character string of the symbol name, such as `"fprintf"`. The `address` attribute is generic pointer to the appropriate object, such as `&fprintf`.

**Variable: `const lt_dlsymlist` **lt_preloaded_symbols[]** ¶**

An array of `lt_dlsymlist` structures, representing all the preloaded symbols linked into the program proper. For each module -dlpreopened by the Libtool linked program there is an element with the `name` of the module and an `address` of `0`, followed by all symbols exported from this file. For the executable itself the special name ‘@PROGRAM@’ is used. The last element of all has a `name` and `address` of `0`.

To facilitate inclusion of symbol lists into libraries, `lt_preloaded_symbols` is ‘#define’d to a suitably unique name in ltdl.h.

This variable may not be declared `const` on some systems due to relocation issues.

Some compilers may allow identifiers that are not valid in ANSI C, such as dollar signs. Libtool only recognizes valid ANSI C symbols (an initial ASCII letter or underscore, followed by zero or more ASCII letters, digits, and underscores), so non-ANSI symbols will not appear in `lt_preloaded_symbols`.

**Function: `int` **lt_dlpreload** `(const lt_dlsymlist **preloaded*)` ¶**

Register the list of preloaded modules *preloaded*. If *preloaded* is `NULL`, then all previously registered symbol lists, except the list set by `lt_dlpreload_default`, are deleted. Return 0 on success.

**Function: `int` **lt_dlpreload_default** `(const lt_dlsymlist **preloaded*)` ¶**

Set the default list of preloaded modules to *preloaded*, which won’t be deleted by `lt_dlpreload`. Note that this function does *not* require libltdl to be initialized using `lt_dlinit` and can be used in the program to register the default preloaded modules. Instead of calling this function directly, most programs will use the macro `LTDL_SET_PRELOADED_SYMBOLS`.

Return 0 on success.

**Macro: **LTDL_SET_PRELOADED_SYMBOLS** ¶**

Set the default list of preloaded symbols. Should be used in your program to initialize libltdl’s list of preloaded modules.

```
#include <ltdl.h>

int main() {
  /* ... */
  LTDL_SET_PRELOADED_SYMBOLS();
  /* ... */
}
```

**Function Type: `int` **lt_dlpreload_callback_func** `(lt_dlhandle *handle*)` ¶**

Functions of this type can be passed to `lt_dlpreload_open`, which in turn will call back into a function thus passed for each preloaded module that it opens.

**Function: `int` **lt_dlpreload_open** `(const char **originator*, lt_dlpreload_callback_func **func*)` ¶**

Load all of the preloaded modules for *originator*. For every module opened in this way, call *func*.

To open all of the modules preloaded into libhell.la (presumably from within the libhell.a initialisation code):

```
#define preloaded_symbols lt_libhell_LTX_preloaded_symbols

static int hell_preload_callback (lt_dlhandle handle);

int
hell_init (void)
{
  ...
  if (lt_dlpreload (&preloaded_symbols) == 0)
    {
      lt_dlpreload_open ("libhell", preload_callback);
    }
  ...
}
```

Note that to prevent clashes between multiple preloaded modules, the preloaded symbols are accessed via a mangled symbol name: to get the symbols preloaded into ‘libhell’, you must prefix ‘preloaded_symbols’ with ‘lt_’; the originator name, ‘libhell’ in this case; and ‘_LTX_’. That is, ‘lt_libhell_LTX_preloaded_symbols’ here.

### 10.3 Linking with dlopened modules

When, say, an interpreter application uses dlopened modules to extend the list of methods it provides, an obvious abstraction for the maintainers of the interpreter is to have all methods (including the built in ones supplied with the interpreter) accessed through dlopen. For one thing, the dlopening functionality will be tested even during routine invocations. For another, only one subsystem has to be written for getting methods into the interpreter.

The downside of this abstraction is, of course, that environments that provide only static linkage can’t even load the intrinsic interpreter methods. Not so! We can statically link those methods by **dlpreopening** them.

Unfortunately, since platforms such as AIX and cygwin require that all library symbols must be resolved at compile time, the interpreter maintainers will need to provide a library to both its own dlpreopened modules, and third-party modules loaded by dlopen. In itself, that is not so bad, except that the interpreter too must provide those same symbols otherwise it will be impossible to resolve all the symbols required by the modules as they are loaded. Things are even worse if the code that loads the modules for the interpreter is itself in a library – and that is usually the case for any non-trivial application. Modern platforms take care of this by automatically loading all of a module’s dependency libraries as the module is loaded (libltdl can do this even on platforms that can’t do it by themselves). In the end, this leads to problems with duplicated symbols and prevents modules from loading, and prevents the application from compiling when modules are preloaded.

```
,-------------.    ,------------------.    ,-----------------.
| Interpreter |---->     Module------------>   Third-party   |
`-------------'    |     Loader       |    |Dlopened Modules |
                   |        |         |    `-----------------'
                   |,-------v--------.|             |
                   ||  Dlpreopened   ||             |
                   ||    Modules     ||             |
                   |`----------------'|             |
                   |        |         |             |
                   |,-------v--------.|    ,--------v--------.
                   ||Module Interface||    |Module Interface |
                   ||    Library     ||    |     Library     |
                   |`----------------'|    `-----------------'
                   `------------------'
```

Libtool has the concept of *weak library interfaces* to circumvent this problem. Recall that the code that dlopens method-provider modules for the interpreter application resides in a library: All of the modules and the dlopener library itself should be linked against the common library that resolves the module symbols at compile time. To guard against duplicate symbol definitions, and for dlpreopened modules to work at all in this scenario, the dlopener library must declare that it provides a weak library interface to the common symbols in the library it shares with the modules. That way, when `libtool` links the **Module Loader** library with some **Dlpreopened Modules** that were in turn linked against the **Module Interface Library**, it knows that the **Module Loader** provides an already loaded **Module Interface Library** to resolve symbols for the **Dlpreopened Modules**, and doesn’t ask the compiler driver to link an identical **Module Interface Library** dependency library too.

In conjunction with Automake, the Makefile.am for the **Module Loader** might look like this:

```
lib_LTLIBRARIES = libinterface.la libloader.la

libinterface_la_SOURCES = interface.c interface.h
libinterface_la_LDFLAGS = -version-info 3:2:1

libloader_la_SOURCES    = loader.c
libloader_la_LDFLAGS    = -weak libinterface.la \
                          -version-info 3:2:1 \
                          -dlpreopen ../modules/intrinsics.la
libloader_la_LIBADD     = $(libinterface_la_OBJECTS)
```

And the Makefile.am for the intrinsics.la module in a sibling modules directory might look like this:

```
AM_CPPFLAGS             = -I$(srcdir)/../libloader
AM_LDFLAGS              = -no-undefined -module -avoid-version \
                          -export-dynamic

noinst_LTLIBRARIES      = intrinsics.la

intrinsics_la_LIBADD    = ../libloader/libinterface.la

../libloader/libinterface.la:
        cd ../libloader && $(MAKE) $(AM_MAKEFLAGS) libinterface.la
```

For a more complex example, see the sources of libltdl in the Libtool distribution, which is built with the help of the -weak option.

### 10.4 Finding the correct name to dlopen

After a library has been linked with -module, it can be dlopened. Unfortunately, because of the variation in library names, your package needs to determine the correct file to dlopen.

The most straightforward and flexible implementation is to determine the name at runtime, by finding the installed .la file, and searching it for the following lines:

```
# The name that we can dlopen.
dlname='dlname'
```

If *dlname* is empty, then the library cannot be dlopened. Otherwise, it gives the dlname of the library. So, if the library was installed as /usr/local/lib/libhello.la, and the *dlname* was libhello.so.3, then /usr/local/lib/libhello.so.3 should be dlopened.

If your program uses this approach, then it should search the directories listed in the `LD_LIBRARY_PATH`10 environment variable, as well as the directory where libraries will eventually be installed. Searching this variable (or equivalent) will guarantee that your program can find its dlopened modules, even before installation, provided you have linked them using libtool.

### 10.5 Unresolved dlopen issues

The following problems are not solved by using libtool’s dlopen support:

- Dlopen functions are generally only available on shared library platforms. If you want your package to be portable to static platforms, you have to use either libltdl (see Using libltdl) or develop your own alternatives to dlopening dynamic code. Most reasonable solutions involve writing wrapper functions for the `dlopen` family, which do package-specific tricks when dlopening is unsupported or not available on a given platform.
- There are major differences in implementations of the `dlopen` family of functions. Some platforms do not even use the same function names (notably HP-UX, with its `shl_load` family).
- The application developer must write a custom search function to discover the correct module filename to supply to `dlopen`.
