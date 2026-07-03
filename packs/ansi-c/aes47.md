---
title: "AES47"
source: https://en.wikipedia.org/wiki/AES47
domain: ansi-c
license: CC-BY-SA-4.0
tags: ansi c
fetched: 2026-07-03
---

# AES47

**AES47** is a standard which describes a method for transporting AES3 professional digital audio streams over Asynchronous Transfer Mode (ATM) networks.

The Audio Engineering Society (AES) published AES47 in 2002. The method described by AES47 is also published by the International Electrotechnical Commission as **IEC 62365**.

## Introduction

Many professional audio systems are now combined with telecommunication and IT technologies to provide new functionality, flexibility and connectivity over both local and wide area networks. AES47 was developed to provide a standardised method of transporting the standard digital audio per AES3 over telecommunications networks that provide a quality of service required by many professional low-latency live audio uses. AES47 may be used directly between specialist audio devices or in combination with telecommunication and computer equipment with suitable network interfaces. In both cases, AES47 the same physical structured cable used as standard by the telecommunications networks.

Common network protocols like Ethernet use large packet sizes, which produce a larger minimum latency. Asynchronous transfer mode divides data into 48-byte *cells* which provide lower latency.

## History

The original work was carried out at the British Broadcasting Corporation’s R&D department and published as "White Paper 074", which established that this approach provides the necessary performance for professional media production. AES47 was originally published in 2002 and was republished with minor revisions in February 2006. Amendment 1 to AES47 was published in February 2009, adding code points in the ATM Adaptation Layer Parameters Information Element to signal that the time to which each audio sample relates can be identified as specified in AES53.

The change in thinking from traditional ATM network design is not to necessarily use ATM to pass IP traffic (apart from management traffic) but to use AES47 in parallel with standard Ethernet structures to deal with extremely high performance secure media streams.

AES47 has been developed to allow the simultaneous transport and switched distribution of a large number of AES3 linear audio streams at different sample frequencies. AES47 can support any of the standard AES3 sample rates and word size. AES11 Annex D (the November 2005 printing or version of AES11-2003) shows an example method to provide isochronous timing relationships for distributed AES3 structures over asynchronous networks such as AES47 where reference signals may be locked to common timing sources such as GPS. AES53 specifies how timing markers within AES47 can be used to associate an absolute time stamp with individual audio samples as described in AES47 Amendment 1.

An additional standard has been published by the Audio Engineering Society to extend AES3 digital audio carried as AES47 streams to enable this to be transported over standard physical Ethernet hardware. This additional standard is known as AES51-2006.

## AES47 details

For minimum latency, AES47 uses "raw" ATM cells, ATM adaptation layer 0. Each ATM virtual circuit negotiates the parameters of a stream at connection time. In addition to the same rate and number of channels (which may be more than the 2 supported by AES3), the negotiation covers the number of bits per sample and the presence of an optional data byte. The total must be 1, 2, 3, 4 or 6 bytes per sample, so it evenly divides the ATM cell size. AES3 uses 4 bytes per sample (24 bits of sample plus the optional data byte), but AES47 supports additional formats.

The optional data byte contains four "ancillary" bits corresponding to the AES3 VUCP bits. However, the P (parity) bit is replaced by a B bit which is set on the first sample of each audio block, and clear at all other times. This serves the same function as the B (or Z) synchronization preamble.

The other half of the data byte contains three "data protection" bits for error control and a sequencing bit. The concatenation of the sequencing bits from all samples in a cell (combined little-endian) form a sequencing word of 8, 12, 16, or 24 bits. Only the first 12 bits are defined.

The first four bits of the sequencing word are a sequencing number, used to detect dropped cells. This increments by 1 for each cell transmitted.

The second four bits are for error detection, with bit 7 being an even parity bit for the first byte.

The third four bits, if present, are a second sequencing number which can be used to align multiple virtual circuits.

## AES53

**AES53** is a standard first published in October 2006 by the Audio Engineering Society that specifies how the timing markers specified in AES47 may be used to associate an absolute time-stamp with individual audio samples. A recommendation is made to refer these timestamps to the SMPTE epoch which in turn provides a reference to UTC and GPS time. It thus provides a way of aligning streams from disparate sources, including synchronizing audio to video, and also allows the total delay across a network to be controlled when the transit time of individual cells is unknown. This is most effective in systems where the audio is aligned with an absolute time reference such as GPS, but can also be used with a local reference.

This standard may be studied by downloading a copy of the latest version from the AES standards web site as AES53-2018.
