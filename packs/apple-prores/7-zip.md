---
title: "7-Zip"
source: https://en.wikipedia.org/wiki/7-Zip
domain: apple-prores
license: CC-BY-SA-4.0
tags: apple prores
fetched: 2026-07-03
---

# 7-Zip

**7-Zip** is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as "archives". It is developed by Igor Pavlov and was first released in 1999. 7-Zip has its own archive format called 7z introduced in 2001, but can read and write several others.

The program can be used from a Windows graphical user interface that also features shell integration, or from a command-line interface as the command `7z` that offers cross-platform support (see versions for details). An obsolete port of 7-Zip to POSIX systems was called `p7zip`. Most of the 7-Zip source code is under the LGPL-2.1-or-later license; the unRAR code, however, is under the LGPL-2.1-or-later license with an "unRAR restriction", which states that developers are not permitted to use the code to reverse-engineer the RAR compression algorithm.

Since version 21.01 alpha, native Linux support has been added.

## Archive formats

### 7z

By default, 7-Zip creates 7z-format archives with a `.7z` file extension. Each archive can contain multiple directories and files. As a *container* format, security or size reduction are achieved by looking for similarities throughout the data using a stacked combination of filters. These can consist of pre-processors, compression algorithms, and encryption filters.

The core 7z compression uses a variety of algorithms, the most common of which are bzip2, PPMd, LZMA2, and LZMA. Developed by Pavlov, LZMA is a relatively new system, making its debut as part of the 7z format. LZMA uses an LZ-based sliding dictionary of up to 3840 MB in size, backed by a range coder.

The native 7z file format is open and modular. File names are stored as Unicode.

The 7z file format specification is distributed with the program's source code, in the "doc" sub-directory.

### Others

7-Zip supports a number of other compression and non-compression archive formats (both for packing and unpacking), including ZIP, gzip, bzip2, xz, tar, and WIM. The utility also supports unpacking APM, ar, ARJ, chm, cpio, deb, FLV, JAR, LHA/LZH, LZMA, MSLZ, Office Open XML, onepkg, RAR, RPM, SMZIP, SWF, XAR, and Z archives and cramfs, DMG, FAT, HFS, ISO, MBR, NTFS, SquashFS, UDF, and VHD disk images. 7-Zip supports the ZIPX format for unpacking only. It has had this support since at least version 9.20, which was released in late 2010. 7-Zip added support for RAR5 in 2015.

7-Zip can open some MSI files, allowing access to the meta-files within along with the main contents. Some Microsoft CAB (LZX compression) and NSIS (LZMA) installer formats can be opened. Similarly, some Microsoft executable programs (.EXEs) that are self-extracting archives or otherwise contain archived content (e.g., some setup files) may be opened as archives.

When compressing ZIP or gzip files, 7-Zip uses its own DEFLATE encoder, which may achieve higher compression, but at lower speed, than the more common zlib DEFLATE implementation. The 7-Zip deflate encoder implementation is available separately as part of the AdvanceCOMP suite of tools.

The decompression engine for RAR archives was developed using freely available source code of the unRAR program, which has a licensing restriction against creation of a RAR compressor. 7-Zip v15.06 and later support extraction of files in the RAR5 format. Some backup systems use formats supported by archiving programs such as 7-Zip; e.g., some Android backups are in `tar` format, and can be extracted by archivers such as 7-Zip.

## Features

- Basic orthodox file manager when used in dual panel mode
- Encryption via the 256-bit AES cipher, which can be enabled for both files and the 7z hierarchy. When the hierarchy is encrypted, users are required to supply a password to see the filenames contained within the archive. WinZip-developed Zip file AES encryption standard is also available in 7-Zip to encrypt ZIP archives with AES 256-bit, but it does not offer filename encryption as in 7z archives.
- Volumes of dynamically variable sizes, allowing use for backups on removable media such as writable CDs and DVDs
- Multi-threaded compression
- Opening EXE files as archives, allowing the decompression of data from inside many "Setup" or "Installer" or "Extract" type programs without having to launch them
- Unpacking archives with corrupted filenames, renaming the files as required.
- Creation of self-extracting archives
- Command-line and graphical user interfaces. Only the Windows version of the application comes with its own GUI. For Unix-like systems, several GUIs, e.g. PeaZip, can handle the 7z file format based on the Unix binaries.
- Calculating Blake2SP, CRC-32, CRC-64, MD5, SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, and XXH64 checksums for disk files, available either via command line or Explorer's context menu
- Ability to optionally record creation dates (`tc`) and last access dates (`ta`) in archives (in addition to modification dates).

### File manager

7-Zip comes with a file manager along with the standard archiver tools. The file manager has a toolbar with options to create an archive, extract an archive, test an archive to detect errors, copy, move, and delete files, and open a file properties menu exclusive to 7-Zip. The file manager, by default, displays hidden files because it does not follow Windows Explorer's policies. The tabs show name, modification time, original and compressed sizes, attributes, and comments (4DOS `descript.ion` format).

When going up one directory on the root, all drives, removable or internal appear. Going up again shows a list with four options:

- **Computer**: loads the drives list
- **Documents**: loads user's documents, usually at `%UserProfile%\My Documents`
- **Network**: loads a list of all network clients connected
- **\\.**: Same as "Computer" except loads the drives in low-level filesystem access. This results in critical drive files and deleted files still existing on the drive to appear. (NOTE: As of November 2020, access to the active partition in low-level mode is not allowed for currently unknown reasons.)

## Versions

In the past three command-line versions were available: 7z (`7z.exe`), using external libraries to support a large number of different formats and the ability to support even more formats via plug-ins; 7za (`7za.exe`), which is a standalone executable containing built-in modules, but with compression/decompression support limited to 7z, ZIP, gzip, bzip2, Z and tar formats; and 7zr (`7zr.exe`), which is a *minimized* standalone executable with compression/decompression support limited to just the 7z format. A 64-bit version is available, with support for large memory maps, leading to faster compression. All versions support multi-threading.

As of 2026, the application comes only with the `7z.exe` command line binary.

### Forks

- **p7zip** is a deprecated port of 7-Zip to Unix-like operating systems (including Linux, FreeBSD, and macOS), FreeDOS, OpenVMS, AmigaOS 4, and MorphOS. Since support for Unix-like operating systems has officially been added to upstream 7-Zip in version 21.01, the *p7zip* fork has become obsolete and is no longer updated; the last available version of *p7zip* is 16.02. It has known vulnerabilities including CVE-2016-9296 and CVE-2022-47069.
- **7-zip ZS** is a fork with Zstandard, Brotli, Lz4, Lz5 and Lizard compression algorithms support.
  - **p7zip-zstd** (p7zip with zstd) is p7zip with ZS additions.
- **NanaZip** is a fork integrating changes from many sources, modernized for the Microsoft Store.

### Plugins

7-zip comes with a plug-in system for expansion. The official "Links" page points to many plugins written by TC4Shell, providing extra file support.

## Software development kit

7-Zip has a LZMA SDK which was originally dual-licensed under both the GNU LGPL and Common Public License, with an additional special exception for linked binaries. On 2 December 2008, the SDK was placed by Igor Pavlov in the public domain.

## Security

Self-extracting archives created by versions of 7-Zip prior to 16.03 were vulnerable to arbitrary code execution through DLL hijacking: they load and run a DLL named UXTheme.dll, if it is in the same folder as the executable file. 7-Zip 16.03 release notes mention that the installer and SFX modules add protection against the DLL preloading attack.

Versions prior to 18.05 contain an arbitrary code execution vulnerability in the RAR extracting module, CVE-2018-10115. It was fixed on April 30, 2018.

Versions prior to 23.0 contain an arbitrary code execution vulnerability, CVE-2023-31102. It was fixed on May 7, 2023.

Versions prior to 24.07 are affected by a remote code execution vulnerability, CVE-2024-11477. It was fixed on November 20, 2024.

Versions prior to 26.01 contain an arbitrary code execution vulnerability, CVE-2026-48095. It was fixed on April 27, 2026.

Versions prior to 26.02 are affected by CVE-2026-58052.

## Reception and usage

Snapfiles.com in 2012 rated 7-Zip 4.5 stars out of 5, noting, "[its] interface and additional features are fairly basic, but the compression ratio is outstanding".

TechRepublic in 2009 found the detailed settings for Windows File Manager integration were "appreciated" and called the compression-decompression benchmark utility "neat". And though the archive dialog has settings that "will confound most users", he concluded: "7-Zip fits a nice niche in between the built-in Windows capabilities and the features of the paid products, and it is able to handle a large variety of file formats in the process."

In 2011, TopTenReviews found that the 7z compression was at least 17% better than ZIP, and 7-Zip's own site has since 2002 reported that while compression ratio results are very dependent upon the data used for the tests, "Usually, 7-Zip compresses to 7z format 30–70% better than to zip format, and 7-Zip compresses to zip format 2–10% better than most other zip-compatible programs."

Between 2002 and 2024, 7-Zip was downloaded 428 million times from SourceForge alone.

### Awards

In 2007, SourceForge granted it community choice awards for "Technical Design" and for "Best Project". In 2013, Tom's Hardware conducted a compression speed test comparing 7-Zip, MagicRAR, WinRAR, WinZip; they concluded that 7-Zip beat out all the others with regards to compression speed, ratio, and size and awarded the software the 2013 Tom's Hardware Elite award.
