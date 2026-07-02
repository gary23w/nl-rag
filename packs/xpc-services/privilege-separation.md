---
title: "Privilege separation"
source: https://en.wikipedia.org/wiki/Privilege_separation
domain: xpc-services
license: CC-BY-SA-4.0
tags: xpc services, cross-process communication, process sandbox, privilege separation
fetched: 2026-07-02
---

# Privilege separation

In computer programming and computer security, **privilege separation** (**privsep**) is one software-based technique for implementing the principle of least privilege. With privilege separation, a program is divided into parts which are limited to the specific privileges they require in order to perform a specific task. This is used to mitigate the potential damage of a computer security vulnerability.

## Implementation

A common method to implement privilege separation is to have a computer program fork into two processes. The main program drops privileges, and the smaller program keeps privileges in order to perform a certain task. The two halves then communicate via a socket pair. Thus, any successful attack against the larger program will gain minimal access, even though the pair of programs will be capable of performing privileged operations.

Privilege separation is traditionally accomplished by distinguishing a *real* user ID/group ID from the *effective* user ID/group ID, using the setuid(2)/setgid(2) and related system calls, which were specified by POSIX. If these are incorrectly positioned, gaps can allow widespread network penetration.

Many network service daemons have to do a specific privileged operation such as open a raw socket or an Internet socket in the well known ports range. Administrative utilities can require particular privileges at run-time as well. Such software tends to separate privileges by revoking them completely after the critical section is done, and change the user it runs under to some unprivileged account after so doing. This action is known as *dropping root* under Unix-like operating systems. The unprivileged part is usually run under the "nobody" user or an equivalent separate user account.

Privilege separation can also be done by splitting functionality of a single program into multiple smaller programs, and then assigning the extended privileges to particular parts using file system permissions. That way the different programs have to communicate with each other through the operating system, so the scope of the potential vulnerabilities is limited (since a crash in the less privileged part cannot be exploited to gain privileges, merely to cause a denial-of-service attack).

## Examples

**Dovecot**

Another email server software designed with privilege separation and security in mind is Dovecot.

**OpenBSD**

Separation of privileges is one of the major OpenBSD security features.

**OpenSSH**

OpenSSH uses privilege separation to ensure *pseudo terminal* (***pty***) creation happens in a secure part of the process, away from per connection processes with network access.

**Postfix**

The implementation of Postfix was focused on implementing comprehensive privilege separation.

**Solaris**

Solaris implements a separate set of functions for privilege bracketing.
