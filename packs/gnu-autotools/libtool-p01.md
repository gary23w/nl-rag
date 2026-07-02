---
title: "Libtool (part 1/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 1/8
---

# Shared library support for GNU

This file documents GNU Libtool, a script that allows package developers to provide generic shared library support. This edition documents version 2.5.4.

See Reporting bugs, for information on how to report problems with GNU Libtool.


## 1 Introduction

In the past, if you were a source code package developer and wanted to take advantage of the power of shared libraries, you needed to write custom support code for each platform on which your package ran. You also had to design a configuration interface so that the package installer could choose what sort of libraries were built.

GNU Libtool simplifies your job by encapsulating both the platform-specific dependencies, and the user interface, in a single script. GNU Libtool is designed so that the complete functionality of each host type is available via a generic interface, but nasty quirks are hidden from the programmer.

GNU Libtool’s consistent interface is reassuring… users don’t need to read obscure documentation to have their favorite source package build shared libraries. They just run your package `configure` script (or equivalent), and libtool does all the dirty work.

There are several examples throughout this document. All assume the same environment: we want to build a library, libhello, in a generic way.

libhello could be a shared library, a static library, or both… whatever is available on the host system, as long as libtool has been ported to it.

This chapter explains the original design philosophy of libtool. Feel free to skip to the next chapter, unless you are interested in history, or want to write code to extend libtool in a consistent way.

### 1.1 Motivation for writing libtool

Since early 1995, several different GNU developers have recognized the importance of having shared library support for their packages. The primary motivation for such a change is to encourage modularity and reuse of code (both conceptually and physically) in GNU programs.

Such a demand means that the way libraries are built in GNU packages needs to be general, to allow for any library type the package installer might want. The problem is compounded by the absence of a standard procedure for creating shared libraries on different platforms.

The following sections outline the major issues facing shared library support in GNU, and how shared library support could be standardized with libtool.

The following specifications were used in developing and evaluating this system:

1. The system must be as elegant as possible.
2. The system must be fully integrated with the GNU Autoconf and Automake utilities, so that it will be easy for GNU maintainers to use. However, the system must not require these tools, so that it can be used by non-GNU packages.
3. Portability to other (non-GNU) architectures and tools is desirable.

### 1.2 Implementation issues

The following issues need to be addressed in any reusable shared library system, specifically libtool:

1. The package installer should be able to control what sort of libraries are built.
2. It can be tricky to run dynamically linked programs whose libraries have not yet been installed. `LD_LIBRARY_PATH` must be set properly (if it is supported), or programs fail to run.
3. The system must operate consistently even on hosts that don’t support shared libraries.
4. The commands required to build shared libraries may differ wildly from host to host. These need to be determined at configure time in a consistent way.
5. It is not always obvious with what prefix or suffix a shared library should be installed. This makes it difficult for Makefile rules, since they generally assume that file names are the same from host to host.
6. The system needs a simple library version number abstraction, so that shared libraries can be upgraded in place. The programmer should be informed how to design the interfaces to the library to maximize binary compatibility.
7. The install Makefile target should warn the package installer to set the proper environment variables (`LD_LIBRARY_PATH` or equivalent), or run `ldconfig`.

### 1.3 Other implementations

Even before libtool was developed, many free software packages built and installed their own shared libraries. At first, these packages were examined to avoid reinventing existing features.

Now it is clear that none of these packages have documented the details of shared library systems that libtool requires. So, other packages have been more or less abandoned as influences.

### 1.4 A postmortem analysis of other implementations

In all fairness, each of the implementations that were examined do the job that they were intended to do, for a number of different host systems. However, none of these solutions seem to function well as a generalized, reusable component.

Most were too complex to use (much less modify) without understanding exactly what the implementation does, and they were generally not documented.

The main difficulty is that different vendors have different views of what libraries are, and none of the packages that were examined seemed to be confident enough to settle on a single paradigm that just *works*.

Ideally, libtool would be a standard that would be implemented as series of extensions and modifications to existing library systems to make them work consistently. However, it is not an easy task to convince operating system developers to mend their evil ways, and people want to build shared libraries right now, even on buggy, broken, confused operating systems.

For this reason, libtool was designed as an independent shell script. It isolates the problems and inconsistencies in library building that plague Makefile writers by wrapping the compiler suite on different platforms with a consistent, powerful interface.

With luck, libtool will be useful to and used by the GNU community, and that the lessons that were learned in writing it will be taken up by designers of future library systems.


## 2 The libtool paradigm

At first, libtool was designed to support an arbitrary number of library object types. After libtool was ported to more platforms, a new paradigm gradually developed for describing the relationship between libraries and programs.

In summary, “libraries are programs with multiple entry points, and more formally defined interfaces.”

The best way to introduce the libtool paradigm is to contrast it with the paradigm of existing library systems, with examples from each. It is a new way of thinking, so it may take a little time to absorb, but when you understand it, the world becomes simpler.


## 3 Using libtool

It makes little sense to talk about using libtool in your own packages until you have seen how it makes your life simpler. The examples in this chapter introduce the main features of libtool by comparing the standard library building procedure to libtool’s operation on two different platforms:

**‘a23’**

An Ultrix 4.2 platform with only static libraries.

**‘burger’**

A NetBSD/i386 1.2 platform with shared libraries.

Source files for the following examples are taken from the Autotest file tests/demo.at. The files can be extracted by running a demo test and preserving the artifacts:

```
burger$ make check TESTSUITEFLAGS="-d -k 'preloaded static library'"
burger$ cp -r tests/testsuite.dir/027 demo/
```

You can follow these examples on your own platform, using the preconfigured libtool script that was installed with libtool (see Configuring libtool). Assume that we are building a library, libhello, out of the files foo.c and hello.c.

Note that the foo.c source file uses the `cos` math library function, which is usually found in the standalone math library, and not the C library (see Trigonometric Functions in *The GNU C Library Reference Manual*). So, we need to add -lm to the end of the link line whenever we link foo.lo into an executable or a library (see Inter-library dependencies).

The same rule applies whenever you use functions that don’t appear in the standard C library… you need to add the appropriate -l*name* flag to the end of the link line when you link against those objects.

After we have built that library, we want to create a program by linking main.o against libhello.

### 3.1 Creating object files

To create an object file from a source file, the compiler is invoked with the -c flag (and any other desired flags):

```
burger$ gcc -I. -g -O -c main.c
burger$
```

The above compiler command produces an object file, usually named main.o, from the source file main.c.

For most library systems, creating object files that become part of a static library is as simple as creating object files that are linked to form an executable:

```
burger$ gcc -I. -g -O -c foo.c
burger$ gcc -I. -g -O -c hello.c
burger$
```

Shared libraries, however, may only be built from *position-independent code* (PIC). So, special flags must be passed to the compiler to tell it to generate PIC rather than the standard position-dependent code.

Since this is a library implementation detail, libtool hides the complexity of PIC compiler flags and uses separate library object files (the PIC one lives in the .libs subdirectory and the static one lives in the current directory). On systems without shared libraries, the PIC library object files are not created, whereas on systems where all code is PIC, such as AIX, the static ones are not created.

To create library object files for foo.c and hello.c, simply invoke libtool with the standard compilation command as arguments (see Compile mode):

```
a23$ libtool --mode=compile gcc -I. -g -O -c foo.c
gcc -I. -g -O -c foo.c -o foo.o
a23$ libtool --mode=compile gcc -I. -g -O -c hello.c
gcc -I. -g -O -c hello.c -o hello.o
a23$
```

Note that libtool silently creates an additional control file on each ‘compile’ invocation. The .lo file is the libtool object, which Libtool uses to determine what object file may be built into a shared library. On ‘a23’, only static libraries are supported so the library objects look like this:

```
# foo.lo - a libtool object file
# Generated by ltmain.sh (GNU libtool) 2.5.4
#
# Please DO NOT delete this file!
# It is necessary for linking the library.

# Name of the PIC object.
pic_object=none

# Name of the non-PIC object.
non_pic_object='foo.o'
```

On shared library systems, libtool automatically generates an additional PIC object by inserting the appropriate PIC generation flags into the compilation command:

```
burger$ libtool --mode=compile gcc -I. -g -O -c foo.c
mkdir .libs
gcc -I. -g -O -c foo.c  -fPIC -DPIC -o .libs/foo.o
gcc -I. -g -O -c foo.c -o foo.o >/dev/null 2>&1
burger$
```

Note that Libtool automatically created the .libs directory upon its first execution, where PIC library object files will be stored.

Since ‘burger’ supports shared libraries, and requires PIC objects to build them, Libtool has compiled a PIC object and made a note of it in the libtool object:

```
# foo.lo - a libtool object file
# Generated by ltmain.sh (GNU libtool) 2.5.4
#
# Please DO NOT delete this file!
# It is necessary for linking the library.

# Name of the PIC object.
pic_object='.libs/foo.o'

# Name of the non-PIC object.
non_pic_object='foo.o'
```

Notice the second run of GCC has its output discarded. This is done so the compiler warnings aren’t annoyingly duplicated. If you need to see both sets of warnings (you might have conditional code inside ‘#ifdef PIC’ for example), you can turn off suppression by passing the -no-suppress option to libtool’s compile mode:

```
burger$ libtool --mode=compile gcc -no-suppress -I. -g -O -c hello.c
gcc -I. -g -O -c hello.c  -fPIC -DPIC -o .libs/hello.o
gcc -I. -g -O -c hello.c -o hello.o
burger$
```

### 3.2 Linking libraries

Without libtool, the programmer would invoke the `ar` command to create a static library:

```
burger$ ar cr libhello.a hello.o foo.o
burger$
```

But of course, that would be too simple, so many systems require that you run the `ranlib` command on the resulting library in order to generate a symbol table:

```
burger$ ranlib libhello.a
burger$
```

It seems more natural to use the C compiler for this task, given libtool’s “libraries are programs” approach. So, on platforms without shared libraries, libtool simply acts as a wrapper for the system `ar` (and possibly `ranlib`) commands.

Again, the libtool control file name (.la suffix) differs from the standard library name (.a suffix). The arguments to libtool are the same ones you would use to produce an executable named libhello.la with your compiler (see Link mode):

```
a23$ libtool --mode=link gcc -g -O -o libhello.la foo.o hello.o
*** Warning: Linking the shared library libhello.la against the
*** non-libtool objects foo.o hello.o is not portable!
ar cr .libs/libhello.a
ranlib .libs/libhello.a
creating libhello.la
(cd .libs && rm -f libhello.la && ln -s ../libhello.la libhello.la)
a23$
```

Aha! Libtool caught a common error… trying to build a library from standard objects instead of special .lo object files. This doesn’t matter so much for static libraries, but on shared library systems, it is of great importance. (Note that you may replace libhello.la with libhello.a in which case libtool won’t issue the warning any more. But although this method works, this is not intended to be used because it makes you lose the benefits of using Libtool.)

So, let’s try again, this time with the library object files. Remember also that we need to add -lm to the link command line because foo.c uses the `cos` math library function (see Using libtool).

Another complication in building shared libraries is that we need to specify the path to the directory where they will (eventually) be installed (in this case, /usr/local/lib)1:

```
a23$ libtool --mode=link gcc -g -O -o libhello.la foo.lo hello.lo \
                -rpath /usr/local/lib -lm
ar cr .libs/libhello.a foo.o hello.o
ranlib .libs/libhello.a
creating libhello.la
(cd .libs && rm -f libhello.la && ln -s ../libhello.la libhello.la)
a23$
```

Now, let’s try the same trick on the shared library platform:

```
burger$ libtool --mode=link gcc -g -O -o libhello.la foo.lo hello.lo \
                -rpath /usr/local/lib -lm
rm -fr  .libs/libhello.a .libs/libhello.la
ld -Bshareable -o .libs/libhello.so.0.0 .libs/foo.o .libs/hello.o -lm
ar cr .libs/libhello.a foo.o hello.o
ranlib .libs/libhello.a
creating libhello.la
(cd .libs && rm -f libhello.la && ln -s ../libhello.la libhello.la)
burger$
```

Now that’s significantly cooler… Libtool just ran an obscure `ld` command to create a shared library, as well as the static library.

Note how libtool creates extra files in the .libs subdirectory, rather than the current directory. This feature makes it easier to clean up the build directory, and helps ensure other programs fail horribly if you accidentally forget to use libtool when you should.

Again, you should look at the .la file to see what Libtool stores in it. You will see Libtool uses this file to remember the destination directory for the library (the argument to -rpath) as well as the dependency on the math library (‘-lm’).

### 3.3 Linking executables

If you choose at this point to *install* the library (put it in a permanent location) before linking executables against it, then you don’t need to use libtool to do the linking. Simply use the appropriate -L and -l flags to specify the library’s location.

Some system linkers insist on encoding the full directory name of each shared library in the resulting executable. Libtool has to work around this misfeature by special magic to ensure that only permanent directory names are put into installed executables.

The importance of this bug must not be overlooked: it won’t cause programs to crash in obvious ways. It creates a security hole, and possibly even worse, if you are modifying the library source code after you have installed the package, you will change the behaviour of the installed programs!

So, if you want to link programs against the library before you install it, you must use libtool to do the linking.

Here’s the old way of linking against an uninstalled library:

```
burger$ gcc -g -O -o hell.old main.o libhello.a -lm
burger$
```

Libtool’s way is almost the same2 (see Link mode):

```
a23$ libtool --mode=link gcc -g -O -o hell main.o libhello.la
gcc -g -O -o hell main.o  ./.libs/libhello.a -lm
a23$
```

That looks too simple to be true. All libtool did was transform libhello.la to ./.libs/libhello.a, but remember that ‘a23’ has no shared libraries. Notice Libtool also remembered libhello.la depends on -lm, so even though we didn’t specify -lm on the libtool command line3 Libtool has added it to the `gcc` link line for us.

On ‘burger’ Libtool links against the uninstalled shared library:

```
burger$ libtool --mode=link gcc -g -O -o hell main.o libhello.la
gcc -g -O -o .libs/hell main.o -L./.libs -R/usr/local/lib -lhello -lm
creating hell
burger$
```

Now assume libhello.la had already been installed, and you want to link a new program with it. You could figure out where it lives by yourself, then run:

```
burger$ gcc -g -O -o test test.o -L/usr/local/lib -lhello -lm
```

However, unless /usr/local/lib is in the standard library search path, you won’t be able to run `test`. If instead you use libtool to link the already-installed libtool library, it will do The Right Thing (TM) for you:

```
burger$ libtool --mode=link gcc -g -O -o test test.o \
                /usr/local/lib/libhello.la
gcc -g -O -o .libs/test test.o -Wl,--rpath \
        -Wl,/usr/local/lib /usr/local/lib/libhello.a -lm
creating test
burger$
```

Note that libtool added the necessary run-time path flag, as well as -lm, the library libhello.la depended upon. Nice, huh?

Notice the executable, `hell`, was actually created in the .libs subdirectory. Then, a wrapper script (or, on certain platforms, a wrapper executable see Wrapper executables for uninstalled programs) was created in the current directory.

Since libtool created a wrapper script, you should use libtool to install it and debug it too. However, since the program does not depend on any uninstalled libtool library, it is probably usable even without the wrapper script.

On NetBSD 1.2, libtool encodes the installation directory of libhello, by using the ‘-R/usr/local/lib’ compiler flag. Then, the wrapper script guarantees the executable finds the correct shared library (the one in ./.libs) so it can be properly installed.

Let’s compare the two different programs:

```
burger$ time ./hell.old
Welcome to GNU Hell!
** This is not GNU Hello.  There is no built-in mail reader. **
        0.21 real         0.02 user         0.08 sys
burger$ time ./hell
Welcome to GNU Hell!
** This is not GNU Hello.  There is no built-in mail reader. **
        0.63 real         0.09 user         0.59 sys
burger$
```

The wrapper script takes significantly longer to execute, but at least the results are correct, even though the shared library hasn’t been installed yet.

So, what about all the space savings that shared libraries are supposed to yield?

```
burger$ ls -l hell.old libhello.a
-rwxr-xr-x  1 gord  gord  15481 Nov 14 12:11 hell.old
-rw-r--r--  1 gord  gord   4274 Nov 13 18:02 libhello.a
burger$ ls -l .libs/hell .libs/libhello.*
-rwxr-xr-x  1 gord  gord  11647 Nov 14 12:10 .libs/hell
-rw-r--r--  1 gord  gord   4274 Nov 13 18:44 .libs/libhello.a
-rwxr-xr-x  1 gord  gord  12205 Nov 13 18:44 .libs/libhello.so.0.0
burger$
```

Well, that sucks. Maybe I should just scrap this project and take up basket weaving.

Actually, it just proves an important point: shared libraries incur overhead because of their (relative) complexity. In this situation, the price of being dynamic is eight kilobytes, and the payoff is about four kilobytes. So, having a shared libhello won’t be an advantage until we link it against at least a few more programs.

#### 3.3.1 Wrapper executables for uninstalled programs

Some platforms, notably those hosted on Windows such as Cygwin and MinGW, use a wrapper executable rather than a wrapper script to ensure proper operation of uninstalled programs linked by libtool against uninstalled shared libraries. The wrapper executable thus performs the same function as the wrapper script used on other platforms, but allows to satisfy the `make` rules for the program, whose name ends in `$(EXEEXT)`. The actual program executable is created below .libs, and its name will end in `$(EXEEXT)` and may or may not contain an `lt-` prefix. This wrapper executable sets various environment values so that the program executable may locate its (uninstalled) shared libraries, and then launches the program executable.

The wrapper executable provides a debug mode, enabled by passing the command-line option `--lt-debug` (see below). When executing in debug mode, diagnostic information will be printed to `stderr` before the program executable is launched.

Finally, the wrapper executable supports a number of command line options that may be useful when debugging the operation of the wrapper system. All of these options begin with `--lt-`, and if present they and their arguments will be removed from the argument list passed on to the program executable. Therefore, the program executable may not employ command line options that begin with `--lt-`. (In fact, the wrapper executable will detect any command line options that begin with `--lt-` and abort with an error message if the option is not recognized.) If this presents a problem, please contact the Libtool team at the Libtool bug reporting address bug-libtool@gnu.org.

These command line options include:

**--lt-dump-script**

Causes the wrapper to print a copy of the wrapper *script* to `stdout`, and exit.

**--lt-debug**

Causes the wrapper to print diagnostic information to `stdout`, before launching the program executable.

For consistency, both the wrapper *script* and the wrapper *executable* support these options.

### 3.4 Debugging executables

If hell was a complicated program, you would certainly want to test and debug it before installing it on your system. In the above section, you saw how the libtool wrapper script makes it possible to run the program directly, but unfortunately, this mechanism interferes with the debugger:

```
burger$ gdb hell
GDB is free software and you are welcome to distribute copies of it
 under certain conditions; type "show copying" to see the conditions.
There is no warranty for GDB; type "show warranty" for details.
GDB 4.16 (i386-unknown-netbsd), (C) 1996 Free Software Foundation, Inc.

"hell": not in executable format: File format not recognized

(gdb) quit
burger$
```

Sad. It doesn’t work because GDB doesn’t know where the executable lives. So, let’s try again, by invoking GDB directly on the executable:

```
burger$ gdb .libs/hell
GNU gdb 5.3 (i386-unknown-netbsd)
Copyright 2002 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License,
and you are welcome to change it and/or distribute copies of it
under certain conditions.  Type "show copying" to see the conditions.
There is no warranty for GDB.  Type "show warranty" for details.
(gdb) break main
Breakpoint 1 at 0x8048547: file main.c, line 29.
(gdb) run
Starting program: /home/src/libtool/demo/.libs/hell
/home/src/libtool/demo/.libs/hell: can't load library 'libhello.so.0'

Program exited with code 020.
(gdb) quit
burger$
```

Argh. Now GDB complains because it cannot find the shared library that hell is linked against. So, we must use libtool to properly set the library path and run the debugger. Fortunately, we can forget all about the .libs directory, and just run it on the executable wrapper (see Execute mode):

```
burger$ libtool --mode=execute gdb hell
GNU gdb 5.3 (i386-unknown-netbsd)
Copyright 2002 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License,
and you are welcome to change it and/or distribute copies of it
under certain conditions.  Type "show copying" to see the conditions.
There is no warranty for GDB.  Type "show warranty" for details.
(gdb) break main
Breakpoint 1 at 0x8048547: file main.c, line 29.
(gdb) run
Starting program: /home/src/libtool/demo/.libs/hell

Breakpoint 1, main (argc=1, argv=0xbffffc40) at main.c:29
29        printf ("Welcome to GNU Hell!\n");
(gdb) quit
The program is running.  Quit anyway (and kill it)? (y or n) y
burger$
```

### 3.5 Installing libraries

Installing libraries on a non-libtool system is quite straightforward… just copy them into place:4

```
burger$ su
Password: ********
burger# cp libhello.a /usr/local/lib/libhello.a
burger#
```

Oops, don’t forget the `ranlib` command:

```
burger# ranlib /usr/local/lib/libhello.a
burger#
```

Libtool installation is quite simple, as well. Just use the `install` or `cp` command that you normally would (see Install mode):

```
a23# libtool --mode=install cp libhello.la /usr/local/lib/libhello.la
cp libhello.la /usr/local/lib/libhello.la
cp .libs/libhello.a /usr/local/lib/libhello.a
ranlib /usr/local/lib/libhello.a
a23#
```

Note that the libtool library libhello.la is also installed, to help libtool with uninstallation (see Uninstall mode) and linking (see Linking executables) and to help programs with dlopening (see Dlopened modules).

Here is the shared library example:

```
burger# libtool --mode=install install -c libhello.la \
                /usr/local/lib/libhello.la
install -c .libs/libhello.so.0.0 /usr/local/lib/libhello.so.0.0
install -c libhello.la /usr/local/lib/libhello.la
install -c .libs/libhello.a /usr/local/lib/libhello.a
ranlib /usr/local/lib/libhello.a
burger#
```

It is safe to specify the -s (strip symbols) flag if you use a BSD-compatible install program when installing libraries. Libtool will either ignore the -s flag, or will run a program that will strip only debugging and compiler symbols from the library.

Once the libraries have been put in place, there may be some additional configuration that you need to do before using them. First, you must make sure that where the library is installed actually agrees with the -rpath flag you used to build it.

Then, running ‘libtool -n finish *libdir*’ can give you further hints on what to do (see Finish mode):

```
burger# libtool -n finish /usr/local/lib
PATH="$PATH:/sbin" ldconfig -m /usr/local/lib
-----------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib

To link against installed libraries in a given directory, LIBDIR,
you must use the '-LLIBDIR' flag during linking.

 You will also need to do one of the following:
   - add LIBDIR to the 'LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the 'LD_RUN_PATH' environment variable
     during linking
   - use the '-RLIBDIR' linker flag

See any operating system documentation about shared libraries for
more information, such as the ld and ld.so manual pages.
-----------------------------------------------------------------
burger#
```

After you have completed these steps, you can go on to begin using the installed libraries. You may also install any executables that depend on libraries you created.

### 3.6 Installing executables

If you used libtool to link any executables against uninstalled libtool libraries (see Linking executables), you need to use libtool to install the executables after the libraries have been installed (see Installing libraries).

So, for our Ultrix example, we would run:

```
a23# libtool --mode=install install -c hell /usr/local/bin/hell
install -c hell /usr/local/bin/hell
a23#
```

On shared library systems that require wrapper scripts, libtool just ignores the wrapper script and installs the correct binary:

```
burger# libtool --mode=install install -c hell /usr/local/bin/hell
install -c .libs/hell /usr/local/bin/hell
burger#
```

### 3.7 Linking static libraries

Why return to `ar` and `ranlib` silliness when you’ve had a taste of libtool? Well, sometimes it is desirable to create a static archive that can never be shared. The most frequent case is when you have a set of object files that you use to build several different libraries. You can create a “convenience library” out of those objects, and link against that with the other libraries, instead of listing all the object files every time.

If you just want to link this convenience library into programs, then you could just ignore libtool entirely, and use the old `ar` and `ranlib` commands (or the corresponding GNU Automake ‘_LIBRARIES’ rules). You can even install a convenience library using GNU Libtool, though you probably don’t want to and hence GNU Automake doesn’t allow you to do so.

```
burger$ libtool --mode=install ./install-sh -c libhello.a \
                /local/lib/libhello.a
./install-sh -c libhello.a /local/lib/libhello.a
ranlib /local/lib/libhello.a
burger$
```

Using libtool for static library installation protects your library from being accidentally stripped (if the installer used the -s flag), as well as automatically running the correct `ranlib` command.

But libtool libraries are more than just collections of object files: they can also carry library dependency information, which old archives do not. If you want to create a libtool static convenience library, you can omit the -rpath flag and use -static to indicate that you’re only interested in a static library. When you link a program with such a library, libtool will actually link all object files and dependency libraries into the program.

If you omit both -rpath and -static, libtool will create a convenience library that can be used to create other libtool libraries, even shared ones. Just like in the static case, the library behaves as an alias to a set of object files and dependency libraries, but in this case the object files are suitable for inclusion in shared libraries. But be careful not to link a single convenience library, directly or indirectly, into a single program or library, otherwise you may get errors about symbol redefinitions.

The key is remembering that a convenience library contains PIC objects, and can be linked where a list of PIC objects makes sense; i.e. into a shared library. A static convenience library contains non-PIC objects, so can be linked into an old static library, or a program.

When GNU Automake is used, you should use `noinst_LTLIBRARIES` instead of `lib_LTLIBRARIES` for convenience libraries, so that the -rpath option is not passed when they are linked.

As a rule of thumb, link a libtool convenience library into at most one libtool library, and never into a program, and link libtool static convenience libraries only into programs, and only if you need to carry library dependency information to the user of the static convenience library.

Another common situation where static linking is desirable is in creating a standalone binary. Use libtool to do the linking and add the -all-static flag.
