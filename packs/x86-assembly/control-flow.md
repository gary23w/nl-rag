---
title: "x86 Assembly/Control Flow"
source: https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
---

# x86 Assembly/Control Flow

<

X86 Assembly

|   | Wikipedia has related information at ***Control flow***. |
|---|---|

Almost all programming languages have the ability to change the order in which statements are evaluated, and assembly is no exception. The instruction pointer (EIP) register contains the address of the next instruction to be executed. To change the flow of control, the programmer must be able to modify the value of EIP. This is where control flow functions come in.

```mw
mov eip, label   ; wrong
jmp label        ; right
```

## Comparison Instructions

| **test** reference, accumulator | GAS Syntax |
|---|---|
| **test** accumulator, reference | Intel Syntax |

Performs a bit-wise logical `and` on `accumulator` and `reference` the result of which we will refer to as `commonBits` and sets the `ZF`(zero), `SF`(sign) and `PF` (parity) flags based on `commonBits`. `CommonBits` is then discarded.

**Operands**

*reference*

- Register
- Immediate

*accumulator*

- Register (where `AL/AX/EAX` can be encoded specially if `reference` is an immediate value)
- Memory

**Modified flags**

- `SF` ≔ MostSignificantBit(`commonBits`)
- `ZF` ≔ (`commonBits` = 0), so a set `ZF` means, `accumulator` and `reference` do not have any set bits in common
- `PF` ≔ BitWiseXorNor(`commonBits`[Max-1:0]), so `PF` is set if and only if `commonBits`[Max-1:0] has an even number of 1 bits
- `CF` ≔ 0
- `OF` ≔ 0
- `AF` is undefined

**Application**

- passing the same register twice: `test rax, rax`
  - `SF` becomes the *sign* of `rax`, which is a simple test for non-negativity
  - `ZF` is set if `rax` is *zero*
  - `PF` is set if `rax` has an even number of set bits

| **cmp** subtrahend, minuend | GAS Syntax |
|---|---|
| **cmp** minuend, subtrahend | Intel Syntax |

Performs a comparison operation between `minuend` and `subtrahend`. The comparison is performed by a (signed) subtraction of `subtrahend` from `minuend`, the results of which can be called `difference`. `Difference` is then discarded. If `subtrahend` is an immediate value it will be sign extended to the length of `minuend`. The `EFLAGS` register is set in the same manner as a `sub` instruction.

Note that the GAS/AT&T syntax can be rather confusing, as for example `cmp $0, %rax` followed by `jl branch` will branch if `%rax < 0` (and not the opposite as might be expected from the order of the operands).

**Operands**

*minuend*

- `AL/AX/EAX` (only if `subtrahend` is immediate)
- Register
- Memory

*subtrahend*

- Register
- Immediate
- Memory

**Modified flags**

- `SF` ≔ MostSignificantBit(`difference`), so an unset `SF` means the `difference` is non-negative (`minuend` ≥ `subtrahend` [NB: signed comparison])
- `ZF` ≔ (`difference` = 0)
- `PF` ≔ BitWiseXorNor(`difference`[Max-1:0])
- `CF`, `OF` and `AF`

## Jump Instructions

The jump instructions allow the programmer to (indirectly) set the value of the EIP register. The location passed as the argument is usually a label. The first instruction executed after the jump is the instruction immediately following the label. All of the jump instructions, with the exception of `jmp`, are **conditional jumps**, meaning that program flow is diverted only if a condition is true. These instructions are often used after a comparison instruction (see above), but since many other instructions set flags, this order is not required.

See chapter “X86 architecture”, § “EFLAGS register” for more information about the flags and their meaning.

### Unconditional Jumps

**jmp** loc

Loads `EIP` with the specified address (i.e. the next instruction executed will be the one specified by `jmp`).

### Jump if Equal

**je** loc

*ZF = 1*

Loads `EIP` with the specified address, if operands of previous `cmp` instruction are equal. `je` is identical to `jz`. For example:

```mw
mov ecx, $5
mov edx, $5
cmp ecx, edx
je equal
; if it did not jump to the label equal,
; then this means ecx and edx are not equal.
equal:
; if it jumped here, then this means ecx and edx are equal
```

### Jump if Not Equal

**jne** loc

*ZF = 0*

Loads `EIP` with the specified address, if operands of previous `cmp` instruction are not equal. `jne` is identical to `jnz`

### Jump if Greater

**jg** loc

*SF = OF and ZF = 0*

Loads `EIP` with the specified address, if the `minuend` of the previous `cmp` instruction is greater than the `subtrahend` (performs signed comparison).

### Jump if Greater or Equal

**jge** loc

*SF = OF or ZF = 1*

Loads `EIP` with the specified address, if the `minuend` of the of previous `cmp` instruction is greater than or equal to the `subtrahend` (performs signed comparison).

### Jump if Above (unsigned comparison)

**ja** loc

*CF = 0 and ZF = 0*

Loads `EIP` with the specified address, if the `minuend` of the previous `cmp` instruction is greater than the `subtrahend`. `ja` is the same as `jg`, except that it performs an unsigned comparison.

That means, the following piece of code *always* jumps (unless `rbx` is `-1`, too), because negative one is represented as all bits set in the two's complement.

```mw
mov rax, -1 // rax := -1
cmp rax, rbx
ja loc
```

Interpreting all bits set (without treating any bit as the sign) has the value 2ⁿ-1 (where n is the length of the register). That is the largest unsigned value a register can hold.

### Jump if Above or Equal (unsigned comparison)

**jae** loc

*CF = 0 or ZF = 1*

Loads `EIP` with the specified address, if the `minuend` of previous `cmp` instruction is greater than or equal to the `subtrahend`. `jae` is the same as `jge`, except that it performs an unsigned comparison.

### Jump if Lesser

**jl** loc

The criterion required for a `jl` is that `SF` ≠ `OF`. It loads `EIP` with the specified address, if the criterion is met. So either `SF` or `OF` can be set, but not both in order to satisfy this criterion. If we take the `sub` (which is *basically* what a `cmp` does) instruction as an example, we have:

minuend

-

subtrahend

With respect to `sub` and `cmp` there are several cases that fulfill this criterion:

1. `minuend` < `subtrahend` and the operation does not have overflow
2. `minuend` > `subtrahend` and the operation has an overflow

In the first case `SF` will be set but not `OF` and in second case `OF` will be set but not `SF` since the overflow will reset the most significant bit to zero and thus preventing `SF` being set. The `SF` ≠ `OF` criterion avoids the cases where:

1. `minuend` > `subtrahend` and the operation does not have overflow
2. `minuend` < `subtrahend` and the operation has an overflow
3. `minuend` = `subtrahend`

In the first case neither `SF` nor `OF` are set, in the second case `OF` will be set and `SF` will be set since the overflow will reset the most significant bit to one and in the last case neither `SF` nor `OF` will be set.

### Jump if Less or Equal

**jle** loc

`SF` ≠ `OF` or `ZF = 1`.

Loads `EIP` with the specified address, if the `minuend` of previous `cmp` instruction is lesser than or equal to the `subtrahend`. See the `jl` section for a more detailed description of the criteria.

### Jump if Below (unsigned comparison)

**jb** loc

*CF = 1*

Loads EIP with the specified address, if first operand of previous CMP instruction is lesser than the second. `jb` is the same as `jl`, except that it performs an unsigned comparison.

```mw
mov rax, 0   ; rax ≔ 0
cmp rax, rbx ; rax ≟ rbx
jb loc       ; always jumps, unless rbx is also 0
```

### Jump if Below or Equal (unsigned comparison)

**jbe** loc

*CF = 1 or ZF = 1*

Loads `EIP` with the specified address, if `minuend` of previous `cmp` instruction is lesser than or equal to the `subtrahend`. `jbe` is the same as `jle`, except that it performs an unsigned comparison.

### Jump if Zero

**jz** loc

*ZF = 1*

Loads `EIP` with the specified address, if the zero bit is set from a previous arithmetic expression. `jz` is identical to `je`.

### Jump if Not Zero

**jnz** loc

*ZF = 0*

Loads `EIP` with the specified address, if the zero bit is not set from a previous arithmetic expression. `jnz` is identical to `jne`.

### Jump if Signed

**js** loc

*SF = 1*

Loads `EIP` with the specified address, if the sign bit is set from a previous arithmetic expression.

### Jump if Not Signed

**jns** loc

*SF = 0*

Loads `EIP` with the specified address, if the sign bit is not set from a previous arithmetic expression.

### Jump if Carry

**jc** loc

*CF = 1*

Loads `EIP` with the specified address, if the carry bit is set from a previous arithmetic expression.

### Jump if Not Carry

**jnc** loc

*CF = 0*

Loads `EIP` with the specified address, if the carry bit is not set from a previous arithmetic expression.

### Jump if Overflow

**jo** loc

*OF = 1*

Loads `EIP` with the specified address, if the overflow bit is set on a previous arithmetic expression.

### Jump if Not Overflow

**jno** loc

*OF = 0*

Loads `EIP` with the specified address, if the overflow bit is not set on a previous arithmetic expression.

### Jump if counter register is zero

**jcxz** loc

*CX = 0*

**jecxz** loc

*ECX = 0*

**jrcxz** loc

*RCX = 0*

Loads `EIP` with the specified address if the counter register is zero.

#### Application

- The existence of this instruction makes the counter register particularly suitable for holding (high-level language) pointers: In most programming languages the “null pointer”, an invalid pointer, is implemented by the numeric value `0`. Usually, you do *not* want to dereference such a null pointer as the result will be bogus or even cause a GPF. By jumping away, with `jecxz`, to some code handling this error, you can avoid running into such a situation *before* you attempt to dereference the pointer value. You do not need an extra `test ecx, ecx`.
- If you are using the `loop` instruction to implement a loop, but it is possible the requested number of iteration is zero, you may want to insert a `jecxz` *before* the loop’s body. Otherwise, `loop` will decrement zero, thus ending up doing 232 iterations.

## Function Calls

**call** proc

Pushes the address of the instruction that follows the `call` call, i.e. usually the next line in your source code, onto the top of the stack, and then jumps to the specified location. This is used mostly for subroutines.

**ret** [val]

Pops the next value on the stack into `EIP`, and then pops the specified number of bytes off the stack. If `val` is not supplied, the instruction will not pop any values off the stack after returning.

## Loop Instructions

**loop** arg

The `loop` instruction decrements `ECX` and jumps to the address specified by `arg` unless decrementing `ECX` caused its value to become zero. For example:

```mw
	mov ecx, 5 ; ecx ≔ 5
head:
	; the code here would be executed 5 times
	loop head
```

`loop` does not set any flags.

**loopcc** arg

These loop instructions decrement `ECX` and jump to the address specified by `arg` if their condition is satisfied (that is, a specific flag is set), unless decrementing `ECX` caused its value to become zero.

- `loope` loop if equal
- `loopne` loop if not equal
- `loopnz` loop if not zero
- `loopz` loop if zero

That way, only testing for a non-zero `ECX` can be combined with testing `ZF`. Other flags can not be tested for, say there is no `loopnc` “loop while `ECX` ≠ 0 and `CF` unset”.

## Enter and Leave

**enter** arg

`enter` creates a stack frame with the specified amount of space allocated on the stack.

**leave**

`leave` destroys the current stack frame, and restores the previous frame. Using Intel syntax this is equivalent to:

```mw
mov esp, ebp ; esp ≔ ebp
pop ebp
```

This will set `EBP` and `ESP` to their respective value before the function prologue began therefore reversing any modification to the stack that took place during the prologue.

## Other Control Instructions

**hlt**

Halts the processor. Execution will be resumed after processing next hardware interrupt, unless `IF` is cleared.

**nop**

No operation. This instruction doesn't do anything, but wastes (an) instruction cycle(s) in the processor.

This instruction is often *represented* as an `xchg` operation with the operands `EAX` and `EAX` (an operation without side-effects), because there is no designated opcode for doing nothing. This just as a passing remark, so that you do not get confused with *disassembled* code.

**lock**

Asserts #LOCK prefix on next instruction.

**wait**

Waits for the FPU to finish its last calculation.

Retrieved from "

https://en.wikibooks.org/w/index.php?title=X86_Assembly/Control_Flow&oldid=4532017

"
