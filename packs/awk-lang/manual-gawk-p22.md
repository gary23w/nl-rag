---
title: "The GNU Awk User’s Guide (part 22/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 22/38
---

# The GNU Awk User’s Guide

Note also that ptys are not fully transparent. Certain binary control codes, such Ctrl-d for end-of-file, are interpreted by the tty driver and not passed through.

> **CAUTION:** Finally, coprocesses open up the possibility of *deadlock* between `gawk` and the program running in the coprocess. This can occur if you send “too much” data to the coprocess before reading any back; each process is blocked writing data with no one available to read what they’ve already written. There is no workaround for deadlock; careful programming and knowledge of the behavior of the coprocess are required.

The following example, due to Andrew Schorr, demonstrates how using ptys can help deal with buffering deadlocks.

Suppose `gawk` were unable to add numbers. You could use a coprocess to do it. Here’s an exceedingly simple program written for that purpose:

```
$ cat add.c
#include <stdio.h>

int
main(void)
{
    int x, y;
    while (scanf("%d %d", & x, & y) == 2)
        printf("%d\n", x + y);
    return 0;
}
$ cc -O add.c -o add      Compile the program
```

You could then write an exceedingly simple `gawk` program to add numbers by passing them to the coprocess:

```
$ echo 1 2 |
> gawk -v cmd=./add '{ print |& cmd; cmd |& getline x; print x }'
```

And it would deadlock, because add.c fails to call ‘setlinebuf(stdout)’. The `add` program freezes.

Now try instead:

```
$ echo 1 2 |
> gawk -v cmd=add 'BEGIN { PROCINFO[cmd, "pty"] = 1 }
>                  { print |& cmd; cmd |& getline x; print x }'
-| 3
```

By using a pty, `gawk` fools the standard I/O library into thinking it has an interactive session, so it defaults to line buffering. And now, magically, it works!

### 12.5 Using `gawk` for Network Programming

> `EMRED`:     *A host is a host from coast to coast,     and nobody talks to a host that’s close,     unless the host that isn’t close     is busy, hung, or dead.*

—

Mike O’Brien (aka Mr. Protocol)

In addition to being able to open a two-way pipeline to a coprocess on the same system (see Two-Way Communications with Another Process), it is possible to make a two-way connection to another process on another system across an IP network connection.

You can think of this as just a *very long* two-way pipeline to a coprocess. The way `gawk` decides that you want to use TCP/IP networking is by recognizing special file names that begin with one of ‘/inet/’, ‘/inet4/’, or ‘/inet6/’.

The full syntax of the special file name is /*net-type*/*protocol*/*local-port*/*remote-host*/*remote-port*. The components are:

***net-type***

Specifies the kind of Internet connection to make. Use ‘/inet4/’ to force IPv4, and ‘/inet6/’ to force IPv6. Plain ‘/inet/’ (which used to be the only option) uses the system default, most likely IPv4.

***protocol***

The protocol to use over IP. This must be either ‘tcp’, or ‘udp’, for a TCP or UDP IP connection, respectively. TCP should be used for most applications. As of version 5.4 of `gawk`, use of UDP is considered obsolete, as it never worked very well. `gawk` issues a warning if UDP is used. Support for it will be removed in version 6.0.

***local-port* ¶**

The local TCP or UDP port number to use. Use a port number of ‘0’ when you want the system to pick a port. This is what you should do when writing a TCP or UDP client. You may also use a well-known service name, such as ‘smtp’ or ‘http’, in which case `gawk` attempts to determine the predefined port number using the C `getaddrinfo()` function.

***remote-host***

The IP address or fully qualified domain name of the Internet host to which you want to connect.

***remote-port***

The TCP or UDP port number to use on the given *remote-host*. Again, use ‘0’ if you don’t care, or else a well-known service name.

> **NOTE:** Failure in opening a two-way socket will result in a nonfatal error being returned to the calling code. The value of `ERRNO` indicates the error (see Built-in Variables That Convey Information).

Consider the following very simple example:

```
BEGIN {
    Service = "/inet/tcp/0/localhost/daytime"
    Service |& getline
    print $0
    close(Service)
}
```

This program reads the current date and time from the local system’s TCP `daytime` server. It then prints the results and closes the connection.

Because this topic is extensive, the use of `gawk` for TCP/IP programming is documented separately. See *TCP/IP Internetworking with `gawk`*, which comes as part of the `gawk` distribution, for a much more complete introduction and discussion, as well as extensive examples.

> **NOTE:** `gawk` can only open direct sockets. There is currently no way to access services available over Secure Socket Layer (SSL); this includes any web service whose URL starts with ‘https://’.

### 12.6 Profiling Your `awk` Programs

You may produce execution traces of your `awk` programs. This is done by passing the option --profile to `gawk`. When `gawk` has finished running, it creates a profile of your program in a file named awkprof.out. Because it is profiling, it also executes up to 45% slower than `gawk` normally does.

As shown in the following example, the --profile option can be used to change the name of the file where `gawk` will write the profile:

```
gawk --profile=myprog.prof -f myprog.awk data1 data2
```

In the preceding example, `gawk` places the profile in myprog.prof instead of in awkprof.out.

Here is a sample session showing a simple `awk` program, its input data, and the results from running `gawk` with the --profile option. First, the `awk` program:

```
BEGIN { print "First BEGIN rule" }

END { print "First END rule" }

/foo/ {
    print "matched /foo/, gosh"
    for (i = 1; i <= 3; i++)
        sing()
}

{
    if (/foo/)
        print "if is true"
    else
        print "else is true"
}

BEGIN { print "Second BEGIN rule" }

END { print "Second END rule" }

function sing(    dummy)
{
    print "I gotta be me!"
}
```

Following is the input data:

```
foo
bar
baz
foo
junk
```

Here is the awkprof.out that results from running the `gawk` profiler on this program and data (this example also illustrates that `awk` programmers sometimes get up very early in the morning to work):

```
    # gawk profile, created Mon Sep 29 05:16:21 2014

    # BEGIN rule(s)

    BEGIN {
 1          print "First BEGIN rule"
    }

    BEGIN {
 1          print "Second BEGIN rule"
    }

    # Rule(s)

 5  /foo/ { # 2
 2          print "matched /foo/, gosh"
 6          for (i = 1; i <= 3; i++) {
 6                  sing()
            }
    }

 5  {
 5          if (/foo/) { # 2
 2                  print "if is true"
 3          } else {
 3                  print "else is true"
            }
    }

    # END rule(s)

    END {
 1          print "First END rule"
    }

    END {
 1          print "Second END rule"
    }

    # Functions, listed alphabetically

 6  function sing(dummy)
    {
 6          print "I gotta be me!"
    }
```

This example illustrates many of the basic features of profiling output. They are as follows:

- The program is printed in the order `BEGIN` rules, `BEGINFILE` rules, pattern–action rules, `ENDFILE` rules, `END` rules, and functions, listed alphabetically. Multiple `BEGIN` and `END` rules retain their separate identities, as do multiple `BEGINFILE` and `ENDFILE` rules.
- Pattern–action rules have two counts. The first count, to the left of the rule, shows how many times the rule’s pattern was *tested*. The second count, to the right of the rule’s opening left brace in a comment, shows how many times the rule’s action was *executed*. The difference between the two indicates how many times the rule’s pattern evaluated to false.
- Similarly, the count for an `if`-`else` statement shows how many times the condition was tested. To the right of the opening left brace for the `if`’s body is a count showing how many times the condition was true. The count for the `else` indicates how many times the test failed.
- The count for a loop header (such as `for` or `while`) shows how many times the loop test was executed. (Because of this, you can’t just look at the count on the first statement in a rule to determine how many times the rule was executed. If the first statement is a loop, the count is misleading.)
- For user-defined functions, the count next to the `function` keyword indicates how many times the function was called. The counts next to the statements in the body show how many times those statements were executed.
- The layout uses “K&R” style with TABs. Braces are used everywhere, even when the body of an `if`, `else`, or loop is only a single statement.
- Parentheses are used only where needed, as indicated by the structure of the program and the precedence rules. For example, ‘(3 + 5) * 4’ means add three and five, then multiply the total by four. However, ‘3 + 5 * 4’ has no parentheses, and means ‘3 + (5 * 4)’. However, explicit parentheses in the source program are retained.
- Parentheses are used around the arguments to `print` and `printf` only when the `print` or `printf` statement is followed by a redirection. Similarly, if the target of a redirection isn’t a scalar, it gets parenthesized.
- `gawk` supplies leading comments in front of the `BEGIN` and `END` rules, the `BEGINFILE` and `ENDFILE` rules, the pattern–action rules, and the functions.
- Functions are listed alphabetically. All functions in the `awk` namespace are listed first, in alphabetical order. Then come the functions in namespaces. The namespaces are listed in alphabetical order, and the functions within each namespace are listed alphabetically.

The profiled version of your program may not look exactly like what you typed when you wrote it. This is because `gawk` creates the profiled version by “pretty-printing” its internal representation of the program. The advantage to this is that `gawk` can produce a standard representation. Also, things such as:

```
/foo/
```

come out as:

```
/foo/   {
    print
}
```

which is correct, but possibly unexpected. (If a program uses both ‘print $0’ and plain ‘print’, that distinction is retained.)

Besides creating profiles when a program has completed, `gawk` can produce a profile while it is running. This is useful if your `awk` program goes into an infinite loop and you want to see what has been executed. To use this feature, run `gawk` with the --profile option in the background:

```
$ gawk --profile -f myprog &
[1] 13992
```

The shell prints a job number and process ID number; in this case, 13992. Use the `kill` command to send the `USR1` signal to `gawk`:

```
$ kill -USR1 13992
```

As usual, the profiled version of the program is written to awkprof.out, or to a different file if one was specified with the --profile option.

Along with the regular profile, as shown earlier, the profile file includes a trace of any active functions:

```
# Function Call Stack:

#   3. baz
#   2. bar
#   1. foo
# -- main --
```

You may send `gawk` the `USR1` signal as many times as you like. Each time, the profile and function call trace are appended to the output profile file.

If you use the `HUP` signal instead of the `USR1` signal, `gawk` produces the profile and the function call trace and then exits.

When `gawk` runs on MS-Windows systems, it uses the `INT` and `QUIT` signals for producing the profile, and in the case of the `INT` signal, `gawk` exits. This is because these systems don’t support the `kill` command, so the only signals you can deliver to a program are those generated by the keyboard. The `INT` signal is generated by the Ctrl-c or Ctrl-BREAK key, while the `QUIT` signal is generated by the Ctrl-\ key.

Finally, `gawk` also accepts another option, --pretty-print. When called this way, `gawk` “pretty-prints” the program into awkprof.out, without any execution counts.

> **NOTE:** Once upon a time, the --pretty-print option would also run your program. This is no longer the case.

There is a significant difference between the output created when profiling, and that created when pretty-printing. Pretty-printed output preserves the original comments that were in the program, although their placement may not correspond exactly to their original locations in the source code. However, no comments should be lost. Also, `gawk` does the best it can to preserve the distinction between comments at the end of a statement and comments on lines by themselves. This isn’t always perfect, though.

However, as a deliberate design decision, profiling output *omits* the original program’s comments. This allows you to focus on the execution count data and helps you avoid the temptation to use the profiler for pretty-printing.

Additionally, pretty-printed output does not have the leading indentation that the profiling output does. This makes it easy to pretty-print your code once development is completed, and then use the result as the final version of your program.

Because the internal representation of your program is formatted to recreate an `awk` program, profiling and pretty-printing automatically disable `gawk`’s default optimizations.

Profiling and pretty-printing also preserve the original format of numeric constants; if you used an octal or hexadecimal value in your source code, it will appear that way in the output.

### 12.7 Preserving Data Between Runs

Starting with version 5.2, `gawk` supports *persistent memory*. This feature stores the values of all of `gawk`’s variables, arrays and user-defined functions in a persistent heap, which resides in a file in the filesystem. When persistent memory is not in use (the normal case), `gawk`’s data resides in ephemeral system memory.

Persistent memory is enabled on certain 64-bit systems supporting the `mmap()` and `munmap()` system calls. Since the persistent store ends up holding pointers to functions held within the `gawk` executable, in order to use persistent memory, you must use the same `gawk` executable from run to run.

You can see if your version of `gawk` supports persistent memory like so:

```
$ gawk --version
-| GNU Awk 5.4.0, API 4.1, PMA Avon 8-g1, (GNU MPFR 4.2.1, GNU MP 6.3.0)
-| Copyright (C) 1989, 1991-2026 Free Software Foundation.
...
```

If you see the ‘PMA’ with a version indicator, then it’s supported.

As of this writing, persistent memory has only been tested on GNU/Linux, Cygwin, FreeBSD 12–16, macOS, MidnightBSD 3 and 4, NetBSD 10 and 11, OpenBSD 7, and Solaris 2.11. On all others, persistent memory is disabled by default. You can force it to be enabled by exporting the shell variable `REALLY_USE_PERSIST_MALLOC` with a nonempty value before running `configure` (see Compiling `gawk` for Unix-Like Systems). If you do so and all the tests pass, please let the maintainer know.

To use persistent memory, follow these steps:

1. Create a new, empty sparse file of the desired size. For example, four gigabytes. On a GNU/Linux system, you can use the `truncate` utility: $ truncate -s 4G data.pma
2. It is recommended (but not required) to change the permissions on the file so that only the owner can read and write it: $ chmod 0600 data.pma
3. Provide the path to the data file in the `GAWK_PERSIST_FILE` environment variable. This is best done by placing the value in the environment just for the run of `gawk`, like so: $ GAWK_PERSIST_FILE=data.pma gawk 'BEGIN { print ++i }' 1
4. Use the same data file in subsequent runs to use the preserved data values: $ GAWK_PERSIST_FILE=data.pma gawk 'BEGIN { print ++i }' 2 $ GAWK_PERSIST_FILE=data.pma gawk 'BEGIN { print ++i }' 3 As shown, in subsequent runs using the same data file, the values of `gawk`’s variables are preserved. However, `gawk`’s special variables, such as `NR`, are reset upon each run. Only the variables defined by the program are preserved across runs.

Interestingly, the `awk` program that you execute need not be the same from run to run; the persistent store only maintains the values of variables, arrays, and user-defined functions, not the totality of `gawk`’s internal state. This lets you share data between unrelated `awk` programs, eliminating the need for scripts to communicate via text files.

Terence Kelly, the author of the persistent memory allocator `gawk` uses, provides the following advice about the backing file:

> Regarding backing file size, I recommend making it far larger than all of the data that will ever reside in it, assuming that the file system supports sparse files. The “pay only for what you use” aspect of sparse files ensures that the actual storage resource footprint of the backing file will meet the application’s needs but will be as small as possible. If the file system does *not* support sparse files, there’s a dilemma: Making the backing file too large is wasteful, but making it too small risks memory exhaustion, i.e., `pma_malloc()` returns `NULL`. But persistent `gawk` should still work even without sparse files.

You can disable the use of the persistent memory allocator in `gawk` with the --disable-pma option to the `configure` command at the time that you build `gawk` (see Compiling and Installing `gawk` on Unix-Like Systems).

You can set the `PMA_VERBOSITY` environment variable to a value between zero and three to control how much debugging and error information the persistent memory allocator will print. `gawk` sets the default to one. See the support/pma.c source code to understand what the different verbosity levels are.

There are a few constraints on the use of persistent memory:

- If you use MPFR mode (the -M option) on the first run of a program using persistent memory, you *must* continue to use it on all subsequent runs. Similarly, if you don’t use -M on the first run, do not use it on any subsequent runs. Mixing and matching MPFR mode and regular mode with the same backing file is not allowed. `gawk` detects such a situation and issues a fatal error message.
- The GNU/Linux CIFS filesystem is known to not work well with the PMA allocator. Don’t use a backing file on a CIFS filesystem.
- If `gawk` is run by the `root` user, then persistent memory is not allowed. This is to avoid the possibility of private data “leaking” into the backing file and being recovered later by an attacker.
- Over time, the backing file will be filled with memory “leaked” by `gawk` as it runs. Most notably this is the memory used to compile your program into an internal form before running it, which happens each time, but there are other leakages as well. (For an extreme example of this, see this thread in the “bug-gawk at gnu.org” mailing list archives.) It is up to you to use ‘du -sh *pmafile*’ occasionally to monitor how full the file is, and arrange to dump any data you may need before the backing file becomes full.
- You can use dynamically loaded extensions (see Writing Extensions for `gawk`) with persistent memory. However, `gawk` notices if an extension is being loaded from a different path than previously, and in such a case it generates a fatal error.
- `gawk` produces a warning if the current version of `gawk` doesn’t match the one that was first used with a particular backing storage file.

Terence Kelly has provided a separate *Persistent-Memory `gawk` User Manual* document, which is included in the `gawk` distribution. It is worth reading.

Here are additional articles and web links that provide more information about persistent memory and why it’s useful in a scripting language like `gawk`.

**https://web.eecs.umich.edu/~tpkelly/pma/**

This is the canonical source for Terence Kelly’s Persistent Memory Allocator (PMA). The latest source code and user manual will always be available at this location. Kelly may be reached directly at any of the following email addresses: “tpkelly AT acm.org”, “tpkelly AT cs.princeton.edu”, or “tpkelly AT eecs.umich.edu”.

***Persistent Memory Allocation***

Terence Kelly, Zi Fan Tan, Jianan Li, and Haris Volos, ACM *Queue* magazine, Vol. 20 No. 2 (March/April 2022), PDF, HTML. This paper explains the design of the PMA allocator used in persistent `gawk`.

***Persistent Scripting***

Zi Fan Tan, Jianan Li, Haris Volos, and Terence Kelly, Non-Volatile Memory Workshop (NVMW) 2022, http://nvmw.ucsd.edu/program/. This paper motivates and describes a research prototype of persistent `gawk` and presents performance evaluations on Intel Optane non-volatile memory; note that the interface differs slightly.

***Persistent Memory Programming on Conventional Hardware***

Terence Kelly, ACM *Queue* magazine Vol. 17 No. 4 (July/Aug 2019), PDF, HTML. This paper describes simple techniques for persistent memory for C/C++ code on conventional computers that lack non-volatile memory hardware.

***Is Persistent Memory Persistent?***

Terence Kelly, ACM *Queue* magazine Vol. 18 No. 2 (March/April 2020), PDF, HTML. This paper describes a simple and robust testbed for testing software against real power failures.

***Crashproofing the Original NoSQL Key/Value Store***

Terence Kelly, ACM *Queue* magazine Vol. 19 No. 4 (July/Aug 2021), PDF, HTML. This paper describes a crash-tolerance feature added to GNU DBM’ (`gdbm`).

When Terence Kelly published his papers, his collaborators produced a prototype integration of PMA with `gawk`. That version used a (mandatory!) option --persist=*file* to specify the file for storing the persistent heap. If this option is given to `gawk`, it produces a fatal error message instructing the user to use the `GAWK_PERSIST_FILE` environment variable instead. Except for this paragraph, that option is otherwise undocumented.

The prototype only supported persistent data; it did not support persistent functions.

> **NOTE:** The maintainer reserves the right to remove the persistent memory feature should it become burdensome.90

### 12.8 Builtin Features versus Extensions

As this and subsequent chapters show, `gawk` has a large number of extensions over standard `awk` built-in to the program. These have developed over time. More recently, the focus has moved to using the extension mechanism (see Writing Extensions for `gawk`) for adding features. This section discusses the “guiding philosophy” behind what should be added to the interpreter as a built-in feature versus what should be done in extensions.

There are several goals:

1. Keep the language `awk`; it should not become unrecognizable, even if programs in it will only run on `gawk`.
2. Keep the core from getting any larger unless absolutely necessary.
3. Add new functionality either in `awk` scripts (-f, `@include`) or in loadable extensions written in C or C++ (-l, `@load`).
4. Extend the core interpreter only if some feature is:
  1. Truly desirable.
  2. Cannot be done via library files or loadable extensions.
  3. Can be implemented without too much pain in the core.

Combining modules with `awk` files is a powerful technique. Some of the sample extensions demonstrate this.

Loading extensions and library files should not be done automatically, because then there’s overhead that most users don’t want or need.

### 12.9 Summary

- The --non-decimal-data option causes `gawk` to treat octal- and hexadecimal-looking input data as octal and hexadecimal. This option should be used with caution or not at all; use of `strtonum()` is preferable. Note that this option may disappear in a future version of `gawk`.
- You can take over complete control of sorting in ‘for (*indx* in *array*)’ array traversal by setting `PROCINFO["sorted_in"]` to the name of a user-defined function that does the comparison of array elements based on index and value.
- Similarly, you can supply the name of a user-defined comparison function as the third argument to either `asort()` or `asorti()` to control how those functions sort arrays. Or you may provide one of the predefined control strings that work for `PROCINFO["sorted_in"]`.
- You can use the ‘|&’ operator to create a two-way pipe to a coprocess. You read from the coprocess with `getline` and write to it with `print` or `printf`. Use `close()` to close off the coprocess completely, or optionally, close off one side of the two-way communications.
- By using special file names with the ‘|&’ operator, you can open a TCP/IP (or UDP/IP) connection to remote hosts on the Internet. `gawk` supports both IPv4 and IPv6.
- You can generate statement count profiles of your program. This can help you determine which parts of your program may be taking the most time and let you tune them more easily. Sending the `USR1` signal while profiling causes `gawk` to dump the profile and keep going, including a function call stack.
- You can also just “pretty-print” the program.
- Persistent memory allows you to preserve the values of variables and arrays between runs of `gawk`. This feature is currently experimental.
- New features should be developed using the extension mechanism if possible; they should be added to the core interpreter only as a last resort.


## 13 Internationalization with `gawk`

> *Moon… Gorgeous… MEDITATION!*

—

Pretty Guardian Sailor Moon Eternal, The Movie

> *It probably sounded better in Japanese.*

—

Malka Robbins

Once upon a time, computer makers wrote software that worked only in English. Eventually, hardware and software vendors noticed that if their systems worked in the native languages of non-English-speaking countries, they were able to sell more systems. As a result, internationalization and localization of programs and software systems became a common practice.

For many years, the ability to provide internationalization was largely restricted to programs written in C and C++. This chapter describes the underlying library `gawk` uses for internationalization, as well as how `gawk` makes internationalization features available at the `awk` program level. Having internationalization available at the `awk` level gives software developers additional flexibility—they are no longer forced to write in C or C++ when internationalization is a requirement.

### 13.1 Internationalization and Localization

*Internationalization* means writing (or modifying) a program once, in such a way that it can use multiple languages without requiring further source code changes. *Localization* means providing the data necessary for an internationalized program to work in a particular language. Most typically, these terms refer to features such as the language used for printing error messages, the language used to read responses, and information related to how numerical and monetary values are printed and read.

### 13.2 GNU `gettext`

`gawk` uses GNU `gettext` to provide its internationalization features. The facilities in GNU `gettext` focus on messages: strings printed by a program, either directly or via formatting with `printf` or `sprintf()`.91

When using GNU `gettext`, each application has its own *text domain*. This is a unique name, such as ‘kpilot’ or ‘gawk’, that identifies the application. A complete application may have multiple components—programs written in C or C++, as well as scripts written in `sh` or `awk`. All of the components use the same text domain.

To make the discussion concrete, assume we’re writing an application named `guide`. Internationalization consists of the following steps, in this order:

1. The programmer reviews the source for all of `guide`’s components and marks each string that is a candidate for translation. For example, "`-F': option required" is a good candidate for translation. A table with strings of option names is not (e.g., `gawk`’s --profile option should remain the same, no matter what the local language).
2. The programmer indicates the application’s text domain (`"guide"`) to the `gettext` library, by calling the `textdomain()` function.
3. Messages from the application are extracted from the source code and collected into a portable object template file (guide.pot), which lists the strings and their translations. The translations are initially empty. The original (usually English) messages serve as the key for lookup of the translations.
4. For each language with a translator, guide.pot is copied to a portable object file (`.po`) and translations are created and shipped with the application. For example, there might be a fr.po for a French translation.
5. Each language’s .po file is converted into a binary message object (.gmo) file. A message object file contains the original messages and their translations in a binary format that allows fast lookup of translations at runtime.
6. When `guide` is built and installed, the binary translation files are installed in a standard place.
7. For testing and development, it is possible to tell `gettext` to use .gmo files in a different directory than the standard one by using the `bindtextdomain()` function.
8. At runtime, `guide` looks up each string via a call to `gettext()`. The returned string is the translated string if available, or the original string if not.
9. If necessary, it is possible to access messages from a different text domain than the one belonging to the application, without having to switch the application’s default text domain back and forth.

In C (or C++), the string marking and dynamic translation lookup are accomplished by wrapping each string in a call to `gettext()`:

```
printf("%s", gettext("Don't Panic!\n"));
```

The tools that extract messages from source code pull out all strings enclosed in calls to `gettext()`.

The GNU `gettext` developers, recognizing that typing ‘gettext(…)’ over and over again is both painful and ugly to look at, use the macro ‘_’ (an underscore) to make things easier:

```
/* In the standard header file: */
#define _(str) gettext(str)

/* In the program text: */
printf("%s", _("Don't Panic!\n"));
```

This reduces the typing overhead to just three extra characters per string and is considerably easier to read as well.

There are locale *categories* for different types of locale-related information. The defined locale categories that `gettext` knows about are:

**`LC_MESSAGES` ¶**

Text messages. This is the default category for `gettext` operations, but it is possible to supply a different one explicitly, if necessary. (It is almost never necessary to supply a different category.)

**`LC_COLLATE` ¶**

Text-collation information (i.e., how different characters and/or groups of characters sort in a given language).

**`LC_CTYPE` ¶**

Character-type information (alphabetic, digit, upper- or lowercase, and so on) as well as character encoding. This information is accessed via the POSIX character classes in regular expressions, such as `/[[:alnum:]]/` (see Using Bracket Expressions).

**`LC_MONETARY` ¶**

Monetary information, such as the currency symbol, and whether the symbol goes before or after a number.

**`LC_NUMERIC` ¶**

Numeric information, such as which characters to use for the decimal point and the thousands separator.92

**`LC_TIME` ¶**

Time- and date-related information, such as 12- or 24-hour clock, month printed before or after the day in a date, local month abbreviations, and so on.

**`LC_ALL` ¶**

All of the above. (Not too useful in the context of `gettext`.)

> **NOTE:** As described in Where You Are Makes a Difference, environment variables with the same name as the locale categories (`LC_CTYPE`, `LC_ALL`, etc.) influence `gawk`’s behavior (and that of other utilities).
> 
> Normally, these variables also affect how the `gettext` library finds translations. However, the `LANGUAGE` environment variable overrides the `LC_*xxx*` variables. Many GNU/Linux systems may define this variable without your knowledge, causing `gawk` to not find the correct translations. If this happens to you, look to see if `LANGUAGE` is defined, and if so, use the shell’s `unset` command to remove it.

For testing translations of `gawk` itself, you can set the `GAWK_LOCALE_DIR` environment variable. See the documentation for the C `bindtextdomain()` function and also see Other Environment Variables.

### 13.3 Internationalizing `awk` Programs

`gawk` provides the following variables for internationalization:

**`TEXTDOMAIN` ¶**

This variable indicates the application’s text domain. For compatibility with GNU `gettext`, the default value is `"messages"`.

**`_"your message here"`**

String constants marked with a leading underscore are candidates for translation at runtime. String constants without a leading underscore are not translated.

`gawk` provides the following functions for internationalization:

**`dcgettext(*string*` [`,` *domain* [`,` *category*]]`)` ¶**

Return the translation of *string* in text domain *domain* for locale category *category*. The default value for *domain* is the current value of `TEXTDOMAIN`. The default value for *category* is `"LC_MESSAGES"`.

If you supply a value for *category*, it must be a string equal to one of the known locale categories described in the previous section. You must also supply a text domain. Use `TEXTDOMAIN` if you want to use the current domain.

> **CAUTION:** The order of arguments to the `awk` version of the `dcgettext()` function is purposely different from the order for the C version. The `awk` version’s order was chosen to be simple and to allow for reasonable `awk`-style default arguments.

**`dcngettext(*string1*, *string2*, *number*` [`,` *domain* [`,` *category*]]`)` ¶**

Return the plural form used for *number* of the translation of *string1* and *string2* in text domain *domain* for locale category *category*. *string1* is the English singular variant of a message, and *string2* is the English plural variant of the same message. The default value for *domain* is the current value of `TEXTDOMAIN`. The default value for *category* is `"LC_MESSAGES"`.

The same remarks about argument order as for the `dcgettext()` function apply.

**`bindtextdomain(*directory*` [`,` *domain* ]`)` ¶**

Change the directory in which `gettext` looks for .gmo files, in case they will not or cannot be placed in the standard locations (e.g., during testing). Return the directory in which *domain* is “bound.”

The default *domain* is the value of `TEXTDOMAIN`. If *directory* is the null string (`""`), then `bindtextdomain()` returns the current binding for the given *domain*.

To use these facilities in your `awk` program, follow these steps:

1. Set the variable `TEXTDOMAIN` to the text domain of your program. This is best done in a `BEGIN` rule (see The `BEGIN` and `END` Special Patterns), or it can also be done via the -v command-line option (see Command-Line Options): BEGIN { TEXTDOMAIN = "guide" ... }
2. Mark all translatable strings with a leading underscore (‘_’) character. It *must* be adjacent to the opening double quote of the string. For example: print _"hello, world" x = _"you goofed" printf(_"Number of users is %d\n", nusers)
3. If you are creating strings dynamically, you can still translate them, using the `dcgettext()` built-in function:93 if (groggy) message = dcgettext("%d customers disturbing me\n", "adminprog") else message = dcgettext("enjoying %d customers\n", "adminprog") printf(message, ncustomers) Here, the call to `dcgettext()` supplies a different text domain (`"adminprog"`) in which to find the message, but it uses the default `"LC_MESSAGES"` category. The previous example only works if `ncustomers` is greater than one. This example would be better done with `dcngettext()`: if (groggy) message = dcngettext("%d customer disturbing me\n", "%d customers disturbing me\n", ncustomers, "adminprog") else message = dcngettext("enjoying %d customer\n", "enjoying %d customers\n", ncustomers, "adminprog") printf(message, ncustomers)
4. During development, you might want to put the .gmo file in a private directory for testing. This is done with the `bindtextdomain()` built-in function: BEGIN { TEXTDOMAIN = "guide" # our text domain if (Testing) { # where to find our files bindtextdomain("testdir") # joe is in charge of adminprog bindtextdomain("../joe/testdir", "adminprog") } ... }

See A Simple Internationalization Example for an example program showing the steps to create and use translations from `awk`.

### 13.4 Translating `awk` Programs

Once a program’s translatable strings have been marked, they must be extracted to create the initial .pot file. As part of translation, it is often helpful to rearrange the order in which arguments to `printf` are output.

`gawk`’s --gen-pot command-line option extracts the messages and is discussed next. After that, `printf`’s ability to rearrange the order for `printf` arguments at runtime is covered.

#### 13.4.1 Extracting Marked Strings

Once your `awk` program is working, and all the strings have been marked and you’ve set (and perhaps bound) the text domain, it is time to produce translations. First, use the --gen-pot command-line option to create the initial .pot file:

```
gawk --gen-pot -f guide.awk > guide.pot
```

When run with --gen-pot, `gawk` does not execute your program. Instead, it parses it as usual and prints all marked strings to standard output in the format of a GNU `gettext` Portable Object file. Also included in the output are any constant strings that appear as the first argument to `dcgettext()` or as the first and second argument to `dcngettext()`.94 You should distribute the generated .pot file with your `awk` program; translators will eventually use it to provide you translations that you can also then distribute. See A Simple Internationalization Example for the full list of steps to go through to create and test translations for `guide`.

#### 13.4.2 Rearranging `printf` Arguments

Format strings for `printf` and `sprintf()` (see Using `printf` Statements for Fancier Printing) present a special problem for translation. Consider the following:95

```
printf(_"String `%s' has %d characters\n",
          string, length(string)))
```

A possible German translation for this might be:

```
"%d Zeichen lang ist die Zeichenkette `%s'\n"
```

The problem should be obvious: the order of the format specifications is different from the original! Even though `gettext()` can return the translated string at runtime, it cannot change the argument order in the call to `printf`.

To solve this problem, `printf` format specifiers may have an additional optional element, which we call a *positional specifier*. For example:

```
"%2$d Zeichen lang ist die Zeichenkette `%1$s'\n"
```

Here, the positional specifier consists of an integer count, which indicates which argument to use, and a ‘$’. Counts are one-based, and the format string itself is *not* included. Thus, in the following example, ‘string’ is the first argument and ‘length(string)’ is the second:

```
$ gawk 'BEGIN {
>     string = "Don\47t Panic"
>     printf "%2$d characters live in \"%1$s\"\n",
>                         string, length(string)
> }'
-| 11 characters live in "Don't Panic"
```

If present, positional specifiers come first in the format specification, before the flags, the field width, and/or the precision.

Positional specifiers can be used with the dynamic field width and precision capability:

```
$ gawk 'BEGIN {
>    printf("%*.*s\n", 10, 20, "hello")
>    printf("%3$*2$.*1$s\n", 20, 10, "hello")
> }'
-|      hello
-|      hello
```

> **NOTE:** When using ‘*’ with a positional specifier, the ‘*’ comes first, then the integer position, and then the ‘$’. This is somewhat counterintuitive.

`gawk` does not allow you to mix regular format specifiers and those with positional specifiers in the same string:

```
$ gawk 'BEGIN { printf "%d %3$s\n", 1, 2, "hi" }'
error→ gawk: cmd. line:1: fatal: must use `count$' on all formats or none
```

> **NOTE:** There are some pathological cases that `gawk` may fail to diagnose. In such cases, the output may not be what you expect. It’s still a bad idea to try mixing them, even if `gawk` doesn’t detect it.

Although positional specifiers can be used directly in `awk` programs, their primary purpose is to help in producing correct translations of format strings into languages different from the one in which the program is first written.

#### 13.4.3 `awk` Portability Issues

`gawk`’s internationalization features were purposely chosen to have as little impact as possible on the portability of `awk` programs that use them to other versions of `awk`. Consider this program:

```
BEGIN {
    TEXTDOMAIN = "guide"
    if (Test_Guide)   # set with -v
        bindtextdomain("/test/guide/messages")
    print _"don't panic!"
}
```

As written, it won’t work on other versions of `awk`. However, it is actually almost portable, requiring very little change:

- Assignments to `TEXTDOMAIN` won’t have any effect, because `TEXTDOMAIN` is not special in other `awk` implementations.
- Non-GNU versions of `awk` treat marked strings as the concatenation of a variable named `_` with the string following it.96 Typically, the variable `_` has the null string (`""`) as its value, leaving the original string constant as the result.
- By defining “dummy” functions to replace `dcgettext()`, `dcngettext()`, and `bindtextdomain()`, the `awk` program can be made to run, but all the messages are output in the original language. For example: function bindtextdomain(dir, domain) { return dir } function dcgettext(string, domain, category) { return string } function dcngettext(string1, string2, number, domain, category) { return (number == 1 ? string1 : string2) }
- The use of positional specifications in `printf` or `sprintf()` is *not* portable. To support `gettext()` at the C level, many systems’ C versions of `sprintf()` do support positional specifiers. But it works only if enough arguments are supplied in the function call. Many versions of `awk` pass `printf` formats and arguments unchanged to the underlying C library version of `sprintf()`, but only one format and argument at a time. What happens if a positional specification is used is anybody’s guess. However, because the positional specifications are primarily for use in *translated* format strings, and because non-GNU `awk`s never retrieve the translated string, this should not be a problem in practice.

### 13.5 A Simple Internationalization Example

Now let’s look at a step-by-step example of how to internationalize and localize a simple `awk` program, using guide.awk as our original source:

```
BEGIN {
    TEXTDOMAIN = "guide"
    bindtextdomain(".")  # for testing
    print _"Don't Panic"
    print _"The Answer Is", 42
    print "Pardon me, Zaphod who?"
}
```

Run ‘gawk --gen-pot’ to create the .pot file:

```
$ gawk --gen-pot -f guide.awk > guide.pot
```

This produces:

```
#: guide.awk:4
msgid "Don't Panic"
msgstr ""

#: guide.awk:5
msgid "The Answer Is"
msgstr ""
```

This original portable object template file is saved and reused for each language into which the application is translated. The `msgid` is the original string and the `msgstr` is the translation.

> **NOTE:** Strings not marked with a leading underscore do not appear in the guide.pot file.

Next, the messages must be translated. Here is a translation to a hypothetical dialect of English, called “Mellow”:97

```
$ cp guide.pot guide-mellow.po
Add translations to guide-mellow.po ...
```

Following are the translations:

```
#: guide.awk:4
msgid "Don't Panic"
msgstr "Hey man, relax!"

#: guide.awk:5
msgid "The Answer Is"
msgstr "Like, the scoop is"
```

> **NOTE:** The following instructions apply to GNU/Linux with the GNU C Library. Be aware that the actual steps may change over time, that the following description may not be accurate for all GNU/Linux distributions, and that things may work entirely differently on other operating systems.

The next step is to make the directory to hold the binary message object file and then to create the guide.mo file. The directory has the form *locale*/LC_MESSAGES, where *locale* is a locale name known to the C `gettext` routines.

How do we know which locale to use? It turns out that there are four different environment variables used by the C `gettext` routines. In order, they are `$LANGUAGE`, `$LC_ALL`, `$LANG`, and `$LC_MESSAGES`.98 Thus, we check the value of `$LANGUAGE`:

```
$ echo $LANGUAGE
-| en_US.UTF-8
```

We next make the directories:

```
$ mkdir en_US.UTF-8 en_US.UTF-8/LC_MESSAGES
```

The `msgfmt` utility converts the human-readable .po file into a machine-readable .mo file. By default, `msgfmt` creates a file named messages. This file must be renamed and placed in the proper directory (using the -o option) so that `gawk` can find it:

```
$ msgfmt guide-mellow.po -o en_US.UTF-8/LC_MESSAGES/guide.mo
```

Finally, we run the program to test it:

```
$ gawk -f guide.awk
-| Hey man, relax!
-| Like, the scoop is 42
-| Pardon me, Zaphod who?
```

If the three replacement functions for `dcgettext()`, `dcngettext()`, and `bindtextdomain()` (see `awk` Portability Issues) are in a file named libintl.awk, then we can run guide.awk unchanged as follows:

```
$ gawk --posix -f guide.awk -f libintl.awk
-| Don't Panic
-| The Answer Is 42
-| Pardon me, Zaphod who?
```

### 13.6 `gawk` Can Speak Your Language

`gawk` itself has been internationalized using the GNU `gettext` package. (GNU `gettext` is described in complete detail in *GNU `gettext` utilities*.) As of this writing, the latest version of GNU `gettext` is version 0.19.8.1.

If a translation of `gawk`’s messages exists, then `gawk` produces usage messages, warnings, and fatal errors in the local language.

### 13.7 Summary

- Internationalization means writing a program such that it can use multiple languages without requiring source code changes. Localization means providing the data necessary for an internationalized program to work in a particular language.
- `gawk` uses GNU `gettext` to let you internationalize and localize `awk` programs. A program’s text domain identifies the program for grouping all messages and other data together.
- You mark a program’s strings for translation by preceding them with an underscore. Once that is done, the strings are extracted into a .pot file. This file is copied for each language into a .po file, and the .po files are compiled into .gmo files for use at runtime.
- You can use positional specifications with `sprintf()` and `printf` to rearrange the placement of argument values in formatted strings and output. This is useful for the translation of format control strings.
- The internationalization features have been designed so that they can be easily worked around in a standard `awk`.
- `gawk` itself has been internationalized and ships with a number of translations for its messages.
