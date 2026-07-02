---
title: "LLVM Language Reference Manual (part 7/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 7/20
---

# LLVM Language Reference Manual

Any other usage is an error in the IR verifier.

Note that in order to support outputs along indirect edges, LLVM may need to split critical edges, which may require synthesizing a replacement block for the `indirect labels`. Therefore, the address of a label as seen by another `callbr` instruction, or for a blockaddress constant, may not be equal to the address provided for the same block to this instruction’s `indirect labels` operand. The assembly code may only transfer control to addresses provided via this instruction’s `indirect labels`.

On target architectures that implement branch target enforcement by requiring indirect (register-controlled) branch instructions to jump only to locations marked by a special instruction (such as AArch64 `bti`), the called code is expected not to use such an indirect branch to transfer control to the locations in `indirect labels`. Therefore, including a label in the `indirect labels` of a `callbr` does not require the compiler to put a `bti` or equivalent instruction at the label.

##### Arguments:

This instruction requires several arguments:

1. The optional “cconv” marker indicates which calling convention the call should use. If none is specified, the call defaults to using C calling conventions.
2. The optional Parameter Attributes list for return values. Only ‘`zeroext`’, ‘`signext`’, ‘`noext`’, and ‘`inreg`’ attributes are valid here.
3. The optional addrspace attribute can be used to indicate the address space of the called function. If it is not specified, the program address space from the datalayout string will be used.
4. ‘`ty`’: the type of the call instruction itself which is also the type of the return value. Functions that return no value are marked `void`. The signature is computed based on the return type and argument types.
5. ‘`fnty`’: shall be the signature of the function being called. The argument types must match the types implied by this signature. This is only required if the signature specifies a varargs type.
6. ‘`fnptrval`’: An LLVM value containing a pointer to a function to be called. In most cases, this is a direct function call, but other `callbr`’s are just as possible, calling an arbitrary pointer to function value.
7. ‘`function args`’: argument list whose types match the function signature argument types and parameter attributes. All arguments must be of first class type. If the function signature indicates the function accepts a variable number of arguments, the extra arguments can be specified.
8. ‘`fallthrough label`’: the label reached when the inline assembly’s execution exits the bottom / the intrinsic call returns.
9. ‘`indirect labels`’: the labels reached when a callee transfers control to a location other than the ‘`fallthrough label`’. Label constraints refer to these destinations.
10. The optional function attributes list.
11. The optional operand bundles list.

##### Semantics:

This instruction is designed to operate as a standard ‘`call`’ instruction in most regards. The primary difference is that it establishes an association with additional labels to define where control flow goes after the call.

The output values of a ‘`callbr`’ instruction are available both in the the ‘`fallthrough`’ block, and any ‘`indirect`’ blocks(s).

The only current uses of this are:

1. implement the “goto” feature of gcc inline assembly where additional labels can be provided as locations for the inline assembly to jump to.
2. support selected intrinsics which manipulate control flow and should be chained to specific terminators, such as ‘`unreachable`’.

##### Example:

```llvm
; "asm goto" without output constraints.
callbr void asm "", "r,!i"(i32 %x)
            to label %fallthrough [label %indirect]

; "asm goto" with output constraints.
<result> = callbr i32 asm "", "=r,r,!i"(i32 %x)
            to label %fallthrough [label %indirect]

; intrinsic which should be followed by unreachable (the order of the
; blocks after the callbr instruction doesn't matter)
  callbr void @llvm.amdgcn.kill(i1 %c) to label %cont [label %kill]
cont:
  ...
kill:
  unreachable
```

##### Syntax:

```
resume <type> <value>
```

##### Overview:

The ‘`resume`’ instruction is a terminator instruction that has no successors.

##### Arguments:

The ‘`resume`’ instruction requires one argument, which must have the same type as the result of any ‘`landingpad`’ instruction in the same function.

##### Semantics:

The ‘`resume`’ instruction resumes propagation of an existing (in-flight) exception whose unwinding was interrupted with a landingpad instruction.

##### Example:

```llvm
resume { ptr, i32 } %exn
```

##### Syntax:

```
<resultval> = catchswitch within <parent> [ label <handler1>, label <handler2>, ... ] unwind to caller
<resultval> = catchswitch within <parent> [ label <handler1>, label <handler2>, ... ] unwind label <default>
```

##### Overview:

The ‘`catchswitch`’ instruction is used by LLVM’s exception handling system to describe the set of possible catch handlers that may be executed by the EH personality routine.

##### Arguments:

The `parent` argument is the token of the funclet that contains the `catchswitch` instruction. If the `catchswitch` is not inside a funclet, this operand may be the token `none`.

The `default` argument is the label of another basic block beginning with either a `cleanuppad` or `catchswitch` instruction. This unwind destination must be a legal target with respect to the `parent` links, as described in the exception handling documentation.

The `handlers` are a nonempty list of successor blocks that each begin with a catchpad instruction.

##### Semantics:

Executing this instruction transfers control to one of the successors in `handlers`, if appropriate, or continues to unwind via the unwind label if present.

The `catchswitch` is both a terminator and a “pad” instruction, meaning that it must be both the first non-phi instruction and last instruction in the basic block. Therefore, it must be the only non-phi instruction in the block.

##### Example:

```
dispatch1:
  %cs1 = catchswitch within none [label %handler0, label %handler1] unwind to caller
dispatch2:
  %cs2 = catchswitch within %parenthandler [label %handler0] unwind label %cleanup
```

##### Syntax:

```
catchret from <token> to label <normal>
```

##### Overview:

The ‘`catchret`’ instruction is a terminator instruction that has a single successor.

##### Arguments:

The first argument to a ‘`catchret`’ indicates which `catchpad` it exits. It must be a catchpad. The second argument to a ‘`catchret`’ specifies where control will transfer to next.

##### Semantics:

The ‘`catchret`’ instruction ends an existing (in-flight) exception whose unwinding was interrupted with a catchpad instruction. The personality function gets a chance to execute arbitrary code to, for example, destroy the active exception. Control then transfers to `normal`.

The `token` argument must be a token produced by a `catchpad` instruction. If the specified `catchpad` is not the most-recently-entered not-yet-exited funclet pad (as described in the EH documentation), the `catchret`’s behavior is undefined.

##### Example:

```
catchret from %catch to label %continue
```

##### Syntax:

```
cleanupret from <value> unwind label <continue>
cleanupret from <value> unwind to caller
```

##### Overview:

The ‘`cleanupret`’ instruction is a terminator instruction that has an optional successor.

##### Arguments:

The ‘`cleanupret`’ instruction requires one argument, which indicates which `cleanuppad` it exits, and must be a cleanuppad. If the specified `cleanuppad` is not the most-recently-entered not-yet-exited funclet pad (as described in the EH documentation), the `cleanupret`’s behavior is undefined.

The ‘`cleanupret`’ instruction also has an optional successor, `continue`, which must be the label of another basic block beginning with either a `cleanuppad` or `catchswitch` instruction. This unwind destination must be a legal target with respect to the `parent` links, as described in the exception handling documentation.

##### Semantics:

The ‘`cleanupret`’ instruction indicates to the personality function that one cleanuppad it transferred control to has ended. It transfers control to `continue` or unwinds out of the function.

##### Example:

```
cleanupret from %cleanup unwind to caller
cleanupret from %cleanup unwind label %continue
```

##### Syntax:

```
unreachable
```

##### Overview:

The ‘`unreachable`’ instruction has no defined semantics. This instruction is used to inform the optimizer that a particular portion of the code is not reachable. This can be used to indicate that the code after a no-return function cannot be reached, and other facts.

##### Semantics:

The ‘`unreachable`’ instruction has no defined semantics.

Unary operators require a single operand, execute an operation on it, and produce a single value. The operand might represent multiple data, as is the case with the vector data type. The result value has the same type as its operand.

##### Syntax:

```
<result> = fneg [fast-math flags]* <ty> <op1>   ; yields ty:result
```

##### Overview:

The ‘`fneg`’ instruction returns the negation of its operand.

##### Arguments:

The argument to the ‘`fneg`’ instruction must be a floating-point or vector of floating-point values.

##### Semantics:

The value produced is a copy of the operand with its sign bit flipped. The value is otherwise completely identical; in particular, if the input is a NaN, then the quiet/signaling bit and payload are perfectly preserved.

This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = fneg float %val          ; yields float:result = -%var
```

Binary operators are used to do most of the computation in a program. They require two operands of the same type, execute an operation on them, and produce a single value. The operands might represent multiple data, as is the case with the vector data type. The result value has the same type as its operands.

There are several different binary operators:

##### Syntax:

```
<result> = add <ty> <op1>, <op2>          ; yields ty:result
<result> = add nuw <ty> <op1>, <op2>      ; yields ty:result
<result> = add nsw <ty> <op1>, <op2>      ; yields ty:result
<result> = add nuw nsw <ty> <op1>, <op2>  ; yields ty:result
```

##### Overview:

The ‘`add`’ instruction returns the sum of its two operands.

##### Arguments:

The two arguments to the ‘`add`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The value produced is the integer sum of the two operands.

If the sum has unsigned overflow, the result returned is the mathematical result modulo 2n, where n is the bit width of the result.

Because LLVM integers use a two’s complement representation, this instruction is appropriate for both signed and unsigned integers.

`nuw` and `nsw` stand for “No Unsigned Wrap” and “No Signed Wrap”, respectively. If the `nuw` and/or `nsw` keywords are present, the result value of the `add` is a poison value if unsigned and/or signed overflow, respectively, occurs.

##### Example:

```
<result> = add i32 4, %var          ; yields i32:result = 4 + %var
```

##### Syntax:

```
<result> = fadd [fast-math flags]* <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`fadd`’ instruction returns the sum of its two operands.

##### Arguments:

The two arguments to the ‘`fadd`’ instruction must be floating-point or vector of floating-point values. Both arguments must have identical types.

##### Semantics:

The value produced is the floating-point sum of the two operands. This instruction is assumed to execute in the default floating-point environment. This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = fadd float 4.0, %var          ; yields float:result = 4.0 + %var
```

##### Syntax:

```
<result> = sub <ty> <op1>, <op2>          ; yields ty:result
<result> = sub nuw <ty> <op1>, <op2>      ; yields ty:result
<result> = sub nsw <ty> <op1>, <op2>      ; yields ty:result
<result> = sub nuw nsw <ty> <op1>, <op2>  ; yields ty:result
```

##### Overview:

The ‘`sub`’ instruction returns the difference of its two operands.

Note that the ‘`sub`’ instruction is used to represent the ‘`neg`’ instruction present in most other intermediate representations.

##### Arguments:

The two arguments to the ‘`sub`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The value produced is the integer difference of the two operands.

If the difference has unsigned overflow, the result returned is the mathematical result modulo 2n, where n is the bit width of the result.

Because LLVM integers use a two’s complement representation, this instruction is appropriate for both signed and unsigned integers.

`nuw` and `nsw` stand for “No Unsigned Wrap” and “No Signed Wrap”, respectively. If the `nuw` and/or `nsw` keywords are present, the result value of the `sub` is a poison value if unsigned and/or signed overflow, respectively, occurs.

##### Example:

```
<result> = sub i32 4, %var          ; yields i32:result = 4 - %var
<result> = sub i32 0, %val          ; yields i32:result = -%var
```

##### Syntax:

```
<result> = fsub [fast-math flags]* <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`fsub`’ instruction returns the difference of its two operands.

##### Arguments:

The two arguments to the ‘`fsub`’ instruction must be floating-point or vector of floating-point values. Both arguments must have identical types.

##### Semantics:

The value produced is the floating-point difference of the two operands. This instruction is assumed to execute in the default floating-point environment. This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = fsub float 4.0, %var           ; yields float:result = 4.0 - %var
<result> = fsub float -0.0, %val          ; yields float:result = -%var
```

##### Syntax:

```
<result> = mul <ty> <op1>, <op2>          ; yields ty:result
<result> = mul nuw <ty> <op1>, <op2>      ; yields ty:result
<result> = mul nsw <ty> <op1>, <op2>      ; yields ty:result
<result> = mul nuw nsw <ty> <op1>, <op2>  ; yields ty:result
```

##### Overview:

The ‘`mul`’ instruction returns the product of its two operands.

##### Arguments:

The two arguments to the ‘`mul`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The value produced is the integer product of the two operands.

If the result of the multiplication has unsigned overflow, the result returned is the mathematical result modulo 2n, where n is the bit width of the result.

Because LLVM integers use a two’s complement representation, and the result is the same width as the operands, this instruction returns the correct result for both signed and unsigned integers. If a full product (e.g., `i32` * `i32` -> `i64`) is needed, the operands should be sign-extended or zero-extended as appropriate to the width of the full product.

`nuw` and `nsw` stand for “No Unsigned Wrap” and “No Signed Wrap”, respectively. If the `nuw` and/or `nsw` keywords are present, the result value of the `mul` is a poison value if unsigned and/or signed overflow, respectively, occurs.

##### Example:

```
<result> = mul i32 4, %var          ; yields i32:result = 4 * %var
```

##### Syntax:

```
<result> = fmul [fast-math flags]* <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`fmul`’ instruction returns the product of its two operands.

##### Arguments:

The two arguments to the ‘`fmul`’ instruction must be floating-point or vector of floating-point values. Both arguments must have identical types.

##### Semantics:

The value produced is the floating-point product of the two operands. This instruction is assumed to execute in the default floating-point environment. This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = fmul float 4.0, %var          ; yields float:result = 4.0 * %var
```

##### Syntax:

```
<result> = udiv <ty> <op1>, <op2>         ; yields ty:result
<result> = udiv exact <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`udiv`’ instruction returns the quotient of its two operands.

##### Arguments:

The two arguments to the ‘`udiv`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The value produced is the unsigned integer quotient of the two operands.

Note that unsigned integer division and signed integer division are distinct operations; for signed integer division, use ‘`sdiv`’.

Division by zero is undefined behavior. For vectors, if any element of the divisor is zero, the operation has undefined behavior.

If the `exact` keyword is present, the result value of the `udiv` is a poison value if %op1 is not a multiple of %op2 (as such, “((a udiv exact b) mul b) == a”).

##### Example:

```
<result> = udiv i32 4, %var          ; yields i32:result = 4 / %var
```

##### Syntax:

```
<result> = sdiv <ty> <op1>, <op2>         ; yields ty:result
<result> = sdiv exact <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`sdiv`’ instruction returns the quotient of its two operands.

##### Arguments:

The two arguments to the ‘`sdiv`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The value produced is the signed integer quotient of the two operands rounded towards zero.

Note that signed integer division and unsigned integer division are distinct operations; for unsigned integer division, use ‘`udiv`’.

Division by zero is undefined behavior. For vectors, if any element of the divisor is zero, the operation has undefined behavior. Overflow also leads to undefined behavior; this is a rare case, but can occur, for example, by doing a 32-bit division of -2147483648 by -1.

If the `exact` keyword is present, the result value of the `sdiv` is a poison value if the result would be rounded.

##### Example:

```
<result> = sdiv i32 4, %var          ; yields i32:result = 4 / %var
```

##### Syntax:

```
<result> = fdiv [fast-math flags]* <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`fdiv`’ instruction returns the quotient of its two operands.

##### Arguments:

The two arguments to the ‘`fdiv`’ instruction must be floating-point or vector of floating-point values. Both arguments must have identical types.

##### Semantics:

The value produced is the floating-point quotient of the two operands. This instruction is assumed to execute in the default floating-point environment. This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = fdiv float 4.0, %var          ; yields float:result = 4.0 / %var
```

##### Syntax:

```
<result> = urem <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`urem`’ instruction returns the remainder from the unsigned division of its two arguments.

##### Arguments:

The two arguments to the ‘`urem`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

This instruction returns the unsigned integer *remainder* of a division. This instruction always performs an unsigned division to get the remainder.

Note that unsigned integer remainder and signed integer remainder are distinct operations; for signed integer remainder, use ‘`srem`’.

Taking the remainder of a division by zero is undefined behavior. For vectors, if any element of the divisor is zero, the operation has undefined behavior.

##### Example:

```
<result> = urem i32 4, %var          ; yields i32:result = 4 % %var
```

##### Syntax:

```
<result> = srem <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`srem`’ instruction returns the remainder from the signed division of its two operands. This instruction can also take vector versions of the values in which case the elements must be integers.

##### Arguments:

The two arguments to the ‘`srem`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

This instruction returns the *remainder* of a division (where the result is either zero or has the same sign as the dividend, `op1`), not the *modulo* operator (where the result is either zero or has the same sign as the divisor, `op2`) of a value. For more information about the difference, see The Math Forum. For a table of how this is implemented in various languages, please see Wikipedia: modulo operation.

Note that signed integer remainder and unsigned integer remainder are distinct operations; for unsigned integer remainder, use ‘`urem`’.

Taking the remainder of a division by zero is undefined behavior. For vectors, if any element of the divisor is zero, the operation has undefined behavior. Overflow also leads to undefined behavior; this is a rare case, but can occur, for example, by taking the remainder of a 32-bit division of -2147483648 by -1. (The remainder doesn’t actually overflow, but this rule lets srem be implemented using instructions that return both the result of the division and the remainder.)

##### Example:

```
<result> = srem i32 4, %var          ; yields i32:result = 4 % %var
```

##### Syntax:

```
<result> = frem [fast-math flags]* <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`frem`’ instruction returns the remainder from the division of its two operands.

Note

The instruction is implemented as a call to libm’s ‘`fmod`’ for some targets, and using the instruction may thus require linking libm.

##### Arguments:

The two arguments to the ‘`frem`’ instruction must be floating-point or vector of floating-point values. Both arguments must have identical types.

##### Semantics:

The value produced is the floating-point remainder of the two operands. This is the same output as a libm ‘`fmod`’ function, but without any possibility of setting `errno`. The remainder has the same sign as the dividend. This instruction is assumed to execute in the default floating-point environment. This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations:

##### Example:

```
<result> = frem float 4.0, %var          ; yields float:result = 4.0 % %var
```

Bitwise binary operators are used to do various forms of bit-twiddling in a program. They are generally very efficient instructions and can commonly be strength reduced from other instructions. They require two operands of the same type, execute an operation on them, and produce a single value. The resulting value is the same type as its operands.

##### Syntax:

```
<result> = shl <ty> <op1>, <op2>           ; yields ty:result
<result> = shl nuw <ty> <op1>, <op2>       ; yields ty:result
<result> = shl nsw <ty> <op1>, <op2>       ; yields ty:result
<result> = shl nuw nsw <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`shl`’ instruction returns the first operand shifted to the left a specified number of bits.

##### Arguments:

Both arguments to the ‘`shl`’ instruction must be the same integer or vector of integer type. ‘`op2`’ is treated as an unsigned value.

##### Semantics:

The value produced is `op1` * 2op2 mod 2n, where `n` is the width of the result. If `op2` is (statically or dynamically) equal to or larger than the number of bits in `op1`, this instruction returns a poison value. If the arguments are vectors, each vector element of `op1` is shifted by the corresponding shift amount in `op2`.

If the `nuw` keyword is present, then the shift produces a poison value if it shifts out any non-zero bits. If the `nsw` keyword is present, then the shift produces a poison value if it shifts out any bits that disagree with the resultant sign bit.

##### Example:

```
<result> = shl i32 4, %var   ; yields i32: 4 << %var
<result> = shl i32 4, 2      ; yields i32: 16
<result> = shl i32 1, 10     ; yields i32: 1024
<result> = shl i32 1, 32     ; undefined
<result> = shl <2 x i32> < i32 1, i32 1>, < i32 1, i32 2>   ; yields: result=<2 x i32> < i32 2, i32 4>
```

##### Syntax:

```
<result> = lshr <ty> <op1>, <op2>         ; yields ty:result
<result> = lshr exact <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`lshr`’ instruction (logical shift right) returns the first operand shifted to the right a specified number of bits with zero fill.

##### Arguments:

Both arguments to the ‘`lshr`’ instruction must be the same integer or vector of integer type. ‘`op2`’ is treated as an unsigned value.

##### Semantics:

This instruction always performs a logical shift right operation. The most significant bits of the result will be filled with zero bits after the shift. If `op2` is (statically or dynamically) equal to or larger than the number of bits in `op1`, this instruction returns a poison value. If the arguments are vectors, each vector element of `op1` is shifted by the corresponding shift amount in `op2`.

If the `exact` keyword is present, the result value of the `lshr` is a poison value if any of the bits shifted out are non-zero.

##### Example:

```
<result> = lshr i32 4, 1   ; yields i32:result = 2
<result> = lshr i32 4, 2   ; yields i32:result = 1
<result> = lshr i8  4, 3   ; yields i8:result = 0
<result> = lshr i8 -2, 1   ; yields i8:result = 0x7F
<result> = lshr i32 1, 32  ; undefined
<result> = lshr <2 x i32> < i32 -2, i32 4>, < i32 1, i32 2>   ; yields: result=<2 x i32> < i32 0x7FFFFFFF, i32 1>
```

##### Syntax:

```
<result> = ashr <ty> <op1>, <op2>         ; yields ty:result
<result> = ashr exact <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`ashr`’ instruction (arithmetic shift right) returns the first operand shifted to the right a specified number of bits with sign extension.

##### Arguments:

Both arguments to the ‘`ashr`’ instruction must be the same integer or vector of integer type. ‘`op2`’ is treated as an unsigned value.

##### Semantics:

This instruction always performs an arithmetic shift right operation, The most significant bits of the result will be filled with the sign bit of `op1`. If `op2` is (statically or dynamically) equal to or larger than the number of bits in `op1`, this instruction returns a poison value. If the arguments are vectors, each vector element of `op1` is shifted by the corresponding shift amount in `op2`.

If the `exact` keyword is present, the result value of the `ashr` is a poison value if any of the bits shifted out are non-zero.

##### Example:

```
<result> = ashr i32 4, 1   ; yields i32:result = 2
<result> = ashr i32 4, 2   ; yields i32:result = 1
<result> = ashr i8  4, 3   ; yields i8:result = 0
<result> = ashr i8 -2, 1   ; yields i8:result = -1
<result> = ashr i32 1, 32  ; undefined
<result> = ashr <2 x i32> < i32 -2, i32 4>, < i32 1, i32 3>   ; yields: result=<2 x i32> < i32 -1, i32 0>
```

##### Syntax:

```
<result> = and <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`and`’ instruction returns the bitwise logical and of its two operands.

##### Arguments:

The two arguments to the ‘`and`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The truth table used for the ‘`and`’ instruction is:

| In0 | In1 | Out |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

##### Example:

```
<result> = and i32 4, %var         ; yields i32:result = 4 & %var
<result> = and i32 15, 40          ; yields i32:result = 8
<result> = and i32 4, 8            ; yields i32:result = 0
```

##### Syntax:

```
<result> = or <ty> <op1>, <op2>   ; yields ty:result
<result> = or disjoint <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`or`’ instruction returns the bitwise logical inclusive or of its two operands.

##### Arguments:

The two arguments to the ‘`or`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The truth table used for the ‘`or`’ instruction is:

| In0 | In1 | Out |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

`disjoint` means that for each bit, that bit is zero in at least one of the inputs. This allows the Or to be treated as an Add since no carry can occur from any bit. If the disjoint keyword is present, the result value of the `or` is a poison value if both inputs have a one in the same bit position. For vectors, only the element containing the bit is poison.

##### Example:

```
<result> = or i32 4, %var         ; yields i32:result = 4 | %var
<result> = or i32 15, 40          ; yields i32:result = 47
<result> = or i32 4, 8            ; yields i32:result = 12
```

##### Syntax:

```
<result> = xor <ty> <op1>, <op2>   ; yields ty:result
```

##### Overview:

The ‘`xor`’ instruction returns the bitwise logical exclusive or of its two operands. The `xor` is used to implement the “one’s complement” operation, which is the “~” operator in C.

##### Arguments:

The two arguments to the ‘`xor`’ instruction must be integer or vector of integer values. Both arguments must have identical types.

##### Semantics:

The truth table used for the ‘`xor`’ instruction is:

| In0 | In1 | Out |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

##### Example:

```
<result> = xor i32 4, %var         ; yields i32:result = 4 ^ %var
<result> = xor i32 15, 40          ; yields i32:result = 39
<result> = xor i32 4, 8            ; yields i32:result = 12
<result> = xor i32 %V, -1          ; yields i32:result = ~%V
```

LLVM supports several instructions to represent vector operations in a target-independent manner. These instructions cover the element-access and vector-specific operations needed to process vectors effectively. While LLVM does directly support these vector operations, many sophisticated algorithms will want to use target-specific intrinsics to take full advantage of a specific target.

##### Syntax:

```
<result> = extractelement <n x <ty>> <val>, <ty2> <idx>  ; yields <ty>
<result> = extractelement <vscale x n x <ty>> <val>, <ty2> <idx> ; yields <ty>
```

##### Overview:

The ‘`extractelement`’ instruction extracts a single scalar element from a vector at a specified index.

##### Arguments:

The first operand of an ‘`extractelement`’ instruction is a value of vector type. The second operand is an index indicating the position from which to extract the element. The index may be a variable of any integer type, and will be treated as an unsigned integer.

##### Semantics:

The result is a scalar of the same type as the element type of `val`. Its value is the value at position `idx` of `val`. If `idx` exceeds the length of `val` for a fixed-length vector, the result is a poison value. For a scalable vector, if the value of `idx` exceeds the runtime length of the vector, the result is a poison value.

##### Example:

```
<result> = extractelement <4 x i32> %vec, i32 0    ; yields i32
```

##### Syntax:

```
<result> = insertelement <n x <ty>> <val>, <ty> <elt>, <ty2> <idx>    ; yields <n x <ty>>
<result> = insertelement <vscale x n x <ty>> <val>, <ty> <elt>, <ty2> <idx> ; yields <vscale x n x <ty>>
```

##### Overview:

The ‘`insertelement`’ instruction inserts a scalar element into a vector at a specified index.

##### Arguments:

The first operand of an ‘`insertelement`’ instruction is a value of vector type. The second operand is a scalar value whose type must equal the element type of the first operand. The third operand is an index indicating the position at which to insert the value. The index may be a variable of any integer type, and will be treated as an unsigned integer.

##### Semantics:

The result is a vector of the same type as `val`. Its element values are those of `val` except at position `idx`, where it gets the value `elt`. If `idx` exceeds the length of `val` for a fixed-length vector, the result is a poison value. For a scalable vector, if the value of `idx` exceeds the runtime length of the vector, the result is a poison value.

##### Example:

```
<result> = insertelement <4 x i32> %vec, i32 1, i32 0    ; yields <4 x i32>
```

##### Syntax:

```
<result> = shufflevector <n x <ty>> <v1>, <n x <ty>> <v2>, <m x i32> <mask>    ; yields <m x <ty>>
<result> = shufflevector <vscale x n x <ty>> <v1>, <vscale x n x <ty>> v2, <vscale x m x i32> <mask>  ; yields <vscale x m x <ty>>
```

##### Overview:

The ‘`shufflevector`’ instruction constructs a permutation of elements from two input vectors, returning a vector with the same element type as the input and length that is the same as the shuffle mask.

##### Arguments:

The first two operands of a ‘`shufflevector`’ instruction are vectors with the same type. The third argument is a shuffle mask vector constant whose element type is `i32`. The mask vector elements must be constant integers or `poison` values. The result of the instruction is a vector whose length is the same as the shuffle mask and whose element type is the same as the element type of the first two operands.

##### Semantics:

The elements of the two input vectors are numbered from left to right across both of the vectors. For each element of the result vector, the shuffle mask selects an element from one of the input vectors to copy to the result. Non-negative elements in the mask represent an index into the concatenated pair of input vectors.

A `poison` element in the mask vector specifies that the resulting element is `poison`. For backwards-compatibility reasons, LLVM temporarily also accepts `undef` mask elements. These will be interpreted the same way as `poison` mask elements, also producing a `poison` element in the result.

If the shuffle mask selects an `undef` element from one of the input vectors, the resulting element is `undef`.

For scalable vectors, the only valid mask values at present are `zeroinitializer`, `undef` and `poison`, since we cannot write all indices as literals for a vector with a length unknown at compile time.

##### Example:

```
<result> = shufflevector <4 x i32> %v1, <4 x i32> %v2,
                        <4 x i32> <i32 0, i32 4, i32 1, i32 5>  ; yields <4 x i32>
<result> = shufflevector <4 x i32> %v1, <4 x i32> poison,
                        <4 x i32> <i32 0, i32 1, i32 2, i32 3>  ; yields <4 x i32> - Identity shuffle.
<result> = shufflevector <8 x i32> %v1, <8 x i32> poison,
                        <4 x i32> <i32 0, i32 1, i32 2, i32 3>  ; yields <4 x i32>
<result> = shufflevector <4 x i32> %v1, <4 x i32> %v2,
                        <8 x i32> <i32 0, i32 1, i32 2, i32 3, i32 4, i32 5, i32 6, i32 7 >  ; yields <8 x i32>
```

LLVM supports several instructions for working with aggregate values.

##### Syntax:

```
<result> = extractvalue <aggregate type> <val>, <idx>{, <idx>}*
```

##### Overview:

The ‘`extractvalue`’ instruction extracts the value of a member field from an aggregate value.

##### Arguments:

The first operand of an ‘`extractvalue`’ instruction is a value of struct or array type. The other operands are constant indices to specify which value to extract in a similar manner as indices in a ‘`getelementptr`’ instruction.

The major differences to `getelementptr` indexing are:

- Since the value being indexed is not a pointer, the first index is omitted and assumed to be zero.
- At least one index must be specified.
- Not only struct indices but also array indices must be in bounds.

##### Semantics:

The result is the value at the position in the aggregate specified by the index operands.

##### Example:

```
<result> = extractvalue {i32, float} %agg, 0    ; yields i32
```

##### Syntax:

```
<result> = insertvalue <aggregate type> <val>, <ty> <elt>, <idx>{, <idx>}*    ; yields <aggregate type>
```

##### Overview:

The ‘`insertvalue`’ instruction inserts a value into a member field in an aggregate value.

##### Arguments:

The first operand of an ‘`insertvalue`’ instruction is a value of struct or array type. The second operand is a first-class value to insert. The following operands are constant indices indicating the position at which to insert the value in a similar manner as indices in a ‘`extractvalue`’ instruction. The value to insert must have the same type as the value identified by the indices.

##### Semantics:

The result is an aggregate of the same type as `val`. Its value is that of `val` except that the value at the position specified by the indices is that of `elt`.

##### Example:

```llvm
%agg1 = insertvalue {i32, float} poison, i32 1, 0              ; yields {i32 1, float poison}
%agg2 = insertvalue {i32, float} %agg1, float %val, 1          ; yields {i32 1, float %val}
%agg3 = insertvalue {i32, {float}} poison, float %val, 1, 0    ; yields {i32 poison, {float %val}}
```

A key design point of an SSA-based representation is how it represents memory. In LLVM, no memory locations are in SSA form, which makes things very simple. This section describes how to read, write, and allocate memory in LLVM.

##### Syntax:

```
<result> = alloca [inalloca] <type> [, <ty> <NumElements>] [, align <alignment>] [, addrspace(<num>)]     ; yields type addrspace(num)*:result
```

##### Overview:

The ‘`alloca`’ instruction allocates memory on the stack frame of the currently executing function, to be automatically released when this function returns to its caller. If the address space is not explicitly specified, the default address space 0 is used.

##### Arguments:

The ‘`alloca`’ instruction allocates `sizeof(<type>)*NumElements` bytes of memory on the runtime stack, returning a pointer of the appropriate type to the program. If “NumElements” is specified, it is the number of elements allocated, otherwise “NumElements” is defaulted to be one.

If a constant alignment is specified, the value result of the allocation is guaranteed to be aligned to at least that boundary. The alignment may not be greater than `1 << 32`.

The alignment is only optional when parsing textual IR; for in-memory IR, it is always present. If not specified, the target can choose to align the allocation on any convenient boundary compatible with the type.

‘`type`’ may be any sized type.

Structs containing scalable vectors cannot be used in allocas unless all fields are the same scalable vector type (e.g., `{<vscale x 2 x i32>, <vscale x 2 x i32>}` contains the same type while `{<vscale x 2 x i32>, <vscale x 2 x i64>}` doesn’t).

##### Semantics:

Memory is allocated; a pointer is returned. The allocated memory is uninitialized, and loading from uninitialized memory produces an undefined value. The operation itself is undefined if there is insufficient stack space for the allocation.’`alloca`’d memory is automatically released when the function returns. The ‘`alloca`’ instruction is commonly used to represent automatic variables that must have an address available. When the function returns (either with the `ret` or `resume` instructions), the memory is reclaimed. Allocating zero bytes is legal, but the returned pointer may not be unique. The order in which memory is allocated (ie., which way the stack grows) is not specified.

Note that ‘`alloca`’ outside of the alloca address space from the datalayout string is meaningful only if the target has assigned it a semantics. For targets that specify a non-zero alloca address space in the datalayout string, the alloca address space needs to be explicitly specified in the instruction if it is to be used.

If the returned pointer is used by llvm.lifetime.start, the returned object is initially dead. See llvm.lifetime.start and llvm.lifetime.end for the precise semantics of lifetime-manipulating intrinsics.

If the element count is `undef` or `poison`, this instruction has undefined behavior.

##### Example:

```llvm
%ptr = alloca i32                             ; yields ptr
%ptr = alloca i32, i32 4                      ; yields ptr
%ptr = alloca i32, i32 4, align 1024          ; yields ptr
%ptr = alloca i32, align 1024                 ; yields ptr
```

##### Syntax:

```
<result> = load [volatile] <ty>, ptr <pointer>[, align <alignment>][, !nontemporal !<nontemp_node>][, !invariant.load !<empty_node>][, !invariant.group !<empty_node>][, !nonnull !<empty_node>][, !dereferenceable !<deref_bytes_node>][, !dereferenceable_or_null !<deref_bytes_node>][, !align !<align_node>][, !noundef !<empty_node>]
<result> = load atomic [volatile] <ty>, ptr <pointer> [syncscope("<target-scope>")] <ordering>, align <alignment> [, !invariant.group !<empty_node>]
!<nontemp_node> = !{ i32 1 }
!<empty_node> = !{}
!<deref_bytes_node> = !{ i64 <dereferenceable_bytes> }
!<align_node> = !{ i64 <value_alignment> }
```

##### Overview:

The ‘`load`’ instruction is used to read from memory.

##### Arguments:

The argument to the `load` instruction specifies the memory address from which to load. The type specified must be a first class type of known size (i.e., not containing an opaque structural type). If the `load` is marked as `volatile`, then the optimizer is not allowed to modify the number or order of execution of this `load` with other volatile operations.

If the `load` is marked as `atomic`, it takes an extra ordering and optional `syncscope("<target-scope>")` argument. The `release` and `acq_rel` orderings are not valid on `load` instructions. Atomic loads produce defined results when they may see multiple atomic stores. The type of the pointee must be an integer, pointer, floating-point, or vector type whose bit width is a power of two greater than or equal to eight. `align` must be explicitly specified on atomic loads. Note: if the alignment is not greater or equal to the size of the *<value>* type, the atomic operation is likely to require a lock and have poor performance. `!nontemporal` does not have any defined semantics for atomic loads.

The optional constant `align` argument specifies the alignment of the operation (that is, the alignment of the memory address). It is the responsibility of the code emitter to ensure that the alignment information is correct. Overestimating the alignment results in undefined behavior. Underestimating the alignment may produce less efficient code. An alignment of 1 is always safe. The maximum possible alignment is `1 << 32`. An alignment value higher than the size of the loaded type does *not* imply (without target specific knowledge) that memory up to the alignment value bytes can be safely loaded without trapping.

The alignment is only optional when parsing textual IR; for in-memory IR, it is always present. An omitted `align` argument means that the operation has the ABI alignment for the target.

The optional `!nontemporal` metadata must reference a single metadata name `<nontemp_node>` corresponding to a metadata node with one `i32` entry of value 1. The existence of the `!nontemporal` metadata on the instruction tells the optimizer and code generator that this load is not expected to be reused in the cache. The code generator may select special instructions to save cache bandwidth, such as the `MOVNT` instruction on x86.

The optional `!invariant.load` metadata must reference a single metadata name `<empty_node>` corresponding to a metadata node with no entries. If a load instruction tagged with the `!invariant.load` metadata is executed, the memory location referenced by the load has to contain the same value at all points in the program where the memory location is dereferenceable; otherwise, the behavior is undefined.

**The optional `!invariant.group` metadata must reference a single metadata name**

`<empty_node>` corresponding to a metadata node with no entries. See `invariant.group` metadata invariant.group.

The optional `!nonnull` metadata must reference a single metadata name `<empty_node>` corresponding to a metadata node with no entries. The existence of the `!nonnull` metadata on the instruction tells the optimizer that the value loaded is known to never be null. If the value is null at runtime, a poison value is returned instead. This is analogous to the `nonnull` attribute on parameters and return values. This metadata can only be applied to loads of a pointer type.

The optional `!dereferenceable` metadata must reference a single metadata name `<deref_bytes_node>` corresponding to a metadata node with one `i64` entry. See `dereferenceable` metadata dereferenceable.

The optional `!dereferenceable_or_null` metadata must reference a single metadata name `<deref_bytes_node>` corresponding to a metadata node with one `i64` entry. See `dereferenceable_or_null` metadata dereferenceable_or_null.

The optional `!align` metadata must reference a single metadata name `<align_node>` corresponding to a metadata node with one `i64` entry. The existence of the `!align` metadata on the instruction tells the optimizer that the value loaded is known to be aligned to a boundary specified by the integer value in the metadata node. The alignment must be a power of 2. This is analogous to the ‘’align’’ attribute on parameters and return values. This metadata can only be applied to loads of a pointer type. If the returned value is not appropriately aligned at runtime, a poison value is returned instead.

The optional `!noundef` metadata must reference a single metadata name `<empty_node>` corresponding to a node with no entries. The existence of `!noundef` metadata on the instruction tells the optimizer that the value loaded is known to be well defined. If the value isn’t well defined, the behavior is undefined. If the `!noundef` metadata is combined with poison-generating metadata like `!nonnull`, violation of that metadata constraint will also result in undefined behavior.

##### Semantics:

The location of memory pointed to is loaded. If the value being loaded is of scalar type then the number of bytes read does not exceed the minimum number of bytes needed to hold all bits of the type. For example, loading an `i24` reads at most three bytes. When loading a value of a type like `i20` with a size that is not an integral number of bytes, the load will be performed on the next larger multiple of the byte size (here `i24`) and truncated. If any of the truncated bits are non-zero, the result is a poison value. As such, a non-byte-sized load behaves like a byte-sized load followed by a `trunc nuw` operation.

If the value being loaded is of aggregate type, the bytes that correspond to padding may be accessed but are ignored, because it is impossible to observe padding from the loaded aggregate value. If `<pointer>` is not a well-defined value, the behavior is undefined. The behavior of loading a value of a type that differs from the type used to store it is described in the bitcast section.

##### Examples:
