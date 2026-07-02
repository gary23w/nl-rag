---
title: "ESP32"
source: https://en.wikipedia.org/wiki/ESP32
domain: esp32
license: Apache-2.0 (ESP-IDF docs) / CC-BY-SA-4.0
tags: esp32, esp-idf, espressif, esp8266
fetched: 2026-07-02
---

# ESP32

**ESP32** is a family of low-cost, energy-efficient microcontrollers that integrate both Wi-Fi and Bluetooth capabilities. These chips feature a variety of processing options, including the Tensilica Xtensa LX6 microprocessor available in both dual-core and single-core variants, the Xtensa LX7 dual-core processor, or a RISC-V microprocessor. In addition, the ESP32 incorporates components essential for wireless data communication such as built-in antenna switches, an RF balun, power amplifiers, low-noise receivers, filters, and power-management modules.

Typically, the ESP32 is embedded on device-specific printed circuit boards or offered as part of development kits that include a variety of GPIO pins and connectors, with configurations varying by model and manufacturer. The ESP32 was designed by Espressif Systems and is manufactured by TSMC using their 40 nm process. It is a successor to the ESP8266 microcontroller.

## Features

Since the release of the original ESP32, a number of variants have been introduced and announced. They form the ESP32 family of microcontrollers. These chips have different CPUs and capabilities, but all share the same SDK and are largely code-compatible. Additionally, the original ESP32 was revised (see ESP32 ECO V3, for example).

ESP32 Family

Feature

ESP32

ESP32-

S2

ESP32-

S3

ESP32-

C2

ESP32-

C3

ESP32-

C5

ESP32-

C6

ESP-

C61

ESP32-

H2

ESP32-

P4

CPU

Xtensa LX6

Xtensa LX7

Xtensa LX7

RV32IMAC

RV32IMC

RV32IMAC

RV32IMAC

RV32IMAC

RV32IMAC

RV32IMAFC

CPU Cores

Single, Dual

Single

Dual

Single

Dual

CPU Frequency

240 MHz

120 MHz

160 MHz

240 MHz

160 MHz

96 MHz

400 MHz

Coprocessor

FSM

FSM

RV32IMC

No

RV32IMC

No

RV32IMC

Coprocessor Speed

20 MHz

20 MHz

17.5 MHz

40 MHz

20 MHz

20 MHz

FPU

Single Precision

No

Single Precision

No

Single Precision

SRAM

520 KiB

320 KiB

512 KiB

272 KiB

400 KiB

384 KiB

512 KiB

320 KiB

256 KiB

768 KiB

ROM

448 KiB

128 KiB

384 KiB

128 KiB

384 KiB

256 KiB

128 KiB

512 KiB

RTC SRAM

8 KiB

16 KiB

8 KiB

16 KiB

8 KiB

32 KiB

PSRAM

4 MiB

8 MiB

No

8 MiB

No

8 MiB

No

16 MiB

SPI

Quad

Octal

Quad

Hex

UART

3

2

3

2

3

2

Wi-FI

802.11 b/g/n

802.11 b/g/n/ac/ax

802.11 b/g/n/ax

No

Ethernet MAC + RMII

Yes

SPI only

Yes

Bluetooth

4.2 + BR/EDR, LE

No

5 + LE

5.3 + LE

6 + LE

5.3 + LE

No

GPIO Pins

34

43

45

20

22

30

26

50

SAR ADCs

2 × 12-bit

2 × 13-bit

2 × 12-bit

1 × 12-bit

No

ADC Channels

18

20

6

7

4

5

DAC

2 × 8-bit DAC

No

USB

No

USB OTG

No

USB OTG

I²C Controllers

2

1

2

I²S Controllers

2

1

2

1

3

DMA

PDMA

GDMA

GDMA + UHCI

GDMA

PWM

LEDC, MCPWM

LEDC

LEDC, MCPWM

Temperature Sensor

Yes

No

Yes

No

Yes

Thread + Zigbee

No

Yes

No

Display Support

SPI

LCD, SPI

SPI

LCD, SPI, HMI

AI/Vector ISA

No

Yes

No

Yes

Storage

4 bit SD, SPI SD

SPI SD

4 bit SD, SPI SD, eMMC

SPI SD only

4 bit SD, SPI SD, eMMC

CAN Bus

CAN 2.0, SPI

SPI

CAN 2.0, SPI

Secure Boot

V1, V2

V2

Crypto Hardware

No

Yes

No

Yes

Yes

Other Features

I²S camera

hatI²S and PDM Mic

PDM Mic

No

Advanced audio

## QFN packaged chip and module

ESP32 is housed in quad-flat no-leads (QFN) packages of varying sizes with 49 pads. Specifically, 48 connection pads along the sides and one large thermal pad (connected to ground) on the bottom.

### Chips

The ESP32 system on a chip integrated circuit is packaged in both 6 mm × 6 mm and 5 mm × 5 mm sized QFN packages.

Series

Identifier

Processor

cores

Processor

speed (MHz)

Embedded flash

memory (

MiB

)

Embedded PSRAM

memory (

MiB

)

GPIOs

Package

size

Description

ESP32

ESP31B

2

240

0

0

34

6 mm × 6 mm

Pre-release

SoC

used for beta testing; no longer available.

ESP32-D0WDQ6

Initial production release chip of the ESP32 series.

Not Recommended for New Designs (NRND).

ESP32-D0WD

5 mm × 5 mm

Smaller physical package variation similar to ESP32-D0WDQ6.

Not Recommended for New Designs (NRND).

ESP32-D0WDQ6-V3

6 mm × 6 mm

Introduces some fixes to ESP32-D0WDQ6.

Not Recommended for New Designs (NRND).

ESP32-D2WD

160

2

5 mm × 5 mm

2 MiB (16 Mibit) embedded flash memory variation.

Removed.

Not Recommended for New Designs (NRND).

ESP32-S0WD

1

0

Single-core processor variation.

Not Recommended for New Designs (NRND).

ESP32-D0WD-V3

2

240

Introduces some fixes to ESP32-D0WD.

ESP32-D0WDR2-V3

2

ESP32-U4WDH

4

0

Single-core processor and 4 MiB (32 Mibit) embedded flash memory variation.

Also 1 CPU 160 MHz variant existed.

ESP32-S2

ESP32-S2

1

240

0

0

43

7 mm × 7 mm

With USB OTG.

ESP32-S2R2

2

ESP32-S2FH2

2

0

ESP32-S2FH4

4

ESP32-S2FN4R2

2

ESP32-S3

ESP32-S3

2

240

0

0

45

7 mm × 7 mm

With USB OTG. With 3.3V and 1.8V VDD_SPI voltage.

ESP32-S3R2

2

With USB OTG.

ESP32-S3R8

8

ESP32-S3R8V

With USB OTG. With 1.8V VDD_SPI voltage.

ESP32-S3FN8

8

0

With USB OTG.

ESP32-S3FH4R2

4

2

ESP32-C2

ESP8684H1

1

120

1

0

14

4 mm × 4 mm

With Bluetooth 5.

ESP8684H2

2

ESP8684H4

4

ESP32-C3

ESP32-C3

1

160

0

22

5 mm × 5 mm

With Bluetooth 5.

ESP32-C3FN4

4

Not Recommended for New Designs (NRND).

ESP32-C3FH4

With Bluetooth 5.

ESP32-C3FH4AZ

16

With Bluetooth 5. SPI0/SPI1 pins for flash connection are not bonded.

ESP-Shelly-C38F

8

11

With Bluetooth 5.

only for the manufacturer Shelly

ESP8686H4

4

15

4 mm × 4 mm

Not released.

ESP8685H2

2

With Bluetooth 5.

ESP8685H4

4

ESP32-C5

ESP32-C5HF4

1H, 1L

240

4

Off-pkg

29

6 mm × 6 mm

Ultra-low-power SoC w. Wi-Fi6 (802.11ax), Zigbee & Thread (802.15.4).

ESP32-C5HR8

Off-pkg

8

ESP32-C6

ESP32-C6

1

160

0

0

30

5 mm × 5 mm

With Wi-Fi 6 and Bluetooth 5.

ESP32-C6FH4

4

22

ESP32-H2

ESP32-H2FH2

1

96

2

0

19

4 mm × 4 mm

With Bluetooth 5 and Bluetooth Mesh.

ESP32-H2FH4

4

ESP32-P4

ESP32-P4NRW16

2H, 1L

360

Off-pkg up to 64MB

16

55

10 mm × 10 mm

Powerful image and voice processing

ESP32-P4NRW32

32

In 2020, chips ESP32-D0WDQ6 and ESP32-D0WD also got a V3 version (ESP32 ECO V3), which fixes some of the bugs and introduces improvements over the previous versions.

### Modules

The ESP32 PICO system in package modules combine an ESP32 silicon chip, crystal oscillator, flash memory chip, filter capacitors, and RF matching links into a single 7 mm × 7 mm sized QFN package.

The first released PICO was the ESP32-PICO-D4 with 2 CPUs at 240 MHz, 4MiB internal flash, a 40 MHz oscillator and 34 GPIOs.

Later, in 2020, the ESP32-PICO-V3 and ESP32-PICO-V3-02 modules were introduced both based on the ESP32 ECO V3 wafer.

In 2022 the ESP32-S3-PICO-1 module was introduced with USB OTG and internal PSRAM.

| Identifier | Processor cores | Processor speed (MHz) | Embedded flash memory (MiB) | Embedded PSRAM memory (MiB) | GPIOs | Package size | Description |
|---|---|---|---|---|---|---|---|
| ESP32-PICO-D4 | 2 | 240 | 4 | 0 | 34 | 7 mm × 7 mm | Includes ESP32 chip, crystal oscillator, flash memory, filter capacitors, and RF matching links. |
| ESP32-PICO-V3 | 31 | Based on ESP32 with ECO V3 wafer. |   |   |   |   |   |
| ESP32-PICO-V3-02 | 8 | 2 | 29 |   |   |   |   |
| ESP32-S3-PICO-1-N8R2 | 39 | Includes USB OTG. |   |   |   |   |   |
| ESP32-S3-PICO-1-N8R8 | 8 | 8 |   |   |   |   |   |

## Printed circuit boards

### Surface-mount module boards

ESP32 based surface-mount printed circuit board modules directly contain the ESP32 SoC and are designed to be easily integrated onto other circuit boards. Meandered inverted-F antenna designs are used for the PCB trace antennas on the modules listed below. In addition to flash memory, some modules include pseudostatic RAM (pSRAM).

| Vendor | Name | Antenna | Flash memory (MiB) | PSRAM (MiB) | Description |
|---|---|---|---|---|---|
| Espressif | ESP-WROOM-03 | PCB trace | 4 | 0 | Discontinued. Limited distribution, pre-production module created by Espressif for beta testing purposes; this module used the ESP31B, the beta testing chip for the ESP32 series. FCC Part 15.247 tested (FCC ID: 2AC7Z-ESP32). |
| ESP32-WROOM-32 | First publicly available ESP32 module board created by Espressif. FCC Part 15.247 tested (FCC ID: 2AC7Z-ESPWROOM32). Based on ESP32-D0WDQ6 chip. Originally named "ESP-WROOM-32". |   |   |   |   |
| ESP32-WROOM-32E | 4,8,16 | Same as ESP32-WROOM-32 but with the Eco V3 processor revisions |   |   |   |
| ESP32-WROOM-32D | 4 | Revision of the ESP-WROOM-32 module which uses an ESP32-D0WD chip instead of an ESP32-D0WDQ6 chip. Originally named "ESP-WROOM-32D". |   |   |   |
| ESP32-SOLO-1 | Similar to the ESP32-WROOM-32D module, but uses the single-core ESP32-S0WD chip instead of the dual-core ESP32-D0WD. |   |   |   |   |
| ESP32-WROOM-32U | U.FL socket | Alternative to the ESP-WROOM-32D module which has a U.FL connector for external antenna in lieu of a PCB trace antenna. |   |   |   |
| ESP32-WROVER | PCB trace | 4 | ESP32 module board with 4 MiB pSRAM created by Espressif. FCC part 15.247 tested (FCC ID 2AC7Z-ESP32WROVER). Uses 40 MHz crystal oscillator. Does not include U.FL connector. Based on ESP32-D0WDQ6 chip. Since June 2018, new modules have been upgraded to 8 MiB pSRAM. |   |   |
| ESP32-WROVER-I | U.FL socket, PCB trace | Variation of ESP32-WROVER module configured to use an on-board U.FL compatible connector. PCB trace antenna not connected by default. |   |   |   |
| ESP32-WROVER-B | PCB trace | 8 | Revision of ESP32-WROVER module with 8 MiB pSRAM (instead of 4 MiB pSRAM) operating at 3.3V (instead of 1.8V in previous versions) and ESP32-D0WD (instead of ESP32-D0WDQ6). FCC part 15.247 tested (FCC ID 2AC7Z-ESP32WROVERB). Does not include U.FL connector. (Custom order option for flash capacity of 8 MiB or 16 MiB also available.) |   |   |
| ESP32-WROVER-IB | U.FL socket, PCB trace | Variation of ESP32-WROVER-B module configured to use an on-board U.FL compatible connector. PCB trace antenna not connected by default. |   |   |   |
| ESP32-WROVER-E | PCB trace | 4,8,16 | 2,8 | Revision of ESP32-WROVER module with 2 or 8 MiB pSRAM (instead of 4 MiB pSRAM) operating at 3.3V (instead of 1.8V in previous versions) and ESP32-D0WD-V3, or in 2MB pSRAM models, ESP32-D0WDR2-V3. FCC part 15.247 tested (FCC ID 2AC7Z-ESP32WROVERE). Does not include U.FL connector. (Custom order option for flash capacity of 2 MiB, 8 MiB, or 16 MiB also available.) |   |
| ESP32-WROVER-IE | U.FL socket, PCB trace | Variation of ESP32-WROVER-E module configured to use an on-board U.FL compatible connector. PCB trace antenna not connected by default. |   |   |   |
| ESP32-PICO-V3-ZERO | PCB trace | 4 | 0 | Based on ESP32-PICO-V3 SiP. It is designed as a module for Alexa Connect Kit (ACK) and connecting with Amazon Alexa. |   |
| Ai-Thinker | ESP32-S | PCB trace | 4 | 0 | Ai-Thinker's equivalent to Espressif's ESP-WROOM-32 module. (Same form factor and general specifications.) Previously branded as "ESP-32S" with the hyphen before "32S", the initial release of the ESP-32S module replaced the previously announced, but never released, ESP3212 module. |
| ESP32-A1S | U.FL socket, PCB trace | 8 | 4 | Contains an extra AC101 audio codec IC whose IO-pins (line, mic, etc.) are led to the board pins. Comes separately or soldered onto a corresponding audio development board ("ESP32-Audio-Kit"). |   |
| AnalogLamb | ESP-32S-ALB | PCB trace | 4 | 0 | Clone of the ESP-32S module (ESP-WROOM-32 compatible footprint). Seen with a green solder mask coating. |
| ALB-WROOM | 16 | Variation of ESP-32S-ALB with 16 MiB of flash memory. |   |   |   |
| ALB32-WROVER | 4 | 4 | ESP32 module board with 4 MiB pSRAM with the same footprint as the ESP-WROOM-32 module. |   |   |
| DFRobot | ESP-WROOM-32 | PCB trace | 4 | 0 | Module board similar to Espressif Systems's ESP-WROOM-32, but is not FCC certified, and uses 26 MHz or 32 kHz crystal oscillator. |
| eBox & Widora | ESP32-Bit | Ceramic, U.FL socket | 4 | 0 | Module has a ceramic antenna and an U.FL antenna connector. This module has a different footprint than the ESP-WROOM-32/ESP-32S modules. |
| Goouuu Tech | ESP-32F | PCB trace | 4 | 0 | Module board similar to Espressif Systems's ESP-WROOM-32. FCC certified (ID 2AM77-ESP-32F). |
| IntoRobot | W32 | PCB trace | 4 | 0 | Module similar in appearance to Espressif's ESP-WROOM-32, but footprint pinout differs. |
| W33 | Ceramic, U.FL socket | Differs from IntoRobot W32 module in its antenna configuration. |   |   |   |
| ITEAD | PSH-C32 | PCB trace | 1 | 0 | Module has unusually small flash memory on board. Also, footprint is unique and differs from all other ESP32 modules. |
| Pycom | W01 | (Not included.) | 8 | 4 | OEM module version of the WiPy 2.0. Supports Wi-Fi and Bluetooth. FCC ID 2AJMTWIPY01R. |
| L01 | OEM module version of the LoPy. Supports Wi-Fi, Bluetooth, and LoRa. FCC ID 2AJMTLOPY01R. |   |   |   |   |
| L04 | OEM module version of the LoPy4. Supports Wi-Fi, Bluetooth, LoRa, and Sigfox. |   |   |   |   |
| S01 | Discontinued. OEM module version of the SiPy. Supports Wi-Fi, Bluetooth, and Sigfox (14 dBm and 22 dBm). |   |   |   |   |
| G01 | OEM module version of the GPy. Supports Cellular LTE-CAT M1/NB1, Wi-Fi and Bluetooth. |   |   |   |   |
| u-blox | NINA-W131 | (Not included.) | 2 | 0 | Belongs to the u-blox NINA-W13 series of Wi-Fi modules. |
| NINA-W132 | PIFA | Belongs to the u-blox NINA-W13 series of Wi-Fi modules. On board planar inverted-F antenna (PIFA) is shaped (cut & bent) metal, not a PCB trace. |   |   |   |

### Development and other boards

Development and break-out boards extend wiring and may add functionality, often building upon ESP32 module boards and making them easier to use for development purposes, especially with breadboards.

| Vendor | Name | Surface-mount module used | Description |
|---|---|---|---|
| Espressif | ESP_Module_Testboard | ESP-WROOM-03 | Break-out board included with ESP-WROOM-03 beta modules. |
| ESP32_Demo Board_V2 | ESP-WROOM-32 | Development & demonstration board created by Espressif. |   |
| ESP32-DevKitC | ESP32-WROOM-32, v4 comes with ESP32-WROOM-DA(Dual Antenna), ESP32-WROVER or ESP32-Solo (single-core variant) | Compact development board created by Espressif. Silkscreen labeling on PCB reads "Core Board". |   |
| ESP-WROVER-KIT | ESP-WROOM-32 or ESP32-WROVER | Large development board created by Espressif. Previously named ESP32-DevKitJ. |   |
| ESP32-PICO-KIT | ESP32-PICO-D4 | Small development board with Micro-USB and two header rows of 17 pins. FCC ID 2AC7Z-ESP32PICOKIT. |   |
| Adafruit | HUZZAH32 | ESP-WROOM-32 | Also referred to as the "ESP32 Feather Board", the HUZZAH32 is a compact development board/module that is compatible with the Adafruit Feather family of products. |
| Ai-Thinker | NodeMCU-32S | ESP-32S | NodeMCU-like development board. |
| ESP32-CAM | ESP32-S | Compact (27 mm × 40.5 mm) board with ribbon cable Camera Serial Interface with support for 1600 × 1200 pixel OV2640 or 640 × 480 OV7670 camera. Has 9 usable IO pins and microSD card slot. |   |
| AnalogLamb | ESP32 Development Board | ESP-32S-ALB or ALB-WROOM | Development board similar to Espressif's ESP32-DevKitC with on board a CP2102 USB/serial bridge. 4 MiB variation uses ESP-32S-ALB; 16 MiB variation uses ALB-WROOM module. |
| Maple ESP32 | ESP-32S-ALB | Development board with Arduino-style connections and CP2104 USB/serial interface. |   |
| April Brother | ESPea32 | † | Development board with perfboard area that may be optionally cut-off. |
| ArduCAM | ESP32 UNO | ESP-32S | Arduino Uno-like development board based on ESP32 IoT UNO framework with support for SPI ArduCAM, battery pins and uSD card slot. |
| Arduino | Arduino Nano ESP32 | U-Blox NORA-W106-10B (based on ESP32-S3 IC) | Deprecated. Arduino Nano footprint |
| Banana pi | BPI:bit | ESP-32S | a development for Webduino and Arduino |
| BPI-UNO32 | ESP32-S | a development board for Arduino |   |
| DoIT | ESPduino32 | ESP-WROOM-32 | Full-featured Arduino Uno-like development board compatible with Arduino Shields. It also adds additional SPI & IO pins. The board is a clone of WeMos D1 R32 with a USB Type B socket. |
| ESP32 DEVKIT V1 | ESP-WROOM-32 | The ESP32 DevKit V1 is probably the most popular among hobbyists and educators for its ease of use and versatility in various electronic projects. The pinout is one of the most copied. |   |
| DPTechnics | Walter | ESP32-S3-WROOM-1 | The Walter module combines cellular IoT (LTE-M and NB-IoT) and GNSS with the ESP32-S3 with 16MiB flash and 2MiB PSRAM. The module is suited for development as well as for production because of the CE, FCC, UKCA, RCM and IC certifications. |
| EzSBC | ESP32-01 Breakout and Development Board | ESP-WROOM-32 | Full-featured development board with two tri-color LEDs and fits on a breadboard. |
| Gravitech & MakerAsia | Nano32 | † | Development board that directly incorporates the ESP32 chip. |
| HydraBus | HydraESP32 | ESP-WROOM-32 or ESP-32S | HydraESP32 HydraBus v1.1 Rev1 shield/breakout board for ESP-WROOM-32 or ESP-32S. This shield can be used with or without a HydraBus board. |
| Noduino | Quantum | † | Arduino-style development board that directly incorporates the ESP32 chip. |
| Olimex | ESP32-Gateway | ESP32-WROOM32 | Wi-Fi/Bluetooth/Ethernet |
| ESP32-DevKit-LiPo | ESP32-WROOM-32 | pin compatible with ESP32-CoreBoard, but adds Lipo charger and ability to work on LiPo. |   |
| ESP32-POE-ISO | ESP32-WROOM-32/UE | Wi-Fi/Bluetooth/Ethernet development board with Power over Ethernet and 2W of isolated DC power |   |
| ESP32-POE | ESP32-WROOM-32 | Wi-Fi/Bluetooth/Ethernet development board with Power over Ethernet |   |
| ESP32-PRO | † | Wi-Fi/Bluetooth and PIC32MX270F256DT microcontroller and 32 Mb SPI flash and 32 Mb PSRAM. ESP32-PRO-C includes external crypto engine with ATECC508A |   |
| ESP32-EVB | ESP32-WROOM32 | Wi-Fi/Bluetooth/Ethernet development board with MicroSD, CAN, IR, LiPo, and two relays. |   |
| ESP32-ADF | ESP32-WROVER-B | audio development framework board with stereo microphones, speakers, audio output jack. |   |
| Pycom | WiPy | † | MicroPython programmable Wi-Fi & Bluetooth IoT development platform with a 1 km Wi-Fi range. WiPy versions 2.0 and 3.0 use ESP32. |
| LoPy | † | Triple network Pycom board featuring LoRa, Wi-Fi (1 km range), and BLE. |   |
| LoPy4 | ? | Quadruple network Pycom board featuring LoRa, Sigfox, Wi-Fi (1 km range), and BLE. |   |
| SiPy | † | Triple network Pycom board featuring Sigfox, Wi-Fi (1 km range), and BLE. |   |
| GPy | † | Triple network Pycom board featuring LTE-M, Wi-Fi (1 km range), and BLE. |   |
| FiPy | † | Quintuple network Pycom board featuring LTE-M, LoRa, Sigfox, Wi-Fi (1 km range), and BLE. |   |
| SparkFun | ESP32 Thing | † | Compact development board with FTDI FT231x USB/serial interface and LiPo charger built-in. |
| SunDUINO | ESP32 MiniBoard | ESP-WROOM-32 | Breakout compatible with the Espressif ESP32-DevKitC. Lacks on-board USB-UART. |
| ESP32 MiniBoard v2 | ESP32-Wrover-B/IB | Breakout board with Silabs CP2102, battery charger. Compatible with Espressif DEVkit. |   |
| ESP32 SunDUINO | ESP-WROOM-32 or ESP-32S | Arduino-style development board. Lacks on-board USB-UART. |   |
| SwitchDoc Labs | BC24 | ESP-WROOM-32 | ESP32 Breakout with 24 SK6812RGBW LEDs with Grove Connectors for easy prototyping. Comes with USB-UART and Feather compatible pinout. |
| Watterott | ESP-WROOM32-Breakout | ESP-WROOM-32 | Breakout which is compatible with the Espressif ESP32-DevKitC. |
| WEMOS | LOLIN32 [Retired] | ESP-WROOM-32 |   |
| LOLIN32 Lite [Retired] | † | ESP32-D0WDQ6 |   |
| LOLIN32 Pro [Retired] | ESP32-WROVER | MicroSD card slot (supports SD and SPI mode) |   |
| LOLIN D32 | ESP-WROOM-32 |   |   |
| LOLIN D32 Pro | ESP32-WROVER | I2C port, TFT port and Micro SD Card slot (support SPI mode) |   |
| Widora | Air | † | Compact ESP32 development board. |
| MagicBit | Magic Bit Core | ESP-WROOM-32 | Compact ESP32 development board with displays and several sensors on board to make learning embedded development convenient. |

† ESP32 SoC incorporated directly onto development board; no module board used.

## Programming

Programming languages, frameworks, platforms, and environments used for ESP32 programming:

- ESP-IDF – Espressif's official IoT Development Framework for the ESP32, ESP32-S, ESP32-C and ESP32-H series of SoCs.
- Arduino-ESP32 – Arduino core for the ESP32, ESP32-S2, ESP32-S3 and ESP32-C3.
- ESP32forth – FORTH implementation for ESP32
- Espruino – JavaScript SDK and firmware closely emulating Node.js
- MicroPython (and CircuitPython) – lean implementation of Python 3 for microcontrollers
- Mongoose OS – an operating system for connected products on microcontrollers; programmable with JavaScript or C. A recommended platform by Espressif Systems, AWS IoT, and Google Cloud IoT.
- mruby and picoruby for the ESP32
- Nim for the ESP32
- NodeMCU – Lua-based firmware
- Rust
- Swift
- Visual Studio Code with the officially supported Espressif Integrated Development Framework (ESP-IDF) Extension
- Zerynth – Python for IoT and microcontrollers, including the ESP32
- Matlab Simulink
- Zig for the ESP32

## Reception and use

Commercial, industrial and academic uses of ESP32:

### Use in commercial devices

- Alibaba Group's IoT LED wristband, used by participants at the group's 2017 annual gathering. Each wristband operated as a "pixel", receiving commands for coordinated LED light control, allowing formation of a "live and wireless" screen.
- DingTalk's M1, a biometric attendance-tracking system.
- Pium, a home fragrance and aromatherapy device.
- HardKernel's Odroid Go, an ESP32 based handheld gaming device kit made to commemorate Odroid's 10th anniversary.
- Playdate, a handheld video game console jointly developed by Panic Inc. and Teenage Engineering.
- Octopus Energy Mini, an ESP32-C6 based real-time energy monitor.
- Mysa smart thermostats, based on ESP32-WROOM.
- Low-end UniFi switches from Ubiquiti, based on ESP32-D0WD-V3.
- Xteink X4, a compact e-ink reader with support for community firmware.

### Use in industrial devices

- TECHBASE's Moduino X series X1 and X2 modules are ESP32-WROVER / ESP32-WROVER-B based computers for industrial automation and monitoring, supporting digital inputs/outputs, analog inputs, and various computer networking interfaces.
- NORVI IIOT Industrial Devices with ESP32-WROVER / ESP32-WROVER-B SOC for industrial automation and monitoring with digital inputs, analog inputs, relay outputs and multiple communications interfaces. Supports LoRa and Nb-IoT as expansion modules.

### Academic uses

- ESP32 devices are utilized in educational settings and academic research projects. Additionally, ESP32 is used in DIY projects such as building low-cost drones. The DJI Robomaster TT, an educational variant of the Ryze Tello drone, is equipped with an ESP32.

## Undocumented HCI commands in ESP32

In March 2025, researchers from Tarlogic Security identified undocumented Host Controller Interface (HCI) commands in the ESP32 Bluetooth firmware, prompting discussions about their functionality and potential implications. This discovery was presented on March 6, 2025, at the RootedCON conference by the Tarlogic Security team.

The identified commands, such as *Write Memory* (0xFC02), are vendor-specific HCI commands used primarily for debugging and testing purposes. These types of commands are common in Bluetooth controller implementations to assist with development and troubleshooting. They are not part of the standard HCI command set and are typically used in controlled environments. While initially described as a "backdoor," further clarifications labeled them as "undocumented debugging features." These commands are not accessible remotely via standard Bluetooth connections but could be interacted with if an entity has physical access to the device or operates in an HCI-UART configuration.

Espressif Systems provided clarification regarding these commands, stating that they are intended for debugging and do not pose a security risk under normal operating conditions. The company emphasized that these commands cannot be triggered remotely and are not used in standard Bluetooth operations. These commands are present only in ESP32 chips and are not included in the ESP32-C, ESP32-S, and ESP32-H series. To address concerns raised within the security community, Espressif announced that future versions of the ESP-IDF would include updates to restrict access to these debugging commands and improve documentation for vendor-specific HCI commands. These actions aim to provide additional transparency and ensure developers are well-informed about available functionalities.
