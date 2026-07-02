---
title: "Windows Native API"
source: https://en.wikipedia.org/wiki/Native_API
domain: windows-internals
license: CC-BY-SA-4.0
tags: windows internals, windows nt architecture, native api, windows registry
fetched: 2026-07-02
---

# Windows Native API

(Redirected from

Native API

)

The **Native API** is a lightweight application programming interface (API) used by Windows NT's kernel and user mode applications. This API is used in the early stages of Windows NT startup process, when other components and APIs are still unavailable. Therefore, a few Windows components, such as the Client/Server Runtime Subsystem (CSRSS), are implemented using the Native API. The Native API is also used by subroutines such as those in kernel32.dll that implement the Windows API, the API based on which most of the Windows components are created.

Most of the Native API calls are implemented in ntoskrnl.exe and are exposed to user mode by **ntdll.dll**. The entry point of ntdll.dll is `LdrInitializeThunk`. Native API calls are handled by the kernel via the System Service Descriptor Table (SSDT).

## Function groups

The Native API comprises many functions. They include C runtime functions that are needed for a very basic C runtime execution, such as strlen(), sprintf(), memcpy() and floor(). Other common procedures like malloc(), printf(), scanf() are missing (the first because it does not specify a heap to allocate memory from and the second and third because they use the console, accessed only via KERNEL32.DLL). The vast majority of other Native API routines, by convention, have a 2 or 3 letter prefix, which is:

- **Nt** or **Zw** are system calls declared in ntdll.dll and ntoskrnl.exe. When called from ntdll.dll in user mode, these groups are almost exactly the same; they execute an interrupt into kernel mode and call the equivalent function in ntoskrnl.exe via the SSDT. When calling the functions directly in ntoskrnl.exe (only possible in kernel mode), the Zw variants ensure kernel mode, whereas the Nt variants do not. The Zw prefix does not stand for anything.
- **Rtl** is the second largest group of ntdll calls. These comprise the (extended) C Run-Time Library, which includes many utility functions that can be used by native applications, yet don't directly involve kernel support.
- **Csr** are client-server functions that are used to communicate with the Win32 subsystem process, csrss.exe (*csrss* stands for client/server runtime sub-system).
- **Dbg** are debugging functions such as a software breakpoint.
- **Ki** are upcalls from kernel mode for events like APC dispatching.
- **Ldr** are loader functions for PE file handling and starting of new processes.
- **Nls** for National Language Support (similar to code pages).
- **Pfx** for prefix handling.
- **Tp** for threadpool handling.

user32.dll and gdi32.dll include several other calls that execute an interrupt into kernel mode. These were not part of the original Windows NT design, as can be seen in Windows NT 3.5. However, due to performance issues of hardware of that age, it was decided to move the graphics subsystem into kernel mode. As such, system call in the range of 0x1000-0x1FFF are satisfied by win32k.sys (instead of ntoskrnl.exe as done for 0-0x0FFF), and are declared in user32.dll and gdi32.dll. These functions have the **NtUser** and **NtGdi** prefix (e.g. **NtUserLockWorkStation** and **NtGdiEnableEudc**).

## Uses

Uses of Native API functions includes but not limited to:

- Enabling and disabling privileges (RtlAdjustPrivilege)
- Creating remote threads within processes that are running in different session (RtlCreateUserThread)
- Running native applications (RtlCreateUserProcess)
- Performing a forced shutdown (NtShutdownSystem)
- Causing a BSOD in User mode (NtRaiseHardError)
- Displaying a string in Native Mode (NtDisplayString)
