---
title: "ASP.NET Core"
source: https://en.wikipedia.org/wiki/ASP.NET_Core
domain: aspnet-libs-dotnet
license: CC-BY-SA-4.0
tags: aspnet core, dotnet web framework, aspnet middleware, aspnet request pipeline
fetched: 2026-07-02
---

# ASP.NET Core

**ASP.NET Core** is an open-source modular web-application framework. It is a redesign of ASP.NET that unites the previously separate ASP.NET MVC and ASP.NET Web API into a single programming model. Despite being a new framework, built on a new web stack, it does have a high degree of concept compatibility with ASP.NET. The ASP.NET Core framework supports side-by-side versioning so that different applications being developed on a single machine can target different versions of ASP.NET Core. This was not possible with previous versions of ASP.NET. ASP.NET Core initially ran on both the Windows-only .NET Framework and the cross-platform .NET. However, support for the .NET Framework was dropped beginning with ASP.Net Core 3.0.

Blazor is a recent (optional) component to support WebAssembly and since version 5.0, it has dropped support for some old web browsers. While current Microsoft Edge works, the legacy version of it, i.e. "Microsoft Edge Legacy" and Internet Explorer 11 was dropped when you use Blazor.

## Release history

| Version number | Release date | End of support | Supported Visual Studio Version(s) |
|---|---|---|---|
| Unsupported: 1.0 | 2016-06-27 | 2019-06-27 | Visual Studio 2015, 2017 |
| Unsupported: 1.1 | 2016-11-18 | 2019-06-27 | Visual Studio 2015, 2017 |
| Unsupported: 2.0 | 2017-08-14 | 2018-10-01 | Visual Studio 2017 |
| Unsupported: 2.1 long-term support | 2018-05-30 | 2021-08-21 | Visual Studio 2017 |
| Unsupported: 2.2 | 2018-12-04 | 2019-12-23 | Visual Studio 2017 15.9 and 2019 16.0 preview 1 |
| Supported: 2.3 long-term support | 2025-01-14 | 2027-04-07 | Visual Studio 2017 |
| Unsupported: 3.0 | 2019-09-23 | 2020-03-03 | Visual Studio 2017 and 2019 |
| Unsupported: 3.1 long-term support | 2019-12-03 | 2022-12-03 | Visual Studio 2019 |
| Unsupported: 5.0 | 2020-11-10 | 2022-05-08 | Visual Studio 2019 16.8 |
| Unsupported: 6.0 long-term support | 2021-11-08 | 2024-11-08 | Visual Studio 2022 |
| Unsupported: 7.0 standard-term support | 2022-11-08 | 2024-05-14 | Visual Studio 2022 |
| Supported: 8.0 long-term support | 2023-11-14 | 2026-11-10 | Visual Studio 2022 |
| Supported: 9.0 standard-term support | 2024-11-12 | 2026-11-10 | Visual Studio 2022 |
| Latest version: 10.0 long-term support | 2025-11-11 | 2028-11-14 | Visual Studio 2026 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

**Notes:**

1. Supported on .NET Framework until 2025-01-14
2. Reshipped as ASP.NET Core 2.3
3. Supported on .NET Framework only

## Naming

Originally deemed **ASP.NET vNext**, the framework was going to be called **ASP.NET 5** when ready. However, in order to avoid implying it is an update to the existing ASP.NET framework, Microsoft later changed the name to ASP.NET Core at the 1.0 release.

## Features

- No-compile developer experience (i.e. compilation is continuous, so that the developer does not have to invoke the compilation command)
- Modular framework distributed as NuGet packages
- Cloud-optimized runtime (optimized for the internet)
- Host-agnostic via Open Web Interface for .NET (OWIN) support – runs in IIS or standalone
- A unified story for building web UI and web APIs (i.e. both the same)
- A cloud-ready environment-based configuration system
- A lightweight and modular HTTP request pipeline
- Build and run cross-platform ASP.NET Core apps on Windows, Mac, and Linux
- Open-source and community-focused
- Side-by-side app versioning when targeting .NET
- In-built support for dependency injection
- Enhanced Security compared to Asp.Net

## Components

- Entity Framework (EF) Core
- Identity Core
- MVC Core
- Razor Core
- SignalR
- Blazor
- Kestrel web server
