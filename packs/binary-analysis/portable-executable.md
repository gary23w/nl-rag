---
title: "Portable Executable"
source: https://en.wikipedia.org/wiki/Portable_Executable
domain: binary-analysis
license: CC-BY-SA-4.0
tags: static binary analysis, executable format inspection, control flow graph recovery, symbol table analysis, machine code inspection
fetched: 2026-07-02
---

# Portable Executable

**Portable Executable** (**PE**) is a file format for native executable code on 32-bit and 64-bit Windows operating systems, as well as in UEFI environments. It is used for native executables (.exe, .com), dynamic link libraries (.dll, .ocx), system drivers (.sys, .drv) and many other types of files. The PE format supports storing the data required to load and start an operating system process – including references to dynamic link libraries, tables for importing and exporting application programming interface (API) functions, resource management data and thread-local storage (TLS) information.

According to the Unified Extensible Firmware Interface (UEFI) specification, the PE format is also the accepted standard for executables in EFI environments. On Windows NT systems, it currently supports a range of instruction sets, including IA-32, x86-64 (AMD64/Intel 64), IA-64, ARM and ARM64. Before the advent of Windows 2000, Windows NT (and by extension the PE format) also supported MIPS, Alpha, and PowerPC architectures. Moreover, thanks to its use in Windows CE, PE has maintained compatibility with several MIPS, ARM (including Thumb), and SuperH variants.

Functionally, the PE format is similar to other platform-specific executable formats, such as the ELF format used in Linux and most Unix-like systems, and the Mach-O format found in macOS and iOS.

## History

Microsoft first introduced the PE format with Windows NT 3.1, replacing the older 16-bit New Executable (NE) format. Soon after, Windows 95, 98, ME, and the Win32s extension for Windows 3.1x, all adopted the PE structure. Each PE file includes a DOS executable header, which generally displays the message "This program cannot be run in DOS mode". However, this DOS section can be replaced by a fully functional DOS program, as demonstrated in the Windows 98 SE installer. Developers can add such a program using the `/STUB` switch with Microsoft's linker, effectively creating a fat binary.

Over time, the PE format has grown with the Windows platform. Notable extensions include the .NET PE format for managed code, PE32+ for 64-bit address space support, and a specialized version for Windows CE.

To determine whether a PE file is intended for 32-bit or 64-bit architectures, one can examine the Machine field in the IMAGE_FILE_HEADER. Common machine values are `0x014c` for 32-bit Intel processors and `0x8664` for x64 processors. Additionally, the Magic field in the `IMAGE_OPTIONAL_HEADER` reveals whether addresses are 32-bit or 64-bit. A value of `0x10B` indicates a 32-bit (PE32) file, while `0x20B` indicates a 64-bit (PE32+) file.

## Technical details

### Layout

A PE file consists of several headers and sections that instruct the dynamic linker on how to map the file into memory. An executable image consists of several different regions, each requiring different memory protection attributes. To ensure proper alignment, the start of each section must align to a page boundary. For instance, the *.text* section, which contains program code, is typically mapped as an execute/read-only. Conversely, the *.data* section, which holds global variables, is mapped as no-execute/read write. However, to conserve space, sections are not aligned on disk in this manner. The dynamic linker maps each section to memory individually and assigns the correct permissions based on the information in the headers.

### Import table

The *import address table* (IAT) is used as a lookup table when the application calls a function in a different module. The imports can be specified by ordinal or by name. Because a compiled program cannot know the memory locations of its dependent libraries beforehand, an indirect jump is necessary for API calls. As the dynamic linker holds modules and resolves dependencies, it populates the IAT slots with actual addresses of the corresponding library functions. Although this adds an extra jump, incurring a performance penalty compared to intermodular calls, it minimizes the number of memory pages that require copy-on-write changes, thus conserving memory and disk I/O. If a call is known to be intermodular beforehand (if indicated by a dllimport attribute), the compiler can generate optimized code with a simple indirect call opcode.

### Address Space Layout Randomization (ASLR)

Modern operating systems use address space layout randomization (ASLR), a process that makes a PE file's in-memory layout unpredictable and therefore harder to exploit. During ASLR, the loader randomizes the virtual addresses where key components reside. This includes the executable's base, shared libraries, the heap, and the stack. Most PE files are not position-independent because mainstream compilers emit some absolute references relative to an assumed base. To cope with randomized rebasing, the linker stores a .reloc table that lets the loader adjust those references at load time.

## .NET, metadata, and the PE format

In a .NET executable, the PE code section contains a stub that invokes the CLR virtual machine startup entry, `_CorExeMain` or `_CorDllMain` in `mscoree.dll`, much like it was in Visual Basic executables. The virtual machine then makes use of .NET metadata present, the root of which, `IMAGE_COR20_HEADER` (also called "CLR header") is pointed to by `IMAGE_DIRECTORY_ENTRY_COMHEADER` (the entry was previously used for COM+ metadata in COM+ applications, hence the name) entry in the PE header's data directory. `IMAGE_COR20_HEADER` strongly resembles PE's optional header, essentially playing its role for the CLR loader.

The CLR-related data, including the root structure itself, is typically contained in the common code section, `.text`. It is composed of a few directories: metadata, embedded resources, strong names and a few for native-code interoperability. Metadata directory is a set of tables that list all the distinct .NET entities in the assembly, including types, methods, fields, constants, events, as well as references between them and to other assemblies.

## Use on other operating systems

The PE format is also used by ReactOS, an open-source operating system created to be binary-compatible with Windows. Historically, it has also been used by other operating systems such as SkyOS and BeOS R3. However, both SkyOS and BeOS eventually moved to ELF.

The Mono development platform, which aims to be binary compatible with the Microsoft .NET Framework, uses the same PE format as the Microsoft implementation. The same goes for Microsoft's own cross-platform .NET Core.

On x86(-64) Unix-like operating systems, Windows binaries (in PE format) can be executed using Wine. The HX DOS Extender also uses the PE format for native DOS 32-bit binaries, and can execute some Windows binaries in DOS, thus acting like an equivalent of Wine for DOS.

Mac OS X 10.5 has the ability to load and parse PE files, although it does not maintain binary compatibility with Windows.

UEFI and UEFI firmware use PE files, as well as the platform related ABI and calling convention (x64 ABI for typical PC devices) for applications.
