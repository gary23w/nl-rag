---
title: "Universal asynchronous receiver-transmitter"
source: https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
---

# Universal asynchronous receiver-transmitter

A **universal asynchronous receiver-transmitter** (**UART** /ˈjuːɑːrt/) is a peripheral device for asynchronous serial communication in which the data format and transmission speeds are configurable. It sends data bits one by one, from the least to most significant, framed by start and stop bits so that precise timing is handled by the communication channel. The electric signaling levels are handled by a driver circuit external to the UART. Common signal levels are RS-232, RS-485, and raw TTL for short debugging links. Early teletypewriters used current loops.

It was one of the earliest computer communication devices, used to attach teletypewriters for an operator console. It was also an early hardware system for the Internet.

A UART is usually implemented in an integrated circuit (IC) and used for serial communications over a computer or peripheral device serial port. One or more UART peripherals are commonly integrated in microcontroller chips. Specialised UARTs are used for automobiles, smart cards and SIMs.

A related device, the universal synchronous and asynchronous receiver-transmitter (USART), also supports synchronous operation.

In OSI model terms, UART falls under layer 2, the data link layer.

## History

Some early telegraph schemes used variable-length pulses (as in Morse code) and rotating clockwork mechanisms to transmit alphabetic characters. The first serial communication devices (with fixed-length pulses) were rotating mechanical switches (*commutators*). Various character codes using 5, 6, 7, or 8 data bits became common in teleprinters and later as computer peripherals. The teletypewriter made an excellent general-purpose I/O device for a small computer.

Gordon Bell of DEC designed the first UART, occupying an entire circuit board called a *line unit*, for the PDP series of computers beginning with the PDP-1. According to Bell, the main innovation of the UART was its use of sampling to convert the signal into the digital domain, allowing more reliable timing than previous circuits that used analog timing devices with manually adjusted potentiometers. To reduce the cost of wiring, backplane and other components, these computers also pioneered flow control using XON and XOFF characters rather than hardware wires.

DEC condensed the line unit design into an early single-chip UART for their own use. Western Digital developed this into the first widely available single-chip UART, the WD1402A, around 1971. This was an early example of a medium-scale integrated circuit. Another popular chip was the SCN2651 from the Signetics 2650 family.

An example of an early 1980s UART was the National Semiconductor 8250, which was used in the original IBM PC's Asynchronous Communications Adapter card. In the 1990s, newer UARTs were developed with on-chip buffers. This allowed higher transmission speed without data loss and without requiring such frequent attention from the computer. For example, the popular National Semiconductor 16550 has a 16-byte FIFO, and spawned many variants, including the *16C550, 16C650, 16C750, and 16C850*.

Depending on the manufacturer, different terms are used to identify devices that perform the UART functions. Intel called their 8251 device a "Programmable Communication Interface" because it was actually a USART and capable of synchronous operation as well as asynchronous. It was introduced in 1979. MOS Technology 6551 was known under the name "Asynchronous Communications Interface Adapter" (ACIA). The term "Serial Communications Interface" (SCI) was first used at Motorola around 1975 to refer to their start-stop asynchronous serial interface device, which others were calling a UART. Zilog manufactured a number of Serial Communication Controllers or SCCs.

Starting in the 2000s, most IBM PC compatible computers removed their external RS-232 COM ports and used USB ports that can send data faster. For users who still need RS-232 serial ports, external USB-to-UART bridges are now commonly used. They combine the hardware cables and a chip to do the USB and UART conversion. Cypress Semiconductor and FTDI are two of the significant commercial suppliers of these chips. Although RS-232 ports are no longer available to users on the outside of most computers, many internal processors have UARTs built into their chips to give hardware designers the ability to interface with other chips or devices that use RS-232 or RS-485 for communication.

## Transmitting and receiving serial data

A UART contains the following components:

- a clock generator, usually a multiple of the bit rate to allow sampling in the middle of a bit period
- input and output shift registers, along with the transmit/receive or FIFO buffers
- transmit/receive control
- read/write control logic

The universal asynchronous receiver-transmitter (UART) takes bytes of data and transmits the individual bits in a sequential fashion. At the destination, a second UART re-assembles the bits into complete bytes. Each UART contains a shift register, which is the fundamental method of conversion between serial and parallel forms. Serial transmission of digital information (bits) through a single wire or other medium is less costly than parallel transmission through multiple wires.

The UART usually does not directly generate or receive the external signals used between different items of equipment. Separate interface devices are used to convert the logic level signals of the UART to and from the external signaling levels, which may be standardized voltage levels, current levels, or other signals.

Communication may be in three modes:

- *simplex* (in one direction only, with no provision for the receiving device to send information back to the transmitting device)
- *full duplex* (both devices send and receive at the same time)
- *half duplex* (devices take turns transmitting and receiving)

For UART to work the following settings need to be the same on both the transmitting and receiving side:

- Voltage level
- Baud rate
- Parity bit
- Data bits size
- Stop bits size
- Flow control

For the voltage level, two UART modules work well when they both have the same voltage level, e.g 3V-3V between the two UART modules. To use two UART modules at different voltage levels, a level shifting circuit needs to be added externally.

### Data framing

A UART frame consists of five elements:

- Idle (logic high (1))
- Start bit (logic low (0)): the start bit signals to the receiver that a new character is coming.
- Data bits: the next five to nine bits, depending on the code set employed, represent the character.
- Parity bit: if a parity bit is used, it would be placed after all of the data bits. The parity bit is a way for the receiving UART to tell if any data has changed during transmission.
- Stop (logic high (1)): the next one or two bits are always in the **mark** (logic high, i.e., 1) condition and called the stop bit(s). They signal to the receiver that the character is complete. Since the start bit is logic low (0) and the stop bit is logic high (1) there are always at least two guaranteed signal changes between characters. If the line is held in the logic low condition for longer than a character time, this is a **break** condition that can be detected by the UART.

In the most common settings of 8 data bits, no parity and 1 stop bit (i.e., 8N1), the protocol efficiency is 8/10 = 80%. For comparison, Ethernet's protocol efficiency when using maximum throughput frames with a payload of 1500 bytes is up to 95% and up to 99% with 9000-byte jumbo frames. However, due to Ethernet's protocol overhead and minimum payload size of 42 bytes, if small messages of one or a few bytes are to be sent, Ethernet's protocol efficiency drops much lower than the UART's 8N1 constant efficiency of 80%.

The idle, no data state is high-voltage, or powered. This is a historic legacy from telegraphy, in which the line is held high to show that the line and transmitter are not damaged.

Each character is framed as a logic low start bit, data bits, possibly a parity bit and one or more stop bits. In most applications, the least significant data bit (the one on the left in this diagram) is transmitted first, but there are exceptions (such as the IBM 2741 printing terminal).

### Receiver

All operations of the UART hardware are controlled by an internal clock signal, which runs at a multiple of the data rate, typically 8 or 16 times the bit rate. The receiver tests the state of the incoming signal on each clock pulse, looking for the beginning of the start bit. If the apparent start bit lasts at least one-half of the bit time, it is valid and signals the start of a new character. If not, it is considered a spurious pulse and is ignored. After waiting a further bit time, the state of the line is again sampled and the resulting level clocked into a shift register. After the required number of bit periods for the character length (5 to 8 bits, typically) have elapsed, the contents of the shift register are made available (in parallel fashion) to the receiving system. The UART will set a flag indicating new data is available, and may also generate a processor interrupt to request that the host processor transfer the received data.

Communicating UARTs have no shared timing system apart from the communication signal. Typically, UARTs resynchronize their internal clocks on each change of the data line that is not considered a spurious pulse. Obtaining timing information in this manner, they reliably receive when the transmitter is sending at a slightly different speed than it should. Simplistic UARTs do not do this; instead, they resynchronize on the falling edge of the start bit only, and then read the center of each expected data bit, and this system works if the broadcast data rate is accurate enough to allow the stop bits to be sampled reliably.

It is a standard feature for a UART to store the most recent character while receiving the next. This "double buffering" gives a receiving computer an entire character transmission time to fetch a received character. Many UARTs have a small first-in, first-out FIFO buffer memory between the receiver shift register and the host system interface. This allows the host processor even more time to handle an interrupt from the UART and prevents loss of received data at high rates.

### Transmitter

Transmission operation is simpler as the timing does not have to be determined from the line state, nor is it bound to any fixed timing intervals. As soon as the sending system deposits a character in the shift register (after completion of the previous character), the UART generates a start bit, shifts the required number of data bits out to the line, generates and sends the parity bit (if used), and sends the stop bits. Since full-duplex operation requires characters to be sent and received at the same time, UARTs use two different shift registers for transmitted and received characters. High-performance UARTs could contain a transmit FIFO (first in, first out) buffer to allow a CPU or DMA controller to deposit multiple characters in a burst into the FIFO rather than have to deposit one character at a time into the shift register. Since transmission of a single or multiple characters may take a long time relative to CPU speeds, a UART maintains a flag showing busy status so that the host system knows if there is at least one character in the transmit buffer or shift register; "ready for next character(s)" may also be signaled with an interrupt.

### Application

Transmitting and receiving UARTs must be set for the same bit speed (Baud rate), character length, parity, and number of stop bits for proper operation. The receiving UART may detect some mismatched settings and set a "framing error" flag bit for the host system; in exceptional cases, the receiving UART will produce an erratic stream of mutilated characters and transfer them to the host system.

Typical serial ports used with personal computers connected to modems use one start bit, eight data bits, no parity, and one stop bit; for this configuration, the number of ASCII characters per second equals the bit rate divided by 10.

Some very low-cost home computers or embedded systems that lack a physical UART may instead emulate the protocol with software by sampling the state of an input port or directly manipulating an output port for data transmission. While very CPU-intensive (since the CPU timing is critical), the UART chip can thus be omitted, saving money and space. The technique is known as bit-banging.

## Models

Most parts in the following table are discontinued and no longer being manufactured. A dual UART, or *DUART*, combines two UARTs into a single chip. Similarly, a quadruple UART or *QUART*, combines four UARTs into one package, such as the NXP 28L194. An octal UART or *OCTART* combines eight UARTs into one package, such as the Exar XR16L788 or the NXP SCC2698.

| Model | Description |
|---|---|
| WD1402A | The first single-chip UART on general sale. Introduced about 1971. Compatible chips included the Fairchild TR1402A and the General Instruments AY-5-1013. |
| Exar XR21V1410 |   |
| Intersil 6402 |   |
| CDP 1854 (RCA, now Intersil) |   |
| Zilog Z8440 | Universal synchronous and asynchronous receiver-transmitter (USART). 2000 kbit/s. Async, Bisync, SDLC, HDLC, X.25. CRC. 4-byte RX buffer. 2-byte TX buffer. Provides signals needed by a third party DMA controller to perform DMA transfers. |
| Z8530/Z85C30 | This USART has a 3-byte receive buffer and a 1-byte transmit buffer. It has hardware to accelerate the processing of HDLC and SDLC. The CMOS version (Z85C30) provides signals to allow a third party DMA controller to perform DMA transfers. It can do asynchronous, byte-level synchronous, and bit-level synchronous communications. |
| 8250 | Obsolete with 1-byte buffers. These UARTs' maximum standard serial port speed is 9600 bits per second if the operating system has a 1 millisecond interrupt latency. 8250 UARTs were used in the IBM PC 5150 and IBM PC/XT, while the 16450 UART were used in IBM PC/AT-series computers. The 8251 has USART capability. |
| 8251 |   |
| Motorola 6850 |   |
| 6551 |   |
| Rockwell 65C52 |   |
| 16450 |   |
| 82510 | This UART allows asynchronous operation up to 288 kbit/s, with two independent four-byte FIFOs. It was produced by Intel from at least 1993 to 1996, and Innovastic Semiconductor has a 2011 Data Sheet for IA82510. |
| 16550 | This UART's FIFO is broken, so it cannot safely run any faster than the 16450 UART. The 16550A and later versions fix this bug. |
| 16550A | This UART has 16-byte FIFO buffers. Its receive interrupt trigger levels can be set to 1, 4, 8, or 14 characters. Its maximum standard serial port speed if the operating system has a 1 millisecond interrupt latency is 128 kbit/s. Systems with lower interrupt latencies or with DMA controllers could handle higher baud rates. This chip can provide signals that are needed to allow a DMA controller to perform DMA transfers to and from the UART if the DMA mode this UART introduces is enabled. It was introduced by National Semiconductor, which has been sold to Texas Instruments. National Semiconductor claimed that this UART could run at up to 1.5 Mbit/s. |
| 16C552 |   |
| 16650 | This UART was introduced by Startech Semiconductor which is now owned by Exar Corporation and is not related to Startech.com. Early versions have a broken FIFO buffer and therefore cannot safely run any faster than the 16450 UART. Versions of this UART that were not broken have 32-character FIFO buffers and could function at standard serial port speeds up to 230.4 kbit/s if the operating system has a 1 millisecond interrupt latency. Current versions of this UART by Exar claim to be able to handle up to 1.5 Mbit/s. This UART introduces the Auto-RTS and Auto-CTS features in which the RTS# signal is controlled by the UART to signal the external device to stop transmitting when the UART's buffer is full to or beyond a user-set trigger point and to stop transmitting to the device when the device drives the CTS# signal high (logic 0). |
| 16750 | 64-byte buffers. This UART can handle a maximum standard serial port speed of 460.8 kbit/s if the maximum interrupt latency is 1 millisecond. This UART was introduced by Texas Instruments. TI claims that early models can run up to 1 Mbit/s, and later models in this series can run up to 3 Mbit/s. |
| 16850 | 128-byte buffers. This UART can handle a maximum standard serial port speed of 921.6 kbit/s if the maximum interrupt latency is 1 millisecond. This UART was introduced by Exar Corporation. Exar claims that early versions can run up to 2 Mbit/s, and later versions can run up to 2.25 Mbit/s depending on the date of manufacture. |
| 16C850 |   |
| 16950 | 128-byte buffers. This now-discontinued UART can handle a maximum standard serial port speed of 921.6 kbit/s if the maximum interrupt latency is 1 millisecond. This UART supports 9-bit characters in addition to the 5- to 8-bit characters that other UARTs support. This was introduced by Oxford Semiconductor which was bought by PLX Technology. Oxford/PLX claimed that this UART can run up to 15 Mbit/s. PCI Express variants by Oxford/PLX are integrated with a first-party bus mastering PCIe DMA controller. This DMA controller uses the UART's DMA mode signals that were defined for the 16550. The DMA controller requires the CPU to set up each transaction and poll a status register after the transaction is started to determine if the transaction is done. Each DMA transaction can transfer between 1 and 128 bytes between a memory buffer and the UART. PCI Express variants can also allow the CPU to transfer data between itself and the UART with 8-, 16-, or 32-bit transfers when using programmed I/O. |
| 16C950 |   |
| 16954 | Quad-port version of the 16950/16C950. 128-byte buffers. This now-discontinued UART can handle a maximum standard serial port speed of 921.6 kbit/s if the maximum interrupt latency is 1 millisecond. This UART supports 9-bit characters in addition to the 5- to 8-bit characters that other UARTs support. This was introduced by Oxford Semiconductor which was bought by PLX Technology. Oxford/PLX claimed that this UART can run up to 15 Mbit/s. PCI Express variants by Oxford/PLX are integrated with a first-party bus mastering PCIe DMA controller. This DMA controller is controlled by the UART's DMA mode signals that were defined for the 16550. The DMA controller requires the CPU to set up each transaction and poll a status register after the transaction is started to determine if the transaction is done. Each DMA transaction can transfer between 1 and 128 bytes between a memory buffer and the UART. PCI Express variants can also allow the CPU to transfer data between itself and the UART with 8-, 16-, or 32-bit transfers when using programmed I/O. |
| 16C954 |   |
| 16C1550/16C1551 | UART with 16-byte FIFO buffers. Up to 1.5 Mbit/s. The ST16C155X is not compatible with the industry standard 16550 and will not work with the standard serial port driver in Microsoft Windows. |
| 16C2450 | Dual UART with 1-byte FIFO buffers. |
| 16C2550 | Dual UART with 16-byte FIFO buffers. Pin-to-pin and functionally compatible with 16C2450. Software compatible with INS8250 and NS16C550. |
| SCC2691 | Currently produced by NXP, the 2691 is a single-channel UART that also includes a programmable counter/timer. The 2691 has a single-byte transmitter holding register and a 4-byte receive FIFO. Maximum standard speed of the 2692 is 115.2 kbit/s. The 28L91 is an upwardly compatible version of the 2691, featuring selectable 8- or 16-byte transmitter and receiver FIFOs, improved support for extended data rates, and faster bus timing characteristics, making the device more suitable for use with high-performance microprocessors. Both the 2691 and 28L91 may also be operated in TIA-422 and TIA-485 modes, and may also be programmed to support non-standard data rates. The devices are produced in PDIP-40, PLCC-44 and 44-pin QFP packages, and are readily adaptable to both Motorola and Intel buses. They have also been successfully adapted to the 65C02 and 65C816 buses. The 28L91 will operate on 3.3 or 5 volts. |
| SCC28L91 |   |
| SCC2692 | Currently produced by NXP, these devices are dual UARTs (DUART), consisting of two communications channels, associated control registers and one counter/timer. Each communication channel is independently programmable and supports independent transmit and receive data rates. The 2692 has a single-byte transmitter holding register and a 4-byte receiver FIFO for each channel. Maximum standard speed of both of the 2692's channels is 115.2 kbit/s. The 26C92 is an upwardly compatible version of the 2692, with 8-byte transmitter and receiver FIFOs for improved performance during continuous bi-directional asynchronous transmission (CBAT) on both channels at the maximum standard speed of 230.4 kbit/s. The letter C in the 26C92 part number has nothing to do with the fabrication process; all NXP UARTs are CMOS devices. The 28L92 is an upwardly compatible version of the 26C92, featuring selectable 8- or 16-byte transmitter and receiver FIFOs, improved support for extended data rates, and faster bus timing characteristics, making the device more suitable for use with high-performance microprocessors. The 2692, 26C92 and 28L92 may be operated in TIA-422 and TIA-485 modes, and may also be programmed to support non-standard data rates. The devices are produced in PDIP-40, PLCC-44 and 44-pin QFP packages, and are readily adaptable to both Motorola and Intel buses. They have also been successfully adapted to the 65C02 and 65C816 buses. The 28L92 will operate on 3.3 or 5 volts. |
| SC26C92 |   |
| SC28L92 |   |
| SCC28C94 | Currently produced by NXP, the 28C94 quadruple UART (QUART) is functionally similar to a pair of SCC26C92 DUARTs mounted in a common package, with the addition of an arbitrated interrupt system for efficient processing during periods of intense channel activity. Some additional signals are present to support the interrupt management features and the auxiliary input/output pins are arranged differently than those of the 26C92. Otherwise, the programming model for the 28C94 is similar to that of the 26C92, requiring only minor code changes to fully utilize all features. The 28C94 supports a maximum standard speed of 230.4 kbit/s, is available in a PLCC-52 package, and is readily adaptable to both Motorola and Intel buses. It has also been successfully adapted to the 65C816 bus. |
| SCC2698B | Currently produced by NXP, the 2698 octal UART (OCTART) is essentially four SCC2692 DUARTs in a single package. Specifications are the same as the SCC2692 (not the SCC26C92). Due to the lack of transmitter FIFOs and the small size of the receiver FIFOs, the 2698 can cause an interrupt "storm" if all channels are simultaneously engaged in continuous bi-directional communication. The device is produced in PDIP-64 and PLCC-84 packages, and is readily adaptable to both Motorola and Intel buses. The 2698 has also been successfully adapted to the 65C02 and 65C816 buses. |
| SCC28L198 | Currently produced by NXP, the 28L198 OCTART is essentially an upscaled enhancement of the SCC28C94 QUART described above, with eight independent communications channels, as well as an arbitrated interrupt system for efficient processing during periods of intense channel activity. The 28L198 supports a maximum standard speed of 460.8 kbit/s, is available in PLCC-84 and LQFP-100 packages, and is readily adaptable to both Motorola and Intel buses. The 28L198 will operate on 3.3 or 5 volts. |
| Z85230 | Synchronous/Asynchronous modes (USART), 2 ports. Provides signals needed by a third-party DMA controller to perform DMA transfers. 4-byte buffer to send, 8-byte buffer to receive per channel. SDLC/HDLC modes. 5 Mbit/s in synchronous mode. |
| Hayes ESP | 1 KB buffers, 921.6 kbit/s, 8-ports. |
| Exar XR17V352, XR17V354 and XR17V358 | Dual, Quad and Octal PCI Express UARTs with 16550 compatible register Set, 256-byte TX and RX FIFOs, Programmable TX and RX Trigger Levels, TX/RX FIFO Level Counters, Fractional baud rate generator, Automatic RTS/CTS or DTR/DSR hardware flow control with programmable hysteresis, Automatic Xon/Xoff software flow control, RS-485 half duplex direction control output with programmable turn-around delay, Multi-drop with Auto Address Detection, Infrared (IrDA 1.1) data encoder/decoder. They are specified up to 25 Mbit/s. DataSheets are dated from 2012. |
| Exar XR17D152, XR17D154 and XR17D158 | Dual, Quad and Octal PCI bus UARTs with 16C550 Compatible 5G Register Set, 64-byte Transmit and Receive FIFOs, Transmit and Receive FIFO Level Counters, Programmable TX and RX FIFO Trigger Level, Automatic RTS/CTS or DTR/DSR Flow Control, Automatic Xon/Xoff Software Flow Control, RS485 HDX Control Output with Selectable Turn-around Delay, Infrared (IrDA 1.0) Data Encoder/Decoder, Programmable Data Rate with Prescaler, Up to 6.25 Mbit/s Serial Data Rate. DataSheets are dated from 2004 and 2005. |
| Exar XR17C152, XR17C154 and XR17C158 | Dual, Quad and Octal 5 V PCI bus UARTs with 16C550 Compatible Registers, 64-byte Transmit and Receive FIFOs, Transmit and Receive FIFO Level Counters, Automatic RTS/CTS or DTR/DSR Flow Control, Automatic Xon/Xoff Software Flow Control, RS485 Half-duplex Control with Selectable Delay, Infrared (IrDA 1.0) Data Encoder/Decoder, Programmable Data Rate with Prescaler, Up to 6.25 Mbit/s Serial Data Rate. DataSheets are dated from 2004 and 2005. |
| Exar XR17V252, XR17V254 and XR17V258 | Dual, Quad and Octal 66 MHz PCI bus UARTs with Power Management Support, 16C550 compatible register set, 64-byte TX and RX FIFOs with level counters and programmable trigger levels, Fractional baud rate generator, Automatic RTS/CTS or DTR/DSR hardware flow control with programmable hysteresis, Automatic Xon/Xoff software flow control, RS-485 half duplex direction control output with selectable turn-around delay, Infrared (IrDA 1.0) data encoder/decoder, Programmable data rate with prescaler. DataSheets are dated from 2008 and 2010. |
| ASIX AS99100 and AS99100A | PCIe chips that can operate in 4 different modes: a QUART, a DUART and a parallel port, a DUART and an SPI interface (of which the AS99100A can interface with an SPI flash ROM), or an ISA-like bus. All modes other than the PCIe to ISA-like bus have additional GPIO pins. The UARTs in each mode other than ISA-like bus bridge mode have 256-byte FIFOs for each direction, support DMA burst transfers, and support up to 25 Mbit/s bidirectional throughput per serial port. |

## Uses

Some modems for personal computers that plug into a motherboard slot include the UART function on the card. The original 8250 UART chip shipped with the IBM personal computer had a one-character buffer for the receiver and the transmitter each, which meant that communications software performed poorly at speeds above 9600 bit/s, especially if operating under a multitasking system or if handling interrupts from disk controllers. High-speed modems used UARTs that were compatible with the original chip but which included additional FIFO buffers, giving software additional time to respond to incoming data.

A look at the performance requirements at high bit rates shows why the 16-, 32-, 64- or 128-byte FIFO is a necessity. The Microsoft specification for a DOS system requires that interrupts not be disabled for more than 1 millisecond at a time. Some hard disk drives and video controllers violate this specification. 9600 bit/s will deliver a character approximately every millisecond, so a 1-byte FIFO should be sufficient at this rate on a DOS system that meets the maximum interrupt disable timing. Rates above this may receive a new character before the old one has been fetched, and thus the old character will be lost. This is referred to as an overrun error and results in one or more lost characters.

A 16-byte FIFO allows up to 16 characters to be received before the computer has to service the interrupt. This increases the maximum bit rate the computer can process reliably from 9600 to 153,000 bit/s if it has a 1 millisecond interrupt dead time. A 32-byte FIFO increases the maximum rate to over 300,000 bit/s. A second benefit to having a FIFO is that the computer only has to service about 8 to 12% as many interrupts, allowing more CPU time for updating the screen or doing other chores. Thus, the computer's responses will improve as well.

## Emulation

Since the UART's communication protocol is simple, it can be emulated by bit banging GPIO pins in software on modern microcontrollers (e.g. Arduino or Teensy), or on programmable I/O state machines (e.g. Raspberry Pi Pico's PIO or NXP's FlexIO).
