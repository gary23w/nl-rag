---
title: "Documentation (part 8/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 8/10
---

## Illegal Behavior

Many operations in Zig trigger what is known as "Illegal Behavior" (IB). If Illegal Behavior is detected at compile-time, Zig emits a compile error and refuses to continue. Otherwise, when Illegal Behavior is not caught at compile-time, it falls into one of two categories.

Some Illegal Behavior is *safety-checked*: this means that the compiler will insert "safety checks" anywhere that the Illegal Behavior may occur at runtime, to determine whether it is about to happen. If it is, the safety check "fails", which triggers a panic.

All other Illegal Behavior is *unchecked*, meaning the compiler is unable to insert safety checks for it. If Unchecked Illegal Behavior is invoked at runtime, anything can happen: usually that will be some kind of crash, but the optimizer is free to make Unchecked Illegal Behavior do anything, such as calling arbitrary functions or clobbering arbitrary data. This is similar to the concept of "undefined behavior" in some other languages. Note that Unchecked Illegal Behavior still always results in a compile error if evaluated at comptime, because the Zig compiler is able to perform more sophisticated checks at compile-time than at runtime.

Most Illegal Behavior is safety-checked. However, to facilitate optimizations, safety checks are disabled by default in the ReleaseFast and ReleaseSmall optimization modes. Safety checks can also be enabled or disabled on a per-block basis, overriding the default for the current optimization mode, using @setRuntimeSafety. When safety checks are disabled, Safety-Checked Illegal Behavior behaves like Unchecked Illegal Behavior; that is, any behavior may result from invoking it.

When a safety check fails, Zig's default panic handler crashes with a stack trace, like this:

```
test "safety check" {
    unreachable;
}
```

```
$ zig test test_illegal_behavior.zig
1/1 test_illegal_behavior.test.safety check...thread 2237163 panic: reached unreachable code
/home/ci/work/zig-bootstrap/zig/doc/langref/test_illegal_behavior.zig:2:5: 0x124d0dc in test.safety check (test_illegal_behavior.zig)
    unreachable;
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
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/e98c515b0769bbdd47bc0c43b886948f/test --seed=0x83f06740
```

### Reaching Unreachable Code

At compile-time:

```
comptime {
    assert(false);
}
fn assert(ok: bool) void {
    if (!ok) unreachable; 
}
```

```
$ zig test test_comptime_reaching_unreachable.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_reaching_unreachable.zig:5:14: error: reached unreachable code
    if (!ok) unreachable; // assertion failure
             ^~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_reaching_unreachable.zig:2:11: note: called at comptime here
    assert(false);
    ~~~~~~^~~~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    std.debug.assert(false);
}
```

```
$ zig build-exe runtime_reaching_unreachable.zig
$ ./runtime_reaching_unreachable
thread 2237521 panic: reached unreachable code
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/debug.zig:435:14: 0x1029ea9 in assert (std.zig)
    if (!ok) unreachable; // assertion failure
             ^
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_reaching_unreachable.zig:4:21: 0x11e1d3e in main (runtime_reaching_unreachable.zig)
    std.debug.assert(false);
                    ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Index out of Bounds

At compile-time:

```
comptime {
    const array: [5]u8 = "hello".*;
    const garbage = array[5];
    _ = garbage;
}
```

```
$ zig test test_comptime_index_out_of_bounds.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_index_out_of_bounds.zig:3:27: error: index 5 outside array of length 5
    const garbage = array[5];
                          ^
```

At runtime:

```
pub fn main() void {
    const x = foo("hello");
    _ = x;
}

fn foo(x: []const u8) u8 {
    return x[5];
}
```

```
$ zig build-exe runtime_index_out_of_bounds.zig
$ ./runtime_index_out_of_bounds
thread 2237297 panic: index out of bounds: index 5, len 5
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_index_out_of_bounds.zig:7:13: 0x11e1e1e in foo (runtime_index_out_of_bounds.zig)
    return x[5];
            ^
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_index_out_of_bounds.zig:2:18: 0x11e1d4a in main (runtime_index_out_of_bounds.zig)
    const x = foo("hello");
                 ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Cast Negative Number to Unsigned Integer

At compile-time:

```
comptime {
    const value: i32 = -1;
    const unsigned: u32 = @intCast(value);
    _ = unsigned;
}
```

```
$ zig test test_comptime_invalid_cast.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_cast.zig:3:36: error: type 'u32' cannot represent integer value '-1'
    const unsigned: u32 = @intCast(value);
                                   ^~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var value: i32 = -1; 
    _ = &value;
    const unsigned: u32 = @intCast(value);
    std.debug.print("value: {}\n", .{unsigned});
}
```

```
$ zig build-exe runtime_invalid_cast.zig
$ ./runtime_invalid_cast
thread 2235389 panic: integer does not fit in destination type
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_cast.zig:6:27: 0x11e1d4f in main (runtime_invalid_cast.zig)
    const unsigned: u32 = @intCast(value);
                          ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

To obtain the maximum value of an unsigned integer, use `std.math.maxInt`.

### Cast Truncates Data

At compile-time:

```
comptime {
    const spartan_count: u16 = 300;
    const byte: u8 = @intCast(spartan_count);
    _ = byte;
}
```

```
$ zig test test_comptime_invalid_cast_truncate.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_cast_truncate.zig:3:31: error: type 'u8' cannot represent integer value '300'
    const byte: u8 = @intCast(spartan_count);
                              ^~~~~~~~~~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var spartan_count: u16 = 300; 
    _ = &spartan_count;
    const byte: u8 = @intCast(spartan_count);
    std.debug.print("value: {}\n", .{byte});
}
```

```
$ zig build-exe runtime_invalid_cast_truncate.zig
$ ./runtime_invalid_cast_truncate
thread 2238803 panic: integer does not fit in destination type
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_cast_truncate.zig:6:22: 0x11e1d50 in main (runtime_invalid_cast_truncate.zig)
    const byte: u8 = @intCast(spartan_count);
                     ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

To truncate bits, use @truncate.

### Integer Overflow

#### Default Operations

The following operators can cause integer overflow:

- `+` (addition)
- `-` (subtraction)
- `-` (negation)
- `*` (multiplication)
- `/` (division)
- @divTrunc (division)
- @divFloor (division)
- @divExact (division)

Example with addition at compile-time:

```
comptime {
    var byte: u8 = 255;
    byte += 1;
}
```

```
$ zig test test_comptime_overflow.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_overflow.zig:3:10: error: overflow of integer type 'u8' with value '256'
    byte += 1;
    ~~~~~^~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var byte: u8 = 255;
    byte += 1;
    std.debug.print("value: {}\n", .{byte});
}
```

```
$ zig build-exe runtime_overflow.zig
$ ./runtime_overflow
thread 2235111 panic: integer overflow
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_overflow.zig:5:10: 0x11e1d65 in main (runtime_overflow.zig)
    byte += 1;
         ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

#### Standard Library Math Functions

These functions provided by the standard library return possible errors.

- `@import("std").math.add`
- `@import("std").math.sub`
- `@import("std").math.mul`
- `@import("std").math.divTrunc`
- `@import("std").math.divFloor`
- `@import("std").math.divExact`
- `@import("std").math.shl`

Example of catching an overflow for addition:

```
const math = @import("std").math;
const print = @import("std").debug.print;
pub fn main() !void {
    var byte: u8 = 255;

    byte = if (math.add(u8, byte, 1)) |result| result else |err| {
        print("unable to add one: {s}\n", .{@errorName(err)});
        return err;
    };

    print("result: {}\n", .{byte});
}
```

```
$ zig build-exe math_add.zig
$ ./math_add
unable to add one: Overflow
error: Overflow
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/math.zig:571:21: 0x11463c4 in add__anon_22097 (std.zig)
    if (ov[1] != 0) return error.Overflow;
                    ^
/home/ci/work/zig-bootstrap/zig/doc/langref/math_add.zig:8:9: 0x11e114f in main (math_add.zig)
        return err;
        ^
```

#### Builtin Overflow Functions

These builtins return a tuple containing whether there was an overflow (as a `u1`) and the possibly overflowed bits of the operation:

- @addWithOverflow
- @subWithOverflow
- @mulWithOverflow
- @shlWithOverflow

Example of @addWithOverflow:

```
const print = @import("std").debug.print;
pub fn main() void {
    const byte: u8 = 255;

    const ov = @addWithOverflow(byte, 10);
    if (ov[1] != 0) {
        print("overflowed result: {}\n", .{ov[0]});
    } else {
        print("result: {}\n", .{ov[0]});
    }
}
```

```
$ zig build-exe addWithOverflow_builtin.zig
$ ./addWithOverflow_builtin
overflowed result: 9
```

#### Wrapping Operations

These operations have guaranteed wraparound semantics.

- `+%` (wraparound addition)
- `-%` (wraparound subtraction)
- `-%` (wraparound negation)
- `*%` (wraparound multiplication)

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;
const minInt = std.math.minInt;
const maxInt = std.math.maxInt;

test "wraparound addition and subtraction" {
    const x: i32 = maxInt(i32);
    const min_val = x +% 1;
    try expectEqual(minInt(i32), min_val);
    const max_val = min_val -% 1;
    try expectEqual(maxInt(i32), max_val);
}
```

```
$ zig test test_wraparound_semantics.zig
1/1 test_wraparound_semantics.test.wraparound addition and subtraction...OK
All 1 tests passed.
```

### Exact Left Shift Overflow

At compile-time:

```
comptime {
    const x = @shlExact(@as(u8, 0b01010101), 2);
    _ = x;
}
```

```
$ zig test test_comptime_shlExact_overflow.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_shlExact_overflow.zig:2:15: error: overflow of integer type 'u8' with value '340'
    const x = @shlExact(@as(u8, 0b01010101), 2);
              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var x: u8 = 0b01010101; 
    _ = &x;
    const y = @shlExact(x, 2);
    std.debug.print("value: {}\n", .{y});
}
```

```
$ zig build-exe runtime_shlExact_overflow.zig
$ ./runtime_shlExact_overflow
thread 2237408 panic: left shift overflowed bits
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_shlExact_overflow.zig:6:5: 0x11e1d71 in main (runtime_shlExact_overflow.zig)
    const y = @shlExact(x, 2);
    ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Exact Right Shift Overflow

At compile-time:

```
comptime {
    const x = @shrExact(@as(u8, 0b10101010), 2);
    _ = x;
}
```

```
$ zig test test_comptime_shrExact_overflow.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_shrExact_overflow.zig:2:15: error: exact shift shifted out 1 bits
    const x = @shrExact(@as(u8, 0b10101010), 2);
              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

At runtime:

```
const builtin = @import("builtin");
const std = @import("std");

pub fn main() void {
    var x: u8 = 0b10101010; 
    _ = &x;
    const y = @shrExact(x, 2);
    std.debug.print("value: {}\n", .{y});

    if ((builtin.cpu.arch.isPowerPC() or builtin.cpu.arch.isRISCV() or builtin.cpu.arch.isLoongArch() or builtin.cpu.arch == .s390x) and builtin.zig_backend == .stage2_llvm) @panic("https://github.com/ziglang/zig/issues/24304");
}
```

```
$ zig build-exe runtime_shrExact_overflow.zig
$ ./runtime_shrExact_overflow
thread 2235342 panic: right shift overflowed bits
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_shrExact_overflow.zig:7:5: 0x11e1d5a in main (runtime_shrExact_overflow.zig)
    const y = @shrExact(x, 2);
    ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Division by Zero

At compile-time:

```
comptime {
    const a: i32 = 1;
    const b: i32 = 0;
    const c = a / b;
    _ = c;
}
```

```
$ zig test test_comptime_division_by_zero.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_division_by_zero.zig:4:19: error: division by zero here causes illegal behavior
    const c = a / b;
                  ^
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var a: u32 = 1;
    var b: u32 = 0;
    _ = .{ &a, &b };
    const c = a / b;
    std.debug.print("value: {}\n", .{c});
}
```

```
$ zig build-exe runtime_division_by_zero.zig
$ ./runtime_division_by_zero
thread 2236198 panic: division by zero
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_division_by_zero.zig:7:17: 0x11e1d60 in main (runtime_division_by_zero.zig)
    const c = a / b;
                ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Remainder Division by Zero

At compile-time:

```
comptime {
    const a: i32 = 10;
    const b: i32 = 0;
    const c = a % b;
    _ = c;
}
```

```
$ zig test test_comptime_remainder_division_by_zero.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_remainder_division_by_zero.zig:4:19: error: division by zero here causes illegal behavior
    const c = a % b;
                  ^
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var a: u32 = 10;
    var b: u32 = 0;
    _ = .{ &a, &b };
    const c = a % b;
    std.debug.print("value: {}\n", .{c});
}
```

```
$ zig build-exe runtime_remainder_division_by_zero.zig
$ ./runtime_remainder_division_by_zero
thread 2235511 panic: division by zero
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_remainder_division_by_zero.zig:7:17: 0x11e1d60 in main (runtime_remainder_division_by_zero.zig)
    const c = a % b;
                ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Exact Division Remainder

At compile-time:

```
comptime {
    const a: u32 = 10;
    const b: u32 = 3;
    const c = @divExact(a, b);
    _ = c;
}
```

```
$ zig test test_comptime_divExact_remainder.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_divExact_remainder.zig:4:15: error: exact division produced remainder
    const c = @divExact(a, b);
              ^~~~~~~~~~~~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var a: u32 = 10;
    var b: u32 = 3;
    _ = .{ &a, &b };
    const c = @divExact(a, b);
    std.debug.print("value: {}\n", .{c});
}
```

```
$ zig build-exe runtime_divExact_remainder.zig
$ ./runtime_divExact_remainder
thread 2236091 panic: exact division produced remainder
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_divExact_remainder.zig:7:15: 0x11e1d95 in main (runtime_divExact_remainder.zig)
    const c = @divExact(a, b);
              ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Attempt to Unwrap Null

At compile-time:

```
comptime {
    const optional_number: ?i32 = null;
    const number = optional_number.?;
    _ = number;
}
```

```
$ zig test test_comptime_unwrap_null.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_unwrap_null.zig:3:35: error: unable to unwrap null
    const number = optional_number.?;
                   ~~~~~~~~~~~~~~~^~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    var optional_number: ?i32 = null;
    _ = &optional_number;
    const number = optional_number.?;
    std.debug.print("value: {}\n", .{number});
}
```

```
$ zig build-exe runtime_unwrap_null.zig
$ ./runtime_unwrap_null
thread 2238908 panic: attempt to use null value
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_unwrap_null.zig:6:35: 0x11e1d64 in main (runtime_unwrap_null.zig)
    const number = optional_number.?;
                                  ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

One way to avoid this crash is to test for null instead of assuming non-null, with the `if` expression:

```
const print = @import("std").debug.print;
pub fn main() void {
    const optional_number: ?i32 = null;

    if (optional_number) |number| {
        print("got number: {}\n", .{number});
    } else {
        print("it's null\n", .{});
    }
}
```

```
$ zig build-exe testing_null_with_if.zig
$ ./testing_null_with_if
it's null
```

See also:

- Optionals

### Attempt to Unwrap Error

At compile-time:

```
comptime {
    const number = getNumberOrFail() catch unreachable;
    _ = number;
}

fn getNumberOrFail() !i32 {
    return error.UnableToReturnNumber;
}
```

```
$ zig test test_comptime_unwrap_error.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_unwrap_error.zig:2:44: error: caught unexpected error 'UnableToReturnNumber'
    const number = getNumberOrFail() catch unreachable;
                                           ^~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_unwrap_error.zig:7:18: note: error returned here
    return error.UnableToReturnNumber;
                 ^~~~~~~~~~~~~~~~~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    const number = getNumberOrFail() catch unreachable;
    std.debug.print("value: {}\n", .{number});
}

fn getNumberOrFail() !i32 {
    return error.UnableToReturnNumber;
}
```

```
$ zig build-exe runtime_unwrap_error.zig
$ ./runtime_unwrap_error
thread 2237160 panic: attempt to unwrap error: UnableToReturnNumber
error return context:
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_unwrap_error.zig:9:5: 0x11e1d3c in getNumberOrFail (runtime_unwrap_error.zig)
    return error.UnableToReturnNumber;
    ^

stack trace:
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_unwrap_error.zig:4:44: 0x11e1da3 in main (runtime_unwrap_error.zig)
    const number = getNumberOrFail() catch unreachable;
                                           ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

One way to avoid this crash is to test for an error instead of assuming a successful result, with the `if` expression:

```
const print = @import("std").debug.print;

pub fn main() void {
    const result = getNumberOrFail();

    if (result) |number| {
        print("got number: {}\n", .{number});
    } else |err| {
        print("got error: {s}\n", .{@errorName(err)});
    }
}

fn getNumberOrFail() !i32 {
    return error.UnableToReturnNumber;
}
```

```
$ zig build-exe testing_error_with_if.zig
$ ./testing_error_with_if
got error: UnableToReturnNumber
```

See also:

- Errors

### Invalid Error Code

At compile-time:

```
comptime {
    _ = @errorFromInt(12345);
}
```

```
$ zig test test_comptime_invalid_error_code.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_error_code.zig:2:23: error: integer value '12345' represents no error
    _ = @errorFromInt(12345);
                      ^~~~~
```

At runtime:

```
const std = @import("std");

pub fn main() void {
    const err = error.AnError;
    var number = @intFromError(err) + 500;
    _ = &number;
    const invalid_err = @errorFromInt(number);
    std.debug.print("value: {}\n", .{invalid_err});
}
```

```
$ zig build-exe runtime_invalid_error_code.zig
$ ./runtime_invalid_error_code
thread 2238366 panic: invalid error code
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_error_code.zig:7:5: 0x11e1d75 in main (runtime_invalid_error_code.zig)
    const invalid_err = @errorFromInt(number);
    ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Invalid Enum Cast

At compile-time:

```
const Foo = enum {
    a,
    b,
    c,
};
comptime {
    const a: u2 = 3;
    const b: Foo = @enumFromInt(a);
    _ = b;
}
```

```
$ zig test test_comptime_invalid_enum_cast.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_enum_cast.zig:8:20: error: enum 'test_comptime_invalid_enum_cast.Foo' has no tag with value '3'
    const b: Foo = @enumFromInt(a);
                   ^~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_enum_cast.zig:1:13: note: enum declared here
const Foo = enum {
            ^~~~
```

At runtime:

```
const std = @import("std");

const Foo = enum {
    a,
    b,
    c,
};

pub fn main() void {
    var a: u2 = 3;
    _ = &a;
    const b: Foo = @enumFromInt(a);
    std.debug.print("value: {s}\n", .{@tagName(b)});
}
```

```
$ zig build-exe runtime_invalid_enum_cast.zig
$ ./runtime_invalid_enum_cast
thread 2237519 panic: invalid enum value
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_enum_cast.zig:12:20: 0x11e1dc0 in main (runtime_invalid_enum_cast.zig)
    const b: Foo = @enumFromInt(a);
                   ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Invalid Error Set Cast

At compile-time:

```
const Set1 = error{
    A,
    B,
};
const Set2 = error{
    A,
    C,
};
comptime {
    _ = @as(Set2, @errorCast(Set1.B));
}
```

```
$ zig test test_comptime_invalid_error_set_cast.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_error_set_cast.zig:10:19: error: 'error.B' not a member of error set 'error{A,C}'
    _ = @as(Set2, @errorCast(Set1.B));
                  ^~~~~~~~~~~~~~~~~~
```

At runtime:

```
const std = @import("std");

const Set1 = error{
    A,
    B,
};
const Set2 = error{
    A,
    C,
};
pub fn main() void {
    foo(Set1.B);
}
fn foo(set1: Set1) void {
    const x: Set2 = @errorCast(set1);
    std.debug.print("value: {}\n", .{x});
}
```

```
$ zig build-exe runtime_invalid_error_set_cast.zig
$ ./runtime_invalid_error_set_cast
thread 2237021 panic: invalid error code
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_error_set_cast.zig:15:21: 0x11e1e3c in foo (runtime_invalid_error_set_cast.zig)
    const x: Set2 = @errorCast(set1);
                    ^
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_error_set_cast.zig:12:8: 0x11e1d47 in main (runtime_invalid_error_set_cast.zig)
    foo(Set1.B);
       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Incorrect Pointer Alignment

At compile-time:

```
comptime {
    const ptr: *align(1) i32 = @ptrFromInt(0x1);
    const aligned: *align(4) i32 = @alignCast(ptr);
    _ = aligned;
}
```

```
$ zig test test_comptime_incorrect_pointer_alignment.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_incorrect_pointer_alignment.zig:3:47: error: pointer address 0x1 is not aligned to 4 bytes
    const aligned: *align(4) i32 = @alignCast(ptr);
                                              ^~~
```

At runtime:

```
const mem = @import("std").mem;
pub fn main() !void {
    var array align(4) = [_]u32{ 0x11111111, 0x11111111 };
    const bytes = mem.sliceAsBytes(array[0..]);
    if (foo(bytes) != 0x11111111) return error.Wrong;
}
fn foo(bytes: []u8) u32 {
    const slice4 = bytes[1..5];
    const int_slice = mem.bytesAsSlice(u32, @as([]align(4) u8, @alignCast(slice4)));
    return int_slice[0];
}
```

```
$ zig build-exe runtime_incorrect_pointer_alignment.zig
$ ./runtime_incorrect_pointer_alignment
thread 2238800 panic: incorrect alignment
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_incorrect_pointer_alignment.zig:9:64: 0x11e2716 in foo (runtime_incorrect_pointer_alignment.zig)
    const int_slice = mem.bytesAsSlice(u32, @as([]align(4) u8, @alignCast(slice4)));
                                                               ^
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_incorrect_pointer_alignment.zig:5:12: 0x11e10ee in main (runtime_incorrect_pointer_alignment.zig)
    if (foo(bytes) != 0x11111111) return error.Wrong;
           ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e1716 in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Wrong Union Field Access

At compile-time:

```
comptime {
    var f = Foo{ .int = 42 };
    f.float = 12.34;
}

const Foo = union {
    float: f32,
    int: u32,
};
```

```
$ zig test test_comptime_wrong_union_field_access.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_wrong_union_field_access.zig:3:6: error: access of union field 'float' while field 'int' is active
    f.float = 12.34;
    ~^~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_wrong_union_field_access.zig:6:13: note: union declared here
const Foo = union {
            ^~~~~
```

At runtime:

```
const std = @import("std");

const Foo = union {
    float: f32,
    int: u32,
};

pub fn main() void {
    var f = Foo{ .int = 42 };
    bar(&f);
}

fn bar(f: *Foo) void {
    f.float = 12.34;
    std.debug.print("value: {}\n", .{f.float});
}
```

```
$ zig build-exe runtime_wrong_union_field_access.zig
$ ./runtime_wrong_union_field_access
thread 2235512 panic: access of union field 'float' while field 'int' is active
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_wrong_union_field_access.zig:14:6: 0x11e1e0e in bar (runtime_wrong_union_field_access.zig)
    f.float = 12.34;
     ^
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_wrong_union_field_access.zig:10:8: 0x11e1d4e in main (runtime_wrong_union_field_access.zig)
    bar(&f);
       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

This safety is not available for `extern` or `packed` unions.

To change the active field of a union, assign the entire union, like this:

```
const std = @import("std");

const Foo = union {
    float: f32,
    int: u32,
};

pub fn main() void {
    var f = Foo{ .int = 42 };
    bar(&f);
}

fn bar(f: *Foo) void {
    f.* = Foo{ .float = 12.34 };
    std.debug.print("value: {}\n", .{f.float});
}
```

```
$ zig build-exe change_active_union_field.zig
$ ./change_active_union_field
value: 12.34
```

To change the active field of a union when a meaningful value for the field is not known, use undefined, like this:

```
const std = @import("std");

const Foo = union {
    float: f32,
    int: u32,
};

pub fn main() void {
    var f = Foo{ .int = 42 };
    f = Foo{ .float = undefined };
    bar(&f);
    std.debug.print("value: {}\n", .{f.float});
}

fn bar(f: *Foo) void {
    f.float = 12.34;
}
```

```
$ zig build-exe undefined_active_union_field.zig
$ ./undefined_active_union_field
value: 12.34
```

See also:

- union
- extern union

### Out of Bounds Float to Integer Cast

This happens when casting a float to an integer where the float has a value outside the integer type's range.

At compile-time:

```
comptime {
    const float: f32 = 4294967296;
    const int: i32 = @intFromFloat(float);
    _ = int;
}
```

```
$ zig test test_comptime_out_of_bounds_float_to_integer_cast.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_out_of_bounds_float_to_integer_cast.zig:3:36: error: float value '4294967296' cannot be stored in integer type 'i32'
    const int: i32 = @intFromFloat(float);
                                   ^~~~~
```

At runtime:

```
pub fn main() void {
    var float: f32 = 4294967296; 
    _ = &float;
    const int: i32 = @intFromFloat(float);
    _ = int;
}
```

```
$ zig build-exe runtime_out_of_bounds_float_to_integer_cast.zig
$ ./runtime_out_of_bounds_float_to_integer_cast
thread 2238159 panic: integer part of floating point value out of bounds
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_out_of_bounds_float_to_integer_cast.zig:4:22: 0x11e1d7e in main (runtime_out_of_bounds_float_to_integer_cast.zig)
    const int: i32 = @intFromFloat(float);
                     ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```

### Pointer Cast Invalid Null

This happens when casting a pointer with the address 0 to a pointer which may not have the address 0. For example, C Pointers, Optional Pointers, and allowzero pointers allow address zero, but normal Pointers do not.

At compile-time:

```
comptime {
    const opt_ptr: ?*i32 = null;
    const ptr: *i32 = @ptrCast(opt_ptr);
    _ = ptr;
}
```

```
$ zig test test_comptime_invalid_null_pointer_cast.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_invalid_null_pointer_cast.zig:3:32: error: null pointer casted to type '*i32'
    const ptr: *i32 = @ptrCast(opt_ptr);
                               ^~~~~~~
```

At runtime:

```
pub fn main() void {
    var opt_ptr: ?*i32 = null;
    _ = &opt_ptr;
    const ptr: *i32 = @ptrCast(opt_ptr);
    _ = ptr;
}
```

```
$ zig build-exe runtime_invalid_null_pointer_cast.zig
$ ./runtime_invalid_null_pointer_cast
thread 2235949 panic: cast causes pointer to be null
/home/ci/work/zig-bootstrap/zig/doc/langref/runtime_invalid_null_pointer_cast.zig:4:23: 0x11e1d5a in main (runtime_invalid_null_pointer_cast.zig)
    const ptr: *i32 = @ptrCast(opt_ptr);
                      ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64: 0x11e166b in callMain (std.zig)
    if (fn_info.param_types.len == 0) return wrapMain(root.main());
                                                               ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:217:5: 0x11e1091 in _start (std.zig)
    asm volatile (switch (native_arch) {
    ^
(process terminated by signal)
```


## Memory

The Zig language performs no memory management on behalf of the programmer. This is why Zig has no runtime, and why Zig code works seamlessly in so many environments, including real-time software, operating system kernels, embedded devices, and low latency servers. As a consequence, Zig programmers must always be able to answer the question:

Where are the bytes?

Like Zig, the C programming language has manual memory management. However, unlike Zig, C has a default allocator - `malloc`, `realloc`, and `free`. When linking against libc, Zig exposes this allocator with `std.heap.c_allocator`. However, by convention, there is no default allocator in Zig. Instead, functions which need to allocate accept an `Allocator` parameter. Likewise, some data structures accept an `Allocator` parameter in their initialization functions:

```
const std = @import("std");
const Allocator = std.mem.Allocator;
const expectEqualStrings = std.testing.expectEqualStrings;

test "using an allocator" {
    var buffer: [100]u8 = undefined;
    var fba = std.heap.FixedBufferAllocator.init(&buffer);
    const allocator = fba.allocator();
    const result = try concat(allocator, "foo", "bar");
    try expectEqualStrings("foobar", result);
}

fn concat(allocator: Allocator, a: []const u8, b: []const u8) ![]u8 {
    const result = try allocator.alloc(u8, a.len + b.len);
    @memcpy(result[0..a.len], a);
    @memcpy(result[a.len..], b);
    return result;
}
```

```
$ zig test test_allocator.zig
1/1 test_allocator.test.using an allocator...OK
All 1 tests passed.
```

In the above example, 100 bytes of stack memory are used to initialize a `FixedBufferAllocator`, which is then passed to a function. As a convenience there is a global `FixedBufferAllocator` available for quick tests at `std.testing.allocator`, which will also perform basic leak detection.

Zig has a general purpose allocator available to be imported with `std.heap.DebugAllocator`. However, it is still recommended to follow the Choosing an Allocator guide.

### Choosing an Allocator

What allocator to use depends on a number of factors. Here is a flow chart to help you decide:

1. Are you making a library? In this case, best to accept an `Allocator` as a parameter and allow your library's users to decide what allocator to use.
2. Are you linking libc? In this case, `std.heap.c_allocator` is likely the right choice, at least for your main allocator.
3. Is the maximum number of bytes that you will need bounded by a number known at comptime? In this case, use `std.heap.FixedBufferAllocator`.
4. Is your program a command line application which runs from start to end without any fundamental cyclical pattern (such as a video game main loop, or a web server request handler), such that it would make sense to free everything at once at the end? In this case, it is recommended to follow this pattern: `const std = @import("std"); pub fn main() !void { var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); defer arena.deinit(); const allocator = arena.allocator(); const ptr = try allocator.create(i32); std.debug.print("ptr={*}\n", .{ptr}); }`$ zig build-exe cli_allocation.zig $ ./cli_allocation ptr=i32@7fe6ea2bc018 When using this kind of allocator, there is no need to free anything manually. Everything gets freed at once with the call to `arena.deinit()`.
5. Are the allocations part of a cyclical pattern such as a video game main loop, or a web server request handler? If the allocations can all be freed at once, at the end of the cycle, for example once the video game frame has been fully rendered, or the web server request has been served, then `std.heap.ArenaAllocator` is a great candidate. As demonstrated in the previous bullet point, this allows you to free entire arenas at once. Note also that if an upper bound of memory can be established, then `std.heap.FixedBufferAllocator` can be used as a further optimization.
6. Are you writing a test, and you want to make sure `error.OutOfMemory` is handled correctly? In this case, use `std.testing.FailingAllocator`.
7. Are you writing a test? In this case, use `std.testing.allocator`.
8. Finally, if none of the above apply, you need a general purpose allocator. If you are in Debug mode, `std.heap.DebugAllocator` is available as a function that takes a comptime struct of configuration options and returns a type. Generally, you will set up exactly one in your main function, and then pass it or sub-allocators around to various parts of your application.
9. If you are compiling in ReleaseFast mode, `std.heap.smp_allocator` is a solid choice for a general purpose allocator.
10. You can also consider implementing an allocator.

### Where are the bytes?

String literals such as `"hello"` are in the global constant data section. This is why it is an error to pass a string literal to a mutable slice, like this:

```
fn foo(s: []u8) void {
    _ = s;
}

test "string literal to mutable slice" {
    foo("hello");
}
```

```
$ zig test test_string_literal_to_slice.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_string_literal_to_slice.zig:6:9: error: expected type '[]u8', found '*const [5:0]u8'
    foo("hello");
        ^~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_string_literal_to_slice.zig:6:9: note: cast discards const qualifier
/home/ci/work/zig-bootstrap/zig/doc/langref/test_string_literal_to_slice.zig:1:11: note: parameter type declared here
fn foo(s: []u8) void {
          ^~~~
```

However if you make the slice constant, then it works:

```
fn foo(s: []const u8) void {
    _ = s;
}

test "string literal to constant slice" {
    foo("hello");
}
```

```
$ zig test test_string_literal_to_const_slice.zig
1/1 test_string_literal_to_const_slice.test.string literal to constant slice...OK
All 1 tests passed.
```

Just like string literals, `const` declarations, when the value is known at comptime, are stored in the global constant data section. Also Compile Time Variables are stored in the global constant data section.

`var` declarations inside functions are stored in the function's stack frame. Once a function returns, any Pointers to variables in the function's stack frame become invalid references, and dereferencing them becomes unchecked Illegal Behavior.

`var` declarations at the top level or in struct declarations are stored in the global data section.

The location of memory allocated with `allocator.alloc` or `allocator.create` is determined by the allocator's implementation.

TODO: thread local variables

### Heap Allocation Failure

Many programming languages choose to handle the possibility of heap allocation failure by unconditionally crashing. By convention, Zig programmers do not consider this to be a satisfactory solution. Instead, `error.OutOfMemory` represents heap allocation failure, and Zig libraries return this error code whenever heap allocation failure prevented an operation from completing successfully.

Some have argued that because some operating systems such as Linux have memory overcommit enabled by default, it is pointless to handle heap allocation failure. There are many problems with this reasoning:

- Only some operating systems have an overcommit feature.
  - Linux has it enabled by default, but it is configurable.
  - Windows does not overcommit.
  - Embedded systems do not have overcommit.
  - Hobby operating systems may or may not have overcommit.
- For real-time systems, not only is there no overcommit, but typically the maximum amount of memory per application is determined ahead of time.
- When writing a library, one of the main goals is code reuse. By making code handle allocation failure correctly, a library becomes eligible to be reused in more contexts.
- Although some software has grown to depend on overcommit being enabled, its existence is the source of countless user experience disasters. When a system with overcommit enabled, such as Linux on default settings, comes close to memory exhaustion, the system locks up and becomes unusable. At this point, the OOM Killer selects an application to kill based on heuristics. This non-deterministic decision often results in an important process being killed, and often fails to return the system back to working order.

### Recursion

Recursion is a fundamental tool in modeling software. However it has an often-overlooked problem: unbounded memory allocation.

Recursion is an area of active experimentation in Zig and so the documentation here is not final. You can read a summary of recursion status in the 0.3.0 release notes.

The short summary is that currently recursion works normally as you would expect. Although Zig code is not yet protected from stack overflow, it is planned that a future version of Zig will provide such protection, with some degree of cooperation from Zig code required.

### Lifetime and Ownership

It is the Zig programmer's responsibility to ensure that a pointer is not accessed when the memory pointed to is no longer available. Note that a slice is a form of pointer, in that it references other memory.

In order to prevent bugs, there are some helpful conventions to follow when dealing with pointers. In general, when a function returns a pointer, the documentation for the function should explain who "owns" the pointer. This concept helps the programmer decide when it is appropriate, if ever, to free the pointer.

For example, the function's documentation may say "caller owns the returned memory", in which case the code that calls the function must have a plan for when to free that memory. Probably in this situation, the function will accept an `Allocator` parameter.

Sometimes the lifetime of a pointer may be more complicated. For example, the `std.ArrayList(T).items` slice has a lifetime that remains valid until the next time the list is resized, such as by appending new elements.

The API documentation for functions and data structures should take great care to explain the ownership and lifetime semantics of pointers. Ownership determines whose responsibility it is to free the memory referenced by the pointer, and lifetime determines the point at which the memory becomes inaccessible (lest Illegal Behavior occur).
