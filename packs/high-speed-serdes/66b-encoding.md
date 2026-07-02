---
title: "64b/66b encoding"
source: https://en.wikipedia.org/wiki/64b/66b_encoding
domain: high-speed-serdes
license: CC-BY-SA-4.0
tags: high-speed serdes, line encoding, channel equalization, clock data recovery
fetched: 2026-07-02
---

# 64b/66b encoding

In data networking and transmission, **64b/66b** is a line code that transforms 64-bit data to 66-bit line code to provide enough state changes to allow reasonable clock recovery and alignment of the data stream at the receiver. It was defined by the IEEE 802.3 working group as part of the IEEE 802.3ae-2002 amendment which introduced 10 Gbit/s Ethernet. At the time 64b/66b was deployed, it allowed 10 Gb Ethernet to be transmitted over fiber optic with the same lasers used by SONET OC-192, rather than requiring the 12.5 Gbit/s lasers that were not expected to be available for several years.

The protocol overhead of a coding scheme is the ratio of the number of raw payload bits to the number of raw payload bits plus the number of added coding bits. The overhead of 64b/66b encoding is 2 coding bits for every 64 payload bits or 3.125%. This is a considerable improvement on the 25% overhead of the previously used 8b/10b encoding scheme, which added 2 coding bits to every 8 payload bits.

The overhead can be reduced further by doubling the payload size to produce the **128b/130b** encoding used by PCIe 3.0.

## Function

As its scheme name suggests, 64 payload bits are encoded as a 66-bit entity. The 66-bit entity is made by prefixing one of two possible 2-bit preambles to the 64 payload bits. This 66-bit entity is now of two possible states.

- If the preamble is 012, the 64 payload bits are data.
- If the preamble is 102, the 64 payload bits hold an 8-bit Type field and 56 bits of control information and/or data.

The preambles 002 and 112 are not used and indicate an error if seen.

The use of the 012 and 102 preambles guarantees a bit transition every 66 bits, which means that a continuous stream of 0s or 1s cannot be valid data. It also allows easier clock/timer synchronization, as a transition must be seen every 66 bits.

The 64-bit payload is then scrambled using a self-synchronous scrambler function. Scrambling is not intended to encrypt the data but to ensure that a relatively even distribution of 1s and 0s are found in the transmitted data. The scrambler cannot guarantee that output data will never have a long run-length of 0s or all 1s, or other undesirable properties in communications, but does allow strong statistical bounds to be put on the probability of such events. Practical designs will choose system parameters such that a bit-error due to long run-lengths is vanishingly unlikely. This method is different from the code-book based approach of 8b/10b encoding.

The encoding and scrambling are normally implemented entirely in hardware, with the scrambler using a linear-feedback shift register. Upper layers of the software stack need not be aware that the link layer is using these methods.

## Properties and application

64b/66b's design goals are clock recovery, stream alignment, DC balance, transition density and run length. 8b/10b encoding guarantees strict bounds on DC balance, transition density and run length, whereas 64b/66b provides statistical bounds on these properties.

### Run length

Most clock recovery circuits designed for SONET OC-192 and 64b/66b are specified to tolerate an 80-bit run length. Such a run cannot occur in 64b/66b because transitions are guaranteed at 66-bit intervals, and in fact long runs are very unlikely. Although it is theoretically possible for a random data pattern to align with the scrambler state and produce a long run of 65 zeroes or 65 ones, the probability of such an event is equal to flipping a fair coin and having it come up in the same state 64 times in a row. At 10 Gigabits per second, the expected event rate of a 66-bit block with a 65-bit run-length, assuming random data, is 66×264÷1010÷2 seconds, or about once every 1900 years.

The run length statistics may get worse if the data consists of specifically chosen patterns, instead of being random. An earlier scrambler used in Packet over SONET/SDH (RFC 1619 (1994)) had a short polynomial with only 7 bits of internal state which allowed a malicious attacker to create a denial-of-service attack by transmitting patterns in all 27−1 states, one of which was guaranteed to de-synchronize the clock recovery circuits. This vulnerability was kept secret until the scrambler length was increased to 43 bits (RFC 2615 (1999)) making it impossible for a malicious attacker to jam the system with a short sequence.

64b/66b avoided this vulnerability by using a scrambling polynomial with enough random internal state (58 bits) so that a dedicated attacker using a crafted Ethernet packet can only create a 64-bit run-length in the scrambler output once in about 29 years. This creates 66-bit blocks containing 65-bit runs at a rate similar to using random data.

### DC balance

The DC balance of 64b/66b is not absolutely bounded. However, it can be shown that the scrambler output closely approximates a sequence of random binary bits. Passing such a sequence through an AC-coupled circuit produces a baseline wander noise that follows a Gaussian distribution, and the impact on the system error rate can be statistically quantified. In practice, a modest coupling capacitor value of 1 nF in a 100 Ω system is sufficient to guarantee that a DC drift of more than 2.5% will occur less often than once per 1022 bits (about 31,700 years at 10 Gbit/s).

### Hamming distance

10 Gigabit Ethernet has a strict charter requiring a Mean Time to False Packet Acceptance (MTTFPA) to be on the order of 1 billion years for a single operating link. To achieve this at normal bit error rates requires at least a 4-bit Hamming distance protection for all packet data. In other words, all combinations of 3 randomly spaced bit-flips within a packet boundary must be detected and result in an invalidated packet. Several strategies were combined to achieve the 4-bit Hamming distance for 64b/66b packets: 1) strong type fields were chosen with 4-bit Hamming distance, 2) the scrambler polynomial was chosen to be compatible with the CRC-32 used for packet protection and 3) protocol violations adjacent to the packet boundaries are required to invalidate the packet. The combination of CRC-32 and the chosen scrambler polynomial were evaluated by exhaustively enumerating all 4-bit error patterns for all possible packet sizes with an optimized C program.

### Observations

The main contribution of 64b/66b is the observation that deterministic run length and transition density of 8b/10b are not always worth a 25% code overhead, and that solid robust systems could be designed using statistically bounded methods. At some point, practical risks, whether from mean time between failures (MTBF) of components such as power supplies or from phenomena such as cosmic rays or solar flares, dominate the reliability of both 8b/10b and 64b/66b systems.

### Variations

The Interlaken protocol improves the DC balance further by trading off more coding bits. Its 64b/67b encoding extends 64b/66b with explicit DC balancing. This may be beneficial for some applications, such as using smaller on-chip coupling capacitors.

PCI Express 3.0 introduced 128b/130b encoding, which is similar to 64b/66b but has a payload of 128 bits instead of 64 bits, and uses a different scrambling polynomial: *x*23 + *x*21 + *x*16 + *x*8 + *x*5 + *x*2 + 1. It is also not self-synchronous and so requires explicit synchronization of seed values, in contrast with 64b/66b.

USB 3.1 and DisplayPort 2.0 use 128b/132b encoding, which is identical to 64b/66b, but duplicates each of the preamble bits to reduce the risk of undetected errors there.

### Successors

For each {*n*}b/{*n*+2}b encoding, the symbol/data ratio is always below 1. With a ratio of 0.985 for 128b/130b encoding, there is no real margin for improvement.

The following approaches are available to further increase the data rate:

**Higher symbol rates combined with FEC**

Very common are 512b/514b encodings combined with Reed–Solomon error correction. The following variants are often used:

- RS(528,514,07,10), adding 14 correction bits to the 512b/514b code word, allowing to correct up to 07 corrupted bits. Overhead is 3%, same as 64b/66b encoding.
- RS(544,514,14,10), adding 30 correction bits to the 512b/514b code word, allowing to correct up to 15 corrupted bits. Overhead is 6%.

The FEC allows symbol error rates of 2.3 · 10−5 or 2.2 · 10−4 to achieve a bit error rate of less than 10−15 in the transmitted data.

**Multi-level encoding combined with FEC**

Further improvements are possible by switching from PAM-2 to PAM-4 or Ensemble NRZ coding.

**Multi-level Trellis modulation combined with FEC**

## Technologies that use 64b/66b encoding

- 100 Gigabit Ethernet
- 10G-EPON, 10 Gbit/s Ethernet Passive Optical Network
- 10 Gigabit Ethernet (most varieties)
- Aurora, from Xilinx
- Camera Link HS
- Common Public Radio Interface
- Fibre Channel 10GFC and 16GFC
- InfiniBand
- Thunderbolt
- JESD204C

## Technologies that use 128b/1xxb encoding

- NVLink 1.0
- PCIe 3.x
- PCIe 4.x
- PCIe 5.x
- SATA 3.2
- SAS 4
- USB 3.1 Gen2
- USB4
- DisplayPort 2.0

## Technologies that use 256b/257b encoding

- Fibre Channel 32GFC "Gen 6" and higher
