---
title: "Boot ROM"
source: https://en.wikipedia.org/wiki/Boot_ROM
domain: tianocore-edk
license: CC-BY-SA-4.0
tags: tianocore edk2, uefi firmware, edk2 build, platform initialization
fetched: 2026-07-02
---

# Boot ROM

**Boot ROM** is a piece of read-only memory (ROM) that is used for booting a computer system. It contains instructions that are run after the CPU is reset to the reset vector, and it typically loads a bootloader. There are two types of boot ROM: a mask boot ROM that cannot be changed afterwards, and a writable boot ROM such as an EEPROM or a flash memory chip.

## Purpose

Upon power up, hardware usually starts uninitialized. To continue booting, the system may need to read a bootloader from some peripheral device, usually a data storage device. It is often easier to implement routines for reading from external storage devices in software than in hardware. A boot ROM provides a place to store this initial loading code, at a fixed location immediately available to the processor when execution starts.

## Operation

The boot ROM is mapped into memory at a fixed location, and the processor is designed to start executing from this location after reset, according to the processor's reset vector. The boot ROM is either placed on the same die as the CPU or is an external ROM chip. On modern systems, the boot ROM (whether integrated into CPU or external ROM chip) usually uses NOR flash, which supports execute in place.

The boot ROM will then initialize the hardware busses and peripherals needed to boot. In some cases, the boot ROM is capable of initializing DRAM, and in other cases it is up to the bootloader to do that. On some modern ARM CPUs, the boot ROM integrated in CPU will initialize DRAM and then load a bootloader; but after a bootloader (such as Das U-Boot) is loaded, the bootloader may reinitialize DRAM, to fix bugs and reduce cost.

At the end of the hardware initialization, the boot ROM will try to load a bootloader from external peripheral(s) (such as a hard disk drive or solid-state drive, an eMMC or eUFS card, a microSD card, an external EEPROM, and so on) or through specific protocol(s) on a communications port (such as a serial port or Ethernet, etc.).

In many systems on a chip (SoC), the peripherals or buses from which the boot ROM tries to load the bootloader, and the order in which they are loaded, can be configured. This configuration can be done by blowing some electronic fuses inside the system on a chip to encode that information, or by having specific pins or jumpers of the system on a chip high or low.

Some boot ROMs are capable of checking the digital signature of the bootloader and will refuse to run the bootloader and stop the boot if the signature is not valid or has not been signed with an authorized key. With some boot ROMs, the hash of the public key needed to verify the signatures is encoded in OTP electronic fuses inside the SoC. Some systems on a chip boot ROMs also support a public key infrastructure and the hash of the certificate authority (CA) public key is encoded in the electronic fuses instead, and the boot ROM will then be able to check if the bootloader is signed by an authorized key by verifying that key with the CA public key (whose hash is encoded in the electronic fuses).

That feature can then be used to implement security features or used as a hardware root of trust in a chain of trust, but once configured, users are denied the freedom to replace the bootloader with the one they want without the use of boot ROM exploits. Because of this, the feature has raised strong concerns from the free software community.

Just before jumping to the bootloader, some systems on a chip also remove the boot ROM from the memory mapping, while others do not, making it possible to dump the boot ROM for later analysis. If the boot ROM is still accessible, bootloaders can also call the code of the boot ROM (which is sometimes documented).

## Suspend to RAM

When a system on a chip (SoC) enters suspend-to-RAM mode, in many cases, the processor is completely off while the RAM is put in self-refresh mode. At resume, the boot ROM is executed again and many boot ROMs are able to detect that the SoC was in suspend-to-RAM mode and can resume by jumping directly to the kernel which then takes care of powering on again the peripherals which were off and restoring the state that the computer was in before.

## Specific implementations

### Allwinner

On many Allwinner systems on a chip (A10, A20, A64), the boot ROM either waits for a bootloader to be loaded through USB (if a specific PIN is high) or tries to boot on several peripherals in a fixed order.

Some Allwinner systems on a chip can verify the signature of the booloaders. But most devices being manufactured are not configured for that. This has enabled free and open-source software to add support for many Allwinner systems on a chip and devices using them in bootloaders like U-Boot.

### Apple

On iPhone, iPad, Apple Watch, iPod Touch, and Apple TV devices, the boot ROM is called "SecureROM" It is a stripped-down version of iBoot. It provides a Device Firmware Upgrade (DFU) mechanism, which can be activated using a special button combination.

### BIOS

On older IBM PC compatible computers, the BIOS serves as a boot ROM.

### NXP

The boot ROM of NXP systems on a chip (SOCs) support configuring the peripherals through specific pins of the system on a chip. On the i.MX6 family it also supports configuring the boot order through eFuses.

The boot ROM of several NXP SoCs have many ways to load the first stage bootloader (from eMMC, microSD, USB, etc.).

Several NXP SoCs can be configured to verify the signature of the bootloaders. Many devices with such SoCs were sold without that verification configured and on those devices users can install the bootloader they want, including several free and open-source software bootloaders like Das U-Boot and Barebox.

### Open Firmware

Open Firmware serves as a boot ROM in systems such as later SPARC-based machines from Sun Microsystems and PowerPC-based Macs.

### STMicroelectronics

STMicroelectronics STM32 family microcontrollers have embedded ROM (also referred as "on-chip ROM") called *system memory* to facilitate empty system flashing. Certain pin combinations or sometimes efuses and/or empty flash checks force the chip to boot from ROM instead of the firmware in main flash. This allows empty chips to be flashed without resorting to hardware programming interfaces. Technically this ROM is stored in a dedicated area of the flash array and programmed by ST during production. Most STM32 microcontrollers can at least be flashed over UART, some support USB and eventually other interfaces like e.g. I2C, SPI, or CAN. The Cortex-M core normally fetches vectors from the well-known addresses 0x00000000 (initial stack pointer value) and 0x00000004 (initial program counter value). However pins and/or fuses define which memory is mapped at these addresses. System memory is one of the mapping options, another would typically be main firmware in flash. In this case, firmware is supposed to do all the jobs boot ROMs do; part of the firmware could act as a bootloader similar to ST's boot ROM. Hardware could provide read-only enforcement on the boot area, turning it into a user-provided version of boot ROM.

### Texas Instruments

The boot ROMs of several Texas Instruments systems on a chip support configuring the peripherals through specific pins of the system on a chip. They have many ways to load the first stage bootloader (which is called MLO in the systems on a chip reference manuals):

- It can be loaded from various storage devices (MMC/SD/eMMC, NAND, etc.).
- With MMC/SD/eMMC, it can be loaded directly from card sectors (called RAW mode in the manual) or from a FAT12/16/32 partition.
- It can also be loaded from USB or UART.

On the OMAP36xx system on a chip, the boot ROM looks for the first stage bootloader at the sectors 0x0 and 0x20000 (128KB), and on the AM3358 system on a chip, it additionally looks at 0x40000 (256KiB) and 0x60000 (384KiB). In both cases its maximum size is 128KiB. This is because the (first stage) bootloader is loaded in an SRAM that is inside the system on a chip.

The OMAP and AM335x systems on a chip can be configured to verify the signature of the bootloaders. Many devices with such system on a chip were sold without verification configured and on those devices users can install the bootloader they want, including several free and open-source software bootloaders like Das U-Boot and Coreboot and Barebox.

### UEFI

UEFI serves as a boot ROM on systems such as newer IBM PC compatible computers.

## Security

### Apple

On devices running iOS, boot ROM exploits (like the limera1n, alloc8, and checkm8 exploits) are sometimes used for iOS jailbreaking. The advantage for people wanting to jailbreak their devices over exploits that affect iOS is that since the boot ROM cannot be modified—and that devices running iOS do not have fuses to append code to the boot ROM, Apple cannot fix the vulnerability on existing devices.

### Nvidia Tegra

The boot ROM of the Tegra SoC of Nvidia (used by the Nintendo Switch) contained a vulnerability which made it possible for users to run the bootloader they want.
