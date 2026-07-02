---
title: "Office Open XML"
source: https://en.wikipedia.org/wiki/Office_Open_XML
domain: openpyxl-excel
license: CC-BY-SA-4.0
tags: python openpyxl, openpyxl excel, xlsx spreadsheet python
fetched: 2026-07-02
---

# Office Open XML

**Office Open XML** (also informally known as **OOXML**) is a zipped, XML-based file format developed by Microsoft for representing spreadsheets, charts, presentations and word processing documents. Ecma International standardized the initial version as ECMA-376. ISO and IEC standardized later versions as ISO/IEC 29500.

Microsoft Office 2010 provides read support for ECMA-376, full support for ISO/IEC 29500 Transitional, and read support for ISO/IEC 29500 Strict. Microsoft Office 2013 and later fully support ISO/IEC 29500 Strict, but do not use it as the default file format because of backwards compatibility concerns.

## Background

In 2000, Microsoft released an initial version of an XML-based format for Microsoft Excel, which was incorporated in Office XP. In 2002, a new file format for Microsoft Word followed. The Excel and Word formats—known as the Microsoft Office XML formats—were later incorporated into the 2003 release of Microsoft Office.

Microsoft announced in November 2005 that it would co-sponsor standardization of the new version of their XML-based formats through Ecma International as "Office Open XML". The presentation was made to Ecma by Microsoft's Jean Paoli and Isabelle Valet-Harper.

## Standardization process

Microsoft submitted initial material to Ecma International Technical Committee TC45, where it was standardized to become ECMA-376, approved in December 2006.

This standard was then fast-tracked in the Joint Technical Committee 1 of ISO and IEC. After initially failing to pass, an amended version of the format received the necessary votes for approval as an ISO/IEC Standard as the result of a JTC 1 fast-tracking standardization process that concluded in April 2008. The resulting four-part International Standard (designated ISO/IEC 29500:2008) was published in November 2008 and can be downloaded from the ITTF. A technically equivalent set of texts is published by Ecma as *ECMA-376 Office Open XML File Formats—2nd edition* (December 2008); they can be downloaded from their website.

The ISO/IEC standardization of Office Open XML was controversial and embittered, with much discussion both about the specification and about the standardization process. According to *InfoWorld*, "OOXML was opposed by many on grounds it was unneeded, as software makers could use OpenDocument Format (ODF), a less complicated office software format that was already an international standard." The same *InfoWorld* article reported that IBM (which supports the ODF format) threatened to leave standards bodies that it said allow dominant corporations like Microsoft to wield undue influence. The article further says that Microsoft was accused of co-opting the standardization process by leaning on countries to ensure that it got enough votes at the ISO/IEC for Office Open XML to pass, although it does not specify exactly who accused Microsoft.

## Licensing

Under the Ecma International code of conduct in patent matters, participating and approving member organizations of ECMA are required to make their patent rights available on a reasonable and non-discriminatory (RAND) basis.

Holders of patents which concern ISO/IEC International Standards may agree to a standardized license governing the terms under which such patents may be licensed, in accord with the ISO/IEC/ITU common patent policy.

Microsoft, the main contributor to the standard, provided a covenant not to sue for its patent licensing. The covenant received a mixed reception, with some like the Groklaw blog criticizing it, and others such as Lawrence Rosen, (an attorney and lecturer at Stanford Law School), endorsing it.

Microsoft has added the format to their *Open Specification Promise* in which

> Microsoft irrevocably promises not to assert any Microsoft Necessary Claims against you for making, using, selling, offering for sale, importing or distributing any implementation to the extent it conforms to a Covered Specification [...]

This is limited to applications which do not deviate from the ISO/IEC 29500:2008 or Ecma-376 standard and to parties that do not "file, maintain or voluntarily participate in a patent infringement lawsuit against a Microsoft implementation of such Covered Specification". The Open Specification Promise was included in documents submitted to ISO/IEC in support of the ECMA-376 fast-track submission. Ecma International asserted that, "The OSP enables both open source and commercial software to implement [the specification]".

## Versions

The Office Open XML specification exists in several versions.

### ECMA-376 1st edition (2006)

The ECMA standard is structured in five parts to meet the needs of different audiences.

**Part 1. Fundamentals**

- Vocabulary, notational conventions and abbreviations
- Summary of primary and supporting markup languages
- Conformance conditions and interoperability guidelines
- Constraints within the Open Packaging Conventions that apply to each document type

**Part 2. Open Packaging Conventions**

- The Open Packaging Conventions (OPC), for the package model and physical package, is defined and used by various document types in various applications from multiple vendors.
- It defines core properties, thumbnails, digital signatures, and authorizations & encryption capabilities for parts or all of the contents in the package.
- XML schemas for the OPC are declared as XML Schema Definitions (XSD) and (non-normatively) using RELAX NG (ISO/IEC 19757-2)

**Part 3. Primer**

- Informative (non-normative) introduction to WordprocessingML, SpreadsheetML, PresentationML, DrawingML, VML and Shared MLs, providing context and illustrating elements through examples and diagrams
- Describes the custom XML data-storing facility within a package to support integration with business data

**Part 4. Markup Language Reference**

- Contains the reference material for WordprocessingML, SpreadsheetML, PresentationML, DrawingML, Shared MLs and Custom XML Schema, defining every element and attribute including the element hierarchy (parent/child relationships)
- XML schemas for the markup languages are declared as XSD and (non-normatively) using RELAX NG
- Defines the custom XML data-storing facility

**Part 5. Markup Compatibility and Extensibility**

- Describes extension facilities of OpenXML documents and specifies elements & attributes through which applications can operate across different extensions.

Later versions of the ECMA-376 standard are aligned and technically equivalent to the corresponding ISO standard.

### ISO/IEC 29500:2008

The ISO/IEC standard is structured into four parts: Parts 1, 2 and 3 are independent standards; for example, Part 2, specifying Open Packaging Conventions, is used by other file formats including XPS and Design Web Format. Part 4 is to be read as a modification to Part 1, which it requires.

A technically equivalent set of texts is also published by Ecma as ECMA-376 2nd edition (2008).

**Part 1. Fundamentals & Markup Language Reference**

Consisting of 5560 pages, this part contains:

- Conformance definitions
- Reference material for the XML document markup languages defined by the Standard
- XML schemas for the document markup languages declared using XSD and (non-normatively) RELAX NG
- Defines the foreign markup facilities

**Part 2. Open Packaging Conventions**

Consisting of 129 pages, this part contains:

- A description of the Open Packaging Conventions (package model, physical package)
- Core properties, thumbnails and digital signatures
- XML schemas for the OPC are declared using XSD and (non-normatively) RELAX NG

**Part 3. Markup Compatibility and Extensibility**

Consisting of 40 pages, this part contains:

- A description of *extensions*: elements & attributes which define mechanisms allowing applications to specify alternative means of negotiating content
- Extensibility rules are expressed using NVDL

**Part 4. Transitional Migration Features**

Consisting of 1464 pages, this part contains:

- Legacy material such as compatibility settings and the graphics markup language VML
- A list of syntactic differences between this text and ECMA-376 1st Edition

The standard specifies two levels of document & application conformance, *strict* and *transitional,* for each of WordprocessingML, PresentationML and SpreadsheetML, and also specifies applications' descriptions of *base* and *full*.

### Compatibility between versions

The intent of the changes from ECMA-376 1st Edition to ISO/IEC 29500:2008 was that a valid ECMA-376 document would also be a valid ISO 29500 Transitional document; however, at least one change introduced at the BRM—refusing to allow further values for xsd:boolean—broke backwards-compatibility for most documents. A fix for this had been suggested to ISO/IEC JTC 1/SC 34/WG 4, and was approved in June 2009 as a recommendation for the first revision to Office Open XML.

Applications capable of reading documents compliant to ECMA-376 Edition 1 would regard ISO/IEC 29500-4 Transitional documents containing ISO 8601 dates as corrupt.

## Application support

Some older versions of Microsoft Word and Microsoft Office are able to read and write `.docx` files after installation of the free compatibility pack provided by Microsoft, although some items, such as equations, are converted into images that cannot be edited.

Starting with Microsoft Office 2007, the Office Open XML file formats have become the default file format of Microsoft Office. However, due to the changes introduced in the Office Open XML standard, Office 2007 is not wholly in compliance with ISO/IEC 29500:2008. Office 2010 includes support for opening documents of the ISO/IEC 29500:2008-compliant version of Office Open XML, but it can only save documents conforming to the *transitional*, not the *strict*, schemas of the specification. Note that the intent of the ISO/IEC is to allow the removal of the transitional variant from the ISO/IEC 29500 standard. Microsoft Office 2013 and later fully support ISO/IEC 29500 Strict, but do not use it as the default file format because of backwards compatibility concerns.

The ability to read and write Office Open XML format is, however, not limited to Microsoft Office; other office products are also able to read & write this format:

- Apache OpenOffice is able to import OOXML files, but defaults to the OpenDocument file format.
- Calligra Suite is able to import OOXML files, but defaults to the OpenDocument file format.
- Collabora Online, Mobile and Desktop editors are compatible with OOXML, but defaults to the OpenDocument file format.
- Google Docs, is able to read and write OOXML and OpenDocument files.
- LibreOffice Desktop editors are compatible with OOXML, but defaults to the OpenDocument file format.

Other office products that offer import support to various levels of compatibility include:

- Abiword is able to read and write OOXML and OpenDocument files.
- Gnumeric is able to read and write OOXML and OpenDocument files
- Go-oo, discontinued in 2010, could import and save to OOXML, but defaulted to the OpenDocument file format.
- iWork is able to read and write OOXML and OpenDocument files.
- KOffice, discontinued in 2011, could import and save to OOXML.
- NeoOffice, discontinued in 2024, could import and save to OOXML, but defaulted to the OpenDocument file format.
- OnlyOffice, Online and Desktop editors are compatible with OOXML and OpenDocument files.
- SoftMaker FreeOffice and SoftMaker Office are able to read and write OOXML and OpenDocument files (word processor only).
- TextEdit (included with macOS)
- WordPerfect, is able to read and write OOXML and OpenDocument files.
- WPS Office, is able to read and write OOXML files.

## Criticism

The Document Foundation, creators of LibreOffice and promoters of the OpenDocument format (ODF), has argued that OOXML is excessively complex and unnecessarily convoluted. According to the foundation, this discourages interoperability and contributes to user dependence on Microsoft software. In a comparative analysis, they reported that OOXML files were many times longer and more intricate than ODF files containing the same text, describing the additional verbosity and structural elements as a "maze" of tags and metadata that complicates non-Microsoft implementations.
