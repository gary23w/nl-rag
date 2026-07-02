---
title: "Vec in std::vec (part 4/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 4/7
---

## Methods from Deref<Target = [T]>

1.0.0

·

Source

#### pub fn len(&self) -> usize

Returns the number of elements in the slice.

##### §Examples

```
let a = [1, 2, 3];
assert_eq!(a.len(), 3);
```

1.0.0

·

Source

#### pub fn is_empty(&self) -> bool

Returns `true` if the slice has a length of 0.

##### §Examples

```
let a = [1, 2, 3];
assert!(!a.is_empty());

let b: &[i32] = &[];
assert!(b.is_empty());
```

1.0.0

·

Source

#### pub fn first(&self) -> Option<&T>

Returns the first element of the slice, or `None` if it is empty.

##### §Examples

```
let v = [10, 40, 30];
assert_eq!(Some(&10), v.first());

let w: &[i32] = &[];
assert_eq!(None, w.first());
```

1.0.0

·

Source

#### pub fn first_mut(&mut self) -> Option<&mut T>

Returns a mutable reference to the first element of the slice, or `None` if it is empty.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some(first) = x.first_mut() {
    *first = 5;
}
assert_eq!(x, &[5, 1, 2]);

let y: &mut [i32] = &mut [];
assert_eq!(None, y.first_mut());
```

1.5.0

·

Source

#### pub fn split_first(&self) -> Option<(&T, &[T])>

Returns the first and all the rest of the elements of the slice, or `None` if it is empty.

##### §Examples

```
let x = &[0, 1, 2];

if let Some((first, elements)) = x.split_first() {
    assert_eq!(first, &0);
    assert_eq!(elements, &[1, 2]);
}
```

1.5.0

·

Source

#### pub fn split_first_mut(&mut self) -> Option<(&mut T, &mut [T])>

Returns the first and all the rest of the elements of the slice, or `None` if it is empty.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some((first, elements)) = x.split_first_mut() {
    *first = 3;
    elements[0] = 4;
    elements[1] = 5;
}
assert_eq!(x, &[3, 4, 5]);
```

1.5.0

·

Source

#### pub fn split_last(&self) -> Option<(&T, &[T])>

Returns the last and all the rest of the elements of the slice, or `None` if it is empty.

##### §Examples

```
let x = &[0, 1, 2];

if let Some((last, elements)) = x.split_last() {
    assert_eq!(last, &2);
    assert_eq!(elements, &[0, 1]);
}
```

1.5.0

·

Source

#### pub fn split_last_mut(&mut self) -> Option<(&mut T, &mut [T])>

Returns the last and all the rest of the elements of the slice, or `None` if it is empty.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some((last, elements)) = x.split_last_mut() {
    *last = 3;
    elements[0] = 4;
    elements[1] = 5;
}
assert_eq!(x, &[4, 5, 3]);
```

1.0.0

·

Source

#### pub fn last(&self) -> Option<&T>

Returns the last element of the slice, or `None` if it is empty.

##### §Examples

```
let v = [10, 40, 30];
assert_eq!(Some(&30), v.last());

let w: &[i32] = &[];
assert_eq!(None, w.last());
```

1.0.0

·

Source

#### pub fn last_mut(&mut self) -> Option<&mut T>

Returns a mutable reference to the last item in the slice, or `None` if it is empty.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some(last) = x.last_mut() {
    *last = 10;
}
assert_eq!(x, &[0, 1, 10]);

let y: &mut [i32] = &mut [];
assert_eq!(None, y.last_mut());
```

1.77.0

·

Source

#### pub fn first_chunk<const N: usize>(&self) -> Option<&[T; N]>

Returns an array reference to the first `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let u = [10, 40, 30];
assert_eq!(Some(&[10, 40]), u.first_chunk::<2>());

let v: &[i32] = &[10];
assert_eq!(None, v.first_chunk::<2>());

let w: &[i32] = &[];
assert_eq!(Some(&[]), w.first_chunk::<0>());
```

1.77.0

·

Source

#### pub fn first_chunk_mut<const N: usize>(&mut self) -> Option<&mut [T; N]>

Returns a mutable array reference to the first `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some(first) = x.first_chunk_mut::<2>() {
    first[0] = 5;
    first[1] = 4;
}
assert_eq!(x, &[5, 4, 2]);

assert_eq!(None, x.first_chunk_mut::<4>());
```

1.77.0

·

Source

#### pub fn split_first_chunk<const N: usize>(&self) -> Option<(&[T; N], &[T])>

Returns an array reference to the first `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &[0, 1, 2];

if let Some((first, elements)) = x.split_first_chunk::<2>() {
    assert_eq!(first, &[0, 1]);
    assert_eq!(elements, &[2]);
}

assert_eq!(None, x.split_first_chunk::<4>());
```

1.77.0

·

Source

#### pub fn split_first_chunk_mut<const N: usize>( &mut self, ) -> Option<(&mut [T; N], &mut [T])>

Returns a mutable array reference to the first `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some((first, elements)) = x.split_first_chunk_mut::<2>() {
    first[0] = 3;
    first[1] = 4;
    elements[0] = 5;
}
assert_eq!(x, &[3, 4, 5]);

assert_eq!(None, x.split_first_chunk_mut::<4>());
```

1.77.0

·

Source

#### pub fn split_last_chunk<const N: usize>(&self) -> Option<(&[T], &[T; N])>

Returns an array reference to the last `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &[0, 1, 2];

if let Some((elements, last)) = x.split_last_chunk::<2>() {
    assert_eq!(elements, &[0]);
    assert_eq!(last, &[1, 2]);
}

assert_eq!(None, x.split_last_chunk::<4>());
```

1.77.0

·

Source

#### pub fn split_last_chunk_mut<const N: usize>( &mut self, ) -> Option<(&mut [T], &mut [T; N])>

Returns a mutable array reference to the last `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some((elements, last)) = x.split_last_chunk_mut::<2>() {
    last[0] = 3;
    last[1] = 4;
    elements[0] = 5;
}
assert_eq!(x, &[5, 3, 4]);

assert_eq!(None, x.split_last_chunk_mut::<4>());
```

1.77.0

·

Source

#### pub fn last_chunk<const N: usize>(&self) -> Option<&[T; N]>

Returns an array reference to the last `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let u = [10, 40, 30];
assert_eq!(Some(&[40, 30]), u.last_chunk::<2>());

let v: &[i32] = &[10];
assert_eq!(None, v.last_chunk::<2>());

let w: &[i32] = &[];
assert_eq!(Some(&[]), w.last_chunk::<0>());
```

1.77.0

·

Source

#### pub fn last_chunk_mut<const N: usize>(&mut self) -> Option<&mut [T; N]>

Returns a mutable array reference to the last `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some(last) = x.last_chunk_mut::<2>() {
    last[0] = 10;
    last[1] = 20;
}
assert_eq!(x, &[0, 10, 20]);

assert_eq!(None, x.last_chunk_mut::<4>());
```

1.0.0

·

Source

#### pub fn get<I>(&self, index: I) -> Option<&<I as SliceIndex<[T]>>::Output>where I: SliceIndex<[T]>,

Returns a reference to an element or subslice depending on the type of index.

- If given a position, returns a reference to the element at that position or `None` if out of bounds.
- If given a range, returns the subslice corresponding to that range, or `None` if out of bounds.

##### §Examples

```
let v = [10, 40, 30];
assert_eq!(Some(&40), v.get(1));
assert_eq!(Some(&[10, 40][..]), v.get(0..2));
assert_eq!(None, v.get(3));
assert_eq!(None, v.get(0..4));
```

1.0.0

·

Source

#### pub fn get_mut<I>( &mut self, index: I, ) -> Option<&mut <I as SliceIndex<[T]>>::Output>where I: SliceIndex<[T]>,

Returns a mutable reference to an element or subslice depending on the type of index (see `get`) or `None` if the index is out of bounds.

##### §Examples

```
let x = &mut [0, 1, 2];

if let Some(elem) = x.get_mut(1) {
    *elem = 42;
}
assert_eq!(x, &[0, 42, 2]);
```

1.0.0

·

Source

#### pub unsafe fn get_unchecked<I>( &self, index: I, ) -> &<I as SliceIndex<[T]>>::Outputwhere I: SliceIndex<[T]>,

Returns a reference to an element or subslice, without doing bounds checking.

For a safe alternative see `get`.

##### §Safety

Calling this method with an out-of-bounds index is *undefined behavior* even if the resulting reference is not used.

You can think of this like `.get(index).unwrap_unchecked()`. It’s UB to call `.get_unchecked(len)`, even if you immediately convert to a pointer. And it’s UB to call `.get_unchecked(..len + 1)`, `.get_unchecked(..=len)`, or similar.

##### §Examples

```
let x = &[1, 2, 4];

unsafe {
    assert_eq!(x.get_unchecked(1), &2);
}
```

1.0.0

·

Source

#### pub unsafe fn get_unchecked_mut<I>( &mut self, index: I, ) -> &mut <I as SliceIndex<[T]>>::Outputwhere I: SliceIndex<[T]>,

Returns a mutable reference to an element or subslice, without doing bounds checking.

For a safe alternative see `get_mut`.

##### §Safety

Calling this method with an out-of-bounds index is *undefined behavior* even if the resulting reference is not used.

You can think of this like `.get_mut(index).unwrap_unchecked()`. It’s UB to call `.get_unchecked_mut(len)`, even if you immediately convert to a pointer. And it’s UB to call `.get_unchecked_mut(..len + 1)`, `.get_unchecked_mut(..=len)`, or similar.

##### §Examples

```
let x = &mut [1, 2, 4];

unsafe {
    let elem = x.get_unchecked_mut(1);
    *elem = 13;
}
assert_eq!(x, &[1, 13, 4]);
```

1.0.0

·

Source

#### pub fn as_ptr(&self) -> *const T

Returns a raw pointer to the slice’s buffer.

The caller must ensure that the slice outlives the pointer this function returns, or else it will end up dangling.

The caller must also ensure that the memory the pointer (non-transitively) points to is never written to (except inside an `UnsafeCell`) using this pointer or any pointer derived from it. If you need to mutate the contents of the slice, use `as_mut_ptr`.

Modifying the container referenced by this slice may cause its buffer to be reallocated, which would also make any pointers to it invalid.

##### §Examples

```
let x = &[1, 2, 4];
let x_ptr = x.as_ptr();

unsafe {
    for i in 0..x.len() {
        assert_eq!(x.get_unchecked(i), &*x_ptr.add(i));
    }
}
```

1.0.0

·

Source

#### pub fn as_mut_ptr(&mut self) -> *mut T

Returns an unsafe mutable pointer to the slice’s buffer.

The caller must ensure that the slice outlives the pointer this function returns, or else it will end up dangling.

Modifying the container referenced by this slice may cause its buffer to be reallocated, which would also make any pointers to it invalid.

##### §Examples

```
let x = &mut [1, 2, 4];
let x_ptr = x.as_mut_ptr();

unsafe {
    for i in 0..x.len() {
        *x_ptr.add(i) += 2;
    }
}
assert_eq!(x, &[3, 4, 6]);
```

1.48.0

·

Source

#### pub fn as_ptr_range(&self) -> Range<*const T> ⓘ

Returns the two raw pointers spanning the slice.

The returned range is half-open, which means that the end pointer points *one past* the last element of the slice. This way, an empty slice is represented by two equal pointers, and the difference between the two pointers represents the size of the slice.

See `as_ptr` for warnings on using these pointers. The end pointer requires extra caution, as it does not point to a valid element in the slice.

This function is useful for interacting with foreign interfaces which use two pointers to refer to a range of elements in memory, as is common in C++.

It can also be useful to check if a pointer to an element refers to an element of this slice:

```
let a = [1, 2, 3];
let x = &a[1] as *const _;
let y = &5 as *const _;

assert!(a.as_ptr_range().contains(&x));
assert!(!a.as_ptr_range().contains(&y));
```

1.48.0

·

Source

#### pub fn as_mut_ptr_range(&mut self) -> Range<*mut T> ⓘ

Returns the two unsafe mutable pointers spanning the slice.

The returned range is half-open, which means that the end pointer points *one past* the last element of the slice. This way, an empty slice is represented by two equal pointers, and the difference between the two pointers represents the size of the slice.

See `as_mut_ptr` for warnings on using these pointers. The end pointer requires extra caution, as it does not point to a valid element in the slice.

This function is useful for interacting with foreign interfaces which use two pointers to refer to a range of elements in memory, as is common in C++.

1.93.0

·

Source

#### pub fn as_array<const N: usize>(&self) -> Option<&[T; N]>

Gets a reference to the underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

1.93.0

·

Source

#### pub fn as_mut_array<const N: usize>(&mut self) -> Option<&mut [T; N]>

Gets a mutable reference to the slice’s underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

1.0.0

·

Source

#### pub fn swap(&mut self, a: usize, b: usize)

Swaps two elements in the slice.

If `a` equals to `b`, it’s guaranteed that elements won’t change value.

##### §Arguments

- a - The index of the first element
- b - The index of the second element

##### §Panics

Panics if `a` or `b` are out of bounds.

##### §Examples

```
let mut v = ["a", "b", "c", "d", "e"];
v.swap(2, 4);
assert!(v == ["a", "b", "e", "d", "c"]);
```

Source

#### pub unsafe fn swap_unchecked(&mut self, a: usize, b: usize)

🔬

This is a nightly-only experimental API. (

slice_swap_unchecked

#88539

)

Swaps two elements in the slice, without doing bounds checking.

For a safe alternative see `swap`.

##### §Arguments

- a - The index of the first element
- b - The index of the second element

##### §Safety

Calling this method with an out-of-bounds index is *undefined behavior*. The caller has to ensure that `a < self.len()` and `b < self.len()`.

##### §Examples

```
#![feature(slice_swap_unchecked)]

let mut v = ["a", "b", "c", "d"];
unsafe { v.swap_unchecked(1, 3) };
assert!(v == ["a", "d", "c", "b"]);
```

1.0.0

·

Source

#### pub fn reverse(&mut self)

Reverses the order of elements in the slice, in place.

##### §Examples

```
let mut v = [1, 2, 3];
v.reverse();
assert!(v == [3, 2, 1]);
```

1.0.0

·

Source

#### pub fn iter(&self) -> Iter<'_, T> ⓘ

Returns an iterator over the slice.

The iterator yields all items from start to end.

##### §Examples

```
let x = &[1, 2, 4];
let mut iterator = x.iter();

assert_eq!(iterator.next(), Some(&1));
assert_eq!(iterator.next(), Some(&2));
assert_eq!(iterator.next(), Some(&4));
assert_eq!(iterator.next(), None);
```

1.0.0

·

Source

#### pub fn iter_mut(&mut self) -> IterMut<'_, T> ⓘ

Returns an iterator that allows modifying each value.

The iterator yields all items from start to end.

##### §Examples

```
let x = &mut [1, 2, 4];
for elem in x.iter_mut() {
    *elem += 2;
}
assert_eq!(x, &[3, 4, 6]);
```

1.0.0

·

Source

#### pub fn windows(&self, size: usize) -> Windows<'_, T> ⓘ

Returns an iterator over all contiguous windows of length `size`. The windows overlap. If the slice is shorter than `size`, the iterator returns no values.

##### §Panics

Panics if `size` is zero.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.windows(3);
assert_eq!(iter.next().unwrap(), &['l', 'o', 'r']);
assert_eq!(iter.next().unwrap(), &['o', 'r', 'e']);
assert_eq!(iter.next().unwrap(), &['r', 'e', 'm']);
assert!(iter.next().is_none());
```

If the slice is shorter than `size`:

```
let slice = ['f', 'o', 'o'];
let mut iter = slice.windows(4);
assert!(iter.next().is_none());
```

Because the Iterator trait cannot represent the required lifetimes, there is no `windows_mut` analog to `windows`; `[0,1,2].windows_mut(2).collect()` would violate the rules of references (though a LendingIterator analog is possible). You can sometimes use `Cell::as_slice_of_cells` in conjunction with `windows` instead:

```
use std::cell::Cell;

let mut array = ['R', 'u', 's', 't', ' ', '2', '0', '1', '5'];
let slice = &mut array[..];
let slice_of_cells: &[Cell<char>] = Cell::from_mut(slice).as_slice_of_cells();
for w in slice_of_cells.windows(3) {
    Cell::swap(&w[0], &w[2]);
}
assert_eq!(array, ['s', 't', ' ', '2', '0', '1', '5', 'u', 'R']);
```

1.0.0

·

Source

#### pub fn chunks(&self, chunk_size: usize) -> Chunks<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See `chunks_exact` for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and `rchunks` for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using `as_chunks` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.chunks(2);
assert_eq!(iter.next().unwrap(), &['l', 'o']);
assert_eq!(iter.next().unwrap(), &['r', 'e']);
assert_eq!(iter.next().unwrap(), &['m']);
assert!(iter.next().is_none());
```

1.0.0

·

Source

#### pub fn chunks_mut(&mut self, chunk_size: usize) -> ChunksMut<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See `chunks_exact_mut` for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and `rchunks_mut` for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using `as_chunks_mut` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.chunks_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 3]);
```

1.31.0

·

Source

#### pub fn chunks_exact(&self, chunk_size: usize) -> ChunksExact<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of `chunks`.

See `chunks` for a variant of this iterator that also returns the remainder as a smaller chunk, and `rchunks_exact` for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using `as_chunks` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.chunks_exact(2);
assert_eq!(iter.next().unwrap(), &['l', 'o']);
assert_eq!(iter.next().unwrap(), &['r', 'e']);
assert!(iter.next().is_none());
assert_eq!(iter.remainder(), &['m']);
```

1.31.0

·

Source

#### pub fn chunks_exact_mut(&mut self, chunk_size: usize) -> ChunksExactMut<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `into_remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of `chunks_mut`.

See `chunks_mut` for a variant of this iterator that also returns the remainder as a smaller chunk, and `rchunks_exact_mut` for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using `as_chunks_mut` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.chunks_exact_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 0]);
```

1.88.0

·

Source

#### pub unsafe fn as_chunks_unchecked<const N: usize>(&self) -> &[[T; N]]

Splits the slice into a slice of `N`-element arrays, assuming that there’s no remainder.

This is the inverse operation to `as_flattened`.

As this is `unsafe`, consider whether you could use `as_chunks` or `as_rchunks` instead, perhaps via something like `if let (chunks, []) = slice.as_chunks()` or `let (chunks, []) = slice.as_chunks() else { unreachable!() };`.

##### §Safety

This may only be called when

- The slice splits exactly into `N`-element chunks (aka `self.len() % N == 0`).
- `N != 0`.

##### §Examples

```
let slice: &[char] = &['l', 'o', 'r', 'e', 'm', '!'];
let chunks: &[[char; 1]] =
    unsafe { slice.as_chunks_unchecked() };
assert_eq!(chunks, &[['l'], ['o'], ['r'], ['e'], ['m'], ['!']]);
let chunks: &[[char; 3]] =
    unsafe { slice.as_chunks_unchecked() };
assert_eq!(chunks, &[['l', 'o', 'r'], ['e', 'm', '!']]);
```

1.88.0

·

Source

#### pub fn as_chunks<const N: usize>(&self) -> (&[[T; N]], &[T])

Splits the slice into a slice of `N`-element arrays, starting at the beginning of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (chunks, remainder) = slice.as_chunks()`, then:

- `chunks.len()` equals `slice.len() / N`,
- `remainder.len()` equals `slice.len() % N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with `as_flattened`.

##### §Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let (chunks, remainder) = slice.as_chunks();
assert_eq!(chunks, &[['l', 'o'], ['r', 'e']]);
assert_eq!(remainder, &['m']);
```

If you expect the slice to be an exact multiple, you can combine `let`-`else` with an empty slice pattern:

```
let slice = ['R', 'u', 's', 't'];
let (chunks, []) = slice.as_chunks::<2>() else {
    panic!("slice didn't have even length")
};
assert_eq!(chunks, &[['R', 'u'], ['s', 't']]);
```

1.88.0

·

Source

#### pub fn as_rchunks<const N: usize>(&self) -> (&[T], &[[T; N]])

Splits the slice into a slice of `N`-element arrays, starting at the end of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (remainder, chunks) = slice.as_rchunks()`, then:

- `remainder.len()` equals `slice.len() % N`,
- `chunks.len()` equals `slice.len() / N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with `as_flattened`.

##### §Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let (remainder, chunks) = slice.as_rchunks();
assert_eq!(remainder, &['l']);
assert_eq!(chunks, &[['o', 'r'], ['e', 'm']]);
```

1.88.0

·

Source

#### pub unsafe fn as_chunks_unchecked_mut<const N: usize>( &mut self, ) -> &mut [[T; N]]

Splits the slice into a slice of `N`-element arrays, assuming that there’s no remainder.

This is the inverse operation to `as_flattened_mut`.

As this is `unsafe`, consider whether you could use `as_chunks_mut` or `as_rchunks_mut` instead, perhaps via something like `if let (chunks, []) = slice.as_chunks_mut()` or `let (chunks, []) = slice.as_chunks_mut() else { unreachable!() };`.

##### §Safety

This may only be called when

- The slice splits exactly into `N`-element chunks (aka `self.len() % N == 0`).
- `N != 0`.

##### §Examples

```
let slice: &mut [char] = &mut ['l', 'o', 'r', 'e', 'm', '!'];
let chunks: &mut [[char; 1]] =
    unsafe { slice.as_chunks_unchecked_mut() };
chunks[0] = ['L'];
assert_eq!(chunks, &[['L'], ['o'], ['r'], ['e'], ['m'], ['!']]);
let chunks: &mut [[char; 3]] =
    unsafe { slice.as_chunks_unchecked_mut() };
chunks[1] = ['a', 'x', '?'];
assert_eq!(slice, &['L', 'o', 'r', 'a', 'x', '?']);
```

1.88.0

·

Source

#### pub fn as_chunks_mut<const N: usize>(&mut self) -> (&mut [[T; N]], &mut [T])

Splits the slice into a slice of `N`-element arrays, starting at the beginning of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (chunks, remainder) = slice.as_chunks_mut()`, then:

- `chunks.len()` equals `slice.len() / N`,
- `remainder.len()` equals `slice.len() % N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with `as_flattened_mut`.

##### §Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

let (chunks, remainder) = v.as_chunks_mut();
remainder[0] = 9;
for chunk in chunks {
    *chunk = [count; 2];
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 9]);
```

1.88.0

·

Source

#### pub fn as_rchunks_mut<const N: usize>(&mut self) -> (&mut [T], &mut [[T; N]])

Splits the slice into a slice of `N`-element arrays, starting at the end of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (remainder, chunks) = slice.as_rchunks_mut()`, then:

- `remainder.len()` equals `slice.len() % N`,
- `chunks.len()` equals `slice.len() / N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with `as_flattened_mut`.

##### §Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

let (remainder, chunks) = v.as_rchunks_mut();
remainder[0] = 9;
for chunk in chunks {
    *chunk = [count; 2];
    count += 1;
}
assert_eq!(v, &[9, 1, 1, 2, 2]);
```

1.94.0

·

Source

#### pub fn array_windows<const N: usize>(&self) -> ArrayWindows<'_, T, N> ⓘ

Returns an iterator over overlapping windows of `N` elements of a slice, starting at the beginning of the slice.

This is the const generic equivalent of `windows`.

If `N` is greater than the size of the slice, it will return no windows.

##### §Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### §Examples

```
let slice = [0, 1, 2, 3];
let mut iter = slice.array_windows();
assert_eq!(iter.next().unwrap(), &[0, 1]);
assert_eq!(iter.next().unwrap(), &[1, 2]);
assert_eq!(iter.next().unwrap(), &[2, 3]);
assert!(iter.next().is_none());
```

1.31.0

·

Source

#### pub fn rchunks(&self, chunk_size: usize) -> RChunks<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See `rchunks_exact` for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and `chunks` for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using `as_rchunks` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.rchunks(2);
assert_eq!(iter.next().unwrap(), &['e', 'm']);
assert_eq!(iter.next().unwrap(), &['o', 'r']);
assert_eq!(iter.next().unwrap(), &['l']);
assert!(iter.next().is_none());
```

1.31.0

·

Source

#### pub fn rchunks_mut(&mut self, chunk_size: usize) -> RChunksMut<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See `rchunks_exact_mut` for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and `chunks_mut` for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using `as_rchunks_mut` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.rchunks_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[3, 2, 2, 1, 1]);
```

1.31.0

·

Source

#### pub fn rchunks_exact(&self, chunk_size: usize) -> RChunksExact<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of `rchunks`.

See `rchunks` for a variant of this iterator that also returns the remainder as a smaller chunk, and `chunks_exact` for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using `as_rchunks` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.rchunks_exact(2);
assert_eq!(iter.next().unwrap(), &['e', 'm']);
assert_eq!(iter.next().unwrap(), &['o', 'r']);
assert!(iter.next().is_none());
assert_eq!(iter.remainder(), &['l']);
```

1.31.0

·

Source

#### pub fn rchunks_exact_mut(&mut self, chunk_size: usize) -> RChunksExactMut<'_, T> ⓘ

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `into_remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of `chunks_mut`.

See `rchunks_mut` for a variant of this iterator that also returns the remainder as a smaller chunk, and `chunks_exact_mut` for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using `as_rchunks_mut` instead, which will give references to arrays of exactly that length, rather than slices.

##### §Panics

Panics if `chunk_size` is zero.

##### §Examples

```
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.rchunks_exact_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[0, 2, 2, 1, 1]);
```

1.77.0

·

Source

#### pub fn chunk_by<F>(&self, pred: F) -> ChunkBy<'_, T, F> ⓘwhere F: FnMut(&T, &T) -> bool,

Returns an iterator over the slice producing non-overlapping runs of elements using the predicate to separate them.

The predicate is called for every pair of consecutive elements, meaning that it is called on `slice[0]` and `slice[1]`, followed by `slice[1]` and `slice[2]`, and so on.

##### §Examples

```
let slice = &[1, 1, 1, 3, 3, 2, 2, 2];

let mut iter = slice.chunk_by(|a, b| a == b);

assert_eq!(iter.next(), Some(&[1, 1, 1][..]));
assert_eq!(iter.next(), Some(&[3, 3][..]));
assert_eq!(iter.next(), Some(&[2, 2, 2][..]));
assert_eq!(iter.next(), None);
```

This method can be used to extract the sorted subslices:

```
let slice = &[1, 1, 2, 3, 2, 3, 2, 3, 4];

let mut iter = slice.chunk_by(|a, b| a <= b);

assert_eq!(iter.next(), Some(&[1, 1, 2, 3][..]));
assert_eq!(iter.next(), Some(&[2, 3][..]));
assert_eq!(iter.next(), Some(&[2, 3, 4][..]));
assert_eq!(iter.next(), None);
```

1.77.0

·

Source

#### pub fn chunk_by_mut<F>(&mut self, pred: F) -> ChunkByMut<'_, T, F> ⓘwhere F: FnMut(&T, &T) -> bool,

Returns an iterator over the slice producing non-overlapping mutable runs of elements using the predicate to separate them.

The predicate is called for every pair of consecutive elements, meaning that it is called on `slice[0]` and `slice[1]`, followed by `slice[1]` and `slice[2]`, and so on.

##### §Examples

```
let slice = &mut [1, 1, 1, 3, 3, 2, 2, 2];

let mut iter = slice.chunk_by_mut(|a, b| a == b);

assert_eq!(iter.next(), Some(&mut [1, 1, 1][..]));
assert_eq!(iter.next(), Some(&mut [3, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 2, 2][..]));
assert_eq!(iter.next(), None);
```

This method can be used to extract the sorted subslices:

```
let slice = &mut [1, 1, 2, 3, 2, 3, 2, 3, 4];

let mut iter = slice.chunk_by_mut(|a, b| a <= b);

assert_eq!(iter.next(), Some(&mut [1, 1, 2, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 3, 4][..]));
assert_eq!(iter.next(), None);
```

1.0.0

·

Source

#### pub fn split_at(&self, mid: usize) -> (&[T], &[T])

Divides one slice into two at an index.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### §Panics

Panics if `mid > len`. For a non-panicking alternative see `split_at_checked`.

##### §Examples

```
let v = ['a', 'b', 'c'];

{
   let (left, right) = v.split_at(0);
   assert_eq!(left, []);
   assert_eq!(right, ['a', 'b', 'c']);
}

{
    let (left, right) = v.split_at(2);
    assert_eq!(left, ['a', 'b']);
    assert_eq!(right, ['c']);
}

{
    let (left, right) = v.split_at(3);
    assert_eq!(left, ['a', 'b', 'c']);
    assert_eq!(right, []);
}
```

1.0.0

·

Source

#### pub fn split_at_mut(&mut self, mid: usize) -> (&mut [T], &mut [T])

Divides one mutable slice into two at an index.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### §Panics

Panics if `mid > len`. For a non-panicking alternative see `split_at_mut_checked`.

##### §Examples

```
let mut v = [1, 0, 3, 0, 5, 6];
let (left, right) = v.split_at_mut(2);
assert_eq!(left, [1, 0]);
assert_eq!(right, [3, 0, 5, 6]);
left[1] = 2;
right[1] = 4;
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

1.79.0

·

Source

#### pub unsafe fn split_at_unchecked(&self, mid: usize) -> (&[T], &[T])

Divides one slice into two at an index, without doing bounds checking.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

For a safe alternative see `split_at`.

##### §Safety

Calling this method with an out-of-bounds index is *undefined behavior* even if the resulting reference is not used. The caller has to ensure that `0 <= mid <= self.len()`.

##### §Examples

```
let v = ['a', 'b', 'c'];

unsafe {
   let (left, right) = v.split_at_unchecked(0);
   assert_eq!(left, []);
   assert_eq!(right, ['a', 'b', 'c']);
}

unsafe {
    let (left, right) = v.split_at_unchecked(2);
    assert_eq!(left, ['a', 'b']);
    assert_eq!(right, ['c']);
}

unsafe {
    let (left, right) = v.split_at_unchecked(3);
    assert_eq!(left, ['a', 'b', 'c']);
    assert_eq!(right, []);
}
```

1.79.0

·

Source

#### pub unsafe fn split_at_mut_unchecked( &mut self, mid: usize, ) -> (&mut [T], &mut [T])

Divides one mutable slice into two at an index, without doing bounds checking.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

For a safe alternative see `split_at_mut`.

##### §Safety

Calling this method with an out-of-bounds index is *undefined behavior* even if the resulting reference is not used. The caller has to ensure that `0 <= mid <= self.len()`.

##### §Examples

```
let mut v = [1, 0, 3, 0, 5, 6];
unsafe {
    let (left, right) = v.split_at_mut_unchecked(2);
    assert_eq!(left, [1, 0]);
    assert_eq!(right, [3, 0, 5, 6]);
    left[1] = 2;
    right[1] = 4;
}
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

1.80.0

·

Source

#### pub fn split_at_checked(&self, mid: usize) -> Option<(&[T], &[T])>

Divides one slice into two at an index, returning `None` if the slice is too short.

If `mid ≤ len` returns a pair of slices where the first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

Otherwise, if `mid > len`, returns `None`.

##### §Examples

```
let v = [1, -2, 3, -4, 5, -6];

{
   let (left, right) = v.split_at_checked(0).unwrap();
   assert_eq!(left, []);
   assert_eq!(right, [1, -2, 3, -4, 5, -6]);
}

{
    let (left, right) = v.split_at_checked(2).unwrap();
    assert_eq!(left, [1, -2]);
    assert_eq!(right, [3, -4, 5, -6]);
}

{
    let (left, right) = v.split_at_checked(6).unwrap();
    assert_eq!(left, [1, -2, 3, -4, 5, -6]);
    assert_eq!(right, []);
}

assert_eq!(None, v.split_at_checked(7));
```

1.80.0

·

Source

#### pub fn split_at_mut_checked( &mut self, mid: usize, ) -> Option<(&mut [T], &mut [T])>

Divides one mutable slice into two at an index, returning `None` if the slice is too short.

If `mid ≤ len` returns a pair of slices where the first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

Otherwise, if `mid > len`, returns `None`.

##### §Examples

```
let mut v = [1, 0, 3, 0, 5, 6];

if let Some((left, right)) = v.split_at_mut_checked(2) {
    assert_eq!(left, [1, 0]);
    assert_eq!(right, [3, 0, 5, 6]);
    left[1] = 2;
    right[1] = 4;
}
assert_eq!(v, [1, 2, 3, 4, 5, 6]);

assert_eq!(None, v.split_at_mut_checked(7));
```

1.0.0

·

Source

#### pub fn split<F>(&self, pred: F) -> Split<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred`. The matched element is not contained in the subslices.

##### §Examples

```
let slice = [10, 40, 33, 20];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

If the first element is matched, an empty slice will be the first item returned by the iterator. Similarly, if the last element in the slice is matched, an empty slice will be the last item returned by the iterator:

```
let slice = [10, 40, 33];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40]);
assert_eq!(iter.next().unwrap(), &[]);
assert!(iter.next().is_none());
```

If two matched elements are directly adjacent, an empty slice will be present between them:

```
let slice = [10, 6, 33, 20];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10]);
assert_eq!(iter.next().unwrap(), &[]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

1.0.0

·

Source

#### pub fn split_mut<F>(&mut self, pred: F) -> SplitMut<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over mutable subslices separated by elements that match `pred`. The matched element is not contained in the subslices.

##### §Examples

```
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.split_mut(|num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(v, [1, 40, 30, 1, 60, 1]);
```

1.51.0

·

Source

#### pub fn split_inclusive<F>(&self, pred: F) -> SplitInclusive<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred`. The matched element is contained in the end of the previous subslice as a terminator.

##### §Examples

```
let slice = [10, 40, 33, 20];
let mut iter = slice.split_inclusive(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40, 33]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

If the last element of the slice is matched, that element will be considered the terminator of the preceding slice. That slice will be the last item returned by the iterator.

```
let slice = [3, 10, 40, 33];
let mut iter = slice.split_inclusive(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[3]);
assert_eq!(iter.next().unwrap(), &[10, 40, 33]);
assert!(iter.next().is_none());
```

1.51.0

·

Source

#### pub fn split_inclusive_mut<F>(&mut self, pred: F) -> SplitInclusiveMut<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over mutable subslices separated by elements that match `pred`. The matched element is contained in the previous subslice as a terminator.

##### §Examples

```
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.split_inclusive_mut(|num| *num % 3 == 0) {
    let terminator_idx = group.len()-1;
    group[terminator_idx] = 1;
}
assert_eq!(v, [10, 40, 1, 20, 1, 1]);
```

1.27.0

·

Source

#### pub fn rsplit<F>(&self, pred: F) -> RSplit<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred`, starting at the end of the slice and working backwards. The matched element is not contained in the subslices.

##### §Examples

```
let slice = [11, 22, 33, 0, 44, 55];
let mut iter = slice.rsplit(|num| *num == 0);

assert_eq!(iter.next().unwrap(), &[44, 55]);
assert_eq!(iter.next().unwrap(), &[11, 22, 33]);
assert_eq!(iter.next(), None);
```

As with `split()`, if the first or last element is matched, an empty slice will be the first (or last) item returned by the iterator.

```
let v = &[0, 1, 1, 2, 3, 5, 8];
let mut it = v.rsplit(|n| *n % 2 == 0);
assert_eq!(it.next().unwrap(), &[]);
assert_eq!(it.next().unwrap(), &[3, 5]);
assert_eq!(it.next().unwrap(), &[1, 1]);
assert_eq!(it.next().unwrap(), &[]);
assert_eq!(it.next(), None);
```

1.27.0

·

Source

#### pub fn rsplit_mut<F>(&mut self, pred: F) -> RSplitMut<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over mutable subslices separated by elements that match `pred`, starting at the end of the slice and working backwards. The matched element is not contained in the subslices.

##### §Examples

```
let mut v = [100, 400, 300, 200, 600, 500];

let mut count = 0;
for group in v.rsplit_mut(|num| *num % 3 == 0) {
    count += 1;
    group[0] = count;
}
assert_eq!(v, [3, 400, 300, 2, 600, 1]);
```

1.0.0

·

Source

#### pub fn splitn<F>(&self, n: usize, pred: F) -> SplitN<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred`, limited to returning at most `n` items. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### §Examples

Print the slice split once by numbers divisible by 3 (i.e., `[10, 40]`, `[20, 60, 50]`):

```
let v = [10, 40, 30, 20, 60, 50];

for group in v.splitn(2, |num| *num % 3 == 0) {
    println!("{group:?}");
}
```

1.0.0

·

Source

#### pub fn splitn_mut<F>(&mut self, n: usize, pred: F) -> SplitNMut<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over mutable subslices separated by elements that match `pred`, limited to returning at most `n` items. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### §Examples

```
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.splitn_mut(2, |num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(v, [1, 40, 30, 1, 60, 50]);
```

1.0.0

·

Source

#### pub fn rsplitn<F>(&self, n: usize, pred: F) -> RSplitN<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred` limited to returning at most `n` items. This starts at the end of the slice and works backwards. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### §Examples

Print the slice split once, starting from the end, by numbers divisible by 3 (i.e., `[50]`, `[10, 40, 30, 20]`):

```
let v = [10, 40, 30, 20, 60, 50];

for group in v.rsplitn(2, |num| *num % 3 == 0) {
    println!("{group:?}");
}
```

1.0.0

·

Source

#### pub fn rsplitn_mut<F>(&mut self, n: usize, pred: F) -> RSplitNMut<'_, T, F> ⓘwhere F: FnMut(&T) -> bool,

Returns an iterator over subslices separated by elements that match `pred` limited to returning at most `n` items. This starts at the end of the slice and works backwards. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### §Examples

```
let mut s = [10, 40, 30, 20, 60, 50];

for group in s.rsplitn_mut(2, |num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(s, [1, 40, 30, 20, 60, 1]);
```

Source

#### pub fn split_once<F>(&self, pred: F) -> Option<(&[T], &[T])>where F: FnMut(&T) -> bool,

🔬

This is a nightly-only experimental API. (

slice_split_once

#112811

)

Splits the slice on the first element that matches the specified predicate.

If any matching elements are present in the slice, returns the prefix before the match and suffix after. The matching element itself is not included. If no elements match, returns `None`.

##### §Examples

```
#![feature(slice_split_once)]
let s = [1, 2, 3, 2, 4];
assert_eq!(s.split_once(|&x| x == 2), Some((
    &[1][..],
    &[3, 2, 4][..]
)));
assert_eq!(s.split_once(|&x| x == 0), None);
```

Source

#### pub fn rsplit_once<F>(&self, pred: F) -> Option<(&[T], &[T])>where F: FnMut(&T) -> bool,

🔬

This is a nightly-only experimental API. (

slice_split_once

#112811

)

Splits the slice on the last element that matches the specified predicate.

If any matching elements are present in the slice, returns the prefix before the match and suffix after. The matching element itself is not included. If no elements match, returns `None`.

##### §Examples

```
#![feature(slice_split_once)]
let s = [1, 2, 3, 2, 4];
assert_eq!(s.rsplit_once(|&x| x == 2), Some((
    &[1, 2, 3][..],
    &[4][..]
)));
assert_eq!(s.rsplit_once(|&x| x == 0), None);
```

1.0.0

·

Source

#### pub fn contains(&self, x: &T) -> boolwhere T: PartialEq,

Returns `true` if the slice contains an element with the given value.

This operation is *O*(*n*).

Note that if you have a sorted slice, `binary_search` may be faster.

##### §Examples

```
let v = [10, 40, 30];
assert!(v.contains(&30));
assert!(!v.contains(&50));
```

If you do not have a `&T`, but some other value that you can compare with one (for example, `String` implements `PartialEq<str>`), you can use `iter().any`:

```
let v = [String::from("hello"), String::from("world")]; assert!(v.iter().any(|e| e == "hello")); assert!(!v.iter().any(|e| e == "hi"));
```

1.0.0

·

Source

#### pub fn starts_with(&self, needle: &[T]) -> boolwhere T: PartialEq,

Returns `true` if `needle` is a prefix of the slice or equal to the slice.

##### §Examples

```
let v = [10, 40, 30];
assert!(v.starts_with(&[10]));
assert!(v.starts_with(&[10, 40]));
assert!(v.starts_with(&v));
assert!(!v.starts_with(&[50]));
assert!(!v.starts_with(&[10, 50]));
```

Always returns `true` if `needle` is an empty slice:

```
let v = &[10, 40, 30];
assert!(v.starts_with(&[]));
let v: &[u8] = &[];
assert!(v.starts_with(&[]));
```

1.0.0

·

Source

#### pub fn ends_with(&self, needle: &[T]) -> boolwhere T: PartialEq,

Returns `true` if `needle` is a suffix of the slice or equal to the slice.

##### §Examples

```
let v = [10, 40, 30];
assert!(v.ends_with(&[30]));
assert!(v.ends_with(&[40, 30]));
assert!(v.ends_with(&v));
assert!(!v.ends_with(&[50]));
assert!(!v.ends_with(&[50, 30]));
```

Always returns `true` if `needle` is an empty slice:

```
let v = &[10, 40, 30];
assert!(v.ends_with(&[]));
let v: &[u8] = &[];
assert!(v.ends_with(&[]));
```

1.51.0

·

Source

#### pub fn strip_prefix<P>(&self, prefix: &P) -> Option<&[T]>where P: SlicePattern<Item = T> + ?Sized, T: PartialEq,

Returns a subslice with the prefix removed.

If the slice starts with `prefix`, returns the subslice after the prefix, wrapped in `Some`. If `prefix` is empty, simply returns the original slice. If `prefix` is equal to the original slice, returns an empty slice.

If the slice does not start with `prefix`, returns `None`.

##### §Examples

```
let v = &[10, 40, 30];
assert_eq!(v.strip_prefix(&[10]), Some(&[40, 30][..]));
assert_eq!(v.strip_prefix(&[10, 40]), Some(&[30][..]));
assert_eq!(v.strip_prefix(&[10, 40, 30]), Some(&[][..]));
assert_eq!(v.strip_prefix(&[50]), None);
assert_eq!(v.strip_prefix(&[10, 50]), None);

let prefix : &str = "he";
assert_eq!(b"hello".strip_prefix(prefix.as_bytes()),
           Some(b"llo".as_ref()));
```

1.51.0

·

Source

#### pub fn strip_suffix<P>(&self, suffix: &P) -> Option<&[T]>where P: SlicePattern<Item = T> + ?Sized, T: PartialEq,

Returns a subslice with the suffix removed.

If the slice ends with `suffix`, returns the subslice before the suffix, wrapped in `Some`. If `suffix` is empty, simply returns the original slice. If `suffix` is equal to the original slice, returns an empty slice.

If the slice does not end with `suffix`, returns `None`.

##### §Examples

```
let v = &[10, 40, 30];
assert_eq!(v.strip_suffix(&[30]), Some(&[10, 40][..]));
assert_eq!(v.strip_suffix(&[40, 30]), Some(&[10][..]));
assert_eq!(v.strip_suffix(&[10, 40, 30]), Some(&[][..]));
assert_eq!(v.strip_suffix(&[50]), None);
assert_eq!(v.strip_suffix(&[50, 30]), None);
```

Source

#### pub fn strip_circumfix<S, P>(&self, prefix: &P, suffix: &S) -> Option<&[T]>where T: PartialEq, S: SlicePattern<Item = T> + ?Sized, P: SlicePattern<Item = T> + ?Sized,

🔬

This is a nightly-only experimental API. (

strip_circumfix

#147946

)

Returns a subslice with the prefix and suffix removed.

If the slice starts with `prefix` and ends with `suffix`, returns the subslice after the prefix and before the suffix, wrapped in `Some`.

If the slice does not start with `prefix` or does not end with `suffix`, returns `None`.

##### §Examples

```
#![feature(strip_circumfix)]

let v = &[10, 50, 40, 30];
assert_eq!(v.strip_circumfix(&[10], &[30]), Some(&[50, 40][..]));
assert_eq!(v.strip_circumfix(&[10], &[40, 30]), Some(&[50][..]));
assert_eq!(v.strip_circumfix(&[10, 50], &[40, 30]), Some(&[][..]));
assert_eq!(v.strip_circumfix(&[50], &[30]), None);
assert_eq!(v.strip_circumfix(&[10], &[40]), None);
assert_eq!(v.strip_circumfix(&[], &[40, 30]), Some(&[10, 50][..]));
assert_eq!(v.strip_circumfix(&[10, 50], &[]), Some(&[40, 30][..]));
```

Source

#### pub fn trim_prefix<P>(&self, prefix: &P) -> &[T]where P: SlicePattern<Item = T> + ?Sized, T: PartialEq,

🔬

This is a nightly-only experimental API. (

trim_prefix_suffix

#142312

)
