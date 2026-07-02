---
title: "LLVM Language Reference Manual (part 2/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 2/20
---

# LLVM Language Reference Manual

Aliases have a name and an aliasee that is either a global value or a constant expression.

Aliases may have an optional linkage type, an optional runtime preemption specifier, an optional visibility style, an optional DLL storage class and an optional tls model.

Syntax:

```
@<Name> = [Linkage] [PreemptionSpecifier] [Visibility] [DLLStorageClass] [ThreadLocal] [(unnamed_addr|local_unnamed_addr)] alias <AliaseeTy>, <AliaseeTy>* @<Aliasee>
          [, partition "name"]
```

The linkage must be one of `private`, `internal`, `linkonce`, `weak`, `linkonce_odr`, `weak_odr`, `external`, `available_externally`. Note that some system linkers might not correctly handle dropping a weak symbol that is aliased.

Aliases that are not `unnamed_addr` are guaranteed to have the same address as the aliasee expression. `unnamed_addr` ones are only guaranteed to point to the same content.

If the `local_unnamed_addr` attribute is given, the address is known to not be significant within the module.

Since aliases are only a second name, some restrictions apply, of which some can only be checked when producing an object file:

- The expression defining the aliasee must be computable at assembly time. Since it is just a name, no relocations can be used.
- No alias in the expression can be weak as the possibility of the intermediate alias being overridden cannot be represented in an object file.
- If the alias has the `available_externally` linkage, the aliasee must be an `available_externally` global value; otherwise the aliasee can be an expression but no global value in the expression can be a declaration, since that would require a relocation, which is not possible.
- If either the alias or the aliasee may be replaced by a symbol outside the module at link time or runtime, any optimization cannot replace the alias with the aliasee, since the behavior may be different. The alias may be used as a name guaranteed to point to the content in the current module.

IFuncs, like aliases, don’t create any new data or func. They are just a new symbol that is resolved at runtime by calling a resolver function.

On ELF platforms, IFuncs are resolved by the dynamic linker at load time. On Mach-O platforms, they are lowered in terms of `.symbol_resolver` functions, which lazily resolve the callee the first time they are called.

IFunc may have an optional linkage type, an optional visibility style, an option partition, and an optional list of attached metadata.

Syntax:

```
@<Name> = [Linkage] [PreemptionSpecifier] [Visibility] ifunc <IFuncTy>, <ResolverTy>* @<Resolver>
          [, partition "name"] (, !name !N)*
```

Comdat IR provides access to object file COMDAT/section group functionality which represents interrelated sections.

Comdats have a name which represents the COMDAT key and a selection kind to provide input on how the linker deduplicates comdats with the same key in two different object files. A comdat must be included or omitted as a unit. Discarding the whole comdat is allowed but discarding a subset is not.

A global object may be a member of at most one comdat. Aliases are placed in the same COMDAT that their aliasee computes to, if any.

Syntax:

```
$<Name> = comdat SelectionKind
```

For selection kinds other than `nodeduplicate`, only one of the duplicate comdats may be retained by the linker and the members of the remaining comdats must be discarded. The following selection kinds are supported:

**`any`**

The linker may choose any COMDAT key, the choice is arbitrary.

**`exactmatch`**

The linker may choose any COMDAT key but the sections must contain the same data.

**`largest`**

The linker will choose the section containing the largest COMDAT key.

**`nodeduplicate`**

No deduplication is performed.

**`samesize`**

The linker may choose any COMDAT key but the sections must contain the same amount of data.

- XCOFF and Mach-O don’t support COMDATs.
- COFF supports all selection kinds. Non-`nodeduplicate` selection kinds need a non-local linkage COMDAT symbol.
- ELF supports `any` and `nodeduplicate`.
- WebAssembly only supports `any`.

Here is an example of a COFF COMDAT where a function will only be selected if the COMDAT key’s section is the largest:

```
$foo = comdat largest
@foo = global i32 2, comdat($foo)

define void @bar() comdat($foo) {
  ret void
}
```

In a COFF object file, this will create a COMDAT section with selection kind `IMAGE_COMDAT_SELECT_LARGEST` containing the contents of the `@foo` symbol and another COMDAT section with selection kind `IMAGE_COMDAT_SELECT_ASSOCIATIVE` which is associated with the first COMDAT section and contains the contents of the `@bar` symbol.

As a syntactic sugar the `$name` can be omitted if the name is the same as the global name:

```llvm
$foo = comdat any
@foo = global i32 2, comdat
@bar = global i32 3, comdat($foo)
```

There are some restrictions on the properties of the global object. It, or an alias to it, must have the same name as the COMDAT group when targeting COFF. The contents and size of this object may be used during link-time to determine which COMDAT groups get selected depending on the selection kind. Because the name of the object must match the name of the COMDAT group, the linkage of the global object must not be local; local symbols can get renamed if a collision occurs in the symbol table.

The combined use of COMDATS and section attributes may yield surprising results. For example:

```llvm
$foo = comdat any
$bar = comdat any
@g1 = global i32 42, section "sec", comdat($foo)
@g2 = global i32 42, section "sec", comdat($bar)
```

From the object file perspective, this requires the creation of two sections with the same name. This is necessary because both globals belong to different COMDAT groups and COMDATs, at the object file level, are represented by sections.

Note that certain IR constructs like global variables and functions may create COMDATs in the object file in addition to any which are specified using COMDAT IR. This arises when the code generator is configured to emit globals in individual sections (e.g., when *-data-sections* or *-function-sections* is supplied to *llc*).

The return type and each parameter of a function type may have a set of *parameter attributes* associated with them. Parameter attributes are used to communicate additional information about the result or parameters of a function. Parameter attributes are considered to be part of the function, not of the function type, so functions with different parameter attributes can have the same function type. Parameter attributes can be placed both on function declarations/definitions, and at call-sites.

Parameter attributes are either simple keywords or strings that follow the specified type. Multiple parameter attributes, when required, are separated by spaces. For example:

```llvm
; On function declarations/definitions:
declare i32 @printf(ptr noalias captures(none), ...)
declare i32 @atoi(i8 zeroext)
declare signext i8 @returns_signed_char()
define void @baz(i32 "amdgpu-flat-work-group-size"="1,256" %x)

; On call-sites:
call i32 @atoi(i8 zeroext %x)
call signext i8 @returns_signed_char()
```

Note that any attributes for the function result (`nonnull`, `signext`) come before the result type.

Parameter attributes can be broadly separated into two kinds: ABI attributes that affect how values are passed to/from functions, like `zeroext`, `inreg`, `byval`, or `sret`. And optimization attributes, which provide additional optimization guarantees, like `noalias`, `nonnull` and `dereferenceable`.

ABI attributes must be specified *both* at the function declaration/definition and call-site, otherwise the behavior may be undefined. ABI attributes cannot be safely dropped. Optimization attributes do not have to match between call-site and function: The intersection of their implied semantics applies. Optimization attributes can also be freely dropped.

If an integer argument to a function is not marked signext/zeroext/noext, the kind of extension used is target-specific. Some targets depend for correctness on the kind of extension to be explicitly specified.

Currently, only the following parameter attributes are defined:

**`zeroext`**

This indicates to the code generator that the parameter or return value should be zero-extended to the extent required by the target’s ABI by the caller (for a parameter) or the callee (for a return value).

**`signext`**

This indicates to the code generator that the parameter or return value should be sign-extended to the extent required by the target’s ABI (which is usually 32-bits) by the caller (for a parameter) or the callee (for a return value).

**`noext`**

This indicates to the code generator that the parameter or return value has the high bits undefined, as for a struct in a register, and therefore does not need to be sign or zero extended. This is the same as default behavior and is only actually used (by some targets) to validate that one of the attributes is always present.

**`inreg`**

This indicates that this parameter or return value should be treated in a special target-dependent fashion while emitting code for a function call or return (usually, by putting it in a register as opposed to memory, though some targets use it to distinguish between two different kinds of registers). Use of this attribute is target-specific.

**`byval(<ty>)`**

This indicates that the pointer parameter should really be passed by value to the function. The attribute implies that a hidden copy of the pointee is made between the caller and the callee, so the callee is unable to modify the value in the caller. This attribute is only valid on LLVM pointer arguments. It is generally used to pass structs and arrays by value, but is also valid on pointers to scalars. The copy is considered to belong to the caller not the callee (for example, `readonly` functions should not write to `byval` parameters). This is not a valid attribute for return values.

The byval type argument is only used for its allocation size and alignment (if there is no explicit align attribute). That is, the hidden copy is interpreted as a call to memcpy with the allocation size of the specified type, instead of loading from the pointee and storing back into the copy in the type. In particular, the padding between field types of a struct type is still copied.

The byval attribute also supports specifying an alignment with the `align` attribute. It indicates the alignment of the stack slot to form and the known alignment of the pointer specified to the call site. If the alignment is not specified, then the code generator makes a target-specific assumption.

`byref(<ty>)`

> The `byref` argument attribute allows specifying the pointee memory type of an argument. This is similar to `byval`, but does not imply a copy is made anywhere, or that the argument is passed on the stack. This implies the pointer is dereferenceable up to the storage size of the type.
> 
> It is not generally permissible to introduce a write to a `byref` pointer. The pointer may have any address space and may be read only.
> 
> This is not a valid attribute for return values.
> 
> The alignment for a `byref` parameter can be explicitly specified by combining it with the `align` attribute, similar to `byval`. If the alignment is not specified, then the code generator makes a target-specific assumption.
> 
> This is intended for representing ABI constraints, and is not intended to be inferred for optimization use.

**`preallocated(<ty>)`**

This indicates that the pointer parameter should really be passed by value to the function, and that the pointer parameter’s pointee has already been initialized before the call instruction. This attribute is only valid on LLVM pointer arguments. The argument must be the value returned by the appropriate llvm.call.preallocated.arg on non `musttail` calls, or the corresponding caller parameter in `musttail` calls, although it is ignored during codegen.

A non `musttail` function call with a `preallocated` attribute in any parameter must have a `"preallocated"` operand bundle. A `musttail` function call cannot have a `"preallocated"` operand bundle.

The preallocated attribute requires a type argument.

The preallocated attribute also supports specifying an alignment with the `align` attribute. It indicates the alignment of the stack slot to form and the known alignment of the pointer specified to the call site. If the alignment is not specified, then the code generator makes a target-specific assumption.

`inalloca(<ty>)`

> The `inalloca` argument attribute allows the caller to take the address of outgoing stack arguments. An `inalloca` argument must be a pointer to stack memory produced by an `alloca` instruction. The alloca, or argument allocation, must also be tagged with the inalloca keyword. Only the last argument may have the `inalloca` attribute, and that argument is guaranteed to be passed in memory.
> 
> An argument allocation may be used by a call at most once because the call may deallocate it. The `inalloca` attribute cannot be used in conjunction with other attributes that affect argument storage, like `inreg`, `nest`, `sret`, or `byval`. The `inalloca` attribute also disables LLVM’s implicit lowering of large aggregate return values, which means that frontend authors must lower them with `sret` pointers.
> 
> When the call site is reached, the argument allocation must have been the most recent stack allocation that is still live, or the behavior is undefined. It is possible to allocate additional stack space after an argument allocation and before its call site, but it must be cleared off with llvm.stackrestore.
> 
> The `inalloca` attribute requires a type argument.
> 
> See Design and Usage of the InAlloca Attribute for more information on how to use this attribute.

**`sret(<ty>)`**

This indicates that the pointer parameter specifies the address of a structure that is the return value of the function in the source program. This pointer must be guaranteed by the caller to be valid: loads and stores to the structure may be assumed by the callee not to trap and to be properly aligned.

The sret type argument specifies the in-memory type.

A function that accepts an `sret` argument must return `void`. A return value may not be `sret`.

`elementtype(<ty>)`

> The `elementtype` argument attribute can be used to specify a pointer element type in a way that is compatible with opaque pointers.
> 
> The `elementtype` attribute by itself does not carry any specific semantics. However, certain intrinsics may require this attribute to be present and assign it particular semantics. This will be documented on individual intrinsics.
> 
> The attribute may only be applied to pointer typed arguments or return values of intrinsic calls. It cannot be applied to non-intrinsic calls, and cannot be applied to parameters on function declarations. For non-opaque pointers, the type passed to `elementtype` must match the pointer element type.

**`align <n>` or `align(<n>)`**

This indicates that the pointer value or vector of pointers has the specified alignment. If applied to a vector of pointers, *all* pointers (elements) have the specified alignment. If the pointer value does not have the specified alignment, poison value is returned or passed instead. The `align` attribute should be combined with the `noundef` attribute to ensure a pointer is aligned, or otherwise the behavior is undefined. Note that `align 1` has no effect on non-byval, non-preallocated arguments.

Note that this attribute has additional semantics when combined with the `byval` or `preallocated` attribute, which are documented there.

**`noalias`**

This indicates that memory locations accessed via pointer values based on the argument or return value are not also accessed, during the execution of the function, via pointer values not *based* on the argument or return value. This guarantee only holds for memory locations that are *modified*, by any means, during the execution of the function. If there are other accesses not based on the argument or return value, the behavior is undefined. The attribute on a return value also has additional semantics, as described below. Both the caller and the callee share the responsibility of ensuring that these requirements are met. For further details, please see the discussion of the NoAlias response in alias analysis.

Note that this definition of `noalias` is intentionally similar to the definition of `restrict` in C99 for function arguments.

For function return values, C99’s `restrict` is not meaningful, while LLVM’s `noalias` is. Furthermore, the semantics of the `noalias` attribute on return values are stronger than the semantics of the attribute when used on function arguments. On function return values, the `noalias` attribute indicates that the function acts like a system memory allocation function, returning a pointer to allocated storage disjoint from the storage for any other object accessible to the caller.

**`captures(...)`**

This attribute restricts the ways in which the callee may capture the pointer. This is not a valid attribute for return values. This attribute applies only to the particular copy of the pointer passed in this argument.

The arguments of `captures` are a list of captured pointer components, which may be `none`, or a combination of:

- `address`: The integral address of the pointer.
- `address_is_null` (subset of `address`): Whether the address is null.
- `provenance`: The ability to access the pointer for both read and write after the function returns.
- `read_provenance` (subset of `provenance`): The ability to access the pointer only for reads after the function returns.

Additionally, it is possible to specify that some components are only captured in certain locations. Currently only the return value (`ret`) and other (default) locations are supported.

The pointer capture section discusses these semantics in more detail.

Some examples of how to use the attribute:

- `captures(none)`: Pointer not captured.
- `captures(address, provenance)`: Equivalent to omitting the attribute.
- `captures(address)`: Address may be captured, but not provenance.
- `captures(address_is_null)`: Only captures whether the address is null.
- `captures(address, read_provenance)`: Both address and provenance captured, but only for read-only access.
- `captures(ret: address, provenance)`: Pointer captured through return value only.
- `captures(address_is_null, ret: address, provenance)`: The whole pointer is captured through the return value, and additionally whether the pointer is null is captured in some other way.

**`nofree`**

This indicates that a pointer based on this argument cannot be freed during the execution of the function.

More formally, a `nofree` argument provides the callee with a new pointer with the same address and a derived provenance, where the derived provenance has the same permissions as the original, except that the underlying object cannot be freed until the function returns (or unwinds), otherwise the behavior is undefined. This includes frees of the pointer on other threads if the free *happens-before* the function return.

Notably, it is still possible to free the underlying object through a pointer that is not based on the argument.

This is not a valid attribute for return values.

**`nest`**

This indicates that the pointer parameter can be excised using the trampoline intrinsics. This is not a valid attribute for return values and can only be applied to one parameter.

**`returned`**

This indicates that the function always returns the argument as its return value. This is a hint to the optimizer and code generator used when generating the caller, allowing value propagation, tail call optimization, and omission of register saves and restores in some cases; it is not checked or enforced when generating the callee. The parameter and the function return type must be valid operands for the bitcast instruction. This is not a valid attribute for return values and can only be applied to one parameter.

**`nonnull`**

This indicates that the parameter or return pointer is not null. This attribute may only be applied to pointer-typed parameters. This is not checked or enforced by LLVM; if the parameter or return pointer is null, poison value is returned or passed instead. The `nonnull` attribute only refers to the address bits of the pointers. If all the address bits are zero, the result will be a poison value, even if the pointer has non-zero non-address bits or non-zero external state. The `nonnull` attribute should be combined with the `noundef` attribute to ensure a pointer is not null or otherwise the behavior is undefined.

**`dereferenceable(<n>)`**

This indicates that the parameter or return pointer is dereferenceable. This attribute may only be applied to pointer-typed parameters. A pointer that is dereferenceable can be loaded from speculatively without a risk of trapping. The number of bytes known to be dereferenceable must be provided in parentheses. The `nonnull` attribute does not imply dereferenceability (consider a pointer to one element past the end of an array), however `dereferenceable(<n>)` does imply `nonnull` in `addrspace(0)` (which is the default address space), except if the `null_pointer_is_valid` function attribute is present. `n` should be a positive number. The pointer should be well defined, otherwise it is undefined behavior. This means `dereferenceable(<n>)` implies `noundef`.

**`dereferenceable_or_null(<n>)`**

This indicates that the parameter or return value isn’t both non-null and non-dereferenceable (up to `<n>` bytes) at the same time. All non-null pointers tagged with `dereferenceable_or_null(<n>)` are `dereferenceable(<n>)`. For address space 0 `dereferenceable_or_null(<n>)` implies that a pointer is exactly one of `dereferenceable(<n>)` or `null`, and in other address spaces `dereferenceable_or_null(<n>)` implies that a pointer is at least one of `dereferenceable(<n>)` or `null` (i.e., it may be both `null` and `dereferenceable(<n>)`). This attribute may only be applied to pointer-typed parameters.

**`swiftself`**

This indicates that the parameter is the self/context parameter. This is not a valid attribute for return values and can only be applied to one parameter.

**`swiftasync`**

This indicates that the parameter is the asynchronous context parameter and triggers the creation of a target-specific extended frame record to store this pointer. This is not a valid attribute for return values and can only be applied to one parameter.

**`swifterror`**

This attribute is motivated to model and optimize Swift error handling. It can be applied to a parameter with pointer-to-pointer type or a pointer-sized alloca. At the call site, the actual argument that corresponds to a `swifterror` parameter has to come from a `swifterror` alloca or the `swifterror` parameter of the caller. A `swifterror` value (either the parameter or the alloca) can only be loaded and stored from, or used as a `swifterror` argument. This is not a valid attribute for return values and can only be applied to one parameter.

These constraints allow the calling convention to optimize access to `swifterror` variables by associating them with a specific register at call boundaries rather than placing them in memory. Since this does change the calling convention, a function which uses the `swifterror` attribute on a parameter is not ABI-compatible with one which does not.

These constraints also allow LLVM to assume that a `swifterror` argument does not alias any other memory visible within a function and that a `swifterror` alloca passed as an argument does not escape.

**`immarg`**

This indicates the parameter is required to be an immediate value. This must be a trivial immediate integer or floating-point constant. Undef or constant expressions are not valid. This is only valid on intrinsic declarations and cannot be applied to a call site or arbitrary function.

**`noundef`**

This attribute applies to parameters and return values. If the value representation contains any undefined or poison bits, the behavior is undefined. Note that this does not refer to padding introduced by the type’s storage representation.

If memory sanitizer is enabled, `noundef` becomes an ABI attribute and must match between the call-site and the function definition.

**`nofpclass(<test mask>)`**

This attribute applies to parameters and return values with floating-point and vector of floating-point types, as well as supported aggregates of such types (matching the supported types for fast-math flags). The test mask has the same format as the second argument to the llvm.is.fpclass, and indicates which classes of floating-point values are not permitted for the value. For example, a bitmask of 3 indicates the parameter may not be a NaN.

If the value is a floating-point class indicated by the `nofpclass` test mask, a poison value is passed or returned instead.

Listing 1

The following invariants hold

```
     @llvm.is.fpclass(nofpclass(test_mask) %x, test_mask) => false
     @llvm.is.fpclass(nofpclass(test_mask) %x, ~test_mask) => true
     nofpclass(all) => poison
```

> In textual IR, various string names are supported for readability and can be combined. For example `nofpclass(nan pinf nzero)` evaluates to a mask of 547.
> 
> This does not depend on the floating-point environment. For example, a function parameter marked `nofpclass(zero)` indicates no zero inputs. If this is applied to an argument in a function marked with denormal_fpenv indicating zero treatment of input denormals, it does not imply the value cannot be a denormal value which would compare equal to 0.

| Name | floating-point class | Bitmask value |
|---|---|---|
| nan | Any NaN | 3 |
| inf | +/- infinity | 516 |
| norm | +/- normal | 264 |
| sub | +/- subnormal | 144 |
| zero | +/- 0 | 96 |
| all | All values | 1023 |
| snan | Signaling NaN | 1 |
| qnan | Quiet NaN | 2 |
| ninf | Negative infinity | 4 |
| nnorm | Negative normal | 8 |
| nsub | Negative subnormal | 16 |
| nzero | Negative zero | 32 |
| pzero | Positive zero | 64 |
| psub | Positive subnormal | 128 |
| pnorm | Positive normal | 256 |
| pinf | Positive infinity | 512 |

**`alignstack(<n>)`**

This indicates the alignment that should be considered by the backend when assigning this parameter or return value to a stack slot during calling convention lowering. The enforcement of the specified alignment is target-dependent, as target-specific calling convention rules may override this value. This attribute serves the purpose of carrying language-specific alignment information that is not mapped to base types in the backend (for example, over-alignment specification through language attributes).

**`allocalign`**

The function parameter marked with this attribute is the alignment in bytes of the newly allocated block returned by this function. The returned value must either have the specified alignment or be the null pointer. The return value MAY be more aligned than the requested alignment, but not less aligned. Invalid (e.g., non-power-of-2) alignments are permitted for the allocalign parameter, so long as the returned pointer is null. This attribute may only be applied to integer parameters.

**`allocptr`**

The function parameter marked with this attribute is the pointer that will be manipulated by the allocator. For a realloc-like function the pointer will be invalidated upon success (but the same address may be returned), for a free-like function the pointer will always be invalidated.

**`readnone`**

This attribute indicates that the function does not dereference that pointer argument, even though it may read or write the memory that the pointer points to if accessed through other pointers.

If a function reads from or writes to a readnone pointer argument, the behavior is undefined.

**`readonly`**

This attribute indicates that the function does not write through this pointer argument, even though it may write to the memory that the pointer points to.

If a function writes to a readonly pointer argument, the behavior is undefined.

**`writeonly`**

This attribute indicates that the function may write to, but does not read through this pointer argument (even though it may read from the memory that the pointer points to).

This attribute is understood in the same way as the `memory(write)` attribute. That is, the pointer may still be read as long as the read is not observable outside the function. See the `memory` documentation for precise semantics.

**`writable`**

This attribute is only meaningful in conjunction with `dereferenceable(N)` or another attribute that implies the first `N` bytes of the pointer argument are dereferenceable.

In that case, the attribute indicates that the first `N` bytes will be (non-atomically) loaded and stored back on entry to the function.

This implies that it’s possible to introduce spurious stores on entry to the function without introducing traps or data races. This does not necessarily hold throughout the whole function, as the pointer may escape to a different thread during the execution of the function. See also the atomic optimization guide

The “other attributes” that imply dereferenceability are `dereferenceable_or_null` (if the pointer is non-null) and the `sret`, `byval`, `byref`, `inalloca`, `preallocated` family of attributes. Note that not all of these combinations are useful, e.g. `byval` arguments are known to be writable even without this attribute.

The `writable` attribute cannot be combined with `readnone`, `readonly` or a `memory` attribute that does not contain `argmem: write`.

**`initializes((Lo1, Hi1), ...)`**

This attribute indicates that the function initializes the ranges of the pointer parameter’s memory `[%p+LoN, %p+HiN)`. Colloquially, this means that all bytes in the specified range are written before the function returns, and not read prior to the initializing write. If the function unwinds, the write may not happen.

Formally, this is specified in terms of an “initialized” shadow state for all bytes in the range, which is set to “not initialized” at function entry. If a memory access is performed through a pointer based on the argument, and an accessed byte has not been marked as “initialized” yet, then:

> - If the byte is stored with a non-volatile, non-atomic write, mark it as “initialized”.
> - If the byte is stored with a volatile or atomic write, the behavior is undefined.
> - If the byte is loaded, return a poison value.

Additionally, if the function returns normally, write an undef value to all bytes that are part of the range and have not been marked as “initialized”.

This attribute only holds for the memory accessed via this pointer parameter. Other arbitrary accesses to the same memory via other pointers are allowed.

The `writable` or `dereferenceable` attribute do not imply the `initializes` attribute. The `initializes` attribute does not imply `writeonly` since `initializes` allows reading from the pointer after writing.

This attribute is a list of constant ranges in ascending order with no overlapping or consecutive list elements. `LoN/HiN` are 64-bit integers, and negative values are allowed in case the argument points partway into an allocation. An empty list is not allowed.

On a `byval` argument, `initializes` refers to the given parts of the callee copy being overwritten. A `byval` callee can never initialize the original caller memory passed to the `byval` argument.

**`dead_on_unwind`**

At a high level, this attribute indicates that the pointer argument is dead if the call unwinds, in the sense that the caller will not depend on the contents of the memory. Stores that would only be visible on the unwind path can be elided.

More precisely, the behavior is as-if any memory written through the pointer during the execution of the function is overwritten with a poison value on unwind. This includes memory written by the implicit write implied by the `writable` attribute. The caller is allowed to access the affected memory, but all loads that are not preceded by a store will return poison.

This attribute cannot be applied to return values.

**`dead_on_return` or `dead_on_return(<n>)`**

This attribute indicates that the memory pointed to by the argument is dead upon function return, both upon normal return and if the calls unwinds, meaning that the caller will not depend on its contents. Stores that would be observable either on the return path or on the unwind path may be elided. A number of bytes known to be dead may optionally be provided in parentheses. If a number of bytes is not specified, all memory reachable through the pointer is marked as dead on return.

Specifically, the behavior is as-if any memory written through the pointer during the execution of the function is overwritten with a poison value upon function return. The caller may access the memory, but any load not preceded by a store will return poison. If a byte count is specified, only writes within the specified range are overwritten with poison on function return.

This attribute does not imply aliasing properties. For pointer arguments that do not alias other memory locations, `noalias` attribute may be used in conjunction. Conversely, this attribute always implies `dead_on_unwind`. When a byte count is specified, `dead_on_unwind` is implied only for that range.

This attribute cannot be applied to return values.

**`range(<ty> <a>, <b>)`**

This attribute expresses the possible range of the parameter or return value. If the value is not in the specified range, it is converted to poison. The arguments passed to `range` have the following properties:

- The type must match the scalar type of the parameter or return value.
- The pair `a,b` represents the range `[a,b)`.
- Both `a` and `b` are constants.
- The range is allowed to wrap.
- The empty range is represented using `0,0`.
- Otherwise, `a` and `b` are not allowed to be equal.

This attribute may only be applied to parameters or return values with integer or vector of integer types.

For vector-typed parameters, the range is applied element-wise.

Each function may specify a garbage collector strategy name, which is simply a string:

```llvm
define void @f() gc "name" { ... }
```

The supported values of *name* include those built in to LLVM and any provided by loaded plugins. Specifying a GC strategy will cause the compiler to alter its output in order to support the named garbage collection algorithm. Note that LLVM itself does not contain a garbage collector, this functionality is restricted to generating machine code which can interoperate with a collector provided externally.

Prefix data is data associated with a function which the code generator will emit immediately before the function’s entrypoint. The purpose of this feature is to allow frontends to associate language-specific runtime metadata with specific functions and make it available through the function pointer while still allowing the function pointer to be called.

To access the data for a given function, a program may bitcast the function pointer to a pointer to the constant’s type and dereference index -1. This implies that the IR symbol points just past the end of the prefix data. For instance, take the example of a function annotated with a single `i32`,

```llvm
define void @f() prefix i32 123 { ... }
```

The prefix data can be referenced as,

```llvm
%a = getelementptr inbounds i32, ptr @f, i32 -1
%b = load i32, ptr %a
```

Prefix data is laid out as if it were an initializer for a global variable of the prefix data’s type. The function will be placed such that the beginning of the prefix data is aligned. This means that if the size of the prefix data is not a multiple of the alignment size, the function’s entrypoint will not be aligned. If alignment of the function’s entrypoint is desired, padding must be added to the prefix data.

A function may have prefix data but no body. This has similar semantics to the `available_externally` linkage in that the data may be used by the optimizers but will not be emitted in the object file.

The `prologue` attribute allows arbitrary code (encoded as bytes) to be inserted prior to the function body. This can be used for enabling function hot-patching and instrumentation.

To maintain the semantics of ordinary function calls, the prologue data must have a particular format. Specifically, it must begin with a sequence of bytes which decode to a sequence of machine instructions, valid for the module’s target, which transfer control to the point immediately succeeding the prologue data, without performing any other visible action. This allows the inliner and other passes to reason about the semantics of the function definition without needing to reason about the prologue data. Obviously this makes the format of the prologue data highly target dependent.

A trivial example of valid prologue data for the x86 architecture is `i8 144`, which encodes the `nop` instruction:

```
define void @f() prologue i8 144 { ... }
```

Generally prologue data can be formed by encoding a relative branch instruction which skips the metadata, as in this example of valid prologue data for the x86_64 architecture, where the first two bytes encode `jmp .+10`:

```
%0 = type <{ i8, i8, ptr }>

define void @f() prologue %0 <{ i8 235, i8 8, ptr @md}> { ... }
```

A function may have prologue data but no body. This has similar semantics to the `available_externally` linkage in that the data may be used by the optimizers but will not be emitted in the object file.

The `personality` attribute permits functions to specify what function to use for exception handling.

Attribute groups are groups of attributes that are referenced by objects within the IR. They are important for keeping `.ll` files readable, because a lot of functions will use the same set of attributes. In the degenerate case of a `.ll` file that corresponds to a single `.c` file, the single attribute group will capture the important command line flags used to build that file.

An attribute group is a module-level object. To use an attribute group, an object references the attribute group’s ID (e.g., `#37`). An object may refer to more than one attribute group. In that situation, the attributes from the different groups are merged.

Here is an example of attribute groups for a function that should always be inlined, has a stack alignment of 4, and which shouldn’t use SSE instructions:

```llvm
; Target-independent attributes:
attributes #0 = { alwaysinline alignstack=4 }

; Target-dependent attributes:
attributes #1 = { "no-sse" }

; Function @f has attributes: alwaysinline, alignstack=4, and "no-sse".
define void @f() #0 #1 { ... }
```

Function attributes are set to communicate additional information about a function. Function attributes are considered to be part of the function, not of the function type, so functions with different function attributes can have the same function type.

Function attributes are simple keywords or strings that follow the specified type. Multiple attributes, when required, are separated by spaces. For example:

```llvm
define void @f() noinline { ... }
define void @f() alwaysinline { ... }
define void @f() alwaysinline optsize { ... }
define void @f() optsize { ... }
define void @f() "no-sse" { ... }
```

**`alignstack(<n>)`**

This attribute indicates that, when emitting the prologue and epilogue, the backend should forcibly align the stack pointer. Specify the desired alignment, which must be a power of two, in parentheses.

**`"alloc-family"="FAMILY"`**

This indicates which “family” an allocator function is part of. To avoid collisions, the family name should match the mangled name of the primary allocator function, that is “malloc” for malloc/calloc/realloc/free, “_Znwm” for `::operator::new` and `::operator::delete`, and “_ZnwmSt11align_val_t” for aligned `::operator::new` and `::operator::delete`. Matching malloc/realloc/free calls within a family can be optimized, but mismatched ones will be left alone.

**`allockind("KIND")`**

Describes the behavior of an allocation function. The KIND string contains comma-separated entries from the following options:

- “alloc”: the function returns a new block of memory or null.
- “realloc”: the function returns a new block of memory or null. If the result is non-null the memory contents from the start of the block up to the smaller of the original allocation size and the new allocation size will match that of the `allocptr` argument and the `allocptr` argument is invalidated, even if the function returns the same address.
- “free”: the function frees the block of memory specified by `allocptr`. Functions marked as “free” `allockind` must return void.
- “uninitialized”: Any newly-allocated memory (either a new block from a “alloc” function or the enlarged capacity from a “realloc” function) will be uninitialized.
- “zeroed”: Any newly-allocated memory (either a new block from a “alloc” function or the enlarged capacity from a “realloc” function) will be zeroed.
- “aligned”: the function returns memory aligned according to the `allocalign` parameter.

The first three options are mutually exclusive, and the remaining options describe more details of how the function behaves. The remaining options are invalid for “free”-type functions.

Calls to functions annotated with `allockind` are subject to allocation elision: Calls to allocator functions can be removed, and the allocation served from a “virtual” allocator instead. Notably, this is allowed even if the allocator calls have side-effects. In other words, for each allocation there is a non-deterministic choice between calling the allocator as usual, or using a virtual, side-effect-free allocator instead.

If multiple allocation functions operate on the same allocation, allocation elision is only allowed for pairs of “alloc” and “free” with the same `"alloc-family"` attribute. For this purpose, a “realloc” call may be decomposed into “alloc” and “free” operations, as long as at least one of them will be elided.

**`"alloc-variant-zeroed"="FUNCTION"`**

This attribute indicates that another function is equivalent to an allocator function, but returns zeroed memory. The function must have “zeroed” allocation behavior, the same `alloc-family`, and take exactly the same arguments.

**`allocsize(<EltSizeParam>[, <NumEltsParam>])`**

This attribute indicates that the annotated function will always return at least a given number of bytes (or null). Its arguments are zero-indexed parameter numbers; if one argument is provided, then it’s assumed that at least `CallSite.Args[EltSizeParam]` bytes will be available at the returned pointer. If two are provided, then it’s assumed that `CallSite.Args[EltSizeParam] * CallSite.Args[NumEltsParam]` bytes are available. The referenced parameters must be integer types. No assumptions are made about the contents of the returned block of memory.

**`alwaysinline`**

This attribute indicates that the inliner should attempt to inline this function into callers whenever possible, ignoring any active inlining size threshold for this caller.

**`builtin`**

This indicates that the callee function at a call site should be recognized as a built-in function, even though the function’s declaration uses the `nobuiltin` attribute. This is only valid at call sites for direct calls to functions that are declared with the `nobuiltin` attribute.

**`cold`**

This attribute indicates that this function is rarely called. When computing edge weights, basic blocks post-dominated by a cold function call are also considered to be cold and, thus, given a low weight.

**`convergent`**

This attribute indicates that this function is convergent. When it appears on a call/invoke, the convergent attribute indicates that we should treat the call as though we’re calling a convergent function. This is particularly useful on indirect calls; without this we may treat such calls as though the target is non-convergent.

See Convergent Operation Semantics for further details.

It is an error to call llvm.experimental.convergence.entry from a function that does not have this attribute.

**`disable_sanitizer_instrumentation`**

When instrumenting code with sanitizers, it can be important to skip certain functions to ensure no instrumentation is applied to them.

This attribute is not always similar to absent `sanitize_<name>` attributes: depending on the specific sanitizer, code can be inserted into functions regardless of the `sanitize_<name>` attribute to prevent false positive reports.

`disable_sanitizer_instrumentation` disables all kinds of instrumentation, taking precedence over the `sanitize_<name>` attributes and other compiler flags.

**`"dontcall-error"`**

This attribute denotes that an error diagnostic should be emitted when a call of a function with this attribute is not eliminated via optimization. Front ends can provide optional `srcloc` metadata nodes on call sites of such callees to attach information about where in the source language such a call came from. A string value can be provided as a note.

**`"dontcall-warn"`**

This attribute denotes that a warning diagnostic should be emitted when a call of a function with this attribute is not eliminated via optimization. Front ends can provide optional `srcloc` metadata nodes on call sites of such callees to attach information about where in the source language such a call came from. A string value can be provided as a note.

**`fn_ret_thunk_extern`**

This attribute tells the code generator that returns from functions should be replaced with jumps to externally-defined architecture-specific symbols. For X86, this symbol’s identifier is `__x86_return_thunk`.

**`"frame-pointer"`**

This attribute tells the code generator whether the function should keep the frame pointer. The code generator may emit the frame pointer even if this attribute says the frame pointer can be eliminated. The allowed string values are:

> - `"none"` (default) - the frame pointer can be eliminated, and its register can be used for other purposes.
> - `"reserved"` - the frame pointer register must either be updated to point to a valid frame record for the current function, or not be modified.
> - `"non-leaf"` - the frame pointer should be kept if the function calls other functions.
> - `"all"` - the frame pointer should be kept.

**`hot`**

This attribute indicates that this function is a hot spot of the program execution. The function will be optimized more aggressively and will be placed into a special subsection of the text section to improve locality.

When profile feedback is enabled, this attribute takes precedence over the profile information. By marking a function `hot`, users can work around the cases where the training input does not have good coverage on all the hot functions.

**`inlinehint`**

This attribute indicates that the source code contained a hint that inlining this function is desirable (such as the “inline” keyword in C/C++). It is just a hint; it imposes no requirements on the inliner.

**`jumptable`**
