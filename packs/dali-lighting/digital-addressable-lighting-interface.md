---
title: "Digital Addressable Lighting Interface"
source: https://en.wikipedia.org/wiki/Digital_Addressable_Lighting_Interface
domain: dali-lighting
license: CC-BY-SA-4.0
tags: dali lighting protocol, digital addressable lighting interface, lighting control bus, led dimming control
fetched: 2026-07-02
---

# Digital Addressable Lighting Interface

**Digital Addressable Lighting Interface** (**DALI**) is a trademark for network-based products that control lighting. The underlying technology was established by a consortium of lighting equipment manufacturers as a successor for 1-10 V/0–10 V lighting control systems, and as an open standard alternative to several proprietary protocols. The DALI, DALI-2 and D4i trademarks are owned by the lighting industry alliance, DiiA (Digital Illumination Interface Alliance).

DALI is specified by a series of technical standards in **IEC 62386**. Standards conformance ensures that equipment from different manufacturers will interoperate. The DALI trademark is allowed on devices that comply with the DiiA testing and certification requirements, and are listed as either registered (DALI version-1) or certified (DALI-2) on the DiiA website. D4i certification - an extension of DALI-2 - was added by DiiA in November 2019.

Members of the AG DALI were allowed to use the DALI trademark until the DALI working party was dissolved on 30 March 2017, when trademark use was transferred to DiiA members. Since 9 June 2017, Digital Illumination Interface Alliance (DiiA) certifies DALI products. DiiA is a Partner Program of IEEE-ISTO.

## Technical overview

A DALI network consists of at least one application controller and bus power supply (which may be built into any of the products) as well as input devices (e.g. sensors and push-buttons), control gear (e.g., electrical ballasts, LED drivers and dimmers) with DALI interfaces. Application controllers can control, configure or query each device by means of a bi-directional data exchange. Unlike DMX, multiple controllers can co-exist on the bus. The DALI protocol permits addressing devices individually, in groups or via broadcast. Scenes can be stored in the devices, for recall on an individual, group or broadcast basis. Groups and scenes are used to ensure simultaneous execution of level changes, since each packet requires about 25 ms - or 1.5 seconds if all 64 addresses were to change level.

Each device is assigned a unique short address between 0 and 63, making up to 64 devices possible in a basic system. Address assignment is performed over the bus using a "commissioning" protocol built into the DALI controller, usually after all hardware is installed, or successively as devices are added. The Device Address is commonly a LED driver with one or many LEDs sharing the same level. A DT6 driver is for single color temperature applications, a DT8 driver is used for CCT color tuning, or RGBWW multi color applications - for example a strip where all the "pixels" have the same color.

Data is transferred between devices by means of an asynchronous, half-duplex, serial protocol over a two-wire bus with a fixed data transfer rate of 1200 bit/s. Collision detection is used to allow multiple transmitters on the bus.

A single pair of wires comprises the bus used for communication on a DALI network. The network can be arranged in bus or star topology, or a combination of these. Each device on a DALI network can be addressed individually, unlike DSI and 0–10V devices. Consequently, DALI networks typically use fewer wires than DSI or 0–10V systems.

The bus is used for both signal and bus power. A power supply provides a current limited source of up to 250 mA at typically 16 V DC; each device may draw up to 2 mA unless bus-powered. While many devices are mains-powered (line-powered), low-power devices such as motion detectors may be powered directly from the DALI bus. Each device has a bridge rectifier on its input so it is polarity-insensitive. The bus is a wired-AND configuration where signals are sent by briefly shorting the bus to a low voltage level. (The power supply is required to tolerate this, limiting the current to 250 mA.)

Although the DALI control cable operates at ELV potential, it is not classified as SELV (*Safety* Extra Low Voltage) and therefore should not be Accessible to the user. The requirements of the DALI standard IEC 62386-101 (clause 4.9.2) categorise the interface as FELV. It also requires that the interface have at least Basic insulation from AC mains, and Supplementary insulation from the interface to any user Accessible part like the cover of the equipment. Clause 4.10 does not permit any part of the interface to be connected to Protective Earth unless this occurs at a low power (less than 250mA) bus power supply, or via a Class Y safety capacitor. This requirement for an unearthed interface precludes the use of an earthed conductor to meet the FELV requirements of IEC 60364-4-41 clause 411.7, further mandating the use of Basic insulation between AC mains and the interface. This also means that the interface cable is required to be mains-rated and permits it to be run next to mains cables or within a multi-core cable which includes mains power.

The network cable is required to provide a maximum drop of 2 volts along the cable. At 250 mA of supply current, that requires a resistance of ≤ 4 Ω per wire. The wire size needed to achieve this depends on the length of the bus, up to a recommended maximum of 2.5 mm2 at 300 m when using the maximum rating of bus power supply.

The speed is kept low so no termination resistors are required, and data is transmitted using relatively high voltages (0±4.5 V for low and 16±6.5 V for high) enabling reliable communications in the presence of significant electrical noise. (This also allows plenty of headroom for a bridge rectifier in each slave.)

Each bit is sent using Manchester encoding (a "1" bit is low for the first half of the bit time, and high for the second, while "0" is the reverse), so that power is present for half of each bit. When the bus is idle, the voltage level is continuously high (which is not the same as a data bit). Frames begin with a "1" start bit, then 8 to 32 data bits with the most significant bit first (standard RS-232 has the least significant bit first), followed by a minimum of 2.45 ms of idle.

## Device addressing

A DALI device, such as a LED driver, can be controlled individually via its short address. Additionally, each DALI device may be members of one to 16 groups, or be a member of up to 16 scenes. All devices of a group respond to the commands addressed to the group. For example, a room with 4 ballasts can be changed from off to on in three common ways:

### Single device

Using the Short Address, e.g. sending the following DALI messages:

- DALI Short Address 1 go to 100%
- DALI Short Address 2 go to 100%
- DALI Short Address 3 go to 100%
- DALI Short Address 4 go to 100%

This method has the advantage of not requiring programming of group and scene information for each ballast. The fade time of the transition can be chosen on the fly. If a large number of devices need to change at once, note that only 40 commands per second are possible - therefore, 64 individual addresses would require 1.5 seconds. For example, turning all lighting fixtures off may result in a visible delay between the first and last ballasts switching off. This issue is normally not a problem in rooms with a smaller number of ballasts. Groups and Scenes solve that.

### Device groups

Using the DALI Group previously assigned to ballasts in the room, if Short Address 1, 2, 3 and 4 are members of Group 1, e.g.:

- DALI Group address 1 go to 100%

This method has the advantage of being immune to synchronization effects as described above. This method has the disadvantage of requiring each ballast to be programmed once, by a DALI master, with the required group numbers and scene information. The fade time can still be configured on the fly, if required.

### Broadcast

Using the DALI Broadcast command, all control gear will change to that level, e.g.:

- DALI Broadcast go to 50%

## Scenes

Devices store 16 programmable output levels as "scenes". Individual, Group or ALL devices can respond to a global Scene recall command to change to its previously configured level, e.g. dim lights over the audience and bright lights over the stage. (A programmed brightness level of 255 causes a device to not respond to a given scene - hence be excluded from scene recall commands.)

## System Fail brightness

A "system failure" level can be triggered by a loss of power (sustained low level) on the DALI bus, to provide a safe fallback if control is lost, a level of 255 excludes the device from this feature.

## Brightness control

DALI lighting levels are specified by an 8-bit value, with 0 representing off, 1 means 0.1% of full brightness, 254 means full brightness, and other values being logarithmically interpolated, giving a 2.77% increase per step. I.e., a (non-zero) control byte x denotes a power level of 103(*x*−254)/253.

(The value of 255 is reserved for freezing the current lighting level without changing it.)

This is designed to match human eye sensitivity so that perceived brightness steps are uniform, and to ensure corresponding brightness levels in units from different manufacturers.

## Commands for control gear

Forward frames sent to control gear are 16 bits long, comprising an address byte followed by an opcode byte. The address byte specifies a target device or a *special command* addressed to all devices.

Except for special commands, when addressing a device, the 7 most significant bits is the device address. The least significant bit of the address byte specifies the interpretation of the opcode byte, with "0" meaning that the opcode is a light level (ARC), and "1" meaning that the opcode is a command.

Multi packet commands are used for more complex tasks - like setting RGB colors. These commands use three "data transfer registers" (DTR, DTR1, DTR2 ) which can be read and written or used as a parameter by subsequent commands. For example, copy the current ARC level to DTR, save DTR as a scene. Evidently, the DTR value can be different in different devices.

Address byte (AB) format:

- `0AAA AAAS`: Target device 0 ≤ A < 64.
- `100A AAAS`: Target group 0 ≤ A < 16. Each control gear may be a member of any or all groups.
- `1111 110S`: Broadcast unaddressed
- `1111 111S`: Broadcast
- `1010 0000 to 1100 1011`: Special commands
- `1100 1100 to 1111 1011`: Reserved

Common control gear commands:

| Value (Hex) | Command | Description | Answer |
|---|---|---|---|
|   | **Control commands** |   |   |
| AB | DAPC (level) | Sets targetLevel (0-254) to device(s) at address AB using the current fade time, or stops a running fade (255). [S bit must be 0] |   |
| 00 | OFF | Set targetLevel to 0 without fading |   |
| 01 | UP | Starts or continues a fade up for 200ms at the current fade rate |   |
| 02 | DOWN | Starts or continues a fade down for 200ms at the current fade rate |   |
| 03 | STEP UP | Increments targetLevel by 1 without fading |   |
| 04 | STEP DOWN | Decrements targetLevel by 1 without fading |   |
| 05 | RECALL MAX LEVEL | Set targetLevel to MAX level without fading |   |
| 06 | RECALL MIN LEVEL | Set targetLevel to MIN level without fading |   |
| 07 | STEP DOWN AND OFF | Decrements targetLevel by 1 without fading, turning off if already at MIN level |   |
| 08 | ON AND STEP UP | Increments targetLevel by 1 without fading, turning on to MIN level if currently off |   |
| 09 | GO TO LAST ACTIVE LEVEL | Sets targetLevel to the last active (non-zero) level, using the current fade time. |   |
| 10+s | GO TO SCENE (sceneNumber) | Sets targetLevel to the value stored in scene sceneNumber, using the current fade time, or no change if the value stored in the scene is 255. |   |
|   | **Configuration commands** |   |   |
| 20 | RESET | Changes all variables to their reset values. |   |
| 21 | STORE ACTUAL LEVEL IN DTR0 | Stores the actualLevel (light output level) in register DTR0 |   |
|   | IDENTIFY DEVICE | Starts a temporary identification process such as flashing the lamps, making a sound or transmitting an RF beacon. |   |
| 2A | SET MAX LEVEL (DTR0) | Changes maxLevel level to DTR0 |   |
| 2B | SET MIN LEVEL (DTR0) | Changes minLevel level to DTR0 |   |
| 2C | SET SYSTEM FAILURE LEVEL (DTR0) | Changes systemFailureLevel to DTR0 |   |
| 2D | SET POWER ON LEVEL (DTR0) | Changes powerOnLevel to DTR0 |   |
| 2E | SET FADE TIME (DTR0) | Changes fadeTime to DTR0 |   |
| 2F | SET FADE RATE (DTR0) | Changes fadeRate to DTR0 |   |
|   | SET EXTENDED FADE TIME (DTR0) | Changes the two 4-bit variables extendedFadeTimeMultiplier:extendedFadeTimeBase to DTR0 |   |
| 40+s | SET SCENE (DTR0, sceneX) | Changes sceneX to the value DTR0 |   |
| 60+g | ADD TO GROUP (group) | Adds the control gear into the specified group |   |
|   | **Query commands** |   |   |
| 90 | QUERY STATUS | Asks the control gear for the current status. Reply bits: 0=controlGearFailure; 1=lampFailure; 2=lampOn; 3=limitError; 4=fadeRunning; 5=resetState; 6=shortAddress is MASK; 7=powerCycleSeen | XX |
| 92 | QUERY LAMP FAILURE | Asks the control gear if it is currently detecting a lamp failure | Yes/No |
| A0 | QUERY ACTUAL LEVEL | Asks the control gear what the current actualLevel (output level) is | XX |

## Commands for control devices

The DALI-2 standard added standardisation of control devices. Control devices can include input devices such as daylight sensors, passive infrared room occupancy sensors, and manual lighting controls, or they can be application controllers that are the "brains" of the system - using information to make decisions and control the lights and other devices. Control devices can also combine the functionality of an application controller and an input device. Control devices use 24-bit forward frames, which are ignored by control gear, so up to 64 control devices may share the bus with up to 64 control gear.

## D4i

DiiA published several new specifications in 2018 and 2019, extending DALI-2 functionality with power and data, especially for intra-luminaire DALI systems. Applications include indoor and outdoor luminaires, and small DALI systems. The D4i trademark is used on certified products to indicate that these new features are included in the products.

## Colour control (DT8)

IEC 62386-209 describes colour control gear. This describes several colour types - methods of controlling colour. The most popular of these is Tc (tunable white), and was added to DALI-2 certification in January 2020.

## Emergency lighting

IEC 62386-202 describes self-contained emergency lighting. Features include automated triggering of function tests and duration tests, and recording of results. These devices are currently included in DALI version-1 registration, with tests for DALI-2 certification in development. Such DALI version-1 products can be mixed with DALI-2 products in the same system, with no problems expected.

## Wireless

IEC 62386-104 describes several wireless and wired transport alternatives to the conventional wired DALI bus system. DiiA is working with other industry associations to enable certification of DALI-2 products that operate over certain underlying wireless carriers. It is also possible to combine DALI with wireless communication via application gateways that translate between DALI and the wireless protocol of choice. While such gateways are not standardized, DiiA is working with other industry associations to develop the necessary specifications and tests to achieve this. DiiA: DALI and Wireless
