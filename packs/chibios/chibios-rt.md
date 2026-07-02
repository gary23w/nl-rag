---
title: "ChibiOS/RT"
source: https://en.wikipedia.org/wiki/ChibiOS/RT
domain: chibios
license: CC-BY-SA-4.0
tags: chibios rt, chibios hal, real-time kernel, stm32 board
fetched: 2026-07-02
---

# ChibiOS/RT

**ChibiOS/RT** is a compact and fast real-time operating system for microcontrollers supporting multiple architectures and released under a mix of the GNU General Public License version 3 (GPL3) and the Apache License 2.0 (depending on module). It is developed by Giovanni Di Sirio.

Commercial licenses are available from *ChibiOS*. Additional products include ChibiOS/HAL, a hardware abstraction layer compatible with ChibiOS/RT, and ChibiStudio, a free integrated development environment based on Eclipse, the GNU Compiler Collection, and the OpenOCD Joint Test Action Group (JTAG) debugging pod.

## Metrics

ChibiOS/RT is designed for embedded applications on microcontrollers of 8-, 16-, and 32-bits. Size and execution efficiency are the main project goals. As reference, the kernel size can range from a minimum of 1.2 KiB up to a maximum of 5.5 KiB with all the subsystems activated on a STM32 Cortex-M3 processor. The kernel can achieve over 220,000 created/terminated threads per second and can perform a context switch in 1.2 microseconds on an STM32 @ 72 MHz. Similar metrics for all the supported platforms are included in the source code distribution as test reports.

## Features

The ChibiOS/RT microkernel supports:

- Preemptive multithreading
- 128 priority queue levels
- Round-robin scheduling for threads at the same priority level
- Software timers
- Counting semaphores
- Mutexes with support for the priority inheritance algorithm
- Condition variables
- Synchronous and asynchronous Messages
- Event flags and handlers
- Queues
- Synchronous and asynchronous I/O with timeout capability
- Thread-safe memory heap and memory pool allocators.
- Hardware Abstraction Layer with support for ADC, CAN, GPT (general-purpose timer), EXT, I2C, ICU, MAC, MMC/SD, PAL, PWM, RTC, SDC, Serial, SPI, and USB drivers.
- Support for the LwIP and uIP TCP/IP stacks.
- Support for the FatFs file system library.

All system objects, such as threads, semaphores, timers, etc., can be created and deleted at runtime. There is no upper limit except for the available memory. To increase system reliability, the kernel architecture is entirely static, a memory allocator is not needed (but is available as an option), and there are no data structures with upper size limits like tables or arrays. The system application programming interfaces (APIs) are designed to not have error conditions such as error codes or exceptions.

The RTOS is designed for applications on embedded systems (devices) and includes demo applications for various microcontrollers:

- STMicroelectronics – STM32F1xx, STM32F2xx, STM32F3xx, STM32F4xx, STM32L1xx, STM32F0xx; STM8S208x, STM8S105x, STM8L152x; ST/Freescale SPC56x, MPC56xx
- NXP Semiconductors – LPC11xx, LPC11Uxx, LPC13xx, LPC2148
- Atmel – AT91SAM7S, AT91SAM7X, megaAVR
- Texas Instruments (TI) – MSP430x1611; TM4C123G, TM4C1294
- Microchip Technology – PIC32MX

Contributed ports are also available for the Coldfire and H8S families.

ChibiOS/RT has also been ported to the Raspberry Pi and the following device drivers have been implemented: Port (GPIO), Serial, GPT (General-Purpose Timer), I2C, SPI and PWM.

It is also possible to run the kernel in a Win32 process in a software I/O emulation mode, allowing easy application development without the need for physical hardware. An example is included for MinGW compiler.

## uGFX

ChibiOS/RT is fully supported by the graphical user interface (GUI) toolkit µGFX, formerly named ChibiOS/GFX.
