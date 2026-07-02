---
title: "CPU cache (part 2/2)"
source: https://en.wikipedia.org/wiki/CPU_cache
domain: spectre-mitigation
license: CC-BY-SA-4.0
tags: spectre mitigation, speculative execution defense, cpu side channel defense, branch predictor hardening
fetched: 2026-07-02
part: 2/2
---

## Cache hierarchy in a modern processor

Modern processors have multiple interacting on-chip caches. The operation of a particular cache can be completely specified by the cache size, the cache block size, the number of blocks in a set, the cache set replacement policy, and the cache write policy (write-through or write-back).

While all of the cache blocks in a particular cache are the same size and have the same associativity, typically the "higher-level" caches (called Level 1 cache) have a smaller number of blocks, smaller block size, and fewer blocks in a set, but have very short access times. "Lower-level" caches (i.e. Level 2 and below) have progressively larger numbers of blocks, larger block size, more blocks in a set, and relatively longer access times, but are still much faster than main memory.

Cache entry replacement policy is determined by a cache algorithm selected to be implemented by the processor designers. In some cases, multiple algorithms are provided for different kinds of work loads.

### Specialized caches

Pipelined CPUs access memory from multiple points in the pipeline: instruction fetch, virtual-to-physical address translation, and data fetch (see classic RISC pipeline). The natural design is to use different physical caches for each of these points, so that no one physical resource has to be scheduled to service two points in the pipeline. Thus the pipeline naturally ends up with at least three separate caches (instruction, TLB, and data), each specialized to its particular role.

#### Victim cache

A **victim cache** is a cache used to hold blocks evicted from a CPU cache upon replacement. The victim cache lies between the main cache and its refill path, and holds only those blocks of data that were evicted from the main cache. The victim cache is usually fully associative, and is intended to reduce the number of conflict misses. Many commonly used programs do not require an associative mapping for all the accesses. In fact, only a small fraction of the memory accesses of the program require high associativity. The victim cache exploits this property by providing high associativity to only these accesses. It was introduced by Norman Jouppi from DEC in 1990.

Intel's *Crystalwell* variant of its Haswell processors introduced an on-package 128 MiB eDRAM Level 4 cache which serves as a victim cache to the processors' Level 3 cache. In the Skylake microarchitecture the Level 4 cache no longer works as a victim cache.

#### Trace cache

One of the more extreme examples of cache specialization is the **trace cache** (also known as *execution trace cache*) found in the Intel Pentium 4 microprocessors. A trace cache is a mechanism for increasing the instruction fetch bandwidth and decreasing power consumption (in the case of the Pentium 4) by storing traces of instructions that have already been fetched and decoded.

A trace cache stores instructions either after they have been decoded, or as they are retired. Generally, instructions are added to trace caches in groups representing either individual basic blocks or dynamic instruction traces. The Pentium 4's trace cache stores micro-operations resulting from decoding x86 instructions, providing also the functionality of a micro-operation cache. Having this, the next time an instruction is needed, it does not have to be decoded into micro-ops again.

#### Write Coalescing Cache (WCC)

Write Coalescing Cache is a special cache that is part of L2 cache in AMD's Bulldozer microarchitecture. Stores from both L1D caches in the module go through the WCC, where they are buffered and coalesced. The WCC's task is reducing number of writes to the L2 cache.

#### Micro-operation (μop or uop) cache

A **micro-operation cache** (**μop cache**, **uop cache** or **UC**) is a specialized cache that stores micro-operations of decoded instructions, as received directly from the instruction decoders or from the instruction cache. When an instruction needs to be decoded, the μop cache is checked for its decoded form which is re-used if cached; if it is not available, the instruction is decoded and then cached.

One of the early works describing μop cache as an alternative frontend for the Intel P6 processor family is the 2001 paper *"Micro-Operation Cache: A Power Aware Frontend for Variable Instruction Length ISA"*. Later, Intel included μop caches in its Sandy Bridge processors and in successive microarchitectures like Ivy Bridge and Haswell. AMD implemented a μop cache in their Zen microarchitecture.

Fetching complete pre-decoded instructions eliminates the need to repeatedly decode variable length complex instructions into simpler fixed-length micro-operations, and simplifies the process of predicting, fetching, rotating and aligning fetched instructions. A μop cache effectively offloads the fetch and decode hardware, thus decreasing power consumption and improving the frontend supply of decoded micro-operations. The μop cache also increases performance by more consistently delivering decoded micro-operations to the backend and eliminating various bottlenecks in the CPU's fetch and decode logic.

A μop cache has many similarities with a trace cache, although a μop cache is much simpler thus providing better power efficiency; this makes it better suited for implementations on battery-powered devices. The main disadvantage of the trace cache, leading to its power inefficiency, is the hardware complexity required for its heuristic deciding on caching and reusing dynamically created instruction traces.

#### Branch target instruction cache

A **branch target cache** or **branch target instruction cache**, the name used on ARM microprocessors, is a specialized cache which holds the first few instructions at the destination of a taken branch. This is used by low-powered processors which do not need a normal instruction cache because the memory system is capable of delivering instructions fast enough to satisfy the CPU without one. However, this only applies to consecutive instructions in sequence; it still takes several cycles of latency to restart instruction fetch at a new address, causing a few cycles of pipeline bubble after a control transfer. A branch target cache provides instructions for those few cycles avoiding a delay after most taken branches.

This allows full-speed operation with a much smaller cache than a traditional full-time instruction cache.

#### Smart cache

**Smart cache** is a level 2 or level 3 caching method for multiple execution cores, developed by Intel.

Smart Cache shares the actual cache memory between the cores of a multi-core processor. In comparison to a dedicated per-core cache, the overall cache miss rate decreases when cores do not require equal parts of the cache space. Consequently, a single core can use the full level 2 or level 3 cache while the other cores are inactive. Furthermore, the shared cache makes it faster to share memory among different execution cores.

### Multi-level caches

Another issue is the fundamental tradeoff between cache latency and hit rate. Larger caches have better hit rates but longer latency. To address this tradeoff, many computers use multiple levels of cache, with small fast caches backed up by larger, slower caches. Multi-level caches generally operate by checking the fastest but smallest cache, *level 1* (**L1**), first; if it hits, the processor proceeds at high speed. If that cache misses, the slower but larger next level cache, *level 2* (**L2**), is checked, and so on, before accessing external memory.

As the latency difference between main memory and the fastest cache has become larger, some processors have begun to utilize as many as three levels of on-chip cache. Price-sensitive designs used this to pull the entire cache hierarchy on-chip, but by the 2010s some of the highest-performance designs returned to having large off-chip caches, which is often implemented in eDRAM and mounted on a multi-chip module, as a fourth cache level. In rare cases, such as in the mainframe CPU IBM z15 (2019), all levels down to L1 are implemented by eDRAM, replacing SRAM entirely (for cache, SRAM is still used for registers). Apple's ARM-based Apple silicon series, starting with the A14 and M1, have a 192 KiB L1i cache for each of the high-performance cores, an unusually large amount; however the high-efficiency cores only have 128 KiB. Since then other processors such as Intel's Lunar Lake and Qualcomm's Oryon have also implemented similar L1i cache sizes.

The benefits of L3 and L4 caches depend on the application's access patterns. Examples of products incorporating L3 and L4 caches include the following:

- Alpha 21164 (1995) had 1 to 64 MiB off-chip L3 cache.
- AMD K6-III (1999) had motherboard-based L3 cache.
- IBM POWER4 (2001) had off-chip L3 caches of 32 MiB per processor, shared among several processors.
- Itanium 2 (2003) had a 6 MiB unified level 3 (L3) cache on-die; the Itanium 2 (2003) MX 2 module incorporated two Itanium 2 processors along with a shared 64 MiB L4 cache on a multi-chip module that was pin compatible with a Madison processor.
- Intel's Xeon MP product codenamed "Tulsa" (2006) features 16 MiB of on-die L3 cache shared between two processor cores.
- AMD Phenom (2007) with 2 MiB of L3 cache.
- AMD Phenom II (2008) has up to 6 MiB on-die unified L3 cache.
- Intel Core i7 (2008) has an 8 MiB on-die unified L3 cache that is inclusive, shared by all cores.
- Intel Haswell CPUs with integrated Intel Iris Pro Graphics have 128 MiB of eDRAM acting essentially as an L4 cache.

Finally, at the other end of the memory hierarchy, the CPU register file itself can be considered the smallest, fastest cache in the system, with the special characteristic that it is scheduled in software—typically by a compiler, as it allocates registers to hold values retrieved from main memory for, as an example, loop nest optimization. However, with register renaming most compiler register assignments are reallocated dynamically by hardware at runtime into a register bank, allowing the CPU to break false data dependencies and thus easing pipeline hazards.

Register files sometimes also have hierarchy: The Cray-1 (circa 1976) had eight address "A" and eight scalar data "S" registers that were generally usable. There was also a set of 64 address "B" and 64 scalar data "T" registers that took longer to access, but were faster than main memory. The "B" and "T" registers were provided because the Cray-1 did not have a data cache. (The Cray-1 did, however, have an instruction cache.)

#### Multi-core chips

When considering a chip with multiple cores, there is a question of whether the caches should be shared or local to each core. Implementing shared cache inevitably introduces more wiring and complexity. But then, having one cache per *chip*, rather than *core*, greatly reduces the amount of space needed, and thus one can include a larger cache.

Typically, sharing the L1 cache is undesirable because the resulting increase in latency would make each core run considerably slower than a single-core chip. However, for the highest-level cache (usually L3, the last one called before accessing memory), having a global cache is desirable for several reasons, such as allowing a single core to use the whole cache, reducing data redundancy by making it possible for different processes or threads to share cached data, and reducing the complexity of utilized cache coherency protocols. For example, an eight-core chip with three levels may include an L1 cache for each core, one intermediate L2 cache for each pair of cores, and one L3 cache shared between all cores.

A shared highest-level cache (usually L3, called before accessing memory), is usually referred to as a *last-level cache* (LLC). Additional techniques are used for increasing the level of parallelism when LLC is shared between multiple cores, including slicing it into multiple pieces which are addressing certain ranges of memory addresses, and can be accessed independently.

#### Separate versus unified

In a separate cache structure, instructions and data are cached separately, meaning that a cache line is used to cache either instructions or data, but not both; various benefits have been demonstrated with separate data and instruction translation lookaside buffers. In a unified structure, this constraint is not present, and cache lines can be used to cache both instructions and data.

#### Exclusive versus inclusive

Multi-level caches introduce new design decisions. For instance, in some processors, all data in the L1 cache must also be somewhere in the L2 cache. These caches are called *strictly inclusive*. Other processors (like the AMD Athlon) have *exclusive* caches: data are guaranteed to be in at most one of the L1 and L2 caches, never in both. Still other processors (like the Intel Pentium II, III, and 4) do not require that data in the L1 cache also reside in the L2 cache, although it may often do so. There is no universally accepted name for this intermediate policy; two common names are "non-exclusive" and "partially-inclusive".

The advantage of exclusive caches is that they store more data. This advantage is larger when the exclusive L1 cache is comparable to the L2 cache, and diminishes if the L2 cache is many times larger than the L1 cache. When the L1 misses and the L2 hits on an access, the hitting cache line in the L2 is exchanged with a line in the L1. This exchange is quite a bit more work than just copying a line from L2 to L1, which is what an inclusive cache does.

One advantage of strictly inclusive caches is that when external devices or other processors in a multiprocessor system wish to remove a cache line from the processor, they need only have the processor check the L2 cache. In cache hierarchies which do not enforce inclusion, the L1 cache must be checked as well. As a drawback, there is a correlation between the associativities of L1 and L2 caches: if the L2 cache does not have at least as many ways as all L1 caches together, the effective associativity of the L1 caches is restricted. Another disadvantage of inclusive cache is that whenever there is an eviction in L2 cache, the (possibly) corresponding lines in L1 also have to get evicted in order to maintain inclusiveness. This is quite a bit of work, and would result in a higher L1 miss rate.

Another advantage of inclusive caches is that the larger cache can use larger cache lines, which reduces the size of the secondary cache tags. (Exclusive caches require both caches to have the same size cache lines, so that cache lines can be swapped on a L1 miss, L2 hit.) If the secondary cache is an order of magnitude larger than the primary, and the cache data are an order of magnitude larger than the cache tags, this tag area saved can be comparable to the incremental area needed to store the L1 cache data in the L2.

### Scratchpad memory

Scratchpad memory (SPM), also known as scratchpad, scratchpad RAM or local store in computer terminology, is a high-speed internal memory used for temporary storage of calculations, data, and other work in progress.

### Example: the K8

To illustrate both specialization and multi-level caching, here is the cache hierarchy of the K8 core in the AMD Athlon 64 CPU.

The K8 has four specialized caches: an instruction cache, an instruction TLB, a data TLB, and a data cache. Each of these caches is specialized:

- The instruction cache keeps copies of 64-byte lines of memory, and fetches 16 bytes each cycle. Each byte in this cache is stored in ten bits rather than eight, with the extra bits marking the boundaries of instructions (this is an example of predecoding). The cache has only parity protection rather than ECC, because parity is smaller and any damaged data can be replaced by fresh data fetched from memory (which always has an up-to-date copy of instructions).
- The instruction TLB keeps copies of page table entries (PTEs). Each cycle's instruction fetch has its virtual address translated through this TLB into a physical address. Each entry is either four or eight bytes in memory. Because the K8 has a variable page size, each of the TLBs is split into two sections, one to keep PTEs that map 4 KiB pages, and one to keep PTEs that map 4 MiB or 2 MiB pages. The split allows the fully associative match circuitry in each section to be simpler. The operating system maps different sections of the virtual address space with different size PTEs.
- The data TLB has two copies which keep identical entries. The two copies allow two data accesses per cycle to translate virtual addresses to physical addresses. Like the instruction TLB, this TLB is split into two kinds of entries.
- The data cache keeps copies of 64-byte lines of memory. It is split into 8 banks (each storing 8 KiB of data), and can fetch two 8-byte data each cycle so long as those data are in different banks. There are two copies of the tags, because each 64-byte line is spread among all eight banks. Each tag copy handles one of the two accesses per cycle.

The K8 also has multiple-level caches. There are second-level instruction and data TLBs, which store only PTEs mapping 4 KiB. Both instruction and data caches, and the various TLBs, can fill from the large **unified** L2 cache. This cache is exclusive to both the L1 instruction and data caches, which means that any 8-byte line can only be in one of the L1 instruction cache, the L1 data cache, or the L2 cache. It is, however, possible for a line in the data cache to have a PTE which is also in one of the TLBs—the operating system is responsible for keeping the TLBs coherent by flushing portions of them when the page tables in memory are updated.

The K8 also caches information that is never stored in memory—prediction information. These caches are not shown in the above diagram. As is usual for this class of CPU, the K8 has fairly complex branch prediction, with tables that help predict whether branches are taken and other tables which predict the targets of branches and jumps. Some of this information is associated with instructions, in both the level 1 instruction cache and the unified secondary cache.

The K8 uses an interesting trick to store prediction information with instructions in the secondary cache. Lines in the secondary cache are protected from accidental data corruption (e.g. by an alpha particle strike) by either ECC or parity, depending on whether those lines were evicted from the data or instruction primary caches. Since the parity code takes fewer bits than the ECC code, lines from the instruction cache have a few spare bits. These bits are used to cache branch prediction information associated with those instructions. The net result is that the branch predictor has a larger effective history table, and so has better accuracy.

### More hierarchies

Other processors have other kinds of predictors (e.g., the store-to-load bypass predictor in the DEC Alpha 21264).

These predictors are caches in that they store information that is costly to compute. Some of the terminology used when discussing predictors is the same as that for caches (one speaks of a **hit** in a branch predictor), but predictors are not generally thought of as part of the cache hierarchy.

The K8 keeps the instruction and data caches **coherent** in hardware, which means that a store into an instruction closely following the store instruction will change that following instruction. Other processors, like those in the Alpha and MIPS family, have relied on software to keep the instruction cache coherent. Stores are not guaranteed to show up in the instruction stream until a program calls an operating system facility to ensure coherency.

### Tag RAM

In computer engineering, a *tag RAM* is used to specify which of the possible memory locations is currently stored in a CPU cache. For a simple, direct-mapped design fast SRAM can be used. Higher associative caches usually employ content-addressable memory.


## Implementation

Cache **reads** are the most common CPU operation that takes more than a single cycle. Program execution time tends to be very sensitive to the latency of a level-1 data cache hit. A great deal of design effort, and often power and silicon area are expended making the caches as fast as possible.

The simplest cache is a virtually indexed direct-mapped cache. The virtual address is calculated with an adder, the relevant portion of the address extracted and used to index an SRAM, which returns the loaded data. The data are byte aligned in a byte shifter, and from there are bypassed to the next operation. There is no need for any tag checking in the inner loop – in fact, the tags need not even be read. Later in the pipeline, but before the load instruction is retired, the tag for the loaded data must be read, and checked against the virtual address to make sure there was a cache hit. On a miss, the cache is updated with the requested cache line and the pipeline is restarted.

An associative cache is more complicated, because some form of tag must be read to determine which entry of the cache to select. An N-way set-associative level-1 cache usually reads all N possible tags and N data in parallel, and then chooses the data associated with the matching tag. Level-2 caches sometimes save power by reading the tags first, so that only one data element is read from the data SRAM.

The adjacent diagram is intended to clarify the manner in which the various fields of the address are used. Address bit 31 is most significant, bit 0 is least significant. The diagram shows the SRAMs, indexing, and multiplexing for a 4 KiB, 2-way set-associative, virtually indexed and virtually tagged cache with 64 byte (B) lines, a 32-bit read width and 32-bit virtual address.

Because the cache is 4 KiB and has 64 B lines, there are just 64 lines in the cache, and we read two at a time from a Tag SRAM which has 32 rows, each with a pair of 21 bit tags. Although any function of virtual address bits 31 through 6 could be used to index the tag and data SRAMs, it is simplest to use the least significant bits.

Similarly, because the cache is 4 KiB and has a 4 B read path, and reads two ways for each access, the Data SRAM is 512 rows by 8 bytes wide.

A more modern cache might be 16 KiB, 4-way set-associative, virtually indexed, virtually hinted, and physically tagged, with 32 B lines, 32-bit read width and 36-bit physical addresses. The read path recurrence for such a cache looks very similar to the path above. Instead of tags, virtual hints are read, and matched against a subset of the virtual address. Later on in the pipeline, the virtual address is translated into a physical address by the TLB, and the physical tag is read (just one, as the virtual hint supplies which way of the cache to read). Finally the physical address is compared to the physical tag to determine if a hit has occurred.

Some SPARC designs have improved the speed of their L1 caches by a few gate delays by collapsing the virtual address adder into the SRAM decoders.

### History

The early history of cache technology is closely tied to the invention and use of virtual memory. Because of scarcity and cost of semi-conductor memories, early mainframe computers in the 1960s used a complex hierarchy of physical memory, mapped onto a flat virtual memory space used by programs. The memory technologies would span semi-conductor, magnetic core, drum and disc. Virtual memory seen and used by programs would be flat and caching would be used to fetch data and instructions into the fastest memory ahead of processor access. Extensive studies were done to optimize the cache sizes. Optimal values were found to depend greatly on the programming language used with Algol needing the smallest and Fortran and Cobol needing the largest cache sizes.

In the early days of microcomputer technology, memory access was only slightly slower than register access. But since the 1980s the performance gap between processor and memory has been growing. Microprocessors have advanced much faster than memory, especially in terms of their operating frequency, so memory became a performance bottleneck. While it was technically possible to have all the main memory as fast as the CPU, a more economically viable path has been taken: use plenty of low-speed memory, but also introduce a small high-speed cache memory to alleviate the performance gap. This provided an order of magnitude more capacity—for the same price—with only a slightly reduced combined performance.

#### First TLB implementations

The first documented uses of a TLB were on the GE 645 and the IBM 360/67, both of which used an associative memory as a TLB.

#### First instruction cache

The first documented use of an instruction cache was on the CDC 6600.

#### First data cache

The first documented use of a data cache was on the IBM System/360 Model 85.

#### In 68k microprocessors

The 68010, released in 1982, has a "loop mode" which can be considered a tiny and special-case instruction cache that accelerates loops that consist of only two instructions. The 68020, released in 1984, replaced that with a typical instruction cache of 256 bytes, being the first 68k series processor to feature true on-chip cache memory.

The 68030, released in 1987, is basically a 68020 core with an additional 256-byte data cache, an on-chip memory management unit (MMU), a process shrink, and added burst mode for the caches.

The 68040, released in 1990, has split instruction and data caches of four kilobytes each.

The 68060, released in 1994, has the following: 8 KiB data cache (four-way associative), 8 KiB instruction cache (four-way associative), 96-byte FIFO instruction buffer, 256-entry branch cache, and 64-entry address translation cache MMU buffer (four-way associative).

#### In x86 microprocessors

As the x86 microprocessors reached clock rates of 20 MHz and above in the 386, small amounts of fast cache memory began to be featured in systems to improve performance. This was because the DRAM used for main memory had significant latency, up to 120 ns, as well as refresh cycles. The cache was constructed from more expensive, but significantly faster, SRAM memory cells, which at the time had latencies around 10–25 ns. The early caches were external to the processor and typically located on the motherboard in the form of eight or nine DIP devices placed in sockets to enable the cache as an optional extra or upgrade feature.

Some versions of the Intel 386 processor could support 16 to 256 KiB of external cache.

With the 486 processor, an 8 KiB cache was integrated directly into the CPU die. This cache was termed Level 1 or L1 cache to differentiate it from the slower on-motherboard, or Level 2 (L2) cache. These on-motherboard caches were much larger, with the most common size being 256 KiB. There were some system boards that contained sockets for the Intel 485Turbocache daughtercard which had either 64 or 128 Kbyte of cache memory. The popularity of on-motherboard cache continued through the Pentium MMX era but was made obsolete by the introduction of SDRAM and the growing disparity between bus clock rates and CPU clock rates, which caused on-motherboard cache to be only slightly faster than main memory.

The next development in cache implementation in the x86 microprocessors began with the Pentium Pro, which brought the secondary cache onto the same package as the microprocessor, clocked at the same frequency as the microprocessor.

On-motherboard caches enjoyed prolonged popularity thanks to the AMD K6-2 and AMD K6-III processors that still used Socket 7, which was previously used by Intel with on-motherboard caches. K6-III included 256 KiB on-die L2 cache and took advantage of the on-board cache as a third level cache, named L3 (motherboards with up to 2 MiB of on-board cache were produced). After the Socket 7 became obsolete, on-motherboard cache disappeared from the x86 systems.

The three-level caches were used again first with the introduction of the Intel Xeon MP "Foster Core", where the L3 cache was added to the CPU die. It became common for the total cache sizes to be increasingly larger in newer processor generations, and recently (as of 2011) it is not uncommon to find Level 3 cache sizes of tens of megabytes.

Intel introduced a Level 4 on-package cache with the Haswell microarchitecture. *Crystalwell* Haswell CPUs, equipped with the GT3e variant of Intel's integrated Iris Pro graphics, effectively feature 128 MiB of embedded DRAM (eDRAM) on the same package. This L4 cache is shared dynamically between the on-die GPU and CPU, and serves as a victim cache to the CPU's L3 cache.

#### In ARM microprocessors

The Apple M1 CPU has 128 or 192 KiB of L1 instruction cache for each core (important for latency/single-thread performance), depending on core type. This is an unusually large L1 cache for any CPU type (not just for a laptop); the total cache memory size is not unusually large (the total is more important for throughput) for a laptop, and much larger total (e.g. L3 or L4) sizes are available in IBM's mainframes.

#### Current research

Early cache designs focused entirely on the direct cost of cache and RAM and average execution speed. More recent cache designs also consider energy efficiency, fault tolerance, and other goals.

There are several tools available to computer architects to help explore tradeoffs between the cache cycle time, energy, and area; the CACTI cache simulator and the SimpleScalar instruction set simulator are two open-source options.

### Multi-ported cache

A multi-ported cache is a cache which can serve more than one request at a time. When accessing a traditional cache we normally use a single memory address, whereas in a multi-ported cache we may request N addresses at a time – where N is the number of ports that connected through the processor and the cache. The benefit of this is that a pipelined processor may access memory from different phases in its pipeline. Another benefit is that it allows the concept of super-scalar processors through different cache levels.
