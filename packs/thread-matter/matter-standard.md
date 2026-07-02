---
title: "Matter (standard)"
source: https://en.wikipedia.org/wiki/Matter_(standard)
domain: thread-matter
license: CC-BY-SA-4.0
tags: thread network protocol, matter standard, thread mesh, ipv6 smart home
fetched: 2026-07-02
---

# Matter (standard)

**Matter** is a technical standard for smart home and Internet of things (IoT) devices. It is intended to improve interoperability and compatibility between different manufacturers and security, always allowing local control as an option.

Matter originated in December 2019 as the Project Connected Home over IP (CHIP) working group, founded by Amazon, Apple, Google, and the Connectivity Standards Alliance (when it was the Zigbee Alliance). Subsequent members include IKEA, Huawei, Heiman, and Schneider. Version 1.0 of the specification was published on 4 October 2022. The Matter software development kit is open-source under the Apache License.

A software development kit (SDK) is provided royalty-free, though the ability to commission a finished product into a Matter network in the field mandates certification and membership fees, entailing both one-time, recurring, and per-product costs. This is enforced using a public key infrastructure (PKI) and so-called device attestation certificates.

Matter-compatible software updates for many existing hubs became available in late 2022, with Matter-enabled devices and software updates starting to release in 2023.

The primary goal of Matter is to improve interoperability for the current smart home ecosystem. CSA and its members aim for the Matter logo to become ubiquitous and for consumers to instantly recognise it as a smart home device that will "just work". However, Matter logos do not imply that devices will "just work"; infrastructure is also still required for full functionality, like a Wi-Fi network (which may need to be dual-band) and a Matter controller, and often, an app for each kind of device.

## Background

In December 2019, Amazon, Apple, Google, Samsung SmartThings and the Zigbee Alliance announced the collaboration and formation of the working group of Project Connected Home over IP. The goal of the project is to simplify development for smart home product brands and manufacturers while increasing the compatibility of the products for consumers.

The standard operates on Internet Protocol (IP) and functions via one or more controllers that connect and manage devices within a local network, eliminating the need for multiple proprietary hubs for each ecosystem. Matter-certified products are engineered to operate locally and do not depend on an internet connection for their core functions. Leveraging IPv6 addressing, the standard facilitates seamless communication with cloud services. Its goal is to facilitate interoperability among smart home devices, mobile apps, and cloud services, employing a specific suite of IP-based networking technologies such as mDNS and IPv6. By adhering to a network design that operates at the Application Layer of the OSI 7 layer model, Matter differs from protocols like Zigbee or Z-Wave and theoretically can function on any IPv6-enabled network. Presently, official support is limited to Wi-Fi, Ethernet, and the wireless mesh network Thread.

## Versions

Updates to the standard are planned to occur biannually.

- Version 1.0 of the specification was published on 4 October 2022. It introduced support for lighting products (such as mains power plugs, electric lights and switches), door locks, thermostats and heating, ventilation, and air conditioning controllers, blinds and shades, home security sensors (such as door, window and motion sensors), and televisions and streaming video players.
- Version 1.1 of the specification was published on 18 May 2023. Although a new version, it did not include any new categories, only bug fixes and enhancements to existing SDK, API and devices.
- Version 1.2 of the specification was published on 23 October 2023. This version added nine new device types (refrigerators, portable air conditioners, dishwashers, laundry washers, robotic vacuum cleaners, smoke and carbon monoxide alarms, air quality sensors, air purifiers, and fans). It also provides revisions and additions to existing categories, improvements to the specification and SDK, and certification and testing tools.
- Version 1.3 of the specification was published on 8 May 2024. This version added support for water and energy management devices as well as appliance support for ovens, microwave ovens, cooktops, extractor hoods, laundry dryers, and Matter-casting media players. Scenes and command-batching were also added.
- Version 1.4 of the specification was released on 7 November 2024, introducing an expanded focus on electricity-related areas, including batteries, solar systems, home routers, water heaters, and heat pumps. It also featured enhancements to existing areas, such as increased support for electric vehicle chargers, along with significant improvements to Thread devices.
- Version 1.4.1 of the specification was released on 7 May 2025. This minor version adds NFC onboarding and multi-device setup.
- Version 1.4.2 of the specification was released on 11 August 2025. The minor update made security enhancements to Matter networks and standardized various existing behaviors to improve networking. The update also made some changes to device support requirements for routers and other "network infrastructure managers," requiring them to be certified for Thread 1.4 and support addressing at least 150 devices.
- Version 1.5 of the specification was published on 20 November 2025. This major update adds support for cameras, soil moisture sensors and energy management features. Additionally, this version enhances the Closures service, allowing for modular motion types (e.g. sliding, rotating and opening) which can be leveraged by component builders to improve services such blinds, curtains, gates and doors.

For future versions, the working group has been working on support for ambient motion and presence sensing, environmental sensing and controls, closure sensors, energy management, Wi-Fi access points, cameras, and major appliances.

## Supported devices

CSA maintains the official list of Matter-certified products, and restricts use of the Matter logo to certified devices. Matter product certification is also stored on the CSA's Distributed Compliance Ledger (DCL), which publishes attestation information about certified devices.

### Supported ecosystems and hubs

| Company | Platforms | Device types | Hubs |   |
|---|---|---|---|---|
| Product name(s) | Thread support included? |   |   |   |
| Amazon | Android, iOS, iPadOS | Air conditioners, air purifiers, dishwashers, fans, lights, locks, outlets, robot vacuums, switches (including generic), sensors (air quality, contact, humidity, light, motion, smoke, and temperature), thermostats, and window coverings | Echo (2nd gen., 3rd gen.) | No |
| Echo (4th gen.) | Yes |   |   |   |
| Echo Dot (2nd gen. and newer) | Yes |   |   |   |
| Echo Dot with Clock (2nd gen. and newer) | Yes |   |   |   |
| Echo Flex | No |   |   |   |
| Echo Hub | Yes |   |   |   |
| Echo Input | No |   |   |   |
| Echo Plus (2nd gen.) | Yes |   |   |   |
| Echo Pop | No |   |   |   |
| Echo Show 5 | No |   |   |   |
| Echo Show 8 (1st gen., 2nd gen.) | No |   |   |   |
| Echo Show 8 (3rd gen.) | Yes |   |   |   |
| Echo Show 10 (3rd gen.) | Yes |   |   |   |
| Echo Show 15 (1st gen.) | No |   |   |   |
| Echo Show 15 (2nd gen.) | Yes |   |   |   |
| Echo Show 21 | Yes |   |   |   |
| Echo Spot (2024) | No |   |   |   |
| Echo Studio (1st gen., 2nd gen.) | Yes |   |   |   |
| eero 6 and eero 6+ | Yes |   |   |   |
| eero Beacon | Yes |   |   |   |
| eero Max 7 | Yes |   |   |   |
| eero Outdoor 7 | Yes |   |   |   |
| eero PoE 6 | Yes |   |   |   |
| eero PoE gateway | Yes |   |   |   |
| eero Pro | Yes |   |   |   |
| eero Pro 6E and eero Pro 6 | Yes |   |   |   |
| Apple | tvOS, audioOS, macOS, iOS, iPadOS | Air purifiers, bridges, lights, locks, outlets, robot vacuums, sensors (air quality, contact, humidity, illuminance, motion, occupancy & temperature), thermostats, and window coverings | HomePod (1st gen.) | No |
| HomePod (2nd gen.) | Yes |   |   |   |
| HomePod mini | Yes |   |   |   |
| Apple TV 4K WIFI (2022) | No |   |   |   |
| Apple TV 4K WIFI + Ethernet (2022) | Yes |   |   |   |
| Apple TV 4K (2021) | Yes |   |   |   |
| Google | Android, Wear OS, iOS, iPadOS | Air purifiers, bridges, dishwashers, dryers, lights, locks, outlets, robot vacuums, sensors (air quality, contact, flow, humidity, illuminance, motion, occupancy, pressure, & temperature), speakers, thermostats, washers, and window coverings (except tilting) | Chromecast with Google TV (4K) | No |
| Google Home | No |   |   |   |
| Google Home Speaker | Yes |   |   |   |
| Google Home mini | No |   |   |   |
| Google TV Streamer | Yes |   |   |   |
| Nest Mini | No |   |   |   |
| Nest Audio | No |   |   |   |
| Nest Hub (1st gen.) | No |   |   |   |
| Nest Hub (2nd gen.) | Yes |   |   |   |
| Nest Hub Max | Yes |   |   |   |
| Nest Wifi Pro | Yes |   |   |   |
| IKEA | Android, iOS | Dimming and colour changing lights, remote switches, sensors (water, motion, door/window, temperature and humidity) | Dirigera | Yes |
| MikroTik | RouterOS | Routers | hAP be³ Media | Yes |
| Samsung | Android, Wear OS, iOS, iPadOS, watchOS, Windows | Air conditioners, air purifiers, basic video players, battery storages, cook surfaces, cooktops, dimmable plug-in units, dimming lights, dishwashers, door locks, electric vehicle supply equipments, enhanced color lights, extractor hoods, fans, generic switches (buttons), heat pumps, laundry dryers, laundry washers, matter bridges, microwave ovens, mounted dimmable load controls, mounted on/off controls, on/off lights, on/off plug-in units, oven (ranges), pumps, refrigerators, robotic vacuum cleaners, sensors (air quality, contact, humidity, light, occupancy, pressure, rain, and temperature), smoke & co alarms, solar power devices, speakers, temperature color lights, temperature controlled cabinets, thermostats, water freeze detectors, water heaters, water leak detectors, water valves, and window coverings | Samsung SmartThings Hub v2 | No |
| Samsung Family Hub refrigerator (2017 and newer) | No (can be added using external dongle) |   |   |   |
| Samsung Smart Monitors 2022 models | No |   |   |   |
| Samsung smart TVs 2022 models | No |   |   |   |
| Aeotec SmartThings Smart Home Hub | Yes |   |   |   |
| Aeotec SmartThings Smart Home Hub 2 | Yes |   |   |   |
| Samsung SmartThings Station | Yes |   |   |   |
| Samsung SmartThings Hub Dongle | Yes |   |   |   |
| Samsung SmartThings Hub v3 | Yes |   |   |   |
| Samsung Smart TVs CU8000 and CU7000 (2023) | Yes |   |   |   |
| Samsung MicroLED TV MNA89MS1BA (2023) | Yes |   |   |   |
| Samsung Smart Monitor M80C (2023) | Yes |   |   |   |
| Samsung Soundbar HW-Q990C (2023) | Yes |   |   |   |
| Samsung NEO QLED 8k and 4K (2023) | Yes |   |   |   |
| Family Hub refrigerator, model numbers RF29CB9900QKAA (US), RF23CB9900QKAA (US), RF85C9581APW (Korea) | Yes |   |   |   |
