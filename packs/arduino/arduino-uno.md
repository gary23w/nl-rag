---
title: "Arduino Uno"
source: https://en.wikipedia.org/wiki/Arduino_Uno
domain: arduino
license: CC-BY-SA-4.0
tags: arduino, arduino sketch, arduino uno, arduino ide, atmega
fetched: 2026-07-02
---

# Arduino Uno

The **Arduino Uno** is a series of open-source microcontroller board based on a diverse range of microcontrollers (MCU). It was initially developed and released by the Arduino company in 2010. The microcontroller board is equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards (shields) and other circuits. The board has 14 digital I/O pins (six capable of PWM output), 6 analog I/O pins, and is programmable with the Arduino IDE (Integrated Development Environment), via a type B USB cable. It can be powered by a USB cable or a barrel connector that accepts voltages between 7 and 20 volts, such as a rectangular 9-volt battery. It has the same microcontroller as the Arduino Nano board, and the same headers as the Leonardo board. The hardware reference design is distributed under a Creative Commons Attribution Share-Alike 2.5 license and is available on the Arduino website. Layout and production files for some versions of the hardware are also available.

The word "uno" means "one" in Italian and was chosen to mark a major redesign of the Arduino hardware and software. The Uno board was the successor of the Duemilanove release and was the 9th version in a series of USB-based Arduino boards. Version 1.0 of the Arduino IDE for the Arduino Uno board has now evolved to newer releases. The ATmega328 on the board comes preprogrammed with a bootloader that allows uploading new code to it without the use of an external hardware programmer.

While the Uno communicates using the original STK500 protocol, it differs from all preceding boards in that it does not use a FTDI USB-to-UART serial chip. Instead, it uses the Atmega16U2 (Atmega8U2 up to version R2) programmed as a USB-to-serial converter.

## History

The Arduino project started at the Interaction Design Institute Ivrea (IDII) in Ivrea, Italy. At that time, the students used a BASIC Stamp microcontroller, at a considerable price. In 2003, Hernando Barragán created the development platform *Wiring* as a Master's thesis project at IDII, under the supervision of Massimo Banzi and Casey Reas, who are known for work on the Processing language. The project goal was to create simple, low-cost tools for creating digital projects by non-engineers. The Wiring platform consisted of a printed circuit board (PCB) with an ATmega168 microcontroller, an IDE based on Processing, and library functions to easily program the microcontroller. In 2003, Massimo Banzi, with David Mellis, another IDII student, and David Cuartielles, added support for the cheaper ATmega8 microcontroller to Wiring. But instead of continuing the work on Wiring, they forked the project and renamed it *Arduino*. Early Arduino boards used the FTDI USB-to-UART serial chip and an ATmega168. The Uno differed from all preceding boards by featuring the ATmega328P microcontroller and an ATmega16U2 (Atmega8U2 up to version R2) programmed as a USB-to-serial converter.

In June 2023, Arduino released two new flavors of the Uno; R4 Minima and R4 Wifi. These mark a departure from previous boards as they use Renesas RA4M1 ARM Cortex M4 microcontroller, and the R4 Wifi a Espressif ESP32-S3-MINI co-processor. These versions are form factor, pin and power compatible with version R1 to R3, so should be largely be able to be drop in replacements.

In October 2025, Arduino released the Arduino UNO Q, a board with Linux support and WIFi, featuring a Qualcomm co-processor following their acquisition by Qualcomm. It also has a LED matrix and Bluetooth support.

## Technical specifications

### Uno R1 to R3

Microcontroller (MCU):

- IC: Microchip ATmega328P (8-bit AVR core)
- Clock Speed: 16 MHz (on Uno R1 to R3 boards), though IC supports 20 MHz maximum at 5 Volts
- Flash memory: 32 KB, of which 0.5 KB used by the bootloader
- SRAM: 2 KB
- EEPROM: 1 KB
- USART peripherals: 1 (Arduino software default configures USART as a 8N1 UART)
- SPI peripherals: 1
- I²C peripherals: 1
- Operating Voltage: 5 Volts (on Uno R1 to R3 boards), though IC supports 1.8 to 5.5 Volts (some 3rd-party Uno variations support 3.3V)

Board:

- Digital I/O Pins: 14
- PWM Pins: 6 (Pin # 3, 5, 6, 9, 10 and 11)
- Analog Input Pins: 6
- DC Current per I/O Pin: 20 mA
- DC Current for 3.3V Pin: 50 mA
- Size: 68.6 mm x 53.4 mm
- Weight: 25 g
- ICSP Header: Yes
- Power Sources:

- USB connector. USB bus specification has a voltage range of 4.75 to 5.25 volts. The official Uno boards have a USB-B connector, but 3rd party boards may have a miniUSB / microUSB / USB-C connector.
- 5.5mm/2.1mm barrel jack connector. Official Uno boards support 6 to 20 volts, though 7 to 12 volts is recommended. The maximum voltage for 3rd party Uno boards varies between board manufactures because various voltage regulators are used, each having a different maximum input rating. Power into this connector is routed through a series diode before connecting to VIN to protect against accidental reverse voltage situations.
- VIN pin on shield header. It has a similar voltage range of the barrel jack. Since this pin doesn't have reverse voltage protection, power can be injected or pulled from this pin. When supplying power into VIN pin, an external series diode is required in case barrel jack is used. When board is powered by barrel jack, power can be pulled out of this pin.

### Uno R4

Two Uno R4 boards are available: Uno R4 Minima and Uno R4 WiFi. The latter has a WiFi coprocessor and LED matrix, but the Minima doesn't.

Common features on both **Uno R4 Minima** and **Uno R4 WiFi** boards:

Microcontroller (MCU):

- IC: Renesas R7FA4M1AB (32-bit ARM Cortex-M4F core with single-precision FPU)
- Clock Speed: 48 MHz (on Uno R4 board)
- Flash memory: 256 KB + bootrom
- SRAM: 32 KB (16 KB ECC) (16 KB parity)
- EEPROM: 8 KB (data flash)
- USART peripherals: 4
- SPI peripherals: 2
- I²C peripherals: 2
- Operating Voltage: 5 Volts (on Uno R4 board), though IC supports 1.6 to 5.5 Volts

Board:

- USB-C connector.
- Barrel jack connector and VIN pin on shield header supports up to a maximum of 24 volts DC.

Additional features only available on the **Uno R4 Minima** board:

- SWD programming connector. This is a 10-pin 5x2 1.27mm header for connecting the microcontroller (R7FA4M1AB) to an external SWD (serial wire debug) programming / debugging device.

Additional features only available on the **Uno R4 WiFi** board:

- WiFi coprocessor - 240 MHz Espressif ESP32-S3-MINI (IEEE802.11 b/g/n WiFi and Bluetooth 5 LE) and a 6-pin 3x2 2.54mm header for external programming.
- 12x8 LED matrix - it is driven by 11 GPIO pins using a charlieplexing scheme.
- Qwiic I²C connector. This 4-pin 1.00mm JST SH connector provides external connection to a 3.3 volt I²C bus. Don't attach 5 volt I²C devices directly to this connector.
- RTC battery header pin (VRTC). This pin connects an external battery to the RTC (real-time clock) inside the microcontroller (R7FA4M1AB) to keep clock running when board is powered down. Connect this pin to positive side of 1.6 to 3.6 volt battery and negative side of battery to ground header pin (GND), such as a 3 volt lithium coin battery.
- Remote-Off header pin (OFF). This pin disables the 5 volt buck switching voltage regulator (SL854102) when powered by the barrel jack or VIN header pin. Connect this pin to ground header pin (GND) to disable this voltage regulator.

### Uno Q

The Arduino Uno Q has a dual processor setup with the Qualcomm Dragonwing serving as the MPU (microprocessor) and the ARM based STM32U585 as the MCU (microcontroller). Unlike the others, the UNO Q is capable of running Linux while also introducing Arduino App Lab.

## Headers

### General pin functions

- **LED**: There is a built-in LED driven by digital pin 13. When the pin is high value, the LED is on, when the pin is low, it is off.
- **VIN**: The input voltage to the Arduino/Genuino board when it is using an external power source (as opposed to 5 volts from the USB connection or other regulated power source). You can supply voltage through this pin, or, if supplying voltage via the power jack, access it through this pin.
- **5V**: This pin outputs a regulated 5V from the regulator on the board. The board can be supplied with power either from the DC power jack (7 - 20V), the USB connector (5V), or the VIN pin of the board (7-20V). Supplying voltage via the 5V or 3.3V pins bypasses the regulator, and can damage the board.
- **3V3**: A 3.3 volt supply generated by the on-board regulator. Maximum current draw is 50 mA.
- **GND**: Ground pins.
- **IOREF**: This pin on the Arduino/Genuino board provides the voltage reference with which the microcontroller operates. A properly configured shield can read the IOREF pin voltage and select the appropriate power source, or enable voltage translators on the outputs to work with the 5V or 3.3V.
- **Reset**: Typically used to add a reset button to shields that block the one on the board.

### Special pin functions

Each of the 14 digital pins and 6 analog pins on the Uno can be used as an input or output, under software control (using pinMode(), digitalWrite(), and digitalRead() functions). They operate at 5 volts. Each pin can provide or receive 20 mA as the recommended operating condition and has an internal pull-up resistor (disconnected by default) of 20-50K ohm. A maximum of 40mA must not be exceeded on any I/O pin to avoid permanent damage to the microcontroller. The Uno has 6 analog inputs, labeled A0 through A5; each provides 10 bits of resolution (i.e. 1024 different values). By default, they measure from ground to 5 volts, though it is possible to change the upper end of the range using the AREF pin and the analogReference() function.

In addition, some pins have specialized functions:

- **Serial** / UART: pins 0 (RX) and 1 (TX). Used to receive (RX) and transmit (TX) TTL serial data. These pins are connected to the corresponding pins of the ATmega8U2 USB-to-TTL serial chip.
- **External interrupts**: pins 2 and 3. These pins can be configured to trigger an interrupt on a low value, a rising or falling edge, or a change in value.
- **PWM** (pulse-width modulation): pins 3, 5, 6, 9, 10, and 11. Can provide 8-bit PWM output with the analogWrite() function.
- **SPI** (Serial Peripheral Interface): pins 10 (SS), 11 (MOSI), 12 (MISO), and 13 (SCK). These pins support SPI communication using the SPI library.
- **TWI** (two-wire interface) / I²C: pin SDA (A4) and pin SCL (A5). Supports TWI communication using the Wire library.
- **AREF** (analog reference): Reference voltage for the analog inputs.

## Communication

The Arduino/Genuino Uno has a number of facilities for communicating with a computer, another Arduino/Genuino board, or other microcontrollers. The ATmega328 provides UART TTL (5V) serial communication, which is available on digital pins 0 (RX) and 1 (TX). An ATmega16U2 on the board channels this serial communication over USB and appears as a virtual com port to software on the computer. The 16U2 firmware uses the standard USB COM drivers, and no external driver is needed. However, on Windows, a .inf file is required. Arduino Software (IDE) includes a serial monitor which allows simple textual data to be sent to and from the board. The RX and TX LEDs on the board will flash when data is being transmitted via the USB-to-serial chip and USB connection to the computer (but not for serial communication on pins 0 and 1). A SoftwareSerial library allows serial communication on any of the Uno's digital pins.

### Automatic (software) reset

Rather than requiring a physical press of the reset button before an upload, the Arduino/Genuino Uno board is designed in a way that allows it to be reset by the software running on a connected computer. One of the hardware flow control lines (DTR) of the ATmega8U2/16U2 is connected to the reset line of the ATmega328 via a 100 nanofarad capacitor. When this line is asserted (taken low), the reset line drops long enough to reset the chip.

This setup has other implications. When the Uno is connected to a computer running Mac OS X or Linux, it resets each time a connection is made to it from software (via USB). For the following half-second or so, the bootloader is running on the Uno. While it is programmed to ignore malformed data (i.e. anything besides an upload of new code), it will intercept the first few bytes of data sent to the board after a connection is opened.

## Arduino board comparison

The following table compares official Arduino boards, and has a similar layout as a table in the Arduino Nano article. The table is split with a dark bar into two high-level microcontroller groups: 8-bit AVR cores (upper group), and 32-bit ARM Cortex-M cores (lower group). Though 3rd-party boards have similar board names it doesn't automatically mean they are 100% identical to official Arduino boards. 3rd-party boards often have a different voltage regulator / different USB-to-UART chip / different color solder mask, and some have a different USB connector or additional features, too.

Board

Name

& Part#

Board

Size

Group

Board

Commun-

ication

MCU

Part#

& Pins

MCU

I/O

Voltage

MCU

Core

MCU

Clock

MCU

Flash

MCU

SRAM

MCU

EEPROM

MCU

USART

&

UART

MCU

SPI

MCU

I²C

MCU

Other Bus

Peripherals

MCU Timers

32/24/16/8

/

WD

/RT/

RC

MCU

ADC

&

DAC

MCU

Engines

Uno R3

,

A000066,

Uno R3 SMD

,

A000073

Uno

USB-B

ATmega328P

,

28 pin

DIP

,

32 pin

SMD

5V

(1.8-5.5V)

8bit

AVR

16

MHz*

32 KB

2 KB

1 KB

1, 0

1

1

None

0, 0, 1, 2,

WD

10bit,

None

None

Uno WiFi R2

,

ABX00021

Uno

USB-B

,

WiFi

,

Bluetooth

ATmega4809,

48 pin

5V

(1.8-5.5V)

8bit

AVR

16

MHz*

48 KB

6 KB

0.25 KB

4, 0

1

1

None

0, 0, 5, 0,

WD, RT

10bit,

None

None

Leonardo

,

A000057

Uno

USB-Micro-B

ATmega32U4,

44 pin

5V

(2.7-5.5V)

8bit

AVR

16

MHz

32 KB

2.5 KB

1 KB

1, 0

1

1

USB-FS

0, 0, 2, 1,

WD, 10bit

10bit,

None

None

Mega 2560 R3

,

A000067

Mega

USB-B

ATmega2560,

100 pin

5V

(4.5-5.5V)

8bit

AVR

16

MHz

256 KB

8 KB

4 KB

4, 0

1

1

None

0, 0, 4, 2,

WD

10bit,

None

None

Uno R4 Minima

,

ABX00080,

Uno R4 WiFi

,

ABX00087,

Uno

USB-C

,

WiFi

*

R7FA4M1AB,

64 pin

5V

(1.6-5.5V)

32bit ARM

Cortex-M4F

(

FPU

)

48

MHz

256 KB

+

bootrom

32 KB

(

ECC

)

(

parity

)

None

+ 8

KB

data

flash

4, 0

2

2

USB-FS

,

CAN-A/B

2, 0, 8, 0,

WD, RC,

24bit SysTick

14bit,

12bit

DMA

x4,

CRC

,

RNG

,

Crypto

,

Touch

,

LCD

Zero

,

ABX00003

Uno

USB-Micro-B

x2

ATSAMD21G18,

48 pin

3.3V

(1.62-3.63V)

32bit ARM

Cortex-M0+

48

MHz

256 KB

32 KB

None

6, 0

None

None

USB-FS

,

I²S

0, 4, 5, 0,

WD, RC,

24bit SysTick

12bit,

10bit

DMA

x12,

CRC32

,

Touch

Due

,

A000062

Mega

USB-Micro-B

x2

ATSAM3X8E,

144 pin

3.3V

(1.62-3.6V)

32bit ARM

Cortex-M3

84

MHz

512 KB

+

bootrom

96 KB

None

4, 1

1

2

USB-HS

,

CAN-A/B

x2,

I²S

,

SD

3, 0, 8, 0,

WD, RT, RC,

24bit SysTick

12bit,

12bit x2

DMA

x8,

RNG

GIGA R1 WiFi

,

ABX00063

Mega

USB-C

,

USB-A

,

WiFi

,

Bluetooth

STM32H747XI,

240 pin

3.3V

(1.62-3.6V)

32bit ARM

Cortex-M7F

Cortex-M4F

(dual core)

(

FPU

)

480

MHz

(M7F),

240

MHz

(M4F)

2048 KB

+

bootrom

1056 KB

(

ECC

)

None

4, 5

6

4

USB-HS

& FS,

CAN-A/B/FD

x2,

I²S

x4,

SD

x2,

S/PDIF

x4,

CEC

,

SWP

,

QSPI

2, 0, 18, 0,

WD, RC,

24bit SysTick

16bit x3,

12bit x2

DMA

x4,

CRC

,

RNG

,

Graphics

**Table notes**

- *Board Size Group* column - Simplified board dimension size grouping: Uno means similar size as Arduino Uno R3 and Duemilanove (predecessor) boards, Mega means similar size as the longer Arduino Mega 2560 R3 and Mega (predecessor) boards. This table has a similar layout as a table in the Arduino Nano article.
- *MCU Part# / Pins* column - MCU means microcontroller. All MCU information in this table was sourced from official datasheets in this column. The pin count is useful to determine the quantity of internal MCU features that are available. All MCU hardware features may not be available at the shield header pins because the MCU IC package has more pins than the shield header pins on the Arduino board (*).
- *MCU I/O Voltage* column - Microcontrollers on official Arduino boards are powered at a fixed voltage of either 3.3 or 5 volts, though some 3rd party boards have a voltage selection switch. The voltage rating of the microcontroller is stated inside parenthesis, though Arduino boards don't support this full range.
- *MCU Clock* column - MHz means 106 Hertz. The ATmega328P MPU and ATmega4809 MCU are rated for a maximum of 20 MHz, but the Uno R3 and Uno WiFi R2 boards both operate at 16 MHz. The following Arduino boards have a 32.768 kHz crystal too: Uno WiFi R2, Zero, Due, GIGA R1 WiFi. The Uno R4 Minima has SMD footprints for a 32.768 kHz crystal and two capacitors, but aren't installed.
- MCU memory columns - KB means 1024 bytes, MB means 10242 bytes. The R7FA4M1AB MCU (Uno R4 boards) contains data flash memory instead of EEPROM memory.
- *MCU SRAM* column - SRAM size doesn't include caches or peripheral buffers. ECC means SRAM has error correction code checking, Parity means SRAM has parity checking.
- *MCU USART/UART* column - USARTs are software configurable to be a: UART / SPI / other peripherals (varies across MCUs).
- *MCU Other Bus Peripherals* column - For USB bus, "FS" means Full Speed (12 Mbit/s max), "HS" means High Speed (480 Mbit/s max). For CAN bus, "A" means CAN 2.0A, "B" means CAN 2.0B, "FD" means CAN-FD. Some buses require additional external circuitry to operate.
- *MCU Timers* column - The numbers in this column are the total number of each timer bit width, for example, the ATmega328P has one 16-bit timer and two 8-bit timers. "WD" means Watchdog timer, "RT" means Real Time Counter/Timer, "RC" means Real Time Clock (sec/min/hr). The 24-bit SysTick timer(s) inside the ARM cores aren't included in the 24-bit total in this column. PWM features are not documented in this table.

### Gallery

- (Arduino Leonardo board with ATmega32U4 MCU)Arduino Leonardo board with ATmega32U4 MCU
- (Arduino Mega with ATmega2560 MCU)Arduino Mega with ATmega2560 MCU
- (Arduino Due board with ATSAM3X8E MCU)Arduino Due board with ATSAM3X8E MCU
- (Arduino GIGA R1 WiFi board with STM32H747XI MCU)Arduino GIGA R1 WiFi board with STM32H747XI MCU
