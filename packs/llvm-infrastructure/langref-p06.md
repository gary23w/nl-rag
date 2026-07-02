---
title: "LLVM Language Reference Manual (part 6/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-infrastructure
license: CC-BY-SA-4.0
tags: llvm infrastructure, llvm compiler toolchain, optimizing compiler backend, clang frontend
fetched: 2026-07-02
part: 6/20
---

# LLVM Language Reference Manual

Label constraints can only be used in conjunction with `callbr` and the number of label constraints must match the number of indirect destination labels in the `callbr` instruction.

##### Constraint Codes

After a potential prefix comes constraint code, or codes.

A Constraint Code is either a single letter (e.g., “`r`”), a “`^`” character followed by two letters (e.g., “`^wc`”), or “`{`” register-name “`}`” (e.g., “`{eax}`”).

The one and two letter constraint codes are typically chosen to be the same as GCC’s constraint codes.

A single constraint may include one or more constraint codes in it, leaving it up to LLVM to choose which one to use. This is included mainly for compatibility with the translation of GCC inline asm coming from clang.

There are two ways to specify alternatives, and either or both may be used in an inline asm constraint list:

1. Append the codes to each other, making a constraint code set. E.g. “`im`” or “`{eax}m`”. This means “choose any of the options in the set”. The choice of constraint is made independently for each constraint in the constraint list.
2. Use “`|`” between constraint code sets, creating alternatives. Every constraint in the constraint list must have the same number of alternative sets. With this syntax, the same alternative in *all* of the items in the constraint list will be chosen together.

Putting those together, you might have a two operand constraint string like `"rm|r,ri|rm"`. This indicates that if operand 0 is `r` or `m`, then operand 1 may be one of `r` or `i`. If operand 0 is `r`, then operand 1 may be one of `r` or `m`. But, operand 0 and 1 cannot both be of type m.

However, the use of either of the alternatives features is *NOT* recommended, as LLVM is not able to make an intelligent choice about which one to use. (At the point it currently needs to choose, not enough information is available to do so in a smart way.) Thus, it simply tries to make a choice that’s most likely to compile, not one that will be optimal performance. (e.g., given “`rm`”, it’ll always choose to use memory, not registers). And, if given multiple registers, or multiple register classes, it will simply choose the first one. (In fact, it doesn’t currently even ensure explicitly specified physical registers are unique, so specifying multiple physical registers as alternatives, like `{r11}{r12},{r11}{r12}`, will assign r11 to both operands, not at all what was intended.)

##### Supported Constraint Code List

The constraint codes are, in general, expected to behave the same way they do in GCC. LLVM’s support is often implemented on an ‘as-needed’ basis, to support C inline asm code which was supported by GCC. A mismatch in behavior between LLVM and GCC likely indicates a bug in LLVM.

Some constraint codes are typically supported by all targets:

- `r`: A register in the target’s general purpose register class.
- `m`: A memory address operand. It is target-specific what addressing modes are supported, typical examples are register, or register + register offset, or register + immediate offset (of some target-specific size).
- `p`: An address operand. Similar to `m`, but used by “load address” type instructions without touching memory.
- `i`: An integer constant (of target-specific width). Allows either a simple immediate, or a relocatable value.
- `n`: An integer constant – *not* including relocatable values.
- `s`: A symbol or label reference with a constant offset.
- `X`: Allows an operand of any kind, no constraint whatsoever. Typically useful to pass a label for an asm branch or call.
- `{register-name}`: Requires exactly the named physical register.

Other constraints are target-specific:

AArch64:

- `z`: An immediate integer 0. Outputs `WZR` or `XZR`, as appropriate.
- `I`: An immediate integer valid for an `ADD` or `SUB` instruction, i.e., 0 to 4095 with optional shift by 12.
- `J`: An immediate integer that, when negated, is valid for an `ADD` or `SUB` instruction, i.e., -1 to -4095 with optional left shift by 12.
- `K`: An immediate integer that is valid for the ‘bitmask immediate 32’ of a logical instruction like `AND`, `EOR`, or `ORR` with a 32-bit register.
- `L`: An immediate integer that is valid for the ‘bitmask immediate 64’ of a logical instruction like `AND`, `EOR`, or `ORR` with a 64-bit register.
- `M`: An immediate integer for use with the `MOV` assembly alias on a 32-bit register. This is a superset of `K`: in addition to the bitmask immediate, also allows immediate integers which can be loaded with a single `MOVZ` or `MOVL` instruction.
- `N`: An immediate integer for use with the `MOV` assembly alias on a 64-bit register. This is a superset of `L`.
- `Q`: Memory address operand must be in a single register (no offsets). (However, LLVM currently does this for the `m` constraint as well.)
- `r`: A 32 or 64-bit integer register (W* or X*).
- `S`: A symbol or label reference with a constant offset. The generic `s` is not supported.
- `Uci`: Like r, but restricted to registers 8 to 11 inclusive.
- `Ucj`: Like r, but restricted to registers 12 to 15 inclusive.
- `w`: A 32, 64, or 128-bit floating-point, SIMD or SVE vector register.
- `x`: Like w, but restricted to registers 0 to 15 inclusive.
- `y`: Like w, but restricted to SVE vector registers Z0 to Z7 inclusive.
- `Uph`: One of the upper eight SVE predicate registers (P8 to P15)
- `Upl`: One of the lower eight SVE predicate registers (P0 to P7)
- `Upa`: Any of the SVE predicate registers (P0 to P15)

AMDGPU:

- `r`: A 32 or 64-bit integer register.
- `s`: SGPR register or tuple
- `v`: VGPR register or tuple
- `a`: AGPR register or tuple. Only valid on gfx908+.
- `VA`: VGPR or AGPR register or tuple. Only valid on gfx90a+.
- `v[0-9]`: The 32-bit VGPR register, number 0-9.
- `s[0-9]`: The 32-bit SGPR register, number 0-9.
- `a[0-9]`: The 32-bit AGPR register, number 0-9.
- `I`: An integer inline constant in the range from -16 to 64.
- `J`: A 16-bit signed integer constant.
- `A`: An integer or a floating-point inline constant.
- `B`: A 32-bit signed integer constant.
- `C`: A 32-bit unsigned integer constant or an integer inline constant in the range from -16 to 64.
- `DA`: A 64-bit constant that can be split into two “A” constants.
- `DB`: A 64-bit constant that can be split into two “B” constants.

All ARM modes:

- `Q`, `Um`, `Un`, `Uq`, `Us`, `Ut`, `Uv`, `Uy`: Memory address operand. Treated the same as operand `m`, at the moment.
- `Te`: An even general-purpose 32-bit integer register: `r0,r2,...,r12,r14`
- `To`: An odd general-purpose 32-bit integer register: `r1,r3,...,r11`

ARM and ARM’s Thumb2 mode:

- `j`: An immediate integer between 0 and 65535 (valid for `MOVW`)
- `I`: An immediate integer valid for a data-processing instruction.
- `J`: An immediate integer between -4095 and 4095.
- `K`: An immediate integer whose bitwise inverse is valid for a data-processing instruction. (Can be used with template modifier “`B`” to print the inverted value).
- `L`: An immediate integer whose negation is valid for a data-processing instruction. (Can be used with template modifier “`n`” to print the negated value).
- `M`: A power of two or an integer between 0 and 32.
- `N`: Invalid immediate constraint.
- `O`: Invalid immediate constraint.
- `r`: A general-purpose 32-bit integer register (`r0-r15`).
- `l`: In Thumb2 mode, low 32-bit GPR registers (`r0-r7`). In ARM mode, same as `r`.
- `h`: In Thumb2 mode, a high 32-bit GPR register (`r8-r15`). In ARM mode, invalid.
- `w`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s31`, `d0-d31`, or `q0-q15`, respectively.
- `t`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s31`, `d0-d15`, or `q0-q7`, respectively.
- `x`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s15`, `d0-d7`, or `q0-q3`, respectively.

ARM’s Thumb1 mode:

- `I`: An immediate integer between 0 and 255.
- `J`: An immediate integer between -255 and -1.
- `K`: An immediate integer between 0 and 255, with optional left-shift by some amount.
- `L`: An immediate integer between -7 and 7.
- `M`: An immediate integer which is a multiple of 4 between 0 and 1020.
- `N`: An immediate integer between 0 and 31.
- `O`: An immediate integer which is a multiple of 4 between -508 and 508.
- `r`: A low 32-bit GPR register (`r0-r7`).
- `l`: A low 32-bit GPR register (`r0-r7`).
- `h`: A high GPR register (`r0-r7`).
- `w`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s31`, `d0-d31`, or `q0-q15`, respectively.
- `t`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s31`, `d0-d15`, or `q0-q7`, respectively.
- `x`: A 32, 64, or 128-bit floating-point/SIMD register in the ranges `s0-s15`, `d0-d7`, or `q0-q3`, respectively.

Hexagon:

- `o`, `v`: A memory address operand, treated the same as constraint `m`, at the moment.
- `r`: A 32 or 64-bit register.

LoongArch:

- `f`: A floating-point register (if available).
- `k`: A memory operand whose address is formed by a base register and (optionally scaled) index register.
- `l`: A signed 16-bit constant.
- `m`: A memory operand whose address is formed by a base register and offset that is suitable for use in instructions with the same addressing mode as st.w and ld.w.
- `q`: A general-purpose register except for $r0 and $r1 (for the csrxchg instruction).
- `I`: A signed 12-bit constant (for arithmetic instructions).
- `J`: An immediate integer zero.
- `K`: An unsigned 12-bit constant (for logic instructions).
- `ZB`: An address that is held in a general-purpose register. The offset is zero.
- `ZC`: A memory operand whose address is formed by a base register and offset that is suitable for use in instructions with the same addressing mode as ll.w and sc.w.

MSP430:

- `r`: An 8 or 16-bit register.

MIPS:

- `I`: An immediate signed 16-bit integer.
- `J`: An immediate integer zero.
- `K`: An immediate unsigned 16-bit integer.
- `L`: An immediate 32-bit integer, where the lower 16 bits are 0.
- `N`: An immediate integer between -65535 and -1.
- `O`: An immediate signed 15-bit integer.
- `P`: An immediate integer between 1 and 65535.
- `m`: A memory address operand. In MIPS-SE mode, allows a base address register plus 16-bit immediate offset. In MIPS mode, just a base register.
- `R`: A memory address operand. In MIPS-SE mode, allows a base address register plus a 9-bit signed offset. In MIPS mode, the same as constraint `m`.
- `ZC`: A memory address operand, suitable for use in a `pref`, `ll`, or `sc` instruction on the given subtarget (details vary).
- `r`, `d`, `y`: A 32 or 64-bit GPR register.
- `f`: A 32 or 64-bit FPU register (`F0-F31`), or a 128-bit MSA register (`W0-W31`). In the case of MSA registers, it is recommended to use the `w` argument modifier for compatibility with GCC.
- `c`: A 32-bit or 64-bit GPR register suitable for indirect jump (always `25`).
- `l`: The `lo` register, 32 or 64-bit.
- `x`: Invalid.

NVPTX:

- `b`: A 1-bit integer register.
- `c` or `h`: A 16-bit integer register.
- `r`: A 32-bit integer register.
- `l` or `N`: A 64-bit integer register.
- `q`: A 128-bit integer register.
- `f`: A 32-bit float register.
- `d`: A 64-bit float register.

PowerPC:

- `I`: An immediate signed 16-bit integer.
- `J`: An immediate unsigned 16-bit integer, shifted left 16 bits.
- `K`: An immediate unsigned 16-bit integer.
- `L`: An immediate signed 16-bit integer, shifted left 16 bits.
- `M`: An immediate integer greater than 31.
- `N`: An immediate integer that is an exact power of 2.
- `O`: The immediate integer constant 0.
- `P`: An immediate integer constant whose negation is a signed 16-bit constant.
- `es`, `o`, `Q`, `Z`, `Zy`: A memory address operand, currently treated the same as `m`.
- `r`: A 32 or 64-bit integer register.
- `b`: A 32 or 64-bit integer register, excluding `R0` (that is: `R1-R31`).
- `f`: A 32 or 64-bit float register (`F0-F31`),
- `v`: For `4 x f32` or `4 x f64` types, a 128-bit altivec vectorregister (`V0-V31`).
- `y`: Condition register (`CR0-CR7`).
- `wc`: An individual CR bit in a CR register.
- `wa`, `wd`, `wf`: Any 128-bit VSX vector register, from the full VSX register set (overlapping both the floating-point and vector register files).
- `ws`: A 32 or 64-bit floating-point register, from the full VSX register set.

RISC-V:

- `A`: An address operand (using a general-purpose register, without an offset).
- `I`: A 12-bit signed integer immediate operand.
- `J`: A zero integer immediate operand.
- `K`: A 5-bit unsigned integer immediate operand.
- `f`: A 32- or 64-bit floating-point register (requires F or D extension).
- `r`: A 32- or 64-bit general-purpose register (depending on the platform `XLEN`).
- `S`: Alias for `s`.
- `vd`: A vector register, excluding `v0` (requires V extension).
- `vm`: The vector register `v0` (requires V extension).
- `vr`: A vector register (requires V extension).

Sparc:

- `I`: An immediate 13-bit signed integer.
- `r`: A 32-bit integer register.
- `f`: Any floating-point register on SparcV8, or a floating-point register in the “low” half of the registers on SparcV9.
- `e`: Any floating-point register. (Same as `f` on SparcV8.)

SystemZ:

- `I`: An immediate unsigned 8-bit integer.
- `J`: An immediate unsigned 12-bit integer.
- `K`: An immediate signed 16-bit integer.
- `L`: An immediate signed 20-bit integer.
- `M`: An immediate integer 0x7fffffff.
- `Q`: A memory address operand with a base address and a 12-bit immediate unsigned displacement.
- `R`: A memory address operand with a base address, a 12-bit immediate unsigned displacement, and an index register.
- `S`: A memory address operand with a base address and a 20-bit immediate signed displacement.
- `T`: A memory address operand with a base address, a 20-bit immediate signed displacement, and an index register.
- `r` or `d`: A 32, 64, or 128-bit integer register.
- `a`: A 32, 64, or 128-bit integer address register (excludes R0, which in an address context evaluates as zero).
- `h`: A 32-bit value in the high part of a 64bit data register (LLVM-specific)
- `f`: A 16, 32, 64, or 128-bit floating-point register.

X86:

- `I`: An immediate integer between 0 and 31.
- `J`: An immediate integer between 0 and 64.
- `K`: An immediate signed 8-bit integer.
- `L`: An immediate integer, 0xff or 0xffff or (in 64-bit mode only) 0xffffffff.
- `M`: An immediate integer between 0 and 3.
- `N`: An immediate unsigned 8-bit integer.
- `O`: An immediate integer between 0 and 127.
- `e`: An immediate 32-bit signed integer.
- `Z`: An immediate 32-bit unsigned integer.
- `q`: An 8, 16, 32, or 64-bit register which can be accessed as an 8-bit `l` integer register. On X86-32, this is the `a`, `b`, `c`, and `d` registers, and on X86-64, it is all of the integer registers. When feature *egpr* and *inline-asm-use-gpr32* are both on, it will be extended to gpr32.
- `Q`: An 8, 16, 32, or 64-bit register which can be accessed as an 8-bit `h` integer register. This is the `a`, `b`, `c`, and `d` registers.
- `r` or `l`: An 8, 16, 32, or 64-bit integer register. When feature *egpr* and *inline-asm-use-gpr32* are both on, it will be extended to gpr32.
- `R`: An 8, 16, 32, or 64-bit “legacy” integer register – one which has existed since i386, and can be accessed without the REX prefix.
- `f`: A 32, 64, or 80-bit ‘387 FPU stack pseudo-register.
- `y`: A 64-bit MMX register, if MMX is enabled.
- `v`: If SSE is enabled: a 32 or 64-bit scalar operand, or 128-bit vector operand in a SSE register. If AVX is also enabled, can also be a 256-bit vector operand in an AVX register. If AVX-512 is also enabled, can also be a 512-bit vector operand in an AVX512 register. Otherwise, an error.
- `Ws`: A symbolic reference with an optional constant addend or a label reference.
- `x`: The same as `v`, except that when AVX-512 is enabled, the `x` code only allocates into the first 16 AVX-512 registers, while the `v` code allocates into any of the 32 AVX-512 registers.
- `Y`: The same as `x`, if *SSE2* is enabled, otherwise an error.
- `A`: Special case: allocates EAX first, then EDX, for a single operand (in 32-bit mode, a 64-bit integer operand will get split into two registers). It is not recommended to use this constraint, as in 64-bit mode, the 64-bit operand will get allocated only to RAX – if two 32-bit operands are needed, you’re better off splitting it yourself, before passing it to the asm statement.
- `jr`: An 8, 16, 32, or 64-bit integer gpr16. It won’t be extended to gpr32 when feature *egpr* or *inline-asm-use-gpr32* is on.
- `jR`: An 8, 16, 32, or 64-bit integer gpr32 when feature *egpr`* is on. Otherwise, same as `r`.

XCore:

- `r`: A 32-bit integer register.

In the asm template string, modifiers can be used on the operand reference, like “`${0:n}`”.

The modifiers are, in general, expected to behave the same way they do in GCC. LLVM’s support is often implemented on an ‘as-needed’ basis, to support C inline asm code which was supported by GCC. A mismatch in behavior between LLVM and GCC likely indicates a bug in LLVM.

Target-independent:

- `a`: Print a memory reference. Targets might customize the output.
- `c`: Print an immediate integer constant unadorned, without the target-specific immediate punctuation (e.g., no `$` prefix).
- `n`: Negate and print immediate integer constant unadorned, without the target-specific immediate punctuation (e.g., no `$` prefix).
- `l`: Print as an unadorned label, without the target-specific label punctuation (e.g., no `$` prefix).

AArch64:

- `w`: Print a GPR register with a `w*` name instead of `x*` name. E.g., instead of `x30`, print `w30`.
- `x`: Print a GPR register with a `x*` name. (this is the default, anyhow).
- `b`, `h`, `s`, `d`, `q`: Print a floating-point/SIMD register with a `b*`, `h*`, `s*`, `d*`, or `q*` name, rather than the default of `v*`.

AMDGPU:

- `r`: No effect.

ARM:

- `a`: Print an operand as an address (with `[` and `]` surrounding a register).
- `P`: No effect.
- `q`: No effect.
- `y`: Print a VFP single-precision register as an indexed double (e.g., print as `d4[1]` instead of `s9`)
- `B`: Bitwise invert and print an immediate integer constant without `#` prefix.
- `L`: Print the low 16-bits of an immediate integer constant.
- `M`: Print as a register set suitable for ldm/stm. Also prints *all* register operands subsequent to the specified one (!), so use carefully.
- `Q`: Print the low-order register of a register-pair, or the low-order register of a two-register operand.
- `R`: Print the high-order register of a register-pair, or the high-order register of a two-register operand.
- `H`: Print the second register of a register-pair. (On a big-endian system, `H` is equivalent to `Q`, and on little-endian system, `H` is equivalent to `R`.)
- `e`: Print the low doubleword register of a NEON quad register.
- `f`: Print the high doubleword register of a NEON quad register.
- `m`: Print the base register of a memory operand without the `[` and `]` adornment.

Hexagon:

- `L`: Print the second register of a two-register operand. Requires that it has been allocated consecutively to the first.
- `I`: Print the letter ‘i’ if the operand is an integer constant, otherwise nothing. Used to print ‘addi’ vs ‘add’ instructions.

LoongArch:

- `u`: Print an LASX register.
- `w`: Print an LSX register.
- `z`: Print $zero register if operand is zero, otherwise print it normally.

MSP430:

No additional modifiers.

MIPS:

- `X`: Print an immediate integer as hexadecimal
- `x`: Print the low 16 bits of an immediate integer as hexadecimal.
- `d`: Print an immediate integer as decimal.
- `m`: Subtract one and print an immediate integer as decimal.
- `z`: Print $0 if an immediate zero, otherwise print normally.
- `L`: Print the low-order register of a two-register operand, or prints the address of the low-order word of a double-word memory operand.
- `M`: Print the high-order register of a two-register operand, or prints the address of the high-order word of a double-word memory operand.
- `D`: Print the second register of a two-register operand, or prints the second word of a double-word memory operand. (On a big-endian system, `D` is equivalent to `L`, and on little-endian system, `D` is equivalent to `M`.)
- `w`: No effect. Provided for compatibility with GCC which requires this modifier in order to print MSA registers (`W0-W31`) with the `f` constraint.

NVPTX:

- `r`: No effect.

PowerPC:

- `L`: Print the second register of a two-register operand. Requires that it has been allocated consecutively to the first.
- `I`: Print the letter ‘i’ if the operand is an integer constant, otherwise nothing. Used to print ‘addi’ vs ‘add’ instructions.
- `y`: For a memory operand, prints formatter for a two-register X-form instruction. (Currently always prints `r0,OPERAND`).
- `U`: Prints ‘u’ if the memory operand is an update form, and nothing otherwise. (NOTE: LLVM does not support update form, so this will currently always print nothing)
- `X`: Prints ‘x’ if the memory operand is an indexed form. (NOTE: LLVM does not support indexed form, so this will currently always print nothing)

RISC-V:

- `i`: Print the letter ‘i’ if the operand is not a register, otherwise print nothing. Used to print ‘addi’ vs ‘add’ instructions, etc.
- `z`: Print the register `zero` if an immediate zero, otherwise print normally.

Sparc:

- `L`: Print the low-order register of a two-register operand.
- `H`: Print the high-order register of a two-register operand.
- `r`: No effect.

SystemZ:

SystemZ implements only `n`, and does *not* support any of the other target-independent modifiers.

X86:

- `a`: Print a memory reference. This displays as `sym(%rip)` for x86-64. i386 should only use this with the static relocation model.
- `c`: Print an unadorned integer or symbol name. (The latter is target-specific behavior for this typically target-independent modifier).
- `A`: Print a register name with a ‘`*`’ before it.
- `b`: Print an 8-bit register name (e.g., `al`); do nothing on a memory operand.
- `h`: Print the upper 8-bit register name (e.g., `ah`); do nothing on a memory operand.
- `w`: Print the 16-bit register name (e.g., `ax`); do nothing on a memory operand.
- `k`: Print the 32-bit register name (e.g., `eax`); do nothing on a memory operand.
- `q`: Print the 64-bit register name (e.g., `rax`), if 64-bit registers are available, otherwise the 32-bit register name; do nothing on a memory operand.
- `n`: Negate and print an unadorned integer, or, for operands other than an immediate integer (e.g., a relocatable symbol expression), print a ‘-’ before the operand. (The behavior for relocatable symbol expressions is a target-specific behavior for this typically target-independent modifier)
- `H`: Print a memory reference with additional offset +8.
- `p`: Print a raw symbol name (without syntax-specific prefixes).
- `P`: Print a memory reference used as the argument of a call instruction or used with explicit base reg and index reg as its offset. So it can not use additional regs to present the memory reference. (E.g. omit `(rip)`, even though it’s PC-relative.)

XCore:

No additional modifiers.

Compiling with ThinLTO causes the building of a compact summary of the module that is emitted into the bitcode. The summary is emitted into the LLVM assembly and identified in syntax by a caret (’`^`’).

The summary is parsed into a bitcode output, along with the Module IR, via the “`llvm-as`” tool. Tools that parse the Module IR for the purposes of optimization (e.g., “`clang -x ir`” and “`opt`”), will ignore the summary entries (just as they currently ignore summary entries in a bitcode input file).

Eventually, the summary will be parsed into a ModuleSummaryIndex object under the same conditions where summary index is currently built from bitcode. Specifically, tools that test the Thin Link portion of a ThinLTO compile (i.e., llvm-lto and llvm-lto2), or when parsing a combined index for a distributed ThinLTO backend via clang’s “`-fthinlto-index=<>`” flag (this part is not yet implemented, use llvm-as to create a bitcode object before feeding into thin link tools for now).

There are currently 3 types of summary entries in the LLVM assembly: module paths, global values, and type identifiers.

Each module path summary entry lists a module containing global values included in the summary. For a single IR module there will be one such entry, but in a combined summary index produced during the thin link, there will be one module path entry per linked module with summary.

Example:

```
^0 = module: (path: "/path/to/file.o", hash: (2468601609, 1329373163, 1565878005, 638838075, 3148790418))
```

The `path` field is a string path to the bitcode file, and the `hash` field is the 160-bit SHA-1 hash of the IR bitcode contents, used for incremental builds and caching.

Each global value summary entry corresponds to a global value defined or referenced by a summarized module.

Example:

```
^4 = gv: (name: "f"[, summaries: (Summary)[, (Summary)]*]?) ; guid = 14740650423002898831
```

For declarations, there will not be a summary list. For definitions, a global value will contain a list of summaries, one per module containing a definition. There can be multiple entries in a combined summary index for symbols with weak linkage.

Each `Summary` format will depend on whether the global value is a function, variable, or alias.

If the global value is a function, the `Summary` entry will look like:

```
function: (module: ^0, flags: (linkage: external, notEligibleToImport: 0, live: 0, dsoLocal: 0), insts: 2[, FuncFlags]?[, Calls]?[, TypeIdInfo]?[, Params]?[, Refs]?
```

The `module` field includes the summary entry id for the module containing this definition, and the `flags` field contains information such as the linkage type, a flag indicating whether it is legal to import the definition, whether it is globally live and whether the linker resolved it to a local definition (the latter two are populated during the thin link). The `insts` field contains the number of IR instructions in the function. Finally, there are several optional fields: FuncFlags, Calls, TypeIdInfo, Params, Refs.

If the global value is a variable, the `Summary` entry will look like:

```
variable: (module: ^0, flags: (linkage: external, notEligibleToImport: 0, live: 0, dsoLocal: 0)[, Refs]?
```

The variable entry contains a subset of the fields in a function summary, see the descriptions there.

If the global value is an alias, the `Summary` entry will look like:

```
alias: (module: ^0, flags: (linkage: external, notEligibleToImport: 0, live: 0, dsoLocal: 0), aliasee: ^2)
```

The `module` and `flags` fields are as described for a function summary. The `aliasee` field contains a reference to the global value summary entry of the aliasee.

The optional `FuncFlags` field looks like:

```
funcFlags: (readNone: 0, readOnly: 0, noRecurse: 0, returnDoesNotAlias: 0, noInline: 0, alwaysInline: 0, noUnwind: 1, mayThrow: 0, hasUnknownCall: 0)
```

If unspecified, flags are assumed to hold the conservative `false` value of `0`.

The optional `Calls` field looks like:

```
calls: ((Callee)[, (Callee)]*)
```

where each `Callee` looks like:

```
callee: ^1[, hotness: None]?[, relbf: 0]?
```

The `callee` refers to the summary entry id of the callee. At most one of `hotness` (which can take the values `Unknown`, `Cold`, `None`, `Hot`, and `Critical`), and `relbf` (which holds the integer branch frequency relative to the entry frequency, scaled down by 2^8) may be specified. The defaults are `Unknown` and `0`, respectively.

The optional `Params` is used by `StackSafety` and looks like:

```
Params: ((Param)[, (Param)]*)
```

where each `Param` describes pointer parameter access inside of the function and looks like:

```
param: 4, offset: [0, 5][, calls: ((Callee)[, (Callee)]*)]?
```

where the first `param` is the number of the parameter it describes, `offset` is the inclusive range of offsets from the pointer parameter to bytes which can be accessed by the function. This range does not include accesses by function calls from `calls` list.

where each `Callee` describes how parameter is forwarded into other functions and looks like:

```
callee: ^3, param: 5, offset: [-3, 3]
```

The `callee` refers to the summary entry id of the callee, `param` is the number of the callee parameter which points into the callers parameter with offset known to be inside of the `offset` range. `calls` will be consumed and removed by thin link stage to update `Param::offset` so it covers all accesses possible by `calls`.

Pointer parameter without corresponding `Param` is considered unsafe and we assume that access with any offset is possible.

Example:

If we have the following function:

```
define i64 @foo(ptr %0, ptr %1, ptr %2, i8 %3) {
  store ptr %1, ptr @x
  %5 = getelementptr inbounds i8, ptr %2, i64 5
  %6 = load i8, ptr %5
  %7 = getelementptr inbounds i8, ptr %2, i8 %3
  tail call void @bar(i8 %3, ptr %7)
  %8 = load i64, ptr %0
  ret i64 %8
}
```

We can expect the record like this:

```
params: ((param: 0, offset: [0, 7]),(param: 2, offset: [5, 5], calls: ((callee: ^3, param: 1, offset: [-128, 127]))))
```

The function may access just 8 bytes of the parameter %0 . `calls` is empty, so the parameter is either not used for function calls or `offset` already covers all accesses from nested function calls. Parameter %1 escapes, so access is unknown. The function itself can access just a single byte of the parameter %2. Additional access is possible inside of the `@bar` or `^3`. The function adds signed offset to the pointer and passes the result as the argument %1 into `^3`. This record itself does not tell us how `^3` will access the parameter. Parameter %3 is not a pointer.

The optional `Refs` field looks like:

```
refs: ((Ref)[, (Ref)]*)
```

where each `Ref` contains a reference to the summary id of the referenced value (e.g., `^1`).

The optional `TypeIdInfo` field, used for Control Flow Integrity, looks like:

```
typeIdInfo: [(TypeTests)]?[, (TypeTestAssumeVCalls)]?[, (TypeCheckedLoadVCalls)]?[, (TypeTestAssumeConstVCalls)]?[, (TypeCheckedLoadConstVCalls)]?
```

These optional fields have the following forms:

##### TypeTests

```
typeTests: (TypeIdRef[, TypeIdRef]*)
```

Where each `TypeIdRef` refers to a type id by summary id or `GUID`.

##### TypeTestAssumeVCalls

```
typeTestAssumeVCalls: (VFuncId[, VFuncId]*)
```

Where each VFuncId has the format:

```
vFuncId: (TypeIdRef, offset: 16)
```

Where each `TypeIdRef` refers to a type id by summary id or `GUID` preceded by a `guid:` tag.

##### TypeCheckedLoadVCalls

```
typeCheckedLoadVCalls: (VFuncId[, VFuncId]*)
```

Where each VFuncId has the format described for `TypeTestAssumeVCalls`.

##### TypeTestAssumeConstVCalls

```
typeTestAssumeConstVCalls: (ConstVCall[, ConstVCall]*)
```

Where each ConstVCall has the format:

```
(VFuncId, args: (Arg[, Arg]*))
```

and where each VFuncId has the format described for `TypeTestAssumeVCalls`, and each Arg is an integer argument number.

##### TypeCheckedLoadConstVCalls

```
typeCheckedLoadConstVCalls: (ConstVCall[, ConstVCall]*)
```

Where each ConstVCall has the format described for `TypeTestAssumeConstVCalls`.

Each type id summary entry corresponds to a type identifier resolution which is generated during the LTO link portion of the compile when building with Control Flow Integrity, so these are only present in a combined summary index.

Example:

```
^4 = typeid: (name: "_ZTS1A", summary: (typeTestRes: (kind: allOnes, sizeM1BitWidth: 7[, alignLog2: 0]?[, sizeM1: 0]?[, bitMask: 0]?[, inlineBits: 0]?)[, WpdResolutions]?)) ; guid = 7004155349499253778
```

The `typeTestRes` gives the type test resolution `kind` (which may be `unsat`, `byteArray`, `inline`, `single`, or `allOnes`), and the `size-1` bit width. It is followed by optional flags, which default to 0, and an optional WpdResolutions (whole program devirtualization resolution) field that looks like:

```
wpdResolutions: ((offset: 0, WpdRes)[, (offset: 1, WpdRes)]*
```

where each entry is a mapping from the given byte offset to the whole-program devirtualization resolution WpdRes, that has one of the following formats:

```
wpdRes: (kind: branchFunnel)
wpdRes: (kind: singleImpl, singleImplName: "_ZN1A1nEi")
wpdRes: (kind: indir)
```

Additionally, each wpdRes has an optional `resByArg` field, which describes the resolutions for calls with all constant integer arguments:

```
resByArg: (ResByArg[, ResByArg]*)
```

where ResByArg is:

```
args: (Arg[, Arg]*), byArg: (kind: UniformRetVal[, info: 0][, byte: 0][, bit: 0])
```

Where the `kind` can be `Indir`, `UniformRetVal`, `UniqueRetVal` or `VirtualConstProp`. The `info` field is only used if the kind is `UniformRetVal` (indicates the uniform return value), or `UniqueRetVal` (holds the return value associated with the unique vtable (0 or 1)). The `byte` and `bit` fields are only used if the target does not support the use of absolute symbols to store constants.

LLVM has a number of “magic” global variables that contain data that affect code generation or other IR semantics. These are documented here. All globals of this sort should have a section specified as “`llvm.metadata`”. This section and all globals that start with “`llvm.`” are reserved for use by LLVM.

The `@llvm.used` global is an array which has appending linkage. This array contains a list of pointers to named global variables, functions and aliases which may optionally have a pointer cast formed of bitcast or getelementptr. For example, a legal use of it is:

```llvm
@X = global i8 4
@Y = global i32 123

@llvm.used = appending global [2 x ptr] [
   ptr @X,
   ptr @Y
], section "llvm.metadata"
```

If a symbol appears in the `@llvm.used` list, then the compiler, assembler, and linker are required to treat the symbol as if there is a reference to the symbol that it cannot see (which is why they have to be named). For example, if a variable has internal linkage and no references other than that from the `@llvm.used` list, it cannot be deleted. This is commonly used to represent references from inline asms and other things the compiler cannot “see”, and corresponds to “`attribute((used))`” in GNU C.

On some targets, the code generator must emit a directive to the assembler or object file to prevent the assembler and linker from removing the symbol.

The `@llvm.compiler.used` directive is the same as the `@llvm.used` directive, except that it only prevents the compiler from touching the symbol. On targets that support it, this allows an intelligent linker to optimize references to the symbol without being impeded as it would be by `@llvm.used`.

This is a rare construct that should only be used in rare circumstances, and should not be exposed to source languages.

```llvm
%0 = type { i32, ptr, ptr }
@llvm.global_ctors = appending global [1 x %0] [%0 { i32 65535, ptr @ctor, ptr @data }]
```

The `@llvm.global_ctors` array contains a list of constructor functions, priorities, and an associated global or function. The functions referenced by this array will be called in ascending order of priority (i.e., lowest first) when the module is loaded. The order of functions with the same priority is not defined.

If the third field is non-null, and points to a global variable or function, the initializer function will only run if the associated data from the current module is not discarded. On ELF the referenced global variable or function must be in a comdat.

```llvm
%0 = type { i32, ptr, ptr }
@llvm.global_dtors = appending global [1 x %0] [%0 { i32 65535, ptr @dtor, ptr @data }]
```

The `@llvm.global_dtors` array contains a list of destructor functions, priorities, and an associated global or function. The functions referenced by this array will be called in descending order of priority (i.e., highest first) when the module is unloaded. The order of functions with the same priority is not defined.

If the third field is non-null, and points to a global variable or function, the destructor function will only run if the associated data from the current module is not discarded. On ELF the referenced global variable or function must be in a comdat.

The LLVM instruction set consists of several different classifications of instructions: terminator instructions, binary instructions, bitwise binary instructions, memory instructions, and other instructions. There are also debug records, which are not instructions themselves but are printed interleaved with instructions to describe changes in the state of the program’s debug information at each position in the program’s execution.

As mentioned previously, every basic block in a program ends with a “Terminator” instruction, which indicates which block should be executed after the current block is finished. These terminator instructions typically yield a ‘`void`’ value: they produce control flow, not values (the one exception being the ‘invoke’ instruction).

The terminator instructions are: ‘ret’, ‘br’, ‘switch’, ‘indirectbr’, ‘invoke’, ‘callbr’ ‘resume’, ‘catchswitch’, ‘catchret’, ‘cleanupret’, and ‘unreachable’.

##### Syntax:

```
ret <type> <value>       ; Return a value from a non-void function
ret void                 ; Return from void function
```

##### Overview:

The ‘`ret`’ instruction is used to return control flow (and optionally a value) from a function back to the caller.

There are two forms of the ‘`ret`’ instruction: one that returns a value and then causes control flow, and one that just causes control flow to occur.

##### Arguments:

The ‘`ret`’ instruction optionally accepts a single argument, the return value. The type of the return value must be a ‘first class’ type.

A function is not well formed if it has a non-void return type and contains a ‘`ret`’ instruction with no return value or a return value with a type that does not match its type, or if it has a void return type and contains a ‘`ret`’ instruction with a return value.

##### Semantics:

When the ‘`ret`’ instruction is executed, control flow returns back to the calling function’s context. If the caller is a “call” instruction, execution continues at the instruction after the call. If the caller was an “invoke” instruction, execution continues at the beginning of the “normal” destination block. If the instruction returns a value, that value shall set the call or invoke instruction’s return value.

##### Example:

```llvm
ret i32 5                       ; Return an integer value of 5
ret void                        ; Return from a void function
ret { i32, i8 } { i32 4, i8 2 } ; Return a struct of values 4 and 2
```

##### Syntax:

```
br i1 <cond>, label <iftrue>, label <iffalse>
br label <dest>          ; Unconditional branch
```

##### Overview:

The ‘`br`’ instruction is used to cause control flow to transfer to a different basic block in the current function. There are two forms of this instruction, corresponding to a conditional branch and an unconditional branch.

##### Arguments:

The conditional branch form of the ‘`br`’ instruction takes a single ‘`i1`’ value and two ‘`label`’ values. The unconditional form of the ‘`br`’ instruction takes a single ‘`label`’ value as a target.

##### Semantics:

Upon execution of a conditional ‘`br`’ instruction, the ‘`i1`’ argument is evaluated. If the value is `true`, control flows to the ‘`iftrue`’ `label` argument. If “cond” is `false`, control flows to the ‘`iffalse`’ `label` argument. If ‘`cond`’ is `poison` or `undef`, this instruction has undefined behavior.

##### Example:

```llvm
Test:
  %cond = icmp eq i32 %a, %b
  br i1 %cond, label %IfEqual, label %IfUnequal
IfEqual:
  ret i32 1
IfUnequal:
  ret i32 0
```

##### Syntax:

```
switch <intty> <value>, label <defaultdest> [ <intty> <val>, label <dest> ... ]
```

##### Overview:

The ‘`switch`’ instruction is used to transfer control flow to one of several different places. It is a generalization of the ‘`br`’ instruction, allowing a branch to occur to one of many possible destinations.

##### Arguments:

The ‘`switch`’ instruction uses three parameters: an integer comparison value ‘`value`’, a default ‘`label`’ destination, and an array of pairs of comparison value constants and ‘`label`’s. The table is not allowed to contain duplicate constant entries.

##### Semantics:

The `switch` instruction specifies a table of values and destinations. When the ‘`switch`’ instruction is executed, this table is searched for the given value. If the value is found, control flow is transferred to the corresponding destination; otherwise, control flow is transferred to the default destination. If ‘`value`’ is `poison` or `undef`, this instruction has undefined behavior.

##### Implementation:

Depending on properties of the target machine and the particular `switch` instruction, this instruction may be code generated in different ways. For example, it could be generated as a series of chained conditional branches or with a lookup table.

##### Example:

```llvm
; Emulate a conditional br instruction
%Val = zext i1 %value to i32
switch i32 %Val, label %truedest [ i32 0, label %falsedest ]

; Emulate an unconditional br instruction
switch i32 0, label %dest [ ]

; Implement a jump table:
switch i32 %val, label %otherwise [ i32 0, label %onzero
                                    i32 1, label %onone
                                    i32 2, label %ontwo ]
```

##### Syntax:

```
indirectbr ptr <address>, [ label <dest1>, label <dest2>, ... ]
```

##### Overview:

The ‘`indirectbr`’ instruction implements an indirect branch to a label within the current function, whose address is specified by “`address`”. Address must be derived from a blockaddress constant.

##### Arguments:

The ‘`address`’ argument is the address of the label to jump to. The rest of the arguments indicate the full set of possible destinations that the address may point to. Blocks are allowed to occur multiple times in the destination list, though this isn’t particularly useful.

This destination list is required so that dataflow analysis has an accurate understanding of the CFG.

##### Semantics:

Control transfers to the block specified in the address argument. All possible destination blocks must be listed in the label list, otherwise this instruction has undefined behavior. This implies that jumps to labels defined in other functions have undefined behavior as well. If ‘`address`’ is `poison` or `undef`, this instruction has undefined behavior.

##### Implementation:

This is typically implemented with a jump through a register.

##### Example:

```llvm
indirectbr ptr %Addr, [ label %bb1, label %bb2, label %bb3 ]
```

##### Syntax:

```
<result> = invoke [cconv] [ret attrs] [addrspace(<num>)] <ty>|<fnty> <fnptrval>(<function args>) [fn attrs]
              [operand bundles] to label <normal label> unwind label <exception label>
```

##### Overview:

The ‘`invoke`’ instruction causes control to transfer to a specified function, with the possibility of control flow transfer to either the ‘`normal`’ label or the ‘`exception`’ label. If the callee function returns with the “`ret`” instruction, control flow will return to the “normal” label. If the callee (or any indirect callees) returns via the “resume” instruction or other exception handling mechanism, control is interrupted and continued at the dynamically nearest “exception” label.

The ‘`exception`’ label is a landing pad for the exception. As such, ‘`exception`’ label is required to have the “landingpad” instruction, which contains the information about the behavior of the program after unwinding happens, as its first non-PHI instruction. The restrictions on the “`landingpad`” instruction’s tightly couples it to the “`invoke`” instruction, so that the important information contained within the “`landingpad`” instruction can’t be lost through normal code motion.

##### Arguments:

This instruction requires several arguments:

1. The optional “cconv” marker indicates which calling convention the call should use. If none is specified, the call defaults to using C calling conventions.
2. The optional Parameter Attributes list for return values. Only ‘`zeroext`’, ‘`signext`’, ‘`noext`’, and ‘`inreg`’ attributes are valid here.
3. The optional addrspace attribute can be used to indicate the address space of the called function. If it is not specified, the program address space from the datalayout string will be used.
4. ‘`ty`’: the type of the call instruction itself which is also the type of the return value. Functions that return no value are marked `void`. The signature is computed based on the return type and argument types.
5. ‘`fnty`’: shall be the signature of the function being invoked. The argument types must match the types implied by this signature. This is only required if the signature specifies a varargs type.
6. ‘`fnptrval`’: An LLVM value containing a pointer to a function to be invoked. In most cases, this is a direct function invocation, but indirect `invoke`’s are just as possible, calling an arbitrary pointer to function value.
7. ‘`function args`’: argument list whose types match the function signature argument types and parameter attributes. All arguments must be of first class type. If the function signature indicates the function accepts a variable number of arguments, the extra arguments can be specified.
8. ‘`normal label`’: the label reached when the called function executes a ‘`ret`’ instruction.
9. ‘`exception label`’: the label reached when a callee returns via the resume instruction or other exception handling mechanism.
10. The optional function attributes list.
11. The optional operand bundles list.

##### Semantics:

This instruction is designed to operate as a standard ‘`call`’ instruction in most regards. The primary difference is that it establishes an association with a label, which is used by the runtime library to unwind the stack.

This instruction is used in languages with destructors to ensure that proper cleanup is performed in the case of either a `longjmp` or a thrown exception. Additionally, this is important for implementation of ‘`catch`’ clauses in high-level languages that support them.

For the purposes of the SSA form, the definition of the value returned by the ‘`invoke`’ instruction is deemed to occur on the edge from the current block to the “normal” label. If the callee unwinds then no return value is available.

##### Example:

```llvm
%retval = invoke i32 @Test(i32 15) to label %Continue
            unwind label %TestCleanup              ; i32:retval set
%retval = invoke coldcc i32 %Testfnptr(i32 15) to label %Continue
            unwind label %TestCleanup              ; i32:retval set
```

##### Syntax:

```
<result> = callbr [cconv] [ret attrs] [addrspace(<num>)] <ty>|<fnty> <fnptrval>(<function args>) [fn attrs]
              [operand bundles] to label <fallthrough label> [indirect labels]
```

##### Overview:

The ‘`callbr`’ instruction causes control to transfer to a specified function, with the possibility of control flow transfer to either the ‘`fallthrough`’ label or one of the ‘`indirect`’ labels.

This instruction can currently only be used

1. to implement the “goto” feature of gcc style inline assembly or
2. to call selected intrinsics.
