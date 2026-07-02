---
title: "Binary file"
source: https://en.wikipedia.org/wiki/Binary_file
domain: binary-analysis
license: CC-BY-SA-4.0
tags: static binary analysis, executable format inspection, control flow graph recovery, symbol table analysis, machine code inspection
fetched: 2026-07-02
---

# Binary file

A **binary file** is a computer file that is not a text file. The term "binary file" is often used as a term meaning "non-text file". Many binary file formats contain parts that can be interpreted as text; for example, some computer document files containing formatted text, such as older Microsoft Word document files, contain the text of the document but also contain formatting information in binary form.

## Background and terminology

All modern computers store information in the form of bits (binary digits), using binary code. For this reason, all data stored on a computer is, in some sense, "binary". However, one particularly useful and ubiquitous type of data stored on a computer is one in which the bits represent text, by way of a character encoding. Those files are called "text files" and files which are not like that are referred to as "binary files", as a sort of retronym or hypernym.

Some "text files" contain portions that are actually binary data, and many "binary files" contain portions that are encoded text; for instance, textual data may be stored as a field within the binary format, or arbitrary constants may have been chosen to correspond to ASCII letters as a mnemonic (this is common for file magic numbers). These mixed binary-and-text file are usually regarded as "binary", because an application that can only process text will not know what to do with them.

It is quite common for a text file to use its text to encode data that could be encoded in binary some other way; a text file that does this is still regarded as a text file, and not a binary file, so long as it remains within the previously-stated constraints about what the bits of the file represent. For example, in a binary file, the number 250 could be encoded in bits as the sequence 11111010. It could also be encoded in a text file (for example, a programming language source file) as the digits 2, 5, 0; which would in turn be encoded by the bits in the text file as (for example, using UTF-8) 00110010, 00110101, 00110000.

## Structure

Binary files are usually thought of as being a sequence of bytes, which means the binary digits (bits) are grouped in eights. Binary files typically contain bytes that are intended to be interpreted as something other than text characters. Compiled computer programs are typical examples; indeed, compiled applications are sometimes referred to, particularly by programmers, as **binaries**. But binary files can also mean that they contain images, sounds, compressed versions of other files, etc. – in short, any type of file content whatsoever.

Some binary files contain headers, blocks of metadata used by a computer program to interpret the data in the file. The header often contains a signature or *magic* number which can identify the format. For example, a GIF file can contain multiple images, and headers are used to identify and describe each block of image data. The leading bytes of the header would contain text like `GIF87a` or `GIF89a` that can identify the binary as a GIF file. If a binary file does not contain any headers, it may be called a **flat binary file**.

A text file may consist partly or entirely of encoded binary information. When sending binary files over the network they may be encoded so that they use only printable characters. This is often necessary due to the limitations of network protocols used for internet browsing and e-mail communication. One such encoding is Base64. Also, files containing public-key and private-key information for use in systems employing asymmetric cryptography (such as website certificates) may also be stored with the binary information encoded in printable characters.

## Manipulation

To send binary files through certain systems (such as email) that do not allow all data values, they are often translated into a plain text representation (using, for example, Base64). Encoding the data has the disadvantage of increasing the file size during the transfer (for example, using Base64 will increase the file's size by approximately 30%), as well as requiring translation back into binary after receipt. The increased size may be countered by lower-level link compression, as the resulting text data will have about as much less entropy as it has increased size, so the actual data transferred in this scenario would likely be very close to the size of the original binary data. See Binary-to-text encoding for more on this subject.

Microsoft Windows and its standard libraries for the C and C++ programming languages allow the programmer to specify a parameter indicating if a file is expected to be plain text or binary when opening a file; this affects the standard library calls to read and write from the file in that the system converts between the C/C++ "end of line" character (the ASCII linefeed character) and the end-of-line sequence Windows expects in files (the ASCII carriage return and linefeed characters in sequence). In Unix-like systems, the C and C++ standard libraries on those systems also allow the programmer to specify whether a file is expected to be text or binary, but the libraries can and do ignore that parameter, as the end-of-line sequence in Unix-like systems is just the C/C++ end-of-line character.

## Viewing

A hex editor or viewer may be used to view file data as a sequence of hexadecimal (or decimal, binary or ASCII character) values for corresponding bytes of a binary file.

If a binary file is opened in a text editor, each group of eight bits will typically be translated as a single character, and the user will see a (probably unintelligible) display of textual characters. If the file is opened in some other application, that application will have its own use for each byte: maybe the application will treat each byte as a number and output a stream of numbers between 0 and 255—or maybe interpret the numbers in the bytes as colors and display the corresponding picture. Other type of viewers (called 'word extractors') simply replace the unprintable characters with spaces revealing only the human-readable text. This type of view is useful for a quick inspection of a binary file in order to find passwords in games, find hidden text in non-text files and recover corrupted documents. It can even be used to inspect suspicious files (software) for unwanted effects. For example, the user would see any URL/email to which the suspected software may attempt to connect in order to upload unapproved data (to steal). If the file is itself treated as an executable and run, then the operating system will attempt to interpret the file as a series of instructions in its machine language.

## Interpretation

Standards are very important to binary files. For example, a binary file interpreted by the ASCII character set will result in text being displayed. A custom application can interpret the file differently: a byte may be a sound, or a pixel, or even an entire word. Binary itself is meaningless, until such time as an executed algorithm defines what should be done with each bit, byte, word or block. Thus, just examining the binary and attempting to match it against known formats can lead to the wrong conclusion as to what it actually represents. This fact can be used in steganography, where an algorithm interprets a binary data file differently to reveal hidden content. Without the algorithm, it is impossible to tell that hidden content exists.

## Binary compatibility

Two files that are binary compatible will have the same sequence of zeros and ones in the data portion of the file. The file header, however, may be different.

The term is used most commonly to state that data files produced by one application are exactly the same as data files produced by another application. For example, some software companies produce applications for Windows and the Macintosh that are binary compatible, which means that a file produced in a Windows environment is interchangeable with a file produced on a Macintosh. This avoids many of the conversion problems caused by importing and exporting data.

One possible binary compatibility issue between different computers is the endianness of the computer. Some computers store the bytes in a file in a different order.
