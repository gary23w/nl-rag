---
title: "1-bit computing"
source: https://en.wikipedia.org/wiki/1-bit_computing
domain: integrated-circuit
license: CC-BY-SA-4.0
tags: integrated circuit
fetched: 2026-07-03
---

# 1-bit computing

In computer architecture, **1-bit** integers or other data units are those that are 1 bit (1/8 octet) wide. Also, 1-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers of that size.

There are no computers or microcontrollers of any kind that are exclusively 1-bit for all registers and address buses. A 1-bit register can only store two different values. This is very restrictive and therefore not enough for a program counter which, on modern systems, is implemented in an on-chip register, but is not implemented on-chip in some 1-bit systems. Opcodes for at least one 1-bit processor architecture were 4-bit and the address bus was 8-bit.

While 1-bit computing is rarely used on its own today, 1-bit serial communication is still used in modern computers, even on machines with large internal buses.

The first carbon nanotube computer from 2013 is a 1-bit one-instruction set computer (and has only 178 transistors; though it has only one instruction, it can emulate 20 MIPS instructions).

## 1-bit

A serial computer processes data a single bit at a time. For example, the PDP-8/S was a 12-bit computer using a 1-bit ALU, processing the 12 bits serially.

An example of a 1-bit computer built from discrete logic SSI chips is the Wang 500 (1970/1971) calculator as well as the Wang 1200 (1971/1972) word processor series developed by Wang Laboratories.

Other examples of 1-bit architectures are programmable logic controllers (PLCs), such as the 1969 PDP-14. These were often programmed in ladder logic or in instruction list (IL). An example of such a 1-bit architecture that was marketed as a CPU is the Motorola MC14500B Industrial Control Unit (ICU), introduced in 1977 and manufactured at least up into the mid 1990s. Its manual states:

> […] Computers and microcomputers may also be used, but they tend to overcomplicate the task and often require highly trained personnel to develop and maintain the system. A simpler device, designed to operate on inputs and outputs one-at-a-time and configured to resemble a relay system, was introduced. These devices became known to the controls industry as programmable logic controllers (PLC). The Motorola MC14500B Industrial Control Unit (ICU) is the monolithic embodiment of the PLC's central architecture […]
> 
> There are functions for which one bit machines are poorly suited. […] Under some circumstances, a combination of an MC6800 MPU and an MC14500B ICU may be the best solution. […]
> 
> *Program Counter* The program counter is composed of two MC145168 binary up-counters chained together to create 8 bits of memory address. This gives the system the capability of addressing 256 separate memory words. The counters are configured to count up on the rising edge of the ICU clock (CLK) signal and reset to zero when the ICU is reset. Notice that the program counter count sequence cannot be altered by any operation of the ICU. This confirms that the system is configured to have a looping control structure.
> 
> *Memory*
> 
> The memory for this system is composed of one MCM7641 512-word by 8 bit PROM memory. Because the program counter is only 8 bits wide, only 256 words, (half of the memory), can be used at any one time. However, by wiring the most significant bit of the memory's address high or low, the system designer can select between two separate programs with only a jumper option. This might be a desirable feature if extremely fast system changes are required.

— MC14500B Industrial Control Unit Handbook

One of the computers known to be based on this CPU was the WDR 1-bit computer. A typical sequence of instructions from a program for a 1-bit architecture might be:

- load digital input 1 into a 1-bit register;
- OR the value in the 1-bit register with input 2, leaving the result in the register;
- write the value in the 1-bit register to output 1.

This architecture was considered superior for programs making decisions rather than performing arithmetic computations, for ladder logic as well as for serial data processing.

There are also several design studies for 1-bit architectures in academia, and corresponding 1-bit logic can also be found in programming. Several early massively parallel computers used 1-bit architectures for the processors as well. Examples include the May 1983 Goodyear MPP and the 1985 Connection Machine. By using a 1-bit architecture for the individual processors a very large array (e.g. the Connection Machine had 65,536 processors) could be constructed with the chip technology available at the time. In this case the slow computation of a 1-bit processor was traded off against the large number of processors.
