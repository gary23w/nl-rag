---
title: "The GNU Awk User’s Guide (part 29/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 29/38
---

## Appendix A The Evolution of the `awk` Language

This Web page describes the GNU implementation of `awk`, which follows the POSIX specification. Many longtime `awk` users learned `awk` programming with the original `awk` implementation in Version 7 Unix. (This implementation was the basis for `awk` in Berkeley Unix, through 4.3-Reno. Subsequent versions of Berkeley Unix, and, for a while, some systems derived from 4.4BSD-Lite, used various versions of `gawk` for their `awk`.) This chapter briefly describes the evolution of the `awk` language, with cross-references to other parts of the Web page where you can find more information.

### A.1 Major Changes Between V7 and SVR3.1

The `awk` language evolved considerably between the release of Version 7 Unix (1978) and the new version that was first made generally available in System V Release 3.1 (1987). This section summarizes the changes, with cross-references to further details:

- The requirement for ‘;’ to separate rules on a line (see `awk` Statements Versus Lines)
- User-defined functions and the `return` statement (see User-Defined Functions)
- The `delete` statement (see The `delete` Statement)
- The `do`-`while` statement (see The `do`-`while` Statement)
- The built-in functions `atan2()`, `cos()`, `sin()`, `rand()`, and `srand()` (see Numeric Functions)
- The built-in functions `gsub()`, `sub()`, and `match()` (see String-Manipulation Functions)
- The built-in functions `close()` and `system()` (see Input/Output Functions)
- The `ARGC`, `ARGV`, `FNR`, `RLENGTH`, `RSTART`, and `SUBSEP` predefined variables (see Predefined Variables)
- Assignable `$0` (see Changing the Contents of a Field)
- The conditional expression using the ternary operator ‘?:’ (see Conditional Expressions)
- The expression ‘*indx* in *array*’ outside of `for` statements (see Referring to an Array Element)
- The exponentiation operator ‘^’ (see Arithmetic Operators) and its assignment operator form ‘^=’ (see Assignment Expressions)
- C-compatible operator precedence, which breaks some old `awk` programs (see Operator Precedence (How Operators Nest))
- Regexps as the value of `FS` (see Specifying How Fields Are Separated) and as the third argument to the `split()` function (see String-Manipulation Functions), rather than using only the first character of `FS`
- Dynamic regexps as operands of the ‘~’ and ‘!~’ operators (see Using Dynamic Regexps)
- The escape sequences ‘\b’, ‘\f’, and ‘\r’ (see Escape Sequences)
- Redirection of input for the `getline` function (see Explicit Input with `getline`)
- Multiple `BEGIN` and `END` rules (see The `BEGIN` and `END` Special Patterns)
- Multidimensional arrays (see Multidimensional Arrays)

### A.2 Changes Between SVR3.1 and SVR4

The System V Release 4 (1989) version of Unix `awk` added these features (some of which originated in `gawk`):

- The `ENVIRON` array (see Predefined Variables)
- Multiple -f options on the command line (see Command-Line Options)
- The -v option for assigning variables before program execution begins (see Command-Line Options)
- The -- signal for terminating command-line options
- The ‘\a’, ‘\v’, and ‘\x’ escape sequences (see Escape Sequences)
- A defined return value for the `srand()` built-in function (see Numeric Functions)
- The `toupper()` and `tolower()` built-in string functions for case translation (see String-Manipulation Functions)
- A cleaner specification for the ‘%c’ format-control letter in the `printf` function (see Format-Control Letters)
- The ability to dynamically pass the field width and precision (`"%*.*d"`) in the argument list of `printf` and `sprintf()` (see Format-Control Letters)
- The use of regexp constants, such as `/foo/`, as expressions, where they are equivalent to using the matching operator, as in ‘$0 ~ /foo/’ (see Using Regular Expression Constants)
- Processing of escape sequences inside command-line variable assignments (see Assigning Variables on the Command Line)

### A.3 Changes Between SVR4 and POSIX `awk`

The POSIX Command Language and Utilities standard for `awk` (1992) introduced the following changes into the language:

- The use of -W for implementation-specific options (see Command-Line Options)
- The use of `CONVFMT` for controlling the conversion of numbers to strings (see Conversion of Strings and Numbers)
- The concept of a numeric string and tighter comparison rules to go with it (see Variable Typing and Comparison Expressions)
- The use of predefined variables as function parameter names is forbidden (see Function Definition Syntax)
- More complete documentation of many of the previously undocumented features of the language

In 2012, a number of extensions that had been commonly available for many years were finally added to POSIX. They are:

- The `fflush()` built-in function for flushing buffered output (see Input/Output Functions)
- The `nextfile` statement (see The `nextfile` Statement)
- The ability to delete all of an array at once with ‘delete *array*’ (see The `delete` Statement)

See Common Extensions Summary for a list of common extensions not permitted by the POSIX standard.

The 2018 POSIX standard can be found online at https://pubs.opengroup.org/onlinepubs/9699919799/.

### A.4 Extensions in Brian Kernighan’s `awk`

Brian Kernighan has made his version available via his home page (see Other Freely Available `awk` Implementations).

This section describes common extensions that originally appeared in his version of `awk`:

- The ‘**’ and ‘**=’ operators (see Arithmetic Operators and Assignment Expressions)
- The use of `func` as an abbreviation for `function` (see Function Definition Syntax)
- The `fflush()` built-in function for flushing buffered output (see Input/Output Functions)

See Common Extensions Summary for a full list of the extensions available in his `awk`.

### A.5 Extensions in `gawk` Not in POSIX `awk`

The GNU implementation, `gawk`, adds a large number of features. They can all be disabled with either the --traditional or --posix options (see Command-Line Options).

A number of features have come and gone over the years. This section summarizes the additional features over POSIX `awk` that are in the current version of `gawk`.

- Additional predefined variables:
  - The `ARGIND`, `BINMODE`, `ERRNO`, `FIELDWIDTHS`, `FPAT`, `IGNORECASE`, `LINT`, `PROCINFO`, `RT`, and `TEXTDOMAIN` variables (see Predefined Variables)
- Special files in I/O redirections:
  - The /dev/stdin, /dev/stdout, /dev/stderr, and /dev/fd/*N* special file names (see Special File names in `gawk`)
  - The /inet, /inet4, and /inet6 special files for TCP/IP networking using ‘|&’ to specify which version of the IP protocol to use (see Using `gawk` for Network Programming)
- Changes and/or additions to the language:
  - The ‘\x’ escape sequence (see Escape Sequences)
  - Full support for both POSIX and GNU regexps (see Regular Expressions)
  - The ability for `FS` and for the third argument to `split()` to be null strings (see Making Each Character a Separate Field)
  - The ability for `RS` to be a regexp (see How Input Is Split into Records)
  - The ability to use octal and hexadecimal constants in `awk` program source code (see Octal and Hexadecimal Numbers)
  - The ‘|&’ operator for two-way I/O to a coprocess (see Two-Way Communications with Another Process)
  - Indirect function calls (see Indirect Function Calls)
  - Directories on the command line produce a warning and are skipped (see Directories on the Command Line)
  - Output with `print` and `printf` need not be fatal (see Enabling Nonfatal Output)
  - Namespaces and the use of `::` to designate an identifier within a namespace (see Namespaces in `gawk`).
- New keywords:
  - The `BEGINFILE` and `ENDFILE` special patterns (see The `BEGINFILE` and `ENDFILE` Special Patterns)
  - The `switch` statement (see The `switch` Statement)
- Changes to standard `awk` functions:
  - The optional second argument to `close()` that allows closing one end of a two-way pipe to a coprocess (see Two-Way Communications with Another Process)
  - POSIX compliance for `gsub()` and `sub()` with --posix
  - The `length()` function accepts an array argument and returns the number of elements in the array (see String-Manipulation Functions)
  - The optional third argument to the `match()` function for capturing text-matching subexpressions within a regexp (see String-Manipulation Functions)
  - Positional specifiers in `printf` formats for making translations easier (see Rearranging `printf` Arguments)
  - The `split()` function’s additional optional fourth argument, which is an array to hold the text of the field separators (see String-Manipulation Functions)
- Additional functions only in `gawk`:
  - The `gensub()`, `patsplit()`, and `strtonum()` functions for more powerful text manipulation (see String-Manipulation Functions)
  - The `asort()` and `asorti()` functions for sorting arrays (see Controlling Array Traversal and Array Sorting)
  - The `mktime()`, `systime()`, and `strftime()` functions for working with timestamps (see Time Functions)
  - The `and()`, `compl()`, `lshift()`, `or()`, `rshift()`, and `xor()` functions for bit manipulation (see Bit-Manipulation Functions)
  - The `isarray()` function to check whether a variable is an array, and the more general `typeof()` function (see Getting Type Information)
  - The `mkbool()` function to create a Boolean value (see Generating Boolean Values)
  - The `bindtextdomain()`, `dcgettext()`, and `dcngettext()` functions for internationalization (see Internationalizing `awk` Programs)
- Changes and/or additions in the command-line options:
  - The `AWKPATH` environment variable for specifying a path search for the -f command-line option (see Command-Line Options)
  - The `AWKLIBPATH` environment variable for specifying a path search for the -l command-line option (see Command-Line Options)
  - The -b, -c, -C, -d, -D, -e, -E, -g, -h, -i, -l, -L, -M, -n, -N, -o, -O, -p, -P, -r, -s, -S, -t, and -V short options. Also, the ability to use GNU-style long-named options that start with --, and the --assign, --bignum, --characters-as-bytes, --copyright, --debug, --dump-variables, --exec, --field-separator, --file, --gen-pot, --help, --include, --lint, --lint-old, --load, --non-decimal-data, --optimize, --no-optimize, --posix, --pretty-print, --profile, --re-interval, --sandbox, --source, --traditional, --use-lc-numeric, and --version long options (see Command-Line Options).
- Support for the following obsolete systems was removed from the code and the documentation for `gawk` version 4.0:
  - Amiga
  - Atari
  - BeOS
  - Cray
  - MIPS RiscOS
  - MS-DOS with the Microsoft Compiler
  - MS-Windows with the Microsoft Compiler
  - NeXT
  - SunOS 3.x, Sun 386 (Road Runner)
  - Tandem (non-POSIX)
  - Prestandard VAX C compiler for VAX/VMS
  - GCC for Alpha has not been tested for a while.
- Support for the following obsolete system was removed from the code for `gawk` version 4.1:
  - Ultrix
- Support for the following systems was removed from the code for `gawk` version 4.2:
  - MirBSD
  - GNU/Linux on Alpha
- Support for the following systems was removed from the code for `gawk` version 5.2:
  - OS/2
  - DJGPP
  - VAX/VMS

### A.6 History of `gawk` Features

This section describes the features in `gawk` over and above those in POSIX `awk`, in the order they were added to `gawk`.

Version 2.10 of `gawk` introduced the following features:

- The `AWKPATH` environment variable for specifying a path search for the -f command-line option (see Command-Line Options).
- The `IGNORECASE` variable and its effects (see Case Sensitivity in Matching).
- The /dev/stdin, /dev/stdout, /dev/stderr and /dev/fd/*N* special file names (see Special File names in `gawk`).

Version 2.13 of `gawk` introduced the following features:

- The `FIELDWIDTHS` variable and its effects (see Reading Fixed-Width Data).
- The `systime()` and `strftime()` built-in functions for obtaining and printing timestamps (see Time Functions).
- Additional command-line options (see Command-Line Options):
  - The -W lint option to provide error and portability checking for both the source code and at runtime.
  - The -W compat option to turn off the GNU extensions.
  - The -W posix option for full POSIX compliance.

Version 2.14 of `gawk` introduced the following feature:

- The `next file` statement for skipping to the next data file (see The `nextfile` Statement).

Version 2.15 of `gawk` introduced the following features:

- New variables (see Predefined Variables):
  - `ARGIND`, which tracks the movement of `FILENAME` through `ARGV`.
  - `ERRNO`, which contains the system error message when `getline` returns −1 or `close()` fails.
- The /dev/pid, /dev/ppid, /dev/pgrpid, and /dev/user special file names. These have since been removed.
- The ability to delete all of an array at once with ‘delete *array*’ (see The `delete` Statement).
- Command-line option changes (see Command-Line Options):
  - The ability to use GNU-style long-named options that start with --.
  - The --source option for mixing command-line and library-file source code.

Version 3.0 of `gawk` introduced the following features:

- New or changed variables:
  - `IGNORECASE` changed, now applying to string comparison as well as regexp operations (see Case Sensitivity in Matching).
  - `RT`, which contains the input text that matched `RS` (see How Input Is Split into Records).
- Full support for both POSIX and GNU regexps (see Regular Expressions).
- The `gensub()` function for more powerful text manipulation (see String-Manipulation Functions).
- The `strftime()` function acquired a default time format, allowing it to be called with no arguments (see Time Functions).
- The ability for `FS` and for the third argument to `split()` to be null strings (see Making Each Character a Separate Field).
- The ability for `RS` to be a regexp (see How Input Is Split into Records).
- The `next file` statement became `nextfile` (see The `nextfile` Statement).
- The `fflush()` function from BWK `awk` (then at Bell Laboratories; see Input/Output Functions).
- New command-line options:
  - The --lint-old option to warn about constructs that are not available in the original Version 7 Unix version of `awk` (see Major Changes Between V7 and SVR3.1).
  - The -m option from BWK `awk`. (Brian was still at Bell Laboratories at the time.) This was later removed from both his `awk` and from `gawk`.
  - The --re-interval option to provide interval expressions in regexps (see Regular Expression Operators).
  - The --traditional option was added as a better name for --compat (see Command-Line Options).
- The use of GNU Autoconf to control the configuration process (see Compiling `gawk` for Unix-Like Systems).
- Amiga support. This has since been removed.

Version 3.1 of `gawk` introduced the following features:

- New variables (see Predefined Variables):
  - `BINMODE`, for non-POSIX systems, which allows binary I/O for input and/or output files (see Using `gawk` on PC Operating Systems).
  - `LINT`, which dynamically controls lint warnings.
  - `PROCINFO`, an array for providing process-related information.
  - `TEXTDOMAIN`, for setting an application’s internationalization text domain (see Internationalization with `gawk`).
- The ability to use octal and hexadecimal constants in `awk` program source code (see Octal and Hexadecimal Numbers).
- The ‘|&’ operator for two-way I/O to a coprocess (see Two-Way Communications with Another Process).
- The /inet special files for TCP/IP networking using ‘|&’ (see Using `gawk` for Network Programming).
- The optional second argument to `close()` that allows closing one end of a two-way pipe to a coprocess (see Two-Way Communications with Another Process).
- The optional third argument to the `match()` function for capturing text-matching subexpressions within a regexp (see String-Manipulation Functions).
- Positional specifiers in `printf` formats for making translations easier (see Rearranging `printf` Arguments).
- A number of new built-in functions:
  - The `asort()` and `asorti()` functions for sorting arrays (see Controlling Array Traversal and Array Sorting).
  - The `bindtextdomain()`, `dcgettext()` and `dcngettext()` functions for internationalization (see Internationalizing `awk` Programs).
  - The `extension()` function and the ability to add new built-in functions dynamically. This has seen removed. It was replaced by the new extension mechanism. See Writing Extensions for `gawk`.
  - The `mktime()` function for creating timestamps (see Time Functions).
  - The `and()`, `or()`, `xor()`, `compl()`, `lshift()`, `rshift()`, and `strtonum()` functions (see Bit-Manipulation Functions).
- The support for ‘next file’ as two words was removed completely (see The `nextfile` Statement).
- Additional command-line options (see Command-Line Options):
  - The --dump-variables option to print a list of all global variables.
  - The --exec option, for use in CGI scripts.
  - The --gen-po command-line option and the use of a leading underscore to mark strings that should be translated (see Extracting Marked Strings).
  - The --non-decimal-data option to allow non-decimal input data (see Allowing Nondecimal Input Data).
  - The --profile option and `pgawk`, the profiling version of `gawk`, for producing execution profiles of `awk` programs (see Profiling Your `awk` Programs).
  - The --use-lc-numeric option to force `gawk` to use the locale’s decimal point for parsing input data (see Conversion of Strings and Numbers).
- The use of GNU Automake to help in standardizing the configuration process (see Compiling `gawk` for Unix-Like Systems).
- The use of GNU `gettext` for `gawk`’s own message output (see `gawk` Can Speak Your Language).
- BeOS support. This was later removed.
- Tandem support. This was later removed.
- The Atari port became officially unsupported and was later removed entirely.
- The source code changed to use ISO C standard-style function definitions.
- POSIX compliance for `sub()` and `gsub()` (see More about ‘\’ and ‘&’ with `sub()`, `gsub()`, and `gensub()`).
- The `length()` function was extended to accept an array argument and return the number of elements in the array (see String-Manipulation Functions).
- The `strftime()` function acquired a third argument to enable printing times as UTC (see Time Functions).

Version 4.0 of `gawk` introduced the following features:

- Variable additions:
  - `FPAT`, which allows you to specify a regexp that matches the fields, instead of matching the field separator (see Defining Fields by Content).
  - If `PROCINFO["sorted_in"]` exists, ‘for (iggy in foo)’ loops sort the indices before looping over them. The value of this element provides control over how the indices are sorted before the loop traversal starts (see Using Predefined Array Scanning Orders with `gawk`).
  - `PROCINFO["strftime"]`, which holds the default format for `strftime()` (see Time Functions).
- The special files /dev/pid, /dev/ppid, /dev/pgrpid and /dev/user were removed.
- Support for IPv6 was added via the /inet6 special file. /inet4 forces IPv4 and /inet chooses the system default, which is probably IPv4 (see Using `gawk` for Network Programming).
- The use of ‘\s’ and ‘\S’ escape sequences in regular expressions (see `gawk`-Specific Regexp Operators).
- Interval expressions became part of default regular expressions (see Regular Expression Operators).
- POSIX character classes work even with --traditional (see Regular Expression Operators).
- `break` and `continue` became invalid outside a loop, even with --traditional (see The `break` Statement, and also see The `continue` Statement).
- `fflush()`, `nextfile`, and ‘delete *array*’ are allowed if --posix or --traditional, since they are all now part of POSIX.
- An optional third argument to `asort()` and `asorti()`, specifying how to sort (see String-Manipulation Functions).
- The behavior of `fflush()` changed to match BWK `awk` and for POSIX; now both ‘fflush()’ and ‘fflush("")’ flush all open output redirections (see Input/Output Functions).
- The `isarray()` function which distinguishes if an item is an array or not, to make it possible to traverse arrays of arrays (see Getting Type Information).
- The `patsplit()` function which gives the same capability as `FPAT`, for splitting (see String-Manipulation Functions).
- An optional fourth argument to the `split()` function, which is an array to hold the values of the separators (see String-Manipulation Functions).
- Arrays of arrays (see Arrays of Arrays).
- The `BEGINFILE` and `ENDFILE` special patterns (see The `BEGINFILE` and `ENDFILE` Special Patterns).
- Indirect function calls (see Indirect Function Calls).
- `switch` / `case` are enabled by default (see The `switch` Statement).
- Command-line option changes (see Command-Line Options):
  - The -b and --characters-as-bytes options which prevent `gawk` from treating input as a multibyte string.
  - The redundant --compat, --copyleft, and --usage long options were removed.
  - The --gen-po option was finally renamed to the correct --gen-pot.
  - The --sandbox option which disables certain features.
  - All long options acquired corresponding short options, for use in ‘#!’ scripts.
- Directories named on the command line now produce a warning, not a fatal error, unless --posix or --traditional are used (see Directories on the Command Line).
- The `gawk` internals were rewritten, bringing the `dgawk` debugger and possibly improved performance (see Debugging `awk` Programs).
- Per the GNU Coding Standards, dynamic extensions must now define a global symbol indicating that they are GPL-compatible (see Extension Licensing).
- In POSIX mode, string comparisons use `strcoll()` / `wcscoll()` (see String Comparison Based on Locale Collating Order).
- The option for raw sockets was removed, since it was never implemented (see Using `gawk` for Network Programming).
- Ranges of the form ‘[d-h]’ are treated as if they were in the C locale, no matter what kind of regexp is being used, and even if --posix (see Regexp Ranges and Locales: A Long Sad Story).
- Support was removed for the following systems:
  - Atari
  - Amiga
  - BeOS
  - Cray
  - MIPS RiscOS
  - MS-DOS with the Microsoft Compiler
  - MS-Windows with the Microsoft Compiler
  - NeXT
  - SunOS 3.x, Sun 386 (Road Runner)
  - Tandem (non-POSIX)
  - Prestandard VAX C compiler for VAX/VMS

Version 4.1 of `gawk` introduced the following features:

- Three new arrays: `SYMTAB`, `FUNCTAB`, and `PROCINFO["identifiers"]` (see Built-in Variables That Convey Information).
- The three executables `gawk`, `pgawk`, and `dgawk`, were merged into one, named just `gawk`. As a result the command-line options changed.
- Command-line option changes (see Command-Line Options):
  - The -D option invokes the debugger.
  - The -i and --include options load `awk` library files.
  - The -l and --load options load compiled dynamic extensions.
  - The -M and --bignum options enable MPFR.
  - The -o option only does pretty-printing.
  - The -p option is used for profiling.
  - The -R option was removed.
- Support for high precision arithmetic with MPFR (see Arithmetic and Arbitrary-Precision Arithmetic with `gawk`).
- The `and()`, `or()` and `xor()` functions changed to allow any number of arguments, with a minimum of two (see Bit-Manipulation Functions).
- The dynamic extension interface was completely redone (see Writing Extensions for `gawk`).
- Redirected `getline` became allowed inside `BEGINFILE` and `ENDFILE` (see The `BEGINFILE` and `ENDFILE` Special Patterns).
- Support for nonfatal I/O (see Enabling Nonfatal Output).
- The `where` command was added to the debugger (see Working with the Stack).
- Support for Ultrix was removed.

Version 4.2 of `gawk` introduced the following changes:

- Changes to `ENVIRON` are reflected into `gawk`’s environment and that of programs that it runs. See Built-in Variables That Convey Information.
- `FIELDWIDTHS` was enhanced to allow skipping characters before assigning a value to a field (see Defining Fields by Content).
- The `PROCINFO["argv"]` array. See Built-in Variables That Convey Information.
- The maximum number of hexadecimal digits in ‘\x’ escapes is now two. See Escape Sequences.
- Strongly typed regexp constants of the form ‘@/…/’ (see Strongly Typed Regexp Constants).
- The bitwise functions changed, making negative arguments into a fatal error (see Bit-Manipulation Functions).
- The `mktime()` function now accepts an optional second argument (see Time Functions).
- The `typeof()` function (see Getting Type Information).
- Optimizations are enabled by default. Use -s / --no-optimize to disable optimizations.
- For many years, POSIX specified that default field splitting only allowed spaces and tabs to separate fields, and this was how `gawk` behaved with --posix. As of 2013, the standard restored historical behavior, and now default field splitting with --posix also allows newlines to separate fields.
- Nonfatal output with `print` and `printf`. See Enabling Nonfatal Output.
- Retryable I/O via `PROCINFO[*input-file*, "RETRY"]`; (see Retrying Reads After Certain Input Errors).
- Changes to the pretty-printer (see Profiling Your `awk` Programs):
  - The --pretty-print option no longer runs the `awk` program too.
  - Comments in the source program are preserved and placed into the output file.
  - Explicit parentheses for expressions in the input are preserved in the generated output.
- Improvements to the extension API (see Writing Extensions for `gawk`):
  - The `get_file()` function to access open redirections.
  - The `nonfatal()` function for generating nonfatal error messages.
  - Support for GMP and MPFR values.
  - Input parsers can now override the default field parsing mechanism by specifying explicit locations.
- Shell startup files are supplied with the distribution and installed by ‘make install’ (see Shell Startup Files).
- The `igawk` program and its manual page are no longer installed when `gawk` is built. See An Easy Way to Use Library Functions.
- Support for MirBSD was removed.
- Support for GNU/Linux on Alpha was removed.

Version 5.0 added the following features:

- The `PROCINFO["platform"]` array element, which allows you to write code that takes the operating system / platform into account.

Version 5.1 was created to release `gawk` with a correct major version number for the API. This was overlooked for version 5.0, unfortunately. It added the following features:

- The index for this manual was completely reworked.
- Support was added for MSYS2.
- `asort()` and `asorti()` were changed to allow `FUNCTAB` and `SYMTAB` as the first argument if a second destination array is supplied (see String-Manipulation Functions).
- The -I/--trace options were added to print a trace of the byte codes as they execute (see Command-Line Options).
- `$0` and the fields are now cleared before starting a `BEGINFILE` rule (see The `BEGINFILE` and `ENDFILE` Special Patterns).
- Several example programs in the manual were updated to their modern POSIX equivalents.
- The “no effect” lint warnings from --lint were fixed up and now behave more sanely (see Command-Line Options).
- Handling of Infinity and NaN values were improved. See Other Stuff to Know, and also see Standards Versus Existing Practice.

Version 5.2 added the following features:

- The `mkbool()` built-in function (see Generating Boolean Values).
- Interval expressions in regular expressions are enabled by default (see Some Notes On Interval Expressions).
- Support for the FNV1-A hash algorithm for its hash function (see Other Environment Variables).
- The `gawkbug` script for reporting bugs (see Submitting Bug Reports).
- Terence Kelly’s persistent memory allocator (PMA) was added, allowing the use of persistent data on certain systems (see Preserving Data Between Runs).
- `PROCINFO["pma"]` exists if the PMA allocator is compiled in (see Built-in Variables That Convey Information).

Version 5.3 added the following features:

- Comma separated value (CSV) field splitting and the --csv command-line option (see Working With Comma Separated Value Files).
- `PROCINFO["CSV"]` exists if `gawk` was invoked with --csv (see Built-in Variables That Convey Information).
- The `do_csv` API information variable (see Informational Variables).
- The ability to make `gawk` buffer output to pipes (see Speeding Up Pipe Output).
- The ‘\u’ escape sequence (see Escape Sequences).
- Support for OpenVMS 9.2-2 x86_64 (at version 5.3.1).
- The need for GNU `libsigsegv` was removed from `gawk`. The value-add was never very much and it caused problems in some environments.
- Support for OSF/1 was removed.

Version 5.4 added the following features:

- The --enable-O3 option to `configure` was added (see Additional Configuration Options).
- Use of the new MinRX regular expression matcher as the default matching engine (see Selecting the Regexp Matching Engine). This brings full POSIX compliance to `gawk`’s regular expression matching.
- The `@nsinclude` directive for including files without resetting the namespace to ‘awk’ (see Including A File Without Changing The Namespace).
- The ability to call `length()` on an array is no longer an extension, as it became part of POSIX in 2004 (see String-Manipulation Functions).
- Persistent memory was enabled on FreeBSD, MidnightBSD, NetBSD and OpenBSD (see Preserving Data Between Runs).
- Hexadecimal floating-point values may be used in program source code, with the `strtonum()` function, and with the --non-decimal-data option (see Allowing Nondecimal Input Data).
- Support for UDP in `gawk`’s networking was marked as obsolete (see Using `gawk` for Network Programming).
- The MinGW port of `gawk` for MS-Windows gained support for UTF-8 encoding of non-ASCII text when codepage 65001 is used by the Windows terminal (see Using `gawk` on PC Operating Systems).
- Support was added for OpenVMS 9 on x86_64 hardware, and support for OpenVMS 8 on Alpha and Itanium was updated.

### A.7 Common Extensions Summary

The following table summarizes the common extensions supported by `gawk`, Brian Kernighan’s `awk`, and `mawk`, the three most widely used freely available versions of `awk` (see Other Freely Available `awk` Implementations).

| Feature | BWK `awk` | `mawk` | `gawk` | Now standard |
|---|---|---|---|---|
| `**` and `**=` operators | X |   | X |   |
| ‘\x’ escape sequence | X | X | X |   |
| ‘\u’ escape sequence | X |   | X |   |
| /dev/stdin special file | X | X | X |   |
| /dev/stdout special file | X | X | X |   |
| /dev/stderr special file | X | X | X |   |
| `BINMODE` variable |   | X | X |   |
| CSV support | X |   | X |   |
| `FS` as null string | X | X | X |   |
| `delete` without subscript | X | X | X | X |
| `fflush()` function | X | X | X | X |
| `func` keyword | X |   | X |   |
| `nextfile` statement | X | X | X | X |
| `RS` as regexp | X | X | X |   |
| Time-related functions |   | X | X |   |

### A.8 Regexp Ranges and Locales: A Long Sad Story

This section describes the confusing history of ranges within regular expressions and their interactions with locales, and how this affected different versions of `gawk`.

The original Unix tools that worked with regular expressions defined character ranges (such as ‘[a-z]’) to match any character between the first character in the range and the last character in the range, inclusive. Ordering was based on the numeric value of each character in the machine’s native character set. Thus, on ASCII-based systems, ‘[a-z]’ matched all the lowercase letters, and only the lowercase letters, as the numeric values for the letters from ‘a’ through ‘z’ were contiguous. (On an EBCDIC system, the range ‘[a-z]’ includes additional nonalphabetic characters as well.)

Almost all introductory Unix literature explained range expressions as working in this fashion, and in particular, would teach that the “correct” way to match lowercase letters was with ‘[a-z]’, and that ‘[A-Z]’ was the “correct” way to match uppercase letters. And indeed, this was true.118

The 1992 POSIX standard introduced the idea of locales (see Where You Are Makes a Difference). Because many locales include other letters besides the plain 26 letters of the English alphabet, the POSIX standard added character classes (see Using Bracket Expressions) as a way to match different kinds of characters besides the traditional ones in the ASCII character set.

However, the standard *changed* the interpretation of range expressions. In the `"C"` and `"POSIX"` locales, a range expression like ‘[a-dx-z]’ is still equivalent to ‘[abcdxyz]’, as in ASCII. But outside those locales, the ordering was defined to be based on *collation order*.

What does that mean? In many locales, ‘A’ and ‘a’ are both less than ‘B’. In other words, these locales sort characters in dictionary order, and ‘[a-dx-z]’ is typically not equivalent to ‘[abcdxyz]’; instead, it might be equivalent to ‘[ABCXYabcdxyz]’, for example.

This point needs to be emphasized: much literature teaches that you should use ‘[a-z]’ to match a lowercase character. But on systems with non-ASCII locales, this also matches all of the uppercase characters except ‘A’ or ‘Z’! This was a continuous cause of confusion, even well into the twenty-first century.

To demonstrate these issues, the following example uses the `sub()` function, which does text replacement (see String-Manipulation Functions). Here, the intent is to remove trailing uppercase characters:

```
$ echo something1234abc | gawk-3.1.8 '{ sub("[A-Z]*$", ""); print }'
-| something1234a
```

This output is unexpected, as the ‘bc’ at the end of ‘something1234abc’ should not normally match ‘[A-Z]*’. This result is due to the locale setting (and thus you may not see it on your system).

Similar considerations apply to other ranges. For example, ‘["-/]’ is perfectly valid in ASCII, but is not valid in many Unicode locales, such as `en_US.UTF-8`.

Early versions of `gawk` used regexp matching code that was not locale-aware, so ranges had their traditional interpretation.

When `gawk` switched to using locale-aware regexp matchers, the problems began; especially as both GNU/Linux and commercial Unix vendors started implementing non-ASCII locales, *and making them the default*. Perhaps the most frequently asked question became something like, “Why does ‘[A-Z]’ match lowercase letters?!?”

This situation existed for close to 10 years, if not more, and the `gawk` maintainer grew weary of trying to explain that `gawk` was being nicely standards-compliant, and that the issue was in the user’s locale. During the development of version 4.0, he modified `gawk` to always treat ranges in the original, pre-POSIX fashion, unless --posix was used (see Command-Line Options).119

Fortunately, shortly before the final release of `gawk` 4.0, the maintainer learned that the 2008 standard had changed the definition of ranges, such that outside the `"C"` and `"POSIX"` locales, the meaning of range expressions was *undefined*.120

By using this lovely technical term, the standard gives license to implementers to implement ranges in whatever way they choose. The `gawk` maintainer chose to apply the pre-POSIX meaning both with the default regexp matching and when --traditional or --posix are used. In all cases `gawk` remains POSIX-compliant.

### A.9 Major Contributors to `gawk`

> *Always give credit where credit is due.*

—

Anonymous

This section names the major contributors to `gawk` and/or this Web page, in approximate chronological order:

- Dr. Alfred V. Aho, Dr. Peter J. Weinberger, and Dr. Brian W. Kernighan, all of Bell Laboratories, designed and implemented Unix `awk`, from which `gawk` gets the majority of its feature set.
- Paul Rubin did the initial design and implementation in 1986, and wrote the first draft (around 40 pages) of this Web page.
- Jay Fenlason finished the initial implementation.
- Diane Close revised the first draft of this Web page, bringing it to around 90 pages.
- Richard Stallman helped finish the implementation and the initial draft of this Web page. He is also the founder of the FSF and the GNU Project.
- John Woods contributed parts of the code (mostly fixes) in the initial version of `gawk`.
- In 1988, David Trueman took over primary maintenance of `gawk`, making it compatible with “new” `awk`, and greatly improving its performance.
- Conrad Kwok, Scott Garfinkle, and Kent Williams did the initial ports to MS-DOS with various versions of MSC.
- Pat Rankin provided the VMS port and its documentation.
- Hal Peterson provided help in porting `gawk` to Cray systems. (This is no longer supported.)
- Kai Uwe Rommel provided the initial port to OS/2 and its documentation.
- Michal Jaegermann provided the port to Atari systems and its documentation. (This port is no longer supported.) He continues to provide portability checking, and has done a lot of work to make sure `gawk` works on non-32-bit systems.
- Fred Fish provided the port to Amiga systems and its documentation. (With Fred’s sad passing, this is no longer supported.)
- Scott Deifik formerly maintained the MS-DOS port using DJGPP.
- Eli Zaretskii currently maintains the MS-Windows port using MinGW.
- Juan Grigera provided a port to Windows32 systems. (This is no longer supported.)
- For many years, Dr. Darrel Hankerson acted as coordinator for the various ports to different PC platforms and created binary distributions for various PC operating systems. He was also instrumental in keeping the documentation up to date for the various PC platforms.
- Christos Zoulas provided the `extension()` built-in function for dynamically adding new functions. (This was obsoleted at `gawk` 4.1.)
- Jürgen Kahrs contributed the initial version of the TCP/IP networking code and documentation, and motivated the inclusion of the ‘|&’ operator.
- Stephen Davies provided the initial port to Tandem systems and its documentation. (However, this is no longer supported.) He was also instrumental in the initial work to integrate the byte-code internals into the `gawk` code base. Additionally, he did most of the work enabling the pretty-printer to preserve and output comments.
- Matthew Woehlke provided improvements for Tandem’s POSIX-compliant systems.
- Martin Brown provided the port to BeOS and its documentation. (This is no longer supported.)
- Arno Peters did the initial work to convert `gawk` to use GNU Automake and GNU `gettext`.
- Alan J. Broder provided the initial version of the `asort()` function as well as the code for the optional third argument to the `match()` function.
- Andreas Buening updated the `gawk` port for OS/2.
- Isamu Hasegawa, of IBM in Japan, contributed support for multibyte characters.
- Michael Benzinger contributed the initial code for `switch` statements.
- Patrick T.J. McPhee contributed the code for dynamic loading in Windows32 environments. (This is no longer supported.)
- Anders Wallin helped keep the VMS port going for several years.
- Assaf Gordon contributed the initial code to implement the --sandbox option.
- John Haque made the following contributions:
  - The modifications to convert `gawk` into a byte-code interpreter, including the debugger
  - The addition of true arrays of arrays
  - The additional modifications for support of arbitrary-precision arithmetic
  - The initial text of Arithmetic and Arbitrary-Precision Arithmetic with `gawk`
  - The work to merge the three versions of `gawk` into one, for the 4.1 release
  - Improved array internals for arrays indexed by integers
  - The improved array sorting features were also driven by John, together with Pat Rankin
- Panos Papadopoulos contributed the original text for Including Other Files into Your Program.
- Efraim Yawitz contributed the original text for Debugging `awk` Programs.
- John Naman contributed the original text for A Note On Shadowed Variables.
- Stuart Ferguson reworked the text in Defining Fields by Content.
- The development of the extension API first released with `gawk` 4.1 was driven primarily by Arnold Robbins and Andrew Schorr, with notable contributions from the rest of the development team.
- John Malmberg contributed significant improvements to the OpenVMS port and the related documentation.
- Antonio Giovanni Colombo rewrote a number of examples in the early chapters that were severely dated, for which I am incredibly grateful. He also provided and maintains the Italian translation.
- Marco Curreli, together with Antonio Colombo, translated this Web page into Italian. It is included in the `gawk` distribution.
- Juan Manuel Guerrero took over maintenance of the DJGPP port.
- “Jannick” provided support for MSYS2.
- Arnold Robbins has been working on `gawk` since 1988, at first helping David Trueman, and as the primary maintainer since around 1994.

### A.10 Summary

- The `awk` language has evolved over time. The first release was with V7 Unix, circa 1978. In 1987, for System V Release 3.1, major additions, including user-defined functions, were made to the language. Additional changes were made for System V Release 4, in 1989. Since then, further minor changes have happened under the auspices of the POSIX standard.
- Brian Kernighan’s `awk` provides a small number of extensions that are implemented in common with other versions of `awk`.
- `gawk` provides a large number of extensions over POSIX `awk`. They can be disabled with either the --traditional or --posix options.
- The interaction of POSIX locales and regexp matching in `gawk` has been confusing over the years. Today, `gawk` implements Rational Range Interpretation, where ranges of the form ‘[a-z]’ match *only* the characters numerically between ‘a’ through ‘z’ in the machine’s native character set. Usually this is ASCII, but it can be EBCDIC on IBM S/390 systems.
- Many people have contributed to `gawk` development over the years. We hope that the list provided in this chapter is complete and gives the appropriate credit where credit is due.
