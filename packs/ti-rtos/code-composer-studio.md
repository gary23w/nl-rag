---
title: "Code Composer Studio"
source: https://en.wikipedia.org/wiki/Code_Composer_Studio
domain: ti-rtos
license: CC-BY-SA-4.0
tags: ti-rtos kernel, sysbios scheduler, msp430 mcu, code composer studio
fetched: 2026-07-02
---

# Code Composer Studio

**Code Composer Studio** (CCStudio or CCS) is an integrated development environment for developing applications for Texas Instruments embedded processors.

Texas Instruments embedded processors include TMS320 DSPs, OMAP system-on-a-chip, DaVinci system-on-a-chip, Sitara applications processors, Hercules microcontrollers, Simplelink MCUs (MSP432 and other Wireless connectivity microcontrollers), MSP430 and Tiva/Stellaris microcontrollers. It also enables debugging on several subsystems such as Ducati, IVA Accelerator and PRU-ICSS.

Code Composer Studio is primarily designed for embedded project design and low-level (baremetal) JTAG based debugging. Versions 4.0 to 12.8 are based on the Eclipse open source IDE, which can be easily extended to include support for OS level application debug (Linux, Android, Windows Embedded) and open source compiler suites such as GCC. Starting with Version 20 in December 2024, CCS is based on the Eclipse Theia platform and IDE.

Early versions included a real time kernel called DSP/BIOS and its later inception SYS/BIOS. Currently, the successor to these tools, the TI-RTOS embedded tools ecosystem, is available for downloading as a free plugin to Code Composer Studio.

## History

Code Composer Studio was first developed under the name Code Composer by the software company GO DSP, located in Toronto, Canada, which was acquired by Texas Instruments in 1997. Integration with DSP/BIOS was added to Code Composer, and Code Composer was rebranded as Code Composer Studio.

CCS releases up until 3.3 were based on a proprietary interface. TI developed a new IDE based on the open-source Eclipse, named Code Composer Essentials (CCE), that was designed for the MSP430 line of microcontrollers. Beginning with release 4.0, all new versions of CCS would also use an interface based upon Eclipse.

Code Composer was originally developed for DSP development and featured graphical visualization tools (XY graphs, FFT magnitude and phase, constellation, raw image visualization) and support for visualizing memory in several numeric formats (decimal, floating-point).

In 2015, a cloud computing version of CCS was introduced and is part of the suite TI Cloud Tools, which also hosts Resource Explorer and Pinmux.

## Versions

### Code Composer

- 4.10 (latest version in 2001). Supported all TMS320 DSPs at that time: C2x, C24x, C3x, C4x, C5x, C54x and C6x. The version for C3x/C4x is still sold by Texas Instruments' partner Spectrum Digital. Support varied through the years, initially Windows 95, NT4 and 98, with the latest release supporting 2000 and XP.

### Code Composer Studio

- 1.x (1999). General release that dropped support for C2x, C3x, C4x and C5x DSPs. v1.3 added support for ARM. Supports Windows 95, 98, 98SE, NT4 and 2000, as well as Sun Solaris 2.6, 2.7 and 8.
- 2.0 (2001). General release that added support for the upcoming C55x and C64x DSPs. Across the years it added support for TMS470 ARM7 (2.10), OMAP ARM9 plus C55x DSP (2.10) and C2x DSPs (2.12). Supports Windows 98SE, Me, 2000 and XP.
- 3.0 (2005). Limited release that supported only C62x, C64x and C67x DSPs. Supports Windows 2000 and XP.
- 3.1 (2005). General release. Supports Windows 2000 and XP.
- 3.2 (2006). Limited release that supported only the new C64x+ DSPs. Supports Windows 2000 and XP.
- 3.3 (2006). General release that supported all device families, and across the years it added support for OMAP Cortex A8 plus C64x+ DSP, TMS570 (ARM Cortex R4), C672x and C674x DSPs (3.3.82). A limited version for C24x DSPs only is still sold by TI. Supports Windows 2000 and XP.
- 4.0 (2009). General release based on a modified version of Eclipse 3.2. Dropped support for C24x DSPs and added support for MSP430, Stellaris (ARM Cortex M3) and DaVinci devices. Adds support for SYSBIOS and its updated debug components (ROV, Execution Graph) while keeping support for DSP/BIOS legacy debug components (RTA, LOG_Printf). Supports Windows XP, Vista and 7. Release 4.2 introduced the Grace plug-in and SYSBIOS for MSP430 devices.
- 5.0 (2010). General release that uses an unmodified version of Eclipse 3.6 and later 3.7. It was hosted also in Linux. Added support for C66x DSPs, Sitara (ARM9 and Cortex A8) and Tiva (ARM Cortex M4) devices. Supports Windows XP and 7. Release 5.3 implements a completely reworked Trace interface as well as version 2.0 of Grace.
- 6.0 (2014). General release that uses an unmodified version of Eclipse 4.3. Added support for CC26x and CC32x wireless microcontrollers. Dropped support for C54x DSPs. Supports Windows XP, 7 and 8.x.
- 6.1 (2015). General release that uses an unmodified version of Eclipse 4.4. Introduced beta support for Mac OS X. Added support for CC25x and MSP432 (the introductory Mac version supports only MSP devices). Supports Windows XP, 7 and 8.x.
- 6.1.1 Added support for SimpleLink™ CC26xx and CC13xx MCU platform of devices. Added support for automatic firmware update for XDS110. Added OS X platform support for CCS for MCU devices (Beta). Improved EnergyTrace tool for profiling application's energy consumption, battery lifetime, monitoring internal device states and determining execution hotspots (statistical function profile).
- 6.1.2 Bug fixes. First OS X released to the public in Beta. Last version that supports the Grace plug-in.
- 6.1.3 Integration with Eclipse v4.5.1 and CDT 8.7. Added support for OS X for MCU devices. Support for GCC for MSP430. Improved Cortex A15 SM debug support. Improved EnergyTrace tool for profiling application's energy consumption, battery lifetime, monitoring internal device states and determining execution hotspots (statistical function profile).
- 6.2.0 (2016). First 64-bit version for Linux (Windows still 32-bit). Beta release of the online Resource Explorer.
- 7.0.0 (2016). Integration with Eclipse 4.6 with CDT 9.0 and JRE 8. First release that is free of charge and without limitations for all devices and Debug Probes. Production release of the online Resource Explorer. Dropped support for Windows XP and the Stellaris devices.
- 7.1.0 (2016). Bug fixes. Added support for EnergyTrace HDR (High Dynamic Range) for Simplelink MCUs. Beta version of ROV2.
- 7.2.0 (2017). Bug fixes. Production version of ROV2.
- 7.3.0 (2017). Bug fixes.
- 7.4.0 (2017). Bug fixes and other updates including device support.
- 8.1.0 (2018). Bug fixes.
- 8.2.0 (2018). Bug fixes and other updates including device support.
- 8.3.0 (2018). Bug fixes.
- 8.3.1 (2019). Bug fixes.
- 9.0.0 (2019). Supported only on 64bit Windows machines. Bug fixes and other updates including device support.
- 9.0.1 (2019). Bug fixes and other updates including device support.
- 9.1.0 (2019). Bug fixes and other updates including device support.
- 9.2.0 (2019). Bug fixes and other updates including device support.
- 9.3.0 (2019). Bug fixes Mac OS installers are now distributed.
- 10.0.0 (2020). Bug fixes. General Enhancements(compiler/IDE/Debugger).
- 10.1.0 (2020). Bug fixes.
- 10.1.1 (2020). Bug fixes.
- 10.2.0 (2021). Bug fixes.
- 10.3.0 (2021). Bug fixes.
- 10.3.1 (2021). Bug fixes.
- 10.4.0 (2021). Bug fixes.
- 11.0.0 (2021). Bug fixes. General Enhancements(compiler/IDE/Debugger).
- 11.1.0 (2021). Bug fixes.
- 11.2.0 (2022). Bug fixes.
- 12.0.0 (2022). Bug fixes. General Enhancements(compiler/IDE/Debugger).
- 12.1.0 (2022). Bug fixes.
- 12.2.0 (2023). Bug fixes.
- 12.3.0 (2023). Bug fixes.
- 12.4.0 (2023). Bug fixes.
- 12.5.0 (2023). Bug fixes. General Enhancements(compiler/IDE/Debugger).
- 12.6.0 (2024). Bug fixes.
- 12.7.0 (2024). Bug fixes.
- 12.7.1 (2024). Bug fixes.
- 12.8.0 (2024). Bug fixes.
- 12.8.1 (2024). Bug fixes.
- 20.0.0 (2024). First version of Code Composer Studio based on the Theia IDE.
- 20.0.1 (2024). Maintenance release for 20.0.0, with enhancements and bug fixes.
- 20.0.2 (2025). Maintenance release based on 20.0.1, with various enhancements and bug fixes.
- 20.1.0 (2025). Improved startup on macOS versions with ARM processors. Added support for various devices and updated the CLANG compiler.
- 20.1.1 (2025). Maintenance release for 20.1.0, fixing bugs and adding debug enhancements.
- 20.2.0 (2025). Theia IDE core update, and added AI features accessible through Theia AI or 3rd-party extensions. Added various debug, IDE, and project enhancements. Added support for various API's, updated compilers, and Device Support.
- 20.3.0 (2025). Added IDE enhancements, including support for aligning address boundary settings and Python scripting. Added support for multiple new devices. Added a secure debug manager for CC27xx devices.

### CCS Cloud

- 1.0 (2015). General release that adds support for all MSP430, MSP432 and Tiva C device families.
- 1.1 (2015). General release that adds debug capabilities for all devices above. Added CC2650 device support.
- 1.6 (2017). General release with bug fixes.

## Licensing

Over the years, CCS followed the trend of the software industry for reduced and free-of-charge software licensing, reflected across the releases:

- CCS releases up to 2.x were separated per device family, i.e., every device family required the purchase of a separate license and a separate software Each license's SRP was US$3,600.00 (apart from release 2.3, which was about US$4,500.00)
- Starting with releases 3.x, all device families were included in the same license (then called Platinum). The license's SRP was the same (US$3,600.00). There was a C2x-only limited license that retailed for US$600.00.
- Starting with release 4.x, CCS can be used for free in several scenarios that include development boards, software device simulators and even the use of a standalone emulator named XDS100. Also, it can be used with a code size limitation of 16kB on MSP430 devices. This release also introduced the floating license, which can be installed on a server and be used across a company's or university's Intranet at almost the cost of a full license.
  - A full license for CCS release 4.x had an SRP of US$1,995.00 and a microcontroller-only license was US$495.00. This microcontroller license covered all MSP430, Stellaris and C2x devices.
  - A full license for CCS releases 5.x and 6.x has an SRP of US$495.00 and the microcontroller-only license ceased to exist.
  - Starting in September 2016, the floating license model ceased to exist.
  - For CCS release 7.x the paid license ceased to exist. The software and all its components are distributed with a TSPA license.
    - The free license model was also retrofitted to all public CCS releases since v4.

For all releases an annual paid subscription fee was required to grant updates for upcoming major releases.

- Starting in August 2015, the concept of subscription fee ceased to exist.

## JTAG Debug probe support

Historically CCS supported only JTAG debug probes from TI - also called XDS emulators. The XDS510-class and the more advanced XDS560-class emulators are supported across all releases, but the new low-cost XDS100-class emulator started to be supported starting with the latest patches to release 3.3.

Releases 4.x added support for an updated design of the existing XDS100-class emulator (called XDS100v2) and, in release 4.2, added support for an updated design of the XDS560-class emulator (called XDS560v2).

Release 5.2 added support for the new XDS200-class emulators.

Up until release 4.x, CCS supported only XDS emulators. With the integration of MSP430 and Stellaris microcontrollers, support was added for their respective JTAG debug probes: MSP-FET430 (both parallel and USB versions) and ICDI.

Release 5.x also saw the introduction of Beta support for J-Link JTAG debug probes from Segger.

Release 6.0.x saw the introduction of the new MSP-FET debug probe for MSP430 devices and the new XDS200-class of debug probes for processors.

Release 6.1.x saw the introduction of the new XDS110-class of debug probes for processors. It also saw the migration to full production support for J-Link JTAG debug probes from Segger.

Release 7.x saw the integration of J-Link JTAG debug probes from Segger directly in the CCS installer. It is also the first release to support the standalone version of XDS110.

64-bit releases do not support Spectrum Digital XDS510USB JTAG debuggers.
