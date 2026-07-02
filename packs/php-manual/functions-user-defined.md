---
title: "PHP: User-defined functions"
source: https://www.php.net/manual/en/functions.user-defined.php
domain: php-manual
license: PHP-3.01 (docs CC-BY-3.0)
tags: php, php manual, php function, php script
fetched: 2026-07-02
---

# PHP: User-defined functions

PHP 8.2.32 Released!

## User-defined functions

A function is defined using the `function` keyword, a name, a list of parameters (which might be empty) separated by commas (`,`) enclosed in parentheses, followed by the body of the function enclosed in curly braces, such as the following:

**Example #1 Declaring a new function named `foo`**

> **Note**:
> 
> As of PHP 8.0.0, the list of parameters may have a trailing comma:

Any valid PHP code may appear inside the body of a function, even other functions and class definitions.

Function names follow the same rules as other labels in PHP. A valid function name starts with a letter or underscore, followed by any number of letters, numbers, or underscores. As a regular expression, it would be expressed thus: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`.

Tip

See also the Userland Naming Guide.

Functions need not be defined before they are referenced, *except* when a function is conditionally defined as shown in the two examples below.

When a function is defined in a conditional manner such as the two examples shown. Its definition must be processed *prior* to being called.

**Example #2 Conditional functions**

**Example #3 Functions within functions**

All functions and classes in PHP have the global scope - they can be called outside a function even if they were defined inside and vice versa.

PHP does not support function overloading, nor is it possible to undefine or redefine previously-declared functions.

> **Note**: Function names are case-insensitive for the ASCII characters `A` to `Z`, though it is usually good form to call functions as they appear in their declaration.

Both variable number of arguments and default arguments are supported in functions. See also the function references for func_num_args(), func_get_arg(), and func_get_args() for more information.

It is possible to call recursive functions in PHP. **Example #4 Recursive functions** **Note**: Recursive function/method calls with over 100-200 recursion levels can smash the stack and cause a termination of the current script. Especially, infinite recursion is considered a programming error.

### Found A Problem?

＋

add a note

### User Contributed Notes

There are no user contributed notes for this page.
