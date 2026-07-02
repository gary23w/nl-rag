---
title: "Memory forensics"
source: https://en.wikipedia.org/wiki/Memory_forensics
domain: digital-forensics
license: CC-BY-SA-4.0
tags: digital forensics, computer forensics, forensic data recovery, memory forensics, chain of custody
fetched: 2026-07-02
---

# Memory forensics

**Memory forensics** is forensic analysis of a computer's memory dump. Its primary application is investigation of advanced cyberattacks which are stealthy enough to avoid leaving data on the computer's hard drive. Consequently, the memory (e.g. RAM) must be analyzed for forensic information.

## History

### Zeroth generation tools

Until the early 2000s, memory forensics was done on an ad hoc basis (termed *unstructured analysis*), often using generic data analysis tools like strings and grep. These tools are not specifically created for memory forensics, and therefore are difficult to use. They also provide limited information. In general, their primary usage is to extract text from the memory dump.

Many operating systems provide features to kernel developers and end-users to actually create a snapshot of the physical memory for either debugging (e.g. core dump or Blue Screen of Death) purposes or experience enhancement (e.g. hibernation). In the case of Microsoft Windows, crash dumps and hibernation had been present since Microsoft Windows NT. Microsoft crash dumps had always been analyzable by Microsoft WinDbg, and Windows hibernation files (hiberfil.sys) are nowadays convertible in Microsoft crash dumps using utilities like MoonSols Windows Memory Toolkit designed by Matthieu Suiche.

### First generation tools

One significant step towards *structured analysis* was in a February 2004 article in SysAdmin Magazine, where Michael Ford demonstrated a more rigorous practice of memory forensics. In that article, he analyzes a memory based rootkit utilizing the existing Linux crash utility as well as two tools developed specifically to recover and analyze the memory forensically, memget and mempeek.

In 2005, DFRWS issued a Memory Analysis Forensics Challenge. In response to this challenge, more tools in this generation, specifically designed to analyze memory dumps, were created - such as MoonSols, KntTools, the FATKit, VolaTools, and Volatility. These tools had knowledge of the operating system's internal data structures, and were thus capable of reconstructing the operating system's process list and process information.

Although intended as research tools, they proved that operating system level memory forensics is possible and practical.

### Second generation tools

Subsequently, several memory forensics tools were developed intended for practical use. These include both commercial tools like Responder PRO, Memoryze, winen, Belkasoft Live RAM Capturer, etc.. New features have been added, such as analysis of Linux and Mac OS X memory dumps, and substantial academic research has been carried out.

Unlike Microsoft Windows, Mac OS X interest is relatively new and had only been initiated by Matthieu Suiche in 2010 during Black Hat Briefings security conference.

Currently, memory forensics is a standard component of incident response.

### Third generation tools

Beginning 2010, more utilities focused on the visualization aspect of memory analysis, such as MoonSols LiveCloudKd presented by Matthieu Suiche at Microsoft BlueHat Security Briefings that inspired a new feature in Microsoft LiveKd written by Mark Russinovich to allow virtual machines introspection by accessing the memory of guest virtual machine from the host virtual machine in order to either analyze them directly with the assistance of Microsoft WinDbg or to acquire a memory dump in a Microsoft crash dump file format.
