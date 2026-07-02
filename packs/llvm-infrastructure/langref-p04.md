---
title: "LLVM Language Reference Manual (part 4/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 4/20
---

# LLVM Language Reference Manual

```llvm
; The marker instruction and a runtime function call are inserted after the call
; to @foo.
call ptr @foo() [ "clang.arc.attachedcall"(ptr @objc_retainAutoreleasedReturnValue) ]
call ptr @foo() [ "clang.arc.attachedcall"(ptr @objc_unsafeClaimAutoreleasedReturnValue) ]
```

The operand bundle is needed to ensure the call is immediately followed by the marker instruction and the ObjC runtime call in the final output.

Pointer Authentication operand bundles are characterized by the `"ptrauth"` operand bundle tag. They are described in the Pointer Authentication document.

A `"kcfi"` operand bundle on an indirect call indicates that the call will be preceded by a runtime type check, which validates that the call target is prefixed with a type identifier that matches the operand bundle attribute. For example:

```llvm
call void %0() ["kcfi"(i32 1234)]
```

Clang emits KCFI operand bundles and the necessary metadata with `-fsanitize=kcfi`.

A “convergencectrl” operand bundle is only valid on a `convergent` operation. When present, the operand bundle must contain exactly one value of token type. See the Convergent Operation Semantics document for details.

A `"deactivation-symbol"` operand bundle is valid on the following instructions (AArch64 only):

- Call to a normal function with `notail` attribute and a first argument and return value of type `ptr`.
- Call to `llvm.ptrauth.sign` or `llvm.ptrauth.auth` intrinsics.

This operand bundle specifies that if the deactivation symbol is defined to a valid value for the target, the marked instruction will return the value of its first argument instead of calling the specified function or intrinsic. This is achieved with `PATCHINST` relocations on the target instructions (see the AArch64 psABI for details).

Modules may contain “module-level inline asm” blocks, which corresponds to the GCC “file scope inline asm” blocks. These blocks are internally concatenated by LLVM and treated as a single unit, but may be separated in the `.ll` file if desired. The syntax is very simple:

```llvm
module asm "inline asm code goes here"
module asm "more can go here"
```

The strings can contain any character by escaping non-printable characters. The escape sequence used is simply “\xx” where “xx” is the two digit hex code for the number.

Note that the assembly string *must* be parseable by LLVM’s integrated assembler (unless it is disabled), even when emitting a `.s` file.

A module may specify a target-specific data layout string that specifies how data is to be laid out in memory. The syntax for the data layout is simply:

```llvm
target datalayout = "layout specification"
```

The *layout specification* consists of a list of specifications separated by the minus sign character (‘-‘). Each specification starts with a letter and may include other information after the letter to define some aspect of the data layout. The specifications accepted are as follows:

**`E`**

Specifies that the target lays out data in big-endian form. That is, the bits with the most significance have the lowest address location.

**`e`**

Specifies that the target lays out data in little-endian form. That is, the bits with the least significance have the lowest address location.

**`S<size>`**

Specifies the natural alignment of the stack in bits. Alignment promotion of stack variables is limited to the natural stack alignment to avoid dynamic stack realignment. If omitted, the natural stack alignment defaults to “unspecified”, which does not prevent any alignment promotions.

**`P<address space>`**

Specifies the address space that corresponds to program memory. Harvard architectures can use this to specify what space LLVM should place things such as functions into. If omitted, the program memory space defaults to the default address space of 0, which corresponds to a Von Neumann architecture that has code and data in the same space.

**`G<address space>`**

Specifies the address space to be used by default when creating global variables. If omitted, the globals address space defaults to the default address space 0. Note: variable declarations without an address space are always created in address space 0, this property only affects the default value to be used when creating globals without additional contextual information (e.g., in LLVM passes).

**`A<address space>`**

Specifies the address space of objects created by ‘`alloca`’. Defaults to the default address space of 0.

**`p[<flags>][<as>][(<name>)]:<size>:<abi>[:<pref>[:<idx>]]`**

This specifies the properties of a pointer in address space `as`. The `<size>` parameter specifies the size of the bitwise representation. For non-integral pointers the representation size may be larger than the address width of the underlying address space (e.g., to accommodate additional metadata). The alignment requirements are specified via the `<abi>` and `<pref>`erred alignments parameters. The fourth parameter `<idx>` is the size of the index that used for address calculations such as getelementptr. It must be less than or equal to the pointer size. If not specified, the default index size is equal to the pointer size. The index size also specifies the width of addresses in this address space. All sizes are in bits. The address space, `<as>`, is optional, and if not specified, denotes the default address space 0. The value of `<as>` must be in the range [1,2^24). The optional `<flags>` are used to specify properties of pointers in this address space: the character `u` marks pointers as having an unstable representation, and `e` marks pointers having external state. See Non-Integral Pointer Types. Additionally, the null pointer bit representation can be specified: `z` indicates it is all-zeros, and `o` indicates it is all-ones. At most one of `z` or `o` may be specified. If neither `z` nor `o` is specified, the null pointer bit representation defaults to all-zeros. The `<name>` is an optional name of that address space, surrounded by `(` and `)`. If the name is specified, it must be unique to that address space and cannot be `A`, `G`, or `P` which are pre-defined names used to denote alloca, global, and program address space respectively.

**`i<size>:<abi>[:<pref>]`**

This specifies the alignment for an integer type of a given bit `<size>`. The value of `<size>` must be in the range [1,2^24). For `i8`, the `<abi>` value must equal 8, that is, `i8` must be naturally aligned.

**`v<size>:<abi>[:<pref>]`**

This specifies the alignment for a vector type of a given bit `<size>`. The value of `<size>` must be in the range [1,2^24).

**`ve`**

Specifies that vectors are element-aligned by default, rather than having natural alignment.

**`f<size>:<abi>[:<pref>]`**

This specifies the alignment for a floating-point type of a given bit `<size>`. Only values of `<size>` that are supported by the target will work. 32 (float) and 64 (double) are supported on all targets; 80 or 128 (different flavors of long double) are also supported on some targets. The value of `<size>` must be in the range [1,2^24).

**`a:<abi>[:<pref>]`**

This specifies the alignment for an object of aggregate type. In addition to the usual requirements for alignment values, the value of `<abi>` can also be zero, which means one byte alignment.

**`F<type><abi>`**

This specifies the alignment for function pointers. The options for `<type>` are:

- `i`: The alignment of function pointers is independent of the alignment of functions, and is a multiple of `<abi>`.
- `n`: The alignment of function pointers is a multiple of the explicit alignment specified on the function, and is a multiple of `<abi>`.

**`m:<mangling>`**

If present, specifies that llvm names are mangled in the output. Symbols prefixed with the mangling escape character `\01` are passed through directly to the assembler without the escape character. The mangling style options are

- `e`: ELF mangling: Private symbols get a `.L` prefix.
- `l`: GOFF mangling: Private symbols get a `@` prefix.
- `m`: Mips mangling: Private symbols get a `$` prefix.
- `o`: Mach-O mangling: Private symbols get `L` prefix. Other symbols get a `_` prefix.
- `x`: Windows x86 COFF mangling: Private symbols get the usual prefix. Regular C symbols get a `_` prefix. Functions with `__stdcall`, `__fastcall`, and `__vectorcall` have custom mangling that appends `@N` where N is the number of bytes used to pass parameters. C++ symbols starting with `?` are not mangled in any way.
- `w`: Windows COFF mangling: Similar to `x`, except that normal C symbols do not receive a `_` prefix.
- `a`: XCOFF mangling: Private symbols get a `L..` prefix.

**`n<size1>:<size2>:<size3>...`**

This specifies a set of native integer widths for the target CPU in bits. For example, it might contain `n32` for 32-bit PowerPC, `n32:64` for PowerPC 64, or `n8:16:32:64` for X86-64. Elements of this set are considered to support most general arithmetic operations efficiently.

**`ni:<address space0>:<address space1>:<address space2>...`**

This marks pointer types with the specified address spaces as unstable. The `0` address space cannot be specified as non-integral. It is only supported for backwards compatibility, the flags of the `p` specifier should be used instead for new code.

`<abi>` is a lower bound on what is required for a type to be considered aligned. This is used in various places, such as:

- The alignment for loads and stores if none is explicitly given.
- The alignment used to compute struct layout.
- The alignment used to compute allocation sizes and thus `getelementptr` offsets.
- The alignment below which accesses are considered underaligned.

`<pref>` allows providing a more optimal alignment that should be used when possible, primarily for `alloca` and the alignment of global variables. It is an optional value that must be greater than or equal to `<abi>`. If omitted, the preceding `:` should also be omitted and `<pref>` will be equal to `<abi>`.

Unless explicitly stated otherwise, every alignment specification is provided in bits and must be in the range [1,2^16). The value must be a power of two times the width of a byte (i.e., `align = 8 * 2^N`).

When constructing the data layout for a given target, LLVM starts with a default set of specifications which are then (possibly) overridden by the specifications in the `datalayout` keyword. The default specifications are given in this list:

- `e` - little endian
- `p:64:64:64` - 64-bit pointers with 64-bit alignment.
- `p[n]:64:64:64` - Other address spaces are assumed to be the same as the default address space.
- `S0` - natural stack alignment is unspecified
- `i8:8:8` - i8 is 8-bit (byte) aligned as mandated
- `i16:16:16` - i16 is 16-bit aligned
- `i32:32:32` - i32 is 32-bit aligned
- `i64:32:64` - i64 has ABI alignment of 32-bits but preferred alignment of 64-bits
- `f16:16:16` - half is 16-bit aligned
- `f32:32:32` - float is 32-bit aligned
- `f64:64:64` - double is 64-bit aligned
- `f128:128:128` - quad is 128-bit aligned
- `v64:64:64` - 64-bit vector is 64-bit aligned
- `v128:128:128` - 128-bit vector is 128-bit aligned
- `a:0:64` - aggregates are 64-bit aligned

When LLVM is determining the alignment for a given type, it uses the following rules:

1. If the type sought is an exact match for one of the specifications, that specification is used.
2. If no match is found, and the type sought is an integer type, then the smallest integer type that is larger than the bitwidth of the sought type is used. If none of the specifications are larger than the bitwidth then the largest integer type is used. For example, given the default specifications above, the i7 type will use the alignment of i8 (next largest) while both i65 and i256 will use the alignment of i64 (largest specified).

The function of the data layout string may not be what you expect. Notably, this is not a specification from the frontend of what alignment the code generator should use.

Instead, if specified, the target data layout is required to match what the ultimate *code generator* expects. This string is used by the mid-level optimizers to improve code, and this only works if it matches what the ultimate code generator uses. There is no way to generate IR that does not embed this target-specific detail into the IR. If you don’t specify the string, the default specifications will be used to generate a Data Layout and the optimization phases will operate accordingly and introduce target specificity into the IR with respect to these default specifications.

A module may specify a target triple string that describes the target host. The syntax for the target triple is simply:

```llvm
target triple = "x86_64-apple-macosx10.7.0"
```

The *target triple* string consists of a series of identifiers delimited by the minus sign character (‘-‘). The canonical forms are:

```
ARCHITECTURE-VENDOR-OPERATING_SYSTEM
ARCHITECTURE-VENDOR-OPERATING_SYSTEM-ENVIRONMENT
```

This information is passed along to the backend so that it generates code for the proper architecture. It’s possible to override this on the command line with the `-mtriple` command-line option.

An allocated object, memory object, or simply object, is a region of a memory space that is reserved by a memory allocation such as alloca, heap allocation calls, and global variable definitions. Once it is allocated, the bytes stored in the region can only be read or written through a pointer that is based on the allocation value. If a pointer that is not based on the object tries to read or write to the object, it is undefined behavior.

The following properties hold for all allocated objects, otherwise the behavior is undefined:

- no allocated object may cross the unsigned address space boundary (including the pointer after the end of the object),
- the size of all allocated objects must be non-negative and not exceed the largest signed integer that fits into the index type.

Allocated objects that are created with operations recognized by LLVM (such as alloca, heap allocation functions marked as such, and global variables) may *not* change their size. (`realloc`-style operations do not change the size of an existing allocated object; instead, they create a new allocated object. Even if the object is at the same location as the old one, old pointers cannot be used to access this new object.) However, allocated objects can also be created by means not recognized by LLVM, e.g., by directly calling `mmap`. Those allocated objects are allowed to grow to the right (i.e., keeping the same base address, but increasing their size) while maintaining the validity of existing pointers, as long as they always satisfy the properties described above. Currently, allocated objects are not permitted to grow to the left or to shrink, nor can they have holes.

A lifetime of an allocated object is a property that decides its accessibility. Unless stated otherwise, an allocated object is alive since its allocation, and dead after its deallocation. It is undefined behavior to access an allocated object that isn’t alive, but operations that don’t dereference it such as getelementptr, ptrtoint and icmp return a valid result. This explains code motion of these instructions across operations that impact the object’s lifetime. A stack object’s lifetime can be explicitly specified using llvm.lifetime.start and llvm.lifetime.end intrinsic function calls.

As an exception to the above, loading from a stack object outside its lifetime is not undefined behavior and returns a poison value instead. Storing to it is still undefined behavior.

Any memory access must be done through a pointer value associated with an address range of the memory access, otherwise the behavior is undefined. Pointer values are associated with address ranges according to the following rules:

- A pointer value is associated with the addresses associated with any value it is *based* on.
- An address of a global variable is associated with the address range of the variable’s storage.
- The result value of an allocation instruction is associated with the address range of the allocated storage.
- A null pointer in the default address-space is associated with no address.
- An undef value in *any* address-space is associated with no address.
- An integer constant other than zero or a pointer value returned from a function not defined within LLVM may be associated with address ranges allocated through mechanisms other than those provided by LLVM. Such ranges shall not overlap with any ranges of addresses allocated by mechanisms provided by LLVM.

A pointer value is *based* on another pointer value according to the following rules:

- A pointer value formed from a scalar `getelementptr` operation is *based* on the pointer-typed operand of the `getelementptr`.
- The pointer in lane *l* of the result of a vector `getelementptr` operation is *based* on the pointer in lane *l* of the vector-of-pointers-typed operand of the `getelementptr`.
- The result value of a `bitcast` is *based* on the operand of the `bitcast`.
- A pointer value formed by an `inttoptr` is *based* on all pointer values that contribute (directly or indirectly) to the computation of the pointer’s value.
- The “*based* on” relationship is transitive.

Note that this definition of *“based”* is intentionally similar to the definition of *“based”* in C99, though it is slightly weaker.

LLVM IR does not associate types with memory. The result type of a `load` merely indicates the size and alignment of the memory from which to load, as well as the interpretation of the value. The first operand type of a `store` similarly only indicates the size and alignment of the store.

Consequently, type-based alias analysis, aka TBAA, aka `-fstrict-aliasing`, is not applicable to general unadorned LLVM IR. Metadata may be used to encode additional information which specialized optimization passes may use to implement type-based alias analysis.

Given a function call and a pointer that is passed as an argument or stored in memory before the call, the call may capture two components of the pointer:

> - The address of the pointer, which is its integral value. This also includes parts of the address or any information about the address, including the fact that it does not equal one specific value. We further distinguish whether only the fact that the address is/isn’t null is captured.
> - The provenance of the pointer, which is the ability to perform memory accesses through the pointer, in the sense of the pointer aliasing rules. We further distinguish whether only read accesses are allowed, or both reads and writes.

These two cases are discussed in more detail in the following.

If an argument does not capture the provenance of the pointer, accesses that are based on the argument and are performed after the function returns (or unwinds) cause undefined behavior. In the case where only read provenance is captured, only stores cause undefined behavior.

More formally, an argument that does not capture provenance effectively provides the callee a new pointer with the same address and a derived provenance, where the derived provenance initially has the same permissions as the original, but all access permissions are removed once the function returns (or unwinds). Or in the case of only capturing read provenance, the permissions are changed to only allow read accesses.

This means that the following code is well-defined in isolation:

```llvm
define void @f(ptr captures(address) %a, ptr %b) {
  store ptr %a, ptr %b
  ret void
}
```

Even though the pointer is stored in another location that persists past the return of the function, this does not cause undefined behavior by itself. It depends on whether/how the pointer will be used in the future.

```llvm
call void @f(ptr captures(address) %a, ptr %b)
%a2 = load ptr, ptr %b ; This is still well-defined
load i64, ptr %a2 ; This causes undefined behavior
```

In this example, the persisted pointer is accessed after the return of the function, which causes undefined behavior.

```llvm
call void @f(ptr captures(address, read_provenance) %a, ptr %b)
%a2 = load ptr, ptr %b
load i64, ptr %a2 ; This is still well-defined
store i64 0, ptr %a2 ; This causes undefined behavior
```

In this example, we additionally declare that `read_provenance` is captured. This means that the `load` after the function return is still well-defined, while the store causes undefined behavior.

The address of the pointer is considered to be captured if the function can exhibit different observable behavior based on the address of the pointer.

For example, the following function captures the address of `%a`, because it will return a different value if the address has a specific value:

```llvm
@glb = global i8 0

define i1 @f(ptr %a) {
  %c = icmp eq ptr %a, @glb
  ret i1 %c
}
```

The function does not capture the provenance of the pointer, because the `icmp` instruction only operates on the pointer address.

Even if the function contains a comparison on the pointer address, this does not necessarily mean that it captures the address:

```llvm
define void @my_memmove(
    ptr captures(none) %dst, ptr captures(none) %src, i64 %size
) {
  %cmp = icmp ult ptr %dst, %src
  br i1 %cmp, label %perform_forward_copy, label %perform_backward_copy

  ; ...
}
```

While the implementation differs based on the addresses of the arguments, the observable behavior stays the same in both branches. A common case where this occurs are runtime aliasing checks for loop versioning.

We can further say that the capture only occurs through a specific location. In the following example, the pointer (both address and provenance) is captured through the return value only:

```llvm
define ptr @f(ptr %a) {
  %gep = getelementptr i8, ptr %a, i64 4
  ret ptr %gep
}
```

However, we always consider direct inspection of the pointer address (e.g., using `ptrtoint`) to be location-independent. The following example is *not* considered a return-only capture, even though the `ptrtoint` ultimately only contributes to the return value:

```llvm
@lookup = constant [4 x i8] [i8 0, i8 1, i8 2, i8 3]

define ptr @f(ptr %a) {
  %a.addr = ptrtoint ptr %a to i64
  %mask = and i64 %a.addr, 3
  %gep = getelementptr i8, ptr @lookup, i64 %mask
  ret ptr %gep
}
```

This definition is chosen to allow capture analysis to continue with the return value in the usual fashion.

The definitions given above are permissive to facilitate frontend-driven annotations based on language semantics. As inference generally cannot know how pointers will be used after the function returns, it needs to make conservative assumptions. Here is an example set of rules that could be used to infer `captures`:

> - Volatile memory accesses capture the address of the pointer.
> - getelementptr, bitcast, addrspacecast, select, phi: Do not capture anything.
> - load, va_arg: Do not capture anything (unless volatile).
> - icmp, ptrtoaddr: Captures only address.
> - ptrtoint: Captures address and provenance.
> - call/invoke: Depends on `captures` on arguments. The callee is never captured.
> - store, atomicrmw, cmpxchg: Capture the address and provenance of the value operand. Do not capture the pointer operand (unless volatile).
> - Other (including insertvalue and insertelement): Conservatively assume address and provenance are captured.

Certain memory accesses, such as load’s, store’s, and llvm.memcpy’s may be marked `volatile`. The optimizers must not change the number of volatile operations or change their order of execution relative to other volatile operations. The optimizers *may* change the order of volatile operations relative to non-volatile operations. This is not Java’s “volatile” and has no cross-thread synchronization behavior.

A volatile load or store may have additional target-specific semantics. Any volatile operation can have side effects, and any volatile operation can read and/or modify state which is not accessible via a regular load or store in this module. Volatile operations may use addresses which do not point to memory (like MMIO registers). This means the compiler may not use a volatile operation to prove a non-volatile access to that address has defined behavior. This includes addresses typically forbidden, such as the pointer with bit-value 0.

The allowed side-effects for volatile accesses are limited. If a non-volatile store to a given address would be legal, a volatile operation may modify the memory at that address. A volatile operation may not modify any other memory accessible by the module being compiled. A volatile operation may not call any code in the current module.

In general (without target-specific context), the address space of a volatile operation may not be changed. Different address spaces may have different trapping behavior when dereferencing an invalid pointer.

Volatile operations are permitted to trap. The compiler may not assume that execution will continue after a volatile operation.

IR-level volatile loads and stores cannot safely be optimized into `llvm.memcpy` or `llvm.memmove` intrinsics even when those intrinsics are flagged volatile. Likewise, the backend should never split or merge target-legal volatile load/store instructions. Similarly, IR-level volatile loads and stores cannot change from integer to floating-point or vice versa.

Rationale

Platforms may rely on volatile loads and stores of natively supported data width to be executed as single instruction. For example, in C this holds for an l-value of volatile primitive type with native hardware support, but not necessarily for aggregate types. The frontend upholds these expectations, which are intentionally unspecified in the IR. The rules above ensure that IR transformations do not violate the frontend’s contract with the language.

The LLVM IR does not define any way to start parallel threads of execution or to register signal handlers. Nonetheless, there are platform-specific ways to create them, and we define LLVM IR’s behavior in their presence. This model is inspired by the C++ memory model.

For a more informal introduction to this model, see the LLVM Atomic Instructions and Concurrency Guide.

We define a *happens-before* partial order as the least partial order that

- Is a superset of single-thread program order, and
- When `a` *synchronizes-with* `b`, includes an edge from `a` to `b`. *Synchronizes-with* pairs are introduced by platform-specific techniques, like pthread locks, thread creation, thread joining, etc., and by atomic instructions. (See also Atomic Memory Ordering Constraints).

Note that program order does not introduce *happens-before* edges between a thread and signals executing inside that thread.

Every (defined) read operation (load instructions, memcpy, atomic loads/read-modify-writes, etc.) R reads a series of bytes written by (defined) write operations (store instructions, atomic stores/read-modify-writes, memcpy, etc.). For the purposes of this section, initialized globals are considered to have a write of the initializer which is atomic and happens before any other read or write of the memory in question. For each byte of a read R, Rbyte may see any write to the same byte, except:

- If write1 happens before write2, and write2 happens before Rbyte, then Rbyte does not see write1.
- If Rbyte happens before write3, then Rbyte does not see write3.

Given that definition, Rbyte is defined as follows:

- If R is volatile, the result is target-dependent. (Volatile is supposed to give guarantees which can support `sig_atomic_t` in C/C++, and may be used for accesses to addresses that do not behave like normal memory. It does not generally provide cross-thread synchronization.)
- Otherwise, if there is no write to the same byte that happens before Rbyte, Rbyte returns `undef` for that byte.
- Otherwise, if Rbyte may see exactly one write, Rbyte returns the value written by that write.
- Otherwise, if R is atomic, and all the writes Rbyte may see are atomic, it chooses one of the values written. See the Atomic Memory Ordering Constraints section for additional constraints on how the choice is made. Targets may impose additional requirements on R and the writes it may see based on their `syncscope`.
- Otherwise Rbyte returns `undef`.

R returns the value composed of the series of bytes it read. This implies that some bytes within the value may be `undef` **without** the entire value being `undef`. Note that this only defines the semantics of the operation; it doesn’t mean that targets will emit more than one instruction to read the series of bytes.

Note that in cases where none of the atomic intrinsics are used, this model places only one restriction on IR transformations on top of what is required for single-threaded execution: introducing a store to a byte which might not otherwise be stored is not allowed in general. (Specifically, in the case where another thread might write to and read from an address, introducing a store can change a load that may see exactly one write into a load that may see multiple writes.)

Atomic instructions (cmpxchg, atomicrmw, fence, atomic load, and atomic store) take ordering parameters that determine which other atomic instructions on the same address they *synchronize with*. These semantics implement the Java or C++ memory models; if these descriptions aren’t precise enough, check those specs (see spec references in the atomics guide). fence instructions treat these orderings somewhat differently since they don’t take an address. See that instruction’s documentation for details.

For a simpler introduction to the ordering constraints, see the LLVM Atomic Instructions and Concurrency Guide.

**`unordered`**

The set of values that can be read is governed by the happens-before partial order. A value cannot be read unless some operation wrote it. This is intended to provide a guarantee strong enough to model Java’s non-volatile shared variables. This ordering cannot be specified for read-modify-write operations; it is not strong enough to make them atomic in any interesting way.

**`monotonic`**

In addition to the guarantees of `unordered`, there is a single total order for modifications by `monotonic` operations on each address. All modification orders must be compatible with the happens-before order. There is no guarantee that the modification orders can be combined to a global total order for the whole program (and this often will not be possible). If the read in an atomic read-modify-write operation M (cmpxchg and atomicrmw) reads from a `monotonic` (or stronger) write W, W must be immediately before M in the address’s modification order. If one atomic read happens before another atomic read of the same address and both are at least `monotonic`, the later read must not see an earlier value in the address’s modification order. This disallows reordering of `monotonic` (or stronger) operations on the same address. If an address is written `monotonic`-ally by one thread, and other threads `monotonic`-ally read that address repeatedly, the other threads must eventually see the write. This corresponds to the C/C++ `memory_order_relaxed`.

**`acquire`**

In addition to the guarantees of `monotonic`, a *synchronizes-with* edge may be formed with a `release` operation. This is intended to model C/C++’s `memory_order_acquire`.

**`release`**

In addition to the guarantees of `monotonic`, if this operation writes a value which is subsequently read by an `acquire` operation, it *synchronizes-with* that operation. Furthermore, this occurs even if the value written by a `release` operation has been modified by a read-modify-write operation before being read. (Such a set of operations comprises a *release sequence*). This corresponds to the C/C++ `memory_order_release`.

**`acq_rel` (acquire+release)**

Acts as both an `acquire` and `release` operation on its address. This corresponds to the C/C++ `memory_order_acq_rel`.

**`seq_cst` (sequentially consistent)**

In addition to the guarantees of `acq_rel` (`acquire` for an operation that only reads, `release` for an operation that only writes), there is a global total order on all sequentially-consistent operations on all addresses. If an address is only accessed through sequentially-consistent operations, each sequentially-consistent read of that address sees the last preceding write to the same address in this global order. This corresponds to the C/C++ `memory_order_seq_cst` and Java `volatile`.

Note: this global total order is *not* guaranteed to be fully consistent with the *happens-before* partial order if non-`seq_cst` accesses are involved. See the C++ standard [atomics.order] section for more details on the exact guarantees.

If an atomic operation is marked `syncscope("singlethread")`, it only *synchronizes with* other operations running in the same thread (for example, in signal handlers) and it is related in the seq_cst order and the monotonic modification order with other operations in the same thread.

If an atomic operation is marked `syncscope("<target-scope>")`, where `<target-scope>` is a target-specific synchronization scope, then it is target-dependent if it *synchronizes with* other operations and if it is related with other operations in the seq_cst order and the monotonic modification order.

Otherwise, an atomic operation that is not marked `syncscope("singlethread")` or `syncscope("<target-scope>")` *synchronizes with* and is related in the seq_cst order and the monotonic modification order with other operations that are not marked `syncscope("singlethread")` or `syncscope("<target-scope>")`.

The default LLVM floating-point environment assumes that traps are disabled and status flags are not observable. Therefore, floating-point math operations do not have side effects and may be speculated freely. Results assume the round-to-nearest rounding mode, and subnormals are assumed to be preserved.

Running LLVM code in an environment where these assumptions are not met typically leads to undefined behavior. The `strictfp` and denormal_fpenv attributes as well as Constrained Floating-Point Intrinsics can be used to weaken LLVM’s assumptions and ensure defined behavior in non-default floating-point environments; see their respective documentation for details.

A floating-point NaN value consists of a sign bit, a quiet/signaling bit, and a payload (which makes up the rest of the mantissa except for the quiet/signaling bit). LLVM assumes that the quiet/signaling bit being set to `1` indicates a quiet NaN (QNaN), and a value of `0` indicates a signaling NaN (SNaN). In the following we will hence just call it the “quiet bit”.

The representation bits of a floating-point value do not mutate arbitrarily; in particular, if there is no floating-point operation being performed, NaN signs, quiet bits, and payloads are preserved.

For the purpose of this section, `bitcast` as well as the following operations are not “floating-point math operations”: `fneg`, `llvm.fabs`, and `llvm.copysign`. These operations act directly on the underlying bit representation and never change anything except possibly for the sign bit.

Floating-point math operations that return a NaN are an exception from the general principle that LLVM implements IEEE 754 semantics. Unless specified otherwise, the following rules apply whenever the IEEE 754 semantics say that a NaN value is returned: the result has a non-deterministic sign; the quiet bit and payload are non-deterministically chosen from the following set of options:

- The quiet bit is set and the payload is all-zero. (“Preferred NaN” case)
- The quiet bit is set and the payload is copied from any input operand that is a NaN. (“Quieting NaN propagation” case)
- The quiet bit and payload are copied from any input operand that is a NaN. (“Unchanged NaN propagation” case)
- The quiet bit is set and the payload is picked from a target-specific set of “extra” possible NaN payloads. The set can depend on the input operand values. This set is empty on x86 and ARM, but can be non-empty on other architectures. (For instance, on wasm, if any input NaN does not have the preferred all-zero payload or any input NaN is an SNaN, then this set contains all possible payloads; otherwise, it is empty. On SPARC, this set consists of the all-one payload.)

In particular, if all input NaNs are quiet (or if there are no input NaNs), then the output NaN is definitely quiet. Signaling NaN outputs can only occur if they are provided as an input value. For example, “fmul SNaN, 1.0” may be simplified to SNaN rather than QNaN. Similarly, if all input NaNs are preferred (or if there are no input NaNs) and the target does not have any “extra” NaN payloads, then the output NaN is guaranteed to be preferred.

Floating-point math operations are allowed to treat all NaNs as if they were quiet NaNs. For example, “pow(1.0, SNaN)” may be simplified to 1.0.

Code that requires different behavior than this should use the Constrained Floating-Point Intrinsics. In particular, constrained intrinsics rule out the “Unchanged NaN propagation” case; they are guaranteed to return a QNaN.

Unfortunately, due to hard-or-impossible-to-fix issues, LLVM violates its own specification on some architectures:

- x86-32 without SSE2 enabled may convert floating-point values to x86_fp80 and back when performing floating-point math operations; this can lead to results with different precision than expected and it can alter NaN values. Since optimizations can make contradicting assumptions, this can lead to arbitrary miscompilations. See issue #44218.
- x86-32 (even with SSE2 enabled) may implicitly perform such a conversion on values returned from a function for some calling conventions. See issue #66803.
- Older MIPS versions use the opposite polarity for the quiet/signaling bit, and LLVM does not correctly represent this. See issue #60796.

This section defines the semantics for core floating-point operations on types that use a format specified by IEEE 754. These types are: `half`, `float`, `double`, and `fp128`, which correspond to the binary16, binary32, binary64, and binary128 formats, respectively. The “core” operations are those defined in section 5 of IEEE 754, which all have corresponding LLVM operations.

The value returned by those operations matches that of the corresponding IEEE 754 operation executed in the default LLVM floating-point environment, except that the behavior of NaN results is instead as specified here. In particular, such a floating-point instruction returning a non-NaN value is guaranteed to always return the same bit-identical result on all machines and optimization levels.

This means that optimizations and backends may not change the observed bitwise result of these operations in any way (unless NaNs are returned), and frontends can rely on these operations providing correctly rounded results as described in the standard.

(Note that this is only about the value returned by these operations; see the floating-point environment section regarding flags and exceptions.)

Various flags, attributes, and metadata can alter the behavior of these operations and thus make them not bit-identical across machines and optimization levels any more: most notably, the fast-math flags as well as the strictfp and denormal_fpenv attributes and fpmath metadata <fpmath-metadata>. See their corresponding documentation for details.

LLVM IR floating-point operations (fneg, fadd, fsub, fmul, fdiv, frem, fcmp, fptrunc, fpext), :ref::*uitofp <i_uitofp>*, :ref::*sitofp <i_sitofp>*, and phi, select, or call instructions that return floating-point types may use the following flags to enable otherwise unsafe floating-point transformations.

**`fast`**

This flag is a shorthand for specifying all fast-math flags at once, and imparts no additional semantics from using all of them.

**`nnan`**

No NaNs - Allow optimizations to assume the arguments and result are not NaN. If an argument is a nan, or the result would be a nan, it produces a poison value instead.

**`ninf`**

No Infs - Allow optimizations to assume the arguments and result are not +/-Inf. If an argument is +/-Inf, or the result would be +/-Inf, it produces a poison value instead.

**`nsz`**

No Signed Zeros - Unless otherwise mentioned, the sign bit of 0.0 or -0.0 input operands can be non-deterministically flipped. This does not imply that -0.0 is poison and/or guaranteed to not exist in the operation.

Note: For phi, select, and call instructions, the following return types are considered to be floating-point types:

- Floating-point scalar or vector types
- Array types (nested to any depth) of floating-point scalar or vector types
- Homogeneous literal struct types of floating-point scalar or vector types

The following flags have rewrite-based semantics. These flags allow expressions, potentially containing multiple non-consecutive instructions, to be rewritten into alternative instructions. When multiple instructions are involved in an expression, it is necessary that all of the instructions have the necessary rewrite-based flag present on them, and the rewritten instructions will generally have the intersection of the flags present on the input instruction.

In the following example, the floating-point expression in the body of `@orig` has `contract` and `reassoc` in common, and thus if it is rewritten into the expression in the body of `@target`, all of the new instructions get those two flags and only those flags as a result. Since the `arcp` is present on only one of the instructions in the expression, it is not present in the transformed expression. Furthermore, this reassociation here is only legal because both the instructions had the `reassoc` flag; if only one had it, it would not be legal to make the transformation.

```llvm
define double @orig(double %a, double %b, double %c) {
  %t1 = fmul contract reassoc double %a, %b
  %val = fmul contract reassoc arcp double %t1, %c
  ret double %val
}

define double @target(double %a, double %b, double %c) {
  %t1 = fmul contract reassoc double %b, %c
  %val = fmul contract reassoc double %a, %t1
  ret double %val
}
```

These rules do not apply to the other fast-math flags. Whether or not a flag like `nnan` is present on any or all of the rewritten instructions is based on whether or not it is possible for said instruction to have a NaN input or output, given the original flags.

**`arcp`**

Allows division to be treated as a multiplication by a reciprocal. Specifically, this permits `a / b` to be considered equivalent to `a * (1.0 / b)` (which may subsequently be susceptible to code motion), and it also permits `a / (b / c)` to be considered equivalent to `a * (c / b)`. Both of these rewrites can be applied in either direction: `a * (c / b)` can be rewritten into `a / (b / c)`.

**`contract`**

Allow floating-point contraction (e.g., fusing a multiply followed by an addition into a fused multiply-and-add). This does not enable reassociation to form arbitrary contractions. For example, `(a*b) + (c*d) + e` can not be transformed into `(a*b) + ((c*d) + e)` to create two fma operations.

**`afn`**

Approximate functions - Allow substitution of approximate calculations for functions (sin, log, sqrt, etc). See floating-point intrinsic definitions for places where this can apply to LLVM’s intrinsic math functions.

**`reassoc`**

Allow algebraically equivalent transformations for floating-point instructions such as reassociation transformations. This may dramatically change results in floating-point.

Use-list directives encode the in-memory order of each use-list, allowing the order to be recreated. `<order-indexes>` is a comma-separated list of indexes that are assigned to the referenced value’s uses. The referenced value’s use-list is immediately sorted by these indexes.

Use-list directives may appear at function scope or global scope. They are not instructions, and have no effect on the semantics of the IR. When they’re at function scope, they must appear after the terminator of the final basic block.

**Syntax:**

```
uselistorder <ty> <value>, { <order-indexes> }
```

**Examples:**

```
define void @foo(i32 %arg1, i32 %arg2) {
entry:
  ; ... instructions ...
bb:
  ; ... instructions ...

  ; At function scope.
  uselistorder i32 %arg1, { 1, 0, 2 }
  uselistorder label %bb, { 1, 0 }
}

; At global scope.
uselistorder ptr @global, { 1, 2, 0 }
uselistorder i32 7, { 1, 0 }
uselistorder i32 (i32) @bar, { 1, 0 }
```

The *source filename* string is set to the original module identifier, which will be the name of the compiled source file when compiling from source through the clang front end, for example. It is then preserved through the IR and bitcode.

This is currently necessary to generate a consistent unique global identifier for local functions used in profile data, which prepends the source file name to the local function name.

The syntax for the source file name is simply:

```
source_filename = "/path/to/source.c"
```

The LLVM type system is one of the most important features of the intermediate representation. Being typed enables a number of optimizations to be performed on the intermediate representation directly, without having to do extra analyses on the side before the transformation. A strong type system makes it easier to read the generated code and enables novel analyses and transformations that are not feasible to perform on normal three address code representations.

**Overview:**

The void type does not represent any value and has no size.

**Syntax:**

```
void
```

**Overview:**

The function type can be thought of as a function signature. It consists of a return type and a list of formal parameter types. The return type of a function type is a void type or first class type — except for label and metadata types.

**Syntax:**

```
<returntype> (<parameter list>)
```

…where ‘`<parameter list>`’ is a comma-separated list of type specifiers. Optionally, the parameter list may include a type `...`, which indicates that the function takes a variable number of arguments. Variable argument functions can access their arguments with the variable argument handling intrinsic functions. ‘`<returntype>`’ is any type except label and metadata.

**Examples:**

| `i32 (i32)` | function taking an `i32`, returning an `i32` |
|---|---|
| `i32 (ptr, ...)` | A vararg function that takes at least one pointer argument and returns an integer. This is the signature for `printf` in LLVM. |
| `{i32, i32} (i32)` | A function taking an `i32`, returning a structure containing two `i32` values |

**Overview:**

Opaque structure types are used to represent structure types that do not have a body specified. This corresponds (for example) to the C notion of a forward declared structure. They can be named (`%X`) or unnamed (`%52`).

It is not possible to create SSA values with an opaque structure type. In practice, this largely limits their use to the value type of external globals.

**Syntax:**

```
%X = type opaque
%52 = type opaque

@g = external global %X
```

The first class types are perhaps the most important. Values of these types are the only ones which can be produced by instructions.

These are the types that are valid in registers from CodeGen’s perspective.

##### Integer Type

**Overview:**

The integer type is a very simple type that simply specifies an arbitrary bit width for the integer type desired. Any bit width from 1 bit to 223(about 8 million) can be specified.

**Syntax:**

```
iN
```

The number of bits the integer will occupy is specified by the `N` value.

###### Examples:
