---
title: "TianoCore EDK II"
source: https://en.wikipedia.org/wiki/TianoCore
domain: tianocore-edk
license: CC-BY-SA-4.0
tags: tianocore edk2, uefi firmware, edk2 build, platform initialization
fetched: 2026-07-02
---

# TianoCore EDK II

(Redirected from

TianoCore

)

**TianoCore EDK II** (formerly **Tiano**) is the reference implementation of UEFI by Intel. EDK is the abbreviation for **EFI Development Kit** and is developed by the TianoCore community. TianoCore EDK II is the de facto standard generic UEFI services implementation.

## History

In 2004, Intel released their "Foundation Code" of their EFI implementation using a free license. The resulting code formed the basis of the community-run EDK project on SourceForge, started in 2004. The name "Tiano" was present in the initial Intel code. The last update to the EDK (version 1) project happened in May 2010. Version 2 is in active development.

An "edk2" project was imported into SourceForge in April 2006, with a package-oriented code base again written by Intel. The initial "DeveloperManual" referred to this project as "Tiano R9". In 2008, a stable, validated version of EDK II was tagged as "UEFI Development Kit 2008" (UDK2008). The tag includes a BuildNotes.txt dating to November 2006 describing the code found in the initial import, and a BuildNotes2.txt describing modules added in May 2008. UDK2010 was the first version of EDK II to be widely known. Intel would continue to validate certain snapshots of EDK II as UDK until 2018, when EDK II moved into a "stable tag" format.

In December 2023 a vulnerability termed "LogoFAIL" was discovered associated with EDK II which enabled an attacker to insert their own code in place of custom boot logo bitmap loader modules.

Although EDK II implements the UEFI specification, it is not endorsed by the UEFI Forum.

## Projects

EDK II code has been integrated into other projects.

A part of TianoCore is the UEFI shell. When a specific UEFI vendor does not provide a UEFI shell, the one from TianoCore can be used.

Google uses a version of coreboot modified to launch Tiano. This feature is called PIANO (payload into Tiano) or tianocoreboot. PIANO code was merged into coreboot in 2013. The code was updated to be compatible with EDK II in 2017.

EDK II source code includes instructions for building as a payload for coreboot or Intel's "slim bootloader".

Project Mu is a fork of EDK II by Microsoft. It is an open source release of the UEFI core used in Microsoft Surface and Hyper-V products initiated by Microsoft in December 2018. The project promotes the idea of firmware as a service. The project was started to build on TianoCore's EDK II implementation to improve modularity and increase the quality of tests when building UEFI firmware.

EFIDroid is a bootloader for Android devices based on Snapdragon processors that is based on EDK II.
