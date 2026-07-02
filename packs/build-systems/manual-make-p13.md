---
title: "GNU make (part 13/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 13/17
---

## 12 Extending GNU `make`

GNU `make` provides many advanced capabilities, including many useful functions. However, it does not contain a complete programming language and so it has limitations. Sometimes these limitations can be overcome through use of the `shell` function to invoke a separate program, although this can be inefficient.

In cases where the built-in capabilities of GNU `make` are insufficient to your requirements there are two options for extending `make`. On systems where it’s provided, you can utilize GNU Guile as an embedded scripting language (see GNU Guile Integration). On systems which support dynamically loadable objects, you can write your own extension in any language (which can be compiled into such an object) and load it to provide extended capabilities (see The `load` Directive).

Next: Loading Dynamic Objects, Previous: Extending GNU `make`, Up: Extending GNU `make`   [Contents][Index]

### 12.1 GNU Guile Integration

GNU `make` may be built with support for GNU Guile as an embedded extension language. Guile implements the Scheme language. A review of GNU Guile and the Scheme language and its features is beyond the scope of this manual: see the documentation for GNU Guile and Scheme.

You can determine if `make` contains support for Guile by examining the `.FEATURES` variable; it will contain the word *guile* if Guile support is available.

The Guile integration provides one new `make` function: `guile`. The `guile` function takes one argument which is first expanded by `make` in the normal fashion, then passed to the GNU Guile evaluator. The result of the evaluator is converted into a string and used as the expansion of the `guile` function in the makefile.

In addition, GNU `make` exposes Guile procedures for use in Guile scripts.

Next: Interfaces from Guile to `make`, Previous: GNU Guile Integration, Up: GNU Guile Integration   [Contents][Index]

#### 12.1.1 Conversion of Guile Types

There is only one “data type” in `make`: a string. GNU Guile, on the other hand, provides a rich variety of different data types. An important aspect of the interface between `make` and GNU Guile is the conversion of Guile data types into `make` strings.

This conversion is relevant in two places: when a makefile invokes the `guile` function to evaluate a Guile expression, the result of that evaluation must be converted into a make string so it can be further evaluated by `make`. And secondly, when a Guile script invokes one of the procedures exported by `make` the argument provided to the procedure must be converted into a string.

The conversion of Guile types into `make` strings is as below:

**`#f`**

False is converted into the empty string: in `make` conditionals the empty string is considered false.

**`#t`**

True is converted to the string ‘#t’: in `make` conditionals any non-empty string is considered true.

**`symbol`**

**`number`**

A symbol or number is converted into the string representation of that symbol or number.

**`character`**

A printable character is converted to the same character.

**`string`**

A string containing only printable characters is converted to the same string.

**`list`**

A list is converted recursively according to the above rules. This implies that any structured list will be flattened (that is, a result of ‘'(a b (c d) e)’ will be converted to the `make` string ‘a b c d e’).

**`other`**

Any other Guile type results in an error. In future versions of `make`, other Guile types may be converted.

The translation of ‘#f’ (to the empty string) and ‘#t’ (to the non-empty string ‘#t’) is designed to allow you to use Guile boolean results directly as `make` boolean conditions. For example:

```
$(if $(guile (access? "myfile" R_OK)),$(info myfile exists))
```

As a consequence of these conversion rules you must consider the result of your Guile script, as that result will be converted into a string and parsed by `make`. If there is no natural result for the script (that is, the script exists solely for its side-effects), you should add ‘#f’ as the final expression in order to avoid syntax errors in your makefile.

Next: Example Using Guile in `make`, Previous: Conversion of Guile Types, Up: GNU Guile Integration   [Contents][Index]

#### 12.1.2 Interfaces from Guile to `make`

In addition to the `guile` function available in makefiles, `make` exposes some procedures for use in your Guile scripts. At startup `make` creates a new Guile module, `gnu make`, and exports these procedures as public interfaces from that module:

**`gmk-expand` ¶**

This procedure takes a single argument which is converted into a string. The string is expanded by `make` using normal `make` expansion rules. The result of the expansion is converted into a Guile string and provided as the result of the procedure.

**`gmk-eval` ¶**

This procedure takes a single argument which is converted into a string. The string is evaluated by `make` as if it were a makefile. This is the same capability available via the `eval` function (see The `eval` Function). The result of the `gmk-eval` procedure is always the empty string.

Note that `gmk-eval` is not quite the same as using `gmk-expand` with the `eval` function: in the latter case the evaluated string will be expanded *twice*; first by `gmk-expand`, then again by the `eval` function.

Previous: Interfaces from Guile to `make`, Up: GNU Guile Integration   [Contents][Index]

#### 12.1.3 Example Using Guile in `make`

Here is a very simple example using GNU Guile to manage writing to a file. These Guile procedures simply open a file, allow writing to the file (one string per line), and close the file. Note that because we cannot store complex values such as Guile ports in `make` variables, we’ll keep the port as a global variable in the Guile interpreter.

You can create Guile functions easily using `define`/`endef` to create a Guile script, then use the `guile` function to internalize it:

```
define GUILEIO
;; A simple Guile IO library for GNU Make

(define MKPORT #f)

(define (mkopen name mode)
  (set! MKPORT (open-file name mode))
  #f)

(define (mkwrite s)
  (display s MKPORT)
  (newline MKPORT)
  #f)

(define (mkclose)
  (close-port MKPORT)
  #f)

#f
endef

# Internalize the Guile IO functions
$(guile $(GUILEIO))
```

If you have a significant amount of Guile support code, you might consider keeping it in a different file (e.g., guileio.scm) and then loading it in your makefile using the `guile` function:

```
$(guile (load "guileio.scm"))
```

An advantage to this method is that when editing guileio.scm, your editor will understand that this file contains Scheme syntax rather than makefile syntax.

Now you can use these Guile functions to create files. Suppose you need to operate on a very large list, which cannot fit on the command line, but the utility you’re using accepts the list as input as well:

```
prog: $(PREREQS)
        @$(guile (mkopen "tmp.out" "w")) \
         $(foreach X,$^,$(guile (mkwrite "$(X)"))) \
         $(guile (mkclose))
        $(LINK) < tmp.out
```

A more comprehensive suite of file manipulation procedures is possible of course. You could, for example, maintain multiple output files at the same time by choosing a symbol for each one and using it as the key to a hash table, where the value is a port, then returning the symbol to be stored in a `make` variable.

Previous: GNU Guile Integration, Up: Extending GNU `make`   [Contents][Index]

### 12.2 Loading Dynamic Objects

| **Warning:** The `load` directive and extension capability is considered a “technology preview” in this release of GNU Make. We encourage you to experiment with this feature and we appreciate any feedback on it. However we cannot guarantee to maintain backward-compatibility in the next release. Consider using GNU Guile instead for extending GNU Make (see The `guile` Function). |
|---|

Many operating systems provide a facility for dynamically loading compiled objects. If your system provides this facility, GNU `make` can make use of it to load dynamic objects at runtime, providing new capabilities which may then be invoked by your makefile.

The `load` directive is used to load a dynamic object. Once the object is loaded, a “setup” function will be invoked to allow the object to initialize itself and register new facilities with GNU `make`. A dynamic object might include new `make` functions, for example, and the “setup” function would register them with GNU `make`’s function handling system.

Next: How Loaded Objects Are Remade, Previous: Loading Dynamic Objects, Up: Loading Dynamic Objects   [Contents][Index]

#### 12.2.1 The `load` Directive

Objects are loaded into GNU `make` by placing the `load` directive into your makefile. The syntax of the `load` directive is as follows:

```
load object-file …
```

or:

```
load object-file(symbol-name) …
```

The file *object-file* is dynamically loaded by GNU `make`. If *object-file* does not include a directory path then it is first looked for in the current directory. If it is not found there, or a directory path is included, then system-specific paths will be searched. If the load fails for any reason, `make` will print a message and exit.

If the load succeeds `make` will invoke an initializing function.

If *symbol-name* is provided, it will be used as the name of the initializing function.

If no *symbol-name* is provided, the initializing function name is created by taking the base file name of *object-file*, up to the first character which is not a valid symbol name character (alphanumerics and underscores are valid symbol name characters). To this prefix will be appended the suffix `_gmk_setup`.

More than one object file may be loaded with a single `load` directive, and both forms of `load` arguments may be used in the same directive.

The initializing function will be provided the file name and line number of the invocation of the `load` operation. It should return a value of type `int`, which must be `0` on failure and non-`0` on success. If the return value is `-1`, then GNU Make will *not* attempt to rebuild the object file (see How Loaded Objects Are Remade).

For example:

```
load ../mk_funcs.so
```

will load the dynamic object ../mk_funcs.so. After the object is loaded, `make` will invoke the function (assumed to be defined by the shared object) `mk_funcs_gmk_setup`.

On the other hand:

```
load ../mk_funcs.so(init_mk_func)
```

will load the dynamic object ../mk_funcs.so. After the object is loaded, `make` will invoke the function `init_mk_func`.

Regardless of how many times an object file appears in a `load` directive, it will only be loaded (and its setup function will only be invoked) once.

After an object has been successfully loaded, its file name is appended to the `.LOADED` variable.

If you would prefer that failure to load a dynamic object not be reported as an error, you can use the `-load` directive instead of `load`. GNU `make` will not fail and no message will be generated if an object fails to load. The failed object is not added to the `.LOADED` variable, which can then be consulted to determine if the load was successful.

Next: Loaded Object Interface, Previous: The `load` Directive, Up: Loading Dynamic Objects   [Contents][Index]

#### 12.2.2 How Loaded Objects Are Remade

Loaded objects undergo the same re-make procedure as makefiles (see How Makefiles Are Remade). If any loaded object is recreated, then `make` will start from scratch and re-read all the makefiles, and reload the object files again. It is not necessary for the loaded object to do anything special to support this.

It’s up to the makefile author to provide the rules needed for rebuilding the loaded object.

Next: Example Loaded Object, Previous: How Loaded Objects Are Remade, Up: Loading Dynamic Objects   [Contents][Index]

#### 12.2.3 Loaded Object Interface

| **Warning:** For this feature to be useful your extensions will need to invoke various functions internal to GNU `make`. The programming interfaces provided in this release should not be considered stable: functions may be added, removed, or change calling signatures or implementations in future versions of GNU `make`. |
|---|

To be useful, loaded objects must be able to interact with GNU `make`. This interaction includes both interfaces the loaded object provides to makefiles and also interfaces `make` provides to the loaded object to manipulate `make`’s operation.

The interface between loaded objects and `make` is defined by the gnumake.h C header file. All loaded objects written in C should include this header file. Any loaded object not written in C will need to implement the interface defined in this header file.

Typically, a loaded object will register one or more new GNU `make` functions using the `gmk_add_function` routine from within its setup function. The implementations of these `make` functions may make use of the `gmk_expand` and `gmk_eval` routines to perform their tasks, then optionally return a string as the result of the function expansion.

#### Loaded Object Licensing

Every dynamic extension should define the global symbol `plugin_is_GPL_compatible` to assert that it has been licensed under a GPL-compatible license. If this symbol does not exist, `make` emits a fatal error and exits when it tries to load your extension.

The declared type of the symbol should be `int`. It does not need to be in any allocated section, though. The code merely asserts that the symbol exists in the global scope. Something like this is enough:

```
int plugin_is_GPL_compatible;
```

#### Data Structures

**`gmk_floc`**

This structure represents a filename/location pair. It is provided when defining items, so GNU `make` can inform the user later where the definition occurred if necessary.

#### Registering Functions

There is currently one way for makefiles to invoke operations provided by the loaded object: through the `make` function call interface. A loaded object can register one or more new functions which may then be invoked from within the makefile in the same way as any other function.

Use `gmk_add_function` to create a new `make` function. Its arguments are as follows:

**`name`**

The function name. This is what the makefile should use to invoke the function. The name must be between 1 and 255 characters long and it may only contain alphanumeric, period (‘.’), dash (‘-’), and underscore (‘_’) characters. It may not begin with a period.

**`func_ptr`**

A pointer to a function that `make` will invoke when it expands the function in a makefile. This function must be defined by the loaded object.

**`min_args`**

The minimum number of arguments the function will accept. Must be between 0 and 255. GNU `make` will check this and fail before invoking `func_ptr` if the function was invoked with too few arguments.

**`max_args`**

The maximum number of arguments the function will accept. Must be between 0 and 255. GNU `make` will check this and fail before invoking `func_ptr` if the function was invoked with too many arguments. If the value is 0, then any number of arguments is accepted. If the value is greater than 0, then it must be greater than or equal to `min_args`.

**`flags`**

Flags that specify how this function will operate; the desired flags should be OR’d together. If the `GMK_FUNC_NOEXPAND` flag is given then the function arguments will not be expanded before the function is called; otherwise they will be expanded first.

#### Registered Function Interface

A function registered with `make` must match the `gmk_func_ptr` type. It will be invoked with three parameters: `name` (the name of the function), `argc` (the number of arguments to the function), and `argv` (an array of pointers to arguments to the function). The last pointer (that is, `argv[argc]`) will be null (`0`).

The return value of the function is the result of expanding the function. If the function expands to nothing the return value may be null. Otherwise, it must be a pointer to a string created with `gmk_alloc`. Once the function returns, `make` owns this string and will free it when appropriate; it cannot be accessed by the loaded object.

#### GNU `make` Facilities

There are some facilities exported by GNU `make` for use by loaded objects. Typically these would be run from within the setup function and/or the functions registered via `gmk_add_function`, to retrieve or modify the data `make` works with.

**`gmk_expand` ¶**

This function takes a string and expands it using `make` expansion rules. The result of the expansion is returned in a nil-terminated string buffer. The caller is responsible for calling `gmk_free` with a pointer to the returned buffer when done.

**`gmk_eval` ¶**

This function takes a buffer and evaluates it as a segment of makefile syntax. This function can be used to define new variables, new rules, etc. It is equivalent to using the `eval` `make` function.

Note that there is a difference between `gmk_eval` and calling `gmk_expand` with a string using the `eval` function: in the latter case the string will be expanded *twice*; once by `gmk_expand` and then again by the `eval` function. Using `gmk_eval` the buffer is only expanded once, at most (as it’s read by the `make` parser).

#### Memory Management

Some systems allow for different memory management schemes. Thus you should never pass memory that you’ve allocated directly to any `make` function, nor should you attempt to directly free any memory returned to you by any `make` function. Instead, use the `gmk_alloc` and `gmk_free` functions.

In particular, the string returned to `make` by a function registered using `gmk_add_function` *must* be allocated using `gmk_alloc`, and the string returned from the `make` `gmk_expand` function *must* be freed (when no longer needed) using `gmk_free`.

**`gmk_alloc` ¶**

Return a pointer to a newly-allocated buffer. This function will always return a valid pointer; if not enough memory is available `make` will exit. `gmk_alloc` does not initialize allocated memory.

**`gmk_free` ¶**

Free a buffer returned to you by `make`. Once the `gmk_free` function returns the string will no longer be valid. If NULL is passed to `gmk_free`, no operation is performed.

Previous: Loaded Object Interface, Up: Loading Dynamic Objects   [Contents][Index]

#### 12.2.4 Example Loaded Object

Let’s suppose we wanted to write a new GNU `make` function that would create a temporary file and return its name. We would like our function to take a prefix as an argument. First we can write the function in a file mk_temp.c:

```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#include <gnumake.h>

int plugin_is_GPL_compatible;

char *
gen_tmpfile(const char *nm, int argc, char **argv)
{
  int fd;

  /* Compute the size of the filename and allocate space for it.  */
  int len = strlen (argv[0]) + 6 + 1;
  char *buf = gmk_alloc (len);

  strcpy (buf, argv[0]);
  strcat (buf, "XXXXXX");

  fd = mkstemp(buf);
  if (fd >= 0)
    {
      /* Don't leak the file descriptor.  */
      close (fd);
      return buf;
    }

  /* Failure.  */
  fprintf (stderr, "mkstemp(%s) failed: %s\n", buf, strerror (errno));
  gmk_free (buf);
  return NULL;
}

int
mk_temp_gmk_setup (const gmk_floc *floc)
{
  printf ("mk_temp plugin loaded from %s:%lu\n", floc->filenm, floc->lineno);
  /* Register the function with make name "mk-temp".  */
  gmk_add_function ("mk-temp", gen_tmpfile, 1, 1, 1);
  return 1;
}
```

Next, we will write a Makefile that can build this shared object, load it, and use it:

```
all:
        @echo Temporary file: $(mk-temp tmpfile.)

load mk_temp.so

mk_temp.so: mk_temp.c
        $(CC) -shared -fPIC -o $@ $<
```

On MS-Windows, due to peculiarities of how shared objects are produced, the compiler needs to scan the *import library* produced when building `make`, typically called libgnumake-*version*.dll.a, where *version* is the version of the load object API. So the recipe to produce a shared object will look on Windows like this (assuming the API version is 1):

```
mk_temp.dll: mk_temp.c
        $(CC) -shared -o $@ $< -lgnumake-1
```

Now when you run `make` you’ll see something like:

```
$ make
mk_temp plugin loaded from Makefile:4
cc -shared -fPIC -o mk_temp.so mk_temp.c
Temporary filename: tmpfile.A7JEwd
```

Next: Features of GNU `make`, Previous: Extending GNU `make`, Up: GNU `make`   [Contents][Index]


## 13 Integrating GNU `make`

GNU `make` is often one component in a larger system of tools, including integrated development environments, compiler toolchains, and others. The role of `make` is to start commands and determine whether they succeeded or not: no special integration is needed to accomplish that. However, sometimes it is convenient to bind `make` more tightly with other parts of the system, both higher-level (tools that invoke `make`) and lower-level (tools that `make` invokes).

Next: Synchronized Terminal Output, Previous: Integrating GNU `make`, Up: Integrating GNU `make`   [Contents][Index]

### 13.1 Sharing Job Slots with GNU `make`

GNU `make` has the ability to run multiple recipes in parallel (see Parallel Execution) and to cap the total number of parallel jobs even across recursive invocations of `make` (see Communicating Options to a Sub-`make`). Tools that `make` invokes which are also able to run multiple operations in parallel, either using multiple threads or multiple processes, can be enhanced to participate in GNU `make`’s job management facility to ensure that the total number of active threads/processes running on the system does not exceed the maximum number of slots provided to GNU `make`.

GNU `make` uses a method called the “jobserver” to control the number of active jobs across recursive invocations. The actual implementation of the jobserver varies across different operating systems, but some fundamental aspects are always true.

First, `make` will provide information necessary for accessing the jobserver through the environment to its children, in the `MAKEFLAGS` environment variable. Tools which want to participate in the jobserver protocol will need to parse this environment variable and find the word starting with `--jobserver-auth=`. The value of this option will describe how to communicate with the jobserver. The interpretation of this value is described in the sections below.

Be aware that the `MAKEFLAGS` variable may contain multiple instances of the `--jobserver-auth=` option. Only the *last* instance is relevant.

Second, every command `make` starts has one implicit job slot reserved for it before it starts. Any tool which wants to participate in the jobserver protocol should assume it can always run one job without having to contact the jobserver at all.

Finally, it’s critical that tools that participate in the jobserver protocol return the exact number of slots they obtained from the jobserver back to the jobserver before they exit, even under error conditions. Remember that the implicit job slot should **not** be returned to the jobserver! Returning too few slots means that those slots will be lost for the rest of the build process; returning too many slots means that extra slots will be available. The top-level `make` command will print an error message at the end of the build if it detects an incorrect number of slots available in the jobserver.

As an example, suppose you are implementing a linker which provides for multithreaded operation. You would like to enhance the linker so that if it is invoked by GNU `make` it can participate in the jobserver protocol to control how many threads are used during link. First you will need to modify the linker to determine if the `MAKEFLAGS` environment variable is set. Next you will need to parse the value of that variable to determine if the jobserver is available, and how to access it. If it is available then you can access it to obtain job slots controlling how much parallelism your tool can use. Once done your tool must return those job slots back to the jobserver.

Next: Windows Jobserver Interaction, Previous: Sharing Job Slots with GNU `make`, Up: Sharing Job Slots with GNU `make`   [Contents][Index]

#### 13.1.1 POSIX Jobserver Interaction

On POSIX systems the jobserver is implemented in one of two ways: on systems that support it, GNU `make` will create a named pipe and use that for the jobserver. In this case the auth option will have the form `--jobserver-auth=fifo:PATH` where ‘PATH’ is the pathname of the named pipe. To access the jobserver you should open the named pipe path and read/write to it as described below.

If the system doesn’t support named pipes, or if the user provided the `--jobserver-style` option and specified ‘pipe’, then the jobserver will be implemented as a simple UNIX pipe. In this case the auth option will have the form `--jobserver-auth=R,W` where ‘R’ and ‘W’ are non-negative integers representing file descriptors: ‘R’ is the read file descriptor and ‘W’ is the write file descriptor. If either or both of these file descriptors are negative, it means the jobserver is disabled for this process.

When using a simple pipe, only command lines that `make` understands to be recursive invocations of `make` (see How the `MAKE` Variable Works) will have access to the jobserver. When writing makefiles you must be sure to mark the command as recursive (most commonly by prefixing the command line with the `+` indicator (see Recursive Use of `make`). Note that the read side of the jobserver pipe is set to “blocking” mode. This should not be changed.

In both implementations of the jobserver, the pipe will be pre-loaded with one single-character token for each available job. To obtain an extra slot you must read a single character from the jobserver; to release a slot you must write a single character back into the jobserver.

It’s important that when you release the job slot, you write back the same character you read. Don’t assume that all tokens are the same character; different characters may have different meanings to GNU `make`. The order is not important, since `make` has no idea in what order jobs will complete anyway.

There are various error conditions you must consider to ensure your implementation is robust:

- If you have a command-line argument controlling the parallel operation of your tool, consider whether your tool should detect situations where both the jobserver and the command-line argument are specified, and how it should react.
- If your tool does not recognize the format of the `--jobserver-auth` string, it should assume the jobserver is using a different style and it cannot connect.
- If your tool determines that the `--jobserver-auth` option references a simple pipe but that the file descriptors specified are closed, this means that the calling `make` process did not think that your tool was a recursive `make` invocation (e.g., the command line was not prefixed with a `+` character). You should notify your users of this situation.
- Your tool should be sure to write back the tokens it read, even under error conditions. This includes not only errors in your tool but also outside influences such as interrupts (`SIGINT`), etc. You may want to install signal handlers to manage this write-back.
- Your tool may also examine the first word of the `MAKEFLAGS` variable and look for the character `n`. If this character is present then `make` was invoked with the ‘-n’ option and your tool may want to stop without performing any operations.

Previous: POSIX Jobserver Interaction, Up: Sharing Job Slots with GNU `make`   [Contents][Index]

#### 13.1.2 Windows Jobserver Interaction

On Windows systems the jobserver is implemented as a named semaphore. The semaphore will be set with an initial count equal to the number of available slots; to obtain a slot you must wait on the semaphore (with or without a timeout). To release a slot, release the semaphore.

To access the semaphore you must parse the `MAKEFLAGS` variable and look for the argument string `--jobserver-auth=NAME` where ‘NAME’ is the name of the named semaphore. Use this name with `OpenSemaphore` to create a handle to the semaphore.

The only valid style for `--jobserver-style` is ‘sem’.

There are various error conditions you must consider to ensure your implementation is robust:

- Usually you will have a command-line argument controlling the parallel operation of your tool. Consider whether your tool should detect situations where both the jobserver and the command-line argument are specified, and how it should react.
- Your tool should be sure to release the semaphore for the tokens it read, even under error conditions. This includes not only errors in your tool but also outside influences such as interrupts (`SIGINT`), etc. You may want to install signal handlers to manage this write-back.

Previous: Sharing Job Slots with GNU `make`, Up: Integrating GNU `make`   [Contents][Index]

### 13.2 Synchronized Terminal Output

Normally GNU `make` will invoke all commands with access to the same standard and error outputs that `make` itself was started with. A number of tools will detect whether the output is a terminal or not-a-terminal, and use this information to change the output style. For example if the output goes to a terminal the tool may add control characters that set color, or even change the location of the cursor. If the output is not going to a terminal then these special control characters are not emitted so that they don’t corrupt log files, etc.

The `--output-sync` (see Output During Parallel Execution) option will defeat the terminal detection. When output synchronization is enabled GNU `make` arranges for all command output to be written to a file, so that its output can be written as a block without interference from other commands. This means that all tools invoked by `make` will believe that their output is not going to be displayed on a terminal, even when it will be (because `make` will display it there after the command is completed).

In order to facilitate tools which would like to determine whether or not their output will be displayed on a terminal, GNU `make` will set the `MAKE_TERMOUT` and `MAKE_TERMERR` environment variables before invoking any commands. Tools which would like to determine whether standard or error output (respectively) will be displayed on a terminal can check these environment variables to determine if they exist and contain a non-empty value. If so the tool can assume that the output will (eventually) be displayed on a terminal. If the variables are not set or have an empty value, then the tool should fall back to its normal methods of detecting whether output is going to a terminal or not.

The content of the variables can be parsed to determine the type of terminal which will be used to display the output.

Similarly, environments which invoke `make` and would like to capture the output and eventually display it on a terminal (or some display which can interpret terminal control characters) can set these variables before invoking `make`. GNU `make` will not modify these environment variables if they already exist when it starts.

Next: Incompatibilities and Missing Features, Previous: Integrating GNU `make`, Up: GNU `make`   [Contents][Index]


## 14 Features of GNU `make`

Here is a summary of the features of GNU `make`, for comparison with and credit to other versions of `make`. We consider the features of `make` in 4.2 BSD systems as a baseline. If you are concerned with writing portable makefiles, you should not use the features of `make` listed here, nor the ones in Incompatibilities and Missing Features.

Many features come from the version of `make` in System V.

- The `VPATH` variable and its special meaning. See Searching Directories for Prerequisites. This feature exists in System V `make`, but is undocumented. It is documented in 4.3 BSD `make` (which says it mimics System V’s `VPATH` feature).
- Included makefiles. See Including Other Makefiles. Allowing multiple files to be included with a single directive is a GNU extension.
- Variables are read from and communicated via the environment. See Variables from the Environment.
- Options passed through the variable `MAKEFLAGS` to recursive invocations of `make`. See Communicating Options to a Sub-`make`.
- The automatic variable `$%` is set to the member name in an archive reference. See Automatic Variables.
- The automatic variables `$@`, `$*`, `$<`, `$%`, and `$?` have corresponding forms like `$(@F)` and `$(@D)`. We have generalized this to `$^` as an obvious extension. See Automatic Variables.
- Substitution variable references. See Basics of Variable References.
- The command line options ‘-b’ and ‘-m’, accepted and ignored. In System V `make`, these options actually do something.
- Execution of recursive commands to run `make` via the variable `MAKE` even if ‘-n’, ‘-q’ or ‘-t’ is specified. See Recursive Use of `make`.
- Support for suffix ‘.a’ in suffix rules. See Suffix Rules for Archive Files. This feature is obsolete in GNU `make`, because the general feature of rule chaining (see Chains of Implicit Rules) allows one pattern rule for installing members in an archive (see Implicit Rule for Archive Member Targets) to be sufficient.
- The arrangement of lines and backslash/newline combinations in recipes is retained when the recipes are printed, so they appear as they do in the makefile, except for the stripping of initial whitespace.

The following features were inspired by various other versions of `make`. In some cases it is unclear exactly which versions inspired which others.

- Pattern rules using ‘%’. This has been implemented in several versions of `make`. We’re not sure who invented it first, but it’s been spread around a bit. See Defining and Redefining Pattern Rules.
- Rule chaining and implicit intermediate files. This was implemented by Stu Feldman in his version of `make` for AT&T Eighth Edition Research Unix, and later by Andrew Hume of AT&T Bell Labs in his `mk` program (where he terms it “transitive closure”). We do not really know if we got this from either of them or thought it up ourselves at the same time. See Chains of Implicit Rules.
- The automatic variable `$^` containing a list of all prerequisites of the current target. We did not invent this, but we have no idea who did. See Automatic Variables. The automatic variable `$+` is a simple extension of `$^`.
- The “what if” flag (‘-W’ in GNU `make`) was (as far as we know) invented by Andrew Hume in `mk`. See Instead of Executing Recipes.
- The concept of doing several things at once (parallelism) exists in many incarnations of `make` and similar programs, though not in the System V or BSD implementations. See Recipe Execution.
- A number of different build tools that support parallelism also support collecting output and displaying as a single block. See Output During Parallel Execution.
- Modified variable references using pattern substitution come from SunOS 4. See Basics of Variable References. This functionality was provided in GNU `make` by the `patsubst` function before the alternate syntax was implemented for compatibility with SunOS 4. It is not altogether clear who inspired whom, since GNU `make` had `patsubst` before SunOS 4 was released.
- The special significance of ‘+’ characters preceding recipe lines (see Instead of Executing Recipes) is mandated by *IEEE Standard 1003.2-1992* (POSIX.2).
- The ‘+=’ syntax to append to the value of a variable comes from SunOS 4 `make`. See Appending More Text to Variables.
- The syntax ‘*archive*(*mem1* *mem2*…)’ to list multiple members in a single archive file comes from SunOS 4 `make`. See Archive Members as Targets.
- The `-include` directive to include makefiles with no error for a nonexistent file comes from SunOS 4 `make`. (But note that SunOS 4 `make` does not allow multiple makefiles to be specified in one `-include` directive.) The same feature appears with the name `sinclude` in SGI `make` and perhaps others.
- The `!=` shell assignment operator exists in many BSD of `make` and is purposefully implemented here to behave identically to those implementations.
- Various build management tools are implemented using scripting languages such as Perl or Python and thus provide a natural embedded scripting language, similar to GNU `make`’s integration of GNU Guile.

The remaining features are inventions new in GNU `make`:

- Use the ‘-v’ or ‘--version’ option to print version and copyright information.
- Use the ‘-h’ or ‘--help’ option to summarize the options to `make`.
- Simply-expanded variables. See The Two Flavors of Variables.
- Pass command line variable assignments automatically through the variable `MAKE` to recursive `make` invocations. See Recursive Use of `make`.
- Use the ‘-C’ or ‘--directory’ command option to change directory. See Summary of Options.
- Make verbatim variable definitions with `define`. See Defining Multi-Line Variables.
- Declare phony targets with the special target `.PHONY`. Andrew Hume of AT&T Bell Labs implemented a similar feature with a different syntax in his `mk` program. This seems to be a case of parallel discovery. See Phony Targets.
- Manipulate text by calling functions. See Functions for Transforming Text.
- Use the ‘-o’ or ‘--old-file’ option to pretend a file’s modification-time is old. See Avoiding Recompilation of Some Files.
- Conditional execution. This feature has been implemented numerous times in various versions of `make`; it seems a natural extension derived from the features of the C preprocessor and similar macro languages and is not a revolutionary concept. See Conditional Parts of Makefiles.
- Specify a search path for included makefiles. See Including Other Makefiles.
- Specify extra makefiles to read with an environment variable. See The Variable `MAKEFILES`.
- Strip leading sequences of ‘./’ from file names, so that ./*file* and *file* are considered to be the same file.
- Use a special search method for library prerequisites written in the form ‘-l*name*’. See Directory Search for Link Libraries.
- Allow suffixes for suffix rules (see Old-Fashioned Suffix Rules) to contain any characters. In other versions of `make`, they must begin with ‘.’ and not contain any ‘/’ characters.
- Keep track of the current level of `make` recursion using the variable `MAKELEVEL`. See Recursive Use of `make`.
- Provide any goals given on the command line in the variable `MAKECMDGOALS`. See Arguments to Specify the Goals.
- Specify static pattern rules. See Static Pattern Rules.
- Provide selective `vpath` search. See Searching Directories for Prerequisites.
- Provide computed variable references. See Basics of Variable References.
- Update makefiles. See How Makefiles Are Remade. System V `make` has a very, very limited form of this functionality in that it will check out SCCS files for makefiles.
- Various new built-in implicit rules. See Catalogue of Built-In Rules.
- Load dynamic objects which can modify the behavior of `make`. See Loading Dynamic Objects.

Next: Makefile Conventions, Previous: Features of GNU `make`, Up: GNU `make`   [Contents][Index]


## 15 Incompatibilities and Missing Features

The `make` programs in various other systems support a few features that are not implemented in GNU `make`. The POSIX.2 standard (*IEEE Standard 1003.2-1992*) which specifies `make` does not require any of these features.

- A target of the form ‘*file*((*entry*))’ stands for a member of archive file *file*. The member is chosen, not by name, but by being an object file which defines the linker symbol *entry*. This feature was not put into GNU `make` because of the non-modularity of putting knowledge into `make` of the internal format of archive file symbol tables. See Updating Archive Symbol Directories.
- Suffixes (used in suffix rules) that end with the character ‘~’ have a special meaning to System V `make`; they refer to the SCCS file that corresponds to the file one would get without the ‘~’. For example, the suffix rule ‘.c~.o’ would make the file *n*.o from the SCCS file s.*n*.c. For complete coverage, a whole series of such suffix rules is required. See Old-Fashioned Suffix Rules. In GNU `make`, this entire series of cases is handled by two pattern rules for extraction from SCCS, in combination with the general feature of rule chaining. See Chains of Implicit Rules.
- In System V and 4.3 BSD `make`, files found by `VPATH` search (see Searching Directories for Prerequisites) have their names changed inside recipes. We feel it is much cleaner to always use automatic variables and thus make this feature unnecessary.
- In some Unix `make`s, the automatic variable `$*` appearing in the prerequisites of a rule has the amazingly strange “feature” of expanding to the full name of the *target of that rule*. We cannot imagine what went on in the minds of Unix `make` developers to do this; it is utterly inconsistent with the normal definition of `$*`.
- In some Unix `make`s, implicit rule search (see Using Implicit Rules) is apparently done for *all* targets, not just those without recipes. This means you can do: foo.o: cc -c foo.c and Unix `make` will intuit that foo.o depends on foo.c. We feel that such usage is broken. The prerequisite properties of `make` are well-defined (for GNU `make`, at least), and doing such a thing simply does not fit the model.
- GNU `make` does not include any built-in implicit rules for compiling or preprocessing EFL programs. If we hear of anyone who is using EFL, we will gladly add them.
- It appears that in SVR4 `make`, a suffix rule can be specified with no recipe, and it is treated as if it had an empty recipe (see Using Empty Recipes). For example: .c.a: will override the built-in .c.a suffix rule. We feel that it is cleaner for a rule without a recipe to always simply add to the prerequisite list for the target. The above example can be easily rewritten to get the desired behavior in GNU `make`: .c.a: ;
- Some versions of `make` invoke the shell with the ‘-e’ flag, except under ‘-k’ (see Testing the Compilation of a Program). The ‘-e’ flag tells the shell to exit as soon as any program it runs returns a nonzero status. We feel it is cleaner to write each line of the recipe to stand on its own and not require this special treatment.

Next: Quick Reference, Previous: Incompatibilities and Missing Features, Up: GNU `make`   [Contents][Index]
