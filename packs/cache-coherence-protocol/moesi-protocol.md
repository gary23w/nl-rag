---
title: "MOESI protocol"
source: https://en.wikipedia.org/wiki/MOESI_protocol
domain: cache-coherence-protocol
license: CC-BY-SA-4.0
tags: cache coherence protocol, mesi protocol, directory-based coherence, bus snooping
fetched: 2026-07-02
---

# MOESI protocol

**Modified Owned Exclusive Shared Invalid** (**MOESI**) is a full cache coherency protocol that encompasses all of the possible states commonly used in other protocols. In addition to the four common MESI protocol states, there is a fifth "Owned" state representing data that is both modified and shared. This avoids the need to write modified data back to main memory before sharing it. While the data must still be written back eventually, the write-back may be deferred.

In order for this to be possible, direct cache-to-cache transfers of data must be possible, so a cache with the data in the modified state can supply that data to another reader without transferring it to memory.

As discussed in AMD64 Architecture Programmer's Manual Vol. 2 '*System Programming*', each cache line is in one of five states:

**Modified**

This cache has the only valid copy of the cache line, and has made changes to that copy. The cached copy may be further modified freely.

**Owned**

This line is one of several copies in the system. This cache does not have permission to modify the copy

but

the line is modified (dirty) relative to main memory, and this cache has the exclusive responsibility for ensuring main memory is eventually updated. The cache line may be changed to the Modified state after invalidating all shared copies, or changed to the Shared state by

writing the modifications back

to main memory. Owned cache lines

must

respond to a

snoop

request with data, to ensure the stale copy in main memory is not used.

**Exclusive**

This cache has the only copy of the line, but the line is clean (unmodified). It may be written to, changing to the Modified state.

**Shared**

This line is one of several copies in the system. This cache does not have permission to modify the copy. Unlike the MESI protocol, a shared cache line

may

be dirty with respect to memory; if it is, one cache has a copy in the Owned state, and that cache is responsible for eventually updating main memory. If no cache holds the line in the Owned state, the memory copy is up to date. The cache line may not be written, but must be changed to the Exclusive or Modified state first, by invalidating all other cached copies. (If the cache line was Owned before, the invalidate response will indicate this, and the state will become Modified, so the obligation to eventually write the data back to memory is not forgotten.) It may also be discarded (changed to the Invalid state) at any time.

**Invalid**

This block is not valid; it must be fetched to satisfy any attempted access.

For any given pair of caches, the permitted states of a given cache line are as follows:

|   | M | O | E | S | I |
|---|---|---|---|---|---|
| M | (Red X)N | (Red X)N | (Red X)N | (Red X)N | (Green tick)Y |
| O | (Red X)N | (Red X)N | (Red X)N | (Green tick)Y | (Green tick)Y |
| E | (Red X)N | (Red X)N | (Red X)N | (Red X)N | (Green tick)Y |
| S | (Red X)N | (Green tick)Y | (Red X)N | (Green tick)Y | (Green tick)Y |
| I | (Green tick)Y | (Green tick)Y | (Green tick)Y | (Green tick)Y | (Green tick)Y |

(The order in which the states are normally listed serves only to make the acronym "MOESI" pronounceable.)

This protocol, a more elaborate version of the simpler MESI protocol, avoids the need to write a dirty cache line back to main memory when another processor tries to read it. Instead, the Owned state allows a processor to supply the modified data directly to the other processor. This is beneficial when the communication between two CPUs is significantly better than to main memory. An example would be multi-core CPUs with per-core L2 caches.

While MOESI can quickly share dirty cache lines from cache, it may struggle to quickly share clean lines from cache. If a cache line is clean with respect to memory and in the shared state, then there is no obvious single candidate cache to respond to a read request, so it is normal to let the read request be filled from memory. (This is solved by the MESIF protocol, which may be combined with MOESI to make MOESIF.)

If a processor wishes to write to an Owned cache line, it must notify the other processors which are sharing that cache line. The standard implementation simply tells them to invalidate their copies, moving its own copy to the Modified state when this is complete, but alternatively it may use a write-through policy, telling them to update their copies with the new contents. This is a partial write-through which does not go as far as main memory; the processor's own copy remains in the Owned state.

The latter reduces cache traffic *if* there are multiple active readers of e.g. a heavily contended lock; one broadcast write is less communication than separate replies to a thundering herd of read requests. Because these two variants are fully compatible, they may both be used in the same system based on heuristics like the cache's estimate of the number of active readers of this cache line.
