---
title: "Documentation (part 9/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 9/10
---

## Compile Variables

Compile variables are accessible by importing the `"builtin"` package, which the compiler makes available to every Zig source file. It contains compile-time constants such as the current target, endianness, and release mode.

```
const builtin = @import("builtin");
const separator = if (builtin.os.tag == .windows) '\\' else '/';
```

Example of what is imported with `@import("builtin")`:

```
const std = @import("std");

pub const zig_version = std.SemanticVersion.parse(zig_version_string) catch unreachable;
pub const zig_version_string = "0.17.0-dev.1158+1d1193aa7";
pub const zig_backend = std.lang.CompilerBackend.stage2_x86_64;

pub const output_mode: std.lang.OutputMode = .Exe;
pub const link_mode: std.lang.LinkMode = .static;
pub const unwind_tables: std.lang.UnwindTables = .async;
pub const is_test = false;
pub const single_threaded = false;
pub const abi: std.Target.Abi = .gnu;
pub const cpu: std.Target.Cpu = .{
    .arch = .x86_64,
    .model = &std.Target.x86.cpu.znver2,
    .features = std.Target.x86.featureSet(&.{
        .@"64bit",
        .adx,
        .aes,
        .allow_light_256_bit,
        .avx,
        .avx2,
        .bmi,
        .bmi2,
        .branchfusion,
        .clflushopt,
        .clwb,
        .clzero,
        .cmov,
        .crc32,
        .cx16,
        .cx8,
        .f16c,
        .fast_15bytenop,
        .fast_bextr,
        .fast_imm16,
        .fast_lzcnt,
        .fast_movbe,
        .fast_scalar_fsqrt,
        .fast_scalar_shift_masks,
        .fast_variable_perlane_shuffle,
        .fast_vector_fsqrt,
        .fma,
        .fsgsbase,
        .fxsr,
        .idivq_to_divl,
        .lzcnt,
        .mmx,
        .movbe,
        .mwaitx,
        .nopl,
        .pclmul,
        .popcnt,
        .prfchw,
        .rdpid,
        .rdpru,
        .rdrnd,
        .rdseed,
        .sahf,
        .sbb_dep_breaking,
        .sha,
        .slow_shld,
        .smap,
        .smep,
        .sse,
        .sse2,
        .sse3,
        .sse4_1,
        .sse4_2,
        .sse4a,
        .ssse3,
        .vzeroupper,
        .wbnoinvd,
        .x87,
        .xsave,
        .xsavec,
        .xsaveopt,
        .xsaves,
    }),
};
pub const os: std.Target.Os = .{
    .tag = .linux,
    .version_range = .{ .linux = .{
        .range = .{
            .min = .{
                .major = 6,
                .minor = 1,
                .patch = 0,
            },
            .max = .{
                .major = 6,
                .minor = 1,
                .patch = 0,
            },
        },
        .glibc = .{
            .major = 2,
            .minor = 36,
            .patch = 0,
        },
        .android = 29,
    }},
};
pub const target: std.Target = .{
    .cpu = cpu,
    .os = os,
    .abi = abi,
    .ofmt = object_format,
    .dynamic_linker = .init("/lib64/ld-linux-x86-64.so.2"),
};
pub const object_format: std.Target.ObjectFormat = .elf;
pub const mode: std.lang.OptimizeMode = .Debug;
pub const link_libc = false;
pub const link_libcpp = false;
pub const have_error_return_tracing = true;
pub const valgrind_support = true;
pub const sanitize_thread = false;
pub const fuzz = false;
pub const position_independent_code = false;
pub const position_independent_executable = false;
pub const strip_debug_info = false;
pub const code_model: std.lang.CodeModel = .default;
pub const omit_frame_pointer = false;
```

See also:

- Build Mode


## Compilation Model

A Zig compilation is separated into *modules*. Each module is a collection of Zig source files, one of which is the module's *root source file*. Each module can *depend* on any number of other modules, forming a directed graph (dependency loops between modules are allowed). If module A depends on module B, then any Zig source file in module A can import the *root source file* of module B using `@import` with the module's name. In essence, a module acts as an alias to import a Zig source file (which might exist in a completely separate part of the filesystem).

A simple Zig program compiled with `zig build-exe` has two key modules: the one containing your code, known as the "main" or "root" module, and the standard library. Your module *depends on* the standard library module under the name "std", which is what allows you to write `@import("std")`! In fact, every single module in a Zig compilation — including the standard library itself — implicitly depends on the standard library module under the name "std".

The "root module" (the one provided by you in the `zig build-exe` example) has a special property. Like the standard library, it is implicitly made available to all modules (including itself), this time under the name "root". So, `@import("root")` will always be equivalent to `@import` of your "main" source file (often, but not necessarily, named `main.zig`).

### Source File Structs

Every Zig source file is implicitly a `struct` declaration; you can imagine that the file's contents are literally surrounded by `struct { ... }`. This means that as well as declarations, the top level of a file is permitted to contain fields:

```
foo: u32,
bar: u64,

const TopLevelFields = @This();

pub fn init(val: u32) TopLevelFields {
    return .{
        .foo = val,
        .bar = val * 10,
    };
}
```

Such files can be instantiated just like any other `struct` type. A file's "root struct type" can be referred to within that file using @This.

### File and Declaration Discovery

Zig places importance on the concept of whether any piece of code is *semantically analyzed*; in essence, whether the compiler "looks at" it. What code is analyzed is based on what files and declarations are "discovered" from a certain point. This process of "discovery" is based on a simple set of recursive rules:

- If a call to `@import` is analyzed, the file being imported is analyzed.
- If a type (including a file) is analyzed, all `comptime` and `export` declarations within it are analyzed.
- If a type (including a file) is analyzed, and the compilation is for a test, and the module the type is within is the root module of the compilation, then all `test` declarations within it are also analyzed.
- If a reference to a named declaration (i.e. a usage of it) is analyzed, the declaration being referenced is analyzed. Declarations are order-independent, so this reference may be above or below the declaration being referenced, or even in another file entirely.

That's it! Those rules define how Zig files and declarations are discovered. All that remains is to understand where this process *starts*.

The answer to that is the root of the standard library: every Zig compilation begins by analyzing the file `lib/std/std.zig`. This file contains a `comptime` declaration which imports `lib/std/start.zig`, and that file in turn uses `@import("root")` to reference the "root module"; so, the file you provide as your main module's root source file is effectively also a root, because the standard library will always reference it.

It is often desirable to make sure that certain declarations — particularly `test` or `export` declarations — are discovered. Based on the above rules, a common strategy for this is to use `@import` within a `comptime` or `test` block:

```
comptime {
    
    
    _ = @import("api.zig");

    
    
    if (builtin.os.tag == .windows) {
        _ = @import("windows_api.zig");
    }
}

test {
    
    
    _ = @import("tests.zig");

    
    
    if (builtin.os.tag == .windows) {
        _ = @import("windows_tests.zig");
    }
}

const builtin = @import("builtin");
```

### Special Root Declarations

Because the root module's root source file is always accessible using `@import("root")`, is is sometimes used by libraries — including the Zig Standard Library — as a place for the program to expose some "global" information to that library. The Zig Standard Library will look for several declarations in this file.

#### Entry Point

When building an executable, the most important thing to be looked up in this file is the program's *entry point*. Most commonly, this is a function named `main`, which `std.start` will call just after performing important initialization work.

Alternatively, the presence of a declaration named `_start` (for instance, `pub const _start = {};`) will disable the default `std.start` logic, allowing your root source file to export a low-level entry point as needed.

```
pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}

const std = @import("std");
```

```
$ zig build-exe entry_point.zig
$ ./entry_point
Hello, World!
```

If the Zig compilation links libc, the `main` function can optionally be an `export fn` which matches the signature of the C `main` function:

```
pub export fn main(argc: c_int, argv: [*]const [*:0]const u8) c_int {
    const args = argv[0..@intCast(argc)];
    std.debug.print("Hello! argv[0] is '{s}'\n", .{args[0]});
    return 0;
}

const std = @import("std");
```

```
$ zig build-exe libc_export_entry_point.zig -lc
$ ./libc_export_entry_point
Hello! argv[0] is './libc_export_entry_point'
```

`std.start` may also use other entry point declarations in certain situations, such as `wWinMain` or `EfiMain`. Refer to the `lib/std/start.zig` logic for details of these declarations.

#### Standard Library Options

The standard library also looks for a declaration in the root module's root source file named `std_options`. If present, this declaration is expected to be a struct of type `std.Options`, and allows the program to customize some standard library functionality, such as the `std.log` implementation.

```
pub const std_options: std.Options = .{
    
    
    
    .enable_segfault_handler = true,
    
    .logFn = myLogFn,
};

fn myLogFn(
    comptime level: std.log.Level,
    comptime scope: @EnumLiteral(),
    comptime format: []const u8,
    args: anytype,
) void {
    
    
    std.log.defaultLog(level, scope, format, args);
}

const std = @import("std");
```

#### Panic Handler

The Zig Standard Library looks for a declaration named `panic` in the root module's root source file. If present, it is expected to be a Namespace with declarations providing different panic handlers.

See `std.debug.simple_panic` for a basic implementation of this namespace.

Overriding how the panic handler actually outputs messages, but keeping the formatted safety panics which are enabled by default, can be easily achieved with `std.debug.FullPanic`:

```
pub fn main() void {
    @setRuntimeSafety(true);
    var x: u8 = 255;
    
    x += 1;
}

pub const panic = std.debug.FullPanic(myPanic);

fn myPanic(msg: []const u8, first_trace_addr: ?usize) noreturn {
    _ = first_trace_addr;
    std.debug.print("Panic! {s}\n", .{msg});
    std.process.exit(1);
}

const std = @import("std");
```

```
$ zig build-exe panic_handler.zig
$ ./panic_handler
Panic! integer overflow
```


## Zig Build System

The Zig Build System provides a cross-platform, dependency-free way to declare the logic required to build a project. With this system, the logic to build a project is written in a build.zig file, using the Zig Build System API to declare and configure build artifacts and other tasks.

Some examples of tasks the build system can help with:

- Performing tasks in parallel and caching the results.
- Depending on other projects.
- Providing a package for other projects to depend on.
- Creating build artifacts by executing the Zig compiler. This includes building Zig source code as well as C and C++ source code.
- Capturing user-configured options and using those options to configure the build.
- Surfacing build configuration as comptime values by providing a file that can be imported by Zig code.
- Caching build artifacts to avoid unnecessarily repeating steps.
- Executing build artifacts or system-installed tools.
- Running tests and verifying the output of executing a build artifact matches the expected value.
- Running `zig fmt` on a codebase or a subset of it.
- Custom tasks.

To use the build system, run zig build --help to see a command-line usage help menu. This will include project-specific options that were declared in the build.zig script.

For the time being, the build system documentation is hosted externally: Build System Documentation


## C

Although Zig is independent of C, and, unlike most other languages, does not depend on libc, Zig acknowledges the importance of interacting with existing C code.

There are a few ways that Zig facilitates C interop.

### C Type Primitives

These have guaranteed C ABI compatibility and can be used like any other type.

- `c_char`
- `c_short`
- `c_ushort`
- `c_int`
- `c_uint`
- `c_long`
- `c_ulong`
- `c_longlong`
- `c_ulonglong`
- `c_longdouble`

To interop with the C `void` type, use `anyopaque`.

See also:

- Primitive Types

### C Translation CLI

Zig's C translation capability is available as a CLI tool via zig translate-c. It requires a single filename as an argument. It may also take a set of optional flags that are forwarded to clang. It writes the translated file to stdout.

#### Command line flags

- -I: Specify a search directory for include files. May be used multiple times. Equivalent to clang's -I flag. The current directory is *not* included by default; use -I. to include it.
- -D: Define a preprocessor macro. Equivalent to clang's -D flag.
- -cflags [flags] --: Pass arbitrary additional command line flags to clang. Note: the list of flags must end with --
- -target: The target triple for the translated Zig code. If no target is specified, the current host target will be used.

#### Using -target and -cflags

**Important!** When translating C code with zig translate-c, you **must** use the same -target triple that you will use when compiling the translated code. In addition, you **must** ensure that the -cflags used, if any, match the cflags used by code on the target system. Using the incorrect -target or -cflags could result in clang or Zig parse failures, or subtle ABI incompatibilities when linking with C code.

```
long FOO = __LONG_MAX__;
```

```
$ zig translate-c -target thumb-freestanding-gnueabihf varytarget.h|grep FOO
pub export var FOO: c_long = 2147483647;
$ zig translate-c -target x86_64-macos-gnu varytarget.h|grep FOO
pub export var FOO: c_long = 9223372036854775807;
```

```
enum FOO { BAR };
int do_something(enum FOO foo);
```

```
$ zig translate-c varycflags.h|grep -B1 do_something
pub const enum_FOO = c_uint;
pub extern fn do_something(foo: enum_FOO) c_int;
$ zig translate-c -cflags -fshort-enums -- varycflags.h|grep -B1 do_something
pub const enum_FOO = u8;
pub extern fn do_something(foo: enum_FOO) c_int;
```

### Translation failures

Some C constructs cannot be translated to Zig - for example, *goto*, structs with bitfields, and token-pasting macros. Zig employs *demotion* to allow translation to continue in the face of non-translatable entities.

Demotion comes in three varieties - opaque, *extern*, and `@compileError`. C structs and unions that cannot be translated correctly will be translated as `opaque{}`. Functions that contain opaque types or code constructs that cannot be translated will be demoted to `extern` declarations. Thus, non-translatable types can still be used as pointers, and non-translatable functions can be called so long as the linker is aware of the compiled function.

`@compileError` is used when top-level definitions (global variables, function prototypes, macros) cannot be translated or demoted. Since Zig uses lazy analysis for top-level declarations, untranslatable entities will not cause a compile error in your code unless you actually use them.

See also:

- opaque
- extern
- @compileError

### C Pointers

This type is to be avoided whenever possible. The only valid reason for using a C pointer is in auto-generated code from translating C code.

When importing C header files, it is ambiguous whether pointers should be translated as single-item pointers (`*T`) or many-item pointers (`[*]T`). C pointers are a compromise so that Zig code can utilize translated header files directly.

`[*c]T` - C pointer.

- Supports all the syntax of the other two pointer types (`*T`) and (`[*]T`).
- Coerces to other pointer types, as well as Optional Pointers. When a C pointer is coerced to a non-optional pointer, safety-checked Illegal Behavior occurs if the address is 0.
- Allows address 0. On non-freestanding targets, dereferencing address 0 is safety-checked Illegal Behavior. Optional C pointers introduce another bit to keep track of null, just like `?usize`. Note that creating an optional C pointer is unnecessary as one can use normal Optional Pointers.
- Supports Type Coercion to and from integers.
- Supports comparison with integers.
- Does not support Zig-only pointer attributes such as alignment. Use normal Pointers please!

When a C pointer is pointing to a single struct (not an array), dereference the C pointer to access the struct's fields or member data. That syntax looks like this:

`ptr_to_struct.*.struct_member`

This is comparable to doing `->` in C.

When a C pointer is pointing to an array of structs, the syntax reverts to this:

`ptr_to_struct_array[index].struct_member`

### C Variadic Functions

Zig supports extern variadic functions.

```
const std = @import("std");
const testing = std.testing;

pub extern "c" fn printf(format: [*:0]const u8, ...) c_int;

test "variadic function" {
    try testing.expectEqual(14, printf("Hello, world!\n"));
    try testing.expect(@typeInfo(@TypeOf(printf)).@"fn".attrs.varargs);
}
```

```
$ zig test test_variadic_function.zig -lc
1/1 test_variadic_function.test.variadic function...OK
All 1 tests passed.
Hello, world!
```

Variadic functions can be implemented using @cVaStart, @cVaEnd, @cVaArg and @cVaCopy.

```
const std = @import("std");
const testing = std.testing;
const builtin = @import("builtin");

fn add(count: c_int, ...) callconv(.c) c_int {
    var ap = @cVaStart();
    defer @cVaEnd(&ap);
    var i: usize = 0;
    var sum: c_int = 0;
    while (i < count) : (i += 1) {
        sum += @cVaArg(&ap, c_int);
    }
    return sum;
}

test "defining a variadic function" {
    if (builtin.cpu.arch == .aarch64 and builtin.os.tag != .macos) {
        
        return error.SkipZigTest;
    }
    if (builtin.cpu.arch == .x86_64 and builtin.os.tag == .windows) {
        
        return error.SkipZigTest;
    }
    if (builtin.cpu.arch == .s390x) {
        
        return error.SkipZigTest;
    }

    try std.testing.expectEqual(@as(c_int, 0), add(0));
    try std.testing.expectEqual(@as(c_int, 1), add(1, @as(c_int, 1)));
    try std.testing.expectEqual(@as(c_int, 3), add(2, @as(c_int, 1), @as(c_int, 2)));
}
```

```
$ zig test test_defining_variadic_function.zig
1/1 test_defining_variadic_function.test.defining a variadic function...OK
All 1 tests passed.
```

### Exporting a C Library

One of the primary use cases for Zig is exporting a library with the C ABI for other programming languages to call into. The `export` keyword in front of functions, variables, and types causes them to be part of the library API:

```
export fn add(a: i32, b: i32) i32 {
    return a + b;
}
```

To make a static library:

```
$ zig build-lib mathtest.zig
```

To make a shared library:

```
$ zig build-lib mathtest.zig -dynamic
```

Here is an example with the Zig Build System:

```
// This header is generated by zig from mathtest.zig
#include "mathtest.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int32_t result = add(42, 1337);
    printf("%d\n", result);
    return 0;
}
```

```
const std = @import("std");

pub fn build(b: *std.Build) void {
    const lib = b.addLibrary(.{
        .linkage = .dynamic,
        .name = "mathtest",
        .root_module = b.createModule(.{
            .root_source_file = b.path("mathtest.zig"),
        }),
        .version = .{ .major = 1, .minor = 0, .patch = 0 },
    });
    const exe = b.addExecutable(.{
        .name = "test",
        .root_module = b.createModule(.{
            .link_libc = true,
        }),
    });
    exe.root_module.addCSourceFile(.{ .file = b.path("test.c"), .flags = &.{"-std=c99"} });
    exe.root_module.linkLibrary(lib);

    b.default_step.dependOn(&exe.step);

    const run_cmd = exe.run();

    const test_step = b.step("test", "Test the program");
    test_step.dependOn(&run_cmd.step);
}
```

```
$ zig build test
1379
```

See also:

- export

### Mixing Object Files

You can mix Zig object files with any other object files that respect the C ABI. Example:

```
const base64 = @import("std").base64;

export fn decode_base_64(
    dest_ptr: [*]u8,
    dest_len: usize,
    source_ptr: [*]const u8,
    source_len: usize,
) usize {
    const src = source_ptr[0..source_len];
    const dest = dest_ptr[0..dest_len];
    const base64_decoder = base64.standard.Decoder;
    const decoded_size = base64_decoder.calcSizeForSlice(src) catch unreachable;
    base64_decoder.decode(dest[0..decoded_size], src) catch unreachable;
    return decoded_size;
}
```

```
// This header is generated by zig from base64.zig
#include "base64.h"

#include <string.h>
#include <stdio.h>

int main(int argc, char **argv) {
    const char *encoded = "YWxsIHlvdXIgYmFzZSBhcmUgYmVsb25nIHRvIHVz";
    char buf[200];

    size_t len = decode_base_64(buf, 200, encoded, strlen(encoded));
    buf[len] = 0;
    puts(buf);

    return 0;
}
```

```
const std = @import("std");

pub fn build(b: *std.Build) void {
    const obj = b.addObject(.{
        .name = "base64",
        .root_module = b.createModule(.{
            .root_source_file = b.path("base64.zig"),
        }),
    });

    const exe = b.addExecutable(.{
        .name = "test",
        .root_module = b.createModule(.{
            .link_libc = true,
        }),
    });
    exe.root_module.addCSourceFile(.{ .file = b.path("test.c"), .flags = &.{"-std=c99"} });
    exe.root_module.addObject(obj);
    b.installArtifact(exe);
}
```

```
$ zig build
$ ./zig-out/bin/test
all your base are belong to us
```

See also:

- Targets
- Zig Build System


## WebAssembly

Zig supports building for WebAssembly out of the box.

### Freestanding

For host environments like the web browser and nodejs, build as an executable using the freestanding OS target. Here's an example of running Zig code compiled to WebAssembly with nodejs.

```
extern fn print(i32) void;

export fn add(a: i32, b: i32) void {
    print(a + b);
}
```

```
$ zig build-exe math.zig -target wasm32-freestanding -fno-entry --export=add
```

```
const fs = require('fs');
const source = fs.readFileSync("./math.wasm");
const typedArray = new Uint8Array(source);

WebAssembly.instantiate(typedArray, {
  env: {
    print: (result) => { console.log(`The result is ${result}`); }
  }}).then(result => {
  const add = result.instance.exports.add;
  add(1, 2);
});
```

```
$ node test.js
The result is 3
```

### WASI

Zig standard library has first-class support for WebAssembly System Interface.

```
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    const args = try init.minimal.args.toSlice(init.arena.allocator());
    for (0.., args) |i, arg| {
        std.debug.print("{d}: {s}\n", .{ i, arg });
    }
}
```

```
$ zig build-exe wasi_args.zig -target wasm32-wasi
```

```
$ wasmtime wasi_args.wasm 123 hello
0: wasi_args.wasm
1: 123
2: hello
```

A more interesting example would be extracting the list of preopens from the runtime. This is now supported in the standard library via `std.fs.wasi.Preopens`:

```
const std = @import("std");

pub fn main(init: std.process.Init) void {
    for (init.preopens.map.keys(), 0..) |preopen, i| {
        std.log.info("{d}: {s}", .{ i, preopen });
    }
}
```

```
$ zig build-exe wasi_preopens.zig -target wasm32-wasi
```

```
$ wasmtime --dir=. wasi_preopens.wasm
0: stdin
1: stdout
2: stderr
3: .
```


## Targets

**Target** refers to the computer that will be used to run an executable. It is composed of the CPU architecture, the set of enabled CPU features, operating system, minimum and maximum operating system version, ABI, and ABI version.

Zig is a general-purpose programming language which means that it is designed to generate optimal code for a large set of targets. The command `zig targets` provides information about all of the targets the compiler is aware of.

When no target option is provided to the compiler, the default choice is to target the **host computer**, meaning that the resulting executable will be *unsuitable for copying to a different computer*. In order to copy an executable to another computer, the compiler needs to know about the target requirements via the `-target` option.

The Zig Standard Library (`@import("std")`) has cross-platform abstractions, making the same source code viable on many targets. Some code is more portable than other code. In general, Zig code is extremely portable compared to other programming languages.

Each platform requires its own implementations to make Zig's cross-platform abstractions work. These implementations are at various degrees of completion. Each tagged release of the compiler comes with release notes that provide the full support table for each target.


## Style Guide

These coding conventions are not enforced by the compiler, but they are shipped in this documentation along with the compiler in order to provide a point of reference, should anyone wish to point to an authority on agreed upon Zig coding style.

### Avoid Redundancy in Names

Avoid these words in type names:

- Value
- Data
- Context
- Manager
- State
- utils, misc, or somebody's initials

Everything is a value, all types are data, everything is context, all logic manages state. Nothing is communicated by using a word that applies to all types.

Temptation to use "utilities", "miscellaneous", or somebody's initials is a failure to categorize, or more commonly, overcategorization. Such declarations can live at the root of a module that needs them with no namespace needed.

### Avoid Redundant Names in Fully-Qualified Namespaces

Every declaration is assigned a **fully qualified namespace** by the compiler, creating a tree structure. Choose names based on the fully-qualified namespace, and avoid redundant name segments.

```
const std = @import("std");

pub const json = struct {
    pub const JsonValue = union(enum) {
        number: f64,
        boolean: bool,
        
    };
};

pub fn main() void {
    std.debug.print("{s}\n", .{@typeName(json.JsonValue)});
}
```

```
$ zig build-exe redundant_fqn.zig
$ ./redundant_fqn
redundant_fqn.json.JsonValue
```

In this example, "json" is repeated in the fully-qualified namespace. The solution is to delete `Json` from `JsonValue`. In this example we have an empty struct named `json` but remember that files also act as part of the fully-qualified namespace.

This example is an exception to the rule specified in Avoid Redundancy in Names. The meaning of the type has been reduced to its core: it is a json value. The name cannot be any more specific without being incorrect.

### Refrain from Underscore Prefixes

In some programming languages, it is common to prefix identifiers with underscores `_like_this` to avoid keyword collisions, name collisions, or indicate additional metadata associated with usage of the identifier, such as: privacy, existence of complex data invariants, exclusion from semantic versioning, or context-specific type reflection meaning.

In Zig, there are no private fields, and this style guide recommends against pretending otherwise. Instead, fields should be named carefully based on their semantics and documentation should indicate how to use fields without violating data invariants. If a field is not subject to the same semantic versioning rules as everything else, the exception should be noted in the Doc Comments.

As for type reflection, it is less error prone and more maintainable to use the type system than to make field names meaningful.

Regarding name collisions, an underscore is insufficient to explain the difference between the two otherwise identical names. If there's no danger in getting them mixed up, then this guide recommends more verbose names at outer scopes and more abbreviated names at inner scopes.

Finally, keyword collisions are better avoided via String Identifier Syntax.

### Whitespace

- 4 space indentation
- Open braces on same line, unless you need to wrap.
- If a list of things is longer than 2, put each item on its own line and exercise the ability to put an extra comma at the end.
- Line length: aim for 100; use common sense.

### Names

Roughly speaking: `camelCaseFunctionName`, `TitleCaseTypeName`, `snake_case_variable_name`. More precisely:

- If `x` is a `struct` with 0 fields and is never meant to be instantiated then `x` is considered to be a "namespace" and should be `snake_case`.
- If `x` is a `type` or `type` alias then `x` should be `TitleCase`.
- If `x` is callable, and `x`'s return type is `type`, then `x` should be `TitleCase`.
- If `x` is otherwise callable, then `x` should be `camelCase`.
- Otherwise, `x` should be `snake_case`.

Acronyms, initialisms, proper nouns, or any other word that has capitalization rules in written English are subject to naming conventions just like any other word. Even acronyms that are only 2 letters long are subject to these conventions.

File names fall into two categories: types and namespaces. If the file (implicitly a struct) has top level fields, it should be named like any other struct with fields using `TitleCase`. Otherwise, it should use `snake_case`. Directory names should be `snake_case`.

These are general rules of thumb; if it makes sense to do something different, do what makes sense. For example, if there is an established convention such as `ENOENT`, follow the established convention.

### Examples

```
const namespace_name = @import("dir_name/file_name.zig");
const TypeName = @import("dir_name/TypeName.zig");
var global_var: i32 = undefined;
const const_name = 42;
const PrimitiveTypeAlias = f32;

const StructName = struct {
    field: i32,
};
const StructAlias = StructName;

fn functionName(param_name: TypeName) void {
    var functionPointer = functionName;
    functionPointer();
    functionPointer = otherFunction;
    functionPointer();
}
const functionAlias = functionName;

fn ListTemplateFunction(comptime ChildType: type, comptime fixed_size: usize) type {
    return List(ChildType, fixed_size);
}

fn ShortList(comptime T: type, comptime n: usize) type {
    return struct {
        field_name: [n]T,
        fn methodName() void {}
    };
}

const xml_document =
    \\<?xml version="1.0" encoding="UTF-8"?>
    \\<document>
    \\</document>
;
const XmlParser = struct {
    field: i32,
};

fn readU32Be() u32 {}
```

See the Zig Standard Library for more examples.

- Omit any information that is redundant based on the name of the thing being documented.
- Duplicating information onto multiple similar functions is encouraged because it helps IDEs and other tools provide better help text.
- Use the word **assume** to indicate invariants that cause *unchecked* Illegal Behavior when violated.
- Use the word **assert** to indicate invariants that cause *safety-checked* Illegal Behavior when violated.


## Source Encoding

Zig source code is encoded in UTF-8. An invalid UTF-8 byte sequence results in a compile error.

Throughout all zig source code (including in comments), some code points are never allowed:

- Ascii control characters, except for U+000a (LF), U+000d (CR), and U+0009 (HT): U+0000 - U+0008, U+000b - U+000c, U+000e - U+0001f, U+007f.
- Non-Ascii Unicode line endings: U+0085 (NEL), U+2028 (LS), U+2029 (PS).

LF (byte value 0x0a, code point U+000a, `'\n'`) is the line terminator in Zig source code. This byte value terminates every line of zig source code except the last line of the file. It is recommended that non-empty source files end with an empty line, which means the last byte would be 0x0a (LF).

Each LF may be immediately preceded by a single CR (byte value 0x0d, code point U+000d, `'\r'`) to form a Windows style line ending, but this is discouraged. Note that in multiline strings, CRLF sequences will be encoded as LF when compiled into a zig program. A CR in any other context is not allowed.

HT hard tabs (byte value 0x09, code point U+0009, `'\t'`) are interchangeable with SP spaces (byte value 0x20, code point U+0020, `' '`) as a token separator, but use of hard tabs is discouraged. See Grammar.

For compatibility with other tools, the compiler ignores a UTF-8-encoded byte order mark (U+FEFF) if it is the first Unicode code point in the source text. A byte order mark is not allowed anywhere else in the source.

Note that running zig fmt on a source file will implement all recommendations mentioned here.

Note that a tool reading Zig source code can make assumptions if the source code is assumed to be correct Zig code. For example, when identifying the ends of lines, a tool can use a naive search such as `/\n/`, or an advanced search such as `/\r\n?|[\n\u0085\u2028\u2029]/`, and in either case line endings will be correctly identified. For another example, when identifying the whitespace before the first token on a line, a tool can either use a naive search such as `/[ \t]/`, or an advanced search such as `/\s/`, and in either case whitespace will be correctly identified.


## Keyword Reference

| Keyword | Description |
|---|---|
| `addrspace` | The `addrspace` keyword. TODO add documentation for addrspace |
| `align` | `align` can be used to specify the alignment of a pointer. It can also be used after a variable or function declaration to specify the alignment of pointers to that variable or function. See also Alignment |
| `allowzero` | The pointer attribute `allowzero` allows a pointer to have address zero. See also allowzero |
| `and` | The boolean operator `and`. See also Operators |
| `anyframe` | `anyframe` can be used as a type for variables which hold pointers to function frames. See also Async Functions |
| `anytype` | Function parameters can be declared with `anytype` in place of the type. The type will be inferred where the function is called. See also Function Parameter Type Inference |
| `asm` | `asm` begins an inline assembly expression. This allows for directly controlling the machine code generated on compilation. See also Assembly |
| `break` | `break` can be used with a block label to return a value from the block. It can also be used to exit a loop before iteration completes naturally. See also Blocks, while, for |
| `callconv` | `callconv` can be used to specify the calling convention in a function type. See also Functions |
| `catch` | `catch` can be used to evaluate an expression if the expression before it evaluates to an error. The expression after the `catch` can optionally capture the error value. See also catch, Operators |
| `comptime` | `comptime` before a declaration can be used to label variables or function parameters as known at compile time. It can also be used to guarantee an expression is run at compile time. See also comptime |
| `const` | `const` declares a variable that can not be modified. Used as a pointer attribute, it denotes the value referenced by the pointer cannot be modified. See also Variables |
| `continue` | `continue` can be used in a loop to jump back to the beginning of the loop. See also while, for |
| `defer` | `defer` will execute an expression when control flow leaves the current block. See also defer |
| `else` | `else` can be used to provide an alternate branch for `if`, `switch`, `while`, and `for` expressions. If used after an if expression, the else branch will be executed if the test value returns false, null, or an error. If used within a switch expression, the else branch will be executed if the test value matches no other cases. If used after a loop expression, the else branch will be executed if the loop finishes without breaking. See also if, switch, while, for |
| `enum` | `enum` defines an enum type. See also enum |
| `errdefer` | `errdefer` will execute an expression when control flow leaves the current block if the function returns an error, the errdefer expression can capture the unwrapped value. See also errdefer |
| `error` | `error` defines an error type. See also Errors |
| `export` | `export` makes a function or variable externally visible in the generated object file. Exported functions default to the C calling convention. See also Functions |
| `extern` | `extern` can be used to declare a function or variable that will be resolved at link time, when linking statically or at runtime, when linking dynamically. See also Functions |
| `fn` | `fn` declares a function. See also Functions |
| `for` | A `for` expression can be used to iterate over the elements of a slice, array, or tuple. See also for |
| `if` | An `if` expression can test boolean expressions, optional values, or error unions. For optional values or error unions, the if expression can capture the unwrapped value. See also if |
| `inline` | `inline` can be used to label a loop expression such that it will be unrolled at compile time. It can also be used to force a function to be inlined at all call sites. See also inline while, inline for, Functions |
| `linksection` | The `linksection` keyword can be used to specify what section the function or global variable will be put into (e.g. `.text`). |
| `noalias` | The `noalias` keyword. TODO add documentation for noalias |
| `noinline` | `noinline` disallows function to be inlined in all call sites. See also Functions |
| `nosuspend` | The `nosuspend` keyword can be used in front of a block, statement or expression, to mark a scope where no suspension points are reached. In particular, inside a `nosuspend` scope: Using the `suspend` keyword results in a compile error. Using `await` on a function frame which hasn't completed yet results in safety-checked Illegal Behavior. Calling an async function may result in safety-checked Illegal Behavior, because it's equivalent to `await async some_async_fn()`, which contains an `await`. Code inside a `nosuspend` scope does not cause the enclosing function to become an async function. See also Async Functions |
| `opaque` | `opaque` defines an opaque type. See also opaque |
| `or` | The boolean operator `or`. See also Operators |
| `orelse` | `orelse` can be used to evaluate an expression if the expression before it evaluates to null. See also Optionals, Operators |
| `packed` | The `packed` keyword before a struct definition changes the struct's in-memory layout to the guaranteed `packed` layout. See also packed struct |
| `pub` | The `pub` in front of a top level declaration makes the declaration available to reference from a different file than the one it is declared in. See also import |
| `resume` | `resume` will continue execution of a function frame after the point the function was suspended. |
| `return` | `return` exits a function with a value. See also Functions |
| `struct` | `struct` defines a struct. See also struct |
| `suspend` | `suspend` will cause control flow to return to the call site or resumer of the function. `suspend` can also be used before a block within a function, to allow the function access to its frame before control flow returns to the call site. |
| `switch` | A `switch` expression can be used to test values of a common type. `switch` cases can capture field values of a Tagged union. See also switch |
| `test` | The `test` keyword can be used to denote a top-level block of code used to make sure behavior meets expectations. See also Zig Test |
| `threadlocal` | `threadlocal` can be used to specify a variable as thread-local. See also Thread Local Variables |
| `try` | `try` evaluates an error union expression. If it is an error, it returns from the current function with the same error. Otherwise, the expression results in the unwrapped value. See also try |
| `union` | `union` defines a union. See also union |
| `unreachable` | `unreachable` can be used to assert that control flow will never happen upon a particular location. Depending on the build mode, `unreachable` may emit a panic. Emits a panic in `Debug` and `ReleaseSafe` mode, or when using zig test. Does not emit a panic in `ReleaseFast` and `ReleaseSmall` mode. See also unreachable |
| `var` | `var` declares a variable that may be modified. See also Variables |
| `volatile` | `volatile` can be used to denote loads or stores of a pointer have side effects. It can also modify an inline assembly expression to denote it has side effects. See also volatile, Assembly |
| `while` | A `while` expression can be used to repeatedly test a boolean, optional, or error union expression, and cease looping when that expression evaluates to false, null, or an error, respectively. See also while |
