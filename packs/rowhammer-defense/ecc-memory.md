---
title: "ECC memory"
source: https://en.wikipedia.org/wiki/ECC_memory
domain: rowhammer-defense
license: CC-BY-SA-4.0
tags: rowhammer defense, dram disturbance mitigation, target row refresh, bit flip attack defense
fetched: 2026-07-02
---

# ECC memory

**Error correction code memory** (**ECC memory**) is a type of computer data storage that uses an error correction code (ECC) to detect and correct *n*-bit data corruption which occurs in memory.

Typically, ECC memory maintains a memory system immune to single-bit errors: the data that is read from each word is always the same as the data that had been written to it, even if one of the bits actually stored has been flipped to the wrong state. Most non-ECC memory cannot detect errors, although some non-ECC memory with parity support allows detection but not correction.

ECC memory is used in most computers where data corruption cannot be tolerated, like industrial control applications, critical databases, and infrastructural memory caches.

## Background: memory errors

### Concept

Error correction codes protect against undetected data corruption and are used in computers where such corruption is unacceptable, examples being scientific and financial computing applications, or in database and file servers. ECC can also reduce the number of crashes in multi-user server applications and maximum-availability systems.

Electrical or magnetic interference inside a computer system can cause a single bit of dynamic random-access memory (DRAM) to spontaneously flip to the opposite state. It was initially thought that this was mainly due to alpha particles emitted by contaminants in chip packaging material, but research has shown that the majority of one-off soft errors in DRAM chips occur as a result of background radiation, chiefly neutrons from cosmic ray secondaries, which may change the contents of one or more memory cells or interfere with the circuitry used to read or write to them. Hence, the error rates increase rapidly with rising altitude; for example, compared to sea level, the rate of neutron flux is 3.5 times higher at 1.5 km and 300 times higher at 10–12 km (the cruising altitude of commercial airplanes). As a result, systems operating at high altitudes require special provisions for reliability.

As an example, the spacecraft *Cassini–Huygens*, launched in 1997, contained two identical flight recorders, each with 2.5 gigabits of memory in the form of arrays of commercial DRAM chips. Due to built-in EDAC functionality, the spacecraft's engineering telemetry reported the number of (correctable) single-bit-per-word errors and (uncorrectable) double-bit-per-word errors. During the first 2.5 years of flight, the spacecraft reported a nearly constant single-bit error rate of about 280 errors per day. However, on November 6, 1997, during the first month in space, the number of errors increased by more than a factor of four on that single day. This was attributed to a solar particle event that had been detected by the satellite GOES 9.

There was some concern that as DRAM density increases further, and thus the components on chips get smaller, while operating voltages continue to fall, DRAM chips will be affected by such radiation more frequently, since lower-energy particles will be able to change a memory cell's state. On the other hand, smaller cells make smaller targets, and moves to technologies such as SOI may make individual cells less susceptible and so counteract, or even reverse, this trend. Recent studies show that single-event upsets due to cosmic radiation have been dropping dramatically with process geometry, and previous concerns over increasing bit cell error rates are unfounded.

### Real-world error rates and consequences

Work published between 2007 and 2009 showed widely varying error rates with over 7 orders of magnitude difference, ranging from 10−10 error/(bit·h), roughly one bit error per hour per gigabyte of memory, to 10−17 error/(bit·h), roughly one bit error per millennium per gigabyte of memory. A large-scale study based on Google's very large number of servers was presented at the SIGMETRICS/Performance '09 conference. The actual error rate found was several orders of magnitude higher than the previous small-scale or laboratory studies, with between 25,000 (2.5×10−11 error/(bit·h)) and 70,000 (7.0×10−11 error/(bit·h), or 1 bit error per gigabyte of RAM per 1.8 hours) errors per billion device hours per megabit. More than 8% of DIMM memory modules were affected by errors per year.

The consequence of a memory error is system-dependent. In systems without ECC, an error can lead either to a crash or to corruption of data; in large-scale production sites, memory errors are one of the most-common hardware causes of machine crashes. Memory errors can cause security vulnerabilities. A memory error can have no consequences if it changes a bit which neither causes observable malfunctioning nor affects data used in calculations or saved. A 2010 simulation study showed that, for a web browser, only a small fraction of memory errors caused data corruption, although, as many memory errors are intermittent and correlated, the effects of memory errors were greater than would be expected for independent soft errors.

Some tests conclude that the isolation of DRAM memory cells can be circumvented by unintended side effects of specially crafted accesses to adjacent cells. Thus, accessing data stored in DRAM causes memory cells to leak their charges and interact electrically, as a result of high cell density in modern memory, altering the content of nearby memory rows that actually were not addressed in the original memory access. This effect is known as row hammer, and it has also been used in some privilege escalation computer security exploits.

An example of a single-bit error that would be ignored by a system with no error-checking, would halt a machine with parity checking or be invisibly corrected by ECC: a single bit is stuck at 1 due to a faulty chip, or becomes changed to 1 due to background or cosmic radiation; a spreadsheet storing numbers in ASCII format is loaded, and the character "8" (decimal value 56 in the ASCII encoding) is stored in the byte that contains the stuck bit at its lowest bit position; then, a change is made to the spreadsheet and it is saved. As a result, the "8" (0011 100**0** binary) has silently become a "9" (0011 100**1**).

### Solutions

Several approaches have been developed to deal with unwanted bit-flips, including immunity-aware programming, RAM parity memory, and ECC memory.

This problem can be mitigated by using DRAM modules that include extra memory bits and memory controllers that exploit these bits. These extra bits are used to record parity or to use an error-correcting code (ECC). Parity allows the detection of all single-bit errors (actually, any odd number of wrong bits), but not correction, so the system has to either carry on (just flagging the problem) or halt. Error-correction codes allow for more errors to be corrected; how much depends on the exact type of memory used.

DRAM memory may provide increased protection against soft errors by relying on error-correcting codes. Such error-correcting memory, known as *ECC* or *EDAC-protected* memory, is particularly desirable for highly fault-tolerant applications, such as servers, as well as deep-space applications due to increased radiation.

Some systems also "scrub" the memory, by periodically reading all addresses and writing back corrected versions if necessary to remove accumulated soft errors.

## Schemes

Modern memory subsystems may deliver data integrity through one or more of the following schemes:

- By memory controller: These schemes have the memory controller send or receive extra data to the chip.
  - **Side-band ECC** (SBECC) is the traditional server approach. ECCs are stored in separate DRAM chips and transmitted with data through additional channels (extra bits per word). The memory controller computes ECCs when writing, corrects errors when reading and reports error corrections and detections to the operating system or firmware (UEFI or BIOS).
  - **Inline ECC** or **In-band ECC** (IBECC) does not use extra channel width and are as a result compatible with "non-ECC" memory modules. The memory controller partitions the physical space.
    - In one style of implementation represented by Intel's IBECC and TI's RTOS processor, the physical address space is partitioned so that there is a chunk of reserved memory. Each write-command would need to be accompanied by an addition write-command and the same applies to read-commands. This results in an approximate doubling of memory latency. Specifically, Intel's implementation has minimal performance impact on web browsing and productivity applications, but can reduce performance by up to 25% in gaming and video editing workloads.
    - It is theoretically possible to simply partition the existing channel (say, 64 bits into 56 bits of data and 8 bits of checking) to provide for an analogue of side-band ECC. A cursory read of Synopsys's description of "inline ECC" mentioning a partitioning of the 16-bit channel-per-chip would lead to this understanding, but this is not very common in commercial products.
- By memory chip: **On-die ECC** (ODECC), also called in-DRAM ECC or integrated ECC, is mandatory in all DDR5 and LPDDR6 memory modules to mitigate higher error rates associated with smaller memory cells. Additional ECC storage and error correction circuitry are embedded in DRAM chips and are invisible to the memory controller. Transmission errors are not corrected since ECCs are not sent with the data, and error corrections and detections are not reported. Additional latency is introduced only when error correction is needed.
- By both
  - **Link ECC** adds error-correction to the data link but not the underlying storage. The memory controller computes and transmits ECCs with the data when writing to the DRAM, which verifies and corrects errors. When reading, the DRAM computes ECCs that the memory controller then verifies. It is a part of LPDDR5. While side-band ECC automatically provides link-level redundancy, inband/inline ECC using physical address space reserving and on-die ECC do not; they would need a layer of *link ECC* to protect against corruption in transmission.

### Reporting of error

Many early implementations of ECC memory, as well as on-die ECC, mask correctable errors, acting "as if" the error never occurred, and only report uncorrectable errors. Modern implementations log both correctable errors (CE) and uncorrectable errors (UE). Some people proactively replace memory modules that exhibit high error rates, in order to reduce the likelihood of uncorrectable error events.

## Implementations

### Standard server memory: side-band SECDEC

Standard server memory are designed for a single-error correction and double-error detection (SECDED) Hamming code, which allows a single-bit error to be corrected and double-bit errors to be detected per word (the unit of bus transfer). Since DDR SDRAM, the standard bus width (word size) as far as memory is concerned is 64 bits. As a result, the typical setup between DDR and DDR4 is a 72-bit word with 64 data bits and 8 checking bits. DDR5 SDRAM splits the bus into two somewhat independent 32-bit subchannels, so ECC memory uses 80 bits of width in total, split between two 40-bit (32 data, 8 checking) channels. ECC is also used with smaller and larger sizes.

An ECC-capable memory controller uses the additional bits to store the SECDED code; the memory is only responsible for holding the extra bits. Since the late 1990s, the memory controller also communicates to the BIOS and maintains a count of errors detected and corrected, in part to help identify failing memory modules before the problem becomes catastrophic. Reading the counter is supported on many systems thanks to the SMBIOS standard, being available on Linux, BSD, and Windows (Windows 2000 and later).

### Layout of bits

Error detection and correction depends on an expectation of the kinds of errors that occur. Implicitly, it is assumed that the failure of each bit in a word of memory is independent, resulting in improbability of two simultaneous errors. This used to be the case when memory chips were one-bit wide, what was typical in the first half of the 1980s; later developments moved many bits into the same chip.

This weakness is addressed by various technologies, including IBM's Chipkill, Sun Microsystems' Extended ECC, Hewlett-Packard's Chipspare, and Intel's Single Device Data Correction (SDDC), all of which make sure that the failure of one memory chip would only affect one bit per ECC word. This is achieved by scattering the bits of ECC words across chips, a form of interleaving. To make sure each chip only gets one bit per word, it may be necessary to interleave across multiple memory modules (sticks).

Interleaving in general is a useful technique to defend against correlated multi-bit failures. A cosmic ray, for example, may upset multiple physically neighboring bits across multiple words by associating neighboring bits to different words. As long as a single-event upset (SEU) does not exceed the error threshold (e.g., a single error) in any particular word between accesses, it can be corrected (e.g., by a single-bit error-correcting code), and an effectively error-free memory system may be maintained.

### By memory chip itself

Some DRAM chips include internal "on-chip" or "on-die" error-correction circuits, which allow systems with non-ECC memory controllers to still gain most of the benefits of ECC memory. In some systems, a similar effect may be achieved by using EOS memory modules.

As mentioned above, on-die ECC is mandatory on DDR5 and LPDDR6. However, its lack of reporting means that very little is known about the true state of the memory chip until the errors exceed the ability for the on-die algorithm to perform correction; no information on how much "margin" there is conveyed. Sophisticated algorithms have been built to infer the existence of corrected errors based on non-corrected errors.

### Location of correction

Many ECC memory systems use an "external" EDAC circuit between the CPU and the memory. A few systems with ECC memory use both internal and external EDAC systems; the external EDAC system should be designed to correct certain errors that the internal EDAC system is unable to correct. Modern desktop and server CPUs integrate the EDAC circuit into the CPU, even before the shift toward CPU-integrated memory controllers, which are related to the NUMA architecture. CPU integration enables a zero-penalty EDAC system during error-free operation.

### Correction algorithms

As of 2009, the most-common error-correction codes use Hamming or Hsiao codes that provide single-bit error correction and double-bit error detection (SEC-DED). Other error-correction codes have been proposed for protecting memory – double-bit error correcting and triple-bit error detecting (DEC-TED) codes, single-nibble error correcting and double-nibble error detecting (SNC-DND) codes, Reed–Solomon error correction codes, etc. However, in practice, multi-bit correction is usually implemented by interleaving multiple SEC-DED codes.

Early research attempted to minimize the area and delay overheads of ECC circuits. Hamming first demonstrated that SEC-DED codes were possible with one particular check matrix. Hsiao showed that an alternative matrix with odd-weight columns provides SEC-DED capability with less hardware area and shorter delay than traditional Hamming SEC-DED codes. More recent research also attempts to minimize power in addition to minimizing area and delay.

#### Redundancy instead of ECC

Error-correcting memory controllers traditionally use space-optimal error-correction codes such as Hamming and Hsiao. If cost and space is not a concern but speed is, a triple modular redundancy (TMR) may be used due for its faster hardware implementation. Space satellite systems often use TMR, although satellite RAM usually uses Hamming error correction.

### Personal computers

Seymour Cray famously said "parity is for farmers" when asked why he left this out of the CDC 6600. Later, he included parity in the CDC 7600, which caused pundits to remark that "apparently a lot of farmers buy computers". The original IBM PC and all PCs until the early 1990s used parity checking. Later ones mostly did not.

Most data paths on a 2020s personal computer, including PCIe, SATA, chip-to-chip interconnection, and on-disk storage, have some form of ECC protection. The lack of ECC on main memory is in comparison unusual, especially given the size and higher likelihood of corruption. Linus Torvalds wrote a long post in a forum in 2021 attacking Intel's choice to forgo ECC support on desktop platforms, when contemporary AMD desktop platforms could use (but not necessary enable the ECC feature on) registered DIMMs with ECC support.

## Cache

Many CPUs use error-correction codes in the on-chip cache, including the Intel Itanium, Xeon, Core and Pentium (since P6 microarchitecture) processors, the AMD Athlon, Opteron, all Zen- and Zen+-based processors (EPYC, EPYC Embedded, Ryzen and Ryzen Threadripper), and the DEC Alpha 21264.

As of 2006, EDC/ECC and ECC/ECC are the two most-common cache error-protection techniques used in commercial microprocessors. The EDC/ECC technique uses an error-detecting code (EDC) in the level 1 cache. If an error is detected, data is recovered from ECC-protected level 2 cache. The ECC/ECC technique uses an ECC-protected level 1 cache and an ECC-protected level 2 cache. CPUs that use the EDC/ECC technique always write-through all STOREs to the level 2 cache, so that when an error is detected during a read from the level 1 data cache, a copy of that data can be recovered from the level 2 cache.

## Registered memory

Registered, or buffered, memory is not the same as ECC; the technologies perform different functions. It is usual for memory used in servers to be both registered, to allow many memory modules to be used without electrical problems, and ECC, for data integrity.

## Cost and benefits

The use of ECC to increase data security often comes with a bigger expense, resulting in a marginally slower performance and higher memory costs.

ECC memory is more expensive than non-ECC memory due to its additional error-checking functionality. The added extra cost of ECC memory for 1 GB in 2010 varies between $0 and $15, depending on performance and manufacturer. The design of ECC and its purpose in high-reliability workloads positioned it to have additional overhead for validation and the added extra circuit-level designs within the memory. The said features typically result in higher costs for the implementation of ECC.

Motherboard manufacturers may choose to add ECC compatibility of varying levels depending on the market segment. Some ECC-enabled boards and processors are able to support unbuffered (unregistered) ECC, but will also work with non-ECC memory; system firmware enables ECC functionality if ECC memory is installed.

ECC may lower memory performance by around 2–3 percent on some systems, depending on the application and implementation, due to the additional time needed for ECC memory controllers to perform error checking. However, modern systems integrate ECC testing into the CPU, generating no additional delay to memory accesses as long as no errors are detected.

This is not the case for **in-band ECC**, which stores tables used for protection in a reserved region of main system memory, supported by Intel for Chromebooks, which showed little impact on web browsing and productivity tasks, but caused up to a 25% reduction in gaming and video editing benchmarks.
