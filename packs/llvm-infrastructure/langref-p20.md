---
title: "LLVM Language Reference Manual (part 20/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 20/20
---

# LLVM Language Reference Manual

```
declare {ptr, i1} @llvm.type.checked.load.relative(ptr %ptr, i32 %offset, metadata %type) nounwind memory(argmem: read)
```

##### Overview:

The `llvm.type.checked.load.relative` intrinsic loads a relative pointer to a function from a virtual table pointer using metadata. Otherwise, its semantic is identical to the `llvm.type.checked.load` intrinsic.

A relative pointer is a pointer to an offset. This is the offset between the destination pointer and the original pointer. The address of the destination pointer is obtained by loading this offset and adding it to the original pointer. This calculation is the same as that of the `llvm.load.relative` intrinsic.

##### Syntax:

```
declare <type>
@llvm.arithmetic.fence(<type> <op>)
```

##### Overview:

The purpose of the `llvm.arithmetic.fence` intrinsic is to prevent the optimizer from performing fast-math optimizations, particularly reassociation, between the argument and the expression that contains the argument. It can be used to preserve the parentheses in the source language.

##### Arguments:

The `llvm.arithmetic.fence` intrinsic takes only one argument. The argument and the return value are floating-point numbers, or vector floating-point numbers, of the same type.

##### Semantics:

This intrinsic returns the value of its operand. The optimizer can optimize the argument, but the optimizer cannot hoist any component of the operand to the containing context, and the optimizer cannot move the calculation of any expression in the containing context into the operand.

##### Syntax:

```
declare void @llvm.donothing() nounwind memory(none)
```

##### Overview:

The `llvm.donothing` intrinsic doesn’t perform any operation. It’s one of only three intrinsics (besides `llvm.experimental.patchpoint` and `llvm.experimental.gc.statepoint`) that can be called with an invoke instruction.

##### Arguments:

None.

##### Semantics:

This intrinsic does nothing, and it’s removed by optimizers and ignored by codegen.

##### Syntax:

```
declare type @llvm.experimental.deoptimize(...) [ "deopt"(...) ]
```

##### Overview:

This intrinsic, together with deoptimization operand bundles, allow frontends to express transfer of control and frame-local state from the currently executing (typically more specialized, hence faster) version of a function into another (typically more generic, hence slower) version.

In languages with a fully integrated managed runtime like Java and JavaScript this intrinsic can be used to implement “uncommon trap” or “side exit” like functionality. In unmanaged languages like C and C++, this intrinsic can be used to represent the slow paths of specialized functions.

##### Arguments:

The intrinsic takes an arbitrary number of arguments, whose meaning is decided by the lowering strategy.

##### Semantics:

The `@llvm.experimental.deoptimize` intrinsic executes an attached deoptimization continuation (denoted using a deoptimization operand bundle) and returns the value returned by the deoptimization continuation. Defining the semantic properties of the continuation itself is out of scope of the language reference – as far as LLVM is concerned, the deoptimization continuation can invoke arbitrary side effects, including reading from and writing to the entire heap.

Deoptimization continuations expressed using `"deopt"` operand bundles always continue execution to the end of the physical frame containing them, so all calls to `@llvm.experimental.deoptimize` must be in “tail position”:

> - `@llvm.experimental.deoptimize` cannot be invoked.
> - The call must immediately precede a ret instruction.
> - The `ret` instruction must return the value produced by the `@llvm.experimental.deoptimize` call if there is one, or void.

Note that the above restrictions imply that the return type for a call to `@llvm.experimental.deoptimize` will match the return type of its immediate caller.

The inliner composes the `"deopt"` continuations of the caller into the `"deopt"` continuations present in the inlinee, and also updates calls to this intrinsic to return directly from the frame of the function it inlined into.

All declarations of `@llvm.experimental.deoptimize` must share the same calling convention.

##### Lowering:

Calls to `@llvm.experimental.deoptimize` are lowered to calls to the symbol `__llvm_deoptimize` (it is the frontend’s responsibility to ensure that this symbol is defined). The call arguments to `@llvm.experimental.deoptimize` are lowered as if they were formal arguments of the specified types, and not as varargs.

##### Syntax:

```
declare void @llvm.experimental.guard(i1, ...) [ "deopt"(...) ]
```

##### Overview:

This intrinsic, together with deoptimization operand bundles, allows frontends to express guards or checks on optimistic assumptions made during compilation. The semantics of `@llvm.experimental.guard` is defined in terms of `@llvm.experimental.deoptimize` – its body is defined to be equivalent to:

```
define void @llvm.experimental.guard(i1 %pred, <args...>) {
  %realPred = and i1 %pred, undef
  br i1 %realPred, label %continue, label %leave [, !make.implicit !{}]

leave:
  call void @llvm.experimental.deoptimize(<args...>) [ "deopt"() ]
  ret void

continue:
  ret void
}
```

with the optional `[, !make.implicit !{}]` present if and only if it is present on the call site. For more details on `!make.implicit`, see FaultMaps and implicit checks.

In words, `@llvm.experimental.guard` executes the attached `"deopt"` continuation if (but **not** only if) its first argument is `false`. Since the optimizer is allowed to replace the `undef` with an arbitrary value, it can optimize guard to fail “spuriously”, i.e., without the original condition being false (hence the “not only if”); and this allows for “check widening” type optimizations.

`@llvm.experimental.guard` cannot be invoked.

After `@llvm.experimental.guard` was first added, a more general formulation was found in `@llvm.experimental.widenable.condition`. Support for `@llvm.experimental.guard` is slowly being rephrased in terms of this alternate.

##### Syntax:

```
declare i1 @llvm.experimental.widenable.condition()
```

##### Overview:

This intrinsic represents a “widenable condition” which is boolean expressions with the following property: whether this expression is *true* or *false*, the program is correct and well-defined.

Together with deoptimization operand bundles, `@llvm.experimental.widenable.condition` allows frontends to express guards or checks on optimistic assumptions made during compilation and represent them as branch instructions on special conditions.

While this may appear similar in semantics to *undef*, it is very different in that an invocation produces a particular, singular value. It is also intended to be lowered late, and remain available for specific optimizations and transforms that can benefit from its special properties.

##### Arguments:

None.

##### Semantics:

The intrinsic `@llvm.experimental.widenable.condition()` returns either *true* or *false*. For each evaluation of a call to this intrinsic, the program must be valid and correct both if it returns *true* and if it returns *false*. This allows transformation passes to replace evaluations of this intrinsic with either value whenever one is beneficial.

When used in a branch condition, it allows us to choose between two alternative correct solutions for the same problem, like in example below:

```
  %cond = call i1 @llvm.experimental.widenable.condition()
  br i1 %cond, label %fast_path, label %slow_path

fast_path:
  ; Apply memory-consuming but fast solution for a task.

slow_path:
  ; Cheap in memory but slow solution.
```

Whether the result of intrinsic’s call is *true* or *false*, it should be correct to pick either solution. We can switch between them by replacing the result of `@llvm.experimental.widenable.condition` with different *i1* expressions.

This is how it can be used to represent guards as widenable branches:

```
block:
  ; Unguarded instructions
  call void @llvm.experimental.guard(i1 %cond, <args...>) ["deopt"(<deopt_args...>)]
  ; Guarded instructions
```

Can be expressed in an alternative equivalent form of explicit branch using `@llvm.experimental.widenable.condition`:

```
block:
  ; Unguarded instructions
  %widenable_condition = call i1 @llvm.experimental.widenable.condition()
  %guard_condition = and i1 %cond, %widenable_condition
  br i1 %guard_condition, label %guarded, label %deopt

guarded:
  ; Guarded instructions

deopt:
  call type @llvm.experimental.deoptimize(<args...>) [ "deopt"(<deopt_args...>) ]
```

So the block *guarded* is only reachable when *%cond* is *true*, and it should be valid to go to the block *deopt* whenever *%cond* is *true* or *false*.

`@llvm.experimental.widenable.condition` will never throw, thus it cannot be invoked.

##### Guard widening:

When `@llvm.experimental.widenable.condition()` is used in condition of a guard represented as explicit branch, it is legal to widen the guard’s condition with any additional conditions.

Guard widening looks like replacement of

```
%widenable_cond = call i1 @llvm.experimental.widenable.condition()
%guard_cond = and i1 %cond, %widenable_cond
br i1 %guard_cond, label %guarded, label %deopt
```

with

```
%widenable_cond = call i1 @llvm.experimental.widenable.condition()
%new_cond = and i1 %any_other_cond, %widenable_cond
%new_guard_cond = and i1 %cond, %new_cond
br i1 %new_guard_cond, label %guarded, label %deopt
```

for this branch. Here *%any_other_cond* is an arbitrarily chosen well-defined *i1* value. By making guard widening, we may impose stricter conditions on *guarded* block and bail to the deopt when the new condition is not met.

##### Lowering:

Default lowering strategy is replacing the result of call of `@llvm.experimental.widenable.condition` with constant *true*. However it is always correct to replace it with any other *i1* value. Any pass can freely do it if it can benefit from non-default lowering.

##### Syntax:

```
declare i1 @llvm.allow.ubsan.check(i8 immarg %kind)
```

##### Overview:

This intrinsic returns `true` if and only if the compiler opted to enable the ubsan check in the current basic block.

Rules to allow ubsan checks are not part of the intrinsic declaration, and controlled by compiler options.

This intrinsic is the ubsan specific version of `@llvm.allow.runtime.check()`.

##### Arguments:

An integer describing the kind of ubsan check guarded by the intrinsic.

##### Semantics:

The intrinsic `@llvm.allow.ubsan.check()` returns either `true` or `false`, depending on compiler options.

For each evaluation of a call to this intrinsic, the program must be valid and correct both if it returns `true` and if it returns `false`.

When used in a branch condition, it selects one of the two paths:

- *true`*: Executes the UBSan check and reports any failures.
- *false*: Bypasses the check, assuming it always succeeds.

Example:

```
  %allow = call i1 @llvm.allow.ubsan.check(i8 5)
  %not.allow = xor i1 %allow, true
  %cond = or i1 %ubcheck, %not.allow
  br i1 %cond, label %cont, label %trap

cont:
  ; Proceed

trap:
  call void @llvm.ubsantrap(i8 5)
  unreachable
```

##### Syntax:

```
declare i1 @llvm.allow.runtime.check(metadata %kind)
```

##### Overview:

This intrinsic returns `true` if and only if the compiler opted to enable runtime checks in the current basic block.

Rules to allow runtime checks are not part of the intrinsic declaration, and controlled by compiler options.

This intrinsic is non-ubsan specific version of `@llvm.allow.ubsan.check()`.

##### Arguments:

A string identifying the kind of runtime check guarded by the intrinsic. The string can be used to control rules to allow checks.

##### Semantics:

The intrinsic `@llvm.allow.runtime.check()` returns either `true` or `false`, depending on compiler options.

For each evaluation of a call to this intrinsic, the program must be valid and correct both if it returns `true` and if it returns `false`.

When used in a branch condition, it allows us to choose between two alternative correct solutions for the same problem.

If the intrinsic is evaluated as `true`, program should execute a guarded check. If the intrinsic is evaluated as `false`, the program should avoid any unnecessary checks.

Example:

```
  %allow = call i1 @llvm.allow.runtime.check(metadata !"my_check")
  br i1 %allow, label %fast_path, label %slow_path

fast_path:
  ; Omit diagnostics.

slow_path:
  ; Additional diagnostics.
```

##### Syntax:

```
declare ptr @llvm.load.relative.iN(ptr %ptr, iN %offset) nounwind memory(argmem: read)
```

##### Overview:

This intrinsic loads a 32-bit value from the address `%ptr + %offset`, adds `%ptr` to that value and returns it. The constant folder specifically recognizes the form of this intrinsic and the constant initializers it may load from; if a loaded constant initializer is known to have the form `i32 trunc(x - %ptr)`, the intrinsic call is folded to `x`.

LLVM provides that the calculation of such a constant initializer will not overflow at link time under the medium code model if `x` is an `unnamed_addr` function. However, it does not provide this guarantee for a constant initializer folded into a function body. This intrinsic can be used to avoid the possibility of overflows when loading from such a constant.

##### Syntax:

```
declare void @llvm.sideeffect() inaccessiblememonly nounwind willreturn
```

##### Overview:

The `llvm.sideeffect` intrinsic doesn’t perform any operation. Optimizers treat it as having side effects, so it can be inserted into a loop to indicate that the loop shouldn’t be assumed to terminate (which could potentially lead to the loop being optimized away entirely), even if it’s an infinite loop with no other side effects.

##### Arguments:

None.

##### Semantics:

This intrinsic actually does nothing, but optimizers must assume that it has externally observable side effects.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.is.constant` with any argument type.

```
declare i1 @llvm.is.constant.i32(i32 %operand) nounwind memory(none)
declare i1 @llvm.is.constant.f32(float %operand) nounwind memory(none)
declare i1 @llvm.is.constant.TYPENAME(TYPE %operand) nounwind memory(none)
```

##### Overview:

The ‘`llvm.is.constant`’ intrinsic will return true if the argument is known to be a manifest compile-time constant. It is guaranteed to fold to either true or false before generating machine code.

##### Semantics:

This intrinsic generates no code. If its argument is known to be a manifest compile-time constant value, then the intrinsic will be converted to a constant true value. Otherwise, it will be converted to a constant false value.

In particular, note that if the argument is a constant expression which refers to a global (the address of which _is_ a constant, but not manifest during the compile), then the intrinsic evaluates to false.

The result also intentionally depends on the result of optimization passes – e.g., the result can change depending on whether a function gets inlined or not. A function’s parameters are obviously not constant. However, a call like `llvm.is.constant.i32(i32 %param)` *can* return true after the function is inlined, if the value passed to the function parameter was a constant.

##### Syntax:

```
declare ptrty llvm.ptrmask(ptrty %ptr, intty %mask) speculatable memory(none)
```

##### Arguments:

The first argument is a pointer or vector of pointers. The second argument is an integer or vector of integers with the same bit width as the index type size of the first argument.

##### Overview:

The `llvm.ptrmask` intrinsic masks out bits of the pointer according to a mask. This allows stripping data from tagged pointers without converting them to an integer (ptrtoint/inttoptr). As a consequence, we can preserve more information to facilitate alias analysis and underlying-object detection.

##### Semantics:

The result of `ptrmask(%ptr, %mask)` is equivalent to the following expansion, where `iPtrIdx` is the index type size of the pointer:

```
%intptr = ptrtoint ptr %ptr to iPtrIdx ; this may truncate
%masked = and iPtrIdx %intptr, %mask
%diff = sub iPtrIdx %masked, %intptr
%result = getelementptr i8, ptr %ptr, iPtrIdx %diff
```

If the pointer index type size is smaller than the pointer type size, this implies that pointer bits beyond the index size are not affected by this intrinsic. For integral pointers, it behaves as if the mask were extended with 1 bits to the pointer type size.

Both the returned pointer(s) and the first argument are based on the same underlying object (for more information on the *based on* terminology see the pointer aliasing rules).

The intrinsic only captures the pointer argument through the return value.

##### Syntax:

```
declare ptr @llvm.threadlocal.address(ptr) nounwind willreturn memory(none)
```

##### Arguments:

The *llvm.threadlocal.address* intrinsic requires a global value argument (a global variable or alias) that is thread local.

##### Semantics:

The address of a thread local global is not a constant, since it depends on the calling thread. The *llvm.threadlocal.address* intrinsic returns the address of the given thread local global in the calling thread.

##### Syntax:

```
declare i32 llvm.vscale.i32()
declare i64 llvm.vscale.i64()
```

##### Overview:

The `llvm.vscale` intrinsic returns the value for `vscale` in scalable vectors such as `<vscale x 16 x i8>`.

##### Semantics:

`vscale` is a positive power-of-two integer that is constant throughout program execution, but is unknown at compile time. If the result value does not fit in the result type, then the result is a poison value.

##### Syntax:

```
declare void @llvm.fake.use(...)
```

##### Overview:

The `llvm.fake.use` intrinsic is a no-op. It takes a single value as an operand and is treated as a use of that operand, to force the optimizer to preserve that value prior to the fake use. This is used for extending the lifetimes of variables, where this intrinsic placed at the end of a variable’s scope helps prevent that variable from being optimized out.

##### Arguments:

The `llvm.fake.use` intrinsic takes one argument, which may be any function-local SSA value. Note that the signature is variadic so that the intrinsic can take any type of argument, but passing more than one argument will result in an error.

##### Semantics:

This intrinsic does nothing, but optimizers must consider it a use of its single operand and should try to preserve the intrinsic and its position in the function.

##### Syntax:

```
declare void @llvm.reloc.none(metadata !<name_str>)
```

##### Overview:

The `llvm.reloc.none` intrinsic emits a no-op relocation against a given operand symbol. This can bring the symbol definition into the link without emitting any code or data to the binary for that purpose.

##### Arguments:

The `llvm.reloc.none` intrinsic takes the symbol as a metadata string argument.

##### Semantics:

This intrinsic emits a no-op relocation for the symbol at the location of the intrinsic call.

LLVM provides experimental intrinsics to support runtime patching mechanisms commonly desired in dynamic language JITs. These intrinsics are described in Stack maps and patch points in LLVM.

These intrinsics are similar to the standard library memory intrinsics except that they perform memory transfer as a sequence of atomic memory accesses.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memcpy.element.unordered.atomic` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memcpy.element.unordered.atomic.p0.p0.i32(ptr <dest>,
                                                             ptr <src>,
                                                             i32 <len>,
                                                             i32 <element_size>)
declare void @llvm.memcpy.element.unordered.atomic.p0.p0.i64(ptr <dest>,
                                                             ptr <src>,
                                                             i64 <len>,
                                                             i32 <element_size>)
```

##### Overview:

The ‘`llvm.memcpy.element.unordered.atomic.*`’ intrinsic is a specialization of the ‘`llvm.memcpy.*`’ intrinsic. It differs in that the `dest` and `src` are treated as arrays with elements that are exactly `element_size` bytes, and the copy between buffers uses a sequence of unordered atomic load/store operations that are a positive integer multiple of the `element_size` in size.

##### Arguments:

The first three arguments are the same as they are in the @llvm.memcpy intrinsic, with the added constraint that `len` is required to be a positive integer multiple of the `element_size`. If `len` is not a positive integer multiple of `element_size`, then the behavior of the intrinsic is undefined.

`element_size` must be a compile-time constant positive power of two no greater than target-specific atomic access size limit.

For each of the input pointers `align` parameter attribute must be specified. It must be a power of two no less than the `element_size`. Caller guarantees that both the source and destination pointers are aligned to that boundary.

##### Semantics:

The ‘`llvm.memcpy.element.unordered.atomic.*`’ intrinsic copies `len` bytes of memory from the source location to the destination location. These locations are not allowed to overlap. The memory copy is performed as a sequence of load/store operations where each access is guaranteed to be a multiple of `element_size` bytes wide and aligned at an `element_size` boundary.

The order of the copy is unspecified. The same value may be read from the source buffer many times, but only one write is issued to the destination buffer per element. It is well defined to have concurrent reads and writes to both source and destination provided those reads and writes are unordered atomic when specified.

This intrinsic does not provide any additional ordering guarantees over those provided by a set of unordered loads from the source location and stores to the destination.

##### Lowering:

In the most general case call to the ‘`llvm.memcpy.element.unordered.atomic.*`’ is lowered to a call to the symbol `__llvm_memcpy_element_unordered_atomic_*`. Where ‘*’ is replaced with an actual element size. See RewriteStatepointsForGC intrinsic lowering for details on GC specific lowering.

Optimizer is allowed to inline memory copy when it’s profitable to do so.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memmove.element.unordered.atomic` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memmove.element.unordered.atomic.p0.p0.i32(ptr <dest>,
                                                              ptr <src>,
                                                              i32 <len>,
                                                              i32 <element_size>)
declare void @llvm.memmove.element.unordered.atomic.p0.p0.i64(ptr <dest>,
                                                              ptr <src>,
                                                              i64 <len>,
                                                              i32 <element_size>)
```

##### Overview:

The ‘`llvm.memmove.element.unordered.atomic.*`’ intrinsic is a specialization of the ‘`llvm.memmove.*`’ intrinsic. It differs in that the `dest` and `src` are treated as arrays with elements that are exactly `element_size` bytes, and the copy between buffers uses a sequence of unordered atomic load/store operations that are a positive integer multiple of the `element_size` in size.

##### Arguments:

The first three arguments are the same as they are in the @llvm.memmove intrinsic, with the added constraint that `len` is required to be a positive integer multiple of the `element_size`. If `len` is not a positive integer multiple of `element_size`, then the behavior of the intrinsic is undefined.

`element_size` must be a compile-time constant positive power of two no greater than a target-specific atomic access size limit.

For each of the input pointers the `align` parameter attribute must be specified. It must be a power of two no less than the `element_size`. Caller guarantees that both the source and destination pointers are aligned to that boundary.

##### Semantics:

The ‘`llvm.memmove.element.unordered.atomic.*`’ intrinsic copies `len` bytes of memory from the source location to the destination location. These locations are allowed to overlap. The memory copy is performed as a sequence of load/store operations where each access is guaranteed to be a multiple of `element_size` bytes wide and aligned at an `element_size` boundary.

The order of the copy is unspecified. The same value may be read from the source buffer many times, but only one write is issued to the destination buffer per element. It is well defined to have concurrent reads and writes to both source and destination provided those reads and writes are unordered atomic when specified.

This intrinsic does not provide any additional ordering guarantees over those provided by a set of unordered loads from the source location and stores to the destination.

##### Lowering:

In the most general case call to the ‘`llvm.memmove.element.unordered.atomic.*`’ is lowered to a call to the symbol `__llvm_memmove_element_unordered_atomic_*`. Where ‘*’ is replaced with an actual element size. See RewriteStatepointsForGC intrinsic lowering for details on GC specific lowering.

The optimizer is allowed to inline the memory copy when it’s profitable to do so.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memset.element.unordered.atomic` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memset.element.unordered.atomic.p0.i32(ptr <dest>,
                                                          i8 <value>,
                                                          i32 <len>,
                                                          i32 <element_size>)
declare void @llvm.memset.element.unordered.atomic.p0.i64(ptr <dest>,
                                                          i8 <value>,
                                                          i64 <len>,
                                                          i32 <element_size>)
```

##### Overview:

The ‘`llvm.memset.element.unordered.atomic.*`’ intrinsic is a specialization of the ‘`llvm.memset.*`’ intrinsic. It differs in that the `dest` is treated as an array with elements that are exactly `element_size` bytes, and the assignment to that array uses uses a sequence of unordered atomic store operations that are a positive integer multiple of the `element_size` in size.

##### Arguments:

The first three arguments are the same as they are in the @llvm.memset intrinsic, with the added constraint that `len` is required to be a positive integer multiple of the `element_size`. If `len` is not a positive integer multiple of `element_size`, then the behavior of the intrinsic is undefined.

`element_size` must be a compile-time constant positive power of two no greater than target-specific atomic access size limit.

The `dest` input pointer must have the `align` parameter attribute specified. It must be a power of two no less than the `element_size`. Caller guarantees that the destination pointer is aligned to that boundary.

##### Semantics:

The ‘`llvm.memset.element.unordered.atomic.*`’ intrinsic sets the `len` bytes of memory starting at the destination location to the given `value`. The memory is set with a sequence of store operations where each access is guaranteed to be a multiple of `element_size` bytes wide and aligned at an `element_size` boundary.

The order of the assignment is unspecified. Only one write is issued to the destination buffer per element. It is well defined to have concurrent reads and writes to the destination provided those reads and writes are unordered atomic when specified.

This intrinsic does not provide any additional ordering guarantees over those provided by a set of unordered stores to the destination.

##### Lowering:

In the most general case call to the ‘`llvm.memset.element.unordered.atomic.*`’ is lowered to a call to the symbol `__llvm_memset_element_unordered_atomic_*`. Where ‘*’ is replaced with an actual element size.

The optimizer is allowed to inline the memory assignment when it’s profitable to do so.

LLVM provides intrinsics that lower to Objective-C ARC runtime entry points. LLVM is aware of the semantics of these functions, and optimizes based on that knowledge. You can read more about the details of Objective-C ARC here.

##### Syntax:

```
declare ptr @llvm.objc.autorelease(ptr)
```

##### Lowering:

Lowers to a call to objc_autorelease.

##### Syntax:

```
declare void @llvm.objc.autoreleasePoolPop(ptr)
```

##### Lowering:

Lowers to a call to objc_autoreleasePoolPop.

##### Syntax:

```
declare ptr @llvm.objc.autoreleasePoolPush()
```

##### Lowering:

Lowers to a call to objc_autoreleasePoolPush.

##### Syntax:

```
declare ptr @llvm.objc.autoreleaseReturnValue(ptr)
```

##### Lowering:

Lowers to a call to objc_autoreleaseReturnValue.

##### Syntax:

```
declare void @llvm.objc.copyWeak(ptr, ptr)
```

##### Lowering:

Lowers to a call to objc_copyWeak.

##### Syntax:

```
declare void @llvm.objc.destroyWeak(ptr)
```

##### Lowering:

Lowers to a call to objc_destroyWeak.

##### Syntax:

```
declare ptr @llvm.objc.initWeak(ptr, ptr)
```

##### Lowering:

Lowers to a call to objc_initWeak.

##### Syntax:

```
declare ptr @llvm.objc.loadWeak(ptr)
```

##### Lowering:

Lowers to a call to objc_loadWeak.

##### Syntax:

```
declare ptr @llvm.objc.loadWeakRetained(ptr)
```

##### Lowering:

Lowers to a call to objc_loadWeakRetained.

##### Syntax:

```
declare void @llvm.objc.moveWeak(ptr, ptr)
```

##### Lowering:

Lowers to a call to objc_moveWeak.

##### Syntax:

```
declare void @llvm.objc.release(ptr)
```

##### Lowering:

Lowers to a call to objc_release.

##### Syntax:

```
declare ptr @llvm.objc.retain(ptr)
```

##### Lowering:

Lowers to a call to objc_retain.

##### Syntax:

```
declare ptr @llvm.objc.retainAutorelease(ptr)
```

##### Lowering:

Lowers to a call to objc_retainAutorelease.

##### Syntax:

```
declare ptr @llvm.objc.retainAutoreleaseReturnValue(ptr)
```

##### Lowering:

Lowers to a call to objc_retainAutoreleaseReturnValue.

##### Syntax:

```
declare ptr @llvm.objc.retainAutoreleasedReturnValue(ptr)
```

##### Lowering:

Lowers to a call to objc_retainAutoreleasedReturnValue.

##### Syntax:

```
declare ptr @llvm.objc.retainBlock(ptr)
```

##### Lowering:

Lowers to a call to objc_retainBlock.

##### Syntax:

```
declare void @llvm.objc.storeStrong(ptr, ptr)
```

##### Lowering:

Lowers to a call to objc_storeStrong.

##### Syntax:

```
declare ptr @llvm.objc.storeWeak(ptr, ptr)
```

##### Lowering:

Lowers to a call to objc_storeWeak.

These intrinsics are used to carry certain debuginfo together with IR-level operations. For example, it may be desirable to know the structure/union name and the original user-level field indices. Such information got lost in IR GetElementPtr instruction since the IR types are different from debugInfo types and unions are converted to structs in IR.

##### Syntax:

```
declare <ret_type>
@llvm.preserve.array.access.index.p0s_union.anons.p0a10s_union.anons(<type> base,
                                                                     i32 dim,
                                                                     i32 index)
```

##### Overview:

The ‘`llvm.preserve.array.access.index`’ intrinsic returns the getelementptr address based on array base `base`, array dimension `dim` and the last access index `index` into the array. The return type `ret_type` is a pointer type to the array element. The array `dim` and `index` are preserved which is more robust than getelementptr instruction which may be subject to compiler transformation. The `llvm.preserve.access.index` type of metadata is attached to this call instruction to provide array or pointer debuginfo type. The metadata is a `DICompositeType` or `DIDerivedType` representing the debuginfo version of `type`.

##### Arguments:

The `base` is the array base address. The `dim` is the array dimension. The `base` is a pointer if `dim` equals 0. The `index` is the last access index into the array or pointer.

The `base` argument must be annotated with an elementtype attribute at the call-site. This attribute specifies the getelementptr element type.

##### Semantics:

The ‘`llvm.preserve.array.access.index`’ intrinsic produces the same result as a getelementptr with base `base` and access operands `{dim's 0's, index}`.

##### Syntax:

```
declare <type>
@llvm.preserve.union.access.index.p0s_union.anons.p0s_union.anons(<type> base,
                                                                  i32 di_index)
```

##### Overview:

The ‘`llvm.preserve.union.access.index`’ intrinsic carries the debuginfo field index `di_index` and returns the `base` address. The `llvm.preserve.access.index` type of metadata is attached to this call instruction to provide union debuginfo type. The metadata is a `DICompositeType` representing the debuginfo version of `type`. The return type `type` is the same as the `base` type.

##### Arguments:

The `base` is the union base address. The `di_index` is the field index in debuginfo.

##### Semantics:

The ‘`llvm.preserve.union.access.index`’ intrinsic returns the `base` address.

##### Syntax:

```
declare <ret_type>
@llvm.preserve.struct.access.index.p0i8.p0s_struct.anon.0s(<type> base,
                                                           i32 gep_index,
                                                           i32 di_index)
```

##### Overview:

The ‘`llvm.preserve.struct.access.index`’ intrinsic returns the getelementptr address based on struct base `base` and IR struct member index `gep_index`. The `llvm.preserve.access.index` type of metadata is attached to this call instruction to provide struct debuginfo type. The metadata is a `DICompositeType` representing the debuginfo version of `type`. The return type `ret_type` is a pointer type to the structure member.

##### Arguments:

The `base` is the structure base address. The `gep_index` is the struct member index based on IR structures. The `di_index` is the struct member index based on debuginfo.

The `base` argument must be annotated with an elementtype attribute at the call-site. This attribute specifies the getelementptr element type.

##### Semantics:

The ‘`llvm.preserve.struct.access.index`’ intrinsic produces the same result as a getelementptr with base `base` and access operands `{0, gep_index}`.

##### Syntax:

```
declare ptr @llvm.protected.field.ptr(ptr ptr, i64 disc, i1 use_hw_encoding)
```

##### Overview:

The ‘`llvm.protected.field.ptr`’ intrinsic returns a pointer to the storage location of a pointer that has special properties as described below.

##### Arguments:

The first argument is the pointer specifying the location to store the pointer. The second argument is the discriminator, which is used as an input for the pointer encoding. The third argument specifies whether to use a target-specific mechanism to encode the pointer.

##### Semantics:

This intrinsic returns a pointer which may be used to store a pointer at the specified address that is encoded using the specified discriminator. Stores via the pointer will cause the stored pointer to be blended with the second argument before being stored. The blend operation shall be either a weak but cheap and target-independent operation (if the third argument is 0) or a stronger target-specific operation (if the third argument is 1). When loading from the pointer, the inverse operation is done on the loaded pointer after it is loaded. Specifically, when the third argument is 1, the pointer is signed (using pointer authentication instructions or emulated PAC if not supported by the hardware) using the discriminator before being stored, and authenticated after being loaded. Note that it is currently unsupported to have the third argument be 1 on targets other than AArch64, and it is also currently unsupported to have the third argument be 0 at all.

If the pointer is used other than for loading or storing (e.g. its address escapes), that will disable all blending operations using the deactivation symbol specified in the intrinsic’s operand bundle. The deactivation symbol operand bundle is copied onto any sign and auth intrinsics that this intrinsic is lowered into. The intent is that the deactivation symbol represents a field identifier.

This intrinsic is used to implement structure protection.

##### Syntax:

```
declare void @llvm.cond.loop(i1 pred)
```

##### Overview:

The ‘`llvm.cond.loop`’ intrinsic spins in an infinite loop if the given predicate `pred` is true, otherwise it does nothing.

##### Arguments:

`pred` is the predicate.

##### Semantics:

This intrinsic is semantically equivalent to a conditional branch conditioned on `pred` to a basic block consisting only of an unconditional branch to itself.

Unlike such a branch, certain backends guarantee that this intrinsic will use specific instructions. This allows an interrupt handler or other introspection mechanism to straightforwardly detect whether the program is currently spinning in the infinite loop and possibly terminate the program if so. The intent is that this intrinsic may be used as a more efficient alternative to a conditional branch to a call to `llvm.trap` in circumstances where the loop detection is guaranteed to be present. This construct has been experimentally determined to be executed more efficiently (when the branch is not taken) than a conditional branch to a trap instruction on AMD and older Intel microarchitectures, and is also more code size efficient by avoiding the need to emit a trap instruction and possibly a long branch instruction.

With the X86 backend, the infinite loop is guaranteed to consist of a short conditional branch instruction that branches to itself. Specifically, the first byte of the instruction will be between 0x70 and 0x7F, and the second byte will be 0xFE.

There are currently no guarantees about instructions used by other backends.

##### Syntax:

```
declare void @llvm.looptrap() cold noreturn nounwind
```

##### Overview:

The ‘`llvm.looptrap`’ intrinsic is equivalent to `llvm.cond.loop(true)`, but is also considered to be `noreturn`, which enables certain optimizations by allowing the optimizer to assume that a branch leading to a call to this intrinsic was not taken. A late optimization pass will convert this intrinsic to either `llvm.cond.loop(true)` or `llvm.cond.loop(pred)`, where `pred` is a predicate for a conditional branch leading to the intrinsic call, if possible.
