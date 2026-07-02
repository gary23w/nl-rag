---
title: "Documentation (part 2/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 2/10
---

## Vectors

A vector is a group of booleans, Integers, Floats, or Pointers which are operated on in parallel, using SIMD instructions if possible. Vector types are created with the builtin function @Vector.

Vectors generally support the same builtin operators as their underlying base types. The only exception to this is the keywords `and` and `or` on vectors of bools, since these operators affect control flow, which is not allowed for vectors. All other operations are performed element-wise, and return a vector of the same length as the input vectors. This includes:

- Arithmetic (`+`, `-`, `/`, `*`, `@divFloor`, `@sqrt`, `@ceil`, `@log`, etc.)
- Bitwise operators (`>>`, `<<`, `&`, `|`, `~`, etc.)
- Comparison operators (`<`, `>`, `==`, etc.)
- Boolean not (`!`)

It is prohibited to use a math operator on a mixture of scalars (individual numbers) and vectors. Zig provides the @splat builtin to easily convert from scalars to vectors, and it supports @reduce and array indexing syntax to convert from vectors to scalars. Vectors also support assignment to and from fixed-length arrays with comptime-known length.

For rearranging elements within and between vectors, Zig provides the @shuffle and @select functions.

Operations on vectors shorter than the target machine's native SIMD size will typically compile to single SIMD instructions, while vectors longer than the target machine's native SIMD size will compile to multiple SIMD instructions. If a given operation doesn't have SIMD support on the target architecture, the compiler will default to operating on each vector element one at a time. Zig supports any comptime-known vector length up to 2^32-1, although small powers of two (2-64) are most typical. Note that excessively long vector lengths (e.g. 2^20) may result in compiler crashes on current versions of Zig.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "Basic vector usage" {
    
    const a = @Vector(4, i32){ 1, 2, 3, 4 };
    const b = @Vector(4, i32){ 5, 6, 7, 8 };

    
    const c = a + b;

    
    try expectEqual(6, c[0]);
    try expectEqual(8, c[1]);
    try expectEqual(10, c[2]);
    try expectEqual(12, c[3]);
}

test "Conversion between vectors, arrays, and slices" {
    
    const arr1: [4]f32 = [_]f32{ 1.1, 3.2, 4.5, 5.6 };
    const vec: @Vector(4, f32) = arr1;
    const arr2: [4]f32 = vec;
    try expectEqual(arr1, arr2);

    
    const vec2: @Vector(2, f32) = arr1[1..3].*;

    const slice: []const f32 = &arr1;
    var offset: u32 = 1; 
    _ = &offset; 
    
    
    
    const vec3: @Vector(2, f32) = slice[offset..][0..2].*;
    try expectEqual(slice[offset], vec2[0]);
    try expectEqual(slice[offset + 1], vec2[1]);
    try expectEqual(vec2, vec3);
}
```

```
$ zig test test_vector.zig
1/2 test_vector.test.Basic vector usage...OK
2/2 test_vector.test.Conversion between vectors, arrays, and slices...OK
All 2 tests passed.
```

TODO talk about C ABI interop TODO consider suggesting std.MultiArrayList

See also:

- @splat
- @shuffle
- @select
- @reduce
- Slicing by Length

### Relationship with Arrays

Vectors and Arrays each have a well-defined **bit layout** and therefore support @bitCast between each other. Type Coercion implicitly peforms `@bitCast`.

Arrays have well-defined byte layout, but vectors do not, making @ptrCast between them Illegal Behavior.

### Destructuring Vectors

Vectors can be destructured:

```
const print = @import("std").debug.print;

pub fn unpack(x: @Vector(4, f32), y: @Vector(4, f32)) @Vector(4, f32) {
    const a, const c, _, _ = x;
    const b, const d, _, _ = y;
    return .{ a, b, c, d };
}

pub fn main() void {
    const x: @Vector(4, f32) = .{ 1.0, 2.0, 3.0, 4.0 };
    const y: @Vector(4, f32) = .{ 5.0, 6.0, 7.0, 8.0 };
    print("{}", .{unpack(x, y)});
}
```

```
$ zig build-exe destructuring_vectors.zig
$ ./destructuring_vectors
{ 1, 5, 2, 6 }
```

See also:

- Destructuring
- Destructuring Tuples
- Destructuring Arrays


## Pointers

Zig has two kinds of pointers: single-item and many-item.

- `*T` - single-item pointer to exactly one item.
  - Supports deref syntax: `ptr.*`
  - Supports slice syntax: `ptr[0..1]`
  - Supports pointer subtraction: `ptr - ptr`
- `[*]T` - many-item pointer to unknown number of items. `T` must have a known size, which means that it cannot be `anyopaque` or any other opaque type.
  - Supports index syntax: `ptr[i]`
  - Supports slice syntax: `ptr[start..end]` and `ptr[start..]`
  - Supports pointer-integer arithmetic: `ptr + int`, `ptr - int`
  - Supports pointer subtraction: `ptr - ptr`

These types are closely related to Arrays and Slices:

- `*[N]T` - pointer to N items, same as single-item pointer to an array.
  - Supports index syntax: `array_ptr[i]`
  - Supports slice syntax: `array_ptr[start..end]`
  - Supports len property: `array_ptr.len`
  - Supports pointer subtraction: `array_ptr - array_ptr`

- `[]T` - is a slice (a fat pointer, which contains a pointer of type `[*]T` and a length).
  - Supports index syntax: `slice[i]`
  - Supports slice syntax: `slice[start..end]`
  - Supports len property: `slice.len`

Use `&x` to obtain a single-item pointer:

```
const expectEqual = @import("std").testing.expectEqual;

test "address of syntax" {
    
    const x: i32 = 1234;
    const x_ptr = &x;

    
    try expectEqual(1234, x_ptr.*);

    
    try expectEqual(*const i32, @TypeOf(x_ptr));

    
    var y: i32 = 5678;
    const y_ptr = &y;
    try expectEqual(*i32, @TypeOf(y_ptr));
    y_ptr.* += 1;
    try expectEqual(5679, y_ptr.*);
}

test "pointer array access" {
    
    
    
    var array = [_]u8{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    const ptr = &array[2];
    try expectEqual(*u8, @TypeOf(ptr));

    try expectEqual(3, array[2]);
    ptr.* += 1;
    try expectEqual(4, array[2]);
}

test "slice syntax" {
    
    var x: i32 = 1234;
    const x_ptr = &x;

    
    const x_array_ptr = x_ptr[0..1];
    try expectEqual(*[1]i32, @TypeOf(x_array_ptr));

    
    const x_many_ptr: [*]i32 = x_array_ptr;
    try expectEqual(1234, x_many_ptr[0]);
}
```

```
$ zig test test_single_item_pointer.zig
1/3 test_single_item_pointer.test.address of syntax...OK
2/3 test_single_item_pointer.test.pointer array access...OK
3/3 test_single_item_pointer.test.slice syntax...OK
All 3 tests passed.
```

Zig supports pointer arithmetic. It's better to assign the pointer to `[*]T` and increment that variable. For example, directly incrementing the pointer from a slice will corrupt it.

```
const expectEqual = @import("std").testing.expectEqual;

test "pointer arithmetic with many-item pointer" {
    const array = [_]i32{ 1, 2, 3, 4 };
    var ptr: [*]const i32 = &array;

    try expectEqual(1, ptr[0]);
    ptr += 1;
    try expectEqual(2, ptr[0]);

    
    
    try expectEqual(ptr[1..], ptr + 1);

    
    try expectEqual(1, &ptr[1] - &ptr[0]);
}

test "pointer arithmetic with slices" {
    var array = [_]i32{ 1, 2, 3, 4 };
    var length: usize = 0; 
    _ = &length; 
    var slice = array[length..array.len];

    try expectEqual(1, slice[0]);
    try expectEqual(4, slice.len);

    slice.ptr += 1;
    

    try expectEqual(2, slice[0]);
    try expectEqual(4, slice.len);
}
```

```
$ zig test test_pointer_arithmetic.zig
1/2 test_pointer_arithmetic.test.pointer arithmetic with many-item pointer...OK
2/2 test_pointer_arithmetic.test.pointer arithmetic with slices...OK
All 2 tests passed.
```

In Zig, we generally prefer Slices rather than Sentinel-Terminated Pointers. You can turn an array or pointer into a slice using slice syntax.

Slices have bounds checking and are therefore protected against this kind of Illegal Behavior. This is one reason we prefer slices to pointers.

```
const expectEqual = @import("std").testing.expectEqual;

test "pointer slicing" {
    var array = [_]u8{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    var start: usize = 2; 
    _ = &start; 
    const slice = array[start..4];
    try expectEqual(2, slice.len);

    try expectEqual(4, array[3]);
    slice[1] += 1;
    try expectEqual(5, array[3]);
}
```

```
$ zig test test_slice_bounds.zig
1/1 test_slice_bounds.test.pointer slicing...OK
All 1 tests passed.
```

Pointers work at compile-time too, as long as the code does not depend on an undefined memory layout:

```
const expectEqual = @import("std").testing.expectEqual;

test "comptime pointers" {
    comptime {
        var x: i32 = 1;
        const ptr = &x;
        ptr.* += 1;
        x += 1;
        try expectEqual(3, ptr.*);
    }
}
```

```
$ zig test test_comptime_pointers.zig
1/1 test_comptime_pointers.test.comptime pointers...OK
All 1 tests passed.
```

To convert an integer address into a pointer, use `@ptrFromInt`. To convert a pointer to an integer, use `@intFromPtr`:

```
const expectEqual = @import("std").testing.expectEqual;

test "@intFromPtr and @ptrFromInt" {
    const ptr: *i32 = @ptrFromInt(0xdeadbee0);
    const addr = @intFromPtr(ptr);
    try expectEqual(usize, @TypeOf(addr));
    try expectEqual(0xdeadbee0, addr);
}
```

```
$ zig test test_integer_pointer_conversion.zig
1/1 test_integer_pointer_conversion.test.@intFromPtr and @ptrFromInt...OK
All 1 tests passed.
```

Zig is able to preserve memory addresses in comptime code, as long as the pointer is never dereferenced:

```
const expectEqual = @import("std").testing.expectEqual;

test "comptime @ptrFromInt" {
    comptime {
        
        
        const ptr: *i32 = @ptrFromInt(0xdeadbee0);
        const addr = @intFromPtr(ptr);
        try expectEqual(usize, @TypeOf(addr));
        try expectEqual(0xdeadbee0, addr);
    }
}
```

```
$ zig test test_comptime_pointer_conversion.zig
1/1 test_comptime_pointer_conversion.test.comptime @ptrFromInt...OK
All 1 tests passed.
```

@ptrCast converts a pointer's element type to another. This creates a new pointer that can cause undetectable Illegal Behavior depending on the loads and stores that pass through it. Generally, other kinds of type conversions are preferable to `@ptrCast` if possible.

```
const std = @import("std");
const native_endian = @import("builtin").target.cpu.arch.endian();
const expectEqual = std.testing.expectEqual;

test "pointer casting" {
    const bytes: [4]u8 align(@alignOf(u32)) = .{ 0x10, 0x20, 0x30, 0x40 };
    const u32_ptr: *const u32 = @ptrCast(&bytes);

    
    
    switch (native_endian) {
        .little => try expectEqual(0x40302010, u32_ptr.*),
        .big => try expectEqual(0x10203040, u32_ptr.*),
    }

    
    
    
    try expectEqual(0x40302010, @as(u32, @bitCast(bytes)));
}

test "pointer child type" {
    
    try expectEqual(u32, @typeInfo(*u32).pointer.child);
}
```

```
$ zig test test_pointer_casting.zig
1/2 test_pointer_casting.test.pointer casting...OK
2/2 test_pointer_casting.test.pointer child type...OK
All 2 tests passed.
```

See also:

- Optional Pointers
- @ptrFromInt
- @intFromPtr
- C Pointers

### volatile

Loads and stores are assumed to not have side effects. If a given load or store should have side effects, such as Memory Mapped Input/Output (MMIO), use `volatile`. In the following code, loads and stores with `mmio_ptr` are guaranteed to all happen and in the same order as in source code:

```
const expectEqual = @import("std").testing.expectEqual;

test "volatile" {
    const mmio_ptr: *volatile u8 = @ptrFromInt(0x12345678);
    try expectEqual(*volatile u8, @TypeOf(mmio_ptr));
}
```

```
$ zig test test_volatile.zig
1/1 test_volatile.test.volatile...OK
All 1 tests passed.
```

Note that `volatile` is unrelated to concurrency and Atomics. If you see code that is using `volatile` for something other than Memory Mapped Input/Output, it is probably a bug.

### Alignment

Each type has an **alignment** - a number of bytes such that, when a value of the type is loaded from or stored to memory, the memory address must be evenly divisible by this number. You can use @alignOf to find out this value for any type.

Alignment depends on the CPU architecture, but is always a power of two, and less than `1 << 29`.

Pointer types may explicitly specify an alignment in bytes. If it is not specified, the alignment is assumed to be equal to the alignment of the underlying type.

```
const std = @import("std");
const builtin = @import("builtin");
const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;

test "variable alignment" {
    var x: i32 = 1234;

    try expectEqual(*i32, @TypeOf(&x));

    try expect(@intFromPtr(&x) % @alignOf(i32) == 0);

    
    
    const ptr: *align(@alignOf(i32)) i32 = &x;

    try expectEqual(1234, ptr.*);
}
```

```
$ zig test test_variable_alignment.zig
1/1 test_variable_alignment.test.variable alignment...OK
All 1 tests passed.
```

In the same way that a `*i32` can be coerced to a `*const i32`, a pointer with a larger alignment can be implicitly cast to a pointer with a smaller alignment, but not vice versa.

You can specify alignment on variables and functions. If you do this, then pointers to them get the specified alignment:

```
const expectEqual = @import("std").testing.expectEqual;

var foo: u8 align(4) = 100;

test "global variable alignment" {
    try expectEqual(4, @typeInfo(@TypeOf(&foo)).pointer.attrs.@"align");
    try expectEqual(*align(4) u8, @TypeOf(&foo));
    const as_pointer_to_array: *align(4) [1]u8 = &foo;
    const as_slice: []align(4) u8 = as_pointer_to_array;
    const as_unaligned_slice: []u8 = as_slice;
    try expectEqual(100, as_unaligned_slice[0]);
}

fn derp() align(@sizeOf(usize) * 2) i32 {
    return 1234;
}
fn noop1() align(1) void {}
fn noop4() align(4) void {}

test "function alignment" {
    try expectEqual(1234, derp());
    try expectEqual(fn () i32, @TypeOf(derp));
    try expectEqual(*align(@sizeOf(usize) * 2) const fn () i32, @TypeOf(&derp));

    noop1();
    try expectEqual(fn () void, @TypeOf(noop1));
    try expectEqual(*align(1) const fn () void, @TypeOf(&noop1));

    noop4();
    try expectEqual(fn () void, @TypeOf(noop4));
    try expectEqual(*align(4) const fn () void, @TypeOf(&noop4));
}
```

```
$ zig test test_variable_func_alignment.zig
1/2 test_variable_func_alignment.test.global variable alignment...OK
2/2 test_variable_func_alignment.test.function alignment...OK
All 2 tests passed.
```

If you have a pointer or a slice that has a small alignment, but you know that it actually has a bigger alignment, use @alignCast to change the pointer into a more aligned pointer. This is a no-op at runtime, but inserts a safety check:

```
const std = @import("std");

test "pointer alignment safety" {
    var array align(4) = [_]u32{ 0x11111111, 0x11111111 };
    const bytes = std.mem.sliceAsBytes(array[0..]);
    try std.testing.expectEqual(0x11111111, foo(bytes));
}
fn foo(bytes: []u8) u32 {
    const slice4 = bytes[1..5];
    const int_slice = std.mem.bytesAsSlice(u32, @as([]align(4) u8, @alignCast(slice4)));
    return int_slice[0];
}
```

```
$ zig test test_incorrect_pointer_alignment.zig
1/1 test_incorrect_pointer_alignment.test.pointer alignment safety...thread 2238160 panic: incorrect alignment
/home/ci/work/zig-bootstrap/zig/doc/langref/test_incorrect_pointer_alignment.zig:10:68: 0x124d356 in foo (test_incorrect_pointer_alignment.zig)
    const int_slice = std.mem.bytesAsSlice(u32, @as([]align(4) u8, @alignCast(slice4)));
                                                                   ^
/home/ci/work/zig-bootstrap/zig/doc/langref/test_incorrect_pointer_alignment.zig:6:48: 0x124d18e in test.pointer alignment safety (test_incorrect_pointer_alignment.zig)
    try std.testing.expectEqual(0x11111111, foo(bytes));
                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:296:25: 0x1200de1 in mainTerminal (test_runner.zig)
        if (test_fn.func()) |_| {
                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:73:28: 0x12005b2 in main (test_runner.zig)
        return mainTerminal(init);
                           ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:752:88: 0x11fcd5f in callMain (std.zig)
    if (fn_info.param_types[0].? == std.process.Init.Minimal) return wrapMain(root.main(.{
                                                                                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11fc731 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
error: the following test command terminated with signal ABRT:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/38f76306ec9f2d0f4a4ea948685c1b76/test --seed=0xede79333
```

### allowzero

This pointer attribute allows a pointer to have address zero. This is only ever needed on the freestanding OS target, where the address zero is mappable. If you want to represent null pointers, use Optional Pointers instead. Optional Pointers with `allowzero` are not the same size as pointers. In this code example, if the pointer did not have the `allowzero` attribute, this would be a Pointer Cast Invalid Null panic:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "allowzero" {
    var zero: usize = 0; 
    _ = &zero; 
    const ptr: *allowzero i32 = @ptrFromInt(zero);
    try expectEqual(0, @intFromPtr(ptr));
}
```

```
$ zig test test_allowzero.zig
1/1 test_allowzero.test.allowzero...OK
All 1 tests passed.
```

### Sentinel-Terminated Pointers

The syntax `[*:x]T` describes a pointer that has a length determined by a sentinel value. This provides protection against buffer overflow and overreads.

```
const std = @import("std");

pub extern "c" fn printf(format: [*:0]const u8, ...) c_int;

pub fn main() anyerror!void {
    _ = printf("Hello, world!\n"); 

    const msg = "Hello, world!\n";
    const non_null_terminated_msg: [msg.len]u8 = msg.*;
    _ = printf(&non_null_terminated_msg);
}
```

```
$ zig build-exe sentinel-terminated_pointer.zig -lc
/home/ci/work/zig-bootstrap/zig/doc/langref/sentinel-terminated_pointer.zig:11:16: error: expected type '[*:0]const u8', found '*const [14]u8'
    _ = printf(&non_null_terminated_msg);
               ^~~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/sentinel-terminated_pointer.zig:11:16: note: destination pointer requires '0' sentinel
/home/ci/work/zig-bootstrap/zig/doc/langref/sentinel-terminated_pointer.zig:4:34: note: parameter type declared here
pub extern "c" fn printf(format: [*:0]const u8, ...) c_int;
                                 ^~~~~~~~~~~~~
referenced by:
    callMain [inlined]: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64
    callMainWithArgs [inlined]: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:692:20
    main: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:717:28
    1 reference(s) hidden; use '-freference-trace=4' to see all references
```

See also:

- Sentinel-Terminated Slices
- Sentinel-Terminated Arrays


## Slices

A slice is a pointer and a length. The difference between an array and a slice is that the array's length is part of the type and known at compile-time, whereas the slice's length is known at runtime. Both can be accessed with the `len` field.

```
const expectEqual = @import("std").testing.expectEqual;
const expectEqualSlices = @import("std").testing.expectEqualSlices;

test "basic slices" {
    var array = [_]i32{ 1, 2, 3, 4 };
    var known_at_runtime_zero: usize = 0;
    _ = &known_at_runtime_zero;
    const slice = array[known_at_runtime_zero..array.len];

    
    const alt_slice: []const i32 = &.{ 1, 2, 3, 4 };

    try expectEqualSlices(i32, slice, alt_slice);

    try expectEqual([]i32, @TypeOf(slice));
    try expectEqual(&array[0], &slice[0]);
    try expectEqual(array.len, slice.len);

    
    
    const array_ptr = array[0..array.len];
    try expectEqual(*[array.len]i32, @TypeOf(array_ptr));

    
    try expectEqual(*i32, @TypeOf(&slice[0]));
    
    try expectEqual([*]i32, @TypeOf(slice.ptr));
    try expectEqual(@intFromPtr(slice.ptr), @intFromPtr(&slice[0]));

    
    
    slice[10] += 1;

    
    

    
    const empty1 = &[0]u8{};
    
    const empty2: []u8 = &.{};
    try expectEqual(0, empty1.len);
    try expectEqual(0, empty2.len);

    
    
}
```

```
$ zig test test_basic_slices.zig
1/1 test_basic_slices.test.basic slices...thread 2237023 panic: index out of bounds: index 10, len 4
/home/ci/work/zig-bootstrap/zig/doc/langref/test_basic_slices.zig:32:10: 0x124f238 in test.basic slices (test_basic_slices.zig)
    slice[10] += 1;
         ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:296:25: 0x1200de1 in mainTerminal (test_runner.zig)
        if (test_fn.func()) |_| {
                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:73:28: 0x12005b2 in main (test_runner.zig)
        return mainTerminal(init);
                           ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:752:88: 0x11fcd5f in callMain (std.zig)
    if (fn_info.param_types[0].? == std.process.Init.Minimal) return wrapMain(root.main(.{
                                                                                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11fc731 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
error: the following test command terminated with signal ABRT:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/3cc89e8acf8c170d49fd643dba8844fb/test --seed=0xe877772d
```

This is one reason we prefer slices to pointers.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;
const expectEqualStrings = std.testing.expectEqualStrings;
const fmt = std.fmt;

test "using slices for strings" {
    
    
    
    
    const hello: []const u8 = "hello";
    const world: []const u8 = "世界";

    var all_together: [100]u8 = undefined;
    
    
    var start: usize = 0;
    _ = &start;
    const all_together_slice = all_together[start..];
    
    const hello_world = try fmt.bufPrint(all_together_slice, "{s} {s}", .{ hello, world });

    
    
    
    try expectEqualStrings("hello 世界", hello_world);
}

test "slice pointer" {
    var array: [10]u8 = undefined;
    const ptr = &array;
    try expectEqual(*[10]u8, @TypeOf(ptr));

    
    var start: usize = 0;
    var end: usize = 5;
    _ = .{ &start, &end };
    const slice = ptr[start..end];
    
    try expectEqual([]u8, @TypeOf(slice));
    slice[2] = 3;
    try expectEqual(3, array[2]);

    
    
    const ptr2 = slice[2..3];
    try expectEqual(1, ptr2.len);
    try expectEqual(3, ptr2[0]);
    try expectEqual(*[1]u8, @TypeOf(ptr2));
}
```

```
$ zig test test_slices.zig
1/2 test_slices.test.using slices for strings...OK
2/2 test_slices.test.slice pointer...OK
All 2 tests passed.
```

See also:

- Pointers
- for
- Arrays

### Slicing by Length

Even though Zig only has syntax for slicing based on start and end indices, by slicing twice, one can express a **slice by length** operation.

The pattern `[a .. a + b]` is always better expressed `[a..][0..b]` because:

- Slices are represented in memory as a pointer and length. Despite syntactically appearing as twice the work, it is actually one less subtraction in machine code.
- If `a` is known at runtime and `b` is known at comptime, the former results in a slice but the latter results in a single-item pointer to an array, a generally more safe type because the length is compile-time known.

```
const expectEqual = @import("std").testing.expectEqual;

test "example" {
    var array = [_]i32{ 1, 2, 3, 4 };
    var runtime_start: usize = 1;
    _ = &runtime_start;
    const length = 2;
    const array_ptr_len = array[runtime_start..][0..length];
    try expectEqual(*[length]i32, @TypeOf(array_ptr_len));
}
```

```
$ zig test slicing_by_length.zig
1/1 slicing_by_length.test.example...OK
All 1 tests passed.
```

### Sentinel-Terminated Slices

The syntax `[:x]T` is a slice which has a runtime-known length and also guarantees a sentinel value at the element indexed by the length. The type does not guarantee that there are no sentinel elements before that. Sentinel-terminated slices allow element access to the `len` index.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "0-terminated slice" {
    const slice: [:0]const u8 = "hello";

    try expectEqual(5, slice.len);
    try expectEqual(0, slice[5]);
}
```

```
$ zig test test_null_terminated_slice.zig
1/1 test_null_terminated_slice.test.0-terminated slice...OK
All 1 tests passed.
```

Sentinel-terminated slices can also be created using a variation of the slice syntax `data[start..end :x]`, where `data` is a many-item pointer, array or slice and `x` is the sentinel value.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "0-terminated slicing" {
    var array = [_]u8{ 3, 2, 1, 0, 3, 2, 1, 0 };
    var runtime_length: usize = 3;
    _ = &runtime_length;
    const slice = array[0..runtime_length :0];

    try expectEqual([:0]u8, @TypeOf(slice));
    try expectEqual(3, slice.len);
}
```

```
$ zig test test_null_terminated_slicing.zig
1/1 test_null_terminated_slicing.test.0-terminated slicing...OK
All 1 tests passed.
```

Sentinel-terminated slicing asserts that the element in the sentinel position of the backing data is actually the sentinel value. If this is not the case, safety-checked Illegal Behavior results.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "sentinel mismatch" {
    var array = [_]u8{ 3, 2, 1, 0 };

    
    
    
    
    var runtime_length: usize = 2;
    _ = &runtime_length;
    const slice = array[0..runtime_length :0];

    _ = slice;
}
```

```
$ zig test test_sentinel_mismatch.zig
1/1 test_sentinel_mismatch.test.sentinel mismatch...thread 2236770 panic: sentinel mismatch: expected 0, found 1
/home/ci/work/zig-bootstrap/zig/doc/langref/test_sentinel_mismatch.zig:13:24: 0x124d17f in test.sentinel mismatch (test_sentinel_mismatch.zig)
    const slice = array[0..runtime_length :0];
                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:296:25: 0x1200de1 in mainTerminal (test_runner.zig)
        if (test_fn.func()) |_| {
                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:73:28: 0x12005b2 in main (test_runner.zig)
        return mainTerminal(init);
                           ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:752:88: 0x11fcd5f in callMain (std.zig)
    if (fn_info.param_types[0].? == std.process.Init.Minimal) return wrapMain(root.main(.{
                                                                                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11fc731 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
error: the following test command terminated with signal ABRT:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/13e40ead91b124c6f5c96decd09292d3/test --seed=0x2035e6ff
```

See also:

- Sentinel-Terminated Pointers
- Sentinel-Terminated Arrays


## struct

```
const Point = struct {
    x: f32,
    y: f32,
};

const p: Point = .{
    .x = 0.12,
    .y = 0.34,
};

const Vec3 = struct {
    x: f32,
    y: f32,
    z: f32,

    pub fn init(x: f32, y: f32, z: f32) Vec3 {
        return Vec3{
            .x = x,
            .y = y,
            .z = z,
        };
    }

    pub fn dot(self: Vec3, other: Vec3) f32 {
        return self.x * other.x + self.y * other.y + self.z * other.z;
    }
};

test "dot product" {
    const v1 = Vec3.init(1.0, 0.0, 0.0);
    const v2 = Vec3.init(0.0, 1.0, 0.0);
    try expectEqual(0.0, v1.dot(v2));

    
    
    
    try expectEqual(0.0, Vec3.dot(v1, v2));
}

const Empty = struct {
    pub const PI = 3.14;
};
test "struct namespaced variable" {
    try expectEqual(3.14, Empty.PI);
    try expectEqual(0, @sizeOf(Empty));

    
    const does_nothing: Empty = .{};

    _ = does_nothing;
}

fn setYBasedOnX(x: *f32, y: f32) void {
    const point: *Point = @fieldParentPtr("x", x);
    point.y = y;
}
test "field parent pointer" {
    var point = Point{
        .x = 0.1234,
        .y = 0.5678,
    };
    setYBasedOnX(&point.x, 0.9);
    try expectEqual(0.9, point.y);
}

fn LinkedList(comptime T: type) type {
    return struct {
        pub const Node = struct {
            prev: ?*Node,
            next: ?*Node,
            data: T,
        };

        first: ?*Node,
        last: ?*Node,
        len: usize,
    };
}

test "linked list" {
    
    try expectEqual(LinkedList(i32), LinkedList(i32));

    const list = LinkedList(i32){
        .first = null,
        .last = null,
        .len = 0,
    };
    try expectEqual(0, list.len);

    
    
    const ListOfInts = LinkedList(i32);
    try expectEqual(LinkedList(i32), ListOfInts);

    var node = ListOfInts.Node{
        .prev = null,
        .next = null,
        .data = 1234,
    };
    const list2 = LinkedList(i32){
        .first = &node,
        .last = &node,
        .len = 1,
    };

    
    
    
    try expectEqual(1234, list2.first.?.data);
    
}

const expectEqual = @import("std").testing.expectEqual;
```

```
$ zig test test_structs.zig
1/4 test_structs.test.dot product...OK
2/4 test_structs.test.struct namespaced variable...OK
3/4 test_structs.test.field parent pointer...OK
4/4 test_structs.test.linked list...OK
All 4 tests passed.
```

### Default Field Values

Each struct field may have an expression indicating the default field value. Such expressions are executed at comptime, and allow the field to be omitted in a struct literal expression:

```
const Foo = struct {
    a: i32 = 1234,
    b: i32,
};

test "default struct initialization fields" {
    const x: Foo = .{
        .b = 5,
    };
    if (x.a + x.b != 1239) {
        comptime unreachable;
    }
}
```

```
$ zig test struct_default_field_values.zig
1/1 struct_default_field_values.test.default struct initialization fields...OK
All 1 tests passed.
```

#### Faulty Default Field Values

Default field values are only appropriate when the data invariants of a struct cannot be violated by omitting that field from an initialization.

For example, here is an inappropriate use of default struct field initialization:

```
const Threshold = struct {
    minimum: f32 = 0.25,
    maximum: f32 = 0.75,

    const Category = enum { low, medium, high };

    fn categorize(t: Threshold, value: f32) Category {
        assert(t.maximum >= t.minimum);
        if (value < t.minimum) return .low;
        if (value > t.maximum) return .high;
        return .medium;
    }
};

pub fn main() !void {
    var threshold: Threshold = .{
        .maximum = 0.20,
    };
    const category = threshold.categorize(0.90);
    std.log.info("category: {t}", .{category});
}

const std = @import("std");
const assert = std.debug.assert;
```

```
$ zig build-exe bad_default_value.zig
$ ./bad_default_value
thread 2237410 panic: reached unreachable code
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/debug.zig:435:14: 0x1029ea9 in assert (std.zig)
    if (!ok) unreachable; // assertion failure
             ^
/home/ci/work/zig-bootstrap/zig/doc/langref/bad_default_value.zig:8:15: 0x11e264a in categorize (bad_default_value.zig)
        assert(t.maximum >= t.minimum);
              ^
/home/ci/work/zig-bootstrap/zig/doc/langref/bad_default_value.zig:19:42: 0x11e10de in main (bad_default_value.zig)
    const category = threshold.categorize(0.90);
                                         ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e16f6 in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

Above you can see the danger of ignoring this principle. The default field values caused the data invariant to be violated, causing illegal behavior.

To fix this, remove the default values from all the struct fields, and provide a named default value:

```
const Threshold = struct {
    minimum: f32,
    maximum: f32,

    const default: Threshold = .{
        .minimum = 0.25,
        .maximum = 0.75,
    };
};
```

If a struct value requires a runtime-known value in order to be initialized without violating data invariants, then use an initialization method that accepts those runtime values, and populates the remaining fields.

### extern struct

An `extern struct` has in-memory layout matching the C ABI for the target.

If well-defined in-memory layout is not required, struct is a better choice because it places fewer restrictions on the compiler.

See packed struct for a struct that has the ABI of its backing integer, which can be useful for modeling flags.

See also:

- extern union
- extern enum

### packed struct

`packed` structs, like `enum`, are based on the concept of interpreting integers differently. All packed structs have a **backing integer**, which is implicitly determined by the total bit count of fields, or explicitly specified. Packed structs have well-defined memory layout - exactly the same ABI as their backing integer.

Each field of a packed struct is interpreted as a logical sequence of bits, arranged from least to most significant. Allowed field types:

- An integer field uses exactly as many bits as its bit width. For example, a `u5` will use 5 bits of the backing integer.
- A bool field uses exactly 1 bit.
- An enum field uses exactly the bit width of its integer tag type.
- A packed union field uses exactly the bit width of the union field with the largest bit width.
- A `packed struct` field uses the bits of its backing integer.

This means that a `packed struct` can participate in a @bitCast or a @ptrCast to reinterpret memory. This even works at comptime:

```
const std = @import("std");
const native_endian = @import("builtin").target.cpu.arch.endian();
const expectEqual = std.testing.expectEqual;

const Full = packed struct {
    number: u16,
};
const Divided = packed struct {
    half1: u8,
    quarter3: u4,
    quarter4: u4,
};

test "@bitCast between packed structs" {
    try doTheTest();
    try comptime doTheTest();
}

fn doTheTest() !void {
    try expectEqual(2, @sizeOf(Full));
    try expectEqual(2, @sizeOf(Divided));
    const full = Full{ .number = 0x1234 };
    const divided: Divided = @bitCast(full);
    try expectEqual(0x34, divided.half1);
    try expectEqual(0x2, divided.quarter3);
    try expectEqual(0x1, divided.quarter4);

    const ordered: [2]u8 = @bitCast(full);
    try expectEqual(0x34, ordered[0]);
    try expectEqual(0x12, ordered[1]);
}
```

```
$ zig test test_packed_structs.zig
1/1 test_packed_structs.test.@bitCast between packed structs...OK
All 1 tests passed.
```

The backing integer can be inferred or explicitly provided. When inferred, it will be unsigned. When explicitly provided, its bit width will be enforced at compile time to exactly match the total bit width of the fields:

```
test "missized packed struct" {
    const S = packed struct(u32) { a: u16, b: u8 };
    _ = S{ .a = 4, .b = 2 };
}
```

```
$ zig test test_missized_packed_struct.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_missized_packed_struct.zig:2:22: error: backing integer bit width does not match total bit width of fields
    const S = packed struct(u32) { a: u16, b: u8 };
              ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_missized_packed_struct.zig:2:29: note: backing integer 'u32' has bit width '32'
    const S = packed struct(u32) { a: u16, b: u8 };
                            ^~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_missized_packed_struct.zig:2:22: note: struct fields have total bit width '24'
referenced by:
    test.missized packed struct: /home/ci/work/zig-bootstrap/zig/doc/langref/test_missized_packed_struct.zig:3:17
```

Zig allows the address to be taken of a non-byte-aligned field:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const BitField = packed struct {
    a: u3,
    b: u3,
    c: u2,
};

var foo = BitField{
    .a = 1,
    .b = 2,
    .c = 3,
};

test "pointer to non-byte-aligned field" {
    const ptr = &foo.b;
    try expectEqual(2, ptr.*);
}
```

```
$ zig test test_pointer_to_non-byte_aligned_field.zig
1/1 test_pointer_to_non-byte_aligned_field.test.pointer to non-byte-aligned field...OK
All 1 tests passed.
```

However, the pointer to a non-byte-aligned field has special properties and cannot be passed when a normal pointer is expected:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const BitField = packed struct {
    a: u3,
    b: u3,
    c: u2,
};

var bit_field = BitField{
    .a = 1,
    .b = 2,
    .c = 3,
};

test "pointer to non-byte-aligned field" {
    try expectEqual(2, bar(&bit_field.b));
}

fn bar(x: *const u3) u3 {
    return x.*;
}
```

```
$ zig test test_misaligned_pointer.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_misaligned_pointer.zig:17:28: error: expected type '*const u3', found '*align(1:3:1) u3'
    try expectEqual(2, bar(&bit_field.b));
                           ^~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_misaligned_pointer.zig:17:28: note: pointer host size '1' cannot cast into pointer host size '0'
/home/ci/work/zig-bootstrap/zig/doc/langref/test_misaligned_pointer.zig:17:28: note: pointer bit offset '3' cannot cast into pointer bit offset '0'
/home/ci/work/zig-bootstrap/zig/doc/langref/test_misaligned_pointer.zig:20:11: note: parameter type declared here
fn bar(x: *const u3) u3 {
          ^~~~~~~~~
```

In this case, the function `bar` cannot be called because the pointer to the non-ABI-aligned field mentions the bit offset, but the function expects an ABI-aligned pointer.

Pointers to non-ABI-aligned fields share the same address as the other fields within their host integer:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const BitField = packed struct {
    a: u3,
    b: u3,
    c: u2,
};

var bit_field = BitField{
    .a = 1,
    .b = 2,
    .c = 3,
};

test "pointers of sub-byte-aligned fields share addresses" {
    try expectEqual(@intFromPtr(&bit_field.a), @intFromPtr(&bit_field.b));
    try expectEqual(@intFromPtr(&bit_field.a), @intFromPtr(&bit_field.c));
}
```

```
$ zig test test_packed_struct_field_address.zig
1/1 test_packed_struct_field_address.test.pointers of sub-byte-aligned fields share addresses...OK
All 1 tests passed.
```

This can be observed with @bitOffsetOf and offsetOf:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const BitField = packed struct {
    a: u3,
    b: u3,
    c: u2,
};

test "offsets of non-byte-aligned fields" {
    comptime {
        try expectEqual(0, @bitOffsetOf(BitField, "a"));
        try expectEqual(3, @bitOffsetOf(BitField, "b"));
        try expectEqual(6, @bitOffsetOf(BitField, "c"));

        try expectEqual(0, @offsetOf(BitField, "a"));
        try expectEqual(0, @offsetOf(BitField, "b"));
        try expectEqual(0, @offsetOf(BitField, "c"));
    }
}
```

```
$ zig test test_bitOffsetOf_offsetOf.zig
1/1 test_bitOffsetOf_offsetOf.test.offsets of non-byte-aligned fields...OK
All 1 tests passed.
```

Packed structs have the same alignment as their backing integer, however, overaligned pointers to packed structs can override this:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const S = packed struct {
    a: u32,
    b: u32,
};
test "overaligned pointer to packed struct" {
    var foo: S align(4) = .{ .a = 1, .b = 2 };
    const ptr: *align(4) S = &foo;
    const ptr_to_b = &ptr.b;
    try expectEqual(2, ptr_to_b.*);
}
```

```
$ zig test test_overaligned_packed_struct.zig
1/1 test_overaligned_packed_struct.test.overaligned pointer to packed struct...OK
All 1 tests passed.
```

It's also possible to set alignment of struct fields:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "aligned struct fields" {
    const S = struct {
        a: u32 align(2),
        b: u32 align(64),
    };
    var foo = S{ .a = 1, .b = 2 };

    try expectEqual(64, @alignOf(S));
    try expectEqual(*align(2) u32, @TypeOf(&foo.a));
    try expectEqual(*align(64) u32, @TypeOf(&foo.b));
}
```

```
$ zig test test_aligned_struct_fields.zig
1/1 test_aligned_struct_fields.test.aligned struct fields...OK
All 1 tests passed.
```

Equating packed structs results in a comparison of the backing integer, and only works for the `==` and `!=` Operators.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "packed struct equality" {
    const S = packed struct {
        a: u4,
        b: u4,
    };
    const x: S = .{ .a = 1, .b = 2 };
    const y: S = .{ .b = 2, .a = 1 };
    try expectEqual(x, y);
}
```

```
$ zig test test_packed_struct_equality.zig
1/1 test_packed_struct_equality.test.packed struct equality...OK
All 1 tests passed.
```

Field access and assignment can be understood as shorthand for bitshifts on the backing integer. These operations are not atomic, so beware using field access syntax when combined with memory-mapped input-output (MMIO). Instead of field access on volatile Pointers, construct a fully-formed new value first, then write that value to the volatile pointer.

```
pub const GpioRegister = packed struct(u8) {
    GPIO0: bool,
    GPIO1: bool,
    GPIO2: bool,
    GPIO3: bool,
    reserved: u4 = 0,
};

const gpio: *volatile GpioRegister = @ptrFromInt(0x0123);

pub fn writeToGpio(new_states: GpioRegister) void {
    
    

    
    gpio.* = new_states;
}
```

### Struct Naming

Since all structs are anonymous, Zig infers the type name based on a few rules.

- If the struct is in the initialization expression of a variable, it gets named after that variable.
- If the struct is in the `return` expression, it gets named after the function it is returning from, with the parameter values serialized.
- Otherwise, the struct gets a name such as `(filename.funcname__struct_ID)`.
- If the struct is declared inside another struct, it gets named after both the parent struct and the name inferred by the previous rules, separated by a dot.

```
const std = @import("std");

pub fn main() void {
    const Foo = struct {};
    std.debug.print("variable: {s}\n", .{@typeName(Foo)});
    std.debug.print("anonymous: {s}\n", .{@typeName(struct {})});
    std.debug.print("function: {s}\n", .{@typeName(List(i32))});
}

fn List(comptime T: type) type {
    return struct {
        x: T,
    };
}
```

```
$ zig build-exe struct_name.zig
$ ./struct_name
variable: struct_name.main.Foo
anonymous: struct_name.main__struct_31913
function: struct_name.List(i32)
```

### Anonymous Struct Literals

Zig allows omitting the struct type of a literal. When the result is coerced, the struct literal will directly instantiate the result location, with no copy:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Point = struct { x: i32, y: i32 };

test "anonymous struct literal" {
    const pt: Point = .{
        .x = 13,
        .y = 67,
    };
    try expectEqual(13, pt.x);
    try expectEqual(67, pt.y);
}
```

```
$ zig test test_struct_result.zig
1/1 test_struct_result.test.anonymous struct literal...OK
All 1 tests passed.
```

The struct type can be inferred. Here the result location does not include a type, and so Zig infers the type:

```
const std = @import("std");
const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;

test "fully anonymous struct" {
    try check(.{
        .int = @as(u32, 1234),
        .float = @as(f64, 12.34),
        .b = true,
        .s = "hi",
    });
}

fn check(args: anytype) !void {
    try expectEqual(1234, args.int);
    try expectEqual(12.34, args.float);
    try expect(args.b);
    try expectEqual('h', args.s[0]);
    try expectEqual('i', args.s[1]);
}
```

```
$ zig test test_anonymous_struct.zig
1/1 test_anonymous_struct.test.fully anonymous struct...OK
All 1 tests passed.
```

### Tuples

Anonymous structs can be created without specifying field names, and are referred to as "tuples". An empty tuple looks like `.{}` and can be seen in one of the Hello World examples.

The fields are implicitly named using numbers starting from 0. Because their names are integers, they cannot be accessed with `.` syntax without also wrapping them in `@""`. Names inside `@""` are always recognised as identifiers.

Like arrays, tuples have a .len field, can be indexed (provided the index is comptime-known) and work with the ++ operator. They can also be iterated over with inline for.

```
const std = @import("std");
const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;

test "tuple" {
    const values = .{
        @as(u32, 1234),
        @as(f64, 12.34),
        true,
        "hi",
    } ++ .{ false, false };
    try expectEqual(1234, values[0]);
    try expectEqual(false, values[4]);
    inline for (values, 0..) |v, i| {
        if (i != 2) continue;
        try expect(v);
    }
    try expectEqual(6, values.len);
    try expectEqual('h', values.@"3"[0]);
}
```

```
$ zig test test_tuples.zig
1/1 test_tuples.test.tuple...OK
All 1 tests passed.
```

#### Destructuring Tuples

Tuples can be destructured.

Tuple destructuring is helpful for returning multiple values from a block:

```
const print = @import("std").debug.print;

pub fn main() void {
    const digits = [_]i8 { 3, 8, 9, 0, 7, 4, 1 };

    const min, const max = blk: {
        var min: i8 = 127;
        var max: i8 = -128;

        for (digits) |digit| {
            if (digit < min) min = digit;
            if (digit > max) max = digit;
        }

        break :blk .{ min, max };
    };

    print("min = {}\n", .{ min });
    print("max = {}\n", .{ max });
}
```

```
$ zig build-exe destructuring_block.zig
$ ./destructuring_block
min = 0
max = 9
```

Tuple destructuring is helpful for dealing with functions and built-ins that return multiple values as a tuple:

```
const print = @import("std").debug.print;

fn divmod(numerator: u32, denominator: u32) struct { u32, u32 } {
    return .{ numerator / denominator, numerator % denominator };
}

pub fn main() void {
    const div, const mod = divmod(10, 3);

    print("10 / 3 = {}\n", .{div});
    print("10 % 3 = {}\n", .{mod});
}
```

```
$ zig build-exe destructuring_return_value.zig
$ ./destructuring_return_value
10 / 3 = 3
10 % 3 = 1
```

See also:

- Destructuring
- Destructuring Arrays
- Destructuring Vectors

See also:

- comptime
- @fieldParentPtr
