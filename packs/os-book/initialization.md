---
title: "Operating System Design/Initialization"
source: https://en.wikibooks.org/wiki/Operating_System_Design/Initialization
domain: os-book
license: CC-BY-SA-4.0 (Wikibooks OS Design)
tags: operating system design, kernel design, process management
fetched: 2026-07-02
---

# Operating System Design/Initialization

<

Operating System Design

## Initialization

When a computer is first started, it is in an unknown state. Static electricity and remnants of previous states can lead to values that are not valid states for the machine. In defense, computer programmers have learned to initialize all variables before using them.

After the initial start-up process, the next step depends on the type of computer

## Mainframes

For large mainframe computers, the Initial Program Load, or IPL, is used to load a bootstrap program, typically very tiny, whose purpose is to load the actual boot loader from disk, tape or other media.

## Microcomputers

For typical desktop, server, or rack-mounted blade computers, the power-on-self-test or POST initializes the computer, which then passes execution over to the ROM, where the BIOS system initializes the bottom page or so of RAM, then passes execution to the boot process.

## Bootstrap

One of the first things that the boot process does is load the boot loader, which then loads the operating system.

- Boot loader
- Hardware Initialization

Retrieved from "

https://en.wikibooks.org/w/index.php?title=Operating_System_Design/Initialization&oldid=2464174

"
