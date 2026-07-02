---
title: "String in std::string (part 4/4)"
source: https://doc.rust-lang.org/std/string/struct.String.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 4/4
---

## Trait Implementations

1.0.0

·

Source

§

### impl Add<&str> for String

Implements the `+` operator for concatenating two strings.

This consumes the `String` on the left-hand side and re-uses its buffer (growing it if necessary). This is done to avoid allocating a new `String` and copying the entire contents on every operation, which would lead to *O*(*n*^2) running time when building an *n*-byte string by repeated concatenation.

The string on the right-hand side is only borrowed; its contents are copied into the returned `String`.

#### §Examples

Concatenating two `String`s takes the first by value and borrows the second:

```
let a = String::from("hello");
let b = String::from(" world");
let c = a + &b;
```

If you want to keep using the first `String`, you can clone it and append to the clone instead:

```
let a = String::from("hello");
let b = String::from(" world");
let c = a.clone() + &b;
```

Concatenating `&str` slices can be done by converting the first to a `String`:

```
let a = "hello";
let b = " world";
let c = a.to_string() + b;
```

Source

§

#### type Output = String

The resulting type after applying the

+

operator.

Source

§

#### fn add(self, other: &str) -> String

Performs the

+

operation.

Read more

1.12.0

·

Source

§

### impl AddAssign<&str> for String

Implements the `+=` operator for appending to a `String`.

This has the same behavior as the `push_str` method.

Source

§

#### fn add_assign(&mut self, other: &str)

Performs the

+=

operation.

Read more

1.43.0

·

Source

§

### impl AsMut<str> for String

Source

§

#### fn as_mut(&mut self) -> &mut str

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl AsRef<[u8]> for String

Source

§

#### fn as_ref(&self) -> &[u8] ⓘ

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl AsRef<OsStr> for String

Source

§

#### fn as_ref(&self) -> &OsStr

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl AsRef<Path> for String

Source

§

#### fn as_ref(&self) -> &Path

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl AsRef<str> for String

Source

§

#### fn as_ref(&self) -> &str

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl Borrow<str> for String

Source

§

#### fn borrow(&self) -> &str

Immutably borrows from an owned value.

Read more

1.36.0

·

Source

§

### impl BorrowMut<str> for String

Source

§

#### fn borrow_mut(&mut self) -> &mut str

Mutably borrows from an owned value.

Read more

1.0.0

·

Source

§

### impl Clone for String

Source

§

#### fn clone_from(&mut self, source: &String)

Clones the contents of `source` into `self`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

Source

§

#### fn clone(&self) -> String

Returns a duplicate of the value.

Read more

1.0.0

·

Source

§

### impl Debug for String

Source

§

#### fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>

Formats the value using the given formatter.

Read more

1.0.0 (const:

unstable

)

·

Source

§

### impl Default for String

Source

§

#### fn default() -> String

Creates an empty `String`.

1.0.0

·

Source

§

### impl Deref for String

Source

§

#### type Target = str

The resulting type after dereferencing.

Source

§

#### fn deref(&self) -> &str

Dereferences the value.

1.3.0

·

Source

§

### impl DerefMut for String

Source

§

#### fn deref_mut(&mut self) -> &mut str

Mutably dereferences the value.

1.0.0

·

Source

§

### impl Display for String

Source

§

#### fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>

Formats the value using the given formatter.

Read more

Source

§

### impl<'a> Extend<&'a AsciiChar> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = &'a AsciiChar>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, c: &'a AsciiChar)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.2.0

·

Source

§

### impl<'a> Extend<&'a char> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = &'a char>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, _: &'a char)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.0.0

·

Source

§

### impl<'a> Extend<&'a str> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = &'a str>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, s: &'a str)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.45.0

·

Source

§

### impl<A> Extend<Box<str, A>> for Stringwhere A: Allocator,

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = Box<str, A>>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, item: A)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

Source

§

### impl Extend<AsciiChar> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = AsciiChar>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, c: AsciiChar)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.19.0

·

Source

§

### impl<'a> Extend<Cow<'a, str>> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = Cow<'a, str>>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, s: Cow<'a, str>)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.4.0

·

Source

§

### impl Extend<String> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = String>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, s: String)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.0.0

·

Source

§

### impl Extend<char> for String

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = char>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, c: char)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Extends a collection with exactly one element.

Source

§

#### fn extend_reserve(&mut self, additional: usize)

🔬

This is a nightly-only experimental API. (

extend_one

#72631

)

Reserves capacity in a collection for the given number of additional elements.

Read more

1.28.0

·

Source

§

### impl<'a> From<&'a String> for Cow<'a, str>

Source

§

#### fn from(s: &'a String) -> Cow<'a, str>

Converts a `String` reference into a `Borrowed` variant. No heap allocation is performed, and the string is not copied.

##### §Example

```
let s = "eggplant".to_string();
assert_eq!(Cow::from(&s), Cow::Borrowed("eggplant"));
```

1.35.0

·

Source

§

### impl From<&String> for String

Source

§

#### fn from(s: &String) -> String

Converts a `&String` into a `String`.

This clones `s` and returns the clone.

1.44.0

·

Source

§

### impl From<&mut str> for String

Source

§

#### fn from(s: &mut str) -> String

Converts a `&mut str` into a `String`.

The result is allocated on the heap.

1.0.0

·

Source

§

### impl From<&str> for String

Source

§

#### fn from(s: &str) -> String

Converts a `&str` into a `String`.

The result is allocated on the heap.

1.18.0

·

Source

§

### impl From<Box<str>> for String

Source

§

#### fn from(s: Box<str>) -> String

Converts the given boxed `str` slice to a `String`. It is notable that the `str` slice is owned.

##### §Examples

```
let s1: String = String::from("hello world");
let s2: Box<str> = s1.into_boxed_str();
let s3: String = String::from(s2);

assert_eq!("hello world", s3)
```

1.14.0

·

Source

§

### impl<'a> From<Cow<'a, str>> for String

Source

§

#### fn from(s: Cow<'a, str>) -> String

Converts a clone-on-write string to an owned instance of `String`.

This extracts the owned string, clones the string if it is not already owned.

##### §Example

```
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
let owned: String = String::from(cow);
assert_eq!(&owned[..], "eggplant");
```

1.21.0

·

Source

§

### impl From<String> for Arc<str>

Source

§

#### fn from(v: String) -> Arc<str>

Allocates a reference-counted `str` and copies `v` into it.

##### §Example

```
let unique: String = "eggplant".to_owned();
let shared: Arc<str> = Arc::from(unique);
assert_eq!("eggplant", &shared[..]);
```

1.6.0

·

Source

§

### impl<'a> From<String> for Box<dyn Error + 'a>

Source

§

#### fn from(str_err: String) -> Box<dyn Error + 'a>

Converts a `String` into a box of dyn `Error`.

##### §Examples

```
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error>::from(a_string_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0

·

Source

§

### impl<'a> From<String> for Box<dyn Error + Sync + Send + 'a>

Source

§

#### fn from(err: String) -> Box<dyn Error + Sync + Send + 'a>

Converts a `String` into a box of dyn `Error` + `Send` + `Sync`.

##### §Examples

```
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_string_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.20.0

·

Source

§

### impl From<String> for Box<str>

Source

§

#### fn from(s: String) -> Box<str>

Converts the given `String` to a boxed `str` slice that is owned.

##### §Examples

```
let s1: String = String::from("hello world");
let s2: Box<str> = Box::from(s1);
let s3: String = String::from(s2);

assert_eq!("hello world", s3)
```

1.0.0

·

Source

§

### impl<'a> From<String> for Cow<'a, str>

Source

§

#### fn from(s: String) -> Cow<'a, str>

Converts a `String` into an `Owned` variant. No heap allocation is performed, and the string is not copied.

##### §Example

```
let s = "eggplant".to_string();
let s2 = "eggplant".to_string();
assert_eq!(Cow::from(s), Cow::<'static, str>::Owned(s2));
```

1.0.0

·

Source

§

### impl From<String> for OsString

Source

§

#### fn from(s: String) -> OsString

Converts a `String` into an `OsString`.

This conversion does not allocate or copy memory.

1.0.0

·

Source

§

### impl From<String> for PathBuf

Source

§

#### fn from(s: String) -> PathBuf

Converts a `String` into a `PathBuf`

This conversion does not allocate or copy memory.

1.21.0

·

Source

§

### impl From<String> for Rc<str>

Source

§

#### fn from(v: String) -> Rc<str>

Allocates a reference-counted string slice and copies `v` into it.

##### §Example

```
let original: String = "statue".to_owned();
let shared: Rc<str> = Rc::from(original);
assert_eq!("statue", &shared[..]);
```

1.14.0

·

Source

§

### impl From<String> for Vec<u8>

Source

§

#### fn from(string: String) -> Vec<u8> ⓘ

Converts the given `String` to a vector `Vec` that holds values of type `u8`.

##### §Examples

```
let s1 = String::from("hello world");
let v1 = Vec::from(s1);

for b in v1 {
    println!("{b}");
}
```

1.46.0

·

Source

§

### impl From<char> for String

Source

§

#### fn from(c: char) -> String

Allocates an owned `String` from a single character.

##### §Example

```
let c: char = 'a';
let s: String = String::from(c);
assert_eq!("a", &s[..]);
```

Source

§

### impl<'a> FromIterator<&'a AsciiChar> for String

Source

§

#### fn from_iter<T>(iter: T) -> Stringwhere T: IntoIterator<Item = &'a AsciiChar>,

Creates a value from an iterator.

Read more

1.17.0

·

Source

§

### impl<'a> FromIterator<&'a char> for String

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = &'a char>,

Creates a value from an iterator.

Read more

1.0.0

·

Source

§

### impl<'a> FromIterator<&'a str> for String

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = &'a str>,

Creates a value from an iterator.

Read more

1.45.0

·

Source

§

### impl<A> FromIterator<Box<str, A>> for Stringwhere A: Allocator,

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = Box<str, A>>,

Creates a value from an iterator.

Read more

Source

§

### impl FromIterator<AsciiChar> for String

Source

§

#### fn from_iter<T>(iter: T) -> Stringwhere T: IntoIterator<Item = AsciiChar>,

Creates a value from an iterator.

Read more

1.19.0

·

Source

§

### impl<'a> FromIterator<Cow<'a, str>> for String

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = Cow<'a, str>>,

Creates a value from an iterator.

Read more

1.80.0

·

Source

§

### impl FromIterator<String> for Box<str>

Source

§

#### fn from_iter<T>(iter: T) -> Box<str>where T: IntoIterator<Item = String>,

Creates a value from an iterator.

Read more

1.12.0

·

Source

§

### impl<'a> FromIterator<String> for Cow<'a, str>

Source

§

#### fn from_iter<I>(it: I) -> Cow<'a, str>where I: IntoIterator<Item = String>,

Creates a value from an iterator.

Read more

1.4.0

·

Source

§

### impl FromIterator<String> for String

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = String>,

Creates a value from an iterator.

Read more

1.0.0

·

Source

§

### impl FromIterator<char> for String

Source

§

#### fn from_iter<I>(iter: I) -> Stringwhere I: IntoIterator<Item = char>,

Creates a value from an iterator.

Read more

1.0.0

·

Source

§

### impl FromStr for String

Source

§

#### type Err = Infallible

The associated error which can be returned from parsing.

Source

§

#### fn from_str(s: &str) -> Result<String, <String as FromStr>::Err>

Parses a string

s

to return a value of this type.

Read more

1.0.0

·

Source

§

### impl Hash for String

Source

§

#### fn hash<H>(&self, hasher: &mut H)where H: Hasher,

Feeds this value into the given

Hasher

.

Read more

1.3.0

·

Source

§

#### fn hash_slice<H>(data: &[Self], state: &mut H)where H: Hasher, Self: Sized,

Feeds a slice of this type into the given

Hasher

.

Read more

1.0.0

·

Source

§

### impl<I> Index<I> for Stringwhere I: SliceIndex<str>,

Source

§

#### type Output = <I as SliceIndex<str>>::Output

The returned type after indexing.

Source

§

#### fn index(&self, index: I) -> &<I as SliceIndex<str>>::Output

Performs the indexing (

container[index]

) operation.

Read more

1.0.0

·

Source

§

### impl<I> IndexMut<I> for Stringwhere I: SliceIndex<str>,

Source

§

#### fn index_mut(&mut self, index: I) -> &mut <I as SliceIndex<str>>::Output

Performs the mutable indexing (

container[index]

) operation.

Read more

1.0.0

·

Source

§

### impl Ord for String

Source

§

#### fn cmp(&self, other: &String) -> Ordering

This method returns an

Ordering

between

self

and

other

.

Read more

1.21.0

·

Source

§

#### fn max(self, other: Self) -> Selfwhere Self: Sized,

Compares and returns the maximum of two values.

Read more

1.21.0

·

Source

§

#### fn min(self, other: Self) -> Selfwhere Self: Sized,

Compares and returns the minimum of two values.

Read more

1.50.0

·

Source

§

#### fn clamp(self, min: Self, max: Self) -> Selfwhere Self: Sized,

Restrict a value to a certain interval.

Read more

1.0.0

·

Source

§

### impl PartialEq<&str> for String

Source

§

#### fn eq(&self, other: &&str) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &&str) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<ByteStr> for String

Source

§

#### fn eq(&self, other: &ByteStr) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<ByteString> for String

Source

§

#### fn eq(&self, other: &ByteString) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq<Cow<'_, str>> for String

Source

§

#### fn eq(&self, other: &Cow<'_, str>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Cow<'_, str>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0

·

Source

§

### impl PartialEq<Path> for String

Source

§

#### fn eq(&self, other: &Path) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0

·

Source

§

### impl PartialEq<PathBuf> for String

Source

§

#### fn eq(&self, other: &PathBuf) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq<String> for &str

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &String) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<String> for ByteStr

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<String> for ByteString

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq<String> for Cow<'_, str>

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &String) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0

·

Source

§

### impl PartialEq<String> for Path

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0

·

Source

§

### impl PartialEq<String> for PathBuf

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq<String> for str

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &String) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq<str> for String

Source

§

#### fn eq(&self, other: &str) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &str) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialEq for String

Source

§

#### fn eq(&self, other: &String) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

1.0.0

·

Source

§

#### fn ne(&self, other: &Rhs) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl PartialOrd for String

Source

§

#### fn partial_cmp(&self, other: &String) -> Option<Ordering>

This method returns an ordering between

self

and

other

values if one exists.

Read more

1.0.0

·

Source

§

#### fn lt(&self, other: &Rhs) -> bool

Tests less than (for

self

and

other

) and is used by the

<

operator.

Read more

1.0.0

·

Source

§

#### fn le(&self, other: &Rhs) -> bool

Tests less than or equal to (for

self

and

other

) and is used by the

<=

operator.

Read more

1.0.0

·

Source

§

#### fn gt(&self, other: &Rhs) -> bool

Tests greater than (for

self

and

other

) and is used by the

>

operator.

Read more

1.0.0

·

Source

§

#### fn ge(&self, other: &Rhs) -> bool

Tests greater than or equal to (for

self

and

other

) and is used by the

>=

operator.

Read more

Source

§

### impl<'b> Pattern for &'b String

A convenience impl that delegates to the impl for `&str`.

#### §Examples

```
assert_eq!(String::from("Hello world").find("world"), Some(6));
```

Source

§

#### type Searcher<'a> = <&'b str as Pattern>::Searcher<'a>

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Associated searcher for this pattern

Source

§

#### fn into_searcher(self, haystack: &str) -> <&'b str as Pattern>::Searcher<'_>

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Constructs the associated searcher from

self

and the

haystack

to search in.

Source

§

#### fn is_contained_in(self, haystack: &str) -> bool

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Checks whether the pattern matches anywhere in the haystack

Source

§

#### fn is_prefix_of(self, haystack: &str) -> bool

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Checks whether the pattern matches at the front of the haystack

Source

§

#### fn strip_prefix_of(self, haystack: &str) -> Option<&str>

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Removes the pattern from the front of haystack, if it matches.

Source

§

#### fn is_suffix_of<'a>(self, haystack: &'a str) -> boolwhere <&'b String as Pattern>::Searcher<'a>: ReverseSearcher<'a>,

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Checks whether the pattern matches at the back of the haystack

Source

§

#### fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>where <&'b String as Pattern>::Searcher<'a>: ReverseSearcher<'a>,

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Removes the pattern from the back of haystack, if it matches.

Source

§

#### fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>>

🔬

This is a nightly-only experimental API. (

pattern

#27721

)

Returns the pattern as utf-8 bytes if possible.

1.16.0

·

Source

§

### impl ToSocketAddrs for String

Source

§

#### type Iter = IntoIter<SocketAddr>

Returned iterator over socket addresses which this type may correspond to.

Source

§

#### fn to_socket_addrs(&self) -> Result<IntoIter<SocketAddr>>

Converts this object to an iterator of resolved

SocketAddr

s.

Read more

Source

§

### impl<'a> TryFrom<&'a ByteStr> for String

Source

§

#### type Error = Utf8Error

The type returned in the event of a conversion error.

Source

§

#### fn try_from( s: &'a ByteStr, ) -> Result<String, <String as TryFrom<&'a ByteStr>>::Error>

Performs the conversion.

Source

§

### impl TryFrom<ByteString> for String

Source

§

#### type Error = FromUtf8Error

The type returned in the event of a conversion error.

Source

§

#### fn try_from( s: ByteString, ) -> Result<String, <String as TryFrom<ByteString>>::Error>

Performs the conversion.

1.85.0

·

Source

§

### impl TryFrom<CString> for String

Source

§

#### fn try_from( value: CString, ) -> Result<String, <String as TryFrom<CString>>::Error>

Converts a `CString` into a `String` if it contains valid UTF-8 data.

This method is equivalent to `CString::into_string`.

Source

§

#### type Error = IntoStringError

The type returned in the event of a conversion error.

1.87.0

·

Source

§

### impl TryFrom<Vec<u8>> for String

Source

§

#### fn try_from( bytes: Vec<u8>, ) -> Result<String, <String as TryFrom<Vec<u8>>>::Error>

Converts the given `Vec<u8>` into a `String` if it contains valid UTF-8 data.

##### §Examples

```
let s1 = b"hello world".to_vec();
let v1 = String::try_from(s1).unwrap();
assert_eq!(v1, "hello world");
```

Source

§

#### type Error = FromUtf8Error

The type returned in the event of a conversion error.

1.0.0

·

Source

§

### impl Write for String

Source

§

#### fn write_str(&mut self, s: &str) -> Result<(), Error>

Writes a string slice into this writer, returning whether the write succeeded.

Read more

Source

§

#### fn write_char(&mut self, c: char) -> Result<(), Error>

Writes a

char

into this writer, returning whether the write succeeded.

Read more

1.0.0

·

Source

§

#### fn write_fmt(&mut self, args: Arguments<'_>) -> Result<(), Error>

Glue for usage of the

write!

macro with implementors of this trait.

Read more

Source

§

### impl DerefPure for String

1.0.0

·

Source

§

### impl Eq for String

1.0.0

·

Source

§

### impl StructuralPartialEq for String


## Auto Trait Implementations

§

### impl Freeze for String

§

### impl RefUnwindSafe for String

§

### impl Send for String

§

### impl Sync for String

§

### impl Unpin for String

§

### impl UnsafeUnpin for String

§

### impl UnwindSafe for String


## Blanket Implementations

Source

§

### impl<T> Any for Twhere T: 'static + ?Sized,

Source

§

#### fn type_id(&self) -> TypeId

Gets the

TypeId

of

self

.

Read more

Source

§

### impl<T> Borrow<T> for Twhere T: ?Sized,

Source

§

#### fn borrow(&self) -> &T

Immutably borrows from an owned value.

Read more

Source

§

### impl<T> BorrowMut<T> for Twhere T: ?Sized,

Source

§

#### fn borrow_mut(&mut self) -> &mut T

Mutably borrows from an owned value.

Read more

Source

§

### impl<T> CloneToUninit for Twhere T: Clone,

Source

§

#### unsafe fn clone_to_uninit(&self, dest: *mut u8)

🔬

This is a nightly-only experimental API. (

clone_to_uninit

#126799

)

Performs copy-assignment from

self

to

dest

.

Read more

Source

§

### impl<T> From<T> for T

Source

§

#### fn from(t: T) -> T

Returns the argument unchanged.

Source

§

### impl<T, U> Into<U> for Twhere U: From<T>,

Source

§

#### fn into(self) -> U

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of `From<T> for U` chooses to do.

Source

§

### impl<P, T> Receiver for Pwhere P: Deref<Target = T> + ?Sized, T: ?Sized,

Source

§

#### type Target = T

🔬

This is a nightly-only experimental API. (

arbitrary_self_types

#44874

)

The target type on which the method may be called.

Source

§

### impl<T> ToOwned for Twhere T: Clone,

Source

§

#### type Owned = T

The resulting type after obtaining ownership.

Source

§

#### fn to_owned(&self) -> T

Creates owned data from borrowed data, usually by cloning.

Read more

Source

§

#### fn clone_into(&self, target: &mut T)

Uses borrowed data to replace owned data, usually by cloning.

Read more

Source

§

### impl<T> ToString for Twhere T: Display + ?Sized,

Source

§

#### fn to_string(&self) -> String

Converts the given value to a

String

.

Read more

Source

§

### impl<T, U> TryFrom<U> for Twhere U: Into<T>,

Source

§

#### type Error = Infallible

The type returned in the event of a conversion error.

Source

§

#### fn try_from(value: U) -> Result<T, <T as TryFrom<U>>::Error>

Performs the conversion.

Source

§

### impl<T, U> TryInto<U> for Twhere U: TryFrom<T>,

Source

§

#### type Error = <U as TryFrom<T>>::Error

The type returned in the event of a conversion error.

Source

§

#### fn try_into(self) -> Result<U, <U as TryFrom<T>>::Error>

Performs the conversion.
