---
title: "Intel 8080"
source: https://en.wikipedia.org/wiki/Intel_8080
domain: retro-z80-assembly
license: CC-BY-SA-4.0
tags: z80 assembly, zilog z80, z80 opcode, intel 8080
fetched: 2026-07-02
---

# Intel 8080

The **Intel 8080** is an 8-bit microprocessor produced by Intel, first released in April 1974. It served as the successor to the 8008, despite not being binary compatible with it. Originally intended for use in embedded systems such as calculators, cash registers, computer terminals, and industrial robots, the 8080 became a popular processor used across a wide range of devices, and contributed to the rise of the microcomputer industry.

Several key design choices contributed to the 8080’s success. Its 40‑pin package simplified interfacing compared to the 8008’s 18‑pin design, enabling a more efficient data bus. The transition to NMOS technology provided faster transistor speeds than the 8008's PMOS, also making it TTL compatible. An expanded instruction set and a full 16-bit address bus allowed the 8080 to access up to 64 KB of memory, quadrupling the capacity of its predecessor. A broader selection of support chips further enhanced its functionality. Many of these improvements stemmed from customer feedback, as designer Federico Faggin and others at Intel heard from industry about shortcomings in the 8008 architecture.

The 8080 found its way into early personal computers such as the Altair 8800 and subsequent S-100 bus systems, and it served as the original target CPU for the CP/M operating system. It directly influenced the later x86 architecture, which was designed so that its assembly language closely resembled that of the 8080, permitting many instructions to map directly from one to the other.

Originally operating at a clock rate of 2 MHz, with common instructions taking between 4 and 11 clock cycles, the 8080 was capable of executing several hundred thousand instructions per second. Later, two faster variants, the 8080A-1 and 8080A-2, offered improved clock speeds of 3.125 MHz and 2.63 MHz, respectively. In most applications, the processor was paired with two support chips, the 8224 clock generator/driver and the 8228 bus controller, to manage its timing and data flow.

## History

Microprocessor customers were reluctant to adopt the 8008 because of limitations such as the single addressing mode, low clock speed, low pin count, and small on-chip stack, which restricted the scale and complexity of software. There were several proposed designs for the 8080, ranging from simply adding stack instructions to the 8008 to a complete departure from all previous Intel architectures. The final design was a compromise between the proposals.

The conception of the 8080 began in the summer of 1971, when Intel wrapped up development of the 4004 and were still working on the 8008. After rumors about the "CPU on a chip" came out, Intel started to see interest in the microprocessor from all sorts of customers. At the same time, Federico Faggin – who led the design of the 4004 and became the primary architect of the 8080 – was giving some technical seminars on both of the aforementioned microprocessors and visiting customers. He found that they were complaining about the architecture and performance of said microprocessors, especially the 8008 – as its speed at 0.5 MHz was "not adequate."

Faggin later proposed the chip to Intel's management and pushed for its implementation in the spring of 1972, as development of the 8008 was wrapping up. Much to his surprise and frustration, however, Intel didn't approve the project. Faggin says that Intel wanted to see how the market would react to the 4004 and 8008 first, while others noted the problems Intel was having getting its latest generation of memory chips out the door and wanted to focus on that. As a result, Intel didn't approve of the project until fall of that year. Faggin hired Masatoshi Shima, who helped design the logic of the 4004 with him, from Japan in November 1972. Shima did the detailed design under Faggin's direction, using the design methodology for random logic with silicon gate that Faggin had created for the 4000 family and the 8008.

The 8080 was explicitly designed to be a general-purpose microprocessor for a larger number of customers. Much of the development effort was spent trying to integrate the functionalities of the 8008's supplemental chips into one package. It was decided early in development that the 8080 was not to be binary-compatible with the 8008, instead opting for source compatibility once run through a transpiler, to allow new software to not be subject to the same restrictions as the 8008. For the same reason, as well as to expand the capabilities of stack-based routines and interrupts, the stack was moved to external memory.

Noting the specialized use of general-purpose registers by programmers in mainframe systems, Faggin with Shima and Stanley Mazor decided the 8080's registers would be specialized, with register pairs having a different set of uses. This also allowed the engineers to more effectively use transistors for other purposes.

Shima finished the layout in August 1973. Production of the chip later began in December of that year. After the development of NMOS logic fabrication, a prototype of the 8080 was completed in January 1974. It had a flaw, in that driving with standard TTL devices increased the ground voltage because high current flowed into the narrow line. Intel had already produced 40,000 units of the 8080 at the direction of the sales section before Shima characterized the prototype. After working out some typical last-minute issues, Intel introduced the product in March 1974. It was released a month later as requiring Low-power Schottky TTL (LS TTL) devices. The 8080A fixed this flaw.

Intel offered an instruction set simulator for the 8080 named INTERP/80 to run compiled PL/M programs. It was written in FORTRAN IV by Gary Kildall while he worked as a consultant for Intel.

There is only one patent on the 8080 with the following names: Federico Faggin, Masatoshi Shima, Stanley Mazor.

## Description

### Programming model

The Intel 8080 is the successor to the 8008. It uses the same basic instruction set and register model as the 8008, although it is neither source code compatible nor binary code compatible with its predecessor. Every instruction in the 8008 has an equivalent instruction in the 8080. The 8080 also adds 16-bit operations in its instruction set. Whereas the 8008 required the use of the HL register pair to indirectly access its 14-bit memory space, the 8080 has addressing modes to directly access its full 16-bit memory space. The internal 7-level push-down call stack of the 8008 was replaced by a dedicated 16-bit stack-pointer (SP) register. The 8080's 40-pin DIP packaging provides a 16-bit address bus and an 8-bit data bus that more efficiently access 64 KiB (216 bytes) of memory.

#### Registers

The processor has seven 8-bit registers (A, B, C, D, E, H, and L), where A is the primary 8-bit accumulator. The other six registers can be used as either individual 8-bit registers or in three 16-bit register pairs (BC, DE, and HL, referred to as B, D and H in Intel documents) depending on the particular instruction. Some instructions can also use the HL register pair as a (limited) 16-bit accumulator. A pseudo-register M, which refers to the dereferenced memory location pointed to by HL, can be used almost anywhere other registers can be used. The 8080 has a 16-bit stack pointer to memory, replacing the 8008's internal stack, and a 16-bit program counter.

#### Flags

The processor maintains internal flag bits (a status register), which indicate the results of arithmetic and logical instructions. Only certain instructions affect the flags. The flags are:

- Sign (S), set if the result is negative.
- Zero (Z), set if the result is zero.
- Parity (P), set if the number of 1 bits in the result is even.
- Carry (C), set if the last addition operation resulted in a carry or if the last subtraction operation required a borrow.
- Auxiliary carry (AC or H), used for binary-coded decimal arithmetic (BCD).

The carry bit can be set or complemented by specific instructions. Conditional-branch instructions test the various flag status bits. The accumulator and the flags together are called the PSW, or program status word. PSW can be pushed to or popped from the stack.

#### Commands, instructions

As with many other 8-bit processors, all instructions are encoded in one byte (including register numbers, but excluding immediate data), for simplicity. Some can be followed by one or two bytes of data, which can be an immediate operand, a memory address, or a port number. Like more advanced processors, it has automatic CALL and RET instructions for multi-level procedure calls and returns (which can even be conditionally executed, like jumps) and instructions to save and restore any 16-bit register pair on the machine stack. Eight one-byte call instructions (`RST`) for subroutines exist at the fixed addresses 00h, 08h, 10h, ..., 38h. These are intended to be supplied by external hardware in order to invoke a corresponding interrupt service routine, but are also often employed as fast system calls. The slowest instruction is `XTHL`, which exchanges the register pair HL with the last item pushed on the stack.

##### 8-bit instructions

All 8-bit ALU operations with two operands can only be performed on the 8-bit accumulator (the A register). The other operand can be either an immediate value, another 8-bit register, or a memory byte addressed by the 16-bit register pair HL. Increments and decrements can be performed on any 8 bit register or an HL-addressed memory byte. Direct copying is supported between any two 8-bit registers and between any 8-bit register and an HL-addressed memory byte. Due to the regular encoding of the `MOV` instruction (using a quarter of available opcode space), there are redundant codes to copy a register into itself (`MOV B,B`, for instance), which are of little use, except for delays. The systematic opcode for `MOV M,M` is instead used to encode the halt (`HLT`) instruction, halting execution until an external reset or interrupt occurs.

##### 16-bit operations

Although the 8080 is generally an 8-bit processor, it has limited abilities to perform 16-bit operations. Any of the three 16-bit register pairs (BC, DE, or HL, referred to as B, D, H in Intel documents) or SP can be loaded with an immediate 16-bit value (using `LXI`), incremented or decremented (using `INX` and `DCX`), or added to HL (using `DAD`). By adding HL to itself, it is possible to achieve the same result as a 16-bit arithmetical left shift with one instruction. The only 16-bit instructions that affect any flag is `DAD`, which sets the CY (carry) flag in order to allow for programmed 24-bit or 32-bit arithmetic (or larger), needed to implement floating-point arithmetic. BC, DE, HL, or PSW can be copied to and from the stack using `PUSH` and `POP`. A stack frame can be allocated using `DAD SP` and `SPHL`. A branch to a computed pointer can be executed with `PCHL`. `LHLD` loads HL from directly addressed memory and `SHLD` stores HL likewise. The `XCHG` instruction exchanges the values of the HL and DE register pairs. `XTHL`exchanges last item pushed on stack with HL. None of these 16-bit operations were supported on the earlier Intel 8008.

##### Instruction set

Opcode

Operands

Mnemonic

Clocks

Description

7

6

5

4

3

2

1

0

b2

b3

0

0

0

0

0

0

0

0

—

—

NOP

4

No operation

0

0

RP

0

0

0

1

datlo

dathi

LXI

rp,data

10

RP ←

data

0

0

RP

0

0

1

0

—

—

STAX

rp

7

(RP) ← A [BC or DE only]

0

0

RP

0

0

1

1

—

—

INX

rp

5

RP ← RP + 1

0

0

DDD

1

0

0

—

—

INR

ddd

5/10

DDD ← DDD + 1

0

0

DDD

1

0

1

—

—

DCR

ddd

5/10

DDD ← DDD - 1

0

0

DDD

1

1

0

data

—

MVI

ddd,data

7/10

DDD ← data

0

0

RP

1

0

0

1

—

—

DAD

rp

10

HL ← HL + RP

0

0

RP

1

0

1

0

—

—

LDAX

rp

7

A ← (RP) [BC or DE only]

0

0

RP

1

0

1

1

—

—

DCX

rp

5

RP ← RP - 1

0

0

0

0

0

1

1

1

—

—

RLC

4

A

1-7

← A

0-6

; A

0

← Cy ← A

7

0

0

0

0

1

1

1

1

—

—

RRC

4

A

0-6

← A

1-7

; A

7

← Cy ← A

0

0

0

0

1

0

1

1

1

—

—

RAL

4

A

1-7

← A

0-6

; Cy ← A

7

; A

0

← Cy

0

0

0

1

1

1

1

1

—

—

RAR

4

A

0-6

← A

1-7

; Cy ← A

0

; A

7

← Cy

0

0

1

0

0

0

1

0

addlo

addhi

SHLD

add

16

(add) ← HL

0

0

1

0

0

1

1

1

—

—

DAA

4

If A

0-3

> 9 OR AC = 1 then A ← A + 6;

then if A4-7 > 9 OR Cy = 1 then A ← A + 0x60

0

0

1

0

1

0

1

0

addlo

addhi

LHLD

add

16

HL ← (add)

0

0

1

0

1

1

1

1

—

—

CMA

4

A ← ¬A

0

0

1

1

0

0

1

0

addlo

addhi

STA

add

13

(add) ← A

0

0

1

1

0

1

1

1

—

—

STC

4

Cy ← 1

0

0

1

1

1

0

1

0

addlo

addhi

LDA

add

13

A ← (add)

0

0

1

1

1

1

1

1

—

—

CMC

4

Cy ← ¬Cy

0

1

DDD

SSS

—

—

MOV

ddd,sss

5/7

DDD ← SSS

0

1

1

1

0

1

1

0

—

—

HLT

7

Halt

1

0

ALU

SSS

—

—

ADD ADC SUB SBB ANA XRA ORA CMP

sss

4/7

A ← A [ALU operation] SSS

1

1

CC

0

0

0

—

—

Rcc (RET conditional)

5/11

If cc true, PC ← (SP), SP ← SP + 2

1

1

RP

0

0

0

1

—

—

POP

rp

10

RP ← (SP), SP ← SP + 2

1

1

CC

0

1

0

addlo

addhi

Jcc

add

(JMP conditional)

10

If cc true, PC ← add

1

1

0

0

0

0

1

1

addlo

addhi

JMP

add

10

PC ← add

1

1

CC

1

0

0

addlo

addhi

Ccc

add

(CALL conditional)

11/17

If cc true, SP ← SP - 2, (SP) ← PC, PC ← add

1

1

RP

0

1

0

1

—

—

PUSH

rp

11

SP ← SP - 2, (SP) ← RP

1

1

ALU

1

1

0

data

—

ADI ACI SUI SBI ANI XRI ORI CPI

data

7

A ← A [ALU operation] data

1

1

N

1

1

1

—

—

RST

n

11

SP ← SP - 2, (SP) ← PC, PC ← N x 8

1

1

0

0

1

0

0

1

—

—

RET

10

PC ← (SP), SP ← SP + 2

1

1

0

0

1

1

0

1

addlo

addhi

CALL

add

17

SP ← SP - 2, (SP) ← PC, PC ← add

1

1

0

1

0

0

1

1

port

—

OUT

port

10

Port ← A

1

1

0

1

1

0

1

1

port

—

IN

port

10

A ← Port

1

1

1

0

0

0

1

1

—

—

XTHL

18

HL ↔ (SP)

1

1

1

0

1

0

0

1

—

—

PCHL

5

PC ← HL

1

1

1

0

1

0

1

1

—

—

XCHG

4

HL ↔ DE

1

1

1

1

0

0

1

1

—

—

DI

4

Disable interrupts

1

1

1

1

1

0

0

1

—

—

SPHL

5

SP ← HL

1

1

1

1

1

0

1

1

—

—

EI

4

Enable interrupts

7

6

5

4

3

2

1

0

b2

b3

Mnemonic

Clocks

Description

SSS DDD

2

1

0

CC

ALU

RP

B

0

0

0

NZ

ADD ADI (A ← A + arg)

BC

C

0

0

1

Z

ADC ACI (A ← A + arg + Cy)

DE

D

0

1

0

NC

SUB SUI (A ← A - arg)

HL

E

0

1

1

C

SBB SBI (A ← A - arg - Cy)

SP or PSW

H

1

0

0

PO

ANA ANI (A ← A ∧ arg)

L

1

0

1

PE

XRA XRI (A ← A ⊻ arg)

M

1

1

0

P

ORA ORI (A ← A ∨ arg)

A

1

1

1

N

CMP CPI (A - arg)

SSS DDD

2

1

0

CC

ALU

### Input/output scheme

#### Input output port space

The 8080 supports 256 input/output (I/O) ports, accessed via dedicated I/O instructions taking port addresses as operands. Generating the control signals for selecting between RAM and I/O is usually aided by a support chip (8212 or 8228). This I/O mapping scheme is regarded as an advantage, as it frees up the processor's limited address space. Many CPU architectures instead use so-called memory-mapped I/O (MMIO), in which a common address space is used for both RAM and peripheral chips. This removes the need for dedicated I/O instructions, although a drawback in such designs may be that special hardware must be used to insert wait states, as peripherals are often slower than memory. In some simple 8080 computers, however, I/O is indeed addressed as if they were memory cells, "memory-mapped", leaving the I/O commands unused. I/O addressing can also sometimes employ the fact that the processor outputs the same 8-bit port address to both the lower and the higher address byte (i.e., `IN 05h` would put the address 0505h on the 16-bit address bus). Similar I/O-port schemes are used in the backward-compatible Zilog Z80 and Intel 8085, and the closely related x86 microprocessor families.

#### Separate stack space

One of the bits in the processor state word (see below) indicates that the processor is accessing data from the stack. Using this signal, it is possible to implement a separate stack memory space. This feature is seldom used.

### Status word

For more advanced systems, during the beginning of each machine cycle, the processor places an eight bit status word on the data bus. This byte contains flags that determine whether the memory or I/O port is accessed and whether it is necessary to handle an interrupt.

The interrupt system state (enabled or disabled) is also output on a separate pin. For simple systems, where the interrupts are not used, it is possible to find cases where this pin is used as an additional single-bit output port (the popular Radio-86RK computer made in the Soviet Union, for instance).

### Interrupts

Hardware interrupts are initiated by asserting the interrupt request (INT) pin. At the next opcode fetch cycle (M1), the interrupt will be acknowledged with the INTA state code. At this time, an instruction is "jammed" (Intel's word) by external hardware on the data bus. This can be a one-byte `RST` instruction, or if using an Intel 8259, a `CALL` instruction. Interrupts may be enabled and disabled with `EI` and `DI` instructions, respectively. Interrupts are disabled after an INTA; they must be re-enabled explicitly by the interrupt service routine. The 8080 does not support non-maskable interrupts.

### Example code

The following 8080/8085 assembler source code is for a subroutine named `memcpy` that copies a block of data bytes of a given size from one location to another. The data block is copied one byte at a time, and the data movement and looping logic utilizes 16-bit operations.

| 1000 1000 1000 1A 1001 77 1002 13 1003 23 1004 0B 1005 78 1006 B1 1007 C2 00 10 100A C9 | ; memcpy -- ; Copy a block of memory from one location to another. ; ; Entry registers ; BC - Number of bytes to copy ; DE - Address of source data block ; HL - Address of target data block ; ; Return registers ; BC - Zero org 1000h ;Origin at 1000h memcpy public loop: ldax d ;Load A from the address pointed by DE mov m,a ;Store A into the address pointed by HL inx d ;Increment DE inx h ;Increment HL dcx b ;Decrement BC (does not affect Flags) mov a,b ;Copy B to A (so as to compare BC with zero) ora c ;A = A \| C (are both B and C zero?) jnz loop ;Jump to 'loop:' if the zero-flag is not set. ret ;Return |
|---|---|

### Pin use

The address bus has its own 16 pins, and the data bus has 8 pins that are usable without any multiplexing. Using the two additional pins (read and write signals), it is possible to assemble simple microprocessor devices very easily. Only the separate IO space, interrupts, and DMA need added chips to decode the processor pin signals. Nonetheless, the pin load capacity is limited; even simple computers often require bus amplifiers.

The processor needs three power sources (−5, +5, and +12 V) and two non-overlapping high-amplitude synchronizing signals. Nonetheless, at least the late Soviet version КР580ВМ80А was able to work with a single +5 V power source, the +12 V pin being connected to +5 V and the −5 V pin to ground.

The pin-out table, from the chip's accompanying documentation, describes the pins as follows:

| Pin number | Signal | Type | Comment |
|---|---|---|---|
| 1 | A10 | Output | Address bus 10 |
| 2 | GND | — | Ground |
| 3 | D4 | Bidirectional | Bidirectional data bus. The processor also momentarily transmits the "processor state" during SYNC^φ1, providing information about what the processor is currently doing: D0 (INTA) reading interrupt command. In response to the interrupt signal, the processor is reading and executing a single arbitrary command with this flag raised. Normally the supporting chips provide the subroutine call command (CALL or RST), transferring control to the interrupt handling code. D1 (WO-) low true. Write to memory or output to port D2 (STACK) accessing stack (probably a separate stack memory space was initially planned) D3 (HLTA) doing nothing, has been halted by the HLT instruction D4 (OUT) writing data to an output port D5 (M1) reading the first byte of an instruction D6 (IN) reading data from an input port D7 (MEMR) reading data from memory |
| 4 | D5 |   |   |
| 5 | D6 |   |   |
| 6 | D7 |   |   |
| 7 | D3 |   |   |
| 8 | D2 |   |   |
| 9 | D1 |   |   |
| 10 | D0 |   |   |
| 11 | −5 V | — | The −5 V power supply. This must be the first power source connected and the last disconnected, otherwise the processor will be damaged. |
| 12 | RESET | Input | Reset. This active low signal forces execution of commands located at address 0000. The content of other processor registers is not modified. |
| 13 | HOLD | Input | Direct memory access request. The processor is requested to switch the data and address bus to the high impedance ("disconnected") state. |
| 14 | INT | Input | Interrupt request |
| 15 | φ2 | Input | The second phase of the clock generator signal |
| 16 | INTE | Output | The processor has two commands for setting 0 or 1 level on this pin. The pin normally is supposed to be used for interrupt control. In simple computers, however, it was sometimes used as a single bit output port for various purposes. |
| 17 | DBIN | Output | Read (the processor reads from memory or input port) |
| 18 | WR- | Output | Write (the processor writes to memory or output port). This is an active low output. |
| 19 | SYNC | Output | Active level indicates that the processor has put the "state word" on the data bus. The various bits of this state word provide added information to support the separate address and memory spaces, interrupts, and direct memory access. This signal is required to pass through additional logic before it can be used to write the processor state word from the data bus into some external register, e.g., 8238 Archived September 18, 2023, at the Wayback Machine-System Controller and Bus Driver. |
| 20 | +5 V | — | The + 5 V power supply |
| 21 | HLDA | Output | Direct memory access confirmation. The processor switches data and address pins into the high impedance state, allowing another device to manipulate the bus |
| 22 | φ1 | Input | The first phase of the clock generator signal |
| 23 | READY | Input | Wait. With this signal it is possible to suspend the processor's work. It is also used to support the hardware-based step-by step debugging mode. |
| 24 | WAIT | Output | Wait (indicates that the processor is in the waiting state) |
| 25 | A0 | Output | Address bus |
| 26 | A1 |   |   |
| 27 | A2 |   |   |
| 28 | 12 V | — | The +12 V power supply. This must be the *last* connected and first disconnected power source. |
| 29 | A3 | Output | The address bus; can switch into high impedance state on demand |
| 30 | A4 |   |   |
| 31 | A5 |   |   |
| 32 | A6 |   |   |
| 33 | A7 |   |   |
| 34 | A8 |   |   |
| 35 | A9 |   |   |
| 36 | A15 |   |   |
| 37 | A12 |   |   |
| 38 | A13 |   |   |
| 39 | A14 |   |   |
| 40 | A11 |   |   |

## Support chips

A key factor in the success of the 8080 was the broad range of support chips available, providing serial communications, counter/timing, input/output, direct memory access, and programmable interrupt control amongst other functions:

- 8214 - Priority Interrupt Control Unit
- 8224 – Clock generator
- 8228/8238 – System controller and bus driver
- 8251 – Communication controller
- 8253 – Programmable interval timer
- 8255 – Programmable peripheral interface
- 8257 – DMA controller
- 8259 – Programmable interrupt controller

## Physical implementation

The 8080 integrated circuit has an NMOS design, which employed non‑saturated enhancement mode transistors as loads, which demanded supplementary voltage levels (+12 V and −5 V) alongside the standard TTL compatible +5 V.

It was manufactured in a silicon gate process using a minimal feature size of 6 μm. A single layer of metal is used to interconnect the approximately 4,500 transistors in the design, but the higher resistance polysilicon layer, which required higher voltage for some interconnects, is implemented with transistor gates. The die size is approximately 20 mm2.

## Commercial impact

### Applications and successors

The 8080 was used in many early microcomputers, such as the MITS Altair 8800 Computer, Processor Technology SOL-20 Terminal Computer and IMSAI 8080. It formed the basis for the CP/M operating system.

In 1979, after the introduction of the Z80 and 8085 processors, five manufacturers of the 8080 were selling an estimated 500,000 units per month at a price around $3 to $4 each.

The first single-board microcomputers, such as MYCRO-1 and the *dyna-micro* / MMD-1 (see: Single-board computer) were based on the Intel 8080. One of the early uses of the 8080 was made in the late 1970s by Cubic-Western Data of San Diego, California, in its Automated Fare Collection Systems custom designed for mass transit systems around the world. An early industrial use of the 8080 is as the "brain" of the DatagraphiX Auto-COM (Computer Output Microfiche) line of products, which takes large amounts of user data from reel-to-reel tape and images it onto microfiche. The Auto-COM instruments also include an entire automated film cutting, processing, washing, and drying sub-system.

Several early arcade video games were built around the 8080 microprocessor. The first commercially available arcade video game to incorporate a microprocessor was *Gun Fight*, Midway Games' 8080-based reimplementation of Taito's discrete-logic *Western Gun*, which was released in November 1975. (A pinball machine that incorporated a Motorola 6800 processor, *The Spirit of '76*, had already been released the previous month.) The 8080 was then used in later Midway arcade video games and in Taito's 1978 *Space Invaders*, one of the most successful and well-known of all arcade video games.

Zilog introduced the Z80, which has a compatible machine language instruction set and initially used the same assembly language as the 8080, but for legal reasons, Zilog developed a syntactically-different (but code compatible) alternative assembly language for the Z80. At Intel, the 8080 was followed by the compatible and electrically more elegant 8085.

Later, Intel issued the assembly-language compatible (but not binary-compatible) 16-bit 8086 and then the 8/16-bit 8088, which was selected by IBM for its new PC to be launched in 1981. Later NEC made the NEC V20 (an 8088 clone with Intel 80186 instruction set compatibility) which also supports an 8080 emulation mode. This is also supported by NEC's V30 (a similarly enhanced 8086 clone). Thus, the 8080, via its instruction set architecture (ISA), made a lasting impact on computer history.

A number of processors compatible with the Intel 8080A were manufactured in the Eastern Bloc: the KR580VM80A (initially marked as КР580ИК80) in the Soviet Union, the MCY7880 made by Unitra CEMI in Poland, the MHB8080A made by TESLA in Czechoslovakia, the 8080APC made by Tungsram / MEV in Hungary, and the MMN8080 made by Microelectronica Bucharest in Romania.

As of 2017, the 8080 is still in production at Lansdale Semiconductors.

- Intel 8080 second sources
- (AMD Am9080)AMD Am9080
- (CEMI MCY7880 (Poland))CEMI MCY7880 (Poland)
- (Kvazar Kyiv K580IK80 (Ukrainian SSR))Kvazar Kyiv K580IK80 (Ukrainian SSR)
- (Mitsubishi Electric M5L8080)Mitsubishi Electric M5L8080
- (National Semiconductor INS8080)National Semiconductor INS8080
- (NEC μPD8080AF)NEC μPD8080AF
- (OKI MSM8080)OKI MSM8080
- (Siemens SAB8080)Siemens SAB8080
- (Signetics MP8080)Signetics MP8080
- (Tesla MHB8080)Tesla MHB8080
- (Texas Instruments TMS8080)Texas Instruments TMS8080
- (5G8080 (PR China))5G8080 (PR China)

### Industry change

The 8080 also changed how computers were created. When the 8080 was introduced, computer systems were usually created by computer manufacturers such as Digital Equipment Corporation, Hewlett-Packard, or IBM. A manufacturer would produce the whole computer, including processor, terminals, and system software such as compilers and operating system. The 8080 was designed for almost any application *except* a complete computer system. Hewlett-Packard developed the HP 2640 series of smart terminals around the 8080. The HP 2647 is a terminal that runs the programming language BASIC on the 8080. Microsoft's founding product, Microsoft BASIC, was originally programmed for the 8080.

The 8080 and 8085 gave rise to the 8086, which was designed as a source code compatible, albeit not binary compatible, extension of the 8080. This design, in turn, later spawned the x86 family of chips, which continue to be Intel's primary line of processors. Many of the 8080's core machine instructions and concepts survive in the widespread x86 platform. Examples include the registers named *A*, *B*, *C*, and *D* and many of the flags used to control conditional jumps. 8080 assembly code can still be directly translated into x86 instructions, since all of its core elements are still present.

### US Patent

US patent 4010449, Federico Faggin, Masatoshi Shima, Stanley Mazor, "MOS computer employing a plurality of separate chips", issued March 1, 1977 . This patent contains three claims. The first two relate to the status word multiplexed onto the data bus. The third claim is for the `RST 7` instruction, which can be invoked by pulling the data bus high. The prior art 8008 `RST 7` required more complicated instruction jamming circuitry.

## Cultural impact

- An asteroid is named 8080 Intel in recognition of the role played by the chip in the PC revolution, which had a significant impact on the field of astronomy.
- Microsoft's published phone number, 425-882-8080, was chosen because much early work was on this chip.
- Many of Intel's main phone numbers also take a similar form: xxx-xxx-8080
