---
title: "LLVM Language Reference Manual (part 8/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 8/20
---

# LLVM Language Reference Manual

```llvm
%ptr = alloca i32                               ; yields ptr
store i32 3, ptr %ptr                           ; yields void
%val = load i32, ptr %ptr                       ; yields i32:val = i32 3
```

##### Syntax:

```
store [volatile] <ty> <value>, ptr <pointer>[, align <alignment>][, !nontemporal !<nontemp_node>][, !invariant.group !<empty_node>]        ; yields void
store atomic [volatile] <ty> <value>, ptr <pointer> [syncscope("<target-scope>")] <ordering>, align <alignment> [, !invariant.group !<empty_node>] ; yields void
!<nontemp_node> = !{ i32 1 }
!<empty_node> = !{}
```

##### Overview:

The ‘`store`’ instruction is used to write to memory.

##### Arguments:

There are two arguments to the `store` instruction: a value to store and an address at which to store it. The type of the `<pointer>` operand must be a pointer to the first class type of the `<value>` operand. If the `store` is marked as `volatile`, then the optimizer is not allowed to modify the number or order of execution of this `store` with other volatile operations. Only values of first class types of known size (i.e., not containing an opaque structural type) can be stored.

If the `store` is marked as `atomic`, it takes an extra ordering and optional `syncscope("<target-scope>")` argument. The `acquire` and `acq_rel` orderings aren’t valid on `store` instructions. Atomic loads produce defined results when they may see multiple atomic stores. The type of the pointee must be an integer, pointer, floating-point, or vector type whose bit width is a power of two greater than or equal to eight. `align` must be explicitly specified on atomic stores. Note: if the alignment is not greater or equal to the size of the *<value>* type, the atomic operation is likely to require a lock and have poor performance. `!nontemporal` does not have any defined semantics for atomic stores.

The optional constant `align` argument specifies the alignment of the operation (that is, the alignment of the memory address). It is the responsibility of the code emitter to ensure that the alignment information is correct. Overestimating the alignment results in undefined behavior. Underestimating the alignment may produce less efficient code. An alignment of 1 is always safe. The maximum possible alignment is `1 << 32`. An alignment value higher than the size of the stored type does *not* imply (without target specific knowledge) that memory up to the alignment value bytes can be safely loaded without trapping.

The alignment is only optional when parsing textual IR; for in-memory IR, it is always present. An omitted `align` argument means that the operation has the ABI alignment for the target.

The optional `!nontemporal` metadata must reference a single metadata name `<nontemp_node>` corresponding to a metadata node with one `i32` entry of value 1. The existence of the `!nontemporal` metadata on the instruction tells the optimizer and code generator that this load is not expected to be reused in the cache. The code generator may select special instructions to save cache bandwidth, such as the `MOVNT` instruction on x86.

The optional `!invariant.group` metadata must reference a single metadata name `<empty_node>`. See `invariant.group` metadata.

##### Semantics:

The contents of memory are updated to contain `<value>` at the location specified by the `<pointer>` operand. If `<value>` is of scalar type then the number of bytes written does not exceed the minimum number of bytes needed to hold all bits of the type. For example, storing an `i24` writes at most three bytes. When writing a value of a type like `i20` with a size that is not an integral number of bytes, the value will be zero extended to the next larger multiple of the byte size (here `i24`) and then stored. As such, a non-byte-sized store behaves like a `zext` followed by a byte-sized store.

If `<value>` is of aggregate type, padding is filled with undef. If `<pointer>` is not a well-defined value, the behavior is undefined.

##### Example:

```llvm
%ptr = alloca i32                               ; yields ptr
store i32 3, ptr %ptr                           ; yields void
%val = load i32, ptr %ptr                       ; yields i32:val = i32 3
```

##### Syntax:

```
fence [syncscope("<target-scope>")] <ordering>  ; yields void
```

##### Overview:

The ‘`fence`’ instruction is used to introduce happens-before edges between operations.

##### Arguments:

‘`fence`’ instructions take an ordering argument which defines what *synchronizes-with* edges they add. They can only be given `acquire`, `release`, `acq_rel`, and `seq_cst` orderings.

##### Semantics:

A fence A which has (at least) `release` ordering semantics *synchronizes with* a fence B with (at least) `acquire` ordering semantics if and only if there exist atomic operations X and Y, both operating on some atomic object M, such that A is sequenced before X, X modifies M (either directly or through some side effect of a sequence headed by X), Y is sequenced before B, and Y observes M. This provides a *happens-before* dependency between A and B. Rather than an explicit `fence`, one (but not both) of the atomic operations X or Y might provide a `release` or `acquire` (resp.) ordering constraint and still *synchronize-with* the explicit `fence` and establish the *happens-before* edge.

A `fence` which has `seq_cst` ordering, in addition to having both `acquire` and `release` semantics specified above, participates in the global program order of other `seq_cst` operations and/or fences. Furthermore, the global ordering created by a `seq_cst` fence must be compatible with the individual total orders of `monotonic` (or stronger) memory accesses occurring before and after such a fence. The exact semantics of this interaction are somewhat complicated, see the C++ standard’s [atomics.order] section for more details.

A `fence` instruction can also take an optional “syncscope” argument.

##### Example:

```
fence acquire                                        ; yields void
fence syncscope("singlethread") seq_cst              ; yields void
fence syncscope("agent") seq_cst                     ; yields void
```

##### Syntax:

```
cmpxchg [weak] [volatile] ptr <pointer>, <ty> <cmp>, <ty> <new> [syncscope("<target-scope>")] <success ordering> <failure ordering>[, align <alignment>] ; yields  { ty, i1 }
```

##### Overview:

The ‘`cmpxchg`’ instruction is used to atomically modify memory. It loads a value in memory and compares it to a given value. If they are equal, it tries to store a new value into the memory.

##### Arguments:

There are three arguments to the ‘`cmpxchg`’ instruction: an address to operate on, a value to compare to the value currently be at that address, and a new value to place at that address if the compared values are equal. The type of ‘<cmp>’ must be an integer or pointer type whose bit width is a power of two greater than or equal to eight. ‘<cmp>’ and ‘<new>’ must have the same type, and the type of ‘<pointer>’ must be a pointer to that type. If the `cmpxchg` is marked as `volatile`, then the optimizer is not allowed to modify the number or order of execution of this `cmpxchg` with other volatile operations.

The success and failure ordering arguments specify how this `cmpxchg` synchronizes with other atomic operations. Both ordering parameters must be at least `monotonic`, the failure ordering cannot be either `release` or `acq_rel`.

A `cmpxchg` instruction can also take an optional “syncscope” argument.

Note: if the alignment is not greater or equal to the size of the *<value>* type, the atomic operation is likely to require a lock and have poor performance.

The alignment is only optional when parsing textual IR; for in-memory IR, it is always present. If unspecified, the alignment is assumed to be equal to the size of the ‘<value>’ type. Note that this default alignment assumption is different from the alignment used for the load/store instructions when align isn’t specified.

The pointer passed into cmpxchg must have alignment greater than or equal to the size in memory of the operand.

##### Semantics:

The contents of memory at the location specified by the ‘`<pointer>`’ operand is read and compared to ‘`<cmp>`’; if the values are equal, ‘`<new>`’ is written to the location. The original value at the location is returned, together with a flag indicating success (true) or failure (false).

If the cmpxchg operation is marked as `weak` then a spurious failure is permitted: the operation may not write `<new>` even if the comparison matched.

If the cmpxchg operation is strong (the default), the i1 value is 1 if and only if the value loaded equals `cmp`.

A successful `cmpxchg` is a read-modify-write instruction for the purpose of identifying release sequences. A failed `cmpxchg` is equivalent to an atomic load with an ordering parameter determined the second ordering parameter.

##### Example:

```llvm
entry:
  %orig = load atomic i32, ptr %ptr unordered, align 4                      ; yields i32
  br label %loop

loop:
  %cmp = phi i32 [ %orig, %entry ], [%value_loaded, %loop]
  %squared = mul i32 %cmp, %cmp
  %val_success = cmpxchg ptr %ptr, i32 %cmp, i32 %squared acq_rel monotonic ; yields  { i32, i1 }
  %value_loaded = extractvalue { i32, i1 } %val_success, 0
  %success = extractvalue { i32, i1 } %val_success, 1
  br i1 %success, label %done, label %loop

done:
  ...
```

##### Syntax:

```
atomicrmw [volatile] [elementwise] <operation> ptr <pointer>, <ty> <value> [syncscope("<target-scope>")] <ordering>[, align <alignment>]  ; yields ty
```

##### Overview:

The ‘`atomicrmw`’ instruction is used to atomically modify memory.

##### Arguments:

There are three arguments to the ‘`atomicrmw`’ instruction: an operation to apply, an address whose value to modify, an argument to the operation. The operation must be one of the following keywords:

- xchg
- add
- sub
- and
- nand
- or
- xor
- max
- min
- umax
- umin
- fadd
- fsub
- fmax
- fmin
- fmaximum
- fminimum
- fmaximumnum
- fminimumnum
- uinc_wrap
- udec_wrap
- usub_cond
- usub_sat

For all of these operations, the type of ‘<value>’ must be a type whose bit width is a power of two greater than or equal to eight. For add/sub/and/nand/or/xor/max/min/umax/umin/uinc_wrap/udec_wrap/usub_cond/usub_sat, this must be an integer type, or, if the `elementwise` modifier is present, a fixed vector of integer type. For fadd/fsub/fmax/fmin/fmaximum/fminimum/fmaximumnum/fminimumnum, this must be a floating-point or fixed vector of floating-point type. For xchg, this must be an integer type, floating-point type, or pointer type, or, if the `elementwise` modifier is present, a fixed vector of integer type, floating-point type, or pointer type. The type of the ‘<pointer>’ operand must be a pointer to the type of ‘<value>’. If the `atomicrmw` is marked as `volatile`, then the optimizer is not allowed to modify the number or order of execution of this `atomicrmw` with other volatile operations.

Note: if the alignment is not greater or equal to the size of the *<value>* type, the atomic operation is likely to require a lock and have poor performance.

The alignment is only optional when parsing textual IR; for in-memory IR, it is always present. If unspecified, the alignment is assumed to be equal to the size of the ‘<value>’ type. Note that this default alignment assumption is different from the alignment used for the load/store instructions when align isn’t specified.

An `atomicrmw` instruction can also take an optional “syncscope” argument.

If the `elementwise` modifier is present, the instruction has per-element vector atomic semantics. It behaves as if it were expanded into one scalar `atomicrmw` per element, that are not ordered with respect to each other. Without `elementwise`, vector `atomicrmw` keeps whole-value atomic semantics.

##### Semantics:

The contents of memory at the location specified by the ‘`<pointer>`’ operand are atomically read, modified, and written back. The original value at the location is returned. The modification is specified by the operation argument:

- xchg: `*ptr = val`
- add: `*ptr = *ptr + val`
- sub: `*ptr = *ptr - val`
- and: `*ptr = *ptr & val`
- nand: `*ptr = ~(*ptr & val)`
- or: `*ptr = *ptr | val`
- xor: `*ptr = *ptr ^ val`
- max: `*ptr = *ptr > val ? *ptr : val` (using a signed comparison)
- min: `*ptr = *ptr < val ? *ptr : val` (using a signed comparison)
- umax: `*ptr = *ptr > val ? *ptr : val` (using an unsigned comparison)
- umin: `*ptr = *ptr < val ? *ptr : val` (using an unsigned comparison)
- fadd: `*ptr = *ptr + val` (using floating point arithmetic)
- fsub: `*ptr = *ptr - val` (using floating point arithmetic)
- fmax: `*ptr = maxnum(*ptr, val)` (match the *llvm.maxnum.** intrinsic)
- fmin: `*ptr = minnum(*ptr, val)` (match the *llvm.minnum.** intrinsic)
- fmaximum: `*ptr = maximum(*ptr, val)` (match the *llvm.maximum.** intrinsic)
- fminimum: `*ptr = minimum(*ptr, val)` (match the *llvm.minimum.** intrinsic)
- fmaximumnum: `*ptr = maximumnum(*ptr, val)` (match the *llvm.maximumnum.** intrinsic)
- fminimumnum: `*ptr = minimumnum(*ptr, val)` (match the *llvm.minimumnum.** intrinsic)
- uinc_wrap: `*ptr = (*ptr u>= val) ? 0 : (*ptr + 1)` (increment value with wraparound to zero when incremented above input value)
- udec_wrap: `*ptr = ((*ptr == 0) || (*ptr u> val)) ? val : (*ptr - 1)` (decrement with wraparound to input value when decremented below zero).
- usub_cond: `*ptr = (*ptr u>= val) ? *ptr - val : *ptr` (subtract only if no unsigned overflow).
- usub_sat: `*ptr = (*ptr u>= val) ? *ptr - val : 0` (subtract with unsigned clamping to zero).

##### Example:

```llvm
%old = atomicrmw add ptr %ptr, i32 1 acquire                        ; yields i32
```

##### Syntax:

```
<result> = getelementptr <ty>, ptr <ptrval>{, <ty> <idx>}*
<result> = getelementptr inbounds <ty>, ptr <ptrval>{, <ty> <idx>}*
<result> = getelementptr nusw <ty>, ptr <ptrval>{, <ty> <idx>}*
<result> = getelementptr nuw <ty>, ptr <ptrval>{, <ty> <idx>}*
<result> = getelementptr inrange(S,E) <ty>, ptr <ptrval>{, <ty> <idx>}*
<result> = getelementptr <ty>, <N x ptr> <ptrval>, <vector index type> <idx>
```

##### Overview:

The ‘`getelementptr`’ instruction is used to get the address of a subelement of an aggregate data structure. It performs address calculation only and does not access memory. The instruction can also be used to calculate a vector of such addresses.

##### Arguments:

The first argument is always a type used as the basis for the calculations. The second argument is always a pointer or a vector of pointers, and is the base address to start from. The remaining arguments are indices that indicate which of the elements of the aggregate object are indexed. The interpretation of each index is dependent on the type being indexed into. The first index always indexes the pointer value given as the second argument, the second index indexes a value of the type pointed to (not necessarily the value directly pointed to, since the first index can be non-zero), etc. The first type indexed into must be a pointer value, subsequent types can be arrays, vectors, and structs. Note that subsequent types being indexed into can never be pointers, since that would require loading the pointer before continuing calculation.

The type of each index argument depends on the type it is indexing into. When indexing into a (optionally packed) structure, only `i32` integer **constants** are allowed (when using a vector of indices they must all be the **same** `i32` integer constant). When indexing into an array, pointer or vector, integers of any width are allowed, and they are not required to be constant. These integers are treated as signed values where relevant.

For example, let’s consider a C code fragment and how it gets compiled to LLVM:

```c
struct RT {
  char A;
  int B[10][20];
  char C;
};
struct ST {
  int X;
  double Y;
  struct RT Z;
};

int *foo(struct ST *s) {
  return &s[1].Z.B[5][13];
}
```

The LLVM code generated by Clang is approximately:

```llvm
%struct.RT = type { i8, [10 x [20 x i32]], i8 }
%struct.ST = type { i32, double, %struct.RT }

define ptr @foo(ptr %s) {
entry:
  %arrayidx = getelementptr inbounds %struct.ST, ptr %s, i64 1, i32 2, i32 1, i64 5, i64 13
  ret ptr %arrayidx
}
```

##### Semantics:

In the example above, the first index is indexing into the ‘`%struct.ST*`’ type, which is a pointer, yielding a ‘`%struct.ST`’ = ‘`{ i32, double, %struct.RT }`’ type, a structure. The second index indexes into the third element of the structure, yielding a ‘`%struct.RT`’ = ‘`{ i8 , [10 x [20 x i32]], i8 }`’ type, another structure. The third index indexes into the second element of the structure, yielding a ‘`[10 x [20 x i32]]`’ type, an array. The two dimensions of the array are subscripted into, yielding an ‘`i32`’ type. The ‘`getelementptr`’ instruction returns a pointer to this element.

Note that it is perfectly legal to index partially through a structure, returning a pointer to an inner element. Because of this, the LLVM code for the given testcase is equivalent to:

```llvm
define ptr @foo(ptr %s) {
  %t1 = getelementptr %struct.ST, ptr %s, i32 1
  %t2 = getelementptr %struct.ST, ptr %t1, i32 0, i32 2
  %t3 = getelementptr %struct.RT, ptr %t2, i32 0, i32 1
  %t4 = getelementptr [10 x [20 x i32]], ptr %t3, i32 0, i32 5
  %t5 = getelementptr [20 x i32], ptr %t4, i32 0, i32 13
  ret ptr %t5
}
```

The indices are first converted to offsets in the pointer’s index type. If the currently indexed type is a struct type, the struct offset corresponding to the index is sign-extended or truncated to the pointer index type. Otherwise, the index itself is sign-extended or truncated, and then multiplied by the type allocation size (that is, the size rounded up to the ABI alignment) of the currently indexed type.

The offsets are then added to the low bits of the base address up to the index type width, with silently-wrapping two’s complement arithmetic. If the pointer size is larger than the index size, this means that the bits outside the index type width will not be affected.

The result value of the `getelementptr` may be outside the object pointed to by the base pointer. The result value may not necessarily be used to access memory though, even if it happens to point into allocated storage. See the Pointer Aliasing Rules section for more information.

The `getelementptr` instruction may have a number of attributes that impose additional rules. If any of the rules are violated, the result value is a poison value. In cases where the base is a vector of pointers, the attributes apply to each computation element-wise.

For `nusw` (no unsigned signed wrap):

> - If the type of an index is larger than the pointer index type, the truncation to the pointer index type preserves the signed value (`trunc nsw`).
> - The multiplication of an index by the type size does not wrap the pointer index type in a signed sense (`mul nsw`).
> - The successive addition of each offset (without adding the base address) does not wrap the pointer index type in a signed sense (`add nsw`).
> - The successive addition of the current address, truncated to the pointer index type and interpreted as an unsigned number, and each offset, interpreted as a signed number, does not wrap the pointer index type.

For `nuw` (no unsigned wrap):

> - If the type of an index is larger than the pointer index type, the truncation to the pointer index type preserves the unsigned value (`trunc nuw`).
> - The multiplication of an index by the type size does not wrap the pointer index type in an unsigned sense (`mul nuw`).
> - The successive addition of each offset (without adding the base address) does not wrap the pointer index type in an unsigned sense (`add nuw`).
> - The successive addition of the current address, truncated to the pointer index type and interpreted as an unsigned number, and each offset, also interpreted as an unsigned number, does not wrap the pointer index type (`add nuw`).

For `inbounds` all rules of the `nusw` attribute apply. Additionally, if the `getelementptr` has any non-zero indices, the following rules apply:

> - The base pointer has an *in bounds* address of the allocated object that it is based on. This means that it points into that allocated object, or to its end. Note that the object does not have to be live anymore; being in-bounds of a deallocated object is sufficient. If the allocated object can grow, then the relevant size for being *in bounds* is the maximal size the object could have while satisfying the allocated object rules, not its current size.
> - During the successive addition of offsets to the address, the resulting pointer must remain *in bounds* of the allocated object at each step.

Note that `getelementptr` with all-zero indices is always considered to be `inbounds`, even if the base pointer does not point to an allocated object. As a corollary, the only pointer in bounds of the null pointer in the default address space is the null pointer itself.

If `inbounds` is present on a `getelementptr` instruction, the `nusw` attribute will be automatically set as well. For this reason, the `nusw` will also not be printed in textual IR if `inbounds` is already present.

If the `inrange(Start, End)` attribute is present, loading from or storing to any pointer derived from the `getelementptr` has undefined behavior if the load or store would access memory outside the half-open range `[Start, End)` from the `getelementptr` expression result. The result of a pointer comparison or `ptrtoint` (including `ptrtoint`-like operations involving memory) involving a pointer derived from a `getelementptr` with the `inrange` keyword is undefined, with the exception of comparisons in the case where both operands are in the closed range `[Start, End]`. Note that the `inrange` keyword is currently only allowed in constant `getelementptr` expressions.

The getelementptr instruction is often confusing. For some more insight into how it works, see the getelementptr FAQ.

##### Example:

```llvm
%aptr = getelementptr {i32, [12 x i8]}, ptr %saptr, i64 0, i32 1
%vptr = getelementptr {i32, <2 x i8>}, ptr %svptr, i64 0, i32 1, i32 1
%eptr = getelementptr [12 x i8], ptr %aptr, i64 0, i32 1
%iptr = getelementptr [10 x i32], ptr @arr, i16 0, i16 0
```

##### Vector of pointers:

The `getelementptr` returns a vector of pointers, instead of a single address, when one or more of its arguments is a vector. In such cases, all vector arguments should have the same number of elements, and every scalar argument will be effectively broadcast into a vector during address calculation.

```llvm
; All arguments are vectors:
;   A[i] = ptrs[i] + offsets[i]*sizeof(i8)
%A = getelementptr i8, <4 x i8*> %ptrs, <4 x i64> %offsets

; Add the same scalar offset to each pointer of a vector:
;   A[i] = ptrs[i] + offset*sizeof(i8)
%A = getelementptr i8, <4 x ptr> %ptrs, i64 %offset

; Add distinct offsets to the same pointer:
;   A[i] = ptr + offsets[i]*sizeof(i8)
%A = getelementptr i8, ptr %ptr, <4 x i64> %offsets

; In all cases described above the type of the result is <4 x ptr>
```

The two following instructions are equivalent:

```llvm
getelementptr  %struct.ST, <4 x ptr> %s, <4 x i64> %ind1,
  <4 x i32> <i32 2, i32 2, i32 2, i32 2>,
  <4 x i32> <i32 1, i32 1, i32 1, i32 1>,
  <4 x i32> %ind4,
  <4 x i64> <i64 13, i64 13, i64 13, i64 13>

getelementptr  %struct.ST, <4 x ptr> %s, <4 x i64> %ind1,
  i32 2, i32 1, <4 x i32> %ind4, i64 13
```

Let’s look at the C code, where the vector version of `getelementptr` makes sense:

```c
// Let's assume that we vectorize the following loop:
double *A, *B; int *C;
for (int i = 0; i < size; ++i) {
  A[i] = B[C[i]];
}
```

```llvm
; get pointers for 8 elements from array B
%ptrs = getelementptr double, ptr %B, <8 x i32> %C
; load 8 elements from array B into A
%A = call <8 x double> @llvm.masked.gather.v8f64.v8p0f64(
     <8 x ptr> align 8 %ptrs, <8 x i1> %mask, <8 x double> %passthru)
```

The instructions in this category are the conversion instructions (casting) which all take a single operand and a type. They perform various bit conversions on the operand.

##### Syntax:

```
<result> = trunc <ty> <value> to <ty2>             ; yields ty2
<result> = trunc nsw <ty> <value> to <ty2>         ; yields ty2
<result> = trunc nuw <ty> <value> to <ty2>         ; yields ty2
<result> = trunc nuw nsw <ty> <value> to <ty2>     ; yields ty2
```

##### Overview:

The ‘`trunc`’ instruction truncates its operand to the type `ty2`.

##### Arguments:

The ‘`trunc`’ instruction takes a value to trunc, and a type to trunc it to. Both types must be of integer types, or vectors of the same number of integers. The bit size of the `value` must be larger than the bit size of the destination type, `ty2`. Equal sized types are not allowed.

##### Semantics:

The ‘`trunc`’ instruction truncates the high order bits in `value` and converts the remaining bits to `ty2`. Since the source size must be larger than the destination size, `trunc` cannot be a *no-op cast*. It will always truncate bits.

If the `nuw` keyword is present, and any of the truncated bits are non-zero, the result is a poison value. If the `nsw` keyword is present, and any of the truncated bits are not the same as the top bit of the truncation result, the result is a poison value.

##### Example:

```llvm
%X = trunc i32 257 to i8                        ; yields i8:1
%Y = trunc i32 123 to i1                        ; yields i1:true
%Z = trunc i32 122 to i1                        ; yields i1:false
%W = trunc <2 x i16> <i16 8, i16 7> to <2 x i8> ; yields <i8 8, i8 7>
```

##### Syntax:

```
<result> = zext <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`zext`’ instruction zero extends its operand to type `ty2`.

The `nneg` (non-negative) flag, if present, specifies that the operand is non-negative. This property may be used by optimization passes to later convert the `zext` into a `sext`.

##### Arguments:

The ‘`zext`’ instruction takes a value to cast, and a type to cast it to. Both types must be of integer types, or vectors of the same number of integers. The bit size of the `value` must be smaller than the bit size of the destination type, `ty2`.

##### Semantics:

The `zext` fills the high order bits of the `value` with zero bits until it reaches the size of the destination type, `ty2`.

When zero extending from i1, the result will always be either 0 or 1.

If the `nneg` flag is set, and the `zext` argument is negative, the result is a poison value.

##### Example:

```llvm
%X = zext i32 257 to i64              ; yields i64:257
%Y = zext i1 true to i32              ; yields i32:1
%Z = zext <2 x i16> <i16 8, i16 7> to <2 x i32> ; yields <i32 8, i32 7>

%a = zext nneg i8 127 to i16 ; yields i16 127
%b = zext nneg i8 -1 to i16  ; yields i16 poison
```

##### Syntax:

```
<result> = sext <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`sext`’ sign extends `value` to the type `ty2`.

##### Arguments:

The ‘`sext`’ instruction takes a value to cast, and a type to cast it to. Both types must be of integer types, or vectors of the same number of integers. The bit size of the `value` must be smaller than the bit size of the destination type, `ty2`.

##### Semantics:

The ‘`sext`’ instruction performs a sign extension by copying the sign bit (highest order bit) of the `value` until it reaches the bit size of the type `ty2`.

When sign extending from i1, the extension always results in -1 or 0.

##### Example:

```llvm
%X = sext i8  -1 to i16              ; yields i16   :65535
%Y = sext i1 true to i32             ; yields i32:-1
%Z = sext <2 x i16> <i16 8, i16 7> to <2 x i32> ; yields <i32 8, i32 7>
```

##### Syntax:

```
<result> = fptrunc [fast-math flags]* <ty> <value> to <ty2> ; yields ty2
```

##### Overview:

The ‘`fptrunc`’ instruction truncates `value` to type `ty2`.

##### Arguments:

The ‘`fptrunc`’ instruction takes a floating-point value to cast and a floating-point type to cast it to. The size of `value` must be larger than the size of `ty2`. This implies that `fptrunc` cannot be used to make a *no-op cast*.

##### Semantics:

The ‘`fptrunc`’ instruction casts a `value` from a larger floating-point type to a smaller floating-point type. This instruction is assumed to execute in the default floating-point environment.

NaN values follow the usual NaN behaviors, except that _if_ a NaN payload is propagated from the input (“Quieting NaN propagation” or “Unchanged NaN propagation” cases), then the low order bits of the NaN payload which cannot fit in the resulting type are discarded. Note that if discarding the low order bits leads to an all-0 payload, this cannot be represented as a signaling NaN (it would represent an infinity instead), so in that case “Unchanged NaN propagation” is not possible.

This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations.

##### Example:

```llvm
%X = fptrunc double 16777217.0 to float    ; yields float:16777216.0
%Y = fptrunc double 1.0E+300 to half       ; yields half:+infinity
```

##### Syntax:

```
<result> = fpext [fast-math flags]* <ty> <value> to <ty2> ; yields ty2
```

##### Overview:

The ‘`fpext`’ extends a floating-point `value` to a larger floating-point value.

##### Arguments:

The ‘`fpext`’ instruction takes a floating-point `value` to cast, and a floating-point type to cast it to. The source type must be smaller than the destination type.

##### Semantics:

The ‘`fpext`’ instruction extends the `value` from a smaller floating-point type to a larger floating-point type. The `fpext` cannot be used to make a *no-op cast* because it always changes bits. Use `bitcast` to make a *no-op cast* for a floating-point cast.

NaN values follow the usual NaN behaviors, except that _if_ a NaN payload is propagated from the input (“Quieting NaN propagation” or “Unchanged NaN propagation” cases), then it is copied to the high order bits of the resulting payload, and the remaining low order bits are zero.

This instruction can also take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations.

##### Example:

```llvm
%X = fpext float 3.125 to double         ; yields double:3.125000e+00
%Y = fpext double %X to fp128            ; yields fp128:0xL00000000000000004000900000000000
```

##### Syntax:

```
<result> = fptoui <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`fptoui`’ converts a floating-point `value` to its unsigned integer equivalent of type `ty2`.

##### Arguments:

The ‘`fptoui`’ instruction takes a value to cast, which must be a scalar or vector floating-point value, and a type to cast it to `ty2`, which must be an integer type. If `ty` is a vector floating-point type, `ty2` must be a vector integer type with the same number of elements as `ty`

##### Semantics:

The ‘`fptoui`’ instruction converts its floating-point operand into the nearest (rounding towards zero) unsigned integer value. If the value cannot fit in `ty2`, the result is a poison value.

##### Example:

```llvm
%X = fptoui double 123.0 to i32      ; yields i32:123
%Y = fptoui float 1.0E+300 to i1     ; yields undefined:1
%Z = fptoui float 1.04E+17 to i8     ; yields undefined:1
```

##### Syntax:

```
<result> = fptosi <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`fptosi`’ instruction converts floating-point `value` to type `ty2`.

##### Arguments:

The ‘`fptosi`’ instruction takes a value to cast, which must be a scalar or vector floating-point value, and a type to cast it to `ty2`, which must be an integer type. If `ty` is a vector floating-point type, `ty2` must be a vector integer type with the same number of elements as `ty`

##### Semantics:

The ‘`fptosi`’ instruction converts its floating-point operand into the nearest (rounding towards zero) signed integer value. If the value cannot fit in `ty2`, the result is a poison value.

##### Example:

```llvm
%X = fptosi double -123.0 to i32      ; yields i32:-123
%Y = fptosi float 1.0E-247 to i1      ; yields undefined:1
%Z = fptosi float 1.04E+17 to i8      ; yields undefined:1
```

##### Syntax:

```
<result> = uitofp [fast-math flags]* [nneg] <ty> <value> to <ty2> ; yields ty2
```

##### Overview:

The ‘`uitofp`’ instruction regards `value` as an unsigned integer and converts that value to the `ty2` type.

The `nneg` (non-negative) flag, if present, specifies that the operand is non-negative. This property may be used by optimization passes to later convert the `uitofp` into a `sitofp`.

##### Arguments:

The ‘`uitofp`’ instruction takes a value to cast, which must be a scalar or vector integer value, and a type to cast it to `ty2`, which must be an floating-point type. If `ty` is a vector integer type, `ty2` must be a vector floating-point type with the same number of elements as `ty`

##### Semantics:

The ‘`uitofp`’ instruction interprets its operand as an unsigned integer quantity and converts it to the corresponding floating-point value. If the value cannot be exactly represented, it is rounded using the default rounding mode.

If the `nneg` flag is set, and the `uitofp` argument is negative, the result is a poison value.

If the ‘`nsz`’ flag is set and the input value is 0, the sign bit of the result is non-deterministic.

##### Example:

```llvm
%X = uitofp i32 257 to float         ; yields float:257.0
%Y = uitofp i8 -1 to double          ; yields double:255.0

%a = uitofp nneg i32 256 to float    ; yields float:256.0
%b = uitofp nneg i32 -256 to float   ; yields float poison
```

##### Syntax:

```
<result> = sitofp [fast-math flags]* <ty> <value> to <ty2> ; yields ty2
```

##### Overview:

The ‘`sitofp`’ instruction regards `value` as a signed integer and converts that value to the `ty2` type.

##### Arguments:

The ‘`sitofp`’ instruction takes a value to cast, which must be a scalar or vector integer value, and a type to cast it to `ty2`, which must be an floating-point type. If `ty` is a vector integer type, `ty2` must be a vector floating-point type with the same number of elements as `ty`

##### Semantics:

The ‘`sitofp`’ instruction interprets its operand as a signed integer quantity and converts it to the corresponding floating-point value. If the value cannot be exactly represented, it is rounded using the default rounding mode.

If the ‘`nsz`’ flag is set and the input value is 0, the sign bit of the result is non-deterministic.

##### Example:

```llvm
%X = sitofp i32 257 to float         ; yields float:257.0
%Y = sitofp i8 -1 to double          ; yields double:-1.0
```

##### Syntax:

```
<result> = ptrtoint <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`ptrtoint`’ instruction converts the pointer or a vector of pointers `value` to the integer (or vector of integers) type `ty2`.

##### Arguments:

The ‘`ptrtoint`’ instruction takes a `value` to cast, which must be a value of type pointer or a vector of pointers, and a type to cast it to `ty2`, which must be an integer or a vector of integers type.

##### Semantics:

The ‘`ptrtoint`’ instruction converts `value` to integer type `ty2` by interpreting all the pointer representation bits as an integer (equivalent to a `bitcast`) and either truncating or zero extending that value to the size of the integer type. If `value` is smaller than `ty2` then a zero extension is done. If `value` is larger than `ty2` then a truncation is done. If they are the same size, then nothing is done (*no-op cast*) other than a type change. The `ptrtoint` always captures address and provenance of the pointer argument.

##### Example:

```llvm
%X = ptrtoint ptr %P to i8                         ; yields truncation on 32-bit architecture
%Y = ptrtoint ptr %P to i64                        ; yields zero extension on 32-bit architecture
%Z = ptrtoint <4 x ptr> %P to <4 x i64>; yields vector zero extension for a vector of addresses on 32-bit architecture
```

##### Syntax:

```
<result> = ptrtoaddr <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`ptrtoaddr`’ instruction converts the pointer or a vector of pointers `value` to the underlying integer address (or vector of addresses) of type `ty2`. This is different from ptrtoint in that it only operates on the index bits of the pointer and ignores all other bits, and does not capture the provenance of the pointer.

##### Arguments:

The ‘`ptrtoaddr`’ instruction takes a `value` to cast, which must be a value of type pointer or a vector of pointers, and a type to cast it to `ty2`, which must be must be the integer type (or vector of integers) matching the pointer index width of the address space of `ty`.

##### Semantics:

The ‘`ptrtoaddr`’ instruction converts `value` to integer type `ty2` by interpreting the lowest index-width pointer representation bits as an integer. If the address size and the pointer representation size are the same and `value` and `ty2` are the same size, then nothing is done (*no-op cast*) other than a type change.

The `ptrtoaddr` instruction always captures the address but not the provenance of the pointer argument.

##### Example:

This example assumes pointers in address space 1 are 64 bits in size with an address width of 32 bits (`p1:64:64:64:32` datalayout string)

```llvm
%X = ptrtoaddr ptr addrspace(1) %P to i32              ; extracts low 32 bits of pointer
%Y = ptrtoaddr <4 x ptr addrspace(1)> %P to <4 x i32>  ; yields vector of low 32 bits for each pointer
```

##### Syntax:

```
<result> = inttoptr <ty> <value> to <ty2>[, !dereferenceable !<deref_bytes_node>][, !dereferenceable_or_null !<deref_bytes_node>][, !nofree !<empty_node>]            ; yields ty2
```

##### Overview:

The ‘`inttoptr`’ instruction converts an integer `value` to a pointer type, `ty2`.

##### Arguments:

The ‘`inttoptr`’ instruction takes an integer value to cast, and a type to cast it to, which must be a pointer type.

The optional `!dereferenceable` metadata must reference a single metadata name `<deref_bytes_node>` corresponding to a metadata node with one `i64` entry. See `dereferenceable` metadata.

The optional `!dereferenceable_or_null` metadata must reference a single metadata name `<deref_bytes_node>` corresponding to a metadata node with one `i64` entry. See `dereferenceable_or_null` metadata.

The optional `!nofree` metadata must reference a single metadata name `<empty_node>` corresponding to a metadata node with no entries. The existence of the `!nofree` metadata on the instruction tells the optimizer that the memory pointed by the pointer will not be freed after this point.

##### Semantics:

The ‘`inttoptr`’ instruction converts `value` to type `ty2` by applying either a zero extension or a truncation depending on the size of the integer `value`. If `value` is larger than the size of a pointer then a truncation is done. If `value` is smaller than the size of a pointer then a zero extension is done. If they are the same size, nothing is done (*no-op cast*). The behavior is equivalent to a `bitcast`, however, the resulting value is not guaranteed to be dereferenceable (e.g., if the result type is a non-integral pointers).

##### Example:

```llvm
%X = inttoptr i32 255 to ptr           ; yields zero extension on 64-bit architecture
%Y = inttoptr i32 255 to ptr           ; yields no-op on 32-bit architecture
%Z = inttoptr i64 0 to ptr             ; yields truncation on 32-bit architecture
%Z = inttoptr <4 x i32> %G to <4 x ptr>; yields truncation of vector G to four pointers
```

##### Syntax:

```
<result> = bitcast <ty> <value> to <ty2>             ; yields ty2
```

##### Overview:

The ‘`bitcast`’ instruction converts `value` to type `ty2` without changing any bits.

##### Arguments:

The ‘`bitcast`’ instruction takes a value to cast, which must be a non-aggregate first class value, and a type to cast it to, which must also be a non-aggregate first class type. The bit sizes of `value` and the destination type, `ty2`, must be identical. If the source type is a pointer, the destination type must also be a pointer or a byte (vector of bytes) of the same size. This instruction supports bitwise conversion of vectors to integers and to vectors of other types (as long as they have the same size).

##### Semantics:

The ‘`bitcast`’ instruction converts `value` to type `ty2`. It is always a *no-op cast* because no bits change with this conversion. The conversion is done as if the `value` had been stored to memory and read back as type `ty2`. Pointer (or vector of pointers) types may only be converted to other pointer (or vector of pointers) types with the same address space or byte (or vector of bytes) types through this instruction. To convert pointers to other types, use the inttoptr or ptrtoint instructions first.

There is a caveat for bitcasts involving vector types in relation to endianness. For example `bitcast <2 x i8> <value> to i16` puts element zero of the vector in the least significant bits of the i16 for little-endian while element zero ends up in the most significant bits for big-endian.

If `value` is of the byte type:

- If `ty2` is a scalar type: If `ty2` is a byte type, the original bits are unchanged. If `ty2` is a pointer type: If at least one bit of `value` is `poison`, the result is `poison`. If all bits of `value` are from the same pointer and are correctly ordered (there were no pointer bit swaps), the result is that pointer. Otherwise, the result is a pointer with the address given by the integer value of the input, and without provenance. If `ty2` is an integer or floating-point type: If at least one bit of `value` is `poison`, the result is `poison`. Otherwise, the result is the value encoded by the input bits with their provenance stripped without being exposed.
- If `ty2` is a vector type, the input bits get sliced into chunks corresponding to lanes of the output. Each lane is then converted using the rules for scalar types above.

##### Example:

```
%X = bitcast i8 255 to i8         ; yields i8 :-1
%Y = bitcast i32* %x to i16*      ; yields i16*:%x
%Z = bitcast <2 x i32> %V to i64; ; yields i64: %V (depends on endianness)
%Z = bitcast <2 x i32*> %V to <2 x i64*> ; yields <2 x i64*>

; considering %bi to hold an integer and %bp to hold a pointer,
%a = bitcast b64 %bi to i64       ; returns an integer, no-op cast
%b = bitcast b64 %bp to i64       ; reinterprets the pointer as an integer, returning its address without exposing provenance
%c = bitcast b64 %bp to ptr       ; returns a pointer, no-op cast
%d = bitcast b64 %bi to ptr       ; reinterprets the integer as a pointer, returning a pointer with no provenance

%e = bitcast <2 x b32> %v to i64  ; reinterprets the raw bytes as an integer
%f = bitcast <2 x b32> %v to ptr  ; reinterprets the raw bytes as a pointer

%g = bitcast <2 x b32> %v to <4 x i16> ; reinterprets the raw bytes as integers
```

##### Syntax:

```
<result> = addrspacecast <pty> <ptrval> to <pty2>       ; yields pty2
```

##### Overview:

The ‘`addrspacecast`’ instruction converts `ptrval` from `pty` in address space `n` to type `pty2` in address space `m`.

##### Arguments:

The ‘`addrspacecast`’ instruction takes a pointer or vector of pointer value to cast and a pointer type to cast it to, which must have a different address space.

##### Semantics:

The ‘`addrspacecast`’ instruction converts the pointer value `ptrval` to type `pty2`. It can be a *no-op cast* or a complex value modification, depending on the target and the address space pair. Pointer conversions within the same address space must be performed with the `bitcast` instruction. Note that if the address space conversion produces a dereferenceable result then both result and operand refer to the same memory location. The conversion must have no side effects, and must not capture the value of the pointer.

If the source is poison, the result is poison.

If the source is not poison, and both source and destination are integral pointers, and the result pointer is dereferenceable, the cast is assumed to be reversible (i.e., casting the result back to the original address space should yield the original bit pattern).

Which address space casts are supported depends on the target. Unsupported address space casts return poison.

##### Example:

```llvm
%X = addrspacecast ptr %x to ptr addrspace(1)
%Y = addrspacecast ptr addrspace(1) %y to ptr addrspace(2)
%Z = addrspacecast <4 x ptr> %z to <4 x ptr addrspace(3)>
```

The instructions in this category are the “miscellaneous” instructions, which defy better classification.

##### Syntax:

```
<result> = icmp <cond> <ty> <op1>, <op2>   ; yields i1 or <N x i1>:result
<result> = icmp samesign <cond> <ty> <op1>, <op2>   ; yields i1 or <N x i1>:result
```

##### Overview:

The ‘`icmp`’ instruction returns a boolean value or a vector of boolean values based on comparison of its two integer, integer vector, pointer, or pointer vector operands.

##### Arguments:

The ‘`icmp`’ instruction takes three operands. The first operand is the condition code indicating the kind of comparison to perform. It is not a value, just a keyword. The possible condition codes are:

1. `eq`: equal
2. `ne`: not equal
3. `ugt`: unsigned greater than
4. `uge`: unsigned greater or equal
5. `ult`: unsigned less than
6. `ule`: unsigned less or equal
7. `sgt`: signed greater than
8. `sge`: signed greater or equal
9. `slt`: signed less than
10. `sle`: signed less or equal

The remaining two arguments must be integer or pointer or integer vector typed. They must also be identical types.

##### Semantics:

The ‘`icmp`’ compares `op1` and `op2` according to the condition code given as `cond`. The comparison performed always yields either an i1 or vector of `i1` result, as follows:

1. `eq`: yields `true` if the operands are equal, `false` otherwise. No sign interpretation is necessary or performed.
2. `ne`: yields `true` if the operands are unequal, `false` otherwise. No sign interpretation is necessary or performed.
3. `ugt`: interprets the operands as unsigned values and yields `true` if `op1` is greater than `op2`.
4. `uge`: interprets the operands as unsigned values and yields `true` if `op1` is greater than or equal to `op2`.
5. `ult`: interprets the operands as unsigned values and yields `true` if `op1` is less than `op2`.
6. `ule`: interprets the operands as unsigned values and yields `true` if `op1` is less than or equal to `op2`.
7. `sgt`: interprets the operands as signed values and yields `true` if `op1` is greater than `op2`.
8. `sge`: interprets the operands as signed values and yields `true` if `op1` is greater than or equal to `op2`.
9. `slt`: interprets the operands as signed values and yields `true` if `op1` is less than `op2`.
10. `sle`: interprets the operands as signed values and yields `true` if `op1` is less than or equal to `op2`.

If the operands are pointer typed, the address bits of the pointers are compared as if they were integers. Non-address bits or external state are not compared. That is, `icmp` on pointers is equivalent to `icmp` on the `ptrtoaddr` of the pointers.

If the operands are integer vectors, then they are compared element by element. The result is an `i1` vector with the same number of elements as the values being compared. Otherwise, the result is an `i1`.
