---
title: "LLVM Language Reference Manual (part 13/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 13/20
---

# LLVM Language Reference Manual

```
declare i16 @llvm.umul.fix.sat.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.umul.fix.sat.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.umul.fix.sat.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.umul.fix.sat.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.umul.fix.sat`’ family of intrinsic functions perform unsigned fixed point saturating multiplication on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo unsigned fixed point multiplication. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point multiplication on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

The maximum value this operation can clamp to is the largest unsigned value representable by the bit width of the first 2 arguments. The minimum value is the smallest unsigned value representable by this bit width (zero).

##### Examples

```llvm
%res = call i4 @llvm.umul.fix.sat.i4(i4 3, i4 2, i32 0)  ; %res = 6 (2 x 3 = 6)
%res = call i4 @llvm.umul.fix.sat.i4(i4 3, i4 2, i32 1)  ; %res = 3 (1.5 x 1 = 1.5)

; The result in the following could be rounded down to 2 or up to 2.5
%res = call i4 @llvm.umul.fix.sat.i4(i4 3, i4 3, i32 1)  ; %res = 4 (or 5) (1.5 x 1.5 = 2.25)

; Saturation
%res = call i4 @llvm.umul.fix.sat.i4(i4 8, i4 2, i32 0)  ; %res = 15 (8 x 2 -> clamped to 15)
%res = call i4 @llvm.umul.fix.sat.i4(i4 8, i4 8, i32 2)  ; %res = 15 (2 x 2 -> clamped to 3.75)

; Scale can affect the saturation result
%res = call i4 @llvm.umul.fix.sat.i4(i4 2, i4 4, i32 0)  ; %res = 7 (2 x 4 -> clamped to 7)
%res = call i4 @llvm.umul.fix.sat.i4(i4 2, i4 4, i32 1)  ; %res = 4 (1 x 2 = 2)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.sdiv.fix` on any integer bit width or vectors of integers.

```
declare i16 @llvm.sdiv.fix.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.sdiv.fix.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.sdiv.fix.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.sdiv.fix.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.sdiv.fix`’ family of intrinsic functions perform signed fixed point division on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. The arguments may also work with int vectors of the same length and int size. `%a` and `%b` are the two values that will undergo signed fixed point division. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point division on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

It is undefined behavior if the result value does not fit within the range of the fixed point type, or if the second argument is zero.

##### Examples

```llvm
%res = call i4 @llvm.sdiv.fix.i4(i4 6, i4 2, i32 0)  ; %res = 3 (6 / 2 = 3)
%res = call i4 @llvm.sdiv.fix.i4(i4 6, i4 4, i32 1)  ; %res = 3 (3 / 2 = 1.5)
%res = call i4 @llvm.sdiv.fix.i4(i4 3, i4 -2, i32 1) ; %res = -3 (1.5 / -1 = -1.5)

; The result in the following could be rounded up to 1 or down to 0.5
%res = call i4 @llvm.sdiv.fix.i4(i4 3, i4 4, i32 1)  ; %res = 2 (or 1) (1.5 / 2 = 0.75)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.udiv.fix` on any integer bit width or vectors of integers.

```
declare i16 @llvm.udiv.fix.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.udiv.fix.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.udiv.fix.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.udiv.fix.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.udiv.fix`’ family of intrinsic functions perform unsigned fixed point division on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. The arguments may also work with int vectors of the same length and int size. `%a` and `%b` are the two values that will undergo unsigned fixed point division. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point division on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

It is undefined behavior if the result value does not fit within the range of the fixed point type, or if the second argument is zero.

##### Examples

```llvm
%res = call i4 @llvm.udiv.fix.i4(i4 6, i4 2, i32 0)  ; %res = 3 (6 / 2 = 3)
%res = call i4 @llvm.udiv.fix.i4(i4 6, i4 4, i32 1)  ; %res = 3 (3 / 2 = 1.5)
%res = call i4 @llvm.udiv.fix.i4(i4 1, i4 -8, i32 4) ; %res = 2 (0.0625 / 0.5 = 0.125)

; The result in the following could be rounded up to 1 or down to 0.5
%res = call i4 @llvm.udiv.fix.i4(i4 3, i4 4, i32 1)  ; %res = 2 (or 1) (1.5 / 2 = 0.75)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.sdiv.fix.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.sdiv.fix.sat.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.sdiv.fix.sat.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.sdiv.fix.sat.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.sdiv.fix.sat.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.sdiv.fix.sat`’ family of intrinsic functions perform signed fixed point saturating division on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo signed fixed point division. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point division on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

The maximum value this operation can clamp to is the largest signed value representable by the bit width of the first 2 arguments. The minimum value is the smallest signed value representable by this bit width.

It is undefined behavior if the second argument is zero.

##### Examples

```llvm
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 6, i4 2, i32 0)  ; %res = 3 (6 / 2 = 3)
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 6, i4 4, i32 1)  ; %res = 3 (3 / 2 = 1.5)
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 3, i4 -2, i32 1) ; %res = -3 (1.5 / -1 = -1.5)

; The result in the following could be rounded up to 1 or down to 0.5
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 3, i4 4, i32 1)  ; %res = 2 (or 1) (1.5 / 2 = 0.75)

; Saturation
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 -8, i4 -1, i32 0)  ; %res = 7 (-8 / -1 = 8 => 7)
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 4, i4 2, i32 2)  ; %res = 7 (1 / 0.5 = 2 => 1.75)
%res = call i4 @llvm.sdiv.fix.sat.i4(i4 -4, i4 1, i32 2)  ; %res = -8 (-1 / 0.25 = -4 => -2)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.udiv.fix.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.udiv.fix.sat.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.udiv.fix.sat.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.udiv.fix.sat.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.udiv.fix.sat.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.udiv.fix.sat`’ family of intrinsic functions perform unsigned fixed point saturating division on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo unsigned fixed point division. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point division on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

The maximum value this operation can clamp to is the largest unsigned value representable by the bit width of the first 2 arguments. The minimum value is the smallest unsigned value representable by this bit width (zero).

It is undefined behavior if the second argument is zero.

##### Examples

```llvm
%res = call i4 @llvm.udiv.fix.sat.i4(i4 6, i4 2, i32 0)  ; %res = 3 (6 / 2 = 3)
%res = call i4 @llvm.udiv.fix.sat.i4(i4 6, i4 4, i32 1)  ; %res = 3 (3 / 2 = 1.5)

; The result in the following could be rounded down to 0.5 or up to 1
%res = call i4 @llvm.udiv.fix.sat.i4(i4 3, i4 4, i32 1)  ; %res = 1 (or 2) (1.5 / 2 = 0.75)

; Saturation
%res = call i4 @llvm.udiv.fix.sat.i4(i4 8, i4 2, i32 2)  ; %res = 15 (2 / 0.5 = 4 => 3.75)
```

##### Syntax:

```
declare float @llvm.canonicalize.f32(float %a)
declare double @llvm.canonicalize.f64(double %b)
```

##### Overview:

The ‘`llvm.canonicalize.*`’ intrinsic returns the platform-specific canonical encoding of a floating-point number. This canonicalization is useful for implementing certain numeric primitives such as frexp. The canonical encoding is defined by IEEE 754-2008 to be:

```
2.1.8 canonical encoding: The preferred encoding of a floating-point
representation in a format. Applied to declets, significands of finite
numbers, infinities, and NaNs, especially in decimal formats.
```

This operation can also be considered equivalent to the IEEE 754-2008 conversion of a floating-point value to the same format. NaNs are handled according to section 6.2.

Examples of non-canonical encodings:

- x87 pseudo denormals, pseudo NaNs, pseudo Infinity, Unnormals. These are converted to a canonical representation per hardware-specific protocol.
- Many normal decimal floating-point numbers have non-canonical alternative encodings.
- Some machines, like GPUs or ARMv7 NEON, do not support subnormal values. These are treated as non-canonical encodings of zero and will be flushed to a zero of the same sign by this operation.

Note that per IEEE 754-2008 6.2, systems that support signaling NaNs with default exception handling must signal an invalid exception, and produce a quiet NaN result.

This function should always be implementable as multiplication by 1.0, provided that the compiler does not constant fold the operation. Likewise, division by 1.0 and `llvm.minnum(x, x)` are possible implementations. Addition with -0.0 is also sufficient provided that the rounding mode is not -Infinity.

`@llvm.canonicalize` must preserve the equality relation. That is:

- `(@llvm.canonicalize(x) == x)` is equivalent to `(x == x)`
- `(@llvm.canonicalize(x) == @llvm.canonicalize(y))` is equivalent to `(x == y)`

Additionally, the sign of zero must be conserved: `@llvm.canonicalize(-0.0) = -0.0` and `@llvm.canonicalize(+0.0) = +0.0`

The payload bits of a NaN must be conserved, with two exceptions. First, environments which use only a single canonical representation of NaN must perform said canonicalization. Second, SNaNs must be quieted per the usual methods.

The canonicalization operation may be optimized away if:

- The input is known to be canonical. For example, it was produced by a floating-point operation that is required by the standard to be canonical.
- The result is consumed only by (or fused with) other floating-point operations. That is, the bits of the floating-point value are not examined.

##### Syntax:

```
declare float @llvm.fmuladd.f32(float %a, float %b, float %c)
declare double @llvm.fmuladd.f64(double %a, double %b, double %c)
```

##### Overview:

The ‘`llvm.fmuladd.*`’ intrinsic functions represent multiply-add expressions that can be fused if the code generator determines that (a) the target instruction set has support for a fused operation, and (b) that the fused operation is more efficient than the equivalent, separate pair of mul and add instructions.

##### Arguments:

The ‘`llvm.fmuladd.*`’ intrinsics each take three arguments: two multiplicands, a and b, and an addend c.

##### Semantics:

The expression:

```
%0 = call float @llvm.fmuladd.f32(%a, %b, %c)
```

is equivalent to the expression a * b + c, except that it is unspecified whether rounding will be performed between the multiplication and addition steps. Fusion is not guaranteed, even if the target platform supports it. If a fused multiply-add is required, the corresponding llvm.fma intrinsic function should be used instead. This never sets errno, just as ‘`llvm.fma.*`’.

##### Examples:

```llvm
%r2 = call float @llvm.fmuladd.f32(float %a, float %b, float %c) ; yields float:r2 = (a * b) + c
```

LLVM support several intrinsics to mark a loop as a hardware-loop. They are hints to the backend which are required to lower these intrinsics further to target specific instructions, or revert the hardware-loop to a normal loop if target specific restriction are not met and a hardware-loop can’t be generated.

These intrinsics may be modified in the future and are not intended to be used outside the backend. Thus, front-end and mid-level optimizations should not be generating these intrinsics.

##### Syntax:

This is an overloaded intrinsic.

```
declare void @llvm.set.loop.iterations.i32(i32)
declare void @llvm.set.loop.iterations.i64(i64)
```

##### Overview:

The ‘`llvm.set.loop.iterations.*`’ intrinsics are used to specify the hardware-loop trip count. They are placed in the loop preheader basic block and are marked as `IntrNoDuplicate` to avoid optimizers duplicating these instructions.

##### Arguments:

The integer operand is the loop trip count of the hardware-loop, and thus not e.g., the loop back-edge taken count.

##### Semantics:

The ‘`llvm.set.loop.iterations.*`’ intrinsics do not perform any arithmetic on their operand. It’s a hint to the backend that can use this to set up the hardware-loop count with a target-specific instruction, usually a move of this value to a special register or a hardware-loop instruction.

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.start.loop.iterations.i32(i32)
declare i64 @llvm.start.loop.iterations.i64(i64)
```

##### Overview:

The ‘`llvm.start.loop.iterations.*`’ intrinsics are similar to the ‘`llvm.set.loop.iterations.*`’ intrinsics, used to specify the hardware-loop trip count but also produce a value identical to the input that can be used as the input to the loop. They are placed in the loop preheader basic block and the output is expected to be the input to the phi for the induction variable of the loop, decremented by the ‘`llvm.loop.decrement.reg.*`’.

##### Arguments:

The integer operand is the loop trip count of the hardware-loop, and thus not e.g., the loop back-edge taken count.

##### Semantics:

The ‘`llvm.start.loop.iterations.*`’ intrinsics do not perform any arithmetic on their operand. It’s a hint to the backend that can use this to set up the hardware-loop count with a target-specific instruction, usually a move of this value to a special register or a hardware-loop instruction.

##### Syntax:

This is an overloaded intrinsic.

```
declare i1 @llvm.test.set.loop.iterations.i32(i32)
declare i1 @llvm.test.set.loop.iterations.i64(i64)
```

##### Overview:

The ‘`llvm.test.set.loop.iterations.*`’ intrinsics are used to specify the the loop trip count, and also test that the given count is not zero, allowing it to control entry to a while-loop. They are placed in the loop preheader’s predecessor basic block, and are marked as `IntrNoDuplicate` to avoid optimizers duplicating these instructions.

##### Arguments:

The integer operand is the loop trip count of the hardware-loop, and thus not e.g., the loop back-edge taken count.

##### Semantics:

The ‘`llvm.test.set.loop.iterations.*`’ intrinsics do not perform any arithmetic on their operand. It’s a hint to the backend that can use this to set up the hardware-loop count with a target-specific instruction, usually a move of this value to a special register or a hardware-loop instruction. The result is the conditional value of whether the given count is not zero.

##### Syntax:

This is an overloaded intrinsic.

```
declare {i32, i1} @llvm.test.start.loop.iterations.i32(i32)
declare {i64, i1} @llvm.test.start.loop.iterations.i64(i64)
```

##### Overview:

The ‘`llvm.test.start.loop.iterations.*`’ intrinsics are similar to the ‘`llvm.test.set.loop.iterations.*`’ and ‘`llvm.start.loop.iterations.*`’ intrinsics, used to specify the hardware-loop trip count, but also produce a value identical to the input that can be used as the input to the loop. The second i1 output controls entry to a while-loop.

##### Arguments:

The integer operand is the loop trip count of the hardware-loop, and thus not e.g., the loop back-edge taken count.

##### Semantics:

The ‘`llvm.test.start.loop.iterations.*`’ intrinsics do not perform any arithmetic on their operand. It’s a hint to the backend that can use this to set up the hardware-loop count with a target-specific instruction, usually a move of this value to a special register or a hardware-loop instruction. The result is a pair of the input and a conditional value of whether the given count is not zero.

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.loop.decrement.reg.i32(i32, i32)
declare i64 @llvm.loop.decrement.reg.i64(i64, i64)
```

##### Overview:

The ‘`llvm.loop.decrement.reg.*`’ intrinsics are used to lower the loop iteration counter and return an updated value that will be used in the next loop test check.

##### Arguments:

Both arguments must have identical integer types. The first operand is the loop iteration counter. The second operand is the maximum number of elements processed in an iteration.

##### Semantics:

The ‘`llvm.loop.decrement.reg.*`’ intrinsics do an integer `SUB` of its two operands, which is not allowed to wrap. They return the remaining number of iterations still to be executed, and can be used together with a `PHI`, `ICMP` and `BR` to control the number of loop iterations executed. Any optimizations are allowed to treat it is a `SUB`, and it is supported by SCEV, so it’s the backends responsibility to handle cases where it may be optimized. These intrinsics are marked as `IntrNoDuplicate` to avoid optimizers duplicating these instructions.

##### Syntax:

This is an overloaded intrinsic.

```
declare i1 @llvm.loop.decrement.i32(i32)
declare i1 @llvm.loop.decrement.i64(i64)
```

##### Overview:

The HardwareLoops pass allows the loop decrement value to be specified with an option. It defaults to a loop decrement value of 1, but it can be an unsigned integer value provided by this option. The ‘`llvm.loop.decrement.*`’ intrinsics decrement the loop iteration counter with this value, and return a false predicate if the loop should exit, and true otherwise. This is emitted if the loop counter is not updated via a `PHI` node, which can also be controlled with an option.

##### Arguments:

The integer argument is the loop decrement value used to decrement the loop iteration counter.

##### Semantics:

The ‘`llvm.loop.decrement.*`’ intrinsics do a `SUB` of the loop iteration counter with the given loop decrement value, and return false if the loop should exit, this `SUB` is not allowed to wrap. The result is a condition that is used by the conditional branch controlling the loop.

Horizontal reductions of vectors can be expressed using the following intrinsics. Each one takes a vector operand as an input and applies its respective operation across all elements of the vector, returning a single scalar result of the same element type.

##### Syntax:

```
declare i32 @llvm.vector.reduce.add.v4i32(<4 x i32> %a)
declare i64 @llvm.vector.reduce.add.v2i64(<2 x i64> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.add.*`’ intrinsics do an integer `ADD` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare float @llvm.vector.reduce.fadd.v4f32(float %start_value, <4 x float> %a)
declare double @llvm.vector.reduce.fadd.v2f64(double %start_value, <2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fadd.*`’ intrinsics do a floating-point `ADD` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

If the intrinsic call has the ‘reassoc’ flag set, then the reduction will not preserve the associativity of an equivalent scalarized counterpart. Otherwise the reduction will be *sequential*, thus implying that the operation respects the associativity of a scalarized reduction. That is, the reduction begins with the start value and performs an fadd operation with consecutively increasing vector element indices. See the following pseudocode:

```
float sequential_fadd(start_value, input_vector)
  result = start_value
  for i = 0 to length(input_vector)
    result = result + input_vector[i]
  return result
```

##### Arguments:

The first argument to this intrinsic is a scalar start value for the reduction. The type of the start value matches the element-type of the vector input. The second argument must be a vector of floating-point values.

To ignore the start value, negative zero (`-0.0`) can be used, as it is the neutral value of floating point addition.

##### Examples:

```
%unord = call reassoc float @llvm.vector.reduce.fadd.v4f32(float -0.0, <4 x float> %input) ; relaxed reduction
%ord = call float @llvm.vector.reduce.fadd.v4f32(float %start_value, <4 x float> %input) ; sequential reduction
```

##### Syntax:

```
declare i32 @llvm.vector.reduce.mul.v4i32(<4 x i32> %a)
declare i64 @llvm.vector.reduce.mul.v2i64(<2 x i64> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.mul.*`’ intrinsics do an integer `MUL` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare float @llvm.vector.reduce.fmul.v4f32(float %start_value, <4 x float> %a)
declare double @llvm.vector.reduce.fmul.v2f64(double %start_value, <2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fmul.*`’ intrinsics do a floating-point `MUL` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

If the intrinsic call has the ‘reassoc’ flag set, then the reduction will not preserve the associativity of an equivalent scalarized counterpart. Otherwise the reduction will be *sequential*, thus implying that the operation respects the associativity of a scalarized reduction. That is, the reduction begins with the start value and performs an fmul operation with consecutively increasing vector element indices. See the following pseudocode:

```
float sequential_fmul(start_value, input_vector)
  result = start_value
  for i = 0 to length(input_vector)
    result = result * input_vector[i]
  return result
```

##### Arguments:

The first argument to this intrinsic is a scalar start value for the reduction. The type of the start value matches the element-type of the vector input. The second argument must be a vector of floating-point values.

To ignore the start value, one (`1.0`) can be used, as it is the neutral value of floating point multiplication.

##### Examples:

```
%unord = call reassoc float @llvm.vector.reduce.fmul.v4f32(float 1.0, <4 x float> %input) ; relaxed reduction
%ord = call float @llvm.vector.reduce.fmul.v4f32(float %start_value, <4 x float> %input) ; sequential reduction
```

##### Syntax:

```
declare i32 @llvm.vector.reduce.and.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.and.*`’ intrinsics do a bitwise `AND` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.or.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.or.*`’ intrinsics do a bitwise `OR` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.xor.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.xor.*`’ intrinsics do a bitwise `XOR` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.smax.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.smax.*`’ intrinsics do a signed integer `MAX` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.smin.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.smin.*`’ intrinsics do a signed integer `MIN` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.umax.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.umax.*`’ intrinsics do an unsigned integer `MAX` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare i32 @llvm.vector.reduce.umin.v4i32(<4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.umin.*`’ intrinsics do an unsigned integer `MIN` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

##### Arguments:

The argument to this intrinsic must be a vector of integer values.

##### Syntax:

```
declare float @llvm.vector.reduce.fmax.v4f32(<4 x float> %a)
declare double @llvm.vector.reduce.fmax.v2f64(<2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fmax.*`’ intrinsics do a floating-point `MAX` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

This instruction has the same comparison and `nsz` semantics as the ‘`llvm.maxnum.*`’ intrinsic.

The reduction is performed in a non-deterministic order. This is only observable if one of the inputs is a signaling NaN.

For example, if a reduction is performed over `<sNaN, 0.0, 1.0>`, then all of NaN, `0.0` and `1.0` are possible results, depending on which order is picked.

##### Arguments:

The argument to this intrinsic must be a vector of floating-point values.

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vector.reduce.fmin.v4f32(<4 x float> %a)
declare double @llvm.vector.reduce.fmin.v2f64(<2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fmin.*`’ intrinsics do a floating-point `MIN` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

This instruction has the same comparison and `nsz` semantics as the ‘`llvm.minnum.*`’ intrinsic.

The reduction is performed in a non-deterministic order. This is only observable if one of the inputs is a signaling NaN.

For example, if a reduction is performed over `<sNaN, 0.0, 1.0>`, then all of NaN, `0.0` and `1.0` are possible results, depending on which order is picked.

##### Arguments:

The argument to this intrinsic must be a vector of floating-point values.

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vector.reduce.fmaximum.v4f32(<4 x float> %a)
declare double @llvm.vector.reduce.fmaximum.v2f64(<2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fmaximum.*`’ intrinsics do a floating-point `MAX` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

This instruction has the same comparison semantics as the ‘`llvm.maximum.*`’ intrinsic. That is, this intrinsic propagates NaNs and +0.0 is considered greater than -0.0. If any element of the vector is a NaN, the result is NaN.

##### Arguments:

The argument to this intrinsic must be a vector of floating-point values.

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vector.reduce.fminimum.v4f32(<4 x float> %a)
declare double @llvm.vector.reduce.fminimum.v2f64(<2 x double> %a)
```

##### Overview:

The ‘`llvm.vector.reduce.fminimum.*`’ intrinsics do a floating-point `MIN` reduction of a vector, returning the result as a scalar. The return type matches the element-type of the vector input.

This instruction has the same comparison semantics as the ‘`llvm.minimum.*`’ intrinsic. That is, this intrinsic propagates NaNs and -0.0 is considered less than +0.0. If any element of the vector is a NaN, the result is NaN.

##### Arguments:

The argument to this intrinsic must be a vector of floating-point values.

Partial reductions of vectors can be expressed using the intrinsics described in this section. Each one reduces the concatenation of the two vector arguments down to the number of elements of the result vector type.

Other than the reduction operator (e.g. add, fadd), the way in which the concatenated arguments is reduced is entirely unspecified. By their nature these intrinsics are not expected to be useful in isolation but can instead be used to implement the first phase of an overall reduction operation.

The typical use case is loop vectorization where reductions are split into an in-loop phase, where maintaining an unordered vector result is important for performance, and an out-of-loop phase is required to calculate the final scalar result.

By avoiding the introduction of new ordering constraints, these intrinsics enhance the ability to leverage a target’s accumulation instructions.

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x i32> @llvm.vector.partial.reduce.add.v4i32.v4i32.v8i32(<4 x i32> %a, <8 x i32> %b)
declare <4 x i32> @llvm.vector.partial.reduce.add.v4i32.v4i32.v16i32(<4 x i32> %a, <16 x i32> %b)
declare <vscale x 4 x i32> @llvm.vector.partial.reduce.add.nxv4i32.nxv4i32.nxv8i32(<vscale x 4 x i32> %a, <vscale x 8 x i32> %b)
declare <vscale x 4 x i32> @llvm.vector.partial.reduce.add.nxv4i32.nxv4i32.nxv16i32(<vscale x 4 x i32> %a, <vscale x 16 x i32> %b)
```

##### Arguments:

The first argument is an integer vector with the same type as the result.

The second argument is a vector with a length that is a known integer multiple of the result’s type, while maintaining the same element type.

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x f32> @llvm.vector.partial.reduce.fadd.v4f32.v8f32(<4 x f32> %a, <8 x f32> %b)
declare <vscale x 4 x f32> @llvm.vector.partial.reduce.fadd.nxv4f32.nxv8f32(<vscale x 4 x f32> %a, <vscale x 8 x f32> %b)
```

##### Arguments:

The first argument is a floating-point vector with the same type as the result.

The second argument is a vector with a length that is a known integer multiple of the result’s type, while maintaining the same element type.

##### Semantics:

As the way in which the arguments to this floating-point intrinsic are reduced is unspecified, this intrinsic will assume floating-point reassociation and contraction can be leveraged to implement the reduction, which may result in variations to the results due to reordering or by lowering to different instructions (including combining multiple instructions into a single one).

##### Syntax:

This is an overloaded intrinsic.

```
; Insert fixed type into scalable type
declare <vscale x 4 x float> @llvm.vector.insert.nxv4f32.v4f32(<vscale x 4 x float> %vec, <4 x float> %subvec, i64 <idx>)
declare <vscale x 2 x double> @llvm.vector.insert.nxv2f64.v2f64(<vscale x 2 x double> %vec, <2 x double> %subvec, i64 <idx>)

; Insert scalable type into scalable type
declare <vscale x 4 x float> @llvm.vector.insert.nxv4f64.nxv2f64(<vscale x 4 x float> %vec, <vscale x 2 x float> %subvec, i64 <idx>)

; Insert fixed type into fixed type
declare <4 x double> @llvm.vector.insert.v4f64.v2f64(<4 x double> %vec, <2 x double> %subvec, i64 <idx>)
```

##### Overview:

The ‘`llvm.vector.insert.*`’ intrinsics insert a vector into another vector starting from a given index. The return type matches the type of the vector we insert into. Conceptually, this can be used to build a scalable vector out of non-scalable vectors, however this intrinsic can also be used on purely fixed types.

Scalable vectors can only be inserted into other scalable vectors.

##### Arguments:

The `vec` is the vector which `subvec` will be inserted into. The `subvec` is the vector that will be inserted.

`idx` represents the starting element number at which `subvec` will be inserted. `idx` must be a constant multiple of `subvec`’s known minimum vector length. If `subvec` is a scalable vector, `idx` is first scaled by the runtime scaling factor of `subvec`. The elements of `vec` starting at `idx` are overwritten with `subvec`. Elements `idx` through (`idx` + num_elements(`subvec`) - 1) must be valid `vec` indices. If this condition cannot be determined statically but is false at runtime, then the result vector is a poison value.

##### Syntax:

This is an overloaded intrinsic.

```
; Extract fixed type from scalable type
declare <4 x float> @llvm.vector.extract.v4f32.nxv4f32(<vscale x 4 x float> %vec, i64 <idx>)
declare <2 x double> @llvm.vector.extract.v2f64.nxv2f64(<vscale x 2 x double> %vec, i64 <idx>)

; Extract scalable type from scalable type
declare <vscale x 2 x float> @llvm.vector.extract.nxv2f32.nxv4f32(<vscale x 4 x float> %vec, i64 <idx>)

; Extract fixed type from fixed type
declare <2 x double> @llvm.vector.extract.v2f64.v4f64(<4 x double> %vec, i64 <idx>)
```

##### Overview:

The ‘`llvm.vector.extract.*`’ intrinsics extract a vector from within another vector starting from a given index. The return type must be explicitly specified. Conceptually, this can be used to decompose a scalable vector into non-scalable parts, however this intrinsic can also be used on purely fixed types.

Scalable vectors can only be extracted from other scalable vectors.

##### Arguments:

The `vec` is the vector from which we will extract a subvector.

The `idx` specifies the starting element number within `vec` from which a subvector is extracted. `idx` must be a constant multiple of the known-minimum vector length of the result type. If the result type is a scalable vector, `idx` is first scaled by the result type’s runtime scaling factor. Elements `idx` through (`idx` + num_elements(result_type) - 1) must be valid vector indices. If this condition cannot be determined statically but is false at runtime, then the result vector is a poison value. The `idx` parameter must be a vector index constant type (for most targets this will be an integer pointer type).

##### Syntax:

This is an overloaded intrinsic.

```
declare <2 x i8> @llvm.vector.reverse.v2i8(<2 x i8> %a)
declare <vscale x 4 x i32> @llvm.vector.reverse.nxv4i32(<vscale x 4 x i32> %a)
```

##### Overview:

The ‘`llvm.vector.reverse.*`’ intrinsics reverse a vector. The intrinsic takes a single vector and returns a vector of matching type but with the original lane order reversed. These intrinsics work for both fixed and scalable vectors. While this intrinsic supports all vector types the recommended way to express this operation for fixed-width vectors is still to use a shufflevector, as that may allow for more optimization opportunities.

##### Arguments:

The argument to this intrinsic must be a vector.

##### Syntax:

This is an overloaded intrinsic.

```
declare {<2 x double>, <2 x double>} @llvm.vector.deinterleave2.v4f64(<4 x double> %vec1)
declare {<vscale x 4 x i32>, <vscale x 4 x i32>}  @llvm.vector.deinterleave2.nxv8i32(<vscale x 8 x i32> %vec1)
declare {<vscale x 2 x i8>, <vscale x 2 x i8>, <vscale x 2 x i8>} @llvm.vector.deinterleave3.nxv6i8(<vscale x 6 x i8> %vec1)
declare {<2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>} @llvm.vector.deinterleave5.v10i32(<10 x i32> %vec1)
declare {<2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>, <2 x i32>} @llvm.vector.deinterleave7.v14i32(<14 x i32> %vec1)
```

##### Overview:

The ‘`llvm.vector.deinterleave2/3/4/5/6/7/8`’ intrinsics deinterleave adjacent lanes into 2 through to 8 separate vectors, respectively, and return them as the result.

This intrinsic works for both fixed and scalable vectors. While this intrinsic supports all vector types the recommended way to express this operation for factor of 2 on fixed-width vectors is still to use a shufflevector, as that may allow for more optimization opportunities.

For example:

```
{<2 x i64>, <2 x i64>} llvm.vector.deinterleave2.v4i64(<4 x i64> <i64 0, i64 1, i64 2, i64 3>); ==> {<2 x i64> <i64 0, i64 2>, <2 x i64> <i64 1, i64 3>}
{<2 x i32>, <2 x i32>, <2 x i32>} llvm.vector.deinterleave3.v6i32(<6 x i32> <i32 0, i32 1, i32 2, i32 3, i32 4, i32 5>)
  ; ==> {<2 x i32> <i32 0, i32 3>, <2 x i32> <i32 1, i32 4>, <2 x i32> <i32 2, i32 5>}
```

##### Arguments:

The argument is a vector whose type corresponds to the logical concatenation of the aggregated result types.

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x double> @llvm.vector.interleave2.v4f64(<2 x double> %vec1, <2 x double> %vec2)
declare <vscale x 8 x i32> @llvm.vector.interleave2.nxv8i32(<vscale x 4 x i32> %vec1, <vscale x 4 x i32> %vec2)
declare <vscale x 6 x i8> @llvm.vector.interleave3.nxv6i8(<vscale x 2 x i8> %vec0, <vscale x 2 x i8> %vec1, <vscale x 2 x i8> %vec2)
declare <10 x i32> @llvm.vector.interleave5.v10i32(<2 x i32> %vec0, <2 x i32> %vec1, <2 x i32> %vec2, <2 x i32> %vec3, <2 x i32> %vec4)
declare <14 x i32> @llvm.vector.interleave7.v14i32(<2 x i32> %vec0, <2 x i32> %vec1, <2 x i32> %vec2, <2 x i32> %vec3, <2 x i32> %vec4, <2 x i32> %vec5, <2 x i32> %vec6)
```

##### Overview:

The ‘`llvm.vector.interleave2/3/4/5/6/7/8`’ intrinsic constructs a vector by interleaving all the input vectors.

This intrinsic works for both fixed and scalable vectors. While this intrinsic supports all vector types the recommended way to express this operation for factor of 2 on fixed-width vectors is still to use a shufflevector, as that may allow for more optimization opportunities.

For example:

```
<4 x i64> llvm.vector.interleave2.v4i64(<2 x i64> <i64 0, i64 2>, <2 x i64> <i64 1, i64 3>); ==> <4 x i64> <i64 0, i64 1, i64 2, i64 3>
<6 x i32> llvm.vector.interleave3.v6i32(<2 x i32> <i32 0, i32 3>, <2 x i32> <i32 1, i32 4>, <2 x i32> <i32 2, i32 5>)
 ; ==> <6 x i32> <i32 0, i32 1, i32 2, i32 3, i32 4, i32 5>
```

##### Arguments:

All arguments must be vectors of the same type whereby their logical concatenation matches the result type.

##### Syntax:

This is an overloaded intrinsic.

```
declare <2 x double> @llvm.vector.splice.left.v2f64(<2 x double> %vec1, <2 x double> %vec2, i32 %offset)
declare <vscale x 4 x i32> @llvm.vector.splice.left.nxv4i32(<vscale x 4 x i32> %vec1, <vscale x 4 x i32> %vec2, i32 %offset)
```

##### Overview:

The ‘`llvm.vector.splice.left.*`’ intrinsics construct a vector by concatenating two vectors together, shifting the elements left by `offset`, and extracting the lower half.

These intrinsics work for both fixed and scalable vectors. While this intrinsic supports all vector types the recommended way to express this operation for fixed-width vectors with an immediate offset is still to use a shufflevector, as that may allow for more optimization opportunities.

For example:

```
llvm.vector.splice.left(<A,B,C,D>, <E,F,G,H>, 1);
                    ==> <A,B,C,D,E,F,G,H>
                    ==> <B,C,D,E,F,G,H,_>
                    ==> <B,C,D,E>
```

##### Arguments:

The first two operands are vectors with the same type. `offset` is an unsigned scalar i32 that determines how many elements to shift left by.

##### Semantics:

For a vector type with a runtime length of N, if `offset` > N then the result is a poison value.

##### Syntax:

This is an overloaded intrinsic.

```
declare <2 x double> @llvm.vector.splice.right.v2f64(<2 x double> %vec1, <2 x double> %vec2, i32 %offset)
declare <vscale x 4 x i32> @llvm.vector.splice.right.nxv4i32(<vscale x 4 x i32> %vec1, <vscale x 4 x i32> %vec2, i32 %offset)
```

##### Overview:

The ‘`llvm.vector.splice.right.*`’ intrinsics construct a vector by concatenating two vectors together, shifting the elements right by `offset`, and extracting the upper half.

These intrinsics work for both fixed and scalable vectors. While this intrinsic supports all vector types the recommended way to express this operation for fixed-width vectors with an immediate offset is still to use a shufflevector, as that may allow for more optimization opportunities.

For example:

```
llvm.vector.splice.right(<A,B,C,D>, <E,F,G,H>, 1);
                     ==> <A,B,C,D,E,F,G,H>
                     ==> <_,A,B,C,D,E,F,G>
                     ==>         <D,E,F,G>
```

##### Arguments:

The first two operands are vectors with the same type. `offset` is an unsigned scalar i32 that determines how many elements to shift right by.

##### Semantics:

For a vector type with a runtime length of N, if `offset` > N then the result is a poison value.

This is an overloaded intrinsic. You can use `llvm.stepvector` to generate a vector whose lane values comprise the linear sequence <0, 1, 2, …>. It is primarily intended for scalable vectors.

```
declare <vscale x 4 x i32> @llvm.stepvector.nxv4i32()
declare <vscale x 8 x i16> @llvm.stepvector.nxv8i16()
```

The ‘`llvm.stepvector`’ intrinsics are used to create vectors of integers whose elements contain a linear sequence of values starting from 0 with a step of 1. This intrinsic can only be used for vectors with integer elements that are at least 8 bits in size. If the sequence value exceeds the allowed limit for the element type then the result for that lane is truncated.

These intrinsics work for both fixed and scalable vectors. While this intrinsic supports all vector types, the recommended way to express this operation for fixed-width vectors is still to generate a constant vector instead.

##### Arguments:

None.

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x i1> @llvm.get.active.lane.mask.v4i1.i32(i32 %base, i32 %n)
declare <8 x i1> @llvm.get.active.lane.mask.v8i1.i64(i64 %base, i64 %n)
declare <16 x i1> @llvm.get.active.lane.mask.v16i1.i64(i64 %base, i64 %n)
declare <vscale x 16 x i1> @llvm.get.active.lane.mask.nxv16i1.i64(i64 %base, i64 %n)
```

##### Overview:

Create a mask representing active and inactive vector lanes.

##### Arguments:

Both arguments have the same scalar integer type. The result is a vector with the i1 element type.

##### Semantics:

The ‘`llvm.get.active.lane.mask.*`’ intrinsics are semantically equivalent to:

```
%m[i] = icmp ult (%base + i), %n
```

where `%m` is a vector (mask) of active/inactive lanes with its elements indexed by `i`, and `%base`, `%n` are the two arguments to `llvm.get.active.lane.mask.*`, `%icmp` is an integer compare and `ult` the unsigned less-than comparison operator. Overflow cannot occur in `(%base + i)` and its comparison against `%n` as it is performed in integer numbers and not in machine numbers. The above is equivalent to:

```
%m = @llvm.get.active.lane.mask(%base, %n)
```

This can, for example, be emitted by the loop vectorizer in which case `%base` is the first element of the vector induction variable (VIV) and `%n` is the loop tripcount. Thus, these intrinsics perform an element-wise less than comparison of VIV with the loop tripcount, producing a mask of true/false values representing active/inactive vector lanes, except if the VIV overflows in which case they return false in the lanes where the VIV overflows. The arguments are scalar types to accommodate scalable vector types, for which it is unknown what the type of the step vector needs to be that enumerate its lanes without overflow.

This mask `%m` can e.g., be used in masked load/store instructions. These intrinsics provide a hint to the backend. I.e., for a vector loop, the back-edge taken count of the original scalar loop is explicit as the second argument.

##### Examples:

```llvm
%active.lane.mask = call <4 x i1> @llvm.get.active.lane.mask.v4i1.i64(i64 %elem0, i64 429)
%wide.masked.load = call <4 x i32> @llvm.masked.load.v4i32.p0v4i32(ptr align 4 %3, <4 x i1> %active.lane.mask, <4 x i32> poison)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x i1> @llvm.loop.dependence.war.mask.v4i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
declare <8 x i1> @llvm.loop.dependence.war.mask.v8i1.i32(i32 %addrA, i32 %addrB, i32 immarg %elementSize)
declare <16 x i1> @llvm.loop.dependence.war.mask.v16i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
declare <vscale x 16 x i1> @llvm.loop.dependence.war.mask.nxv16i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
```

##### Overview:

Given a vector load from address %addrA followed by a vector store to address %addrB, this instruction generates a mask where an active lane indicates that the write-after-read sequence can be performed safely for that lane, without the danger of a write-after-read hazard occurring.

A write-after-read hazard occurs when a write-after-read sequence for a given lane in a vector ends up being executed as a read-after-write sequence due to the aliasing of pointers.

##### Arguments:

The first two arguments are integers and the last argument is an immediate. The result is a vector with the i1 element type.

##### Semantics:

`%elementSize` is the size of the accessed elements in bytes. The intrinsic returns `poison` if the distance between `%addrA` and `%addrB` is smaller than `VF * %elementsize` and either `%addrA + VF * %elementSize` or `%addrB + VF * %elementSize` wrap.
