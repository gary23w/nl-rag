---
title: "Operating System Design/Memory Management"
source: https://en.wikibooks.org/wiki/Operating_System_Design/Memory_Management
domain: os-book
license: CC-BY-SA-4.0 (Wikibooks OS Design)
tags: operating system design, kernel design, process management
fetched: 2026-07-02
---

# Operating System Design/Memory Management

<

Operating System Design

Memory Management is a term used to describe how the operating system handles the available RAM. It is managed at multiple levels.

## Physical memory

At the most basic level, there is the physical memory. The physical memory's size is the sum of the capacities of all RAM-modules (such as DDR SDRAM) installed in the system. For example, when you have two 512 MiB DDR SDRAM modules installed in your system, the OS will have 1 GiB of physical memory at its disposal.

## Segmented memory

On top of the physical memory is the segmented memory. It uses the Memory Management Unit (MMU) to translate a logical address (specifying a segment and an offset) into a physical address (or linear address). This allowed early computers to address more than 64 KiB of memory. Most operating systems today don't use a segmented memory model, preferring to use paging.

## Paged memory

A paged memory model uses the MMU to translate virtual addresses to physical addresses. With paging, one can map multiple 4 KiB-sized chunks (called pages) to any virtual address. For example, data at offset 0x1000 in physical memory might be mapped to address 0xC0000000 (at offset 3 GiB) in virtual memory, even though the system may have only 32 MiB of physical RAM available. Accessing the data at address 0xC0000000 internally accesses the data at physical address 0x1000. This provides processes with their own virtual address space which contains only the code and data required by that single process, and everything else is hidden. This way, a process can't corrupt another process' code or data, improving security and reliability.

## Allocated memory

With paging, memory is managed in 4 KiB-sized chunks. Most applications require the ability to be able to get only a fraction of that size, to store data. The memory allocator gets a big chunk of memory (say, 4 pages, or 4 * 4 KiB) and divides this into much smaller chunks (e.g. a chunk of 16 bytes and another chunk of 6 bytes.) which it gives to the applications when requested.

## The Heap

Many Languages and some operating systems use a form of allocated memory called a HEAP, essentially one large space where memory can be used and re-used. Associated with the heap, is the need to do a process called garbage collection, where now allocated space is consolidated to form larger spaces, and the heap recovers from the eventual fragmentation that happens when the sizes of records using the same space at different times are not congruent and are guarded by other allocated spaces that remain active. The fragmentation effect results in lots of small unusable spaces spread throughout the heap. Garbage collection may for instance involve the movement of an allocated memory from one location to another in order to free up more space. To achieve this transparently to the memory, the allocation unit address must not be the same as the public address, but the public address must be a reference to a look-up table that contains the allocation unit address. The garbage collector can then write a copy of the data to a new address, and then change the look-up table address before removing the original data and allowing the consolidation process to recover the space. Another technique is to reference the start and end point of each allocated memory unit, and when a memory unit is released, test to see if the unit before and after it are either free, and if so reallocate a larger block that contains all the free sections that are contiguous. During allocation the allocation utility will start at the top of the list of free sections and look to see if any are exactly the size requested, if so, the first that fits will be selected, then the next largest one if none are found the exact size. Garbage collection can be done continuously or at low use times, with the eventual caveat that if no low use times are found, the garbage collection will cause the whole computer to slow down temporarily when fragmentation becomes unwieldy.

Retrieved from "

https://en.wikibooks.org/w/index.php?title=Operating_System_Design/Memory_Management&oldid=3440038

"
