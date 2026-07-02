---
title: "LLVM Language Reference Manual (part 1/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 1/20
---

# LLVM Language Reference Manual

This document is a reference manual for the LLVM assembly language. LLVM is a Static Single Assignment (SSA) based representation that provides type safety, low-level operations, flexibility, and the capability of representing ‘all’ high-level languages cleanly. It is the common code representation used throughout all phases of the LLVM compilation strategy.

The LLVM code representation is designed to be used in three different forms: as an in-memory compiler IR, as an on-disk bitcode representation (suitable for fast loading by a Just-In-Time compiler), and as a human readable assembly language representation. This allows LLVM to provide a powerful intermediate representation for efficient compiler transformations and analysis, while providing a natural means to debug and visualize the transformations. The three different forms of LLVM are all equivalent. This document describes the human-readable representation and notation.

The LLVM representation aims to be light-weight and low-level while being expressive, typed, and extensible at the same time. It aims to be a “universal IR” of sorts, by being at a low enough level that high-level ideas may be cleanly mapped to it (similar to how microprocessors are “universal IR’s”, allowing many source languages to be mapped to them). By providing type information, LLVM can be used as the target of optimizations: for example, through pointer analysis, it can be proven that a C automatic variable is never accessed outside of the current function, allowing it to be promoted to a simple SSA value instead of a memory location.

It is important to note that this document describes ‘well formed’ LLVM assembly language. There is a difference between what the parser accepts and what is considered ‘well formed’. For example, the following instruction is syntactically okay, but not well formed:

```llvm
%x = add i32 1, %x
```

because the definition of `%x` does not dominate all of its uses. The LLVM infrastructure provides a verification pass that may be used to verify that an LLVM module is well formed. This pass is automatically run by the parser after parsing input assembly and by the optimizer before it outputs bitcode. The violations pointed out by the verifier pass indicate bugs in transformation passes or input to the parser.

LLVM identifiers come in two basic types: global and local. Global identifiers (functions, global variables) begin with the `'@'` character. Local identifiers (register names, types) begin with the `'%'` character. Additionally, there are three different formats for identifiers, for different purposes:

1. Named values are represented as a string of characters with their prefix. For example, `%foo`, `@DivisionByZero`, `%a.really.long.identifier`. The actual regular expression used is ‘`[%@][-a-zA-Z$._][-a-zA-Z$._0-9]*`’. Identifiers that require other characters in their names can be surrounded with quotes. Special characters may be escaped using `"\xx"` where `xx` is the ASCII code for the character in hexadecimal. In this way, any character can be used in a name value, even quotes themselves. The `"\01"` prefix can be used on global values to suppress mangling.
2. Unnamed values are represented as an unsigned numeric value with their prefix. For example, `%12`, `@2`, `%44`.
3. Constants, which are described in the section Constants below.

LLVM requires that values start with a prefix for two reasons: Compilers don’t need to worry about name clashes with reserved words, and the set of reserved words may be expanded in the future without penalty. Additionally, unnamed identifiers allow a compiler to quickly come up with a temporary variable without having to avoid symbol table conflicts.

Reserved words in LLVM are very similar to reserved words in other languages. There are keywords for different opcodes (’`add`’, ‘`bitcast`’, ‘`ret`’, etc…), for primitive type names (’`void`’, ‘`i32`’, etc…), and others. These reserved words cannot conflict with variable names, because none of them start with a prefix character (`'%'` or `'@'`).

Here is an example of LLVM code to multiply the integer variable ‘`%X`’ by 8:

The easy way:

```llvm
%result = mul i32 %X, 8
```

After strength reduction:

```llvm
%result = shl i32 %X, 3
```

And the hard way:

```llvm
%0 = add i32 %X, %X           ; yields i32:%0
%1 = add i32 %0, %0           ; yields i32:%1
%result = add i32 %1, %1
```

This last way of multiplying `%X` by 8 illustrates several important lexical features of LLVM:

1. Comments are delimited with a ‘`;`’ and go until the end of line. Alternatively, comments can start with `/*` and terminate with `*/`.
2. Unnamed temporaries are created when the result of a computation is not assigned to a named value.
3. By default, unnamed temporaries are numbered sequentially (using a per-function incrementing counter, starting with 0). However, when explicitly specifying temporary numbers, it is allowed to skip over numbers. Note that basic blocks and unnamed function parameters are included in this numbering. For example, if the entry basic block is not given a label name and all function parameters are named, then it will get number 0.

It also shows a convention that we follow in this document. When demonstrating instructions, we will follow an instruction with a comment that defines the type and name of value produced.

Strings in LLVM programs are delimited by `"` characters. Within a string, all bytes are treated literally with the exception of `\` characters, which start escapes, and the first `"` character, which ends the string.

There are two kinds of escapes.

- `\\` represents a single `\` character.
- `\` followed by two hexadecimal characters (0-9, a-f, or A-F) represents the byte with the given value (e.g., `\00` represents a null byte).

To represent a `"` character, use `\22`. (`\"` will end the string with a trailing `\`.)

Newlines do not terminate string constants; strings can span multiple lines.

The interpretation of string constants (e.g., their character encoding) depends on context.

LLVM programs are composed of `Module`’s, each of which is a translation unit of the input programs. Each module consists of functions, global variables, and symbol table entries. Modules may be combined together with the LLVM linker, which merges function (and global variable) definitions, resolves forward declarations, and merges symbol table entries. Here is an example of the “hello world” module:

```llvm
; Declare the string constant as a global constant.
@.str = private unnamed_addr constant [13 x i8] c"hello world\0A\00"

; External declaration of the puts function
declare i32 @puts(ptr captures(none)) nounwind

; Definition of main function
define i32 @main() {
  ; Call puts function to write out the string to stdout.
  call i32 @puts(ptr @.str)
  ret i32 0
}

; Named metadata
!0 = !{i32 42, null, !"string"}
!foo = !{!0}
```

This example is made up of a global variable named “`.str`”, an external declaration of the “`puts`” function, a function definition for “`main`” and named metadata “`foo`”.

In general, a module is made up of a list of global values (where both functions and global variables are global values). Global values are represented by a pointer to a memory location (in this case, a pointer to an array of char, and a pointer to a function), and have one of the following linkage types.

All Global Variables and Functions have one of the following types of linkage:

**`private`**

Global values with “`private`” linkage are only directly accessible by objects in the current module. In particular, linking code into a module with a private global value may cause the private to be renamed as necessary to avoid collisions. Because the symbol is private to the module, all references can be updated. This doesn’t show up in any symbol table in the object file.

**`internal`**

Similar to private, but the value shows as a local symbol (`STB_LOCAL` in the case of ELF) in the object file. This corresponds to the notion of the ‘`static`’ keyword in C.

**`available_externally`**

Globals with “`available_externally`” linkage are never emitted into the object file corresponding to the LLVM module. From the linker’s perspective, an `available_externally` global is equivalent to an external declaration. They exist to allow inlining and other optimizations to take place given knowledge of the definition of the global, which is known to be somewhere outside the module. Globals with `available_externally` linkage are allowed to be discarded at will, and allow inlining and other optimizations. This linkage type is only allowed on definitions, not declarations.

**`linkonce`**

Globals with “`linkonce`” linkage are merged with other globals of the same name when linkage occurs. This can be used to implement some forms of inline functions, templates, or other code which must be generated in each translation unit that uses it, but where the body may be overridden with a more definitive definition later. Unreferenced `linkonce` globals are allowed to be discarded. Note that `linkonce` linkage does not actually allow the optimizer to inline the body of this function into callers because it doesn’t know if this definition of the function is the definitive definition within the program or whether it will be overridden by a stronger definition. To enable inlining and other optimizations, use “`linkonce_odr`” linkage.

**`weak`**

“`weak`” linkage has the same merging semantics as `linkonce` linkage, except that unreferenced globals with `weak` linkage may not be discarded. This is used for globals that are declared “weak” in C source code.

**`common`**

“`common`” linkage is most similar to “`weak`” linkage, but they are used for tentative definitions in C, such as “`int X;`” at global scope. Symbols with “`common`” linkage are merged in the same way as `weak symbols`, and they may not be deleted if unreferenced. `common` symbols may not have an explicit section, must have a zero initializer, and may not be marked ‘constant’. Functions and aliases may not have common linkage.

**`appending`**

“`appending`” linkage may only be applied to global variables of pointer to array type. When two global variables with appending linkage are linked together, the two global arrays are appended together. This is the LLVM, typesafe, equivalent of having the system linker append together “sections” with identical names when `.o` files are linked.

Unfortunately this doesn’t correspond to any feature in `.o` files, so it can only be used for variables like `llvm.global_ctors` which llvm interprets specially.

**`extern_weak`**

The semantics of this linkage follow the ELF object file model: the symbol is weak until linked, if not linked, the symbol becomes null instead of being an undefined reference.

**`linkonce_odr`, `weak_odr`**

The `odr` suffix indicates that all globals defined with the given name are equivalent, along the lines of the C++ “one definition rule” (“ODR”). Informally, this means we can inline functions and fold loads of constants.

Formally, use the following definition: when an `odr` function is called, one of the definitions is non-deterministically chosen to run. For `odr` variables, if any byte in the value is not equal in all initializers, that byte is a poison value. For aliases and ifuncs, apply the rule for the underlying function or variable.

These linkage types are otherwise the same as their non-`odr` versions.

**`external`**

If none of the above identifiers are used, the global is externally visible, meaning that it participates in linkage and can be used to resolve external symbol references.

It is illegal for a global variable or function *declaration* to have any linkage type other than `external` or `extern_weak`.

LLVM functions, calls and invokes can all have an optional calling convention specified for the call. The calling convention of any pair of dynamic caller/callee must match, or the behavior of the program is undefined. The following calling conventions are supported by LLVM, and more may be added in the future:

**“`ccc`” - The C calling convention**

This calling convention (the default if no other calling convention is specified) matches the target C calling conventions. This calling convention supports varargs function calls and tolerates some mismatch in the declared prototype and implemented declaration of the function (as does normal C).

**“`fastcc`” - The fast calling convention**

This calling convention attempts to make calls as fast as possible (e.g., by passing things in registers). This calling convention allows the target to use whatever tricks it wants to produce fast code for the target, without having to conform to an externally specified ABI (Application Binary Interface). Targets may use different implementations according to different features. In this case, a TTI interface `useFastCCForInternalCall` must return false when any caller functions and the callee belong to different implementations. Tail calls can only be optimized when this, the tailcc, the GHC or the HiPE convention is used. This calling convention does not support varargs and requires the prototype of all callees to exactly match the prototype of the function definition.

**“`coldcc`” - The cold calling convention**

This calling convention attempts to make code in the caller as efficient as possible under the assumption that the call is not commonly executed. As such, these calls often preserve all registers so that the call does not break any live ranges in the caller side. This calling convention does not support varargs and requires the prototype of all callees to exactly match the prototype of the function definition. Furthermore the inliner doesn’t consider such function calls for inlining.

**“`ghccc`” - GHC convention**

This calling convention has been implemented specifically for use by the Glasgow Haskell Compiler (GHC). It passes everything in registers, going to extremes to achieve this by disabling callee save registers. This calling convention should not be used lightly but only for specific situations such as an alternative to the *register pinning* performance technique often used when implementing functional programming languages. At the moment only X86, AArch64, and RISCV support this convention. The following limitations exist:

- On *X86-32* only up to 4 bit type parameters are supported. No floating-point types are supported.
- On *X86-64* only up to 10 bit type parameters and 6 floating-point parameters are supported.
- On *AArch64* only up to 4 32-bit floating-point parameters, 4 64-bit floating-point parameters, and 10 bit type parameters are supported.
- *RISCV64* only supports up to 11 bit type parameters, 4 32-bit floating-point parameters, and 4 64-bit floating-point parameters.

This calling convention supports tail call optimization but requires both the caller and callee to use it.

**“`cc 11`” - The HiPE calling convention**

This calling convention has been implemented specifically for use by the High-Performance Erlang (HiPE) compiler, *the* native code compiler of the Ericsson’s Open Source Erlang/OTP system. It uses more registers for argument passing than the ordinary C calling convention and defines no callee-saved registers. The calling convention properly supports tail call optimization but requires that both the caller and the callee use it. It uses a *register pinning* mechanism, similar to GHC’s convention, for keeping frequently accessed runtime components pinned to specific hardware registers. At the moment only X86 supports this convention (both 32 and 64 bit).

**“`anyregcc`” - Dynamic calling convention for code patching**

This is a special convention that supports patching an arbitrary code sequence in place of a call site. This convention forces the call arguments into registers but allows them to be dynamically allocated. This can currently only be used with calls to `llvm.experimental.patchpoint` because only this intrinsic records the location of its arguments in a side table. See Stack maps and patch points in LLVM.

**“`preserve_mostcc`” - The *PreserveMost* calling convention**

This calling convention attempts to make the code in the caller as unintrusive as possible. This convention behaves identically to the *C* calling convention on how arguments and return values are passed, but it uses a different set of caller/callee-saved registers. This alleviates the burden of saving and recovering a large register set before and after the call in the caller. If the arguments are passed in callee-saved registers, then they will be preserved by the callee across the call. This doesn’t apply for values returned in callee-saved registers.

- On X86-64 the callee preserves all general purpose registers, except for R11 and return registers, if any. R11 can be used as a scratch register. The treatment of floating-point registers (XMMs/YMMs) matches the OS’s C calling convention: on most platforms, they are not preserved and need to be saved by the caller, but on Windows, xmm6-xmm15 are preserved.
- On AArch64 the callee preserves all general purpose registers, except X0-X8 and X16-X18. Not allowed with `nest`.
- On RISC-V the callee preserves x5-x31 except x6, x7 and x28 registers.
- On LoongArch the callee preserves r4-r31 except r12-r15 and r20-r21 registers.

The idea behind this convention is to support calls to runtime functions that have a hot path and a cold path. The hot path is usually a small piece of code that doesn’t use many registers. The cold path might need to call out to another function and therefore only needs to preserve the caller-saved registers, which haven’t already been saved by the caller. The *PreserveMost* calling convention is very similar to the *cold* calling convention in terms of caller/callee-saved registers, but they are used for different types of function calls. *coldcc* is for function calls that are rarely executed, whereas *preserve_mostcc* function calls are intended to be on the hot path and definitely executed a lot. Furthermore *preserve_mostcc* doesn’t prevent the inliner from inlining the function call.

This calling convention will be used by a future version of the Objective-C runtime and should therefore still be considered experimental at this time. Although this convention was created to optimize certain runtime calls to the Objective-C runtime, it is not limited to this runtime and might be used by other runtimes in the future too. The current implementation only supports X86-64, but the intention is to support more architectures in the future.

**“`preserve_allcc`” - The *PreserveAll* calling convention**

This calling convention attempts to make the code in the caller even less intrusive than the *PreserveMost* calling convention. This calling convention also behaves identically to the *C* calling convention on how arguments and return values are passed, but it uses a different set of caller/callee-saved registers. This removes the burden of saving and recovering a large register set before and after the call in the caller. If the arguments are passed in callee-saved registers, then they will be preserved by the callee across the call. This doesn’t apply for values returned in callee-saved registers.

- On X86-64 the callee preserves all general purpose registers, except for R11. R11 can be used as a scratch register. Furthermore it also preserves all floating-point registers (XMMs/YMMs).
- On AArch64 the callee preserves all general purpose registers, except X0-X8 and X16-X18. Furthermore it also preserves lower 128 bits of V8-V31 SIMD floating point registers. Not allowed with `nest`.

The idea behind this convention is to support calls to runtime functions that don’t need to call out to any other functions.

This calling convention, like the *PreserveMost* calling convention, will be used by a future version of the Objective-C runtime and should be considered experimental at this time.

**“`preserve_nonecc`” - The *PreserveNone* calling convention**

This calling convention doesn’t preserve any general registers. So all general registers are caller saved registers. It also uses all general registers to pass arguments. This attribute doesn’t impact non-general purpose registers (e.g., floating point registers, on X86 XMMs/YMMs). Non-general purpose registers still follow the standard C calling convention. Currently it is for x86_64, AArch64 and LoongArch only.

**“`cxx_fast_tlscc`” - The *CXX_FAST_TLS* calling convention for access functions**

Clang generates an access function to access C++-style Thread Local Storage (TLS). The access function generally has an entry block, an exit block and an initialization block that is run at the first time. The entry and exit blocks can access a few TLS IR variables, each access will be lowered to a platform-specific sequence.

This calling convention aims to minimize overhead in the caller by preserving as many registers as possible (all the registers that are preserved on the fast path, composed of the entry and exit blocks).

This calling convention behaves identically to the *C* calling convention on how arguments and return values are passed, but it uses a different set of caller/callee-saved registers.

Given that each platform has its own lowering sequence, hence its own set of preserved registers, we can’t use the existing *PreserveMost*.

- On X86-64 the callee preserves all general purpose registers, except for RDI and RAX.

**“`tailcc`” - Tail callable calling convention**

This calling convention ensures that calls in tail position will always be tail call optimized. This calling convention is equivalent to fastcc, except for an additional guarantee that tail calls will be produced whenever possible. Tail calls can only be optimized when this, the fastcc, the GHC or the HiPE convention is used. This calling convention does not support varargs and requires the prototype of all callees to exactly match the prototype of the function definition.

**“`swiftcc`” - This calling convention is used for Swift language.**

- On X86-64 RCX and R8 are available for additional integer returns, and XMM2 and XMM3 are available for additional FP/vector returns.
- On iOS platforms, we use AAPCS-VFP calling convention.

**“`swifttailcc`”**

This calling convention is like `swiftcc` in most respects, but also the callee pops the argument area of the stack so that mandatory tail calls are possible as in `tailcc`.

**“`cfguard_checkcc`” - Windows Control Flow Guard (Check mechanism)**

This calling convention is used for the Control Flow Guard check function, calls to which can be inserted before indirect calls to check that the call target is a valid function address. The check function has no return value, but it will trigger an OS-level error if the address is not a valid target. The set of registers preserved by the check function, and the register containing the target address are architecture-specific.

- On X86 the target address is passed in ECX.
- On ARM the target address is passed in R0.
- On AArch64 the target address is passed in X15.

**“`cc <n>`” - Numbered convention**

Any calling convention may be specified by number, allowing target-specific calling conventions to be used. Target-specific calling conventions start at 64.

More calling conventions can be added/defined on an as-needed basis, to support Pascal conventions or any other well-known target-independent convention.

All Global Variables and Functions have one of the following visibility styles:

**“`default`” - Default style**

On targets that use the ELF object file format, default visibility means that the declaration is visible to other modules and, in shared libraries, means that the declared entity may be overridden. On Darwin, default visibility means that the declaration is visible to other modules. On XCOFF, default visibility means no explicit visibility bit will be set and whether the symbol is visible (i.e “exported”) to other modules depends primarily on export lists provided to the linker. Default visibility corresponds to “external linkage” in the language.

**“`hidden`” - Hidden style**

Two declarations of an object with hidden visibility refer to the same object if they are in the same shared object. Usually, hidden visibility indicates that the symbol will not be placed into the dynamic symbol table, so no other module (executable or shared library) can reference it directly.

**“`protected`” - Protected style**

On ELF, protected visibility indicates that the symbol will be placed in the dynamic symbol table, but that references within the defining module will bind to the local symbol. That is, the symbol cannot be overridden by another module.

A symbol with `internal` or `private` linkage must have `default` visibility.

All Global Variables, Functions and Aliases can have one of the following DLL storage classes:

**`dllimport`**

“`dllimport`” causes the compiler to reference a function or variable via a global pointer to a pointer that is set up by the DLL exporting the symbol. On Microsoft Windows targets, the pointer name is formed by combining `__imp_` and the function or variable name.

**`dllexport`**

On Microsoft Windows targets, “`dllexport`” causes the compiler to provide a global pointer to a pointer in a DLL, so that it can be referenced with the `dllimport` attribute. The pointer name is formed by combining `__imp_` and the function or variable name. On XCOFF targets, `dllexport` indicates that the symbol will be made visible to other modules using “exported” visibility and thus placed by the linker in the loader section symbol table. Since this storage class exists for defining a DLL interface, the compiler, assembler and linker know it is externally referenced and must refrain from deleting the symbol.

A symbol with `internal` or `private` linkage cannot have a DLL storage class.

A variable may be defined as `thread_local`, which means that it will not be shared by threads (each thread will have a separate copy of the variable). Not all targets support thread-local variables. Optionally, a TLS model may be specified:

**`localdynamic`**

For variables that are only used within the current shared library.

**`initialexec`**

For variables in modules that will not be loaded dynamically.

**`localexec`**

For variables defined in the executable and only used within it.

If no explicit model is given, the “general dynamic” model is used.

The models correspond to the ELF TLS models; see ELF Handling For Thread-Local Storage for more information on under which circumstances the different models may be used. The target may choose a different TLS model if the specified model is not supported, or if a better choice of model can be made.

A model can also be specified in an alias, but then it only governs how the alias is accessed. It will not have any effect on the aliasee.

For platforms without linker support of ELF TLS model, the `-femulated-tls` flag can be used to generate GCC-compatible emulated TLS code.

Global variables, functions and aliases may have an optional runtime preemption specifier. If a preemption specifier isn’t given explicitly, then a symbol is assumed to be `dso_preemptable`.

**`dso_preemptable`**

Indicates that the function or variable may be replaced by a symbol from outside the linkage unit at runtime.

**`dso_local`**

The compiler may assume that a function or variable marked as `dso_local` will resolve to a symbol within the same linkage unit. Direct access will be generated even if the definition is not within this compilation unit.

LLVM IR allows you to specify both “identified” and “literal” structure types. Literal types are uniqued structurally, but identified types are never uniqued. An opaque structural type can also be used to forward declare a type that is not yet available.

An example of an identified structure specification is:

```llvm
%mytype = type { %mytype*, i32 }
```

Prior to the LLVM 3.0 release, identified types were structurally uniqued. Only literal types are uniqued in recent versions of LLVM.

Note: non-integral pointer types are a work in progress, and they should be considered experimental at this time.

For most targets, the pointer representation is a direct mapping from the bitwise representation to the address of the underlying memory location. Such pointers are considered “integral”, and any pointers where the representation is not just an integer address are called “non-integral”.

Non-integral pointers have at least one of the following three properties:

- the pointer representation contains non-address bits
- the pointer representation is unstable (may change at any time in a target-specific way)
- the pointer representation has external state

These properties (or combinations thereof) can be applied to pointers via the datalayout string.

The exact implications of these properties are target-specific. The following subsections describe the IR semantics and restrictions to optimization passes for each of these properties.

Pointers in this address space have a bitwise representation that not only has address bits, but also some other target-specific metadata. In most cases pointers with non-address bits behave exactly the same as integral pointers, the only difference is that it is not possible to create a pointer just from an address unless all the non-address bits are also recreated correctly in a target-specific way.

An example of pointers with non-address bits are the AMDGPU buffer descriptors which are 160 bits: a 128-bit fat pointer and a 32-bit offset. Similarly, CHERI capabilities contain a 32- or 64-bit address as well as the same number of metadata bits, but unlike the AMDGPU buffer descriptors they have external state in addition to non-address bits.

Pointers in this address space have an *unspecified* bitwise representation (i.e., not backed by a fixed integer). The bitwise pattern of such pointers is allowed to change in a target-specific way. For example, this could be a pointer type used with copying garbage collection where the garbage collector could update the pointer at any time in the collection sweep.

`inttoptr` and `ptrtoint` instructions have the same semantics as for integral (i.e., normal) pointers in that they convert integers to and from corresponding pointer types, but there are additional implications to be aware of.

For “unstable” pointer representations, the bit-representation of the pointer may not be stable, so two identical casts of the same operand may or may not return the same value. Said differently, the conversion to or from the “unstable” pointer type depends on environmental state in an implementation defined manner.

If the frontend wishes to observe a *particular* value following a cast, the generated IR must fence with the underlying environment in an implementation defined manner. (In practice, this tends to require `noinline` routines for such operations.)

From the perspective of the optimizer, `inttoptr` and `ptrtoint` for “unstable” pointer types are analogous to ones on integral types with one key exception: the optimizer may not, in general, insert new dynamic occurrences of such casts. If a new cast is inserted, the optimizer would need to either ensure that a) all possible values are valid, or b) appropriate fencing is inserted. Since the appropriate fencing is implementation defined, the optimizer can’t do the latter. The former is challenging as many commonly expected properties, such as `ptrtoint(v)-ptrtoint(v) == 0`, don’t hold for “unstable” pointer types. Similar restrictions apply to intrinsics that might examine the pointer bits, such as llvm.ptrmask.

The alignment information provided by the frontend for an “unstable” pointer (typically using attributes or metadata) must be valid for every possible representation of the pointer.

A further special case of non-integral pointers is ones that include external state (such as bounds information or a type tag) with a target-defined size. An example of such a type is a CHERI capability, where there is an additional validity bit that is part of all pointer-typed registers, but is located in memory at an implementation-defined address separate from the pointer itself. Another example would be a fat-pointer scheme where pointers remain plain integers, but the associated bounds are stored in an out-of-band table.

Unless also marked as “unstable”, the bit-wise representation of pointers with external state is stable and `ptrtoint(x)` always yields a deterministic value. This means transformation passes are still permitted to insert new `ptrtoint` instructions.

The following restrictions apply to IR level optimization passes:

The `inttoptr` instruction does not recreate the external state and therefore it is target dependent whether it can be used to create a dereferenceable pointer. In general passes should assume that the result of such an `inttoptr` is not dereferenceable. For example, on CHERI targets an `inttoptr` will yield a capability with the external state (the validity tag bit) set to zero, which will cause any dereference to trap. The `ptrtoint` instruction also only returns the “in-band” state and omits all external state.

When a `store ptr addrspace(N) %p, ptr @dst` of such a non-integral pointer is performed, the external metadata is also stored to an implementation-defined location. Similarly, a `%val = load ptr addrspace(N), ptr @dst` will fetch the external metadata and make it available for all uses of `%val`. Similarly, the `llvm.memcpy` and `llvm.memmove` intrinsics also transfer the external state. This is essential to allow frontends to efficiently emit copies of structures containing such pointers, since expanding all these copies as individual loads and stores would affect compilation speed and inhibit optimizations.

Notionally, these external bits are part of the pointer, but since `inttoptr` / ptrtoint` only operate on the “in-band” bits of the pointer and the external bits are not explicitly exposed, they are not included in the size specified in the datalayout string.

When a pointer type has external state, all roundtrips via memory must be performed as loads and stores of the correct type since stores of other types may not propagate the external data. Therefore it is not legal to convert an existing load/store (or a `llvm.memcpy` / `llvm.memmove` intrinsic) of pointer types with external state to a load/store of an integer or byte type with the same bitwidth, as that may drop the external state.

Global variables define regions of memory allocated at compilation time instead of run-time.

Global variable definitions must be initialized with a sized value.

Global variables in other translation units can also be declared, in which case they don’t have an initializer.

Global variables can optionally specify a linkage type.

Either global variable definitions or declarations may have an explicit section to be placed in and may have an optional explicit alignment specified. If there is a mismatch between the explicit or inferred section information for the variable declaration and its definition, the resulting behavior is undefined.

A variable may be defined as a global `constant`, which indicates that the contents of the variable will **never** be modified (enabling better optimization, allowing the global data to be placed in the read-only section of an executable, etc). Note that variables that need runtime initialization cannot be marked `constant` as there is a store to the variable.

LLVM explicitly allows *declarations* of global variables to be marked constant, even if the final definition of the global is not. This capability can be used to enable slightly better optimization of the program, but requires the language definition to guarantee that optimizations based on the ‘constantness’ are valid for the translation units that do not include the definition.

As SSA values, global variables define pointer values that are in scope for (i.e., they dominate) all basic blocks in the program. Global variables always define a pointer to their “content” type because they describe a region of memory, and all allocated object in LLVM are accessed through pointers.

Global variables can be marked with `unnamed_addr` which indicates that the address is not significant, only the content. Constants marked like this can be merged with other constants if they have the same initializer, and can also be duplicated. Note that a constant with significant address *can* be merged with a `unnamed_addr` constant, the result being a constant whose address is significant.

Warning

Constant duplication currently makes it unsound to compare pointers if either may be `unnamed_addr`, because each reference to the global in the IR may return a different pointer, and optimization passes may create additional references. Optimization passes can also create pointer comparisons with the expectation that the comparison will return true if the object is the same, which theoretically can make any usage of `unnamed_addr` unsound, but in practice it is unlikely that input IR that does not explicitly compare pointers will be affected by this issue.

If the `local_unnamed_addr` attribute is given, the address is known to not be significant within the module.

A global variable may be declared to reside in a target-specific numbered address space. For targets that support them, address spaces may affect how optimizations are performed and/or what target instructions are used to access the variable. The default address space is zero. The address space qualifier must precede any other attributes.

LLVM allows an explicit section to be specified for globals. If the target supports it, it will emit globals to the section specified. Additionally, the global can be placed in a comdat if the target has the necessary support.

External declarations may have an explicit section specified. Section information is retained in LLVM IR for targets that make use of this information. Attaching section information to an external declaration is an assertion that its definition is located in the specified section. If the definition is located in a different section, the behavior is undefined.

LLVM allows an explicit code model to be specified for globals. If the target supports it, it will emit globals in the code model specified, overriding the code model used to compile the translation unit. The allowed values are “tiny”, “small”, “kernel”, “medium”, “large”. This may be extended in the future to specify global data layout that doesn’t cleanly fit into a specific code model.

By default, global initializers are optimized by assuming that global variables defined within the module are not modified from their initial values before the start of the global initializer. This is true even for variables potentially accessible from outside the module, including those with external linkage or appearing in `@llvm.used` or dllexported variables. This assumption may be suppressed by marking the variable with `externally_initialized`.

An explicit alignment may be specified for a global, which must be a power of 2. If not present, or if the alignment is set to zero, the alignment of the global is set by the target to whatever it feels convenient. If an explicit alignment is specified, the global is forced to have exactly that alignment. Targets and optimizers are not allowed to over-align the global if the global has an assigned section. In this case, the extra alignment could be observable: for example, code could assume that the globals are densely packed in their section and try to iterate over them as an array, alignment padding would break this iteration. For TLS variables, the module flag `MaxTLSAlign`, if present, limits the alignment to the given value. Optimizers are not allowed to impose a stronger alignment on these variables. The maximum alignment is `1 << 32`.

For global variable declarations, as well as definitions that may be replaced at link time (`linkonce`, `weak`, `extern_weak` and `common` linkage types), the allocation size and alignment of the definition it resolves to must be greater than or equal to that of the declaration or replaceable definition, otherwise the behavior is undefined.

Globals can also have a DLL storage class, an optional runtime preemption specifier, an optional global attributes and an optional list of attached metadata.

Variables and aliases can have a Thread Local Storage Model.

Globals cannot be or contain Scalable vectors because their size is unknown at compile time. They are allowed in structs to facilitate intrinsics returning multiple values. Generally, structs containing scalable vectors are not considered “sized” and cannot be used in loads, stores, allocas, or GEPs. The only exception to this rule is for structs that contain scalable vectors of the same type (e.g., `{<vscale x 2 x i32>, <vscale x 2 x i32>}` contains the same type while `{<vscale x 2 x i32>, <vscale x 2 x i64>}` doesn’t). These kinds of structs (we may call them homogeneous scalable vector structs) are considered sized and can be used in loads, stores, allocas, but not GEPs.

Globals with `toc-data` attribute set are stored in TOC of XCOFF. Their alignments are not larger than that of a TOC entry. Optimizations should not increase their alignments to mitigate TOC overflow.

Syntax:

```
@<GlobalVarName> = [Linkage] [PreemptionSpecifier] [Visibility]
                   [DLLStorageClass] [ThreadLocal]
                   [(unnamed_addr|local_unnamed_addr)] [AddrSpace]
                   [ExternallyInitialized]
                   <global | constant> <Type> [<InitializerConstant>]
                   [, section "name"] [, partition "name"]
                   [, comdat [($name)]] [, align <Alignment>]
                   [, code_model "model"]
                   [, no_sanitize_address] [, no_sanitize_hwaddress]
                   [, sanitize_address_dyninit] [, sanitize_memtag]
                   (, !name !N)*
```

For example, the following defines a global in a numbered address space with an initializer, section, and alignment:

```llvm
@G = addrspace(5) constant float 1.0, section "foo", align 4
```

The following example just declares a global variable

```llvm
@G = external global i32
```

The following example defines a global variable with the `large` code model:

```llvm
@G = internal global i32 0, code_model "large"
```

The following example defines a thread-local global with the `initialexec` TLS model:

```llvm
@G = thread_local(initialexec) global i32 0, align 4
```

LLVM function definitions consist of the “`define`” keyword, an optional linkage type, an optional runtime preemption specifier, an optional visibility style, an optional DLL storage class, an optional calling convention, an optional `unnamed_addr` attribute, a return type, an optional parameter attribute for the return type, a function name, a (possibly empty) argument list (each with optional parameter attributes), optional function attributes, an optional address space, an optional section, an optional partition, an optional minimum alignment, an optional preferred alignment, an optional comdat, an optional garbage collector name, an optional prefix, an optional prologue, an optional personality, an optional list of attached metadata, an opening curly brace, a list of basic blocks, and a closing curly brace.

Syntax:

```
define [linkage] [PreemptionSpecifier] [visibility] [DLLStorageClass]
       [cconv] [ret attrs]
       <ResultType> @<FunctionName> ([argument list])
       [(unnamed_addr|local_unnamed_addr)] [AddrSpace] [fn Attrs]
       [section "name"] [partition "name"] [comdat [($name)]] [align N]
       [prefalign(N)] [gc] [prefix Constant] [prologue Constant]
       [personality Constant] (!name !N)* { ... }
```

The argument list is a comma-separated sequence of arguments where each argument is of the following form:

Syntax:

```
<type> [parameter Attrs] [name]
```

LLVM function declarations consist of the “`declare`” keyword, an optional linkage type, an optional visibility style, an optional DLL storage class, an optional calling convention, an optional `unnamed_addr` or `local_unnamed_addr` attribute, an optional address space, a return type, an optional parameter attribute for the return type, a function name, a possibly empty list of arguments, an optional alignment, an optional garbage collector name, an optional prefix, and an optional prologue.

Syntax:

```
declare [linkage] [visibility] [DLLStorageClass]
        [cconv] [ret attrs]
        <ResultType> @<FunctionName> ([argument list])
        [(unnamed_addr|local_unnamed_addr)] [align N] [gc]
        [prefix Constant] [prologue Constant]
```

A function definition contains a list of basic blocks, forming the CFG (Control Flow Graph) for the function. Each basic block may optionally start with a label (giving the basic block a symbol table entry), contains a list of instructions and debug records, and ends with a terminator instruction (such as a branch or function return). If an explicit label name is not provided, a block is assigned an implicit numbered label, using the next value from the same counter as used for unnamed temporaries (see above). For example, if a function entry block does not have an explicit label, it will be assigned label “%0”, then the first unnamed temporary in that block will be “%1”, etc. If a numeric label is explicitly specified, it must match the numeric label that would be used implicitly.

The first basic block in a function is special in two ways: it is immediately executed on entrance to the function, and it is not allowed to have predecessor basic blocks (i.e., there can not be any branches to the entry block of a function). Because the block can have no predecessors, it also cannot have any PHI nodes.

LLVM allows an explicit section to be specified for functions. If the target supports it, it will emit functions to the section specified. Additionally, the function can be placed in a COMDAT.

An explicit minimum alignment (`align`) may be specified for a function. If not present, or if the alignment is set to zero, the alignment of the function is set according to the preferred alignment rules described below. If an explicit minimum alignment is specified, the function is forced to have at least that much alignment. All alignments must be a power of 2.

An explicit preferred alignment (`prefalign`) may also be specified for a function (definitions only, and must be a power of 2). If a function does not have a preferred alignment attribute, the preferred alignment is determined in a target-specific way. The preferred alignment, if provided, is treated as a hint; the final alignment of the function will generally be set to a value somewhere between the minimum alignment and the preferred alignment.

If the `unnamed_addr` attribute is given, the address is known to not be significant and two identical functions can be merged.

If the `local_unnamed_addr` attribute is given, the address is known to not be significant within the module.

If an explicit address space is not given, it will default to the program address space from the datalayout string.

Aliases, unlike function or variables, don’t create any new data. They are just a new symbol and metadata for an existing position.
