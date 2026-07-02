---
title: "printf"
source: https://en.wikipedia.org/wiki/Printf_format_string
domain: fmt-cpp-lib
license: CC-BY-SA-4.0
tags: fmt library, cpp string formatting, fmt format spec, fmt print library
fetched: 2026-07-02
---

# printf

(Redirected from

Printf format string

)

**printf** is a C standard library function and is also a Linux terminal *(shell)* command that formats text and writes it to standard output. The function accepts a format C-string argument and a variable number of value arguments that the function serializes per the format string. Mismatch between the format specifiers and count and type of values results in undefined behavior, and the program might crash or vulnerabilities may arise.

The format string is encoded as a template language consisting of verbatim text and *format specifiers* that each specify how to serialize a value. As the format string is processed left-to-right, a subsequent value is used for each format specifier found. A format specifier starts with a `%` character and has one or more following characters that specify how to serialize a value.

The standard library provides other, similar functions that form a family of *printf-like* functions. The functions share the same formatting capabilities but provide different behavior such as output to a different destination or safety measures that limit exposure to vulnerabilities. Functions of the printf-family have been implemented in other computer programming contexts (i.e., programming languages) with the same or similar syntax and semantics.

The scanf() C standard library function complements printf by providing formatted input (a.k.a. lexing, a.k.a. parsing) via a similar format string syntax.

The name, *printf*, is short for *print formatted* where *print* refers to output to a printer although the function is not limited to printer output. Today, print refers to output to any text-based environment such as a terminal or a file.

## History

### 1950s: Fortran

Early programming languages like Fortran used special statements with different syntax from other calculations to build formatting descriptions. In this example, the format is specified on line 601, and the `PRINT` command refers to it by line number:

```mw
      PRINT 601, IA, IB, AREA
 601  FORMAT (4H A= ,I5,5H  B= ,I5,8H  AREA= ,F10.2, 13H SQUARE UNITS)
```

Hereby:

- `4H` indicates a string of 4 characters `" A= "` (`H` means Hollerith Field);
- `I5` indicates an integer field of width 5;
- `F10.2` indicates a floating-point field of width 10 with 2 digits after the decimal point.

An output with input arguments `100`, `200`, and `1500.25` might look like this:

```mw
 A=   100  B=   200  AREA=    1500.25 SQUARE UNITS
```

### 1960s: BCPL and ALGOL 68

In 1967, BCPL appeared. Its library included the `writef` routine which looked like any other function call. An example application looks like this:

```mw
WRITEF("%I2-QUEENS PROBLEM HAS %I5 SOLUTIONS*N", NUMQUEENS, COUNT)
```

Hereby:

- `%I2` indicates an integer of width 2 (the order of the format specification's field width and type is reversed compared to C's `printf`);
- `%I5` indicates an integer of width 5;
- `*N` is a BCPL *language* escape sequence representing a newline character (for which C uses the escape sequence `\n`).

ALGOL 68 also had a function api, but used special syntax for the format:

```mw
printf(($"Color "g", number1 "6d,", number2 "4zd,", hex "16r2d,", float "-d.2d,", unsigned value"-3d"."l$,
         "red", 123456, 89, BIN 255, 3.14, 250));
```

Using normal function syntax for the printing simplifies the language, and allows the printing to be implemented in the language itself. In most newer languages of that era I/O is not part of the syntax. However the format was usually not checked to see if it matched the type (or even the number) of values being printed.

### 1970s: C

In 1973, `printf` was included as a C standard library routine as part of Version 4 Unix.

### 1990s: Shell command

In 1990, the `printf` shell command, modeled after the C standard library function, was included with 4.3BSD-Reno. In 1991, a `printf` command was included with GNU shellutils (now part of GNU Core Utilities) and the syntax (options, arguments, etc.) of this "*shell command*" are different from the *C-Language function* e.g.: the *"format section"* does not use the *positional arguments* with a "$" symbol (n$) in the same way as `printf()` function:

```mw
str="AA BB CC" # simple string with 3 fields
set -- $str # convert fields to positional parameters
printf "%s " $2 $3 $1; echo # in C printf() uses 2$ 3$..
# prints: BB CC AA
```

### 2000s: Java

In 2004, Java 5.0 (1.5) released, which extended the class `java.io.PrintStream`, adding a method named `printf()` which functions analogously to `printf()` in C. Thus to print a formatted string to the standard output stream, one uses `System.out.printf()`. Java further introduced the method `format` to its string class `java.lang.String`.

### 2000s: -Wformat safety

The need to do something about the range of problems resulting from lack of type safety has prompted attempts to make compilers `printf`-aware.

The -Wformat option of GNU Compiler Collection (GCC) allows compile time checks to `printf` calls, enabling the compiler to detect a subset of invalid calls (and issue either a warning or an error, terminating compilation, as set by other flags).

Because the compiler inspects `printf` format specifiers, this feature effectively extends static analysis in C to include formatting aspects.

### 2020s: std::print

C++ added input/output support using the << operator to avoid safety issues of printf. This used the type of the arguments to choose which code to execute to print them, avoiding the crashes that are possible with format strings. However, the syntax can be verbose (especially for setting options like precision), and printf remains available in C++ and is often used instead.

C++20 added a new API which uses a string consisting of verbatim text and placeholders followed by the values to print. The format string uses curly braces instead of percent signs, based on the syntax used in the Python standard library:

std

::

format

(

"The hex value of {} is {:x}."

,

name

,

value

)

The recommended implementation is from Victor Zverovich's *fmtlib* which at compile time converts the string and argument types into an optimized formatting object, this is type-safe and syntax errors are detected at compile time. C++23 introduced the functions `std::print()` and `std::println()` which combined formatting and outputting, and is therefore a functional replacement for `printf()`. It is possible to make a translator from a printf %-string to the same formatting object and this could produce a type-safe printf, but this was also not added to the spec. No analogous scanf modernization has been introduced, though one has been proposed based on *scnlib*.

These functions (plus `std::to_chars`) can print floating point accurately using the least number of trailing digits possible, an ability long missing from printf. Another useful feature is that they ignore the locale.

## Format specifier

Formatting of a value is specified as markup in the format string. For example, the following outputs `Your age is` and then the value of the variable *age* in decimal format.

```mw
printf("Your age is %d", age);
```

### Syntax

The syntax for a format specifier is:

```
%[parameter][flags][width][.precision][length]type
```

### Parameter field

The parameter field is optional. If included, then matching specifiers to values is *not* sequential. The numeric value n selects the n-th value parameter. This is a POSIX extension, not C99.

| Text | Description |
|---|---|
| *n*$ | *n* is the index of the value parameter to serialize using this format specifier |

This field allows for using the same value multiple times in a format string instead of having to pass the value multiple times. If a specifier includes this field, then subsequent specifiers must also.

For example,

```mw
printf("%2$d %2$#x; %1$d %1$#x",16,17);
```

outputs: 17 0x11; 16 0x10

This field is very useful for localizing messages to different natural languages that use different word orders.

In the Windows API, support for this feature is via a different function, `printf_p`.

### Flags field

The flags field can be zero or more of (in any order):

| Text | Description |
|---|---|
| - | Left-align the output of this placeholder; default is to right-align the output |
| + | Prepends a plus sign for a positive value; by default a positive value does not have a prefix |
| (space) | Prepends a space character for a positive value; ignored if the + flag exists; by default a positive value does not have a prefix |
| 0 | When the 'width' option is specified, prepends zeros instead of spaces for numeric types; for example, `printf("%4X",3)` produces " 3", while `printf("%04X",3);` produces "0003" |
| ' | The integer or exponent of a decimal has the thousands grouping separator applied |
| # | Alternate form: For g and G types, trailing zeros are not removed For f, F, e, E, g, G types, the output always contains a decimal point For o, x, X types, the text 0, 0x, 0X, respectively, is prepended to non-zero numbers |

### Width field

The width field specifies the *minimum* number of characters to output. If the value can be represented in fewer characters, then the value is left-padded with spaces so that output is the number of characters specified. If the value requires more characters, then the output is longer than the specified width. A value is never truncated.

For example, `printf("%3d", 12);` specifies a width of 3 and outputs 12 with a space on the left to output 3 characters. The call `printf("%3d", 1234);` outputs 1234 which is 4 characters long since that is the minimum width for that value even though the width specified is 3.

If the width field is omitted, the output is the minimum number of characters for the value.

If the field is specified as `*`, then the width value is read from the list of values in the call. For example, `printf("%*d", 3, 10);` outputs 10 (<space>10) where the second parameter, `3`, is the width (matches with `*`) and `10` is the value to serialize (matches with `d`).

Though not part of the width field, a leading zero is interpreted as the zero-padding flag mentioned above, and a negative value is treated as the positive value in conjunction with the left-alignment `-` flag also mentioned above.

The width field can be used to format values as a table (tabulated output). But, columns do not align if any value is larger than fits in the width specified. For example, notice that the last line value (1234) does not fit in the first column of width 3 and therefore the column is not aligned.

```mw
  1   1
 12  12
123 123
1234 123
```

### Precision field

The precision field usually specifies a *maximum* limit of the output, as set by the formatting type. For floating-point numeric types, it specifies the number of digits to the right of the decimal point to which the output should be rounded; for `%g` and `%G` it specifies the total number of significant figures (before and after the decimal, not including leading or trailing zeroes) to round to. For the string type, it limits the number of characters that should be output, after which the string is truncated.

The precision field may be omitted, or a numeric integer value, or a dynamic value when passed as another argument when indicated by an asterisk (`*`). For example, `printf("%.*s", 3, "abcdef");` outputs abc.

### Length field

The length field can be omitted or be any of:

| Text | Description |
|---|---|
| hh | For integer types, causes printf to expect an int-sized integer argument which was promoted from a char. |
| h | For integer types, causes printf to expect an int-sized integer argument which was promoted from a short. |
| l | For integer types, causes printf to expect a long-sized integer argument. For floating-point types, this is ignored. float arguments are always promoted to double when used in a varargs call. |
| ll | For integer types, causes printf to expect a long long-sized integer argument. |
| L | For floating-point types, causes printf to expect a long double argument. |
| z | For integer types, causes printf to expect a size_t-sized integer argument. |
| j | For integer types, causes printf to expect a intmax_t-sized integer argument. |
| t | For integer types, causes printf to expect a ptrdiff_t-sized integer argument. |

Platform-specific length options came to exist prior to widespread use of the ISO C99 extensions, including:

| Text | Description | *Commonly found platforms* |
|---|---|---|
| I | For signed integer types, causes printf to expect ptrdiff_t-sized integer argument; for unsigned integer types, causes printf to expect size_t-sized integer argument | Win32/Win64 |
| I32 | For integer types, causes printf to expect a 32-bit (double word) integer argument | Win32/Win64 |
| I64 | For integer types, causes printf to expect a 64-bit (quad word) integer argument | Win32/Win64 |
| q | For integer types, causes printf to expect a 64-bit (quad word) integer argument | BSD |

ISO C99 includes the `inttypes.h` header file that includes a number of macros for cross-platform `printf` coding. For example: `printf("%" PRId64, t);` specifies decimal format for a 64-bit signed integer. Since the macros evaluate to a string literal, and the compiler concatenates adjacent string literals, the expression `"%" PRId64` compiles to a single string.

Macros include:

| Macro | Description |
|---|---|
| PRId32 | Typically equivalent to I32d (*Win32/Win64*) or d |
| PRId64 | Typically equivalent to I64d (*Win32/Win64*), lld (*32-bit platforms*) or ld (*64-bit platforms*) |
| PRIi32 | Typically equivalent to I32i (*Win32/Win64*) or i |
| PRIi64 | Typically equivalent to I64i (*Win32/Win64*), lli (*32-bit platforms*) or li (*64-bit platforms*) |
| PRIu32 | Typically equivalent to I32u (*Win32/Win64*) or u |
| PRIu64 | Typically equivalent to I64u (*Win32/Win64*), llu (*32-bit platforms*) or lu (*64-bit platforms*) |
| PRIx32 | Typically equivalent to I32x (*Win32/Win64*) or x |
| PRIx64 | Typically equivalent to I64x (*Win32/Win64*), llx (*32-bit platforms*) or lx (*64-bit platforms*) |

### Type field

The type field can be any of:

| Text | Description |
|---|---|
| % | Output a literal % character; does not accept flags, width, precision or length fields |
| d, i | (signed) int formatted as decimal; %d and %i are synonymous except when used with `scanf` |
| u | unsigned int formatted as decimal. |
| f, F | double formatted as fixed-point; f and F only differs in how the strings for an infinite number or NaN are printed (inf, infinity and nan for f; INF, INFINITY and NAN for F) |
| e, E | double formatted as in exponential notation *d*.*ddd*e±*dd*; E results in E rather than e to introduce the exponent; the exponent always contains at least two digits; if the value is zero, the exponent is 00; in Windows, the exponent contains three digits by default, e.g. 1.5e002, but this can be altered by Microsoft-specific `_set_output_format` function |
| g, G | double formatted as either fixed-point or exponential notation, whichever is more appropriate for its magnitude; g uses lower-case letters, G uses upper-case letters; this type differs slightly from fixed-point notation in that insignificant zeroes to the right of the decimal point are not included, and that the precision field specifies the total number of significant digits rather than the digits after the decimal; the decimal point is not included on whole numbers |
| x, X | unsigned int formatted as hexadecimal; x uses lower-case letters and X uses upper-case |
| o | unsigned int formatted as octal |
| s | null-terminated string |
| c | char |
| p | Pointer formatted in an implementation-defined way |
| a, A | double in hexadecimal notation, starting with 0x or 0X. a uses lower-case letters, A uses upper-case letters |
| n | Outputs nothing but writes the number of characters written so far into an integer pointer parameter; in Java this prints a newline |

### Custom data type formatting

A common way to handle formatting with a custom data type is to format the custom data type value into a string, then use the `%s` specifier to include the serialized value in a larger message.

Some printf-like functions allow extensions to the escape-character-based mini-language, thus allowing the programmer to use a specific formatting function for non-builtin types. One is the (now deprecated) glibc's `register_printf_function()`. However, it is rarely used due to the fact that it conflicts with static format string checking. Another is Vstr custom formatters, which allows adding multi-character format names.

Some applications (like the Apache HTTP Server) include their own printf-like function, and embed extensions into it. However these all tend to have the same problems that `register_printf_function()` has.

The Linux kernel `printk` function supports a number of ways to display kernel structures using the generic `%p` specification, by *appending* additional format characters. For example, `%pI4` prints an IPv4 address in dotted-decimal form. This allows static format string checking (of the `%p` portion) at the expense of full compatibility with normal printf.

## Vulnerabilities

### Format string attack

Extra value arguments are ignored, but if the format string has more format specifiers than value arguments passed, the behavior is undefined. For some C compilers, an extra format specifier results in consuming a value even though there isn't one which allows the format string attack. Generally, for C, arguments are passed on the stack. If too few arguments are passed, then printf can read past the end of the stack frame, thus allowing an attacker to read the stack.

Some compilers, like the GNU Compiler Collection, will statically check the format strings of printf-like functions and warn about problems (when using the flags -Wall or -Wformat). GCC will also warn about user-defined printf-style functions if the non-standard "format" `__attribute__` is applied to the function.

### Uncontrolled format string exploit

The format string is often a string literal, which allows static analysis of the function call. However, the format string can be the value of a variable, which allows for dynamic formatting but also a security vulnerability known as an uncontrolled format string exploit.

### Memory write

Although an output function on the surface, `printf` allows writing to a memory location specified by an argument via `%n`. This functionality can be used for code injection attacks without violating control-flow integrity.

The `%n` format specifier also makes `printf` accidentally Turing-complete even with a well-formed set of arguments. A game of tic-tac-toe written in the format string is a winner of the 27th IOCCC.

### Family

Variants of `printf` in the C standard library include: `fprintf` outputs to a file instead of standard output.

`sprintf` writes to a string buffer instead of standard output.

`snprintf` provides a level of safety over `sprintf` since the caller provides a length *n* that is the length of the output buffer in bytes (including space for the trailing null character).

`asprintf` provides for safety by accepting a string handle (`char**`) argument. The function allocates a buffer of sufficient size to contain the formatted text and outputs the buffer via the handle.

For each function of the family, including printf, there is also a variant that accepts a single `va_list` argument rather than a variable list of arguments. Typically, these variants start with "v". For example: `vprintf`, `vfprintf`, `vsprintf`.

Generally, printf-like functions return the number of bytes output or -1 to indicate failure.

### Other contexts

The following list includes notable programming languages that provide (directly or via a standard library) functioning that is the same or similar to the C printf-like functions. Excluded are languages that use format strings that deviate from the style in this article (such as AMPL and Elixir), languages that inherit their implementation from the Java virtual machine (JVM) or other environment (such as Clojure and Scala), and languages that do not have a standard native printf implementation but have external libraries which emulate printf behavior (such as JavaScript).

- awk
- C
- C++
- D
- F#
- G
- GNU MathProg
- GNU Octave
- Go
- Haskell
- J
- Java (since version 1.5) and JVM languages
- Julia (via Printf standard library)
- Lua (`string.format`)
- Maple
- MATLAB
- Max (via the `sprintf` object)
- Objective-C
- OCaml (via Printf module)
- PARI/GP
- Perl
  - Raku (via `printf`, `sprintf`, and `fmt`)
- PHP
- Python (via `%` operator)
- R
- Red/System
- Ruby
- SQLite
- Tcl (via `format` command)
- Transact-SQL (via `xp_sprintf`)
- Vala (via `print()` and `FileStream.printf()`)
