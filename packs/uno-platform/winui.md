---
title: "Windows UI Library"
source: https://en.wikipedia.org/wiki/WinUI
domain: uno-platform
license: CC-BY-SA-4.0
tags: uno platform, webassembly dotnet ui, pixel-perfect cross-platform, single codebase app
fetched: 2026-07-02
---

# Windows UI Library

(Redirected from

WinUI

)

**Windows UI Library** (**WinUI** codenamed "Jupiter", and also known as **UWP XAML** and **WinRT XAML**) is a user interface API that is part of the Windows Runtime programming model that forms the backbone of Universal Windows Platform apps (formerly known as *Metro-style* or *Immersive*) for the Windows 8, Windows 8.1, Windows 10 and Windows Phone 8.1 operating systems. It enables declaring user interfaces using Extensible Application Markup Language (XAML) technology.

WinUI is one of the multiple UI frameworks provided built-in for the Windows Runtime; the others being HTML5 (e.g., via WinJS) and DirectX.

WinUI 2 is an extension library for UWP XAML containing controls and styling that match the Windows 11 design language. It is shipped through NuGet and is distinct from the UWP XAML framework, which provides the actual rendering engine; though, they may be treated as synonyms.

WinUI 3 decouples WinRT XAML from the operating system as a separate package to be updated quickly and make new features work on older versions of Windows. It is part of Windows App SDK (codenamed "Project Reunion"), a Microsoft effort to reconcile the Windows desktop (Win32) and the UWP low IL app model.

## Windows Phone

Up to Windows Phone 8.0 WinRT XAML was not supported and XAML applications were based on Silverlight XAML and deployed in XAP format.

In Windows Phone 8.1 WinRT XAML is available along with improved Windows Runtime support. This convergence between platforms enable Universal apps that can target both Windows 8.1 and Windows Phone 8.1 while sharing most of the code, including user interface. The Windows Phone 8.1 is still capable of running Silverlight XAML apps and new features and API were also added to this too (called Silverlight 8.1)

WinUI is related to Windows Presentation Foundation (WPF) and Silverlight (WPF/E)—similar XAML-based UI frameworks used for desktop applications and portable applications respectively. WinUI uses a lot of the same names for its APIs as both of these older technologies—especially Silverlight, but its use is limited to the Windows (specifically Windows 8 and later) as with WPF. The major difference is that WPF and Silverlight are written in C# and require using .NET languages such as C# or Visual Basic, while WinRT XAML is part of the Windows Runtime, written in C++ and available to native code, and has tools for development, with C++/CX or C++/WinRT.
