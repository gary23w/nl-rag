---
title: "Opcode"
source: https://en.wikipedia.org/wiki/Opcode
domain: disassembly-analysis
license: CC-BY-SA-4.0
tags: disassembly analysis, interactive disassembler workflow, assembly instruction decoding, opcode instruction set, binary code inspection
fetched: 2026-07-02
---

# Opcode

In computing, an **opcode** (abbreviated from **operation code**) is an enumerated value that specifies the operation to be performed. Opcodes are employed in hardware devices such as arithmetic logic units (ALUs), central processing units (CPUs), and software instruction sets. In ALUs, the opcode is directly applied to circuitry via an input signal bus. In contrast, in CPUs, the opcode is the portion of a machine language instruction that specifies the operation to be performed.

## CPUs

Opcodes are found in the machine language instructions of CPUs as well as in some abstract computing machines. In CPUs, an opcode may be referred to as an **instruction machine code**, **instruction code**, **instruction syllable**, **instruction parcel,** or **opstring**. For any particular processor (which may be a general CPU or a more specialized processing unit), the opcodes are defined by the processor's instruction set architecture (ISA). They can be described using an opcode table. The types of operations may include arithmetic, data copying, logical operations, program control, and special instructions (e.g., CPUID).

In addition to the opcode, many instructions specify the data (known as operands) the operation will act upon, although some instructions may have implicit operands or none. Some instruction sets have nearly uniform fields for opcode and operand specifiers, whereas others (e.g., x86 architecture) have a less uniform, variable-length structure. Instruction sets can be extended through opcode prefixes, which add a subset of new instructions made up of existing opcodes following reserved byte sequences.

### Sample opcode table

This table shows opcodes of a simple 8-bit microprocessor, the Intel 8008 from 1972.

Each opcode is 8 bits long. Each is shown as a binary pattern of ones and zeros in the **Opcode** column. Up to two additional fields may be embedded into the opcode. Some 3-bit fields are labeled DDD, SSS, CC, and ALU. The SSS (source) and DDD (destination) fields specify one of the eight possible 8008 registers or memory: A, B, C, D, E, H, L, or M. CC specifies one of eight result conditions that will activate certain JMP, CAL, and RET instructions. ALU specifies one of a possible eight arithmetic logic unit functions to be performed during an instruction, specifically, add, add with carry, subtract, subtract with borrow, logical AND, logical XOR, logical OR, and compare. The **X** in some fields means that either a 1 or 0 can be inserted with no effect.

The fixed ones and zeros are combined with the parameter fields to build the 8-bit opcode. Additionally, the full instruction might require one or two additional bytes of operands. These are shown in the second major column of the table, labeled **Operands**. If no operands are required, the column is filled with a dash (—).

Since the ones and zeros are difficult to remember, the **Mnemonic** column shows a short, easy to remember letter code that an assembly language programmer may use to invoke the required opcode.

The **Description** column shows the function performed by the microprocessor when it encounters a specific opcode.

Opcode

Operands

Mnemonic

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

X

—

—

HLT

Halt

0

0

DDD

0

0

0

—

—

INr

DDD ← DDD + 1 (except A and M)

0

0

DDD

0

0

1

—

—

DCr

DDD ← DDD - 1 (except A and M)

0

0

0

0

0

0

1

0

—

—

RLC

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

CC

0

1

1

—

—

Rcc (RET conditional)

If cc true, P ← (stack)

0

0

ALU

1

0

0

data

—

ADI ACI SUI SBI NDI XRI ORI CPI

data

A ← A [ALU operation] data

0

0

N

1

0

1

—

—

RST

n

(stack) ← P, P ← N x 8

0

0

DDD

1

1

0

data

—

LrI

data

(Load r with immediate data)

DDD ← data

0

0

X

X

X

1

1

1

—

—

RET

P ← (stack)

0

0

0

0

1

0

1

0

—

—

RRC

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

0

1

0

—

—

RAL

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

0

1

0

—

—

RAR

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

1

CC

0

0

0

addlo

addhi

Jcc

add

(JMP conditional)

If cc true, P ← add

0

1

0

0

port

1

—

—

INP

port

A ← Port (ports 0-7 only)

0

1

port

1

—

—

OUT

port

Port ← A (ports 8-31 only)

0

1

CC

0

1

0

addlo

addhi

Ccc

add

(CAL conditional)

If cc true, (stack) ← P, P ← add

0

1

X

X

X

1

0

0

addlo

addhi

JMP

add

P ← add

0

1

X

X

X

1

1

0

addlo

addhi

CAL

add

(stack) ← P, P ← add

1

0

ALU

SSS

—

—

ADr ACr SUr SBr NDr XRr ORr CPr

A ← A [ALU operation] SSS

1

1

DDD

SSS

—

—

Lds (Load d with s)

DDD ← SSS

1

1

1

1

1

1

1

1

—

—

HLT

Halt

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

Description

SSS DDD

2

1

0

CC

ALU

A

0

0

0

FC, C false

ADr ADI (A ← A + arg)

B

0

0

1

FZ, Z false

ACr ACI (A ← A + arg + Cy)

C

0

1

0

FS, S false

SUr SUI (A ← A - arg)

D

0

1

1

FP, P odd

SBr SBI (A ← A - arg - Cy)

E

1

0

0

TC, C true

NDr NDI (A ← A ∧ arg)

H

1

0

1

TZ, Z true

XRr XRI (A ← A ⊻ arg)

L

1

1

0

TS, S true

ORr ORI (A ← A ∨ arg)

M

1

1

1

TP, P even

CPr CPI (A - arg)

SSS DDD

2

1

0

CC

ALU

## Software instruction sets

Opcodes can be found in bytecodes and other representations intended for execution by software interpreters. These often employ slightly higher-level data types and operations than those found in hardware opcodes but are nevertheless constructed along similar lines. Examples include the byte code found in Java class files, which are interpreted by Java virtual machines, the byte code used in GNU Emacs for compiled Lisp code, and NET Common Intermediate Language.
