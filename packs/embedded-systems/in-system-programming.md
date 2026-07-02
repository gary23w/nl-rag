---
title: "In-system programming"
source: https://en.wikipedia.org/wiki/In-system_programming
domain: embedded-systems
license: CC-BY-SA-4.0
tags: embedded system, microcontroller, firmware, bare metal, bootloader, mcu
fetched: 2026-07-02
---

# In-system programming

**In-system programming** (ISP), or also called **in-circuit serial programming** (ICSP), is the ability of a programmable logic device, microcontroller, chipset, or other embedded device to be programmed while installed in a complete system, rather than requiring the chip to be programmed before installing. It also allows firmware updates to be delivered to the on-chip memory of microcontrollers and related processors without requiring specialist programming circuitry on the circuit board, and simplifies design work.

## Overview

There is no standard for in-system programming protocols for programming microcontroller devices. Almost all manufacturers of microcontrollers support ISP, but all have implemented their own protocols, which often differ even for various devices from the same manufacturer. Up to 4 pins may be required for implementing a JTAG standard interface. In general, modern protocols try to keep the number of pins used low, typically to 2 pins. Some ISP interfaces manage to achieve the same with just a single pin. Newer ATtiny microcontrollers with UPDI can even reuse that programming pin also as a general-purpose input/output.

The primary advantage of in-system programming is that it allows manufacturers of electronic devices to integrate programming and testing into a single production phase, and save money, rather than requiring a separate programming stage prior to assembling the system. This may allow manufacturers to program the chips in their own system's production line instead of buying pre-programmed chips from a manufacturer or distributor, making it feasible to apply code or design changes in the middle of a production run. The other advantage is that production can always use the latest firmware, and new features as well as bug fixes can be implemented and put into production without the delay occurring when using pre-programmed microcontrollers.

Microcontrollers are typically soldered directly to a printed circuit board and usually do not have the circuitry or space for a large external programming cable to another computer.

Typically, chips supporting ISP have internal circuitry to generate any necessary programming voltage from the system's normal supply voltage, and communicate with the programmer via a serial protocol. Most programmable logic devices use a variant of the JTAG protocol for ISP, in order to facilitate easier integration with automated testing procedures. Other devices usually use proprietary protocols or protocols defined by older standards. In systems complex enough to require moderately large glue logic, designers may implement a JTAG-controlled programming subsystem for non-JTAG devices such as flash memory and microcontrollers, allowing the entire programming and test procedure to be accomplished under the control of a single protocol.

## History

Starting from the early 1990s, an important technological evolution in the architecture of the microcontrollers was witnessed. At first, they were realized in two possible solutions: with one-time programmable (OTP) or with EPROM memories. For EPROM, a memory-erasing process requires the chip to be exposed to ultraviolet light through a specific window above the package. In 1993 Microchip Technology introduced the first microcontroller with EEPROM memory: the PIC16C84. EEPROM memories can be electrically erased. This feature allowed to lower the realization costs by removing the erasing window above the package and initiate in-system programming technology. With ISP flashing process can be performed directly on the board at the end of the production process. This evolution gave the possibility to unify the programming and functional test phase and in production environments and to start the preliminary production of the boards even if the firmware development has not yet been completed. This way it was possible to correct bugs or to make changes at a later time. In the same year, Atmel developed the first microcontroller with flash memory, easier and faster to program and with much longer life cycle compared to EEPROM memories.

Microcontrollers that support ISP are usually provided with pins used by the serial communication peripheral to interface with the programmer, a flash/EEPROM memory and the circuitry used to supply the voltage necessary to program the microcontroller. The communication peripheral is in turn connected to a programming peripheral which provides commands to operate on the flash or EEPROM memory.

When designing electronic boards for ISP programming, it’s necessary to take into account some guidelines to have a programming phase as reliable as possible. Some microcontrollers with a low number of pins share the programming lines with the I/O lines. This can be a problem if the necessary precautions are not taken into account in the design of the board; the device can suffer the damage of the I/O components during the programming. Moreover, it’s important to connect the ISP lines to high impedance circuitry both to avoid a damage of the components by the programmer and because the microcontroller often cannot supply enough current to pilot the line. Many microcontrollers need a dedicated reset line to enter in the programming mode. It is necessary to pay attention to current supplied for line driving and to check for presence of watchdogs connected to the reset line that can generate an unwanted reset and, so, to lead a programming failure. Moreover, some microcontrollers need a higher voltage to enter in Programming Mode and, hence, it’s necessary to check that this value it’s not attenuated and that this voltage is not forwarded to others components on the board.

## Industrial application

In-system programming takes place during the final stage of production of a product. It can be performed in two different ways based on the production volumes:

In the first method, a connector is manually connected to the programmer. This solution expects the human participation to the programming process that has to connect the programmer to the electronic board with the cable. Hence, this solution is meant for low production volumes.

The second method uses test points on the board. These are specific areas placed on the printed board, or PCB, that are electrically connected to some of the electronic components on the board. Test points are used to perform functional tests for components mounted on board and, since they are connected directly to some microcontroller pins, they are very effective for ISP. For medium and high production volumes using test points is the best solution since it allows to integrate the programming phase in an assembly line.

In production lines, boards are placed on a bed of nails called a fixture. The latter are integrated, based on the production volumes, in semiautomatic or automatic test systems called automatic test equipment (ATE). Fixtures are specifically designed for each board - or at most for few models similar to the board they were designed for – therefore these are interchangeable in the system environment where they are integrated. The test system, once the board and the fixture are placed in position, has a mechanism to put in contact the needles of the fixture with the test points on the board to test. The system it’s connected to, or has directly integrated inside, an ISP programmer. This one has to program the device or devices mounted on the board: for example, a microcontroller and/or a serial memory.

## Microchip ICSP

For most Microchip microcontrollers, ICSP programming is performed using two pins, clock (PGC) and data (PGD), while a high voltage (12 V) is present on the Vpp/MCLR pin. Low voltage programming (5 V or 3.3 V) dispenses with the high voltage, but reserves exclusive use of an I/O pin. However, for newer microcontrollers, specifically PIC18F6XJXX/8XJXX microcontrollers families from Microchip Technology, entering into ICSP modes is a bit different. Entering ICSP Program/Verify mode requires the following three steps:

1. Voltage is briefly applied to the MCLR (master clear) pin.
2. A 32-bit key sequence is presented on PGD.
3. Voltage is reapplied to MCLR.

A separate piece of hardware, called a programmer is required to connect to an I/O port of a PC on one side and to the PIC on the other side. A list of the features for each major programming type are:

1. **Parallel port** - large bulky cable, most computers have only one port and it may be inconvenient to swap the programming cable with an attached printer. Most laptops newer than 2010 do not support this port. Parallel port programming is very fast.
2. **Serial port** (COM port) - At one time the most popular method. Serial ports usually lack adequate circuit programming supply voltage. Most computers and laptops newer than 2010 lack support for this port.
3. **Socket** (in or out of circuit) - the CPU must be either removed from circuit board, or a clamp must be attached to the chip-making access an issue.
4. **USB cable** - Small and light weight, has support for voltage source and most computers have extra ports available. The distance between the circuit to be programmed and the computer is limited by the length of USB cable - it must usually be less than 180 cm. This can make programming devices deep in machinery or cabinets a problem.

ICSP programmers have many advantages, with size, computer port availability, and power source being major features. Due to variations in the interconnect scheme and the target circuit surrounding a micro-controller, there is no programmer that works with ***all*** possible target circuits or interconnects. Microchip Technology provides a detailed ICSP programming guide Many sites provide programming and circuit examples.

PICs are programmed using five signals (a sixth pin 'aux' is provided but not used). The data is transferred using a two-wire synchronous serial scheme, three more wires provide programming and chip power. The clock signal is always controlled by the programmer.

### Signals and pinout

- **Vpp** - Programming mode voltage. This must be connected to the MCLR pin, or the Vpp pin of the optional ICSP port available on some large-pin-count PICs. To put the PIC into programming mode, this line must be in a specified range that varies from PIC to PIC. For 5 V PICs, this is always some amount above Vdd, and can be as high as 13.5 V. The 3.3 V only PICs like the 18FJ, 24H, and 33F series use a special signature to enter programming mode and Vpp is a digital signal that is either at ground or Vdd. There is no one Vpp voltage that is within the valid Vpp range of all PICs. In fact, the minimum required Vpp level for some PICs can damage other PICs.
- **Vdd** - This is the positive power input to the PIC. Some programmers require this to be provided by the circuit (circuit must be at least partially powered up), some programmers expect to drive this line themselves and require the circuit to be off, while others can be configured either way (like the Microchip ICD2). The Embed Inc programmers expect to drive the Vdd line themselves and require the target circuit to be off during programming.
- **Vss** - Negative power input to the PIC and the zero volts reference for the remaining signals. Voltages of the other signals are implicitly with respect to Vss.
- **ICSPCLK** - Clock line of the serial data interface. This line swings from GND to Vdd and is always driven by the programmer. Data is transferred on the falling edge.
- **ICSPDAT** - Serial data line. The serial interface is bi-directional, so this line can be driven by either the programmer or the PIC depending on the current operation. In either case this line swings from GND to Vdd. A bit is transferred on the falling edge of PGC.
- **AUX/PGM** - Newer PIC controllers use this pin to enable low voltage programming (LVP). By holding PGM high, the micro-controller will enter LVP mode. PIC micro-controllers are shipped with LVP enabled - so if you use a brand new chip you can use it in LVP mode. The only way to change the mode is by using a high voltage programmer. If you program the micro controller with no connection to this pin, the mode is left unchanged.

### RJ11 pinout

Microchip supports an industry standard for using RJ11 sockets with an ICSP programmer. The illustration represents information provided in their data sheets. However, there is room for confusion. The PIC data sheets show an inverted socket and do not provide a pictorial view of pinouts so it is unclear what side of the socket Pin 1 is located on. The illustration provided here is **untested** but uses the phone industry standard pinout (the RJ11 plug/socket was originally developed for wired desktop phones).
