---
title: "Bluetooth Low Energy"
source: https://en.wikipedia.org/wiki/Bluetooth_Low_Energy
domain: bluetooth-mesh
license: CC-BY-SA-4.0
tags: bluetooth mesh, bluetooth low energy, managed flooding, iot mesh network
fetched: 2026-07-02
---

# Bluetooth Low Energy

**Bluetooth Low Energy** (**Bluetooth LE**, colloquially **BLE**, formerly marketed as **Bluetooth Smart**) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries. Compared to Classic Bluetooth, Bluetooth Low Energy is intended to provide considerably reduced power consumption and cost while maintaining a similar communication range.

BLE and Classic Bluetooth use different sets of radio frequencies, and although BLE is independent of classic Bluetooth and has no direct compatibility, Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) and BLE can coexist. The original specification was developed by Nokia in 2006 under the name Wibree, which was integrated into Bluetooth 4.0 in December 2009 as Bluetooth Low Energy.

Mobile operating systems including iOS, Android, Windows Phone and BlackBerry, as well as the desktop computer operating systems macOS, Linux, Windows 8, Windows 10 and Windows 11, natively support Bluetooth Low Energy.

## Compatibility

Bluetooth Low Energy is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.

Bluetooth Low Energy uses the same 2.4 GHz radio frequencies as classic Bluetooth, which allows dual-mode devices to share a single radio antenna, but uses a simpler modulation system.

## Branding

In 2011, the Bluetooth SIG announced the Bluetooth Smart logo so as to clarify compatibility between the new low-energy devices and other Bluetooth devices.

- Bluetooth Smart Ready indicates a dual-mode device compatible with both classic and low-energy peripherals.
- Bluetooth Smart indicates a low-energy–only device which requires either a Smart Ready or another Bluetooth Smart device in order to function.

With the May 2016 Bluetooth SIG branding information, the Bluetooth SIG began phasing out the Bluetooth Smart and Bluetooth Smart Ready logos and word marks and reverted to using the Bluetooth logo and word mark in a new blue color.

## Target market

The Bluetooth SIG identifies a number of markets for low-energy technology, particularly in the smart home, health, sport, and fitness sectors. Cited advantages include:

- low power requirements, operating for "months or years" on a button cell.
- small size and low cost.
- compatibility with a large installed base of mobile phones, tablets, and computers.

## History

In 2001, researchers at Nokia determined various scenarios that contemporary wireless technologies did not address. The company began developing a wireless technology adapted from the Bluetooth standard which would provide lower power usage and cost while minimizing its differences from Bluetooth technology. The results were published in 2004 using the name Bluetooth Low End Extension.

After further development with partners, in particular Logitech and within the European project MIMOSA, and actively promoted and supported by STMicroelectronics since its early stage, the technology was released to the public in October 2006 with the brand name Wibree. After negotiations with Bluetooth SIG members, an agreement was reached in June 2007 to include Wibree in a future Bluetooth specification as a Bluetooth ultra-low-power technology.

The technology was marketed as Bluetooth Smart and integration into version 4.0 of the Core Specification was completed in early 2010. The first smartphone to implement the 4.0 specification was the iPhone 4S, released in October 2011. A number of other manufacturers released Bluetooth Low Energy Ready devices in 2012.

The Bluetooth SIG officially unveiled Bluetooth 5 on 16 June 2016 during a media event in London. One change on the marketing side was that the point number was dropped, so it is now just called Bluetooth 5 (and not Bluetooth 5.0 or 5.0 LE like for Bluetooth 4.0). This decision was made to "simplify marketing, and communicate user benefits more effectively". On the technical side, Bluetooth 5 will quadruple the range by using increased transmit power or coded physical layer, double the speed by using optional half of the symbol time compared to Bluetooth 4.x, and provide an eight-fold increase in data broadcasting capacity by increasing the advertising data length of low-energy Bluetooth transmissions compared to Bluetooth 4.x, which could be important for IoT applications where nodes are connected throughout a whole house. An "advertising packet" in Bluetooth parlance is the information that is exchanged between two devices *before* pairing, i.e. when they are not connected. For example, advertising packets allow a device to display to the user the name of another Bluetooth device before pairing with it. Bluetooth 5 increased the data length of this advertising packet. The length of this packet in Bluetooth 4.x was 31 bytes (for broadcast topology).

The Bluetooth SIG officially released Mesh Profile and Mesh Model specifications on 18 July 2017. Mesh specification enables using Bluetooth Low Energy for many-to-many device communications for home automation, sensor networks, and other applications, where sensors, robots, smartphones, and other equipment need to be coordinated.

## Applications

Borrowing from the original Bluetooth specification, the Bluetooth SIG defines several profiles – specifications for how a device works in a particular application – for low-energy devices. Manufacturers are expected to implement the appropriate specifications for their device in order to ensure compatibility. A device may contain implementations of multiple profiles.

The majority of current Low Energy application profiles are based on the Generic Attribute Profile (GATT), a general specification for sending and receiving short pieces of data, known as attributes, over a low-energy link. The Bluetooth mesh profile is an exception to this rule, being based on the General Access Profile (GAP).

### Mesh profiles

Bluetooth mesh profiles use Bluetooth Low Energy to communicate with other Bluetooth Low Energy devices in the network. Each device can pass the information forward to other Bluetooth Low Energy devices, creating a "mesh" effect – for example, switching off an entire building of lights from a single smartphone.

- MESH (Mesh Profile) – for base mesh networking.
- MMDL (Mesh models) – for application layer definitions. The term "model" is used in mesh specifications instead of "profile" to avoid ambiguities.

### Health care profiles

There are many profiles for Bluetooth Low Energy devices in healthcare applications. The Continua Health Alliance consortium promotes these in cooperation with the Bluetooth SIG:

- BLP (Blood Pressure Profile) – for blood pressure measurement
- HTP (Health Thermometer Profile) – for medical temperature-measurement devices
- GLP (Glucose Profile) – for blood glucose monitors
- CGMP (Continuous Glucose Monitor Profile)

### Sports and fitness profiles

Profiles for sporting and fitness accessories include:

- BCS (Body Composition Service)
- CSCP (Cycling Speed and Cadence Profile) – for sensors attached to a bicycle or exercise bike to measure cadence and wheel speed
- CPP (Cycling Power Profile)
- HRP (Heart Rate Profile) – for devices which measure heart rate
- LNP (Location and Navigation Profile)
- RSCP (Running Speed and Cadence Profile)
- WSP (Weight Scale Profile)

### Generic sensors

- ESP (Environmental Sensing Profile)
- UDS (User Data Service)

### HID connectivity

- HOGP (HID over GATT Profile) allowing Bluetooth LE-enabled wireless mice, keyboards and other devices offering long-lasting battery life.

### Proximity sensing

"Electronic leash" applications are well-suited to the long battery life possible for "always-on" devices. Manufacturers of iBeacon devices implement the appropriate specifications for their device to make use of proximity-sensing capabilities supported by Apple's iOS devices.

Relevant application profiles include:

- FMP (the "find me" profile) – allows one device to issue an alert on a second misplaced device.
- PXP (the proximity profile) – allows a proximity monitor to detect whether a proximity reporter is within a close range. Physical proximity can be estimated using the radio receiver's RSSI value, although this does not have absolute calibration of distances. Typically, an alarm may be sounded when the distance between the devices exceeds a set threshold.

An example of proximity sensing usage is WebAuthn Hybrid Transport with cloud-assisted Bluetooth Low Energy (caBLE), allowing roaming authenticators such as smartphones to authenticate with WebAuthn credential (known as passkey). Bluetooth Low Energy is used as a proximity check between roaming authenticators and clients (such as personal computers).

### Alerts and time profiles

- The phone alert status profile and alert notification profile allow a client device to receive notifications such as incoming call alerts from another device.
- The time profile allows current time and time zone information on a client device to be set from a server device, such as between a wristwatch and a mobile phone's network time.

### Battery

- The Battery Service exposes the Battery State and Battery Level of a single battery or set of batteries in a device.

### Audio

Announced in January 2020, LE Audio is built on top of Bluetooth 5.2 / 5.3. It allows the Bluetooth LE protocol to carry audio, with lower battery consumption compared to regular Bluetooth Audio; features like one set of headphones connecting to multiple audio sources or multiple headphones connecting to one source (known as Auracast); and support for hearing aids. It introduces LC3 as its default codec. The standard has a lower minimum latency claim of 20–30 ms vs. Bluetooth Classic audio's 100–200 ms.

Specifications on the implementation of Basic Audio Profile and Coordinated Set Identification was released in 2021, and the Common Audio Profile and Service in March 2022. On 12 July 2022, the Bluetooth SIG announced the completion of Bluetooth LE Audio.

#### Auracast

Auracast implements public audio broadcasting services, allowing multiple receivers to connect to a single audio transmitter without going through Bluetooth device pairing first. It is a trademark owned by the Bluetooth SIG.

|   | Transmitter | Receiver | Assistant |
|---|---|---|---|
| BAP | Source | Sink | Assistant |
| PBP |   |   |   |
| CAP | Initiator | Acceptor | Commander |
| TMAP | Sender | Receiver | —N/a |
| HAP | —N/a | Hearing aid | —N/a |

Auracast is based on the following Bluetooth LE profiles and services:

- Basic Audio Profile (BAP) 1.0.1
- Public Broadcast Profile (PBP) 1.0
- Common Audio Profile (CAP) 1.0
- Telephony and Media Audio Profile (TMAP) 1.0
- Hearing Access Profile (HAP) 1.0
- Broadcast Audio Scan Service 1.0
- Published Audio Capabilities Service 1.0.1

Auracast transmitters use wireless advertisements to broadcast information about available streams – such as transmitter name, type of audio, program title, and language – which can be displayed on the receiver and in the apps on smartphones and smartwatches, or processed by the receiver to automatically connect to preferred sources.

Bluetooth LE–enabled smartphones function as an assistant to control Auracast receivers like headphones and earbuds. Broadcast Audio URI, marketed as "Scan to Listen", provides information required to connect to the specific audio stream, encoded with a QR code or transmitted using NFC. This allows users to directly select a specific audio stream in applications such as audio guides in a museum, simultaneous translations in multiple languages, silent TV screens in a bar or community center, public events or music performances at conference halls / sports venues / houses of worship, station and service announcements in public transport, and flight announcements in airports.

### MIDI

Developed by the MIDI Manufacturers Association (MMA) Working Group (now The MIDI Association), there is a formalized Bluetooth LE MIDI (BLE-MIDI) specification, a wireless protocol designed to transmit MIDI data over Bluetooth Low Energy. It focuses on power-efficient wireless MIDI communication for devices such as MIDI controllers, keyboards, pedals, etc., that don't continuously stream data – and without significant latency. Operating systems that support it include Windows 10 Version 1607, macOS and Android.

### Contact tracing and notification

In December 2020, the Bluetooth SIG released a draft specification for a wearable exposure-notification service. This service allows exposure-notification services on wearable devices to communicate with, and be controlled by, client devices such as smartphones.

## Implementation

### Chip

Starting in late 2009, Bluetooth Low Energy integrated circuits were announced by a number of manufacturers. These ICs commonly use software radio, so updates to the specification can be accommodated through a firmware upgrade.

### Hardware

Current mobile devices are commonly released with hardware and software support for both classic Bluetooth and Bluetooth Low Energy.

### Operating systems

- iOS 5 and later
- Windows Phone 8.1
- Windows 8 and later (Windows 7 and earlier requires drivers from Bluetooth radio manufacturer supporting BLE stack as it has no built-in generic BLE drivers.)
- Android 4.3 and later. Android 6 or later requires location permission to connect to BLE.
- BlackBerry OS 10
- Linux 3.4 and later through BlueZ 5.0
- Unison OS 5.2
- macOS 10.10
- Zephyr OS

## Technical details

### Radio interface

Bluetooth Low Energy technology operates in the same spectrum range (the 2.400–2.4835 GHz ISM band) as classic Bluetooth technology, but uses a different set of channels. Instead of the classic Bluetooth 79 1-MHz channels, Bluetooth Low Energy has 40 2-MHz channels. Within a channel, data is transmitted using Gaussian frequency shift modulation, similar to classic Bluetooth's Basic Rate scheme. The bit rate is 1 Mbit/s (with an option of 2 Mbit/s in Bluetooth 5), and the maximum transmit power is 10 mW (100 mW in Bluetooth 5). Further details are given in Volume 6 Part A (Physical Layer Specification) of the Bluetooth Core Specification V4.0.

Bluetooth Low Energy uses frequency hopping to counteract narrowband interference problems. Classic Bluetooth also uses frequency hopping but the details are different; as a result, while both FCC and ETSI classify Bluetooth technology as an FHSS scheme, Bluetooth Low Energy is classified as a system using digital modulation techniques or a direct-sequence spread spectrum.

| Specification | Basic/Enhanced Data Rate | Low Energy |
|---|---|---|
| Nominal max. range | 100 m (330 ft) | <100 m (<330 ft) |
| Over the air data rate | 1–3 Mbit/s | 125 kbit/s, 500 kbit/s, 1 Mbit/s, 2 Mbit/s |
| Application throughput, or 'goodput' | 0.7–2.1 Mbit/s | 0.27–1.37 Mbit/s |
| Active slaves | 7 | Not defined; implementation dependent |
| Security | 56/128-bit and application layer user defined | 128-bit AES in CCM mode and application layer user defined |
| Robustness | Adaptive fast frequency hopping, FEC, fast ACK | Adaptive frequency hopping, lazy acknowledgement, 24-bit CRC, 32-bit message integrity check |
| Wake latency (from a non-connected state) | Typically 100 ms | 6 ms |
| Minimum total time to send data (det. battery life) | 0.625 ms | 3 ms |
| Voice capable | Yes | Yes |
| Network topology | Scatternet | Scatternet |
| Power consumption | 1 W as the reference | 0.01–0.50 W (depending on use case) |
| Peak current consumption | <30 mA | <15 mA |
| Primary use cases | Mobile phones, gaming, headsets, stereo audio streaming, smart homes, wearables, automotive, PCs, security, proximity, healthcare, sports & fitness, etc. | Mobile phones, gaming, smart homes, wearables, automotive, PCs, security, proximity, healthcare, sports & fitness, industrial, etc. |

More technical details may be obtained from official specification as published by the Bluetooth SIG. Note that power consumption is not part of the Bluetooth specification.

### Advertising and discovery

BLE devices are detected through a procedure based on broadcasting advertising packets. This is done using 3 separate channels (frequencies), in order to reduce interference. The advertising device sends a packet on at least one of these three channels, with a repetition period called the advertising interval. For reducing the chance of multiple consecutive collisions, a random delay of up to 10 milliseconds is added to each advertising interval. The scanner listens to the channel for a duration called the scan window, which is periodically repeated every scan interval.

The discovery latency is therefore determined by a probabilistic process and depends on the three parameters (viz., the advertising interval, the scan interval and the scan window). The discovery scheme of BLE adopts a periodic-interval based technique, for which upper bounds on the discovery latency can be inferred for most parametrizations. While the discovery latencies of BLE can be approximated by models for purely periodic interval-based protocols, the random delay added to each advertising interval and the three-channel discovery can cause deviations from these predictions, or potentially lead to unbounded latencies for certain parametrizations.

### Security

Bluetooth Low Energy has security instances such as the Encrypted Advertising Data (EAD) feature allowing some or all of the application data payload that is transmitted in advertising packets, to be encrypted. A standard mechanism for the sharing of key material between a broadcasting device and the observers that are intended to receive this data is also defined, so that the data may be decrypted when received.

All transmitted Bluetooth LE PDUs include a cyclic redundancy check (CRC) that is recalculated and checked by the receiving device for the possibility of the PDU having been changed in flight.

### Software model

All Bluetooth Low Energy devices use the Generic Attribute Profile (GATT). The application programming interface offered by a Bluetooth Low Energy aware operating system will typically be based around GATT concepts. GATT has the following terminology:

**Client**

A device that initiates GATT commands and requests, and accepts responses, for example, a computer or smartphone.

**Server**

A device that receives GATT commands and requests, and returns responses, for example, a temperature sensor.

**Characteristic**

A data value transferred between client and server, for example, the current battery voltage.

**Service**

A collection of related characteristics, which operate together to perform a particular function. For instance, the

Health Thermometer

service includes characteristics for a temperature measurement value, and a time interval between measurements.

**Descriptor**

A descriptor provides additional information about a characteristic. For instance, a temperature value characteristic may have an indication of its units (e.g. Celsius), and the maximum and minimum values which the sensor can measure. Descriptors are optional – each characteristic can have any number of descriptors.

Some service and characteristic values are used for administrative purposes – for instance, the model name and serial number can be read as standard characteristics within the *Generic Access* service. Services may also include other services as sub-functions; the main functions of the device are so-called *primary* services, and the auxiliary functions they refer to are *secondary* services.

#### Identifiers

Services, characteristics, and descriptors are collectively referred to as *attributes*, and identified by universally unique identifiers (UUIDs). Any implementer may pick a random or pseudorandom UUID for proprietary uses, but the Bluetooth SIG have reserved a range of UUIDs (of the form *xxxxxxxx-0000-1000-8000-00805F9B34FB*) for standard attributes. For efficiency, these identifiers are represented as 16-bit or 32-bit values in the protocol, rather than the 128 bits required for a full UUID. For example, the *Device Information* service has the short code 0x180A, rather than 0000180A-0000-1000-... . The full list is kept in the Bluetooth Assigned Numbers document online.

#### GATT operations

The GATT protocol provides a number of commands for the client to discover information about the server. These include:

- Discover UUIDs for all primary services
- Find a service with a given UUID
- Find secondary services for a given primary service
- Discover all characteristics for a given service
- Find characteristics matching a given UUID
- Read all descriptors for a particular characteristic

Commands are also provided to *read* (data transfer from server to client) and *write* (from client to server) the values of characteristics:

- A value may be read either by specifying the characteristic's UUID, or by a *handle* value (which is returned by the information discovery commands above).
- Write operations always identify the characteristic by handle, but have a choice of whether or not a response from the server is required.
- 'Long read' and 'Long write' operations can be used when the length of the characteristic's data exceeds the MTU of the radio link.

Finally, GATT offers *notifications* and *indications*. The client may request a notification for a particular characteristic from the server. The server can then send the value to the client whenever it becomes available. For instance, a temperature sensor server may notify its client every time it takes a measurement. This avoids the need for the client to poll the server, which would require the server's radio circuitry to be constantly operational.

An *indication* is similar to a notification, except that it requires a response from the client, as confirmation that it has received the message.

#### Battery impact

Bluetooth Low Energy is designed to enable devices to have very low power consumption. Several chipmakers including Cambridge Silicon Radio, Dialog Semiconductor, Nordic Semiconductor, STMicroelectronics, Cypress Semiconductor, Silicon Labs and Texas Instruments had introduced Bluetooth Low Energy optimized chipsets by 2014. Devices with peripheral and central roles have different power requirements. A study by beacon software company Aislelabs reported that peripherals such as proximity beacons usually function for 1–2 years powered by a 1,000 mAh coin cell battery. This is possible because of the power efficiency of Bluetooth Low Energy protocol, which only transmits small packets as compared to Bluetooth Classic which is also suitable for audio and high bandwidth data.

In contrast, a continuous scan for the same beacons in central role can consume 1,000 mAh in a few hours. Android and iOS devices also have very different battery impact depending on type of scans and the number of Bluetooth Low Energy devices in the vicinity. With newer chipsets and advances in software, by 2014 both Android and iOS phones had negligible power consumption in real-life Bluetooth Low Energy use.

### 2M PHY

Bluetooth 5 has introduced a new transmission mode with a doubled symbol rate. Bluetooth LE has been traditionally transmitting 1 bit per symbol so that theoretically the data rate doubles as well. However, the new mode doubles the bandwidth from about 1 MHz to about 2 MHz which makes for more interferences on the edge regions. The partitioning of the ISM frequency band has not changed being still 40 channels spaced at a distance of 2 MHz. This is an essential difference over Bluetooth 2 EDR which also doubled the data rate but was doing that by employing a π/4-DQPSK or 8-DPSK phase modulation on a 1 MHz channel while Bluetooth 5 continues to use just frequency shift keying.

The traditional transmission of 1 Mbit in the Bluetooth Basic Rate was renamed 1M PHY in Bluetooth 5. The new mode at a doubled symbol speed was introduced as the 2M PHY. In Bluetooth Low Energy every transmission starts on the 1M PHY leaving it to the application to initiate a switch to the 2M PHY. In that case both sender and receiver will switch to the 2M PHY for transmissions. This is designed to facilitate firmware updates where the application can switch back to a traditional 1M PHY in case of errors. In reality the target device should be close to the programming station (at a few meters).

### LE Coded

Bluetooth 5 has introduced two new modes with lower data rate. The symbol rate of the new "Coded PHY" is the same as the Base Rate 1M PHY but in mode S=2 there are two symbols transmitted per data bit. In mode S=2 only a simple Pattern Mapping P=1 is used which simply produces the same stuffing bit for each input data bit. In mode S=8 there are eight symbols per data bit with a Pattern Mapping P=4 producing contrasting symbol sequences – a 0 bit is encoded as binary 0011 and a 1 bit is encoded as binary 1100. In mode S=2 using P=1 the range doubles approximately, while in mode S=8 using P=4 it does quadruple.

The "LE Coded" transmissions have not only changed the error correction scheme but it uses a fundamentally new packet format. Each "LE Coded" burst consists of three blocks. The switch block ("extended preamble") is transmitted on the LE 1M PHY but it only consists of 10 times a binary '00111100' pattern. These 80 bits are not FEC encoded as usual but they are sent directly to the radio channel. It is followed by a header block ("FEC Block 1") which is always transmitted in S=8 mode. The header block only contains the destination address ("Access Address" / 32 bit) and an encoding flag ("Coding Indicator" / 2 Bit). The Coding Indicator defines the Pattern Mapping used for the following payload block ("FEC Block 2") where S=2 is possible.

The new packet format of Bluetooth 5 allows transmitting from 2 up to 256 bytes as the payload in a single burst. This is a lot more than the maximum of 31 bytes in Bluetooth 4. Along with reach measurements this should allow for localisation functions. As a whole the quadrupled range—at the same transmission power—is achieved at the expense of a lower data being at an eighth with 125 kbit. The old transmission packet format, as it continues to be used in the 1M PHY and 2M PHY modes, has been named "Uncoded" in Bluetooth 5. The intermediate "LE Coded" S=2 mode allows for a 500 kbit data rate in the payload which is both beneficial for shorter latencies as well lower power consumption as the burst time itself is shorter.
