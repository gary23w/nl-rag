---
title: "InfiniBand"
source: https://en.wikipedia.org/wiki/InfiniBand
domain: rdma-networking
license: CC-BY-SA-4.0
tags: remote direct memory access, zero-copy transfer, kernel bypass, low latency networking
fetched: 2026-07-02
---

# InfiniBand

**InfiniBand** (**IB**) is a computer networking standard used in high-performance computing that features very high throughput and very low latency. It is used for data interconnect both among and within computers. InfiniBand is also used as either a direct or switched interconnect between servers and storage systems, as well as an interconnect between storage systems. It is designed to be scalable and uses a switched fabric network topology. Between 2014 and June 2016, it was the most commonly used interconnect in the TOP500 list of supercomputers.

Mellanox (acquired by Nvidia) manufactures InfiniBand host bus adapters and network switches, which are used by large computer system and database vendors in their product lines.

As a computer cluster interconnect, IB competes with Ethernet, Fibre Channel, and Intel Omni-Path. The technology is promoted by the **InfiniBand Trade Association**.

## History

InfiniBand originated in 1999 from the merger of two competing designs: Future I/O and Next Generation I/O (NGIO). NGIO was led by Intel, with a specification released in 1998, and joined by Sun Microsystems and Dell. Future I/O was backed by Compaq, IBM, and Hewlett-Packard. This led to the formation of the InfiniBand Trade Association (IBTA), which included both sets of hardware vendors as well as software vendors such as Microsoft. At the time it was thought some of the more powerful computers were approaching the interconnect bottleneck of the PCI bus, in spite of upgrades like PCI-X. Version 1.0 of the InfiniBand Architecture Specification was released in 2000. Initially the IBTA vision for IB was simultaneously a replacement for PCI in I/O, Ethernet in the machine room, cluster interconnect and Fibre Channel. IBTA also envisaged decomposing server hardware on an IB fabric.

Mellanox had been founded in 1999 to develop NGIO technology, but by 2001 shipped an InfiniBand product line called InfiniBridge at 10 Gbit/second speeds. Following the burst of the dot-com bubble there was hesitation in the industry to invest in such a far-reaching technology jump. By 2002, Intel announced that instead of shipping IB integrated circuits ("chips"), it would focus on developing PCI Express, and Microsoft discontinued IB development in favor of extending Ethernet. Sun Microsystems and Hitachi continued to support IB.

In 2003, the System X supercomputer built at Virginia Tech used InfiniBand in what was estimated to be the third largest computer in the world at the time. The OpenIB Alliance (later renamed OpenFabrics Alliance) was founded in 2004 to develop an open set of software for the Linux kernel. By February, 2005, the support was accepted into the 2.6.11 Linux kernel. In November 2005 storage devices finally were released using InfiniBand from vendors such as Engenio. Cisco, desiring to keep technology superior to Ethernet off the market, adopted a "buy to kill" strategy. Cisco successfully killed InfiniBand switching companies such as Topspin via acquisition.

Of the top 500 supercomputers in 2009, Gigabit Ethernet was the internal interconnect technology in 259 installations, compared with 181 using InfiniBand. In 2010, market leaders Mellanox and Voltaire merged, leaving just one other IB vendor, QLogic, primarily a Fibre Channel vendor. At the 2011 International Supercomputing Conference, links running at about 56 gigabits per second (known as FDR, see below), were announced and demonstrated by connecting booths in the trade show. In 2012, Intel acquired QLogic's InfiniBand technology, leaving only one independent supplier.

By 2014, InfiniBand was the most popular internal connection technology for supercomputers, although within two years, 10 Gigabit Ethernet started displacing it.

In 2016, it was reported that Oracle Corporation (an investor in Mellanox) might engineer its own InfiniBand hardware.

In 2019 Nvidia acquired Mellanox, the last independent supplier of InfiniBand products.

## Specification

Specifications are published by the InfiniBand trade association.

### Performance

Original names for speeds were single-data rate (SDR), double-data rate (DDR) and quad-data rate (QDR) as given below. Subsequently, other three-letter initialisms were added for even higher data rates.

InfiniBand unidirectional data rates

Year

Line code

Signaling rate (Gbit/s)

Throughput

(Gbit/s)

Adapter latency (μs)

1x

4x

8x

12x

SDR

2001, 2003

NRZ

8b/10b

2.5

2

8

16

24

5

DDR

2005

5

4

16

32

48

2.5

QDR

2007

10

8

32

64

96

1.3

FDR10

2011

64b/66b

10.3125

10

40

80

120

0.7

FDR

2011

14.0625

13.64

54.54

109.08

163.64

0.7

EDR

2014

25.78125

25

100

200

300

0.5

HDR

2018

PAM4

256b/257b

53.125

50

200

400

600

<0.6

NDR

2022

106.25

100

400

800

1200

?

XDR

2024

212.5

200

800

1600

2400

?

GDR

TBA

~

425

400

1600

3200

4800

?

LDR

TBA

~

850

800

3200

6400

9600

?

**Notes**

1. Using Reed-Solomon forward error correction

Each link is duplex. Links can be aggregated: most systems use a 4 link/lane connector (QSFP). HDR often makes use of 2x links (aka HDR100, 100 Gb link using 2 lanes of HDR, while still using a QSFP connector). NDR introduced OSFP connectors which host one or two links at 2x (NDR200) or 4x (NDR400). They are not logically configured as a single 8x link, even when connecting switches together with an OSFP cable.

InfiniBand provides remote direct memory access (RDMA) capabilities for low CPU overhead.

### Topology

InfiniBand uses a switched fabric topology, as opposed to early shared medium Ethernet. All transmissions begin or end at a channel adapter. Each processor contains a host channel adapter (HCA) and each peripheral has a target channel adapter (TCA). These adapters can also exchange information for security or quality of service (QoS).

### Messages

InfiniBand transmits data in packets of up to 4 KB that are taken together to form a message. A message can be:

- a remote direct memory access read or write
- a channel send or receive
- a transaction-based operation (that can be reversed)
- a multicast transmission
- an atomic operation

### Physical interconnection

In addition to a board form factor connection, it can use both active and passive copper (up to 10 meters) and optical fiber cable (up to 10 km). QSFP connectors are used.

The InfiniBand Association also specified the CXP connector system for speeds up to 120 Gbit/s over copper, active optical cables, and optical transceivers using parallel multi-mode fiber cables with 24-fiber MPO connectors.

### Software interfaces

Mellanox operating system support is available for Solaris, FreeBSD, Red Hat Enterprise Linux, SUSE Linux Enterprise Server (SLES), Windows, HP-UX, VMware ESX, and AIX.

InfiniBand has no specific standard application programming interface (API). The standard only lists a set of verbs such as `ibv_open_device` or `ibv_post_send`, which are abstract representations of functions or methods that must exist. The syntax of these functions is left to the vendors. Sometimes for reference this is called the *verbs* API. The de facto standard software is developed by OpenFabrics Alliance and called the Open Fabrics Enterprise Distribution (OFED). It is released under two licenses GPL2 or BSD license for Linux and FreeBSD, and as Mellanox OFED for Windows (product names: WinOF / WinOF-2; attributed as host controller driver for matching specific ConnectX 3 to 5 devices) under a choice of BSD license for Windows. It has been adopted by most of the InfiniBand vendors, for Linux, FreeBSD, and Microsoft Windows. IBM refers to a software library called `libibverbs`, for its AIX operating system, as well as "AIX InfiniBand verbs". The Linux kernel support was integrated in 2005 into the kernel version 2.6.11.

### Ethernet over InfiniBand

Ethernet over InfiniBand, abbreviated to EoIB, is an Ethernet implementation over the InfiniBand protocol and connector technology. EoIB enables multiple Ethernet bandwidths varying on the InfiniBand (IB) version. Ethernet's implementation of the Internet Protocol Suite, usually referred to as TCP/IP, is different in some details compared to the direct InfiniBand protocol in IP over IB (IPoIB).

| Type | Lanes | Bandwidth (Gbit/s) | Compatible Ethernet type(s) | Compatible Ethernet quantity |
|---|---|---|---|---|
| SDR | 001 | 0002.5 | GbE to 2.5 GbE | 02 × GbE to 1 × 02.5 GbE |
| 004 | 0010 | GbE to 10 GbE | 10 × GbE to 1 × 10 GbE |   |
| 008 | 0020 | GbE to 10 GbE | 20 × GbE to 2 × 10 GbE |   |
| 012 | 0030 | GbE to 25 GbE | 30 × GbE to 1 × 25 GbE + 1 × 05 GbE |   |
| DDR | 001 | 0005 | GbE to 5 GbE | 05 × GbE to 1 × 05 GbE |
| 004 | 0020 | GbE to 10 GbE | 20 × GbE to 2 × 10 GbE |   |
| 008 | 0040 | GbE to 40 GbE | 40 × GbE to 1 × 40 GbE |   |
| 012 | 0060 | GbE to 50 GbE | 60 × GbE to 1 × 50 GbE + 1 × 10 GbE |   |
| QDR | 001 | 0010 | GbE to 10 GbE | 10 × GbE to 1 × 10 GbE |
| 004 | 0040 | GbE to 40 GbE | 40 × GbE to 1 × 40 GbE |   |
