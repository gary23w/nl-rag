---
title: "List of x86 instructions (part 1/5)"
source: https://en.wikipedia.org/wiki/X86_instruction_listings
domain: x86-assembly
license: CC-BY-SA-4.0
tags: x86 assembly, assembly language, x86, x86-64, amd64, asm
fetched: 2026-07-02
part: 1/5
---

# List of x86 instructions

(Redirected from

X86 instruction listings

)

The x86 instruction set refers to the set of instructions that x86-compatible microprocessors support. The instructions are usually part of an executable program, often stored as a computer file and executed on the processor.

The x86 instruction set has been extended several times, introducing wider registers and datatypes as well as new functionality.

## x86 integer instructions

Below is the full 8086/8088 instruction set of Intel (81 instructions total). These instructions are also available in 32-bit mode, in which they operate on 32-bit registers (**eax**, **ebx**, etc.) and values instead of their 16-bit (**ax**, **bx**, etc.) counterparts. The updated instruction set is grouped according to architecture (i186, i286, i386, i486, i586/i686) and is referred to as (32-bit) x86 and (64-bit) x86-64 (also known as AMD64).

### Original 8086/8088 instructions

This is the original instruction set. In the 'Notes' column, *r* means *register*, *m* means *memory address* and *imm* means *immediate* (i.e. a value).

| In- struc- tion | Meaning | Notes | Opcode |
|---|---|---|---|
| AAA | ASCII adjust AL after addition | used with unpacked binary-coded decimal | 0x37 |
| AAD | ASCII adjust AX before division | 8086/8088 datasheet documents only base 10 version of the AAD instruction (opcode 0xD5 0x0A), but any other base will work. Later Intel's documentation has the generic form too. NEC V20 and V30 (and possibly other NEC V-series CPUs) always use base 10, and ignore the argument, causing a number of incompatibilities | 0xD5 |
| AAM | ASCII adjust AX after multiplication | Only base 10 version (Operand is 0xA) is documented, see notes for AAD | 0xD4 |
| AAS | ASCII adjust AL after subtraction |   | 0x3F |
| ADC | Add with carry | (1) `r += (r/m/imm+CF);` (2) `m += (r/imm+CF);` | 0x10...0x15, 0x80...0x81/2, 0x83/2 |
| ADD | Add | (1) `r += r/m/imm;` (2) `m += r/imm;` | 0x00...0x05, 0x80/0...0x81/0, 0x83/0 |
| AND | Logical AND | (1) `r &= r/m/imm;` (2) `m &= r/imm;` | 0x20...0x25, 0x80...0x81/4, 0x83/4 |
| CALL | Call procedure | (1) push IP, jmp within segment; (2) push CS:IP, jump intersegment | 0x9A, 0xE8, 0xFF/2, 0xFF/3 |
| CBW | Convert byte to word | `AH = (sign)AL` | 0x98 |
| CLC | Clear carry flag | `CF = 0;` | 0xF8 |
| CLD | Clear direction flag | `DF = 0;` | 0xFC |
| CLI | Clear interrupt flag | `IF = 0;` | 0xFA |
| CMC | Complement carry flag | `CF = !CF;` | 0xF5 |
| CMP | Compare operands | (1) `r - r/m/imm;` (2) `m - r/imm;` | 0x38...0x3D, 0x80...0x81/7, 0x83/7 |
| CMPSB | Compare bytes in memory. May be used with a REPE or REPNE prefix to test and repeat the instruction CX times. | if (DF==0) *(byte*)SI++ - *(byte*)ES:DI++; else *(byte*)SI-- - *(byte*)ES:DI--; | 0xA6 |
| CMPSW | Compare words. May be used with a REPE or REPNE prefix to test and repeat the instruction CX times. | if (DF==0) *(word*)SI++ - *(word*)ES:DI++; else *(word*)SI-- - *(word*)ES:DI--; | 0xA7 |
| CWD | Convert word to doubleword | DX = (sign)AX | 0x99 |
| DAA | Decimal adjust AL after addition | (used with packed BCD) | 0x27 |
| DAS | Decimal adjust AL after subtraction | (used with packed BCD) | 0x2F |
| DEC | Decrement by 1 |   | 0x48...0x4F, 0xFE/1, 0xFF/1 |
| DIV | Unsigned divide | (1) `AX = DX:AX / r/m; DX = remainder` (2) `AL = AX / r/m;] AH = remainder` | 0xF7/6, 0xF6/6 |
| ESC | Used with floating-point unit |   | 0xD8..0xDF |
| HLT | Enter halt state |   | 0xF4 |
| IDIV | Signed divide | (1) `AX = DX:AX / r/m; DX = remainder` (2) `AL = AX / r/m; AH = remainder` | 0xF7/7, 0xF6/7 |
| IMUL | Signed multiply in One-operand form | (1) `DX:AX = AX * r/m;` (2) `AX = AL * r/m` | 0xF7/5, 0xF6/5 |
| IN | Input from port | (1) `AL = port[imm];` (2) `AL = port[DX];` (3) `AX = port[imm];` (4) `AX = port[DX];` | 0xE4, 0xE5, 0xEC, 0xED |
| INC | Increment by 1 |   | 0x40...0x47, 0xFE/0, 0xFF/0 |
| INT | Call to interrupt | *--SP = FLAGS; *--SP = CS; *--SP = IP | 0xCC, 0xCD |
| INTO | Call to interrupt if overflow | if (O == 1) *--SP = FLAGS; *--SP = CS; *--SP = IP | 0xCE |
| IRET | Return from interrupt | IP = *SP++, CS = *SP++, FLAGS = *SP++; | 0xCF |
| Jcc | Jump if condition | JA, JAE, JB, JBE, JC (same as JB), JE, JG, JGE, JL, JLE, JNA (same as JBE), JNAE (same as JB), JNB (same as JAE), JNBE (same as JA), JNC (same as JAE), JNE, JNG (same as JLE), JNGE (same as JL), JNL (same as JGE), JNLE (same as JG), JNO, JNP, JNS, JNZ (same as JNE), JO, JP, JPE (same as JP), JPO (same as JNP), JS, JZ (same as JE) | 0x70...0x7F |
| JCXZ | Jump if CX is zero | JECXZ for ECX instead of CX in 32 bit mode (same opcode). | 0xE3 |
| JMP | Jump | (1) jump within segment; (2) jump intersegment | 0xE9...0xEB, 0xFF/4, 0xFF/5 |
| LAHF | Load FLAGS into AH register |   | 0x9F |
| LDS | Load DS:r with far pointer | `r = m; DS = 2 + m;` | 0xC5 |
| LEA | Load Effective Address |   | 0x8D |
| LES | Load ES:r with far pointer | `r = m; ES = 2 + m;` | 0xC4 |
| LOCK | Assert BUS LOCK# signal | (for multiprocessing) | 0xF0 |
| LODSB | Load string byte. May be used with a REP prefix to repeat the instruction CX times. | `if (DF==0) AL = *SI++; else AL = *SI--;` | 0xAC |
| LODSW | Load string word. May be used with a REP prefix to repeat the instruction CX times. | `if (DF==0) AX = *SI++; else AX = *SI--;` | 0xAD |
| LOOP/ LOOPx | Loop control | (LOOPE, LOOPNE, LOOPNZ, LOOPZ) `if (x && --CX) goto lbl;` | 0xE0...0xE2 |
| MOV | Move | (1) `r = r/m/imm;` (2) `m = r/imm;` (3) `r/m = sreg;` (4) `sreg = r/m;` | 0x88...0x8C, 0x8E, 0xA0...0xA3, 0xB0...0xBF, 0xC6, 0xC7 |
| MOVSB | Move byte from string to string. May be used with a REP prefix to repeat the instruction CX times. | if (DF==0) *(byte*)ES:DI++ = *(byte*)SI++; else *(byte*)ES:DI-- = *(byte*)SI--; . | 0xA4 |
| MOVSW | Move word from string to string. May be used with a REP prefix to repeat the instruction CX times. | if (DF==0) *(word*)ES:DI++ = *(word*)SI++; else *(word*)ES:DI-- = *(word*)SI--; | 0xA5 |
| MUL | Unsigned multiply | (1) `DX:AX = AX * r/m;` (2) `AX = AL * r/m;` | 0xF7/4, 0xF6/4 |
| NEG | Two's complement negation | `r/m = 0 – r/m;` | 0xF6/3...0xF7/3 |
| NOP | No operation | opcode equivalent to `XCHG EAX, EAX` | 0x90 |
| NOT | Negate the operand, logical NOT | `r/m ^= -1;` | 0xF6/2...0xF7/2 |
| OR | Logical OR | (1) `r ∣= r/m/imm;` (2) `m ∣= r/imm;` | 0x08...0x0D, 0x80...0x81/1, 0x83/1 |
| OUT | Output to port | (1) `port[imm] = AL;` (2) `port[DX] = AL;` (3) `port[imm] = AX;` (4) `port[DX] = AX;` | 0xE6, 0xE7, 0xEE, 0xEF |
| POP | Pop data from stack | `r/m/sreg = *SP++;` | 0x07, 0x17, 0x1F, 0x58...0x5F, 0x8F/0 |
| POPF | Pop FLAGS register from stack | `FLAGS = *SP++;` | 0x9D |
| PUSH | Push data onto stack | `*--SP = r/m/sreg;` | 0x06, 0x0E, 0x16, 0x1E, 0x50...0x57, 0xFF/6 |
| PUSHF | Push FLAGS onto stack | `*--SP = FLAGS;` | 0x9C |
| RCL | Rotate left (with carry) |   | 0xC0...0xC1/2 (186+), 0xD0...0xD3/2 |
| RCR | Rotate right (with carry) |   | 0xC0...0xC1/3 (186+), 0xD0...0xD3/3 |
| REPxx | Repeat MOVS/STOS/CMPS/LODS/SCAS | (REP, REPE, REPNE, REPNZ, REPZ) | 0xF2, 0xF3 |
| RET | Return from procedure | Not a real instruction. The assembler will translate these to a RETN or a RETF depending on the memory model of the target system. |   |
| RETN | Return from near procedure |   | 0xC2, 0xC3 |
| RETF | Return from far procedure |   | 0xCA, 0xCB |
| ROL | Rotate left |   | 0xC0...0xC1/0 (186+), 0xD0...0xD3/0 |
| ROR | Rotate right |   | 0xC0...0xC1/1 (186+), 0xD0...0xD3/1 |
| SAHF | Store AH into FLAGS |   | 0x9E |
| SAL | Shift Arithmetically left (signed shift left) | (1) `r/m <<= 1;` (2) `r/m <<= CL;` | 0xC0...0xC1/4 (186+), 0xD0...0xD3/4 |
| SAR | Shift Arithmetically right (signed shift right) | (1) `(signed) r/m >>= 1;` (2) `(signed) r/m >>= CL;` | 0xC0...0xC1/7 (186+), 0xD0...0xD3/7 |
| SBB | Subtraction with borrow | (1) `r -= (r/m/imm+CF);` (2) `m -= (r/imm+CF);` alternative 1-byte encoding of `SBB AL, AL` is available via undocumented SALC instruction | 0x18...0x1D, 0x80...0x81/3, 0x83/3 |
| SCASB | Compare byte string. May be used with a REPE or REPNE prefix to test and repeat the instruction CX times. | `if (DF==0) AL - *ES:DI++; else AL - *ES:DI--;` | 0xAE |
| SCASW | Compare word string. May be used with a REPE or REPNE prefix to test and repeat the instruction CX times. | `if (DF==0) AX - *ES:DI++; else AX - *ES:DI--;` | 0xAF |
| SHL | Shift left (unsigned shift left) | Same opcode as SAL, since logical left shifts are equal to arithmetical left shifts. | 0xC0...0xC1/4 (186+), 0xD0...0xD3/4 |
| SHR | Shift right (unsigned shift right) |   | 0xC0...0xC1/5 (186+), 0xD0...0xD3/5 |
| STC | Set carry flag | `CF = 1;` | 0xF9 |
| STD | Set direction flag | `DF = 1;` | 0xFD |
| STI | Set interrupt flag | `IF = 1;` | 0xFB |
| STOSB | Store byte in string. May be used with a REP prefix to repeat the instruction CX times. | `if (DF==0) *ES:DI++ = AL; else *ES:DI-- = AL;` | 0xAA |
| STOSW | Store word in string. May be used with a REP prefix to repeat the instruction CX times. | `if (DF==0) *ES:DI++ = AX; else *ES:DI-- = AX;` | 0xAB |
| SUB | Subtraction | (1) `r -= r/m/imm;` (2) `m -= r/imm;` | 0x28...0x2D, 0x80...0x81/5, 0x83/5 |
| TEST | Logical compare (AND) | (1) `r & r/m/imm;` (2) `m & r/imm;` | 0x84, 0x85, 0xA8, 0xA9, 0xF6/0, 0xF7/0 |
| WAIT | Wait until not busy | Waits until BUSY# pin is inactive (used with floating-point unit) | 0x9B |
| XCHG | Exchange data | `r :=: r/m;` A spinlock typically uses xchg as an atomic operation. (coma bug). | 0x86, 0x87, 0x91...0x97 |
| XLAT | Table look-up translation | behaves like `MOV AL, [BX+AL]` | 0xD7 |
| XOR | Exclusive OR | (1) `r ^+= r/m/imm;` (2) `m ^= r/imm;` | 0x30...0x35, 0x80...0x81/6, 0x83/6 |

### Added in specific processors

#### Added with 80186/80188

New instructions and instruction forms added in the Intel 80186 and 80188. Also present in the NEC V20/V30 processors and their successors.

| Instruction mnemonic | Opcode | Instruction description | Ring |
|---|---|---|---|
| `PUSHA` | `60` | Push all general purpose registers onto the stack. Pushes AX,CX,DX,BX,SP,BP,SI,DI onto the stack in that order. The value of SP pushed onto the stack is the initial value of SP before the `PUSHA` instruction. | 3 |
| `POPA` | `61` | Pop all general purpose registers from stack. The registers are popped from the stack into registers in the reverse order of that of `PUSHA` (the popped item that corresponds to the SP register is popped but not put in any register.) |   |
| `BOUND reg,m16&16` | `NFx 62 /r` | Read a pair of signed array bounds from memory, then check that the register-argument is neither below the first bound nor above the second bound. If either test fails, a bounds range-exceeded exception (#BR, interrupt vector 5) is raised. |   |
|   |   |   |   |
| `PUSH imm` | `68 *iw*` | Push an immediate word (or byte sign-extended to word) value onto the stack. Examples: PUSH 12h ; encoded as 6Ah 12h PUSH 1234h ; encoded as 68h 34h 12h | 3 |
| `6A *ib*` |   |   |   |
| `IMUL reg,r/m,imm`, `IIMUL reg,r/m,imm` | `69 /r *iw*` | Non-widening 3-argument integer word multiply with immediate. Examples: IMUL CX, DX, 12h IMUL BX, SI, 1200h IMUL DI, word ptr [BX+SI], 12h IMUL SI, word ptr [BP-4], 1200h Note that since the lower half is the same for unsigned and signed multiplication, this version of the instruction can be used for both. |   |
| `6B /r *ib*` |   |   |   |
| `INSB` | `6C` | 8-bit input from I/O port to string. Operation is equivalent to: IN AL, DX STOSB ; adjust DI according to operand size and DF | Usually 0 |
| `INSW` | `6D` | 16-bit input from I/O port to string. |   |
| `OUTSB` | `6E` | 8-bit output from string to I/O port. Operation is equivalent to: LODSB ; adjust SI according to operand size and DF OUT DX, AL |   |
| `OUTSW` | `6F` | 16-bit output from string to I/O port. |   |
|   |   |   |   |
| `ROL r/m, imm8` | `C0 /0 *ib*` `C1 /0 *ib*` | Rotate left immediate | 3 |
| `ROR r/m, imm8` | `C0 /1 *ib*`, `C1 /1 *ib*` | Rotate right immediate |   |
| `RCL r/m, imm8` | `C0 /2 *ib*`, `C1 /2 *ib*` | Rotate left through carry with immediate rotate-amount |   |
| `RCR r/m, imm8` | `C0 /3 *ib*`, `C1 /3 *ib*` | Rotate right through carry with immediate rotate-amount |   |
| `SHL r/m, imm8` | `C0 /4 *ib*`, `C1 /4 *ib*` | Shift left immediate |   |
| C0 /6 *ib*,  C1 /6 *ib* |   |   |   |
| `SHR r/m, imm8` | `C0 /5 *ib*`, `C1 /5 *ib*` | Unsigned shift right immediate |   |
| `SAR r/m, imm8` | `C0 /7 *ib*`, `C1 /7 *ib*` | Signed shift right immediate |   |
|   |   |   |   |
| `ENTER imm16,imm8` | `C8 *iw ib*` | Create procedure stack frame. The first operand specifies the size of the stack frame to allocate by the instruction, the second operand specifies nesting level (the number of earlier stack frame pointers for the CPU to copy before adjusting the stack pointer). The operation of `ENTER arg1,arg2` is: PUSH rBP temp1 := rSP if( arg2 > 0 ) { for( i = 1; i<arg2; i++ ) { temp2 := read_mem[SS:rBP-i*OperandSize] PUSH temp2 } PUSH rBP } rSP := rSP - arg1 ; allocate stack - updates SP/ESP/RSP based on StackAddressSize rBP := temp1 ; set frame pointer - updates BP/EBP/RBP based on OperandSize | 3 |
| `LEAVE` | `C9` | Release procedure stack created by previous `ENTER` instruction. Operation is equivalent to:MOV rSP,rBP ; release stack - updates SP/ESP/RSP based on StackAddressSize POP rBP ; restore old frame pointer - updates BP/EBP/RBP based on OperandSize |   |
|   |   |   |   |
| `UDW` | `FF FF` | The 80186/80188 did introduce the #UD exception, but did not explicitly reserve any opcode encoding for triggering #UD. The use of two bytes with all bits set to one is convenient – it works if memory has been explicitly initialized to all bits set to one, and it works if a chipset responds to non-DRAM non-MMIO accesses (in this case: code fetches) with bytes that have all bits set to one. No subsequent x86 processor has ever allocated this encoding for anything else. To ensure that its #UD behavior persists, the name UDW is used. This follows the naming convention precedence set by UDB: there the B denotes the byte length; here the W denotes the x86 word length. It also avoids UD{0,1,2}. group #5 (1st FF) with a modrm byte of mod=11b r/m=111b (/7) reg=111b (2nd FF) |   |

1. Protection rings apply to 80286 and later, not to 80186.
2. In 64-bit mode, the `PUSHA`, `POPA` and `BOUND` instructions are not available — the `PUSHA` and `POPA` opcodes will cause #UD, and the `BOUND` opcode (`62`) is repurposed for the EVEX prefix.
3. On some processors, including some 80186 variants, using repeat-prefixes with the `BOUND` instruction will modify its operation to compare only the lower-bound. For this reason, repeat-prefixes should be avoided for this instruction.
4. On Intel 80186/80188 and NEC V-series processors, bounds-check failure will cause #BR to be issued as a trap-type exception (the value of CS:IP stored on the stack points to the instruction following the `BOUND` instruction), while on 80286 and later processors, it is issued as a fault-type exception (the value of CS:IP stored on the stack is that of the `BOUND` instruction itself).
5. The "`IIMUL`" mnemonic for the 80186 multiply-immediate instruction is sometimes used in IBM PC documentation, but is not commonly used otherwise.
6. The `REP` (`F3`) prefix can be used with the `INSB`/`INSW`/`OUTSB`/`OUTSW` instructions. Doing so will cause the instruction to be repeated the number of times specified in rCX. (setting rCX to 0 will cause zero repetitions, i.e. the instructions will act as NOPs)
7. On 80286 and later processors, the `INSB`/`INSW` instructions may perform access-rights checks for its memory store after the read from the I/O port has been performed - if any of these checks fail (e.g. segfault or page-fault), then the data item read from the I/O port is lost. For this reason, using the `INSB`/`INSW` instructions to read an I/O port that has side-effects upon read is not recommended.
8. I/O port access is only allowed when CPL≤IOPL, or (on 80386 and later) the I/O port permission bitmap bits for the port to access are all set to 0.
9. For the ROL/ROR/RCL/RCR/SHL/SHR/SAR instructions, opcode `C0` is used for byte variants and opcode `C1` is used for word variants. For the `C0`/`C1` immediate versions of the shift/rotate instructions, only the bottom 5 bits of the immediate are used (6 bits for opcode `C1` if it is encoded with a 64-bit operand-size under x86-64)
10. On 80186 and later, sub-opcode /6 for the shift-opcodes `C0`/`C1`/`D0`/`D1`/`D2`/`D3` acts as an (often poorly documented) alias of sub-opcode /4 — these are all variants of the `SHL` instruction.
11. The first argument to the `ENTER` instruction is always a 16-bit unsigned immediate regardless of OperandSize.The second argument to `ENTER` is an 8-bit immediate - on 80186/80188 and NEC V-series processors, all 8 bits are used, but 80286 and later processors use only the bottom 5 bits.
12. On newer processors, the `ENTER` instruction will, after setting up the stack frame, check whether the byte location pointed to by the new value of SS:rSP is writable — if it isn't, then it will generate the same exception (e.g. page-fault) as a write to that address would have caused.

#### Added with 80286

The new instructions added in 80286 add support for x86 protected mode. Some but not all of the instructions are available in real mode as well.

| Instruction | Opcode | Instruction description | Real mode | Ring |
|---|---|---|---|---|
|   |   |   |   |   |
| `LGDT m16&32` | `0F 01 /2` | Load GDTR (Global Descriptor Table Register) from memory. | Yes | 0 |
| `LIDT m16&32` | `0F 01 /3` | Load IDTR (Interrupt Descriptor Table Register) from memory. The IDTR controls not just the address/size of the IDT (interrupt Descriptor Table) in protected mode, but the IVT (Interrupt Vector Table) in real mode as well. |   |   |
| `LMSW r/m16` | `0F 01 /6` | Load MSW (Machine Status Word) from 16-bit register or memory. |   |   |
| `CLTS` | `0F 06` | Clear task-switched flag in the MSW. |   |   |
| `LLDT r/m16` | `0F 00 /2` | Load LDTR (Local Descriptor Table Register) from 16-bit register or memory. | #UD |   |
| `LTR r/m16` | `0F 00 /3` | Load TR (Task Register) from 16-bit register or memory. The TSS (Task State Segment) specified by the 16-bit argument is marked busy, but a task switch is not done. |   |   |
|   |   |   |   |   |
| `SGDT m16&32` | `0F 01 /0` | Store GDTR to memory. | Yes | Usually 3 |
| `SIDT m16&32` | `0F 01 /1` | Store IDTR to memory. |   |   |
| `SMSW r/m16` | `0F 01 /4` | Store MSW to register or 16-bit memory. |   |   |
| `SLDT r/m16` | `0F 00 /0` | Store LDTR to register or 16-bit memory. | #UD |   |
| `STR r/m16` | `0F 00 /1` | Store TR to register or 16-bit memory. |   |   |
|   |   |   |   |   |
| `ARPL r/m16,r16` | `63 /r` | Adjust RPL (Requested Privilege Level) field of selector. The operation performed is:if (dst & 3) < (src & 3) then dst = (dst & 0xFFFC) \| (src & 3) eflags.zf = 1 else eflags.zf = 0 | #UD | 3 |
| `LAR r,r/m16` | `0F 02 /r` | Load access rights byte from the specified segment descriptor. Reads bytes 4-7 of segment descriptor, bitwise-ANDs it with `0x00FxFF00`, then stores the bottom 16/32 bits of the result in destination register. Sets EFLAGS.ZF=1 if the descriptor could be loaded, ZF=0 otherwise. | #UD |   |
| `LSL r,r/m16` | `0F 03 /r` | Load segment limit from the specified segment descriptor. Sets ZF=1 if the descriptor could be loaded, ZF=0 otherwise. |   |   |
| `VERR r/m16` | `0F 00 /4` | Verify a segment for reading. Sets ZF=1 if segment can be read, ZF=0 otherwise. |   |   |
| `VERW r/m16` | `0F 00 /5` | Verify a segment for writing. Sets ZF=1 if segment can be written, ZF=0 otherwise. |   |   |
|   |   |   |   |   |
| LOADALL | 0F 05 | Load all CPU registers from a 102-byte data structure starting at physical address `800h`, including "hidden" part of segment descriptor registers. | Yes | 0 |
| STOREALL | F1 0F 04 | Store all CPU registers to a 102-byte data structure starting at physical address `800h`, then shut down CPU. |   |   |

1. The descriptors used by the `LGDT`, `LIDT`, `SGDT` and `SIDT` instructions consist of a 2-part data structure. The first part is a 16-bit value, specifying table size in bytes minus 1. The second part is a 32-bit value (64-bit value in 64-bit mode), specifying the linear start address of the table. For `LGDT` and `LIDT` with a 16-bit operand size, the address is ANDed with 00FFFFFFh.On Intel (but not AMD) CPUs, the `SGDT` and `SIDT` instructions with a 16-bit operand size is – as of Intel SDM revision 079, March 2023 – documented to write a descriptor to memory with the last byte being set to 0. However, observed behavior is that bits 31:24 of the descriptor table address are written instead.On the Intel 80286, the last byte written by `SGDT`/`SIDT` is always 0xFF - this has been used by software (e.g. an NE2000 NDIS driver and Microsoft Windows 3.0) to detect whether the CPU is an 80286 or not.
2. The `LGDT`, `LIDT`, `LLDT` and `LTR` instructions are serializing on Pentium and later processors.
3. The `LMSW` instruction is serializing on Intel processors from Pentium onwards, but not on AMD processors.When the `LMSW` instruction is used to enter Protected mode, it should be immediately followed by a jump instruction to clear the prefetch queue. (On the Intel 80286, executing three non-jump instructions immediately after an `LMSW` that enters protected mode has been reported to cause a CPU reset.)
4. On 80386 and later, the "Machine Status Word" is the same as the CR0 control register – however, the `LMSW` instruction can only modify the bottom 4 bits of this register and cannot clear bit 0. The inability to clear bit 0 means that `LMSW` can be used to enter but not leave x86 Protected Mode. On 80286, it is not possible to leave Protected Mode at all (neither with `LMSW` nor with `LOADALL`) without a CPU reset – on 80386 and later, it is possible to leave Protected Mode, but this requires the use of the 80386-and-later `MOV` to `CR0` instruction.
5. If `CR4.UMIP=1` is set, then the `SGDT`, `SIDT`, `SLDT`, `SMSW` and `STR` instructions can only run in Ring 0. These instructions were unprivileged on all x86 CPUs from 80286 onwards until the introduction of UMIP in 2017. This has been a significant security problem for software-based virtualization, since it enables these instructions to be used by a VM guest to detect that it is running inside a VM.
6. The `SMSW`, `SLDT` and `STR` instructions always use an operand size of 16 bits when used with a memory argument. With a register argument on 80386 or later processors, wider destination operand sizes are available and behave as follows: `SMSW`: Stores full CR0 in 64-bit mode on x86-64 CPUs, undefined otherwise. `SLDT`: Zero-extends 16-bit argument on Pentium Pro and later processors, undefined on earlier processors. `STR`: Zero-extends 16-bit argument.
7. On processors with x86-64, the `ARPL` instruction is not available in 64-bit mode – the `63 /r` opcode has been reassigned to the 64-bit-mode-only `MOVSXD` instruction.
8. The `ARPL` instruction causes #UD in Real mode and Virtual 8086 Mode – Windows 95 and OS/2 2.x are known to make extensive use of this #UD to use the `63` opcode as a one-byte breakpoint to transition from Virtual 8086 mode to kernel mode.
9. Bits 19:16 of this mask are documented as "undefined" on Intel CPUs. On AMD CPUs, the mask is documented as `0x00FFFF00`.
10. For the `LAR` and `LSL` instructions, if the specified segment descriptor could not be loaded, then the instruction's destination register is left unmodified.
11. On some Intel CPU/microcode combinations from 2019 onwards, as well as some AMD CPU/microcode combinations from 2025 onwards, the `VERW` instruction also flushes various microarchitectural data buffers in an implementation-specific manner. This enables it to be used as part of workarounds for security vulnerabilities such as Microarchitectural Data Sampling and Transient Scheduler Attacks. Some of the microarchitectural buffer-flushing functions that have been added to `VERW` may require the instruction to be executed with a memory operand.
12. Undocumented, 80286 only. (A different variant of `LOADALL` with a different opcode and memory layout exists on 80386.)

#### Added with 80386

The 80386 added support for 32-bit operation to the x86 instruction set. This was done by widening the general-purpose registers to 32 bits and introducing the concepts of *OperandSize* and *AddressSize* – most instruction forms that would previously take 16-bit data arguments were given the ability to take 32-bit arguments by setting their OperandSize to 32 bits, and instructions that could take 16-bit address arguments were given the ability to take 32-bit address arguments by setting their AddressSize to 32 bits. (Instruction forms that work on 8-bit data continue to be 8-bit regardless of OperandSize. Using a data size of 16 bits will cause only the bottom 16 bits of the 32-bit general-purpose registers to be modified – the top 16 bits are left unchanged.)

The default OperandSize and AddressSize to use for each instruction is given by the D bit of the segment descriptor of the current code segment - `D=0` makes both 16-bit, `D=1` makes both 32-bit. Additionally, they can be overridden on a per-instruction basis with two new instruction prefixes that were introduced in the 80386:

- `66h`: OperandSize override. Will change OperandSize from 16-bit to 32-bit if `CS.D=0`, or from 32-bit to 16-bit if `CS.D=1`.
- `67h`: AddressSize override. Will change AddressSize from 16-bit to 32-bit if `CS.D=0`, or from 32-bit to 16-bit if `CS.D=1`.

The 80386 also introduced the two new segment registers `FS` and `GS` as well as the x86 control, debug and test registers.

The new instructions introduced in the 80386 can broadly be subdivided into two classes:

- Pre-existing opcodes that needed new mnemonics for their 32-bit OperandSize variants (e.g. `CWDE`, `LODSD`)
- New opcodes that introduced new functionality (e.g. `SHLD`, `SETcc`)

For instruction forms where the operand size can be inferred from the instruction's arguments (e.g. `ADD EAX,EBX` can be inferred to have a 32-bit OperandSize due to its use of EAX as an argument), new instruction mnemonics are not needed and not provided.

| Type | Instruction mnemonic | Opcode | Description | Mnemonic for older 16-bit variant | Ring |
|---|---|---|---|---|---|
| String instructions | `LODSD` | `AD` | Load string doubleword: `EAX := DS:[rSI±±]` | `LODSW` | 3 |
| `STOSD` | `AB` | Store string doubleword: `ES:[rDI±±] := EAX` | `STOSW` |   |   |
| `MOVSD` | `A5` | Move string doubleword: `ES:[rDI±±] := DS:[rSI±±]` | `MOVSW` |   |   |
| `CMPSD` | `A7` | Compare string doubleword: temp1 := DS:[rSI±±] temp2 := ES:[rDI±±] CMP temp1, temp2 /* 32-bit compare and set EFLAGS */ | `CMPSW` |   |   |
| `SCASD` | `AF` | Scan string doubleword: temp1 := ES:[rDI±±] CMP EAX, temp1 /* 32-bit compare and set EFLAGS */ | `SCASW` |   |   |
| `INSD` | `6D` | Input string from doubleword I/O port:`ES:[rDI±±] := port[DX]` | `INSW` | Usually 0 |   |
| `OUTSD` | `6F` | Output string to doubleword I/O port:`port[DX] := DS:[rSI±±]` | `OUTSW` |   |   |
|   |   |   |   |   |   |
| Other | `CWDE` | `98` | Sign-extend 16-bit value in AX to 32-bit value in EAX | `CBW` | 3 |
| `CDQ` | `99` | Sign-extend 32-bit value in EAX to 64-bit value in EDX:EAX. Mainly used to prepare a dividend for the 32-bit `IDIV` (signed divide) instruction. | `CWD` |   |   |
| `JECXZ rel8` | `E3 *cb*` | Jump if ECX is zero | `JCXZ` |   |   |
| `PUSHAD` | `60` | Push all 32-bit registers onto stack | `PUSHA` |   |   |
| `POPAD` | `61` | Pop all 32-bit general-purpose registers off stack | `POPA` |   |   |
| `PUSHFD` | `9C` | Push 32-bit EFLAGS register onto stack | `PUSHF` | Usually 3 |   |
| `POPFD` | `9D` | Pop 32-bit EFLAGS register off stack | `POPF` |   |   |
| `IRETD` | `CF` | 32-bit interrupt return. Differs from the older 16-bit `IRET` instruction in that it will pop interrupt return items (EIP,CS,EFLAGS; also ESP and SS if there is a CPL change; and also ES,DS,FS,GS if returning to virtual 8086 mode) off the stack as 32-bit items instead of 16-bit items. Should be used to return from interrupts when the interrupt handler was entered through a 32-bit IDT interrupt/trap gate. Instruction is serializing. | `IRET` |   |   |

1. For the 32-bit string instructions, the ±± notation is used to indicate that the indicated register is post-decremented by 4 if `EFLAGS.DF=1` and post-incremented by 4 otherwise. For the operands where the DS segment is indicated, the DS segment can be overridden by a segment-override prefix – where the ES segment is indicated, the segment is always ES and cannot be overridden. The choice of whether to use the 16-bit SI/DI registers or the 32-bit ESI/EDI registers as the address registers to use is made by AddressSize, overridable with the `67` prefix.
2. The 32-bit string instructions accept repeat-prefixes in the same way as older 8/16-bit string instructions. For `LODSD`, `STOSD`, `MOVSD`, `INSD` and `OUTSD`, the `REP` prefix (`F3`) will repeat the instruction the number of times specified in rCX (CX or ECX, decided by AddressSize), decrementing rCX for each iteration (with rCX=0 resulting in no-op and proceeding to the next instruction). For `CMPSD` and `SCASD`, the `REPE` (`F3`) and `REPNE` (`F2`) prefixes are available, which will repeat the instruction, decrementing rCX for each iteration, but only as long as the flag condition (ZF=1 for `REPE`, ZF=0 for `REPNE`) holds true AND rCX ≠ 0.
3. For the `INSB/W/D` instructions, the memory access rights for the `ES:[rDI]` memory address might not be checked until after the port access has been performed – if this check fails (e.g. page fault or other memory exception), then the data item read from the port is lost. As such, it is not recommended to use this instruction to access an I/O port that performs any kind of side effect upon read.
4. I/O port access is only allowed when CPL≤IOPL or the I/O port permission bitmap bits for the port to access are all set to 0.
5. The `CWDE` instruction differs from the older `CWD` instruction in that `CWD` would sign-extend the 16-bit value in AX into a 32-bit value in the DX:AX register pair.
6. For the `E3` opcode (`JCXZ`/`JECXZ`), the choice of whether the instruction will use `CX` or `ECX` for its comparison (and consequently which mnemonic to use) is based on the AddressSize, not OperandSize. (OperandSize instead controls whether the jump destination should be truncated to 16 bits or not). This also applies to the loop instructions `LOOP`,`LOOPE`,`LOOPNE` (opcodes `E0`,`E1`,`E2`), however, unlike `JCXZ`/`JECXZ`, these instructions have not been given new mnemonics for their ECX-using variants.
7. For `PUSHA(D)`, the value of SP/ESP pushed onto the stack is the value it had just before the `PUSHA(D)` instruction started executing.
8. For `POPA`/`POPAD`, the stack item corresponding to SP/ESP is popped off the stack (performing a memory read), but not placed into SP/ESP.
9. The `PUSHFD` and `POPFD` instructions will cause a #GP exception if executed in virtual 8086 mode if IOPL is not 3. The `PUSHF`, `POPF`, `IRET` and `IRETD` instructions will cause a #GP exception if executed in Virtual-8086 mode if IOPL is not 3 and VME is not enabled.
10. If `IRETD` is used to return from kernel mode to user mode (which will entail a CPL change) and the user-mode stack segment indicated by SS is a 16-bit segment, then the `IRETD` instruction will only restore the low 16 bits of the stack pointer (ESP/RSP), with the remaining bits keeping whatever value they had in kernel code before the `IRETD`. This has necessitated complex workarounds on both Linux ("ESPFIX") and Windows. This issue also affects the later 64-bit `IRETQ` instruction.

| Instruction mnemonics | Opcode | Description | Ring |
|---|---|---|---|
| `BT r/m, r` | `0F A3 /r` | Bit Test. Second operand specifies which bit of the first operand to test. The bit to test is copied to EFLAGS.CF. | 3 |
| `BT r/m, imm8` | `0F BA /4 *ib*` |   |   |
| `BTS r/m, r` | `0F AB /r` | Bit Test-and-set. Second operand specifies which bit of the first operand to test and set. |   |
| `BTS r/m, imm8` | `0F BA /5 *ib*` |   |   |
| `BTR r/m, r` | `0F B3 /r` | Bit Test and Reset. Second operand specifies which bit of the first operand to test and clear. |   |
| `BTR r/m, imm8` | `0F BA /6 *ib*` |   |   |
| `BTC r/m, r` | `0F BB /r` | Bit Test and Complement. Second operand specifies which bit of the first operand to test and toggle. |   |
| `BTC r/m, imm8` | `0F BA /7 *ib*` |   |   |
|   |   |   |   |
| `BSF r, r/m` | `NFx 0F BC /r` | Bit scan forward. Returns bit index of lowest set bit in input. | 3 |
| `BSR r, r/m` | `NFx 0F BD /r` | Bit scan reverse. Returns bit index of highest set bit in input. |   |
| `SHLD r/m, r, imm8` | `0F A4 /r *ib*` | Shift Left Double. The operation of `SHLD arg1,arg2,shamt` is: `arg1 := (arg1<<shamt) \| (arg2>>(operand_size - shamt))` |   |
| `SHLD r/m, r, CL` | `0F A5 /r` |   |   |
| `SHRD r/m, r, imm8` | `0F AC /r *ib*` | Shift Right Double. The operation of `SHRD arg1,arg2,shamt` is: `arg1 := (arg1>>shamt) \| (arg2<<(operand_size - shamt))` |   |
| `SHRD r/m, r, CL` | `0F AD /r` |   |   |
|   |   |   |   |
| `MOVZX reg, r/m8` | `0F B6 /r` | Move from 8/16-bit source to 16/32-bit register with zero-extension. | 3 |
| `MOVZX reg, r/m16` | `0F B7 /r` |   |   |
| `MOVSX reg, r/m8` | `0F BE /r` | Move from 8/16-bit source to 16/32/64-bit register with sign-extension. |   |
| `MOVSX reg, r/m16` | `0F BF /r` |   |   |
| `SETcc r/m8` | `0F 9x /0` | Set byte to 1 if condition is satisfied, 0 otherwise. |   |
| `Jcc *rel16*` `Jcc *rel32*` | `0F 8x *cw*` `0F 8x *cd*` | Conditional jump near. Differs from older variants of conditional jumps in that they accept a 16/32-bit offset rather than just an 8-bit offset. |   |
| `IMUL r, r/m` | `0F AF /r` | Two-operand non-widening integer multiply. |   |
|   |   |   |   |
| `FS:` | `64` | Segment-override prefixes for FS and GS segment registers. | 3 |
| `GS:` | `65` |   |   |
| `PUSH FS` | `0F A0` | Push/pop FS and GS segment registers. |   |
| `POP FS` | `0F A1` |   |   |
| `PUSH GS` | `0F A8` |   |   |
| `POP GS` | `0F A9` |   |   |
| `LFS r16, m16&16` `LFS r32, m32&16` | `0F B4 /r` | Load far pointer from memory. Offset part is stored in destination register argument, segment part in FS/GS/SS segment register as indicated by the instruction mnemonic. |   |
| `LGS r16, m16&16` `LGS r32, m32&16` | `0F B5 /r` |   |   |
| `LSS r16, m16&16` `LSS r32, m32&16` | `0F B2 /r` |   |   |
|   |   |   |   |
| `MOV reg,CRx` | `0F 20 /r` | Move from control register to general register. | 0 |
| `MOV CRx,reg` | `0F 22 /r` | Move from general register to control register. Moves to the `CR3` control register are serializing and will flush the TLB. On Pentium and later processors, moves to the `CR0` and `CR4` control registers are also serializing. |   |
| `MOV reg,DRx` | `0F 21 /r` | Move from x86 debug register to general register. |   |
| `MOV DRx,reg` | `0F 23 /r` | Move from general register to x86 debug register. On Pentium and later processors, moves to the DR0-DR7 debug registers are serializing. |   |
| `MOV reg,TRx` | `0F 24 /r` | Move from x86 test register to general register. |   |
| `MOV TRx,reg` | `0F 26 /r` | Move from general register to x86 test register. |   |
|   |   |   |   |
| ICEBP,  INT01,  INT1 | F1 | In-circuit emulation breakpoint. Performs software interrupt #1 if executed when not using in-circuit emulation. | 3 |
| UMOV r/m, r8 | 0F 10 /r | User Move – perform data moves that can access user memory while in In-circuit emulation HALT mode. Performs same operation as `MOV` if executed when not doing in-circuit emulation. |   |
| UMOV r/m, r16/32 | 0F 11 /r |   |   |
| UMOV r8, r/m | 0F 12 /r |   |   |
| UMOV r16/32, r/m | 0F 13 /r |   |   |
| XBTS reg,r/m | 0F A6 /r | Bitfield extract (early 386 only). |   |
| IBTS r/m,reg | 0F A7 /r | Bitfield insert (early 386 only). |   |
| LOADALLD,  LOADALL386 | 0F 07 | Load all CPU registers from a 296-byte data structure starting at ES:EDI, including "hidden" part of segment descriptor registers. | 0 |

1. For the `BT`, `BTS`, `BTR` and `BTC` instructions: If the first argument to the instruction is a register operand and/or the second argument is an immediate, then the bit-index in the second argument is taken modulo operand size (16/32/64, in effect using only the bottom 4, 5 or 6 bits of the index.) If the first argument is a memory operand and the second argument is a register operand, then the bit-index in the second argument is used in full – it is interpreted as a signed bit-index that is used to offset the memory address to use for the bit test.
2. The `BTS`, `BTC` and `BTR` instructions accept the `LOCK` (`F0`) prefix when used with a memory argument – this results in the instruction executing atomically.
3. If the `F3` prefix is used with the `0F BC /r` opcode, then the instruction will execute as `TZCNT` on systems that support the BMI1 extension. `TZCNT` differs from `BSF` in that `TZCNT` but not `BSR` is defined to return operand size if the source operand is zero – for other source operand values, they produce the same result (except for flags).
4. `BSF` and `BSR` set the EFLAGS.ZF flag to 1 if the source argument was all-0s and 0 otherwise.If the source argument was all-0s, then the destination register is left unchanged on AMD processors. It is usually left unchanged on Intel processors as well, but some exceptions exist: On some older Intel 64 processors, the 32-bit forms of the `BSF`/`BSR` instructions will, with an all-0s source, leave the bottom 32 bits of the destination register unchanged but clear the top 32 bits. On 386/486 processors, `BSF`/`BSR` with an all-0s source are documented as returning an undefined value into the destination register — most 386/486 versions leave the destination register unchanged, but some early Intel 486 versions are known to modify it.
5. If the `F3` prefix is used with the `0F BD /r` opcode, then the instruction will execute as `LZCNT` on systems that support the ABM or LZCNT extensions. `LZCNT` produces a different result from `BSR` for most input values.
6. For `SHLD` and `SHRD`, the shift-amount is masked – the bottom 5 bits are used for 16/32-bit operand size and 6 bits for 64-bit operand size. `SHLD` and `SHRD` with 16-bit arguments and a shift-amount greater than 16 produce undefined results. (Actual results differ between different Intel CPUs, with at least three different behaviors known.)
7. The condition codes supported for the `SET**cc**` and `J**cc** near` instructions (opcodes `0F 9**x** /0` and `0F 8**x**` respectively, with the **x** nibble specifying the condition) are: xccCondition (EFLAGS) 0OOF=1: "Overflow" 1NOOF=0: "Not Overflow" 2C,B,NAECF=1: "Carry", "Below", "Not Above or Equal" 3NC,NB,AECF=0: "Not Carry", "Not Below", "Above or Equal" 4Z,EZF=1: "Zero", "Equal" 5NZ,NEZF=0: "Not Zero", "Not Equal" 6NA,BE(CF=1 or ZF=1): "Not Above", "Below or Equal" 7A,NBE(CF=0 and ZF=0): "Above", "Not Below or Equal" 8SSF=1: "Sign" 9NSSF=0: "Not Sign" AP,PEPF=1: "Parity", "Parity Even" BNP,POPF=0: "Not Parity", "Parity Odd" CL,NGESF≠OF: "Less", "Not Greater Or Equal" DNL,GESF=OF: "Not Less", "Greater Or Equal" ELE,NG(ZF=1 or SF≠OF): "Less or Equal", "Not Greater" FNLE,G(ZF=0 and SF=OF): "Not Less or Equal", "Greater"
8. For `SETcc`, while the opcode is commonly specified as /0 – implying that bits 5:3 of the instruction's ModR/M byte should be 000 – modern x86 processors (Pentium and later) ignore bits 5:3 and will execute the instruction as `SETcc` regardless of the contents of these bits.
9. For `LFS`, `LGS` and `LSS`, the size of the offset part of the far pointer is given by operand size – the size of the segment part is always 16 bits. In 64-bit mode, using the `REX.W` prefix with these instructions will cause them to load a far pointer with a 64-bit offset on Intel but not AMD processors.
10. For `MOV` to/from the `CRx`, `DRx` and `TRx` registers, the reg part of the ModR/M byte is used to indicate `CRx/DRx/TRx` register and r/m part the general-register. Uniquely for the `MOV CRx/DRx/TRx` opcodes, the top two bits of the ModR/M byte is ignored – these opcodes are decoded and executed as if the top two bits of the ModR/M byte are `11b`.
11. For moves to/from the `CRx` and `DRx` registers, the operand size is always 64 bits in 64-bit mode and 32 bits otherwise.
12. On processors that support global pages (Pentium and later), global page table entries will not be flushed by a `MOV` to `CR3` − instead, these entries can be flushed by toggling the CR4.PGE bit.On processors that support PCIDs, writing to `CR3` while PCIDs are enabled will only flush TLB entries belonging to the PCID specified in bits 11:0 of the value written to `CR3`. Flushing pages belonging to other PCIDs can instead be done by toggling the CR4.PGE bit, clearing the CR4.PCIDE bit, or using the `INVPCID` instruction.In 64-bit mode, TLB flushing can be suppressed by setting bit 63 of the value written to `CR3` to 1.
13. On processors prior to Pentium, moves to `CR0` would not serialize the instruction stream – for this reason, it is usually required to perform a jump (`JMP` or `CALL`) immediately after a `MOV` to `CR0` if such a `MOV` is used to enable/disable protected mode and/or memory paging. This can be either a near or a far jump - either will work for flushing the instruction queue, but a far jump is required in order to update access rights for the CS segment.When the CR0.PG bit is toggled (turning paging on or off), its effect on instruction fetch is immediate on Pentium Pro and later processors, however, on 386/486/Pentium processors, the effect is delayed by at least 1 instruction — this difference has been know to cause compatibility problems, e.g. with SCO UNIX 3.2v4.0.`MOV` to `CR2` is architecturally listed as serializing, but has been reported to be non-serializing on at least some Intel Core-i7 processors.`MOV` to `CR8` (introduced with x86-64) is serializing on AMD but not Intel processors.
14. The `MOV TRx` instructions were discontinued from Pentium onwards.
15. The `INT1`/`ICEBP` (`F1`) instruction is present on all known Intel x86 processors from the 80386 onwards, but only fully documented for Intel processors from the May 2018 release of the Intel SDM (rev 067) onwards. Before this release, mention of the instruction in Intel material was sporadic, e.g. AP-526 rev 001. For AMD processors, the instruction has been documented since 2002.
16. The operation of the `F1`(`ICEBP`) opcode differs from the operation of the regular software interrupt opcode `CD 01` in several ways:In protected mode, `CD 01` will check CPL against the interrupt descriptor's DPL field as an access-rights check, while `F1` will not.In virtual-8086 mode, `CD 01` will also check CPL against IOPL as an access-rights check, while `F1` will not.In virtual-8086 mode with VME enabled, interrupt redirection is supported for `CD 01` but not `F1`.
17. The UMOV instruction is present on 386 and 486 processors only.
18. The `XBTS` and `IBTS` instructions were discontinued with the B1 stepping of 80386. They have been used by software mainly for detection of the buggy B0 stepping of the 80386. Microsoft Windows (v2.01 and later) will attempt to run the `XBTS` instruction as part of its CPU detection if `CPUID` is not present, and will refuse to boot if `XBTS` is found to be working.
19. For `XBTS` and `IBTS`, the r/m argument represents the data to extract/insert a bitfield from/to, the reg argument the bitfield to be inserted/extracted, AX/EAX a bit-offset and CL a bitfield length.
20. Undocumented, 80386 only.

#### Added with 80486

| Instruction | Opcode | Description | Ring |
|---|---|---|---|
| `BSWAP r32` | `0F C8+r` | Byte Order Swap. Usually used to convert between big-endian and little-endian data representations. For 32-bit registers, the operation performed is:r = (r << 24) \| ((r << 8) & 0x00FF0000) \| ((r >> 8) & 0x0000FF00) \| (r >> 24); Using `BSWAP` with a 16-bit register argument produces an undefined result. | 3 |
| `CMPXCHG r/m8,r8` | `0F B0 /r` | Compare and Exchange. If accumulator (AL/AX/EAX/RAX) compares equal to first operand, then `EFLAGS.ZF` is set to 1 and the first operand is overwritten with the second operand. Otherwise, `EFLAGS.ZF` is set to 0, and first operand is copied into the accumulator. Instruction atomic only if used with `LOCK` prefix. |   |
| `CMPXCHG r/m,r16` `CMPXCHG r/m,r32` | `0F B1 /r` |   |   |
| `XADD r/m,r8` | `0F C0 /r` | eXchange and ADD. Exchanges the first operand with the second operand, then stores the sum of the two values into the destination operand. Instruction atomic only if used with `LOCK` prefix. |   |
| `XADD r/m,r16` `XADD r/m,r32` | `0F C1 /r` |   |   |
| `INVLPG m8` | `0F 01 /7` | Invalidate the TLB entries that would be used for the 1-byte memory operand. Instruction is serializing. | 0 |
| `WBINVD` | `NFx 0F 09` | Write Back and Invalidate Cache. Writes back all modified cache lines in the processor's internal cache to main memory and invalidates the internal caches. |   |
| `INVD` | `0F 08` | Invalidate Internal Caches. Modified data in the cache are not written back to memory, potentially causing data loss. | 0 |

1. Using `BSWAP` with 16-bit registers is not disallowed per se (it will execute without producing an #UD or other exceptions) but is documented to produce undefined results – it is reported to produce various different results on 486, 586, and Bochs/QEMU.
2. On Intel 80486 stepping A, the `CMPXCHG` instruction uses a different encoding - `0F A6 /r` for 8-bit variant, `0F A7 /r` for 16/32-bit variant. The `0F B0/B1` encodings are used on 80486 stepping B and later.
3. The `CMPXCHG` instruction sets `EFLAGS` in the same way as a `CMP` instruction that uses the accumulator (AL/AX/EAX/RAX) as its first argument would do.
4. `INVLPG` executes as no-operation if the m8 argument is invalid (e.g. unmapped page or non-canonical address). `INVLPG` can be used to invalidate TLB entries for individual global pages.
5. If the `F3` prefix is used with the `0F 09` opcode, then the instruction will execute as `WBNOINVD` on processors that support the WBNOINVD extension – this will not invalidate the cache.
6. The `INVD` and `WBINVD` instructions will invalidate all cache lines in the CPU's L1 caches. It is implementation-defined whether they will invalidate the content of L2/L3 caches as well. The `INVD` and `WBINVD` instructions will not prevent cache prefetching from taking place while they're operating — if there is a need to guarantee that caches are empty, then it is necessary to set `CR0.CD` to 1 before invoking either of these instructions. (If the cache is shared between multiple logical processors, then emptying the cache requires all the logical processors that share the cache to have their `CR0.CD` bit set to 1 before `INVD` or `WBINVD` is invoked.)
7. The `INVD` and `WBINVD` instructions are serializing – on some processors, they may block interrupts until completion as well.
8. There are several circumstances under which the `INVD` instruction cannot be executed even under ring 0: On processors that support Intel SGX, if the PRM (Processor Reserved Memory) has been set up by using the PRMRRs (PRM range registers), then the `INVD` instruction is not permitted and will cause a #GP(0) exception. On processors that support Intel TDX, if the SEAM (SEcure Arbitration Mode) has been set up, `INVD` will cause #GP(0). On some newer Intel processors (Meteor Lake/Arrow Lake and later), trying to execute `INVD` when bit 0 of the `MSR_BIOS_DONE` MSR is set will result in #GP(0) — this effectively prevents all non-BIOS use of this instruction. Under Intel VT-x virtualization, the `INVD` instruction will cause a mandatory #VMEXIT.

#### Added in P5/P6-class processors

Integer/system instructions that were not present in the basic 80486 instruction set, but were added in various x86 processors prior to the introduction of SSE. (Discontinued instructions are not included.)
