---
title: "GDDR6 SDRAM"
source: https://en.wikipedia.org/wiki/GDDR6_SDRAM
domain: hbm-memory
license: CC-BY-SA-4.0
tags: high bandwidth memory, stacked dram, through-silicon via, silicon interposer
fetched: 2026-07-02
---

# GDDR6 SDRAM

**Graphics Double Data Rate 6 Synchronous Dynamic Random-Access Memory** (**GDDR6 SDRAM**) is a type of synchronous graphics random-access memory (SGRAM) with a high-bandwidth, "double data rate" interface, designed for use in graphics cards, game consoles, and high-performance computing. It is a type of GDDR SDRAM (graphics DDR SDRAM), and is the successor to GDDR5. Just like GDDR5X it uses QDR (quad data rate) in reference to the write command clock (WCK) and ODR (Octal Data Rate) in reference to the command clock (CK).

## Overview

The finalized specification was published by JEDEC in July 2017. GDDR6 offers increased per-pin bandwidth (up to 16 Gbit/s) and lower operating voltages (1.35 V), increasing performance and decreasing power consumption relative to GDDR5X.

## Commercial implementation

At Hot Chips 2016, Samsung announced GDDR6 as the successor of GDDR5X. Samsung later announced that the first products would be 16 Gbit/s, 1.35 V chips. In January 2018, Samsung began mass production of 16 Gb (2 GB) GDDR6 chips, fabricated on a 10 nm class process and with a data rate of up to 18 Gbit/s per pin.

In February 2017, Micron Technology announced it would release its own GDDR6 products by early 2018. Micron began mass production of 8 Gb chips in June 2018.

SK Hynix announced its GDDR6 products would be released in early 2018. SK Hynix announced in April 2017 that its GDDR6 chips would be produced on a 21 nm process and be 10% lower voltage than GDDR5. The SK Hynix chips were expected to have a transfer rate of 14–16 Gbit/s. The first graphics cards to use SK Hynix's GDDR6 RAM were expected to use 12 GB of RAM with a 384-bit memory bus, yielding a bandwidth of 768 GB/s. SK Hynix began mass production in February 2018, with 8 Gbit chips and a data rate of 14 Gbit/s per pin.

Nvidia officially announced the first consumer graphics cards using GDDR6, the Turing-based GeForce RTX 2080 Ti, RTX 2080 & RTX 2070 on August 20, 2018, RTX 2060 on January 6, 2019 and GTX 1660 Ti on February 22, 2019. GDDR6 memory from Samsung Electronics is also used for the Turing-based Quadro RTX series. The RTX 20 series initially launched with Micron memory chips, before switching to Samsung chips by November 2018.

AMD officially announced the Radeon RX 5700, 5700 XT, and 5700 XT 50th Anniversary Edition on June 10, 2019. These Navi 10 GPUs utilize 8 GB of GDDR6 memory.

## GDDR6X

Micron developed GDDR6X in close collaboration with Nvidia. GDDR6X SGRAM had not been standardized by JEDEC yet. Nvidia is Micron's only GDDR6X launch partner. GDDR6X offers increased per-pin bandwidth between 19–21 Gbit/s with PAM4 signaling, allowing two bits per symbol to be transmitted and replacing earlier NRZ (non return to zero, PAM2) coding that provided only one bit per symbol, thereby limiting the per-pin bandwidth of GDDR6 to 16 Gbit/s. The first graphics cards to use GDDR6X are the Nvidia GeForce RTX 3080 and 3090 graphics cards. PAM4 signalling is not new but it costs more to implement, partly because it requires more space in chips and is more prone to signal-to-noise ratio (SNR) issues, which mostly limited its use to high speed networking (like 200G Ethernet). GDDR6X consumes 15% less power per transferred bit than GDDR6, but overall power consumption is higher since GDDR6X is faster than GDDR6. On average, PAM4 consumes less power and uses fewer pins than differential signalling while still being faster than NRZ. GDDR6X is thought to be cheaper than High Bandwidth Memory.

## GDDR6W

Samsung announced the development of GDDR6W on November 29, 2022. Its improvements over GDDR6 are:

- Higher per pin transmission rate of 22 Gb/s
- Doubling per package capacity from 16 Gb to 32 Gb
- Double the I/O pins from 32 to 64
- 36% lower thickness (0.7 mm down from 1.1 mm by using Fan-Out Wafer-Level Packaging (FOWLP)
