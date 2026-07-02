---
title: "Windows Subsystem for Linux"
source: https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux
domain: wsl-subsystem
license: CC-BY-SA-4.0
tags: windows subsystem for linux, wsl subsystem, subsystem for android, windows terminal
fetched: 2026-07-02
---

# Windows Subsystem for Linux

**Windows Subsystem for Linux** (**WSL**) is a component of Microsoft Windows that allows the use of a Linux environment from within Windows, forgoing the overhead of a virtual machine and being an alternative to dual booting. The WSL command-line interface tool is installed by default in Windows 11, but a distribution must be downloaded and installed through it before use. In Windows 10, WSL can be installed either by joining the Windows Insider program or manually via Microsoft Store or Winget.

The original version, WSL 1, differs significantly from the second major version, WSL 2. WSL 1 (released August 2, 2016), acted as a compatibility layer for running Linux binary executables (in ELF format) by implementing Linux system calls in the Windows kernel. WSL 2 (announced May 2019), introduced a real Linux kernel – a managed virtual machine (via Hyper-V) that implements the full Linux kernel. As a result, WSL 2 is compatible with more Linux binaries as not all system calls were implemented in WSL 1. As of June 2026, WSL 1 is still maintained and supported.

Microsoft offers WSL for a variety of reasons. Microsoft envisions WSL as "a tool for developers – especially web developers and those who work on or with open source projects". Microsoft also claims that "WSL requires fewer resources (CPU, memory, and storage) than a full virtual machine" (a common alternative for using Linux in Windows), while also allowing the use of both Windows and Linux tools on the same set of files.

The majority of WSL was released as open source software on May 19, 2025, although certain filesystem functions still rely on a closed-source proprietary library as of September 2025.

## History

Microsoft's first foray into achieving Unix-like compatibility on Windows was the Microsoft POSIX subsystem, superseded by Windows Services for UNIX via MKS/Interix, which was eventually deprecated with the release of Windows 8.1. The technology behind Windows Subsystem for Linux originated in the unreleased Project Astoria, which enabled some Android applications to run on Windows 10 Mobile. It was first made available in Windows 10 Insider Preview build 14316.

Whereas Microsoft's prior projects and the third-party Cygwin had focused on creating their own unique Unix-like environments based on the POSIX standard, WSL aimed for native Linux compatibility. Instead of wrapping non-native functionality into Win32 system calls as Cygwin did, WSL's initial design (WSL 1) leveraged the NT kernel executive to serve Linux programs as special, isolated minimal processes (known as *"pico processes"*) attached to kernel mode *"pico providers"* as dedicated system call and exception handlers distinct from that of a vanilla NT process, opting to reutilize existing NT implementations wherever possible.

WSL beta was introduced in Windows 10 version 1607 (Anniversary Update) on August 2, 2016. Only Ubuntu (with Bash as the default shell) was supported. WSL beta was also called "Bash on Ubuntu on Windows" or "Bash on Windows". WSL was no longer beta in Windows 10 version 1709 (Fall Creators Update), released on October 17, 2017. Multiple Linux distributions could be installed and were available for install in the Windows Store.

Though the initial design of WSL was faster and more popular than the prior UNIX-on-Windows projects, Windows kernel engineers found difficulty in trying to increase WSL's performance and system call compatibility by trying to reshape the existing NT kernel to recognize and operate correctly on Linux's API. At a Microsoft Ignite conference in 2018, Microsoft engineers gave a high-level overview of a new "lightweight" Hyper-V VM technology for containerization where a virtualized kernel could make direct use of NT primitives on the host. In 2019, Microsoft announced a completely redesigned WSL architecture (WSL 2) using this lightweight VM technology hosting actual (customized) Linux kernel images, claiming to provide full syscall compatibility. Microsoft announced WSL 2 on May 6, 2019, and it was shipped with Windows 10 version 2004. It was also backported to Windows 10 version 1903 and 1909.

GPU support for WSL 2 to run GPU-accelerated machine learning was introduced in Windows build 20150. GUI support for WSL 2 to run Linux applications with graphical user interfaces (GUIs) was introduced in Windows build 21364. Both are shipped in Windows 11.

In April 2021, Microsoft released a Windows 10 test build that also includes the ability to run Linux graphical user interface (GUI) apps using WSL 2 and CBL-Mariner. The Windows Subsystem for Linux GUI (WSLg) was officially released at the Microsoft Build 2021 conference. It is included in Windows 10 Insider build 21364 or later.

On October 11, 2021, Microsoft introduced a version of WSL in the Microsoft Store for Windows 11. It reached version 1.0.0 in November 2022 with added support for Windows 10.

In November 2024, Microsoft announced new features coming to WSL intended to improve the experience for new users, including a window with new "getting started" navigation tips and explanations.

On May 19, 2025, during Build, Microsoft announced that the majority of WSL had been released as open source software, aside from a driver used by WSL 1, and the IFS network redirector drivers on WSL 2.

### Notable releases

| Release, feature | Preview build | Public build |
|---|---|---|
| WSL (Beta) (Bash on Ubuntu on Windows) | Windows 10 build 14316 | Windows 10 version 1607 (Anniversary Update) |
| WSL (no longer Beta) | Windows 10 build 16251 | Windows 10 version 1709 (Fall Creators Update) |
| WSL 2 (lightweight VM) | Windows 10 build 18917 | Windows 10 version 2004 (also backported to 1903 and 1909) |
| WSL 2 GPU support | Windows 10 build 20150 | Windows 11 (also Windows 10 21H2) |
| WSL 2 GUI support (WSLg) (last version) | Windows 10 build 21364 | Windows 11 |

| Version | Comment |
|---|---|
| 0.47.1 | First version |
| 0.67.6 | systemd support |
| 1.0.0 | Generally available; Windows 10 support |

## Features

The first release of WSL provides a Linux-compatible kernel interface developed by Microsoft, containing no Linux kernel code, which can then run the user space of a Linux distribution on it, such as Ubuntu, openSUSE, SUSE Linux Enterprise Server, Fedora, CentOS, AlmaLinux, Debian, and Kali Linux. Such a user space might contain a GNU Bash shell and command language, with native GNU command-line tools (sed, awk, etc.), programming-language interpreters (Ruby, Python, etc.), and even graphical applications (using an X11 server at the host side).

The architecture was redesigned in WSL 2, with a Linux kernel running in a lightweight virtual machine environment.

### wsl.exe

The `wsl.exe` command accesses and manages Linux distributions in WSL via command-line interface (CLI) – for example via Command Prompt or PowerShell. With no arguments it enters the default distribution shell. It can list available distributions, set a default distribution, and uninstall distributions. It can also run a Linux command – replacing `lxrun.exe` which is deprecated as of Windows 10 1803 and later.

### WSLg

Windows Subsystem for Linux GUI (WSLg) is built with the purpose of enabling support for running graphical X11 and Wayland applications on Windows in a fully integrated desktop experience. WSLg was officially released at the Microsoft Build 2021 conference and is included in Windows 10 Insider build 21364 or later. However, with the introduction of Windows 11, WSLg is finally shipping with a production build of Windows, bringing support for both graphics and audio in WSL apps. FreeRDP is used to encode all communications going from the Remote Desktop Protocol (RDP) Server (in Weston) to the RDP Client (msrdc on Windows) according to the RDP protocol specifications.

Prerequisites for running WSLg include:

- Windows 11 or Windows 10 Insider Preview builds 21362–21390.
- A system with virtual GPU (vGPU) enabled for WSL is recommended, as it will allow benefits from hardware accelerated OpenGL rendering.

## Design

### WSL 1

LXSS Manager Service is the service in charge of interacting with the subsystem (through the *drivers* `lxss.sys` and `lxcore.sys`), and the way that Bash.exe (not to be confused with the Shells provided by the Linux distributions) launches the processes, as well as handling the Linux system calls and the binary locks during their execution. All processes invoked by a particular user go into a so called "Linux Instance" (usually the first invoked process is init). Once all the applications are closed, the instance is closed.

WSL 1's design featured no hardware emulation / virtualization (unlike other projects such as coLinux) and made direct use of the host file system (through `VolFS` and `DrvFS`) and some parts of the hardware, such as the network, which guarantees interoperability. Web servers for example, can be accessed through the same interfaces and IP addresses configured on the host, and shares the same restrictions on the use of ports that require administrative permissions, or ports already occupied by other applications. There are certain locations (such as system folders) and configurations whose access/modification is restricted, even when running as root, with sudo from the shell. An instance with elevated privileges must be launched in order to get "sudo" to give administrator privileges, and allow such access.

WSL 1 is not capable of running all Linux software, such as 32-bit binaries, or those that require specific Linux kernel services not implemented in WSL. Due to a total lack of Linux in WSL 1, kernel modules, such as device drivers, cannot be run. WSL 2, however, makes use of live virtualized Linux kernel instances. It is possible to run some graphical (GUI) applications (such as Mozilla Firefox) by installing an X11 server within the Windows (host) environment (such as VcXsrv or Xming), although not without caveats, such as the lack of audio support (though this can be remedied by installing PulseAudio in Windows in a similar manner to X11) or hardware acceleration (resulting in poor graphics performance). Support for OpenCL and CUDA is also not being implemented currently, although planned for future releases. Microsoft stated WSL was designed for the development of applications, and not for desktop computers or production servers, recommending the use of virtual machines (Hyper-V), Kubernetes, and Azure for those purposes.

In benchmarks, WSL 1's performance is often near native Linux Ubuntu, Debian, Intel Clear Linux or other Linux distributions. I/O is in some tests a bottleneck for WSL. The redesigned WSL 2 backend is claimed by Microsoft to offer twenty-fold increases in speed on certain operations compared to that of WSL 1. In June 2020, a benchmark with 173 tests on WSL 2 (20H2) with an AMD Ryzen Threadripper 3970X showed an average of 87% of the performance of native Ubuntu 20.04 LTS. In contrast, WSL 1 had only 70% of the performance of native Ubuntu. WSL 2 improves I/O performance, providing a near-native level. A comparison of 69 tests with an Intel Core i9-10900K in May 2020 resulted in nearly the same relative performance. In December 2020, a benchmark with 43 tests on WSL 2 (20H2) with an AMD Ryzen 9 5900X displayed an average of 93% of the performance of native 20.04.1 LTS, compared to WSL 1 which only achieved 73%.

### WSL 2

Version 2 introduces changes in the architecture. Microsoft has opted for virtualization through a highly optimized subset of Hyper-V features, in order to run the kernel and distributions (based upon the kernel), promising performance equivalent to WSL 1. For backward compatibility, developers do not need to change anything in their published distributions. WSL 2 settings can be tweaked by the *WSL global configuration*, contained in an INI file named `.wslconfig` in the User Profile folder.

The distribution installation resides inside an ext4-formatted filesystem inside a virtual disk, and the host file system is transparently accessible through the 9P protocol, similarly to other virtual machine technologies like QEMU. For the users, Microsoft promised up to 20 times the read/write performance of WSL 1. From Windows an IFS network redirector is provided for Linux guest file access using the UNC path prefix of `\\wsl$`.

WSL 2 requires Windows 11, or Windows 10 version 1903 or higher, with Build 18362 or higher, for x64 systems, and Version 2004 or higher, with Build 19041 or higher, for ARM64 systems.

WSL 2 on Windows 11 retains 95% of the performance of native Ubuntu 20.04 LTS.

WSL 1 and WSL 2 both support IPv6 connections. IPv6 support in WSL 2 requires Windows 11 or newer.

## Reception and criticism

In 2017, free software movement founder Richard Stallman expressed concerns that integrating GNU functionality into Windows would hinder the development of free software, calling efforts like WSL "a step backward in the campaign for freedom."

In 2021, Jim Salter writing for *Ars Technica* called WSL "the best part of Windows 11," noting the ability to run applications with graphics and sound and install multiple distributions side-by-side.

WSL has most widely been described as a tool more useful to developers, rather than end users. Reviewers criticized some limitations, noting that it is not the same as having Linux, and that it suffers from some performance limitations, including slow disk I/O.
