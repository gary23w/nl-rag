---
title: "Block-level storage"
source: https://en.wikipedia.org/wiki/Block-level_storage
domain: scaleway
license: CC-BY-SA-4.0
tags: scaleway cloud, scaleway elements, scaleway bare metal, european cloud scaleway
fetched: 2026-07-02
---

# Block-level storage

**Block-level storage** is a concept in cloud-hosted data persistence where cloud services emulate the behaviour of a traditional block device, such as a physical hard drive.

Storage in such services is organised as blocks. This emulates the type of behaviour seen in traditional disks or tape storage through storage virtualization. Blocks are identified by an arbitrary and assigned identifier by which they may be stored and retrieved, but this has no obvious meaning in terms of files or documents. A file system must be applied on top of the block-level storage to map 'files' onto a sequence of blocks.

Amazon EBS (elastic block store) is an example of a cloud block store. Cloud block-level storage will usually offer facilities such as replication for reliability, or backup services.

Block-level storage is in contrast to an object store or 'bucket store', such as Amazon S3 (simple storage service), or to a database. These operate at a higher level of abstraction and are able to work with entities such as files, documents, images, videos or database records.

Instance stores are another form of cloud-hosted block-level storage. These are provided as *part of* an 'instance', such as an Amazon EC2 (elastic compute cloud) service. As EC2 instances are primarily provided as compute resources, rather than storage resources, their storage is less robust. Their contents will be lost if the cloud instance is stopped. As these stores are part of the instance's virtual server they offer higher performance and bandwidth to the instance. They are best used for temporary storage such as caching or temporary files, with persistent storage held on a different type of server.

At one time, block-level storage was provided by storage area networks (SAN), and network-attached storage (NAS) provided file-level storage. With the shift from on-premises hosting to cloud services, this distinction has shifted. Even block-storage is now seen as distinct servers (thus NAS), rather than the previous array of bare disks.
