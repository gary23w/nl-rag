---
title: "Forensic disk controller"
source: https://en.wikipedia.org/wiki/Write_blocker
domain: disk-forensics-sleuthkit
license: CC-BY-SA-4.0
tags: disk forensics sleuth kit, file system forensic analysis, forensic disk imaging, file carving recovery, write blocker acquisition
fetched: 2026-07-02
---

# Forensic disk controller

(Redirected from

Write blocker

)

A **forensic disk controller** or **hardware write-block device** is a specialized type of computer hard disk controller made for the purpose of gaining read-only access to computer hard drives without the risk of damaging the drive's contents. The device is named forensic because its most common application is for use in investigations where a computer hard drive may contain evidence. Such a controller historically has been made in the form of a dongle that fits between a computer and an IDE or SCSI hard drive, but with the advent of USB and SATA, forensic disk controllers supporting these newer technologies have become widespread. Steve Bress and Mark Menz invented hard drive write blocking (US Patent 6,813,682).

A device which is installed between a storage media under investigation and an investigator's computer is called a "**bridge kit**". The bridge kit has one connector for the storage media and another connector the investigator's computer. It allows the investigator to read, but not alter the device under investigation.

The United States National Institute of Justice operates a Computer Forensics Tool Testing (CFTT) program which formally identifies the following top-level tool requirements:

> A hardware write block (HWB) device shall not transmit a command to a protected storage device that modifies the data on the storage device.
> 
> An HWB device shall return the data requested by a read operation.
> 
> An HWB device shall return without modification any access-significant information requested from the drive.
> 
> Any error condition reported by the storage device to the HWB device shall be reported to the host.

## Description

Forensic disk controllers intercept write commands from the host operating system, preventing them from reaching the drive. Whenever the host bus architecture supports it the controller reports that the drive is read-only. The disk controller can either deny all writes to the disk and report them as failures, or use on-board memory to cache the writes for the duration of the session.

A disk controller that caches writes in memory presents the appearance to the operating system that the drive is writable, and uses the memory to ensure that the operating system sees changes to the individual disk sectors it attempted to overwrite. It does this by retrieving sectors from the disk if the operating system hasn't attempted to change them, and retrieving the changed version from memory for sectors that have been changed.

## Uses

Forensic disk controllers are most commonly associated with the process of creating a disk image, or acquisition, during forensic analysis. Their use is to prevent inadvertent modification of evidence.

Using hardware to protect the hard drive from writes is very important for several reasons. First, many operating systems, including Windows, may write to any hard disk that is connected to the system. At the very least, Windows will update the access time for any file accessed, and may write things to the disk unexpectedly - such as creating hidden folders for the recycle bin or saved hardware configuration. Virus infections or malware on the system used for analysis may attempt to infect the disk being inspected. Additionally, the NTFS file system may attempt to commit or rollback unfinished transactions, and/or change flags on the volume to mark it as "in use". At the worst, undesired files may allocate and overwrite deleted space on the hard disk which may potentially destroy evidence in the form of previously deleted files.

Protecting an evidence drive from writes during investigation is also important to counter potential allegations that the contents of the drive were altered during the investigation. Of course, this can be alleged anyway, but in the absence of technology to protect a drive from writes, there is no way for such an allegation to be refuted.
