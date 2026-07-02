---
title: "LLVM Language Reference Manual (part 16/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 16/20
---

# LLVM Language Reference Manual

The ‘`llvm.vp.reduce.and`’ intrinsic performs the integer `AND` reduction (llvm.vector.reduce.and) of the vector argument `val` on each enabled lane, performing an ‘`and`’ of that with with the scalar `start_value`. Disabled lanes are treated as containing the neutral value `UINT_MAX`, or `-1` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.and.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 -1, i32 -1, i32 -1, i32 -1>
%reduction = call i32 @llvm.vector.reduce.and.v4i32(<4 x i32> %masked.a)
%also.r = and i32 %reduction, %start
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.or.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.or.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer `OR` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.or`’ intrinsic performs the integer `OR` reduction (llvm.vector.reduce.or) of the vector argument `val` on each enabled lane, performing an ‘`or`’ of that with the scalar `start_value`. Disabled lanes are treated as containing the neutral value `0` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.or.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 0, i32 0, i32 0, i32 0>
%reduction = call i32 @llvm.vector.reduce.or.v4i32(<4 x i32> %masked.a)
%also.r = or i32 %reduction, %start
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.xor.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.xor.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer `XOR` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.xor`’ intrinsic performs the integer `XOR` reduction (llvm.vector.reduce.xor) of the vector argument `val` on each enabled lane, performing an ‘`xor`’ of that with the scalar `start_value`. Disabled lanes are treated as containing the neutral value `0` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.xor.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 0, i32 0, i32 0, i32 0>
%reduction = call i32 @llvm.vector.reduce.xor.v4i32(<4 x i32> %masked.a)
%also.r = xor i32 %reduction, %start
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.smax.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.smax.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated signed-integer `MAX` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.smax`’ intrinsic performs the signed-integer `MAX` reduction (llvm.vector.reduce.smax) of the vector argument `val` on each enabled lane, and taking the maximum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value `INT_MIN` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i8 @llvm.vp.reduce.smax.v4i8(i8 %start, <4 x i8> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i8> %a, <4 x i8> <i8 -128, i8 -128, i8 -128, i8 -128>
%reduction = call i8 @llvm.vector.reduce.smax.v4i8(<4 x i8> %masked.a)
%also.r = call i8 @llvm.smax.i8(i8 %reduction, i8 %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.smin.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.smin.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated signed-integer `MIN` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.smin`’ intrinsic performs the signed-integer `MIN` reduction (llvm.vector.reduce.smin) of the vector argument `val` on each enabled lane, and taking the minimum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value `INT_MAX` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i8 @llvm.vp.reduce.smin.v4i8(i8 %start, <4 x i8> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i8> %a, <4 x i8> <i8 127, i8 127, i8 127, i8 127>
%reduction = call i8 @llvm.vector.reduce.smin.v4i8(<4 x i8> %masked.a)
%also.r = call i8 @llvm.smin.i8(i8 %reduction, i8 %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.umax.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.umax.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated unsigned-integer `MAX` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.umax`’ intrinsic performs the unsigned-integer `MAX` reduction (llvm.vector.reduce.umax) of the vector argument `val` on each enabled lane, and taking the maximum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value `0` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.umax.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 0, i32 0, i32 0, i32 0>
%reduction = call i32 @llvm.vector.reduce.umax.v4i32(<4 x i32> %masked.a)
%also.r = call i32 @llvm.umax.i32(i32 %reduction, i32 %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.umin.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.umin.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated unsigned-integer `MIN` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.umin`’ intrinsic performs the unsigned-integer `MIN` reduction (llvm.vector.reduce.umin) of the vector argument `val` on each enabled lane, taking the minimum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value `UINT_MAX`, or `-1` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.umin.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 -1, i32 -1, i32 -1, i32 -1>
%reduction = call i32 @llvm.vector.reduce.umin.v4i32(<4 x i32> %masked.a)
%also.r = call i32 @llvm.umin.i32(i32 %reduction, i32 %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fmax.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fmax.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `MAX` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fmax`’ intrinsic performs the floating-point `MAX` reduction (llvm.vector.reduce.fmax) of the vector argument `val` on each enabled lane, taking the maximum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

The neutral value is dependent on the fast-math flags. If no flags are set, the neutral value is `-QNAN`. If `nnan` and `ninf` are both set, then the neutral value is the smallest floating-point value for the result type. If only `nnan` is set then the neutral value is `-Infinity`.

This instruction has the same comparison semantics as the llvm.vector.reduce.fmax intrinsic (and thus the ‘`llvm.maxnum.*`’ intrinsic).

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fmax.v4f32(float %float, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float QNAN, float QNAN, float QNAN, float QNAN>
%reduction = call float @llvm.vector.reduce.fmax.v4f32(<4 x float> %masked.a)
%also.r = call float @llvm.maxnum.f32(float %reduction, float %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fmin.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fmin.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `MIN` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fmin`’ intrinsic performs the floating-point `MIN` reduction (llvm.vector.reduce.fmin) of the vector argument `val` on each enabled lane, taking the minimum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

The neutral value is dependent on the fast-math flags. If no flags are set, the neutral value is `+QNAN`. If `nnan` and `ninf` are both set, then the neutral value is the largest floating-point value for the result type. If only `nnan` is set then the neutral value is `+Infinity`.

This instruction has the same comparison semantics as the llvm.vector.reduce.fmin intrinsic (and thus the ‘`llvm.minnum.*`’ intrinsic).

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fmin.v4f32(float %start, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float QNAN, float QNAN, float QNAN, float QNAN>
%reduction = call float @llvm.vector.reduce.fmin.v4f32(<4 x float> %masked.a)
%also.r = call float @llvm.minnum.f32(float %reduction, float %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fmaximum.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fmaximum.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `MAX` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fmaximum`’ intrinsic performs the floating-point `MAX` reduction (llvm.vector.reduce.fmaximum) of the vector argument `val` on each enabled lane, taking the maximum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

The neutral value is dependent on the fast-math flags. If no flags are set or only the `nnan` is set, the neutral value is `-Infinity`. If `ninf` is set, then the neutral value is the smallest floating-point value for the result type.

This instruction has the same comparison semantics as the llvm.vector.reduce.fmaximum intrinsic (and thus the ‘`llvm.maximum.*`’ intrinsic). That is, the result will always be a number unless any of the elements in the vector or the starting value is `NaN`. Namely, this intrinsic propagates `NaN`. Also, -0.0 is considered less than +0.0.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fmaximum.v4f32(float %float, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float -infinity, float -infinity, float -infinity, float -infinity>
%reduction = call float @llvm.vector.reduce.fmaximum.v4f32(<4 x float> %masked.a)
%also.r = call float @llvm.maximum.f32(float %reduction, float %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fminimum.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fminimum.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `MIN` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fminimum`’ intrinsic performs the floating-point `MIN` reduction (llvm.vector.reduce.fminimum) of the vector argument `val` on each enabled lane, taking the minimum of that and the scalar `start_value`. Disabled lanes are treated as containing the neutral value (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

The neutral value is dependent on the fast-math flags. If no flags are set or only the `nnan` is set, the neutral value is `+Infinity`. If `ninf` is set, then the neutral value is the largest floating-point value for the result type.

This instruction has the same comparison semantics as the llvm.vector.reduce.fminimum intrinsic (and thus the ‘`llvm.minimum.*`’ intrinsic). That is, the result will always be a number unless any of the elements in the vector or the starting value is `NaN`. Namely, this intrinsic propagates `NaN`. Also, -0.0 is considered less than +0.0.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fminimum.v4f32(float %start, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float infinity, float infinity, float infinity, float infinity>
%reduction = call float @llvm.vector.reduce.fminimum.v4f32(<4 x float> %masked.a)
%also.r = call float @llvm.minimum.f32(float %reduction, float %start)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <2 x double> @llvm.experimental.vp.splice.v2f64(<2 x double> %vec1, <2 x double> %vec2, i32 %imm, <2 x i1> %mask, i32 %evl1, i32 %evl2)
declare <vscale x 4 x i32> @llvm.experimental.vp.splice.nxv4i32(<vscale x 4 x i32> %vec1, <vscale x 4 x i32> %vec2, i32 %imm, <vscale x 4 x i1> %mask, i32 %evl1, i32 %evl2)
```

##### Overview:

The ‘`llvm.experimental.vp.splice.*`’ intrinsic is the vector length predicated version of the ‘`llvm.vector.splice.*`’ intrinsic.

##### Arguments:

The result and the first two arguments `vec1` and `vec2` are vectors with the same type. The third argument `imm` is an immediate signed integer that indicates the offset index. The fourth argument `mask` is a vector mask and has the same number of elements as the result. The last two arguments `evl1` and `evl2` are unsigned integers indicating the explicit vector lengths of `vec1` and `vec2` respectively. `imm`, `evl1` and `evl2` should respect the following constraints: `-evl1 <= imm < evl1`, `0 <= evl1 <= VL` and `0 <= evl2 <= VL`, where `VL` is the runtime vector factor. If these constraints are not satisfied the intrinsic has undefined behavior.

##### Semantics:

Effectively, this intrinsic concatenates `vec1[0..evl1-1]` and `vec2[0..evl2-1]` and creates the result vector by selecting the elements in a window of size `evl2`, starting at index `imm` (for a positive immediate) of the concatenated vector. Elements in the result vector beyond `evl2` are `undef`. If `imm` is negative the starting index is `evl1 + imm`. The result vector of active vector length `evl2` contains `evl1 - imm` (`-imm` for negative `imm`) elements from indices `[imm..evl1 - 1]` (`[evl1 + imm..evl1 -1]` for negative `imm`) of `vec1` followed by the first `evl2 - (evl1 - imm)` (`evl2 + imm` for negative `imm`) elements of `vec2`. If `evl1 - imm` (`-imm`) >= `evl2`, only the first `evl2` elements are considered and the remaining are `undef`. The lanes in the result vector disabled by `mask` are `poison`.

##### Examples:

```
llvm.experimental.vp.splice(<A,B,C,D>, <E,F,G,H>, 1, 2, 3);  ==> <B, E, F, poison> index
llvm.experimental.vp.splice(<A,B,C,D>, <E,F,G,H>, -2, 3, 2); ==> <B, C, poison, poison> trailing elements
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <2 x double> @llvm.experimental.vp.reverse.v2f64(<2 x double> %vec, <2 x i1> %mask, i32 %evl)
declare <vscale x 4 x i32> @llvm.experimental.vp.reverse.nxv4i32(<vscale x 4 x i32> %vec, <vscale x 4 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.experimental.vp.reverse.*`’ intrinsic is the vector length predicated version of the ‘`llvm.vector.reverse.*`’ intrinsic.

##### Arguments:

The result and the first argument `vec` are vectors with the same type. The second argument `mask` is a vector mask and has the same number of elements as the result. The third argument is the explicit vector length of the operation.

##### Semantics:

This intrinsic reverses the order of the first `evl` elements in a vector. The lanes in the result vector disabled by `mask` are `poison`. The elements past `evl` are poison.

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x float> @llvm.vp.load.v4f32.p0(ptr %ptr, <4 x i1> %mask, i32 %evl)
declare <vscale x 2 x i16> @llvm.vp.load.nxv2i16.p0(ptr %ptr, <vscale x 2 x i1> %mask, i32 %evl)
declare <8 x float> @llvm.vp.load.v8f32.p1(ptr addrspace(1) %ptr, <8 x i1> %mask, i32 %evl)
declare <vscale x 1 x i64> @llvm.vp.load.nxv1i64.p6(ptr addrspace(6) %ptr, <vscale x 1 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.vp.load.*`’ intrinsic is the vector length predicated version of the llvm.masked.load intrinsic.

##### Arguments:

The first argument is the base pointer for the load. The second argument is a vector of boolean values with the same number of elements as the return type. The third is the explicit vector length of the operation. The return type and underlying type of the base pointer are the same vector types.

The align parameter attribute can be provided for the first argument.

##### Semantics:

The ‘`llvm.vp.load`’ intrinsic reads a vector from memory in the same way as the ‘`llvm.masked.load`’ intrinsic, where the mask is taken from the combination of the ‘`mask`’ and ‘`evl`’ arguments in the usual VP way. Certain ‘`llvm.masked.load`’ arguments do not have corresponding arguments in ‘`llvm.vp.load`’: the ‘`passthru`’ argument is implicitly `poison`; the ‘`alignment`’ argument is taken as the `align` parameter attribute, if provided. The default alignment is taken as the ABI alignment of the return type as specified by the datalayout string.

##### Examples:

```
%r = call <8 x i8> @llvm.vp.load.v8i8.p0(ptr align 2 %ptr, <8 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%also.r = call <8 x i8> @llvm.masked.load.v8i8.p0(ptr align 2 %ptr, <8 x i1> %mask, <8 x i8> poison)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare {<4 x float>, i32} @llvm.vp.load.ff.v4f32.p0(ptr %ptr, <4 x i1> %mask, i32 %evl)
declare {<vscale x 2 x i16>, i32} @llvm.vp.load.ff.nxv2i16.p0(ptr %ptr, <vscale x 2 x i1> %mask, i32 %evl)
declare {<8 x float>, i32} @llvm.vp.load.ff.v8f32.p1(ptr addrspace(1) %ptr, <8 x i1> %mask, i32 %evl)
declare {<vscale x 1 x i64>, i32} @llvm.vp.load.ff.nxv1i64.p6(ptr addrspace(6) %ptr, <vscale x 1 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.vp.load.ff.*`’ intrinsic is similar to ‘`llvm.vp.load.*`’, but will not trap if there are not `evl` readable lanes at the pointer. ‘`ff`’ stands for first-fault or fault-only-first.

##### Arguments:

The first argument is the base pointer for the load. The second argument is a vector of boolean values with the same number of elements as the first return type. The third is the explicit vector length of the operation. The first return type and underlying type of the base pointer are the same vector types.

The align parameter attribute can be provided for the first argument.

##### Semantics:

The ‘`llvm.vp.load.ff`’ is designed for reading vector lanes in a single IR operation where the number of lanes that can be read is not known and can only be determined by looking at the data. This is useful for vectorizing strcmp or strlen like loops where the data contains a null terminator. Some targets have a fault-only-first load instruction that this intrinsic can be lowered to. Other targets may support this intrinsic differently, for example by lowering to a single scalar load guarded by `evl!=0` and `mask[0]==1` and indicating only 1 lane could be read.

Like ‘`llvm.vp.load`’, this intrinsic reads memory based on a `mask` and an `evl`. If `evl` is non-zero and the first lane is masked-on, then the first lane of the vector needs to be inbounds of an allocation. The remaining masked-on lanes with index less than `evl` do not need to be inbounds of an the same allocation or any allocation.

The second return value from the intrinsic indicates the index of the first lane that could not be read for some reason or `evl` if all lanes could be be read. Lanes at this index or higher in the first return value are poison value. If `evl` is non-zero, the result in the second return value must be at least 1, even if the first lane is masked-off.

The second result is usually less than `evl` when an exception would occur for reading that lane, but it can be reduced for any reason. This facilitates emulating this intrinsic when the hardware only supports narrower vector types natively or when when hardware does not support fault-only-first loads.

Masked-on lanes that are not inbounds of the allocation that contains the first lane are poison value. There should be a marker in the allocation that indicates where valid data stops such as a null terminator. The terminator should be checked for after calling this intrinsic to prevent using any lanes past the terminator. Even if second return value is less than `evl`, the terminator value may not have been read.

This intrinsic will typically be called in a loop until a terminator is found. The second result should be used to indicates how many elements are valid to look for the null terminator. If the terminator is not found, the pointer should be advanced by the number of elements in the second result and the intrinsic called again.

The default alignment is taken as the ABI alignment of the first return type as specified by the datalayout string.

##### Examples:

```
%r = call {<8 x i8>, i32} @llvm.vp.load.ff.v8i8.p0(ptr align 2 %ptr, <8 x i1> %mask, i32 %evl)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare void @llvm.vp.store.v4f32.p0(<4 x float> %val, ptr %ptr, <4 x i1> %mask, i32 %evl)
declare void @llvm.vp.store.nxv2i16.p0(<vscale x 2 x i16> %val, ptr %ptr, <vscale x 2 x i1> %mask, i32 %evl)
declare void @llvm.vp.store.v8f32.p1(<8 x float> %val, ptr addrspace(1) %ptr, <8 x i1> %mask, i32 %evl)
declare void @llvm.vp.store.nxv1i64.p6(<vscale x 1 x i64> %val, ptr addrspace(6) %ptr, <vscale x 1 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.vp.store.*`’ intrinsic is the vector length predicated version of the llvm.masked.store intrinsic.

##### Arguments:

The first argument is the vector value to be written to memory. The second argument is the base pointer for the store. It has the same underlying type as the value argument. The third argument is a vector of boolean values with the same number of elements as the return type. The fourth is the explicit vector length of the operation.

The align parameter attribute can be provided for the second argument.

##### Semantics:

The ‘`llvm.vp.store`’ intrinsic reads a vector from memory in the same way as the ‘`llvm.masked.store`’ intrinsic, where the mask is taken from the combination of the ‘`mask`’ and ‘`evl`’ arguments in the usual VP way. The alignment of the operation (corresponding to the ‘`alignment`’ argument of ‘`llvm.masked.store`’) is specified by the `align` parameter attribute (see above). If it is not provided then the ABI alignment of the type of the ‘`value`’ argument as specified by the datalayout string is used instead.

##### Examples:

```
call void @llvm.vp.store.v8i8.p0(<8 x i8> %val, ptr align 4 %ptr, <8 x i1> %mask, i32 %evl)
;; For all lanes below %evl, the call above is lane-wise equivalent to the call below.

call void @llvm.masked.store.v8i8.p0(<8 x i8> %val, ptr %ptr, i32 4, <8 x i1> %mask)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x float> @llvm.experimental.vp.strided.load.v4f32.i64(ptr %ptr, i64 %stride, <4 x i1> %mask, i32 %evl)
declare <vscale x 2 x i16> @llvm.experimental.vp.strided.load.nxv2i16.i64(ptr %ptr, i64 %stride, <vscale x 2 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.experimental.vp.strided.load`’ intrinsic loads, into a vector, scalar values from memory locations evenly spaced apart by ‘`stride`’ number of bytes, starting from ‘`ptr`’.

##### Arguments:

The first argument is the base pointer for the load. The second argument is the stride value expressed in bytes. The third argument is a vector of boolean values with the same number of elements as the return type. The fourth is the explicit vector length of the operation. The base pointer underlying type matches the type of the scalar elements of the return argument.

The align parameter attribute can be provided for the first argument.

##### Semantics:

The ‘`llvm.experimental.vp.strided.load`’ intrinsic loads, into a vector, multiple scalar values from memory in the same way as the llvm.vp.gather intrinsic, where the vector of pointers is in the form:

> `%ptrs = <%ptr, %ptr + %stride, %ptr + 2 * %stride, ... >`,

with ‘`ptr`’ previously casted to a pointer ‘`i8`’, ‘`stride`’ always interpreted as a signed integer and all arithmetic occurring in the pointer type.

##### Examples:

```
%r = call <8 x i64> @llvm.experimental.vp.strided.load.v8i64.i64(i64* %ptr, i64 %stride, <8 x i64> %mask, i32 %evl)
;; The operation can also be expressed like this:

%addr = bitcast i64* %ptr to i8*
;; Create a vector of pointers %addrs in the form:
;; %addrs = <%addr, %addr + %stride, %addr + 2 * %stride, ...>
%ptrs = bitcast <8 x i8* > %addrs to <8 x i64* >
%also.r = call <8 x i64> @llvm.vp.gather.v8i64.v8p0i64(<8 x i64* > %ptrs, <8 x i64> %mask, i32 %evl)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare void @llvm.experimental.vp.strided.store.v4f32.i64(<4 x float> %val, ptr %ptr, i64 %stride, <4 x i1> %mask, i32 %evl)
declare void @llvm.experimental.vp.strided.store.nxv2i16.i64(<vscale x 2 x i16> %val, ptr %ptr, i64 %stride, <vscale x 2 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`@llvm.experimental.vp.strided.store`’ intrinsic stores the elements of ‘`val`’ into memory locations evenly spaced apart by ‘`stride`’ number of bytes, starting from ‘`ptr`’.

##### Arguments:

The first argument is the vector value to be written to memory. The second argument is the base pointer for the store. Its underlying type matches the scalar element type of the value argument. The third argument is the stride value expressed in bytes. The fourth argument is a vector of boolean values with the same number of elements as the return type. The fifth is the explicit vector length of the operation.

The align parameter attribute can be provided for the second argument.

##### Semantics:

The ‘`llvm.experimental.vp.strided.store`’ intrinsic stores the elements of ‘`val`’ in the same way as the llvm.vp.scatter intrinsic, where the vector of pointers is in the form:

> `%ptrs = <%ptr, %ptr + %stride, %ptr + 2 * %stride, ... >`,

with ‘`ptr`’ previously casted to a pointer ‘`i8`’, ‘`stride`’ always interpreted as a signed integer and all arithmetic occurring in the pointer type.

##### Examples:

```
call void @llvm.experimental.vp.strided.store.v8i64.i64(<8 x i64> %val, i64* %ptr, i64 %stride, <8 x i1> %mask, i32 %evl)
;; The operation can also be expressed like this:

%addr = bitcast i64* %ptr to i8*
;; Create a vector of pointers %addrs in the form:
;; %addrs = <%addr, %addr + %stride, %addr + 2 * %stride, ...>
%ptrs = bitcast <8 x i8* > %addrs to <8 x i64* >
call void @llvm.vp.scatter.v8i64.v8p0i64(<8 x i64> %val, <8 x i64*> %ptrs, <8 x i1> %mask, i32 %evl)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x double> @llvm.vp.gather.v4f64.v4p0(<4 x ptr> %ptrs, <4 x i1> %mask, i32 %evl)
declare <vscale x 2 x i8> @llvm.vp.gather.nxv2i8.nxv2p0(<vscale x 2 x ptr> %ptrs, <vscale x 2 x i1> %mask, i32 %evl)
declare <2 x float> @llvm.vp.gather.v2f32.v2p2(<2 x ptr addrspace(2)> %ptrs, <2 x i1> %mask, i32 %evl)
declare <vscale x 4 x i32> @llvm.vp.gather.nxv4i32.nxv4p4(<vscale x 4 x ptr addrspace(4)> %ptrs, <vscale x 4 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.vp.gather.*`’ intrinsic is the vector length predicated version of the llvm.masked.gather intrinsic.

##### Arguments:

The first argument is a vector of pointers which holds all memory addresses to read. The second argument is a vector of boolean values with the same number of elements as the return type. The third is the explicit vector length of the operation. The return type and underlying type of the vector of pointers are the same vector types.

The align parameter attribute can be provided for the first argument.

##### Semantics:

The ‘`llvm.vp.gather`’ intrinsic reads multiple scalar values from memory in the same way as the ‘`llvm.masked.gather`’ intrinsic, where the mask is taken from the combination of the ‘`mask`’ and ‘`evl`’ arguments in the usual VP way. Certain ‘`llvm.masked.gather`’ arguments do not have corresponding arguments in ‘`llvm.vp.gather`’: the ‘`passthru`’ argument is implicitly `poison`; the ‘`alignment`’ argument is taken as the `align` parameter, if provided. The default alignment is taken as the ABI alignment of the source addresses as specified by the datalayout string.

##### Examples:

```
%r = call <8 x i8> @llvm.vp.gather.v8i8.v8p0(<8 x ptr>  align 8 %ptrs, <8 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%also.r = call <8 x i8> @llvm.masked.gather.v8i8.v8p0(<8 x ptr> align 8 %ptrs, <8 x i1> %mask, <8 x i8> poison)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare void @llvm.vp.scatter.v4f64.v4p0(<4 x double> %val, <4 x ptr> %ptrs, <4 x i1> %mask, i32 %evl)
declare void @llvm.vp.scatter.nxv2i8.nxv2p0(<vscale x 2 x i8> %val, <vscale x 2 x ptr> %ptrs, <vscale x 2 x i1> %mask, i32 %evl)
declare void @llvm.vp.scatter.v2f32.v2p2(<2 x float> %val, <2 x ptr addrspace(2)> %ptrs, <2 x i1> %mask, i32 %evl)
declare void @llvm.vp.scatter.nxv4i32.nxv4p4(<vscale x 4 x i32> %val, <vscale x 4 x ptr addrspace(4)> %ptrs, <vscale x 4 x i1> %mask, i32 %evl)
```

##### Overview:

The ‘`llvm.vp.scatter.*`’ intrinsic is the vector length predicated version of the llvm.masked.scatter intrinsic.

##### Arguments:

The first argument is a vector value to be written to memory. The second argument is a vector of pointers, pointing to where the value elements should be stored. The third argument is a vector of boolean values with the same number of elements as the return type. The fourth is the explicit vector length of the operation.

The align parameter attribute can be provided for the second argument.

##### Semantics:

The ‘`llvm.vp.scatter`’ intrinsic writes multiple scalar values to memory in the same way as the ‘`llvm.masked.scatter`’ intrinsic, where the mask is taken from the combination of the ‘`mask`’ and ‘`evl`’ arguments in the usual VP way. The ‘`alignment`’ argument of the ‘`llvm.masked.scatter`’ does not have a corresponding argument in ‘`llvm.vp.scatter`’: it is instead provided via the optional `align` parameter attribute on the vector-of-pointers argument. Otherwise it is taken as the ABI alignment of the destination addresses as specified by the datalayout string.

##### Examples:

```
call void @llvm.vp.scatter.v8i8.v8p0(<8 x i8> %val, <8 x ptr> align 1 %ptrs, <8 x i1> %mask, i32 %evl)
;; For all lanes below %evl, the call above is lane-wise equivalent to the call below.

call void @llvm.masked.scatter.v8i8.v8p0(<8 x i8> %val, <8 x ptr> align 1 %ptrs, <8 x i1> %mask)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i16>  @llvm.vp.trunc.v16i16.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i16>  @llvm.vp.trunc.nxv4i16.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.trunc`’ intrinsic truncates its first argument to the return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.trunc`’ intrinsic takes a value to cast as its first argument. The return type is the type to cast the value to. Both types must be vector of integer type. The bit size of the value must be larger than the bit size of the return type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.trunc`’ intrinsic truncates the high order bits in value and converts the remaining bits to return type. Since the source size must be larger than the destination size, ‘`llvm.vp.trunc`’ cannot be a *no-op cast*. It will always truncate bits. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i16> @llvm.vp.trunc.v4i16.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = trunc <4 x i32> %a to <4 x i16>
%also.r = select <4 x i1> %mask, <4 x i16> %t, <4 x i16> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.zext.v16i32.v16i16 (<16 x i16> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.zext.nxv4i32.nxv4i16 (<vscale x 4 x i16> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.zext`’ intrinsic zero extends its first argument to the return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.zext`’ intrinsic takes a value to cast as its first argument. The return type is the type to cast the value to. Both types must be vectors of integer type. The bit size of the value must be smaller than the bit size of the return type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.zext`’ intrinsic fill the high order bits of the value with zero bits until it reaches the size of the return type. When zero extending from i1, the result will always be either 0 or 1. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.zext.v4i32.v4i16(<4 x i16> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = zext <4 x i16> %a to <4 x i32>
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.sext.v16i32.v16i16 (<16 x i16> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.sext.nxv4i32.nxv4i16 (<vscale x 4 x i16> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.sext`’ intrinsic sign extends its first argument to the return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.sext`’ intrinsic takes a value to cast as its first argument. The return type is the type to cast the value to. Both types must be vectors of integer type. The bit size of the value must be smaller than the bit size of the return type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sext`’ intrinsic performs a sign extension by copying the sign bit (highest order bit) of the value until it reaches the size of the return type. When sign extending from i1, the result will always be either -1 or 0. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.sext.v4i32.v4i16(<4 x i16> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = sext <4 x i16> %a to <4 x i32>
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fptrunc.v16f32.v16f64 (<16 x double> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.trunc.nxv4f32.nxv4f64 (<vscale x 4 x double> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.fptrunc`’ intrinsic truncates its first argument to the return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.fptrunc`’ intrinsic takes a value to cast as its first argument. The return type is the type to cast the value to. Both types must be vector of floating-point type. The bit size of the value must be larger than the bit size of the return type. This implies that ‘`llvm.vp.fptrunc`’ cannot be used to make a *no-op cast*. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fptrunc`’ intrinsic casts a `value` from a larger floating-point type to a smaller floating-point type. This instruction is assumed to execute in the default floating-point environment. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fptrunc.v4f32.v4f64(<4 x double> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fptrunc <4 x double> %a to <4 x float>
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x double>  @llvm.vp.fpext.v16f64.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x double>  @llvm.vp.fpext.nxv4f64.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.fpext`’ intrinsic extends its first argument to the return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:
