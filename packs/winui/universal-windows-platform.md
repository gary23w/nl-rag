---
title: "Universal Windows Platform"
source: https://en.wikipedia.org/wiki/Universal_Windows_Platform
domain: winui
license: CC-BY-SA-4.0
tags: winui toolkit, fluent design controls, windows native ui, modern app controls
fetched: 2026-07-02
---

# Universal Windows Platform

**Universal Windows Platform** (**UWP**) is a computing platform created by Microsoft and introduced in Windows 10. The purpose of this platform is to help develop universal apps that run on Windows 10, Windows 10 Mobile (discontinued), Windows 11, Xbox One, Xbox Series X/S, and HoloLens without the need to be rewritten for each. It supports Windows app development using C++, C#, VB.NET, and XAML. The API is implemented in C++, and supported in C++, VB.NET, C#, F# and JavaScript. Designed as an extension to the Windows Runtime (WinRT) platform introduced in Windows Server 2012 and Windows 8, UWP allows developers to create apps that will potentially run on multiple types of devices.

UWP does not target non-Microsoft systems. Microsoft's solution for other platforms is .NET MAUI (previously "Xamarin.Forms"), an open-source API created by Xamarin, a Microsoft subsidiary since 2016. Community solutions also exist for non-targeted platforms, such as Uno Platform.

## Compatibility

UWP is a part of Windows 10, Windows 10 Mobile and Windows 11. UWP apps do not run on earlier Windows versions.

Apps that are capable of implementing this platform are natively developed using Visual Studio 2015, Visual Studio 2017, Visual Studio 2019, or Visual Studio 2022. Older Metro-style apps for Windows 8.1, Windows Phone 8.1, or for both (universal 8.1) need modifications to migrate to UWP.

Some Windows platform features in later versions have been exclusive to UWP and software specifically packaged for it, and are not usable in other architectures such as the existing WinAPI, WPF, and Windows Forms. However, as of 2019, Microsoft has taken steps to increase the parity between these application platforms and make UWP features usable inside non-UWP software. Microsoft introduced XAML Islands (a method for embedding UWP controls and widgets into non-UWP software) as part of the Windows 10 May 2019 update, and stated that it would also allow UWP functions and Windows Runtime components to be invoked within non-packaged software.

### API bridges

UWP Bridges translate calls in other application programming interfaces (APIs) to the UWP interface, so that applications written in these APIs would run on UWP. Two bridges are announced during the 2015 Build keynote for Android and iOS apps to be ported to Windows 10 Mobile. Until January 2022, Microsoft maintained support for bridges for Windows desktop apps, progressive web apps, Microsoft Silverlight, and iOS's Cocoa Touch API.

#### iOS

*Windows Bridge for iOS* (codenamed "Islandwood") is an open-source middleware toolkit that allows iOS apps developed in Objective-C to be ported to Windows 10 by using Visual Studio 2015 to convert the Xcode project into a Visual Studio project. An early build of Windows Bridge for iOS was released as open-source software under the MIT License on August 6, 2015, while the Android version was in closed beta.

This "WinObjC" project is open source on GitHub. It contains code from various existing implementations of Cocoa Touch like Cocotron and GNUstep as well as Microsoft's own code that implements iOS frameworks using UWP methods. It uses a version of the LLVM clang compiler.

#### Android

*Windows Bridge for Android* (codenamed "Astoria") was a runtime environment that would allow for Android apps written in Java or C++ to run on Windows 10 Mobile and published to Microsoft Store. Kevin Gallo, technical lead of Windows Developer Platform, explained that the layer contained some limitations: Google Mobile Services and certain core APIs are not available, and apps that have "deep integration into background tasks", such as messaging software, would not run well in this environment.

In February 2016, Microsoft announced that it had ceased development on Windows Bridge for Android, citing redundancies due to iOS already being a primary platform for multi-platform development, and that Windows Bridge for iOS produced native code and did not require an OS-level emulator. Instead, Microsoft encouraged the use of C# for multi-platform app development using tools from Xamarin, which they had acquired prior to the announcement. In 2021, Microsoft allowed Windows 11 to run Android apps with an OS-level emulator and allowed apps to be installed in the store.

## Deployment

UWP provides an application model based upon its CoreApplication class and the Windows Runtime (WinRT). Universal Windows apps that are created using the UWP no longer indicate having been written for a specific OS in their manifest build; instead, they target one or more device families, such as a PC, smartphone, tablet, or Xbox One, using Universal Windows Platform Bridges. These extensions allow the app to automatically utilize the capabilities that are available to the particular device it is currently running on. A universal app may run on either a mobile phone or a tablet and provide suitable experiences on each. A universal app running on a smartphone may start behaving the way it would if it were running on a PC when the phone is connected to a desktop computer or a suitable docking station.

## Reception

Games developed for UWP are subject to technical restrictions, including incompatibility with multi-video card setups, difficulties modding the game, overlays for gameplay-oriented chat clients, or key binding managers. UWP will only support DirectX 11.1 or later, so games built on older DirectX versions will not work. During Build 2016, Microsoft Xbox division head Phil Spencer announced that the company was attempting to address issues which would improve the viability of UWP for PC games, stating that Microsoft was "committed to ensuring we meet or exceed the performance expectations of full-screen games as well as the additional features including support for overlays, modding, and more." Support for AMD FreeSync and Nvidia G-Sync technologies, and disabling V-sync, was later added to UWP.

Epic Games founder Tim Sweeney criticized UWP for being a walled garden, since by default UWP software may only be published and installed via Windows Store, requiring changes in system settings to enable the installation of external software (similarly to Android). Additionally, certain operating system features are exclusive to UWP and cannot be used in non-UWP software such as most video games. Sweeney characterized these moves as "the most aggressive move Microsoft has ever made" in attempting to transform PCs into a closed platform, and felt that these moves were meant to put third-party games storefronts such as Steam at a disadvantage as Microsoft is "curtailing users' freedom to install full-featured PC software and subverting the rights of developers and publishers to maintain a direct relationship with their customers". As such, Sweeney argued that end-users should be able to download UWP software and install it in the same manner as non-UWP software.

Windows VP Kevin Gallo addressed Sweeney's concerns, stating that "in the Windows 10 November Update, we enabled people to easily side-load apps by default, with no UX required. We want to make Windows the best development platform regardless of technologies used, and offer tools to help developers with existing code bases of HTML/JavaScript, .NET and Win32, C++ and Objective-C bring their code to Windows, and integrate UWP capabilities. With Xamarin, UWP developers can not only reach all Windows 10 devices, but they can now use a large percentage of their C# code to deliver a fully native mobile app experiences for iOS and Android."

In a live interview with *Giant Bomb* during its E3 2016 coverage, Spencer defended the mixed reception of its UWP-exclusive releases, stating that "they all haven't gone swimmingly. Some of them have gone well", and that "there's still definitely concern that UWP and our store are somehow linked in a way that is nefarious. It's not." He also discussed Microsoft's relationships with third-party developers and distributors such as Steam, considering the service to be "a critical part of gaming's success on Windows" and stating that Microsoft planned to continue releasing games through the platform as well as its own, but that "There's going to be areas where we cooperate and there's going to be areas where we compete. The end result is better for gamers." Spencer also stated that he was a friend of Sweeney and had been in frequent contact with him.

On May 30, 2019, Microsoft announced that it would support distribution of Win32 games on Microsoft Store; Spencer (who had since been promoted to head of all games operations at Microsoft, reporting directly to CEO Satya Nadella) explained that developers preferred the architecture, and that it "allow[s] for the customization and control [developers and players] come to expect from the open Windows gaming ecosystem." It was also announced that future Xbox Game Studios releases on Windows would be made available on third-party storefronts such as Steam, rather than be exclusive to Microsoft Store.
