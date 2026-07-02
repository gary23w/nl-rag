---
title: "String interpolation"
source: https://en.wikipedia.org/wiki/String_interpolation
domain: fmt-cpp-lib
license: CC-BY-SA-4.0
tags: fmt library, cpp string formatting, fmt format spec, fmt print library
fetched: 2026-07-02
---

# String interpolation

In computer programming, **string interpolation** (or **variable interpolation**, **variable substitution**, or **variable expansion**) is the process of evaluating a string literal containing one or more placeholders, yielding a result in which the placeholders are replaced with their corresponding values. It is a form of simple template processing or, in formal terms, a form of quasi-quotation (or logic substitution interpretation). The placeholder may be a variable name, or in some languages an arbitrary expression, in either case evaluated in the current context.

String interpolation is an alternative to building a string via concatenation, which requires repeat quoting and unquoting; or substituting into a printf format string, where the variable is far from where it is used. Consider this example in Ruby:

```mw
apples = 4
puts "I have #{apples} apples." # string interpolation
puts "I have " + String(apples) + " apples." # string concatenation
puts "I have %d apples." % apples # format string
```

Two types of literal expression are usually offered: one with interpolation enabled, the other without. Non-interpolated strings may also escape sequences, in which case they are termed a raw string, though in other cases this is separate, yielding three classes of raw string, non-interpolated (but escaped) string, interpolated (and escaped) string. For example, in Unix shells, single-quoted strings are raw, while double-quoted strings are interpolated. Placeholders are usually represented by a bare or a named sigil (typically `$` or `%`), e.g. `$apples` or `%apples`, or with braces, e.g. `{apples}`, sometimes both, e.g. `${apples}`. In some cases, additional formatting specifiers can be used (as in printf), e.g. `{apples:3}`, and in some cases the formatting specifiers themselves can be interpolated, e.g. `{apples:width}`. Expansion of the string usually occurs at run time.

Language support for string interpolation varies widely. Some languages do not offer string interpolation, instead using concatenation, simple formatting functions, or template libraries. String interpolation is common in many programming languages which make heavy use of string representations of data, such as Apache Groovy, Julia, Kotlin, Perl, PHP, Python, Ruby, Scala, Swift, Tcl and most Unix shells.

## Algorithms

There are two main types of variable-expanding algorithms for *variable interpolation*:

1. *Replace and expand placeholders*: creating a new string from the original one, by find–replace operations. Find variable reference (placeholder), replace it with its variable value. This algorithm offers no cache strategy.
2. *Split and join string*: splitting the string into an array, merging it with the corresponding array of values, then joining items by concatenation. The split string can be cached for reuse.

## Security issues

String interpolation, like string concatenation, may lead to security problems. If user input data is improperly escaped or filtered, the system will be exposed to SQL injection, script injection, XML external entity (XXE) injection, and cross-site scripting (XSS) attacks.

An SQL injection example:

```mw
query = "SELECT x, y, z FROM Table WHERE id='$id' "
```

If *`$id`* is replaced with *"'; `DELETE FROM Table; SELECT * FROM Table WHERE id='`"*, executing this query will wipe out all the data in `Table`.

## Examples

### ABAP

```mw
DATA(apples) = 4.
WRITE |I have { apples } apples|.
```

The output will be:

```mw
I have 4 apples
```

### Bash

```mw
apples=4
echo "I have $apples apples"
# or
echo "I have ${apples} apples"
```

The output will be:

```mw
I have 4 apples
```

### Boo

```mw
apples = 4
print("I have $(apples) apples")
# or
print("I have {0} apples" % apples)
```

The output will be:

```mw
I have 4 apples
```

### C

C does not have interpolated strings, but they can be approximated using `sprintf()` from `<stdio.h>`.

```mw
#include <stdio.h>

#define BUFFER_SIZE 100

int main() {
    char sentence[BUFFER_SIZE];

    int age = 20;
    float height = 5.9;
    char name[] = "Alice";

    sprintf(sentence, "My name is %s and I am %d years old, and I am %.1f feet tall.", name, age, height);
    printf(sentence);
    // prints:
    // My name is Alice, and I am 20 years old, and I am 5.9 feet tall.
}
```

### C++

While interpolated strings do not exist in C++, they can be approximated using `std::format` and `std::print` functions.

```mw
import std;

using std::string;

int main() {
    int apples = 4;
    int bananas = 3;

    std::println("I have {} apples", apples); // format specifiers
    std::println("I have {0} fruits, of which there are {1} apples and {2} bananas", apples + bananas, apples, bananas); // specify position explicitly

    // using std::format():
    string name = "John Doe";
    int age = 20;
    string greeting = std::format("Hello, {}! You are {} years old.", name, age);
}
```

Interpolated strings have been proposed for inclusion into C++, based on Python f-strings. The proposal incorporates features previously included from `std::format`, based on *{fmt}*. In this proposal, each f-string is transformed into a function call to a new function, `std::make_formatted_string()`.

```mw
import std;

using std::string;
using std::string_view;

int calculate(int x) {
    // ...
}

string represent(string_view prefix, int bits) {
    return f"{prefix}-{__LINE__}: got {calculate(bits)} for {bits:#06x}";
}

void display(string_view prefix, int bits) {
    std::print(f"{prefix}-{__LINE__}: got {calculate(bits)} for {bits:#06x}");
}
```

### C

```mw
int apples = 4;
int bananas = 3;

Console.WriteLine($"I have {apples} apples");
Console.WriteLine($"I have {apples + bananas} fruits");
```

The output will be:

```mw
I have 4 apples
I have 7 fruits
```

This can also be done using `String.Format()`.

```mw
int apples = 4;
int bananas = 3;

Console.WriteLine(String.Format("I have {0} apples and {1} bananas.", apples, bananas));
```

### ColdFusion Markup Language

ColdFusion Markup Language (CFML) script syntax:

```mw
apples = 4;
writeOutput("I have #apples# apples");
```

Tag syntax:

```mw
<cfset apples = 4>
<cfoutput>I have #apples# apples</cfoutput>
```

The output will be:

```
I have 4 apples
```

### CoffeeScript

```mw
apples = 4
console.log "I have #{apples} apples"
```

The output will be:

```mw
I have 4 apples
```

### Dart

```mw
int apples = 4, bananas = 3;
print('I have $apples apples.');
print('I have ${apples+bananas} fruits.');
```

The output will be:

```mw
I have 4 apples.
I have 7 fruits.
```

### Go

While there have been some proposals for string interpolation (which have been rejected), As of 2025 Go does not have interpolated strings.

However, they can be approximated using `fmt.Sprintf()`.

```mw
import "fmt"

func main() {
    // message is of type string
    message := fmt.Sprintf("My name is %s and I am %d years old.", "John Doe", 20)
    fmt.Println(message)
}
```

### Groovy

In groovy, interpolated strings are known as GStrings:

```mw
def quality = "superhero"
final age = 52
def sentence = "A developer is a $quality if he is ${age <= 42 ? 'young' : 'seasoned'}"
println sentence
```

The output will be:

```mw
A developer is a superhero if he is seasoned
```

### Haxe

```mw
var apples = 4;
var bananas = 3;
trace('I have $apples apples.');
trace('I have ${apples+bananas} fruits.');
```

The output will be:

```mw
I have 4 apples.
I have 7 fruits.
```

### Java

Java had interpolated strings as a preview feature in Java 21 and Java 22. One could use the constant STR of java.lang.StringTemplate directly.

```mw
package org.wikipedia.examples;

enum Stage {
    TEST,
    QA,
    PRODUCTION
}

record Deploy(UUID image, Stage stage) {}

public class Example {
    public static void main(String[] args) {
        Deploy deploy = new Deploy(UUID.randomUUID(), Stage.TEST)
        STR."Installing \{deploy.image()} on Stage \{deploy.stage()} ..."
        Deploy deploy = new Deploy(UUID.randomUUID(), Stage.PRODUCTION)
        STR."Installing \{deploy.image()} on Stage \{deploy.stage()} ..."
    }
}
```

They were removed in Java 23 due to design issues.

Otherwise, interpolated strings can be approximated using the `String.format()` method.

```mw
package org.wikipedia.examples;

public class Example {
    public static void main(String[] args) {
        int apples = 3;
        int bananas = 4;

        String sentence = String.format("I have %d fruits, of which %d are apples and %d are bananas.", apples + bananas, apples, bananas);
        System.out.println(sentence);

        String name = "John Doe";
        int age = 20;
        System.out.printf("My name is %s, and I am %d years old.", name, age);
    }
}
```

### JavaScript/TypeScript

JavaScript and TypeScript, as of the ECMAScript 2015 (ES6) standard, support string interpolation using backticks ``. This feature is called *template literals*. Here is an example:

```mw
const apples: number = 4;
const bananas: number = 3;
console.log(`I have ${apples} apples`);
console.log(`I have ${apples + bananas} fruits`);
```

The output will be:

```mw
I have 4 apples
I have 7 fruits
```

Template literals can also be used for multi-line strings:

```mw
console.log(`This is the first line of text.
This is the second line of text.`);
```

The output will be:

```mw
This is the first line of text.
This is the second line of text.
```

### Julia

```mw
apples = 4
bananas = 3
print("I have $apples apples and $bananas bananas, making $(apples + bananas) pieces of fruit in total.")
```

The output will be:

```mw
I have 4 apples and 3 bananas, making 7 pieces of fruit in total.
```

### Kotlin

```mw
fun main() {
    val quality: String = "superhero"
    val apples: Int = 4
    val bananas: Int = 3
    val sentence: String = "A developer is a $quality. I have ${apples + bananas} fruits"
    println(sentence)
}
```

The output will be:

```mw
A developer is a superhero. I have 7 fruits
```

### Nemerle

```mw
def apples = 4;
def bananas = 3;
Console.WriteLine($"I have $apples apples.");
Console.WriteLine($"I have $(apples + bananas) fruit.");
```

It also supports advanced formatting features, such as:

```mw
def fruit = ["apple", "banana"];
Console.WriteLine($<#I have ..$(fruit; "\n"; f => f + "s")#>);
```

The output will be:

```mw
apples
bananas
```

### Nim

Nim provides string interpolation via the strutils module. Formatted string literals inspired by Python F-string are provided via the strformat module, the strformat macro verifies that the format string is well-formed and well-typed, and then are expanded into Nim source code at compile-time.

```mw
import strutils, strformat
var apples = 4
var bananas = 3
echo "I have $1 apples".format(apples)
echo fmt"I have {apples} apples"
echo fmt"I have {apples + bananas} fruits"

# Multi-line
echo fmt"""
I have 
{apples} apples"""

# Debug the formatting
echo fmt"I have {apples=} apples"

# Custom openChar and closeChar characters
echo fmt("I have (apples) {apples}", '(', ')')

# Backslash inside the formatted string literal
echo fmt"""{ "yep\nope" }"""
```

The output will be:

```mw
I have 4 apples
I have 4 apples
I have 7 fruits
I have
4 apples
I have apples=4 apples
I have 4 {apples}
yep
ope
```

### Nix

```mw
let numberOfApples = "4";
in "I have ${numberOfApples} apples"
```

The output will be:

```mw
I have 4 apples
```

### ParaSail

```mw
const Apples := 4
const Bananas := 3
Println ("I have `(Apples) apples.\n")
Println ("I have `(Apples+Bananas) fruits.\n")
```

The output will be:

```mw
I have 4 apples.
I have 7 fruits.
```

### Perl

```mw
my $apples = 4;
my $bananas = 3;
print "I have $apples apples.\n";
print "I have @{[$apples+$bananas]} fruit.\n";  # Uses the Perl array (@) interpolation.
```

The output will be:

```mw
I have 4 apples.
I have 7 fruit.
```

### PHP

```mw
<?php
$apples = 5;
$bananas = 3;
echo "There are $apples apples and $bananas bananas.\n";
echo "I have {$apples} apples and {$bananas} bananas.";
```

The output will be:

```mw
There are 5 apples and 3 bananas.
I have 5 apples and 3 bananas.
```

### Python

Python supports string interpolation as of version 3.6, referred to as "formatted string literals" or "f-strings". Such a literal begins with an `f` or `F` before the opening quote, and uses braces for placeholders:

```mw
apples: int = 4
bananas: int = 3

print(f"I have {apples} apples and {bananas} bananas")
```

The output will be:

```mw
I have 4 apples and 3 bananas
```

### Ruby/Crystal

```mw
apples = 4
puts "I have #{apples} apples"
# Format string applications for comparison:
puts "I have %s apples" % apples
puts "I have %{a} apples" % {a: apples}
```

The output will be:

```mw
I have 4 apples
```

### Rust

Rust does not have general string interpolation, but provides similar functionality via macros, referred to as "Captured identifiers in format strings", introduced in version 1.58.0, released 2022-01-13.

Rust provides formatting via the std::fmt module, which is interfaced with through various macros such as format!, write!, and print!. These macros are converted into Rust source code at compile-time, whereby each argument interacts with a formatter. The formatter supports positional parameters, named parameters, argument types, defining various formatting traits, and capturing identifiers from the environment.

```mw
fn main() {
    let (apples, bananas): (i32, i32) = (4, 3);
    // println! captures the identifiers when formatting: the string itself isn't interpolated by Rust.
    println!("There are {apples} apples and {bananas} bananas.");

    // alternatively, with format!():
    let sentence: String = format!("There are {0} apples and {1} bananas.", apples, bananas);
    println!(sentence);
}
```

The output will be:

```mw
There are 4 apples and 3 bananas.
```

### Scala

Scala 2.10+ provides a general facility to allow arbitrary processing of a string literal, and supports string interpolation using the included `s` and `f` string interpolators. It is also possible to write custom ones or override the standard ones.

The `f` interpolator is a compiler macro that rewrites a format string with embedded expressions as an invocation of String.format. It verifies that the format string is well-formed and well-typed.

#### The standard interpolators

Scala 2.10+'s string interpolation allows embedding variable references directly in processed string literals. Here is an example:

```mw
val apples = 4
val bananas = 3
//before Scala 2.10
printf("I have %d apples\n", apples)
println("I have %d apples" format apples)
//Scala 2.10+
println(s"I have $apples apples")
println(s"I have ${apples + bananas} fruits")
println(f"I have $apples%d apples")
```

The output will be:

```mw
I have 4 apples
```

### Sciter (tiscript)

In Sciter any function with name starting from $ is considered as interpolating function and so interpolation is customizable and context sensitive:

```mw
var apples = 4
var bananas = 3
var domElement = ...;

domElement.$content(<p>I have {apples} apples</p>);
domElement.$append(<p>I have {apples + bananas} fruits</p>);
```

Where

```mw
domElement.$content(<p>I have {apples} apples</p>);
```

gets compiled to this:

```mw
domElement.html = "<p>I have " + apples.toHtmlString() + " apples</p>";
```

### Snobol

```mw
   apples = 4 ; bananas = 3
   Output = "I have " apples " apples."
   Output = "I have "  (apples + bananas) " fruits."
```

The output will be:

```mw
I have 4 apples.
I have 7 fruits.
```

### Swift

In Swift, a new String value can be created from a mix of constants, variables, literals, and expressions by including their values inside a string literal. Each item inserted into the string literal is wrapped in a pair of parentheses, prefixed by a backslash.

```mw
let apples = 4
print("I have \(apples) apples")
```

The output will be:

```mw
I have 4 apples
```

### Tcl

The Tool Command Language has always supported string interpolation in all quote-delimited strings.

```mw
set apples 4
puts "I have $apples apples."
```

The output will be:

```mw
I have 4 apples.
```

In order to actually format – and not simply replace – the values, there is a formatting function.

```mw
set apples 4
puts [format "I have %d apples." $apples]
```

### Visual Basic .NET

As of Visual Basic 14, string interpolation is supported in Visual Basic.

```mw
name = "Tom"
Console.WriteLine($"Hello, {name}")
```

The output will be:

```mw
Hello, Tom
```
