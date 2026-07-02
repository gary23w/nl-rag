---
title: "Embedded Systems/Memory"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Memory
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Memory

<

Embedded Systems

On an Embedded System, memory is at a premium. Some chips, particularly embedded VLSI chips, and low-end microprocessors may only have a small amount of RAM "on board" (built directly into the chip), and therefore their memory is not expandable. Other embedded systems have a certain amount of memory, and have no means to expand. In addition to RAM, some embedded systems have some non-volatile memory, in the form of miniature magnetic disks, FLASH memory expansions, or even various 3rd-party memory card expansions. Keep in mind however, that a memory upgrade on an embedded system may cost more than the entire system itself. An embedded systems programmer, therefore, needs to be very much aware of the memory available, and the memory needed to complete a task.

Memory is frequently broken up into a number of different regions that are set aside for particular purposes.

## Addressable Areas

There are typically 4 distinct addressable areas, each one implemented with a different technology:

- Program memory (which holds the programs you write), often called ROM (although most developers prefer to use chips that actually implement this with Flash). While your program is running, it is impossible to change any of the data in program memory. But at least when the power comes back on, it's all still there.
- RAM, which holds the variables and stack. (Initial values for variables are copied from ROM). Forgets everything when power is lost.
- EEPROM. Used kind of like the hard drive in a personal computer, to store settings that might change occasionally, and that need to be remembered next time it starts up.
- I/O. This is really the entire point of a microcontroller.

Many popular microcontrollers (including the 8051, the Atmel AVR, the Microchip PIC, the Cypress PSoC) have a "Harvard architecture", meaning that programs can only execute out of "ROM". You can copy bytes from ROM (or elsewhere) into RAM, but it's physically impossible to jump or call such "code" in RAM. This is exactly the opposite of the situation on desktop computers, where the code you write cannot be executed until after it is copied into RAM.

A few popular microcontrollers (such as the 68HC11 and 68HC12 and ...) have a unified address space (a "von Neumann architecture"). You can jump or call code anywhere (although jumping to an address in I/O space is almost certainly not what you really wanted to do).

## Paging and Banking

Often software applications grow and grow. Ancient processors (such as the 8085 used on the Mars rover Sojourner) with 16 bit address registers can directly access a maximum of 65 536 locations—however, systems using these processors often have much more physical RAM and ROM than that. They use "paging" hardware that swaps in and out "banks" of memory into the directly accessible space. Early Microchip PIC processors had 2 completely separate set of "banking registers", one for swapping in different banks of program ROM, the other for swapping in different banks of RAM.

## Memory Management

All too often, programs written for embedded systems grow and grow until they exceed the available program space. There are a variety of techniques for dealing with the out-of-memory problem:

- re-compile with the "-Os" (optimize for size) option
- find and comment-out "dead code"
- "refactor" repeated sections into a common subroutine
- trade RAM space for program space.
- put a small interpreter in "internal program memory" that loads and interprets "instructions".
  - use "instructions"—perhaps p-code or threaded code—that are more compact than directly coding it in assembly language. Or
  - place these "instructions" can be placed in EEPROM or external serial Flash that couldn't otherwise be used as program memory. Or
  - Both. This technique is often used in "stamp" style CPU modules.
- add more memory (perhaps using a paging or banking scheme)

Most CPUs used in desktop machines have a "memory management unit" (MMU). The MMU handles virtual memory, protects regions of memory used by the OS from untrusted programs, and ...

Most embedded systems do not have a MMU. We discuss the two versions of Linux that can run on a system that does not have a MMU in Embedded Systems/Linux.

## x86 Memory Layout

### Reserved Memory

Reserved memory is memory which is reserved for some purpose like additional software installation and startup.

### Restricted Memory

### General-Purpose Memory

## Segmented Memory

Old X86 processors were only 16 bit processors, and if a flat memory scheme was used, those processors would only be able to support 65 Kilobytes of memory. The system engineers behind the old 8086 and 80286 processors came up with the idea to segment memory, and use a combination of segment pointers and offset pointers to access an effective 20 bit address range, for a maximum of 1 megabyte of addressable memory.

Address = (Segment register * 16) + pointer register

New 32 bit processors allow for 4 Gigabytes of addressable memory space, and therefore the segmented memory model was all but abandoned in current 32 bit machines (although the segment registers are still used to implement paging schemes).

## Memory-Mapped I/O

Memory-Mapped I/O is a mechanism by which the processor performs I/O access by using memory access techniques. This is often put into effect because the memory bus is frequently much faster than the I/O bus. Another reason that memory mapped I/O might be used is that the architecture in use does not have a separate I/O bus.

In memory mapped IO, certain range of CPU's address space is kept aside for the external peripherals. These locations can be accessed using the same instructions as used for other memory accesses. But instead, the read/writes to these addresses are interpreted as access to device rather than a location on the main memory.

A CPU may expect a particular device at a fixed location or can dynamically assign a space for it.

The way this works is that memory interfaces are often designed as a bus (a shared communications resource), where many devices are attached. These devices are usually arranged as primary and secondary devices, where a primary device can send and receive data from any of the secondary devices. A typical system would have:

- A CPU as the primary
- One or more RAM and/or ROM devices for program code and data storage
- Peripheral devices for interfacing with the outside world. Examples of these might be a UART (serial communications), Display device or Input device
