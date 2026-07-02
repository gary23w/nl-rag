---
title: "Human interface device"
source: https://en.wikipedia.org/wiki/Human_interface_device
domain: web-hid
license: CC-BY-SA-4.0
tags: web hid api, human interface device, hid report descriptor, raw input output device
fetched: 2026-07-02
---

# Human interface device

A **human interface device** (**HID**) is a type of computer device usually used by humans that takes input from or provides output to humans.

The term "HID" most commonly refers to the USB HID specification. The term was coined by Mike Van Flandern of Microsoft when he proposed that the USB committee create a Human Input Device class working group. The working group was renamed as the Human Interface Device class at the suggestion of Tom Schmidt of DEC because the proposed standard supported bidirectional communication.

## HID standard

A working committee with representatives from several prominent companies developed the HID standard. The list of participants appears in the "Device Class Definition for Human Interface Devices (HID)" document. The concept of a self-describing extensible protocol initially came from Mike Van Flandern and Manolito Adan while working on a project named "Raptor" at Microsoft, and independently from Steve McGowan, who worked on a "SIM" project that defined a device protocol for the VFX1 VR Headset and its peripherals based on ACCESS.bus while at Forte Technologies. SIM was also self-describing and extensible, however it was more focused on SIMulation devices used for VR and motion capture. After comparing notes at a Consumer Game Developer Conference, Steve and Mike agreed to collaborate on a new standard for the emerging Universal Serial Bus (USB).

## Other protocols using HID

Since HID's original definition over USB, HID is now also used in other computer communication buses. This enables HID devices that traditionally were only found on USB to also be used on alternative buses. This is done since existing support for USB HID devices can typically be adapted much faster than having to invent an entirely new protocol to support mouse, touchpad, keyboards, and the like. Known buses that use HID are:

- Bluetooth HID – Used for mouse and keyboards that are connected via Bluetooth
- Serial HID – Used in Microsoft's Windows Media Center PC remote control receivers.
- Zigbee input device – Zigbee (RF4CE) supports HID devices through the Zigbee input device profile.
- HID over I²C – Used for embedded devices in Microsoft Windows 8
- HID over SPI – Developed by Microsoft for faster, lower latency fixed-device communications
- HID over GPIO – Used for embedded devices in Microsoft Windows 10
- HOGP (HID over GATT) – Used for HID devices connected using Bluetooth Low Energy technology
