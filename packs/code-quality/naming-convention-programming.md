---
title: "Naming convention (programming)"
source: https://en.wikipedia.org/wiki/Naming_convention_(programming)
domain: code-quality
license: CC-BY-SA-4.0
tags: refactoring, code smell, technical debt, cyclomatic complexity, coupling, clean code
fetched: 2026-07-02
---

# Naming convention (programming)

In computer programming, a **naming convention** is a set of rules for choosing the character sequence to be used for identifiers which denote variables, types, functions, and other entities in source code and documentation.

The choice of naming conventions can be a controversial issue, with partisans of each holding theirs to be the best and others to be inferior. Colloquially, this is said to be a matter of dogma. Many companies have also established their own set of conventions.

## Common elements

The exact rules of a naming convention depend on the context in which they are employed. Nevertheless, there are several common elements that influence most if not all naming conventions in common use today.

### Letter case and numerals

Some naming conventions limit whether letters may appear in uppercase or lowercase. Other conventions do not restrict letter case, but attach a well-defined interpretation based on letter case. Some naming conventions specify whether alphabetic, numeric, or alphanumeric characters may be used, and if so, in what sequence.

### Multiple-word identifiers

A common recommendation is "Use meaningful identifiers." A single word may not be as meaningful, or specific, as multiple words. Consequently, some naming conventions specify rules for the treatment of "compound" identifiers containing more than one word.

As most programming languages do not allow whitespace in identifiers, a method of delimiting each word is needed to make it easier for subsequent readers to interpret which characters belong to which word. Historically some early languages, notably FORTRAN (1955) and ALGOL (1958), allowed spaces within identifiers, determining the end of identifiers by context. This was abandoned in later languages due to the difficulty of tokenization. It is possible to write names by simply concatenating words, and this is sometimes used, as in `mypackage` for Java package names, though legibility suffers for longer terms, so usually some form of separation is used.

#### Delimiter-separated words

One approach is to delimit separate words with a non-alphanumeric character. The two characters commonly used for this purpose are the hyphen ("-") and the underscore ("_"); e.g., the two-word name "`two words`" would be represented as "`two-words`" or "`two_words`".

The hyphen is commonly used by when writing COBOL (1959), Forth (1970), and Lisp (1958); it is also common in Unix for commands and packages, and is used in CSS.

By contrast, languages in the FORTRAN/ALGOL tradition, notably languages in the C and Pascal families, used the hyphen for the subtraction infix operator, and did not wish to require spaces around it (as free-form languages), preventing its use in identifiers.

An alternative is to use underscores; this is common in the C family (including Python), with lowercase words, being found for example in *The C Programming Language* (1978), and has come to be known as snake case or *snail case*. Underscores with uppercase, as in UPPER_CASE, are commonly used for C preprocessor macros, hence known as MACRO_CASE, and for environment variables in Unix, such as BASH_VERSION in bash. Sometimes this is humorously referred to as SCREAMING_SNAKE_CASE (alternatively SCREAMING_SNAIL_CASE).

#### Letter case-separated words

Another approach is to indicate word boundaries using medial capitalization, called "camelCase", "PascalCase", and many other names, thus respectively rendering "`two words`" as "`twoWords`" or "`TwoWords`". This convention is commonly used in Pascal, Java, C#, and Visual Basic. Treatment of initialisms in identifiers (e.g. the "XML" and "HTTP" in `XMLHttpRequest`) varies. Some dictate that they be lowercase (e.g. `XmlHttpRequest`) to ease typing, readability and ease of segmentation, whereas others leave them uppercased (e.g. `XMLHTTPRequest`) for accuracy.

Some naming conventions represent rules or requirements that go beyond the requirements of a specific project or problem domain, and instead reflect a greater overarching set of principles defined by the software architecture, underlying programming language or other kind of cross-project methodology.

### Hungarian notation

Perhaps the most well-known is Hungarian notation, which encodes either the purpose ("Apps Hungarian") or the type ("Systems Hungarian") of a variable in its name. For example, the prefix "sz" for the variable szName indicates that the variable is a null-terminated string.

### Positional notation

A style used for very short (eight characters and less) could be: LCCIIL01, where LC would be the application (Letters of Credit), C for COBOL, IIL for the particular process subset, and the 01 a sequence number.

This sort of convention is still in active use in mainframes dependent upon JCL and is also seen in the 8.3 (maximum eight characters with period separator followed by three character file type) MS-DOS style.

### Composite word scheme (OF Language)

IBM's "OF Language" was documented in an IMS (Information Management System) manual. It detailed the PRIME-MODIFIER-CLASS word scheme, which consisted of names like "CUST-ACT-NO" to indicate "customer account number". PRIME words were meant to indicate major "entities" of interest to a system. MODIFIER words were used for additional refinement, qualification and readability.

CLASS words ideally would be a very short list of data types relevant to a particular application. Common CLASS words might be: NO (number), ID (identifier), TXT (text), AMT (amount), QTY (quantity), FL (flag), CD (code), W (work) and so forth. In practice, the available CLASS words would be a list of less than two dozen terms. CLASS words, typically positioned on the right (suffix), served much the same purpose as Hungarian notation prefixes.

The purpose of CLASS words, in addition to consistency, was to specify to the programmer the data type of a particular data field. Prior to the acceptance of BOOLEAN (two values only) fields, FL (flag) would indicate a field with only two possible values.
