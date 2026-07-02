---
title: "Wi-Fi 7"
source: https://en.wikipedia.org/wiki/IEEE_802.11be
domain: wifi-7
license: CC-BY-SA-4.0
tags: wi-fi 7, 802.11be standard, multi-link operation, extremely high throughput
fetched: 2026-07-02
---

# Wi-Fi 7

(Redirected from

IEEE 802.11be

)

| Gen. | IEEE standard | Adopt. | Link rate (Mbit/s) | RF (GHz) |   |   |
|---|---|---|---|---|---|---|
| 2.4 | 5 | 6 |   |   |   |   |
| — | 802.11 | 1997 | 1–2 | (Yes) |   |   |
| 802.11b | 1999 | 1–11 | (Yes) |   |   |   |
| 802.11a | 6–54 |   | (Yes) |   |   |   |
| 802.11g | 2003 | (Yes) |   |   |   |   |
| Wi-Fi 4 | 802.11n | 2009 | 6.5–600 | (Yes) | (Yes) |   |
| Wi-Fi 5 | 802.11ac | 2013 | 6.5–6,933 |   | (Yes) |   |
| Wi-Fi 6 | 802.11ax | 2021 | 0.4–9,608 | (Yes) | (Yes) |   |
| Wi-Fi 6E | (Yes) | (Yes) | (Yes) |   |   |   |
| Wi-Fi 7 | 802.11be | 2024 | 0.4–23,059 | (Yes) | (Yes) | (Yes) |
| Wi-Fi 8 | 802.11bn | TBA | (Yes) | (Yes) | (Yes) |   |

**IEEE 802.11be-2024** or **802.11be**, dubbed *Extremely High Throughput (EHT)*, is a wireless networking standard in the IEEE 802.11 set of protocols which is designated **Wi-Fi 7** by the Wi-Fi Alliance. It is built upon Wi-Fi 6 (IEEE 802.11ax), focusing on WLAN indoor and outdoor operation with stationary and pedestrian speeds in the 2.4, 5, and 6 GHz frequency bands.

In a single band, throughput reaches a theoretical maximum of 23 Gbit/s, although actual results are much lower.

Development of the 802.11be amendment began with an initial draft in March 2021 and the final version was published on 22 July 2025. Despite this, numerous products were announced in 2022 based on draft standards, with retail availability in early 2023. On 8 January 2024, the Wi-Fi Alliance introduced its *Wi-Fi Certified 7* program to certify Wi-Fi 7 devices as the technical requirements were essentially complete.

## Core features

The following are core features that have been approved as of Draft 3.0:

- 4096-QAM (4K-QAM) enables each symbol to carry 12 bits rather than 10 bits, resulting in 20% higher theoretical transmission rates than Wi-Fi 6's 1024-QAM, at the same symbol or baud rate. This feature is **optional** for Wi-Fi 7 certification.
- Contiguous and non-contiguous 320/160+160 MHz and 240/160+80 MHz bandwidth. This feature is **optional** for Wi-Fi 7 certification.
- Multi-link Operation (MLO), a feature that increases capacity by simultaneously sending and receiving data across different frequency bands and channels. (2.4 GHz, 5 GHz, 6 GHz). This feature is **mandatory** for Wi-Fi 7 certification. Wi-Fi 7 builds on the technology of Wi-Fi 6 through the introduction of Multi-Link Operation (MLO), allowing users to connect to 2.4 GHz, 5 GHz, and 6 GHz bands simultaneously.
- 8 spatial streams and Multiple Input Multiple Output (MIMO) protocol enhancements. (Initial 16 but removed from the specs in 2024).
- Flexible Channel Utilization – Interference currently can negate an entire Wi-Fi channel. With preamble puncturing, a portion of the channel that is affected by interference can be blocked off while continuing to use the rest of the channel. This feature is **mandatory** for Wi-Fi 7 certification.
- Multiple Resource Unit (MRU) – Improves OFDMA technology from Wi-Fi 6, allowing a single user to have multiple Resource Units. This feature is **mandatory** for Wi-Fi 7 certification.

## Candidate features

The main candidate features mentioned in the 802.11be Project Authorization Request (PAR) are:

- Multi-Access Point (AP) Coordination (e.g. coordinated and joint transmission),
- Enhanced link adaptation and retransmission protocol (e.g. Hybrid Automatic Repeat Request (HARQ)).
- If needed, adaptation to regulatory rules specific to 6 GHz spectrum.
- Integrating Time-Sensitive Networking (TSN) IEEE 802.1Q extensions for low-latency real-time traffic:
  - IEEE 802.1AS timing and synchronization
  - IEEE 802.11aa MAC Enhancements for Robust Audio Video Streaming (Stream Reservation Protocol over IEEE 802.11)
  - IEEE 802.11ak Enhancements for Transit Links Within Bridged Networks (802.11 links in 802.1Q networks)
  - Bounded latency: credit-based (IEEE 802.1Qav) and cyclic/time-aware traffic shaping (IEEE 802.1Qch/Qbv), asynchronous traffic scheduling (IEEE 802.1Qcr-2020)
  - IEEE 802.11ax Scheduled Operation extensions for reduced jitter/latency

## Additional features

Apart from the features mentioned in the PAR, there are newly introduced features:

- Frame formats with improved forward-compatibility.
- Enhanced resource allocation in OFDMA.
- Implicit channel sounding, optimized to require less airtime.
- Support for direct links, managed by an access point.

## Rate set

Modulation and coding schemes

MCS index

Modulation type

Coding rate

Data rate (Mbit/s)

20 MHz channels

40 MHz channels

80 MHz channels

160 MHz channels

320 MHz channels

3200 ns GI

1600 ns GI

800 ns GI

3200 ns GI

1600 ns GI

800 ns GI

3200 ns GI

1600 ns GI

800 ns GI

3200 ns GI

1600 ns GI

800 ns GI

3200 ns GI

1600 ns GI

800 ns GI

0

BPSK

1/2

7

8

9

15

16

17

31

34

36

61

68

72

123

136

144

1

QPSK

1/2

15

16

17

29

33

34

61

68

72

122

136

144

245

272

288

2

QPSK

3/4

22

24

26

44

49

52

92

102

108

184

204

216

368

408

432

3

16-QAM

1/2

29

33

34

59

65

69

123

136

144

245

272

288

490

544

577

4

16-QAM

3/4

44

49

52

88

98

103

184

204

216

368

408

432

735

817

865

5

64-QAM

2/3

59

65

69

117

130

138

245

272

288

490

544

576

980

1089

1153

6

64-QAM

3/4

66

73

77

132

146

155

276

306

324

551

613

649

1103

1225

1297

7

64-QAM

5/6

73

81

86

146

163

172

306

340

360

613

681

721

1225

1361

1441

8

256-QAM

3/4

88

98

103

176

195

207

368

408

432

735

817

865

1470

1633

1729

9

256-QAM

5/6

98

108

115

195

217

229

408

453

480

817

907

961

1633

1815

1922

10

1024-QAM

3/4

110

122

129

219

244

258

459

510

540

919

1021

1081

1838

2042

2162

11

1024-QAM

5/6

122

135

143

244

271

287

510

567

600

1021

1134

1201

2042

2269

2402

12

4096-QAM

3/4

131

146

155

263

293

310

551

613

649

1103

1225

1297

2205

2450

2594

13

4096-QAM

5/6

146

163

172

293

325

344

613

681

721

1225

1361

1441

2450

2722

2882

14

BPSK-DCM-DUP

1/2

7

8

9

15

17

18

31

34

36

15

BPSK-DCM

1/2

4

4

4

7

8

9

15

17

18

31

34

36

61

68

72

## Comparison

Frequency

range,

or type

PHY

Protocol

Release

date

Freq­uency band

Channel width

Stream

data rate

Max.

MIMO

streams

Modulation

Approx.

range

In­door

Out­door

(GHz)

(MHz)

(

Mbit/s

)

1–7

GHz

DSSS

,

FHSS

802.11-1997

June 1997

2.4

22

1, 2

—

N/a

DSSS

,

FHSS

20 m (66 ft)

100 m (330 ft)

HR/DSSS

802.11b

September 1999

2.4

22

1, 2, 5.5, 11

—

N/a

CCK

, DSSS

35 m (115 ft)

140 m (460 ft)

OFDM

802.11a

September 1999

5

5, 10, 20

6, 9, 12, 18, 24, 36, 48, 54

(for 20

MHz bandwidth,

divide by 2 and 4 for 10 and 5

MHz)

—

N/a

OFDM

35 m (115 ft)

120 m (390 ft)

802.11j

November 2004

4.9, 5.0

?

?

802.11y

November 2008

3.7

?

5,000 m (16,000 ft)

802.11p

July 2010

5.9

200 m

1,000 m (3,300 ft)

802.11bd

December 2022

5.9, 60

500 m

1,000 m (3,300 ft)

ERP

-OFDM

802.11g

June 2003

2.4

38 m (125 ft)

140 m (460 ft)

HT

-OFDM

802.11n

(

Wi-Fi 4

)

October 2009

2.4, 5

20

Up to 288.8

4

MIMO-OFDM

(64-

QAM

)

70 m (230 ft)

250 m (820 ft)

40

Up to 600

VHT

-OFDM

802.11ac

(

Wi-Fi 5

)

December 2013

5

20

Up to 693

8

DL

MU-MIMO

OFDM

(256-

QAM

)

35 m (115 ft)

?

40

Up to 1,600

80

Up to 3,467

160

Up to 6,933

HE

-OFDMA

802.11ax

(

Wi-Fi 6

,

Wi-Fi 6E

)

May 2021

2.4, 5, 6

20

Up to 1,147

8

UL/DL

MU-MIMO

OFDMA

(1024-

QAM

)

30 m (98 ft)

120 m (390 ft)

40

Up to 2,294

80

Up to 5,500

80+80

Up to 11,000

EHT

-OFDMA

802.11be

(

Wi-Fi 7

)

Sep 2024

2.4, 5, 6

80

Up to 5,764

8

UL/DL

MU-MIMO

OFDMA

(4096-

QAM

)

30 m (98 ft)

120 m (390 ft)

160

(80+80)

Up to 11,500

240

(160+80)

Up to 14,282

320

(160+160)

Up to 23,059

UHR

802.11bn

(

Wi-Fi 8

)

May 2028

(

est.

)

2.4, 5, 6

320

Up to

23,059

8

Multi-link

MU-MIMO

OFDM

(4096-

QAM

)

?

?

WUR

802.11ba

October 2021

2.4, 5

4, 20

0.0625, 0.25

(62.5

kbit/s, 250

kbit/s)

—

N/a

OOK

(multi-carrier OOK)

?

?

mmWave

(

WiGig

)

DMG

802.11ad

December 2012

60

2,160

(2.16

GHz)

Up to 8,085

(8

Gbit/s)

—

N/a

OFDM

,

single

carrier, low-power single carrier

3.3 m (11 ft)

?

802.11aj

April 2018

60

1,080

Up to 3,754

(3.75

Gbit/s)

—

N/a

single

carrier, low-power single carrier

?

?

CMMG

802.11aj

April 2018

45

540,

1,080

Up to 15,015

(15

Gbit/s)

4

OFDM

, single

carrier

?

?

EDMG

802.11ay

July 2021

60

Up to 8,640

(8.64

GHz)

Up to 303,336

(303

Gbit/s)

8

OFDM

, single

carrier

10

m (33

ft)

100

m (328

ft)

Sub 1 GHz (

IoT

)

TVHT

802.11af

February 2014

0.054–

0.79

6, 7, 8

Up to 568.9

4

MIMO-OFDM

?

?

S1G

802.11ah

May 2017

0.7, 0.8,

0.9

1–16

Up to 8.67

(@2

MHz)

4

?

?

Light

(

Li-Fi

)

LC

(

VLC

/

OWC

)

802.11bb

November 2023

800–1000 nm

20

Up to 9.6

Gbit/s

—

N/a

O-

OFDM

?

?

IR

(

IrDA

)

802.11-1997

June 1997

850–900 nm

?

1, 2

—

N/a

PPM

?

?

802.11 Standard rollups

802.11-2007 (802.11ma)

March 2007

2.4, 5

Up to 54

DSSS

,

OFDM

802.11-2012 (802.11mb)

March 2012

2.4, 5

Up to 150

DSSS

,

OFDM

802.11-2016 (802.11mc)

December 2016

2.4, 5, 60

Up to 866.7 or 6,757

DSSS

,

OFDM

802.11-2020 (802.11md)

December 2020

2.4, 5, 60

Up to 866.7 or 6,757

DSSS

,

OFDM

802.11-2024 (802.11me)

September 2024

2.4, 5, 6, 60

Up to 9,608 or 303,336

DSSS

,

OFDM

1. This is obsolete, and support for this might be subject to removal in a future revision of the standard
2. For Japanese regulation.
3. IEEE 802.11y-2008 extended operation of 802.11a to the licensed 3.7 GHz band. Increased power limits allow a range up to 5,000 m. As of 2009, it is only being licensed in the United States by the FCC.
4. Based on short guard interval; standard guard interval is ~10% slower. Rates vary widely based on distance, obstructions, and interference.
5. For single-user cases only, based on default guard interval which is 0.8 microseconds. Since multi-user via OFDMA has become available for 802.11ax, these may decrease. Also, these theoretical values depend on the link distance, whether the link is line-of-sight or not, interferences and the multi-path components in the environment.
6. The default guard interval is 0.8 microseconds. However, 802.11ax extended the maximum available guard interval to 3.2 microseconds, in order to support outdoor communications, where the maximum possible propagation delay is larger compared to Indoor environments.
7. Wake-up Radio (WUR) Operation.
8. For Chinese regulation.

## 802.11be Task Group

The 802.11be Task Group is led by individuals affiliated with Qualcomm, Intel, and Broadcom. Those affiliated with Huawei, Maxlinear, NXP, and Apple also have senior positions.

## Commercial availability

### Hardware

The Wi-Fi Alliance maintains a list of Wi-Fi 7 certified devices.

### Software

Android 13 and higher provide support for Wi-Fi 7.

The Linux 6.2 kernel provides support for Wi-Fi 7 devices. The 6.4 kernel added Wi-Fi 7 mesh support. Linux 6.5 included significant driver support by Intel engineers, particularly support for MLO.

Support for Wi-Fi 7 was added to Windows 11, as of build 26063.1.
