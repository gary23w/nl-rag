---
title: "Apollo Computer"
source: https://en.wikipedia.org/wiki/Apollo_Computer
domain: avid-technology
license: CC-BY-SA-4.0
tags: avid technology
fetched: 2026-07-03
---

# Apollo Computer

**Apollo Computer Inc.** was an American technology corporation headquartered and founded in Chelmsford, Massachusetts. It was founded in 1980 by William Poduska (a founder of Prime Computer) and others. Apollo Computer developed and produced Apollo/Domain workstations in the 1980s. Along with Symbolics and Sun Microsystems, Apollo was one of the first vendors of graphical workstations. Like other computer companies at the time, Apollo produced much of its own hardware and software.

Apollo was acquired by Hewlett-Packard in 1989 for US$476 million (equivalent to $1236 million in 2025), and gradually closed down over the period of 1990–1997. The brand (as "HP Apollo") was resurrected in 2014 as part of HP's high-performance computing portfolio.

## History

Apollo was started in 1980, two years before rival Sun Microsystems. In addition to Poduska, the founders included Dave Nelson (engineering), Mike Greata (engineering), Charlie Spector (COO), Bob Antonuccio (manufacturing), Gerry Stanley (sales and marketing), and Dave Lubrano (finance). The founding engineering team included Mike Sporer, Bernie Stumpf, Russ Barbour, Paul Leach, and Andy Marcuvitz.

Apollo was the first to release a standalone workstation. In 1981, the company unveiled the DN100 workstation, which used the Motorola 68000 microprocessor. Apollo workstations ran Aegis (later replaced by Domain/OS), a proprietary operating system with a Unix alternative shell. Apollo's networking was particularly elegant, among the first to allow demand paging over the network, and allowing a degree of network transparency and low sysadmin-to-machine ratio.

From 1980 to 1987, Apollo was the largest manufacturer of network workstations. Its quarterly sales exceeded $100 million for the first time in late 1986, and by the end of that year, it had the largest worldwide share of the engineering workstations market, at twice the market share of the number two, Sun Microsystems. At the end of 1987, it was third in market share after Digital Equipment Corporation and Sun, but ahead of Hewlett-Packard and IBM. Apollo's largest customers were Mentor Graphics (electronic design), General Motors, Ford, Chrysler, Chicago Research and Trading (Options and Futures) and Boeing.

Apollo was acquired by Hewlett-Packard in 1989 for US$476 million, and gradually closed down over the period 1990–1997. But after acquiring Apollo Computer in 1989, HP integrated a lot of Apollo technology into their own HP 9000 series of workstations and servers. The Apollo engineering center took over PA-RISC workstation development and Apollo became an HP workstation brand name (*HP Apollo 9000*) for a while. Apollo also invented the revision control system *DSEE* (Domain Software Engineering Environment) which inspired IBM IBM DevOps Code ClearCase. DSEE was pronounced "dizzy".

Aegis, like Unix, was based on concepts from the Multics time-sharing operating system. It used the concepts of shell programming (à la Stephen Bourne), single-level store, and object-oriented design. Aegis was written in a proprietary version of Pascal.

The dual 68000 processor configuration was designed to provide automatic page fault switching, with the main processor executing the OS and program instructions, and the "fixer" processor satisfying the page faults. When a page fault was raised, the main CPU was halted in mid (memory) cycle while the fixer CPU would bring the page into memory and then allow the main CPU to continue, unaware of the page fault. Later improvements in the Motorola 68010 processor obviated the need for the dual-processor design.

Certain efficiencies were gained by careful design; for example, the memory page size, network packet, and disk sector were all 1K byte in size. With this arrangement, a page fault could take place across the network as well as on the individual computer and Aegis file system was a single system of memory mapped files across the entire network. The namespace of the network was self discovering as new nodes (workstations) were added.

Domain/OS (Distributed On-line Multi-access Interactive Network/Operating System) was initially a layer over Aegis and was not built on a Unix kernel. Release 10 incorporated large parts of Unix but the burden of backwards compatibility with previous releases led to a system that was larger and significantly slower than the previous ones. In the end, Hewlett Packard shut down the Domain/OS line. Release 10 came out as competitors were gaining ground in the area of graphics and windowing systems, particularly with the trend to open systems and the X Window System.

Another feature was its proprietary token ring network, which was originally designed to support relatively small networks of, at most, dozens of computers in an office environment. It was a superb design, allowing direct memory access page faulting from any hard drive on the network, but it did not inter-operate with any other existing network hardware or software. The industry widely adopted Ethernet and TCP/IP, a more universal, albeit much slower network. Apollo later added support for these industry standards while continuing to support its own Domain networking using both Ethernet and token ring. The Domain network routing was modeled after Xerox Network Systems.

The company moved from a proprietary data bus architecture in favor of IBM's AT-bus, as used in the second generation of IBM PCs, and was simultaneously embracing RISC technology moving towards high-end processors, eventually producing the PRISM line.

The workstation industry in general experienced hard times in the second half of the 1980s, as IBM Personal Computers and IBM PC compatibles began making inroads on their customer base.

Thomas Vanderslice was hired as President and CEO in 1984, and founder William Poduska left the company in 1985 to found Stellar.

The company incurred large losses in 1987 in currency speculation due to the trading activities of one individual, and in 1988 from declining demand for its products. In 1989, Apollo was acquired by Hewlett-Packard for US$476 million (equivalent to $1236 million in 2025). HP support for Apollo products was fragmented for the first few years, but was reorganized in late 1992, at which point there were still some 100,000 users of Apollo products and the user group InterWorks had some 4,500 members. Earlier that year, Sun had already offered discounts on its systems for customers trading in their Apollo machines; HP responded the next winter with a trade-in program of its own, that also allowed trading in hardware from Sun and other vendors in return for a discount on HP workstations.

Apollo was gradually closed down over the period of 1990–1997.

## Models

| System Type | Model | CPU | Speed (MHz) | Display | Release date | Internal name |
|---|---|---|---|---|---|---|
| SAU1 | DN416 | 2× 68000 | 8 | Portrait black & green |   |   |
| SAU1 | DN100 | 2× 68000 | 8 | Portrait BW |   |   |
| SAU1 | DN400 | 2× 68000 | 8 | Portrait BW |   |   |
| SAU1 | DN600 | 2× 68000 | 8 | Color |   |   |
| SAU1 | DN420 | 2× 68000 | 8 | Landscape BW |   |   |
| SAU2 | DN300 | 68010 | 8 | Landscape BW |   | Swallow |
| SAU2 | DN320 | 68010 | 8 | Landscape BW |   | Swallow |
| SAU2 | DN330 | 68020 | 12 | Landscape BW |   | Swallow |
| SAU3 | DSP80, DSP80A | 68010 | 8 | none |   | Sparrow |
| SAU3 | DSP90 | 68020 | 12 | none |   | Sparrow |
| SAU4 | DN460 | Custom 2900 bit slice | ? | BW |   | Tern |
| SAU4 | DN660 | Custom 2900 bit slice | ? | Color |   | Tern |
| SAU4 | DSP160 | Custom 2900 bit slice | ? | none |   | Tern |
| SAU5 | DN550 | 68010 | 10 | VME 600 Graphics |   | Stingray |
| SAU5 | DN560 | 68020 | 12 | VME 600 Graphics |   | Stingray |
| SAU5 | DN570 | 68020 | 16 | Ocelot Graphics Single Card 8 plane |   | Banshee |
| SAU5 | DN580 | 68020 | 16 | Aurora Graphics |   | Banshee |
| SAU5 | DN590 | 68020 | 20 | Aurora Graphics |   | Banshee |
| SAU6 | DN560T | 68020 | 12 | Color |   | Banshee |
| SAU6 | DN570T | 68020 | 16 | Color |   | Banshee |
| SAU6 | DN580T | 68020 | 16 | Color |   | Banshee |
| SAU6 | DN590T | 68020 | 20 | Color |   | Banshee |
| SAU7 | DN3500 | 68030 | 25 | BW / Color |   | Cougar II |
| SAU7 | DN3550 | 68030 | 25 | BW / Color |   |   |
| SAU7 | DN4000 | 68020 | 25 | BW / Color |   | Mink |
| SAU7 | DN4500 | 68030 | 33 | BW / Color |   | Roadrunner |
| SAU8 | DN3000 | 68020 | 12 | BW / Color |   | Otter |
| SAU8 | DN3010, DN3010A | 68020 | 12 | BW / Color |   |   |
| SAU8 | DN3040 | 68020 | 12 | BW / Color |   |   |
| SAU9 | DN2500 | 68030 | 20 | BW / Color |   | Frodo |
| SAU10 | DN10000 | PRISM | 18 | BW / Color |   | AT |
| SAU11 | 9000/425S | 68040 | 25 |   |   | Trailways |
| SAU11 | 9000/425T | 68040 | 25 | HP DIOII |   | Strider |
| SAU11 | 9000/425E | 68040 | 25 |   |   | Woody |
| SAU11 | 9000/433S | 68040 | 33 |   |   | Trailways |
| SAU11 | 9000/433T | 68040 | 33 |   |   |   |
| SAU12 | 9000/400S | 68030 | 50 |   |   | Trailways |
| SAU12 | 9000/400T | 68030 | 50 |   |   | Strider |
| SAU12 | 9000/400DL | 68030 | 50 |   |   |   |
| SAU14 | DN5500 | 68040 | 25 | BW / Color |   | Leopard |
