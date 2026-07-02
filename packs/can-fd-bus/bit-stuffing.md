---
title: "Bit stuffing"
source: https://en.wikipedia.org/wiki/Bit_stuffing
domain: can-fd-bus
license: CC-BY-SA-4.0
tags: can fd, flexible data-rate, controller area network, bit stuffing frame
fetched: 2026-07-02
---

# Bit stuffing

In data transmission and telecommunications, **bit stuffing** (also known—uncommonly—as **positive justification**) is the insertion of non-information bits into data. Stuffed bits should not be confused with overhead bits.

Bit stuffing refers to adding extra bits that do not contain any actual information into the data stream. These stuffed bits are different from overhead bits. Overhead bits are also non-data bits, but they are required for transmission, such as those used in headers, checksums, and other control information.

Bit stuffing is used for various purposes, such as for bringing bit streams that do not necessarily have the same or rationally related bit rates up to a common rate, or to fill buffers or frames. The location of the stuffing bits is communicated to the receiving end of the data link, where these extra bits are removed to return the bit streams to their original bit rates or form. Bit stuffing may be used to synchronize several channels before multiplexing or to rate-match two single channels to each other.

Another use of bit stuffing is for run length limited coding: to limit the number of consecutive bits of the same value in the data to be transmitted. A bit of the opposite value is inserted after the maximum allowed number of consecutive bits. Since this is a general rule the receiver doesn't need extra information about the location of the stuffing bits in order to do the de-stuffing. This is done to create additional signal transitions to ensure reliable reception or to escape special reserved code words such as frame sync sequences when the data happens to contain them. This technique is particularly useful in situations where data frames are transmitted over unreliable channels, such as wireless networks or noisy copper wires.

Bit stuffing does not ensure that the payload is intact (*i.e.* not corrupted by transmission errors); it is merely a way of attempting to ensure that the transmission starts and ends at the correct places. Error detection and correction techniques are used to check the frame for corruption after its delivery and, if necessary, the frame will be re-sent.

## Zero-bit insertion

The NRZI coding scheme transmits a 0 bit as a signal transition, and a 1 bit as no change. In this case, bit stuffing is most easily described as the insertion of a 0 bit after a long run of 1 bits.

It was popularized by IBM's SDLC (later renamed HDLC), and is also used in low- and full-speed USB.

After a long sequence of 1 bits there would be no transitions in the transmitted data, and it would be possible for the transmitter and receiver clocks to lose synchronisation. By inserting a 0 after five (SDLC) or six (USB) consecutive 1 bits the transmitter guarantees a maximum of six (SDLC) or seven (USB) bit times between transitions. The receiver can synchronise its clock against the transitions to ensure proper data recovery.

In SDLC the transmitted bit sequence "01111110" containing six adjacent 1 bits is the flag byte. Bit stuffing ensures that this pattern can never occur in normal data, so it can be used as a marker for the beginning and end of the frame without any possibility of being confused with normal data.

The main disadvantage of bit-stuffing is that the code rate is unpredictable; it depends on the data being transmitted.

*Source: from Federal Standard 1037C in support of MIL-STD-188*
