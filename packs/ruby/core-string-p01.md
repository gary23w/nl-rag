---
title: "class String (part 1/4)"
source: https://ruby-doc.org/core/String.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/4
---

# class String

A `String` object has an arbitrary sequence of bytes, typically representing text or binary data. A `String` object may be created using `String::new` or as literals.

`String` objects differ from `Symbol` objects in that `Symbol` objects are designed to be used as identifiers, instead of text or data.

You can create a `String` object explicitly with:

- A string literal.
- A heredoc literal.

You can convert certain objects to Strings with:

- Method `String`.

Some `String` methods modify `self`. Typically, a method whose name ends with `!` modifies `self` and returns `self`; often, a similarly named method (without the `!`) returns a new string.

In general, if both bang and non-bang versions of a method exist, the bang method mutates and the non-bang method does not. However, a method without a bang can also mutate, such as `String#replace`.


## Substitution Methods¶ ↑

These methods perform substitutions:

- `String#sub`: One substitution (or none); returns a new string.
- `String#sub!`: One substitution (or none); returns `self` if any changes, `nil` otherwise.
- `String#gsub`: Zero or more substitutions; returns a new string.
- `String#gsub!`: Zero or more substitutions; returns `self` if any changes, `nil` otherwise.

Each of these methods takes:

- A first argument, `pattern` (`String` or `Regexp`), that specifies the substring(s) to be replaced.
- Either of the following:
  - A second argument, `replacement` (`String` or `Hash`), that determines the replacing string.
  - A block that will determine the replacing string.

The examples in this section mostly use the `String#sub` and `String#gsub` methods; the principles illustrated apply to all four substitution methods.

**Argument `pattern`**

Argument `pattern` is commonly a regular expression:

```
s = 'hello'
s.sub(/[aeiou]/, '*') 
s.gsub(/[aeiou]/, '*') 
s.gsub(/[aeiou]/, '')  
s.sub(/ell/, 'al')     
s.gsub(/xyzzy/, '*')   
'THX1138'.gsub(/\d+/, '00') 
```

When `pattern` is a string, all its characters are treated as ordinary characters (not as `Regexp` special characters):

```
'THX1138'.gsub('\d+', '00') 
```

**`String` `replacement`**

If `replacement` is a string, that string determines the replacing string that is substituted for the matched text.

Each of the examples above uses a simple string as the replacing string.

`String` `replacement` may contain back-references to the pattern’s captures:

- `\n` (*n* is a non-negative integer) refers to `$n`.
- `\k<name>` refers to the named capture `name`.

See `Regexp` for details.

Note that within the string `replacement`, a character combination such as `$&` is treated as ordinary text, not as a special match variable. However, you may refer to some special match variables using these combinations:

- `\&` and `\0` correspond to `$&`, which contains the complete matched text.
- `\'` corresponds to `$'`, which contains the string after the match.
- \` corresponds to $`, which contains the string before the match.
- `\+` corresponds to `$+`, which contains the last capture group.

See `Regexp` for details.

Note that `\\` is interpreted as an escape, i.e., a single backslash.

Note also that a string literal consumes backslashes. See String Literals for details about string literals.

A back-reference is typically preceded by an additional backslash. For example, if you want to write a back-reference `\&` in `replacement` with a double-quoted string literal, you need to write `"..\\&.."`.

If you want to write a non-back-reference string `\&` in `replacement`, you need to first escape the backslash to prevent this method from interpreting it as a back-reference, and then you need to escape the backslashes again to prevent a string literal from consuming them: `"..\\\\&.."`.

You may want to use the block form to avoid excessive backslashes.

**Hash `replacement`**

If the argument `replacement` is a hash, and `pattern` matches one of its keys, the replacing string is the value for that key:

```
h = {'foo' => 'bar', 'baz' => 'bat'}
'food'.sub('foo', h) 
```

Note that a symbol key does not match:

```
h = {foo: 'bar', baz: 'bat'}
'food'.sub('foo', h) 
```

**Block**

In the block form, the current match string is passed to the block; the block’s return value becomes the replacing string:

```
s = '@'
'1234'.gsub(/\d/) { |match| s.succ! } 
```

Special match variables such as `$1`, `$2`, $`, `$&`, and `$'` are set appropriately.


## Whitespace in Strings¶ ↑

In the class `String`, *whitespace* is defined as a contiguous sequence of characters consisting of any mixture of the following:

- NL (null): `"\x00"`, `"\u0000"`.
- HT (horizontal tab): `"\x09"`, `"\t"`.
- LF (line feed): `"\x0a"`, `"\n"`.
- VT (vertical tab): `"\x0b"`, `"\v"`.
- FF (form feed): `"\x0c"`, `"\f"`.
- CR (carriage return): `"\x0d"`, `"\r"`.
- SP (space): `"\x20"`, `" "`.

Whitespace is relevant for the following methods:

- `lstrip`, `lstrip!`: Strip leading whitespace.
- `rstrip`, `rstrip!`: Strip trailing whitespace.
- `strip`, `strip!`: Strip leading and trailing whitespace.


## `String` Slices¶ ↑

A *slice* of a string is a substring selected by certain criteria.

These instance methods utilize slicing:

- `String#[]` (aliased as `String#slice`): Returns a slice copied from `self`.
- `String#[]=`: Mutates `self` with the slice replaced.
- `String#slice!`: Mutates `self` with the slice removed and returns the removed slice.

Each of the above methods takes arguments that determine the slice to be copied or replaced.

The arguments have several forms. For a string `string`, the forms are:

- `string[index]`
- `string[start, length]`
- `string[range]`
- `string[regexp, capture = 0]`
- `string[substring]`

**`string[index]`**

When a non-negative integer argument `index` is given, the slice is the 1-character substring found in `self` at character offset `index`:

```
'bar'[0]      
'bar'[2]      
'bar'[20]     
'тест'[2]     
'こんにちは'[4] 
```

When a negative integer `index` is given, the slice begins at the offset given by counting backward from the end of `self`:

```
'bar'[-3]      
'bar'[-1]      
'bar'[-20]     
```

**`string[start, length]`**

When non-negative integer arguments `start` and `length` are given, the slice begins at character offset `start`, if it exists, and continues for `length` characters, if available:

```
'foo'[0, 2]      
'тест'[1, 2]     
'こんにちは'[2, 2] 

'foo'[2, 0]      

'foo'[1, 200]    

'foo'[4, 2]      
```

Special case: if `start` equals the length of `self`, the slice is a new empty string:

```
'foo'[3, 2]    
'foo'[3, 200]  
```

When a negative `start` and non-negative `length` are given, the slice begins by counting backward from the end of `self`, and continues for `length` characters, if available:

```
'foo'[-2, 2]     
'foo'[-2, 200]   

'foo'[-4, 2]     
```

When a negative `length` is given, there is no slice:

```
'foo'[1, -1]   
'foo'[-2, -1]  
```

**`string[range]`**

When a `Range` argument `range` is given, it creates a substring of `string` using the indices in `range`. The slice is then determined as above:

```
'foo'[0..1]     
'foo'[0, 2]     

'foo'[2...2]    
'foo'[2, 0]     

'foo'[1..200]   
'foo'[1, 200]   

'foo'[4..5]     
'foo'[4, 2]     

'foo'[-4..-3]   
'foo'[-4, 2]    

'foo'[3..4]     
'foo'[3, 2]     

'foo'[-2..-1]   
'foo'[-2, 2]    

'foo'[-2..197]  
'foo'[-2, 200]  
```

**`string[regexp, capture = 0]`**

When the `Regexp` argument `regexp` is given, and the `capture` argument is `0`, the slice is the first matching substring found in `self`:

```
'foo'[/o/]                
'foo'[/x/]                
s = 'hello there'
s[/[aeiou](.)\1/]        
s[/[aeiou](.)\1/, 0]     
```

If the argument `capture` is provided and not `0`, it should be either a capture group index (integer) or a capture group name (`String` or `Symbol`); the slice is the specified capture (see Groups at `Regexp` and Captures):

```
s = 'hello there'
s[/[aeiou](.)\1/, 1] 
s[/(?<vowel>[aeiou])(?<non_vowel>[^aeiou])/, "non_vowel"] 
s[/(?<vowel>[aeiou])(?<non_vowel>[^aeiou])/, :vowel]      
```

If an invalid capture group index is given, there is no slice. If an invalid capture group name is given, `IndexError` is raised.

**`string[substring]`**

When the single `String` argument `substring` is given, it returns the substring from `self` if found, otherwise `nil`:

```
'foo'['oo'] 
'foo'['xx'] 
```
