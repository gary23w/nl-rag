---
title: "Documentation (part 5/10)"
source: https://ziglang.org/documentation/master/
domain: zig
license: MIT
tags: zig, comptime
fetched: 2026-07-02
part: 5/10
---

## Zero Bit Types

For some types, @sizeOf is 0:

- void
- The integer type `u0`.
- Arrays and Vectors with len 0, or with an element type that is a zero bit type.
- An enum with only 1 tag.
- A struct with all fields being zero bit types.
- A union with only 1 field which is a zero bit type.

These types can only ever have one possible value, and thus require 0 bits to represent. Code that makes use of these types is not included in the final generated code:

```
export fn entry() void {
    var x: void = {};
    var y: void = {};
    x = y;
    y = x;
}
```

When this turns into machine code, there is no code generated in the body of `entry`, even in Debug mode. For example, on x86_64:

```
0000000000000010 <entry>:
  10:	55                   	push   %rbp
  11:	48 89 e5             	mov    %rsp,%rbp
  14:	5d                   	pop    %rbp
  15:	c3                   	retq   
```

These assembly instructions do not have any code associated with the void values - they only perform the function call prologue and epilogue.

### void

`void` can be useful for instantiating generic types. For example, given a `Map(Key, Value)`, one can pass `void` for the `Value` type to make it into a `Set`:

```
const std = @import("std");
const expect = std.testing.expect;

test "turn HashMap into a set with void" {
    var map = std.AutoHashMap(i32, void).init(std.testing.allocator);
    defer map.deinit();

    try map.put(1, {});
    try map.put(2, {});

    try expect(map.contains(2));
    try expect(!map.contains(3));

    _ = map.remove(2);
    try expect(!map.contains(2));
}
```

```
$ zig test test_void_in_hashmap.zig
1/1 test_void_in_hashmap.test.turn HashMap into a set with void...OK
All 1 tests passed.
```

Note that this is different from using a dummy value for the hash map value. By using `void` as the type of the value, the hash map entry type has no value field, and thus the hash map takes up less space. Further, all the code that deals with storing and loading the value is deleted, as seen above.

`void` is distinct from `anyopaque`. `void` has a known size of 0 bytes, and `anyopaque` has an unknown, but non-zero, size.

Expressions of type `void` are the only ones whose value can be ignored. For example, ignoring a non-`void` expression is a compile error:

```
test "ignoring expression value" {
    foo();
}

fn foo() i32 {
    return 1234;
}
```

```
$ zig test test_expression_ignored.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_expression_ignored.zig:2:8: error: value of type 'i32' ignored
    foo();
    ~~~^~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_expression_ignored.zig:2:8: note: all non-void values must be used
/home/ci/work/zig-bootstrap/zig/doc/langref/test_expression_ignored.zig:2:8: note: to discard the value, assign it to '_'
```

However, if the expression has type `void`, there will be no error. Expression results can be explicitly ignored by assigning them to `_`.

```
test "void is ignored" {
    returnsVoid();
}

test "explicitly ignoring expression value" {
    _ = foo();
}

fn returnsVoid() void {}

fn foo() i32 {
    return 1234;
}
```

```
$ zig test test_void_ignored.zig
1/2 test_void_ignored.test.void is ignored...OK
2/2 test_void_ignored.test.explicitly ignoring expression value...OK
All 2 tests passed.
```


## Result Location Semantics

During compilation, every Zig expression and sub-expression is assigned optional result location information. This information dictates what type the expression should have (its result type), and where the resulting value should be placed in memory (its result location). The information is optional in the sense that not every expression has this information: assignment to `_`, for instance, does not provide any information about the type of an expression, nor does it provide a concrete memory location to place it in.

As a motivating example, consider the statement `const x: u32 = 42;`. The type annotation here provides a result type of `u32` to the initialization expression `42`, instructing the compiler to coerce this integer (initially of type `comptime_int`) to this type. We will see more examples shortly.

This is not an implementation detail: the logic outlined above is codified into the Zig language specification, and is the primary mechanism of type inference in the language. This system is collectively referred to as "Result Location Semantics".

### Result Types

Result types are propagated recursively through expressions where possible. For instance, if the expression `&e` has result type `*u32`, then `e` is given a result type of `u32`, allowing the language to perform this coercion before taking a reference.

The result type mechanism is utilized by casting builtins such as `@intCast`. Rather than taking as an argument the type to cast to, these builtins use their result type to determine this information. The result type is often known from context; where it is not, the `@as` builtin can be used to explicitly provide a result type.

We can break down the result types for each component of a simple expression as follows:

```
const expectEqual = @import("std").testing.expectEqual;
test "result type propagates through struct initializer" {
    const S = struct { x: u32 };
    const val: u64 = 123;
    const s: S = .{ .x = @intCast(val) };
    
    
    
    try expectEqual(@as(u32, 123), s.x);
}
```

```
$ zig test result_type_propagation.zig
1/1 result_type_propagation.test.result type propagates through struct initializer...OK
All 1 tests passed.
```

This result type information is useful for the aforementioned cast builtins, as well as to avoid the construction of pre-coercion values, and to avoid the need for explicit type coercions in some cases. The following table details how some common expressions propagate result types, where `x` and `y` are arbitrary sub-expressions.

| Expression | Parent Result Type | Sub-expression Result Type |
|---|---|---|
| `const val: T = x` | - | `x` is a `T` |
| `var val: T = x` | - | `x` is a `T` |
| `val = x` | - | `x` is a `@TypeOf(val)` |
| `@as(T, x)` | - | `x` is a `T` |
| `&x` | `*T` | `x` is a `T` |
| `&x` | `[]T` | `x` is some array of `T` |
| `f(x)` | - | `x` has the type of the first parameter of `f` |
| `.{x}` | `T` | `x` is a `@FieldType(T, "0")` |
| `.{ .a = x }` | `T` | `x` is a `@FieldType(T, "a")` |
| `T{x}` | - | `x` is a `@FieldType(T, "0")` |
| `T{ .a = x }` | - | `x` is a `@FieldType(T, "a")` |
| `@Int(x, y)` | - | `x` is a `std.lang.Signedness`, `y` is a `u16` |
| `@typeInfo(x)` | - | `x` is a `type` |
| `x << y` | - | `y` is a `std.math.Log2IntCeil(@TypeOf(x))` |

### Result Locations

In addition to result type information, every expression may be optionally assigned a result location: a pointer to which the value must be directly written. This system can be used to prevent intermediate copies when initializing data structures, which can be important for types which must have a fixed memory address ("pinned" types).

When compiling the simple assignment expression `x = e`, many languages would create the temporary value `e` on the stack, and then assign it to `x`, potentially performing a type coercion in the process. Zig approaches this differently. The expression `e` is given a result type matching the type of `x`, and a result location of `&x`. For many syntactic forms of `e`, this has no practical impact. However, it can have important semantic effects when working with more complex syntax forms.

For instance, if the expression `.{ .a = x, .b = y }` has a result location of `ptr`, then `x` is given a result location of `&ptr.a`, and `y` a result location of `&ptr.b`. Without this system, this expression would construct a temporary struct value entirely on the stack, and only then copy it to the destination address. In essence, Zig desugars the assignment `foo = .{ .a = x, .b = y }` to the two statements `foo.a = x; foo.b = y;`.

This can sometimes be important when assigning an aggregate value where the initialization expression depends on the previous value of the aggregate. The easiest way to demonstrate this is by attempting to swap fields of a struct or array - the following logic looks sound, but in fact is not:

```
const expectEqual = @import("std").testing.expectEqual;
test "attempt to swap array elements with array initializer" {
    var arr: [2]u32 = .{ 1, 2 };
    arr = .{ arr[1], arr[0] };
    
    
    
    
    try expectEqual(2, arr[0]); 
    try expectEqual(1, arr[1]); 
}
```

```
$ zig test result_location_interfering_with_swap.zig
1/1 result_location_interfering_with_swap.test.attempt to swap array elements with array initializer...expected 1, found 2
FAIL (TestExpectedEqual)
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/testing.zig:111:17: 0x124d104 in expectEqualInner__anon_40499 (std.zig)
                return error.TestExpectedEqual;
                ^
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/testing.zig:75:5: 0x124d27d in expectEqual (result_location_interfering_with_swap.zig)
    return expectEqualInner(T, expected, actual);
    ^
/home/ci/work/zig-bootstrap/zig/doc/langref/result_location_interfering_with_swap.zig:10:5: 0x124d2c4 in test.attempt to swap array elements with array initializer (result_location_interfering_with_swap.zig)
    try expectEqual(1, arr[1]); // fails
    ^
0 passed; 0 skipped; 1 failed.
error: the following test command failed with exit code 1:
/home/ci/work/zig-bootstrap/out/zig-local-cache/o/216c1c81a0c1582f1a1a317a21999ae9/test --seed=0x26fba9d2
```

The following table details how some common expressions propagate result locations, where `x` and `y` are arbitrary sub-expressions. Note that some expressions cannot provide meaningful result locations to sub-expressions, even if they themselves have a result location.

| Expression | Result Location | Sub-expression Result Locations |
|---|---|---|
| `const val: T = x` | - | `x` has result location `&val` |
| `var val: T = x` | - | `x` has result location `&val` |
| `val = x` | - | `x` has result location `&val` |
| `@as(T, x)` | `ptr` | `x` has no result location |
| `&x` | `ptr` | `x` has no result location |
| `f(x)` | `ptr` | `x` has no result location |
| `.{x}` | `ptr` | `x` has result location `&ptr[0]` |
| `.{ .a = x }` | `ptr` | `x` has result location `&ptr.a` |
| `T{x}` | `ptr` | `x` has no result location (typed initializers do not propagate result locations) |
| `T{ .a = x }` | `ptr` | `x` has no result location (typed initializers do not propagate result locations) |
| `@Int(x, y)` | - | `x` and `y` do not have result locations |
| `@typeInfo(x)` | `ptr` | `x` has no result location |
| `x << y` | `ptr` | `x` and `y` do not have result locations |


## comptime

Zig places importance on the concept of whether an expression is known at compile-time. There are a few different places this concept is used, and these building blocks are used to keep the language small, readable, and powerful.

### Introducing the Compile-Time Concept

#### Compile-Time Parameters

Compile-time parameters is how Zig implements generics. It is compile-time duck typing.

```
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}
fn gimmeTheBiggerFloat(a: f32, b: f32) f32 {
    return max(f32, a, b);
}
fn gimmeTheBiggerInteger(a: u64, b: u64) u64 {
    return max(u64, a, b);
}
```

In Zig, types are first-class citizens. They can be assigned to variables, passed as parameters to functions, and returned from functions. However, they can only be used in expressions which are known at *compile-time*, which is why the parameter `T` in the above snippet must be marked with `comptime`.

A `comptime` parameter means that:

- At the callsite, the value must be known at compile-time, or it is a compile error.
- In the function definition, the value is known at compile-time.

For example, if we were to introduce another function to the above snippet:

```
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}
test "try to pass a runtime type" {
    foo(false);
}
fn foo(condition: bool) void {
    const result = max(if (condition) f32 else u64, 1234, 5678);
    _ = result;
}
```

```
$ zig test test_unresolved_comptime_value.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unresolved_comptime_value.zig:8:28: error: unable to resolve comptime value
    const result = max(if (condition) f32 else u64, 1234, 5678);
                           ^~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unresolved_comptime_value.zig:8:24: note: argument to comptime parameter must be comptime-known
    const result = max(if (condition) f32 else u64, 1234, 5678);
                       ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_unresolved_comptime_value.zig:1:8: note: parameter declared comptime here
fn max(comptime T: type, a: T, b: T) T {
       ^~~~~~~~
referenced by:
    test.try to pass a runtime type: /home/ci/work/zig-bootstrap/zig/doc/langref/test_unresolved_comptime_value.zig:5:8
```

This is an error because the programmer attempted to pass a value only known at run-time to a function which expects a value known at compile-time.

Another way to get an error is if we pass a type that violates the type checker when the function is analyzed. This is what it means to have *compile-time duck typing*.

For example:

```
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}
test "try to compare bools" {
    _ = max(bool, true, false);
}
```

```
$ zig test test_comptime_mismatched_type.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_mismatched_type.zig:2:18: error: operator > not allowed for type 'bool'
    return if (a > b) a else b;
               ~~^~~
referenced by:
    test.try to compare bools: /home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_mismatched_type.zig:5:12
```

On the flip side, inside the function definition with the `comptime` parameter, the value is known at compile-time. This means that we actually could make this work for the bool type if we wanted to:

```
fn max(comptime T: type, a: T, b: T) T {
    if (T == bool) {
        return a or b;
    } else if (a > b) {
        return a;
    } else {
        return b;
    }
}
test "try to compare bools" {
    try @import("std").testing.expectEqual(true, max(bool, false, true));
}
```

```
$ zig test test_comptime_max_with_bool.zig
1/1 test_comptime_max_with_bool.test.try to compare bools...OK
All 1 tests passed.
```

This works because Zig implicitly inlines `if` expressions when the condition is known at compile-time, and the compiler guarantees that it will skip analysis of the branch not taken.

This means that the actual function generated for `max` in this situation looks like this:

```
fn max(a: bool, b: bool) bool {
    {
        return a or b;
    }
}
```

All the code that dealt with compile-time known values is eliminated and we are left with only the necessary run-time code to accomplish the task.

This works the same way for `switch` expressions - they are implicitly inlined when the target expression is compile-time known.

#### Compile-Time Variables

In Zig, the programmer can label variables as `comptime`. This guarantees to the compiler that every load and store of the variable is performed at compile-time. Any violation of this results in a compile error.

This combined with the fact that we can `inline` loops allows us to write a function which is partially evaluated at compile-time and partially at run-time.

For example:

```
const expectEqual = @import("std").testing.expectEqual;

const CmdFn = struct {
    name: []const u8,
    func: fn (i32) i32,
};

const cmd_fns = [_]CmdFn{
    CmdFn{ .name = "one", .func = one },
    CmdFn{ .name = "two", .func = two },
    CmdFn{ .name = "three", .func = three },
};
fn one(value: i32) i32 {
    return value + 1;
}
fn two(value: i32) i32 {
    return value + 2;
}
fn three(value: i32) i32 {
    return value + 3;
}

fn performFn(comptime prefix_char: u8, start_value: i32) i32 {
    var result: i32 = start_value;
    comptime var i = 0;
    inline while (i < cmd_fns.len) : (i += 1) {
        if (cmd_fns[i].name[0] == prefix_char) {
            result = cmd_fns[i].func(result);
        }
    }
    return result;
}

test "perform fn" {
    try expectEqual(6, performFn('t', 1));
    try expectEqual(1, performFn('o', 0));
    try expectEqual(99, performFn('w', 99));
}
```

```
$ zig test test_comptime_evaluation.zig
1/1 test_comptime_evaluation.test.perform fn...OK
All 1 tests passed.
```

This example is a bit contrived, because the compile-time evaluation component is unnecessary; this code would work fine if it was all done at run-time. But it does end up generating different code. In this example, the function `performFn` is generated three different times, for the different values of `prefix_char` provided:

```
fn performFn(start_value: i32) i32 {
    var result: i32 = start_value;
    result = two(result);
    result = three(result);
    return result;
}
```

```
fn performFn(start_value: i32) i32 {
    var result: i32 = start_value;
    result = one(result);
    return result;
}
```

```
fn performFn(start_value: i32) i32 {
    var result: i32 = start_value;
    _ = &result;
    return result;
}
```

Note that this happens even in a debug build. This is not a way to write more optimized code, but it is a way to make sure that what *should* happen at compile-time, *does* happen at compile-time. This catches more errors and allows expressiveness that in other languages requires using macros, generated code, or a preprocessor to accomplish.

#### Compile-Time Expressions

In Zig, it matters whether a given expression is known at compile-time or run-time. A programmer can use a `comptime` expression to guarantee that the expression will be evaluated at compile-time. If this cannot be accomplished, the compiler will emit an error. For example:

```
extern fn exit() noreturn;

test "foo" {
    comptime {
        exit();
    }
}
```

```
$ zig test test_comptime_call_extern_function.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_call_extern_function.zig:5:13: error: comptime call of extern function
        exit();
        ~~~~^~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_comptime_call_extern_function.zig:4:5: note: 'comptime' keyword forces comptime evaluation
    comptime {
    ^~~~~~~~
```

It doesn't make sense that a program could call `exit()` (or any other external function) at compile-time, so this is a compile error. However, a `comptime` expression does much more than sometimes cause a compile error.

Within a `comptime` expression:

- All variables are `comptime` variables.
- All `if`, `while`, `for`, and `switch` expressions are evaluated at compile-time, or emit a compile error if this is not possible.
- All `return` and `try` expressions are invalid (unless the function itself is called at compile-time).
- All code with runtime side effects or depending on runtime values emits a compile error.
- All function calls cause the compiler to interpret the function at compile-time, emitting a compile error if the function tries to do something that has global runtime side effects.

This means that a programmer can create a function which is called both at compile-time and run-time, with no modification to the function required.

Let's look at an example:

```
const expectEqual = @import("std").testing.expectEqual;

fn fibonacci(index: u32) u32 {
    if (index < 2) return index;
    return fibonacci(index - 1) + fibonacci(index - 2);
}

test "fibonacci" {
    
    try expectEqual(13, fibonacci(7));

    
    try comptime expectEqual(13, fibonacci(7));
}
```

```
$ zig test test_fibonacci_recursion.zig
1/1 test_fibonacci_recursion.test.fibonacci...OK
All 1 tests passed.
```

Imagine if we had forgotten the base case of the recursive function and tried to run the tests:

```
const expectEqual = @import("std").testing.expectEqual;

fn fibonacci(index: u32) u32 {
    
    return fibonacci(index - 1) + fibonacci(index - 2);
}

test "fibonacci" {
    try comptime expectEqual(13, fibonacci(7));
}
```

```
$ zig test test_fibonacci_comptime_overflow.zig
/home/ci/work/zig-bootstrap/zig/doc/langref/test_fibonacci_comptime_overflow.zig:5:28: error: overflow of integer type 'u32' with value '-1'
    return fibonacci(index - 1) + fibonacci(index - 2);
                     ~~~~~~^~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_fibonacci_comptime_overflow.zig:5:21: note: called at comptime here (7 times)
    return fibonacci(index - 1) + fibonacci(index - 2);
           ~~~~~~~~~^~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_fibonacci_comptime_overflow.zig:9:43: note: called at comptime here
    try comptime expectEqual(13, fibonacci(7));
                                 ~~~~~~~~~^~~
```

The compiler produces an error which is a stack trace from trying to evaluate the function at compile-time.

Luckily, we used an unsigned integer, and so when we tried to subtract 1 from 0, it triggered Illegal Behavior, which is always a compile error if the compiler knows it happened. But what would have happened if we used a signed integer?

```
const assert = @import("std").debug.assert;

fn fibonacci(index: i32) i32 {
    
    return fibonacci(index - 1) + fibonacci(index - 2);
}

test "fibonacci" {
    try comptime assert(fibonacci(7) == 13);
}
```

The compiler is supposed to notice that evaluating this function at compile-time took more than 1000 branches, and thus emits an error and gives up. If the programmer wants to increase the budget for compile-time computation, they can use a built-in function called @setEvalBranchQuota to change the default number 1000 to something else.

However, there is a design flaw in the compiler causing it to stack overflow instead of having the proper behavior here. I'm terribly sorry about that. I hope to get this resolved before the next release.

What if we fix the base case, but put the wrong value in the `expect` line?

```
const assert = @import("std").debug.assert;

fn fibonacci(index: i32) i32 {
    if (index < 2) return index;
    return fibonacci(index - 1) + fibonacci(index - 2);
}

test "fibonacci" {
    try comptime assert(fibonacci(7) == 99999);
}
```

```
$ zig test test_fibonacci_comptime_unreachable.zig
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/debug.zig:435:14: error: reached unreachable code
    if (!ok) unreachable; // assertion failure
             ^~~~~~~~~~~
/home/ci/work/zig-bootstrap/zig/doc/langref/test_fibonacci_comptime_unreachable.zig:9:24: note: called at comptime here
    try comptime assert(fibonacci(7) == 99999);
                 ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
```

At Namespace level (outside of any function), all expressions are implicitly `comptime` expressions. This means that we can use functions to initialize complex constant data. For example:

```
const first_25_primes = firstNPrimes(25);
const sum_of_first_25_primes = sum(&first_25_primes);

fn firstNPrimes(comptime n: usize) [n]i32 {
    var prime_list: [n]i32 = undefined;
    var next_index: usize = 0;
    var test_number: i32 = 2;
    while (next_index < prime_list.len) : (test_number += 1) {
        var test_prime_index: usize = 0;
        var is_prime = true;
        while (test_prime_index < next_index) : (test_prime_index += 1) {
            if (test_number % prime_list[test_prime_index] == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            prime_list[next_index] = test_number;
            next_index += 1;
        }
    }
    return prime_list;
}

fn sum(numbers: []const i32) i32 {
    var result: i32 = 0;
    for (numbers) |x| {
        result += x;
    }
    return result;
}

test "variable values" {
    try @import("std").testing.expectEqual(1060, sum_of_first_25_primes);
}
```

```
$ zig test test_namespace-level_comptime_expressions.zig
1/1 test_namespace-level_comptime_expressions.test.variable values...OK
All 1 tests passed.
```

When we compile this program, Zig generates the constants with the answer pre-computed. Here are the lines from the generated LLVM IR:

```
@0 = internal unnamed_addr constant [25 x i32] [i32 2, i32 3, i32 5, i32 7, i32 11, i32 13, i32 17, i32 19, i32 23, i32 29, i32 31, i32 37, i32 41, i32 43, i32 47, i32 53, i32 59, i32 61, i32 67, i32 71, i32 73, i32 79, i32 83, i32 89, i32 97]
@1 = internal unnamed_addr constant i32 1060
```

Note that we did not have to do anything special with the syntax of these functions. For example, we could call the `sum` function as is with a slice of numbers whose length and values were only known at run-time.

### Generic Data Structures

Zig uses comptime capabilities to implement generic data structures without introducing any special-case syntax.

Here is an example of a generic `List` data structure.

```
fn List(comptime T: type) type {
    return struct {
        items: []T,
        len: usize,
    };
}

var buffer: [10]i32 = undefined;
var list = List(i32){
    .items = &buffer,
    .len = 0,
};
```

That's it. It's a function that returns an anonymous `struct`. For the purposes of error messages and debugging, Zig infers the name `"List(i32)"` from the function name and parameters invoked when creating the anonymous struct.

To explicitly give a type a name, we assign it to a constant.

```
const Node = struct {
    next: ?*Node,
    name: []const u8,
};

var node_a = Node{
    .next = null,
    .name = "Node A",
};

var node_b = Node{
    .next = &node_a,
    .name = "Node B",
};
```

In this example, the `Node` struct refers to itself. This works because all top level declarations are order-independent. As long as the compiler can determine the size of the struct, it is free to refer to itself. In this case, `Node` refers to itself as a pointer, which has a well-defined size at compile time, so it works fine.

### Case Study: print in Zig

Putting all of this together, let's see how `print` works in Zig.

```
const print = @import("std").debug.print;

const a_number: i32 = 1234;
const a_string = "foobar";

pub fn main() void {
    print("here is a string: '{s}' here is a number: {}\n", .{ a_string, a_number });
}
```

```
$ zig build-exe print.zig
$ ./print
here is a string: 'foobar' here is a number: 1234
```

Let's crack open the implementation of this and see how it works:

```
const Writer = struct {
    
    pub fn print(self: *Writer, comptime format: []const u8, args: anytype) anyerror!void {
        const State = enum {
            start,
            open_brace,
            close_brace,
        };

        comptime var start_index: usize = 0;
        comptime var state = State.start;
        comptime var next_arg: usize = 0;

        inline for (format, 0..) |c, i| {
            switch (state) {
                State.start => switch (c) {
                    '{' => {
                        if (start_index < i) try self.write(format[start_index..i]);
                        state = State.open_brace;
                    },
                    '}' => {
                        if (start_index < i) try self.write(format[start_index..i]);
                        state = State.close_brace;
                    },
                    else => {},
                },
                State.open_brace => switch (c) {
                    '{' => {
                        state = State.start;
                        start_index = i;
                    },
                    '}' => {
                        try self.printValue(args[next_arg]);
                        next_arg += 1;
                        state = State.start;
                        start_index = i + 1;
                    },
                    's' => {
                        continue;
                    },
                    else => @compileError("Unknown format character: " ++ [1]u8{c}),
                },
                State.close_brace => switch (c) {
                    '}' => {
                        state = State.start;
                        start_index = i;
                    },
                    else => @compileError("Single '}' encountered in format string"),
                },
            }
        }
        comptime {
            if (args.len != next_arg) {
                @compileError("Unused arguments");
            }
            if (state != State.start) {
                @compileError("Incomplete format string: " ++ format);
            }
        }
        if (start_index < format.len) {
            try self.write(format[start_index..format.len]);
        }
        try self.flush();
    }

    fn write(self: *Writer, value: []const u8) !void {
        _ = self;
        _ = value;
    }
    pub fn printValue(self: *Writer, value: anytype) !void {
        _ = self;
        _ = value;
    }
    fn flush(self: *Writer) !void {
        _ = self;
    }
};
```

This is a proof of concept implementation; the actual function in the standard library has more formatting capabilities.

Note that this is not hard-coded into the Zig compiler; this is userland code in the standard library.

When this function is analyzed from our example code above, Zig partially evaluates the function and emits a function that actually looks like this:

```
pub fn print(self: *Writer, arg0: []const u8, arg1: i32) !void {
    try self.write("here is a string: '");
    try self.printValue(arg0);
    try self.write("' here is a number: ");
    try self.printValue(arg1);
    try self.write("\n");
    try self.flush();
}
```

`printValue` is a function that takes a parameter of any type, and does different things depending on the type:

```
const Writer = struct {
    pub fn printValue(self: *Writer, value: anytype) !void {
        switch (@typeInfo(@TypeOf(value))) {
            .int => {
                return self.writeInt(value);
            },
            .float => {
                return self.writeFloat(value);
            },
            .pointer => {
                return self.write(value);
            },
            else => {
                @compileError("Unable to print type '" ++ @typeName(@TypeOf(value)) ++ "'");
            },
        }
    }

    fn write(self: *Writer, value: []const u8) !void {
        _ = self;
        _ = value;
    }
    fn writeInt(self: *Writer, value: anytype) !void {
        _ = self;
        _ = value;
    }
    fn writeFloat(self: *Writer, value: anytype) !void {
        _ = self;
        _ = value;
    }
};
```

And now, what happens if we give too many arguments to `print`?

```
const print = @import("std").debug.print;

const a_number: i32 = 1234;
const a_string = "foobar";

test "print too many arguments" {
    print("here is a string: '{s}' here is a number: {}\n", .{
        a_string,
        a_number,
        a_number,
    });
}
```

```
$ zig test test_print_too_many_args.zig
/home/ci/work/zig-bootstrap/out/host/lib/zig/std/Io/Writer.zig:741:18: error: unused argument in 'here is a string: '{s}' here is a number: {}
                                                                              '
            1 => @compileError("unused argument in '" ++ fmt ++ "'"),
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
referenced by:
    print__anon_40488: /home/ci/work/zig-bootstrap/out/host/lib/zig/std/debug.zig:323:39
    test.print too many arguments: /home/ci/work/zig-bootstrap/zig/doc/langref/test_print_too_many_args.zig:7:10
```

Zig gives programmers the tools needed to protect themselves against their own mistakes.

Zig doesn't care whether the format argument is a string literal, only that it is a compile-time known value that can be coerced to a `[]const u8`:

```
const print = @import("std").debug.print;

const a_number: i32 = 1234;
const a_string = "foobar";
const fmt = "here is a string: '{s}' here is a number: {}\n";

pub fn main() void {
    print(fmt, .{ a_string, a_number });
}
```

```
$ zig build-exe print_comptime-known_format.zig
$ ./print_comptime-known_format
here is a string: 'foobar' here is a number: 1234
```

This works fine.

Zig does not special case string formatting in the compiler and instead exposes enough power to accomplish this task in userland. It does so without introducing another language on top of Zig, such as a macro language or a preprocessor language. It's Zig all the way down.

See also:

- inline while
- inline for


## Assembly

For some use cases, it may be necessary to directly control the machine code generated by Zig programs, rather than relying on Zig's code generation. For these cases, one can use inline assembly. Here is an example of implementing Hello, World on x86_64 Linux using inline assembly:

```
pub fn main() noreturn {
    const msg = "hello world\n";
    _ = syscall3(SYS_write, STDOUT_FILENO, @intFromPtr(msg), msg.len);
    _ = syscall1(SYS_exit, 0);
    unreachable;
}

pub const SYS_write = 1;
pub const SYS_exit = 60;

pub const STDOUT_FILENO = 1;

pub fn syscall1(number: usize, arg1: usize) usize {
    return asm volatile ("syscall"
        : [ret] "={rax}" (-> usize),
        : [number] "{rax}" (number),
          [arg1] "{rdi}" (arg1),
        : .{ .rcx = true, .r11 = true });
}

pub fn syscall3(number: usize, arg1: usize, arg2: usize, arg3: usize) usize {
    return asm volatile ("syscall"
        : [ret] "={rax}" (-> usize),
        : [number] "{rax}" (number),
          [arg1] "{rdi}" (arg1),
          [arg2] "{rsi}" (arg2),
          [arg3] "{rdx}" (arg3),
        : .{ .rcx = true, .r11 = true });
}
```

```
$ zig build-exe inline_assembly.zig -target x86_64-linux
$ ./inline_assembly
hello world
```

Dissecting the syntax:

```
pub fn syscall1(number: usize, arg1: usize) usize {
    
    
    return asm
    
    
    
    
    volatile (
    
    
    
    
    
    
    
    
        \\syscall
        
        
        
        
        
        :
        
        
        
          [ret]
          
          
          
          
          
          
          
          "={rax}"
          
          
          
          
          (-> usize),
          
          
          
          
          
        : [number] "{rax}" (number),
          [arg1] "{rdi}" (arg1),
          
          
          
          
          
          
          
        : .{ .rcx = true, .r11 = true });
}
```

For x86 and x86_64 targets, the syntax is AT&T syntax, rather than the more popular Intel syntax. This is due to technical constraints; assembly parsing is provided by LLVM and its support for Intel syntax is buggy and not well tested.

Some day Zig may have its own assembler. This would allow it to integrate more seamlessly into the language, as well as be compatible with the popular NASM syntax. This documentation section will be updated before 1.0.0 is released, with a conclusive statement about the status of AT&T vs Intel/NASM syntax.

### Output Constraints

Output constraints are still considered to be unstable in Zig, and so LLVM documentation and GCC documentation must be used to understand the semantics.

Note that some breaking changes to output constraints are planned with issue #215.

### Input Constraints

Input constraints are still considered to be unstable in Zig, and so LLVM documentation and GCC documentation must be used to understand the semantics.

Note that some breaking changes to input constraints are planned with issue #215.

### Clobbers

Clobbers are the set of registers whose values will not be preserved by the execution of the assembly code. These do not include output or input registers. The special clobber value of `"memory"` means that the assembly causes writes to arbitrary undeclared memory locations - not only the memory pointed to by a declared indirect output.

Failure to declare the full set of clobbers for a given inline assembly expression is unchecked Illegal Behavior.

### Global Assembly

When an assembly expression occurs in a Namespace level comptime block, this is **global assembly**.

This kind of assembly has different rules than inline assembly. First, `volatile` is not valid because all global assembly is unconditionally included. Second, there are no inputs, outputs, or clobbers. All global assembly is concatenated verbatim into one long string and assembled together. There are no template substitution rules regarding `%` as there are in inline assembly expressions.

```
const std = @import("std");
const expectEqual = std.testing.expectEqual;

comptime {
    asm (
        \\.global my_func;
        \\.type my_func, @function;
        \\my_func:
        \\  lea (%rdi,%rsi,1),%eax
        \\  retq
    );
}

extern fn my_func(a: i32, b: i32) i32;

test "global assembly" {
    try expectEqual(46, my_func(12, 34));
}
```

```
$ zig test test_global_assembly.zig -target x86_64-linux -fllvm
1/1 test_global_assembly.test.global assembly...OK
All 1 tests passed.
```


## Atomics

TODO: @atomic rmw

TODO: builtin atomic memory ordering enum

See also:

- @atomicLoad
- @atomicStore
- @atomicRmw
- @cmpxchgWeak
- @cmpxchgStrong


## Async Functions

Async functions regressed with the release of 0.11.0. The current plan is to reintroduce them as a lower level primitive that powers I/O implementations.

Tracking issue: Proposal: stackless coroutines as low-level primitives
