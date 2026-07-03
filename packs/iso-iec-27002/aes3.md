---
title: "AES3"
source: https://en.wikipedia.org/wiki/AES3
domain: iso-iec-27002
license: CC-BY-SA-4.0
tags: iso/iec 27002
fetched: 2026-07-03
---

# AES3

**AES3** is a standard for the exchange of digital audio signals between professional audio devices. An AES3 signal can carry two channels of pulse-code-modulated digital audio over several transmission media including balanced lines, unbalanced lines, and optical fiber.

AES3 was jointly developed by the Audio Engineering Society (AES) and the European Broadcasting Union (EBU) and so is also known as **AES/EBU**. The standard was first published in 1985 and was revised in 1992 and 2003. AES3 has been incorporated into the International Electrotechnical Commission's standard **IEC 60958**, and is available in a consumer-grade variant known as S/PDIF.

## History and development

The development of standards for digital audio interconnect for both professional and domestic audio equipment, began in the late 1970s in a joint effort between the Audio Engineering Society and the European Broadcasting Union, and culminated in the publishing of AES3 in 1985. The AES3 standard has been revised in 1992 and 2003 and is published in AES and EBU versions. Early on, the standard was frequently known as AES/EBU.

Variants using different physical connections are specified in IEC 60958. These are essentially consumer versions of AES3 for use within the domestic high fidelity environment using connectors more commonly found in the consumer market. These variants are commonly known as S/PDIF.

### IEC 60958

**IEC 60958** (formerly IEC 958) is the International Electrotechnical Commission's standard on digital audio interfaces. It reproduces the AES3 professional digital audio interconnect standard and the consumer version of the same, S/PDIF.

The standard consists of several parts:

- IEC 60958-1: General
- IEC 60958-2: Software Information Delivery Mode
- IEC 60958-3: Consumer applications
- IEC 60958-4: Professional applications
- IEC 60958-5: Consumer application enhancement

### AES-2id

**AES-2id** is an AES information document published by the Audio Engineering Society for digital audio engineering—Guidelines for the use of the AES3 interface. This document provides guidelines for the use of AES3, AES Recommended Practice for Digital Audio Engineering, Serial transmission format for two-channel linearly represented digital audio data. This document also covers the description of related standards used in conjunction with AES3 such as AES11. The full details of AES-2id can be found in the standards section of the Audio Engineering Society web site.

## Hardware connections

The AES3 standard parallels part 4 of the international standard IEC 60958. Of the physical interconnection types defined by IEC 60958, two are in common use.

### IEC 60958 type I

Type I connections use balanced, three-conductor, 110-ohm twisted pair cabling with XLR connectors. Type I connections are most often used in professional installations and are considered the standard connector for AES3. The hardware interface is usually implemented using RS-422 line drivers and receivers.

|   | Cable end | Device end |
|---|---|---|
| Input | XLR male plug | XLR female jack |
| Output | XLR female plug | XLR male jack |

### IEC 60958 type II

IEC 60958 Type II defines an unbalanced electrical or optical interface for consumer electronics applications. The precursor of the IEC 60958 Type II specification was the Sony/Philips Digital Interface, or S/PDIF. Both were based on the original AES/EBU work. S/PDIF and AES3 are interchangeable at the protocol level, but at the physical level, they specify different electrical signalling levels and impedances, which may be significant in some applications.

### BNC connector

AES/EBU signals can also be run using unbalanced BNC connectors with a 75-ohm coaxial cable. The unbalanced version has a very long transmission distance as opposed to the 150 meters maximum for the balanced version. The AES-3id standard defines a 75-ohm BNC electrical variant of AES3. This uses the same cabling, patching and infrastructure as analogue or digital video, and is thus common in the broadcast industry.

## Protocol

The low-level protocol for data transmission in AES3 and S/PDIF is largely identical, and the following discussion applies for S/PDIF, except as noted.

AES3 was designed primarily to support stereo PCM encoded audio in either DAT format at 48 kHz or CD format at 44.1 kHz. No attempt was made to use a carrier able to support both rates; instead, AES3 allows the data to be run at *any* rate, and encoding the clock and the data together using biphase mark code (BMC).

Each bit occupies one *time slot*. Each audio sample (of up to 24 bits) is combined with four flag bits and a synchronisation preamble which is four time slots long to make a *subframe* of 32 time slots. The 32 time slots of each subframe are assigned as follows:

| Time slot | Name | Description |
|---|---|---|
| 0–3 | Preamble | A synchronisation preamble (biphase mark code violation) for audio blocks, frames, and subframes. |
| 4–7 | Auxiliary sample (optional) | A low-quality auxiliary channel used as specified in the channel status word, notably for producer talkback or recording studio-to-studio communication. |
| 8–27, or 4–27 | Audio sample | One sample stored with most significant bit (MSB) last. If the auxiliary sample is used, bits 4–7 are not included. Data with smaller sample bit depths always have MSB at bit 27 and are zero-extended towards the least significant bit (LSB). |
| 28 | Validity (V) | Unset if the audio data are correct and suitable for D/A conversion. During the presence of defective samples, the receiving equipment may be instructed to mute its output. It is used by most CD players to indicate that concealment rather than error correction is taking place. |
| 29 | User data (U) | Forms a serial data stream for each channel (with 1 bit per frame), with a format specified in the channel status word. |
| 30 | Channel status (C) | Bits from each frame of an audio block are collated giving a 192-bit channel status word. Its structure depends on whether AES3 or S/PDIF is used. |
| 31 | Parity (P) | Even parity bit for detection of errors in data transmission. Excludes preamble; Bits 4–31 have an even number of ones. |

Two subframes (A and B, normally used for left and right audio channels) make a **frame**. Frames contain 64 bit periods and are produced once per audio sample period. At the highest level, each 192 consecutive frames are grouped into an *audio block*. While samples repeat each frame time, metadata is only transmitted once per audio block. At 48 kHz sample rate, there are 250 audio blocks per second, and 3,072,000 time slots per second supported by a 6.144 MHz biphase clock.

### Synchronisation preamble

The synchronisation preamble is a specially coded *preamble* that identifies the subframe and its position within the audio block. Preambles are not normal BMC-encoded data bits, although they do still have zero DC bias.

Three preambles are possible:

- X (or M) : 111000102 if previous time slot was *0*, 000111012 if it was *1*. (Equivalently, 100100112 NRZI encoded.) Marks a word for channel A (left), other than at the start of an audio block.
- Y (or W) : 111001002 if previous time slot was *0*, 000110112 if it was *1*. (Equivalently, 100101102 NRZI encoded.) Marks a word for channel B (right).
- Z (or B) : 111010002 if previous time slot was *0*, 000101112 if it was *1*. (Equivalently, 100111002 NRZI encoded.) Marks a word for channel A (left) at the start of an audio block.

The three preambles are called X, Y, Z in the AES3 standard; and M, W, B in IEC 958 (an AES extension).

The 8-bit preambles are transmitted in the time allocated to the first four time slots of each subframe (time slots 0 to 3). Any of the three marks the beginning of a subframe. X or Z marks the beginning of a frame, and Z marks the beginning of an audio block.

```
 | 0 | 1 | 2 | 3 |  | 0 | 1 | 2 | 3 | Time slots
  _____       _            _____   _
 /     \_____/ \_/  \_____/     \_/ \ Preamble X
  _____     _              ___   ___
 /     \___/ \___/  \_____/   \_/   \ Preamble Y
  _____   _                _   _____
 /     \_/ \_____/  \_____/ \_/     \ Preamble Z
  ___     ___            ___     ___ 
 /   \___/   \___/  \___/   \___/   \ All 0 bits BMC encoded
  _   _   _   _        _   _   _   _
 / \_/ \_/ \_/ \_/  \_/ \_/ \_/ \_/ \ All 1 bits BMC encoded
 
 | 0 | 1 | 2 | 3 |  | 0 | 1 | 2 | 3 | Time slots
```

In two-channel AES3, the preambles form a pattern of ZYXYXYXY..., but it is straightforward to extend this structure to additional channels (more subframes per frame), each with a Y preamble, as is done in the MADI protocol.

### Channel status word

There is one channel status bit in each subframe, a total of 192 bits or 24 bytes for each channel in each block. Between the AES3 and S/PDIF standards, the contents of the 192-bit channel status word differ significantly, although they agree that the first channel status bit distinguishes between the two. In the case of AES3, the standard describes, in detail, the function of each bit.

- Byte 0: Basic control data: sample rate, compression, emphasis
  - bit 0: A value of 1 indicates this is AES3 channel status data. 0 indicates this is S/PDIF data.
  - bit 1: A value of 0 indicates this is linear audio PCM data. A value of 1 indicates other (usually non-audio) data.
  - bits 2–4: Indicates the type of signal preemphasis applied to the data. Generally set to 1002 (none).
  - bit 5: A value of 0 indicates that the source is locked to some (unspecified) external time sync. A value of 1 indicates an unlocked source.
  - bits 6–7: Sample rate. These bits are redundant when real-time audio is transmitted (the receiver can observe the sample rate directly), but are useful if AES3 data is recorded or otherwise stored. Options are unspecified, 48 kHz (the default), 44.1 kHz, and 32 kHz. Additional sample rate options may be indicated in the *extended sample rate* field (see below).
- Byte 1: indicates if the audio stream is stereo, mono or some other combination.
  - bits 0–3: Indicates the relationship of the two channels; they might be unrelated audio data, a stereo pair, duplicated mono data, music and voice commentary, a stereo sum/difference code.
  - bits 4–7: Used to indicate the format of the user channel word
- Byte 2: Audio word length
  - bits 0–2: Aux bits usage. This indicates how the aux bits (time slots 4–7) are used. Generally set to 0002 (unused) or 0012 (used for 24-bit audio data).
  - bits 3–5: Word length. Specifies the sample size, relative to the 20- or 24-bit maximum. Can specify 0, 1, 2 or 4 missing bits. Unused bits are filled with 0, but audio processing functions such as mixing will generally fill them in with valid data without changing the effective word length.
  - bits 6–7: Indicates if the alignment level of the audio signal follows either the EBU R68 or the SMPTE RP155 recommendation.
- Byte 3: Used only for multichannel applications
- Byte 4: Additional sample rate information
  - bits 0–1: Indicates the grade of the sample rate reference, per AES11
  - bit 2: Reserved
  - bits 3–6: Extended sample rate. This indicates other sample rates, not representable in byte 0 bits 6–7. Values are assigned for 24, 96, and 192 kHz, as well as 22.05, 88.2, and 176.4 kHz.
  - bit 7: Sampling frequency scaling flag. If set, indicates that the sample rate is multiplied by 1/1.001 to match NTSC video frame rates.
- Byte 5: Reserved
- Bytes 6–9: Four ASCII characters for indicating channel origin. Widely used in large studios.
- Bytes 10–13: Four ASCII characters indicating channel destination, to control automatic switchers. Less often used.
- Bytes 14–17: 32-bit sample address, incrementing block-to-block by 192 (because there are 192 frames per block). At 48 kHz, this wraps approximately every day.
- Bytes 18–21: 32-bit sample address offset to indicate samples since midnight.
- Byte 22: Channel status word reliability indication
  - bits 0–3: Reserved
  - bit 4: If set, bytes 0–5 (signal format) are unreliable.
  - bit 5: If set, bytes 6–13 (channel labels) are unreliable.
  - bit 6: If set, bytes 14–17 (sample address) are unreliable.
  - bit 7: If set, bytes 18–21 (timestamp) are unreliable.
- Byte 23: CRC. This byte is used to detect corruption of the channel status word, as might be caused by switching mid-block.

### Embedded timecode

SMPTE timecode data can be embedded within AES3 signals. It can be used for synchronization and for logging and identifying audio content. It is embedded as a 32-bit binary word in bytes 18 to 21 of the channel status data.

The AES11 standard provides information on the synchronization of digital audio structures.

the AES52 standard describes how to insert unique identifiers into an AES3 bit stream.

### SMPTE 2110

SMPTE 2110-31 defines how to encapsulate an AES3 data stream in Real-time Transport Protocol packets for transmission over an IP network using the SMPTE 2110 IP based multicast framework.

### SMPTE 302M

SMPTE 302M-2007 defines how to encapsulate an AES3 data stream in an MPEG transport stream for television applications.

### Other formats

AES3 digital audio format can also be carried over an Asynchronous Transfer Mode network. The standard for packing AES3 frames into ATM cells is AES47.
