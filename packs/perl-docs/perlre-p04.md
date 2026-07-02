---
title: "perlre (part 4/4)"
source: https://perldoc.perl.org/perlre
domain: perl-docs
license: GPL-1.0-or-later OR Artistic-1.0
tags: perl, perldoc, perl script, perl module, cpan
fetched: 2026-07-02
part: 4/4
---

## #Script Runs

A script run is basically a sequence of characters, all from the same Unicode script (see "Scripts" in perlunicode), such as Latin or Greek. In most places a single word would never be written in multiple scripts, unless it is a spoofing attack. An infamous example, is

```
paypal.com
```

Those letters could all be Latin (as in the example just above), or they could be all Cyrillic (except for the dot), or they could be a mixture of the two. In the case of an internet address the `.com` would be in Latin, And any Cyrillic ones would cause it to be a mixture, not a script run. Someone clicking on such a link would not be directed to the real PayPal website, but an attacker would craft a look-alike one to attempt to gather sensitive information from the person.

Starting in Perl 5.28, it is now easy to detect strings that aren't script runs. Simply enclose just about any pattern like either of these:

```
(*script_run:pattern)
(*sr:pattern)
```

What happens is that after *pattern* succeeds in matching, it is subjected to the additional criterion that every character in it must be from the same script (see exceptions below). If this isn't true, backtracking occurs until something all in the same script is found that matches, or all possibilities are exhausted. This can cause a lot of backtracking, but generally, only malicious input will result in this, though the slow down could cause a denial of service attack. If your needs permit, it is best to make the pattern atomic to cut down on the amount of backtracking. This is so likely to be what you want, that instead of writing this:

```
(*script_run:(?>pattern))
```

you can write either of these:

```
(*atomic_script_run:pattern)
(*asr:pattern)
```

(See `"(?>*pattern*)"`.)

In Taiwan, Japan, and Korea, it is common for text to have a mixture of characters from their native scripts and base Chinese. Perl follows Unicode's UTS 39 (https://unicode.org/reports/tr39/) Unicode Security Mechanisms in allowing such mixtures. For example, the Japanese scripts Katakana and Hiragana are commonly mixed together in practice, along with some Chinese characters, and hence are treated as being in a single script run by Perl.

The rules used for matching decimal digits are slightly stricter. Many scripts have their own sets of digits equivalent to the Western `0` through `9` ones. A few, such as Arabic, have more than one set. For a string to be considered a script run, all digits in it must come from the same set of ten, as determined by the first digit encountered. As an example,

```
qr/(*script_run: \d+ \b )/x
```

guarantees that the digits matched will all be from the same set of 10. You won't get a look-alike digit from a different script that has a different value than what it appears to be.

Unicode has three pseudo scripts that are handled specially.

"Unknown" is applied to code points whose meaning has yet to be determined. Perl currently will match as a script run, any single character string consisting of one of these code points. But any string longer than one code point containing one of these will not be considered a script run.

"Inherited" is applied to characters that modify another, such as an accent of some type. These are considered to be in the script of the master character, and so never cause a script run to not match.

The other one is "Common". This consists of mostly punctuation, emoji, characters used in mathematics and music, the ASCII digits `0` through `9`, and full-width forms of these digits. These characters can appear intermixed in text in many of the world's scripts. These also don't cause a script run to not match. But like other scripts, all digits in a run must come from the same set of 10.

This construct is non-capturing. You can add parentheses to *pattern* to capture, if desired. You will have to do this if you plan to use "(*ACCEPT) (*ACCEPT:arg)" and not have it bypass the script run checking.

The `Script_Extensions` property as modified by UTS 39 (https://unicode.org/reports/tr39/) is used as the basis for this feature.

To summarize,

- All length 0 or length 1 sequences are script runs.
- A longer sequence is a script run if and only if **all** of the following conditions are met:
  1. No code point in the sequence has the `Script_Extension` property of `Unknown`. This currently means that all code points in the sequence have been assigned by Unicode to be characters that aren't private use nor surrogate code points.
  2. All characters in the sequence come from the Common script and/or the Inherited script and/or a single other script. The script of a character is determined by the `Script_Extensions` property as modified by UTS 39 (https://unicode.org/reports/tr39/), as described above.
  3. All decimal digits in the sequence come from the same block of 10 consecutive digits.


## #Special Backtracking Control Verbs

These special patterns are generally of the form `(**VERB*:*arg*)`. Unless otherwise stated the *arg* argument is optional; in some cases, it is mandatory.

Any pattern containing a special backtracking verb that allows an argument has the special behaviour that when executed it sets the current package's `$REGERROR` and `$REGMARK` variables. When doing so the following rules apply:

On failure, the `$REGERROR` variable will be set to the *arg* value of the verb pattern, if the verb was involved in the failure of the match. If the *arg* part of the pattern was omitted, then `$REGERROR` will be set to the name of the last `(*MARK:*NAME*)` pattern executed, or to TRUE if there was none. Also, the `$REGMARK` variable will be set to FALSE.

On a successful match, the `$REGERROR` variable will be set to FALSE, and the `$REGMARK` variable will be set to the name of the last `(*MARK:*NAME*)` pattern executed. See the explanation for the `(*MARK:*NAME*)` verb below for more details.

**NOTE:** `$REGERROR` and `$REGMARK` are not magic variables like `$1` and most other regex-related variables. They are not local to a scope, nor readonly, but instead are volatile package variables similar to `$AUTOLOAD`. They are set in the package containing the code that *executed* the regex (rather than the one that compiled it, where those differ). If necessary, you can use `local` to localize changes to these variables to a specific scope before executing a regex.

If a pattern does not contain a special backtracking verb that allows an argument, then `$REGERROR` and `$REGMARK` are not touched at all.

**#Verbs**

**#`(*PRUNE)` `(*PRUNE:*NAME*)`**

This zero-width pattern prunes the backtracking tree at the current point when backtracked into on failure. Consider the pattern `/*A* (*PRUNE) *B*/`, where *A* and *B* are complex patterns. Until the `(*PRUNE)` verb is reached, *A* may backtrack as necessary to match. Once it is reached, matching continues in *B*, which may also backtrack as necessary; however, should B not match, then no further backtracking will take place, and the pattern will fail outright at the current starting position.

The following example counts all the possible matching strings in a pattern (without actually matching any of them).

```
'aaab' =~ /a+b?(?{print "$&\n"; $count++})(*FAIL)/;
print "Count=$count\n";
```

which produces:

```
aaab
aaa
aa
a
aab
aa
a
ab
a
Count=9
```

If we add a `(*PRUNE)` before the count like the following

```
'aaab' =~ /a+b?(*PRUNE)(?{print "$&\n"; $count++})(*FAIL)/;
print "Count=$count\n";
```

we prevent backtracking and find the count of the longest matching string at each matching starting point like so:

```
aaab
aab
ab
Count=3
```

Any number of `(*PRUNE)` assertions may be used in a pattern.

See also `"(?>*pattern*)"` and possessive quantifiers for other ways to control backtracking. In some cases, the use of `(*PRUNE)` can be replaced with a `(?>pattern)` with no functional difference; however, `(*PRUNE)` can be used to handle cases that cannot be expressed using a `(?>pattern)` alone.

**#`(*SKIP)` `(*SKIP:*NAME*)`**

This zero-width pattern is similar to `(*PRUNE)`, except that on failure it also signifies that whatever text that was matched leading up to the `(*SKIP)` pattern being executed cannot be part of *any* match of this pattern. This effectively means that the regex engine "skips" forward to this position on failure and tries to match again, (assuming that there is sufficient room to match).

The name of the `(*SKIP:*NAME*)` pattern has special significance. If a `(*MARK:*NAME*)` was encountered while matching, then it is that position which is used as the "skip point". If no `(*MARK)` of that name was encountered, then the `(*SKIP)` operator has no effect. When used without a name the "skip point" is where the match point was when executing the `(*SKIP)` pattern.

Compare the following to the examples in `(*PRUNE)`; note the string is twice as long:

```
'aaabaaab' =~ /a+b?(*SKIP)(?{print "$&\n"; $count++})(*FAIL)/;
print "Count=$count\n";
```

outputs

```
aaab
aaab
Count=2
```

Once the 'aaab' at the start of the string has matched, and the `(*SKIP)` executed, the next starting point will be where the cursor was when the `(*SKIP)` was executed.

**#`(*MARK:*NAME*)` `(*:*NAME*)`**

This zero-width pattern can be used to mark the point reached in a string when a certain part of the pattern has been successfully matched. This mark may be given a name. A later `(*SKIP)` pattern will then skip forward to that point if backtracked into on failure. Any number of `(*MARK)` patterns are allowed, and the *NAME* portion may be duplicated.

In addition to interacting with the `(*SKIP)` pattern, `(*MARK:*NAME*)` can be used to "label" a pattern branch, so that after matching, the program can determine which branches of the pattern were involved in the match.

When a match is successful, the `$REGMARK` variable will be set to the name of the most recently executed `(*MARK:*NAME*)` that was involved in the match.

This can be used to determine which branch of a pattern was matched without using a separate capture group for each branch, which in turn can result in a performance improvement, as perl cannot optimize `/(?:(x)|(y)|(z))/` as efficiently as something like `/(?:x(*MARK:x)|y(*MARK:y)|z(*MARK:z))/`.

When a match has failed, and unless another verb has been involved in failing the match and has provided its own name to use, the `$REGERROR` variable will be set to the name of the most recently executed `(*MARK:*NAME*)`.

See "(*SKIP)" for more details.

As a shortcut `(*MARK:*NAME*)` can be written `(*:*NAME*)`.

**#`(*THEN)` `(*THEN:*NAME*)`**

This is similar to the "cut group" operator `::` from Raku. Like `(*PRUNE)`, this verb always matches, and when backtracked into on failure, it causes the regex engine to try the next alternation in the innermost enclosing group (capturing or otherwise) that has alternations. The two branches of a `(?(*condition*)*yes-pattern*|*no-pattern*)` do not count as an alternation, as far as `(*THEN)` is concerned.

Its name comes from the observation that this operation combined with the alternation operator (`"|"`) can be used to create what is essentially a pattern-based if/then/else block:

```
( COND (*THEN) FOO | COND2 (*THEN) BAR | COND3 (*THEN) BAZ )
```

Note that if this operator is used and NOT inside of an alternation then it acts exactly like the `(*PRUNE)` operator.

```
/ A (*PRUNE) B /
```

is the same as

```
/ A (*THEN) B /
```

but

```
/ ( A (*THEN) B | C ) /
```

is not the same as

```
/ ( A (*PRUNE) B | C ) /
```

as after matching the *A* but failing on the *B* the `(*THEN)` verb will backtrack and try *C*; but the `(*PRUNE)` verb will simply fail.

**#`(*COMMIT)` `(*COMMIT:*arg*)`**

This is the Raku "commit pattern" `<commit>` or `:::`. It's a zero-width pattern similar to `(*SKIP)`, except that when backtracked into on failure it causes the match to fail outright. No further attempts to find a valid match by advancing the start pointer will occur again. For example,

```
'aaabaaab' =~ /a+b?(*COMMIT)(?{print "$&\n"; $count++})(*FAIL)/;
print "Count=$count\n";
```

outputs

```
aaab
Count=1
```

In other words, once the `(*COMMIT)` has been entered, and if the pattern does not match, the regex engine will not try any further matching on the rest of the string.

**#`(*FAIL)` `(*F)` `(*FAIL:*arg*)`**

This pattern matches nothing and always fails. It can be used to force the engine to backtrack. It is equivalent to `(?!)`, but easier to read. In fact, `(?!)` gets optimised into `(*FAIL)` internally. You can provide an argument so that if the match fails because of this `FAIL` directive the argument can be obtained from `$REGERROR`.

It is probably useful only when combined with `(?{})` or `(??{})`.

**#`(*ACCEPT)` `(*ACCEPT:*arg*)`**

This pattern matches nothing and causes the end of successful matching at the point at which the `(*ACCEPT)` pattern was encountered, regardless of whether there is actually more to match in the string. When inside of a nested pattern, such as recursion, or in a subpattern dynamically generated via `(??{})`, only the innermost pattern is ended immediately.

If the `(*ACCEPT)` is inside of capturing groups then the groups are marked as ended at the point at which the `(*ACCEPT)` was encountered. For instance:

```
'AB' =~ /(A (A|B(*ACCEPT)|C) D)(E)/x;
```

will match, and `$1` will be `AB` and `$2` will be `"B"`, `$3` will not be set. If another branch in the inner parentheses was matched, such as in the string 'ACDE', then the `"D"` and `"E"` would have to be matched as well.

You can provide an argument, which will be available in the var `$REGMARK` after the match completes.


## #Warning on `\1` Instead of `$1`

Some people get too used to writing things like:

```
$pattern =~ s/(\W)/\\\1/g;
```

This is grandfathered (for \1 to \9) for the RHS of a substitute to avoid shocking the **sed** addicts, but it's a dirty habit to get into. That's because in PerlThink, the righthand side of an `s///` is a double-quoted string. `\1` in the usual double-quoted string means a control-A. The customary Unix meaning of `\1` is kludged in for `s///`. However, if you get into the habit of doing that, you get yourself into trouble if you then add an `/e` modifier.

```
s/(\d+)/ \1 + 1 /eg;            # causes warning under -w
```

Or if you try to do

```
s/(\d+)/\1000/;
```

You can't disambiguate that by saying `\{1}000`, whereas you can fix it with `${1}000`. The operation of interpolation should not be confused with the operation of matching a backreference. Certainly they mean two different things on the *left* side of the `s///`.


## #Repeated Patterns Matching a Zero-length Substring

**WARNING**: Difficult material (and prose) ahead. This section needs a rewrite.

Regular expressions provide a terse and powerful programming language. As with most other power tools, power comes together with the ability to wreak havoc.

A common abuse of this power stems from the ability to make infinite loops using regular expressions, with something as innocuous as:

```
'foo' =~ m{ ( o? )* }x;
```

The `o?` matches at the beginning of "`foo`", and since the position in the string is not moved by the match, `o?` would match again and again because of the `"*"` quantifier. Another common way to create a similar cycle is with the looping modifier `/g`:

```
@matches = ( 'foo' =~ m{ o? }xg );
```

or

```
print "match: <$&>\n" while 'foo' =~ m{ o? }xg;
```

or the loop implied by `split()`.

However, long experience has shown that many programming tasks may be significantly simplified by using repeated subexpressions that may match zero-length substrings. Here's a simple example being:

```
@chars = split //, $string;           # // is not magic in split
($whitewashed = $string) =~ s/()/ /g; # parens avoid magic s// /
```

Thus Perl allows such constructs, by *forcefully breaking the infinite loop*. The rules for this are different for lower-level loops given by the greedy quantifiers `*+{}`, and for higher-level ones like the `/g` modifier or `split()` operator.

The lower-level loops are *interrupted* (that is, the loop is broken) when Perl detects that a repeated expression matched a zero-length substring. Thus

```
m{ (?: NON_ZERO_LENGTH | ZERO_LENGTH )* }x;
```

is made equivalent to

```
m{ (?: NON_ZERO_LENGTH )* (?: ZERO_LENGTH )? }x;
```

For example, this program

```
#!perl -l
"aaaaab" =~ /
  (?:
     a                 # non-zero
     |                 # or
    (?{print "hello"}) # print hello whenever this
                       #    branch is tried
    (?=(b))            # zero-width assertion
  )*  # any number of times
 /x;
print $&;
print $1;
```

prints

```
hello
aaaaa
b
```

Notice that "hello" is only printed once, as when Perl sees that the sixth iteration of the outermost `(?:)*` matches a zero-length string, it stops the `"*"`.

The higher-level loops preserve an additional state between iterations: whether the last match was zero-length. To break the loop, the following match after a zero-length match is prohibited to have a length of zero. This prohibition interacts with backtracking (see "Backtracking"), and so the *second best* match is chosen if the *best* match is of zero length.

For example:

```
$_ = 'bar';
s/\w??/<$&>/g;
```

results in `<><b><><a><><r><>`. At each position of the string the best match given by non-greedy `??` is the zero-length match, and the *second best* match is what is matched by `\w`. Thus zero-length matches alternate with one-character-long matches.

Similarly, for repeated `m/()/g` the second-best match is the match at the position one notch further in the string.

The additional state of being *matched with zero-length* is associated with the matched string, and is reset by each assignment to `pos()`. Zero-length matches at the end of the previous match are ignored during `split`.


## #Combining RE Pieces

Each of the elementary pieces of regular expressions which were described before (such as `ab` or `\Z`) could match at most one substring at the given position of the input string. However, in a typical regular expression these elementary pieces are combined into more complicated patterns using combining operators `ST`, `S|T`, `S*` *etc*. (in these examples `"S"` and `"T"` are regular subexpressions).

Such combinations can include alternatives, leading to a problem of choice: if we match a regular expression `a|ab` against `"abc"`, will it match substring `"a"` or `"ab"`? One way to describe which substring is actually matched is the concept of backtracking (see "Backtracking"). However, this description is too low-level and makes you think in terms of a particular implementation.

Another description starts with notions of "better"/"worse". All the substrings which may be matched by the given regular expression can be sorted from the "best" match to the "worst" match, and it is the "best" match which is chosen. This substitutes the question of "what is chosen?" by the question of "which matches are better, and which are worse?".

Again, for elementary pieces there is no such question, since at most one match at a given position is possible. This section describes the notion of better/worse for combining operators. In the description below `"S"` and `"T"` are regular subexpressions.

**#`ST`**

Consider two possible matches, `AB` and `A'B'`, `"A"` and `A'` are substrings which can be matched by `"S"`, `"B"` and `B'` are substrings which can be matched by `"T"`.

If `"A"` is a better match for `"S"` than `A'`, `AB` is a better match than `A'B'`.

If `"A"` and `A'` coincide: `AB` is a better match than `AB'` if `"B"` is a better match for `"T"` than `B'`.

**#`S|T`**

When `"S"` can match, it is a better match than when only `"T"` can match.

Ordering of two matches for `"S"` is the same as for `"S"`. Similar for two matches for `"T"`.

**#`S{REPEAT_COUNT}`**

Matches as `SSS...S` (repeated as many times as necessary).

**#`S{min,max}`**

Matches as `S{max}|S{max-1}|...|S{min+1}|S{min}`.

**#`S{min,max}?`**

Matches as `S{min}|S{min+1}|...|S{max-1}|S{max}`.

**#`S?`, `S*`, `S+`**

Same as `S{0,1}`, `S{0,BIG_NUMBER}`, `S{1,BIG_NUMBER}` respectively.

**#`S??`, `S*?`, `S+?`**

Same as `S{0,1}?`, `S{0,BIG_NUMBER}?`, `S{1,BIG_NUMBER}?` respectively.

**#`(?>S)`**

Matches the best match for `"S"` and only that.

**#`(?=S)`, `(?<=S)`**

Only the best match for `"S"` is considered. (This is important only if `"S"` has capturing parentheses, and backreferences are used somewhere else in the whole regular expression.)

**#`(?!S)`, `(?<!S)`**

For this grouping operator there is no need to describe the ordering, since only whether or not `"S"` can match is important.

**#`(??{ *EXPR* })`, `(?*PARNO*)`**

The ordering is the same as for the regular expression which is the result of *EXPR*, or the pattern contained by capture group *PARNO*.

**#`(?(*condition*)*yes-pattern*|*no-pattern*)`**

Recall that which of *yes-pattern* or *no-pattern* actually matches is already determined. The ordering of the matches is the same as for the chosen subexpression.

The above recipes describe the ordering of matches *at a given position*. One more rule is needed to understand how a match is determined for the whole regular expression: a match at an earlier position is always better than a match at a later position.


## #Creating Custom RE Engines

As of Perl 5.10.0, one can create custom regular expression engines. This is not for the faint of heart, as they have to plug in at the C level. See perlreapi for more details.

As an alternative, overloaded constants (see overload) provide a simple way to extend the functionality of the RE engine, by substituting one pattern for another.

Suppose that we want to enable a new RE escape-sequence `\Y|` which matches at a boundary between whitespace characters and non-whitespace characters. Note that `(?=\S)(?<!\S)|(?!\S)(?<=\S)` matches exactly at these positions, so we want to have each `\Y|` in the place of the more complicated version. We can create a module `customre` to do this:

```
package customre;
use overload;

sub import {
  shift;
  die "No argument to customre::import allowed" if @_;
  overload::constant 'qr' => \&convert;
}

sub invalid { die "/$_[0]/: invalid escape '\\$_[1]'"}

# We must also take care of not escaping the legitimate \\Y|
# sequence, hence the presence of '\\' in the conversion rules.
my %rules = ( '\\' => '\\\\',
              'Y|' => qr/(?=\S)(?<!\S)|(?!\S)(?<=\S)/ );
sub convert {
  my $re = shift;
  $re =~ s{
            \\ ( \\ | Y . )
          }
          { $rules{$1} or invalid($re,$1) }sgex;
  return $re;
}
```

Now `use customre` enables the new escape in constant regular expressions, *i.e.*, those without any runtime variable interpolations. As documented in overload, this conversion will work only over literal parts of regular expressions. For `\Y|$re\Y|` the variable part of this regular expression needs to be converted explicitly (but only if the special meaning of `\Y|` should be enabled inside `$re`):

```
use customre;
$re = <>;
chomp $re;
$re = customre::convert $re;
/\Y|$re\Y|/;
```


## #Embedded Code Execution Frequency

The exact rules for how often `(?{})` and `(??{})` are executed in a pattern are unspecified, and this is even more true of `(*{})`. In the case of a successful match you can assume that they DWIM and will be executed in left to right order the appropriate number of times in the accepting path of the pattern as would any other meta-pattern. How non- accepting pathways and match failures affect the number of times a pattern is executed is specifically unspecified and may vary depending on what optimizations can be applied to the pattern and is likely to change from version to version.

For instance in

```
"aaabcdeeeee"=~/a(?{print "a"})b(?{print "b"})cde/;
```

the exact number of times "a" or "b" are printed out is unspecified for failure, but you may assume they will be printed at least once during a successful match, additionally you may assume that if "b" is printed, it will be preceded by at least one "a".

In the case of branching constructs like the following:

```
/a(b|(?{ print "a" }))c(?{ print "c" })/;
```

you can assume that the input "ac" will output "ac", and that "abc" will output only "c".

When embedded code is quantified, successful matches will call the code once for each matched iteration of the quantifier. For example:

```
"good" =~ /g(?:o(?{print "o"}))*d/;
```

will output "o" twice.

For historical and consistency reasons the use of normal code blocks anywhere in a pattern will disable certain optimisations. As of 5.37.7 you can use an "optimistic" codeblock, `(*{ ... })` as a replacement for `(?{ ... })`, if you do *not* wish to disable these optimisations. This may result in the code block being called less often than it might have been had they not been optimistic.


## #PCRE/Python Support

As of Perl 5.10.0, Perl supports several Python/PCRE-specific extensions to the regex syntax. While Perl programmers are encouraged to use the Perl-specific syntax, the following are also accepted:

**#`(?P<*NAME*>*pattern*)`**

Define a named capture group. Equivalent to `(?<*NAME*>*pattern*)`.

**#`(?P=*NAME*)`**

Backreference to a named capture group. Equivalent to `\g{*NAME*}`.

**#`(?P>*NAME*)`**

Subroutine call to a named capture group. Equivalent to `(?&*NAME*)`.


## #Quoting metacharacters

This section has been replaced by "Quoting (escaping) metacharacters".

# #BUGS

There are a number of issues with regard to case-insensitive matching in Unicode rules. See `"i"` under "Modifiers" above.

This document varies from difficult to understand to completely and utterly opaque. The wandering prose riddled with jargon is hard to fathom in several places.

This document needs a rewrite that separates the tutorial content from the reference content.

# #SEE ALSO

The syntax of patterns used in Perl pattern matching evolved from those supplied in the Bell Labs Research Unix 8th Edition (Version 8) regex routines. (The code is actually derived (distantly) from Henry Spencer's freely redistributable reimplementation of those V8 routines.)

perlrequick.

perlretut.

"Regexp Quote-Like Operators" in perlop.

"Gory details of parsing quoted constructs" in perlop.

perlfaq6.

"pos" in perlfunc.

perllocale.

perlebcdic.

*Mastering Regular Expressions* by Jeffrey Friedl, published by O'Reilly and Associates.
