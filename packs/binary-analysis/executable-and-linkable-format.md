---
title: "Executable and Linkable Format"
source: https://en.wikipedia.org/wiki/Executable_and_Linkable_Format
domain: binary-analysis
license: CC-BY-SA-4.0
tags: static binary analysis, executable format inspection, control flow graph recovery, symbol table analysis, machine code inspection
fetched: 2026-07-02
---

# Executable and Linkable Format

In computing, the **Executable and Linkable Format** (**ELF**, formerly named **Extensible Linking Format**) is a common standard file format for executable files, object code, shared libraries, device drivers, and core dumps. First published in the specification for the application binary interface (ABI) of the Unix operating system version named System V Release 4 (SVR4), and later in the Tool Interface Standard, it was quickly accepted among different vendors of Unix systems. In 1999, it was chosen as the standard binary file format for Unix and Unix-like systems on x86 processors by the 86open project.

By design, the ELF format is flexible, extensible, and cross-platform. For instance, it supports different endiannesses and address sizes so it does not exclude any particular CPU or instruction set architecture. This has allowed it to be adopted by many different operating systems on many different hardware platforms.

## File layout

Each ELF file is made up of one ELF header, followed by file data. The data can include:

- Program header table, describing zero or more memory segments
- Section header table, describing zero or more sections
- Data referred to by entries in the program header table or section header table

The segments contain information that is needed for run time execution of the file, while sections contain important data for linking and relocation. Any byte in the entire file can be owned by one section at most, and orphan bytes can occur which are unowned by any section.

### ELF header

The ELF header defines whether to use 32-bit or 64-bit addresses. The header contains three fields that are affected by this setting and offset other fields that follow them. The ELF header is 52 or 64 bytes long for 32-bit and 64-bit binaries, respectively.

| Offset | Size (bytes) | Field | Purpose |   |   |
|---|---|---|---|---|---|
| 32-bit | 64-bit | 32-bit | 64-bit |   |   |
| 0x00 | 4 | e_ident[EI_MAG0] through e_ident[EI_MAG3] | `0x7F` followed by `ELF`(`45 4c 46`) in ASCII; these four bytes constitute the magic number. |   |   |
| 0x04 | 1 | e_ident[EI_CLASS] | This byte is set to either `1` or `2` to signify 32- or 64-bit format, respectively. |   |   |
| 0x05 | 1 | e_ident[EI_DATA] | This byte is set to either `1` or `2` to signify little or big endianness, respectively. This affects interpretation of multi-byte fields starting with offset `0x10`. |   |   |
| 0x06 | 1 | e_ident[EI_VERSION] | Set to `1` for the original and current version of ELF. |   |   |
| 0x07 | 1 | e_ident[EI_OSABI] | Identifies the target operating system ABI. Value ABI 0x00 System V 0x01 HP-UX 0x02 NetBSD 0x03 Linux 0x04 GNU Hurd 0x06 Solaris 0x07 AIX (Monterey) 0x08 IRIX 0x09 FreeBSD 0x0A Tru64 0x0B Novell Modesto 0x0C OpenBSD 0x0D OpenVMS 0x0E NonStop Kernel 0x0F AROS 0x10 FenixOS 0x11 Nuxi CloudABI 0x12 Stratus Technologies OpenVOS |   |   |
| 0x08 | 1 | e_ident[EI_ABIVERSION] | Further specifies the ABI version. Its interpretation depends on the target ABI. Linux kernel (after at least 2.6) has no definition of it, so it is ignored for statically linked executables. In that case, offset and size of EI_PAD are `8`. glibc 2.12+ in case e_ident[EI_OSABI] == 3 treats this field as ABI version of the dynamic linker: it defines a list of dynamic linker's features, treats e_ident[EI_ABIVERSION] as a feature level requested by the shared object (executable or dynamic library) and refuses to load it if an unknown feature is requested, i.e. e_ident[EI_ABIVERSION] is greater than the largest known feature. |   |   |
| 0x09 | 7 | e_ident[EI_PAD] | Reserved padding bytes. Currently unused. Should be filled with zeros and ignored when read. |   |   |
| 0x10 | 2 | e_type | Identifies object file type. Value Type Meaning 0x00 ET_NONE Unknown. 0x01 ET_REL Relocatable file. 0x02 ET_EXEC Executable file. 0x03 ET_DYN Shared object. 0x04 ET_CORE Core file. 0xFE00 ET_LOOS Reserved inclusive range. Operating system specific. 0xFEFF ET_HIOS 0xFF00 ET_LOPROC Reserved inclusive range. Processor specific. 0xFFFF ET_HIPROC |   |   |
| 0x12 | 2 | e_machine | Specifies target instruction set architecture. Some examples are: Value ISA 0x00 No specific instruction set 0x01 AT&T WE 32100 0x02 SPARC 0x03 x86 0x04 Motorola 68000 (M68k) 0x05 Motorola 88000 (M88k) 0x06 Intel MCU 0x07 Intel 80860 0x08 MIPS 0x09 IBM System/370 0x0A MIPS RS3000 Little-endian 0x0B – 0x0E Reserved for future use 0x0F Hewlett-Packard PA-RISC 0x13 Intel 80960 0x14 PowerPC 0x15 PowerPC (64-bit) 0x16 S390, including S390x 0x17 IBM SPU/SPC 0x18 – 0x23 Reserved for future use 0x24 NEC V800 0x25 Fujitsu FR20 0x26 TRW RH-32 0x27 Motorola RCE 0x28 Arm (up to Armv7/AArch32) 0x29 Digital Alpha 0x2A SuperH 0x2B SPARC Version 9 0x2C Siemens TriCore embedded processor 0x2D Argonaut RISC Core 0x2E Hitachi H8/300 0x2F Hitachi H8/300H 0x30 Hitachi H8S 0x31 Hitachi H8/500 0x32 IA-64 0x33 Stanford MIPS-X 0x34 Motorola ColdFire 0x35 Motorola M68HC12 0x36 Fujitsu MMA Multimedia Accelerator 0x37 Siemens PCP 0x38 Sony nCPU embedded RISC processor 0x39 Denso NDR1 microprocessor 0x3A Motorola Star*Core processor 0x3B Toyota ME16 processor 0x3C STMicroelectronics ST100 processor 0x3D Advanced Logic Corp. TinyJ embedded processor family 0x3E AMD x86-64 0x3F Sony DSP Processor 0x40 Digital Equipment Corp. PDP-10 0x41 Digital Equipment Corp. PDP-11 0x42 Siemens FX66 microcontroller 0x43 STMicroelectronics ST9+ 8/16-bit microcontroller 0x44 STMicroelectronics ST7 8-bit microcontroller 0x45 Motorola MC68HC16 Microcontroller 0x46 Motorola MC68HC11 Microcontroller 0x47 Motorola MC68HC08 Microcontroller 0x48 Motorola MC68HC05 Microcontroller 0x49 Silicon Graphics SVx 0x4A STMicroelectronics ST19 8-bit microcontroller 0x4B Digital VAX 0x4C Axis Communications 32-bit embedded processor 0x4D Infineon Technologies 32-bit embedded processor 0x4E Element 14 64-bit DSP Processor 0x4F LSI Logic 16-bit DSP Processor 0x8C TMS320C6000 Family 0xAF MCST Elbrus e2k 0xB7 Arm 64-bits (Armv8/AArch64) 0xDC Zilog Z80 0xF3 RISC-V 0xF7 Berkeley Packet Filter 0x101 WDC 65C816 0x102 LoongArch |   |   |
| 0x14 | 4 | e_version | Set to `1` for the original version of ELF. |   |   |
| 0x18 | 4 | 8 | e_entry | This is the memory address of the entry point from where the process starts executing. This field is either 32 or 64 bits long, depending on the format defined earlier (byte 0x04). If the file doesn't have an associated entry point, then this holds zero. |   |
| 0x1C | 0x20 | 4 | 8 | e_phoff | Points to the start of the program header table. It usually follows the file header immediately following this one, making the offset `0x34` or `0x40` for 32- and 64-bit ELF executables, respectively. |
| 0x20 | 0x28 | 4 | 8 | e_shoff | Points to the start of the section header table. |
| 0x24 | 0x30 | 4 | e_flags | Interpretation of this field depends on the target architecture. |   |
| 0x28 | 0x34 | 2 | e_ehsize | Contains the size of this header, normally 64 Bytes for 64-bit and 52 Bytes for 32-bit format. |   |
| 0x2A | 0x36 | 2 | e_phentsize | Contains the size of a program header table entry. As explained below, this will typically be 0x20 (32-bit) or 0x38 (64-bit). |   |
| 0x2C | 0x38 | 2 | e_phnum | Contains the number of entries in the program header table. |   |
| 0x2E | 0x3A | 2 | e_shentsize | Contains the size of a section header table entry. As explained below, this will typically be 0x28 (32-bit) or 0x40 (64-bit). |   |
| 0x30 | 0x3C | 2 | e_shnum | Contains the number of entries in the section header table. |   |
| 0x32 | 0x3E | 2 | e_shstrndx | Contains index of the section header table entry that contains the section names. |   |
| 0x34 | 0x40 |   | End of ELF Header (size). |   |   |

### Example hexdump

```mw
00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  02 00 3e 00 01 00 00 00  c5 48 40 00 00 00 00 00  |..>......H@.....|
```

### Program header

The program header table tells the system how to create a process image. It is found at file offset e_phoff, and consists of e_phnum entries, each with size e_phentsize. The layout is slightly different in 32-bit ELF vs 64-bit ELF, because the p_flags are in a different structure location for alignment reasons. Each entry is structured as:

| Offset | Size (bytes) | Field | Purpose |   |   |
|---|---|---|---|---|---|
| 32-bit | 64-bit | 32-bit | 64-bit |   |   |
| 0x00 | 4 | p_type | Identifies the type of the segment. Value Name Meaning 0x00000000 PT_NULL Program header table entry unused. 0x00000001 PT_LOAD Loadable segment. 0x00000002 PT_DYNAMIC Dynamic linking information. 0x00000003 PT_INTERP Interpreter information. 0x00000004 PT_NOTE Auxiliary information. 0x00000005 PT_SHLIB Reserved. 0x00000006 PT_PHDR Segment containing program header table itself. 0x00000007 PT_TLS Thread-Local Storage template. 0x60000000 PT_LOOS Reserved inclusive range. Operating system specific. 0x6FFFFFFF PT_HIOS 0x70000000 PT_LOPROC Reserved inclusive range. Processor specific. 0x7FFFFFFF PT_HIPROC |   |   |
|   | 0x04 |   | 4 | p_flags | Segment-dependent flags (position for 64-bit structure). Value Name Meaning 0x1 PF_X Executable segment. 0x2 PF_W Writeable segment. 0x4 PF_R Readable segment. |
| 0x04 | 0x08 | 4 | 8 | p_offset | Offset of the segment in the file image. |
| 0x08 | 0x10 | 4 | 8 | p_vaddr | Virtual address of the segment in memory. |
| 0x0C | 0x18 | 4 | 8 | p_paddr | On systems where physical address is relevant, reserved for segment's physical address. |
| 0x10 | 0x20 | 4 | 8 | p_filesz | Size in bytes of the segment in the file image. May be 0. |
| 0x14 | 0x28 | 4 | 8 | p_memsz | Size in bytes of the segment in memory. May be 0. |
| 0x18 |   | 4 |   | p_flags | Segment-dependent flags (position for 32-bit structure). See above `p_flags` field for flag definitions. |
| 0x1C | 0x30 | 4 | 8 | p_align | `0` and `1` specify no alignment. Otherwise should be a positive, integral power of 2, with p_vaddr equating p_offset modulus p_align. |
| 0x20 | 0x38 |   | End of Program Header (size). |   |   |

### Section header

| Offset | Size (bytes) | Field | Purpose |   |   |
|---|---|---|---|---|---|
| 32-bit | 64-bit | 32-bit | 64-bit |   |   |
| 0x00 | 4 | sh_name | An offset to a string in the **.shstrtab** section that represents the name of this section. |   |   |
| 0x04 | 4 | sh_type | Identifies the type of this header. Value Name Meaning 0x0 SHT_NULL Section header table entry unused 0x1 SHT_PROGBITS Program data 0x2 SHT_SYMTAB Symbol table 0x3 SHT_STRTAB String table 0x4 SHT_RELA Relocation entries with addends 0x5 SHT_HASH Symbol hash table 0x6 SHT_DYNAMIC Dynamic linking information 0x7 SHT_NOTE Notes 0x8 SHT_NOBITS Program space with no data (bss) 0x9 SHT_REL Relocation entries, no addends 0x0A SHT_SHLIB Reserved 0x0B SHT_DYNSYM Dynamic linker symbol table 0x0E SHT_INIT_ARRAY Array of constructors 0x0F SHT_FINI_ARRAY Array of destructors 0x10 SHT_PREINIT_ARRAY Array of pre-constructors 0x11 SHT_GROUP Section group 0x12 SHT_SYMTAB_SHNDX Extended section indices 0x13 SHT_NUM Number of defined types. 0x60000000 SHT_LOOS Start OS-specific. ... ... ... |   |   |
| 0x08 | 4 | 8 | sh_flags | Identifies the attributes of the section. Value Name Meaning 0x1 SHF_WRITE Writable 0x2 SHF_ALLOC Occupies memory during execution 0x4 SHF_EXECINSTR Executable 0x10 SHF_MERGE Might be merged 0x20 SHF_STRINGS Contains null-terminated strings 0x40 SHF_INFO_LINK 'sh_info' contains SHT index 0x80 SHF_LINK_ORDER Preserve order after combining 0x100 SHF_OS_NONCONFORMING Non-standard OS specific handling required 0x200 SHF_GROUP Section is member of a group 0x400 SHF_TLS Section hold thread-local data 0x0FF00000 SHF_MASKOS OS-specific 0xF0000000 SHF_MASKPROC Processor-specific 0x4000000 SHF_ORDERED Special ordering requirement (Solaris) 0x8000000 SHF_EXCLUDE Section is excluded unless referenced or allocated (Solaris) |   |
| 0x0C | 0x10 | 4 | 8 | sh_addr | Virtual address of the section in memory, for sections that are loaded. |
| 0x10 | 0x18 | 4 | 8 | sh_offset | Offset of the section in the file image. |
| 0x14 | 0x20 | 4 | 8 | sh_size | Size in bytes of the section. May be 0. |
| 0x18 | 0x28 | 4 | sh_link | Contains the section index of an associated section. This field is used for several purposes, depending on the type of section. |   |
| 0x1C | 0x2C | 4 | sh_info | Contains extra information about the section. This field is used for several purposes, depending on the type of section. |   |
| 0x20 | 0x30 | 4 | 8 | sh_addralign | Contains the required alignment of the section. This field must be a power of two. |
| 0x24 | 0x38 | 4 | 8 | sh_entsize | Contains the size, in bytes, of each entry, for sections that contain fixed-size entries. Otherwise, this field contains zero. |
| 0x28 | 0x40 |   | End of Section Header (size). |   |   |

## Tools

- `readelf` is a Unix binary utility that displays information about one or more ELF files. A free software implementation is provided by GNU Binutils.
- `elfutils` provides alternative tools to GNU Binutils purely for Linux.
- `elfdump` is a command for viewing ELF information in an ELF file, available under Solaris and FreeBSD.
- `objdump` provides a wide range of information about ELF files and other object formats. `objdump` uses the Binary File Descriptor library as a back-end to structure the ELF data.
- The Unix `file` utility can display some information about ELF files, including the instruction set architecture for which the code in a relocatable, executable, or shared object file is intended, or on which an ELF core dump was produced.

## Applications

### Unix-like systems

The ELF format has replaced older executable formats in various environments. It has replaced a.out and COFF formats in Unix-like operating systems:

- Linux
- Solaris / Illumos
- IRIX
- FreeBSD
- NetBSD
- OpenBSD
- Redox
- DragonFly BSD
- Syllable
- HP-UX (except for 32-bit PA-RISC programs which continue to use SOM)
- QNX Neutrino
- MINIX

### Non-Unix adoption

ELF has also seen some adoption in non-Unix operating systems, such as:

- OpenVMS, in its Itanium and amd64 versions
- BeOS Revision 4 and later for x86 based computers (where it replaced the Portable Executable format; the PowerPC version stayed with Preferred Executable Format)
- Haiku, an open source reimplementation of BeOS
- RISC OS
- Stratus VOS, in PA-RISC and x86 versions
- SkyOS
- Fuchsia OS
- Z/TPF
- HPE NonStop OS
- Deos

Microsoft Windows also uses the ELF format, but only for its Windows Subsystem for Linux compatibility system.

### Game consoles

Some game consoles also use ELF:

- PlayStation Portable, PlayStation Vita, PlayStation, PlayStation 2, PlayStation 3, PlayStation 4, PlayStation 5
- GP2X
- Dreamcast
- GameCube
- Nintendo 64
- Wii
- Wii U

### PowerPC

Other (operating) systems running on PowerPC that use ELF:

- AmigaOS 4, the ELF executable has replaced the prior Extended Hunk Format (EHF) which was used on Amigas equipped with PPC processor expansion cards.
- MorphOS
- AROS
- Café OS (The operating system run by the Wii U)

### Mobile phones

Some operating systems for mobile phones and mobile devices use ELF:

- Symbian OS v9 uses E32Image format that is based on the ELF file format;
- Sony Ericsson, for example, the W800i, W610, W300, etc.
- Siemens, the SGOLD and SGOLD2 platforms: from Siemens C65 to S75 and BenQ-Siemens E71/EL71;
- Motorola, for example, the E398, SLVR L7, v360, v3i (and all phone LTE2 which has the patch applied).
- Bada, for example, the Samsung Wave S8500.
- Nokia phones or tablets running the Maemo or the Meego OS, for example, the Nokia N900.
- Android uses ELF .so (shared object) libraries for the Java Native Interface. With Android Runtime (ART), the default since Android 5.0 "Lollipop", all applications are compiled into native ELF binaries on installation. It's also possible to use native Linux software from package managers like Termux, or compile them from sources via Clang or GCC, that are available in repositories.

Some phones can run ELF files through the use of a patch that adds assembly code to the main firmware, which is a feature known as *ELFPack* in the underground modding culture. The ELF file format is also used with the Atmel AVR (8-bit), AVR32 and with Texas Instruments MSP430 microcontroller architectures. Some implementations of Open Firmware can also load ELF files, most notably Apple's implementation used in almost all PowerPC machines the company produced.

### Blockchain platforms

- Solana uses ELF format for its on-chain programs (smart contracts). The platform processes ELF files compiled to BPF (Berkeley Packet Filter) byte-code, which are then deployed as shared objects and executed in Solana's runtime environment. The BPF loader validates and processes these ELF files during program deployment.

## Specifications

| Architecture | Specification |
|---|---|
| Generic | *System V Application Binary Interface* Edition 4.1 (1997-03-18) *System V ABI Update* (October 2009) |
| AMD64 | *System V ABI, AMD64 Supplement* |
| Arm | *ELF for the ARM Architecture* |
| IA-32 | *System V ABI, Intel386 Architecture Processor Supplement* |
| IA-64 | *Itanium Software Conventions and Runtime Guide* (September 2000) |
| M32R | *M32R ELF ABI Supplement Archived 2022-05-12 at the Wayback Machine* Version 1.2 (2004-08-26) |
| MIPS | *System V ABI, MIPS RISC Processor Supplement* *MIPS EABI documentation Archived 2012-04-01 at the Wayback Machine* (2003-06-11) |
| Motorola 6800 | *Motorola 8- and 16- bit Embedded ABI* |
| PA-RISC | *ELF Supplement for PA-RISC* Version 1.43 (October 6, 1997) |
| PowerPC | *System V ABI, PPC Supplement* *PowerPC Embedded Application Binary Interface 32-Bit Implementation* (1995-10-01) *64-bit PowerPC ELF Application Binary Interface Supplement* Version 1.9 (2004) |
| RISC-V | *RISC-V ELF Specification* |
| SPARC | *System V ABI, SPARC Supplement* |
| S/390 | *S/390 32bit ELF ABI Supplement* |
| zSeries | *zSeries 64bit ELF ABI Supplement* |
| Symbian OS 9 | *E32Image file format on Symbian OS 9* |

The Linux Standard Base (LSB) supplements some of the above specifications for architectures in which it is specified. For example, that is the case for the System V ABI, AMD64 Supplement.

## 86open

**86open** was a project to form consensus on a common binary file format for Unix and Unix-like operating systems on the common PC compatible x86 architecture, to encourage software developers to port to the architecture. The initial idea was to standardize on a small subset of Spec 1170, a predecessor of the Single UNIX Specification, and the GNU C Library (glibc) to enable unmodified binaries to run on the x86 Unix-like operating systems. The project was originally designated "Spec 150".

The format eventually chosen was ELF, specifically the Linux implementation of ELF, after it had turned out to be a *de facto* standard supported by all involved vendors and operating systems.

The group began email discussions in 1997 and first met together at the Santa Cruz Operation offices on August 22, 1997.

The steering committee was Marc Ewing, Dion Johnson, Evan Leibovitch, Bruce Perens, Andrew Roach, Bryan Wayne Sparks and Linus Torvalds. Other people on the project were Keith Bostic, Chuck Cranor, Michael Davidson, Chris G. Demetriou, Ulrich Drepper, Don Dugger, Steve Ginzburg, Jon "maddog" Hall, Ron Holt, Jordan Hubbard, Dave Jensen, Kean Johnston, Andrew Josey, Robert Lipe, Bela Lubkin, Tim Marsland, Greg Page, Ronald Joe Record, Tim Ruckle, Joel Silverstein, Chia-pi Tien, and Erik Troan. Operating systems and companies represented were BeOS, BSDI, FreeBSD, Intel, Linux, NetBSD, SCO and SunSoft.

The project progressed and in mid-1998, SCO began developing lxrun, an open-source compatibility layer able to run Linux binaries on OpenServer, UnixWare, and Solaris. SCO announced official support of lxrun at LinuxWorld in March 1999. Sun Microsystems began officially supporting lxrun for Solaris in early 1999, and later moved to integrated support of the Linux binary format via Solaris Containers for Linux Applications.

With the BSDs having long supported Linux binaries (through a compatibility layer) and the main x86 Unix vendors having added support for the format, the project decided that Linux ELF was the format chosen by the industry and "declare[d] itself dissolved" on July 25, 1999.

## FatELF: universal binaries for Linux

FatELF is an ELF binary-format extension that adds fat binary capabilities. It is aimed for Linux and other Unix-like operating systems. Additionally to the CPU architecture abstraction (byte order, word size, CPU instruction set etc.), there is the potential advantage of software-platform abstraction e.g., binaries which support multiple kernel ABI versions. As of 2021, FatELF has not been integrated into the mainline Linux kernel.
