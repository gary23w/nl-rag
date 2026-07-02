---
title: "runit"
source: https://en.wikipedia.org/wiki/Runit
domain: init-systems
license: CC-BY-SA-4.0
tags: init system, systemd manager, sysvinit scripts, process identifier
fetched: 2026-07-02
---

# runit

**runit** is an init and service management scheme for Unix-like operating systems that initializes, supervises, and ends processes throughout the operating system. Runit is a reimplementation of the daemontools process supervision toolkit that runs on many Linux-based operating systems, as well as BSD, and Solaris operating systems. Runit features parallelization of the start up of system services, which can speed up the boot time of the operating system.

When running as an init daemon, Runit is the direct or indirect ancestor of all other processes. It is the first process started during booting, and continues running until the system is shut down. It is often used with other init systems as a separate service manager. In the service manager role, it can be used by unprivileged users to orchestrate personal services, as well as by root to manage services not otherwise managed by the init system currently in use.

## Design

Runit focuses on being a small, modular, and portable codebase. In the init role, Runit is split into three stages: one time initialization, process supervision, and halting or rebooting. While the first and third stages must be adapted to the specific operating system they are running on, the second stage is portable across all POSIX compliant operating systems. The 3 stages can be configured through 3 executable files (they are usually shell scripts) named, respectively, 1, 2, and 3.

Stage 2 usually invokes a binary named runsvdir, which is the process responsible for global daemon management: for every daemon it finds in a folder passed to it by argument, it then spawns an individual watchdog, each of those starts a daemon (and a logger service eventually associated to it) and restarts it if it dies. In case a daemon is added or removed, it kills the watchdog or starts a new one. Executable files with specific names are used to describe the various phases of the daemon's life (run, check, finish, ...), it can intercept signals sent and run by specific scripts if they exist, and named pipes are created to expose interfaces to control the daemon.

## Usage

Runit can be used either as a drop-in replacement for sysvinit, or as a service supervisor (with sysvinit as the parent PID 1 process which runs processes specified by the inittab file, or some other init system). The RubyWorks stack of software able to run Ruby on Rails incorporated Runit into its suite.

### Adoption

Runit is the default init system of:

- antiX (Debian based, since version 19)
- Dragora GNU/Linux-Libre (since Dragora 2)
- Void Linux

Runit is an "officially" available init system for:

- Artix Linux (Arch based)
- Devuan (Debian based, since version 3.1.0)
- Gentoo Linux
- Hyperbola GNU/Linux-libre (Arch and Debian based)
