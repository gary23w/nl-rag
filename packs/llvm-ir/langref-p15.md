---
title: "LLVM Language Reference Manual (part 15/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 15/20
---

# LLVM Language Reference Manual

```
declare <16 x i32>  @llvm.vp.srem.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.srem.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.srem.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated computations of the signed remainder of two integer vectors.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.srem`’ intrinsic computes the remainder of the signed division (srem) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.srem.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = srem <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.urem.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.urem.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.urem.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated computation of the unsigned remainder of two integer vectors.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.urem`’ intrinsic computes the remainder of the unsigned division (urem) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.urem.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = urem <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.ashr.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.ashr.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.ashr.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated arithmetic right-shift.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.ashr`’ intrinsic computes the arithmetic right shift (ashr) of the first argument by the second argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.ashr.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = ashr <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.lshr.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.lshr.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.lshr.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated logical right-shift.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.lshr`’ intrinsic computes the logical right shift (lshr) of the first argument by the second argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.lshr.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = lshr <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.shl.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.shl.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.shl.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated left shift.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.shl`’ intrinsic computes the left shift (shl) of the first argument by the second argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.shl.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = shl <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.or.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.or.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.or.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated or.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.or`’ intrinsic performs a bitwise or (or) of the first two arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.or.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = or <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.and.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.and.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.and.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated and.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.and`’ intrinsic performs a bitwise and (and) of the first two arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.and.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = and <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.xor.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.xor.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.xor.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Vector-predicated, bitwise xor.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.xor`’ intrinsic performs a bitwise xor (xor) of the first two arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.xor.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = xor <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.abs.v16i32 (<16 x i32> <op>, i1 <is_int_min_poison>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.abs.nxv4i32 (<vscale x 4 x i32> <op>, i1 <is_int_min_poison>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.abs.v256i64 (<256 x i64> <op>, i1 <is_int_min_poison>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated abs of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument must be a constant and is a flag to indicate whether the result value of the ‘`llvm.vp.abs`’ intrinsic is a poison value if the first argument is statically or dynamically an `INT_MIN` value. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.abs`’ intrinsic performs abs (abs) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.abs.v4i32(<4 x i32> %a, i1 false, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.abs.v4i32(<4 x i32> %a, i1 false)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.smax.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.smax.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.smax.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer signed maximum of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.smax`’ intrinsic performs integer signed maximum (smax) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.smax.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.smax.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.smin.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.smin.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.smin.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer signed minimum of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.smin`’ intrinsic performs integer signed minimum (smin) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.smin.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.smin.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.umax.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.umax.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.umax.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer unsigned maximum of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.umax`’ intrinsic performs integer unsigned maximum (umax) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.umax.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.umax.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.umin.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.umin.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.umin.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer unsigned minimum of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.umin`’ intrinsic performs integer unsigned minimum (umin) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.umin.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.umin.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.copysign.v16f32 (<16 x float> <mag_op>, <16 x float> <sign_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.copysign.nxv4f32 (<vscale x 4 x float> <mag_op>, <vscale x 4 x float> <sign_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.copysign.v256f64 (<256 x double> <mag_op>, <256 x double> <sign_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point copysign of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.copysign`’ intrinsic performs floating-point copysign (copysign) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.copysign.v4f32(<4 x float> %mag, <4 x float> %sign, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.copysign.v4f32(<4 x float> %mag, <4 x float> %sign)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.minnum.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.minnum.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.minnum.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point IEEE 754-2008 minNum of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.minnum`’ intrinsic performs floating-point minimum (minnum) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.minnum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.minnum.v4f32(<4 x float> %a, <4 x float> %b)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.maxnum.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.maxnum.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.maxnum.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point IEEE 754-2008 maxNum of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.maxnum`’ intrinsic performs floating-point maximum (maxnum) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.maxnum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.maxnum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.minimum.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.minimum.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.minimum.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point minimum of two vectors of floating-point values, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.minimum`’ intrinsic performs floating-point minimum (minimum) of the first and second vector arguments on each enabled lane, the result being NaN if either argument is a NaN. -0.0 is considered to be less than +0.0 for this intrinsic. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.minimum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.minimum.v4f32(<4 x float> %a, <4 x float> %b)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.maximum.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.maximum.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.maximum.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point maximum of two vectors of floating-point values, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.maximum`’ intrinsic performs floating-point maximum (maximum) of the first and second vector arguments on each enabled lane, the result being NaN if either argument is a NaN. -0.0 is considered to be less than +0.0 for this intrinsic. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.maximum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.maximum.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fadd.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fadd.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fadd.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point addition of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fadd`’ intrinsic performs floating-point addition (fadd) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fadd.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fadd <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fsub.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fsub.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fsub.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point subtraction of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fsub`’ intrinsic performs floating-point subtraction (fsub) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fsub.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fsub <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fmul.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fmul.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fmul.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point multiplication of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fmul`’ intrinsic performs floating-point multiplication (fmul) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fmul.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fmul <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fdiv.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fdiv.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fdiv.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point division of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fdiv`’ intrinsic performs floating-point division (fdiv) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fdiv.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fdiv <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.frem.v16f32 (<16 x float> <left_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.frem.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.frem.v256f64 (<256 x double> <left_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point remainder of two vectors of floating-point values.

##### Arguments:

The first two arguments and the result have the same vector of floating-point type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.frem`’ intrinsic performs floating-point remainder (frem) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.frem.v4f32(<4 x float> %a, <4 x float> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = frem <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fneg.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fneg.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fneg.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point negation of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fneg`’ intrinsic performs floating-point negation (fneg) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fneg.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fneg <4 x float> %a
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fabs.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fabs.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fabs.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point absolute value of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fabs`’ intrinsic performs floating-point absolute value (fabs) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fabs.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.fabs.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.sqrt.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.sqrt.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.sqrt.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point square root of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sqrt`’ intrinsic performs floating-point square root (sqrt) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.sqrt.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.sqrt.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fma.v16f32 (<16 x float> <left_op>, <16 x float> <middle_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fma.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <middle_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fma.v256f64 (<256 x double> <left_op>, <256 x double> <middle_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point fused multiply-add of two vectors of floating-point values.

##### Arguments:

The first three arguments and the result have the same vector of floating-point type. The fourth argument is the vector mask and has the same number of elements as the result vector type. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fma`’ intrinsic performs floating-point fused multiply-add (llvm.fma) of the first, second, and third vector argument on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fma.v4f32(<4 x float> %a, <4 x float> %b, <4 x float> %c, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.fma(<4 x float> %a, <4 x float> %b, <4 x float> %c)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.fmuladd.v16f32 (<16 x float> <left_op>, <16 x float> <middle_op>, <16 x float> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.fmuladd.nxv4f32 (<vscale x 4 x float> <left_op>, <vscale x 4 x float> <middle_op>, <vscale x 4 x float> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.fmuladd.v256f64 (<256 x double> <left_op>, <256 x double> <middle_op>, <256 x double> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point multiply-add of two vectors of floating-point values that can be fused if code generator determines that (a) the target instruction set has support for a fused operation, and (b) that the fused operation is more efficient than the equivalent, separate pair of mul and add instructions.

##### Arguments:

The first three arguments and the result have the same vector of floating-point type. The fourth argument is the vector mask and has the same number of elements as the result vector type. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fmuladd`’ intrinsic performs floating-point multiply-add (llvm.fuladd) of the first, second, and third vector argument on each enabled lane. The result on disabled lanes is a poison value. The operation is performed in the default floating-point environment.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.fmuladd.v4f32(<4 x float> %a, <4 x float> %b, <4 x float> %c, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.fmuladd(<4 x float> %a, <4 x float> %b, <4 x float> %c)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.add.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.add.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer `ADD` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.add`’ intrinsic performs the integer `ADD` reduction (llvm.vector.reduce.add) of the vector argument `val` on each enabled lane, adding it to the scalar `start_value`. Disabled lanes are treated as containing the neutral value `0` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is equal to `start_value`.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.add.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> zeroinitializer
%reduction = call i32 @llvm.vector.reduce.add.v4i32(<4 x i32> %masked.a)
%also.r = add i32 %reduction, %start
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fadd.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fadd.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `ADD` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fadd`’ intrinsic performs the floating-point `ADD` reduction (llvm.vector.reduce.fadd) of the vector argument `val` on each enabled lane, adding it to the scalar `start_value`. Disabled lanes are treated as containing the neutral value `-0.0` (i.e., having no effect on the reduction operation). If no lanes are enabled, the resulting value will be equal to `start_value`.

To ignore the start value, the neutral value can be used.

See the unpredicated version (llvm.vector.reduce.fadd) for more detail on the semantics of the reduction.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fadd.v4f32(float %start, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float -0.0, float -0.0, float -0.0, float -0.0>
%also.r = call float @llvm.vector.reduce.fadd.v4f32(float %start, <4 x float> %masked.a)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.mul.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.mul.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer `MUL` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.mul`’ intrinsic performs the integer `MUL` reduction (llvm.vector.reduce.mul) of the vector argument `val` on each enabled lane, multiplying it by the scalar `start_value`. Disabled lanes are treated as containing the neutral value `1` (i.e., having no effect on the reduction operation). If the vector length is zero, the result is the start value.

To ignore the start value, the neutral value can be used.

##### Examples:

```llvm
%r = call i32 @llvm.vp.reduce.mul.v4i32(i32 %start, <4 x i32> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x i32> %a, <4 x i32> <i32 1, i32 1, i32 1, i32 1>
%reduction = call i32 @llvm.vector.reduce.mul.v4i32(<4 x i32> %masked.a)
%also.r = mul i32 %reduction, %start
```

##### Syntax:

This is an overloaded intrinsic.

```
declare float @llvm.vp.reduce.fmul.v4f32(float <start_value>, <4 x float> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare double @llvm.vp.reduce.fmul.nxv8f64(double <start_value>, <vscale x 8 x double> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point `MUL` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar floating-point type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of floating-point values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.reduce.fmul`’ intrinsic performs the floating-point `MUL` reduction (llvm.vector.reduce.fmul) of the vector argument `val` on each enabled lane, multiplying it by the scalar *start_value`*. Disabled lanes are treated as containing the neutral value `1.0` (i.e., having no effect on the reduction operation). If no lanes are enabled, the resulting value will be equal to the starting value.

To ignore the start value, the neutral value can be used.

See the unpredicated version (llvm.vector.reduce.fmul) for more detail on the semantics.

##### Examples:

```llvm
%r = call float @llvm.vp.reduce.fmul.v4f32(float %start, <4 x float> %a, <4 x i1> %mask, i32 %evl)
; %r is equivalent to %also.r, where lanes greater than or equal to %evl
; are treated as though %mask were false for those lanes.

%masked.a = select <4 x i1> %mask, <4 x float> %a, <4 x float> <float 1.0, float 1.0, float 1.0, float 1.0>
%also.r = call float @llvm.vector.reduce.fmul.v4f32(float %start, <4 x float> %masked.a)
```

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.vp.reduce.and.v4i32(i32 <start_value>, <4 x i32> <val>, <4 x i1> <mask>, i32 <vector_length>)
declare i16 @llvm.vp.reduce.and.nxv8i16(i16 <start_value>, <vscale x 8 x i16> <val>, <vscale x 8 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer `AND` reduction of a vector and a scalar starting value, returning the result as a scalar.

##### Arguments:

The first argument is the start value of the reduction, which must be a scalar integer type equal to the result type. The second argument is the vector on which the reduction is performed and must be a vector of integer values whose element type is the result/start type. The third argument is the vector mask and is a vector of boolean values with the same number of elements as the vector argument. The fourth argument is the explicit vector length of the operation.

##### Semantics:
