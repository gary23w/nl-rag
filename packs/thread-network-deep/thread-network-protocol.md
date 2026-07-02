---
title: "Thread (network protocol)"
source: https://en.wikipedia.org/wiki/Thread_(network_protocol)
domain: thread-network-deep
license: CC-BY-SA-4.0
tags: thread protocol, 6lowpan mesh, low-power ipv6, border router
fetched: 2026-07-02
---

# Thread (network protocol)

**Thread** is an IPv6-based, low-power mesh networking technology for Internet of things (IoT) products. Often used as a transport for the home automation connectivity standard Matter (the combination being known as *Matter over Thread*), the protocol has seen increased use for connecting low-power and battery-operated smart-home devices.

## Organization

In July 2014, the Thread Group alliance was formed as an industry group to develop, maintain and drive adoption of Thread as an industry networking standard for IoT applications. Thread Group provides certification for components and products to ensure adherence to the spec. Initial members were ARM Holdings, Big Ass Solutions, NXP Semiconductors/Freescale, Google-subsidiary Nest Labs, OSRAM, Samsung, Silicon Labs, Somfy, Tyco International, Qualcomm, and the Yale lock company. In August 2018, Apple joined the group, and released its first Thread product, the HomePod Mini, in late 2020.

The Thread protocol specification is available at no cost. It requires agreement and continued adherence to an end-user license agreement (EULA), which states "Membership in Thread Group is necessary to implement, practice, and ship Thread technology and Thread Group specifications."

## Characteristics

Thread uses IPv6 over Low-Power Wireless Personal Area Networks (6LoWPAN), which, in turn, uses LR-WPAN as defined by the IEEE 802.15.4 wireless protocol with mesh communication (in the 2.4 GHz spectrum), as do Zigbee and other systems. However, Thread is IP-addressable, with cloud access and AES encryption. A BSD-licensed open-source implementation of Thread called *OpenThread* is available from and managed by Google.

The OpenThread network simulator, a part of the OpenThread implementation, simulates Thread networks using OpenThread POSIX instances. The simulator utilises discrete-event simulation and allows for visualisation of communications through a web interface.

## Use cases

In 2019, the Connected Home over IP (CHIP) project, subsequently renamed to *Matter*, led by the Zigbee Alliance, now the Connectivity Standards Alliance (CSA), Google, Amazon, and Apple, announced a broad collaboration to create a royalty-free standard and open-source code base to promote interoperability in home connectivity, leveraging Thread, Wi-Fi, and Bluetooth Low Energy.

## Border routers

A Thread border router is a device that provides bidirectional Internet Protocol connectivity between a Thread network and another physical network, such as Wi-Fi or Ethernet. It enables communication between Thread devices and other local networks or the Internet. A Thread network is a low-power mesh network using the IEEE 802.15.4 protocol in the 2.4 GHz ISM radio band, and a border router translates between such a network another physical network, allows for service discovery across network boundaries, and enables external commissioning of Thread devices. Without a border router, Thread devices would be isolated from other networks and the Internet.

| Company | Device name | Release year | Availability |
|---|---|---|---|
| Amazon | Echo | 2020 | 4th generation and newer |
| Echo Hub | 2024 | All models |   |
| Echo Plus | 2018 | 2nd generation |   |
| Echo Show | 2024 2024 2021 2023 | Echo Show 21 Echo Show 15 (2nd generation) Echo Show 10 (3rd generation) Echo Show 8 (3rd generation) |   |
| Echo Studio | 2019 | All models |   |
| eero routers | 2017 | All eero Pro routers and eero Beacon All third-generation routers with Wi-Fi 6 and newer |   |
| Apple | Apple TV 4K | 2021 | 2nd generation 3rd generation with Ethernet |
| HomePod Mini | 2020 | All models |   |
| HomePod | 2023 | 2nd generation |   |
| Google | Google Home Speaker | 2026 | All models |
| Google TV Streamer 4K | 2024 | All models |   |
| Nest Hub | 2021 | 2nd generation |   |
| Nest Hub Max | 2019 | All models |   |
| Nest Wifi | 2019 | All models |   |
| MikroTik | hAP be³ Media | 2026 | All models |
| Samsung SmartThings | SmartThings Hub | 2018 | Version 3 |
| SmartThings Station | 2023 | All models |   |
| Aeotec Smart Home Hub | 2021 | All models |   |
