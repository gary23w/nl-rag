---
title: "STM32"
source: https://en.wikipedia.org/wiki/STM32
domain: chibios
license: CC-BY-SA-4.0
tags: chibios rt, chibios hal, real-time kernel, stm32 board
fetched: 2026-07-02
---

# STM32

**STM32** is a family of 32-bit microcontroller and microprocessor integrated circuits by STMicroelectronics. STM32 microcontrollers are grouped into related series that are based around the same 32-bit ARM processor core: Cortex-M0, Cortex-M0+, Cortex-M3, Cortex-M4, Cortex-M7, Cortex-M33, Cortex-M55, or Cortex-M85. Internally, each microcontroller consists of ARM processor core(s), flash memory, static RAM, a debugging interface, and various peripherals.

In addition to its microcontroller lines, STMicroelectronics has introduced microprocessor (MPU) offerings such as the MP1 and MP2 series into the STM32 family. These processors are based around single or dual ARM Cortex-A cores combined with an ARM Cortex-M core. Cortex-A application processors include a memory management unit (MMU), enabling them to run advanced operating systems such as Linux.

## Overview

The **STM32** family of the microcontroller ICs is based on various 32-bit RISC ARM Cortex-M cores. STMicroelectronics licenses the ARM Processor IP from ARM Holdings and integrates them with custom-designed peripherals to create complete microcontroller solutions. Each STM32 microcontroller is designed for specific performance, power efficiency, and feature requirements, making them suitable for a wide range of embedded applications. The following tables summarize the STM32 family of microcontrollers (MCUs) and microprocessors (MPUs).

| Series | ARM CPU core(s) | Target |
|---|---|---|
| C0 | Cortex-M0+ | Low-cost |
| C5 | Cortex-M33F | Low-cost |
| F0 | Cortex-M0 | Mainstream |
| F1 | Cortex-M3 | Mainstream |
| F2 | Cortex-M3 | High-performance |
| F3 | Cortex-M4F | Mixed-signal processing |
| F4 | Cortex-M4F | High-performance |
| F7 | Cortex-M7F | High-performance |
| G0 | Cortex-M0+ | Mainstream, Low Cost |
| G4 | Cortex-M4F | Mixed-signal processing |
| H5 | Cortex-M33F | High-performance, security |
| H7 | Cortex-M7F (single), or Cortex-M7F and Cortex-M4F | High-performance |
| L0 | Cortex-M0+ | Low-power |
| L1 | Cortex-M3 | Low-power |
| L4 | Cortex-M4F | Low Power |
| L4+ | Cortex-M4F | Low-power |
| L5 | Cortex-M33F | Low-power, security |
| N6 | Cortex-M55F and NPU | High-performance (Machine learning inference) |
| U0 | Cortex-M0+ | Low-power |
| U3 | Cortex-M33F | Low-power, security |
| U5 | Cortex-M33F | Low-power, security |
| V8 | Cortex-M85F | High-performance, security |
| WB0 | Cortex-M0+ | Wireless (Bluetooth LE) |
| WB | Cortex-M4F and Cortex-M0+ | Wireless (Bluetooth LE, IEEE 802.15.4) |
| WBA | Cortex-M33F | Wireless (Bluetooth LE, IEEE 802.15.4), security |
| WL | Cortex-M4 and/or Cortex-M0+ | Wireless (LoRa, sub-GHz) |

| Series | ARM CPU core(s) | Target |
|---|---|---|
| MP1 | Single or Dual Cortex-A7 and optionally Cortex-M4 | Embedded Linux, industrial, IoT |
| MP2 | Dual Cortex-A35 Cores + Cortex-M33 | High-performance, machine learning, advanced HMI |

## History

The STM32 is the third ARM family by STMicroelectronics. It follows their earlier STR9 family based on the ARM9E core, and STR7 family based on the ARM7TDMI core. The following is the history of how the STM32 family has evolved.

| Date | Announcement |
|---|---|
| October 2006 | STMicroelectronics licensed the ARM Cortex-M3 core |
| June 2007 | ST announced the STM32 F1-series based on the ARM Cortex-M3 |
| October 2009 | ST announced new ARM chips would be built using the 90 nm process |
| April 2010 | ST announced the STM32 L1-series chips |
| November 2010 | ST announced the STM32 F2-series chips based on the ARM Cortex-M3 core, and future development |
| March 2011 | ST announced the expansion of their STM32 L1-series chips with flash densities of 256 KB and 384 KB |
| September 2011 | ST announced the STM32 F4-series chips based on the ARM Cortex-M4F core |
| February 2012 | ST announced the STM32 F0-series chips based on the ARM Cortex-M0 core |
| June 2012 | ST announced the STM32 F3-series chips based on the ARM Cortex-M4F core |
| January 2013 | ST announced full Java support for STM32 F2 and F4-series chips |
| February 2013 | ST announced STM32 Embedded Coder support for MATLAB and Simulink |
| February 2013 | ST announced the STM32 F4x9-series chips |
| April 2013 | ST announced the STM32 F401-series chips |
| July 2013 | ST announced the STM32 F030-series chips and availability in a TSSOP20 package |
| December 2013 | ST announced that it is joining the mbed project |
| January 2014 | ST announced the STM32 F0x2-series chips |
| February 2014 | ST announced the STM32 L0-series chips based on the ARM Cortex-M0+ core |
| February 2014 | ST announced multiple STM32 Nucleo boards with Arduino headers and mbed IDE |
| February 2014 | ST announced the release of free STM32Cube software tool with graphical configurator and C code |
| September 2014 | ST announced the STM32 F7 series, the first chips based on the Cortex-M7F core |
| October 2016 | STM32H7 series announced, based on ARM Cortex-M7F core, produced using 40 nm technology, runs at 400 MHz |
| November 2017 | STM32L4+ series announced, an upgrade to STM32L4 series Cortex-M4 MCUs |
| October 2018 | STM32L5 series announced, ultra-low-power MCUs based on ARM Cortex-M33 core with various security features |
| February 2021 | STM32U5 series announced, ultra-low-power MCUs based on ARM Cortex-M33 core with low power and hardware & software-based security measures targeting PSA Certified and SESIP assurance level 3 with physical attacker resistance |
| January 2023 | STM32C0 series announced, based on ARM Cortex-M0+ core, targeting equipment like home appliances, industrial pumps, fans, smoke detectors, typically served by simpler 8-bit and 16-bit MCUs. |
| March 2023 | STM32H5 series announced, based on ARM Cortex-M33 core, designed for smart, connected devices, which provide more intelligence “in the edge” and also strengthens defenses against attacks on IoT assets. |
| March 2024 | STM32U0 series announced, based on ARM Cortex-M0+ core, targeting ultra-low power entry-level battery-powered applications in industrial, medical, smart metering, and consumer wellness markets. |
| March 2026 | STM32C5 with Cortex-M33, increased performance with cost efficiency and enhanced end-device capabilities. Aiming at consumer and professional devices. |
| April 2026 | MathWorks released the STM32 Microcontroller Blockset, adding support for STM32 microcontrollers |

## Series

The STM32 family consists of many series of microcontrollers. Each STM32 microcontroller series is based upon a specific ARM Cortex-M processor core.

### STM32 C0

The STM32 C0-series is an entry-level low-cost STM32-series of microcontrollers:

- ARM Cortex-M0+ core at a maximum clock rate of 48 MHz.

### STM32 F0

The STM32 F0-series are the first group of ARM Cortex-M0 chips in the STM32 family. The summary for this series is:

- Core:
  - ARM Cortex-M0 core at a maximum clock rate of 48 MHz.
  - Cortex-M0 options include the SysTick Timer.
- Memory:
  - Static RAM consists of 4 / 6 / 8 / 16 / 32 KB general purpose with hardware parity checking.
  - Flash consists of 16 / 32 / 64 / 128 / 256 KB general purpose.
  - Each chip has a factory-programmed 96-bit unique device identifier number. (except STM32F030x4/6/8/C and STM32F070x6/B,)
- Peripherals:
  - Each F0-series includes various peripherals that vary from line to line.
- Oscillators consists of internal (8 MHz, 40 kHz), optional external (1 to 32 MHz, 32.768 to 1000 kHz).
- IC packages: TSSOP20, UFQFPN32, LQFP/UFQFN48, LQFP64, LQFP/UFBGA100.
- Operating voltage range is 2.0 to 3.6 volt with the possibility to go down to 1.65 V.

### STM32 F1

The STM32 F1-series was the first group of STM32 microcontrollers based on the ARM Cortex-M3 core and considered their mainstream ARM microcontrollers. The F1-series has evolved over time by increasing CPU speed, size of internal memory, variety of peripherals. There are five F1 lines: Connectivity (STM32F105/107), Performance (STM32F103), USB Access (STM32F102), Access (STM32F101), Value (STM32F100). The summary for this series is:

- Core:
  - ARM Cortex-M3 core at a maximum clock rate of 24 / 36 / 48 / 72 MHz.
- Memory:
  - Static RAM consists of 4 / 6 / 8 / 10 / 16 / 20 / 24 / 32 / 48 / 64 / 80 / 96 KB.
  - Flash consists of 16 / 32 / 64 / 128 / 256 / 384 / 512 / 768 / 1024 KB.
- Peripherals:
  - Each F1-series includes various peripherals that vary from line to line.
- IC packages: VFQFPN36, VFQFPN48, LQFP48, WLCSP64, TFBGA64, LQFP64, LQFP100, LFBGA100, LQFP144, LFBGA144.

### STM32 F2

The STM32 F2-series of STM32 microcontrollers based on the ARM Cortex-M3 core. It is the most recent and fastest Cortex-M3 series. The F2 is pin-to-pin compatible with the STM32 F4-series. The summary for this series is:

- Core:
  - ARM Cortex-M3 core at a maximum clock rate of 120 MHz.
- Memory:
  - Static RAM consists of 64 / 96 / 128 KB general purpose, 4 KB battery-backed, 80 bytes battery-backed with tamper-detection erase.
  - Flash consists of 128 / 256 / 512 / 768 / 1024 KB general purpose, 30 KB system boot, 512 bytes one-time programmable (OTP), 16 option bytes.
  - Each chip has a factory-programmed 96-bit unique device identifier number.
- Peripherals:
  - Common peripherals included in all IC packages are USB 2.0 OTG HS, two CAN 2.0B, one SPI + two SPI or I²S, three I²C, four USART, two UART, SDIO/MMC, twelve 16-bit timers, two 32-bit timers, two watchdog timers, temperature sensor, 16 or 24 channels into three ADCs, two DACs, 51 to 140 GPIOs, sixteen DMA, real-time clock (RTC), cyclic redundancy check (CRC) engine, random number generator (RNG) engine. Larger IC packages add 8/16-bit external memory bus capabilities.
  - The STM32F2x7 models add Ethernet MAC, camera interface, USB 2.0 OTG FS.
  - The STM32F21x models add a cryptographic processor for DES / TDES / AES, and a hash processor for SHA-1 and MD5.
- Oscillators consists of internal (16 MHz, 32 kHz), optional external (4 to 26 MHz, 32.768 to 1000 kHz).
- IC packages: WLCSP64, LQFP64, LQFP100, LQFP144, LQFP176, UFBGA176.
- Operating voltage range is 1.8 to 3.6 volt.

### STM32 F3

The STM32 F3-series is the second group of STM32 microcontrollers based on the ARM Cortex-M4F core. The F3 is almost pin-to-pin compatible with the STM32 F1-series. The summary for this series is:

- Core:
  - ARM Cortex-M4F core at a maximum clock rate of 72 MHz.
- Memory:
  - Static RAM consists of 16 / 24 / 32 / 40 KB general purpose with hardware parity check, 0 / 8 KB core coupled memory (CCM) with hardware parity check, 64 / 128 bytes battery-backed with tamper-detection erase.
  - Flash consists of 64 / 128 / 256 KB general purpose, 8 KB system boot, and option bytes.
  - Each chip has a factory-programmed 96-bit unique device identifier number.
- Peripherals:
  - Each F3-series includes various peripherals that vary from line to line.
- Oscillators consists of internal (8 MHz, 40 kHz), optional external (1 to 32 MHz, 32.768 to 1000 kHz).
- IC packages: LQFP48, LQFP64, LQFP100, UFBGA100.
- Operating voltage range is 2.0 to 3.6 volt.

The distinguishing feature for this series is presence of four fast, 12-bit, simultaneous sampling ADCs (multiplexer to over 30 channels), and four matched, 8 MHz bandwidth op-amps with all pins exposed and additionally internal PGA (Programmable Gain Array) network. The exposed pads allow for a range of analog signal conditioning circuits like band-pass filters, anti-alias filters, charge amplifiers, integrators/differentiators, 'instrumentation' high-gain differential inputs, and other. This eliminates need for external op-amps for many applications. The built-in two-channel DAC has arbitrary waveform as well as a hardware-generated waveform (sine, triangle, noise etc.) capability. All analog devices can be completely independent, or partially internally connected, meaning that one can have nearly everything that is needed for an advanced measurement and sensor interfacing system in a single chip.

The four ADCs can be simultaneously sampled making a wide range of precision analog control equipment possible. It is also possible to use a hardware scheduler for the multiplexer array, allowing good timing accuracy when sampling more than 4 channels, independent of the main processor thread. The sampling and multiplexing trigger can be controlled from a variety of sources including timers and built-in comparators, allowing for irregular sampling intervals where needed.

STM32F37/38xxx integrate a 14-effective number of bits delta-sigma ADC.

The op-amps inputs feature 2-to-1 analog multiplexer, allowing for a total of eight analog channels to be pre-processed using the op-amp; all the op-amp outputs can be internally connected to ADCs.

### STM32 F4

The STM32 F4-series is the first group of STM32 microcontrollers based on the ARM Cortex-M4F core. The F4-series is also the first STM32 series to have DSP and floating-point instructions. The F4 is pin-to-pin compatible with the STM32 F2-series and adds higher clock speed, 64 KB CCM static RAM, full-duplex I²S, improved real-time clock, and faster ADCs. The summary for this series is:

- Core:
  - ARM Cortex-M4F core at a maximum clock rate of 84 / 100 / 168 / 180 MHz.
- Memory:
  - Static RAM consists of up to 192 KB general-purpose, 64 KB core-coupled memory (CCM), 4 KB battery-backed, 80 bytes battery-backed with tamper-detection erase.
  - Flash consists of 512 / 1024 / 2048 KB general-purpose, 30 KB system boot, 512 bytes one-time programmable (OTP), 16 option bytes.
  - Each chip has a factory-programmed 96-bit unique device identifier number.
- Peripherals:
  - Common peripherals included in all IC packages are USB 2.0 OTG HS and FS, two CAN 2.0B, one SPI + two SPI or full-duplex I²S, three I²C, four USART, two UART, SDIO for SD/MMC cards, twelve 16-bit timers, two 32-bit timers, two watchdog timers, temperature sensor, 16 or 24 channels into three ADCs, two DACs, 51 to 140 GPIOs, sixteen DMA, improved real-time clock (RTC), cyclic redundancy check (CRC) engine, random number generator (RNG) engine. Larger IC packages add 8/16-bit external memory bus capabilities.
    - Digital filter for sigma-delta modulators (DFSDM) interface in STM32F412 and STM32F413/423 lines
  - The STM32F4x7 models add Ethernet MAC and camera interface.
  - The STM32F41x/43x models add a cryptographic processor for DES / TDES / AES, and a hash processor for SHA-1 and MD5.
  - The STM32F4x9 models add a LCD-TFT controller.
- Oscillators consists of internal (16 MHz, 32 kHz), optional external (4 to 26 MHz, 32.768 to 1000 kHz).
- IC packages: WLCSP64, LQFP64, LQFP100, LQFP144, LQFP176, UFBGA176. STM32F429/439 also offers LQFP208 and UFBGA216.
- Operating voltage range is 1.8 to 3.6 volt.

### STM32 F7

The STM32 F7-series is a group of STM32 microcontrollers based on the ARM Cortex-M7F core. Many of the F7 series are pin-to-pin compatible with the STM32 F4-series.

Core:

- ARM Cortex-M7F core at a maximum clock rate of 216 MHz.

Many of STM32F76xxx and STM32F77xxx models have a digital filter for sigma-delta modulators (DFSDM) interface.

### STM32 G0

The STM32 G0-series is a next generation of Cortex-M0/M0+ microcontrollers for budget market segment, offering the golden mean in productivity and power efficiency, e.g. better power efficiency and performance compared to the older F0 series and higher performance compared to ultra low power L0 series

- Core:
  - ARM Cortex-M0+ core at a maximum clock rate of 64 MHz.
  - Debug interface is SWD with breakpoints and watchpoints. JTAG debugging isn't supported.
- Memory:
  - Static RAM sizes of 8 to 128 KB general purpose with hardware parity checking and up to 144 KB without hardware parity checking, 5x 32-bit battery-backed registers with tamper-detection erase.
  - Flash sizes of 16 to 512 KB.

### STM32 G4

The STM32 G4-series is a next generation of Cortex-M4F microcontrollers aiming to replace F3 series, offering the golden mean in productivity and power efficiency, e.g. better power efficiency and performance compared to the older F3/F4 series and higher performance compared to ultra low power L4 series, integrated several hardware accelerators.

- Core:
  - ARM Cortex-M4F core at a maximum clock rate of 170 MHz with FPU and DSP instructions
- Mathematical accelerators:
  - CORDIC (trigonometric and hyperbolic functions)
  - FMAC (filtering functions)
- Memory:
  - Flash memory with error-correcting code (ECC) and sizes of 128 to 512 KB.
  - Static RAM sizes of 32 to 128 KB with hardware parity checking and CCM-SRAM routine booster, 32x 32-bit battery-backed registers with tamper-detection erase.
- Rich advanced analog peripherals (comparator, op-amps, DAC)
- ADC with hardware oversampling (16-bit resolution) up to 4 Msps
- High-resolution timer version 2
- USB Type-C interface with Power Delivery including physical layer (PHY)
- Securable memory area
- AES hardware encryption

### STM32 H7

The STM32 H7-series is a group of high performance STM32 microcontrollers based on the ARM Cortex-M7F core with double-precision floating point unit and optional second Cortex-M4F core with single-precision floating point. Cortex-M7F core can reach working frequency up to 600 MHz, while Cortex-M4F - up to 240 MHz. Each of these cores can work independently or as master/slave core.

The STM32H7 Series is the first series of STM32 microcontrollers in 40 nm process technology and the first series of ARM Cortex-M7-based microcontrollers which is able to run up to 600 MHz, allowing a performance boost versus previous series of Cortex-M microcontrollers, reaching new performance records of 1284 DMIPS and 3174 CoreMark.

### STM32 L0

The STM32 L0-series is the first group of STM32 microcontrollers based on the ARM Cortex-M0+ core. This series targets low power applications. The summary for this series is:

- Core:
  - ARM Cortex-M0+ core at a maximum clock rate of 32 MHz.
  - Debug interface is SWD with breakpoints and watchpoints. JTAG debugging isn't supported.
- Memory:
  - Static RAM sizes of 8 KB general purpose with hardware parity checking, 20 bytes battery-backed with tamper-detection erase.
  - Flash sizes of 32 or 64 KB general purpose (with ECC).
  - EEPROM sizes of 2 KB (with ECC).
  - ROM which contains a boot loader with optional reprogramming of the flash from USART1, USART2, SPI1, SPI2.
  - Each chip has a factory-programmed 96-bit unique device identifier number.
- Peripherals:
  - two USART, one low-power UART, two I²C, two SPI or one I²S, one full-speed USB (only L0x2 and L0x3 chips).
  - one 12-bit ADC with multiplexer, one 12-bit DAC, two analog comparators, temperature sensor.
  - timers, low-power timers, watchdog timers, 5 V-tolerant GPIOs, real-time clock, DMA controller, CRC engine.
  - capacitive touch sense and 32-bit random number generator (only L0x2 and L0x3 chips), LCD controller (only L0x3 chips), 128-bit AES engine (only L06x chips).
- Oscillators consists of optional external 1 to 24 MHz crystal or oscillator, optional external 32.768 kHz crystal or ceramic resonator, multiple internal oscillators, and one PLL.
- IC packages are LQFP48, LQFP64, TFBGA64.
- Operating voltage range is 1.8 to 3.6 volt, including a programmable brownout detector.

### STM32 L1

The STM32 L1-series was the first group of STM32 microcontrollers with a primary goal of ultra-low power usage for battery-powered applications. The summary for this series is:

- Core:
  - ARM Cortex-M3 core at a maximum clock rate of 32 MHz.
- Memory:
  - Static RAM consists of 10 / 16 / 32 / 48 / 80 KB general purpose, 80 bytes with tamper-detection erase.
  - Flash consists of 32 / 64 / 128 / 256 / 384 / 512 KB general purpose with ECC, 4 / 8 KB system boot, 32 option bytes, EEPROM consists of 4 / 8 / 12 / 16 KB data storage with ECC.
  - Each chip has a factory-programmed 96-bit unique device identifier number.
- Peripherals:
  - Common peripherals included in all IC packages are USB 2.0 FS, two SPI, two I²C, three USART, eight 16-bit timers, two watchdog timers, temperature sensor, 16 to 24 channels into one ADC, two DACs, 37 to 83 GPIOs, seven DMA, real-time clock (RTC), cyclic redundancy check (CRC) engine. The STM32FL152 line adds a LCD controller.
- Oscillators consists of internal (16 MHz, 38 kHz, variable 64 kHz to 4 MHz), optional external (1 to 26 MHz, 32.768 to 1000 kHz).
- IC packages: UFQFPN48, LQFP48, LQFP64, TFBGA64, LQFP100, UFBGA100.
- Operating voltage range is 1.65 to 3.6 volt.

### STM32 L4

The STM32 L4-series is an evolution of STM32L1-series of ultra-low power microcontrollers. An example of L4 MCU is STM32L432KC in UFQFPN32 package, that has:

- ARM 32-bit Cortex-M4 core
- 80 MHz max CPU frequency
- VDD from 1.65 V to 3.6 V
- 256 KB Flash, 64 KB SRAM
- General purpose timers (4), SPI/I2S (2), I2C (2), USART (2), 12-bit ADC with 10 channels (1), GPIO (20) with external interrupt capability, RTC
- Random number generator (TRNG for HW entropy).
- Digital filter for sigma-delta modulators (DFSDM) interface

### STM32 L4+

The STM32 L4+-series is expansion of STM32L4-series of ultra-low power microcontrollers, providing more performance, more embedded memory and richer graphics and connectivity features while keeping ultra-low-power capability.

Main features:

- ARM 32-bit Cortex-M4 core
- 120 MHz max CPU frequency
- VDD from 1.71 V to 3.6 V
- Ultra low power consumption: down to 41 μA/MHz, 20 nA power consumption in power-down mode.
- Up to 2048 KB Flash, up to 640 KB SRAM
- Advanced peripherals, including TFT-LCD controller, Chrom-ART Accelerator, Camera interface etc.
- Digital filter for sigma-delta modulators (DFSDM) interface

### STM32 L5

The STM32 L5-series is an evolution of STM32L-series of ultra-low power microcontrollers:

- ARM Cortex-M33 32-bit core
- 110 MHz max CPU frequency

### STM32 U0

The STM32 U0-series is an entry-level addition to the STM32-series of ultra-low power microcontrollers:

- ARM Cortex-M0+ core at a maximum clock rate of 56 MHz.
- Static consumption of 160 nA in standby mode with RTC (Real-Time Clock) and 16 nA in shutdown.
- Up to 256KB of Flash, package options up to 81 pins.
- Integrated LCD segment display controller.
- Targets SESIP Level 3, PSA-Certified Level 1, and NIST certifications.

### STM32 U3

The STM32 U3-series is a near-threshold design of ultra-low power microcontrollers that shares similarities with the U5:

- ARM Cortex-M33 32-bit core with 96 MHz max CPU frequency
- 40-nm process node with down to 16 μA/MHz in active mode, 110 nA in low power mode
- Up to 1 MB of flash memory.
- Up to 256 KB of SRAM.
- TrustZone

### STM32 U5

The STM32 U5-series is an evolution of STM32L-series of ultra-low power microcontrollers:

- ARM Cortex-M33 32-bit core with 160 MHz max CPU frequency
- 40-nm process node with down to 16 μA/MHz in active mode, 110 nA in low power mode
- Up to 4 MB of flash memory.
- Up to 3 MB of SRAM.
- Advanced Vector Graphic GPU (NeoChromVG).

## Development boards

### Arduino Nano style

The following boards have Arduino Nano pin-compatible male pin headers with 0.6-inch row-to-row DIP-30 footprint, but these boards have 3.3 volt logic I/O, instead of 5 volt logic I/O for an Arduino Nano "R3" and Nano R4.

- Blue Pill board has a STM32F103C8T6 microcontroller. Unfortunately, most blue pill boards now contain a fake STM32 from China.
- Black Pill board has a STM32F401CCU6 or STM32F411CEU6 microcontroller.
- ST Nucleo-32 boards have Arduino Nano pin-compatible male pin headers too. (see Nucleo section below)

### Arduino Uno style

The following boards have Arduino Uno R3 pin-compatible female pin headers for Arduino shields, but these boards have 3.3 volt logic I/O, instead of 5 volt logic I/O for an Arduino Uno.

- Maple board by Leaflabs has a STM32F103RB microcontroller. A C/C++ library called libmaple is available to make it easier to migrate from Arduino.
- OLIMEXINO-STM32 board by Olimex has a STM32F103RBT6 microcontroller and similar to the Maple board.
- Netduino with support for .NET Micro Framework.
- ST Nucleo-64 and Nucleo-144 boards have female pin headers for Arduino shields too. (see Nucleo section below)

### ST Nucleo

There are three Nucleo board types, each supporting a different STM32 IC package footprint. As of fall 2025, there were over eighty Nucleo board variations: 9 of Nucleo-32, 39 of Nucleo-64, 28 of Nucleo-144; 1 obsolete Nucleo-32, 5 obsolete Nucleo-144.

All Nucleo boards by STMicroelectronics have an additional onboard ST-LINK host adapter chip which supplies SWD debugging, virtual COM port, and mass storage over USB. The debugger embedded on Nucleo boards can be converted to the SEGGER J-Link debugger protocol. Though some STM32 microcontrollers have a real-time clock (RTC) peripheral and/or battery-back SRAM, none of the Nucleo boards have a battery holder.

**Nucleo-32**

Nucleo-32 boards have 32-pin STM32 ICs and Arduino Nano pin-compatible male pin headers with 0.6-inch row-to-row DIP-30 footprint. The unlisted Nucleo-F301K8 is obsolete.

**Nucleo-64**

Nucleo-64 boards have 64-pin STM32 ICs (except Nucleo-C031C6 and Nucleo-C051C8 have 48-pin ICs), Arduino Uno R3 female headers for shields, ST Morpho male pin headers (two 19x2), some board have a second USB connector, one board (NUCLEO-C092RC) has a CAN-FD bus connector.

**Nucleo-144**

Nucleo-144 boards have 144-pin STM32 ICs (except Nucleo-H7S3L8 has 225-pin IC and Nucleo-N657X0-Q has 264-pin IC), Arduino Uno R3 female headers for shields, ST Zio female headers, ST Morpho male pin headers (two 19x2), some have a second USB connector, some have a RJ45 Ethernet connector. The unlisted Nucleo-F429ZI, Nucleo-F746ZG, Nucleo-H743ZI, Nucleo-H743ZI2, Nucleo-H745ZI-Q are obsolete.

**Table**

The following table compares various features of official Nucleo boards from STMicroelectronics. The left half of the table contains details about each board, the right half of the table contains details about the microcontroller (MCU) on each board. Table columns can be sorted by clicking on the arrows in the top row.

Various terms have been shortened or simplified to reduce the column widths: mini means miniUSB, micro means microUSB, conn means connector, dev means device. The suffixes MHz and KB have been moved to the top row. The Nucleo board types have been reduced to numeric values. See "Table notes" (under table) for additional explainations.

Nucleo

Board

Name

Nucleo

Board

Type

Nucleo

Host

USB

Conn

Nucleo

Dev

USB

Conn

Nucleo

Other

Conn

Nucleo

Debug

Conn

MCU

Part

Number

MCU

Clock

(

MHz

)

MCU

ARM

Cortex

MCU

Cache

(

KB

)

MCU

Flash

(KB)

MCU

EEPROM

,

OTP

(KB)

MCU

SRAM

(KB)

Nucleo-F031K6

32

micro-AB FS

STM32F031K6T6

48

M0

32

4

Nucleo-F042K6

32

micro-AB FS

STM32F042K6T6

48

M0

32

6

Nucleo-F303K8

32

micro-AB FS

STM32F303K8T6

72

M4F

64

16

Nucleo-G031K8

32

micro-B FS

STM32G031K8T6

64

M0+

64(ECC)

8

Nucleo-G431KB

32

micro-B

HS

STM32G431KBT6

170

M4F

128(ECC)

32

Nucleo-L011K4

32

micro-AB FS

STM32L011K4T6

32

M0+

16(ECC)

0.5(ECC) EEPROM

2

Nucleo-L031K6

32

micro-AB FS

STM32L031K6T6

32

M0+

32(ECC)

1(ECC) EEPROM

8

Nucleo-L412KB

32

micro-AB FS

STM32L412KBU6

80

M4F

128(ECC)

40

Nucleo-L432KC

32

micro-AB FS

STM32L432KCU6

80

M4F

256(ECC)

64

Nucleo-C031C6

64

micro-B FS

6x1 2.54mm

STM32C031C6T6

48

M0+

32

12

Nucleo-C051C8

64

micro-B FS

6x1 2.54mm

STM32C051C8T6

48

M0+

64

12

Nucleo-C071RB

64

USB-C FS

USB-C FS

5x2 1.27mm

STM32C071RBT6

48

M0+

128

24

Nucleo-C092RC

64

USB-C FS

CAN-FD

5x2 1.27mm

STM32C092RCT6

48

M0+

256

30

Nucleo-C542RC

64

USB-C

HS

USB-C FS

CAN-FD

5x2 1.27mm

STM32C542RC

144

M33F

8I

256(ECC)

64(ECC) Data Flash,

4.5(ECC) OTP

64

Nucleo-C562RE

64

USB-C

HS

USB-C FS

CAN-FD

5x2 1.27mm

STM32C562RE

144

M33F

8I

512(ECC)

64(ECC) Data Flash,

4.5(ECC) OTP

128

Nucleo-F030R8

64

mini-B FS

6x1 2.54mm

STM32F030R8T6

48

M0

64

8

Nucleo-F070RB

64

mini-B FS

6x1 2.54mm

STM32F070RBT6

48

M0

128

16

Nucleo-F072RB

64

mini-B FS

6x1 2.54mm

STM32F072RBT6

48

M0

128

16

Nucleo-F091RC

64

mini-B FS

6x1 2.54mm

STM32F091RCT6

48

M0

256

32

Nucleo-F103RB

64

mini-B FS

6x1 2.54mm

STM32F103RBT6

72

M3

128

20

Nucleo-F302R8

64

mini-B FS

6x1 2.54mm

STM32F302R8T6

72

M4F

64

16

Nucleo-F303RE

64

mini-B FS

6x1 2.54mm

STM32F303RET6

72

M4F

512

80

Nucleo-F334R8

64

mini-B FS

6x1 2.54mm

STM32F334R8T6

72

M4F

64

16

Nucleo-F401RE

64

mini-B FS

6x1 2.54mm

STM32F401RET6

84

M4F

512

0.5 OTP

96

Nucleo-F410RB

64

mini-B FS

6x1 2.54mm

STM32F410RBT6

100

M4F

128

0.5 OTP

32

Nucleo-F411RE

64

mini-B FS

6x1 2.54mm

STM32F411RET6

100

M4F

512

0.5 OTP

128

Nucleo-F446RE

64

mini-B FS

6x1 2.54mm

STM32F446RET6

180

M4F

512

132

Nucleo-G070RB

64

micro-B FS

6x1 2.54mm

STM32G070RBT6

64

M0+

128(ECC)

32

Nucleo-G071RB

64

micro-B FS

6x1 2.54mm

STM32G071RBT6

64

M0+

128(ECC)

32

Nucleo-G0B1RE

64

micro-B FS

6x1 2.54mm

STM32G0B1RET6

64

M0+

512(ECC)

128

Nucleo-G431RB

64

micro-B

HS

5x2 1.27mm

STM32G431RBT6

170

M4F

128(ECC)

32

Nucleo-G474RE

64

micro-B

HS

5x2 1.27mm

STM32G474RET6

170

M4F

512(ECC)

132

Nucleo-G491RE

64

micro-B

HS

5x2 1.27mm

STM32G491RET6

170

M4F

512(ECC)

112

Nucleo-H503RB

64

USB-C

HS

USB-C FS

5x2 1.27mm

STM32H503RBT6

250

M33F

8I

128(ECC)

2(ECC) OTP

34

Nucleo-H533RE

64

USB-C

HS

USB-C FS

5x2 1.27mm

STM32H533RET6

250

M33F

8I, 4Dx

512(ECC)

2(ECC) OTP

274

Nucleo-L010RB

64

mini-B FS

6x1 2.54mm

STM32L010RBT6

32

M0+

128

0.5 EEPROM

20

Nucleo-L053R8

64

mini-B FS

6x1 2.54mm

STM32L053R8T6

32

M0+

64(ECC)

2(ECC) EEPROM

8

Nucleo-L073RZ

64

mini-B FS

6x1 2.54mm

STM32L073RZT6

32

M0+

192(ECC)

6(ECC) EEPROM

20

Nucleo-L152RE

64

mini-B FS

6x1 2.54mm

STM32L152RET6

32

M3

512(ECC)

16(ECC) EEPROM

80

Nucleo-L412RB-P

64

micro-B FS

6x1 2.54mm

STM32L412RBT6P

80

M4F

128(ECC)

40

Nucleo-L433RC-P

64

micro-B FS

6x1 2.54mm

STM32L433RCT6P

80

M4F

256(ECC)

64

Nucleo-L452RE

64

mini-B FS

6x1 2.54mm

STM32L452RET6

80

M4F

512(ECC)

160

Nucleo-L452RE-P

64

micro-B FS

6x1 2.54mm

STM32L452RET6P

80

M4F

512(ECC)

160

Nucleo-L476RG

64

mini-B FS

6x1 2.54mm

STM32L476RGT6

80

M4F

1024(ECC)

128

Nucleo-U031R8

64

micro-B FS

5x2 1.27mm

STM32U031R8T6

56

M0+

64

12

Nucleo-U083RC

64

micro-B FS

5x2 1.27mm

STM32U083RCT6

56

M0+

256

40

Nucleo-U385RG-Q

64

USB-C

HS

USB-C FS

5x2 1.27mm

STM32U385RGT6Q

96

M33F

8I

1024(ECC)

256

Nucleo-U545RE-Q

64

USB-C

HS

USB-C FS

5x2 1.27mm

STM32U545RET6Q

160

M33F

8I, 4Dx

512(ECC)

274

Nucleo-C5A3ZG

144

USB-C

HS

USB-C FS

Ethernet

RJ45

100M

10x2 1.27mm

STM32C5A3ZG

144

M33F

8I

1024(ECC)

64(ECC) Data Flash,

4.5(ECC) OTP

256

Nucleo-F207ZG

144

micro-B FS

micro-AB FS

Ethernet

RJ45 100M

6x1 2.54mm

STM32F207ZGT6

120

M3

1024(ECC)

132

Nucleo-F303ZE

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32F303ZET6

72

M4F

512(ECC)

80

Nucleo-F412ZG

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32F412ZGT6

100

M4F

1024

0.5 OTP

256

Nucleo-F413ZH

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32F413ZHT6

100

M4F

1536

0.5 OTP

320

Nucleo-F439ZI

144

micro-B FS

micro-AB FS

Ethernet

RJ45 100M

6x1 2.54mm

STM32F439ZIT6

180

M4F

2048

256

Nucleo-F446ZE

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32F446ZET6

180

M4F

512

132

Nucleo-F722ZE

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32F722ZET6

216

M7F

8I, 8D

512

0.5 OTP

276

Nucleo-F756ZG

144

micro-B FS

micro-AB FS

Ethernet

RJ45 100M

6x1 2.54mm

STM32F756ZGT6

216

M7F

4I, 4D

1024

1 OTP

340

Nucleo-F767ZI

144

micro-B FS

micro-AB FS

Ethernet

RJ45 100M

6x1 2.54mm

STM32F767ZIT6

216

M7FDP

16I, 16D

2048

532

Nucleo-H563ZI

144

USB-C

HS

USB-C FS

Ethernet

RJ45 100M

10x2 1.27mm

STM32H563ZIT6

250

M33F

8I, 4Dx

2048(ECC)

2(ECC) OTP

644

Nucleo-H5E5ZJ

144

USB-C

HS

USB-C

HS

Ethernet

RJ45 100M

10x2 1.27mm

STM32H5E5ZJT6

250

M33F

16I, 8Dx

4096(ECC)

192(ECC) Data Flash,

2(ECC) OTP

1476

Nucleo-H723ZG

144

micro-B

HS

micro-AB FS

Ethernet

RJ45 100M

5x2 1.27mm

STM32H723ZGT6

550

M7FDP

32I, 32D

1024(ECC)

564

Nucleo-H753ZI

144

micro-B

HS

micro-AB FS

Ethernet

RJ45 100M

5x2 1.27mm

STM32H753ZIT6

480

M7FDP

16I, 16D

2048(ECC)

1060

Nucleo-H755ZI-Q

144

micro-B

HS

micro-AB FS

Ethernet

RJ45 100M

5x2 1.27mm

STM32H755ZIT6

480,

240

M7FDP

& M4F

16I, 16D

2048(ECC)

1060

Nucleo-H7A3ZI-Q

144

micro-B

HS

micro-AB FS

5x2 1.27mm

STM32H7A3ZIT6Q

280

M7FDP

16I, 16D

2048(ECC)

1(ECC) OTP

1480

Nucleo-H7S3L8

144

USB-C

HS

USB-C

HS

Ethernet

RJ45 100M

10x2 1.27mm

STM32H7S3L8H6

600

M7FDP

32I, 32D

64(ECC)

1(ECC) OTP

548

Nucleo-L496ZG

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L496ZGT6

80

M4F

1024(ECC)

1(ECC) OTP

320

Nucleo-L496ZG-P

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L496ZGT6P

80

M4F

1024(ECC)

1(ECC) OTP

320

Nucleo-L4A6ZG

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L4A6ZGT6

80

M4F

1024(ECC)

1(ECC) OTP

320

Nucleo-L4P5ZG

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L4P5ZGT6

120

M4F

1024(ECC)

1(ECC) OTP

320

Nucleo-L4R5ZI

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L4R5ZIT6

120

M4F

2048(ECC)

1(ECC) OTP

640

Nucleo-L4R5ZI-P

144

micro-B FS

micro-AB FS

6x1 2.54mm

STM32L4R5ZIT6P

120

M4F

2048(ECC)

1(ECC) OTP

640

Nucleo-L552ZE-Q

144

micro-B FS

USB-C FS

6x1 2.54mm

STM32L552ZET6Q

110

M33F

8I

512(ECC)

0.5(ECC) OTP

256

Nucleo-N657X0-Q

144

USB-C

HS

USB-C

HS

Ethernet

RJ45

1G

,

Camera

CSI

22-pin

10x2 1.27mm

STM32N657X0H3Q

800,

1000

M55FDP

& NPU

32I, 32D

0

1.5 OTP

4424

Nucleo-U3C5ZI-Q

144

micro-B

HS

USB-C FS

CAN-FD

10x2 1.27mm

STM32U3C5ZIT6Q

96

M33F

8I

2048(ECC)

0.5(ECC) OTP

640

Nucleo-U575ZI-Q

144

micro-B

HS

USB-C FS

5x2 1.27mm

STM32U575ZIT6Q

160

M33F

8I, 4Dx

2048(ECC)

0.5(ECC) OTP

722

Nucleo-U5A5ZJ-Q

144

micro-B

HS

USB-C

HS

5x2 1.27mm

STM32U5A5ZJT6Q

160

M33F

32I, 16Dx

4096(ECC)

0.5(ECC) OTP

2450

**Table notes**

- *Nucleo Board Name* column - STMicroelectronics Nucleo board name and part number.
- *Nucleo Board Type* column - Nucleo board type. 32 means Nucleo-32, 64 means Nucleo-64, 144 means Nucleo-144.
- *Nucleo Host USB Conn* column - USB host connector type (and speed) on each Nucleo board. "FS" means Full Speed (12 Mbps max), "HS" means High Speed (480 Mbps max).
- *Nucleo Dev USB Conn* column - USB device connector type (and speed) on each Nucleo board. Mini means miniUSB, Micro means microUSB.
- *Nucleo Other Conn* column - Other connectors on each Nucleo board, such as CAN-FD, Ethernet, Camera. Ethernet includes its connector (RJ45) and maximum bit rate speed.
- *Nucleo Debug Conn* column - Debug connector (pin header) on each Nucleo board, including pin count and pitch (distance between center of pins in millimeters.
- *MCU Part Number* column - STMicroelectronics microcontroller part number of the IC on each Nucleo board. All MCU information in this table was sourced from official datasheets in this column.
- *MCU Clock (MHz)* column - Maximum clock rate (MHz) of the processor core inside the microcontroller. MHz means 106 Hertz, also known as megahertz.
- *MCU ARM Cortex* column - ARM Cortex-M processor core family inside the microcontroller. The shortened "M0+" in the table means "ARM Cortex M0+". An appended "F" means the processor core contains a FPU (floating-point unit) with single-precision, appended "DP" means the FPU also supports double precision.
- *MCU Cache (KB)* column - Processor cache memory size (KB) and type inside the microcontroller. "I" means instruction cache, "D" means data cache, "Dx" means data cache for external memory.
- *MCU Flash (KB)* column - Total Flash memory size (KB) inside the microcontroller.
- *MCU EEPROM, OTP (KB)* column - Total EEPROM or One-Time Programmable (OTP) memory size (KB) inside the microcontroller.
- *MCU SRAM (KB)* column - Total Static RAM memory size (KB) inside the microcontroller. Total size assumes ECC and parity memory are enabled. Total size includes battery-backed SRAM. Total size doesn't include cache memory or peripheral buffer memory.
- For memories, ECC means memory has error correction code checking, Parity means memory has parity checking.

### ST Discovery

The following **Discovery** evaluation boards are sold by STMicroelectronics to provide a quick and easy way for engineers to evaluate their microcontroller chips. These kits are available from various distributors for less than US$20. The STMicroelectronics evaluation product licence agreement forbids their use in any production system or any product that is offered for sale.

Each board includes an on-board ST-LINK for programming and debugging via a Mini-B USB connector. The power for each board is provided by a choice of the 5 V via the USB cable, or an external 5 V power supply. They can be used as output power supplies of 3 V or 5 V (current must be less than 100 mA). All Discovery boards also include a voltage regulator, reset button, user button, multiple LEDs, SWD header on top of each board, and rows of header pins on the bottom.

An open-source project was created to allow Linux to communicate with the ST-LINK debugger.

ChibiOS/RT, a free RTOS, has been ported to run on some of the Discovery boards.

**STM32L476GDISCOVERY**

- A discovery board for STM32L476VGT6 microcontroller with 80 MHz ARM Cortex-M4F core, 1024 KB flash, 128 KB RAM in LQFP100 package

**STM32F429IDISCOVERY**

- A discovery board for STM32F429ZIT6 microcontroller with 180 MHz ARM Cortex-M4F core, 2048 KB flash, 256 KB RAM, 4 KB battery-backed RAM in LQFP144 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 8 MB SDRAM (IS42S16400J), 2.4-inch 320x200 TFT LCD color display (SF-TC240T), touchscreen controller (STMPE811), gyroscope (L3GD20), 2 user LEDs, user button, reset button, Full-Speed USB OTG to second Micro-AB USB connector, and two 32x2 male pin headers.

**STM32F4DISCOVERY**

- A discovery board for STM32F407VGT6 microcontroller with 168 MHz ARM Cortex-M4F core, 1024 KB flash, 192 KB RAM, 4 KB battery-backed RAM in LQFP100 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, accelerometer (LIS302DL), microphone (MP45DT02), audio codec (CS43L22), 3.5 mm audio jack, 4 user LEDs, user button, reset button, Full-Speed USB OTG to second Micro-AB USB connector, and two 25x2 male pin headers.
- A separate STM32F4DIS-BB baseboard is available.

**STM32F401CDISCOVERY**

- A discovery board for STM32F401VCT6 microcontroller with 84 MHz ARM Cortex-M4F core, 256 KB flash, 64 KB RAM in LQFP100 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, accelerometer/compass (LSM303DLHC), gyroscope (L3GD20), microphone (MP45DT02), audio codec (CS43L22), 3.5 mm audio jack, 4 user LEDs, user button, reset button, Full-Speed USB OTG to second Micro-AB USB connector, and two 25x2 male pin headers.

**STM32F3DISCOVERY**

- A discovery board for STM32F303VCT6 microcontroller with 72 MHz ARM Cortex-M4F core, 256 KB flash, 48 KB RAM (24K with parity) in LQFP100 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, accelerometer/compass (LSM303DLHC), gyroscope (L3GD20), 8 user LEDs, user button, reset button, Full-Speed USB to second Mini-B USB connector, and two 25x2 male pin headers.

**STM32VLDISCOVERY**

- A discovery board for STM32F100RBT6 microcontroller with 24 MHz ARM Cortex-M3 core, 128 KB flash, 8 KB RAM in LQFP64 package.
- This board includes an integrated ST-LINK debugger via Mini-B USB connector, 2 user LEDs, user button, reset button, and two 28x1 male pin headers.

**STM32L-DISCOVERY**

- A discovery board for STM32L152RBT6 microcontroller with 32 MHz ARM Cortex-M3 core, 128 KB flash (with ECC), 16 KB RAM, 4 KB EEPROM (with ECC) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 24-segment LCD, touch sensors, 2 user LEDs, user button, reset button, and two 28x1 male pin headers.
- This board is currently End-Of-Life and replaced by the 32L152CDISCOVERY board.

**STM32L152CDISCOVERY**

- A discovery board for STM32L152RCT6 microcontroller with 32 MHz ARM Cortex-M3 core, 256 KB flash (with ECC), 32 KB RAM, 8 KB EEPROM (with ECC) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 24-segment LCD, touch sensors, 2 user LEDs, user button, reset button, and two 28x1 male pin headers.

**STM32L100CDISCOVERY**

- A discovery board for STM32L100RCT6 microcontroller with 32 MHz ARM Cortex-M3 core, 256 KB flash (with ECC), 16 KB RAM, 4 KB EEPROM (with ECC) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 2 user LEDs, user button, reset button, and two 33x1 male pin headers.

**STM32F072BDISCOVERY**

- A discovery board for STM32F072RBT6 microcontroller with 48 MHz ARM Cortex-M0 core, 128 KB flash, 16 KB RAM (with parity) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, gyroscope (L3GD20), 4 user LEDs, user button, reset button, linear touch keys, Full-Speed USB to second Mini-B USB connector, and two 33x1 male pin headers.

**STM32F0DISCOVERY**

- A discovery board for STM32F051R8T6 microcontroller with 48 MHz ARM Cortex-M0 core, 64 KB flash, 8 KB RAM (with parity) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 2 user LEDs, user button, reset button, and two 33x1 male pin headers.
- A prototyping perfboard with 0.1-inch (2.54 mm) grid of holes is included.

**STM32F0308DISCOVERY**

- A discovery board for STM32F030R8T6 microcontroller with 48 MHz ARM Cortex-M0 core, 64 KB flash, 8 KB RAM (with parity) in LQFP64 package.
- This board includes an integrated ST-LINK/V2 debugger via Mini-B USB connector, 2 user LEDs, user button, reset button, and two 33x1 male pin headers.
- A prototyping perfboard with 0.1-inch (2.54 mm) grid of holes is included.

### ST Evaluation

The following evaluation kits are sold by STMicroelectronics.

**STM32W-RFCKIT**

- An RF evaluation board for STM32 W-series.
- It contains two boards, each with a STM32W108 SoC microcontroller in VFQFPN40 and VFQFPN48 packages.
- The evaluation board has a built-in 2.4 GHz IEEE 802.15.4 transceiver and Lower MAC (so supports 802.15.4, ZigBee RF4CE, ZigBee Pro, 6LoWPAN (Contiki) wireless protocols). The SoC contains 128-Kbyte flash and 8-Kbyte RAM memory. Flash memory is upgradable too via USB. It has an ARM Serial Wire Debug (SWD) interface (Remote board) and is designed to be powered by USB or with 2 AAA batteries (Remote board). There are two user-defined LEDs (green and yellow) and five push buttons to create easy-to-use remote functions (remote board).

**STM3220G-JAVA**

A ready-to-use Java development kits for its STM32 microcontrollers. The STM3220G-JAVA Starter Kit combines an evaluation version of IS2T's MicroEJ Software Development Kit (SDK) and the STM32F2 series microcontroller evaluation board providing everything engineers need to start their projects. MicroEJ provides extended features to create, simulate, test and deploy Java applications in embedded systems. Support for Graphical User Interface (GUI) development includes a widget library, design tools including storyboarding, and tools for customizing fonts. STM32 microcontrollers that embed Java have a Part Number that ends with J like STM32F205VGT6J.

## Development tools

### ARM Cortex-M

### STM32

**Design utilities**

- Simulink, by MathWorks provides model-based design solutions to design embedded systems. The STM32 Microcontroller Blockset provide parameter tuning, signal monitoring and one-click deployment of Simulink algorithms to STM32 boards with access to peripherals like ADC, PWM, GPIOs, I²C, SPI, SCI, TCP/IP, UDP, etc.

**Flash programming via USART**

All STM32 microcontrollers have a ROM'ed bootloader that supports loading a binary image into its flash memory using one or more peripherals (varies by STM32 family). Since all STM32 bootloaders support loading from the USART peripheral and most boards connect the USART to RS-232 or a USB-to-UART adapter IC, thus it's a universal method to program the STM32 microcontroller. This method requires the target to have a way to enable/disable booting from the ROM'ed bootloader (i.e. jumper / switch / button).

**STM32 C/C++ software libraries**

- HAL (Hardware Abstraction Layer) Drivers
- LL (Low Layer) Drivers
- Human machine interface (HMI) Framework
- Standard peripheral library (deprecated)
- embOS, FreeRTOS, CMSIS-RTOS, ThreadX
- USB device library
- DSP library
- Encryption library
- Motor control library
- MP3 / WMA / Speex codecs and audio engine
- Self-test routines
- Audio kit Far field denoiser for speech recognition

## Documentation

The amount of documentation for all ARM chips can be daunting, especially for newcomers. As microprocessors have increased in capability and complexity, the documentation has grown. The total documentation for all ARM chips consists of documents from the IC manufacturer (STMicroelectronics) and documents from CPU core vendor (ARM Holdings).

A typical top-down documentation tree is: manufacturer website, manufacturer marketing slides, manufacturer datasheet for the exact physical chip, manufacturer detailed reference manual that describes common peripherals and aspects of a physical chip family, ARM core generic user guide, ARM core technical reference manual, ARM architecture reference manual that describes the instruction set(s).

**STM32 documentation tree (top to bottom)**

1. STM32 website.
2. STM32 marketing slides.
3. STM32 datasheet.
4. STM32 reference manual.
5. ARM core website.
6. ARM core generic user guide.
7. ARM core technical reference manual.
8. ARM architecture reference manual.

STMicroelectronics has additional documents, such as: evaluation board user manuals, application notes, getting started guides, software library documents, errata, and more. See External Links section for links to official STM32 and ARM documents.

## Part number decoding

Example:

STM32F407VG

- splits into STM32 F4 07 V G
- means: F4 series, 07 subtype, 100 pin, 1024 KB flash

Decoding:

STM32

xx ww y z

- **xx** – Series family
- **ww** – Subtype, differs by each series family
- **y** – Package pin count
- **z** – Flash memory size

| Family [xx] Family code ARM Core Max Freq (MHz) Max Flash (KB) Max SRAM (KB) Target C0Cortex-M0+4825636Low cost C5Cortex-M33F1441024256Low cost F0Cortex-M04825632Mainstream F1Cortex-M372102496Mainstream F2Cortex-M31201024128High performance F3Cortex-M4F7251280Mainstream F4Cortex-M4F1802048384High performance F7Cortex-M7F2162048512High performance G0Cortex-M0+64512144Mainstream G4Cortex-M4F170512128Mainstream H5Cortex-M33F2502048640High performance H7Cortex-M7F48020481024High performance L0Cortex-M0+3219220Ultra low power L1Cortex-M33251280Ultra low power L4Cortex-M4F801024320Ultra low power L4+Cortex-M4F1202048640Ultra low power L5Cortex-M33F110512256Ultra low power N6Cortex-M55F80004200High performance (machine learning) U0Cortex-M0+5625640Ultra low power U3Cortex-M33F961024256Ultra low power U5Cortex-M33F1602048786Ultra low power WBCortex-M4F641024256Wireless WLCortex-M44825664Wireless | Package pin count [y] Package code Number of pins A169 B208 C48 F20 G28 H40 I176 J8 or 72 K32 M81 N216 Q132 R64 T36 U63 V100 Z144 | Flash size [z] Flash code Flash size (KB) 416 632 864 B128 Z192 C256 D384 E512 F768 G1024 H1536 I2048 J4096 |
|---|---|---|
