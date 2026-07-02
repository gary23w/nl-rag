---
title: "LLVM Language Reference Manual (part 11/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 11/20
---

# LLVM Language Reference Manual

Note that, unlike the standard libc function, the `llvm.memcpy.inline.*` intrinsics do not return a value, takes extra isvolatile arguments and the pointers can be in specified address spaces.

##### Arguments:

The first argument is a pointer to the destination, the second is a pointer to the source. The third argument is an integer argument specifying the number of bytes to copy, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first and second arguments.

If the `isvolatile` parameter is `true`, the `llvm.memcpy.inline` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.memcpy.inline.*`’ intrinsics copy a block of memory from the source location to the destination location, which are not allowed to overlap. It copies “len” bytes of memory over. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument. The behavior of ‘`llvm.memcpy.inline.*`’ is equivalent to the behavior of ‘`llvm.memcpy.*`’, but the generated code is guaranteed not to call any external functions.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memmove` on any integer bit width and for different address space. Not all targets support all bit widths however.

```
declare void @llvm.memmove.p0.p0.i32(ptr <dest>, ptr <src>,
                                     i32 <len>, i1 <isvolatile>)
declare void @llvm.memmove.p0.p0.i64(ptr <dest>, ptr <src>,
                                     i64 <len>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.memmove.*`’ intrinsics move a block of memory from the source location to the destination location. It is similar to the ‘`llvm.memcpy`’ intrinsic but allows the two memory locations to overlap.

Note that, unlike the standard libc function, the `llvm.memmove.*` intrinsics do not return a value, takes an extra isvolatile argument and the pointers can be in specified address spaces.

##### Arguments:

The first argument is a pointer to the destination, the second is a pointer to the source. The third argument is an integer argument specifying the number of bytes to copy, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first and second arguments.

If the `isvolatile` parameter is `true`, the `llvm.memmove` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.memmove.*`’ intrinsics copy a block of memory from the source location to the destination location, which may overlap. It copies “len” bytes of memory over. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

If `<len>` is 0, it is no-op modulo the behavior of attributes attached to the arguments. If `<len>` is not a well-defined value, the behavior is undefined. If `<len>` is not zero, both `<dest>` and `<src>` should be well-defined, otherwise the behavior is undefined.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memset` on any integer bit width and for different address spaces. However, not all targets support all bit widths.

```
declare void @llvm.memset.p0.i32(ptr <dest>, i8 <val>,
                                 i32 <len>, i1 <isvolatile>)
declare void @llvm.memset.p0.i64(ptr <dest>, i8 <val>,
                                 i64 <len>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.memset.*`’ intrinsics fill a block of memory with a particular byte value.

Note that, unlike the standard libc function, the `llvm.memset` intrinsic does not return a value and takes an extra volatile argument. Also, the destination can be in an arbitrary address space.

##### Arguments:

The first argument is a pointer to the destination to fill, the second is the byte value with which to fill it, the third argument is an integer argument specifying the number of bytes to fill, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first arguments.

If the `isvolatile` parameter is `true`, the `llvm.memset` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.memset.*`’ intrinsics fill “len” bytes of memory starting at the destination location. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

If `<len>` is 0, it is no-op modulo the behavior of attributes attached to the arguments. If `<len>` is not a well-defined value, the behavior is undefined. If `<len>` is not zero, `<dest>` should be well-defined, otherwise the behavior is undefined.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memset.inline` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memset.inline.p0.i32(ptr <dest>, i8 <val>,
                                        i32 <len>, i1 <isvolatile>)
declare void @llvm.memset.inline.p0.i64(ptr <dest>, i8 <val>,
                                        i64 <len>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.memset.inline.*`’ intrinsics fill a block of memory with a particular byte value and guarantees that no external functions are called.

Note that, unlike the standard libc function, the `llvm.memset.inline.*` intrinsics do not return a value, take an extra isvolatile argument and the pointer can be in specified address spaces.

##### Arguments:

The first argument is a pointer to the destination to fill, the second is the byte value with which to fill it, the third argument is an integer argument specifying the number of bytes to fill, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first argument.

If the `isvolatile` parameter is `true`, the `llvm.memset.inline` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.memset.inline.*`’ intrinsics fill “len” bytes of memory starting at the destination location. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

If `<len>` is 0, it is no-op modulo the behavior of attributes attached to the arguments. If `<len>` is not a well-defined value, the behavior is undefined. If `<len>` is not zero, `<dest>` should be well-defined, otherwise the behavior is undefined.

The behavior of ‘`llvm.memset.inline.*`’ is equivalent to the behavior of ‘`llvm.memset.*`’, but the generated code is guaranteed not to call any external functions.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.experimental.memset.pattern` on any sized type and for different address spaces.

```
declare void @llvm.experimental.memset.pattern.p0.i128.i64(ptr <dest>, i128 <val>,
                                                           i64 <count>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.experimental.memset.pattern.*`’ intrinsics fill a block of memory with a particular value. This may be expanded to an inline loop, a sequence of stores, or a libcall depending on what is available for the target and the expected performance and code size impact.

##### Arguments:

The first argument is a pointer to the destination to fill, the second is the value with which to fill it, the third argument is an integer argument specifying the number of times to fill the value, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first argument.

If the `isvolatile` parameter is `true`, the `llvm.experimental.memset.pattern` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.experimental.memset.pattern*`’ intrinsic fills memory starting at the destination location with the given pattern `<count>` times, incrementing by the allocation size of the type each time. The stores follow the usual semantics of store instructions, including regarding endianness and padding. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

If `<count>` is 0, it is no-op modulo the behavior of attributes attached to the arguments. If `<count>` is not a well-defined value, the behavior is undefined. If `<count>` is not zero, `<dest>` should be well-defined, otherwise the behavior is undefined.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sqrt` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.sqrt.f32(float %Val)
declare double    @llvm.sqrt.f64(double %Val)
declare x86_fp80  @llvm.sqrt.f80(x86_fp80 %Val)
declare fp128     @llvm.sqrt.f128(fp128 %Val)
declare ppc_fp128 @llvm.sqrt.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.sqrt`’ intrinsics return the square root of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`sqrt`’ function but without trapping or setting `errno`. For types specified by IEEE 754, the result matches a conforming libm implementation.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.powi` on any floating-point or vector of floating-point type. Not all targets support all types however.

Generally, the only supported type for the exponent is the one matching with the C type `int`.

```
declare float     @llvm.powi.f32.i32(float  %Val, i32 %power)
declare double    @llvm.powi.f64.i16(double %Val, i16 %power)
declare x86_fp80  @llvm.powi.f80.i32(x86_fp80  %Val, i32 %power)
declare fp128     @llvm.powi.f128.i32(fp128 %Val, i32 %power)
declare ppc_fp128 @llvm.powi.ppcf128.i32(ppc_fp128  %Val, i32 %power)
```

##### Overview:

The ‘`llvm.powi.*`’ intrinsics return the first operand raised to the specified (positive or negative) power. The order of evaluation of multiplications is not defined. When a vector of floating-point type is used, the second argument remains a scalar integer value.

##### Arguments:

The second argument is an integer power, and the first is a value to raise to that power.

##### Semantics:

This function returns the first value raised to the second power with an unspecified sequence of rounding operations.

Note that the *powi* function is unusual in that NaN inputs can lead to non-NaN results, and this depends on the kind of NaN (quiet vs signaling). Due to how LLVM treats NaN values in non-constrained functions, the function may non-deterministically treat signaling NaNs as quiet NaNs. For example, *powi(QNaN, 0)* returns *1.0*, and *powi(SNaN, 0)* may non-deterministically return *1.0* or a NaN.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sin` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.sin.f32(float  %Val)
declare double    @llvm.sin.f64(double %Val)
declare x86_fp80  @llvm.sin.f80(x86_fp80  %Val)
declare fp128     @llvm.sin.f128(fp128 %Val)
declare ppc_fp128 @llvm.sin.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.sin.*`’ intrinsics return the sine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`sin`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.cos` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.cos.f32(float  %Val)
declare double    @llvm.cos.f64(double %Val)
declare x86_fp80  @llvm.cos.f80(x86_fp80  %Val)
declare fp128     @llvm.cos.f128(fp128 %Val)
declare ppc_fp128 @llvm.cos.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.cos.*`’ intrinsics return the cosine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`cos`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.tan` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.tan.f32(float  %Val)
declare double    @llvm.tan.f64(double %Val)
declare x86_fp80  @llvm.tan.f80(x86_fp80  %Val)
declare fp128     @llvm.tan.f128(fp128 %Val)
declare ppc_fp128 @llvm.tan.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.tan.*`’ intrinsics return the tangent of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`tan`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.asin` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.asin.f32(float  %Val)
declare double    @llvm.asin.f64(double %Val)
declare x86_fp80  @llvm.asin.f80(x86_fp80  %Val)
declare fp128     @llvm.asin.f128(fp128 %Val)
declare ppc_fp128 @llvm.asin.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.asin.*`’ intrinsics return the arcsine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`asin`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.acos` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.acos.f32(float  %Val)
declare double    @llvm.acos.f64(double %Val)
declare x86_fp80  @llvm.acos.f80(x86_fp80  %Val)
declare fp128     @llvm.acos.f128(fp128 %Val)
declare ppc_fp128 @llvm.acos.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.acos.*`’ intrinsics return the arccosine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`acos`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.atan` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.atan.f32(float  %Val)
declare double    @llvm.atan.f64(double %Val)
declare x86_fp80  @llvm.atan.f80(x86_fp80  %Val)
declare fp128     @llvm.atan.f128(fp128 %Val)
declare ppc_fp128 @llvm.atan.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.atan.*`’ intrinsics return the arctangent of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`atan`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.atan2` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.atan2.f32(float  %Y, float %X)
declare double    @llvm.atan2.f64(double %Y, double %X)
declare x86_fp80  @llvm.atan2.f80(x86_fp80  %Y, x86_fp80 %X)
declare fp128     @llvm.atan2.f128(fp128 %Y, fp128 %X)
declare ppc_fp128 @llvm.atan2.ppcf128(ppc_fp128  %Y, ppc_fp128 %X)
```

##### Overview:

The ‘`llvm.atan2.*`’ intrinsics return the arctangent of `Y/X` accounting for the quadrant.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`atan2`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sinh` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.sinh.f32(float  %Val)
declare double    @llvm.sinh.f64(double %Val)
declare x86_fp80  @llvm.sinh.f80(x86_fp80  %Val)
declare fp128     @llvm.sinh.f128(fp128 %Val)
declare ppc_fp128 @llvm.sinh.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.sinh.*`’ intrinsics return the hyperbolic sine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`sinh`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.cosh` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.cosh.f32(float  %Val)
declare double    @llvm.cosh.f64(double %Val)
declare x86_fp80  @llvm.cosh.f80(x86_fp80  %Val)
declare fp128     @llvm.cosh.f128(fp128 %Val)
declare ppc_fp128 @llvm.cosh.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.cosh.*`’ intrinsics return the hyperbolic cosine of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`cosh`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.tanh` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.tanh.f32(float  %Val)
declare double    @llvm.tanh.f64(double %Val)
declare x86_fp80  @llvm.tanh.f80(x86_fp80  %Val)
declare fp128     @llvm.tanh.f128(fp128 %Val)
declare ppc_fp128 @llvm.tanh.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.tanh.*`’ intrinsics return the hyperbolic tangent of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`tanh`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sincos` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare { float, float }          @llvm.sincos.f32(float  %Val)
declare { double, double }        @llvm.sincos.f64(double %Val)
declare { x86_fp80, x86_fp80 }    @llvm.sincos.f80(x86_fp80  %Val)
declare { fp128, fp128 }          @llvm.sincos.f128(fp128 %Val)
declare { ppc_fp128, ppc_fp128 }  @llvm.sincos.ppcf128(ppc_fp128  %Val)
declare { <4 x float>, <4 x float> } @llvm.sincos.v4f32(<4 x float>  %Val)
```

##### Overview:

The ‘`llvm.sincos.*`’ intrinsics returns the sine and cosine of the operand.

##### Arguments:

The argument is a floating-point value or vector of floating-point values. Returns two values matching the argument type in a struct.

##### Semantics:

This intrinsic is equivalent to a calling both llvm.sin and llvm.cos on the argument.

The first result is the sine of the argument and the second result is the cosine of the argument.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.sincospi` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare { float, float }          @llvm.sincospi.f32(float  %Val)
declare { double, double }        @llvm.sincospi.f64(double %Val)
declare { x86_fp80, x86_fp80 }    @llvm.sincospi.f80(x86_fp80  %Val)
declare { fp128, fp128 }          @llvm.sincospi.f128(fp128 %Val)
declare { ppc_fp128, ppc_fp128 }  @llvm.sincospi.ppcf128(ppc_fp128  %Val)
declare { <4 x float>, <4 x float> } @llvm.sincospi.v4f32(<4 x float>  %Val)
```

##### Overview:

The ‘`llvm.sincospi.*`’ intrinsics returns the sine and cosine of pi*operand.

##### Arguments:

The argument is a floating-point value or vector of floating-point values. Returns two values matching the argument type in a struct.

##### Semantics:

This is equivalent to the `llvm.sincos.*` intrinsic where the argument has been multiplied by pi, however, it computes the result more accurately especially for large input values.

Note

Currently, the default lowering of this intrinsic relies on the `sincospi[f|l]` functions being available in the target’s runtime (e.g., libc).

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.modf` on any floating-point or vector of floating-point type. However, not all targets support all types.

```
declare { float, float }             @llvm.modf.f32(float  %Val)
declare { double, double }           @llvm.modf.f64(double %Val)
declare { x86_fp80, x86_fp80 }       @llvm.modf.f80(x86_fp80  %Val)
declare { fp128, fp128 }             @llvm.modf.f128(fp128 %Val)
declare { ppc_fp128, ppc_fp128 }     @llvm.modf.ppcf128(ppc_fp128  %Val)
declare { <4 x float>, <4 x float> } @llvm.modf.v4f32(<4 x float>  %Val)
```

##### Overview:

The ‘`llvm.modf.*`’ intrinsics return the operand’s integral and fractional parts.

##### Arguments:

The argument is a floating-point value or vector of floating-point values. Returns two values matching the argument type in a struct.

##### Semantics:

Return the same values as a corresponding libm ‘`modf`’ function without trapping or setting `errno`.

The first result is the fractional part of the operand and the second result is the integral part of the operand. Both results have the same sign as the operand.

Not including exceptional inputs (listed below), `llvm.modf.*` is semantically equivalent to:

```
%fp = frem <fptype> %x, 1.0  ; Fractional part
%ip = fsub <fptype> %x, %fp  ; Integral part
```

(assuming no floating-point precision errors)

If the argument is a zero, returns a zero with the same sign for both the fractional and integral parts.

If the argument is an infinity, returns a fractional part of zero with the same sign, and infinity with the same sign as the integral part.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.pow` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.pow.f32(float  %Val, float %Power)
declare double    @llvm.pow.f64(double %Val, double %Power)
declare x86_fp80  @llvm.pow.f80(x86_fp80  %Val, x86_fp80 %Power)
declare fp128     @llvm.pow.f128(fp128 %Val, fp128 %Power)
declare ppc_fp128 @llvm.pow.ppcf128(ppc_fp128  %Val, ppc_fp128 Power)
```

##### Overview:

The ‘`llvm.pow.*`’ intrinsics return the first operand raised to the specified (positive or negative) power.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`pow`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

Note that the *pow* function is unusual in that NaN inputs can lead to non-NaN results, and this depends on the kind of NaN (quiet vs signaling). Due to how LLVM treats NaN values in non-constrained functions, the function may non-deterministically treat signaling NaNs as quiet NaNs. For example, *pow(QNaN, 0.0)* returns *1.0*, and *pow(SNaN, 0.0)* may non-deterministically return *1.0* or a NaN.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.exp` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.exp.f32(float  %Val)
declare double    @llvm.exp.f64(double %Val)
declare x86_fp80  @llvm.exp.f80(x86_fp80  %Val)
declare fp128     @llvm.exp.f128(fp128 %Val)
declare ppc_fp128 @llvm.exp.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.exp.*`’ intrinsics compute the base-e exponential of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`exp`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.exp2` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.exp2.f32(float  %Val)
declare double    @llvm.exp2.f64(double %Val)
declare x86_fp80  @llvm.exp2.f80(x86_fp80  %Val)
declare fp128     @llvm.exp2.f128(fp128 %Val)
declare ppc_fp128 @llvm.exp2.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.exp2.*`’ intrinsics compute the base-2 exponential of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`exp2`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.exp10` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.exp10.f32(float  %Val)
declare double    @llvm.exp10.f64(double %Val)
declare x86_fp80  @llvm.exp10.f80(x86_fp80  %Val)
declare fp128     @llvm.exp10.f128(fp128 %Val)
declare ppc_fp128 @llvm.exp10.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.exp10.*`’ intrinsics compute the base-10 exponential of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`exp10`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.ldexp` on any floating point or vector of floating point type. Not all targets support all types however.

```
declare float     @llvm.ldexp.f32.i32(float %Val, i32 %Exp)
declare double    @llvm.ldexp.f64.i32(double %Val, i32 %Exp)
declare x86_fp80  @llvm.ldexp.f80.i32(x86_fp80 %Val, i32 %Exp)
declare fp128     @llvm.ldexp.f128.i32(fp128 %Val, i32 %Exp)
declare ppc_fp128 @llvm.ldexp.ppcf128.i32(ppc_fp128 %Val, i32 %Exp)
declare <2 x float> @llvm.ldexp.v2f32.v2i32(<2 x float> %Val, <2 x i32> %Exp)
```

##### Overview:

The ‘`llvm.ldexp.*`’ intrinsics perform the ldexp function.

##### Arguments:

The first argument and the return value are floating-point or vector of floating-point values of the same type. The second argument is an integer with the same number of elements.

##### Semantics:

This function multiplies the first argument by 2 raised to the second argument’s power. If the first argument is NaN or infinite, the same value is returned. If the result underflows a zero with the same sign is returned. If the result overflows, the result is an infinity with the same sign.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.frexp` on any floating point or vector of floating point type. Not all targets support all types however.

```
declare { float, i32 }     @llvm.frexp.f32.i32(float %Val)
declare { double, i32 }    @llvm.frexp.f64.i32(double %Val)
declare { x86_fp80, i32 }  @llvm.frexp.f80.i32(x86_fp80 %Val)
declare { fp128, i32 }     @llvm.frexp.f128.i32(fp128 %Val)
declare { ppc_fp128, i32 } @llvm.frexp.ppcf128.i32(ppc_fp128 %Val)
declare { <2 x float>, <2 x i32> }  @llvm.frexp.v2f32.v2i32(<2 x float> %Val)
```

##### Overview:

The ‘`llvm.frexp.*`’ intrinsics perform the frexp function.

##### Arguments:

The argument is a floating-point or vector of floating-point values. Returns two values in a struct. The first struct field matches the argument type, and the second field is an integer or a vector of integer values with the same number of elements as the argument.

##### Semantics:

This intrinsic splits a floating point value into a normalized fractional component and integral exponent.

For a non-zero argument, returns the argument multiplied by some power of two such that the absolute value of the returned value is in the range [0.5, 1.0), with the same sign as the argument. The second result is an integer such that the first result raised to the power of the second result is the input argument.

If the argument is a zero, returns a zero with the same sign and a 0 exponent.

If the argument is a NaN, a NaN is returned and the returned exponent is unspecified.

If the argument is an infinity, returns an infinity with the same sign and an unspecified exponent.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.log` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.log.f32(float  %Val)
declare double    @llvm.log.f64(double %Val)
declare x86_fp80  @llvm.log.f80(x86_fp80  %Val)
declare fp128     @llvm.log.f128(fp128 %Val)
declare ppc_fp128 @llvm.log.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.log.*`’ intrinsics compute the base-e logarithm of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`log`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.log10` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.log10.f32(float  %Val)
declare double    @llvm.log10.f64(double %Val)
declare x86_fp80  @llvm.log10.f80(x86_fp80  %Val)
declare fp128     @llvm.log10.f128(fp128 %Val)
declare ppc_fp128 @llvm.log10.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.log10.*`’ intrinsics compute the base-10 logarithm of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`log10`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.log2` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.log2.f32(float  %Val)
declare double    @llvm.log2.f64(double %Val)
declare x86_fp80  @llvm.log2.f80(x86_fp80  %Val)
declare fp128     @llvm.log2.f128(fp128 %Val)
declare ppc_fp128 @llvm.log2.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.log2.*`’ intrinsics compute the base-2 logarithm of the specified value.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as a corresponding libm ‘`log2`’ function but without trapping or setting `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fma` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.fma.f32(float  %a, float  %b, float  %c)
declare double    @llvm.fma.f64(double %a, double %b, double %c)
declare x86_fp80  @llvm.fma.f80(x86_fp80 %a, x86_fp80 %b, x86_fp80 %c)
declare fp128     @llvm.fma.f128(fp128 %a, fp128 %b, fp128 %c)
declare ppc_fp128 @llvm.fma.ppcf128(ppc_fp128 %a, ppc_fp128 %b, ppc_fp128 %c)
```

##### Overview:

The ‘`llvm.fma.*`’ intrinsics perform the fused multiply-add operation.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

Return the same value as the IEEE 754 fusedMultiplyAdd operation. This is assumed to not trap or set `errno`.

When specified with the fast-math-flag ‘afn’, the result may be approximated using a less accurate calculation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fabs` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.fabs.f32(float  %Val)
declare double    @llvm.fabs.f64(double %Val)
declare x86_fp80  @llvm.fabs.f80(x86_fp80 %Val)
declare fp128     @llvm.fabs.f128(fp128 %Val)
declare ppc_fp128 @llvm.fabs.ppcf128(ppc_fp128 %Val)
```

##### Overview:

The ‘`llvm.fabs.*`’ intrinsics return the absolute value of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `fabs` functions would, and handles error conditions in the same way. The returned value is completely identical to the input except for the sign bit; in particular, if the input is a NaN, then the quiet/signaling bit and payload are perfectly preserved.

LLVM supports three pairs of floating-point min/max intrinsics, which differ in their handling of NaN values:

> - `llvm.minimum` and `llvm.maximum`: Return NaN if one the arguments is NaN.
> - `llvm.minimumnum` and `llvm.maximumnum`: Return the other argument if one of the arguments is NaN.
> - `llvm.minnum` and `llvm.maxnum`: For quiet NaNs behaves like minimumnum/maximumnum. For signaling NaNs, non-deterministically returns NaN or the other operand.

Additionally, each of these intrinsics supports two behaviors for signed zeros. By default, -0.0 is considered smaller than +0.0. If the `nsz` flag is specified, the order is non-deterministic: If the two inputs are zeros with opposite sign, either input may be returned.

The mapping between the LLVM intrinsics, C functions and IEEE 754 functions is as follows (up to divergences permitted by the usual *NaN rules <floatnan>*):

| LLVM intrinsic | llvm.minnum with nsz flag | llvm.minimum | llvm.minimumnum |
|---|---|---|---|
| C function | fmin | fminimum | fminimum_num |
| IEEE 754 function | minNum (2008) | minimum (2019) | minimumNumber (2019) |

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.minnum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.minnum.f32(float %Val0, float %Val1)
declare double    @llvm.minnum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.minnum.f80(x86_fp80 %Val0, x86_fp80 %Val1)
declare fp128     @llvm.minnum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.minnum.ppcf128(ppc_fp128 %Val0, ppc_fp128 %Val1)
```

##### Overview:

The ‘`llvm.minnum.*`’ intrinsics return the minimum of the two arguments.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If both operands are qNaNs, returns a NaN. If one operand is qNaN and another operand is a number, returns the number. If both operands are numbers, returns the lesser of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

If an operand is a signaling NaN, then the intrinsic will non-deterministically either:

> - Return a NaN.
> - Or treat the signaling NaN as a quiet NaN.

If the `nsz` flag is specified, `llvm.minnum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

When used with the `nsz` flag, this intrinsic follows the semantics of `fmin` in C and `minNum` in IEEE 754-2008, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

The `llvm.minnum` intrinsic can be refined into `llvm.minimumnum`, as the latter exhibits a subset of behaviors of the former.

Warning

If the intrinsic is used without nsz, not all backends currently respect the specified signed zero ordering. Do not rely on it until this warning has been removed. See issue #174730.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.maxnum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.maxnum.f32(float  %Val0, float  %Val1)
declare double    @llvm.maxnum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.maxnum.f80(x86_fp80  %Val0, x86_fp80  %Val1)
declare fp128     @llvm.maxnum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.maxnum.ppcf128(ppc_fp128  %Val0, ppc_fp128  %Val1)
```

##### Overview:

The ‘`llvm.maxnum.*`’ intrinsics return the maximum of the two arguments.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If both operands are qNaNs, returns a NaN. If one operand is qNaN and another operand is a number, returns the number. If both operands are numbers, returns the greater of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

If an operand is a signaling NaN, then the intrinsic will non-deterministically either:

> - Return a NaN.
> - Or treat the signaling NaN as a quiet NaN.

If the `nsz` flag is specified, `llvm.maxnum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

When used with the `nsz` flag, this intrinsic follows the semantics of `fmax` in C and `maxNum` in IEEE 754-2008, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

The `llvm.maxnum` intrinsic can be refined into `llvm.maximumnum`, as the latter exhibits a subset of behaviors of the former.

Warning

If the intrinsic is used without nsz, not all backends currently respect the specified signed zero ordering. Do not rely on it until this warning has been removed. See issue #174730.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.minimum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.minimum.f32(float %Val0, float %Val1)
declare double    @llvm.minimum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.minimum.f80(x86_fp80 %Val0, x86_fp80 %Val1)
declare fp128     @llvm.minimum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.minimum.ppcf128(ppc_fp128 %Val0, ppc_fp128 %Val1)
```

##### Overview:

The ‘`llvm.minimum.*`’ intrinsics return the minimum of the two arguments, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If either operand is a NaN, returns a NaN. Otherwise returns the lesser of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

This intrinsic follows the semantics of `fminimum` in C23 and `minimum` in IEEE 754-2019, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

If the `nsz` flag is specified, `llvm.maximum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.maximum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.maximum.f32(float %Val0, float %Val1)
declare double    @llvm.maximum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.maximum.f80(x86_fp80 %Val0, x86_fp80 %Val1)
declare fp128     @llvm.maximum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.maximum.ppcf128(ppc_fp128 %Val0, ppc_fp128 %Val1)
```

##### Overview:

The ‘`llvm.maximum.*`’ intrinsics return the maximum of the two arguments, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If either operand is a NaN, returns a NaN. Otherwise returns the greater of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

This intrinsic follows the semantics of `fmaximum` in C23 and `maximum` in IEEE 754-2019, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

If the `nsz` flag is specified, `llvm.maximum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.minimumnum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.minimumnum.f32(float %Val0, float %Val1)
declare double    @llvm.minimumnum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.minimumnum.f80(x86_fp80 %Val0, x86_fp80 %Val1)
declare fp128     @llvm.minimumnum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.minimumnum.ppcf128(ppc_fp128 %Val0, ppc_fp128 %Val1)
```

##### Overview:

The ‘`llvm.minimumnum.*`’ intrinsics return the minimum of the two arguments, not propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If both operands are NaNs (including sNaN), returns a NaN. If one operand is NaN (including sNaN) and another operand is a number, return the number. Otherwise returns the lesser of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

If the `nsz` flag is specified, `llvm.minimumnum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

This intrinsic follows the semantics of `fminimum_num` in C23 and `minimumNumber` in IEEE 754-2019, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

This intrinsic behaves the same as `llvm.minnum` other than its treatment of sNaN inputs.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.maximumnum` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.maximumnum.f32(float %Val0, float %Val1)
declare double    @llvm.maximumnum.f64(double %Val0, double %Val1)
declare x86_fp80  @llvm.maximumnum.f80(x86_fp80 %Val0, x86_fp80 %Val1)
declare fp128     @llvm.maximumnum.f128(fp128 %Val0, fp128 %Val1)
declare ppc_fp128 @llvm.maximumnum.ppcf128(ppc_fp128 %Val0, ppc_fp128 %Val1)
```

##### Overview:

The ‘`llvm.maximumnum.*`’ intrinsics return the maximum of the two arguments, not propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

If both operands are NaNs (including sNaN), returns a NaN. If one operand is NaN (including sNaN) and another operand is a number, return the number. Otherwise returns the greater of the two arguments. -0.0 is considered to be less than +0.0 for this intrinsic.

If the `nsz` flag is specified, `llvm.maximumnum` with one +0.0 and one -0.0 operand may non-deterministically return either operand. Contrary to normal `nsz` semantics, if both operands have the same sign, the result must also have the same sign.

This intrinsic follows the semantics of `fmaximum_num` in C23 and `maximumNumber` in IEEE 754-2019, except for signaling NaN inputs, which follow LLVM’s usual signaling NaN behavior instead.

This intrinsic behaves the same as `llvm.maxnum` other than its treatment of sNaN inputs.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.copysign` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.copysign.f32(float  %Mag, float  %Sgn)
declare double    @llvm.copysign.f64(double %Mag, double %Sgn)
declare x86_fp80  @llvm.copysign.f80(x86_fp80  %Mag, x86_fp80  %Sgn)
declare fp128     @llvm.copysign.f128(fp128 %Mag, fp128 %Sgn)
declare ppc_fp128 @llvm.copysign.ppcf128(ppc_fp128  %Mag, ppc_fp128  %Sgn)
```

##### Overview:

The ‘`llvm.copysign.*`’ intrinsics return a value with the magnitude of the first operand and the sign of the second operand.

##### Arguments:

The arguments and return value are floating-point numbers of the same type.

##### Semantics:

This function returns the same values as the libm `copysign` functions would, and handles error conditions in the same way. The returned value is completely identical to the first operand except for the sign bit; in particular, if the input is a NaN, then the quiet/signaling bit and payload are perfectly preserved.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.floor` on any floating-point or vector of floating-point type. Not all targets support all types however.

```
declare float     @llvm.floor.f32(float  %Val)
declare double    @llvm.floor.f64(double %Val)
declare x86_fp80  @llvm.floor.f80(x86_fp80  %Val)
declare fp128     @llvm.floor.f128(fp128 %Val)
declare ppc_fp128 @llvm.floor.ppcf128(ppc_fp128  %Val)
```

##### Overview:

The ‘`llvm.floor.*`’ intrinsics return the floor of the operand.

##### Arguments:

The argument and return value are floating-point numbers of the same type.

##### Semantics:
