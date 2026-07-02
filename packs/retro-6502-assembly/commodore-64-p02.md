---
title: "Commodore 64 (part 2/2)"
source: https://en.wikipedia.org/wiki/Commodore_64
domain: retro-6502-assembly
license: CC-BY-SA-4.0
tags: 6502 assembly, mos 6502, 6502 opcode, 6502 processor
fetched: 2026-07-02
part: 2/2
---

## Hardware

### CPU and memory

The C64 uses an 8-bit MOS Technology 6510 microprocessor that is almost identical to the 6502 but has three-state buses, a different pinout, slightly different clock signals and other minor changes for this application. It also has six I/O lines on otherwise-unused legs on the 40-pin IC package. These are used for two purposes in the C64: to bank-switch the machine's read-only memory (ROM) in and out of the processor's address space, and to operate the datasette tape recorder. The C64 has 64 KB of 8-bit-wide dynamic RAM, 1 KB of 4-bit-wide static color RAM for text mode, and 38 KB are available to built-in Commodore BASIC 2.0 on startup. There is 20 KB of ROM, made up of the BASIC interpreter, the KERNAL, and the character ROM. Because the processor can only address 64 KB at a time, the ROM was mapped into memory and only 38911 bytes of RAM (plus 4 KB between the ROMs) were available at startup. Most "breadbin" Commodore 64s used 4164 DRAM with eight chips totaling 64K of system RAM. Later models, featuring Assy 250466 and Assy 250469 motherboards, used 41464 DRAM (64K×4) chips which stored 32 KB per chip (so only two were required). Because 4164 DRAMs are 64K×1, eight chips are needed to make an entire byte; the computer will not function without all of them present. The first chip contains Bit 0 for the memory space, the second chip contains Bit 1, and so forth.

The C64 performs a RAM test on power-up and if a RAM error is detected, the amount of free BASIC memory will be lower than the normal 38,911. If the faulty chip is in lower memory, then an `?OUT OF MEMORY IN 0` error is displayed rather than the usual BASIC startup banner.

The C64 uses a complicated memory-banking scheme; the normal power-on default is the BASIC ROM mapped in at $A000–$BFFF, and the screen editor (KERNAL) ROM at $E000–$FFFF. RAM under the system ROMs can be written to, but not read back, without swapping out the ROMs. Memory location $01 contains a register with control bits for enabling or disabling the system ROMs and the I/O area at $D000. If the KERNAL ROM is swapped out, BASIC will be removed at the same time. BASIC is not active without the KERNAL; BASIC often calls KERNAL routines, and part of the ROM code for BASIC is in the KERNAL ROM.

The character ROM is normally invisible to the CPU. The character ROM may be mapped into $D000–$DFFF, where it is then visible to the CPU. Because doing so necessitates swapping out the I/O registers, interrupts must first be disabled. By removing I/O from the memory map, $D000–$DFFF becomes free RAM.

C64 cartridges map into assigned ranges in the CPU's address space. The most common cartridge auto-starting requires a string at $8000 which contains "CBM80" followed by the address where program execution begins. A few C64 cartridges released in 1982 use Ultimax mode (or MAX mode), a leftover feature of the unsuccessful MAX Machine. These cartridges map into $F000 and displace the KERNAL ROM. If Ultimax mode is used, the programmer will have to provide code for handling system interrupts. The cartridge port has 16 address lines, which grants access to the computer's entire address space if needed. Disk and tape software normally load at the start of BASIC memory ($0801), and use a small BASIC stub (such as `10 SYS(2064)`) to jump to the start of the program. Although no Commodore 8-bit machine except the C128 can automatically boot from a floppy disk, some software intentionally overwrites certain BASIC vectors in the process of loading so execution begins automatically (instead of requiring the user to type RUN at the BASIC prompt after loading).

About 300 cartridges were released for the C64, primarily during the machine's first 2+1⁄2 years on the market, after which most software outgrew the 16 KB cartridge limit. One notable third-party expansion was the Power Cartridge, developed by Dutch company Kolff Computer Supplies (KCS). It provided a BASIC extension toolkit, a machine code monitor, a reset button, and fastload routines that accelerated cassette and disk access (up to 10× and 6× respectively). Popular in the Benelux region, it was used for both productivity and programming purposes. Larger software companies, such as Ocean Software, began releasing games on bank-switched cartridges to overcome the 16 KB cartridge limit during the C64's final years.

Commodore did not include a reset button on its computers until the CBM-II line, but third-party cartridges had a reset button. A soft reset can be triggered by jumping to the CPU reset routine at $FCE2 (64738). A few programs use this as an exit feature, although it does not clear memory.

The KERNAL ROM underwent three revisions, mainly designed to fix bugs. The initial version is only found on 326298 motherboards (used in the first production models), and cannot detect whether an NTSC or PAL VIC-II is present. The second revision is found on all C64s made from late 1982 through 1985. The final KERNAL ROM revision was introduced on the 250466 motherboard (late breadbin models with 41464 RAM), and is found in all C64Cs. The 6510 CPU is clocked at 1.023 MHz (NTSC) and 0.985 MHz (PAL), lower than some competing systems; the Atari 800, for example, is clocked at 1.79 MHz). Performance can be boosted slightly by disabling the VIC-II's video output via a register write. This feature is often used by tape and disk fast loaders and the KERNAL cassette routine to keep a standard CPU cycle timing not modified by the VIC-II's sharing of the bus.

The restore key is gated directly to the CPU's NMI line, and will generate an NMI if pressed. The KERNAL handler for the NMI checks if run/stop is also pressed; if not, it ignores the NMI and exits. Run/stop-restore is normally a soft reset in BASIC which restores all I/O registers to their power-on default state, but does not clear memory or reset pointers; any BASIC programs in memory will be left untouched. Machine-language software usually disables run/stop-restore by remapping the NMI vector to a dummy RTI instruction. The NMI can also be used for an extra interrupt thread by programs, but risks a system lockup or other undesirable side effects if the restore key is accidentally pressed (which activates the NMI thread).

### Joysticks, mice, and paddles

(from top)

Commodore's version of the Atari joystick; a set of analog paddles; a 1350/1351 mouse, and DE-9 Atari-style joystick ports

The C64 retained the VIC-20's DE-9 Atari joystick port and added another; any Atari-specification game controller can be used on a C64. The joysticks are read from the registers at $DC00 and $DC01, and most software is designed to use a joystick in port 2 for control rather than port 1; the upper bits of $DC00 are used by the keyboard, and an I/O conflict can result. Although it is possible to use Sega gamepads on a C64, it is not recommended; their slightly different signal can damage the CIA chip. The SID chip's register $D419, used to control paddles, is an analog input. A handful of games, primarily released early in the computer's life cycle, can use paddles. In 1986, Commodore released two mice for the C64 and C128: the 1350 and 1351. The 1350 is a digital device read from the joystick registers, and can be used with any program supporting joystick input. The 1351 is an analog potentiometer-based mouse, read with the SID's analog-to-digital converter.

### Graphics

The VIC-II graphics chip features a new palette, eight hardware sprites per scanline (enabling up to 112 sprites per PAL screen), scrolling capabilities, and two bitmap graphics modes.

| Color # | Name | Hexadecimal RGB value |
|---|---|---|
| 0 | Black | #000000 |
| 1 | White | #FFFFFF |
| 2 | Red | #9F4E44 |
| 3 | Cyan | #6ABFC6 |
| 4 | Purple | #A057A3 |
| 5 | Green | #5CAB5E |
| 6 | Blue | #50459B |
| 7 | Yellow | #C9D487 |
| 8 | Orange | #A1683C |
| 9 | Brown | #6D5412 |
| 10 | Light Red | #CB7E75 |
| 11 | Dark-Gray | #626262 |
| 12 | Mid-Gray | #898989 |
| 13 | Light Green | #9AE29B |
| 14 | Light Blue | #887ECB |
| 15 | Light-Gray | #ADADAD |

### Text modes

The standard text mode features 40 columns, like most Commodore PET models; the built-in character encoding is not standard ASCII but PETSCII, an extended form of ASCII-1963. The KERNAL ROM sets the VIC-II to a dark-blue background on power-up, with a light-blue border and text. Unlike the PET and VIC-20, the C64 uses double-width text; some early VIC-IIs had poor video quality which resulted in a fuzzy picture. Most screenshots show borders around the screen, a feature of the VIC-II chip. By utilizing interrupts to reset hardware registers with precise timing, it was possible to place graphics within the borders and use the full screen.

The C64 has a resolution of 320×200 pixels, consisting of a 40×25 grid of 8×8 character blocks. It has 256 predefined character blocks, known as PETSCII. The character set can be copied into RAM and modified by a programmer.

There are three color modes: *high resolution*, with two colors available per character block (one foreground and one background), *multicolor* (four colors per character block – three foreground and one background), and *extended color* (each individual character on the text screen may have one of four different background colors; the trade-off is that the character set is limited to the first 64 characters in the character set). In multicolor mode, attributes are shared between pixel pairs so the effective visible resolution is 160×200 pixels; only 16 KiB of memory is available for the VIC-II video processor.

Since the C64 has a bitmapped screen, it is possible (but slow) to draw each pixel individually. Most programmers used techniques developed for earlier, non-bitmapped systems like the Commodore PET and TRS-80. A programmer redraws the character set, and the video processor fills the screen block by block from the top left corner to the bottom right corner. Two types of animation are used: character block animation and hardware sprites.

#### Character block animation

The user draws a series of characters of a person walking, possibly two in the middle of the block and another two walking in and out of the block. Then the user sequences them so the character walks into the block and out again. Drawing a series of these gets a person walking across the screen. By timing the redraw to occur when the television screen blanks out to restart drawing the screen, there will be no flicker. For this to happen, a user programs the VIC-II that it generates a raster interrupt when video flyback occurs. This technique is used in the *Space Invaders* arcade game.

Horizontal and vertical pixel scrolling of up to one character block is supported by two hardware scroll registers. Depending on timing, hardware scrolling affects the entire screen or selected lines of character blocks. On a non-emulated C64, scrolling is glass-like and blur-free.

#### Hardware sprites

A sprite is a character which moves over an area of the screen, draws over the background, and redraws it after it moves. This differs from character block animation, where the user flips character blocks. On the C64, the VIC-II video controller handles most sprite emulation; the programmer defines the sprite and where it goes.

The C64 has two types of sprites, respecting their color-mode limitations. Hi-res sprites have one color (one background and one foreground), and multi-color sprites have three (one background and three foreground). Color modes can be split or windowed on a single screen. Sprites can be doubled in size vertically and horizontally up to four times their size, but the pixel attributes are the same – the pixels become "fatter". There are eight sprites, and all eight can be shown in each horizontal line concurrently. Sprites can move with glassy smoothness in front of, and behind, screen characters and other sprites.

The hardware sprites of a C64 can be displayed on a bitmapped (high-resolution) screen or a text-mode screen in conjunction with fast and smooth character block animation. Software-emulated sprites on systems without support for hardware sprites, such as the Apple II and ZX Spectrum, required a bitmapped screen. Sprite-sprite and sprite-background collisions are detected in hardware, and the VIC-II can be programmed to trigger an interrupt accordingly.

### Sound

The SID chip has three channels, each with its own ADSR envelope generator and filter capabilities. Ring modulation makes use of channel three to work with the other two channels. Bob Yannes developed the SID chip and, later, co-founded the synthesizer company Ensoniq. Composers and programmers of game music on the C64 include Rob Hubbard, Jeroen Tel, Tim Follin, David Whittaker, Chris Hülsbeck, Ben Daglish, Martin Galway, Kjell Nordbø and David Dunn. Due to the chip's three channels, chords are often played as arpeggios. It was also possible to continuously update the master volume with sampled data to enable the playback of 4-bit digitized audio. By 2008, it was possible to play four-channel 8-bit audio samples and two SID channels and still use filtering.

There are two versions of the SID chip: the 6581 and the 8580. The MOS Technology 6581 was used in the original ("breadbin") C64s, the early versions of the 64C, and the Commodore 128. The 6581 was replaced with the MOS Technology 8580 in 1987. Although the 6581 sound quality is a little crisper, it lacks the 8580's versatility; the 8580 can mix all available waveforms on each channel, but the 6581 can only mix waveforms in a channel in a limited fashion. The main difference between the 6581 and the 8580 is the supply voltage; the 6581 requires 12 volts, and the 8580 9 volts. A modification can be made to use the 6581 in a newer 64C board (which uses the 9-volt chip).

In 1986, the Sound Expander was released for the Commodore 64. It was a sound module with a Yamaha YM3526 chip capable of FM synthesis, primarily intended for professional music production.

### Revisions

Commodore made many changes to the C64's hardware, sometimes introducing compatibility issues. The computer's rapid development and Commodore and Jack Tramiel's focus on cost-cutting instead of product testing resulted in several defects which caused developers like Epyx to complain and required many revisions; Charpentier said that "not coming a little close to quality" was one of the company's mistakes.

Cost reduction was the reason for most of the revisions. Reducing manufacturing costs was vitally important to Commodore's survival during the price war and lean years of the 16-bit era. The C64's original (NMOS-based) motherboard went through two major redesigns and a number of revisions, exchanging positions of the VIC-II, SID and PLA chips. Much of the cost was initially eliminated by reducing the number of discrete components, such as diodes and resistors, which enabled a smaller printed circuit board. There were 16 C64 motherboard revisions to simplify production and reduce manufacturing costs. Some board revisions were exclusive to PAL regions. All C64 motherboards were manufactured in Hong Kong.

IC locations changed frequently with each motherboard revision, as did the presence (or lack) of the metal RF shield around the VIC-II; PAL boards often had aluminized cardboard instead of a metal shield. The SID and VIC-II are socketed on all boards, but the other ICs may be socketed or soldered. The first production C64s, made from 1982 to early 1983, are known as "silver label" models due to the case having a silver-colored "Commodore" logo. The power LED had a silver badge reading "64" around it. These machines have only a five-pin video cable, and cannot produce S-Video. Commodore introduced the familiar "rainbow badge" case in late 1982, but many machines produced into early 1983 also used silver-label cases until the existing stock was used up. The original 326298 board was replaced in spring 1983 by the 250407 motherboard, which had an eight-pin video connector and added S-Video support. This case design was used until the C64C appeared in 1986. All ICs switched to plastic shells, but the silver-label C64s (notably the VIC-II) had some ceramic ICs. The case is made from ABS plastic, which may become brown with time; this can be reversed with retrobright.

#### ICs

The VIC-II was manufactured with 5-micrometer NMOS technology, and was clocked at 17.73447 MHz (PAL) or 14.31818 MHz (NTSC). Internally, the clock was divided to generate the dot clock (about 8 MHz) and the two-phase system clocks (about 1 MHz; the pixel and system clock speeds differ slightly on NTSC and PAL machines). At such high clock rates the chip generated considerable heat, forcing MOS Technology to use a ceramic dual in-line package known as a CERDIP. The ceramic package was more expensive, but dissipated heat more effectively than plastic.

After a redesign in 1983, the VIC-II was encased in a plastic dual in-line package; this reduced costs substantially, but did not eliminate the heat problem. Without a ceramic package, the VIC-II required a heat sink. To avoid extra cost, the metal RF shielding doubled as the VIC's heat sink; not all units shipped with this type of shielding, however. Most C64s in Europe shipped with a cardboard RF shield coated with a layer of metal foil. The effectiveness of the cardboard was questionable; it acted instead as an insulator, blocking airflow and trapping heat generated by the SID, VIC, and PLA chips. The SID was originally manufactured using NMOS at 7 micrometers and, in some areas, 6 micrometers. The prototype SID and some early production models had a ceramic dual in-line package, but (unlike the VIC-II) are very rare; the SID was encased in plastic when production began in early 1982.

#### Motherboard

In 1986, Commodore released the last revision of the classic C64 motherboard. It was otherwise identical to the 1984 design, except for two 64-kilobit × 4-bit DRAM chips which replaced the original eight 64-kilobit × 1-bit ICs. After the release of the Commodore 64C, MOS Technology began to reconfigure the original C64's chipset to use HMOS technology. The main benefit of HMOS was that it required less voltage to drive the IC, generating less heat. This enhanced the reliability of the SID and VIC-II. The new chipset was renumbered 85xx to reflect the change to HMOS.

In 1987, Commodore released a 64C variant with a redesigned motherboard known as a "short board". The new board used the HMOS chipset, with a new 64-pin PLA chip. The "SuperPLA", as it was called, integrated discrete components and transistor–transistor logic (TTL) chips. In the last revision of the 64C motherboard, the 2114 4-bit-wide color RAM was integrated into the SuperPLA.

### Power supply

The C64 used an external power supply, a linear transformer with multiple taps differing from switch mode (presently used on PC power supplies). It was encased in epoxy resin gel, which discouraged tampering but increased the heat level during use. The design saved space in the computer's case, and allowed international versions to be more easily manufactured. The 1541-II and 1581 disk drives and third-party clones also have external power-supply "bricks", like most peripherals.

Commodore power supplies often failed sooner than expected. The computer reportedly had a 30-percent return rate in late 1983, compared to the 5–7 percent rate considered acceptable by the industry; *Creative Computing* reported four working C64s, out of seven. Malfunctioning power bricks were notorious for damaging the RAM chips. Due to their higher density and single supply (+5V), they had less tolerance for over-voltage. The usually-failing voltage regulator could be replaced by piggybacking a new regulator on the board and fitting a heat sink on top.

The original PSU on early-1982 and 1983 machines had a 5-pin connector which could accidentally be plugged into the computer's video output. Commodore later changed the design, omitting the resin gel to reduce costs. The following model, the Commodore 128, used a larger, improved power supply which included a fuse. The power supply for the Commodore REU was similar to that of the Commodore 128, providing an upgrade for customers purchasing the accessory.

### Specifications

#### Internal hardware

- Microprocessor CPU:
  - MOS Technology 6510/8500 (the 6510/8500 is a modified 6502 with an integrated 6-bit I/O port)
  - Clock speed: 0.985 MHz (PAL) or 1.023 MHz (NTSC)
- Video: MOS Technology VIC-II 6567/8562 (NTSC), 6569/8565 (PAL)
  - 16 colors
  - Text mode: 40×25 characters; 256 user-defined chars (8×8 pixels, or 4×8 in multicolor mode); or extended background color; 64 user-defined chars with 4 background colors, 4-bit color RAM defines foreground color
  - Bitmap modes: 320×200 (2 unique colors in each 8×8 pixel block), 160×200 (3 unique colors + 1 common color in each 4×8 block)
  - 8 hardware sprites of 24×21 pixels (12×21 in multicolor mode)
  - Smooth scrolling, raster interrupts
- Sound: MOS Technology 6581/8580 SID
  - 3-channel synthesizer with programmable ADSR envelope
  - 8 octaves
  - 4 waveforms per audio channel: triangle, sawtooth, variable pulse, noise
  - Oscillator synchronization, ring modulation
  - Programmable filters: high-pass, low-pass, band-pass, and notch filter
- Input/Output: Two 6526 Complex Interface Adapters
  - 16-bit parallel I/O
  - 8-bit serial I/O
  - 24-hour (AM/PM) Time of Day clock (TOD), with programmable alarm clock
  - 16 bit interval timers
- RAM:
  - 64 KiB, of which 38 KiB were available for BASIC programs
  - 1024 nybbles color RAM (memory allocated for screen color data storage)
  - Expandable to 320 KiB with Commodore 1764 256 KiB RAM Expansion Unit (REU); although only 64 KiB directly accessible; REU used mostly for the GEOS. REUs of 128 KiB and 512 KiB, originally designed for the C128, were also available, but required the user to buy a stronger power supply from some third party supplier; with the 1764 this was included.

Creative Micro Designs also produced a 2 MB REU for the C64 and C128, called the 1750 XL. The technology actually supported up to 16 MB, but 2 MB was the biggest one officially made. Expansions of up to 16 MB were also possible via the CMD SuperCPU.

- ROM:
  - 20 KB (9 KB Commodore BASIC 2.0; 7 KB KERNAL; 4 KB character generator, providing two 2 KB character sets)

#### Input/output (I/O) ports and power supply

- I/O ports:
  - ROM cartridge expansion slot (44-pin slot for edge connector with 6510 CPU address/data bus lines and control signals, as well as GND and voltage pins; used for program modules and memory expansions, among others)
  - Integrated RF modulator television antenna output via an RCA connector. The used channel could be adjusted from number 36 with the potentiometer to the left.
  - 8-pin DIN connector containing composite video output, separate Y/C outputs and sound input/output. This is a 262° horseshoe version of the plug, rather than the 270° circular version. Early C64 units (with motherboard Assy 326298) use a 5-pin DIN connector that carries composite video and luminance signals, but lacks a chroma signal.
  - Serial bus (proprietary serial version of IEEE-488, 6-pin DIN plug) for CBM printers and disk drives
  - PET-type Commodore Datasette 300 baud tape interface (edge connector with digital cassette motor/read/write/key-sense signals), Ground and +5V DC lines. The cassette motor is controlled by a +5V DC signal from the 6510 CPU. The 9V AC input is transformed into unregulated 6.36V DC which is used to actually power the cassette motor.
  - User port (edge connector with TTL-level signals, for modems and so on; byte-parallel signals which can be used to drive third-party parallel printers, among other things, 17 logic signals, 7 ground and voltage pins, including 9 V AC)
  - 2× screwless DE9M game controller ports (compatible with Atari 2600 controllers), each supporting five digital inputs and two analog inputs. Available peripherals included digital joysticks, analog paddles, a light pen, the Commodore 1351 mouse, and graphics tablets such as the KoalaPad.
- Power supply:
  - 5 V DC and 9 V AC from an external "power brick", attached to a 7-pin female DIN-connector on the computer.

The 9 volt AC is used to supply power via a charge pump to the SID sound generator chip, provide 6.8 V via a rectifier to the cassette motor, a "0" pulse for every positive half wave to the time-of-day (TOD) input on the CIA chips, and 9 volts AC directly to the user-port. Thus, as a minimum, a 12 V square wave is required. But a 9 V sine wave is preferred.

#### Memory map

| Address | Size [KiB] | Description |   |   |   |
|---|---|---|---|---|---|
| 0x0000 | 32 | RAM |   |   |   |
| 0x8000 | 8 | RAM | Cartridge ROM |   |   |
| 0xA000 | 8 | RAM | BASIC ROM |   |   |
| 0xC000 | 4 | RAM |   |   |   |
| 0xD000 | 4 | RAM | I/O/Color RAM | Character ROM |   |
| 0xE000 | 8 | RAM | KERNAL ROM |   |   |

Note that even if an I/O chip like the VIC-II only uses 64 positions in the memory address space, it will occupy 1,024 addresses because some address bits are left undecoded.

#### Peripherals

- (Commodore 1541 floppy drive) Commodore 1541 floppy drive
- (Commodore 1541C floppy drive) Commodore 1541C floppy drive
- (Commodore 1541-II floppy drive) Commodore 1541-II floppy drive
- (Commodore 1530 Datasette) Commodore 1530 Datasette
- (Commodore MPS-802 dot matrix printer) Commodore MPS-802 dot matrix printer
- (Commodore VIC-Modem) Commodore VIC-Modem
- (Commodore 1351 mouse) Commodore 1351 mouse
- (Commodore 1702 video monitor) Commodore 1702 video monitor
- (Commodore 1581 3.5-inch double-sided floppy drive) Commodore 1581 3.5-inch double-sided floppy drive

### Manufacturing cost

Vertical integration was the key to keeping Commodore 64 production costs low. At the introduction in 1982, the production cost was US$135 and the retail price US$595. In 1985, the retail price went down to US$149 (US$450 today) and the production costs were believed to be somewhere between US$35–50 (c. US$100–150 today). Commodore would not confirm this cost figure. Dougherty of the Berkeley Softworks estimated the costs of the Commodore 64 parts based on his experience at Mattel and Imagic.

| Count | Price in 1985 US$ | Part |
|---|---|---|
| 3 | 1 | ROMs |
| 8 | 1.85 | Dynamic RAMs |
|   | 4 | SID (sound) chip |
|   | 4 | VIC-II (graphics) chip |
|   | 3 | RF modulator package |
|   | 1–2 | 6510 8-bit microprocessor |
|   | 5 | A handful of TTL, buffers, power regulators and capacitors |
|   | 10 max. | Keyboard |
|   | 1–2 | Printed circuit board |
|   | 1–2 | Plastic case |
|   | 5–10 | Power supply and miscellaneous connectors |
|   | 1–2 | Packaging and manual |
| Total: | 52.8–61.8 |   |

To lower costs, TTL chips were replaced with less expensive custom chips and ways to increase the yields on the sound and graphics chips were found. The video chip 6567 had the ceramic package replaced with plastic but heat dissipation demanded a redesign of the chip and the development of a plastic package that can dissipate heat as well as ceramic.

### Compatible hardware

C64 enthusiasts were developing new hardware in 2008, including Ethernet cards, specially adapted hard disks and flash card interfaces (sd2iec). A-SID, which gives the C-64 a wah-wah effect, was introduced in 2022.


## Clones and other reuse of the Commodore 64 name

### Clones

C64 clones are computers which imitate Commodore 64 functions. In mid-2004, after an absence from the marketplace of more than 10 years, PC manufacturer Tulip Computers (owners of the Commodore brand since 1997) announced the C64 Direct-to-TV (C64DTV): a joystick-based TV game based on the C64, with 30 games in its ROM. Designed by Jeri Ellsworth, a self-taught computer designer who had designed the C-One C64 implementation, the C64DTV was similar to other mini-consoles based on the modestly-successful Atari 2600 and Intellivision. The C64DTV was advertised on QVC in the United States for the 2004 holiday season.

In 2015, a Commodore 64-compatible motherboard was produced by Individual Computers. Called the C64 Reloaded, it is a redesign of Commodore 64 motherboard revision 250466 with several new features. The motherboard is designed to be placed in an existing, empty C64 or C64C case. Produced in limited quantities, models of this Commodore 64 clone have machined or ZIF sockets in which custom C64 chips are placed. The board contains jumpers to accept revisions of the VIC-II and SID chips and the ability to switch between the PAL and NTSC video systems. It has several innovations, including selection (via the restore key) of KERNAL and character ROMs, built-in reset toggle on the power switch, and an S-Video socket to replace the original TV modulator. The motherboard is powered by a DC-to-DC converter which uses 12 V DC from a mains adapter, rather than the original (and failure-prone) Commodore 64 power-supply brick.

### Web.it Internet computer

The C64 brand was reused in 1998 for the Web.it Internet Computer, a low-powered, Internet-oriented, all-in-one x86 PC running MS-DOS and Windows 3.1. It uses an AMD Élan SC400 SoC with 16 MB of RAM, a 3.5-inch floppy disk drive, 56k modem and PC Card. Despite its Commodore 64 nameplate, the C64 Web.it looks different and is only directly compatible with the original via included emulation software. PC clones branded C64x sold by Commodore USA, a company licensing the Commodore trademark, began shipping in June 2011. The C64x's case resembles the original C64 computer, but – like the Web.it – it is based on x86 architecture and is not compatible with the Commodore 64.

### Virtual Console

Several Commodore 64 games were released on the Nintendo Wii's Virtual Console service in Europe and North America. They were delisted from the service in August 2013.

### THEC64 and THEC64 Mini

British company Retro Games released two unofficial Linux-based emulation consoles based on the Commodore 64: THEC64 Mini in 2018 and the full size THEC64 in 2019. The name THEC64 – without a space between "The" and "C64" – is due to Retro Games not licensing the use of any Commodore trademarks including the C64 name; another consequence of this is that the Commodore key from the original keyboard is replaced with a THEC64 key.

THEC64 Mini is a decorative, half-size Commodore 64 with two USB and one HDMI port, and a mini USB connection to power the system. The keyboard is non-functional; the system is controlled by an included THEC64 joystick or a separate USB keyboard. The console uses the VICE emulator which can also load additional software ROMs.

The full-size THEC64 is the same size as the original Commodore 64, with a functional keyboard. Enhancements include VIC-20 emulation, two additional USB ports, and an upgraded joystick.

- (A C64 and a much-smaller THEC64 Mini) THEC64 Mini *(top)* next to an original C64
- (See caption) Full-size THEC64 in its original box

### Commodore 64 Ultimate

In December 2025, the Commodore 64 Ultimate was released by Commodore International. It is an FPGA-based remake of the Commodore 64, with added features such as HDMI output and the ability to load software over USB or a Wi-Fi or Ethernet network connection.


## Emulators

Commodore 64 emulators include the open source VICE, Hoxs64, and CCS64. An iPhone app was also released with a compilation of C64 ports.

The *Commodore PET*, introduced in July 2015, was an Android smartphone with Commodore 64 and Amiga emulation built-in.
