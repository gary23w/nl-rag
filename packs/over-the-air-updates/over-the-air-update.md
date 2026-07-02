---
title: "Over-the-air update"
source: https://en.wikipedia.org/wiki/Over-the-air_update
domain: over-the-air-updates
license: CC-BY-SA-4.0
tags: over-the-air update, firmware over-the-air, a/b partition rollback, ota campaign
fetched: 2026-07-02
---

# Over-the-air update

An **over-the-air update** (or **OTA update**), also known as **over-the-air programming** (or **OTA programming**), is an update to an operating system, or to firmware for an embedded system, that is delivered through a wireless network, such as Wi-Fi or a cellular network. These systems include mobile phones, tablets, set-top boxes, cars and telecommunications equipment. OTA updates for cars and internet of things devices can also be called **firmware over-the-air** (**FOTA**). Various components may be updated OTA, including the device's operating system, applications, configuration settings, or parameters like encryption keys.

## Terminology

The term *over-the-air update* applies to embedded systems. Before OTA updates, embedded devices could only be flashed through direct physical access (with a JTAG) or wired connections (usually through USB or a serial port). It is also used for mobile devices such as smartphones and tablet computers.

## Purpose

Over-the-air delivery may allow updates to be distributed at larger scales, reduce the cost of delivering updates, or increase the rate of adoption of these updates.

## Implementation

The distributor of these updates can decide whether users are allowed to decline these updates, and may choose to disable certain features on end-user devices until an update is applied. Users may be unable to revert an update after it is installed.

OTA updates are designed to be as small as possible in order to minimize energy consumption, network usage, and storage space. This is achieved by only transferring the differences between the old firmware and the new firmware, rather than transmitting the entire firmware. A delta of the old and new firmware is produced through a process called diffing; then, the delta file is distributed to the end-device, which uses the delta file to update itself.

## Industries

### Smartphones

On smartphones, tablets, and other devices, an over-the-air update is a firmware or operating system update that is downloaded by the device over the internet. Previously, users had to connect these devices to a computer over USB to perform an update. These updates may add features, patch security vulnerabilities, or fix software bugs. The two main mobile operating systems are iOS and Android.

iOS gained support for over-the-air updates in iOS 5. iOS updates are distributed exclusively by Apple, resulting in wide availability and relatively high adoption rates. Major iOS releases are usually installed on 60%–70% of iPhones within a few months of release.

Android OTA updates are device-dependent, and are not distributed by Google but by device manufacturers and sometimes wireless carriers. This has led to inconsistent availability of updates, and to Android fragmentation. In the past, fragmentation increased the complexity of developing third-party apps for Android due to inconsistent availability of the latest software frameworks on users' phones, and led to security concerns due to delays in the distribution of security updates. Google reduced Android fragmentation through the 2017 Project Treble, which allows OEMs to release OS updates without needing to re-test hardware drivers for each version, and the 2019 Project Mainline, which allows Google to update Android components and deliver security patches through its Play Store without requiring a full OS update. Project Mainline significantly lowers the role of middlemen in delivering OTA updates. Since Android 8.0, Android OTA updates follow an A/B partition scheme, in which an update is installed to a second ("B") partition in the background, and the phone switches to that partition the next time it is rebooted, reducing the time taken to install updates.

Windows Phone OTA updates were usually distributed by OEMs such as Nokia, and sometimes wireless carriers. OTA updates for Windows Phone devices labelled Microsoft Mobile were usually distributed by Microsoft.

### Automotive

Cars can support OTA updates to their in-car entertainment system, navigation map, telematic control unit, or their electronic control units (the onboard computers responsible for most of the car's operation). In cars, the telematic control unit is in charge of downloading and installing updates, and OTA updates are downloaded through cellular networks, like smartphones. Cars cannot be driven while an OTA update is being installed. Before an update, the car checks that the update is genuine, and after the update completes, it verifies the integrity of all affected systems.

OTA updates provide several benefits. In the past, Volkswagen had to recall 11 million vehicles to fix an issue with its cars' emissions control software, and other manufacturers have instituted recalls due to software bugs affecting the brakes, or the airbags, requiring all affected customers to travel to dealership to receive updates. OTA updates would have removed the need to go through dealerships, leading to lower warranty costs for manufacturers and lower downtime for customers. OTA updates also allow manufacturers to deploy potential new features and bug fixes more quickly, making their cars more competitive in the market, and resulting in an increased pace of product improvements for consumers. For example, OTA updates can deliver improvements to a car's driver assistance systems and improve the car's safety.

However, OTA updates can also present a new attack vector for hackers, since security vulnerabilities in the update process could be used by hackers to remotely take control of cars. Hackers have discovered such vulnerabilities in the past, and many car manufacturers have responded by instituting vulnerability disclosure programs (a.k.a. bug bounty programs). Attack vectors specific to OTA updates include "spoofing, tampering, repudiation [attacks], information leakage, denial-of-service," replay attacks, and privilege escalation attacks. Example scenarios include a hacker successfully interrupting an ongoing update (deemed a "flashing fail"), which may corrupt the car's computer systems and make the car malfunction later on; another scenario is "arbitrary flashings", in which hackers trick the car into installing a malicious OTA update.

### Internet of things (IoT)

With the newer concepts of wireless sensor networks and the Internet of Things (IoT), where the networks consist of hundreds or thousands of nodes, OTA is taken to a new direction: for the first time OTA is applied using unlicensed frequency bands (868 MHz, 900 MHz, 2400 MHz) and with low consumption and low data rate transmission using protocols such as 802.15.4 and Zigbee.

Sensor nodes are often located in places that are either remote or difficult to access. As an example, Libelium has implemented an OTA programming system for Zigbee WSN devices. This system enables firmware upgrades without the need of physical access, saving time and money if the nodes must be re-programmed.

### Internet routers

OTA is similar to firmware distribution methods used by other mass-produced consumer electronics, such as cable modems, which use TFTP as a way to remotely receive new programming, thus reducing the amount of time spent by both the owner and the user of the device on maintenance.

Over-the-air provisioning (OTAP) is also available in wireless environments (though it is disabled by default for security reasons). It allows an access point (AP) to discover the IP address of its controller. When enabled, the controller tells the other APs to include additional information in the Radio Resource Management Packets (RRM) that would assist a new access point in learning of the controller. It is sent in plain text however, which would make it vulnerable to sniffing. That is why it is disabled by default.

### Cellular networks

**Over-the-air provisioning** (OTAP) is a form of OTA update by which cellular network operators can remotely provision a mobile phone (termed a *client* or *mobile station* in industry parlance) and update the cellular network settings stored on its SIM card. This can occur at any time while a phone is turned on. The term *over-the-air parameter administration* (OTAPA) is synonymous. OTA provisioning allows mobile phones to remain properly configured when cellular network operators make changes to their networks. It also configures phones with the settings required to access certain features, like WAP (an early incarnation of the mobile web), MMS messaging, and cellular data (which requires the configuration of an Access Point Name).

The similar term *over-the-air service provisioning* (OTASP) specifically refers to the wireless initial provisioning ("activation") of a phone. During activation, a mobile phone is provisioned with parameters like its phone number, mobile identification number, and system ID, granting it initial access to the cellular network. OTASP is sometimes called *over-the-air activation* or *over-the-air bootstrapping*. The alternative to OTA bootstrapping is SIM bootstrapping, where the phone reads the network settings stored on a SIM card. SIM bootstrapping has limitations: settings stored on a SIM card may become stale between the time the SIM is manufactured and the time it is used; also, some phones (and other cellular client equipment) do not use SIM cards.

Various standards bodies have issued OTA provisioning standards. In 2001, the WAP Forum published the WAP Client Provisioning standard. After the Open Mobile Alliance subsumed the WAP Forum, this standard became known as OMA Client Provisioning (OMA CP). In OMA CP, phones are provisioned by "invisible" SMS messages sent by the cellular network, which contain the requisite settings. OMA CP was followed by a newer standard, OMA Device Management (OMA DM), which use a different form of SMS-based provisioning (called "OMA Push"). OMA DM sessions are always client-initiated. The "invisible" SMS does not contain configuration settings; instead, it tells the phone (the "DM Client") to connect to a DM Server (operated by the cellular network provider); once connected, the DM Server sends configuration commands to the client.

## OTA standards

There are a number of standards that describe OTA functions. One of the first was the GSM 03.48 series. The Zigbee suite of standards includes the Zigbee Over-the-Air Upgrading Cluster which is part of the Zigbee Smart Energy Profile and provides an interoperable (vendor-independent) way of updating device firmware.
