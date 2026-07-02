---
title: "Multi-booting"
source: https://en.wikipedia.org/wiki/Multi-booting
domain: grub-bootloader
license: CC-BY-SA-4.0
tags: grub bootloader, boot loader, master boot record, multi-boot menu
fetched: 2026-07-02
---

# Multi-booting

**Multi-booting** is the act of installing multiple operating systems on a single computer, and being able to choose which one to boot. The term **dual-booting** refers to the common configuration of specifically two operating systems. Multi-booting may require a custom boot loader.

## Usage

Multi-booting allows more than one operating system to reside on one computer; for example, if a user has a primary operating system that they use most frequently and an alternate operating system that they use less frequently. Multi-booting allows a new operating system to configure all applications needed and migrate data before removing the old operating system, if desired. Another reason for multi-booting can be to investigate or test a new operating system without switching completely.

Multi-booting is also useful in situations where different software requires different operating systems. A multi-boot configuration allows a user to use all of their software on one computer. This is often accomplished by using a boot loader such as NTLDR, Windows Boot Manager, LILO, or GRUB which can boot more than one operating system.

Multi-booting is also used by software developers when multiple operating systems are required for development or testing purposes. Having these systems on one machine is a way to reduce hardware costs.

Multi-booting also allows a user to switch between private and work dedicated systems to maintain access integrity and separation between the two user environments, even if the same operating system is used for each of them.

The following is an example of GUID Partition Table (GPT) for a 512 GB NVM Express solid state drive as used with multi-booting configuration, containing an EFI system partition, a Microsoft Reserved Partition, three Microsoft basic data partitions (one is Windows standard partition and two are hidden Windows Recovery Environment partitions), and three Linux partitions (including a swap partition):

```mw
label: gpt
label-id: 96BB56B7-AE3C-4E94-986E-10E7F3CCA80B
device: /dev/nvme0n1
unit: sectors
first-lba: 34
last-lba: 1000215182
sector-size: 512

/dev/nvme0n1p1 : start=        2048, size=      532480, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, uuid=7885D52E-0F50-4E28-B058-8DCE7B7FF921, name="EFI system partition"
/dev/nvme0n1p2 : start=      534528, size=       32768, type=E3C9E316-0B5C-4DB8-817D-F92DF00215AE, uuid=5C34D099-E77A-4B46-9662-430D33E55AFF, name="Microsoft reserved partition"
/dev/nvme0n1p3 : start=      567296, size=   419196928, type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, uuid=109218B1-3097-4635-BE5F-044E28C2BCB0, name="Basic data partition"
/dev/nvme0n1p4 : start=   419764224, size=     1669120, type=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC, uuid=527B26E5-2768-444E-AB1F-ECB28201F3C8, attrs="RequiredPartition GUID:63"
/dev/nvme0n1p5 : start=   421435392, size=   329410560, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, uuid=5C52E480-AEE7-437B-A136-53F8C946D5ED, name="Linux Stuff"
/dev/nvme0n1p6 : start=   750845952, size=   243933184, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, uuid=023F3B88-D3D9-4E39-9F50-77F242410789, name="Linux Root"
/dev/nvme0n1p7 : start=   994779136, size=     4194304, type=0657FD6D-A4AB-43C4-84E5-0933C84B4F4F, uuid=18F44D65-B28D-4871-AF02-DDBD96771460, name="Swap"
/dev/nvme0n1p8 : start=   998973440, size=     1228800, type=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC, uuid=D4A41B1A-2F28-4AE5-AC67-A2D98FB91E22, name="Basic data partition", attrs="RequiredPartition GUID:63"
```

A possible alternative to multi-booting is virtualization, where a hypervisor is used to host one or more virtual machines running guest operating systems.

## Technical issues

### Number of operating systems per volume (logical drive)

In an OS/2 dual-boot configuration, the C drive can contain both DOS and OS/2. The user issues the BOOT command from the DOS or OS/2 command line to do the necessary copy, move and rename operations and then reboot to the specified system on C:. Other systems provide similar mechanisms for alternate systems on the same logical drive.

### Number of operating systems per storage device

In a multi-boot computer, each of the multiple operating systems can reside on its own storage device, or some storage devices might contain more than one operating system in different partitions. The bootloader loaded by the PC displays a menu of choices and loads the selected OS from the PBR of that drive.

An example of a computer with **one operating system per storage device** is a dual-booting computer that stores Windows on one disk drive and Linux on another disk drive. In this case a multi-booting bootloader is not strictly necessary because the user can choose to enter a one-time boot menu (quite often F-12) immediately after power-up and pick the desired OS from the list.

A dual-booting PC that has both Windows and Linux on the same physical disk, but where the PC does not allow selective booting. In this case, a bootloader *is* necessary. The disk should be partitioned to give each OS its own partitions on the drive, as each OS *may* need a different format. For example, if a user intends to install both Windows and Linux, with the Windows partition formatted NTFS format and the Linux partition formatted ext4 format.

### Partitioning

The basic concept involves partitioning a disk to accommodate each planned installation, usually including separate partitions for boot, root, data storage and backups.

### MBR loader

An MBR loader, such as Air-Boot, replaces the standard boot code in track 0 with code that displays a selection menu and loads the selected system. Some, e.g., Air-Boot, can be configured either automatically or by the user at boot time, rather than requiring an external configuration menu.

### Linux boot loaders

Linux loaders, such as GNU GRUB and LILO, can reside in the MBR or in a PBR. They use configuration files in /boot to control their selection menus.

### OS/2 Boot Manager

The OS/2 Boot Manager must be installed in a primary partition. The OS/2 partitioning utilities can configure up to four systems in the menu, each of which can be either in a primary partition or in a logical volume within the extended logical partition. It is possible to include a boot loader such as GRUB in the OS/2 Boot Manager menu, and it is possible to include the OS/2 Boot Manager in the menu for another boot loader. Newer loaders such as Air-Boot, GRUB and LILO offer more flexibility.

### UEFI loading

Modern computer systems (Intel Macs and newer PCs) use Unified Extensible Firmware Interface aka UEFI. Unlike BIOS aka Legacy, UEFI does not rely on a partition's boot sector, the PC's UEFI firmware loads a small boot loader, a .efi file in the EFI System Partition aka ESP directly, and the OS kernel is then loaded by this boot loader.

### Microsoft Windows and Linux

One popular multi-boot configuration is to dual-boot Linux and Windows operating systems, each contained within its own partition. Windows does not facilitate or support multi-boot systems, other than allowing for partition-specific installations, and no choice of boot loader is offered. However, most current Linux installers accommodate multi-booting (although some knowledge of partitions is desirable). Commonly installations proceed without incident but upon restart, the boot loader will recognize only one of the two operating systems.

There are some advantages to installing a Linux boot manager/loader (usually GRUB) as the primary bootloader pointed to by the master boot record. Windows operating systems will be found by properly installed Linux bootloaders, but Windows boot managers do not recognize Linux installations (nor does Windows deal natively with Linux file systems). The MBR boot code can be backed up and restored with dd, available on System Rescue CD.

It is often recommended that Windows be installed to the first primary partition. The boot loaders of both Windows and Linux identify partitions with a number derived by counting the partitions. (Note, both Windows and Linux count the partitions according to the ordering of the partitions *in the partition table*, which may be different from the order of the partitions on the disk.) Adding or deleting a partition at the end of a hard drive will have no effect on any partitions prior to it. However, if a partition is added or deleted at the beginning or middle of a hard drive, the numbering of subsequent partitions may change. If the number of the system partition changes, it requires boot loader reconfiguration in order for an operating system to boot and function properly.

Windows must be installed into a primary partition (and in older systems this must be the first partition). Linux can be installed into a partition in any position on the hard drive and can also be installed into logical partitions (within the extended partition). If Linux is installed into a logical partition within the extended partition, it is unaffected by changes in the primary partitions.

### Neutral MBR

An alternative to storing GRUB in the MBR is keeping Windows' or other generic PC boot code in the MBR, and installing GRUB or another bootloader into a primary partition other than that of Windows, thus keeping the MBR neutral. Operating system selection at boot time consequently depends on the bootloader configured within the primary partition that has the boot or "active" flag set on its partition table entry, which could be a bootloader of DOS, OS/2, eComStation, ArcaOS or BSD, in addition to Linux or Windows.

With the boot flag set on the Windows primary, the Windows Boot Manager can be used to chainload another installed bootloader through use of a program like EasyBCD. This means the active partition's boot manager will first prompt the user for selection what OS to boot, then load another if necessary, such as GRUB, even a bootloader installed to a logical partition, and then GRUB will load the Linux kernel as it normally would were GRUB installed to the MBR.

The active partition could also be one that exists for no purpose other than choosing an operating system to boot, such as the boot manager that shipped with IBM's OS/2 Warp and its derivatives.

### Apple's Boot Camp

Boot Camp allows owners of Intel-based Apple Macintosh computers to install Windows XP, Vista, 7, 8, and 10 on their Macs. The software was initially available in beta version as a download from Apple's website (which was compatible with Mac OS X version 10.4 (Tiger)), and later came bundled with Mac OS X since version 10.5 (Leopard).

Boot Camp allows non-destructive disk partitioning and resizing of HFS+ filesystems, boot menu options, and an option to burn a CD with necessary device drivers. Since Windows XP is incompatible with Extensible Firmware Interface (the successor to legacy BIOS), the firmware on early Intel Macs needs to be updated to support BIOS emulation first. BIOS emulation is achieved with a compatibility support module (CSM). Apple does not support non-Windows partition formats or drivers so therefore configuring other operating systems is not directly possible through Boot Camp itself. However, any operating system which can utilize the BIOS emulation of Intel Macintosh can be made to work, including non-XP versions of Windows. The Ubuntu Linux distribution is particularly popular for this purpose because they provide an option to use proprietary device drivers along with open source drivers.
