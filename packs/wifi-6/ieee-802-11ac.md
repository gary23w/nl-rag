---
title: "IEEE 802.11ac"
source: https://en.wikipedia.org/wiki/IEEE_802.11ac
domain: wifi-6
license: CC-BY-SA-4.0
tags: wi-fi 6, 802.11ax standard, wireless lan, ofdma channel access
fetched: 2026-07-02
---

# IEEE 802.11ac

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

**IEEE 802.11ac**, formally **IEEE 802.11ac-2013** and also simply called **802.11ac**, is a wireless networking standard in the IEEE 802.11 set of protocols (which is part of the Wi-Fi networking family), providing high-throughput wireless local area networks (WLANs) on the 5 GHz band. The standard has been retroactively labelled as **Wi-Fi 5** by Wi-Fi Alliance.

The specification has multi-station throughput of at least 1.1 gigabit per second (1.1 Gbit/s) and single-link throughput of at least 500 megabits per second (0.5 Gbit/s). This is accomplished by extending the air-interface concepts embraced by 802.11n: wider RF bandwidth (up to 160 MHz), more MIMO spatial streams (up to eight), downlink multi-user MIMO (up to four clients), and high-density modulation (up to 256-QAM).

The Wi-Fi Alliance separated the introduction of 802.11ac wireless products into two phases ("waves"), named "Wave 1" and "Wave 2". From mid-2013, the alliance started certifying **Wave 1** 802.11ac products shipped by manufacturers, based on the IEEE 802.11ac Draft 3.0 (the IEEE standard was not finalized until later that year). Subsequently, in 2016, Wi-Fi Alliance introduced the **Wave 2** certification, which includes additional features like MU-MIMO (downlink only), 160 MHz channel width support, support for more 5 GHz channels, and four spatial streams (with four antennas; compared to three in Wave 1 and 802.11n, and eight in IEEE's 802.11ax specification). It meant Wave 2 products would have higher bandwidth and capacity than Wave 1 products.

## New technologies

New technologies introduced with 802.11ac include the following:

- Extended channel binding
  - Optional 160 MHz and mandatory 80 MHz channel bandwidth for stations; cf. 40 MHz maximum in 802.11n.
- More MIMO spatial streams
  - Support for up to eight spatial streams (vs. four in 802.11n)
- Downlink multi-user MIMO (MU-MIMO, allows up to four simultaneous downlink MU-MIMO clients)
  - Multiple STAs, each with one or more antennas, transmit or receive independent data streams simultaneously.
    - Space-division multiple access (SDMA): streams not separated by frequency, but instead resolved spatially, analogous to 11n-style MIMO.
  - Downlink MU-MIMO (one transmitting device, multiple receiving devices) included as an optional mode.
- Modulation
  - 256-QAM, rate 3/4 and 5/6, added as optional modes (vs. 64-QAM, rate 5/6 maximum in 802.11n).
  - Some vendors offer a non-standard 1024-QAM mode, providing 25% higher data rate compared to 256-QAM
- Other elements/features
  - Beamforming with standardized sounding and feedback for compatibility between vendors (non-standard in 802.11n made it hard for beamforming to work effectively between different vendor products)
  - MAC modifications (mostly to support above changes)
  - Coexistence mechanisms for 20, 40, 80, and 160 MHz channels, 11ac and 11a/n devices
  - Adds four new fields to the PPDU header identifying the frame as a very high throughput (VHT) frame as opposed to 802.11n's high throughput (HT) or earlier. The first three fields in the header are readable by legacy devices to allow coexistence
  - DFS was mandated between channels 52 and 144 for 5 GHz to reduce interference with weather radar systems using the same frequency band.

## Features

### Mandatory

- Borrowed from the 802.11a/802.11g specifications:
  - 800 ns regular guard interval
  - Binary convolutional coding (BCC)
  - Single spatial stream
- Newly introduced by the 802.11ac specification:
  - 80 MHz channel bandwidths

### Optional

- Borrowed from the 802.11n specification:
  - Two to four spatial streams
  - Low-density parity-check code (LDPC)
  - Space–time block coding (STBC)
  - Transmit beamforming (TxBF)
  - 400 ns short guard interval (SGI)
- Newly introduced by the 802.11ac specification:
  - five to eight spatial streams
  - 160 MHz channel bandwidths (contiguous 80+80)
  - 80+80 MHz channel bonding (discontiguous 80+80)
  - MCS 8/9 (256-QAM)

## New scenarios and configurations

The single-link and multi-station enhancements supported by 802.11ac enable several new WLAN usage scenarios, such as simultaneous streaming of HD video to multiple clients throughout the home, rapid synchronization and backup of large data files, wireless display, large campus/auditorium deployments, and manufacturing floor automation.

To fully utilize their WLAN capacities, 802.11ac access points and routers have sufficient throughput to require the inclusion of a USB 3.0 interface to provide various services such as video streaming, FTP servers, and personal cloud services. With storage locally attached through USB 2.0, filling the bandwidth made available by 802.11ac was not easily accomplished.

### Example configurations

All rates assume 256-QAM, rate 5/6:

| Scenario | Typical client form factor | PHY link rate | Aggregate capacity (speed) |
|---|---|---|---|
| One-antenna AP, one-antenna STA, 80 MHz | Handheld | 433 Mbit/s | 433 Mbit/s |
| Two-antenna AP, two-antenna STA, 80 MHz | Tablet, laptop | 867 Mbit/s | 867 Mbit/s |
| One-antenna AP, one-antenna STA, 160 MHz | Handheld | 867 Mbit/s | 867 Mbit/s |
| Three-antenna AP, three-antenna STA, 80 MHz | Laptop, PC | 1.30 Gbit/s | 1.30 Gbit/s |
| Two-antenna AP, two-antenna STA, 160 MHz | Tablet, laptop | 1.73 Gbit/s | 1.73 Gbit/s |
| Four-antenna AP, four one-antenna STAs, 160 MHz (MU-MIMO) | Handheld | 867 Mbit/s to each STA | 3.39 Gbit/s |
| Eight-antenna AP, 160 MHz (MU-MIMO) one four-antenna STA one two-antenna STA two one-antenna STAs | Digital TV, set-top box, tablet, laptop, PC, handheld | 3.47 Gbit/s to four-antenna STA 1.73 Gbit/s to two-antenna STA 867 Mbit/s to each one-antenna STA | 6.93 Gbit/s |
| Eight-antenna AP, four 2-antenna STAs, 160 MHz (MU-MIMO) | Digital TV, tablet, laptop, PC | 1.73 Gbit/s to each STA | 6.93 Gbit/s |

## Wave 1 vs. Wave 2

Wave 2, referring to products introduced in 2016, offers a higher throughput than legacy Wave 1 products, those introduced starting in 2013. The maximum physical layer theoretical rate for Wave 1 is 1.3 Gbit/s, while Wave 2 can reach 2.34 Gbit/s. Wave 2 can therefore achieve 1 Gbit/s even if the real world throughput turns out to be only 50% of the theoretical rate. Wave 2 also supports a higher number of connected devices.

## Data rates and speed

Modulation and coding schemes

MCS

index

Spatial

Streams

Modulation

type

Coding

rate

Data rate (Mbit/s)

20 MHz channels

40 MHz channels

80 MHz channels

160 MHz channels

800 ns

GI

400 ns GI

800 ns GI

400 ns GI

800 ns GI

400 ns GI

800 ns GI

400 ns GI

0

1

BPSK

1/2

6.5

7.2

13.5

15

29.3

32.5

58.5

65

1

1

QPSK

1/2

13

14.4

27

30

58.5

65

117

130

2

1

QPSK

3/4

19.5

21.7

40.5

45

87.8

97.5

175.5

195

3

1

16-QAM

1/2

26

28.9

54

60

117

130

234

260

4

1

16-QAM

3/4

39

43.3

81

90

175.5

195

351

390

5

1

64-QAM

2/3

52

57.8

108

120

234

260

468

520

6

1

64-QAM

3/4

58.5

65

121.5

135

263.3

292.5

526.5

585

7

1

64-QAM

5/6

65

72.2

135

150

292.5

325

585

650

8

1

256-QAM

3/4

78

86.7

162

180

351

390

702

780

9

1

256-QAM

5/6

—

N/a

—

N/a

180

200

390

433.3

780

866.7

0

2

BPSK

1/2

13

14.4

27

30

58.5

65

117

130

1

2

QPSK

1/2

26

28.9

54

60

117

130

234

260

2

2

QPSK

3/4

39

43.3

81

90

175.5

195

351

390

3

2

16-QAM

1/2

52

57.8

108

120

234

260

468

520

4

2

16-QAM

3/4

78

86.7

162

180

351

390

702

780

5

2

64-QAM

2/3

104

115.6

216

240

468

520

936

1040

6

2

64-QAM

3/4

117

130.3

243

270

526.5

585

1053

1170

7

2

64-QAM

5/6

130

144.4

270

300

585

650

1170

1300

8

2

256-QAM

3/4

156

173.3

324

360

702

780

1404

1560

9

2

256-QAM

5/6

—

N/a

—

N/a

360

400

780

866.7

1560

1733.3

0

3

BPSK

1/2

19.5

21.7

40.5

45

87.8

97.5

175.5

195

1

3

QPSK

1/2

39

43.3

81

90

175.5

195

351

390

2

3

QPSK

3/4

58.5

65

121.5

135

263.3

292.5

526.5

585

3

3

16-QAM

1/2

78

86.7

162

180

351

390

702

780

4

3

16-QAM

3/4

117

130

243

270

526.6

585

1053

1170

5

3

64-QAM

2/3

156

173.3

324

360

702

780

1404

1560

6

3

64-QAM

3/4

175.5

195

364.5

405

789.9

877.5

1579.5

1755

7

3

64-QAM

5/6

195

216.7

405

450

877.5

975

1755

1950

8

3

256-QAM

3/4

234

260

486

540

1053

1170

2106

2340

9

3

256-QAM

5/6

—

N/a

—

N/a

540

600

1170

1300

2340

2600

0

4

BPSK

1/2

26

28.8

54

60

117.2

130

234

260

1

4

QPSK

1/2

52

57.6

108

120

234

260

468

520

2

4

QPSK

3/4

78

86.8

162

180

351.2

390

702

780

3

4

16-QAM

1/2

104

115.6

216

240

468

520

936

1040

4

4

16-QAM

3/4

156

173.2

324

360

702

780

1404

1560

5

4

64-QAM

2/3

208

231.2

432

480

936

1040

1872

2080

6

4

64-QAM

3/4

234

260

486

540

1053.2

1170

2106

2340

7

4

64-QAM

5/6

260

288.8

540

600

1170

1300

2340

2600

8

4

256-QAM

3/4

312

346.8

648

720

1404

1560

2808

3120

9

4

256-QAM

5/6

—

N/a

—

N/a

720

800

1560

1733.3

3120

3466.7

Several companies are currently offering 802.11ac chipsets with higher modulation rates: MCS-10 and MCS-11 (1024-QAM), supported by Quantenna and Broadcom. Although technically not part of 802.11ac, these new MCS indices became official in the 802.11ax standard, ratified in 2021.

160 MHz channels are unavailable in some countries due to regulatory issues that allocated some frequencies for other purposes.

### Advertised speeds

802.11ac-class device wireless speeds are often advertised as AC followed by a number, that number being the highest link rates in Mbit/s of all the simultaneously usable radios in the device added up. For example, an AC1900 access point might have 600 Mbit/s capability on its 2.4 GHz radio and 1300 Mbit/s capability on its 5 GHz radio. No single client device could connect and achieve 1900 Mbit/s of throughput, but separate devices each connecting to the 2.4 GHz and 5 GHz radios could achieve combined throughput approaching 1900 Mbit/s. Different possible stream configurations can add up to the same AC number.

| Type | 2.4 GHz band Mbit/s | 2.4 GHz band config [all 40 MHz] | 5 GHz band Mbit/s | 5 GHz band config [all 80 MHz] |
|---|---|---|---|---|
| AC450 | - | - | 433 | 1 stream @ MCS 9 |
| AC600 | 150 | 1 stream @ MCS 7 | 433 | 1 stream @ MCS 9 |
| AC750 | 300 | 2 streams @ MCS 7 | 433 | 1 stream @ MCS 9 |
| AC1000 | 300 | 2 streams @ MCS 7 | 650 | 2 streams @ MCS 7 |
| AC1200 | 300 | 2 streams @ MCS 7 | 867 | 2 streams @ MCS 9 |
| AC1300 | 400 | 2 streams @ 256-QAM | 867 | 2 streams @ MCS 9 |
| AC1300 | 400 | - | 867 | 2 streams @ MCS 9 |
| AC1350 | 450 | 3 streams @ MCS 7 | 867 | 2 streams @ MCS 9 |
| AC1450 | 450 | 3 streams @ MCS 7 | 975 | 3 streams @ MCS 7 |
| AC1600 | 300 | 2 streams @ MCS 7 | 1,300 | 3 streams @ MCS 9 |
| AC1700 | 800 | 4 streams @ 256-QAM | 867 | 2 streams @ MCS 9 |
| AC1750 | 450 | 3 streams @ MCS 7 | 1,300 | 3 streams @ MCS 9 |
| AC1900 | 600 | 3 streams @ 256-QAM | 1,300 | 3 streams @ MCS 9 |
| AC2100 | 800 | 4 streams @ 256-QAM | 1,300 | 3 streams @ MCS 9 |
| AC2200 | 450 | 3 streams @ MCS 7 | 1,733 | 4 streams @ MCS 9 |
| AC2300 | 600 | 4 streams @ MCS 7 | 1,625 | 3 streams @ 1024-QAM |
| AC2400 | 600 | 4 streams @ MCS 7 | 1,733 | 4 streams @ MCS 9 |
| AC2600 | 800 | 4 streams @ 256-QAM | 1,733 | 4 streams @ MCS 9 |
| AC2900 | 750 | 3 streams @ 1024-QAM | 2,167 | 4 streams @ 1024-QAM |
| AC3000 | 450 | 3 streams @ MCS 7 | 1,300 + 1,300 | 3 streams @ MCS 9 x 2 |
| AC3150 | 1000 | 4 streams @ 1024-QAM | 2,167 | 4 streams @ 1024-QAM |
| AC3200 | 600 | 3 streams @ 256-QAM | 1,300 + 1,300 | 3 streams @ MCS 9 x 2 |
| AC5000 | 600 | 4 streams @ MCS 7 | 2,167 + 2,167 | 4 streams @ 1024-QAM x 2 |
| AC5300 | 1000 | 4 streams @ 1024-QAM | 2,167 + 2,167 | 4 streams @ 1024-QAM x 2 |
