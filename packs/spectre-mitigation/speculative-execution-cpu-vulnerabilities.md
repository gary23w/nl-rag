---
title: "Transient execution CPU vulnerability"
source: https://en.wikipedia.org/wiki/Speculative_execution_CPU_vulnerabilities
domain: spectre-mitigation
license: CC-BY-SA-4.0
tags: spectre mitigation, speculative execution defense, cpu side channel defense, branch predictor hardening
fetched: 2026-07-02
---

# Transient execution CPU vulnerability

(Redirected from

Speculative execution CPU vulnerabilities

)

**Transient execution CPU vulnerabilities** are vulnerabilities in which instructions, most often optimized using speculative execution, are executed temporarily by a microprocessor, without committing their results due to a misprediction or error, resulting in leaking secret data to an unauthorized party. The archetype is Spectre, and transient execution attacks like Spectre belong to the cache-attack category, one of several categories of side-channel attacks. Since January 2018 many different cache-attack vulnerabilities have been identified.

## Overview

Modern computers are highly parallel devices, composed of components with very different performance characteristics. If an operation (such as a branch) cannot yet be performed because some earlier slow operation (such as a memory read) has not yet completed, a microprocessor may attempt to *predict* the result of the earlier operation and execute the later operation *speculatively*, acting as if the prediction were correct. The prediction may be based on recent behavior of the system. When the earlier, slower operation completes, the microprocessor determines whether the prediction was correct or incorrect. If it was correct then execution proceeds uninterrupted; if it was incorrect then the microprocessor rolls back the speculatively executed operations and repeats the original instruction with the real result of the slow operation. Specifically, a *transient instruction* refers to an instruction processed by error by the processor (incriminating the branch predictor in the case of Spectre) which can affect the micro-architectural state of the processor, leaving the architectural state without any trace of its execution.

In terms of the directly visible behavior of the computer it is as if the speculatively executed code "never happened". However, this speculative execution may affect the state of certain components of the microprocessor, such as the cache, and this effect may be discovered by careful monitoring of the timing of subsequent operations.

If an attacker can arrange that the speculatively executed code (which may be directly written by the attacker, or may be a suitable *gadget* that they have found in the targeted system) operates on secret data that they are unauthorized to access, and has a different effect on the cache for different values of the secret data, they may be able to discover the value of the secret data.

## Timeline

### 2018

In early January 2018, it was reported that all Intel processors made since 1995 (besides Intel Itanium and pre-2013 Intel Atom) have been subject to two security flaws dubbed **Meltdown** and **Spectre**.

The impact on performance resulting from software patches is "workload-dependent". Several procedures to help protect home computers and related devices from the Spectre and Meltdown security vulnerabilities have been published. Spectre patches have been reported to significantly slow down performance, especially on older computers; on the newer 8th-generation Core platforms, benchmark performance drops of 2–14% have been measured. Meltdown patches may also produce performance loss. It is believed that "hundreds of millions" of systems could be affected by these flaws. More security flaws were disclosed on May 3, 2018, on August 14, 2018, on January 18, 2019, and on March 5, 2020.

At the time, Intel was not commenting on this issue.

On March 15, 2018, Intel reported that it will redesign its CPUs (performance losses to be determined) to protect against the Spectre security vulnerability, and expects to release the newly redesigned processors later in 2018.

On May 3, 2018, eight additional Spectre-class flaws were reported. Intel reported that they are preparing new patches to mitigate these flaws.

On August 14, 2018, Intel disclosed three additional chip flaws referred to as **L1 Terminal Fault (L1TF)**. They reported that previously released microcode updates, along with new, pre-release microcode updates can be used to mitigate these flaws.

### 2019

On January 18, 2019, Intel disclosed three new vulnerabilities affecting all Intel CPUs, named "**Fallout**", "**RIDL**", and "**ZombieLoad**", allowing a program to read information recently written, read data in the line-fill buffers and load ports, and leak information from other processes and virtual machines. Coffee Lake-series CPUs are even more vulnerable, due to hardware mitigations for Spectre.

### 2020

On March 5, 2020, computer security experts reported another Intel chip security flaw, besides the Meltdown and Spectre flaws, with the systematic name CVE-2019-0090 (or "**Intel CSME Bug**"). This newly found flaw is not fixable with a firmware update, and affects nearly "all Intel chips released in the past five years".

### 2021

In March 2021 AMD security researchers discovered that the Predictive Store Forwarding algorithm in Zen 3 CPUs could be used by malicious applications to access data it shouldn't be accessing. According to Phoronix there's little performance impact in disabling the feature.

In June 2021, two new vulnerabilities, **Speculative Code Store Bypass** (**SCSB**, CVE-2021-0086) and **Floating Point Value Injection** (FPVI, CVE-2021-0089), affecting *all* modern x86-64 CPUs both from Intel and AMD were discovered. In order to mitigate them software has to be rewritten and recompiled. ARM CPUs are not affected by SCSB but some certain ARM architectures are affected by FPVI.

Also in June 2021, MIT researchers revealed the **PACMAN** attack on Pointer Authentication Codes (PAC) in ARM v8.3A.

In August 2021 a vulnerability called "**Transient Execution of Non-canonical Accesses**" affecting certain AMD CPUs was disclosed. It requires the same mitigations as the MDS vulnerability affecting certain Intel CPUs. It was assigned CVE-2020-12965. Since most x86 software is already patched against MDS and this vulnerability has the exact same mitigations, software vendors don't have to address this vulnerability.

In October 2021 for the first time ever a vulnerability similar to Meltdown was disclosed to be affecting all AMD CPUs however the company doesn't think any new mitigations have to be applied and the existing ones are already sufficient.

### 2022

In March 2022, a new variant of the Spectre vulnerability called **Branch History Injection** was disclosed. It affects certain ARM64 CPUs and the following Intel CPU families: Cascade Lake, Ice Lake, Tiger Lake and Alder Lake. According to Linux kernel developers AMD CPUs are also affected.

In March 2022, a vulnerability affecting a wide range of AMD CPUs was disclosed under CVE-2021-26341.

In June 2022, multiple MMIO Intel CPUs vulnerabilities related to execution in virtual environments were announced. The following CVEs were designated: CVE-2022-21123, CVE-2022-21125, CVE-2022-21166.

In July 2022, the **Retbleed** vulnerability was disclosed affecting Intel Core 6 to 8th generation CPUs and AMD Zen 1, 1+ and 2 generation CPUs. Newer Intel microarchitectures as well as AMD starting with Zen 3 are not affected. The mitigations for the vulnerability decrease the performance of the affected Intel CPUs by up to 39%, while AMD CPUs lose up to 14%.

In August 2022, the **SQUIP** vulnerability was disclosed affecting Ryzen 2000–5000 series CPUs. According to AMD the existing mitigations are enough to protect from it.

According to a Phoronix review released in October, 2022 Zen 4/Ryzen 7000 CPUs are not slowed down by mitigations, in fact disabling them leads to a performance loss.

### 2023

In February 2023 a vulnerability affecting a wide range of AMD CPU architectures called "**Cross-Thread Return Address Predictions**" was disclosed.

In July 2023 a critical vulnerability in the Zen 2 AMD microarchitecture called **Zenbleed** was made public. AMD released a microcode update to fix it.

In August 2023 a vulnerability in AMD's Zen 1, Zen 2, Zen 3, and Zen 4 microarchitectures called **Inception** was revealed and assigned CVE-2023-20569. According to AMD it is not practical but the company released a microcode update for the affected products.

Also in August 2023 a new vulnerability called **Downfall** or **Gather Data Sampling** was disclosed, affecting Intel CPU Skylake, Cascade Lake, Cooper Lake, Ice Lake, Tiger Lake, Amber Lake, Kaby Lake, Coffee Lake, Whiskey Lake, Comet Lake & Rocket Lake CPU families. Intel will release a microcode update for affected products.

The **SLAM** vulnerability (**Spectre based on Linear Address Masking**) reported in 2023 neither has received a corresponding CVE, nor has been confirmed or mitigated against.

### 2024

In March 2024, a variant of Spectre-V1 attack called **GhostRace** was published. It was claimed it affected all the major microarchitectures and vendors, including Intel, AMD and ARM. It was assigned CVE-2024-2193. AMD dismissed the vulnerability (calling it "Speculative Race Conditions (SRCs)") claiming that existing mitigations were enough. Linux kernel developers chose not to add mitigations citing performance concerns. The Xen hypervisor project released patches to mitigate the vulnerability but they are not enabled by default.

Also in March 2024, a vulnerability in Intel Atom processors called **Register File Data Sampling** (**RFDS**) was revealed. It was assigned CVE-2023-28746. Its mitigations incur a slight performance degradation.

In April 2024, it was revealed that the BHI vulnerability in certain Intel CPU families could be still exploited in Linux entirely in user space without using any kernel features or root access despite existing mitigations. Intel recommended "additional software hardening". The attack was assigned CVE-2024-2201.

In June 2024, Samsung Research and Seoul National University researchers revealed the **TikTag** attack against the Memory Tagging Extension in ARM v8.5A CPUs. The researchers created PoCs for Google Chrome and the Linux kernel. Researchers from VUSec previously revealed ARM's Memory Tagging Extension is vulnerable to speculative probing.

In July 2024, UC San Diego researchers revealed the **Indirector** attack against Intel Alder Lake and Raptor Lake CPUs leveraging high-precision Branch Target Injection (BTI). Intel downplayed the severity of the vulnerability and claimed the existing mitigations are enough to tackle the issue. No CVE was assigned.

### 2025

In January 2025, Georgia Institute of Technology researchers published two whitepapers on **Data Speculation Attacks via Load Address Prediction on Apple Silicon (SLAP)** and Breaking the Apple M3 CPU via False Load Output Predictions (FLOP).

Also in January 2025, ARM disclosed a vulnerability (CVE-2024-7881) in which an unprivileged context can trigger a data memory-dependent prefetch engine to fetch data from a privileged location, potentially leading to unauthorized access. To mitigate the issue, Arm recommends disabling the affected prefetcher by setting CPUACTLR6_EL1[41].

In May 2025, VUSec released three vulnerabilities extending on Spectre-v2 in various Intel and ARM architectures under the moniker **Training Solo**. Mitigations require a microcode update for Intel CPUs and changes in the Linux kernel.

- The history-based attack affects all Intel CPUs with eIBRS, including the latest as of 2025, Intel’s latest generation Lion Cove which features the BHI_NO feature and selected ARM microarchitectures.
- Indirect Target Selection (ITS) (CVE-2024-28956) affects Intel Core 9th-11th generations and Intel Xeon 2nd-3rd generations.
- Lion Cove BPU issue (CVE-2025-24495) affects the Lion Cove core, Lunar Lake and Arrow Lake.

Also in May 2025, ETH Zurich Computer Security Group "COMSEC" disclosed the **Branch Privilege Injection** vulnerability affecting all Intel x86 architectures starting from the 9th generation (Coffee Lake Refresh) under CVE-2024-45332. A microcode update is required to mitigate it. It comes with a performance cost up to 8%.

In July 2025, AMD disclosed a new class of speculative execution vulnerabilities known as **Transient Scheduler Attacks (TSA)**, which were discovered by researchers from Microsoft. The attacks are affecting AMD Zen 3 and Zen 4 microarchitectures, and they exploit microarchitectural timing leaks in CPU scheduler logic—specifically, the forwarding of incorrect data during false completion of speculative loads—to infer sensitive data from other processes or privilege levels. TSA encompasses four vulnerabilities: CVE-2024-36350 (TSA-SQ), which leaks data from prior stores; CVE-2024-36357 (TSA-L1), which leverages the L1 data cache; CVE-2024-36348, enabling speculative reads of control registers; and CVE-2024-36349, which leaks TSC_AUX register values. Mitigations include microcode updates, Linux kernel patches (`tsa=` tunable), and optional use of the `VERW` instruction—albeit with potential performance costs.

In September 2025, researchers at ETH Zurich disclosed **VMScape** (CVE-2025-40300), a Spectre-BTI-style transient execution attack that exploits incomplete isolation of the branch predictor between guest virtual machines and host user-space hypervisors (notably QEMU under KVM), allowing a malicious guest to influence speculative execution and leak sensitive host memory. The flaw affects AMD Zen 1–5 and Intel “Coffee Lake” processors, and mitigations include Linux kernel patches that conditionally issue Indirect Branch Prediction Barrier (IBPB) instructions on VMEXITs before returning control to user-space in order to flush predictor state.

### 2026

In February 2026 at FOSDEM 2026, the talk "How Secure Are Commercial RISC-V CPUs?" covered the security properties of several commercially available RISC-V processors and showed that current implementations already exhibit weaknesses related to microarchitectural side channels and speculative behavior. The researchers demonstrated that even relatively "simple" in-order RISC-V cores can leak sensitive information through timing channels, unprivileged performance counters, and undocumented vendor-specific extensions. The authors argued that manual analysis of such designs does not scale and presented **RISCover**, an open-source differential fuzzing framework, to compare architectural behavior across cores and configurations. Using this approach, they identified issues such as out-of-bounds memory accesses and denial-of-service conditions, and suggested that the lack of standardized mechanisms to constrain speculation and timing sources increases the risk of transient execution vulnerabilities similar to those previously observed in x86 and ARM processors.

In April 2026, Floating Point Divider State Sampling (FP-DSS), a transient execution vulnerability, affecting multiple generations of AMD CPUs, was reported in a paper titled "TREVEX: A Black-Box Detection Framework For Data-Flow Transient Execution Vulnerabilities". It was assigned CVE-2025-54505.

## Future

Spectre class vulnerabilities will remain unfixed because otherwise CPU designers will have to disable speculative execution which will entail a massive performance loss. Despite this, AMD has managed to design Zen 4 such a way its performance is *not* affected by mitigations.

## Vulnerabilities and mitigations summary

| Mitigation Type | Comprehensiveness | Effectiveness | Performance impact | Description |
|---|---|---|---|---|
| Hardware | Full | Full | None to small | Require changes to the CPU design and thus a new iteration of hardware |
| Microcode | Partial to full | Partial to full | None to large | Updates the software that the CPU runs on which requires patches to be released for each affected CPU and integrated into every BIOS or operating system |
| OS/VMM | Partial | Partial to full | Small to large | Applied at the operating system or virtual machine level and (depending on workload) |
| Software recompilation | Poor | Partial to full | Medium to large | Requires recompiling *lots* of pieces of software |

***** Various CPU microarchitectures not included above are also affected, among them are ARM, IBM Power, IBM Z, MIPS and others. Vulnerabilities starting with SLAM are not included in the table. It only exists as historical evidence because it doesn't include newer AMD and Intel x86 architectures.

****** The 8th generation Coffee Lake architecture in this table **also** applies to a wide range of previously released Intel CPUs, not limited to the architectures based on Intel Core, Pentium 4 and Intel Atom starting with Silvermont.

| **Vulnerability Name(s)/Subname** Official Name/Subname | CVE | Affected CPU architectures and mitigations* |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Intel | AMD |   |   |   |   |   |   |
| 10th gen | 9th gen | 8th gen** | Zen / Zen+ | Zen 2 |   |   |   |
| Ice Lake | Cascade / Comet / Amber Lake | Coffee Lake | Whiskey Lake | Coffee Lake, Amber Lake |   |   |   |
| **Spectre** | **v1** Bounds Check Bypass | CVE-2017-5753 | Software recompilation |   |   |   |   |
| **v2** Branch Target Injection | CVE-2017-5715 | Hardware + OS/VMM / Software recompilation | Microcode + ... | Microcode + OS/VMM / Software recompilation | Hardware + OS/VMM / Software recompilation |   |   |
| Hardware + ... |   |   |   |   |   |   |   |
| **Meltdown / v3** Rogue Data Cache Load | CVE-2017-5754 | Hardware | OS | Not affected |   |   |   |
| **Spectre-NG** | **v3a** Rogue System Register Read | CVE-2018-3640 | Hardware | Hardware | Microcode | Microcode | Microcode |
| Microcode | Hardware |   |   |   |   |   |   |
| **v4** Speculative Store Bypass | CVE-2018-3639 | [Hardware + OS / ] Software recompilation | ... | [Microcode + OS / ] Software recompilation | OS/VMM | Hardware + OS/VMM |   |
| ... |   |   |   |   |   |   |   |
| Lazy FP State Restore | CVE-2018-3665 | OS/VMM | Not affected |   |   |   |   |
| **v1.1** Bounds Check Bypass Store | CVE-2018-3693 | Software recompilation |   |   |   |   |   |
| **SpectreRSB**/**ret2spec** Return Mispredict | CVE-2018-15572 | OS |   |   |   |   |   |
| **Foreshadow** L1 Terminal Fault (L1TF) | SGX | CVE-2018-3615 | Not affected | Microcode | Not affected |   |   |
| OS/SMM | CVE-2018-3620 | Microcode + OS/VMM |   |   |   |   |   |
| VMM | CVE-2018-3646 |   |   |   |   |   |   |
| Microarchitectural Data Sampling (MDS) | **RIDL** | **ZombieLoad** Fill Buffer (MFBDS) | CVE-2018-12130 | Microcode + OS |   |   |   |
| Load Port (MLPDS) | CVE-2018-12127 | Hardware | Microcode + OS/VMM |   |   |   |   |
| Hardware |   |   |   |   |   |   |   |
| **Fallout** Store Buffer (MSBDS) | CVE-2018-12126 | Hardware + Microcode | Microcode + OS/VMM | Microcode + OS/VMM |   |   |   |
| Hardware |   |   |   |   |   |   |   |
| **RIDL** | Uncacheable Memory (MDSUM) | CVE-2019-11091 | Same as the buffer having entries |   |   |   |   |
| **SWAPGS** | CVE-2019-1125 | OS |   |   |   |   |   |
| **RIDL** (Rogue In-Flight Data Load) | **ZombieLoad v2** TSX Asynchronous Abort (TAA) | CVE-2019-11135 | Hardware | Microcode + OS/VMM | Existing MDS mitigations | Existing MDS mitigations |   |
| TSX not supported | Microcode + OS/VMM |   |   |   |   |   |   |
| **ZombieLoad/CacheOut** L1D Eviction Sampling (L1DES) | CVE-2020-0549 | Not affected | Microcode | Microcode |   |   |   |
| Not affected |   |   |   |   |   |   |   |
| Vector Register Sampling (VRS) | CVE-2020-0548 | Microcode |   |   |   |   |   |
| Not affected |   |   |   |   |   |   |   |
| Load Value Injection (LVI) | CVE-2020-0551 | Software recompilation (mainly for Intel SGX) |   |   |   |   |   |
| **CROSSTalk** Special Register Buffer Data Sampling (SRBDS) | CVE-2020-0543 | Microcode | Microcode |   |   |   |   |
| Not affected |   |   |   |   |   |   |   |
| Floating Point Value Injection (FPVI) | CVE-2021-0086 CVE-2021-26314 | Software recompilation |   |   |   |   |   |
| Speculative Code Store Bypass (SCSB) | CVE-2021-0089 CVE-2021-26313 |   |   |   |   |   |   |
| Branch History Injection (BHI) and other forms of intra-mode BTI | CVE-2022-0001 CVE-2022-0002 | Software recompilation | Not affected | Not affected |   |   |   |
| Software recompilation |   |   |   |   |   |   |   |
| MMIO Stale Data | Shared Buffers Data Read (SBDR) | CVE-2022-21123 | Not affected Microcode + Software recompilation | Microcode + Software recompilation | Software recompilation | Not affected |   |
| Shared Buffers Data Sampling (SBDS) | CVE-2022-21125 |   |   |   |   |   |   |
| Device Register Partial Write (DRPW) | CVE-2022-21166 | Microcode | Existing MDS mitigations |   |   |   |   |
| Branch Type Confusion (BTC) | **Phantom** | BTC-NOBR BTC-DIR | CVE-2022-23825 | Not affected | OS/VMM |   |   |
| BTC-IND | Existing Spectre v2 mitigations |   |   |   |   |   |   |
| **Retbleed** BTC-RET | CVE-2022-29900 CVE-2022-29901 | Not affected | OS/VMM | OS/VMM | OS/VMM / Software recompilation |   |   |
| Not affected |   |   |   |   |   |   |   |
| Cross-Thread Return Address Predictions | CVE-2022-27672 | Not affected | OS/VMM |   |   |   |   |
| **Zenbleed** Cross-Process Information Leak | CVE-2023-20593 | Not affected | Microcode |   |   |   |   |
| **Inception** Speculative Return Stack Overflow (SRSO) | CVE-2023-20569 | Not affected | OS/VMM |   |   |   |   |
| **Downfall** Gather Data Sampling (GDS) | CVE-2022-40982 | Microcode | Not affected |   |   |   |   |
