---
title: "VirtualBox"
source: https://en.wikipedia.org/wiki/VirtualBox
domain: vagrant
license: CC-BY-SA-4.0
tags: hashicorp vagrant, development environment, virtual machine provisioning, reproducible dev environment
fetched: 2026-07-02
---

# VirtualBox

**Oracle VirtualBox** (formerly **Sun VirtualBox**, **Sun xVM VirtualBox** and **InnoTek VirtualBox**) is a hosted hypervisor for x86 and ARM virtualization developed by Oracle Corporation. VirtualBox was originally created by InnoTek Systemberatung GmbH, which was acquired by Sun Microsystems in 2008, which was in turn acquired by Oracle in 2010.

VirtualBox may be installed on Microsoft Windows, macOS, Linux, Solaris and OpenSolaris. There are also ports to FreeBSD and Genode. It supports the creation and management of guest virtual machines running Windows, Linux, BSD, OS/2, Solaris, Haiku, and OSx86, as well as limited virtualization of macOS guests on Apple hardware. For some guest operating systems, a "Guest Additions" package of device drivers and system applications is available, which typically improves performance, especially that of graphics, and allows changing the resolution of the guest OS automatically when the window of the virtual machine on the host OS is resized.

Released under the terms of the GNU General Public License and, optionally, the CDDL for most files of the source distribution, VirtualBox is free and open-source software, though the Extension Pack is proprietary software, free of charge only to personal users. The license to VirtualBox was relicensed to GPLv3 with linking exceptions to the CDDL and other GPL-incompatible licenses.

## History

VirtualBox was first offered by InnoTek Systemberatung GmbH, a German company based in Weinstadt, under a proprietary software license, making one version of the product available at no cost for personal or evaluation use, subject to the VirtualBox Personal Use and Evaluation License (PUEL). In January 2007, based on counsel by LiSoG, InnoTek released VirtualBox Open Source Edition (OSE) as free and open-source software, subject to the requirements of the GNU General Public License (GPL), version 2.

InnoTek also contributed to the development of OS/2 and Linux support in virtualization and OS/2 ports of products from Connectix which were later acquired by Microsoft. Specifically, InnoTek developed the "additions" code in both Windows Virtual PC and Microsoft Virtual Server, which enables various host–guest OS interactions like shared clipboards or dynamic viewport resizing.

Sun Microsystems acquired InnoTek in February 2008.

Following the acquisition of Sun Microsystems by Oracle Corporation in January 2010, the product was re-branded as "Oracle VM VirtualBox".

In December 2019, VirtualBox removed support for software-based virtualization and exclusively performs hardware-assisted virtualization.

In August 2025, VirtualBox started fully supporting ARM virtualization.

### Release history

| Version | Release date | Notable changes |
|---|---|---|
| 3.2 | May 19, 2010 | Mac OS X Server guest support – experimental Memory ballooning (not available on Solaris hosts) RAM deduplication (Page Fusion) for Windows guests on 64-bit hosts CPU hot-plugging for Linux (hot-add and hot-remove) and certain Windows guests (hot-add only) Deleting snapshots while the VM is running Multi-monitor guest setups in the GUI, for Windows guests LSI Logic SAS controller emulation Remote Desktop Protocol (RDP) video acceleration via a non-free extension Run and control guest applications from the host – for automated software deployments |
| 4.0 | Dec 22, 2010 | The PUEL/OSE separation was abandoned in favor of an open source base product and a closed source extension pack that can be installed on top of the base product. As part of this change, additional components of VirtualBox were made open source (installers, documentation, device drivers) Intel HD audio codec emulation Intel ICH9 chipset emulation A new VM storage scheme where all VM data is stored in one single folder to improve VM portability Several UI enhancements including a new look with VM preview and scale mode On 32-bit hosts, VMs can each use more than 1.5 GB of RAM In addition to OVF, the single file OVA format is supported CPU use and I/O bandwidth can be limited per VM Support for Apple DMG images (DVD) Multi-monitor guest setups for Linux/Solaris guests (previously Windows only) Resizing of disk image formats from Oracle, VDI (VirtualBox disk image), and Microsoft, VHD (Virtual PC hard disk) |
| 4.1 | Jul 19, 2011 | Windows Aero support (experimental) Virtual machine cloning |
| 4.2 | Sep 13, 2012 | Virtual machine groups – allows management of a group of virtual machines as a single unit (power them on or off, take snapshots, etc.) Some VM settings can be altered during VM execution Support up to 36 NICs in case of the ICH9 chipset Support for limiting network I/O bandwidth Can automatically run VMs on host system startup (except on Windows hosts) |
| 4.3 | Oct 15, 2013 | VM video-capture support Host touch device support (GUI passes host touch events to guest)/USB virtualization of such devices |
| 5.0 | Jul 9, 2015 | Paravirtualization support for Windows and Linux guests to improve time-keeping accuracy and performance USB3 controller based on Intel's hardware implementation. It is supported by any Windows version starting from Windows 8, any Linux kernel starting from 2.6.31 and Mac OS X starting from version 10.7.4. Bidirectional drag and drop support for Windows, Linux and Solaris guests VM disk image encryption via a non-free extension VM output scaling and HiDPI displays support Hotplugging of SATA disks using GUI USB traffic capturing VMs can be disconnected from a GUI session and run in background AVX, AVX-2, AES-NI, SSE 4.1/4.2 instructions (if supported by the host CPU) |
| 6.0 | Dec 18, 2018 | Support for exporting virtual machines to Oracle Cloud A file manager which allows to control the guest file system and copy files from/to it VMSVGA GPU driver for Linux hosts Surround speakers setup support Support for hardware-assisted nested virtualization on AMD CPUs |
| 6.1 | Dec 10, 2019 | Support for importing virtual machines from Oracle Cloud Added nested virtualization support for Intel CPUs (it was already available for AMD CPUs) starting with Intel Core i5 Broadwell Experimental support for file transfers via drag-n-drop only for Windows host and guests (disabled by default, must be enabled using VBoxManage) Support for virtio-scsi for hard disks and optical drives, including boot support Support for hosts with up to 1024 CPUs DXVA (hardware accelerated video decoding) support for Windows guests NVRAM support for EFI which improves compatibility with many guest OSes Software keyboard (virtual) for entering any keys to a guest Guest CPU use monitoring **Dropped** support for software CPU virtualization: a CPU with hardware virtualization support is now required **Dropped** support for PCI pass-through for Linux hosts |
| 7.0 | Oct 10, 2022 | Support for Windows 11 guest: UEFI Secure Boot and emulation of TPM 1.2 and 2.0 chips Intel and AMD IOMMU emulation Full VM encryption (in previous VirtualBox releases only VM disks could be encrypted) available via CLI 3D acceleration with DirectX 11 on Windows, and DXVK on other hosts Dark mode for UI currently implemented only for Windows hosts Experimental support for Apple ARM64 hosts |
| 7.1 | Sep 9, 2024 | IPv6 support for NAT MacOS on ARM: ARM virtualization for Linux and BSD virtual machines Clipboard sharing for Wayland |
| 7.2 | Aug 14, 2025 | ARM virtualization of VMs for Windows on ARM Windows ARM virtualization for ARM hosts Experimental 3D acceleration for Direct3D 10/11 using DXMT for guests for MacOS ARM hosts |
| 7.2.6 | Jan 20, 2026 | The following previously proprietary features have been made open source: Disk and VM encryption VRDP server USB smartcard emulation |

## Licensing

The core package, since version 4 in December 2010, is free software under GNU General Public License version 2 (GPLv2). A supplementary package, under a proprietary license, adds support for USB 2.0 and 3.0 devices, Remote Desktop Protocol (RDP), disk encryption, NVMe, and Preboot Execution Environment (PXE). This package is called "VirtualBox Oracle VM VirtualBox extension pack". It includes closed-source components, so it is not source-available. The license is called *Personal Use and Evaluation License (PUEL)*. It allows gratis access for personal use, educational use, and evaluation. Since VirtualBox version 5.1.30, Oracle defines personal use as installation on a single computer for non-commercial purposes.

Prior to version 4, there were two different packages of the VirtualBox software. The full package was offered gratis under the PUEL, with licenses for other commercial deployment purchasable from Oracle. A second package called the *VirtualBox Open Source Edition (OSE)* was released under GPLv2. This removed the same proprietary components not available under GPLv2.

Since September 9, 2011, building the BIOS for VirtualBox requires the Open Watcom compiler, which is released under the Sybase Open Watcom Public License. The Open Source Initiative has approved this as "Open Source" but the Free Software Foundation and the Debian Free Software Guidelines do not consider it "free".

VirtualBox has experimental support for macOS guests. However, macOS's end user license agreement does not permit running on non-Apple hardware. The operating system enforces this by calling the Apple System Management Controller (SMC), to verify the hardware's authenticity. All Apple machines have an SMC.

## Virtualization

Users of VirtualBox can load multiple guest OSes under a single host operating-system (host OS). Each guest can be started, paused and stopped independently within its own virtual machine (VM). The user can independently configure each VM and run it under a choice of software-based virtualization or hardware assisted virtualization if the underlying host hardware supports this. The host OS and guest OSs and applications can communicate with each other through a number of mechanisms including a common clipboard and a virtualized network facility. Guest VMs can also directly communicate with each other if configured to do so.

### Hardware-assisted

VirtualBox supports both Intel's VT-x and AMD's AMD-V hardware-assisted virtualization. Making use of these facilities, VirtualBox can run each guest VM in its own separate address-space; the guest OS ring 0 code runs on the host at ring 0 in VMX non-root mode rather than in ring 1.

Starting with version 6.1, VirtualBox only supports this method. Until then, VirtualBox specifically supported some guests (including 64-bit guests, SMP guests and certain proprietary OSs) only on hosts with hardware-assisted virtualization.

### Devices and peripherals

VirtualBox emulates hard disks in three formats: the native *VDI* (Virtual Disk Image), VMware's VMDK, and Microsoft's VHD. It thus supports disks created by other hypervisor software. VirtualBox can also connect to iSCSI targets and to raw partitions on the host, using either as virtual hard disks. VirtualBox emulates IDE (PIIX4 and ICH6 controllers), SCSI, SATA (ICH8M controller), and SAS controllers, to which hard drives can be attached.

VirtualBox has supported Open Virtualization Format (OVF) since version 2.2.0 (April 2009).

Both ISO images and physical devices connected to the host can be mounted as CD or DVD drives. VirtualBox supports running operating systems from live CDs and DVDs.

By default, VirtualBox provides graphics support through a custom virtual graphics-card that is VBE or UEFI GOP compatible. The Guest Additions for Windows, Linux, Solaris, OpenSolaris, and OS/2 guests include a special video-driver that increases video performance and includes additional features, such as automatically adjusting the guest resolution when resizing the VM window and desktop composition via virtualized WDDM drivers.

For an Ethernet network adapter, VirtualBox virtualizes these Network Interface Cards:

- AMD PCnet PCI II (Am79C970A)
- AMD PCnet-Fast III (Am79C973)
- Intel Pro/1000 MT Desktop (82540EM)
- Intel Pro/1000 MT Server (82545EM)
- Intel Pro/1000 T Server (82543GC)
- Paravirtualized network adapter (virtio-net)

The emulated network cards allow most guest OSs to run without the need to find and install drivers for networking hardware as they are shipped as part of the guest OS. A special paravirtualized network adapter is also available, which improves network performance by eliminating the need to match a specific hardware interface, but requires special driver support in the guest. (Many distributions of Linux ship with this driver included.) By default, VirtualBox uses NAT through which Internet software for end-users such as Firefox or ssh can operate. Bridged networking via a host network adapter or virtual networks between guests can also be configured. Up to 36 network adapters can be attached simultaneously, but only four are configurable through the graphical interface.

For a sound card, VirtualBox virtualizes Intel HD Audio, Intel ICH AC'97, and SoundBlaster 16 devices.

A USB 1.1 controller is emulated, so that any USB devices attached to the host can be seen in the guest. The proprietary extension pack adds a USB 2.0 or USB 3.0 controller and, if VirtualBox acts as an RDP server, it can also use USB devices on the remote RDP client, as if they were connected to the host, although only if the client supports this VirtualBox-specific extension (Oracle provides clients for Solaris, Linux, and Sun Ray thin clients that can do this, and has promised support for other platforms in future versions).

### Software-based

In the absence of hardware-assisted virtualization, versions 6.0.24 and earlier of VirtualBox made use of a standard software-based virtualization approach. This mode supports 32-bit guest operating systems which run in rings 0 and 3 of the Intel ring architecture.

- The system reconfigures the guest OS code, which would normally run in ring 0, to execute in ring 1 on the host hardware. Because this code contains many privileged instructions which cannot run natively in ring 1, VirtualBox employs a Code Scanning and Analysis Manager (CSAM) to scan the ring 0 code recursively before its first execution to identify problematic instructions and then calls the Patch Manager (PATM) to perform *in-situ* patching. This replaces the instruction with a jump to a VM-safe equivalent compiled code fragment in hypervisor memory.
- The guest user-mode code, running in ring 3, generally runs directly on the host hardware in ring 3.

In both cases, VirtualBox uses CSAM and PATM to inspect and patch the offending instructions whenever a fault occurs. VirtualBox also contains a dynamic recompiler, based on QEMU to recompile any real mode or protected mode code entirely (e.g. BIOS code, a DOS guest, or any operating system startup).

Using these techniques, VirtualBox could achieve performance comparable to that of VMware in its later versions.

The feature was dropped starting with VirtualBox 6.1.

## Features

- Snapshots of the RAM and storage that allow reverting to a prior state.
- Screenshots and screen video capture
- "Host key" for releasing the keyboard and mouse cursor to the host system if captured (coupled) to the guest system, and for keyboard shortcuts to features such as configuration, restarting, and screenshot. By default, it is the right-side Ctrl key, or on Mac, the left ⌘ Command key.
- Mouse pointer integration, meaning automatic coupling and uncoupling of mouse cursor when moved inside and outside the virtual screen, if supported by guest operating system.
- Seamless mode – the ability to run virtualized applications side by side with normal desktop applications
- Shared clipboard
- Shared folders through "guest additions" software
- Special drivers and utilities to facilitate switching between systems
- Ability to specify amount of shared RAM, video memory, and CPU execution cap
- Ability to emulate multiple screens
- Command line interaction (in addition to the GUI)
- Public API (Java, Python, SOAP, XPCOM) to control VM configuration and execution
- Nested paging for AMD-V and Intel VT (only for processors supporting SLAT and with SLAT enabled)
- Limited support for 3D graphics acceleration (including OpenGL up to (but not including) 3.0 and Direct3D 9.0c via Wine's Direct3D to OpenGL translation in versions prior to 7.0 or DXVK in later releases)
- SMP support (up to 32 virtual CPUs per virtual machine), since version 3.0
- Teleportation (aka Live Migration)
- 2D video output acceleration (not to be mistaken with video decoding acceleration), since version 3.1
- EFI has been supported since version 3.1 (Windows 7 guests are not supported)

### Storage emulation

- Ability to mount virtual hard disk drives and disk images. Virtual optical disc images can be used for booting and sharing files to guest systems lacking networking support.
- NCQ support for SATA, SCSI and SAS raw disks and partitions
- SATA disk hotplugging
- Pass-through mode for solid-state drives
- Pass-through mode for CD/DVD/BD drives – allows users to play audio CDs, burn optical disks, and play encrypted DVD discs
- Can disable host OS I/O cache
- Allows limitation of IO bandwidth
- PATA, SATA, NVMe, SCSI, SAS, iSCSI, floppy disk controllers
- VM disk image encryption using AES128/AES256

Storage support includes:

- Raw hard disk access – allows physical hard disk partitions on the host system to appear in the guest system
- VMware Virtual Machine Disk (VMDK) format support – allows exchange of disk images with VMware
- Microsoft VHD support
- QEMU qed and qcow disks
- HDD format disks (only version 2; versions 3 and 4 are not supported) used by Parallels virtualization products

## Limitations

- 3D graphics acceleration for Windows guests earlier than Windows Vista was removed in version 6.1.
- VirtualBox has a very low transfer rate to and from USB2 devices.
- For USB3 equipment, device pass-through does not work in older guest OSes, such as Windows Vista and Windows XP, which lack appropriate drivers. However, since version 5.0, VirtualBox has added an experimental USB3 controller (the Renesas uPD720201 xHCI), which enables USB3 in these operating systems. This requires editing some configuration files.
- Guest Additions for macOS are unavailable at this time.
- Native Guest Additions for Windows 9x (Windows 95, 98 and ME) are not available. This results in poor performance due to the lack of graphics acceleration with the default limited color depth. External third-party software is available to enable support for 32-bit color mode, resulting in better performance.
- EFI support is incomplete, e.g. EFI boot for a Windows 7 guest is not supported.
- Only older versions of DirectX and OpenGL pass-through are supported (the feature can be enabled using the 3D Acceleration option for each VM individually).
- Video RAM is limited to 128 MiB (256 MiB with 2D Video Acceleration enabled) due to technical difficulties (merely changing the GUI to allow the user to allocate more video RAM to a VM or manually editing the configuration file of a VM won't work and will result in a fatal error).
- Windows 95/98/98SE/ME cannot be installed or work unreliably on any CPU with frequency of ~2GHz and more (until Windows 98SE) and with modern CPUs (AMD Zen and newer; Intel Tiger Lake and newer) and hardware assisted virtualization (VirtualBox 6.1 and higher). This is due to these OSes not being coded correctly. An open source patch has been developed to fix the issue which also addresses Windows 95/98/98SE bug which makes the system crash when running on new fast CPUs.
- VirtualBox 7.0 and later is required to run a pristine Windows 11 guest. Full compatibility with Windows 11 is achieved in VirtualBox version 7.0.14 and higher.
- The provided NVMe controller doesn't support Windows guests.

## Host OS

The supported operating systems include:

- Windows 10 64-bit and higher. Support for 64-bit Windows was added with VirtualBox 1.5. Support for 32-bit Windows was removed in 6.0.
  - Support for Windows 2000 was removed in version 1.6.
  - Support for Windows XP was removed in version 5.0.
  - Support for Windows Vista was removed in version 5.2.
  - Support for Windows 7 (64-bit) was removed in version 6.1.
  - Support for Windows 8 (64-bit) was removed in version 7.0.
  - Support for Windows 8.1 (64-bit) was removed in version 7.1.
- Windows Server 2019 and higher.
  - Support for Windows Server 2003 was removed in 5.0.
  - Support for Windows Server 2008 was removed in 6.0.
  - Support for Windows Server 2008 R2 was removed in version 7.0.
  - Support for Windows Server 2012 and 2016 was removed in version 7.1.
- Linux distributions
- macOS from version 11 (Big Sur) to 14 (Sonoma) both ARM and Intel versions:
  - Preliminary Mac OS X support (beta stage) was added with VirtualBox 1.4, full support with 1.6.
  - Support for Mac OS X 10.4 (Tiger) and earlier was removed with VirtualBox 3.1.
  - Support for Mac OS X 10.5 (Leopard) was removed with VirtualBox 4.2.
  - Support for Mac OS X 10.6 (Snow Leopard) and 10.7 (Lion) was removed with VirtualBox 5.0.
  - Support for Mac OS X 10.8 (Mountain Lion) was removed with VirtualBox 5.1.
  - Support for Mac OS X 10.9 (Mavericks) was removed with VirtualBox 5.2.
  - Support for Mac OS X 10.10 (Yosemite) and OS X 10.11 (El Capitan) was removed with VirtualBox 6.0.
  - Support for macOS 10.12 (Sierra) was officially removed with VirtualBox 6.1 *(as of 6.1.16 it will still install and run, however).*
  - Support for macOS 10.13 (High Sierra) and macOS 10.14 (Mojave) was officially removed with VirtualBox 7.0.
  - Support for macOS 10.15 (Catalina) was officially removed with VirtualBox 7.1.
- Oracle Solaris

## Guest additions

Some features require the installation of the closed-source "VirtualBox Extension Pack":

- Support for a virtual USB 2.0/3.0 controller (EHCI/xHCI) (Starting with VirtualBox 7.0, this functionality was integrated into the GPL version instead.)
- PXE boot for Intel cards.
- Webcam support

While VirtualBox itself is free to use and is distributed under an open source license the VirtualBox Extension Pack is licensed under the VirtualBox Personal Use and Evaluation License (PUEL). Personal use of the extension pack is free but commercial users need to purchase a license.

Guest Additions are installed within each guest virtual machine which supports them; the Extension Pack is installed on the host running VirtualBox.
