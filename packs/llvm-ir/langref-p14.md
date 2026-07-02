---
title: "LLVM Language Reference Manual (part 14/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 14/20
---

# LLVM Language Reference Manual

The element of the result mask is active when loading from %addrA then storing to %addrB is safe and doesn’t result in a write-after-read hazard, meaning that:

- (addrB - addrA) <= 0 (guarantees that all lanes are loaded before any stores), or
- elementSize * lane < (addrB - addrA) (guarantees that this lane is loaded before the store to the same address)

##### Examples:

```llvm
%addrA = ptrtoaddr ptr %ptrA to i64
%addrB = ptrtoaddr ptr %ptrB to i64
%loop.dependence.mask = call <4 x i1> @llvm.loop.dependence.war.mask.v4i1.i64(i64 %addrA, i64 %addrB, i64 4)
%vecA = call <4 x i32> @llvm.masked.load.v4i32.p0(ptr align 4 %ptrA, <4 x i1> %loop.dependence.mask, <4 x i32> poison)
[...]
call @llvm.masked.store.v4i32.p0(<4 x i32> %vecA, ptr align 4 %ptrB, <4 x i1> %loop.dependence.mask)

; For the above example, consider the following cases:
;
; 1. addrA >= addrB
;
;   load =      <0,1,2,3>     ; uint32_t load = array[i+2];
;  store =  <0,1,2,3>         ; array[i] = store;
;
; This results in an all-true mask, as the load always occurs before the
; store, so it does not depend on any values to be stored.
;
; 2. addrB - addrA = 2 * elementSize:
;
;   load =  <0,1,2,3>         ; uint32_t load = array[i];
;  store =      <0,1,2,3>     ; array[i+2] = store;
;
; This results in a mask with the first two lanes active. This is because
; we can only read two lanes before we would read values that have yet to
; be written.
;
; 3. addrB - addrA = 4 * elementSize
;
;   load =  <0,1,2,3>         ; uint32_t load = array[i];
;  store =          <0,1,2,3> ; array[i+4] = store;
;
; This results in an all-true mask, as the store is a full vector ahead
; of the load, so all values will be written before any lane is read.
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <4 x i1> @llvm.loop.dependence.raw.mask.v4i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
declare <8 x i1> @llvm.loop.dependence.raw.mask.v8i1.i32(i32 %addrA, i32 %addrB, i32 immarg %elementSize)
declare <16 x i1> @llvm.loop.dependence.raw.mask.v16i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
declare <vscale x 16 x i1> @llvm.loop.dependence.raw.mask.nxv16i1.i64(i64 %addrA, i64 %addrB, i64 immarg %elementSize)
```

##### Overview:

Given a vector store to address %addrA followed by a vector load from address %addrB, this instruction generates a mask where an active lane indicates that the read-after-write sequence can be performed safely for that lane, without a read-after-write hazard or a store-to-load forwarding hazard being introduced.

A read-after-write hazard occurs when a read-after-write sequence for a given lane in a vector ends up being executed as a write-after-read sequence due to the aliasing of pointers.

A store-to-load forwarding hazard occurs when a vector store writes to an address that partially overlaps with the address of a subsequent vector load, meaning that the vector load can’t be performed until the vector store is complete.

##### Arguments:

The first two arguments are integers and the last argument is an immediate. The result is a vector with the i1 element type.

##### Semantics:

`%elementSize` is the size of the accessed elements in bytes. The intrinsic returns `poison` if the distance between `%addrA` and `%addrB` is smaller than `VF * %elementsize` and either `%addrA + VF * %elementSize` or `%addrB + VF * %elementSize` wrap.

The element of the result mask is active when storing to %addrA then loading from %addrB is safe and doesn’t result in aliasing, meaning that:

- elementSize * lane < abs(addrB - addrA) (guarantees that the store of this lane occurs before loading from this address), or
- addrA == addrB (doesn’t introduce any new hazards that weren’t in the scalar code)

##### Examples:

```llvm
%addrA = ptrtoaddr ptr %ptrA to i64
%addrB = ptrtoaddr ptr %ptrB to i64
%loop.dependence.mask = call <4 x i1> @llvm.loop.dependence.raw.mask.v4i1.i64(i64 %addrA, i64 %addrB, i64 4)
call @llvm.masked.store.v4i32.p0(<4 x i32> %vecA, ptr align 4 %ptrA, <4 x i1> %loop.dependence.mask)
[...]
%vecB = call <4 x i32> @llvm.masked.load.v4i32.p0(ptr align 4 %ptrB, <4 x i1> %loop.dependence.mask, <4 x i32> poison)

; For the above example, consider the following cases:
;
; 1. addrA == addrB
;
;  store = <0,1,2,3>       ; array[i] = store;
;   load = <0,1,2,3>       ; uint32_t load = array[i];
;
; This results in a all-true mask. There is no conflict.
;
; 2. addrB - addrA = 2 * elementSize
;
;  store =  <0,1,2,3>      ; array[i] = store;
;   load =      <0,1,2,3>  ; uint32_t load = array[i+2];
;
; This results in a mask with the first two lanes active. In this case,
; only two lanes can be written without overwriting values yet to be read.
;
; 3. addrB - addrA = -2 * elementSize
;
;  store =      <0,1,2,3>  ; array[i+2] = store;
;   load =  <0,1,2,3>      ; uint32_t load = array[i];
;
; This also results in a mask with the first two lanes active. This is
; because if any more lanes were active the load would be dependent on the
; completion of the store.
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.experimental.cttz.elts` on any vector of integer elements, both fixed width and scalable.

```
declare i8 @llvm.experimental.cttz.elts.i8.v8i1(<8 x i1> <src>, i1 <is_zero_poison>)
```

##### Overview:

The ‘`llvm.experimental.cttz.elts`’ intrinsic counts the number of trailing zero elements of a vector.

##### Arguments:

The first argument is the vector to be counted. This argument must be a vector with integer element type. The return type must also be an integer type which is wide enough to hold the maximum number of elements of the source vector. The result is a poison value if the return type is not wide enough for the number of elements in the input vector.

The second argument is a constant flag that indicates whether the intrinsic returns a valid result if the first argument is all zero. If the first argument is all zero and the second argument is true, the result is poison.

##### Semantics:

The ‘`llvm.experimental.cttz.elts`’ intrinsic counts the trailing (least significant) zero elements in a vector. If `src == 0` the result is the number of elements in the input vector.

##### Syntax:

This is an overloaded intrinsic.

```
declare i32 @llvm.experimental.get.vector.length.i32(i32 %cnt, i32 immarg %vf, i1 immarg %scalable)
declare i32 @llvm.experimental.get.vector.length.i64(i64 %cnt, i32 immarg %vf, i1 immarg %scalable)
```

##### Overview:

The ‘`llvm.experimental.get.vector.length.*`’ intrinsics take a number of elements to process and returns how many of the elements can be processed with the requested vectorization factor.

##### Arguments:

The first argument is an unsigned value of any scalar integer type and specifies the total number of elements to be processed. The second argument is an i32 immediate for the vectorization factor. The third argument indicates if the vectorization factor should be multiplied by vscale.

##### Semantics:

Returns a non-negative i32 value (explicit vector length) that is unknown at compile time and depends on the hardware specification. If the result value does not fit in the result type, then the result is a poison value.

This intrinsic is intended to be used by loop vectorization with VP intrinsics in order to get the number of elements to process on each loop iteration. The result should be used to decrease the count for the next iteration until the count reaches zero.

Let `%max_lanes` be the number of lanes in the type described by `%vf` and `%scalable`, here are the constraints on the returned value:

- If `%cnt` equals to 0, returns 0.
- The returned value is always less than or equal to `%max_lanes`.
- The returned value is always greater than or equal to `ceil(%cnt / ceil(%cnt / %max_lanes))`, if `%cnt` is non-zero.
- The returned values are monotonically non-increasing in each loop iteration. That is, the returned value of an iteration is at least as large as that of any later iteration.

Note that it has the following implications:

- For a loop that uses this intrinsic, the number of iterations is equal to `ceil(%C / %max_lanes)` where `%C` is the initial `%cnt` value.
- If `%cnt` is non-zero, the return value is non-zero as well.
- If `%cnt` is less than or equal to `%max_lanes`, the return value is equal to `%cnt`.

These intrinsics are overloaded.

These intrinsics represent histogram-like operations; that is, updating values in memory that may not be contiguous, and where multiple elements within a single vector may be updating the same value in memory.

The update operation must be specified as part of the intrinsic name. For a simple histogram like the following the `add` operation would be used.

```c
void simple_histogram(int *restrict buckets, unsigned *indices, int N, int inc) {
  for (int i = 0; i < N; ++i)
    buckets[indices[i]] += inc;
}
```

More update operation types may be added in the future.

```
declare void @llvm.experimental.vector.histogram.add.v8p0.i32(<8 x ptr> %ptrs, i32 %inc, <8 x i1> %mask)
declare void @llvm.experimental.vector.histogram.add.nxv2p0.i64(<vscale x 2 x ptr> %ptrs, i64 %inc, <vscale x 2 x i1> %mask)
declare void @llvm.experimental.vector.histogram.uadd.sat.v8p0.i32(<8 x ptr> %ptrs, i32 %inc, <8 x i1> %mask)
declare void @llvm.experimental.vector.histogram.umax.v8p0.i32(<8 x ptr> %ptrs, i32 %val, <8 x i1> %mask)
declare void @llvm.experimental.vector.histogram.umin.v8p0.i32(<8 x ptr> %ptrs, i32 %val, <8 x i1> %mask)
```

##### Arguments:

The first argument is a vector of pointers to the memory locations to be updated. The second argument is a scalar used to update the value from memory; it must match the type of value to be updated. The final argument is a mask value to exclude locations from being modified.

##### Semantics:

The ‘`llvm.experimental.vector.histogram.*`’ intrinsics are used to perform updates on potentially overlapping values in memory. The intrinsics represent the following sequence of operations:

1. Gather load from the `ptrs` operand, with element type matching that of the `inc` operand.
2. Update of the values loaded from memory. In the case of the `add` update operation, this means:
  1. Perform a cross-vector histogram operation on the `ptrs` operand.
  2. Multiply the result by the `inc` operand.
  3. Add the result to the values loaded from memory
3. Scatter the result of the update operation to the memory locations from the `ptrs` operand.

The `mask` operand will apply to at least the gather and scatter operations.

This is an overloaded intrinsic.

```
declare i32 @llvm.experimental.vector.extract.last.active.v4i32(<4 x i32> %data, <4 x i1> %mask, i32 %passthru)
declare i16 @llvm.experimental.vector.extract.last.active.nxv8i16(<vscale x 8 x i16> %data, <vscale x 8 x i1> %mask, i16 %passthru)
```

##### Arguments:

The first argument is the data vector to extract a lane from. The second is a mask vector controlling the extraction. The third argument is a passthru value.

The two input vectors must have the same number of elements, and the type of the passthru value must match that of the elements of the data vector.

##### Semantics:

The ‘`llvm.experimental.vector.extract.last.active`’ intrinsic will extract an element from the data vector at the index matching the highest active lane of the mask vector. If no mask lanes are active then the passthru value is returned instead.

LLVM provides an intrinsic for compressing data within a vector based on a selection mask. Semantically, this is similar to llvm.masked.compressstore but with weaker assumptions and without storing the results to memory, i.e., the data remains in the vector.

##### Syntax:

This is an overloaded intrinsic. A number of scalar values of integer, floating point or pointer data type are collected from an input vector and placed adjacently within the result vector. A mask defines which elements to collect from the vector. The remaining lanes are filled with values from `passthru`.

```llvm
declare <8 x i32> @llvm.experimental.vector.compress.v8i32(<8 x i32> <value>, <8 x i1> <mask>, <8 x i32> <passthru>)
declare <16 x float> @llvm.experimental.vector.compress.v16f32(<16 x float> <value>, <16 x i1> <mask>, <16 x float> undef)
```

##### Overview:

Selects elements from input vector `value` according to the `mask`. All selected elements are written into adjacent lanes in the result vector, from lower to higher. The mask holds an entry for each vector lane, and is used to select elements to be kept. If a `passthru` vector is given, all remaining lanes are filled with the corresponding lane’s value from `passthru`. The main difference to llvm.masked.compressstore is that the we do not need to guard against memory access for unselected lanes. This allows for branchless code and better optimization for all targets that do not support or have inefficient instructions of the explicit semantics of llvm.masked.compressstore but still have some form of compress operations. The result vector can be written with a similar effect, as all the selected values are at the lower positions of the vector, but without requiring branches to avoid writes where the mask is `false`.

##### Arguments:

The first operand is the input vector, from which elements are selected. The second operand is the mask, a vector of boolean values. The third operand is the passthru vector, from which elements are filled into remaining lanes. The mask and the input vector must have the same number of vector elements. The input and passthru vectors must have the same type.

##### Semantics:

The `llvm.experimental.vector.compress` intrinsic compresses data within a vector. It collects elements from possibly non-adjacent lanes of a vector and places them contiguously in the result vector based on a selection mask, filling the remaining lanes with values from `passthru`. This intrinsic performs the logic of the following C++ example. All values in `out` after the last selected one are undefined if `passthru` is undefined. If all entries in the `mask` are 0, the `out` vector is `passthru`. If any element of the mask is poison, all elements of the result are poison. Otherwise, if any element of the mask is undef, all elements of the result are undef. If `passthru` is undefined, the number of valid lanes is equal to the number of `true` entries in the mask, i.e., all lanes >= number-of-selected-values are undefined.

```cpp
// Consecutively place selected values in a vector.
using VecT __attribute__((vector_size(N))) = int;
VecT compress(VecT vec, VecT mask, VecT passthru) {
  VecT out;
  int idx = 0;
  for (int i = 0; i < N / sizeof(int); ++i) {
    out[idx] = vec[i];
    idx += static_cast<bool>(mask[i]);
  }
  for (; idx < N / sizeof(int); ++idx) {
    out[idx] = passthru[idx];
  }
  return out;
}
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <<n> x i1> @llvm.experimental.vector.match(<<n> x <ty>> %op1, <<m> x <ty>> %op2, <<n> x i1> %mask)
declare <vscale x <n> x i1> @llvm.experimental.vector.match(<vscale x <n> x <ty>> %op1, <<m> x <ty>> %op2, <vscale x <n> x i1> %mask)
```

##### Overview:

Find active elements of the first argument matching any elements of the second.

##### Arguments:

The first argument is the search vector, the second argument the vector of elements we are searching for (i.e., for which we consider a match successful), and the third argument is a mask that controls which elements of the first argument are active. The first two arguments must be vectors of matching integer element types. The first and third arguments and the result type must have matching element counts (fixed or scalable). The second argument must be a fixed vector, but its length may be different from the remaining arguments.

##### Semantics:

The ‘`llvm.experimental.vector.match`’ intrinsic compares each active element in the first argument against the elements of the second argument, placing `1` in the corresponding element of the output vector if any equality comparison is successful, and `0` otherwise. Inactive elements in the mask are set to `0` in the output.

Operations on matrixes requiring shape information (like number of rows/columns or the memory layout) can be expressed using the matrix intrinsics. These intrinsics require matrix dimensions to be passed as immediate arguments, and matrixes are passed and returned as vectors. This means that for a `R` x `C` matrix, element `i` of column `j` is at index `j * R + i` in the corresponding vector, with indices starting at 0. Currently column-major layout is assumed. The intrinsics support both integer and floating point matrixes.

##### Syntax:

This is an overloaded intrinsic.

```
declare vectorty @llvm.matrix.transpose.*(vectorty %In, i32 <Rows>, i32 <Cols>)
```

##### Overview:

The ‘`llvm.matrix.transpose.*`’ intrinsics treat `%In` as a `<Rows> x <Cols>` matrix and return the transposed matrix in the result vector.

##### Arguments:

The first argument `%In` is a vector that corresponds to a `<Rows> x <Cols>` matrix. Thus, arguments `<Rows>` and `<Cols>` correspond to the number of rows and columns, respectively, and must be positive, constant integers. The returned vector must have `<Rows> * <Cols>` elements, and have the same float or integer element type as `%In`.

##### Syntax:

This is an overloaded intrinsic.

```
declare vectorty @llvm.matrix.multiply.*(vectorty %A, vectorty %B, i32 <OuterRows>, i32 <Inner>, i32 <OuterColumns>)
```

##### Overview:

The ‘`llvm.matrix.multiply.*`’ intrinsics treat `%A` as a `<OuterRows> x <Inner>` matrix, `%B` as a `<Inner> x <OuterColumns>` matrix, and multiplies them. The result matrix is returned in the result vector.

##### Arguments:

The first vector argument `%A` corresponds to a matrix with `<OuterRows> * <Inner>` elements, and the second argument `%B` to a matrix with `<Inner> * <OuterColumns>` elements. Arguments `<OuterRows>`, `<Inner>` and `<OuterColumns>` must be positive, constant integers. The returned vector must have `<OuterRows> * <OuterColumns>` elements. Vectors `%A`, `%B`, and the returned vector all have the same float or integer element type.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.matrix.column.major.load` to load any vector type with a stride of any bitwidth up to 64.

```
declare <4 x i32> @llvm.matrix.column.major.load.v4i32.i64(
    ptrty %Ptr, i64 %Stride, i1 <IsVolatile>, i32 <Rows>, i32 <Cols>)
declare <9 x double> @llvm.matrix.column.major.load.v9f64.i32(
    ptrty %Ptr, i32 %Stride, i1 <IsVolatile>, i32 <Rows>, i32 <Cols>)
```

##### Overview:

The ‘`llvm.matrix.column.major.load.*`’ intrinsics load a `<Rows> x <Cols>` matrix using a stride of `%Stride` to compute the start address of the different columns. This allows for convenient loading of sub matrixes. Independent of `%Stride`’s bitwidth, the offset is computed using the target daya layout’s pointer index type. If `<IsVolatile>` is true, the intrinsic is considered a volatile memory access. The result matrix is returned in the result vector. If the `%Ptr` argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

##### Arguments:

The first argument `%Ptr` is a pointer type to the returned vector type, and corresponds to the start address to load from. The second argument `%Stride` is a positive integer for which `%Stride >= <Rows>`. `%Stride` is used to compute the column memory addresses. I.e., for a column `C`, its start memory addresses is calculated with `%Ptr + C * %Stride`. The third Argument `<IsVolatile>` is a boolean value. The fourth and fifth arguments, `<Rows>` and `<Cols>`, correspond to the number of rows and columns, respectively, and must be positive, constant integers. The returned vector must have `<Rows> * <Cols>` elements.

The align parameter attribute can be provided for the `%Ptr` arguments.

##### Syntax:

This is an overloaded intrinsic. `llvm.matrix.column.major.store` to store any vector type with a stride of any bitwidth up to 64.

```
declare void @llvm.matrix.column.major.store.v4i32.i64(
    <4 x i32> %In, ptrty %Ptr, i64 %Stride, i1 <IsVolatile>, i32 <Rows>,
    i32 <Cols>)
declare void @llvm.matrix.column.major.store.v9f64.i32(
    <9 x double> %In, ptrty %Ptr, i32 %Stride, i1 <IsVolatile>, i32
    <Rows>, i32 <Cols>)
```

##### Overview:

The ‘`llvm.matrix.column.major.store.*`’ intrinsics store the `<Rows> x <Cols>` matrix in `%In` to memory using a stride of `%Stride` between columns. Independent of `%Stride`’s bitwidth, the offset is computed using the target daya layout’s pointer index type. If `<IsVolatile>` is true, the intrinsic is considered a volatile memory access.

If the `%Ptr` argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

##### Arguments:

The first argument `%In` is a vector that corresponds to a `<Rows> x <Cols>` matrix to be stored to memory. The second argument `%Ptr` is a pointer to the vector type of `%In`, and is the start address of the matrix in memory. The third argument `%Stride` is a positive integer for which `%Stride >= <Rows>`. `%Stride` is used to compute the column memory addresses. I.e., for a column `C`, its start memory addresses is calculated with `%Ptr + C * %Stride`. The fourth argument `<IsVolatile>` is a boolean value. The arguments `<Rows>` and `<Cols>` correspond to the number of rows and columns, respectively, and must be positive, constant integers.

The align parameter attribute can be provided for the `%Ptr` arguments.

The `fptoui` and `fptosi` instructions return a poison value if the rounded-towards-zero value is not representable by the result type. These intrinsics provide an alternative conversion, which will saturate towards the smallest and largest representable integer values instead.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fptoui.sat` on any floating-point argument type and any integer result type, or vectors thereof. Not all targets may support all types, however.

```
declare i32 @llvm.fptoui.sat.i32.f32(float %f)
declare i19 @llvm.fptoui.sat.i19.f64(double %f)
declare <4 x i100> @llvm.fptoui.sat.v4i100.v4f128(<4 x fp128> %f)
```

##### Overview:

This intrinsic converts the argument into an unsigned integer using saturating semantics.

##### Arguments:

The argument may be any floating-point or vector of floating-point type. The return value may be any integer or vector of integer type. The number of vector elements in argument and return must be the same.

##### Semantics:

The conversion to integer is performed subject to the following rules:

- If the argument is any NaN, zero is returned.
- If the argument is smaller than zero (this includes negative infinity), zero is returned.
- If the argument is larger than the largest representable unsigned integer of the result type (this includes positive infinity), the largest representable unsigned integer is returned.
- Otherwise, the result of rounding the argument towards zero is returned.

##### Example:

```
%a = call i8 @llvm.fptoui.sat.i8.f32(float 123.875)            ; yields i8: 123
%b = call i8 @llvm.fptoui.sat.i8.f32(float -5.75)              ; yields i8:   0
%c = call i8 @llvm.fptoui.sat.i8.f32(float 377.0)              ; yields i8: 255
%d = call i8 @llvm.fptoui.sat.i8.f32(float 0xFFF8000000000000) ; yields i8:   0
```

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.fptosi.sat` on any floating-point argument type and any integer result type, or vectors thereof. Not all targets may support all types, however.

```
declare i32 @llvm.fptosi.sat.i32.f32(float %f)
declare i19 @llvm.fptosi.sat.i19.f64(double %f)
declare <4 x i100> @llvm.fptosi.sat.v4i100.v4f128(<4 x fp128> %f)
```

##### Overview:

This intrinsic converts the argument into a signed integer using saturating semantics.

##### Arguments:

The argument may be any floating-point or vector of floating-point type. The return value may be any integer or vector of integer type. The number of vector elements in argument and return must be the same.

##### Semantics:

The conversion to integer is performed subject to the following rules:

- If the argument is any NaN, zero is returned.
- If the argument is smaller than the smallest representable signed integer of the result type (this includes negative infinity), the smallest representable signed integer is returned.
- If the argument is larger than the largest representable signed integer of the result type (this includes positive infinity), the largest representable signed integer is returned.
- Otherwise, the result of rounding the argument towards zero is returned.

##### Example:

```
%a = call i8 @llvm.fptosi.sat.i8.f32(float 23.875)             ; yields i8:   23
%b = call i8 @llvm.fptosi.sat.i8.f32(float -130.75)            ; yields i8: -128
%c = call i8 @llvm.fptosi.sat.i8.f32(float 999.0)              ; yields i8:  127
%d = call i8 @llvm.fptosi.sat.i8.f32(float 0xFFF8000000000000) ; yields i8:    0
```

This class of intrinsics is designed for floating-point conversions that do not fall into other categories. For example conversions with specified rounding mode or mini-float conversions.

##### Syntax:

```
declare <ty2>
@llvm.fptrunc.round(<type> <value>, metadata <rounding mode>)
```

##### Overview:

The ‘`llvm.fptrunc.round`’ intrinsic truncates floating-point `value` to type `ty2` with a specified rounding mode.

##### Arguments:

The ‘`llvm.fptrunc.round`’ intrinsic takes a floating-point value to cast and a floating-point type to cast it to. This argument must be larger in size than the result.

The second argument specifies the rounding mode as described in the constrained intrinsics section. For this intrinsic, the “round.dynamic” mode is not supported.

##### Semantics:

The ‘`llvm.fptrunc.round`’ intrinsic casts a `value` from a larger floating-point type to a smaller floating-point type. This intrinsic is assumed to execute in the default floating-point environment *except* for the rounding mode. This intrinsic is not supported on all targets. Some targets may not support all rounding modes.

##### Syntax:

```
declare <iNxM> @llvm.convert.to.arbitrary.fp.<iNxM>.<fNxM>(
    <fNxM> <value>, metadata <interpretation>,
    metadata <rounding mode>, i1 <saturation>)
```

##### Overview:

The `llvm.convert.to.arbitrary.fp` intrinsic converts a native LLVM floating-point value to an arbitrary FP format, returning the result as an integer containing the arbitrary FP bits. This intrinsic is overloaded on both its return type and first argument.

##### Arguments:

**`value`**

The native LLVM floating-point value to convert (e.g., `half`, `float`, `double`).

**`interpretation`**

A metadata string describing the target arbitrary FP format. Supported format names include:

- FP8 formats: `"Float8E5M2"`, `"Float8E5M2FNUZ"`, `"Float8E4M3"`, `"Float8E4M3FN"`, `"Float8E4M3FNUZ"`, `"Float8E4M3B11FNUZ"`, `"Float8E3M4"`, `"Float8E8M0FNU"`
- FP6 formats: `"Float6E3M2FN"`, `"Float6E2M3FN"`
- FP4 formats: `"Float4E2M1FN"`

**`rounding mode`**

A metadata string specifying the rounding mode. The permitted strings match those accepted by `llvm.fptrunc.round` (for example, `"round.tonearest"` or `"round.towardzero"`).

The rounding mode is only consulted when `value` is not exactly representable in the target format. If the value is exactly representable, all rounding modes produce the same result.

**`saturation`**

A compile-time constant boolean value (`i1`). This parameter controls how overflow is handled when values exceed the representable finite range of the target format:

- When `true`: overflowing values are clamped to the minimum or maximum representable finite value (saturating to the largest negative finite value or largest positive finite value).
- When `false`: overflowing values are converted to infinity (preserving sign of the original value) if the target format supports infinity, or return a poison value if infinity is not supported by the target format.

This parameter must be an immediate constant.

##### Semantics:

The intrinsic converts the native LLVM floating-point value to the arbitrary FP format specified by `interpretation`, applying the requested rounding mode and saturation behavior. The conversion is performed in two steps: first, the value is rounded according to the specified rounding mode to fit the target format’s precision; then, if the rounded result exceeds the target format’s representable range, saturation is applied according to the `saturation` parameter. The result is returned as an integer (e.g., `i8` for FP8, `i6` for FP6) containing the encoded arbitrary FP bits.

**Handling of special values:**

- **NaN**: NaN values follow LLVM’s standard NaN rules. When the target format supports NaN, the NaN representation is preserved (quiet NaNs remain quiet, signaling NaNs remain signaling). The exact NaN payload may be truncated or extended to fit the target format’s payload size. If the target format does not support NaN, the intrinsic returns a poison value.
- **Infinity and Overflow**: If the input is +/-Inf or a finite value that exceeds the representable range:
  - When `saturation` is `false` and the target format supports infinity, the result is +/-Inf (preserving the sign).
  - When `saturation` is `false` and the target format does not support infinity (e.g., formats with “FN” suffix), the intrinsic returns a poison value.
  - When `saturation` is `true`, the value is clamped to the maximum/minimum representable finite value.

For FP6/FP4 interpretations, producers are expected to use `saturation` = `true`; using `saturation` = `false` and generating NaN/Inf/overflowing values results in a poison value.

##### Example:

```
; Convert half to FP8 E4M3 format
%fp8bits = call i8 @llvm.convert.to.arbitrary.fp.i8.f16(
    half %value, metadata !"Float8E4M3",
    metadata !"round.tonearest", i1 false)

; Convert vector of float to FP8 E5M2 with saturation
%vec_fp8 = call <4 x i8> @llvm.convert.to.arbitrary.fp.v4i8.v4f32(
    <4 x float> %values, metadata !"Float8E5M2",
    metadata !"round.towardzero", i1 true)
```

##### Syntax:

```
declare <fNxM> @llvm.convert.from.arbitrary.fp.<fNxM>.<iNxM>(
    <iNxM> <value>, metadata <interpretation>)
```

##### Overview:

The `llvm.convert.from.arbitrary.fp` intrinsic converts an integer containing arbitrary FP bits to a native LLVM floating-point value. This intrinsic is overloaded on both its return type and first argument.

##### Arguments:

**`value`**

An integer value containing the arbitrary FP bits (e.g., `i8` for FP8, `i6` for FP6).

**`interpretation`**

A metadata string describing the source arbitrary FP format. Supported format names include:

- FP8 formats: `"Float8E5M2"`, `"Float8E5M2FNUZ"`, `"Float8E4M3"`, `"Float8E4M3FN"`, `"Float8E4M3FNUZ"`, `"Float8E4M3B11FNUZ"`, `"Float8E3M4"`, `"Float8E8M0FNU"`
- FP6 formats: `"Float6E3M2FN"`, `"Float6E2M3FN"`
- FP4 formats: `"Float4E2M1FN"`

##### Semantics:

The intrinsic interprets the integer value as arbitrary FP bits according to `interpretation`, then converts to the native LLVM floating-point result type.

Conversions from arbitrary FP formats to native LLVM floating-point types are widening conversions (e.g., FP8 to FP16 or FP32), which are exact and require no rounding. Normal finite values are converted exactly. NaN values follow LLVM’s standard NaN rules; the NaN representation is preserved (quiet NaNs remain quiet, signaling NaNs remain signaling), and the NaN payload may be truncated or extended to fit the target format’s payload size. Infinity values are preserved as infinity. If a value exceeds the representable range of the target type (for example, converting `Float8E8M0FNU` with large exponents to `half`), the result is converted to infinity with the appropriate sign.

##### Example:

```
; Convert FP8 E4M3 bits to half
%half_val = call half @llvm.convert.from.arbitrary.fp.f16.i8(
    i8 %fp8bits, metadata !"Float8E4M3")

; Convert vector of FP8 E5M2 bits to float
%vec_float = call <4 x float> @llvm.convert.from.arbitrary.fp.v4f32.v4i8(
    <4 x i8> %fp8_values, metadata !"Float8E5M2")
```

The LLVM convergence intrinsics for controlling the semantics of `convergent` operations, which all start with the `llvm.experimental.convergence.` prefix, are described in the Convergent Operation Semantics document.

The LLVM debugger intrinsics (which all start with `llvm.dbg.` prefix), are described in the LLVM Source Level Debugging document.

The LLVM exception handling intrinsics (which all start with `llvm.eh.` prefix), are described in the LLVM Exception Handling document.

The LLVM pointer authentication intrinsics (which all start with `llvm.ptrauth.` prefix), are described in the Pointer Authentication document.

These intrinsics make it possible to excise one parameter, marked with the nest attribute, from a function. The result is a callable function pointer lacking the nest parameter - the caller does not need to provide a value for it. Instead, the value to use is stored in advance in a “trampoline”, a block of memory usually allocated on the stack, which also contains code to splice the nest value into the argument list. This is used to implement the GCC nested function address extension.

For example, if the function is `i32 f(ptr nest %c, i32 %x, i32 %y)` then the resulting function pointer has signature `i32 (i32, i32)`. It can be created as follows:

```llvm
%tramp = alloca [10 x i8], align 4 ; size and alignment only correct for X86
call ptr @llvm.init.trampoline(ptr %tramp, ptr @f, ptr %nval)
%fp = call ptr @llvm.adjust.trampoline(ptr %tramp)
```

The call `%val = call i32 %fp(i32 %x, i32 %y)` is then equivalent to `%val = call i32 %f(ptr %nval, i32 %x, i32 %y)`.

##### Syntax:

```
declare void @llvm.init.trampoline(ptr <tramp>, ptr <func>, ptr <nval>)
```

##### Overview:

This fills the memory pointed to by `tramp` with executable code, turning it into a trampoline.

##### Arguments:

The `llvm.init.trampoline` intrinsic takes three arguments, all pointers. The `tramp` argument must point to a sufficiently large and sufficiently aligned block of memory; this memory is written to by the intrinsic. Note that the size and the alignment are target-specific - LLVM currently provides no portable way of determining them, so a front-end that generates this intrinsic needs to have some target-specific knowledge.

The `func` argument must be a constant (potentially bitcasted) pointer to a function declaration or definition, since the calling convention may affect the content of the trampoline that is created.

##### Semantics:

The block of memory pointed to by `tramp` is filled with target dependent code, turning it into a function. Then `tramp` needs to be passed to llvm.adjust.trampoline to get a pointer which can be bitcast (to a new function) and called. The new function’s signature is the same as that of `func` with any arguments marked with the `nest` attribute removed. At most one such `nest` argument is allowed, and it must be of pointer type. Calling the new function is equivalent to calling `func` with the same argument list, but with `nval` used for the missing `nest` argument. If, after calling `llvm.init.trampoline`, the memory pointed to by `tramp` is modified, then the effect of any later call to the returned function pointer is undefined.

##### Syntax:

```
declare ptr @llvm.adjust.trampoline(ptr <tramp>)
```

##### Overview:

This performs any required machine-specific adjustment to the address of a trampoline (passed as `tramp`).

##### Arguments:

`tramp` must point to a block of memory which already has trampoline code filled in by a previous call to llvm.init.trampoline.

##### Semantics:

On some architectures the address of the code to be executed needs to be different than the address where the trampoline is actually stored. This intrinsic returns the executable address corresponding to `tramp` after performing the required machine-specific adjustments. The pointer returned can then be bitcast and executed.

VP intrinsics are intended for predicated SIMD/vector code. A typical VP operation takes a vector mask and an explicit vector length parameter as in:

```
<W x T> llvm.vp.<opcode>.*(<W x T> %x, <W x T> %y, <W x i1> %mask, i32 %evl)
```

The vector mask parameter (%mask) always has a vector of *i1* type, for example *<32 x i1>*. The explicit vector length parameter always has the type *i32* and is an unsigned integer value. The explicit vector length parameter (%evl) is in the range:

```
0 <= %evl <= W,  where W is the number of vector elements
```

Note that for scalable vector types `W` is the runtime length of the vector.

The VP intrinsic has undefined behavior if `%evl > W`. The explicit vector length (%evl) creates a mask, %EVLmask, with all elements `0 <= i < %evl` set to True, and all other lanes `%evl <= i < W` to False. A new mask %M is calculated with an element-wise AND from %mask and %EVLmask:

```
M = %mask AND %EVLmask
```

A vector operation `<opcode>` on vectors `A` and `B` calculates:

```
A <opcode> B =  {  A[i] <opcode> B[i]   M[i] = True, and
                {  undef otherwise
```

Some targets, such as AVX512, do not support the %evl parameter in hardware. The use of an effective %evl is discouraged for those targets. The function `TargetTransformInfo::hasActiveVectorLength()` returns true when the target has native support for %evl.

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.select.v16i32 (<16 x i1> <condition>, <16 x i32> <on_true>, <16 x i32> <on_false>, i32 <evl>)
declare <vscale x 4 x i64>  @llvm.vp.select.nxv4i64 (<vscale x 4 x i1> <condition>, <vscale x 4 x i64> <on_true>, <vscale x 4 x i64> <on_false>, i32 <evl>)
```

##### Overview:

The ‘`llvm.vp.select`’ intrinsic is used to choose one value based on a condition vector, without IR-level branching.

##### Arguments:

The first argument is a vector of `i1` and indicates the condition. The second argument is the value that is selected where the condition vector is true. The third argument is the value that is selected where the condition vector is false. The vectors must be of the same size. The fourth argument is the explicit vector length.

1. The optional `fast-math flags` marker indicates that the select has one or more fast-math flags. These are optimization hints to enable otherwise unsafe floating-point optimizations. Fast-math flags are only valid for selects that return supported floating-point types.

##### Semantics:

The intrinsic selects lanes from the second and third argument depending on a condition vector.

All result lanes at positions greater or equal than `%evl` are undefined. For all lanes below `%evl` where the condition vector is true the lane is taken from the second argument. Otherwise, the lane is taken from the third argument.

##### Example:

```llvm
%r = call <4 x i32> @llvm.vp.select.v4i32(<4 x i1> %cond, <4 x i32> %on_true, <4 x i32> %on_false, i32 %evl)

;;; Expansion.
;; Any result is legal on lanes at and above %evl.
%also.r = select <4 x i1> %cond, <4 x i32> %on_true, <4 x i32> %on_false
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.merge.v16i32 (<16 x i1> <condition>, <16 x i32> <on_true>, <16 x i32> <on_false>, i32 <pivot>)
declare <vscale x 4 x i64>  @llvm.vp.merge.nxv4i64 (<vscale x 4 x i1> <condition>, <vscale x 4 x i64> <on_true>, <vscale x 4 x i64> <on_false>, i32 <pivot>)
```

##### Overview:

The ‘`llvm.vp.merge`’ intrinsic is used to choose one value based on a condition vector and an index argument, without IR-level branching.

##### Arguments:

The first argument is a vector of `i1` and indicates the condition. The second argument is the value that is merged where the condition vector is true. The third argument is the value that is selected where the condition vector is false or the lane position is greater equal than the pivot. The fourth argument is the pivot.

1. The optional `fast-math flags` marker indicates that the merge has one or more fast-math flags. These are optimization hints to enable otherwise unsafe floating-point optimizations. Fast-math flags are only valid for merges that return supported floating-point types.

##### Semantics:

The intrinsic selects lanes from the second and third argument depending on a condition vector and pivot value.

For all lanes where the condition vector is true and the lane position is less than `%pivot` the lane is taken from the second argument. Otherwise, the lane is taken from the third argument.

##### Example:

```llvm
%r = call <4 x i32> @llvm.vp.merge.v4i32(<4 x i1> %cond, <4 x i32> %on_true, <4 x i32> %on_false, i32 %pivot)

;;; Expansion.
;; Lanes at and above %pivot are taken from %on_false
%atfirst = insertelement <4 x i32> poison, i32 %pivot, i32 0
%splat = shufflevector <4 x i32> %atfirst, <4 x i32> poison, <4 x i32> zeroinitializer
%pivotmask = icmp ult <4 x i32> <i32 0, i32 1, i32 2, i32 3>, <4 x i32> %splat
%mergemask = and <4 x i1> %cond, <4 x i1> %pivotmask
%also.r = select <4 x i1> %mergemask, <4 x i32> %on_true, <4 x i32> %on_false
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.add.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.add.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.add.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer addition of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.add`’ intrinsic performs integer addition (add) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.add.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = add <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.sub.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.sub.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.sub.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer subtraction of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sub`’ intrinsic performs integer subtraction (sub) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.sub.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = sub <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.mul.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.mul.nxv46i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.mul.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated integer multiplication of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.mul`’ intrinsic performs integer multiplication (mul) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.mul.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = mul <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.sdiv.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.sdiv.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.sdiv.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated, signed division of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.sdiv`’ intrinsic performs signed division (sdiv) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.sdiv.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = sdiv <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.

```
declare <16 x i32>  @llvm.vp.udiv.v16i32 (<16 x i32> <left_op>, <16 x i32> <right_op>, <16 x i1> <mask>, i32 <vector_length>)
declare <vscale x 4 x i32>  @llvm.vp.udiv.nxv4i32 (<vscale x 4 x i32> <left_op>, <vscale x 4 x i32> <right_op>, <vscale x 4 x i1> <mask>, i32 <vector_length>)
declare <256 x i64>  @llvm.vp.udiv.v256i64 (<256 x i64> <left_op>, <256 x i64> <right_op>, <256 x i1> <mask>, i32 <vector_length>)
```

##### Overview:

Predicated, unsigned division of two vectors of integers.

##### Arguments:

The first two arguments and the result have the same vector of integer type. The third argument is the vector mask and has the same number of elements as the result vector type. The fourth argument is the explicit vector length of the operation.

##### Semantics:

The ‘`llvm.vp.udiv`’ intrinsic performs unsigned division (udiv) of the first and second vector arguments on each enabled lane. The result on disabled lanes is a poison value.

##### Examples:

```llvm
%r = call <4 x i32> @llvm.vp.udiv.v4i32(<4 x i32> %a, <4 x i32> %b, <4 x i1> %mask, i32 %evl)
;; For all lanes below %evl, %r is lane-wise equivalent to %also.r

%t = udiv <4 x i32> %a, %b
%also.r = select <4 x i1> %mask, <4 x i32> %t, <4 x i32> poison
```

##### Syntax:

This is an overloaded intrinsic.
