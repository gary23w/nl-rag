---
title: "Doxygen: Configuration (part 4/5)"
source: https://www.doxygen.nl/manual/config.html
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
part: 4/5
---

# Configuration options related to the LaTeX output

**`GENERATE_LATEX`**

If the `GENERATE_LATEX` tag is set to `YES`, Doxygen will generate ($\mbox{\LaTeX}$) output.

The default value is: `YES`.

**`LATEX_OUTPUT`**

The `LATEX_OUTPUT` tag is used to specify where the ($\mbox{\LaTeX}$) docs will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it.

The default directory is: `latex`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_CMD_NAME`**

The `LATEX_CMD_NAME` tag can be used to specify the ($\mbox{\LaTeX}$) command name to be invoked. Note that when not enabling USE_PDFLATEX the default is `latex` when enabling USE_PDFLATEX the default is `pdflatex` and when in the later case `latex` is chosen this is overwritten by `pdflatex`. For specific output languages the default can have been set differently, this depends on the implementation of the output language.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`MAKEINDEX_CMD_NAME`**

The `MAKEINDEX_CMD_NAME` tag can be used to specify the command name to generate index for ($\mbox{\LaTeX}$).

**Note**

This tag is used in the

Makefile

/

make.bat

.

**See also**

LATEX_MAKEINDEX_CMD

for the part in the generated output file (

.tex

).

The default file is: `makeindex`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_MAKEINDEX_CMD`**

The `LATEX_MAKEINDEX_CMD` tag can be used to specify the command name to generate index for ($\mbox{\LaTeX}$). In case there is no backslash (\\endiskip) as first character it will be automatically added in the ($\mbox{\LaTeX}$) code.

**Note**

This tag is used in the generated output file (

.tex

).

**See also**

MAKEINDEX_CMD_NAME

for the part in the

Makefile

/

make.bat

.

The default value is: `makeindex`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`COMPACT_LATEX`**

If the `COMPACT_LATEX` tag is set to `YES`, Doxygen generates more compact ($\mbox{\LaTeX}$) documents. This may be useful for small projects and may help to save some trees in general.

The default value is: `NO`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`PAPER_TYPE`**

The `PAPER_TYPE` tag can be used to set the paper type that is used by the printer.

Possible values are: `a4` (210 x 297 mm), `letter` (8.5 x 11 inches), `legal` (8.5 x 14 inches) and `executive` (7.25 x 10.5 inches).

The default value is: `a4`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`EXTRA_PACKAGES`**

The `EXTRA_PACKAGES` tag can be used to specify one or more ($\mbox{\LaTeX}$) package names that should be included in the ($\mbox{\LaTeX}$) output. The package can be specified just by its name or with the correct syntax as to be used with the ($\mbox{\LaTeX}$) \usepackage command.

To get the times font for instance you can specify :

```
  EXTRA_PACKAGES=times
or
  EXTRA_PACKAGES={times}
```

To use the option intlimits with the amsmath package you can specify:

```
   EXTRA_PACKAGES=[intlimits]{amsmath}
```

If left blank no extra packages will be included.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_HEADER`**

The `LATEX_HEADER` tag can be used to specify a user-defined ($\mbox{\LaTeX}$) header for the generated ($\mbox{\LaTeX}$) document. The header should contain everything until the first chapter. If it is left blank Doxygen will generate a standard header.

It is highly recommended to start with a default header using

```
doxygen -w latex new_header.tex new_footer.tex new_stylesheet.sty
```

and then modify the file `new_header.tex`.

See also section Doxygen usage for information on how to generate the default header that Doxygen normally uses.

Note: Only use a user-defined header if you know what you are doing!

**Note**

The header is subject to change so you typically have to regenerate the default header when upgrading to a newer version of Doxygen. The following commands have a special meaning inside the header (and footer):

**`$title`**

will be replaced with the project name.

**`$datetime`**

will be replaced with the current date and time.

**`$date`**

will be replaced with the current date.

**`$time`**

will be replaced with the current time.

**`$year`**

will be replaced with the current year.

**`$showdate(<format>)`**

will be replaced with the current date and time according to the format as specified by

<format>

. The

<format>

follows the rules as specified for the

\showdate

command with the exception that no

)

is allowed in the

<format>

.

**`$doxygenversion`**

will be replaced with the version of Doxygen

**`$projectname`**

will be replaced with the name of the project (see

PROJECT_NAME

)

**`$projectnumber`**

will be replaced with the project number (see

PROJECT_NUMBER

)

**`$projectbrief`**

will be replaced with the project brief description (see

PROJECT_BRIEF

)

**`$projectlogo`**

will be replaced with the project logo (see

PROJECT_LOGO

)

**`$latexdocumentpre`**

will be replaced by an output language dependent setting e.g. embed the entire document in a special environment (for Chinese, Japanese etc.) Commonly used together with

$latexdocumentpost

in the footer.

**`$latexdocumentpost`**

will be replaced by an output language dependent setting e.g. embed the entire document in a special environment (for Chinese, Japanese etc.) Commonly used together with

$latexdocumentpre

in the header.

**`$generatedby`**

will be replaced with the output language dependent version of the text "Generated by" or when the

TIMESTAMP

is set by the output language dependent version of the text "Generated on

$datetime

for

$projectname

by".

**`$latexcitereference`**

will be replaced by the output language dependent$ version of the word "Bibliography". This setting is typically used in combination with the block name

CITATIONS_PRESENT

.

**`$latexbibstyle`**

will be replaced with the latex bib style to be used as set by

LATEX_BIB_STYLE

, in case nothing is set the bib style

plain

is used. This setting is typically used in combination with the block name

CITATIONS_PRESENT

.

**`$latexbibfiles`**

will be replaced by the comma separated list of

bib

. files as set by

CITE_BIB_FILES

(when necessary a missing

.bib

is automatically added). This setting is typically used in combination with the block name

CITATIONS_PRESENT

.

**`$papertype`**

will be replaced by the paper type as set in

PAPER_TYPE

and the word "paper" is directly appended to it to have a correct

paper type.

**`$langISO`**

will be replaced by the ISO language name.

**`$languagesupport`**

will be replaced by an output language dependent setting of packages required for translating terms of the specified language.

**`$latexfontenc`**

will be replaced by an output language dependent setting of the fontencoding to be used. This setting is typically used in combination with the block name

LATEX_FONTENC

.

**`$latexfont`**

will be replaced by an output language dependent setting of the fonts to be used.

**`$latexemojidirectory`**

will be replaced by the directory as set in

LATEX_EMOJI_DIRECTORY

with the backslashes replaced by forward slashes (so usable by

). In case the

LATEX_EMOJI_DIRECTORY

is empty, the current directory will be used.

**`$makeindex`**

will be replaced by the command as set in

LATEX_MAKEINDEX_CMD

. Then the command doesn't start with a backslash, a backslash is automatically prepended. In case the setting is empty the command

\makeindex

is used.

**`$extralatexpackages`**

will be replaced by commands for using the packages set in

EXTRA_PACKAGES

.

**`$extralatexstylesheet`**

will be replaced by commands for using the packages set in

LATEX_EXTRA_STYLESHEET

(when the extension is the default extension,

.sty

, this extension is stripped for the package name).

**`$latexspecialformulachars`**

will be replaced by the code for some special unicode characters that are commonly used (i.e. superscript minus, superscript 2 and superscript 3)

**`$formulamacrofile`**

will be replaced by the name of the file as set in

FORMULA_MACROFILE

. This setting is typically used in combination with the block name

FORMULA_MACROFILE

.

To cope with differences in the layout of the header and footer that depend on configuration settings, the header and footer can also contain special blocks that will be copied to the output or skipped depending on the configuration. Such blocks have the following form:

```
 %%BEGIN BLOCKNAME
 Some context copied when condition BLOCKNAME holds
 %%END BLOCKNAME
 %%BEGIN !BLOCKNAME
 Some context copied when condition BLOCKNAME does not hold
 %%END !BLOCKNAME
```

The following block names are set based on the used settings in the configuration file:

**`COMPACT_LATEX`**

Content within this block is copied to the output when the

COMPACT_LATEX

option is enabled.

**`PDF_HYPERLINKS`**

Content within this block is copied to the output when the

PDF_HYPERLINKS

option is enabled.

**`USE_PDFLATEX`**

Content within this block is copied to the output when the

USE_PDFLATEX

option is enabled.

**`LATEX_BATCHMODE`**

Content within this block is copied to the output when the

LATEX_BATCHMODE

option is enabled.

**`TIMESTAMP`**

Content within this block is copied to the output when the

TIMESTAMP

option is enabled.

The following block names are set based on the fact whether or not the tag has a value in the used configuration file:

**`LATEX_FONTENC`**

Content within this block is copied to the output when the Doxygen latex translator function returns a value for the font encoding to be used. It is to be used in combination with the above mentioned

$latexfontenc

.

**`FORMULA_MACROFILE`**

Content within this block is copied to the output when the

FORMULA_MACROFILE

option is not empty. It is to be used in combination with the above mentioned

$formulamacrofile

.

The following block name is set based on whether or not a feature is used in the documentation:

**`CITATIONS_PRESENT`**

Content within this block is copied to the output when in the documentation citations are present and the relevant .. are present. It is to be used in combination with the above mentioned

$latexcitereference

,

$latexbibstyle

and

$latexbibfiles

.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_FOOTER`**

The `LATEX_FOOTER` tag can be used to specify a user-defined ($\mbox{\LaTeX}$) footer for the generated ($\mbox{\LaTeX}$) document. The footer should contain everything after the last chapter. If it is left blank Doxygen will generate a standard footer.

See LATEX_HEADER for more information on how to generate a default footer and what special commands can be used inside the footer.

See also section Doxygen usage for information on how to generate the default footer that Doxygen normally uses.

Note: Only use a user-defined footer if you know what you are doing!

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_EXTRA_STYLESHEET`**

The

LATEX_EXTRA_STYLESHEET

tag can be used to specify additional user-defined

style sheets that are included after the standard style sheets created by Doxygen. Using this option one can overrule certain style aspects. Doxygen will copy the style sheet files to the output directory.

**Note**

The order of the extra style sheet files is of importance (e.g. the last style sheet in the list overrules the setting of the previous ones in the list).

This tag requires that the tag

GENERATE_LATEX

is set to

YES

.

**`LATEX_EXTRA_FILES`**

The `LATEX_EXTRA_FILES` tag can be used to specify one or more extra images or other source files which should be copied to the LATEX_OUTPUT output directory. Note that the files will be copied as-is; there are no commands or markers available.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`PDF_HYPERLINKS`**

If the `PDF_HYPERLINKS` tag is set to `YES`, the ($\mbox{\LaTeX}$) that is generated is prepared for conversion to PDF (using `ps2pdf` or `pdflatex`). The PDF file will contain links (just like the HTML output) instead of page references. This makes the output suitable for online browsing using a PDF viewer.

The default value is: `YES`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`USE_PDFLATEX`**

If the `USE_PDFLATEX` tag is set to `YES`, Doxygen will use the engine as specified with LATEX_CMD_NAME to generate the PDF file directly from the ($\mbox{\LaTeX}$) files. Set this option to `YES`, to get a higher quality PDF documentation. See also section LATEX_CMD_NAME for selecting the engine.

The default value is: `YES`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_BATCHMODE`**

The `LATEX_BATCHMODE` tag signals the behavior of ($\mbox{\LaTeX}$) in case of an error.

Possible values are: `NO` same as ERROR_STOP, `YES` same as BATCH, `BATCH` In batch mode nothing is printed on the terminal, errors are scrolled as if <return> is hit at every error; missing files that TeX tries to input or request from keyboard input (\read on a not open input stream) cause the job to abort, `NON_STOP` In nonstop mode the diagnostic message will appear on the terminal, but there is no possibility of user interaction just like in batch mode, `SCROLL` In scroll mode, TeX will stop only for missing files to input or if keyboard input is necessary and `ERROR_STOP` In errorstop mode, TeX will stop at each error, asking for user intervention.

The default value is: `NO`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_HIDE_INDICES`**

If the `LATEX_HIDE_INDICES` tag is set to `YES` then Doxygen will not include the index chapters (such as File Index, Compound Index, etc.) in the output.

The default value is: `NO`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_BIB_STYLE`**

The `LATEX_BIB_STYLE` tag can be used to specify the style to use for the bibliography, e.g. `plainnat`, or `ieeetr`. See https://en.wikipedia.org/wiki/BibTeX and \cite for more info.

The default value is: `plainnat`.

This tag requires that the tag GENERATE_LATEX is set to `YES`.

**`LATEX_EMOJI_DIRECTORY`**

The `LATEX_EMOJI_DIRECTORY` tag is used to specify the (relative or absolute) path from which the emoji images will be read. If a relative path is entered, it will be relative to the LATEX_OUTPUT directory. If left blank the LATEX_OUTPUT directory will be used.

This tag requires that the tag GENERATE_LATEX is set to `YES`.


# Configuration options related to the RTF output

**`GENERATE_RTF`**

If the `GENERATE_RTF` tag is set to `YES`, Doxygen will generate RTF output. The RTF output is optimized for Word 97 and may not look too pretty with other RTF readers/editors.

The default value is: `NO`.

**`RTF_OUTPUT`**

The `RTF_OUTPUT` tag is used to specify where the RTF docs will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it.

The default directory is: `rtf`.

This tag requires that the tag GENERATE_RTF is set to `YES`.

**`COMPACT_RTF`**

If the `COMPACT_RTF` tag is set to `YES`, Doxygen generates more compact RTF documents. This may be useful for small projects and may help to save some trees in general.

The default value is: `NO`.

This tag requires that the tag GENERATE_RTF is set to `YES`.

**`RTF_HYPERLINKS`**

If the `RTF_HYPERLINKS` tag is set to `YES`, the RTF that is generated will contain hyperlink fields. The RTF file will contain links (just like the HTML output) instead of page references. This makes the output suitable for online browsing using Word or some other Word compatible readers that support those fields.

Note: WordPad (write) and others do not support links.

The default value is: `NO`.

This tag requires that the tag GENERATE_RTF is set to `YES`.

**`RTF_STYLESHEET_FILE`**

Load stylesheet definitions from file. Syntax is similar to Doxygen's configuration file, i.e. a series of assignments. You only have to provide replacements, missing definitions are set to their default value. See also section Doxygen usage for information on how to generate the default style sheet that Doxygen normally uses.

This tag requires that the tag GENERATE_RTF is set to `YES`.

**`RTF_EXTENSIONS_FILE`**

Set optional variables used in the generation of an RTF document. Syntax is similar to Doxygen's configuration file. A template extensions file can be generated using `doxygen -e rtf extensionFile`.

This tag requires that the tag GENERATE_RTF is set to `YES`.

**`RTF_EXTRA_FILES`**

The `RTF_EXTRA_FILES` tag can be used to specify one or more extra images or other source files which should be copied to the RTF_OUTPUT output directory. Note that the files will be copied as-is; there are no commands or markers available.

This tag requires that the tag GENERATE_RTF is set to `YES`.


# Configuration options related to the man page output

**`GENERATE_MAN`**

If the `GENERATE_MAN` tag is set to `YES`, Doxygen will generate man pages for classes and files.

The default value is: `NO`.

**`MAN_OUTPUT`**

The `MAN_OUTPUT` tag is used to specify where the man pages will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it. A directory `man3` will be created inside the directory specified by `MAN_OUTPUT`.

The default directory is: `man`.

This tag requires that the tag GENERATE_MAN is set to `YES`.

**`MAN_EXTENSION`**

The `MAN_EXTENSION` tag determines the extension that is added to the generated man pages. In case the manual section does not start with a number, the number 3 is prepended. The dot (.) at the beginning of the `MAN_EXTENSION` tag is optional.

The default value is: `.3`.

This tag requires that the tag GENERATE_MAN is set to `YES`.

**`MAN_SUBDIR`**

The `MAN_SUBDIR` tag determines the name of the directory created within `MAN_OUTPUT` in which the man pages are placed. If defaults to man followed by `MAN_EXTENSION` with the initial . removed.

This tag requires that the tag GENERATE_MAN is set to `YES`.

**`MAN_LINKS`**

If the `MAN_LINKS` tag is set to `YES` and Doxygen generates man output, then it will generate one additional man file for each entity documented in the real man page(s). These additional files only source the real man page, but without them the `man` command would be unable to find the correct page.

The default value is: `NO`.

This tag requires that the tag GENERATE_MAN is set to `YES`.


# Configuration options related to the XML output

**`GENERATE_XML`**

If the `GENERATE_XML` tag is set to `YES`, Doxygen will generate an XML file that captures the structure of the code including all documentation.

The default value is: `NO`.

**`XML_OUTPUT`**

The `XML_OUTPUT` tag is used to specify where the XML pages will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it.

The default directory is: `xml`.

This tag requires that the tag GENERATE_XML is set to `YES`.

**`XML_PROGRAMLISTING`**

If the `XML_PROGRAMLISTING` tag is set to `YES`, Doxygen will dump the program listings (including syntax highlighting and cross-referencing information) to the XML output. Note that enabling this will significantly increase the size of the XML output.

The default value is: `YES`.

This tag requires that the tag GENERATE_XML is set to `YES`.

**`XML_NS_MEMB_FILE_SCOPE`**

If the `XML_NS_MEMB_FILE_SCOPE` tag is set to `YES`, Doxygen will include namespace members in file scope as well, matching the HTML output.

The default value is: `NO`.

This tag requires that the tag GENERATE_XML is set to `YES`.


# Configuration options related to the DOCBOOK output

**`GENERATE_DOCBOOK`**

If the `GENERATE_DOCBOOK` tag is set to `YES`, Doxygen will generate Docbook files that can be used to generate PDF.

The default value is: `NO`.

**`DOCBOOK_OUTPUT`**

The `DOCBOOK_OUTPUT` tag is used to specify where the Docbook pages will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it.

The default directory is: `docbook`.

This tag requires that the tag GENERATE_DOCBOOK is set to `YES`.


# Configuration options for the AutoGen Definitions output

**`GENERATE_AUTOGEN_DEF`**

If the `GENERATE_AUTOGEN_DEF` tag is set to `YES`, Doxygen will generate an AutoGen Definitions (see https://autogen.sourceforge.net/) file that captures the structure of the code including all documentation. Note that this feature is still experimental and incomplete at the moment.

The default value is: `NO`.


# Configuration options related to Sqlite3 output

**`GENERATE_SQLITE3`**

If the `GENERATE_SQLITE3` tag is set to `YES` Doxygen will generate a `Sqlite3` database with symbols found by Doxygen stored in tables.

The default value is: `NO`.

**`SQLITE3_OUTPUT`**

The `SQLITE3_OUTPUT` tag is used to specify where the `Sqlite3` database will be put. If a relative path is entered the value of OUTPUT_DIRECTORY will be put in front of it.

The default directory is: `sqlite3`.

This tag requires that the tag GENERATE_SQLITE3 is set to `YES`.

**`SQLITE3_RECREATE_DB`**

The `SQLITE3_RECREATE_DB` tag is set to `YES`, the existing doxygen_sqlite3.db database file will be recreated with each Doxygen run. If set to `NO`, Doxygen will warn if a database file is already found and not modify it.

The default value is: `YES`.

This tag requires that the tag GENERATE_SQLITE3 is set to `YES`.


# Configuration options related to the Perl module output

**`GENERATE_PERLMOD`**

If the `GENERATE_PERLMOD` tag is set to `YES`, Doxygen will generate a Perl module file that captures the structure of the code including all documentation. Note that this feature is still experimental and incomplete at the moment.

The default value is: `NO`.

**`PERLMOD_LATEX`**

If the `PERLMOD_LATEX` tag is set to `YES`, Doxygen will generate the necessary `Makefile` rules, `Perl` scripts and ($\mbox{\LaTeX}$) code to be able to generate PDF and DVI output from the Perl module output.

The default value is: `NO`.

This tag requires that the tag GENERATE_PERLMOD is set to `YES`.

**`PERLMOD_PRETTY`**

If the `PERLMOD_PRETTY` tag is set to `YES`, the Perl module output will be nicely formatted so it can be parsed by a human reader. This is useful if you want to understand what is going on. On the other hand, if this tag is set to `NO`, the size of the Perl module output will be much smaller and Perl will parse it just the same.

The default value is: `YES`.

This tag requires that the tag GENERATE_PERLMOD is set to `YES`.

**`PERLMOD_MAKEVAR_PREFIX`**

The names of the make variables in the generated doxyrules.make file are prefixed with the string contained in `PERLMOD_MAKEVAR_PREFIX`. This is useful so different doxyrules.make files included by the same Makefile don't overwrite each other's variables.

This tag requires that the tag GENERATE_PERLMOD is set to `YES`.


# Configuration options related to the preprocessor

**`ENABLE_PREPROCESSING`**

If the `ENABLE_PREPROCESSING` tag is set to `YES`, Doxygen will evaluate all C-preprocessor directives found in the sources and include files.

The default value is: `YES`.

**`MACRO_EXPANSION`**

If the `MACRO_EXPANSION` tag is set to `YES`, Doxygen will expand all macro names in the source code. If set to `NO`, only conditional compilation will be performed. Macro expansion can be done in a controlled way by setting EXPAND_ONLY_PREDEF to `YES`.

The default value is: `NO`.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`EXPAND_ONLY_PREDEF`**

If the `EXPAND_ONLY_PREDEF` and MACRO_EXPANSION tags are both set to `YES` then the macro expansion is limited to the macros specified with the PREDEFINED and EXPAND_AS_DEFINED tags.

The default value is: `NO`.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`SEARCH_INCLUDES`**

If the `SEARCH_INCLUDES` tag is set to `YES`, the include files in the INCLUDE_PATH will be searched if a `#include` is found.

The default value is: `YES`.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`INCLUDE_PATH`**

The `INCLUDE_PATH` tag can be used to specify one or more directories that contain include files that are not input files but should be processed by the preprocessor.

Note that the `INCLUDE_PATH` is not recursive, so the setting of RECURSIVE has no effect here.

This tag requires that the tag SEARCH_INCLUDES is set to `YES`.

**`INCLUDE_FILE_PATTERNS`**

You can use the `INCLUDE_FILE_PATTERNS` tag to specify one or more wildcard patterns (like *.h and *.hpp) to filter out the header-files in the directories. If left blank, the patterns specified with FILE_PATTERNS will be used.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`PREDEFINED`**

The `PREDEFINED` tag can be used to specify one or more macro names that are defined before the preprocessor is started (similar to the -D option of e.g. `gcc`). The argument of the tag is a list of macros of the form: `name` or `name=definition` (no spaces). If the definition and the `"="` are omitted, `"=1"` is assumed. To prevent a macro definition from being undefined via `#undef` or recursively expanded use the `:=` operator instead of the `=` operator.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`EXPAND_AS_DEFINED`**

If the MACRO_EXPANSION and EXPAND_ONLY_PREDEF tags are set to `YES` then this tag can be used to specify a list of macro names that should be expanded. The macro definition that is found in the sources will be used. Use the PREDEFINED tag if you want to use a different macro definition that overrules the definition found in the source code.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.

**`SKIP_FUNCTION_MACROS`**

If the `SKIP_FUNCTION_MACROS` tag is set to `YES` then Doxygen's preprocessor will remove all references to function-like macros that are alone on a line, have an all uppercase name, and do not end with a semicolon. Such function macros are typically used for boiler-plate code, and will confuse the parser if not removed.

The default value is: `YES`.

This tag requires that the tag ENABLE_PREPROCESSING is set to `YES`.


# Configuration options related to external references

**`TAGFILES`**

The `TAGFILES` tag can be used to specify one or more tag files.

For each tag file the location of the external documentation should be added. The format of a tag file without this location is as follows:

```
  TAGFILES = file1 file2 ...
```

Adding location for the tag files is done as follows:

```
  TAGFILES = file1=loc1 "file2 = loc2" ...
```

where loc1 and loc2 can be relative or absolute paths or URLs. See the section Linking to external documentation for more information about the use of tag files.

**Note**

Each tag file must have a unique name (where the name does

NOT

include the path). If a tag file is not located in the directory in which Doxygen is run, you must also specify the path to the tagfile here.

**`GENERATE_TAGFILE`**

When a file name is specified after `GENERATE_TAGFILE`, Doxygen will create a tag file that is based on the input files it reads. See section Linking to external documentation for more information about the usage of tag files.

**`ALLEXTERNALS`**

If the `ALLEXTERNALS` tag is set to `YES`, all external classes and namespaces will be listed in the class and namespace index. If set to `NO`, only the inherited external classes will be listed.

The default value is: `NO`.

**`EXTERNAL_GROUPS`**

If the `EXTERNAL_GROUPS` tag is set to `YES`, all external groups will be listed in the topic index. If set to `NO`, only the current project's groups will be listed.

The default value is: `YES`.

**`EXTERNAL_PAGES`**

If the `EXTERNAL_PAGES` tag is set to `YES`, all external pages will be listed in the related pages index. If set to `NO`, only the current project's pages will be listed.

The default value is: `YES`.
