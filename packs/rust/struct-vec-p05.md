---
title: "Vec in std::vec (part 5/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 5/7
---

# Vec in std::vec

Returns a subslice with the optional prefix removed.

If the slice starts with `prefix`, returns the subslice after the prefix. If `prefix` is empty or the slice does not start with `prefix`, simply returns the original slice. If `prefix` is equal to the original slice, returns an empty slice.

##### §Examples

```
#![feature(trim_prefix_suffix)]

let v = &[10, 40, 30];

assert_eq!(v.trim_prefix(&[10]), &[40, 30][..]);
assert_eq!(v.trim_prefix(&[10, 40]), &[30][..]);
assert_eq!(v.trim_prefix(&[10, 40, 30]), &[][..]);

assert_eq!(v.trim_prefix(&[50]), &[10, 40, 30][..]);
assert_eq!(v.trim_prefix(&[10, 50]), &[10, 40, 30][..]);

let prefix : &str = "he";
assert_eq!(b"hello".trim_prefix(prefix.as_bytes()), b"llo".as_ref());
```

Source

#### pub fn trim_suffix<P>(&self, suffix: &P) -> &[T]where P: SlicePattern<Item = T> + ?Sized, T: PartialEq,

🔬

This is a nightly-only experimental API. (

trim_prefix_suffix

#142312

)

Returns a subslice with the optional suffix removed.

If the slice ends with `suffix`, returns the subslice before the suffix. If `suffix` is empty or the slice does not end with `suffix`, simply returns the original slice. If `suffix` is equal to the original slice, returns an empty slice.

##### §Examples

```
#![feature(trim_prefix_suffix)]

let v = &[10, 40, 30];

assert_eq!(v.trim_suffix(&[30]), &[10, 40][..]);
assert_eq!(v.trim_suffix(&[40, 30]), &[10][..]);
assert_eq!(v.trim_suffix(&[10, 40, 30]), &[][..]);

assert_eq!(v.trim_suffix(&[50]), &[10, 40, 30][..]);
assert_eq!(v.trim_suffix(&[50, 30]), &[10, 40, 30][..]);
```

Binary searches this slice for a given element. If the slice is not sorted, the returned result is unspecified and meaningless.

If the value is found then `Result::Ok` is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then `Result::Err` is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also `binary_search_by`, `binary_search_by_key`, and `partition_point`.

##### §Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

assert_eq!(s.binary_search(&13),  Ok(9));
assert_eq!(s.binary_search(&4),   Err(7));
assert_eq!(s.binary_search(&100), Err(13));
let r = s.binary_search(&1);
assert!(match r { Ok(1..=4) => true, _ => false, });
```

If you want to find that whole *range* of matching items, rather than an arbitrary matching one, that can be done using `partition_point`:

```
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

let low = s.partition_point(|x| x < &1);
assert_eq!(low, 1);
let high = s.partition_point(|x| x <= &1);
assert_eq!(high, 5);
let r = s.binary_search(&1);
assert!((low..high).contains(&r.unwrap()));

assert!(s[..low].iter().all(|&x| x < 1));
assert!(s[low..high].iter().all(|&x| x == 1));
assert!(s[high..].iter().all(|&x| x > 1));

assert_eq!(s.partition_point(|x| x < &11), 9);
assert_eq!(s.partition_point(|x| x <= &11), 9);
assert_eq!(s.binary_search(&11), Err(9));
```

If you want to insert an item to a sorted vector, while maintaining sort order, consider using `partition_point`:

```
let mut s = vec![0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
let num = 42;
let idx = s.partition_point(|&x| x <= num);
s.insert(idx, num);
assert_eq!(s, [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

Binary searches this slice with a comparator function.

The comparator function should return an order code that indicates whether its argument is `Less`, `Equal` or `Greater` the desired target. If the slice is not sorted or if the comparator function does not implement an order consistent with the sort order of the underlying slice, the returned result is unspecified and meaningless.

If the value is found then `Result::Ok` is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then `Result::Err` is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also `binary_search`, `binary_search_by_key`, and `partition_point`.

##### §Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

let seek = 13;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Ok(9));
let seek = 4;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Err(7));
let seek = 100;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Err(13));
let seek = 1;
let r = s.binary_search_by(|probe| probe.cmp(&seek));
assert!(match r { Ok(1..=4) => true, _ => false, });
```

Binary searches this slice with a key extraction function.

Assumes that the slice is sorted by the key, for instance with `sort_by_key` using the same key extraction function. If the slice is not sorted by the key, the returned result is unspecified and meaningless.

If the value is found then `Result::Ok` is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then `Result::Err` is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also `binary_search`, `binary_search_by`, and `partition_point`.

##### §Examples

Looks up a series of four elements in a slice of pairs sorted by their second elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```
let s = [(0, 0), (2, 1), (4, 1), (5, 1), (3, 1),
         (1, 2), (2, 3), (4, 5), (5, 8), (3, 13),
         (1, 21), (2, 34), (4, 55)];

assert_eq!(s.binary_search_by_key(&13, |&(a, b)| b),  Ok(9));
assert_eq!(s.binary_search_by_key(&4, |&(a, b)| b),   Err(7));
assert_eq!(s.binary_search_by_key(&100, |&(a, b)| b), Err(13));
let r = s.binary_search_by_key(&1, |&(a, b)| b);
assert!(match r { Ok(1..=4) => true, _ => false, });
```

1.20.0

·

Source

#### pub fn sort_unstable(&mut self)where T: Ord,

Sorts the slice in ascending order **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the implementation of `Ord` for `T` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the `Ord` documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if the implementation of `Ord` for `T` panics.

Sorting types that only implement `PartialOrd` such as `f32` and `f64` require additional precautions. For example, `f32::NAN != f32::NAN`, which doesn’t fulfill the reflexivity requirement of `Ord`. By using an alternative comparison function with `slice::sort_unstable_by` such as `f32::total_cmp` or `f64::total_cmp` that defines a total order users can sort slices containing floating-point values. Alternatively, if all values in the slice are guaranteed to be in a subset for which `PartialOrd::partial_cmp` forms a total order, it’s possible to sort the slice with `sort_unstable_by(|a, b| a.partial_cmp(b).unwrap())`.

##### §Current implementation

The current implementation is based on ipnsort by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### §Panics

May panic if the implementation of `Ord` for `T` does not implement a total order, or if the `Ord` implementation panics.

##### §Examples

```
let mut v = [4, -5, 1, -3, 2];

v.sort_unstable();
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

1.20.0

·

Source

#### pub fn sort_unstable_by<F>(&mut self, compare: F)where F: FnMut(&T, &T) -> Ordering,

Sorts the slice in ascending order with a comparison function, **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the comparison function `compare` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the `Ord` documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if `compare` panics.

##### §Current implementation

The current implementation is based on ipnsort by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### §Panics

May panic if the `compare` does not implement a total order, or if the `compare` itself panics.

##### §Examples

```
let mut v = [4, -5, 1, -3, 2];
v.sort_unstable_by(|a, b| a.cmp(b));
assert_eq!(v, [-5, -3, 1, 2, 4]);

v.sort_unstable_by(|a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

1.20.0

·

Source

#### pub fn sort_unstable_by_key<K, F>(&mut self, f: F)where F: FnMut(&T) -> K, K: Ord,

Sorts the slice in ascending order with a key extraction function, **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the implementation of `Ord` for `K` does not implement a total order, the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the `Ord` documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if the implementation of `Ord` for `K` panics.

##### §Current implementation

The current implementation is based on ipnsort by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### §Panics

May panic if the implementation of `Ord` for `K` does not implement a total order, or if the `Ord` implementation panics.

##### §Examples

```
let mut v = [4i32, -5, 1, -3, 2];

v.sort_unstable_by_key(|k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

Source

#### pub fn partial_sort_unstable<R>(&mut self, range: R)where T: Ord, R: RangeBounds<usize>,

🔬

This is a nightly-only experimental API. (

slice_partial_sort_unstable

#149046

)

Partially sorts the slice in ascending order **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of `sort_unstable` for implementation notes.

##### §Panics

May panic if the implementation of `Ord` for `T` does not implement a total order, or if the `Ord` implementation panics, or if the specified range is out of bounds.

##### §Examples

```
#![feature(slice_partial_sort_unstable)]

let mut v = [4, -5, 1, -3, 2];

v.partial_sort_unstable(0..0);
assert_eq!(v, [4, -5, 1, -3, 2]);

v.partial_sort_unstable(2..2);
for i in 0..2 {
   assert!(v[i] <= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] <= v[i]);
}

v.partial_sort_unstable(2..3);
for i in 0..2 {
   assert!(v[i] <= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] <= v[i]);
}

v.partial_sort_unstable(1..4);
assert_eq!(&v[1..4], [-3, 1, 2]);

v.partial_sort_unstable(..);
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

Source

#### pub fn partial_sort_unstable_by<F, R>(&mut self, range: R, compare: F)where F: FnMut(&T, &T) -> Ordering, R: RangeBounds<usize>,

🔬

This is a nightly-only experimental API. (

slice_partial_sort_unstable

#149046

)

Partially sorts the slice in ascending order with a comparison function, **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of `sort_unstable_by` for implementation notes.

##### §Panics

May panic if the `compare` does not implement a total order, or if the `compare` itself panics, or if the specified range is out of bounds.

##### §Examples

```
#![feature(slice_partial_sort_unstable)]

let mut v = [4, -5, 1, -3, 2];

v.partial_sort_unstable_by(0..0, |a, b| b.cmp(a));
assert_eq!(v, [4, -5, 1, -3, 2]);

v.partial_sort_unstable_by(2..2, |a, b| b.cmp(a));
for i in 0..2 {
   assert!(v[i] >= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] >= v[i]);
}

v.partial_sort_unstable_by(2..3, |a, b| b.cmp(a));
for i in 0..2 {
   assert!(v[i] >= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] >= v[i]);
}

v.partial_sort_unstable_by(1..4, |a, b| b.cmp(a));
assert_eq!(&v[1..4], [2, 1, -3]);

v.partial_sort_unstable_by(.., |a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

Source

#### pub fn partial_sort_unstable_by_key<K, F, R>(&mut self, range: R, f: F)where F: FnMut(&T) -> K, K: Ord, R: RangeBounds<usize>,

🔬

This is a nightly-only experimental API. (

slice_partial_sort_unstable

#149046

)

Partially sorts the slice in ascending order with a key extraction function, **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of `sort_unstable_by_key` for implementation notes.

##### §Panics

May panic if the implementation of `Ord` for `K` does not implement a total order, or if the `Ord` implementation panics, or if the specified range is out of bounds.

##### §Examples

```
#![feature(slice_partial_sort_unstable)]

let mut v = [4i32, -5, 1, -3, 2];

v.partial_sort_unstable_by_key(0..0, |k| k.abs());
assert_eq!(v, [4, -5, 1, -3, 2]);

v.partial_sort_unstable_by_key(2..2, |k| k.abs());
for i in 0..2 {
   assert!(v[i].abs() <= v[2].abs());
}
for i in 3..v.len() {
  assert!(v[2].abs() <= v[i].abs());
}

v.partial_sort_unstable_by_key(2..3, |k| k.abs());
for i in 0..2 {
   assert!(v[i].abs() <= v[2].abs());
}
for i in 3..v.len() {
  assert!(v[2].abs() <= v[i].abs());
}

v.partial_sort_unstable_by_key(1..4, |k| k.abs());
assert_eq!(&v[1..4], [2, -3, 4]);

v.partial_sort_unstable_by_key(.., |k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

1.49.0

·

Source

#### pub fn select_nth_unstable( &mut self, index: usize, ) -> (&mut [T], &mut T, &mut [T])where T: Ord,

Reorders the slice such that the element at `index` is at a sort-order position. All elements before `index` will be `<=` to this value, and all elements after will be `>=` to it.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple that partitions the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `x <= self[index]`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `x >= self[index]`.

##### §Current implementation

The current algorithm is an introselect implementation based on ipnsort by Lukas Bergdoll and Orson Peters, which is also the basis for `sort_unstable`. The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### §Panics

Panics when `index >= len()`, and so always panics on empty slices.

May panic if the implementation of `Ord` for `T` does not implement a total order.

##### §Examples

```
let mut v = [-5i32, 4, 2, -3, 1];

let (lesser, median, greater) = v.select_nth_unstable(2);

assert!(lesser == [-3, -5] || lesser == [-5, -3]);
assert_eq!(median, &mut 1);
assert!(greater == [4, 2] || greater == [2, 4]);

assert!(v == [-3, -5, 1, 2, 4] ||
        v == [-5, -3, 1, 2, 4] ||
        v == [-3, -5, 1, 4, 2] ||
        v == [-5, -3, 1, 4, 2]);
```

1.49.0

·

Source

#### pub fn select_nth_unstable_by<F>( &mut self, index: usize, compare: F, ) -> (&mut [T], &mut T, &mut [T])where F: FnMut(&T, &T) -> Ordering,

Reorders the slice with a comparator function such that the element at `index` is at a sort-order position. All elements before `index` will be `<=` to this value, and all elements after will be `>=` to it, according to the comparator function.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple partitioning the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `compare(x, self[index]).is_le()`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `compare(x, self[index]).is_ge()`.

##### §Current implementation

The current algorithm is an introselect implementation based on ipnsort by Lukas Bergdoll and Orson Peters, which is also the basis for `sort_unstable`. The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### §Panics

Panics when `index >= len()`, and so always panics on empty slices.

May panic if `compare` does not implement a total order.

##### §Examples

```
let mut v = [-5i32, 4, 2, -3, 1];

let (before, median, after) = v.select_nth_unstable_by(2, |a, b| b.cmp(a));

assert!(before == [4, 2] || before == [2, 4]);
assert_eq!(median, &mut 1);
assert!(after == [-3, -5] || after == [-5, -3]);

assert!(v == [2, 4, 1, -5, -3] ||
        v == [2, 4, 1, -3, -5] ||
        v == [4, 2, 1, -5, -3] ||
        v == [4, 2, 1, -3, -5]);
```

1.49.0

·

Source

#### pub fn select_nth_unstable_by_key<K, F>( &mut self, index: usize, f: F, ) -> (&mut [T], &mut T, &mut [T])where F: FnMut(&T) -> K, K: Ord,

Reorders the slice with a key extraction function such that the element at `index` is at a sort-order position. All elements before `index` will have keys `<=` to the key at `index`, and all elements after will have keys `>=` to it.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple partitioning the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `f(x) <= f(self[index])`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `f(x) >= f(self[index])`.

##### §Current implementation

The current algorithm is an introselect implementation based on ipnsort by Lukas Bergdoll and Orson Peters, which is also the basis for `sort_unstable`. The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### §Panics

Panics when `index >= len()`, meaning it always panics on empty slices.

May panic if `K: Ord` does not implement a total order.

##### §Examples

```
let mut v = [-5i32, 4, 1, -3, 2];

let (lesser, median, greater) = v.select_nth_unstable_by_key(2, |a| a.abs());

assert!(lesser == [1, 2] || lesser == [2, 1]);
assert_eq!(median, &mut -3);
assert!(greater == [4, -5] || greater == [-5, 4]);

assert!(v == [1, 2, -3, 4, -5] ||
        v == [1, 2, -3, -5, 4] ||
        v == [2, 1, -3, 4, -5] ||
        v == [2, 1, -3, -5, 4]);
```

Source

#### pub fn partition_dedup(&mut self) -> (&mut [T], &mut [T])where T: PartialEq,

🔬

This is a nightly-only experimental API. (

slice_partition_dedup

#54279

)

Moves all consecutive repeated elements to the end of the slice according to the `PartialEq` trait implementation.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

If the slice is sorted, the first returned slice contains no duplicates.

##### §Examples

```
#![feature(slice_partition_dedup)]

let mut slice = [1, 2, 2, 3, 3, 2, 1, 1];

let (dedup, duplicates) = slice.partition_dedup();

assert_eq!(dedup, [1, 2, 3, 2, 1]);
assert_eq!(duplicates, [2, 3, 1]);
```

Source

#### pub fn partition_dedup_by<F>(&mut self, same_bucket: F) -> (&mut [T], &mut [T])where F: FnMut(&mut T, &mut T) -> bool,

🔬

This is a nightly-only experimental API. (

slice_partition_dedup

#54279

)

Moves all but the first of consecutive elements to the end of the slice satisfying a given equality relation.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

The `same_bucket` function is passed references to two elements from the slice and must determine if the elements compare equal. The elements are passed in opposite order from their order in the slice, so if `same_bucket(a, b)` returns `true`, `a` is moved at the end of the slice.

If the slice is sorted, the first returned slice contains no duplicates.

##### §Examples

```
#![feature(slice_partition_dedup)]

let mut slice = ["foo", "Foo", "BAZ", "Bar", "bar", "baz", "BAZ"];

let (dedup, duplicates) = slice.partition_dedup_by(|a, b| a.eq_ignore_ascii_case(b));

assert_eq!(dedup, ["foo", "BAZ", "Bar", "baz"]);
assert_eq!(duplicates, ["bar", "Foo", "BAZ"]);
```

Source

#### pub fn partition_dedup_by_key<K, F>(&mut self, key: F) -> (&mut [T], &mut [T])where F: FnMut(&mut T) -> K, K: PartialEq,

🔬

This is a nightly-only experimental API. (

slice_partition_dedup

#54279

)

Moves all but the first of consecutive elements to the end of the slice that resolve to the same key.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

If the slice is sorted, the first returned slice contains no duplicates.

##### §Examples

```
#![feature(slice_partition_dedup)]

let mut slice = [10, 20, 21, 30, 30, 20, 11, 13];

let (dedup, duplicates) = slice.partition_dedup_by_key(|i| *i / 10);

assert_eq!(dedup, [10, 20, 30, 20, 11]);
assert_eq!(duplicates, [21, 30, 13]);
```

1.26.0

·

Source

#### pub fn rotate_left(&mut self, mid: usize)

Rotates the slice in-place such that the first `mid` elements of the slice move to the end while the last `self.len() - mid` elements move to the front.

After calling `rotate_left`, the element previously at index `mid` will become the first element in the slice.

##### §Panics

This function will panic if `mid` is greater than the length of the slice. Note that `mid == self.len()` does *not* panic and is a no-op rotation.

##### §Complexity

Takes linear (in `self.len()`) time.

##### §Examples

```
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.rotate_left(2);
assert_eq!(a, ['c', 'd', 'e', 'f', 'a', 'b']);
```

Rotating a subslice:

```
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a[1..5].rotate_left(1);
assert_eq!(a, ['a', 'c', 'd', 'e', 'b', 'f']);
```

1.26.0

·

Source

#### pub fn rotate_right(&mut self, k: usize)

Rotates the slice in-place such that the first `self.len() - k` elements of the slice move to the end while the last `k` elements move to the front.

After calling `rotate_right`, the element previously at index `self.len() - k` will become the first element in the slice.

##### §Panics

This function will panic if `k` is greater than the length of the slice. Note that `k == self.len()` does *not* panic and is a no-op rotation.

##### §Complexity

Takes linear (in `self.len()`) time.

##### §Examples

```
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.rotate_right(2);
assert_eq!(a, ['e', 'f', 'a', 'b', 'c', 'd']);
```

Rotating a subslice:

```
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a[1..5].rotate_right(1);
assert_eq!(a, ['a', 'e', 'b', 'c', 'd', 'f']);
```

Source

#### pub fn shift_left<const N: usize>(&mut self, inserted: [T; N]) -> [T; N]

🔬

This is a nightly-only experimental API. (

slice_shift

#151772

)

Moves the elements of this slice `N` places to the left, returning the ones that “fall off” the front, and putting `inserted` at the end.

Equivalently, you can think of concatenating `self` and `inserted` into one long sequence, then returning the left-most `N` items and the rest into `self`:

```
          self (before)    inserted
          vvvvvvvvvvvvvvv  vvv
          [1, 2, 3, 4, 5]  [9]
       ↙   ↙  ↙  ↙  ↙   ↙
     [1]  [2, 3, 4, 5, 9]
     ^^^  ^^^^^^^^^^^^^^^
returned  self (after)
```

See also `Self::shift_right` and compare `Self::rotate_left`.

##### §Examples

```
#![feature(slice_shift)]

let mut a = [1, 2, 3, 4, 5];
let inserted = [9];
let returned = a.shift_left(inserted);
assert_eq!(returned, [1]);
assert_eq!(a, [2, 3, 4, 5, 9]);

let mut a = *b"Hello world";
assert_eq!(a.shift_left(*b" peace"), *b"Hello ");
assert_eq!(a, *b"world peace");

let mut a: u8 = 0b10010110;
a <<= 3;
assert_eq!(a, 0b10110000_u8);
let mut a: [_; 8] = [1, 0, 0, 1, 0, 1, 1, 0];
a.shift_left([0; 3]);
assert_eq!(a, [1, 0, 1, 1, 0, 0, 0, 0]);

let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
assert_eq!(a[1..=4].shift_left(['Z']), ['b']);
assert_eq!(a, ['a', 'c', 'd', 'e', 'Z', 'f']);

let mut a = [1, 2, 3];
assert_eq!(a.shift_left([7, 8, 9]), [1, 2, 3]);
assert_eq!(a, [7, 8, 9]);

let mut a = [];
assert_eq!(a.shift_left([1, 2, 3]), [1, 2, 3]);
let mut a = [9];
assert_eq!(a.shift_left([1, 2, 3]), [9, 1, 2]);
assert_eq!(a, [3]);
```

Source

#### pub fn shift_right<const N: usize>(&mut self, inserted: [T; N]) -> [T; N]

🔬

This is a nightly-only experimental API. (

slice_shift

#151772

)

Moves the elements of this slice `N` places to the right, returning the ones that “fall off” the back, and putting `inserted` at the beginning.

Equivalently, you can think of concatenating `inserted` and `self` into one long sequence, then returning the right-most `N` items and the rest into `self`:

```
inserted  self (before)
     vvv  vvvvvvvvvvvvvvv
     [0]  [5, 6, 7, 8, 9]
       ↘   ↘  ↘  ↘  ↘   ↘
          [0, 5, 6, 7, 8]  [9]
          ^^^^^^^^^^^^^^^  ^^^
          self (after)     returned
```

See also `Self::shift_left` and compare `Self::rotate_right`.

##### §Examples

```
#![feature(slice_shift)]

let mut a = [5, 6, 7, 8, 9];
let inserted = [0];
let returned = a.shift_right(inserted);
assert_eq!(returned, [9]);
assert_eq!(a, [0, 5, 6, 7, 8]);

let mut a: u8 = 0b10010110;
a >>= 3;
assert_eq!(a, 0b00010010_u8);
let mut a: [_; 8] = [1, 0, 0, 1, 0, 1, 1, 0];
a.shift_right([0; 3]);
assert_eq!(a, [0, 0, 0, 1, 0, 0, 1, 0]);

let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
assert_eq!(a[1..=4].shift_right(['Z']), ['e']);
assert_eq!(a, ['a', 'Z', 'b', 'c', 'd', 'f']);

let mut a = [1, 2, 3];
assert_eq!(a.shift_right([7, 8, 9]), [1, 2, 3]);
assert_eq!(a, [7, 8, 9]);

let mut a = [];
assert_eq!(a.shift_right([1, 2, 3]), [1, 2, 3]);
let mut a = [9];
assert_eq!(a.shift_right([1, 2, 3]), [2, 3, 9]);
assert_eq!(a, [1]);
```

1.50.0

·

Source

#### pub fn fill(&mut self, value: T)where T: Clone,

Fills `self` with elements by cloning `value`.

##### §Examples

```
let mut buf = vec![0; 10];
buf.fill(1);
assert_eq!(buf, vec![1; 10]);
```

1.51.0

·

Source

#### pub fn fill_with<F>(&mut self, f: F)where F: FnMut() -> T,

Fills `self` with elements returned by calling a closure repeatedly.

This method uses a closure to create new values. If you’d rather `Clone` a given value, use `fill`. If you want to use the `Default` trait to generate values, you can pass `Default::default` as the argument.

##### §Examples

```
let mut buf = vec![1; 10];
buf.fill_with(Default::default);
assert_eq!(buf, vec![0; 10]);
```

1.7.0

·

Source

#### pub fn clone_from_slice(&mut self, src: &[T])where T: Clone,

Copies the elements from `src` into `self`.

The length of `src` must be the same as `self`.

##### §Panics

This function will panic if the two slices have different lengths.

##### §Examples

Cloning two elements from a slice into another:

```
let src = [1, 2, 3, 4];
let mut dst = [0, 0];

dst.clone_from_slice(&src[2..]);

assert_eq!(src, [1, 2, 3, 4]);
assert_eq!(dst, [3, 4]);
```

Rust enforces that there can only be one mutable reference with no immutable references to a particular piece of data in a particular scope. Because of this, attempting to use `clone_from_slice` on a single slice will result in a compile failure:

ⓘ

```
let mut slice = [1, 2, 3, 4, 5];

slice[..2].clone_from_slice(&slice[3..]); 
```

To work around this, we can use `split_at_mut` to create two distinct sub-slices from a slice:

```
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.clone_from_slice(&right[1..]);
}

assert_eq!(slice, [4, 5, 3, 4, 5]);
```

1.9.0

·

Source

#### pub fn copy_from_slice(&mut self, src: &[T])where T: Copy,

Copies all elements from `src` into `self`, using a memcpy.

The length of `src` must be the same as `self`.

If `T` does not implement `Copy`, use `clone_from_slice`.

##### §Panics

This function will panic if the two slices have different lengths.

##### §Examples

Copying two elements from a slice into another:

```
let src = [1, 2, 3, 4];
let mut dst = [0, 0];

dst.copy_from_slice(&src[2..]);

assert_eq!(src, [1, 2, 3, 4]);
assert_eq!(dst, [3, 4]);
```

Rust enforces that there can only be one mutable reference with no immutable references to a particular piece of data in a particular scope. Because of this, attempting to use `copy_from_slice` on a single slice will result in a compile failure:

ⓘ

```
let mut slice = [1, 2, 3, 4, 5];

slice[..2].copy_from_slice(&slice[3..]); 
```

To work around this, we can use `split_at_mut` to create two distinct sub-slices from a slice:

```
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.copy_from_slice(&right[1..]);
}

assert_eq!(slice, [4, 5, 3, 4, 5]);
```

1.37.0

·

Source

#### pub fn copy_within<R>(&mut self, src: R, dest: usize)where R: RangeBounds<usize>, T: Copy,

Copies elements from one part of the slice to another part of itself, using a memmove.
