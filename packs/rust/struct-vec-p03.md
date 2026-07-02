---
title: "Vec in std::vec (part 3/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 3/7
---

# Vec in std::vec

·

Source

#### pub const fn as_mut_slice(&mut self) -> &mut [T]

Extracts a mutable slice of the entire vector.

Equivalent to `&mut s[..]`.

##### §Examples

```
use std::io::{self, Read};
let mut buffer = vec![0; 3];
io::repeat(0b101).read_exact(buffer.as_mut_slice()).unwrap();
```

1.37.0 (const: 1.87.0)

·

Source

#### pub const fn as_ptr(&self) -> *const T

Returns a raw pointer to the vector’s buffer, or a dangling raw pointer valid for zero sized reads if the vector didn’t allocate.

The caller must ensure that the vector outlives the pointer this function returns, or else it will end up dangling. Modifying the vector may cause its buffer to be reallocated, which would also make any pointers to it invalid.

The caller must also ensure that the memory the pointer (non-transitively) points to is never written to (except inside an `UnsafeCell`) using this pointer or any pointer derived from it. If you need to mutate the contents of the slice, use `as_mut_ptr`.

This method guarantees that for the purpose of the aliasing model, this method does not materialize a reference to the underlying slice, and thus the returned pointer will remain valid when mixed with other calls to `as_ptr`, `as_mut_ptr`, and `as_non_null`. Note that calling other methods that materialize mutable references to the slice, or mutable references to specific elements you are planning on accessing through this pointer, as well as writing to those elements, may still invalidate this pointer. See the second example below for how this guarantee can be used.

##### §Examples

```
let x = vec![1, 2, 4];
let x_ptr = x.as_ptr();

unsafe {
    for i in 0..x.len() {
        assert_eq!(*x_ptr.add(i), 1 << i);
    }
}
```

Due to the aliasing guarantee, the following code is legal:

```
unsafe {
    let mut v = vec![0, 1, 2];
    let ptr1 = v.as_ptr();
    let _ = ptr1.read();
    let ptr2 = v.as_mut_ptr().offset(2);
    ptr2.write(2);
    let _ = ptr1.read();
}
```

1.37.0 (const: 1.87.0)

·

Source

#### pub const fn as_mut_ptr(&mut self) -> *mut T

Returns a raw mutable pointer to the vector’s buffer, or a dangling raw pointer valid for zero sized reads if the vector didn’t allocate.

The caller must ensure that the vector outlives the pointer this function returns, or else it will end up dangling. Modifying the vector may cause its buffer to be reallocated, which would also make any pointers to it invalid.

This method guarantees that for the purpose of the aliasing model, this method does not materialize a reference to the underlying slice, and thus the returned pointer will remain valid when mixed with other calls to `as_ptr`, `as_mut_ptr`, and `as_non_null`. Note that calling other methods that materialize references to the slice, or references to specific elements you are planning on accessing through this pointer, may still invalidate this pointer. See the second example below for how this guarantee can be used.

The method also guarantees that, as long as `T` is not zero-sized and the capacity is nonzero, the pointer may be passed into `dealloc` with a layout of `Layout::array::<T>(capacity)` in order to deallocate the backing memory. If this is done, be careful not to run the destructor of the `Vec`, as dropping it will result in double-frees. Wrapping the `Vec` in a `ManuallyDrop` is the typical way to achieve this.

##### §Examples

```
let size = 4;
let mut x: Vec<i32> = Vec::with_capacity(size);
let x_ptr = x.as_mut_ptr();

unsafe {
    for i in 0..size {
        *x_ptr.add(i) = i as i32;
    }
    x.set_len(size);
}
assert_eq!(&*x, &[0, 1, 2, 3]);
```

Due to the aliasing guarantee, the following code is legal:

```
unsafe {
    let mut v = vec![0];
    let ptr1 = v.as_mut_ptr();
    ptr1.write(1);
    let ptr2 = v.as_mut_ptr();
    ptr2.write(2);
    ptr1.write(3);
}
```

Deallocating a vector using `Box` (which uses `dealloc` internally):

```
use std::mem::{ManuallyDrop, MaybeUninit};

let mut v = ManuallyDrop::new(vec![0, 1, 2]);
let ptr = v.as_mut_ptr();
let capacity = v.capacity();
let slice_ptr: *mut [MaybeUninit<i32>] =
    std::ptr::slice_from_raw_parts_mut(ptr.cast(), capacity);
drop(unsafe { Box::from_raw(slice_ptr) });
```

Source

#### pub const fn as_non_null(&mut self) -> NonNull<T>

🔬

This is a nightly-only experimental API. (

box_vec_non_null

#130364

)

Returns a `NonNull` pointer to the vector’s buffer, or a dangling `NonNull` pointer valid for zero sized reads if the vector didn’t allocate.

The caller must ensure that the vector outlives the pointer this function returns, or else it will end up dangling. Modifying the vector may cause its buffer to be reallocated, which would also make any pointers to it invalid.

This method guarantees that for the purpose of the aliasing model, this method does not materialize a reference to the underlying slice, and thus the returned pointer will remain valid when mixed with other calls to `as_ptr`, `as_mut_ptr`, and `as_non_null`. Note that calling other methods that materialize references to the slice, or references to specific elements you are planning on accessing through this pointer, may still invalidate this pointer. See the second example below for how this guarantee can be used.

##### §Examples

```
#![feature(box_vec_non_null)]

let size = 4;
let mut x: Vec<i32> = Vec::with_capacity(size);
let x_ptr = x.as_non_null();

unsafe {
    for i in 0..size {
        x_ptr.add(i).write(i as i32);
    }
    x.set_len(size);
}
assert_eq!(&*x, &[0, 1, 2, 3]);
```

Due to the aliasing guarantee, the following code is legal:

```
#![feature(box_vec_non_null)]

unsafe {
    let mut v = vec![0];
    let ptr1 = v.as_non_null();
    ptr1.write(1);
    let ptr2 = v.as_non_null();
    ptr2.write(2);
    ptr1.write(3);
}
```

Source

#### pub const fn allocator(&self) -> &A

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Returns a reference to the underlying allocator.

1.0.0

·

Source

#### pub unsafe fn set_len(&mut self, new_len: usize)

Forces the length of the vector to `new_len`.

This is a low-level operation that maintains none of the normal invariants of the type. Normally changing the length of a vector is done using one of the safe operations instead, such as `truncate`, `resize`, `extend`, or `clear`.

##### §Safety

- `new_len` must be less than or equal to `capacity()`.
- The elements at `old_len..new_len` must be initialized.

##### §Examples

See `spare_capacity_mut()` for an example with safe initialization of capacity elements and use of this method.

`set_len()` can be useful for situations in which the vector is serving as a buffer for other code, particularly over FFI:

```
pub fn get_dictionary(&self) -> Option<Vec<u8>> {
    let mut dict = Vec::with_capacity(32_768);
    let mut dict_length = 0;
    unsafe {
        let r = deflateGetDictionary(self.strm, dict.as_mut_ptr(), &mut dict_length);
        if r == Z_OK {
            dict.set_len(dict_length);
            Some(dict)
        } else {
            None
        }
    }
}
```

While the following example is sound, there is a memory leak since the inner vectors were not freed prior to the `set_len` call:

```
let mut vec = vec![vec![1, 0, 0],
                   vec![0, 1, 0],
                   vec![0, 0, 1]];
unsafe {
    vec.set_len(0);
}
```

Normally, here, one would use `clear` instead to correctly drop the contents and thus not leak memory.

1.0.0

·

Source

#### pub fn swap_remove(&mut self, index: usize) -> T

Removes an element from the vector and returns it.

The removed element is replaced by the last element of the vector.

This does not preserve ordering of the remaining elements, but is *O*(1). If you need to preserve the element order, use `remove` instead.

##### §Panics

Panics if `index` is out of bounds.

##### §Examples

```
let mut v = vec!["foo", "bar", "baz", "qux"];

assert_eq!(v.swap_remove(1), "bar");
assert_eq!(v, ["foo", "qux", "baz"]);

assert_eq!(v.swap_remove(0), "foo");
assert_eq!(v, ["baz", "qux"]);
```

1.0.0

·

Source

#### pub fn insert(&mut self, index: usize, element: T)

Inserts an element at position `index` within the vector, shifting all elements after it to the right.

##### §Panics

Panics if `index > len`.

##### §Examples

```
let mut vec = vec!['a', 'b', 'c'];
vec.insert(1, 'd');
assert_eq!(vec, ['a', 'd', 'b', 'c']);
vec.insert(4, 'e');
assert_eq!(vec, ['a', 'd', 'b', 'c', 'e']);
```

##### §Time complexity

Takes *O*(`Vec::len`) time. All items after the insertion index must be shifted to the right. In the worst case, all elements are shifted when the insertion index is 0.

1.95.0

·

Source

#### pub fn insert_mut(&mut self, index: usize, element: T) -> &mut T

Inserts an element at position `index` within the vector, shifting all elements after it to the right, and returning a reference to the new element.

##### §Panics

Panics if `index > len`.

##### §Examples

```
let mut vec = vec![1, 3, 5, 9];
let x = vec.insert_mut(3, 6);
*x += 1;
assert_eq!(vec, [1, 3, 5, 7, 9]);
```

##### §Time complexity

Takes *O*(`Vec::len`) time. All items after the insertion index must be shifted to the right. In the worst case, all elements are shifted when the insertion index is 0.

1.0.0

·

Source

#### pub fn remove(&mut self, index: usize) -> T

Removes and returns the element at position `index` within the vector, shifting all elements after it to the left.

Note: Because this shifts over the remaining elements, it has a worst-case performance of *O*(*n*). If you don’t need the order of elements to be preserved, use `swap_remove` instead. If you’d like to remove elements from the beginning of the `Vec`, consider using `VecDeque::pop_front` instead.

##### §Panics

Panics if `index` is out of bounds.

##### §Examples

```
let mut v = vec!['a', 'b', 'c'];
assert_eq!(v.remove(1), 'b');
assert_eq!(v, ['a', 'c']);
```

Source

#### pub fn try_remove(&mut self, index: usize) -> Option<T>

🔬

This is a nightly-only experimental API. (

vec_try_remove

#146954

)

Remove and return the element at position `index` within the vector, shifting all elements after it to the left, or `None` if it does not exist.

Note: Because this shifts over the remaining elements, it has a worst-case performance of *O*(*n*). If you’d like to remove elements from the beginning of the `Vec`, consider using `VecDeque::pop_front` instead.

##### §Examples

```
#![feature(vec_try_remove)]
let mut v = vec![1, 2, 3];
assert_eq!(v.try_remove(0), Some(1));
assert_eq!(v.try_remove(2), None);
```

1.0.0

·

Source

#### pub fn retain<F>(&mut self, f: F)where F: FnMut(&T) -> bool,

Retains only the elements specified by the predicate.

In other words, remove all elements `e` for which `f(&e)` returns `false`. This method operates in place, visiting each element exactly once in the original order, and preserves the order of the retained elements.

##### §Examples

```
let mut vec = vec![1, 2, 3, 4];
vec.retain(|&x| x % 2 == 0);
assert_eq!(vec, [2, 4]);
```

Because the elements are visited exactly once in the original order, external state may be used to decide which elements to keep.

```
let mut vec = vec![1, 2, 3, 4, 5];
let keep = [false, true, true, false, true];
let mut iter = keep.iter();
vec.retain(|_| *iter.next().unwrap());
assert_eq!(vec, [2, 3, 5]);
```

1.61.0

·

Source

#### pub fn retain_mut<F>(&mut self, f: F)where F: FnMut(&mut T) -> bool,

Retains only the elements specified by the predicate, passing a mutable reference to it.

In other words, remove all elements `e` such that `f(&mut e)` returns `false`. This method operates in place, visiting each element exactly once in the original order, and preserves the order of the retained elements.

##### §Examples

```
let mut vec = vec![1, 2, 3, 4];
vec.retain_mut(|x| if *x <= 3 {
    *x += 1;
    true
} else {
    false
});
assert_eq!(vec, [2, 3, 4]);
```

1.16.0

·

Source

#### pub fn dedup_by_key<F, K>(&mut self, key: F)where F: FnMut(&mut T) -> K, K: PartialEq,

Removes all but the first of consecutive elements in the vector that resolve to the same key.

If the vector is sorted, this removes all duplicates.

##### §Examples

```
let mut vec = vec![10, 20, 21, 30, 20];

vec.dedup_by_key(|i| *i / 10);

assert_eq!(vec, [10, 20, 30, 20]);
```

1.16.0

·

Source

#### pub fn dedup_by<F>(&mut self, same_bucket: F)where F: FnMut(&mut T, &mut T) -> bool,

Removes all but the first of consecutive elements in the vector satisfying a given equality relation.

The `same_bucket` function is passed references to two elements from the vector and must determine if the elements compare equal. The elements are passed in opposite order from their order in the slice, so if `same_bucket(a, b)` returns `true`, `a` is removed.

If the vector is sorted, this removes all duplicates.

##### §Examples

```
let mut vec = vec!["foo", "bar", "Bar", "baz", "bar"];

vec.dedup_by(|a, b| a.eq_ignore_ascii_case(b));

assert_eq!(vec, ["foo", "bar", "baz", "bar"]);
```

Source

#### pub fn push_within_capacity(&mut self, value: T) -> Result<&mut T, T>

🔬

This is a nightly-only experimental API. (

vec_push_within_capacity

#100486

)

Appends an element and returns a reference to it if there is sufficient spare capacity, otherwise an error is returned with the element.

Unlike `push` this method will not reallocate when there’s insufficient capacity. The caller should use `reserve` or `try_reserve` to ensure that there is enough capacity.

##### §Examples

A manual, panic-free alternative to `FromIterator`:

```
#![feature(vec_push_within_capacity)]

use std::collections::TryReserveError;
fn from_iter_fallible<T>(iter: impl Iterator<Item=T>) -> Result<Vec<T>, TryReserveError> {
    let mut vec = Vec::new();
    for value in iter {
        if let Err(value) = vec.push_within_capacity(value) {
            vec.try_reserve(1)?;
            let _ = vec.push_within_capacity(value);
        }
    }
    Ok(vec)
}
assert_eq!(from_iter_fallible(0..100), Ok(Vec::from_iter(0..100)));
```

##### §Time complexity

Takes *O*(1) time.

1.0.0

·

Source

#### pub fn pop(&mut self) -> Option<T>

Removes the last element from a vector and returns it, or `None` if it is empty.

If you’d like to pop the first element, consider using `VecDeque::pop_front` instead.

##### §Examples

```
let mut vec = vec![1, 2, 3];
assert_eq!(vec.pop(), Some(3));
assert_eq!(vec, [1, 2]);
```

##### §Time complexity

Takes *O*(1) time.

1.86.0

·

Source

#### pub fn pop_if(&mut self, predicate: impl FnOnce(&mut T) -> bool) -> Option<T>

Removes and returns the last element from a vector if the predicate returns `true`, or `None` if the predicate returns false or the vector is empty (the predicate will not be called in that case).

##### §Examples

```
let mut vec = vec![1, 2, 3, 4];
let pred = |x: &mut i32| *x % 2 == 0;

assert_eq!(vec.pop_if(pred), Some(4));
assert_eq!(vec, [1, 2, 3]);
assert_eq!(vec.pop_if(pred), None);
```

Source

#### pub fn peek_mut(&mut self) -> Option<PeekMut<'_, T, A>>

🔬

This is a nightly-only experimental API. (

vec_peek_mut

#122742

)

Returns a mutable reference to the last item in the vector, or `None` if it is empty.

##### §Examples

Basic usage:

```
#![feature(vec_peek_mut)]
let mut vec = Vec::new();
assert!(vec.peek_mut().is_none());

vec.push(1);
vec.push(5);
vec.push(2);
assert_eq!(vec.last(), Some(&2));
if let Some(mut val) = vec.peek_mut() {
    *val = 0;
}
assert_eq!(vec.last(), Some(&0));
```

1.4.0

·

Source

#### pub fn append(&mut self, other: &mut Vec<T, A>)

Moves all the elements of `other` into `self`, leaving `other` empty.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1, 2, 3];
let mut vec2 = vec![4, 5, 6];
vec.append(&mut vec2);
assert_eq!(vec, [1, 2, 3, 4, 5, 6]);
assert_eq!(vec2, []);
```

1.6.0

·

Source

#### pub fn drain<R>(&mut self, range: R) -> Drain<'_, T, A> ⓘwhere R: RangeBounds<usize>,

Removes the subslice indicated by the given range from the vector, returning a double-ended iterator over the removed subslice.

If the iterator is dropped before being fully consumed, it drops the remaining removed elements.

The returned iterator keeps a mutable borrow on the vector to optimize its implementation.

##### §Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the vector.

##### §Leaking

If the returned iterator goes out of scope without being dropped (due to `mem::forget`, for example), the vector may have lost and leaked elements arbitrarily, including elements outside the range.

##### §Examples

```
let mut v = vec![1, 2, 3];
let u: Vec<_> = v.drain(1..).collect();
assert_eq!(v, &[1]);
assert_eq!(u, &[2, 3]);

v.drain(..);
assert_eq!(v, &[]);
```

1.0.0

·

Source

#### pub fn clear(&mut self)

Clears the vector, removing all values.

Note that this method has no effect on the allocated capacity of the vector.

##### §Examples

```
let mut v = vec![1, 2, 3];

v.clear();

assert!(v.is_empty());
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn len(&self) -> usize

Returns the number of elements in the vector, also referred to as its ‘length’.

##### §Examples

```
let a = vec![1, 2, 3];
assert_eq!(a.len(), 3);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn is_empty(&self) -> bool

Returns `true` if the vector contains no elements.

##### §Examples

```
let mut v = Vec::new();
assert!(v.is_empty());

v.push(1);
assert!(!v.is_empty());
```

1.4.0

·

Source

#### pub fn split_off(&mut self, at: usize) -> Vec<T, A>where A: Clone,

Splits the collection into two at the given index.

Returns a newly allocated vector containing the elements in the range `[at, len)`. After the call, the original vector will be left containing the elements `[0, at)` with its previous capacity unchanged.

- If you want to take ownership of the entire contents and capacity of the vector, see `mem::take` or `mem::replace`.
- If you don’t need the returned vector at all, see `Vec::truncate`.
- If you want to take ownership of an arbitrary subslice, or you don’t necessarily want to store the removed items in a vector, see `Vec::drain`.

##### §Panics

Panics if `at > len`.

##### §Examples

```
let mut vec = vec!['a', 'b', 'c'];
let vec2 = vec.split_off(1);
assert_eq!(vec, ['a']);
assert_eq!(vec2, ['b', 'c']);
```

1.33.0

·

Source

#### pub fn resize_with<F>(&mut self, new_len: usize, f: F)where F: FnMut() -> T,

Resizes the `Vec` in-place so that `len` is equal to `new_len`.

If `new_len` is greater than `len`, the `Vec` is extended by the difference, with each additional slot filled with the result of calling the closure `f`. The return values from `f` will end up in the `Vec` in the order they have been generated.

If `new_len` is less than `len`, the `Vec` is simply truncated.

This method uses a closure to create new values on every push. If you’d rather `Clone` a given value, use `Vec::resize`. If you want to use the `Default` trait to generate values, you can pass `Default::default` as the second argument.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1, 2, 3];
vec.resize_with(5, Default::default);
assert_eq!(vec, [1, 2, 3, 0, 0]);

let mut vec = vec![];
let mut p = 1;
vec.resize_with(4, || { p *= 2; p });
assert_eq!(vec, [2, 4, 8, 16]);
```

1.47.0

·

Source

#### pub fn leak<'a>(self) -> &'a mut [T]where A: 'a,

Consumes and leaks the `Vec`, returning a mutable reference to the contents, `&'a mut [T]`.

Note that the type `T` must outlive the chosen lifetime `'a`. If the type has only static references, or none at all, then this may be chosen to be `'static`.

As of Rust 1.57, this method does not reallocate or shrink the `Vec`, so the leaked allocation may include unused capacity that is not part of the returned slice.

This function is mainly useful for data that lives for the remainder of the program’s life. Dropping the returned reference will cause a memory leak.

##### §Examples

Simple usage:

```
let x = vec![1, 2, 3];
let static_ref: &'static mut [usize] = x.leak();
static_ref[0] += 1;
assert_eq!(static_ref, &[2, 2, 3]);
```

1.60.0

·

Source

#### pub fn spare_capacity_mut(&mut self) -> &mut [MaybeUninit<T>]

Returns the remaining spare capacity of the vector as a slice of `MaybeUninit<T>`.

The returned slice can be used to fill the vector with data (e.g. by reading from a file) before marking the data as initialized using the `set_len` method.

##### §Examples

```
let mut v = Vec::with_capacity(10);

let uninit = v.spare_capacity_mut();
uninit[0].write(0);
uninit[1].write(1);
uninit[2].write(2);

unsafe {
    v.set_len(3);
}

assert_eq!(&v, &[0, 1, 2]);
```

Source

#### pub fn split_at_spare_mut(&mut self) -> (&mut [T], &mut [MaybeUninit<T>])

🔬

This is a nightly-only experimental API. (

vec_split_at_spare

#81944

)

Returns vector content as a slice of `T`, along with the remaining spare capacity of the vector as a slice of `MaybeUninit<T>`.

The returned spare capacity slice can be used to fill the vector with data (e.g. by reading from a file) before marking the data as initialized using the `set_len` method.

Note that this is a low-level API, which should be used with care for optimization purposes. If you need to append data to a `Vec` you can use `push`, `extend`, `extend_from_slice`, `extend_from_within`, `insert`, `append`, `resize` or `resize_with`, depending on your exact needs.

##### §Examples

```
#![feature(vec_split_at_spare)]

let mut v = vec![1, 1, 2];

v.reserve(10);

let (init, uninit) = v.split_at_spare_mut();
let sum = init.iter().copied().sum::<u32>();

uninit[0].write(sum);
uninit[1].write(sum * 2);
uninit[2].write(sum * 3);
uninit[3].write(sum * 4);

unsafe {
    let len = v.len();
    v.set_len(len + 4);
}

assert_eq!(&v, &[1, 1, 2, 4, 8, 12, 16]);
```

Source

#### pub fn into_chunks<const N: usize>(self) -> Vec<[T; N], A>

🔬

This is a nightly-only experimental API. (

vec_into_chunks

#142137

)

Groups every `N` elements in the `Vec<T>` into chunks to produce a `Vec<[T; N]>`, dropping elements in the remainder. `N` must be greater than zero.

If the capacity is not a multiple of the chunk size, the buffer will shrink down to the nearest multiple with a reallocation or deallocation.

This function can be used to reverse `Vec::into_flattened`.

##### §Examples

```
#![feature(vec_into_chunks)]

let vec = vec![0, 1, 2, 3, 4, 5, 6, 7];
assert_eq!(vec.into_chunks::<3>(), [[0, 1, 2], [3, 4, 5]]);

let vec = vec![0, 1, 2, 3];
let chunks: Vec<[u8; 10]> = vec.into_chunks();
assert!(chunks.is_empty());

let flat = vec![0; 8 * 8 * 8];
let reshaped: Vec<[[[u8; 8]; 8]; 8]> = flat.into_chunks().into_chunks().into_chunks();
assert_eq!(reshaped.len(), 1);
```

Source

#### pub fn recycle<U>(self) -> Vec<U, A>where U: Recyclable<T>,

🔬

This is a nightly-only experimental API. (

vec_recycle

#148227

)

This clears out this `Vec` and recycles the allocation into a new `Vec`. The item type of the resulting `Vec` needs to have the same size and alignment as the item type of the original `Vec`.

##### §Examples

```
#![feature(vec_recycle, transmutability)]
let a: Vec<u8> = vec![0; 100];
let capacity = a.capacity();
let addr = a.as_ptr().addr();
let b: Vec<i8> = a.recycle();
assert_eq!(b.len(), 0);
assert_eq!(b.capacity(), capacity);
assert_eq!(b.as_ptr().addr(), addr);
```

The `Recyclable` bound prevents this method from being called when `T` and `U` have different sizes; e.g.:

ⓘ

```
#![feature(vec_recycle, transmutability)]
let vec: Vec<[u8; 2]> = Vec::new();
let _: Vec<[u8; 1]> = vec.recycle();
```

…or different alignments:

ⓘ

```
#![feature(vec_recycle, transmutability)]
let vec: Vec<[u16; 0]> = Vec::new();
let _: Vec<[u8; 0]> = vec.recycle();
```

However, due to temporary implementation limitations of `Recyclable`, this method is not yet callable when `T` or `U` are slices, trait objects, or other exotic types; e.g.:

ⓘ

```
#![feature(vec_recycle, transmutability)]
let mut storage: Vec<&[&str]> = Vec::new();

for input in inputs {
    let mut buffer: Vec<&str> = storage.recycle();
    buffer.extend(input.split(" "));
    process(&buffer);
    storage = buffer.recycle();
}
```

Source

§

### impl<T, A> Vec<T, A>where T: Clone, A: Allocator,

1.5.0

·

Source

#### pub fn resize(&mut self, new_len: usize, value: T)

Resizes the `Vec` in-place so that `len` is equal to `new_len`.

If `new_len` is greater than `len`, the `Vec` is extended by the difference, with each additional slot filled with `value`. If `new_len` is less than `len`, the `Vec` is simply truncated.

This method requires `T` to implement `Clone`, in order to be able to clone the passed value. If you need more flexibility (or want to rely on `Default` instead of `Clone`), use `Vec::resize_with`. If you only need to resize to a smaller size, use `Vec::truncate`.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec!["hello"];
vec.resize(3, "world");
assert_eq!(vec, ["hello", "world", "world"]);

let mut vec = vec!['a', 'b', 'c', 'd'];
vec.resize(2, '_');
assert_eq!(vec, ['a', 'b']);
```

1.6.0

·

Source

#### pub fn extend_from_slice(&mut self, other: &[T])

Clones and appends all elements in a slice to the `Vec`.

Iterates over the slice `other`, clones each element, and then appends it to this `Vec`. The `other` slice is traversed in-order.

Note that this function is the same as `extend`, except that it also works with slice elements that are Clone but not Copy. If Rust gets specialization this function may be deprecated.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1];
vec.extend_from_slice(&[2, 3, 4]);
assert_eq!(vec, [1, 2, 3, 4]);
```

1.53.0

·

Source

#### pub fn extend_from_within<R>(&mut self, src: R)where R: RangeBounds<usize>,

Given a range `src`, clones a slice of elements in that range and appends it to the end.

`src` must be a range that can form a valid subslice of the `Vec`.

##### §Panics

Panics if starting index is greater than the end index, if the index is greater than the length of the vector, or if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut characters = vec!['a', 'b', 'c', 'd', 'e'];
characters.extend_from_within(2..);
assert_eq!(characters, ['a', 'b', 'c', 'd', 'e', 'c', 'd', 'e']);

let mut numbers = vec![0, 1, 2, 3, 4];
numbers.extend_from_within(..2);
assert_eq!(numbers, [0, 1, 2, 3, 4, 0, 1]);

let mut strings = vec![String::from("hello"), String::from("world"), String::from("!")];
strings.extend_from_within(1..=2);
assert_eq!(strings, ["hello", "world", "!", "world", "!"]);
```

Source

§

### impl<T, A, const N: usize> Vec<[T; N], A>where A: Allocator,

1.80.0

·

Source

#### pub fn into_flattened(self) -> Vec<T, A>

Takes a `Vec<[T; N]>` and flattens it into a `Vec<T>`.

##### §Panics

Panics if the length of the resulting vector would overflow a `usize`.

This is only possible when flattening a vector of arrays of zero-sized types, and thus tends to be irrelevant in practice. If `size_of::<T>() > 0`, this will never panic.

##### §Examples

```
let mut vec = vec![[1, 2, 3], [4, 5, 6], [7, 8, 9]];
assert_eq!(vec.pop(), Some([7, 8, 9]));

let mut flattened = vec.into_flattened();
assert_eq!(flattened.pop(), Some(6));
```

Source

§

### impl<T, A> Vec<T, A>where T: PartialEq, A: Allocator,

1.0.0

·

Source

#### pub fn dedup(&mut self)

Removes consecutive repeated elements in the vector according to the `PartialEq` trait implementation.

If the vector is sorted, this removes all duplicates.

##### §Examples

```
let mut vec = vec![1, 2, 2, 3, 2];

vec.dedup();

assert_eq!(vec, [1, 2, 3, 2]);
```

Source

§

### impl<T, A> Vec<T, A>where A: Allocator,

1.21.0

·

Source

#### pub fn splice<R, I>( &mut self, range: R, replace_with: I, ) -> Splice<'_, <I as IntoIterator>::IntoIter, A> ⓘwhere R: RangeBounds<usize>, I: IntoIterator<Item = T>,

Creates a splicing iterator that replaces the specified range in the vector with the given `replace_with` iterator and yields the removed items. `replace_with` does not need to be the same length as `range`.

`range` is removed even if the `Splice` iterator is not consumed before it is dropped.

It is unspecified how many elements are removed from the vector if the `Splice` value is leaked.

The input iterator `replace_with` is only consumed when the `Splice` value is dropped.

This is optimal if:

- The tail (elements in the vector after `range`) is empty,
- or `replace_with` yields fewer or equal elements than `range`’s length
- or the lower bound of its `size_hint()` is exact.

Otherwise, a temporary vector is allocated and the tail is moved twice.

##### §Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the vector.

##### §Examples

```
let mut v = vec![1, 2, 3, 4];
let new = [7, 8, 9];
let u: Vec<_> = v.splice(1..3, new).collect();
assert_eq!(v, [1, 7, 8, 9, 4]);
assert_eq!(u, [2, 3]);
```

Using `splice` to insert new items into a vector efficiently at a specific position indicated by an empty range:

```
let mut v = vec![1, 5];
let new = [2, 3, 4];
v.splice(1..1, new);
assert_eq!(v, [1, 2, 3, 4, 5]);
```

1.87.0

·

Source

#### pub fn extract_if<F, R>( &mut self, range: R, filter: F, ) -> ExtractIf<'_, T, F, A> ⓘwhere F: FnMut(&mut T) -> bool, R: RangeBounds<usize>,

Creates an iterator which uses a closure to determine if an element in the range should be removed.

If the closure returns `true`, the element is removed from the vector and yielded. If the closure returns `false`, or panics, the element remains in the vector and will not be yielded.

Only elements that fall in the provided range are considered for extraction, but any elements after the range will still have to be moved if any element has been extracted.

If the returned `ExtractIf` is not exhausted, e.g. because it is dropped without iterating or the iteration short-circuits, then the remaining elements will be retained. Use `extract_if().for_each(drop)` if you do not need the returned iterator, or `retain_mut` with a negated predicate if you also do not need to restrict the range.

Using this method is equivalent to the following code:

```
let mut i = range.start;
let end_items = vec.len() - range.end;

while i < vec.len() - end_items {
    if some_predicate(&mut vec[i]) {
        let val = vec.remove(i);
        } else {
        i += 1;
    }
}
```

But `extract_if` is easier to use. `extract_if` is also more efficient, because it can backshift the elements of the array in bulk.

The iterator also lets you mutate the value of each element in the closure, regardless of whether you choose to keep or remove it.

##### §Panics

If `range` is out of bounds.

##### §Examples

Splitting a vector into even and odd values, reusing the original vector:

```
let mut numbers = vec![1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15];

let evens = numbers.extract_if(.., |x| *x % 2 == 0).collect::<Vec<_>>();
let odds = numbers;

assert_eq!(evens, vec![2, 4, 6, 8, 14]);
assert_eq!(odds, vec![1, 3, 5, 9, 11, 13, 15]);
```

Using the range argument to only process a part of the vector:

```
let mut items = vec![0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2];
let ones = items.extract_if(7.., |x| *x == 1).collect::<Vec<_>>();
assert_eq!(items, vec![0, 0, 0, 0, 0, 0, 0, 2, 2, 2]);
assert_eq!(ones.len(), 3);
```
