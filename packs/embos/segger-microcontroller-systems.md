---
title: "Segger"
source: https://en.wikipedia.org/wiki/Segger_Microcontroller_Systems
domain: embos
license: CC-BY-SA-4.0
tags: embos rtos, segger embos, j-link debugger, stm32 target
fetched: 2026-07-02
---

# Segger

(Redirected from

Segger Microcontroller Systems

)

**Segger Microcontroller** is a private company involved in the embedded systems industry. It provides products used to develop and manufacture four categories of embedded systems: real-time operating systems (RTOS) and software libraries (middleware), debugging and trace probes, programming tools (integrated development environment (IDE), compiler, linker), and in-system programmers (Flasher line of products). The company is headquartered in Monheim am Rhein, Germany, with remote offices in Gardner, Massachusetts; Milpitas, California; and Shanghai, China.

## History

Segger Microcontroller was founded in 1992 by Rolf Segger in Hilden, Germany. The first product was the real-time operating system (RTOS), now named embOS. It was followed by emWin two years later. Initial products focused on RTOS and middleware products. However, the company later produced ISP-programming tools (Flasher) and debug probes (J-Link). In 2015, Segger introduced Embedded Studio, their cross-platform IDE for central processing units conforming to the ARM architecture, though recent versions are also used by RISC-V. All products are developed, maintained and updated in Germany except for Embedded Studio, which is primarily developed by a team of developers in the United Kingdom.

## Product categories

### Debug and trace probes

Segger is most noted for its J-Link family, which supports JTAG (Joint Test Action Group) and SWD (Serial Wire Debug) debug probes for microcontrollers that have older ARM cores (ARM7, ARM9, ARM11), ARM Cortex-M cores (M0, M0+, M1, M3, M4, M7, M23, M33, M85), ARM Cortex-R cores (R4, R5, R8), ARM Cortex-A cores (A5, A7, A8, A9, A12, A15, A17, A53, A72), Renesas RX, Microchip PIC32, SiLab EFM8, RISC-V. It is also repackaged and sold as an OEM item by Analog Devices as the mIDASLink, Atmel as the SAM-ICE, Digi International as the Digi JTAG Link, and IAR Systems as the J-Link and the J-Link KS. This is the only JTAG emulator that can add Segger's patented flash breakpoint software to a debugger to enable the setting of multiple breakpoints in flash while running on an ARM device which is typically hindered by the limited availability of hardware breakpoints.

In the following table, the top group are trace devices, the bottom group are educational / hobbyist devices.

J-Trace & J-Link Models

Model

Host

USB

speed

Host

Ethernet

speed

Host

Wi-Fi

type

Target

voltage

range

Target Trace

connector

(pins, pitch)

Target Debug

connector

(pins, pitch)

Target

download

speed (max)

Target

VCOM

UART

Segger

software

features

Photo

J-Trace PRO

(

ARM & RISC-V

)

3.0

SS

1

Gbit/s

None

1.2V to 5V

19-pins,

1.27mm

(150

MHz

)

20-pins,

2.54mm

(50

MHz

)

4

MByte

/s

None

All

J-Trace PRO Cortex-A/R/M

3.0 SS

1 Gbit/s

None

1.2V to 5V

19-pins,

1.27mm

(150

MHz)

20-pins,

2.54mm

(50

MHz)

4 MByte/s

None

All

J-Trace PRO Cortex-M

3.0 SS

1 Gbit/s

None

1.2V to 5V

19-pins,

1.27mm

(150

MHz)

20-pins,

2.54mm

(50

MHz)

4 MByte/s

None

All

J-Trace PRO RISC-V

3.0 SS

1 Gbit/s

None

1.2V to 5V

19-pins,

1.27mm

(150

MHz)

20-pins,

2.54mm

(50

MHz)

4 MByte/s

None

All

J-Link PRO

PoE

2.0

HS

100

Mbit/s

(

PoE

)

None

1.2V to 5V

None

20-pins,

2.54mm

(50

MHz)

4 MByte/s

2-pins

(

10M

)

All

J-Link PRO

2.0 HS

100 Mbit/s

None

1.2V to 5V

None

20-pins,

2.54mm

(50

MHz)

4 MByte/s

2-pins

(10M)

All

J-Link ULTRA+

2.0 HS

None

None

1.2V to 5V

None

20-pins,

2.54mm

(50

MHz)

4 MByte/s

2-pins

(10M)

All

J-Link

WiFi

2.0 HS

None

802.11b/g/n

(2.4

GHz

)

1.2V to 5V

None

20-pins,

2.54mm

(15

MHz

)

1

MByte

/s

2-pins

(

115.2K

)

All

J-Link PLUS,

J-Link PLUS Compact

2.0 HS

None

None

1.2V to 5V

None

20-pins,

2.54mm

(15

MHz)

1 MByte/s

2-pins

(115.2K)

All

J-Link BASE,

J-Link BASE Compact

2.0 HS

None

None

1.2V to 5V

None

20-pins,

2.54mm

(15

MHz)

1 MByte/s

2-pins

(115.2K)

Limited

J-Link EDU

(

discontinued

)

2.0 HS

None

None

1.2V to 5V

None

20-pins,

2.54mm

(15

MHz)

1 MByte/s

2-pins

(115.2K)

Limited

J-Link EDU Mini

2.0

FS

None

None

1.8V to 3.3V,

3.3V-only for

older models

None

9-pins,

1.27mm

(4

MHz

)

0.2

MByte

/s

None

Limited

(newer models have a case)

J-Link OB

(

on board

)

2.0 FS

None

None

Depends

None

Integrated

on dev board

(2 to 4

MHz)

0.1 to 0.2

MByte/s

Depends

Limited

- Note: Further models are J-Link LITE ARM, J-Link LITE CortexM, J-Link LITE RX, J-Link OEM.
- Note: Software options vary by model: J-Flash, J-Flash-SPI, Ozone, RDDI, RDI, Unlimited Flash Breakponts.
- Note: The EDU & EDU Mini models cannot be used for commercial software development, also doesn't come with J-Flash, J-Flash-SPI, RDDI, RDI options.
- Note: Adapters and isolators are available to convert the 20-pin 0.1"/2.54mm male shrouded (box) header to another target board connector.
- Note: The compact variants are functionally identical to their larger variants.
