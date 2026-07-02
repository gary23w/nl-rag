---
title: "Service Control Manager"
source: https://en.wikipedia.org/wiki/Service_Control_Manager
domain: windows-services
license: CC-BY-SA-4.0
tags: windows service, service control manager, svchost process, task scheduler
fetched: 2026-07-02
---

# Service Control Manager

**Service Control Manager** (**SCM**) is a special system process under the Windows NT family of operating systems, which starts, stops and interacts with Windows service processes. It is located in the `%SystemRoot%\System32\services.exe` executable. Service processes interact with SCM through a well-defined API, and the same API is used internally by the interactive Windows service management tools such as the MMC snap-in `Services.msc` and the command-line Service Control utility `sc.exe`.

## Implementation

The SCM executable, `Services.exe`, runs as a Windows console program and is launched by the Wininit process early during the system startup. Its main function, `SvcCtrlMain()`, launches all the services configured for automatic startup. First an internal database of installed services is initialized by reading the following two registry keys:

- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ServiceGroupOrder\List`, containing the names and order of service groups. Each service's registry key contains an optional `Group` value which governs the order of initialization of a respective service or a device driver, with respect to other service groups.
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`, which contains the actual database of services and device drivers and is read into SCM's internal database. SCM reads every service's `Group` value as well as load-order dependencies from their `DependOnGroup` and `DependOnService` registry keys.

In the next step, SCM's main function `SvcCtrlMain()` calls the function `ScGetBootAndSystemDriverState()` function which checks whether the device drivers that should be started during the boot or system startup were successfully loaded, and those that have failed to do so are stored in a list called `ScFailedDrivers`. Then a named pipe `\Pipe\Ntsvcs` is created as a remote procedure call interface between the SCM and the SCPs (Service Control Processes) that interact with specific services.

Next, it calls the `ScAutoStartServices()` function which loops through all the services marked as auto-start, paying attention to the calculated load-order dependencies. In case of a circular dependency an error is noted and the service depending on a service that belongs to a group coming later in the load order is skipped. For delayed auto-start services, grouping has no effect, and those are loaded at a later stage of system startup.

For each service it wants to start, the SCM calls the `ScStartService()` function which checks the name of the file that runs the service's process, ensuring that the account specified for the service is same as the account that the service process runs in. Every service that does not run in the `System` account is logged in by calling the LSASS function `LogonUserEx()`, for which LSASS process looks up "secret" passwords stored in the `HKLM\SECURITY\Policy\Secrets\` registry key, which were stored by the SCP using the `LsaStorePrivateData()` API, when the service was originally configured.

Next, the `ScLogonAndStartImage()` function is called for every service whose service process has not been already launched. Service processes are created in a suspended state via the `CreateProcessAsUser()` API. Before the service process' execution is resumed, a named pipe `\Pipe\Net\NtControlPipeX` (where X is a number incremented for each service iteration) is created which serves as a communication channel between the SCM and the service process. Service process connects to the pipe by calling the `StartServiceCtrlDispatcher()` function, after which the SCM sends the service a "start" command.

### Delayed auto-start services

Delayed auto-start services have been added in Windows Vista, in order to solve the problem of a prolonged system startup, as well as to speed-up the start of critical services that cannot be delayed. Originally the auto-start method of service initialization was designed for essential system services upon which other applications and services depend. The SCM initializes the delayed services only after handling all the non-delayed auto-start services, by invoking the `ScInitDelayStart()` function. This function queues a delayed (120 seconds by default) work item associated with a corresponding worker thread. Other than being initialized after a delay, there are no other differences between delayed and non-delayed services.

### Device drivers

Services whose `Type` registry value is `SERVICE_KERNEL_DRIVER` or `SERVICE_FILE_SYSTEM_DRIVER` are handled specially: these represent device drivers for which `ScStartService()` calls the `ScLoadDeviceDriver()` function which loads the appropriate driver (usually a file with an extension `.sys`) which must be located in the `%SystemRoot%\System32\Drivers\` directory. For that purpose, the `NtLoadDriver` system call is invoked, and the `SeLoadDriverPrivilege` is added to the SCM's process.

### Network drive letters

SCM provides an additional functionality completely unrelated to Windows services: it notifies GUI applications such as the Windows Explorer when a network drive-letter connection has been created or deleted, by broadcasting Windows messages `WM_DEVICECHANGE`.
