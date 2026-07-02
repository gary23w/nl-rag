---
title: "LLVM Language Reference Manual (part 3/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 3/20
---

# LLVM Language Reference Manual

This attribute indicates that the function should be added to a jump-instruction table at code-generation time, and that all address-taken references to this function should be replaced with a reference to the appropriate jump-instruction-table function pointer. Note that this creates a new pointer for the original function, which means that code that depends on function-pointer identity can break. So, any function annotated with `jumptable` must also be `unnamed_addr`.

**`memory(...)`**

This attribute specifies the possible memory effects of the call-site or function. It allows specifying the possible access kinds (`none`, `read`, `write`, or `readwrite`) for the possible memory location kinds (`argmem`, `inaccessiblemem`, `errnomem`, `target_mem0`, `target_mem1`, as well as a default). It is best understood by example:

- `memory(none)`: Does not access any memory.
- `memory(read)`: May read (but not write) any memory.
- `memory(write)`: May write (but not read) any memory.
- `memory(readwrite)`: May read or write any memory.
- `memory(argmem: read)`: May only read argument memory.
- `memory(argmem: read, inaccessiblemem: write)`: May only read argument memory and only write inaccessible memory.
- `memory(argmem: read, errnomem: write)`: May only read argument memory and only write errno.
- `memory(read, argmem: readwrite)`: May read any memory (default mode) and additionally write argument memory.
- `memory(readwrite, argmem: none)`: May access any memory apart from argument memory.

The supported access kinds are:

- `readwrite`: Any kind of access to the location is allowed.
- `read`: The location is only read. Writing to the location is immediate undefined behavior. This includes the case where the location is read from and then the same value is written back.
- `write`: Only writes to the location are observable outside the function call. However, the function may still internally read the location after writing it, as this is not observable. Reading the location prior to writing it results in a poison value.
- `none`: No reads or writes to the location are observed outside the function. It is always valid to read and write allocas, and to read global constants, even if `memory(none)` is used, as these effects are not externally observable.

The supported memory location kinds are:

- `argmem`: This refers to accesses that are based on pointer arguments to the function.
- `inaccessiblemem`: This refers to accesses to memory which is not accessible by the current module (before return from the function – an allocator function may return newly accessible memory while only accessing inaccessible memory itself). Inaccessible memory is often used to model control dependencies of intrinsics.
- `errnomem`: This refers to accesses to the `errno` variable.
- `target_mem#` : These refer to target specific state that cannot be accessed by any other means. # is a number between 0 and 1 inclusive. Note: The target_mem locations are experimental and intended for internal testing only. They must not be used in production code.
- The default access kind (specified without a location prefix) applies to all locations that haven’t been specified explicitly, including those that don’t currently have a dedicated location kind (e.g., accesses to globals or captured pointers).

If the `memory` attribute is not specified, then `memory(readwrite)` is implied (all memory effects are possible).

The memory effects of a call can be computed as `CallSiteEffects & (FunctionEffects | OperandBundleEffects)`. Thus, the call-site annotation takes precedence over the potential effects described by either the function annotation or the operand bundles.

**`minsize`**

This attribute suggests that optimization passes and code generator passes make choices that keep the code size of this function as small as possible and perform optimizations that may sacrifice runtime performance in order to minimize the size of the generated code. This attribute is incompatible with the `optdebug` and `optnone` attributes.

**`naked`**

This attribute disables prologue / epilogue emission for the function. This can have very system-specific consequences. The arguments of a `naked` function can not be referenced through IR values.

**`"no-inline-line-tables"`**

When this attribute is set to true, the inliner discards source locations when inlining code and instead uses the source location of the call site. Breakpoints set on code that was inlined into the current function will not fire during the execution of the inlined call sites. If the debugger stops inside an inlined call site, it will appear to be stopped at the outermost inlined call site.

**`no-jump-tables`**

When this attribute is set to true, the jump tables and lookup tables that can be generated from a switch case lowering are disabled.

**`nobuiltin`**

This indicates that the callee function at a call site is not recognized as a built-in function. LLVM will retain the original call and not replace it with equivalent code based on the semantics of the built-in function, unless the call site uses the `builtin` attribute. This is valid at call sites and on function declarations and definitions.

**`nocallback`**

This attribute indicates that the function is only allowed to jump back into the caller’s module by a return or an exception, and is not allowed to jump back by invoking a callback function, a direct, possibly transitive, external function call, use of `longjmp`, or other means. It is a compiler hint that is used at the module level to improve dataflow analysis, dropped during linking, and has no effect on functions defined in the current module.

**`nodivergencesource`**

A call to this function is not a source of divergence. In uniformity analysis, a *source of divergence* is an instruction that generates divergence even if its inputs are uniform. A call with no further information would normally be considered a source of divergence; setting this attribute on a function means that a call to it is not a source of divergence.

**`noduplicate`**

This attribute indicates that calls to the function cannot be duplicated. A call to a `noduplicate` function may be moved within its parent function, but may not be duplicated within its parent function.

A function containing a `noduplicate` call may still be an inlining candidate, provided that the call is not duplicated by inlining. That implies that the function has internal linkage and only has one call site, so the original call is dead after inlining.

**`nofree`**

This function attribute indicates that the function does not free any memory allocation which existed before the call, either through direct calls to a memory-deallocation function like `free`, or through synchronization. Freeing through synchronization here means that a deallocation *happens-before* the function exit but does not *happens-before* the function entry.

As a result, pointers that are known to be dereferenceable prior to a call to a function with the `nofree` attribute are still known to be dereferenceable after the call.

A `nofree` function is explicitly allowed to free memory which it allocated or arrange for another thread to free such memory on its behalf. As a result, perhaps surprisingly, a `nofree` function can return a pointer to a previously deallocated allocated object.

**`noimplicitfloat`**

Disallows implicit floating-point code. This inhibits optimizations that use floating-point code and floating-point registers for operations that are not nominally floating-point. LLVM instructions that perform floating-point operations or require access to floating-point registers may still cause floating-point code to be generated.

Also inhibits optimizations that create SIMD/vector code and registers from scalar code such as vectorization or memcpy/memset optimization. This includes integer vectors. Vector instructions present in IR may still cause vector code to be generated.

**`noinline`**

This attribute indicates that the inliner should never inline this function in any situation. This attribute may not be used together with the `alwaysinline` attribute.

**`noipa`**

Disables any interprocedural analysis that inspects the definition of this function. This attribute is equivalent to moving this function definition to a separate, optimizer-opaque, module. Any attributes on the function are still respected (as they would be if they remained on a function declaration in this module). This attribute does *not* control inlining or outlining. Add the `noinline` and `nooutline` attributes as well in cases where inlining and outlining should additionally be disabled.

**`nomerge`**

This attribute indicates that calls to this function should never be merged during optimization. For example, it will prevent tail merging otherwise identical code sequences that raise an exception or terminate the program. Tail merging normally reduces the precision of source location information, making stack traces less useful for debugging. This attribute gives the user control over the tradeoff between code size and debug information precision.

**`nonlazybind`**

This attribute suppresses lazy symbol binding for the function. This may make calls to the function faster, at the cost of extra program startup time if the function is not called during program startup.

**`noprofile`**

This function attribute prevents instrumentation-based profiling, used for coverage or profile based optimization, from being added to a function. It also blocks inlining if the caller and callee have different values of this attribute.

**`skipprofile`**

This function attribute prevents instrumentation-based profiling, used for coverage or profile based optimization, from being added to a function. This attribute does not restrict inlining, so instrumented instructions could end up in this function.

**`noredzone`**

This attribute indicates that the code generator should not use a red zone, even if the target-specific ABI normally permits it.

**`indirect-tls-seg-refs`**

This attribute indicates that the code generator should not use direct TLS access through segment registers, even if the target-specific ABI normally permits it.

**`noreturn`**

This function attribute indicates that the function never returns normally, hence through a return instruction. This produces undefined behavior at runtime if the function ever does dynamically return. Annotated functions may still raise an exception, i.a., `nounwind` is not implied.

**`norecurse`**

This function attribute indicates that the function is not recursive and does not participate in recursion. This means that the function never occurs inside a cycle in the dynamic call graph. For example:

```
fn -> other_fn -> fn       ; fn is not norecurse
other_fn -> fn -> other_fn ; fn is not norecurse
fn -> other_fn -> other_fn ; fn is norecurse
```

**`willreturn`**

This function attribute indicates that a call of this function will either exhibit undefined behavior or comes back and continues execution at a point in the existing call stack that includes the current invocation. Annotated functions may still raise an exception, i.a., `nounwind` is not implied. If an invocation of an annotated function does not return control back to a point in the call stack, the behavior is undefined.

**`nosync`**

This function attribute indicates that the function does not introduce any *synchronizes-with* edges in the sense of the memory model.

In particular, synchronization is considered possible in the presence of *atomic* accesses that enforce an order, thus not “unordered” and “monotonic”, as well as *convergent* function calls.

Note that *convergent* operations can involve communication that is considered to be not through memory and does not necessarily imply an ordering between threads for the purposes of the memory model. Therefore, an operation can be both *convergent* and *nosync*.

If a *nosync* function does ever synchronize with another thread, the behavior is undefined.

**`nounwind`**

This function attribute indicates that the function never raises an exception. If the function does raise an exception, its runtime behavior is undefined. However, functions marked nounwind may still trap or generate asynchronous exceptions. Exception handling schemes that are recognized by LLVM to handle asynchronous exceptions, such as SEH, will still provide their implementation defined semantics.

**`nosanitize_bounds`**

This attribute indicates that bounds checking sanitizer instrumentation is disabled for this function.

**`nosanitize_coverage`**

This attribute indicates that SanitizerCoverage instrumentation is disabled for this function.

**`null_pointer_is_valid`**

If `null_pointer_is_valid` is set, then the `null` address in address-space 0 is considered to be a valid address for memory loads and stores. Any analysis or optimization should not treat dereferencing a pointer to `null` as undefined behavior in this function. Note: Comparing the address of a global variable to `null` may still evaluate to false because of a limitation in querying this attribute inside constant expressions.

**`optdebug`**

This attribute suggests that optimization passes and code generator passes should make choices that try to preserve debug info without significantly degrading runtime performance. This attribute is incompatible with the `minsize`, `optsize`, and `optnone` attributes.

**`optforfuzzing`**

This attribute indicates that this function should be optimized for maximum fuzzing signal.

**`optnone`**

This function attribute indicates that most optimization passes will skip this function, with the exception of interprocedural optimization passes. Code generation defaults to the “fast” instruction selector. This attribute cannot be used together with the `alwaysinline` attribute; this attribute is also incompatible with the `minsize`, `optsize`, and `optdebug` attributes.

This attribute requires the `noinline` attribute to be specified on the function as well, so the function is never inlined into any caller. Only functions with the `alwaysinline` attribute are valid candidates for inlining into the body of this function.

**`optsize`**

This attribute suggests that optimization passes and code generator passes make choices that keep the code size of this function low, and otherwise do optimizations specifically to reduce code size as long as they do not significantly impact runtime performance. This attribute is incompatible with the `optdebug` and `optnone` attributes.

**`"patchable-function"`**

This attribute tells the code generator that the code generated for this function needs to follow certain conventions that make it possible for a runtime function to patch over it later. The exact effect of this attribute depends on its string value, for which there currently is one legal possibility:

> - `"prologue-short-redirect"` - This style of patchable function is intended to support patching a function prologue to redirect control away from the function in a thread-safe manner. It guarantees that the first instruction of the function will be large enough to accommodate a short jump instruction, and will be sufficiently aligned to allow being fully changed via an atomic compare-and-swap instruction. While the first requirement can be satisfied by inserting large enough NOP, LLVM can and will try to re-purpose an existing instruction (i.e., one that would have to be emitted anyway) as the patchable instruction larger than a short jump. `"prologue-short-redirect"` is currently only supported on x86-64.

This attribute by itself does not imply restrictions on inter-procedural optimizations. All of the semantic effects the patching may have to be separately conveyed via the linkage type.

**`"patchable-function-prefix"`**

This attribute specifies the number of target-specific NOP instructions emitted before the function entry label.

**`"patchable-function-entry"`**

This attribute specifies the number of target-specific NOP instructions emitted after the function entry label. These NOPs are emitted before the function prologue.

**`"patchable-function-entry-section"`**

This attribute specifies the section used to record the start of the patchable function entry area when such a section is emitted. If omitted, the default section name is `__patchable_function_entries`.

**`"probe-stack"`**

This attribute indicates that the function will trigger a guard region in the end of the stack. It ensures that accesses to the stack must be no further apart than the size of the guard region to a previous access of the stack. It takes one required string value, the name of the stack probing function that will be called.

If a function that has a `"probe-stack"` attribute is inlined into a function with another `"probe-stack"` attribute, the resulting function has the `"probe-stack"` attribute of the caller. If a function that has a `"probe-stack"` attribute is inlined into a function that has no `"probe-stack"` attribute at all, the resulting function has the `"probe-stack"` attribute of the callee.

**`"stack-probe-size"`**

This attribute controls the behavior of stack probes: either the `"probe-stack"` attribute, or ABI-required stack probes, if any. It defines the size of the guard region. It ensures that if the function may use more stack space than the size of the guard region, a stack probing sequence will be emitted. It takes one required integer value, which is 4096 by default.

If a function that has a `"stack-probe-size"` attribute is inlined into a function with another `"stack-probe-size"` attribute, the resulting function has the `"stack-probe-size"` attribute that has the lower numeric value. If a function that has a `"stack-probe-size"` attribute is inlined into a function that has no `"stack-probe-size"` attribute at all, the resulting function has the `"stack-probe-size"` attribute of the callee.

**`"no-stack-arg-probe"`**

This attribute disables ABI-required stack probes, if any.

**`returns_twice`**

This attribute indicates that this function can return twice. The C `setjmp` is an example of such a function. The compiler disables some optimizations (like tail calls) in the caller of these functions.

**`safestack`**

This attribute indicates that SafeStack protection is enabled for this function.

If a function that has a `safestack` attribute is inlined into a function that doesn’t have a `safestack` attribute or which has an `ssp`, `sspstrong` or `sspreq` attribute, then the resulting function will have a `safestack` attribute.

**`sanitize_address`**

This attribute indicates that AddressSanitizer checks (dynamic address safety analysis) are enabled for this function.

**`sanitize_memory`**

This attribute indicates that MemorySanitizer checks (dynamic detection of accesses to uninitialized memory) are enabled for this function.

**`sanitize_thread`**

This attribute indicates that ThreadSanitizer checks (dynamic thread safety analysis) are enabled for this function.

**`sanitize_hwaddress`**

This attribute indicates that HWAddressSanitizer checks (dynamic address safety analysis based on tagged pointers) are enabled for this function.

**`sanitize_memtag`**

This attribute indicates that MemTagSanitizer checks (dynamic address safety analysis based on Armv8 MTE) are enabled for this function.

**`sanitize_realtime`**

This attribute indicates that RealtimeSanitizer checks (realtime safety analysis - no allocations, syscalls or exceptions) are enabled for this function.

**`sanitize_realtime_blocking`**

This attribute indicates that RealtimeSanitizer should error immediately if the attributed function is called during invocation of a function attributed with `sanitize_realtime`. This attribute is incompatible with the `sanitize_realtime` attribute.

**`sanitize_alloc_token`**

This attribute indicates that implicit allocation token instrumentation is enabled for this function.

**`speculative_load_hardening`**

This attribute indicates that Speculative Load Hardening should be enabled for the function body.

Speculative Load Hardening is a best-effort mitigation against information leak attacks that make use of control flow miss-speculation - specifically miss-speculation of whether a branch is taken or not. Typically vulnerabilities enabling such attacks are classified as “Spectre variant #1”. Notably, this does not attempt to mitigate against miss-speculation of branch target, classified as “Spectre variant #2” vulnerabilities.

When inlining, the attribute is sticky. Inlining a function that carries this attribute will cause the caller to gain the attribute. This is intended to provide a maximally conservative model where the code in a function annotated with this attribute will always (even after inlining) end up hardened.

**`speculatable`**

This function attribute indicates that the function does not have any effects besides calculating its result and does not have undefined behavior. Note that `speculatable` is not enough to conclude that along any particular execution path the number of calls to this function will not be externally observable. This attribute is only valid on functions and declarations, not on individual call sites. If a function is incorrectly marked as speculatable and really does exhibit undefined behavior, the undefined behavior may be observed even if the call site is dead code.

**`ssp`**

This attribute indicates that the function should emit a stack smashing protector. It is in the form of a “canary” — a random value placed on the stack before the local variables that’s checked upon return from the function to see if it has been overwritten. A heuristic is used to determine if a function needs stack protectors or not. The heuristic used will enable protectors for functions with:

- Character arrays larger than `ssp-buffer-size` (default 8).
- Aggregates containing character arrays larger than `ssp-buffer-size`.
- Calls to alloca() with variable sizes or constant sizes greater than `ssp-buffer-size`.

Variables that are identified as requiring a protector will be arranged on the stack such that they are adjacent to the stack protector guard.

If a function with an `ssp` attribute is inlined into a calling function, the attribute is not carried over to the calling function.

**`sspstrong`**

This attribute indicates that the function should emit a stack smashing protector. This attribute causes a strong heuristic to be used when determining if a function needs stack protectors. The strong heuristic will enable protectors for functions with:

- Arrays of any size and type
- Aggregates containing an array of any size and type.
- Calls to alloca().
- Local variables that have had their address taken.

Variables that are identified as requiring a protector will be arranged on the stack such that they are adjacent to the stack protector guard. The specific layout rules are:

1. Large arrays and structures containing large arrays (`>= ssp-buffer-size`) are closest to the stack protector.
2. Small arrays and structures containing small arrays (`< ssp-buffer-size`) are 2nd closest to the protector.
3. Variables that have had their address taken are 3rd closest to the protector.

This overrides the `ssp` function attribute.

If a function with an `sspstrong` attribute is inlined into a calling function which has an `ssp` attribute, the calling function’s attribute will be upgraded to `sspstrong`.

**`sspreq`**

This attribute indicates that the function should *always* emit a stack smashing protector. This overrides the `ssp` and `sspstrong` function attributes.

Variables that are identified as requiring a protector will be arranged on the stack such that they are adjacent to the stack protector guard. The specific layout rules are:

1. Large arrays and structures containing large arrays (`>= ssp-buffer-size`) are closest to the stack protector.
2. Small arrays and structures containing small arrays (`< ssp-buffer-size`) are 2nd closest to the protector.
3. Variables that have had their address taken are 3rd closest to the protector.

If a function with an `sspreq` attribute is inlined into a calling function which has an `ssp` or `sspstrong` attribute, the calling function’s attribute will be upgraded to `sspreq`.

**`strictfp`**

This attribute indicates that the function was called from a scope that requires strict floating-point semantics. LLVM will not attempt any optimizations that require assumptions about the floating-point rounding mode or that might alter the state of floating-point status flags that might otherwise be set or cleared by calling this function. LLVM will not introduce any new floating-point instructions that may trap.

**`denormal_fpenv`**

This indicates the denormal (subnormal) handling that may be assumed for the default floating-point environment. The base form is a `|` separated pair. The elements may be one of `ieee`, `preservesign`, `positivezero`, or `dynamic`. The first entry indicates the flushing mode for the result of floating point operations. The second indicates the handling of denormal inputs to floating point instructions. For compatibility with older bitcode, if the second value is omitted, both input and output modes will assume the same mode.

If this is attribute is not specified, the default is `ieee|ieee`.

If the output mode is `preservesign`, or `positivezero`, denormal outputs may be flushed to zero by standard floating-point operations. It is not mandated that flushing to zero occurs, but if a denormal output is flushed to zero, it must respect the sign mode. Not all targets support all modes.

If the mode is `dynamic`, the behavior is derived from the dynamic state of the floating-point environment. Transformations which depend on the behavior of denormal values should not be performed.

While this indicates the expected floating point mode the function will be executed with, this does not make any attempt to ensure the mode is consistent. User or platform code is expected to set the floating point mode appropriately before function entry.

This may optionally specify a second pair, prefixed with `float:`. This provides an override for the behavior of 32-bit float type (or vectors of 32-bit floats).

If the input mode is `preservesign`, or `positivezero`, a floating-point operation must treat any input denormal value as zero. In some situations, if an instruction does not respect this mode, the input may need to be converted to 0 as if by `@llvm.canonicalize` during lowering for correctness.

This may optionally specify a second pair, prefixed with `float:`. This provides an override for the behavior of 32-bit float type. (or vectors of 32-bit floats). If this is present, this overrides the base handling of the default mode. Not all targets support separately setting the denormal mode per type, and no attempt is made to diagnose unsupported uses. Currently this attribute is respected by the AMDGPU and NVPTX backends.

**Examples:**

`denormal_fpenv(preservesign)` `denormal_fpenv(float: preservesign)` `denormal_fpenv(dynamic, float: preservesign|ieee)` `denormal_fpenv(ieee|ieee, float: preservesign|preservesign)` `denormal_fpenv(ieee|dynamic, float: preservesign|ieee)`

**`"thunk"`**

This attribute indicates that the function will delegate to some other function with a tail call. The prototype of a thunk should not be used for optimization purposes. The caller is expected to cast the thunk prototype to match the thunk target prototype.

**`uwtable[(sync|async)]`**

This attribute indicates that the ABI being targeted requires that an unwind table entry be produced for this function even if we can show that no exceptions pass by it. This is normally the case for the ELF x86-64 abi, but it can be disabled for some compilation units. The optional parameter describes what kind of unwind tables to generate: `sync` for normal unwind tables, `async` for asynchronous (instruction precise) unwind tables. Without the parameter, the attribute `uwtable` is equivalent to `uwtable(async)`.

**`nocf_check`**

This attribute indicates that no control-flow check will be performed on the attributed entity. It disables -fcf-protection=<> for a specific entity to fine grain the HW control flow protection mechanism. The flag is target independent and currently appertains to a function or function pointer.

**`shadowcallstack`**

This attribute indicates that the ShadowCallStack checks are enabled for the function. The instrumentation checks that the return address for the function has not changed between the function prologue and epilogue. It is currently x86_64-specific.

**`mustprogress`**

This attribute indicates that the function is required to return, unwind, or interact with the environment in an observable way e.g., via a volatile memory access, I/O, or other synchronization. The `mustprogress` attribute is intended to model the requirements of the first section of [intro.progress] of the C++ Standard. As a consequence, a loop in a function with the `mustprogress` attribute can be assumed to terminate if it does not interact with the environment in an observable way, and terminating loops without side-effects can be removed. If a `mustprogress` function does not satisfy this contract, the behavior is undefined. If a `mustprogress` function calls a function not marked `mustprogress`, and that function never returns, the program is well-defined even if there isn’t any other observable progress. Note that `willreturn` implies `mustprogress`.

**`"warn-stack-size"="<threshold>"`**

This attribute sets a threshold to emit diagnostics once the frame size is known should the frame size exceed the specified value. It takes one required integer value, which should be a non-negative integer, and less than *UINT_MAX*. It’s unspecified which threshold will be used when duplicate definitions are linked together with differing values.

**`vscale_range(<min>[, <max>])`**

This function attribute indicates *vscale* is a power-of-two within a specified range. *min* must be a power-of-two that is greater than 0. When specified, *max* must be a power-of-two greater-than-or-equal to *min* or 0 to signify an unbounded maximum. The syntax *vscale_range(<val>)* can be used to set both *min* and *max* to the same value. Functions that don’t include this attribute make no assumptions about the range of *vscale*.

**`nooutline`**

This attribute indicates that outlining passes should not modify the function.

**`nocreateundeforpoison`**

This attribute indicates that the result of the function (prior to application of return attributes/metadata) will not be undef or poison if all arguments are not undef and not poison. Otherwise, it is undefined behavior.

**`"modular-format"="<type>,<string_idx>,<first_arg_idx>,<modular_impl_fn>,<impl_name>,<aspects...>"`**

This attribute indicates that the implementation is modular on a particular format string argument. If the compiler can determine that not all aspects of the implementation are needed, it can report which aspects were needed and redirect the call to a modular implementation function instead.

The compiler reports that an implementation aspect is needed by issuing a relocation for the symbol *<impl_name>_<aspect>`*. This arranges for code and data needed to support the aspect of the implementation to be brought into the link to satisfy weak references in the modular implemenation function.

The first three arguments have the same semantics as the arguments to the C `format` attribute.

The following aspects are currently supported:

- `fixed`: The call has a C ISO 18037 fixed-point argument.
- `float`: The call has a floating-point argument.

In addition to function attributes the following call site only attributes are supported:

**`vector-function-abi-variant`**

This attribute can be attached to a call to list the vector functions associated to the function. Notice that the attribute cannot be attached to a invoke or a callbr instruction. The attribute consists of a comma separated list of mangled names. The order of the list does not imply preference (it is logically a set). The compiler is free to pick any listed vector function of its choosing.

The syntax for the mangled names is as follows::

```
_ZGV<isa><mask><vlen><parameters>_<scalar_name>[(<vector_redirection>)]
```

When present, the attribute informs the compiler that the function `<scalar_name>` has a corresponding vector variant that can be used to perform the concurrent invocation of `<scalar_name>` on vectors. The shape of the vector function is described by the tokens between the prefix `_ZGV` and the `<scalar_name>` token. The standard name of the vector function is `_ZGV<isa><mask><vlen><parameters>_<scalar_name>`. When present, the optional token `(<vector_redirection>)` informs the compiler that a custom name is provided in addition to the standard one (custom names can be provided for example via the use of `declare variant` in OpenMP 5.0). The declaration of the variant must be present in the IR Module. The signature of the vector variant is determined by the rules of the Vector Function ABI (VFABI) specifications of the target. For Arm and X86, the VFABI can be found at https://github.com/ARM-software/abi-aa and https://software.intel.com/content/www/us/en/develop/download/vector-simd-function-abi.html, respectively.

For X86 and Arm targets, the values of the tokens in the standard name are those that are defined in the VFABI. LLVM has an internal `<isa>` token that can be used to create scalar-to-vector mappings for functions that are not directly associated to any of the target ISAs (for example, some of the mappings stored in the TargetLibraryInfo). Valid values for the `<isa>` token are::

```
<isa>:= b | c | d | e  -> X86 SSE, AVX, AVX2, AVX512
      | n | s          -> Armv8 Advanced SIMD, SVE
      | __LLVM__       -> Internal LLVM Vector ISA
```

For all targets currently supported (x86, Arm and Internal LLVM), the remaining tokens can have the following values::

```
<mask>:= M | N         -> mask | no mask

<vlen>:= number        -> number of lanes
       | x             -> VLA (Vector Length Agnostic)

<parameters>:= v              -> vector
             | l | l <number> -> linear
             | R | R <number> -> linear with ref modifier
             | L | L <number> -> linear with val modifier
             | U | U <number> -> linear with uval modifier
             | ls <pos>       -> runtime linear
             | Rs <pos>       -> runtime linear with ref modifier
             | Ls <pos>       -> runtime linear with val modifier
             | Us <pos>       -> runtime linear with uval modifier
             | u              -> uniform

<scalar_name>:= name of the scalar function

<vector_redirection>:= optional, custom name of the vector function
```

**`preallocated(<ty>)`**

This attribute is required on calls to `llvm.call.preallocated.arg` and cannot be used on any other call. See llvm.call.preallocated.arg for more details.

Attributes may be set to communicate additional information about a global variable. Unlike function attributes, attributes on a global variable are grouped into a single attribute group.

**`no_sanitize_address`**

This attribute indicates that the global variable should not have AddressSanitizer instrumentation applied to it, because it was annotated with *__attribute__((no_sanitize(“address”)))*, *__attribute__((disable_sanitizer_instrumentation))*, or included in the *-fsanitize-ignorelist* file.

**`no_sanitize_hwaddress`**

This attribute indicates that the global variable should not have HWAddressSanitizer instrumentation applied to it, because it was annotated with *__attribute__((no_sanitize(“hwaddress”)))*, *__attribute__((disable_sanitizer_instrumentation))*, or included in the *-fsanitize-ignorelist* file.

**`sanitize_memtag`**

This attribute indicates that the global variable should have AArch64 memory tags (MTE) instrumentation applied to it. This attribute causes the suppression of certain optimizations, like GlobalMerge, as well as ensuring extra directives are emitted in the assembly and extra bits of metadata are placed in the object file so that the linker can ensure the accesses are protected by MTE. This attribute is added by clang when *-fsanitize=memtag-globals* is provided, as long as the global is not marked with *__attribute__((no_sanitize(“memtag”)))*, *__attribute__((disable_sanitizer_instrumentation))*, or included in the *-fsanitize-ignorelist* file. The AArch64 Globals Tagging pass may remove this attribute when it’s not possible to tag the global (e.g., it’s a TLS variable).

**`sanitize_address_dyninit`**

This attribute indicates that the global variable, when instrumented with AddressSanitizer, should be checked for ODR violations. This attribute is applied to global variables that are dynamically initialized according to C++ rules.

Operand bundles are tagged sets of SSA values or metadata strings that can be associated with certain LLVM instructions (currently only `call` s and `invoke` s). In a way they are like metadata, but dropping them is incorrect and will change program semantics.

Syntax:

```
operand bundle set ::= '[' operand bundle (, operand bundle )* ']'
operand bundle ::= tag '(' [ bundle operand ] (, bundle operand )* ')'
bundle operand ::= SSA value | metadata string
tag ::= string constant
```

Operand bundles are **not** part of a function’s signature, and a given function may be called from multiple places with different kinds of operand bundles. This reflects the fact that the operand bundles are conceptually a part of the `call` (or `invoke`), not the callee being dispatched to.

Operand bundles are a generic mechanism intended to support runtime-introspection-like functionality for managed languages. While the exact semantics of an operand bundle depend on the bundle tag, there are certain limitations to how much the presence of an operand bundle can influence the semantics of a program. These restrictions are described as the semantics of an “unknown” operand bundle. As long as the behavior of an operand bundle is describable within these restrictions, LLVM does not need to have special knowledge of the operand bundle to not miscompile programs containing it.

- The bundle operands for an unknown operand bundle escape in unknown ways before control is transferred to the callee or invokee.
- Calls and invokes with operand bundles have unknown read / write effect on the heap on entry and exit (even if the call target specifies a `memory` attribute), unless they’re overridden with callsite specific attributes.
- An operand bundle at a call site cannot change the implementation of the called function. Inter-procedural optimizations work as usual as long as they take into account the first two properties.

More specific types of operand bundles are described below.

Deoptimization operand bundles are characterized by the `"deopt"` operand bundle tag. These operand bundles represent an alternate “safe” continuation for the call site they’re attached to, and can be used by a suitable runtime to deoptimize the compiled frame at the specified call site. There can be at most one `"deopt"` operand bundle attached to a call site. Exact details of deoptimization are out of scope for the language reference, but it usually involves rewriting a compiled frame into a set of interpreted frames.

From the compiler’s perspective, deoptimization operand bundles make the call sites they’re attached to at least `readonly`. They read through all of their pointer typed operands (even if they’re not otherwise escaped) and the entire visible heap. Deoptimization operand bundles do not capture their operands except during deoptimization, in which case control will not be returned to the compiled frame.

The inliner knows how to inline through calls that have deoptimization operand bundles. Just like inlining through a normal call site involves composing the normal and exceptional continuations, inlining through a call site with a deoptimization operand bundle needs to appropriately compose the “safe” deoptimization continuation. The inliner does this by prepending the parent’s deoptimization continuation to every deoptimization continuation in the inlined body. E.g. inlining `@f` into `@g` in the following example

```llvm
define void @f() {
  call void @x()  ;; no deopt state
  call void @y() [ "deopt"(i32 10) ]
  call void @y() [ "deopt"(i32 10), "unknown"(ptr null) ]
  ret void
}

define void @g() {
  call void @f() [ "deopt"(i32 20) ]
  ret void
}
```

will result in

```llvm
define void @g() {
  call void @x()  ;; still no deopt state
  call void @y() [ "deopt"(i32 20, i32 10) ]
  call void @y() [ "deopt"(i32 20, i32 10), "unknown"(ptr null) ]
  ret void
}
```

It is the frontend’s responsibility to structure or encode the deoptimization state in a way that syntactically prepending the caller’s deoptimization state to the callee’s deoptimization state is semantically equivalent to composing the caller’s deoptimization continuation after the callee’s deoptimization continuation.

Funclet operand bundles are characterized by the `"funclet"` operand bundle tag. These operand bundles indicate that a call site is within a particular funclet. There can be at most one `"funclet"` operand bundle attached to a call site and it must have exactly one bundle operand.

If any funclet EH pads have been “entered” but not “exited” (per the description in the EH doc), it is undefined behavior to execute a `call` or `invoke` which:

- does not have a `"funclet"` bundle and is not a `call` to a nounwind intrinsic, or
- has a `"funclet"` bundle whose operand is not the most-recently-entered not-yet-exited funclet EH pad.

Similarly, if no funclet EH pads have been entered-but-not-yet-exited, executing a `call` or `invoke` with a `"funclet"` bundle is undefined behavior.

GC transition operand bundles are characterized by the `"gc-transition"` operand bundle tag. These operand bundles mark a call as a transition between a function with one GC strategy to a function with a different GC strategy. If coordinating the transition between GC strategies requires additional code generation at the call site, these bundles may contain any values that are needed by the generated code. For more details, see GC Transitions.

The bundle contains an arbitrary list of Values which need to be passed to GC transition code. They will be lowered and passed as operands to the appropriate `GC_TRANSITION` nodes in the selection DAG. It is assumed that these arguments must be available before and after (but not necessarily during) the execution of the callee.

Operand bundles on an llvm.assume allow representing assumptions that hold at the location of the assume. Operand bundles enable assumptions that are either hard or impossible to represent as a boolean argument of an llvm.assume.

Assumes with operand bundles must have `i1 true` as the condition operand.

Just like for the argument of llvm.assume, if any of the provided guarantees are violated at runtime the behavior is undefined.

While attributes expect constant arguments, assume operand bundles may be provided a dynamic value, for example:

```llvm
call void @llvm.assume(i1 true) ["align"(ptr %val, i32 %align)]
```

The following attributes are currently accepted:

**`"align"(ptr %p, i64 %align)`, `"align"(ptr %p, i64 %align, i64 %offset)`**

Equivalent to align(%align) on `%p`, or `%p - %offset` if the `%offset` argument exists, except that `%align` may be a non-power-of-two alignment (including a zero alignment). If `%align` is not a power of two the pointer value must be all-zero. Otherwise the behavior is undefined.

**`"cold"()`**

Equivalent to cold.

**`"dereferenceable"(ptr %p, i64 %size)`**

Equivalent to dereferenceable(%size) on `%p`, except that `%size` may also be zero, in which case the bundle doesn’t imply `nonnull`.

**`"dereferenceable_or_null"(ptr %p, i64 %size)`**

Equivalent to dereferenceable_or_null(%size) on `%p`, except that `%size` may also be zero.

**`"ignore"(...)`**

Doesn’t imply anything and is ignored. This is used to drop an assume where the `llvm.assume` call cannot be replaced or dropped.

**`"nonnull"(ptr %p)`**

Equivalent to nonnull on `%p`.

**`"noundef"(any_type %v)`**

Equivalent to noundef on `%v`.

**`"separate_storage"(ptr %p1, ptr %p2)`**

This indicates that no pointer based on one of its arguments can alias any pointer based on the other.

For example:

```llvm
call void @llvm.assume(i1 true) ["align"(ptr %val, i32 8)]
```

allows the optimizer to assume that at location of call to llvm.assume `%val` has an alignment of at least 8.

```llvm
call void @llvm.assume(i1 true) ["cold"(), "nonnull"(ptr %val)]
```

allows the optimizer to assume that the llvm.assume call location is cold and that `%val` may not be null.

Even if the assumed property can be encoded as a boolean value, like `nonnull`, using operand bundles to express the property can still have benefits:

- Attributes that can be expressed via operand bundles are directly the property that the optimizer uses and cares about. Encoding attributes as operand bundles removes the need for an instruction sequence that represents the property (e.g., *icmp ne ptr %p, null* for *nonnull*) and for the optimizer to deduce the property from that instruction sequence.
- Expressing the property using operand bundles makes it easy to identify the use of the value as a use in an llvm.assume. This then simplifies and improves heuristics, e.g., for use “use-sensitive” optimizations.

Preallocated operand bundles are characterized by the `"preallocated"` operand bundle tag. These operand bundles allow separation of the allocation of the call argument memory from the call site. This is necessary to pass non-trivially copyable objects by value in a way that is compatible with MSVC on some targets. There can be at most one `"preallocated"` operand bundle attached to a call site and it must have exactly one bundle operand, which is a token generated by `@llvm.call.preallocated.setup`. A call with this operand bundle should not adjust the stack before entering the function, as that will have been done by one of the `@llvm.call.preallocated.*` intrinsics.

```llvm
%foo = type { i64, i32 }

...

%t = call token @llvm.call.preallocated.setup(i32 1)
%a = call ptr @llvm.call.preallocated.arg(token %t, i32 0) preallocated(%foo)
; initialize %b
call void @bar(i32 42, ptr preallocated(%foo) %a) ["preallocated"(token %t)]
```

A “gc-live” operand bundle is only valid on a gc.statepoint intrinsic. The operand bundle must contain every pointer to a garbage collected object which potentially needs to be updated by the garbage collector.

When lowered, any relocated value will be recorded in the corresponding stackmap entry. See the intrinsic description for further details.

A `"clang.arc.attachedcall"` operand bundle on a call indicates the call is implicitly followed by a marker instruction and a call to an ObjC runtime function that uses the result of the call. The operand bundle takes a mandatory pointer to the runtime function (`@objc_retainAutoreleasedReturnValue` or `@objc_unsafeClaimAutoreleasedReturnValue`). The return value of a call with this bundle is used by a call to `@llvm.objc.clang.arc.noop.use` unless the called function’s return type is void, in which case the operand bundle is ignored.
