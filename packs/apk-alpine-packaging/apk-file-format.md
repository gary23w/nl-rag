---
title: "apk (file format)"
source: https://en.wikipedia.org/wiki/Apk_(file_format)
domain: apk-alpine-packaging
license: CC-BY-SA-4.0
tags: alpine package keeper, apk package format, musl libc, software repository
fetched: 2026-07-02
---

# apk (file format)

The **Android Package** with the file extension **apk** is a package format used by Android and a number of other Android-based operating systems for distribution and installation of mobile apps, mobile games and middleware. A file using this format can be built from source code written in either Java or Kotlin.

APK files can be generated and signed from Android App Bundles.

## Overview

APK is analogous to other software packages such as APPX in Microsoft Windows, APP for HarmonyOS or a Debian package in Debian-based operating systems. To make an APK file, a program for Android is first compiled using a tool such as Android Studio or Visual Studio and then all of its parts are packaged into one container file. An APK file contains all of a program's code (such as .dex files), resources, assets, certificates, and manifest file. As is the case with many file formats, APK files can have any desired name but, for the system to recognize them, the .apk filename suffix may be necessary.

Most Android implementations allow users to manually install APK files (sideloading) only after they turn on an "Unknown Sources" setting that allows installation from sources other than trusted ones such as Google Play. This may be done for many reasons, such as during the development of apps, to install apps not available on the store, or to install an older version of an app in the Play Store.

In 2026, Google announced that the "Unknown sources" toggle will be replaced with a process that involves enabling developer mode and a 24-hour pause before allowing sideloading from unverified developers. Verification requires an identity document and $25 payment.

## Use on other operating systems

The QNX-based BlackBerry 10 included an Android runtime environment; initially, apps were required to be packaged in the operating system's native format, and installed via the BlackBerry World app store or sideloading. Beginning on BlackBerry 10.2.1, the operating system added support for sideloading APK files directly.

At Build 2015, Microsoft announced an Android runtime environment for Windows 10 Mobile codenamed "Astoria" (later renamed *Windows Bridge for Android*), which would allow Android apps to run in an emulated environment with minimal changes, and have access to Microsoft platform APIs such as Bing Maps and Xbox Live as nearly drop-in replacements for equivalent Google Mobile Services. Google Mobile Services and certain core APIs would not be available, and apps with "deep integration into background tasks" were said to poorly support the environment. On February 25, 2016, after already having delayed it in November 2015, Microsoft announced that Windows Bridge for Android would be shelved, in favor of focusing on Windows Bridge for iOS (a native implementation of the iOS Objective-C APIs, which allows Xcode projects to be converted to Visual Studio projects targeting Windows platforms) and cross-platform development using the C# language instead. Portions of Astoria were used as a basis for Windows Subsystem for Linux (WSL) on the PC version of Windows 10.

On August 9, 2019, HarmonyOS came with APK compatibility via AOSP base with Linux kernel on HarmonyOS 1.0 for TVs and also June 2, 2021, HarmonyOS 2.0 version expanded to smartphones and tablets until Galaxy Edition version under HarmonyOS NEXT system for the next iterative HarmonyOS 5 beta to commercial version, starting in November 26, 2024 stable, officially dropping APK support.

In June 2021, Microsoft announced the "Windows Subsystem for Android" (WSA), an AOSP-based layer for sideloading Android apps on Windows 11. The software utilized a runtime compiler developed by Intel, and apps could be sideloaded, published via Microsoft Store, or obtained via an Amazon Appstore client. Microsoft deprecated and discontinued WSA in March 2025.

An APK file is a ZIP archive that usually contains the following files and directories:

- `META-INF` directory:
  - `MANIFEST.MF`: the Manifest file
  - The certificate of the application.
  - `CERT.SF`: The list of resources and a SHA-1 digest of the corresponding lines in the MANIFEST.MF file; for example:Signature-Version: 1.0 Created-By: 1.0 (Android) SHA1-Digest-Manifest: wxqnEAI0UA5nO5QJ8CGMwjkGGWE= ... Name: res/layout/exchange_component_back_bottom.xml SHA1-Digest: eACjMjESj7Zkf0cBFTZ0nqWrt7w= Name: res/drawable-hdpi/icon.png SHA1-Digest: DGEqylP8W0n0iV/ZzBx3MW0WGCA=
- `lib`: the directory containing the compiled code that is platform dependent, for example native libraries that can be loaded through JNI; the directory is split into more directories within it:
  - `armeabi-v7a`: compiled code for all ARMv7 and above based processors only
  - `arm64-v8a`: compiled code for all ARMv8 arm64 and above based processors only
  - `x86`: compiled code for x86 processors only
  - `x86_64`: compiled code for x86-64 processors only
  - `mips` and `armeabi`, deprecated since NDK r17
- `res`: the directory containing resources not compiled into `resources.arsc` (see below).
- `assets`: a directory containing applications assets, which can be retrieved by `AssetManager`.
- `AndroidManifest.xml`: An additional Android manifest file, describing the name, version, access rights, referenced library files for the application. This file may be in Android binary XML that can be converted into human-readable plaintext XML with tools such as AXMLPrinter2, Apktool M, or Androguard.
- `classes.dex`: The classes compiled in the dex file format executed by Android Runtime (or by Dalvik virtual machine used in Android 4.4 KitKat).
- `resources.arsc`: a file containing precompiled resources, such as binary XML, for example.
