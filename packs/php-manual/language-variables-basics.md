---
title: "PHP: Basics"
source: https://www.php.net/manual/en/language.variables.basics.php
domain: php-manual
license: PHP-3.01 (docs CC-BY-3.0)
tags: php, php manual, php function, php script
fetched: 2026-07-02
---

# PHP: Basics

PHP 8.2.32 Released!

## Basics

Variables in PHP are represented by a dollar sign followed by the name of the variable. The variable name is case-sensitive.

A valid variable name starts with a letter (`A-Z`, `a-z`, or the bytes from 128 through 255) or underscore, followed by any number of letters, numbers, or underscores. As a regular expression, it would be expressed thus: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`

> **Note**: PHP doesn't support Unicode variable names, however, some character encodings (such as UTF-8) encode characters in such a way that all bytes of a multi-byte character fall within the allowed range, thus making it a valid variable name.

> **Note**: `$this` is a special variable that can't be assigned. Prior to PHP 7.1.0, indirect assignment (e.g. by using variable variables) was possible.

Tip

See also the Userland Naming Guide.

**Example #1 Valid variable names**

**Example #2 Invalid variable names**

PHP accepts a sequence of any bytes as a variable name. Variable names that do not follow the above-mentioned naming rules can only be accessed dynamically at runtime. See variable variables for information on how to access them.

**Example #3 Accessing obscure variable names**

By default, variables are always assigned by value. That is to say, when an expression is assigned to a variable, the entire value of the original expression is copied into the destination variable. This means, for instance, that after assigning one variable's value to another, changing one of those variables will have no effect on the other. For more information on this kind of assignment, see the chapter on Expressions.

PHP also offers another way to assign values to variables: assign by reference. This means that the new variable simply references (in other words, "becomes an alias for" or "points to") the original variable. Changes to the new variable affect the original, and vice versa.

To assign by reference, simply prepend an ampersand (&) to the beginning of the variable which is being assigned (the source variable). For instance, the following code snippet outputs '`My name is Bob`' twice:

One important thing to note is that only variables may be assigned by reference.

It is not necessary to declare variables in PHP, however, it is a very good practice. Accessing an undefined variable will result in an **`E_WARNING`** (prior to PHP 8.0.0, **`E_NOTICE`**). An undefined variable has a default value of **`null`**. The isset() language construct can be used to detect if a variable has already been initialized.

**Example #4 Default value of an uninitialized variable**

PHP allows array autovivification (automatic creation of new arrays) from an undefined variable. Appending an element to an undefined variable will create a new array and will not generate a warning.

**Example #5 Autovivification of an array from an undefined variable**

Warning

Relying on the default value of an uninitialized variable is problematic when including one file in another which uses the same variable name.

A variable can be destroyed by using the unset() language construct.

For information on variable-related functions, see the Variable Functions Reference.

### Found A Problem?

＋

add a note

### User Contributed Notes

There are no user contributed notes for this page.
