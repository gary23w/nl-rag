---
title: "Process identifier"
source: https://en.wikipedia.org/wiki/Process_identifier
domain: init-systems
license: CC-BY-SA-4.0
tags: init system, systemd manager, sysvinit scripts, process identifier
fetched: 2026-07-02
---

# Process identifier

In computing, the **process identifier** (a.k.a. **process ID** or **PID**) is a number used by most operating system kernels—such as those of Unix, macOS and Windows—to uniquely identify an active process. This number may be used as a parameter in various function calls, allowing processes to be manipulated, such as adjusting the process's priority or killing it altogether.

## Unix-like

In Unix-like operating systems, new processes are created by the `fork()` system call. The PID is returned to the parent process, enabling it to refer to the child in further function calls. The parent may, for example, wait for the child to terminate with the `waitpid()` function, or terminate the process with `kill()`.

There are two tasks with specially distinguished process IDs: PID 0 is used for *swapper* or *sched*, which is part of the kernel and is a process that runs on a CPU core whenever that CPU core has nothing else to do. Linux also calls the threads of this process *idle tasks*. In some APIs, PID 0 is also used as a special value that always refers to the calling thread, process, or process group. Process ID 1 is usually the init process primarily responsible for starting and shutting down the system. Originally, process ID 1 was not specifically reserved for init by any technical measures: it simply had this ID as a natural consequence of being the first process invoked by the kernel. More recent Unix systems typically have additional kernel components visible as 'processes', in which case PID 1 is actively reserved for the init process to maintain consistency with older systems.

Process IDs, in the first place, are usually allocated on a sequential basis, beginning at 0 and rising to a maximum value which varies from system to system. Once this limit is reached, allocation restarts at 300 and again increases. In macOS and HP-UX, allocation restarts at 100. However, for this and subsequent passes any PIDs still assigned to processes are skipped. Some consider this to be a potential security vulnerability in that it allows information about the system to be extracted, or messages to be covertly passed between processes. As such, implementations that are particularly concerned about security may choose a different method of PID assignment. On some systems, like MPE/iX, the lowest available PID is used, sometimes in an effort to minimize the number of process information kernel pages in memory.

The current process ID is provided by a `getpid()` system call, or as a variable `$$` in shell. The process ID of a parent process is obtainable by a `getppid()` system call.

On Linux, the maximum process ID is given by the pseudo-file `/proc/sys/kernel/pid_max`. `pid_max` has historically been set to 65,535 ( $2^{16}-1$ ) on Linux, but can now be configured to up to 4,194,303 ( $2^{22}-1$ ) on 64-bit Linux systems,

### Pidfile

Some processes (including many daemons, for example, the MySQL daemon), write their process ID to a documented file location, to allow other processes to look it up.

## Microsoft Windows

On Microsoft Windows operating systems, one can get a current process's ID using the `GetCurrentProcessId()` function of the Windows API, and ID of other processes using `GetProcessId()`. Internally, process ID is called a *client ID*, and is allocated from the same namespace as thread IDs, so these two never overlap. The System Idle Process is given process ID 0. On older Windows systems, the System Process is given the process ID 8 on Windows 2000 and 4 on Windows XP and Windows Server 2003. On the Windows NT family of operating systems, process and thread identifiers are all multiples of 4, but it is not part of the specification.
