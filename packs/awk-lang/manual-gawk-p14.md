---
title: "The GNU Awk User’s Guide (part 14/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 14/38
---

# The GNU Awk User’s Guide

**`%Ec %EC %Ex %EX %Ey %EY %Od %Oe %OH`**

**`%OI %Om %OM %OS %Ou %OU %OV %Ow %OW %Oy`**

“Alternative representations” for the specifications that use only the second letter (‘%c’, ‘%C’, and so on).61 (These facilitate compliance with the POSIX `date` utility.)

**`%%`**

A literal ‘%’.

If a conversion specifier is not one of those just listed, the behavior is undefined.62

For systems that are not yet fully standards-compliant, `gawk` supplies a copy of `strftime()` from the GNU C Library. It supports all of the just-listed format specifications. If that version is used to compile `gawk` (see Installing `gawk`), then the following additional format specifications are available:

**`%k`**

The hour (24-hour clock) as a decimal number (0–23). Single-digit numbers are padded with a space.

**`%l`**

The hour (12-hour clock) as a decimal number (1–12). Single-digit numbers are padded with a space.

**`%s`**

The time as a decimal timestamp in seconds since the epoch.

Additionally, the alternative representations are recognized but their normal representations are used.

> **NOTE:** Similar to `printf()`, some versions of `strftime()` support the use of flags between the `%` and the format specification letter. Check your local man page for `strftime()` to see if it supports flags or not, and what they are. Be aware, however, that using any such flags is likely to make your script less portable to other systems.

The following example is an `awk` implementation of the POSIX `date` utility. Normally, the `date` utility prints the current date and time of day in a well-known format. However, if you provide an argument to it that begins with a ‘+’, `date` copies nonformat specifier characters to the standard output and interprets the current time according to the format specifiers in the string. For example:

```
$ date '+Today is %A, %B %d, %Y.'
-| Today is Monday, September 22, 2014.
```

Here is the `gawk` version of the `date` utility. It has a shell “wrapper” to handle the -u option, which requires that `date` run as if the time zone is set to UTC:

```
#! /bin/sh
#
# date --- approximate the POSIX 'date' command

case $1 in
-u)  TZ=UTC0     # use UTC
     export TZ
     shift ;;
esac

gawk 'BEGIN  {
    format = PROCINFO["strftime"]
    exitval = 0

    if (ARGC > 2)
        exitval = 1
    else if (ARGC == 2) {
        format = ARGV[1]
        if (format ~ /^\+/)
            format = substr(format, 2)   # remove leading +
    }
    print strftime(format)
    exit exitval
}' "$@"
```

This script was written before the `strftime()` function acquired its third argument, *utc-flag*. Consider how you might modify the program to work entirely in `awk` and process the -u option for printing the time in UTC.

#### 9.1.7 Bit-Manipulation Functions

> *I can explain it for you, but I can’t understand it for you.*

—

Anonymous

Many languages provide the ability to perform *bitwise* operations on two integer numbers. In other words, the operation is performed on each successive pair of bits in the operands. Three common operations are bitwise AND, OR, and XOR. The operations are described in Table 9.6.

```
                Bit operator
          |  AND  |   OR  |  XOR
          |---+---+---+---+---+---
Operands  | 0 | 1 | 0 | 1 | 0 | 1
----------+---+---+---+---+---+---
    0     | 0   0 | 0   1 | 0   1
    1     | 0   1 | 1   1 | 1   0
```

**Table 9.6:**Bitwise operations

As you can see, the result of an AND operation is 1 only when *both* bits are 1. The result of an OR operation is 1 if *either* bit is 1. The result of an XOR operation is 1 if either bit is 1, but not both. The next operation is the *complement*; the complement of 1 is 0 and the complement of 0 is 1. Thus, this operation “flips” all the bits of a given value.

Finally, two other common operations are to shift the bits left or right. For example, if you have a bit string ‘10111001’ and you shift it right by three bits, you end up with ‘00010111’.63 If you start over again with ‘10111001’ and shift it left by three bits, you end up with ‘11001000’. The following list describes `gawk`’s built-in functions that implement the bitwise operations. Optional parameters are enclosed in square brackets ([ ]):

**`and(`*v1*`,` *v2* [`,` …]`)`**

Return the bitwise AND of the arguments. There must be at least two.

**`compl(*val*)`**

Return the bitwise complement of *val*.

**`lshift(*val*, *count*)` ¶**

Return the value of *val*, shifted left by *count* bits.

**`or(`*v1*`,` *v2* [`,` …]`)`**

Return the bitwise OR of the arguments. There must be at least two.

**`rshift(*val*, *count*)` ¶**

Return the value of *val*, shifted right by *count* bits.

**`xor(`*v1*`,` *v2* [`,` …]`)`**

Return the bitwise XOR of the arguments. There must be at least two.

> **CAUTION:** Beginning with `gawk` version 4.2, negative operands are not allowed for any of these functions. A negative operand produces a fatal error. See the sidebar “Beware The Smoke and Mirrors!” for more information as to why.
> 
> Beginning with `gawk` version 5.4, if not in MPFR mode (see Arithmetic and Arbitrary-Precision Arithmetic with `gawk`), shifting with `lshift()` or `rshift()` by as many or more bits than are available in the largest unsigned integer returns zero, instead of whatever the underlying C compiler might do.

Here is a user-defined function (see User-Defined Functions) that illustrates the use of these functions:

```
# bits2str --- turn an integer into readable ones and zeros

function bits2str(bits,        data, mask)
{
    if (bits == 0)
        return "0"

    mask = 1
    for (; bits != 0; bits = rshift(bits, 1))
        data = (and(bits, mask) ? "1" : "0") data

    while ((length(data) % 8) != 0)
        data = "0" data

    return data
}
```

```
BEGIN {
    printf "123 = %s\n", bits2str(123)
    printf "0123 = %s\n", bits2str(0123)
    printf "0x99 = %s\n", bits2str(0x99)
    comp = compl(0x99)
    printf "compl(0x99) = %#x = %s\n", comp, bits2str(comp)
    shift = lshift(0x99, 2)
    printf "lshift(0x99, 2) = %#x = %s\n", shift, bits2str(shift)
    shift = rshift(0x99, 2)
    printf "rshift(0x99, 2) = %#x = %s\n", shift, bits2str(shift)
}
```

This program produces the following output when run:

```
$ gawk -f testbits.awk
-| 123 = 01111011
-| 0123 = 01010011
-| 0x99 = 10011001
-| compl(0x99) = 0x3fffffffffff66 =
-| 00111111111111111111111111111111111111111111111101100110
-| lshift(0x99, 2) = 0x264 = 0000001001100100
-| rshift(0x99, 2) = 0x26 = 00100110
```

The `bits2str()` function turns a binary number into a string. Initializing `mask` to one creates a binary value where the rightmost bit is set to one. Using this mask, the function repeatedly checks the rightmost bit. ANDing the mask with the value indicates whether the rightmost bit is one or not. If so, a `"1"` is concatenated onto the front of the string. Otherwise, a `"0"` is added. The value is then shifted right by one bit and the loop continues until there are no more one bits.

If the initial value is zero, it returns a simple `"0"`. Otherwise, at the end, it pads the value with zeros to represent multiples of 8-bit quantities. This is typical in modern computers.

The main code in the `BEGIN` rule shows the difference between the decimal and octal values for the same numbers (see Octal and Hexadecimal Numbers), and then demonstrates the results of the `compl()`, `lshift()`, and `rshift()` functions.

| Beware The Smoke and Mirrors! |
|---|
| In other languages, bitwise operations are performed on integer values, not floating-point values. As a general statement, such operations work best when performed on unsigned integers. `gawk` attempts to treat the arguments to the bitwise functions as unsigned integers. For this reason, negative arguments produce a fatal error. In normal operation, for all of these functions, first the double-precision floating-point value is converted to the widest C unsigned integer type, then the bitwise operation is performed. If the result cannot be represented exactly as a C `double`, leading nonzero bits are removed one by one until it can be represented exactly. The result is then converted back into a C `double`.64 However, when using arbitrary precision arithmetic with the -M option (see Arithmetic and Arbitrary-Precision Arithmetic with `gawk`), the results may differ. This is particularly noticeable with the `compl()` function: $ gawk 'BEGIN { print compl(42) }' -\| 9007199254740949 $ gawk -M 'BEGIN { print compl(42) }' -\| -43 What’s going on becomes clear when printing the results in hexadecimal: $ gawk 'BEGIN { printf "%#x\n", compl(42) }' -\| 0x1fffffffffffd5 $ gawk -M 'BEGIN { printf "%#x\n", compl(42) }' -\| 0xffffffffffffffd5 When using the -M option, under the hood, `gawk` uses GNU MP arbitrary precision integers which have at least 64 bits of precision. When not using -M, `gawk` stores integral values in regular double-precision floating point, which only maintain 53 bits of precision. Furthermore, the GNU MP library treats (or at least seems to treat) the leading bit as a sign bit; thus the result with -M in this case is a negative number. In short, using `gawk` for any but the simplest kind of bitwise operations is probably a bad idea; caveat emptor! |

#### 9.1.8 Getting Type Information

`gawk` provides two functions that let you distinguish the type of a variable. This is necessary for writing code that traverses every element of an array of arrays (see Arrays of Arrays), and in other contexts.

**`isarray(*x*)` ¶**

Return a true value if *x* is an array. Otherwise, return false.

**`typeof(*x*)`**

Return one of the following strings, depending upon the type of *x*:

**`"array"`**

*x* is an array.

**`"regexp"`**

*x* is a strongly typed regexp (see Strongly Typed Regexp Constants).

**`"number"`**

*x* is a number.

**`"number|bool"`**

*x* is a Boolean typed value (see Boolean Typed Values).

**`"string"`**

*x* is a string.

**`"strnum"`**

*x* is a number that started life as user input, such as a field or the result of calling `split()`. (I.e., *x* has the strnum attribute; see String Type versus Numeric Type.)

**`"unassigned"`**

*x* is a *scalar* variable that has not been assigned a value yet.

**`"untyped"`**

*x* has not yet been used yet at all; it can become a scalar or an array.

`isarray()` is meant for use in two circumstances. The first is when traversing a multidimensional array: you can test if an element is itself an array or not. The second is inside the body of a user-defined function (not discussed yet; see User-Defined Functions), to test if a parameter is an array or not.

> **NOTE:** While you can use `isarray()` at the global level to test variables, doing so makes no sense. Because *you* are the one writing the program, *you* are supposed to know if your variables are arrays or not.

The `typeof()` function is general; it allows you to determine if a variable or function parameter is a scalar (number, string, or strongly typed regexp) or an array.

We delay further discussion of `unassigned` vs. `untyped` to Dynamic Typing In `gawk`.

#### 9.1.9 String-Translation Functions

`gawk` provides facilities for internationalizing `awk` programs. These include the functions described in the following list. The descriptions here are purposely brief. See Internationalization with `gawk`, for the full story. Optional parameters are enclosed in square brackets ([ ]):

**`bindtextdomain(*directory*` [`,` *domain*]`)` ¶**

Set the directory in which `gawk` will look for message translation files, in case they will not or cannot be placed in the “standard” locations (e.g., during testing). It returns the directory in which *domain* is “bound.”

The default *domain* is the value of `TEXTDOMAIN`. If *directory* is the null string (`""`), then `bindtextdomain()` returns the current binding for the given *domain*.

**`dcgettext(*string*` [`,` *domain* [`,` *category*] ]`)` ¶**

Return the translation of *string* in text domain *domain* for locale category *category*. The default value for *domain* is the current value of `TEXTDOMAIN`. The default value for *category* is `"LC_MESSAGES"`.

**`dcngettext(*string1*, *string2*, *number*` [`,` *domain* [`,` *category*] ]`)` ¶**

Return the plural form used for *number* of the translation of *string1* and *string2* in text domain *domain* for locale category *category*. *string1* is the English singular variant of a message, and *string2* is the English plural variant of the same message. The default value for *domain* is the current value of `TEXTDOMAIN`. The default value for *category* is `"LC_MESSAGES"`.

### 9.2 User-Defined Functions

Complicated `awk` programs can often be simplified by defining your own functions. User-defined functions can be called just like built-in ones (see Function Calls), but it is up to you to define them (i.e., to tell `awk` what they should do).

#### 9.2.1 Function Definition Syntax

> *It’s entirely fair to say that the awk syntax for local variable definitions is appallingly awful.*

—

Brian Kernighan

Definitions of functions can appear anywhere between the rules of an `awk` program. Thus, the general form of an `awk` program is extended to include sequences of rules *and* user-defined function definitions. There is no need to put the definition of a function before all uses of the function. This is because `awk` reads the entire program before starting to execute any of it.

The definition of a function named *name* looks like this:

```
function name([parameter-list])
{
     body-of-function
}
```

Here, *name* is the name of the function to define. A valid function name is like a valid variable name: a sequence of letters, digits, and underscores that doesn’t start with a digit. Here too, only the 52 upper- and lowercase English letters may be used in a function name. Within a single `awk` program, any particular name can only be used as a variable, array, or function.

*parameter-list* is an optional list of the function’s arguments and local variable names, separated by commas. When the function is called, the argument names are used to hold the argument values given in the call.

A function cannot have two parameters with the same name, nor may it have a parameter with the same name as the function itself.

> **CAUTION:** According to the POSIX standard, function parameters cannot have the same name as one of the special predefined variables (see Predefined Variables), nor may a function parameter have the same name as another function.
> 
> Not all versions of `awk` enforce these restrictions. (d.c.) `gawk` always enforces the first restriction. With --posix (see Command-Line Options), it also enforces the second restriction.

Local variables act like the empty string if referenced where a string value is required, and like zero if referenced where a numeric value is required. This is the same as the behavior of regular variables that have never been assigned a value. (There is more to understand about local variables; see Variable Typing Is Dynamic.)

The *body-of-function* consists of `awk` statements. It is the most important part of the definition, because it says what the function should actually *do*. The argument names exist to give the body a way to talk about the arguments; local variables exist to give the body places to keep temporary values.

Argument names are not distinguished syntactically from local variable names. Instead, the number of arguments supplied when the function is called determines how many argument variables there are. Thus, if three argument values are given, the first three names in *parameter-list* are arguments and the rest are local variables.

It follows that if the number of arguments is not the same in all calls to the function, some of the names in *parameter-list* may be arguments on some occasions and local variables on others. Another way to think of this is that omitted arguments default to the null string.

Usually when you write a function, you know how many names you intend to use for arguments and how many you intend to use as local variables. It is conventional to place some extra space between the arguments and the local variables, in order to document how your function is supposed to be used.

During execution of the function body, the arguments and local variable values hide, or *shadow*, any variables of the same names used in the rest of the program. The shadowed variables are not accessible in the function definition, because there is no way to name them while their names have been taken away for the arguments and local variables. All other variables used in the `awk` program can be referenced or set normally in the function’s body. (Also, see A Note On Shadowed Variables.)

The arguments and local variables last only as long as the function body is executing. Once the body finishes, you can once again access the variables that were shadowed while the function was running.

The function body can contain expressions that call functions. They can even call this function, either directly or by way of another function. When this happens, we say the function is *recursive*. The act of a function calling itself is called *recursion*.

All the built-in functions return a value to their caller. User-defined functions can do so also, using the `return` statement, which is described in detail in The `return` Statement. Many of the subsequent examples in this section use the `return` statement.

In many `awk` implementations, including `gawk`, the keyword `function` may be abbreviated `func`. (c.e.) However, POSIX only specifies the use of the keyword `function`. This actually has some practical implications. If `gawk` is in POSIX-compatibility mode (see Command-Line Options), then the following statement does *not* define a function:

```
func foo() { a = sqrt($1) ; print a }
```

Instead, it defines a rule that, for each record, concatenates the value of the variable ‘func’ with the return value of the function ‘foo’. If the resulting string is non-null, the action is executed. This is probably not what is desired. (`awk` accepts this input as syntactically valid, because functions may be used before they are defined in `awk` programs.65)

To ensure that your `awk` programs are portable, always use the keyword `function` when defining a function.

#### 9.2.2 Function Definition Examples

Here is an example of a user-defined function, called `myprint()`, that takes a number and prints it in a specific format:

```
function myprint(num)
{
     printf "%6.3g\n", num
}
```

To illustrate, here is an `awk` rule that uses our `myprint()` function:

```
$3 > 0     { myprint($3) }
```

This program prints, in our special format, all the third fields that contain a positive number in our input. Therefore, when given the following input:

```
 1.2   3.4    5.6   7.8
 9.10 11.12 -13.14 15.16
17.18 19.20  21.22 23.24
```

this program, using our function to format the results, prints:

```
   5.6
  21.2
```

This function deletes all the elements in an array (recall that the extra whitespace signifies the start of the local variable list):

```
function delarray(a,    i)
{
    for (i in a)
        delete a[i]
}
```

When working with arrays, it is often necessary to delete all the elements in an array and start over with a new list of elements (see The `delete` Statement). Instead of having to repeat this loop everywhere that you need to clear out an array, your program can just call `delarray()`. (This guarantees portability. The use of ‘delete *array*’ to delete the contents of an entire array is a relatively recent66 addition to the POSIX standard.)

The following is an example of a recursive function. It takes a string as an input parameter and returns the string in reverse order. Recursive functions must always have a test that stops the recursion. In this case, the recursion terminates when the input string is already empty:

```
function rev(str)
{
    if (str == "")
        return ""

    return (rev(substr(str, 2)) substr(str, 1, 1))
}
```

If this function is in a file named rev.awk, it can be tested this way:

```
$ echo "Don't Panic!" |
> gawk -e '{ print rev($0) }' -f rev.awk
-| !cinaP t'noD
```

The C `ctime()` function takes a timestamp and returns it as a string, formatted in a well-known fashion. The following example uses the built-in `strftime()` function (see Time Functions) to create an `awk` version of `ctime()`:

```
# ctime.awk
#
# awk version of C ctime(3) function

function ctime(ts,    format)
{
    format = "%a %b %e %H:%M:%S %Z %Y"

    if (ts == 0)
        ts = systime()       # use current time as default
    return strftime(format, ts)
}
```

You might think that `ctime()` could use `PROCINFO["strftime"]` for its format string. That would be a mistake, because `ctime()` is supposed to return the time formatted in a standard fashion, and user-level code could have changed `PROCINFO["strftime"]`.

#### 9.2.3 Calling User-Defined Functions

*Calling a function* means causing the function to run and do its job. A function call is an expression and its value is the value returned by the function.

#### 9.2.3.1 Writing a Function Call

A function call consists of the function name followed by the arguments in parentheses. `awk` expressions are what you write in the call for the arguments. Each time the call is executed, these expressions are evaluated, and the values become the actual arguments. For example, here is a call to `foo()` with three arguments (the first being a string concatenation):

```
foo(x y, "lose", 4 * z)
```

> **CAUTION:** Whitespace characters (spaces and TABs) are not allowed between the function name and the opening parenthesis of the argument list. If you write whitespace by mistake, `awk` might think that you mean to concatenate a variable with an expression in parentheses. However, it notices that you used a function name and not a variable name, and reports an error.

#### 9.2.3.2 Controlling Variable Scope

Unlike in many languages, there is no way to make a variable local to a `{` … `}` block in `awk`, but you can make a variable local to a function. It is good practice to do so whenever a variable is needed only in that function.

To make a variable local to a function, simply declare the variable as an argument after the actual function arguments (see Function Definition Syntax). Look at the following example, where variable `i` is a global variable used by both functions `foo()` and `bar()`:

```
function bar()
{
    for (i = 0; i < 3; i++)
        print "bar's i=" i
}

function foo(j)
{
    i = j + 1
    print "foo's i=" i
    bar()
    print "foo's i=" i
}

BEGIN {
      i = 10
      print "top's i=" i
      foo(0)
      print "top's i=" i
}
```

Running this script produces the following, because the `i` in functions `foo()` and `bar()` and at the top level refer to the same variable instance:

```
top's i=10
foo's i=1
bar's i=0
bar's i=1
bar's i=2
foo's i=3
top's i=3
```

If you want `i` to be local to both `foo()` and `bar()`, do as follows (the extra space before `i` is a coding convention to indicate that `i` is a local variable, not an argument):

```
function bar(    i)
{
    for (i = 0; i < 3; i++)
        print "bar's i=" i
}

function foo(j,    i)
{
    i = j + 1
    print "foo's i=" i
    bar()
    print "foo's i=" i
}

BEGIN {
      i = 10
      print "top's i=" i
      foo(0)
      print "top's i=" i
}
```

Running the corrected script produces the following:

```
top's i=10
foo's i=1
bar's i=0
bar's i=1
bar's i=2
foo's i=1
top's i=10
```

Besides scalar values (strings and numbers), you may also have local arrays. By using a parameter name as an array, `awk` treats it as an array, and it is local to the function. In addition, recursive calls create new arrays. Consider this example:

```
function some_func(p1,      a)
{
    if (p1++ > 3)
        return
```

```
    a[p1] = p1

    some_func(p1)

    printf("At level %d, index %d %s found in a\n",
         p1, (p1 - 1), (p1 - 1) in a ? "is" : "is not")
    printf("At level %d, index %d %s found in a\n",
         p1, p1, p1 in a ? "is" : "is not")
    print ""
}

BEGIN {
    some_func(1)
}
```
