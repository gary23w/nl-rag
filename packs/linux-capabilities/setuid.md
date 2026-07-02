---
title: "setuid"
source: https://en.wikipedia.org/wiki/Setuid
domain: linux-capabilities
license: CC-BY-SA-4.0
tags: linux capability model, privilege decomposition capabilities, capability bounding set, least privilege capability drop
fetched: 2026-07-02
---

# setuid

In Unix-like systems, the access rights flags **setuid** and **setgid** (short for *set user identity* and *set group identity*) allow users to run an executable with the file system permissions of the executable's owner or group respectively and to change behaviour in directories. They are often used to allow users on a computer system to run programs with temporarily elevated privileges to perform a specific task. While the assumed user id or group id privileges provided are not always elevated, at a minimum they are specific.

The flags `setuid` and `setgid` are needed for tasks that require different privileges than what the user is normally granted, such as the ability to alter system files or databases to change their login password. Some of the tasks that require additional privileges may not immediately be obvious, though, such as the `ping` command, which must send and listen for control packets on a network interface.

## Effects

The `setuid` and `setgid` flags have different effects, depending on whether they are applied to a file, to a directory or binary executable or non-binary executable file. The `setuid` and `setgid` flags have an effect only on binary executable files and not on scripts (e.g., Bash, Perl, Python).

### When set on an executable file

When the `setuid` or `setgid` attributes are set on an executable file, then any users able to execute the file will automatically execute the file with the privileges of the file's owner (commonly root) and/or the file's group, depending upon the flags set, by setting the effective user ID of the process running the file to the file's owner or setting the effective group ID of the process running the file to the file's group. This allows the system designer to permit trusted programs to be run which a user would otherwise not be allowed to execute. These may not always be obvious. For example, the ping command may need access to networking privileges that a normal user cannot access; therefore it may be given the setuid flag to ensure that a user who needs to ping another system can do so, even if their account does not have the required privilege for sending packets.

#### Security impact

For security purposes, the invoking user is usually prohibited by the system from altering the new process in any way, such as by using `ptrace`, specifying environment variables such as `PATH` or `LD_LIBRARY_PATH`, or sending signals to it, to exploit the raised privilege, although signals from the terminal will still be accepted.

While the `setuid` feature is very useful in many cases, its improper use can pose a security risk if the `setuid` attribute is assigned to executable programs that are not carefully designed. Due to potential security issues, many operating systems ignore the `setuid` attribute when applied to executable *shell scripts*.

The presence of `setuid` executables explains why the `chroot` system call is not available to non-root users on Unix. See limitations of `chroot` for more details.

### When set on a directory

Setting the `setgid` permission on a directory causes files and subdirectories created within to inherit its group ownership, rather than the primary group of the file-creating process. Created subdirectories also inherit the `setgid` bit. The policy is only applied during creation and, thus, only prospectively. Directories and files existing when the `setgid` bit is applied are unaffected, as are directories and files moved into the directory on which the bit is set.

This allows a group of users to work with files without explicitly setting permissions, but limited by the security model expectation that existing files permissions do not implicitly change.

This is generally not needed on most systems derived from BSD, since by default directories are treated as if their `setgid` bit is always set, regardless of the actual value.

On FreeBSD, setting the `setuid` bit on a directory on a UFS file system mounted with the suiddir option causes files and subdirectories created within to inherit its ownership, rather than the user ID of the file-creating process.

## Security

Executables on which these bits are set must be designed and implemented carefully to avoid security vulnerabilities including buffer overruns and path injection. Successful buffer-overrun attacks on vulnerable applications allow the attacker to execute arbitrary code under the rights of the process exploited. In the event that a vulnerable process uses the `setuid` bit to run as `root`, the code will execute with root privileges, in effect giving the attacker root access to the system on which the vulnerable process is running.

Of particular importance in the case of a `setuid` or `setgid` process is the environment of the process. If the environment is not properly sanitized by a privileged process, its behavior can be changed by the unprivileged process that started it. For example, GNU libc was at one point vulnerable to an exploit using `setuid` and an environment variable that allowed executing code from untrusted shared libraries.

## History

The `setuid` bit was invented by Dennis Ritchie and was in the first version of Unix. His employer, then Bell Telephone Laboratories, applied for a patent in 1972. The patent was granted in 1979 as patent number US 4135240  "Protection of data file contents", and was dedicated to the public domain in the same year.

The patent expired in 1996.
