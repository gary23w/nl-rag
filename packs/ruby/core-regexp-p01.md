---
title: "class Regexp (part 1/2)"
source: https://ruby-doc.org/core/Regexp.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/2
---

# class Regexp

A regular expression (also called a *regexp*) is a *match pattern* (also simply called a *pattern*).

A common notation for a regexp uses enclosing slash characters:

```
/foo/
```

A regexp may be applied to a *target string*; The part of the string (if any) that matches the pattern is called a *match*, and may be said *to match*:

```
re = /red/
re.match?('redirect') 
re.match?('bored')    
re.match?('credit')   
re.match?('foo')      
```


## Regexp Uses¶ ↑

A regexp may be used:

- To extract substrings based on a given pattern: See sections Method match and Operator =~.
  ```
re = /foo/              
re.match('food')        
re.match('good')        
  ```
- To determine whether a string matches a given pattern: See section Method match?.
  ```
re.match?('food') 
re.match?('good') 
  ```
- As an argument for calls to certain methods in other classes and modules; most such methods accept an argument that may be either a string or the (much more powerful) regexp. See Regexp Methods.


## Regexp Objects¶ ↑

A regexp object has:

- A source; see Sources.
- Several modes; see Modes.
- A timeout; see Timeouts.
- An encoding; see Encodings.


## Creating a Regexp¶ ↑

A regular expression may be created with:

- A regexp literal using slash characters (see Regexp Literals):
  ```
/foo/ 
  ```
- A `%r` regexp literal (see %r: Regexp Literals):
  ```
%r/name\/value pair/ 
%r:name/value pair:  
%r|name/value pair|  

%r[foo] 
%r{foo} 
%r(foo) 
%r<foo> 
  ```
- Method `Regexp.new`.


## Method `match`¶ ↑

Each of the methods `Regexp#match`, `String#match`, and `Symbol#match` returns a `MatchData` object if a match was found, `nil` otherwise; each also sets global variables:

```
'food'.match(/foo/) 
'food'.match(/bar/) 
```


## Operator `=~`¶ ↑

Each of the operators Regexp#=~, String#=~, and Symbol#=~ returns an integer offset if a match was found, `nil` otherwise; each also sets global variables:

```
/bar/ =~ 'foo bar' 
'foo bar' =~ /bar/ 
/baz/ =~ 'foo bar' 
```


## Method `match?`¶ ↑

Each of the methods `Regexp#match?`, `String#match?`, and `Symbol#match?` returns `true` if a match was found, `false` otherwise; none sets global variables:

```
'food'.match?(/foo/) 
'food'.match?(/bar/) 
```


## Global Variables¶ ↑

Certain regexp-oriented methods assign values to global variables:

- `#match`: see Method match.
- `#=~`: see Operator =~.

The affected global variables are:

- `$~`: Returns a `MatchData` object, or `nil`.
- `$&`: Returns the matched part of the string, or `nil`.
- $`: Returns the part of the string to the left of the match, or `nil`.
- `$'`: Returns the part of the string to the right of the match, or `nil`.
- `$+`: Returns the last group matched, or `nil`.
- `$1`, `$2`, etc.: Returns the first, second, etc., matched group, or `nil`. Note that `$0` is quite different; it returns the name of the currently executing program.

Examples:

```
'foo bar bar baz'.match('bar')
$~ 
$& 
$` 
$' 
$+ 
$1 

/s(\w{2}).*(c)/.match('haystack')
$~ 
$& 
$` 
$' 
$+ 
$1 
$2 
$3 

'foo'.match('bar')
$~ 
$& 
$` 
$' 
$+ 
$1 
```

Note that `Regexp#match?`, `String#match?`, and `Symbol#match?` do not set global variables.


## Sources¶ ↑

As seen above, the simplest regexp uses a literal expression as its source:

```
re = /foo/              
re.match('food')        
re.match('good')        
```

A rich collection of available *subexpressions* gives the regexp great power and flexibility:

- Special characters
- Source literals
- Character classes
- Shorthand character classes
- Anchors
- Alternation
- Quantifiers
- Groups and captures
- Unicode
- POSIX Bracket Expressions
- Comments

### Special Characters¶ ↑

Regexp special characters, called *metacharacters*, have special meanings in certain contexts; depending on the context, these are sometimes metacharacters:

```
. ? - + * ^ \ | $ ( ) [ ] { }
```

To match a metacharacter literally, backslash-escape it:

```
/o+/.match('foo')  

/o\+/.match('foo') 
```

To match a backslash literally, backslash-escape it:

```
/\./.match('\.')  
/\\./.match('\.') 
```

`Method` `Regexp.escape` returns an escaped string:

```
Regexp.escape('.?-+*^\|$()[]{}')
```

### Source Literals¶ ↑

The source literal largely behaves like a double-quoted string; see Double-Quoted String Literals.

In particular, a source literal may contain interpolated expressions:

```
s = 'foo'         
/#{s}/            
/#{s.capitalize}/ 
/#{2 + 2}/        
```

There are differences between an ordinary string literal and a source literal; see Shorthand Character Classes.

- `\s` in an ordinary string literal is equivalent to a space character; in a source literal, it’s shorthand for matching a whitespace character.
- In an ordinary string literal, these are (needlessly) escaped characters; in a source literal, they are shorthands for various matching characters:
  ```
\w \W \d \D \h \H \S \R
  ```

### Character Classes¶ ↑

A *character class* is delimited by square brackets; it specifies that certain characters match at a given point in the target string:

```
re = /B[aeiou]rd/
re.match('Bird') 
re.match('Bard') 
re.match('Byrd') 
```

A character class may contain hyphen characters to specify ranges of characters:

```
/[abcdef]/.match('foo') 
/[a-f]/.match('foo')    
/[a-cd-f]/.match('foo') 
```

When the first character of a character class is a caret (`^`), the sense of the class is inverted: it matches any character *except* those specified.

```
/[^a-eg-z]/.match('f') 
```

A character class may contain another character class. By itself this isn’t useful because `[a-z[0-9]]` describes the same set as `[a-z0-9]`.

However, character classes also support the `&&` operator, which performs set intersection on its arguments. The two can be combined as follows:

```
/[a-w&&[^c-g]z]/ 
```

This is equivalent to:

```
/[abh-w]/
```

### Shorthand Character Classes¶ ↑

Each of the following metacharacters serves as a shorthand for a character class:

- `/./`: Matches any character except a newline:
  ```
/./.match('foo') 
/./.match("\n")  
  ```
- `/./m`: Matches any character, including a newline; see Multiline Mode:
  ```
/./m.match("\n") 
  ```
- `/\w/`: Matches a word character: equivalent to `[a-zA-Z0-9_]`:
  ```
/\w/.match(' foo') 
/\w/.match(' _')   
/\w/.match(' ')    
  ```
- `/\W/`: Matches a non-word character: equivalent to `[^a-zA-Z0-9_]`:
  ```
/\W/.match(' ') 
/\W/.match('_') 
  ```
- `/\d/`: Matches a digit character: equivalent to `[0-9]`:
  ```
/\d/.match('THX1138') 
/\d/.match('foo')     
  ```
- `/\D/`: Matches a non-digit character: equivalent to `[^0-9]`:
  ```
/\D/.match('123Jump!') 
/\D/.match('123')      
  ```
- `/\h/`: Matches a hexdigit character: equivalent to `[0-9a-fA-F]`:
  ```
/\h/.match('xyz fedcba9876543210') 
/\h/.match('xyz')                  
  ```
- `/\H/`: Matches a non-hexdigit character: equivalent to `[^0-9a-fA-F]`:
  ```
/\H/.match('fedcba9876543210xyz') 
/\H/.match('fedcba9876543210')    
  ```
- `/\s/`: Matches a whitespace character: equivalent to `/[ \t\r\n\f\v]/`:
  ```
/\s/.match('foo bar') 
/\s/.match('foo')     
  ```
- `/\S/`: Matches a non-whitespace character: equivalent to `/[^ \t\r\n\f\v]/`:
  ```
/\S/.match(" \t\r\n\f\v foo") 
/\S/.match(" \t\r\n\f\v")     
  ```
- `/\R/`: Matches a linebreak, platform-independently:
  ```
/\R/.match("\r")     
/\R/.match("\n")     
/\R/.match("\f")     
/\R/.match("\v")     
/\R/.match("\r\n")   
/\R/.match("\u0085") 
/\R/.match("\u2028") 
/\R/.match("\u2029") 
  ```

### Anchors¶ ↑

An anchor is a metasequence that matches a zero-width position between characters in the target string.

For a subexpression with no anchor, matching may begin anywhere in the target string:

```
/real/.match('surrealist') 
```

For a subexpression with an anchor, matching must begin at the matched anchor.

#### Boundary Anchors¶ ↑

Each of these anchors matches a boundary:

- `^`: Matches the beginning of a line:
  ```
/^bar/.match("foo\nbar") 
/^ar/.match("foo\nbar")  
  ```
- `$`: Matches the end of a line:
  ```
/bar$/.match("foo\nbar") 
/ba$/.match("foo\nbar")  
  ```
- `\A`: Matches the beginning of the string:
  ```
/\Afoo/.match('foo bar')  
/\Afoo/.match(' foo bar') 
  ```
- `\Z`: Matches the end of the string; if string ends with a single newline, it matches just before the ending newline:
  ```
/foo\Z/.match('bar foo')     
/foo\Z/.match('foo bar')     
/foo\Z/.match("bar foo\n")   
/foo\Z/.match("bar foo\n\n") 
  ```
- `\z`: Matches the end of the string:
  ```
/foo\z/.match('bar foo')   
/foo\z/.match('foo bar')   
/foo\z/.match("bar foo\n") 
  ```
- `\b`: Matches word boundary when not inside brackets; matches backspace (`"0x08"`) when inside brackets:
  ```
/foo\b/.match('foo bar') 
/foo\b/.match('foobar')  
  ```
- `\B`: Matches non-word boundary:
  ```
/foo\B/.match('foobar')  
/foo\B/.match('foo bar') 
  ```
- `\G`: Matches first matching position: In methods like `String#gsub` and `String#scan`, it changes on each iteration. It initially matches the beginning of subject, and in each following iteration it matches where the last match finished. In methods like `Regexp#match` and `String#match` that take an optional offset, it matches where the search begins.
  ```
"    a b c".gsub(/ /, '_')   
"    a b c".gsub(/\G /, '_') 
  ```
  ```
"hello, world".match(/,/, 3)   
"hello, world".match(/\G,/, 3) 
  ```

#### Lookaround Anchors¶ ↑

Lookahead anchors:

- `(?=*pat*)`: Positive lookahead assertion: ensures that the following characters match *pat*, but doesn’t include those characters in the matched substring.
- `(?!*pat*)`: Negative lookahead assertion: ensures that the following characters *do not* match *pat*, but doesn’t include those characters in the matched substring.

Lookbehind anchors:

- `(?<=*pat*)`: Positive lookbehind assertion: ensures that the preceding characters match *pat*, but doesn’t include those characters in the matched substring.
- `(?<!*pat*)`: Negative lookbehind assertion: ensures that the preceding characters do not match *pat*, but doesn’t include those characters in the matched substring.

The pattern below uses positive lookahead and positive lookbehind to match text appearing in **…** tags without including the tags in the match:

```
/(?<=<b>)\w+(?=<\/b>)/.match("Fortune favors the <b>bold</b>.")
```

#### Match-Reset Anchor¶ ↑

- `\K`: Match reset: the matched content preceding `\K` in the regexp is excluded from the result. For example, the following two regexps are almost equivalent: These match same string and `$&` equals `'c'`, while the matched position is different. As are the following two regexps:
  ```
/ab\Kc/.match('abc')    
/(?<=ab)c/.match('abc') 
  ```
  ```
/(a)\K(b)\Kc/
/(?<=(?<=(a))(b))c/
  ```

### Alternation¶ ↑

The vertical bar metacharacter (`|`) may be used within parentheses to express alternation: two or more subexpressions any of which may match the target string.

Two alternatives:

```
re = /(a|b)/
re.match('foo') 
re.match('bar') 
```

Four alternatives:

```
re = /(a|b|c|d)/
re.match('shazam') 
re.match('cold')   
```

Each alternative is a subexpression, and may be composed of other subexpressions:

```
re = /([a-c]|[x-z])/
re.match('bar') 
re.match('ooz') 
```

Method `Regexp.union` provides a convenient way to construct a regexp with alternatives.

### Quantifiers¶ ↑

A simple regexp matches one character:

```
/\w/.match('Hello')  
```

An added *quantifier* specifies how many matches are required or allowed:

- `*` - Matches zero or more times:
  ```
/\w*/.match('')

/\w*/.match('x')

/\w*/.match('xyz')
  ```
- `+` - Matches one or more times:
  ```
/\w+/.match('')    
/\w+/.match('x')   
/\w+/.match('xyz') 
  ```
- `?` - Matches zero or one times:
  ```
/\w?/.match('')    
/\w?/.match('x')   
/\w?/.match('xyz') 
  ```
- `{`*n*`}` - Matches exactly *n* times:
  ```
/\w{2}/.match('')    
/\w{2}/.match('x')   
/\w{2}/.match('xyz') 
  ```
- `{`*min*`,}` - Matches *min* or more times:
  ```
/\w{2,}/.match('')    
/\w{2,}/.match('x')   
/\w{2,}/.match('xy')  
/\w{2,}/.match('xyz') 
  ```
- `{,`*max*`}` - Matches *max* or fewer times:
  ```
/\w{,2}/.match('')    
/\w{,2}/.match('x')   
/\w{,2}/.match('xyz') 
  ```
- `{`*min*`,`*max*`}` - Matches at least *min* times and at most *max* times:
  ```
/\w{1,2}/.match('')    
/\w{1,2}/.match('x')   
/\w{1,2}/.match('xyz') 
  ```

#### Greedy, Lazy, or Possessive Matching¶ ↑

Quantifier matching may be greedy, lazy, or possessive:

- In *greedy* matching, as many occurrences as possible are matched while still allowing the overall match to succeed. Greedy quantifiers: `*`, `+`, `?`, `{min, max}` and its variants.
- In *lazy* matching, the minimum number of occurrences are matched. Lazy quantifiers: `*?`, `+?`, `??`, `{min, max}?` and its variants.
- In *possessive* matching, once a match is found, there is no backtracking; that match is retained, even if it jeopardises the overall match. Possessive quantifiers: `*+`, `++`, `?+`. Note that `{min, max}` and its variants do *not* support possessive matching.

More:

- About greedy and lazy matching, see Choosing Minimal or Maximal Repetition.
- About possessive matching, see Eliminate Needless Backtracking.

### Groups and Captures¶ ↑

A simple regexp has (at most) one match:

```
re = /\d\d\d\d-\d\d-\d\d/
re.match('1943-02-04')      
re.match('1943-02-04').size 
re.match('foo')             
```

Adding one or more pairs of parentheses, `(*subexpression*)`, defines *groups*, which may result in multiple matched substrings, called *captures*:

```
re = /(\d\d\d\d)-(\d\d)-(\d\d)/
re.match('1943-02-04')      
re.match('1943-02-04').size 
```

The first capture is the entire matched string; the other captures are the matched substrings from the groups.

A group may have a quantifier:

```
re = /July 4(th)?/
re.match('July 4')   
re.match('July 4th') 

re = /(foo)*/
re.match('')       
re.match('foo')    
re.match('foofoo') 

re = /(foo)+/
re.match('')       
re.match('foo')    
re.match('foofoo') 
```

The returned MatchData object gives access to the matched substrings:

```
re = /(\d\d\d\d)-(\d\d)-(\d\d)/
md = re.match('1943-02-04')

md[0] 
md[1] 
md[2] 
md[3] 
```

#### Non-Capturing Groups¶ ↑

A group may be made non-capturing; it is still a group (and, for example, can have a quantifier), but its matching substring is not included among the captures.

A non-capturing group begins with `?:` (inside the parentheses):

```
re = /(?:\d\d\d\d)-(\d\d)-(\d\d)/
md = re.match('1943-02-04') 
```

#### Backreferences¶ ↑

A group match may also be referenced within the regexp itself; such a reference is called a `backreference`:

```
/[csh](..) [csh]\1 in/.match('The cat sat in the hat')
```

This table shows how each subexpression in the regexp above matches a substring in the target string:

```
| Subexpression in Regexp   | Matching Substring in Target String |
|---------------------------|-------------------------------------|
|       First '[csh]'       |            Character 'c'            |
|          '(..)'           |        First substring 'at'         |
|      First space ' '      |      First space character ' '      |
|       Second '[csh]'      |            Character 's'            |
| '\1' (backreference 'at') |        Second substring 'at'        |
|           ' in'           |            Substring ' in'          |
```

A regexp may contain any number of groups:

- For a large number of groups:
  - The ordinary `\*n*` notation applies only for *n* in range (1..9).
  - The `MatchData[*n*]` notation applies for any non-negative *n*.
- `\0` is a special backreference, referring to the entire matched string; it may not be used within the regexp itself, but may be used outside it (for example, in a substitution method call):
  ```
'The cat sat in the hat'.gsub(/[csh]at/, '\0s')
  ```

#### Named Captures¶ ↑

As seen above, a capture can be referred to by its number. A capture can also have a name, prefixed as `?<*name*>` or `?'*name*'`, and the name (symbolized) may be used as an index in `MatchData[]`:

```
md = /\$(?<dollars>\d+)\.(?'cents'\d+)/.match("$3.67")

md[:dollars]  
md[:cents]    

md[2]         
```

When a regexp contains a named capture, there are no unnamed captures:

```
/\$(?<dollars>\d+)\.(\d+)/.match("$3.67")
```

A named group may be backreferenced as `\k<*name*>`:

```
/(?<vowel>[aeiou]).\k<vowel>.\k<vowel>/.match('ototomy')
```

When (and only when) a regexp contains named capture groups and appears before the `=~` operator, the captured substrings are assigned to local variables with corresponding names:

```
/\$(?<dollars>\d+)\.(?<cents>\d+)/ =~ '$3.67'
dollars 
cents   
```

Method `Regexp#named_captures` returns a hash of the capture names and substrings; method `Regexp#names` returns an array of the capture names.

#### Atomic Grouping¶ ↑

A group may be made *atomic* with `(?>`*subexpression*`)`.

This causes the subexpression to be matched independently of the rest of the expression, so that the matched substring becomes fixed for the remainder of the match, unless the entire subexpression must be abandoned and subsequently revisited.

In this way *subexpression* is treated as a non-divisible whole. Atomic grouping is typically used to optimise patterns to prevent needless backtracking .

Example (without atomic grouping):

```
/".*"/.match('"Quote"') 
```

Analysis:

1. The leading subexpression `"` in the pattern matches the first character `"` in the target string.
2. The next subexpression `.*` matches the next substring `Quote“` (including the trailing double-quote).
3. Now there is nothing left in the target string to match the trailing subexpression `"` in the pattern; this would cause the overall match to fail.
4. The matched substring is backtracked by one position: `Quote`.
5. The final subexpression `"` now matches the final substring `"`, and the overall match succeeds.

If subexpression `.*` is grouped atomically, the backtracking is disabled, and the overall match fails:

```
/"(?>.*)"/.match('"Quote"') 
```

Atomic grouping can affect performance; see Atomic Group.

#### Subexpression Calls¶ ↑

As seen above, a backreference number (`\*n*`) or name (`\k<*name*>`) gives access to a captured *substring*; the corresponding regexp *subexpression* may also be accessed, via the number (`\g*n*`) or name (`\g<*name*>`):

```
/\A(?<paren>\(\g<paren>*\))*\z/.match('(())')
```

The pattern:

1. Matches at the beginning of the string, i.e. before the first character.
2. Enters a named group `paren`.
3. Matches the first character in the string, `'('`.
4. Calls the `paren` group again, i.e. recurses back to the second step.
5. Re-enters the `paren` group.
6. Matches the second character in the string, `'('`.
7. Attempts to call `paren` a third time, but fails because doing so would prevent an overall successful match.
8. Matches the third character in the string, `')'`; marks the end of the second recursive call
9. Matches the fourth character in the string, `')'`.
10. Matches the end of the string.

See Subexpression calls.

#### Conditionals¶ ↑

The conditional construct takes the form `(?(*cond*)*yes*|*no*)`, where:

- *cond* may be a capture number or name.
- The match to be applied is *yes* if *cond* is captured; otherwise the match to be applied is *no*.
- If not needed, `|*no*` may be omitted.

Examples:

```
re = /\A(foo)?(?(1)(T)|(F))\z/
re.match('fooT') 
re.match('F')    
re.match('fooF') 
re.match('T')    

re = /\A(?<xyzzy>foo)?(?(<xyzzy>)(T)|(F))\z/
re.match('fooT') 
re.match('F')    
re.match('fooF') 
re.match('T')    
```

#### Absence Operator¶ ↑

The absence operator is a special group that matches anything which does *not* match the contained subexpressions.

```
/(?~real)/.match('surrealist') 
/(?~real)ist/.match('surrealist') 
/sur(?~real)ist/.match('surrealist') 
```

### Unicode¶ ↑

#### Unicode Properties¶ ↑

The `/\p{*property_name*}/` construct (with lowercase `p`) matches characters using a Unicode property name, much like a character class; property `Alpha` specifies alphabetic characters:

```
/\p{Alpha}/.match('a') 
/\p{Alpha}/.match('1') 
```

A property can be inverted by prefixing the name with a caret character (`^`):

```
/\p{^Alpha}/.match('1') 
/\p{^Alpha}/.match('a') 
```

Or by using `\P` (uppercase `P`):

```
/\P{Alpha}/.match('1') 
/\P{Alpha}/.match('a') 
```

See Unicode Properties for regexps based on the numerous properties.

Some commonly-used properties correspond to POSIX bracket expressions:

- `/\p{Alnum}/`: Alphabetic and numeric character
- `/\p{Alpha}/`: Alphabetic character
- `/\p{Blank}/`: Space or tab
- `/\p{Cntrl}/`: Control character
- `/\p{Digit}/`: Digit characters, and similar)
- `/\p{Lower}/`: Lowercase alphabetical character
- `/\p{Print}/`: Like `\p{Graph}`, but includes the space character
- `/\p{Punct}/`: Punctuation character
- `/\p{Space}/`: Whitespace character (`[:blank:]`, newline, carriage return, etc.)
- `/\p{Upper}/`: Uppercase alphabetical
- `/\p{XDigit}/`: Digit allowed in a hexadecimal number (i.e., 0-9a-fA-F)

These are also commonly used:

- `/\p{Emoji}/`: Unicode emoji.
- `/\p{Graph}/`: Characters excluding `/\p{Cntrl}/` and `/\p{Space}/`. Note that invisible characters under the Unicode {“Format”}[https://www.compart.com/en/unicode/category/Cf] category are included.
- `/\p{Word}/`: A member in one of these Unicode character categories (see below) or having one of these Unicode properties:
  - Unicode categories:
    - `Mark` (`M`).
    - `Decimal Number` (`Nd`)
    - `Connector Punctuation` (`Pc`).
  - Unicode properties:
    - `Alpha`
    - `Join_Control`
- `/\p{ASCII}/`: A character in the ASCII character set.
- `/\p{Any}/`: Any Unicode character (including unassigned characters).
- `/\p{Assigned}/`: An assigned character.

#### Unicode Character Categories¶ ↑

A Unicode character category name:

- May be either its full name or its abbreviated name.
- Is case-insensitive.
- Treats a space, a hyphen, and an underscore as equivalent.

Examples:

```
/\p{lu}/                
/\p{LU}/                
/\p{Uppercase Letter}/  
/\p{Uppercase_Letter}/  
/\p{UPPERCASE-LETTER}/  
```

Below are the Unicode character category abbreviations and names. Enumerations of characters in each category are at the links.

Letters:

- `L`, `Letter`: `LC`, `Lm`, or `Lo`.
- `LC`, `Cased_Letter`: `Ll`, `Lt`, or `Lu`.
- Lu, Lowercase_Letter.
- Lu, Modifier_Letter.
- Lu, Other_Letter.
- Lu, Titlecase_Letter.
- Lu, Uppercase_Letter.

Marks:

- `M`, `Mark`: `Mc`, `Me`, or `Mn`.
- Mc, Spacing_Mark.
- Me, Enclosing_Mark.
- Mn, Nonapacing_Mark.

Numbers:

- `N`, `Number`: `Nd`, `Nl`, or `No`.
- Nd, Decimal_Number.
- Nl, Letter_Number.
- No, Other_Number.

Punctuation:

- `P`, `Punctuation`: `Pc`, `Pd`, `Pe`, `Pf`, `Pi`, `Po`, or `Ps`.
- Pc, Connector_Punctuation.
- Pd, Dash_Punctuation.
- Pe, Close_Punctuation.
- Pf, Final_Punctuation.
- Pi, Initial_Punctuation.
- Po, Other_Punctuation.
- Ps, Open_Punctuation.
- `S`, `Symbol`: `Sc`, `Sk`, `Sm`, or `So`.
- Sc, Currency_Symbol.
- Sk, Modifier_Symbol.
- Sm, Math_Symbol.
- So, Other_Symbol.
- `Z`, `Separator`: `Zl`, `Zp`, or `Zs`.
- Zl, Line_Separator.
- Zp, Paragraph_Separator.
- Zs, Space_Separator.
- `C`, `Other`: `Cc`, `Cf`, `Cn`, `Co`, or `Cs`.
- Cc, Control.
- Cf, Format.
- Cn, Unassigned.
- Co, Private_Use.
- Cs, Surrogate.

#### Unicode Scripts and Blocks¶ ↑

Among the Unicode properties are:

- Unicode scripts; see supported scripts.
- Unicode blocks; see supported blocks.

### POSIX Bracket Expressions¶ ↑

A POSIX *bracket expression* is also similar to a character class. These expressions provide a portable alternative to the above, with the added benefit of encompassing non-ASCII characters:

- `/\d/` matches only ASCII decimal digits `0` through `9`.
- `/[[:digit:]]/` matches any character in the Unicode `Decimal Number` (`Nd`) category; see below.

The POSIX bracket expressions:

- `/[[:digit:]]/`: Matches a Unicode digit:
  ```
/[[:digit:]]/.match('9')       
/[[:digit:]]/.match("\u1fbf9") 
  ```
- `/[[:xdigit:]]/`: Matches a digit allowed in a hexadecimal number; equivalent to `[0-9a-fA-F]`.
- `/[[:upper:]]/`: Matches a Unicode uppercase letter:
  ```
/[[:upper:]]/.match('A')      
/[[:upper:]]/.match("\u00c6") 
  ```
- `/[[:lower:]]/`: Matches a Unicode lowercase letter:
  ```
/[[:lower:]]/.match('a')      
/[[:lower:]]/.match("\u01fd") 
  ```
- `/[[:alpha:]]/`: Matches `/[[:upper:]]/` or `/[[:lower:]]/`.
- `/[[:alnum:]]/`: Matches `/[[:alpha:]]/` or `/[[:digit:]]/`.
- `/[[:space:]]/`: Matches Unicode space character:
  ```
/[[:space:]]/.match(' ')      
/[[:space:]]/.match("\u2005") 
  ```
- `/[[:blank:]]/`: Matches `/[[:space:]]/` or tab character:
  ```
/[[:blank:]]/.match(' ')      
/[[:blank:]]/.match("\u2005") 
/[[:blank:]]/.match("\t")     
  ```
- `/[[:cntrl:]]/`: Matches Unicode control character:
  ```
/[[:cntrl:]]/.match("\u0000") 
/[[:cntrl:]]/.match("\u009f") 
  ```
- `/[[:graph:]]/`: Matches any character except `/[[:space:]]/` or `/[[:cntrl:]]/`.
- `/[[:print:]]/`: Matches `/[[:graph:]]/` or space character.
- `/[[:punct:]]/`: Matches any (Unicode punctuation character}[www.compart.com/en/unicode/category/Po]:

Ruby also supports these (non-POSIX) bracket expressions:

- `/[[:ascii:]]/`: Matches a character in the ASCII character set.
- `/[[:word:]]/`: Matches a character in one of these Unicode character categories or having one of these Unicode properties:
  - Unicode categories:
    - `Mark` (`M`).
    - `Decimal Number` (`Nd`)
    - `Connector Punctuation` (`Pc`).
  - Unicode properties:
    - `Alpha`
    - `Join_Control`

A comment may be included in a regexp pattern using the `(?#`*comment*`)` construct, where *comment* is a substring that is to be ignored. arbitrary text ignored by the regexp engine:

```
/foo(?#Ignore me)bar/.match('foobar') 
```

The comment may not include an unescaped terminator character.

See also Extended Mode.


## Modes¶ ↑

Each of these modifiers sets a mode for the regexp:

- `i`: `/*pattern*/i` sets Case-Insensitive Mode.
- `m`: `/*pattern*/m` sets Multiline Mode.
- `x`: `/*pattern*/x` sets Extended Mode.
- `o`: `/*pattern*/o` sets Interpolation Mode.

Any, all, or none of these may be applied.

Modifiers `i`, `m`, and `x` may be applied to subexpressions:

- `(?*modifier*)` turns the mode “on” for ensuing subexpressions
- `(?-*modifier*)` turns the mode “off” for ensuing subexpressions
- `(?*modifier*:*subexp*)` turns the mode “on” for *subexp* within the group
- `(?-*modifier*:*subexp*)` turns the mode “off” for *subexp* within the group

Example:

```
re = /(?i)te(?-i)st/
re.match('test') 
re.match('TEst') 
re.match('TEST') 
re.match('teST') 

re = /t(?i:e)st/
re.match('test') 
re.match('tEst') 
re.match('tEST') 
```

Method `Regexp#options` returns an integer whose value showing the settings for case-insensitivity mode, multiline mode, and extended mode.

### Case-Insensitive Mode¶ ↑

By default, a regexp is case-sensitive:

```
/foo/.match('FOO')  
```

Modifier `i` enables case-insensitive mode:

```
/foo/i.match('FOO')
```

Method `Regexp#casefold?` returns whether the mode is case-insensitive.

### Multiline Mode¶ ↑

The multiline-mode in Ruby is what is commonly called a “dot-all mode”:

- Without the `m` modifier, the subexpression `.` does not match newlines:
  ```
/a.c/.match("a\nc")  
  ```
- With the modifier, it does match:
  ```
/a.c/m.match("a\nc") 
  ```

Unlike other languages, the modifier `m` does not affect the anchors `^` and `$`. These anchors always match at line-boundaries in Ruby.

### Extended Mode¶ ↑

Modifier `x` enables extended mode, which means that:

- Literal white space in the pattern is to be ignored.
- Character `#` marks the remainder of its containing line as a comment, which is also to be ignored for matching purposes.

In extended mode, whitespace and comments may be used to form a self-documented regexp.

`Regexp` not in extended mode (matches some Roman numerals):

```
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
re = /#{pattern}/
re.match('MCMXLIII') 
```

`Regexp` in extended mode:

```
pattern = <<-EOT
  ^                   # beginning of string
  M{0,3}              # thousands - 0 to 3 Ms
  (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                      #            or 500-800 (D, followed by 0 to 3 Cs)
  (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                      #        or 50-80 (L, followed by 0 to 3 Xs)
  (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                      #        or 5-8 (V, followed by 0 to 3 Is)
  $                   # end of string
EOT
re = /#{pattern}/x
re.match('MCMXLIII') 
```

### Interpolation Mode¶ ↑

Modifier `o` means that the first time a literal regexp with interpolations is encountered, the generated `Regexp` object is saved and used for all future evaluations of that literal regexp. Without modifier `o`, the generated `Regexp` is not saved, so each evaluation of the literal regexp generates a new `Regexp` object.

Without modifier `o`:

```
def letters; sleep 5; /[A-Z][a-z]/; end
words = %w[abc def xyz]
start = Time.now
words.each {|word| word.match(/\A[#{letters}]+\z/) }
Time.now - start 
```

With modifier `o`:

```
start = Time.now
words.each {|word| word.match(/\A[#{letters}]+\z/o) }
Time.now - start 
```

Note that if the literal regexp does not have interpolations, the `o` behavior is the default.


## Encodings¶ ↑

By default, a regexp with only US-ASCII characters has US-ASCII encoding:

```
re = /foo/
re.source.encoding 
re.encoding        
```

A regular expression containing non-US-ASCII characters is assumed to use the source encoding. This can be overridden with one of the following modifiers.

- `/*pat*/n`: US-ASCII if only containing US-ASCII characters, otherwise ASCII-8BIT:
  ```
/foo/n.encoding     
/foo\xff/n.encoding 
/foo\x7f/n.encoding 
  ```
- `/*pat*/u`: UTF-8
  ```
/foo/u.encoding 
  ```
- `/*pat*/e`: EUC-JP
  ```
/foo/e.encoding 
  ```
- `/*pat*/s`: Windows-31J
  ```
/foo/s.encoding 
  ```

A regexp can be matched against a target string when either:

- They have the same encoding.
- The regexp’s encoding is a fixed encoding and the string contains only ASCII characters. `Method` `Regexp#fixed_encoding?` returns whether the regexp has a *fixed* encoding.

If a match between incompatible encodings is attempted an `Encoding::CompatibilityError` exception is raised.

Example:

```
re = eval("# encoding: ISO-8859-1\n/foo\\xff?/")
re.encoding                 
re =~ "foo".encode("UTF-8") 
re =~ "foo\u0100"           
```

The encoding may be explicitly fixed by including `Regexp::FIXEDENCODING` in the second argument for `Regexp.new`:

```
re = Regexp.new("a".force_encoding('iso-8859-1'), Regexp::FIXEDENCODING)
re.encoding  

s = "a\u3042"
s.encoding   
re.match(s)  
```


## Timeouts¶ ↑

When either a regexp source or a target string comes from untrusted input, malicious values could become a denial-of-service attack; to prevent such an attack, it is wise to set a timeout.

Regexp has two timeout values:

- A class default timeout, used for a regexp whose instance timeout is `nil`; this default is initially `nil`, and may be set by method `Regexp.timeout=`:
  ```
Regexp.timeout 
Regexp.timeout = 3.0
Regexp.timeout 
  ```
- An instance timeout, which defaults to `nil` and may be set in `Regexp.new`:
  ```
re = Regexp.new('foo', timeout: 5.0)
re.timeout 
  ```

When regexp.timeout is `nil`, the timeout “falls through” to `Regexp.timeout`; when regexp.timeout is non-`nil`, that value controls timing out:

```
| regexp.timeout Value | Regexp.timeout Value |            Result           |
|----------------------|----------------------|-----------------------------|
|         nil          |          nil         |       Never times out.      |
|         nil          |         Float        | Times out in Float seconds. |
|        Float         |          Any         | Times out in Float seconds. |
```


## Optimization¶ ↑

For certain values of the pattern and target string, matching time can grow polynomially or exponentially in relation to the input size; the potential vulnerability arising from this is the regular expression denial-of-service (ReDoS) attack.

Regexp matching can apply an optimization to prevent ReDoS attacks. When the optimization is applied, matching time increases linearly (not polynomially or exponentially) in relation to the input size, and a ReDoS attach is not possible.

This optimization is applied if the pattern meets these criteria:

- No backreferences.
- No subexpression calls.
- No nested lookaround anchors or atomic groups.
- No nested quantifiers with counting (i.e. no nested `{n}`, `{min,}`, `{,max}`, or `{min,max}` style quantifiers)

You can use method `Regexp.linear_time?` to determine whether a pattern meets these criteria:

```
Regexp.linear_time?(/a*/)     
Regexp.linear_time?('a*')     
Regexp.linear_time?(/(a*)\1/) 
```

However, an untrusted source may not be safe even if the method returns `true`, because the optimization uses memoization (which may invoke large memory consumption).
