---
title: "Ubuntu version history (part 3/3)"
source: https://en.wikipedia.org/wiki/Ubuntu_version_history
domain: ubuntu-linux
license: CC-BY-SA-4.0
tags: ubuntu linux, canonical company, ubuntu release, long-term support
fetched: 2026-07-02
part: 3/3
---

### Ubuntu 16.04 LTS (Xenial Xerus)

Shuttleworth announced on 21 October 2015 that Ubuntu 16.04 LTS would be called *Xenial Xerus* and include an option for Unity 8. It was released on 21 April 2016. In September 2021, Canonical announced that it would extend LTS support for the 14.04 and 16.04 to a total of 10 years, extending the ESM support date for 16.04 until April 2026. The release adds support for Ceph and ZFS filesystems, the LXD hypervisor for OpenStack, and Snap packages.

This release has online Dash search results disabled by default in Unity 7, does not support the AMD Catalyst (fglrx) driver for AMD/ATI graphics cards, and instead recommends the Radeon and AMDGPU alternatives. It also replaced the Ubuntu Software Center with GNOME Software (rebranded as "Ubuntu Software") and eliminated Empathy and Brasero from the ISO file.

### Ubuntu 16.10 (Yakkety Yak)

Mark Shuttleworth announced on 21 April 2016 that Ubuntu 16.10 would be called *Yakkety Yak*. It was released on 13 October 2016. This release includes a faster version of Ubuntu Software, better support for installing command-line-only applications, support for installing fonts and multimedia codecs, paid applications, changelog entries for Personal Package Archives (PPAs) in the Update Manager, user session handling by systemd, and Linux kernel 4.8.

### Ubuntu 17.04 (Zesty Zapus)

On 17 October 2016, Mark Shuttleworth announced that the codename of Ubuntu 17.04, released on 13 April 2017, would be *Zesty Zapus*. This release dropped support for the 32-bit PowerPC architecture, following the same move by the upstream Debian project. Other changes include the default DNS resolver now being *systemd-resolved*, Linux kernel 4.10, and included support for printers. Reviewers noted that this was likely to be the last version of Ubuntu to ship with Unity 7 by default before Ubuntu's switch to GNOME, matching the end of the alphabet in Ubuntu's codename scheme.

### Ubuntu 17.10 (Artful Aardvark)

Artful Aardvark was announced via Launchpad on 21 April 2017 instead of on Shuttleworth's blog as had been the case in the past. It was released on 19 October 2017. Critics praised the smooth transition to GNOME and the significance of the release's changes.

This is the first release of Ubuntu to use the GNOME Shell interface, and the first release to replace X11 with the Wayland display server. In May 2017, Ken VanDine, a Canonical Software Engineer on the Ubuntu desktop team tasked with the switch to GNOME, confirmed that the intention is to ship the most current version of GNOME, with very few changes from a stock installation. This release also dropped 32-bit desktop images; other images' 32-bit versions remain.

### Ubuntu 18.04 LTS (Bionic Beaver)

Ubuntu 18.04 LTS Bionic Beaver, the seventh LTS release, is a long-term support version that was announced on 24 October 2017 on Shuttleworth's blog and released on 26 April 2018. Ubuntu 18.04 LTS had normal LTS support for five years until May 2023 and has paid ESM support available from Canonical for an additional five years until April 2028. New features include colour emoji, a new To-Do application preinstalled in the default installation, the "Minimal Install" option in the system installer, which only installs a web browser and system tools, and new command-line system installer for Ubuntu Server. This release employed Linux kernel 4.15, which incorporated a CPU controller for the cgroup v2 interface, AMD secure memory encryption support and improved SATA Link Power Management.

Ubuntu 18.04 LTS's default display server was returned to Xorg for more stability; Wayland was still included as part of the default install. For the first time some bundled applications were delivered by default as snaps.

Plans to include a new theme, *Communitheme* (now *Yaru*), created by the Ubuntu community, were announced on 5 February 2018. However, Ubuntu 18.04 LTS did not include it, citing "outstanding bugs, a lack of broader testing, as well as ongoing gaps in corner-case usage." The new theme was available as a Snap package instead.

### Ubuntu 18.10 (Cosmic Cuttlefish)

Shuttleworth announced Ubuntu 18.10 *Cosmic Cuttlefish* on 8 May 2018. It was released on 18 October 2018. Installation speeds are faster due to the use of a lossless compression algorithm known as Zstandard. Startup speeds of pre-installed Snap applications were also improved.

Ubuntu 18.10 includes a new theme, *Yaru*, as the default theme, along with its accompanying icon theme, *Suru*.

### Ubuntu 19.04 (Disco Dingo)

Shuttleworth announced Ubuntu 19.04 *Disco Dingo* on 20 October 2018. It was released on 18 April 2019. It incorporates Linux kernel 5.0, which adds support for AMD FreeSync technology for liquid-crystal displays, Raspberry Pi touchscreens, Adiantum encryption, Btrfs swap files as well as many USB 3.2 and Type-C improvements and several other new hardware. It uses GNOME 3.32, which includes a new icon set, night light intensity control, advanced application permissions, favoriting files, and a new header bar as well as 'find' and 'read only' modes in the default terminal emulator. Version 19 of the open-source graphics drivers Mesa is natively available in this version of Ubuntu. Furthermore, the Grub menu now allows a 'safe graphics' mode in case of issues with graphics cards or graphics drivers. Geoclue integration and fractional scaling in the GNOME Shell for HiDPI displays are also included. Improvements for running Ubuntu on a VMWare virtual machine include integration of open-vm-tools within Ubuntu, allowing for bi-directional clipboard and file sharing.

Ubuntu Server 19.04 updated QEMU to version 3.1, allowing for creation of a virtual 3D GPU inside QEMU virtual machines. libvirt was updated to version 5.0 and Samba was updated to version 4.10.x. Samba and its dependencies were updated to Python 3, with the exception of tdb, which still builds a Python 2 package, namely *python-tdb*. Ubuntu Server 19.04 includes the latest OpenStack release, Stein, and has vSwitch version 2.11.

### Ubuntu 19.10 (Eoan Ermine)

Shuttleworth announced Ubuntu 19.10, codenamed *Eoan Ermine* on 3 April 2019. It was released on 17 October 2019. It uses Linux kernel 5.3 which, among others, introduces compatibility for third-generation Ryzen CPU motherboards and associated Intel Wireless devices as well as AMD's 7 nm Navi GPUs.

Experimental support for the ZFS filesystem is now available from the installer. NVIDIA-specific improvements were made. Proprietary Nvidia graphics drivers are now bundled with the installer in place of the open-source Nouveau drivers. Support for the Raspberry Pi 4 platform was added. The installation media now uses LZ4 compression which, compared to the previously used compression algorithm, gzip, offers faster installation times. This was decided following benchmarking of a variety of compression algorithms conducted by the Ubuntu kernel team. Kernel load and decompression times were tested and LZ4 was found to offer decompression as much as seven times faster. Ubuntu 19.10 uses GNOME 3.34 which, among others, adds the ability to group application icons into folders, introduces a background settings panel and a separate Night Light tab as well as improves upon performance and smoothness. A new Yaru light theme was introduced with this release as well.

In a November 2019 *Ars Technica* review by Scott Gilbertson, he concluded, "Ubuntu 19.10 is unusual for an October Ubuntu release in that I would call it a must-have upgrade. While it retains some of the experimental elements Ubuntu's fall releases have always been known for, the speed boosts to GNOME alone make this release well worth your time."

### Ubuntu 20.04 LTS (Focal Fossa)

On 17 August 2019, Ubuntu 20.04 LTS, codenamed *Focal Fossa* was announced by Shuttleworth. It was released on 23 April 2020, and as a long-term support release, it received maintenance updates for 5 years until April 2025. This release is based on Linux kernel 5.4 LTS which adds support for new hardware including Intel's Comet Lake and Tiger Lake CPUs, Qualcomm's Snapdragon 835 and 855 SoCs as well as AMD Navi 12 and 14 GPUs. It also adds support for reboot-free kernel updates, the exFAT filesystem, the open-source WireGuard VPN, and a security module named Lockdown, disabled by default, which aims to prevent privileged root accounts from interacting with the underlying kernel by restricting kernel functionality, disallowing execution of arbitrary code and enforcing kernel module signatures. Python 2 is no longer included by default. This release refreshed the Yaru theme and uses GNOME 3.36 which revamped the login screen. Improvements have also been made to the system menu and the installation screen, which now shows a graphical drive checking routine. The ZFS file system is now offered as an option in the installer and tools for it are now bundled.

The OEM logo is now displayed during boot. Ubuntu Software will now only install packages from the Snap Store and provide an option for selecting the desired release channel to install from. This release also ended all support for the 32-bit architecture. DEB files now open in Archive Manager by default.

Reviewers praised the stability, polish and speed of the release. Joey Sneddon of *OMG Ubuntu* noted the significant number of major changes compared to other recent LTS releases. However, Jesse Smith of DistroWatch gave a negative review, citing boot and stability issues, lack of documentation and functionality of ZFS tools, lack of Flatpak support, and the decision to have Ubuntu Software only offer Snaps—a Flatpak alternative developed by Canonical, criticized as few in number, slow, heavily memory-consuming and bad at integration.

### Ubuntu 20.10 (Groovy Gorilla)

Ubuntu 20.10, codenamed *Groovy Gorilla*, was released on 22 October 2020. This release is based on GNOME 3.38 and Linux kernel 5.8 which includes support for USB4, AMD Zen 3 CPUs, Intel Ice Lake and Tiger Lake processors, and initial support for booting Power10 processors. In addition, nftables is now the default firewall backend, replacing iptables. Ubuntu 20.10 is the first release to feature desktop images for the Raspberry Pi 4 (4 GB and 8 GB models) and the Compute Module 4. Older Pi models with less memory are not officially supported.

### Ubuntu 21.04 (Hirsute Hippo)

Ubuntu 21.04, codenamed *Hirsute Hippo*, was released on 22 April 2021. It uses Linux kernel 5.11 which introduces smartcard authentication, support for Intel's Software Guard Extensions and improved support for AMD CPUs and GPUs.

Wayland is now used as the default on hardware without Nvidia graphics processors. Support for drag and drop from the file manager to the desktop was also added. An update to GNOME 40 was canceled due to questions about the stability of the GTK4 toolkit, a major GNOME interface redesign, and its unknown impact on GNOME extensions and Ubuntu's default Yaru GTK theme.

In a review, Joey Sneddon of *OMG Ubuntu* praised the stability and new features: "But it's not a release totally devoid of value. Ubuntu 21.04 features a striking new dark theme and makes a raft of smaller UI tweaks that add up to an impressive, polished whole. There are also new installer features, a new desktop icons experience, and (of course) a new wallpaper."

### Ubuntu 21.10 (Impish Indri)

Ubuntu 21.10, codenamed *Impish Indri*, was released on 14 October 2021. It uses Linux kernel 5.13, which introduces rudimentary support for Apple M1 chips, FreeSync HDMI support for AMD GPUs, a new "Landlock" security module and support for several new hardware.

This release transitions from GNOME 3.38 to GNOME 40, which introduces a horizontal workspace switcher and an improved Activities Overview design. The Ubuntu Dock remains vertically placed on the left of the screen and now features separators between pinned and running applications, a persistent trash can icon and USB drive shortcuts. After logging in, the user will be shown the desktop instead of the Activities Overview. Despite Ubuntu 21.10 shipping with GNOME 40, a few GNOME 41 apps are available. A Firefox Snap is now installed by default on Ubuntu 21.10 instead of the deb package, which remained available. Furthermore, the Nvidia proprietary drivers now support Wayland sessions. The default Yaru theme was also updated with new icons and Zstd compression was enabled in the main archive, making installations faster.

### Ubuntu 22.04 LTS (Jammy Jellyfish)

Ubuntu 22.04, codenamed *Jammy Jellyfish*, was released on 21 April 2022, and is a long-term support release, supported for five years, until April 2027. Ubuntu 22.04 LTS Desktop uses Linux kernel 5.17 for newer hardware and a rolling HWE (hardware enablement) kernel based on version 5.15 for other hardware; Ubuntu 22.04 LTS Server uses version 5.15, while Ubuntu Cloud and Ubuntu for IoT use an optimized kernel based on version 5.15. It updates Python to 3.10 and Ruby to 3.0.

The desktop is a mix of GNOME 41 and 42 applications to avoid libadwaita. The default web browser, Firefox, is only available as a snap package and the release repositories no longer provide an alternative .deb package. This release includes two Yaru themes, light and dark, with a choice of ten different accent colors for customization. A planned notification asking to enable Ubuntu Pro, a free-for-home-use rebrand of Ubuntu Advantage, was dropped from the release after user backlash.

While most reviews were positive, DistroWatch reviewer Jesse Smith was critical of the release, citing several bugs, inconsistent design, and stagnation, writing:

> I think the launch of Ubuntu 22.04 is a clear sign Canonical is much more interested in publishing releases on a set schedule than producing something worthwhile. This version was not ready for release and it is probably going to be a costly endeavour to maintain this collection of mixed versioned software and mixed display server and mixed designs for a full five years. It's a platform I would recommend avoiding.

In a poll conducted by DistroWatch, 70% of readers expressed dislike at Ubuntu migrating packages to being snap-only.

### Ubuntu 22.10 (Kinetic Kudu)

Ubuntu 22.10, codenamed *Kinetic Kudu*, was released on 20 October 2022. It uses Linux kernel 5.19, which improves the power efficiency on Intel-based computers and supports multithreaded decompression. It also upgrades to GNOME 43, which introduces quick settings in the top-right corner, replaces PulseAudio–its default audio server–with PipeWire, adds support for MicroPython on microcontrollers such as the Raspberry Pi Pico W, and adds support for RISC-V processors. rshell, thonny, and mpremote were added to the Ubuntu repositories.

### Ubuntu 23.04 (Lunar Lobster)

Ubuntu 23.04 *Lunar Lobster* is an interim release, released on 20 April 2023 and supported for nine months until 20 January 2024. This release incorporates GNOME 44, Linux kernel 6.2, Mesa 23.0 graphics drivers, a new Flutter-based installer, an improved Quick Settings menu, a new Mouse & Touchpad menu in Settings, improved Snap package startup times, and improved Snap package support that allows downloading open applications in the background and installing them when the application is closed. The release also provides support for Microsoft Azure Active Directory (a.k.a. Entra ID), which allows users with Microsoft 365 Enterprise plans to authenticate the Ubuntu desktops using common credentials. The default font has been updated to be slimmer and sharper. Reviewer Joey Sneddon of *OMG! Ubuntu* wrote, "if you asked me to describe Ubuntu 23.04 in one word I'd choose: "improvement". Nothing in this release is revolutionary – but that's not a bad thing."

### Ubuntu 23.10 (Mantic Minotaur)

Ubuntu 23.10 *Mantic Minotaur* is an interim release, originally released on 12 October 2023, and supported for nine months until July 2024. This release incorporates a new App Center built in Flutter that replaces Ubuntu Software, TPM disk encryption, a separated firmware updater, Netplan as the default network configuration tool, and support for Raspberry Pi 5. The installer can now update itself, support guided ZFS installation, and defaults to a minimal installation, which doesn't include apps deemed non-essential such as LibreOffice, Mozilla Thunderbird, Rhythmbox, and Calendar. Out-of-the-box support for installing .deb package files graphically was removed; however, the dialog for choosing an alternative app to open the file still recommended opening with the App Center. This would lead to uproar when the behavior was left unchanged in the next release.

This version also includes an upgrade to GNOME 45, which replaces the top-left corner's app name display with an indicator of the workspace being used, adds a camera usage indicator, a new camera app named "Snapshot", and a new image viewer app. Sidebars are now as tall as their windows as part of design polishing.

Approximately 6 hours after release, the download link to Ubuntu 23.10 was removed due to hate speech in an externally-sourced Ukrainian translation of the installer. Downloads were restored 4 days later.

### Ubuntu 24.04 LTS (Noble Numbat)

Ubuntu 24.04 *Noble Numbat* is a long-term support release that was released on 25 April 2024. It is based on systemd v255.4 and Linux kernel 6.8, which includes support for more gamepads and better swap memory handling. Raspberry Pi users no longer need to install its own package for bluetooth support, and the year 2038 problem has been patched for 32-bit armhf systems, which will no longer have their own images in future major releases. The release coincides with the release of Netplan v1.0, the default network configuration tool since 23.10. System image size has been reduced by 200 MB.

As part of an upgrade to GNOME 46, many apps have been updated to use libadwaita and GTK4. Nautilus, the file manager, has received several quality-of-life features, and Wi-Fi settings now include an option to generate a QR code for network credentials. Notifications now include a header for the sender app's name, settings have been reorganized, touch users now tap to click by default, and users can now log in from a remote desktop.

Cheese, a Photo Booth-like camera app, has been replaced by GNOME Snapshot in the extended install, and GNOME Games is now never bundled on install. Thunderbird is now provided as only its snap version.

Abishek of *It's Foss News* strongly criticized the LTS release for not changing behavior from 23.10, the last release, that by default made users unable to graphically install .deb packages, the most popular format for distributing software. Combined with the App Center, a recommended application to open the package with, freezing when attempting to open a .deb file, along with .deb's being opened with the archive extractor by default in 20.04, he argued that this was indicative of Canonical resorting to sabotaging user experience to promote their own products—in this case, snap packages. Conversely, *It's Foss* praised other aspects of the release as "a near-perfect upgrade". By July 15, the App Center received the ability to install .deb packages (while providing a warning), though they still cannot be managed even if installed from the App Center's store.

### Ubuntu 24.10 (Oracular Oriole)

Ubuntu 24.10 *Oracular Oriole* is an interim release, released on 10 October 2024, marking the 20th anniversary of the Ubuntu project; to commemorate, the release includes a selectable retro theme (wallpaper, accent color, and startup sound). Ubuntu's GNOME customizations were moved to a separate Settings section, a Security Center was added that features fine-grained app-by-app permissions control, the dock shows progress bars for updates to snap apps, and the App Center now supports graphically installing DEB files. The release uses Wayland by default on Nvidia GPUs and ships GNOME 47.

On 9 August 2024, Ubuntu announced a change in policy to always use the latest upstream version of the Linux kernel—even if said version is a release candidate instead of a stable release, as long as it is past its merge window—at the time of each kernel freeze, which is now two weeks before the release date.

### Ubuntu 25.04 (Plucky Puffin)

Ubuntu 25.04 *Plucky Puffin* was released on 17 April 2025 and ships Linux 6.14 and GNOME 48, which includes notification grouping; "Wellbeing", a screen time and limits management feature; battery charge limits powered by UPower; HDR support; and the replacement of Evince with its GTK 4 fork Papers as the default document viewer. Additionally, it includes JPEG XL support by default and replaces the archived Mozilla Location Service with beaconDB.

### Ubuntu 25.10 (Questing Quokka)

Ubuntu 25.10 *Questing Quokka* was released on 9 October 2025. Update notification is now done through a notification and tray applet instead of a window that steals input focus; Ubuntu plans to work on a different solution when Wayland protocols allow for better control of the window to focus. Icons on the desktop now have improved keyboard navigation and screenreader announcements. TPM-backed full-disk encryption has been added as an experimental installer option along with support in Firmware Updater and Security Center. A new boot spinner fixes distracting visual glitches, and the dock icon outline now aligns with the edge of the dock, shipped along with updates to the default Yaru theme (including a new trash can).

The release adopts Dracut for initramfs generation, chrony for time synchronization, and Rust rewrites of fundamental command-line utilities: sudo-rs for sudo and rust-coreutils to replace GNU Core Utilities. APT 3.1 is customized to include the upcoming history-related features as an "easter egg"—without documentation. In a push to cut down on size, wget was removed from the default server install in favor of wcurl, as well as Byobu and GNU Screen in favor of tmux. The Raspberry Pi image is now consistent with the "minimal" software set option in the desktop installer and uses a backup and boot-testing mechanism to improve booting reliability in a new process dubbed "tryboot". For RISC-V processors, the release raises profile requirements to RVA23, which was not implemented in any on-market hardware as of 9 October.

Ptyxis replaces GNOME Terminal as the default terminal emulator, providing container and remote connection support along with performance improvements. Loupe replaces Eye of GNOME as the default image viewer. Ubuntu 25.10 incorporates GNOME 49, which disables the X11 session by default, adds accessibility tools and media controls to the lock screen, changes fractional scaling calculation to sharpen rendering on high-res displays, implements pointer wrap, supports variable–refresh-rate cursors, and removes the "Startup Applications" app in favor of a settings panel; *OMG! Ubuntu* expressed annoyance at being unable to run custom commands at login with the new interface.

Initially, Ubuntu 25.10 could not install flatpaks due to an AppArmor issue. This was fixed on 15 October. Some Ubuntu 25.10 systems could not automatically check for software updates due to a bug in rust-coreutils's version of the `date` command fixed on 22 October. Manual updates such as updates done through the `apt` command were not affected.

### Ubuntu 26.04 LTS (Resolute Raccoon)

Ubuntu 26.04 *Resolute Raccoon* was released on 23 April 2026 and users were officially allowed to upgrade from 25.10 on 14 May. 24.04 LTS installations were expected to be able to upgrade in August with the release of 26.04.1. The codename was selected by and as a tribute to the Debian and Ubuntu release manager, Steve Langasek, before his death.

This version incorporates Linux 7.0 and GNOME 50, which removed support for Xorg/X11. Recommended system requirements were raised to 6 GB RAM to reflect typical workloads. Sudo was configured to show asterisks when typing by default. The desktop UI was updated with greater contrast and consistency, more colorful folder icons, and a new boot animation inspired by the Resolute Raccoon mascot. Showtime replaced Totem video player, and Resources replaces System Monitor and Power Statistics. Global search can now search for available Snap applications and the web. Software & Updates, which manages package repositories, was dropped from the default installation; Ubuntu Pro status is now managed by Security Center, along with disk encryption.

### Ubuntu 26.10 (Stonking Stingray)

Canonical revealed the codename for Ubuntu 26.10 on April 20, 2026, and it is officially “Stonking Stingray.” According to the company’s schedule, its release is expected on October 15, 2026.


## Table of versions

| Version | Code name | Release date | Standard support until | Extended security maintenance until | Legacy Add-On Coverage until | Initial kernel version |
|---|---|---|---|---|---|---|
| 4.10 | Warty Warthog | 2004-10-20 | Unsupported: 2006-04-30 | —N/a | —N/a | 2.6.8 |
| 5.04 | Hoary Hedgehog | 2005-04-08 | Unsupported: 2006-10-31 | —N/a | —N/a | 2.6.10 |
| 5.10 | Breezy Badger | 2005-10-12 | Unsupported: 2007-04-13 | —N/a | —N/a | 2.6.12 |
| 6.06 LTS | Dapper Drake | 2006-06-01 | Unsupported: 2009-07-14 | —N/a | —N/a | 2.6.15 |
| 6.10 | Edgy Eft | 2006-10-26 | Unsupported: 2008-04-25 | —N/a | —N/a | 2.6.17 |
| 7.04 | Feisty Fawn | 2007-04-19 | Unsupported: 2008-10-19 | —N/a | —N/a | 2.6.20 |
| 7.10 | Gutsy Gibbon | 2007-10-18 | Unsupported: 2009-04-18 | —N/a | —N/a | 2.6.22 |
| 8.04 LTS | Hardy Heron | 2008-04-24 | Unsupported: 2011-05-12 | —N/a | —N/a | 2.6.24 |
| 8.10 | Intrepid Ibex | 2008-10-30 | Unsupported: 2010-04-30 | —N/a | —N/a | 2.6.27 |
| 9.04 | Jaunty Jackalope | 2009-04-23 | Unsupported: 2010-10-23 | —N/a | —N/a | 2.6.28 |
| 9.10 | Karmic Koala | 2009-10-29 | Unsupported: 2011-04-30 | —N/a | —N/a | 2.6.31 |
| 10.04 LTS | Lucid Lynx | 2010-04-29 | Unsupported: 2013-05-09 | —N/a | —N/a | 2.6.32 |
| 10.10 | Maverick Meerkat | 2010-10-10 | Unsupported: 2012-04-10 | —N/a | —N/a | 2.6.35 |
| 11.04 | Natty Narwhal | 2011-04-28 | Unsupported: 2012-10-28 | —N/a | —N/a | 2.6.38 |
| 11.10 | Oneiric Ocelot | 2011-10-13 | Unsupported: 2013-05-09 | —N/a | —N/a | 3.0 |
| 12.04 LTS | Precise Pangolin | 2012-04-26 | Unsupported: 2017-04-28 | Unsupported: 2019-04-26 | —N/a | 3.2 |
| 12.10 | Quantal Quetzal | 2012-10-18 | Unsupported: 2014-05-16 | —N/a | —N/a | 3.5 |
| 13.04 | Raring Ringtail | 2013-04-25 | Unsupported: 2014-01-27 | —N/a | —N/a | 3.8 |
| 13.10 | Saucy Salamander | 2013-10-17 | Unsupported: 2014-07-17 | —N/a | —N/a | 3.11 |
| 14.04 LTS | Trusty Tahr | 2014-04-17 | Unsupported: 2019-04-25 | Unsupported: 2024-04-25 | Supported: 2029-04-25 | 3.13 |
| 14.10 | Utopic Unicorn | 2014-10-23 | Unsupported: 2015-07-23 | —N/a | —N/a | 3.16 |
| 15.04 | Vivid Vervet | 2015-04-23 | Unsupported: 2016-02-04 | —N/a | —N/a | 3.19 |
| 15.10 | Wily Werewolf | 2015-10-22 | Unsupported: 2016-07-28 | —N/a | —N/a | 4.2 |
| 16.04 LTS | Xenial Xerus | 2016-04-21 | Unsupported: 2021-04-30 | Unsupported: 2026-04-23 | Supported: 2031-04-23 | 4.4 |
| 16.10 | Yakkety Yak | 2016-10-13 | Unsupported: 2017-07-20 | —N/a | —N/a | 4.8 |
| 17.04 | Zesty Zapus | 2017-04-13 | Unsupported: 2018-01-13 | —N/a | —N/a | 4.10 |
| 17.10 | Artful Aardvark | 2017-10-19 | Unsupported: 2018-07-19 | —N/a | —N/a | 4.13 |
| 18.04 LTS | Bionic Beaver | 2018-04-26 | Unsupported: 2023-05-31 | Supported: 2028-04-26 | Supported: 2033-04-26 | 4.15 |
| 18.10 | Cosmic Cuttlefish | 2018-10-18 | Unsupported: 2019-07-18 | —N/a | —N/a | 4.18 |
| 19.04 | Disco Dingo | 2019-04-18 | Unsupported: 2020-01-23 | —N/a | —N/a | 5.0 |
| 19.10 | Eoan Ermine | 2019-10-17 | Unsupported: 2020-07-17 | —N/a | —N/a | 5.3 |
| 20.04 LTS | Focal Fossa | 2020-04-23 | Unsupported: 2025-05-29 | Supported: 2030-04-23 | Supported: 2035-04-23 | 5.4 |
| 20.10 | Groovy Gorilla | 2020-10-22 | Unsupported: 2021-07-22 | —N/a | —N/a | 5.8 |
| 21.04 | Hirsute Hippo | 2021-04-22 | Unsupported: 2022-01-20 | —N/a | —N/a | 5.11 |
| 21.10 | Impish Indri | 2021-10-14 | Unsupported: 2022-07-14 | —N/a | —N/a | 5.13 |
| 22.04 LTS | Jammy Jellyfish | 2022-04-21 | Supported: 2027-06-01 | Supported: 2032-04-21 | Supported: 2037-04-21 | 5.15 or 5.17 |
| 22.10 | Kinetic Kudu | 2022-10-20 | Unsupported: 2023-07-20 | —N/a | —N/a | 5.19 |
| 23.04 | Lunar Lobster | 2023-04-20 | Unsupported: 2024-01-25 | —N/a | —N/a | 6.2 |
| 23.10 | Mantic Minotaur | 2023-10-12 | Unsupported: 2024-07-11 | —N/a | —N/a | 6.5 |
| 24.04 LTS | Noble Numbat | 2024-04-25 | Supported: 2029-05-31 | Supported: 2034-04-25 | Supported: 2039-04-25 | 6.8 |
| 24.10 | Oracular Oriole | 2024-10-10 | Unsupported: 2025-07-10 | —N/a | —N/a | 6.11 |
| 25.04 | Plucky Puffin | 2025-04-17 | Unsupported: 2026-01-15 | —N/a | —N/a | 6.14 |
| 25.10 | Questing Quokka | 2025-10-09 | Latest version: 2026-07-09 | —N/a | —N/a | 6.17 |
| 26.04 LTS | Resolute Raccoon | 2026-04-23 | Latest version: 2031-05-29 | Latest version: 2036-04-23 | Latest version: 2041-04-23 | 7.0 |
| 26.10 | Stonking Stingray | 2026-10-15 | Preview version: 2027-07-15 | —N/a | —N/a | —N/a |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |   |   |

1. 2011-06-01 for Ubuntu 6.06 LTS Server
2. 2013-05-09 for Ubuntu 8.04 LTS Server
3. 2015-04-30 for Ubuntu 10.04 LTS Server
4. Announced as 6.20.
