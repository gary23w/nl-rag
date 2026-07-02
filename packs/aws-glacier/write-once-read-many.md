---
title: "Write once read many"
source: https://en.wikipedia.org/wiki/Write_once_read_many
domain: aws-glacier
license: CC-BY-SA-4.0
tags: aws glacier, amazon s3 glacier, cold archive storage, long-term data archive
fetched: 2026-07-02
---

# Write once read many

**Write once read many** (**WORM**) describes a data storage device in which information, once written, cannot be modified. This write protection affords the assurance that the data cannot be tampered with once it is written to the device, excluding the possibility of data loss from human error, computer bugs, or malware.

On ordinary (non-WORM) data storage devices, the number of times data can be modified is limited only by the lifespan of the device, as modification involves physical changes that may cause wear to the device. The "read many" aspect is unremarkable, as modern storage devices permit unlimited reading of data once written. Historical exceptions include time-limited discs such as Flexplay, designed for short-term rental of movies; and early non-volatile memory technologies such as magnetic-core memory and bubble memory, from which reading data also erased it.

WORM prevents important data being deleted or modified, helping to preserve its authenticity.

## History

WORM drives preceded the invention of the CD-R, DVD-R and BD-R. An example was the IBM 3363. These drives typically used either a 5.1 in (13 cm) or a 12 in (30 cm) disc in a cartridge, with an ablative optical layer that could be written to only once, and were often used in places like libraries that needed to store large amounts of data. Interfaces to connect these to PCs also existed.

Punched cards and paper tape are obsolete WORM media. Although any unpunched area of the medium could be punched after the first write of the medium, doing so was virtually never useful. Read-only memory (ROM) is also a WORM medium. Such memory may contain the instructions to a computer to read the operating system from another storage device such as a hard disk. The non-technical end-user, however, cannot write the ROM even once but considers it part of the unchangeable computing platform.

WORM was utilized for broker-dealer records within the Financial Industry Regulatory Authority and the U.S. Securities and Exchange Commission.

## Current WORM drives

The CD-R, DVD-R and BD-R optical discs for computers are common WORM devices. On these discs, no region of the disc can be recorded a second time. Through packet writing, which uses the Universal Disk Format (UDF) file system, these discs often use a file system that permits additional files, and even revised versions of a file by the same name, to be recorded in a different region of the disc. To the user, the disc appears to allow additions and revisions until all the disk space is used.

The SD card and microSD card spec allows for multiple forms of write-protection. The most common form, only available when using a full-size SD card, provides a physical write protection switch which allows the user to advise the host card reader to disallow write access. This does not protect the data on the card if the card reader hardware is not built to respect the write protection switch.

Multiple vendors beginning in the early 2000s developed magnetic WORM devices. These archival grade storage devices utilize a variation of RAID and magnetic storage technologies to secure data from unauthorized alteration or modification at both the hardware and software levels. As the cost of magnetic (and solid-state) storage has decreased, so has the cost for these archival storage technologies. These technologies are almost always integrated directly into a content/document management system that manages retention schedules and access controls, along with document level history.

There are multiple vendors providing magnetic storage technologies including NetApp, EMC Centera, KOM Networks, and others. In 2013, GreenTec-USA, Inc. developed WORM hard disk drives in capacities of 3 TB and greater. Prevention of rewrite is done at the physical disk level and cannot be modified or overridden by the attached computer.

## Research

In the first decade of the 21st century, there had been a renewed interest in WORM based on organic components, such as PEDOT:PSS or other polymers such as PVK or PCz. Organic WORM devices, considered organic memory, can be used as memory elements for low-power RFID tags.
