---
title: "LLVM Language Reference Manual (part 5/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 5/20
---

# LLVM Language Reference Manual

| `i1` | a single-bit integer. |
|---|---|
| `i32` | a 32-bit integer. |
| `i1942652` | a really big integer of over 1 million bits. |

##### Byte Type

**Overview:**

The byte type represents raw memory data in SSA registers. It should be used when it cannot be determined whether a value holds a pointer or another type at run time, or if the value contains uninitialized or poison data. Frontends are expected to use a byte type when:

1. Lowering memory operations like *memcpy* and *memmove* to load/store pairs without knowing the underlying type being copied.
2. Working with union types that can hold a pointer alongside a non-pointer type.
3. Working with possibly uninitialized data.

Otherwise, when known, the specific type should be used. Each bit can be:

- An integer bit (0 or 1)
- Part of a pointer value
- `poison`

Any bit width from 1 bit to 223(about 8 million) can be specified.

The per-bit semantics described above (poison and conditional pointer provenance preservation) are mid-end only. At the IR-to-MIR boundary both SelectionDAG and GlobalISel lower `bN` as the equi-sized integer scalar (`iN`/`sN`); backend passes do not see the byte type and do not preserve its bit-level semantics.

**Syntax:**

```
bN
```

The number of bits the byte occupies is specified by the `N` value.

###### Examples:

| `b1` | a single-bit byte value. |
|---|---|
| `b32` | a 32-bit byte value. |
| `b128` | a 128-bit byte value. |

##### Floating-Point Types

| Type | Description |
|---|---|
| `half` | 16-bit floating-point value (IEEE 754 binary16) |
| `bfloat` | 16-bit “brain” floating-point value (7-bit significand). Provides the same number of exponent bits as `float`, so that it matches its dynamic range, but with greatly reduced precision. Used in Intel’s AVX-512 BF16 extensions and Arm’s ARMv8.6-A extensions, among others. |
| `float` | 32-bit floating-point value (IEEE 754 binary32) |
| `double` | 64-bit floating-point value (IEEE 754 binary64) |
| `fp128` | 128-bit floating-point value (IEEE 754 binary128) |
| `x86_fp80` | 80-bit floating-point value (X87) |
| `ppc_fp128` | 128-bit floating-point value (two 64-bits) |

##### X86_amx Type

**Overview:**

The x86_amx type represents a value held in an AMX tile register on an x86 machine. The operations allowed on it are quite limited. Only a few intrinsics are allowed: stride load and store, zero and dot product. No instruction is allowed for this type. There are no arguments, arrays, pointers, vectors or constants of this type.

**Syntax:**

```
x86_amx
```

##### Pointer Type

**Overview:**

The pointer type `ptr` is used to specify memory locations. Pointers are commonly used to reference objects in memory.

Pointer types may have an optional address space attribute defining the numbered address space where the pointed-to object resides. For example, `ptr addrspace(5)` is a pointer to address space 5. In addition to integer constants, `addrspace` can also reference one of the address spaces defined in the datalayout string. `addrspace("A")` will use the alloca address space, `addrspace("G")` the default globals address space and `addrspace("P")` the program address space.

The representation of pointers can be different for each address space and does not necessarily need to be a plain integer address (e.g., for non-integral pointers). In addition to a representation bits size, pointers in each address space also have an index size which defines the bitwidth of indexing operations as well as the size of *integer addresses* in this address space. For example, CHERI capabilities are twice the size of the underlying addresses to accommodate for additional metadata such as bounds and permissions: on a 32-bit system the bitwidth of the pointer representation size is 64, but the underlying address width remains 32 bits.

The default address space is number zero.

The semantics of non-zero address spaces are target-specific. Memory access through a non-dereferenceable pointer is undefined behavior in any address space. Pointers with the bit-value 0 are only assumed to be non-dereferenceable in address space 0, unless the function is marked with the `null_pointer_is_valid` attribute. However, *volatile* access to any non-dereferenceable address may have defined behavior (according to the target), and in this case the attribute is not needed even for address 0.

If an object can be proven accessible through a pointer with a different address space, the access may be modified to use that address space. Exceptions apply if the operation is `volatile`.

Prior to LLVM 15, pointer types also specified a pointee type, such as `i8*`, `[4 x i32]*` or `i32 (i32*)*`. In LLVM 15, such “typed pointers” are still supported under non-default options. See the opaque pointers document for more information.

##### Target Extension Type

**Overview:**

Target extension types represent types that must be preserved through optimization, but are otherwise generally opaque to the compiler. They may be used as function parameters or arguments, and in phi or select instructions. Some types may be also used in alloca instructions or as global values, and correspondingly it is legal to use load and store instructions on them. Full semantics for these types are defined by the target.

The only constants that target extension types may have are `zeroinitializer`, `undef`, and `poison`. Other possible values for target extension types may arise from target-specific intrinsics and functions.

These types cannot be converted to other types. As such, it is not legal to use them in bitcast instructions (as a source or target type), nor is it legal to use them in ptrtoint or inttoptr instructions. Similarly, they are not legal to use in an icmp instruction.

Target extension types have a name and optional type or integer parameters. The meanings of name and parameters are defined by the target. When being defined in LLVM IR, all of the type parameters must precede all of the integer parameters.

Specific target extension types are registered with LLVM as having specific properties. These properties can be used to restrict the type from appearing in certain contexts, such as being the type of a global variable or having a `zeroinitializer` constant be valid. A complete list of type properties may be found in the documentation for `llvm::TargetExtType::Property` (doxygen).

**Syntax:**

```llvm
target("label")
target("label", void)
target("label", void, i32)
target("label", 0, 1, 2)
target("label", void, i32, 0, 1, 2)
```

##### Vector Type

**Overview:**

A vector type is a simple derived type that represents a vector of elements. Vector types are used when multiple primitive data are operated in parallel using a single instruction (SIMD). A vector type requires a size (number of elements), an underlying primitive data type, and a scalable property to represent vectors where the exact hardware vector length is unknown at compile time. Vector types are considered first class.

**Memory Layout:**

In general vector elements are laid out in memory in the same way as array types. Such an analogy works fine as long as the vector elements are byte sized. However, when the elements of the vector aren’t byte sized it gets a bit more complicated. One way to describe the layout is by describing what happens when a vector such as <N x iM> is bitcasted to an integer type with N*M bits, and then following the rules for storing such an integer to memory.

A bitcast from a vector type to a scalar integer type will see the elements being packed together (without padding). The order in which elements are inserted in the integer depends on endianness. For little endian element zero is put in the least significant bits of the integer, and for big endian element zero is put in the most significant bits.

Using a vector such as `<i4 1, i4 2, i4 3, i4 5>` as an example, together with the analogy that we can replace a vector store by a bitcast followed by an integer store, we get this for big endian:

```llvm
%val = bitcast <4 x i4> <i4 1, i4 2, i4 3, i4 5> to i16

; Bitcasting from a vector to an integral type can be seen as
; concatenating the values:
;   %val now has the hexadecimal value 0x1235.

store i16 %val, ptr %ptr

; In memory the content will be (8-bit addressing):
;
;    [%ptr + 0]: 00010010  (0x12)
;    [%ptr + 1]: 00110101  (0x35)
```

The same example for little endian:

```llvm
%val = bitcast <4 x i4> <i4 1, i4 2, i4 3, i4 5> to i16

; Bitcasting from a vector to an integral type can be seen as
; concatenating the values:
;   %val now has the hexadecimal value 0x5321.

store i16 %val, ptr %ptr

; In memory the content will be (8-bit addressing):
;
;    [%ptr + 0]: 00100001  (0x21)
;    [%ptr + 1]: 01010011  (0x53)
```

When `<N*M>` isn’t evenly divisible by the byte size the exact memory layout is unspecified (just like it is for an integral type of the same size). This is because different targets could put the padding at different positions when the type size is smaller than the type’s store size.

**Syntax:**

```
< <# elements> x <elementtype> >          ; Fixed-length vector
< vscale x <# elements> x <elementtype> > ; Scalable vector
```

The number of elements is a constant integer value larger than 0; elementtype may be any integer, floating-point, pointer type, or a sized target extension type that has the `CanBeVectorElement` property. Vectors of size zero are not allowed. For scalable vectors, the total number of elements is a constant multiple (called vscale) of the specified number of elements; vscale is a positive power-of-two integer that is unknown at compile time and the same hardware-dependent constant for all scalable vectors at run time. The size of a specific scalable vector type is thus constant within IR, even if the exact size in bytes cannot be determined until run time.

**Examples:**

| `<4 x i32>` | Vector of 4 32-bit integer values. |
|---|---|
| `<8 x float>` | Vector of 8 32-bit floating-point values. |
| `<2 x i64>` | Vector of 2 64-bit integer values. |
| `<4 x ptr>` | Vector of 4 pointers |
| `<vscale x 4 x i32>` | Vector with a multiple of 4 32-bit integer values. |

**Overview:**

The label type represents code labels.

**Syntax:**

```
label
```

**Overview:**

The token type is used when a value is associated with an instruction but all uses of the value must not attempt to introspect or obscure it. As such, it is not appropriate to have a phi or select of type token.

**Syntax:**

```
token
```

Aggregate Types are a subset of derived types that can contain multiple member types. Arrays and structs are aggregate types. Vectors are not considered to be aggregate types.

##### Array Type

**Overview:**

The array type is a very simple derived type that arranges elements sequentially in memory. The array type requires a size (number of elements) and an underlying data type.

**Syntax:**

```
[<# elements> x <elementtype>]
```

The number of elements is a constant integer value; `elementtype` may be any type with a size.

**Examples:**

| `[40 x i32]` | Array of 40 32-bit integer values. |
|---|---|
| `[41 x i32]` | Array of 41 32-bit integer values. |
| `[4 x i8]` | Array of 4 8-bit integer values. |

Here are some examples of multidimensional arrays:

| `[3 x [4 x i32]]` | 3x4 array of 32-bit integer values. |
|---|---|
| `[12 x [10 x float]]` | 12x10 array of single precision floating-point values. |
| `[2 x [3 x [4 x i16]]]` | 2x3x4 array of 16-bit integer values. |

There is no restriction on indexing beyond the end of the array implied by a static type (though there are restrictions on indexing beyond the bounds of an allocated object in some cases). This means that single-dimension ‘variable sized array’ addressing can be implemented in LLVM with a zero length array type. An implementation of ‘pascal style arrays’ in LLVM could use the type “`{ i32, [0 x float]}`”, for example.

##### Structure Type

**Overview:**

The structure type is used to represent a collection of data members together in memory. The elements of a structure may be any type that has a size.

Structures in memory are accessed using ‘`load`’ and ‘`store`’ by getting a pointer to a field with the ‘`getelementptr`’ instruction. Structures in registers are accessed using the ‘`extractvalue`’ and ‘`insertvalue`’ instructions.

Structures may optionally be “packed” structures, which indicate that the alignment of the struct is one byte, and that there is no padding between the elements. In non-packed structs, padding between field types is inserted as defined by the DataLayout string in the module, which is required to match what the underlying code generator expects.

Structures can either be “literal” or “identified”. A literal structure is defined inline with other types (e.g., `[2 x {i32, i32}]`) whereas identified types are always defined at the top level with a name. Literal types are uniqued by their contents and can never be recursive or opaque since there is no way to write one. Identified types can be opaqued and are never uniqued. Identified types must not be recursive.

**Syntax:**

```
%T1 = type { <type list> }     ; Identified normal struct type
%T2 = type <{ <type list> }>   ; Identified packed struct type
```

**Examples:**

| `{ i32, i32, i32 }` | A triple of three `i32` values (this is a “homogeneous” struct as all element types are the same) |
|---|---|
| `{ float, ptr }` | A pair, where the first element is a `float` and the second element is a pointer. |
| `<{ i8, i32 }>` | A packed struct known to be 5 bytes in size. |

LLVM has several different basic types of constants. This section describes them all and their syntax.

****Boolean constants****

The two strings ‘`true`’ and ‘`false`’ are both valid constants of the `i1` type.

****Integer constants****

Standard integers (such as ‘4’) are constants of the integer type. They can be either decimal or hexadecimal. Decimal integers can be prefixed with - to represent negative integers, e.g., ‘`-1234`’. Hexadecimal integers must be prefixed with either u or s to indicate whether they are unsigned or signed respectively. e.g ‘`u0x8000`’ gives 32768, whilst ‘`s0x8000`’ gives -32768.

Note that hexadecimal integers are sign extended from the number of active bits, i.e., the bit width minus the number of leading zeros. So ‘`s0x0001`’ of type ‘`i16`’ will be -1, not 1.

****Byte constants****

Byte constants are used to initialize global variables of the byte type. These are strictly equivalent to integer constants: `store b8 42, ptr %p` is equivalent to `store i8 42, ptr %p`.

****Floating-point constants****

Floating-point constants use standard decimal notation (e.g. 123.421), exponential notation (e.g. 1.23421e+2), standard hexadecimal notation (e.g., 0x1.3effp-43), one of several special values, or a precise bitstring for the underlying value. When converting decimal and hexadecimal literals to the floating-point type, the value is converted using the default rounding mode (round to nearest, half to even). String conversions that underflow to 0 or overflow to infinity are not permitted. Floating-point constants must have a floating-point type.

****Null pointer constants****

The identifier ‘`null`’ is recognized as a null pointer constant and must be of pointer type.

****Token constants****

The identifier ‘`none`’ is recognized as an empty token constant and must be of token type.

Floating-point constants support the following kinds of strings:

> | Syntax | Description |
> |---|---|
> | `+4.5e-13` | Common decimal literal. Signs are optional, as is the exponent portion. The decimal point is required, as is one or more leading digits before the decimal point. |
> | `-0x1.fp13` | Common hexadecimal literal. Signs are optional. The decimal point is required, as is the exponent portion of the literal (after the `p`). |
> | `+inf`, `-inf` | Positive or negative infinity. The sign is required. |
> | `+qnan`, `-qnan` | Positive or negative preferred quiet NaN, i.e., the quiet bit is set, and all other payload bits are 0. The sign is required. |
> | `+nan(0x1)` | qNaN value with a particular payload, specified as hexadecimal (not including the quiet bit as part of the payload). The sign is required. |
> | `+snan(0x1)` | sNaN value with a particular payload, specified as hexadecimal (not including the quiet bit as part of the payload). The sign is required. |
> | `f0x3c00` | Value of the floating-point number if bitcast to an integer. The number must have exactly as many hexadecimal digits as is necessary for the size of the floating-point number. |

There is a legacy syntax for hexadecimal floating-point literals that will be removed in the future. In this format, constants are represented as their underlying integer representation as in the `f0x3c00` syntax, but instead use slightly different prefixes. `float` and `double` use `0x` followed by 16 hexadecimal digits representing the equivalent `double` value bitcast to an integer type. `bfloat` uses `0xR` followed by 4 hexadecimal digits. `half` uses `0xH` followed by 4 hexadecimal digits. `x86_fp80` uses `0xK` followed by 20 hexadecimal digits. `ppc_fp128` uses `0xM` followed by 32 hexadecimal digits. `fp128` uses `0xL` followed by 32 hexadecimal digits. For the last two types only, the bits are not fully written in big-endian order but rather with the low 64 bits written in big-endian then the high 64 bits written in big-endian.

There are no constants of type x86_amx.

Complex constants are a (potentially recursive) combination of simple constants and smaller complex constants.

****Structure constants****

Structure constants are represented with notation similar to structure type definitions (a comma separated list of elements, surrounded by braces (`{}`)). For example: “`{ i32 4, float 17.0, ptr @G }`”, where “`@G`” is declared as “`@G = external global i32`”. Structure constants must have structure type, and the number and types of elements must match those specified by the type.

****Array constants****

Array constants are represented with notation similar to array type definitions (a comma separated list of elements, surrounded by square brackets (`[]`)). For example: “`[ i32 42, i32 11, i32 74 ]`”. Array constants must have array type, and the number and types of elements must match those specified by the type. As a special case, character array constants may also be represented as a double-quoted string using the `c` prefix. For example: “`c"Hello World\0A\00"`”.

****Vector constants****

Vector constants are represented with notation similar to vector type definitions (a comma separated list of elements, surrounded by less-than/greater-than’s (`<>`)). For example: “`< i32 42, i32 11, i32 74, i32 100 >`”. Vector constants must have vector type, and the number and types of elements must match those specified by the type.

When creating a vector whose elements have the same constant value, the preferred syntax is `splat (<Ty> Val)`. For example: “`splat (i32 11)`”. These vector constants must have vector type with an element type that matches the `splat` operand.

****Zero initialization****

The string ‘`zeroinitializer`’ can be used to zero initialize a value to zero of *any* type, including scalar and aggregate types. This is often used to avoid having to print large zero initializers (e.g., for large arrays) and is always exactly equivalent to using explicit zero initializers.

****Metadata node****

A metadata node is a constant tuple without types. For example: “`!{!0, !{!2, !0}, !"test"}`”. Metadata can reference constant values, for example: “`!{!0, i32 0, ptr @global, ptr @function, !"str"}`”. Unlike other typed constants that are meant to be interpreted as part of the instruction stream, metadata is a place to attach additional information such as debug info.

The addresses of global variables and functions are always implicitly valid (link-time) constants. These constants are explicitly referenced when the identifier for the global is used and always have pointer type. For example, the following is a legal LLVM file:

```llvm
@X = global i32 17
@Y = global i32 42
@Z = global [2 x ptr] [ ptr @X, ptr @Y ]
```

The string ‘`undef`’ can be used anywhere a constant is expected, and indicates that the user of the value may receive an unspecified bit-pattern. Undefined values may be of any type (other than ‘`label`’ or ‘`void`’) and be used anywhere a constant is permitted.

Note

A ‘`poison`’ value (described in the next section) should be used instead of ‘`undef`’ whenever possible. Poison values are stronger than undef, and enable more optimizations. Just the existence of ‘`undef`’ blocks certain optimizations (see the examples below).

Undefined values are useful because they indicate to the compiler that the program is well defined no matter what value is used. This gives the compiler more freedom to optimize. Here are some examples of (potentially surprising) transformations that are valid (in pseudo IR):

```llvm
  %A = add %X, undef
  %B = sub %X, undef
  %C = xor %X, undef
Safe:
  %A = undef
  %B = undef
  %C = undef
```

This is safe because all of the output bits are affected by the undef bits. Any output bit can have a zero or one depending on the input bits.

```llvm
  %A = or %X, undef
  %B = and %X, undef
Safe:
  %A = -1
  %B = 0
Safe:
  %A = %X  ;; By choosing undef as 0
  %B = %X  ;; By choosing undef as -1
Unsafe:
  %A = undef
  %B = undef
```

These logical operations have bits that are not always affected by the input. For example, if `%X` has a zero bit, then the output of the ‘`and`’ operation will always be a zero for that bit, no matter what the corresponding bit from the ‘`undef`’ is. As such, it is unsafe to optimize or assume that the result of the ‘`and`’ is ‘`undef`’. However, it is safe to assume that all bits of the ‘`undef`’ could be 0, and optimize the ‘`and`’ to 0. Likewise, it is safe to assume that all the bits of the ‘`undef`’ operand to the ‘`or`’ could be set, allowing the ‘`or`’ to be folded to -1.

```llvm
  %A = select undef, %X, %Y
  %B = select undef, 42, %Y
  %C = select %X, %Y, undef
Safe:
  %A = %X     (or %Y)
  %B = 42     (or %Y)
  %C = %Y     (if %Y is provably not poison; unsafe otherwise)
Unsafe:
  %A = undef
  %B = undef
  %C = undef
```

This set of examples shows that undefined ‘`select`’ conditions can go *either way*, but they have to come from one of the two operands. In the `%A` example, if `%X` and `%Y` were both known to have a clear low bit, then `%A` would have to have a cleared low bit. However, in the `%C` example, the optimizer is allowed to assume that the ‘`undef`’ operand could be the same as `%Y` if `%Y` is provably not ‘`poison`’, allowing the whole ‘`select`’ to be eliminated. This is because ‘`poison`’ is stronger than ‘`undef`’.

```llvm
  %A = xor undef, undef

  %B = undef
  %C = xor %B, %B

  %D = undef
  %E = icmp slt %D, 4
  %F = icmp sge %D, 4

Safe:
  %A = undef
  %B = undef
  %C = undef
  %D = undef
  %E = undef
  %F = undef
```

This example points out that two ‘`undef`’ operands are not necessarily the same. This can be surprising to people (and also matches C semantics) where they assume that “`X^X`” is always zero, even if `X` is undefined. This isn’t true for a number of reasons, but the short answer is that an ‘`undef`’ “variable” can arbitrarily change its value over its “live range”. This is true because the variable doesn’t actually *have a live range*. Instead, the value is logically read from arbitrary registers that happen to be around when needed, so the value is not necessarily consistent over time. In fact, `%A` and `%C` need to have the same semantics or the core LLVM “replace all uses with” concept would not hold.

To ensure all uses of a given register observe the same value (even if ‘`undef`’), the freeze instruction can be used.

```llvm
  %A = sdiv undef, %X
  %B = sdiv %X, undef
Safe:
  %A = 0
b: unreachable
```

These examples show the crucial difference between an *undefined value* and *undefined behavior*. An undefined value (like ‘`undef`’) is allowed to have an arbitrary bit-pattern. This means that the `%A` operation can be constant folded to ‘`0`’, because the ‘`undef`’ could be zero, and zero divided by any value is zero. However, in the second example, we can make a more aggressive assumption: because the `undef` is allowed to be an arbitrary value, we are allowed to assume that it could be zero. Since a divide by zero has *undefined behavior*, we are allowed to assume that the operation does not execute at all. This allows us to delete the divide and all code after it. Because the undefined operation “can’t happen”, the optimizer can assume that it occurs in dead code.

```
a:  store undef -> %X
b:  store %X -> undef
Safe:
a: <deleted>     (if the stored value in %X is provably not poison)
b: unreachable
```

A store *of* an undefined value can be assumed to not have any effect; we can assume that the value is overwritten with bits that happen to match what was already there. This argument is only valid if the stored value is provably not `poison`. However, a store *to* an undefined location could clobber arbitrary memory, therefore, it has undefined behavior.

Branching on an undefined value is undefined behavior. This explains optimizations that depend on branch conditions to construct predicates, such as Correlated Value Propagation and Global Value Numbering. In case of switch instruction, the branch condition should be frozen, otherwise it is undefined behavior.

```llvm
Unsafe:
  br undef, BB1, BB2 ; UB

  %X = and i32 undef, 255
  switch %X, label %ret [ .. ] ; UB

  store undef, ptr %ptr
  %X = load ptr %ptr ; %X is undef
  switch i8 %X, label %ret [ .. ] ; UB

Safe:
  %X = or i8 undef, 255 ; always 255
  switch i8 %X, label %ret [ .. ] ; Well-defined

  %X = freeze i1 undef
  br %X, BB1, BB2 ; Well-defined (non-deterministic jump)
```

A poison value is a result of an erroneous operation. In order to facilitate speculative execution, many instructions do not invoke immediate undefined behavior when provided with illegal operands, and return a poison value instead. The string ‘`poison`’ can be used anywhere a constant is expected, and operations such as add with the `nsw` flag can produce a poison value.

Most instructions return ‘`poison`’ when one of their arguments is ‘`poison`’. A notable exception is the select instruction. Propagation of poison can be stopped with the freeze instruction.

It is correct to replace a poison value with an undef value or any value of the type.

This means that immediate undefined behavior occurs if a poison value is used as an instruction operand that has any values that trigger undefined behavior. Notably this includes (but is not limited to):

- The pointer operand of a load, store or any other pointer dereferencing instruction (independent of address space).
- The divisor operand of a `udiv`, `sdiv`, `urem` or `srem` instruction.
- The condition operand of a br instruction.
- The callee operand of a call or invoke instruction.
- The parameter operand of a call or invoke instruction, when the function or invoking call site has a `noundef` attribute in the corresponding position.
- The operand of a ret instruction if the function or invoking call site has a *noundef* attribute in the return value position.

Here are some examples:

```llvm
entry:
  %poison = sub nuw i32 0, 1           ; Results in a poison value.
  %poison2 = sub i32 poison, 1         ; Also results in a poison value.
  %still_poison = and i32 %poison, 0   ; 0, but also poison.
  %poison_yet_again = getelementptr i32, ptr @h, i32 %still_poison
  store i32 0, ptr %poison_yet_again   ; Undefined behavior due to
                                       ; store to poison.

  store i32 %poison, ptr @g            ; Poison value stored to memory.
  %poison3 = load i32, ptr @g          ; Poison value loaded back from memory.

  %poison4 = load i16, ptr @g          ; Returns a poison value.
  %poison5 = load i64, ptr @g          ; Returns a poison value.

  %cmp = icmp slt i32 %poison, 0       ; Returns a poison value.
  br i1 %cmp, label %end, label %end   ; undefined behavior

end:
```

Given a program execution, a value is *well defined* if the value does not have an undef bit and is not poison in the execution. An aggregate value or vector is well defined if its elements are well defined. The padding of an aggregate isn’t considered, since it isn’t visible without storing it into memory and loading it with a different type.

A constant of a single value, non-vector type is well defined if it is neither ‘`undef`’ constant nor ‘`poison`’ constant. The result of freeze instruction is well defined regardless of its operand.

`blockaddress(@function, %block)`

The ‘`blockaddress`’ constant computes the address of the specified basic block in the specified function.

It always has a `ptr addrspace(P)` type, where `P` is the address space of the function containing `%block` (usually `addrspace(0)`).

Taking the address of the entry block is illegal.

This value only has defined behavior when used as an operand to the ‘indirectbr’ or for comparisons against null. Pointer equality tests between label addresses results in undefined behavior — though, again, comparison against null is ok, and no label is equal to the null pointer. This may be passed around as an opaque pointer sized value as long as the bits are not inspected. This allows `ptrtoint` and arithmetic to be performed on these values so long as the original value is reconstituted before the `indirectbr` instruction.

Finally, some targets may provide defined semantics when using the value as the operand to an inline assembly, but that is target specific.

`dso_local_equivalent @func`

A ‘`dso_local_equivalent`’ constant represents a function which is functionally equivalent to a given function, but is always defined in the current linkage unit. The resulting pointer has the same type as the underlying function. The resulting pointer is permitted, but not required, to be different from a pointer to the function, and it may have different values in different translation units.

The target function may not have `extern_weak` linkage.

`dso_local_equivalent` can be implemented as such:

- If the function has local linkage, hidden visibility, or is `dso_local`, `dso_local_equivalent` can be implemented as simply a pointer to the function.
- `dso_local_equivalent` can be implemented with a stub that tail-calls the function. Many targets support relocations that resolve at link time to either a function or a stub for it, depending on whether the function is defined within the linkage unit; LLVM will use this when available. (This is commonly called a “PLT stub”.) On other targets, the stub may need to be emitted explicitly.

This can be used wherever a `dso_local` instance of a function is needed without needing to explicitly make the original function `dso_local`. An instance where this can be used is for static offset calculations between a function and some other `dso_local` symbol. This is especially useful for the Relative VTables C++ ABI, where dynamic relocations for function pointers in VTables can be replaced with static relocations for offsets between the VTable and virtual functions which may not be `dso_local`.

This is currently only supported for ELF binary formats.

`no_cfi @func`

With Control-Flow Integrity (CFI), a ‘`no_cfi`’ constant represents a function reference that does not get replaced with a reference to the CFI jump table in the `LowerTypeTests` pass. These constants may be useful in low-level programs, such as operating system kernels, which need to refer to the actual function body.

`ptrauth (ptr CST, i32 KEY[, i64 DISC[, ptr ADDRDISC[, ptr DS]?]?]?)`

A ‘`ptrauth`’ constant represents a pointer with a cryptographic authentication signature embedded into some bits, as described in the Pointer Authentication document.

A ‘`ptrauth`’ constant is simply a constant equivalent to the `llvm.ptrauth.sign` intrinsic, potentially fed by a discriminator `llvm.ptrauth.blend` if needed.

Its type is the same as the first argument. An integer constant discriminator and an address discriminator may be optionally specified. Otherwise, they have values `i64 0` and `ptr null`.

If the address discriminator is `null` then the expression is equivalent to

```llvm
%tmp = call i64 @llvm.ptrauth.sign(i64 ptrtoint (ptr CST to i64), i32 KEY, i64 DISC)
%val = inttoptr i64 %tmp to ptr
```

Otherwise, the expression is equivalent to:

```llvm
%tmp1 = call i64 @llvm.ptrauth.blend(i64 ptrtoint (ptr ADDRDISC to i64), i64 DISC)
%tmp2 = call i64 @llvm.ptrauth.sign(i64 ptrtoint (ptr CST to i64), i32 KEY, i64 %tmp1)
%val = inttoptr i64 %tmp2 to ptr
```

If the deactivation symbol operand `DS` has a non-null value, the semantics are as if a deactivation-symbol operand bundle were added to the `llvm.ptrauth.sign` intrinsic calls above, with `DS` as the only operand.

Constant expressions are used to allow expressions involving other constants to be used as constants. Constant expressions may be of any first class type and may involve any LLVM operation that does not have side effects (e.g., load and call are not supported). The following is the syntax for constant expressions:

**`trunc (CST to TYPE)`**

Perform the trunc operation on constants.

**`ptrtoint (CST to TYPE)`**

Perform the ptrtoint operation on constants.

**`ptrtoaddr (CST to TYPE)`**

Perform the ptrtoaddr operation on constants.

**`inttoptr (CST to TYPE)`**

Perform the inttoptr operation on constants. This one is *really* dangerous!

**`bitcast (CST to TYPE)`**

Convert a constant, CST, to another TYPE. The constraints of the operands are the same as those for the bitcast instruction.

**`addrspacecast (CST to TYPE)`**

Convert a constant pointer or constant vector of pointer, CST, to another TYPE in a different address space. The constraints of the operands are the same as those for the addrspacecast instruction.

**`getelementptr (TY, CSTPTR, IDX0, IDX1, ...)`, `getelementptr inbounds (TY, CSTPTR, IDX0, IDX1, ...)`**

Perform the getelementptr operation on constants. As with the getelementptr instruction, the index list may have one or more indexes, which are required to make sense for the type of “pointer to TY”. These indexes may be implicitly sign-extended or truncated to match the index size of CSTPTR’s address space.

**`extractelement (VAL, IDX)`**

Perform the extractelement operation on constants.

**`insertelement (VAL, ELT, IDX)`**

Perform the insertelement operation on constants.

**`shufflevector (VEC1, VEC2, IDXMASK)`**

Perform the shufflevector operation on constants.

**`add (LHS, RHS)`**

Perform an addition on constants.

**`sub (LHS, RHS)`**

Perform a subtraction on constants.

**`xor (LHS, RHS)`**

Perform a bitwise xor on constants.

LLVM supports inline assembler expressions (as opposed to Module-Level Inline Assembly) through the use of a special value. This value represents the inline assembler as a template string (containing the instructions to emit), a list of operand constraints (stored as a string), a flag that indicates whether or not the inline asm expression has side effects, and a flag indicating whether the function containing the asm needs to align its stack conservatively.

The compiler may not assume that the actual code executed at runtime matches the contents of the template string. Correctness-critical analyses must base their results only on the list of operand constraints and the flags – not the contents of the template string. This ensures correct behavior if the assembly code emitted by this expression is altered later, e.g. via self-modifying code, as long as the code keeps upholding the requirements of the operand constraints and the flags.

The template string supports argument substitution of the operands using “`$`” followed by a number, to indicate substitution of the given register/memory location, as specified by the constraint string. “`${NUM:MODIFIER}`” may also be used, where `MODIFIER` is a target-specific annotation for how to print the operand (See Asm template argument modifiers).

A literal “`$`” may be included by using “`$$`” in the template. To include other special characters into the output, the usual “`\XX`” escapes may be used, just as in other strings. Note that after template substitution, the resulting assembly string is parsed by LLVM’s integrated assembler unless it is disabled – even when emitting a `.s` file – and thus must contain assembly syntax known to LLVM.

LLVM also supports a few more substitutions useful for writing inline assembly:

- `${:uid}`: Expands to a decimal integer unique to this inline assembly blob. This substitution is useful when declaring a local label. Many standard compiler optimizations, such as inlining, may duplicate an inline asm blob. Adding a blob-unique identifier ensures that the two labels will not conflict during assembly. This is used to implement GCC’s %= special format string.
- `${:comment}`: Expands to the comment character of the current target’s assembly dialect. This is usually `#`, but many targets use other strings, such as `;`, `//`, or `!`.
- `${:private}`: Expands to the assembler private label prefix. Labels with this prefix will not appear in the symbol table of the assembled object. Typically the prefix is `L`, but targets may use other strings. `.L` is relatively popular.

LLVM’s support for inline asm is modeled closely on the requirements of Clang’s GCC-compatible inline-asm support. Thus, the feature-set and the constraint and modifier codes listed here are similar or identical to those in GCC’s inline asm support. However, to be clear, the syntax of the template and constraint strings described here is *not* the same as the syntax accepted by GCC and Clang, and, while most constraint letters are passed through as-is by Clang, some get translated to other codes when converting from the C source to the LLVM assembly.

An example inline assembler expression is:

```llvm
i32 (i32) asm "bswap $0", "=r,r"
```

Inline assembler expressions may **only** be used as the callee operand of a call or an invoke instruction. Thus, typically we have:

```llvm
%X = call i32 asm "bswap $0", "=r,r"(i32 %Y)
```

Inline asms with side effects not visible in the constraint list must be marked as having side effects. This is done through the use of the ‘`sideeffect`’ keyword, like so:

```llvm
call void asm sideeffect "eieio", ""()
```

In some cases inline asms will contain code that will not work unless the stack is aligned in some way, such as calls or SSE instructions on x86, yet will not contain code that does that alignment within the asm. The compiler should make conservative assumptions about what the asm might contain and should generate its usual stack alignment code in the prologue if the ‘`alignstack`’ keyword is present:

```llvm
call void asm alignstack "eieio", ""()
```

Inline asms also support using non-standard assembly dialects. The assumed dialect is ATT. When the ‘`inteldialect`’ keyword is present, the inline asm is using the Intel dialect. Currently, ATT and Intel are the only supported dialects. An example is:

```llvm
call void asm inteldialect "eieio", ""()
```

In the case that the inline asm might unwind the stack, the ‘`unwind`’ keyword must be used, so that the compiler emits unwinding information:

```llvm
call void asm unwind "call func", ""()
```

If the inline asm unwinds the stack and isn’t marked with the ‘`unwind`’ keyword, the behavior is undefined.

If multiple keywords appear, the ‘`sideeffect`’ keyword must come first, the ‘`alignstack`’ keyword second, the ‘`inteldialect`’ keyword third, and the ‘`unwind`’ keyword last.

The constraint list is a comma-separated string, each element containing one or more constraint codes.

For each element in the constraint list an appropriate register or memory operand will be chosen, and it will be made available to assembly template string expansion as `$0` for the first constraint in the list, `$1` for the second, etc.

There are three different types of constraints, which are distinguished by a prefix symbol in front of the constraint code: Output, Input, and Clobber. The constraints must always be given in that order: outputs first, then inputs, then clobbers. They cannot be intermingled.

There are also three different categories of constraint codes:

- Register constraint. This is either a register class, or a fixed physical register. This kind of constraint will allocate a register, and if necessary, bitcast the argument or result to the appropriate type.
- Memory constraint. This kind of constraint is for use with an instruction taking a memory operand. Different constraints allow for different addressing modes used by the target.
- Immediate value constraint. This kind of constraint is for an integer or other immediate value which can be rendered directly into an instruction. The various target-specific constraints allow the selection of a value in the proper range for the instruction you wish to use it with.

##### Output constraints

Output constraints are specified by an “`=`” prefix (e.g., “`=r`”). This indicates that the assembly will write to this operand, and the operand will then be made available as a return value of the `asm` expression. Output constraints do not consume an argument from the call instruction. (Except, see below about indirect outputs).

Normally, it is expected that no output locations are written to by the assembly expression until *all* of the inputs have been read. As such, LLVM may assign the same register to an output and an input. If this is not safe (e.g., if the assembly contains two instructions, where the first writes to one output, and the second reads an input and writes to a second output), then the “`&`” modifier must be used (e.g., “`=&r`”) to specify that the output is an “early-clobber” output. Marking an output as “early-clobber” ensures that LLVM will not use the same register for any inputs (other than an input tied to this output).

##### Input constraints

Input constraints do not have a prefix – just the constraint codes. Each input constraint will consume one argument from the call instruction. It is not permitted for the asm to write to any input register or memory location (unless that input is tied to an output). Note also that multiple inputs may all be assigned to the same register, if LLVM can determine that they necessarily all contain the same value.

Instead of providing a Constraint Code, input constraints may also “tie” themselves to an output constraint, by providing an integer as the constraint string. Tied inputs still consume an argument from the call instruction, and take up a position in the asm template numbering as is usual – they will simply be constrained to always use the same register as the output they’ve been tied to. For example, a constraint string of “`=r,0`” says to assign a register for output, and use that register as an input as well (it being the 0’th constraint).

It is permitted to tie an input to an “early-clobber” output. In that case, no *other* input may share the same register as the input tied to the early-clobber (even when the other input has the same value).

You may only tie an input to an output which has a register constraint, not a memory constraint. Only a single input may be tied to an output.

There is also an “interesting” feature which deserves a bit of explanation: if a register class constraint allocates a register which is too small for the value type operand provided as input, the input value will be split into multiple registers, and all of them passed to the inline asm.

However, this feature is often not as useful as you might think.

Firstly, the registers are *not* guaranteed to be consecutive. So, on those architectures that have instructions which operate on multiple consecutive instructions, this is not an appropriate way to support them. (e.g., the 32-bit SparcV8 has a 64-bit load, which instruction takes a single 32-bit register. The hardware then loads into both the named register, and the next register. This feature of inline asm would not be useful to support that.)

A few of the targets provide a template string modifier allowing explicit access to the second register of a two-register operand (e.g., MIPS `L`, `M`, and `D`). On such an architecture, you can actually access the second allocated register (yet, still, not any subsequent ones). But, in that case, you’re still probably better off simply splitting the value into two separate operands, for clarity. (e.g., see the description of the `A` constraint on X86, which, despite existing only for use with this feature, is not really a good idea to use)

##### Indirect inputs and outputs

Indirect output or input constraints can be specified by the “`*`” modifier (which goes after the “`=`” in case of an output). This indicates that the asm will write to or read from the contents of an *address* provided as an input argument. (Note that in this way, indirect outputs act more like an *input* than an output: just like an input, they consume an argument of the call expression, rather than producing a return value. An indirect output constraint is an “output” only in that the asm is expected to write to the contents of the input memory location, instead of just read from it).

This is most typically used for memory constraint, e.g., “`=*m`”, to pass the address of a variable as a value.

It is also possible to use an indirect *register* constraint, but only on output (e.g., “`=*r`”). This will cause LLVM to allocate a register for an output value normally, and then, separately emit a store to the address provided as input, after the provided inline asm. (It’s not clear what value this functionality provides, compared to writing the store explicitly after the asm statement, and it can only produce worse code, since it bypasses many optimization passes. I would recommend not using it.)

Call arguments for indirect constraints must have pointer type and must specify the elementtype attribute to indicate the pointer element type.

##### Clobber constraints

A clobber constraint is indicated by a “`~`” prefix. A clobber does not consume an input operand, nor generate an output. Clobbers cannot use any of the general constraint code letters – they may use only explicit register constraints, e.g., “`~{eax}`”.

The one exception is that a clobber string of “`~{memory}`” indicates that the assembly reads and writes to arbitrary undeclared memory locations – not only the memory pointed to by a declared indirect output. Furthermore, the assembly may also cause synchronization with other threads, such as via release/acquire fences and atomic memory accesses.

Note that clobbering named registers that are also present in output constraints is not legal.

##### Label constraints

A label constraint is indicated by a “`!`” prefix and typically used in the form `"!i"`. Instead of consuming call arguments, label constraints consume indirect destination labels of `callbr` instructions.
