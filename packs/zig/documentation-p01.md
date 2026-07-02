---
title: "Documentation (part 1/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 1/10
---

## Introduction

Zig is a general-purpose programming language and toolchain for maintaining **robust**, **optimal**, and **reusable** software.

**Robust**

Behavior is correct even for edge cases such as out of memory.

**Optimal**

Write programs the best way they can behave and perform.

**Reusable**

The same code works in many environments which have different constraints.

**Maintainable**

Precisely communicate intent to the compiler and other programmers. The language imposes a low overhead to reading code and is resilient to changing requirements and environments.

Often the most efficient way to learn something new is to see examples, so this documentation shows how to use each of Zig's features. It is all on one page so you can search with your browser's search tool.

The code samples in this document are compiled and tested as part of the main test suite of Zig.

This HTML document depends on no external files, so you can use it offline.


## Zig Standard Library

The Zig Standard Library has its own documentation.

Zig's Standard Library contains commonly used algorithms, data structures, and definitions to help you build programs or libraries. You will see many examples of Zig's Standard Library used in this documentation. To learn more about the Zig Standard Library, visit the link above.

Alternatively, the Zig Standard Library documentation is provided with each Zig distribution. It can be rendered via a local webserver with:

```
zig std
```


## Hello World

```
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    try std.Io.File.stdout().writeStreamingAll(init.io, "Hello, World!\n");
}
```

```
$ zig build-exe hello.zig
$ ./hello
Hello, World!
```

Most of the time, it is more appropriate to write to stderr rather than stdout, and whether or not the message is successfully written to the stream is irrelevant. Also, formatted printing often comes in handy. For this common case, there is a simpler API:

```
const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, {s}!\n", .{"World"});
}
```

```
$ zig build-exe hello_again.zig
$ ./hello_again
Hello, World!
```

In this case, the `!` may be omitted from the return type of `main` because no errors are returned from the function.

See also:

- Values
- Tuples
- @import
- Errors
- Entry Point
- Source Encoding
- try

There are three types of comments. Normal comments are ignored, while Doc Comments and Top-Level Doc Comments are used by the compiler to generate the package documentation.

```
const print = @import("std").debug.print;

pub fn main() void {
    
    

    

    print("Hello, world!\n", .{}); 
}
```

```
$ zig build-exe comments.zig
$ ./comments
Hello, world!
```

There are no multiline comments. Zig has the property that each line of code can be tokenized independently.

A doc comment is one that begins with exactly three slashes (i.e. but not ); multiple doc comments in a row are merged together to form a multiline doc comment. The doc comment documents whatever immediately follows it.

```
const Timestamp = struct {
    
    seconds: i64, 
    
    nanos: u32,

    
    
    pub fn unixEpoch() Timestamp {
        return Timestamp{
            .seconds = 0,
            .nanos = 0,
        };
    }
};
```

Doc comments are only allowed in certain places; it is a compile error to have a doc comment in an unexpected place, such as in the middle of an expression, or just before a non-doc comment.

```
const std = @import("std");
```

```
$ zig build-obj invalid_doc-comment.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/invalid_doc-comment.zig:1:16: error: expected type expression, found 'a document comment'
/// doc-comment
               ^
```

```
pub fn main() void {}
```

```
$ zig build-obj unattached_doc-comment.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/unattached_doc-comment.zig:3:1: error: unattached documentation comment
/// End of file
^~~~~~~~~~~~~~~
```

Doc comments can be interleaved with normal comments, which are ignored.

A top-level doc comment is one that begins with two slashes and an exclamation point: ; it documents the type which owns the containing Namespace.

It is a compile error if a top-level doc comment is not placed at the start of a namespace, before any expressions.

```
const S = struct {
    
    
    
};
```


## Namespace

A namespace in Zig is created by struct, enum, union, and opaque.

They contain Namespace Level Variables, function declarations, and comptime blocks.

Although namespaces use curly braces to surround their definition, they should not be confused with blocks or function bodies.

**Every Zig source file is implicitly a struct**, with the keyword `struct` and curly braces omitted.


## Identifiers

Identifiers must start with an alphabetic character or underscore and may be followed by any number of alphanumeric characters or underscores. They must not overlap with any keywords. See Keyword Reference.

### String Identifier Syntax

If a name that does not fit these requirements is needed, such as for linking with external libraries, the `@""` syntax may be used.

```
const @"identifier with spaces in it" = 0xff;
const @"1SmallStep4Man" = 112358;

const c = @import("std").c;
pub extern "c" fn @"error"() void;
pub extern "c" fn @"fstat$INODE64"(fd: c.fd_t, buf: *c.Stat) c_int;

const Color = enum {
    red,
    @"really red",
};
const color: Color = .@"really red";
```


## Values

```
const print = std.debug.print;
const std = @import("std");
const os = std.os;
const assert = std.debug.assert;

const ExampleErrorSet = error{
    ExampleErrorVariant,
};

pub fn main() void {
    
    const one_plus_one: i32 = 1 + 1;
    print("1 + 1 = {}\n", .{one_plus_one});

    
    const seven_div_three: f32 = 7.0 / 3.0;
    print("7.0 / 3.0 = {}\n", .{seven_div_three});

    
    print("{}\n{}\n{}\n", .{
        true and false,
        true or false,
        !true,
    });

    
    var optional_value: ?[]const u8 = null;
    assert(optional_value == null);

    print("\noptional 1\ntype: {}\nvalue: {?s}\n", .{
        @TypeOf(optional_value), optional_value,
    });

    optional_value = "hi";
    assert(optional_value != null);

    print("\noptional 2\ntype: {}\nvalue: {?s}\n", .{
        @TypeOf(optional_value), optional_value,
    });

    
    var number_or_error: ExampleErrorSet!i32 = ExampleErrorSet.ExampleErrorVariant;

    print("\nerror union 1\ntype: {}\nvalue: {!}\n", .{
        @TypeOf(number_or_error),
        number_or_error,
    });

    number_or_error = 1234;

    print("\nerror union 2\ntype: {}\nvalue: {!}\n", .{
        @TypeOf(number_or_error), number_or_error,
    });
}
```

```
$ zig build-exe values.zig
$ ./values
1 + 1 = 2
7.0 / 3.0 = 2.3333333
false
true
false

optional 1
type: ?[]const u8
value: null

optional 2
type: ?[]const u8
value: hi

error union 1
type: error{ExampleErrorVariant}!i32
value: error.ExampleErrorVariant

error union 2
type: error{ExampleErrorVariant}!i32
value: 1234
```

### Primitive Types

| Type | C Equivalent | Description |
|---|---|---|
| `i8` | `int8_t` | signed 8-bit integer |
| `u8` | `uint8_t` | unsigned 8-bit integer |
| `i16` | `int16_t` | signed 16-bit integer |
| `u16` | `uint16_t` | unsigned 16-bit integer |
| `i32` | `int32_t` | signed 32-bit integer |
| `u32` | `uint32_t` | unsigned 32-bit integer |
| `i64` | `int64_t` | signed 64-bit integer |
| `u64` | `uint64_t` | unsigned 64-bit integer |
| `i128` | `__int128` | signed 128-bit integer |
| `u128` | `unsigned __int128` | unsigned 128-bit integer |
| `isize` | `intptr_t`, `ssize_t` | signed pointer sized integer |
| `usize` | `uintptr_t`, `size_t` | unsigned pointer sized integer. Also see #5185 |
| `c_char` | `char` | for ABI compatibility with C |
| `c_short` | `short` | for ABI compatibility with C |
| `c_ushort` | `unsigned short` | for ABI compatibility with C |
| `c_int` | `int` | for ABI compatibility with C |
| `c_uint` | `unsigned int` | for ABI compatibility with C |
| `c_long` | `long` | for ABI compatibility with C |
| `c_ulong` | `unsigned long` | for ABI compatibility with C |
| `c_longlong` | `long long` | for ABI compatibility with C |
| `c_ulonglong` | `unsigned long long` | for ABI compatibility with C |
| `c_longdouble` | `long double` | for ABI compatibility with C |
| `f16` | `_Float16` | 16-bit floating point (10-bit mantissa) IEEE-754-2008 binary16 |
| `f32` | `float` | 32-bit floating point (23-bit mantissa) IEEE-754-2008 binary32 |
| `f64` | `double` | 64-bit floating point (52-bit mantissa) IEEE-754-2008 binary64 |
| `f80` | `long double` | 80-bit floating point (64-bit mantissa) IEEE-754-2008 80-bit extended precision |
| `f128` | `_Float128` | 128-bit floating point (112-bit mantissa) IEEE-754-2008 binary128 |
| `bool` | `bool` | `true` or `false` |
| `anyopaque` | `void` | Used for type-erased pointers. |
| `noreturn` | (none) | the type of `break`, `continue`, `return`, `unreachable`, and `while (true) {}` |
| `type` | (none) | the type of types |
| `anyerror` | (none) | an error code |
| `comptime_int` | (none) | Only allowed for comptime-known values. The type of integer literals. |
| `comptime_float` | (none) | Only allowed for comptime-known values. The type of float literals. |

In addition to the integer types above, arbitrary bit-width integers can be referenced by using an identifier of `i` or `u` followed by digits. For example, the identifier `i7` refers to a signed 7-bit integer. The maximum allowed bit-width of an integer type is `65535`.

See also:

- Integers
- Floats
- void
- Errors
- @Int

### Primitive Values

| Name | Description |
|---|---|
| `true` and `false` | `bool` values |
| `null` | used to set an optional type to `null` |
| `undefined` | used to leave a value unspecified |

See also:

- Optionals
- undefined

### String Literals and Unicode Code Point Literals

String literals are constant single-item Pointers to null-terminated byte arrays. The type of string literals encodes both the length, and the fact that they are null-terminated, and thus they can be coerced to both Slices and Null-Terminated Pointers. Dereferencing string literals converts them to Arrays.

Because Zig source code is UTF-8 encoded, any non-ASCII bytes appearing within a string literal in source code carry their UTF-8 meaning into the content of the string in the Zig program; the bytes are not modified by the compiler. It is possible to embed non-UTF-8 bytes into a string literal using `\xNN` notation.

Indexing into a string containing non-ASCII bytes returns individual bytes, whether valid UTF-8 or not.

Unicode code point literals have type `comptime_int`, the same as Integer Literals. All Escape Sequences are valid in both string literals and Unicode code point literals.

```
const print = @import("std").debug.print;
const mem = @import("std").mem; 

pub fn main() void {
    const bytes = "hello";
    print("{}\n", .{@TypeOf(bytes)}); 
    print("{d}\n", .{bytes.len}); 
    print("{c}\n", .{bytes[1]}); 
    print("{d}\n", .{bytes[5]}); 
    print("{}\n", .{'e' == '\x65'}); 
    print("{d}\n", .{'\u{1f4a9}'}); 
    print("{d}\n", .{'💯'}); 
    print("{u}\n", .{'⚡'});
    print("{}\n", .{mem.eql(u8, "hello", "h\x65llo")}); 
    print("{}\n", .{mem.eql(u8, "💯", "\xf0\x9f\x92\xaf")}); 
    const invalid_utf8 = "\xff\xfe"; 
    print("0x{x}\n", .{invalid_utf8[1]}); 
    print("0x{x}\n", .{"💯"[1]}); 
}
```

```
$ zig build-exe string_literals.zig
$ ./string_literals
*const [5:0]u8
5
e
0
true
128169
128175
⚡
true
true
0xfe
0x9f
```

See also:

- Arrays
- Source Encoding

#### Escape Sequences

| Escape Sequence | Name |
|---|---|
| `\n` | Newline |
| `\r` | Carriage Return |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single Quote |
| `\"` | Double Quote |
| `\xNN` | hexadecimal 8-bit byte value (2 digits) |
| `\u{NNNNNN}` | hexadecimal Unicode scalar value UTF-8 encoded (1 or more digits) |

Note that the maximum valid Unicode scalar value is `0x10ffff`.

#### Multiline String Literals

Multiline string literals have no escapes and can span across multiple lines. To start a multiline string literal, use the `\\` token. Just like a comment, the string literal goes until the end of the line. The end of the line is not included in the string literal. However, if the next line begins with `\\` then a newline is appended and the string literal continues.

```
const hello_world_in_c =
    \\#include <stdio.h>
    \\
    \\int main(int argc, char **argv) {
    \\    printf("hello world\n");
    \\    return 0;
    \\}
;
```

See also:

- @embedFile

### Assignment

Use the `const` keyword to assign a value to an identifier:

```
const x = 1234;

fn foo() void {
    
    const y = 5678;

    
    y += 1;
}

pub fn main() void {
    foo();
}
```

```
$ zig build-exe constant_identifier_cannot_change.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/constant_identifier_cannot_change.zig:8:5: error: cannot assign to constant
    y += 1;
    ^
referenced by:
    main: /home/ci/work/zig-bootstrap/zig/doc/langref/constant_identifier_cannot_change.zig:12:8
    callMain [inlined]: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:751:64
    callMainWithArgs [inlined]: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:692:20
    posixCallMainAndExit: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:644:38
    2 reference(s) hidden; use '-freference-trace=6' to see all references
```

`const` applies to all of the bytes that the identifier immediately addresses. Pointers have their own const-ness.

If you need a variable that you can modify, use the `var` keyword:

```
const print = @import("std").debug.print;

pub fn main() void {
    var y: i32 = 5678;

    y += 1;

    print("{d}", .{y});
}
```

```
$ zig build-exe mutable_var.zig
$ ./mutable_var
5679
```

Variables must be initialized:

```
pub fn main() void {
    var x: i32;

    x = 1;
}
```

```
$ zig build-exe var_must_be_initialized.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/var_must_be_initialized.zig:2:15: error: expected '=', found ';'
    var x: i32;
              ^
```

#### undefined

Use `undefined` to leave variables uninitialized:

```
const print = @import("std").debug.print;

pub fn main() void {
    var x: i32 = undefined;
    x = 1;
    print("{d}", .{x});
}
```

```
$ zig build-exe assign_undefined.zig
$ ./assign_undefined
1
```

`undefined` can be coerced to any type. Once this happens, it is no longer possible to detect that the value is `undefined`. `undefined` means the value could be anything, even something that is nonsense according to the type. Translated into English, `undefined` means "Not a meaningful value. Using this value would be a bug. The value will be unused, or overwritten before being used."

In Debug and ReleaseSafe mode, Zig writes `0xaa` bytes to undefined memory. This is to catch bugs early, and to help detect use of undefined memory in a debugger. However, this behavior is only an implementation feature, not a language semantic, so it is not guaranteed to be observable to code.

#### Destructuring

A destructuring assignment can separate elements of indexable aggregate types (Tuples, Arrays, Vectors):

```
const print = @import("std").debug.print;

pub fn main() void {
    var x: u32 = undefined;
    var y: u32 = undefined;
    var z: u32 = undefined;

    const tuple = .{ 1, 2, 3 };

    x, y, z = tuple;

    print("tuple: x = {}, y = {}, z = {}\n", .{x, y, z});

    const array = [_]u32{ 4, 5, 6 };

    x, y, z = array;

    print("array: x = {}, y = {}, z = {}\n", .{x, y, z});

    const vector: @Vector(3, u32) = .{ 7, 8, 9 };

    x, y, z = vector;

    print("vector: x = {}, y = {}, z = {}\n", .{x, y, z});
}
```

```
$ zig build-exe destructuring_to_existing.zig
$ ./destructuring_to_existing
tuple: x = 1, y = 2, z = 3
array: x = 4, y = 5, z = 6
vector: x = 7, y = 8, z = 9
```

A destructuring expression may only appear within a block (i.e. not at Namespace scope). The left hand side of the assignment must consist of a comma separated list, each element of which may be either an lvalue (for instance, an existing `var`) or a variable declaration:

```
const print = @import("std").debug.print;

pub fn main() void {
    var x: u32 = undefined;

    const tuple = .{ 1, 2, 3 };

    x, var y : u32, const z = tuple;

    print("x = {}, y = {}, z = {}\n", .{x, y, z});

    
    y = 100;

    
    _, x, _ = tuple;

    print("x = {}\n", .{x});
}
```

```
$ zig build-exe destructuring_mixed.zig
$ ./destructuring_mixed
x = 1, y = 2, z = 3
x = 2
```

A destructure may be prefixed with the `comptime` keyword, in which case the entire destructure expression is evaluated at comptime. All `var`s declared would be `comptime var`s and all expressions (both result locations and the assignee expression) are evaluated at comptime.

See also:

- Destructuring Tuples
- Destructuring Arrays
- Destructuring Vectors


## Zig Test

Code written within one or more `test` declarations can be used to ensure behavior meets expectations:

```
const std = @import("std");

test "expect addOne adds one to 41" {

    
    
    
    
    try std.testing.expect(addOne(41) == 42);

    
    
    try std.testing.expectEqual(42, addOne(41));
}

test addOne {
    
    
    try std.testing.expectEqual(42, addOne(41));
}

fn addOne(number: i32) i32 {
    return number + 1;
}
```

```
$ zig test testing_introduction.zig
1/2 testing_introduction.test.expect addOne adds one to 41...OK
2/2 testing_introduction.decltest.addOne...OK
All 2 tests passed.
```

The `testing_introduction.zig` code sample tests the function `addOne` to ensure that it returns `42` given the input `41`. From this test's perspective, the `addOne` function is said to be *code under test*.

zig test is a tool that creates and runs a test build. By default, it builds and runs an executable program using the *default test runner* provided by the Zig Standard Library as its main entry point. During the build, `test` declarations found while resolving the given Zig source file are included for the default test runner to run and report on.

The shell output shown above displays two lines after the zig test command. These lines are printed to standard error by the default test runner:

**1/2 testing_introduction.test.expect addOne adds one to 41...**

Lines like this indicate which test, out of the total number of tests, is being run. In this case,

1/2

indicates that the first test, out of a total of two tests, is being run. Note that, when the test runner program's standard error is output to the terminal, these lines are cleared when a test succeeds.

**2/2 testing_introduction.decltest.addOne...**

When the test name is an identifier, the default test runner uses the text decltest instead of test.

**All 2 tests passed.**

This line indicates the total number of tests that have passed.

### Test Declarations

Test declarations contain the keyword `test`, followed by an optional name written as a string literal or an identifier, followed by a block containing any valid Zig code that is allowed in a function.

Non-named test blocks always run during test builds and are exempt from Skip Tests.

Test declarations are similar to Functions: they have a return type and a block of code. The implicit return type of `test` is the Error Union Type `anyerror!void`, and it cannot be changed. When a Zig source file is not built using the zig test tool, the test declarations are omitted from the build.

Test declarations can be written in the same file, where code under test is written, or in a separate Zig source file. Since test declarations are top-level declarations, they are order-independent and can be written before or after the code under test.

See also:

- The Global Error Set
- Grammar

#### Doctests

Test declarations named using an identifier are *doctests*. The identifier must refer to another declaration in scope. A doctest, like a doc comment, serves as documentation for the associated declaration, and will appear in the generated documentation for the declaration.

An effective doctest should be self-contained and focused on the declaration being tested, answering questions a new user might have about its interface or intended usage, while avoiding unnecessary or confusing details. A doctest is not a substitute for a doc comment, but rather a supplement and companion providing a testable, code-driven example, verified by zig test.

### Test Failure

The default test runner checks for an error returned from a test. When a test returns an error, the test is considered a failure and its error return trace is output to standard error. The total number of failures will be reported after all tests have run.

```
const std = @import("std");

test "expect this to fail" {
    try std.testing.expect(false);
}

test "expect this to succeed" {
    try std.testing.expect(true);
}
```

```
$ zig test testing_failure.zig
1/2 testing_failure.test.expect this to fail...FAIL (TestUnexpectedResult)
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/testing.zig:614:14: 0x124d0e9 in expect (std.zig)
    if (!ok) return error.TestUnexpectedResult;
             ^
/home/ci/work/zig-bootstrap/zig/doc/langref/testing_failure.zig:4:5: 0x124d1d9 in test.expect this to fail (testing_failure.zig)
    try std.testing.expect(false);
    ^
2/2 testing_failure.test.expect this to succeed...OK
1 passed; 0 skipped; 1 failed.
error: the following test command failed with exit code 1:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/b4e844dd1520a33841c3bdabb9dacd4d/test --seed=0xbf9a9d72
```

One way to skip tests is to filter them out by using the zig test command line parameter --test-filter [text]. This makes the test build only include tests whose name contains the supplied filter text. Note that non-named tests are run even when using the --test-filter [text] command line parameter.

To programmatically skip a test, make a `test` return the error `error.SkipZigTest` and the default test runner will consider the test as being skipped. The total number of skipped tests will be reported after all tests have run.

```
test "this will be skipped" {
    return error.SkipZigTest;
}
```

```
$ zig test testing_skip.zig
1/1 testing_skip.test.this will be skipped...SKIP
0 passed; 1 skipped; 0 failed.
```

### Report Memory Leaks

When code allocates Memory using the Zig Standard Library's testing allocator, `std.testing.allocator`, the default test runner will report any leaks that are found from using the testing allocator:

```
const std = @import("std");

test "detect leak" {
    const gpa = std.testing.allocator;
    var list: std.ArrayList(u21) = .empty;
    
    try list.append(gpa, '☔');

    try std.testing.expectEqual(1, list.items.len);
}
```

```
$ zig test testing_detect_leak.zig
1/1 testing_detect_leak.test.detect leak...OK
[SafeAllocator] (err): leaked [addr: 7fdeae84a010, len: 132 (0x84) align: 4] allocated at:
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/array_list.zig:1232:56: 0x124e277 in ensureTotalCapacityPrecise (std.zig)
                const new_memory = try gpa.alignedAlloc(T, alignment, new_capacity);
                                                       ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/array_list.zig:1208:51: 0x124dec9 in ensureTotalCapacity (std.zig)
            return self.ensureTotalCapacityPrecise(gpa, growCapacity(new_capacity));
                                                  ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/array_list.zig:1262:41: 0x124d4ad in addOne (std.zig)
            try self.ensureTotalCapacity(gpa, newlen);
                                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/array_list.zig:901:49: 0x124d347 in append (std.zig)
            const new_item_ptr = try self.addOne(gpa);
                                                ^
/home/ci/work/zig-bootstrap/zig/doc/langref/testing_detect_leak.zig:7:20: 0x124d1a1 in test.detect leak (testing_detect_leak.zig)
    try list.append(gpa, '☔');
                   ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:296:25: 0x1200de1 in mainTerminal (test_runner.zig)
        if (test_fn.func()) |_| {
                        ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/compiler/test_runner.zig:73:28: 0x12005b2 in main (test_runner.zig)
        return mainTerminal(init);
                           ^
(additional stack frames may have been skipped...)

All 1 tests passed.
1 errors were logged.
1 tests leaked memory.
error: the following test command failed with exit code 1:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/aa4c55fc7acffb16b3340f131daac80c/test --seed=0x86f6f27a
```

See also:

- defer
- Memory

### Detecting Test Build

Use the compile variable `@import("builtin").is_test` to detect a test build:

```
const std = @import("std");
const builtin = @import("builtin");
const expect = std.testing.expect;

test "builtin.is_test" {
    try expect(isATest());
}

fn isATest() bool {
    return builtin.is_test;
}
```

```
$ zig test testing_detect_test.zig
1/1 testing_detect_test.test.builtin.is_test...OK
All 1 tests passed.
```

### Test Output and Logging

The default test runner and the Zig Standard Library's testing namespace output messages to standard error.

### The Testing Namespace

The Zig Standard Library's `testing` namespace contains useful functions to help you create tests. In addition to the `expect` function, this document uses a couple of more functions as exemplified here:

```
const std = @import("std");

test "expectEqual demo" {
    const expected: i32 = 42;
    const actual = 42;

    
    
    
    try std.testing.expectEqual(expected, actual);
}

test "expectError demo" {
    const expected_error = error.DemoError;
    const actual_error_union: anyerror!void = error.DemoError;

    
    
    try std.testing.expectError(expected_error, actual_error_union);
}
```

```
$ zig test testing_namespace.zig
1/2 testing_namespace.test.expectEqual demo...OK
2/2 testing_namespace.test.expectError demo...OK
All 2 tests passed.
```

The Zig Standard Library also contains functions to compare Slices, strings, and more. See the rest of the `std.testing` namespace in the Zig Standard Library for more available functions.

### Test Tool Documentation

zig test has a few command line parameters which affect the compilation. See zig test --help for a full list.


## Variables

A variable is a unit of Memory storage.

It is generally preferable to use `const` rather than `var` when declaring a variable. This causes less work for both humans and computers to do when reading code, and creates more optimization opportunities.

Variables are never allowed to shadow Identifiers from an outer scope.

The `extern` keyword or @extern builtin function can be used to link against a variable that is exported from another object. The `export` keyword or @export builtin function can be used to make a variable available to other objects at link time. In both cases, the type of the variable must be C ABI compatible.

See also:

- Exporting a C Library

### Namespace Level Variables

Namespace level variables have global lifetime and are order-independent and lazily analyzed. The initialization value of namespace level variables is implicitly comptime. If a namespace level variable is `const` then its value is `comptime`-known, otherwise it is runtime-known.

```
var y: i32 = add(10, x);
const x: i32 = add(12, 34);

test "container level variables" {
    try expectEqual(46, x);
    try expectEqual(56, y);
}

fn add(a: i32, b: i32) i32 {
    return a + b;
}

const std = @import("std");
const expectEqual = std.testing.expectEqual;
```

```
$ zig test test_namespace_level_variables.zig
1/1 test_namespace_level_variables.test.container level variables...OK
All 1 tests passed.
```

Namespace level variables may be declared inside a struct, union, enum, or opaque:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "namespaced container level variable" {
    try expectEqual(1235, foo());
    try expectEqual(1236, foo());
}

const S = struct {
    var x: i32 = 1234;
};

fn foo() i32 {
    S.x += 1;
    return S.x;
}
```

```
$ zig test test_namespaced_variable.zig
1/1 test_namespaced_variable.test.namespaced container level variable...OK
All 1 tests passed.
```

### Locally-Scoped Global Variables

It is also possible to have local variables with global lifetime by using namespaces inside functions.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "static local variable" {
    try expectEqual(1235, foo());
    try expectEqual(1236, foo());
}

fn foo() i32 {
    const S = struct {
        var x: i32 = 1234;
    };
    S.x += 1;
    return S.x;
}
```

```
$ zig test test_locally_scoped_global_variable.zig
1/1 test_locally_scoped_global_variable.test.static local variable...OK
All 1 tests passed.
```

### Thread Local Variables

A variable may be specified to be a thread-local variable using the `threadlocal` keyword, which makes each thread work with a separate instance of the variable:

```
const std = @import("std");
const assert = std.debug.assert;

threadlocal var x: i32 = 1234;

test "thread local storage" {
    const thread1 = try std.Thread.spawn(.{}, testTls, .{});
    const thread2 = try std.Thread.spawn(.{}, testTls, .{});
    testTls();
    thread1.join();
    thread2.join();
}

fn testTls() void {
    assert(x == 1234);
    x += 1;
    assert(x == 1235);
}
```

```
$ zig test test_thread_local_variables.zig
1/1 test_thread_local_variables.test.thread local storage...OK
All 1 tests passed.
```

For Single Threaded Builds, all thread local variables are treated as regular Namespace Level Variables.

Thread local variables may not be `const`.

### Local Variables

Local variables occur inside Functions, comptime blocks, and labeled Blocks.

When a local variable is `const`, it means that after initialization, the variable's value will not change. If the initialization value of a `const` variable is comptime-known, then the variable is also `comptime`-known.

A local variable may be qualified with the `comptime` keyword. This causes the variable's value to be `comptime`-known, and all loads and stores of the variable to happen during semantic analysis of the program, rather than at runtime. All variables declared in a `comptime` expression are implicitly `comptime` variables.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "comptime vars" {
    var x: i32 = 1;
    comptime var y: i32 = 1;

    x += 1;
    y += 1;

    try expectEqual(2, x);
    try expectEqual(2, y);

    if (y != 2) {
        
        
        @compileError("wrong y value");
    }
}
```

```
$ zig test test_comptime_variables.zig
1/1 test_comptime_variables.test.comptime vars...OK
All 1 tests passed.
```


## Integers

### Integer Literals

```
const decimal_int = 98222;
const hex_int = 0xff;
const another_hex_int = 0xFF;
const octal_int = 0o755;
const binary_int = 0b11110000;

const one_billion = 1_000_000_000;
const binary_mask = 0b1_1111_1111;
const permissions = 0o7_5_5;
const big_address = 0xFF80_0000_0000_0000;
```

### Runtime Integer Values

Integer literals have no size limitation, and if any Illegal Behavior occurs, the compiler catches it.

However, once an integer value is no longer known at compile-time, it must have a known size, and is vulnerable to safety-checked Illegal Behavior.

```
fn divide(a: i32, b: i32) i32 {
    return a / b;
}
```

In this function, values `a` and `b` are known only at runtime, and thus this division operation is vulnerable to both Integer Overflow and Division by Zero.

Operators such as `+` and `-` cause Illegal Behavior on integer overflow. Alternative operators are provided for wrapping and saturating arithmetic on all targets. `+%` and `-%` perform wrapping arithmetic while `+|` and `-|` perform saturating arithmetic.

Zig supports arbitrary bit-width integers, referenced by using an identifier of `i` or `u` followed by digits. For example, the identifier `i7` refers to a signed 7-bit integer. The maximum allowed bit-width of an integer type is `65535`. For signed integer types, Zig uses a two's complement representation.

See also:

- Wrapping Operations


## Floats

Zig has the following floating point types:

- `f16` - IEEE-754-2008 binary16
- `f32` - IEEE-754-2008 binary32
- `f64` - IEEE-754-2008 binary64
- `f80` - IEEE-754-2008 80-bit extended precision
- `f128` - IEEE-754-2008 binary128
- `c_longdouble` - matches `long double` for the target C ABI

### Float Literals

Float literals have type `comptime_float` which is guaranteed to have the same precision and operations of the largest other floating point type, which is `f128`.

Float literals coerce to any floating point type, and to any integer type when there is no fractional component.

```
const floating_point = 123.0E+77;
const another_float = 123.0;
const yet_another = 123.0e+77;

const hex_floating_point = 0x103.70p-5;
const another_hex_float = 0x103.70;
const yet_another_hex_float = 0x103.70P-5;

const lightspeed = 299_792_458.000_000;
const nanosecond = 0.000_000_001;
const more_hex = 0x1234_5678.9ABC_CDEFp-10;
```

There is no syntax for NaN, infinity, or negative infinity. For these special values, one must use the standard library:

```
const std = @import("std");

const inf = std.math.inf(f32);
const negative_inf = -std.math.inf(f64);
const nan = std.math.nan(f128);
```

### Floating Point Operations

By default floating point operations use `.strict` mode, but you can switch to `.optimized` mode on a per-block basis:

```
const std = @import("std");
const big = @as(f64, 1 << 40);

export fn foo_strict(x: f64) f64 {
    return x + big - big;
}

export fn foo_optimized(x: f64) f64 {
    @setFloatMode(.optimized);
    return x + big - big;
}
```

```
$ zig build-obj float_mode_obj.zig -O ReleaseFast
```

For this test we have to separate code into two object files - otherwise the optimizer figures out all the values at compile-time, which operates in strict mode.

```
const print = @import("std").debug.print;

extern fn foo_strict(x: f64) f64;
extern fn foo_optimized(x: f64) f64;

pub fn main() void {
    const x = 0.001;
    print("optimized = {}\n", .{foo_optimized(x)});
    print("strict = {}\n", .{foo_strict(x)});
}
```

See also:

- @setFloatMode
- Division by Zero


## Operators

There is no operator overloading. When you see an operator in Zig, you know that it is doing something from this table, and nothing else.

### Table of Operators

| Name | Syntax | Types | Remarks | Example |
|---|---|---|---|---|
| Addition | `a + b a += b` | Integers Floats | Can cause overflow for integers. Invokes Peer Type Resolution for the operands. See also @addWithOverflow. | `2 + 5 == 7` |
| Wrapping Addition | `a +% b a +%= b` | Integers | Twos-complement wrapping behavior. Invokes Peer Type Resolution for the operands. See also @addWithOverflow. | `@as(u32, 0xffffffff) +% 1 == 0` |
| Saturating Addition | `a +\| b a +\|= b` | Integers | Invokes Peer Type Resolution for the operands. | `@as(u8, 255) +\| 1 == @as(u8, 255)` |
| Subtraction | `a - b a -= b` | Integers Floats | Can cause overflow for integers. Invokes Peer Type Resolution for the operands. See also @subWithOverflow. | `2 - 5 == -3` |
| Wrapping Subtraction | `a -% b a -%= b` | Integers | Twos-complement wrapping behavior. Invokes Peer Type Resolution for the operands. See also @subWithOverflow. | `@as(u8, 0) -% 1 == 255` |
| Saturating Subtraction | `a -\| b a -\|= b` | Integers | Invokes Peer Type Resolution for the operands. | `@as(u32, 0) -\| 1 == 0` |
| Negation | `-a` | Integers Floats | Can cause overflow for integers. | `-1 == 0 - 1` |
| Wrapping Negation | `-%a` | Integers | Twos-complement wrapping behavior. | `-%@as(i8, -128) == -128` |
| Multiplication | `a * b a *= b` | Integers Floats | Can cause overflow for integers. Invokes Peer Type Resolution for the operands. See also @mulWithOverflow. | `2 * 5 == 10` |
| Wrapping Multiplication | `a *% b a *%= b` | Integers | Twos-complement wrapping behavior. Invokes Peer Type Resolution for the operands. See also @mulWithOverflow. | `@as(u8, 200) *% 2 == 144` |
| Saturating Multiplication | `a *\| b a *\|= b` | Integers | Invokes Peer Type Resolution for the operands. | `@as(u8, 200) *\| 2 == 255` |
| Division | `a / b a /= b` | Integers Floats | Can cause overflow for integers. Can cause Division by Zero for integers. Can cause Division by Zero for floats in FloatMode.optimized Mode. Signed integer operands must be comptime-known and positive. In other cases, use @divTrunc, @divFloor, or @divExact instead. Invokes Peer Type Resolution for the operands. | `10 / 5 == 2` |
| Remainder Division | `a % b a %= b` | Integers Floats | Can cause Division by Zero for integers. Can cause Division by Zero for floats in FloatMode.optimized Mode. Signed or floating-point operands must be comptime-known and positive. In other cases, use @rem or @mod instead. Invokes Peer Type Resolution for the operands. | `10 % 3 == 1` |
| Bit Shift Left | `a << b a <<= b` | Integers | Moves all bits to the left, inserting new zeroes at the least-significant bit. `b` must be comptime-known or have a type with log2 number of bits as `a`. See also @shlExact. See also @shlWithOverflow. | `0b1 << 8 == 0b100000000` |
| Saturating Bit Shift Left | `a <<\| b a <<\|= b` | Integers | See also @shlExact. See also @shlWithOverflow. | `@as(u8, 1) <<\| 8 == 255` |
| Bit Shift Right | `a >> b a >>= b` | Integers | When LHS is unsigned, performs a **logical shift**, moving all bits to the right, inserting zeroes at the most-significant bit. When LHS is signed, performs an **arithmetic shift**, moving all bits to the right, inserting ones at the most-significant bit if and only if the most significant bit is one. `b` must be comptime-known or have a type with log2 number of bits as `a`. See also @shrExact. | `0b1010 >> 1 == 0b101` |
| Bitwise And | `a & b a &= b` | Integers | Invokes Peer Type Resolution for the operands. | `0b011 & 0b101 == 0b001` |
| Bitwise Or | `a \| b a \|= b` | Integers | Invokes Peer Type Resolution for the operands. | `0b010 \| 0b100 == 0b110` |
| Bitwise Xor | `a ^ b a ^= b` | Integers | Invokes Peer Type Resolution for the operands. | `0b011 ^ 0b101 == 0b110` |
| Bitwise Not | `~a` | Integers |   | `~@as(u8, 0b10101111) == 0b01010000` |
| Defaulting Optional Unwrap | `a orelse b` | Optionals | If `a` is `null`, returns `b` ("default value"), otherwise returns the unwrapped value of `a`. Note that `b` may be a value of type noreturn. | `const value: ?u32 = null; const unwrapped = value orelse 1234; unwrapped == 1234` |
| Optional Unwrap | `a.?` | Optionals | Equivalent to: `a orelse unreachable` | `const value: ?u32 = 5678; value.? == 5678` |
| Defaulting Error Unwrap | `a catch b a catch \|err\| b` | Error Unions | If `a` is an `error`, returns `b` ("default value"), otherwise returns the unwrapped value of `a`. Note that `b` may be a value of type noreturn. `err` is the `error` and is in scope of the expression `b`. | `const value: anyerror!u32 = error.Broken; const unwrapped = value catch 1234; unwrapped == 1234` |
| Logical And | `a and b` | bool | If `a` is `false`, returns `false` without evaluating `b`. Otherwise, returns `b`. | `(false and true) == false` |
| Logical Or | `a or b` | bool | If `a` is `true`, returns `true` without evaluating `b`. Otherwise, returns `b`. | `(false or true) == true` |
| Boolean Not | `!a` | bool |   | `!false == true` |
| Equality | `a == b` | Integers Floats bool type packed struct | Returns `true` if a and b are equal, otherwise returns `false`. Invokes Peer Type Resolution for the operands. | `(1 == 1) == true` |
| Null Check | `a == null` | Optionals | Returns `true` if a is `null`, otherwise returns `false`. | `const value: ?u32 = null; (value == null) == true` |
| Inequality | `a != b` | Integers Floats bool type | Returns `false` if a and b are equal, otherwise returns `true`. Invokes Peer Type Resolution for the operands. | `(1 != 1) == false` |
| Non-Null Check | `a != null` | Optionals | Returns `false` if a is `null`, otherwise returns `true`. | `const value: ?u32 = null; (value != null) == false` |
| Greater Than | `a > b` | Integers Floats | Returns `true` if a is greater than b, otherwise returns `false`. Invokes Peer Type Resolution for the operands. | `(2 > 1) == true` |
| Greater or Equal | `a >= b` | Integers Floats | Returns `true` if a is greater than or equal to b, otherwise returns `false`. Invokes Peer Type Resolution for the operands. | `(2 >= 1) == true` |
| Less Than | `a < b` | Integers Floats | Returns `true` if a is less than b, otherwise returns `false`. Invokes Peer Type Resolution for the operands. | `(1 < 2) == true` |
| Lesser or Equal | `a <= b` | Integers Floats | Returns `true` if a is less than or equal to b, otherwise returns `false`. Invokes Peer Type Resolution for the operands. | `(1 <= 2) == true` |
| Array Concatenation | `a ++ b` | Arrays | Only available when the lengths of both `a` and `b` are compile-time known. | `const mem = @import("std").mem; const array1 = [_]u32{1,2}; const array2 = [_]u32{3,4}; const together = array1 ++ array2; mem.eql(u32, &together, &[_]u32{1,2,3,4})` |
| Pointer Dereference | `a.*` | Pointers | Pointer dereference. | `const x: u32 = 1234; const ptr = &x; ptr.* == 1234` |
| Address Of | `&a` | All types |   | `const x: u32 = 1234; const ptr = &x; ptr.* == 1234` |
| Error Set Merge | `a \|\| b` | Error Set Type | Merging Error Sets | `const A = error{One}; const B = error{Two}; (A \|\| B) == error{One, Two}` |

### Precedence

```
x() x[] x.y x.* x.?
a!b
x{}
!x -x -%x ~x &x ?x
* / % *% *| ||
+ - ++ +% -% +| -|
<< >> <<|
& ^ | orelse catch
== != < > <= >=
and
or
= *= *%= *|= /= %= += +%= +|= -= -%= -|= <<= <<|= >>= &= ^= |=
```


## Arrays

```
const expectEqual = @import("std").testing.expectEqual;
const assert = @import("std").debug.assert;
const mem = @import("std").mem;

const message = [_]u8{ 'h', 'e', 'l', 'l', 'o' };

const alt_message: [5]u8 = .{ 'h', 'e', 'l', 'l', 'o' };

comptime {
    assert(mem.eql(u8, &message, &alt_message));
}

comptime {
    assert(message.len == 5);
}

const same_message = "hello";

comptime {
    assert(mem.eql(u8, &message, same_message));
}

test "iterate over an array" {
    var sum: usize = 0;
    for (message) |byte| {
        sum += byte;
    }
    try expectEqual('h' + 'e' + 'l' * 2 + 'o', sum);
}

var some_integers: [100]i32 = undefined;

test "modify an array" {
    for (&some_integers, 0..) |*item, i| {
        item.* = @intCast(i);
    }
    try expectEqual(10, some_integers[10]);
    try expectEqual(99, some_integers[99]);
}

const part_one = [_]i32{ 1, 2, 3, 4 };
const part_two = [_]i32{ 5, 6, 7, 8 };
const all_of_it = part_one ++ part_two;
comptime {
    assert(mem.eql(i32, &all_of_it, &[_]i32{ 1, 2, 3, 4, 5, 6, 7, 8 }));
}

const hello = "hello";
const world = "world";
const hello_world = hello ++ " " ++ world;
comptime {
    assert(mem.eql(u8, hello_world, "hello world"));
}

const all_zero: [10]u16 = @splat(0);

comptime {
    assert(all_zero.len == 10);
    assert(all_zero[5] == 0);
}

var fancy_array = init: {
    var initial_value: [10]Point = undefined;
    for (&initial_value, 0..) |*pt, i| {
        pt.* = Point{
            .x = @intCast(i),
            .y = @intCast(i * 2),
        };
    }
    break :init initial_value;
};
const Point = struct {
    x: i32,
    y: i32,
};

test "compile-time array initialization" {
    try expectEqual(4, fancy_array[4].x);
    try expectEqual(8, fancy_array[4].y);
}

var more_points: [10]Point = @splat(makePoint(3));
fn makePoint(x: i32) Point {
    return Point{
        .x = x,
        .y = x * 2,
    };
}
test "array initialization with function calls" {
    try expectEqual(3, more_points[4].x);
    try expectEqual(6, more_points[4].y);
    try expectEqual(10, more_points.len);
}
```

```
$ zig test test_arrays.zig
1/4 test_arrays.test.iterate over an array...OK
2/4 test_arrays.test.modify an array...OK
3/4 test_arrays.test.compile-time array initialization...OK
4/4 test_arrays.test.array initialization with function calls...OK
All 4 tests passed.
```

See also:

- for
- Slices

### Multidimensional Arrays

Multidimensional arrays can be created by nesting arrays:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const mat4x5 = [4][5]f32{
    [_]f32{ 1.0, 0.0, 0.0, 0.0, 0.0 },
    [_]f32{ 0.0, 1.0, 0.0, 1.0, 0.0 },
    [_]f32{ 0.0, 0.0, 1.0, 0.0, 0.0 },
    [_]f32{ 0.0, 0.0, 0.0, 1.0, 9.9 },
};
test "multidimensional arrays" {
    
    try expectEqual(mat4x5[1], [_]f32{ 0.0, 1.0, 0.0, 1.0, 0.0 });

    
    try expectEqual(9.9, mat4x5[3][4]);

    
    for (mat4x5, 0..) |row, row_index| {
        for (row, 0..) |cell, column_index| {
            if (row_index == column_index) {
                try expectEqual(1.0, cell);
            }
        }
    }

    
    const all_zero: [4][5]f32 = @splat(@splat(0));
    try expectEqual(0, all_zero[0][0]);
}
```

```
$ zig test test_multidimensional_arrays.zig
1/1 test_multidimensional_arrays.test.multidimensional arrays...OK
All 1 tests passed.
```

### Sentinel-Terminated Arrays

The syntax `[N:x]T` describes an array which has a sentinel element of value `x` at the index corresponding to the length `N`.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "0-terminated sentinel array" {
    const array = [_:0]u8{ 1, 2, 3, 4 };

    try expectEqual([4:0]u8, @TypeOf(array));
    try expectEqual(4, array.len);
    try expectEqual(0, array[4]);
}

test "extra 0s in 0-terminated sentinel array" {
    
    const array = [_:0]u8{ 1, 0, 0, 4 };

    try expectEqual([4:0]u8, @TypeOf(array));
    try expectEqual(4, array.len);
    try expectEqual(0, array[4]);
}
```

```
$ zig test test_null_terminated_array.zig
1/2 test_null_terminated_array.test.0-terminated sentinel array...OK
2/2 test_null_terminated_array.test.extra 0s in 0-terminated sentinel array...OK
All 2 tests passed.
```

See also:

- Sentinel-Terminated Pointers
- Sentinel-Terminated Slices

### Destructuring Arrays

Arrays can be destructured:

```
const print = @import("std").debug.print;

fn swizzleRgbaToBgra(rgba: [4]u8) [4]u8 {
    
    const r, const g, const b, const a = rgba;
    return .{ b, g, r, a };
}

pub fn main() void {
    const pos = [_]i32{ 1, 2 };
    const x, const y = pos;
    print("x = {}, y = {}\n", .{x, y});

    const orange: [4]u8 = .{ 255, 165, 0, 255 };
    print("{any}\n", .{swizzleRgbaToBgra(orange)});
}
```

```
$ zig build-exe destructuring_arrays.zig
$ ./destructuring_arrays
x = 1, y = 2
{ 0, 165, 255, 255 }
```

See also:

- Destructuring
- Destructuring Tuples
- Destructuring Vectors
