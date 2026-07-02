---
title: "Bootloader"
source: https://en.wikipedia.org/wiki/Bootloader
domain: grub-bootloader
license: CC-BY-SA-4.0
tags: grub bootloader, boot loader, master boot record, multi-boot menu
fetched: 2026-07-02
---

# Bootloader

A **bootloader**, also spelled as **boot loader** or called **bootstrap loader**, is a computer program that is responsible for booting a computer and booting an operating system. If it also provides an interactive menu with multiple boot choices then it is often called a **boot manager**.

When a computer is turned off, its software‍—‌including operating systems, application code, and data‍—‌remains stored on non-volatile memory. When the computer is powered on, it typically does not have an operating system or its loader in random-access memory (RAM). The computer first executes a relatively small program stored in the boot ROM, which is read-only memory (ROM, and later EEPROM, NOR flash) along with some needed data, to initialize hardware devices such as CPU, motherboard, memory, storage and other I/O devices, to access the nonvolatile device (usually a block device, e.g., NAND flash) or devices from which the operating system programs and data can be loaded into RAM.

Some earlier computer systems, upon receiving a boot signal from a human operator or a peripheral device, may load a very small number of fixed instructions into memory at a specific location, initialize at least one CPU, and then point the CPU to the instructions and start their execution. These instructions typically start an input operation from some peripheral device (which may be switch-selectable by the operator). Other systems may send hardware commands directly to peripheral devices or I/O controllers that cause an extremely simple input operation (such as "read sector zero of the system device into memory starting at location 1000") to be carried out, effectively loading a small number of boot loader instructions into memory; a completion signal from the I/O device may then be used to start execution of the instructions by the CPU.

Smaller computers often use less flexible but more automatic boot loader mechanisms to ensure that the computer starts quickly and with a predetermined software configuration. In many desktop computers, for example, the bootstrapping process begins with the CPU executing software contained in ROM (for example, the BIOS/basic input output system of an IBM PC or an IBM PC compatible) at a predefined address (some CPUs, including the Intel x86 series, are designed to execute this software after reset without outside help). This software contains rudimentary functionality to search for devices eligible to participate in booting, and load a small program from a special section (most commonly the boot sector) of the most promising device, typically starting at a fixed entry point such as the start of the sector.

## First-stage boot loader

Examples of first-stage bootloaders include BIOS, UEFI, coreboot, Libreboot, and Das U-Boot. It initializes hardware devices such as CPU, motherboard, memory, storage and other I/O devices.

## Second-stage boot loader

Second-stage boot loaders, such as GNU GRUB, rEFInd, BOOTMGR, Syslinux, and NTLDR, are not themselves operating systems, but are able to load an operating system properly and transfer execution to it; the operating system subsequently initializes itself and may load extra device drivers.

Second-stage implementations can include interactive user interfaces, allowing boot option selection and parameter modification. They handle kernel loading, including processing of initrd/initramfs images, and can pass boot parameters to the kernel. Many implement modular designs supporting loadable modules for additional functionality. These choices can include different operating systems (for dual or multi-booting from different partitions or drives), different versions of the same operating system (in case a new version has unexpected problems), different operating system loading options (e.g., booting into a rescue or safe mode), and some standalone programs that can function without an operating system, such as memory testers (e.g., memtest86+), a basic shell (as in GNU GRUB), or even games (see List of PC booter games). Some boot loaders can also load other boot loaders; for example, GRUB loads BOOTMGR instead of loading Windows directly. Usually, a default choice is preselected with a time delay during which a user can press a key to change the choice; after this delay, the default choice is automatically run so normal booting can occur without interaction. They may also handle compression, cryptographic verification, and chain-loading of other bootloaders. The boot process can be considered complete when the computer is ready to interact with the user, or the operating system is capable of running system programs or application programs.

## Examples

### IBM-compatible personal computers

#### Legacy BIOS

In x86 computers, after the BIOS executes Power-On Self Test, it executes the first-stage bootloader, which is a compact 512-byte program that resides in the master boot record (MBR). Running in 16-bit real mode at address 0x7C00, it locates the second-stage bootloader. Its primary challenge lies in accomplishing these tasks within strict size constraints while handling potential hardware failures. The bootloader must navigate disk structures, often implementing FAT file system support, and manage the delicate transition from the BIOS startup state to a stable environment for the next boot stage.

First-stage MBR boot loaders may face peculiar constraints, especially in size; for instance, on the earlier IBM PC and compatibles, a boot sector should typically work with 510 bytes of code (or less) and in only 32 KiB (later relaxed to 64 KiB) of system memory and only use instructions supported by the original 8088/8086 processors. The first stage of PC boot loaders (FSBL, first-stage boot loader) located on fixed disks and removable drives must fit into the first 446 bytes of the master boot record in order to leave room for the default 64-byte partition table with four partition entries and the two-byte boot signature, which the BIOS requires for a proper boot loader — or even less, when additional features like more than four partition entries (up to 16 with 16 bytes each), a disk signature (6 bytes), a disk timestamp (6 bytes), an Advanced Active Partition (18 bytes) or special multi-boot loaders have to be supported as well in some environments.

In floppy and superfloppy volume boot records, up to 59 bytes are occupied for the extended BIOS parameter block (EBPB) on FAT12 and FAT16 volumes since DOS 4.0, whereas the FAT32 EBPB introduced with DOS 7.1 requires even 87 bytes, leaving only 423 bytes for the boot loader when assuming a sector size of 512 bytes. Microsoft boot sectors, therefore, traditionally imposed certain restrictions on the boot process. For example, the boot file had to be located at a fixed position in the root directory of the file system and stored within consecutive sectors, conditions taken care of by the `SYS` command and slightly relaxed in later versions of DOS. The boot loader was then able to load the first three sectors of the file into memory, which happened to contain another embedded boot loader able to load the remainder of the file into memory. When Microsoft added logical block addressing (LBA) and FAT32 support, they switched to a boot loader reaching over *two* physical sectors, using 386 instructions for size reasons. At the same time, other vendors managed to squeeze much more functionality into a single boot sector without relaxing the original constraints on only minimal available memory (32 KiB) and processor support (8088/8086). For example, DR-DOS boot sectors are able to locate the boot file in the FAT12, FAT16 and FAT32 file systems, and load it into memory as a whole via CHS or LBA, even if the file is not stored in a fixed location and in consecutive sectors.

In x86 computers, second-stage bootloaders, such as PBR, operate without the strict 512-byte limitation of their first-stage counterparts. They execute in a more sophisticated environment, typically ranging from 8KB to several megabytes in size. This expanded space allows implementation of complex features such as filesystem support, runtime configuration, and bootloader menu interfaces. The second-stage boot loader does not need drivers for its own operation, but may instead use generic storage access methods provided by system firmware such as the BIOS, though typically with restricted hardware functionality and lower performance.

In x86 computers, third-stage bootloaders include IO.SYS, NTLDR, BOOTMGR, and GRUB.

#### UEFI

UEFI (except for CSM boot) does not rely on boot sectors; it directly loads the next-stage bootloader (such as BOOTMGR and GRUB2) from the EFI System Partition.

### IBM System/360 and successors

In IBM System/360 and successors, the **LOAD** operator control initiates a process called *Initial Program Load* (IPL), which

1. Does a *System reset*
2. Sends a *Read IPL* (IPL) channel command (0216) to the selected device in order to read 24 bytes into locations 0-23 and causes the channel to begin fetching channel command words (CCWs) at location 8; the effect is as if the channel had fetched a CCW from location 0 with a length of 24, an address of 0 and the flags containing Command Chaining + Suppress Length Indication.
3. At the completion of the operation, the system stores the I/O address in the halfword at location 2 and loads the PSW from location 0.

The operating systems for S/360 through z/Architecture reside on direct access storage devices (DASDs), e.g., disk, drum. For these devices, *Read IPL* does a seek to cylinder 000016, head 000016, and orients to record 0116. For all supported operating systems, record 0116 contains a *Read Data* CCW to read a *bootstrap record* and a *Transfer In Channel* (TIC) CCW to the bootstrap. The channel program in the bootstrap reads the IPL program text into location 0, beginning with a PSW pointing to the first IPL program text instruction.

For OS/360 the IPL program does some initialization, relocates itself, locates the *Nucleus*, loads the nucleus and transfers to the *Nucleus Initialization Program* (NIP) at the end of the Nucleus.

## Embedded and multi-stage boot loaders

Many embedded systems must boot immediately. For example, waiting a minute for a digital television or a GPS navigation device to start is generally unacceptable. Therefore, such devices have software systems in ROM or flash memory so the device can begin functioning immediately; little or no loading is necessary, because the loading can be precomputed and stored on the ROM when the device is made.

Large and complex systems may have boot procedures that proceed in multiple phases until finally the operating system and other programs are loaded and ready to execute. Because operating systems are designed as if they never start or stop, a boot loader might load the operating system, configure itself as a mere process within that system, and then irrevocably transfer control to the operating system. The boot loader then terminates normally as any other process would.

## Network booting

Most computers are also capable of booting over a computer network. In this scenario, the operating system is stored on the disk of a server, and certain parts of it are transferred to the client using a simple protocol such as the Trivial File Transfer Protocol (TFTP). After these parts have been transferred, the operating system takes over the control of the booting process.

As with the second-stage boot loader, network booting begins by using generic network access methods provided by the network interface's boot ROM, which typically contains a Preboot Execution Environment (PXE) image. No drivers are required, but the system functionality is limited until the operating system kernel and drivers are transferred and started. As a result, once the ROM-based booting has completed it is entirely possible to network boot into an operating system that itself does not have the ability to use the network interface.
