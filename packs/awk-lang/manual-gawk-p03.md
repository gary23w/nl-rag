---
title: "The GNU Awk User’s Guide (part 3/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 3/38
---

## 2 Running `awk` and `gawk`

This chapter covers how to run `awk`, both POSIX-standard and `gawk`-specific command-line options, and what `awk` and `gawk` do with nonoption arguments. It then proceeds to cover how `gawk` searches for source files, reading standard input along with other files, `gawk`’s environment variables, `gawk`’s exit status, using include files, and obsolete and undocumented options and/or features.

Many of the options and features described here are discussed in more detail later in the Web page; feel free to skip over things in this chapter that don’t interest you right now.

### 2.1 Invoking `awk`

There are two ways to run `awk`—with an explicit program or with one or more program files. Here are templates for both of them; items enclosed in […] in these templates are optional:

```
awk [options] -f progfile [--] file ...
awk [options] [--] 'program' file ...
```

In addition to traditional one-letter POSIX-style options, `gawk` also supports GNU long options.

It is possible to invoke `awk` with an empty program:

```
awk '' datafile1 datafile2
```

Doing so makes little sense, though; `awk` exits silently when given an empty program. (d.c.) If --lint has been specified on the command line, `gawk` issues a warning that the program is empty.

### 2.2 Command-Line Options

Options begin with a dash and consist of a single character. GNU-style long options consist of two dashes and a keyword. The keyword can be abbreviated, as long as the abbreviation allows the option to be uniquely identified. If the option takes an argument, either the keyword is immediately followed by an equals sign (‘=’) and the argument’s value, or the keyword and the argument’s value are separated by whitespace (spaces or TABs). If a particular option with a value is given more than once, it is (usually) the last value that counts.

Each long option for `gawk` has a corresponding POSIX-style short option. The long and short options are interchangeable in all contexts. The following list describes options mandated by the POSIX standard:

**`-F *fs*` ¶**

**`--field-separator *fs*`**

Set the `FS` variable to *fs* (see Specifying How Fields Are Separated).

**`-f *source-file*` ¶**

**`--file *source-file*`**

Read the `awk` program source from *source-file* instead of in the first nonoption argument. This option may be given multiple times; the `awk` program consists of the concatenation of the contents of each specified *source-file*.

Files named with -f are treated as if they had ‘@namespace "awk"’ at their beginning. See Changing The Namespace, for more information on this advanced feature.

**`-v *var*=*val*` ¶**

**`--assign *var*=*val*`**

Set the variable *var* to the value *val* *before* execution of the program begins. Such variable values are available inside the `BEGIN` rule (see Other Command-Line Arguments).

The -v option can only set one variable, but it can be used more than once, setting another variable each time, like this: ‘awk -v foo=1 -v bar=2 …’.

> **CAUTION:** Using -v to set the values of the built-in variables may lead to surprising results. `awk` will reset the values of those variables as it needs to, possibly ignoring any initial value you may have given.

**`-W *gawk-opt*` ¶**

Provide an implementation-specific option. This is the POSIX convention for providing implementation-specific options. These options also have corresponding GNU-style long options. Note that the long options may be abbreviated, as long as the abbreviations remain unique. The full list of `gawk`-specific options is provided next.

**`--` ¶**

Signal the end of the command-line options. The following arguments are not treated as options even if they begin with ‘-’. This interpretation of -- follows the POSIX argument parsing conventions.

This is useful if you have file names that start with ‘-’, or in shell scripts, if you have file names that will be specified by the user that could start with ‘-’. It is also useful for passing options on to the `awk` program; see Processing Command-Line Options.

The following list describes `gawk`-specific options:

**-b ¶**

**--characters-as-bytes**

Cause `gawk` to treat all input data as single-byte characters. In addition, all output written with `print` or `printf` is treated as single-byte characters.

Normally, `gawk` follows the POSIX standard and attempts to process its input data according to the current locale (see Where You Are Makes a Difference). This can often involve converting multibyte characters into wide characters (internally), and can lead to problems or confusion if the input data does not contain valid multibyte characters. This option is an easy way to tell `gawk`, “Hands off my data!”

**-c ¶**

**--traditional**

Specify *compatibility mode*, in which the GNU extensions to the `awk` language are disabled, so that `gawk` behaves just like BWK `awk`. See Extensions in `gawk` Not in POSIX `awk`, which summarizes the extensions. Also see Downward Compatibility and Debugging.

**-C ¶**

**--copyright**

Print the short version of the General Public License and then exit.

**-d[*file*] ¶**

**--dump-variables[`=`*file*]**

Print a sorted list of global variables, their types, and final values to *file*. If no *file* is provided, print this list to a file named awkvars.out in the current directory. No space is allowed between the -d and *file*, if *file* is supplied.

Having a list of all global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions don’t inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like `i`, `j`, etc.)

**-D[*file*] ¶**

**--debug[`=`*file*]**

Enable debugging of `awk` programs (see Introduction to the `gawk` Debugger). By default, the debugger reads commands interactively from the keyboard (standard input). The optional *file* argument allows you to specify a file with a list of commands for the debugger to execute noninteractively. No space is allowed between the -D and *file*, if *file* is supplied.

**-e *program-text* ¶**

**--source *program-text***

Provide program source code in the *program-text*. This option allows you to mix source code in files with source code that you enter on the command line. This is particularly useful when you have library functions that you want to use from your command-line programs (see The `AWKPATH` Environment Variable).

Note that `gawk` treats each string as if it ended with a newline character (even if it doesn’t). This makes building the total program easier.

> **CAUTION:** Prior to version 5.0, there was no requirement that each *program-text* be a full syntactic unit. I.e., the following worked:
> 
> ```
> $ gawk -e 'BEGIN { a = 5 ;' -e 'print a }'
> -| 5
> ```
> 
> However, this is no longer true. If you have any scripts that rely upon this feature, you should revise them.
> 
> This is because each *program-text* is treated as if it had ‘@namespace "awk"’ at its beginning. See Changing The Namespace, for more information.

**-E *file* ¶**

**--exec *file***

Similar to -f, read `awk` program text from *file*. There are two differences from -f:

- This option terminates option processing; anything else on the command line is passed on directly to the `awk` program.
- Command-line variable assignments of the form ‘*var*=*value*’ are disallowed.

This option is particularly necessary for World Wide Web CGI applications that pass arguments through the URL; using this option prevents a malicious (or other) user from passing in options, assignments, or `awk` source code (via -e) to the CGI application.11 This option should be used with ‘#!’ scripts (see Executable `awk` Programs), like so:

```
#! /usr/local/bin/gawk -E

awk program here ...
```

**-g ¶**

**--gen-pot**

Analyze the source program and generate a GNU `gettext` portable object template file on standard output for all string constants that have been marked for translation. See Internationalization with `gawk`, for information about this option.

**-h ¶**

**--help**

Print a “usage” message summarizing the short- and long-style options that `gawk` accepts and then exit.

**-i *source-file* ¶**

**--include *source-file***

Read an `awk` source library from *source-file*. This option is completely equivalent to using the `@include` directive inside your program. It is very similar to the -f option, but there are two important differences. First, when -i is used, the program source is not loaded if it has been previously loaded, whereas with -f, `gawk` always loads the file. Second, because this option is intended to be used with code libraries, `gawk` does not recognize such files as constituting main program input. Thus, after processing an -i argument, `gawk` still expects to find the main source code via the -f option or on the command line.

Files named with -i are treated as if they had ‘@namespace "awk"’ at their beginning. See Changing The Namespace, for more information.

**-I ¶**

**--trace**

Print the internal byte code names as they are executed when running the program. The trace is printed to standard error. Each “op code” is preceded by a `+` sign in the output.

**-k ¶**

**--csv**

Enable special processing for files with comma separated values (CSV). See Working With Comma Separated Value Files. This option cannot be used with --posix. Attempting to do causes a fatal error.

**-l *ext* ¶**

**--load *ext***

Load a dynamic extension named *ext*. Extensions are stored as system shared libraries. This option searches for the library using the `AWKLIBPATH` environment variable. The correct library suffix for your platform will be supplied by default, so it need not be specified in the extension name. The extension initialization routine should be named `dl_load()`. An alternative is to use the `@load` directive inside the program to load a shared library. This advanced feature is described in detail in Writing Extensions for `gawk`.

**-L[*value*] ¶**

**--lint[`=`*value*]**

Warn about constructs that are dubious or nonportable to other `awk` implementations. No space is allowed between the -L and *value*, if *value* is supplied. Some warnings are issued when `gawk` first reads your program. Others are issued at runtime, as your program executes. The optional argument may be one of the following:

**`fatal`**

Cause lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner `awk` programs.

**`invalid`**

Only issue warnings about things that are actually invalid are issued. (This is not fully implemented yet.)

**`no-ext`**

Disable warnings about `gawk` extensions.

Some warnings are only printed once, even if the dubious constructs they warn about occur multiple times in your `awk` program. Thus, when eliminating problems pointed out by --lint, you should take care to search for all occurrences of each inappropriate construct. As `awk` programs are usually short, doing so is not burdensome.

**-M ¶**

**--bignum**

Select arbitrary-precision arithmetic on numbers. This option has no effect if `gawk` is not compiled to use the GNU MPFR and MP libraries (see Arithmetic and Arbitrary-Precision Arithmetic with `gawk`).

As of version 5.2, the arbitrary precision arithmetic features in `gawk` are “on parole.” The primary maintainer is no longer willing to support this feature, but another member of the development team has stepped up to take it over. As long as this situation remains stable, MPFR will be supported. If it changes, the MPFR support will be removed from `gawk`.

**-n ¶**

**--non-decimal-data**

Enable automatic interpretation of octal and hexadecimal values in input data (see Allowing Nondecimal Input Data).

> **CAUTION:** This option can severely break old programs. Use with care.

**-N ¶**

**--use-lc-numeric**

Force the use of the locale’s decimal point character when parsing numeric input data (see Where You Are Makes a Difference).

**-o[*file*] ¶**

**--pretty-print[`=`*file*]**

Enable pretty-printing of `awk` programs. Implies --no-optimize. By default, the output program is created in a file named awkprof.out (see Profiling Your `awk` Programs). The optional *file* argument allows you to specify a different file name for the output. No space is allowed between the -o and *file*, if *file* is supplied.

> **NOTE:** In the past, this option would also execute your program. This is no longer the case.

**-O ¶**

**--optimize**

Enable `gawk`’s default optimizations on the internal representation of the program. At the moment, this includes just simple constant folding.

Optimization is enabled by default. This option remains primarily for backwards compatibility. However, it may be used to cancel the effect of an earlier -s option (see later in this list).

**-p[*file*] ¶**

**--profile[`=`*file*]**

Enable profiling of `awk` programs (see Profiling Your `awk` Programs). Implies --no-optimize. By default, profiles are created in a file named awkprof.out. The optional *file* argument allows you to specify a different file name for the profile file. No space is allowed between the -p and *file*, if *file* is supplied.

The profile contains execution counts for each statement in the program in the left margin, and function call counts for each function.

**-P ¶**

**--posix**

Operate in strict POSIX mode. This disables all `gawk` extensions (just like --traditional) and disables all extensions not allowed by POSIX. See Common Extensions Summary for a summary of the extensions in `gawk` that are disabled by this option. Also, the following additional restrictions apply:

- Newlines are not allowed after ‘?’ or ‘:’ (see Conditional Expressions).
- Specifying ‘-Ft’ on the command line does not set the value of `FS` to be a single TAB character (see Specifying How Fields Are Separated).
- The locale’s decimal point character is used for parsing input data (see Where You Are Makes a Difference).

If you supply both --traditional and --posix on the command line, --posix takes precedence. `gawk` issues a warning if both options are supplied.

**-r ¶**

**--re-interval**

Allow interval expressions (see Regular Expression Operators) in regexps. This is now `gawk`’s default behavior. Nevertheless, this option remains for backward compatibility.

**-s ¶**

**--no-optimize**

Disable `gawk`’s default optimizations on the internal representation of the program.

**-S ¶**

**--sandbox**

Disable the `system()` function, input redirections with `getline`, output redirections with `print` and `printf`, and dynamic extensions. Also, disallow adding file names to `ARGV` that were not there when `gawk` started running. This is particularly useful when you want to run `awk` scripts from questionable sources and need to make sure the scripts can’t access your system (other than the specified input data files).

**-t ¶**

**--lint-old**

Warn about constructs that are not available in the original version of `awk` from Version 7 Unix (see Major Changes Between V7 and SVR3.1).

**-V ¶**

**--version**

Print version information for this particular copy of `gawk`. This allows you to determine if your copy of `gawk` is up to date with respect to whatever the Free Software Foundation is currently distributing. It is also useful for bug reports (see Reporting Problems and Bugs).

**`--`**

Mark the end of all options. Any command-line arguments following `--` are placed in `ARGV`, even if they start with a minus sign.

In compatibility mode, as long as program text has been supplied, any other options are flagged as invalid with a warning message but are otherwise ignored.

In compatibility mode, as a special case, if the value of *fs* supplied to the -F option is ‘t’, then `FS` is set to the TAB character (`"\t"`). This is true only for --traditional and not for --posix (see Specifying How Fields Are Separated).

The -f option may be used more than once on the command line. If it is, `awk` reads its program source from all of the named files, as if they had been concatenated together into one big file. This is useful for creating libraries of `awk` functions. These functions can be written once and then retrieved from a standard place, instead of having to be included in each individual program. The -i option is similar in this regard. (As mentioned in Function Definition Syntax, function names must be unique.)

With standard `awk`, library functions can still be used, even if the program is entered at the keyboard, by specifying ‘-f /dev/tty’. After typing your program, type Ctrl-d (the end-of-file character) to terminate it. (You may also use ‘-f -’ to read program source from the standard input, but then you will not be able to also use the standard input as a source of data.)

Because it is clumsy using the standard `awk` mechanisms to mix source file and command-line `awk` programs, `gawk` provides the -e option. This does not require you to preempt the standard input for your source code, and it allows you to easily mix command-line and library source code (see The `AWKPATH` Environment Variable). As with -f, the -e and -i options may also be used multiple times on the command line.

If no -f option (or -e option for `gawk`) is specified, then `awk` uses the first nonoption command-line argument as the text of the program source code. Arguments on the command line that follow the program text are entered into the `ARGV` array; `awk` does *not* continue to parse the command line looking for options.

If the environment variable `POSIXLY_CORRECT` exists, then `gawk` behaves in strict POSIX mode, exactly as if you had supplied --posix. Many GNU programs look for this environment variable to suppress extensions that conflict with POSIX, but `gawk` behaves differently: it suppresses all extensions, even those that do not conflict with POSIX, and behaves in strict POSIX mode. If --lint is supplied on the command line and `gawk` turns on POSIX mode because of `POSIXLY_CORRECT`, then it issues a warning message indicating that POSIX mode is in effect. You would typically set this variable in your shell’s startup file. For a Bourne-compatible shell (such as Bash), you would add these lines to the .profile file in your home directory:

```
POSIXLY_CORRECT=true
export POSIXLY_CORRECT
```

For a C shell-compatible shell,12 you would add this line to the .login file in your home directory:

```
setenv POSIXLY_CORRECT true
```

Having `POSIXLY_CORRECT` set is not recommended for daily use, but it is good for testing the portability of your programs to other environments.

### 2.3 Other Command-Line Arguments

Any additional arguments on the command line are normally treated as input files to be processed in the order specified. However, an argument that has the form `*var*=*value*`, assigns the value *value* to the variable *var*—it does not specify a file at all. (See Assigning Variables on the Command Line.) In the following example, ‘count=1’ is a variable assignment, not a file name:

```
awk -f program.awk file1 count=1 file2
```

As a side point, should you really need to have `awk` process a file named count=1 (or any file whose name looks like a variable assignment), precede the file name with ‘./’, like so:

```
awk -f program.awk file1 ./count=1 file2
```

All the command-line arguments are made available to your `awk` program in the `ARGV` array (see Predefined Variables). Command-line options and the program text (if present) are omitted from `ARGV`. All other arguments, including variable assignments, are included. As each element of `ARGV` is processed, `gawk` sets `ARGIND` to the index in `ARGV` of the current element. (`gawk` makes the full command line, including program text and options, available in `PROCINFO["argv"]`; see Built-in Variables That Convey Information.)

Changing `ARGC` and `ARGV` in your `awk` program lets you control how `awk` processes the input files; this is described in more detail in Using `ARGC` and `ARGV`.

The distinction between file name arguments and variable-assignment arguments is made when `awk` is about to open the next input file. At that point in execution, it checks the file name to see whether it is really a variable assignment; if so, `awk` sets the variable instead of reading a file.

Therefore, the variables actually receive the given values after all previously specified files have been read. In particular, the values of variables assigned in this fashion are *not* available inside a `BEGIN` rule (see The `BEGIN` and `END` Special Patterns), because such rules are run before `awk` begins scanning the argument list.

The variable values given on the command line are processed for escape sequences (see Escape Sequences). (d.c.)

In some very early implementations of `awk`, when a variable assignment occurred before any file names, the assignment would happen *before* the `BEGIN` rule was executed. `awk`’s behavior was thus inconsistent; some command-line assignments were available inside the `BEGIN` rule, while others were not. Unfortunately, some applications came to depend upon this “feature.” When `awk` was changed to be more consistent, the -v option was added to accommodate applications that depended upon the old behavior.

The variable assignment feature is most useful for assigning to variables such as `RS`, `OFS`, and `ORS`, which control input and output formats, before scanning the data files. It is also useful for controlling state if multiple passes are needed over a data file. For example:

```
awk 'pass == 1  { pass 1 stuff }
     pass == 2  { pass 2 stuff }' pass=1 mydata pass=2 mydata
```

Given the variable assignment feature, the -F option for setting the value of `FS` is not strictly necessary. It remains for historical compatibility.

| Quoting Shell Variables On The `awk` Command Line |
|---|
| Small `awk` programs are often embedded in larger shell scripts, so it’s worthwhile to understand some shell basics. Consider the following: f="" awk '{ print("hi") }' $f In this case, `awk` reads from standard input instead of trying to open any command line files. To the unwary, this looks like `awk` is hanging. However `awk` doesn’t see an explicit empty string. When a variable expansion is the null string, *and* it’s not quoted, the shell simply removes it from the command line. To demonstrate: $ f="" $ awk 'BEGIN { print ARGC }' $f -\| 1 $ awk 'BEGIN { print ARGC }' "$f" -\| 2 |

### 2.4 Naming Standard Input

Often, you may wish to read standard input together with other files. For example, you may wish to read one file, read standard input coming from a pipe, and then read another file.

The way to name the standard input, with all versions of `awk`, is to use a single, standalone minus sign or dash, ‘-’. For example:

```
some_command | awk -f myprog.awk file1 - file2
```

Here, `awk` first reads file1, then it reads the output of *some_command*, and finally it reads file2.

You may also use `"-"` to name standard input when reading files with `getline` (see Using `getline` from a File). And, you can even use `"-"` with the -f option to read program source code from standard input (see Command-Line Options).

In addition, `gawk` allows you to specify the special file name /dev/stdin, both on the command line and with `getline`. Some other versions of `awk` also support this, but it is not standard. (Some operating systems provide a /dev/stdin file in the filesystem; however, `gawk` always processes this file name itself.)

### 2.5 The Environment Variables `gawk` Uses

A number of environment variables influence how `gawk` behaves.

#### 2.5.1 The `AWKPATH` Environment Variable

In most `awk` implementations, you must supply a precise pathname for each program file, unless the file is in the current directory. But with `gawk`, if the file name supplied to the -f or -i options does not contain a directory separator ‘/’, then `gawk` searches a list of directories (called the *search path*) one by one, looking for a file with the specified name.

The search path is a string consisting of directory names separated by colons.13 `gawk` gets its search path from the `AWKPATH` environment variable. If that variable does not exist, or if it has an empty value, `gawk` uses a default path (described shortly).

The search path feature is particularly helpful for building libraries of useful `awk` functions. The library files can be placed in a standard directory in the default path and then specified on the command line with a short file name. Otherwise, you would have to type the full file name for each file.

By using the -i or -f options, your command-line `awk` programs can use facilities in `awk` library files (see A Library of `awk` Functions). Path searching is always done, even if `gawk` is in compatibility mode. This is true for both --traditional and --posix. See Command-Line Options.

If the source code file is not found after the initial search, the path is searched again after adding the suffix ‘.awk’ to the file name.

`gawk`’s path search mechanism is similar to the shell’s. (See *The Bourne-Again SHell manual*.) It treats a null entry in the path as indicating the current directory. (A null entry is indicated by starting or ending the path with a colon or by placing two colons next to each other [‘::’].)

> **NOTE:** To include the current directory in the path, either place . as an entry in the path or write a null entry in the path.
> 
> Different past versions of `gawk` would also look explicitly in the current directory, either before or after the path search. As of version 4.1.2, this no longer happens; if you wish to look in the current directory, you must include . either as a separate entry or as a null entry in the search path.

The default value for `AWKPATH` is ‘.:/usr/local/share/awk’.14 Since . is included at the beginning, `gawk` searches first in the current directory and then in /usr/local/share/awk. In practice, this means that you will rarely need to change the value of `AWKPATH`.

See Shell Startup Files, for information on functions that help to manipulate the `AWKPATH` variable.

`gawk` places the value of the search path that it used into `ENVIRON["AWKPATH"]`. This provides access to the actual search path value from within an `awk` program.

Although you can change `ENVIRON["AWKPATH"]` within your `awk` program, this has no effect on the running program’s behavior. This makes sense: the `AWKPATH` environment variable is used to find the program source files. Once your program is running, all the files have been found, and `gawk` no longer needs to use `AWKPATH`.

#### 2.5.2 The `AWKLIBPATH` Environment Variable

The `AWKLIBPATH` environment variable is similar to the `AWKPATH` variable, but it is used to search for loadable extensions (stored as system shared libraries) specified with the -l option rather than for source files. If the extension is not found, the path is searched again after adding the appropriate shared library suffix for the platform. For example, on GNU/Linux systems, the suffix ‘.so’ is used. The search path specified is also used for extensions loaded via the `@load` directive (see Loading Dynamic Extensions into Your Program).

If `AWKLIBPATH` does not exist in the environment, or if it has an empty value, `gawk` uses a default path; this is typically ‘/usr/local/lib/gawk’, although it can vary depending upon how `gawk` was built.15

See Shell Startup Files, for information on functions that help to manipulate the `AWKLIBPATH` variable.

`gawk` places the value of the search path that it used into `ENVIRON["AWKLIBPATH"]`. This provides access to the actual search path value from within an `awk` program.

Although you can change `ENVIRON["AWKLIBPATH"]` within your `awk` program, this has no effect on the running program’s behavior. This makes sense: the `AWKLIBPATH` environment variable is used to find any requested extensions, and they are loaded before the program starts to run. Once your program is running, all the extensions have been found, and `gawk` no longer needs to use `AWKLIBPATH`.

#### 2.5.3 Other Environment Variables

A number of other environment variables affect `gawk`’s behavior, but they are more specialized. Those in the following list are meant to be used by regular users:

**`GAWK_MSEC_SLEEP`**

Specifies the interval between connection retries, in milliseconds. On systems that do not support the `usleep()` system call, the value is rounded up to an integral number of seconds.

**`GAWK_PERSIST_FILE`**

Specifies the backing file to use for persistent storage of `gawk`’s variables and arrays. See Preserving Data Between Runs.

**`GAWK_READ_TIMEOUT`**

Specifies the time, in milliseconds, for `gawk` to wait for input before returning with an error. See Reading Input with a Timeout.

**`GAWK_SOCK_RETRIES`**

Controls the number of times `gawk` attempts to retry a two-way TCP/IP (socket) connection before giving up. See Using `gawk` for Network Programming. Note that when nonfatal I/O is enabled (see Enabling Nonfatal Output), `gawk` only tries to open a TCP/IP socket once.

**`PMA_VERBOSITY`**

Controls the verbosity of the persistent memory allocator. See Preserving Data Between Runs.

**`POSIXLY_CORRECT`**

Causes `gawk` to switch to POSIX-compatibility mode, disabling all traditional and GNU extensions. See Command-Line Options.

The environment variables in the following list are meant for use by the `gawk` developers for testing and tuning. They are subject to change. The variables are:

**`AWKBUFSIZE`**

This variable only affects `gawk` on POSIX-compliant systems. With a value of ‘exact’, `gawk` uses the size of each input file as the size of the memory buffer to allocate for I/O. Otherwise, the value should be a number, and `gawk` uses that number as the size of the buffer to allocate. (When this variable is not set, `gawk` uses the smaller of the file’s size and the “default” blocksize, which is usually the filesystem’s I/O blocksize.)

**`AWK_HASH`**

If this variable exists with a value of ‘gst’, `gawk` switches to using the hash function from GNU Smalltalk for managing arrays. With a value of ‘fnv1a’, `gawk` uses the FNV1-A hash function. These functions may be marginally faster than the standard function.

**`AWKREADFUNC`**

If this variable exists, `gawk` switches to reading source files one line at a time, instead of reading in blocks. This exists for debugging problems on filesystems on non-POSIX operating systems where I/O is performed in records, not in blocks.

**`GAWK_MSG_SRC`**

If this variable exists, `gawk` includes the file name and line number within the `gawk` source code from which warning and/or fatal messages are generated. Its purpose is to help isolate the source of a message, as there are multiple places that produce the same warning or error message.

**`GAWK_LOCALE_DIR`**

Specifies the location of compiled message object files for `gawk` itself. This is passed to the `bindtextdomain()` function when `gawk` starts up.

**`GAWK_NO_DFA`**

If this variable exists, `gawk` does not use the DFA regexp matcher for “does it match” kinds of tests. This can cause `gawk` to be slower. Its purpose is to help isolate differences between the two regexp matchers that `gawk` uses internally. (There aren’t supposed to be differences, but occasionally theory and practice don’t coordinate with each other.)

**`GAWK_STACKSIZE`**

This specifies the amount by which `gawk` should grow its internal evaluation stack, when needed.

**`INT_CHAIN_MAX`**

This specifies intended maximum number of items `gawk` will maintain on a hash chain for managing arrays indexed by integers.

**`STR_CHAIN_MAX`**

This specifies intended maximum number of items `gawk` will maintain on a hash chain for managing arrays indexed by strings.

**`TIDYMEM`**

If this variable exists, `gawk` uses the `mtrace()` library calls from the GNU C library to help track down possible memory leaks. This cannot be used together with the persistent memory allocator.

### 2.6 `gawk`’s Exit Status

If the `exit` statement is used with a value (see The `exit` Statement), then `gawk` exits with the numeric value given to it.

Otherwise, if there were no problems during execution, `gawk` exits with the value of the C constant `EXIT_SUCCESS`. This is usually zero.

If an error occurs, `gawk` exits with the value of the C constant `EXIT_FAILURE`. This is usually one.

If `gawk` exits because of a fatal error, the exit status is two. On non-POSIX systems, this value may be mapped to `EXIT_FAILURE`.

### 2.7 Including Other Files into Your Program

This section describes a feature that is specific to `gawk`. It discusses how one source file may include another.

The `@include` directive can be used to read external `awk` source files. This gives you the ability to split large `awk` source files into smaller, more manageable pieces, and also lets you reuse common `awk` code from various `awk` scripts. In other words, you can group together `awk` functions used to carry out specific tasks into external files. These files can be used just like function libraries, using the `@include` directive in conjunction with the `AWKPATH` environment variable. Note that source files may also be included using the -i option.

Let’s see an example. We’ll start with two (trivial) `awk` scripts, namely test1 and test2. Here is the test1 script:

```
BEGIN {
    print "This is script test1."
}
```

and here is test2:

```
@include "test1"
BEGIN {
    print "This is script test2."
}
```

Running `gawk` with test2 produces the following result:

```
$ gawk -f test2
-| This is script test1.
-| This is script test2.
```

`gawk` runs the test2 script, which includes test1 using the `@include` directive. So, to include external `awk` source files, you just use `@include` followed by the name of the file to be included, enclosed in double quotes.

> **NOTE:** Keep in mind that this is a language construct and the file name cannot be a string variable, but rather just a literal string constant in double quotes.

The files to be included may be nested; e.g., given a third script, namely test3:

```
@include "test2"
BEGIN {
    print "This is script test3."
}
```

Running `gawk` with the test3 script produces the following results:

```
$ gawk -f test3
-| This is script test1.
-| This is script test2.
-| This is script test3.
```

The file name can, of course, be a pathname. For example:

```
@include "../io_funcs"
```

and:

```
@include "/usr/awklib/network"
```

are both valid. The `AWKPATH` environment variable can be of great value when using `@include`. The same rules for the use of the `AWKPATH` variable in command-line file searches (see The `AWKPATH` Environment Variable) apply to `@include` also.

This is very helpful in constructing `gawk` function libraries. If you have a large script with useful, general-purpose `awk` functions, you can break it down into library files and put those files in a special directory. You can then include those “libraries,” either by using the full pathnames of the files, or by setting the `AWKPATH` environment variable accordingly and then using `@include` with just the file part of the full pathname. Of course, you can keep library files in more than one directory; the more complex the working environment is, the more directories you may need to organize the files to be included.

Given the ability to specify multiple -f options, the `@include` mechanism is not strictly necessary. However, the `@include` directive can help you in constructing self-contained `gawk` programs, thus reducing the need for writing complex and tedious command lines. In particular, `@include` is very useful for writing CGI scripts to be run from web pages.

The `@include` directive and the -i/--include command line option are completely equivalent. An included program source is not loaded if it has been previously loaded.

The rules for finding a source file described in The `AWKPATH` Environment Variable also apply to files loaded with `@include`.

Finally, files included with `@include` are treated as if they had ‘@namespace "awk"’ at their beginning. See Changing The Namespace, for more information. However, there is a separate `@nsinclude` command which does not change the namespace; see Including A File Without Changing The Namespace.

### 2.8 Loading Dynamic Extensions into Your Program

This section describes a feature that is specific to `gawk`.

The `@load` directive can be used to read external `awk` extensions (stored as system shared libraries). This allows you to link in compiled code that may offer superior performance and/or give you access to extended capabilities not supported by the `awk` language. The `AWKLIBPATH` variable is used to search for the extension. Using `@load` is completely equivalent to using the -l command-line option.

If the extension is not initially found in `AWKLIBPATH`, another search is conducted after appending the platform’s default shared library suffix to the file name. For example, on GNU/Linux systems, the suffix ‘.so’ is used:

```
$ gawk '@load "ordchr"; BEGIN {print chr(65)}'
-| A
```

This is equivalent to the following example:

```
$ gawk -lordchr 'BEGIN {print chr(65)}'
-| A
```

For command-line usage, the -l option is more convenient, but `@load` is useful for embedding inside an `awk` source file that requires access to an extension.

Writing Extensions for `gawk`, describes how to write extensions (in C or C++) that can be loaded with either `@load` or the -l option. It also describes the `ordchr` extension.

### 2.9 Obsolete Options and/or Features

This section describes features and/or command-line options from previous releases of `gawk` that either are not available in the current version or are still supported but deprecated (meaning that they will *not* be in a future release).

As of `gawk` version 5.2, the arbitrary precision arithmetic feature is “on parole.” This feature is now being supported by a volunteer in the development team and not by the primary maintainer. If this situation changes, then the feature will be removed. For more information see Arbitrary Precision Arithmetic is On Parole!.

### 2.10 Undocumented Options and Features

> *Use the Source, Luke!*

—

Obi-Wan

This section intentionally left blank.

### 2.11 Summary

- `gawk` parses arguments on the command line, left to right, to determine if they should be treated as options or as non-option arguments.
- `gawk` recognizes several options which control its operation, as described in Command-Line Options. All options begin with ‘-’.
- Any argument that is not recognized as an option is treated as a non-option argument, even if it begins with ‘-’.
  - However, when an option itself requires an argument, and the option is separated from that argument on the command line by at least one space, the space is ignored, and the argument is considered to be related to the option. Thus, in the invocation, ‘gawk -F x’, the ‘x’ is treated as belonging to the -F option, not as a separate non-option argument.
- Once `gawk` finds a non-option argument, it stops looking for options. Therefore, all following arguments are also non-option arguments, even if they resemble recognized options.
- If no -e or -f options are present, `gawk` expects the program text to be in the first non-option argument.
- All non-option arguments, except program text provided in the first non-option argument, are placed in `ARGV` as explained in Using `ARGC` and `ARGV`, and are processed as described in Other Command-Line Arguments. Adjusting `ARGC` and `ARGV` affects how `awk` processes input.
- The three standard options for all versions of `awk` are -f, -F, and -v. `gawk` supplies these and many others, as well as corresponding GNU-style long options.
- Nonoption command-line arguments are usually treated as file names, unless they have the form ‘*var*=*value*’, in which case they are taken as variable assignments to be performed at that point in processing the input.
- You can use a single minus sign (‘-’) to refer to standard input on the command line. `gawk` also lets you use the special file name /dev/stdin.
- `gawk` pays attention to a number of environment variables. `AWKPATH`, `AWKLIBPATH`, and `POSIXLY_CORRECT` are the most important ones.
- `gawk`’s exit status conveys information to the program that invoked it. Use the `exit` statement from within an `awk` program to set the exit status.
- `gawk` allows you to include other `awk` source files into your program using the `@include` directive and/or the -i and -f command-line options.
- `gawk` allows you to load additional functions written in C or C++ using the `@load` directive and/or the -l option. (This advanced feature is described later, in Writing Extensions for `gawk`.)
