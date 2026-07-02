---
title: "System in a package"
source: https://en.wikipedia.org/wiki/System_in_package
domain: system-in-package
license: CC-BY-SA-4.0
tags: system in package, wafer-level packaging, ball grid array, flip chip bonding
fetched: 2026-07-02
---

# System in a package

(Redirected from

System in package

)

A **system in a package**, or **system in package** (**SiP**), is a number of integrated circuits (ICs) enclosed in one chip carrier package or encompassing an IC package substrate that may include passive components and perform the functions of an entire system. The ICs may be stacked using die stacking or package on package, placed side by side (multi-chip module, MCM), and/or embedded in the substrate. The SiP performs all or most of the functions of an electronic system, and is typically used when designing components for mobile phones, digital music players, etc. Dies containing integrated circuits may be stacked vertically on the package substrate. They are internally connected by fine wires that are bonded to the package substrate. Alternatively, with a flip chip technology, solder bumps are used to join stacked chips together and to the package substrate, or even both techniques can be used in a single package. SiPs are like systems on a chip (SoCs) but less tightly integrated and not on a single semiconductor die.

SIPs can be used either to reduce the size of a system, improve performance or to reduce costs. Some definitions of SiP exclude those that only use two-dimensional MCM.

## Technology

SiP dies can be stacked vertically or tiled horizontally, with techniques like chiplets or quilt packaging. SiPs connect the dies with standard off-chip wire bonds or solder bumps, unlike slightly denser three-dimensional integrated circuits which connect stacked silicon dies with conductors running through the die using through-silicon vias. Many different 3D packaging techniques have been developed for stacking many fairly standard chip dies into a compact area.

SiPs can contain several chips or dies—such as a specialized processor, DRAM, flash memory—combined with passive components—resistors and capacitors—all mounted on the same substrate. This means that a complete functional unit can be built in a single package, so that few external components need to be added to make it work. This is particularly valuable in space constrained environments like MP3 players and mobile phones as it reduces the complexity of the printed circuit board and overall design. Despite its benefits, this technique decreases the yield of fabrication since any defective chip in the package will result in a non-functional packaged integrated circuit, even if all other modules in that same package are functional.

SiPs are in contrast to the common system on a chip (SoC) integrated circuit architecture which integrates components based on function into a single circuit die. An SoC will typically integrate a CPU, graphics and memory interfaces, hard-disk and USB connectivity, random-access and read-only memories, and secondary storage and/or their controllers on a single die. In comparison a SiP would connect these modules as discrete components in one or more chip packages or dies. A SiP resembles the common traditional motherboard-based PC architecture, as it separates components based on function and connects them through a central interfacing circuit board. A SiP has a lower grade of integration in comparison to an SoC. Hybrid integrated circuits (HICs) are somewhat similar to SiPs, however they tend to handle analog signals whereas SiPs usually handle digital signals, because of this HICs use older or less advanced technology (tend to use single layer circuit boards or substrates, not use die stacking, do not use flip chip or BGA for connecting components or dies, use only wire bonding for connecting dies or Small outline integrated circuit packages, use Dual in-line packages, or Single in-line packages for interfacing outside the Hybrid IC instead of BGA, etc.).

SiP solutions may require multiple packaging technologies, such as flip chip, wire bonding, wafer-level packaging, through-silicon vias (TSVs), chiplets and more.

## Applications

### Embedded systems

### Mobile computing

SiP technology is primarily being driven by early market trends in wearables, mobile devices and the Internet of things which do not demand the high numbers of produced units as in the established consumer and business SoC market. As the Internet of things becomes more commonplace in the SiP market, advances in SiP packaging design enable microelectromechanical (MEMS) sensors to be integrated on a separate die and control connectivity.

### Personal computers

Desktop SiPs generally integrate CPU, memory controller, high-speed IO (PCIe/USB3/USB4), and sometimes integrated graphics. Storage such as main memory and disks are left separate.

AMD desktop CPUs since Zen 2 use a MCM design. The CPU handles its own PCIe, USB3, and in those with integrated graphics, display output. Lower-speed I/O such as extra PCIe lanes, SATA, slower USB, and serial links such as SPI and SMBus are still handled by a "chipset", actually a PCIe device.

Intel mobile CPUs beginning with ultra-low-power Haswells and continuing with mobile Skylake also use a SiP design. These directly expose PCIe lanes, as well as SATA, USB, and HDA lines from integrated controllers, and SPI/I²C/UART/GPIO lines for sensors. Like PCH-compatible CPUs, they continue to expose DisplayPort, RAM, and SMBus lines. However, a fully integrated voltage regulator will be absent until Cannon Lake.

## Suppliers

Embedded/Mobile:

- Amkor Technology
- Atmel
- AMPAK Technology Inc.
- NANIUM, S.A.
- ASE Group
- CeraMicro
- ChipSiP Technology
- Cypress Semiconductor
- STATS ChipPAC Ltd
- Toshiba
- Renesas
- SanDisk
- Samsung
- Silicon Labs
- Octavo Systems
- Nordic Semiconductor
- JCET
- Desay Sip
- Universal Scientific Industrial (USI)

Personal computers:

- Advanced Micro Devices
- Intel
