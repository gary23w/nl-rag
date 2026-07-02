---
title: "PostScript fonts"
source: https://en.wikipedia.org/wiki/PostScript_fonts
domain: postscript-lang
license: CC-BY-SA-4.0
tags: postscript language, page description language, adobe systems, encapsulated postscript, document structuring conventions
fetched: 2026-07-02
---

# PostScript fonts

**PostScript fonts** are font files encoded in outline font specifications developed by Adobe for professional digital typesetting. This system uses the PostScript file format to encode font information.

*PostScript fonts* may also separately be used to refer to a basic set of fonts included as standards in the PostScript system, such as Times New Roman, Helvetica, and Avant Garde.

## History

Type 1 and Type 3 fonts, though introduced by Adobe in 1984 as part of the PostScript page description language, did not see widespread use until March 1985, when the first laser printer to use the PostScript language, the Apple LaserWriter, was introduced.

Even then, in 1985, the outline fonts were resident only in the printer, and the screen used bitmap fonts as substitutes for outline fonts.

Although originally part of PostScript, Type 1 fonts used a simplified set of drawing operations compared to ordinary PostScript (programmatic elements such as loops and variables were removed, much like PDF), but Type 1 fonts added *hints* to help low-resolution rendering. Originally, Adobe kept the details of their hinting scheme undisclosed and used a (simple) encryption scheme to protect Type 1 outlines and hints, which still persists today (although the encryption scheme and key have since been published by Adobe). Despite these measures, Adobe's scheme was quickly reverse-engineered by other players in the industry. Adobe nevertheless required anyone working with Type 1 fonts to license their technology.

Type 3 fonts allowed for all the sophistication of the PostScript language, but without the standardized approach to hinting (though some companies, such as ATF, implemented their own proprietary schemes) or an encryption scheme. Other differences further added to the confusion.

The cost of the licensing was considered very high at this time, and Adobe continued to stonewall on more attractive rates. It was this issue that led Apple to design their own system, TrueType, around 1991. Immediately following the announcement of TrueType, Adobe published ”Adobe type 1 font format”, a detailed specification for the format. Font development tools such as Fontographer added the ability to create Type 1 fonts. The Type 2 format has since been used as one basis for the modern OpenType Format.

## Technology

In the PostScript (PS) language glyphs are described with cubic Bézier curves (as opposed to the quadratic curves of TrueType), and thus a single set of glyphs can be resized through simple mathematical transformations performed in a PostScript raster image processor such as in a PostScript printer. Because the data of Type 1 is a description of the outline of a glyph and not a raster image (i.e. a bitmap), Type 1 fonts are commonly referred to as *outline* fonts as opposed to *bitmap*, or *screen*, fonts. Bitmap versions of outline fonts were used on-screen, but bitmap fonts aligned with the pixels of screens, not the higher-resolution grids of printers and imagesetters, causing differences in letter spacing, line wraps, and other copy-fitting issues. Print dialogs included an option to mitigate this discrepancy by printing at 96% size, fitting each screen pixel to an integral number of print pixels. The alternative was Adobe Type Manager, which rendered PostScript fonts on-screen, using *hinting* and, on color and greyscale screens, providing anti-aliasing, which, aside from smoothing the edges of glyphs on-screen, allowed on-screen letter spacing matching print output to not appear as irregular.

## Font type

### Type 0

Type 0 is a *composite* font format—as described in the PostScript Language Reference Manual, 2nd Edition. A composite font is composed of a high-level font that references multiple descendant fonts.

### Type 1

Type 1 (also known as ***PostScript***, ***PostScript Type 1***, ***PS1***, ***T1*** or ***Adobe Type 1***) is the font format for single-byte digital fonts for use with Adobe Type Manager software and with PostScript printers. It can support font hinting.

It was originally a proprietary specification, but Adobe released the specification to third-party font manufacturers provided that all Type 1 fonts adhere to it.

Type 1 fonts are natively supported in macOS, and in Windows 2000 and later via the GDI API. (They are not supported in the Windows GDI+, WPF or DirectWrite APIs.)

Adobe announced on 27 January 2021 that they would end support for Type 1 fonts in Adobe products after January 2023. Support for Type 1 fonts in Adobe Photoshop was discontinued with the release of version 23.0 of the product in October 2021.

### Type 2

Type 2 is a character string format that offers a compact representation of the character description procedures in an outline font file. The format is designed to be used with the Compact Font Format (CFF). The CFF/Type2 format is the basis for Type 1 OpenType fonts, and is used for embedding fonts in Acrobat 3.0 PDF files (PDF format version 1.2).

### Type 3

Type 3 font (also known as ***PostScript Type 3*** or ***PS3***, ***T3*** or ***Adobe Type 3***) consists of glyphs defined using the full PostScript language, rather than just a subset. Because of this, a Type 3 font can do some things that Type 1 fonts cannot do, such as specify shading, color, and fill patterns. However, it does not support hinting. Adobe Type Manager did not support Type 3 fonts, and they are not supported as native WYSIWYG fonts on any version of macOS or Windows.

### Type 4

Type 4 is a format that was used to make fonts for printer font cartridges and for permanent storage on a printer's hard disk. The character descriptions are expressed in the Type 1 format. Adobe does not document this proprietary format.

### Type 5

Type 5 is similar to the Type 4 format but is used for fonts stored in the ROMs of PostScript printers, also known as *compressed ROM* (*CROM*) fonts.

### Types 9, 10, 11

Ghostscript referred them as CID font types 0, 1, and 2 respectively, documented in Adobe supplements. Types 9, 10, and 11 are CID-keyed fonts for storing Types 1, 3, and 42, respectively.

### Type 14

Type 14, or the Chameleon font format, is used to represent a large number of fonts in a small amount of storage space such as printer ROM. The core set of Chameleon fonts consists of one Master Font, and a set of font descriptors that specify how the Master Font is to be adjusted to give the desired set of character shapes for a specific typeface.

Adobe does not document the Type 14 format. It was introduced with PostScript 3 in 1997, and de-emphasized in later years as storage became cheaper.

### Type 32

Type 32 is used for downloading bitmap fonts to PostScript interpreters with version number 2016 or greater. The bitmap characters are transferred directly into the interpreter's font cache, thus saving space in the printer's memory.

### Type 42

The Type 42 font format is a PostScript wrapper around a TrueType font, allowing PostScript-capable printers containing a TrueType rasterizer (which was first implemented in PostScript interpreter version 2010 as an optional feature, later standard) to print TrueType fonts. Support for multibyte CJK TrueType fonts was added in PostScript version 2015. The out-of-sequence choice of the number 42 is said to be a jesting reference to *The Hitchhiker's Guide to the Galaxy*, where 42 is the Answer to Life, the Universe, and Everything.

## Core Font Set

In addition to font types, PostScript specifications also defined the Core Font Set, which dictates the minimum number of fonts, and character sets to be supported by each font.

### PostScript Level 1

The original PostScript defined 13 font styles which form 4 type families:

- Courier (Regular, Oblique, Bold, Bold Oblique)
- Helvetica (Regular, Oblique, Bold, Bold Oblique)
- Times (Roman, Italic, Bold, Bold Italic)
- Symbol

### PostScript Level 2

PostScript Level 2 defined 35 font styles which form 10 type families. They include all of the above Level 1 fonts, *plus* the following:

- ITC Avant Garde Gothic (Book, Book Oblique, Demi, Demi Oblique)
- ITC Bookman (Light, Light Italic, Demi, Demi Italic)
- Helvetica (Narrow, Narrow Oblique, Narrow Bold, Narrow Bold Oblique, in addition to the 4 font styles in PostScript Level 1)
- New Century Schoolbook (Roman, Italic, Bold, Bold Italic)
- Palatino (Roman, Italic, Bold, Bold Italic)
- ITC Zapf Chancery (Medium Italic)
- ITC Zapf Dingbats

Many computer operating systems have these fonts installed, while various projects have created clones of them. For instance, the Ghostscript fonts (also known as the URW Base 35 fonts) are open-source clones of all fonts defined in PostScript 2.

### PostScript Level 3

In PostScript 3, 136 font styles are specified, which include the 35 font styles defined in PostScript 2, core fonts in popular operating systems (namely Windows 95, Windows NT, and Macintosh), selected fonts from Microsoft Office, and the HP 110 font set. New fonts include:

- Albertus (Light, Roman, Italic)
- Antique Olive (Roman, Italic, Bold, Compact)
- Apple Chancery
- Arial (Regular, Italic, Bold, Bold Italic)
- Bodoni (Roman, Italic, Bold, Bold Italic, Poster, Poster Compressed)
- Carta (a dingbat)
- Chicago
- Clarendon (Light, Roman, Bold)
- Cooper Black, Cooper Black Italic
- Copperplate Gothic (32BC, 33BC)
- Coronet
- Eurostile (Medium, Bold, Extended No.2, Bold Extended No.2)
- Geneva
- Gill Sans (Light, Light Italic, Book, Book Italic, Bold, Bold Italic, Extra Bold, Condensed, Condensed Bold)
- Goudy (Oldstyle, Oldstyle Italic, Bold, Bold Italic, Extra Bold)
- Helvetica (Condensed, Condensed Oblique, Condensed Bold, Condensed Bold Oblique)
- Hoefler Text (Roman, Italic, Black, Black Italic), Hoefler Ornaments
- Joanna (Roman/Regular, Italic, Bold, Bold Italic)
- Letter Gothic (Regular, Slanted, Bold, Bold Slanted)
- ITC Lubalin Graph (Book, Oblique, Demi, Demi Oblique)
- ITC Mona Lisa Recut
- Marigold
- Monaco
- New York
- Optima (Roman, Italic, Bold, Bold Italic)
- Oxford
- Stempel Garamond (Roman, Italic, Bold, Bold Italic)
- Tekton (Regular)
- Times New Roman (Regular, Italic, Bold, Bold Italic)
- Univers (45 Light, 45 Light Oblique, 55, 55 Oblique, 65 Bold, 65 Bold Oblique, 57 Condensed, 57 Condensed Oblique, 67 Condensed Bold, 67 Condensed Bold Oblique, 53 Extended, 53 Extended Oblique, 63 Extended Bold, 63 Extended Bold Oblique)
- Wingdings

### Others

In PDF, 14 Type 1 fonts are defined as the standard fonts. They include the 13 font styles defined by PostScript Level 1, along with ITC Zapf Dingbats.

However, in recent versions of Adobe Acrobat Reader, Helvetica and Times were internally replaced by Arial and Times New Roman respectively.

## Character sets

Although PostScript fonts can contain any character set, there are character sets specifically developed by Adobe, which are used by fonts developed by Adobe.

### Adobe Western 2

It includes a basic character set containing upper and lowercase letters, figures, accented characters, and punctuation. These fonts also contain currency symbols (cent, dollar, euro, florin, pound sterling, yen), standard ligatures (fi, fl), common fractions (1/4, 1/2, 3/4), common mathematics operators, superscript numerals (1,2,3), common delimiters and conjoiners, and other symbols (including daggers, trademark, registered trademark, copyright, paragraph, litre and estimated symbol). Compared to the ISO-Adobe character set, Western 2 also adds 17 additional symbol characters: euro, litre, estimated, omega, pi, partialdiff, delta, product, summation, radical, infinity, integral, approxequal, notequal, lessequal, greaterequal, and lozenge.

Fonts with an Adobe Western 2 character set support most western languages including Afrikaans, Basque, Breton, Catalan, Danish, Dutch, English, Finnish, French, Gaelic, German, Icelandic, Indonesian, Irish, Italian, Norwegian, Portuguese, Sami, Spanish, Swahili and Swedish.

This standard superseded ISO-Adobe as the new minimum character set standard as implemented in OpenType fonts from Adobe.

### Adobe CE

Fonts with an Adobe CE character set also include the characters necessary to support the following central European languages: Croatian, Czech, Estonian, Hungarian, Latvian, Lithuanian, Polish, Romanian, Serbian (Latin), Slovak, Slovenian and Turkish.

### Adobe-GB1

This Simplified Chinese character collection provides support for the GB 1988–89, GB 2312–80, GB/T 12345–90, GB 13000.1-93, and GB 18030-2005 character set standards. Supported encodings include ISO-2022, EUC-CN, GBK, UCS-2, UTF-8, UTF-16, UTF-32, and the mixed one, two- and four-byte encoding as published in GB 18030-2005.

### Adobe-CNS1

This Traditional Chinese character collection provides support for the Big-5 and CNS 11643-1992 character set standards. It also includes support for a number of extensions to Big-5, which contain characters used mainly in the Hong Kong locale. Primary supported Big-5 extensions include HKSCS.

Supported encodings include ISO-2022, EUC-TW, Big Five, UCS-2, UTF-8, UTF-16, and UTF-32.

In Adobe-CNS1-7, 23 additional glyphs were added, with 25 additional mappings for its Unicode CMap resources.

### Adobe-Japan1

It is a series of character sets developed for Japanese fonts. Adobe's latest, the Adobe-Japan1-6 set covers character sets from JIS X 0208, ISO-2022-JP, Microsoft Windows 3.1 J, JIS X 0213:2004, JIS X 0212-1990, Kyodo News U-PRESS character set.

### Adobe-Japan2

It was originally as an implementation of JIS X 0212-1990 character set standard and the Macintosh extensions, but with the introduction of Adobe-Japan1 supplement 6 (Adobe-Japan1-6) standard, Adobe-Japan2-0 became obsolete.

### Adobe-Korea1

This Korean character collection provides support for the KS X 1001:1992 and KS X 1003:1992 character set standards, and their selected corporate variations. Supported encodings include ISO-2022-KR, EUC-KR, Johab, UHC, UCS-2, UTF-8, UTF-16, and UTF-32.

### ISO-Adobe

Fonts with an ISO-Adobe character set support most western languages including: Afrikaans, Basque, Breton, Catalan, Danish, Dutch, English, Finnish, French, Gaelic, German, Icelandic, Indonesian, Irish, Italian, Norwegian, Portuguese, Sami, Spanish, Swahili and Swedish. This is the standard character set in most PostScript Type 1 fonts from Adobe.

## File formats

### CID

The **CID-keyed font** (also known as ***CID font***, ***CID-based font***, short for ***Character Identifier font***) is a font structure, originally developed for PostScript font formats, designed to address a large number of glyphs. It was developed to support pictographic East Asian character sets, as these comprise many more characters than the Latin, Greek and Cyrillic writing systems.

Adobe developed CID-keyed font formats to solve problems with the OCF/Type 0 format, for addressing complex Asian-language (CJK) encoding and very large character sets. CID-keyed internals can be used with the Type 1 font format for standard CID-keyed fonts, or Type 2 for CID-keyed OpenType fonts. CID-keyed fonts often reference "character collections," static glyph sets defined for different language coverage purposes. Although in principle any font maker may define character collections, Adobe's are the only ones in wide usage. Each character collection has an encoding which maps Character IDs to glyphs. Each member glyph in a character collection is identified by a unique character identifier (CID). Such CIDs are generally supplemental to other encodings or mappings such as Unicode.

Character collections are uniquely named by registry, ordering and supplement, such as "Adobe-Japan1-6." The registry is the developer (such as Adobe). The so-called "ordering" gives the purpose of the collection (for example, "Japan1"). The supplement number (such as 6) indicates incremental additions: for a given language, there may be multiple character collections of increasing size, each a superset of the last, using a higher supplement number. The Adobe-Japan1-0 collection is 8284 glyphs, while Adobe-Japan1-6 is 23,058 glyphs.

CID-keyed fonts may be made without reference to a character collection by using an "identity" encoding, such as Identity-H (for horizontal writing) or Identity-V (for vertical). Such fonts may each have a unique character set, and in such cases the CID number of a glyph is not informative; generally the Unicode encoding is used instead, potentially with supplemental information.

CID-keyed fonts internally have their character sets divided into "rows," with the advantage that each row may have different global hinting parameters applied.

In theory it would be possible to make CID-keyed OpenType versions of western fonts. This would seem desirable for some such fonts because of the hinting advantages. However, according to Adobe, much of the software infrastructure (applications, drivers, operating systems) makes incorrect assumptions about CID-keyed fonts in ways that makes such fonts behave badly in real-world usage.

Adobe **ClearScan** technology (as from Acrobat 9 Pro) creates custom **Type1-CID** fonts to match the visual appearance of a scanned document after optical character recognition (OCR). ClearScan does not replace the fonts with system fonts or substitute them by Type1-MM (as in Acrobat 8 and earlier versions), but uses these newly created custom fonts. The custom fonts are embedded in the PDF file (this is mandatory). In Acrobat DC, it is no longer called "ClearScan" but instead "Recognize Text - Editable Text & Images", and it is now possible to edit the text.

### Compact Font Format

**Compact Font Format** (CFF, also known as Type 2 or CFF/Type 2 font format) is a lossless compaction of the Type 1 format using Type 2 charstrings. It is designed to use less storage space than Type 1 fonts, by using operators with multiple arguments, various predefined default values, more efficient allotment of encoding values and shared subroutines within a FontSet (family of fonts).

The so-called PostScript or Type 1 flavor of OpenType fonts, also called OpenType CFF, contains glyph outlines and hints in a CFF table.

CFF fonts can be embedded in PDF files, starting with PDF version 1.2. It is the usual approach to representing a Type 1 font within PDF.

CID-keyed fonts can be represented within CFF with Type 2 charstrings for CID-keyed OpenType fonts.

A Type 1 font can be losslessly converted into CFF/Type2 format and back.

### Multiple Master

**Multiple master fonts** (or **MM fonts**) are an extension to Adobe Systems' Type 1 PostScript fonts. Multiple master fonts contain one or more *masters*—that is, original font styles, e.g. a light, a regular and a bold version—and enable a user to interpolate these font styles along a continuous range of *axes*. While Multiple Master fonts are not common in end user fonts anymore, they still play an important role when developing complex font families.

### OpenType

PostScript glyph data can be embedded in OpenType font files, but OpenType fonts are not limited to using PostScript outlines. PostScript outlines in OpenType fonts are encoded in the Type2 Compact Font Format (CFF).

#### OpenType conversion

When Adobe converted PostScript Type 1 and Type 1 multiple master fonts to OpenType CFF format, they were made based on the last Type 1/MM versions from the Adobe Type Library fonts. In addition to file format change, there are other changes:

- All alphabetic fonts had 17 additional characters included: the euro (some had already gotten this in Type 1), litre, estimated, and the 14 Mac "symbol substitution" characters. Symbol substitution was a scheme used on macOS to deal with the fact that the standard "ISO-Adobe" character set omitted certain characters which were part of the MacRoman character set. When one of these 14 characters was typed in a Type 1 font with standard encoding, both ATM and the printer driver would get a generic glyph in the Times style from the Symbol font. In the OpenType conversion, these characters were built into every font, getting some degree of font-specific treatment (weight and width).
- Fonts that had unkerned accented characters had additional kerning to deal with accented characters.
- Font families that included separate Type 1 expert fonts or Cyrillic fonts have these glyphs built into the "base font" in their OpenType counterparts.
- Multiple master fonts were converted to individual OpenType fonts; each font consisting of a former Multiple Master instance.

For many Adobe Originals fonts, particularly those designed by Robert Slimbach, Adobe did some degree of redesign along with the conversion to OpenType.

The typeface Helvetica Narrow was not converted to OpenType, because the Type 1 original was a mathematically squished version of Helvetica, rather than an actually designed condensed typeface. This was originally done to conserve ROM space in PostScript printers.

As a result of the above changes, Adobe no longer guarantees metric compatibility between Type 1 and OpenType fonts. However, Adobe claims the change is minimal for Adobe (not Adobe Originals) fonts, if:

- Text is written in English
- The formatted text contains only non-accented characters
- Only characters that were present in the old fonts are used, without the former Symbol substitution characters
- Applications are used which base line spacing solely on point size or leading, and not on the bounding box of the font

### Original Composite Font

**Original Composite Font** format (which uses a Type 0 file structure) was Adobe's first effort to implement a format for fonts with large character sets, debuted with PostScript level 2.

Adobe then developed the CID-keyed font file format which was designed to offer better performance and a more flexible architecture for addressing the complex Asian-language encoding and character set issues. Adobe does not document or support OCF font format.

OCF font metrics are described in Adobe Composite Font Metrics file.

### Adobe Font Metrics, Adobe Composite Font Metrics, Adobe Multiple Font Metrics

**Adobe Font Metrics** (AFM), **Adobe Composite Font Metrics** (ACFM), **Adobe Multiple Font Metrics** (AMFM) files contain general font information and font metrics information for the font program. These files are generally used directly only in Unix environments.

An AFM file provides both global metrics for a font program and the metrics of each individual character.

The metrics of a multiple master font are described by one AMFM file, which specifies the control data and global font information, plus one AFM file for each of the master designs in the font.

An ACFM file provides information about the structure of a composite font. Specifically, the global metrics of the composite font program and the global metrics of each of its immediately descendent font programs. ACFM file does not associate with a base font, but act as the top-level structure of a composite font. The character metrics of individual characters in the composite font are described completely by one of more associated AFM files.

The formats are sufficiently similar that a compliant parser can parse AFM, ACFM, and AMFM files.

### Printer Font ASCII

**Printer Font ASCII** (PFA) is a pure ASCII version of a Type 1 font program, containing in particular a font's glyph data. It is pure PostScript code without any sort of wrapper, and can be copied in full into a PS file to define the font to the PS interpreter. PFA is the preferred format for Type 1 fonts used in UNIX environments, and usually carries a ".PFA" file name extension.

Though these files syntactically can contain arbitrary PostScript code, they usually follow a rather rigid formula in order to allow readers that are less than full PostScript interpreters to process them (for example to subset the font). The first section of the file is called the clear text portion, and begins constructing those data structures that define the font in the PostScript interpreter; the information here are things Adobe in the 1980s were comfortable having public, and much of it would be present also in the companion AFM file. The last two operators in the clear text portion are `currentfile eexec` (encrypted exec), which instructs the interpreter to switch to reading the current file as an encrypted stream of instructions. The following encrypted portion is again PostScript code for finishing constructing the font data structures—a lot of it consists of charstrings, which is rather a kind of bytecode, but at the font definition stage those are merely data stored in the font—even if that code is encrypted (which produces arbitrary byte values) and then hex-encoded to ensure the overall ASCII nature of the file. The data structures created here are marked `noaccess` to make them inaccessible for subsequent PostScript code. The final action in the encrypted portion is to switch back to reading the file normally, but since eexec would read ahead a bit it was impossible to know at exactly which character normal processing would resume. Therefore, PFA files end with a trailer of 512 zeroes followed by a `cleartomark` operator that throws away any operands that might have ended up on the stack as a result of interpreting those zeroes starting from a random position.

### Printer Font Binary

**Printer Font Binary** (PFB) is a binary PostScript font format created by Adobe Systems, usually carrying ".PFB" file name extension. It contains a font's glyph data.

The PFB format is a lightweight wrapper to allow more compact storage of the data in a PFA file. The file consists of a number of blocks, each of which is marked as ASCII or binary. To recreate the corresponding PFA file, one takes the ASCII blocks verbatim and hex-encodes the binary blocks. The binary blocks are those which make up the encrypted portion of the font program.

### LaserWriter Font

**LaserWriter Font** (LWFN) is a binary PostScript font format used on Classic Mac OS, conceptually similar to the Printer Font Binary format but using the macOS resource fork data structure rather than a custom wrapper for the font data. It contains the glyph data for one font.

`LWFN` is the file type code for this kind of file. It would not carry any extension, and the file name would be an abbreviation of the PostScript name of the font, according to a 5+3+3+... formula: the name is read as being in CamelCase and split into subwords, up to 5 letters are kept from the first subword, and up to 3 letters of any subsequent subword. Palatino-BoldItalic would thus be found in the file PalatBolIta.

### Printer Font Metric

**Printer Font Metric** (PFM) is a binary version of AFM, usually carrying ".PFM" file name extension. It contains font metric information.

The PFM format is documented in the Windows 3.1 "*Printers and Fonts Kit*" help file (PFK31WH.HLP). Some details are also covered in the Windows 3.1 "*Device Drivers Adaptation Guide*" help file (DDAG31WH.HLP). Both of those documents are part of the Windows 3.1 Device Development Kit (DDK), which is still available (October 2008) to MSDN subscribers.

### .INF

**.inf** (INFormation) files contain application-specific information in plain ASCII text, such as font menu names for Windows and DOS-based applications. When a font is installed in Windows, the ATM Installer software takes the AFM and the INF file as input and generates the required PFM file at installation time. The AFM and INF files are not installed in the user's system.

### .MMM

**.MMM** files are used for the metric data needed by multiple master fonts for the Windows environment.

### .OFM

**.OFM** is the extension used by OS/2 for its version of binary font metrics file, starting from version 2.1.

## Support for Microsoft Windows

Windows 95, Windows 98, Windows NT 4 and Windows Me do not support Type 1 fonts natively. Adobe Type Manager is needed in order to use these fonts on these operating systems. Windows 2000, Windows XP and Windows Vista support Type 1 fonts natively through GDI calls. The Windows Presentation Foundation introduced in Windows Vista, which is also available for Windows XP however drops support for Type 1 fonts, in favor of Type 2 fonts.

For Microsoft Windows platforms that natively support PostScript, only binary PostScript and OpenType file formats are supported.

Windows Presentation Foundation (formerly codenamed Avalon) in Windows Vista supports rasterizing OpenType CFF/Type 2 fonts, whereas Type 1 fonts will still be supported in GDI, but not in GDI+.

## PostScript font utilities

The t1utils font utility package by I. Lee Hetherington and Eddie Kohler provides tools for decoding Type 1 fonts into a human-readable, and editable format (t1disasm), reassembling them back into fonts (t1asm), for converting between the ASCII and binary formats (t1ascii and t1binary), and for converting from Macintosh PostScript format to Adobe PostScript font format (unpost).
