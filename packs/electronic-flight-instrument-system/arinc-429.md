---
title: "ARINC 429"
source: https://en.wikipedia.org/wiki/ARINC_429
domain: electronic-flight-instrument-system
license: CC-BY-SA-4.0
tags: electronic flight instrument system
fetched: 2026-07-05
---

# ARINC 429

**ARINC 429**, the "Mark 33 Digital Information Transfer System (DITS)," is the ARINC technical standard for the predominant avionics data bus used on most higher-end commercial and transport aircraft. It defines the physical and electrical interfaces of a two-wire data bus and a data protocol to support an aircraft's avionics local area network.

## Technical description

### Medium and signaling

ARINC 429 is a data transfer standard for aircraft avionics. It uses a self-clocking, self-synchronizing data bus protocol (Tx and Rx are on separate ports). The physical connection wires are twisted pairs carrying balanced differential signaling. Data words are 32 bits in length and most messages consist of a single data word. Messages are transmitted at either 12.5 or 100 kbit/s to other system elements that are monitoring the bus messages. The transmitter constantly transmits either 32-bit data words or the NULL state (0 Volts). A single wire pair is limited to one transmitter and no more than 20 receivers. The protocol allows for self-clocking at the receiver end, thus eliminating the need to transmit clocking data. ARINC 429 is an alternative to MIL-STD-1553.

### Bit numbering, transmission order, and bit significance

The ARINC 429 unit of transmission is a fixed-length 32-bit frame, which the standard refers to as a 'word'. The bits within an ARINC 429 word are serially identified from Bit Number 1 to Bit Number 32 or simply Bit 1 to Bit 32. The fields and data structures of the ARINC 429 word are defined in terms of this numbering.

While it is common to illustrate serial protocol frames progressing in time from right to left, a reversed ordering is commonly practiced within the ARINC standard. Even though ARINC 429 word transmission begins with Bit 1 and ends with Bit 32, it is common to diagram and describe ARINC 429 words in the order from Bit 32 to Bit 1. In simplest terms, while the transmission order of bits (from the first transmitted bit to the last transmitted bit) for a 32-bit frame is conventionally diagrammed as

First bit > 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ... 29, 30, 31, 32 < Last bit,

this sequence is often diagrammed in ARINC 429 publications in the opposite direction as

Last bit > 32, 31, 30, 29, ... 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 < First bit.

Generally, when the ARINC 429 word format is illustrated with Bit 32 to the left, the numeric representations in the data field are read with the most significant bit on the left. However, in this particular bit order presentation, the Label field reads with its most significant bit on the right. Like CAN Protocol Identifier Fields, ARINC 429 *label fields* are transmitted most significant bit first. However, like UART Protocol, Binary-coded decimal numbers and binary numbers in the ARINC 429 *data fields* are generally transmitted least significant bit first.

Some equipment suppliers publish the bit transmission order as

First bit >

8, 7, 6, 5, 4, 3, 2, 1,

9, 10, 11, 12, 13 ... 32 < Last bit.

The suppliers that use this representation have in effect renumbered the bits in the Label field, converting the standard's MSB 1 bit numbering for that field to LSB 1 bit numbering. This renumbering highlights the relative reversal of "bit endianness" between the Label representation and numeric data representations as defined within the ARINC 429 standard. Of note is how the *87654321* bit numbering is similar to the *76543210* bit numbering common in digital equipment; but reversed from the *12345678* bit numbering defined for the ARINC 429 Label field.

This notional reversal also reflects historical implementation details. ARINC 429 transceivers have been implemented with 32-bit shift registers. Parallel access to that shift register is often octet-oriented. As such, the bit order of the octet access is the bit order of the accessing device, which is usually LSB 0; and serial transmission is arranged such that the least significant bit of each octet is transmitted first. So, in common practice, the accessing device wrote or read a "reversed label" (for example, to transmit a Label 2138 [or 8B16] the bit-reversed value D116 is written to the Label octet). Newer or "enhanced" transceivers may be configured to reverse the Label field bit order "in hardware".

### Word format

ARINC 429 Word Format

P

SSM

MSB

Data

LSB

SDI

LSB

Label

MSB

32

31

30

29

28

27

26

25

24

23

22

21

20

19

18

17

16

15

14

13

12

11

10

9

8

7

6

5

4

3

2

1

Each ARINC 429 word is a 32-bit sequence that contains five fields:

Bit 32

is the

parity bit

, and is used to verify that the word was not damaged or garbled during transmission. Every ARINC 429 channel typically uses "odd" parity - there must be an odd number of "1" bits in the word. This bit is set to 0 or 1 to ensure that the correct number of bits are set to 1 in the word.

Bits 30 to 31

are the Sign/Status Matrix (SSM) - these bits may have various encodings dependent on the particular data representation applied to a given word:

- In all cases using the SSM, these bits may be encoded to indicate:

Normal Operation (NO) - Indicates the data in this word is considered to be correct data.

Functional Test (FT) - Indicates that the data is being provided by a test source.

Failure Warning (FW) - Indicates a failure which causes the data to be suspect or missing.

No Computed Data (NCD) - Indicates that the data is missing or inaccurate for some reason other than a failure. For example, autopilot commands will show as NCD when the autopilot is not turned on.

- In the case of binary-coded decimal (BCD) representation, the SSM may also indicate the Sign (+/-) of the data or some information analogous to sign, like an orientation (North/South; East/West). When so indicating sign, the SSM is also considered to be indicating Normal Operation.
- In the case of two's-complement representation of signed binary numbers (BNR), Bit 29 represents the number's sign; that is, sign indication is delegated to Bit 29 in this case.
- In the case of discrete data representation (e.g., bit-fields), the SSM has a different, signless encoding.

| SSM | Data Dependent SSM Encodings: |   |   |   |
|---|---|---|---|---|
| Bit 31 | Bit 30 | Sign/Status Matrix for BCD Data | Status Matrix for BNR Data | Status Matrix for Discrete Data |
| 0 | 0 | Plus, North, East, Right, To, Above | Failure Warning (FW) | Verified Data, Normal Operation |
| 0 | 1 | No Computed Data (NCD) | No Computed Data (NCD) | No Computed Data (NCD) |
| 1 | 0 | Functional Test (FT) | Functional Test (FT) | Functional Test (FT) |
| 1 | 1 | Minus, South, West, Left, From, Below | Normal Operation (NO) | Failure Warning (FW) |

| Bit 29 | Sign Matrix for BNR Data |
|---|---|
| 0 | Plus, North, East, Right, To, Above |
| 1 | Minus, South, West, Left, From, Below |

Bits 11 to 29

contain the data.

Bit-field

discrete data,

binary-coded decimal

(BCD), and

Binary Number Representation

(BNR) are common ARINC 429 data formats. Data formats may also be mixed.

Bits 9 and 10

are Source/Destination Identifiers (SDI) and may indicate the intended receiver or, more frequently, indicate the transmitting subsystem.

Bits 1 to 8

contain a label (label words), expressed in

octal

(

MSB 1 bit numbering

), identifying the data type.

The image below exemplifies many of the concepts explained in the adjacent sections. In this image the Label (260) appears in red, the Data in blue-green and the Parity bit in navy blue.

Example ARINC 429

P

SSM

MSB

Data

LSB

SDI

LSB

Label

MSB

32

31

30

29

28

27

26

25

24

23

22

21

20

19

18

17

16

15

14

13

12

11

10

9

8

7

6

5

4

3

2

1

1

0

0

1

0

0

0

1

1

0

0

0

1

1

0

0

0

1

0

0

0

1

0

0

0

0

0

0

1

1

0

1

1

0

2

3

3

17

0

0

6

2

Day(1)

Day(0)

Month

Milliseconds

## Labels

Label guidelines are provided as part of the ARINC 429 specification, for various equipment types. Each aircraft will contain a number of different systems, such as flight management computers, inertial reference systems, air data computers, radar altimeters, radios, and GPS sensors. For each type of equipment, a set of standard parameters is defined, which is common across all manufacturers and models. For example, any air data computer will provide the barometric altitude of the aircraft as label 203. This allows some degree of interchangeability of parts, as all air data computers behave, for the most part, in the same way. There are only a limited number of labels, though, and so label 203 may have some completely different meaning if sent by a GPS sensor, for example. Very commonly needed aircraft parameters, however, use the same label regardless of source. Also, as with any specification, each manufacturer has slight differences from the formal specification, such as by providing extra data above and beyond the specification, leaving out some data recommended by the specification, or other various changes.

## Protection from interference

Avionics systems must meet environmental requirements, usually stated as RTCA DO-160 environmental categories. ARINC 429 employs several physical, electrical, and protocol techniques to minimize electromagnetic interference with on-board radios and other equipment, for example via other transmission cables.

Its cabling is a shielded 78 Ω twisted-pair. ARINC signaling defines a 10 Vp differential between the Data A and Data B levels within the bipolar transmission (i.e. 5 V on Data A and -5 V on Data B would constitute a valid driving signal), and the specification defines acceptable voltage rise and fall times.

ARINC 429's data encoding uses a complementary differential bipolar return-to-zero (BPRZ) transmission waveform, further reducing EMI emissions from the cable itself.

## Development tools

When developing and/or troubleshooting the ARINC 429 bus, examination of hardware signals can be very important to find problems. A protocol analyzer is useful to collect, analyze, decode and store signals.
