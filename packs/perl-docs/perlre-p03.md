---
title: "perlre (part 3/4)"
source: https://perldoc.perl.org/perlre
domain: perl-docs
license: GPL-1.0-or-later OR Artistic-1.0
tags: perl, perldoc, perl script, perl module, cpan
fetched: 2026-07-02
part: 3/4
---

## #Extended Patterns

Perl also defines a consistent extension syntax for features not found in standard tools like **awk** and **lex**. The syntax for most of these is a pair of parentheses with a question mark as the first thing within the parentheses. The character after the question mark indicates the extension.

A question mark was chosen for this and for the minimal-matching construct because 1) question marks are rare in older regular expressions, and 2) whenever you see one, you should stop and "question" exactly what is going on. That's psychology....

**#`(?#*text*)`**

A comment. The *text* is ignored. Note that Perl closes the comment as soon as it sees a `")"`, so there is no way to put a literal `")"` in the comment. The pattern's closing delimiter must be escaped by a backslash if it appears in the comment.

See "/x" for another way to have comments in patterns.

Note that a comment can go just about anywhere, except in the middle of an escape sequence. Examples:

```
qr/foo(?#comment)bar/'  # Matches 'foobar'

# The pattern below matches 'abcd', 'abccd', or 'abcccd'
qr/abc(?#comment between literal and its quantifier){1,3}d/

# The pattern below generates a syntax error, because the '\p' must
# be followed immediately by a '{'.
qr/\p(?#comment between \p and its property name){Any}/

# The pattern below generates a syntax error, because the initial
# '\(' is a literal opening parenthesis, and so there is nothing
# for the  closing ')' to match
qr/\(?#the backslash means this isn't a comment)p{Any}/

# Comments can be used to fold long patterns into multiple lines
qr/First part of a long regex(?#
  )remaining part/
```

**#`(?adlupimnsx-imnsx)`**

**#`(?^alupimnsx)`**

Zero or more embedded pattern-match modifiers, to be turned on (or turned off if preceded by `"-"`) for the remainder of the pattern or the remainder of the enclosing pattern group (if any).

This is particularly useful for dynamically-generated patterns, such as those read in from a configuration file, taken from an argument, or specified in a table somewhere. Consider the case where some patterns want to be case-sensitive and some do not: The case-insensitive ones merely need to include `(?i)` at the front of the pattern. For example:

```
$pattern = "foobar";
if ( /$pattern/i ) { }

# more flexible:

$pattern = "(?i)foobar";
if ( /$pattern/ ) { }
```

These modifiers are restored at the end of the enclosing group. For example,

```
( (?i) blah ) \s+ \g1
```

will match `blah` in any case, some spaces, and an exact (*including the case*!) repetition of the previous word, assuming the `/x` modifier, and no `/i` modifier outside this group.

These modifiers do not carry over into named subpatterns called in the enclosing group. In other words, a pattern such as `((?i)(?&*NAME*))` does not change the case-sensitivity of the *NAME* pattern.

A modifier is overridden by later occurrences of this construct in the same scope containing the same modifier, so that

```
/((?im)foo(?-m)bar)/
```

matches all of `foobar` case insensitively, but uses `/m` rules for only the `foo` portion. The `"a"` flag overrides `aa` as well; likewise `aa` overrides `"a"`. The same goes for `"x"` and `xx`. Hence, in

```
/(?-x)foo/xx
```

both `/x` and `/xx` are turned off during matching `foo`. And in

```
/(?x)foo/x
```

`/x` but NOT `/xx` is turned on for matching `foo`. (One might mistakenly think that since the inner `(?x)` is already in the scope of `/x`, that the result would effectively be the sum of them, yielding `/xx`. It doesn't work that way.) Similarly, doing something like `(?xx-x)foo` turns off all `"x"` behavior for matching `foo`, it is not that you subtract 1 `"x"` from 2 to get 1 `"x"` remaining.

Any of these modifiers can be set to apply globally to all regular expressions compiled within the scope of a `use re`. See "'/flags' mode" in re.

Starting in Perl 5.14, a `"^"` (caret or circumflex accent) immediately after the `"?"` is a shorthand equivalent to `d-imnsx`. Flags (except `"d"`) may follow the caret to override it. But a minus sign is not legal with it.

Note that the `"a"`, `"d"`, `"l"`, `"p"`, and `"u"` modifiers are special in that they can only be enabled, not disabled, and the `"a"`, `"d"`, `"l"`, and `"u"` modifiers are mutually exclusive: specifying one de-specifies the others, and a maximum of one (or two `"a"`'s) may appear in the construct. Thus, for example, `(?-p)` will warn when compiled under `use warnings`; `(?-d:...)` and `(?dl:...)` are fatal errors.

Note also that the `"p"` modifier is special in that its presence anywhere in a pattern has a global effect.

Having zero modifiers makes this a no-op (so why did you specify it, unless it's generated code), and starting in v5.30, warns under `use re 'strict'`.

**#`(?:*pattern*)`**

**#`(?adluimnsx-imnsx:*pattern*)`**

**#`(?^aluimnsx:*pattern*)`**

This is for clustering, not capturing; it groups subexpressions like `"()"`, but doesn't make backreferences as `"()"` does. So

```
@fields = split(/\b(?:a|b|c)\b/)
```

matches the same field delimiters as

```
@fields = split(/\b(a|b|c)\b/)
```

but doesn't spit out the delimiters themselves as extra fields (even though that's the behaviour of "split" in perlfunc when its pattern contains capturing groups). It's also cheaper not to capture characters if you don't need to.

Any letters between `"?"` and `":"` act as flags modifiers as with `(?adluimnsx-imnsx)`. For example,

```
/(?s-i:more.*than).*million/i
```

is equivalent to the more verbose

```
/(?:(?s-i)more.*than).*million/i
```

Note that any `()` constructs enclosed within this one will still capture unless the `/n` modifier is in effect.

Like the "(?adlupimnsx-imnsx)" construct, `aa` and `"a"` override each other, as do `xx` and `"x"`. They are not additive. So, doing something like `(?xx-x:foo)` turns off all `"x"` behavior for matching `foo`.

Starting in Perl 5.14, a `"^"` (caret or circumflex accent) immediately after the `"?"` is a shorthand equivalent to `d-imnsx`. Any positive flags (except `"d"`) may follow the caret, so

```
(?^x:foo)
```

is equivalent to

```
(?x-imns:foo)
```

The caret tells Perl that this cluster doesn't inherit the flags of any surrounding pattern, but uses the system defaults (`d-imnsx`), modified by any flags specified.

The caret allows for simpler stringification of compiled regular expressions. These look like

```
(?^:pattern)
```

with any non-default flags appearing between the caret and the colon. A test that looks at such stringification thus doesn't need to have the system default flags hard-coded in it, just the caret. If new flags are added to Perl, the meaning of the caret's expansion will change to include the default for those flags, so the test will still work, unchanged.

Specifying a negative flag after the caret is an error, as the flag is redundant.

Mnemonic for `(?^...)`: A fresh beginning since the usual use of a caret is to match at the beginning.

**#`(?|*pattern*)`**

This is the "branch reset" pattern, which has the special property that the capture groups are numbered from the same starting point in each alternation branch. It is available starting from perl 5.10.0.

Capture groups are numbered from left to right, but inside this construct the numbering is restarted for each branch.

The numbering within each branch will be as normal, and any groups following this construct will be numbered as though the construct contained only one branch, that being the one with the most capture groups in it.

This construct is useful when you want to capture one of a number of alternative matches.

Consider the following pattern. The numbers underneath show in which group the captured content will be stored.

```
# before  ---------------branch-reset----------- after
/ ( a )  (?| x ( y ) z | (p (q) r) | (t) u (v) ) ( z ) /x
# 1            2         2  3        2     3     4
```

Be careful when using the branch reset pattern in combination with named captures. Named captures are implemented as being aliases to numbered groups holding the captures, and that interferes with the implementation of the branch reset pattern. If you are using named captures in a branch reset pattern, it's best to use the same names, in the same order, in each of the alternations:

```
/(?|  (?<a> x ) (?<b> y )
   |  (?<a> z ) (?<b> w )) /x
```

Not doing so may lead to surprises:

```
"12" =~ /(?| (?<a> \d+ ) | (?<b> \D+))/x;
say $+{a};    # Prints '12'
say $+{b};    # *Also* prints '12'.
```

The problem here is that both the group named `a` and the group named `b` are aliases for the group belonging to `$1`.

**#Lookaround Assertions**

Lookaround assertions are zero-width patterns which match a specific pattern without including it in `$&`. Positive assertions match when their subpattern matches, negative assertions match when their subpattern fails. Lookbehind matches text up to the current match position, lookahead matches text following the current match position.

**#`(?=*pattern*)`**

**#`(*pla:*pattern*)`**

**#`(*positive_lookahead:*pattern*)`**

A zero-width positive lookahead assertion. For example, `/\w+(?=\t)/` matches a word followed by a tab, without including the tab in `$&`.

**#`(?!*pattern*)`**

**#`(*nla:*pattern*)`**

**#`(*negative_lookahead:*pattern*)`**

A zero-width negative lookahead assertion. For example `/foo(?!bar)/` matches any occurrence of "foo" that isn't followed by "bar". Note however that lookahead and lookbehind are NOT the same thing. You cannot use this for lookbehind.

If you are looking for a "bar" that isn't preceded by a "foo", `/(?!foo)bar/` will not do what you want. That's because the `(?!foo)` is just saying that the next thing cannot be "foo"--and it's not, it's a "bar", so "foobar" will match. Use lookbehind instead (see below).

**#`(?<=*pattern*)`**

**#`\K`**

**#`(*plb:*pattern*)`**

**#`(*positive_lookbehind:*pattern*)`**

A zero-width positive lookbehind assertion. For example, `/(?<=\t)\w+/` matches a word that follows a tab, without including the tab in `$&`.

Prior to Perl 5.30, it worked only for fixed-width lookbehind, but starting in that release, it can handle variable lengths from 1 to 255 characters as an experimental feature. The feature is enabled automatically if you use a variable length positive lookbehind assertion.

In Perl 5.35.10 the scope of the experimental nature of this construct has been reduced, and experimental warnings will only be produced when the construct contains capturing parentheses. The warnings will be raised at pattern compilation time, unless turned off, in the `experimental::vlb` category. This is to warn you that the exact contents of capturing buffers in a variable length positive lookbehind is not well defined and is subject to change in a future release of perl.

Currently if you use capture buffers inside of a positive variable length lookbehind the result will be the longest and thus leftmost match possible. This means that

```
"aax" =~ /(?=x)(?<=(a|aa))/
"aax" =~ /(?=x)(?<=(aa|a))/
"aax" =~ /(?=x)(?<=(a{1,2}?)/
"aax" =~ /(?=x)(?<=(a{1,2})/
```

will all result in `$1` containing `"aa"`. It is possible in a future release of perl we will change this behavior.

There is a special form of this construct, called `\K` (available since Perl 5.10.0), which causes the regex engine to "keep" everything it had matched prior to the `\K` and not include it in `$&`. This effectively provides non-experimental variable-length lookbehind of any length.

And, there is a technique that can be used to handle variable length lookbehinds on earlier releases, and longer than 255 characters. It is described in http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html.

Note that under `/i`, a few single characters match two or three other characters. This makes them variable length, and the 255 length applies to the maximum number of characters in the match. For example `qr/\N{LATIN SMALL LETTER SHARP S}/i` matches the sequence `"ss"`. Your lookbehind assertion could contain 127 Sharp S characters under `/i`, but adding a 128th would generate a compilation error, as that could match 256 `"s"` characters in a row.

The use of `\K` inside of another lookaround assertion is allowed, but the behaviour is currently not well defined.

For various reasons `\K` may be significantly more efficient than the equivalent `(?<=...)` construct, and it is especially useful in situations where you want to efficiently remove something following something else in a string. For instance

```
s/(foo)bar/$1/g;
```

can be rewritten as the much more efficient

```
s/foo\Kbar//g;
```

Use of the non-greedy modifier `"?"` may not give you the expected results if it is within a capturing group within the construct.

**#`(?<!*pattern*)`**

**#`(*nlb:*pattern*)`**

**#`(*negative_lookbehind:*pattern*)`**

A zero-width negative lookbehind assertion. For example `/(?<!bar)foo/` matches any occurrence of "foo" that does not follow "bar".

Prior to Perl 5.30, it worked only for fixed-width lookbehind, but starting in that release, it can handle variable lengths from 1 to 255 characters as an experimental feature. The feature is enabled automatically if you use a variable length negative lookbehind assertion.

In Perl 5.35.10 the scope of the experimental nature of this construct has been reduced, and experimental warnings will only be produced when the construct contains capturing parentheses. The warnings will be raised at pattern compilation time, unless turned off, in the `experimental::vlb` category. This is to warn you that the exact contents of capturing buffers in a variable length negative lookbehind is not well defined and is subject to change in a future release of perl.

Currently if you use capture buffers inside of a negative variable length lookbehind the result may not be what you expect, for instance:

```
say "axfoo"=~/(?=foo)(?<!(a|ax)(?{ say $1 }))/ ? "y" : "n";
```

will output the following:

```
a
no
```

which does not make sense as this should print out "ax" as the "a" does not line up at the correct place. Another example would be:

```
say "yes: '$1-$2'" if "aayfoo"=~/(?=foo)(?<!(a|aa)(a|aa)x)/;
```

will output the following:

```
yes: 'aa-a'
```

It is possible in a future release of perl we will change this behavior so both of these examples produced more reasonable output.

Note that we are confident that the construct will match and reject patterns appropriately, the undefined behavior strictly relates to the value of the capture buffer during or after matching.

There is a technique that can be used to handle variable length lookbehind on earlier releases, and longer than 255 characters. It is described in http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html.

Note that under `/i`, a few single characters match two or three other characters. This makes them variable length, and the 255 length applies to the maximum number of characters in the match. For example `qr/\N{LATIN SMALL LETTER SHARP S}/i` matches the sequence `"ss"`. Your lookbehind assertion could contain 127 Sharp S characters under `/i`, but adding a 128th would generate a compilation error, as that could match 256 `"s"` characters in a row.

Use of the non-greedy modifier `"?"` may not give you the expected results if it is within a capturing group within the construct.

**#`(?<*NAME*>*pattern*)`**

**#`(?'*NAME*'*pattern*)`**

A named capture group. Identical in every respect to normal capturing parentheses `()` but for the additional fact that the group can be referred to by name in various regular expression constructs (like `\g{*NAME*}`) and can be accessed by name after a successful match via `%+` or `%-`. See perlvar for more details on the `%+` and `%-` hashes.

If multiple distinct capture groups have the same name, then `$+{*NAME*}` will refer to the leftmost defined group in the match.

The forms `(?'*NAME*'*pattern*)` and `(?<*NAME*>*pattern*)` are equivalent.

**NOTE:** While the notation of this construct is the same as the similar function in .NET regexes, the behavior is not. In Perl the groups are numbered sequentially regardless of being named or not. Thus in the pattern

```
/(x)(?<foo>y)(z)/
```

`$+{foo}` will be the same as `$2`, and `$3` will contain 'z' instead of the opposite which is what a .NET regex hacker might expect.

Currently *NAME* is restricted to simple identifiers only. In other words, it must match `/^[_A-Za-z][_A-Za-z0-9]*\z/` or its Unicode extension (see utf8), though it isn't extended by the locale (see perllocale).

**NOTE:** In order to make things easier for programmers with experience with the Python or PCRE regex engines, the pattern `(?P<*NAME*>*pattern*)` may be used instead of `(?<*NAME*>*pattern*)`; however this form does not support the use of single quotes as a delimiter for the name.

**#`\k<*NAME*>`**

**#`\k'*NAME*'`**

**#`\k{*NAME*}`**

Named backreference. Similar to numeric backreferences, except that the group is designated by name and not number. If multiple groups have the same name then it refers to the leftmost defined group in the current match.

It is an error to refer to a name not defined by a `(?<*NAME*>)` earlier in the pattern.

All three forms are equivalent, although with `\k{ *NAME* }`, you may optionally have blanks within but adjacent to the braces, as shown.

**NOTE:** In order to make things easier for programmers with experience with the Python or PCRE regex engines, the pattern `(?P=*NAME*)` may be used instead of `\k<*NAME*>`.

**#`(?{ *code* })`**

**WARNING**: Using this feature safely requires that you understand its limitations. Code executed that has side effects may not perform identically from version to version due to the effect of future optimisations in the regex engine. For more information on this, see "Embedded Code Execution Frequency".

This zero-width assertion executes any embedded Perl code. It always succeeds, and its return value is set as `$^R`.

In literal patterns, the code is parsed at the same time as the surrounding code. While within the pattern, control is passed temporarily back to the perl parser, until the logically-balancing closing brace is encountered. This is similar to the way that an array index expression in a literal string is handled, for example

```
"abc$array[ 1 + f('[') + g()]def"
```

In particular, braces do not need to be balanced:

```
s/abc(?{ f('{'); })/def/
```

Even in a pattern that is interpolated and compiled at run-time, literal code blocks will be compiled once, at perl compile time; the following prints "ABCD":

```
print "D";
my $qr = qr/(?{ BEGIN { print "A" } })/;
my $foo = "foo";
/$foo$qr(?{ BEGIN { print "B" } })/;
BEGIN { print "C" }
```

In patterns where the text of the code is derived from run-time information rather than appearing literally in a source code /pattern/, the code is compiled at the same time that the pattern is compiled, and for reasons of security, `use re 'eval'` must be in scope. This is to stop user-supplied patterns containing code snippets from being executable.

In situations where you need to enable this with `use re 'eval'`, you should also have taint checking enabled, if your perl supports it. Better yet, use the carefully constrained evaluation within a Safe compartment. See perlsec for details about both these mechanisms.

From the viewpoint of parsing, lexical variable scope and closures,

```
/AAA(?{ BBB })CCC/
```

behaves approximately like

```
/AAA/ && do { BBB } && /CCC/
```

Similarly,

```
qr/AAA(?{ BBB })CCC/
```

behaves approximately like

```
sub { /AAA/ && do { BBB } && /CCC/ }
```

In particular:

```
{ my $i = 1; $r = qr/(?{ print $i })/ }
my $i = 2;
/$r/; # prints "1"
```

Inside a `(?{...})` block, `$_` refers to the string the regular expression is matching against. You can also use `pos()` to know what is the current position of matching within this string.

The code block introduces a new scope from the perspective of lexical variable declarations, but **not** from the perspective of `local` and similar localizing behaviours. So later code blocks within the same pattern will still see the values which were localized in earlier blocks. These accumulated localizations are undone either at the end of a successful match, or if the assertion is backtracked (compare "Backtracking"). For example,

```
$_ = 'a' x 8;
m<
   (?{ $cnt = 0 })               # Initialize $cnt.
   (
     a
     (?{
         local $cnt = $cnt + 1;  # Update $cnt,
                                 # backtracking-safe.
     })
   )*
   aaaa
   (?{ $res = $cnt })            # On success copy to
                                 # non-localized location.
 >x;
```

will initially increment `$cnt` up to 8; then during backtracking, its value will be unwound back to 4, which is the value assigned to `$res`. At the end of the regex execution, `$cnt` will be wound back to its initial value of 0.

This assertion may be used as the condition in a

```
(?(condition)yes-pattern|no-pattern)
```

switch. If *not* used in this way, the result of evaluation of *code* is put into the special variable `$^R`. This happens immediately, so `$^R` can be used from other `(?{ *code* })` assertions inside the same regular expression.

The assignment to `$^R` above is properly localized, so the old value of `$^R` is restored if the assertion is backtracked; compare "Backtracking".

Note that the special variable `$^N` is particularly useful with code blocks to capture the results of submatches in variables without having to keep track of the number of nested parentheses. For example:

```
$_ = "The brown fox jumps over the lazy dog";
/the (\S+)(?{ $color = $^N }) (\S+)(?{ $animal = $^N })/i;
print "color = $color, animal = $animal\n";
```

The use of this construct disables some optimisations globally in the pattern, and the pattern may execute much slower as a consequence. Use a `*` instead of the `?` block to create an optimistic form of this construct. `(*{ ... })` should not disable any optimisations.

**#`(*{ *code* })`**

This is *exactly* the same as `(?{ *code* })` with the exception that it does not disable **any** optimisations at all in the regex engine. How often it is executed may vary from perl release to perl release. In a failing match it may not even be executed at all.

**#`(??{ *code* })`**

**WARNING**: Using this feature safely requires that you understand its limitations. Code executed that has side effects may not perform identically from version to version due to the effect of future optimisations in the regex engine. For more information on this, see "Embedded Code Execution Frequency".

This is a "postponed" regular subexpression. It behaves in *exactly* the same way as a `(?{ *code* })` code block as described above, except that its return value, rather than being assigned to `$^R`, is treated as a pattern, compiled if it's a string (or used as-is if it's a qr// object), then matched as if it were inserted instead of this construct.

During the matching of this sub-pattern, it has its own set of captures which are valid during the sub-match, but are discarded once control returns to the main pattern. For example, the following matches, with the inner pattern capturing "B" and matching "BB", while the outer pattern captures "A";

```
my $inner = '(.)\1';
"ABBA" =~ /^(.)(??{ $inner })\1/;
print $1; # prints "A";
```

Note that this means that there is no way for the inner pattern to refer to a capture group defined outside. (The code block itself can use `$1`, *etc*., to refer to the enclosing pattern's capture groups.) Thus, although

```
('a' x 100)=~/(??{'(.)' x 100})/
```

*will* match, it will *not* set `$1` on exit.

The following pattern matches a parenthesized group:

```
$re = qr{
           \(
           (?:
              (?> [^()]+ )  # Non-parens without backtracking
            |
              (??{ $re })   # Group with matching parens
           )*
           \)
        }x;
```

See also `(?*PARNO*)` for a different, more efficient way to accomplish the same task.

Executing a postponed regular expression too many times without consuming any input string will also result in a fatal error. The depth at which that happens is compiled into perl, so it can be changed with a custom build.

The use of this construct disables some optimisations globally in the pattern, and the pattern may execute much slower as a consequence.

**#`(?*PARNO*)` `(?-*PARNO*)` `(?+*PARNO*)` `(?R)` `(?0)`**

Recursive subpattern. Treat the contents of a given capture buffer in the current pattern as an independent subpattern and attempt to match it at the current position in the string. Information about capture state from the caller for things like backreferences is available to the subpattern, but capture buffers set by the subpattern are not visible to the caller.

Similar to `(??{ *code* })` except that it does not involve executing any code or potentially compiling a returned pattern string; instead it treats the part of the current pattern contained within a specified capture group as an independent pattern that must match at the current position. Also different is the treatment of capture buffers, unlike `(??{ *code* })` recursive patterns have access to their caller's match state, so one can use backreferences safely.

*PARNO* is a sequence of digits (not starting with 0) whose value reflects the paren-number of the capture group to recurse to. `(?R)` recurses to the beginning of the whole pattern. `(?0)` is an alternate syntax for `(?R)`. If *PARNO* is preceded by a plus or minus sign then it is assumed to be relative, with negative numbers indicating preceding capture groups and positive ones following. Thus `(?-1)` refers to the most recently declared group, and `(?+1)` indicates the next group to be declared. Note that the counting for relative recursion differs from that of relative backreferences, in that with recursion unclosed groups **are** included.

The following pattern matches a function `foo()` which may contain balanced parentheses as the argument.

```
$re = qr{ (                   # paren group 1 (full function)
            foo
            (                 # paren group 2 (parens)
              \(
                (             # paren group 3 (contents of parens)
                (?:
                 (?> [^()]+ ) # Non-parens without backtracking
                |
                 (?2)         # Recurse to start of paren group 2
                )*
                )
              \)
            )
          )
        }x;
```

If the pattern was used as follows

```
'foo(bar(baz)+baz(bop))'=~/$re/
    and print "\$1 = $1\n",
              "\$2 = $2\n",
              "\$3 = $3\n";
```

the output produced should be the following:

```
$1 = foo(bar(baz)+baz(bop))
$2 = (bar(baz)+baz(bop))
$3 = bar(baz)+baz(bop)
```

If there is no corresponding capture group defined, then it is a fatal error. Recursing deeply without consuming any input string will also result in a fatal error. The depth at which that happens is compiled into perl, so it can be changed with a custom build.

The following shows how using negative indexing can make it easier to embed recursive patterns inside of a `qr//` construct for later use:

```
my $parens = qr/(\((?:[^()]++|(?-1))*+\))/;
if (/foo $parens \s+ \+ \s+ bar $parens/x) {
   # do something here...
}
```

**Note** that this pattern does not behave the same way as the equivalent PCRE or Python construct of the same form. In Perl you can backtrack into a recursed group, in PCRE and Python the recursed into group is treated as atomic. Also, modifiers are resolved at compile time, so constructs like `(?i:(?1))` or `(?:(?i)(?1))` do not affect how the sub-pattern will be processed.

**#`(?&*NAME*)`**

Recurse to a named subpattern. Identical to `(?*PARNO*)` except that the parenthesis to recurse to is determined by name. If multiple parentheses have the same name, then it recurses to the leftmost.

It is an error to refer to a name that is not declared somewhere in the pattern.

**NOTE:** In order to make things easier for programmers with experience with the Python or PCRE regex engines the pattern `(?P>*NAME*)` may be used instead of `(?&*NAME*)`.

**#`(?(*condition*)*yes-pattern*|*no-pattern*)`**

**#`(?(*condition*)*yes-pattern*)`**

Conditional expression. Matches *yes-pattern* if *condition* yields a true value, matches *no-pattern* otherwise. A missing pattern always matches.

`(*condition*)` should be one of:

**#an integer in parentheses**

(which is valid if the corresponding pair of parentheses matched);

**#a lookahead/lookbehind/evaluate zero-width assertion;**

**#a name in angle brackets or single quotes**

(which is valid if a group with the given name matched);

**#the special symbol `(R)`**

(true when evaluated inside of recursion or eval). Additionally the `"R"` may be followed by a number, (which will be true when evaluated when recursing inside of the appropriate group), or by `&*NAME*`, in which case it will be true only when evaluated during recursion in the named group.

Here's a summary of the possible predicates:

**#`(1)` `(2)` ...**

Checks if the numbered capturing group has matched something. Full syntax: `(?(1)then|else)`

**#`(<*NAME*>)` `('*NAME*')`**

Checks if a group with the given name has matched something. Full syntax: `(?(<name>)then|else)`

**#`(?=...)` `(?!...)` `(?<=...)` `(?<!...)`**

Checks whether the pattern matches (or does not match, for the `"!"` variants). Full syntax: `(?(?=*lookahead*)*then*|*else*)`

**#`(?{ *CODE* })`**

Treats the return value of the code block as the condition. Full syntax: `(?(?{ *CODE* })*then*|*else*)`

Note use of this construct may globally affect the performance of the pattern. Consider using `(*{ *CODE* })`

**#`(*{ *CODE* })`**

Treats the return value of the code block as the condition. Full syntax: `(?(*{ *CODE* })*then*|*else*)`

**#`(R)`**

Checks if the expression has been evaluated inside of recursion. Full syntax: `(?(R)*then*|*else*)`

**#`(R1)` `(R2)` ...**

Checks if the expression has been evaluated while executing directly inside of the n-th capture group. This check is the regex equivalent of

```
if ((caller(0))[3] eq 'subname') { ... }
```

In other words, it does not check the full recursion stack.

Full syntax: `(?(R1)*then*|*else*)`

**#`(R&*NAME*)`**

Similar to `(R1)`, this predicate checks to see if we're executing directly inside of the leftmost group with a given name (this is the same logic used by `(?&*NAME*)` to disambiguate). It does not check the full stack, but only the name of the innermost active recursion. Full syntax: `(?(R&*name*)*then*|*else*)`

**#`(DEFINE)`**

In this case, the yes-pattern is never directly executed, and no no-pattern is allowed. Similar in spirit to `(?{0})` but more efficient. See below for details. Full syntax: `(?(DEFINE)*definitions*...)`

For example:

```
m{ ( \( )?
   [^()]+
   (?(1) \) )
 }x
```

matches a chunk of non-parentheses, possibly included in parentheses themselves.

A special form is the `(DEFINE)` predicate, which never executes its yes-pattern directly, and does not allow a no-pattern. This allows one to define subpatterns which will be executed only by the recursion mechanism. This way, you can define a set of regular expression rules that can be bundled into any pattern you choose.

It is recommended that for this usage you put the DEFINE block at the end of the pattern, and that you name any subpatterns defined within it.

Also, it's worth noting that patterns defined this way probably will not be as efficient, as the optimizer is not very clever about handling them.

An example of how this might be used is as follows:

```
/(?<NAME>(?&NAME_PAT))(?<ADDR>(?&ADDRESS_PAT))
 (?(DEFINE)
   (?<NAME_PAT>....)
   (?<ADDRESS_PAT>....)
 )/x
```

Note that capture groups matched inside of recursion are not accessible after the recursion returns, so the extra layer of capturing groups is necessary. Thus `$+{NAME_PAT}` would not be defined even though `$+{NAME}` would be.

Finally, keep in mind that subpatterns created inside a DEFINE block count towards the absolute and relative number of captures, so this:

```
my @captures = "a" =~ /(.)                  # First capture
                       (?(DEFINE)
                           (?<EXAMPLE> 1 )  # Second capture
                       )/x;
say scalar @captures;
```

Will output 2, not 1. This is particularly important if you intend to compile the definitions with the `qr//` operator, and later interpolate them in another pattern.

**#`(?>*pattern*)`**

**#`(*atomic:*pattern*)`**

An "independent" subexpression, one which matches the substring that a standalone *pattern* would match if anchored at the given position, and it matches *nothing other than this substring*. This construct is useful for optimizations of what would otherwise be "eternal" matches, because it will not backtrack (see "Backtracking"). It may also be useful in places where the "grab all you can, and do not give anything back" semantic is desirable.

For example: `^(?>a*)ab` will never match, since `(?>a*)` (anchored at the beginning of string, as above) will match *all* characters `"a"` at the beginning of string, leaving no `"a"` for `ab` to match. In contrast, `a*ab` will match the same as `a+b`, since the match of the subgroup `a*` is influenced by the following group `ab` (see "Backtracking"). In particular, `a*` inside `a*ab` will match fewer characters than a standalone `a*`, since this makes the tail match.

`(?>*pattern*)` does not disable backtracking altogether once it has matched. It is still possible to backtrack past the construct, but not into it. So `((?>a*)|(?>b*))ar` will still match "bar".

An effect similar to `(?>*pattern*)` may be achieved by writing `(?=(*pattern*))\g{-1}`. This matches the same substring as a standalone `a+`, and the following `\g{-1}` eats the matched string; it therefore makes a zero-length assertion into an analogue of `(?>...)`. (The difference between these two constructs is that the second one uses a capturing group, thus shifting ordinals of backreferences in the rest of a regular expression.)

Consider this pattern:

```
m{ \(
      (
        [^()]+           # x+
      |
        \( [^()]* \)
      )+
   \)
 }x
```

That will efficiently match a nonempty group with matching parentheses two levels deep or less. However, if there is no such group, it will take virtually forever on a long string. That's because there are so many different ways to split a long string into several substrings. This is what `(.+)+` is doing, and `(.+)+` is similar to a subpattern of the above pattern. Consider how the pattern above detects no-match on `((()aaaaaaaaaaaaaaaaaa` in several seconds, but that each extra letter doubles this time. This exponential performance will make it appear that your program has hung. However, a tiny change to this pattern

```
m{ \(
      (
        (?> [^()]+ )        # change x+ above to (?> x+ )
      |
        \( [^()]* \)
      )+
   \)
 }x
```

which uses `(?>...)` matches exactly when the one above does (verifying this yourself would be a productive exercise), but finishes in a fourth the time when used on a similar string with 1000000 `"a"`s. Be aware, however, that, when this construct is followed by a quantifier, it currently triggers a warning message under the `use warnings` pragma or **-w** switch saying it `"matches null string many times in regex"`.

On simple groups, such as the pattern `(?> [^()]+ )`, a comparable effect may be achieved by negative lookahead, as in `[^()]+ (?! [^()] )`. This was only 4 times slower on a string with 1000000 `"a"`s.

The "grab all you can, and do not give anything back" semantic is desirable in many situations where on the first sight a simple `()*` looks like the correct solution. Suppose we parse text with comments being delimited by `"#"` followed by some optional (horizontal) whitespace. Contrary to its appearance, `#[ \t]*` *is not* the correct subexpression to match the comment delimiter, because it may "give up" some whitespace if the remainder of the pattern can be made to match that way. The correct answer is either one of these:

```
(?>#[ \t]*)
#[ \t]*(?![ \t])
```

For example, to grab non-empty comments into `$1`, one should use either one of these:

```
/ (?> \# [ \t]* ) (        .+ ) /x;
/     \# [ \t]*   ( [^ \t] .* ) /x;
```

Which one you pick depends on which of these expressions better reflects the above specification of comments.

In some literature this construct is called "atomic matching" or "possessive matching".

Possessive quantifiers are equivalent to putting the item they are applied to inside of one of these constructs. The following equivalences apply:

```
Quantifier Form     Bracketing Form
---------------     ---------------
PAT*+               (?>PAT*)
PAT++               (?>PAT+)
PAT?+               (?>PAT?)
PAT{min,max}+       (?>PAT{min,max})
```

Nested `(?>...)` constructs are not no-ops, even if at first glance they might seem to be. This is because the nested `(?>...)` can restrict internal backtracking that otherwise might occur. For example,

```
"abc" =~ /(?>a[bc]*c)/
```

matches, but

```
"abc" =~ /(?>a(?>[bc]*)c)/
```

does not.

**#`(?[ ])`**

See "Extended Bracketed Character Classes" in perlrecharclass.


## #Backtracking

NOTE: This section presents an abstract approximation of regular expression behavior. For a more rigorous (and complicated) view of the rules involved in selecting a match among possible alternatives, see "Combining RE Pieces".

A fundamental feature of regular expression matching involves the notion called *backtracking*, which is currently used (when needed) by all regular non-possessive expression quantifiers, namely `"*"`, `*?`, `"+"`, `+?`, `{n,m}`, and `{n,m}?`. Backtracking is often optimized internally, but the general principle outlined here is valid.

For a regular expression to match, the *entire* regular expression must match, not just part of it. So if the beginning of a pattern containing a quantifier succeeds in a way that causes later parts in the pattern to fail, the matching engine backs up and recalculates the beginning part--that's why it's called backtracking.

Here is an example of backtracking: Let's say you want to find the word following "foo" in the string "Food is on the foo table.":

```
$_ = "Food is on the foo table.";
if ( /\b(foo)\s+(\w+)/i ) {
    print "$2 follows $1.\n";
}
```

When the match runs, the first part of the regular expression (`\b(foo)`) finds a possible match right at the beginning of the string, and loads up `$1` with "Foo". However, as soon as the matching engine sees that there's no whitespace following the "Foo" that it had saved in `$1`, it realizes its mistake and starts over again one character after where it had the tentative match. This time it goes all the way until the next occurrence of "foo". The complete regular expression matches this time, and you get the expected output of "table follows foo."

Sometimes minimal matching can help a lot. Imagine you'd like to match everything between "foo" and "bar". Initially, you write something like this:

```
$_ =  "The food is under the bar in the barn.";
if ( /foo(.*)bar/ ) {
    print "got <$1>\n";
}
```

Which perhaps unexpectedly yields:

```
got <d is under the bar in the >
```

That's because `.*` was greedy, so you get everything between the *first* "foo" and the *last* "bar". Here it's more effective to use minimal matching to make sure you get the text between a "foo" and the first "bar" thereafter.

```
  if ( /foo(.*?)bar/ ) { print "got <$1>\n" }
got <d is under the >
```

Here's another example. Let's say you'd like to match a number at the end of a string, and you also want to keep the preceding part of the match. So you write this:

```
$_ = "I have 2 numbers: 53147";
if ( /(.*)(\d*)/ ) {                                # Wrong!
    print "Beginning is <$1>, number is <$2>.\n";
}
```

That won't work at all, because `.*` was greedy and gobbled up the whole string. As `\d*` can match on an empty string the complete regular expression matched successfully.

```
Beginning is <I have 2 numbers: 53147>, number is <>.
```

Here are some variants, most of which don't work:

```
$_ = "I have 2 numbers: 53147";
@pats = qw{
    (.*)(\d*)
    (.*)(\d+)
    (.*?)(\d*)
    (.*?)(\d+)
    (.*)(\d+)$
    (.*?)(\d+)$
    (.*)\b(\d+)$
    (.*\D)(\d+)$
};

for $pat (@pats) {
    printf "%-12s ", $pat;
    if ( /$pat/ ) {
        print "<$1> <$2>\n";
    } else {
        print "FAIL\n";
    }
}
```

That will print out:

```
(.*)(\d*)    <I have 2 numbers: 53147> <>
(.*)(\d+)    <I have 2 numbers: 5314> <7>
(.*?)(\d*)   <> <>
(.*?)(\d+)   <I have > <2>
(.*)(\d+)$   <I have 2 numbers: 5314> <7>
(.*?)(\d+)$  <I have 2 numbers: > <53147>
(.*)\b(\d+)$ <I have 2 numbers: > <53147>
(.*\D)(\d+)$ <I have 2 numbers: > <53147>
```

As you see, this can be a bit tricky. It's important to realize that a regular expression is merely a set of assertions that gives a definition of success. There may be 0, 1, or several different ways that the definition might succeed against a particular string. And if there are multiple ways it might succeed, you need to understand backtracking to know which variety of success you will achieve.

When using lookahead assertions and negations, this can all get even trickier. Imagine you'd like to find a sequence of non-digits not followed by "123". You might try to write that as

```
$_ = "ABC123";
if ( /^\D*(?!123)/ ) {                # Wrong!
    print "Yup, no 123 in $_\n";
}
```

But that isn't going to match; at least, not the way you're hoping. It claims that there is no 123 in the string. Here's a clearer picture of why that pattern matches, contrary to popular expectations:

```
$x = 'ABC123';
$y = 'ABC445';

print "1: got $1\n" if $x =~ /^(ABC)(?!123)/;
print "2: got $1\n" if $y =~ /^(ABC)(?!123)/;

print "3: got $1\n" if $x =~ /^(\D*)(?!123)/;
print "4: got $1\n" if $y =~ /^(\D*)(?!123)/;
```

This prints

```
2: got ABC
3: got AB
4: got ABC
```

You might have expected test 3 to fail because it seems to a more general purpose version of test 1. The important difference between them is that test 3 contains a quantifier (`\D*`) and so can use backtracking, whereas test 1 will not. What's happening is that you've asked "Is it true that at the start of `$x`, following 0 or more non-digits, you have something that's not 123?" If the pattern matcher had let `\D*` expand to "ABC", this would have caused the whole pattern to fail.

The search engine will initially match `\D*` with "ABC". Then it will try to match `(?!123)` with "123", which fails. But because a quantifier (`\D*`) has been used in the regular expression, the search engine can backtrack and retry the match differently in the hope of matching the complete regular expression.

The pattern really, *really* wants to succeed, so it uses the standard pattern back-off-and-retry and lets `\D*` expand to just "AB" this time. Now there's indeed something following "AB" that is not "123". It's "C123", which suffices.

We can deal with this by using both an assertion and a negation. We'll say that the first part in `$1` must be followed both by a digit and by something that's not "123". Remember that the lookaheads are zero-width expressions--they only look, but don't consume any of the string in their match. So rewriting this way produces what you'd expect; that is, case 5 will fail, but case 6 succeeds:

```
print "5: got $1\n" if $x =~ /^(\D*)(?=\d)(?!123)/;
print "6: got $1\n" if $y =~ /^(\D*)(?=\d)(?!123)/;

6: got ABC
```

In other words, the two zero-width assertions next to each other work as though they're ANDed together, just as you'd use any built-in assertions: `/^$/` matches only if you're at the beginning of the line AND the end of the line simultaneously. The deeper underlying truth is that juxtaposition in regular expressions always means AND, except when you write an explicit OR using the vertical bar. `/ab/` means match "a" AND (then) match "b", although the attempted matches are made at different positions because "a" is not a zero-width assertion, but a one-width assertion.

**WARNING**: Particularly complicated regular expressions can take exponential time to solve because of the immense number of possible ways they can use backtracking to try for a match. For example, without internal optimizations done by the regular expression engine, this will take a painfully long time to run:

```
'aaaaaaaaaaaa' =~ /((a{0,5}){0,5})*[c]/
```

And if you used `"*"`'s in the internal groups instead of limiting them to 0 through 5 matches, then it would take forever--or until you ran out of stack space. Moreover, these internal optimizations are not always applicable. For example, if you put `{0,5}` instead of `"*"` on the external group, no current optimization is applicable, and the match takes a long time to finish.

A powerful tool for optimizing such beasts is what is known as an "independent group", which does not backtrack (see `"(?>pattern)"`). Note also that zero-length lookahead/lookbehind assertions will not backtrack to make the tail match, since they are in "logical" context: only whether they match is considered relevant. For an example where side-effects of lookahead *might* have influenced the following match, see `"(?>pattern)"`.
