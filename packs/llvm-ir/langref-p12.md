---
title: "LLVM Language Reference Manual (part 12/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 12/20
---

# LLVM Language Reference Manual

This function returns the same values as the libm `floor` functions would, and handles error conditions in the same way.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.ceil` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.ceil.f32(float  %Val)
declare double    @llvm.ceil.f64(double %Val)
declare x86_fp80  @llvm.ceil.f80(x86_fp80  %Val)
declare fp128     @llvm.ceil.f128(fp128 %Val)
declare ppc_fp128 @llvm.ceil.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.ceil.*`’ intrinsics return the ceiling of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `ceil` functions would, and handles error conditions in the same way.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.trunc` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.trunc.f32(float  %Val)
declare double    @llvm.trunc.f64(double %Val)
declare x86_fp80  @llvm.trunc.f80(x86_fp80  %Val)
declare fp128     @llvm.trunc.f128(fp128 %Val)
declare ppc_fp128 @llvm.trunc.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.trunc.*`’ intrinsics returns the operand rounded to the nearest integer not larger in magnitude than the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `trunc` functions would, and handles error conditions in the same way.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.rint` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.rint.f32(float  %Val)
declare double    @llvm.rint.f64(double %Val)
declare x86_fp80  @llvm.rint.f80(x86_fp80  %Val)
declare fp128     @llvm.rint.f128(fp128 %Val)
declare ppc_fp128 @llvm.rint.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.rint.*`’ intrinsics returns the operand rounded to the nearest integer. It may raise an inexact floating-point exception if the operand isn’t an integer.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `rint` functions would, and handles error conditions in the same way. Since LLVM assumes the default floating-point environment, the rounding mode is assumed to be set to “nearest”, so halfway cases are rounded to the even integer. Use Constrained Floating-Point Intrinsics to avoid that assumption.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.nearbyint` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.nearbyint.f32(float  %Val)
declare double    @llvm.nearbyint.f64(double %Val)
declare x86_fp80  @llvm.nearbyint.f80(x86_fp80  %Val)
declare fp128     @llvm.nearbyint.f128(fp128 %Val)
declare ppc_fp128 @llvm.nearbyint.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.nearbyint.*`’ intrinsics returns the operand rounded to the nearest integer.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `nearbyint` functions would, and handles error conditions in the same way. Since LLVM assumes the default floating-point environment, the rounding mode is assumed to be set to “nearest”, so halfway cases are rounded to the even integer. Use Constrained Floating-Point Intrinsics to avoid that assumption.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.round` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.round.f32(float  %Val)
declare double    @llvm.round.f64(double %Val)
declare x86_fp80  @llvm.round.f80(x86_fp80  %Val)
declare fp128     @llvm.round.f128(fp128 %Val)
declare ppc_fp128 @llvm.round.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.round.*`’ intrinsics returns the operand rounded to the nearest integer.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `round` functions would, and handles error conditions in the same way.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.roundeven` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.roundeven.f32(float  %Val)
declare double    @llvm.roundeven.f64(double %Val)
declare x86_fp80  @llvm.roundeven.f80(x86_fp80  %Val)
declare fp128     @llvm.roundeven.f128(fp128 %Val)
declare ppc_fp128 @llvm.roundeven.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.roundeven.*`’ intrinsics returns the operand rounded to the nearest integer in floating-point format rounding halfway cases to even (that is, to the nearest value that is an even integer).

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function implements IEEE 754 operation `roundToIntegralTiesToEven`. It also behaves in the same way as C standard function `roundeven`, including that it disregards rounding mode and does not raise floating point exceptions.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.lround` on any floating-point type or vector of floating-point type. Not all targets support all types however.

```
declare i32 @llvm.lround.i32.f32(float %Val)
declare i32 @llvm.lround.i32.f64(double %Val)
declare i32 @llvm.lround.i32.f80(x86_fp80 %Val)
declare i32 @llvm.lround.i32.f128(fp128 %Val)
declare i32 @llvm.lround.i32.ppcf128(ppc_fp128 %Val)

declare i64 @llvm.lround.i64.f32(float %Val)
declare i64 @llvm.lround.i64.f64(double %Val)
declare i64 @llvm.lround.i64.f80(x86_fp80 %Val)
declare i64 @llvm.lround.i64.f128(fp128 %Val)
declare i64 @llvm.lround.i64.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.lround.*`’ intrinsics return the operand rounded to the nearest integer with ties away from zero.

##### Arguments:

The argument is a floating-point number and the return value is an integer type.

##### Semantics:

This function returns the same values as the libm `lround` functions would, but without setting errno. If the rounded value is too large to be stored in the result type, the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.llround` on any floating-point type. Not all targets support all types however.

```
declare i64 @llvm.llround.i64.f32(float %Val)
declare i64 @llvm.llround.i64.f64(double %Val)
declare i64 @llvm.llround.i64.f80(x86_fp80 %Val)
declare i64 @llvm.llround.i64.f128(fp128 %Val)
declare i64 @llvm.llround.i64.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.llround.*`’ intrinsics return the operand rounded to the nearest integer with ties away from zero.

##### Arguments:

The argument is a floating-point number and the return value is an integer type.

##### Semantics:

This function returns the same values as the libm `llround` functions would, but without setting errno. If the rounded value is too large to be stored in the result type, the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.lrint` on any floating-point type or vector of floating-point type. Not all targets support all types however.

```
declare i32 @llvm.lrint.i32.f32(float %Val)
declare i32 @llvm.lrint.i32.f64(double %Val)
declare i32 @llvm.lrint.i32.f80(x86_fp80 %Val)
declare i32 @llvm.lrint.i32.f128(fp128 %Val)
declare i32 @llvm.lrint.i32.ppcf128(ppc_fp128 %Val)

declare i64 @llvm.lrint.i64.f32(float %Val)
declare i64 @llvm.lrint.i64.f64(double %Val)
declare i64 @llvm.lrint.i64.f80(x86_fp80 %Val)
declare i64 @llvm.lrint.i64.f128(fp128 %Val)
declare i64 @llvm.lrint.i64.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.lrint.*`’ intrinsics return the operand rounded to the nearest integer.

##### Arguments:

The argument is a floating-point number and the return value is an integer type.

##### Semantics:

This function returns the same values as the libm `lrint` functions would, but without setting errno. If the rounded value is too large to be stored in the result type, the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.llrint` on any floating-point type or vector of floating-point type. Not all targets support all types however.

```
declare i64 @llvm.llrint.i64.f32(float %Val)
declare i64 @llvm.llrint.i64.f64(double %Val)
declare i64 @llvm.llrint.i64.f80(x86_fp80 %Val)
declare i64 @llvm.llrint.i64.f128(fp128 %Val)
declare i64 @llvm.llrint.i64.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.llrint.*`’ intrinsics return the operand rounded to the nearest integer.

##### Arguments:

The argument is a floating-point number and the return value is an integer type.

##### Semantics:

This function returns the same values as the libm `llrint` functions would, but without setting errno. If the rounded value is too large to be stored in the result type, the return value is a non-deterministic value (equivalent to *freeze poison*).

LLVM provides intrinsics for a few important bit manipulation operations. These allow efficient code generation for some algorithms.

##### Syntax:

This is an overloaded intrinsic function. You can use bitreverse on any integer type.

```
declare i16 @llvm.bitreverse.i16(i16 <id>)
declare i32 @llvm.bitreverse.i32(i32 <id>)
declare i64 @llvm.bitreverse.i64(i64 <id>)
declare <4 x i32> @llvm.bitreverse.v4i32(<4 x i32> <id>)
```

##### Overview:

The ‘`llvm.bitreverse`’ family of intrinsics is used to reverse the bitpattern of an integer value or vector of integer values; for example `0b10110110` becomes `0b01101101`.

##### Semantics:

The `llvm.bitreverse.iN` intrinsic returns an iN value that has bit `M` in the input moved to bit `N-M-1` in the output. The vector intrinsics, such as `llvm.bitreverse.v4i32`, operate on a per-element basis and the element order is not affected.

##### Syntax:

This is an overloaded intrinsic function. You can use bswap on any integer type that is an even number of bytes (i.e., BitWidth % 16 == 0).

```
declare i16 @llvm.bswap.i16(i16 <id>)
declare i32 @llvm.bswap.i32(i32 <id>)
declare i64 @llvm.bswap.i64(i64 <id>)
declare <4 x i32> @llvm.bswap.v4i32(<4 x i32> <id>)
```

##### Overview:

The ‘`llvm.bswap`’ family of intrinsics is used to byte swap an integer value or vector of integer values with an even number of bytes (positive multiple of 16 bits).

##### Semantics:

The `llvm.bswap.i16` intrinsic returns an i16 value that has the high and low byte of the input i16 swapped. Similarly, the `llvm.bswap.i32` intrinsic returns an i32 value that has the four bytes of the input i32 swapped, so that if the input bytes are numbered 0, 1, 2, 3 then the returned i32 will have its bytes in 3, 2, 1, 0 order. The `llvm.bswap.i48`, `llvm.bswap.i64` and other intrinsics extend this concept to additional even-byte lengths (6 bytes, 8 bytes and more, respectively). The vector intrinsics, such as `llvm.bswap.v4i32`, operate on a per-element basis and the element order is not affected.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.ctpop` on any integer bit width, or on any vector with integer elements. Not all targets support all bit widths or vector types, however.

```
declare i8 @llvm.ctpop.i8(i8  <src>)
declare i16 @llvm.ctpop.i16(i16 <src>)
declare i32 @llvm.ctpop.i32(i32 <src>)
declare i64 @llvm.ctpop.i64(i64 <src>)
declare i256 @llvm.ctpop.i256(i256 <src>)
declare <2 x i32> @llvm.ctpop.v2i32(<2 x i32> <src>)
```

##### Overview:

The ‘`llvm.ctpop`’ family of intrinsics counts the number of bits set in a value.

##### Arguments:

The only argument is the value to be counted. The argument may be of any integer type, or a vector with integer elements. The return type must match the argument type.

##### Semantics:

The ‘`llvm.ctpop`’ intrinsic counts the 1’s in a variable, or within each element of a vector.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.ctlz` on any integer bit width, or any vector whose elements are integers. Not all targets support all bit widths or vector types, however.

```
declare i8   @llvm.ctlz.i8  (i8   <src>, i1 <is_zero_poison>)
declare <2 x i37> @llvm.ctlz.v2i37(<2 x i37> <src>, i1 <is_zero_poison>)
```

##### Overview:

The ‘`llvm.ctlz`’ family of intrinsic functions counts the number of leading zeros in a variable.

##### Arguments:

The first argument is the value to be counted. This argument may be of any integer type, or a vector with integer element type. The return type must match the first argument type.

The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is zero. If the first argument is zero and the second argument is true, the result is poison. Historically some architectures did not provide a defined result for zero values as efficiently, and many algorithms are now predicated on avoiding zero-value inputs.

##### Semantics:

The ‘`llvm.ctlz`’ intrinsic counts the leading (most significant) zeros in a variable, or within each element of the vector. If `src == 0` then the result is the size in bits of the type of `src` if `is_zero_poison == 0` and `poison` otherwise. For example, `llvm.ctlz(i32 2) = 30`.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.cttz` on any integer bit width, or any vector of integer elements. Not all targets support all bit widths or vector types, however.

```
declare i42   @llvm.cttz.i42  (i42   <src>, i1 <is_zero_poison>)
declare <2 x i32> @llvm.cttz.v2i32(<2 x i32> <src>, i1 <is_zero_poison>)
```

##### Overview:

The ‘`llvm.cttz`’ family of intrinsic functions counts the number of trailing zeros.

##### Arguments:

The first argument is the value to be counted. This argument may be of any integer type, or a vector with integer element type. The return type must match the first argument type.

The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is zero. If the first argument is zero and the second argument is true, the result is poison. Historically some architectures did not provide a defined result for zero values as efficiently, and many algorithms are now predicated on avoiding zero-value inputs.

##### Semantics:

The ‘`llvm.cttz`’ intrinsic counts the trailing (least significant) zeros in a variable, or within each element of a vector. If `src == 0` then the result is the size in bits of the type of `src` if `is_zero_poison == 0` and `poison` otherwise. For example, `llvm.cttz(2) = 1`.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fshl` on any integer bit width or any vector of integer elements. Not all targets support all bit widths or vector types, however.

```
declare i8  @llvm.fshl.i8 (i8 %a, i8 %b, i8 %c)
declare i64 @llvm.fshl.i64(i64 %a, i64 %b, i64 %c)
declare <2 x i32> @llvm.fshl.v2i32(<2 x i32> %a, <2 x i32> %b, <2 x i32> %c)
```

##### Overview:

The ‘`llvm.fshl`’ family of intrinsic functions performs a funnel shift left: the first two values are concatenated as { %a : %b } (%a is the most significant bits of the wide value), the combined value is shifted left, and the most significant bits are extracted to produce a result that is the same size as the original arguments. If the first 2 arguments are identical, this is equivalent to a rotate left operation. For vector types, the operation occurs for each element of the vector. The shift argument is treated as an unsigned amount modulo the element size of the arguments.

##### Arguments:

The first two arguments are the values to be concatenated. The third argument is the shift amount. The arguments may be any integer type or a vector with integer element type. All arguments and the return value must have the same type.

##### Example:

```
%r = call i8 @llvm.fshl.i8(i8 %x, i8 %y, i8 %z)  ; %r = i8: msb_extract((concat(x, y) << (z % 8)), 8)
%r = call i8 @llvm.fshl.i8(i8 255, i8 0, i8 15)  ; %r = i8: 128 (0b10000000)
%r = call i8 @llvm.fshl.i8(i8 15, i8 15, i8 11)  ; %r = i8: 120 (0b01111000)
%r = call i8 @llvm.fshl.i8(i8 0, i8 255, i8 8)   ; %r = i8: 0   (0b00000000)
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fshr` on any integer bit width or any vector of integer elements. Not all targets support all bit widths or vector types, however.

```
declare i8  @llvm.fshr.i8 (i8 %a, i8 %b, i8 %c)
declare i64 @llvm.fshr.i64(i64 %a, i64 %b, i64 %c)
declare <2 x i32> @llvm.fshr.v2i32(<2 x i32> %a, <2 x i32> %b, <2 x i32> %c)
```

##### Overview:

The ‘`llvm.fshr`’ family of intrinsic functions performs a funnel shift right: the first two values are concatenated as { %a : %b } (%a is the most significant bits of the wide value), the combined value is shifted right, and the least significant bits are extracted to produce a result that is the same size as the original arguments. If the first 2 arguments are identical, this is equivalent to a rotate right operation. For vector types, the operation occurs for each element of the vector. The shift argument is treated as an unsigned amount modulo the element size of the arguments.

##### Arguments:

The first two arguments are the values to be concatenated. The third argument is the shift amount. The arguments may be any integer type or a vector with integer element type. All arguments and the return value must have the same type.

##### Example:

```
%r = call i8 @llvm.fshr.i8(i8 %x, i8 %y, i8 %z)  ; %r = i8: lsb_extract((concat(x, y) >> (z % 8)), 8)
%r = call i8 @llvm.fshr.i8(i8 255, i8 0, i8 15)  ; %r = i8: 254 (0b11111110)
%r = call i8 @llvm.fshr.i8(i8 15, i8 15, i8 11)  ; %r = i8: 225 (0b11100001)
%r = call i8 @llvm.fshr.i8(i8 0, i8 255, i8 8)   ; %r = i8: 255 (0b11111111)
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.clmul` on any integer or vectors of integer elements.

```
declare i16 @llvm.clmul.i16(i16 %a, i16 %b)
declare i32 @llvm.clmul.i32(i32 %a, i32 %b)
declare i64 @llvm.clmul.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.clmul.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.clmul`’ family of intrinsic functions performs carry-less multiplication, or XOR multiplication, on the two arguments, and returns the low-bits.

##### Arguments:

The arguments may be any integer type or vector of integer type. Both arguments and result must have the same type.

##### Semantics:

The ‘`llvm.clmul`’ intrinsic computes carry-less multiply of its arguments, which is the result of applying the standard multiplication algorithm, where all of the additions are replaced with XORs, and returns the low-bits. The vector variants operate lane-wise.

##### Example:

```llvm
%r = call i4 @llvm.clmul.i4(i4 1, i4 2)    ; %r = 2
%r = call i4 @llvm.clmul.i4(i4 5, i4 6)    ; %r = 14
%r = call i4 @llvm.clmul.i4(i4 -4, i4 2)   ; %r = -8
%r = call i4 @llvm.clmul.i4(i4 -4, i4 -5)  ; %r = 4
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.pext` on any integer or integer vector type.

```
declare i32 @llvm.pext.i32(i32 %val, i32 %mask)
declare i64 @llvm.pext.i64(i64 %val, i64 %mask)
declare <4 x i32> @llvm.pext.v4i32(<4 x i32> %val, <4 x i32> %mask)
```

##### Overview:

The ‘`llvm.pext`’ family of intrinsic functions extracts the bits from `val` where the `mask` has bits set and packs them contiguously in the low bits of the result, same as the x86 `PEXT` instruction.

##### Arguments:

The arguments may be any integer type or vector of integer type. Both arguments and result must have the same type.

##### Semantics:

The ‘`llvm.pext`’ intrinsic extracts bits from the first argument `val` at the positions indicated by set bits in `mask`, and packs them contiguously into the low bits of the result. The remaining high bits of the result are zero.

Equivalently, if the set bit positions in `mask` (from LSB to MSB) are `p0, p1, ..., pk`, then the result bit `i` equals bit `pi` of `val`.

```
%r = call i8 @llvm.pext.i8(i8 0b10101010, i8 0b11001100) ; %r = 0b00001010
%r = call i8 @llvm.pext.i8(i8 0b11111111, i8 0b10101010) ; %r = 0b00001111
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.pdep` on any integer or integer vector type.

```
declare i32 @llvm.pdep.i32(i32 %val, i32 %mask)
declare i64 @llvm.pdep.i64(i64 %val, i64 %mask)
declare <4 x i32> @llvm.pdep.v4i32(<4 x i32> %val, <4 x i32> %mask)
```

##### Overview:

The ‘`llvm.pdep`’ family of intrinsic functions deposits the low bits of `val` into the result at the positions where `mask` has bits set, same as the x86 `PDEP` instruction.

##### Arguments:

The arguments may be any integer type or vector of integer type. Both arguments and result must have the same type.

##### Semantics:

The ‘`llvm.pdep`’ intrinsic takes the low bits of the first argument `val` and scatters them to the bit positions in the result indicated by set bits in `mask`. Bits in the result at positions where `mask` is zero are zero.

Equivalently, if the set bit positions in `mask` (from LSB to MSB) are `p0, p1, ..., pk`, then result bit `pi` equals bit `i` of `val`.

The operations satisfy the round-trip identity: `pdep(pext(val, mask), mask) == val & mask`.

```
%r = call i8 @llvm.pdep.i8(i8 0b00001010, i8 0b11001100) ; %r = 0b10001000
%r = call i8 @llvm.pdep.i8(i8 0b00001111, i8 0b10101010) ; %r = 0b10101010
```

LLVM provides intrinsics for fast arithmetic overflow checking.

Each of these intrinsics returns a two-element struct. The first element of this struct contains the result of the corresponding arithmetic operation modulo 2n, where n is the bit width of the result. Therefore, for example, the first element of the struct returned by `llvm.sadd.with.overflow.i32` is always the same as the result of a 32-bit `add` instruction with the same operands, where the `add` is *not* modified by an `nsw` or `nuw` flag.

The second element of the result is an `i1` that is 1 if the arithmetic operation overflowed and 0 otherwise. An operation overflows if, for any values of its operands `A` and `B` and for any `N` larger than the operands’ width, `ext(A op B) to iN` is not equal to `(ext(A) to iN) op (ext(B) to iN)` where `ext` is `sext` for signed overflow and `zext` for unsigned overflow, and `op` is the underlying arithmetic operation.

The behavior of these intrinsics is well-defined for all argument values.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sadd.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.sadd.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.sadd.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.sadd.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.sadd.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.sadd.with.overflow`’ family of intrinsic functions perform a signed addition of the two arguments, and indicate whether an overflow occurred during the signed summation.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo signed addition.

##### Semantics:

The ‘`llvm.sadd.with.overflow`’ family of intrinsic functions perform a signed addition of the two variables. They return a structure — the first element of which is the signed summation, and the second element of which is a bit specifying if the signed summation resulted in an overflow.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.sadd.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %overflow, label %normal
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.uadd.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.uadd.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.uadd.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.uadd.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.uadd.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.uadd.with.overflow`’ family of intrinsic functions perform an unsigned addition of the two arguments, and indicate whether a carry occurred during the unsigned summation.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo unsigned addition.

##### Semantics:

The ‘`llvm.uadd.with.overflow`’ family of intrinsic functions perform an unsigned addition of the two arguments. They return a structure — the first element of which is the sum, and the second element of which is a bit specifying if the unsigned summation resulted in a carry.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.uadd.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %carry, label %normal
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.ssub.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.ssub.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.ssub.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.ssub.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.ssub.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.ssub.with.overflow`’ family of intrinsic functions perform a signed subtraction of the two arguments, and indicate whether an overflow occurred during the signed subtraction.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo signed subtraction.

##### Semantics:

The ‘`llvm.ssub.with.overflow`’ family of intrinsic functions perform a signed subtraction of the two arguments. They return a structure — the first element of which is the subtraction, and the second element of which is a bit specifying if the signed subtraction resulted in an overflow.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.ssub.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %overflow, label %normal
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.usub.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.usub.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.usub.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.usub.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.usub.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.usub.with.overflow`’ family of intrinsic functions perform an unsigned subtraction of the two arguments, and indicate whether an overflow occurred during the unsigned subtraction.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo unsigned subtraction.

##### Semantics:

The ‘`llvm.usub.with.overflow`’ family of intrinsic functions perform an unsigned subtraction of the two arguments. They return a structure — the first element of which is the subtraction, and the second element of which is a bit specifying if the unsigned subtraction resulted in an overflow.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.usub.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %overflow, label %normal
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.smul.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.smul.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.smul.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.smul.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.smul.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.smul.with.overflow`’ family of intrinsic functions perform a signed multiplication of the two arguments, and indicate whether an overflow occurred during the signed multiplication.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo signed multiplication.

##### Semantics:

The ‘`llvm.smul.with.overflow`’ family of intrinsic functions perform a signed multiplication of the two arguments. They return a structure — the first element of which is the multiplication, and the second element of which is a bit specifying if the signed multiplication resulted in an overflow.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.smul.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %overflow, label %normal
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.umul.with.overflow` on any integer bit width or vectors of integers.

```
declare {i16, i1} @llvm.umul.with.overflow.i16(i16 %a, i16 %b)
declare {i32, i1} @llvm.umul.with.overflow.i32(i32 %a, i32 %b)
declare {i64, i1} @llvm.umul.with.overflow.i64(i64 %a, i64 %b)
declare {<4 x i32>, <4 x i1>} @llvm.umul.with.overflow.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

The ‘`llvm.umul.with.overflow`’ family of intrinsic functions perform an unsigned multiplication of the two arguments, and indicate whether an overflow occurred during the unsigned multiplication.

##### Arguments:

The arguments (%a and %b) and the first element of the result structure may be of integer types of any bit width, but they must have the same bit width. The second element of the result structure must be of type `i1`. `%a` and `%b` are the two values that will undergo unsigned multiplication.

##### Semantics:

The ‘`llvm.umul.with.overflow`’ family of intrinsic functions perform an unsigned multiplication of the two arguments. They return a structure — the first element of which is the multiplication, and the second element of which is a bit specifying if the unsigned multiplication resulted in an overflow.

##### Examples:

```llvm
%res = call {i32, i1} @llvm.umul.with.overflow.i32(i32 %a, i32 %b)
%sum = extractvalue {i32, i1} %res, 0
%obit = extractvalue {i32, i1} %res, 1
br i1 %obit, label %overflow, label %normal
```

Saturation arithmetic is a version of arithmetic in which operations are limited to a fixed range between a minimum and maximum value. If the result of an operation is greater than the maximum value, the result is set (or “clamped”) to this maximum. If it is below the minimum, it is clamped to this minimum.

##### Syntax

This is an overloaded intrinsic. You can use `llvm.sadd.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.sadd.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.sadd.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.sadd.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.sadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.sadd.sat`’ family of intrinsic functions perform signed saturating addition on the 2 arguments.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo signed addition.

##### Semantics:

The maximum value this operation can clamp to is the largest signed value representable by the bit width of the arguments. The minimum value is the smallest signed value representable by this bit width.

##### Examples

```llvm
%res = call i4 @llvm.sadd.sat.i4(i4 1, i4 2)  ; %res = 3
%res = call i4 @llvm.sadd.sat.i4(i4 5, i4 6)  ; %res = 7
%res = call i4 @llvm.sadd.sat.i4(i4 -4, i4 2)  ; %res = -2
%res = call i4 @llvm.sadd.sat.i4(i4 -4, i4 -5)  ; %res = -8
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.uadd.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.uadd.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.uadd.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.uadd.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.uadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.uadd.sat`’ family of intrinsic functions perform unsigned saturating addition on the 2 arguments.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo unsigned addition.

##### Semantics:

The maximum value this operation can clamp to is the largest unsigned value representable by the bit width of the arguments. Because this is an unsigned operation, the result will never saturate towards zero.

##### Examples

```llvm
%res = call i4 @llvm.uadd.sat.i4(i4 1, i4 2)  ; %res = 3
%res = call i4 @llvm.uadd.sat.i4(i4 5, i4 6)  ; %res = 11
%res = call i4 @llvm.uadd.sat.i4(i4 8, i4 8)  ; %res = 15
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.ssub.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.ssub.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.ssub.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.ssub.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.ssub.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.ssub.sat`’ family of intrinsic functions perform signed saturating subtraction on the 2 arguments.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo signed subtraction.

##### Semantics:

The maximum value this operation can clamp to is the largest signed value representable by the bit width of the arguments. The minimum value is the smallest signed value representable by this bit width.

##### Examples

```llvm
%res = call i4 @llvm.ssub.sat.i4(i4 2, i4 1)  ; %res = 1
%res = call i4 @llvm.ssub.sat.i4(i4 2, i4 6)  ; %res = -4
%res = call i4 @llvm.ssub.sat.i4(i4 -4, i4 5)  ; %res = -8
%res = call i4 @llvm.ssub.sat.i4(i4 4, i4 -5)  ; %res = 7
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.usub.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.usub.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.usub.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.usub.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.usub.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.usub.sat`’ family of intrinsic functions perform unsigned saturating subtraction on the 2 arguments.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo unsigned subtraction.

##### Semantics:

The minimum value this operation can clamp to is 0, which is the smallest unsigned value representable by the bit width of the unsigned arguments. Because this is an unsigned operation, the result will never saturate towards the largest possible value representable by this bit width.

##### Examples

```llvm
%res = call i4 @llvm.usub.sat.i4(i4 2, i4 1)  ; %res = 1
%res = call i4 @llvm.usub.sat.i4(i4 2, i4 6)  ; %res = 0
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.sshl.sat` on integers or vectors of integers of any bit width.

```
declare i16 @llvm.sshl.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.sshl.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.sshl.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.sshl.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.sshl.sat`’ family of intrinsic functions perform signed saturating left shift on the first argument.

##### Arguments

The arguments (`%a` and `%b`) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` is the value to be shifted, and `%b` is the amount to shift by. If `b` is (statically or dynamically) equal to or larger than the integer bit width of the arguments, the result is a poison value. If the arguments are vectors, each vector element of `a` is shifted by the corresponding shift amount in `b`.

##### Semantics:

The maximum value this operation can clamp to is the largest signed value representable by the bit width of the arguments. The minimum value is the smallest signed value representable by this bit width.

##### Examples

```llvm
%res = call i4 @llvm.sshl.sat.i4(i4 2, i4 1)  ; %res = 4
%res = call i4 @llvm.sshl.sat.i4(i4 2, i4 2)  ; %res = 7
%res = call i4 @llvm.sshl.sat.i4(i4 -5, i4 1)  ; %res = -8
%res = call i4 @llvm.sshl.sat.i4(i4 -1, i4 1)  ; %res = -2
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.ushl.sat` on integers or vectors of integers of any bit width.

```
declare i16 @llvm.ushl.sat.i16(i16 %a, i16 %b)
declare i32 @llvm.ushl.sat.i32(i32 %a, i32 %b)
declare i64 @llvm.ushl.sat.i64(i64 %a, i64 %b)
declare <4 x i32> @llvm.ushl.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview

The ‘`llvm.ushl.sat`’ family of intrinsic functions perform unsigned saturating left shift on the first argument.

##### Arguments

The arguments (`%a` and `%b`) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` is the value to be shifted, and `%b` is the amount to shift by. If `b` is (statically or dynamically) equal to or larger than the integer bit width of the arguments, the result is a poison value. If the arguments are vectors, each vector element of `a` is shifted by the corresponding shift amount in `b`.

##### Semantics:

The maximum value this operation can clamp to is the largest unsigned value representable by the bit width of the arguments.

##### Examples

```llvm
%res = call i4 @llvm.ushl.sat.i4(i4 2, i4 1)  ; %res = 4
%res = call i4 @llvm.ushl.sat.i4(i4 3, i4 3)  ; %res = 15
```

A fixed point number represents a real data type for a number that has a fixed number of digits after a radix point (equivalent to the decimal point ‘.’). The number of digits after the radix point is referred as the *scale*. These are useful for representing fractional values to a specific precision. The following intrinsics perform fixed point arithmetic operations on 2 operands of the same scale, specified as the third argument.

The `llvm.*mul.fix` family of intrinsic functions represents a multiplication of fixed point numbers through scaled integers. Therefore, fixed point multiplication can be represented as

```llvm
%result = call i4 @llvm.smul.fix.i4(i4 %a, i4 %b, i32 %scale)

; Expands to
%a2 = sext i4 %a to i8
%b2 = sext i4 %b to i8
%mul = mul nsw nuw i8 %a2, %b2
%scale2 = trunc i32 %scale to i8
%r = ashr i8 %mul, i8 %scale2  ; this is for a target rounding down towards negative infinity
%result = trunc i8 %r to i4
```

The `llvm.*div.fix` family of intrinsic functions represents a division of fixed point numbers through scaled integers. Fixed point division can be represented as:

```llvm
%result call i4 @llvm.sdiv.fix.i4(i4 %a, i4 %b, i32 %scale)

; Expands to
%a2 = sext i4 %a to i8
%b2 = sext i4 %b to i8
%scale2 = trunc i32 %scale to i8
%a3 = shl i8 %a2, %scale2
%r = sdiv i8 %a3, %b2 ; this is for a target rounding towards zero
%result = trunc i8 %r to i4
```

For each of these functions, if the result cannot be represented exactly with the provided scale, the result is rounded. Rounding is unspecified since preferred rounding may vary for different targets. Rounding is specified through a target hook. Different pipelines should legalize or optimize this using the rounding specified by this hook if it is provided. Operations like constant folding, instruction combining, KnownBits, and ValueTracking should also use this hook, if provided, and not assume the direction of rounding. A rounded result must always be within one unit of precision from the true result. That is, the error between the returned result and the true result must be less than 1/2^(scale).

##### Syntax

This is an overloaded intrinsic. You can use `llvm.smul.fix` on any integer bit width or vectors of integers.

```
declare i16 @llvm.smul.fix.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.smul.fix.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.smul.fix.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.smul.fix.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.smul.fix`’ family of intrinsic functions perform signed fixed point multiplication on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. The arguments may also work with int vectors of the same length and int size. `%a` and `%b` are the two values that will undergo signed fixed point multiplication. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point multiplication on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

It is undefined behavior if the result value does not fit within the range of the fixed point type.

##### Examples

```llvm
%res = call i4 @llvm.smul.fix.i4(i4 3, i4 2, i32 0)  ; %res = 6 (2 x 3 = 6)
%res = call i4 @llvm.smul.fix.i4(i4 3, i4 2, i32 1)  ; %res = 3 (1.5 x 1 = 1.5)
%res = call i4 @llvm.smul.fix.i4(i4 3, i4 -2, i32 1)  ; %res = -3 (1.5 x -1 = -1.5)

; The result in the following could be rounded up to -2 or down to -2.5
%res = call i4 @llvm.smul.fix.i4(i4 3, i4 -3, i32 1)  ; %res = -5 (or -4) (1.5 x -1.5 = -2.25)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.umul.fix` on any integer bit width or vectors of integers.

```
declare i16 @llvm.umul.fix.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.umul.fix.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.umul.fix.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.umul.fix.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.umul.fix`’ family of intrinsic functions perform unsigned fixed point multiplication on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. The arguments may also work with int vectors of the same length and int size. `%a` and `%b` are the two values that will undergo unsigned fixed point multiplication. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs unsigned fixed point multiplication on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

It is undefined behavior if the result value does not fit within the range of the fixed point type.

##### Examples

```llvm
%res = call i4 @llvm.umul.fix.i4(i4 3, i4 2, i32 0)  ; %res = 6 (2 x 3 = 6)
%res = call i4 @llvm.umul.fix.i4(i4 3, i4 2, i32 1)  ; %res = 3 (1.5 x 1 = 1.5)

; The result in the following could be rounded down to 3.5 or up to 4
%res = call i4 @llvm.umul.fix.i4(i4 15, i4 1, i32 1)  ; %res = 7 (or 8) (7.5 x 0.5 = 3.75)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.smul.fix.sat` on any integer bit width or vectors of integers.

```
declare i16 @llvm.smul.fix.sat.i16(i16 %a, i16 %b, i32 %scale)
declare i32 @llvm.smul.fix.sat.i32(i32 %a, i32 %b, i32 %scale)
declare i64 @llvm.smul.fix.sat.i64(i64 %a, i64 %b, i32 %scale)
declare <4 x i32> @llvm.smul.fix.sat.v4i32(<4 x i32> %a, <4 x i32> %b, i32 %scale)
```

##### Overview

The ‘`llvm.smul.fix.sat`’ family of intrinsic functions perform signed fixed point saturating multiplication on 2 arguments of the same scale.

##### Arguments

The arguments (%a and %b) and the result may be of integer types of any bit width, but they must have the same bit width. `%a` and `%b` are the two values that will undergo signed fixed point multiplication. The argument `%scale` represents the scale of both operands, and must be a constant integer.

##### Semantics:

This operation performs fixed point multiplication on the 2 arguments of a specified scale. The result will also be returned in the same scale specified in the third argument.

If the result value cannot be precisely represented in the given scale, the value is rounded up or down to the closest representable value. The rounding direction is unspecified.

The maximum value this operation can clamp to is the largest signed value representable by the bit width of the first 2 arguments. The minimum value is the smallest signed value representable by this bit width.

##### Examples

```llvm
%res = call i4 @llvm.smul.fix.sat.i4(i4 3, i4 2, i32 0)  ; %res = 6 (2 x 3 = 6)
%res = call i4 @llvm.smul.fix.sat.i4(i4 3, i4 2, i32 1)  ; %res = 3 (1.5 x 1 = 1.5)
%res = call i4 @llvm.smul.fix.sat.i4(i4 3, i4 -2, i32 1)  ; %res = -3 (1.5 x -1 = -1.5)

; The result in the following could be rounded up to -2 or down to -2.5
%res = call i4 @llvm.smul.fix.sat.i4(i4 3, i4 -3, i32 1)  ; %res = -5 (or -4) (1.5 x -1.5 = -2.25)

; Saturation
%res = call i4 @llvm.smul.fix.sat.i4(i4 7, i4 2, i32 0)  ; %res = 7
%res = call i4 @llvm.smul.fix.sat.i4(i4 7, i4 4, i32 2)  ; %res = 7
%res = call i4 @llvm.smul.fix.sat.i4(i4 -8, i4 5, i32 2)  ; %res = -8
%res = call i4 @llvm.smul.fix.sat.i4(i4 -8, i4 -2, i32 1)  ; %res = 7

; Scale can affect the saturation result
%res = call i4 @llvm.smul.fix.sat.i4(i4 2, i4 4, i32 0)  ; %res = 7 (2 x 4 -> clamped to 7)
%res = call i4 @llvm.smul.fix.sat.i4(i4 2, i4 4, i32 1)  ; %res = 4 (1 x 2 = 2)
```

##### Syntax

This is an overloaded intrinsic. You can use `llvm.umul.fix.sat` on any integer bit width or vectors of integers.
