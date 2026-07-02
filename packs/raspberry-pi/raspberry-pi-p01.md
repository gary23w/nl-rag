---
title: "Raspberry Pi (part 1/2)"
source: https://en.wikipedia.org/wiki/Raspberry_Pi
domain: raspberry-pi
license: CC-BY-SA-4.0
tags: raspberry pi, raspberry pi os, raspbian, pi pico, rp2040
fetched: 2026-07-02
part: 1/2
---

# Raspberry Pi

**Raspberry Pi** (/paɪ/ *PY*) is a series of small single-board computers (SBCs) originally developed in the United Kingdom by the Raspberry Pi Foundation in collaboration with Broadcom. To commercialize the product and support its growing demand, the Foundation established a commercial entity, now known as Raspberry Pi Holdings.

The Raspberry Pi was originally created to help teach computer science in schools, but gained popularity for many other uses due to its low cost, compact size, and flexibility. It is now used in areas such as industrial automation, robotics, home automation, IoT devices, and hobbyist projects.

The company's products range from simple microcontrollers to computers that the company markets as being powerful enough to be used as a general purpose PC. Computers are built around a custom designed system on a chip and offer features such as HDMI video/audio output, USB ports, wireless networking, GPIO pins, and up to 16 GB of RAM. Storage is typically provided via microSD cards.

In 2015, the Raspberry Pi surpassed the ZX Spectrum as the best-selling British computer of all time. As of March 2025, 68 million units had been sold.


## History

### Origins and launch (2008–2012)

The Raspberry Pi Foundation was established in 2008 by a group including Eben Upton, in response to a noticeable decline in both the number and skill level of students applying to study computer science at the University of Cambridge Computer Laboratory. The foundation's goal was to create a low-cost computer to help rekindle interest in programming among schoolchildren.

This mission was inspired by the aims of the BBC Micro computer of the early 1980s, which was developed by Acorn Computers as part of a BBC initiative to promote computer literacy in UK schools. The names "Model A" and "Model B" were chosen as a deliberate homage to the BBC Micro. The name "Raspberry Pi" combines the fruit-themed naming convention used by early computer companies with a nod to the Python programming language.

The first prototypes resembled small USB sticks. By August 2011, fifty functionally complete "alpha" boards were produced for testing, with demonstrations showing them running a Debian-based desktop and handling 1080p video playback. In late 2011, twenty-five "beta" boards were finalized, and to generate publicity before the official launch, ten of these were auctioned on eBay in early 2012.

The first commercial Raspberry Pi, the Model B, was launched on 29 February 2012, with an initial price of $35. Demand far exceeded expectations, causing the websites of the two initial licensed distributors, Premier Farnell and RS Components, to crash from high traffic. Initial batches sold out almost immediately, with one distributor reporting over 100,000 pre-orders on the first day. The lower-cost $25 Model A followed on 4 February 2013.

The Raspberry Pi did not ship with a pre-installed operating system. While ports of RISC OS 5 and Fedora Linux were available, a port of Debian called Raspbian quickly became the standard. Released in July 2012, it was optimized to leverage the Raspberry Pi's floating-point unit, offering significant performance gains. Raspberry Pi quickly endorsed it as the official recommended OS, and by September 2013, the company assumed leadership of Raspbian's development.

### Corporate evolution

In 2012, the Foundation restructured, creating Raspberry Pi (Trading) Ltd. to handle engineering and commercial activities, with Eben Upton as its CEO. This allowed the Raspberry Pi Foundation to focus solely on its charitable and educational mission. Raspberry Pi (Trading) Ltd. was renamed Raspberry Pi Ltd. in 2021. In June 2024, the company went public on the London Stock Exchange under the ticker symbol RPI, becoming Raspberry Pi Holdings.

### Post-launch production (2012–2014)

Following the launch, the first units reached buyers in April 2012. To address overwhelming demand and initial supply chain issues, the Foundation ramped up production to 4,000 units per day by July. The first batch of 10,000 boards was produced in factories located in Taiwan and China. A significant strategic shift occurred in September 2012, when manufacturing began moving to a Sony factory in Pencoed, Wales. During this period, the hardware was also refined: the Model B Revision 2.0 board was announced with minor corrections, and in October, its included RAM was doubled to 512 MB.

The post-launch period focused heavily on software and ecosystem development. In August 2012, the Foundation enabled hardware-accelerated H.264 video encoding and began selling licenses for MPEG-2 and VC-1 codecs. A major milestone for the open-source community occurred in October 2012, when the Foundation released the Videocore IV graphics driver as free software. While the claim of it being the first fully open-source ARM SoC driver was debated, the move was widely praised. This effort culminated in February 2014 with the release of full documentation for the graphics core and a complete source release of the graphics stack under a 3-clause BSD license.

### Product line expansion (2014–present)

In 2014, the Raspberry Pi product line began to diversify. April saw the release of the Compute Module, a miniature Raspberry Pi in a small form factor designed for industrial and embedded applications, which would soon become the largest market for the computers. In July the Model B+ was released with a refined design featuring additional USB ports and a more efficient board layout that established the form factor for future models. A smaller, cheaper ($20) Model A+ was released in November. A significant leap in performance came in February 2015 with the Raspberry Pi 2, which featured a 900 MHz quad-core CPU and 1 GB of RAM. Following its release, the price of the Model B+ was lowered to $25, a move some observers linked to the emergence of lower-priced competitors.

The Raspberry Pi Zero, launched in November 2015, radically redefined the entry point for computing at a price of just $5. In February 2016, the Raspberry Pi 3 marked another major milestone by integrating a 64-bit processor, Wi-Fi, and Bluetooth. The product line continued to expand with the wireless-enabled Raspberry Pi Zero W (February 2017), the faster Raspberry Pi 3B+ (March 2018), Raspberry Pi 3A+ (November 2018), and Compute Module 3+ (January 2019).

The Raspberry Pi 4, launched in June 2019, represented another major performance leap with a faster processor, up to 8 GB of RAM, dual-monitor support, and USB 3.0 ports. A compute module version (CM4) launched in October 2020. This era saw further diversification with the Raspberry Pi 400 (a computer integrated into a keyboard) in November 2020, and the Raspberry Pi Pico in January 2021. The Pico, based on the in-house designed RP2040 chip, marked the company's first entry into the low-cost microcontroller market. The Raspberry Pi Zero 2 W, introduced in 2021, featured a faster processor, providing a significant performance boost while maintaining the low-cost, compact form factor.

The global chip shortage starting in 2020, as well as an uptake in demand starting in early 2021, notably affected the Raspberry Pi, causing significant availability issues from that time onward. The company explained its approach to the shortages in 2021, and April 2022, explaining that it was prioritising business and industrial customers.

The Raspberry Pi 5 was released in October 2023, featuring an upgraded CPU and GPU, up to 16 GB of RAM, a PCIe interface for fast peripherals and an in-house designed southbridge chip. Updated versions of the Compute Module (CM5) and keyboard computer (Pi 500, Pi 500+) based on the Pi 5's architecture were subsequently announced. The Raspberry Pi Pico 2, released in 2024, introduced the RP2350 microcontroller, featuring two Hazard3 RISC-V and two ARM Cortex-M33 cores, any two of which may be selected at boot time, 520 KB of RAM, and 4 MB of flash memory.

Raspberry Pi expanded its artificial intelligence focused hardware ecosystem with the release of the Raspberry Pi AI Camera, based on Sony's IMX500 Intelligent Vision Sensor. The product integrated on-sensor neural network inference, enabling edge-based computer vision applications when paired with Raspberry Pi computers. The company also introduced the Raspberry Pi AI HAT+, incorporating a Hailo neural processing unit (NPU) to accelerate machine learning workloads on the Raspberry Pi 5 platform. The accessory was positioned for high-performance edge inference use cases, including industrial automation and embedded AI systems.

During the same period, Raspberry Pi announced updated keyboard-integrated desktop models derived from the Raspberry Pi 5 architecture. These revisions included expanded memory configurations and enhanced storage options, continuing the company's development of compact, integrated desktop computing systems.

### Sales milestones

The Raspberry Pi's sales demonstrated remarkable growth. The one-millionth Pi was sold by October 2013, a figure that doubled just a month later. By February 2016, sales reached eight million units, surpassing the ZX Spectrum as the best-selling British computer of all time. Sales hit ten million in September 2016, thirty million by December 2019, and forty million by May 2021. As of its tenth anniversary in February 2022, a total of 46 million Raspberry Pis had been sold. As of March 2025, 68 million units had been sold.


## Series and generations

There are five main series of Raspberry Pi computers, each with multiple generations. Most models feature a Broadcom system on a chip (SoC) with an integrated ARM-based central processing unit (CPU) and an on-chip graphics processing unit (GPU). The exception is the Pico series, a microcontroller which uses the RP2040, a custom-designed SoC with an ARM-compatible CPU but no GPU.

### Flagship series

Original Raspberry Pi Model B, introduced in 2012

Raspberry Pi Model A+, introduced in 2014

Raspberry Pi 5, introduced in 2023

The flagship Raspberry Pi series, often referred to simply as "Raspberry Pi", offers high-performance hardware, a full Linux operating system, and a variety of common ports in a compact form factor roughly the size of a credit card.

- The **Model B** (2012) features a 700 MHz single-core 32-bit ARM11 CPU, a VideoCore IV GPU, 512 MB RAM and a 26-pin GPIO header.
- The **Model A** (2013) is a lower-cost version with 256 MB RAM, no Ethernet, and fewer USB ports.
- The **Model B+** and **Model A+** (2014) add a 40-pin GPIO header, microSD card support, and replace the RCA video connector with a combined 3.5 mm audio/video jack.
- The **Raspberry Pi 2 Model B**, v 1.1 (2015) includes a 900 MHz quad-core Cortex-A7 CPU and 1 GB of RAM.
- The **Raspberry Pi 2 Model B**, v 1.2 (2016) or v 1.3 includes a 900 MHz quad-core Cortex-A53 CPU and 1 GB of RAM.
- The **Raspberry Pi 3 Model B** (2016) features a 1.2 GHz quad-core 64-bit Cortex-A53 CPU, Wi-Fi, Bluetooth, and USB boot support.
- The **Raspberry Pi 3 Model B+** (2018) upgrades to a 1.4 GHz CPU, faster Ethernet, dual-band Wi-Fi, and Power over Ethernet (PoE) support.
- The **Raspberry Pi 3 Model A+** (2018) is the final A-series model, offering the same features as the 3B+, but with 512 MB RAM and in a smaller form factor.
- The **Raspberry Pi 4** (2019) introduces a 1.5 GHz quad-core Cortex-A72 CPU, a VideoCore VI GPU, USB 3.0 ports, true Gigabit Ethernet, support for dual 4K monitors, and options for 1, 2, 3, 4, or 8 GB of RAM.
- The **Raspberry Pi 5** (2023) features a 2.4 GHz quad-core Cortex-A76 CPU, a VideoCore VII GPU, PCIe support, and options for 1, 2, 4, 8, or 16 GB of RAM.

### Keyboard Computer series

The Keyboard Computer series combines Raspberry Pi board and a keyboard into a keyboard computer form factor, providing a self-contained Linux-based desktop system.

- The **Raspberry Pi 400** (2020) features a custom board based on the Pi 4. It includes a 1.8 GHz quad-core Cortex-A72 processor, 4 GB of RAM, and a large integrated heat sink. It supports dual 4K monitors via two micro HDMI ports and includes gigabit Ethernet.
- The **Raspberry Pi 500** (2024) is based on the Pi 5 and succeeds the Pi 400. It features a 2.4 GHz quad-core Cortex-A76 processor and 8 GB of RAM. Unlike the Raspberry Pi 5, it lacks a PCIe interface.
- The **Raspberry Pi 500+** (2025) is based on the Pi 5. It features the same 2.4 GHz quad-core Cortex-A76 processor as the Pi 500, 16 GB of RAM and an M.2 slot with a 256 GB SSD preinstalled. It replaces the membrane keyboard of the original model for a mechanical variant with RGB lighting.

### Zero series

The Raspberry Pi Zero, introduced in 2015

The Raspberry Pi Zero 2 W, introduced in 2021

The Raspberry Pi Zero is a series of compact, low-cost, and low-power single-board computers that provide basic functionality and Linux compatibility for embedded and minimalist computing applications.

- The **Raspberry Pi Zero** (2015), priced at US$5, features a 1 GHz single-core 32-bit ARM11 CPU, 512 MB of RAM, mini HDMI, and micro USB ports for data and power. It includes an unpopulated 40-pin GPIO header.
  - The **Zero v1.3** (2016) added a camera connector.
  - The **Zero W** (2017) introduced onboard Wi-Fi and Bluetooth for US$10.
  - The **Zero WH** (2018) added pre-soldered GPIO pins for US$15.
- The **Raspberry Pi Zero 2 W** (2021), priced at US$15, features a quad-core 64-bit ARM Cortex-A53 CPU and includes wireless connectivity. The **Zero 2 WH** variant adds a pre-soldered GPIO header for US$18.

### Pico series

The Pico is a series of compact microcontroller boards based on Raspberry Pi-designed chips. Unlike other models, they do not run Linux or support removable storage, and are instead programmed by flashing binaries to onboard flash memory.

- The **Raspberry Pi Pico** (2021) was the first board based on the in-house RP2040 microcontroller. It features a dual-core 32-bit ARM Cortex-M0+ CPU, 264 KB of RAM, and 2 MB of flash memory, priced at US$4. The **Pico W** (2022) adds Wi-Fi and Bluetooth and launched at US$6. The board has a castellated edge for direct soldering to a carrier board; versions are available with pre-soldered, bottom-mounted header pins, the **Pico H** for US$5 and the **Pico WH** for US$7.
- The **Raspberry Pi Pico 2** (2024) introduced the RP2350 microcontroller, featuring a pair of 32-bit ARM Cortex-M33 cores and a pair of Hazard3 RISC-V processor cores (the user can select any two cores), 520 KB of RAM, and 4 MB of flash memory, priced at US$5. The **Pico 2 W** adds Wi-Fi and Bluetooth at US$7.

### Compute Module series

Raspberry Pi Compute Module 3

Raspberry Pi Compute Module 4

The **Compute Module** (CM) series delivers Raspberry Pi's flagship hardware in a compact form for industrial and embedded applications, omitting onboard ports and GPIO headers in favour of a carrier board interface. Compute Modules are offered in one of two formats: a board matching the physical dimensions of a DDR2 SO-DIMM RAM module (though electrically incompatible with standard SO-DIMM sockets) and a smaller board with dual 100-pin high-density connectors that enables additional interfaces.

- **Compute Module 1** (2014) – Based on the original Raspberry Pi. Features a single-core ARM11 CPU, 512 MB RAM, and 4 GB eMMC flash storage. SO-DIMM form factor.
- **Compute Module 3** (2017) – Based on the Pi 3. Includes a quad-core 64-bit Cortex-A53 CPU, 1 GB RAM, and 4 GB eMMC; also available as a "Lite" variant without eMMC. SO-DIMM form factor.
- **Compute Module 3+** (2019) – Based on the Pi 3+. Offers 0 (Lite), 8, 16, or 32 GB eMMC options. SO-DIMM form factor.
- **Compute Module 4** (2020) – Based on the Pi 4. Includes a quad-core 64-bit Cortex-A72 CPU, 1, 2, 4, or 8 GB RAM, and 0 (Lite), 8, 16, or 32 GB eMMC; optional Wi-Fi and Bluetooth. High-density connector form factor; CM4S variant uses SO-DIMM form factor.
- **Compute Module 5** (2024) – Based on the Pi 5. Features a quad-core 64-bit Cortex-A76 CPU, 2, 4, 8, or 16 GB RAM, and 0 (Lite), 16, 32, or 64 GB eMMC; optional Wi-Fi and Bluetooth. High-density connector form factor.

### Model/series comparison table

Series

Model

SoC

CPU

Memory

Ethernet

Wireless

USB

GPIO

header

Released

MSRP

(US$)

Flagship

Model B

1

BCM2835

1×

ARM11

512 MB

100 Mbit

No

2 × 2.0

26-pin

2012

35

1+

4 × 2.0

40-pin

2014

2 (v 1.1)

BCM2836

4×

A7

1 GB

2015

2 (v 1.2/1.3)

BCM2837

4×

A53

2016

3

2.4 GHz

Wi-Fi 4

Bluetooth 4.1/BLE

3+

300 Mbit

2.4/5 GHz

Wi-Fi 5

Bluetooth 4.2/BLE

2018

4

BCM2711

4×

A72

1, 2, 3, 4 or 8 GB

Gigabit

2.4/5 GHz

Wi-Fi 5

Bluetooth 5.0/BLE

2 × 2.0

2 × 3.0

2019

35–85

5

BCM2712

4×

A76

1, 2, 4, 8 or 16 GB

2023

45–305

Flagship

Model A

1

BCM2835

1×

ARM11

256 MB

No

No

1 × 2.0

26-pin

2013

25

1+

512 MB

40-pin

2014

3+

BCM2837

4×

A53

2.4/5 GHz

Wi-Fi 5

Bluetooth 4.2/BLE

2018

Keyboard

400

BCM2711

4×

A72

4 GB

Gigabit

2.4/5 GHz

Wi-Fi 5

Bluetooth 5.0/BLE

1 × 2.0

2 × 3.0

40-pin

2020

70

500

BCM2712

4×

A76

8 GB

2024

130

500+

16 GB

2025

260

Zero

1

BCM2835

1×

ARM11

512 MB

No

Optional

2.4 GHz

Wi-Fi 4

Bluetooth 4.1/BLE

1 × 2.0

40-pin

2015

5–15

2

BCM2710

4×

A53

2.4 GHz

Wi-Fi 4

Bluetooth 4.2/BLE

2021

15–18

Pico

1

RP2040

2×

M0+

264 KB

No

Optional

2.4 GHz

Wi-Fi 4

Bluetooth 5.2/BLE

1 × 2.0

40-pin

2021

4–7

2

RP2350

2×

ARM Cortex-M33

, 2×

RISC-V

Hazard3, or 1× M33 + 1× RISC-V

520 KB

2024

5–8

Compute

Module

1

BCM2835

1×

ARM11

512 MB

No

No

No

No

2014

30

3/3+

BCM2837

4×

A53

1 GB

2017

25–40

4

BCM2711

4×

A72

1, 2, 4 or 8 GB

Optional

2.4/5 GHz

Wi-Fi 5

Bluetooth 5.0/BLE

2020

30–125

5

BCM2712

4×

A76

2, 4, 8 or 16 GB

2024

55–215

**Notes**

1. Marketed as Gigabit Ethernet, but actual throughput is limited to approximately 300 Mbit/s due to the internal USB 2.0 connection.
2. "W" models only
3. Custom Raspberry Pi SiP RP3A0
4. Signals routed through board connector


## Hardware

Since its introduction, Raspberry Pi hardware has been designed to provide low-cost computing platforms. The founders intended it to be an affordable and accessible system by making it compatible with widely available second-hand peripherals, such as televisions for displays, USB input devices, and cellphone chargers for power. Over time, the hardware has expanded to support both advanced configurations and ultra-low-cost variants.

The company has committed to keeping its single-board computer products in production for at least ten years, longer than typical consumer electronics. It also publishes guaranteed minimum manufacturing end dates. These policies are intended to support the use of its products in industrial and OEM applications that require long-term availability. For example, the original Raspberry Pi Model 1B, introduced in 2012, remained in production as of 2025.

The Raspberry Pi has undergone multiple hardware revisions, with changes in processor type, memory capacity, networking features, and peripheral support. All models include a processor, memory, and various input/output interfaces on a single circuit board. Most include an HDMI output, USB ports, and a GPIO (general-purpose input/output) header. Networking capabilities vary by model, with later versions featuring integrated Wi-Fi and Bluetooth. Storage is typically provided via a microSD card, with newer models supporting USB or PCIe-based boot options.

### Processors and system on chip

Raspberry Pi models use a range of system on a chip (SoC) designs, developed in partnership with Arm and Broadcom. Each generation has introduced improvements in CPU architecture, clock speed, graphics, and overall performance.

The original Raspberry Pi and the Pi Zero use the Broadcom BCM2835, featuring a single-core 32-bit ARM11 CPU and a VideoCore IV GPU. The CPU is clocked at 700 MHz on the original Pi and 1 GHz on the Zero and Zero W.

The Raspberry Pi 2 introduced the BCM2836 with a 900 MHz quad-core 32-bit Cortex-A7 CPU, while later revisions used the 64-bit BCM2837 with Cortex-A53 cores. The Raspberry Pi 3 retained the BCM2837, increasing the CPU clock to 1.2–1.4 GHz depending on the model. The Pi Zero 2 uses the RP3A0, a system in a package (SiP) combining the quad-core Cortex-A53 processor clocked at 1 GHz with 512 MB of RAM.

The Raspberry Pi 4 introduced the BCM2711, a 64-bit SoC with a quad-core Cortex-A72 CPU and VideoCore VI GPU. Clock speeds were initially 1.5 GHz and later increased to 1.8 GHz. The Raspberry Pi 5 uses the BCM2712, featuring a quad-core Cortex-A76 CPU at 2.4 GHz, an 800 MHz VideoCore VII GPU, and a separate RP1 southbridge chip designed in-house.

Raspberry Pi has also developed its own chips outside of its partnership with Broadcom. The Raspberry Pi Pico uses the RP2040, featuring dual-core 32-bit Cortex-M0+ processors running at 133 MHz and 264 kB of on-chip RAM. The Pico 2 uses the RP2350, featuring two Cortex-M33 and two Hazard3 RISC-V CPU cores, any two of which may be selected at boot, running at 150 MHz, with 520 kB of RAM.

#### Overclocking

Most Raspberry Pi models support user-configurable overclocking through the system configuration file. More recent models feature dynamic frequency scaling, adjusting CPU speed based on workload to balance performance and thermal output. This behavior, while similar to overclocking, is part of the default power management system. If the CPU temperature exceeds 85 °C (185 °F) or if undervoltage is detected, performance is throttled automatically. For sustained high-performance workloads, additional cooling—such as a heat sink or fan—may be required.

### RAM

The original Raspberry Pi Model B was equipped with 512 MB of random-access memory (RAM), which, like later models, shares memory between the CPU and GPU. All Raspberry Pi boards support dynamic memory allocation between these components, allowing the system to adjust the division based on workload or user configuration. The original Model A included 256 MB of RAM.

Subsequent models introduced increased memory capacities. The Pi 2B and 3 B/B+ models feature 1 GB of RAM, while the smaller 1A+ and 3A+ models have 512 MB. The Pi Zero and Zero 2 W also include 512 MB. The Pi 4 is available with 1, 2, 3, 4, or 8 GB of RAM, and the Pi 5 expands this further with options for 1, 2, 4, 8, or 16 GB of RAM, the highest capacity offered to date.

On 1 April 2026, Raspberry Pi announced a 3 GB version of the Raspberry Pi 4 due to the increasing cost of LPDDR4 RAM. The PCB was redesigned to use two 1.5 GB chips, which are cheaper and in greater supply.

### Storage and peripherals

Storage is typically provided via a microSD card, though some Compute Modules offer onboard eMMC flash. Newer models support USB booting, and the Pi 5 includes support for NVMe SSDs over PCIe. The original Model A and Model B uses a full-sized SD card slot.

Boards also include USB ports for peripherals such as keyboards, mice, and storage devices.

### Video

Raspberry Pi devices support both digital and analog video output across various resolutions.

Early models featured a full-size HDMI port and an RCA connector for analog composite video output. Later boards removed the RCA jack but retained analog output via the 3.5 mm TRRS jack or dedicated solder points. According to the Raspberry Pi Foundation, analog support helps maintain accessibility in developing countries.

To accommodate the addition of features on the compact boards, video connectors have shrunk across models. The Pi Zero series uses a mini-HDMI connector, while the Pi 4 and 5 use dual micro-HDMI ports. This change enables support for multiple displays: the Pi 4 can drive two 4K displays at 30 Hz or one at 60 Hz, while the Pi 5 improves on this with support for two 4K displays at 60 Hz.

Older Raspberry Pi models support common display resolutions such as 720p and 1080p by default, with some capable of higher resolutions depending on hardware and configuration. In some cases, older hardware can output in 4K, though performance may be poor.

### GPIO header

| Function | Pin # | Function |   |   |
|---|---|---|---|---|
| +3.3 V power | 1 |   | 2 | +5 V power |
| GPIO 2 (I²C SDA) | 3 | 4 | +5 V power |   |
| GPIO 3 (I2C SCL) | 5 | 6 | Ground |   |
| GPIO 4 (GPCLK) | 7 | 8 | GPIO 14 (UART TXD) |   |
| Ground | 9 | 10 | GPIO 15 (UART RXD) |   |
| GPIO 17 | 11 | 12 | GPIO 18 |   |
| GPIO 27 | 13 | 14 | Ground |   |
| GPIO 22 | 15 | 16 | GPIO 23 |   |
| +3.3 V power | 17 | 18 | GPIO 24 |   |
| GPIO 10 (SPI MOSI) | 19 | 20 | Ground |   |
| GPIO 9 (SPI MISO) | 21 | 22 | GPIO 25 |   |
| GPIO 11 (SPI SCLK) | 23 | 24 | GPIO 8 (SPI CE0) |   |
| Ground | 25 | 26 | GPIO 7 (SPI CE1) |   |
| GPIO 0 (EEPROM SDA) | 27 | 28 | GPIO 1 (EEPROM SDC) |   |
| GPIO 5 | 29 | 30 | Ground |   |
| GPIO 6 | 31 | 32 | GPIO 12 |   |
| GPIO 13 | 33 | 34 | Ground |   |
| GPIO 19 | 35 | 36 | GPIO 16 |   |
| GPIO 26 | 37 | 38 | GPIO 20 (PCM_DIN) |   |
| Ground | 39 | 40 | GPIO 21 (PCM_DOUT) |   |
| **Legend**  SPI   GPIO   I²C   UART   PCM   Ground   +5 V   +3.3 V |   |   |   |   |

Most Raspberry Pi models include a 40-pin connector known as the GPIO (general-purpose input/output) header, although only some of the pins are dedicated to GPIO functions. The header, designated as J8, uses a consistent pinout across models.

The header supplies 3.3 V and 5 V power along with various multiplexed, low-speed interfaces, including UART, SPI, I²C, I²S, and PCM. GPIO pins can be configured as either inputs or outputs. When set as an output, a pin can drive a high (3.3 V) or low (0 V) signal. When configured as an input, it can read a high (3.3 V) or low (0 V) voltage level.

The original Raspberry Pi 1 Model A and B include only the first 26 pins of this header. On some Pi Zero models, the header is unpopulated, but solderable through-holes are provided. The Pico models feature a unique layout with unpopulated through-holes and a castellated edge, allowing it to be surface-mounted as a module. Compute Module boards do not include GPIO headers but instead expose GPIO signals through their board connectors.

### Networking

Networking capabilities differ by model. The Model B and B+ include an Ethernet port. Starting with the Raspberry Pi 3, most models come with built-in WiFi and Bluetooth. The Raspberry Pi 3B+ adds faster Ethernet and dual-band WiFi. The Raspberry Pi 4 and 5 offer full gigabit Ethernet. The "A" models and the Pi Zero series do not have Ethernet ports, and built-in wireless support is optional. A USB adapter may be used for wired or wireless connections. Headless Raspberry Pi configurations may experience intermittent network connectivity issues, often attributed to default WiFi power management settings. These issues are typically addressable through configuration changes.

### Special-purpose features

Some Raspberry Pi models, like the Zero, 1A, 3A+, and 4, can act like a USB device (via the USB On-The-Go protocol) when plugged into another computer. This lets them work as gadgets such as a virtual keyboard, network adapter, or serial device.

Many newer models can also start up (or "boot") directly from a USB drive, without needing a microSD card. This feature is not available on older models like the original Raspberry Pi, Pi Zero, or early versions of the Pi 2.

### Real-time clock

Most Raspberry Pi models do not include a built-in real-time clock, which means they rely on an internet connection to set the correct time with the Network Time Protocol when they start up. If there is no connection, the time must be set manually; otherwise, the system assumes no time has passed since it was last used. Add-on clock modules are available for situations where accurate timekeeping is needed without internet access. The Raspberry Pi 5 is the first model to include a built-in clock which uses a battery to keep time when powered off.

### Board layouts

- (Zero 2w layout) Zero 2w layout
- (Pi 1A) Pi 1A
- (Pi 1A+ v1.1) Pi 1A+ v1.1
- (Pi 1B v1.2) Pi 1B v1.2
- (Pi 1B+ v1.2 and Pi 2) Pi 1B+ v1.2 and Pi 2
- (Pi 3) Pi 3
- (Pi 3+) Pi 3+
- (Pi 4) Pi 4
- (Pi 5) Pi 5


## Specifications

Version

Pico 1

Pico 2

1A

1A+

3A+

1B

1B+

2B

2B v1.2

3B

3B+

4

5

CM1

CM3

CM4

CM5

Zero

Zero 2

400

Release date

Jan 2021

W: Jun 2022

Aug 2024

Feb 2013

Nov 2014

Nov 2018

Apr–Jun 2012

Jul 2014

Feb 2015

Oct 2016

Feb 2016

Mar 2018

Jun 2019

Oct 2023

Apr 2014

Jan 2017

Oct 2020

Nov 2024

Nov 2015

Oct 2021

Nov 2020

Target price (USD)

US$4

W:

US$6

US$5

W:

US$7

$25

$20

$25

$35

$25

$35

$35‍–‍75

$50‍–‍120

$25‍–‍40

$30–85

$45

US$5

W:

US$10

$15

$70

Instruction set

ARMv6

(32‑bit)

ARMv8-M

(64/32‑bit) or

RV32IMAC

(32‑bit)

ARMv6

(32‑bit)

ARMv8-A

(64/32‑bit)

ARMv6

(32‑bit)

ARMv7-A

(32‑bit)

ARMv8-A

(64/32‑bit)

ARMv6

(32‑bit)

ARMv8-A

(64/32‑bit)

ARMv8-A (64/32-bit)

ARMv6

(32‑bit)

ARMv8-A

(64/32‑bit)

ARMv8-A

(64/32‑bit)

Fabrication node

40 nm

40 nm

40 nm

40 nm

40 nm

40 nm

40 nm

28 nm

16 nm

40 nm

40 nm

28 nm

16 nm

40 nm

28 nm

SoC

RP2040

RP2350

A

BCM2835

BCM2837

BCM2835

BCM2836

BCM2837

BCM2837

BCM2711

BCM2712

BCM2835

BCM2837

BCM2711

BCM2712

BCM2835

BCM2710

BCM2711

FPU

Software emulation

FPv5 (ARM only)

VFPv2

VFPv4 + NEON

VFPv2

VFPv4 + NEON

VFPv2

VFPv4 + NEON

VFPv2

VFPv4 + NEON

VFPv4 + NEON

CPU

2× Arm Cortex-M0+

2× CPU cores, independently selectable as

Arm Cortex-M33

or Hazard3

RISC-V

at boot

1×

ARM11

@ 700 MHz

4×

Cortex-A53

@ 1.4 GHz

1×

ARM11

@ 700 MHz

4×

Cortex-A7

900 MHz

4×

Cortex-A53

@ 900 MHz

4×

Cortex-A53

@ 1.2 GHz

4×

Cortex-A53

@ 1.4 GHz

4×

Cortex-A72

@ 1.5 GHz or 1.8 GHz

4×

Cortex-A76

@ 2.4 GHz

1×

ARM11

@ 700 MHz

4×

Cortex-A53

@ 1.2 GHz

4×

Cortex-A72

@ 1.5 GHz

4×

Cortex-A76

@ 2.4 GHz

1×

ARM11

@ 1 GHz

4×

Cortex-A53

@ 1 GHz

4×

Cortex-A72

@ 1.8 GHz

GPU

—

N/a

VideoCore

IV @ 250 MHz

VideoCore IV @ 400 MHz (Core) / 300 MHz (V3D)

VideoCore VI @ 500 MHz

VideoCore VII @ 800 MHz

VideoCore IV @ 250 MHz

VideoCore VI @ 500 MHz

VideoCore VII

VideoCore IV @ 400 MHz (Core) / 300 MHz (V3D)

VideoCore VI @ 500 MHz

Memory (SDRAM)

264 KB

520 KB

256 MiB

256 or 512 MiB

Changed to 512 MB on 10 August 2016

512 MiB

256 or 512 MiB

Changed to 512 MB on 15 October 2012

512 MiB

1 GiB

1, 2, 3,

4 or 8 GiB

2, 4, 8 or 16 GiB

512 MB

1 GiB

1, 2, 4 or 8 GiB

2, 4, 8, or 16 GiB

512 MiB

4 GiB

USB 2.0 ports

—

N/a

1

1

2

4

2

1

1

1

1

1 Micro-USB

1

USB 3.0 ports

—

N/a

2

—

N/a

2

USB OTG ports

—

N/a

1 (Power

USB-C

)

1 (Power

USB-C

)

—

N/a

?

1 Micro-USB

—

N/a

PCIe interface

—

N/a

PCIe

Gen 2 x1

—

N/a

PCIe Gen 2 x1

—

N/a

—

N/a

—

N/a

Video input

15-pin

MIPI

camera interface

(

CSI

) connector, used with the Raspberry Pi camera or Raspberry Pi NoIR camera

2× 22-pin mini-MIPI display/camera interface (DSI/CSI)

2× MIPI camera interface (CSI)

2-lane MIPI CSI camera interface, 4-lane MIPI CSI camera interface

2× 4-lane MIPI camera

v1.3 & W: MIPI camera interface (CSI)

MIPI camera interface (CSI)

—

N/a

HDMI

1×

HDMI

(rev 1.3)

2×

HDMI

(rev 2.0) via Micro-HDMI

2× HDMI (rev?)

1× HDMI

2× HDMI

1× Mini-HDMI

2×

HDMI

(rev 2.0) via Micro-HDMI

Composite video

via

RCA jack

via 3.5 mm CTIA-style

TRRS jack

via

RCA jack

via 3.5 mm CTIA style

TRRS jack

pair of 0.1"-spaced pads

Yes

?

via marked points on PCB for optional header pins

?

MIPI display interface (

DSI

)

1× standard size (15-pin, 1 mm pitch), for a display only

2× mini

(22-pin, 0.5 mm pitch), each for a display or camera

Yes

Yes

No

?

Audio inputs

As of revision 2 boards via

I²S

?

Audio outputs

Analog via

3.5 mm phone jack

; digital via HDMI and, as of revision 2 boards,

I²S

HDMI

Analog, HDMI,

I²S

Mini-HDMI, stereo audio through PWM on GPIO

Micro-HDMI

On-board storage

—

N/a

4 MB internal flash

SD

,

MMC

, SDIO card slot (3.3

V

with card power only)

MicroSDHC

slot

SD

,

MMC

, SDIO card slot

MicroSDHC

slot

MicroSDHC

slot, USB Boot Mode

MicroSDXC

MicroSDXC

UHS-1

Slot

4 GB

eMMC

(optional)

8/16/32 GB

eMMC

(optional)

16/32/64GB eMMC (optional)

MicroSDHC

slot

MicroSDHC

slot

Ethernet

(Max.

Mbit/s

)

—

N/a

100

300

1000

—

N/a

1000

—

N/a

1000

WiFi

2.4 GHz 802.11n (optional, W model)

2.4 GHz 802.11n (optional, W model)

—

N/a

2.4/5 GHz 802.11b/g/n/ac

—

N/a

2.4 GHz 802.11b/g/n

2.4/5 GHz 802.11b/g/n/ac

2.4/5 GHz 802.11b/g/n/ac(optional)

2.4 GHz 802.11b/g/n (optional, W model)

2.4/5 GHz 802.11b/g/n/ac

Bluetooth

5.2 (optional, W model)

5.2 (optional, W model)

4.2, BLE

4.1, BLE

4.2, LS BLE

5.0, BLE

4.2, BLE (optional, W model)

5.0

Low-level peripherals

UART

8×

GPIO

plus the following, which can also be used as GPIO:

UART

,

I²C

bus,

SPI

bus with two

chip selects

,

I²S

audio

+3.3 V, +5 V, ground

17×

GPIO

plus the same specific functions, and HAT ID bus

8×

GPIO

plus the following, which can also be used as GPIO:

UART

,

I²C

bus,

SPI

bus with two

chip selects

,

I²S

audio +3.3 V, +5 V, ground.

17×

GPIO

plus the same specific functions, and HAT ID bus

17×

GPIO

plus the same specific functions, HAT, and an additional 4× UART, 4× SPI, and 4× I2C connectors.

46×

GPIO

, some of which can be used for specific functions including

I²C

,

SPI

,

UART

,

PCM

,

PWM

28× GPIO supporting either 1.8v or 3.3v signalling and peripheral options

17× GPIO plus the same specific functions, and HAT ID bus

?

Power ratings

?

?

300 mA (1.5 W)

200 mA (1 W)

?

700 mA (3.5 W)

200 mA (1 W) average when idle, 350 mA (1.75 W) maximum under stress (monitor, keyboard and mouse connected)

220 mA (1.1 W) average when idle, 820 mA (4.1 W) maximum under stress (monitor, keyboard and mouse connected)

300 mA (1.5 W) average when idle, 1.34 A (6.7 W) maximum under stress (monitor, keyboard, mouse and WiFi connected)

459 mA (2.295 W) average when idle, 1.13 A (5.661 W) maximum under stress (monitor, keyboard, mouse and WiFi connected)

600 mA (3 W) average when idle, 1.25 A (6.25 W) maximum under stress (monitor, keyboard, mouse and Ethernet connected),

1.6 A (8 W) for "power virus" workloads 3 A (15 W) power supply recommended.

12 W for "

power virus

" workloads

200 mA (1 W)

700 mA (3.5 W)

?

100 mA (0.5 W) average when idle, 350 mA (1.75 W) maximum under stress (monitor, keyboard and mouse connected)

120 mA (0.6 W) average when idle

?

Power source

MicroUSB or GPIO Header 1.8 V to 5 V

5 V via

MicroUSB

or GPIO header

5 V via

MicroUSB

, GPIO header, or

PoE

(with the PoE HAT)

5 V via

USB-C

, GPIO header, or

PoE

(with the PoE HAT)

2.5–5 V, 3.3 V, 2.5–3.3 V, and 1.8 V

5 V

5 V via

MicroUSB

or GPIO header

5 V via USB-C

Size

51 × 21 mm (2.01 × 0.83 in)

85.6 × 56.5 mm (3.37 × 2.22 in)

65 × 56.5 × 10 mm (2.56 × 2.22 × 0.39 in)

65 × 56.5 mm (2.56 × 2.22 in)

85.60 × 56.5 mm (3.370 × 2.224 in)

85.60 × 56.5 × 17 mm (3.370 × 2.224 × 0.669 in)

85 × 56 mm (3.3 × 2.2 in)

67.6 × 30 mm (2.66 × 1.18 in)

67.6 × 31 mm (2.66 × 1.22 in)

55 × 40 mm (2.2 × 1.6 in)

65 × 30 × 5 mm (2.56 × 1.18 × 0.20 in)

286 × 113 × 23 mm (11.26 × 4.45 × 0.91 in)

Weight

?

?

31 g (1.1 oz)

23 g (0.81 oz)

45 g (1.6 oz)

46 g (1.6 oz)

7 g (0.25 oz)

9 g (0.32 oz)

10.8 g (0.38 oz)

Production lifetime

2028

W: 2036

2040

?

2030

2030

?

2030

2026

2028

2030

2034

2036

2026

CM3: 2026

CM3+: 2028

2034

2036

2030

2030

2030

2028

1. BCM2837: 3D part of GPU at 300 MHz, video part of GPU at 400 MHz, OpenGL ES 2.0 (BCM2835, BCM2836: 24 GFLOPS / BCM2837: 28.8 GFLOPS). MPEG-2 and VC-1 (with licence), 1080p30 H.264/MPEG-4 AVC high-profile decoder and encoder (BCM2837: 1080p60)
2. Shared with GPU
3. Direct from the BCM2835 chip
4. Direct from the BCM2837B0 chip
5. via on-board 3-port USB hub; one USB port internally connected to the Ethernet port.
6. via on-board 5-port USB hub; one USB port internally connected to the Ethernet port.
7. 200-pin DDR2 SO-DIMM interface until CM3+
8. for raw LCD panels
9. Excluding protruding connectors
10. Same as HAT board


## Software

### Operating systems

The recommended operating system is Raspberry Pi OS, a Debian-based Linux distribution optimized for Raspberry Pi hardware and tuned to have low base memory requirements. It is available in both 32-bit and 64-bit versions and comes in several editions: a standard edition, a "Lite" version without a desktop environment, and a "Full" version that includes a comprehensive suite of software.

Raspberry Pi OS can be purchased pre-installed on a microSD card, or downloaded and installed using Raspberry Pi Imager, a utility introduced in March 2020 to simplify the installation of operating systems onto SD cards and other media for Raspberry Pi devices. Available for macOS, Raspberry Pi OS, Ubuntu, and Windows, Imager allows users to download and write operating system disk images within a single application. In addition to Raspberry Pi OS, the utility supports a variety of third-party operating systems, including Alpine Linux, Arch Linux ARM, Armbian, Emteria.OS (Android based), FreedomBox, Kali Linux, LibreELEC, RetroPie, RISC OS, SatNOGS, Ubuntu, and Arm versions of Windows 10 IoT Core and version 11.

### Firmware

The Raspberry Pi uses official firmware that is proprietary, meaning its source code is not publicly available, but the binary blob can be freely redistributed. An experimental open-source alternative to the official firmware is also available. Although limited in functionality, it demonstrates that it is possible to start the Raspberry Pi's ARM processor cores and boot a basic version of the Linux kernel without relying on the proprietary components. This is significant for developers and advocates who aim to build fully open systems.

### Driver APIs

Raspberry Pi systems use Broadcom's VideoCore GPU, which requires a proprietary firmware binary blob to be loaded at boot. Initially, the supporting software stack was entirely proprietary, though parts of the code were later released. Most driver functionality remains within the proprietary GPU firmware, accessed via closed-source runtime libraries such as OpenMAX IL, OpenGL ES, and OpenVG. These libraries interface with a kernel-space open-source driver, which in turn communicates with the proprietary GPU firmware. Applications use OpenMAX IL for video, OpenGL ES for 3D graphics, and OpenVG for 2D graphics, with all graphics libraries making use of the closed-source EGL interface.

In February 2020, Raspberry Pi announced the development of a Vulkan graphics driver. A working prototype demonstrated high performance in Quake III Arena on a Raspberry Pi 3B+ later that year. On 24 November 2020, Raspberry Pi 4's Vulkan driver was declared conformant.


## Official accessories

### Cameras

Raspberry Pi offers several official camera modules that connect via the Camera Serial Interface. These modules are used for photography, video capture, and machine vision applications.

- **Camera Module** (2013) – A 5-megapixel (MP) camera based on the OmniVision OV5647 sensor, supporting video resolutions up to 1080p. A version without an infrared filter (NoIR) was available for night-vision applications when used with infrared lighting. This model is no longer produced.
- **Camera Module 2** (2016) – 8 MP Sony IMX219 sensor. Also available in NoIR version.
- **High Quality Camera** (2020) – 12.3 MP Sony IMX477 sensor. Supports interchangeable C/CS mount or M12 mount lenses and includes a tripod thread. Not available in a NoIR version, but IR filter can be removed.
- **Camera Module 3** (2023) – 12 MP Sony IMX708 sensor with support for autofocus and high dynamic range. Offered in four variants: standard, wide field of view (FoV), NoIR, and NoIR wide FoV.
- **Global Shutter Camera** (2023) – 1.6 MP Sony IMX296 sensor with global shutter for high-speed imaging. Supports C/CS mount lenses and includes a tripod mount. Not available in a NoIR version, but IR filter can be removed.
- **AI Camera** (2024) – 12.3 MP Sony IMX500 sensor with integrated on-sensor processing capabilities for AI applications.

### Displays

Raspberry Pi also offers official display peripherals for graphical and touchscreen interfaces:

- **Raspberry Pi Touch Display** (2015) – A 7-inch capacitive touchscreen.
- **Raspberry Pi Touch Display 2** (2024) – A revised version of the original 7-inch touchscreen display with improved performance and compatibility. Also available in an 5-inch version since 2025.
- **Raspberry Pi Monitor** (2024) – A 15.6-inch Full HD IPS display with built-in speakers and folding stand.

### Add-on boards (HATs)

Official Raspberry Pi HATs (Hardware Attached on Top) and expansion boards extend the functionality of Raspberry Pi computers. The HAT standard was introduced in July 2014. Many boards use an EEPROM for automatic configuration.

- **AI HAT+** (2024) – A HAT for the Raspberry Pi 5 featuring a built-in Hailo-8L chip providing 13 TOPS of AI acceleration, or Hailo-8 chip providing 26 TOPS.
- **AI HAT+ 2** (2026) – A HAT for the Raspberry Pi 5 featuring a built-in Hailo-10H chip providing 40 TOPS of AI acceleration, along with 8 GB of dedicated on-board RAM.
- **Build HAT** (2021) – Designed to interface with Lego Technic motors and sensors.
- **Codec Zero** – A compact audio input/output board for the Pi Zero.
- **DAC+ / DAC Pro / DigiAMP+** – A range of audio HATs offering high-resolution digital-to-analog conversion, with the DigiAMP+ including a built-in amplifier.
- **M.2 HAT+** (2024) – A HAT for the Raspberry Pi 5 featuring an interface for attaching M.2 peripherals.
  - **AI Kit** (2024) – A bundle including the M.2 HAT+ and a Hailo AI-8L module providing 13 TOPS of AI acceleration.
  - **SSD Kit** (2024) – A bundle including the M.2 HAT+ and a NVMe SSD.
- **Sense HAT** (2015) – Includes sensors for temperature, humidity, pressure, orientation, and an 8×8 LED matrix with a joystick. Originally developed for the Astro Pi project.
- **PoE+ HAT** (2021) – Enables Power over Ethernet functionality for models with PoE support.
- **TV HAT** (2018) – Allows reception and decoding of digital DVB-T2 television broadcasts.

#### Power supplies

- **Build HAT Power Supply** – A 48 W power supply providing 8 V at up to 6 A, designed for use with the Build HAT. It provides sufficient power for connected Lego Technic motors and sensors, as well as the attached Raspberry Pi computer.
- **PoE+ Injector** (2018) – Provides Power over Ethernet (up to 30W) for compatible models using a PoE HAT.
- **USB Power Supplies** – Available in multiple versions delivering 5.1V at different power levels: 12.5W via Micro-USB for earlier models, 15W via USB-C for Pi 4, 27W via USB-C for Pi 5, and 45W via USB-C for third-party laptops.

#### Peripherals

- **Active cooler** (2023) – A heatsink and temperature‑controlled fan for thermal management on Pi 5.
- **Cables and adapters** – Includes HDMI (micro for Pi 4/5, mini for Zero), USB (micro‑USB and USB‑C), and various adapters for display and peripheral connectivity.
- **Cases** – Plastic enclosures for Raspberry Pi A+, 3, 4, 5, and Zero series with venting, and in some cases, fans, to aid heat dissipation. A minimalist "bumper" silicone enclosure is also offered for the Pi 5.
- **Keyboard and mouse** – Official USB keyboard (with integrated hub with three USB 2 Type-A ports) and optical mouse designed for use with Raspberry Pi.
- **SD cards** – Officially tested microSD cards that support A2 application performance, C10 card speeds, and UHS-I (SDR104) bus speeds. Available with Raspberry Pi OS pre-installed.
- **Smart Display Module** – Compute Module adapter board that allows it to be embedded into professional signage displays that use the Intel Smart Display Module standard. Includes HDMI output for a second independent video stream, along with an M.2 expansion slot for an optional Hailo AI accelerator.
- **USB 3 hub** – Adds four additional USB 3 Type-A ports, also includes a USB-C power input to support high power draw peripherals.

#### Debugging and utility

- **Debug probe** (2022) – RP2040-based hardware debug tool for Raspberry Pi and RP2040 development boards.
- **RTC battery** (2024) – Rechargeable lithium battery for powering the real-time clock on Raspberry Pi 5 during power loss.
