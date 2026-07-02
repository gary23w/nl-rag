---
title: "Background process"
source: https://en.wikipedia.org/wiki/Background_process
domain: render-cloud
license: CC-BY-SA-4.0
tags: render cloud platform, render web service, render static site, unified cloud render
fetched: 2026-07-02
---

# Background process

A **background process** is a computer process that runs *behind the scenes* (i.e., in the background) and without user intervention. Typical tasks for these processes include logging, system monitoring, scheduling, and user notification.

On a Windows system, a background process is either a computer program that does not create a user interface, or a Windows service. The former are started just as any other program is started, e.g., via Start menu. Windows services, on the other hand, are started by Service Control Manager. In Windows Vista and later, they are run in a separate session.

On a Unix-like system, a daemon would be a background process. However, in a shell that supports job control, a process that is in a process group whose process group ID differs from its terminal group ID (TGID) would be a background process. (The TGID of a process is the process ID of the process group leader that opened the terminal, which is typically the login shell. The TGID identifies the control terminal of the process group.) This type of process is unable to receive keyboard signals from its parent terminal, and typically will not send output to that terminal. This more technical definition does not distinguish between whether or not the process can receive user intervention. Although background processes are typically used for purposes needing few resources, any process can be run in the background, and such a process will behave like any other process, with the exceptions given above.

## Windows services

In Windows NT family of operating systems, a Windows service is a dedicated background process. A Windows service must conform to the interface rules and protocols of the Service Control Manager, the component responsible for managing Windows services.

Windows services can be configured to start when the operating system starts, and to run in the background as long as Windows runs. Alternatively, they can be started manually or by an event. Windows NT operating systems include numerous services which run in context of three user accounts: `System`, `Network Service` and `Local Service`. These Windows components are often associated with Host Process for Windows Services: svchost.exe. Since Windows services operate in the context of their own dedicated user accounts, they can operate when a user is not logged on.

Before Windows Vista, services installed as "interactive services" could interact with Windows desktop and show a graphical user interface. With Windows Vista, however, interactive services became deprecated and ceased operating properly, as a result of Windows Service Hardening.

The three principal means of managing Windows services are:

1. Services snap-in for Microsoft Management Console
2. `sc.exe`
3. Windows PowerShell

## Daemon

A daemon is a type of background process designed to run continually in the background, waiting for event(s) to occur or condition(s) to be met. When launched with the *daemon* function, daemons are disassociated from their parent terminal.

## Background jobs in Unix

From a Unix command line, a background process can be launched using the "&" operator. The *bg* command can resume a suspended job (sending SIGCONT), running it in the background. Using the *fg* command will also set the foreground process group of the controlling terminal of the session to the process group of the job, bringing the job into the foreground. The *jobs* command will list all processes associated with the current terminal and can be used to bring background processes into the foreground.

When a login session ends, via explicit logout or network disconnection, all processes, including background processes, will by default be terminated, to prevent them from becoming orphan processes. Concretely, when the user exits the launching shell process, as part of shutdown it sends a *hangup* signal (SIGHUP) to all its jobs, to terminate all the processes in the corresponding process group. To have processes continue to run, one can either not end the session, or end the session without terminating the processes. A terminal multiplexer can be used to leave a session running but detach a virtual terminal from it, leaving processes running as child processes of the session; the user can then reattach session later. Or, termination can be prevented by either starting the process via the nohup command (telling the process to ignore SIGHUP), or by subsequently running `disown` with the job id, which either removes the job from the job list entirely, or simply prevents SIGHUP from being sent. In the latter case when the session ends, the child processes are not terminated, either because they are not sent SIGHUP or because they ignore it, and thus become orphan processes, which are then adopted by the init process (the kernel sets the init process as their parent), and they continue running without a session, now called *daemons*.

### Example

In this example running on Unix, the *sleep* utility was launched into the background. Afterward, the *ps* tool was run in the foreground, where it output the below text. Both were launched from the shell.

```mw
  PID TT  STAT    TIME COMMAND
54659 10  S    0:00.06 su (zsh)
54703 10  IN   0:00.00 - sleep 1000
54852 10  R+   0:00.00 - ps -U botty -axd
```

## Smartphones

Many newer versions of smartphone and PDA operating systems now include the ability to start background processes. Due to hardware limits, background processes on mobile operating systems are often restricted to certain tasks or consumption levels. On Android, CPU use for background processes may be bounded at 5–10%. Applications on Apple's iOS are limited to a subset of functions while running in the background. On both iOS and Android, background processes, as well as background or unused apps, can be killed by the system if they are using too much memory or too much battery power.
