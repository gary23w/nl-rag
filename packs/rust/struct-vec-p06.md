---
title: "Vec in std::vec (part 6/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 6/7
---

# Vec in std::vec

`src` is the range within `self` to copy from. `dest` is the starting index of the range within `self` to copy to, which will have the same length as `src`. The two ranges may overlap. The ends of the two ranges must be less than or equal to `self.len()`.

##### §Panics

This function will panic if either range exceeds the end of the slice, or if the end of `src` is before the start.

##### §Examples

Copying four bytes within a slice:

```
let mut bytes = *b"Hello, World!";

bytes.copy_within(1..5, 8);

assert_eq!(&bytes, b"Hello, Wello!");
```

1.27.0

·

Source

#### pub fn swap_with_slice(&mut self, other: &mut [T])

Swaps all elements in `self` with those in `other`.

The length of `other` must be the same as `self`.

##### §Panics

This function will panic if the two slices have different lengths.

##### §Example

Swapping two elements across slices:

```
let mut slice1 = [0, 0];
let mut slice2 = [1, 2, 3, 4];

slice1.swap_with_slice(&mut slice2[2..]);

assert_eq!(slice1, [3, 4]);
assert_eq!(slice2, [1, 2, 0, 0]);
```

Rust enforces that there can only be one mutable reference to a particular piece of data in a particular scope. Because of this, attempting to use `swap_with_slice` on a single slice will result in a compile failure:

ⓘ

```
let mut slice = [1, 2, 3, 4, 5];
slice[..2].swap_with_slice(&mut slice[3..]); 
```

To work around this, we can use `split_at_mut` to create two distinct mutable sub-slices from a slice:

```
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.swap_with_slice(&mut right[1..]);
}

assert_eq!(slice, [4, 5, 3, 1, 2]);
```

1.30.0

·

Source

#### pub unsafe fn align_to<U>(&self) -> (&[T], &[U], &[T])

Transmutes the slice to a slice of another type, ensuring alignment of the types is maintained.

This method splits the slice into three distinct slices: prefix, correctly aligned middle slice of a new type, and the suffix slice. The middle part will be as big as possible under the given alignment constraint and element size.

This method has no purpose when either input element `T` or output element `U` are zero-sized and will return the original slice without splitting anything.

##### §Safety

This method is essentially a `transmute` with respect to the elements in the returned middle slice, so all the usual caveats pertaining to `transmute::<T, U>` also apply here.

##### §Examples

Basic usage:

```
unsafe {
    let bytes: [u8; 7] = [1, 2, 3, 4, 5, 6, 7];
    let (prefix, shorts, suffix) = bytes.align_to::<u16>();
    }
```

1.30.0

·

Source

#### pub unsafe fn align_to_mut<U>(&mut self) -> (&mut [T], &mut [U], &mut [T])

Transmutes the mutable slice to a mutable slice of another type, ensuring alignment of the types is maintained.

This method splits the slice into three distinct slices: prefix, correctly aligned middle slice of a new type, and the suffix slice. The middle part will be as big as possible under the given alignment constraint and element size.

This method has no purpose when either input element `T` or output element `U` are zero-sized and will return the original slice without splitting anything.

##### §Safety

This method is essentially a `transmute` with respect to the elements in the returned middle slice, so all the usual caveats pertaining to `transmute::<T, U>` also apply here.

##### §Examples

Basic usage:

```
unsafe {
    let mut bytes: [u8; 7] = [1, 2, 3, 4, 5, 6, 7];
    let (prefix, shorts, suffix) = bytes.align_to_mut::<u16>();
    }
```

Source

#### pub fn as_simd<const LANES: usize>(&self) -> (&[T], &[Simd<T, LANES>], &[T])where Simd<T, LANES>: AsRef<[T; LANES]>, T: SimdElement,

🔬

This is a nightly-only experimental API. (

portable_simd

#86656

)

Splits a slice into a prefix, a middle of aligned SIMD types, and a suffix.

This is a safe wrapper around `slice::align_to`, so inherits the same guarantees as that method.

##### §Panics

This will panic if the size of the SIMD type is different from `LANES` times that of the scalar.

At the time of writing, the trait restrictions on `Simd<T, LANES>` keeps that from ever happening, as only power-of-two numbers of lanes are supported. It’s possible that, in the future, those restrictions might be lifted in a way that would make it possible to see panics from this method for something like `LANES == 3`.

##### §Examples

```
#![feature(portable_simd)]
use core::simd::prelude::*;

let short = &[1, 2, 3];
let (prefix, middle, suffix) = short.as_simd::<4>();
assert_eq!(middle, []); let it = prefix.iter().chain(suffix).copied();
assert_eq!(it.collect::<Vec<_>>(), vec![1, 2, 3]);

fn basic_simd_sum(x: &[f32]) -> f32 {
    use std::ops::Add;
    let (prefix, middle, suffix) = x.as_simd();
    let sums = f32x4::from_array([
        prefix.iter().copied().sum(),
        0.0,
        0.0,
        suffix.iter().copied().sum(),
    ]);
    let sums = middle.iter().copied().fold(sums, f32x4::add);
    sums.reduce_sum()
}

let numbers: Vec<f32> = (1..101).map(|x| x as _).collect();
assert_eq!(basic_simd_sum(&numbers[1..99]), 4949.0);
```

Source

#### pub fn as_simd_mut<const LANES: usize>( &mut self, ) -> (&mut [T], &mut [Simd<T, LANES>], &mut [T])where Simd<T, LANES>: AsMut<[T; LANES]>, T: SimdElement,

🔬

This is a nightly-only experimental API. (

portable_simd

#86656

)

Splits a mutable slice into a mutable prefix, a middle of aligned SIMD types, and a mutable suffix.

This is a safe wrapper around `slice::align_to_mut`, so inherits the same guarantees as that method.

This is the mutable version of `slice::as_simd`; see that for examples.

##### §Panics

This will panic if the size of the SIMD type is different from `LANES` times that of the scalar.

At the time of writing, the trait restrictions on `Simd<T, LANES>` keeps that from ever happening, as only power-of-two numbers of lanes are supported. It’s possible that, in the future, those restrictions might be lifted in a way that would make it possible to see panics from this method for something like `LANES == 3`.

1.82.0

·

Source

#### pub fn is_sorted(&self) -> boolwhere T: PartialOrd,

Checks if the elements of this slice are sorted.

That is, for each element `a` and its following element `b`, `a <= b` must hold. If the slice yields exactly zero or one element, `true` is returned.

Note that if `Self::Item` is only `PartialOrd`, but not `Ord`, the above definition implies that this function returns `false` if any two consecutive items are not comparable.

##### §Examples

```
let empty: [i32; 0] = [];

assert!([1, 2, 2, 9].is_sorted());
assert!(![1, 3, 2, 4].is_sorted());
assert!([0].is_sorted());
assert!(empty.is_sorted());
assert!(![0.0, 1.0, f32::NAN].is_sorted());
```

1.82.0

·

Source

#### pub fn is_sorted_by<'a, F>(&'a self, compare: F) -> boolwhere F: FnMut(&'a T, &'a T) -> bool,

Checks if the elements of this slice are sorted using the given comparator function.

Instead of using `PartialOrd::partial_cmp`, this function uses the given `compare` function to determine whether two elements are to be considered in sorted order.

##### §Examples

```
assert!([1, 2, 2, 9].is_sorted_by(|a, b| a <= b));
assert!(![1, 2, 2, 9].is_sorted_by(|a, b| a < b));

assert!([0].is_sorted_by(|a, b| true));
assert!([0].is_sorted_by(|a, b| false));

let empty: [i32; 0] = [];
assert!(empty.is_sorted_by(|a, b| false));
assert!(empty.is_sorted_by(|a, b| true));
```

1.82.0

·

Source

#### pub fn is_sorted_by_key<'a, F, K>(&'a self, f: F) -> boolwhere F: FnMut(&'a T) -> K, K: PartialOrd,

Checks if the elements of this slice are sorted using the given key extraction function.

Instead of comparing the slice’s elements directly, this function compares the keys of the elements, as determined by `f`. Apart from that, it’s equivalent to `is_sorted`; see its documentation for more information.

##### §Examples

```
assert!(["c", "bb", "aaa"].is_sorted_by_key(|s| s.len()));
assert!(![-2i32, -1, 0, 3].is_sorted_by_key(|n| n.abs()));
```

1.52.0

·

Source

#### pub fn partition_point<P>(&self, pred: P) -> usizewhere P: FnMut(&T) -> bool,

Returns the index of the partition point according to the given predicate (the index of the first element of the second partition).

The slice is assumed to be partitioned according to the given predicate. This means that all elements for which the predicate returns true are at the start of the slice and all elements for which the predicate returns false are at the end. For example, `[7, 15, 3, 5, 4, 12, 6]` is partitioned under the predicate `x % 2 != 0` (all odd numbers are at the start, all even at the end).

If this slice is not partitioned, the returned result is unspecified and meaningless, as this method performs a kind of binary search.

See also `binary_search`, `binary_search_by`, and `binary_search_by_key`.

##### §Examples

```
let v = [1, 2, 3, 3, 5, 6, 7];
let i = v.partition_point(|&x| x < 5);

assert_eq!(i, 4);
assert!(v[..i].iter().all(|&x| x < 5));
assert!(v[i..].iter().all(|&x| !(x < 5)));
```

If all elements of the slice match the predicate, including if the slice is empty, then the length of the slice will be returned:

```
let a = [2, 4, 8];
assert_eq!(a.partition_point(|x| x < &100), a.len());
let a: [i32; 0] = [];
assert_eq!(a.partition_point(|x| x < &100), 0);
```

If you want to insert an item to a sorted vector, while maintaining sort order:

```
let mut s = vec![0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
let num = 42;
let idx = s.partition_point(|&x| x <= num);
s.insert(idx, num);
assert_eq!(s, [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

1.87.0

·

Source

#### pub fn split_off<'a, R>(self: &mut &'a [T], range: R) -> Option<&'a [T]>where R: OneSidedRange<usize>,

Removes the subslice corresponding to the given range and returns a reference to it.

Returns `None` and does not modify the slice if the given range is out of bounds.

Note that this method only accepts one-sided ranges such as `2..` or `..6`, but not `2..6`.

##### §Examples

Splitting off the first three elements of a slice:

```
let mut slice: &[_] = &['a', 'b', 'c', 'd'];
let mut first_three = slice.split_off(..3).unwrap();

assert_eq!(slice, &['d']);
assert_eq!(first_three, &['a', 'b', 'c']);
```

Splitting off a slice starting with the third element:

```
let mut slice: &[_] = &['a', 'b', 'c', 'd'];
let mut tail = slice.split_off(2..).unwrap();

assert_eq!(slice, &['a', 'b']);
assert_eq!(tail, &['c', 'd']);
```

Getting `None` when `range` is out of bounds:

```
let mut slice: &[_] = &['a', 'b', 'c', 'd'];

assert_eq!(None, slice.split_off(5..));
assert_eq!(None, slice.split_off(..5));
assert_eq!(None, slice.split_off(..=4));
let expected: &[char] = &['a', 'b', 'c', 'd'];
assert_eq!(Some(expected), slice.split_off(..4));
```

1.87.0

·

Source

#### pub fn split_off_mut<'a, R>( self: &mut &'a mut [T], range: R, ) -> Option<&'a mut [T]>where R: OneSidedRange<usize>,

Removes the subslice corresponding to the given range and returns a mutable reference to it.

Returns `None` and does not modify the slice if the given range is out of bounds.

Note that this method only accepts one-sided ranges such as `2..` or `..6`, but not `2..6`.

##### §Examples

Splitting off the first three elements of a slice:

```
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];
let mut first_three = slice.split_off_mut(..3).unwrap();

assert_eq!(slice, &mut ['d']);
assert_eq!(first_three, &mut ['a', 'b', 'c']);
```

Splitting off a slice starting with the third element:

```
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];
let mut tail = slice.split_off_mut(2..).unwrap();

assert_eq!(slice, &mut ['a', 'b']);
assert_eq!(tail, &mut ['c', 'd']);
```

Getting `None` when `range` is out of bounds:

```
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];

assert_eq!(None, slice.split_off_mut(5..));
assert_eq!(None, slice.split_off_mut(..5));
assert_eq!(None, slice.split_off_mut(..=4));
let expected: &mut [_] = &mut ['a', 'b', 'c', 'd'];
assert_eq!(Some(expected), slice.split_off_mut(..4));
```

1.87.0

·

Source

#### pub fn split_off_first<'a>(self: &mut &'a [T]) -> Option<&'a T>

Removes the first element of the slice and returns a reference to it.

Returns `None` if the slice is empty.

##### §Examples

```
let mut slice: &[_] = &['a', 'b', 'c'];
let first = slice.split_off_first().unwrap();

assert_eq!(slice, &['b', 'c']);
assert_eq!(first, &'a');
```

1.87.0

·

Source

#### pub fn split_off_first_mut<'a>(self: &mut &'a mut [T]) -> Option<&'a mut T>

Removes the first element of the slice and returns a mutable reference to it.

Returns `None` if the slice is empty.

##### §Examples

```
let mut slice: &mut [_] = &mut ['a', 'b', 'c'];
let first = slice.split_off_first_mut().unwrap();
*first = 'd';

assert_eq!(slice, &['b', 'c']);
assert_eq!(first, &'d');
```

1.87.0

·

Source

#### pub fn split_off_last<'a>(self: &mut &'a [T]) -> Option<&'a T>

Removes the last element of the slice and returns a reference to it.

Returns `None` if the slice is empty.

##### §Examples

```
let mut slice: &[_] = &['a', 'b', 'c'];
let last = slice.split_off_last().unwrap();

assert_eq!(slice, &['a', 'b']);
assert_eq!(last, &'c');
```

1.87.0

·

Source

#### pub fn split_off_last_mut<'a>(self: &mut &'a mut [T]) -> Option<&'a mut T>

Removes the last element of the slice and returns a mutable reference to it.

Returns `None` if the slice is empty.

##### §Examples

```
let mut slice: &mut [_] = &mut ['a', 'b', 'c'];
let last = slice.split_off_last_mut().unwrap();
*last = 'd';

assert_eq!(slice, &['a', 'b']);
assert_eq!(last, &'d');
```

1.86.0

·

Source

#### pub unsafe fn get_disjoint_unchecked_mut<I, const N: usize>( &mut self, indices: [I; N], ) -> [&mut <I as SliceIndex<[T]>>::Output; N]where I: GetDisjointMutIndex + SliceIndex<[T]>,

Returns mutable references to many indices at once, without doing any checks.

An index can be either a `usize`, a `Range` or a `RangeInclusive`. Note that this method takes an array, so all indices must be of the same type. If passed an array of `usize`s this method gives back an array of mutable references to single elements, while if passed an array of ranges it gives back an array of mutable references to slices.

For a safe alternative see `get_disjoint_mut`.

##### §Safety

Calling this method with overlapping or out-of-bounds indices is *undefined behavior* even if the resulting references are not used.

##### §Examples

```
let x = &mut [1, 2, 4];

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([0, 2]);
    *a *= 10;
    *b *= 100;
}
assert_eq!(x, &[10, 2, 400]);

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([0..1, 1..3]);
    a[0] = 8;
    b[0] = 88;
    b[1] = 888;
}
assert_eq!(x, &[8, 88, 888]);

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([1..=2, 0..=0]);
    a[0] = 11;
    a[1] = 111;
    b[0] = 1;
}
assert_eq!(x, &[1, 11, 111]);
```

1.86.0

·

Source

#### pub fn get_disjoint_mut<I, const N: usize>( &mut self, indices: [I; N], ) -> Result<[&mut <I as SliceIndex<[T]>>::Output; N], GetDisjointMutError>where I: GetDisjointMutIndex + SliceIndex<[T]>,

Returns mutable references to many indices at once.

An index can be either a `usize`, a `Range` or a `RangeInclusive`. Note that this method takes an array, so all indices must be of the same type. If passed an array of `usize`s this method gives back an array of mutable references to single elements, while if passed an array of ranges it gives back an array of mutable references to slices.

Returns an error if any index is out-of-bounds, or if there are overlapping indices. An empty range is not considered to overlap if it is located at the beginning or at the end of another range, but is considered to overlap if it is located in the middle.

This method does a O(n^2) check to check that there are no overlapping indices, so be careful when passing many indices.

##### §Examples

```
let v = &mut [1, 2, 3];
if let Ok([a, b]) = v.get_disjoint_mut([0, 2]) {
    *a = 413;
    *b = 612;
}
assert_eq!(v, &[413, 2, 612]);

if let Ok([a, b]) = v.get_disjoint_mut([0..1, 1..3]) {
    a[0] = 8;
    b[0] = 88;
    b[1] = 888;
}
assert_eq!(v, &[8, 88, 888]);

if let Ok([a, b]) = v.get_disjoint_mut([1..=2, 0..=0]) {
    a[0] = 11;
    a[1] = 111;
    b[0] = 1;
}
assert_eq!(v, &[1, 11, 111]);
```

1.94.0

·

Source

#### pub fn element_offset(&self, element: &T) -> Option<usize>

Returns the index that an element reference points to.

Returns `None` if `element` does not point to the start of an element within the slice.

This method is useful for extending slice iterators like `slice::split`.

Note that this uses pointer arithmetic and **does not compare elements**. To find the index of an element via comparison, use `.iter().position()` instead.

##### §Panics

Panics if `T` is zero-sized.

##### §Examples

Basic usage:

```
let nums: &[u32] = &[1, 7, 1, 1];
let num = &nums[2];

assert_eq!(num, &1);
assert_eq!(nums.element_offset(num), Some(2));
```

Returning `None` with an unaligned element:

```
let arr: &[[u32; 2]] = &[[0, 1], [2, 3]];
let flat_arr: &[u32] = arr.as_flattened();

let ok_elm: &[u32; 2] = flat_arr[0..2].try_into().unwrap();
let weird_elm: &[u32; 2] = flat_arr[1..3].try_into().unwrap();

assert_eq!(ok_elm, &[0, 1]);
assert_eq!(weird_elm, &[1, 2]);

assert_eq!(arr.element_offset(ok_elm), Some(0)); assert_eq!(arr.element_offset(weird_elm), None); 
```

Source

#### pub fn subslice_range(&self, subslice: &[T]) -> Option<Range<usize>>

🔬

This is a nightly-only experimental API. (

substr_range

#126769

)

Returns the range of indices that a subslice points to.

Returns `None` if `subslice` does not point within the slice or if it is not aligned with the elements in the slice.

This method **does not compare elements**. Instead, this method finds the location in the slice that `subslice` was obtained from. To find the index of a subslice via comparison, instead use `.windows()``.position()`.

This method is useful for extending slice iterators like `slice::split`.

Note that this may return a false positive (either `Some(0..0)` or `Some(self.len()..self.len())`) if `subslice` has a length of zero and points to the beginning or end of another, separate, slice.

##### §Panics

Panics if `T` is zero-sized.

##### §Examples

Basic usage:

```
#![feature(substr_range)]
use core::range::Range;

let nums = &[0, 5, 10, 0, 0, 5];

let mut iter = nums
    .split(|t| *t == 0)
    .map(|n| nums.subslice_range(n).unwrap());

assert_eq!(iter.next(), Some(Range { start: 0, end: 0 }));
assert_eq!(iter.next(), Some(Range { start: 1, end: 3 }));
assert_eq!(iter.next(), Some(Range { start: 4, end: 4 }));
assert_eq!(iter.next(), Some(Range { start: 5, end: 6 }));
```

Source

#### pub fn as_slice(&self) -> &[T]

🔬

This is a nightly-only experimental API. (

str_as_str

#130366

)

Returns the same slice `&[T]`.

This method is redundant when used directly on `&[T]`, but it helps dereferencing other “container” types to slices, for example `Box<[T]>` or `Arc<[T]>`.

Source

#### pub fn as_mut_slice(&mut self) -> &mut [T]

🔬

This is a nightly-only experimental API. (

str_as_str

#130366

)

Returns the same slice `&mut [T]`.

This method is redundant when used directly on `&mut [T]`, but it helps dereferencing other “container” types to slices, for example `Box<[T]>` or `MutexGuard<[T]>`.

1.0.0

·

Source

#### pub fn sort(&mut self)where T: Ord,

Sorts the slice in ascending order, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*n* * log(*n*)) worst-case.

If the implementation of `Ord` for `T` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

When applicable, unstable sorting is preferred because it is generally faster than stable sorting and it doesn’t allocate auxiliary memory. See `sort_unstable`. The exception are partially sorted slices, which may be better served with `slice::sort`.

Sorting types that only implement `PartialOrd` such as `f32` and `f64` require additional precautions. For example, `f32::NAN != f32::NAN`, which doesn’t fulfill the reflexivity requirement of `Ord`. By using an alternative comparison function with `slice::sort_by` such as `f32::total_cmp` or `f64::total_cmp` that defines a total order users can sort slices containing floating-point values. Alternatively, if all values in the slice are guaranteed to be in a subset for which `PartialOrd::partial_cmp` forms a total order, it’s possible to sort the slice with `sort_by(|a, b| a.partial_cmp(b).unwrap())`.

##### §Current implementation

The current implementation is based on driftsort by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### §Panics

May panic if the implementation of `Ord` for `T` does not implement a total order, or if the `Ord` implementation itself panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### §Examples

```
let mut v = [4, -5, 1, -3, 2];

v.sort();
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

1.0.0

·

Source

#### pub fn sort_by<F>(&mut self, compare: F)where F: FnMut(&T, &T) -> Ordering,

Sorts the slice in ascending order with a comparison function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*n* * log(*n*)) worst-case.

If the comparison function `compare` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the `Ord` documentation.

##### §Current implementation

The current implementation is based on driftsort by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### §Panics

May panic if `compare` does not implement a total order, or if `compare` itself panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### §Examples

```
let mut v = [4, -5, 1, -3, 2];
v.sort_by(|a, b| a.cmp(b));
assert_eq!(v, [-5, -3, 1, 2, 4]);

v.sort_by(|a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

1.7.0

·

Source

#### pub fn sort_by_key<K, F>(&mut self, f: F)where F: FnMut(&T) -> K, K: Ord,

Sorts the slice in ascending order with a key extraction function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*m* * *n* * log(*n*)) worst-case, where the key function is *O*(*m*).

If the implementation of `Ord` for `K` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

##### §Current implementation

The current implementation is based on driftsort by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### §Panics

May panic if the implementation of `Ord` for `K` does not implement a total order, or if the `Ord` implementation or the key-function `f` panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### §Examples

```
let mut v = [4i32, -5, 1, -3, 2];

v.sort_by_key(|k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

1.34.0

·

Source

#### pub fn sort_by_cached_key<K, F>(&mut self, f: F)where F: FnMut(&T) -> K, K: Ord,

Sorts the slice in ascending order with a key extraction function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*m* * *n* + *n* * log(*n*)) worst-case, where the key function is *O*(*m*).

During sorting, the key function is called at most once per element, by using temporary storage to remember the results of key evaluation. The order of calls to the key function is unspecified and may change in future versions of the standard library.

If the implementation of `Ord` for `K` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For simple key functions (e.g., functions that are property accesses or basic operations), `sort_by_key` is likely to be faster.

##### §Current implementation

The current implementation is based on instruction-parallel-network sort by Lukas Bergdoll, which combines the fast average case of randomized quicksort with the fast worst case of heapsort, while achieving linear time on fully sorted and reversed inputs. And *O*(*k* * log(*n*)) where *k* is the number of distinct elements in the input. It leverages superscalar out-of-order execution capabilities commonly found in CPUs, to efficiently perform the operation.

In the worst case, the algorithm allocates temporary storage in a `Vec<(K, usize)>` the length of the slice.

##### §Panics

May panic if the implementation of `Ord` for `K` does not implement a total order, or if the `Ord` implementation panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### §Examples

```
let mut v = [4i32, -5, 1, -3, 2, 10];

v.sort_by_cached_key(|k| k.to_string());
assert_eq!(v, [-3, -5, 1, 10, 2, 4]);
```

1.0.0

·

Source

#### pub fn to_vec(&self) -> Vec<T>where T: Clone,

Copies `self` into a new `Vec`.

##### §Examples

```
let s = [10, 40, 30];
let x = s.to_vec();
```

Source

#### pub fn to_vec_in<A>(&self, alloc: A) -> Vec<T, A>where A: Allocator, T: Clone,

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Copies `self` into a new `Vec` with an allocator.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let s = [10, 40, 30];
let x = s.to_vec_in(System);
```

1.40.0

·

Source

#### pub fn repeat(&self, n: usize) -> Vec<T>where T: Copy,

Creates a vector by copying a slice `n` times.

##### §Panics

This function will panic if the capacity would overflow.

##### §Examples

```
assert_eq!([1, 2].repeat(3), vec![1, 2, 1, 2, 1, 2]);
```

A panic upon overflow:

ⓘ

```
b"0123456789abcdef".repeat(usize::MAX);
```

1.0.0

·

Source

#### pub fn concat<Item>(&self) -> <[T] as Concat<Item>>::Output ⓘwhere [T]: Concat<Item>, Item: ?Sized,

Flattens a slice of `T` into a single value `Self::Output`.

##### §Examples

```
assert_eq!(["hello", "world"].concat(), "helloworld");
assert_eq!([[1, 2], [3, 4]].concat(), [1, 2, 3, 4]);
```

1.3.0

·

Source

#### pub fn join<Separator>( &self, sep: Separator, ) -> <[T] as Join<Separator>>::Output ⓘwhere [T]: Join<Separator>,

Flattens a slice of `T` into a single value `Self::Output`, placing a given separator between each.

##### §Examples

```
assert_eq!(["hello", "world"].join(" "), "hello world");
assert_eq!([[1, 2], [3, 4]].join(&0), [1, 2, 0, 3, 4]);
assert_eq!([[1, 2], [3, 4]].join(&[0, 0][..]), [1, 2, 0, 0, 3, 4]);
```

1.0.0

·

Source

#### pub fn connect<Separator>( &self, sep: Separator, ) -> <[T] as Join<Separator>>::Output ⓘwhere [T]: Join<Separator>,

👎

Deprecated since 1.3.0:

renamed to join

Flattens a slice of `T` into a single value `Self::Output`, placing a given separator between each.

##### §Examples

```
assert_eq!(["hello", "world"].connect(" "), "hello world");
assert_eq!([[1, 2], [3, 4]].connect(&0), [1, 2, 0, 3, 4]);
```
