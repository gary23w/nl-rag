---
title: "Vec in std::vec (part 7/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 7/7
---

## Trait Implementations

1.5.0

·

Source

§

### impl<T, A> AsMut<[T]> for Vec<T, A>where A: Allocator,

Source

§

#### fn as_mut(&mut self) -> &mut [T]

Converts this type into a mutable reference of the (usually inferred) input type.

1.5.0

·

Source

§

### impl<T, A> AsMut<Vec<T, A>> for Vec<T, A>where A: Allocator,

Source

§

#### fn as_mut(&mut self) -> &mut Vec<T, A>

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl<T, A> AsRef<[T]> for Vec<T, A>where A: Allocator,

Source

§

#### fn as_ref(&self) -> &[T]

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl<T, A> AsRef<Vec<T, A>> for Vec<T, A>where A: Allocator,

Source

§

#### fn as_ref(&self) -> &Vec<T, A>

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0

·

Source

§

### impl<T, A> Borrow<[T]> for Vec<T, A>where A: Allocator,

Source

§

#### fn borrow(&self) -> &[T]

Immutably borrows from an owned value.

Read more

1.0.0

·

Source

§

### impl<T, A> BorrowMut<[T]> for Vec<T, A>where A: Allocator,

Source

§

#### fn borrow_mut(&mut self) -> &mut [T]

Mutably borrows from an owned value.

Read more

1.0.0

·

Source

§

### impl<T, A> Clone for Vec<T, A>where T: Clone, A: Allocator + Clone,

Source

§

#### fn clone_from(&mut self, source: &Vec<T, A>)

Overwrites the contents of `self` with a clone of the contents of `source`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible. Additionally, if the element type `T` overrides `clone_from()`, this will reuse the resources of `self`’s elements as well.

##### §Examples

```
let x = vec![5, 6, 7];
let mut y = vec![8, 9, 10];
let yp: *const i32 = y.as_ptr();

y.clone_from(&x);

assert_eq!(x, y);

assert_eq!(yp, y.as_ptr());
```

Source

§

#### fn clone(&self) -> Vec<T, A>

Returns a duplicate of the value.

Read more

1.0.0

·

Source

§

### impl<T, A> Debug for Vec<T, A>where T: Debug, A: Allocator,

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

### impl<T> Default for Vec<T>

Source

§

#### fn default() -> Vec<T>

Creates an empty `Vec<T>`.

The vector will not allocate until elements are pushed onto it.

1.0.0

·

Source

§

### impl<T, A> Deref for Vec<T, A>where A: Allocator,

Source

§

#### type Target = [T]

The resulting type after dereferencing.

Source

§

#### fn deref(&self) -> &[T]

Dereferences the value.

1.0.0

·

Source

§

### impl<T, A> DerefMut for Vec<T, A>where A: Allocator,

Source

§

#### fn deref_mut(&mut self) -> &mut [T]

Mutably dereferences the value.

1.0.0

·

Source

§

### impl<T, A> Drop for Vec<T, A>where A: Allocator,

Source

§

#### fn drop(&mut self)

Executes the destructor for this type.

Read more

1.2.0

·

Source

§

### impl<'a, T, A> Extend<&'a T> for Vec<T, A>where T: Copy + 'a, A: Allocator,

Extend implementation that copies elements out of references before pushing them onto the Vec.

This implementation is specialized for slice iterators, where it uses `copy_from_slice` to append the entire slice at once.

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = &'a T>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, _: &'a T)

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

### impl<T, A> Extend<T> for Vec<T, A>where A: Allocator,

Source

§

#### fn extend<I>(&mut self, iter: I)where I: IntoIterator<Item = T>,

Extends a collection with the contents of an iterator.

Read more

Source

§

#### fn extend_one(&mut self, item: T)

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

### impl<T> From<&[T]> for Vec<T>where T: Clone,

Source

§

#### fn from(s: &[T]) -> Vec<T>

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### §Examples

```
assert_eq!(Vec::from(&[1, 2, 3][..]), vec![1, 2, 3]);
```

1.74.0

·

Source

§

### impl<T, const N: usize> From<&[T; N]> for Vec<T>where T: Clone,

Source

§

#### fn from(s: &[T; N]) -> Vec<T>

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### §Examples

```
assert_eq!(Vec::from(&[1, 2, 3]), vec![1, 2, 3]);
```

1.28.0

·

Source

§

### impl<'a, T> From<&'a Vec<T>> for Cow<'a, [T]>where T: Clone,

Source

§

#### fn from(v: &'a Vec<T>) -> Cow<'a, [T]>

Creates a `Borrowed` variant of `Cow` from a reference to `Vec`.

This conversion does not allocate or clone the data.

1.19.0

·

Source

§

### impl<T> From<&mut [T]> for Vec<T>where T: Clone,

Source

§

#### fn from(s: &mut [T]) -> Vec<T>

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### §Examples

```
assert_eq!(Vec::from(&mut [1, 2, 3][..]), vec![1, 2, 3]);
```

1.74.0

·

Source

§

### impl<T, const N: usize> From<&mut [T; N]> for Vec<T>where T: Clone,

Source

§

#### fn from(s: &mut [T; N]) -> Vec<T>

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### §Examples

```
assert_eq!(Vec::from(&mut [1, 2, 3]), vec![1, 2, 3]);
```

1.0.0

·

Source

§

### impl From<&str> for Vec<u8>

Source

§

#### fn from(s: &str) -> Vec<u8> ⓘ

Allocates a `Vec<u8>` and fills it with a UTF-8 string.

##### §Examples

```
assert_eq!(Vec::from("123"), vec![b'1', b'2', b'3']);
```

1.44.0

·

Source

§

### impl<T, const N: usize> From<[T; N]> for Vec<T>

Source

§

#### fn from(s: [T; N]) -> Vec<T>

Allocates a `Vec<T>` and moves `s`’s items into it.

##### §Examples

```
assert_eq!(Vec::from([1, 2, 3]), vec![1, 2, 3]);
```

1.5.0

·

Source

§

### impl<T, A> From<BinaryHeap<T, A>> for Vec<T, A>where A: Allocator,

Source

§

#### fn from(heap: BinaryHeap<T, A>) -> Vec<T, A>

Converts a `BinaryHeap<T>` into a `Vec<T>`.

This conversion requires no data movement or allocation, and has constant time complexity.

1.18.0

·

Source

§

### impl<T, A> From<Box<[T], A>> for Vec<T, A>where A: Allocator,

Source

§

#### fn from(s: Box<[T], A>) -> Vec<T, A>

Converts a boxed slice into a vector by transferring ownership of the existing heap allocation.

##### §Examples

```
let b: Box<[i32]> = vec![1, 2, 3].into_boxed_slice();
assert_eq!(Vec::from(b), vec![1, 2, 3]);
```

Source

§

### impl From<ByteString> for Vec<u8>

Source

§

#### fn from(s: ByteString) -> Vec<u8> ⓘ

Converts to this type from the input type.

1.7.0

·

Source

§

### impl From<CString> for Vec<u8>

Source

§

#### fn from(s: CString) -> Vec<u8> ⓘ

Converts a `CString` into a `Vec<u8>`.

The conversion consumes the `CString`, and removes the terminating NUL byte.

1.14.0

·

Source

§

### impl<'a, T> From<Cow<'a, [T]>> for Vec<T>where [T]: ToOwned<Owned = Vec<T>>,

Source

§

#### fn from(s: Cow<'a, [T]>) -> Vec<T>

Converts a clone-on-write slice into a vector.

If `s` already owns a `Vec<T>`, it will be returned directly. If `s` is borrowing a slice, a new `Vec<T>` will be allocated and filled by cloning `s`’s items into it.

##### §Examples

```
let o: Cow<'_, [i32]> = Cow::Owned(vec![1, 2, 3]);
let b: Cow<'_, [i32]> = Cow::Borrowed(&[1, 2, 3]);
assert_eq!(Vec::from(o), Vec::from(b));
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

1.43.0

·

Source

§

### impl From<Vec<NonZero<u8>>> for CString

Source

§

#### fn from(v: Vec<NonZero<u8>>) -> CString

Converts a `Vec<NonZero<u8>>` into a `CString` without copying nor checking for inner nul bytes.

1.8.0

·

Source

§

### impl<'a, T> From<Vec<T>> for Cow<'a, [T]>where T: Clone,

Source

§

#### fn from(v: Vec<T>) -> Cow<'a, [T]>

Creates an `Owned` variant of `Cow` from an owned instance of `Vec`.

This conversion does not allocate or clone the data.

1.21.0

·

Source

§

### impl<T, A> From<Vec<T, A>> for Arc<[T], A>where A: Allocator + Clone,

Source

§

#### fn from(v: Vec<T, A>) -> Arc<[T], A>

Allocates a reference-counted slice and moves `v`’s items into it.

##### §Example

```
let unique: Vec<i32> = vec![1, 2, 3];
let shared: Arc<[i32]> = Arc::from(unique);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.5.0

·

Source

§

### impl<T, A> From<Vec<T, A>> for BinaryHeap<T, A>where T: Ord, A: Allocator,

Source

§

#### fn from(vec: Vec<T, A>) -> BinaryHeap<T, A>

Converts a `Vec<T>` into a `BinaryHeap<T>`.

This conversion happens in-place, and has *O*(*n*) time complexity.

1.20.0

·

Source

§

### impl<T, A> From<Vec<T, A>> for Box<[T], A>where A: Allocator,

Source

§

#### fn from(v: Vec<T, A>) -> Box<[T], A>

Converts a vector into a boxed slice.

Before doing the conversion, this method discards excess capacity like `Vec::shrink_to_fit`.

##### §Examples

```
assert_eq!(Box::from(vec![1, 2, 3]), vec![1, 2, 3].into_boxed_slice());
```

Any excess capacity is removed:

```
let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);

assert_eq!(Box::from(vec), vec![1, 2, 3].into_boxed_slice());
```

1.21.0

·

Source

§

### impl<T, A> From<Vec<T, A>> for Rc<[T], A>where A: Allocator,

Source

§

#### fn from(v: Vec<T, A>) -> Rc<[T], A>

Allocates a reference-counted slice and moves `v`’s items into it.

##### §Example

```
let unique: Vec<i32> = vec![1, 2, 3];
let shared: Rc<[i32]> = Rc::from(unique);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.10.0

·

Source

§

### impl<T, A> From<Vec<T, A>> for VecDeque<T, A>where A: Allocator,

Source

§

#### fn from(other: Vec<T, A>) -> VecDeque<T, A>

Turn a `Vec<T>` into a `VecDeque<T>`.

This conversion is guaranteed to run in *O*(1) time and to not re-allocate the `Vec`’s buffer or allocate any additional memory.

1.10.0

·

Source

§

### impl<T, A> From<VecDeque<T, A>> for Vec<T, A>where A: Allocator,

Source

§

#### fn from(other: VecDeque<T, A>) -> Vec<T, A>

Turn a `VecDeque<T>` into a `Vec<T>`.

This never needs to re-allocate, but does need to do *O*(*n*) data movement if the circular buffer doesn’t happen to be at the beginning of the allocation.

##### §Examples

```
use std::collections::VecDeque;

let deque: VecDeque<_> = (1..5).collect();
let ptr = deque.as_slices().0.as_ptr();
let vec = Vec::from(deque);
assert_eq!(vec, [1, 2, 3, 4]);
assert_eq!(vec.as_ptr(), ptr);

let mut deque: VecDeque<_> = (1..5).collect();
deque.push_front(9);
deque.push_front(8);
let ptr = deque.as_slices().1.as_ptr();
let vec = Vec::from(deque);
assert_eq!(vec, [8, 9, 1, 2, 3, 4]);
assert_eq!(vec.as_ptr(), ptr);
```

1.0.0

·

Source

§

### impl<T> FromIterator<T> for Vec<T>

Collects an iterator into a Vec, commonly called via `Iterator::collect()`

#### §Allocation behavior

In general `Vec` does not guarantee any particular growth or allocation strategy. That also applies to this trait impl.

**Note:** This section covers implementation details and is therefore exempt from stability guarantees.

Vec may use any or none of the following strategies, depending on the supplied iterator:

- preallocate based on `Iterator::size_hint()`
  - and panic if the number of items is outside the provided lower/upper bounds
- use an amortized growth strategy similar to `pushing` one item at a time
- perform the iteration in-place on the original allocation backing the iterator

The last case warrants some attention. It is an optimization that in many cases reduces peak memory consumption and improves cache locality. But when big, short-lived allocations are created, only a small fraction of their items get collected, no further use is made of the spare capacity and the resulting `Vec` is moved into a longer-lived structure, then this can lead to the large allocations having their lifetimes unnecessarily extended which can result in increased memory footprint.

In cases where this is an issue, the excess capacity can be discarded with `Vec::shrink_to()`, `Vec::shrink_to_fit()` or by collecting into `Box<[T]>` instead, which additionally reduces the size of the long-lived struct.

```
static LONG_LIVED: Mutex<Vec<Vec<u16>>> = Mutex::new(Vec::new());

for i in 0..10 {
    let big_temporary: Vec<u16> = (0..1024).collect();
    let mut result: Vec<_> = big_temporary.into_iter().filter(|i| i % 100 == 0).collect();
    result.shrink_to_fit();
    LONG_LIVED.lock().unwrap().push(result);
}
```

Source

§

#### fn from_iter<I>(iter: I) -> Vec<T>where I: IntoIterator<Item = T>,

Creates a value from an iterator.

Read more

1.0.0

·

Source

§

### impl<T, A> Hash for Vec<T, A>where T: Hash, A: Allocator,

The hash of a vector is the same as that of the corresponding slice, as required by the `core::borrow::Borrow` implementation.

```
use std::hash::BuildHasher;

let b = std::hash::RandomState::new();
let v: Vec<u8> = vec![0xa8, 0x3c, 0x09];
let s: &[u8] = &[0xa8, 0x3c, 0x09];
assert_eq!(b.hash_one(v), b.hash_one(s));
```

Source

§

#### fn hash<H>(&self, state: &mut H)where H: Hasher,

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

### impl<T, I, A> Index<I> for Vec<T, A>where I: SliceIndex<[T]>, A: Allocator,

Source

§

#### type Output = <I as SliceIndex<[T]>>::Output

The returned type after indexing.

Source

§

#### fn index(&self, index: I) -> &<Vec<T, A> as Index<I>>::Output ⓘ

Performs the indexing (

container[index]

) operation.

Read more

1.0.0

·

Source

§

### impl<T, I, A> IndexMut<I> for Vec<T, A>where I: SliceIndex<[T]>, A: Allocator,

Source

§

#### fn index_mut(&mut self, index: I) -> &mut <Vec<T, A> as Index<I>>::Output ⓘ

Performs the mutable indexing (

container[index]

) operation.

Read more

1.0.0

·

Source

§

### impl<'a, T, A> IntoIterator for &'a Vec<T, A>where A: Allocator,

Source

§

#### type Item = &'a T

The type of the elements being iterated over.

Source

§

#### type IntoIter = Iter<'a, T>

Which kind of iterator are we turning this into?

Source

§

#### fn into_iter(self) -> <&'a Vec<T, A> as IntoIterator>::IntoIter ⓘ

Creates an iterator from a value.

Read more

1.0.0

·

Source

§

### impl<'a, T, A> IntoIterator for &'a mut Vec<T, A>where A: Allocator,

Source

§

#### type Item = &'a mut T

The type of the elements being iterated over.

Source

§

#### type IntoIter = IterMut<'a, T>

Which kind of iterator are we turning this into?

Source

§

#### fn into_iter(self) -> <&'a mut Vec<T, A> as IntoIterator>::IntoIter ⓘ

Creates an iterator from a value.

Read more

1.0.0

·

Source

§

### impl<T, A> IntoIterator for Vec<T, A>where A: Allocator,

Source

§

#### fn into_iter(self) -> <Vec<T, A> as IntoIterator>::IntoIter ⓘ

Creates a consuming iterator, that is, one that moves each value out of the vector (from start to end). The vector cannot be used after calling this.

##### §Examples

```
let v = vec!["a".to_string(), "b".to_string()];
let mut v_iter = v.into_iter();

let first_element: Option<String> = v_iter.next();

assert_eq!(first_element, Some("a".to_string()));
assert_eq!(v_iter.next(), Some("b".to_string()));
assert_eq!(v_iter.next(), None);
```

Source

§

#### type Item = T

The type of the elements being iterated over.

Source

§

#### type IntoIter = IntoIter<T, A>

Which kind of iterator are we turning this into?

1.0.0

·

Source

§

### impl<T, A> Ord for Vec<T, A>where T: Ord, A: Allocator,

Implements ordering of vectors, lexicographically.

Source

§

#### fn cmp(&self, other: &Vec<T, A>) -> Ordering

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

### impl<T, U, A> PartialEq<&[U]> for Vec<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &&[U]) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &&[U]) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl<T, U, A, const N: usize> PartialEq<&[U; N]> for Vec<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &&[U; N]) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &&[U; N]) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl<T, U, A> PartialEq<&mut [U]> for Vec<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &&mut [U]) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &&mut [U]) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.48.0

·

Source

§

### impl<T, U, A> PartialEq<[U]> for Vec<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &[U]) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &[U]) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl<T, U, A, const N: usize> PartialEq<[U; N]> for Vec<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &[U; N]) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &[U; N]) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<ByteStr> for Vec<u8>

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

### impl PartialEq<ByteString> for Vec<u8>

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

1.46.0

·

Source

§

### impl<T, U, A> PartialEq<Vec<U, A>> for &[T]where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &Vec<U, A>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Vec<U, A>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.46.0

·

Source

§

### impl<T, U, A> PartialEq<Vec<U, A>> for &mut [T]where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &Vec<U, A>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Vec<U, A>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.48.0

·

Source

§

### impl<T, U, A> PartialEq<Vec<U, A>> for [T]where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &Vec<U, A>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Vec<U, A>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0

·

Source

§

### impl<T, U, A> PartialEq<Vec<U, A>> for Cow<'_, [T]>where A: Allocator, T: PartialEq<U> + Clone,

Source

§

#### fn eq(&self, other: &Vec<U, A>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Vec<U, A>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0

·

Source

§

### impl<T, U, A> PartialEq<Vec<U, A>> for VecDeque<T, A>where A: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &Vec<U, A>) -> bool

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

### impl<T, U, A1, A2> PartialEq<Vec<U, A2>> for Vec<T, A1>where A1: Allocator, A2: Allocator, T: PartialEq<U>,

Source

§

#### fn eq(&self, other: &Vec<U, A2>) -> bool

Tests for

self

and

other

values to be equal, and is used by

==

.

Source

§

#### fn ne(&self, other: &Vec<U, A2>) -> bool

Tests for

!=

. The default implementation is almost always sufficient, and should not be overridden without very good reason.

Source

§

### impl PartialEq<Vec<u8>> for ByteStr

Source

§

#### fn eq(&self, other: &Vec<u8>) -> bool

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

### impl PartialEq<Vec<u8>> for ByteString

Source

§

#### fn eq(&self, other: &Vec<u8>) -> bool

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

### impl<T, A1, A2> PartialOrd<Vec<T, A2>> for Vec<T, A1>where T: PartialOrd, A1: Allocator, A2: Allocator,

Implements comparison of vectors, lexicographically.

Source

§

#### fn partial_cmp(&self, other: &Vec<T, A2>) -> Option<Ordering>

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

1.66.0

·

Source

§

### impl<T, const N: usize> TryFrom<Vec<T>> for Box<[T; N]>

Source

§

#### fn try_from( vec: Vec<T>, ) -> Result<Box<[T; N]>, <Box<[T; N]> as TryFrom<Vec<T>>>::Error>

Attempts to convert a `Vec<T>` into a `Box<[T; N]>`.

Like `Vec::into_boxed_slice`, this is in-place if `vec.capacity() == N`, but will require a reallocation otherwise.

##### §Errors

Returns the original `Vec<T>` in the `Err` variant if `boxed_slice.len()` does not equal `N`.

##### §Examples

This can be used with `vec!` to create an array on the heap:

```
let state: Box<[f32; 100]> = vec![1.0; 100].try_into().unwrap();
assert_eq!(state.len(), 100);
```

Source

§

#### type Error = Vec<T>

The type returned in the event of a conversion error.

1.48.0

·

Source

§

### impl<T, A, const N: usize> TryFrom<Vec<T, A>> for [T; N]where A: Allocator,

Source

§

#### fn try_from(vec: Vec<T, A>) -> Result<[T; N], Vec<T, A>>

Gets the entire contents of the `Vec<T>` as an array, if its size exactly matches that of the requested array.

##### §Examples

```
assert_eq!(vec![1, 2, 3].try_into(), Ok([1, 2, 3]));
assert_eq!(<Vec<i32>>::new().try_into(), Ok([]));
```

If the length doesn’t match, the input comes back in `Err`:

```
let r: Result<[i32; 4], _> = (0..10).collect::<Vec<_>>().try_into();
assert_eq!(r, Err(vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
```

If you’re fine with just getting a prefix of the `Vec<T>`, you can call `.truncate(N)` first.

```
let mut v = String::from("hello world").into_bytes();
v.sort();
v.truncate(2);
let [a, b]: [_; 2] = v.try_into().unwrap();
assert_eq!(a, b' ');
assert_eq!(b, b'd');
```

Source

§

#### type Error = Vec<T, A>

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

### impl<A: Allocator> Write for Vec<u8, A>

Write is implemented for `Vec<u8>` by appending to the vector. The vector will grow as needed.

Source

§

#### fn write(&mut self, buf: &[u8]) -> Result<usize>

Writes a buffer into this writer, returning how many bytes were written.

Read more

Source

§

#### fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> Result<usize>

Like

write

, except that it writes from a slice of buffers.

Read more

Source

§

#### fn is_write_vectored(&self) -> bool

🔬

This is a nightly-only experimental API. (

can_vector

#69941

)

Determines if this

Write

r has an efficient

write_vectored

implementation.

Read more

Source

§

#### fn write_all(&mut self, buf: &[u8]) -> Result<()>

Attempts to write an entire buffer into this writer.

Read more

Source

§

#### fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> Result<()>

🔬

This is a nightly-only experimental API. (

write_all_vectored

#70436

)

Attempts to write multiple buffers into this writer.

Read more

Source

§

#### fn flush(&mut self) -> Result<()>

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination.

Read more

1.0.0

·

Source

§

#### fn write_fmt(&mut self, args: Arguments<'_>) -> Result<()>

Writes a formatted string into this writer, returning any error encountered.

Read more

1.0.0

·

Source

§

#### fn by_ref(&mut self) -> &mut Selfwhere Self: Sized,

Creates a “by reference” adapter for this instance of

Write

.

Read more

Source

§

### impl<T, A> DerefPure for Vec<T, A>where A: Allocator,

1.0.0

·

Source

§

### impl<T, A> Eq for Vec<T, A>where T: Eq, A: Allocator,


## Auto Trait Implementations

§

### impl<T, A> Freeze for Vec<T, A>where A: Freeze,

§

### impl<T, A> RefUnwindSafe for Vec<T, A>where A: RefUnwindSafe, T: RefUnwindSafe,

§

### impl<T, A> Send for Vec<T, A>where A: Send, T: Send,

§

### impl<T, A> Sync for Vec<T, A>where A: Sync, T: Sync,

§

### impl<T, A> Unpin for Vec<T, A>where A: Unpin, T: Unpin,

§

### impl<T, A> UnsafeUnpin for Vec<T, A>where A: UnsafeUnpin,

§

### impl<T, A> UnwindSafe for Vec<T, A>where A: UnwindSafe, T: UnwindSafe,


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
