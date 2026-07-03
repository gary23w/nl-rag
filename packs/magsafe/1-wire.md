---
title: "1-Wire"
source: https://en.wikipedia.org/wiki/1-Wire
domain: magsafe
license: CC-BY-SA-4.0
tags: magsafe
fetched: 2026-07-03
---

# 1-Wire

**1-Wire** is a wired half-duplex serial bus designed by Dallas Semiconductor that provides low-speed (standard 16.3 kbit/s; "overdrive" at 10×) data communication and supply voltage over a single conductor.

1-Wire is similar in concept to I2C, but with lower data rates and longer range. It is typically used to communicate with small inexpensive devices such as digital thermometers and weather instruments. A network of 1-Wire devices with an associated master device is called a **MicroLAN**. The protocol is also used in small, 16 mm electronic keys known as a **Dallas key** or **iButton**.

One distinctive feature of the bus is the possibility of using only two conductors — data and ground. To accomplish this, 1-Wire devices integrate a small capacitor (~800 pF) to store charge, which powers the device during periods when the data line is active.

## Usage example

1-Wire devices are available in different packages: integrated circuits, a TO-92-style package (as typically used for transistors), and a portable form called an iButton or Dallas key which is a small stainless-steel package that resembles a watch battery. Manufacturers also produce devices more complex than a single component that use the 1-Wire bus to communicate.

1-Wire devices can fit in different places in a system. It might be one of many components on a circuit board within a product. It also might be a single component within a device such as a temperature probe. It could be attached to a device being monitored. Some laboratory systems connect to 1-Wire devices using cables with modular connectors or CAT-5 cable. In such systems, RJ11 (6P2C or 6P4C modular plugs, commonly used for telephones) are popular.

Systems of sensors and actuators can be built by wiring together many 1-Wire components. Each 1-Wire component contains all of the logic needed to operate on the 1-Wire bus. Examples include temperature loggers, timers, voltage and current sensors, battery monitors, and memory. These can be connected to a PC using a bus converter. USB, RS-232 serial, and parallel port interfaces are popular solutions for connecting a MicroLan to the host PC. 1-Wire devices can also be interfaced directly to microcontrollers from various vendors.

iButtons are connected to 1-Wire bus systems by means of sockets with contacts that touch the "lid" and "base" of the canister. Alternatively, the connection can be semi-permanent with a socket into which the iButton clips, but from which it is easily removed.

Each 1-Wire chip has a unique identifier code. This feature makes the chips, especially iButtons, suitable electronic keys. Some uses include locks, burglar alarms, computer systems, manufacturer-approved accessories, time clocks and courier and maintenance keys for smart safes.

iButtons have been used as Akbil smart tickets for the public transport in Istanbul. They can also run smartcard programs such as Java Card 2.0, as exemplified by the "Java Ring" of 1998.

### Power supplies

Apple MagSafe- and MagSafe-2-connector–equipped power supplies, displays, and Mac laptops use the 1-Wire protocol to send and receive data to and from the connected Mac laptop, via the middle pin of the connector. Data include power supply model, wattage, and serial number; and laptop commands to send full power, and illuminate the red or green light-emitting diodes in the connector.

Dell laptop power supplies use the 1-Wire protocol to send data via the third wire to the laptop computer about power, current and voltage ratings. The laptop will then refuse charging if the adapter does not meet requirements.

## Communication protocol

In any MicroLan, there is always one master in overall charge, which may be a personal computer or a microcontroller. The master initiates activity on the bus, simplifying the avoidance of collisions on the bus. Protocols are built into the master's software to detect collisions. After a collision, the master retries the required communication.

A 1-Wire network is a single open drain wire with a single pull-up resistor. The pull-up resistor pulls the wire up to 3 or 5 volts. The master device and all the slaves each have a single open-drain connection to drive the wire, and a way to sense the state of the wire. Despite the "1-Wire" name, all devices must also have a second conductor for a ground connection to permit a return current to flow through the data wire. Communication occurs when a master or slave briefly pulls the bus low, *i.e.*, connects the pull-up resistor to ground through its output MOSFET. The data wire is high when idle, and so it can also power a limited number of slave devices. Data rates of 16.3 kbit/s can be achieved. There is also an overdrive mode that speeds up the communication by a factor of 10.

A short 1-Wire bus can be driven from a single digital I/O pin on a microcontroller. A universal asynchronous receiver-transmitter (UART) can also be used. Specific 1-Wire driver and bridge chips are available. Universal Serial Bus "bridge" chips are also available. Bridge chips are particularly useful to drive cables longer than 100 m. Up to 300-meter twisted pairs, *i.e.*, telephone cables, have been tested by the manufacturer. These extreme lengths require adjustments to the pull-up resistances from 5 to 1 kΩ.

The master starts a transmission with a *reset* pulse, which pulls the wire to 0 volts for at least 480 μs. This resets every slave device on the bus. After that, any slave device, if present, shows that it exists with a "presence" pulse: it holds the bus low for at least 60 μs after the master releases the bus.

To send a binary number "1", the bus master sends a very brief (1–15 μs) low pulse. To send a binary number "0", the master sends a 60 μs low pulse. The falling (negative) edge of the pulse is used to start a monostable multivibrator in the slave device. The multivibrator in the slave reads the data line about 30 μs after the falling edge. The slave's internal timer is an inexpensive analog timer. It has analog tolerances that affect its timing accuracy. Therefore, the pulses are calculated to be within margins. Therefore, the "0" pulses have to be 60 μs long, and the "1" pulses can't be longer than 15 μs.

When receiving data, the master sends a 1–15 μs 0 volt pulse to start each bit. If the transmitting slave unit wants to send a "1", it does nothing, and the bus goes to the pulled-up voltage. If the transmitting slave wants to send a "0", it pulls the data line to ground for 60 μs.

The basic sequence is a reset pulse followed by an eight-bit command, and then data are sent or received in groups of eight bits.

When a sequence of data is being transferred, errors can be detected with an eight-bit CRC (weak data protection)..

Many devices can share the same bus. Each device on the bus has a 64-bit serial number, of which eight bits are used as a checksum, thus allowing a "universe" of 256 (over 7.2 × 1016) unique device identities. The least significant byte of the serial number is an eight-bit number that tells the type of the device. The most significant byte is a standard (for the 1-Wire bus) eight-bit CRC.

There are several standard broadcast commands, as well as commands used to address a particular device. The master can send a selection command, then the address of a particular device. The next command is executed only by the addressed device.

The 1-Wire bus enumeration protocol, like other singulation protocols, is an algorithm the master uses to read the address of every device on the bus. Since the address includes the device type and a CRC, recovering the roster of addresses also produces a reliable inventory of the devices on the bus. To find the devices, the master broadcasts an enumeration command, and then an address, "listening" after each bit of an address. If a slave's address matches all the address bits sent so far, it returns a 0. The master uses this simple behavior to search systematically for valid sequences of address bits. The process is much faster than a brute force search of all possible 56-bit numbers, because as soon as an invalid bit is detected, all subsequent address bits are known to be invalid. The 56-bit address space is searched as a binary tree, allowing up to 75 devices to be found per second. The order in which device addresses are discovered by this enumeration protocol is deterministic and depends only on the device type and serial number. Bit-reversing these 56 bits yields the order of discovery for devices using Maxim's published algorithm (algorithm defined in Application Note 187). The search algorithm can be implemented in an alternative form, initially searching paths with address bits equal to 1, rather than 0. In this case, inverting the 56 address bits and then reversing them yields the order of discovery.

The location of devices on the bus is sometimes significant. For these situations, a microcontroller can use several pins, or the manufacturer has a 1-Wire device that can switch the bus off or pass it on. Software can therefore explore sequential *bus domains*.

## ROM family codes

Every 1-Wire device's 64-bit ROM ID ends with an 8-bit family code. In most cases this byte is assigned to a single part number, so reading it from the bus is usually enough to identify the device—for example, 0x10 (DS18S20 thermometer), 0x01 (DS2401 silicon serial number), or 0x2D (DS2431 1 kbit EEPROM).

Various people have created online databases of family codes from the broad range of 1-Wire memory, authenticator, ID, and battery-monitor devices.

## Example communication with a device

The following signals were generated by an FPGA, which was the master for the communication with a DS2432 (1 kbit EEPROM with SHA-1 Engine) chip, and measured with a logic analyzer. A logic high on the 1-Wire output, means the output of the FPGA is in tri-state mode and the 1-Wire device can pull the bus low. A low means the FPGA pulls down the bus. The 1-Wire input is the measured bus signal. On input sample time high, the FPGA samples the input for detecting the device response and receiving bits.

## Development tools

When developing and/or troubleshooting the 1-Wire bus, examination of hardware signals can be very important. Logic analyzers and bus analyzers are tools that collect, analyze, decode, and store signals to simplify viewing the high-speed waveforms.
