---
title: "Modbus"
source: https://en.wikipedia.org/wiki/Modbus
domain: modbus-protocol
license: CC-BY-SA-4.0
tags: modbus protocol, modbus rtu, modbus tcp, serial fieldbus
fetched: 2026-07-02
---

# Modbus

**Modbus** is a fieldbus, an industrial computer networking protocol. It was originally designed for use with programmable logic controllers (PLCs), but has become a *de facto* standard communication protocol for communication between industrial electronic devices in a wide range of buses and networks.

Modbus is popular in industrial environments because it is openly published and royalty-free. It was developed for industrial applications, is relatively easy to deploy and maintain compared to other standards, and places few restrictions on the format of the data to be transmitted.

The Modbus protocol uses serial communication lines, Ethernet, or the Internet protocol suite as a transport layer. Modbus supports communication to and from multiple devices connected to the same cable or Ethernet network. For example, there can be a device that measures temperature and another device to measure humidity connected to the same cable, both communicating measurements to the same computer, via Modbus.

Modbus is often used to connect a plant/system supervisory computer with a remote terminal unit (RTU) in supervisory control and data acquisition (SCADA) systems. Many of the data types are named from industrial control of factory devices, such as ladder logic because of its use in driving relays: a single-bit physical output is called a *coil*, and a single-bit physical input is called a *discrete input* or a *contact*.

It was originally published in 1979 by Modicon (bought by Schneider Electric in 1997). In 2004, they transferred the rights to the Modbus Organization which is a trade association of users and suppliers of Modbus-compliant devices that advocates for the continued use of the technology.

## Protocol description

Modbus standards or buses include:

- TCP/IP over Ethernet
- Asynchronous serial communication in a wide range of standards, technologies: EIA/TIA-232-E, EIA-422, EIA/TIA-485-A, fiber, radio frequency,...
- MODBUS PLUS, a high speed token passing network.

To support Modbus communication on a network, many modems and gateways incorporate proprietary designs (refer to the diagram: *Architecture of a network for Modbus communication*). Implementations may deploy either wireline or wireless communication, such as in the ISM radio band, and even Short Message Service (SMS) or General Packet Radio Service (GPRS).

### PDU and ADU

Modbus defines a *client* which is an entity that initiates a transaction to request any specific task from its *request receiver*. The client's "request receiver", which the client has initiated the transaction with, is then called the *server*. For example, when a microcontroller connects to a sensor to read its data by Modbus on a wired network, e.g RS485 bus, the MCU in this context is the client and the sensor is the server. In former terminology, the client was named master and the server named slave.

Modbus defines a protocol data unit (PDU) independently to its lower layer protocols in its protocol stack. Mapping MODBUS protocol on specific buses or networks requires some additional fields, defined as the application data unit (ADU). The ADU is formed by a *client* inside a Modbus network when the client initiates a transaction. Contents are:

- PDU = Function code + data
- ADU = Additional address + PDU + error check

The ADU is officially called a *Modbus frame* by the Modbus Organization, although *frame* is used as the data unit in the data-link layer in the OSI and TCP/IP model (while Modbus is an application layer protocol).

PDU max size is 253 bytes. ADU max size on RS232/RS485 network is 256 bytes, and with TCP is 260 bytes.

For data encoding, Modbus uses a big-endian representation for addresses and data fields. Thus, for a 16-bit value, the most significant byte is sent first. For example, when a 16-bit register has value 0x1234, byte 0x12 is sent before byte 0x34.

*Function code* is 1 byte which gives the code of the function to execute. Function codes are integer values, ranging from 1 to 255, and the range from 128 to 255 is for exception responses.

The data field of the PDU has the address from 0 to 65535 (not to be confused with the address of the Additional address field of ADU). The data field of the PDU can be empty, and then has a size of 0. In this case, the server will not request any information and the function code defines the function to be executed. If there is no error during the execution process, the data field of the ADU response from server to client will include the data requested, i.e. the data the client previously received. If there is any error, the server will respond with an exception code.

### Modbus transaction and PDU

A Modbus transaction between client and server includes:

- Step 1: Client initiates a request with PDU = Function code + data request
- Step 2: Server receives the request from client. Server will then read/parse the function code, get the address of the data field of the PDU, then get this data field value and finally perform the action based on the function code. If there is no error during those steps, the server will respond with PDU = Function code + data response. As long as there is no error during those steps, the server's responding function code will also be the function code sent from the client. If there is any error during those steps, the server will respond with PDU = Exception Function code + Exception code (Reference to PDU mb_excep_rsp_pdu defined below).
- Step 3: Client receives the response and ends the transaction.

Based on that, Modbus defines 3 PDU types:

- MODBUS Request PDU, mb_req_pdu
- MODBUS Response PDU, mb_rsp_pdu
- MODBUS Exception Response PDU, mb_excep_rsp_pdu

mb_req_pdu = Function code (1 byte) + request data (n bytes)

request data

field's size depends on the function code and usually includes values like variable values, data offset, and sub-function codes.

mb_rsp_pdu = Function code (1 byte) + response data (n bytes)

As in mb_req_pdu,

response data

field's size depends on the function code and usually includes values like variable values, data offset, and sub-function codes.

mb_excep_rsp_pdu = Exception Function code (1 byte) + exception code (1 byte)

Exception Function code

= Function code (1 byte) + 0x80.

Exception Function code

is equal to the Function code, except that its MSB is set to 1.

Exception code (1 byte) of mb_excep_rsp_pdu is defined in the

MODBUS Exception Codes

table.

### Modbus data model

Modbus defines its data model based on a series of tables of four primary types:

| Primary tables | Access | Size | Features |
|---|---|---|---|
| Discrete input | R | 1 bit (0–1) | Read on/off value |
| Coil (discrete output) | R/W | 1 bit (0–1) | Read/Write on/off value |
| Input register | R | 16 bit words (0–65,535) | Read measurements and statuses |
| Holding register | R/W | 16 bit words (0–65,535) | Read/Write configuration values |

For each of the primary tables, the protocol allows individual selection of 65536 data items, and the operations of read or write of those items are designed to span multiple consecutive data items up to a data size limit which is dependent on the transaction function code.

## Function code

Modbus defines three types of function codes: Public, User-Defined and Reserved.

### Public function codes

| Function type | Function name | Function code | Comment |   |   |
|---|---|---|---|---|---|
| Data Access | Bit access | Physical Discrete Inputs | Read Discrete Inputs | 2 |   |
| Internal Bits or Physical Coils | Read Coils | 1 |   |   |   |
| Write Single Coil | 5 |   |   |   |   |
| Write Multiple Coils | 15 |   |   |   |   |
| 16-bit access | Physical Input Registers | Read Input Registers | 4 |   |   |
| Internal Registers or Physical Output Registers | Read Multiple Holding Registers | 3 |   |   |   |
| Write Single Holding Register | 6 |   |   |   |   |
| Write Multiple Holding Registers | 16 | > 1 |   |   |   |
| Read/Write Multiple Registers | 23 |   |   |   |   |
| Mask Write Register | 22 |   |   |   |   |
| Read FIFO Queue | 24 |   |   |   |   |
| File Record Access | Read File Record | 20 |   |   |   |
| Write File Record | 21 |   |   |   |   |
| Diagnostics | Read Exception Status | 7 | serial only |   |   |
| Diagnostic | 8 | serial only |   |   |   |
| Get Com Event Counter | 11 | serial only |   |   |   |
| Get Com Event Log | 12 | serial only |   |   |   |
| Report Server ID | 17 | serial only |   |   |   |
| Read Device Identification | 43 |   |   |   |   |
| Other | Encapsulated Interface Transport | 43 |   |   |   |

Note: Some sources use terminology that differs from the standard; for example *Force Single Coil* instead of *Write Single Coil*.

#### Function code 01 (read coils) as an example of public function code

Function code 01 (read coils) allows reading the state from 1 to 2000 coils of a remote device. mb_req_pdu (request PDU) will then have 2 bytes to indicate the address of the first coil to read (from 0x0000 to 0xFFFF), and 2 bytes to indicate the number of coils to read. mb_req_pdu defines coil address by index 0, i.e the first coil has address 0x0. On a successful execution, mb_rsp_pdu will return one byte to note the function code (0x01), followed by one byte to indicate the number of data bytes it is returning (n), which will be the number of coils requested by mb_req_pdu, divided by 8 bits per byte, and rounded up. The remainder of the response will be the specified number (n) of data bytes. That is, the mb_req_pdu and mb_rsp_pdu of function code 01 will take the following form:

mb_req_pdu:

- Function code: 0x01 (1 byte)
- Starting Address (1st coil address to read): From 0x0000 to 0xFFFF (2 bytes)
- Quantity of coils to read: Range from 1 to 2000 (0x7D0) (2 bytes)

mb_rsp_pdu:

- Function code: 0x01 (1 byte)
- Byte count: 1 byte (n=quantity of coils/8, rounded up)
- Coil Status: n bytes

For instance, mb_req_pdu and mb_rsp_pdu to read coils status from 20-38 will be:

mb_req_pdu:

- Function code: 0x01
- Starting Address High byte: 0x00
- Starting Address Low byte: 0x13
- Quantity of Outputs High byte: 0x00
- Quantity of Outputs Low byte: 0x13

Starting Address (2 bytes) is 0x0013, (or 19 in decimal) which is the 20th coil.

Quantity of Outputs (2 bytes) is 0x0013, (or 19 in decimal) which corresponds to 19 values of status of coils 20th to 38th.

mb_rsp_pdu:

- Function code: 0x01
- Byte Count: 0x03
- Outputs status 27-20: 0xCD
- Outputs status 35-28: 0x6B
- Outputs status 38-36: 0x05

As 19 coils (20-38) are required, 3 bytes is used to indicate the coil's state. So that Byte Count is 0x03. States of coil from 20 to 27 is 0xCD, which is 1100 1101 in binary. So coil 27 is MSb, and coil 20 is LSb. Same for coil 28 to 35. With coil from 36 to 38, the state will be 0x05, which is 0000 0101. Coil 38 state is the 3rd bit (count from the right), i.e 1, coil 37 is 0, and coil 36 state is LSb bit, i.e. 1. 5 left bits are all 0.

### User-defined function codes

User-Defined Function Codes are function codes defined by users. Modbus gives two range of values for user-defined function codes: 65 to 72 and 100 to 110. Obviously, user-defined function codes are not unique.

### Reserved function codes

Reserved Function Codes are function codes used by some companies for legacy product and are not available for public use.

## Exception responses

When a client sends a request to a server, there can be four possible events for that request:

- If server receives the request and execute successfully, server will return a normal response.
- If server cannot receive the request as having communication channel error, server will not respond anything to the client. Client will then have the timeout request error.
- If server receives the request and detect an error on the communication channel (e.g parity, LRC, CRC), server will not response anything to the client. Client will then have the timeout request error.
- If server receives the request and is unable to execute it (e.g client requests to read a non-existent register), server will return an *exception response* to client to indicate the nature of the error.

Exception response message includes two other fields when compared to a normal response message:

- Function Code: Function code's MSB bit of Exception is 1. This will make this function code 0x80 higher than then request message function code.
- Data: Server returns the exception code inside the Data field. This field defines the nature of the error.

All Modbus exception code:

| Code | Text | Details |
|---|---|---|
| 1 | Illegal Function | Function code received in the query is not recognized or allowed by server |
| 2 | Illegal Data Address | Data address of some or all the required entities are not allowed or do not exist in server |
| 3 | Illegal Data Value | Value is not accepted by server |
| 4 | Server Device Failure | Unrecoverable error occurred while server was attempting to perform requested action |
| 5 | Acknowledge | Server has accepted request and is processing it, but a long duration of time is required. This response is returned to prevent a timeout error from occurring in the client. client can next issue a *Poll Program Complete* message to determine whether processing is completed |
| 6 | Server Device Busy | Server is engaged in processing a long-duration command; client should retry later |
| 7 | Negative Acknowledge | Server cannot perform the programming functions; client should request diagnostic or error information from server |
| 8 | Memory Parity Error | Server detected a parity error in memory; client can retry the request |
| 10 | Gateway Path Unavailable | Specialized for Modbus gateways: indicates a misconfigured gateway |
| 11 | Gateway Target Device Failed to Respond | Specialized for Modbus gateways: sent when server fails to respond |

## Modbus over Serial Line protocol

Modbus standard also defines Modbus over Serial Line, a protocol over the data link layer of the OSI model for the Modbus application layer protocol to be communicated over a serial bus. Modbus Serial Line protocol is a master-slave protocol which supports one master and multiple slaves in the serial bus. With Modbus protocol on the application layer, client/server model is used for the devices on the communication channel. With Modbus over Serial Line, *client*'s role is implemented by *master*, and the *server*'s role is implemented by *slave*.

The organization's naming convention inverts the common usage of having multiple clients and only one server. To avoid this confusion, the RS-485 transport layer uses the terms "node" or "device" instead of "server", and the "client" is not a "node".

> The (Modbus Organization) is using "client-server" to describe Modbus communications, characterized by communication between [client device (s), which initiates communication and makes requests of server device(s), which process requests and return an appropriate response (or error message).

A serial bus for Modbus over Serial Line can have a maximum of 247 slaves communicating with one master. Those slaves have a unique address ranging from 1 to 247 (01hex to F7hex). The addresses from 248 to 255 (F8hex … FFhex) are reserved and must not be used. The master doesn't need to have an address. The communication process is initiated by the master, as only it can initiate a Modbus transaction. A slave will never transmit any data or perform any action without a request from the master, and slaves cannot communicate with each other.

In Modbus over Serial Line, the master initiates requests to the slaves in *unicast* or *broadcast* modes. In *unicast mode*, the master will initiate a request to a single slave with a specific address. Upon receiving and finishing the request, the slave will respond with a message to the master. In this mode, a Modbus transaction includes two messages: one request from the master and one reply from the slave. Each slave must have a unique address (from 1 to 247) to be addressed independently for the communication. In *broadcast mode*, the master can send a request to all the slaves, using the broadcast address 0, which is the address reserved for broadcast exchanges (and not the master address). Slaves must accept broadcast exchanges but must not respond. The mapping of PDU of Modbus to the serial bus of Modbus over Serial Line protocol results in Modbus Serial Line PDU.

Modbus Serial Line PDU = Address + PDU + CRC (or LRC)

With PDU = Function code + data

- Address is slave address
- PDU is defined identically to the PDU of Modbus Application protocol
- The Error check field with CRC/LRC: The error check methods depend on the protocol versions of the MODBUS over Serial Line, whether it is *Modbus RTU* or *Modbus ASCII*.

On the physical layer, MODBUS over Serial Line performs its communication on bit by RS485 or RS232, with TIA/EIA-485 Two-Wire interface as the most popular way. RS485 Four-Wire interface is also used. TIA/EIA-232-E (RS232) can also be used but is limited to point-to-point short-range communication. MODBUS over Serial Line has two transmission modes *RTU* and *ASCII* which are corresponded to two versions of the protocol, known as *Modbus RTU* and *Modbus ASCII*.

### Modbus RTU

Modbus RTU (Remote Terminal Unit), which is the most common implementation available for Modbus, makes use of a compact, binary representation of the data for protocol communication. The RTU format follows the commands/data with a cyclic redundancy check checksum as an error check mechanism to ensure the reliability of data. A Modbus RTU message must be transmitted continuously without inter-character hesitations. Modbus messages are framed (separated) by idle (silent) periods. Each byte (8 bits) of data is sent as 11 bits:

- 1 start bit
- 8 bit data/message, least significant bit sent first
- 1 bit parity
- 1 stop bit

The default is even parity, while odd or no parity may be implemented as additional options.

A Modbus RTU frame then will be:

| Slave Address | Modbus PDU | CRC |   |
|---|---|---|---|
| Function Code | Data |   |   |
| 1 byte | 1 byte | 0 – 252 bytes | 2 bytes: 1 CRC low byte and 1 CRC high byte |

The CRC calculation is widely known as CRC-16-MODBUS, whose polynomial is *x*16 + *x*15 + *x*2 + 1 (normal hexadecimal algebraic polynomial being `8005` and reversed `A001`).

Example of a Modbus RTU frame in hexadecimal: `01 04 02 FF FF B8 80` (CRC-16-MODBUS calculation for the 5 bytes from `01` to `FF` gives `80B8`, which is transmitted least significant byte first).

To ensure frame integrity during the transmission, the time interval between two frames must be at least the transmission time of 3.5 characters, and the time interval between two consecutive characters must be no more than the transmission time of 1.5 characters. For example, with the default data rate of 19200 bit/s, the transmission times of 3.5 (t3.5) and 1.5 (t1.5) 11-bit characters are:

$t3.5=3.5\cdot \left({\frac {11\cdot 1000}{19200}}\right)=2.005\,\mathrm {ms}$

$t1.5=1.5\cdot \left({\frac {11\cdot 10^{6}}{19200}}\right)=859.375\,\mathrm {\mu s}$

For higher data rates, Modbus RTU recommends to use the fixed values 750 μs for t1.5 and 1.750 ms for t3.5.

### Modbus ASCII

Modbus ASCII makes use of ASCII characters (chars) for protocol communication. The ASCII format uses a longitudinal redundancy check checksum. Modbus ASCII messages are framed by a leading colon (":", ASCII value 3A16) and trailing newline (CR/LF, ASCII values 0D16 and 0A16). Modbus ASCII frame do not need to be sent in bursts like Modbus RTU, a delay up to 1 second is permitted between each character transmission by default. Each ASCII character is sent as 10 bits:

- 1 start bit
- 7 bit ASCII character, least significant bit sent first
- 1 bit parity
- 1 stop bit

The default is even parity, while odd or no parity may be implemented as additional options.

A Modbus ASCII frame includes:

| Start | Slave Address | Modbus PDU | LRC | End |   |
|---|---|---|---|---|---|
| Function Code | Data |   |   |   |   |
| 1 char (always ":") | 2 chars | 2 chars | 0-252 x 2 chars | 2 chars | 2 chars (always CR/LF) |

Address, Function, Data, and LRC are ASCII hexadecimal encoded values, whereby each byte (8 bits) of information is encoded as two human-readable ASCII characters from the ranges 0–9 and A–F. For example, a byte value of 122 (11110102 or 7A16) is encoded as two ASCII characters, "7" and "A", and transmitted as two bytes, `55` (3716, ASCII value for "7") and `65` (4116, ASCII value for "A").

LRC is calculated as the sum of 8-bit values (excluding the start and end characters), negated (two's complement) and encoded as an 8-bit value. For example, if Address, Function, and Data are 247, 3, 19, 137, 0, and 10, the two's complement of their sum (416) is −416; this trimmed to 8 bits is 96 (256 × 2 − 416 = 6016), giving the following 17 ASCII character frame: `:F7031389000A60␍␊`. LRC is specified for use only as a checksum: because it is calculated on the encoded data rather than the transmitted characters, its 'longitudinal' characteristic is not available for use with parity bits to locate single-bit errors.

## Modbus messaging on TCP/IP

### Modbus TCP

*Modbus TCP* or *Modbus TCP/IP* is a Modbus variant used for communications over TCP/IP networks, connecting over port 502. It does not require a checksum calculation, as lower layers already provide checksum protection.

Modbus TCP nomenclature is the same as for the Modbus over Serial line protocol, as any device which send out a Modbus command, is the 'client' and the response comes from a 'server'.

The ADU for Modbus TCP is officially called *Modbus TCP/IP ADU* by the Modbus organization and is also called *Modbus TCP frame* by other parties.

MODBUS TCP/IP ADU = MODBUS Application Protocol Header + Function code + Data

MODBUS Application Protocol header - is the dedicated header used on TCP/IP to identify the MODBUS Application Data Unit.

The MODBUS Application Protocol Header contains the following fields:

| Name | Length (bytes) | Function |
|---|---|---|
| Transaction identifier | 2 | For synchronization between messages of server and client |
| Protocol identifier | 2 | 0 for Modbus/TCP |
| Length field | 2 | Number of remaining bytes in this frame |
| Unit identifier | 1 | Server address (255 if not used), treated like slave address in Modbus over Serial line |

*Unit identifier* is used with Modbus TCP devices that are composites of several Modbus devices, e.g. Modbus TCP to Modbus RTU gateways. In such a case, the unit identifier is the Server Address of the device behind the gateway.

A MODBUS TCP/IP ADU/Modbus TCP frame format then will be:

| MODBUS Application Protocol Header | Modbus PDU |   |   |   |   |
|---|---|---|---|---|---|
| Transaction identifier | Protocol identifier | Length | Unit identifier | Function code | Data |
| 2 bytes | 2 bytes | 2 bytes | 1 byte | 1 byte | n bytes |

#### Example of a Modbus TCP/IP ADU/Modbus TCP frame in hexadecimal

`12 34 00 00 00 06 01 03 00 01 00 01`

- `0x12` and `0x34` : With transaction ID = 0x1234 (2 bytes) as a "unique number" to be identified between the Modbus TCP client/server, the transaction ID High byte is 0x12 and transaction ID Low byte is 0x34
- `0x00` and `0x00` : Protocol identifier high byte and low byte
- `0x00` and `0x06` : Length high byte and low byte. The length is 6 bytes which includes: unit identifier (slave address) (1 byte), function code (1 byte), high byte of the register address to read (1 byte), low byte of the register address to read (1 byte) and data (2 bytes = high byte and low byte of the number of registers to read)
- `0x01` : Unit identifier (slave address)
- `0x03` : Function code (Read Multiple Holding Registers)
- `0x00` and `0x01` : high byte and low byte of the register address to read. The register address to read in this case is `0x0001`.
- `0x00` and `0x01` : high byte and low byte of the number of registers to read. The number of registers to read in this case is `0x0001`. (i.e 1 register)

### Other Modbus protocol versions over TCP/IP

- *Modbus over TCP/IP*, *Modbus over TCP*, or *Modbus RTU/IP* – a variant that differs from Modbus TCP in that a checksum is included in the payload, as with Modbus RTU.
- *Modbus over UDP* – Using Modbus over UDP on IP networks, which removes the overhead of TCP.

## Other Modbus protocol versions

Besides the widely used Modbus RTU, Modbus ASCII and Modbus TCP, there are many variants of Modbus protocols:

- *Modbus Plus* (*Modbus+*, *MB+*, or *MBP*) – Modbus Plus is proprietary to Schneider Electric, though it is unpublished rather than patented, and unlike the other variants, it supports peer-to-peer communications between multiple clients. Despite the name, Modbus Plus is not a variant of Modbus. It is a different protocol, involving token passing. It requires a dedicated co-processor to handle fast HDLC-like token rotation. It uses twisted pair at 1 Mbit/s and includes transformer isolation at each node, which makes it transition/edge-triggered instead of voltage/level-triggered. Special hardware is required to connect Modbus Plus to a computer, typically a card made for the ISA, PCI, or PCMCIA bus. Modbus Plus is normally implemented using a custom chipset available only to partners of Schneider.
- *Pemex Modbus* – an extension of standard Modbus with support for historical and flow data. It was designed for the Pemex oil and gas company for use in process control and never gained widespread adoption.
- *Enron Modbus* – another extension of standard Modbus developed by Enron with support for 32-bit integer and floating-point variables, and historical and flow data. Data types are mapped using standard addresses. The historical data serves to meet an American Petroleum Institute (API) industry standard for how data should be stored.

Data models and function calls are identical for the first four variants listed above; only the encapsulation is different. However the variants are not interoperable, nor are the frame formats.

### JBUS mapping

Another *de facto* protocol closely related to Modbus appeared later, and was defined by PLC maker April Automates, the result of a collaborative effort between French companies Renault Automation and Merlin Gerin et Cie in 1985: JBUS. Differences between Modbus and JBUS at that time (number of entities, server stations) are now irrelevant as this protocol almost disappeared with the April PLC series, which AEG Schneider Automation bought in 1994 and then made obsolete. However, the name JBUS has survived to some extent.

JBUS supports function codes 1, 2, 3, 4, 5, 6, 15, and 16 and thus all the entities described above, although numbering is different:

- Number and address coincide: entity #*x* has address *x* in the data frame.
- Consequently, entity number does not include the entity type. For example, holding register #40010 in Modbus will be holding register #9, at address 9 in JBUS.
- Number 0 (and thus address 0) is not supported. The server should not implement any real data at this number and address, and it can return a null value or throw an error when requested.

## Limitations

- Since Modbus was designed in the late 1970s to communicate to programmable logic controllers, the number of data types is limited to those understood by PLCs at the time. Large binary objects are not supported.
- No standard way exists for a node to find the description of a data object, for example, to learn that a register value represents a temperature between 30 and 175 degrees.
- Since Modbus is a client/server (formerly master/slave) protocol, there is no way for a field device to get data by the event handler mechanism (except over Ethernet TCP/IP, called open-mbus) as the client node must routinely poll each field device and look for changes in the data. This consumes bandwidth and network time in applications where bandwidth may be expensive, such as over a low-bit-rate radio link.
- Modbus is restricted to addressing 247 devices on one data link, which limits the number of field devices that may be connected to a parent station (again, Ethernet TCP/IP is an exception).
- Modbus protocol itself provides no security against unauthorized commands or interception of data.
