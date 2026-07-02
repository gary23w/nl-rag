---
title: "Regular expression (part 2/2)"
source: https://en.wikipedia.org/wiki/Regular_expression
domain: guided-decoding
license: CC-BY-SA-4.0
tags: guided decoding, grammar constrained decoding, logit masking generation, schema constrained output, token filtering decode
fetched: 2026-07-02
part: 2/2
---

## Uses

Regexes are useful in a wide variety of text processing tasks, and more generally string processing, where the data need not be textual. Common applications include data validation, data scraping (especially web scraping), data wrangling, simple parsing, the production of syntax highlighting systems, and many other tasks.

Some high-end desktop publishing software has the ability to use regexes to automatically apply text styling, saving the person doing the layout from laboriously doing this by hand for anything that can be matched by a regex. For example, by defining a character style that makes text into small caps and then using the regex `[A-Z]{4,}` to apply that style, any word of four or more consecutive capital letters will be automatically rendered as small caps instead.

While regexes would be useful on Internet search engines, processing them across the entire database could consume excessive computer resources depending on the complexity and design of the regex. Although in many cases system administrators can run regex-based queries internally, most search engines do not offer regex support to the public. Notable exceptions include Google Code Search and Exalead. However, Google Code Search was shut down in January 2012.


## Examples

The specific syntax rules vary depending on the specific implementation, programming language, or library in use. Additionally, the functionality of regex implementations can vary between versions.

Because regexes can be difficult to both explain and understand without examples, interactive websites for testing regexes are a useful resource for learning regexes by experimentation. This section provides a basic description of some of the properties of regexes by way of illustration.

The following conventions are used in the examples.

```
metacharacter(s) ;; the metacharacters column specifies the regex syntax being demonstrated
=~ m//           ;; indicates a regex match operation in Perl
=~ s///          ;; indicates a regex substitution operation in Perl
```

These regexes are all Perl-like syntax. Standard POSIX regular expressions are different.

Unless otherwise indicated, the following examples conform to the Perl programming language, release 5.8.8, January 31, 2006. This means that other implementations may lack support for some parts of the syntax shown here (e.g. basic vs. extended regex, `\( \)` vs. `()`, or lack of `\d` instead of POSIX `[:digit:]`).

The syntax and conventions used in these examples coincide with that of other programming environments as well.

| Meta­character(s) | Description | Example |
|---|---|---|
| `.` | Normally matches any character except a newline. Within square brackets the dot is literal. | $string1 = "Hello World\n"; if ($string1 =~ m/...../) { print "$string1 has length >= 5.\n"; } **Output:** Hello World has length >= 5. |
| `( )` | Groups a series of pattern elements to a single element. When you match a pattern within parentheses, you can use any of `$1`, `$2`, ... later to refer to the previously matched pattern. Some implementations may use a backslash notation instead, like `\1`, `\2`. | $string1 = "Hello World\n"; if ($string1 =~ m/(H..).(o..)/) { print "We matched '$1' and '$2'.\n"; } **Output:** We matched 'Hel' and 'o W'. |
| `+` | Matches the preceding pattern element one or more times. | $string1 = "Hello World\n"; if ($string1 =~ m/l+/) { print "There are one or more consecutive letter \"l\"'s in $string1.\n"; } **Output:** There are one or more consecutive letter "l"'s in Hello World. |
| `?` | Matches the preceding pattern element zero or one time. | $string1 = "Hello World\n"; if ($string1 =~ m/H.?e/) { print "There is an 'H' and a 'e' separated by "; print "0-1 characters (e.g., He Hue Hee).\n"; } **Output:** There is an 'H' and a 'e' separated by 0-1 characters (e.g., He Hue Hee). |
| `?` | Modifies the `*`, `+`, `?` or `{M,N}`'d regex that comes before to match as few times as possible. | $string1 = "Hello World\n"; if ($string1 =~ m/(l.+?o)/) { print "The non-greedy match with 'l' followed by one or "; print "more characters is 'llo' rather than 'llo Wo'.\n"; } **Output:** The non-greedy match with 'l' followed by one or more characters is 'llo' rather than 'llo Wo'. |
| `*` | Matches the preceding pattern element zero or more times. | $string1 = "Hello World\n"; if ($string1 =~ m/el*o/) { print "There is an 'e' followed by zero to many "; print "'l' followed by 'o' (e.g., eo, elo, ello, elllo).\n"; } **Output:** There is an 'e' followed by zero to many 'l' followed by 'o' (e.g., eo, elo, ello, elllo). |
| `{M,N}` | Denotes the minimum M and the maximum N match count. N can be omitted and M can be 0: `{M}` matches "exactly" M times; `{M,}` matches "at least" M times; `{0,N}` matches "at most" N times. `x* y+ z?` is thus equivalent to `x{0,} y{1,} z{0,1}`. | $string1 = "Hello World\n"; if ($string1 =~ m/l{1,2}/) { print "There exists a substring with at least 1 "; print "and at most 2 l's in $string1\n"; } **Output:** There exists a substring with at least 1 and at most 2 l's in Hello World |
| `[…]` | Denotes a set of possible character matches. | $string1 = "Hello World\n"; if ($string1 =~ m/[aeiou]+/) { print "$string1 contains one or more vowels.\n"; } **Output:** Hello World contains one or more vowels. |
| `\|` | Separates alternate possibilities. | $string1 = "Hello World\n"; if ($string1 =~ m/(Hello\|Hi\|Pogo)/) { print "$string1 contains at least one of Hello, Hi, or Pogo."; } **Output:** Hello World contains at least one of Hello, Hi, or Pogo. |
| `\b` | Matches a zero-width boundary between a word-class character (see next) and either a non-word class character or an edge; same as `(^\w\|\w$\|\W\w\|\w\W)`. | $string1 = "Hello World\n"; if ($string1 =~ m/llo\b/) { print "There is a word that ends with 'llo'.\n"; } **Output:** There is a word that ends with 'llo'. |
| `\w` | Matches an alphanumeric character, including "_"; same as `[A-Za-z0-9_]` in ASCII, and `[\p{Alphabetic}\p{GC=Mark}\p{GC=Decimal_Number}\p{GC=Connector_Punctuation}]` in Unicode, where the `Alphabetic` property contains more than Latin letters, and the `Decimal_Number` property contains more than Arab digits. | $string1 = "Hello World\n"; if ($string1 =~ m/\w/) { print "There is at least one alphanumeric "; print "character in $string1 (A-Z, a-z, 0-9, _).\n"; } **Output:** There is at least one alphanumeric character in Hello World (A-Z, a-z, 0-9, _). |
| `\W` | Matches a *non*-alphanumeric character, excluding "_"; same as `[^A-Za-z0-9_]` in ASCII, and `[^\p{Alphabetic}\p{GC=Mark}\p{GC=Decimal_Number}\p{GC=Connector_Punctuation}]` in Unicode. | $string1 = "Hello World\n"; if ($string1 =~ m/\W/) { print "The space between Hello and "; print "World is not alphanumeric.\n"; } **Output:** The space between Hello and World is not alphanumeric. |
| `\s` | Matches a whitespace character, which in ASCII are tab, line feed, form feed, carriage return, and space; in Unicode, also matches no-break spaces, next line, and the variable-width spaces (among others). | $string1 = "Hello World\n"; if ($string1 =~ m/\s.*\s/) { print "In $string1 there are TWO whitespace characters, which may"; print " be separated by other characters.\n"; } **Output:** In Hello World there are TWO whitespace characters, which may be separated by other characters. |
| `\S` | Matches anything *but* a whitespace. | $string1 = "Hello World\n"; if ($string1 =~ m/\S.*\S/) { print "In $string1 there are TWO non-whitespace characters, which"; print " may be separated by other characters.\n"; } **Output:** In Hello World there are TWO non-whitespace characters, which may be separated by other characters. |
| `\d` | Matches a digit; same as `[0-9]` in ASCII; in Unicode, same as the `\p{Digit}` or `\p{GC=Decimal_Number}` property, which itself the same as the `\p{Numeric_Type=Decimal}` property. | $string1 = "99 bottles of beer on the wall."; if ($string1 =~ m/(\d+)/) { print "$1 is the first number in '$string1'\n"; } **Output:** 99 is the first number in '99 bottles of beer on the wall.' |
| `\D` | Matches a non-digit; same as `[^0-9]` in ASCII or `\P{Digit}` in Unicode. | $string1 = "Hello World\n"; if ($string1 =~ m/\D/) { print "At least one character in $string1"; print " is not a digit.\n"; } **Output:** At least one character in Hello World is not a digit. |
| `^` | Matches the beginning of a line or string. | $string1 = "Hello World\n"; if ($string1 =~ m/^He/) { print "$string1 starts with the characters 'He'.\n"; } **Output:** Hello World starts with the characters 'He'. |
| `$` | Matches the end of a line or string. | $string1 = "Hello World\n"; if ($string1 =~ m/rld$/) { print "$string1 is a line or string "; print "that ends with 'rld'.\n"; } **Output:** Hello World is a line or string that ends with 'rld'. |
| `\A` | Matches the beginning of a string (but not an internal line). | $string1 = "Hello\nWorld\n"; if ($string1 =~ m/\AH/) { print "$string1 is a string "; print "that starts with 'H'.\n"; } **Output:** Hello World is a string that starts with 'H'. |
| `\z` | Matches the end of a string (but not an internal line). | $string1 = "Hello\nWorld\n"; if ($string1 =~ m/d\n\z/) { print "$string1 is a string "; print "that ends with 'd\\n'.\n"; } **Output:** Hello World is a string that ends with 'd\n'. |
| `[^…]` | Matches every character except the ones inside brackets. | $string1 = "Hello World\n"; if ($string1 =~ m/[^abc]/) { print "$string1 contains a character other than "; print "a, b, and c.\n"; } **Output:** Hello World contains a character other than a, b, and c. |


## Induction

Regular expressions can often be created ("induced" or "learned") based on a set of example strings. This is known as the induction of regular languages and is part of the general problem of grammar induction in computational learning theory. Formally, given examples of strings in a regular language, and perhaps also given examples of strings *not* in that regular language, it is possible to induce a grammar for the language, i.e., a regular expression that generates that language. Not all regular languages can be induced in this way (see language identification in the limit), but many can. For example, the set of examples {1, 10, 100}, and negative set (of counterexamples) {11, 1001, 101, 0} can be used to induce the regular expression 1⋅0* (1 followed by zero or more 0s).
