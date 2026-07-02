---
title: "Embedded Systems/Microprocessor Introduction"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Microprocessor_Introduction
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Microprocessor Introduction

<

Embedded Systems

Effectively programming an embedded system, and implementing it reliably requires the engineer to know many of the details of the system architecture. Section 1 of the Embedded Systems book will cover some of the basics of microprocessor architecture. This information might not apply to all embedded computers, and much of it may apply to computers in general. This book can only cover some basic concepts, because the actual embedded computers available on the market are changing every day, and it is the engineer's responsibility to find out what capabilities and limitations their particular systems have.

As manufacturers continue to pack more and more transistors onto a single chip, more and more of the stuff that was once "peripheral logic" has been integrated on the same chip as the CPU. A *microcontroller* includes most or all the electronics needed in an embedded system in a single integrated circuit ("chip").

- CPU
- I/O ports
- RAM - contains temporary data
- ROM - contains program and constant data—the firmware. Starting in 1993, many microcontrollers use Flash memory instead of true ROM to hold the firmware, but many engineers still refer to the Flash memory that holds the firmware as "ROM" to differentiate it from "RAM".
- Timers—we discuss these later at Timers.
- Serial interface—often a USART—we discuss these later at IO
- EEPROM - contains "permanent" data
- Analog-to-digital converter
- Specialized functions

This list is roughly in order of integration. The earliest microcontrollers contained only the CPU and I/O ports; modern microprocessors typically contain the CPU, some I/O ports, and cache RAM; the cost of a microcontroller dropped dramatically once the CPU, I/O, RAM, and ROM could all be squeezed onto the same chip, because such a microcontroller no longer needs "address pins"; etc. The most highly integrated microcontrollers include all these parts on one chip.
