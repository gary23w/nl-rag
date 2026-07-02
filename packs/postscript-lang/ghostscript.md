---
title: "Ghostscript"
source: https://en.wikipedia.org/wiki/Ghostscript
domain: postscript-lang
license: CC-BY-SA-4.0
tags: postscript language, page description language, adobe systems, encapsulated postscript, document structuring conventions
fetched: 2026-07-02
---

# Ghostscript

**Ghostscript** is a suite of software based on an interpreter for Adobe Systems' PostScript and Portable Document Format (PDF) page description languages. Its main purposes are the rasterization of documents in these languages, the display or printing of document pages, and conversion between PostScript and PDF files.

## Features

Ghostscript can be used as a raster image processor (RIP) for raster computer printers—for instance, as an input filter of line printer daemon—or as the RIP engine behind PostScript and PDF viewers. It can also be used as a file format converter, such as PostScript to PDF converter. The `ps2pdf` conversion program comes with the Ghostscript distribution.

Ghostscript can also serve as the back-end for PDF to raster image (png, tiff, jpeg, etc.) converter; this is often combined with a PostScript printer driver in "virtual printer" PDF creators. As it takes the form of a language interpreter, Ghostscript can also be used as a general purpose programming environment.

Ghostscript has been ported to many operating systems, including Unix-like systems, classic Mac OS, OpenVMS, Microsoft Windows, Plan 9, MS-DOS, FreeDOS, OS/2, ArcaOS, Atari TOS, RISC OS and AmigaOS.

## History

Ghostscript was originally written by L. Peter Deutsch for the GNU Project, and released under the GNU General Public License in 1988. At the time of the initial release there was a similar commercial software product named GoScript from LaserGo. Later, Deutsch formed *Aladdin Enterprises* to dual-license Ghostscript also under a proprietary license with an own development fork: *Aladdin Ghostscript* under the Aladdin Free Public License (which, despite the name, is not a free software license, as it forbids commercial distribution) and *GNU Ghostscript* distributed with the *GNU General Public License*. With version 8.54 in 2006, both development branches were merged again, and dual-licensed releases were still provided.

Ghostscript is currently owned by Artifex Software and maintained by Artifex Software employees and the worldwide user community. According to Artifex, as of version 9.03, the commercial version of Ghostscript can no longer be freely distributed for commercial purposes without purchasing a license, though the (A)GPL variant allows commercial distribution provided all code using it is released under the (A)GPL.

In February 2013, with version 9.07, Ghostscript changed its license from GPLv3 to GNU AGPL. which raised license compatibility questions, for example by Debian.

Starting with release 9.55.0 Ghostscript has two built-in PDF interpreters. Until spring 2022, up to Ghostscript version 9.56.1, the default PDF interpreters implementation itself was coded in PostScript. The new default PDF interpreter has been rewritten in C entirely, and is faster and more secure than its predecessor, while its interface and graphics library have not changed. Scripting the new C written PDF interpreter from PostScript is still possible.

## Free fonts

There are several sets of free fonts supplied for Ghostscript, intended to be metrically compatible with common fonts attached with the PostScript standard. These include:

- A collection of 35 font styles from ten typeface families contributed by German foundry URW++ in 1996 under the GNU General Public License (GPL) and Aladdin Free Public License (AFPL), which is commonly called the "URW Base 35 fonts" or "URW Core 35 fonts". The collection is similar to the 35 fonts defined by Adobe in PostScript Level 2: Bookman L (Bookman), Century Schoolbook L (New Century Schoolbook), Chancery L (Zapf Chancery), Dingbats (Zapf Dingbats), Gothic L (Avant Garde), Nimbus Mono L (Courier), Nimbus Roman No9 L (Times), Nimbus Sans L (Helvetica), Palladio L (Palatino), Standard Symbols L (Symbol), in Type1, TrueType, and OpenType formats.
- The GhostPDL package (including Ghostscript as well as companion implementations of HP PCL and Microsoft XPS) includes additional fonts under the AFPL which bars commercial use. It includes URW++ versions of Garamond (Garamond No. 8), Optima (URW Classico), Arial (A030), Antique Olive, and Univers (U001), Clarendon, Coronet, Letter Gothic, as well as URW Mauritius and a modified form of Albertus known as A028. Combined with the base set, they represent a little more than half of the standard PostScript 3 font complement.
- A miscellaneous set including Cyrillic, kana, and fonts derived from the free Hershey fonts, with improvements by Thomas Wolff (such as adding accented characters).

The Ghostscript fonts were developed in the PostScript Type 1 format but have been converted into the TrueType format. As a result, a user can install and use the Ghostscript fonts via most modern software. Furthermore, the Ghostscript fonts are used as parts of various open source applications, e.g., the Linux version of GIMP depends on Graphviz which in turn depends on the Ghostscript fonts. Finally, multiple open source font projects used glyphs from the Ghostscript fonts, e.g., the Latin characters of GNU FreeFont are based on Nimbus Mono L, Nimbus Roman No9 L, and Nimbus Sans L. The TeX Gyre fonts are also based on 8 out of the 10 original Ghostscript typeface families. The Garamond font has additionally been improved upon.
