---
title: "Reset (computing)"
source: https://en.wikipedia.org/wiki/Reset_(computing)
domain: watchdog-supervisors
license: CC-BY-SA-4.0
tags: watchdog timer, brownout detection, reset circuit, fail-safe design
fetched: 2026-07-02
---

# Reset (computing)

In a computer or data transmission system, a **reset** clears any pending errors or events and brings a system to normal condition or an initial state, usually in a controlled manner. It is usually done in response to an error condition when it is impossible or undesirable for a processing activity to proceed and all error recovery mechanisms fail. A computer storage program would normally perform a "reset" if a command times out and error recovery schemes like retry or abort also fail.

## Software reset

A software reset (or soft reset) is initiated by the software, for example, Control-Alt-Delete key combination have been pressed, or execute restart in Microsoft Windows.

## Hardware reset

Most computers have a reset line that brings the device into the startup state and is active for a short time after powering on. For example, in the x86 architecture, asserting the RESET line halts the CPU; this is done after the system is switched on and before the power supply has asserted "power good" to indicate that it is ready to supply stable voltages at sufficient power levels. Reset places less stress on the hardware than power cycling, as the power is not removed. Many computers, especially older models, have user accessible "reset" buttons that assert the reset line to facilitate a system reboot in a way that cannot be trapped (i.e. prevented) by the operating system, or holding a combination of buttons on some mobile devices. Devices may not have a dedicated Reset button, but have the user hold the power button to cut power, which the user can then turn the computer back on. Out-of-band management also frequently provides the possibility to reset the remote system in this way.

Many memory-capable digital circuits (flip-flops, registers, counters and so on) accept the reset signal that sets them to the pre-determined state. This signal is often applied after powering on but may also be applied under other circumstances. After a hard reset, the register states of many hardware have been cleared.

The ability for an electronic device to reset itself in case of error or abnormal power loss is an important aspect of embedded system design and programming. This ability can be observed with everyday electronics such as a television, audio equipment or the electronics of a car, which are able to function as intended again even after having lost power suddenly. A sudden and strange error with a device might sometimes be fixed by removing and restoring power, making the device reset. Some devices, such as portable media players, very often have a dedicated reset button as they are prone to freezing or locking up. The lack of a proper reset ability could otherwise possibly render the device useless after a power loss or malfunction.

User initiated hard resets can be used to reset the device if the software hangs, crashes, or is otherwise unresponsive. However, data may become corrupted if this occurs. Generally, a hard reset is initiated by pressing a dedicated reset button On some systems (e.g, the PlayStation 2 video game console), pressing and releasing the power button initiates a hard reset, and holding the button turns the system off.

### Hardware reset in 80x86 IBM PC

The 8086 microprocessors provide RESET pin that is used to do the hardware reset. When a HIGH is applied to the pin, the CPU immediately stops, and sets the major registers to these values:

| Register | Value |
|---|---|
| CS (Code Segment) | 0xFFFF |
| DS (Data Segment) | 0x0000 |
| ES (Extra Data Segment) | 0x0000 |
| SS (Stack Segment) | 0x0000 |
| IP (Instruction Pointer) | 0x0000 |

The CPU uses the values of CS and IP registers to find the location of the next instruction to execute. Location of next instruction is calculated using this simple equation:

`Location of next instruction = (CS<<4) + (IP)`

This implies that after the hardware reset, the CPU will start execution at the physical address 0xFFFF0. In IBM PC compatible computers, This address maps to BIOS ROM. The memory word at 0xFFFF0 usually contains a JMP instruction that redirects the CPU to execute the initialization code of BIOS. This JMP instruction is absolutely the first instruction executed after the reset.

### Hardware reset in later x86 CPUs

Later x86 processors reset the CS and IP registers similarly, refer to Reset vector.

### Mac

Apple Mac computers allow various levels of resetting, including (CTL,CMD,EJECT) analogous to the three-finger salute (CTL,ALT,DEL) on Windows computers.
