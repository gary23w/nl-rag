---
title: "LoRaWAN"
source: https://en.wikipedia.org/wiki/LoRaWAN
domain: lorawan-deep
license: CC-BY-SA-4.0
tags: lorawan protocol, lora wide-area network, lpwan networking, chirp spread spectrum radio
fetched: 2026-07-02
---

# LoRaWAN

**LoRaWAN** is a low-power, wide-area network (LPWAN) protocol that wirelessly connects battery-operated devices to the Internet. LoRaWAN uses LoRa as the physical layer. LoRa can be thought of as the radio signal technology (similar to Wi-Fi or cellular), while LoRaWAN is the protocol and network architecture that manages communication over that signal.

Together, LoRa and LoRaWAN provide a solution for connecting low-power devices over long distances, making them a key technology for the Internet of Things (IoT). The technology is primarily used for applications where small amounts of data need to be transmitted infrequently from hard-to-reach locations, such as in smart agriculture, industrial monitoring, and asset tracking. The technology was originally developed by the French company Cycleo, which was acquired by Semtech in 2012, and the LoRaWAN standard is now managed by the LoRa Alliance.

## Features

LoRaWAN devices have geolocation capabilities used for trilaterating positions of devices via timestamps from gateways.

LoRa's geolocation feature, combined with the technology's long-range and low-power characteristics, makes it suitable for a wide range of Internet of Things (IoT) applications where assets are dispersed and battery life is critical.

### Asset tracking and logistics

LoRaWAN is widely used for asset tracking, particularly for non-powered assets that require a tracking system with a long battery life. Because it does not rely on cellular networks, it is an effective technology for monitoring moving objects in areas with poor or no GSM signal, such as in remote areas or inside large metal shipping containers. A common application is in the track and trace of construction and railway equipment. For example, LoRaWAN trackers are used in Switzerland to monitor the location of construction wagons, providing security against theft and improving the efficiency of fleet logistics.

### Smart agriculture

In precision agriculture, LoRaWAN sensors are used to create managing information systems that optimize farming operations. Low-power sensors are deployed across large fields to monitor soil moisture, temperature, and nutrient levels, allowing for more efficient irrigation and fertilization. The technology is also used for tracking the location and health of livestock.

### Smart cities and utilities

LoRaWAN is used for smart city applications. Municipalities use it for a variety of services, including:

- Smart metering: Utility companies deploy LoRaWAN-enabled meters to automatically read water and gas consumption without needing to send a technician.
- Waste management: Sensors in public trash bins can report when they are full, allowing for the optimization of collection routes.
- Smart parking: Sensors in parking spaces can detect whether a space is occupied, providing real-time data to drivers via a mobile app.

## LoRaWAN elaboration

While LoRa defines the lower physical layer, LoRaWAN is the system architecture for the network. LoRaWAN defines the communication protocol for managing communication between low-power end-node devices and gateways.

The LoRaWAN network architecture consists of three main components:

- **End Devices:** These are the small, battery-powered sensors or trackers that are spread out in the field. Each device has a LoRa chip that allows it to transmit small packets of data over long distances using the LoRa radio protocol. Its MAC layer is configured from the Network Server.
- **Gateways (Base Stations):** A gateway is a receiving station that is connected to the internet. It listens on multiple channels for signals from all the LoRaWAN end devices within its range. When a gateway receives a data packet from a device, it forwards it to the central network server without processing it. A key feature of LoRaWAN is that a single data packet from a device can be picked up by multiple gateways simultaneously, which increases the network's reliability. When commanded by the Network Server to transmit data it derives all LoRa PHY configurations per packet. Therefor it requires no MAC layer.
- **Network Server:** This is the central cloud-based software that manages the entire network. It receives the data from all the gateways, removes duplicate messages, and then routes the data to the correct application server. It is also responsible for managing the communication frequencies, data rate, and power for all end devices.

Devices in the network are asynchronous and transmit when they have data available to send. Data transmitted by an end-node device is received by multiple gateways, which then forward the data packets to the centralized network server. The data is then forwarded to an associated application server.

### CSMA for LoRaWAN

In the wireless communication, particularly across the IoT applications, collision avoidance is essential for reliable communication and overall spectral efficiency. Previously, LoRaWAN has relied upon ALOHA as the medium access control (MAC) layer protocol, but to improve this, the LoRa Alliance's Technical Recommendation TR013 introduced CSMA-CA. Employing the CAD based CSMA technique specified in TR013 enhances LoRaWAN's spectrum efficiency and ensures more reliable device communication, including in congested environments. TR013 is based on the LMAC and is the first industry-academia collaboration of LoRa Alliance to have resulted in a Technical Recommendation.

## Version history

- January 2015: 1.0
- February 2016: 1.0.1
- July 2016: 1.0.2
- October 2017: 1.1, adds Class B
- July 2018: 1.0.3
- October 2020: 1.0.4

## Governance

The **LoRa Alliance** is nonprofit organization located in Fremont, California supporting the LoRaWAN standard and deployments in remote or hard-to-reach locations. Members include Actility, Amazon Web Services, Cisco, Everynet, Helium, Kerlink, MachineQ, Microsoft, MikroTik, Minol Zenner, Netze BW, Semtech, Senet, STMicroelectronics, TEKTELIC,Orbiwise SA and The Things Industries. In 2018, the LoRa Alliance had over 100 LoRaWAN network operators in over 100 countries; in 2023, there are nearly 200, providing coverage in nearly every country in the world. On October 1, 2024, Cisco announced it is "exiting the LoRaWAN space" with no planned migration for Cisco LoRaWAN gateways.
