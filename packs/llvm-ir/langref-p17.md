---
title: "LLVM Language Reference Manual (part 17/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 17/20
---

# LLVM Language Reference Manual

The ‘`llvm.vp.fpext`’ intrinsic takes a value to cast as its first argument. The return type is the type to cast the value to. Both types must be vector of floating-point type. The bit size of the value must be smaller than the bit size of the return type. This implies that ‘`llvm.vp.fpext`’ cannot be used to make a *no-op cast*. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fpext`’ intrinsic extends the `value` from a smaller floating-point type to a larger floating-point type. The ‘`llvm.vp.fpext`’ cannot be used to make a *no-op cast* because it always changes bits. Use `bitcast` to make a *no-op cast* for a floating-point cast. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x double> @llvm.vp.fpext.v4f64.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fpext <4 x float> %a to <4 x double>
%also.r = select <4 x i1> %mask, <4 x double> %t, <4 x double> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.fptoui.v16i32.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.fptoui.nxv4i32.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.fptoui.v256i64.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.fptoui`’ intrinsic converts the floating-point argument to the unsigned integer return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.fptoui`’ intrinsic takes a value to cast as its first argument. The value to cast must be a vector of floating-point type. The return type is the type to cast the value to. The return type must be vector of integer type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fptoui`’ intrinsic converts its floating-point argument into the nearest (rounding towards zero) unsigned integer value where the lane position is below the explicit vector length and the vector mask is true. Masked-off lanes are `poison`. On enabled lanes where conversion takes place and the value cannot fit in the return type, the result on that lane is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.fptoui.v4i32.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fptoui <4 x float> %a to <4 x i32>
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.fptosi.v16i32.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.fptosi.nxv4i32.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.fptosi.v256i64.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.fptosi`’ intrinsic converts the floating-point argument to the signed integer return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.fptosi`’ intrinsic takes a value to cast as its first argument. The value to cast must be a vector of floating-point type. The return type is the type to cast the value to. The return type must be vector of integer type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fptosi`’ intrinsic converts its floating-point argument into the nearest (rounding towards zero) signed integer value where the lane position is below the explicit vector length and the vector mask is true. Masked-off lanes are `poison`. On enabled lanes where conversion takes place and the value cannot fit in the return type, the result on that lane is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.fptosi.v4i32.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fptosi <4 x float> %a to <4 x i32>
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.uitofp.v16f32.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.uitofp.nxv4f32.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.uitofp.v256f64.v256i64 (<256 x i64> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.uitofp`’ intrinsic converts its unsigned integer argument to the floating-point return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.uitofp`’ intrinsic takes a value to cast as its first argument. The value to cast must be vector of integer type. The return type is the type to cast the value to. The return type must be a vector of floating-point type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.uitofp`’ intrinsic interprets its first argument as an unsigned integer quantity and converts it to the corresponding floating-point value. If the value cannot be exactly represented, it is rounded using the default rounding mode. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.uitofp.v4f32.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = uitofp <4 x i32> %a to <4 x float>
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.sitofp.v16f32.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.sitofp.nxv4f32.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.sitofp.v256f64.v256i64 (<256 x i64> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.sitofp`’ intrinsic converts its signed integer argument to the floating-point return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.sitofp`’ intrinsic takes a value to cast as its first argument. The value to cast must be vector of integer type. The return type is the type to cast the value to. The return type must be a vector of floating-point type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sitofp`’ intrinsic interprets its first argument as a signed integer quantity and converts it to the corresponding floating-point value. If the value cannot be exactly represented, it is rounded using the default rounding mode. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.sitofp.v4f32.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = sitofp <4 x i32> %a to <4 x float>
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i8>  @llvm.vp.ptrtoint.v16i8.v16p0(<16 x ptr> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i8>  @llvm.vp.ptrtoint.nxv4i8.nxv4p0(<vscale x 4 x ptr> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.ptrtoint.v16i64.v16p0(<256 x ptr> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.ptrtoint`’ intrinsic converts its pointer to the integer return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.ptrtoint`’ intrinsic takes a value to cast as its first argument , which must be a vector of pointers, and a type to cast it to return type, which must be a vector of integer type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.ptrtoint`’ intrinsic converts value to return type by interpreting the pointer value as an integer and either truncating or zero extending that value to the size of the integer type. If `value` is smaller than return type, then a zero extension is done. If `value` is larger than return type, then a truncation is done. If they are the same size, then nothing is done (*no-op cast*) other than a type change. The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i8> @llvm.vp.ptrtoint.v4i8.v4p0i32(<4 x ptr> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = ptrtoint <4 x ptr> %a to <4 x i8>
%also.r = select <4 x i1> %mask, <4 x i8> %t, <4 x i8> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x ptr>  @llvm.vp.inttoptr.v16p0.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x ptr>  @llvm.vp.inttoptr.nxv4p0.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x ptr>  @llvm.vp.inttoptr.v256p0.v256i32 (<256 x i32> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.inttoptr`’ intrinsic converts its integer value to the point return type. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.inttoptr`’ intrinsic takes a value to cast as its first argument , which must be a vector of integer type, and a type to cast it to return type, which must be a vector of pointers type. The second argument is the vector mask. The return type, the value to cast, and the vector mask have the same number of elements. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.inttoptr`’ intrinsic converts `value` to return type by applying either a zero extension or a truncation depending on the size of the integer `value`. If `value` is larger than the size of a pointer, then a truncation is done. If `value` is smaller than the size of a pointer, then a zero extension is done. If they are the same size, nothing is done (*no-op cast*). The conversion is performed on lane positions below the explicit vector length and where the vector mask is true. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x ptr> @llvm.vp.inttoptr.v4p0i32.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = inttoptr <4 x i32> %a to <4 x ptr>
%also.r = select <4 x i1> %mask, <4 x ptr> %t, <4 x ptr> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i1> @llvm.vp.fcmp.v16f32(<16 x float> <left_op>, <16 x float> <right_op>, metadata <condition code>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i1> @llvm.vp.fcmp.nxv4f32(<vscale x 4 x float> <left_op>, <vscale x 4 x float> <right_op>, metadata <condition code>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i1> @llvm.vp.fcmp.v256f64(<256 x double> <left_op>, <256 x double> <right_op>, metadata <condition code>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.fcmp`’ intrinsic returns a vector of boolean values based on the comparison of its arguments. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.fcmp`’ intrinsic takes the two values to compare as its first and second arguments. These two values must be vectors of floating-point types. The return type is the result of the comparison. The return type must be a vector of i1 type. The fourth argument is the vector mask. The return type, the values to compare, and the vector mask have the same number of elements. The third argument is the condition code indicating the kind of comparison to perform. It must be a metadata string with one of the supported floating-point condition code values. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fcmp`’ compares its first two arguments according to the condition code given as the third argument. The arguments are compared element by element on each enabled lane, where the semantics of the comparison are defined according to the condition code. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i1> @llvm.vp.fcmp.v4f32(<4 x float> %a, <4 x float> %b, metadata !"oeq", <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = fcmp oeq <4 x float> %a, %b
%also.r = select <4 x i1> %mask, <4 x i1> %t, <4 x i1> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <32 x i1> @llvm.vp.icmp.v32i32(<32 x i32> <left_op>, <32 x i32> <right_op>, metadata <condition code>, <32 x i1> <mask>, i32 <vector_length>)
declare <vscale x 2 x i1> @llvm.vp.icmp.nxv2i32(<vscale x 2 x i32> <left_op>, <vscale x 2 x i32> <right_op>, metadata <condition code>, <vscale x 2 x i1> <mask>, i32 <vector_length>)
declare <128 x i1> @llvm.vp.icmp.v128i8(<128 x i8> <left_op>, <128 x i8> <right_op>, metadata <condition code>, <128 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

The ‘`llvm.vp.icmp`’ intrinsic returns a vector of boolean values based on the comparison of its arguments. The operation has a mask and an explicit vector length parameter.

##### Arguments:

The ‘`llvm.vp.icmp`’ intrinsic takes the two values to compare as its first and second arguments. These two values must be vectors of integer types. The return type is the result of the comparison. The return type must be a vector of i1 type. The fourth argument is the vector mask. The return type, the values to compare, and the vector mask have the same number of elements. The third argument is the condition code indicating the kind of comparison to perform. It must be a metadata string with one of the supported integer condition code values. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.icmp`’ compares its first two arguments according to the condition code given as the third argument. The arguments are compared element by element on each enabled lane, where the semantics of the comparison are defined according to the condition code. Masked-off lanes are `poison`.

##### Examples:

```llvm
%r = call <4 x i1> @llvm.vp.icmp.v4i32(<4 x i32> %a, <4 x i32> %b, metadata !"ne", <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = icmp ne <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i1> %t, <4 x i1> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.ceil.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.ceil.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.ceil.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point ceiling of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.ceil`’ intrinsic performs floating-point ceiling (ceil) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.ceil.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.ceil.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.floor.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.floor.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.floor.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point floor of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.floor`’ intrinsic performs floating-point floor (floor) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.floor.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.floor.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.rint.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.rint.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.rint.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point rint of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.rint`’ intrinsic performs floating-point rint (rint) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.rint.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.rint.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.nearbyint.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.nearbyint.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.nearbyint.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point nearbyint of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.nearbyint`’ intrinsic performs floating-point nearbyint (nearbyint) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.nearbyint.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.nearbyint.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.round.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.round.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.round.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point round of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.round`’ intrinsic performs floating-point round (round) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.round.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.round.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.roundeven.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.roundeven.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.roundeven.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point roundeven of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.roundeven`’ intrinsic performs floating-point roundeven (roundeven) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.roundeven.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.roundeven.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x float>  @llvm.vp.roundtozero.v16f32 (<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x float>  @llvm.vp.roundtozero.nxv4f32 (<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x double>  @llvm.vp.roundtozero.v256f64 (<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated floating-point round-to-zero of a vector of floating-point values.

##### Arguments:

The first argument and the result have the same vector of floating-point type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.roundtozero`’ intrinsic performs floating-point roundeven (llvm.trunc) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x float> @llvm.vp.roundtozero.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x float> @llvm.trunc.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x float> %t, <4 x float> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32> @llvm.vp.lrint.v16i32.v16f32(<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32> @llvm.vp.lrint.nxv4i32.nxv4f32(<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64> @llvm.vp.lrint.v256i64.v256f64(<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated lrint of a vector of floating-point values.

##### Arguments:

The result is an integer vector and the first argument is a vector of floating-point type with the same number of elements as the result vector type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.lrint`’ intrinsic performs lrint (lrint) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.lrint.v4i32.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.lrint.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32> @llvm.vp.llrint.v16i32.v16f32(<16 x float> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32> @llvm.vp.llrint.nxv4i32.nxv4f32(<vscale x 4 x float> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64> @llvm.vp.llrint.v256i64.v256f64(<256 x double> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated llrint of a vector of floating-point values.

##### Arguments:

The result is an integer vector and the first argument is a vector of floating-point type with the same number of elements as the result vector type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.llrint`’ intrinsic performs lrint (llrint) of the first vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.llrint.v4i32.v4f32(<4 x float> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.llrint.v4f32(<4 x float> %a)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.bitreverse.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.bitreverse.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.bitreverse.v256i64 (<256 x i64> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated bitreverse of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.bitreverse`’ intrinsic performs bitreverse (bitreverse) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.bitreverse.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.bitreverse.v4i32(<4 x i32> %a)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.bswap.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.bswap.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.bswap.v256i64 (<256 x i64> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated bswap of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.bswap`’ intrinsic performs bswap (bswap) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.bswap.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.bswap.v4i32(<4 x i32> %a)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.ctpop.v16i32 (<16 x i32> <op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.ctpop.nxv4i32 (<vscale x 4 x i32> <op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.ctpop.v256i64 (<256 x i64> <op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated ctpop of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument is the vector mask and has the same number of elements as the result vector type. The third argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.ctpop`’ intrinsic performs ctpop (ctpop) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.ctpop.v4i32(<4 x i32> %a, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.ctpop.v4i32(<4 x i32> %a)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.ctlz.v16i32 (<16 x i32> <op>, i1 <is_zero_poison>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.ctlz.nxv4i32 (<vscale x 4 x i32> <op>, i1 <is_zero_poison>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.ctlz.v256i64 (<256 x i64> <op>, i1 <is_zero_poison>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated ctlz of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is zero. The third argument is the vector mask and has the same number of elements as the result vector type. the fourth argument is the explicit vector length of the operation. If the first argument is zero and the second argument is true, the result is poison.

##### Semantics:

The ‘`llvm.vp.ctlz`’ intrinsic performs ctlz (ctlz) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.ctlz.v4i32(<4 x i32> %a, i1 false, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.ctlz.v4i32(<4 x i32> %a, i1 false)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.cttz.v16i32 (<16 x i32> <op>, i1 <is_zero_poison>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.cttz.nxv4i32 (<vscale x 4 x i32> <op>, i1 <is_zero_poison>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.cttz.v256i64 (<256 x i64> <op>, i1 <is_zero_poison>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated cttz of a vector of integers.

##### Arguments:

The first argument and the result have the same vector of integer type. The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is zero. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation. If the first argument is zero and the second argument is true, the result is poison.

##### Semantics:

The ‘`llvm.vp.cttz`’ intrinsic performs cttz (cttz) of the first argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.cttz.v4i32(<4 x i32> %a, i1 false, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.cttz.v4i32(<4 x i32> %a, i1 false)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.vp.cttz.elts` on any vector of integer elements, both fixed width and scalable.

```
declare i32  @llvm.vp.cttz.elts.i32.v16i32 (<16 x i32> <op>, i1 <is_zero_poison>, <16 x i1> <mask>, i32 <vector_length>)
declare i64  @llvm.vp.cttz.elts.i64.nxv4i32 (<vscale x 4 x i32> <op>, i1 <is_zero_poison>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare i64  @llvm.vp.cttz.elts.i64.v256i1 (<256 x i1> <op>, i1 <is_zero_poison>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

This ‘`llvm.vp.cttz.elts`’ intrinsic counts the number of trailing zero elements of a vector. This is basically the vector-predicated version of ‘`llvm.experimental.cttz.elts`’.

##### Arguments:

The first argument is the vector to be counted. This argument must be a vector with integer element type. The return type must also be an integer type which is wide enough to hold the maximum number of elements of the source vector. The result is a poison value if the return type is not wide enough for the number of elements in the input vector.

The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is all zero.

The third argument is the vector mask and has the same number of elements as the input vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.cttz.elts`’ intrinsic counts the trailing (least significant / lowest-numbered) zero elements in the first argument on each enabled lane. If the first argument is all zero and the second argument is true, the result is poison. Otherwise, it returns the explicit vector length (i.e., the fourth argument).

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.sadd.sat.v16i32 (<16 x i32> <left_op> <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.sadd.sat.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.sadd.sat.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated signed saturating addition of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sadd.sat`’ intrinsic performs sadd.sat (sadd.sat) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.sadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.sadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.uadd.sat.v16i32 (<16 x i32> <left_op> <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.uadd.sat.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.uadd.sat.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated unsigned saturating addition of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.uadd.sat`’ intrinsic performs uadd.sat (uadd.sat) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.uadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.uadd.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.ssub.sat.v16i32 (<16 x i32> <left_op> <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.ssub.sat.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.ssub.sat.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated signed saturating subtraction of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.ssub.sat`’ intrinsic performs ssub.sat (ssub.sat) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.ssub.sat.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.ssub.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.usub.sat.v16i32 (<16 x i32> <left_op> <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.usub.sat.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.usub.sat.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated unsigned saturating subtraction of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.usub.sat`’ intrinsic performs usub.sat (usub.sat) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.usub.sat.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.usub.sat.v4i32(<4 x i32> %a, <4 x i32> %b)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.fshl.v16i32 (<16 x i32> <left_op>, <16 x i32> <middle_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.fshl.nxv4i32  (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <middle_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.fshl.v256i64 (<256 x i64> <left_op>, <256 x i64> <middle_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated fshl of three vectors of integers.

##### Arguments:

The first three arguments and the result have the same vector of integer type. The fourth argument is the vector mask and has the same number of elements as the result vector type. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fshl`’ intrinsic performs fshl (fshl) of the first, second, and third vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.fshl.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i32> %c, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.fshl.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i32> %c)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.fshr.v16i32 (<16 x i32> <left_op>, <16 x i32> <middle_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.fshr.nxv4i32  (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <middle_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.fshr.v256i64 (<256 x i64> <left_op>, <256 x i64> <middle_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated fshr of three vectors of integers.

##### Arguments:

The first three arguments and the result have the same vector of integer type. The fourth argument is the vector mask and has the same number of elements as the result vector type. The fifth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.fshr`’ intrinsic performs fshr (fshr) of the first, second, and third vector argument on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.fshr.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i32> %c, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = call <4 x i32> @llvm.fshr.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i32> %c)
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <vscale x 2 x i1> @llvm.vp.is.fpclass.nxv2f32(<vscale x 2 x float> <op>, i32 <test>, <vscale x 2 x i1> <mask>, i32 <vector_length>)
declare <2 x i1> @llvm.vp.is.fpclass.v2f16(<2 x half> <op>, i32 <test>, <2 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated `llvm.is.fpclass` llvm.is.fpclass

##### Arguments:

The first argument is a floating-point vector, the result type is a vector of boolean with the same number of elements as the first argument. The second argument specifies, which tests to perform llvm.is.fpclass. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.is.fpclass`’ intrinsic performs `llvm.is.fpclass` (llvm.is.fpclass).

##### Examples:

```llvm
%r = call <2 x i1> @llvm.vp.is.fpclass.v2f16(<2 x half> %x, i32 3, <2 x i1> %m, i32 %evl)
%t = call <vscale x 2 x i1> @llvm.vp.is.fpclass.nxv2f16(<vscale x 2 x half> %x, i32 3, <vscale x 2 x i1> %m, i32 %evl)
```

LLVM provides intrinsics for predicated vector load and store operations. The predicate is specified by a mask argument, which holds one bit per vector element, switching the associated vector lane on or off. The memory addresses corresponding to the “off” lanes are not accessed. When all bits of the mask are on, the intrinsic is identical to a regular vector load or store. When all bits are off, no memory is accessed.

##### Syntax:

This is an overloaded intrinsic. The loaded data is a vector of any integer, floating-point or pointer data type.

```
declare <16 x float>  @llvm.masked.load.v16f32.p0(ptr <ptr>, <16 x i1> <mask>, <16 x float> <passthru>)
declare <2 x double>  @llvm.masked.load.v2f64.p0(ptr <ptr>, <2 x i1>  <mask>, <2 x double> <passthru>)
;; The data is a vector of pointers
declare <8 x ptr> @llvm.masked.load.v8p0.p0(ptr <ptr>, <8 x i1> <mask>, <8 x ptr> <passthru>)
```

##### Overview:

Reads a vector from memory according to the provided mask. The mask holds a bit for each vector lane, and is used to prevent memory accesses to the masked-off lanes. The masked-off lanes in the result vector are taken from the corresponding lanes of the ‘`passthru`’ argument.

##### Arguments:

The first argument is the base pointer for the load. The second argument, mask, is a vector of boolean values with the same number of elements as the return type. The third is a pass-through value that is used to fill the masked-off lanes of the result. The return type, underlying type of the base pointer and the type of the ‘`passthru`’ argument are the same vector types.

The alignment of the base pointer can be specified using the `align` attribute on the first argument.

##### Semantics:

The ‘`llvm.masked.load`’ intrinsic is designed for conditional reading of selected vector elements in a single IR operation. It is useful for targets that support vector masked loads and allows vectorizing predicated basic blocks on these targets. Other targets may support this intrinsic differently, for example by lowering it into a sequence of branches that guard scalar load operations. The result of this operation is equivalent to a regular vector load instruction followed by a ‘select’ between the loaded and the passthru values, predicated on the same mask, except that the masked-off lanes are not accessed. Only the masked-on lanes of the vector need to be inbounds of an allocation (but all these lanes need to be inbounds of the same allocation). In particular, using this intrinsic prevents exceptions on memory accesses to masked-off lanes. Masked-off lanes are also not considered accessed for the purpose of data races or `noalias` constraints.
