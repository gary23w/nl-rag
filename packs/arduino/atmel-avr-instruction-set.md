---
title: "Atmel AVR instruction set"
source: https://en.wikipedia.org/wiki/Atmel_AVR_instruction_set
domain: arduino
license: CC-BY-SA-4.0
tags: arduino, arduino sketch, arduino uno, arduino ide, atmega
fetched: 2026-07-02
---

# Atmel AVR instruction set

The **Atmel AVR instruction set** is the machine language for the Atmel AVR, a modified Harvard architecture 8-bit RISC single chip microcontroller which was developed by Atmel in 1996. Atmel was acquired by Microchip Technology in 2016. The AVR was one of the first microcontroller families to use on-chip flash memory for program storage.

## Processor registers

There are 32 general-purpose 8-bit registers, R0–R31. All arithmetic and logic operations operate on those registers; only load and store instructions access RAM.

A limited number of instructions operate on 16-bit register pairs. The lower-numbered register of the pair holds the least significant bits and must be even-numbered. The last three register pairs are used as pointer registers for memory addressing. They are known as X (R27:R26), Y (R29:R28) and Z (R31:R30). Postincrement and predecrement addressing modes are supported on all three. Y and Z also support a six-bit positive displacement.

Instructions which allow an immediate value are limited to registers R16–R31 (8-bit operations) or to register pairs R25:R24–R31:R30 (16-bit operations ADIW and SBIW). Some variants of the MUL operation are limited to eight registers, R16 through R23.

### Special purpose registers

In addition to these 32 general-purpose registers, the CPU has a few special-purpose registers:

- PC: 16- or 22-bit program counter
- SP: 8- or 16-bit stack pointer
- SREG: 8-bit status register
- RAMPX, RAMPY, RAMPZ, RAMPD and EIND: 8-bit segment registers that are prepended to 16-bit addresses in order to form 24-bit addresses; only available in parts with large address spaces.

### Status register

The status register bits are:

2. C Carry flag. This is a borrow flag on subtracts.
3. Z Zero flag. Set when an arithmetic result is zero, and cleared when it is non-zero.
4. N Negative flag. Set to a copy of the most significant bit of an arithmetic result.
5. V Overflow flag. Set in case of two's complement overflow.
6. S Sign flag. Unique to AVR, this is always N⊕V, and shows the true sign of a comparison.
7. H Half-carry flag. This is an internal carry from additions and is used to support BCD arithmetic.
8. T Bit copy. Special bit load and bit store instructions use this bit.
9. I Interrupt flag. Set when interrupts are enabled.

There are two special cases which exist to facilitate multi-byte arithmetic:

- The `INC` and `DEC` instructions do *not* modify the carry flag, so they may be used to loop over arbitrary-precision arithmetic operands.
- The `CPC`, `SBC` and `SBCI` (compare/subtract with carry) instructions do *not* set the Z flag when the result is zero, but only clear it if the result is non-zero. For *fixed* precision multi-byte comparisons, implemented with an unrolled `CP; CPC; CPC; CPC` sequence, this produces a zero flag which is set only if the *entire* difference is zero.

## Addressing

The following address spaces are available:

- The general purpose registers are addressed by their numbers (0–31), although the full 5-bit number is not stored in instructions that can only operate on a subset of those registers.
- I/O registers have a dedicated 6-bit address space, the lower half of which is bit-addressable; some parts have I/O registers outside this address space, which are called "extended I/O" and are only accessible as memory-mapped I/O in the data address space.
- The data address space maps the 32 general-purpose registers, all the I/O registers (including those also accessible through the I/O address space), and the RAM; it can be addressed either directly or indirectly through the X, Y and Z pointer registers, prepended if necessary by RAMPX, RAMPY and RAMPZ respectively.
- Program memory (flash) has a separate address space, addressed as 16-bit words for the purpose of fetching instructions
- For the purpose of fetching constant data, program memory is addressed bytewise through the Z pointer register, prepended if necessary by RAMPZ.
- The EEPROM is memory-mapped in some devices; in others, it is not directly addressable and is instead accessed through address, data and control I/O registers.
- The general purpose registers, the status register and some I/O registers are bit-addressable, with bit 0 being the least significant and bit 7 the most significant.

The first 64 I/O registers are accessible through both the I/O and the data address space. They have therefore two different addresses. These are usually written as "0x00 (0x20)" through "0x3F (0x5F)", where the first item is the I/O address and the second, in parentheses, the data address.

The special-purpose CPU registers, with the exception of PC, can be accessed as I/O registers. Some registers (RAMPX, RAMPY) may not be present on machines with less than 64 KiB of addressable memory.

| Register | I/O address | Data address |
|---|---|---|
| SREG | 0x3F | 0x5F |
| SP | 0x3E:0x3D | 0x5E:0x5D |
| EIND | 0x3C | 0x5C |
| RAMPZ | 0x3B | 0x5B |
| RAMPY | 0x3A | 0x5A |
| RAMPX | 0x39 | 0x59 |
| RAMPD | 0x38 | 0x58 |

A typical ATmega memory map may look like:

| Data address | I/O address | Contents |
|---|---|---|
| 0x0000 – 0x001F |   | Registers R0 – R31 |
| 0x0020 – 0x003F | 0x00 – 0x1F | I/O registers (bit-addressable) |
| 0x0040 – 0x005F | 0x20 – 0x3F | I/O registers (not bit-addressable) |
| 0x0060 – 0x00FF |   | Extended I/O registers (memory-mapped I/O only) |
| 0x0100 – RAMEND |   | Internal SRAM |

where RAMEND is the last RAM address. In parts lacking extended I/O the RAM would start at 0x0060.

## Instruction timing

Arithmetic operations work on registers R0–R31 but not directly on RAM and take one clock cycle, except for multiplication and word-wide addition (ADIW and SBIW) which take two cycles.

RAM and I/O space can be accessed only by copying to or from registers. Indirect access (including optional postincrement, predecrement or constant displacement) is possible through registers X, Y, and Z. All accesses to RAM takes two clock cycles. Moving between registers and I/O is one cycle. Moving eight or sixteen bit data between registers or constant to register is also one cycle. Reading program memory (LPM) takes three cycles.

## Instruction list

Instructions are one 16-bit long word, save for those including a 16-bit or 22-bit address, which take two words.

There are two types of conditional branches: jumps to address and skips. Conditional branches (BRxx) can test an ALU flag and jump to specified address. Skips (SBxx) test an arbitrary bit in a register or I/O and skip the next instruction if the test was true.

In the following:

- Rd and Rr are registers in the range R0–R31
- Rdh and Rrh are registers in the range R16–R31 (high half)
- Rdq and Rrq are registers in the range R16–R23 (one quarter of the register file)
- Rp is a register pair R25:R24, R27:R26 (X), R29:R28 (Y) or R31:R30 (Z)
- XYZ is a pointer register, X or Y or Z
- XYZ+ is a pointer register, X or Y or Z, postincremented
- -XYZ is a pointer register, X or Y or Z, predecremented
- YZ is a pointer register, either Y or Z
- Z+ is pointer register Z, postincremented
- s is a bit number in the status register (0 = C, 1 = Z, etc., see the list above)
- b is a bit number in a general-purpose or I/O register (0 = least significant, 7 = most significant)
- K6 is a 6-bit immediate *unsigned* constant (range: 0–63)
- K8 is an 8-bit immediate constant; since it is used only in 8-bit operations, its signedness is irrelevant
- IO5 is a 5-bit I/O address covering the bit-addressable part of the I/O address space, i.e. the lower half (range: 0–31)
- IO6 is a 6-bit I/O address covering the full I/O address space (range: 0–63)
- D16 is a 16-bit data address covering 64 KiB; in parts with more than 64 KiB data space, the contents of the RAMPD segment register is prepended
- P22 is a 22-bit program address covering 222 16-bit words (i.e. 8 MiB)
- S7 and S12 are 7-bit and 12-bit *signed* displacements, in units of words, relative to the program address stored in the program counter

| Arithmetic | Bit & Others | Transfer | Jump |
|---|---|---|---|
| ADD Rd, Rr ADC Rd, Rr ADIW Rp+1:Rp, K6 SUB Rd, Rr SUBI Rdh, K8 SBC Rd, Rr SBCI Rdh, K8 SBIW Rp+1:Rp, K6 INC Rd DEC Rd AND Rd, Rr ANDI Rdh, K8 OR Rd, Rr ORI Rdh, K8 COM Rd NEG Rd CP Rd, Rr CPC Rd, Rr CPI Rdh, K8 SWAP Rd LSR Rd ROR Rd ASR Rd MUL Rd, Rr MULS Rdh, Rrh MULSU Rdq, Rrq FMUL Rdq, Rrq FMULS Rdq, Rrq FMULSU Rdq, Rrq | BSET s BCLR s SBI IO5, b CBI IO5, b BST Rd, b BLD Rd, b NOP BREAK SLEEP WDR | MOV Rd, Rr MOVW Rd+1:Rd, Rr+1:Rr IN Rd, IO6 OUT IO6, Rr PUSH Rr POP Rr LDI Rdh, K8 LDS Rd, D16 LD Rd, X LDD Rd, YZ+K6 LD Rd, -XYZ LD Rd, XYZ+ STS D16, Rr ST X, Rr STD YZ+K6, Rr ST -XYZ, Rr ST XYZ+, Rr LPM LPM Rd, Z LPM Rd, Z+ ELPM ELPM Rd, Z ELPM Rd, Z+ SPM | RJMP S12 IJMP EIJMP JMP P22 |
| Call |   |   |   |
| RCALL S12 ICALL EICALL CALL P22 RET RETI |   |   |   |
| Branch |   |   |   |
| CPSE Rd, Rr SBRC Rr, b SBRS Rr, b SBIC IO5, b SBIS IO5, b BRBC s, S7 BRBS s, S7 |   |   |   |

## Instruction set inheritance

Not all instructions are implemented in all Atmel AVR controllers. This is the case of the instructions performing multiplications, extended loads/jumps/calls, long jumps, and power control.

The optional instructions may be grouped into three categories:

- core cpu (computation) features, added on more capable CPU cores
- memory addressing features, added on all models with memory large enough to require them
- optional features, a few peripherals that may or may not be present on a particular model.

While higher-end processors tend to have both more capable cores and more memory, the presence of one does not guarantee the presence of the other.

### Core CPU instructions

Beginning with the original "classic" core, enhancements are organized into the following levels, each of which includes all the preceding:

1. The "Classic" core has only the zero-operand form of the `LPM` instruction, which is equivalent to `LPM r0,Z`.
2. "Classic plus" adds the `MOVW` instruction for moving register pairs, and the more general form of the LPM instruction (`LPM Rd,Z` and `LPM Rd,Z+`) which permit an arbitrary destination register and auto-increment of the Z pointer.
3. "Enhanced" cores add the multiply instructions.
4. The XMEGA cores do not add new instructions *per se*, but make some significant changes:
  - The memory map is reorganized, eliminating memory-mapping of the processor register file (so I/O ports begin at RAM address 0) and expanding the I/O port range. Now the first 4K is special function registers, the second 4K is data flash, and normal RAM begins at 8K.
  - It is not necessary to explicitly disable interrupts before adjusting the stack pointer registers (SPL and SPH); any write to SPL automatically disables interrupts for 4 clock cycles to give time for SPH to be updated.
  - Other multi-byte registers are provided with shadow registers to enable atomic read and write. When the lowest-order byte is read, the higher-order bytes are copied to the shadow registers, so reading them later produces a snapshot of the register at the time of the first read. Writes to low-order bytes are buffered until the highest-order byte is written, upon which the entire multi-byte register is updated atomically.
5. Later XMEGA cores (specifically, the B, C, and AU models such as the ATxmega16A4U, but *not* the earlier A, D and E models such as the ATxmega16D4) add four atomic read-modify-write instructions: exchange (`XCH`), load-and-set, load-and-clear, and load-and-toggle. These help coordinate with direct memory access peripherals, notably a USB controller.

Less capable than the "classic" CPU cores are two subsets: the "AVR1" core, and the "AVR tiny". Confusingly, "ATtiny" branded processors have a variety of cores, including AVR1 (ATtiny11, ATtiny28), classic (ATtiny22, ATtiny26), classic+ (ATtiny24) and AVRtiny (ATtiny20, ATtiny40).

The AVR1 subset was not popular and no new models have been introduced since 2000. It omits all RAM except for the 32 registers mapped at address 0–31 and the I/O ports at addresses 32–95. The stack is replaced by a 3-level hardware stack, and the `PUSH` and `POP` instructions are deleted. All 16-bit operations are deleted, as are `IJMP`, `ICALL`, and all load and store addressing modes except indirect via Z.

A second, more successful attempt to subset the AVR instruction set is the "AVR tiny" core.

The most significant change is that the AVRtiny core omits registers R0–R15. The registers are also not memory-mapped, with I/O ports from 0–63 and general-purpose RAM beginning at address 64. The 16-bit arithmetic operations (`ADIW`, `SBIW`) are omitted, as are the load/store with displacement addressing modes (`Y+d`, `Z+d`), but the predecrement and postincrement addressing modes are retained. The `LPM` instruction is omitted; instead program ROM is mapped to the data address space and may be accessed with normal load instructions.

Finally, the AVRtiny core deletes the 2-word `LDS` and `STS` instructions for direct RAM addressing, and instead uses the opcode space previously assigned to the load/store with displacement instructions for new 1-word `LDS` and `STS` instructions which can access the first 128 locations of general-purpose RAM, addresses 0x40 to 0xBF. (The `IN` and `OUT` instructions provide direct access to I/O space from 0 to 0x3F.)

### Memory addressing instructions

The smallest cores have ≤256 bytes of data address space (meaning ≤128 bytes of RAM after I/O ports and other reserved addresses are removed) and ≤8192 bytes (8 KiB) of program ROM. These have only an 8-bit stack pointer (in SPL), and only support the 12-bit relative jump/call instructions `RJMP`/`RCALL`. (Because the AVR program counter counts 16-bit words, not bytes, a 12-bit offset is sufficient to address 213 bytes of ROM.)

Additional memory addressing capabilities are present as required to access available resources:

1. Models with >256 bytes of data address space (≥256 bytes of RAM) have a 16-bit stack pointer, with the high half in the SPH register.
2. Models with >8 KiB of ROM add the 2-word (22-bit) `JUMP` and `CALL` instructions. (Some early models suffer an erratum if a skip instruction is followed by a 2-word instruction.)
3. Models with >64 KiB of ROM add the `ELPM` instruction and corresponding RAMPZ register. `LPM` instructions zero-extend the ROM address in Z; `ELPM` instructions prepend the RAMPZ register for high bits. This is not the same thing as the more general `LPM` instruction; there exist "classic" models with only the zero-operand form of `ELPM` (ATmega103 and at43usb320). When auto-increment is available (most models), it updates the entire 24-bit address including RAMPZ.
4. (Rare) models with >128 KiB of ROM have a 3-byte program counter. Subroutine calls and returns use an additional byte of stack space, there is a new EIND register to provide additional high bits for indirect jumps and calls, and there are new extended instructions `EIJMP` and `EICALL` which use EIND:Z as the destination address. (The previous `IJMP` and `ICALL` instructions use zero-extended Z.)
5. (Rare) models with >64 KiB of RAM address space extend the 16-bit RAM addressing limits with RAMPX, RAMPY, RAMPZ and RAMPD registers. These provide additional high bits for addressing modes which use the X, Y, or Z register pairs, respectively, or the direct addressing instructions `LDS`/`STS`. Unlike ROM access, there are no distinct "extended" instructions; instead the RAMP registers are used unconditionally.

### Optional feature instructions

Three instructions are present only on models which have the corresponding hardware facility

- `SPM` for storing to flash ROM, is present only on processors with flash ROM (most of them)
- `BREAK` for invoking the on-chip debugger, is omitted on some small models without on-chip debugger support
- `DES` for performing Data Encryption Standard rounds, is present on XMEGA models with DES accelerator support

Architectures other than AVR1 are named according to avr-libc conventions.

| Family | Members | Arithmetic | Branches | Transfers | Bit-Wise |
|---|---|---|---|---|---|
| Minimal AVR1 Core | AT90S1200ATtiny11ATtiny12ATtiny15ATtiny28 | ADD (LSL)ADC (ROL)SUBSUBISBCSBCIAND (TST)ANDI (CBR)ORORI (SBR)EOR (CLR)COMNEGINCDEC | RJMPRCALLRETRETICPSECPCPCCPISBRCSBRSSBICSBISBRBS (BRCS,BRLO,BREQ,BRMI,BRVS,BRLT,BRHS,BRTS,BRIE)BRBC (BRCC,BRSH,BRNE,BRPL,BRVC,BRGE,BRHC,BRTC,BRID) | LDSTMOVLDI (SER)INOUTLPM (not in AT90S1200) | SBICBILSRRORASRSWAPBSET (SEC, SEZ, SEN, SEV, SES, SEH, SET, SEI)BCLR (CLC, CLZ, CLN, CLV, CLS, CLH, CLT, CLI)BSTBLDNOPSLEEPWDR |
| Classic Core up to 8K Program Space ("AVR2") | AT90S2313AT90S2323ATtiny22AT90S2333AT90S2343AT90S4414AT90S4433AT90S4434AT90S8515AT90C8534AT90S8535ATtiny26 | new instructions: ADIWSBIW | new instructions: IJMPICALL | new instructions: LD (now 9 modes)LDDLDSST (9 modes)STDSTSPUSHPOP | (nothing new) |
| AVR2, with MOVW and LPM instructions ("AVR2.5") | ATa5272 ATtiny13/a ATtiny2313/a ATtiny24/a ATtiny25 ATtiny261/a ATtiny4313 ATtiny43u ATtiny44/a ATtiny45 ATtiny461/a ATtiny48 ATtiny828 ATtiny84/a ATtiny85 ATtiny861/a ATtiny87 ATtiny88 | (nothing new) | (nothing new) | new instructions: MOVW LPM (Rx, Z[+]) SPM | (nothing new) |
| Classic Core with up to 128K ("AVR3") | ATmega103ATmega603AT43USB320AT76C711 | (nothing new) | new instructions:JMPCALL | new instructions:ELPM (in "AVR3.1") | (nothing new) |
| Enhanced Core with up to 8K ("AVR4") | ATmega8ATmega83ATmega85ATmega8515 | new instructions:MULMULSMULSUFMULFMULSFMULSU | (nothing new) | new instructions:MOVWLPM (3 modes)SPM | (nothing new) |
| Enhanced Core with up to 128K ("AVR5", "AVR5.1") | ATmega16ATmega161ATmega163ATmega32ATmega323ATmega64ATmega128AT43USB355AT94 (FPSLIC)AT90CAN seriesAT90PWM seriesATmega48ATmega88ATmega168ATmega162ATmega164ATmega324ATmega328ATmega644ATmega165ATmega169ATmega325ATmega3250ATmega645ATmega6450ATmega406 | (nothing new) | new instruction: ELPMX ("AVR5.1") | (nothing new) | new instructions:BREAK |
| Enhanced Core with up to 4M ("AVR5" and "AVR6") | ATmega640ATmega1280ATmega1281ATmega2560ATmega2561 | (nothing new) | new instructions:EIJMPEICALL | (nothing new) | (nothing new) |
| XMEGA Core ("avrxmega" 2-6) | ATxmega series | new instructions:DES | (nothing new) | new instructions (from second revision silicon - AU,B,C parts) XCHLASLACLAT | (nothing new) |
| Reduced AVRtiny Core ("avrtiny10") | ATtiny40ATtiny20ATtiny10ATtiny9ATtiny5ATtiny4 | (Identical to minimal core, except for reduced CPU register set**a** ) | (Identical to classic core with up to 8K, except for reduced CPU register set**a** ) | Identical to classic core with up to 8K, with the following exceptions:LPM(removed)LDD(removed)STD(removed)LD(also accesses program memory)LDS STS(access is limited to the first 128 bytes of SRAM)Reduced CPU register set**a** | (Identical to enhanced core with up to 128K, except for reduced CPU register set**a** ) |

**a** Reduced register set is limited to R16 through R31.

## Instruction encoding

Bit assignments:

- rrrrr / ddddd = Source/destination register
- rrrr / dddd = Source/destination register (R16–R31)
- rrr / ddd = Source/destination register (R16–R23)
- RRRR / DDDD = Source/destination register pair (R1:R0–R31:R30)
- pp = Register pair, W, X, Y or Z
- y = Y/Z register pair bit (0=Z, 1=Y)
- u = FMULS(U) unsigned bit (0=FMULS signed, 1=FMULSU unsigned)
- s = Store/load bit (0=LD Rd,mem, 1=ST mem,Rd)
- c = Call/jump (0=jump, 1=call)
- cy = With carry (0=without carry, 1=with carry)
- e = Extend indirect jump/call address with EIND (0=0:Z, 1=EIND:Z)
- q = Extend program memory address with RAMPZ (0=0:Z, 1=RAMPZ:Z)
- aaaaaa = I/O space address
- aaaaa = I/O space address (first 32 only)
- bbb = Bit number (0–7)
- B = Bit value (0 or 1)
- kkkk = 4-bit unsigned constant (DES opcode)
- kkkkkk = 6-bit unsigned constant
- KKKKKKKK = 8-bit constant

The Atmel AVR uses many split fields, where bits are not contiguous in the instruction word. The most commonly encountered is the 5-bit source register field in bits 9 and 3–0. The most extreme example is the load/store with offset instructions, which break a 6-bit offset into three pieces.

Atmel AVR instruction set overview

1

5

1

4

1

3

1

2

1

1

1

0

9

8

7

6

5

4

3

2

1

0

Instruction

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

NOP

0

0

0

0

0

0

0

1

D D D D

R R R R

MOVW Rd,Rr Move register pair

0

0

0

0

0

0

1

0

d d d d

r r r r

MULS Rd,Rr

0

0

0

0

0

0

1

1

0

d d d

0

r r r

MULSU Rd,Rr

0

0

0

0

0

0

1

1

0

d d d

1

r r r

FMUL Rd,Rr

0

0

0

0

0

0

1

1

1

d d d

u

r r r

FMULS(U) Rd,Rr

0

0

opcode

r

d d d d d

r r r r

Two-operand instructions

0

0

0

c̅y̅

0

1

r

d d d d d

r r r r

CPC/CP Rd,Rr

0

0

0

c̅y̅

1

0

r

d d d d d

r r r r

SBC/SUB Rd,Rr

0

0

0

cy

1

1

r

d d d d d

r r r r

ADD/ADC Rd,Rr (LSL/ROL Rd when Rd=Rr)

0

0

0

1

0

0

r

d d d d d

r r r r

CPSE Rd,Rr

0

0

1

0

0

0

r

d d d d d

r r r r

AND Rd,Rr

0

0

1

0

0

1

r

d d d d d

r r r r

EOR Rd,Rr

0

0

1

0

1

0

r

d d d d d

r r r r

OR Rd,Rr

0

0

1

0

1

1

r

d d d d d

r r r r

MOV Rd,Rr

0

0

1

1

K K K K

d d d d

K K K K

CPI Rd,K

0

1

opc

K K K K

d d d d

K K K K

Register-immediate operations

0

1

0

c̅y̅

K K K K

d d d d

K K K K

SBCI/SUBI Rd,K

0

1

1

0

K K K K

d d d d

K K K K

ORI Rd,K

SBR Rd,K

0

1

1

1

K K K K

d d d d

K K K K

ANDI Rd,K

CBR Rd,K

1

0

k

0

k k

s

d d d d d

y

k k k

LDD/STD Rd through Z+k or Y+k

1

0

0

1

0

0

s

d d d d d

opcode

Load/store operations

1

0

0

1

0

0

s

d d d d d

0

0

0

0

LDS Rd,i/STS i,Rd

16-Bit immediate SRAM address i

1

0

0

1

0

0

s

d d d d d

1

0

0

0

(reserved)

1

0

0

1

0

0

s

d d d d d

y

0

0

1

LD/ST Rd through Z+/Y+

1

0

0

1

0

0

s

d d d d d

y

0

1

0

LD/ST Rd through

−

Z/

−

Y

1

0

0

1

0

0

s

d d d d d

y

0

1

1

(reserved)

1

0

0

1

0

0

0

d d d d d

0

1

q

0

LPM/ELPM Rd,Z

1

0

0

1

0

0

0

d d d d d

0

1

q

1

LPM/ELPM Rd,Z+

1

0

0

1

0

0

1

d d d d d

0

1

0

0

XCH Z,Rd

1

0

0

1

0

0

1

d d d d d

0

1

0

1

LAS Z,Rd

1

0

0

1

0

0

1

d d d d d

0

1

1

0

LAC Z,Rd

1

0

0

1

0

0

1

d d d d d

0

1

1

1

LAT Z,Rd

1

0

0

1

0

0

s

d d d d d

1

1

0

0

LD/ST Rd through X

1

0

0

1

0

0

s

d d d d d

1

1

0

1

LD/ST Rd through X+

1

0

0

1

0

0

s

d d d d d

1

1

1

0

LD/ST Rd through

−

X

1

0

0

1

0

0

s

d d d d d

1

1

1

1

POP/PUSH Rd

1

0

0

1

0

1

0

d d d d d

0

opcode

One-operand instructions:

1

0

0

1

0

1

0

d d d d d

0

0

0

0

COM Rd

1

0

0

1

0

1

0

d d d d d

0

0

0

1

NEG Rd

1

0

0

1

0

1

0

d d d d d

0

0

1

0

SWAP Rd

1

0

0

1

0

1

0

d d d d d

0

0

1

1

INC Rd

1

0

0

1

0

1

0

d d d d d

0

1

0

0

(reserved)

1

0

0

1

0

1

0

d d d d d

0

1

0

1

ASR Rd

1

0

0

1

0

1

0

d d d d d

0

1

1

0

LSR Rd

1

0

0

1

0

1

0

d d d d d

0

1

1

1

ROR Rd

1

0

0

1

0

1

0

0

B̅

b b b

1

0

0

0

SEx/CLx Status register clear/set bit

1

0

0

1

0

1

0

1

opcode

1

0

0

0

Zero-operand instructions

1

0

0

1

0

1

0

1

0

0

0

0

1

0

0

0

RET

1

0

0

1

0

1

0

1

0

0

0

1

1

0

0

0

RETI

1

0

0

1

0

1

0

1

0

≠ 00

x

1

0

0

0

(reserved)

1

0

0

1

0

1

0

1

1

0

0

0

1

0

0

0

SLEEP

1

0

0

1

0

1

0

1

1

0

0

1

1

0

0

0

BREAK

1

0

0

1

0

1

0

1

1

0

1

0

1

0

0

0

WDR

1

0

0

1

0

1

0

1

1

0

1

1

1

0

0

0

(reserved)

1

0

0

1

0

1

0

1

1

1

0

q

1

0

0

0

LPM/ELPM

1

0

0

1

0

1

0

1

1

1

1

0

1

0

0

0

SPM

1

0

0

1

0

1

0

1

1

1

1

1

1

0

0

0

SPM Z+

1

0

0

1

0

1

0

c

0

0

0

e

1

0

0

1

Indirect jump/call to Z or EIND:Z

1

0

0

1

0

1

0

c

≠ 000

e

1

0

0

1

(reserved)

1

0

0

1

0

1

0

d d d d d

1

0

1

0

DEC Rd

1

0

0

1

0

1

0

0

k k k k

1

0

1

1

DES round k

1

0

0

1

0

1

0

k k k k k

1

1

c

k

JMP/CALL abs22

k k k k k k k k k k k k k k k k

1

0

0

1

0

1

1

0

k k

p p

k k k k

ADIW Rp,uimm6

1

0

0

1

0

1

1

1

k k

p p

k k k k

SBIW Rp,uimm6

1

0

0

1

1

0

B

0

a a a a a

b b b

CBI/SBI a,b (clear/set I/O bit)

1

0

0

1

1

0

B

1

a a a a a

b b b

SBIC/SBIS a,b (I/O bit test)

1

0

0

1

1

1

r

d d d d d

r r r r

MUL, unsigned: R1:R0 = Rr × Rd

1

0

1

1

s

a a

d d d d d

a a a a

IN/OUT to I/O space

1

1

0

c

12 bit signed offset

RJMP/RCALL to PC + simm12

1

1

1

0

K K K K

d d d d

K K K K

LDI Rd,K

1

1

1

1

0

B̅

7-bit signed offset

b b b

Conditional branch on status register bit

1

1

1

1

1

0

s

d d d d d

0

b b b

BLD/BST register bit to STATUS.T

1

1

1

1

1

1

B

d d d d d

0

b b b

SBRC/SBRS skip if register bit equals B

1

1

1

1

1

x

x

d d d d d

1

b b b

(reserved)
