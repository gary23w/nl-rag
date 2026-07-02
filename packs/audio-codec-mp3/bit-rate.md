---
title: "Bit rate"
source: https://en.wikipedia.org/wiki/Bit_rate
domain: audio-codec-mp3
license: CC-BY-SA-4.0
tags: mp3 codec, mpeg audio layer, psychoacoustic model, audio bit rate
fetched: 2026-07-02
---

# Bit rate

| Name | Symbol | Multiple |   |
|---|---|---|---|
| bit per second | bit/s | 1 | 1 |
| Metric prefixes (SI) |   |   |   |
| kilobit per second | kbit/s | 103 | 10001 |
| megabit per second | Mbit/s | 106 | 10002 |
| gigabit per second | Gbit/s | 109 | 10003 |
| terabit per second | Tbit/s | 1012 | 10004 |
| Binary prefixes (IEC 80000-13) |   |   |   |
| kibibit per second | Kibit/s | 210 | 10241 |
| mebibit per second | Mibit/s | 220 | 10242 |
| gibibit per second | Gibit/s | 230 | 10243 |
| tebibit per second | Tibit/s | 240 | 10244 |

In telecommunications and computing, **bit rate** (**bitrate** or as a variable *R*) is the number of bits that are conveyed or processed per unit of time.

The bit rate is expressed as **bits per second** (symbol: **bit/s**), often with an SI prefix such as kilo (1 kbit/s = 1,000 bit/s), mega (1 Mbit/s = 1,000 kbit/s), giga (1 Gbit/s = 1,000 Mbit/s) or tera (1 Tbit/s = 1,000 Gbit/s). The non-standard abbreviation **bps** is often used: 1 Mbps is 1 Mbit/s, that is, one million bits per second.

The bit rate is different from the **transfer rate**, measured in transfers per second, when the channel is parallel and thus transfers multiple bits per transfer.

In most computing and digital communication environments, one **byte per second** (symbol: **B/s**) corresponds to 8 bit/s (1 byte = 8 bits). However if stop bits, start bits, and parity bits need to be factored in, a higher number of bits per second will be required to achieve a throughput of the same number of bytes.

## Prefixes

For large or small bit rates, SI prefixes (also known as metric prefixes or decimal prefixes) are used:

| 0.001 bit/s | = 1 mbit/s (one millibit per second, i.e., one bit per thousand seconds) = 1 bit/ks |
|---|---|
| 1 bit/s | = 1 bit/s (one bit per second) |
| 1,000 bit/s | = 1 kbit/s (one kilobit per second, i.e., one thousand bits per second) |
| 1,000,000 bit/s | = 1 Mbit/s (one megabit per second, i.e., one million bits per second) |
| 1,000,000,000 bit/s | = 1 Gbit/s (one gigabit per second, i.e., one billion bits per second) |
| 1,000,000,000,000 bit/s | = 1 Tbit/s (one terabit per second, i.e., one trillion bits per second) |

The binary prefixes defined by International Standard IEC 80000-13 are sometimes used: e.g., 1 KiB/s = 1024 B/s = 8192 bit/s, and 1 MiB/s = 1024 KiB/s.

## In data communications

### Gross bit rate

In digital communication systems, the physical layer *gross bitrate*, *raw bitrate*, *data signaling rate*, *gross data transfer rate* or *uncoded transmission rate* (sometimes written as a variable *R*b or *f*b) is the total number of physically transferred bits per second over a communication link, including useful data as well as protocol overhead.

In case of serial communications, the gross bit rate is related to the bit transmission time $T_{\text{b}}$ as:

$R_{\text{b}}={1 \over T_{\text{b}}},$

The gross bit rate is related to the symbol rate or modulation rate, which is expressed in baud or symbols per second. However, the gross bit rate and the baud value are equal *only* when there are only two levels per symbol, representing 0 and 1, meaning that each symbol of a data transmission system carries exactly one bit of data; this is not the case for modern modulation systems used in modems and LAN equipment.

For most line codes and modulation methods:

${\text{symbol rate}}\leq {\text{gross bit rate}}$

More specifically, a line code (or baseband transmission scheme) representing the data using pulse-amplitude modulation with $2^{N}$ different voltage levels, can transfer N bits per pulse. A digital modulation method (or passband transmission scheme) using $2^{N}$ different symbols, for example $2^{N}$ amplitudes, phases or frequencies, can transfer N bits per symbol. This results in:

${\text{gross bit rate}}={\text{symbol rate}}\times N$

An exception from the above is some self-synchronizing line codes, for example Manchester coding and return-to-zero (RTZ) coding, where each bit is represented by two pulses (signal states), resulting in:

${\text{gross bit rate = symbol rate/2}}$

A theoretical upper bound for the symbol rate in baud, symbols/s or pulses/s for a certain spectral bandwidth in hertz is given by the Nyquist law:

${\text{symbol rate}}\leq {\text{Nyquist rate}}=2\times {\text{bandwidth}}$

In practice this upper bound can only be approached for line coding schemes and for so-called vestigial sideband digital modulation. Most other digital carrier-modulated schemes, for example ASK, PSK, QAM and OFDM, can be characterized as double sideband modulation, resulting in the following relation:

${\text{symbol rate}}\leq {\text{bandwidth}}$

In case of parallel communication, the gross bit rate is given by

$\sum _{i=1}^{n}{\frac {\log _{2}{M_{i}}}{T_{i}}}$

where *n* is the number of parallel channels, *Mi* is the number of symbols or levels of the modulation in the *i*th channel, and *Ti* is the symbol duration time, expressed in seconds, for the *i*th channel.

### Information rate

The physical layer **net bitrate**, **information rate**, **useful bit rate**, **payload rate**, **net data transfer rate**, **coded transmission rate**, **effective data rate** or wire speed (informal language) of a digital communication channel is the capacity excluding the physical layer protocol overhead, for example time division multiplex (TDM) framing bits, redundant forward error correction (FEC) codes, equalizer training symbols and other channel coding. Error-correcting codes are common especially in wireless communication systems, broadband modem standards and modern copper-based high-speed LANs. The physical layer net bitrate is the datarate measured at a reference point in the interface between the data link layer and physical layer, and may consequently include data link and higher layer overhead.

In modems and wireless systems, link adaptation (automatic adaptation of the data rate and the modulation and/or error coding scheme to the signal quality) is often applied. In that context, the term **peak bitrate** denotes the net bitrate of the fastest and least robust transmission mode, used for example when the distance is very short between sender and transmitter. Some operating systems and network equipment may detect the "**connection speed**" (informal language) of a network access technology or communication device, implying the current net bit rate. The term **line rate** in some textbooks is defined as gross bit rate, in others as net bit rate.

The relationship between the gross bit rate and net bit rate is affected by the FEC code rate according to the following.

net bit rate ≤ gross bit rate ×

code rate

The connection speed of a technology that involves forward error correction typically refers to the physical layer *net bit rate* in accordance with the above definition.

For example, the net bitrate (and thus the "connection speed") of an IEEE 802.11a wireless network is the net bit rate of between 6 and 54 Mbit/s, while the gross bit rate is between 12 and 72 Mbit/s inclusive of error-correcting codes.

The net bit rate of ISDN2 Basic Rate Interface (2 B-channels + 1 D-channel) of 64+64+16 = 144 kbit/s also refers to the payload data rates, while the D channel signalling rate is 16 kbit/s.

The net bit rate of the Ethernet 100BASE-TX physical layer standard is 100 Mbit/s, while the gross bitrate is 125 Mbit/s, due to the 4B5B (four bit over five bit) encoding. In this case, the gross bit rate is equal to the symbol rate or pulse rate of 125 megabaud, due to the NRZI line code.

In communications technologies without forward error correction and other physical layer protocol overhead, there is no distinction between gross bit rate and physical layer net bit rate. For example, the net as well as gross bit rate of Ethernet 10BASE-T is 10 Mbit/s. Due to the Manchester line code, each bit is represented by two pulses, resulting in a pulse rate of 20 megabaud.

The "connection speed" of a V.92 voiceband modem typically refers to the gross bit rate, since there is no additional error-correction code. It can be up to 56,000 bit/s downstream and 48,000 bit/s upstream. A lower bit rate may be chosen during the connection establishment phase due to adaptive modulation – slower but more robust modulation schemes are chosen in case of poor signal-to-noise ratio. Due to data compression, the actual data transmission rate or throughput (see below) may be higher.

The channel capacity, also known as the Shannon capacity, is a theoretical upper bound for the maximum net bitrate, exclusive of forward error correction coding, that is possible without bit errors for a certain physical analog node-to-node communication link.

net bit rate ≤ channel capacity

The channel capacity is proportional to the analog bandwidth in hertz. This proportionality is called Hartley's law. Consequently, the net bit rate is sometimes called digital bandwidth capacity in bit/s.

### Network throughput

The term *throughput*, essentially the same thing as **digital bandwidth consumption**, denotes the achieved average useful bit rate in a computer network over a logical or physical communication link or through a network node, typically measured at a reference point above the data link layer. This implies that the throughput often excludes data link layer protocol overhead. The throughput is affected by the traffic load from the data source in question, as well as from other sources sharing the same network resources. See also measuring network throughput.

### Goodput (data transfer rate)

*Goodput* or **data transfer rate** refers to the achieved average net bit rate that is delivered to the application layer, exclusive of all protocol overhead, data packets retransmissions, etc. For example, in the case of file transfer, the goodput corresponds to the achieved **file transfer rate**. The file transfer rate in bit/s can be calculated as the file size (in bytes) divided by the file transfer time (in seconds) and multiplied by eight.

As an example, the goodput or data transfer rate of a V.92 voiceband modem is affected by the modem physical layer and data link layer protocols. It is sometimes higher than the physical layer data rate due to V.44 data compression, and sometimes lower due to bit-errors and automatic repeat request retransmissions.

If no data compression is provided by the network equipment or protocols, we have the following relation:

goodput ≤ throughput ≤ maximum throughput ≤ net bit rate

for a certain communication path.

### Progress trends

These are examples of physical layer net bit rates in proposed communication standard interfaces and devices:

| WAN modems | Ethernet LAN | WiFi WLAN | Mobile data |
|---|---|---|---|
| 1972: Acoustic coupler 300 baud 1977: 1200 baud Vadic and Bell 212A 1986: ISDN introduced with two 64 kbit/s channels (144 kbit/s gross bit rate) 1990: V.32bis modems: 2400 / 4800 / 9600 / 19200 bit/s 1994: V.34 modems with 28.8 kbit/s 1995: V.90 modems with 56 kbit/s downstreams, 33.6 kbit/s upstreams 1999: V.92 modems with 56 kbit/s downstreams, 48 kbit/s upstreams 1998: ADSL (ITU G.992.1) up to 10 Mbit/s 2003: ADSL2 (ITU G.992.3) up to 12 Mbit/s 2003: GPON up to 1 Gbit/s 2005: ADSL2+ (ITU G.992.5) up to 26 Mbit/s 2005: VDSL2 (ITU G.993.2) up to 200 Mbit/s 2010: 10G-PON up to 10 Gbit/s 2014: G.fast (ITU G.9701) up to 1 Gbit/s | 1975: Experimental 2.94 Mbit/s 1981: 10 Mbit/s 10BASE5 (coaxial cable) 1990: 10 Mbit/s 10BASE-T (twisted pair) 1995: 100 Mbit/s Fast Ethernet 1999: Gigabit Ethernet 2003: 10 Gigabit Ethernet 2010: 100 Gigabit Ethernet 2017: 200/400 Gigabit Ethernet | 1997: 802.11 2 Mbit/s 1999: 802.11b 11 Mbit/s 1999: 802.11a 54 Mbit/s 2003: 802.11g 54 Mbit/s 2007: 802.11n 600 Mbit/s 2012: 802.11ac ~1000 Mbit/s | 1G: 1981: NMT 1200 bit/s 2G: 1991: GSM CSD and D-AMPS 14.4 kbit/s 2003: GSM EDGE 296 kbit/s down, 118.4 kbit/s up 3G: 2001: UMTS-FDD (WCDMA) 384 kbit/s 2007: UMTS HSDPA 14.4 Mbit/s 2008: UMTS HSPA 14.4 Mbit/s down, 5.76 Mbit/s up 2009: HSPA+ (Without MIMO) 28 Mbit/s downstreams (56 Mbit/s with 2×2 MIMO), 22 Mbit/s upstreams 2010: CDMA2000 EV-DO Rev. B 14.7 Mbit/s downstreams 2011: HSPA+ accelerated (With MIMO) 42 Mbit/s downstreams Pre-4G: 2007: Mobile WiMAX (IEEE 802.16e) 144 Mbit/s down, 35 Mbit/s up 2009: LTE 100 Mbit/s downstreams (360 Mbit/s with MIMO 2×2), 50 Mbit/s upstreams 5G |

## Multimedia

In digital multimedia, bit rate represents the amount of information, or detail, that is stored per unit of time of a recording. The bitrate depends on several factors:

- The original material may be sampled at different frequencies.
- The samples may use different numbers of bits.
- The data may be encoded by different schemes.
- The information may be digitally compressed by different algorithms or to different degrees.

Generally, choices are made about the above factors in order to achieve the desired trade-off between minimizing the bitrate and maximizing the quality of the material when it is played.

If lossy data compression is used on audio or visual data, differences from the original signal will be introduced; if the compression is substantial, or lossy data is decompressed and recompressed, this may become noticeable in the form of compression artifacts. Whether these affect the perceived quality, and if so how much, depends on the compression scheme, encoder power, the characteristics of the input data, the listener's perceptions, the listener's familiarity with artifacts, and the listening or viewing environment.

The encoding bit rate of a multimedia file is its size in bytes divided by the playback time of the recording (in seconds), multiplied by eight.

For real-time streaming multimedia, the encoding bit rate is the goodput that is required to avoid playback interruption.

The term average bitrate is used in case of variable bitrate multimedia source coding schemes. In this context, the *peak bit rate* is the maximum number of bits required for any short-term block of compressed data.

A theoretical lower bound for the encoding bit rate for lossless data compression is the source information rate, also known as the *entropy rate*.

The bitrates in this section are approximately the *minimum* that the *average* listener in a typical listening or viewing environment, when using the best available compression, would perceive as not significantly worse than the reference standard.

### Audio

#### CD-DA

Compact Disc Digital Audio (CD-DA) uses 44,100 samples per second, each with a bit depth of 16, a format sometimes abbreviated like "16bit / 44.1kHz". CD-DA is also stereo, using a left and right channel, so the amount of audio data per second is double that of mono, where only a single channel is used.

The bit rate of PCM audio data can be calculated with the following formula:

${\text{bit rate}}={\text{sample rate}}\times {\text{bit depth}}\times {\text{channels}}$

For example, the bit rate of a CD-DA recording (44.1 kHz sampling rate, 16 bits per sample and two channels) can be calculated as follows:

$44,100\times 16\times 2=1,411,200\ {\text{bit/s}}=1,411.2\ {\text{kbit/s}}$

The cumulative size of a length of PCM audio data (excluding a file header or other metadata) can be calculated using the following formula:

${\text{size in bits}}={\text{sample rate}}\times {\text{bit depth}}\times {\text{channels}}\times {\text{time}}.$

The cumulative size in bytes can be found by dividing the file size in bits by the number of bits in a byte, which is eight:

${\text{size in bytes}}={\frac {\text{size in bits}}{8}}$

Therefore, 80 minutes (4,800 seconds) of CD-DA data requires 846,720,000 bytes of storage:

${\frac {44,100\times 16\times 2\times 4,800}{8}}=846,720,000\ {\text{bytes}}\approx 847\ {\text{MB}}\approx 807.5\ {\text{MiB}}$

where **MiB** is mebibytes with binary prefix Mi, meaning 220 = 1,048,576.

#### MP3

The MP3 audio format provides lossy data compression. Audio quality improves with increasing bitrate:

- 32 kbit/s – generally acceptable only for speech
- 96 kbit/s – generally used for speech or low-quality streaming
- 128 or 160 kbit/s – mid-range bitrate quality
- 192 kbit/s – medium quality bitrate
- 256 kbit/s – a commonly used high-quality bitrate
- 320 kbit/s – highest level supported by the MP3 standard

#### M4A

The Advanced Audio Coding (AAC) audio format provides lossy data compression or lossless data compression. Audio quality improves with increasing bitrate:

- 320 kbit/s – typical highest level in AAC lossy stereo audio used by Apple Music, Spotify, etc
- 512 kbit/s – highest level supported by the AAC lossy standard in stereo audio

#### Other audio

- 700 bit/s – lowest bitrate open-source speech codec Codec2, but Codec2 sounds much better at 1.2 kbit/s
- 800 bit/s – minimum necessary for recognizable speech, using the special-purpose FS-1015 speech codecs
- 2.15 kbit/s – minimum bitrate available through the open-source Speex codec
- 6 kbit/s – minimum bitrate available through the open-source Opus codec
- 8 kbit/s – telephone quality using speech codecs
- 32–500 kbit/s – lossy audio as used in Ogg Vorbis
- 256 kbit/s – Digital Audio Broadcasting (DAB) MP2 bit rate required to achieve a high quality signal
- 292 kbit/s – Sony Adaptive Transform Acoustic Coding (ATRAC) for use on the MiniDisc Format
- 400 kbit/s–1,411 kbit/s – lossless audio as used in formats such as Free Lossless Audio Codec, WavPack, or Monkey's Audio to compress CD audio
- 1,411.2 kbit/s – Linear PCM sound format of CD-DA
- 5,644.8 kbit/s – DSD, which is a trademarked implementation of PDM sound format used on Super Audio CD.
- 6.144 Mbit/s – E-AC-3 (Dolby Digital Plus), an enhanced coding system based on the AC-3 codec
- 9.6 Mbit/s – DVD-Audio, a digital format for delivering high-fidelity audio content on a DVD. DVD-Audio is not intended to be a video delivery format and is not the same as video DVDs containing concert films or music videos. These discs cannot be played on a standard DVD-player without DVD-Audio logo.
- 18 Mbit/s – advanced lossless audio codec based on Meridian Lossless Packing (MLP)

### Video

- 16 kbit/s – videophone quality (minimum necessary for a consumer-acceptable "talking head" picture using various video compression schemes)
- 128–384 kbit/s – business-oriented videoconferencing quality using video compression
- 400 kbit/s YouTube 240p videos (using H.264)
- 750 kbit/s YouTube 360p videos (using H.264)
- 1 Mbit/s YouTube 480p videos (using H.264)
- 1.15 Mbit/s max – VCD quality (using MPEG1 compression)
- 2.5 Mbit/s YouTube 720p videos (using H.264)
- 3.5 Mbit/s typ – Standard-definition television quality (with bit-rate reduction from MPEG-2 compression)
- 3.8 Mbit/s YouTube 720p60 (60 FPS) videos (using H.264)
- 3-8 Mbit/s YouTube 1080p videos (using H.264)
- 4-10 Mbit/s YouTube 1080p60 (60 FPS) videos (using H.264)
- 5-25 Mbit/s YouTube 1440p videos (using H.264)
- 6-30 Mbit/s YouTube 1440p60 (60 FPS) videos (using H.264)
- 8-35 Mbit/s YouTube 2160p videos (using H.264)
- 9.8 Mbit/s max – DVD (using MPEG2 compression)
- 10-40 Mbit/s YouTube 2160p60 (60 FPS) videos (using H.264)
- 8 to 15 Mbit/s typ – HDTV quality (with bit-rate reduction from MPEG-4 AVC compression)
- 19 Mbit/s approximate – HDV 720p (using MPEG2 compression)
- 24 Mbit/s max – AVCHD (using MPEG4 AVC compression)
- 25 Mbit/s approximate – HDV 1080i (using MPEG2 compression)
- 29.4 Mbit/s max – HD DVD
- 40 Mbit/s max – 1080p Blu-ray Disc (using MPEG2, MPEG4 AVC or VC-1 compression)
- 250 Mbit/s max – DCP (using JPEG 2000 compression)
- 1.5 Gbit/s – 10-bit 4:4:4 uncompressed 1080p at 24 FPS
