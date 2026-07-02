---
title: "CPU cache (part 1/2)"
source: https://en.wikipedia.org/wiki/CPU_cache
domain: computer-architecture
license: CC-BY-SA-4.0
tags: computer architecture, cpu cache, pipeline, branch prediction, virtual memory, instruction cycle
fetched: 2026-07-02
part: 1/2
---

# CPU cache

A **CPU cache** is a hardware cache used by the central processing unit (CPU) of a computer to reduce the average cost (time or energy) to access data from the main memory. A cache is a smaller, faster memory, located closer to a processor core, which stores copies of the data from frequently used main memory locations, avoiding the need to always refer to main memory which may be tens to hundreds of times slower to access.

Cache memory is typically implemented with static random-access memory (SRAM), which requires multiple transistors to store a single bit. This makes it expensive in terms of the area it takes up, and in modern CPUs the cache is typically the largest part by chip area. The size of the cache needs to be balanced with the general desire for smaller chips which cost less. Some modern designs implement some or all of their cache using the physically smaller eDRAM, which is slower to use than SRAM but allows larger amounts of cache for any given amount of chip area.

Most CPUs have a hierarchy of multiple cache levels (L1, L2, often L3, and rarely even L4), with separate instruction-specific (I-cache) and data-specific (D-cache) caches at level 1. The different levels are implemented in different areas of the chip; L1 is located as close to a CPU core as possible and thus offers the highest speed due to short signal paths, but requires careful design. L2 caches are physically separate from the CPU and operate slower, but place fewer demands on the chip designer and can be made much larger without impacting the CPU design. L3 caches are generally shared among multiple CPU cores.

Other types of caches exist (that are not counted towards the "cache size" of the most important caches mentioned above), such as the translation lookaside buffer (TLB) which is part of the memory management unit (MMU) which most CPUs have. Input/output sections also often contain data buffers that serve a similar purpose.


## Overview

To access data in main memory, a multi-step process is used and each step introduces a delay. For instance, to read a value from memory in a simple computer system the CPU first selects the address to be accessed by expressing it on the address bus and waiting a fixed time to allow the value to settle. The memory device with that value, normally implemented in DRAM, holds that value in a very low-energy form that is not powerful enough to be read directly by the CPU. Instead, it has to copy that value from storage into a small buffer which is connected to the data bus. It then waits a certain time to allow this value to settle before reading the value from the data bus.

By locating the memory physically closer to the CPU the time needed for the buses to settle is reduced, and by replacing the DRAM with SRAM, which hold the value in a form that does not require amplification to be read, the delay within the memory itself is eliminated. This makes the cache much faster both to respond and to read or write. SRAM, however, requires anywhere from four to six transistors to hold a single bit, depending on the type, whereas DRAM generally uses one transistor and one capacitor per bit, which makes it able to store much more data for any given chip area.

Implementing some memory in a faster format can lead to large performance improvements. When trying to read from or write to a location in the memory, the processor checks whether the data from that location is already in the cache. If so, the processor will read from or write to the cache instead of the much slower main memory.

Many modern desktop, server, and industrial CPUs have at least three independent levels of caches (L1, L2 and L3) and different types of caches:

**Translation lookaside buffer (TLB)**

Used to speed up virtual-to-physical address translation for both executable instructions and data. A single TLB can be provided for access to both instructions and data, or a separate Instruction TLB (ITLB) and data TLB (DTLB) can be provided. However, the TLB cache is part of the

memory management unit

(MMU) and not directly related to the CPU caches.

**Instruction cache (I-cache)**

Used to speed executable instruction fetch; some specialized versions include

micro-operation caches

and

branch target instruction caches

.

**Data cache (D-cache)**

Used to speed data fetch and store.

**Higher-level caches**

caches above the I-cache and D-cache are usually organized as a hierarchy of more cache levels (L2, L3, etc.); see also

multi-level caches

below).


## History

Early examples of CPU caches include the Atlas 2 and the IBM System/360 Model 85 in the 1960s. The first CPUs that used a cache had only one level of cache; unlike later level 1 cache, it was not split into L1d (for data) and L1i (for instructions). Split L1 cache started in 1976 with the IBM 801 CPU, became mainstream in the late 1980s, and in 1997 entered the embedded CPU market with the ARMv5TE. As of 2015, even sub-dollar SoCs split the L1 cache. They also have L2 caches and, for larger processors, L3 caches as well. The L2 cache is usually not split, and acts as a common repository for the already split L1 cache. Every core of a multi-core processor has a dedicated L1 cache and is usually not shared between the cores. The L2 cache, and lower-level caches, may be shared between the cores. L4 cache is currently uncommon, and is generally dynamic random-access memory (DRAM) on a separate die or chip, rather than static random-access memory (SRAM). An exception to this is when eDRAM is used for all levels of cache, down to L1. Historically L1 was also on a separate die, however bigger die sizes have allowed integration of it as well as other cache levels, with the possible exception of the last level. Each extra level of cache tends to be smaller and faster than the lower levels.

Caches (like for RAM historically) have generally been sized in powers of: 2, 4, 8, 16 etc. KiB; when up to MiB sizes (i.e. for larger non-L1), very early on the pattern broke down, to allow for larger caches without being forced into the doubling-in-size paradigm, with e.g. Intel Core 2 Duo with 3 MiB L2 cache in April 2008. This happened much later for L1 caches, as their size is generally still a small number of KiB. The IBM zEC12 from 2012 is an exception however, to gain unusually large 96 KiB L1 data cache for its time, and e.g. the IBM z13 having a 96 KiB L1 instruction cache (and 128 KiB L1 data cache), and Intel Ice Lake-based processors from 2018, having 48 KiB L1 data cache and 48 KiB L1 instruction cache. In 2020, some Intel Atom CPUs (with up to 24 cores) have (multiple of) 4.5 MiB and 15 MiB cache sizes.


## Operation

### Cache entries

Data is transferred between memory and cache in blocks of fixed size, called *cache lines* or *cache blocks*. When a cache line is copied from memory into the cache, a cache entry is created. The cache entry will include the copied data as well as the requested memory location (called a tag).

When the processor needs to read or write a location in memory, it first checks for a corresponding entry in the cache. The cache checks for the contents of the requested memory location in any cache lines that might contain that address. If the processor finds that the memory location is in the cache, a **cache hit** has occurred. However, if the processor does not find the memory location in the cache, a **cache miss** has occurred. In the case of a cache hit, the processor immediately reads or writes the data in the cache line. For a cache miss, the cache allocates a new entry and copies data from main memory, then the request is fulfilled from the contents of the cache.

### Policies

#### Replacement policies

To make room for the new entry on a cache miss, the cache may have to evict one of the existing entries. The heuristic it uses to choose the entry to evict is called the replacement policy. The fundamental problem with any replacement policy is that it must predict which existing cache entry is least likely to be used in the future. Predicting the future is generally difficult, so there is no perfect method to choose among the variety of replacement policies available. One popular replacement policy, least-recently used (LRU), replaces the least recently accessed entry.

Marking some memory ranges as non-cacheable can improve performance, by avoiding caching of memory regions that are rarely re-accessed. This avoids the overhead of loading something into the cache without having any reuse. Cache entries may also be disabled or locked depending on the context.

#### Write policies

If data are written to the cache, at some point they must also be written to main memory; the timing of this write is known as the write policy. In a write-through cache, every write to the cache causes a write to main memory. Alternatively, in a write-back or copy-back cache, writes are not immediately mirrored to the main memory, with locations been written over being marked as dirty, being written back to the main memory only when they are evicted from the cache. For this reason, a read miss in a write-back cache may sometimes require two memory accesses to service: one to first write the dirty location to main memory, and then another to read the new location from memory. Also, a write to a main memory location that is not yet mapped in a write-back cache may evict an already dirty location, thereby freeing that cache space for the new memory location.

There are intermediate policies as well. The cache may be write-through, but the writes may be held in a store data queue temporarily, usually so multiple stores can be processed together (which can reduce bus turnarounds and improve bus utilization).

Cached data from the main memory may be changed by other entities (e.g., peripherals using direct memory access (DMA) or another core in a multi-core processor), in which case the copy in the cache may become out-of-date or stale. Alternatively, when a CPU in a multiprocessor system updates data in the cache, copies of data in caches associated with other CPUs become stale. Communication protocols between the cache managers that keep the data consistent are known as cache coherence protocols.

### Cache performance

Cache performance measurement has become important in recent times where the speed gap between the memory performance and the processor performance is increasing exponentially. The cache was introduced to reduce this speed gap. Thus knowing how well the cache is able to bridge the gap in the speed of processor and memory becomes important, especially in high-performance systems. The cache hit rate and the cache miss rate play an important role in determining this performance. To improve the cache performance, reducing the miss rate becomes one of the necessary steps among other steps. Decreasing the access time to the cache also gives a boost to its performance and helps with optimization.

#### CPU stalls

The time taken to fetch one cache line from memory (read latency due to a cache miss) matters because the CPU will run out of work while waiting for the cache line. When a CPU reaches this state, it is called a stall. As CPUs become faster compared to main memory, stalls due to cache misses displace more potential computation; modern CPUs can execute hundreds of instructions in the time taken to fetch a single cache line from main memory.

Various techniques have been employed to keep the CPU busy during this time, including out-of-order execution in which the CPU attempts to execute independent instructions after the instruction that is waiting for the cache miss data. Another technology, used by many processors, is simultaneous multithreading (SMT), which allows an alternate thread to use the CPU core while the first thread waits for required CPU resources to become available.


## Associativity

The placement policy decides where in the cache a copy of a particular entry of main memory will go. If the placement policy is free to choose any entry in the cache to hold the copy, the cache is called *fully associative*. At the other extreme, if each entry in the main memory can go in just one place in the cache, the cache is *direct-mapped*. Many caches implement a compromise in which each entry in the main memory can go to any one of N places in the cache, and are described as N-way set associative. For example, the level-1 data cache in an AMD Athlon is two-way set associative, which means that any particular location in main memory can be cached in either of two locations in the level-1 data cache.

Choosing the right value of associativity involves a trade-off. If there are ten places to which the placement policy could have mapped a memory location, then to check if that location is in the cache, ten cache entries must be searched. Checking more places takes more power and chip area, and potentially more time. On the other hand, caches with more associativity suffer fewer misses (see conflict misses), so that the CPU wastes less time reading from the slow main memory. The general guideline is that doubling the associativity, from direct mapped to two-way, or from two-way to four-way, has about the same effect on raising the hit rate as doubling the cache size. However, increasing associativity more than four does not improve hit rate as much, and are generally done for other reasons (see virtual aliasing). Some CPUs can dynamically reduce the associativity of their caches in low-power states, which acts as a power-saving measure.

In order of worse but simple to better but complex:

- Direct mapped cache – good best-case time, but unpredictable in the worst case
- Two-way set associative cache
- Two-way skewed associative cache
- Four-way set-associative cache
- Eight-way set-associative cache, a common choice for later implementations
- 12-way set associative cache, similar to eight-way
- Fully associative cache – the best miss rates, but practical only for a small number of entries

### Direct-mapped cache

In this cache organization, each location in the main memory can go in only one entry in the cache. Therefore, a direct-mapped cache can also be called a "one-way set associative" cache. It does not have a placement policy as such, since there is no choice of which cache entry's contents to evict. This means that if two locations map to the same entry, they may continually knock each other out. Although simpler, a direct-mapped cache needs to be much larger than an associative one to give comparable performance, and it is more unpredictable. Let x be block number in cache, y be block number of memory, and n be number of blocks in cache, then mapping is done with the help of the equation *x* = *y* mod *n*.

### Two-way set associative cache

If each location in the main memory can be cached in either of two locations in the cache, one logical question is: *which one of the two?* The simplest and most commonly used scheme, shown in the right-hand diagram above, is to use the least significant bits of the memory location's index as the index for the cache memory, and to have two entries for each index. One benefit of this scheme is that the tags stored in the cache do not have to include that part of the main memory address which is implied by the cache memory's index. Since the cache tags have fewer bits, they require fewer transistors, take less space on the processor circuit board or on the microprocessor chip, and can be read and compared faster. Also LRU algorithm is especially simple since only one bit needs to be stored for each pair.

### Speculative execution

One of the advantages of a direct-mapped cache is that it allows simple and fast speculation. Once the address has been computed, the one cache index which might have a copy of that location in memory is known. That cache entry can be read, and the processor can continue to work with that data before it finishes checking that the tag actually matches the requested address.

The idea of having the processor use the cached data before the tag match completes can be applied to associative caches as well. A subset of the tag, called a *hint*, can be used to pick just one of the possible cache entries mapping to the requested address. The entry selected by the hint can then be used in parallel with checking the full tag. The hint technique works best when used in the context of address translation, as explained below.

### Two-way skewed associative cache

Other schemes have been suggested, such as the *skewed cache*, where the index for way 0 is direct, as above, but the index for way 1 is formed with a hash function. A good hash function has the property that addresses which conflict with the direct mapping tend not to conflict when mapped with the hash function, and so it is less likely that a program will suffer from an unexpectedly large number of conflict misses due to a pathological access pattern. The downside is extra latency from computing the hash function. Additionally, when it comes time to load a new line and evict an old line, it may be difficult to determine which existing line was least recently used, because the new line conflicts with data at different indexes in each way; LRU tracking for non-skewed caches is usually done on a per-set basis. Nevertheless, skewed-associative caches have major advantages over conventional set-associative ones.

### Pseudo-associative cache

A true set-associative cache tests all the possible ways simultaneously, using something like a content-addressable memory. A pseudo-associative cache tests each possible way one at a time. A hash-rehash cache and a column-associative cache are examples of a pseudo-associative cache.

In the common case of finding a hit in the first way tested, a pseudo-associative cache is as fast as a direct-mapped cache, but it has a much lower conflict miss rate than a direct-mapped cache, closer to the miss rate of a fully associative cache.

### Multicolumn cache

Comparing with a direct-mapped cache, a set associative cache has a reduced number of bits for its cache set index that maps to a cache set, where multiple ways or blocks stays, such as 2 blocks for a 2-way set associative cache and 4 blocks for a 4-way set associative cache. Comparing with a direct mapped cache, the unused cache index bits become a part of the tag bits. For example, a 2-way set associative cache contributes 1 bit to the tag and a 4-way set associative cache contributes 2 bits to the tag. The basic idea of the multicolumn cache is to use the set index to map to a cache set as a conventional set associative cache does, and to use the added tag bits to index a way in the set. For example, in a 4-way set associative cache, the two bits are used to index way 00, way 01, way 10, and way 11, respectively. This double cache indexing is called a "major location mapping", and its latency is equivalent to a direct-mapped access. Extensive experiments in multicolumn cache design shows that the hit ratio to major locations is as high as 90%. If cache mapping conflicts with a cache block in the major location, the existing cache block will be moved to another cache way in the same set, which is called "selected location". Because the newly indexed cache block is a most recently used (MRU) block, it is placed in the major location in multicolumn cache with a consideration of temporal locality. Since multicolumn cache is designed for a cache with a high associativity, the number of ways in each set is high; thus, it is easy find a selected location in the set. A selected location index by an additional hardware is maintained for the major location in a cache block.

Multicolumn cache remains a high hit ratio due to its high associativity, and has a comparable low latency to a direct-mapped cache due to its high percentage of hits in major locations. The concepts of major locations and selected locations in multicolumn cache have been used in several cache designs in ARM Cortex R chip, Intel's way-predicting cache memory, IBM's reconfigurable multi-way associative cache memory and Oracle's dynamic cache replacement way selection based on address tab bits.


## Cache entry structure

Cache row entries usually have the following structure:

| tag | data block | flag bits |
|---|---|---|

The *data block* (cache line) contains the actual data fetched from the main memory. The *tag* contains (part of) the address of the actual data fetched from the main memory. The flag bits are discussed below.

The "size" of the cache is the amount of main memory data it can hold. This size can be calculated as the number of bytes stored in each data block times the number of blocks stored in the cache. (The tag, flag and error correction code bits are not included in the size, although they do affect the physical area of a cache.)

An effective memory address which goes along with the cache line (memory block) is split (MSB to LSB) into the tag, the index and the block offset.

| tag | index | block offset |
|---|---|---|

The index describes which cache set that the data has been put in. The index length is $\lceil \log _{2}(s)\rceil$ bits for s cache sets.

The block offset specifies the desired data within the stored data block within the cache row. Typically the effective address is in bytes, so the block offset length is $\lceil \log _{2}(b)\rceil$ bits, where b is the number of bytes per data block. The tag contains the most significant bits of the address, which are checked against all rows in the current set (the set has been retrieved by index) to see if this set contains the requested address. If it does, a cache hit occurs. The tag length in bits is as follows:

tag_length = address_length - index_length - block_offset_length

Some authors refer to the block offset as simply the "offset" or the "displacement".

### Example

The original Pentium 4 processor had a four-way set associative L1 data cache of 8 KiB in size, with 64-byte cache blocks. Hence, there are 8 KiB / 64 = 128 cache blocks. The number of sets is equal to the number of cache blocks divided by the number of ways of associativity, what leads to 128 / 4 = 32 sets, and hence 25 = 32 different indices. There are 26 = 64 possible offsets. Since the CPU address is 32 bits wide, this implies 32 − 5 − 6 = 21 bits for the tag field.

The original Pentium 4 processor also had an eight-way set associative L2 integrated cache 256 KiB in size, with 128-byte cache blocks. This implies 32 − 8 − 7 = 17 bits for the tag field.

### Flag bits

An instruction cache requires only one flag bit per cache row entry: a valid bit. The valid bit indicates whether or not a cache block has been loaded with valid data.

On power-up, the hardware sets all the valid bits in all the caches to "invalid". Some systems also set a valid bit to "invalid" at other times, such as when multi-master bus snooping hardware in the cache of one processor hears an address broadcast from some other processor, and realizes that certain data blocks in the local cache are now stale and should be marked invalid.

A data cache typically requires two flag bits per cache line – a valid bit and a dirty bit. Having a dirty bit set indicates that the associated cache line has been changed since it was read from main memory ("dirty"), meaning that the processor has written data to that line and the new value has not propagated all the way to main memory.


## Cache miss

A cache miss is a failed attempt to read or write a piece of data in the cache, which results in a main memory access with much longer latency. There are three kinds of cache misses: instruction read miss, data read miss, and data write miss.

*Cache read misses* from an *instruction* cache generally cause the largest delay, because the processor, or at least the thread of execution, has to wait (stall) until the instruction is fetched from main memory. *Cache read misses* from a *data* cache usually cause a smaller delay, because instructions not dependent on the cache read can be issued and continue execution until the data are returned from main memory, and the dependent instructions can resume execution. *Cache write misses* to a *data* cache generally cause the shortest delay, because the write can be queued and there are few limitations on the execution of subsequent instructions; the processor can continue until the queue is full. For a detailed introduction to the types of misses, see cache performance measurement and metric.


## Address translation

Most general purpose CPUs implement some form of virtual memory. To summarize, either each program running on the machine sees its own simplified address space, which contains code and data for that program only, or all programs run in a common virtual address space. A program executes by calculating, comparing, reading and writing to addresses of its virtual address space, rather than addresses of physical address space, making programs simpler and thus easier to write.

Virtual memory requires the processor to translate virtual addresses generated by the program into physical addresses in main memory. The portion of the processor that does this translation is known as the memory management unit (MMU). The fast path through the MMU can perform those translations stored in the translation lookaside buffer (TLB), which is a cache of mappings from the operating system's page table, segment table, or both.

For the purposes of the present discussion, there are three important features of address translation:

- *Latency:* The physical address is available from the MMU some time, perhaps a few cycles, after the virtual address is available from the address generator.
- *Aliasing:* Multiple virtual addresses can map to a single physical address. Most processors guarantee that all updates to that single physical address will happen in program order. To deliver on that guarantee, the processor must ensure that only one copy of a physical address resides in the cache at any given time.
- *Granularity:* The virtual address space is broken up into pages. For instance, a 4 GiB virtual address space might be cut up into 1,048,576 pages of 4 KiB size, each of which can be independently mapped. There may be multiple page sizes supported; see virtual memory for elaboration.

One early virtual memory system, the IBM M44/44X, required an access to a mapping table held in core memory before every programmed access to main memory. With no caches, and with the mapping table memory running at the same speed as main memory this effectively cut the speed of memory access in half. Two early machines that used a page table in main memory for mapping, the IBM System/360 Model 67 and the GE 645, both had a small associative memory as a cache for accesses to the in-memory page table. Both machines predated the first machine with a cache for main memory, the IBM System/360 Model 85, so the first hardware cache used in a computer system was not a data or instruction cache, but rather a TLB.

Caches can be divided into four types, based on whether the index or tag correspond to physical or virtual addresses:

- *Physically indexed, physically tagged* (PIPT) caches use the physical address for both the index and the tag. While this is simple and avoids problems with aliasing, it is also slow, as the physical address must be looked up (which could involve a TLB miss and access to main memory) before that address can be looked up in the cache.
- *Virtually indexed, virtually tagged* (VIVT) caches use the virtual address for both the index and the tag. This caching scheme can result in much faster lookups, since the MMU does not need to be consulted first to determine the physical address for a given virtual address. However, VIVT suffers from aliasing problems, where several different virtual addresses may refer to the same physical address. The result is that such addresses would be cached separately despite referring to the same memory, causing coherency problems. Although solutions to this problem exist they do not work for standard coherence protocols. Another problem is homonyms, where the same virtual address maps to several different physical addresses. It is not possible to distinguish these mappings merely by looking at the virtual index itself, though potential solutions include: flushing the cache after a context switch, forcing address spaces to be non-overlapping, tagging the virtual address with an address space ID (ASID). Additionally, there is a problem that virtual-to-physical mappings can change, which would require flushing cache lines, as the VAs would no longer be valid. All these issues are absent if tags use physical addresses (VIPT).
- *Virtually indexed, physically tagged* (VIPT) caches use the virtual address for the index and the physical address in the tag. The advantage over PIPT is lower latency, as the cache set can be looked up in parallel with the TLB translation, however the tag cannot be compared until the physical address is available. The advantage over VIVT is that since the tag has the physical address, the cache can detect homonyms. Theoretically, VIPT requires more tags bits because some of the index bits could differ between the virtual and physical addresses (for example bit 12 and above for 4 KiB pages) and would have to be included both in the virtual index and in the physical tag. In practice this is not an issue because, in order to avoid coherency problems, VIPT caches are designed to have no such index bits (e.g., by limiting the total number of bits for the index and the block offset to 12 for 4 KiB pages); this limits the size of VIPT caches to the page size times the associativity of the cache.
- *Physically indexed, virtually tagged* (PIVT) caches are often claimed in literature to be useless and non-existing. However, the MIPS R6000 uses this cache type as the sole known implementation. The R6000 is implemented in emitter-coupled logic, which is an extremely fast technology not suitable for large memories such as a TLB. The R6000 solves the issue by putting the TLB memory into a reserved part of the second-level cache having a tiny, high-speed TLB "slice" on chip. The cache is indexed by the physical address obtained from the TLB slice. However, since the TLB slice only translates those virtual address bits that are necessary to index the cache and does not use any tags, false cache hits may occur, which is solved by tagging with the virtual address.

The speed of this recurrence (the *load latency*) is crucial to CPU performance, and so most modern level-1 caches are virtually indexed, which at least allows the MMU's TLB lookup to proceed in parallel with fetching the data from the cache RAM.

But virtual indexing is not the best choice for all cache levels. The cost of dealing with virtual aliases grows with cache size, and as a result most level-2 and larger caches are physically indexed.

Caches have historically used both virtual and physical addresses for the cache tags, although virtual tagging is now uncommon. If the TLB lookup can finish before the cache RAM lookup, then the physical address is available in time for tag compare, and there is no need for virtual tagging. Large caches, then, tend to be physically tagged, and only small, very low latency caches are virtually tagged. In recent general-purpose CPUs, virtual tagging has been superseded by virtual hints, as described below.

### Homonym and synonym problems

A cache that relies on virtual indexing and tagging becomes inconsistent after the same virtual address is mapped into different physical addresses (homonym), which can be solved by using physical address for tagging, or by storing the address space identifier in the cache line. However, the latter approach does not help against the synonym problem, in which several cache lines end up storing data for the same physical address. Writing to such locations may update only one location in the cache, leaving the others with inconsistent data. This issue may be solved by using non-overlapping memory layouts for different address spaces, or otherwise the cache (or a part of it) must be flushed when the mapping changes.

### Virtual tags and hints

The great advantage of virtual tags is that, for associative caches, they allow the tag match to proceed before the virtual to physical translation is done. However, coherence probes and evictions present a physical address for action. The hardware must have some means of converting the physical addresses into a cache index, generally by storing physical tags as well as virtual tags. For comparison, a physically tagged cache does not need to keep virtual tags, which is simpler. When a virtual to physical mapping is deleted from the TLB, cache entries with those virtual addresses will have to be flushed somehow. Alternatively, if cache entries are allowed on pages not mapped by the TLB, then those entries will have to be flushed when the access rights on those pages are changed in the page table.

It is also possible for the operating system to ensure that no virtual aliases are simultaneously resident in the cache. The operating system makes this guarantee by enforcing page coloring, which is described below. Some early RISC processors (SPARC, RS/6000) took this approach. It has not been used recently, as the hardware cost of detecting and evicting virtual aliases has fallen and the software complexity and performance penalty of perfect page coloring has risen.

It can be useful to distinguish the two functions of tags in an associative cache: they are used to determine which way of the entry set to select, and they are used to determine if the cache hit or missed. The second function must always be correct, but it is permissible for the first function to guess, and get the wrong answer occasionally.

Some processors (e.g. early SPARCs) have caches with both virtual and physical tags. The virtual tags are used for way selection, and the physical tags are used for determining hit or miss. This kind of cache enjoys the latency advantage of a virtually tagged cache, and the simple software interface of a physically tagged cache. It bears the added cost of duplicated tags, however. Also, during miss processing, the alternate ways of the cache line indexed have to be probed for virtual aliases and any matches evicted.

The extra area (and some latency) can be mitigated by keeping *virtual hints* with each cache entry instead of virtual tags. These hints are a subset or hash of the virtual tag, and are used for selecting the way of the cache from which to get data and a physical tag. Like a virtually tagged cache, there may be a virtual hint match but physical tag mismatch, in which case the cache entry with the matching hint must be evicted so that cache accesses after the cache fill at this address will have just one hint match. Since virtual hints have fewer bits than virtual tags distinguishing them from one another, a virtually hinted cache suffers more conflict misses than a virtually tagged cache.

Perhaps the ultimate reduction of virtual hints can be found in the Pentium 4 (Willamette and Northwood cores). In these processors the virtual hint is effectively two bits, and the cache is four-way set associative. Effectively, the hardware maintains a simple permutation from virtual address to cache index, so that no content-addressable memory (CAM) is necessary to select the right one of the four ways fetched.

### Page coloring

Large physically indexed caches (usually secondary caches) run into a problem: the operating system rather than the application controls which pages collide with one another in the cache. Differences in page allocation from one program run to the next lead to differences in the cache collision patterns, which can lead to very large differences in program performance. These differences can make it very difficult to get a consistent and repeatable timing for a benchmark run.

To understand the problem, consider a CPU with a 1 MiB physically indexed direct-mapped level-2 cache and 4 KiB virtual memory pages. Sequential physical pages map to sequential locations in the cache until after 256 pages the pattern wraps around. We can label each physical page with a color of 0–255 to denote where in the cache it can go. Locations within physical pages with different colors cannot conflict in the cache.

Programmers attempting to make maximum use of the cache may arrange their programs' access patterns so that only 1 MiB of data need be cached at any given time, thus avoiding capacity misses. But they should also ensure that the access patterns do not have conflict misses. One way to think about this problem is to divide up the virtual pages the program uses and assign them virtual colors in the same way as physical colors were assigned to physical pages before. Programmers can then arrange the access patterns of their code so that no two pages with the same virtual color are in use at the same time. There is a wide literature on such optimizations (e.g. loop nest optimization), largely coming from the High Performance Computing (HPC) community.

The snag is that while all the pages in use at any given moment may have different virtual colors, some may have the same physical colors. In fact, if the operating system assigns physical pages to virtual pages randomly and uniformly, it is extremely likely that some pages will have the same physical color, and then locations from those pages will collide in the cache (this is the birthday paradox).

The solution is to have the operating system attempt to assign different physical color pages to different virtual colors, a technique called *page coloring*. Although the actual mapping from virtual to physical color is irrelevant to system performance, odd mappings are difficult to keep track of and have little benefit, so most approaches to page coloring simply try to keep physical and virtual page colors the same.

If the operating system can guarantee that each physical page maps to only one virtual color, then there are no virtual aliases, and the processor can use virtually indexed caches with no need for extra virtual alias probes during miss handling. Alternatively, the OS can flush a page from the cache whenever it changes from one virtual color to another. As mentioned above, this approach was used for some early SPARC and RS/6000 designs.

The software page coloring technique has been used to effectively partition the shared Last level Cache (LLC) in multicore processors. This operating system-based LLC management in multicore processors has been adopted by Intel.
