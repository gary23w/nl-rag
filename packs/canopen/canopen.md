---
title: "CANopen"
source: https://en.wikipedia.org/wiki/CANopen
domain: canopen
license: CC-BY-SA-4.0
tags: canopen protocol, canopen fieldbus, can bus higher-layer, embedded device network
fetched: 2026-07-02
---

# CANopen

**CANopen** is a communication protocol stack and device profile specification for embedded systems used in automation. In terms of the OSI model, CANopen implements the layers above and including the network layer. The CANopen standard consists of an addressing scheme, several small communication protocols and an application layer defined by a device profile. The communication protocols have support for network management, device monitoring and communication between nodes, including a simple transport layer for message segmentation/desegmentation. The lower level protocol implementing the data link and physical layers is usually Controller Area Network (CAN), although devices using some other means of communication (such as Ethernet Powerlink, EtherCAT) can also implement the CANopen device profile.

The basic CANopen device and communication profiles are given in the CiA 301 specification released by CAN in Automation. Profiles for more specialized devices are built on top of this basic profile, and are specified in numerous other standards released by CAN in Automation, such as CiA 401 for I/O-modules and CiA 402 for motion control.

## Device model

Every CANopen device has to implement certain standard features in its controlling software.

- A **communication unit** implements the protocols for messaging with the other nodes in the network.
- Starting and resetting the device is controlled via a state machine. It must contain the states Initialization, Pre-operational, Operational and Stopped. The transitions between states are made by issuing a network management (NMT) communication object to the device.
- The **object dictionary** is an array of variables with a 16-bit index. Additionally, each variable can have an 8-bit subindex. The variables can be used to configure the device and reflect its environment, i.e. contain measurement data.
- The **application** part of the device actually performs the desired function of the device, after the state machine is set to the operational state. The application is configured by variables in the object dictionary and the data are sent and received through the communication layer.

### Object dictionary

CANopen devices must have an object dictionary, which is used for configuration and communication with the device. An entry in the object dictionary is defined by:

- **Index**, the 16-bit address of the object in the dictionary
- **Object name** (Object Type/Size), a symbolic type of the object in the entry, such as an array, record, or simple variable
- **Name**, a string describing the entry
- **Type**, gives the datatype of the variable (or the datatype of all variables of an array)
- **Attribute**, which gives information on the access rights for this entry, this can be read/write, read-only or write-only
- The **Mandatory/Optional** field (M/O) defines whether a device conforming to the device specification has to implement this object or not

The basic datatypes for object dictionary values such as booleans, integers and floats are defined in the standard (their size in bits is optionally stored in the related type definition, index range 0x0001–0x001F), as well as composite datatypes such as strings, arrays and records (defined in index range 0x0040–0x025F). The composite datatypes can be subindexed with an 8-bit index; the value in subindex 0 of an array or record indicates the number of elements in the data structure, and is of type UNSIGNED8.

For example, the device communication parameters, standardized in the basic device profile CiA 301 are mapped in the index range 0x1000–0x1FFF ("communication profile area"). The first few entries in this area are as follows:

| Index | Object name | Name | Type | Attribute | M/O |
|---|---|---|---|---|---|
| 0x1000 | VAR | device type | UNSIGNED32 | ro | M |
| 0x1001 | VAR | error register | UNSIGNED8 | ro | M |
| ... |   |   |   |   |   |
| 0x1008 | VAR | manufacturer device name | Vis-String | const | O |
| ... |   |   |   |   |   |

Given suitable tools, the content of the object dictionary of a device, based on an electronic data sheet (EDS), can be customized to a device configuration file (DCF) to integrate the device into a specific CANopen network. According to CiA 306, the format of the EDS-file is the INI file format. There is an upcoming XML-style format, that is described in CiA 311.

## Communication

### Communication objects

CAN bus, the data link layer of CANopen, can only transmit short packages consisting of an 11-bit id, a remote transmission request (RTR) bit and 0 to 8 bytes of data. The CANopen standard divides the 11-bit CAN frame id into a 4-bit function code and 7-bit CANopen node ID. This limits the number of devices in a CANopen network to 127 (0 being reserved for broadcast). An extension to the CAN bus standard (CAN 2.0 B) allows extended frame ids of 29 bits, but in practice CANopen networks big enough to need the extended id range are rarely seen.

In CANopen the 11-bit id of a CAN-frame is known as communication object identifier, or COB-ID. In case of a transmission collision, the bus arbitration used in the CAN bus allows the frame with the smallest id to be transmitted first and without a delay. Using a low code number for time critical functions ensures the lowest possible delay.

Contents of a CANopen frame:

|   | COB-ID | RTR | Data length | Data |
|---|---|---|---|---|
| Length | 11 bits | 1 bit | 4 bits | 0-8 bytes |

The data frame with an 11-bit identifier is also called "base frame format".

The default CAN-ID mapping sorts frames by attributing a function code (NMT, SYNC, EMCY, PDO, SDO...) to the first 4 bits, so that critical functions are given priority. This mapping can however be customized for special purposes (except for NMT and SDO, required for basic communication).

|   | Function code | Node ID |
|---|---|---|
| Length | 4 bits | 7 bits |

The standard reserves certain CAN-IDs to network management and SDO transfers. Some function codes and CAN-IDs have to be mapped to standard functionality after device initialization, but can be configured for other uses later.

#### Predefined Connection Set

For simple network structures, CANopen supports a predefined allocation of message identifiers.

The transmit and receive directions are from the device's point of view. So a query to a device on the network would send a 0x600+nodeid and get back a 0x580+nodeid.

| Communication object | COB-ID(s) hex | Slave nodes | Specification |
|---|---|---|---|
| NMT node control | 000 | Receive only | CiA 301 |
| Global failsafe command | 001 | ? | CiA 304 |
| Flying master | 071 to 076 | ? | CiA 302-2 |
| Indicate active interface | 07F | ? | CiA 302-6 |
| Sync | 080 | Receive only | CiA 301 |
| Emergency | 080 + NodeID | Transmit | CiA 301 |
| TimeStamp | 100 | Receive only | CiA 301 |
| Safety-relevant data objects | 101 to 180 | ? | CiA 304 |
| PDO | 180 + NodeID 200 + NodeID 280 + NodeID 300 + NodeID 380 + NodeID 400 + NodeID 480 + NodeID 500 + NodeID | 1. Transmit PDO 1. Receive PDO 2. Transmit PDO 2. Receive PDO 3. Transmit PDO 3. Receive PDO 4. Transmit PDO 4. Receive PDO | CiA 301 |
| SDO | 580 + NodeID 600 + NodeID | Transmit Receive | CiA 301 |
| Dynamic SDO request | 6E0 | ? | CiA 302-5 |
| Node claiming procedure | 6E1 to 6E3 | ? | CiA 416-1 |
| Node claiming procedure | 6F0 to 6FF | ? | CiA 416-1 |
| NMT node monitoring (node guarding/heartbeat) | 700 + NodeID | Transmit | CiA 301 |
| LSS | 7E4 7E5 | Transmit Receive | CiA 305 |

### Communication models

Different kinds of communication models are used in the messaging between CANopen nodes.

In a **master/slave** relationship, one CANopen node is designated as the master, which sends or requests data from the slaves. The NMT protocol is an example of a master/slave communication model.

A **client/server** relationship is implemented in the SDO protocol, where the SDO client sends data (the object dictionary index and subindex) to an SDO server, which replies with one or more SDO packages containing the requested data (the contents of the object dictionary at the given index).

A **producer/consumer** model is used in the Heartbeat and Node Guarding protocols. In the *push-model* of producer/consumer, the producer sends data to the consumer without a specific request, whereas in the *pull model*, the consumer has to request the data from the producer.

### Protocols

#### Network management (NMT) protocols

The NMT protocols are used to issue state machine change commands (e.g. to start and stop the devices), detect remote device bootups and error conditions.

The **Module control protocol** is used by the NMT master to change the state of the devices. The CAN-frame COB-ID of this protocol is always 0, meaning that it has a function code 0 and node ID 0, which means that every node in the network will process this message. The actual node ID, to which the command is meant to, is given in the data part of the message (at the second byte). This can also be 0, meaning that all the devices on the bus should go to the indicated state.

| COB-ID | Data Byte 0 | Data Byte 1 |
|---|---|---|
| 0x000 | Requested state | Addressed node |

| NMT command code | Meaning |
|---|---|
| 0x01 | Go to 'operational' |
| 0x02 | Go to 'stopped' |
| 0x80 | Go to 'pre-operational' |
| 0x81 | Go to 'reset node' |
| 0x82 | Go to 'reset communication' |

The **Heartbeat protocol** is used to monitor the nodes in the network and verify that they are alive. A heartbeat producer (usually a slave device) periodically sends a message with the binary function code of 1110 and its node ID (COB-ID19 = 0x700 + node ID). The data part of the frame contains a byte indicating the node status. The heartbeat consumer reads these messages. If the messages fail to arrive within a certain time limit (defined in the object dictionary of the devices) the consumer can take action to, for example, reset the device or indicate an error. The frame format is:

| COB-ID | Data Byte 0 |
|---|---|
| 0x700 + node ID | State |

| NMT state code | Represented state |
|---|---|
| 0x00 | Boot up (Initialising) |
| 0x04 | Stopped |
| 0x05 | Operational |
| 0x7f | Pre-operational |

CANopen devices are required to make the transition from the state Initializing to Pre-operational automatically during bootup. When this transition is made, a single heartbeat message is sent to the bus. This is the **bootup protocol**.

A response/reply-style (pull model) protocol, called node guarding, exists for slave monitoring.

#### Service Data Object (SDO) protocol

The SDO protocol is used for setting and for reading values from the object dictionary of a remote device. The device whose object dictionary is accessed is the SDO server and the device accessing the remote device is the SDO client. The communication is always initiated by the SDO client. In CANopen terminology, communication is viewed from the SDO server, so that a read from an object dictionary results in an SDO upload and a write to a dictionary entry is an SDO download.

Because the object dictionary values can be larger than the eight bytes limit of a CAN frame, the SDO protocol implements segmentation and desegmentation of longer messages. Actually, there are two of these protocols: SDO download/upload and SDO Block download/upload. The SDO block transfer is a newer addition to standard, which allows large amounts of data to be transferred with slightly less protocol overhead.

The COB-IDs of the respective SDO transfer messages from client to server and server to client can be set in the object dictionary. Up to 128 SDO servers can be set up in the object dictionary at addresses 0x1200 - 0x127F. Similarly, the SDO client connections of the device can be configured with variables at 0x1280 - 0x12FF. However the *pre-defined connection set* defines an SDO channel which can be used even just after bootup (in the Pre-operational state) to configure the device. The COB-IDs of this channel are 0x600 + node ID for receiving and 0x580 + node ID for transmitting.

To initiate a download, the SDO client sends the following data in a CAN message with the 'receive' COB-ID of the SDO channel.

Byte Nr:

Byte 0

Byte 1-2

Byte 3

Byte 4-7

Length:

3 bits

1 bit

2 bits

1 bit

1 bit

2 bytes

1 byte

4 bytes

Meaning:

ccs=1

reserved(=0)

n

e

s

index

subindex

data

- **ccs** is the client command specifier of the SDO transfer, this is 0 for SDO segment download, 1 for initiating download, 2 for initiating upload, 3 for SDO segment upload, 4 for aborting an SDO transfer, 5 for SDO block upload and 6 for SDO block download
- **n** is the number of bytes in the data part of the message which do not contain data, only valid if e and s are set
- **e**, if set, indicates an expedited transfer, i.e. all data exchanged are contained within the message. If this bit is cleared then the message is a segmented transfer where the data does not fit into one message and multiple messages are used.
- **s**, if set, indicates that the data size is specified in n (if e is set) or in the data part of the message
- **index** is the object dictionary index of the data to be accessed, encoded in little endian
- **subindex** is the subindex of the object dictionary variable
- **data** contains the data to be uploaded in the case of an expedited transfer (e is set), or the size of the data to be uploaded (s is set, e is not set), often encoded in little endian

#### Process Data Object (PDO) protocol

The Process Data Object protocol is used to process real time data among various nodes. You can transfer up to 8 bytes (64 bits) of data per one PDO either from or to the device. One PDO can contain multiple object dictionary entries and the objects within one PDO are configurable using the mapping and parameter object dictionary entries.

There are two kinds of PDOs: transmit and receive PDOs (TPDO and RPDO). The former is for data coming from the device (the device is a data producer) and the latter is for data going to the device (the device is a data consumer); that is, with RPDO you can send data to the device and with TPDO you can read data from the device. In the pre-defined connection set there are identifiers for four TPDOs and four RPDOs available. With configuration, 512 PDOs are possible.

PDOs can be sent synchronously or asynchronously. Synchronous PDOs are sent after the SYNC message whereas asynchronous messages are sent after internal or external trigger. For example, you can make a request to a device to transmit TPDO that contains data you need by sending an empty TPDO with the RTR flag (if the device is configured to accept TPDO requests).

With RPDOs you can, for example, start two devices simultaneously. You only need to map the same RPDO into two or more different devices and make sure those RPDOs are mapped with the same COB-ID.

#### Synchronization Object (SYNC) protocol

The Sync-Producer provides the synchronization-signal for the Sync-Consumer. When the Sync-Consumer receive the signal they start carrying out their synchronous tasks.

In general, the fixing of the transmission time of synchronous PDO messages coupled with the periodicity of transmission of the Sync Object guarantees that sensor devices may arrange to sample process variables and that actuator devices may apply their actuation in a coordinated fashion.

The identifier of the Sync Object is available at index 1005h.

#### Time Stamp Object (TIME) protocol

Usually the Time-Stamp object represents a time as a 6-byte field: a count of milliseconds after midnight (at most 27 bits, stored in a 32-bit field), and an unsigned 16-bit number of days since January 1, 1984. (This will overflow on 7 June 2163.)

Some time critical applications especially in large networks with reduced transmission rates require very accurate synchronization; it may be necessary to synchronize the local clocks with an accuracy in the order of microseconds. This is achieved by using the optional high resolution synchronization protocol which employs a special form of timestamp message to adjust the inevitable drift of the local clocks.

The high-resolution timestamp is encoded as unsigned32 with a resolution of 1 microsecond which means that the time counter restarts every 72 minutes. It is configured by mapping the high resolution time-stamp (object 1013h) into a PDO.

#### Emergency Object (EMCY) protocol

Emergency messages are triggered by the occurrence of a device internal fatal error situation and are transmitted from the concerned application device to the other devices with high priority. This makes them suitable for interrupt type error alerts. An Emergency Telegram may be sent only once per ‘error event’, i.e. the emergency messages must not be repeated. As long as no new errors occur on a device no further emergency message must be sent. By means of CANopen Communication Profile defined emergency error codes, the error register and device specific additional information are specified in the device profiles.

### Initialization

Sample trace of communications between a master and two pressure transducer slaves configured for id 1 and node ID 2.

| CAN ID | DATA LENGTH | DATA | Description |
|---|---|---|---|
| 0x0 | 2 | 01 00 | Master puts all devices on the bus into operational mode |
| 0x80 | 0 |   | Master sends a SYNC message, which triggers devices to send data |
| 0x181 | 4 | CD 82 01 00 | Node at ID 1 (CID-0x180), reading pressure of 0x0182CD (99021) pascals |
| 0x182 | 4 | E5 83 01 00 | Node at ID 2 (CID-0x180), reading pressure of 0x0183E5 (99301) pascals |

## Electronic Data Sheet

Electronic Data Sheet (EDS) is a file format, defined in CiA306, that describes the communication behaviour and the object dictionary entries of a device. This allows tools such as service tools, configuration tools, development tools, and others to handle the devices properly.

Those EDS files are mandatory for passing the CiA CANopen conformance test.

Since end of 2007 a new XML based format called XDD is defined in CiA311. XDD is conformant to ISO standard 15745.

## Glossary of CANopen terms

- **PDO**: Process Data Object - Inputs and outputs. Values of type rotational speed, voltage, frequency, electric current, etc.
- **SDO**: Service Data Object - Configuration settings, possibly node ID, baud rate, offset, gain, etc.
- **COB-ID**: Communication object identifier
- **CAN ID**: CAN Identifier. This is the 11-bit CAN message identifier which is at the beginning of every CAN message on the bus.
- **EDS**: Electronic Data Sheet. This is an INI style or XML style formatted file.
- **DCF**: Device Configuration File. This is a modified EDS file with settings for node ID and baud rate.
