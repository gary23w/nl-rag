---
title: "Documentation (part 3/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 3/10
---

## enum

```
const expect = @import("std").testing.expect;
const expectEqual = @import("std").testing.expectEqual;
const expectEqualStrings = @import("std").testing.expectEqualStrings;
const mem = @import("std").mem;

const Type = enum {
    ok,
    not_ok,
};

const c = Type.ok;

const Value = enum(u2) {
    zero,
    one,
    two,
};

test "enum ordinal value" {
    try expectEqual(0, @intFromEnum(Value.zero));
    try expectEqual(1, @intFromEnum(Value.one));
    try expectEqual(2, @intFromEnum(Value.two));
}

const Value2 = enum(u32) {
    hundred = 100,
    thousand = 1000,
    million = 1000000,
};
test "set enum ordinal value" {
    try expectEqual(100, @intFromEnum(Value2.hundred));
    try expectEqual(1000, @intFromEnum(Value2.thousand));
    try expectEqual(1000000, @intFromEnum(Value2.million));
}

const Value3 = enum(u4) {
    a,
    b = 8,
    c,
    d = 4,
    e,
};
test "enum implicit ordinal values and overridden values" {
    try expectEqual(0, @intFromEnum(Value3.a));
    try expectEqual(8, @intFromEnum(Value3.b));
    try expectEqual(9, @intFromEnum(Value3.c));
    try expectEqual(4, @intFromEnum(Value3.d));
    try expectEqual(5, @intFromEnum(Value3.e));
}

const Suit = enum {
    clubs,
    spades,
    diamonds,
    hearts,

    pub fn isClubs(self: Suit) bool {
        return self == Suit.clubs;
    }
};
test "enum method" {
    const p = Suit.spades;
    try expect(!p.isClubs());
}

const Foo = enum {
    string,
    number,
    none,
};
test "enum switch" {
    const p = Foo.number;
    const what_is_it = switch (p) {
        Foo.string => "this is a string",
        Foo.number => "this is a number",
        Foo.none => "this is a none",
    };
    try expectEqualStrings(what_is_it, "this is a number");
}

const Small = enum {
    one,
    two,
    three,
    four,
};
test "std.meta.Tag" {
    try expectEqual(u2, @typeInfo(Small).@"enum".tag_type);
}

test "@typeInfo" {
    try expectEqual(4, @typeInfo(Small).@"enum".field_names.len);
    try expectEqualStrings(@typeInfo(Small).@"enum".field_names[1], "two");
}

test "@tagName" {
    try expectEqualStrings(@tagName(Small.three), "three");
}
```

```
$ zig test test_enums.zig
1/8 test_enums.test.enum ordinal value...OK
2/8 test_enums.test.set enum ordinal value...OK
3/8 test_enums.test.enum implicit ordinal values and overridden values...OK
4/8 test_enums.test.enum method...OK
5/8 test_enums.test.enum switch...OK
6/8 test_enums.test.std.meta.Tag...OK
7/8 test_enums.test.@typeInfo...OK
8/8 test_enums.test.@tagName...OK
All 8 tests passed.
```

See also:

- @typeInfo
- @tagName
- @sizeOf

### extern enum

By default, enums are not guaranteed to be compatible with the C ABI:

```
const Foo = enum { a, b, c };
export fn entry(foo: Foo) void {
    _ = foo;
}
```

```
$ zig build-obj enum_export_error.zig -target x86_64-linux
/home/ci/work/zig-bootstrap/zig/doc/langref/enum_export_error.zig:2:17: error: parameter of type 'enum_export_error.Foo' not allowed in function with calling convention 'x86_64_sysv'
export fn entry(foo: Foo) void {
                ^~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/enum_export_error.zig:1:13: note: integer tag type of enum is inferred
const Foo = enum { a, b, c };
            ^~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/enum_export_error.zig:1:13: note: consider explicitly specifying the integer tag type
/home/ci/work/zig-bootstrap/zig/doc/langref/enum_export_error.zig:1:13: note: enum declared here
referenced by:
    root: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:13:22
    comptime: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/start.zig:20:9
    2 reference(s) hidden; use '-freference-trace=4' to see all references
```

For a C-ABI-compatible enum, provide an explicit tag type to the enum:

```
const Foo = enum(c_int) { a, b, c };
export fn entry(foo: Foo) void {
    _ = foo;
}
```

```
$ zig build-obj enum_export.zig
```

### Enum Literals

Enum literals allow specifying the name of an enum field without specifying the enum type:

```
const std = @import("std");
const expect = std.testing.expect;
const expectEqual = std.testing.expectEqual;

const Color = enum {
    auto,
    off,
    on,
};

test "enum literals" {
    const color1: Color = .auto;
    const color2 = Color.auto;
    try expectEqual(color1, color2);
}

test "switch using enum literals" {
    const color = Color.on;
    const result = switch (color) {
        .auto => false,
        .on => true,
        .off => false,
    };
    try expect(result);
}
```

```
$ zig test test_enum_literals.zig
1/2 test_enum_literals.test.enum literals...OK
2/2 test_enum_literals.test.switch using enum literals...OK
All 2 tests passed.
```

### Non-exhaustive enum

A non-exhaustive enum can be created by adding a trailing `_` field. The enum must specify a tag type and cannot consume every enumeration value.

@enumFromInt on a non-exhaustive enum involves the safety semantics of @intCast to the integer tag type, but beyond that always results in a well-defined enum value.

A switch on a non-exhaustive enum can include a `_` prong as an alternative to an `else` prong. With a `_` prong the compiler errors if all the known tag names are not handled by the switch.

```
const std = @import("std");
const expect = std.testing.expect;

const Number = enum(u8) {
    one,
    two,
    three,
    _,
};

test "switch on non-exhaustive enum" {
    const number = Number.one;
    const result = switch (number) {
        .one => true,
        .two, .three => false,
        _ => false,
    };
    try expect(result);
    const is_one = switch (number) {
        .one => true,
        else => false,
    };
    try expect(is_one);
}
```

```
$ zig test test_switch_non-exhaustive.zig
1/1 test_switch_non-exhaustive.test.switch on non-exhaustive enum...OK
All 1 tests passed.
```


## union

A bare `union` defines a set of possible types that a value can be as a list of fields. Only one field can be active at a time. The in-memory representation of bare unions is not guaranteed. Bare unions cannot be used to reinterpret memory. For that, use @ptrCast, or use an extern union or a packed union which have guaranteed in-memory layout. Accessing the non-active field is safety-checked Illegal Behavior:

```
const Payload = union {
    int: i64,
    float: f64,
    boolean: bool,
};
test "simple union" {
    var payload = Payload{ .int = 1234 };
    payload.float = 12.34;
}
```

```
$ zig test test_wrong_union_access.zig
1/1 test_wrong_union_access.test.simple union...thread 2238040 panic: access of union field 'float' while field 'int' is active
/home/ci/work/zig-bootstrap/zig/doc/langref/test_wrong_union_access.zig:8:12: 0x124d112 in test.simple union (test_wrong_union_access.zig)
    payload.float = 12.34;
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
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/929a59a7cfda517f45c60ecce3a04a78/test --seed=0x53cab995
```

You can activate another field by assigning the entire union:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Payload = union {
    int: i64,
    float: f64,
    boolean: bool,
};
test "simple union" {
    var payload = Payload{ .int = 1234 };
    try expectEqual(1234, payload.int);
    payload = Payload{ .float = 12.34 };
    try expectEqual(12.34, payload.float);
}
```

```
$ zig test test_simple_union.zig
1/1 test_simple_union.test.simple union...OK
All 1 tests passed.
```

In order to use switch with a union, it must be a Tagged union.

To initialize a union when the tag is a comptime-known name, see @unionInit.

### Tagged union

Unions can be declared with an enum tag type. This turns the union into a *tagged* union, which makes it eligible to use with switch expressions. When switching on tagged unions, the tag value can be obtained using an additional capture. Tagged unions coerce to their tag type: Type Coercion: Unions and Enums.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const ComplexTypeTag = enum {
    ok,
    not_ok,
};
const ComplexType = union(ComplexTypeTag) {
    ok: u8,
    not_ok: void,
};

test "switch on tagged union" {
    const c = ComplexType{ .ok = 42 };
    try expectEqual(ComplexTypeTag.ok, @as(ComplexTypeTag, c));

    switch (c) {
        .ok => |value| try expectEqual(42, value),
        .not_ok => unreachable,
    }

    switch (c) {
        .ok => |_, tag| {
            
            comptime std.debug.assert(tag == .ok);
        },
        .not_ok => unreachable,
    }
}

test "get tag type" {
    try expectEqual(ComplexTypeTag, std.meta.Tag(ComplexType));
}
```

```
$ zig test test_tagged_union.zig
1/2 test_tagged_union.test.switch on tagged union...OK
2/2 test_tagged_union.test.get tag type...OK
All 2 tests passed.
```

In order to modify the payload of a tagged union in a switch expression, place a `*` before the variable name to make it a pointer:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const ComplexTypeTag = enum {
    ok,
    not_ok,
};
const ComplexType = union(ComplexTypeTag) {
    ok: u8,
    not_ok: void,
};

test "modify tagged union in switch" {
    var c = ComplexType{ .ok = 42 };

    switch (c) {
        ComplexTypeTag.ok => |*value| value.* += 1,
        ComplexTypeTag.not_ok => unreachable,
    }

    try expectEqual(43, c.ok);
}
```

```
$ zig test test_switch_modify_tagged_union.zig
1/1 test_switch_modify_tagged_union.test.modify tagged union in switch...OK
All 1 tests passed.
```

Unions can be made to infer the enum tag type. Further, unions can have methods just like structs and enums.

```
const std = @import("std");
const expect = std.testing.expect;

const Variant = union(enum) {
    int: i32,
    boolean: bool,

    
    none,

    fn truthy(self: Variant) bool {
        return switch (self) {
            Variant.int => |x_int| x_int != 0,
            Variant.boolean => |x_bool| x_bool,
            Variant.none => false,
        };
    }
};

test "union method" {
    var v1: Variant = .{ .int = 1 };
    var v2: Variant = .{ .boolean = false };
    var v3: Variant = .none;

    try expect(v1.truthy());
    try expect(!v2.truthy());
    try expect(!v3.truthy());
}
```

```
$ zig test test_union_method.zig
1/1 test_union_method.test.union method...OK
All 1 tests passed.
```

Unions with inferred enum tag types can also assign ordinal values to their inferred tag. This requires the tag to specify an explicit integer type. @intFromEnum can be used to access the ordinal value corresponding to the active field.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Tagged = union(enum(u32)) {
    int: i64 = 123,
    boolean: bool = 67,
};

test "tag values" {
    const int: Tagged = .{ .int = -40 };
    try expectEqual(123, @intFromEnum(int));

    const boolean: Tagged = .{ .boolean = false };
    try expectEqual(67, @intFromEnum(boolean));
}
```

```
$ zig test test_tagged_union_with_tag_values.zig
1/1 test_tagged_union_with_tag_values.test.tag values...OK
All 1 tests passed.
```

@tagName can be used to return a comptime `[:0]const u8` value representing the field name:

```
const std = @import("std");
const expectEqualSlices = std.testing.expectEqualSlices;

const Small2 = union(enum) {
    a: i32,
    b: bool,
    c: u8,
};
test "@tagName" {
    try expectEqualSlices(u8, "a", @tagName(Small2.a));
}
```

```
$ zig test test_tagName.zig
1/1 test_tagName.test.@tagName...OK
All 1 tests passed.
```

### extern union

An `extern union` has memory layout guaranteed to be compatible with the target C ABI.

See also:

- extern struct

### packed union

A `packed union` has well-defined in-memory layout and is eligible to be in a packed struct.

All fields in a packed union must have the same @bitSizeOf.

Equating packed unions results in a comparison of the backing integer, and only works for the `==` and `!=` Operators.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "packed union equality" {
    const U = packed union {
        a: u4,
        b: i4,
    };
    const x: U = .{ .a = 3 };
    const y: U = .{ .b = 3 };
    try expectEqual(x, y);
}
```

```
$ zig test test_packed_union_equality.zig
1/1 test_packed_union_equality.test.packed union equality...OK
All 1 tests passed.
```

### Anonymous Union Literals

Anonymous Struct Literals syntax can be used to initialize unions without specifying the type:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Number = union {
    int: i32,
    float: f64,
};

test "anonymous union literal syntax" {
    const i: Number = .{ .int = 42 };
    const f = makeNumber();
    try expectEqual(42, i.int);
    try expectEqual(12.34, f.float);
}

fn makeNumber() Number {
    return .{ .float = 12.34 };
}
```

```
$ zig test test_anonymous_union.zig
1/1 test_anonymous_union.test.anonymous union literal syntax...OK
All 1 tests passed.
```


## opaque

`opaque {}` declares a new type with an unknown (but non-zero) size and alignment. It can contain declarations the same as structs, unions, and enums.

This is typically used for type safety when interacting with C code that does not expose struct details. Example:

```
const Derp = opaque {};
const Wat = opaque {};

extern fn bar(d: *Derp) void;
fn foo(w: *Wat) callconv(.c) void {
    bar(w);
}

test "call foo" {
    foo(undefined);
}
```

```
$ zig test test_opaque.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:6:9: error: expected type '*test_opaque.Derp', found '*test_opaque.Wat'
    bar(w);
        ^
/home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:6:9: note: pointer type child 'test_opaque.Wat' cannot cast into pointer type child 'test_opaque.Derp'
/home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:2:13: note: opaque declared here
const Wat = opaque {};
            ^~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:1:14: note: opaque declared here
const Derp = opaque {};
             ^~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:4:18: note: parameter type declared here
extern fn bar(d: *Derp) void;
                 ^~~~~
referenced by:
    test.call foo: /home/ci/work/zig-bootstrap/zig/doc/langref/test_opaque.zig:10:8
```


## Blocks

Blocks are used to limit the scope of variable declarations:

```
test "access variable after block scope" {
    {
        var x: i32 = 1;
        _ = &x;
    }
    x += 1;
}
```

```
$ zig test test_blocks.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_blocks.zig:6:5: error: use of undeclared identifier 'x'
    x += 1;
    ^
```

Blocks are expressions. When labeled, `break` can be used to return a value from the block:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "labeled break from labeled block expression" {
    var y: i32 = 123;

    const x = blk: {
        y += 1;
        break :blk y;
    };
    try expectEqual(124, x);
    try expectEqual(124, y);
}
```

```
$ zig test test_labeled_break.zig
1/1 test_labeled_break.test.labeled break from labeled block expression...OK
All 1 tests passed.
```

Here, `blk` can be any name.

See also:

- Labeled while
- Labeled for

### Shadowing

Identifiers are never allowed to "hide" other identifiers by using the same name:

```
const pi = 3.14;

test "inside test block" {
    
    {
        var pi: i32 = 1234;
    }
}
```

```
$ zig test test_shadowing.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_shadowing.zig:6:13: error: local variable shadows declaration of 'pi'
        var pi: i32 = 1234;
            ^~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_shadowing.zig:1:1: note: declared here
const pi = 3.14;
^~~~~~~~~~~~~~~
```

Because of this, when you read Zig code you can always rely on an identifier to consistently mean the same thing within the scope it is defined. Note that you can, however, use the same name if the scopes are separate:

```
test "separate scopes" {
    {
        const pi = 3.14;
        _ = pi;
    }
    {
        var pi: bool = true;
        _ = &pi;
    }
}
```

```
$ zig test test_scopes.zig
1/1 test_scopes.test.separate scopes...OK
All 1 tests passed.
```

### Empty Blocks

An empty block returns the single value of type `void`:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test {
    const a = {};
    try expectEqual(void, @TypeOf(a));
}
```

```
$ zig test test_empty_block.zig
1/1 test_empty_block.test_0...OK
All 1 tests passed.
```


## switch

```
const std = @import("std");
const builtin = @import("builtin");
const expectEqual = std.testing.expectEqual;

test "switch simple" {
    const a: u64 = 10;
    const zz: u64 = 103;

    
    
    
    
    
    const b = switch (a) {
        
        1, 2, 3 => 0,

        
        
        5...100 => 1,

        
        101 => blk: {
            const c: u64 = 5;
            break :blk c * 2 + 1;
        },

        
        
        zz => zz,
        blk: {
            const d: u32 = 5;
            const e: u32 = 100;
            break :blk d + e;
        } => 107,

        
        
        
        else => 9,
    };

    try expectEqual(1, b);
}

const os_msg = switch (builtin.target.os.tag) {
    .linux => "we found a linux user",
    else => "not a linux user",
};

test "switch inside function" {
    switch (builtin.target.os.tag) {
        .fuchsia => {
            
            
            
            @compileError("fuchsia not supported");
        },
        else => {},
    }
}
```

```
$ zig test test_switch.zig
1/2 test_switch.test.switch simple...OK
2/2 test_switch.test.switch inside function...OK
All 2 tests passed.
```

`switch` can be used to capture the field values of a Tagged union. Modifications to the field values can be done by placing a `*` before the capture variable name, turning it into a pointer.

```
const expectEqual = @import("std").testing.expectEqual;

test "switch on tagged union" {
    const Point = struct {
        x: u8,
        y: u8,
    };
    const Item = union(enum) {
        a: u32,
        c: Point,
        d,
        e: u32,
    };

    var a = Item{ .c = Point{ .x = 1, .y = 2 } };

    
    const b = switch (a) {
        
        
        
        Item.a, Item.e => |item| item,

        
        Item.c => |*item| blk: {
            item.*.x += 1;
            break :blk 6;
        },

        
        Item.d => 8,
    };

    try expectEqual(6, b);
    try expectEqual(2, a.c.x);
}
```

```
$ zig test test_switch_tagged_union.zig
1/1 test_switch_tagged_union.test.switch on tagged union...OK
All 1 tests passed.
```

See also:

- comptime
- enum
- @compileError
- Compile Variables

### Exhaustive Switching

When a `switch` expression does not have an `else` clause, it must exhaustively list all the possible values. Failure to do so is a compile error:

```
const Color = enum {
    auto,
    off,
    on,
};

test "exhaustive switching" {
    const color = Color.off;
    switch (color) {
        Color.auto => {},
        Color.on => {},
    }
}
```

```
$ zig test test_unhandled_enumeration_value.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unhandled_enumeration_value.zig:9:5: error: switch must handle all possibilities
    switch (color) {
    ^~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unhandled_enumeration_value.zig:3:5: note: unhandled enumeration value: 'off'
    off,
    ^~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unhandled_enumeration_value.zig:1:15: note: enum 'test_unhandled_enumeration_value.Color' declared here
const Color = enum {
              ^~~~
```

### Switching with Enum Literals

Enum Literals can be useful to use with `switch` to avoid repetitively specifying enum or union types:

```
const std = @import("std");
const expect = std.testing.expect;

const Color = enum {
    auto,
    off,
    on,
};

test "enum literals with switch" {
    const color = Color.off;
    const result = switch (color) {
        .auto => false,
        .on => false,
        .off => true,
    };
    try expect(result);
}
```

```
$ zig test test_exhaustive_switch.zig
1/1 test_exhaustive_switch.test.enum literals with switch...OK
All 1 tests passed.
```

### Switching on Errors

When switching on errors, some special cases are allowed to simplify generic programming patterns:

```
const FileOpenError0 = error{
    AccessDenied,
    OutOfMemory,
    FileNotFound,
};

fn openFile0() FileOpenError0 {
    return error.OutOfMemory;
}

test "unreachable else prong" {
    switch (openFile0()) {
        error.AccessDenied, error.FileNotFound => |e| return e,
        error.OutOfMemory => {},
        
        
        
        else => unreachable,
    }

    
    
    
    
}

const FileOpenError1 = error{
    AccessDenied,
    SystemResources,
    FileNotFound,
};

fn openFile1() FileOpenError1 {
    return error.SystemResources;
}

fn openFileGeneric(comptime kind: u1) switch (kind) {
    0 => FileOpenError0,
    1 => FileOpenError1,
} {
    return switch (kind) {
        0 => openFile0(),
        1 => openFile1(),
    };
}

test "comptime unreachable errors not in error set" {
    switch (openFileGeneric(1)) {
        error.AccessDenied, error.FileNotFound => |e| return e,
        error.OutOfMemory => comptime unreachable, 
        error.SystemResources => {},
    }
}
```

```
$ zig test test_switch_on_errors.zig
1/2 test_switch_on_errors.test.unreachable else prong...OK
2/2 test_switch_on_errors.test.comptime unreachable errors not in error set...OK
All 2 tests passed.
```

### Labeled switch

When a switch statement is labeled, it can be referenced from a `break` or `continue`. `break` will return a value from the `switch`.

A `continue` targeting a switch must have an operand. When executed, it will jump to the matching prong, as if the `switch` were executed again with the `continue`'s operand replacing the initial switch value.

```
const std = @import("std");

test "switch continue" {
    sw: switch (@as(i32, 5)) {
        5 => continue :sw 4,

        
        2...4 => |v| {
            if (v > 3) {
                continue :sw 2;
            } else if (v == 3) {

                
                break :sw;
            }

            continue :sw 1;
        },

        1 => return,

        else => unreachable,
    }
}
```

```
$ zig test test_switch_continue.zig
1/1 test_switch_continue.test.switch continue...OK
All 1 tests passed.
```

Semantically, this is equivalent to the following loop:

```
const std = @import("std");

test "switch continue, equivalent loop" {
    var sw: i32 = 5;
    while (true) {
        switch (sw) {
            5 => {
                sw = 4;
                continue;
            },
            2...4 => |v| {
                if (v > 3) {
                    sw = 2;
                    continue;
                } else if (v == 3) {
                    break;
                }

                sw = 1;
                continue;
            },
            1 => return,
            else => unreachable,
        }
    }
}
```

```
$ zig test test_switch_continue_equivalent.zig
1/1 test_switch_continue_equivalent.test.switch continue, equivalent loop...OK
All 1 tests passed.
```

This can improve clarity of (for example) state machines, where the syntax `continue :sw .next_state` is unambiguous, explicit, and immediately understandable.

However, the motivating example is a switch on each element of an array, where using a single switch can improve clarity and performance:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const Instruction = enum {
    add,
    mul,
    end,
};

fn evaluate(initial_stack: []const i32, code: []const Instruction) !i32 {
    var buffer: [8]i32 = undefined;
    var stack = std.ArrayList(i32).initBuffer(&buffer);
    try stack.appendSliceBounded(initial_stack);
    var ip: usize = 0;

    return vm: switch (code[ip]) {
        
        
        .add => {
            try stack.appendBounded(stack.pop().? + stack.pop().?);

            ip += 1;
            continue :vm code[ip];
        },
        .mul => {
            try stack.appendBounded(stack.pop().? * stack.pop().?);

            ip += 1;
            continue :vm code[ip];
        },
        .end => stack.pop().?,
    };
}

test "evaluate" {
    const result = try evaluate(&.{ 7, 2, -3 }, &.{ .mul, .add, .end });
    try expectEqual(1, result);
}
```

```
$ zig test test_switch_dispatch_loop.zig
1/1 test_switch_dispatch_loop.test.evaluate...OK
All 1 tests passed.
```

If the operand to `continue` is comptime-known, then it can be lowered to an unconditional branch to the relevant case. Such a branch is perfectly predicted, and hence typically very fast to execute.

If the operand is runtime-known, each `continue` can embed a conditional branch inline (ideally through a jump table), which allows a CPU to predict its target independently of any other prong. A loop-based lowering would force every branch through the same dispatch point, hindering branch prediction.

### Inline Switch Prongs

Switch prongs can be marked as `inline` to generate the prong's body for each possible value it could have, making the captured value comptime.

```
const std = @import("std");
const expect = std.testing.expect;
const expectError = std.testing.expectError;

fn isFieldOptional(comptime T: type, field_index: usize) !bool {
    const field_types = @typeInfo(T).@"struct".field_types;
    return switch (field_index) {
        
        
        inline 0, 1 => |idx| @typeInfo(field_types[idx]) == .optional,
        else => return error.IndexOutOfBounds,
    };
}

const Struct1 = struct { a: u32, b: ?u32 };

test "using @typeInfo with runtime values" {
    var index: usize = 0;
    try expect(!try isFieldOptional(Struct1, index));
    index += 1;
    try expect(try isFieldOptional(Struct1, index));
    index += 1;
    try expectError(error.IndexOutOfBounds, isFieldOptional(Struct1, index));
}

fn isFieldOptionalUnrolled(field_index: usize) !bool {
    return switch (field_index) {
        0 => false,
        1 => true,
        else => return error.IndexOutOfBounds,
    };
}
```

```
$ zig test test_inline_switch.zig
1/1 test_inline_switch.test.using @typeInfo with runtime values...OK
All 1 tests passed.
```

The `inline` keyword may also be combined with ranges:

```
fn isFieldOptional(comptime T: type, field_index: usize) !bool {
    const field_types = @typeInfo(T).@"struct".field_types;
    return switch (field_index) {
        inline 0...field_types.len - 1 => |idx| @typeInfo(field_types[idx]) == .optional,
        else => return error.IndexOutOfBounds,
    };
}
```

`inline else` prongs can be used as a type safe alternative to `inline for` loops:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const SliceTypeA = extern struct {
    len: usize,
    ptr: [*]u32,
};
const SliceTypeB = extern struct {
    ptr: [*]SliceTypeA,
    len: usize,
};
const AnySlice = union(enum) {
    a: SliceTypeA,
    b: SliceTypeB,
    c: []const u8,
    d: []AnySlice,
};

fn withFor(any: AnySlice) usize {
    const Tag = @typeInfo(AnySlice).@"union".tag_type.?;
    const info = @typeInfo(Tag).@"enum";
    inline for (info.field_names, info.field_values) |field_name, field_value| {
        
        
        
        if (field_value == @intFromEnum(any)) {
            return @field(any, field_name).len;
        }
    }
    
    
    unreachable;
}

fn withSwitch(any: AnySlice) usize {
    return switch (any) {
        
        
        
        inline else => |slice| slice.len,
    };
}

test "inline for and inline else similarity" {
    const any = AnySlice{ .c = "hello" };
    try expectEqual(5, withFor(any));
    try expectEqual(5, withSwitch(any));
}
```

```
$ zig test test_inline_else.zig
1/1 test_inline_else.test.inline for and inline else similarity...OK
All 1 tests passed.
```

When using an inline prong switching on an union an additional capture can be used to obtain the union's enum tag value at comptime, even though its payload might only be known at runtime.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

const U = union(enum) {
    a: u32,
    b: f32,
};

fn getNum(u: U) u32 {
    switch (u) {
        
        
        inline else => |num, tag| {
            if (tag == .b) {
                return @intFromFloat(num);
            }
            return num;
        },
    }
}

test "test" {
    const u = U{ .b = 42 };
    try expectEqual(42, getNum(u));
}
```

```
$ zig test test_inline_switch_union_tag.zig
1/1 test_inline_switch_union_tag.test.test...OK
All 1 tests passed.
```

See also:

- inline while
- inline for
- Tagged union


## while

A while loop is used to repeatedly execute an expression until some condition is no longer true.

```
const expectEqual = @import("std").testing.expectEqual;

test "while basic" {
    var i: usize = 0;
    while (i < 10) {
        i += 1;
    }
    try expectEqual(10, i);
}
```

```
$ zig test test_while.zig
1/1 test_while.test.while basic...OK
All 1 tests passed.
```

Use `break` to exit a while loop early.

```
const expectEqual = @import("std").testing.expectEqual;

test "while break" {
    var i: usize = 0;
    while (true) {
        if (i == 10)
            break;
        i += 1;
    }
    try expectEqual(10, i);
}
```

```
$ zig test test_while_break.zig
1/1 test_while_break.test.while break...OK
All 1 tests passed.
```

Use `continue` to jump back to the beginning of the loop.

```
const expectEqual = @import("std").testing.expectEqual;

test "while continue" {
    var i: usize = 0;
    while (true) {
        i += 1;
        if (i < 10)
            continue;
        break;
    }
    try expectEqual(10, i);
}
```

```
$ zig test test_while_continue.zig
1/1 test_while_continue.test.while continue...OK
All 1 tests passed.
```

While loops support a continue expression which is executed when the loop is continued. The `continue` keyword respects this expression.

```
const expectEqual = @import("std").testing.expectEqual;
const expect = @import("std").testing.expect;

test "while loop continue expression" {
    var i: usize = 0;
    while (i < 10) : (i += 1) {}
    try expectEqual(10, i);
}

test "while loop continue expression, more complicated" {
    var i: usize = 1;
    var j: usize = 1;
    while (i * j < 2000) : ({
        i *= 2;
        j *= 3;
    }) {
        const my_ij = i * j;
        try expect(my_ij < 2000);
    }
}
```

```
$ zig test test_while_continue_expression.zig
1/2 test_while_continue_expression.test.while loop continue expression...OK
2/2 test_while_continue_expression.test.while loop continue expression, more complicated...OK
All 2 tests passed.
```

While loops are expressions. The result of the expression is the result of the `else` clause of a while loop, which is executed when the condition of the while loop is tested as false.

`break`, like `return`, accepts a value parameter. This is the result of the `while` expression. When you `break` from a while loop, the `else` branch is not evaluated.

```
const expect = @import("std").testing.expect;

test "while else" {
    try expect(rangeHasNumber(0, 10, 5));
    try expect(!rangeHasNumber(0, 10, 15));
}

fn rangeHasNumber(begin: usize, end: usize, number: usize) bool {
    var i = begin;
    return while (i < end) : (i += 1) {
        if (i == number) {
            break true;
        }
    } else false;
}
```

```
$ zig test test_while_else.zig
1/1 test_while_else.test.while else...OK
All 1 tests passed.
```

### Labeled while

When a `while` loop is labeled, it can be referenced from a `break` or `continue` from within a nested loop:

```
test "nested break" {
    outer: while (true) {
        while (true) {
            break :outer;
        }
    }
}

test "nested continue" {
    var i: usize = 0;
    outer: while (i < 10) : (i += 1) {
        while (true) {
            continue :outer;
        }
    }
}
```

```
$ zig test test_while_nested_break.zig
1/2 test_while_nested_break.test.nested break...OK
2/2 test_while_nested_break.test.nested continue...OK
All 2 tests passed.
```

### while with Optionals

Just like if expressions, while loops can take an optional as the condition and capture the payload. When null is encountered the loop exits.

When the `|x|` syntax is present on a `while` expression, the while condition must have an Optional Type.

The `else` branch is allowed on optional iteration. In this case, it will be executed on the first null value encountered.

```
const expectEqual = @import("std").testing.expectEqual;

test "while null capture" {
    var sum1: u32 = 0;
    numbers_left = 3;
    while (eventuallyNullSequence()) |value| {
        sum1 += value;
    }
    try expectEqual(3, sum1);

    
    var sum2: u32 = 0;
    numbers_left = 3;
    while (eventuallyNullSequence()) |value| {
        sum2 += value;
    } else {
        try expectEqual(3, sum2);
    }

    
    var i: u32 = 0;
    var sum3: u32 = 0;
    numbers_left = 3;
    while (eventuallyNullSequence()) |value| : (i += 1) {
        sum3 += value;
    }
    try expectEqual(3, i);
}

var numbers_left: u32 = undefined;
fn eventuallyNullSequence() ?u32 {
    return if (numbers_left == 0) null else blk: {
        numbers_left -= 1;
        break :blk numbers_left;
    };
}
```

```
$ zig test test_while_null_capture.zig
1/1 test_while_null_capture.test.while null capture...OK
All 1 tests passed.
```

### while with Error Unions

Just like if expressions, while loops can take an error union as the condition and capture the payload or the error code. When the condition results in an error code the else branch is evaluated and the loop is finished.

When the `else |x|` syntax is present on a `while` expression, the while condition must have an Error Union Type.

```
const expectEqual = @import("std").testing.expectEqual;

test "while error union capture" {
    var sum1: u32 = 0;
    numbers_left = 3;
    while (eventuallyErrorSequence()) |value| {
        sum1 += value;
    } else |err| {
        try expectEqual(error.ReachedZero, err);
    }
}

var numbers_left: u32 = undefined;

fn eventuallyErrorSequence() anyerror!u32 {
    return if (numbers_left == 0) error.ReachedZero else blk: {
        numbers_left -= 1;
        break :blk numbers_left;
    };
}
```

```
$ zig test test_while_error_capture.zig
1/1 test_while_error_capture.test.while error union capture...OK
All 1 tests passed.
```

### inline while

While loops can be inlined. This causes the loop to be unrolled, which allows the code to do some things which only work at compile time, such as use types as first class values.

```
const expectEqual = @import("std").testing.expectEqual;

test "inline while loop" {
    comptime var i = 0;
    var sum: usize = 0;
    inline while (i < 3) : (i += 1) {
        const T = switch (i) {
            0 => f32,
            1 => i8,
            2 => bool,
            else => unreachable,
        };
        sum += typeNameLength(T);
    }
    try expectEqual(9, sum);
}

fn typeNameLength(comptime T: type) usize {
    return @typeName(T).len;
}
```

```
$ zig test test_inline_while.zig
1/1 test_inline_while.test.inline while loop...OK
All 1 tests passed.
```

It is recommended to use `inline` loops only for one of these reasons:

- You need the loop to execute at comptime for the semantics to work.
- You have a benchmark to prove that forcibly unrolling the loop in this way is measurably faster.

See also:

- if
- Optionals
- Errors
- comptime
- unreachable


## for

```
const expectEqual = @import("std").testing.expectEqual;

test "for basics" {
    const items = [_]i32{ 4, 5, 3, 4, 0 };
    var sum: i32 = 0;

    
    for (items) |value| {
        
        if (value == 0) {
            continue;
        }
        sum += value;
    }
    try expectEqual(16, sum);

    
    for (items[0..1]) |value| {
        sum += value;
    }
    try expectEqual(20, sum);

    
    
    var sum2: i32 = 0;
    for (items, 0..) |_, i| {
        try expectEqual(usize, @TypeOf(i));
        sum2 += @as(i32, @intCast(i));
    }
    try expectEqual(10, sum2);

    
    
    var sum3: usize = 0;
    for (0..5) |i| {
        sum3 += i;
    }
    try expectEqual(10, sum3);
}

test "multi object for" {
    const items = [_]usize{ 1, 2, 3 };
    const items2 = [_]usize{ 4, 5, 6 };
    var count: usize = 0;

    
    
    
    for (items, items2) |i, j| {
        count += i + j;
    }

    try expectEqual(21, count);
}

test "for reference" {
    var items = [_]i32{ 3, 4, 2 };

    
    
    for (&items) |*value| {
        value.* += 1;
    }

    try expectEqual(4, items[0]);
    try expectEqual(5, items[1]);
    try expectEqual(3, items[2]);
}

test "for else" {
    
    const items = [_]?i32{ 3, 4, null, 5 };

    
    
    var sum: i32 = 0;
    const result = for (items) |value| {
        if (value != null) {
            sum += value.?;
        }
    } else blk: {
        try expectEqual(12, sum);
        break :blk sum;
    };
    try expectEqual(12, result);
}
```

```
$ zig test test_for.zig
1/4 test_for.test.for basics...OK
2/4 test_for.test.multi object for...OK
3/4 test_for.test.for reference...OK
4/4 test_for.test.for else...OK
All 4 tests passed.
```

### Labeled for

When a `for` loop is labeled, it can be referenced from a `break` or `continue` from within a nested loop:

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

test "nested break" {
    var count: usize = 0;
    outer: for (1..6) |_| {
        for (1..6) |_| {
            count += 1;
            break :outer;
        }
    }
    try expectEqual(1, count);
}

test "nested continue" {
    var count: usize = 0;
    outer: for (1..9) |_| {
        for (1..6) |_| {
            count += 1;
            continue :outer;
        }
    }

    try expectEqual(8, count);
}
```

```
$ zig test test_for_nested_break.zig
1/2 test_for_nested_break.test.nested break...OK
2/2 test_for_nested_break.test.nested continue...OK
All 2 tests passed.
```

### inline for

For loops can be inlined. This causes the loop to be unrolled, which allows the code to do some things which only work at compile time, such as use types as first class values. The capture value and iterator value of inlined for loops are compile-time known.

```
const expectEqual = @import("std").testing.expectEqual;

test "inline for loop" {
    const nums = [_]i32{ 2, 4, 6 };
    var sum: usize = 0;
    inline for (nums) |i| {
        const T = switch (i) {
            2 => f32,
            4 => i8,
            6 => bool,
            else => unreachable,
        };
        sum += typeNameLength(T);
    }
    try expectEqual(9, sum);
}

fn typeNameLength(comptime T: type) usize {
    return @typeName(T).len;
}
```

```
$ zig test test_inline_for.zig
1/1 test_inline_for.test.inline for loop...OK
All 1 tests passed.
```

It is recommended to use `inline` loops only for one of these reasons:

- You need the loop to execute at comptime for the semantics to work.
- You have a benchmark to prove that forcibly unrolling the loop in this way is measurably faster.

See also:

- while
- comptime
- Arrays
- Slices


## if

```
const expect = @import("std").testing.expect;
const expectEqual = @import("std").testing.expectEqual;

test "if expression" {
    
    const a: u32 = 5;
    const b: u32 = 4;
    const result = if (a != b) 47 else 3089;
    try expectEqual(result, 47);
}

test "if boolean" {
    
    const a: u32 = 5;
    const b: u32 = 4;
    if (a != b) {
        try expect(true);
    } else if (a == 9) {
        unreachable;
    } else {
        unreachable;
    }
}

test "if error union" {
    
    

    const a: anyerror!u32 = 0;
    if (a) |value| {
        try expectEqual(value, 0);
    } else |err| {
        _ = err;
        unreachable;
    }

    const b: anyerror!u32 = error.BadValue;
    if (b) |value| {
        _ = value;
        unreachable;
    } else |err| {
        try expectEqual(err, error.BadValue);
    }

    
    if (a) |value| {
        try expectEqual(value, 0);
    } else |_| {}

    
    if (b) |_| {} else |err| {
        try expectEqual(err, error.BadValue);
    }

    
    var c: anyerror!u32 = 3;
    if (c) |*value| {
        value.* = 9;
    } else |_| {
        unreachable;
    }

    if (c) |value| {
        try expectEqual(value, 9);
    } else |_| {
        unreachable;
    }
}
```

```
$ zig test test_if.zig
1/3 test_if.test.if expression...OK
2/3 test_if.test.if boolean...OK
3/3 test_if.test.if error union...OK
All 3 tests passed.
```

### if with Optionals

```
const expect = @import("std").testing.expect;
const expectEqual = @import("std").testing.expectEqual;

test "if optional" {
    

    const a: ?u32 = 0;
    if (a) |value| {
        try expectEqual(0, value);
    } else {
        unreachable;
    }

    const b: ?u32 = null;
    if (b) |_| {
        unreachable;
    } else {
        try expect(true);
    }

    
    if (a) |value| {
        try expectEqual(0, value);
    }

    
    if (b == null) {
        try expect(true);
    }

    
    var c: ?u32 = 3;
    if (c) |*value| {
        value.* = 2;
    }

    if (c) |value| {
        try expectEqual(2, value);
    } else {
        unreachable;
    }
}

test "if error union with optional" {
    
    

    const a: anyerror!?u32 = 0;
    if (a) |optional_value| {
        try expectEqual(0, optional_value.?);
    } else |err| {
        _ = err;
        unreachable;
    }

    const b: anyerror!?u32 = null;
    if (b) |optional_value| {
        try expectEqual(null, optional_value);
    } else |_| {
        unreachable;
    }

    const c: anyerror!?u32 = error.BadValue;
    if (c) |optional_value| {
        _ = optional_value;
        unreachable;
    } else |err| {
        try expectEqual(error.BadValue, err);
    }

    
    var d: anyerror!?u32 = 3;
    if (d) |*optional_value| {
        if (optional_value.*) |*value| {
            value.* = 9;
        }
    } else |_| {
        unreachable;
    }

    if (d) |optional_value| {
        try expectEqual(9, optional_value.?);
    } else |_| {
        unreachable;
    }
}
```

```
$ zig test test_if_optionals.zig
1/2 test_if_optionals.test.if optional...OK
2/2 test_if_optionals.test.if error union with optional...OK
All 2 tests passed.
```

See also:

- Optionals
- Errors


## defer

Executes an expression unconditionally at scope exit.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;
const print = std.debug.print;

fn deferExample() !usize {
    var a: usize = 1;

    {
        defer a = 2;
        a = 1;
    }
    try expectEqual(2, a);

    a = 5;
    return a;
}

test "defer basics" {
    try expectEqual(5, (try deferExample()));
}
```

```
$ zig test test_defer.zig
1/1 test_defer.test.defer basics...OK
All 1 tests passed.
```

Defer expressions are evaluated in reverse order.

```
const std = @import("std");
const print = std.debug.print;

pub fn main() void {
    print("\n", .{});

    defer {
        print("1 ", .{});
    }
    defer {
        print("2 ", .{});
    }
    if (false) {
        
        defer {
            print("3 ", .{});
        }
    }
}
```

```
$ zig build-exe defer_unwind.zig
$ ./defer_unwind

2 1
```

Inside a defer expression the return statement is not allowed.

```
fn deferInvalidExample() !void {
    defer {
        return error.DeferError;
    }

    return error.DeferError;
}
```

```
$ zig test test_invalid_defer.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_invalid_defer.zig:3:9: error: cannot return from defer expression
        return error.DeferError;
        ^~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_invalid_defer.zig:2:5: note: defer expression here
    defer {
    ^~~~~
```

See also:

- Errors


## unreachable

In Debug and ReleaseSafe mode `unreachable` emits a call to `panic` with the message `reached unreachable code`.

In ReleaseFast and ReleaseSmall mode, the optimizer uses the assumption that `unreachable` code will never be hit to perform optimizations.

### Basics

```
test "basic math" {
    const x = 1;
    const y = 2;
    if (x + y != 3) {
        unreachable;
    }
}
```

```
$ zig test test_unreachable.zig
1/1 test_unreachable.test.basic math...OK
All 1 tests passed.
```

In fact, this is how `std.debug.assert` is implemented:

```
fn assert(ok: bool) void {
    if (!ok) unreachable; 
}

test "this will fail" {
    assert(false);
}
```

```
$ zig test test_assertion_failure.zig
1/1 test_assertion_failure.test.this will fail...thread 2235727 panic: reached unreachable code
/home/ci/work/zig-bootstrap/zig/doc/langref/test_assertion_failure.zig:3:14: 0x124d109 in assert (test_assertion_failure.zig)
    if (!ok) unreachable; // assertion failure
             ^
/home/ci/work/zig-bootstrap/zig/doc/langref/test_assertion_failure.zig:8:11: 0x124d0de in test.this will fail (test_assertion_failure.zig)
    assert(false);
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
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/845868e6bb85a84e184813ffd5b3feee/test --seed=0xb4d398a2
```

### At Compile-Time

```
const assert = @import("std").debug.assert;

test "type of unreachable" {
    comptime {
        

        
        

        assert(@TypeOf(unreachable) == noreturn);
    }
}
```

```
$ zig test test_comptime_unreachable.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_unreachable.zig:10:16: error: unreachable code
        assert(@TypeOf(unreachable) == noreturn);
               ^~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_unreachable.zig:10:24: note: control flow is diverted here
        assert(@TypeOf(unreachable) == noreturn);
                       ^~~~~~~~~~~
```

See also:

- Zig Test
- Build Mode
- comptime
