---
title: "DTrace"
source: https://en.wikipedia.org/wiki/DTrace
domain: freebsd-os
license: CC-BY-SA-4.0
tags: freebsd, berkeley software distribution, freebsd jail, dtrace
fetched: 2026-07-02
---

# DTrace

**DTrace** is a comprehensive dynamic tracing framework originally created by Sun Microsystems for troubleshooting kernel and application problems on production systems in real time. Originally developed for Solaris, it has since been released under the free Common Development and Distribution License (CDDL) in OpenSolaris and its descendant illumos, and has been ported to several other Unix-like systems. Windows Server systems from Windows Server 2025 will have DTrace as part of the system.

DTrace can be used to get a global overview of a running system, such as the amount of memory, CPU time, filesystem and network resources used by the active processes. It can also provide much more fine-grained information, such as a log of the arguments with which a specific function is being called, or a list of the processes accessing a specific file.

In 2010, Oracle Corporation acquired Sun Microsystems and announced the discontinuation of OpenSolaris. As a community effort of some core Solaris engineers to create a truly open source Solaris, illumos operating system was announced via webinar on Thursday, 3 August 2010, as a fork on OpenSolaris OS/Net consolidation, including DTrace technology.

In October 2011, Oracle announced the porting of DTrace to Linux, and in 2019 official DTrace for Fedora is available on GitHub. For several years an unofficial DTrace port to Linux was available, with no changes in licensing terms.

In August 2017, Oracle released DTrace kernel code under the GPLv2+ license, and user space code under GPLv2 and UPL licensing. In September 2018 Microsoft announced that they had ported DTrace from FreeBSD to Windows.

In September 2016 the OpenDTrace effort began on GitHub with both code and comprehensive documentation of the system's internals. The OpenDTrace effort maintains the original CDDL licensing for the code from OpenSolaris with additional code contributions coming under a BSD 2 Clause license. The goal of OpenDTrace is to provide an OS agnostic, portable implementation of DTrace that is acceptable to all consumers, including macOS, FreeBSD, OpenBSD, NetBSD, and Linux as well as embedded systems.

## Description

Sun Microsystems designed DTrace to give operational insights that allow users to tune and troubleshoot applications and the OS itself.

Testers write tracing programs (also referred to as scripts) using the D programming language (not to be confused with other programming languages named "D"). The language, inspired by C, includes added functions and variables specific to tracing. D programs resemble AWK programs in structure; they consist of a list of one or more *probes* (instrumentation points), and each probe is associated with an action. These probes are comparable to a pointcut in aspect-oriented programming. Whenever the condition for the probe is met, the associated action is executed (the probe "fires"). A typical probe might fire when a certain file is opened, or a process is started, or a certain line of code is executed. A probe that fires may analyze the run-time situation by accessing the call stack and context variables and evaluating expressions; it can then print out or log some information, record it in a database, or modify context variables. The reading and writing of context variables allows probes to pass information to each other, allowing them to cooperatively analyze the correlation of different events.

Special consideration has been taken to make DTrace safe to use in a production environment. For example, there is minimal probe effect when tracing is underway, and no performance impact associated with any disabled probe; this is important since there are tens of thousands of DTrace probes that can be enabled. New probes can also be created dynamically.

## Command line examples

DTrace scripts can be invoked directly from the command line, providing one or more probes and actions as arguments. Some examples:

```mw
# New processes with arguments
dtrace -n 'proc:::exec-success { trace(curpsinfo->pr_psargs); }'

# Files opened by process
dtrace -n 'syscall::open*:entry { printf("%s %s",execname,copyinstr(arg0)); }'

# Syscall count by program
dtrace -n 'syscall:::entry { @num[execname] = count(); }'

# Syscall count by syscall
dtrace -n 'syscall:::entry { @num[probefunc] = count(); }'

# Syscall count by process
dtrace -n 'syscall:::entry { @num[pid,execname] = count(); }'

# Disk size by process
dtrace -n 'io:::start { printf("%d %s %d",pid,execname,args[0]->b_bcount); }'

# Pages paged in by process
dtrace -n 'vminfo:::pgpgin { @pg[execname] = sum(arg0); }'
```

Scripts can also be written which can reach hundreds of lines in length, although typically only tens of lines are needed for advanced troubleshooting and analysis. Over 200 examples of open source DTrace scripts can be found in the DTraceToolkit, created by Brendan Gregg (author of the DTrace book), which also provides documentation and demonstrations of each.

## Supported platforms

DTrace first became available for use in November 2003, and was formally released as part of Sun's Solaris 10 in January 2005. DTrace was the first component of the OpenSolaris project to have its source code released under the Common Development and Distribution License (CDDL).

DTrace is an integral part of illumos and related distributions.

DTrace is a standard part of FreeBSD and NetBSD.

Apple added DTrace support in Mac OS X 10.5 "Leopard", including a GUI called Instruments. Over 40 DTrace scripts from the DTraceToolkit are included in /usr/bin, including tools to examine disk I/O (iosnoop) and process execution (execsnoop). Unlike other platforms that DTrace is supported on, Mac OS X has a flag (P_LNOATTACH) that a program may set that disallows tracing of that process by debugging utilities such as DTrace and gdb. In the original Mac OS X DTrace implementation, this could affect tracing of other system information, as unrelated probes that should fire while a program with this flag set was running would fail to do so. The OS X 10.5.3 update addressed this issue a few months later. However, since El Capitan, System Integrity Protection prevents user from DTracing protected binary by default.

The Linux port of DTrace has been available since 2008; work continues actively to enhance and fix issues. There is also an active implementation on github. Standard core providers are available (fbt, syscall, profile), plus a special "instr" provider (some of the Solaris providers are not yet available as of 2013). The Linux DTrace implementation is a loadable kernel module, which means that the kernel itself requires no modification, and thus allows DTrace to avoid CDDL vs. GPL licensing conflicts (in its source form, at least). However, once DTrace is loaded the kernel instance will be marked as tainted.

In 2007, a developer at QNX Software Systems announced on his blog that he and a colleague were working on incorporating DTrace into the QNX operating system.

Oracle Corporation added beta DTrace support for Oracle Linux in 2011, as a technology preview in the Unbreakable Enterprise Kernel release 2, which is under GPLv2 (the DTrace Linux kernel module was originally released under CDDL). General availability was announced in December 2012.

On March 11, 2019, Microsoft released a version of DTrace for Windows 10 insider builds. Microsoft included DTrace as a built-in tool in Windows Server 2025.

## Language and application providers

With a supported *language provider*, DTrace can retrieve context of the code, including function, source file, and line number location. Further, dynamic memory allocation and garbage collection can be made available if supported by the language. Supported language providers include assembly language, C, C++, Java, Erlang, JavaScript, Perl, PHP, Python, Ruby, shell script, and Tcl.

*Application providers* allow DTrace to follow the operation of applications through system calls and into the kernel. Applications that offer DTrace application providers include MySQL, PostgreSQL, Oracle Database, Oracle Grid Engine, and Firefox.

## Authors and awards

DTrace was designed and implemented by Bryan Cantrill, Mike Shapiro, and Adam Leventhal.

The authors received recognition in 2005 for the innovations in DTrace from *InfoWorld* and *Technology Review*. DTrace won the top prize in *The Wall Street Journal*'s 2006 Technology Innovation Awards competition. The authors were recognized by USENIX with the Software Tools User Group (STUG) award in 2008.
