---
title: "String in std::string (part 1/4)"
source: https://doc.rust-lang.org/std/string/struct.String.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 1/4
---

# Struct String

1.0.0

·

Source

```
pub struct String {  }
```

Expand description

A UTF-8–encoded, growable string.

`String` is the most common string type. It has ownership over the contents of the string, stored in a heap-allocated buffer (see Representation). It is closely related to its borrowed counterpart, the primitive `str`.


## §Examples

You can create a `String` from a literal string with `String::from`:

```
let hello = String::from("Hello, world!");
```

You can append a `char` to a `String` with the `push` method, and append a `&str` with the `push_str` method:

```
let mut hello = String::from("Hello, ");

hello.push('w');
hello.push_str("orld!");
```

If you have a vector of UTF-8 bytes, you can create a `String` from it with the `from_utf8` method:

```
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);
```


## §UTF-8

`String`s are always valid UTF-8. If you need a non-UTF-8 string, consider `OsString`. It is similar, but without the UTF-8 constraint. Because UTF-8 is a variable width encoding, `String`s are typically smaller than an array of the same `char`s:

```
let s = "hello";
assert_eq!(s.len(), 5);

let s = ['h', 'e', 'l', 'l', 'o'];
let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
assert_eq!(size, 20);

let s = "💖💖💖💖💖";
assert_eq!(s.len(), 20);

let s = ['💖', '💖', '💖', '💖', '💖'];
let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
assert_eq!(size, 20);
```

This raises interesting questions as to how `s[i]` should work. What should `i` be here? Several options include byte indices and `char` indices but, because of UTF-8 encoding, only byte indices would provide constant time indexing. Getting the `i`th `char`, for example, is available using `chars`:

```
let s = "hello";
let third_character = s.chars().nth(2);
assert_eq!(third_character, Some('l'));

let s = "💖💖💖💖💖";
let third_character = s.chars().nth(2);
assert_eq!(third_character, Some('💖'));
```

Next, what should `s[i]` return? Because indexing returns a reference to underlying data it could be `&u8`, `&[u8]`, or something similar. Since we’re only providing one index, `&u8` makes the most sense but that might not be what the user expects and can be explicitly achieved with `as_bytes()`:

```
let s = "hello";
assert_eq!(s.as_bytes()[0], 104);
assert_eq!(s.as_bytes()[0], b'h');

let s = "💖💖💖💖💖";
assert_eq!(s.as_bytes()[0], 240);
```

Due to these ambiguities/restrictions, indexing with a `usize` is simply forbidden:

ⓘ

```
let s = "hello";

println!("The first letter of s is {}", s[0]);
```

It is more clear, however, how `&s[i..j]` should work (that is, indexing with a range). It should accept byte indices (to be constant-time) and return a `&str` which is UTF-8 encoded. This is also called “string slicing”. Note this will panic if the byte indices provided are not character boundaries - see `is_char_boundary` for more details. See the implementations for `SliceIndex<str>` for more details on string slicing. For a non-panicking version of string slicing, see `get`.

The `bytes` and `chars` methods return iterators over the bytes and codepoints of the string, respectively. To iterate over codepoints along with byte indices, use `char_indices`.


## §Deref

`String` implements `Deref<Target = str>`, and so inherits all of `str`’s methods. In addition, this means that you can pass a `String` to a function which takes a `&str` by using an ampersand (`&`):

```
fn takes_str(s: &str) { }

let s = String::from("Hello");

takes_str(&s);
```

This will create a `&str` from the `String` and pass it in. This conversion is very inexpensive, and so generally, functions will accept `&str`s as arguments unless they need a `String` for some specific reason.

In certain cases Rust doesn’t have enough information to make this conversion, known as `Deref` coercion. In the following example a string slice `&'a str` implements the trait `TraitExample`, and the function `example_func` takes anything that implements the trait. In this case Rust would need to make two implicit conversions, which Rust doesn’t have the means to do. For that reason, the following example will not compile.

ⓘ

```
trait TraitExample {}

impl<'a> TraitExample for &'a str {}

fn example_func<A: TraitExample>(example_arg: A) {}

let example_string = String::from("example_string");
example_func(&example_string);
```

There are two options that would work instead. The first would be to change the line `example_func(&example_string);` to `example_func(example_string.as_str());`, using the method `as_str()` to explicitly extract the string slice containing the string. The second way changes `example_func(&example_string);` to `example_func(&*example_string);`. In this case we are dereferencing a `String` to a `str`, then referencing the `str` back to `&str`. The second way is more idiomatic, however both work to do the conversion explicitly rather than relying on the implicit conversion.


## §Representation

A `String` is made up of three components: a pointer to some bytes, a length, and a capacity. The pointer points to the internal buffer which `String` uses to store its data. The length is the number of bytes currently stored in the buffer, and the capacity is the size of the buffer in bytes. As such, the length will always be less than or equal to the capacity.

This buffer is always stored on the heap.

You can look at these with the `as_ptr`, `len`, and `capacity` methods:

```
let story = String::from("Once upon a time...");

let (ptr, len, capacity) = story.into_raw_parts();

assert_eq!(19, len);

let s = unsafe { String::from_raw_parts(ptr, len, capacity) } ;

assert_eq!(String::from("Once upon a time..."), s);
```

If a `String` has enough capacity, adding elements to it will not re-allocate. For example, consider this program:

```
let mut s = String::new();

println!("{}", s.capacity());

for _ in 0..5 {
    s.push_str("hello");
    println!("{}", s.capacity());
}
```

This will output the following:

```
0
8
16
16
32
32
```

At first, we have no memory allocated at all, but as we append to the string, it increases its capacity appropriately. If we instead use the `with_capacity` method to allocate the correct capacity initially:

```
let mut s = String::with_capacity(25);

println!("{}", s.capacity());

for _ in 0..5 {
    s.push_str("hello");
    println!("{}", s.capacity());
}
```

We end up with a different output:

```
25
25
25
25
25
25
```

Here, there’s no need to allocate more memory inside the loop.


## Implementations

Source

§

### impl String

1.0.0 (const: 1.39.0)

·

Source

#### pub const fn new() -> String

Creates a new empty `String`.

Given that the `String` is empty, this will not allocate any initial buffer. While that means that this initial operation is very inexpensive, it may cause excessive allocation later when you add data. If you have an idea of how much data the `String` will hold, consider the `with_capacity` method to prevent excessive re-allocation.

##### §Examples

```
let s = String::new();
```

1.0.0

·

Source

#### pub fn with_capacity(capacity: usize) -> String

Creates a new empty `String` with at least the specified capacity.

`String`s have an internal buffer to hold their data. The capacity is the length of that buffer, and can be queried with the `capacity` method. This method creates an empty `String`, but one with an initial buffer that can hold at least `capacity` bytes. This is useful when you may be appending a bunch of data to the `String`, reducing the number of reallocations it needs to do.

If the given capacity is `0`, no allocation will occur, and this method is identical to the `new` method.

##### §Panics

Panics if the capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut s = String::with_capacity(10);

assert_eq!(s.len(), 0);

let cap = s.capacity();
for _ in 0..10 {
    s.push('a');
}

assert_eq!(s.capacity(), cap);

s.push('a');
```

Source

#### pub fn try_with_capacity(capacity: usize) -> Result<String, TryReserveError>

🔬

This is a nightly-only experimental API. (

try_with_capacity

#91913

)

Creates a new empty `String` with at least the specified capacity.

##### §Errors

Returns `Err` if the capacity exceeds `isize::MAX` bytes, or if the memory allocator reports failure.

1.0.0

·

Source

#### pub fn from_utf8(vec: Vec<u8>) -> Result<String, FromUtf8Error>

Converts a vector of bytes to a `String`.

A string (`String`) is made of bytes (`u8`), and a vector of bytes (`Vec<u8>`) is made of bytes, so this function converts between the two. Not all byte slices are valid `String`s, however: `String` requires that it is valid UTF-8. `from_utf8()` checks to ensure that the bytes are valid UTF-8, and then does the conversion.

If you are sure that the byte slice is valid UTF-8, and you don’t want to incur the overhead of the validity check, there is an unsafe version of this function, `from_utf8_unchecked`, which has the same behavior but skips the check.

This method will take care to not copy the vector, for efficiency’s sake.

If you need a `&str` instead of a `String`, consider `str::from_utf8`.

The inverse of this method is `into_bytes`.

##### §Errors

Returns `Err` if the slice is not UTF-8 with a description as to why the provided bytes are not UTF-8. The vector you moved in is also included.

##### §Examples

Basic usage:

```
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);
```

Incorrect bytes:

```
let sparkle_heart = vec![0, 159, 146, 150];

assert!(String::from_utf8(sparkle_heart).is_err());
```

See the docs for `FromUtf8Error` for more details on what you can do with this error.

1.0.0

·

Source

#### pub fn from_utf8_lossy(v: &[u8]) -> Cow<'_, str>

Converts a slice of bytes to a string, including invalid characters.

Strings are made of bytes (`u8`), and a slice of bytes (`&[u8]`) is made of bytes, so this function converts between the two. Not all byte slices are valid strings, however: strings are required to be valid UTF-8. During this conversion, `from_utf8_lossy()` will replace any invalid UTF-8 sequences with `U+FFFD REPLACEMENT CHARACTER`, which looks like this: �

If you are sure that the byte slice is valid UTF-8, and you don’t want to incur the overhead of the conversion, there is an unsafe version of this function, `from_utf8_unchecked`, which has the same behavior but skips the checks.

This function returns a `Cow<'a, str>`. If our byte slice is invalid UTF-8, then we need to insert the replacement characters, which will change the size of the string, and hence, require a `String`. But if it’s already valid UTF-8, we don’t need a new allocation. This return type allows us to handle both cases.

##### §Examples

Basic usage:

```
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8_lossy(&sparkle_heart);

assert_eq!("💖", sparkle_heart);
```

Incorrect bytes:

```
let input = b"Hello \xF0\x90\x80World";
let output = String::from_utf8_lossy(input);

assert_eq!("Hello �World", output);
```

Source

#### pub fn from_utf8_lossy_owned(v: Vec<u8>) -> String

🔬

This is a nightly-only experimental API. (

string_from_utf8_lossy_owned

#129436

)

Converts a `Vec<u8>` to a `String`, substituting invalid UTF-8 sequences with replacement characters.

See `from_utf8_lossy` for more details.

Note that this function does not guarantee reuse of the original `Vec` allocation.

##### §Examples

Basic usage:

```
#![feature(string_from_utf8_lossy_owned)]
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8_lossy_owned(sparkle_heart);

assert_eq!(String::from("💖"), sparkle_heart);
```

Incorrect bytes:

```
#![feature(string_from_utf8_lossy_owned)]
let input: Vec<u8> = b"Hello \xF0\x90\x80World".into();
let output = String::from_utf8_lossy_owned(input);

assert_eq!(String::from("Hello �World"), output);
```

1.0.0

·

Source

#### pub fn from_utf16(v: &[u16]) -> Result<String, FromUtf16Error>

Decode a native endian UTF-16–encoded vector `v` into a `String`, returning `Err` if `v` contains any invalid data.

##### §Examples

```
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0x0073, 0x0069, 0x0063];
assert_eq!(String::from("𝄞music"),
           String::from_utf16(v).unwrap());

let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0xD800, 0x0069, 0x0063];
assert!(String::from_utf16(v).is_err());
```

1.0.0

·

Source

#### pub fn from_utf16_lossy(v: &[u16]) -> String

Decode a native endian UTF-16–encoded slice `v` into a `String`, replacing invalid data with the replacement character (`U+FFFD`).

Unlike `from_utf8_lossy` which returns a `Cow<'a, str>`, `from_utf16_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### §Examples

```
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0x0073, 0xDD1E, 0x0069, 0x0063,
          0xD834];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16_lossy(v));
```

Source

#### pub fn from_utf16le(v: &[u8]) -> Result<String, FromUtf16Error>

🔬

This is a nightly-only experimental API. (

str_from_utf16_endian

#116258

)

Decode a UTF-16LE–encoded vector `v` into a `String`, returning `Err` if `v` contains any invalid data.

##### §Examples

Basic usage:

```
#![feature(str_from_utf16_endian)]
let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x73, 0x00, 0x69, 0x00, 0x63, 0x00];
assert_eq!(String::from("𝄞music"),
           String::from_utf16le(v).unwrap());

let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x00, 0xD8, 0x69, 0x00, 0x63, 0x00];
assert!(String::from_utf16le(v).is_err());
```

Source

#### pub fn from_utf16le_lossy(v: &[u8]) -> String

🔬

This is a nightly-only experimental API. (

str_from_utf16_endian

#116258

)

Decode a UTF-16LE–encoded slice `v` into a `String`, replacing invalid data with the replacement character (`U+FFFD`).

Unlike `from_utf8_lossy` which returns a `Cow<'a, str>`, `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### §Examples

Basic usage:

```
#![feature(str_from_utf16_endian)]
let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x73, 0x00, 0x1E, 0xDD, 0x69, 0x00, 0x63, 0x00,
          0x34, 0xD8];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16le_lossy(v));
```

Source

#### pub fn from_utf16be(v: &[u8]) -> Result<String, FromUtf16Error>

🔬

This is a nightly-only experimental API. (

str_from_utf16_endian

#116258

)

Decode a UTF-16BE–encoded vector `v` into a `String`, returning `Err` if `v` contains any invalid data.

##### §Examples

Basic usage:

```
#![feature(str_from_utf16_endian)]
let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0x00, 0x73, 0x00, 0x69, 0x00, 0x63];
assert_eq!(String::from("𝄞music"),
           String::from_utf16be(v).unwrap());

let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0xD8, 0x00, 0x00, 0x69, 0x00, 0x63];
assert!(String::from_utf16be(v).is_err());
```

Source

#### pub fn from_utf16be_lossy(v: &[u8]) -> String

🔬

This is a nightly-only experimental API. (

str_from_utf16_endian

#116258

)

Decode a UTF-16BE–encoded slice `v` into a `String`, replacing invalid data with the replacement character (`U+FFFD`).

Unlike `from_utf8_lossy` which returns a `Cow<'a, str>`, `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### §Examples

Basic usage:

```
#![feature(str_from_utf16_endian)]
let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0x00, 0x73, 0xDD, 0x1E, 0x00, 0x69, 0x00, 0x63,
          0xD8, 0x34];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16be_lossy(v));
```

1.93.0

·

Source

#### pub fn into_raw_parts(self) -> (*mut u8, usize, usize)

Decomposes a `String` into its raw components: `(pointer, length, capacity)`.

Returns the raw pointer to the underlying data, the length of the string (in bytes), and the allocated capacity of the data (in bytes). These are the same arguments in the same order as the arguments to `from_raw_parts`.

After calling this function, the caller is responsible for the memory previously managed by the `String`. The only way to do this is to convert the raw pointer, length, and capacity back into a `String` with the `from_raw_parts` function, allowing the destructor to perform the cleanup.

##### §Examples

```
let s = String::from("hello");

let (ptr, len, cap) = s.into_raw_parts();

let rebuilt = unsafe { String::from_raw_parts(ptr, len, cap) };
assert_eq!(rebuilt, "hello");
```

1.0.0

·

Source

#### pub unsafe fn from_raw_parts( buf: *mut u8, length: usize, capacity: usize, ) -> String

Creates a new `String` from a pointer, a length and a capacity.

##### §Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- all safety requirements for `Vec::<u8>::from_raw_parts`.
- all safety requirements for `String::from_utf8_unchecked`.

Violating these may cause problems like corrupting the allocator’s internal data structures. For example, it is normally **not** safe to build a `String` from a pointer to a C `char` array containing UTF-8 *unless* you are certain that array was originally allocated by the Rust standard library’s allocator.

The ownership of `buf` is effectively transferred to the `String` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### §Examples

```
unsafe {
    let s = String::from("hello");

    let (ptr, len, capacity) = s.into_raw_parts();

    let s = String::from_raw_parts(ptr, len, capacity);

    assert_eq!(String::from("hello"), s);
}
```

1.0.0

·

Source

#### pub unsafe fn from_utf8_unchecked(bytes: Vec<u8>) -> String

Converts a vector of bytes to a `String` without checking that the string contains valid UTF-8.

See the safe version, `from_utf8`, for more details.

##### §Safety

This function is unsafe because it does not check that the bytes passed to it are valid UTF-8. If this constraint is violated, it may cause memory unsafety issues with future users of the `String`, as the rest of the standard library assumes that `String`s are valid UTF-8.

##### §Examples

```
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = unsafe {
    String::from_utf8_unchecked(sparkle_heart)
};

assert_eq!("💖", sparkle_heart);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn into_bytes(self) -> Vec<u8> ⓘ

Converts a `String` into a byte vector.

This consumes the `String`, so we do not need to copy its contents.

##### §Examples

```
let s = String::from("hello");
let bytes = s.into_bytes();

assert_eq!(&[104, 101, 108, 108, 111][..], &bytes[..]);
```

1.7.0 (const: 1.87.0)

·

Source

#### pub const fn as_str(&self) -> &str

Extracts a string slice containing the entire `String`.

##### §Examples

```
let s = String::from("foo");

assert_eq!("foo", s.as_str());
```

1.7.0 (const: 1.87.0)

·

Source

#### pub const fn as_mut_str(&mut self) -> &mut str

Converts a `String` into a mutable string slice.

##### §Examples

```
let mut s = String::from("foobar");
let s_mut_str = s.as_mut_str();

s_mut_str.make_ascii_uppercase();

assert_eq!("FOOBAR", s_mut_str);
```

1.0.0

·

Source

#### pub fn push_str(&mut self, string: &str)

Appends a given string slice onto the end of this `String`.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut s = String::from("foo");

s.push_str("bar");

assert_eq!("foobar", s);
```

1.87.0

·

Source

#### pub fn extend_from_within<R>(&mut self, src: R)where R: RangeBounds<usize>,

Copies elements from `src` range to the end of the string.

##### §Panics

Panics if the range has `start_bound > end_bound`, if the range is bounded on either end and does not lie on a `char` boundary, or if the new capacity exceeds `isize::MAX` bytes.

##### §Examples

```
let mut string = String::from("abcde");

string.extend_from_within(2..);
assert_eq!(string, "abcdecde");

string.extend_from_within(..2);
assert_eq!(string, "abcdecdeab");

string.extend_from_within(4..8);
assert_eq!(string, "abcdecdeabecde");
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn capacity(&self) -> usize

Returns this `String`’s capacity, in bytes.

##### §Examples

```
let s = String::with_capacity(10);

assert!(s.capacity() >= 10);
```

1.0.0

·

Source

#### pub fn reserve(&mut self, additional: usize)

Reserves capacity for at least `additional` bytes more than the current length. The allocator may reserve more space to speculatively avoid frequent allocations. After calling `reserve`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if capacity is already sufficient.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

Basic usage:

```
let mut s = String::new();

s.reserve(10);

assert!(s.capacity() >= 10);
```

This might not actually increase the capacity:

```
let mut s = String::with_capacity(10);
s.push('a');
s.push('b');

let capacity = s.capacity();
assert_eq!(2, s.len());
assert!(capacity >= 10);

s.reserve(8);

assert_eq!(capacity, s.capacity());
```

1.0.0

·

Source

#### pub fn reserve_exact(&mut self, additional: usize)

Reserves the minimum capacity for at least `additional` bytes more than the current length. Unlike `reserve`, this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `reserve_exact`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if the capacity is already sufficient.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

Basic usage:

```
let mut s = String::new();

s.reserve_exact(10);

assert!(s.capacity() >= 10);
```

This might not actually increase the capacity:

```
let mut s = String::with_capacity(10);
s.push('a');
s.push('b');

let capacity = s.capacity();
assert_eq!(2, s.len());
assert!(capacity >= 10);

s.reserve_exact(8);

assert_eq!(capacity, s.capacity());
```

1.57.0

·

Source

#### pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError>

Tries to reserve capacity for at least `additional` bytes more than the current length. The allocator may reserve more space to speculatively avoid frequent allocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient. This method preserves the contents even if an error occurs.

##### §Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### §Examples

```
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<String, TryReserveError> {
    let mut output = String::new();

    output.try_reserve(data.len())?;

    output.push_str(data);

    Ok(output)
}
```

1.57.0

·

Source

#### pub fn try_reserve_exact( &mut self, additional: usize, ) -> Result<(), TryReserveError>

Tries to reserve the minimum capacity for at least `additional` bytes more than the current length. Unlike `try_reserve`, this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `try_reserve_exact`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer `try_reserve` if future insertions are expected.

##### §Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### §Examples

```
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<String, TryReserveError> {
    let mut output = String::new();

    output.try_reserve_exact(data.len())?;

    output.push_str(data);

    Ok(output)
}
```

1.0.0

·

Source

#### pub fn shrink_to_fit(&mut self)

Shrinks the capacity of this `String` to match its length.

##### §Examples

```
let mut s = String::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to_fit();
assert_eq!(3, s.capacity());
```

1.56.0

·

Source

#### pub fn shrink_to(&mut self, min_capacity: usize)

Shrinks the capacity of this `String` with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

##### §Examples

```
let mut s = String::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to(10);
assert!(s.capacity() >= 10);
s.shrink_to(0);
assert!(s.capacity() >= 3);
```

1.0.0

·

Source

#### pub fn push(&mut self, ch: char)

Appends the given `char` to the end of this `String`.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut s = String::from("abc");

s.push('1');
s.push('2');
s.push('3');

assert_eq!("abc123", s);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn as_bytes(&self) -> &[u8] ⓘ

Returns a byte slice of this `String`’s contents.

The inverse of this method is `from_utf8`.

##### §Examples

```
let s = String::from("hello");

assert_eq!(&[104, 101, 108, 108, 111], s.as_bytes());
```

1.0.0

·

Source

#### pub fn truncate(&mut self, new_len: usize)

Shortens this `String` to the specified length.

If `new_len` is greater than or equal to the string’s current length, this has no effect.

Note that this method has no effect on the allocated capacity of the string

##### §Panics

Panics if `new_len` does not lie on a `char` boundary.

##### §Examples

```
let mut s = String::from("hello");

s.truncate(2);

assert_eq!("he", s);
```

1.0.0

·

Source

#### pub fn pop(&mut self) -> Option<char>

Removes the last character from the string buffer and returns it.

Returns `None` if this `String` is empty.

##### §Examples

```
let mut s = String::from("abč");

assert_eq!(s.pop(), Some('č'));
assert_eq!(s.pop(), Some('b'));
assert_eq!(s.pop(), Some('a'));

assert_eq!(s.pop(), None);
```

1.0.0

·

Source

#### pub fn remove(&mut self, idx: usize) -> char

Removes a `char` from this `String` at byte position `idx` and returns it.

Copies all bytes after the removed char to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### §Panics

Panics if `idx` is larger than or equal to the `String`’s length, or if it does not lie on a `char` boundary.

##### §Examples

```
let mut s = String::from("abç");

assert_eq!(s.remove(0), 'a');
assert_eq!(s.remove(1), 'ç');
assert_eq!(s.remove(0), 'b');
```

Source

#### pub fn remove_matches<P>(&mut self, pat: P)where P: Pattern,

🔬

This is a nightly-only experimental API. (

string_remove_matches

#72826

)

Remove all matches of pattern `pat` in the `String`.

##### §Examples

```
#![feature(string_remove_matches)]
let mut s = String::from("Trees are not green, the sky is not blue.");
s.remove_matches("not ");
assert_eq!("Trees are green, the sky is blue.", s);
```

Matches will be detected and removed iteratively, so in cases where patterns overlap, only the first pattern will be removed:

```
#![feature(string_remove_matches)]
let mut s = String::from("banana");
s.remove_matches("ana");
assert_eq!("bna", s);
```

1.26.0

·

Source

#### pub fn retain<F>(&mut self, f: F)where F: FnMut(char) -> bool,

Retains only the characters specified by the predicate.

In other words, remove all characters `c` such that `f(c)` returns `false`. This method operates in place, visiting each character exactly once in the original order, and preserves the order of the retained characters.

##### §Examples

```
let mut s = String::from("f_o_ob_ar");

s.retain(|c| c != '_');

assert_eq!(s, "foobar");
```

Because the elements are visited exactly once in the original order, external state may be used to decide which elements to keep.

```
let mut s = String::from("abcde");
let keep = [false, true, true, false, true];
let mut iter = keep.iter();
s.retain(|_| *iter.next().unwrap());
assert_eq!(s, "bce");
```

1.0.0

·

Source

#### pub fn insert(&mut self, idx: usize, ch: char)

Inserts a character into this `String` at byte position `idx`.

Reallocates if `self.capacity()` is insufficient, which may involve copying all `self.capacity()` bytes. Makes space for the insertion by copying all bytes of `&self[idx..]` to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### §Panics

Panics if `idx` is larger than the `String`’s length, or if it does not lie on a `char` boundary.

##### §Examples

```
let mut s = String::with_capacity(3);

s.insert(0, 'f');
s.insert(1, 'o');
s.insert(2, 'o');

assert_eq!("foo", s);
```

1.16.0

·

Source

#### pub fn insert_str(&mut self, idx: usize, string: &str)

Inserts a string slice into this `String` at byte position `idx`.

Reallocates if `self.capacity()` is insufficient, which may involve copying all `self.capacity()` bytes. Makes space for the insertion by copying all bytes of `&self[idx..]` to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### §Panics

Panics if `idx` is larger than the `String`’s length, or if it does not lie on a `char` boundary.

##### §Examples

```
let mut s = String::from("bar");

s.insert_str(0, "foo");

assert_eq!("foobar", s);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const unsafe fn as_mut_vec(&mut self) -> &mut Vec<u8> ⓘ

Returns a mutable reference to the contents of this `String`.

##### §Safety

This function is unsafe because the returned `&mut Vec` allows writing bytes which are not valid UTF-8. If this constraint is violated, using the original `String` after dropping the `&mut Vec` may violate memory safety, as the rest of the standard library assumes that `String`s are valid UTF-8.

##### §Examples

```
let mut s = String::from("hello");

unsafe {
    let vec = s.as_mut_vec();
    assert_eq!(&[104, 101, 108, 108, 111][..], &vec[..]);

    vec.reverse();
}
assert_eq!(s, "olleh");
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn len(&self) -> usize

Returns the length of this `String`, in bytes, not `char`s or graphemes. In other words, it might not be what a human considers the length of the string.

##### §Examples

```
let a = String::from("foo");
assert_eq!(a.len(), 3);

let fancy_f = String::from("ƒoo");
assert_eq!(fancy_f.len(), 4);
assert_eq!(fancy_f.chars().count(), 3);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn is_empty(&self) -> bool

Returns `true` if this `String` has a length of zero, and `false` otherwise.

##### §Examples

```
let mut v = String::new();
assert!(v.is_empty());

v.push('a');
assert!(!v.is_empty());
```

1.16.0

·

Source

#### pub fn split_off(&mut self, at: usize) -> String

Splits the string into two at the given byte index.

Returns a newly allocated `String`. `self` contains bytes `[0, at)`, and the returned `String` contains bytes `[at, len)`. `at` must be on the boundary of a UTF-8 code point.

Note that the capacity of `self` does not change.

##### §Panics

Panics if `at` is not on a `UTF-8` code point boundary, or if it is beyond the last code point of the string.

##### §Examples

```
let mut hello = String::from("Hello, World!");
let world = hello.split_off(7);
assert_eq!(hello, "Hello, ");
assert_eq!(world, "World!");
```

1.0.0

·

Source

#### pub fn clear(&mut self)

Truncates this `String`, removing all contents.

While this means the `String` will have a length of zero, it does not touch its capacity.

##### §Examples

```
let mut s = String::from("foo");

s.clear();

assert!(s.is_empty());
assert_eq!(0, s.len());
assert_eq!(3, s.capacity());
```

1.6.0

·

Source

#### pub fn drain<R>(&mut self, range: R) -> Drain<'_> ⓘwhere R: RangeBounds<usize>,

Removes the specified range from the string in bulk, returning all removed characters as an iterator.

The returned iterator keeps a mutable borrow on the string to optimize its implementation.

##### §Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and does not lie on a `char` boundary.

##### §Leaking

If the returned iterator goes out of scope without being dropped (due to `core::mem::forget`, for example), the string may still contain a copy of any drained characters, or may have lost characters arbitrarily, including characters outside the range.

##### §Examples

```
let mut s = String::from("α is alpha, β is beta");
let beta_offset = s.find('β').unwrap_or(s.len());

let t: String = s.drain(..beta_offset).collect();
assert_eq!(t, "α is alpha, ");
assert_eq!(s, "β is beta");

s.drain(..);
assert_eq!(s, "");
```

Source

#### pub fn into_chars(self) -> IntoChars ⓘ

🔬

This is a nightly-only experimental API. (

string_into_chars

#133125

)

Converts a `String` into an iterator over the `char`s of the string.

As a string consists of valid UTF-8, we can iterate through a string by `char`. This method returns such an iterator.

It’s important to remember that `char` represents a Unicode Scalar Value, and might not match your idea of what a ‘character’ is. Iteration over grapheme clusters may be what you actually want. That functionality is not provided by Rust’s standard library, check crates.io instead.

##### §Examples

Basic usage:

```
#![feature(string_into_chars)]

let word = String::from("goodbye");

let mut chars = word.into_chars();

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
#![feature(string_into_chars)]

let y = String::from("y̆");

let mut chars = y.into_chars();

assert_eq!(Some('y'), chars.next()); assert_eq!(Some('\u{0306}'), chars.next());

assert_eq!(None, chars.next());
```

1.27.0

·

Source

#### pub fn replace_range<R>(&mut self, range: R, replace_with: &str)where R: RangeBounds<usize>,

Removes the specified range in the string, and replaces it with the given string. The given string doesn’t need to be the same length as the range.

##### §Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and does not lie on a `char` boundary.

##### §Examples

```
let mut s = String::from("α is alpha, β is beta");
let beta_offset = s.find('β').unwrap_or(s.len());

s.replace_range(..beta_offset, "Α is capital alpha; ");
assert_eq!(s, "Α is capital alpha; β is beta");
```

Source

#### pub fn replace_first<P>(&mut self, from: P, to: &str)where P: Pattern,

🔬

This is a nightly-only experimental API. (

string_replace_in_place

#147949

)

Replaces the leftmost occurrence of a pattern with another string, in-place.

This method can be preferred over `string = string.replacen(..., 1);`, as it can use the `String`’s existing capacity to prevent a reallocation if sufficient space is available.

##### §Examples

Basic usage:

```
#![feature(string_replace_in_place)]

let mut s = String::from("Test Results: ❌❌❌");

s.replace_first('❌', "✅");
assert_eq!(s, "Test Results: ✅❌❌");
```

Source

#### pub fn replace_last<P>(&mut self, from: P, to: &str)where P: Pattern, <P as Pattern>::Searcher<'a>: for<'a> ReverseSearcher<'a>,

🔬

This is a nightly-only experimental API. (

string_replace_in_place

#147949

)

Replaces the rightmost occurrence of a pattern with another string, in-place.

##### §Examples

Basic usage:

```
#![feature(string_replace_in_place)]

let mut s = String::from("Test Results: ❌❌❌");

s.replace_last('❌', "✅");
assert_eq!(s, "Test Results: ❌❌✅");
```

1.4.0

·

Source

#### pub fn into_boxed_str(self) -> Box<str>

Converts this `String` into a `Box<str>`.

Before doing the conversion, this method discards excess capacity like `shrink_to_fit`. Note that this call may reallocate and copy the bytes of the string.

##### §Examples

```
let s = String::from("hello");

let b = s.into_boxed_str();
```

1.72.0

·

Source

#### pub fn leak<'a>(self) -> &'a mut str

Consumes and leaks the `String`, returning a mutable reference to the contents, `&'a mut str`.

The caller has free choice over the returned lifetime, including `'static`. Indeed, this function is ideally used for data that lives for the remainder of the program’s life, as dropping the returned reference will cause a memory leak.

It does not reallocate or shrink the `String`, so the leaked allocation may include unused capacity that is not part of the returned slice. If you want to discard excess capacity, call `into_boxed_str`, and then `Box::leak` instead. However, keep in mind that trimming the capacity may result in a reallocation and copy.

##### §Examples

```
let x = String::from("bucket");
let static_ref: &'static mut str = x.leak();
assert_eq!(static_ref, "bucket");
```
