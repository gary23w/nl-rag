---
title: "Dynamic-link library"
source: https://en.wikipedia.org/wiki/Dynamic-link_library
domain: wine-compatibility-layer
license: CC-BY-SA-4.0
tags: wine compatibility layer, windows api reimplementation, dxvk translation, compatibility layer
fetched: 2026-07-02
---

# Dynamic-link library

**Dynamic-link library** (**DLL**) is Microsoft's implementation of the shared library concept in the Microsoft Windows and OS/2 operating systems. These libraries usually have the file extension `DLL`, `OCX` (for libraries containing ActiveX controls), or `DRV` (for legacy system drivers). The file formats for DLLs are the same as for Windows EXE files – that is, Portable Executable (PE) for 32-bit and 64-bit Windows, and New Executable (NE) for 16-bit Windows. As with EXEs, DLLs can contain code, data, and resources, in any combination.

Data files with the same file format as a DLL, but with different file extensions and possibly containing only resource sections, can be called *resource DLLs*. Examples of such DLLs include *icon libraries*, sometimes having the extension `ICL`, and font files, having the extensions `FON` and `FOT`.

## Background

The first versions of Microsoft Windows ran programs together in a single address space. Every program was meant to co-operate by yielding the CPU to other programs so that the graphical user interface (GUI) could multitask and be maximally responsive. All operating-system level operations were provided by the underlying operating system: MS-DOS. All higher-level services were provided by Windows Libraries "Dynamic Link Library". The Drawing API, Graphics Device Interface (GDI), was implemented in a DLL called `GDI.EXE`, the user interface in `USER.EXE`. These extra layers on top of DOS had to be shared across all running Windows programs, not just to enable Windows to work in a machine with less than a megabyte of RAM, but to enable the programs to co-operate with each other. The code in GDI needed to translate drawing commands to operations on specific devices. On the display, it had to manipulate pixels in the frame buffer. When drawing to a printer, the API calls had to be transformed into requests to a printer. Although it could have been possible to provide hard-coded support for a limited set of devices (like the Color Graphics Adapter display, the HP LaserJet Printer Command Language), Microsoft chose a different approach. GDI would work by loading different pieces of code, called "device drivers", to work with different output devices.

The same architectural concept that allowed GDI to load different device drivers also allowed the Windows shell to load different Windows programs, and for these programs to invoke API calls from the shared USER and GDI libraries. That concept was "dynamic linking".

In a conventional non-shared static library, sections of code are simply added to the calling program when its executable is built at the "linking" phase; if two programs call the same routine, the routine is included in both the programs during the linking stage of the two. With dynamic linking, shared code is placed into a single, separate file. The programs that call this file are connected to it at run time, with the operating system (or, in the case of early versions of Windows, the OS-extension), performing the binding.

For those early versions of Windows (1.0 to 3.11), the DLLs were the foundation for the entire GUI. As such, display drivers were merely DLLs with a .DRV extension that provided custom implementations of the same drawing API through a unified device driver interface (DDI), and the Drawing (GDI) and GUI (USER) APIs were merely the function calls exported by the GDI and USER, system DLLs with .EXE extension.

This notion of building up the operating system from a collection of dynamically loaded libraries is a core concept of Windows that persists as of 2015. DLLs provide the standard benefits of shared libraries, such as modularity. Modularity allows changes to be made to code and data in a single self-contained DLL shared by several applications without any change to the applications themselves.

Another benefit of modularity is the use of generic interfaces for plug-ins. A single interface may be developed which allows old as well as new modules to be integrated seamlessly at run-time into pre-existing applications, without any modification to the application itself. This concept of dynamic extensibility is taken to the extreme with the Component Object Model, the underpinnings of ActiveX.

In Windows 1.x, 2.x and 3.x, all Windows applications shared the same address space as well as the same memory. A DLL was only loaded once into this address space; from then on, all programs using the library accessed it. The library's data was shared across all the programs. This could be used as an indirect form of inter-process communication, or it could accidentally corrupt the different programs. With the introduction of 32-bit libraries in Windows 95, every process ran in its own address space. While the DLL code may be shared, the data is private except where shared data is explicitly requested by the library. That said, large swathes of Windows 95, Windows 98 and Windows Me were built from 16-bit libraries, which limited the performance of the Pentium Pro microprocessor when launched, and ultimately limited the stability and scalability of the DOS-based versions of Windows.

Although DLLs are the core of the Windows architecture, they have several drawbacks, collectively called "DLL hell". As of 2015 Microsoft promotes .NET Framework as one solution to the problems of DLL hell, although they now promote virtualization-based solutions such as Microsoft Virtual PC and Microsoft Application Virtualization, because they offer superior isolation between applications. An alternative mitigating solution to DLL hell has been to implement side-by-side assembly.

## Features

Since DLLs are essentially the same as EXEs, the choice of which to produce as part of the linking process is for clarity, since it is possible to export functions and data from either.

It is not possible to directly execute a DLL, since it requires an EXE for the operating system to load it through an entry point, hence the existence of utilities like RUNDLL.EXE or RUNDLL32.EXE which provide the entry point and minimal framework for DLLs that contain enough functionality to execute without much support.

DLLs provide a mechanism for shared code and data, allowing a developer of shared code/data to upgrade functionality without requiring applications to be re-linked or re-compiled. From the application development point of view, Windows and OS/2 can be thought of as a collection of DLLs that are upgraded, allowing applications for one version of the OS to work in a later one, provided that the OS vendor has ensured that the interfaces and functionality are compatible.

DLLs execute in the memory space of the calling process and with the same access permissions, which means there is little overhead in their use, but also that there is no protection for the calling program if the DLL has any sort of bug.

### Memory management

In Windows API, DLL files are organized into *sections*. Each section has its own set of attributes, such as being writable or read-only, executable (for code) or non-executable (for data), and so on.

The code in a DLL is usually shared among all the processes that use the DLL; that is, they occupy a single place in physical memory, and do not take up space in the page file. Windows does not use position-independent code for its DLLs; instead, the code undergoes relocation as it is loaded, fixing addresses for all its entry points at locations which are free in the memory space of the first process to load the DLL. In older versions of Windows, in which all running processes occupied a single common address space, a single copy of the DLL's code would always be sufficient for all the processes. However, in newer versions of Windows which use separate address spaces for each program, it is only possible to use the same relocated copy of the DLL in multiple programs if each program has the same virtual addresses free to accommodate the DLL's code. If some programs (or their combination of already-loaded DLLs) do not have those addresses free, then an additional physical copy of the DLL's code will need to be created, using a different set of relocated entry points. If the physical memory occupied by a code section is to be reclaimed, its contents are discarded, and later reloaded directly from the DLL file as necessary.

In contrast to code sections, the data sections of a DLL are usually private; that is, each process using the DLL has its own copy of all the DLL's data. Optionally, data sections can be made shared, allowing inter-process communication via this shared memory area. However, because user restrictions do not apply to the use of shared DLL memory, this creates a security hole; namely, one process can corrupt the shared data, which will likely cause all other sharing processes to behave undesirably. For example, a process running under a guest account can in this way corrupt another process running under a privileged account. This is an important reason to avoid the use of shared sections in DLLs.

If a DLL is compressed by certain executable packers (e.g. UPX), all of its code sections are marked as read and write, and will be unshared. Read-and-write code sections, much like private data sections, are private to each process. Thus DLLs with shared data sections should not be compressed if they are intended to be used simultaneously by multiple programs, since each program instance would have to carry its own copy of the DLL, resulting in increased memory consumption.

### Import libraries

Like static libraries, import libraries for DLLs are noted by the `.lib` file extension. For example, kernel32.dll, the primary dynamic library for Windows's base functions such as file creation and memory management, is linked via `kernel32.lib`. The usual way to tell an import library from a proper static library is by size: the import library is much smaller as it only contains symbols referring to the actual DLL, to be processed at link-time. Both nevertheless are Unix ar format files.

Linking to dynamic libraries is usually handled by linking to an import library when building or linking to create an executable file. The created executable then contains an import address table (IAT) by which all DLL function calls are referenced (each referenced DLL function contains its own entry in the IAT). At run-time, the IAT is filled with appropriate addresses that point directly to a function in the separately loaded DLL.

In Cygwin/MSYS and MinGW, import libraries are conventionally given the suffix `.dll.a`, combining both the Windows DLL suffix and the Unix ar suffix. The file format is similar, but the symbols used to mark the imports are different (`_head_foo_dll` vs `__IMPORT_DESCRIPTOR_foo`). Although its GNU Binutils toolchain can generate import libraries and link to them, it is faster to link to the DLL directly. An experimental tool in MinGW called genlib can be used to generate import libs with MSVC-style symbols.

### Symbol resolution and binding

Each function exported by a DLL is identified by a numeric ordinal and optionally a name. Likewise, functions can be imported from a DLL either by ordinal or by name. The ordinal represents the position of the function's address pointer in the DLL Export Address table. It is common for internal functions to be exported by ordinal only. For most Windows API functions only the names are preserved across different Windows releases; the ordinals are subject to change. Thus, one cannot reliably import Windows API functions by their ordinals.

Importing functions by ordinal provides only slightly better performance than importing them by name: export tables of DLLs are ordered by name, so a binary search can be used to find a function. The index of the found name is then used to look up the ordinal in the Export Ordinal table. In 16-bit Windows, the name table was not sorted, so the name lookup overhead was much more noticeable.

It is also possible to *bind* an executable to a specific version of a DLL, that is, to resolve the addresses of imported functions at compile-time. For bound imports, the linker saves the timestamp and checksum of the DLL to which the import is bound. At run-time, Windows checks to see if the same version of library is being used, and if so, Windows bypasses processing the imports. Otherwise, if the library is different from the one which was bound to, Windows processes the imports in a normal way.

Bound executables load somewhat faster if they are run in the same environment that they were compiled for, and exactly the same time if they are run in a different environment, so there is no drawback for binding the imports. For example, all the standard Windows applications are bound to the system DLLs of their respective Windows release. A good opportunity to bind an application's imports to its target environment is during the application's installation. This keeps the libraries "bound" until the next OS update. It does, however, change the checksum of the executable, so it is not something that can be done with signed programs, or programs that are managed by a configuration management tool that uses checksums (such as MD5 checksums) to manage file versions. As more recent Windows versions have moved away from having fixed addresses for every loaded library (for security reasons), the opportunity and value of binding an executable is decreasing.

### Explicit run-time linking

DLL files may be explicitly loaded at run-time, a process referred to simply as *run-time dynamic linking* by Microsoft, by using the `LoadLibrary` (or `LoadLibraryEx`) API function. The `GetProcAddress` API function is used to look up exported symbols by name, and `FreeLibrary` – to unload the DLL. These functions are analogous to `dlopen`, `dlsym`, and `dlclose` in the POSIX standard API.

The procedure for explicit run-time linking is the same in any language that supports pointers to functions, since it depends on the Windows API rather than language constructs.

### Delayed loading

Normally, an application that is linked against a DLL’s import library will fail to start if the DLL cannot be found, because Windows will not run the application unless it can find all of the DLLs that the application may need. However an application may be linked against an import library to allow delayed loading of the dynamic library. In this case, the operating system will not try to find or load the DLL when the application starts; instead, a stub is included in the application by the linker which will try to find and load the DLL through `LoadLibrary` and `GetProcAddress` when one of its functions is called. If the DLL cannot be found or loaded, or the called function does not exist, the application will generate an exception, which may be caught and handled appropriately. If the application does not handle the exception, it will be caught by the operating system, which will terminate the program with an error message.

The delayed loading mechanism also provides notification hooks, allowing the application to perform additional processing or error handling when the DLL is loaded and/or any DLL function is called.

## Compiler and language considerations

### Delphi

In a source file, the keyword `library` is used instead of `program`. At the end of the file, the functions to be exported are listed in `exports` clause.

Delphi does not need `LIB` files to import functions from DLLs; to link to a DLL, the `external` keyword is used in the function declaration to signal the DLL name, followed by `name` to name the symbol (if different) or `index` to identify the index.

### Microsoft Visual Basic

In Visual Basic (VB), only run-time linking is supported; but in addition to using `LoadLibrary` and `GetProcAddress` API functions, *declarations* of imported functions are allowed.

When importing DLL functions through declarations, VB will generate a run-time error if the `DLL` file cannot be found. The developer can catch the error and handle it appropriately.

When creating DLLs in VB, the IDE will only allow creation of ActiveX DLLs, however methods have been created to allow the user to explicitly tell the linker to include a .DEF file which defines the ordinal position and name of each exported function. This allows the user to create a standard Windows DLL using Visual Basic (Version 6 or lower) which can be referenced through a "Declare" statement.

### C and C++

Microsoft Visual C++ (MSVC) provides several extensions to standard C++ which allow functions to be specified as imported or exported directly in the C++ code; these have been adopted by other Windows C and C++ compilers, including Windows versions of GCC. These extensions use the attribute `__declspec` before a function declaration. Note that when C functions are accessed from C++, they must also be declared as `extern "C"` in C++ code, to inform the compiler that the C linkage should be used.

Besides specifying imported or exported functions using `__declspec` attributes, they may be listed in IMPORT or EXPORTS section of the `DEF` file used by the project. The `DEF` file is processed by the linker, rather than the compiler, and thus it is not specific to C++.

DLL compilation will produce both `DLL` and `LIB` files. The `LIB` file (import library) is used to link against a DLL at compile-time; it is not necessary for run-time linking. Unless the DLL is a Component Object Model (COM) server, the `DLL` file must be placed in one of the directories listed in the PATH environment variable, in the default system directory, or in the same directory as the program using it. COM server DLLs are registered using regsvr32.exe, which places the DLL's location and its globally unique ID (GUID) in the registry. Programs can then use the DLL by looking up its GUID in the registry to find its location or create an instance of the COM object indirectly using its class identifier and interface identifier.

## Programming examples

### Using DLL imports

The following examples show how to use language-specific bindings to import symbols for linking against a DLL at compile-time.

**Delphi**

```mw
{$APPTYPE CONSOLE}

program Example;

// import function that adds two numbers
function AddNumbers(a, b : Double): Double; StdCall; external 'Example.dll';

// main program
var
   R: Double;

begin
  R := AddNumbers(1, 2);
  Writeln('The result was: ', R);
end.
```

**C**

'Example.lib' file must be included (assuming that Example.dll is generated) in the project before static linking. The file 'Example.lib' is automatically generated by the compiler when compiling the DLL. Not executing the above statement would cause linking error as the linker would not know where to find the definition of `AddNumbers`. The DLL file 'Example.dll' may also have to be copied to the location where the .exe file would be generated by the following code:

```mw
#include <windows.h>
#include <stdio.h>

// Import function that adds two numbers
extern "C" __declspec(dllimport) double AddNumbers(double a, double b);

int main(int argc, char *argv[])
{
    double result = AddNumbers(1, 2);
    printf("The result was: %f\n", result);
    return 0;
}
```

### Using explicit run-time linking

The following examples show how to use the run-time loading and linking facilities using language-specific Windows API bindings.

Note that all of the four samples are vulnerable to DLL preloading attacks, since example.dll can be resolved to a place unintended by the author (the current working directory goes *before* system library locations), and thus to a malicious version of the library. See the reference for Microsoft's guidance on safe library loading: one should use `SetDllDirectoryW` in `kernel32` to remove the current-directory lookup before any libraries are loaded.

#### Microsoft Visual Basic

```mw
Option Explicit
Declare Function AddNumbers Lib "Example.dll" _
(ByVal a As Double, ByVal b As Double) As Double

Sub Main()
	Dim Result As Double
	Result = AddNumbers(1, 2)
	Debug.Print "The result was: " & Result
End Sub
```

#### Delphi

```mw
program Example;
  {$APPTYPE CONSOLE}
  uses Windows;
  var
  AddNumbers:function (a, b: integer): Double; StdCall;
  LibHandle:HMODULE;
begin
  LibHandle := LoadLibrary('example.dll');
  if LibHandle <> 0 then
    AddNumbers := GetProcAddress(LibHandle, 'AddNumbers');
  if Assigned(AddNumbers) then
    Writeln( '1 + 2 = ', AddNumbers( 1, 2 ) );
  Readln;
end.
```

#### C

```mw
#include <windows.h>
#include <stdio.h>

// DLL function signature
typedef double (*importFunction)(double, double);

int main(int argc, char **argv)
{
	importFunction addNumbers;
	double result;
	HINSTANCE hinstLib;

	// Load DLL file
	hinstLib = LoadLibrary(TEXT("Example.dll"));
	if (hinstLib == NULL) {
		printf("ERROR: unable to load DLL\n");
		return 1;
	}

	// Get function pointer
	addNumbers = (importFunction) GetProcAddress(hinstLib, "AddNumbers");
	if (addNumbers == NULL) {
		printf("ERROR: unable to find DLL function\n");
		FreeLibrary(hinstLib);
		return 1;
	}

	// Call function.
	result = addNumbers(1, 3);

	// Unload DLL file
	FreeLibrary(hinstLib);

	// Display result
	printf("The result was: %f\n", result);

	return 0;
}
```

#### Python

The Python ctypes binding will use POSIX API on POSIX systems.

```mw
import ctypes

my_dll = ctypes.cdll.LoadLibrary("Example.dll")

# The following "restype" method specification is needed to make
# Python understand what type is returned by the function.
my_dll.AddNumbers.restype = ctypes.c_double

p = my_dll.AddNumbers(ctypes.c_double(1.0), ctypes.c_double(2.0))

print("The result was:", p)
```

## Component Object Model

The Component Object Model (COM) defines a binary standard to host the implementation of objects in DLL and EXE files. It provides mechanisms to locate and version those files as well as a language-independent and machine-readable description of the interface. Hosting COM objects in a DLL is more lightweight and allows them to share resources with the client process. This allows COM objects to implement powerful back-ends to simple GUI front ends such as Visual Basic and ASP. They can also be programmed from scripting languages.

## DLL hijacking

Due to a vulnerability commonly known as DLL hijacking, DLL spoofing, DLL preloading or binary planting, many programs will load and execute a malicious DLL contained in the same folder as a data file opened by these programs. The vulnerability was discovered by Georgi Guninski in 2000. In August 2010 it gained worldwide publicity after ACROS Security rediscovered it again and many hundreds of programs were found vulnerable. Programs that are run from unsafe locations, i.e. user-writable folders like the *Downloads* or the *Temp* directory, are almost always susceptible to this vulnerability.
