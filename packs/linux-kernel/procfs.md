---
title: "procfs"
source: https://en.wikipedia.org/wiki/Procfs
domain: linux-kernel
license: CC-BY-SA-4.0
tags: linux kernel, loadable kernel module, monolithic kernel, kernel preemption
fetched: 2026-07-02
---

# procfs

The **proc filesystem** (**procfs**) is a special filesystem in Unix-like operating systems that presents information about processes and other system information in a hierarchical file-like structure, providing a more convenient and standardized method for dynamically accessing process data held in the kernel than traditional tracing methods or direct access to kernel memory. Typically, it is mapped to a mount point named */proc* at boot time. The proc file system acts as an interface to internal data structures about running processes in the kernel. In Linux, it can also be used to obtain information about the kernel and to change certain kernel parameters at runtime (sysctl).

Many Unix-like operating systems support the proc filesystem, including System V, Solaris, IRIX, Tru64 UNIX, BSD, Linux, IBM AIX, QNX, and Plan 9 from Bell Labs. OpenBSD dropped support in version 5.7, released in May 2015. It is absent from HP-UX and macOS.

The Linux kernel extends it to non–process-related data.

The proc filesystem provides a method of communication between kernel space and user space. For example, the ps command on Plan 9 and the GNU version of the process reporting utility ps uses the proc file system to obtain its data, without using any specialized system calls.

## History

### UNIX 8th Edition

Tom J. Killian implemented the UNIX 8th Edition (V8) version of */proc*: he presented a paper titled "Processes as Files" at USENIX in June 1984. The design of procfs aimed to replace the *ptrace* system call used for process tracing. Detailed documentation can be found in the proc(4) manual page.

### SVR3

The original AT&T System V Release 3 (SVR3) operating system (available internally to AT&T in 1986 and generally in 1987) did not come with the */proc* filesystem, but a subsequent incremental version of it did. It only contained files representing the processes rather than the now common subdirectories.

### SVR4

Roger Faulkner and Ron Gomes ported V8 */proc* to SVR4, and published a paper called "The Process File System and Process Model in UNIX System V" at USENIX in January 1991. This kind of procfs supported the creation of *ps*, but the files could only be accessed with functions *read()*, *write()*, and *ioctl()*. Between 1995 and 1996, Roger Faulkner created the procfs-2 interface for Solaris-2.6 that offers a structured /proc filesystem with sub-directories.

### Plan 9

Plan 9 implemented a process file system, but went further than V8. V8's process file system implemented a single file per process. Plan 9 created a hierarchy of separate files to provide those functions, and made /proc a real part of the file system. Furthermore, Plan 9's approach to portability allows systems with different architectures and byte order to debug others' processes.

### 4.4BSD and derivatives

4.4BSD cloned its implementation of /proc from Plan 9. As of February 2011, procfs is gradually becoming phased out in FreeBSD, and it has turned to use the *sysctl* interface instead for process-related information. To provide binary compatibility with Linux user space programs, the FreeBSD kernel also provides **linprocfs** that is similar to the Linux procfs. It was removed from OpenBSD in version 5.7, which was released in May 2015, because it "always suffered from race conditions and is now unused". macOS did not implement procfs and user space programs have to use the *sysctl* interface for retrieving process data.

### Solaris

/proc in Solaris was available from the beginning (June 1992). Solaris 2.6 in 1996 introduced procfs2 from Roger Faulkner.

### Linux

Linux first added a /proc filesystem in v0.97.3, September 1992, and first began expanding it to non-process related data in v0.98.6, December 1992.

As of 2020, the Linux implementation includes a directory for each running process, including kernel processes, in directories named /proc/PID, where PID is the process number. Each directory contains information about one process, including:

- /proc/PID/cmdline, the command that originally started the process.
- /proc/PID/cwd, a symlink to the current working directory of the process.
- /proc/PID/environ contains the names and values of the environment variables that affect the process.
- /proc/PID/exe, a symlink to the original executable file, if it still exists (a process may continue running after its original executable has been deleted or replaced).
- /proc/PID/fd, a directory containing a symbolic link for each open file descriptor.
- /proc/PID/fdinfo, a directory containing entries which describe the position and flags for each open file descriptor.
- /proc/PID/maps, a text file containing information about mapped files and blocks (like heap and stack).
- /proc/PID/mem, a binary image representing the process's virtual memory, can only be accessed by a ptrace'ing process.
- /proc/PID/root, a symlink to the root path as seen by the process. For most processes this will be a link to / unless the process is running in a chroot jail.
- /proc/PID/status contains basic information about a process including its run state and memory usage.
- /proc/PID/task, a directory containing hard links to any tasks that have been started by this (i.e.: the parent) process.

(Users may obtain the PID with a utility such as pgrep, pidof or ps:

```mw
$ ls -l /proc/$(pgrep -n python3)/fd        # List all file descriptors of the most recently started `python3' process
total 0
lrwx------ 1 baldur baldur 64 2020-03-18 12:31 0 -> /dev/pts/3
lrwx------ 1 baldur baldur 64 2020-03-18 12:31 1 -> /dev/pts/3
lrwx------ 1 baldur baldur 64 2020-03-18 12:31 2 -> /dev/pts/3
$ readlink /proc/$(pgrep -n python3)/exe    # List executable used to launch the most recently started `python3' process  
/usr/bin/python3.8
```

)

/proc also includes non-process-related system information, although in the 2.6 kernel much of that information moved to a separate pseudo-file system, sysfs, mounted under /sys:

- depending on the mode of power management (if at all), either directory, /proc/acpi or /proc/apm, which predate sysfs and contain various bits of information about the state of power management.
- /proc/buddyinfo, information about the buddy algorithm that handles memory fragmentation.
- /proc/bus, containing directories representing various buses on the computer, such as PCI/USB. This has been largely superseded by sysfs under /sys/bus which is far more informative.
- /proc/fb, a list of the available framebuffers
- /proc/cmdline, giving the boot options passed to the kernel
- /proc/cpuinfo, containing information about the CPU, such as its vendor (and CPU family, model and model names which should allow users to identify the CPU) and its speed (CPU clockspeed), cache size, number of siblings, cores, and CPU flags. The format and available information is highly architecture-depended. On some architectures, /proc/cpuinfo includes a value for "bogomips", frequently misconstrued as a measure of CPU speed, like a benchmark, but it does not actually measure any sensible (for end-users) value at all. It occurs as a side-effect of kernel timer calibration and yields highly varying values depending on CPU type, even at equal clock speeds.

```mw
$ cat /proc/cpuinfo
processor   : 0
 vendor_id  : AuthenticAMD
 cpu family : 16
 model      : 6
 model name : AMD Athlon II X2 270 Processor
 stepping   : 3
 microcode  : 0x10000c8
 cpu MHz    : 2000.000
 cache size : 1024 KB
 ...
 processor  : 1
 vendor_id  : AuthenticAMD
 cpu family : 16
 model      : 6
 model name : AMD Athlon II X2 270 Processor
 stepping   : 3
 microcode  : 0x10000c8
 cpu MHz    : 800.000
 cache size : 1024 KB
 ...
```

On multi-core CPUs, /proc/cpuinfo contains the fields for "siblings" and "cpu cores" which represent the following calculation is applied:

```
"siblings" = (HT per CPU package) * (# of cores per CPU package)
"cpu cores" = (# of cores per CPU package)
```

A CPU package means physical CPU which can have multiple cores (*single core* for one, *dual core* for two, *quad core* for four). This allows a distinction between hyper-threading and dual-core, i.e. the number of hyper-threads per CPU package can be calculated by *siblings / CPU cores*. If both values for a CPU package are the same, then hyper-threading is not supported. For instance, a CPU package with siblings=2 and "cpu cores"=2 is a dual-core CPU but does not support hyper-threading.

- /proc/crypto, a list of available cryptographic modules
- /proc/devices, a list of character and block devices sorted by device ID but giving the major part of the /dev name too
- /proc/diskstats, giving some information (including device numbers) for each of the logical disk devices
- /proc/filesystems, a list of the file systems supported by the kernel at the time of listing
- /proc/interrupts, /proc/iomem, /proc/ioports and the directory /proc/irq, giving some details about the devices (physical or logical) using the various system resources
- /proc/kmsg, holding messages output by the kernel
- /proc/loadavg, containing stats about the current load average in the last minutes.
- /proc/meminfo, containing a summary of how the kernel is managing its memory.
- /proc/modules, one of the most important files in /proc, containing a list of the kernel modules currently loaded . It gives some indication (not always entirely correct) of dependencies.
- /proc/mounts, a symlink to self/mounts which contains a list of the currently mounted devices and their mount points (and which file system is in use and what mount options are in use).
- /proc/net/, a directory containing useful information about the network stack, in particular /proc/net/nf_conntrack, which lists existing network connections (particularly useful for tracking routing when iptables FORWARD is used to redirect network connections)
- /proc/partitions, a list of the device-numbers, their size and /dev names which the kernel has identified as existing partitions
- /proc/scsi, giving information about any devices connected via a SCSI or RAID controller
- a symbolic link to the current (traversing) process at /proc/self (i.e. /proc/PID/ where PID is that of the current process).
- /proc/slabinfo, listing statistics on the caches for frequently-used objects in the Linux kernel
- /proc/swaps, a list of the active swap partitions, their various sizes and priorities
- Access to dynamically configurable kernel options under /proc/sys. Under /proc/sys appear directories representing the areas of kernel, containing readable and writable virtual files. For example, a commonly referenced virtual file is /proc/sys/net/ipv4/ip_forward, because it is necessary for routing firewalls or tunnels. The file contains either a '1' or a '0': if it is 1, the IPv4 stack forwards packets not meant for the local host, if it is 0 then it does not.
- /proc/sysvipc, containing memory-sharing and inter-process communication (IPC) information.
- /proc/tty, containing information about terminals; /proc/tty/driver contains a list of TTY drivers and their usage
- /proc/uptime, the length of time the kernel has been running since boot and spent in idle mode (both in seconds)
- /proc/version, containing the Linux kernel version, distribution number, gcc version number (used to build the kernel) and any other pertinent information relating to the version of the kernel currently running
- other files depending on various hardware, module configurations, and changes to the kernel.

The basic utilities that use /proc under Linux come in the procps (/proc processes) package, and only function in conjunction with a mounted /proc.

### CYGWIN

Cygwin implemented a procfs that is basically the same as the Linux procfs.
