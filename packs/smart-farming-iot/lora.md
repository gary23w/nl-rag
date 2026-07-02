---
title: "LoRa"
source: https://en.wikipedia.org/wiki/LoRa
domain: smart-farming-iot
license: CC-BY-SA-4.0
tags: digital agriculture, wireless sensor network, lora, farm management
fetched: 2026-07-02
---

# LoRa

**LoRa** (from "long range") is a physical proprietary radio communication technique based on spread spectrum modulation. LoRa can be thought of as a radio signal technology, similar to Wi-Fi or cellular.

The technology is primarily used for applications where small amounts of data need to be transmitted infrequently from hard-to-reach locations.

LoRa uses license-free sub-gigahertz radio frequency bands EU433 (433.050-434.790 MHz) or EU868 (863–870/873 MHz) in Europe; AU915/AS923-1 (915–928 MHz) in South America; US915 (902–928 MHz) in North America; IN865 (865–867 MHz) in India; and AS923 (915–928 MHz) in Asia; LoRa enables long-range transmissions with low power consumption. The technology covers the physical layer, while other technologies and protocols such as LoRaWAN cover the upper layers. It can achieve data rates between 0.3 kbit/s and 27 kbit/s, depending upon the spreading factor.

## Description

LoRa uses a proprietary spread spectrum modulation that is similar to and a derivative of chirp spread spectrum (CSS) modulation. Each symbol is represented by a cyclic shifted chirp over the bandwidth centered around the base frequency.

The spreading factor (SF) is a selectable radio parameter from 5 to 12 and represents the number of bits sent per symbol and in addition determines how much the information is spread over time. There are $M=2^{\mathrm {SF} }$ different initial frequencies of the cyclic shifted chirp across the bandwidth around the center frequency.

The symbol rate is determined by $R_{s}=B/M$ . LoRa can tradeoff data rate for sensitivity (assuming a fixed channel bandwidth B ) by selecting the SF, i.e. the amount of spread used. A lower SF corresponds to a higher data rate but a worse sensitivity, a higher SF implies a better sensitivity but a lower data rate. Compared to lower SF, sending the same amount of data with higher SF needs more transmission time, known as time-on-air. More time-on-air means that the modem is transmitting for a longer time and consuming more energy.

Typical LoRa modems support transmit powers up to +22 dBm. However, the regulations of the respective country may additionally limit the allowed transmit power. Higher transmit power results in higher signal power at the receiver and hence a higher link budget, but at the cost of consuming more energy. There are measurement studies of LoRa performance with regard to energy consumption, communication distances, and medium access efficiency. According to the LoRa Development Portal, the range provided by LoRa can be up to 3 miles (4.8 km) in urban areas, and up to 10 miles (16 km) or more in rural areas (line of sight).

In addition, LoRa uses forward error correction coding to improve resilience against interference. LoRa's high range is characterized by high wireless link budgets of around 155 dB to 170 dB.

Range extenders for LoRa are called LoRaX.

## Applications

LoRa applications:

- Meshtastic — an open source mesh network protocol that uses LoRa flood messaging
- MeshCore — open source mesh network protocol that uses LoRa with more structured routing than Meshtastic
- Reticulum — open source mesh network that can use a multitude of transports, including LoRa
- LoRaWAN — a low-power, wide-area network (LPWAN) protocol that wirelessly connects battery-operated devices to the Internet. Uses LoRa.
  - Helium Network — LoRaWAN protocol paired with blockchain technology
- ExpressLRS — open source UAV remote control protocol that uses LoRa, widely used in FPV drones
- Amazon Sidewalk — a mesh wireless network developed by Amazon. Uses LoRa for long range
