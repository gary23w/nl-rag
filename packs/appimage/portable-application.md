---
title: "Portable application"
source: https://en.wikipedia.org/wiki/Portable_application
domain: appimage
license: CC-BY-SA-4.0
tags: appimage format, portable application, self-extracting archive, software deployment
fetched: 2026-07-02
---

# Portable application

A **portable application** (**portable app**), sometimes also called standalone software, is a computer program designed to operate without changing other files or requiring other software to be installed. In this way, it can be easily added to, run, and removed from any compatible computer without setup or side-effects.

In practical terms, a portable application often stores user-created data and configuration settings in the same directory it resides in. This makes it easier to transfer the program with the user's preferences and data between different computers. A program that doesn't have any configuration options can also be a portable application.

Portable applications can be stored on any data storage device, including internal mass storage, a file share, cloud storage or external storage such as USB drives, pen drives and floppy disks—storing its program files and any configuration information and data on the storage medium alone. If no configuration information is required a portable program can be run from read-only storage such as CD-ROMs and DVD-ROMs. Some applications are available in both installable and portable versions.

Some applications which are not portable by default do support optional portability through other mechanisms, the most common being command-line arguments. Examples might include `/portable` to simply instruct the program to behave as a portable program, or `--cfg=/path/inifile` to specify the configuration file location.

Like any application, portable applications must be compatible with the computer system hardware and operating system.

Depending on the operating system, *portability* is more or less complex to implement; to operating systems such as AmigaOS, all applications are by definition portable.

## Portable Windows applications

Most portable applications do not leave files or settings on the host computer or modify the existing system and its configuration. The application may not write to the Windows registry or store its configuration files (such as an INI file) in the user's profile, but today, many portables do; many, however, still store their configuration files in the portable directory. Another possibility, since file paths will often differ on changing computers due to variation in drive letter assignments, is that portable applications may store them in a *relative* format. While some applications have options to support this behavior, many programs are not designed to do this. A common technique for such programs is the use of a launcher program to copy necessary settings and files to the host computer when the application starts and move them back to the application's directory when it closes.

An alternative strategy for achieving application portability within Windows, without requiring application source code changes, is application virtualization: An application is "sequenced" or "packaged" against a runtime layer that transparently intercepts its file system and registry calls, then redirects these to other persistent storage without the application's knowledge. This approach leaves the application itself unchanged, yet portable.

The same approach is used for individual application components: run-time libraries, COM components or ActiveX, not only for the entire application. As a result, when individual components are ported in such manner they are able to be: integrated into original portable applications, repeatedly instantiated (virtually installed) with different configurations/settings on the same operating system (OS) without mutual conflicts. As the ported components do not affect the OS-protected related entities (registry and files), the components will not require administrative privileges for installation and management.

Microsoft saw the need for an application-specific registry for its Windows operating system as far back as 2005. It eventually incorporated some of this technology, using the techniques mentioned above, via its Application Compatibility Database using its Detours code library, into Windows XP. It did not make any of this technology available via its system APIs.

## Portability on Unix-like systems

Programs written with a Unix-like base in mind often do not make any assumptions. Whereas many Windows programs assume the user is an administrator—something very prevalent in the days of Windows 95/98/ME (and to some degree in Windows XP/2000, though not in Windows Vista or Windows 7)—such would quickly result in "Permission denied" errors in Unix-like environments since users will be in an unprivileged state much more often. Programs are therefore generally designed to use the `HOME` environment variable to store settings (e.g. `*$HOME*/.w3m` for the w3m browser). The dynamic linker provides an environment variable `LD_LIBRARY_PATH` that programs can use to load libraries from non-standard directories. Assuming `/mnt` contains the portable programs and configuration, a command line may look like:

`HOME=/mnt/home/user LD_LIBRARY_PATH=/mnt/usr/lib /mnt/usr/bin/w3m www.example.com`

A Linux application without need for a user-interaction (e.g. adapting a script or environment variable) on varying directory paths can be achieved with the GCC linker option `$ORIGIN` which allows a relative library search path.

Not all programs honor this—some completely ignore $HOME and instead do a user look-up in `/etc/passwd` to find the home directory, therefore thwarting portability.

There are also cross-distro package formats that do not require admin rights to run, like Autopackage, AppImage, or CDE, but which gained only limited acceptance and support in the Linux community in the 2000s. Around 2015 the idea of portable and distro independent packing for the Linux ecosystem got more traction when Linus Torvalds discussed this topic on the DebConf 2014 and endorsed later AppImage for his dive log application Subsurface. For instance, MuseScore and Krita followed in 2016 and started to use AppImage builds for software deployment. RedHat released in 2016 the Flatpak system, which is a successor of Alexander Larsson's *glick* project which was inspired by klik (now called AppImage). Similarly, Canonical released in 2016 Snap packages for Ubuntu and many other Linux distros.

Many Mac applications that can be installed by drag-and-drop are inherently portable as Mac application bundles. Examples include Mozilla Firefox, Skype and Google Chrome which do not require admin access and do not need to be placed into a central, restricted area. Applications placed into `/Users/username/Applications` (`~/Applications`) are registered with macOS LaunchServices in the same way as applications placed into the main `/Applications` folder. For example, right-clicking a file in Finder and then selecting "Open With..." will show applications available from both /Applications and ~/Applications. Developers can create Mac product installers which allow the user to perform a home directory install, labelled "Install for me only" in the Installer user interface. Such an installation is performed as the user.
