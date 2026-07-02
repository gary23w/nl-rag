---
title: "Uptime"
source: https://en.wikipedia.org/wiki/Uptime
domain: synthetic-monitoring-deep
license: CC-BY-SA-4.0
tags: synthetic monitoring, scripted probe check, proactive uptime test, synthetic transaction
fetched: 2026-07-02
---

# Uptime

**Uptime** is a measure of system reliability, expressed as the period of time a machine, typically a computer, has been continuously working and available. Uptime is the opposite of downtime.

It is often used as a measure of computer operating system reliability or stability, in that this time represents the time a computer can be left unattended without crashing or needing to be rebooted for administrative or maintenance purposes.

Conversely, long uptime may indicate negligence, because some critical updates can require reboots on some platforms.

## Records

In 2005, Novell reported a server with a 6-year uptime. This level of uptime is common when servers are maintained under an industrial context and host critical applications such as banking systems.

Netcraft maintains the uptime records for many thousands of web hosting computers.

A server running Novell NetWare has been reported to have been shut down after 16 years of uptime due to a failing hard disk.

## Determining system uptime

### Unix-like systems (Linux, FreeBSD)

#### Using uptime

Most Unix-like systems including Linux, FreeBSD, Mac OS X, and SySVr4 have the *uptime* command. It also displays the system load averages for the past 1, 5, and 15-minute intervals:

```mw
user@Linux$ uptime
  18:17:07 up 68 days,  3:57,  6 users,  load average: 0.16, 0.07, 0.06
user@BSD$ uptime
3:01AM  up 69 days,  7:53, 0 users, load averages: 0.08, 0.07, 0.05
```

This command originated in 3.0BSD and has become ubiquitous among Unix systems ever since. Despite almost always providing the same collection of information and being so ubiquitous, it is not part of any Unix-related standard, neither SUS nor POSIX.

On Linux, an *uptime* command is part of GNU coreutils, BusyBox and Toybox.

On BSD, the *uptime* command is hard link to the *w* program. The *w* program is based on the RSTS/E, TOPS-10, and TOPS-20 SYSTAT program.

#### Using system-specific interfaces

Each Unix-like system also has its own private interfaces for obtaining the system uptime.

##### Linux

On Linux, several procfs files provide information on the system uptime. The main file is `/proc/uptime`, but `/proc/stat` provides related information too.

```mw
$ cat /proc/uptime
  350735.47 234388.90
```

The first number is the total number of seconds the system has been up. The second number is how much of that time the machine has spent idle, in seconds. On multi-core systems (and some Linux versions) the second number is the sum of the idle time accumulated by each CPU.

The C API for uptime information is `sysinfo()`.

##### BSD

On BSD systems and macOS (a combination of BSD and XNU parts), the uptime information is available from the sysctl system, both in the form of the *sysctl* command and the `sysctl()` C function. The sysctl entry is called `kern.boottime`, which provides boot time that can be converted to an uptime by subtracting it from the current time:

```mw
$ sysctl kern.boottime
kern.boottime: { sec = 1271934886, usec = 667779 } Thu Apr 22 12:14:46 2010
```

macOS also provides the uptime as `clock_gettime(CLOCK_MONOTONIC_RAW)`, a POSIX interface with implementation-defined starting point; macOS sets the starting point at system boot. `mach_timebase_info()` and `CACurrentMediaTime()` are additional ways to access the same raw monotonic clock.

On FreeBSD (but not macOS), the kernel exports three symbols that can be used as `extern` variables in C to obtain the boot time and uptime. They are called `boottime`, `time_second`, and `time_uptime`. These require no function call at all to use, unlike `sysctl()`. Higher-precision uptime is provided from functions such as `microuptime()`.

### Microsoft Windows

#### Windows Task Manager

Some versions of Microsoft Windows include an uptime field in Windows Task Manager, under the "Performance" tab. The format is D:HH:MM:SS (days, hours, minutes, seconds).

#### systeminfo

The output of the `systeminfo` command includes a "System Up Time" or "System Boot Time" field.

```mw
C:\>systeminfo | findstr "Time:"
System Up Time:            0 days, 8 hours, 7 minutes, 19 seconds
```

The exact text and format are dependent on the language and locale. The time given by `systeminfo` is not reliable. It does not take into account time spent in sleep or hibernation. Thus, the boot time will drift forward every time the computer sleeps or hibernates.

#### NET command

The `NET` command with its `STATISTICS` sub-command provides the date and time the computer started, for both the `NET STATISTICS WORKSTATION` and `NET STATISTICS SERVER` variants. The command `NET STATS SRV` is shorthand for `NET STATISTICS SERVER`. The exact text and date format is dependent on the configured language and locale.

```mw
C:\>NET STATISTICS WORKSTATION | findstr "since"
Statistics since 8/31/2009 8:52:29 PM
```

#### Windows Management Instrumentation (WMI)

Uptime can be determined via Windows Management Instrumentation (WMI), by querying the `LastBootUpTime` property of the `Win32_OperatingSystem` class. At the command prompt, this can be done using the `wmic` command:

```mw
C:\>wmic os get lastbootuptime
LastBootUpTime
20110508161751.822066+060
```

The timestamp uses the format `yyyymmddhhmmss.nnn`, so in the above example, the computer last booted up on 8 May 2011 at 16:17:51.822. The text "LastBootUpTime" and the timestamp format do not vary with language or locale. WMI can also be queried using a variety of application programming interfaces, including VBScript or PowerShell.

#### Uptime.exe

Microsoft formerly provided a downloadable utility called `Uptime.exe`, which reports elapsed time in days, hours, minutes, and seconds.

```mw
C:\>Uptime
SYSTEMNAME has been up for: 2 day(s), 4 hour(s), 24 minute(s), 47 second(s)
```

The time given by `Uptime.exe` is not reliable. It does not take into account time spent in sleep or hibernation. Thus, the boot time will drift forward every time the computer sleeps or hibernates.

### FreeDOS

The `uptime` command is also available for FreeDOS. The version was developed by M. Aitchison.

### OpenVMS

On OpenVMS systems, the `show system` command can be used at the DCL command prompt to obtain the system uptime. The first line of the resulting display includes the system's uptime, displayed as days followed by hours:minutes:seconds. In the following example, the command qualifier `/noprocess` suppresses the display of per-process detail lines of information.

```mw
$ show system/noprocess
OpenVMS V7.3-2 on node JACK 29-JAN-2008 16:32:04.67  Uptime  894 22:28:52
```

The command output above shows that node JACK on 29 January 2008 at 16:32:04.67 has an uptime of 894 days 22 hours 28 minutes and 52 seconds.
