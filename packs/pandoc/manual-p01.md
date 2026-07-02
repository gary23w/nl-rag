---
title: "Pandoc (part 1/4)"
source: https://pandoc.org/MANUAL.html
domain: pandoc
license: CC-BY-SA-4.0
tags: pandoc converter, document conversion, markup converter, markdown to pdf
fetched: 2026-07-02
part: 1/4
---

# Pandoc User’s Guide

# Synopsis

`pandoc` [*options*] [*input-file*]…

# Description

Pandoc is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library.

Pandoc can convert between numerous markup and word processing formats, including, but not limited to, various flavors of Markdown, HTML, LaTeX and Word docx. For the full lists of input and output formats, see the `--from` and `--to` options below. Pandoc can also produce PDF output: see creating a PDF, below.

Pandoc’s enhanced version of Markdown includes syntax for tables, definition lists, metadata blocks, footnotes, citations, math, and much more. See below under Pandoc’s Markdown.

Pandoc has a modular design: it consists of a set of readers, which parse text in a given format and produce a native representation of the document (an *abstract syntax tree* or AST), and a set of writers, which convert this native representation into a target format. Thus, adding an input or output format requires only adding a reader or writer. Users can also run custom pandoc filters to modify the intermediate AST.

Because pandoc’s intermediate representation of a document is less expressive than many of the formats it converts between, one should not expect perfect conversions between every format and every other. Pandoc attempts to preserve the structural elements of a document, but not formatting details such as margin size. And some document elements, such as complex tables, may not fit into pandoc’s simple document model. While conversions from pandoc’s Markdown to all formats aspire to be perfect, conversions from formats more expressive than pandoc’s Markdown can be expected to be lossy.


## Using pandoc

If no *input-files* are specified, input is read from *stdin*. Output goes to *stdout* by default. For output to a file, use the `-o`/`--output` option:

```
pandoc -o output.html input.txt
```

By default, pandoc produces a document fragment. To produce a standalone document (e.g. a valid HTML file including `<head>` and `<body>`), use the `-s` or `--standalone` flag:

```
pandoc -s -o output.html input.txt
```

For more information on how standalone documents are produced, see Templates below.

If multiple input files are given, pandoc will concatenate them all (with blank lines between them) before parsing. (Use `--file-scope` to parse files individually.)


## Specifying formats

The format of the input and output can be specified explicitly using command-line options. The input format can be specified using the `-f/--from` option, the output format using the `-t/--to` option. Thus, to convert `hello.txt` from Markdown to LaTeX, you could type:

```
pandoc -f markdown -t latex hello.txt
```

To convert `hello.html` from HTML to Markdown:

```
pandoc -f html -t markdown hello.html
```

Supported input and output formats are listed below under Options (see `-f` for input formats and `-t` for output formats). You can also use `pandoc --list-input-formats` and `pandoc --list-output-formats` to print lists of supported formats.

If the input or output format is not specified explicitly, pandoc will attempt to guess it from the extensions of the filenames. Thus, for example,

```
pandoc -o hello.tex hello.txt
```

will convert `hello.txt` from Markdown to LaTeX. If no output file is specified (so that output goes to *stdout*), or if the output file’s extension is unknown, the output format will default to HTML. If no input file is specified (so that input comes from *stdin*), or if the input files’ extensions are unknown, the input format will be assumed to be Markdown.


## Character encoding

Pandoc uses the UTF-8 character encoding for both input and output. If your local character encoding is not UTF-8, you should pipe input and output through `iconv`:

```
iconv -t utf-8 input.txt | pandoc | iconv -f utf-8
```

Note that in some output formats (such as HTML, LaTeX, ConTeXt, RTF, OPML, DocBook, and Texinfo), information about the character encoding is included in the document header, which will only be included if you use the `-s/--standalone` option.


## Creating a PDF

To produce a PDF, specify an output file with a `.pdf` extension:

```
pandoc test.txt -o test.pdf
```

By default, pandoc will use LaTeX to create the PDF, which requires that a LaTeX engine be installed (see `--pdf-engine` below). Alternatively, pandoc can use ConTeXt, roff ms, or HTML as an intermediate format. To do this, specify an output file with a `.pdf` extension, as before, but add the `--pdf-engine` option or `-t context`, `-t html`, or `-t ms` to the command line. The tool used to generate the PDF from the intermediate format may be specified using `--pdf-engine`.

You can control the PDF style using variables, depending on the intermediate format used: see variables for LaTeX, variables for ConTeXt, variables for `wkhtmltopdf`, variables for ms. When HTML is used as an intermediate format, the output can be styled using `--css`.

To debug the PDF creation, it can be useful to look at the intermediate representation: instead of `-o test.pdf`, use for example `-s -o test.tex` to output the generated LaTeX. You can then test it with `pdflatex test.tex`.

When using LaTeX, the following packages need to be available (they are included with all recent versions of TeX Live): `amsfonts`, `amsmath`, `lm`, `unicode-math`, `iftex`, `listings` (if the `--listings` option is used), `fancyvrb`, `longtable`, `booktabs`, `multirow` (if the document contains a table with cells that cross multiple rows), `graphicx` (if the document contains images), `bookmark`, `xcolor`, `soul`, `geometry` (with the `geometry` variable set), `setspace` (with `linestretch`), and `babel` (with `lang`). If `CJKmainfont` is set, `xeCJK` is needed if `xelatex` is used, else `luatexja` is needed if `lualatex` is used. `framed` is required if code is highlighted in a scheme that use a colored background. The use of `xelatex` or `lualatex` as the PDF engine requires `fontspec`. `lualatex` uses `selnolig` and `lua-ul`. `xelatex` uses `bidi` (with the `dir` variable set). If the `mathspec` variable is set, `xelatex` will use `mathspec` instead of `unicode-math`. The `csquotes` package will be used for typography if the `csquotes` variable or metadata field is set to a true value. The `natbib`, `biblatex`, `bibtex`, and `biber` packages can optionally be used for citation rendering. If math with `\cancel`, `\bcancel`, or `\xcancel` is used, the `cancel` package is needed. The following packages will be used to improve output quality if present, but pandoc does not require them to be present: `upquote` (for straight quotes in verbatim environments), `microtype` (for better spacing adjustments), `parskip` (for better inter-paragraph spaces), `xurl` (for better line breaks in URLs), and `footnotehyper` or `footnote` (to allow footnotes in tables).


## Reading from the Web

Instead of an input file, an absolute URI may be given. In this case pandoc will fetch the content using HTTP:

```
pandoc -f html -t markdown https://www.fsf.org
```

It is possible to supply a custom User-Agent string or other header when requesting a document from a URL:

```
pandoc -f html -t markdown --request-header User-Agent:"Mozilla/5.0" \
  https://www.fsf.org
```

# Options


## General options

**`-f` *FORMAT*, `-r` *FORMAT*, `--from=`*FORMAT*, `--read=`*FORMAT***

Specify input format. *FORMAT* can be:

- `asciidoc` (AsciiDoc markup)
- `bibtex` (BibTeX bibliography)
- `biblatex` (BibLaTeX bibliography)
- `bits` (BITS XML, alias for `jats`)
- `commonmark` (CommonMark Markdown)
- `commonmark_x` (CommonMark Markdown with extensions)
- `creole` (Creole 1.0)
- `csljson` (CSL JSON bibliography)
- `csv` (CSV table)
- `tsv` (TSV table)
- `djot` (Djot markup)
- `docbook` (DocBook)
- `docx` (Word docx)
- `dokuwiki` (DokuWiki markup)
- `endnotexml` (EndNote XML bibliography)
- `epub` (EPUB)
- `fb2` (FictionBook2 e-book)
- `gfm` (GitHub-Flavored Markdown), or the deprecated and less accurate `markdown_github`; use `markdown_github` only if you need extensions not supported in `gfm`.
- `haddock` (Haddock markup)
- `html` (HTML)
- `ipynb` (Jupyter notebook)
- `jats` (JATS XML)
- `jira` (Jira/Confluence wiki markup)
- `json` (JSON version of native AST)
- `latex` (LaTeX)
- `markdown` (Pandoc’s Markdown)
- `markdown_mmd` (MultiMarkdown)
- `markdown_phpextra` (PHP Markdown Extra)
- `markdown_strict` (original unextended Markdown)
- `mediawiki` (MediaWiki markup)
- `man` (roff man)
- `mdoc` (mdoc manual page markup)
- `muse` (Muse)
- `native` (native Haskell)
- `odt` (OpenDocument text document)
- `opml` (OPML)
- `org` (Emacs Org mode)
- `pod` (Perl’s Plain Old Documentation)
- `pptx` (PowerPoint)
- `ris` (RIS bibliography)
- `rtf` (Rich Text Format)
- `rst` (reStructuredText)
- `t2t` (txt2tags)
- `textile` (Textile)
- `tikiwiki` (TikiWiki markup)
- `twiki` (TWiki markup)
- `typst` (typst)
- `vimwiki` (Vimwiki)
- `xlsx` (Excel spreadsheet)
- `xml` (XML version of native AST)
- the path of a custom Lua reader, see Custom readers and writers below

Extensions can be individually enabled or disabled by appending `+EXTENSION` or `-EXTENSION` to the format name. See Extensions below, for a list of extensions and their names. See `--list-input-formats` and `--list-extensions`, below.

**`-t` *FORMAT*, `-w` *FORMAT*, `--to=`*FORMAT*, `--write=`*FORMAT***

Specify output format. *FORMAT* can be:

- `ansi` (text with ANSI escape codes, for terminal viewing)
- `asciidoc` (modern AsciiDoc as interpreted by AsciiDoctor)
- `asciidoc_legacy` (AsciiDoc as interpreted by `asciidoc-py`).
- `asciidoctor` (deprecated synonym for `asciidoc`)
- `bbcode` BBCode
- `bbcode_fluxbb` BBCode (FluxBB)
- `bbcode_phpbb` BBCode (phpBB)
- `bbcode_steam` BBCode (Steam)
- `bbcode_hubzilla` BBCode (Hubzilla)
- `bbcode_xenforo` BBCode (xenForo)
- `beamer` (LaTeX beamer slide show)
- `bibtex` (BibTeX bibliography)
- `biblatex` (BibLaTeX bibliography)
- `chunkedhtml` (zip archive of multiple linked HTML files)
- `commonmark` (CommonMark Markdown)
- `commonmark_x` (CommonMark Markdown with extensions)
- `context` (ConTeXt)
- `csljson` (CSL JSON bibliography)
- `djot` (Djot markup)
- `docbook` or `docbook4` (DocBook 4)
- `docbook5` (DocBook 5)
- `docx` (Word docx)
- `dokuwiki` (DokuWiki markup)
- `epub` or `epub3` (EPUB v3 book)
- `epub2` (EPUB v2)
- `fb2` (FictionBook2 e-book)
- `gfm` (GitHub-Flavored Markdown), or the deprecated and less accurate `markdown_github`; use `markdown_github` only if you need extensions not supported in `gfm`.
- `haddock` (Haddock markup)
- `html` or `html5` (HTML, i.e. HTML5/XHTML polyglot markup)
- `html4` (XHTML 1.0 Transitional)
- `icml` (InDesign ICML)
- `ipynb` (Jupyter notebook)
- `jats_archiving` (JATS XML, Archiving and Interchange Tag Set)
- `jats_articleauthoring` (JATS XML, Article Authoring Tag Set)
- `jats_publishing` (JATS XML, Journal Publishing Tag Set)
- `jats` (alias for `jats_archiving`)
- `jira` (Jira/Confluence wiki markup)
- `json` (JSON version of native AST)
- `latex` (LaTeX)
- `man` (roff man)
- `markdown` (Pandoc’s Markdown)
- `markdown_mmd` (MultiMarkdown)
- `markdown_phpextra` (PHP Markdown Extra)
- `markdown_strict` (original unextended Markdown)
- `markua` (Markua)
- `mediawiki` (MediaWiki markup)
- `ms` (roff ms)
- `muse` (Muse)
- `native` (native Haskell)
- `odt` (OpenDocument text document)
- `opml` (OPML)
- `opendocument` (OpenDocument XML)
- `org` (Emacs Org mode)
- `pdf` (PDF)
- `plain` (plain text)
- `pptx` (PowerPoint slide show)
- `rst` (reStructuredText)
- `rtf` (Rich Text Format)
- `texinfo` (GNU Texinfo)
- `textile` (Textile)
- `slideous` (Slideous HTML and JavaScript slide show)
- `slidy` (Slidy HTML and JavaScript slide show)
- `dzslides` (DZSlides HTML5 + JavaScript slide show)
- `revealjs` (reveal.js HTML5 + JavaScript slide show)
- `s5` (S5 HTML and JavaScript slide show)
- `tei` (TEI Simple)
- `typst` (typst)
- `vimdoc` (Vimdoc)
- `xml` (XML version of native AST)
- `xwiki` (XWiki markup)
- `zimwiki` (ZimWiki markup)
- the path of a custom Lua writer, see Custom readers and writers below

Note that `odt`, `docx`, `epub`, and `pdf` output will not be directed to *stdout* unless forced with `-o -`.

Extensions can be individually enabled or disabled by appending `+EXTENSION` or `-EXTENSION` to the format name. See Extensions below, for a list of extensions and their names. See `--list-output-formats` and `--list-extensions`, below.

**`-o` *FILE*, `--output=`*FILE***

Write output to *FILE* instead of *stdout*. If *FILE* is `-`, output will go to *stdout*, even if a non-textual format (`docx`, `odt`, `epub2`, `epub3`) is specified. If the output format is `chunkedhtml` and *FILE* has no extension, then instead of producing a `.zip` file pandoc will create a directory *FILE* and unpack the zip archive there (unless *FILE* already exists, in which case an error will be raised).

**`--data-dir=`*DIRECTORY***

Specify the user data directory to search for pandoc data files. If this option is not specified, the default user data directory will be used. On *nix and macOS systems this will be the `pandoc` subdirectory of the XDG data directory (by default, `$HOME/.local/share`, overridable by setting the `XDG_DATA_HOME` environment variable). If that directory does not exist and `$HOME/.pandoc` exists, it will be used (for backwards compatibility). On Windows the default user data directory is `%APPDATA%\pandoc`. You can find the default user data directory on your system by looking at the output of `pandoc --version`. Data files placed in this directory (for example, `reference.odt`, `reference.docx`, `epub.css`, `templates`) will override pandoc’s normal defaults. (Note that the user data directory is not created by pandoc, so you will need to create it yourself if you want to make use of it.)

**`-d` *FILE*, `--defaults=`*FILE***

Specify a set of default option settings. *FILE* is a YAML or JSON file whose fields correspond to command-line option settings. All options for document conversion, including input and output files, can be set using a defaults file. The file will be searched for first in the working directory, and then in the `defaults` subdirectory of the user data directory (see `--data-dir`). The `.yaml` extension will be added if *FILE* lacs an extension. See the section Defaults files for more information on the file format. Settings from the defaults file may be overridden or extended by subsequent options on the command line.

**`--bash-completion`**

Generate a bash completion script. To enable bash completion with pandoc, add this to your `.bashrc`:

```
eval "$(pandoc --bash-completion)"
```

**`--sandbox[=true|false]`**

Run pandoc in a sandbox, limiting IO operations in readers and writers to reading the files specified on the command line. Note that this option does not limit IO operations by filters or in the production of PDF documents. But it does offer security against, for example, disclosure of files through the use of `include` directives. Anyone using pandoc on untrusted user input should use this option.

Note: some readers and writers (e.g., `docx`) need access to data files. If these are stored on the file system, then pandoc will not be able to find them when run in `--sandbox` mode and will raise an error. For these applications, we recommend using a pandoc binary compiled with the `embed_data_files` option, which causes the data files to be baked into the binary instead of being stored on the file system.

**`--verbose`**

Give verbose debugging output.

**`--quiet`**

Suppress warning messages.

**`--fail-if-warnings[=true|false]`**

Exit with error status if there are any warnings.

**`--log=`*FILE***

Write log messages in machine-readable JSON format to *FILE*. All messages above DEBUG level will be written, regardless of verbosity settings (`--verbose`, `--quiet`).

**`--list-input-formats`**

List supported input formats, one per line.

**`--list-output-formats`**

List supported output formats, one per line.

**`--list-extensions`[`=`*FORMAT*]**

List supported extensions for *FORMAT*, one per line, preceded by a `+` or `-` indicating whether it is enabled by default in *FORMAT*. If *FORMAT* is not specified, defaults for pandoc’s Markdown are given.

**`--list-highlight-languages`**

List supported languages for syntax highlighting, one per line.

**`--list-highlight-styles`**

List supported styles for syntax highlighting, one per line. See `--syntax-highlighting`.

**`-v`, `--version`**

Print version.

**`-h`, `--help`**

Show usage message.


## Reader options

**`--shift-heading-level-by=`*NUMBER***

Shift heading levels by a positive or negative integer. For example, with `--shift-heading-level-by=-1`, level 2 headings become level 1 headings, and level 3 headings become level 2 headings. Headings cannot have a level less than 1, so a heading that would be shifted below level 1 becomes a regular paragraph. Exception: with a shift of -N, a level-N heading at the beginning of the document replaces the metadata title. `--shift-heading-level-by=-1` is a good choice when converting HTML or Markdown documents that use an initial level-1 heading for the document title and level-2+ headings for sections. `--shift-heading-level-by=1` may be a good choice for converting Markdown documents that use level-1 headings for sections to HTML, since pandoc uses a level-1 heading to render the document title.

**`--base-header-level=`*NUMBER***

*Deprecated. Use `--shift-heading-level-by`=X instead, where X = NUMBER - 1.* Specify the base level for headings (defaults to 1).

**`--indented-code-classes=`*CLASSES***

Specify classes to use for indented code blocks—for example, `perl,numberLines` or `haskell`. Multiple classes may be separated by spaces or commas.

**`--default-image-extension=`*EXTENSION***

Specify a default extension to use when image paths/URLs have no extension. This allows you to use the same source for formats that require different kinds of images. Currently this option only affects the Markdown and LaTeX readers.

**`--file-scope[=true|false]`**

Parse each file individually before combining for multifile documents. This will allow footnotes in different files with the same identifiers to work as expected. If this option is set, footnotes and links will not work across files. Reading binary files (docx, odt, epub) implies `--file-scope`.

If two or more files are processed using `--file-scope`, prefixes based on the filenames will be added to identifiers in order to disambiguate them, and internal links will be adjusted accordingly. For example, a header with identifier `foo` in `subdir/file1.txt` will have its identifier changed to `subdir__file1.txt__foo`.

**`-F` *PROGRAM*, `--filter=`*PROGRAM***

Specify an executable to be used as a filter transforming the pandoc AST after the input is parsed and before the output is written. The executable should read JSON from stdin and write JSON to stdout. The JSON must be formatted like pandoc’s own JSON input and output. The name of the output format will be passed to the filter as the first argument. Hence,

```
pandoc --filter ./caps.py -t latex
```

is equivalent to

```
pandoc -t json | ./caps.py latex | pandoc -f json -t latex
```

The latter form may be useful for debugging filters.

Filters may be written in any language. `Text.Pandoc.JSON` exports `toJSONFilter` to facilitate writing filters in Haskell. Those who would prefer to write filters in python can use the module `pandocfilters`, installable from PyPI. There are also pandoc filter libraries in PHP, perl, and JavaScript/node.js.

In order of preference, pandoc will look for filters in

1. a specified full or relative path (executable or non-executable),
2. `$DATADIR/filters` (executable or non-executable) where `$DATADIR` is the user data directory (see `--data-dir`, above),
3. `$PATH` (executable only).

Filters, Lua-filters, and citeproc processing are applied in the order specified on the command line.

**`-L` *SCRIPT*, `--lua-filter=`*SCRIPT***

Transform the document in a similar fashion as JSON filters (see `--filter`), but use pandoc’s built-in Lua filtering system. The given Lua script is expected to return a list of Lua filters which will be applied in order. Each Lua filter must contain element-transforming functions indexed by the name of the AST element on which the filter function should be applied.

The `pandoc` Lua module provides helper functions for element creation. It is always loaded into the script’s Lua environment.

See the Lua filters documentation for further details.

In order of preference, pandoc will look for Lua filters in

1. a specified full or relative path,
2. `$DATADIR/filters` where `$DATADIR` is the user data directory (see `--data-dir`, above).

Filters, Lua filters, and citeproc processing are applied in the order specified on the command line.

Set the metadata field *KEY* to the value *VAL*. A value specified on the command line overrides a value specified in the document using YAML metadata blocks. Values will be parsed as YAML boolean or string values. If no value is specified, the value will be treated as Boolean true. Like `--variable`, `--metadata` causes template variables to be set. But unlike `--variable`, `--metadata` affects the metadata of the underlying document (which is accessible from filters and may be printed in some output formats) and metadata values will be escaped when inserted into the template.

Read metadata from the supplied YAML (or JSON) file. This option can be used with every input format, but string scalars in the metadata file will always be parsed as Markdown. (If the input format is Markdown or a Markdown variant, then the same variant will be used to parse the metadata file; if it is a non-Markdown format, pandoc’s default Markdown extensions will be used.) This option can be used repeatedly to include multiple metadata files; values in files specified later on the command line will be preferred over those specified in earlier files. Metadata values specified inside the document, or by using `-M`, overwrite values specified with this option. The file will be searched for first in the working directory, and then in the `metadata` subdirectory of the user data directory (see `--data-dir`).

**`-p`, `--preserve-tabs[=true|false]`**

Preserve tabs instead of converting them to spaces. (By default, pandoc converts tabs to spaces before parsing its input.) Note that this will only affect tabs in literal code spans and code blocks. Tabs in regular text are always treated as spaces.

**`--tab-stop=`*NUMBER***

Specify the number of spaces per tab (default is 4).

**`--track-changes=accept`|`reject`|`all`**

Specifies what to do with insertions, deletions, and comments produced by the MS Word “Track Changes” feature. `accept` (the default) processes all the insertions and deletions. `reject` ignores them. Both `accept` and `reject` ignore comments. `all` includes all insertions, deletions, and comments, wrapped in spans with `insertion`, `deletion`, `comment-start`, and `comment-end` classes, respectively. The author and time of change is included. `all` is useful for scripting: only accepting changes from a certain reviewer, say, or before a certain date. If a paragraph is inserted or deleted, `track-changes=all` produces a span with the class `paragraph-insertion`/`paragraph-deletion` before the affected paragraph break. This option only affects the docx reader.

**`--extract-media=`*DIR*|*FILE*`.zip`**

Extract images and other media contained in or linked from the source document to the path *DIR*, creating it if necessary, and adjust the images references in the document so they point to the extracted files. Media are downloaded, read from the file system, or extracted from a binary container (e.g. docx), as needed. The original file paths are used if they are relative paths not containing `..`. Otherwise filenames are constructed from the SHA1 hash of the contents.

If the path given ends in `.zip`, then instead of creating a directory, pandoc will create a zip archive containing the media files.

**`--abbreviations=`*FILE***

Specifies a custom abbreviations file, with abbreviations one to a line. If this option is not specified, pandoc will read the data file `abbreviations` from the user data directory or fall back on a system default. To see the system default, use `pandoc --print-default-data-file=abbreviations`. The only use pandoc makes of this list is in the Markdown reader. Strings found in this list will be followed by a nonbreaking space, and the period will not produce sentence-ending space in formats like LaTeX. The strings may not contain spaces.

**`--typst-input=`*KEY*[`=`*VAL*]**

Set a parameter value that will be made available to the typst parser in `sys.inputs`, like `--input` in the `typst` CLI. Either `:` or `=` may be used to separate *KEY* from *VAL*. Values containing spaces must be quoted.

**`--trace[=true|false]`**

Print diagnostic output tracing parser progress to stderr. This option is intended for use by developers in diagnosing performance issues.


## General writer options

**`-s`, `--standalone`**

Produce output with an appropriate header and footer (e.g. a standalone HTML, LaTeX, TEI, or RTF file, not a fragment). This option is set automatically for `pdf`, `epub`, `epub3`, `fb2`, `docx`, and `odt` output. For `native` output, this option causes metadata to be included; otherwise, metadata is suppressed.

**`--template=`*FILE*|*URL***

Use the specified file as a custom template for the generated document. Implies `--standalone`. See Templates, below, for a description of template syntax. If the template is not found, pandoc will search for it in the `templates` subdirectory of the user data directory (see `--data-dir`). If no extension is specified and an extensionless template is not found, pandoc will look for a template with an extension corresponding to the writer, so that `--template=special` looks for `special.html` for HTML output. If this option is not used, a default template appropriate for the output format will be used (see `-D/--print-default-template`).

**`-V` *KEY*[`=`*VAL*], `--variable=`*KEY*[`=`*VAL*]**

Set the template variable *KEY* to the string value *VAL* when rendering the document in standalone mode. Either `:` or `=` may be used to separate *KEY* from *VAL*. If no *VAL* is specified, the key will be given the value `true`. Structured values (lists, maps) cannot be assigned using this option, but they can be assigned in the `variables` section of a defaults file or using the `--variable-json` option. If the variable already has a *list* value, the value will be added to the list. If it already has another kind of value, it will be made into a list containing the previous and the new value. For example, `-V author=Joe -V author=Sue` makes `author` contain a list of strings: `Joe` and `Sue`.

**`--variable-json=`*KEY*[`=`*JSON*]**

Set the template variable *KEY* to the value specified by a JSON string (this may be a boolean, a string, a list, or a mapping; a number will be treated as a string). For example, `--variable-json foo=false` will give `foo` the boolean false value, while `--variable-json foo='"false"'` will give it the string value `"false"`. Either `:` or `=` may be used to separate *KEY* from *VAL*. If the variable already has a value, this value will be replaced.

**`-D` *FORMAT*, `--print-default-template=`*FORMAT***

Print the system default template for an output *FORMAT*. (See `-t` for a list of possible *FORMAT*s.) Templates in the user data directory are ignored. This option may be used with `-o`/`--output` to redirect output to a file, but `-o`/`--output` must come before `--print-default-template` on the command line.

Note that some of the default templates use partials, for example `styles.html`. To print the partials, use `--print-default-data-file`: for example, `--print-default-data-file=templates/styles.html`.

**`--print-default-data-file=`*FILE***

Print a system default data file. Files in the user data directory are ignored. This option may be used with `-o`/`--output` to redirect output to a file, but `-o`/`--output` must come before `--print-default-data-file` on the command line.

**`--eol=crlf`|`lf`|`native`**

Manually specify line endings: `crlf` (Windows), `lf` (macOS/Linux/UNIX), or `native` (line endings appropriate to the OS on which pandoc is being run). The default is `native`.

**`--dpi`=*NUMBER***

Specify the default dpi (dots per inch) value for conversion from pixels to inch/centimeters and vice versa. (Technically, the correct term would be ppi: pixels per inch.) The default is 96dpi. When images contain information about dpi internally, the encoded value is used instead of the default specified by this option.

**`--wrap=auto`|`none`|`preserve`**

Determine how text is wrapped in the output (the source code, not the rendered version). With `auto` (the default), pandoc will attempt to wrap lines to the column width specified by `--columns` (default 72). With `none`, pandoc will not wrap lines at all. With `preserve`, pandoc will attempt to preserve the wrapping from the source document (that is, where there are nonsemantic newlines in the source, there will be nonsemantic newlines in the output as well). In `ipynb` output, this option affects wrapping of the contents of Markdown cells.

**`--columns=`*NUMBER***

Specify length of lines in characters. This affects text wrapping in the generated source code (see `--wrap`). It also affects calculation of column widths for plain text tables (see Tables below).

**`--toc[=true|false]`, `--table-of-contents[=true|false]`**

Include an automatically generated table of contents (or, in the case of `latex`, `context`, `docx`, `odt`, `opendocument`, `rst`, or `ms`, an instruction to create one) in the output document. This option has no effect unless `-s/--standalone` is used, and it has no effect on `man`, `docbook4`, `docbook5`, or `jats` output.

Note that if you are producing a PDF via `ms` and using (the default) `groff` as a `--pdf-engine`, the table of contents will appear at the end of the document. If you would prefer it to be at the beginning of the document, before the title, you can use `--pdf-engine=pdfroff`.

Specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents).

**`--lof[=true|false]`, `--list-of-figures[=true|false]`**

Include an automatically generated list of figures (or, in some formats, an instruction to create one) in the output document. This option has no effect unless `-s/--standalone` is used, and it only has an effect on `latex`, `context`, and `docx` output.

**`--lot[=true|false]`, `--list-of-tables[=true|false]`**

Include an automatically generated list of tables (or, in some formats, an instruction to create one) in the output document. This option has no effect unless `-s/--standalone` is used, and it only has an effect on `latex`, `context`, and `docx` output.

**`--strip-comments[=true|false]`**

Strip out HTML comments in the Markdown or Textile source, rather than passing them on to Markdown, Textile or HTML output as raw HTML. This does not apply to HTML comments inside raw HTML blocks when the `markdown_in_html_blocks` extension is not set.

**`--syntax-highlighting=default|none|idiomatic|`*STYLE*`|`*FILE***

The method to use for code syntax highlighting. Setting a specific *STYLE* causes highlighting to be performed with the internal highlighting engine, using KDE syntax definitions and styles. The `idiomatic` method uses a format-specific highlighter if one is available, or the default style if the target format has no idiomatic highlighting method. Setting this option to `none` disables all syntax highlighting. The `default` method uses a format-specific default.

The default for HTML, EPUB, Docx, Ms, Man, and LaTeX output is to use the internal highlighter with the default style; for Typst it is to use Typst’s own syntax highlighting system.

Style options are `pygments` (the default), `kate`, `monochrome`, `breezeDark`, `espresso`, `zenburn`, `haddock`, and `tango`. For more information on syntax highlighting in pandoc, see Syntax highlighting, below. See also `--list-highlight-styles`.

Instead of a *STYLE* name, a JSON file with extension `.theme` may be supplied. This will be parsed as a KDE syntax highlighting theme and (if valid) used as the highlighting style.

To generate the JSON version of an existing style, use `--print-highlight-style`.

**`--no-highlight`**

*Deprecated, use `--syntax-highlighting=none` instead.*

Disables syntax highlighting for code blocks and inlines, even when a language attribute is given.

**`--highlight-style=`*STYLE*|*FILE***

*Deprecated, use `--syntax-highlighting=`*STYLE*|*FILE* instead.*

Specifies the coloring style to be used in highlighted source code.

**`--print-highlight-style=`*STYLE*|*FILE***

Prints a JSON version of a highlighting style, which can be modified, saved with a `.theme` extension, and used with `--syntax-highlighting`. This option may be used with `-o`/`--output` to redirect output to a file, but `-o`/`--output` must come before `--print-highlight-style` on the command line.

**`--syntax-definition=`*FILE***

Instructs pandoc to load a KDE XML syntax definition file, which will be used for syntax highlighting of appropriately marked code blocks. This can be used to add support for new languages or to use altered syntax definitions for existing languages. This option may be repeated to add multiple syntax definitions.

**`-H` *FILE*, `--include-in-header=`*FILE*|*URL***

Include contents of *FILE*, verbatim, at the end of the header. This can be used, for example, to include special CSS or JavaScript in HTML documents. This option can be used repeatedly to include multiple files in the header. They will be included in the order specified. Implies `--standalone`.

**`-B` *FILE*, `--include-before-body=`*FILE*|*URL***

Include contents of *FILE*, verbatim, at the beginning of the document body (e.g. after the `<body>` tag in HTML, or the `\begin{document}` command in LaTeX). This can be used to include navigation bars or banners in HTML documents. This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies `--standalone`. Note that if the output format is `odt`, this file must be in OpenDocument XML format suitable for insertion into the body of the document, and if the output is `docx`, this file must be in appropriate OpenXML format.

**`-A` *FILE*, `--include-after-body=`*FILE*|*URL***

Include contents of *FILE*, verbatim, at the end of the document body (before the `</body>` tag in HTML, or the `\end{document}` command in LaTeX). This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies `--standalone`. Note that if the output format is `odt`, this file must be in OpenDocument XML format suitable for insertion into the body of the document, and if the output is `docx`, this file must be in appropriate OpenXML format.

**`--resource-path=`*SEARCHPATH***

List of paths to search for images and other resources. The paths should be separated by `:` on Linux, UNIX, and macOS systems, and by `;` on Windows. If `--resource-path` is not specified, the default resource path is the working directory. Note that, if `--resource-path` is specified, the working directory must be explicitly listed or it will not be searched. For example: `--resource-path=.:test` will search the working directory and the `test` subdirectory, in that order. This option can be used repeatedly. Search path components that come later on the command line will be searched before those that come earlier, so `--resource-path foo:bar --resource-path baz:bim` is equivalent to `--resource-path baz:bim:foo:bar`. Note that this option only has an effect when pandoc itself needs to find an image (e.g., in producing a PDF or docx, or when `--embed-resources` is used.) It will not cause image paths to be rewritten in other cases (e.g., when pandoc is generating LaTeX or HTML).

**`--request-header=`*NAME*`:`*VAL***

Set the request header *NAME* to the value *VAL* when making HTTP requests (for example, when a URL is given on the command line, or when resources used in a document must be downloaded). If you’re behind a proxy, you also need to set the environment variable `http_proxy` to `http://...`.

**`--no-check-certificate[=true|false]`**

Disable the certificate verification to allow access to unsecure HTTP resources (for example when the certificate is no longer valid or self signed).
