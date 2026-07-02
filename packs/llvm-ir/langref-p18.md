---
title: "LLVM Language Reference Manual (part 18/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 18/20
---

# LLVM Language Reference Manual

```
%res = call <16 x float> @llvm.masked.load.v16f32.p0(ptr align 4 %ptr, <16 x i1>%mask, <16 x float> %passthru)

;; The result of the two following instructions is identical aside from potential memory access exception
%loadlal = load <16 x float>, ptr %ptr, align 4
%res = select <16 x i1> %mask, <16 x float> %loadlal, <16 x float> %passthru
```

##### Syntax:

This is an overloaded intrinsic. The data stored in memory is a vector of any integer, floating-point or pointer data type.

```
declare void @llvm.masked.store.v8i32.p0 (<8  x i32>   <value>, ptr <ptr>, <8  x i1> <mask>)
declare void @llvm.masked.store.v16f32.p0(<16 x float> <value>, ptr <ptr>, <16 x i1> <mask>)
;; The data is a vector of pointers
declare void @llvm.masked.store.v8p0.p0  (<8 x ptr>    <value>, ptr <ptr>, <8 x i1> <mask>)
```

##### Overview:

Writes a vector to memory according to the provided mask. The mask holds a bit for each vector lane, and is used to prevent memory accesses to the masked-off lanes.

##### Arguments:

The first argument is the vector value to be written to memory. The second argument is the base pointer for the store, it has the same underlying type as the value argument. The third argument, mask, is a vector of boolean values. The types of the mask and the value argument must have the same number of vector elements.

The alignment of the base pointer can be specified using the `align` attribute on the second argument.

##### Semantics:

The ‘`llvm.masked.store`’ intrinsics is designed for conditional writing of selected vector elements in a single IR operation. It is useful for targets that support vector masked store and allows vectorizing predicated basic blocks on these targets. Other targets may support this intrinsic differently, for example by lowering it into a sequence of branches that guard scalar store operations. The result of this operation is equivalent to a load-modify-store sequence, except that the masked-off lanes are not accessed. Only the masked-on lanes of the vector need to be inbounds of an allocation (but all these lanes need to be inbounds of the same allocation). In particular, using this intrinsic prevents exceptions on memory accesses to masked-off lanes. Masked-off lanes are also not considered accessed for the purpose of data races or `noalias` constraints.

```
call void @llvm.masked.store.v16f32.p0(<16 x float> %value, ptr align 4 %ptr, <16 x i1> %mask)

;; The result of the following instructions is identical aside from potential data races and memory access exceptions
%oldval = load <16 x float>, ptr %ptr, align 4
%res = select <16 x i1> %mask, <16 x float> %value, <16 x float> %oldval
store <16 x float> %res, ptr %ptr, align 4
```

LLVM provides intrinsics for vector gather and scatter operations. They are similar to Masked Vector Load and Store, except they are designed for arbitrary memory accesses, rather than sequential memory accesses. Gather and scatter also employ a mask argument, which holds one bit per vector element, switching the associated vector lane on or off. The memory addresses corresponding to the “off” lanes are not accessed. When all bits are off, no memory is accessed.

##### Syntax:

This is an overloaded intrinsic. The loaded data are multiple scalar values of any integer, floating-point or pointer data type gathered together into one vector.

```
declare <16 x float> @llvm.masked.gather.v16f32.v16p0(<16 x ptr> <ptrs>, <16 x i1> <mask>, <16 x float> <passthru>)
declare <2 x double> @llvm.masked.gather.v2f64.v2p1(<2 x ptr addrspace(1)> <ptrs>, <2 x i1>  <mask>, <2 x double> <passthru>)
declare <8 x ptr> @llvm.masked.gather.v8p0.v8p0(<8 x ptr> <ptrs>, <8 x i1>  <mask>, <8 x ptr> <passthru>)
```

##### Overview:

Reads scalar values from arbitrary memory locations and gathers them into one vector. The memory locations are provided in the vector of pointers ‘`ptrs`’. The memory is accessed according to the provided mask. The mask holds a bit for each vector lane, and is used to prevent memory accesses to the masked-off lanes. The masked-off lanes in the result vector are taken from the corresponding lanes of the ‘`passthru`’ argument.

##### Arguments:

The first argument is a vector of pointers which holds all memory addresses to read. The second argument, mask, is a vector of boolean values with the same number of elements as the return type. The third is a pass-through value that is used to fill the masked-off lanes of the result. The return type, underlying type of the vector of pointers and the type of the ‘`passthru`’ argument are the same vector types.

The alignment of the pointers can be specified using the `align` attribute on the first argument.

##### Semantics:

The ‘`llvm.masked.gather`’ intrinsic is designed for conditional reading of multiple scalar values from arbitrary memory locations in a single IR operation. It is useful for targets that support vector masked gathers and allows vectorizing basic blocks with data and control divergence. Other targets may support this intrinsic differently, for example by lowering it into a sequence of scalar load operations. The semantics of this operation are equivalent to a sequence of conditional scalar loads with subsequent gathering all loaded values into a single vector. The mask restricts memory access to certain lanes and facilitates vectorization of predicated basic blocks.

```
%res = call <4 x double> @llvm.masked.gather.v4f64.v4p0(<4 x ptr> align 8 %ptrs, <4 x i1> <i1 true, i1 true, i1 true, i1 true>, <4 x double> poison)

;; The gather with all-true mask is equivalent to the following instruction sequence
%ptr0 = extractelement <4 x ptr> %ptrs, i32 0
%ptr1 = extractelement <4 x ptr> %ptrs, i32 1
%ptr2 = extractelement <4 x ptr> %ptrs, i32 2
%ptr3 = extractelement <4 x ptr> %ptrs, i32 3

%val0 = load double, ptr %ptr0, align 8
%val1 = load double, ptr %ptr1, align 8
%val2 = load double, ptr %ptr2, align 8
%val3 = load double, ptr %ptr3, align 8

%vec0    = insertelement <4 x double> poison, %val0, 0
%vec01   = insertelement <4 x double> %vec0, %val1, 1
%vec012  = insertelement <4 x double> %vec01, %val2, 2
%vec0123 = insertelement <4 x double> %vec012, %val3, 3
```

##### Syntax:

This is an overloaded intrinsic. The data stored in memory is a vector of any integer, floating-point or pointer data type. Each vector element is stored in an arbitrary memory address. Scatter with overlapping addresses is guaranteed to be ordered from least-significant to most-significant element.

```
declare void @llvm.masked.scatter.v8i32.v8p0  (<8 x i32>    <value>, <8 x ptr>               <ptrs>, <8 x i1>  <mask>)
declare void @llvm.masked.scatter.v16f32.v16p1(<16 x float> <value>, <16 x ptr addrspace(1)> <ptrs>, <16 x i1> <mask>)
declare void @llvm.masked.scatter.v4p0.v4p0   (<4 x ptr>    <value>, <4 x ptr>               <ptrs>, <4 x i1>  <mask>)
```

##### Overview:

Writes each element from the value vector to the corresponding memory address. The memory addresses are represented as a vector of pointers. Writing is done according to the provided mask. The mask holds a bit for each vector lane, and is used to prevent memory accesses to the masked-off lanes.

##### Arguments:

The first argument is a vector value to be written to memory. The second argument is a vector of pointers, pointing to where the value elements should be stored. It has the same underlying type as the value argument. The third argument, mask, is a vector of boolean values. The types of the mask and the value argument must have the same number of vector elements.

The alignment of the pointers can be specified using the `align` attribute on the second argument.

##### Semantics:

The ‘`llvm.masked.scatter`’ intrinsics is designed for writing selected vector elements to arbitrary memory addresses in a single IR operation. The operation may be conditional, when not all bits in the mask are switched on. It is useful for targets that support vector masked scatter and allows vectorizing basic blocks with data and control divergence. Other targets may support this intrinsic differently, for example by lowering it into a sequence of branches that guard scalar store operations.

```
;; This instruction unconditionally stores data vector in multiple addresses
call @llvm.masked.scatter.v8i32.v8p0(<8 x i32> %value, <8 x ptr> align 4 %ptrs,  <8 x i1>  <true, true, .. true>)

;; It is equivalent to a list of scalar stores
%val0 = extractelement <8 x i32> %value, i32 0
%val1 = extractelement <8 x i32> %value, i32 1
..
%val7 = extractelement <8 x i32> %value, i32 7
%ptr0 = extractelement <8 x ptr> %ptrs, i32 0
%ptr1 = extractelement <8 x ptr> %ptrs, i32 1
..
%ptr7 = extractelement <8 x ptr> %ptrs, i32 7
;; Note: the order of the following stores is important when they overlap:
store i32 %val0, ptr %ptr0, align 4
store i32 %val1, ptr %ptr1, align 4
..
store i32 %val7, ptr %ptr7, align 4
```

LLVM provides intrinsics for expanding load and compressing store operations. Data selected from a vector according to a mask is stored in consecutive memory addresses (compressed store), and vice-versa (expanding load). These operations effective map to “if (cond.i) a[j++] = v.i” and “if (cond.i) v.i = a[j++]” patterns, respectively. Note that when the mask starts with ‘1’ bits followed by ‘0’ bits, these operations are identical to llvm.masked.store and llvm.masked.load.

##### Syntax:

This is an overloaded intrinsic. Several values of integer, floating point or pointer data type are loaded from consecutive memory addresses and stored into the elements of a vector according to the mask.

```
declare <16 x float>  @llvm.masked.expandload.v16f32 (ptr <ptr>, <16 x i1> <mask>, <16 x float> <passthru>)
declare <2 x i64>     @llvm.masked.expandload.v2i64 (ptr <ptr>, <2 x i1>  <mask>, <2 x i64> <passthru>)
```

##### Overview:

Reads a number of scalar values sequentially from memory location provided in ‘`ptr`’ and spreads them in a vector. The ‘`mask`’ holds a bit for each vector lane. The number of elements read from memory is equal to the number of ‘1’ bits in the mask. The loaded elements are positioned in the destination vector according to the sequence of ‘1’ and ‘0’ bits in the mask. E.g., if the mask vector is ‘10010001’, “expandload” reads 3 values from memory addresses ptr, ptr+1, ptr+2 and places them in lanes 0, 3 and 7 accordingly. The masked-off lanes are filled by elements from the corresponding lanes of the ‘`passthru`’ argument.

##### Arguments:

The first argument is the base pointer for the load. It has the same underlying type as the element of the returned vector. The second argument, mask, is a vector of boolean values with the same number of elements as the return type. The third is a pass-through value that is used to fill the masked-off lanes of the result. The return type and the type of the ‘`passthru`’ argument have the same vector type.

The align parameter attribute can be provided for the first argument. The pointer alignment defaults to 1.

##### Semantics:

The ‘`llvm.masked.expandload`’ intrinsic is designed for reading multiple scalar values from adjacent memory addresses into possibly non-adjacent vector lanes. It is useful for targets that support vector expanding loads and allows vectorizing loop with cross-iteration dependency like in the following example:

```c
// In this loop we load from B and spread the elements into array A.
double *A, B; int *C;
for (int i = 0; i < size; ++i) {
  if (C[i] != 0)
    A[i] = B[j++];
}
```

```llvm
; Load several elements from array B and expand them in a vector.
; The number of loaded elements is equal to the number of '1' elements in the Mask.
%Tmp = call <8 x double> @llvm.masked.expandload.v8f64(ptr %Bptr, <8 x i1> %Mask, <8 x double> poison)
; Store the result in A
call void @llvm.masked.store.v8f64.p0(<8 x double> %Tmp, ptr %Aptr, i32 8, <8 x i1> %Mask)

; %Bptr should be increased on each iteration according to the number of '1' elements in the Mask.
%MaskI = bitcast <8 x i1> %Mask to i8
%MaskIPopcnt = call i8 @llvm.ctpop.i8(i8 %MaskI)
%MaskI64 = zext i8 %MaskIPopcnt to i64
%BNextInd = add i64 %BInd, %MaskI64
```

Other targets may support this intrinsic differently, for example, by lowering it into a sequence of conditional scalar load operations and shuffles. If all mask elements are ‘1’, the intrinsic behavior is equivalent to the regular unmasked vector load.

##### Syntax:

This is an overloaded intrinsic. A number of scalar values of integer, floating point or pointer data type are collected from an input vector and stored into adjacent memory addresses. A mask defines which elements to collect from the vector.

```
declare void @llvm.masked.compressstore.v8i32  (<8  x i32>   <value>, ptr <ptr>, <8  x i1> <mask>)
declare void @llvm.masked.compressstore.v16f32 (<16 x float> <value>, ptr <ptr>, <16 x i1> <mask>)
```

##### Overview:

Selects elements from input vector ‘`value`’ according to the ‘`mask`’. All selected elements are written into adjacent memory addresses starting at address ‘*ptr*’, from lower to higher. The mask holds a bit for each vector lane, and is used to select elements to be stored. The number of elements to be stored is equal to the number of active bits in the mask.

##### Arguments:

The first argument is the input vector, from which elements are collected and written to memory. The second argument is the base pointer for the store, it has the same underlying type as the element of the input vector argument. The third argument is the mask, a vector of boolean values. The mask and the input vector must have the same number of vector elements.

The align parameter attribute can be provided for the second argument. The pointer alignment defaults to 1.

##### Semantics:

The ‘`llvm.masked.compressstore`’ intrinsic is designed for compressing data in memory. It allows to collect elements from possibly non-adjacent lanes of a vector and store them contiguously in memory in one IR operation. It is useful for targets that support compressing store operations and allows vectorizing loops with cross-iteration dependencies like in the following example:

```c
// In this loop we load elements from A and store them consecutively in B
double *A, B; int *C;
for (int i = 0; i < size; ++i) {
  if (C[i] != 0)
    B[j++] = A[i]
}
```

```llvm
; Load elements from A.
%Tmp = call <8 x double> @llvm.masked.load.v8f64.p0(ptr %Aptr, i32 8, <8 x i1> %Mask, <8 x double> poison)
; Store all selected elements consecutively in array B
call <void> @llvm.masked.compressstore.v8f64(<8 x double> %Tmp, ptr %Bptr, <8 x i1> %Mask)

; %Bptr should be increased on each iteration according to the number of '1' elements in the Mask.
%MaskI = bitcast <8 x i1> %Mask to i8
%MaskIPopcnt = call i8 @llvm.ctpop.i8(i8 %MaskI)
%MaskI64 = zext i8 %MaskIPopcnt to i64
%BNextInd = add i64 %BInd, %MaskI64
```

Other targets may support this intrinsic differently, for example, by lowering it into a sequence of branches that guard scalar store operations.

##### Syntax:

This is an overloaded intrinsic.

```
declare <8 x i32> @llvm.masked.udiv.v8i32(<8 x i32> <op1>, <8 x i32> <op2>, <8 x i1> <mask>)
declare <vscale x 2 x i64> @llvm.masked.udiv.nxv2i64(<vscale x 2 x i64> <op1>, <vscale x 2 x i64> <op2>, <vscale x 2 x i1> <mask>)
```

##### Overview:

Performs unsigned division (udiv) of two vectors of integers, but only on enabled lanes.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type.

##### Semantics:

Follows the same semantics as udiv with the exception that disabled lanes cannot produce undefined behaviour and always result in poison.

##### Syntax:

This is an overloaded intrinsic.

```
declare <8 x i32> @llvm.masked.sdiv.v8i32(<8 x i32> <op1>, <8 x i32> <op2>, <8 x i1> <mask>)
declare <vscale x 2 x i64> @llvm.masked.sdiv.nxv2i64(<vscale x 2 x i64> <op1>, <vscale x 2 x i64> <op2>, <vscale x 2 x i1> <mask>)
```

##### Overview:

Performs signed division (sdiv) of two vectors of integers, but only on enabled lanes.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type.

##### Semantics:

Follows the same semantics as sdiv with the exception that disabled lanes cannot produce undefined behaviour and always result in poison.

##### Syntax:

This is an overloaded intrinsic.

```
declare <8 x i32> @llvm.masked.urem.v8i32(<8 x i32> <op1>, <8 x i32> <op2>, <8 x i1> <mask>)
declare <vscale x 2 x i64> @llvm.masked.urem.nxv2i64(<vscale x 2 x i64> <op1>, <vscale x 2 x i64> <op2>, <vscale x 2 x i1> <mask>)
```

##### Overview:

Computes the remainder from the unsigned division (urem) of two vectors of integers, but only on enabled lanes.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type.

##### Semantics:

Follows the same semantics as urem with the exception that disabled lanes cannot produce undefined behaviour and always result in poison.

##### Syntax:

This is an overloaded intrinsic.

```
declare <8 x i32> @llvm.masked.srem.v8i32(<8 x i32> <op1>, <8 x i32> <op2>, <8 x i1> <mask>)
declare <vscale x 2 x i64> @llvm.masked.srem.nxv2i64(<vscale x 2 x i64> <op1>, <vscale x 2 x i64> <op2>, <vscale x 2 x i1> <mask>)
```

##### Overview:

Computes the remainder from the signed division (srem) of two vectors of integers, but only on enabled lanes.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type.

##### Semantics:

Follows the same semantics as srem with the exception that disabled lanes cannot produce undefined behaviour and always result in poison.

This class of intrinsics provides information about the lifetime of allocated objects and ranges where variables are immutable.

##### Syntax:

```
declare void @llvm.lifetime.start(ptr captures(none) <ptr>)
```

##### Overview:

The ‘`llvm.lifetime.start`’ intrinsic specifies the start of a memory object’s lifetime.

##### Arguments:

The argument is either a `poison` value or an SSA variable whose defining instruction is `alloca` or a call of the `llvm.structured.alloca` intrinsics. Otherwise, the IR is considered ill-formed.

##### Semantics:

If `ptr` is a `poison` value, the intrinsic has no effect.

Otherwise, the stack-allocated object that `ptr` points to is initially marked as dead. After ‘`llvm.lifetime.start`’, the stack object is marked as alive and has an uninitialized value. Calling `llvm.lifetime.start` when the stack object is already alive just resets its contents to be uninitialized.

The stack object is marked as dead again when either llvm.lifetime.end to the alloca/structured.alloca is executed or the function returns. After llvm.lifetime.end is called, ‘`llvm.lifetime.start`’ on the stack object can be called again. The second ‘`llvm.lifetime.start`’ call marks the object as alive, but it does not change the address of the object.

##### Syntax:

```
declare void @llvm.lifetime.end(ptr captures(none) <ptr>)
```

##### Overview:

The ‘`llvm.lifetime.end`’ intrinsic specifies the end of a allocated object’s lifetime.

##### Arguments:

The argument is either a `poison` value or an SSA variable whose defining instruction is `alloca` or a call of the `llvm.structured.alloca` intrinsics. Otherwise, the IR is considered ill-formed.

##### Semantics:

If `ptr` is a `poison` value, the intrinsic has no effect.

Otherwise, the stack-allocated object that `ptr` points to becomes dead after the call to this intrinsic.

Calling `llvm.lifetime.end` on an already dead alloca/structured.alloca is no-op.

##### Syntax:

This is an overloaded intrinsic. The allocated object can belong to any address space.

```
declare ptr @llvm.invariant.start.p0(i64 <size>, ptr captures(none) <ptr>)
```

##### Overview:

The ‘`llvm.invariant.start`’ intrinsic specifies that the contents of an allocated object will not change.

##### Arguments:

The first argument is a constant integer representing the size of the object, or -1 if it is variable sized. The second argument is a pointer to the object.

##### Semantics:

This intrinsic indicates that until an `llvm.invariant.end` that uses the return value, the referenced memory location is constant and unchanging.

##### Syntax:

This is an overloaded intrinsic. The allocated object can belong to any address space.

```
declare void @llvm.invariant.end.p0(ptr <start>, i64 <size>, ptr captures(none) <ptr>)
```

##### Overview:

The ‘`llvm.invariant.end`’ intrinsic specifies that the contents of an allocated object are mutable.

##### Arguments:

The first argument is the matching `llvm.invariant.start` intrinsic. The second argument is a constant integer representing the size of the object, or -1 if it is variable sized and the third argument is a pointer to the object.

##### Semantics:

This intrinsic indicates that the memory is mutable again.

##### Syntax:

This is an overloaded intrinsic. The allocated object can belong to any address space. The returned pointer must belong to the same address space as the argument.

```
declare ptr @llvm.launder.invariant.group.p0(ptr <ptr>)
```

##### Overview:

The ‘`llvm.launder.invariant.group`’ intrinsic can be used when an invariant established by `invariant.group` metadata no longer holds, to obtain a new pointer value that carries fresh invariant group information. It is an experimental intrinsic, which means that its semantics might change in the future.

##### Arguments:

The `llvm.launder.invariant.group` takes only one argument, which is a pointer to the memory.

##### Semantics:

Returns another pointer that aliases its argument but which is considered different for the purposes of `load`/`store` `invariant.group` metadata. It does not read any accessible memory and the execution can be speculated.

##### Syntax:

This is an overloaded intrinsic. The allocated object can belong to any address space. The returned pointer must belong to the same address space as the argument.

```
declare ptr @llvm.strip.invariant.group.p0(ptr <ptr>)
```

##### Overview:

The ‘`llvm.strip.invariant.group`’ intrinsic can be used when an invariant established by `invariant.group` metadata no longer holds, to obtain a new pointer value that does not carry the invariant information. It is an experimental intrinsic, which means that its semantics might change in the future.

##### Arguments:

The `llvm.strip.invariant.group` takes only one argument, which is a pointer to the memory.

##### Semantics:

Returns another pointer that aliases its argument but which has no associated `invariant.group` metadata. It does not read any memory and can be speculated.

These intrinsics are used to provide special handling of floating-point operations when specific rounding mode or floating-point exception behavior is required. By default, LLVM optimization passes assume that the rounding mode is round-to-nearest and that floating-point exceptions will not be monitored. Constrained FP intrinsics are used to support non-default rounding modes and accurately preserve exception behavior without compromising LLVM’s ability to optimize FP code when the default behavior is used.

If any FP operation in a function is constrained then they all must be constrained. This is required for correct LLVM IR. Optimizations that move code around can create miscompiles if mixing of constrained and normal operations is done. The correct way to mix constrained and less constrained operations is to use the rounding mode and exception handling metadata to mark constrained intrinsics as having LLVM’s default behavior.

Each of these intrinsics corresponds to a normal floating-point operation. The data arguments and the return value are the same as the corresponding FP operation.

The rounding mode argument is a metadata string specifying what assumptions, if any, the optimizer can make when transforming constant values. Some constrained FP intrinsics omit this argument. If required by the intrinsic, this argument must be one of the following strings:

```
"round.dynamic"
"round.tonearest"
"round.downward"
"round.upward"
"round.towardzero"
"round.tonearestaway"
```

If this argument is “round.dynamic” optimization passes must assume that the rounding mode is unknown and may change at runtime. No transformations that depend on rounding mode may be performed in this case.

The other possible values for the rounding mode argument correspond to the similarly named IEEE rounding modes. If the argument is any of these values optimization passes may perform transformations as long as they are consistent with the specified rounding mode.

For example, ‘x-0’->’x’ is not a valid transformation if the rounding mode is “round.downward” or “round.dynamic” because if the value of ‘x’ is +0 then ‘x-0’ should evaluate to ‘-0’ when rounding downward. However, this transformation is legal for all other rounding modes.

For values other than “round.dynamic” optimization passes may assume that the actual runtime rounding mode (as defined in a target-specific manner) matches the specified rounding mode, but this is not guaranteed. Using a specific non-dynamic rounding mode which does not match the actual rounding mode at runtime results in undefined behavior.

The exception behavior argument is a metadata string describing the floating point exception semantics that required for the intrinsic. This argument must be one of the following strings:

```
"fpexcept.ignore"
"fpexcept.maytrap"
"fpexcept.strict"
```

If this argument is “fpexcept.ignore” optimization passes may assume that the exception status flags will not be read and that floating-point exceptions will be masked. This allows transformations to be performed that may change the exception semantics of the original code. For example, FP operations may be speculatively executed in this case whereas they must not be for either of the other possible values of this argument.

If the exception behavior argument is “fpexcept.maytrap” optimization passes must avoid transformations that may raise exceptions that would not have been raised by the original code (such as speculatively executing FP operations), but passes are not required to preserve all exceptions that are implied by the original code. For example, exceptions may be potentially hidden by constant folding.

If the exception behavior argument is “fpexcept.strict” all transformations must strictly preserve the floating-point exception semantics of the original code. Any FP exception that would have been raised by the original code must be raised by the transformed code, and the transformed code must not raise any FP exceptions that would not have been raised by the original code. This is the exception behavior argument that will be used if the code being compiled reads the FP exception status flags, but this mode can also be used with code that unmasks FP exceptions.

The number and order of floating-point exceptions is NOT guaranteed. For example, a series of FP operations that each may raise exceptions may be vectorized into a single instruction that raises each unique exception a single time.

Proper function attributes usage is required for the constrained intrinsics to function correctly.

All function *calls* done in a function that uses constrained floating point intrinsics must have the `strictfp` attribute either on the calling instruction or on the declaration or definition of the function being called.

All function *definitions* that use constrained floating point intrinsics must have the `strictfp` attribute.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fadd(<type> <op1>, <type> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fadd`’ intrinsic returns the sum of its two arguments.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.fadd`’ intrinsic must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The value produced is the floating-point sum of the two value arguments and has the same type as the arguments.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fsub(<type> <op1>, <type> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fsub`’ intrinsic returns the difference of its two arguments.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.fsub`’ intrinsic must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The value produced is the floating-point difference of the two value arguments and has the same type as the arguments.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fmul(<type> <op1>, <type> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fmul`’ intrinsic returns the product of its two arguments.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.fmul`’ intrinsic must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The value produced is the floating-point product of the two value arguments and has the same type as the arguments.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fdiv(<type> <op1>, <type> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fdiv`’ intrinsic returns the quotient of its two arguments.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.fdiv`’ intrinsic must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The value produced is the floating-point quotient of the two value arguments and has the same type as the arguments.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.frem(<type> <op1>, <type> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.frem`’ intrinsic returns the remainder from the division of its two arguments.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.frem`’ intrinsic must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third and fourth arguments specify the rounding mode and exception behavior as described above. The rounding mode argument has no effect, since the result of frem is never rounded, but the argument is included for consistency with the other constrained floating-point intrinsics.

##### Semantics:

The value produced is the floating-point remainder from the division of the two value arguments and has the same type as the arguments. The remainder has the same sign as the dividend.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fma(<type> <op1>, <type> <op2>, <type> <op3>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fma`’ intrinsic returns the result of a fused-multiply-add operation on its arguments.

##### Arguments:

The first three arguments to the ‘`llvm.experimental.constrained.fma`’ intrinsic must be floating-point or vector of floating-point values. All arguments must have identical types.

The fourth and fifth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The result produced is the product of the first two arguments added to the third argument computed with infinite precision, and then rounded to the target precision.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.fptoui(<type> <value>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fptoui`’ intrinsic converts a floating-point `value` to its unsigned integer equivalent of type `ty2`.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.fptoui`’ intrinsic must be floating point or vector of floating point values.

The second argument specifies the exception behavior as described above.

##### Semantics:

The result produced is an unsigned integer converted from the floating point argument. The value is truncated, so it is rounded towards zero.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.fptosi(<type> <value>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fptosi`’ intrinsic converts floating-point `value` to type `ty2`.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.fptosi`’ intrinsic must be floating point or vector of floating point values.

The second argument specifies the exception behavior as described above.

##### Semantics:

The result produced is a signed integer converted from the floating point argument. The value is truncated, so it is rounded towards zero.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.uitofp(<type> <value>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.uitofp`’ intrinsic converts an unsigned integer `value` to a floating-point of type `ty2`.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.uitofp`’ intrinsic must be an integer or vector of integer values.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

An inexact floating-point exception will be raised if rounding is required. Any result produced is a floating point value converted from the input integer argument.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.sitofp(<type> <value>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.sitofp`’ intrinsic converts a signed integer `value` to a floating-point of type `ty2`.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.sitofp`’ intrinsic must be an integer or vector of integer values.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

An inexact floating-point exception will be raised if rounding is required. Any result produced is a floating point value converted from the input integer argument.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.fptrunc(<type> <value>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fptrunc`’ intrinsic truncates `value` to type `ty2`.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.fptrunc`’ intrinsic must be floating point or vector of floating point values. This argument must be larger in size than the result.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The result produced is a floating point value truncated to be smaller in size than the argument.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.fpext(<type> <value>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fpext`’ intrinsic extends a floating-point `value` to a larger floating-point value.

##### Arguments:

The first argument to the ‘`llvm.experimental.constrained.fpext`’ intrinsic must be floating point or vector of floating point values. This argument must be smaller in size than the result.

The second argument specifies the exception behavior as described above.

##### Semantics:

The result produced is a floating point value extended to be larger in size than the argument. All restrictions that apply to the fpext instruction also apply to this intrinsic.

##### Syntax:

```
declare <ty2>
@llvm.experimental.constrained.fcmp(<type> <op1>, <type> <op2>,
                                    metadata <condition code>,
                                    metadata <exception behavior>)
declare <ty2>
@llvm.experimental.constrained.fcmps(<type> <op1>, <type> <op2>,
                                     metadata <condition code>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fcmp`’ and ‘`llvm.experimental.constrained.fcmps`’ intrinsics return a boolean value or vector of boolean values based on comparison of its arguments.

If the arguments are floating-point scalars, then the result type is a boolean (i1).

If the arguments are floating-point vectors, then the result type is a vector of boolean with the same number of elements as the arguments being compared.

The ‘`llvm.experimental.constrained.fcmp`’ intrinsic performs a quiet comparison operation while the ‘`llvm.experimental.constrained.fcmps`’ intrinsic performs a signaling comparison operation.

##### Arguments:

The first two arguments to the ‘`llvm.experimental.constrained.fcmp`’ and ‘`llvm.experimental.constrained.fcmps`’ intrinsics must be floating-point or vector of floating-point values. Both arguments must have identical types.

The third argument is the condition code indicating the kind of comparison to perform. It must be a metadata string with one of the following values:

- “`oeq`”: ordered and equal
- “`ogt`”: ordered and greater than
- “`oge`”: ordered and greater than or equal
- “`olt`”: ordered and less than
- “`ole`”: ordered and less than or equal
- “`one`”: ordered and not equal
- “`ord`”: ordered (no nans)
- “`ueq`”: unordered or equal
- “`ugt`”: unordered or greater than
- “`uge`”: unordered or greater than or equal
- “`ult`”: unordered or less than
- “`ule`”: unordered or less than or equal
- “`une`”: unordered or not equal
- “`uno`”: unordered (either nans)

*Ordered* means that neither argument is a NAN while *unordered* means that either argument may be a NAN.

The fourth argument specifies the exception behavior as described above.

##### Semantics:

`op1` and `op2` are compared according to the condition code given as the third argument. If the arguments are vectors, then the vectors are compared element by element. Each comparison performed always yields an i1 result, as follows:

- “`oeq`”: yields `true` if both arguments are not a NAN and `op1` is equal to `op2`.
- “`ogt`”: yields `true` if both arguments are not a NAN and `op1` is greater than `op2`.
- “`oge`”: yields `true` if both arguments are not a NAN and `op1` is greater than or equal to `op2`.
- “`olt`”: yields `true` if both arguments are not a NAN and `op1` is less than `op2`.
- “`ole`”: yields `true` if both arguments are not a NAN and `op1` is less than or equal to `op2`.
- “`one`”: yields `true` if both arguments are not a NAN and `op1` is not equal to `op2`.
- “`ord`”: yields `true` if both arguments are not a NAN.
- “`ueq`”: yields `true` if either argument is a NAN or `op1` is equal to `op2`.
- “`ugt`”: yields `true` if either argument is a NAN or `op1` is greater than `op2`.
- “`uge`”: yields `true` if either argument is a NAN or `op1` is greater than or equal to `op2`.
- “`ult`”: yields `true` if either argument is a NAN or `op1` is less than `op2`.
- “`ule`”: yields `true` if either argument is a NAN or `op1` is less than or equal to `op2`.
- “`une`”: yields `true` if either argument is a NAN or `op1` is not equal to `op2`.
- “`uno`”: yields `true` if either argument is a NAN.

The quiet comparison operation performed by ‘`llvm.experimental.constrained.fcmp`’ will only raise an exception if either argument is a SNAN. The signaling comparison operation performed by ‘`llvm.experimental.constrained.fcmps`’ will raise an exception if either argument is a NAN (QNAN or SNAN). Such an exception does not preclude a result being produced (e.g., exception might only set a flag), therefore the distinction between ordered and unordered comparisons is also relevant for the ‘`llvm.experimental.constrained.fcmps`’ intrinsic.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.fmuladd(<type> <op1>, <type> <op2>,
                                       <type> <op3>,
                                       metadata <rounding mode>,
                                       metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.fmuladd`’ intrinsic represents multiply-add expressions that can be fused if the code generator determines that (a) the target instruction set has support for a fused operation, and (b) that the fused operation is more efficient than the equivalent, separate pair of mul and add instructions.

##### Arguments:

The first three arguments to the ‘`llvm.experimental.constrained.fmuladd`’ intrinsic must be floating-point or vector of floating-point values. All three arguments must have identical types.

The fourth and fifth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

The expression:

```
%0 = call float @llvm.experimental.constrained.fmuladd.f32(%a, %b, %c,
                                                           metadata <rounding mode>,
                                                           metadata <exception behavior>)
```

is equivalent to the expression:

```
%0 = call float @llvm.experimental.constrained.fmul.f32(%a, %b,
                                                        metadata <rounding mode>,
                                                        metadata <exception behavior>)
%1 = call float @llvm.experimental.constrained.fadd.f32(%0, %c,
                                                        metadata <rounding mode>,
                                                        metadata <exception behavior>)
```

except that it is unspecified whether rounding will be performed between the multiplication and addition steps. Fusion is not guaranteed, even if the target platform supports it. If a fused multiply-add is required, the corresponding llvm.experimental.constrained.fma intrinsic function should be used instead. This never sets errno, just as ‘`llvm.experimental.constrained.fma.*`’.

In addition to the basic floating-point operations for which constrained intrinsics are described above, there are constrained versions of various operations which provide equivalent behavior to a corresponding libm function. These intrinsics allow the precise behavior of these operations with respect to rounding mode and exception behavior to be controlled.

As with the basic constrained floating-point intrinsics, the rounding mode and exception behavior arguments only control the behavior of the optimizer. They do not change the runtime floating-point environment.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.sqrt(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.sqrt`’ intrinsic returns the square root of the specified value, returning the same value as the libm ‘`sqrt`’ functions would, but without setting `errno`.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the nonnegative square root of the specified value. If the value is less than negative zero, a floating-point exception occurs and the return value is architecture specific.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.pow(<type> <op1>, <type> <op2>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.pow`’ intrinsic returns the first argument raised to the (positive or negative) power specified by the second argument.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type. The second argument specifies the power to which the first argument should be raised.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the first value raised to the second power, returning the same values as the libm `pow` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.powi(<type> <op1>, i32 <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.powi`’ intrinsic returns the first argument raised to the (positive or negative) power specified by the second argument. The order of evaluation of multiplications is not defined. When a vector of floating-point type is used, the second argument remains a scalar integer value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type. The second argument is a 32-bit signed integer specifying the power to which the first argument should be raised.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the first value raised to the second power with an unspecified sequence of rounding operations.

##### Syntax:

```
declare <type0>
@llvm.experimental.constrained.ldexp(<type0> <op1>, <type1> <op2>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.ldexp`’ performs the ldexp function.

##### Arguments:
