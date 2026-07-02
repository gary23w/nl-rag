---
title: "The GNU Awk User’s Guide (part 8/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 8/38
---

## 6 Expressions

Expressions are the basic building blocks of `awk` patterns and actions. An expression evaluates to a value that you can print, test, or pass to a function. Additionally, an expression can assign a new value to a variable or a field by using an assignment operator.

An expression can serve as a pattern or action statement on its own. Most other kinds of statements contain one or more expressions that specify the data on which to operate. As in other languages, expressions in `awk` can include variables, array references, constants, and function calls, as well as combinations of these with various operators.

### 6.1 Constants, Variables, and Conversions

Expressions are built up from values and the operations performed upon them. This section describes the elementary objects that provide the values used in expressions.

#### 6.1.1 Constant Expressions

The simplest type of expression is the *constant*, which always has the same value. There are three types of constants: numeric, string, and regular expression.

Each is used in the appropriate context when you need a data value that isn’t going to change. Numeric constants can have different forms, but are internally stored in an identical manner.

#### 6.1.1.1 Numeric and String Constants

A *numeric constant* stands for a number. This number can be an integer, a decimal fraction, or a number in scientific (exponential) notation.33 Here are some examples of numeric constants that all have the same value:

```
105
1.05e+2
1050e-1
```

A *string constant* consists of a sequence of characters enclosed in double quotation marks. For example:

```
"parrot"
```

represents the string whose contents are ‘parrot’. Strings in `gawk` can be of any length, and they can contain any of the possible eight-bit ASCII characters, including ASCII NUL (character code zero). Other `awk` implementations may have difficulty with some character codes.

Some languages allow you to continue long strings across multiple lines by ending the line with a backslash. For example in C:

```
#include <stdio.h>

int main()
{
    printf("hello, \
world\n");
    return 0;
}
```

In such a case, the C compiler removes both the backslash and the newline, producing a string as if it had been typed ‘"hello, world\n"’. This is useful when a single string needs to contain a large amount of text.

The POSIX standard says explicitly that newlines are not allowed inside string constants. And indeed, all `awk` implementations report an error if you try to do so. For example:

```
$ gawk 'BEGIN { print "hello, 
> world" }'
-| gawk: cmd. line:1: BEGIN { print "hello,
-| gawk: cmd. line:1:               ^ unterminated string
-| gawk: cmd. line:1: BEGIN { print "hello,
-| gawk: cmd. line:1:               ^ syntax error
```

Although POSIX doesn’t define what happens if you use an escaped newline, as in the previous C example, all known versions of `awk` allow you to do so. Unfortunately, what each one does with such a string varies. (d.c.) `gawk`, `mawk`, and the OpenSolaris POSIX `awk` (see Other Freely Available `awk` Implementations) elide the backslash and newline, as in C:

```
$ gawk 'BEGIN { print "hello, \
> world" }'
-| hello, world
```

In POSIX mode (see Command-Line Options), `gawk` does not allow escaped newlines. Otherwise, it behaves as just described.

BWK `awk`34 and BusyBox `awk` remove the backslash but leave the newline intact, as part of the string:

```
$ nawk 'BEGIN { print "hello, \
> world" }'
-| hello,
-| world
```

#### 6.1.1.2 Octal and Hexadecimal Numbers

In `awk`, all numbers are in decimal (i.e., base 10). Many other programming languages allow you to specify numbers in other bases, often octal (base 8) and hexadecimal (base 16). In octal, the numbers go 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, and so on. Just as ‘11’ in decimal is 1 times 10 plus 1, so ‘11’ in octal is 1 times 8 plus 1. This equals 9 in decimal. In hexadecimal, there are 16 digits. Because the everyday decimal number system only has ten digits (‘0’–‘9’), the letters ‘a’ through ‘f’ represent the rest. (Case in the letters is usually irrelevant; hexadecimal ‘a’ and ‘A’ have the same value.) Thus, ‘11’ in hexadecimal is 1 times 16 plus 1, which equals 17 in decimal.

Just by looking at plain ‘11’, you can’t tell what base it’s in. So, in C, C++, and other languages derived from C, there is a special notation to signify the base. Octal numbers start with a leading ‘0’, and hexadecimal numbers start with a leading ‘0x’ or ‘0X’:

**`11`**

Decimal value 11

**`011`**

Octal 11, decimal value 9

**`0x11`**

Hexadecimal 11, decimal value 17

This example shows the difference:

```
$ gawk 'BEGIN { printf "%d, %d, %d\n", 011, 11, 0x11 }'
-| 9, 11, 17
```

Being able to use octal and hexadecimal constants in your programs is most useful when working with data that cannot be represented conveniently as characters or as regular numbers, such as binary data of various sorts.

`gawk` allows the use of octal and hexadecimal constants in your program text. However, such numbers in the input data are not treated differently; doing so by default would break old programs. (If you really need to do this, use the --non-decimal-data command-line option; see Allowing Nondecimal Input Data.) If you have octal or hexadecimal data, you can use the `strtonum()` function (see String-Manipulation Functions) to convert the data into a number. Most of the time, you will want to use octal or hexadecimal constants when working with the built-in bit-manipulation functions; see Bit-Manipulation Functions for more information.

Unlike in some early C implementations, ‘8’ and ‘9’ are not valid in octal constants. For example, `gawk` treats ‘018’ as decimal 18:

```
$ gawk 'BEGIN { print "021 is", 021 ; print 018 }'
-| 021 is 17
-| 18
```

Hexadecimal integer constants have been part of the C language since the beginning. The C99 standard added support for hexadecimal floating-point values. This is a floating point number of the form [`-`]`0x*h*`[`.*hhhh*`]`p+-*dd*`. The ‘p’ introduces the exponent, and is *required*. The radix point and following digits are optional. As with integer hexadecimal constants, both ‘0x’ and ‘0X’ may be used, and case in the letters ‘a’ through ‘f’ does not matter.

Beginning with version 5.4.0, `gawk` supports hexadecimal floating point values, as constants in `awk` program source code, with the `strtonum()` built-in function, and with the --non-decimal-data command-line option. Here is an example:

```
$ gawk 'BEGIN { print 0xdeadbeefp-1 }'
-| 1.86796e+09
```

For this to work correctly, the version of `strtod()` in the system’s underlying C library must understand such constants. On modern systems this isn’t a problem.

Octal and hexadecimal source code constants are a `gawk` extension. If `gawk` is in compatibility mode (see Command-Line Options), they are not available.

| A Constant’s Base Does Not Affect Its Value |
|---|
| Once a numeric constant has been converted internally into a number, `gawk` no longer remembers what the original form of the constant was; the internal value is always used. This has particular consequences for conversion of numbers to strings: $ gawk 'BEGIN { printf "0x11 is <%s>\n", 0x11 }' -\| 0x11 is <17> |

#### 6.1.1.3 Regular Expression Constants

A *regexp constant* is a regular expression description enclosed in slashes, such as `/^beginning and end$/`. Most regexps used in `awk` programs are constant, but the ‘~’ and ‘!~’ matching operators can also match computed or dynamic regexps (which are typically just ordinary strings or variables that contain a regexp, but could be more complex expressions).

#### 6.1.2 Using Regular Expression Constants

Regular expression constants consist of text describing a regular expression enclosed in slashes (such as `/the +answer/`). This section describes how such constants work in POSIX `awk` and `gawk`, and then goes on to describe *strongly typed regexp constants*, which are a `gawk` extension.

#### 6.1.2.1 Standard Regular Expression Constants

When used on the righthand side of the ‘~’ or ‘!~’ operators, a regexp constant merely stands for the regexp that is to be matched. However, regexp constants (such as `/foo/`) may be used like simple expressions. When a regexp constant appears by itself, it has the same meaning as if it appeared in a pattern (i.e., ‘($0 ~ /foo/)’). (d.c.) See Expressions as Patterns. This means that the following two code segments:

```
if ($0 ~ /barfly/ || $0 ~ /camelot/)
    print "found"
```

and:

```
if (/barfly/ || /camelot/)
    print "found"
```

are exactly equivalent. One rather bizarre consequence of this rule is that the following Boolean expression is valid, but does not do what its author probably intended:

```
# Note that /foo/ is on the left of the ~
if (/foo/ ~ $1) print "found foo"
```

This code is “obviously” testing `$1` for a match against the regexp `/foo/`. But in fact, the expression ‘/foo/ ~ $1’ really means ‘($0 ~ /foo/) ~ $1’. In other words, first match the input record against the regexp `/foo/`. The result is either zero or one, depending upon the success or failure of the match. That result is then matched against the first field in the record. Because it is unlikely that you would ever really want to make this kind of test, `gawk` issues a warning when it sees this construct in a program. Another consequence of this rule is that the assignment statement:

```
matches = /foo/
```

assigns either zero or one to the variable `matches`, depending upon the contents of the current input record.

Constant regular expressions are also used as the first argument for the `gensub()`, `sub()`, and `gsub()` functions, as the second argument of the `match()` function, and as the third argument of the `split()` and `patsplit()` functions (see String-Manipulation Functions). Modern implementations of `awk`, including `gawk`, allow the third argument of `split()` to be a regexp constant, but some older implementations do not. (d.c.) Because some built-in functions accept regexp constants as arguments, confusion can arise when attempting to use regexp constants as arguments to user-defined functions (see User-Defined Functions). For example:

```
function mysub(pat, repl, str, global)
{
    if (global)
        gsub(pat, repl, str)
    else
        sub(pat, repl, str)
    return str
}
```

```
{
    ...
    text = "hi! hi yourself!"
    mysub(/hi/, "howdy", text, 1)
    ...
}
```

In this example, the programmer wants to pass a regexp constant to the user-defined function `mysub()`, which in turn passes it on to either `sub()` or `gsub()`. However, what really happens is that the `pat` parameter is assigned a value of either one or zero, depending upon whether or not `$0` matches `/hi/`. `gawk` issues a warning when it sees a regexp constant used as a parameter to a user-defined function, because passing a truth value in this way is probably not what was intended.

#### 6.1.2.2 Strongly Typed Regexp Constants

This section describes a `gawk`-specific feature.

As we saw in the previous section, regexp constants (`/…/`) hold a strange position in the `awk` language. In most contexts, they act like an expression: ‘$0 ~ /…/’. In other contexts, they denote only a regexp to be matched. In no case are they really a “first class citizen” of the language. That is, you cannot define a scalar variable whose type is “regexp” in the same sense that you can define a variable to be a number or a string:

```
num = 42        Numeric variable
str = "hi"      String variable
re = /foo/      Wrong! re is the result of $0 ~ /foo/
```

For a number of more advanced use cases, it would be nice to have regexp constants that are *strongly typed*; in other words, that denote a regexp useful for matching, and not an expression.

`gawk` provides this feature. A strongly typed regexp constant looks almost like a regular regexp constant, except that it is preceded by an ‘@’ sign:

```
re = @/foo/     Regexp variable
```

Strongly typed regexp constants *cannot* be used everywhere that a regular regexp constant can, because this would make the language even more confusing. Instead, you may use them only in certain contexts:

- On the righthand side of the ‘~’ and ‘!~’ operators: ‘some_var ~ @/foo/’ (see How to Use Regular Expressions).
- In the `case` part of a `switch` statement (see The `switch` Statement).
- As an argument to one of the built-in functions that accept regexp constants: `gensub()`, `gsub()`, `match()`, `patsplit()`, `split()`, and `sub()` (see String-Manipulation Functions).
- As a parameter in a call to a user-defined function (see User-Defined Functions).
- As the return value of a user-defined function.
- On the righthand side of an assignment to a variable: ‘some_var = @/foo/’. In this case, the type of `some_var` is regexp. Additionally, `some_var` can be used with ‘~’ and ‘!~’, passed to one of the built-in functions listed above, or passed as a parameter to a user-defined function.

You may use the -v option (see Command-Line Options) to assign a strongly-typed regexp constant to a variable on the command line, like so:

```
gawk -v pattern='@/something(interesting)+/' ...
```

You may also make such assignments as regular command-line arguments (see Other Command-Line Arguments).

You may use the `typeof()` built-in function (see Getting Type Information) to determine if a variable or function parameter is a regexp variable.

The true power of this feature comes from the ability to create variables that have regexp type. Such variables can be passed on to user-defined functions, without the confusing aspects of computed regular expressions created from strings or string constants. They may also be passed through indirect function calls (see Indirect Function Calls) and on to the built-in functions that accept regexp constants.

When used in numeric conversions, strongly typed regexp variables convert to zero. When used in string conversions, they convert to the string value of the original regexp text.

There is an additional, interesting corner case. When used as the third argument to `sub()` or `gsub()`, they retain their type. Thus, if you have something like this:

```
re = @/don't panic/
sub(/don't/, "do", re)
print typeof(re), re
```

then `re` retains its type, but now attempts to match the string ‘do panic’. This provides a (very indirect) way to create regexp-typed variables at runtime.

#### 6.1.3 Variables

*Variables* are ways of storing values at one point in your program for use later in another part of your program. They can be manipulated entirely within the program text, and they can also be assigned values on the `awk` command line.

#### 6.1.3.1 Using Variables in a Program

Variables let you give names to values and refer to them later. Variables have already been used in many of the examples. The name of a variable must be a sequence of letters, digits, or underscores, and it may not begin with a digit. Here, a *letter* is any one of the 52 upper- and lowercase English letters. Other characters that may be defined as letters in non-English locales are not valid in variable names. Case is significant in variable names; `a` and `A` are distinct variables.

A variable name is a valid expression by itself; it represents the variable’s current value. Variables are given new values with *assignment operators*, *increment operators*, and *decrement operators* (see Assignment Expressions). In addition, the `sub()` and `gsub()` functions can change a variable’s value, and the `match()`, `split()`, and `patsplit()` functions can change the contents of their array parameters (see String-Manipulation Functions).

A few variables have special built-in meanings, such as `FS` (the field separator) and `NF` (the number of fields in the current input record). See Predefined Variables for a list of the predefined variables. These predefined variables can be used and assigned just like all other variables, but their values are also used or changed automatically by `awk`. All predefined variables’ names are entirely uppercase.

Variables in `awk` can be assigned either numeric or string values. The kind of value a variable holds can change over the life of a program. By default, variables are initialized to the empty string, which is zero if converted to a number. There is no need to explicitly initialize a variable in `awk`, which is what you would do in C and in most other traditional languages.

#### 6.1.3.2 Assigning Variables on the Command Line

Any `awk` variable can be set by including a *variable assignment* among the arguments on the command line when `awk` is invoked (see Other Command-Line Arguments). Such an assignment has the following form:

```
variable=text
```

With it, a variable is set either at the beginning of the `awk` run or in between input files. When the assignment is preceded with the -v option, as in the following:

```
-v variable=text
```

the variable is set at the very beginning, even before the `BEGIN` rules execute. The -v option and its assignment must precede all the file name arguments, as well as the program text. (See Command-Line Options for more information about the -v option.) Otherwise, the variable assignment is performed at a time determined by its position among the input file arguments—after the processing of the preceding input file argument. For example:

```
awk '{ print $n }' n=4 inventory-shipped n=2 mail-list
```

prints the value of field number `n` for all input records. Before the first file is read, the command line sets the variable `n` equal to four. This causes the fourth field to be printed in lines from inventory-shipped. After the first file has finished, but before the second file is started, `n` is set to two, so that the second field is printed in lines from mail-list:

```
$ awk '{ print $n }' n=4 inventory-shipped n=2 mail-list
-| 15
-| 24
...
-| 555-5553
-| 555-3412
...
```

Command-line arguments are made available for explicit examination by the `awk` program in the `ARGV` array (see Using `ARGC` and `ARGV`). `awk` processes the values of command-line assignments for escape sequences (see Escape Sequences). (d.c.)

Normally, variables assigned on the command line (with or without the -v option) are treated as strings. When such variables are used as numbers, `awk`’s normal automatic conversion of strings to numbers takes place, and everything “just works.”

However, `gawk` supports variables whose types are “regexp”. You can assign variables of this type using the following syntax:

```
gawk -v 're1=@/foo|bar/' '...' /path/to/file1 're2=@/baz|quux/' /path/to/file2
```

Strongly typed regexps are an advanced feature (see Strongly Typed Regexp Constants). We mention them here only for completeness.

#### 6.1.4 Conversion of Strings and Numbers

Number-to-string and string-to-number conversion are generally straightforward. There can be subtleties to be aware of; this section discusses this important facet of `awk`.

#### 6.1.4.1 How `awk` Converts Between Strings and Numbers

Strings are converted to numbers and numbers are converted to strings, if the context of the `awk` program demands it. For example, if the value of either `foo` or `bar` in the expression ‘foo + bar’ happens to be a string, it is converted to a number before the addition is performed. If numeric values appear in string concatenation, they are converted to strings. Consider the following:

```
two = 2; three = 3
print (two three) + 4
```

This prints the (numeric) value 27. The numeric values of the variables `two` and `three` are converted to strings and concatenated together. The resulting string is converted back to the number 23, to which 4 is then added.

If, for some reason, you need to force a number to be converted to a string, concatenate that number with the empty string, `""`. To force a string to be converted to a number, add zero to that string. A string is converted to a number by interpreting any numeric prefix of the string as numerals: `"2.5"` converts to 2.5, `"1e3"` converts to 1,000, and `"25fix"` has a numeric value of 25. Strings that can’t be interpreted as valid numbers convert to zero.

The exact manner in which numbers are converted into strings is controlled by the `awk` predefined variable `CONVFMT` (see Predefined Variables). Numbers are converted using the `sprintf()` function with `CONVFMT` as the format specifier (see String-Manipulation Functions).

`CONVFMT`’s default value is `"%.6g"`, which creates a value with at most six significant digits. For some applications, you might want to change it to specify more precision. On most modern machines, 17 digits is usually enough to capture a floating-point number’s value exactly.35

Strange results can occur if you set `CONVFMT` to a string that doesn’t tell `sprintf()` how to format floating-point numbers in a useful way. For example, if you forget the ‘%’ in the format, `awk` converts all numbers to the same constant string.

As a special case, if a number is an integer, then the result of converting it to a string is *always* an integer, no matter what the value of `CONVFMT` may be. Given the following code fragment:

```
CONVFMT = "%2.2f"
a = 12
b = a ""
```

`b` has the value `"12"`, not `"12.00"`. (d.c.)

| Pre-POSIX `awk` Used `OFMT` for String Conversion |
|---|
| Prior to the POSIX standard, `awk` used the value of `OFMT` for converting numbers to strings. `OFMT` specifies the output format to use when printing numbers with `print`. `CONVFMT` was introduced in order to separate the semantics of conversion from the semantics of printing. Both `CONVFMT` and `OFMT` have the same default value: `"%.6g"`. In the vast majority of cases, old `awk` programs do not change their behavior. See The `print` Statement for more information on the `print` statement. |

#### 6.1.4.2 Locales Can Influence Conversion

Where you are can matter when it comes to converting between numbers and strings. The local character set and language—the *locale*—can affect numeric formats. In particular, for `awk` programs, it affects the decimal point character and the thousands-separator character. The `"C"` locale, and most English-language locales, use the period character (‘.’) as the decimal point and don’t have a thousands separator. However, many (if not most) European and non-English locales use the comma (‘,’) as the decimal point character. European locales often use either a space or a period as the thousands separator, if they have one.

The POSIX standard says that `awk` always uses the period as the decimal point when reading the `awk` program source code, and for command-line variable assignments (see Other Command-Line Arguments). However, when interpreting input data, for `print` and `printf` output, and for number-to-string conversion, the local decimal point character is used. (d.c.) In all cases, numbers in source code and in input data cannot have a thousands separator. Here are some examples indicating the difference in behavior, on a GNU/Linux system:

```
$ export POSIXLY_CORRECT=1                        Force POSIX behavior
$ gawk 'BEGIN { printf "%g\n", 3.1415927 }'
-| 3.14159
$ LC_ALL=en_DK.utf-8 gawk 'BEGIN { printf "%g\n", 3.1415927 }'
-| 3,14159
$ echo 4,321 | gawk '{ print $1 + 1 }'
-| 5
$ echo 4,321 | LC_ALL=en_DK.utf-8 gawk '{ print $1 + 1 }'
-| 5,321
```

The `en_DK.utf-8` locale is for English in Denmark, where the comma acts as the decimal point separator. In the normal `"C"` locale, `gawk` treats ‘4,321’ as 4, while in the Danish locale, it’s treated as the full number including the fractional part, 4.321.

Some earlier versions of `gawk` fully complied with this aspect of the standard. However, many users in non-English locales complained about this behavior, because their data used a period as the decimal point, so the default behavior was restored to use a period as the decimal point character. You can use the --use-lc-numeric option (see Command-Line Options) to force `gawk` to use the locale’s decimal point character. (`gawk` also uses the locale’s decimal point character when in POSIX mode, either via --posix or the `POSIXLY_CORRECT` environment variable, as shown previously.)

Table 6.1 describes the cases in which the locale’s decimal point character is used and when a period is used. Some of these features have not been described yet.

| Feature | Default | --posix or --use-lc-numeric |
|---|---|---|
| `%'g` | Use locale | Use locale |
| `%g` | Use period | Use locale |
| Input | Use period | Use locale |
| `strtonum()` | Use period | Use locale |

**Table 6.1:**Locale decimal point versus a period

Finally, modern-day formal standards and the IEEE standard floating-point representation can have an unusual but important effect on the way `gawk` converts some special string values to numbers. The details are presented in Standards Versus Existing Practice.

### 6.2 Operators: Doing Something with Values

This section introduces the *operators* that make use of the values provided by constants and variables.

#### 6.2.1 Arithmetic Operators

The `awk` language uses the common arithmetic operators when evaluating expressions. All of these arithmetic operators follow normal precedence rules and work as you would expect them to.

The following example uses a file named grades, which contains a list of student names as well as three test scores per student (it’s a small class):

```
Pat   100 97 58
Sandy  84 72 93
Chris  72 92 89
```

This program takes the file grades and prints the average of the scores:

```
$ awk '{ sum = $2 + $3 + $4 ; avg = sum / 3
>        print $1, avg }' grades
-| Pat 85
-| Sandy 83
-| Chris 84.3333
```

The following list provides the arithmetic operators in `awk`, in order from the highest precedence to the lowest:

**`*x* ^ *y*`**

**`*x* ** *y*`**

Exponentiation; *x* raised to the *y* power. ‘2 ^ 3’ has the value eight; the character sequence ‘**’ is equivalent to ‘^’. (c.e.)

**`- *x*`**

Negation.

**`+ *x*`**

Unary plus; the expression is converted to a number.

**`*x* * *y*`**

Multiplication.

**`*x* / *y*` ¶**

Division; because all numbers in `awk` are floating-point numbers, the result is *not* rounded to an integer—‘3 / 4’ has the value 0.75. (It is a common mistake, especially for C programmers, to forget that *all* numbers in `awk` are floating point, and that division of integer-looking constants produces a real number, not an integer.)

**`*x* % *y*`**

Remainder; further discussion is provided in the text, just after this list.

**`*x* + *y*`**

Addition.

**`*x* - *y*`**

Subtraction.

Unary plus and minus have the same precedence, the multiplication operators all have the same precedence, and addition and subtraction have the same precedence.

When computing the remainder of ‘*x* % *y*’, the quotient is rounded toward zero to an integer and multiplied by *y*. This result is subtracted from *x*; this operation is sometimes known as “trunc-mod.” The following relation always holds:

```
b * int(a / b) + (a % b) == a
```

One possibly undesirable effect of this definition of remainder is that ‘*x* % *y*’ is negative if *x* is negative. Thus:

```
-17 % 8 = -1
```

This definition is compliant with the POSIX standard, which says that the `%` operator produces results equivalent to using the standard C `fmod()` function, and that function in turn works as just described.

In other `awk` implementations, the signedness of the remainder may be machine-dependent.

> **NOTE:** The POSIX standard only specifies the use of ‘^’ for exponentiation. For maximum portability, do not use the ‘**’ operator.

#### 6.2.2 String Concatenation

> *It seemed like a good idea at the time.*

—

Brian Kernighan

There is only one string operation: concatenation. It does not have a specific operator to represent it. Instead, concatenation is performed by writing expressions next to one another, with no operator. For example:

```
$ awk '{ print "Field number one: " $1 }' mail-list
-| Field number one: Amelia
-| Field number one: Anthony
...
```

Without the space in the string constant after the ‘:’, the line runs together. For example:

```
$ awk '{ print "Field number one:" $1 }' mail-list
-| Field number one:Amelia
-| Field number one:Anthony
...
```

Because string concatenation does not have an explicit operator, it is often necessary to ensure that it happens at the right time by using parentheses to enclose the items to concatenate. For example, you might expect that the following code fragment concatenates `file` and `name`:

```
file = "file"
name = "name"
print "something meaningful" > file name
```

This produces a syntax error with some versions of Unix `awk`.36 It is necessary to use the following:

```
print "something meaningful" > (file name)
```

Parentheses should be used around concatenation in all but the most common contexts, such as on the righthand side of ‘=’. Be careful about the kinds of expressions used in string concatenation. In particular, the order of evaluation of expressions used for concatenation is undefined in the `awk` language. Consider this example:

```
BEGIN {
    a = "don't"
    print (a " " (a = "panic"))
}
```

It is not defined whether the second assignment to `a` happens before or after the value of `a` is retrieved for producing the concatenated value. The result could be either ‘don't panic’, or ‘panic panic’.

The precedence of concatenation, when mixed with other operators, is often counter-intuitive. Consider this example:

```
$ awk 'BEGIN { print -12 " " -24 }'
-| -12-24
```

This “obviously” is concatenating −12, a space, and −24. But where did the space disappear to? The answer lies in the combination of operator precedences and `awk`’s automatic conversion rules. To get the desired result, write the program this way:

```
$ awk 'BEGIN { print -12 " " (-24) }'
-| -12 -24
```

This forces `awk` to treat the ‘-’ on the ‘-24’ as unary. Otherwise, it’s parsed as follows:

```
    −12 (" " − 24)
⇒ −12 (0 − 24)
⇒ −12 (−24)
⇒ −12−24
```

As mentioned earlier, when mixing concatenation with other operators, *parenthesize*. Otherwise, you’re never quite sure what you’ll get.

#### 6.2.3 Assignment Expressions

An *assignment* is an expression that stores a (usually different) value into a variable. For example, let’s assign the value one to the variable `z`:

```
z = 1
```

After this expression is executed, the variable `z` has the value one. Whatever old value `z` had before the assignment is forgotten.

Assignments can also store string values. For example, the following stores the value `"this food is good"` in the variable `message`:

```
thing = "food"
predicate = "good"
message = "this " thing " is " predicate
```

This also illustrates string concatenation. The ‘=’ sign is called an *assignment operator*. It is the simplest assignment operator because the value of the righthand operand is stored unchanged. Most operators (addition, concatenation, and so on) have no effect except to compute a value. If the value isn’t used, there’s no reason to use the operator. An assignment operator is different; it does produce a value, but even if you ignore it, the assignment still makes itself felt through the alteration of the variable. We call this a *side effect*.

The lefthand operand of an assignment need not be a variable (see Variables); it can also be a field (see Changing the Contents of a Field) or an array element (see Arrays in `awk`). These are all called *lvalues*, which means they can appear on the lefthand side of an assignment operator. The righthand operand may be any expression; it produces the new value that the assignment stores in the specified variable, field, or array element. (Such values are called *rvalues*.)

It is important to note that variables do *not* have permanent types. A variable’s type is simply the type of whatever value was last assigned to it. In the following program fragment, the variable `foo` has a numeric value at first, and a string value later on:

```
foo = 1
print foo
```

```
foo = "bar"
print foo
```

When the second assignment gives `foo` a string value, the fact that it previously had a numeric value is forgotten.

String values that do not begin with a digit have a numeric value of zero. After executing the following code, the value of `foo` is five:

```
foo = "a string"
foo = foo + 5
```

> **NOTE:** Using a variable as a number and then later as a string can be confusing and is poor programming style. The previous two examples illustrate how `awk` works, *not* how you should write your programs!

An assignment is an expression, so it has a value—the same value that is assigned. Thus, ‘z = 1’ is an expression with the value one. One consequence of this is that you can write multiple assignments together, such as:

```
x = y = z = 5
```

This example stores the value five in all three variables (`x`, `y`, and `z`). It does so because the value of ‘z = 5’, which is five, is stored into `y` and then the value of ‘y = z = 5’, which is five, is stored into `x`.

Assignments may be used anywhere an expression is called for. For example, it is valid to write ‘x != (y = 1)’ to set `y` to one, and then test whether `x` equals one. But this style tends to make programs hard to read; such nesting of assignments should be avoided, except perhaps in a one-shot program.

Aside from ‘=’, there are several other assignment operators that do arithmetic with the old value of the variable. For example, the operator ‘+=’ computes a new value by adding the righthand value to the old value of the variable. Thus, the following assignment adds five to the value of `foo`:

```
foo += 5
```

This is equivalent to the following:

```
foo = foo + 5
```

Use whichever makes the meaning of your program clearer.
