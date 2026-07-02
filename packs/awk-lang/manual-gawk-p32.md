---
title: "The GNU Awk User’s Guide (part 32/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 32/38
---

## Appendix C Implementation Notes

This appendix contains information mainly of interest to implementers and maintainers of `gawk`. Everything in it applies specifically to `gawk` and not to other implementations.

### C.1 Downward Compatibility and Debugging

See Extensions in `gawk` Not in POSIX `awk`, for a summary of the GNU extensions to the `awk` language and program. All of these features can be turned off by invoking `gawk` with the --traditional option or with the --posix option.

If `gawk` is compiled for debugging with ‘-DDEBUG’, then there is one more option available on the command line:

**`-Y`**

**`--parsedebug`**

Print out the parse stack information as the program is being parsed.

This option is intended only for serious `gawk` developers and not for the casual user. It probably has not even been compiled into your version of `gawk`, since it slows down execution.

### C.2 Making Additions to `gawk`

If you find that you want to enhance `gawk` in a significant fashion, you are perfectly free to do so. That is the point of having free software; the source code is available and you are free to change it as you want (see GNU General Public License).

This section discusses the ways you might want to change `gawk` as well as any considerations you should bear in mind.

#### C.2.1 Accessing The `gawk` Git Repository

As `gawk` is Free Software, the source code is always available. The `gawk` Distribution describes how to get and build the formal, released versions of `gawk`.

However, if you want to modify `gawk` and contribute back your changes, you will probably wish to work with the development version. To do so, you will need to access the `gawk` source code repository. The code is maintained using the Git distributed version control system. You will need to install it if your system doesn’t have it. Once you have done so, use the command:

```
git clone git://git.savannah.gnu.org/gawk.git
```

This clones the `gawk` repository. If you are behind a firewall that does not allow you to use the Git native protocol, you can still access the repository using:

```
git clone https://git.savannah.gnu.org/git/gawk.git
```

(Using the `https` URL is considered to be more secure.)

Once you have made changes, you can use ‘git diff’ to produce a patch, and send that to the `gawk` maintainer; see Reporting Problems and Bugs, for how to do that.

Once upon a time there was Git–CVS gateway for use by people who could not install Git. However, this gateway no longer works, so you may have better luck using a more modern version control system like Bazaar, that has a Git plug-in for working with Git repositories.

#### C.2.2 Adding New Features

You are free to add any new features you like to `gawk`. However, if you want your changes to be incorporated into the `gawk` distribution, there are several steps that you need to take in order to make it possible to include them:

1. Discuss the proposed new feature with the `gawk` maintainer. The bug list may be used for this. Even if I don’t wish to include your feature, be aware that you are still free to add it and distribute your own “fork” of `gawk`.
2. Before building the new feature into `gawk` itself, consider writing it as an extension (see Writing Extensions for `gawk`). If that’s not possible, continue with the rest of the steps in this list.
3. Be prepared to sign the appropriate paperwork. In order for the FSF to distribute your changes, you must either place those changes in the public domain and submit a signed statement to that effect, or assign the copyright in your changes to the FSF. Both of these actions are easy to do and *many* people have done so already. If you have questions, please contact me (see Reporting Problems and Bugs), or “assign at gnu dot org”.
4. Get the latest version. It is much easier for me to integrate changes if they are relative to the most recent distributed version of `gawk`, or better yet, relative to the latest code in the Git repository. If your version of `gawk` is very old, I may not be able to integrate your changes at all. (See Getting the `gawk` Distribution, for information on getting the latest version of `gawk`.)
5. Follow the *GNU Coding Standards*. This document describes how GNU software should be written. If you haven’t read it, please do so, preferably *before* starting to modify `gawk`. (The *GNU Coding Standards* are available from the GNU Project’s website. Texinfo, Info, and DVI versions are also available.)
6. Use the `gawk` coding style. The C code for `gawk` follows the instructions in the *GNU Coding Standards*, with minor exceptions. The code is formatted using the traditional “K&R” style, particularly as regards to the placement of braces and the use of TABs. In brief, the coding rules for `gawk` are as follows: **NOTE:** If I have to reformat your code to follow the coding style used in `gawk`, I may not bother to integrate your changes at all.
  - Use ANSI/ISO style (prototype) function headers when defining functions.
  - Put the name of the function at the beginning of its own line.
  - Use ‘#elif’ instead of nesting ‘#if’ inside ‘#else’.
  - Put the return type of the function, even if it is `int`, on the line above the line with the name and arguments of the function.
  - Put spaces around parentheses used in control structures (`if`, `while`, `for`, `do`, and `switch`).
  - Do not parenthesize the expression used with `return`.
  - Do not put spaces in front of parentheses used in function calls.
  - Put spaces around all C operators and after commas in function calls.
  - Do not use the comma operator to produce multiple side effects, except in `for` loop initialization and increment parts, and in macro bodies.
  - Use real TABs for indenting, not spaces.
  - Use the “K&R” brace layout style.
  - Use comparisons against `NULL` and `'\0'` in the conditions of `if`, `while`, and `for` statements, as well as in the `case`s of `switch` statements, instead of just the plain pointer or character value.
  - Do not, *under any circumstances*, use the ‘-1 == foo’ or ‘0 >= bar’ style of comparison expressions. I have known about it for decades, and I understand why some people like it. Nonetheless, I abhor it with a passion, and code that uses it will never be accepted.
  - Use `true` and `false` for `bool` values, the `NULL` symbolic constant for pointer values, and the character constant `'\0'` where appropriate, instead of `1` and `0`.
  - Provide one-line descriptive comments for each function.
  - Do not use the `alloca()` function for allocating memory off the stack. Its use causes more portability trouble than is worth the minor benefit of not having to free the storage. Instead, use `malloc()` and `free()`.
  - Do not use comparisons of the form ‘! strcmp(a, b)’ or similar. As Henry Spencer once said, “`strcmp()` is not a boolean!” Instead, use ‘strcmp(a, b) == 0’.
  - If adding new bit flag values, use explicit hexadecimal constants (`0x001`, `0x002`, `0x004`, and so on) instead of shifting one left by successive amounts (‘(1<<0)’, ‘(1<<1)’, and so on).
7. Update the documentation. Along with your new code, please supply new sections and/or chapters for this Web page. If at all possible, please use real Texinfo, instead of just supplying unformatted ASCII text (although even that is better than no documentation at all). Conventions to be followed in *GAWK: Effective AWK Programming* are provided after the ‘@bye’ at the end of the Texinfo source file. If possible, please update the `man` page as well. You will also have to sign paperwork for your documentation changes.
8. Submit changes as unified diffs. Use ‘diff -u -r -N’ to compare the original `gawk` source tree with your version. I recommend using the GNU version of `diff`, or best of all, ‘git diff’ or ‘git format-patch’. Send the output produced by `diff` to me when you submit your changes. (See Reporting Problems and Bugs, for the electronic mail information.) Using this format makes it easy for me to apply your changes to the master version of the `gawk` source code (using `patch`). If I have to apply the changes manually, using a text editor, I may not do so, particularly if there are lots of changes.
9. Include an entry for the ChangeLog file with your submission. This helps further minimize the amount of work I have to do, making it easier for me to accept patches. It is simplest if you just make this part of your diff.

Although this sounds like a lot of work, please remember that while you may write the new code, I have to maintain it and support it. If it isn’t possible for me to do that with a minimum of extra work, then I probably will not.

#### C.2.3 Porting `gawk` to a New Operating System

If you want to port `gawk` to a new operating system, there are several steps:

1. Follow the guidelines in the previous section concerning coding style, submission of diffs, and so on.
2. Be prepared to sign the appropriate paperwork. In order for the FSF to distribute your code, you must either place your code in the public domain and submit a signed statement to that effect, or assign the copyright in your code to the FSF. Both of these actions are easy to do and *many* people have done so already. If you have questions, please contact me, or “gnu at gnu dot org”.
3. When doing a port, bear in mind that your code must coexist peacefully with the rest of `gawk` and the other ports. Avoid gratuitous changes to the system-independent parts of the code. If at all possible, avoid sprinkling ‘#ifdef’s just for your port throughout the code. If the changes needed for a particular system affect too much of the code, I probably will not accept them. In such a case, you can, of course, distribute your changes on your own, as long as you comply with the GPL (see GNU General Public License).
4. A number of the files that come with `gawk` are maintained by other people. Thus, you should not change them unless it is for a very good reason; i.e., changes are not out of the question, but changes to these files are scrutinized extra carefully. These are all the files in the support directory within the `gawk` distribution. See there.
5. A number of other files are provided by the GNU Autotools (Autoconf, Automake, and GNU `gettext`). You should not change them either, unless it is for a very good reason. The files are ABOUT-NLS, INSTALL, and all the files in the build-aux directory.
6. Be willing to continue to maintain the port. Non-Unix operating systems are supported by volunteers who maintain the code needed to compile and run `gawk` on their systems. If no-one volunteers to maintain a port, it becomes unsupported and it may be necessary to remove it from the distribution.
7. Supply an appropriate gawkmisc.??? file. Each port has its own gawkmisc.??? that implements certain operating system specific functions. This is cleaner than a plethora of ‘#ifdef’s scattered throughout the code. The gawkmisc.c in the main source directory includes the appropriate gawkmisc.??? file from each subdirectory. Be sure to update it as well. Each port’s gawkmisc.??? file has a suffix reminiscent of the machine or operating system for the port—for example, pc/gawkmisc.pc and vms/gawkmisc.vms. The use of separate suffixes, instead of plain gawkmisc.c, makes it possible to move files from a port’s subdirectory into the main subdirectory, without accidentally destroying the real gawkmisc.c file. (Currently, this is only an issue for the PC operating system ports.)
8. Supply a Makefile as well as any other C source and header files that are necessary for your operating system. All your code should be in a separate subdirectory, with a name that is the same as, or reminiscent of, either your operating system or the computer system. If possible, try to structure things so that it is not necessary to move files out of the subdirectory into the main source directory. If that is not possible, then be sure to avoid using names for your files that duplicate the names of files in the main source directory.
9. Update the documentation. Please write a section (or sections) for this Web page describing the installation and compilation steps needed to compile and/or install `gawk` for your system.

Following these steps makes it much easier to integrate your changes into `gawk` and have them coexist happily with other operating systems’ code that is already there.

In the code that you supply and maintain, feel free to use a coding style and brace layout that suits your taste.

#### C.2.4 Why Generated Files Are Kept In Git

If you look at the `gawk` source in the Git repository, you will notice that it includes files that are automatically generated by GNU infrastructure tools, such as Makefile.in from Automake and even configure from Autoconf.

This is different from many Free Software projects that do not store the derived files, because that keeps the repository less cluttered, and it is easier to see the substantive changes when comparing versions and trying to understand what changed between commits.

However, there are several reasons why the `gawk` maintainer likes to have everything in the repository.

First, because it is then easy to reproduce any given version completely, without relying upon the availability of (older, likely obsolete, and maybe even impossible to find) other tools.

As an extreme example, if you ever even think about trying to compile, oh, say, the V7 `awk`, you will discover that not only do you have to bootstrap the V7 `yacc` to do so, but you also need the V7 `lex`. And the latter is pretty much impossible to bring up on a modern GNU/Linux system.122

(Or, let’s say `gawk` 1.2 required `bison` whatever-it-was in 1989 and that there was no awkgram.c file in the repository. Is there a guarantee that we could find that `bison` version? Or that *it* would build?)

If the repository has all the generated files, then it’s easy to just check them out and build. (Or *easier*, depending upon how far back we go.)

And that brings us to the second (and stronger) reason why all the files really need to be in Git. It boils down to who do you cater to—the `gawk` developer(s), or the user who just wants to check out a version and try it out?

The `gawk` maintainer wants it to be possible for any interested `awk` user in the world to just clone the repository, check out the branch of interest and build it, without their having to have the correct version(s) of the autotools.123 That is the point of the bootstrap.sh file. It touches the various other files in the right order such that

```
# The canonical incantation for building GNU software:
./bootstrap.sh && ./configure && make
```

will *just work*.

This is extremely important for the `master` and `gawk-*X*.*Y*-stable` branches.

Further, the `gawk` maintainer would argue that it’s also important for the `gawk` developers. When he tried to check out the `xgawk` branch124 to build it, he couldn’t. (No ltmain.sh file, and he had no idea how to create it, and that was not the only problem.)

He felt *extremely* frustrated. With respect to that branch, the maintainer is no different than Jane User who wants to try to build `gawk-4.1-stable` or `master` from the repository.

Thus, the maintainer thinks that it’s not just important, but critical, that for any given branch, the above incantation *just works*.

A third reason to have all the files is that without them, using ‘git bisect’ to try to find the commit that introduced a bug is exceedingly difficult. The maintainer tried to do that on another project that requires running bootstrapping scripts just to create `configure` and so on; it was really painful. When the repository is self-contained, using `git bisect` in it is very easy.

What are some of the consequences and/or actions to take?

1. We don’t mind that there are differing files in the different branches as a result of different versions of the autotools.
  1. It’s the maintainer’s job to merge them and he will deal with it.
  2. He is really good at ‘git diff x y > /tmp/diff1 ; gvim /tmp/diff1’ to remove the diffs that aren’t of interest in order to review code.
2. It would certainly help if everyone used the same versions of the GNU tools as he does, which in general are the latest released versions of Automake, Autoconf, `bison`, GNU `gettext`, and Libtool. Installing from source is quite easy. It’s how the maintainer worked for years (and still works). He had /usr/local/bin at the front of his `PATH` and just did: wget https://ftp.gnu.org/gnu/*package*/*package*-*x*.*y*.*z*.tar.gz tar -xpzvf *package*-*x*.*y*.*z*.tar.gz cd *package*-*x*.*y*.*z* ./configure && make && make check make install # as root **NOTE:** Because of the ‘https://’ URL, you may have to supply the --no-check-certificate option to `wget` to download the file.

Most of the above was originally written by the maintainer to other `gawk` developers. It raised the objection from one of the developers “… that anybody pulling down the source from Git is not an end user.”

However, this is not true. There are “power `awk` users” who can build `gawk` (using the magic incantation shown previously) but who can’t program in C. Thus, the major branches should be kept buildable all the time.

It was then suggested that there be a `cron` job to create nightly tarballs of “the source.” Here, the problem is that there are source trees, corresponding to the various branches! So, nightly tarballs aren’t the answer, especially as the repository can go for weeks without significant change being introduced.

Fortunately, the Git server can meet this need. For any given branch named *branchname*, use:

```
wget https://git.savannah.gnu.org/cgit/gawk.git/snapshot/gawk-branchname.tar.gz
```

to retrieve a snapshot of the given branch.

### C.3 Probable Future Extensions

> *AWK is a language similar to PERL, only considerably more elegant.*

—

Arnold Robbins

> *Hey!*

—

Larry Wall

The TODO file in the `master` branch of the `gawk` Git repository lists possible future enhancements. Some of these relate to the source code, and others to possible new features. Please see that file for the list. See Making Additions to `gawk`, if you are interested in tackling any of the projects listed there.

### C.4 Some Limitations of the Implementation

This following table describes limits of `gawk` on a Unix-like system (although it is variable even then). Other systems may have different limits.

| Item | Limit |
|---|---|
| Characters in a character class | 2^(number of bits per byte) |
| Length of input record in bytes | `ULONG_MAX` |
| Length of output record | Unlimited |
| Length of source line | Unlimited |
| Number of fields in a record | `ULONG_MAX` |
| Number of file redirections | Unlimited |
| Number of input records in one file | `MAX_LONG` |
| Number of input records total | `MAX_LONG` |
| Number of pipe redirections | min(number of processes per user, number of open files) |
| Numeric values | Double-precision floating point (if not using MPFR) |
| Size of a field in bytes | `ULONG_MAX` |
| Size of a literal string in bytes | `ULONG_MAX` |
| Size of a printf string in bytes | `ULONG_MAX` |

### C.5 Extension API Design

This section documents the design of the extension API, including a discussion of some of the history and problems that needed to be solved.

The first version of extensions for `gawk` was developed in the mid-1990s and released with `gawk` 3.1 in the late 1990s. The basic mechanisms and design remained unchanged for close to 15 years, until 2012.

The old extension mechanism used data types and functions from `gawk` itself, with a “clever hack” to install extension functions.

`gawk` included some sample extensions, of which a few were really useful. However, it was clear from the outset that the extension mechanism was bolted onto the side and was not really well thought out.

#### C.5.1 Problems With The Old Mechanism

The old extension mechanism had several problems:

- It depended heavily upon `gawk` internals. Any time the `NODE` structure125 changed, an extension would have to be recompiled. Furthermore, to really write extensions required understanding something about `gawk`’s internal functions. There was some documentation in this Web page, but it was quite minimal.
- Being able to call into `gawk` from an extension required linker facilities that are common on Unix-derived systems but that did not work on MS-Windows systems; users wanting extensions on MS-Windows had to statically link them into `gawk`, even though MS-Windows supports dynamic loading of shared objects.
- The API would change occasionally as `gawk` changed; no compatibility between versions was ever offered or planned for.

Despite the drawbacks, the `xgawk` project developers forked `gawk` and developed several significant extensions. They also enhanced `gawk`’s facilities relating to file inclusion and shared object access.

A new API was desired for a long time, but only in 2012 did the `gawk` maintainer and the `xgawk` developers finally start working on it together. More information about the `xgawk` project is provided in The `gawkextlib` Project.

#### C.5.2 Goals For A New Mechanism

Some goals for the new API were:

- The API should be independent of `gawk` internals. Changes in `gawk` internals should not be visible to the writer of an extension function.
- The API should provide *binary* compatibility across `gawk` releases as long as the API itself does not change.
- The API should enable extensions written in C or C++ to have roughly the same “appearance” to `awk`-level code as `awk` functions do. This means that extensions should have:
  - The ability to access function parameters.
  - The ability to turn an undefined parameter into an array (call by reference).
  - The ability to create, access and update global variables.
  - Easy access to all the elements of an array at once (“array flattening”) in order to loop over all the element in an easy fashion for C code.
  - The ability to create arrays (including `gawk`’s true arrays of arrays).

Some additional important goals were:

- The API should use only features in ISO C 90, so that extensions can be written using the widest range of C and C++ compilers. The header should include the appropriate ‘#ifdef __cplusplus’ and ‘extern "C"’ magic so that a C++ compiler could be used. (If using C++, the runtime system has to be smart enough to call any constructors and destructors, as `gawk` is a C program. As of this writing, this has not been tested.)
- The API mechanism should not require access to `gawk`’s symbols126 by the compile-time or dynamic linker, in order to enable creation of extensions that also work on MS-Windows.

During development, it became clear that there were other features that should be available to extensions, which were also subsequently provided:

- Extensions should have the ability to hook into `gawk`’s I/O redirection mechanism. In particular, the `xgawk` developers provided a so-called “open hook” to take over reading records. During development, this was generalized to allow extensions to hook into input processing, output processing, and two-way I/O.
- An extension should be able to provide a “call back” function to perform cleanup actions when `gawk` exits.
- An extension should be able to provide a version string so that `gawk`’s --version option can provide information about extensions as well.

The requirement to avoid access to `gawk`’s symbols is, at first glance, a difficult one to meet.

One design, apparently used by Perl and Ruby and maybe others, would be to make the mainline `gawk` code into a library, with the `gawk` utility a small C `main()` function linked against the library.

This seemed like the tail wagging the dog, complicating build and installation and making a simple copy of the `gawk` executable from one system to another (or one place to another on the same system!) into a chancy operation.

Pat Rankin suggested the solution that was adopted. See How It Works at a High Level, for the details.

#### C.5.3 Other Design Decisions

As an arbitrary design decision, extensions can read the values of predefined variables and arrays (such as `ARGV` and `FS`), but cannot change them, with the exception of `PROCINFO`.

The reason for this is to prevent an extension function from affecting the flow of an `awk` program outside its control. While a real `awk` function can do what it likes, that is at the discretion of the programmer. An extension function should provide a service or make a C API available for use within `awk`, and not mess with `FS` or `ARGC` and `ARGV`.

In addition, it becomes easy to start down a slippery slope. How much access to `gawk` facilities do extensions need? Do they need `getline`? What about calling `gsub()` or compiling regular expressions? What about calling into `awk` functions? (*That* would be messy.)

In order to avoid these issues, the `gawk` developers chose to start with the simplest, most basic features that are still truly useful.

Another decision is that although `gawk` provides nice things like MPFR, and arrays indexed internally by integers, these features are not being brought out to the API in order to keep things simple and close to traditional `awk` semantics. (In fact, arrays indexed internally by integers are so transparent that they aren’t even documented!)

Additionally, all functions in the API check that their pointer input parameters are not `NULL`. If they are, they return an error. (It is a good idea for extension code to verify that pointers received from `gawk` are not `NULL`. Such a thing should not happen, but the `gawk` developers are only human, and they have been known to occasionally make mistakes.)

With time, the API will undoubtedly evolve; the `gawk` developers expect this to be driven by user needs. For now, the current API seems to provide a minimal yet powerful set of features for creating extensions.

#### C.5.4 Room For Future Growth

The API can later be expanded, in at least the following way:

- `gawk` passes an “extension id” into the extension when it first loads the extension. The extension then passes this id back to `gawk` with each function call. This mechanism allows `gawk` to identify the extension calling into it, should it need to know.

Of course, as of this writing, no decisions have been made with respect to the above.

### C.6 Summary

- `gawk`’s extensions can be disabled with either the --traditional option or with the --posix option. The --parsedebug option is available if `gawk` is compiled with ‘-DDEBUG’.
- The source code for `gawk` is maintained in a publicly accessible Git repository. Anyone may check it out and view the source.
- Contributions to `gawk` are welcome. Following the steps outlined in this chapter will make it easier to integrate your contributions into the code base. This applies both to new feature contributions and to ports to additional operating systems.
- `gawk` has some limits—generally those that are imposed by the machine architecture.
- The extension API design was intended to solve a number of problems with the previous extension mechanism, enable features needed by the `xgawk` project, and provide binary compatibility going forward.
- The previous extension mechanism is no longer supported and was removed from the code base with the 4.2 release.


## Appendix D Basic Programming Concepts

This appendix attempts to define some of the basic concepts and terms that are used throughout the rest of this Web page. As this Web page is specifically about `awk`, and not about computer programming in general, the coverage here is by necessity fairly cursory and simplistic. (If you need more background, there are many other introductory texts that you should refer to instead.)

### D.1 What a Program Does

At the most basic level, the job of a program is to process some input data and produce results. See Figure D.1.

**Figure D.1:**General Program Flow

The “program” in the figure can be either a compiled program127 (such as `ls`), or it may be *interpreted*. In the latter case, a machine-executable program such as `awk` reads your program, and then uses the instructions in your program to process the data.

When you write a program, it usually consists of the following, very basic set of steps, as shown in Figure D.2:

**Figure D.2:**Basic Program Steps

**Initialization**

These are the things you do before actually starting to process data, such as checking arguments, initializing any data you need to work with, and so on. This step corresponds to `awk`’s `BEGIN` rule (see The `BEGIN` and `END` Special Patterns).

If you were baking a cake, this might consist of laying out all the mixing bowls and the baking pan, and making sure you have all the ingredients that you need.

**Processing**

This is where the actual work is done. Your program reads data, one logical chunk at a time, and processes it as appropriate.

In most programming languages, you have to manually manage the reading of data, checking to see if there is more each time you read a chunk. `awk`’s pattern-action paradigm (see Getting Started with `awk`) handles the mechanics of this for you.

In baking a cake, the processing corresponds to the actual labor: breaking eggs, mixing the flour, water, and other ingredients, and then putting the cake into the oven.

**Clean Up**

Once you’ve processed all the data, you may have things you need to do before exiting. This step corresponds to `awk`’s `END` rule (see The `BEGIN` and `END` Special Patterns).

After the cake comes out of the oven, you still have to wrap it in plastic wrap to keep anyone from tasting it, as well as wash the mixing bowls and utensils.

An *algorithm* is a detailed set of instructions necessary to accomplish a task, or process data. It is much the same as a recipe for baking a cake. Programs implement algorithms. Often, it is up to you to design the algorithm and implement it, simultaneously.

The “logical chunks” we talked about previously are called *records*, similar to the records a company keeps on employees, a school keeps for students, or a doctor keeps for patients. Each record has many component parts, such as first and last names, date of birth, address, and so on. The component parts are referred to as the *fields* of the record.

The act of reading data is termed *input*, and that of generating results, not too surprisingly, is termed *output*. They are often referred to together as “input/output,” and even more often, as “I/O” for short. (You will also see “input” and “output” used as verbs.)

`awk` manages the reading of data for you, as well as the breaking it up into records and fields. Your program’s job is to tell `awk` what to do with the data. You do this by describing *patterns* in the data to look for, and *actions* to execute when those patterns are seen. This *data-driven* nature of `awk` programs usually makes them both easier to write and easier to read.

### D.2 Data Values in a Computer

In a program, you keep track of information and values in things called *variables*. A variable is just a name for a given value, such as `first_name`, `last_name`, `address`, and so on. `awk` has several predefined variables, and it has special names to refer to the current input record and the fields of the record. You may also group multiple associated values under one name, as an array.

Data, particularly in `awk`, consists of either numeric values, such as 42 or 3.1415927, or string values. String values are essentially anything that’s not a number, such as a name. Strings are sometimes referred to as *character data*, since they store the individual characters that comprise them. Individual variables, as well as numeric and string variables, are referred to as *scalar* values. Groups of values, such as arrays, are not scalars.

A General Description of Computer Arithmetic, provided a basic introduction to numeric types (integer and floating-point) and how they are used in a computer. Please review that information, including a number of caveats that were presented.

While you are probably used to the idea of a number without a value (i.e., zero), it takes a bit more getting used to the idea of zero-length character data. Nevertheless, such a thing exists. It is called the *null string*. The null string is character data that has no value. In other words, it is empty. It is written in `awk` programs like this: `""`.

Humans are used to working in decimal; i.e., base 10. In base 10, numbers go from 0 to 9, and then “roll over” into the next column. (Remember grade school? 42 = 4 x 10 + 2.)

There are other number bases though. Computers commonly use base 2 or *binary*, base 8 or *octal*, and base 16 or *hexadecimal*. In binary, each column represents two times the value in the column to its right. Each column may contain either a 0 or a 1. Thus, binary 1010 represents (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1), or decimal 10. Octal and hexadecimal are discussed more in Octal and Hexadecimal Numbers.

At the very lowest level, computers store values as groups of binary digits, or *bits*. Modern computers group bits into groups of eight, called *bytes*. Advanced applications sometimes have to manipulate bits directly, and `gawk` provides functions for doing so.

Programs are written in programming languages. Hundreds, if not thousands, of programming languages exist. One of the most popular is the C programming language. The C language had a very strong influence on the design of the `awk` language.

There have been several versions of C. The first is often referred to as “K&R” C, after the initials of Brian Kernighan and Dennis Ritchie, the authors of the first book on C. (Dennis Ritchie created the language, and Brian Kernighan was one of the creators of `awk`.)

In the mid-1980s, an effort began to produce an international standard for C. This work culminated in 1989, with the production of the ANSI standard for C. This standard became an ISO standard in 1990. In 1999, a revised ISO C standard was approved and released. Where it makes sense, POSIX `awk` is compatible with 1999 ISO C.
