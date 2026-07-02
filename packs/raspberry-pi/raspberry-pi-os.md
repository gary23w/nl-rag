---
title: "Raspberry Pi OS"
source: https://en.wikipedia.org/wiki/Raspberry_Pi_OS
domain: raspberry-pi
license: CC-BY-SA-4.0
tags: raspberry pi, raspberry pi os, raspbian, pi pico, rp2040
fetched: 2026-07-02
---

# Raspberry Pi OS

**Raspberry Pi OS** is a Unix-like operating system developed for the Raspberry Pi line of single-board computers. Based on Debian, a Linux distribution, it is maintained by Raspberry Pi Holdings and optimized for the Pi's hardware, with low memory requirements and support for both 32-bit and 64-bit architectures. Originally released in July 2012 under the name **Raspbian**, it was introduced shortly after the launch of the first Raspberry Pi model.

The operating system is compatible with all Raspberry Pi models except the Raspberry Pi Pico microcontroller. It is available in several configurations: a standard edition, a "Lite" version without a desktop environment, and a "Full" version that includes additional software such as LibreOffice and Wolfram Mathematica. The operating system is available as a free download and can be installed using the official Raspberry Pi Imager utility. It is also sold preloaded on official microSD cards.

## History

Raspbian was first developed by Mike Thompson and Peter Green as an independent and unofficial port of Debian to the Raspberry Pi. The first build was released on 15 July 2012. As the Raspberry Pi had no officially provided operating system at the time, the Raspberry Pi Foundation built on the work by the Raspbian project and began producing and releasing their own operating system images of the software. The Foundation's first release of Raspbian, which now referred both to the community project as well as the official operating system, was announced on 10 September 2013.

On 28 May 2020, the Raspberry Pi Foundation announced a beta 64-bit version. However, this version was not based on Raspbian, instead taking its user space software from Debian. When the Foundation did not want to use the name Raspbian to refer to software that was not based on the Raspbian project, the name of the officially provided operating system images was changed to Raspberry Pi OS. This change was also carried over to the 32-bit images that they distributed, though it continued to be based on Raspbian. The 64-bit version of Raspberry Pi OS was officially released on 2 February 2022.

## Features

### User interface

The Raspberry Pi OS user interface is optimized for Raspberry Pi hardware and tuned to have low base memory requirements, aiming to deliver a lightweight, fast, and energy-efficient desktop experience. It is built on the Wayland display protocol, using labwc as its compositing manager, which is based on wlroots, a modular Wayland implementation that underpins several other compositors.

The operating system previously used the X Window System. A transition to Wayland began with the Bullseye release in 2021, which introduced the mutter window manager to support both X and Wayland environments. In the Bookworm release of 2023, wayfire was adopted as a dedicated Wayland compositor. However, performance issues on older Raspberry Pi models prompted a search for a more suitable alternative. In 2024, developers ultimately selected labwc, a lightweight compositor that better matched the hardware's capabilities. Following collaboration and extensive optimization, labwc now offers performance comparable to X across all models, and Raspberry Pi OS now defaults to Wayland.

The interface is designed to feel familiar to users of macOS and Microsoft Windows. It provides a traditional desktop environment with a top menu bar that includes an application menu, shortcuts to frequently used programs, and system controls such as Bluetooth, Wi-Fi, volume, and clock.

### Other components

Raspberry Pi OS originally included the Epiphany web browser, but transitioned to Chromium in 2016. Firefox was added as an additional pre-installed browser option in 2023. The included browsers come with uBlock, an ad-blocking extension, and h264ify, an extension that makes YouTube serve videos using the H.264 codec which is supported by the Raspberry Pi's hardware acceleration. As of May 2025, other pre-installed applications includes Geany, ImageMagick, Thonny, VNC Viewer and VLC media player.

As of May 2025, installations with the full suite of recommended software includes Claws Mail, Firebird database server, KiCad, LibreOffice, Java, Scratch, and Wolfram Mathematica, and additional font packages.

Software can be installed via the APT (Advanced Package Tool) command-line interface, or through graphical front-ends such as the included Add/Remove Software tool, or by using third-party app stores like Pi-Apps.

## Reception

According to Raspberry Pi Imager usage statistics, Raspberry Pi OS accounted for 67% of all operating system downloads for the Raspberry Pi in May 2025, followed by Ubuntu at 9%.

In a 2015 review, Jesse Smith of *DistroWatch* found that while Raspbian was not well-suited for heavier desktop workloads, it provided a functional experience with its lightweight environment. He noted that the system was responsive when running a modest number of applications, but struggled with more resource-intensive software such as LibreOffice or Firefox.

In a January 2024 review for *Ars Technica*, Andrew Cunningham tested Raspberry Pi OS version 5 on a Pi 5 with 8 GB of RAM and found it functional for general-purpose desktop use, but with notable limitations. While it handled basic tasks like writing, web browsing, and audio editing well, the OS lacked modern conveniences such as window snapping, a notification center, refined window borders, and smooth multi-monitor performance. Its software ecosystem was also constrained by limited native app availability for ARM Linux, often requiring users to rely on web-based versions of services like Slack, Zoom, and Dropbox.

### Microsoft repository controversy

In January 2021, the Raspberry Pi OS package `raspberrypi-sys-mods` added a Microsoft GPG encryption key and repository configuration to the APT package manager, enabling easier installation of Visual Studio Code, a source code editor. As a result, the system contacted Microsoft's servers during update checks, prompting concerns among users due to privacy considerations and Microsoft's once-adversarial history with the open source software community. The repository configuration was later removed.

## Versions

Raspberry Pi OS is available in three main variants:

- **Raspberry Pi OS Lite** – a minimal version without a desktop environment
- **Raspberry Pi OS with desktop** – includes the desktop environment and a limited number of pre-installed applications
- **Raspberry Pi OS with desktop and recommended software** – includes the desktop environment and the full suite of recommended pre-installed applications

Each variant is available in both 32-bit and 64-bit versions.

A "legacy" branch has been available since December 2021. It is based on the previous stable release of Debian, allowing for continued use of older software while still receiving security and hardware support updates. All standard variants (Lite, with desktop, and with desktop and recommended software) are offered in this legacy form.

New major versions of Debian are released every two years, typically in the summer of odd-numbered years (e.g., 2023, 2025, 2027). Raspberry Pi OS ports of each new Debian release generally follow a few months later, usually in the fall.

Raspberry Pi OS can be purchased pre-installed on a microSD card or downloaded as a `.img` disk image file to be written to an SD card or other media. Official documentation recommends a minimum of 16 GB for the Lite version and at least 32 GB for versions with a desktop environment.

The **Raspberry Pi Imager** utility was introduced in March 2020 to simplify the installation of a disk image file onto an SD card or other media. Available for macOS, Raspberry Pi OS, Ubuntu, and Windows, it allows users to download and write the disk image file in a single application. In addition to Raspberry Pi OS, the utility supports a variety of third-party operating systems.

## Releases

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

Version

Release date

Debian version

Linux kernel

GCC

APT

User interface

1

2

3

Zero

3+

4

Zero 2

5

Unsupported:

0

2013-09-27

7

(Wheezy)

3.6

4.7.2

0.9.7

X.Org Server

1

2013-10-07

2013-12-24

3.10

2014-01-09

2014-06-22

3.12

2014-07-08

2014-09-12

2014-10-08

2014-12-25

2015-02-02

3.18

2015-02-17

2015-02-18

2015-05-07

2015-05-12

Unsupported:

1

2015-09-28

8

(Jessie)

4.1

4.9

1.0.9.8.1

2015-11-24

2016-02-08

2016-02-09

2016-02-29

2016-03-18

2016-05-13

4.4

2016-05-31

2016-09-28

2016-11-29

2017-02-27

4.9

2017-03-03

2017-04-10

2017-06-23

2017-07-05

Unsupported:

2

2017-08-17

9

(Stretch)

6.3

1.4.6

2017-09-08

2017-11-29

2018-03-13

2018-04-18

4.14

1.4.8

2018-06-29

2018-10-09

2018-11-13

2019-04-08

1.4.9

Unsupported:

3

2019-06-24

10

(Buster)

4.19

8.3

1.8.2

2019-07-10

2019-09-30

2020-02-07

2020-02-14

2020-05-27

2020-08-20

5.4

2020-12-02

1.8.2.1

2021-01-11

1.8.2.2

2021-03-04

5.10

2021-05-07

1.8.2.3

2021-10-30

Unsupported:

4

2021-12-03

11

(Bullseye)

5.10

10.2.1

2.2.4

X.Org Server 1.20

2022-01-28

2022-03-08

2022-04-04

5.15

2022-09-06

2022-09-22

2023-02-21

2023-05-03

6.1

2023-12-05

2024-03-12

2024-07-04

2024-10-22

2025-05-06

Unsupported:

5.0

2023-10-10

12

(Bookworm)

6.1

12.2.0

2.6.1

X.Org Server 21.1

Unsupported:

5.1

2023-12-05

Unsupported:

5.2

2024-03-15

6.6

Unsupported:

5.3

2024-05-29

Unsupported:

5.4

2024-07-04

Unsupported:

5.5

2024-11-19

labwc 0.7.2

Unsupported:

5.6

2025-05-06

6.12

labwc 0.8.1

Unsupported:

5.7

2025-10-01

Unsupported:

5.8

2025-11-24

Unsupported:

5.9

2026-04-14

Supported:

5.10

2026-06-18

Unsupported:

6.0

2025-10-01

13

(Trixie)

6.12

14.2.0

3.0.3

labwc 0.8.4

Unsupported:

6.1

2025-11-24

labwc 0.9.2

Unsupported:

6.2

2026-04-14

Latest version:

6.3

2026-06-18

6.18

labwc 0.9.7
