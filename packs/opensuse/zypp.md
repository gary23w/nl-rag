---
title: "ZYpp"
source: https://en.wikipedia.org/wiki/ZYpp
domain: opensuse
license: CC-BY-SA-4.0
tags: opensuse distribution, zypper package manager, yast tool, suse enterprise
fetched: 2026-07-02
---

# ZYpp

**ZYpp** (or **libzypp**; *"Zen / YaST Packages Patches Patterns Products"*) is a package manager engine that powers Linux applications like Myrlyn, YaST, Zypper and the implementation of PackageKit for openSUSE and SUSE Linux Enterprise. Unlike some more basic package managers, it provides a satisfiability solver to compute package dependencies. It is a free and open-source software project sponsored by SUSE and licensed under the terms of the GNU General Public License v2 or later. ZYpp is implemented mostly in the programming language C++.

**Zypper** is the native command-line interface of the ZYpp package manager to install, remove, update and query software packages of local or remote (networked) media. Its graphical equivalent is the YaST package manager module. It has been used in openSUSE since version 10.2 beta1. In openSUSE 11.1, Zypper reached version 1.0. Zypper is also part of the mobile Linux distributions MeeGo, Sailfish OS, and Tizen.

## History

### Purpose

Following its consecutive acquisitions of Ximian and SuSE GmbH in 2003, Novell decided to merge both package management systems, YaST package manager and Red Carpet, in a best of breed approach, as the two solutions so far were used at Novell. Looking at the extant open source tools and their maturity available back in 2005, none fulfilled the requirements, and were able to work smoothly with the extant Linux management infrastructure software developed by Ximian and SUSE, so it was decided to get the best ideas from extant pieces and to work on a new implementation. Libzypp, the resulting library, was planned to be the software management engine of the SUSE distributions and the Linux Management component of the Novell ZENworks Management suite.

### Early days

The Libzypp's solver was a port from the Red Carpet solver, which was written to update packages in installed systems. Using it for the full installing process brought it to its limits, and adding extensions such as support for weak dependencies and patches made it fragile and unpredictable. Although this first version of ZYpp's solver worked satisfactorily, on the company enterprise products with the coupled ZMD daemon, it led to an openSUSE 10.1 release which came out in May 2006 with a system package not working as expected. In December 2006, the openSUSE 10.2 release corrected some defects of the prior release, using the revisited ZYpp v2. ZMD was subsequently removed from the 10.3 release and reserved for only the company Enterprise products. While ZYpp v3 provided openSUSE with a relatively good package manager, equivalent to other existing package managers, it suffered from some flaws in its implementation which greatly limited its speed performance.

### SAT solver integration

An area where libzypp needed improvement was the speed of the dependency solver. libsolv is being written and released under the revised BSD license.

Projects like Optimal Package Install/Uninstall Manager (OPIUM) and MANCOOSI were trying to fix dependency solving issues with a SAT solver. Traditional solvers like Advanced Packaging Tool (APT) sometimes show unacceptable deficiencies. It was decided to integrate SAT algorithms into the ZYpp stack; the solver algorithms used were based on the popular minisat solver.

The SAT solver implementation as it appears in openSUSE 11.0 is based on two major, but independent, blocks:

- Using a data dictionary approach to store and retrieve package and dependency information. A new solv format was created, which stores a repository as a string dictionary, a relation dictionary and then all package dependencies. Reading and merging multiple solv repositories takes only milliseconds.
- Using satisfiability for computing package dependencies. The Boolean satisfiability problem is a well-researched problem with many exemplar solvers available. It is very fast, as package solving complexity is very low compared to other areas where SAT solvers are used. Also, it does not need complex algorithms and can provide understandable suggestions by calculating proof of why a problem is unsolvable.

After several months of work, the benchmark results of this fourth ZYpp version integrated with the SAT solver were more than encouraging, moving YaST and Zypper ahead of other RPM-based package managers in speed and size.

## Front ends

Typically, YaST has served as the graphical front end for ZYpp in SUSE. ZYpp is also supported by PackageKit. Starting in 2025 with openSUSE Leap 16.0, YaST was replaced by Myrlyn.
