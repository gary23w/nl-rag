---
title: "Serial communication"
source: https://en.wikipedia.org/wiki/Serial_communication
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
---

# Serial communication

In telecommunication and data transmission, **serial communication** is the process of sending data one bit at a time, sequentially, over a communication channel or computer bus. This is in contrast to parallel communication, where several bits are sent as a whole, on a link with several parallel channels.

Serial communication is used for all long-haul communication and most computer networks, where the cost of cable and difficulty of synchronization make parallel communication impractical. Serial computer buses have become more common even at shorter distances, as improved signal integrity and transmission speeds in newer serial technologies have begun to outweigh the parallel bus's advantage of simplicity (no need for serializer and deserializer, or SerDes) and to outstrip its disadvantages (clock skew, interconnect density). The migration from PCI to PCI Express (PCIe) is an example.

Modern high speed serial interfaces such as PCIe send data several bits at a time using modulation/encoding techniques such as PAM4 which groups 2 bits at a time into a single symbol, and several symbols are still sent one at a time. This replaces PAM2 or non return to zero (NRZ) which only sends one bit at a time, or in other words one bit per symbol. The symbols are sent at a speed known as the symbol rate or the baud rate.

## Cables

Many serial communication systems were originally designed to transfer data over relatively large distances through some sort of data cable.

Practically all long-distance communication transmits data one bit at a time, rather than in parallel, because it reduces the cost of the cable. The cables that carry this data (other than "the" serial cable) and the computer ports they plug into are usually referred to with a more specific name, to reduce confusion.

Keyboard and mouse cables and ports are almost invariably serial—such as PS/2 port, Apple Desktop Bus and USB.

The cables that carry digital video are also mostly serial—such as coax cable plugged into a HD-SDI port, a webcam plugged into a USB port or FireWire port, Ethernet cable connecting an IP camera to a Power over Ethernet port, FPD-Link, digital telephone lines (ex. ISDN), etc.

Other such cables and ports, transmitting data one bit at a time, include Serial ATA, Serial SCSI, Ethernet cable plugged into Ethernet ports, the Display Data Channel using previously reserved pins of the VGA connector or the DVI port or the HDMI port.

## Serial buses

Many communication systems were generally designed to connect two integrated circuits on the same printed circuit board, connected by signal traces on that board (rather than external cables).

Integrated circuits are more expensive when they have more pins. To reduce the number of pins in a package, many ICs use a serial bus to transfer data when speed is not important. Some examples of such low-cost lower-speed serial buses include RS-232, DALI, SPI, CAN bus, I²C, UNI/O, and 1-Wire. Higher-speed serial buses include USB, SATA and PCI Express.

## Serial versus parallel

The communication links, across which computers (or parts of computers) talk to one another, may be either serial or parallel. A parallel link transmits several streams of data simultaneously along multiple channels (e.g., wires, printed circuit tracks, or optical fibers); whereas, a serial link transmits only a single stream of data. The rationale for parallel communication was the added benefit of having Direct Memory Access to the 8-bit or 16-bit registry addresses at a time when mapping direct data lanes was more convenient and faster than synchronizing data serially.

Although a serial link may seem inferior to a parallel one, since it can transmit less data per clock cycle, it is often the case that serial links can be clocked considerably faster than parallel links in order to achieve a higher data rate. Several factors allow serial to be clocked at a higher rate:

- Clock skew between different channels is not an issue (for unclocked asynchronous serial communication links). This can be caused by mismatched wire or conductor lengths.
- A serial connection requires fewer interconnecting cables (e.g., wires/fibers) and hence occupies less space. The extra space allows for better isolation of the channel from its surroundings.
- Crosstalk is less of an issue, because there are fewer conductors in proximity.
- Budgets for power use, power dissipation, cable cost, component cost, IC die area, PC board area, ESD protection, etc. can be focused on a single link.

The transition from parallel to serial buses was allowed by Moore's law which allowed for the incorporation of SerDes in integrated circuits. An electrical serial link only requires a pair of wires, whereas a parallel link requires several. Thus serial links can save on costs (also known as the Bill of Materials). Differential signalling uses length-matched wires or conductors and are used in high speed serial links. Length-matching is easier to perform on serial links as they require fewer conductors.

In many cases, serial is cheaper to implement than parallel. Many ICs have serial interfaces, as opposed to parallel ones, so that they have fewer pins and are therefore less expensive.

## Examples of architectures

- ARINC 818 Avionics Digital Video Bus
- Atari SIO (Joe Decuir credits his work on Atari SIO as the basis of USB)
- Binary Synchronous Communications BSC - Binary Synchronous Communications
- CAN Control Area Network Vehicle Bus
- ccTalk Used in the money transaction and point-of-sale industry
- CoaXPress industrial camera protocol over Coax
- DMX512 control of theatrical lighting
- Ethernet
- Fiber Distributed Data Interface
- Fibre Channel (high-speed, for connecting computers to mass storage devices)
- FireWire
- HDMI
- HyperTransport
- InfiniBand (very high speed, broadly comparable in scope to PCI)
- I²C multidrop serial bus
- MIDI control of electronic musical instruments
- MIL-STD-1553A/B
- Morse code telegraphy
- PCI Express
- Profibus
- RS-232 (low-speed, implemented by serial ports)
- RS-422 multidrop serial bus
- RS-423
- RS-485 multidrop multimaster serial bus
- SDI-12 industrial sensor protocol
- SERCOM
- Serial ATA
- Serial Attached SCSI
- Shift register with serial-in and serial-out configuration
- SONET and SDH (high speed telecommunication over optical fibers)
- SpaceWire Spacecraft communication network
- S/PDIF and AES3 audio communication protocols
- SPI
- T-1, E-1 and variants (high speed telecommunication over copper pairs)
- Universal Serial Bus (for connecting peripherals to computers)
- UNI/O multidrop serial bus
- 1-Wire multidrop serial bus
