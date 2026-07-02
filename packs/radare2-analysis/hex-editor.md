---
title: "Hex editor"
source: https://en.wikipedia.org/wiki/Hex_editor
domain: radare2-analysis
license: CC-BY-SA-4.0
tags: radare2 analysis framework, command line reverse engineering, binary debugger toolkit, hex editor inspection, disassembly workflow
fetched: 2026-07-02
---

# Hex editor

A **hex** (short for hexadecimal), **binary**, or **byte editor** is software that allows for editing data as binary data. It is particularly useful for editing non-human-readable data of a file, but can be used for any data. Generally, a hex editor is a standalone program, and its user experience is similar to that of a text editor. A user can see and edit the raw and exact contents of a file, as opposed to the interpretation of the content that other, higher level application software may associate with the file format. For example, this could be the data bytes that represent an image instead of a graphical representation.

Generally, data is grouped in 4 groups of 4 bytes or 2 groups of 8 bytes, followed by one group of 16 printable ASCII characters which correspond to each pair of hex values (each byte). Non-printable ASCII characters are typically represented by a dot (".") in the ASCII field.

A hex editor is sometimes used to fix data corruption problems. It can be useful to bypass application edit checks which may prevent correction of erroneous data. It has been used to "patch" executable programs (change or add a few instructions) as an alternative to recompilation. Program fixes for IBM mainframe systems are sometimes distributed as patches rather than distributing a complete copy of the affected program.

## Early history

Since the invention of computers and their different uses, a variety of file formats has been created. In some special circumstances it was convenient to be able to access the data as a series of raw digits. A program called SUPERZAP (AMASPZAP) was available for IBM OS/360 systems which could edit raw disk records and also understood the format of executable files. Pairs of hexadecimal digits (each pair can represent a byte) are the current standard, because the vast majority of machines and file formats in use today handle data in units or groups of 8-bit bytes. Hexadecimal and also octal are common because these digits allow one to see which bits in a byte are set. Depending on the data content, decimal or other numerical base instead of hexadecimal representation can support editing operations also using template systems and data inspectors.

## Template systems

Some hex editors offer a template system that can present the sequence of bytes of a binary file in a structured way, covering part or all of the desired file format. Usually the GUI for a template is a separate tool window next to the main hex editor. Some cheat engine systems consist only of such a template GUI.

Typically, a template is represented as a list of labeled text boxes, such that individual values of a file can be easily edited in the appropriate format (e.g., as string, color, or decimal number). Without template support, it is necessary to find the right offset in a file where the value that is to be changed is stored. Also, raw hex editing may require conversion from hexadecimal to decimal, catering for byte order, or other data type conversion peculiarities.

Templates can be stored as files, thereby exchanged by users, and are often shared publicly over the manufacturer's website. Most if not all hex editors define their own template file format; there is no trend to support a standard or even compatibility between the various formats out in the wild.

## Scripting systems

Advanced hex editors have scripting systems that let the user create macro like functionality as a sequence of user interface commands for automating common tasks. This can be used for providing scripts that automatically patch files (e.g., game cheating, modding, or product fixes provided by community) or to write more complex/intelligent templates.

Scripting languages vary widely, often being product specific languages resembling MS-DOS batch files, to systems that support fully-fledged scripting languages such as Lua or Python.

## Plugin systems

A few select editors have a plugin system that allows to extend the GUI and add new functionality, usually loading dynamic link libraries written in a C-compatible language(Different operating systems adopt distinct dynamic link library formats: DLL for Windows, SO for Linux, and Dylib for macOS.).
