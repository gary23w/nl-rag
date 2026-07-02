---
title: "Wi-Fi 6"
source: https://en.wikipedia.org/wiki/Wi-Fi_6
domain: wifi-6
license: CC-BY-SA-4.0
tags: wi-fi 6, 802.11ax standard, wireless lan, ofdma channel access
fetched: 2026-07-02
---

# Wi-Fi 6

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

**IEEE 802.11ax-2021** or **802.11ax**, is an IEEE standard from the Wi-Fi Alliance, for wireless networks (WLANs). The standard is marketed as **Wi-Fi 6**. It operates in the 2.4 GHz and 5 GHz bands, with an extended version, **Wi-Fi 6E**, that adds the 6 GHz band; these are license-exempt ISM bands. It is an upgrade from Wi-Fi 5 (IEEE 802.11ac), with improvements for better performance in crowded places.

This standard aims to boost throughput in crowded places like offices and malls. Though the nominal data rate is only 37% higher than that of Wi-Fi 5, the throughput increases by at least four times, making it more efficient and reducing latency by 75%. The quintupling of overall throughput is made possible by higher spectral efficiency.

Wi-Fi 6 has a main feature called OFDMA, similar to how cellular common-carrier networks work. This brings better spectrum use, improved power control to avoid interference, and enhancements like 1024‑QAM, MIMO and MU-MIMO for faster speeds. There are also reliability improvements such as lower power consumption and security protocols like Target Wake Time and WPA3.

The 802.11ax standard was approved on September 1, 2020, with Draft 8 getting 95% approval. Subsequently, on February 1, 2021, the standard received official endorsement from the IEEE Standards Board.

## Rate set

Modulation and coding schemes

MCS

index

Modulation

type

Coding

rate

Data rate (Mbit/s)

Channel width (MHz)

20

40

80

160

Guard Interval (μs)

1.6

0.8

1.6

0.8

1.6

0.8

1.6

0.8

0

BPSK

1/2

8

8.6

16

17.2

34

36.0

68

72

1

QPSK

1/2

16

17.2

33

34.4

68

72.1

136

144

2

QPSK

3/4

24

25.8

49

51.6

102

108.1

204

216

3

16-QAM

1/2

33

34.4

65

68.8

136

144.1

272

288

4

16-QAM

3/4

49

51.6

98

103.2

204

216.2

408

432

5

64-QAM

2/3

65

68.8

130

137.6

272

288.2

544

576

6

64-QAM

3/4

73

77.4

146

154.9

306

324.4

613

649

7

64-QAM

5/6

81

86.0

163

172.1

340

360.3

681

721

8

256-QAM

3/4

98

103.2

195

206.5

408

432.4

817

865

9

256-QAM

5/6

108

114.7

217

229.4

453

480.4

907

961

10

1024-QAM

3/4

122

129.0

244

258.1

510

540.4

1021

1081

11

1024-QAM

5/6

135

143.4

271

286.8

567

600.5

1134

1201

*Notes*

1. MCS 9 is not applicable to all combinations of channel width and spatial stream count.
2. Per spatial stream.

## MU-MIMO and OFDMA

With the previous generation Wi-Fi 5, multi-user MIMO was introduced, which is a spatial multiplexing technique. MU-MIMO allows the access point to form beams towards each client, while transmitting information simultaneously. By doing so, the interference between clients is reduced, and the overall throughput is increased, since multiple clients can receive data simultaneously.

With Wi-Fi 6, a similar multiplexing is introduced in the *frequency-division multiplexing*: OFDMA. With OFDMA, multiple clients are assigned to different Resource Units in the available spectrum. By doing so, an 80 MHz channel can be split into multiple Resource Units, so that multiple clients receive different types of data over the same spectrum, simultaneously.

To support OFDMA, Wi-Fi 6 needs four times as many subcarriers as Wi-Fi 5. Specifically, for 20, 40, 80, and 160 MHz channels, the 802.11ac standard has, respectively, 64, 128, 256 and 512 subcarriers while the 802.11ax standard has 256, 512, 1024, and 2048 subcarriers. Since the available bandwidths have not changed and the number of subcarriers increases by a factor of four, the subcarrier spacing is reduced by the same factor. This introduces OFDM symbols that are four times longer: with Wi-Fi 5, an OFDM symbol takes 3.2 microseconds to transmit. With Wi-Fi 6, it takes 12.8 microseconds (both without guard intervals).

## Technical improvements

The 802.11ax amendment brings several key improvements over 802.11ac. While 802.11ac only uses the 5 GHz band, which is a bit over 700 MHz wide, 802.11ax also allows the use of the 2.4 GHz band of some earlier protocols, less than 100 MHz wide, and the larger 6 GHz band, about 1200 MHz wide. Wi-Fi 6E adds to Wi‑Fi 6 the use of the 6 GHz band and, thereby, channels that are 160 MHz wide without the restrictions of Dynamic Frequency Selection that apply to all 160 MHz channels in the 5 GHz band. The number and selection of channels available depends on the country a given Wi-Fi 6 network operates in. To meet the goal of supporting dense 802.11 deployments, the following features have been approved.

| Feature | Wi-Fi 5 | Wi-Fi 6 | Comment |
|---|---|---|---|
| OFDMA | *not available* | Centrally controlled medium access with dynamic assign­ment of 26, 52, 106, 242(?), 484(?), or 996(?) tones per station. Each tone consists of a single subcarrier of 78.125 kHz bandwidth. Therefore, a single OFDMA transmission is between 2.03125 MHz and ca. 80 MHz wide. | OFDMA segregates the spectrum in time-frequency resource units (RUs). A central coordinating entity (the AP in 802.11ax) assigns RUs for reception or transmission to associated stations. Through the central scheduling of the RUs, contention overhead can be avoided, which increases efficiency in scenarios of dense deployments. |
| Multi-user MIMO (MU-MIMO) | Available in Downlink direction | Available in Downlink and Uplink direction | With downlink MU-MIMO an AP may transmit concurrently with multiple stations, and with uplink MU-MIMO an AP may simultaneously receive from multiple stations. Whereas OFDMA separates receivers to different RUs, with MU-MIMO the devices are separated into different spatial streams. In 802.11ax, MU-MIMO and OFDMA can be used simultaneously. To enable uplink MU transmissions, the AP transmits a new control frame (Trigger) which contains scheduling information (RU allocations for stations, and the modulation and coding scheme (MCS) that shall be used for each station). Furthermore, a Trigger also provides synchronization for an uplink transmission, since the transmission starts SIFS after the end of a Trigger. |
| Trigger-based Random Access | *not available* | Allows performing UL OFDMA transmissions by stations which are not allocated RUs directly | In a Trigger frame, the AP specifies scheduling information about subsequent UL MU transmission. However, several RUs can be assigned for random access. Stations which are not assigned RUs directly can perform transmissions within RUs assigned for random access. To reduce collision probability (i.e. situation when two or more stations select the same RU for transmission), the 802.11ax amendment specifies a special OFDMA back-off procedure. Random access is favorable for transmitting buffer status reports when the AP has no information about pending UL traffic at a station. |
| Spatial frequency reuse | *not available* | Coloring enables devices to differentiate transmissions in their own network from trans­missions in neighboring net­works. Adaptive power and sensitivity thresholds allow dynamically adjusting transmit power and signal detection threshold to increase spatial reuse. | Without spatial reuse capabilities devices refuse transmitting concurrently with transmissions in neighboring networks. With basic service set coloring (BSS coloring), a wireless transmission is marked at its very beginning, helping surrounding devices to decide if a simultaneous use of the wireless medium is permissible. A station is allowed to consider the wireless medium idle and start a new transmission even if the detected signal level from a neighboring network exceeds the legacy signal detection threshold, provided that the transmit power for the new transmission is appropriately decreased. |
| NAV | Single NAV | Dual NAVs | In dense deployment scenarios, the NAV (network allocation vector) value set by a frame from one network may be easily reset by a frame from another network, which leads to misbehavior and collisions. To avoid this, each 802.11ax station will maintain two separate NAVs: One NAV is modified by frames from a network the station is associated with, while the other NAV is modified by frames from overlapping networks. |
| Target Wake Time (TWT) | *not available* | TWT reduces power consumption and medium access contention. | TWT is a concept developed in 802.11ah. It allows devices to wake up at times other than the periodic beacon transmission time. Furthermore, the AP may group devices with various TWT periods, thereby reducing the number of devices contending simultaneously for the wireless medium. |
| Fragmentation | Static | Dynamic | With static fragmentation, all fragments of a data packet are of equal size, except for the last fragment. With dynamic fragmentation, a device may fill available RUs of other opportunities to transmit up to the available maximum duration. Thus, dynamic fragmentation helps reduce overhead. |
| Guard interval duration | 0.4 or 0.8 μs | 0.8, 1.6 or 3.2 μs | Extended guard interval durations allow for better protection against signal delay spread as it occurs in outdoor environments. |
| Symbol duration | 3.2 μs | 12.8 μs | Since the subcarrier spacing is reduced by a factor of four, the OFDM symbol duration is increased by a factor of four as well. Extended symbol durations allow for increased efficiency. |
| Frequency bands | 5 GHz only | 2.4 and 5 GHz | 802.11ac falls back to 802.11n for the 2.4 GHz band. |

## Adoption

Following the ratification of the IEEE 802.11ax standard in February 2021, Wi-Fi 6 saw rapid adoption across consumer and enterprise devices. The Wi-Fi Alliance began certifying Wi-Fi 6 devices under its *Wi-Fi CERTIFIED 6* program in September 2019, ahead of the standard's formal approval. Major smartphone, laptop, and router manufacturers incorporated Wi-Fi 6 support into their product lines beginning in 2020.

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
