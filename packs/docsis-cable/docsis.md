---
title: "DOCSIS"
source: https://en.wikipedia.org/wiki/DOCSIS
domain: docsis-cable
license: CC-BY-SA-4.0
tags: docsis standard, cable modem, cable termination system, hybrid fiber coax
fetched: 2026-07-02
---

# DOCSIS

**Data Over Cable Service Interface Specification** (**DOCSIS**) is an international telecommunications standard that permits the addition of high-bandwidth data transfer to an existing cable television (CATV) system. It is used by many cable television operators to provide cable Internet access over their existing hybrid fiber-coaxial (HFC) infrastructure.

DOCSIS was originally developed by CableLabs and contributing companies, including Broadcom, Comcast, Cox, General Instrument, Motorola, Terayon, and Time Warner Cable.

## Versions

**DOCSIS 1.0**

Released in March 1997, DOCSIS 1.0 included functional elements from preceding proprietary

cable modems

.

**DOCSIS 1.1**

Released in April 1999, DOCSIS 1.1 standardized

quality of service

(QoS) mechanisms that were outlined in DOCSIS 1.0.

**DOCSIS 2.0 (abbreviated D2)**

Released in December 2001, DOCSIS 2.0 enhanced upstream data rates in response to increased demand for symmetric services such as IP telephony.

**DOCSIS 3.0 (abbreviated D3)**

Released in August 2006, DOCSIS 3.0 significantly increased data rates (both upstream and downstream) and introduced support for

Internet Protocol version 6

(IPv6).

**DOCSIS 3.1**

First released in October 2013, and subsequently updated several times, the DOCSIS 3.1 suite of specifications support capacities of up to 10 Gbit/s downstream and 1 Gbit/s upstream using 4096

QAM

. The new specifications eliminated 6 MHz and 8 MHz wide

channel spacing

and instead use narrower (25 kHz or 50 kHz wide)

orthogonal frequency-division multiplexing

(OFDM)

subcarriers

; these can be

bonded

inside a block spectrum that could end up being about 200 MHz wide.

DOCSIS 3.1 technology also includes

power-management

features that will enable the cable industry to reduce its energy usage, and the DOCSIS-PIE

algorithm to reduce

bufferbloat

.

In the

United States

, broadband provider Comcast announced in February 2016 that several cities within its footprint will have DOCSIS 3.1 availability before the end of the year.

At the end of 2016,

Mediacom

announced it would become the first major U.S. cable company to fully transition to the DOCSIS 3.1 platform.

**DOCSIS 4.0**

Improves DOCSIS 3.1 to use the full spectrum of the cable plant (0 MHz to ~1.8 GHz) at the same time in both upstream and downstream directions. This technology enables multi-gigabit symmetrical services while retaining

backward compatibility

with DOCSIS 3.1. CableLabs released the full specification in October 2017.

Previously branded as DOCSIS 3.1 Full Duplex, these technologies have been rebranded as part of DOCSIS 4.0.

**DOCSIS 5.0**

There is currently no official version of DOCSIS declared as DOCSIS 5.0 by CableLabs. There is speculation proposing targets of 25 Gbit/s downstream and at least 5 Gbit/s upstream at 3 GHz, and a reference implementation that was demonstrated in 2024.

### Comparison

Several DOCSIS versions can co exist by using frequency division multiplexing and separating new DOCSIS versions from old ones according to their operation frequencies.

| DOCSIS version | Production date | Maximum downstream capacity | Maximum upstream capacity | Features |
|---|---|---|---|---|
| 1.0 | 1997 | 40 Mbit/s | 10 Mbit/s | Initial release |
| 1.1 | 2001 | Added VOIP capabilities and QoS mechanisms |   |   |
| 2.0 | 2002 | 30 Mbit/s | Enhanced upstream data rates |   |
| 3.0 | 2006 | 1 Gbit/s | 200 Mbit/s | Significantly increased downstream and upstream data rates, introduced support for IPv6, introduced channel bonding |
| 3.1 | 2013 | 10 Gbit/s | 1–2 Gbit/s | Significantly increased downstream and upstream data rates, restructured channel specifications |
| 4.0 | 2017 | 6 Gbit/s | Significantly increased upstream rates from DOCSIS 3.1 |   |

## European alternative

As frequency allocation bandwidth plans differ between United States and European CATV systems, DOCSIS standards earlier than 3.1 have been modified for use in Europe. These modifications were published under the name **EuroDOCSIS**. The differences between the bandwidths exist because European cable TV conforms to PAL/DVB-C standards of 8 MHz RF channel bandwidth and North American cable TV conforms to NTSC/ATSC standards which specify 6 MHz per channel. The wider channel bandwidth in EuroDOCSIS architectures permits more bandwidth to be allocated to the downstream data path (toward the user). EuroDOCSIS certification testing is executed by Belgian company Excentis (formerly known as tComLabs), while DOCSIS certification testing is executed by CableLabs. Typically, customer premises equipment receives "certification", while CMTS equipment receives "qualification".

## International standards

The ITU Telecommunication Standardization Sector (ITU-T) has approved the various versions of DOCSIS as international standards. DOCSIS 1.0 was ratified as ITU-T Recommendation J.112 Annex B (1998), but it was superseded by DOCSIS 1.1 which was ratified as ITU-T Recommendation J.112 Annex B (2001). Subsequently, DOCSIS 2.0 was ratified as ITU-T Recommendation J.122. Most recently, DOCSIS 3.0 was ratified as ITU-T Recommendation J.222 (J.222.0, J.222.1, J.222.2, J.222.3).

Note: While ITU-T Recommendation J.112 Annex B corresponds to DOCSIS/EuroDOCSIS 1.1, Annex A describes an earlier European cable modem system ("DVB EuroModem") based on ATM transmission standards. Annex C describes a variant of DOCSIS 1.1 that is designed to operate in Japanese cable systems. The ITU-T Recommendation J.122 main body corresponds to DOCSIS 2.0, J.122 Annex F corresponds to EuroDOCSIS 2.0, and J.122 Annex J describes the Japanese variant of DOCSIS 2.0 (analogous to Annex C of J.112).

## Features

DOCSIS provides a variety of options available at Open Systems Interconnection (OSI) layers 1 and 2—the physical and data link layers.

### Physical layer

- Channel width:
  - Downstream: All versions of DOCSIS earlier than 3.1 use either 6 MHz channels (e.g. North America) or 8 MHz channels ("EuroDOCSIS"). DOCSIS 3.1 uses channel bandwidths of up to 192 MHz in the downstream.
  - Upstream: DOCSIS 1.0/1.1 specifies channel widths between 200 kHz and 3.2 MHz. DOCSIS 2.0 & 3.0 specify 6.4 MHz, but can use the earlier, narrower channel widths for backward compatibility. DOCSIS 3.1 uses channel bandwidths of up to 96 MHz in the upstream.
- Modulation:
  - Downstream: All versions of DOCSIS prior to 3.1 specify that 64-level or 256-level QAM (64-QAM or 256-QAM) be used for modulation of downstream data, using the ITU-T J.83-Annex B standard for 6 MHz channel operation, and the DVB-C modulation standard for 8 MHz (EuroDOCSIS) operation. DOCSIS 3.1 adds 16-QAM, 128-QAM, 512-QAM, 1024-QAM, 2048-QAM and 4096-QAM, with optional support of 8192-QAM/16384-QAM.
  - Upstream: Upstream data uses QPSK or 16-level QAM (16-QAM) for DOCSIS 1.x, while QPSK, 8-QAM, 16-QAM, 32-QAM, and 64-QAM are used for DOCSIS 2.0 and 3.0. DOCSIS 2.0 and 3.0 also support 128-QAM with trellis coded modulation in S-CDMA mode (with an effective spectral efficiency equivalent to that of 64-QAM). DOCSIS 3.1 supports data modulations from QPSK up to 1024-QAM, with optional support for 2048-QAM and 4096-QAM.

### Data link layer

- DOCSIS employs a mixture of deterministic access methods for upstream transmissions, specifically time-division multiple access (TDMA) for DOCSIS 1.0/1.1 and both TDMA and S-CDMA for DOCSIS 2.0 and 3.0, with a limited use of contention for bandwidth reservation requests. In TDMA, a cable modem requests a time to transmit and the CMTS grants it an available time slot.
- For DOCSIS 1.1 and above, the data layer also includes extensive quality-of-service (QoS) features that help to efficiently support applications that have specific traffic requirements such as low latency, e.g. voice over IP.
- DOCSIS 3.0 features channel bonding, which enables multiple downstream and upstream channels to be used together at the same time by a single subscriber.

### Throughput

Bandwidth is shared among users of an HFC, within service groups which are groups of customers that share RF channels.

The first three versions of the DOCSIS standard support a downstream throughput with 256-QAM of up to 42.88 Mbit/s per 6 MHz channel (approximately 38 Mbit/s after overhead), or 55.62 Mbit/s per 8 MHz channel for EuroDOCSIS (approximately 50 Mbit/s after overhead). The upstream throughput possible is 30.72 Mbit/s per 6.4 MHz channel (approximately 27 Mbit/s after overhead), or 10.24 Mbit/s per 3.2 MHz channel (approximately 9 Mbit/s after overhead).

DOCSIS 3.1 supports a downstream throughput with 4096-QAM and 25 kHz subcarrier spacing of up to 1.89 Gbit/s per 192 MHz OFDM channel. The upstream throughput possible is 0.94 Gbit/s per 96 MHz OFDMA channel.

### Network layer

- DOCSIS modems are managed via an Internet Protocol (IP) address.
- The 'DOCSIS 2.0 + IPv6' specification allowed support for IPv6 on DOCSIS 2.0 modems via a firmware upgrade.
- DOCSIS 3.0 added management over IPv6.

## Throughput

Tables assume 256-QAM modulation for downstream and 64-QAM for upstream on DOCSIS 3.0, and 4096-QAM modulation for OFDM/OFDMA (first downstream/upstream methods) on DOCSIS 3.1, although real-world data rates may be lower due to variable modulation depending on SNR. Higher data rates are possible but require higher order QAM schemes which require higher downstream modulation error ratio (MER). DOCSIS 3.1 was designed to support up to 8192-QAM/16,384-QAM, but only support of up through 4096-QAM is mandatory to meet the minimum DOCSIS 3.1 standards.

Maximum raw throughput including overhead

Version

Downstream

Upstream

Channel configuration

DOCSIS throughput in Mbit/s

EuroDOCSIS throughput in Mbit/s

Channel configuration

Throughput in Mbit/s

Minimum selectable number of channels

Minimum number of channels that hardware must support

Selected number of channels

Maximum number of channels

Minimum selectable number of channels

Minimum number of channels that hardware must support

Selected number of channels

Maximum number of channels

1.x

1

1

1

1

42.88

55.62

1

1

1

1

10.24

2.0

1

1

1

1

42.88

55.62

1

1

1

1

30.72

3.0

1

4

m

Not defined

m

× 42.88

m

× 55.62

1

4

n

Not defined

n

× 30.72

3.1

1 OFDM channel

or

1 SC-QAM channel

2 OFDM channels

and

32 SC-QAM channels

m

1

m

2

Not defined

Dependent on OFDM channel bandwidth in MHz

plus

m

2

× 42.88

Dependent on OFDM channel bandwidth in MHz

plus

m

2

× 55.62

1 OFDMA channel

or

1 SC-QAM channel

2 OFDMA channels

and

8 SC-QAM channels

n

1

n

2

Not defined

Dependent on OFDMA channel bandwidth in MHz

plus

n

2

× 30.72

For DOCSIS 3.0, the theoretical maximum throughput for the number of bonded channels are listed in the table below.

| Number of channels | Downstream throughput | Upstream throughput |   |   |
|---|---|---|---|---|
| Downstream | Upstream | DOCSIS | EuroDOCSIS |   |
| 4 | 4 | 171.52 Mbit/s | 222.48 Mbit/s | 122.88 Mbit/s |
| 8 | 4 | 343.04 Mbit/s | 444.96 Mbit/s |   |
| 16 | 4 | 686.08 Mbit/s | 889.92 Mbit/s |   |
| 24 | 8 | 1029.12 Mbit/s | 1334.784 Mbit/s | 245.76 Mbit/s |
| 32 | 8 | 1372.16 Mbit/s | 1779.712 Mbit/s |   |

Note that the number of channels a cable system can support is dependent on how the cable system is set up. For example, the amount of available bandwidth in each direction, the width of the channels selected in the upstream direction, and hardware constraints limit the maximum amount of channels in each direction. (See below.)

Note that the maximum downstream bandwidth on all versions of DOCSIS depends on the version of DOCSIS used and the number of upstream channels used if DOCSIS 3.0 is used, but the upstream channel widths are independent of whether DOCSIS or EuroDOCSIS is used.

### Upstream

Traditional DOCSIS upstream in North America uses the 5–42 MHz frequency range. The 5–65 MHz range is used by EuroDOCSIS. This is known as a "low-split" or "sub-split" design, capable of a total shared capacity of ~108 Mbit/s upstream (assuming 4 SC-QAM upstream channels) for the service group.

Since DOCSIS 3.0, cable operators have begun to increase the amount of bandwidth dedicated to the upstream. The two most popular options for this include a "mid-split" or "high-split".

A mid-split increases the upstream frequency range to 5–85 MHz, supporting a total shared upstream capacity of ~450 Mbit/s (assuming 4 SC-QAM + OFDMA channels) for the service group.

A high-split increases the upstream frequency range to 5–204 MHz, supporting a total shared upstream capacity of ~1.5 Gbit/s (assuming 4 SC-QAM + OFDMA channels) for the service group.

DOCSIS 4.0 in both full-duplex (FDX) and extended spectrum DOCSIS (ESD) configurations will support upstream speeds surpassing 5 Gbit/s.

## Equipment

A DOCSIS architecture includes two primary components: a cable modem located at the customer premises, and a cable modem termination system (CMTS) located at the CATV headend.

The customer PC and associated peripherals are termed customer-premises equipment (CPE). The CPE are connected to the cable modem, which is in turn connected through the HFC network to the CMTS. The CMTS then routes traffic between the HFC and the Internet. Using provisioning systems and through the CMTS, the cable operator exercises control over the cable modem's configuration.

DOCSIS 2.0 was also used over microwave frequencies (10 GHz) in Ireland by Digiweb, using dedicated wireless links rather than HFC network. At each subscriber premises the ordinary CM is connected to an antenna box which converts to/from microwave frequencies and transmits/receives on 10 GHz. Each customer has a dedicated link but the transmitter mast must be in line of sight (most sites are hilltop).

## Security

DOCSIS includes media access control (MAC) layer security services in its Baseline Privacy Interface specifications. DOCSIS 1.0 used the initial Baseline Privacy Interface (BPI) specification. BPI was later improved with the release of the Baseline Privacy Interface Plus (BPI+) specification used by DOCSIS 1.1 and 2.0. Most recently, a number of enhancements to the Baseline Privacy Interface were added as part of DOCSIS 3.0, and the specification was renamed "Security" (SEC).

The intent of the BPI/SEC specifications is to describe MAC layer security services for DOCSIS CMTS to cable modem communications. BPI/SEC security goals are twofold:

- Provide cable modem users with data privacy across the cable network
- Provide cable service operators with service protection (i.e. prevent unauthorized modems and users from gaining access to the network's RF MAC services)

BPI/SEC is intended to prevent cable users from listening to each other. It does this by encrypting data flows between the CMTS and the cable modem. BPI and BPI+ use 56-bit Data Encryption Standard (DES) encryption, while SEC adds support for 128-bit Advanced Encryption Standard (AES). The AES key, however, is protected only by a 1024-bit RSA key.

BPI/SEC is intended to allow cable service operators to refuse service to uncertified cable modems and unauthorized users. BPI+ strengthened service protection by adding digital certificate based authentication to its key exchange protocol, using a public key infrastructure (PKI), based on digital certificate authorities (CAs) of the certification testers, currently Excentis (formerly known as tComLabs) for EuroDOCSIS and CableLabs for DOCSIS. Typically, the cable service operator manually adds the cable modem's MAC address to a customer's account with the cable service operator; and the network allows access only to a cable modem that can attest to that MAC address using a valid certificate issued via the PKI. The earlier BPI specification (ANSI/SCTE 22-2) had limited service protection because the underlying key management protocol did not authenticate the user's cable modem.
