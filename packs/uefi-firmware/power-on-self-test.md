---
title: "Power-on self-test"
source: https://en.wikipedia.org/wiki/Power-on_self-test
domain: uefi-firmware
license: CC-BY-SA-4.0
tags: uefi firmware, bios firmware, guid partition table, system firmware
fetched: 2026-07-02
---

# Power-on self-test

A **power-on self-test** (**POST**) is a process performed by firmware or software routines immediately after a computer or other digital electronic device is powered on.

POST processes may set the initial state of the device and detect if any hardware components are non-functional. The results of the POST may be displayed on a panel that is part of the device, output to an external device, or stored for future retrieval by a diagnostic tool. In some computers, an indicator lamp or a speaker may be provided to show error codes as a sequence of flashes or beeps in the event that a computer display malfunctions.

POST routines are part of a computer's **pre-boot sequence**. If they complete successfully, the bootstrap loader code is invoked to load an operating system.

In IBM PC compatible computers, the main duties of POST are handled by the BIOS or UEFI.

## IBM-compatible PC POST

In IBM PC compatible computers, the main duties of POST are handled by the BIOS or UEFI, which may hand some of these duties to other programs designed to initialize very specific peripheral devices, notably for video and SCSI initialization. These other duty-specific programs are generally known collectively as option ROMs or individually as the video BIOS, SCSI BIOS, etc.

### History

In earlier BIOSes, up to around the turn of the millennium, the POST would perform a thorough test of all devices, including a complete memory test. This design by IBM was modeled after their larger mainframe systems, which would perform a complete hardware test as part of their cold-start process. As the PC platform evolved into more of a commodity consumer device, the mainframe and minicomputer-inspired high-reliability features such as parity memory and the thorough memory test in every POST were dropped from most models. The exponential growth of PC memory sizes, driven by the equally exponential drop in memory prices, was also a factor in this, as the duration of a memory test using a given CPU is directly proportional to the memory size.

The original IBM PC could be equipped with as little as 16 KB of RAM and typically had between 64 and 640 KB; depending on the amount of equipped memory, the computer's 4.77 MHz 8088 required between 5 seconds and 1.5 minutes to complete the POST and there was no way to skip it. Beginning with the IBM XT, a memory count was displayed during POST instead of a blank screen. A modern PC with a bus rate of around 1 GHz and a 32-bit bus might be 2000x or even 5000x faster, but might have many more gigabytes of memory. With boot times more of a concern now than in the 1980s, the 30- to 60-second memory test adds undesirable delay for a benefit of confidence that is not perceived to be worth that cost by most users. Most clone PC BIOSes allowed the user to skip the POST RAM check by pressing a key, and more modern machines (2000s and later) often performed no RAM test at all unless it was enabled via the BIOS setup. In addition, modern DRAM is significantly more reliable than DRAM was in the 1980s.

### Purposes

During the POST, the BIOS must integrate multiple competing, changing, and even mutually exclusive standards and initiatives for the matrix of hardware and operating systems the PC is expected to support, although at most only simple memory tests and the setup screen are displayed. The principal duties of the main BIOS during POST include:

- verify CPU registers
- verify the integrity of the BIOS code itself
- verify some basic components like DMA, timer, interrupt controller
- initialize, size, and verify system main memory
- initialize BIOS
- pass control to other specialized extension BIOSes (if installed)
- identify, organize, and select which devices are available for booting

The functions above are served by the POST in all BIOS versions back to the very first. In later BIOS versions, POST will also:

- initialize chipset
- discover, initialize, and catalog all system buses and devices
- provide a user interface for system's configuration
- construct whatever system environment is required by the target operating system

In early BIOSes, POST did not organize or select boot devices; it simply identified floppy or hard disks, which the system would always try to boot in that order.

### Process

The BIOS begins its POST when the CPU is reset. The first memory location the CPU tries to execute is known as the reset vector. In the case of a hard reboot, the northbridge will direct a code fetch request to the BIOS located on the system flash memory. For a warm boot, the BIOS will be located in the proper place in RAM and the northbridge will direct the reset vector call to the RAM. In earlier PC systems, before chipsets were standard, the BIOS ROM would be located at an address range that included the reset vector, and BIOS ran directly out of ROM. This is why the motherboard BIOS ROM is in segment F000 in the conventional memory map.

During the POST flow of a contemporary BIOS, one of the first things a BIOS should do is determine the reason it is executing. For a cold boot, for example, it may need to execute all of its functionality. If, however, the system supports power-saving or quick-boot methods, the BIOS may be able to circumvent the standard POST device discovery and simply program the devices from a preloaded system device table.

As part of the starting sequence the POST routines may display a prompt to the user for a key press to access built-in setup functions of the BIOS. This allows the user to set various options particular to the motherboard before the operating system is loaded. If no key is pressed, the POST will proceed on to the boot sequence required to load the installed operating system.

Many modern BIOS and UEFI implementations show a manufacturer's logo during POST and hide the classic text screens unless an error occurs. The text screen can often be enabled in the BIOS settings by disabling the "Quiet Boot" option.

### Progress and error reporting

The original IBM BIOS made POST diagnostic information available by outputting a number to I/O port 0x80 (a screen display was not possible with some failure modes). Both progress indication and error codes were generated; in the case of a failure which did not generate a code, the code of the last successful operation was available to aid in diagnosing the problem. Using a logic analyzer or a dedicated POST card‍—‌an interface card that shows port 0x80 output on a small display‍—‌a technician could determine the origin of the problem. Once an operating system is running on the computer the code displayed by such a board may become meaningless, since some OSes, e.g. Linux, use port 0x80 for I/O timing operations. The actual numeric codes for the possible stages and error conditions differ from one BIOS supplier to another. Codes for different BIOS versions from a single supplier may also vary, although many codes remain unchanged in different versions.

Later BIOSes used a sequence of beeps from the motherboard-attached PC speaker (if present and working) to signal error codes. Some vendors developed proprietary variants or enhancements, such as MSI's D-Bracket. POST beep codes vary from manufacturer to manufacturer.

Information on numeric and beep codes is available from manufacturers of BIOSes and motherboards. There are websites which collect codes for many BIOSes.

#### Original IBM POST beep codes

| Beeps | Meaning |
|---|---|
| 1 short beep | Normal POST – system is OK |
| 2 short beeps | POST error – error code shown on screen |
| No beep | Power supply, system board problem, disconnected CPU, or disconnected speaker |
| Continuous beep | Power supply, system board, RAM or keyboard problem |
| Repeating short beeps | Power supply, system board or keyboard problem |
| 1 long, 1 short beep | System board problem |
| 1 long, 2 short beeps | Display adapter problem (MDA, CGA) |
| 1 long, 3 short beeps | Enhanced Graphics Adapter problem (EGA) |
| 3 long beeps | 3270 keyboard card error |

#### POST AMI BIOS beep codes

| Beeps | Meaning |
|---|---|
| 1 | Memory refresh timer error |
| 2 | Parity error in base memory (first 64 KiB block) |
| 3 | Base memory read/write test error |
| 4 | Motherboard timer not operational (check all PSU to MB connectors seated) |
| 5 | Processor failure |
| 6 | 8042 Gate A20 test error (cannot switch to protected mode) |
| 7 | General exception error (processor exception interrupt error) |
| 8 | Display memory error (system video adapter) |
| 9 | AMI BIOS ROM checksum fix |
| 10 | CMOS shutdown register read/write fix |
| 11 | Cache memory test failed |
| continuous beeping | Motherboard does not detect a RAM module |

#### POST beep codes on CompTIA A+ certification exam

These POST beep codes are covered specifically on the CompTIA A+ Exam:

| Beeps | Meaning |
|---|---|
| Steady, short beeps | Power supply may be bad |
| Long continuous beep tone | Memory failure |
| Steady, long beeps | Power supply bad |
| No beep | Power supply bad, system not plugged in, or power not turned on |
| No beep | If everything seems to be functioning correctly there may be a problem with the 'beeper' itself. The system will normally beep one short beep. |
| One long, two short beeps | Video card failure |

#### IBM POST diagnostic code descriptions

| Code | Meaning |
|---|---|
| 100–199 | System boards |
| 200–299 | Memory |
| 300–399 | Keyboard |
| 400–499 | Monochrome display |
| 500–599 | Color/graphics display |
| 600–699 | Floppy-disk drive or adapter |
| 700–799 | Math coprocessor |
| 900–999 | Parallel printer port |
| 1000–1099 | Alternate printer adapter |
| 1100–1299 | Asynchronous communication device, adapter, or port |
| 1300–1399 | Game port |
| 1400–1499 | Color/graphics printer |
| 1500–1599 | Synchronous communication device, adapter, or port |
| 1700–1799 | Hard drive or adapter (or both) |
| 1800–1899 | Expansion unit (XT) |
| 2000–2199 | Bisynchronous communication adapter |
| 2400–2599 | EGA system-board video (MCA) |
| 3000–3199 | LAN adapter |
| 4800–4999 | Internal modem |
| 7000–7099 | Phoenix BIOS chips |
| 7300–7399 | 3.5-inch disk drive |
| 8900–8999 | MIDI adapter |
| 11200–11299 | SCSI adapter |
| 21000–21099 | SCSI fixed disk and controller |
| 21500–21599 | SCSI CD-ROM system |

## Macintosh POST

Apple's Macintosh computers also perform a POST after a cold boot. In the event of a fatal error, the Mac will not make its startup chime.

### Old World Macs (until 1998)

Macs made before 1987, upon failing the POST, crashed silently without playing any sound and froze, with a single hexadecimal string and a Sad Mac icon on the screen, if working. Macs made after 1987 but before 1998, upon failing the POST, will immediately halt with a "death chime", which is a sound that varies by model; it can be a simple beep, a car crash sound, the sound of shattering glass, a short musical tone, or more. On the screen, if working, will be the Sad Mac icon, along with two hexadecimal strings, which can be used to identify the problem. Some Macs made during that same time period do not use a death chime like Macs made before 1987, but retained the same format as those that used the death chimes, such as the presence of the Sad Mac icon and two hexadecimal strings on screen. Old World Macs based on PCI architecture before 1998 don’t display a Sad Mac icon nor the hexadecimal strings on screen and only play the death chime.

### New World Macs (1998–1999)

When Apple introduced the iMac in 1998, it was a radical departure from other Macs of the time. The iMac began the production of New World Macs, as they are called; New World Macs, such as the iMac G3, Power Macintosh G3 (Blue & White), Power Mac G4 (PCI Graphics), PowerBook G3 (bronze keyboard), and PowerBook G3 (FireWire), load the Mac OS ROM from the hard drive. In the event of an error that is not a fatal hardware error, they display the same screen as seen when holding ⌘ Command+⌥ Option+O+F at startup but with the error message instead of the "0 >" prompt. In the event of a fatal hardware error, they give these beeps:

| Beeps | Meaning |
|---|---|
| 1 | No RAM installed/detected |
| 2 | Incompatible RAM type installed (for example, EDO) |
| 3 | No RAM banks passed memory testing |
| 4 | Bad checksum for the remainder of the boot ROM |
| 5 | Bad checksum for the ROM boot block |

### New World Macs (1999 onward)

The beep codes were revised in October 1999. In addition, on some models, the power LED will flash in cadence.

| Beeps | Meaning |
|---|---|
| 1 | No RAM installed/detected |
| 2 | Incompatible RAM types |
| 3 | No good banks |
| 4 | No good boot images in the boot ROM, bad sys config block, or both |
| 5 | Processor is not usable |

### Intel-based Macs

With the introduction of Intel-based Macs using UEFI, the startup tones were changed again. These tones are not present in Intel-based Macs equipped with a T2 security chip, as they handle the POST process differently from those without a T2 security chip.

| Tones | Meaning |
|---|---|
| One tone, repeating every five seconds | No RAM installed/detected |
| Three successive tones followed by a repeating five-second pause | Incompatible RAM types; No good banks |
| One long tone while the power button is held down | EFI ROM update in progress (For Macs made until 2012) |
| Three long tones, three short tones, three long tones | EFI ROM corruption detected, ROM recovery in process |

### Apple silicon-based Macs

The Mac transition to Apple silicon marked a radical change in the POST process in Macs. Unlike most Intel-based Macs with UEFI, Apple silicon-based Macs use a boot ROM that loads the Low-Level Bootloader (LLB), similar to that of the firmware for the iPhone and iPad. No audible beep codes or tones are used to indicate hardware failures, similar to Intel-based Macs equipped with a T2 security chip. In the event of an error that is not a fatal hardware error, an exclamation mark will be displayed on the screen or the device will go into Device Firmware Update (DFU) mode. In the event of a fatal hardware error, no audio or visual feedback is provided. In addition, on some models, the power LED will flash in cadence.

## Amiga POST

Amiga historical line of computers, from A1000 to 4000 present an interesting POST sequence that prompts the user with a sequence of flashing screens of different colors (rather than audible beeps as in other systems) to show if various hardware POST tests were correct or else if they failed:

### POST sequence of Amiga

The Amiga system performs the following steps at boot:

1. Delays beginning the tests a fraction of a second to allow the hardware to stabilize.
2. Jumps to ROM code in diagnostic card (if found)
3. Disables and clears all DMA and interrupts.
4. Turns on the screen.
5. Checks the general hardware configuration. If the screen remains a light gray color and the tests continue, the hardware is OK. If an error occurs, the system halts.
6. Performs checksum test on ROMs.

If the system fails the ROM test, the screen display turns red and the system halts.

### Sequence for all main Amiga models

Almost all Amiga models present the same color sequence when turned on: black screen, dark gray, light gray color screens filling the entire monitor screen in a rapid sequence (Amigas usually take between 2 and 3 seconds to turn on and boot).

### Color screens scheme

| Color | Meaning |   |
|---|---|---|
|   | Red | Bad ROM |
|   | Yellow | CPU Exception Before Bootstrap Code is Loaded |
|   | Green | Bad Chip RAM or failure of Agnus Chip (check seating of Agnus) |
|   | Black | No CPU |
|   | Cyan | Rev 0.x Kickstarts - Kickstart Error |
|   | White | Expansion passed test successfully |
|   | Grey | Turn on |
|   | Constant white | Failure of CPU |
|   | Purple | Return from InitCode() |

### Sequence for A4000

#### Correct tests color sequence scheme

A4000 presents just a light gray screen during its boot time (it just occurs in 2 or max 3 seconds)

- Light Gray
- = Initial hardware configuration tests passed
- = Initial system software tests passed
- = Final initialization test passed

#### Failed tests color scheme

| Color | Meaning |   |
|---|---|---|
|   | Red | ROM Error - Reset or replace |
|   | Green | CHIP RAM error (reset AGNUS and re-test) |
|   | Blue | Custom Chip(s) Error |
|   | Yellow | 68000 detected error before software trapped it (GURU) |

### Amiga keyboard LED error signals

The keyboards of historical Amiga models are not proprietary as it happened in early computer ages, but more pragmatically it was based on international standard ANSI/ISO 8859-1. The keyboard itself was an intelligent device and had its own processor and 4 kilobytes of RAM for keeping a buffer of the sequence of keys that were being pressed; thus it can communicate with the user if a fault is found by flashing its main LED in sequence:

| Blinks | Meaning |
|---|---|
| 1 | ROM checksum failure |
| 2 | RAM test failed |
| 3 | Watchdog timer failed |
| 4 | A shortcut exists between two row lines or one of the seven special keys (not implemented) |

## Embedded systems

Many embedded systems such as those in major appliances, avionics, communications, or medical equipment have built-in self-test routines that are automatically invoked at power-on.
