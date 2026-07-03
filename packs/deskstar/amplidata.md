---
title: "Amplidata"
source: https://en.wikipedia.org/wiki/Amplidata
domain: deskstar
license: CC-BY-SA-4.0
tags: deskstar
fetched: 2026-07-03
---

# Amplidata

**Amplidata** is a privately held cloud storage technology provider based in Lochristi, Belgium. In November 2010, Amplidata opened its U.S. headquarters in Redwood City, California. The research and development department has locations in Belgium and Egypt, while the sales and support departments are represented in a number of countries in Europe and North America.

Amplidata has developed a Distributed Storage System (DSS) technology designed to solve the scalability and reliability problems traditional storage systems face, by taking advantage of the introduction of large capacity SATA drives and solid state disk. By storing data across a selection of disks that are widely distributed across storage nodes, racks and sites, the DSS architecture spreads the risk of hardware failure to ensure that a failure of a component such as a disk, storage node or even a full rack has no impact on data availability and a minimal impact on data redundancy. The entire system is permanently monitored and data integrity is constantly checked. As a result, bit errors on disks are proactively healed before they become an issue to the user.

Amplidata's AmpliStor distributes and stores data redundantly across a large number of disks. The algorithm that AmpliStor uses first puts the data into an object and then stores the data across multiple disks in the AmpliStor system. By storing the data as an object, Amplidata can reconstruct the original data from any of the disks on which the data within the object resides.

Amplidata was acquired in March 2015 by HGST, a Western Digital subsidiary.

## History

Amplidata was founded in 2008 by Wim De Wispelaere (CEO) and Wouter Van Eetvelde (COO). The company was initially funded by Kristof De Spiegeleer. The two founders started the company to address some of the inherent weaknesses of high capacity disk systems, such as performance, bit error rates, mean time between failures and RAID rebuild times which have not improved sufficiently to keep up with the explosion of digital storage needs. The company's headquarters are in Lochristi, near Gent in Belgium.

De Spiegeleer founded Racktivity, Datacenter Technologies, Hostbasket and Dedigate and has been quoted as a proponent for European adoption of cloud computing. De Spiegeleer is also the CEO of Incubaid, which focuses on developing technology ventures via cloud computing and green data centers. Active member companies of Incubaid include: Amplidata, Ractivity, A-Server, Dacentec. Incubaid owns the automation framework used as the foundation for all the technologies that member companies create.

Amplidata employs about 50 data storage experts. Some employees of Amplidata were employed by DataCenter Technologies, which was acquired by Symantec in 2005 and Q-layer, which became part of Sun Microsystems in 2009.

In May 2010, Amplidata finalized the first round of venture capital funding worth 2.5 million euros, secured by Big Bang Ventures. Big Bang Ventures is known for specializing in funding for start-ups and strives to provide expertise and connections to entrepreneurs in the technology sector. According to CEO and Founder De Wispelaere, Amplidata needed the funding to boost sales and marketing activities in Europe.

In September 2010, Amplidata closed a US$6 million funding round with investors Big Bang Ventures, Endeavour Vision and Swisscom Ventures. Following the funding, Amplidata announced the opening of a U.S. headquarters in Redwood City. However, the company does not plan to relocate its R&D departments, which are located in Belgium and Egypt.

On March 3, 2015, it was announced that Amplidata was to be acquired by HGST, a Western Digital subsidiary. The financial terms of the acquisition were not disclosed.

## Technology

The company has become known for developing unbreakable storage systems. Amplidata's Optimized Object Storage system enables customers to build large-scale online storage systems that aim to meet the highest reliability and availability requirements at the lowest cost.

Amplidata was designed to change the way data is stored. The company's patent-pending BitSpread encoding technology was created to offer the scalability and ease of use of a next-generation RAIN grid, while striving to create a 10,000 times more reliable alternative to RAID. Through more efficient usage of power and raw storage capacity, Amplidata works to drastically decrease the storage cost. Amplidata is known for easily scaling up to tens of Petabytes.

Amplidata technology aims to overcome the limitations of RAID by the increasing length of time required to rebuild larger capacity drives. Rebuild times for 2TB drives are already known to take four hours or longer to complete, and in some cases—depending on how busy the storage system is—it can take days for a rebuild. There is also the need to keep all disks in a RAID group spinning so no power savings can be realized. Spin down is likely to become more important in the years to come as more data is archived to disk, with it likely becoming a function of the storage array to intelligently manage and place the archived data on these drives—as opposed to the software—to facilitate the spin-down of drives.

Amplidata works to reduce the risk for data loss from one event in years—as measured on current storage systems—to one in thousands of years. Its DSS architecture was developed to ensure that a failure of a component such as a disk, storage node or even a full rack has no impact on data availability and a minimal impact on data redundancy. The technology enables data availability and reliability through an ability to reconstruct data from a subset of the originally stored disks. The entire system is permanently monitored and data integrity is constantly checked. As a result, bit errors on disks are proactively healed before they become an issue to the user.

## Products and Technologies

Amplidata technologies that target cloud providers include BitSpread, BitDynamics and BitLog.

Amplidata's technology addressing the end of RAID is BitSpread. It is a RAID replacement technology based on erasure coding that spreads data and parity out across multiple nodes in the storage grid. It aims to greatly minimize the impact of a node or disk failure. Customers can configure availability based on their needs and can have multiple availability policies within a single storage system. Recovery of a drive or node is comparatively very fast, unlike RAID.

BitDynamics provides the storage cluster with scalability and self-healing. It performs proactive self-verification of disk bit errors and then automatically heals that disk block or entire disk as needed. This aims to reduce the amount of work that BitSpread needs to do on a component failure and is expected to improve overall system reliability.

BitLog leverages idle power on the connecting host by using local SSD and HDD cache to provide continuous logged sequential writes from the host to the storage. Then, in turn, it will give high random read performance with the SSD cache, local in the application server for the most frequently accessed data. Meaning that a hot file does not even need to go across the storage network, it can be delivered directly from the application server. In addition, BitLog includes thin provisioning, unlimited snapshots, writeable clones and out-of-band optimization.

AmpliStor product provides object storage for petabyte-scale, unstructured data applications.
