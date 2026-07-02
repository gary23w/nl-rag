---
title: "Vec in std::vec (part 2/7)"
source: https://doc.rust-lang.org/std/vec/struct.Vec.html
domain: rust
license: MIT OR Apache-2.0
tags: rust, cargo, borrow checker, rustc
fetched: 2026-07-02
part: 2/7
---

## Implementations

Source

§

### impl<T> Vec<T>

1.0.0 (const: 1.39.0)

·

Source

#### pub const fn new() -> Vec<T>

Constructs a new, empty `Vec<T>`.

The vector will not allocate until elements are pushed onto it.

##### §Examples

```
let mut vec: Vec<i32> = Vec::new();
```

1.0.0 (const:

unstable

)

·

Source

#### pub fn with_capacity(capacity: usize) -> Vec<T>

Constructs a new, empty `Vec<T>` with at least the specified capacity.

The vector will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the vector will not allocate.

It is important to note that although the returned vector has the minimum *capacity* specified, the vector will have a zero *length*. For an explanation of the difference between length and capacity, see *Capacity and reallocation*.

If it is important to know the exact allocated capacity of a `Vec`, always use the `capacity` method after construction.

For `Vec<T>` where `T` is a zero-sized type, there will be no allocation and the capacity will always be `usize::MAX`.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = Vec::with_capacity(10);

assert_eq!(vec.len(), 0);
assert!(vec.capacity() >= 10);

for i in 0..10 {
    vec.push(i);
}
assert_eq!(vec.len(), 10);
assert!(vec.capacity() >= 10);

vec.push(11);
assert_eq!(vec.len(), 11);
assert!(vec.capacity() >= 11);

let vec_units = Vec::<()>::with_capacity(10);
assert_eq!(vec_units.capacity(), usize::MAX);
```

Source

#### pub fn try_with_capacity(capacity: usize) -> Result<Vec<T>, TryReserveError>

🔬

This is a nightly-only experimental API. (

try_with_capacity

#91913

)

Constructs a new, empty `Vec<T>` with at least the specified capacity.

The vector will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the vector will not allocate.

##### §Errors

Returns an error if the capacity exceeds `isize::MAX` *bytes*, or if the allocator reports allocation failure.

1.0.0 (const:

unstable

)

·

Source

#### pub unsafe fn from_raw_parts( ptr: *mut T, length: usize, capacity: usize, ) -> Vec<T>

Creates a `Vec<T>` directly from a pointer, a length, and a capacity.

##### §Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- If `T` is not a zero-sized type and the capacity is nonzero, `ptr` must have been allocated using the global allocator, such as via the `alloc::alloc` function. If `T` is a zero-sized type or the capacity is zero, `ptr` need only be non-null and aligned.
- `T` needs to have the same alignment as what `ptr` was allocated with, if the pointer is required to be allocated. (`T` having a less strict alignment is not sufficient, the alignment really needs to be equal to satisfy the `dealloc` requirement that memory must be allocated and deallocated with the same layout.)
- The size of `T` times the `capacity` (i.e. the allocated size in bytes), if nonzero, needs to be the same size as the pointer was allocated with. (Because similar to alignment, `dealloc` must be called with the same layout `size`.)
- `length` needs to be less than or equal to `capacity`.
- The first `length` values must be properly initialized values of type `T`.
- `capacity` needs to be the capacity that the pointer was allocated with, if the pointer is required to be allocated.
- The allocated size in bytes must be no larger than `isize::MAX`. See the safety documentation of `pointer::offset`.

These requirements are always upheld by any `ptr` that has been allocated via `Vec<T>`. Other allocation sources are allowed if the invariants are upheld.

Violating these may cause problems like corrupting the allocator’s internal data structures. For example it is normally **not** safe to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`, doing so is only safe if the array was initially allocated by a `Vec` or `String`. It’s also not safe to build one from a `Vec<u16>` and its length, because the allocator cares about the alignment, and these two types have different alignments. The buffer was allocated with alignment 2 (for `u16`), but after turning it into a `Vec<u8>` it’ll be deallocated with alignment 1. To avoid these issues, it is often preferable to do casting/transmuting using `slice::from_raw_parts` instead.

The ownership of `ptr` is effectively transferred to the `Vec<T>` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### §Examples

```
use std::ptr;

let v = vec![1, 2, 3];

let (p, len, cap) = v.into_raw_parts();

unsafe {
    for i in 0..len {
        ptr::write(p.add(i), 4 + i);
    }

    let rebuilt = Vec::from_raw_parts(p, len, cap);
    assert_eq!(rebuilt, [4, 5, 6]);
}
```

Using memory that was allocated elsewhere:

```
use std::alloc::{alloc, Layout};

fn main() {
    let layout = Layout::array::<u32>(16).expect("overflow cannot happen");

    let vec = unsafe {
        let mem = alloc(layout).cast::<u32>();
        if mem.is_null() {
            return;
        }

        mem.write(1_000_000);

        Vec::from_raw_parts(mem, 1, 16)
    };

    assert_eq!(vec, &[1_000_000]);
    assert_eq!(vec.capacity(), 16);
}
```

Source

#### pub const unsafe fn from_parts( ptr: NonNull<T>, length: usize, capacity: usize, ) -> Vec<T>

🔬

This is a nightly-only experimental API. (

box_vec_non_null

#130364

)

Creates a `Vec<T>` directly from a `NonNull` pointer, a length, and a capacity.

##### §Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- `ptr` must have been allocated using the global allocator, such as via the `alloc::alloc` function.
- `T` needs to have the same alignment as what `ptr` was allocated with. (`T` having a less strict alignment is not sufficient, the alignment really needs to be equal to satisfy the `dealloc` requirement that memory must be allocated and deallocated with the same layout.)
- The size of `T` times the `capacity` (i.e. the allocated size in bytes) needs to be the same size as the pointer was allocated with. (Because similar to alignment, `dealloc` must be called with the same layout `size`.)
- `length` needs to be less than or equal to `capacity`.
- The first `length` values must be properly initialized values of type `T`.
- `capacity` needs to be the capacity that the pointer was allocated with.
- The allocated size in bytes must be no larger than `isize::MAX`. See the safety documentation of `pointer::offset`.

These requirements are always upheld by any `ptr` that has been allocated via `Vec<T>`. Other allocation sources are allowed if the invariants are upheld.

Violating these may cause problems like corrupting the allocator’s internal data structures. For example it is normally **not** safe to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`, doing so is only safe if the array was initially allocated by a `Vec` or `String`. It’s also not safe to build one from a `Vec<u16>` and its length, because the allocator cares about the alignment, and these two types have different alignments. The buffer was allocated with alignment 2 (for `u16`), but after turning it into a `Vec<u8>` it’ll be deallocated with alignment 1. To avoid these issues, it is often preferable to do casting/transmuting using `NonNull::slice_from_raw_parts` instead.

The ownership of `ptr` is effectively transferred to the `Vec<T>` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### §Examples

```
#![feature(box_vec_non_null)]

let v = vec![1, 2, 3];

let (p, len, cap) = v.into_parts();

unsafe {
    for i in 0..len {
        p.add(i).write(4 + i);
    }

    let rebuilt = Vec::from_parts(p, len, cap);
    assert_eq!(rebuilt, [4, 5, 6]);
}
```

Using memory that was allocated elsewhere:

```
#![feature(box_vec_non_null)]

use std::alloc::{alloc, Layout};
use std::ptr::NonNull;

fn main() {
    let layout = Layout::array::<u32>(16).expect("overflow cannot happen");

    let vec = unsafe {
        let Some(mem) = NonNull::new(alloc(layout).cast::<u32>()) else {
            return;
        };

        mem.write(1_000_000);

        Vec::from_parts(mem, 1, 16)
    };

    assert_eq!(vec, &[1_000_000]);
    assert_eq!(vec.capacity(), 16);
}
```

Source

#### pub fn from_fn<F>(length: usize, f: F) -> Vec<T>where F: FnMut(usize) -> T,

🔬

This is a nightly-only experimental API. (

vec_from_fn

#149698

)

Creates a `Vec<T>` where each element is produced by calling `f` with that element’s index while walking forward through the `Vec<T>`.

This is essentially the same as writing

```
vec![f(0), f(1), f(2), …, f(length - 2), f(length - 1)]
```

and is similar to `(0..i).map(f)`, just for `Vec<T>`s not iterators.

If `length == 0`, this produces an empty `Vec<T>` without ever calling `f`.

##### §Example

```
#![feature(vec_from_fn)]

let vec = Vec::from_fn(5, |i| i);

assert_eq!(vec, [0, 1, 2, 3, 4]);

let vec2 = Vec::from_fn(8, |i| i * 2);

assert_eq!(vec2, [0, 2, 4, 6, 8, 10, 12, 14]);

let bool_vec = Vec::from_fn(5, |i| i % 2 == 0);

assert_eq!(bool_vec, [true, false, true, false, true]);
```

The `Vec<T>` is generated in ascending index order, starting from the front and going towards the back, so you can use closures with mutable state:

```
#![feature(vec_from_fn)]

let mut state = 1;
let a = Vec::from_fn(6, |_| { let x = state; state *= 2; x });

assert_eq!(a, [1, 2, 4, 8, 16, 32]);
```

1.93.0 (const:

unstable

)

·

Source

#### pub fn into_raw_parts(self) -> (*mut T, usize, usize)

Decomposes a `Vec<T>` into its raw components: `(pointer, length, capacity)`.

Returns the raw pointer to the underlying data, the length of the vector (in elements), and the allocated capacity of the data (in elements). These are the same arguments in the same order as the arguments to `from_raw_parts`.

After calling this function, the caller is responsible for the memory previously managed by the `Vec`. Most often, one does this by converting the raw pointer, length, and capacity back into a `Vec` with the `from_raw_parts` function; more generally, if `T` is non-zero-sized and the capacity is nonzero, one may use any method that calls `dealloc` with a layout of `Layout::array::<T>(capacity)`; if `T` is zero-sized or the capacity is zero, nothing needs to be done.

##### §Examples

```
let v: Vec<i32> = vec![-1, 0, 1];

let (ptr, len, cap) = v.into_raw_parts();

let rebuilt = unsafe {
    let ptr = ptr as *mut u32;

    Vec::from_raw_parts(ptr, len, cap)
};
assert_eq!(rebuilt, [4294967295, 0, 1]);
```

Source

#### pub const fn into_parts(self) -> (NonNull<T>, usize, usize)

🔬

This is a nightly-only experimental API. (

box_vec_non_null

#130364

)

Decomposes a `Vec<T>` into its raw components: `(NonNull pointer, length, capacity)`.

Returns the `NonNull` pointer to the underlying data, the length of the vector (in elements), and the allocated capacity of the data (in elements). These are the same arguments in the same order as the arguments to `from_parts`.

After calling this function, the caller is responsible for the memory previously managed by the `Vec`. The only way to do this is to convert the `NonNull` pointer, length, and capacity back into a `Vec` with the `from_parts` function, allowing the destructor to perform the cleanup.

##### §Examples

```
#![feature(box_vec_non_null)]

let v: Vec<i32> = vec![-1, 0, 1];

let (ptr, len, cap) = v.into_parts();

let rebuilt = unsafe {
    let ptr = ptr.cast::<u32>();

    Vec::from_parts(ptr, len, cap)
};
assert_eq!(rebuilt, [4294967295, 0, 1]);
```

Source

#### pub const fn const_make_global(self) -> &'static [T]where T: Freeze,

🔬

This is a nightly-only experimental API. (

const_heap

#79597

)

Interns the `Vec<T>`, making the underlying memory read-only. This method should be called during compile time. (This is a no-op if called during runtime)

This method must be called if the memory used by `Vec` needs to appear in the final values of constants.

Source

§

### impl<T, A> Vec<T, A>where A: Allocator,

Source

#### pub const fn with_capacity_in(capacity: usize, alloc: A) -> Vec<T, A>

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Constructs a new, empty `Vec<T, A>` with at least the specified capacity with the provided allocator.

The vector will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the vector will not allocate.

It is important to note that although the returned vector has the minimum *capacity* specified, the vector will have a zero *length*. For an explanation of the difference between length and capacity, see *Capacity and reallocation*.

If it is important to know the exact allocated capacity of a `Vec`, always use the `capacity` method after construction.

For `Vec<T, A>` where `T` is a zero-sized type, there will be no allocation and the capacity will always be `usize::MAX`.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let mut vec = Vec::with_capacity_in(10, System);

assert_eq!(vec.len(), 0);
assert!(vec.capacity() >= 10);

for i in 0..10 {
    vec.push(i);
}
assert_eq!(vec.len(), 10);
assert!(vec.capacity() >= 10);

vec.push(11);
assert_eq!(vec.len(), 11);
assert!(vec.capacity() >= 11);

let vec_units = Vec::<(), System>::with_capacity_in(10, System);
assert_eq!(vec_units.capacity(), usize::MAX);
```

1.0.0 (const:

unstable

)

·

Source

#### pub fn push(&mut self, value: T)

Appends an element to the back of a collection.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1, 2];
vec.push(3);
assert_eq!(vec, [1, 2, 3]);
```

##### §Time complexity

Takes amortized *O*(1) time. If the vector’s length would exceed its capacity after the push, *O*(*capacity*) time is taken to copy the vector’s elements to a larger allocation. This expensive operation is offset by the *capacity* *O*(1) insertions it allows.

1.95.0 (const:

unstable

)

·

Source

#### pub fn push_mut(&mut self, value: T) -> &mut T

Appends an element to the back of a collection, returning a reference to it.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1, 2];
let last = vec.push_mut(3);
assert_eq!(*last, 3);
assert_eq!(vec, [1, 2, 3]);

let last = vec.push_mut(3);
*last += 1;
assert_eq!(vec, [1, 2, 3, 4]);
```

##### §Time complexity

Takes amortized *O*(1) time. If the vector’s length would exceed its capacity after the push, *O*(*capacity*) time is taken to copy the vector’s elements to a larger allocation. This expensive operation is offset by the *capacity* *O*(1) insertions it allows.

Source

§

### impl<T, A> Vec<T, A>where A: Allocator,

Source

#### pub const fn new_in(alloc: A) -> Vec<T, A>

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Constructs a new, empty `Vec<T, A>`.

The vector will not allocate until elements are pushed onto it.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let vec: Vec<i32, System> = Vec::new_in(System);
```

Source

#### pub fn try_with_capacity_in( capacity: usize, alloc: A, ) -> Result<Vec<T, A>, TryReserveError>

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Constructs a new, empty `Vec<T, A>` with at least the specified capacity with the provided allocator.

The vector will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the vector will not allocate.

##### §Errors

Returns an error if the capacity exceeds `isize::MAX` *bytes*, or if the allocator reports allocation failure.

Source

#### pub const unsafe fn from_raw_parts_in( ptr: *mut T, length: usize, capacity: usize, alloc: A, ) -> Vec<T, A>

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Creates a `Vec<T, A>` directly from a pointer, a length, a capacity, and an allocator.

##### §Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- `ptr` must be *currently allocated* via the given allocator `alloc`.
- `T` needs to have the same alignment as what `ptr` was allocated with. (`T` having a less strict alignment is not sufficient, the alignment really needs to be equal to satisfy the `dealloc` requirement that memory must be allocated and deallocated with the same layout.)
- The size of `T` times the `capacity` (i.e. the allocated size in bytes) needs to be the same size as the pointer was allocated with. (Because similar to alignment, `dealloc` must be called with the same layout `size`.)
- `length` needs to be less than or equal to `capacity`.
- The first `length` values must be properly initialized values of type `T`.
- `capacity` needs to *fit* the layout size that the pointer was allocated with.
- The allocated size in bytes must be no larger than `isize::MAX`. See the safety documentation of `pointer::offset`.

These requirements are always upheld by any `ptr` that has been allocated via `Vec<T, A>`. Other allocation sources are allowed if the invariants are upheld.

Violating these may cause problems like corrupting the allocator’s internal data structures. For example it is **not** safe to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`. It’s also not safe to build one from a `Vec<u16>` and its length, because the allocator cares about the alignment, and these two types have different alignments. The buffer was allocated with alignment 2 (for `u16`), but after turning it into a `Vec<u8>` it’ll be deallocated with alignment 1.

The ownership of `ptr` is effectively transferred to the `Vec<T>` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

use std::ptr;

let mut v = Vec::with_capacity_in(3, System);
v.push(1);
v.push(2);
v.push(3);

let (p, len, cap, alloc) = v.into_raw_parts_with_alloc();

unsafe {
    for i in 0..len {
        ptr::write(p.add(i), 4 + i);
    }

    let rebuilt = Vec::from_raw_parts_in(p, len, cap, alloc.clone());
    assert_eq!(rebuilt, [4, 5, 6]);
}
```

Using memory that was allocated elsewhere:

```
#![feature(allocator_api)]

use std::alloc::{AllocError, Allocator, Global, Layout};

fn main() {
    let layout = Layout::array::<u32>(16).expect("overflow cannot happen");

    let vec = unsafe {
        let mem = match Global.allocate(layout) {
            Ok(mem) => mem.cast::<u32>().as_ptr(),
            Err(AllocError) => return,
        };

        mem.write(1_000_000);

        Vec::from_raw_parts_in(mem, 1, 16, Global)
    };

    assert_eq!(vec, &[1_000_000]);
    assert_eq!(vec.capacity(), 16);
}
```

Source

#### pub const unsafe fn from_parts_in( ptr: NonNull<T>, length: usize, capacity: usize, alloc: A, ) -> Vec<T, A>

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Creates a `Vec<T, A>` directly from a `NonNull` pointer, a length, a capacity, and an allocator.

##### §Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- `ptr` must be *currently allocated* via the given allocator `alloc`.
- `T` needs to have the same alignment as what `ptr` was allocated with. (`T` having a less strict alignment is not sufficient, the alignment really needs to be equal to satisfy the `dealloc` requirement that memory must be allocated and deallocated with the same layout.)
- The size of `T` times the `capacity` (i.e. the allocated size in bytes) needs to be the same size as the pointer was allocated with. (Because similar to alignment, `dealloc` must be called with the same layout `size`.)
- `length` needs to be less than or equal to `capacity`.
- The first `length` values must be properly initialized values of type `T`.
- `capacity` needs to *fit* the layout size that the pointer was allocated with.
- The allocated size in bytes must be no larger than `isize::MAX`. See the safety documentation of `pointer::offset`.

These requirements are always upheld by any `ptr` that has been allocated via `Vec<T, A>`. Other allocation sources are allowed if the invariants are upheld.

Violating these may cause problems like corrupting the allocator’s internal data structures. For example it is **not** safe to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`. It’s also not safe to build one from a `Vec<u16>` and its length, because the allocator cares about the alignment, and these two types have different alignments. The buffer was allocated with alignment 2 (for `u16`), but after turning it into a `Vec<u8>` it’ll be deallocated with alignment 1.

The ownership of `ptr` is effectively transferred to the `Vec<T>` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let mut v = Vec::with_capacity_in(3, System);
v.push(1);
v.push(2);
v.push(3);

let (p, len, cap, alloc) = v.into_parts_with_alloc();

unsafe {
    for i in 0..len {
        p.add(i).write(4 + i);
    }

    let rebuilt = Vec::from_parts_in(p, len, cap, alloc.clone());
    assert_eq!(rebuilt, [4, 5, 6]);
}
```

Using memory that was allocated elsewhere:

```
#![feature(allocator_api)]

use std::alloc::{AllocError, Allocator, Global, Layout};

fn main() {
    let layout = Layout::array::<u32>(16).expect("overflow cannot happen");

    let vec = unsafe {
        let mem = match Global.allocate(layout) {
            Ok(mem) => mem.cast::<u32>(),
            Err(AllocError) => return,
        };

        mem.write(1_000_000);

        Vec::from_parts_in(mem, 1, 16, Global)
    };

    assert_eq!(vec, &[1_000_000]);
    assert_eq!(vec.capacity(), 16);
}
```

Source

#### pub const fn into_raw_parts_with_alloc(self) -> (*mut T, usize, usize, A)

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Decomposes a `Vec<T>` into its raw components: `(pointer, length, capacity, allocator)`.

Returns the raw pointer to the underlying data, the length of the vector (in elements), the allocated capacity of the data (in elements), and the allocator. These are the same arguments in the same order as the arguments to `from_raw_parts_in`.

After calling this function, the caller is responsible for the memory previously managed by the `Vec`. The only way to do this is to convert the raw pointer, length, and capacity back into a `Vec` with the `from_raw_parts_in` function, allowing the destructor to perform the cleanup.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let mut v: Vec<i32, System> = Vec::new_in(System);
v.push(-1);
v.push(0);
v.push(1);

let (ptr, len, cap, alloc) = v.into_raw_parts_with_alloc();

let rebuilt = unsafe {
    let ptr = ptr as *mut u32;

    Vec::from_raw_parts_in(ptr, len, cap, alloc)
};
assert_eq!(rebuilt, [4294967295, 0, 1]);
```

Source

#### pub const fn into_parts_with_alloc(self) -> (NonNull<T>, usize, usize, A)

🔬

This is a nightly-only experimental API. (

allocator_api

#32838

)

Decomposes a `Vec<T>` into its raw components: `(NonNull pointer, length, capacity, allocator)`.

Returns the `NonNull` pointer to the underlying data, the length of the vector (in elements), the allocated capacity of the data (in elements), and the allocator. These are the same arguments in the same order as the arguments to `from_parts_in`.

After calling this function, the caller is responsible for the memory previously managed by the `Vec`. The only way to do this is to convert the `NonNull` pointer, length, and capacity back into a `Vec` with the `from_parts_in` function, allowing the destructor to perform the cleanup.

##### §Examples

```
#![feature(allocator_api)]

use std::alloc::System;

let mut v: Vec<i32, System> = Vec::new_in(System);
v.push(-1);
v.push(0);
v.push(1);

let (ptr, len, cap, alloc) = v.into_parts_with_alloc();

let rebuilt = unsafe {
    let ptr = ptr.cast::<u32>();

    Vec::from_parts_in(ptr, len, cap, alloc)
};
assert_eq!(rebuilt, [4294967295, 0, 1]);
```

1.0.0 (const: 1.87.0)

·

Source

#### pub const fn capacity(&self) -> usize

Returns the total number of elements the vector can hold without reallocating.

##### §Examples

```
let mut vec: Vec<i32> = Vec::with_capacity(10);
vec.push(42);
assert!(vec.capacity() >= 10);
```

A vector with zero-sized elements will always have a capacity of usize::MAX:

```
#[derive(Clone)]
struct ZeroSized;

fn main() {
    assert_eq!(std::mem::size_of::<ZeroSized>(), 0);
    let v = vec![ZeroSized; 0];
    assert_eq!(v.capacity(), usize::MAX);
}
```

1.0.0

·

Source

#### pub fn reserve(&mut self, additional: usize)

Reserves capacity for at least `additional` more elements to be inserted in the given `Vec<T>`. The collection may reserve more space to speculatively avoid frequent reallocations. After calling `reserve`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if capacity is already sufficient.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1];
vec.reserve(10);
assert!(vec.capacity() >= 11);
```

1.0.0

·

Source

#### pub fn reserve_exact(&mut self, additional: usize)

Reserves the minimum capacity for at least `additional` more elements to be inserted in the given `Vec<T>`. Unlike `reserve`, this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `reserve_exact`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer `reserve` if future insertions are expected.

##### §Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### §Examples

```
let mut vec = vec![1];
vec.reserve_exact(10);
assert!(vec.capacity() >= 11);
```

1.57.0

·

Source

#### pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError>

Tries to reserve capacity for at least `additional` more elements to be inserted in the given `Vec<T>`. The collection may reserve more space to speculatively avoid frequent reallocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient. This method preserves the contents even if an error occurs.

##### §Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### §Examples

```
use std::collections::TryReserveError;

fn process_data(data: &[u32]) -> Result<Vec<u32>, TryReserveError> {
    let mut output = Vec::new();

    output.try_reserve(data.len())?;

    output.extend(data.iter().map(|&val| {
        val * 2 + 5 }));

    Ok(output)
}
```

1.57.0

·

Source

#### pub fn try_reserve_exact( &mut self, additional: usize, ) -> Result<(), TryReserveError>

Tries to reserve the minimum capacity for at least `additional` elements to be inserted in the given `Vec<T>`. Unlike `try_reserve`, this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `try_reserve_exact`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer `try_reserve` if future insertions are expected.

##### §Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### §Examples

```
use std::collections::TryReserveError;

fn process_data(data: &[u32]) -> Result<Vec<u32>, TryReserveError> {
    let mut output = Vec::new();

    output.try_reserve_exact(data.len())?;

    output.extend(data.iter().map(|&val| {
        val * 2 + 5 }));

    Ok(output)
}
```

1.0.0

·

Source

#### pub fn shrink_to_fit(&mut self)

Shrinks the capacity of the vector as much as possible.

The behavior of this method depends on the allocator, which may either shrink the vector in-place or reallocate. The resulting vector might still have some excess capacity, just as is the case for `with_capacity`. See `Allocator::shrink` for more details.

##### §Examples

```
let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);
assert!(vec.capacity() >= 10);
vec.shrink_to_fit();
assert!(vec.capacity() >= 3);
```

1.56.0

·

Source

#### pub fn shrink_to(&mut self, min_capacity: usize)

Shrinks the capacity of the vector with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

##### §Examples

```
let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);
assert!(vec.capacity() >= 10);
vec.shrink_to(4);
assert!(vec.capacity() >= 4);
vec.shrink_to(0);
assert!(vec.capacity() >= 3);
```

Source

#### pub fn try_shrink_to_fit(&mut self) -> Result<(), TryReserveError>

🔬

This is a nightly-only experimental API. (

vec_fallible_shrink

#152350

)

Tries to shrink the capacity of the vector as much as possible

The behavior of this method depends on the allocator, which may either shrink the vector in-place or reallocate. The resulting vector might still have some excess capacity, just as is the case for `with_capacity`. See `Allocator::shrink` for more details.

##### §Errors

This function returns an error if the allocator fails to shrink the allocation, the vector thereafter is still safe to use, the capacity remains unchanged however. See `Allocator::shrink`.

##### §Examples

```
#![feature(vec_fallible_shrink)]

let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);
assert!(vec.capacity() >= 10);
vec.try_shrink_to_fit().expect("why is the test harness failing to shrink to 12 bytes");
assert!(vec.capacity() >= 3);
```

Source

#### pub fn try_shrink_to( &mut self, min_capacity: usize, ) -> Result<(), TryReserveError>

🔬

This is a nightly-only experimental API. (

vec_fallible_shrink

#152350

)

Shrinks the capacity of the vector with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

##### §Errors

This function returns an error if the allocator fails to shrink the allocation, the vector thereafter is still safe to use, the capacity remains unchanged however. See `Allocator::shrink`.

##### §Examples

```
#![feature(vec_fallible_shrink)]

let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);
assert!(vec.capacity() >= 10);
vec.try_shrink_to(4).expect("why is the test harness failing to shrink to 12 bytes");
assert!(vec.capacity() >= 4);
vec.try_shrink_to(0).expect("this is a no-op and thus the allocator isn't involved.");
assert!(vec.capacity() >= 3);
```

1.0.0

·

Source

#### pub fn into_boxed_slice(self) -> Box<[T], A>

Converts the vector into `Box<[T]>`.

Before doing the conversion, this method discards excess capacity like `shrink_to_fit`.

##### §Examples

```
let v = vec![1, 2, 3];

let slice = v.into_boxed_slice();
```

Any excess capacity is removed:

```
let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);

assert!(vec.capacity() >= 10);
let slice = vec.into_boxed_slice();
assert_eq!(slice.into_vec().capacity(), 3);
```

1.0.0

·

Source

#### pub fn truncate(&mut self, len: usize)

Shortens the vector, keeping the first `len` elements and dropping the rest.

If `len` is greater or equal to the vector’s current length, this has no effect.

The `drain` method can emulate `truncate`, but causes the excess elements to be returned instead of dropped.

Note that this method has no effect on the allocated capacity of the vector.

##### §Examples

Truncating a five element vector to two elements:

```
let mut vec = vec![1, 2, 3, 4, 5];
vec.truncate(2);
assert_eq!(vec, [1, 2]);
```

No truncation occurs when `len` is greater than the vector’s current length:

```
let mut vec = vec![1, 2, 3];
vec.truncate(8);
assert_eq!(vec, [1, 2, 3]);
```

Truncating when `len == 0` is equivalent to calling the `clear` method.

```
let mut vec = vec![1, 2, 3];
vec.truncate(0);
assert_eq!(vec, []);
```

1.7.0 (const: 1.87.0)

·

Source

#### pub const fn as_slice(&self) -> &[T]

Extracts a slice containing the entire vector.

Equivalent to `&s[..]`.

##### §Examples

```
use std::io::{self, Write};
let buffer = vec![1, 2, 3, 5, 8];
io::sink().write(buffer.as_slice()).unwrap();
```

1.7.0 (const: 1.87.0)
