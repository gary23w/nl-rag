---
title: "PHP - Wikipedia (part 1/2)"
source: https://en.wikipedia.org/wiki/PHP
domain: hack-lang
license: CC-BY-SA-4.0
tags: hack language, hacklang, hhvm hack, facebook hack
fetched: 2026-07-02
part: 1/2
---

# PHP

**PHP** is a general-purpose scripting language geared towards web development. It was created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995. The PHP reference implementation is now produced by the PHP Group. PHP was originally an abbreviation of ***Personal Home Page***, but it now stands for the recursive backronym ***PHP: Hypertext Preprocessor***.

PHP code is usually processed on a web server by a PHP interpreter implemented as a module, a daemon or a Common Gateway Interface (CGI) executable. On a web server, the result of the interpreted and executed PHP code—which may be any type of data, such as generated HTML or binary image data—can form the whole or part of an HTTP response. Various web template systems, web content management systems, and web frameworks exist that can be employed to orchestrate or facilitate the generation of that response. PHP can be used for programming tasks outside the web context, though non-web uses are rare. PHP code can also be directly executed from the command line.

The standard PHP interpreter, powered by the Zend Engine, is free software released under the PHP License. PHP has been widely ported and can be deployed on most web servers on a variety of operating systems and platforms.


## History

The PHP language at first evolved without a written formal specification or standard, with the original implementation acting as the *de facto* standard that other implementations aimed to follow.

Rasmus Lerdorf

, creator of PHP; and

Andi Gutmans

and

Zeev Suraski

, creators of the

Zend Engine

### Early history (1993 to 1997)

PHP development began in 1993 when Rasmus Lerdorf wrote several Common Gateway Interface (CGI) programs in C, which he used to maintain his personal homepage. He extended them to work with HTML forms and to communicate with databases, and called this implementation "Personal Home Page/Forms Interpreter" or PHP/FI.

An example of the early PHP syntax:

```mw
<!--include /text/header.html-->

<!--getenv HTTP_USER_AGENT-->
<!--if substr $exec_result Mozilla-->
  Hey, you are using Netscape!<p>
<!--endif-->

<!--sql database select * from table where user='$username'-->
<!--ifless $numentries 1-->
  Sorry, that record does not exist<p>
<!--endif exit-->
  Welcome <!--$user-->!<p>
  You have <!--$index:0--> credits left in your account.<p>

<!--include /text/footer.html-->
```

PHP/FI could be used to build simple, dynamic web applications. To accelerate bug reporting and improve the code, Lerdorf initially announced the release of PHP/FI as "Personal Home Page Tools (PHP Tools) version 1.0" on the Usenet discussion group *comp.infosystems.www.authoring.cgi* on 8 June 1995. This release included basic functionality such as Perl-like variables, form handling, and the ability to embed HTML. By this point, the syntax had changed to resemble that of Perl, but was simpler, more limited, and less consistent.

Early PHP was never intended to be a new programming language; rather, it grew organically, with Lerdorf noting in retrospect: "I don't know how to stop it [...] there was never any intent to write a programming language [...] I have absolutely no idea how to write a programming language [...] I just kept adding the next logical step on the way." A development team began to form and, after months of work and beta testing, officially released PHP/FI 2 in November 1997.

The fact that PHP was not originally designed, but instead was developed organically has led to inconsistent naming of functions and inconsistent ordering of their parameters. In some cases, the function names were chosen to match the lower-level libraries which PHP was "wrapping", while in some very early versions of PHP the length of the function names was used internally as a hash function, so names were chosen to improve the distribution of hash values.

### PHP 3 and 4 (1998 to 2004)

Zeev Suraski and Andi Gutmans rewrote the parser in 1997 and formed the base of PHP 3, changing the language's name to the recursive acronym *PHP: Hypertext Preprocessor*. Afterwards, public testing of PHP 3 began, and the official launch came in June 1998. Suraski and Gutmans then started a new rewrite of PHP's core, producing the Zend Engine in 1999. They also founded Zend Technologies in Ramat Gan, Israel.

On 22 May 2000, PHP 4.0, powered by the Zend Engine 1.0, was released. By August 2008, this branch had reached version 4.4.9. PHP 4 is now no longer under development nor are any security updates planned to be released.

### Early PHP 5 (2004 to 2006)

On 1 July 2004, PHP 5.0 was released, powered by the new Zend Engine 2.0. PHP 5.0 included significant changes to the language, most notably an overhauled approach to object-oriented programming, as well as iterators and exceptions.

PHP 5.1 and PHP 5.2 were released the following years, adding smaller improvements and new features, such as the PHP Data Objects (PDO) extension (which defines a lightweight and consistent interface for accessing databases) In 2008, PHP 5.x became the only stable version under development.

Many high-profile open-source projects ceased to support PHP 4 in new code from February 5, 2008, because of the GoPHP5 initiative, provided by a consortium of PHP developers promoting the transition from PHP 4 to PHP 5.

### PHP 6 and Unicode

PHP's native string functions worked only on raw bytes, making use with multibyte character encodings difficult. In 2005, a project headed by Andrei Zmievski was initiated to bring native Unicode support throughout PHP, by embedding the International Components for Unicode (ICU) library, and representing text strings as UTF-16 internally. Since this would cause major changes both to the internals of the language and to user code, it was planned to release this as version 6.0 of the language, along with other major features then in development.

However, a shortage of developers who understood the necessary changes, and performance problems arising from conversion to and from UTF-16, which is rarely used in a web context, led to delays in the project. As a result, a PHP 5.3 release was created in 2009, and in March 2010, the project in its current form was officially abandoned, and a PHP 5.4 release was prepared to contain most remaining non-Unicode features from PHP 6. Initial hopes were that a new plan would be formed for Unicode integration, but by 2014 none had been adopted.

### Later PHP 5 (2009 to 2014)

Because it contained features originally intended to be part of 6.0, PHP 5.3 was a significant release, adding support for namespaces, closures, late static binding, and many fixes and improvements to standard functions.

With the Unicode branch officially abandoned, a new release process was adopted in 2011, planning a yearly release cycle, and a clear distinction between "feature releases" (x.y.z to x.y+1.z) and "major releases" (x.y.z to x+1.0.0). Remaining features which had been planned for the 6.0 release were included in PHP 5.4, released in March 2012, such as trait support and a new "short array syntax". This was followed by more incremental changes in PHP 5.5 (June 2013) and 5.6 (August 2014).

For PHP versions 5.3 and 5.4, the only available Microsoft Windows binary distributions were 32-bit IA-32 builds, requiring Windows 32-bit compatibility mode while using Internet Information Services (IIS) on a 64-bit Windows platform. PHP version 5.5 made the 64-bit x86-64 builds available for Microsoft Windows.

Official security support for PHP 5.6 ended on 31 December 2018.

### PHP 7.x (2015 to 2019)

During 2014 and 2015, a new major PHP version was developed, PHP 7.0. The numbering of this version involved some debate among internal developers. While the PHP 6 Unicode experiments had never been released, several articles and book titles referenced the PHP 6 names, which might have caused confusion if a new release were to reuse the name. After a vote, the name PHP 7 was chosen.

The foundation of PHP 7.0 was a PHP branch that was originally dubbed *PHP next generation* (*phpng*). It was written by Dmitry Stogov, Xinchen Hui and Nikita Popov, and aimed to optimize PHP performance by refactoring the Zend Engine while retaining near-complete language compatibility. By 14 July 2014, WordPress-based benchmarks, which served as the main benchmark suite for the phpng project, showed an almost 100% increase in performance. Changes from phpng make it easier to improve performance in future versions, as more compact data structures and other changes are seen as better suited for a successful migration to a just-in-time (JIT) compiler. Because of the significant changes, the reworked Zend Engine was called *Zend Engine 3*, succeeding Zend Engine 2 used in PHP 5.x.

PHP 7.0 also included changes which were not backward compatible, as allowed for "major versions" under the versioning scheme agreed in 2011. Changes to the core language included a more consistent handling of variable dereferencing, a more predictable behavior of the `foreach` statement, and platform consistency of bitwise shifts and floating-point to integer conversion. Several unmaintained or deprecated server application programming interfaces (SAPIs) and extensions were removed from the PHP core, most notably the legacy `mysql` extension. Other legacy features were also removed, such as ASP-style delimiters `<%` and `%>` and `<script language="php"> ... </script>`.

PHP 7.0 marked the beginning of an expansion in PHP's type system. In PHP 5.x, only function parameters could have type declarations, but this was extended to function return types in 7.0., and object properties in 7.4 The types expressible also expanded, with scalar types (integer, float, string, and boolean) in 7.0; `iterable` type, nullable types, and `void` return type. all in 7.1; and the `object` type in 7.2

Other changes in this period aimed to add expressiveness to the language, such as the `??` (null coalesce) and `<=>` "spaceship" three-way comparison operators in 7.0; new syntax for array derefencing and catching multiple exception types in PHP 7.1; more flexible Heredoc and Nowdoc syntax in 7.3; and the null-coalescing assignment operator in 7.4.

### PHP 8.x (2020 onwards)

PHP 8.0 was released on 26 November 2020, as a major version with breaking changes from previous versions.

One of the most high-profile changes was the addition of a JIT compiler, which can provide substantial performance improvements for some use cases. Substantial improvements were expected more for mathematical-type operations than for common web-development use cases. Additionally, the performance advantage of the JIT compiler provides the potential to move some code from C to PHP.

A significant addition to the language in 8.0 is attributes, which allow metadata to be added to program elements such as classes, methods, and parameters. Later versions added built-in attributes which change the behaviour of the language, such as the `#[\SensitiveParameter]` attribute in PHP 8.2, `#[\Override]` in PHP 8.3, `#[\Deprecated]` in PHP 8.4, and the `#[\NoDiscard]` and `#[\DelayedTargetValidation]` attributes in PHP 8.5.

A significant extension to the language's type system is the addition of composite types: union types in PHP 8.0 (e.g. `int|string` meaning "either integer or string"), intersection types in PHP 8.1 (e.g. `Traversable&Countable` meaning the value must implement both the `Traversable` and `Countable` interfaces), and disjunctive normal form (DNF) types in PHP 8.2 (unions of intersections, such as `array|(Traversable&Countable)`). Additional special type keywords have been added, such as `mixed` and `static` in PHP 8.0, `never` (a bottom type indicating that a function never returns) in PHP 8.1, and `null`, `false`, and `true` as stand-alone types in PHP 8.2.

The addition of a rich type system is part of a general trend towards a stricter language, and PHP 8.0 included breaking changes to the handling of string to number comparisons, numeric strings, and incompatible method signatures. Later versions have introduced deprecation notices for behaviour which is planned as a breaking change in a future major version, such as passing `null` to non-nullable internal function parameters and referring to properties which have not been declared on the class.

### Release history

| Version | Release date | Supported until | Notes |
|---|---|---|---|
| Unsupported: 1.0 | 8 June 1995 |   | Officially called "Personal Home Page Tools (PHP Tools)". This is the first use of the name "PHP". |
| Unsupported: 2.0 | 1 November 1997 |   | Officially called "PHP/FI 2.0". The first release that could be characterised as PHP, being a standalone language with many features that have endured to the present day. |
| Unsupported: 3.0 | 6 June 1998 | 20 October 2000 | Development moves from one person to multiple developers. Zeev Suraski and Andi Gutmans rewrote the base for this version. |
| Unsupported: 4.0 | 22 May 2000 | 23 June 2001 | Added a more advanced two-stage parse/execute tag-parsing system called the Zend Engine. |
| Unsupported: 4.1 | 10 December 2001 | 12 March 2002 | Introduced "superglobals" (`$_GET`, `$_POST`, `$_SESSION`, etc.) |
| Unsupported: 4.2 | 22 April 2002 | 6 September 2002 | Disabled `register_globals` by default. Data received over the network is not inserted directly into the global namespace anymore, closing possible security holes in applications. |
| Unsupported: 4.3 | 27 December 2002 | 31 March 2005 | Introduced the command-line interface (CLI), to supplement the CGI. |
| Unsupported: 4.4 | 11 July 2005 | 7 August 2008 | Fixed a memory corruption bug, which required breaking binary compatibility with extensions compiled against PHP version 4.3.x. |
| Unsupported: 5.0 | 13 July 2004 | 5 September 2005 | Zend Engine II with a new object model. |
| Unsupported: 5.1 | 24 November 2005 | 24 August 2006 | Performance improvements with the introduction of compiler variables in a re-engineered PHP Engine. Added PHP Data Objects (PDO) as a consistent interface for accessing databases. |
| Unsupported: 5.2 | 2 November 2006 | 6 January 2011 | Enabled the filter extension by default. Native JSON support. |
| Unsupported: 5.3 | 30 June 2009 | 14 August 2014 | Namespace support; late static bindings, jump label (limited goto), anonymous functions, closures, PHP archives (phar), garbage collection for circular references, improved Windows support, sqlite3, mysqlnd as a replacement for libmysql as the underlying library for the extensions that work with MySQL, fileinfo as a replacement for mime_magic for better MIME support, the Internationalization extension, and deprecation of the ereg extension. |
| Unsupported: 5.4 | 1 March 2012 | 3 September 2015 | Trait support, short array syntax support. Removed items: `register_globals`, `safe_mode`, `allow_call_time_pass_reference`, `session_register()`, `session_unregister()` and `session_is_registered()`. Built-in web server. Improvements to features and performance, reduced memory requirements. |
| Unsupported: 5.5 | 20 June 2013 | 10 July 2016 | Support for generators, `finally` blocks for exceptions handling, OpCache (based on Zend Optimizer+) bundled in official distribution. |
| Unsupported: 5.6 | 28 August 2014 | 31 December 2018 | Constant scalar expressions, variadic functions, argument unpacking, new exponentiation operator, extensions of the `use` statement for functions and constants, new `phpdbg` debugger as a SAPI module, and other smaller improvements. |
| 6.x | Not released | —N/a | Abandoned version of PHP that planned to include native Unicode support. |
| Unsupported: 7.0 | 3 December 2015 | 10 January 2019 | Zend Engine 3 (performance improvements and 64-bit integer support on Windows), uniform variable syntax, AST-based compilation process, added `Closure::call()`, bitwise shift consistency across platforms, `??` (null coalesce) operator, Unicode code point escape syntax, return type declarations, scalar type (integer, float, string and boolean) declarations, `<=>` "spaceship" three-way comparison operator, generator delegation, anonymous classes, simpler and more consistently available CSPRNG API, replacement of many remaining internal PHP "errors" with the more modern exceptions, and shorthand syntax for importing multiple items from a namespace. |
| Unsupported: 7.1 | 1 December 2016 | 1 December 2019 | `iterable` type, nullable types, `void` return type, class constant visibility modifiers, short list syntax, multi-catch |
| Unsupported: 7.2 | 30 November 2017 | 30 November 2020 | `object` parameter and return type declaration, libsodium extension, abstract method overriding, parameter type widening |
| Unsupported: 7.3 | 6 December 2018 | 6 December 2021 | Flexible Heredoc and Nowdoc syntax, support for reference assignment and array deconstruction with `list()`, PCRE2 support, `hrtime` function |
| Unsupported: 7.4 | 28 November 2019 | 28 November 2022 | Typed properties, preloading, null-coalescing assignment operator, improve `openssl_random_pseudo_bytes`, weak references, foreign function interface (FFI), always available hash extension, password hash registry, multibyte string splitting, reflection for references, unbundle ext/wddx, new custom object serialization mechanism |
| Unsupported: 8.0 | 26 November 2020 | 26 November 2023 | Just-In-Time (JIT) compilation, arrays starting with a negative index, stricter/saner language semantics (validation for abstract trait methods), saner string to number comparisons, saner numeric strings, `TypeError` on invalid arithmetic/bitwise operators, reclassification of various engine errors, consistent type errors for internal functions, fatal error for incompatible method signatures, locale-independent float to string conversion, variable syntax tweaks, attributes, named arguments, match expression, constructor property promotion, union types, `mixed` type, static return type, nullsafe operator, non-capturing catches, `throw` expression, JSON extension is always available. |
| Unsupported: 8.1 | 25 November 2021 | 31 December 2025 | Explicit octal integer literal notation, enumerations, read-only properties, first-class callable syntax, `new` in initializers, pure intersection types, `never` return type, `final` class constraints, fibers |
| Supported: 8.2 | 8 December 2022 | 31 December 2026 | Readonly classes, `null`, `false`, and `true` as stand-alone types, locale-independent case conversion, disjunctive normal form types, constants in traits |
| Supported: 8.3 | 23 November 2023 | 31 December 2027 | Typed class constants, dynamic class constant fetch, `#[\Override]` attribute, deep-cloning of read-only properties, new `json_validate` function, randomizer additions, the command-line linter supports multiple files |
| Supported: 8.4 | 21 November 2024 | 31 December 2028 | Property hooks, asymmetric visibility, an updated DOM API, performance improvements, bug fixes, and general cleanup. |
| Latest version: 8.5 | 20 November 2025 | 31 December 2029 | Pipe operator `\|>` |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

Beginning on 28 June 2011, the PHP Development Team implemented a timeline for the release of new versions of PHP. Under this system, at least one release should occur every month. Once per year, a minor release should occur which may include new features. Every minor release should at least be supported for two years with security and bug fixes, followed by at least one year of only security fixes, for a total of a three-year release process for every minor release. No new features, unless small and self-contained, are to be introduced into a minor release during the three-year release process. A 2024 RFC extended the length of the security fix only period to two years, fixed all end of life dates to 31 December, and removed the exception that allowed for "small and self-contained" features to be introduced in patch versions.

#### Prevalence of outdated versions

W3Techs reports that as of November 2025 (about three years since PHP 7 was discontinued and 23 months after the PHP 8.3 release), unsupported versions such as PHP 7 are still used by well over half of PHP websites, which are outdated and known to be insecure. Those included the 9.7% of PHP websites using the even more outdated (discontinued for 7 years) and insecure PHP 5, released over two decades ago.


## Mascot

The mascot of the PHP project is the *elePHPant*, a blue elephant with the PHP logo on its side, designed by Vincent Pontier in 1998. "The (PHP) letters were forming the shape of an elephant if viewed in a sideways angle."

The elePHPant is sometimes differently coloured when in plush toy form. Many variations of this physical mascot have been made over the years. Only the elePHPants based on the original design by Vincent Pontier are considered official by the community. These are collectable and some of them are extremely rare.


## Syntax

The following "Hello, World!" program is written in PHP code embedded in an HTML document:

```mw
<!DOCTYPE html>
<html>
    <head>
        <title>PHP "Hello, World!" program</title>
    </head>
    <body>
        <p><?= 'Hello, World!' ?></p>
    </body>
</html>
```

The PHP interpreter only executes PHP code within its delimiters. Anything outside its delimiters is not processed by PHP, although the non-PHP text can still be subject to control structures described in PHP code. `<?php` is used to open and `?>` to close PHP sections. A shorthand `<?=` exists, which is a shorthand for `<?php echo`. The shortened form `<?` also exists, which makes script files less portable since support can be disabled in the local PHP configuration. The shortened form is discouraged by the PHP Group for this reason. Conversely, there is no recommendation against the echo short tag `<?=`. Prior to PHP 5.4.0, the short syntax for `echo` only works with the `short_open_tag` configuration setting enabled, while for PHP 5.4.0 and later it is always available. The purpose of delimiters is to separate PHP code from non-PHP content, such as JavaScript code or HTML markup.

The first form of delimiters, `<?php` and `?>`, in XHTML and other XML documents, creates correctly formed XML processing instructions. This means that the resulting mixture of PHP code and other markup in the server-side file is itself well-formed XML.

Variables are prefixed with a dollar symbol, and a type does not need to be specified in advance. PHP 5 introduced type declarations that allow functions to force their parameters to be objects of a specific class, arrays, interfaces or callback functions. However, before PHP 7, type declarations could not be used with scalar types such as integers or strings.

Below is an example of how PHP variables are declared and initialized.

```mw
<?php
    $name = 'John';  // variable of string type being declared and initialized
    $age = 18;       // variable of integer type being declared and initialized
    $height = 5.3;   // variable of double type being declared and initialized
    echo $name . ' is ' . $height . "m tall\n"; // concatenating variables and strings
    echo "$name is $age years old."; // interpolating variables to string
?>
```

Unlike function and class names, variable names are case-sensitive. Both double-quoted ("") and heredoc strings provide the ability to interpolate a variable's value into the string. PHP treats newlines as whitespace in the manner of a free-form language, and statements are terminated by a semicolon. PHP has three types of comments: `/* */` marks block and inline comments; `//` or `#` are used for one-line comments. The `echo` statement is one of several keywords PHP provides to output text.

In terms of keywords and language syntax, PHP is similar to C-style syntax. `if` conditions, `for` and `while` loops and function returns are similar in syntax to languages such as C, C++, C#, Java and Perl.

### Data types

PHP is loosely typed. It stores integers in a platform-dependent range, either as a 32, 64 or 128-bit signed integer equivalent to the C-language long type. Unsigned integers are converted to signed values in certain situations, which is different behaviour to many other programming languages. Integer variables can be assigned using decimal (positive and negative), octal, hexadecimal, and binary notations.

Floating-point numbers are also stored in a platform-specific range. They can be specified using floating-point notation, or two forms of scientific notation. PHP has a native Boolean type that is similar to the native Boolean types in Java and C++. Using the Boolean type conversion rules, non-zero values are interpreted as true and zero as false, as in Perl and C++.

The null data type represents a variable that has no value; `NULL` is the only allowed value for this data type.

Variables of the "resource" type represent references to resources from external sources. These are typically created by functions from a particular extension, and can only be processed by functions from the same extension; examples include file, image, and database resources.

Arrays can contain elements of any type that PHP can handle, including resources, objects, and even other arrays. Order is preserved in lists of values and in hashes with both keys and values, and the two can be intermingled. PHP also supports strings, which can be used with single quotes, double quotes, nowdoc or heredoc syntax.

The **Standard PHP Library** (SPL) attempts to solve standard problems and implements efficient data access interfaces and classes.

### Functions

PHP defines a large array of functions in the core language and many are also available in various extensions; these functions are well documented online PHP documentation. However, the built-in library has a wide variety of naming conventions and associated inconsistencies, as described under history above.

Custom functions may be defined by the developer:

```mw
function myAge(int $birthYear): string
{
    // calculate the age by subtracting the birth year from the current year.
    $yearsOld = date('Y') - $birthYear;

    // return the age in a descriptive string.
    return $yearsOld . ($yearsOld == 1 ? ' year' : ' years');
}

echo 'I am currently ' . myAge(1995) . ' old.';
```

As of 2026, the output of the above sample program is "I am currently 31 years old."

In lieu of function pointers, functions in PHP can be referenced by a string containing their name. In this manner, normal PHP functions can be used, for example, as callbacks or within function tables. User-defined functions may be created at any time without being prototyped. Functions may be defined inside code blocks, permitting a run-time decision as to whether or not a function should be defined. There is a `function_exists` function that determines whether a function with a given name has already been defined. Function calls must use parentheses, with the exception of zero-argument class constructor functions called with the PHP operator `new`, in which case parentheses are optional.

Since PHP 4.0.1 `create_function()`, a thin wrapper around `eval()`, allowed normal PHP functions to be created during program execution; it was deprecated in PHP 7.2 and removed in PHP 8.0 in favor of syntax for anonymous functions or "closures" that can capture variables from the surrounding scope, which was added in PHP 5.3. Shorthand arrow syntax was added in PHP 7.4:

```mw
function getAdder($x) {
    return fn($y) => $x + $y;
}

$adder = getAdder(8);
echo $adder(2);  // prints "10"
```

In the example above, `getAdder()` function creates a closure using passed argument `$x`, which takes an additional argument `$y`, and returns the created closure to the caller. Such a function is a first-class object, meaning that it can be stored in a variable, passed as a parameter to other functions, etc.

Unusually for a dynamically typed language, PHP supports type declarations on function parameters, which are enforced at runtime. This has been supported for classes and interfaces since PHP 5.0, for arrays since PHP 5.1, for "callables" since PHP 5.4, and scalar (integer, float, string and boolean) types since PHP 7.0. PHP 7.0 also has type declarations for function return types, expressed by placing the type name after the list of parameters, preceded by a colon. For example, the `getAdder` function from the earlier example could be annotated with types like so in PHP 7:

```mw
function getAdder(int $x): Closure
{
    return fn(int $y): int => $x + $y;
}

$adder = getAdder(8);
echo $adder(2); // prints "10"
echo $adder(null); // throws an exception because an incorrect type was passed
$adder = getAdder([]); // would also throw an exception
```

By default, scalar type declarations follow weak typing principles. So, for example, if a parameter's type is `int`, PHP would allow not only integers, but also convertible numeric strings, floats or Booleans to be passed to that function, and would convert them. However, PHP 7 has a "strict typing" mode which, when used, disallows such conversions for function calls and returns within a file.

### PHP objects

Basic object-oriented programming functionality was added in PHP 3 and improved in PHP 4. This allowed for PHP to gain further abstraction, making creative tasks easier for programmers using the language. Object handling was completely rewritten for PHP 5, expanding the feature set and enhancing performance. In previous versions of PHP, objects were handled like value types. The drawback of this method was that code had to make heavy use of PHP's "reference" variables if it wanted to modify an object it was passed rather than creating a copy of it. In the new approach, objects are referenced by handle, and not by value.

PHP 5 introduced private and protected member variables and methods, along with abstract classes, final classes, abstract methods, and final methods. It also introduced a standard way of declaring constructors and destructors, similar to that of other object-oriented languages such as C++, and a standard exception handling model. Furthermore, PHP 5 added interfaces and allowed for multiple interfaces to be implemented. There are special interfaces that allow objects to interact with the runtime system. Objects implementing ArrayAccess can be used with array syntax and objects implementing Iterator or IteratorAggregate can be used with the `foreach` language construct. There is no virtual table feature in the engine, so static variables are bound with a name instead of a reference at compile time.

If the developer creates a copy of an object using the reserved word `clone`, the Zend engine will check whether a `__clone()` method has been defined. If not, it will call a default `__clone()` which will copy the object's properties. If a `__clone()` method is defined, then it will be responsible for setting the necessary properties in the created object. For convenience, the engine will supply a function that imports the properties of the source object, so the programmer can start with a by-value replica of the source object and only override properties that need to be changed.

The visibility of PHP properties and methods is defined using the keywords `public`, `private`, and `protected`. The default is public, if only var is used; `var` is a synonym for `public`. Items declared `public` can be accessed everywhere. `protected` limits access to inherited classes (and to the class that defines the item). `private` limits visibility only to the class that defines the item. Objects of the same type have access to each other's private and protected members even though they are not the same instance.

#### Example

The following is a basic example of object-oriented programming in PHP 8:

```mw
<?php

abstract class User
{
    protected string $name;

    public function __construct(string $name)
    {
        // make first letter uppercase and the rest lowercase
        $this->name = ucfirst(strtolower($name));
    }

    public function greet(): string
    {
        return "Hello, my name is " . $this->name;
    }

    abstract public function job(): string;
}

class Student extends User
{
    public function __construct(string $name, private string $course)
    {
        parent::__construct($name);
    }

    public function job(): string
    {
        return "I learn " . $this->course;
    }
}

class Teacher extends User
{
    public function __construct(string $name, private array $teachingCourses)
    {
        parent::__construct($name);
    }

    public function job(): string
    {
        return "I teach " . implode(", ", $this->teachingCourses);
    }
}

$students = [
    new Student("Alice", "Computer Science"),
    new Student("Bob", "Computer Science"),
    new Student("Charlie", "Business Studies"),
];

$teachers = [
    new Teacher("Dan", ["Computer Science", "Information Security"]),
    new Teacher("Erin", ["Computer Science", "3D Graphics Programming"]),
    new Teacher("Frankie", ["Online Marketing", "Business Studies", "E-commerce"]),
];

foreach ([$students, $teachers] as $users) {
    echo $users[0]::class . "s:\n";

    array_walk($users, function (User $user) {
        echo "{$user->greet()}, {$user->job()}\n";
    });
}
```

This program outputs the following:

```mw
Students:
Hello, my name is Alice, I learn Computer Science
Hello, my name is Bob, I learn Computer Science
Hello, my name is Charlie, I learn Business Studies
Teachers:
Hello, my name is Dan, I teach Computer Science, Information Security
Hello, my name is Erin, I teach Computer Science, 3D Graphics Programming
Hello, my name is Frankie, I teach Online Marketing, Business Studies, E-commerce
```


## Implementations

The only complete PHP implementation is the original, known simply as PHP. It is the most widely used and is powered by the Zend Engine. To disambiguate it from other implementations, it is sometimes unofficially called "Zend PHP". The Zend Engine compiles PHP source code on-the-fly into an internal format that it can execute, thus it works as an interpreter. It is also the "reference implementation" of PHP, as PHP has no formal specification, and so the semantics of Zend PHP define the semantics of PHP. Due to the complex and nuanced semantics of PHP, defined by how Zend works, it is difficult for competing implementations to offer complete compatibility.

PHP's single-request-per-script-execution model, and the fact that the Zend Engine is an interpreter, leads to inefficiency; as a result, various products have been developed to help improve PHP performance. To speed up execution time and not have to compile the PHP source code every time the web page is accessed, PHP scripts can also be deployed in the PHP engine's internal format by using an opcode cache, which works by caching the compiled form of a PHP script (opcodes) in shared memory to avoid the overhead of parsing and compiling the code every time the script runs. An opcode cache, Zend Opcache, is built into PHP since version 5.5. Another example of a widely used opcode cache is the Alternative PHP Cache (APC), which is available as a PECL extension.

While Zend PHP is still the most popular implementation, several other implementations have been developed. Some of these are compilers or support JIT compilation, and hence offer performance benefits over Zend PHP at the expense of lacking full PHP compatibility. Alternative implementations include the following:

- HHVM (HipHop Virtual Machine) – developed at Facebook and available as open source, it converts PHP code into a high-level bytecode (commonly known as an intermediate language), which is then translated into x86-64 machine code dynamically at runtime by a just-in-time (JIT) compiler, resulting in up to 6× performance improvements. However, since version 7.2 Zend has outperformed HHVM, and HHVM 3.24 is the last version to officially support PHP.
  - HipHop – developed at Facebook and available as open source, it transforms the PHP scripts into C++ code and then compiles the resulting code, reducing the server load up to 50%. In early 2013, Facebook deprecated it in favour of HHVM due to multiple reasons, including deployment difficulties and lack of support for the whole PHP language, including the `create_function()` and `eval()` constructs.
- Parrot – a virtual machine designed to run dynamic languages efficiently; the cross-translator Pipp transforms the PHP source code into the Parrot intermediate representation, which is then translated into the Parrot's bytecode and executed by the virtual machine.
- PeachPie – a second-generation compiler to .NET Common Intermediate Language (CIL) bytecode, built on the Roslyn platform; successor of Phalanger, sharing several architectural components
- Phalanger – compiles PHP into .Net Common Intermediate Language bytecode; predecessor of PeachPie
- Quercus – compiles PHP into Java bytecode


## Licensing

PHP is free software released under the PHP License, which is equivalent to the 3-clause BSD license.

Versions prior to 8.6 were released under a more restrictive license, which stipulates that:

> Products derived from this software may not be called "PHP", nor may "PHP" appear in their name, without prior written permission from group@php.net. You may indicate that your software works in conjunction with PHP by saying "Foo for PHP" instead of calling it "PHP Foo" or "phpfoo".

This restriction on the use of "PHP" made the PHP License incompatible with the GNU General Public License (GPL), while the Zend License was incompatible due to an advertising clause similar to that of the original BSD license.


## Development and community

PHP includes various free and open-source libraries in its source distribution or uses them in resulting PHP binary builds. PHP is fundamentally an Internet-aware system with built-in modules for accessing File Transfer Protocol (FTP) servers and many database servers, including PostgreSQL, MySQL, Microsoft SQL Server and SQLite (which is an embedded database), LDAP servers, and others. Numerous functions are familiar to C programmers, such as those in the stdio family, are available in standard PHP builds.

PHP allows developers to write extensions in C to add functionality to the PHP language. PHP extensions can be compiled statically into PHP or loaded dynamically at runtime. Numerous extensions have been written to add support for the Windows API, process management on Unix-like operating systems, multibyte strings (Unicode), cURL, and several popular compression formats. Other PHP features made available through extensions include integration with Internet Relay Chat (IRC), dynamic generation of images and Adobe Flash content, *PHP Data Objects* (PDO) as an abstraction layer used for accessing databases, and even speech synthesis. Some of the language's core functions, such as those dealing with strings and arrays, are also implemented as extensions. The PHP Extension Community Library (PECL) project is a repository for extensions to the PHP language. Most of the community focuses on web development, and PHP running server side (though also serving JavaScript for the client side), and some exceptional uses are for e.g. standalone graphical applications (with PHP-GTK unmaintained now for over a decade), and even drone control.

Some other projects, such as *Zephir*, provide the ability for PHP extensions to be created in a high-level language and compiled into native PHP extensions. Such an approach, instead of writing PHP extensions directly in C, simplifies the development of extensions and reduces the time required for programming and testing.

By December 2018 the PHP Group consisted of ten people: Thies C. Arntzen, Stig Bakken, Shane Caraveo, Andi Gutmans, Rasmus Lerdorf, Sam Ruby, Sascha Schumann, Zeev Suraski, Jim Winstead, and Andrei Zmievski.

Zend Technologies provides a PHP Certification based on PHP 8 exam (and previously based on PHP 7 and 5.5) for programmers to become certified PHP developers.


## The PHP Foundation

On 26 November 2021, the JetBrains blog announced the creation of The PHP Foundation, which will sponsor the design and development of PHP.

| Year | Commits | Reviews | RFCs |
|---|---|---|---|
| 2022 | 683 | 283 | 8 |
| 2023 | 784 | 702 | 17 |
| 2024 | 1976 | 1278 | 13 |

The foundation hires "Core Developers" to work on the PHP language's core repository. Roman Pronskiy, a member of the foundation's board, said that they aim to pay "market salaries" to developers.

The response to the foundation has been largely positive.

Germany's Sovereign Tech Fund provided more than 200,000 Euros to support the PHP Foundation.


## Installation and configuration

There are two primary ways for adding support for PHP to a web server – as a native web server module, or as a CGI executable. PHP has a direct module interface called server application programming interface (SAPI), which is supported by many web servers including Apache HTTP Server, Microsoft IIS, Caddy (through FrankenPHP) and iPlanet Web Server. Some other web servers, such as OmniHTTPd, support the Internet Server Application Programming Interface (ISAPI), which is Microsoft's web server module interface. If PHP has no module support for a web server, it can always be used as a Common Gateway Interface (CGI) or FastCGI processor; in that case, the web server is configured to use PHP's CGI executable to process all requests to PHP files.

PHP-FPM (FastCGI Process Manager) is an alternative FastCGI implementation for PHP, bundled with the official PHP distribution since version 5.3.3. When compared to the older FastCGI implementation, it contains some additional features, mostly useful for heavily loaded web servers.

When using PHP for command-line scripting, a PHP command-line interface (CLI) executable is needed. PHP supports a CLI server application programming interface (SAPI) since PHP 4.3.0. The main focus of this SAPI is developing shell applications using PHP. There are quite a few differences between the CLI SAPI and other SAPIs, although they do share many of the same behaviours.

PHP has a direct module interface called SAPI for different web servers; in case of PHP 5 and Apache 2.0 on Windows, it is provided in form of a DLL file called php5apache2.dll, which is a module that, among other functions, provides an interface between PHP and the web server, implemented in a form that the server understands. This form is what is known as a SAPI.

There are different kinds of SAPIs for various web server extensions. For example, in addition to those listed above, other SAPIs for the PHP language include the Common Gateway Interface and command-line interface.

PHP can also be used for writing desktop graphical user interface (GUI) applications, by using the *"PHP Desktop". *GitHub*.* or discontinued PHP-GTK extension. PHP-GTK is not included in the official PHP distribution, and as an extension, it can be used only with PHP versions 5.1.0 and newer. The most common way of installing PHP-GTK is by compiling it from the source code.

When PHP is installed and used in cloud environments, software development kits (SDKs) are provided for using cloud-specific features. For example:

- Amazon Web Services provides the AWS SDK for PHP
- Microsoft Azure can be used with the Windows Azure SDK for PHP.

Numerous configuration options are supported, affecting both core PHP features and extensions. Configuration file `php.ini` is searched for in different locations, depending on the way PHP is used. The configuration file is split into various sections, while some of the configuration options can be also set within the web server configuration.
