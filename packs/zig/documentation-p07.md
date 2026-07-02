---
title: "Documentation (part 7/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 7/10
---

# Documentation

NaNs are handled as follows: return the biggest non-NaN value included. If all operands are NaN, return NaN.

See also:

- @min
- Vectors

### @memcpy

```
@memcpy(noalias dest, noalias source) void
```

This function copies bytes from one region of memory to another.

`dest` must be a mutable slice, a mutable pointer to an array, or a mutable many-item pointer. It may have any alignment, and it may have any element type.

`source` must be a slice, a pointer to an array, or a many-item pointer. It may have any alignment, and it may have any element type.

The `source` element type must have the same in-memory representation as the `dest` element type.

Similar to for loops, at least one of `source` and `dest` must provide a length, and if two lengths are provided, they must be equal.

Finally, the two memory regions must not overlap.

### @memset

```
@memset(dest, elem) void
```

This function sets all the elements of a memory region to `elem`.

`dest` must be a mutable slice or a mutable pointer to an array. It may have any alignment, and it may have any element type.

`elem` is coerced to the element type of `dest`.

For securely zeroing out sensitive contents from memory, you should use `std.crypto.secureZero`

### @memmove

```
@memmove(dest, source) void
```

This function copies bytes from one region of memory to another, but unlike @memcpy the regions may overlap.

`dest` must be a mutable slice, a mutable pointer to an array, or a mutable many-item pointer. It may have any alignment, and it may have any element type.

`source` must be a slice, a pointer to an array, or a many-item pointer. It may have any alignment, and it may have any element type.

The `source` element type must have the same in-memory representation as the `dest` element type.

Similar to for loops, at least one of `source` and `dest` must provide a length, and if two lengths are provided, they must be equal.

### @min

```
@min(...) T
```

Takes two or more arguments and returns the smallest value included (the minimum). This builtin accepts integers, floats, and vectors of either. In the latter case, the operation is performed element wise.

NaNs are handled as follows: return the smallest non-NaN value included. If all operands are NaN, return NaN.

See also:

- @max
- Vectors

### @wasmMemorySize

```
@wasmMemorySize(index: u32) usize
```

This function returns the size of the Wasm memory identified by `index` as an unsigned value in units of Wasm pages. Note that each Wasm page is 64KB in size.

This function is a low level intrinsic with no safety mechanisms usually useful for allocator designers targeting Wasm. So unless you are writing a new allocator from scratch, you should use something like `@import("std").heap.WasmPageAllocator`.

See also:

- @wasmMemoryGrow

### @wasmMemoryGrow

```
@wasmMemoryGrow(index: u32, delta: usize) isize
```

This function increases the size of the Wasm memory identified by `index` by `delta` in units of unsigned number of Wasm pages. Note that each Wasm page is 64KB in size. On success, returns previous memory size; on failure, if the allocation fails, returns -1.

This function is a low level intrinsic with no safety mechanisms usually useful for allocator designers targeting Wasm. So unless you are writing a new allocator from scratch, you should use something like `@import("std").heap.WasmPageAllocator`.

```
const std = @import("std");
const native_arch = @import("builtin").target.cpu.arch;
const expectEqual = std.testing.expectEqual;

test "@wasmMemoryGrow" {
    if (native_arch != .wasm32) return error.SkipZigTest;

    const prev = @wasmMemorySize(0);
    try expectEqual(@wasmMemoryGrow(0, 1), prev);
    try expectEqual(@wasmMemorySize(0), prev + 1);
}
```

```
$ zig test test_wasmMemoryGrow_builtin.zig
1/1 test_wasmMemoryGrow_builtin.test.@wasmMemoryGrow...SKIP
0 passed; 1 skipped; 0 failed.
```

See also:

- @wasmMemorySize

### @mod

```
@mod(numerator: T, denominator: T) T
```

Modulus division. For unsigned integers this is the same as `numerator % denominator`. Caller guarantees `denominator != 0`, otherwise the operation will result in a Remainder Division by Zero when runtime safety checks are enabled.

- `@mod(-5, 3) == 1`
- `(@divFloor(a, b) * b) + @mod(a, b) == a`

For a function that returns an error code, see `@import("std").math.mod`.

See also:

- @rem

### @mulWithOverflow

```
@mulWithOverflow(a: anytype, b: anytype) struct { @TypeOf(a, b), u1 }
```

Performs `a * b` and returns a tuple with the result and a possible overflow bit.

### @panic

```
@panic(message: []const u8) noreturn
```

Invokes the panic handler function. By default the panic handler function calls the public `panic` function exposed in the root source file, or if there is not one specified, the `std.lang.default_panic` function from `std/lang.zig`.

Generally it is better to use `@import("std").debug.panic`. However, `@panic` can be useful for 2 scenarios:

- From library code, calling the programmer's panic function if they exposed one in the root source file.
- When mixing C and Zig code, calling the canonical panic implementation across multiple .o files.

See also:

- Panic Handler

### @popCount

```
@popCount(operand: anytype) anytype
```

`@TypeOf(operand)` must be an integer type.

`operand` may be an integer or vector.

Counts the number of bits set in an integer - "population count".

The return type is an unsigned integer or vector of unsigned integers with the minimum number of bits that can represent the bit count of the integer type.

See also:

- @ctz
- @clz

### @prefetch

```
@prefetch(ptr: anytype, comptime options: PrefetchOptions) void
```

This builtin tells the compiler to emit a prefetch instruction if supported by the target CPU. If the target CPU does not support the requested prefetch instruction, this builtin is a no-op. This function has no effect on the behavior of the program, only on the performance characteristics.

The `ptr` argument may be any pointer type and determines the memory address to prefetch. This function does not dereference the pointer, it is perfectly legal to pass a pointer to invalid memory to this function and no Illegal Behavior will result.

`PrefetchOptions` can be found with `@import("std").lang.PrefetchOptions`.

### @ptrCast

```
@ptrCast(value: anytype) anytype
```

Converts a pointer of one type to a pointer of another type. The return type is the inferred result type.

Optional Pointers are allowed. Casting an optional pointer which is null to a non-optional pointer invokes safety-checked Illegal Behavior.

`@ptrCast` cannot be used for:

- Removing `const` qualifier, use @constCast.
- Removing `volatile` qualifier, use @volatileCast.
- Changing pointer address space, use @addrSpaceCast.
- Increasing pointer alignment, use @alignCast.
- Casting a non-slice pointer to a slice, use slicing syntax `ptr[start..end]`.

### @ptrFromInt

```
@ptrFromInt(address: usize) anytype
```

Converts an integer to a pointer. The return type is the inferred result type. To convert the other way, use @intFromPtr. Casting an address of 0 to a destination type which in not optional and does not have the `allowzero` attribute will result in a Pointer Cast Invalid Null panic when runtime safety checks are enabled.

If the destination pointer type does not allow address zero and `address` is zero, this invokes safety-checked Illegal Behavior.

### @rem

```
@rem(numerator: T, denominator: T) T
```

Remainder division. For unsigned integers this is the same as `numerator % denominator`. Caller guarantees `denominator != 0`, otherwise the operation will result in a Remainder Division by Zero when runtime safety checks are enabled.

- `@rem(-5, 3) == -2`
- `(@divTrunc(a, b) * b) + @rem(a, b) == a`

For a function that returns an error code, see `@import("std").math.rem`.

See also:

- @mod

### @returnAddress

```
@returnAddress() usize
```

This function returns the address of the next machine code instruction that will be executed when the current function returns.

The implications of this are target-specific and not consistent across all platforms.

This function is only valid within function scope. If the function gets inlined into a calling function, the returned address will apply to the calling function.

### @select

```
@select(comptime T: type, pred: @Vector(len, bool), a: @Vector(len, T), b: @Vector(len, T)) @Vector(len, T)
```

Selects values element-wise from `a` or `b` based on `pred`. If `pred[i]` is `true`, the corresponding element in the result will be `a[i]` and otherwise `b[i]`.

See also:

- Vectors

### @setEvalBranchQuota

```
@setEvalBranchQuota(comptime new_quota: u32) void
```

Increase the maximum number of backwards branches that compile-time code execution can use before giving up and making a compile error.

If the `new_quota` is smaller than the default quota (`1000`) or a previously explicitly set quota, it is ignored.

Example:

```
test "foo" {
    comptime {
        var i = 0;
        while (i < 1001) : (i += 1) {}
    }
}
```

```
$ zig test test_without_setEvalBranchQuota_builtin.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_without_setEvalBranchQuota_builtin.zig:4:9: error: evaluation exceeded 1000 backwards branches
        while (i < 1001) : (i += 1) {}
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_without_setEvalBranchQuota_builtin.zig:4:9: note: use @setEvalBranchQuota() to raise the branch limit from 1000
```

Now we use `@setEvalBranchQuota`:

```
test "foo" {
    comptime {
        @setEvalBranchQuota(1001);
        var i = 0;
        while (i < 1001) : (i += 1) {}
    }
}
```

```
$ zig test test_setEvalBranchQuota_builtin.zig
1/1 test_setEvalBranchQuota_builtin.test.foo...OK
All 1 tests passed.
```

See also:

- comptime

### @setFloatMode

```
@setFloatMode(comptime mode: FloatMode) void
```

Changes the current scope's rules about how floating point operations are defined.

- `.strict` (default) - Floating point operations follow strict IEEE compliance.
- `.optimized` - Floating point operations may do all of the following: This is equivalent to `-ffast-math` in GCC.
  - Assume the arguments and result are not NaN. Optimizations are required to retain legal behavior over NaNs, but the value of the result is undefined.
  - Assume the arguments and result are not +/-Inf. Optimizations are required to retain legal behavior over +/-Inf, but the value of the result is undefined.
  - Treat the sign of a zero argument or result as insignificant.
  - Use the reciprocal of an argument rather than perform division.
  - Perform floating-point contraction (e.g. fusing a multiply followed by an addition into a fused multiply-add).
  - Perform algebraically equivalent transformations that may change results in floating point (e.g. reassociate).

The floating point mode is inherited by child scopes, and can be overridden in any scope. You can set the floating point mode in a struct or module scope by using a comptime block.

`FloatMode` can be found with `@import("std").lang.FloatMode`.

See also:

- Floating Point Operations

### @setRuntimeSafety

```
@setRuntimeSafety(comptime safety_on: bool) void
```

Sets whether runtime safety checks are enabled for the scope that contains the function call.

```
test "@setRuntimeSafety" {
    
    
    
    
    {
        
        
        @setRuntimeSafety(true);
        var x: u8 = 255;
        x += 1;

        {
            
            
            @setRuntimeSafety(false);
            
            
        }
    }
}
```

```
$ zig test test_setRuntimeSafety_builtin.zig -OReleaseFast
1/1 test_setRuntimeSafety_builtin.test.@setRuntimeSafety...thread 2238681 panic: integer overflow
/home/ci/work/zig-bootstrap/out/zig-local-cache/tmp/f8456721e8b37f9e/../../../../zig/doc/langref/test_setRuntimeSafety_builtin.zig:11:11: 0x1078948 in test.@setRuntimeSafety (test)
        x += 1;
          ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:296:25: 0x106a8d2 in mainTerminal (test)
        if (test_fn.func()) |_| {
                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:752:88: 0x1068fb6 in callMain (test)
    if (fn_info.param_types[0].? == std.process.Init.Minimal) return wrapMain(root.main(.{
                                                                                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x1068c5d in _start (test)
    asm volatile (switch (native_arch) {
    ^
error: the following test command terminated with signal ABRT:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/b182ce0bd33e78fab90f9d04d1213967/test --seed=0xea4498ee
```

Note: it is planned to replace `@setRuntimeSafety` with `@optimizeFor`

### @shlExact

```
@shlExact(value: T, shift_amt: Log2T) T
```

Performs the left shift operation (`<<`). For unsigned integers, the result is undefined if any 1 bits are shifted out. For signed integers, the result is undefined if any bits that disagree with the resultant sign bit are shifted out.

The type of `shift_amt` is an unsigned integer with `log2(@typeInfo(T).int.bits)` bits. This is because `shift_amt >= @typeInfo(T).int.bits` triggers safety-checked Illegal Behavior.

`comptime_int` is modeled as an integer with an infinite number of bits, meaning that in such case, `@shlExact` always produces a result and cannot produce a compile error.

See also:

- @shrExact
- @shlWithOverflow

### @shlWithOverflow

```
@shlWithOverflow(a: anytype, shift_amt: Log2T) struct { @TypeOf(a), u1 }
```

Performs `a << b` and returns a tuple with the result and a possible overflow bit.

The type of `shift_amt` is an unsigned integer with `log2(@typeInfo(@TypeOf(a)).int.bits)` bits. This is because `shift_amt >= @typeInfo(@TypeOf(a)).int.bits` triggers safety-checked Illegal Behavior.

See also:

- @shlExact
- @shrExact

### @shrExact

```
@shrExact(value: T, shift_amt: Log2T) T
```

Performs the right shift operation (`>>`). Caller guarantees that the shift will not shift any 1 bits out.

The type of `shift_amt` is an unsigned integer with `log2(@typeInfo(T).int.bits)` bits. This is because `shift_amt >= @typeInfo(T).int.bits` triggers safety-checked Illegal Behavior.

See also:

- @shlExact
- @shlWithOverflow

### @shuffle

```
@shuffle(comptime E: type, a: @Vector(a_len, E), b: @Vector(b_len, E), comptime mask: @Vector(mask_len, i32)) @Vector(mask_len, E)
```

Constructs a new vector by selecting elements from `a` and `b` based on `mask`.

Each element in `mask` selects an element from either `a` or `b`. Positive numbers select from `a` starting at 0. Negative values select from `b`, starting at `-1` and going down. It is recommended to use the `~` operator for indexes from `b` so that both indexes can start from `0` (i.e. `~@as(i32, 0)` is `-1`).

For each element of `mask`, if it or the selected value from `a` or `b` is `undefined`, then the resulting element is `undefined`.

`a_len` and `b_len` may differ in length. Out-of-bounds element indexes in `mask` result in compile errors.

If `a` or `b` is `undefined`, it is equivalent to a vector of all `undefined` with the same length as the other vector. If both vectors are `undefined`, `@shuffle` returns a vector with all elements `undefined`.

`E` must be an integer, float, pointer, or `bool`. The mask may be any vector length, and its length determines the result length.

```
const std = @import("std");
const expectEqualStrings = std.testing.expectEqualStrings;

test "vector @shuffle" {
    const a = @Vector(7, u8){ 'o', 'l', 'h', 'e', 'r', 'z', 'w' };
    const b = @Vector(4, u8){ 'w', 'd', '!', 'x' };

    
    
    const mask1 = @Vector(5, i32){ 2, 3, 1, 1, 0 };
    const res1: @Vector(5, u8) = @shuffle(u8, a, undefined, mask1);
    try expectEqualStrings("hello", &@as([5]u8, res1));

    
    const mask2 = @Vector(6, i32){ -1, 0, 4, 1, -2, -3 };
    const res2: @Vector(6, u8) = @shuffle(u8, a, b, mask2);
    try expectEqualStrings("world!", &@as([6]u8, res2));
}
```

```
$ zig test test_shuffle_builtin.zig
1/1 test_shuffle_builtin.test.vector @shuffle...OK
All 1 tests passed.
```

See also:

- Vectors

### @sizeOf

```
@sizeOf(comptime T: type) comptime_int
```

This function returns the number of bytes it takes to store `T` in memory. The result is a target-specific compile time constant.

This size may contain padding bytes. If there were two consecutive T in memory, the padding would be the offset in bytes between element at index 0 and the element at index 1. For integer, consider whether you want to use `@sizeOf(T)` or `@typeInfo(T).int.bits`.

This function measures the size at runtime. For types that are disallowed at runtime, such as `comptime_int` and `type`, the result is `0`.

See also:

- @bitSizeOf
- @typeInfo

### @splat

```
@splat(scalar: anytype) anytype
```

Produces an array or vector where each element is the value `scalar`. The return type and thus the length of the vector is inferred.

```
const std = @import("std");
const expectEqualSlices = std.testing.expectEqualSlices;

test "vector @splat" {
    const scalar: u32 = 5;
    const result: @Vector(4, u32) = @splat(scalar);
    try expectEqualSlices(u32, &[_]u32{ 5, 5, 5, 5 }, &@as([4]u32, result));
}

test "array @splat" {
    const scalar: u32 = 5;
    const result: [4]u32 = @splat(scalar);
    try expectEqualSlices(u32, &[_]u32{ 5, 5, 5, 5 }, &@as([4]u32, result));
}
```

```
$ zig test test_splat_builtin.zig
1/2 test_splat_builtin.test.vector @splat...OK
2/2 test_splat_builtin.test.array @splat...OK
All 2 tests passed.
```

`scalar` must be an integer, bool, float, or pointer.

See also:

- Vectors
- @shuffle

### @reduce

```
@reduce(comptime op: std.lang.ReduceOp, value: anytype) E
```

Transforms a vector into a scalar value (of type `E`) by performing a sequential horizontal reduction of its elements using the specified operator `op`.

Not every operator is available for every vector element type:

- Every operator is available for integer vectors.
- `.And`, `.Or`, `.Xor` are additionally available for `bool` vectors,
- `.Min`, `.Max`, `.Add`, `.Mul` are additionally available for floating point vectors,

Note that `.Add` and `.Mul` reductions on integral types are wrapping; when applied on floating point types the operation associativity is preserved, unless the float mode is set to `.optimized`.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "vector @reduce" {
    const V = @Vector(4, i32);
    const value = V{ 1, -1, 1, -1 };
    const result = value > @as(V, @splat(0));
    
    try comptime expectEqual(@Vector(4, bool), @TypeOf(result));
    const is_all_true = @reduce(.And, result);
    try comptime expectEqual(bool, @TypeOf(is_all_true));
    try expectEqual(false, is_all_true);
}
```

```
$ zig test test_reduce_builtin.zig
1/1 test_reduce_builtin.test.vector @reduce...OK
All 1 tests passed.
```

See also:

- Vectors
- @setFloatMode

### @src

```
@src() std.lang.SourceLocation
```

Returns a `SourceLocation` struct representing the function's name and location in the source code. This must be called in a function.

```
const std = @import("std");
const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;

test "@src" {
    try doTheTest();
}

fn doTheTest() !void {
    const src = @src();

    try expectEqual(10, src.line);
    try expectEqual(17, src.column);
    try expect(std.mem.endsWith(u8, src.fn_name, "doTheTest"));
    try expect(std.mem.endsWith(u8, src.file, "test_src_builtin.zig"));
}
```

```
$ zig test test_src_builtin.zig
1/1 test_src_builtin.test.@src...OK
All 1 tests passed.
```

### @sqrt

```
@sqrt(value: anytype) @TypeOf(value)
```

Performs the square root of a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @sin

```
@sin(value: anytype) @TypeOf(value)
```

Sine trigonometric function on a floating point number in radians. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @cos

```
@cos(value: anytype) @TypeOf(value)
```

Cosine trigonometric function on a floating point number in radians. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @tan

```
@tan(value: anytype) @TypeOf(value)
```

Tangent trigonometric function on a floating point number in radians. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @exp

```
@exp(value: anytype) @TypeOf(value)
```

Base-e exponential function on a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @exp2

```
@exp2(value: anytype) @TypeOf(value)
```

Base-2 exponential function on a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @log

```
@log(value: anytype) @TypeOf(value)
```

Returns the natural logarithm of a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @log2

```
@log2(value: anytype) @TypeOf(value)
```

Returns the logarithm to the base 2 of a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @log10

```
@log10(value: anytype) @TypeOf(value)
```

Returns the logarithm to the base 10 of a floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

### @abs

```
@abs(value: anytype) anytype
```

Returns the absolute value of an integer or a floating point number. Uses a dedicated hardware instruction when available. The return type is always an unsigned integer of the same bit width as the operand if the operand is an integer. Unsigned integer operands are supported. The builtin cannot overflow for signed integer operands.

Supports Floats, Integers and Vectors of floats or integers.

### @floor

```
@floor(value: anytype) @TypeOf(value)
```

Returns the largest integral value not greater than the given floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

When the inferred result type is an integer, the integer part is extracted from the floored result. If that value cannot fit in the destination type, it invokes safety-checked Illegal Behavior.

### @ceil

```
@ceil(value: anytype) @TypeOf(value)
```

Returns the smallest integral value not less than the given floating point number. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of floats.

When the inferred result type is an integer, the integer part is extracted from the ceiled result. If that value cannot fit in the destination type, it invokes safety-checked Illegal Behavior.

### @trunc

```
@trunc(value: anytype) @TypeOf(value)
```

Rounds the given floating point number to an integer, towards zero. Uses a dedicated hardware instruction when available.

Supports Floats and Vectors of float parameters.

When the inferred result type is an integer, the integer part is extracted from the truncated result. If that value cannot fit in the destination type, it invokes safety-checked Illegal Behavior.

### @round

```
@round(value: anytype) @TypeOf(value)
```

Rounds the given floating point number to the nearest integer. If two integers are equally close, rounds away from zero. Uses a dedicated hardware instruction when available.

```
const expectEqual = @import("std").testing.expectEqual;

test "@round" {
    try expectEqual(1, @round(1.4));
    try expectEqual(2, @round(1.5));
    try expectEqual(-1, @round(-1.4));
    try expectEqual(-3, @round(-2.5));
}
```

```
$ zig test test_round_builtin.zig
1/1 test_round_builtin.test.@round...OK
All 1 tests passed.
```

Supports Floats and Vectors of floats.

When the inferred result type is an integer, the integer part is extracted from the rounded result. If that value cannot fit in the destination type, it invokes safety-checked Illegal Behavior.

### @subWithOverflow

```
@subWithOverflow(a: anytype, b: anytype) struct { @TypeOf(a, b), u1 }
```

Performs `a - b` and returns a tuple with the result and a possible overflow bit.

### @tagName

```
@tagName(value: anytype) [:0]const u8
```

Converts an enum value or union value to a string literal representing the name.

If the enum is non-exhaustive and the tag value does not map to a name, it invokes safety-checked Illegal Behavior.

### @This

```
@This() type
```

Returns the innermost struct, enum, or union that this function call is inside. This can be useful for an anonymous struct that needs to refer to itself:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "@This()" {
    var items = [_]i32{ 1, 2, 3, 4 };
    const list = List(i32){ .items = items[0..] };
    try expectEqual(4, list.length());
}

fn List(comptime T: type) type {
    return struct {
        const Self = @This();

        items: []T,

        fn length(self: Self) usize {
            return self.items.len;
        }
    };
}
```

```
$ zig test test_this_builtin.zig
1/1 test_this_builtin.test.@This()...OK
All 1 tests passed.
```

When `@This()` is used at file scope, it returns a reference to the struct that corresponds to the current file.

### @trap

```
@trap() noreturn
```

This function inserts a platform-specific trap/jam instruction which can be used to exit the program abnormally. This may be implemented by explicitly emitting an invalid instruction which may cause an illegal instruction exception of some sort. Unlike for `@breakpoint()`, execution does not continue after this point.

Outside function scope, this builtin causes a compile error.

See also:

- @breakpoint

### @truncate

```
@truncate(integer: anytype) anytype
```

This function truncates bits from an integer type, resulting in a smaller or same-sized integer type. The return type is the inferred result type.

This function always truncates the significant bits of the integer, regardless of endianness on the target platform.

Calling `@truncate` on a number out of range of the destination type is well defined and working code:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "integer truncation" {
    const a: u16 = 0xabcd;
    const b: u8 = @truncate(a);
    try expectEqual(0xcd, b);
}
```

```
$ zig test test_truncate_builtin.zig
1/1 test_truncate_builtin.test.integer truncation...OK
All 1 tests passed.
```

Use @intCast to convert numbers guaranteed to fit the destination type.

### @EnumLiteral

```
@EnumLiteral() type
```

Returns the comptime-only "enum literal" type. This is the type of uncoerced Enum Literals. Values of this type can coerce to any enum with a matching field.

### @Int

```
@Int(comptime signedness: std.lang.Signedness, comptime bits: u16) type
```

Returns an integer type with the given signedness and bit width.

For instance, `@Int(.unsigned, 18)` returns the type `u18`.

### @Tuple

```
@Tuple(comptime field_types: []const type) type
```

Returns a tuple type with the given field types.

### @Pointer

```
@Pointer(
    comptime size: std.lang.Type.Pointer.Size,
    comptime attrs: std.lang.Type.Pointer.Attributes,
    comptime Element: type,
    comptime sentinel: ?Element,
) type
```

Returns a pointer type with the properties specified by the arguments.

### @Fn

```
@Fn(
    comptime param_types: []const type,
    comptime param_attrs: *const [param_types.len]std.lang.Type.Fn.ParamAttributes,
    comptime ReturnType: type,
    comptime attrs: std.lang.Type.Fn.Attributes,
) type
```

Returns a function type with the properties specified by the arguments.

### @Struct

```
@Struct(
    comptime layout: std.lang.Type.ContainerLayout,
    comptime BackingInt: ?type,
    comptime field_names: []const []const u8,
    comptime field_types: *const [field_names.len]type,
    comptime field_attrs: *const [field_names.len]std.lang.Type.Struct.FieldAttributes,
) type
```

Returns a struct type with the properties specified by the arguments.

### @Union

```
@Union(
    comptime layout: std.lang.Type.ContainerLayout,
    
    comptime ArgType: ?type,
    comptime field_names: []const []const u8,
    comptime field_types: *const [field_names.len]type,
    comptime field_attrs: *const [field_names.len]std.lang.Type.Union.FieldAttributes,
) type
```

Returns a union type with the properties specified by the arguments.

### @Enum

```
@Enum(
    comptime TagInt: type,
    comptime mode: std.lang.Type.Enum.Mode,
    comptime field_names: []const []const u8,
    comptime field_values: *const [field_names.len]TagInt,
) type
```

Returns an enum type with the properties specified by the arguments.

### @SpirvType

```
@SpirvType(comptime options: std.lang.Type.Spirv) type
```

Returns a SPIR-V type with the properties specified by the arguments.

| Tag | SPIR-V Equivalent | Description |
|---|---|---|
| `.sampler` | `OpTypeSampler` | An opaque sampler |
| `.image` | `OpTypeImage` | An opaque image |
| `.sampled_image` | `OpTypeSampledImage` | An opaque image combined with a sampler |
| `.runtime_array` | `OpTypeRuntimeArray` | An array whose length is determined at runtime. The resulting type supports indexing and exposes a `.len` field. It may only appear as the last field of an extern struct. |

### @typeInfo

```
@typeInfo(comptime T: type) std.lang.Type
```

Provides type reflection.

Type information of structs, unions, enums, and error sets has fields which are guaranteed to be in the same order as appearance in the source file.

Type information of structs, unions, enums, and opaques has declarations, which are also guaranteed to be in the same order as appearance in the source file.

### @typeName

```
@typeName(T: type) *const [N:0]u8
```

This function returns the string representation of a type, as an array. It is equivalent to a string literal of the type name. The returned type name is fully qualified with the parent namespace included as part of the type name with a series of dots.

### @TypeOf

```
@TypeOf(...) type
```

`@TypeOf` is a special builtin function that takes any (non-zero) number of expressions as parameters and returns the type of the result, using Peer Type Resolution.

The expressions are evaluated, however they are guaranteed to have no *runtime* side-effects:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "no runtime side effects" {
    var data: i32 = 0;
    const T = @TypeOf(foo(i32, &data));
    try comptime expectEqual(i32, T);
    try expectEqual(0, data);
}

fn foo(comptime T: type, ptr: *T) T {
    ptr.* += 1;
    return ptr.*;
}
```

```
$ zig test test_TypeOf_builtin.zig
1/1 test_TypeOf_builtin.test.no runtime side effects...OK
All 1 tests passed.
```

### @unionInit

```
@unionInit(comptime Union: type, comptime active_field_name: []const u8, init_expr) Union
```

This is the same thing as union initialization syntax, except that the field name is a comptime-known value rather than an identifier token.

`@unionInit` forwards its result location to `init_expr`.

### @Vector

```
@Vector(len: comptime_int, Element: type) type
```

Creates Vectors.

### @volatileCast

```
@volatileCast(value: anytype) DestType
```

Remove `volatile` qualifier from a pointer.

### @workGroupId

```
@workGroupId(comptime dimension: u32) u32
```

Returns the index of the work group in the current kernel invocation in dimension `dimension`.

### @workGroupSize

```
@workGroupSize(comptime dimension: u32) u32
```

Returns the number of work items that a work group has in dimension `dimension`.

### @workItemId

```
@workItemId(comptime dimension: u32) u32
```

Returns the index of the work item in the work group in dimension `dimension`. This function returns values between `0` (inclusive) and `@workGroupSize(dimension)` (exclusive).


## Build Mode

Zig has four build modes:

- Debug (default)
- ReleaseFast
- ReleaseSafe
- ReleaseSmall

To add standard build options to a `build.zig` file:

```
const std = @import("std");

pub fn build(b: *std.Build) void {
    const optimize = b.standardOptimizeOption(.{});
    const exe = b.addExecutable(.{
        .name = "example",
        .root_module = b.createModule(.{
            .root_source_file = b.path("example.zig"),
            .optimize = optimize,
        }),
    });
    b.default_step.dependOn(&exe.step);
}
```

This causes these options to be available:

**-Doptimize=Debug**

Optimizations off and safety on (default)

**-Doptimize=ReleaseSafe**

Optimizations on and safety on

**-Doptimize=ReleaseFast**

Optimizations on and safety off

**-Doptimize=ReleaseSmall**

Size optimizations on and safety off

### Debug

```
$ zig build-exe example.zig
```

- Fast compilation speed
- Safety checks enabled
- Slow runtime performance
- Large binary size
- No reproducible build requirement

### ReleaseFast

```
$ zig build-exe example.zig -O ReleaseFast
```

- Fast runtime performance
- Safety checks disabled
- Slow compilation speed
- Large binary size
- Reproducible build

### ReleaseSafe

```
$ zig build-exe example.zig -O ReleaseSafe
```

- Medium runtime performance
- Safety checks enabled
- Slow compilation speed
- Large binary size
- Reproducible build

### ReleaseSmall

```
$ zig build-exe example.zig -O ReleaseSmall
```

- Medium runtime performance
- Safety checks disabled
- Slow compilation speed
- Small binary size
- Reproducible build

See also:

- Compile Variables
- Zig Build System
- Illegal Behavior


## Single Threaded Builds

Zig has a compile option -fsingle-threaded which has the following effects:

- All Thread Local Variables are treated as regular Namespace Level Variables.
- The overhead of Async Functions becomes equivalent to function call overhead.
- The `@import("builtin").single_threaded` becomes `true` and therefore various userland APIs which read this variable become more efficient. For example `std.Mutex` becomes an empty data structure and all of its functions become no-ops.
