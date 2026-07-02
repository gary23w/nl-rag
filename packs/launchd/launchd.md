---
title: "launchd"
source: https://en.wikipedia.org/wiki/Launchd
domain: launchd
license: CC-BY-SA-4.0
tags: launchd daemon, macos init, service management, property list config
fetched: 2026-07-02
---

# launchd

**launchd** is an init and operating system service management daemon created by Apple Inc. as part of macOS, iOS, iPadOS, watchOS, tvOS, and visionOS to replace its BSD-style init and SystemStarter. There have been efforts to port launchd to FreeBSD and derived systems.

## Components

There are two main programs in the launchd system: launchd and launchctl.

*launchd* manages the daemons at both a system and user level. Similar to xinetd, launchd can start daemons on demand. Similar to watchdogd, launchd can monitor daemons to make sure that they keep running. launchd also has replaced init as PID 1 on macOS and as a result it is responsible for starting the system at boot time.

Configuration files define the parameters of services run by launchd. Stored in the LaunchAgents and LaunchDaemons subdirectories of the Library folders, the property list-based files have approximately thirty different keys that can be set. launchd itself has no knowledge of these configuration files or any ability to read them - that is the responsibility of "launchctl".

*launchctl* is a command line application which talks to launchd using IPC and knows how to parse the property list files used to describe launchd jobs, serializing them using a specialized dictionary protocol that launchd understands. launchctl can be used to load and unload daemons, start and stop launchd controlled jobs, get system utilization statistics for launchd and its child processes, and set environment settings.

### launchd

launchd has two main tasks. The first is to boot the system, and the second is to load and maintain services.

Here is a simplified view of the Mac OS X Tiger system startup on a PowerPC Mac (on an Intel Mac, EFI replaces Open Firmware and `boot.efi` replaces BootX):

1. Open Firmware activates, initializes the hardware, and then loads BootX.
2. BootX loads the kernel, spins the pinwheel cursor, and loads any needed kernel extensions (kexts).
3. The kernel loads launchd.
4. launchd runs `/etc/rc`, various scripts which scan through `/System/Library/LaunchDaemons` and `/Library/LaunchDaemons`, calling launchctl on the plists as needed, then launchd starts the login window.

In step 4, the startup scripts scan through a few different directories for jobs to run. There are two different directories that are scanned:

1. The LaunchDaemons directories contain items that will run as root, generally background processes.
2. The LaunchAgents directories contain jobs, called agent applications, that will run as a user or in the context of userland. These may be scripts or other foreground items, and they can even include a user interface.

These directories are all kept in the typical Library directories of Mac OS X.

launchd is very different from SystemStarter in that it may not actually launch all the daemons at boot time. Key to launchd, and similar to xinetd, is the idea of launch-on-demand daemons. When launchctl scans through the job plists at boot time, it asks launchd to reserve and listen on all of the ports requested by those jobs. If so indicated in the plist by the "OnDemand" key, the daemon is not actually loaded at the time. Rather, launchd will listen on the port, start the daemon when needed, and shut it down when it is no longer needed. After a daemon is loaded, launchd will keep track of it and make sure it is running if needed. In this way it is like watchdogd, and shares watchdogd's requirement that processes do not attempt to fork or daemonize on their own. If a process goes into the background, launchd will lose track of it and attempt to relaunch it.

Mac OS X Tiger, consequently, boots much faster than previous releases. The system only has to register the daemons that are to run and does not actually launch them until they are needed. In fact, the progress bar that appears during boot time is just a placebo application (named WaitingForLoginWindow) that does not really show anything other than the passage of time.

The hardest part to manage during a launchd boot is dependencies. SystemStarter had a very simple system of dependencies that used the "Uses", "Requires", and "Provides" keys in the plist of a startup item. There are two main strategies when creating launchd dependencies on Tiger: IPC allows daemons to talk amongst themselves to work out dependencies, or daemons can watch files or paths for changes. Using IPC is much more subtle than the SystemStarter's keys and requires more work from the developer, but it may lead to cleaner and quicker startups. SystemStarter was still supported up to OS X Mountain Lion, but was removed in OS X Yosemite.

### launchctl

In launchd, control of services is centralized in the `launchctl` application.

Originally, launchctl could take commands from the command line, from the standard input, or operate in interactive mode. With superuser privileges, it allowed the user to make system-wide changes, and commands could be made permanent when stored in */etc/launchd.conf*. (A per-user *~/.launchd.conf* file appears to have been considered, but was never implemented.)

In later versions of macOS, interactive mode was removed, as was the ability to read commands from standard input, and the */etc/launchd.conf* file is no longer supported. The reason given for these changes is security considerations.

Today, launchctl works exclusively through command-line invocations and persistence is achieved through launchd .plist files in the appropriate locations (see below).

launchctl communicates with launchd via a Mach-specific IPC mechanism.

### Property list

A property list (plist) is a type of file that launchd uses for program configuration. When launchd scans a folder, or a job is submitted with launchctl, it reads a plist file that describes how the program is to be run.

A list of often used keys follows below. All keys are optional unless otherwise noted. For a full list, see Apple's manual page for `launchd.plist`.

| Key | Type | Description |
|---|---|---|
| `Label` | String | The name of the job. By convention, the job label is the same as the plist file name, without the *.plist* extension. **Required**. |
| `Program` | String | A path to an executable. Useful for simple launches. At least one of `Program` or `ProgramArguments` is **required**. |
| `ProgramArguments` | Array of strings | An array of strings representing a UNIX command. The first string is generally a path to an executable, while latter strings contain options or parameters. At least one of `Program` or `ProgramArguments` is **required**. |
| `UserName` | String (defaults to `root` or current user) | The job will be run as the given user, who may (or may not) be the user who submitted it to launchd. |
| `OnDemand` *(Deprecated since 10.5)* | Boolean (defaults to `YES`) | Deprecated as of 10.5 with the more powerful `KeepAlive` option. A Boolean flag that defines if a job runs continuously or not. |
| `RunAtLoad` | Boolean (defaults to `NO`) | A Boolean flag that defines if a task is launched immediately when the job is loaded into launchd. |
| `StartOnMount` | Boolean (defaults to `NO`) | A Boolean flag that defines if a task is launched when a new filesystem is mounted. |
| `QueueDirectories` | Array of strings | Watch a directory for new files. The directory must be empty to begin with, and must be returned to an empty state before `QueueDirectories` will launch its task again. |
| `WatchPaths` | Array of strings | Watch a filesystem path for changes. Can be a file or folder. |
| `StartInterval` | Integer | Schedules job to run on a repeating schedule. Indicates number of seconds to wait between runs. |
| `StartCalendarInterval` | Dictionary of integers *or* Array of dictionaries of integers | Job scheduling. The syntax is similar to cron. |
| `RootDirectory` | String | The job will be chrooted into this directory before execution. |
| `WorkingDirectory` | String | The job will be chdired into this directory before execution. |
| `StandardInPath`, `StandardOutPath`, `StandardErrorPath` | String | Keys to determine files for input and output for the launched process. |
| `LowPriorityIO` | Boolean | Tells the kernel that this task is of a low priority when doing filesystem I/O. |
| `AbandonProcessGroup` | Boolean (defaults to `NO`) | A Boolean flag that defines whether subprocesses launched from a task launched by launchd will be killed when the task ends. Useful where a short-lived task starts a long-lived subtask, but may result in zombie processes. |
| `SessionCreate` | Boolean (defaults to `NO`) | A Boolean flag that defines whether a security session will be created for the task and its subprocesses. |

## Socket activation protocol

The name of each key under Sockets will be placed into the environment of the job when it is run, and the file descriptor of that socket will be available in that environment variable. This differs from systemd's socket activation in that the name of a socket definition inside of the job configuration is hardcoded into the application. This protocol is less flexible, although it does not, as systemd does, require the daemon to hardcode a starting file descriptor (as of 2014, it is 3).

## History

The software was designed and programmed by Dave Zarzycki at Apple. The company planned for all of the following to be superseded in Mac OS X environments, of which most were with the release of Mac OS X v10.4 (Tiger):

- init
- rc
- init.d script
- rc.d script
- SystemStarter
- inetd / xinetd
- crond / atd
- watchdogd

In 2005, R. Tyler Croy ported launchd to FreeBSD as part of Google Summer of Code Project. It could not be run as PID 1 (only a session init), and it was not commonly used on that platform.

In 2006, the Ubuntu Linux distribution considered using launchd. The option was rejected because the source code was subject to the Apple Public Source License – described as an "inescapable licence problem". Ubuntu instead developed and switched to its own service management tool, Upstart.

In August 2006, Apple relicensed launchd under the Apache License, Version 2.0 in an effort to make adoption by other open source developers easier. Most Linux distributions use systemd or Upstart, or continue with init, and the BSDs also continue with init.

In December 2013, R. Tyler Croy announced his intent to resume work on his port of launchd to FreeBSD, and his "openlaunchd" GitHub repo subsequently rose in activity.

The last Wayback Machine capture of the Mac OS Forge area for launchd was in June 2012, and the most recent open source version from Apple was 842.92.1 in code for OS X 10.9.5.

In 2014, with OS X 10.10 and iOS 8, Apple moved code for launchd to closed source libxpc.

In August 2015 Jordan Hubbard and Kip Macy announced NextBSD, which is based on FreeBSD-CURRENT kernel while adding in Mach IPC, Libdispatch, notifyd, asld, launchd, and other components derived from Darwin, Apple's open-source code for OS X.

### Apple open source release history

| Version | License | Included in macOS versions | Included Apple Developer Tools versions |
|---|---|---|---|
| launchd-106 | Apple Public Source License | Mac OS X 10.4 |   |
| launchd-106.3 | Apple Public Source License | Mac OS X 10.4.2 Mac OS X 10.4.3 Mac OS X 10.4.4.ppc Mac OS X 10.4.5.ppc |   |
| launchd-106.10 | Apple Public Source License | Mac OS X 10.4.4.x86 Mac OS X 10.4.5.x86 |   |
| launchd-106.13 | Apple Public Source License | Mac OS X 10.4.6.ppc Mac OS X 10.4.6.x86 |   |
| launchd-106.14 | Apple Public Source License | Mac OS X 10.4.7.ppc Mac OS X 10.4.7.x86 Mac OS X 10.4.8.ppc Mac OS X 10.4.9.ppc Mac OS X 10.4.10.ppc Mac OS X 10.4.11.ppc |   |
| launchd-106.20 | Apple Public Source License | Mac OS X 10.4.8.x86 Mac OS X 10.4.9.x86 Mac OS X 10.4.10.x86 Mac OS X 10.4.11.x86 | Developer Tools 2.4 |
| launchd-152 | Apache License 2.0 |   |   |
| launchd-257 | Apache License 2.0 | Mac OS X 10.5 Mac OS X 10.5.1 | Developer Tools 3.1 Developer Tools 3.1b Developer Tools 3.1.1 Developer Tools 3.1.2 Developer Tools 3.1.3 Developer Tools 3.1.4 |
| launchd-258.1 | Apache License 2.0 | Mac OS X 10.5.2 |   |
| launchd-258.12 | Apache License 2.0 | Mac OS X 10.5.3 Mac OS X 10.5.4 |   |
| launchd-258.18 | Apache License 2.0 | Mac OS X 10.5.5 |   |
| launchd-258.19 | Apache License 2.0 | Mac OS X 10.5.6 |   |
| launchd-258.22 | Apache License 2.0 | Mac OS X 10.5.7 |   |
| launchd-258.25 | Apache License 2.0 | Mac OS X 10.5.8 |   |
| launchd-328 | Apache License 2.0 | Mac OS X 10.6 Mac OS X 10.6.1 Mac OS X 10.6.2 | Developer Tools 3.2.1 Developer Tools 3.2.2 Developer Tools 3.2.3 Developer Tools 3.2.4 |
| launchd-329.3 | Apache License 2.0 | Mac OS X 10.6.3 |   |
| launchd-329.3.1 | Apache License 2.0 | Mac OS X 10.6.4 | Developer Tools 3.2.5 Developer Tools 3.2.6 |
| launchd-329.3.2 | Apache License 2.0 | Mac OS X 10.6.5 |   |
| launchd-329.3.3 | Apache License 2.0 | Mac OS X 10.6.6 Mac OS X 10.6.7 Mac OS X 10.6.8 |   |
| launchd-392.18 | Apache License 2.0 | Mac OS X 10.7 Mac OS X 10.7.1 |   |
| launchd-392.35 | Apache License 2.0 | Mac OS X 10.7.2 |   |
| launchd-392.36 | Apache License 2.0 | Mac OS X 10.7.3 |   |
| launchd-392.38 | Apache License 2.0 | Mac OS X 10.7.4 |   |
| launchd-392.39 | Apache License 2.0 | Mac OS X 10.7.5 |   |
| launchd-442.21 | Apache License 2.0 | Mac OS X 10.8 Mac OS X 10.8.1 |   |
| launchd-442.26.2 | Apache License 2.0 | Mac OS X 10.8.2 Mac OS X 10.8.3 Mac OS X 10.8.4 Mac OS X 10.8.5 |   |
| launchd-842.1.4 | Apache License 2.0 | OS X 10.9 OS X 10.9.1 |   |
| launchd-842.90.1 | Apache License 2.0 | OS X 10.9.2 OS X 10.9.3 |   |
| launchd-842.92.1 | Apache License 2.0 | OS X 10.9.4 OS X 10.9.5 |   |
