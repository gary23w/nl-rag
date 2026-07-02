---
title: "PHP: Introduction"
source: https://www.php.net/manual/en/language.types.intro.php
domain: php-manual
license: PHP-3.01 (docs CC-BY-3.0)
tags: php, php manual, php function, php script
fetched: 2026-07-02
---

# PHP: Introduction

PHP 8.2.32 Released!

## Introduction

Every single expression in PHP has one of the following built-in types depending on its value: null bool int float (floating-point number) string array object callable resource

PHP is a dynamically typed language, which means that by default there is no need to specify the type of a variable, as this will be determined at runtime. However, it is possible to statically type some aspect of the language via the use of type declarations. Different types that are supported by PHP's type system can be found at the type system page.

Types restrict the kind of operations that can be performed on them. However, if an expression/variable is used in an operation which its type does not support, PHP will attempt to type juggle the value into a type that supports the operation. This process depends on the context in which the value is used. For more information, see the section on Type Juggling.

Tip

The type comparison tables may also be useful, as various examples of comparison between values of different types are present.

> **Note**: It is possible to force an expression to be evaluated to a certain type by using a type cast. A variable can also be type cast in-place by using the settype() function on it.

To check the value and type of an expression, use the var_dump() function. To retrieve the type of an expression, use the get_debug_type() function. However, to check if an expression is of a certain type use the `is_type` functions instead. **Example #1 Different Types**

> **Note**: Prior to PHP 8.0.0, where the get_debug_type() is not available, the gettype() function can be used instead. However, it doesn't use the canonical type names.

### Found A Problem?

＋

add a note

### User Contributed Notes

There are no user contributed notes for this page.
