---
title: "The GNU Awk User’s Guide (part 9/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 9/38
---

# The GNU Awk User’s Guide

There are situations where using ‘+=’ (or any assignment operator) is *not* the same as simply repeating the lefthand operand in the righthand expression. For example:

```
# Thanks to Pat Rankin for this example
BEGIN  {
    foo[rand()] += 5
    for (x in foo)
       print x, foo[x]
```

```
    bar[rand()] = bar[rand()] + 5
    for (x in bar)
       print x, bar[x]
}
```

The indices of `bar` are practically guaranteed to be different, because `rand()` returns different values each time it is called. (Arrays and the `rand()` function haven’t been covered yet. See Arrays in `awk`, and see Numeric Functions for more information.) This example illustrates an important fact about assignment operators: the lefthand expression is only evaluated *once*.

It is up to the implementation as to which expression is evaluated first, the lefthand or the righthand. Consider this example:

```
i = 1
a[i += 2] = i + 1
```

The value of `a[3]` could be either two or four.

Table 6.2 lists the arithmetic assignment operators. In each case, the righthand operand is an expression whose value is converted to a number.

| Operator | Effect |
|---|---|
| *lvalue* `+=` *increment* | Add *increment* to the value of *lvalue*. |
| *lvalue* `-=` *decrement* | Subtract *decrement* from the value of *lvalue*. |
| *lvalue* `*=` *coefficient* | Multiply the value of *lvalue* by *coefficient*. |
| *lvalue* `/=` *divisor* | Divide the value of *lvalue* by *divisor*. |
| *lvalue* `%=` *modulus* | Set *lvalue* to its remainder by *modulus*. |
| *lvalue* `^=` *power* | Raise *lvalue* to the power *power*. |
| *lvalue* `**=` *power* | Raise *lvalue* to the power *power*. (c.e.) |

**Table 6.2:**Arithmetic assignment operators

> **NOTE:** Only the ‘^=’ operator is specified by POSIX. For maximum portability, do not use the ‘**=’ operator.

| Syntactic Ambiguities Between ‘/=’ and Regular Expressions |
|---|
| There is a syntactic ambiguity between the `/=` assignment operator and regexp constants whose first character is an ‘=’. (d.c.) This is most notable in some commercial `awk` versions. For example: $ awk /==/ /dev/null error→ awk: syntax error at source line 1 error→ context is error→ >>> /= <<< error→ awk: bailing out at source line 1 A workaround is: awk '/[=]=/' /dev/null `gawk` does not have this problem; BWK `awk` and `mawk` also do not. |

#### 6.2.4 Increment and Decrement Operators

*Increment* and *decrement operators* increase or decrease the value of a variable by one. An assignment operator can do the same thing, so the increment operators add no power to the `awk` language; however, they are convenient abbreviations for very common operations.

The operator used for adding one is written ‘++’. It can be used to increment a variable either before or after taking its value. To *pre-increment* a variable `v`, write ‘++v’. This adds one to the value of `v`—that new value is also the value of the expression. (The assignment expression ‘v += 1’ is completely equivalent.) Writing the ‘++’ after the variable specifies *post-increment*. This increments the variable value just the same; the difference is that the value of the increment expression itself is the variable’s *old* value. Thus, if `foo` has the value four, then the expression ‘foo++’ has the value four, but it changes the value of `foo` to five. In other words, the operator returns the old value of the variable, but with the side effect of incrementing it.

The post-increment ‘foo++’ is nearly the same as writing ‘(foo += 1) - 1’. It is not perfectly equivalent because all numbers in `awk` are floating point—in floating point, ‘foo + 1 - 1’ does not necessarily equal `foo`. But the difference is minute as long as you stick to numbers that are fairly small (less than 1012).

Fields and array elements are incremented just like variables. (Use ‘$(i++)’ when you want to do a field reference and a variable increment at the same time. The parentheses are necessary because of the precedence of the field reference operator ‘$’.)

The decrement operator ‘--’ works just like ‘++’, except that it subtracts one instead of adding it. As with ‘++’, it can be used before the lvalue to pre-decrement or after it to post-decrement. Following is a summary of increment and decrement expressions:

**`++*lvalue*`**

Increment *lvalue*, returning the new value as the value of the expression.

**`*lvalue*++`**

Increment *lvalue*, returning the *old* value of *lvalue* as the value of the expression.

**`--*lvalue*`**

Decrement *lvalue*, returning the new value as the value of the expression. (This expression is like ‘++*lvalue*’, but instead of adding, it subtracts.)

**`*lvalue*--`**

Decrement *lvalue*, returning the *old* value of *lvalue* as the value of the expression. (This expression is like ‘*lvalue*++’, but instead of adding, it subtracts.)

| Operator Evaluation Order |
|---|
| *Doctor, it hurts when I do this! Then don’t do that!* — *Groucho Marx* What happens for something like the following? b = 6 print b += b++ Or something even stranger? b = 6 b += ++b + b++ print b In other words, when do the various side effects prescribed by the postfix operators (‘b++’) take effect? When side effects happen is *implementation-defined*. In other words, it is up to the particular version of `awk`. The result for the first example may be 12 or 13, and for the second, it may be 22 or 23. In short, doing things like this is not recommended and definitely not anything that you can rely upon for portability. You should avoid such things in your own programs. |

### 6.3 Truth Values and Conditions

In certain contexts, expression values also serve as “truth values”; i.e., they determine what should happen next as the program runs. This section describes how `awk` defines “true” and “false” and how values are compared.

#### 6.3.1 True and False in `awk`

Many programming languages have a special representation for the concepts of “true” and “false.” Such languages usually use the special constants `true` and `false`, or perhaps their uppercase equivalents. However, `awk` is different. It borrows a very simple concept of true and false from C. In `awk`, any nonzero numeric value *or* any nonempty string value is true. Any other value (zero or the null string, `""`) is false. The following program prints ‘A strange truth value’ three times:

```
BEGIN {
   if (3.1415927)
       print "A strange truth value"
   if ("Four Score And Seven Years Ago")
       print "A strange truth value"
   if (j = 57)
       print "A strange truth value"
}
```

There is a surprising consequence of the “nonzero or non-null” rule: the string constant `"0"` is actually true, because it is non-null. (d.c.)

#### 6.3.2 Variable Typing and Comparison Expressions

> *The Guide is definitive. Reality is frequently inaccurate.*

—

Douglas Adams,

The Hitchhiker’s Guide to the Galaxy

Unlike in other programming languages, in `awk` variables do not have a fixed type. Instead, they can be either a number or a string, depending upon the value that is assigned to them. We look now at how variables are typed, and how `awk` compares variables.

#### 6.3.2.1 String Type versus Numeric Type

Scalar objects in `awk` (variables, array elements, and fields) are *dynamically* typed. This means their type can change as the program runs, from *untyped* before any use,37 to string or number, and then from string to number or number to string, as the program progresses. (`gawk` also provides regexp-typed scalars, but let’s ignore that for now; see Strongly Typed Regexp Constants.)

You can’t do much with untyped variables, other than tell that they are untyped. The following program tests `a` against `""` and `0`; the test succeeds when `a` has never been assigned a value. It also uses the built-in `typeof()` function (not presented yet; see Getting Type Information) to show `a`’s type:

```
$ gawk 'BEGIN { print (a == "" && a == 0 ?
> "a is untyped" : "a has a type!") ; print typeof(a) }'
-| a is untyped
-| unassigned
```

A scalar has numeric type when assigned a numeric value, such as from a numeric constant, or from another scalar with numeric type:

```
$ gawk 'BEGIN { a = 42 ; print typeof(a)
> b = a ; print typeof(b) }'
number
number
```

Similarly, a scalar has string type when assigned a string value, such as from a string constant, or from another scalar with string type:

```
$ gawk 'BEGIN { a = "forty two" ; print typeof(a)
> b = a ; print typeof(b) }'
string
string
```

So far, this is all simple and straightforward. What happens, though, when `awk` has to process data from a user? Let’s start with field data. What should the following command produce as output?

```
echo hello | awk '{ printf("%s %s < 42\n", $1,
                           ($1 < 42 ? "is" : "is not")) }'
```

Since ‘hello’ is alphabetic data, `awk` can only do a string comparison. Internally, it converts `42` into `"42"` and compares the two string values `"hello"` and `"42"`. Here’s the result:

```
$ echo hello | awk '{ printf("%s %s < 42\n", $1,
>                            ($1 < 42 ? "is" : "is not")) }'
-| hello is not < 42
```

However, what happens when data from a user *looks like* a number? On the one hand, in reality, the input data consists of characters, not binary numeric values. But, on the other hand, the data looks numeric, and `awk` really ought to treat it as such. And indeed, it does:

```
$ echo 37 | awk '{ printf("%s %s < 42\n", $1,
>                         ($1 < 42 ? "is" : "is not")) }'
-| 37 is < 42
```

Here are the rules for when `awk` treats data as a number, and for when it treats data as a string.

The POSIX standard uses the term *numeric string* for input data that looks numeric. The ‘37’ in the previous example is a numeric string. So what is the type of a numeric string? Answer: numeric.

The type of a variable is important because the types of two variables determine how they are compared. Variable typing follows these definitions and rules:

- A numeric constant or the result of a numeric operation has the *numeric* attribute.
- A string constant or the result of a string operation has the *string* attribute.
- Fields, `getline` input, `FILENAME`, `ARGV` elements, `ENVIRON` elements, and the elements of an array created by `match()`, `split()`, and `patsplit()` that are numeric strings have the *strnum* attribute.38 Otherwise, they have the *string* attribute. Uninitialized variables also have the *strnum* attribute.
- Attributes propagate across assignments but are not changed by any use.

The last rule is particularly important. In the following program, `a` has numeric type, even though it is later used in a string operation:

```
BEGIN {
     a = 12.345
     b = a " is a cute number"
     print b
}
```

When two operands are compared, either string comparison or numeric comparison may be used. This depends upon the attributes of the operands, according to the following symmetric matrix:

```
        +----------------------------------------------
        |       STRING          NUMERIC         STRNUM
--------+----------------------------------------------
        |
STRING  |       string          string          string
        |
NUMERIC |       string          numeric         numeric
        |
STRNUM  |       string          numeric         numeric
--------+----------------------------------------------
```

The basic idea is that user input that looks numeric—and *only* user input—should be treated as numeric, even though it is actually made of characters and is therefore also a string. Thus, for example, the string constant `" +3.14"`, when it appears in program source code, is a string—even though it looks numeric—and is *never* treated as a number for comparison purposes.

In short, when one operand is a “pure” string, such as a string constant, then a string comparison is performed. Otherwise, a numeric comparison is performed. (The primary difference between a number and a strnum is that for strnums `gawk` preserves the original string value that the scalar had when it came in.)

This point bears additional emphasis: Input that looks numeric *is* numeric. All other input is treated as strings.

Thus, the six-character input string ‘ +3.14’ receives the strnum attribute. In contrast, the eight characters `" +3.14"` appearing in program text comprise a string constant. The following examples print ‘1’ when the comparison between the two different constants is true, and ‘0’ otherwise:

```
$ echo ' +3.14' | awk '{ print($0 == " +3.14") }'    True
-| 1
$ echo ' +3.14' | awk '{ print($0 == "+3.14") }'     False
-| 0
$ echo ' +3.14' | awk '{ print($0 == "3.14") }'      False
-| 0
$ echo ' +3.14' | awk '{ print($0 == 3.14) }'        True
-| 1
$ echo ' +3.14' | awk '{ print($1 == " +3.14") }'    False
-| 0
$ echo ' +3.14' | awk '{ print($1 == "+3.14") }'     True
-| 1
$ echo ' +3.14' | awk '{ print($1 == "3.14") }'      False
-| 0
$ echo ' +3.14' | awk '{ print($1 == 3.14) }'        True
-| 1
```

You can see the type of an input field (or other user input) using `typeof()`:

```
$ echo hello 37 | gawk '{ print typeof($1), typeof($2) }'
-| string strnum
```

#### 6.3.2.2 Comparison Operators

*Comparison expressions* compare strings or numbers for relationships such as equality. They are written using *relational operators*, which are a superset of those in C. Table 6.3 describes them.

| Expression | Result |
|---|---|
| *x* `<` *y* | True if *x* is less than *y* |
| *x* `<=` *y* | True if *x* is less than or equal to *y* |
| *x* `>` *y* | True if *x* is greater than *y* |
| *x* `>=` *y* | True if *x* is greater than or equal to *y* |
| *x* `==` *y* | True if *x* is equal to *y* |
| *x* `!=` *y* | True if *x* is not equal to *y* |
| *x* `~` *y* | True if the string *x* matches the regexp denoted by *y* |
| *x* `!~` *y* | True if the string *x* does not match the regexp denoted by *y* |
| *subscript* `in` *array* | True if the array *array* has an element with the subscript *subscript* |

**Table 6.3:**Relational operators

Comparison expressions have the value one if true and zero if false. When comparing operands of mixed types, numeric operands are converted to strings using the value of `CONVFMT` (see Conversion of Strings and Numbers).

Strings are compared by comparing the first character of each, then the second character of each, and so on. Thus, `"10"` is less than `"9"`. If there are two strings where one is a prefix of the other, the shorter string is less than the longer one. Thus, `"abc"` is less than `"abcd"`.

It is very easy to accidentally mistype the ‘==’ operator and leave off one of the ‘=’ characters. The result is still valid `awk` code, but the program does not do what is intended:

```
if (a = b)   # oops! should be a == b
   ...
else
   ...
```

Unless `b` happens to be zero or the null string, the `if` part of the test always succeeds. Because the operators are so similar, this kind of error is very difficult to spot when scanning the source code.

The following list of expressions illustrates the kinds of comparisons `awk` performs, as well as what the result of each comparison is:

**`1.5 <= 2.0`**

Numeric comparison (true)

**`"abc" >= "xyz"`**

String comparison (false)

**`1.5 != " +2"`**

String comparison (true)

**`"1e2" < "3"`**

String comparison (true)

**`a = 2; b = "2"`**

**`a == b`**

String comparison (true)

**`a = 2; b = " +2"`**

**`a == b`**

String comparison (false)

In this example:

```
$ echo 1e2 3 | awk '{ print ($1 < $2) ? "true" : "false" }'
-| false
```

the result is ‘false’ because both `$1` and `$2` are user input. They are numeric strings—therefore both have the strnum attribute, dictating a numeric comparison. The purpose of the comparison rules and the use of numeric strings is to attempt to produce the behavior that is “least surprising,” while still “doing the right thing.”

String comparisons and regular expression comparisons are very different. For example:

```
x == "foo"
```

has the value one, or is true if the variable `x` is precisely ‘foo’. By contrast:

```
x ~ /foo/
```

has the value one if `x` contains ‘foo’, such as `"Oh, what a fool am I!"`.

The righthand operand of the ‘~’ and ‘!~’ operators may be either a regexp constant (`/`…`/`) or an ordinary expression. In the latter case, the value of the expression as a string is used as a dynamic regexp (see How to Use Regular Expressions; also see Using Dynamic Regexps).

A constant regular expression in slashes by itself is also an expression. `/*regexp*/` is an abbreviation for the following comparison expression:

```
$0 ~ /regexp/
```

One special place where `/foo/` is *not* an abbreviation for ‘$0 ~ /foo/’ is when it is the righthand operand of ‘~’ or ‘!~’. See Using Regular Expression Constants, where this is discussed in more detail.

#### 6.3.2.3 String Comparison Based on Locale Collating Order

The POSIX standard used to say that all string comparisons are performed based on the locale’s *collating order*. This is the order in which characters sort, as defined by the locale (for more discussion, see Where You Are Makes a Difference). This order is usually very different from the results obtained when doing straight byte-by-byte comparison.39

Because this behavior differs considerably from existing practice, `gawk` only implemented it when in POSIX mode (see Command-Line Options). Here is an example to illustrate the difference, in an `en_US.UTF-8` locale:

```
$ gawk 'BEGIN { printf("ABC < abc = %s\n",
>                     ("ABC" < "abc" ? "TRUE" : "FALSE")) }'
-| ABC < abc = TRUE
$ gawk --posix 'BEGIN { printf("ABC < abc = %s\n",
>                             ("ABC" < "abc" ? "TRUE" : "FALSE")) }'
-| ABC < abc = FALSE
```

Fortunately, as of August 2016, comparison based on locale collating order is no longer required for the `==` and `!=` operators.40 However, comparison based on locales is still required for `<`, `<=`, `>`, and `>=`. POSIX thus recommends as follows:

> Since the `==` operator checks whether strings are identical, not whether they collate equally, applications needing to check whether strings collate equally can use:
> 
> ```
> a <= b && a >= b
> ```

As of version 4.2, `gawk` continues to use locale collating order for `<`, `<=`, `>`, and `>=` only in POSIX mode.

#### 6.3.3 Boolean Expressions

A *Boolean expression* is a combination of comparison expressions or matching expressions, using the Boolean operators “or” (‘||’), “and” (‘&&’), and “not” (‘!’), along with parentheses to control nesting. The truth value of the Boolean expression is computed by combining the truth values of the component expressions. Boolean expressions are also referred to as *logical expressions*. The terms are equivalent.

Boolean expressions can be used wherever comparison and matching expressions can be used. They can be used in `if`, `while`, `do`, and `for` statements (see Control Statements in Actions). They have numeric values (one if true, zero if false) that come into play if the result of the Boolean expression is stored in a variable or used in arithmetic.

In addition, every Boolean expression is also a valid pattern, so you can use one as a pattern to control the execution of rules. The Boolean operators are:

**`*boolean1* && *boolean2*`**

True if both *boolean1* and *boolean2* are true. For example, the following statement prints the current input record if it contains both ‘edu’ and ‘li’:

```
if ($0 ~ /edu/ && $0 ~ /li/) print
```

The subexpression *boolean2* is evaluated only if *boolean1* is true. This can make a difference when *boolean2* contains expressions that have side effects. In the case of ‘$0 ~ /foo/ && ($2 == bar++)’, the variable `bar` is not incremented if there is no substring ‘foo’ in the record.

**`*boolean1* || *boolean2*`**

True if at least one of *boolean1* or *boolean2* is true. For example, the following statement prints all records in the input that contain *either* ‘edu’ or ‘li’:

```
if ($0 ~ /edu/ || $0 ~ /li/) print
```

The subexpression *boolean2* is evaluated only if *boolean1* is false. This can make a difference when *boolean2* contains expressions that have side effects. (Thus, this test never really distinguishes records that contain both ‘edu’ and ‘li’—as soon as ‘edu’ is matched, the full test succeeds.)

**`! *boolean*`**

True if *boolean* is false. For example, the following program prints ‘no home!’ in the unusual event that the `HOME` environment variable is not defined:

```
BEGIN { if (! ("HOME" in ENVIRON))
            print "no home!" }
```

(The `in` operator is described in Referring to an Array Element.)

The ‘&&’ and ‘||’ operators are called *short-circuit* operators because of the way they work. Evaluation of the full expression is “short-circuited” if the result can be determined partway through its evaluation.

Statements that end with ‘&&’ or ‘||’ can be continued simply by putting a newline after them. But you cannot put a newline in front of either of these operators without using backslash continuation (see `awk` Statements Versus Lines).

The actual value of an expression using the ‘!’ operator is either one or zero, depending upon the truth value of the expression it is applied to. The ‘!’ operator is often useful for changing the sense of a flag variable from false to true and back again. For example, the following program is one way to print lines in between special bracketing lines:

```
$1 == "START"   { interested = ! interested; next }
interested      { print }
$1 == "END"     { interested = ! interested; next }
```

The variable `interested`, as with all `awk` variables, starts out initialized to zero, which is also false. When a line is seen whose first field is ‘START’, the value of `interested` is toggled to true, using ‘!’. The next rule prints lines as long as `interested` is true. When a line is seen whose first field is ‘END’, `interested` is toggled back to false.41

Most commonly, the ‘!’ operator is used in the conditions of `if` and `while` statements, where it often makes more sense to phrase the logic in the negative:

```
if (! some condition || some other condition) {
    ... do whatever processing ...
}
```

> **NOTE:** The `next` statement is discussed in The `next` Statement. `next` tells `awk` to skip the rest of the rules, get the next record, and start processing the rules over again at the top. The reason it’s there is to avoid printing the bracketing ‘START’ and ‘END’ lines.

#### 6.3.4 Conditional Expressions

A *conditional expression* is a special kind of expression that has three operands. It allows you to use one expression’s value to select one of two other expressions. The conditional expression in `awk` is the same as in the C language, as shown here:

```
selector ? if-true-exp : if-false-exp
```

There are three subexpressions. The first, *selector*, is always computed first. If it is “true” (not zero or not null), then *if-true-exp* is computed next, and its value becomes the value of the whole expression. Otherwise, *if-false-exp* is computed next, and its value becomes the value of the whole expression. For example, the following expression produces the absolute value of `x`:

```
x >= 0 ? x : -x
```

Each time the conditional expression is computed, only one of *if-true-exp* and *if-false-exp* is used; the other is ignored. This is important when the expressions have side effects. For example, this conditional expression examines element `i` of either array `a` or array `b`, and increments `i`:

```
x == y ? a[i++] : b[i++]
```

This is guaranteed to increment `i` exactly once, because each time only one of the two increment expressions is executed and the other is not. See Arrays in `awk`, for more information about arrays.

As a minor `gawk` extension, a statement that uses ‘?:’ can be continued simply by putting a newline after either character. However, putting a newline in front of either character does not work without using backslash continuation (see `awk` Statements Versus Lines). If --posix is specified (see Command-Line Options), this extension is disabled.

### 6.4 Function Calls

A *function* is a name for a particular calculation. This enables you to ask for it by name at any point in the program. For example, the function `sqrt()` computes the square root of a number.

A fixed set of functions are *built in*, which means they are available in every `awk` program. The `sqrt()` function is one of these. See Built-in Functions for a list of built-in functions and their descriptions. In addition, you can define functions for use in your program. See User-Defined Functions for instructions on how to do this. Finally, `gawk` lets you write functions in C or C++ that may be called from your program (see Writing Extensions for `gawk`).

The way to use a function is with a *function call* expression, which consists of the function name followed immediately by a list of *arguments* in parentheses. The arguments are expressions that provide the raw materials for the function’s calculations. When there is more than one argument, they are separated by commas. If there are no arguments, just write ‘()’ after the function name. The following examples show function calls with and without arguments:

```
sqrt(x^2 + y^2)        one argument
atan2(y, x)            two arguments
rand()                 no arguments
```

> **CAUTION:** Do not put any space between the function name and the opening parenthesis! A user-defined function name looks just like the name of a variable—a space would make the expression look like concatenation of a variable with an expression inside parentheses. With built-in functions, space before the parenthesis is harmless, but it is best not to get into the habit of using space to avoid mistakes with user-defined functions.

Each function expects a particular number of arguments. For example, the `sqrt()` function must be called with a single argument, the number of which to take the square root:

```
sqrt(argument)
```

Some of the built-in functions have one or more optional arguments. If those arguments are not supplied, the functions use a reasonable default value. See Built-in Functions for full details. If arguments are omitted in calls to user-defined functions, then those arguments are treated as local variables. Such local variables act like the empty string if referenced where a string value is required, and like zero if referenced where a numeric value is required (see User-Defined Functions).

As an advanced feature, `gawk` provides indirect function calls, which is a way to choose the function to call at runtime, instead of when you write the source code to your program. We defer discussion of this feature until later; see Indirect Function Calls.

Like every other expression, the function call has a value, often called the *return value*, which is computed by the function based on the arguments you give it. In this example, the return value of ‘sqrt(*argument*)’ is the square root of *argument*. The following program reads numbers, one number per line, and prints the square root of each one:

```
$ awk '{ print "The square root of", $1, "is", sqrt($1) }'
1
-| The square root of 1 is 1
3
-| The square root of 3 is 1.73205
5
-| The square root of 5 is 2.23607
Ctrl-d
```

A function can also have side effects, such as assigning values to certain variables or doing I/O. This program shows how the `match()` function (see String-Manipulation Functions) changes the variables `RSTART` and `RLENGTH`:

```
{
    if (match($1, $2))
        print RSTART, RLENGTH
    else
        print "no match"
}
```

Here is a sample run:

```
$ awk -f matchit.awk
aaccdd  c+
-| 3 2
foo     bar
-| no match
abcdefg e
-| 5 1
```

### 6.5 Operator Precedence (How Operators Nest)

*Operator precedence* determines how operators are grouped when different operators appear close by in one expression. For example, ‘*’ has higher precedence than ‘+’; thus, ‘a + b * c’ means to multiply `b` and `c`, and then add `a` to the product (i.e., ‘a + (b * c)’).

The normal precedence of the operators can be overruled by using parentheses. Think of the precedence rules as saying where the parentheses are assumed to be. In fact, it is wise to always use parentheses whenever there is an unusual combination of operators, because other people who read the program may not remember what the precedence is in this case. Even experienced programmers occasionally forget the exact rules, which leads to mistakes. Explicit parentheses help prevent any such mistakes.

When operators of equal precedence are used together, the leftmost operator groups first, except for the assignment, conditional, and exponentiation operators, which group in the opposite order. Thus, ‘a - b + c’ groups as ‘(a - b) + c’ and ‘a = b = c’ groups as ‘a = (b = c)’.

Normally the precedence of prefix unary operators does not matter, because there is only one way to interpret them: innermost first. Thus, ‘$++i’ means ‘$(++i)’ and ‘++$x’ means ‘++($x)’. However, when another operator follows the operand, then the precedence of the unary operators can matter. ‘$x^2’ means ‘($x)^2’, but ‘-x^2’ means ‘-(x^2)’, because ‘-’ has lower precedence than ‘^’, whereas ‘$’ has higher precedence. Also, operators cannot be combined in a way that violates the precedence rules; for example, ‘$$0++--’ is not a valid expression because the first ‘$’ has higher precedence than the ‘++’; to avoid the problem the expression can be rewritten as ‘$($0++)--’.

This list presents `awk`’s operators, in order of highest to lowest precedence:

**`(`…`)`**

Grouping.

**`$`**

Field reference.

**`++ --`**

Increment, decrement.

**`^ **`**

Exponentiation. These operators group right to left.

**`+ - !`**

Unary plus, minus, logical “not.”

**`* / %`**

Multiplication, division, remainder.

**`+ -`**

Addition, subtraction.

**String concatenation**

There is no special symbol for concatenation. The operands are simply written side by side (see String Concatenation).

**`< <= == != > >= >> | |&`**

Relational and redirection. The relational operators and the redirections have the same precedence level. Characters such as ‘>’ serve both as relationals and as redirections; the context distinguishes between the two meanings.

Note that the I/O redirection operators in `print` and `printf` statements belong to the statement level, not to expressions. The redirection does not produce an expression that could be the operand of another operator. As a result, it does not make sense to use a redirection operator near another operator of lower precedence without parentheses. Such combinations (e.g., ‘print foo > a ? b : c’) result in syntax errors. The correct way to write this statement is ‘print foo > (a ? b : c)’.

**`~ !~`**

Matching, nonmatching.

**`in` ¶**

Array membership.

**`&&`**

Logical “and.”

**`||`**

Logical “or.”

**`?:`**

Conditional. This operator groups right to left.

**`= += -= *= /= %= ^= **=`**

Assignment. These operators group right to left.

> **NOTE:** The ‘|&’, ‘**’, and ‘**=’ operators are not specified by POSIX. For maximum portability, do not use them.

### 6.6 Where You Are Makes a Difference

Modern systems support the notion of *locales*: a way to tell the system about the local character set and language. The ISO C standard defines a default `"C"` locale, which is an environment that is typical of what many C programmers are used to.

Once upon a time, the locale setting used to affect regexp matching, but this is no longer true (see Regexp Ranges and Locales: A Long Sad Story).

Locales can affect record splitting. For the normal case of ‘RS = "\n"’, the locale is largely irrelevant. For other single-character record separators, setting ‘LC_ALL=C’ in the environment will give you much better performance when reading records. Otherwise, `gawk` has to make several function calls, *per input character*, to find the record terminator.

Locales can affect how dates and times are formatted (see Time Functions). For example, a common way to abbreviate the date September 4, 2015, in the United States is “9/4/15.” In many countries in Europe, however, it is abbreviated “4.9.15.” Thus, the ‘%x’ specification in a `"US"` locale might produce ‘9/4/15’, while in a `"EUROPE"` locale, it might produce ‘4.9.15’.

According to POSIX, string comparison is also affected by locales (similar to regular expressions). The details are presented in String Comparison Based on Locale Collating Order.

Finally, the locale affects the value of the decimal point character used when `gawk` parses input data. This is discussed in detail in Conversion of Strings and Numbers.

### 6.7 Summary

- Expressions are the basic elements of computation in programs. They are built from constants, variables, function calls, and combinations of the various kinds of values with operators.
- `awk` supplies three kinds of constants: numeric, string, and regexp. `gawk` lets you specify numeric constants in octal and hexadecimal (bases 8 and 16) as well as decimal (base 10). In certain contexts, a standalone regexp constant such as `/foo/` has the same meaning as ‘$0 ~ /foo/’.
- Variables hold values between uses in computations. A number of built-in variables provide information to your `awk` program, and a number of others let you control how `awk` behaves.
- Numbers are automatically converted to strings, and strings to numbers, as needed by `awk`. Numeric values are converted as if they were formatted with `sprintf()` using the format in `CONVFMT`. Locales can influence the conversions.
- `awk` provides the usual arithmetic operators (addition, subtraction, multiplication, division, modulus), and unary plus and minus. It also provides comparison operators, Boolean operators, an array membership testing operator, and regexp matching operators. String concatenation is accomplished by placing two expressions next to each other; there is no explicit operator. The three-operand ‘?:’ operator provides an “if-else” test within expressions.
- Assignment operators provide convenient shorthands for common arithmetic operations.
- In `awk`, a value is considered to be true if it is nonzero *or* non-null. Otherwise, the value is false.
- A variable’s type is set upon each assignment and may change over its lifetime. The type determines how it behaves in comparisons (string or numeric).
- Function calls return a value that may be used as part of a larger expression. Expressions used to pass parameter values are fully evaluated before the function is called. `awk` provides built-in and user-defined functions; this is described in Functions.
- Operator precedence specifies the order in which operations are performed, unless explicitly overridden by parentheses. `awk`’s operator precedence is compatible with that of C.
- Locales can affect the format of data as output by an `awk` program, and occasionally the format for data read as input.
