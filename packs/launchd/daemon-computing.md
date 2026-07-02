---
title: "Daemon (computing)"
source: https://en.wikipedia.org/wiki/Daemon_(computing)
domain: launchd
license: CC-BY-SA-4.0
tags: launchd daemon, macos init, service management, property list config
fetched: 2026-07-02
---

# Daemon (computing)

In computing, a **daemon** is a program that runs as a background process, rather than being under the direct control of an interactive user. Customary convention is to name a daemon process with the letter *d* as a suffix to indicate that it's a daemon. For example, syslogd is a daemon that implements system logging facility, and sshd is a daemon that serves incoming SSH connections.

Even though the concept can apply to many computing systems, the term *daemon* is used almost exclusively in the context of Unix-based systems. In other contexts, different terms are used for the same concept.

Systems often start daemons at boot time that will respond to network requests, hardware activity, or other programs by performing some task. Daemons such as cron may also perform defined tasks at scheduled times.

## Terminology

In the context of computing, the word is generally pronounced either as /ˈdiːmən/ *DEE-mən* or /ˈdeɪmən/ *DAY-mən*.

The term was coined by the programmers at MIT's Project MAC. According to Fernando J. Corbató, who worked on Project MAC around 1963, his team was the first to use the term daemon, inspired by Maxwell's demon, an imaginary agent in physics and thermodynamics that helped to sort molecules, stating, "We fancifully began to use the word daemon to describe background processes that worked tirelessly to perform system chores". Unix systems inherited this terminology. Maxwell's demon is consistent with Greek mythology's interpretation of a daemon as a supernatural being working in the background.

In the general sense, daemon is an older form of the word "demon", from the Greek δαίμων. In the *Unix System Administration Handbook* Evi Nemeth states the following about daemons:

> Many people equate the word "daemon" with the word "demon", implying some kind of satanic connection between UNIX and the underworld. This is an egregious misunderstanding. "Daemon" is actually a much older form of "demon"; daemons have no particular bias towards good or evil, but rather serve to help define a person's character or personality. The ancient Greeks' concept of a "personal daemon" was similar to the modern concept of a "guardian angel"—*eudaemonia* is the state of being helped or protected by a kindly spirit. As a rule, UNIX systems seem to be infested with both daemons and demons.

Alternative terms include *service* (used in Windows, from Windows NT onwards, and later also in Linux), *started task* (IBM z/OS), and *ghost job* (XDS UTS). Sometimes the more general term *server* or *server process* is used, particularly for daemons that operate as part of client-server systems. A daemon that connects to a computer network is a network service.

After the term was adopted for computer use, it was incorrectly rationalized as a backronym for **d**isk **a**nd **e**xecution **mon**itor.

## Implementations

### Unix-like systems

In a Unix-like system, the parent process of a daemon is often, but not always, the init process. A daemon is usually created either by the init process directly launching the daemon, by the daemon being run by an initialization script run by init, or by the daemon being launched by a super-server launched by init.

The init process in Research Unix and BSD starts daemons from an initialization script. A daemon started as a command in an initialization script must either fork a child process and then immediately exit, or must be run as a background process using &, so that the shell running the initialization script can continue after starting the daemon. In the former case, the daemon process run from the shell exits, thus causing init to adopt the child process that runs as the daemon; in the latter case, when the shell running the initialization script exits, the child daemon process is adopted by init.

The versions of init in System III and in System V can run arbitrary commands and can be configured to run them once or to restart them when they terminate. The former mechanism can be used to run initialization scripts; daemons started from those scripts behave the same as in Research Unix and BSD. The latter mechanism can be used to run daemons directly from init.

A daemon can also be launched from a user's command line. However, daemons launched in that fashion typically must perform other operations, such as dissociating the process from any controlling terminal (tty). Such procedures are often implemented in various convenience routines such as *daemon(3)*. A daemon launched by an initialization script need not do these steps, but doing so allows the daemon to be restarted by a user if it exits; init itself would not restart them. Operations such a daemon must do include:

- Optionally removing unnecessary variables from environment.
- Executing as a background task by forking and exiting (in the parent "half" of the fork). This allows daemon's parent (shell or startup process) to receive exit notification and continue its normal execution.
- Detaching from the invoking session, usually accomplished by a single operation, `setsid()`:
  - Dissociating from the controlling tty.
  - Creating a new session and becoming the session leader of that session.
  - Becoming a process group leader.
- If the daemon wants to ensure that it will not acquire a new controlling tty even by accident (which happens when a session leader without a controlling tty opens a free tty), it may fork and exit again. This means that it is no longer a session leader in the new session, and cannot acquire a controlling tty.
- Setting the root directory (/) as the current working directory so that the process does not keep any directory in use that may be on a mounted file system (allowing it to be unmounted).
- Changing the umask to 0 to allow `open()`, `creat()`, and other operating system calls to provide their own permission masks and not to depend on the umask of the caller.
- Redirecting file descriptors 0, 1 and 2 for the standard streams (stdin, stdout and stderr) to /dev/null or a logfile, and closing all the other file descriptors inherited from the parent process.

If the process is started by a super-server daemon, such as inetd, launchd, or systemd, the super-server daemon will perform those functions for the process, except for old-style daemons not converted to run under systemd and specified as Type=forking and "multi-threaded" datagram servers under inetd.

### MS-DOS

In MS-DOS, daemon-like functionality was implemented as a terminate-and-stay-resident program (TSR).

### Windows

In Windows, a Windows service provides the functionality of a daemon. It runs as a process, usually does not interact with the user (i.e. via monitor, keyboard, or mouse) and may be launched by the operating system at boot time. In Windows 2000 and later versions, a Windows service is configured and controlled via various interfaces including the Control Panel, the Service Control Manager `sc` command, the `net start` and `net stop` commands, PowerShell, or a custom program.

However, any Windows application can perform the role of a daemon, not just a service, and some Windows daemons have the option of running as a normal process.

### Mac

In classic Mac OS, optional features and services were provided by system extensions and control panels – files loaded at startup time that patched the operating system. Later versions of classic Mac OS augmented these with faceless background applications: regular applications that ran in the background. To the user, these were still described as regular system extensions.

The more modern macOS, which is Unix-based, uses daemons but uses the term "services" to designate software that performs functions selected from the Services menu, rather than using that term for daemons, as Windows does.
