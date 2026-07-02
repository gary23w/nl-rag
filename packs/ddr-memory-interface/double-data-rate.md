---
title: "Double data rate"
source: https://en.wikipedia.org/wiki/Double_data_rate
domain: ddr-memory-interface
license: CC-BY-SA-4.0
tags: ddr memory interface, double data rate, dram memory controller, ddr5 sdram
fetched: 2026-07-02
---

# Double data rate

In computing, **double data rate** (**DDR**) describes a computer bus that transfers data on both the rising and falling edges of the clock signal and hence doubles the memory bandwidth by transferring data twice per clock cycle. This is also known as **double pumped**, **dual-pumped**, and **double transition**. The term **toggle mode** is used in the context of NAND flash memory.

## Overview

The simplest way to design a clocked electronic circuit is to make it perform one transfer per full cycle (rise and fall) of a clock signal. This, however, requires that the clock signal changes twice per transfer, while the data lines change at most once per transfer. When operating at a high bandwidth, signal integrity limitations constrain the clock frequency. By using both edges of the clock, the data signals operate with the same limiting frequency, thereby doubling the data transmission rate.

This technique has been used for microprocessor front-side busses, Ultra-3 SCSI, expansion buses (AGP, PCI-X), graphics memory (GDDR), main memory (both RDRAM and DDR1 through DDR5), and the HyperTransport bus on AMD's Athlon 64 processors. It is more recently being used for other systems with high data transfer speed requirements – as an example, for the output of analog-to-digital converters (ADCs).

DDR should not be confused with dual channel, in which each memory channel accesses two RAM modules simultaneously. The two technologies are independent of each other and many motherboards use both, by using DDR memory in a dual channel configuration.

An alternative to double or quad pumping is to use self-clocking signals. This tactic was chosen by InfiniBand and PCI Express.

## Relation of bandwidth and frequency

Describing the bandwidth of a double-pumped bus can be confusing. Each clock edge is referred to as a *beat*, with two beats (one upbeat and one downbeat) per cycle. Technically, the hertz is a unit of *cycles* per second, but many people refer to the number of *transfers* per second. Careful usage generally talks about "500 MHz, double data rate" or "1000 MT/s", but many refer casually to a "1000 MHz bus," even though no signal cycles faster than 500 MHz.

Using the letter "T" for transfers is technically incorrect, as T is assigned by the International System of Units to the Tesla, a unit of magnetic flux density, so "MT/s" is a rate of change of magnetic field strength. However, given that such rapid magnetic field changes are confined to the specialized field of kicker magnet design, and such a magnet might switch a 0.03 T field in 0.3 μs, a rate of 0.1 T/μs = 0.1 MT/s, the ambiguity is not a problem in practice.

DDR SDRAM popularized the technique of referring to the bus bandwidth in megabytes per second, the product of the transfer rate and the bus width in bytes. DDR SDRAM operating with a 100 MHz clock is called DDR-200 (after its 200 MT/s data transfer rate), and a 64-bit (8-byte) wide DIMM operated at that data rate is called PC-1600, after its 1600 MB/s peak (theoretical) bandwidth. Likewise, 12.8 GB/s transfer rate DDR3-1600 is called PC3-12800.

Some examples of popular designations of DDR modules:

| Names | Memory clock | I/O bus clock | Transfer rate | Theoretical bandwidth |
|---|---|---|---|---|
| DDR-200, PC-1600 | 100 MHz | 100 MHz | 200 MT/s | 1.6 GB/s |
| DDR-400, PC-3200 | 200 MHz | 200 MHz | 400 MT/s | 3.2 GB/s |
| DDR2-800, PC2-6400 | 200 MHz | 400 MHz | 800 MT/s | 6.4 GB/s |
| DDR3-1600, PC3-12800 | 200 MHz | 800 MHz | 1600 MT/s | 12.8 GB/s |
| DDR4-2400, PC4-19200 | 300 MHz | 1200 MHz | 2400 MT/s | 19.2 GB/s |
| DDR4-3200, PC4-25600 | 400 MHz | 1600 MHz | 3200 MT/s | 25.6 GB/s |
| DDR5-4800, PC5-38400 | 300 MHz | 2400 MHz | 4800 MT/s | 38.4 GB/s |
| DDR5-6400, PC5-51200 | 400 MHz | 3200 MHz | 6400 MT/s | 51.2 GB/s |

DDR SDRAM uses double-data-rate signaling only on the data lines. Address and control signals are still sent to the DRAM once per clock *cycle* (to be precise, on the rising edge of the clock), and timing parameters such as CAS latency are specified in clock cycles. Some less common DRAM interfaces, notably LPDDR2, GDDR5 and XDR DRAM, also send commands and addresses using double data rate. DDR5 uses two 7-bit double data rate command/address buses to each DIMM, where a registered clock driver chip converts to a 14-bit SDR bus to each memory chip.
