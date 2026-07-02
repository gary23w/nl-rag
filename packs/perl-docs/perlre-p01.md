---
title: "perlre (part 1/4)"
source: https://perldoc.perl.org/perlre
domain: perl-docs
license: GPL-1.0-or-later OR Artistic-1.0
tags: perl, perldoc, perl script, perl module, cpan
fetched: 2026-07-02
part: 1/4
---

# perlre

perlre

(

source

,

CPAN

)

- NAME
- DESCRIPTION
  - The Basics
    - Metacharacters
  - Modifiers
    - Overview
    - Details on some modifiers
      - /x and /xx
      - Character set modifiers
      - /l
      - /u
      - /d
      - /a (and /aa)
      - Which character set modifier is in effect?
      - Character set modifier behavior prior to Perl 5.14
  - Regular Expressions
    - Quantifiers
    - Escape sequences
    - Character Classes and other Special Escapes
    - Assertions
    - Capture groups
  - Quoting (escaping) metacharacters
  - Extended Patterns
  - Backtracking
  - Script Runs
  - Special Backtracking Control Verbs
  - Warning on \1 Instead of $1
  - Repeated Patterns Matching a Zero-length Substring
  - Combining RE Pieces
  - Creating Custom RE Engines
  - Embedded Code Execution Frequency
  - PCRE/Python Support
  - Quoting metacharacters
- BUGS
- SEE ALSO

# #NAME

perlre - Perl regular expressions

# #DESCRIPTION

This page describes the syntax of regular expressions in Perl.

If you haven't used regular expressions before, a tutorial introduction is available in perlretut. If you know just a little about them, a quick-start introduction is available in perlrequick.

Except for "The Basics" section, this page assumes you are familiar with regular expression basics, like what is a "pattern", what does it look like, and how it is basically used. For a reference on how they are used, plus various examples of the same, see discussions of `m//`, `s///`, `qr//` and `"??"` in "Regexp Quote-Like Operators" in perlop.

New in v5.22, `use re 'strict'` applies stricter rules than otherwise when compiling regular expression patterns. It can find things that, while legal, may not be what you intended.


## #The Basics

Regular expressions are strings with the very particular syntax and meaning described in this document and auxiliary documents referred to by this one. The strings are called "patterns". Patterns are used to determine if some other string, called the "target", has (or doesn't have) the characteristics specified by the pattern. We call this "matching" the target string against the pattern. Usually the match is done by having the target be the first operand, and the pattern be the second operand, of one of the two binary operators `=~` and `!~`, listed in "Binding Operators" in perlop; and the pattern will have been converted from an ordinary string by one of the operators in "Regexp Quote-Like Operators" in perlop, like so:

```
$foo =~ m/abc/
```

This evaluates to true if and only if the string in the variable `$foo` contains somewhere in it, the sequence of characters "a", "b", then "c". (The `=~ m`, or match operator, is described in "m/PATTERN/msixpodualngc" in perlop.)

Patterns that aren't already stored in some variable must be delimited, at both ends, by delimiter characters. These are often, as in the example above, forward slashes, and the typical way a pattern is written in documentation is with those slashes. In most cases, the delimiter is the same character, fore and aft, but there are a few cases where a character looks like it has a mirror-image mate, where the opening version is the beginning delimiter, and the closing one is the ending delimiter, like

```
$foo =~ m<abc>
```

Most times, the pattern is evaluated in double-quotish context, but it is possible to choose delimiters to force single-quotish, like

```
$foo =~ m'abc'
```

If the pattern contains its delimiter within it, that delimiter must be escaped. Prefixing it with a backslash (*e.g.*, `"/foo\/bar/"`) serves this purpose.

Any single character in a pattern matches that same character in the target string, unless the character is a *metacharacter* with a special meaning described in this document. A sequence of non-metacharacters matches the same sequence in the target string, as we saw above with `m/abc/`.

Only a few characters (all of them being ASCII punctuation characters) are metacharacters. The most commonly used one is a dot `"."`, which normally matches almost any character (including a dot itself).

You can cause characters that normally function as metacharacters to be interpreted literally by prefixing them with a `"\"`, just like the pattern's delimiter must be escaped if it also occurs within the pattern. Thus, `"\."` matches just a literal dot, `"."` instead of its normal meaning. This means that the backslash is also a metacharacter, so `"\\"` matches a single `"\"`. And a sequence that contains an escaped metacharacter matches the same sequence (but without the escape) in the target string. So, the pattern `/blur\\fl/` would match any target string that contains the sequence `"blur\fl"`.

The metacharacter `"|"` is used to match one thing or another. Thus

```
$foo =~ m/this|that/
```

is TRUE if and only if `$foo` contains either the sequence `"this"` or the sequence `"that"`. Like all metacharacters, prefixing the `"|"` with a backslash makes it match the plain punctuation character; in its case, the VERTICAL LINE.

```
$foo =~ m/this\|that/
```

is TRUE if and only if `$foo` contains the sequence `"this|that"`.

You aren't limited to just a single `"|"`.

```
$foo =~ m/fee|fie|foe|fum/
```

is TRUE if and only if `$foo` contains any of those 4 sequences from the children's story "Jack and the Beanstalk".

As you can see, the `"|"` binds less tightly than a sequence of ordinary characters. We can override this by using the grouping metacharacters, the parentheses `"("` and `")"`.

```
$foo =~ m/th(is|at) thing/
```

is TRUE if and only if `$foo` contains either the sequence `"this thing"` or the sequence `"that thing"`. The portions of the string that match the portions of the pattern enclosed in parentheses are normally made available separately for use later in the pattern, substitution, or program. This is called "capturing", and it can get complicated. See "Capture groups".

The first alternative includes everything from the last pattern delimiter (`"("`, `"(?:"` (described later), *etc*. or the beginning of the pattern) up to the first `"|"`, and the last alternative contains everything from the last `"|"` to the next closing pattern delimiter. That's why it's common practice to include alternatives in parentheses: to minimize confusion about where they start and end.

Alternatives are tried from left to right, so the first alternative found for which the entire expression matches, is the one that is chosen. This means that alternatives are not necessarily greedy. For example: when matching `foo|foot` against `"barefoot"`, only the `"foo"` part will match, as that is the first alternative tried, and it successfully matches the target string. (This might not seem important, but it is important when you are capturing matched text using parentheses.)

Besides taking away the special meaning of a metacharacter, a prefixed backslash changes some letter and digit characters away from matching just themselves to instead have special meaning. These are called "escape sequences", and all such are described in perlrebackslash. A backslash sequence (of a letter or digit) that doesn't currently have special meaning to Perl will raise a warning if warnings are enabled, as those are reserved for potential future use.

One such sequence is `\b`, which matches a boundary of some sort. `\b{wb}` and a few others give specialized types of boundaries. (They are all described in detail starting at "\b{}, \b, \B{}, \B" in perlrebackslash.) Note that these don't match characters, but the zero-width spaces between characters. They are an example of a zero-width assertion. Consider again,

```
$foo =~ m/fee|fie|foe|fum/
```

It evaluates to TRUE if, besides those 4 words, any of the sequences "feed", "field", "Defoe", "fume", and many others are in `$foo`. By judicious use of `\b` (or better (because it is designed to handle natural language) `\b{wb}`), we can make sure that only the Giant's words are matched:

```
$foo =~ m/\b(fee|fie|foe|fum)\b/
$foo =~ m/\b{wb}(fee|fie|foe|fum)\b{wb}/
```

The final example shows that the characters `"{"` and `"}"` are metacharacters.

Another use for escape sequences is to specify characters that cannot (or which you prefer not to) be written literally. These are described in detail in "Character Escapes" in perlrebackslash, but the next three paragraphs briefly describe some of them.

Various control characters can be written in C language style: `"\n"` matches a newline, `"\t"` a tab, `"\r"` a carriage return, `"\f"` a form feed, *etc*.

More generally, `\*nnn*`, where *nnn* is a string of three octal digits, matches the character whose native code point is *nnn*. You can easily run into trouble if you don't have exactly three digits. So always use three, or since Perl 5.14, you can use `\o{...}` to specify any number of octal digits.

Similarly, `\x*nn*`, where *nn* are hexadecimal digits, matches the character whose native ordinal is *nn*. Again, not using exactly two digits is a recipe for disaster, but you can use `\x{...}` to specify any number of hex digits.

Besides being a metacharacter, the `"."` is an example of a "character class", something that can match any single character of a given set of them. In its case, the set is just about all possible characters. Perl predefines several character classes besides the `"."`; there is a separate reference page about just these, perlrecharclass.

You can define your own custom character classes, by putting into your pattern in the appropriate place(s), a list of all the characters you want in the set. You do this by enclosing the list within `[]` bracket characters. These are called "bracketed character classes" when we are being precise, but often the word "bracketed" is dropped. (Dropping it usually doesn't cause confusion.) This means that the `"["` character is another metacharacter. It doesn't match anything just by itself; it is used only to tell Perl that what follows it is a bracketed character class. If you want to match a literal left square bracket, you must escape it, like `"\["`. The matching `"]"` is also a metacharacter; again it doesn't match anything by itself, but just marks the end of your custom class to Perl. It is an example of a "sometimes metacharacter". It isn't a metacharacter if there is no corresponding `"["`, and matches its literal self:

```
print "]" =~ /]/;  # prints 1
```

The list of characters within the character class gives the set of characters matched by the class. `"[abc]"` matches a single "a" or "b" or "c". But if the first character after the `"["` is `"^"`, the class instead matches any character not in the list. Within a list, the `"-"` character specifies a range of characters, so that `a-z` represents all characters between "a" and "z", inclusive. If you want either `"-"` or `"]"` itself to be a member of a class, put it at the start of the list (possibly after a `"^"`), or escape it with a backslash. `"-"` is also taken literally when it is at the end of the list, just before the closing `"]"`. (The following all specify the same class of three characters: `[-az]`, `[az-]`, and `[a\-z]`. All are different from `[a-z]`, which specifies a class containing twenty-six characters, even on EBCDIC-based character sets.)

There is lots more to bracketed character classes; full details are in "Bracketed Character Classes" in perlrecharclass.

### #Metacharacters

"The Basics" introduced some of the metacharacters. This section gives them all. Most of them have the same meaning as in the *egrep* command.

Only the `"\"` is always a metacharacter. The others are metacharacters just sometimes. The following tables lists all of them, summarizes their use, and gives the contexts where they are metacharacters. Outside those contexts or if prefixed by a `"\"`, they match their corresponding punctuation character. In some cases, their meaning varies depending on various pattern modifiers that alter the default behaviors. See "Modifiers".

```
           PURPOSE                                  WHERE
\   Escape the next character                    Always, except when
                                                 escaped by another \
^   Match the beginning of the string            Not in []
      (or line, if /m is used)
^   Complement the [] class                      At the beginning of []
.   Match any single character except newline    Not in []
      (under /s, includes newline)
$   Match the end of the string                  Not in [], but can
      (or before newline at the end of the       mean interpolate a
      string; or before any newline if /m is     scalar
      used)
|   Alternation                                  Not in []
()  Grouping                                     Not in []
[   Start Bracketed Character class              Not in []
]   End Bracketed Character class                Only in [], and
                                                   not first
*   Matches the preceding element 0 or more      Not in []
      times
+   Matches the preceding element 1 or more      Not in []
      times
?   Matches the preceding element 0 or 1         Not in []
      times
{   Starts a sequence that gives number(s)       Not in []
      of times the preceding element can be
      matched
{   when following certain escape sequences
      starts a modifier to the meaning of the
      sequence
}   End sequence started by {
-   Indicates a range                            Only in [] interior
#   Beginning of comment, extends to line end    Only with /x modifier
```

Notice that most of the metacharacters lose their special meaning when they occur in a bracketed character class, except `"^"` has a different meaning when it is at the beginning of such a class. And `"-"` and `"]"` are metacharacters only at restricted positions within bracketed character classes; while `"}"` is a metacharacter only when closing a special construct started by `"{"`.

In double-quotish context, as is usually the case, you need to be careful about `"$"` and the non-metacharacter `"@"`. Those could interpolate variables, which may or may not be what you intended.

These rules were designed for compactness of expression, rather than legibility and maintainability. The "/x and /xx" pattern modifiers allow you to insert white space to improve readability. And use of `re 'strict'` adds extra checking to catch some typos that might silently compile into something unintended.

By default, the `"^"` character is guaranteed to match only the beginning of the string, the `"$"` character only the end (or before the newline at the end), and Perl does certain optimizations with the assumption that the string contains only one line. Embedded newlines will not be matched by `"^"` or `"$"`. You may, however, wish to treat a string as a multi-line buffer, such that the `"^"` will match after any newline within the string (except if the newline is the last character in the string), and `"$"` will match before any newline. At the cost of a little more overhead, you can do this by using the `"/m"` modifier on the pattern match operator. (Older programs did this by setting `$*`, but this option was removed in perl 5.10.)

To simplify multi-line substitutions, the `"."` character never matches a newline unless you use the `/s` modifier, which in effect tells Perl to pretend the string is a single line--even if it isn't.


## #Modifiers

### #Overview

The default behavior for matching can be changed, using various modifiers. Modifiers that relate to the interpretation of the pattern are listed just below. Modifiers that alter the way a pattern is used by Perl are detailed in "Regexp Quote-Like Operators" in perlop and "Gory details of parsing quoted constructs" in perlop. Modifiers can be added dynamically; see "Extended Patterns" below.

**#**`m`****

Treat the string being matched against as multiple lines. That is, change `"^"` and `"$"` from matching the start of the string's first line and the end of its last line to matching the start and end of each line within the string.

**#**`s`****

Treat the string as single line. That is, change `"."` to match any character whatsoever, even a newline, which normally it would not match.

Used together, as `/ms`, they let the `"."` match any character whatsoever, while still allowing `"^"` and `"$"` to match, respectively, just after and just before newlines within the string.

**#**`i`****

Do case-insensitive pattern matching. For example, "A" will match "a" under `/i`.

If locale matching rules are in effect, the case map is taken from the current locale for code points less than 255, and from Unicode rules for larger code points. However, matches that would cross the Unicode rules/non-Unicode rules boundary (ords 255/256) will not succeed, unless the locale is a UTF-8 one. See perllocale.

There are a number of Unicode characters that match a sequence of multiple characters under `/i`. For example, `LATIN SMALL LIGATURE FI` should match the sequence `fi`. Perl is not currently able to do this when the multiple characters are in the pattern and are split between groupings, or when one or more are quantified. Thus

```
"\N{LATIN SMALL LIGATURE FI}" =~ /fi/i;          # Matches
"\N{LATIN SMALL LIGATURE FI}" =~ /[fi][fi]/i;    # Doesn't match!
"\N{LATIN SMALL LIGATURE FI}" =~ /fi*/i;         # Doesn't match!

# The below doesn't match, and it isn't clear what $1 and $2 would
# be even if it did!!
"\N{LATIN SMALL LIGATURE FI}" =~ /(f)(i)/i;      # Doesn't match!
```

Perl doesn't match multiple characters in a bracketed character class unless the character that maps to them is explicitly mentioned, and it doesn't match them at all if the character class is inverted, which otherwise could be highly confusing. See "Bracketed Character Classes" in perlrecharclass, and "Negation" in perlrecharclass.

**#**`x`** and **`xx`****

Extend your pattern's legibility by permitting whitespace and comments. Details in "/x and /xx"

**#**`p`****

Preserve the string matched such that `${^PREMATCH}`, `${^MATCH}`, and `${^POSTMATCH}` are available for use after matching.

In Perl 5.20 and higher this is ignored. Due to a new copy-on-write mechanism, `${^PREMATCH}`, `${^MATCH}`, and `${^POSTMATCH}` will be available after the match regardless of the modifier.

**#**`a`**, **`d`**, **`l`**, and **`u`****

These modifiers, all new in 5.14, affect which character-set rules (Unicode, *etc*.) are used, as described below in "Character set modifiers".

**#**`n`****

Prevent the grouping metacharacters `()` from capturing. This modifier, new in 5.22, will stop `$1`, `$2`, *etc*... from being filled in.

```
"hello" =~ /(hi|hello)/;   # $1 is "hello"
"hello" =~ /(hi|hello)/n;  # $1 is undef
```

This is equivalent to putting `?:` at the beginning of every capturing group:

```
"hello" =~ /(?:hi|hello)/; # $1 is undef
```

`/n` can be negated on a per-group basis. Alternatively, named captures may still be used.

```
"hello" =~ /(?-n:(hi|hello))/n;   # $1 is "hello"
"hello" =~ /(?<greet>hi|hello)/n; # $1 is "hello", $+{greet} is
                                  # "hello"
```

**#Other Modifiers**

There are a number of flags that can be found at the end of regular expression constructs that are *not* generic regular expression flags, but apply to the operation being performed, like matching or substitution (`m//` or `s///` respectively).

Flags described further in "Using regular expressions in Perl" in perlretut are:

```
c  - keep the current position during repeated matching
g  - globally match the pattern repeatedly in the string
```

Substitution-specific modifiers described in "s/PATTERN/REPLACEMENT/msixpodualngcer" in perlop are:

```
e  - evaluate the right-hand side as an expression
ee - evaluate the right side as a string then eval the result
o  - pretend to optimize your code, but actually introduce bugs
r  - perform non-destructive substitution and return the new value
```

Regular expression modifiers are usually written in documentation as *e.g.*, "the `/x` modifier", even though the delimiter in question might not really be a slash. The modifiers `/imnsxadlup` may also be embedded within the regular expression itself using the `(?...)` construct, see "Extended Patterns" below.

### #Details on some modifiers

Some of the modifiers require more explanation than given in the "Overview" above.

#### #`/x` and `/xx`

A single `/x` tells the regular expression parser to ignore most whitespace that is neither backslashed nor within a bracketed character class, nor within the characters of a multi-character metapattern like `(?i: ... )`. You can use this to break up your regular expression into more readable parts. Also, the `"#"` character is treated as a metacharacter introducing a comment that runs up to the pattern's closing delimiter, or to the end of the current line if the pattern extends onto the next line. Hence, this is very much like an ordinary Perl code comment. (You can include the closing delimiter within the comment only if you precede it with a backslash, so be careful!)

Use of `/x` means that if you want real whitespace or `"#"` characters in the pattern (outside a bracketed character class, which is unaffected by `/x`), then you'll either have to escape them (using backslashes or `\Q...\E`) or encode them using octal, hex, or `\N{}` or `\p{name=...}` escapes. It is ineffective to try to continue a comment onto the next line by escaping the `\n` with a backslash or `\Q`.

You can use "(?#text)" to create a comment that ends earlier than the end of the current line, but `text` also can't contain the closing delimiter unless escaped with a backslash.

A common pitfall is to forget that `"#"` characters (outside a bracketed character class) begin a comment under `/x` and are not matched literally. Just keep that in mind when trying to puzzle out why a particular `/x` pattern isn't working as expected. Inside a bracketed character class, `"#"` retains its non-special, literal meaning.

Starting in Perl v5.26, if the modifier has a second `"x"` within it, the effect of a single `/x` is increased. The only difference is that inside bracketed character classes, non-escaped (by a backslash) SPACE and TAB characters are not added to the class, and hence can be inserted to make the classes more readable:

```
/ [d-e g-i 3-7]/xx
/[ ! @ " # $ % ^ & * () = ? <> ' ]/xx
```

may be easier to grasp than the squashed equivalents

```
/[d-eg-i3-7]/
/[!@"#$%^&*()=?<>']/
```

Note that this unfortunately doesn't mean that your bracketed classes can contain comments or extend over multiple lines. A `#` inside a character class is still just a literal `#`, and doesn't introduce a comment. And, unless the closing bracket is on the same line as the opening one, the newline character (and everything on the next line(s) until terminated by a `]` will be part of the class, just as if you'd written `\n`.

Taken together, these features go a long way towards making Perl's regular expressions more readable. Here's an example:

```
    # Delete (most) C comments.
    $program =~ s {
	/\*	# Match the opening delimiter.
	.*?	# Match a minimal number of characters.
	\*/	# Match the closing delimiter.
    } []gsx;
```

Note that anything inside a `\Q...\E` stays unaffected by `/x`. And note that `/x` doesn't affect space interpretation within a single multi-character construct. For example `(?:...)` can't have a space between the `"("`, `"?"`, and `":"`. Within any delimiters for such a construct, allowed spaces are not affected by `/x`, and depend on the construct. For example, all constructs using curly braces as delimiters, such as `\x{...}` can have blanks within but adjacent to the braces, but not elsewhere, and no non-blank space characters. An exception are Unicode properties which follow Unicode rules, for which see "Properties accessible through \p{} and \P{}" in perluniprops.

The set of characters that are deemed whitespace are those that Unicode calls "Pattern White Space", namely:

```
U+0009 CHARACTER TABULATION
U+000A LINE FEED
U+000B LINE TABULATION
U+000C FORM FEED
U+000D CARRIAGE RETURN
U+0020 SPACE
U+0085 NEXT LINE
U+200E LEFT-TO-RIGHT MARK
U+200F RIGHT-TO-LEFT MARK
U+2028 LINE SEPARATOR
U+2029 PARAGRAPH SEPARATOR
```

#### #Character set modifiers

`/d`, `/u`, `/a`, and `/l`, available starting in 5.14, are called the character set modifiers; they affect the character set rules used for the regular expression.

The `/d`, `/u`, and `/l` modifiers are not likely to be of much use to you, and so you need not worry about them very much. They exist for Perl's internal use, so that complex regular expression data structures can be automatically serialized and later exactly reconstituted, including all their nuances. But, since Perl can't keep a secret, and there may be rare instances where they are useful, they are documented here.

The `/a` modifier, on the other hand, may be useful. Its purpose is to allow code that is to work mostly on ASCII data to not have to concern itself with Unicode.

Briefly, `/l` sets the character set to that of whatever **L**ocale is in effect at the time of the execution of the pattern match.

`/u` sets the character set to **U**nicode.

`/a` also sets the character set to Unicode, BUT adds several restrictions for **A**SCII-safe matching.

`/d` is the old, problematic, pre-5.14 **D**efault character set behavior. Its only use is to force that old behavior.

At any given time, exactly one of these modifiers is in effect. Their existence allows Perl to keep the originally compiled behavior of a regular expression, regardless of what rules are in effect when it is actually executed. And if it is interpolated into a larger regex, the original's rules continue to apply to it, and don't affect the other parts.

The `/l` and `/u` modifiers are automatically selected for regular expressions compiled within the scope of various pragmas, and we recommend that in general, you use those pragmas instead of specifying these modifiers explicitly. For one thing, the modifiers affect only pattern matching, and do not extend to even any replacement done, whereas using the pragmas gives consistent results for all appropriate operations within their scopes. For example,

```
s/foo/\Ubar/il
```

will match "foo" using the locale's rules for case-insensitive matching, but the `/l` does not affect how the `\U` operates. Most likely you want both of them to use locale rules. To do this, instead compile the regular expression within the scope of `use locale`. This both implicitly adds the `/l`, and applies locale rules to the `\U`. The lesson is to `use locale`, and not `/l` explicitly.

Similarly, it would be better to use `use feature 'unicode_strings'` instead of,

```
s/foo/\Lbar/iu
```

to get Unicode rules, as the `\L` in the former (but not necessarily the latter) would also use Unicode rules.

More detail on each of the modifiers follows. Most likely you don't need to know this detail for `/l`, `/u`, and `/d`, and can skip ahead to /a.

#### #/l

means to use the current locale's rules (see perllocale) when pattern matching. For example, `\w` will match the "word" characters of that locale, and `"/i"` case-insensitive matching will match according to the locale's case folding rules. The locale used will be the one in effect at the time of execution of the pattern match. This may not be the same as the compilation-time locale, and can differ from one match to another if there is an intervening call of the setlocale() function.

Prior to v5.20, Perl did not support multi-byte locales. Starting then, UTF-8 locales are supported. No other multi byte locales are ever likely to be supported. However, in all locales, one can have code points above 255 and these will always be treated as Unicode no matter what locale is in effect.

Under Unicode rules, there are a few case-insensitive matches that cross the 255/256 boundary. Except for UTF-8 locales in Perls v5.20 and later, these are disallowed under `/l`. For example, 0xFF (on ASCII platforms) does not caselessly match the character at 0x178, `LATIN CAPITAL LETTER Y WITH DIAERESIS`, because 0xFF may not be `LATIN SMALL LETTER Y WITH DIAERESIS` in the current locale, and Perl has no way of knowing if that character even exists in the locale, much less what code point it is.

In a UTF-8 locale in v5.20 and later, the only visible difference between locale and non-locale in regular expressions should be tainting, if your perl supports taint checking (see perlsec).

This modifier may be specified to be the default by `use locale`, but see "Which character set modifier is in effect?".

#### #/u

means to use Unicode rules when pattern matching. On ASCII platforms, this means that the code points between 128 and 255 take on their Latin-1 (ISO-8859-1) meanings (which are the same as Unicode's). (Otherwise Perl considers their meanings to be undefined.) Thus, under this modifier, the ASCII platform effectively becomes a Unicode platform; and hence, for example, `\w` will match any of the more than 100_000 word characters in Unicode.

Unlike most locales, which are specific to a language and country pair, Unicode classifies all the characters that are letters *somewhere* in the world as `\w`. For example, your locale might not think that `LATIN SMALL LETTER ETH` is a letter (unless you happen to speak Icelandic), but Unicode does. Similarly, all the characters that are decimal digits somewhere in the world will match `\d`; this is hundreds, not 10, possible matches. And some of those digits look like some of the 10 ASCII digits, but mean a different number, so a human could easily think a number is a different quantity than it really is. For example, `BENGALI DIGIT FOUR` (U+09EA) looks very much like an `ASCII DIGIT EIGHT` (U+0038), and `LEPCHA DIGIT SIX` (U+1C46) looks very much like an `ASCII DIGIT FIVE` (U+0035). And, `\d+`, may match strings of digits that are a mixture from different writing systems, creating a security issue. A fraudulent website, for example, could display the price of something using U+1C46, and it would appear to the user that something cost 500 units, but it really costs 600. A browser that enforced script runs ("Script Runs") would prevent that fraudulent display. "num()" in Unicode::UCD can also be used to sort this out. Or the `/a` modifier can be used to force `\d` to match just the ASCII 0 through 9.

Also, under this modifier, case-insensitive matching works on the full set of Unicode characters. The `KELVIN SIGN`, for example matches the letters "k" and "K"; and `LATIN SMALL LIGATURE FF` matches the sequence "ff", which, if you're not prepared, might make it look like a hexadecimal constant, presenting another potential security issue. See https://unicode.org/reports/tr36 for a detailed discussion of Unicode security issues.

This modifier may be specified to be the default by `use feature 'unicode_strings`, `use locale ':not_characters'`, or `use v5.12` (or higher), but see "Which character set modifier is in effect?".

#### #/d

**IMPORTANT:** Because of the unpredictable behaviors this modifier causes, only use it to maintain weird backward compatibilities. Use the `unicode_strings` feature in new code to avoid inadvertently enabling this modifier by default.

What does this modifier do? It "Depends"!

This modifier means to use platform-native matching rules except when there is cause to use Unicode rules instead, as follows:

1. the target string's UTF8 flag (see below) is set; or
2. the pattern's UTF8 flag (see below) is set; or
3. the pattern explicitly mentions a code point that is above 255 (say by `\x{100}`); or
4. the pattern uses a Unicode name (`\N{...}`); or
5. the pattern uses a Unicode property (`\p{...}` or `\P{...}`); or
6. the pattern uses a Unicode break (`\b{...}` or `\B{...}`); or
7. the pattern uses `"(?[ ])"`
8. the pattern uses `(*script_run: ...)`

Regarding the "UTF8 flag" references above: normally Perl applications shouldn't think about that flag. It's part of Perl's internals, so it can change whenever Perl wants. `/d` may thus cause unpredictable results. See "The "Unicode Bug"" in perlunicode. This bug has become rather infamous, leading to yet other (without swearing) names for this modifier like "Dicey" and "Dodgy".

Here are some examples of how that works on an ASCII platform:

```
$str =  "\xDF";        #
utf8::downgrade($str); # $str is not UTF8-flagged.
$str =~ /^\w/;         # No match, since no UTF8 flag.

$str .= "\x{0e0b}";    # Now $str is UTF8-flagged.
$str =~ /^\w/;         # Match! $str is now UTF8-flagged.
chop $str;
$str =~ /^\w/;         # Still a match! $str retains its UTF8 flag.
```

Under Perl's default configuration this modifier is automatically selected by default when none of the others are, so yet another name for it (unfortunately) is "Default".

Whenever you can, use the `unicode_strings` to cause `/u` to be the default instead.

#### #/a (and /aa)

This modifier stands for ASCII-restrict (or ASCII-safe). This modifier may be doubled-up to increase its effect.

When it appears singly, it causes the sequences `\d`, `\s`, `\w`, and the Posix character classes to match only in the ASCII range. They thus revert to their pre-5.6, pre-Unicode meanings. Under `/a`, `\d` always means precisely the digits `"0"` to `"9"`; `\s` means the five characters `[ \f\n\r\t]`, and starting in Perl v5.18, the vertical tab; `\w` means the 63 characters `[A-Za-z0-9_]`; and likewise, all the Posix classes such as `[[:print:]]` match only the appropriate ASCII-range characters.

This modifier is useful for people who only incidentally use Unicode, and who do not wish to be burdened with its complexities and security concerns.

With `/a`, one can write `\d` with confidence that it will only match ASCII characters, and should the need arise to match beyond ASCII, you can instead use `\p{Digit}` (or `\p{Word}` for `\w`). There are similar `\p{...}` constructs that can match beyond ASCII both white space (see "Whitespace" in perlrecharclass), and Posix classes (see "POSIX Character Classes" in perlrecharclass). Thus, this modifier doesn't mean you can't use Unicode, it means that to get Unicode matching you must explicitly use a construct (`\p{}`, `\P{}`) that signals Unicode.

As you would expect, this modifier causes, for example, `\D` to mean the same thing as `[^0-9]`; in fact, all non-ASCII characters match `\D`, `\S`, and `\W`. `\b` still means to match at the boundary between `\w` and `\W`, using the `/a` definitions of them (similarly for `\B`).

Otherwise, `/a` behaves like the `/u` modifier, in that case-insensitive matching uses Unicode rules; for example, "k" will match the Unicode `\N{KELVIN SIGN}` under `/i` matching, and code points in the Latin1 range, above ASCII will have Unicode rules when it comes to case-insensitive matching.

To forbid ASCII/non-ASCII matches (like "k" with `\N{KELVIN SIGN}`), specify the `"a"` twice, for example `/aai` or `/aia`. (The first occurrence of `"a"` restricts the `\d`, *etc*., and the second occurrence adds the `/i` restrictions.) But, note that code points outside the ASCII range will use Unicode rules for `/i` matching, so the modifier doesn't really restrict things to just ASCII; it just forbids the intermixing of ASCII and non-ASCII.

To summarize, this modifier provides protection for applications that don't wish to be exposed to all of Unicode. Specifying it twice gives added protection.

This modifier may be specified to be the default by `use re '/a'` or `use re '/aa'`. If you do so, you may actually have occasion to use the `/u` modifier explicitly if there are a few regular expressions where you do want full Unicode rules (but even here, it's best if everything were under feature `"unicode_strings"`, along with the `use re '/aa'`). Also see "Which character set modifier is in effect?".

#### #Which character set modifier is in effect?

Which of these modifiers is in effect at any given point in a regular expression depends on a fairly complex set of interactions. These have been designed so that in general you don't have to worry about it, but this section gives the gory details. As explained below in "Extended Patterns" it is possible to explicitly specify modifiers that apply only to portions of a regular expression. The innermost always has priority over any outer ones, and one applying to the whole expression has priority over any of the default settings that are described in the remainder of this section.

The `use re '/foo'` pragma can be used to set default modifiers (including these) for regular expressions compiled within its scope. This pragma has precedence over the other pragmas listed below that also change the defaults. Note that the /x modifier does NOT affect `split STR` patterns.

Otherwise, `use locale` sets the default modifier to `/l`; and `use feature 'unicode_strings`, or `use v5.12` (or higher) set the default to `/u` when not in the same scope as either `use locale` or `use bytes`. (`use locale ':not_characters'` also sets the default to `/u`, overriding any plain `use locale`.) Unlike the mechanisms mentioned above, these affect operations besides regular expressions pattern matching, and so give more consistent results with other operators, including using `\U`, `\l`, *etc*. in substitution replacements.

If none of the above apply, for backwards compatibility reasons, the `/d` modifier is the one in effect by default. As this can lead to unexpected results, it is best to specify which other rule set should be used.

#### #Character set modifier behavior prior to Perl 5.14

Prior to 5.14, there were no explicit modifiers, but `/l` was implied for regexes compiled within the scope of `use locale`, and `/d` was implied otherwise. However, interpolating a regex into a larger regex would ignore the original compilation in favor of whatever was in effect at the time of the second compilation. There were a number of inconsistencies (bugs) with the `/d` modifier, where Unicode rules would be used when inappropriate, and vice versa. `\p{}` did not imply Unicode rules, and neither did all occurrences of `\N{}`, until 5.12.
