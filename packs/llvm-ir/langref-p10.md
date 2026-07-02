---
title: "LLVM Language Reference Manual (part 10/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 10/20
---

# LLVM Language Reference Manual

The ‘`llvm.returnaddress`’ intrinsic either returns a pointer indicating the return address of the specified call frame, or zero if it cannot be identified. The value returned by this intrinsic is likely to be incorrect or 0 for arguments other than zero, so it should only be used for debugging purposes.

Note that calling this intrinsic does not prevent function inlining or other aggressive transformations, so the value returned may not be that of the obvious source-language caller.

##### Syntax:

```
declare ptr @llvm.addressofreturnaddress()
```

##### Overview:

The ‘`llvm.addressofreturnaddress`’ intrinsic returns a target-specific pointer to the place in the stack frame where the return address of the current function is stored.

##### Semantics:

Note that calling this intrinsic does not prevent function inlining or other aggressive transformations, so the value returned may not be that of the obvious source-language caller.

This intrinsic is only implemented for x86 and aarch64.

##### Syntax:

```
declare ptr @llvm.sponentry()
```

##### Overview:

The ‘`llvm.sponentry`’ intrinsic returns the stack pointer value at the entry of the current function calling this intrinsic.

##### Semantics:

Note this intrinsic is only verified on AArch64 and ARM.

##### Syntax:

```
declare ptr @llvm.stackaddress.p0()
```

##### Overview:

The ‘`llvm.stackaddress`’ intrinsic returns the starting address of the stack region that may be used by called functions.

##### Semantics:

This intrinsic returns the *logical* value of the stack pointer register, that is, the address separating the stack space of the current function from the stack space that may be modified by called functions. It corresponds to the address returned by ‘`llvm.sponentry`’, offset by the size of the current function’s stack frame.

On certain targets (e.g. x86), the logical and actual (or physical) values of the stack pointer register are the same. However, on other architectures (e.g. SPARCv9), the logical value of the stack pointer register may differ from the physical value. ‘`llvm.stackaddress`’ handles this discrepancy and returns the correct boundary address.

##### Syntax:

```
declare ptr @llvm.frameaddress(i32 <level>)
```

##### Overview:

The ‘`llvm.frameaddress`’ intrinsic attempts to return the target-specific frame pointer value for the specified stack frame.

##### Arguments:

The argument to this intrinsic indicates which function to return the frame pointer for. Zero indicates the calling function, one indicates its caller, etc. The argument is **required** to be a constant integer value.

##### Semantics:

The ‘`llvm.frameaddress`’ intrinsic either returns a pointer indicating the frame address of the specified call frame, or zero if it cannot be identified. The value returned by this intrinsic is likely to be incorrect or 0 for arguments other than zero, so it should only be used for debugging purposes.

Note that calling this intrinsic does not prevent function inlining or other aggressive transformations, so the value returned may not be that of the obvious source-language caller.

##### Syntax:

```
declare ptr @llvm.swift.async.context.addr()
```

##### Overview:

The ‘`llvm.swift.async.context.addr`’ intrinsic returns a pointer to the part of the extended frame record containing the asynchronous context of a Swift execution.

##### Semantics:

If the caller has a `swiftasync` parameter, that argument will initially be stored at the returned address. If not, it will be initialized to null.

##### Syntax:

```
declare void @llvm.localescape(...)
declare ptr @llvm.localrecover(ptr %func, ptr %fp, i32 %idx)
```

##### Overview:

The ‘`llvm.localescape`’ intrinsic escapes offsets of a collection of static allocas, and the ‘`llvm.localrecover`’ intrinsic applies those offsets to a live frame pointer to recover the address of the allocation. The offset is computed during frame layout of the caller of `llvm.localescape`.

##### Arguments:

All arguments to ‘`llvm.localescape`’ must be pointers to static allocas or casts of static allocas. Each function can only call ‘`llvm.localescape`’ once, and it can only do so from the entry block.

The `func` argument to ‘`llvm.localrecover`’ must be a constant bitcasted pointer to a function defined in the current module. The code generator cannot determine the frame allocation offset of functions defined in other modules.

The `fp` argument to ‘`llvm.localrecover`’ must be a frame pointer of a call frame that is currently live. The return value of ‘`llvm.localaddress`’ is one way to produce such a value, but various runtimes also expose a suitable pointer in platform-specific ways.

The `idx` argument to ‘`llvm.localrecover`’ indicates which alloca passed to ‘`llvm.localescape`’ to recover. It is zero-indexed.

##### Semantics:

These intrinsics allow a group of functions to share access to a set of local stack allocations of a one parent function. The parent function may call the ‘`llvm.localescape`’ intrinsic once from the function entry block, and the child functions can use ‘`llvm.localrecover`’ to access the escaped allocas. The ‘`llvm.localescape`’ intrinsic blocks inlining, as inlining changes where the escaped allocas are allocated, which would break attempts to use ‘`llvm.localrecover`’.

##### Syntax:

```
declare void @llvm.seh.try.begin()
declare void @llvm.seh.try.end()
```

##### Overview:

The ‘`llvm.seh.try.begin`’ and ‘`llvm.seh.try.end`’ intrinsics mark the boundary of a _try region for Windows SEH Asynchronous Exception Handling.

##### Semantics:

When a C-function is compiled with Windows SEH Asynchronous Exception option, -feh_asynch (aka MSVC -EHa), these two intrinsics are injected to mark _try boundary and to prevent potential exceptions from being moved across boundary. Any set of operations can then be confined to the region by reading their leaf inputs via volatile loads and writing their root outputs via volatile stores.

##### Syntax:

```
declare void @llvm.seh.scope.begin()
declare void @llvm.seh.scope.end()
```

##### Overview:

The ‘`llvm.seh.scope.begin`’ and ‘`llvm.seh.scope.end`’ intrinsics mark the boundary of a CPP object lifetime for Windows SEH Asynchronous Exception Handling (MSVC option -EHa).

##### Semantics:

LLVM’s ordinary exception-handling representation associates EH cleanups and handlers only with invoke``s, which normally correspond only to call sites.  To support arbitrary faulting instructions, it must be possible to recover the current EH scope for any instruction.  Turning every operation in LLVM that could fault into an ``invoke of a new, potentially-throwing intrinsic would require adding a large number of intrinsics, impede optimization of those operations, and make compilation slower by introducing many extra basic blocks. These intrinsics can be used instead to mark the region protected by a cleanup, such as for a local C++ object with a non-trivial destructor. `llvm.seh.scope.begin` is used to mark the start of the region; it is always called with `invoke`, with the unwind block being the desired unwind destination for any potentially-throwing instructions within the region. *llvm.seh.scope.end* is used to mark when the scope ends and the EH cleanup is no longer required (e.g., because the destructor is being called).

##### Syntax:

```
declare i32 @llvm.read_register.i32(metadata)
declare i64 @llvm.read_register.i64(metadata)
declare i32 @llvm.read_volatile_register.i32(metadata)
declare i64 @llvm.read_volatile_register.i64(metadata)
declare void @llvm.write_register.i32(metadata, i32 @value)
declare void @llvm.write_register.i64(metadata, i64 @value)
declare void @llvm.write_volatile_register.i32(metadata, i32 @value)
declare void @llvm.write_volatile_register.i64(metadata, i64 @value)
!0 = !{!"sp\00"}
```

##### Overview:

The ‘`llvm.read_register`’, ‘`llvm.read_volatile_register`’, ‘`llvm.write_register`’, and ‘`llvm.write_volatile_register`’ intrinsics provide access to the named register. The register must be valid on the architecture being compiled to. The type needs to be compatible with the register being accessed.

##### Semantics:

The ‘`llvm.read_register`’ and ‘`llvm.read_volatile_register`’ intrinsics return the current value of the register, where possible. The ‘`llvm.write_register`’ and ‘`llvm.write_volatile_register`’ intrinsics set the current value of the register, where possible.

A call to ‘`llvm.read_volatile_register`’ or ‘`llvm.write_volatile_register`’ is assumed to have side-effects and will not be reordered or eliminated by the optimizer.

This is useful to implement named register global variables that need to always be mapped to a specific register, as is common practice on bare-metal programs including OS kernels.

The compiler doesn’t check for register availability or use of the used register in surrounding code, including inline assembly. Because of that, allocatable registers are not supported by ‘`llvm.read_register`’, ‘`llvm.read_volatile_register`’, or ‘`llvm.write_register`’.

‘`llvm.write_volatile_register`’ supports allocatable registers. Writing to an allocatable register means the value is copied into that physical register at the point of the call; the register may subsequently be reused by the register allocator for other purposes. The backend emits a `FAKE_USE` of the physical register after the write to prevent the store from being dead-eliminated before register allocation.

Warning: Register support is target-specific. The IR-level verifier does not validate register names; an unsupported name results in a fatal error during code generation. Supported registers vary by target and can be found in each target’s `getRegisterByName` implementation. ‘`llvm.write_volatile_register`’ support for allocatable registers is currently only implemented on AArch64.

##### Syntax:

```
declare ptr @llvm.stacksave.p0()
declare ptr addrspace(5) @llvm.stacksave.p5()
```

##### Overview:

The ‘`llvm.stacksave`’ intrinsic is used to remember the current state of the function stack, for use with llvm.stackrestore. This is useful for implementing language features like scoped automatic variable sized arrays in C99.

##### Semantics:

This intrinsic returns an opaque pointer value that can be passed to llvm.stackrestore. When an `llvm.stackrestore` intrinsic is executed with a value saved from `llvm.stacksave`, it effectively restores the state of the stack to the state it was in when the `llvm.stacksave` intrinsic executed. In practice, this pops any alloca blocks from the stack that were allocated after the `llvm.stacksave` was executed. The address space should typically be the alloca address space.

##### Syntax:

```
declare void @llvm.stackrestore.p0(ptr %ptr)
declare void @llvm.stackrestore.p5(ptr addrspace(5) %ptr)
```

##### Overview:

The ‘`llvm.stackrestore`’ intrinsic is used to restore the state of the function stack to the state it was in when the corresponding llvm.stacksave intrinsic executed. This is useful for implementing language features like scoped automatic variable sized arrays in C99. The address space should typically be the alloca address space.

##### Semantics:

See the description for llvm.stacksave.

##### Syntax:

```
declare <ret_type>
@llvm.structured.gep(ptr elementtype(<basetype>) <source>
                     {, [i32/i64] <index> }*)
```

##### Overview:

The ‘`llvm.structured.gep`’ intrinsic (structured **G**et**E**lement**P**tr) computes a new pointer address resulting from a logical indexing into the `<source>` pointer. The returned address depends on the indices and may depend on the layout of `<basetype>` at runtime.

##### Arguments:

`ptr elementtype(<basetype>) <source>`: A pointer to the memory location used as base for the address computation.

The `source` argument must be annotated with an elementtype attribute at the call-site. This attribute specifies the type of the element pointed to by the pointer source. This type will be used along with the provided indices and source operand to compute a new pointer representing the result of a logical indexing into the basetype pointed by source.

The `basetype` is only associated with `<source>` for this particular call. A frontend could possibly emit multiple structured GEP with the same source pointer but a different `basetype`.

`[i32/i64] index, ...`: Indices used to traverse into the `basetype` and compute a pointer to the target element. Indices can be 32-bit or 64-bit unsigned integers. Indices being handled one by one, both sizes can be mixed in the same instruction. The precision used to compute the resulting pointer is target-dependent. When used to index into a struct, only integer constants are allowed.

##### Semantics:

The `llvm.structured.gep` performs a logical traversal of the type `basetype` using the list of provided indices, computing the pointer addressing the targeted element/field assuming `source` points to a physically laid out `basetype`. The physical layout of the source depends on the target and does not necessarily match the one described by the datalayout.

The first index determines which element/field of `basetype` is selected, computes the pointer to access this element/field assuming `source` points to the start of `basetype`. This pointer becomes the new `source`, the current type the new `basetype`, and the next indices is consumed until a scalar type is reached or all indices are consumed.

All indices must be consumed, and it is illegal to index into a scalar type. Meaning the maximum number of indices depends on the depth of the basetype.

Because this instruction performs a logical addressing, all indices are assumed to be inbounds. This means it is not possible to access the next element in the logical layout by overflowing:

- If the indexed type is a struct with N fields, the index must be an immediate/constant value in the range `[0; N[`.
- If indexing into an array or vector, the index can be a variable, but is assumed to be inbounds with regards to the current basetype logical layout.
- If the traversed type is an array or vector of N elements with `N > 0`, the index is assumed to belong to `[0; N[`.
- If the traversed type is an array of size `0`, the array size is assumed to be known at runtime, and the instruction assumes the index is always inbounds.

In all cases **except** when the accessed type is a 0-sized array, indexing out of bounds yields *poison*. When the index value is unknown, optimizations can use the type bounds to determine the range of values the index can have. If the source pointer is poison, the instruction returns poison. The resulting pointer belongs to the same address space as `source`. This instruction does not dereference the pointer.

##### Example:

**Simple case: logical access of a struct field**

```cpp
struct A { int a, int b, int c, int d };
int val = my_struct->b;
```

Could be translated to:

```llvm
%A = type { i32, i32, i32, i32 }
%src = call ptr @llvm.structured.gep(ptr elementtype(%A) %my_struct, i32 1)
%val = load i32, ptr %src
```

**A more complex case**

This instruction can also be used on the same pointer with different basetypes, as long as codegen knows how those are physically laid out. Let’s consider the following code:

```cpp
struct S {
    uint a;
    uint b;
    uint c;
    uint d;
}

int val = my_struct->b;
```

In this example, the frontend doesn’t know the exact physical layout, but knows those logical layouts are lowered to the same physical layout:

> - *{ i32, i32, i32, i32 }*
> - *[ i32 x 4 ]*

This means is is valid to lower the following code to either:

```llvm
%S = type { i32, i32, i32, i32 }
%src = call ptr @llvm.structured.gep(ptr elementtype(%S) %my_struct, i32 1)
load i32, ptr %src
```

Or:

```llvm
%src = call ptr @llvm.structured.gep(ptr elementtype([ 4 x i32 ]) %my_struct, i32 1)
load i32, ptr %src
```

This is, however, dependent on context that codegen has an insight on. The fact that *[ i32 x 4 ]* and *%S* are equivalent depends on the target.

##### Syntax:

```
declare elementtype(<allocated_type>) ptr
@llvm.structured.alloca()
```

##### Overview:

The ‘`llvm.structured.alloca`’ intrinsic allocates uninitialized memory on the stack for a logical type, such as an aggregate, an array, or a scalar.

Unlike the standard alloca instruction, the physical memory layout of a `llvm.structured.alloca` is completely opaque to the IR. Exact padding, size, alignment and subtype offsets is target-dependent and may differ from the standard `DataLayout`.

##### Arguments:

The intrinsic must be annotated with an elementtype attribute at the call-site on the return value. This attribute specifies the type of the allocated element.

##### Semantics:

The `llvm.structured.alloca` intrinsic allocates uninitialized memory for a logical type. Loading from uninitialized memory produces an undefined value. This intrinsic does not guarantee that the allocated memory will store a value of the given type, only that it allocates enough space for it on the destination target. While the type’s size and layout are constant (independent of location), the exact padding and offsets between subtypes are opaque to the IR and are determined by the target’s backend.

The resulting pointer is in the alloca address space defined in the datalayout string.

Standard pointer arithmetic (`getelementptr`, `ptradd`) and lifetime intrinsics (llvm.lifetime.start, llvm.lifetime.end) are permitted on the returned pointer. However, because the physical layout is opaque, using physical pointer arithmetic requires the frontend or emitting pass to have explicit knowledge of the backend’s layout rules.

##### Example:

```llvm
%S = type { i32, i32, i32, i32 }

; Allocate one instance of %S on the stack
%ptr = call elementtype(%S) ptr @llvm.structured.alloca()

; Access the second field of the allocated struct
%field_ptr = call ptr @llvm.structured.gep(ptr elementtype(%S) %ptr, i32 1)
%val = load i32, ptr %field_ptr

; Allocate an array of 10 i32s on the stack
%array_ptr = call elementtype([10 x i32]) ptr @llvm.structured.alloca()

; Allocate a single i32 on the stack
%scalar_ptr = call elementtype(i32) ptr @llvm.structured.alloca()

; Although the exact size of 'i32' or '%S' is opaque, it is constant
; for the duration of the module. This allows, for example, reusing
; an allocation slot for two different values of the same type.
%a = call elementtype(float) ptr @llvm.structured.alloca()
%b = call elementtype(float) ptr @llvm.structured.alloca()
; %a and %b are guaranteed to have the same allocation size.
```

##### Syntax:

```
declare i32 @llvm.get.dynamic.area.offset.i32()
declare i64 @llvm.get.dynamic.area.offset.i64()
```

##### Overview:

> The ‘`llvm.get.dynamic.area.offset.*`’ intrinsic family is used to get the offset from native stack pointer to the address of the most recent dynamic alloca on the caller’s stack. These intrinsics are intended for use in combination with llvm.stacksave to get a pointer to the most recent dynamic alloca. This is useful, for example, for AddressSanitizer’s stack unpoisoning routines.

##### Semantics:

> These intrinsics return a non-negative integer value that can be used to get the address of the most recent dynamic alloca, allocated by alloca on the caller’s stack. In particular, for targets where stack grows downwards, adding this offset to the native stack pointer would get the address of the most recent dynamic alloca. For targets where stack grows upwards, the situation is a bit more complicated, because subtracting this value from stack pointer would get the address one past the end of the most recent dynamic alloca.
> 
> Although for most targets *llvm.get.dynamic.area.offset <int_get_dynamic_area_offset>* returns just a zero, for others, such as PowerPC and PowerPC64, it returns a compile-time-known constant value.
> 
> The return value type of llvm.get.dynamic.area.offset must match the target’s alloca address space type.

##### Syntax:

```
declare void @llvm.prefetch(ptr <address>, i32 <rw>, i32 <locality>, i32 <cache type>)
```

##### Overview:

The ‘`llvm.prefetch`’ intrinsic is a hint to the code generator to insert a prefetch instruction if supported; otherwise, it is a noop. Prefetches have no effect on the behavior of the program but can change its performance characteristics.

##### Arguments:

`address` is the address to be prefetched, `rw` is the specifier determining if the fetch should be for a read (0) or write (1), and `locality` is a temporal locality specifier ranging from (0) - no locality, to (3) - extremely local keep in cache. The `cache type` specifies whether the prefetch is performed on the data (1) or instruction (0) cache. The `rw`, `locality` and `cache type` arguments must be constant integers.

##### Semantics:

This intrinsic does not modify the behavior of the program. In particular, prefetches cannot trap and do not produce a value. On targets that support this intrinsic, the prefetch can provide hints to the processor cache for better performance.

##### Syntax:

```
declare void @llvm.pcmarker(i32 <id>)
```

##### Overview:

The ‘`llvm.pcmarker`’ intrinsic is a method to export a Program Counter (PC) in a region of code to simulators and other tools. The method is target specific, but it is expected that the marker will use exported symbols to transmit the PC of the marker. The marker makes no guarantees that it will remain with any specific instruction after optimizations. It is possible that the presence of a marker will inhibit optimizations. The intended use is to be inserted after optimizations to allow correlations of simulation runs.

##### Arguments:

`id` is a numerical id identifying the marker.

##### Semantics:

This intrinsic does not modify the behavior of the program. Backends that do not support this intrinsic may ignore it.

##### Syntax:

```
declare i64 @llvm.readcyclecounter()
```

##### Overview:

The ‘`llvm.readcyclecounter`’ intrinsic provides access to the cycle counter register (or similar low latency, high accuracy clocks) on those targets that support it. On X86, it should map to RDTSC. On Alpha, it should map to RPCC. As the backing counters overflow quickly (on the order of 9 seconds on alpha), this should only be used for small timings.

##### Semantics:

When directly supported, reading the cycle counter should not modify any memory. Implementations are allowed to either return an application specific value or a system wide value. On backends without support, this is lowered to a constant 0.

Note that runtime support may be conditional on the privilege-level code is running at and the host platform.

##### Syntax:

```
declare i64 @llvm.readsteadycounter()
```

##### Overview:

The ‘`llvm.readsteadycounter`’ intrinsic provides access to the fixed frequency clock on targets that support it. Unlike ‘`llvm.readcyclecounter`’, this clock is expected to tick at a constant rate, making it suitable for measuring elapsed time. The actual frequency of the clock is implementation defined.

##### Semantics:

When directly supported, reading the steady counter should not modify any memory. Implementations are allowed to either return an application specific value or a system wide value. On backends without support, this is lowered to a constant 0.

##### Syntax:

```
declare void @llvm.clear_cache(ptr, ptr)
```

##### Overview:

The ‘`llvm.clear_cache`’ intrinsic ensures visibility of modifications in the specified range to the execution unit of the processor. On targets with non-unified instruction and data cache, the implementation flushes the instruction cache.

##### Semantics:

On platforms with coherent instruction and data caches (e.g., x86), this intrinsic is a nop. On platforms with non-coherent instruction and data cache (e.g., ARM, MIPS), the intrinsic is lowered either to appropriate instructions or a system call, if cache flushing requires special privileges.

The default behavior is to emit a call to `__clear_cache` from the run time library.

This intrinsic does *not* empty the instruction pipeline. Modifications of the current function are outside the scope of the intrinsic.

##### Syntax:

```
declare void @llvm.instrprof.increment(ptr <name>, i64 <hash>,
                                       i32 <num-counters>, i32 <index>)
```

##### Overview:

The ‘`llvm.instrprof.increment`’ intrinsic can be emitted by a frontend for use with instrumentation-based profiling. These will be lowered by the `-instrprof` pass to generate execution counts of a program at runtime.

##### Arguments:

The first argument is a pointer to a global variable containing the name of the entity being instrumented. This should generally be the (mangled) function name for a set of counters.

The second argument is a hash value that can be used by the consumer of the profile data to detect changes to the instrumented source, and the third is the number of counters associated with `name`. It is an error if `hash` or `num-counters` differ between two instances of `instrprof.increment` that refer to the same name.

The last argument refers to which of the counters for `name` should be incremented. It should be a value between 0 and `num-counters`.

##### Semantics:

This intrinsic represents an increment of a profiling counter. It will cause the `-instrprof` pass to generate the appropriate data structures and the code to increment the appropriate value, in a format that can be written out by a compiler runtime and consumed via the `llvm-profdata` tool.

The intrinsic is lowered differently for contextual profiling by the `-ctx-instr-lower` pass. Here:

- the entry basic block increment counter is lowered as a call to compiler-rt, to either `__llvm_ctx_profile_start_context` or `__llvm_ctx_profile_get_context`. Either returns a pointer to a context object which contains a buffer into which counter increments can happen. Note that the pointer value returned by compiler-rt may have its LSB set - counter increments happen offset from the address with the LSB cleared.
- all the other lowerings of `llvm.instrprof.increment[.step]` happen within that context.
- the context is assumed to be a local value to the function, and no concurrency concerns need to be handled by LLVM.

##### Syntax:

```
declare void @llvm.instrprof.increment.step(ptr <name>, i64 <hash>,
                                            i32 <num-counters>,
                                            i32 <index>, i64 <step>)
```

##### Overview:

The ‘`llvm.instrprof.increment.step`’ intrinsic is an extension to the ‘`llvm.instrprof.increment`’ intrinsic with an additional fifth argument to specify the step of the increment.

##### Arguments:

The first four arguments are the same as ‘`llvm.instrprof.increment`’ intrinsic.

The last argument specifies the value of the increment of the counter variable.

##### Semantics:

See description of ‘`llvm.instrprof.increment`’ intrinsic.

##### Syntax:

```
declare void @llvm.instrprof.callsite(ptr <name>, i64 <hash>,
                                      i32 <num-counters>,
                                      i32 <index>, ptr <callsite>)
```

##### Overview:

The ‘`llvm.instrprof.callsite`’ intrinsic should be emitted before a callsite that’s not to a “fake” callee (like another intrinsic or asm). It is used by contextual profiling and has side-effects. Its lowering happens in IR, and target-specific backends should never encounter it.

##### Arguments:

The first 4 arguments are similar to `llvm.instrprof.increment`. The indexing is specific to callsites, meaning callsites are indexed from 0, independent from the indexes used by the other intrinsics (such as `llvm.instrprof.increment[.step]`).

The last argument is the called value of the callsite this intrinsic precedes.

##### Semantics:

This is lowered by contextual profiling. In contextual profiling, functions get, from compiler-rt, a pointer to a context object. The context object consists of a buffer LLVM can use to perform counter increments (i.e., the lowering of `llvm.instrprof.increment[.step]`. The address range following the counter buffer, `<num-counters>` x `sizeof(ptr)` - sized, is expected to contain pointers to contexts of functions called from this function (“subcontexts”). LLVM does not dereference into that memory region, just calculates GEPs.

The lowering of `llvm.instrprof.callsite` consists of:

- write to `__llvm_ctx_profile_expected_callee` the `<callsite>` value;
- write to `__llvm_ctx_profile_callsite` the address into this function’s context of the `<index>` position into the subcontexts region.

`__llvm_ctx_profile_{expected_callee|callsite}` are initialized by compiler-rt and are TLS. They are both vectors of pointers of size 2. The index into each is determined when the current function obtains the pointer to its context from compiler-rt. The pointer’s LSB gives the index.

##### Syntax:

```
declare void @llvm.instrprof.timestamp(i8* <name>, i64 <hash>,
                                       i32 <num-counters>, i32 <index>)
```

##### Overview:

The ‘`llvm.instrprof.timestamp`’ intrinsic is used to implement temporal profiling.

##### Arguments:

The arguments are the same as ‘`llvm.instrprof.increment`’. The `index` is expected to always be zero.

##### Semantics:

Similar to the ‘`llvm.instrprof.increment`’ intrinsic, but it stores a timestamp representing when this function was executed for the first time.

##### Syntax:

```
declare void @llvm.instrprof.cover(ptr <name>, i64 <hash>,
                                   i32 <num-counters>, i32 <index>)
```

##### Overview:

The ‘`llvm.instrprof.cover`’ intrinsic is used to implement coverage instrumentation.

##### Arguments:

The arguments are the same as the first four arguments of ‘`llvm.instrprof.increment`’.

##### Semantics:

Similar to the ‘`llvm.instrprof.increment`’ intrinsic, but it stores zero to the profiling variable to signify that the function has been covered. We store zero because this is more efficient on some targets.

##### Syntax:

```
declare void @llvm.instrprof.value.profile(ptr <name>, i64 <hash>,
                                           i64 <value>, i32 <value_kind>,
                                           i32 <index>)
```

##### Overview:

The ‘`llvm.instrprof.value.profile`’ intrinsic can be emitted by a frontend for use with instrumentation-based profiling. This will be lowered by the `-instrprof` pass to find out the target values, instrumented expressions take in a program at runtime.

##### Arguments:

The first argument is a pointer to a global variable containing the name of the entity being instrumented. `name` should generally be the (mangled) function name for a set of counters.

The second argument is a hash value that can be used by the consumer of the profile data to detect changes to the instrumented source. It is an error if `hash` differs between two instances of `llvm.instrprof.*` that refer to the same name.

The third argument is the value of the expression being profiled. The profiled expression’s value should be representable as an unsigned 64-bit value. The fourth argument represents the kind of value profiling that is being done. The supported value profiling kinds are enumerated through the `InstrProfValueKind` type declared in the `<include/llvm/ProfileData/InstrProf.h>` header file. The last argument is the index of the instrumented expression within `name`. It should be >= 0.

##### Semantics:

This intrinsic represents the point where a call to a runtime routine should be inserted for value profiling of target expressions. `-instrprof` pass will generate the appropriate data structures and replace the `llvm.instrprof.value.profile` intrinsic with the call to the profile runtime library with proper arguments.

##### Syntax:

```
declare void @llvm.instrprof.mcdc.parameters(ptr <name>, i64 <hash>,
                                             i32 <bitmap-bits>)
```

##### Overview:

The ‘`llvm.instrprof.mcdc.parameters`’ intrinsic is used to initiate MC/DC code coverage instrumentation for a function.

##### Arguments:

The first argument is a pointer to a global variable containing the name of the entity being instrumented. This should generally be the (mangled) function name for a set of counters.

The second argument is a hash value that can be used by the consumer of the profile data to detect changes to the instrumented source.

The third argument is the number of bitmap bits required by the function to record the number of test vectors executed for each boolean expression.

##### Semantics:

This intrinsic represents basic MC/DC parameters initiating one or more MC/DC instrumentation sequences in a function. It will cause the `-instrprof` pass to generate the appropriate data structures and the code to instrument MC/DC test vectors in a format that can be written out by a compiler runtime and consumed via the `llvm-profdata` tool.

##### Syntax:

```
declare void @llvm.instrprof.mcdc.tvbitmap.update(ptr <name>, i64 <hash>,
                                                  i32 <bitmap-index>,
                                                  ptr <mcdc-temp-addr>)
```

##### Overview:

The ‘`llvm.instrprof.mcdc.tvbitmap.update`’ intrinsic is used to track MC/DC test vector execution after each boolean expression has been fully executed. The overall value of the condition bitmap, after it has been successively updated with the true or false evaluation of each condition, uniquely identifies an executed MC/DC test vector and is used as a bit index into the global test vector bitmap.

##### Arguments:

The first argument is a pointer to a global variable containing the name of the entity being instrumented. This should generally be the (mangled) function name for a set of counters.

The second argument is a hash value that can be used by the consumer of the profile data to detect changes to the instrumented source.

The third argument is the bit index into the global test vector bitmap corresponding to the function.

The fourth argument is the address of the condition bitmap, which contains a value representing an executed MC/DC test vector. It is loaded and used as the bit index of the test vector bitmap.

##### Semantics:

This intrinsic represents the final operation of an MC/DC instrumentation sequence and will cause the `-instrprof` pass to generate the code to instrument an update of a function’s global test vector bitmap to indicate that a test vector has been executed. The global test vector bitmap can be consumed by the `llvm-profdata` and `llvm-cov` tools.

##### Syntax:

```
declare ptr @llvm.thread.pointer.p0()
declare ptr addrspace(5) @llvm.thread.pointer.p5()
```

##### Overview:

The ‘`llvm.thread.pointer`’ intrinsic returns the value of the thread pointer.

##### Semantics:

The ‘`llvm.thread.pointer`’ intrinsic returns a pointer to the TLS area for the current thread. The exact semantics of this value are target specific: it may point to the start of TLS area, to the end, or somewhere in the middle. Depending on the target, this intrinsic may read a register, call a helper function, read from an alternate memory space, or perform other operations necessary to locate the TLS area. Not all targets support this intrinsic. The address space must be the globals address space.

##### Syntax:

```
declare token @llvm.call.preallocated.setup(i32 %num_args)
```

##### Overview:

The ‘`llvm.call.preallocated.setup`’ intrinsic returns a token which can be used with a call’s `"preallocated"` operand bundle to indicate that certain arguments are allocated and initialized before the call.

##### Semantics:

The ‘`llvm.call.preallocated.setup`’ intrinsic returns a token which is associated with at most one call. The token can be passed to ‘`@llvm.call.preallocated.arg`’ to get a pointer to get that corresponding argument. The token must be the parameter to a `"preallocated"` operand bundle for the corresponding call.

Nested calls to ‘`llvm.call.preallocated.setup`’ are allowed, but must be properly nested. e.g.

:: code-block:: llvm

> %t1 = call token @llvm.call.preallocated.setup(i32 0) %t2 = call token @llvm.call.preallocated.setup(i32 0) call void foo() [“preallocated”(token %t2)] call void foo() [“preallocated”(token %t1)]

is allowed, but not

:: code-block:: llvm

> %t1 = call token @llvm.call.preallocated.setup(i32 0) %t2 = call token @llvm.call.preallocated.setup(i32 0) call void foo() [“preallocated”(token %t1)] call void foo() [“preallocated”(token %t2)]

##### Syntax:

```
declare ptr @llvm.call.preallocated.arg(token %setup_token, i32 %arg_index)
```

##### Overview:

The ‘`llvm.call.preallocated.arg`’ intrinsic returns a pointer to the corresponding preallocated argument for the preallocated call.

##### Semantics:

The ‘`llvm.call.preallocated.arg`’ intrinsic returns a pointer to the %arg_index``th argument with the ``preallocated attribute for the call associated with the `%setup_token`, which must be from ‘`llvm.call.preallocated.setup`’.

A call to ‘`llvm.call.preallocated.arg`’ must have a call site `preallocated` attribute. The type of the `preallocated` attribute must match the type used by the `preallocated` attribute of the corresponding argument at the preallocated call. The type is used in the case that an `llvm.call.preallocated.setup` does not have a corresponding call (e.g., due to DCE), where otherwise we cannot know how large the arguments are.

It is undefined behavior if this is called with a token from an ‘`llvm.call.preallocated.setup`’ if another ‘`llvm.call.preallocated.setup`’ has already been called or if the preallocated call corresponding to the ‘`llvm.call.preallocated.setup`’ has already been called.

##### Syntax:

```
declare ptr @llvm.call.preallocated.teardown(token %setup_token)
```

##### Overview:

The ‘`llvm.call.preallocated.teardown`’ intrinsic cleans up the stack created by a ‘`llvm.call.preallocated.setup`’.

##### Semantics:

The token argument must be a ‘`llvm.call.preallocated.setup`’.

The ‘`llvm.call.preallocated.teardown`’ intrinsic cleans up the stack allocated by the corresponding ‘`llvm.call.preallocated.setup`’. Exactly one of this or the preallocated call must be called to prevent stack leaks. It is undefined behavior to call both a ‘`llvm.call.preallocated.teardown`’ and the preallocated call for a given ‘`llvm.call.preallocated.setup`’.

For example, if the stack is allocated for a preallocated call by a ‘`llvm.call.preallocated.setup`’, then an initializer function called on an allocated argument throws an exception, there should be a ‘`llvm.call.preallocated.teardown`’ in the exception handler to prevent stack leaks.

Following the nesting rules in ‘`llvm.call.preallocated.setup`’, nested calls to ‘`llvm.call.preallocated.setup`’ and ‘`llvm.call.preallocated.teardown`’ are allowed but must be properly nested.

##### Example:

```llvm
    %cs = call token @llvm.call.preallocated.setup(i32 1)
    %x = call ptr @llvm.call.preallocated.arg(token %cs, i32 0) preallocated(i32)
    invoke void @constructor(ptr %x) to label %conta unwind label %contb
conta:
    call void @foo1(ptr preallocated(i32) %x) ["preallocated"(token %cs)]
    ret void
contb:
    %s = catchswitch within none [label %catch] unwind to caller
catch:
    %p = catchpad within %s []
    call void @llvm.call.preallocated.teardown(token %cs)
    ret void
```

LLVM provides intrinsics for a few important standard C/C++ library functions. These intrinsics allow source-language front-ends to pass information about the alignment of the pointer arguments to the code generator, providing opportunity for more efficient code generation.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.abs` on any integer bit width or any vector of integer elements.

```
declare i32 @llvm.abs.i32(i32 <src>, i1 <is_int_min_poison>)
declare <4 x i32> @llvm.abs.v4i32(<4 x i32> <src>, i1 <is_int_min_poison>)
```

##### Overview:

The ‘`llvm.abs`’ family of intrinsic functions returns the absolute value of an argument.

##### Arguments:

The first argument is the value for which the absolute value is to be returned. This argument may be of any integer type or a vector with integer element type. The return type must match the first argument type.

The second argument must be a constant and is a flag to indicate whether the result value of the ‘`llvm.abs`’ intrinsic is a poison value if the first argument is statically or dynamically an `INT_MIN` value.

##### Semantics:

The ‘`llvm.abs`’ intrinsic returns the magnitude (always positive) of the first argument or each element of a vector argument.”. If the first argument is `INT_MIN`, then the result is also `INT_MIN` if `is_int_min_poison == 0` and `poison` otherwise.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.smax` on any integer bit width or any vector of integer elements.

```
declare i32 @llvm.smax.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.smax.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return the larger of `%a` and `%b` comparing the values as signed integers. Vector intrinsics operate on a per-element basis. The larger element of `%a` and `%b` at a given index is returned for that index.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must match the argument type.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.smin` on any integer bit width or any vector of integer elements.

```
declare i32 @llvm.smin.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.smin.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return the smaller of `%a` and `%b` comparing the values as signed integers. Vector intrinsics operate on a per-element basis. The smaller element of `%a` and `%b` at a given index is returned for that index.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must match the argument type.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.umax` on any integer bit width or any vector of integer elements.

```
declare i32 @llvm.umax.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.umax.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return the larger of `%a` and `%b` comparing the values as unsigned integers. Vector intrinsics operate on a per-element basis. The larger element of `%a` and `%b` at a given index is returned for that index.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must match the argument type.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.umin` on any integer bit width or any vector of integer elements.

```
declare i32 @llvm.umin.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.umin.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return the smaller of `%a` and `%b` comparing the values as unsigned integers. Vector intrinsics operate on a per-element basis. The smaller element of `%a` and `%b` at a given index is returned for that index.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must match the argument type.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.scmp` on any integer bit width or any vector of integer elements.

```
declare i2 @llvm.scmp.i2.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.scmp.v4i32.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return `-1` if `%a` is signed less than `%b`, `0` if they are equal, and `1` if `%a` is signed greater than `%b`. Vector intrinsics operate on a per-element basis.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must be at least as wide as `i2`, to hold the three possible return values.

##### Syntax:

This is an overloaded intrinsic. You can use `@llvm.ucmp` on any integer bit width or any vector of integer elements.

```
declare i2 @llvm.ucmp.i2.i32(i32 %a, i32 %b)
declare <4 x i32> @llvm.ucmp.v4i32.v4i32(<4 x i32> %a, <4 x i32> %b)
```

##### Overview:

Return `-1` if `%a` is unsigned less than `%b`, `0` if they are equal, and `1` if `%a` is unsigned greater than `%b`. Vector intrinsics operate on a per-element basis.

##### Arguments:

The arguments (`%a` and `%b`) may be of any integer type or a vector with integer element type. The argument types must match each other, and the return type must be at least as wide as `i2`, to hold the three possible return values.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memcpy` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memcpy.p0.p0.i32(ptr <dest>, ptr <src>,
                                    i32 <len>, i1 <isvolatile>)
declare void @llvm.memcpy.p0.p0.i64(ptr <dest>, ptr <src>,
                                    i64 <len>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.memcpy.*`’ intrinsics copy a block of memory from the source location to the destination location.

Note that, unlike the standard libc function, the `llvm.memcpy.*` intrinsics do not return a value, takes extra isvolatile arguments and the pointers can be in specified address spaces.

##### Arguments:

The first argument is a pointer to the destination, the second is a pointer to the source. The third argument is an integer argument specifying the number of bytes to copy, and the fourth is a boolean indicating a volatile access.

The align parameter attribute can be provided for the first and second arguments.

If the `isvolatile` parameter is `true`, the `llvm.memcpy` call is a volatile operation. The detailed access behavior is not very cleanly specified and it is unwise to depend on it.

##### Semantics:

The ‘`llvm.memcpy.*`’ intrinsics copy a block of memory from the source location to the destination location, which must either be equal or non-overlapping. It copies “len” bytes of memory over. If the argument is known to be aligned to some boundary, this can be specified as an attribute on the argument.

If `<len>` is 0, it is no-op modulo the behavior of attributes attached to the arguments. If `<len>` is not a well-defined value, the behavior is undefined. If `<len>` is not zero, both `<dest>` and `<src>` should be well-defined, otherwise the behavior is undefined.

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.memcpy.inline` on any integer bit width and for different address spaces. Not all targets support all bit widths however.

```
declare void @llvm.memcpy.inline.p0.p0.i32(ptr <dest>, ptr <src>,
                                           i32 <len>, i1 <isvolatile>)
declare void @llvm.memcpy.inline.p0.p0.i64(ptr <dest>, ptr <src>,
                                           i64 <len>, i1 <isvolatile>)
```

##### Overview:

The ‘`llvm.memcpy.inline.*`’ intrinsics copy a block of memory from the source location to the destination location and guarantees that no external functions are called.
