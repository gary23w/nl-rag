---
title: "Windows Task Scheduler"
source: https://en.wikipedia.org/wiki/Windows_Task_Scheduler
domain: windows-services
license: CC-BY-SA-4.0
tags: windows service, service control manager, svchost process, task scheduler
fetched: 2026-07-02
---

# Windows Task Scheduler

**Task Scheduler** (formerly **Scheduled Tasks**) is a job scheduler in Microsoft Windows that launches computer programs or scripts at pre-defined times or after specified time intervals. Microsoft introduced this component in the Microsoft Plus! for Windows 95 as *System Agent.* Its core component is an eponymous Windows service. The Windows Task Scheduler infrastructure is the basis for the Windows PowerShell scheduled jobs feature introduced with PowerShell v3.

Task Scheduler can be compared to cron or anacron on Unix-like operating systems. This service should not be confused with the scheduler, which is a core component of the OS kernel that allocates CPU resources to processes already running.

## Versions

### Task Scheduler 1.0

Task Scheduler 1.0 is included with Windows NT 4.0 (with Internet Explorer 4.0 or later), Windows 2000, Windows XP and Windows Server 2003. It runs as a Windows Service, and the task definitions and schedules are stored in binary `.job` files. Tasks are manipulated directly by manipulating the `.job` files. Each task corresponds to single action. On Windows 95 (with Internet Explorer 4.0 or later), Windows 98 and Windows Me, the Task Scheduler runs as an ordinary program, `mstask.exe`. It also displays a status icon in the notification area on Windows 95 and Windows 98 and runs as a hidden service on Windows Me, but can be made to show a tray icon. Computer programs and scripts can access the service through six COM interfaces. Microsoft provides a scheduling agent DLL, a sample VBScript and a configuration file to automate Task Scheduler.

In addition to the graphical user interface for Task Scheduler in Control Panel, Windows provides two command-line tools for managing scheduled task: `at.exe` (deprecated) and `schtasks.exe`. However, `at.exe` cannot access tasks created or modified by Control Panel or `schtasks.exe`. Also, tasks created with `at.exe`are not interactive by default; interactivity needs to be explicitly requested. The binary ".job" files which the AT command produces are stored in the %WINDIR%\Tasks directory.

### Task Scheduler 2.0

Task Scheduler 2.0 was introduced with Windows Vista and included in Windows Server 2008 as well. The redesigned Task Scheduler user interface is now based on Management Console. In addition to running tasks on scheduled times or specified intervals, Task Scheduler 2.0 also supports calendar and event-based triggers, such as starting a task when a particular event is logged to the *event log*, or when a combination of events has occurred. Also, several tasks that are triggered by the same event can be configured to run either simultaneously or in a pre-determined chained sequence of a series of actions, instead of having to create multiple scheduled tasks. Tasks can also be configured to run based on system status such as being idle for a pre-configured amount of time, on startup, logoff, or only during or for a specified time. XPath expressions can be used to filter events from the Windows Event Log. Tasks can also be delayed for a specified time after the triggering event has occurred, or repeat until some other event occurs. Actions that need to be done if a task fails can also be configured. The actions that can be taken in response to triggers, both event-based as well as time-based, not only include launching applications but also take a number of custom actions. Task Scheduler includes a number of actions built-in, spanning a number of applications; including send an e-mail, show a message box, or fire a COM handler when it is triggered. Custom actions can also be specified using the Task Scheduler API. Task Scheduler keeps a history log of all execution details of all the tasks. Windows Vista uses Task Scheduler 2.0 to run various system-level tasks; consequently, the Task Scheduler service can no longer be disabled (except with a simple registry tweak).

Task Scheduler 2.0 exposes an API to allow computer programs and scripts create tasks. It consists of 42 COM interfaces. The Windows API does not, however, include a managed wrapper for Task Scheduler though an open source implementation exists. The job files for Task Scheduler 2.0 are XML-based, and are human-readable, conforming to the *Task Scheduler Schema*.

#### Other features

- New security features, including using *Credential Manager* to passwords for tasks on workgroup computers and using Active Directory for task credentials on domain-joined computers so that they cannot be retrieved easily. Also, scheduled tasks are executed in their own session, instead of the same session as system services or the current user.
- Ability to wake up a machine remotely or using BIOS timer from sleep or hibernation to execute a scheduled task or run a previously scheduled task after a machine gets turned on.
- Ability to attach *tasks* to *events* directly from the Event Viewer.

## Tasks

The Task Scheduler service works by managing *Tasks*; *Task* refers to the action (or actions) taken in response to trigger(s). A task is defined by associating a set of actions, which can include launching an application or taking some custom-defined action, to a set of triggers, which can either be time-based or event-based. In addition, a task also can contain metadata that defines how the actions will be executed, such as the security context the task will run in. Tasks are serialized to `.job` files and are stored in the special folder titled *Task Folder*, organized in subdirectories. Programmatically, the task folder is accessed using the `ITaskFolder` interface or the `TaskFolder` scripting object and individual tasks using the `IRegisteredTask` interface or `RegisteredTask` object.

## Column 'Last Result'

The Last Result column displays a completion code. The common codes for scheduled tasks are:

- 0 or 0x0: The operation completed successfully.
- 1 or 0x1: Incorrect function called or unknown function called.
- 2 or 0x2: File not found.
- 10 or 0xa: The environment is incorrect.
- 0x00041300: Task is ready to run at its next scheduled time.
- 0x00041301: The task is currently running.
- 0x00041302: The task has been disabled.
- 0x00041303: The task has not yet run.
- 0x00041304: There are no more runs scheduled for this task.
- 0x00041305: One or more of the properties that are needed to run this task have not been set.
- 0x00041306: The last run of the task was terminated by the user.
- 0x00041307: Either the task has no triggers or the existing triggers are disabled or not set.
- 0x00041308: Event triggers do not have set run times.
- 0x80010002: Call was canceled by the message filter
- 0x80041309: A task's trigger is not found.
- 0x8004130A: One or more of the properties required to run this task have not been set.
- 0x8004130B: There is no running instance of the task.
- 0x8004130C: The Task Scheduler service is not installed on this computer.
- 0x8004130D: The task object could not be opened.
- 0x8004130E: The object is either an invalid task object or is not a task object.
- 0x8004130F: No account information could be found in the Task Scheduler security database for the task indicated.
- 0x80041310: Unable to establish existence of the account specified.
- 0x80041311: Corruption was detected in the Task Scheduler security database
- 0x80041312: Task Scheduler security services are available only on Windows NT.
- 0x80041313: The task object version is either unsupported or invalid.
- 0x80041314: The task has been configured with an unsupported combination of account settings and run time options.
- 0x80041315: The Task Scheduler Service is not running.
- 0x80041316: The task XML contains an unexpected node.
- 0x80041317: The task XML contains an element or attribute from an unexpected namespace.
- 0x80041318: The task XML contains a value which is incorrectly formatted or out of range.
- 0x80041319: The task XML is missing a required element or attribute.
- 0x8004131A: The task XML is malformed.
- 0x0004131B: The task is registered, but not all specified triggers will start the task.
- 0x0004131C: The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal.
- 0x8004131D: The task XML contains too many nodes of the same type.
- 0x8004131E: The task cannot be started after the trigger end boundary.
- 0x8004131F: An instance of this task is already running.
- 0x80041320: The task will not run because the user is not logged on.
- 0x80041321: The task image is corrupt or has been tampered with.
- 0x80041322: The Task Scheduler service is not available.
- 0x80041323: The Task Scheduler service is too busy to handle your request. Please try again later.
- 0x80041324: The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.
- 0x00041325: The Task Scheduler service has asked the task to run.
- 0x80041326: The task is disabled.
- 0x80041327: The task has properties that are not compatible with earlier versions of Windows.
- 0x80041328: The task settings do not allow the task to start on demand.
- 0x80070002: The Task Scheduler cannot find the file.
- 0x800710E0: The operator or administrator has refused the request.
- 0xC000013A: The application terminated as a result of a CTRL+C.
- 0xC0000142: The application failed to initialize properly.

## Bugs

On Windows 2000 and Windows XP, when a computer is prepared for disk imaging with the sysprep utility, it cannot run tasks configured to run in the context of the SYSTEM account. Sysprep changes the security identifier (SID) to avoid duplication but does not update scheduled tasks to use the new SID. Consequently, the affected tasks fail to run. There is no solution for this problem but one may reschedule the affected tasks to work around the issue.

On Windows Vista or Windows Server 2008, the next execution time displayed in Task Scheduler may be wrong. Microsoft issued a hotfix to remedy this issue.
