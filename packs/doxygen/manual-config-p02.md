---
title: "Doxygen: Configuration (part 2/5)"
source: https://www.doxygen.nl/manual/config.html
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
part: 2/5
---

# Configuration options related to warning and progress messages

**`QUIET`**

The `QUIET` tag can be used to turn on/off the messages that are generated to standard output by Doxygen. If `QUIET` is set to `YES` this implies that the messages are off.

The default value is: `NO`.

**`WARNINGS`**

The `WARNINGS` tag can be used to turn on/off the warning messages that are generated to standard error (`stderr`) by Doxygen. If `WARNINGS` is set to `YES` this implies that the warnings are on. **Tip:** Turn warnings on while writing the documentation.

The default value is: `YES`.

**`WARN_IF_UNDOCUMENTED`**

If the `WARN_IF_UNDOCUMENTED` tag is set to `YES` then Doxygen will generate warnings for undocumented members. If EXTRACT_ALL is set to `YES` then this flag will automatically be disabled.

The default value is: `YES`.

**`WARN_IF_DOC_ERROR`**

If the `WARN_IF_DOC_ERROR` tag is set to `YES`, Doxygen will generate warnings for potential errors in the documentation, such as documenting some parameters in a documented function twice, or documenting parameters that don't exist or using markup commands wrongly.

The default value is: `YES`.

**`WARN_IF_INCOMPLETE_DOC`**

If `WARN_IF_INCOMPLETE_DOC` is set to `YES`, Doxygen will warn about incomplete function parameter documentation. If set to `NO`, Doxygen will accept that some parameters have no documentation without warning.

The default value is: `YES`.

**`WARN_NO_PARAMDOC`**

This `WARN_NO_PARAMDOC` option can be enabled to get warnings for functions that are documented, but have no documentation for their parameters or return value. If set to `NO`, Doxygen will only warn about wrong parameter documentation, but not about the absence of documentation. If EXTRACT_ALL is set to `YES` then this flag will automatically be disabled. See also WARN_IF_INCOMPLETE_DOC

The default value is: `NO`.

**`WARN_IF_UNDOC_ENUM_VAL`**

If `WARN_IF_UNDOC_ENUM_VAL` option is set to `YES`, Doxygen will warn about undocumented enumeration values. If set to `NO`, Doxygen will accept undocumented enumeration values. If EXTRACT_ALL is set to `YES` then this flag will automatically be disabled.

The default value is: `NO`.

**`WARN_LAYOUT_FILE`**

If `WARN_LAYOUT_FILE` option is set to `YES`, Doxygen will warn about issues found while parsing the user defined layout file, such as missing or wrong elements. See also LAYOUT_FILE for details. If set to `NO`, problems with the layout file will be suppressed.

The default value is: `YES`.

**`WARN_AS_ERROR`**

If the `WARN_AS_ERROR` tag is set to `YES` then Doxygen will immediately stop when a warning is encountered. If the `WARN_AS_ERROR` tag is set to `FAIL_ON_WARNINGS` then Doxygen will continue running as if `WARN_AS_ERROR` tag is set to `NO`, but at the end of the Doxygen process Doxygen will return with a non-zero status. If the `WARN_AS_ERROR` tag is set to `FAIL_ON_WARNINGS_PRINT` then Doxygen behaves like `FAIL_ON_WARNINGS` but in case no WARN_LOGFILE is defined Doxygen will not write the warning messages in between other messages but write them at the end of a run, in case a WARN_LOGFILE is defined the warning messages will be besides being in the defined file also be shown at the end of a run, unless the WARN_LOGFILE is defined as - i.e. standard output (stdout) in that case the behavior will remain as with the setting `FAIL_ON_WARNINGS`.

Possible values are: `NO`, `YES`, `FAIL_ON_WARNINGS` and `FAIL_ON_WARNINGS_PRINT`.

The default value is: `NO`.

**`WARN_FORMAT`**

The `WARN_FORMAT` tag determines the format of the warning messages that Doxygen can produce. The string should contain the `$file`, `$line`, and `$text` tags, which will be replaced by the file and line number from which the warning originated and the warning text. Optionally the format may contain `$version`, which will be replaced by the version of the file (if it could be obtained via FILE_VERSION_FILTER)

**See also**

WARN_LINE_FORMAT

The default value is: `$file:$line: $text`.

**`WARN_LINE_FORMAT`**

In the $text part of the WARN_FORMAT command it is possible that a reference to a more specific place is given. To make it easier to jump to this place (outside of Doxygen) the user can define a custom "cut" / "paste" string.

Example:

```
  WARN_LINE_FORMAT = "'vi $file +$line'"
```

**See also**

WARN_FORMAT

The default value is: `at line $line of file $file`.

**`WARN_LOGFILE`**

The `WARN_LOGFILE` tag can be used to specify a file to which warning and error messages should be written. If left blank the output is written to standard error (stderr). In case the file specified cannot be opened for writing the warning and error messages are written to standard error. When as file - is specified the warning and error messages are written to standard output (stdout).


# Configuration options related to the input files

**`INPUT`**

The `INPUT` tag is used to specify the files and/or directories that contain documented source files. You may enter file names like `myfile.cpp` or directories like `/usr/src/myproject`. Separate the files or directories with spaces. See also FILE_PATTERNS and EXTENSION_MAPPING

**Note**

If this tag is empty the current directory is searched.

**`INPUT_ENCODING`**

This tag can be used to specify the character encoding of the source files that Doxygen parses. Internally Doxygen uses the UTF-8 encoding. Doxygen uses libiconv (or the iconv built into libc) for the transcoding. See the libiconv documentation for the list of possible encodings.

**See also**

INPUT_FILE_ENCODING

The default value is: `UTF-8`.

**`INPUT_FILE_ENCODING`**

This tag can be used to specify the character encoding of the source files that Doxygen parses. The `INPUT_FILE_ENCODING` tag can be used to specify character encoding on a per file pattern basis. Doxygen will compare the file name with each pattern and apply the encoding instead of the default INPUT_ENCODING if there is a match. The character encodings are a list of the form: pattern=encoding (like *.php=ISO-8859-1).

**See also**

INPUT_ENCODING

for further information on supported encodings.

**`FILE_PATTERNS`**

If the value of the INPUT tag contains directories, you can use the `FILE_PATTERNS` tag to specify one or more wildcard patterns (like *.cpp and *.h) to filter out the source-files in the directories. Note that for custom extensions or not directly supported extensions you also need to set EXTENSION_MAPPING for the extension otherwise the files are not read by Doxygen. Note the list of default checked file patterns might differ from the list of default file extension mappings. If left blank the following patterns are tested: `*.c`, `*.cc`, `*.cxx`, `*.cxxm`, `*.cpp`, `*.cppm`, `*.ccm`, `*.c++`, `*.c++m`, `*.java`, `*.ii`, `*.ixx`, `*.ipp`, `*.i++`, `*.inl`, `*.idl`, `*.ddl`, `*.odl`, `*.h`, `*.hh`, `*.hxx`, `*.hpp`, `*.h++`, `*.l`, `*.cs`, `*.d`, `*.php`, `*.php4`, `*.php5`, `*.phtml`, `*.inc`, `*.m`, `*.markdown`, `*.md`, `*.mm`, `*.dox` (to be provided as Doxygen C comment), `*.py`, `*.pyw`, `*.f90`, `*.f95`, `*.f03`, `*.f08`, `*.f18`, `*.f`, `*.for`, `*.vhd`, `*.vhdl`, `*.ucf`, `*.qsf` and `*.ice`.

**`RECURSIVE`**

The `RECURSIVE` tag can be used to specify whether or not subdirectories should be searched for input files as well.

The default value is: `NO`.

**`EXCLUDE`**

The `EXCLUDE` tag can be used to specify files and/or directories that should be excluded from the INPUT source files. This way you can easily exclude a subdirectory from a directory tree whose root is specified with the INPUT tag. Note that relative paths are relative to the directory from which Doxygen is run.

**`EXCLUDE_SYMLINKS`**

The `EXCLUDE_SYMLINKS` tag can be used to select whether or not files or directories that are symbolic links (a Unix file system feature) are excluded from the input.

The default value is: `NO`.

**`EXCLUDE_PATTERNS`**

If the value of the INPUT tag contains directories, you can use the `EXCLUDE_PATTERNS` tag to specify one or more wildcard patterns to exclude certain files from those directories. Note that the wildcards are matched against the file with absolute path, so to exclude all test directories for example use the pattern *``/test/``*

**`EXCLUDE_SYMBOLS`**

The `EXCLUDE_SYMBOLS` tag can be used to specify one or more symbol names (namespaces, classes, functions, etc.) that should be excluded from the output. The symbol name can be a fully qualified name, a word, or if the wildcard * is used, a substring. Examples: ANamespace, AClass, ANamespace::AClass, ANamespace::*Test

**`EXAMPLE_PATH`**

The `EXAMPLE_PATH` tag can be used to specify one or more files or directories that contain example code fragments that are included (see the \include command).

**`EXAMPLE_PATTERNS`**

If the value of the EXAMPLE_PATH tag contains directories, you can use the `EXAMPLE_PATTERNS` tag to specify one or more wildcard pattern (like *.cpp and *.h) to filter out the source-files in the directories. If left blank all files are included.

**`EXAMPLE_RECURSIVE`**

If the `EXAMPLE_RECURSIVE` tag is set to `YES` then subdirectories will be searched for input files to be used with the \include or \dontinclude commands irrespective of the value of the RECURSIVE tag.

The default value is: `NO`.

**`IMAGE_PATH`**

The `IMAGE_PATH` tag can be used to specify one or more files or directories that contain images that are to be included in the documentation (see the \image command).

**`INPUT_FILTER`**

The `INPUT_FILTER` tag can be used to specify a program that Doxygen should invoke to filter for each input file. Doxygen will invoke the filter program by executing (via `popen()`) the command: `<filter> <input-file>` where `<filter>` is the value of the `INPUT_FILTER` tag, and `<input-file>` is the name of an input file. Doxygen will then use the output that the filter program writes to standard output. If FILTER_PATTERNS is specified, this tag will be ignored. Note that the filter must not add or remove lines; it is applied before the code is scanned, but not when the output code is generated. If lines are added or removed, the anchors will not be placed correctly. Note that Doxygen will use the data processed and written to standard output for further processing, therefore nothing else, like debug statements or used commands (so in case of a Windows batch file always use @echo OFF), should be written to standard output. Note that for custom extensions or not directly supported extensions you also need to set EXTENSION_MAPPING for the extension otherwise the files are not properly processed by Doxygen.

**`FILTER_PATTERNS`**

The `FILTER_PATTERNS` tag can be used to specify filters on a per file pattern basis. Doxygen will compare the file name with each pattern and apply the filter if there is a match. The filters are a list of the form: pattern=filter (like *.cpp=my_cpp_filter). See INPUT_FILTER for further information on how filters are used. If the `FILTER_PATTERNS` tag is empty or if none of the patterns match the file name, INPUT_FILTER is applied. Note that for custom extensions or not directly supported extensions you also need to set EXTENSION_MAPPING for the extension otherwise the files are not properly processed by Doxygen.

**`FILTER_SOURCE_FILES`**

If the `FILTER_SOURCE_FILES` tag is set to `YES`, the input filter (if set using INPUT_FILTER) will also be used to filter the input files that are used for producing the source files to browse (i.e. when SOURCE_BROWSER is set to `YES`).

The default value is: `NO`.

**`FILTER_SOURCE_PATTERNS`**

The `FILTER_SOURCE_PATTERNS` tag can be used to specify source filters per file pattern. A pattern will override the setting for FILTER_PATTERN (if any) and it is also possible to disable source filtering for a specific pattern using *.ext= (so without naming a filter).

This tag requires that the tag FILTER_SOURCE_FILES is set to `YES`.

**`USE_MDFILE_AS_MAINPAGE`**

If the `USE_MDFILE_AS_MAINPAGE` tag refers to the name of a markdown file that is part of the input, its contents will be placed on the main page (index.html). This can be useful if you have a project on for instance GitHub and want to reuse the introduction page also for the Doxygen output.

**`IMPLICIT_DIR_DOCS`**

If the `IMPLICIT_DIR_DOCS` tag is set to `YES`, any README.md file found in sub-directories of the project's root, is used as the documentation for that sub-directory, except when the README.md starts with a \dir, \page or \mainpage command. If set to `NO`, the README.md file needs to start with an explicit \dir command in order to be used as directory documentation.

The default value is: `YES`.

**`FORTRAN_COMMENT_AFTER`**

The Fortran standard specifies that for fixed formatted Fortran code all characters from position 72 are to be considered as comment. A common extension is to allow longer lines before the automatic comment starts. The setting `FORTRAN_COMMENT_AFTER` will also make it possible that longer lines can be processed before the automatic comment starts.

Minimum value: `7`, maximum value: `10000`, default value: `72`.


# Configuration options related to source browsing

**`SOURCE_BROWSER`**

If the `SOURCE_BROWSER` tag is set to `YES` then a list of source files will be generated. Documented entities will be cross-referenced with these sources. Note: To get rid of all source code in the generated output, make sure that also VERBATIM_HEADERS is set to `NO`.

The default value is: `NO`.

**`INLINE_SOURCES`**

Setting the `INLINE_SOURCES` tag to `YES` will include the body of functions, multi-line macros, enums or list initialized variables directly into the documentation.

The default value is: `NO`.

**`STRIP_CODE_COMMENTS`**

Setting the `STRIP_CODE_COMMENTS` tag to `YES` will instruct Doxygen to hide any special comment blocks from generated source code fragments. Normal C, C++ and Fortran comments will always remain visible.

The default value is: `YES`.

**`REFERENCED_BY_RELATION`**

If the `REFERENCED_BY_RELATION` tag is set to `YES` then for each documented entity all documented functions referencing it will be listed.

The default value is: `NO`.

**`REFERENCES_RELATION`**

If the `REFERENCES_RELATION` tag is set to `YES` then for each documented function all documented entities called/used by that function will be listed.

The default value is: `NO`.

**`REFERENCES_LINK_SOURCE`**

If the `REFERENCES_LINK_SOURCE` tag is set to `YES` and SOURCE_BROWSER tag is set to `YES` then the hyperlinks from functions in REFERENCES_RELATION and REFERENCED_BY_RELATION lists will link to the source code. Otherwise they will link to the documentation.

The default value is: `YES`.

**`SOURCE_TOOLTIPS`**

If `SOURCE_TOOLTIPS` is enabled (the default) then hovering a hyperlink in the source code will show a tooltip with additional information such as prototype, brief description and links to the definition and documentation. Since this will make the HTML file larger and loading of large files a bit slower, you can opt to disable this feature.

The default value is: `YES`.

This tag requires that the tag SOURCE_BROWSER is set to `YES`.

**`USE_HTAGS`**

If the `USE_HTAGS` tag is set to `YES` then the references to source code will point to the HTML generated by the `htags(1)` tool instead of Doxygen built-in source browser. The `htags` tool is part of GNU's global source tagging system (see https://www.gnu.org/software/global/global.html). You will need version 4.8.6 or higher. To use it do the following:

1. Install the latest version of `global`
2. Enable SOURCE_BROWSER and `USE_HTAGS` in the configuration file
3. Make sure the INPUT points to the root of the source tree
4. Run `doxygen` as normal Doxygen will invoke `htags` (and that will in turn invoke `gtags`), so these tools must be available from the command line (i.e. in the search path). The result: instead of the source browser generated by Doxygen, the links to source code will now point to the output of `htags`.

The default value is: `NO`.

This tag requires that the tag SOURCE_BROWSER is set to `YES`.

**`VERBATIM_HEADERS`**

If the `VERBATIM_HEADERS` tag is set the `YES` then Doxygen will generate a verbatim copy of the header file for each class for which an include is specified. Set to `NO` to disable this.

**See also**

Section

\class

.

The default value is: `YES`.

**`CLANG_ASSISTED_PARSING`**

If the `CLANG_ASSISTED_PARSING` tag is set to `YES` then Doxygen will use the clang parser for more accurate parsing at the cost of reduced performance. This can be particularly helpful with template rich C++ code for which Doxygen's built-in parser lacks the necessary type information.

**Note**

The availability of this option depends on whether or not Doxygen was generated with the

-Duse_libclang=ON

option for CMake.

The default value is: `NO`.

**`CLANG_ADD_INC_PATHS`**

If the `CLANG_ASSISTED_PARSING` tag is set to `YES` and the `CLANG_ADD_INC_PATHS` tag is set to `YES` then Doxygen will add the directory of each input to the include path.

The default value is: `YES`.

This tag requires that the tag CLANG_ASSISTED_PARSING is set to `YES`.

**`CLANG_OPTIONS`**

If clang assisted parsing is enabled you can provide the compiler with command line options that you would normally use when invoking the compiler. Note that the include paths will already be set by Doxygen for the files and directories specified with INPUT and INCLUDE_PATH.

This tag requires that the tag CLANG_ASSISTED_PARSING is set to `YES`.

**`CLANG_DATABASE_PATH`**

If clang assisted parsing is enabled you can provide the clang parser with the path to the directory containing a file called compile_commands.json. This file is the compilation database containing the options used when the source files were built. This is equivalent to specifying the -p option to a clang tool, such as clang-check. These options will then be passed to the parser. Any options specified with CLANG_OPTIONS will be added as well.

**Note**

The availability of this option depends on whether or not Doxygen was generated with the

-Duse_libclang=ON

option for CMake.


# Configuration options related to the alphabetical class index

**`ALPHABETICAL_INDEX`**

If the `ALPHABETICAL_INDEX` tag is set to `YES`, an alphabetical index of all compounds will be generated. Enable this if the project contains a lot of classes, structs, unions or interfaces.

The default value is: `YES`.

**`IGNORE_PREFIX`**

The `IGNORE_PREFIX` tag can be used to specify a prefix (or a list of prefixes) that should be ignored while generating the index headers. The `IGNORE_PREFIX` tag works for classes, function and member names. The entity will be placed in the alphabetical list under the first letter of the entity name that remains after removing the prefix.

This tag requires that the tag ALPHABETICAL_INDEX is set to `YES`.
