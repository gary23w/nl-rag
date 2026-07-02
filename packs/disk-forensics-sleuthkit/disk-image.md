---
title: "Disk image"
source: https://en.wikipedia.org/wiki/Disk_image
domain: disk-forensics-sleuthkit
license: CC-BY-SA-4.0
tags: disk forensics sleuth kit, file system forensic analysis, forensic disk imaging, file carving recovery, write blocker acquisition
fetched: 2026-07-02
---

# Disk image

A **disk image** is a snapshot of a storage device's content – typically stored in a file on another storage device.

Traditionally, a disk image was relatively large because it was a bit-by-bit copy of every storage location of a device (i.e. every sector of a hard disk drive), but it is now common to only store allocated data to reduce storage space. Compression and deduplication are commonly used to further reduce the size of image files.

Disk imaging is performed for a variety of purposes including digital forensics, cloud computing, system administration, backup, and emulation for digital preservation strategy. Despite the benefits, storage costs can be high, management can be difficult and imaging can be time consuming.

Disk images can be made in a variety of formats depending on the purpose. Virtual disk images (such as VHD and VMDK) are intended to be used for cloud computing, ISO images are intended to emulate optical media, such as a CD-ROM. Raw disk images are used for forensic purposes. Proprietary formats are typically used by disk imaging software.

## Background

Disk images were originally (in the late 1960s) used for backup and disk cloning of mainframe disk media. Early ones were as small as 5 megabytes and as large as 330 megabytes, and the copy medium was magnetic tape, which ran as large as 200 megabytes per reel. Disk images became much more popular when floppy disk media became popular, where replication or storage of an exact structure was necessary and efficient, especially in the case of copy protected floppy disks.

Disk image creation is called disk imaging and is often time consuming, even with a fast computer, because the entire disk must be copied. Typically, disk imaging requires a third party disk imaging program or backup software. The software required varies according to the type of disk image that needs to be created. For example, RawWrite and WinImage create floppy disk image files for MS-DOS and Microsoft Windows. In Unix or similar systems the dd program can be used to create raw disk images. Apple Disk Copy can be used on Classic Mac OS and macOS systems to create and write disk image files.

Authoring software for CDs/DVDs such as Nero Burning ROM can generate and load disk images for optical media. A *virtual disk writer* or *virtual burner* is a computer program that emulates an actual disc authoring device such as a CD writer or DVD writer. Instead of writing data to an actual disc, it creates a virtual disk image. A virtual burner, by definition, appears as a disc drive in the system with writing capabilities (as opposed to conventional disc authoring programs that can create virtual disk images), thus allowing software that can burn discs to create virtual discs.

## Uses

### Digital forensics

Forensic imaging is the process of creating a bit-by-bit copy of the data on the drive, including files, metadata, volume information, filesystems and their structure. Often, these images are also hashed to verify their integrity and that they have not been altered since being created. Unlike disk imaging for other purposes, digital forensic applications take a bit-by-bit copy to ensure forensic soundness. The purposes of imaging the disk is to not only discover evidence preserved in digital information but also to examine the drive to gather clues of how the crime was committed.

### Virtualization

Creating a virtual disk image of optical media or a hard disk drive is typically done to make the content available to one or more virtual machines. Virtual machines emulate a CD/DVD drive by reading an ISO image. This can also be faster than reading from the physical optical medium. Further, there are less issues with wear and tear. A hard disk drive or solid-state drive in a virtual machine is implemented as a disk image (i.e. either the VHD format used by Microsoft's Hyper-V, the VDI format used by Oracle Corporation's VirtualBox, the VMDK format used for VMware virtual machines, or the QCOW format used by QEMU). Virtual hard disk images tend to be stored as either a collection of files (where each one is typically 2GB in size), or as a single file. Virtual machines treat the image set as a physical drive.

### Rapid deployment of systems

Educational institutions and businesses can often need to buy or replace computer systems in large numbers. Disk imaging is commonly used to rapidly deploy the same configuration across workstations. Disk imaging software is used to create an image of a completely-configured system (such an image is sometimes called a golden image). This image is then written to a computer's hard disk (which is sometimes described as restoring an image).

#### Network-based image deployment

Image restoration can be done using network-based image deployment. This method uses a PXE server to boot an operating system over a computer network that contains the necessary components to image or restore storage media in a computer. This is usually used in conjunction with a DHCP server to automate the configuration of network parameters including IP addresses. Multicasting, broadcasting or unicasting tend to be used to restore an image to many computers simultaneously. These approaches do not work well if one or more computers experience packet loss. As a result, some imaging solutions use the BitTorrent protocol to overcome this problem.

Network-based image deployment reduces the need to maintain and update individual systems manually. Imaging is also easier than automated setup methods because an administrator does not need to have knowledge of the prior configuration to copy it.

### Backup strategy

A disk image contains all files and data (i.e., file attributes and the file fragmentation state). For this reason, it is also used for backing up optical media (CDs and DVDs, etc.), and allows the exact and efficient recovery after experimenting with modifications to a system or virtual machine. Typically, disk imaging can be used to quickly restore an entire system to an operational state after a disaster.

### Digital preservation

Libraries and museums are typically required to archive and digitally preserve information without altering it in any manner. Emulators frequently use disk images to emulate floppy disks that have been preserved. This is usually simpler to program than accessing a real floppy drive (particularly if the disks are in a format not supported by the host operating system), and allows a large library of software to be managed. Emulation also allows existing disk images to be put into a usable form even though the data contained in the image is no longer readable without emulation.

## Limitations

Disk imaging is time consuming, the space requirements are high and reading from them can be slower than reading from the disk directly because of a performance overhead.

Other limitations can be the lack of access to software required to read the contents of the image. For example, prior to Windows 8, third party software was required to mount disk images. When imaging multiple computers with only minor differences, much data is duplicated unnecessarily, wasting space.

### Speed and failure

Disk imaging can be slow, especially for older storage devices. A typical 4.7 GB DVD can take an average of 18 minutes to duplicate. Floppy disks read and write much slower than hard disks. Therefore, despite their small size, it can take several minutes to copy a single disk. In some cases, disk imaging can fail due to bad sectors or physical wear and tear on the source device. Unix utilities (such as dd) are not designed to cope with failures, causing the disk image creation process to fail. When data recovery is the end goal, it is instead recommended to use more specialised tools (such as ddrescue).
