---
title: "Microsoft Excel"
source: https://en.wikipedia.org/wiki/Microsoft_Excel
domain: vba-macros
license: CC-BY-SA-4.0
tags: visual basic for applications, vba macros, excel vba, office vba
fetched: 2026-07-02
---

# Microsoft Excel

**Microsoft Excel**, or simply **Excel**, is a spreadsheet editor developed by Microsoft for Windows, macOS, Android, iOS and iPadOS. It features calculation or computation capabilities, graphing tools, pivot tables, and a macro programming language called Visual Basic for Applications (VBA).

Excel forms part of the Microsoft 365 and Microsoft Office suites of software and has been developed since 1985.

## Features

### Basic operation

Microsoft Excel has the basic features of all spreadsheets, using a grid of *cells* arranged in numbered *rows* and letter-named *columns* to organize data manipulations like arithmetic operations. It has a battery of supplied functions to answer statistical, engineering, and financial needs. In addition, it can display data as line graphs, histograms and charts, and with a very limited three-dimensional graphical display. It allows sectioning of data to view its dependencies on various factors for different perspectives (using *pivot tables* and the *scenario manager*). A PivotTable is a tool for data analysis. It does this by simplifying large data sets via PivotTable fields. It has a programming aspect, *Visual Basic for Applications*, allowing the user to employ a wide variety of numerical methods, for example, for solving differential equations of mathematical physics, and then reporting the results back to the spreadsheet. It also has a variety of interactive features allowing user interfaces that can completely hide the spreadsheet from the user, so the spreadsheet presents itself as a so-called *application*, or *decision support system* (DSS), via a custom-designed user interface, for example, a stock analyzer, or in general, as a design tool that asks the user questions and provides answers and reports. In a more elaborate realization, an Excel application can automatically poll external databases and measuring instruments using an update schedule, analyze the results, make a Word report or PowerPoint slide show, and email these presentations on a regular basis to a list of participants.

Microsoft allows for a number of optional command-line switches to control the manner in which Excel starts.

### Functions

Excel 2016 has 484 functions. Of these, 360 existed prior to Excel 2010. Microsoft classifies these functions into 14 categories. Of the 484 current functions, 386 may be called from VBA as methods of the object "WorksheetFunction" and 44 have the same names as VBA functions.

With the introduction of LAMBDA on December 3, 2020, Excel became Turing complete.

### Macro programming

#### VBA programming

The Windows version of Excel supports programming through Microsoft's Visual Basic for Applications (VBA), which is a dialect of Visual Basic. Programming with VBA allows spreadsheet manipulation that is awkward or impossible with standard spreadsheet techniques. Programmers may write code directly using the Visual Basic Editor (VBE), which includes a window for writing code, debugging code, and code module organization environment. The user can implement numerical methods as well as automating tasks such as formatting or data organization in VBA and guide the calculation using any desired intermediate results reported back to the spreadsheet.

VBA was removed from Mac Excel 2008, as the developers did not believe that a timely release would allow porting the VBA engine natively to Mac OS X. VBA was restored in the next version, Mac Excel 2011, although the build lacks support for ActiveX objects, impacting some high level developer tools.

A common and easy way to generate VBA code is by using the Macro Recorder. The Macro Recorder records actions of the user and generates VBA code in the form of a macro. These actions can then be repeated automatically by running the macro. The macros can also be linked to different trigger types like keyboard shortcuts, a command button or a graphic. The actions in the macro can be executed from these trigger types or from the generic toolbar options. The VBA code of the macro can also be edited in the VBE. Certain features such as loop functions and screen prompt by their own properties, and some graphical display items, cannot be recorded but must be entered into the VBA module directly by the programmer. Advanced users can employ user prompts to create an interactive program, or react to events such as sheets being loaded or changed.

Macro Recorded code may not be compatible with all Excel versions. Some code that is used in Excel 2010 cannot be used in Excel 2003. Making a Macro that changes the cell colors and making changes to other aspects of cells may not be backward compatible.

VBA code interacts with the spreadsheet through the Excel *Object Model*, a vocabulary identifying spreadsheet objects, and a set of supplied functions or *methods* that enable reading and writing to the spreadsheet and interaction with its users (for example, through custom toolbars or *command bars* and *message boxes*). User-created VBA subroutines execute these actions and operate like macros generated using the macro recorder, but are more flexible and efficient.

#### History

From its first version Excel supported end-user programming of macros (automation of repetitive tasks) and user-defined functions (extension of Excel's built-in function library). In early versions of Excel, these programs were written in a macro language whose statements had formula syntax and resided in the cells of special-purpose macro sheets (stored with file extension .XLM in Windows.) XLM was the default macro language for Excel through Excel 4.0. Beginning with version 5.0 Excel recorded macros in VBA by default but with version 5.0 XLM recording was still allowed as an option. After version 5.0 that option was discontinued. All versions of Excel, including Excel 2021, are capable of running an XLM macro, though Microsoft discourages their use.

### Python programming

In 2023, Microsoft announced Excel would support the Python programming language directly. As of 2025, Python in Excel is available to Enterprise and Business users (with some exceptions, and is in preview for Family, Personal, and Education users).

### Charts

Excel supports charts, graphs, or histograms generated from specified groups of cells. It also supports Pivot Charts that allow for a chart to be linked directly to a Pivot table. This allows the chart to be refreshed with the Pivot Table. The generated graphic component can either be embedded within the current sheet or added as a separate object.

These displays are dynamically updated if the content of cells changes. For example, suppose that the important design requirements are displayed visually; then, in response to a user's change in trial values for parameters, the curves describing the design change shape, and their points of intersection shift, assisting the selection of the best design.

### Add-ins

Additional features are available using add-ins. Several are provided with Excel, including:

- Analysis ToolPak: Provides data analysis tools for statistical and engineering analysis (includes analysis of variance and regression analysis)
- Analysis ToolPak VBA: VBA functions for Analysis ToolPak
- Euro Currency Tools: Conversion and formatting for euro currency
- Solver Add-In: Tools for optimization and equation solving

## Data storage and communication

### Number of rows and columns

Versions of Excel up to 7.0 had a limitation in the size of their data sets of 16K (214 = 16384) rows. Versions 8.0 through 11.0 could handle 64K (216 = 65536) rows and 256 columns (28 as label 'IV'). Version 12.0 onwards, including the current Version 16.x, can handle over 1M (220 = 1048576) rows, and 16384 (214, labeled as column 'XFD') columns.

### File formats

Up until the 2007 version, Microsoft Excel used a proprietary binary file format called Excel Binary File Format (.XLS) as its primary format. Excel 2007 uses Office Open XML as its primary file format, an XML-based format that followed after a previous XML-based format called "XML Spreadsheet" ("XMLSS"), first introduced in Excel 2002.

Although supporting and encouraging the use of new XML-based formats as replacements, Excel 2007 remained backwards-compatible with the traditional, binary formats. In addition, most versions of Microsoft Excel can read CSV, DBF, SYLK, DIF, and other legacy formats. Support for some older file formats, mostly from DOS-based programs, was removed in Excel 2007.

#### Binary

OpenOffice.org has created documentation of the Excel format. Two epochs of the format exist: the 97-2003 OLE format, and the older stream format. Microsoft has made the Excel binary format specification available to freely download.

#### XML Spreadsheet

The *XML Spreadsheet* format introduced in Excel 2002 is a simple, XML based format missing some more advanced features like storage of VBA macros. Though the intended file extension for this format is *.xml*, the program also correctly handles XML files with *.xls* extension. This feature is widely used by third-party applications (e.g. *MySQL Query Browser*) to offer "export to Excel" capabilities without implementing binary file format. The following example will be correctly opened by Excel if saved either as *Book1.xml* or *Book1.xls*:

```mw
<?xml version="1.0"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <Worksheet ss:Name="Sheet1">
  <Table ss:ExpandedColumnCount="2" ss:ExpandedRowCount="2" x:FullColumns="1" x:FullRows="1">
   <Row>
    <Cell><Data ss:Type="String">Name</Data></Cell>
    <Cell><Data ss:Type="String">Example</Data></Cell>
   </Row>
   <Row>
    <Cell><Data ss:Type="String">Value</Data></Cell>
    <Cell><Data ss:Type="Number">123</Data></Cell>
   </Row>
  </Table>
 </Worksheet>
</Workbook>
```

#### Current file extensions

Microsoft Excel 2007, along with the other products in the Microsoft Office 2007 suite, introduced new file formats. The first of these (.xlsx) is defined in the Office Open XML (OOXML) specification.

| Format | Extension | Description |
|---|---|---|
| Excel Workbook | `.xlsx` | The default Excel 2007 and later workbook format. In reality, a ZIP compressed archive with a directory structure of XML text documents. Functions as the primary replacement for the former binary .xls format, although it does not support Excel macros for security reasons. Saving as .xlsx offers file size reduction over .xls |
| Excel Macro-enabled Workbook | `.xlsm` | As Excel Workbook, but with macro support. |
| Excel Binary Workbook | `.xlsb` | As Excel Macro-enabled Workbook, but storing information in binary form rather than XML documents for opening and saving documents more quickly and efficiently. Intended especially for very large documents with tens of thousands of rows, and/or several hundreds of columns. This format is very useful for shrinking large Excel files as is often the case when doing data analysis. |
| Excel Macro-enabled Template | `.xltm` | A template document that forms a basis for actual workbooks, with macro support. The replacement for the old .xlt format. |
| Excel Add-in | `.xlam` | Excel add-in to add extra functionality and tools. Inherent macro support because of the file purpose. |

#### Old file extensions

| Format | Extension | Description |
|---|---|---|
| Spreadsheet | `.xls` | Main spreadsheet format which holds data in worksheets, charts, and macros |
| Add-in (VBA) | `.xla` | Adds custom functionality; written in VBA |
| Toolbar | `.xlb` | The file extension where Microsoft Excel custom toolbar settings are stored. |
| Chart | `.xlc` | A chart created with data from a Microsoft Excel spreadsheet that only saves the chart. To save the chart and spreadsheet save as .XLS. XLC is not supported in Excel 2007 or in any newer versions of Excel. |
| Dialog | `.xld` | Used in older versions of Excel |
| Archive | `.xlk` | A backup of an Excel spreadsheet |
| Add-in (DLL) | `.xll` | Adds custom functionality; written in C++/C, Fortran, etc. and compiled into a special dynamic-link library |
| Macro | `.xlm` | A macro is created by the user or pre-installed with Excel. |
| Template | `.xlt` | A pre-formatted spreadsheet created by the user or by Microsoft Excel |
| Module | `.xlv` | A module written in VBA (Visual Basic for Applications) for Microsoft Excel |
| Library | `.DLL` | Code written in VBA may access functions in a DLL, typically this is used to access the Windows API |
| Workspace | `.xlw` | Arrangement of the windows of multiple Workbooks |

### Using other Windows applications

Windows applications such as Microsoft Access and Microsoft Word, as well as Excel can communicate with each other and use each other's capabilities. The most common is Dynamic Data Exchange: although strongly deprecated by Microsoft, this is a common method to send data between applications running on Windows, with official MS publications referring to it as "the protocol from hell". As the name suggests, it allows applications to supply data to others for calculation and display. It is very common in financial markets, being used to connect to important financial data services such as Bloomberg and Reuters.

OLE Object Linking and Embedding allows a Windows application to control another to enable it to format or calculate data. This may take on the form of "embedding" where an application uses another to handle a task that it is more suited to, for example a PowerPoint presentation may be embedded in an Excel spreadsheet or vice versa.

### Using external data

Excel users can access external data sources via Microsoft Office features such as (for example) `.odc` connections built with the Office Data Connection file format. Excel files themselves may be updated using a Microsoft supplied ODBC driver.

Excel can accept data in real-time through several programming interfaces, which allow it to communicate with many data sources such as Bloomberg and Reuters (through addins such as Power Plus Pro).

- Dynamic Data Exchange uses the message passing mechanism in Windows to allow data to flow between Excel and other applications. Although it is easy for users to create such links, programming such links reliably is so difficult that Microsoft, the creators of the system, officially refer to it as "the protocol from hell". In spite of its many issues DDE remains the most common way for data to reach traders in financial markets.
- Network DDE extended the DDE protocol to allow spreadsheets on different computers to exchange data. Starting with Windows Vista, Microsoft no longer supports Network DDE.
- Real Time Data, although in many ways technically superior to DDE, has been slow to gain acceptance, since it requires non-trivial programming skills, and when first released was neither adequately documented nor supported by major data vendors.

Alternatively, Microsoft Query provides ODBC-based browsing within Microsoft Excel.

### Export and migration of spreadsheets

Programmers have produced APIs to open Excel spreadsheets in a variety of applications and environments other than Microsoft Excel. These include opening Excel documents on the web using either ActiveX controls, or plugins like the Adobe Flash Player. The Apache POI open-source project provides Java libraries for reading and writing Excel spreadsheet files.

### Password protection

Microsoft Excel protection offers several types of passwords:

- Password to open a document
- Password to modify a document
- Password to unprotect the worksheet
- Password to protect workbook
- Password to protect the sharing workbook

All passwords except *password to open a document* can be removed instantly regardless of the Microsoft Excel version used to create the document. These types of passwords are used primarily for shared work on a document. Such password-protected documents are not encrypted, and data sources from a set password are saved in a document's header. *Password to protect workbook* is an exception – when it is set, a document is encrypted with the standard password "VelvetSweatshop", but since it is known to the public, it actually does not add any extra protection to the document. The only type of password that can prevent a trespasser from gaining access to a document is the *password to open a document*. The cryptographic strength of this kind of protection depends strongly on the Microsoft Excel version that was used to create the document.

In *Microsoft Excel 95* and earlier versions, the password to open is converted to a 16-bit key that can be instantly cracked. In *Excel 97/2000* the password is converted to a 40-bit key, which can also be cracked very quickly using modern equipment. As regards services that use rainbow tables (e.g. Password-Find), it takes up to several seconds to remove protection. In addition, password-cracking programs can brute-force attack passwords at a rate of hundreds of thousands of passwords a second, which not only lets them decrypt a document but also find the original password.

In *Excel 2003/XP* the encryption is slightly better – a user can choose any encryption algorithm that is available in the system (see Cryptographic Service Provider). Due to the CSP, an *Excel* file cannot be decrypted, and thus the *password to open* cannot be removed, though the brute-force attack speed remains quite high. Nevertheless, the older *Excel 97/2000* algorithm is set by the default. Therefore, users who do not change the default settings lack reliable protection of their documents.

The situation changed fundamentally in *Excel 2007*, where the modern AES algorithm with a key of 128 bits started being used for decryption, and a 50,000-fold use of the hash function SHA1 reduced the speed of brute-force attacks down to hundreds of passwords per second. In *Excel 2010*, the strength of the protection by the default was increased two times due to the use of a 100,000-fold SHA1 to convert a password to a key.

## Other platforms

### Excel for mobile

Excel Mobile is a spreadsheet program that can edit XLSX files. It can edit and format text in cells, calculate formulas, search within the spreadsheet, sort rows and columns, freeze panes, filter the columns, add comments, and create charts. It cannot add columns or rows except at the edge of the document, rearrange columns or rows, delete rows or columns, or add spreadsheet tabs. The 2007 version has the ability to use a full-screen mode to deal with limited screen resolution, as well as split panes to view different parts of a worksheet at one time. Protection settings, zoom settings, autofilter settings, certain chart formatting, hidden sheets, and other features are not supported on Excel Mobile, and will be modified upon opening and saving a workbook. In 2015, Excel Mobile became available for Windows 10 and Windows 10 Mobile on Windows Store.

### Excel for the web

Excel for the web is a free lightweight version of Microsoft Excel available as part of Office on the web, which also includes web versions of Microsoft Word and Microsoft PowerPoint.

Excel for the web can display most of the features available in the desktop versions of Excel, although it may not be able to insert or edit them. Certain data connections are not accessible on Excel for the web, including with charts that may use these external connections. Excel for the web also cannot display legacy features, such as Excel 4.0 macros or Excel 5.0 dialog sheets. There are also small differences between how some of the Excel functions work.

## Microsoft Excel Viewer

Microsoft Excel Viewer was a freeware program for Microsoft Windows for viewing and printing spreadsheet documents created by Excel. Microsoft retired the viewer in April 2018 with the last security update released in February 2019 for Excel Viewer 2007 (SP3).

The first version released by Microsoft was Excel 97 Viewer. Excel 97 Viewer was supported in Windows CE for Handheld PCs. In October 2004, Microsoft released Excel Viewer 2003. In September 2007, Microsoft released Excel Viewer 2003 Service Pack 3 (SP3). In January 2008, Microsoft released Excel Viewer 2007 (featuring a non-collapsible Ribbon interface). In April 2009, Microsoft released Excel Viewer 2007 Service Pack 2 (SP2). In October 2011, Microsoft released Excel Viewer 2007 Service Pack 3 (SP3).

Microsoft advises those who wish to view and print Excel files for free to use the Excel Mobile application for Windows 10 and for Windows 7 and Windows 8 to upload the file to OneDrive and use Excel for the web with a Microsoft account to open them in a browser.

## Limitations and errors

In addition to issues with spreadsheets in general, other problems specific to Excel include numeric precision, misleading statistics functions, mod function errors, date limitations and more.

### Numeric precision

Despite the use of 15-figure precision, Excel can display many more figures (up to thirty) upon user request. But the displayed figures are *not* those actually used in its computations, and so, for example, the difference of two numbers may differ from the difference of their displayed values. Although such departures are usually beyond the 15th decimal, exceptions do occur, especially for very large or very small numbers. Serious errors can occur if decisions are made based upon automated comparisons of numbers (for example, using the Excel *If* function), as equality of two numbers can be unpredictable.

In the figure, the fraction 1/9000 is displayed in Excel. Although this number has a decimal representation that is an infinite string of ones, Excel displays only the leading 15 figures. In the second line, the number one is added to the fraction, and again Excel displays only 15 figures. In the third line, one is subtracted from the sum using Excel. Because the sum in the second line has only eleven 1's after the decimal, the difference when 1 is subtracted from this displayed value is three 0's followed by a string of eleven 1's. However, the difference reported by Excel in the third line is three 0's followed by a string of *thirteen* 1's and two extra erroneous digits. This is because Excel calculates with about half a digit more than it displays.

Excel works with a modified 1985 version of the IEEE 754 specification. Excel's implementation involves conversions between binary and decimal representations, leading to accuracy that is on average better than one would expect from simple fifteen digit precision, but that can be worse. See the main article for details.

Besides accuracy in user computations, the question of accuracy in Excel-provided functions may be raised. Particularly in the arena of statistical functions, Excel has been criticized for sacrificing accuracy for speed of calculation.

As many calculations in Excel are executed using VBA, an additional issue is the accuracy of VBA, which varies with variable type and user-requested precision.

### Statistical functions

The accuracy and convenience of statistical tools in Excel has been criticized, as mishandling situations when data is missing, as returning incorrect values due to inept handling of round-off and large numbers, as only selectively updating calculations on a spreadsheet when some cell values are changed, and as having a limited set of statistical tools. Microsoft has announced that some of these issues are addressed in Excel 2010.

### Excel MOD function error

Excel has issues with modulo operations. In the case of excessively large results, Excel will return the error warning #NUM! instead of an answer.

### Fictional leap day in 1900

Excel includes February 29, 1900, incorrectly treating 1900 as a leap year, even though e.g. 2100 is correctly treated as a non-leap year. Thus, a formula counting dates between (for example) February 1, 1900 and March 1, 1900 will return an incorrect result. The bug originated from Lotus 1-2-3, where it was deliberately implemented to save computer memory, and was also intentionally implemented in Excel for the purpose of bug compatibility. This legacy has later been carried over into Office Open XML file format.

### Date range

Excel supports dates with years in the range 1900–9999, except that December 31, 1899, can be entered as 0 and is displayed as 0-jan-1900.

Converting a fraction of a day into hours, minutes and days by treating it as a moment on the day January 1, 1900, does not work for a negative fraction.

### Conversion problems

If text is entered that happens to be in a form that Excel interprets as a date, the text can be unintentionally changed to a standard date format. A similar problem occurs when a text happens to be in the form of a floating-point notation of a number. In these cases the original exact text cannot be recovered from the result. Formatting the cell as TEXT before entering ambiguous text prevents Excel from converting it.

This issue has caused a well known problem in the analysis of DNA, for example in bioinformatics. As first reported in 2004, genetic scientists found that Excel automatically and incorrectly converts certain gene names into dates. A follow-up study in 2016 found many peer reviewed scientific journal papers had been affected and that "Of the selected journals, the proportion of published articles with Excel files containing gene lists that are affected by gene name errors is 19.6%." Excel parses the copied and pasted data and sometimes changes them depending on what it thinks they are. For example, MARCH1 (Membrane Associated Ring-CH-type finger 1) gets converted to the date March 1 (1-Mar) and SEPT2 (Septin 2) is converted into September 2 (2-Sep) etc. While some secondary news sources reported this as a fault with Excel, the original authors of the 2016 paper placed the blame with the researchers misusing Excel.

In August 2020 the HUGO Gene Nomenclature Committee (HGNC) published new guidelines in the journal Nature regarding gene naming in order to avoid issues with "symbols that affect data handling and retrieval." As of 2020, 27 genes had been renamed, including changing MARCH1 to MARCHF1 and SEPT1 to SEPTIN1 in order to avoid accidental conversion of the gene names into dates.

In October 2023, Microsoft introduced a settings option that allows the conversion to be disabled.

### Errors with large strings

The following functions return incorrect results when passed a string longer than 255 characters:

- `type()` incorrectly returns 16, meaning "Error value"
- `IsText()`, when called as a method of the VBA object `WorksheetFunction` (i.e., `WorksheetFunction.IsText()` in VBA), incorrectly returns "false".

### Filenames

Microsoft Excel will not open two documents with the same name and instead will display the following error:

A document with the name '%s' is already open. You cannot open two documents with the same name, even if the documents are in different folders. To open the second document, either close the document that is currently open, or rename one of the documents.

The reason is for calculation ambiguity with linked cells. If there is a cell `='[Book1.xlsx]Sheet1'!$G$33`, and there are two books named "Book1" open, there is no way to tell which one the user means.

## Versions

### Early history

In 1982, Microsoft launched its first spreadsheet program, Multiplan, which gained popularity on CP/M systems. However, Multiplan struggled to compete on MS-DOS systems, losing market share to Lotus 1-2-3, which became the dominant spreadsheet program by 1983, surpassing both Multiplan and the earlier VisiCalc.

To address Multiplan's falling marketshare, Microsoft began developing a new, advanced spreadsheet program in 1983, codenamed "Odyssey." The project was led by Jabe Blumenthal, who worked on its design, and Doug Klunder, the primary developer of Multiplan. Originally intended for IBM PCs running CP/M and MS-DOS, the project shifted focus in early 1984 when Lotus began developing Jazz, an integrated program for the Apple Macintosh, and Lotus 1-2-3 maintained its dominance on IBM PCs. In March 1984, Bill Gates redirected Odyssey's development to the Macintosh platform, which required supporting the system's 512 KB memory. This decision delayed the project by nine months, after which Klunder temporarily left Microsoft to work growing lettuce, and the project then was led by Philip Florence, a former developer at Wang Laboratories. After Florence had a heart attack, Klunder returned to finish the project.

On May 2, 1985, Steve Jobs of Apple Computer and Bill Gates held a joint press conference at Tavern on the Green in New York City to publicly announce Excel for Apple's Macintosh platform. Following the announcement, the software was officially released for sale on September 30, 1985. The first Windows version, Excel 2.05, followed on November 19, 1987, designed to align with the Macintosh version 2.2. A 1990 American Institute of Certified Public Accountants member survey found that 2% of respondents used Excel as their spreadsheet, 3% as their database, and 8% for graphics. Lotus was slow to bring 1-2-3 to Windows and by the early 1990s, Excel had started to outsell 1-2-3 and helped Microsoft achieve its position as a leading PC software developer. This accomplishment solidified Microsoft as a valid competitor and showed its future in developing GUI software. Microsoft maintained its advantage with regular new releases, every two years or so.

### Microsoft Windows

Excel 2.0 is the first version of Excel for the Intel platform. Versions prior to 2.0 were only available on the Apple Macintosh.

#### Excel 2.0 (1987)

The first Windows version was labeled "2" to correspond to the Mac version. It was announced on October 6, 1987, and released on November 19. This included a runtime version of Windows.

*BYTE* in 1989 listed Excel for Windows as among the "Distinction" winners of the BYTE Awards. The magazine stated that the port of the "extraordinary" Macintosh version "shines", with a user interface as good as or better than the original.

#### Excel 3.0 (1990)

Included toolbars, drawing capabilities, outlining, add-in support, 3D charts, and many more new features.

#### Excel 4.0 (1992)

Included with Microsoft Office 3.0, this version introduced auto-fill.

Also, an easter egg in Excel 4.0 reveals a hidden animation of a dancing set of numbers 1 through 3, representing Lotus 1–2–3, which is then crushed by an Excel logo.

#### Excel 5.0 (1993)

With version 5.0, included in Microsoft Office 4.2 and 4.3, Excel included Visual Basic for Applications (VBA), a programming language based on Visual Basic which adds the ability to automate tasks in Excel and to provide user-defined functions (UDF) for use in worksheets. VBA includes a fully featured integrated development environment (IDE). Macro recording can produce VBA code replicating user actions, thus allowing simple automation of regular tasks. VBA allows the creation of forms and in‑worksheet controls to communicate with the user. The language supports use (but not creation) of ActiveX (COM) DLL's; later versions add support for class modules allowing the use of basic object-oriented programming techniques.

The automation functionality provided by VBA made Excel a target for macro viruses. This caused serious problems until antivirus products began to detect these viruses. Microsoft belatedly took steps to prevent the misuse by adding the ability to disable macros completely, to enable macros when opening a workbook or to trust all macros signed using a trusted certificate.

Versions 5.0 to 9.0 of Excel contain various Easter eggs, including a "Hall of Tortured Souls", a *Doom*-like minigame, although since version 10 Microsoft has taken measures to eliminate such undocumented features from their products.

5.0 was released in a 16-bit x86 version for Windows 3.1 and later in a 32-bit version for NT 3.51 (x86/Alpha/PowerPC)

#### Excel 95 (v7.0)

Released in 1995 with Microsoft Office for Windows 95, this is the first major version after Excel 5.0, as there is no Excel 6.0 with all of the Office applications standardizing on the same major version number.

Internal rewrite to 32-bits. Almost no external changes, but faster and more stable.

Excel 95 contained a hidden *Doom*-like mini-game called "The Hall of Tortured Souls", a series of rooms featuring the names and faces of the developers as an Easter egg.

#### Excel 97 (v8.0)

Included in Office 97 (for x86 and Alpha). This was a major upgrade that introduced the paper clip office assistant and featured standard VBA used instead of internal Excel Basic. It introduced the now-removed Natural Language labels.

This version of Excel includes a flight simulator as an Easter egg.

#### Excel 2000 (v9.0)

Included in Office 2000. This was a minor upgrade but introduced an upgrade to the clipboard where it can hold multiple objects at once. The Office Assistant, whose frequent unsolicited appearance in Excel 97 had annoyed many users, became less intrusive.

A small 3-D game called "Dev Hunter" (inspired by Spy Hunter) was included as an Easter egg.

#### Excel 2002 (v10.0)

Included in Office XP with minor enhancements over the previous version.

#### Excel 2003 (v11.0)

Included in Office 2003 with minor enhancements over the previous version.

#### Excel 2007 (v12.0)

Included in Office 2007. This release was a major upgrade from the previous version. Similar to other updated Office products, Excel in 2007 used the new Ribbon menu system. This was different from what users were used to, and was met with mixed reactions. One study reported fairly good acceptance by users except for highly experienced users and users of word processing applications with a classical WIMP interface, but was less convinced in terms of efficiency and organization. However, an online survey reported that a majority of respondents had a negative opinion of the change, with advanced users being "somewhat more negative" than intermediate users, and users reporting a self-estimated reduction in productivity.

Added functionality included Tables, and the SmartArt set of editable business diagrams. Also added was an improved management of named variables through the *Name Manager*, and much-improved flexibility in formatting graphs, which allow (*x, y*) coordinate labeling and lines of arbitrary weight. Several improvements to pivot tables were introduced.

Also like other office products, the Office Open XML file formats were introduced, including *.xlsm* for a workbook with macros and *.xlsx* for a workbook without macros.

Specifically, many of the size limitations of previous versions were greatly increased. To illustrate, the number of rows was now 1,048,576 (220) and the columns was 16,384 (214; the far-right column is XFD). This changes what is a valid *A1* reference versus a named range. This version made more extensive use of multiple cores for the calculation of spreadsheets; however, VBA macros are not handled in parallel and XLL add‑ins were only executed in parallel if they were thread-safe and this was indicated at registration.

#### Excel 2010 (v14.0)

Included in Office 2010, this is the next major version after v12.0, as version number 13 was skipped.

Minor enhancements and 64-bit support, including the following:

- Multi-threading recalculation (MTR) for commonly used functions
- Improved pivot tables
- More conditional formatting options
- Additional image editing capabilities
- In-cell charts called *sparklines*
- Ability to preview before pasting
- Office 2010 *backstage* feature for document-related tasks
- Ability to customize the Ribbon
- Many new formulas, most highly specialized to improve accuracy

#### Excel 2013 (v15.0)

Included in Office 2013, along with a lot of new tools included in this release:

- Improved Multi-threading and Memory Contention
- FlashFill
- Power View
- Power Pivot
- Timeline Slicer
- Windows App
- Inquire
- 50 new functions

#### Excel 2016 (v16.0)

Included in Office 2016, along with a lot of new tools included in this release:

- Power Query integration
- Read-only mode for Excel
- Keyboard access for Pivot Tables and Slicers in Excel
- New Chart Types
- Quick data linking in Visio
- Excel forecasting functions
- Support for multi-selection of Slicer items using touch
- Time grouping and Pivot Chart Drill Down
- Excel data cards

#### Excel 2019, Excel 2021, Excel 2024, Office 365 and subsequent (v16.0)

Microsoft no longer releases Office or Excel in distinctive versions. Instead, features are introduced automatically over time. The version number remains 16.0. Thereafter only the approximate dates when features appear can now be given. New features include:

- Dynamic Arrays. These are essentially Array Formulas but they "Spill" automatically into neighboring cells and do not need the ctrl-shift-enter to create them. Further, dynamic arrays are the default format, with new "@" and "#" operators to provide compatibility with previous versions. This is perhaps the biggest structural change since 2007, and is in response to a similar feature in Google Sheets. Dynamic arrays started appearing in pre-releases about 2018, and as of March 2020 are available in published versions of Office 365 provided a user selected "Office Insiders".

Microsoft Office 2024 (the fourth perpetual release of Office 16.0) for the Microsoft Windows and macOS was released on October 1, 2024.

### Mac

- 1985 Excel 1.0
- 1988 Excel 1.5
- 1989 Excel 2.2
- 1990 Excel 3.0
- 1992 Excel 4.0
- 1993 Excel 5.0 (part of Office 4.x—Final Motorola 680x0 version and first PowerPC version)
- 1998 Excel 8.0 (part of Office 98)
- 2000 Excel 9.0 (part of Office 2001)
- 2001 Excel 10.0 (part of Office v. X)
- 2004 Excel 11.0 (part of Office 2004)
- 2008 Excel 12.0 (part of Office 2008)
- 2010 Excel 14.0 (part of Office 2011)
- 2015 Excel 15.0 (part of Office 2016—Office 2016 for Mac brings the Mac version much closer to parity with its Windows cousin, harmonizing many of the reporting and high-level developer functions, while bringing the ribbon and styling into line with its PC counterpart.)
- Part of Microsoft Office 2019 for Mac
- Part of Microsoft Office 2021 for Mac
- Part of Microsoft Office 2024 for Mac

### OS/2

- 1989 Excel 2.2
- 1990 Excel 2.3
- 1991 Excel 3.0

### Summary

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

| Year | Name | Version | Comments |
|---|---|---|---|
| 1987 | Excel 2 | Unsupported: 2.0 | Renumbered to 2 to correspond with contemporary Macintosh version. Supported macros (later known as Excel 4 macros). |
| 1990 | Excel 3 | Unsupported: 3.0 | Added 3D graphing capabilities |
| 1992 | Excel 4 | Unsupported: 4.0 | Introduced auto-fill feature |
| 1993 | Excel 5 | Unsupported: 5.0 | Included Visual Basic for Applications (VBA) and various object-oriented options |
| 1995 | Excel 95 | Unsupported: 7.0 | Renumbered for contemporary Word version. Both programs were packaged in Microsoft Office by this time. |
| 1997 | Excel 97 | Unsupported: 8.0 |   |
| 2000 | Excel 2000 | Unsupported: 9.0 | Part of Microsoft Office 2000 |
| 2002 | Excel 2002 | Unsupported: 10.0 |   |
| 2003 | Excel 2003 | Unsupported: 11.0 | Released only 1 year later to correspond better with the rest of Microsoft Office (Word, PowerPoint, etc.). |
| 2007 | Excel 2007 | Unsupported: 12.0 |   |
| 2010 | Excel 2010 | Unsupported: 14.0 | Due to superstitions surrounding the number 13, Excel 13 was skipped in version counting. |
| 2013 | Excel 2013 | Unsupported: 15.0 | Introduced 50 more mathematical functions (available as pre-packaged commands, rather than typing the formula manually). |
| 2016 | Excel 2016 | Unsupported: 16.0 | Part of Microsoft Office 2016 |
| 2019 | Excel 2019 | Unsupported: 17.0 | Part of Microsoft Office 2019 |
| 2021 | Excel 2021 | Supported: 17.0 | Part of Microsoft Office 2021 |
| 2024 | Excel 2024 | Latest version: 17.0 | Part of Microsoft Office 2024 |

| Year | Name | Version | Comments |
|---|---|---|---|
| 1985 | Excel 1 | Unsupported: 1.0 | Initial version of Excel. Supported macros (later known as Excel 4 macros). |
| 1988 | Excel 1.5 | Unsupported: 1.5 |   |
| 1989 | Excel 2 | Unsupported: 2.2 |   |
| 1990 | Excel 3 | Unsupported: 3.0 |   |
| 1992 | Excel 4 | Unsupported: 4.0 |   |
| 1993 | Excel 5 | Unsupported: 5.0 | Only available on PowerPC-based Macs. First PowerPC version. |
| 1998 | Excel 98 | Unsupported: 8.0 | Excel 6 and Excel 7 were skipped to correspond with the rest of Microsoft Office at the time. |
| 2000 | Excel 2000 | Unsupported: 9.0 |   |
| 2001 | Excel 2001 | Unsupported: 10.0 |   |
| 2004 | Excel 2004 | Unsupported: 11.0 |   |
| 2008 | Excel 2008 | Unsupported: 12.0 |   |
| 2011 | Excel 2011 | Unsupported: 14.0 | As with the Windows version, version 13 was skipped for superstitious reasons. |
| 2016 | Excel 2016 | Unsupported: 16.0 | Future release dates for the Macintosh version are intended to correspond better to those for the Windows version, from 2016 onward. |
| 2019 | Excel 2019 | Unsupported: 17.0 | Part of Microsoft Office 2019 |
| 2021 | Excel 2021 | Supported: 17.0 | Part of Microsoft Office 2021 |
| 2024 | Excel 2024 | Latest version: 17.0 | Part of Microsoft Office 2024 |

| Year | Name | Version | Comments |
|---|---|---|---|
| 1989 | Excel 2.2 | Unsupported: 2.2 | Numbered in between Windows versions at the time |
| 1990 | Excel 2.3 | Unsupported: 2.3 |   |
| 1991 | Excel 3 | Unsupported: 3.0 | Last OS/2 version. Discontinued subseries of Microsoft Excel, which is otherwise still an actively developed program. |

## Impact

Excel offers many user interface tweaks over the earliest electronic spreadsheets; however, the essence remains the same as in the original spreadsheet software, VisiCalc: the program displays cells organized in rows and columns, and each cell may contain data or a formula, with relative or absolute references to other cells.

Excel 2.0 for Windows, which was modeled after its Mac GUI-based counterpart, indirectly expanded the installed base of the then-nascent Windows environment. Excel 2.0 was released a month before Windows 2.0, and the installed base of Windows was so low at that point in 1987 that Microsoft had to bundle a runtime version of Windows 1.0 with Excel 2.0. Unlike Microsoft Word, there never was a DOS version of Excel.

Excel became the first spreadsheet to allow the user to define the appearance of spreadsheets (fonts, character attributes, and cell appearance). It also introduced intelligent cell re-computation, where only cells dependent on the cell being modified are updated (previous spreadsheet programs recomputed everything all the time or waited for a specific user command). Excel introduced auto-fill, the ability to drag and expand the selection box to automatically copy a cell or row contents to adjacent cells or rows, adjusting the copies intelligently by automatically incrementing cell references or contents. Excel also introduced extensive graphing capabilities.

Excel holds a central place in modern office work: a 2022 survey found that two-thirds of office workers use Excel at least once per hour, spending 38% of their total working time inside the program. It is estimated between 750 million and 1.2 billion users access Excel each month.

## Security

Because Excel is widely used, it has been attacked by hackers. While Excel is not directly exposed to the Internet, if an attacker can get a victim to open a file in Excel, and there is an appropriate security bug in Excel, then the attacker can gain control of the victim's computer. UK's GCHQ has a tool named TORNADO ALLEY with this purpose.

## Games

Besides the easter eggs, numerous games have been created or recreated in Excel, such as *Tetris*, *2048*, *Scrabble*, *Yahtzee*, *Angry Birds*, *Pac-Man*, *Civilization*, *Monopoly*, *Battleship*, Blackjack, *Space Invaders*, and others.

In 2020, Excel became an esport with the advent of the Financial Modeling World Cup.
