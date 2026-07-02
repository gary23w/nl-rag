---
title: "Doxygen: Configuration (part 1/5)"
source: https://www.doxygen.nl/manual/config.html
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
part: 1/5
---

# Format

A configuration file is a free-form ASCII text file with a structure that is similar to that of a `Makefile`, with the default name `Doxyfile`. It is parsed by `doxygen`. The file may contain tabs and newlines for formatting purposes. The statements in the file are case-sensitive.

The configuration file essentially consists of a list of assignment statements. Each statement consists of a `TAG_NAME` written in capitals, followed by the equal sign (`=`) and one or more values. If the same tag is assigned more than once, the last assignment overwrites any earlier assignment. For tags that take a list as their argument, the `+=` operator can be used instead of `=` to append new values to the list. Values are sequences of non-blanks. If the value should contain one or more blanks it must be surrounded by quotes (`"..."`). Multiple lines can be concatenated by inserting a backslash (`\`) as the last non-whitespace character of a line.

Comments begin with the hash character (`#`) and end at the end of the line. Comments may be placed anywhere within the file (except within quotes). Comments beginning with two hash characters (`##`) are kept while updating the configuration file when they are placed in front of a `TAG_NAME`, or at the beginning or end of the configuration file.

Environment variables can be expanded using the pattern `$(ENV_VARIABLE_NAME)`. A small example:

```
DOT_PATH      = $(YOUR_DOT_PATH)
```

You can also include part of a configuration file from another configuration file using a `@INCLUDE` tag as follows:

```
@INCLUDE = config_file_name
```

The include file is searched in the current working directory. You can also specify a list of directories that should be searched before looking in the current working directory. Do this by putting a `@INCLUDE_PATH` tag with these paths before the `@INCLUDE` tag, e.g.:

```
@INCLUDE_PATH = my_config_dir
```

The configuration options can be divided into several categories. Below is an alphabetical index of the tags that are recognized followed by the descriptions of the tags grouped by category.

- ABBREVIATE_BRIEF
- ALIASES
- ALLEXTERNALS
- ALLOW_UNICODE_NAMES
- ALPHABETICAL_INDEX
- ALWAYS_DETAILED_SEC
- AUTOLINK_IGNORE_WORDS
- AUTOLINK_SUPPORT
- BINARY_TOC
- BRIEF_MEMBER_DESC
- BUILTIN_STL_SUPPORT
- CALLER_GRAPH
- CALL_GRAPH
- CASE_SENSE_NAMES
- CHM_FILE
- CHM_INDEX_ENCODING
- CITE_BIB_FILES
- CLANG_ADD_INC_PATHS
- CLANG_ASSISTED_PARSING
- CLANG_DATABASE_PATH
- CLANG_OPTIONS
- CLASS_GRAPH
- COLLABORATION_GRAPH
- COMPACT_LATEX
- COMPACT_RTF
- CPP_CLI_SUPPORT
- CREATE_SUBDIRS
- CREATE_SUBDIRS_LEVEL
- DIAFILE_DIRS
- DIA_PATH
- DIRECTORY_GRAPH
- DIR_GRAPH_MAX_DEPTH
- DISABLE_INDEX
- DISTRIBUTE_GROUP_DOC
- DOCBOOK_OUTPUT
- DOCSET_BUNDLE_ID
- DOCSET_FEEDNAME
- DOCSET_FEEDURL
- DOCSET_PUBLISHER_ID
- DOCSET_PUBLISHER_NAME
- DOTFILE_DIRS
- DOT_BATCH_SIZE
- DOT_CLEANUP
- DOT_COMMON_ATTR
- DOT_EDGE_ATTR
- DOT_FONTPATH
- DOT_GRAPH_MAX_NODES
- DOT_IMAGE_FORMAT
- DOT_NODE_ATTR
- DOT_NUM_THREADS
- DOT_PATH
- DOT_UML_DETAILS
- DOT_WRAP_THRESHOLD
- DOXYFILE_ENCODING
- ECLIPSE_DOC_ID
- ENABLED_SECTIONS
- ENABLE_PREPROCESSING
- ENUM_VALUES_PER_LINE
- EXAMPLE_PATH
- EXAMPLE_PATTERNS
- EXAMPLE_RECURSIVE
- EXCLUDE
- EXCLUDE_PATTERNS
- EXCLUDE_SYMBOLS
- EXCLUDE_SYMLINKS
- EXPAND_AS_DEFINED
- EXPAND_ONLY_PREDEF
- EXTENSION_MAPPING
- EXTERNAL_GROUPS
- EXTERNAL_PAGES
- EXTERNAL_SEARCH
- EXTERNAL_SEARCH_ID
- EXTERNAL_TOOL_PATH
- EXTRACT_ALL
- EXTRACT_ANON_NSPACES
- EXTRACT_LOCAL_CLASSES
- EXTRACT_LOCAL_METHODS
- EXTRACT_PACKAGE
- EXTRACT_PRIVATE
- EXTRACT_PRIV_VIRTUAL
- EXTRACT_STATIC
- EXTRA_PACKAGES
- EXTRA_SEARCH_MAPPINGS
- EXT_LINKS_IN_WINDOW
- FILE_PATTERNS
- FILE_VERSION_FILTER
- FILTER_PATTERNS
- FILTER_SOURCE_FILES
- FILTER_SOURCE_PATTERNS
- FORCE_LOCAL_INCLUDES
- FORMULA_FONTSIZE
- FORMULA_MACROFILE
- FORTRAN_COMMENT_AFTER
- FULL_PATH_NAMES
- FULL_SIDEBAR
- GENERATE_AUTOGEN_DEF
- GENERATE_BUGLIST
- GENERATE_CHI
- GENERATE_DEPRECATEDLIST
- GENERATE_DOCBOOK
- GENERATE_DOCSET
- GENERATE_ECLIPSEHELP
- GENERATE_HTML
- GENERATE_HTMLHELP
- GENERATE_LATEX
- GENERATE_LEGEND
- GENERATE_MAN
- GENERATE_PERLMOD
- GENERATE_QHP
- GENERATE_REQUIREMENTS
- GENERATE_RTF
- GENERATE_SQLITE3
- GENERATE_TAGFILE
- GENERATE_TESTLIST
- GENERATE_TODOLIST
- GENERATE_TREEVIEW
- GENERATE_XML
- GRAPHICAL_HIERARCHY
- GROUP_GRAPHS
- GROUP_NESTED_COMPOUNDS
- HAVE_DOT
- HHC_LOCATION
- HIDE_COMPOUND_REFERENCE
- HIDE_FRIEND_COMPOUNDS
- HIDE_IN_BODY_DOCS
- HIDE_SCOPE_NAMES
- HIDE_UNDOC_CLASSES
- HIDE_UNDOC_MEMBERS
- HIDE_UNDOC_NAMESPACES
- HIDE_UNDOC_RELATIONS
- HTML_CODE_FOLDING
- HTML_COLORSTYLE
- HTML_COLORSTYLE_GAMMA
- HTML_COLORSTYLE_HUE
- HTML_COLORSTYLE_SAT
- HTML_COPY_CLIPBOARD
- HTML_DYNAMIC_MENUS
- HTML_DYNAMIC_SECTIONS
- HTML_EXTRA_FILES
- HTML_EXTRA_STYLESHEET
- HTML_FILE_EXTENSION
- HTML_FOOTER
- HTML_FORMULA_FORMAT
- HTML_HEADER
- HTML_INDEX_NUM_ENTRIES
- HTML_OUTPUT
- HTML_PROJECT_COOKIE
- HTML_STYLESHEET
- IDL_PROPERTY_SUPPORT
- IGNORE_PREFIX
- IMAGE_PATH
- IMPLICIT_DIR_DOCS
- INCLUDED_BY_GRAPH
- INCLUDE_FILE_PATTERNS
- INCLUDE_GRAPH
- INCLUDE_PATH
- INHERIT_DOCS
- INLINE_GROUPED_CLASSES
- INLINE_INFO
- INLINE_INHERITED_MEMB
- INLINE_SIMPLE_STRUCTS
- INLINE_SOURCES
- INPUT
- INPUT_ENCODING
- INPUT_FILE_ENCODING
- INPUT_FILTER
- INTERACTIVE_SVG
- INTERNAL_DOCS
- JAVADOC_AUTOBRIEF
- JAVADOC_BANNER
- LATEX_BATCHMODE
- LATEX_BIB_STYLE
- LATEX_CMD_NAME
- LATEX_EMOJI_DIRECTORY
- LATEX_EXTRA_FILES
- LATEX_EXTRA_STYLESHEET
- LATEX_FOOTER
- LATEX_HEADER
- LATEX_HIDE_INDICES
- LATEX_MAKEINDEX_CMD
- LATEX_OUTPUT
- LAYOUT_FILE
- LOOKUP_CACHE_SIZE
- MACRO_EXPANSION
- MAKEINDEX_CMD_NAME
- MAN_EXTENSION
- MAN_LINKS
- MAN_OUTPUT
- MAN_SUBDIR
- MARKDOWN_ID_STYLE
- MARKDOWN_STRICT
- MARKDOWN_SUPPORT
- MATHJAX_CODEFILE
- MATHJAX_EXTENSIONS
- MATHJAX_FORMAT
- MATHJAX_RELPATH
- MATHJAX_VERSION
- MAX_DOT_GRAPH_DEPTH
- MAX_INITIALIZER_LINES
- MERMAIDFILE_DIRS
- MERMAID_CONFIG_FILE
- MERMAID_JS_URL
- MERMAID_PATH
- MERMAID_RENDER_MODE
- MSCFILE_DIRS
- MSCGEN_TOOL
- MULTILINE_CPP_IS_BRIEF
- NUM_PROC_THREADS
- OBFUSCATE_EMAILS
- OPTIMIZE_FOR_FORTRAN
- OPTIMIZE_OUTPUT_FOR_C
- OPTIMIZE_OUTPUT_JAVA
- OPTIMIZE_OUTPUT_SLICE
- OPTIMIZE_OUTPUT_VHDL
- OUTPUT_DIRECTORY
- OUTPUT_LANGUAGE
- PAGE_OUTLINE_PANEL
- PAPER_TYPE
- PDF_HYPERLINKS
- PERLMOD_LATEX
- PERLMOD_MAKEVAR_PREFIX
- PERLMOD_PRETTY
- PLANTUMLFILE_DIRS
- PLANTUML_CFG_FILE
- PLANTUML_INCLUDE_PATH
- PLANTUML_JAR_PATH
- PREDEFINED
- PROJECT_BRIEF
- PROJECT_ICON
- PROJECT_LOGO
- PROJECT_NAME
- PROJECT_NUMBER
- PYTHON_DOCSTRING
- QCH_FILE
- QHG_LOCATION
- QHP_CUST_FILTER_ATTRS
- QHP_CUST_FILTER_NAME
- QHP_NAMESPACE
- QHP_SECT_FILTER_ATTRS
- QHP_VIRTUAL_FOLDER
- QT_AUTOBRIEF
- QUIET
- RECURSIVE
- REFERENCED_BY_RELATION
- REFERENCES_LINK_SOURCE
- REFERENCES_RELATION
- REPEAT_BRIEF
- REQ_TRACEABILITY_INFO
- RESOLVE_UNNAMED_PARAMS
- RTF_EXTENSIONS_FILE
- RTF_EXTRA_FILES
- RTF_HYPERLINKS
- RTF_OUTPUT
- RTF_STYLESHEET_FILE
- SEARCHDATA_FILE
- SEARCHENGINE
- SEARCHENGINE_URL
- SEARCH_INCLUDES
- SEPARATE_MEMBER_PAGES
- SERVER_BASED_SEARCH
- SHORT_NAMES
- SHOW_ENUM_VALUES
- SHOW_FILES
- SHOW_GROUPED_MEMB_INC
- SHOW_HEADERFILE
- SHOW_INCLUDE_FILES
- SHOW_NAMESPACES
- SHOW_USED_FILES
- SIP_SUPPORT
- SITEMAP_URL
- SKIP_FUNCTION_MACROS
- SORT_BRIEF_DOCS
- SORT_BY_SCOPE_NAME
- SORT_GROUP_NAMES
- SORT_MEMBERS_CTORS_1ST
- SORT_MEMBER_DOCS
- SOURCE_BROWSER
- SOURCE_TOOLTIPS
- SQLITE3_OUTPUT
- SQLITE3_RECREATE_DB
- STRICT_PROTO_MATCHING
- STRIP_CODE_COMMENTS
- STRIP_FROM_INC_PATH
- STRIP_FROM_PATH
- SUBGROUPING
- TAB_SIZE
- TAGFILES
- TEMPLATE_RELATIONS
- TIMESTAMP
- TOC_EXPAND
- TOC_INCLUDE_HEADINGS
- TREEVIEW_WIDTH
- TYPEDEF_HIDES_STRUCT
- UML_LIMIT_NUM_FIELDS
- UML_LOOK
- UML_MAX_EDGE_LABELS
- USE_HTAGS
- USE_MATHJAX
- USE_MDFILE_AS_MAINPAGE
- USE_PDFLATEX
- VERBATIM_HEADERS
- WARNINGS
- WARN_AS_ERROR
- WARN_FORMAT
- WARN_IF_DOC_ERROR
- WARN_IF_INCOMPLETE_DOC
- WARN_IF_UNDOCUMENTED
- WARN_IF_UNDOC_ENUM_VAL
- WARN_LAYOUT_FILE
- WARN_LINE_FORMAT
- WARN_LOGFILE
- WARN_NO_PARAMDOC
- XML_NS_MEMB_FILE_SCOPE
- XML_OUTPUT
- XML_PROGRAMLISTING


# Project related configuration options

**`DOXYFILE_ENCODING`**

This tag specifies the encoding used for all characters in the configuration file that follow. The default is UTF-8 which is also the encoding used for all text before the first occurrence of this tag. Doxygen uses `libiconv` (or the iconv built into `libc`) for the transcoding. See https://www.gnu.org/software/libiconv/ for the list of possible encodings.

The default value is: `UTF-8`.

**`PROJECT_NAME`**

The `PROJECT_NAME` tag is a single word (or a sequence of words surrounded by double-quotes, unless you are using Doxywizard) that should identify the project for which the documentation is generated. This name is used in the title of most generated pages and in a few other places.

The default value is: `My Project`.

**`PROJECT_NUMBER`**

The `PROJECT_NUMBER` tag can be used to enter a project or revision number. This could be handy for archiving the generated documentation or if some version control system is used.

**`PROJECT_BRIEF`**

Using the `PROJECT_BRIEF` tag one can provide an optional one line description for a project that appears at the top of each page and should give viewers a quick idea about the purpose of the project. Keep the description short.

**`PROJECT_LOGO`**

With the `PROJECT_LOGO` tag one can specify a logo or an icon that is included in the documentation. The maximum height of the logo should not exceed 55 pixels and the maximum width should not exceed 200 pixels. Doxygen will copy the logo to the output directory.

**`PROJECT_ICON`**

With the `PROJECT_ICON` tag one can specify an icon that is included in the tabs when the HTML document is shown. Doxygen will copy the logo to the output directory.

**`OUTPUT_DIRECTORY`**

The `OUTPUT_DIRECTORY` tag is used to specify the (relative or absolute) path into which the generated documentation will be written. If a relative path is entered, it will be relative to the location where Doxygen was started. If left blank the current directory will be used.

**`CREATE_SUBDIRS`**

If the `CREATE_SUBDIRS` tag is set to `YES` then Doxygen will create up to 4096 sub-directories (in 2 levels) under the output directory of each output format and will distribute the generated files over these directories. Enabling this option can be useful when feeding Doxygen a huge amount of source files, where putting all generated files in the same directory would otherwise cause performance problems for the file system. Adjust `CREATE_SUBDIRS_LEVEL` to control the number of sub-directories.

The default value is: `NO`.

**`CREATE_SUBDIRS_LEVEL`**

Controls the number of sub-directories that will be created when `CREATE_SUBDIRS` tag is set to `YES`. Level 0 represents 16 directories, and every level increment doubles the number of directories, resulting in 4096 directories at level 8 which is the default and also the maximum value. The sub-directories are organized in 2 levels, the first level always has a fixed number of 16 directories.

Minimum value: `0`, maximum value: `8`, default value: `8`.

This tag requires that the tag CREATE_SUBDIRS is set to `YES`.

**`ALLOW_UNICODE_NAMES`**

If the `ALLOW_UNICODE_NAMES` tag is set to `YES`, Doxygen will allow non-ASCII characters to appear in the names of generated files. If set to `NO`, non-ASCII characters will be escaped, for example _xE3_x81_x84 will be used for Unicode U+3044.

The default value is: `NO`.

**`OUTPUT_LANGUAGE`**

The `OUTPUT_LANGUAGE` tag is used to specify the language in which all documentation generated by Doxygen is written. Doxygen will use this information to generate all constant output in the proper language.

Possible values are: `Afrikaans`, `Arabic`, `Armenian`, `Brazilian`, `Bulgarian`, `Catalan`, `Chinese`, `Chinese-Traditional`, `Croatian`, `Czech`, `Danish`, `Dutch`, `English` (United States), `Esperanto`, `Farsi` (Persian), `Finnish`, `French`, `German`, `Greek`, `Hindi`, `Hungarian`, `Indonesian`, `Italian`, `Japanese`, `Japanese-en` (Japanese with English messages), `Korean`, `Korean-en` (Korean with English messages), `Latvian`, `Lithuanian`, `Macedonian`, `Norwegian`, `Persian` (Farsi), `Polish`, `Portuguese`, `Romanian`, `Russian`, `Serbian`, `Serbian-Cyrillic`, `Slovak`, `Slovene`, `Spanish`, `Swedish`, `Turkish`, `Ukrainian` and `Vietnamese`.

The default value is: `English`.

**`BRIEF_MEMBER_DESC`**

If the `BRIEF_MEMBER_DESC` tag is set to `YES`, Doxygen will include brief member descriptions after the members that are listed in the file and class documentation (similar to `Javadoc`). Set to `NO` to disable this.

The default value is: `YES`.

**`REPEAT_BRIEF`**

If the `REPEAT_BRIEF` tag is set to `YES`, Doxygen will prepend the brief description of a member or function before the detailed description Note: If both HIDE_UNDOC_MEMBERS and BRIEF_MEMBER_DESC are set to `NO`, the brief descriptions will be completely suppressed.

The default value is: `YES`.

**`ABBREVIATE_BRIEF`**

This tag implements a quasi-intelligent brief description abbreviator that is used to form the text in various listings. Each string in this list, if found as the leading text of the brief description, will be stripped from the text and the result, after processing the whole list, is used as the annotated text. Otherwise, the brief description is used as-is. If left blank, the following values are used ($name is automatically replaced with the name of the entity): `The $name class`, `The $name widget`, `The $name file`, `is`, `provides`, `specifies`, `contains`, `represents`, `a`, `an` and `the`.

**`ALWAYS_DETAILED_SEC`**

If the `ALWAYS_DETAILED_SEC` and REPEAT_BRIEF tags are both set to `YES` then Doxygen will generate a detailed section even if there is only a brief description.

The default value is: `NO`.

**`INLINE_INHERITED_MEMB`**

If the `INLINE_INHERITED_MEMB` tag is set to `YES`, Doxygen will show all inherited members of a class in the documentation of that class as if those members were ordinary class members. Constructors, destructors and assignment operators of the base classes will not be shown.

The default value is: `NO`.

**`FULL_PATH_NAMES`**

If the `FULL_PATH_NAMES` tag is set to `YES`, Doxygen will prepend the full path before files name in the file list and in the header files. If set to `NO` the shortest path that makes the file name unique will be used

The default value is: `YES`.

**`STRIP_FROM_PATH`**

The `STRIP_FROM_PATH` tag can be used to strip a user-defined part of the path. Stripping is only done if one of the specified strings matches the left-hand part of the path. The tag can be used to show relative paths in the file list. If left blank the directory from which Doxygen is run is used as the path to strip. Note that you can specify absolute paths here, but also relative paths, which will be relative from the directory where Doxygen is started.

This tag requires that the tag FULL_PATH_NAMES is set to `YES`.

**`STRIP_FROM_INC_PATH`**

The `STRIP_FROM_INC_PATH` tag can be used to strip a user-defined part of the path mentioned in the documentation of a class, which tells the reader which header file to include in order to use a class. If left blank only the name of the header file containing the class definition is used. Otherwise one should specify the list of include paths that are normally passed to the compiler using the -I flag.

**`SHORT_NAMES`**

If the `SHORT_NAMES` tag is set to `YES`, Doxygen will generate much shorter (but less readable) file names. This can be useful if your file system doesn't support long names like on DOS, Mac, or CD-ROM.

The default value is: `NO`.

**`JAVADOC_AUTOBRIEF`**

If the `JAVADOC_AUTOBRIEF` tag is set to `YES` then Doxygen will interpret the first line (until the first dot, question mark or exclamation mark) of a Javadoc-style comment as the brief description. If set to `NO`, the Javadoc-style will behave just like regular Qt-style comments (thus requiring an explicit @brief command for a brief description.)

The default value is: `NO`.

**`JAVADOC_BANNER`**

If the `JAVADOC_BANNER` tag is set to `YES` then Doxygen will interpret a line such as

```
/***************
```

as being the beginning of a Javadoc-style comment "banner". If set to `NO`, the Javadoc-style will behave just like regular comments and it will not be interpreted by Doxygen.

The default value is: `NO`.

**`QT_AUTOBRIEF`**

If the `QT_AUTOBRIEF` tag is set to `YES` then Doxygen will interpret the first line (until the first dot, question mark or exclamation mark) of a Qt-style comment as the brief description. If set to `NO`, the Qt-style will behave just like regular Qt-style comments (thus requiring an explicit \brief command for a brief description.)

The default value is: `NO`.

**`MULTILINE_CPP_IS_BRIEF`**

The `MULTILINE_CPP_IS_BRIEF` tag can be set to `YES` to make Doxygen treat a multi-line C++ special comment block (i.e. a block of `//!` or `///` comments) as a brief description. This used to be the default behavior. The new default is to treat a multi-line C++ comment block as a detailed description. Set this tag to `YES` if you prefer the old behavior instead. Note that setting this tag to `YES` also means that rational rose comments are not recognized any more.

The default value is: `NO`.

**`PYTHON_DOCSTRING`**

By default Python docstrings are displayed as preformatted text and Doxygen's special commands cannot be used. By setting `PYTHON_DOCSTRING` to `NO` the Doxygen's special commands can be used and the contents of the docstring documentation blocks is shown as Doxygen documentation.

The default value is: `YES`.

**`INHERIT_DOCS`**

If the `INHERIT_DOCS` tag is set to `YES` then an undocumented member inherits the documentation from any documented member that it re-implements.

The default value is: `YES`.

**`SEPARATE_MEMBER_PAGES`**

If the `SEPARATE_MEMBER_PAGES` tag is set to `YES` then Doxygen will produce a new page for each member. If set to `NO`, the documentation of a member will be part of the file/class/namespace that contains it.

The default value is: `NO`.

**`TAB_SIZE`**

The `TAB_SIZE` tag can be used to set the number of spaces in a tab. Doxygen uses this value to replace tabs by spaces in code fragments.

Minimum value: `1`, maximum value: `16`, default value: `4`.

**`ALIASES`**

This tag can be used to specify a number of aliases that act as commands in the documentation. An alias has the form:

```
 name=value
```

For example adding

```
 "sideeffect=@par Side Effects:^^"
```

will allow you to put the command `\sideeffect` (or `@sideeffect`) in the documentation, which will result in a user-defined paragraph with heading "Side Effects:". Note that you cannot put \n's in the value part of an alias to insert newlines (in the resulting output). You can put ^^ in the value part of an alias to insert a newline as if a physical newline was in the original file. When you need a literal { or } or , in the value part of an alias you have to escape them by means of a backslash (\\endiskip), this can lead to conflicts with the commands `\{` and `\}` for these it is advised to use the version `@{` and `@}` or use a double escape (`\\{` and `\\}`)

**`OPTIMIZE_OUTPUT_FOR_C`**

Set the `OPTIMIZE_OUTPUT_FOR_C` tag to `YES` if your project consists of C sources only. Doxygen will then generate output that is more tailored for C. For instance, some of the names that are used will be different. The list of all members will be omitted, etc.

The default value is: `NO`.

**`OPTIMIZE_OUTPUT_JAVA`**

Set the `OPTIMIZE_OUTPUT_JAVA` tag to `YES` if your project consists of Java or Python sources only. Doxygen will then generate output that is more tailored for that language. For instance, namespaces will be presented as packages, qualified scopes will look different, etc.

The default value is: `NO`.

**`OPTIMIZE_FOR_FORTRAN`**

Set the `OPTIMIZE_FOR_FORTRAN` tag to `YES` if your project consists of Fortran sources. Doxygen will then generate output that is tailored for Fortran.

The default value is: `NO`.

**`OPTIMIZE_OUTPUT_VHDL`**

Set the `OPTIMIZE_OUTPUT_VHDL` tag to `YES` if your project consists of VHDL sources. Doxygen will then generate output that is tailored for VHDL.

The default value is: `NO`.

**`OPTIMIZE_OUTPUT_SLICE`**

Set the `OPTIMIZE_OUTPUT_SLICE` tag to `YES` if your project consists of Slice sources only. Doxygen will then generate output that is more tailored for that language. For instance, namespaces will be presented as modules, types will be separated into more groups, etc.

The default value is: `NO`.

**`EXTENSION_MAPPING`**

Doxygen selects the parser to use depending on the extension of the files it parses. With this tag you can assign which parser to use for a given extension. Doxygen has a built-in mapping, but you can override or extend it using this tag. The format is `ext=language`, where `ext` is a file extension, and language is one of the parsers supported by Doxygen: IDL, Java, JavaScript, Csharp (C#), C, C++, Lex, D, PHP, md (Markdown), Objective-C, Python, Slice, VHDL, Fortran (fixed format Fortran: FortranFixed, free formatted Fortran: FortranFree, unknown formatted Fortran: Fortran. In the later case the parser tries to guess whether the code is fixed or free formatted code, this is the default for Fortran type files).

For instance to make Doxygen treat `.inc` files as Fortran files (default is PHP), and `.f` files as C (default is Fortran), use: inc=Fortran f=C.

Note: For files without extension you can use no_extension as a placeholder. Note that for custom extensions you also need to set FILE_PATTERNS otherwise the files are not read by Doxygen. When specifying no_extension you should add * to the FILE_PATTERNS. Note see also the list of default file extension mappings.

**`MARKDOWN_SUPPORT`**

If the `MARKDOWN_SUPPORT` tag is enabled then Doxygen pre-processes all comments according to the Markdown format, which allows for more readable documentation. See https://daringfireball.net/projects/markdown/ for details. The output of markdown processing is further processed by Doxygen, so you can mix Doxygen, HTML, and XML commands with Markdown formatting. Disable only in case of backward compatibilities issues.

The default value is: `YES`.

**`MARKDOWN_STRICT`**

If the `MARKDOWN_STRICT` tag is enabled then Doxygen treats text in comments as Markdown formatted also in cases where Doxygen's native markup format conflicts with that of Markdown. This is only relevant in cases where backticks are used. Doxygen's native markup style allows a single quote to end a text fragment started with a backtick and then treat it as a piece of quoted text, whereas in Markdown such text fragment is treated as verbatim and only ends when a second matching backtick is found. Also, Doxygen's native markup format requires double quotes to be escaped when they appear in a backtick section, whereas this is not needed for Markdown.

The default value is: `YES`.

This tag requires that the tag MARKDOWN_SUPPORT is set to `YES`.

**`TOC_INCLUDE_HEADINGS`**

When the `TOC_INCLUDE_HEADINGS` tag is set to a non-zero value, all headings up to that level are automatically included in the table of contents, even if they do not have an id attribute.

**Note**

This feature currently applies only to Markdown headings.

Minimum value: `0`, maximum value: `99`, default value: `6`.

This tag requires that the tag MARKDOWN_SUPPORT is set to `YES`.

**`MARKDOWN_ID_STYLE`**

The `MARKDOWN_ID_STYLE` tag can be used to specify the algorithm used to generate identifiers for the Markdown headings. Note: Every identifier is unique.

Possible values are: `DOXYGEN` use a fixed 'autotoc_md' string followed by a sequence number starting at 0 and `GITHUB` use the lower case version of title with any whitespace replaced by '-' and punctuation characters removed.

The default value is: `DOXYGEN`.

This tag requires that the tag MARKDOWN_SUPPORT is set to `YES`.

**`AUTOLINK_SUPPORT`**

When enabled Doxygen tries to link words that correspond to documented classes, or namespaces to their corresponding documentation. Such a link can be prevented in individual cases by putting a `%` sign in front of the word or globally by setting `AUTOLINK_SUPPORT` to `NO`. Words listed in the `AUTOLINK_IGNORE_WORDS` tag are excluded from automatic linking.

The default value is: `YES`.

**`AUTOLINK_IGNORE_WORDS`**

This tag specifies a list of words that, when matching the start of a word in the documentation, will suppress auto links generation, if it is enabled via AUTOLINK_SUPPORT. This list does not affect links explicitly created using # or the \link or \ref commands.

This tag requires that the tag AUTOLINK_SUPPORT is set to `YES`.

**`BUILTIN_STL_SUPPORT`**

If you use STL classes (i.e. std::string, std::vector, etc.) but do not want to include (a tag file for) the STL sources as input, then you should set this tag to `YES` in order to let Doxygen match functions declarations and definitions whose arguments contain STL classes (e.g. func(std::string); versus func(std::string) {}). This also makes the inheritance and collaboration diagrams that involve STL classes more complete and accurate.

The default value is: `NO`.

**`CPP_CLI_SUPPORT`**

If you use Microsoft's C++/CLI language, you should set this option to `YES` to enable parsing support.

The default value is: `NO`.

**`SIP_SUPPORT`**

Set the `SIP_SUPPORT` tag to `YES` if your project consists of sip sources only. Doxygen will parse them like normal C++ but will assume all classes use public instead of private inheritance when no explicit protection keyword is present.

The default value is: `NO`.

**`IDL_PROPERTY_SUPPORT`**

For Microsoft's IDL there are `propget` and `propput` attributes to indicate getter and setter methods for a property. Setting this option to `YES` will make Doxygen to replace the get and set methods by a property in the documentation. This will only work if the methods are indeed getting or setting a simple type. If this is not the case, or you want to show the methods anyway, you should set this option to `NO`.

The default value is: `YES`.

**`DISTRIBUTE_GROUP_DOC`**

If member grouping is used in the documentation and the `DISTRIBUTE_GROUP_DOC` tag is set to `YES` then Doxygen will reuse the documentation of the first member in the group (if any) for the other members of the group. By default all members of a group must be documented explicitly.

The default value is: `NO`.

**`GROUP_NESTED_COMPOUNDS`**

If one adds a struct or class to a group and this option is enabled, then also any nested class or struct is added to the same group. By default this option is disabled and one has to add nested compounds explicitly via \ingroup.

The default value is: `NO`.

**`SUBGROUPING`**

Set the `SUBGROUPING` tag to `YES` to allow class member groups of the same type (for instance a group of public functions) to be put as a subgroup of that type (e.g. under the Public Functions section). Set it to `NO` to prevent subgrouping. Alternatively, this can be done per class using the \nosubgrouping command.

The default value is: `YES`.

**`INLINE_GROUPED_CLASSES`**

When the `INLINE_GROUPED_CLASSES` tag is set to `YES`, classes, structs and unions are shown inside the group in which they are included (e.g. using \ingroup) instead of on a separate page (for HTML and Man pages) or section (for ($\mbox{\LaTeX}$) and RTF). Note that this feature does not work in combination with SEPARATE_MEMBER_PAGES.

The default value is: `NO`.

**`INLINE_SIMPLE_STRUCTS`**

When the `INLINE_SIMPLE_STRUCTS` tag is set to `YES`, structs, classes, and unions with only public data fields or simple typedef fields will be shown inline in the documentation of the scope in which they are defined (i.e. file, namespace, or group documentation), provided this scope is documented. If set to `NO`, structs, classes, and unions are shown on a separate page (for HTML and Man pages) or section (for ($\mbox{\LaTeX}$) and RTF).

The default value is: `NO`.

**`TYPEDEF_HIDES_STRUCT`**

When `TYPEDEF_HIDES_STRUCT` tag is enabled, a typedef of a struct, union, or enum is documented as struct, union, or enum with the name of the typedef. So `typedef struct TypeS {} TypeT`, will appear in the documentation as a struct with name `TypeT`. When disabled the typedef will appear as a member of a file, namespace, or class. And the struct will be named `TypeS`. This can typically be useful for C code in case the coding convention dictates that all compound types are typedef'ed and only the typedef is referenced, never the tag name.

The default value is: `NO`.

**`LOOKUP_CACHE_SIZE`**

The size of the symbol lookup cache can be set using `LOOKUP_CACHE_SIZE`. This cache is used to resolve symbols given their name and scope. Since this can be an expensive process and often the same symbol appears multiple times in the code, Doxygen keeps a cache of pre-resolved symbols. If the cache is too small Doxygen will become slower. If the cache is too large, memory is wasted. The cache size is given by this formula: ($2^{(16+\mbox{LOOKUP\_CACHE\_SIZE})}$). The valid range is 0..9, the default is 0, corresponding to a cache size of ($2^{16} = 65536$) symbols. At the end of a run Doxygen will report the cache usage and suggest the optimal cache size from a speed point of view.

Minimum value: `0`, maximum value: `9`, default value: `0`.

**`NUM_PROC_THREADS`**

The `NUM_PROC_THREADS` specifies the number of threads Doxygen is allowed to use during processing. When set to `0` Doxygen will based this on the number of cores available in the system. You can set it explicitly to a value larger than 0 to get more control over the balance between CPU load and processing speed. At this moment only the input processing can be done using multiple threads. Since this is still an experimental feature the default is set to 1, which effectively disables parallel processing. Please report any issues you encounter. Generating dot graphs in parallel is controlled by the `DOT_NUM_THREADS` setting.

Minimum value: `0`, maximum value: `512`, default value: `1`.

**`TIMESTAMP`**

If the `TIMESTAMP` tag is set different from `NO` then each generated page will contain the date or date and time when the page was generated. Setting this to `NO` can help when comparing the output of multiple runs.

Possible values are: `YES`, `NO`, `DATETIME` and `DATE`.

The default value is: `NO`.


# Build related configuration options

**`EXTRACT_ALL`**

If the `EXTRACT_ALL` tag is set to `YES`, Doxygen will assume all entities in documentation are documented, even if no documentation was available. Private class members and static file members will be hidden unless the EXTRACT_PRIVATE respectively EXTRACT_STATIC tags are set to `YES`.

**Note**

This will also disable the warnings about undocumented members that are normally produced when

WARNINGS

is set to

YES

.

The default value is: `NO`.

**`EXTRACT_PRIVATE`**

If the `EXTRACT_PRIVATE` tag is set to `YES`, all private members of a class will be included in the documentation.

The default value is: `NO`.

**`EXTRACT_PRIV_VIRTUAL`**

If the `EXTRACT_PRIV_VIRTUAL` tag is set to `YES`, documented private virtual methods of a class will be included in the documentation.

The default value is: `NO`.

**`EXTRACT_PACKAGE`**

If the `EXTRACT_PACKAGE` tag is set to `YES`, all members with package or internal scope will be included in the documentation.

The default value is: `NO`.

**`EXTRACT_STATIC`**

If the `EXTRACT_STATIC` tag is set to `YES`, all static members of a file will be included in the documentation.

The default value is: `NO`.

**`EXTRACT_LOCAL_CLASSES`**

If the `EXTRACT_LOCAL_CLASSES` tag is set to `YES`, classes (and structs) defined locally in source files will be included in the documentation. If set to `NO`, only classes defined in header files are included. Does not have any effect for Java sources.

The default value is: `YES`.

**`EXTRACT_LOCAL_METHODS`**

This flag is only useful for Objective-C code. If set to `YES`, local methods, which are defined in the implementation section but not in the interface are included in the documentation. If set to `NO`, only methods in the interface are included.

The default value is: `NO`.

**`EXTRACT_ANON_NSPACES`**

If this flag is set to `YES`, the members of anonymous namespaces will be extracted and appear in the documentation as a namespace called 'anonymous_namespace{file}', where file will be replaced with the base name of the file that contains the anonymous namespace. By default anonymous namespace are hidden.

The default value is: `NO`.

**`RESOLVE_UNNAMED_PARAMS`**

If this flag is set to `YES`, the name of an unnamed parameter in a declaration will be determined by the corresponding definition. By default unnamed parameters remain unnamed in the output.

The default value is: `YES`.

**`HIDE_UNDOC_MEMBERS`**

If the `HIDE_UNDOC_MEMBERS` tag is set to `YES`, Doxygen will hide all undocumented members inside documented classes or files. If set to `NO` these members will be included in the various overviews, but no documentation section is generated. This option has no effect if EXTRACT_ALL is enabled.

The default value is: `NO`.

**`HIDE_UNDOC_CLASSES`**

If the `HIDE_UNDOC_CLASSES` tag is set to `YES`, Doxygen will hide all undocumented classes that are normally visible in the class hierarchy. If set to `NO`, these classes will be included in the various overviews. This option will also hide undocumented C++ concepts if enabled. This option has no effect if EXTRACT_ALL is enabled.

The default value is: `NO`.

**`HIDE_UNDOC_NAMESPACES`**

If the `HIDE_UNDOC_NAMESPACES` tag is set to `YES`, Doxygen will hide all undocumented namespaces that are normally visible in the namespace hierarchy. If set to `NO`, these namespaces will be included in the various overviews. This option has no effect if EXTRACT_ALL is enabled.

The default value is: `YES`.

**`HIDE_FRIEND_COMPOUNDS`**

If the `HIDE_FRIEND_COMPOUNDS` tag is set to `YES`, Doxygen will hide all friend declarations. If set to `NO`, these declarations will be included in the documentation.

The default value is: `NO`.

**`HIDE_IN_BODY_DOCS`**

If the `HIDE_IN_BODY_DOCS` tag is set to `YES`, Doxygen will hide any documentation blocks found inside the body of a function. If set to `NO`, these blocks will be appended to the function's detailed documentation block.

The default value is: `NO`.

**`INTERNAL_DOCS`**

The `INTERNAL_DOCS` tag determines if documentation that is typed after a \internal command is included. If the tag is set to `NO` then the documentation will be excluded. Set it to `YES` to include the internal documentation.

The default value is: `NO`.

**`CASE_SENSE_NAMES`**

With the correct setting of option `CASE_SENSE_NAMES` Doxygen will better be able to match the capabilities of the underlying filesystem.

In case the filesystem is case sensitive (i.e. it supports files in the same directory whose names only differ in casing), the option must be set to `YES` to properly deal with such files in case they appear in the input.

For filesystems that are not case sensitive the option should be set to `NO` to properly deal with output files written for symbols that only differ in casing, such as for two classes, one named `CLASS` and the other named `Class`, and to also support references to files without having to specify the exact matching casing.

On Windows (including Cygwin) and macOS, users should typically set this option to `NO`, whereas on Linux or other Unix flavors it should typically be set to `YES`.

Possible values are: `SYSTEM`, `NO` and `YES`.

The default value is: `SYSTEM`.

**`HIDE_SCOPE_NAMES`**

If the `HIDE_SCOPE_NAMES` tag is set to `NO` then Doxygen will show members with their full class and namespace scopes in the documentation. If set to `YES`, the scope will be hidden.

The default value is: `NO`.

**`HIDE_COMPOUND_REFERENCE`**

If the `HIDE_COMPOUND_REFERENCE` tag is set to `NO` (default) then Doxygen will append additional text to a page's title, such as Class Reference. If set to `YES` the compound reference will be hidden.

The default value is: `NO`.

**`SHOW_HEADERFILE`**

If the `SHOW_HEADERFILE` tag is set to `YES` then the documentation for a class will show which file needs to be included to use the class.

The default value is: `YES`.

**`SHOW_INCLUDE_FILES`**

If the `SHOW_INCLUDE_FILES` tag is set to `YES` then Doxygen will put a list of the files that are included by a file in the documentation of that file.

The default value is: `YES`.

**`SHOW_GROUPED_MEMB_INC`**

If the `SHOW_GROUPED_MEMB_INC` tag is set to `YES` then Doxygen will add for each grouped member an include statement to the documentation, telling the reader which file to include in order to use the member.

The default value is: `NO`.

**`FORCE_LOCAL_INCLUDES`**

If the `FORCE_LOCAL_INCLUDES` tag is set to `YES` then Doxygen will list include files with double quotes in the documentation rather than with sharp brackets.

The default value is: `NO`.

**`INLINE_INFO`**

If the `INLINE_INFO` tag is set to `YES` then a tag [inline] is inserted in the documentation for inline members.

The default value is: `YES`.

**`SORT_MEMBER_DOCS`**

If the `SORT_MEMBER_DOCS` tag is set to `YES` then Doxygen will sort the (detailed) documentation of file and class members alphabetically by member name. If set to `NO`, the members will appear in declaration order.

The default value is: `YES`.

**`SORT_BRIEF_DOCS`**

If the `SORT_BRIEF_DOCS` tag is set to `YES` then Doxygen will sort the brief descriptions of file, namespace and class members alphabetically by member name. If set to `NO`, the members will appear in declaration order. Note that this will also influence the order of the classes in the class list.

The default value is: `NO`.

**`SORT_MEMBERS_CTORS_1ST`**

If the `SORT_MEMBERS_CTORS_1ST` tag is set to `YES` then Doxygen will sort the (brief and detailed) documentation of class members so that constructors and destructors are listed first. If set to `NO` the constructors will appear in the respective orders defined by SORT_BRIEF_DOCS and SORT_MEMBER_DOCS.

**Note**

If

SORT_BRIEF_DOCS

is set to

NO

this option is ignored for sorting brief member documentation.

If

SORT_MEMBER_DOCS

is set to

NO

this option is ignored for sorting detailed member documentation.

The default value is: `NO`.

**`SORT_GROUP_NAMES`**

If the `SORT_GROUP_NAMES` tag is set to `YES` then Doxygen will sort the hierarchy of group names into alphabetical order. If set to `NO` the group names will appear in their defined order.

The default value is: `NO`.

**`SORT_BY_SCOPE_NAME`**

If the `SORT_BY_SCOPE_NAME` tag is set to `YES`, the class list will be sorted by fully-qualified names, including namespaces. If set to `NO`, the class list will be sorted only by class name, not including the namespace part.

**Note**

This option is not very useful if

HIDE_SCOPE_NAMES

is set to

YES

.

This option applies only to the class list, not to the alphabetical list.

The default value is: `NO`.

**`STRICT_PROTO_MATCHING`**

If the `STRICT_PROTO_MATCHING` option is enabled and Doxygen fails to do proper type resolution of all parameters of a function it will reject a match between the prototype and the implementation of a member function even if there is only one candidate or it is obvious which candidate to choose by doing a simple string match. By disabling `STRICT_PROTO_MATCHING` Doxygen will still accept a match between prototype and implementation in such cases.

The default value is: `NO`.

**`GENERATE_TODOLIST`**

The `GENERATE_TODOLIST` tag can be used to enable (`YES`) or disable (`NO`) the todo list. This list is created by putting \todo commands in the documentation.

The default value is: `YES`.

**`GENERATE_TESTLIST`**

The `GENERATE_TESTLIST` tag can be used to enable (`YES`) or disable (`NO`) the test list. This list is created by putting \test commands in the documentation.

The default value is: `YES`.

**`GENERATE_BUGLIST`**

The `GENERATE_BUGLIST` tag can be used to enable (`YES`) or disable (`NO`) the bug list. This list is created by putting \bug commands in the documentation.

The default value is: `YES`.

**`GENERATE_DEPRECATEDLIST`**

The `GENERATE_DEPRECATEDLIST` tag can be used to enable (`YES`) or disable (`NO`) the deprecated list. This list is created by putting \deprecated commands in the documentation.

The default value is: `YES`.

**`GENERATE_REQUIREMENTS`**

The `GENERATE_REQUIREMENTS` tag can be used to enable (`YES`) or disable (`NO`) the requirements page. When enabled, this page is automatically created when at least one comment block with a \requirement command appears in the input.

The default value is: `YES`.

**`REQ_TRACEABILITY_INFO`**

The `REQ_TRACEABILITY_INFO` tag controls if traceability information is shown on the requirements page (only relevant when using \requirement comment blocks). The setting `NO` will disable the traceability information altogether. The setting `UNSATISFIED_ONLY` will show a list of requirements that are missing a satisfies relation (through the command: \satisfies). Similarly the setting `UNVERIFIED_ONLY` will show a list of requirements that are missing a verifies relation (through the command: \verifies). Setting the tag to `YES` (the default) will show both lists if applicable.

Possible values are: `YES`, `NO`, `UNSATISFIED_ONLY` and `UNVERIFIED_ONLY`.

The default value is: `YES`.

This tag requires that the tag GENERATE_REQUIREMENTS is set to `YES`.

**`ENABLED_SECTIONS`**

The `ENABLED_SECTIONS` tag can be used to enable conditional documentation sections, marked by \if <section_label> ... \endif and \cond <section_label> ... \endcond blocks.

**`MAX_INITIALIZER_LINES`**

The `MAX_INITIALIZER_LINES` tag determines the maximum number of lines that the initial value of a variable or macro / define can have for it to appear in the documentation. If the initializer consists of more lines than specified here it will be hidden. Use a value of 0 to hide initializers completely. The appearance of the value of individual variables and macros / defines can be controlled using \showinitializer or \hideinitializer command in the documentation regardless of this setting.

Minimum value: `0`, maximum value: `10000`, default value: `30`.

**`SHOW_USED_FILES`**

Set the `SHOW_USED_FILES` tag to `NO` to disable the list of files generated at the bottom of the documentation of classes and structs. If set to `YES`, the list will mention the files that were used to generate the documentation.

The default value is: `YES`.

**`SHOW_FILES`**

Set the `SHOW_FILES` tag to `NO` to disable the generation of the Files page. This will remove the Files entry from the Quick Index and from the Folder Tree View (if specified).

The default value is: `YES`.

**`SHOW_NAMESPACES`**

Set the `SHOW_NAMESPACES` tag to `NO` to disable the generation of the Namespaces page. This will remove the Namespaces entry from the Quick Index and from the Folder Tree View (if specified).

The default value is: `YES`.

**`FILE_VERSION_FILTER`**

The `FILE_VERSION_FILTER` tag can be used to specify a program or script that Doxygen should invoke to get the current version for each file (typically from the version control system). Doxygen will invoke the program by executing (via `popen()`) the command `command input-file`, where `command` is the value of the `FILE_VERSION_FILTER` tag, and `input-file` is the name of an input file provided by Doxygen. Whatever the program writes to standard output is used as the file version. Example of using a shell script as a filter for Unix:

```
 FILE_VERSION_FILTER = "/bin/sh versionfilter.sh"
```

Example shell script for CVS:

```
#!/bin/sh
cvs status $1 | sed -n 's/^[ \‍]*Working revision:[ \t]*\‍([0-9][0-9\.]*\‍).*/\1/p'
```

Example shell script for Subversion:

```
#!/bin/sh
svn stat -v $1 | sed -n 's/^[ A-Z?\*|!]\{1,15\}/r/;s/ \{1,15\}/\/r/;s/ .*//p'
```

Example filter for ClearCase:

```
FILE_VERSION_FILTER = "cleartool desc -fmt \%Vn"
```

**`LAYOUT_FILE`**

The `LAYOUT_FILE` tag can be used to specify a layout file which will be parsed by Doxygen. The layout file controls the global structure of the generated output files in an output format independent way. To create the layout file that represents Doxygen's defaults, run Doxygen with the -l option. You can optionally specify a file name after the option, if omitted `DoxygenLayout.xml` will be used as the name of the layout file. See also section Changing the layout of pages for information. Note that if you run Doxygen from a directory containing a file called `DoxygenLayout.xml`, Doxygen will parse it automatically even if the `LAYOUT_FILE` tag is left empty.

**`CITE_BIB_FILES`**

The `CITE_BIB_FILES` tag can be used to specify one or more `bib` files containing the reference definitions. This must be a list of `.bib` files. The `.bib` extension is automatically appended if omitted. This requires the `bibtex` tool to be installed. See also https://en.wikipedia.org/wiki/BibTeX for more info. For ($\mbox{\LaTeX}$) the style of the bibliography can be controlled using LATEX_BIB_STYLE. To use this feature you need `bibtex` and `perl` available in the search path. See also \cite for info how to create references.

**`EXTERNAL_TOOL_PATH`**

The

EXTERNAL_TOOL_PATH

tag can be used to extend the search path (PATH environment variable) so that external tools such as

latex

and

gs

can be found.

**Note**

Directories specified with EXTERNAL_TOOL_PATH are added in front of the path already specified by the PATH variable, and are added in the order specified.

This option is particularly useful for macOS version 14 (Sonoma) and higher, when running Doxygen from Doxywizard, because in this case any user-defined changes to the PATH are ignored. A typical example on macOS is to set

```
EXTERNAL_TOOL_PATH = /Library/TeX/texbin /usr/local/bin
```

together with the standard path, the full search path used by doxygen when launching external tools will then become

```
PATH=/Library/TeX/texbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```
