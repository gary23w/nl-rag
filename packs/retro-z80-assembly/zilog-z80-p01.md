---
title: "Zilog Z80 (part 1/2)"
source: https://en.wikipedia.org/wiki/Zilog_Z80
domain: retro-z80-assembly
license: CC-BY-SA-4.0
tags: z80 assembly, zilog z80, z80 opcode, intel 8080
fetched: 2026-07-02
part: 1/2
---

# Zilog Z80

The **Zilog Z80** is an 8-bit microprocessor designed by Zilog, first released in 1976; it played an important role in the evolution of early personal computing. It was designed to be software-compatible with the Intel 8080, offering a compelling alternative due to its better integration and increased performance. Along with the 8080's seven registers and flags register, the Z80 introduced an alternate register set, two 16-bit index registers, and additional instructions, including bit manipulation and block copy/search.

Originally intended for use in embedded systems like the 8080 was, the Z80's combination of compatibility, affordability, and superior performance led to widespread adoption in video game systems and home computers throughout the late 1970s and early 1980s, helping to fuel the personal computing revolution. The Z80 was used in iconic products such as the Osborne 1, Radio Shack TRS-80, ColecoVision, ZX Spectrum, Sega's Master System and the *Pac-Man* arcade cabinet. In the early 1990s, it was used in portable devices, including the Game Gear and the TI-81 and succeeding graphing calculators.

The Z80 was the brainchild of Federico Faggin, a key figure behind the creation of the Intel 8080. After leaving Intel in 1974, he co-founded Zilog with Ralph Ungermann. The Z80 debuted in July 1976, and its success allowed Zilog to establish its own chip factories. For initial production, Zilog licensed the Z80 to U.S.-based Synertek and Mostek, along with European second-source manufacturer, SGS. The design was also copied by various Japanese, Eastern European, and Soviet manufacturers gaining global market acceptance as major companies like NEC, Toshiba, Sharp, and Hitachi produced their own versions or compatible clones.

The Z80 continued to be used in embedded systems for many years, despite the introduction of more powerful processors; it remained in production until June 2024, 48 years after its original release. Zilog also continued to enhance the basic design of the Z80 with several successors, including the Z180, Z280, and Z380, with the latest iteration, the eZ80, introduced in 2001 and available for purchase as of 2025.


## History

### Early history

At Fairchild Semiconductor, and later at Intel, physicist and engineer Federico Faggin had been working on fundamental transistor and semiconductor manufacturing technology. He also developed the basic design methodology used for memories and microprocessors at Intel and led the work on the Intel 4004, the Intel 8080 and several other ICs. Masatoshi Shima was the principal logic and transistor-level designer of the 4004 and the 8080 under Faggin's supervision, while Ralph Ungermann was in charge of custom integrated circuit design.

In early 1974, Intel viewed microprocessors not so much as products to be sold on their own but as a way to sell more of its main products, static RAM and ROM. A reorganization placed some of the formerly independent sections under the direction of Les Vadasz, further diluting the microprocessor's place in the company. That year, the 1973–1975 recession reached a peak, and Intel laid off several employees. All of this led to Faggin becoming restless, and he invited Ungermann out for drinks and asked if he would be interested in starting their own company. Ungermann immediately agreed, and as he had less to do at Intel, he left in August or September, followed by Faggin, whose last day at Intel was Halloween 1974. When Shima heard, he asked to come to the new company as well, but having no actual product design or money, they told him to wait.

The newly formed and unnamed company initially began designing a single-chip microcontroller called the 2001. They met with Synertek to discuss fabrication on their lines, and when Faggin began to understand the costs involved, it became clear that a low-cost product like this would not be able to compete with a design from a company with its own production lines, like Intel. They then began considering a more complex microprocessor instead, initially known as the Super 80, with the main feature being its use of a +5 V bus instead of the more common −5, +5 and 12 V used by designs like the 8080. The new design was intended to be compatible with the 8080, but add a number of the features of the Motorola 6800, including index registers and improved interrupts.

### Exxon investment, detailed development begins

While still being set up, the industry newsletter *Electronic News* heard of them and published a story on the newly formed company. This attracted the attention of Exxon Enterprises, Exxon's high-tech investment arm. At the time, in the midst of the recession, there was little venture capital available, with a total of $10 million for the entire industry being spent in all of 1975 (equivalent to $60 million in 2025). Someone from Exxon contacted the still-unnamed company, and arranged a meeting that eventually led to them providing an initial $500,000 funding in June 1975 (equivalent to $3 million in 2025).

With funding being discussed and a design to be built, Masatoshi Shima joined in February 1975. Shima immediately set about producing a high-level design, adding several concepts of his own. In particular, he used his experience on NEC minicomputers to add the concept of two sets of processor registers so they could quickly respond to interrupts. Ungerman began the development of a series of related controllers and peripheral chips that would complement the design.

Through this period, Shima developed a legendary reputation for being able to convert logic concepts into physical design in realtime; while discussing a proposed feature, he would often interrupt and state how much room that would take on the chip and veto its addition if it was too large. The first pass at the design was complete by April 1975. Shima had completed a logic layout by the beginning of May. A second version of the logic design was issued on August 7 and the bus details by September 16. Tape-out was completed in November and converting the tape into a production mask required two more months.

Faggin had already started looking for a production partner. By this time, Synertek and Mostek had both set up the depletion-mode production lines that could be used to produce the design. Having talked to Synertek previously, Faggin approached them first. However, the president of Synertek demanded that the company be given a second source license, allowing them to sell the design directly. Faggin thought this would mean they could never compete even if they set up their own lines, and the agreement fell through. He then turned to Mostek, who agreed to a term of exclusivity while Zilog got their lines set up, and was eventually given the second source agreement.

After considering multiple names for the new company, and finding them so unmemorable they could not recall them even a day later, Faggin and Ungermann were kicking around ideas based on "integrated logic" when Ungermann said, "How about Zilog?" Faggin immediately agreed, stating they could say it was the "last word in integrated logic". When they met the next day and both immediately recalled it, the company had its name.

### Into production

The first samples were returned from Mostek on March 9, 1976. By the end of the month, they had also completed an assembler-based development system. Some of the Z80 support and peripheral ICs were under development at this point, and some of them were launched during the following year. Among them were the Z80 CTC (counter/timer), Z80 DMA (direct memory access), Z80 DART (dual asynchronous receiver–transmitter), Z80 SIO (synchronous communication controller), and Z80 PIO (parallel input/output).

The Z80 was officially launched in July 1976. At the time, concerns existed within the semiconductor industry about the unlicensed reproduction of chip designs by foreign manufacturers. To help deter reverse engineering, the Zilog team incorporated six "traps", transistors that were subtly modified to behave differently than their appearance would suggest. According to Shima, an engineer at NEC later told him that these traps delayed their reverse engineering efforts by six months. NEC later settled a patent infringement dispute with Zilog, securing a license to produce authorized versions of the Z80 and other chips.

Following the successful launch of the Z80, Faggin and Ungermann approached Exxon for funding to establish semiconductor fabrication plant. Exxon agreed, and Zilog built its own production line, enabling the company to capture an estimated 60 to 70 percent of the total market for Z80 sales. Meanwhile, Mostek was authorized to produce a licensed version of the chip, the MK3880, providing a second source for customers, a safeguard that Intel lacked. At the time, second-source agreements were considered essential, particularly for startups like Zilog, which carried a higher risk of business failure and supply disruption.

### Comparison with the 8080

Faggin designed the instruction set to be binary compatible with the 8080 so that most 8080 code, notably the CP/M operating system and Intel's PL/M compiler for 8080 (as well as its generated code), would run unmodified on the new Z80 CPU. Masatoshi Shima designed most of the microarchitecture as well as the gate and transistor levels of the Z80 CPU, assisted by a small number of engineers and layout people. CEO Federico Faggin was actually heavily involved in the chip layout work, together with two dedicated layout people. According to Faggin, he worked 80 hours a week in order to meet the tight schedule given by the financial investors.

The Z80 offered multiple improvements over the 8080:

- An enhanced instruction set including:
  - a more logical, comprehensible and readable system of assembler instruction mnemonics
  - more flexible 16-bit data movement (load, or LD) instructions, crucially including the stack pointer SP
  - more flexible addressing modes for input/output to external peripheral ports
  - single-bit addressing of all registers and memory, including bit testing
  - shifts/rotates on memory and registers other than the accumulator
  - subtraction supported for BCD arithmetic
  - rotate instructions for packed BCD number strings in memory
  - 16-bit subtraction and 8-bit negation
  - program looping
  - program counter (PC) relative jumps
  - block copy, block input/output (I/O), and byte search instructions.
- An overflow flag with better support for signed 8- and 16-bit arithmetics.
- New IX and IY index registers with *base+offset* addressing mode
- A better interrupt system:
  - A more automatic and general vectorized interrupt system, *mode 2*, primarily intended for Zilog's line of counter/timers, DMA and communications controllers, as well as a fixed vector interrupt system, *mode 1*, for simple systems with minimal hardware (with *mode 0* being the 8080-compatible mode).
  - A non-maskable interrupt (NMI), which can be used to respond to power-down situations or other high-priority events (and allowing a minimalistic Z80 system to easily implement a two-level interrupt scheme in *mode 1*).
- A complete duplicate register file, which could be quickly switched, to speed up response to interrupts such as fast asynchronous event handlers or a multitasking dispatcher. Although they were not intended as extra registers for general code, they were nevertheless used that way in some applications.
- Less hardware required for power supply, clock generation and interface to memory and I/O
- Single 5-volt power supply (the 8080 needed −5 V, +5 V, and +12 V).
- Single-phase 5-volt clock (the 8080 needed a high-amplitude (9 to 12 volts) non-overlapping two-phase clock).
- Built-in DRAM refresh, which would otherwise require external circuitry. The 8080 had been designed before DRAM was widely used, and the common SRAM did not need refresh. By the mid-1970s DRAM had largely replaced SRAM for most roles, but using DRAM with the 8080 required additional external circuitry. Implementing this internally in the Z80 reduced the complexity and cost of a complete system.
- Non-multiplexed buses (the 8080 had state signals multiplexed onto the data bus).
- A special reset that zeroes only the program counter, so that a single Z80 CPU could be used in a development system such as an in-circuit emulator.

### Success in the market

The Z80 took over from the 8080 and its offspring, the 8085, in the processor market and became one of the most popular and widely used 8-bit CPUs. Some organizations such as British Telecom remained loyal to the 8085 for embedded applications, owing to their familiarity with it and to its on-chip serial interface and interrupt architecture. Likewise, Zenith Data Systems paired the 8085 with the 16-bit Intel 8088 in its first MS-DOS computer, the Zenith Z-100, despite having previous experience with its pioneering Z80-based Heathkit H89 and Zenith Z-89 products. However, other computers were made integrating the Z80 with other CPUs: the Radio Shack TRS-80 Model 16 with a Motorola 68000, the DEC Rainbow with an 8088, and the Commodore 128 with a MOS Technology 8502.

Zilog was later producing a low-power Z80 suitable for the growing laptop computer market of the early 1980s. Intel produced a CMOS 8085 (80C85) used in battery-powered portable computers, such as the Kyocera-designed laptop from April 1983, also sold by Tandy (as TRS-80 Model 100), Olivetti, and NEC. In following years, however, CMOS versions of the Z80 (from both Zilog and Japanese manufacturers) would dominate this market as well, in products such as the Amstrad NC100, Cambridge Z88 and Tandy's own WP-2.

Perhaps a key to the initial success of the Z80 was the built-in DRAM refresh, at least in markets such as CP/M and other office and home computers. (Most Z80 embedded systems use static RAM that do not need refresh.) It may also have been its minimalistic two-level interrupt system, or conversely, its general multi-level daisy-chain interrupt system useful in servicing multiple Z80 IO chips. These features allowed systems to be built with less support hardware and simpler circuit board layouts.

However, others claim that its popularity was due to the duplicated registers that allowed fast context switches or more efficient processing of things like floating-point math compared to 8-bit CPUs with fewer registers. (The Z80 can keep several such numbers internally, using HL'HL, DE'DE and BC'BC as 32-bits registers, avoiding having to access them from slower RAM during computation.)

For the original NMOS design, the specified upper clock-frequency limit increased successively from the introductory 2.5 MHz, via the well known 4 MHz (Z80A), up to 6 MHz (Z80B) and 8 MHz (Z80H). An NMOS version was produced as a 10 MHz part beginning in the late 1980s. CMOS versions were developed with specified upper frequency limits ranging from 4 MHz up to 20 MHz for the version sold today. The CMOS versions allowed low-power standby with internal state retained, having no *lower* frequency limit. The fully compatible derivatives HD64180/Z180 and eZ80 are currently specified for up to 33 MHz and 50 MHz, respectively.


## Design

### Programming model and register set

The programming model and register set of the Z80 are fairly conventional, ultimately based on the register structure of the Datapoint 2200. The Z80 was designed as an extension of the Intel 8080, created by the same engineers, which in turn was an extension of the 8008. The 8008 was basically a PMOS implementation of the TTL-based CPU of the Datapoint 2200.

The 2200 design allowed 8-bit registers H and L (High and Low) to be paired into a 16-bit address register HL. In the 8080, this pairing was added to the BC and DE pairs as well, while HL was generalized to allow use as a 16-bit accumulator, not just an address register. The 8080 also introduced immediate 16-bit data for BC, DE, HL, and SP loads. Furthermore, direct 16-bit copying between HL and memory was now possible, using a direct address.

The Z80 orthogonalized this further by making all 16-bit register pairs, including IX and IY, more general purpose, as well as allowing 16-bit copying directly to and from memory for all of these pairs. The 16-bit IX and IY registers in the Z80 are primarily intended as base address-registers, where a particular instruction supplies a constant offset that is added to the previous values, but they are also usable as 16-bit accumulators, among other things. A limitation is that all operand references involving IX or IY require an extra instruction prefix byte, adding at least four clock cycles over the timing of an instruction using HL instead; this sometimes makes using IX or IY less efficient than a method using only the 8080-model registers. The Z80 also introduced a new signed overflow flag and complemented the fairly simple 16-bit arithmetics of the 8080 with dedicated instructions for *signed* 16-bit arithmetics.

The 8080-compatible registers AF, BC, DE, HL are duplicated as a separate register file in the Z80, where the processor can quickly (in four t-states, the least possible execution time for any Z80 instruction) switch from one bank to the other; a feature useful for speeding up responses to single-level, high-priority interrupts. The dual register-set is useful in the embedded role, as it improves interrupt handling performance, but found widespread use in the personal computer role as an additional set of general registers for complex code like floating-point arithmetic or home computer games.

The duplicate register file is often referred to as the "alternate register set" (by some, the "primed" register file since the apostrophe character is used to denote them in assembler source code and the Zilog documentation). This emphasizes that only one set is addressable at any time. However, the 8-bit accumulator A with its flag register F is bifurcated from the "general purpose" register pairs HL, DE and BC. This is accomplished with two separate instructions used to swap their accessibilities: `EX AF,AF'` exchanges only register pair AF with AF', while the `EXX` instruction exchanges the three general purpose register pairs HL, DE and BC with their alternates HL', DE' and BC'. Thus the accumulator A can interact independently with any of the general purpose 8-bit registers in the alternate (or primed) register file, or, if HL' contains a pointer to memory, some byte there (DE' and BC' can also transfer 8-bit data between memory and accumulator A).

This can become confusing for programmers because after executing `EX AF,AF'` or `EXX`, the contents of the alternate (primed) registers are now in the main registers, and vice versa. The only way for the programmer to understand and track this swapped condition is to trace through the code flow, noting each occurrence of a register swap instruction. Obviously if jump and call instructions are made within these code segments it can quickly become difficult to tell which register file is in context unless carefully commented. Thus it is advisable that exchange instructions be used directly and in short discrete code segments. The Zilog Z280 instruction set includes `JAF` and `JAR` instructions which jump to a destination address if the alternate registers are in context (thus officially recognizing this programming complication).

#### Registers

| 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 *(bit position)* **Main registers** Accumulator (A) Flags (F) **AF** B C **BC** D E **DE** H L **HL** **Alternate (shadow) registers** Accumulator' (A') Flags' (F') **AF'** B' C' **BC'** D' E' **DE'** H' L' **HL'** **Index registers** Index X **IX** Index Y **IY** Stack Pointer **SP** **Other registers** Interrupt vector Refresh counter **I/R** **Program counter** Program Counter **PC** **Status**   S Z - H - P/V N C **F**lags   IM IFF1 IFF2 **I**nterrupt |
|---|

As on the 8080, 8-bit registers are typically paired to provide 16-bit versions. The 8080 compatible registers are:

- `AF`: 8-bit accumulator (A) and flag bits (F) carry, zero, minus, parity/overflow, half-carry (used for BCD), and an Add/Subtract flag (usually called N) also for BCD
- `BC`: 16-bit data/address register or two 8-bit registers
- `DE`: 16-bit data/address register or two 8-bit registers
- `HL`: 16-bit accumulator/address register or two 8-bit registers
- `SP`: stack pointer, 16 bits
- `PC`: program counter, 16 bits

The new registers introduced with the Z80 are:

- `IX`: 16-bit index or base register for 8-bit immediate offsets
- `IY`: 16-bit index or base register for 8-bit immediate offsets
- `I`: interrupt vector base register, 8 bits
- `R`: DRAM refresh counter, 8 bits (msb does not count)
- `AF'`: alternate (or shadow) accumulator and flags (*toggled in and out with EX AF,AF'*)
- `BC'`, `DE'` and `HL'`: alternate (or shadow) registers (*toggled in and out with EXX*)
- Four bits of interrupt status: two interrupt enable flags, `IFF1` and `IFF2`, plus the two-bit interrupt mode, `IM`.

The *refresh register*, `R`, increments each time the CPU fetches an opcode (or an opcode prefix, which internally executes like a 1-byte instruction) and has no simple relationship with program execution. This has sometimes been used to generate pseudorandom numbers in games, and also in software protection schemes. It has also been employed as a "hardware" counter in some designs; an example of this is the ZX81, which lets it keep track of character positions on the TV screen by triggering an interrupt at wrap around (by connecting INT to A6).

The *interrupt vector register*, `I`, is used for the Z80 specific mode 2 interrupts (selected by the `IM 2` instruction). It supplies the high byte of the base address for a 128-entry table of service routine addresses which are selected via an index sent to the CPU during an interrupt acknowledge cycle; this index is simply the low byte part of the pointer to the tabulated indirect address pointing to the service routine. The pointer identifies a particular peripheral chip or peripheral function or event, where the chips are normally connected in a so-called daisy chain for priority resolution. Like the refresh register, this register has also sometimes been used creatively; in interrupt modes 0 and 1 (or in a system not using interrupts) it can be used as simply another 8-bit data register.

The instructions `LD A,R` and `LD A,I` affect the Z80 flags register, unlike all the other `LD` (load) instructions. The Sign (bit 7) and Zero (bit 6) flags are set according to the data loaded from the Refresh or Interrupt source registers. For both instructions, the Parity/Overflow flag (bit 2) is set according to the current state of the IFF2 flip-flop.

#### Microarchitecture

Although the Z80 is generally considered an eight-bit CPU, it has a four-bit ALU, so calculations are done in two steps.

### Z80 assembly language

#### Datapoint 2200 and Intel 8008

The first Intel 8008 assembly language was based on a simple (but systematic) syntax inherited from the Datapoint 2200 design. This original syntax was later transformed into a new, somewhat more traditional, assembly language form for this same original 8008 chip. At about the same time, the new assembly language was also extended to accommodate the additional addressing modes in the more advanced Intel 8080 chip (the 8008 and 8080 shared a language subset without being binary compatible; however, the 8008 was binary compatible with the Datapoint 2200).

In this process, the mnemonic `L`, for *LOAD*, was replaced by various abbreviations of the words *LOAD*, *STORE* and *MOVE*, intermixed with other symbolic letters. The mnemonic letter `M`, for *memory* (referenced by HL), was lifted out from within the instruction mnemonic to become a syntactically freestanding *operand*, while registers and combinations of registers became inconsistently denoted; either by abbreviated operands (MVI D, LXI H and so on), within the instruction mnemonic itself (LDA, LHLD and so on), or both at the same time (LDAX B, STAX D and so on).

| Intel 8008 Datapoint 2200 | Intel 8080 Intel 8085 | Zilog Z80 | Intel 8086/ Intel 8088 |
|---|---|---|---|
| before ca. 1973 | ca. 1974 | 1976 | 1978 |
| `LBC` | `MOV B,C` | `LD B,C` | `MOV CH,CL` |
| `--` | `LDAX B` | `LD A,(BC)` | `--` |
| `LAM` | `MOV A,M` | `LD A,(HL)` | `MOV AL,[BX]` |
| `LBM` | `MOV B,M` | `LD B,(HL)` | `MOV CH,[BX]` |
| `--` | `STAX D` | `LD (DE),A` | `--` |
| `LMA` | `MOV M,A` | `LD (HL),A` | `MOV [BX],AL` |
| `LMC` | `MOV M,C` | `LD (HL),C` | `MOV [BX],CL` |
| `LDI 56` | `MVI D,56` | `LD D,56` | `MOV DL,56` |
| `LMI 56` | `MVI M,56` | `LD (HL),56` | `MOV byte ptr [BX],56` |
| `--` | `LDA 1234` | `LD A,(1234)` | `MOV AL,[1234]` |
| `--` | `STA 1234` | `LD (1234),A` | `MOV [1234],AL` |
| `--` | `--` | `LD B,(IX+56)` | `MOV CH,[SI+56]` |
| `--` | `--` | `LD (IX+56),C` | `MOV [SI+56],CL` |
| `--` | `--` | `LD (IY+56),78` | `MOV byte ptr [DI+56],78` |
| `--` | `LXI B,1234` | `LD BC,1234` | `MOV CX,1234` |
| `--` | `LXI H,1234` | `LD HL,1234` | `MOV BX,1234` |
| `--` | `SHLD 1234` | `LD (1234),HL` | `MOV [1234],BX` |
| `--` | `LHLD 1234` | `LD HL,(1234)` | `MOV BX,[1234]` |
| `--` | `--` | `LD BC,(1234)` | `MOV CX,[1234]` |
| `--` | `--` | `LD IX,(1234)` | `MOV SI,[1234]` |

*Illustration of four syntaxes, using samples of equivalent, or (for 8086) very similar, load and store instructions. The Z80 syntax uses parentheses around an expression to indicate that the value should be used as a memory address (as mentioned below), while the 8086 syntax uses brackets instead of ordinary parentheses for this purpose. Both Z80 and 8086 use the + sign to indicate that a constant is added to a base register to form an address. Note that the 8086 is not a complete superset of the Z80. BX is the only 8086 register pair that can be used as a pointer.*

#### New syntax

Because Intel claimed a copyright on their assembly mnemonics, a new assembly syntax had to be developed for the Z80. This time a more systematic approach was used:

- All registers and register pairs are explicitly denoted by their full names
- Parentheses are consistently used to indicate "memory contents at" (constant address or variable pointer dereferencing) with the exception the jump instructions `JP (HL)`, `JP (IX)`, and `JP (IY)` which imply an effective address. These load the new PC address from the respective register directly, without indirecting through memory.
- All load and store instructions use the same mnemonic name, LD, for LOAD (a return to the simplistic Datapoint 2200 vocabulary); other common instructions, such as ADD and INC, use the same mnemonic regardless of addressing mode or operand size. This is possible because the operands themselves carry enough information to determine the specific opcode.

These principles made it straightforward to find names and forms for all new Z80 instructions, as well as orthogonalizations of old ones, such as `LD BC,1234`.

There was at least one inconsistency introduced. Even though a subtract with carry is coded as `SBC A,r`, the non-carry subtract is coded as `SUB r` rather than `SUB A,r`.

Apart from naming differences, and despite a certain discrepancy in basic register structure, the Z80 and 8086 syntax are virtually isomorphic for a large portion of instructions. Only quite superficial similarities (such as the word MOV, or the letter X, for extended register) exist between the 8080 and 8086 assembly languages, although 8080 programs can be translated to 8086 assembly language by translator programs.

### Instruction set and encoding

The Z80 uses 252 out of the available 256 codes as single byte opcodes ("root instruction" most of which are inherited from the 8080); the four remaining codes are used extensively as opcode prefixes: CB and ED enable extra instructions, and DD or FD select IX+d or IY+d respectively (in some cases without displacement d) in place of HL. This scheme gives the Z80 a large number of permutations of instructions and registers; Zilog categorizes these into 158 different "instruction types", 78 of which are the same as those of the Intel 8080 (allowing operation of all 8080 programs on a Z80). The Zilog documentation further groups instructions into the following categories (most from the 8080, others entirely new like the block and bit instructions, and others 8080 instructions with more versatile addressing modes, like the 16-bit loads, I/O, rotates/shifts and relative jumps):

- Load and exchange
- Block transfer and search
- Arithmetic and logical
- Rotate and shift
- Bit manipulation (set, reset, test)
- Jump, call and return
- Input/output
- Basic CPU control

No explicit multiply instructions are available in the original Z80, though registers A and HL can be multiplied by powers of two with ADD A,A and ADD HL,HL instructions (similarly IX and IY also). Shift instructions can also multiply or divide by powers of two.

Different sizes and variants of additions, shifts, and rotates have somewhat differing effects on flags because most of the flag-changing properties of the 8080 were copied. However, the parity flag bit P of the 8080 (bit 2) is called P/V (parity/overflow) in the Z80 as it serves the additional purpose of a twos complement overflow indicator, a feature lacking in the 8080. Arithmetic instructions on the Z80 set it to indicate overflow rather than parity, while bitwise instructions still use it as a parity flag. (This introduces a subtle incompatibility of the Z80 with code written for the 8080, as the Z80 sometimes indicates signed overflow where the 8080 would indicate parity, possibly causing the logic of some practical 8080 software to fail on the Z80.) This new overflow flag is used for all new Z80-specific 16-bit operations (`ADC`, `SBC`) as well as for 8-bit arithmetic operations, while the 16-bit operations inherited from the 8080 (`ADD`, `INC`, `DEC`) do not affect it. Also, bit 1 of the flags register (a spare bit on the 8080) is used as a flag N that indicates whether the last arithmetic instruction executed was a subtraction or addition. The Z80 version of the `DAA` instruction (decimal adjust accumulator for BCD arithmetic) checks the N flag and behaves accordingly, so a (hypothetical) subtraction followed later by `DAA` will yield a different result on an old 8080 than on the Z80. However, this would likely be erroneous code on the 8080, as `DAA` was defined for addition only on that processor.

The Z80 has six new `LD` instructions that can load the DE, BC, and SP register pairs from memory, and load memory from these three register pairs—unlike the 8080. As on the 8080, load instructions do not affect the flags (except for the special-purpose I and R register loads). A result of a regular encoding (common with the 8080) is that each of the 8-bit registers can be loaded from themselves (e.g. `LD A,A`). This is effectively a `NOP`.

New block transfer instructions can move up to 64 kilobytes from memory to memory or between memory and I/O peripheral ports. Block instructions `LDIR` and `LDDR` (**l**oa**d**, **i**ncrement/**d**ecrement, **r**epeat) use HL to point to the source address, DE to the destination address, and BC as a byte counter. Bytes are copied from source to destination, the pointers are incremented or decremented, and the byte counter is decremented until BC reaches zero. Non-repeating versions `LDI` and `LDD` move a single byte and bump the pointers and byte counter, which if it becomes zero resets the P/V flag. Corresponding memory-to-I/O instructions `INIR`, `INDR`, `OTIR`, `OTDR`, `INI`, `IND`, `OUTI` and `OUTD` operate similarly, except that B, not BC, is used as the byte counter. The Z80 can input and output any register to an I/O port using register C to designate the port. (The 8080 only performs I/O through the accumulator A, using a direct port address specified in the instruction; a self-modifying code technique is required to use a variable 8080 port address.)

The last group of block instructions perform a `CP` compare operation between the byte at (HL) and the accumulator A. Register pair DE is not used. The repeating versions `CPIR` and `CPDR` only terminate if BC goes to zero or a match is found. HL is left pointing to the byte after (`CPIR`) or before (`CPDR`) the matching byte. If no match is found, the Z flag is reset. There are non-repeating versions `CPI` and `CPD`.

Unlike the 8080, the Z80 can jump to a relative address (`JR` instead of `JP`) using a shorter instruction with a signed 8-bit displacement. There are unconditional and conditional forms of this instruction. Only the zero and carry conditions can be tested. (All 8080 jumps and calls, conditional or not, are three-byte instructions.) If jump is taken, the two-byte `JR` instructions are slower than the 8080-style three-byte `JP` instructions; if not taken, `JR` instructions are quicker.

A two-byte instruction specialized for program looping is also new to the Z80: `DJNZ` (**d**ecrement **j**ump if **n**on-**z**ero) takes a signed 8-bit displacement as an operand. The B register is decremented, and if the result is nonzero, then program execution jumps relative to PC; the flags remain unaltered. To perform an equivalent loop on an 8080 requires separate `DEC` and conditional jump (to a two-byte absolute address) instructions (totalling four bytes), and the `DEC` alters the flag register.

The index register (IX/IY, often abbreviated XY) instructions can be useful for accessing data organised in fixed heterogenous structures (such as records) or at fixed offsets relative a variable base address (as in recursive stack frames) and can also reduce code size by removing the need for multiple short instructions using non-indexed registers. However, although they may save speed in some contexts when compared to long/complex "equivalent" sequences of simpler operations, they incur a lot of additional CPU time (e.g., 19 T-states to access one indexed memory location vs. as little as 11 to access the same memory using HL and `INC` to point to the next). Thus, for simple or linear accesses of data, use of IX and IY tend to be slower and occupy more memory. Still, they may be useful in cases where the "main" registers are all occupied, by removing the need to save/restore registers. Their officially undocumented 8-bit halves (see below) can be especially useful in this context, for they incur less slowdown than their 16-bit parents. Similarly, instructions for 16-bit additions are not particularly fast (11 clocks) in the original Z80 (being 1 clock slower than in the 8080/8085); nonetheless, they are about twice as fast as performing the same calculations using 8-bit operations, and equally important, they reduce register usage. It was not uncommon for programmers to "poke" different offset displacement bytes (which were typically calculated dynamically) into indexed instructions; this is an example of self-modifying code, which was regular practice on nearly all early 8-bit processors with non-pipelined execution units.

The index registers have a parallel instruction to `JP (HL)`, which is `JP (IX)` and `JP (IY)`. This is often seen in stack-oriented languages like Forth, which at the end of every Forth word (atomic subroutines comprising the language) must jump unconditionally back to their thread interpreter routines. Typically this jump instruction appears hundreds of times in an application, and using `JP (IX)` rather than `JP THREAD` saves a byte and two T-states for each occurrence. This naturally makes the index register unavailable for any other use, or else the need to constantly reload it would negate its efficiency.

The 10-year-newer microcoded Z180 design could initially afford more "chip area", permitting a slightly more efficient implementation (using a wider ALU, among other things); similar things can be said for the Z800, Z280, and Z380. However, it was not until the fully pipelined eZ80 was launched in 2001 that those instructions finally became approximately as cycle-efficient as it is technically possible to make them, i.e. given the Z80 encodings combined with the capability to do an 8-bit read or write every clock cycle.

#### Undocumented instructions

The index registers, IX and IY, were intended as flexible 16-bit pointers, enhancing the ability to manipulate memory, stack frames and data structures. Officially, they were treated as 16-bit only. In reality they were implemented as a pair of 8-bit registers, in the same fashion as the HL register, which is accessible either as 16 bits or separately as the *H*igh and *L*ow registers. The binary opcodes (machine language) were identical, but preceded by a new opcode prefix. Zilog published the opcodes and related mnemonics for the intended functions, but did not document the fact that every opcode that allowed manipulation of the H and L registers was equally valid for the 8 bit portions of the IX and IY registers. For example, the opcode 26h followed by an immediate byte value `(LD H,n)` will load that value into the H register. Preceding this two-byte instruction with the IX register's opcode prefix, DD, would instead result in the most significant 8 bits of the IX register being loaded with that same value. A notable exception to this would be instructions similar to `LD H,(IX+d)` which make use of both the HL and IX or IY registers in the same instruction; in this case the DD prefix is only applied to the (IX+d) portion of the instruction. The halves of the XY registers could also hold operands for 8-bit arithmetic, logical and compare instructions, sparing the regular 8-bit registers for other use. The undocumented ability to increment and decrement the upper half of an index register made it easy to expand the range of the normal indexed instructions, without having to resort to the documented `ADD/SBC XY,DE` or `ADD/SBC XY,BC`.

There are several other undocumented instructions as well. Undocumented or illegal opcodes are not detected by the Z80 and have various effects, some of which are useful. However, as they are not part of the formal definition of the instruction set, different implementations of the Z80 are not guaranteed (or especially likely) to work the same way for every undocumented opcode.

#### Bugs

The `OTDR` instruction does not conform to the Z80 documentation. Both the `OTDR` and `OTIR` instructions are supposed to leave the carry (C) flag unmodified. The `OTIR` instruction operates correctly; however, during the execution of the `OTDR` instruction, the carry flag takes the results of a spurious compare between the accumulator (A) and the last output of the `OTDR` instruction.

### Example code

The following Z80 assembly source code is for a subroutine named `memcpy` that copies a block of data bytes of a given size from one location to another. The data block is copied one byte at a time, and the data movement and looping logic utilizes 16-bit operations. It demonstrates a variety of instructions but in practice it would not be coded this way as the Z80 has a single instruction that could replace this entire subroutine: `LDIR`. The sample code will move one byte every 46 T-states. Substituting the `LDIR` instruction will move each byte in only 21 T-states. Note that the assembled code is binary-compatible with the Intel 8080 and 8085 CPUs.

| 1000 1000 1000 F5 1001 7E 1002 12 1003 23 1004 13 1005 0B 1006 78 1007 B1 1008 C2 01 10 100B F1 100C C9 100D | ; memcpy -- ; Copy a block of memory from one location to another. ; This routine is the equivalent of LDIR ; ; Entry registers ; HL - Address of source data block ; DE - Address of destination data block ; BC - Number of bytes to copy ; ; Return registers ; HL - First byte after source data block ; DE - First byte after destination data block ; BC - Zero ; (LDIR does not fully save AF. H, P/V, and N are reset.) org 1000h ; Origin at 1000h memcpy public push af ; Save AF like LDIR loop ld a,(hl) ; Copy 1 source byte ld (de),a ; to its destination inc hl ; Bump source pointer inc de ; Bump dest pointer dec bc ; Count the copied byte ld a,b ; Test BC for zero or c ; If BC != 0, jp nz,loop ; repeat the loop pop af ; Restore AF ret ; Return end |
|---|---|

### Instruction execution

Each instruction is executed in steps that are usually termed machine cycles (M-cycles), each of which can take between three and six clock periods (T-states). Each M-cycle corresponds roughly to one memory access or internal operation. Multiple instructions actually end during the M1 of the *next* instruction which is known as a *fetch/execute overlap*.

Examples of typical instructions (R=read, W=write)

Total

M-cycles

T-states

instruction

M1

M2

M3

M4

M5

M6

1

4

INC

B

opcode

2

7

ADD

A

,

n

opcode

n

3

11

ADD

HL

,

DE

opcode

internal

internal

4

15

SET

b

,(

HL

)

prefix

opcode

R(HL), set

W(HL)

5

19

LD

(

IX

+

d

),

n

prefix

opcode

d

n,add

W(IX+d)

6

23

INC

(

IY

+

d

)

prefix

opcode

d

add

R(IY+d),inc

W(IY+d)

The Z80 machine cycles are sequenced by an internal state machine which builds each M-cycle out of 3, 4, 5 or 6 T-states depending on context. This avoids cumbersome asynchronous logic and makes the control signals behave consistently at a wide range of clock frequencies. It also means that a higher frequency crystal must be used than without this subdivision of machine cycles (approximately 2–3 times higher). It does not imply tighter requirements on memory access times, since a high resolution clock allows more precise control of memory timings and so memory can be active in parallel with the CPU to a greater extent, allowing more efficient use of available memory bandwidth.

One central example of this is that, for opcode fetch, the Z80 combines two full clock cycles into a memory access period (the M1-signal). In the Z80 this signal lasts for a relatively larger part of the typical instruction execution time than in a design such as the 6800, 6502, or similar, where this period would typically last typically 30-40% of a clock cycle. With memory chip affordability (i.e. access times around 450-250 ns in the 1980s) typically determining the fastest possible access time, this meant that such designs were locked to a significantly longer clock cycle (i.e. lower internal clock speed) than the Z80.

Memory was generally slow compared to the state machine sub-cycles (clock cycles) used in contemporary microprocessors. The shortest machine cycle that could safely be used in embedded designs has therefore often been limited by memory access times, not by the maximum CPU frequency (especially so during the home computer era). However, this relation has slowly changed during the last decades, particularly regarding SRAM; cacheless, single-cycle designs such as the eZ80 have therefore become much more meaningful recently.

The content of the refresh register R is sent out on the lower half of the address bus along with a refresh control signal while the CPU is decoding and executing the fetched instruction. During refresh the contents of the Interrupt register I are sent out on the upper half of the address bus.

### Compatible peripherals

Zilog introduced a number of peripheral parts for the Z80, which all support the Z80's interrupt handling system and I/O address space. These include the counter/timer channel (CTC), the SIO (serial input/output), the DMA (direct memory access), the PIO (parallel input/output) and the DART (dual asynchronous receiver–transmitter). As the product line developed, low-power, high-speed and CMOS versions of these chips were introduced.

- (PIO Z84C2008) PIO Z84C2008
- (CTC Z84C3008) CTC Z84C3008
- (SIO Z84C4008) SIO Z84C4008

Like the 8080, 8085 and 8086 processors, but unlike processors such as the Motorola 6800 and MOS Technology 6502, the Z80 and 8080 has a separate control line and address space for I/O instructions. While some Z80-based computers such as the Osborne 1 used "Motorola-style" memory mapped input/output devices, usually the I/O space was used to address one of the Zilog peripheral chips compatible with the Z80. During the timing for an I/O read or an I/O write operation, a single wait cycle is automatically inserted by the Z80. Zilog I/O chips supported the Z80's new mode 2 interrupts which simplified interrupt handling for large numbers of peripherals.

The Z80 was officially described as supporting 16-bit (64 KB) memory addressing, and 8-bit (256 ports) I/O-addressing. All I/O instructions actually assert the entire 16-bit address bus. OUT (C),reg and IN reg,(C) places the contents of the entire 16-bit BC register on the address bus; OUT (n),A and IN A,(n) places the contents of the A register on b8–b15 of the address bus and the port address *n* on b0–b7 of the address bus. A designer could choose to decode the entire 16-bit address bus on I/O operations in order to take advantage of this feature, or use the high half of the address bus to select subfeatures of the I/O device. This feature has also been used to minimise decoding hardware requirements, such as in the Amstrad CPC/PCW and ZX81.
