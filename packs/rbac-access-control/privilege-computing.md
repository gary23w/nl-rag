---
title: "Privilege (computing)"
source: https://en.wikipedia.org/wiki/Privilege_(computing)
domain: rbac-access-control
license: CC-BY-SA-4.0
tags: role based access control, access control list, least privilege access, computing privilege, identity and access management
fetched: 2026-07-02
---

# Privilege (computing)

In computing, **privilege** is defined as the delegation of authority to perform security-relevant functions on a computer system. A privilege allows a user to perform an action with security consequences. Examples of various privileges include the ability to create a new user, install software, or change kernel functions.

Users who have been delegated extra levels of control are called privileged. Users who lack most privileges are defined as unprivileged, regular, or normal users.

## Theory

Privileges can either be automatic, granted, or applied for.

An automatic privilege exists when there is no requirement to have permission to perform an action. For example, on systems where people are required to log into a system to use it, logging out will not require a privilege. Systems that do not implement file protection - such as MS-DOS - essentially give unlimited privilege to perform any action on a file.

A granted privilege exists as a result of presenting some credential to the privilege granting authority. This is usually accomplished by logging on to a system with a username and password, and if the username and password supplied are correct, the user is granted additional privileges.

A privilege is applied for by either an executed program issuing a request for advanced privileges, or by running some program to apply for the additional privileges. An example of a user applying for additional privileges is provided by the `sudo` command to run a command as superuser (*root*) user, or by the Kerberos authentication system.

Modern processor architectures have multiple CPU modes that allows the OS to run at different privilege levels. Some processors have two levels (such as *user* and *supervisor*); i386+ processors have four levels (#0 with the most, #3 with the least privileges). Tasks are tagged with a privilege level. Resources (segments, pages, ports, etc.) and the privileged instructions are tagged with a demanded privilege level. When a task tries to use a resource, or execute a privileged instruction, the processor determines whether it has the permission (if not, a "protection fault" interrupt is generated). This prevents user tasks from damaging the OS or each other.

In computer programming, exceptions related to privileged instruction violations may be caused when an array has been accessed out of bounds or an invalid pointer has been dereferenced when the invalid memory location referenced is a privileged location, such as one controlling device input/output. This is particularly more likely to occur in programming languages such as C, which use pointer arithmetic or do not check array bounds automatically.

### Criticism

Mark Miller has critiqued the framing of privilege as being poorly defined and hard to measure, and suggested that authority can be defined as the set of things a program can do, which is more helpful.

## Unix

On Unix-like systems, the superuser (commonly known as 'root') owns all the privileges. Ordinary users are granted only enough permissions to accomplish their most common tasks. UNIX systems have built-in security features. Most users cannot set up a new user account nor do other administrative procedures. The user “root” is a special user, something called super-user, which can do anything at all on the system. This high degree power is necessary to fully administer a UNIX system, but it also allows its user to make a mistake and cause system problems.

Unprivileged users usually cannot:

- Adjust kernel options;
- modify system files, or files of other users.
- change the ownership of any files;
- change the runlevel (on systems with System V-style initialization);
- change the file mode of any files;
- adjust ulimits or disk quotas;
- start, stop and remove daemons;
- signal processes of other users;
- create device nodes;
- create or remove users or groups;
- mount or unmount volumes (although it is becoming common to allow regular users to mount and unmount removable media, such as compact discs - this is typically accomplished via FUSE);
- execute the contents of any `sbin/` directory (although it is becoming common to simply restrict the behavior of such programs when executed by regular users);
- bind ports below 1024.

## Windows NT

On Windows NT-based systems, privileges are delegated in varying degrees. These delegations can be defined using the local security policy manager (`secpol.msc`). The following is an abbreviated list of the default assignments:

- 'NT AUTHORITY\System' is the closest equivalent to the Superuser on Unix-like systems. It has many of the privileges of a classic Unix superuser (such as being a trustee on every file created);
- 'Administrator' is one of the closest equivalents to the superuser (root) on Unix-like systems. However, this user cannot override as many of the operating system's protections as the superuser can;
- members of the 'Administrators' group have privileges almost equal to 'Administrator';
- members of the 'Power Users' group have the ability to install programs and backup the system.
- members of the 'Users' group are the equivalent to unprivileged users on Unix-like systems.

Windows defines a number of administrative privileges that can be assigned individually to users and/or groups. An account (user) holds only the privileges granted to it, either directly or indirectly through group memberships. Upon installation a number of groups and accounts are created and privileges are granted to them. However, these grants can be changed at a later time or though a group policy. Unlike Linux, no privileges are implicitly or permanently granted to a specific account.

Some administrative privileges (e.g. taking ownership of or restoring arbitrary files) are so powerful that if used with malicious intent they could allow the entire system to be compromised. With user account control (on by default since Windows Vista) Windows will strip the user token of these privileges at login. Thus, if a user logs in with an account with broad system privileges, he/she will still not be *running* with these system privileges. Whenever the user wants to perform administrative actions requiring any of the system privileges he/she will have to do this from an *elevated* process. When launching an *elevated* process, the user is made aware that his/her administrative privileges are being asserted through a prompt requiring his/her consent. Not holding privileges until actually required is in keeping with the principle of least privilege.

Elevated processes will run with the full privileges of the *user*, not the full privileges of the *system*. Even so, the privileges of the user may still be more than what is required for that particular process, thus not completely least privilege.

The DOS-based Windows ME, Windows 98, Windows 95 and previous versions of non-NT Windows only operated on the FAT filesystem, did not support filesystem permissions and therefore privileges are effectively defeated on Windows NT-based systems that do not use the NTFS file system.

### Nomenclature

The names used in the Windows source code end in either "privilege" or "logonright". This has led to some confusion about what the full set of all these "rights" and "privileges" should be called.

Microsoft currently uses the term "user rights". In the past some other terms have also been used by Microsoft, such as "privilege rights" , "logon user rights" and "nt-rights".
