---
title: "String in std::string (part 2/4)"
source: https://doc.rust-lang.org/std/string/struct.String.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 2/4
---

## Methods from Deref<Target = str>

1.0.0

·

Source

#### pub fn len(&self) -> usize

Returns the length of `self`.

This length is in bytes, not `char`s or graphemes. In other words, it might not be what a human considers the length of the string.

##### §Examples

```
let len = "foo".len();
assert_eq!(3, len);

assert_eq!("ƒoo".len(), 4); assert_eq!("ƒoo".chars().count(), 3);
```

1.0.0

·

Source

#### pub fn is_empty(&self) -> bool

Returns `true` if `self` has a length of zero bytes.

##### §Examples

```
let s = "";
assert!(s.is_empty());

let s = "not empty";
assert!(!s.is_empty());
```

1.9.0

·

Source

#### pub fn is_char_boundary(&self, index: usize) -> bool

Checks that `index`-th byte is the first byte in a UTF-8 code point sequence or the end of the string.

The start and end of the string (when `index == self.len()`) are considered to be boundaries.

Returns `false` if `index` is greater than `self.len()`.

##### §Examples

```
let s = "Löwe 老虎 Léopard";
assert!(s.is_char_boundary(0));
assert!(s.is_char_boundary(6));
assert!(s.is_char_boundary(s.len()));

assert!(!s.is_char_boundary(2));

assert!(!s.is_char_boundary(8));
```

1.91.0

·

Source

#### pub fn floor_char_boundary(&self, index: usize) -> usize

Finds the closest `x` not exceeding `index` where `is_char_boundary(x)` is `true`.

This method can help you truncate a string so that it’s still valid UTF-8, but doesn’t exceed a given number of bytes. Note that this is done purely at the character level and can still visually split graphemes, even though the underlying characters aren’t split. For example, the emoji 🧑‍🔬 (scientist) could be split so that the string only includes 🧑 (person) instead.

##### §Examples

```
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.floor_char_boundary(13);
assert_eq!(closest, 10);
assert_eq!(&s[..closest], "❤️🧡");
```

1.91.0

·

Source

#### pub fn ceil_char_boundary(&self, index: usize) -> usize

Finds the closest `x` not below `index` where `is_char_boundary(x)` is `true`.

If `index` is greater than the length of the string, this returns the length of the string.

This method is the natural complement to `floor_char_boundary`. See that method for more details.

##### §Examples

```
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.ceil_char_boundary(13);
assert_eq!(closest, 14);
assert_eq!(&s[..closest], "❤️🧡💛");
```

1.0.0

·

Source

#### pub fn as_bytes(&self) -> &[u8] ⓘ

Converts a string slice to a byte slice. To convert the byte slice back into a string slice, use the `from_utf8` function.

##### §Examples

```
let bytes = "bors".as_bytes();
assert_eq!(b"bors", bytes);
```

1.20.0

·

Source

#### pub unsafe fn as_bytes_mut(&mut self) -> &mut [u8] ⓘ

Converts a mutable string slice to a mutable byte slice.

##### §Safety

The caller must ensure that the content of the slice is valid UTF-8 before the borrow ends and the underlying `str` is used.

Use of a `str` whose contents are not valid UTF-8 is undefined behavior.

##### §Examples

Basic usage:

```
let mut s = String::from("Hello");
let bytes = unsafe { s.as_bytes_mut() };

assert_eq!(b"Hello", bytes);
```

Mutability:

```
let mut s = String::from("🗻∈🌏");

unsafe {
    let bytes = s.as_bytes_mut();

    bytes[0] = 0xF0;
    bytes[1] = 0x9F;
    bytes[2] = 0x8D;
    bytes[3] = 0x94;
}

assert_eq!("🍔∈🌏", s);
```

1.0.0

·

Source

#### pub fn as_ptr(&self) -> *const u8

Converts a string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a `u8`. This pointer will be pointing to the first byte of the string slice.

The caller must ensure that the returned pointer is never written to. If you need to mutate the contents of the string slice, use `as_mut_ptr`.

##### §Examples

```
let s = "Hello";
let ptr = s.as_ptr();
```

1.36.0

·

Source

#### pub fn as_mut_ptr(&mut self) -> *mut u8

Converts a mutable string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a `u8`. This pointer will be pointing to the first byte of the string slice.

It is your responsibility to make sure that the string slice only gets modified in a way that it remains valid UTF-8.

1.20.0

·

Source

#### pub fn get<I>(&self, i: I) -> Option<&<I as SliceIndex<str>>::Output>where I: SliceIndex<str>,

Returns a subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns `None` whenever equivalent indexing operation would panic.

##### §Examples

```
let v = String::from("🗻∈🌏");

assert_eq!(Some("🗻"), v.get(0..4));

assert!(v.get(1..).is_none());
assert!(v.get(..8).is_none());

assert!(v.get(..42).is_none());
```

1.20.0

·

Source

#### pub fn get_mut<I>( &mut self, i: I, ) -> Option<&mut <I as SliceIndex<str>>::Output>where I: SliceIndex<str>,

Returns a mutable subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns `None` whenever equivalent indexing operation would panic.

##### §Examples

```
let mut v = String::from("hello");
assert!(v.get_mut(0..5).is_some());
assert!(v.get_mut(..42).is_none());
assert_eq!(Some("he"), v.get_mut(0..2).map(|v| &*v));

assert_eq!("hello", v);
{
    let s = v.get_mut(0..2);
    let s = s.map(|s| {
        s.make_ascii_uppercase();
        &*s
    });
    assert_eq!(Some("HE"), s);
}
assert_eq!("HEllo", v);
```

1.20.0

·

Source

#### pub unsafe fn get_unchecked<I>(&self, i: I) -> &<I as SliceIndex<str>>::Outputwhere I: SliceIndex<str>,

Returns an unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### §Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### §Examples

```
let v = "🗻∈🌏";
unsafe {
    assert_eq!("🗻", v.get_unchecked(0..4));
    assert_eq!("∈", v.get_unchecked(4..7));
    assert_eq!("🌏", v.get_unchecked(7..11));
}
```

1.20.0

·

Source

#### pub unsafe fn get_unchecked_mut<I>( &mut self, i: I, ) -> &mut <I as SliceIndex<str>>::Outputwhere I: SliceIndex<str>,

Returns a mutable, unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### §Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### §Examples

```
let mut v = String::from("🗻∈🌏");
unsafe {
    assert_eq!("🗻", v.get_unchecked_mut(0..4));
    assert_eq!("∈", v.get_unchecked_mut(4..7));
    assert_eq!("🌏", v.get_unchecked_mut(7..11));
}
```

1.0.0

·

Source

#### pub unsafe fn slice_unchecked(&self, begin: usize, end: usize) -> &str

👎

Deprecated since 1.29.0:

use `get_unchecked(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see `str` and `Index`.

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get a mutable string slice instead, see the `slice_mut_unchecked` method.

##### §Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

##### §Examples

```
let s = "Löwe 老虎 Léopard";

unsafe {
    assert_eq!("Löwe 老虎 Léopard", s.slice_unchecked(0, 21));
}

let s = "Hello, world!";

unsafe {
    assert_eq!("world", s.slice_unchecked(7, 12));
}
```

1.5.0

·

Source

#### pub unsafe fn slice_mut_unchecked( &mut self, begin: usize, end: usize, ) -> &mut str

👎

Deprecated since 1.29.0:

use `get_unchecked_mut(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see `str` and `IndexMut`.

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get an immutable string slice instead, see the `slice_unchecked` method.

##### §Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

1.4.0

·

Source

#### pub fn split_at(&self, mid: usize) -> (&str, &str)

Divides one string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the `split_at_mut` method.

##### §Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see `split_at_checked`.

##### §Examples

```
let s = "Per Martin-Löf";

let (first, last) = s.split_at(3);

assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);
```

1.4.0

·

Source

#### pub fn split_at_mut(&mut self, mid: usize) -> (&mut str, &mut str)

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the `split_at` method.

##### §Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see `split_at_mut_checked`.

##### §Examples

```
let mut s = "Per Martin-Löf".to_string();
{
    let (first, last) = s.split_at_mut(3);
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);
```

1.80.0

·

Source

#### pub fn split_at_checked(&self, mid: usize) -> Option<(&str, &str)>

Divides one string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the `split_at_mut_checked` method.

##### §Examples

```
let s = "Per Martin-Löf";

let (first, last) = s.split_at_checked(3).unwrap();
assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);

assert_eq!(None, s.split_at_checked(13));  assert_eq!(None, s.split_at_checked(16));  
```

1.80.0

·

Source

#### pub fn split_at_mut_checked( &mut self, mid: usize, ) -> Option<(&mut str, &mut str)>

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the `split_at_checked` method.

##### §Examples

```
let mut s = "Per Martin-Löf".to_string();
if let Some((first, last)) = s.split_at_mut_checked(3) {
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);

assert_eq!(None, s.split_at_mut_checked(13));  assert_eq!(None, s.split_at_mut_checked(16));  
```

1.0.0

·

Source

#### pub fn chars(&self) -> Chars<'_> ⓘ

Returns an iterator over the `char`s of a string slice.

As a string slice consists of valid UTF-8, we can iterate through a string slice by `char`. This method returns such an iterator.

It’s important to remember that `char` represents a Unicode Scalar Value, and might not match your idea of what a ‘character’ is. Iteration over grapheme clusters may be what you actually want. This functionality is not provided by Rust’s standard library, check crates.io instead.

##### §Examples

Basic usage:

```
let word = "goodbye";

let count = word.chars().count();
assert_eq!(7, count);

let mut chars = word.chars();

assert_eq!(Some('g'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('d'), chars.next());
assert_eq!(Some('b'), chars.next());
assert_eq!(Some('y'), chars.next());
assert_eq!(Some('e'), chars.next());

assert_eq!(None, chars.next());
```

Remember, `char`s might not match your intuition about characters:

```
let y = "y̆";

let mut chars = y.chars();

assert_eq!(Some('y'), chars.next()); assert_eq!(Some('\u{0306}'), chars.next());

assert_eq!(None, chars.next());
```

1.0.0

·

Source

#### pub fn char_indices(&self) -> CharIndices<'_> ⓘ

Returns an iterator over the `char`s of a string slice, and their positions.

As a string slice consists of valid UTF-8, we can iterate through a string slice by `char`. This method returns an iterator of both these `char`s, as well as their byte positions.

The iterator yields tuples. The position is first, the `char` is second.

##### §Examples

Basic usage:

```
let word = "goodbye";

let count = word.char_indices().count();
assert_eq!(7, count);

let mut char_indices = word.char_indices();

assert_eq!(Some((0, 'g')), char_indices.next());
assert_eq!(Some((1, 'o')), char_indices.next());
assert_eq!(Some((2, 'o')), char_indices.next());
assert_eq!(Some((3, 'd')), char_indices.next());
assert_eq!(Some((4, 'b')), char_indices.next());
assert_eq!(Some((5, 'y')), char_indices.next());
assert_eq!(Some((6, 'e')), char_indices.next());

assert_eq!(None, char_indices.next());
```

Remember, `char`s might not match your intuition about characters:

```
let yes = "y̆es";

let mut char_indices = yes.char_indices();

assert_eq!(Some((0, 'y')), char_indices.next()); assert_eq!(Some((1, '\u{0306}')), char_indices.next());

assert_eq!(Some((3, 'e')), char_indices.next());
assert_eq!(Some((4, 's')), char_indices.next());

assert_eq!(None, char_indices.next());
```

1.0.0

·

Source

#### pub fn bytes(&self) -> Bytes<'_> ⓘ

Returns an iterator over the bytes of a string slice.

As a string slice consists of a sequence of bytes, we can iterate through a string slice by byte. This method returns such an iterator.

##### §Examples

```
let mut bytes = "bors".bytes();

assert_eq!(Some(b'b'), bytes.next());
assert_eq!(Some(b'o'), bytes.next());
assert_eq!(Some(b'r'), bytes.next());
assert_eq!(Some(b's'), bytes.next());

assert_eq!(None, bytes.next());
```

1.1.0

·

Source

#### pub fn split_whitespace(&self) -> SplitWhitespace<'_> ⓘ

Splits a string slice by whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of whitespace.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`. If you only want to split on ASCII whitespace instead, use `split_ascii_whitespace`.

##### §Examples

Basic usage:

```
let mut iter = "A few words".split_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

All kinds of whitespace are considered:

```
let mut iter = " Mary   had\ta\u{2009}little  \n\t lamb".split_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all whitespace, the iterator yields no string slices:

```
assert_eq!("".split_whitespace().next(), None);
assert_eq!("   ".split_whitespace().next(), None);
```

1.34.0

·

Source

#### pub fn split_ascii_whitespace(&self) -> SplitAsciiWhitespace<'_> ⓘ

Splits a string slice by ASCII whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of ASCII whitespace.

This uses the same definition as `char::is_ascii_whitespace`. To split by Unicode `Whitespace` instead, use `split_whitespace`.

##### §Examples

Basic usage:

```
let mut iter = "A few words".split_ascii_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

Various kinds of ASCII whitespace are considered (see `char::is_ascii_whitespace`):

```
let mut iter = " Mary   had\ta little  \n\t lamb".split_ascii_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all ASCII whitespace, the iterator yields no string slices:

```
assert_eq!("".split_ascii_whitespace().next(), None);
assert_eq!("   ".split_ascii_whitespace().next(), None);
```

1.0.0

·

Source

#### pub fn lines(&self) -> Lines<'_> ⓘ

Returns an iterator over the lines of a string, as string slices.

Lines are split at line endings that are either newlines (`\n`) or sequences of a carriage return followed by a line feed (`\r\n`).

Line terminators are not included in the lines returned by the iterator.

Note that any carriage return (`\r`) not immediately followed by a line feed (`\n`) does not split a line. These carriage returns are thereby included in the produced lines.

The final line ending is optional. A string that ends with a final line ending will return the same lines as an otherwise identical string without a final line ending.

An empty string returns an empty iterator.

##### §Examples

Basic usage:

```
let text = "foo\r\nbar\n\nbaz\r";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
assert_eq!(Some("baz\r"), lines.next());

assert_eq!(None, lines.next());
```

The final line does not require any ending:

```
let text = "foo\nbar\n\r\nbaz";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
assert_eq!(Some("baz"), lines.next());

assert_eq!(None, lines.next());
```

An empty string returns an empty iterator:

```
let text = "";
let mut lines = text.lines();

assert_eq!(lines.next(), None);
```

1.0.0

·

Source

#### pub fn lines_any(&self) -> LinesAny<'_> ⓘ

👎

Deprecated since 1.4.0:

use lines() instead now

Returns an iterator over the lines of a string.

1.8.0

·

Source

#### pub fn encode_utf16(&self) -> EncodeUtf16<'_> ⓘ

Returns an iterator of `u16` over the string encoded as native endian UTF-16 (without byte-order mark).

##### §Examples

```
let text = "Zażółć gęślą jaźń";

let utf8_len = text.len();
let utf16_len = text.encode_utf16().count();

assert!(utf16_len <= utf8_len);
```

1.0.0

·

Source

#### pub fn contains<P>(&self, pat: P) -> boolwhere P: Pattern,

Returns `true` if the given pattern matches a sub-slice of this string slice.

Returns `false` if it does not.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
let bananas = "bananas";

assert!(bananas.contains("nana"));
assert!(!bananas.contains("apples"));
```

1.0.0

·

Source

#### pub fn starts_with<P>(&self, pat: P) -> boolwhere P: Pattern,

Returns `true` if the given pattern matches a prefix of this string slice.

Returns `false` if it does not.

The pattern can be a `&str`, in which case this function will return true if the `&str` is a prefix of this string slice.

The pattern can also be a `char`, a slice of `char`s, or a function or closure that determines if a character matches. These will only be checked against the first character of this string slice. Look at the second example below regarding behavior for slices of `char`s.

##### §Examples

```
let bananas = "bananas";

assert!(bananas.starts_with("bana"));
assert!(!bananas.starts_with("nana"));
```

```
let bananas = "bananas";

assert!(bananas.starts_with(&['b', 'a', 'n', 'a']));
assert!(bananas.starts_with(&['a', 'b', 'c', 'd']));
```

1.0.0

·

Source

#### pub fn ends_with<P>(&self, pat: P) -> boolwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns `true` if the given pattern matches a suffix of this string slice.

Returns `false` if it does not.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
let bananas = "bananas";

assert!(bananas.ends_with("anas"));
assert!(!bananas.ends_with("nana"));
```

1.0.0

·

Source

#### pub fn find<P>(&self, pat: P) -> Option<usize>where P: Pattern,

Returns the byte index of the first character of this string slice that matches the pattern.

Returns `None` if the pattern doesn’t match.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

Simple patterns:

```
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.find('L'), Some(0));
assert_eq!(s.find('é'), Some(14));
assert_eq!(s.find("pard"), Some(17));
```

More complex patterns using point-free style and closures:

```
let s = "Löwe 老虎 Léopard";

assert_eq!(s.find(char::is_whitespace), Some(5));
assert_eq!(s.find(char::is_lowercase), Some(1));
assert_eq!(s.find(|c: char| c.is_whitespace() || c.is_lowercase()), Some(1));
assert_eq!(s.find(|c: char| (c < 'o') && (c > 'a')), Some(4));
```

Not finding the pattern:

```
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.find(x), None);
```

1.0.0

·

Source

#### pub fn rfind<P>(&self, pat: P) -> Option<usize>where P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns the byte index for the first character of the last match of the pattern in this string slice.

Returns `None` if the pattern doesn’t match.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

Simple patterns:

```
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.rfind('L'), Some(13));
assert_eq!(s.rfind('é'), Some(14));
assert_eq!(s.rfind("pard"), Some(24));
```

More complex patterns with closures:

```
let s = "Löwe 老虎 Léopard";

assert_eq!(s.rfind(char::is_whitespace), Some(12));
assert_eq!(s.rfind(char::is_lowercase), Some(20));
```

Not finding the pattern:

```
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.rfind(x), None);
```

1.0.0

·

Source

#### pub fn split<P>(&self, pat: P) -> Split<'_, P> ⓘwhere P: Pattern,

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

If there are no matches the full string slice is returned as the only item in the iterator.

##### §Iterator behavior

The returned iterator will be a `DoubleEndedIterator` if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., `char`, but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the `rsplit` method can be used.

##### §Examples

Simple patterns:

```
let v: Vec<&str> = "Mary had a little lamb".split(' ').collect();
assert_eq!(v, ["Mary", "had", "a", "little", "lamb"]);

let v: Vec<&str> = "".split('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".split('X').collect();
assert_eq!(v, ["lion", "", "tiger", "leopard"]);

let v: Vec<&str> = "lion::tiger::leopard".split("::").collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);

let v: Vec<&str> = "AABBCC".split("DD").collect();
assert_eq!(v, ["AABBCC"]);

let v: Vec<&str> = "abc1def2ghi".split(char::is_numeric).collect();
assert_eq!(v, ["abc", "def", "ghi"]);

let v: Vec<&str> = "lionXtigerXleopard".split(char::is_uppercase).collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);
```

If the pattern is a slice of chars, split on each occurrence of any of the characters:

```
let v: Vec<&str> = "2020-11-03 23:59".split(&['-', ' ', ':', '@'][..]).collect();
assert_eq!(v, ["2020", "11", "03", "23", "59"]);
```

A more complex pattern, using a closure:

```
let v: Vec<&str> = "abc1defXghi".split(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "def", "ghi"]);
```

If a string contains multiple contiguous separators, you will end up with empty strings in the output:

```
let x = "||||a||b|c".to_string();
let d: Vec<_> = x.split('|').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

Contiguous separators are separated by the empty string.

```
let x = "(///)".to_string();
let d: Vec<_> = x.split('/').collect();

assert_eq!(d, &["(", "", "", ")"]);
```

Separators at the start or end of a string are neighbored by empty strings.

```
let d: Vec<_> = "010".split("0").collect();
assert_eq!(d, &["", "1", ""]);
```

When the empty string is used as a separator, it separates every character in the string, along with the beginning and end of the string.

```
let f: Vec<_> = "rust".split("").collect();
assert_eq!(f, &["", "r", "u", "s", "t", ""]);
```

Contiguous separators can lead to possibly surprising behavior when whitespace is used as the separator. This code is correct:

```
let x = "    a  b c".to_string();
let d: Vec<_> = x.split(' ').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

It does *not* give you:

ⓘ

```
assert_eq!(d, &["a", "b", "c"]);
```

Use `split_whitespace` for this behavior.

1.51.0

·

Source

#### pub fn split_inclusive<P>(&self, pat: P) -> SplitInclusive<'_, P> ⓘwhere P: Pattern,

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

Differs from the iterator produced by `split` in that `split_inclusive` leaves the matched part as the terminator of the substring.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Examples

```
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb."
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb."]);
```

If the last element of the string is matched, that element will be considered the terminator of the preceding substring. That substring will be the last item returned by the iterator.

```
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb.\n"
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb.\n"]);
```

1.0.0

·

Source

#### pub fn rsplit<P>(&self, pat: P) -> RSplit<'_, P> ⓘwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern and yielded in reverse order.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a `DoubleEndedIterator` if a forward/reverse search yields the same elements.

For iterating from the front, the `split` method can be used.

##### §Examples

Simple patterns:

```
let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);

let v: Vec<&str> = "".rsplit('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplit('X').collect();
assert_eq!(v, ["leopard", "tiger", "", "lion"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplit("::").collect();
assert_eq!(v, ["leopard", "tiger", "lion"]);
```

A more complex pattern, using a closure:

```
let v: Vec<&str> = "abc1defXghi".rsplit(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "def", "abc"]);
```

1.0.0

·

Source

#### pub fn split_terminator<P>(&self, pat: P) -> SplitTerminator<'_, P> ⓘwhere P: Pattern,

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

Equivalent to `split`, except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### §Iterator behavior

The returned iterator will be a `DoubleEndedIterator` if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., `char`, but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the `rsplit_terminator` method can be used.

##### §Examples

```
let v: Vec<&str> = "A.B.".split_terminator('.').collect();
assert_eq!(v, ["A", "B"]);

let v: Vec<&str> = "A..B..".split_terminator(".").collect();
assert_eq!(v, ["A", "", "B", ""]);

let v: Vec<&str> = "A.B:C.D".split_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["A", "B", "C", "D"]);
```

1.0.0

·

Source

#### pub fn rsplit_terminator<P>(&self, pat: P) -> RSplitTerminator<'_, P> ⓘwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns an iterator over substrings of `self`, separated by characters matched by a pattern and yielded in reverse order.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

Equivalent to `split`, except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### §Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be double ended if a forward/reverse search yields the same elements.

For iterating from the front, the `split_terminator` method can be used.

##### §Examples

```
let v: Vec<&str> = "A.B.".rsplit_terminator('.').collect();
assert_eq!(v, ["B", "A"]);

let v: Vec<&str> = "A..B..".rsplit_terminator(".").collect();
assert_eq!(v, ["", "B", "", "A"]);

let v: Vec<&str> = "A.B:C.D".rsplit_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["D", "C", "B", "A"]);
```

1.0.0

·

Source

#### pub fn splitn<P>(&self, n: usize, pat: P) -> SplitN<'_, P> ⓘwhere P: Pattern,

Returns an iterator over substrings of the given string slice, separated by a pattern, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

If the pattern allows a reverse search, the `rsplitn` method can be used.

##### §Examples

Simple patterns:

```
let v: Vec<&str> = "Mary had a little lambda".splitn(3, ' ').collect();
assert_eq!(v, ["Mary", "had", "a little lambda"]);

let v: Vec<&str> = "lionXXtigerXleopard".splitn(3, "X").collect();
assert_eq!(v, ["lion", "", "tigerXleopard"]);

let v: Vec<&str> = "abcXdef".splitn(1, 'X').collect();
assert_eq!(v, ["abcXdef"]);

let v: Vec<&str> = "".splitn(1, 'X').collect();
assert_eq!(v, [""]);
```

A more complex pattern, using a closure:

```
let v: Vec<&str> = "abc1defXghi".splitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "defXghi"]);
```

1.0.0

·

Source

#### pub fn rsplitn<P>(&self, n: usize, pat: P) -> RSplitN<'_, P> ⓘwhere P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

Returns an iterator over substrings of this string slice, separated by a pattern, starting from the end of the string, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The pattern can be a `&str`, `char`, a slice of `char`s, or a function or closure that determines if a character matches.

##### §Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

For splitting from the front, the `splitn` method can be used.

##### §Examples

Simple patterns:

```
let v: Vec<&str> = "Mary had a little lamb".rsplitn(3, ' ').collect();
assert_eq!(v, ["lamb", "little", "Mary had a"]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplitn(3, 'X').collect();
assert_eq!(v, ["leopard", "tiger", "lionX"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplitn(2, "::").collect();
assert_eq!(v, ["leopard", "lion::tiger"]);
```
