---
title: "S-expression"
source: https://en.wikipedia.org/wiki/S-expression
domain: newlisp
license: CC-BY-SA-4.0
tags: newlisp language, lisp language, scripting language, interpreter computing, s expression
fetched: 2026-07-02
---

# S-expression

In computer programming, an **S-expression** (or **symbolic expression**, abbreviated as **sexpr** or **sexp**) is an expression in a like-named notation for nested list (tree-structured) data. S-expressions were invented for, and popularized by, the programming language Lisp, which uses them for source code as well as data.

## Characteristics

In the usual parenthesized syntax of Lisp, an S-expression is classically defined as

1. an atom of the form *x*, or
2. an expression of the form (*x* . *y*) where *x* and *y* are S-expressions.

This definition reflects LISP's representation of a list as a series of "cells", each one an ordered pair. In plain lists, *y* points to the next cell (if any), thus forming a list. The recursive clause of the definition means that both this representation and the S-expression notation can represent any binary tree. However, the representation can in principle allow circular references, in which case the structure is not a tree at all, but a cyclic graph, and cannot be represented in classical S-expression notation unless a convention for cross-reference is provided, analogous to SQL foreign keys, SGML/XML IDREFs, etc. Modern Lisp dialects such as Common Lisp and Scheme provide such syntax via *datum labels*, with which objects can be marked, which can then recur elsewhere, indicating shared rather than duplicated structure, enabling the reader or printer to detect and thus trigger evaluation or display of cycles without infinitely recursing

#n=(

x

y

. #n#)

The definition of an atom varies per context; in the original definition by John McCarthy, it was assumed that there existed "an infinite set of distinguishable atomic symbols" represented as "strings of capital Latin letters and digits with single embedded blanks" (a subset of character string and numeric literals).

Most modern sexpr notations allow more general quoted strings (for example including punctuation or full Unicode), and use an abbreviated notation to represent lists with more than 2 members, so that

(

x

y

z

)

stands for

(

x

. (

y

. (

z

. NIL)))

`NIL` is the special end-of-list object (alternatively written `()`, which is the only representation in Scheme).

In the Lisp family of programming languages, S-expressions are used to represent both source code and data. Other uses of S-expressions are in Lisp-derived languages such as DSSSL, and as mark-up in communication protocols like IMAP and John McCarthy's CBCL. It is also used as text representation of WebAssembly. The details of the syntax and supported data types vary in the different languages, but the most common feature among these languages is the use of S-expressions and prefix notation.

## Datatypes and syntax

There are many variants of the S-expression format, supporting a variety of different syntaxes for different datatypes. The most widely supported are:

- *Lists and pairs*: `(1 () (2 . 3) (4))`
- *Symbols*: `with-hyphen` `?@!$` `|a symbol with spaces|`
- *Strings*: `"Hello, world!"`
- *Integers*: `-9876543210`
- *Floating-point numbers*: `-0.0` `6.28318` `6.022e23`

The character `#` is often used to prefix extensions to the syntax, e.g. `#x10` for hexadecimal integers, or `#\C` for characters.

## Uses

### Use in Lisp

When representing source code in Lisp, the first element of an S-expression is commonly an operator or function name and any remaining elements are treated as arguments. This is called "prefix notation" or "Polish notation". As an example, the Boolean expression written `4 == (2 + 2)` in C, is represented as `(= 4 (+ 2 2))` in Lisp's s-expr-based prefix notation.

As noted above, the precise definition of "atom" varies across LISP-like languages. A quoted string can typically contain anything but a quote, while an unquoted identifier atom can typically contain anything but quotes, whitespace characters, parentheses, brackets, braces, backslashes, and semicolons. In either case, a prohibited character can typically be included by escaping it with a preceding backslash. Unicode support varies.

The recursive case of the definition of S-expressions is traditionally implemented using cons cells.

S-expressions were originally intended only for data to be manipulated by M-expressions, but the first implementation of Lisp was an interpreter of S-expression encodings of M-expressions, and Lisp programmers soon became accustomed to using S-expressions for both code and data. This means that Lisp is homoiconic; that is, the primary representation of programs is also a data structure in a primitive type of the language itself.

Nested lists can be written as S-expressions: `((milk juice) (honey marmalade))` is a two-element S-expression whose elements are also two-element S-expressions. The whitespace-separated notation used in Lisp (and this article) is typical. Line breaks (newline characters) usually qualify as separators. This is a simple context-free grammar for a tiny subset of English written as an S-expression, where S = sentence, NP = Noun Phrase, VP = Verb Phrase, V = Verb:

```mw
(((S) (NP VP))
 ((VP) (V))
 ((VP) (V NP))
 ((V) died)
 ((V) employed)
 ((NP) nurses)
 ((NP) patients)
 ((NP) Medicenter)
 ((NP) "Dr Chan"))
```

Program code can be written in S-expressions, usually using prefix notation. Example in Common Lisp:

```mw
(defun factorial (x)
   (if (zerop x)
       1
       (* x (factorial (- x 1)))))
```

S-expressions can be read in Lisp using the function READ. READ reads the textual representation of an S-expression and returns Lisp data. The function PRINT can be used to output an S-expression. The output then can be read with the function READ, when all printed data objects have a readable representation. Lisp has readable representations for numbers, strings, symbols, lists and many other data types. Program code can be formatted as pretty printed S-expressions using the function PPRINT (note: with two Ps, short for *pretty*-print).

Lisp programs are valid S-expressions, but not all S-expressions are valid Lisp programs. `(1.0 + 3.1)` is a valid S-expression, but not a valid Lisp program, since Lisp uses prefix notation and a floating point number (here 1.0) is not valid as an operation (the first element of the expression).

An S-expression preceded by a single quotation mark, as in `'x`, is syntactic sugar for a quoted S-expression, in this case `(quote x)`.

### Other uses

S-expressions are also used for WebAssembly text format.

## Relation to XML

S-expressions are often compared to XML: one key difference is that S-expressions have just one form of containment, the dotted pair, while XML tags can contain simple attributes, other tags, or CDATA, each using different syntax. Another is that S-expressions do not define a reference mechanism, whereas XML provides a notion of unique identifiers and references to them. For simple use cases, S-expressions are simpler than XML, but for more advanced use cases, XML has a query language called XPath which many tools and third party libraries use to simplify the handling of XML data.

## Standardization

Standards for some Lisp-derived programming languages include a specification for their S-expression syntax. These include Common Lisp (ANSI standard document ANSI INCITS 226-1994 (R2004)), Scheme (R5RS and R6RS), and ISLISP.

In May 1997, Ron Rivest submitted an Internet Draft to be considered for publication as an RFC. The draft defined a syntax based on Lisp S-expressions but intended for general-purpose data storage and exchange (similar to XML) rather than specifically for programming. It was never approved as an RFC, but it has since been cited and used by other RFCs (e.g. RFC 2693) and several other publications. It was originally intended for use in SPKI.

Rivest's format defines an S-expression as being either an octet-string (a series of bytes) or a finite list of other S-expressions. It describes three interchange formats for expressing this structure. One is the "advanced transport", which is very flexible in terms of formatting, and is syntactically similar to Lisp-style expressions, but they are not identical. The advanced transport, for example, allows octet-strings to be represented verbatim (the string's length followed by a colon and the entire raw string), a quoted form allowing escape characters, hexadecimal, Base64, or placed directly as a "token" if it meets certain conditions. (Rivest's tokens differ from Lisp tokens in that the former are just for convenience and aesthetics, and treated exactly like other strings, while the latter have specific syntactical meaning.)

Rivest's draft defines a canonical representation "for digital signature purposes". It is intended to be compact, easier to parse, and unique for any abstract S-expression. It only allows verbatim strings, and prohibits whitespace as formatting outside strings. Finally there is the "basic transport representation", which is either the canonical form or the same encoded as Base64 and surrounded by braces, the latter intended to safely transport a canonically encoded S-expression in a system which might change spacing (e.g. an email system which has 80-character-wide lines and wraps anything longer than that).

This format has not been widely adapted for use outside of SPKI (some of the users being GnuPG, libgcrypt, Nettle, and GNU lsh). Rivest's S-expressions web page provides C source code for a parser and generator (available under the MIT license), which could be adapted and embedded into other programs. In addition, there are no restrictions on independently implementing the format.
