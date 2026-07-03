---
title: "ATmega328"
source: https://en.wikipedia.org/wiki/ATmega328
domain: dual-in-line-package
license: CC-BY-SA-4.0
tags: dual in-line package
fetched: 2026-07-03
---

# ATmega328

The **ATmega328** is a single-chip microcontroller created by Atmel in the megaAVR family (later Microchip Technology acquired Atmel in 2016). It has a modified Harvard architecture 8-bit RISC processor core.

## Specifications

The Atmel 8-bit AVR RISC-based microcontroller combines 32 KB ISP flash memory with read-while-write capabilities, 1 KB EEPROM, 2 KB SRAM, 23 general-purpose I/O lines, 32 general-purpose working registers, 3 flexible timer/counters with compare modes, internal and external interrupts, serial programmable USART, a byte-oriented 2-wire serial interface, SPI serial port, 6-channel 10-bit A/D converter (8 channels in TQFP and QFN/MLF packages), programmable watchdog timer with internal oscillator, and 5 software-selectable power-saving modes. The device operates between 1.8 and 5.5 volts. The device achieves throughput approaching 1 MIPS/MHz.

## Features

| Parameter | Value |
|---|---|
| CPU type | 8-bit AVR |
| Maximum CPU speed | 20 MHz |
| Performance | 20 MIPS at 20 MHz |
| Flash memory | 32 KB |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| Package pin count | 28 or 32 |
| Capacitive touch sensing channels | 16 |
| Maximum I/O pins | 23 |
| External interrupts | 3 |
| USB interface | No |

## Family

A common alternative to the ATmega328 is the "picoPower" ATmega328P. A comprehensive list of all other members of the megaAVR series can be found on the Atmel website.

- ATmega328
- ATmega328P and ATmega328P-AUTOMOTIVE
- ATmega328PB and ATmega328PB-AUTOMOTIVE (superset of ATmega328P) - has more UART, I2C, and SPI peripherals than ATmega328P

## Applications

ATmega328 is commonly used in many projects and autonomous systems where a simple, low-powered, low-cost micro-controller is needed.

Perhaps the most common use of this chip is on the popular Arduino development platform, namely the Arduino Uno, Arduino Pro Mini and Arduino Nano models.

## Programming

Reliability qualification shows that the projected data retention failure rate is much less than 1 PPM over 20 years at 85 °C or 100 years at 25 °C.

| Programming signal | Pin Name | I/O | Function |
|---|---|---|---|
| RDY/BSY | PD1 | O | High means the MCU is ready for a new command, otherwise busy. |
| OE | PD2 | I | Output enable (active low) |
| WR | PD3 | I | Write pulse (active low) |
| BS1 | PD4 | I | Byte select 1 ("0" = Low byte, "1" = High byte) |
| XA0 | PD5 | I | XTAL action bit 0 |
| XA1 | PD6 | I | XTAL action bit 1 |
| PAGEL | PD7 | I | Program memory and EEPROM data page load |
| BS2 | PC2 | I | Byte select 2 ("0" = low byte, "1" = 2nd high byte) |
| DATA | PC[1:0]:PB[5:0] | I/O | Bi-directional data bus (output when OE is low) |

Programming mode is entered when PAGEL (PD7), XA1 (PD6), XA0 (PD5), BS1 (PD4) is set to zero. RESET pin to 0 V and VCC to 0 V. VCC is set to 4.5–5.5 V. Wait 60 μs, and RESET is set to 11.5–12.5 V. Wait more than 310 μs. Set XA1:XA0:BS1:DATA = 100 1000 0000, pulse XTAL1 for at least 150 ns, pulse WR to zero. This starts the chip erase. Wait until RDY/BSY (PD1) goes high. XA1:XA0:BS1:DATA = 100 0001 0000, XTAL1 pulse, pulse WR to zero. This is the flash write command. And so on.

| Symbol | Pins | I/O | Description |
|---|---|---|---|
| MOSI | PB3 | I | Serial data in |
| MISO | PB4 | O | Serial Data out |
| SCK | PB5 | I | Serial Clock |

Serial data to the MCU is clocked on the rising edge and data from the MCU is clocked on the falling edge. Power is applied to VCC while RESET and SCK are set to zero. Wait for at least 20 ms and then the programming enable serial instruction 0xAC, 0x53, 0x00, 0x00 is sent to the MOSI pin. The second byte (0x53) will be echoed back by the MCU.
