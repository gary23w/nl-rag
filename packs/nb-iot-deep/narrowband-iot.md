---
title: "Narrowband IoT"
source: https://en.wikipedia.org/wiki/Narrowband_IoT
domain: nb-iot-deep
license: CC-BY-SA-4.0
tags: nb-iot protocol, narrowband iot, cellular lpwan, 3gpp machine-type communication
fetched: 2026-07-02
---

# Narrowband IoT

**Narrowband Internet of things** (**NB-IoT**) is a low-power wide-area network (LPWAN) radio technology standard developed by 3GPP for cellular network devices and services. The specification was frozen in 3GPP Release 13 (LTE Advanced Pro), in June 2016. Other 3GPP IoT technologies include eMTC (enhanced Machine-Type Communication) and EC-GSM-IoT.

NB-IoT focuses specifically on indoor coverage, long battery life, and high connection density. NB-IoT uses a subset of the LTE standard, but limits the bandwidth to a single narrow-band of 200 kHz. It uses OFDM modulation for downlink communication and SC-FDMA for uplink communications. IoT applications which require more frequent communications will be better served by LTE-M, which has no duty cycle limitations operating on the licensed spectrum. LTE-M is also more suited for applications in moving devices.

In March 2019, the Global Mobile Suppliers Association (GSA) announced that over 100 operators had either NB-IoT or LTE-M networks. This number had risen to 142 deployed/launched networks by September 2019.

## 3GPP LPWAN standards

LTE Cat 1

LTE Cat 1 bis

LTE-M

NB-IoT

EC-GSM-IoT

LC-LTE/MTCe

eMTC

LTE Cat 0

LTE Cat M1

LTE Cat M2

non-BL

LTE Cat NB1

LTE Cat NB2

3GPP release

Release 8

Release 13

Release 12

Release 13

Release 14

Release 13

Release 14

Release 13

Downlink peak rate

10 Mbit/s

1 Mbit/s

~4 Mbit/s

26 kbit/s

127 kbit/s

474 kbit/s (EDGE)

2 Mbit/s (EGPRS2B)

Uplink peak rate

5 Mbit/s

~7 Mbit/s

66 kbit/s (multi-tone)

16.9 kbit/s (single-tone)

159 kbit/s

Latency

50–100 ms

not deployed

10–15ms

1.6–10 s

700 ms – 2 s

Number of antennas

2

1

1–2

Duplex mode

Full duplex

Full or half duplex

Half duplex

Device receive bandwidth

1.4–20

MHz

1.4

MHz

5

MHz

180

kHz

200

kHz

Receiver chains

2 (

MIMO

)

1 (

SISO

)

1–2

Device transmit power

23

dBm

20 / 23 dBm

14 / 20 / 23 dBm

23 / 33 dBm

## Deployments

As of March 2019 GSA identified:

- 149 operators in 69 countries investing in one or both of the NB-IoT and LTE-M network technologies
- 104 of those operators in 53 countries had deployed/launched at least one of the NB-IoT or LTE-M technologies of those, 20 operators in 19 countries had deployed/launched both NB-IoT and LTE-M
- 22 countries are now home to deployed/launched NB-IoT and LTE-M networks
- 29 countries are home to deployed/launched NB-IoT networks only
- Two countries are home to deployed/launched LTE-M networks only
- 141 operators in 69 countries investing in NB-IoT networks; 90 of those operators in 51 countries had deployed/launched their networks
- 60 operators in 35 countries investing in LTE-M networks; 34 of those operators in 24 countries had deployed/launched their networks

## Devices and modules

The 3GPP-compliant LPWA device ecosystem continues to grow. In April 2019, GSA identified 210 devices supporting either Cat-NB1/NB-2 or Cat-M1 – more than double the number in its GAMBoD database at the end of March 2018. This figure had risen a further 50% by September 2019, with a total of 303 devices identified as supporting either Cat-M1, Cat-NB1 (NB-IoT) or Cat-NB2. Of these, 230 devices support Cat-NB1 (including known variants) and 198 devices support Cat-M1 (including known variants). The split of devices (as of September 2019) was 60.4% modules, 25.4% asset trackers, and 5.6% routers, with data loggers, femtocells, smart-home devices, and smart watches, USB modems, and vehicle on-board units (OBUs), making up the balance.

In 2018 first NB-IoT data loggers and other certified devices started to appear. For example ThingsLog released their first CE certified single channel NB-IoT data logger on Tindie in late 2018.

To integrate NB-IoT into a maker board for IoT developments, SODAQ, a Dutch IoT hardware and software engineering company, crowdfunded an NB-IoT shield on Kickstarter. They then went on to partner with module manufacturer u-blox to create maker boards with NB-IoT and LTE-M integrated.

Since 2021, there also is a cheap all-in-one NB-IoT solution available to the general public developed by the Chinese manufacturer Ai-Thinker.

At the beginning of 2023 the Belgian company DPTechnics released the Walter IoT board which combines an ESP32-S3 together with a Sequans Monarch 2 NB-IoT/LTE-M platform. The board is focused on long-term availability and includes a GNSS receiver.
