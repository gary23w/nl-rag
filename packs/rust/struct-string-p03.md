---
title: "String in std::string (part 3/4)"
source: https://doc.rust-lang.org/std/string/struct.String.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 3/4
---

# String in std::string

A more complex pattern, using a closure:

```
let v: Vec<&str> = "abc1defXghi".rsplitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "abc1def"]);
```

1.52.0

·

Source

#### pub fn split_once<P>(&self, delimiter: P) -> Option<(&str, &str)>where P: Pattern,

Splits the string on the first occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### §Examples

```
assert_eq!("cfg".split_once('='), None);
assert_eq!("cfg=".split_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".split_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".split_once('='), Some(("cfg", "foo=bar")));
```

1.52.0

·

Source

#### pub fn rsplit_once<P>(&self, delimiter: P) -> Option<(&str, &str)>where P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Splits the string on the last occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### §Examples

```
assert_eq!("cfg".rsplit_once('='), None);
assert_eq!("cfg=".rsplit_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".rsplit_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".rsplit_once('='), Some(("cfg=foo", "bar")));
```

1.2.0

·

Source

#### pub fn matches<P>(&self, pat: P) -> Matches<'_, P> ⓘwhere P: Pattern,

Returns an iterator over the disjoint matches of a pattern within the given string slice.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator will be a `DoubleEndedIterator` if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., `char`, but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the `rmatches` method can be used.

##### §Examples

```
let v: Vec<&str> = "abcXXXabcYYYabc".matches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".matches(char::is_numeric).collect();
assert_eq!(v, ["1", "2", "3"]);
```

1.2.0

·

Source

#### pub fn rmatches<P>(&self, pat: P) -> RMatches<'_, P> ⓘwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns an iterator over the disjoint matches of a pattern within this string slice, yielded in reverse order.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a `DoubleEndedIterator` if a forward/reverse search yields the same elements.

For iterating from the front, the `matches` method can be used.

##### §Examples

```
let v: Vec<&str> = "abcXXXabcYYYabc".rmatches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".rmatches(char::is_numeric).collect();
assert_eq!(v, ["3", "2", "1"]);
```

1.5.0

·

Source

#### pub fn match_indices<P>(&self, pat: P) -> MatchIndices<'_, P> ⓘwhere P: Pattern,

Returns an iterator over the disjoint matches of a pattern within this string slice as well as the index that the match starts at.

For matches of `pat` within `self` that overlap, only the indices corresponding to the first match are returned.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator will be a `DoubleEndedIterator` if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., `char`, but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the `rmatch_indices` method can be used.

##### §Examples

```
let v: Vec<_> = "abcXXXabcYYYabc".match_indices("abc").collect();
assert_eq!(v, [(0, "abc"), (6, "abc"), (12, "abc")]);

let v: Vec<_> = "1abcabc2".match_indices("abc").collect();
assert_eq!(v, [(1, "abc"), (4, "abc")]);

let v: Vec<_> = "ababa".match_indices("aba").collect();
assert_eq!(v, [(0, "aba")]); 
```

1.5.0

·

Source

#### pub fn rmatch_indices<P>(&self, pat: P) -> RMatchIndices<'_, P> ⓘwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns an iterator over the disjoint matches of a pattern within `self`, yielded in reverse order along with the index of the match.

For matches of `pat` within `self` that overlap, only the indices corresponding to the last match are returned.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a `DoubleEndedIterator` if a forward/reverse search yields the same elements.

For iterating from the front, the `match_indices` method can be used.

##### §Examples

```
let v: Vec<_> = "abcXXXabcYYYabc".rmatch_indices("abc").collect();
assert_eq!(v, [(12, "abc"), (6, "abc"), (0, "abc")]);

let v: Vec<_> = "1abcabc2".rmatch_indices("abc").collect();
assert_eq!(v, [(4, "abc"), (1, "abc")]);

let v: Vec<_> = "ababa".rmatch_indices("aba").collect();
assert_eq!(v, [(2, "aba")]); 
```

1.0.0

·

Source

#### pub fn trim(&self) -> &str

Returns a string slice with leading and trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### §Examples

```
let s = "\n Hello\tworld\t\n";

assert_eq!("Hello\tworld", s.trim());
```

1.30.0

·

Source

#### pub fn trim_start(&self) -> &str

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### §Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### §Examples

Basic usage:

```
let s = "\n Hello\tworld\t\n";
assert_eq!("Hello\tworld\t\n", s.trim_start());
```

Directionality:

```
let s = "  English  ";
assert!(Some('E') == s.trim_start().chars().next());

let s = "  עברית  ";
assert!(Some('ע') == s.trim_start().chars().next());
```

1.30.0

·

Source

#### pub fn trim_end(&self) -> &str

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### §Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### §Examples

Basic usage:

```
let s = "\n Hello\tworld\t\n";
assert_eq!("\n Hello\tworld", s.trim_end());
```

Directionality:

```
let s = "  English  ";
assert!(Some('h') == s.trim_end().chars().rev().next());

let s = "  עברית  ";
assert!(Some('ת') == s.trim_end().chars().rev().next());
```

1.0.0

·

Source

#### pub fn trim_left(&self) -> &str

👎

Deprecated since 1.33.0:

superseded by `trim_start`

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### §Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### §Examples

Basic usage:

```
let s = " Hello\tworld\t";

assert_eq!("Hello\tworld\t", s.trim_left());
```

Directionality:

```
let s = "  English";
assert!(Some('E') == s.trim_left().chars().next());

let s = "  עברית";
assert!(Some('ע') == s.trim_left().chars().next());
```

1.0.0

·

Source

#### pub fn trim_right(&self) -> &str

👎

Deprecated since 1.33.0:

superseded by `trim_end`

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### §Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### §Examples

Basic usage:

```
let s = " Hello\tworld\t";

assert_eq!(" Hello\tworld", s.trim_right());
```

Directionality:

```
let s = "English  ";
assert!(Some('h') == s.trim_right().chars().rev().next());

let s = "עברית  ";
assert!(Some('ת') == s.trim_right().chars().rev().next());
```

1.0.0

·

Source

#### pub fn trim_matches<P>(&self, pat: P) -> &strwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> DoubleEndedSearcher<'a>,

Returns a string slice with all prefixes and suffixes that match a pattern repeatedly removed.

The pattern can be a `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

Simple patterns:

```
assert_eq!("11foo1bar11".trim_matches('1'), "foo1bar");
assert_eq!("123foo1bar123".trim_matches(char::is_numeric), "foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_matches(x), "foo1bar");
```

A more complex pattern, using a closure:

```
assert_eq!("1foo1barXX".trim_matches(|c| c == '1' || c == 'X'), "foo1bar");
```

1.30.0

·

Source

#### pub fn trim_start_matches<P>(&self, pat: P) -> &strwhere P: Pattern,

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### §Examples

```
assert_eq!("11foo1bar11".trim_start_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_start_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_start_matches(x), "foo1bar12");
```

1.45.0

·

Source

#### pub fn strip_prefix<P>(&self, prefix: P) -> Option<&str>where P: Pattern,

Returns a string slice with the prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix, wrapped in `Some`. Unlike `trim_start_matches`, this method removes the prefix exactly once.

If the string does not start with `prefix`, returns `None`.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
assert_eq!("foo:bar".strip_prefix("foo:"), Some("bar"));
assert_eq!("foo:bar".strip_prefix("bar"), None);
assert_eq!("foofoo".strip_prefix("foo"), Some("foo"));
```

1.45.0

·

Source

#### pub fn strip_suffix<P>(&self, suffix: P) -> Option<&str>where P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns a string slice with the suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix, wrapped in `Some`. Unlike `trim_end_matches`, this method removes the suffix exactly once.

If the string does not end with `suffix`, returns `None`.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
assert_eq!("bar:foo".strip_suffix(":foo"), Some("bar"));
assert_eq!("bar:foo".strip_suffix("bar"), None);
assert_eq!("foofoo".strip_suffix("foo"), Some("foo"));
```

Source

#### pub fn strip_circumfix<P, S>(&self, prefix: P, suffix: S) -> Option<&str>where P: Pattern, S: Pattern, <S as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

🔬

This is a nightly-only experimental API. (

strip_circumfix

#147946

)

Returns a string slice with the prefix and suffix removed.

If the string starts with the pattern `prefix` and ends with the pattern `suffix`, returns the substring after the prefix and before the suffix, wrapped in `Some`. Unlike `trim_start_matches` and `trim_end_matches`, this method removes both the prefix and suffix exactly once.

If the string does not start with `prefix` or does not end with `suffix`, returns `None`.

Each pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
#![feature(strip_circumfix)]

assert_eq!("bar:hello:foo".strip_circumfix("bar:", ":foo"), Some("hello"));
assert_eq!("bar:foo".strip_circumfix("foo", "foo"), None);
assert_eq!("foo:bar;".strip_circumfix("foo:", ';'), Some("bar"));
```

Source

#### pub fn trim_prefix<P>(&self, prefix: P) -> &strwhere P: Pattern,

🔬

This is a nightly-only experimental API. (

trim_prefix_suffix

#142312

)

Returns a string slice with the optional prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix. Unlike `strip_prefix`, this method always returns `&str` for easy method chaining, instead of returning `Option<&str>`.

If the string does not start with `prefix`, returns the original string unchanged.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
#![feature(trim_prefix_suffix)]

assert_eq!("foo:bar".trim_prefix("foo:"), "bar");
assert_eq!("foofoo".trim_prefix("foo"), "foo");

assert_eq!("foo:bar".trim_prefix("bar"), "foo:bar");

assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

Source

#### pub fn trim_suffix<P>(&self, suffix: P) -> &strwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

🔬

This is a nightly-only experimental API. (

trim_prefix_suffix

#142312

)

Returns a string slice with the optional suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix. Unlike `strip_suffix`, this method always returns `&str` for easy method chaining, instead of returning `Option<&str>`.

If the string does not end with `suffix`, returns the original string unchanged.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
#![feature(trim_prefix_suffix)]

assert_eq!("bar:foo".trim_suffix(":foo"), "bar");
assert_eq!("foofoo".trim_suffix("foo"), "foo");

assert_eq!("bar:foo".trim_suffix("bar"), "bar:foo");

assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

1.30.0

·

Source

#### pub fn trim_end_matches<P>(&self, pat: P) -> &strwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### §Examples

Simple patterns:

```
assert_eq!("11foo1bar11".trim_end_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_end_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_end_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```
assert_eq!("1fooX".trim_end_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0

·

Source

#### pub fn trim_left_matches<P>(&self, pat: P) -> &strwhere P: Pattern,

👎

Deprecated since 1.33.0:

superseded by `trim_start_matches`

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### §Examples

```
assert_eq!("11foo1bar11".trim_left_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_left_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_left_matches(x), "foo1bar12");
```

1.0.0

·

Source

#### pub fn trim_right_matches<P>(&self, pat: P) -> &strwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

👎

Deprecated since 1.33.0:

superseded by `trim_end_matches`

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### §Examples

Simple patterns:

```
assert_eq!("11foo1bar11".trim_right_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_right_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_right_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```
assert_eq!("1fooX".trim_right_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0

·

Source

#### pub fn parse<F>(&self) -> Result<F, <F as FromStr>::Err>where F: FromStr,

Parses this string slice into another type.

Because `parse` is so general, it can cause problems with type inference. As such, `parse` is one of the few times you’ll see the syntax affectionately known as the ‘turbofish’: `::<>`. This helps the inference algorithm understand specifically which type you’re trying to parse into.

`parse` can parse into any type that implements the `FromStr` trait.

##### §Errors

Will return `Err` if it’s not possible to parse this string slice into the desired type.

##### §Examples

Basic usage:

```
let four: u32 = "4".parse().unwrap();

assert_eq!(4, four);
```

Using the ‘turbofish’ instead of annotating `four`:

```
let four = "4".parse::<u32>();

assert_eq!(Ok(4), four);
```

Failing to parse:

```
let nope = "j".parse::<u32>();

assert!(nope.is_err());
```

1.23.0

·

Source

#### pub fn is_ascii(&self) -> bool

Checks if all characters in this string are within the ASCII range.

An empty string returns `true`.

##### §Examples

```
let ascii = "hello!\n";
let non_ascii = "Grüße, Jürgen ❤";

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

Source

#### pub fn as_ascii(&self) -> Option<&[AsciiChar]>

🔬

This is a nightly-only experimental API. (

ascii_char

#110998

)

If this string slice `is_ascii`, returns it as a slice of ASCII characters, otherwise returns `None`.

Source

#### pub unsafe fn as_ascii_unchecked(&self) -> &[AsciiChar]

🔬

This is a nightly-only experimental API. (

ascii_char

#110998

)

Converts this string slice into a slice of ASCII characters, without checking whether they are valid.

##### §Safety

Every character in this string must be ASCII, or else this is UB.

1.23.0

·

Source

#### pub fn eq_ignore_ascii_case(&self, other: &str) -> bool

Checks that two strings are an ASCII case-insensitive match.

Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`, but without allocating and copying temporaries.

##### §Examples

```
assert!("Ferris".eq_ignore_ascii_case("FERRIS"));
assert!("Ferrös".eq_ignore_ascii_case("FERRöS"));
assert!(!"Ferrös".eq_ignore_ascii_case("FERRÖS"));
```

1.23.0

·

Source

#### pub fn make_ascii_uppercase(&mut self)

Converts this string to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use `to_ascii_uppercase()`.

##### §Examples

```
let mut s = String::from("Grüße, Jürgen ❤");

s.make_ascii_uppercase();

assert_eq!("GRüßE, JüRGEN ❤", s);
```

1.23.0

·

Source

#### pub fn make_ascii_lowercase(&mut self)

Converts this string to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use `to_ascii_lowercase()`.

##### §Examples

```
let mut s = String::from("GRÜßE, JÜRGEN ❤");

s.make_ascii_lowercase();

assert_eq!("grÜße, jÜrgen ❤", s);
```

1.80.0

·

Source

#### pub fn trim_ascii_start(&self) -> &str

Returns a string slice with leading ASCII whitespace removed.

‘Whitespace’ refers to the definition used by `u8::is_ascii_whitespace`.

##### §Examples

```
assert_eq!(" \t \u{3000}hello world\n".trim_ascii_start(), "\u{3000}hello world\n");
assert_eq!("  ".trim_ascii_start(), "");
assert_eq!("".trim_ascii_start(), "");
```

1.80.0

·

Source

#### pub fn trim_ascii_end(&self) -> &str

Returns a string slice with trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by `u8::is_ascii_whitespace`.

##### §Examples

```
assert_eq!("\r hello world\u{3000}\n ".trim_ascii_end(), "\r hello world\u{3000}");
assert_eq!("  ".trim_ascii_end(), "");
assert_eq!("".trim_ascii_end(), "");
```

1.80.0

·

Source

#### pub fn trim_ascii(&self) -> &str

Returns a string slice with leading and trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by `u8::is_ascii_whitespace`.

##### §Examples

```
assert_eq!("\r hello world\n ".trim_ascii(), "hello world");
assert_eq!("  ".trim_ascii(), "");
assert_eq!("".trim_ascii(), "");
```

1.34.0

·

Source

#### pub fn escape_debug(&self) -> EscapeDebug<'_> ⓘ

Returns an iterator that escapes each char in `self` with `char::escape_debug`.

Note: only extended grapheme codepoints that begin the string will be escaped.

##### §Examples

As an iterator:

```
for c in "❤\n!".escape_debug() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```
println!("{}", "❤\n!".escape_debug());
```

Both are equivalent to:

```
println!("❤\\n!");
```

Using `to_string`:

```
assert_eq!("❤\n!".escape_debug().to_string(), "❤\\n!");
```

1.34.0

·

Source

#### pub fn escape_default(&self) -> EscapeDefault<'_> ⓘ

Returns an iterator that escapes each char in `self` with `char::escape_default`.

##### §Examples

As an iterator:

```
for c in "❤\n!".escape_default() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```
println!("{}", "❤\n!".escape_default());
```

Both are equivalent to:

```
println!("\\u{{2764}}\\n!");
```

Using `to_string`:

```
assert_eq!("❤\n!".escape_default().to_string(), "\\u{2764}\\n!");
```

1.34.0

·

Source

#### pub fn escape_unicode(&self) -> EscapeUnicode<'_> ⓘ

Returns an iterator that escapes each char in `self` with `char::escape_unicode`.

##### §Examples

As an iterator:

```
for c in "❤\n!".escape_unicode() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```
println!("{}", "❤\n!".escape_unicode());
```

Both are equivalent to:

```
println!("\\u{{2764}}\\u{{a}}\\u{{21}}");
```

Using `to_string`:

```
assert_eq!("❤\n!".escape_unicode().to_string(), "\\u{2764}\\u{a}\\u{21}");
```

Source

#### pub fn substr_range(&self, substr: &str) -> Option<Range<usize>>

🔬

This is a nightly-only experimental API. (

substr_range

#126769

)

Returns the range that a substring points to.

Returns `None` if `substr` does not point within `self`.

Unlike `str::find`, **this does not search through the string**. Instead, it uses pointer arithmetic to find where in the string `substr` is derived from.

This is useful for extending `str::split` and similar methods.

Note that this method may return false positives (typically either `Some(0..0)` or `Some(self.len()..self.len())`) if `substr` is a zero-length `str` that points at the beginning or end of another, independent, `str`.

##### §Examples

```
#![feature(substr_range)]
use core::range::Range;

let data = "a, b, b, a";
let mut iter = data.split(", ").map(|s| data.substr_range(s).unwrap());

assert_eq!(iter.next(), Some(Range { start: 0, end: 1 }));
assert_eq!(iter.next(), Some(Range { start: 3, end: 4 }));
assert_eq!(iter.next(), Some(Range { start: 6, end: 7 }));
assert_eq!(iter.next(), Some(Range { start: 9, end: 10 }));
```

Source

#### pub fn as_str(&self) -> &str

🔬

This is a nightly-only experimental API. (

str_as_str

#130366

)

Returns the same string as a string slice `&str`.

This method is redundant when used directly on `&str`, but it helps dereferencing other string-like types to string slices, for example references to `Box<str>` or `Arc<str>`.

1.0.0

·

Source

#### pub fn replace<P>(&self, from: P, to: &str) -> Stringwhere P: Pattern,

Replaces all matches of a pattern with another string.

`replace` creates a new `String`, and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice.

##### §Examples

```
let s = "this is old";

assert_eq!("this is new", s.replace("old", "new"));
assert_eq!("than an old", s.replace("is", "an"));
```

When the pattern doesn’t match, it returns this string slice as `String`:

```
let s = "this is old";
assert_eq!(s, s.replace("cookie monster", "little lamb"));
```

1.16.0

·

Source

#### pub fn replacen<P>(&self, pat: P, to: &str, count: usize) -> Stringwhere P: Pattern,

Replaces first N matches of a pattern with another string.

`replacen` creates a new `String`, and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice at most `count` times.

##### §Examples

```
let s = "foo foo 123 foo";
assert_eq!("new new 123 foo", s.replacen("foo", "new", 2));
assert_eq!("faa fao 123 foo", s.replacen('o', "a", 3));
assert_eq!("foo foo new23 foo", s.replacen(char::is_numeric, "new", 1));
```

When the pattern doesn’t match, it returns this string slice as `String`:

```
let s = "this is old";
assert_eq!(s, s.replacen("cookie monster", "little lamb", 10));
```

1.2.0

·

Source

#### pub fn to_lowercase(&self) -> String

Returns the lowercase equivalent of this string slice, as a new `String`.

‘Lowercase’ is defined according to the terms of the Unicode Derived Core Property `Lowercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a `String` instead of modifying the parameter in-place.

##### §Examples

Basic usage:

```
let s = "HELLO";

assert_eq!("hello", s.to_lowercase());
```

A tricky example, with sigma:

```
let sigma = "Σ";

assert_eq!("σ", sigma.to_lowercase());

let odysseus = "ὈΔΥΣΣΕΎΣ";

assert_eq!("ὀδυσσεύς", odysseus.to_lowercase());
```

Languages without case are not changed:

```
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_lowercase());
```

1.2.0

·

Source

#### pub fn to_uppercase(&self) -> String

Returns the uppercase equivalent of this string slice, as a new `String`.

‘Uppercase’ is defined according to the terms of the Unicode Derived Core Property `Uppercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a `String` instead of modifying the parameter in-place.

##### §Examples

Basic usage:

```
let s = "hello";

assert_eq!("HELLO", s.to_uppercase());
```

Scripts without case are not changed:

```
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_uppercase());
```

One character can become multiple:

```
let s = "tschüß";

assert_eq!("TSCHÜSS", s.to_uppercase());
```

1.16.0

·

Source

#### pub fn repeat(&self, n: usize) -> String

Creates a new `String` by repeating a string `n` times.

##### §Panics

This function will panic if the capacity would overflow.

##### §Examples

Basic usage:

```
assert_eq!("abc".repeat(4), String::from("abcabcabcabc"));
```

A panic upon overflow:

ⓘ

```
let huge = "0123456789abcdef".repeat(usize::MAX);
```

1.23.0

·

Source

#### pub fn to_ascii_uppercase(&self) -> String

Returns a copy of this string where each character is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use `make_ascii_uppercase`.

To uppercase ASCII characters in addition to non-ASCII characters, use `to_uppercase`.

##### §Examples

```
let s = "Grüße, Jürgen ❤";

assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
```

1.23.0

·

Source

#### pub fn to_ascii_lowercase(&self) -> String

Returns a copy of this string where each character is mapped to its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use `make_ascii_lowercase`.

To lowercase ASCII characters in addition to non-ASCII characters, use `to_lowercase`.

##### §Examples

```
let s = "Grüße, Jürgen ❤";

assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
```
