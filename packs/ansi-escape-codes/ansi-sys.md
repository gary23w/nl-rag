---
title: "ANSI.SYS"
source: https://en.wikipedia.org/wiki/ANSI.SYS
domain: ansi-escape-codes
license: CC-BY-SA-4.0
tags: ansi escape code, terminal escape sequences, ansi color codes, control character sequences
fetched: 2026-07-02
---

# ANSI.SYS

**ANSI.SYS** is a device driver in the DOS family of operating systems that allows a program to control the display by inserting ANSI escape sequences into its output. Without this a program could only add lines of text to the bottom of the screen, unless it directly manipulated the graphics hardware. Using ANSI.SYS would have allowed graphics device independence in IBM clones; but it was not installed by default and was notoriously slow.

## Usage

To use ANSI.SYS under DOS, a line is added to the CONFIG.SYS (or CONFIG.NT under Windows NT based versions of Windows) file that reads:

DEVICE

=

drive:

\

path

\ANSI.SYS

options

where *drive:* and *path* are the drive letter and path to the directory in which the file ANSI.SYS is found, and *options* can be a number of optional switches to control the behaviour. ANSI.SYS may also be loaded into upper memory via DEVICEHIGH/HIDEVICE.

- /K use extended keyboard BIOS functions (INT 16h) rather than standard ones This made the F11 and F12 keys work.
- /L force number of lines
- /R adjust line scrolling to support screen readers
- /S or /SCREENSIZE set screensize
- /X support redefinition of extended key codes independent of standard codes

## Functionality

Using this driver, programs that write to the standard output can write escape sequences to make use of the 16 text foreground colors and 8 background colors available in VGA-compatible text mode, make text blink, change the location of the cursor on the screen, and blank the screen. They could also change the video mode from standard 80×25 text mode to a number of different graphics modes (for example, 320×200 graphics mode with text drawn as pixels, though ANSI.SYS is not able to turn individual pixels on and off).

The standard ANSI.SYS is very slow as it changed the screen using BIOS calls (which needed *two* calls to put a character on the screen and move the cursor right). Several companies made third-party replacements that interface directly with the video memory and ran at usable speeds, examples are ANSI.COM, NANSI.SYS and ANSIPLUS.EXE.

COMMAND.COM checked if this driver was in use, and changed the CLS command to use an escape sequence instead of a BIOS call.

### Keyboard remapping

An interesting (mis)feature of ANSI.SYS is the ability to remap any key on the keyboard in order to perform shortcuts or macros for complex instructions. Using special escape sequences, the user can define any keystroke that has a character-code mapping to simulate an arbitrary sequence of such keystrokes. This was used to create simple trojans out of text files laced with nefarious keyboard remaps, known as "ANSI bombs". A number of products were released to protect users against this:

- Many replacements for ANSI.SYS support a command line switch to disable the key remapping feature, f.e. the option /S (Secure) in Datalight ROM-DOS or NANSI.SYS of FreeDOS. Other ANSI drivers like ANSIPLUS can be configured to disable the redefinition of keys as well.
- Some replacements were deliberately designed never to support the keyboard remapping functions.
- PKWARE, Inc. produced a terminate-and-stay-resident program, PKSFANSI (PK Safe ANSI), which filters out keyboard remapping escape codes as they are written to the standard output. This has the advantage that the user can load some useful remappings from a text file and then run PKSFANSI to prevent further, possibly malicious remappings.

## Occurrence

ANSI.SYS appeared in MS-DOS 2.0, the first version of the operating system supporting device drivers. It was supported by all following versions of MS-DOS. It is also present in many non-Microsoft DOS systems, e.g. IBM PC DOS and DR-DOS.

ANSI.SYS was required to run some software that used its cursor and color control functions. It could also be used to enable elaborate color codes in the COMMAND.COM prompt. These uses were overshadowed by the use of ANSI.SYS in BBSes; ANSI escape sequences were used to enable BBSes to send text graphics more elaborate than ASCII art, and to control the cursor in ways that were used in a number of online games and similar features. Software that could run a dial-up modem often interpreted the sequences itself, and the driver was not needed.

Windows did not support this driver in any useful way (it could be used by MSDOS emulation in some versions). In Windows 10 support for similar escape sequences was built into the Win32 console (the text terminal window), but must be activated using the Windows API function `SetConsoleMode` by setting the `ENABLE_VIRTUAL_TERMINAL_PROCESSING` flag.

## Features

CSI (Control Sequence Introducer) is a placeholder for the common two-byte escape lead-in sequence "ESC [" (that is, 0x1B 0x5B). The ANSI standard also defines an alternative single-byte CSI code 0x9B, which is not supported by ANSI.SYS (this code instead drew a cent sign ⟨¢⟩ from CP437).

Standard DOS ANSI.SYS drivers support only the following sub-set of ANSI escape sequences:

| Sequence | Effect |
|---|---|
| ESC [ *r* A | Cursor up (CUU) |
| ESC [ *r* B | Cursor down (CUD) |
| ESC [ *c* C | Cursor forward (CUF) |
| ESC [ *c* D | Cursor back (CUB) |
| ESC [ *r*;*c* f | Horizontal and vertical position (HVP) |
| ESC [ *r*;*c* H | Cursor position (CUP) |
| ESC [ *n* J | Erase display (ED) (n=0, 2 or n=0, 1, 2) |
| ESC [ *n* K | Erase in line (EL) (n=0 or n=0, 1, 2) |
| ESC [ *n* m | Select graphic rendition (SGR) (n=0..47) |
| ESC [ 6 n | Device status report (DSR) requests cursor position, returned as cursor position report (CPR): ESC [ *r*;*c* R |
| ESC [ s | Save cursor position (SCP) |
| ESC [ u | Restore cursor position (RCP) |

There are also some escape sequences specific to the implementation of ANSI.SYS. They are not generally supported by ANSI consoles in other operating systems.

| Sequence | Effect |
|---|---|
| ESC [ *n* h ESC [ ?*n* h ESC [ =*n* h ESC [ >*n* h | Set screen mode (SM) |
| ESC [ *n* l ESC [ ?*n* l ESC [ =*n* l ESC [ >*n* l | Reset screen mode (RM) |
| ESC [ *n* q | Enable (n=1) or disable (n=0) /X support |
| ESC [ L | Insert line (IL) |
| ESC [ M | Delete line (DL) |
| ESC $ ) 1 | Switch keyboard input mode to Korean (Hangul) |
| ESC ( 2 | Switch keyboard input mode to English |
| ESC [ + | Enable console output |
| ESC [ - | Disable console output |
| ESC [ *a*;*b*;... p | Set key re-definement (SKR/KR) |

| Mode | Description | Mode | Description |
|---|---|---|---|
| 0 | 40 × 25 monochrome | 1 | 40 × 25 color |
| 2 | 80 × 25 monochrome | 3 | 80 × 25 color |
| 4 | 320 × 200 color | 5 | 320 × 200 monochrome |
| 6 | 640 × 200 monochrome |   |   |
| 7 | Wrap at end of line |   |   |
| 13 | 320 x 200 color (graphics) | 14 | 640 x 200 color (16-color graphics) |
| 15 | 640 x 350 monochrome (2-color graphics) | 16 | 640 x 350 color (16-color graphics) |
| 17 | 640 x 480 monochrome (2-color graphics) | 18 | 640 x 480 color (16-color graphics) |
| 19 | 320 x 200 color (256-color graphics) |   |   |
| 114 | 640 x 480 color (16-color graphics) | 115 | 640 x 475 color (16-color graphics) |

In some DOS implementations, video modes above 7 are not documented. Under Multiuser DOS, the only valid argument in conjunction with PCTERM is 7.
