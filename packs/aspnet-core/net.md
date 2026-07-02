---
title: ".NET"
source: https://en.wikipedia.org/wiki/.NET
domain: aspnet-core
license: CC-BY-SA-4.0
tags: asp.net core, asp.net mvc, dotnet web, razor pages
fetched: 2026-07-02
---

# .NET

The **.NET** platform (pronounced as "*dot net"*; formerly named **.NET Core**) is a free and open-source, managed computer software framework for Windows, Linux, and macOS operating systems. It is a cross-platform successor to the .NET Framework. The project is mainly developed by Microsoft employees by way of the .NET Foundation and is today released under an MIT License.

New versions of the .NET platform are released annually, typically in November. The most recent version of .NET is .NET 10, released in November 2025, which is a long-term support (LTS) version, and is scheduled to receive updates until November 2028.

## History

In the late 1990s, Microsoft began developing a managed code runtime and programming language (C#) which it billed together as part of the ".NET platform", with the core runtime and software libraries comprising the .NET Framework.

> At the heart of the .NET Platform is the .NET Framework, a high-productivity, multilanguage development and execution environment for building and running Web services with important features such as cross-language inheritance and debugging.

Soon after the announcement of the C# language at the Professional Developers Conference in 2000 and previews of its software became available, Microsoft began a standardization effort through ECMA for what it dubbed the Common Language Infrastructure. The company continued development and support of its own implementation as proprietary, closed source software in the meantime.

On November 12, 2014, Microsoft introduced **.NET Core**—an open-source, cross-platform successor to .NET Framework—and released source code for the .NET Core CoreCLR implementation, source for the "entire [...] library stack" for .NET Core, and announced the adoption of a conventional ("bazaar"-like) open-source development model under the stewardship of the .NET Foundation. Miguel de Icaza describes .NET Core as a "redesigned version of .NET that is based on the simplified version of the class libraries", and Microsoft's Immo Landwerth explained that .NET Core would be "the foundation of all future .NET platforms". At the time of the announcement, the initial release of the .NET Core project had been seeded with a subset of the libraries' source code and coincided with the relicensing of Microsoft's existing .NET reference source away from the restrictions of the Ms-RSL. Landwerth acknowledged the disadvantages of the formerly selected shared license, explaining that it made codename Rotor "a non-starter" as a community-developed open source project because it did not meet the criteria of an Open Source Initiative (OSI) approved license.

.NET Core 1.0 was released on June 27, 2016, along with Microsoft Visual Studio 2015 Update 3, which enables .NET Core development. .NET Core 1.0.4 and .NET Core 1.1.1 were released along with .NET Core Tools 1.0 and Visual Studio 2017 on March 7, 2017.

.NET Core 2.0 was released on August 14, 2017, along with Visual Studio 2017 15.3, ASP.NET Core 2.0, and Entity Framework Core 2.0. .NET Core 2.1 was released on May 30, 2018. NET Core 2.2 was released on December 4, 2018.

.NET Core 3 was released on September 23, 2019. NET Core 3 adds support for Windows desktop application development and significant performance improvements throughout the base library.

In November 2020, Microsoft released .NET 5.0. The "Core" branding was abandoned and version 4.0 was skipped to avoid conflation with .NET Framework, of which the latest releases had all used 4.x versioning for all significant (non-bugfix) releases since 2010.

| Version | Release date | Released with | Latest update | Latest update date | Support ends | Support Lifetime |
|---|---|---|---|---|---|---|
| Unsupported: .NET Core 1.0 | June 27, 2016 | Visual Studio 2015 Update 3 | 1.0.16 | May 14, 2019 | June 27, 2019 | 3 years |
| Unsupported: .NET Core 1.1 | November 16, 2016 | Visual Studio 2017 Version 15.0 | 1.1.13 | May 14, 2019 | June 27, 2019 | 2.5 years |
| Unsupported: .NET Core 2.0 | August 14, 2017 | Visual Studio 2017 Version 15.3 | 2.0.9 | July 10, 2018 | October 1, 2018 | 1.25 years |
| Unsupported: .NET Core 2.1 | May 30, 2018 | Visual Studio 2017 Version 15.7 | 2.1.30 (LTS) | August 19, 2021 | August 21, 2021 | 3.25 years |
| Unsupported: .NET Core 2.2 | December 4, 2018 | Visual Studio 2019 Version 16.0 | 2.2.8 | November 19, 2019 | December 23, 2019 | 0.9 years |
| Unsupported: .NET Core 3.0 | September 23, 2019 | Visual Studio 2019 Version 16.3 | 3.0.3 | February 18, 2020 | March 3, 2020 | 0.5 years |
| Unsupported: .NET Core 3.1 | December 3, 2019 | Visual Studio 2019 Version 16.4 | 3.1.32 (LTS) | December 13, 2022 | December 13, 2022 | 3 years |
| Unsupported: .NET 5 | November 10, 2020 | Visual Studio 2019 Version 16.8 | 5.0.17 | May 10, 2022 | May 10, 2022 | 1.5 years |
| Unsupported: .NET 6 | November 8, 2021 | Visual Studio 2022 Version 17.0 | 6.0.36 (LTS) | November 12, 2024 | November 12, 2024 | 3 years |
| Unsupported: .NET 7 | November 8, 2022 | Visual Studio 2022 Version 17.4 | 7.0.20 | May 28, 2024 | May 14, 2024 | 1.5 years |
| Supported: .NET 8 | November 14, 2023 | Visual Studio 2022 Version 17.8 | 8.0.23 (LTS) | January 13, 2026 | November 10, 2026 | 3 years |
| Supported: .NET 9 | November 12, 2024 | Visual Studio 2022 Version 17.12 | 9.0.12 | January 13, 2026 | November 10, 2026 | 2 years |
| Latest version: .NET 10 | November 11, 2025 | Visual Studio 2026 Version 18.0 | 10.0.2 (LTS) | January 13, 2026 | November 14, 2028 | 3 years |
| Preview version: .NET 11 | November 2026 (projected) |   |   |   | November 2028 (projected) | 2 years (projected) |
| Future version: .NET 12 | November 2027 (projected) |   | (LTS) |   | November 2030 (projected) | 3 years (projected) |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |   |   |

### Versioning practice

.NET Core Runtime roughly uses semantic versioning, the *major.minor.patch* format. Major versions are incremented with "significant changes", API-breaking changes, or with the major version increase in an existing dependency. It should happen yearly. Minor versions are incremented with the addition of API features, dependencies, or with the minor version increase in an existing dependency. Patch versions are given for bug fixes, new platform support, or other changes not included above. As of 2019, runtime versions are backwards-compatible within the same major version number. For example, .NET Core 2.2 is able to run programs built for .NET Core 2.1. Runtime versions in the same minor version. This appears to have relaxed since .NET 5. A "roll-forward" behavior allows any .NET program to be run on any newer version given the correct settings.

The SDK does not use semantic versioning. As of 2019, it supports targeting *every* runtime version prior to its maximum supported version. As of 2020, this extends down to .NET Framework runtimes as well, though downloading an additional "targeting pack" from NuGet may be necessary. The major and minor versions of an SDK always matches the major and minor versions of the runtime it contains or is aligned for.

### OS and architecture support

Alpine Linux, which primarily supports and uses musl libc, is supported since .NET Core 2.1.

Windows Arm64 is natively supported since .NET 5. Previously, .NET on ARM meant applications compiled for the x86 architecture and run through the ARM emulation layer.

Linux .NET runs on Power ISA to some extent since .NET 7, officially no support is claimed by Microsoft but .NET does contain code for Power ISA compatibility for Linux systems and is able to be compiled for Power ISA systems specifically 64 bit Little Endian variant.

## Language support

.NET fully supports C# and F# (and C++/CLI as of 3.1; only enabled on Windows) and supports Visual Basic .NET (for version 15.5 in .NET Core 5.0.100-preview.4, and some old versions supported in old .NET Core).

VB.NET compiles and runs on .NET, but as of .NET Core 3.1, the separate Visual Basic Runtime is not implemented. Microsoft initially announced that .NET Core 3 would include the Visual Basic Runtime, but after two years the timeline for such support was updated to .NET 5.

## Architecture

.NET supports the following cross-platform scenarios: ASP.NET Core web apps, command-line/console apps, libraries and Universal Windows Platform apps. Prior to .NET Core 3.0, it did not implement Windows Forms or Windows Presentation Foundation (WPF), which render the standard GUI for desktop software on Windows. However, from .NET Core 3 on, it started implementing them along with Universal Windows Platform (UWP). It was also possible to write cross-platform graphical applications using .NET with the GTK# language-binding for the GTK widget toolkit, but this binding has not been maintained for many years.

.NET supports use of NuGet packages. Unlike .NET Framework, which is serviced using Windows Update, .NET used to rely on its package manager to receive updates. Since December 2020, however, .NET updates started being delivered via Windows Update as well.

NuGet serves as the primary distribution mechanism for libraries and tools in the .NET ecosystem, including third-party components that extend core functionality. Among these are ADO.NET-compatible data providers, which offer database connectivity for systems beyond the default SQL Server support. These providers enable direct access to databases such as Oracle, MySQL, PostgreSQL, and others, and are commonly used in applications that require cross-platform data access, integration with ORM technologies, or support for specific database features.

The two main components of .NET are CoreCLR and CoreFX, which are comparable to the Common Language Runtime (CLR) and the Framework Class Library (FCL) of the .NET Framework's Common Language Infrastructure (CLI) implementation.

As an implementation of CLI's Virtual Execution System (VES), CoreCLR is a complete runtime and virtual machine for managed execution of CLI programs and includes a just-in-time compiler called RyuJIT. .NET Core also contains CoreRT, the .NET Native runtime optimized to be integrated into AOT compiled native binaries.

As an implementation of CLI's Standard Libraries, CoreFX shares a subset of .NET Framework APIs, however, it also comes with its own APIs that are not part of the .NET Framework. A variant of the .NET library is used for UWP.

The .NET command-line interface offers an execution entry point for operating systems and provides developer services like compilation and package management.

## .NET MAUI

**.NET Multi-platform App UI** (**.NET MAUI**, introduced with .NET 6) is a cross-platform framework for creating native mobile and desktop apps with C# and Extensible Application Markup Language (XAML), which also supports Android, iOS, macOS, Windows and Tizen.

## Mascot

The official community mascot of .NET is the .NET Bot (stylized as "dotnet bot" or "dotnet-bot"). The dotnet bot served as the placeholder developer for the initial check-in of the .NET source code when it was open-sourced. It has since been used as the official mascot.
