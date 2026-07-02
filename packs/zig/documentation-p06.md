---
title: "Documentation (part 6/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 6/10
---

## Builtin Functions

Builtin functions are provided by the compiler and are prefixed with `@`. The `comptime` keyword on a parameter means that the parameter must be known at compile time.

### @addrSpaceCast

```
@addrSpaceCast(ptr: anytype) anytype
```

Converts a pointer from one address space to another. The new address space is inferred based on the result type. Depending on the current target and address spaces, this cast may be a no-op, a complex operation, or illegal. If the cast is legal, then the resulting pointer points to the same memory location as the pointer operand. It is always valid to cast a pointer between the same address spaces.

### @addWithOverflow

```
@addWithOverflow(a: anytype, b: anytype) struct { @TypeOf(a, b), u1 }
```

Performs `a + b` and returns a tuple with the result and a possible overflow bit.

### @alignCast

```
@alignCast(ptr: anytype) anytype
```

`ptr` can be `*T`, `?*T`, or `[]T`. Changes the alignment of a pointer. The alignment to use is inferred based on the result type.

A pointer alignment safety check is added to the generated code to make sure the pointer is aligned as promised.

### @alignOf

```
@alignOf(comptime T: type) comptime_int
```

This function returns the number of bytes that this type should be aligned to for the current target to match the C ABI. When the child type of a pointer has this alignment, the alignment can be omitted from the type.

```
const assert = @import("std").debug.assert;
comptime {
    assert(*u32 == *align(@alignOf(u32)) u32);
}
```

The result is a target-specific compile time constant. It is guaranteed to be less than or equal to @sizeOf(T).

See also:

- Alignment

### @as

```
@as(comptime T: type, expression) T
```

Performs Type Coercion. This cast is allowed when the conversion is unambiguous and safe, and is the preferred way to convert between types, whenever possible.

### @atomicLoad

```
@atomicLoad(comptime T: type, ptr: *const T, comptime ordering: AtomicOrder) T
```

This builtin function atomically dereferences a pointer to a `T` and returns the value.

`T` must be a pointer, a `bool`, a float, an integer, an enum, or a packed struct.

`AtomicOrder` can be found with `@import("std").lang.AtomicOrder`.

See also:

- @atomicStore
- @atomicRmw
- @cmpxchgWeak
- @cmpxchgStrong

### @atomicRmw

```
@atomicRmw(comptime T: type, ptr: *T, comptime op: AtomicRmwOp, operand: T, comptime ordering: AtomicOrder) T
```

This builtin function dereferences a pointer to a `T` and atomically modifies the value and returns the previous value.

`T` must be a pointer, a `bool`, a float, an integer, an enum, or a packed struct.

`AtomicOrder` can be found with `@import("std").lang.AtomicOrder`.

`AtomicRmwOp` can be found with `@import("std").lang.AtomicRmwOp`.

See also:

- @atomicStore
- @atomicLoad
- @cmpxchgWeak
- @cmpxchgStrong

### @atomicStore

```
@atomicStore(comptime T: type, ptr: *T, value: T, comptime ordering: AtomicOrder) void
```

This builtin function dereferences a pointer to a `T` and atomically stores the given value.

`T` must be a pointer, a `bool`, a float, an integer, an enum, or a packed struct.

`AtomicOrder` can be found with `@import("std").lang.AtomicOrder`.

See also:

- @atomicLoad
- @atomicRmw
- @cmpxchgWeak
- @cmpxchgStrong

### @bitCast

```
@bitCast(value: anytype) anytype
```

Converts a value of one type to another type. The return type is the inferred result type.

Asserts that `@sizeOf(@TypeOf(value)) == @sizeOf(DestType)`.

Asserts that `@typeInfo(DestType) != .pointer`. Use `@ptrCast` or `@ptrFromInt` if you need this.

Can be used for these things for example:

- Convert `f32` to `u32` bits
- Convert `i32` to `u32` preserving twos complement

Works at compile-time if `value` is known at compile time. It's a compile error to bitcast a value of undefined layout; this means that, besides the restriction from types which possess dedicated casting builtins (enums, pointers, error sets), bare structs, error unions, slices, optionals, and any other type without a well-defined memory layout, also cannot be used in this operation.

### @bitOffsetOf

```
@bitOffsetOf(comptime T: type, comptime field_name: []const u8) comptime_int
```

Returns the bit offset of a field relative to its containing struct.

For non packed structs, this will always be divisible by `8`. For packed structs, non-byte-aligned fields will share a byte offset, but they will have different bit offsets.

See also:

- @offsetOf

### @bitSizeOf

```
@bitSizeOf(comptime T: type) comptime_int
```

This function returns the number of bits it takes to store `T` in memory if the type were a field in a packed struct/union. The result is a target-specific compile time constant.

This function measures the size at runtime. For types that are disallowed at runtime, such as `comptime_int` and `type`, the result is `0`.

See also:

- @sizeOf
- @typeInfo

### @branchHint

```
@branchHint(hint: BranchHint) void
```

Hints to the optimizer how likely a given branch of control flow is to be reached.

`BranchHint` can be found with `@import("std").lang.BranchHint`.

This function is only valid as the first statement in a control flow branch, or the first statement in a function.

### @breakpoint

```
@breakpoint() void
```

This function inserts a platform-specific debug trap instruction which causes debuggers to break there. Unlike for `@trap()`, execution may continue after this point if the program is resumed.

This function is only valid within function scope.

See also:

- @trap

### @mulAdd

```
@mulAdd(comptime T: type, a: T, b: T, c: T) T
```

Fused multiply-add, similar to `(a * b) + c`, except only rounds once, and is thus more accurate.

Supports Floats and Vectors of floats.

### @byteSwap

```
@byteSwap(operand: anytype) T
```

`@TypeOf(operand)` must be an integer type or an integer vector type with bit count evenly divisible by 8.

`operand` may be an integer or vector.

Swaps the byte order of the integer. This converts a big endian integer to a little endian integer, and converts a little endian integer to a big endian integer.

Note that for the purposes of memory layout with respect to endianness, the integer type should be related to the number of bytes reported by @sizeOf bytes. This is demonstrated with `u24`. `@sizeOf(u24) == 4`, which means that a `u24` stored in memory takes 4 bytes, and those 4 bytes are what are swapped on a little vs big endian system. On the other hand, if `T` is specified to be `u24`, then only 3 bytes are reversed.

### @bitReverse

```
@bitReverse(integer: anytype) T
```

`@TypeOf(anytype)` accepts any integer type or integer vector type.

Reverses the bitpattern of an integer value, including the sign bit if applicable.

For example 0b10110110 (`u8 = 182`, `i8 = -74`) becomes 0b01101101 (`u8 = 109`, `i8 = 109`).

### @offsetOf

```
@offsetOf(comptime T: type, comptime field_name: []const u8) comptime_int
```

Returns the byte offset of a field relative to its containing struct.

See also:

- @bitOffsetOf

### @call

```
@call(modifier: std.lang.CallModifier, function: anytype, args: anytype) anytype
```

Calls a function, in the same way that invoking an expression with parentheses does:

```
const expectEqual = @import("std").testing.expectEqual;

test "noinline function call" {
    try expectEqual(12, @call(.auto, add, .{ 3, 9 }));
}

fn add(a: i32, b: i32) i32 {
    return a + b;
}
```

```
$ zig test test_call_builtin.zig
1/1 test_call_builtin.test.noinline function call...OK
All 1 tests passed.
```

`@call` allows more flexibility than normal function call syntax does. The `CallModifier` enum is reproduced here:

```
pub const CallModifier = enum {
    
    auto,

    
    
    
    
    never_tail,

    
    
    never_inline,

    
    
    no_suspend,

    
    
    always_tail,

    
    
    always_inline,

    
    
    compile_time,
};
```

### @clz

```
@clz(operand: anytype) anytype
```

`@TypeOf(operand)` must be an integer type or an integer vector type.

`operand` may be an integer or vector.

Counts the number of most-significant (leading in a big-endian sense) zeroes in an integer - "count leading zeroes".

The return type is an unsigned integer or vector of unsigned integers with the minimum number of bits that can represent the bit count of the integer type.

If `operand` is zero, `@clz` returns the bit width of integer type `T`.

See also:

- @ctz
- @popCount

### @cmpxchgStrong

```
@cmpxchgStrong(comptime T: type, ptr: *T, expected_value: T, new_value: T, success_order: AtomicOrder, fail_order: AtomicOrder) ?T
```

This function performs a strong atomic compare-and-exchange operation, returning `null` if the current value is the given expected value. It's the equivalent of this code, except atomic:

```
fn cmpxchgStrongButNotAtomic(comptime T: type, ptr: *T, expected_value: T, new_value: T) ?T {
    const old_value = ptr.*;
    if (old_value == expected_value) {
        ptr.* = new_value;
        return null;
    } else {
        return old_value;
    }
}
```

If you are using cmpxchg in a retry loop, @cmpxchgWeak is the better choice, because it can be implemented more efficiently in machine instructions.

`T` must be a pointer, a `bool`, an integer, an enum, or a packed struct.

`@typeInfo(@TypeOf(ptr)).pointer.alignment` must be `>= @sizeOf(T).`

`AtomicOrder` can be found with `@import("std").lang.AtomicOrder`.

See also:

- @atomicStore
- @atomicLoad
- @atomicRmw
- @cmpxchgWeak

### @cmpxchgWeak

```
@cmpxchgWeak(comptime T: type, ptr: *T, expected_value: T, new_value: T, success_order: AtomicOrder, fail_order: AtomicOrder) ?T
```

This function performs a weak atomic compare-and-exchange operation, returning `null` if the current value is the given expected value. It's the equivalent of this code, except atomic:

```
fn cmpxchgWeakButNotAtomic(comptime T: type, ptr: *T, expected_value: T, new_value: T) ?T {
    const old_value = ptr.*;
    if (old_value == expected_value and usuallyTrueButSometimesFalse()) {
        ptr.* = new_value;
        return null;
    } else {
        return old_value;
    }
}
```

If you are using cmpxchg in a retry loop, the sporadic failure will be no problem, and `cmpxchgWeak` is the better choice, because it can be implemented more efficiently in machine instructions. However if you need a stronger guarantee, use @cmpxchgStrong.

`T` must be a pointer, a `bool`, an integer, an enum, or a packed struct.

`@typeInfo(@TypeOf(ptr)).pointer.alignment` must be `>= @sizeOf(T).`

`AtomicOrder` can be found with `@import("std").lang.AtomicOrder`.

See also:

- @atomicStore
- @atomicLoad
- @atomicRmw
- @cmpxchgStrong

### @compileError

```
@compileError(comptime msg: []const u8) noreturn
```

This function, when semantically analyzed, causes a compile error with the message `msg`.

There are several ways that code avoids being semantically checked, such as using `if` or `switch` with compile time constants, and `comptime` functions.

### @compileLog

```
@compileLog(...) void
```

This function prints the arguments passed to it at compile-time.

To prevent accidentally leaving compile log statements in a codebase, a compilation error is added to the build, pointing to the compile log statement. This error prevents code from being generated, but does not otherwise interfere with analysis.

This function can be used to do "printf debugging" on compile-time executing code.

```
const print = @import("std").debug.print;

const num1 = blk: {
    var val1: i32 = 99;
    @compileLog("comptime val1 = ", val1);
    val1 = val1 + 1;
    break :blk val1;
};

test "main" {
    @compileLog("comptime in main");

    print("Runtime in main, num1 = {}.\n", .{num1});
}
```

```
$ zig test test_compileLog_builtin.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_compileLog_builtin.zig:5:5: error: found compile log statement
    @compileLog("comptime val1 = ", val1);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_compileLog_builtin.zig:11:5: note: also here
    @compileLog("comptime in main");
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
referenced by:
    test.main: /home/ci/work/zig-bootstrap/zig/doc/langref/test_compileLog_builtin.zig:13:46

Compile Log Output:
@as(*const [16:0]u8, "comptime val1 = "), @as(i32, 99)
@as(*const [16:0]u8, "comptime in main")
```

### @constCast

```
@constCast(value: anytype) DestType
```

Remove `const` qualifier from a pointer.

### @ctz

```
@ctz(operand: anytype) anytype
```

`@TypeOf(operand)` must be an integer type or an integer vector type.

`operand` may be an integer or vector.

Counts the number of least-significant (trailing in a big-endian sense) zeroes in an integer - "count trailing zeroes".

The return type is an unsigned integer or vector of unsigned integers with the minimum number of bits that can represent the bit count of the integer type.

If `operand` is zero, `@ctz` returns the bit width of integer type `T`.

See also:

- @clz
- @popCount

### @cVaArg

```
@cVaArg(operand: *std.lang.VaList, comptime T: type) T
```

Implements the C macro `va_arg`.

See also:

- @cVaCopy
- @cVaEnd
- @cVaStart

### @cVaCopy

```
@cVaCopy(src: *std.lang.VaList) std.lang.VaList
```

Implements the C macro `va_copy`.

See also:

- @cVaArg
- @cVaEnd
- @cVaStart

### @cVaEnd

```
@cVaEnd(src: *std.lang.VaList) void
```

Implements the C macro `va_end`.

See also:

- @cVaArg
- @cVaCopy
- @cVaStart

### @cVaStart

```
@cVaStart() std.lang.VaList
```

Implements the C macro `va_start`. Only valid inside a variadic function.

See also:

- @cVaArg
- @cVaCopy
- @cVaEnd

### @divExact

```
@divExact(numerator: T, denominator: T) T
```

Exact division. Caller guarantees `denominator != 0` and `@divTrunc(numerator, denominator) * denominator == numerator`.

- `@divExact(6, 3) == 2`
- `@divExact(a, b) * b == a`

For a function that returns a possible error code, use `@import("std").math.divExact`.

See also:

- @divTrunc
- @divFloor

### @divFloor

```
@divFloor(numerator: T, denominator: T) T
```

Floored division. Rounds toward negative infinity. For unsigned integers it is the same as `numerator / denominator`. Caller guarantees `denominator != 0` and `!(@typeInfo(T) == .int and T.is_signed and numerator == std.math.minInt(T) and denominator == -1)`.

- `@divFloor(-5, 3) == -2`
- `(@divFloor(a, b) * b) + @mod(a, b) == a`

For a function that returns a possible error code, use `@import("std").math.divFloor`.

See also:

- @divTrunc
- @divExact

### @divTrunc

```
@divTrunc(numerator: T, denominator: T) T
```

Truncated division. Rounds toward zero. For unsigned integers it is the same as `numerator / denominator`. Caller guarantees `denominator != 0` and `!(@typeInfo(T) == .int and T.is_signed and numerator == std.math.minInt(T) and denominator == -1)`.

- `@divTrunc(-5, 3) == -1`
- `(@divTrunc(a, b) * b) + @rem(a, b) == a`

For a function that returns a possible error code, use `@import("std").math.divTrunc`.

See also:

- @divFloor
- @divExact

### @embedFile

```
@embedFile(comptime path: []const u8) *const [N:0]u8
```

This function returns a compile time constant pointer to null-terminated, fixed-size array with length equal to the byte count of the file given by `path`. The contents of the array are the contents of the file. This is equivalent to a string literal with the file contents.

`path` is absolute or relative to the current file, just like `@import`.

See also:

- @import

### @enumFromInt

```
@enumFromInt(integer: anytype) anytype
```

Converts an integer into an enum value. The return type is the inferred result type.

Attempting to convert an integer with no corresponding value in the enum invokes safety-checked Illegal Behavior. Note that a non-exhaustive enum has corresponding values for all integers in the enum's integer tag type: the `_` value represents all the remaining unnamed integers in the enum's tag type.

See also:

- @intFromEnum

### @errorFromInt

```
@errorFromInt(value: @Int(.unsigned, @bitSizeOf(anyerror))) anyerror
```

Converts from the integer representation of an error into The Global Error Set type.

It is generally recommended to avoid this cast, as the integer representation of an error is not stable across source code changes.

Attempting to convert an integer that does not correspond to any error results in safety-checked Illegal Behavior.

See also:

- @intFromError

### @errorName

```
@errorName(err: anyerror) [:0]const u8
```

This function returns the string representation of an error. The string representation of `error.OutOfMem` is `"OutOfMem"`.

If there are no calls to `@errorName` in an entire application, or all calls have a compile-time known value for `err`, then no error name table will be generated.

### @errorReturnTrace

```
@errorReturnTrace() ?*std.lang.StackTrace
```

If the binary is built with error return tracing, and this function is invoked in a function that calls a function with an error or error union return type, returns a stack trace object. Otherwise returns null.

### @errorCast

```
@errorCast(value: anytype) anytype
```

Converts an error set or error union value from one error set to another error set. The return type is the inferred result type. Attempting to convert an error which is not in the destination error set results in safety-checked Illegal Behavior.

### @export

```
@export(comptime ptr: *const anyopaque, comptime options: std.lang.ExportOptions) void
```

Creates a symbol in the output object file which refers to the target of `ptr`.

`ptr` must point to a global variable or a comptime-known constant.

This builtin can be called from a comptime block to conditionally export symbols. When `ptr` points to a function with the C calling convention and `options.linkage` is `.strong`, this is equivalent to the `export` keyword used on a function:

```
comptime {
    @export(&internalName, .{ .name = "foo", .linkage = .strong });
}

fn internalName() callconv(.c) void {}
```

```
$ zig build-obj export_builtin.zig
```

This is equivalent to:

```
export fn foo() void {}
```

```
$ zig build-obj export_builtin_equivalent_code.zig
```

Note that even when using `export`, the `@"foo"` syntax for identifiers can be used to choose any string for the symbol name:

```
export fn @"A function name that is a complete sentence."() void {}
```

```
$ zig build-obj export_any_symbol_name.zig
```

When looking at the resulting object, you can see the symbol is used verbatim:

```
00000000000001f0 T A function name that is a complete sentence.
```

See also:

- Exporting a C Library

### @extern

```
@extern(T: type, comptime options: std.lang.ExternOptions) T
```

Creates a reference to an external symbol in the output object file. T must be a pointer type.

See also:

- @export

### @field

```
@field(lhs: anytype, comptime field_name: []const u8) (field)
```

Performs field access by a compile-time string. Works on both fields and declarations.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Point = struct {
    x: u32,
    y: u32,

    pub var z: u32 = 1;
};

test "field access by string" {
    var p = Point{ .x = 0, .y = 0 };

    @field(p, "x") = 4;
    @field(p, "y") = @field(p, "x") + 1;

    try expectEqual(4, @field(p, "x"));
    try expectEqual(5, @field(p, "y"));
}

test "decl access by string" {
    try expectEqual(1, @field(Point, "z"));

    @field(Point, "z") = 2;
    try expectEqual(2, @field(Point, "z"));
}
```

```
$ zig test test_field_builtin.zig
1/2 test_field_builtin.test.field access by string...OK
2/2 test_field_builtin.test.decl access by string...OK
All 2 tests passed.
```

### @fieldParentPtr

```
@fieldParentPtr(comptime field_name: []const u8, field_ptr: *T) anytype
```

Given a pointer to a struct or union field, returns a pointer to the struct or union containing that field. The return type (pointer to the parent struct or union in question) is the inferred result type.

If `field_ptr` does not point to the `field_name` field of an instance of the result type, and the result type has ill-defined layout, invokes unchecked Illegal Behavior.

### @FieldType

```
@FieldType(comptime Type: type, comptime field_name: []const u8) type
```

Given a type and the name of one of its fields, returns the type of that field.

### @floatCast

```
@floatCast(value: anytype) anytype
```

Convert from one float type to another. This cast is safe, but may cause the numeric value to lose precision. The return type is the inferred result type.

### @floatFromInt

```
@floatFromInt(int: anytype) anytype
```

Converts an integer to the closest floating point representation. The return type is the inferred result type. To convert the other way, use @round, @floor, @ceil, or @trunc. This operation is legal for all values of all integer types.

### @frameAddress

```
@frameAddress() usize
```

This function returns the base pointer of the current stack frame.

The implications of this are target-specific and not consistent across all platforms. The frame address may not be available in release mode due to aggressive optimizations.

This function is only valid within function scope.

### @hasDecl

```
@hasDecl(comptime Namespace: type, comptime name: []const u8) bool
```

Returns whether or not a Namespace has a declaration matching `name`.

```
const std = @import("std");
const expect = std.testing.expect;

const Foo = struct {
    nope: i32,

    pub var blah = "xxx";
    const hi = 1;
};

test "@hasDecl" {
    try expect(@hasDecl(Foo, "blah"));

    
    
    
    try expect(@hasDecl(Foo, "hi"));

    
    try expect(!@hasDecl(Foo, "nope"));
    try expect(!@hasDecl(Foo, "nope1234"));
}
```

```
$ zig test test_hasDecl_builtin.zig
1/1 test_hasDecl_builtin.test.@hasDecl...OK
All 1 tests passed.
```

See also:

- @hasField

### @hasField

```
@hasField(comptime T: type, comptime name: []const u8) bool
```

Returns whether the field name of a struct, union, or enum exists.

The result is a compile time constant.

It does not include functions, variables, or constants.

See also:

- @hasDecl

### @import

```
@import(comptime target: []const u8) anytype
```

Imports the file at `target`, adding it to the compilation if it is not already added. `target` is either a relative path to another file from the file containing the `@import` call, or it is the name of a module, with the import referring to the root source file of that module. Either way, the file path must end in either `.zig` (for a Zig source file) or `.zon` (for a ZON data file).

If `target` refers to a Zig source file, then `@import` returns that file's corresponding struct type, essentially as if the builtin call was replaced by `struct { FILE_CONTENTS }`. The return type is `type`.

If `target` refers to a ZON file, then `@import` returns the value of the literal in the file. If there is an inferred result type, then the return type is that type, and the ZON literal is interpreted as that type (Result Types are propagated through the ZON expression). Otherwise, the return type is the type of the equivalent Zig expression, essentially as if the builtin call was replaced by the ZON file contents.

The following modules are always available for import:

- `@import("std")` - Zig Standard Library
- `@import("builtin")` - Target-specific information. The command `zig build-exe --show-builtin` outputs the source to stdout for reference.
- `@import("root")` - Alias for the root module. In typical project structures, this means it refers back to `src/main.zig`.

See also:

- Compile Variables
- @embedFile

### @inComptime

```
@inComptime() bool
```

Returns whether the builtin was run in a `comptime` context. The result is a compile-time constant.

This can be used to provide alternative, comptime-friendly implementations of functions. It should not be used, for instance, to exclude certain functions from being evaluated at comptime.

See also:

- comptime

### @intCast

```
@intCast(int: anytype) anytype
```

Converts an integer to another integer while keeping the same numerical value. The return type is the inferred result type. Attempting to convert a number which is out of range of the destination type results in safety-checked Illegal Behavior.

```
test "integer cast panic" {
    var a: u16 = 0xabcd; 
    _ = &a;
    const b: u8 = @intCast(a);
    _ = b;
}
```

```
$ zig test test_intCast_builtin.zig
1/1 test_intCast_builtin.test.integer cast panic...thread 2235825 panic: integer does not fit in destination type
/home/ci/work/zig-bootstrap/zig/doc/langref/test_intCast_builtin.zig:4:19: 0x124d0f0 in test.integer cast panic (test_intCast_builtin.zig)
    const b: u8 = @intCast(a);
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
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/5346c4224b7b3e750f8bf7c91c7db1bd/test --seed=0xdec47623
```

To truncate the significant bits of a number out of range of the destination type, use @truncate.

If `T` is `comptime_int`, then this is semantically equivalent to Type Coercion.

### @intFromBool

```
@intFromBool(value: bool) u1
```

Converts `true` to `@as(u1, 1)` and `false` to `@as(u1, 0)`.

### @intFromEnum

```
@intFromEnum(enum_or_tagged_union: anytype) anytype
```

Converts an enumeration value into its integer tag type. When a tagged union is passed, the tag value is used as the enumeration value.

If there is only one possible enum value, the result is a `comptime_int` known at comptime.

See also:

- @enumFromInt

### @intFromError

```
@intFromError(err: anytype) @Int(.unsigned, @bitSizeOf(anyerror))
```

Supports the following types:

- The Global Error Set
- Error Set Type
- Error Union Type

Converts an error to the integer representation of an error.

It is generally recommended to avoid this cast, as the integer representation of an error is not stable across source code changes.

See also:

- @errorFromInt

### @intFromFloat

```
@intFromFloat(float: anytype) anytype
```

Deprecated. Equivalent to @trunc.

See also:

- @floatFromInt
- @round
- @floor
- @ceil
- @trunc

### @intFromPtr

```
@intFromPtr(value: anytype) usize
```

Converts `value` to a `usize` which is the address of the pointer. `value` can be `*T` or `?*T`.

To convert the other way, use @ptrFromInt

### @max

```
@max(...) T
```

Takes two or more arguments and returns the biggest value included (the maximum). This builtin accepts integers, floats, and vectors of either. In the latter case, the operation is performed element wise.
