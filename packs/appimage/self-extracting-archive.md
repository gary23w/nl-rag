---
title: "Self-extracting archive"
source: https://en.wikipedia.org/wiki/Self-extracting_archive
domain: appimage
license: CC-BY-SA-4.0
tags: appimage format, portable application, self-extracting archive, software deployment
fetched: 2026-07-02
---

# Self-extracting archive

A **self-extracting archive** (**SFX** or **SEA**) is a computer executable program which combines compressed data in an archive file with machine-executable code to extract the information. Running on a compatible operating system, it does not need a suitable extractor in the target computer to extract the data. The executable part of the file is known as a *decompressor stub*.

Self-extracting files are used to share compressed files with a party that may not have the software needed to decompress a regular archive. Users can also use self-extracting archives to distribute their own software. For example, the WinRAR installation program is made using the graphical GUI RAR self-extracting module Default.sfx.

## Overview

Self-extracting archives contain an executable file module, which is used to run uncompressed files from compressed files. The latter does not require an external program to decompress the contents of the self-extracting file and can run the operation itself. However, file archivers like WinRAR can still treat a self-extracting file as if it were any other type of compressed file. By using a file archiver, users can view or decompress self-extracting files they received without running executable code (for example, if they are concerned about viruses).

A self-extracting archive is extracted and stored on a disk when executed under an operating system that supports it. Many embedded self-extractors support a number of command-line arguments, such as specifying the target location or selecting only specific files.

Unlike self-extracting archives, non-self-extracting archives only contain archived files and must be extracted with a program that is compatible with them. While some formats of self-extracting archives cannot be extracted under another operating system, non-self-extracting ones can usually still be opened using a suitable extractor. This tool will disregard the executable part of the file and extract only the archive resource. The self-extracting executable may need to be renamed to contain a file extension associated with the corresponding packer; archive file formats known to support this include ARJ and ZIP. Typically, self-extracting files for Microsoft operating systems such as DOS and Windows have a .exe extension, just like any other executable file.

For example, an archive may be called "somefiles.zip—it", which can be opened under any operating system by a suitable archive manager that supports both the file format and compression algorithm used. It may also be converted into somefiles.exe, which will self-extract under Microsoft Windows. It will not self-extract under Linux but can be opened with a suitable archive manager. Files that are not recognized as archives by archive managers due to their executable extension can be renamed into .zip. This works for ZIP archives due to the way the ZIP header is defined, but not necessarily for other less flexible archive formats.

There are several functionally equivalent but incompatible archive file formats, such as ZIP, RAR, 7z, and others. Many programs can handle multiple types of archives, whereas others can create, extract, or modify only one type. Additionally, there is a distinction between the file format and the compression algorithm. A single file format, such as 7z, can support multiple different compression algorithms, including LZMA, LZMA2, PPMd, and BZip2. Decompression utilities must be able to handle both the file format and the algorithm used when expanding self-extracting or standard archives. Depending on the options used to create a self-extracting archive, the executable code placed at the beginning may vary. When comparing a LZMA 7z archive to a LZMA2 7z archive, for example, the decompression routines will differ.

Several programs can create self-extracting archives. Among the Windows archivers are WinZip, WinRAR, 7-Zip, WinUHA, KGB Archiver, Make SFX, the built-in IExpress wizard, and others, including experimental ones. Macintosh users can choose among StuffIt, The Unarchiver, or 7z X as their archivers. There are also programs that create self-extracting archives on Unix as shell scripts, which utilize programs like tar and gzip (which must be present in the destination system). Others (like 7-Zip or RAR) can create self-extracting archives as regular executables in ELF format. One of the early examples of self-extracting archives is the Unix shar archive, which combined a number of text files into a shell script that recreated their original content after being executed.

It is possible to archive both data and executable files with self-extracting archives. It must be distinguished from executable compression, where the executable file only contains a single executable, and running the file does not result in the uncompressed file being stored on disk but in its code being executed in memory after decompression.

## Advantages

1. Archiving files rather than sending them separately allows several related files to be combined into a single resource.
2. It reduces the size of files that aren't already efficiently compressed (most compression algorithms cannot reduce the size of already compressed files. Compression usually reduces the size of plain text documents, but rarely affects JPEGs or word processor documents, as many modern word processors already involve a certain level of compression).
3. Self-extracting archives can also be used by users without the necessary programs for extracting their contents, as long as they run a compatible operating system. A self-extracting archive may still be more convenient for users who do have archive management software.

As long as the underlying compression algorithm and format allow it, self-extracting archives can also be encrypted for security. It is important to note, however, that in many cases, the file and directory names are not included in the encryption and can be viewed by anyone without a key or password. If a person can guess part of the contents of the files from their names or context alone, an attacker may be able to break the encryption on the entire archive with a short amount of computing power and time.

## Disadvantages

1. When sent as an email attachment or downloaded from the Internet, it may be a security risk. An executable file described as a self-extracting archive may actually be a malicious program. A suggested protection against this is to open it with an archive manager instead of executing it (losing the advantage of self-extraction); the archive manager will either report the file as not an archive or will show the underlying metadata of the executable file - a strong indication that the file is not actually a self-extracting archive.
2. Some systems for distributing files do not accept executable files in order to prevent the transmission of malicious programs. These systems disallow self-extracting archive files unless they are cumbersomely renamed by the sender to, say, somefiles.exe, and later renamed back again by the recipient. This technique is gradually becoming less effective, however, as an increasing number of security suites and antivirus software packages instead scan file headers for the underlying format rather than relying on a correct file extension.
3. Self-extracting archives will only run under the operating system family and platform with which they are compatible, making it more difficult to extract their contents under other systems. Examples of self-extracting archives, which can be run on multiple targets (such as DOS and CP/M) rather than only the archive contents to be usable under multiple systems, are very rare, because they require the embedded decompressor stub to be a fat binary.
4. Since the self-extracting archives must include executable code to handle the extraction of the contained archive file, they are slightly larger in size than the original archive.
