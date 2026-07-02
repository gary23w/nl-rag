---
title: "Zilog Z80 (part 2/2)"
source: https://en.wikipedia.org/wiki/Zilog_Z80
domain: retro-z80-assembly
license: CC-BY-SA-4.0
tags: z80 assembly, zilog z80, z80 opcode, intel 8080
fetched: 2026-07-02
part: 2/2
---

## Second sources and derivatives

### Second sources

Mostek, which produced the first Z80 for Zilog, offered it second-source as MK3880. SGS-Thomson (now STMicroelectronics) was a second source, too, with their Z8400. Sharp and NEC developed second sources for the NMOS Z80, the LH0080 and μPD780C, respectively. The LH0080 was used in various home computers and personal computers made by Sharp and other Japanese manufacturers, including Sony MSX computers, and a number of computers in the Sharp MZ series. Sharp developed the LH0080A and LH0080B to operate at frequencies of 4 MHz and 6 MHz, respectively. Sharp also developed LH0083 compatible with Z80 DMA.

Toshiba made a CMOS-version, the TMPZ84C00, which is believed (but not verified) to be the same design also used by Zilog for its own CMOS Z84C00. There were also Z8400, Z80-chips made by GoldStar (now LG) and the BU18400 series of Z80-clones (including DMA, PIO, CTC, DART and SIO) in NMOS and CMOS made by ROHM Electronics. The LH5080, LH5081, and LH5082, which are CMOS versions of the Z80, PIO, and CTC respectively, are manufactured by Sharp.

In East Germany, an unlicensed clone of the Z80, known as the U880, was manufactured. It was used extensively in Robotron's and VEB Mikroelektronik Mühlhausen's computer systems (such as the KC85-series) and also in multiple self-made computer systems. In Romania another unlicensed clone could be found, named MMN80CPU and produced by Microelectronica, used in home computers like TIM-S, HC, COBRA.

Also, several clones of Z80 were created in the Soviet Union, notable ones being the T34BM1, also called КР1858ВМ1 (parallelling the Soviet 8080-clone KR580VM80A). The first marking was used in pre-production series, while the second had to be used for a larger production. Though, due to the collapse of Soviet microelectronics in the late 1980s, there are more T34BM1s than КР1858ВМ1s.

- (Mostek Z80: MK3880) Mostek Z80: MK3880
- (NEC μPD780C) NEC μPD780C
- (Sharp LH0080) Sharp LH0080
- (Toshiba Z84C00) Toshiba Z84C00
- (East Germany RFT U880D) East Germany RFT U880D
- (Soviet T34BM1 Z80 clone) Soviet T34BM1 Z80 clone

### Derivatives

**Compatible with the original Z80**

- Hitachi developed the HD64180, a microcoded and partially dynamic Z80 in CMOS, with on-chip peripherals and a simple MMU, giving a 1 MB address space. It was later second sourced by Zilog, initially as the Z64180, and then in the form of the slightly modified Zilog Z180 which has bus protocol and timings better adapted to Z80 peripheral chips. Z180 has been maintained and further developed under Zilog's name, the newest versions being based on the fully static S180/L180 core with low power draw and EMI (noise).
- Toshiba developed the 84-pin Z84013 / Z84C13 and the 100 pin Z84015 / Z84C15 series of "intelligent peripheral controllers", basically ordinary NMOS and CMOS Z80 cores with Z80 peripherals, watchdog timer, power on reset, and wait state generator on the same chip. Manufactured by Sharp as well as Toshiba. These products are today second sourced by Zilog.
- The 32-bit Z80 compatible Zilog Z380, introduced 1994, is used in telecom equipment.
- Zilog's fully pipelined Z80 compatible eZ80 with an 8/16/24-bit word length and a linear 16 MB address space was introduced in 2001. It exists in versions with on-chip SRAM or Flash memory, as well as with integrated peripherals. One variant has an on-chip medium access controller (MAC), and available software include a TCP/IP stack. In contrast with the Z800 and Z280, there are only a few added instructions (primarily load Effective Address (LEA), Push Effective Address (PEA), and variable-address 16/24-bit loads), but instructions are instead executed between 2 and 11 times as clock cycle efficiently as on the original Z80, with a mean value around 3-5 times. It is currently specified for clock frequencies up to 50 MHz.
- Kawasaki developed the binary compatible KL5C8400 which is approximately 1.2-1.3 times as clock cycle efficient as the original Z80 and can be clocked at up to 33 MHz. Kawasaki also produces the KL5C80A1x family, which has peripherals as well as a small RAM on chip; it is approximately as clock cycle efficient as the eZ80 and can be clocked at up to 10 MHz (2006).
- The NEC μPD9002 was a hybrid CPU compatible with both Z80 and x86 families.
- The Chinese Actions Semiconductor's audio processor family of chips (ATJ2085 and others) contains a Z80-compatible MCUs together with a 24-bit dedicated DSP processor. These chips are used in a number of MP3 and media player products.
- The T80 (VHDL) and TV80 (Verilog) synthesizable soft cores are available from OpenCores.org.
- The National Semiconductor NSC800 announced in 1980 is used in multiple TeleSecurity Timmann (TST) electronic cipher machines and the Canon X-07. The NSC800 is fully compatible with the Z80 instruction set. The NSC800 uses a multiplexed bus like the 8085 but has a different pinout than the Z80.

**Non-compatible**

- The Toshiba TLCS 900 series of high volume, mostly one-time programmable microcontrollers are based on the Z80. They share the same basic BC,DE,HL,IX,IY register structure, and largely the same instructions, but are not binary compatible, while the previous TLCS 90 is Z80-compatible.
- The NEC 78K series microcontrollers are based on the Z80. They share the same basic BC,DE,HL register structure, and has similar, but differently named instructions; not binary compatible.

**Partly compatible**

- Rabbit Semiconductor's Rabbit 2000/3000/4000 microprocessors/microcontrollers are based on the HD64180/Z180 architecture, although they are not fully binary compatible.

**No longer produced**

- The ASCII Corporation R800 was a fast 16-bit processor used in MSX TurboR computers; it was software-, but not hardware-compatible with the Z80 (signal timing, pinout and function of pins differ from the Z80).
- Zilog's NMOS Z800 and CMOS Z280 were 16-bit Z80 implementations (before the HD64180/Z180) with a 16 MB-paged MMU address space; they added multiple orthogonalizations and addressing modes to the Z80 instruction set. Minicomputer features — such as user and system modes, multiprocessor support, on chip MMU, on chip instruction and data cache, and so on — were seen rather as more complexity than as functionality and support for the (usually electronics-oriented) embedded systems designer; it also made it hard to predict instruction execution times.
- Certain arcade games, such as Pang/Buster Bros., use an encrypted "Kabuki" Z80 CPU manufactured by VLSI Technology, where the decryption keys are stored in its internal battery-backed memory, to avoid piracy and illegal bootleg games.

- (ASCII R800) ASCII R800
- (Hitachi HD64180) Hitachi HD64180
- (Zilog Z180) Zilog Z180
- (Zilog Z280) Zilog Z280
- (Toshiba TMPZ84C015) Toshiba TMPZ84C015


## Notable uses

### Desktop computers

During the late 1970s and early 1980s, the Z80 was used in a great number of fairly anonymous business-oriented machines with the CP/M operating system, a combination that dominated the market at the time. Four well-known examples of Z80 business computers running CP/M are the Heathkit H89, the portable Osborne 1, the Kaypro series, and the Epson QX-10. Less well-known was the expensive high-end Otrona Attache. Some systems used multi-tasking operating system software (like MP/M or Morrow's Micronix) to share the one processor between several concurrent users.

Multiple home computers were introduced that used the Z80 as the main processor or as a plug-in option to allow access to software written for the Z80. Notable are the TRS-80 series, including the original model (later retronymed "Model I"), Model II, Model III, and Model 4, which were equipped with a Z80 as their main processor, and some (but not all) other TRS-80 models which used the Z80 as either the main or a secondary processor. Other notable machines were the DEC Rainbow 100, and the Seequa Chameleon, both of which featured both an Intel 8088 and a Z80 CPU, to support either 8-bit CP/M-80 applications running on the Z80, or a custom MS-DOS that was not fully compatible with PC DOS applications running on the 8088.

In 1981, Multitech (later to become Acer) introduced the Microprofessor I, a simple and inexpensive training system for the Z80 microprocessor. Currently, it is still manufactured and sold by Flite Electronics International Limited in Southampton, England.

In 1984 Toshiba introduced the Toshiba MSX HX-10 in Japan and Australia.

In 1985, Sharp introduced the Hotbit and Gradiente introduced the Expert, which became the dominant 8-bit home computers in Brazil until the late 1980s.

### Portable and handheld computers

Use of the Z80 in lighter, battery-operated devices became more widespread with the availability of CMOS versions of the processor. It also inspired the development of other CMOS based processors, such as the LH5801 from Sharp. The Sharp PC-1500, a BASIC-programmable pocket computer was released in 1981, followed by the improved Sharp PC-1600 in 1986 and the Sharp PC-E220 in 1991. Later models of the Sharp Wizard series of personal organizers also were Z80 based. Laptops which could run the CP/M operating system just like the desktop machines followed with Epson PX-8 Geneva in 1984, and in 1985 the Epson PX-4 and Bondwell-2. While the laptop market in subsequent years moved to more powerful Intel 8086 processors and the MS-DOS operating system, light-weight Z80-based systems with a longer battery life were still being introduced, such as the Cambridge Z88 in 1988 and the Amstrad NC100 in 1992. The Z80-derived Z8S180 also found its way into an early pen-operated personal digital assistant, the Amstrad PenPad PDA600 in 1993. Hong Kong-based VTech produced a line of small laptop computers called "Lasers" based on a Z80. The last two were the Laser PC5 and PC6. The Cidco MailStation Mivo 100, first released in 1999, was a stand-alone portable email device, with a Z80-based microcontroller. Texas Instruments produced a line of pocket organizers (ending in 2000) using Toshiba processors built around a Z80 core; the first of these was the TI PS-6200 and after a lengthy production run of some dozen models culminated in their PocketMate series.

### Embedded systems and consumer electronics

The Zilog Z80 has long been a popular microprocessor in embedded systems and microcontroller cores, where it remains in widespread use today. Applications of the Z80 include uses in consumer electronics, industrial products, and electronic musical instruments. For example, Z80 was used in the groundbreaking music synthesizer Prophet-5, as well as in the first MIDI-equipped synthesizer, the Prophet 600. The Z80 was the basis for all E-mu Systems instruments from 1976 to 1986. Casio used the Z80A in its PV-1000 video game console.

Many early-1980s arcade video games, including the arcade game Pac-Man, contain Z80 CPUs.

The Z80 was used in Sega's Master System and Game Gear consoles. The Sega Genesis contains a Z80, with its own 8 KB of RAM, which runs in parallel with the MC68000 main CPU, has direct access to the system's sound chips and I/O (controller) ports, and has a switched data path to the main memory bus of the 68000 (providing access to the 64 KB main RAM, the software cartridge, and the whole video chip); in addition to providing backward compatibility with Master System games, the Z80 is often used to control and play back audio in Genesis software.

Z80 CPUs were also used in the popular TI-8x series of graphing calculators from Texas Instruments, beginning in 1990 with the TI-81, which features a Z80 clocked at 2 MHz. Most higher-line calculators in the series, starting with the TI-82 and TI-85, clock their Z80 CPUs at 6 MHz or higher. (A few models with TI-8x names use other CPUs, such as the M68000, but the vast majority are Z80-based. On those, it is possible to run assembled or compiled user programs in the form of Z80 machine-language code.)

TI-83 and TI-84 Plus model graphing calculators uses the Z80 while the TI-84 Plus CE series use the eZ80; all three calculator series are still sold by Texas Instruments as of 2025.

In the late 1980s, a series of Soviet landline phones called "AON" featured the Z80; these phones expanded the feature set of the landline with caller ID, different ringtones based on the caller, speed dial and so forth. In the second half of the 1990s however, manufacturers of these phones switched to 8051 compatible MCUs to reduce power consumption, and prevent compact wall power adapters from overheating.

Early Micromouse autonomous maze-solving mobile robots used the Z80 CPU, such as the Moonlight Special (1978), that utilized a 4 MHz Z80A to minimize onboard hardware by leveraging its single +5V power supply requirement. The design relied on the processor's new block transfer instructions to manage maze node tables and its vectored interrupts to handle real-time sensor sampling and stepper motor control within a tight 4 kHz (250 µsec) interrupt cycle.


## Discontinuation

On April 15, 2024, Zilog announced the discontinuation of the Z80 processor, with orders being accepted until June 14, 2024. The announcement included 13 variants of the Z80 processor, some of which were DIP40 variants of the chip. Zilog will continue to manufacture the upgraded eZ80 version of the processor.
