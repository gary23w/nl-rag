---
title: "Time-of-check to time-of-use"
source: https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use
domain: race-condition-security
license: CC-BY-SA-4.0
tags: time of check time of use, race condition security, concurrency vulnerability, atomic operation defense
fetched: 2026-07-02
---

# Time-of-check to time-of-use

In software development, **time-of-check to time-of-use** (**TOCTOU**, **TOCTTOU** or **TOC/TOU**) is a class of software bugs caused by a race condition involving the *checking* of the state of a part of a system (such as a security credential) and the *use* of the results of that check.

TOCTOU race conditions are common in Unix between operations on the file system, but can occur in other contexts, including local sockets and improper use of database transactions. In the early 1990s, the mail utility of BSD 4.3 UNIX had an exploitable race condition for temporary files because it used the `mktemp()` function. Early versions of OpenSSH had an exploitable race condition for Unix domain sockets. They remain a problem in modern systems; as of 2019, a TOCTOU race condition in Docker allows root access to the filesystem of the host platform. In the 2023 Pwn2Own competition in Vancouver, a team of hackers were able to compromise the gateway in an updated Tesla Model 3 using this bug. In 2025, a TOCTOU race condition in Amazon Web Services' DNS management system for DynamoDB caused a major outage across the US-EAST-1 region. The incident stemmed from outdated DNS plans being applied after newer ones had already been cleaned up, resulting in the deletion of endpoint IP addresses and widespread service failure.

## Description

A program is vulnerable to a TOCTOU race condition if it does the following

1. Checks some property or validates some data
2. Takes some action based on this information

and the following are the case

1. Non-atomic: It's possible for other programs that run concurrently with this program to execute in between steps 1 and 2
2. Outside control: Other programs can change the property or data

Then, if another process does in fact change the property between step 1 and 2, step 2 is performed based on outdated information, which can have unintended consequences.

If the program running is privileged, and an unprivileged process can affect the property, it can effectively execute certain privileged tasks.

In particular, if the property checks whether some action is allowed, and thereby implements a security boundary, such as a permissions check, this permissions check can then be bypassed completely, and a variety of privileged actions can be executed this way (privilege escalation).

## Examples

In Unix, the following C code, when used in a `setuid` program, has a TOCTOU bug:

```mw
if (access("file", W_OK) != 0) {
    exit(1);
}

fd = open("file", O_WRONLY);
write(fd, buffer, sizeof(buffer));
```

Here, *access* is intended to check whether the real user who executed the `setuid` program would normally be allowed to write the file (i.e., `*access*` checks the real userid rather than effective userid).

This race condition is vulnerable to an attack:

| Victim | Attacker |
|---|---|
| if (access("file", W_OK) != 0) { exit(1); } |   |
|   | After the access check, before the open, the attacker replaces `file` with a symlink to the Unix password file `/etc/passwd`:symlink("/etc/passwd", "file"); |
| fd = open("file", O_WRONLY); write(fd, buffer, sizeof(buffer)); Actually writing over `/etc/passwd` |   |

In this example, an attacker can exploit the race condition between the `access` and `open` to trick the `setuid` victim into overwriting an entry in the system password database. TOCTOU races can be used for privilege escalation to get administrative access to a machine.

Although this sequence of events requires precise timing, it is possible for an attacker to arrange such conditions without too much difficulty.

The implication is that applications cannot assume the state managed by the operating system (in this case the file system namespace) will not change between system calls.

## Reliably timing TOCTOU

Exploiting a TOCTOU race condition requires precise timing to ensure that the attacker's operations interleave properly with the victim's. In the example above, the attacker must execute the `symlink` system call precisely between the `access` and `open`. For the most general attack, the attacker must be scheduled for execution after each operation by the victim, also known as "single-stepping" the victim.

In the case of BSD 4.3 mail utility and `mktemp()`, the attacker can simply keep launching mail utility in one process, and keep guessing the temporary file names and keep making symlinks in another process. The attack can usually succeed in less than one minute.

Techniques for single-stepping a victim program include file system mazes and algorithmic complexity attacks. In both cases, the attacker manipulates the OS state to control scheduling of the victim.

File system mazes force the victim to read a directory entry that is not in the OS cache, and the OS puts the victim to sleep while it is reading the directory from disk. Algorithmic complexity attacks force the victim to spend its entire scheduling quantum inside a single system call traversing the kernel's hash table of cached file names. The attacker creates a very large number of files with names that hash to the same value as the file the victim will look up.

## Preventing TOCTOU

Despite conceptual simplicity, TOCTOU race conditions are difficult to avoid and eliminate. One general technique is to use error handling instead of pre-checking, under the philosophy of EAFP – "It is easier to ask for forgiveness than permission" – rather than LBYL – "look before you leap". In this case there is no check, and failure of assumptions to hold are signaled by an error being returned.

In the context of file system TOCTOU race conditions, the fundamental challenge is ensuring that the file system cannot be changed between two system calls. In 2004, an impossibility result was published, showing that there was no portable, deterministic technique for avoiding TOCTOU race conditions when using the Unix `access` and `open` filesystem calls.

Since this impossibility result, libraries for tracking file descriptors and ensuring correctness have been proposed by researchers.

An alternative solution proposed in the research community is for Unix systems to adopt transactions in the file system or the OS kernel. Transactions provide a concurrency control abstraction for the OS, and can be used to prevent TOCTOU races. While no production Unix kernel has yet adopted transactions, proof-of-concept research prototypes have been developed for Linux, including the Valor file system and the TxOS kernel. Microsoft Windows has added transactions to its NTFS file system, but Microsoft discourages their use, and has indicated that they may be removed in a future version of Windows.

File locking is a common technique for preventing race conditions for a single file, but it does not extend to the file system namespace and other metadata, nor does locking work well with networked filesystems, and cannot prevent TOCTOU race conditions.

For `setuid` binaries, a possible solution is to use the `seteuid()` system call to change the effective user and then perform the `open()` call. Differences in `setuid()` between operating systems can be problematic.

## Real-world consequences

TOCTOU vulnerabilities have caused significant outages in large-scale systems. In October 2025, AWS experienced a major disruption due to a race condition in its DNS management system for DynamoDB. The incident involved outdated DNS plans being applied after newer ones had already been cleaned up, leading to the deletion of endpoint IPs and widespread service failure.
