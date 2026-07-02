---
title: "Pandoc (part 2/4)"
source: https://pandoc.org/MANUAL.html
domain: pandoc
license: CC-BY-SA-4.0
tags: pandoc converter, document conversion, markup converter, markdown to pdf
fetched: 2026-07-02
part: 2/4
---

## Options affecting specific writers

**`--self-contained[=true|false]`**

*Deprecated synonym for `--embed-resources --standalone`.*

**`--embed-resources[=true|false]`**

Produce a standalone HTML file with no external dependencies, using `data:` URIs to incorporate the contents of linked scripts, stylesheets, images, and videos. The resulting file should be “self-contained,” in the sense that it needs no external files and no net access to be displayed properly by a browser. This option works only with HTML output formats, including `html4`, `html5`, `html+lhs`, `html5+lhs`, `s5`, `slidy`, `slideous`, `dzslides`, and `revealjs`. Scripts, images, and stylesheets at absolute URLs will be downloaded; those at relative URLs will be sought relative to the working directory (if the first source file is local) or relative to the base URL (if the first source file is remote). Elements with the attribute `data-external="1"` will be left alone; the documents they link to will not be incorporated in the document. Limitation: resources that are loaded dynamically through JavaScript cannot be incorporated; as a result, fonts may be missing when `--mathjax` is used, and some advanced features (e.g. zoom or speaker notes) may not work in an offline “self-contained” `reveal.js` slide show.

For SVG images, `img` tags with `data:` URIs are used, unless the image has the class `inline-svg`, in which case an inline SVG element is inserted. This approach is recommended when there are many occurrences of the same SVG in a document, as `<use>` elements will be used to reduce duplication.

**`--link-images[=true|false]`**

Include links to images instead of embedding the images in ODT. (This option currently only affects ODT output.)

**`--html-q-tags[=true|false]`**

Use `<q>` tags for quotes in HTML. (This option only has an effect if the `smart` extension is enabled for the input format used.)

**`--ascii[=true|false]`**

Use only ASCII characters in output. Currently supported for XML and HTML formats (which use entities instead of UTF-8 when this option is selected), CommonMark, gfm, and Markdown (which use entities), roff man and ms (which use hexadecimal escapes), and to a limited degree LaTeX (which uses standard commands for accented characters when possible).

**`--reference-links[=true|false]`**

Use reference-style links, rather than inline links, in writing Markdown or reStructuredText. By default inline links are used. The placement of link references is affected by the `--reference-location` option.

**`--reference-location=block`|`section`|`document`**

Specify whether footnotes (and references, if `reference-links` is set) are placed at the end of the current (top-level) block, the current section, or the document. The default is `document`. Currently this option only affects the `markdown`, `muse`, `html`, `epub`, `slidy`, `s5`, `slideous`, `dzslides`, and `revealjs` writers. In slide formats, specifying `--reference-location=section` will cause notes to be rendered at the bottom of a slide.

**`--figure-caption-position=above`|`below`**

Specify whether figure captions go above or below figures (default is `below`). This option only affects HTML, LaTeX, Docx, ODT, and Typst output.

**`--table-caption-position=above`|`below`**

Specify whether table captions go above or below tables (default is `above`). This option only affects HTML, LaTeX, Docx, ODT, and Typst output.

**`--markdown-headings=setext`|`atx`**

Specify whether to use ATX-style (`#`-prefixed) or Setext-style (underlined) headings for level 1 and 2 headings in Markdown output. (The default is `atx`.) ATX-style headings are always used for levels 3+. This option also affects Markdown cells in `ipynb` output.

**`--list-tables[=true|false]`**

Render tables as list tables in RST output.

**`--top-level-division=default`|`section`|`chapter`|`part`**

Treat top-level headings as the given division type in LaTeX, ConTeXt, DocBook, and TEI output. The hierarchy order is part, chapter, then section; all headings are shifted such that the top-level heading becomes the specified type. The default behavior is to determine the best division type via heuristics: unless other conditions apply, `section` is chosen. When the `documentclass` variable is set to `report`, `book`, or `memoir` (unless the `article` option is specified), `chapter` is implied as the setting for this option. If `beamer` is the output format, specifying either `chapter` or `part` will cause top-level headings to become `\part{..}`, while second-level headings remain as their default type.

In Docx output, this option adds section breaks before first-level headings if `chapter` is selected, and before first- and second-level headings if `part` is selected. Footnote numbers will restart with each section break unless the reference doc modifies this.

**`-N`, `--number-sections=[true|false]`**

Number section headings in LaTeX, ConTeXt, HTML, Docx, ms, or EPUB output. By default, sections are not numbered. Sections with class `unnumbered` will never be numbered, even if `--number-sections` is specified.

**`--number-offset=`*NUMBER*[`,`*NUMBER*`,`*…*]**

Offsets for section heading numbers. The first number is added to the section number for level-1 headings, the second for level-2 headings, and so on. So, for example, if you want the first level-1 heading in your document to be numbered “6” instead of “1”, specify `--number-offset=5`. If your document starts with a level-2 heading which you want to be numbered “1.5”, specify `--number-offset=1,4`. `--number-offset` only directly affects the number of the first section heading in a document; subsequent numbers increment in the normal way. Implies `--number-sections`. Currently this feature only affects HTML and Docx output.

**`--listings[=true|false]`**

*Deprecated, use `--syntax-highlighting=idiomatic` or `--syntax-highlighting=default` instead.

Use the `listings` package for LaTeX code blocks. The package does not support multi-byte encoding for source code. To handle UTF-8 you would need to use a custom template. This issue is fully documented here: Encoding issue with the listings package.

**`-i`, `--incremental[=true|false]`**

Make list items in slide shows display incrementally (one by one). The default is for lists to be displayed all at once.

**`--slide-level=`*NUMBER***

Specifies that headings with the specified level create slides (for `beamer`, `revealjs`, `pptx`, `s5`, `slidy`, `slideous`, `dzslides`). Headings above this level in the hierarchy are used to divide the slide show into sections; headings below this level create subheads within a slide. Valid values are 0-6. If a slide level of 0 is specified, slides will not be split automatically on headings, and horizontal rules must be used to indicate slide boundaries. If a slide level is not specified explicitly, the slide level will be set automatically based on the contents of the document; see Structuring the slide show.

**`--section-divs[=true|false]`**

Wrap sections in `<section>` tags (or `<div>` tags for `html4`), and attach identifiers to the enclosing `<section>` (or `<div>`) rather than the heading itself (see Heading identifiers, below). This option only affects HTML output (and does not affect HTML slide formats).

**`--email-obfuscation=none`|`javascript`|`references`**

Specify a method for obfuscating `mailto:` links in HTML documents. `none` leaves `mailto:` links as they are. `javascript` obfuscates them using JavaScript. `references` obfuscates them by printing their letters as decimal or hexadecimal character references. The default is `none`.

**`--id-prefix=`*STRING***

Specify a prefix to be added to all identifiers and internal links in HTML and DocBook output, and to footnote numbers in Markdown and Haddock output. This is useful for preventing duplicate identifiers when generating fragments to be included in other pages.

**`-T` *STRING*, `--title-prefix=`*STRING***

Specify *STRING* as a prefix at the beginning of the title that appears in the HTML header (but not in the title as it appears at the beginning of the HTML body). Implies `--standalone`.

**`-c` *URL*, `--css=`*URL***

Link to a CSS style sheet. This option can be used repeatedly to include multiple files. They will be included in the order specified. This option only affects HTML (including HTML slide shows) and EPUB output. It should be used together with `-s/--standalone`, because the link to the stylesheet goes in the document header.

A stylesheet is required for generating EPUB. If none is provided using this option (or the `css` or `stylesheet` metadata fields), pandoc will look for a file `epub.css` in the user data directory (see `--data-dir`). If it is not found there, sensible defaults will be used.

**`--reference-doc=`*FILE*|*URL***

Use the specified file as a style reference in producing a docx or ODT file.

**Docx**

For best results, the reference docx should be a modified version of a docx file produced using pandoc. The contents of the reference docx are ignored, but its stylesheets and document properties (including margins, page size, header, and footer) are used in the new docx. If no reference docx is specified on the command line, pandoc will look for a file `reference.docx` in the user data directory (see `--data-dir`). If this is not found either, sensible defaults will be used.

To produce a custom `reference.docx`, first get a copy of the default `reference.docx`: `pandoc -o custom-reference.docx --print-default-data-file reference.docx`. Then open `custom-reference.docx` in Word or LibreOffice, modify the styles as you wish, and save the file. For best results, do not make changes to this file other than modifying the styles used by pandoc:

Paragraph styles:

- Normal
- Body Text
- First Paragraph
- Compact
- Title
- Subtitle
- Author
- Date
- Abstract
- AbstractTitle
- Bibliography
- Heading 1
- Heading 2
- Heading 3
- Heading 4
- Heading 5
- Heading 6
- Heading 7
- Heading 8
- Heading 9
- Block Text [for block quotes]
- Footnote Block Text [for block quotes in footnotes]
- Source Code
- Footnote Text
- Definition Term
- Definition
- Caption
- Table Caption
- Image Caption
- Figure
- Captioned Figure
- TOC Heading

Character styles:

- Default Paragraph Font
- Verbatim Char
- Footnote Reference
- Hyperlink
- Section Number

Table style:

- Table

**ODT**

For best results, the reference ODT should be a modified version of an ODT produced using pandoc. The contents of the reference ODT are ignored, but its stylesheets are used in the new ODT. If no reference ODT is specified on the command line, pandoc will look for a file `reference.odt` in the user data directory (see `--data-dir`). If this is not found either, sensible defaults will be used.

To produce a custom `reference.odt`, first get a copy of the default `reference.odt`: `pandoc -o custom-reference.odt --print-default-data-file reference.odt`. Then open `custom-reference.odt` in LibreOffice, modify the styles as you wish, and save the file.

**PowerPoint**

Templates included with Microsoft PowerPoint 2013 (either with `.pptx` or `.potx` extension) are known to work, as are most templates derived from these.

The specific requirement is that the template should contain layouts with the following names (as seen within PowerPoint):

- Title Slide
- Title and Content
- Section Header
- Two Content
- Comparison
- Content with Caption
- Blank

For each name, the first layout found with that name will be used. If no layout is found with one of the names, pandoc will output a warning and use the layout with that name from the default reference doc instead. (How these layouts are used is described in PowerPoint layout choice.)

All templates included with a recent version of MS PowerPoint will fit these criteria. (You can click on `Layout` under the `Home` menu to check.)

You can also modify the default `reference.pptx`: first run `pandoc -o custom-reference.pptx --print-default-data-file reference.pptx`, and then modify `custom-reference.pptx` in MS PowerPoint (pandoc will use the layouts with the names listed above).

**`--split-level=`*NUMBER***

Specify the heading level at which to split an EPUB or chunked HTML document into separate files. The default is to split into chapters at level-1 headings. In the case of EPUB, this option only affects the internal composition of the EPUB, not the way chapters and sections are displayed to users. Some readers may be slow if the chapter files are too large, so for large documents with few level-1 headings, one might want to use a chapter level of 2 or 3. For chunked HTML, this option determines how much content goes in each “chunk.”

**`--chunk-template=`*PATHTEMPLATE***

Specify a template for the filenames in a `chunkedhtml` document. In the template, `%n` will be replaced by the chunk number (padded with leading 0s to 3 digits), `%s` with the section number of the chunk, `%h` with the heading text (with formatting removed), `%i` with the section identifier. For example, `section-%s-%i.html` might be resolved to `section-1.1-introduction.html`. The characters `/` and `\` are not allowed in chunk templates and will be ignored. The default is `%s-%i.html`.

**`--epub-chapter-level=`*NUMBER***

*Deprecated synonym for `--split-level`.*

**`--epub-cover-image=`*FILE***

Use the specified image as the EPUB cover. It is recommended that the image be less than 1000px in width and height. Note that in a Markdown source document you can also specify `cover-image` in a YAML metadata block (see EPUB Metadata, below).

**`--epub-title-page=true`|`false`**

Determines whether a the title page is included in the EPUB (default is `true`).

Look in the specified XML file for metadata for the EPUB. The file should contain a series of Dublin Core elements. For example:

```
 <dc:rights>Creative Commons</dc:rights>
 <dc:language>es-AR</dc:language>
```

By default, pandoc will include the following metadata elements: `<dc:title>` (from the document title), `<dc:creator>` (from the document authors), `<dc:date>` (from the document date, which should be in ISO 8601 format), `<dc:language>` (from the `lang` variable, or, if is not set, the locale), and `<dc:identifier id="BookId">` (a randomly generated UUID). Any of these may be overridden by elements in the metadata file.

Note: if the source document is Markdown, a YAML metadata block in the document can be used instead. See below under EPUB Metadata.

**`--epub-embed-font=`*FILE***

Embed the specified font in the EPUB. This option can be repeated to embed multiple fonts. Wildcards can also be used: for example, `DejaVuSans-*.ttf`. However, if you use wildcards on the command line, be sure to escape them or put the whole filename in single quotes, to prevent them from being interpreted by the shell. To use the embedded fonts, you will need to add declarations like the following to your CSS (see `--css`):

```
@font-face {
   font-family: DejaVuSans;
   font-style: normal;
   font-weight: normal;
   src:url("../fonts/DejaVuSans-Regular.ttf");
}
@font-face {
   font-family: DejaVuSans;
   font-style: normal;
   font-weight: bold;
   src:url("../fonts/DejaVuSans-Bold.ttf");
}
@font-face {
   font-family: DejaVuSans;
   font-style: italic;
   font-weight: normal;
   src:url("../fonts/DejaVuSans-Oblique.ttf");
}
@font-face {
   font-family: DejaVuSans;
   font-style: italic;
   font-weight: bold;
   src:url("../fonts/DejaVuSans-BoldOblique.ttf");
}
body { font-family: "DejaVuSans"; }
```

**`--epub-subdirectory=`*DIRNAME***

Specify the subdirectory in the OCF container that is to hold the EPUB-specific contents. The default is `EPUB`. To put the EPUB contents in the top level, use an empty string.

**`--ipynb-output=all|none|best`**

Determines how ipynb output cells are treated. `all` means that all of the data formats included in the original are preserved. `none` means that the contents of data cells are omitted. `best` causes pandoc to try to pick the richest data block in each output cell that is compatible with the output format. The default is `best`.

**`--pdf-engine=`*PROGRAM***

Use the specified engine when producing PDF output. Valid values are `pdflatex`, `lualatex`, `xelatex`, `latexmk`, `tectonic`, `wkhtmltopdf`, `weasyprint`, `pagedjs-cli`, `prince`, `context`, `groff`, `pdfroff`, and `typst`. If the engine is not in your PATH, the full path of the engine may be specified here. If this option is not specified, pandoc uses the following defaults depending on the output format specified using `-t/--to`:

- `-t latex` or none: `pdflatex` (other options: `xelatex`, `lualatex`, `tectonic`, `latexmk`)
- `-t context`: `context`
- `-t html`: `weasyprint` (other options: `prince`, `wkhtmltopdf`, `pagedjs-cli`; see print-css.rocks for a good introduction to PDF generation from HTML/CSS)
- `-t ms`: `groff`
- `-t typst`: `typst`

This option is normally intended to be used when a PDF file is specified as `-o/--output`. However, it may still have an effect when other output formats are requested. For example, `ms` output will include `.pdfhref` macros only if a `--pdf-engine` is selected, and the macros will be differently encoded depending on whether `groff` or `pdfroff` is specified.

**`--pdf-engine-opt=`*STRING***

Use the given string as a command-line argument to the `pdf-engine`. For example, to use a persistent directory `foo` for `latexmk`’s auxiliary files, use `--pdf-engine-opt=-outdir=foo`. Note that no check for duplicate options is done.


## Citation rendering

**`-C`, `--citeproc`**

Process the citations in the file, replacing them with rendered citations and adding a bibliography. Citation processing will not take place unless bibliographic data is supplied, either through an external file specified using the `--bibliography` option or the `bibliography` field in metadata, or via a `references` section in metadata containing a list of citations in CSL YAML format with Markdown formatting. The style is controlled by a CSL stylesheet specified using the `--csl` option or the `csl` field in metadata. (If no stylesheet is specified, the `chicago-author-date` style will be used by default.) The citation processing transformation may be applied before or after filters or Lua filters (see `--filter`, `--lua-filter`): these transformations are applied in the order they appear on the command line. For more information, see the section on Citations.

Note: if this option is specified, the `citations` extension will be disabled automatically in the writer, to ensure that the citeproc-generated citations will be rendered instead of the format’s own citation syntax.

**`--bibliography=`*FILE***

Set the `bibliography` field in the document’s metadata to *FILE*, overriding any value set in the metadata. If you supply this argument multiple times, each *FILE* will be added to bibliography. If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see `--resource-path`).

**`--csl=`*FILE***

Set the `csl` field in the document’s metadata to *FILE*, overriding any value set in the metadata. (This is equivalent to `--metadata csl=FILE`.) If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see `--resource-path`) and finally in the `csl` subdirectory of the pandoc user data directory.

**`--citation-abbreviations=`*FILE***

Set the `citation-abbreviations` field in the document’s metadata to *FILE*, overriding any value set in the metadata. (This is equivalent to `--metadata citation-abbreviations=FILE`.) If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see `--resource-path`) and finally in the `csl` subdirectory of the pandoc user data directory.

**`--natbib`**

Use `natbib` for citations in LaTeX output. This option is not for use with the `--citeproc` option or with PDF output. It is intended for use in producing a LaTeX file that can be processed with `bibtex`.

**`--biblatex`**

Use `biblatex` for citations in LaTeX output. This option is not for use with the `--citeproc` option or with PDF output. It is intended for use in producing a LaTeX file that can be processed with `bibtex` or `biber`.


## Math rendering in HTML

The default is to render TeX math as far as possible using Unicode characters. Formulas are put inside a `span` with `class="math"`, so that they may be styled differently from the surrounding text if needed. However, this gives acceptable results only for basic math, usually you will want to use `--mathjax` or another of the following options.

**`--mathjax`[`=`*URL*]**

Use MathJax to display embedded TeX math in HTML output. TeX math will be put between `\(...\)` (for inline math) or `\[...\]` (for display math) and wrapped in `<span>` tags with class `math`. Then the MathJax JavaScript will render it. The *URL* should point to the `MathJax.js` load script. If a *URL* is not provided, a link to the Cloudflare CDN will be inserted.

**`--mathml`**

Convert TeX math to MathML (in `epub3`, `docbook4`, `docbook5`, `jats`, `html4` and `html5`). This is the default in `odt` output. MathML is supported natively by the main web browsers and select e-book readers.

**`--webtex`[`=`*URL*]**

Convert TeX formulas to `<img>` tags that link to an external script that converts formulas to images. The formula will be URL-encoded and concatenated with the URL provided. For SVG images you can for example use `--webtex https://latex.codecogs.com/svg.latex?`. If no URL is specified, the CodeCogs URL generating PNGs will be used (`https://latex.codecogs.com/png.latex?`). Note: the `--webtex` option will affect Markdown output as well as HTML, which is useful if you’re targeting a version of Markdown without native math support.

**`--katex`[`=`*URL*]**

Use KaTeX to display embedded TeX math in HTML output. The *URL* is the base URL for the KaTeX library. That directory should contain a `katex.min.js` and a `katex.min.css` file. If a *URL* is not provided, a link to the KaTeX CDN will be inserted.

**`--gladtex`**

Enclose TeX math in `<eq>` tags in HTML output. The resulting HTML can then be processed by GladTeX to produce SVG images of the typeset formulas and an HTML file with these images embedded.

```
pandoc -s --gladtex input.md -o myfile.htex
gladtex -d image_dir myfile.htex
# produces myfile.html and images in image_dir
```


## Options for wrapper scripts

**`--dump-args[=true|false]`**

Print information about command-line arguments to *stdout*, then exit. This option is intended primarily for use in wrapper scripts. The first line of output contains the name of the output file specified with the `-o` option, or `-` (for *stdout*) if no output file was specified. The remaining lines contain the command-line arguments, one per line, in the order they appear. These do not include regular pandoc options and their arguments, but do include any options appearing after a `--` separator at the end of the line.

**`--ignore-args[=true|false]`**

Ignore command-line arguments (for use in wrapper scripts). Regular pandoc options are not ignored. Thus, for example,

```
pandoc --ignore-args -o foo.html -s foo.txt -- -e latin1
```

is equivalent to

```
pandoc -o foo.html -s
```

# Exit codes

If pandoc completes successfully, it will return exit code 0. Nonzero exit codes have the following meanings:

| Code | Error |
|---|---|
| 1 | PandocIOError |
| 3 | PandocFailOnWarningError |
| 4 | PandocAppError |
| 5 | PandocTemplateError |
| 6 | PandocOptionError |
| 21 | PandocUnknownReaderError |
| 22 | PandocUnknownWriterError |
| 23 | PandocUnsupportedExtensionError |
| 24 | PandocCiteprocError |
| 25 | PandocBibliographyError |
| 31 | PandocEpubSubdirectoryError |
| 43 | PandocPDFError |
| 44 | PandocXMLError |
| 47 | PandocPDFProgramNotFoundError |
| 61 | PandocHttpError |
| 62 | PandocShouldNeverHappenError |
| 63 | PandocSomeError |
| 64 | PandocParseError |
| 66 | PandocMakePDFError |
| 67 | PandocSyntaxMapError |
| 83 | PandocFilterError |
| 84 | PandocLuaError |
| 89 | PandocNoScriptingEngine |
| 91 | PandocMacroLoop |
| 92 | PandocUTF8DecodingError |
| 93 | PandocIpynbDecodingError |
| 94 | PandocUnsupportedCharsetError |
| 95 | PandocInputNotTextError |
| 97 | PandocCouldNotFindDataFileError |
| 98 | PandocCouldNotFindMetadataFileError |
| 99 | PandocResourceNotFound |

# Defaults files

The `--defaults` option may be used to specify a package of options, in the form of a YAML or JSON file. Examples in this section will be given in YAML, but the equivalent forms in JSON will also work.

Fields that are omitted will just have their regular default values. So a defaults file can be as simple as one line:

```
verbosity: INFO
```

or in JSON:

```
{ "verbosity": "INFO" }
```

In fields that expect a file path (or list of file paths), the following syntax may be used to interpolate environment variables:

```
csl:  ${HOME}/mycsldir/special.csl
```

`${USERDATA}` may also be used; this will always resolve to the user data directory that is current when the defaults file is parsed, regardless of the setting of the environment variable `USERDATA`.

`${.}` will resolve to the directory containing the defaults file itself. This allows you to refer to resources contained in that directory:

```
epub-cover-image: ${.}/cover.jpg
epub-metadata: ${.}/meta.xml
resource-path:
- .             # the working directory from which pandoc is run
- ${.}/images   # the images subdirectory of the directory
                # containing this defaults file
```

This environment variable interpolation syntax *only* works in fields that expect file paths.

Defaults files can be placed in the `defaults` subdirectory of the user data directory and used from any directory. For example, one could create a file specifying defaults for writing letters, save it as `letter.yaml` in the `defaults` subdirectory of the user data directory, and then invoke these defaults from any directory using `pandoc --defaults letter` or `pandoc -dletter`.

When multiple defaults are used, their contents will be combined.

Note that, where command-line arguments may be repeated (`--metadata-file`, `--css`, `--include-in-header`, `--include-before-body`, `--include-after-body`, `--variable`, `--metadata`, `--syntax-definition`), the values specified on the command line will combine with values specified in the defaults file, rather than replacing them.

The following tables show the mapping between the command line and defaults file entries.

| command line | defaults file |
|---|---|
| `foo.md` | `input-file: foo.md` |
| `foo.md bar.md` | `input-files: - foo.md - bar.md` |

The value of `input-files` may be left empty to indicate input from stdin, and it can be an empty sequence `[]` for no input.


## General options

| command line | defaults file |
|---|---|
| `--from markdown+emoji` | `from: markdown+emoji` `reader: markdown+emoji` |
| `--to markdown+hard_line_breaks` | `to: markdown+hard_line_breaks` `writer: markdown+hard_line_breaks` |
| `--output foo.pdf` | `output-file: foo.pdf` |
| `--output -` | `output-file:` |
| `--data-dir dir` | `data-dir: dir` |
| `--defaults file` | `defaults: - file` |
| `--verbose` | `verbosity: INFO` |
| `--quiet` | `verbosity: ERROR` |
| `--fail-if-warnings` | `fail-if-warnings: true` |
| `--sandbox` | `sandbox: true` |
| `--log=FILE` | `log-file: FILE` |

Options specified in a defaults file itself always have priority over those in another file included with a `defaults:` entry.

`verbosity` can have the values `ERROR`, `WARNING`, or `INFO`.


## Reader options

| command line | defaults file |
|---|---|
| `--shift-heading-level-by -1` | `shift-heading-level-by: -1` |
| `--indented-code-classes python` | `indented-code-classes: - python` |
| `--default-image-extension ".jpg"` | `default-image-extension: '.jpg'` |
| `--file-scope` | `file-scope: true` |
| `--citeproc \ --lua-filter count-words.lua \ --filter special.lua` | `filters: - citeproc - count-words.lua - type: json path: special.lua` |
| `--metadata key=value \ --metadata key2` | `metadata: key: value key2: true` |
| `--metadata-file meta.yaml` | `metadata-files: - meta.yaml` `metadata-file: meta.yaml` |
| `--preserve-tabs` | `preserve-tabs: true` |
| `--tab-stop 8` | `tab-stop: 8` |
| `--track-changes accept` | `track-changes: accept` |
| `--extract-media dir` | `extract-media: dir` |
| `--abbreviations abbrevs.txt` | `abbreviations: abbrevs.txt` |
| `--typst-input foo=bar` | `typst-inputs: foo: bar` |
| `--trace` | `trace: true` |

Metadata values specified in a defaults file are parsed as literal string text, not Markdown.

Filters will be assumed to be Lua filters if they have the `.lua` extension, and JSON filters otherwise. But the filter type can also be specified explicitly, as shown. Filters are run in the order specified. To include the built-in citeproc filter, use either `citeproc` or `{type: citeproc}`.


## General writer options

| command line | defaults file |
|---|---|
| `--standalone` | `standalone: true` |
| `--template letter` | `template: letter` |
| `--variable key=val \ --variable key2` | `variables: key: val key2: true` |
| `--eol nl` | `eol: nl` |
| `--dpi 300` | `dpi: 300` |
| `--wrap preserve` | `wrap: "preserve"` |
| `--columns 72` | `columns: 72` |
| `--table-of-contents` | `table-of-contents: true` |
| `--toc` | `toc: true` |
| `--toc-depth 3` | `toc-depth: 3` |
| `--strip-comments` | `strip-comments: true` |
| `--no-highlight` | `syntax-highlighting: 'none'` |
| `--syntax-highlighting kate` | `syntax-highlighting: kate` |
| `--syntax-definition mylang.xml` | `syntax-definitions: - mylang.xml` `syntax-definition: mylang.xml` |
| `--include-in-header inc.tex` | `include-in-header: - inc.tex` |
| `--include-before-body inc.tex` | `include-before-body: - inc.tex` |
| `--include-after-body inc.tex` | `include-after-body: - inc.tex` |
| `--resource-path .:foo` | `resource-path: ['.','foo']` |
| `--request-header foo:bar` | `request-headers: - ["User-Agent", "Mozilla/5.0"]` |
| `--no-check-certificate` | `no-check-certificate: true` |


## Options affecting specific writers

| command line | defaults file |
|---|---|
| `--self-contained` | `self-contained: true` |
| `--link-images` | `link-images: true` |
| `--html-q-tags` | `html-q-tags: true` |
| `--ascii` | `ascii: true` |
| `--reference-links` | `reference-links: true` |
| `--reference-location block` | `reference-location: block` |
| `--figure-caption-position=above` | `figure-caption-position: above` |
| `--table-caption-position=below` | `table-caption-position: below` |
| `--markdown-headings atx` | `markdown-headings: atx` |
| `--list-tables` | `list-tables: true` |
| `--top-level-division chapter` | `top-level-division: chapter` |
| `--number-sections` | `number-sections: true` |
| `--number-offset=1,4` | `number-offset: \[1,4\]` |
| `--listings` | `listings: true` |
| `--list-of-figures` | `list-of-figures: true` |
| `--lof` | `lof: true` |
| `--list-of-tables` | `list-of-tables: true` |
| `--lot` | `lot: true` |
| `--incremental` | `incremental: true` |
| `--slide-level 2` | `slide-level: 2` |
| `--section-divs` | `section-divs: true` |
| `--email-obfuscation references` | `email-obfuscation: references` |
| `--id-prefix ch1` | `identifier-prefix: ch1` |
| `--title-prefix MySite` | `title-prefix: MySite` |
| `--css styles/screen.css \ --css styles/special.css` | `css: - styles/screen.css - styles/special.css` |
| `--reference-doc my.docx` | `reference-doc: my.docx` |
| `--epub-cover-image cover.jpg` | `epub-cover-image: cover.jpg` |
| `--epub-title-page=false` | `epub-title-page: false` |
| `--epub-metadata meta.xml` | `epub-metadata: meta.xml` |
| `--epub-embed-font special.otf \ --epub-embed-font headline.otf` | `epub-fonts: - special.otf - headline.otf` |
| `--split-level 2` | `split-level: 2` |
| `--chunk-template="%i.html"` | `chunk-template: "%i.html"` |
| `--epub-subdirectory=""` | `epub-subdirectory: ''` |
| `--ipynb-output best` | `ipynb-output: best` |
| `--pdf-engine xelatex` | `pdf-engine: xelatex` |
| `--pdf-engine-opt=--shell-escape` | `pdf-engine-opts: - '-shell-escape'` `pdf-engine-opt: '-shell-escape'` |


## Citation rendering

| command line | defaults file |
|---|---|
| `--citeproc` | `citeproc: true` |
| `--bibliography logic.bib` | `bibliography: logic.bib` |
| `--csl ieee.csl` | `csl: ieee.csl` |
| `--citation-abbreviations ab.json` | `citation-abbreviations: ab.json` |
| `--natbib` | `cite-method: natbib` |
| `--biblatex` | `cite-method: biblatex` |

`cite-method` can be `citeproc`, `natbib`, or `biblatex`. This only affects LaTeX output. If you want to use citeproc to format citations, you should also set ‘citeproc: true’.

If you need control over when the citeproc processing is done relative to other filters, you should instead use `citeproc` in the list of `filters` (see Reader options).


## Math rendering in HTML

| command line | defaults file |
|---|---|
| `--mathjax` | `html-math-method: method: mathjax` |
| `--mathml` | `html-math-method: method: mathml` |
| `--webtex` | `html-math-method: method: webtex` |
| `--katex` | `html-math-method: method: katex` |
| `--gladtex` | `html-math-method: method: gladtex` |

In addition to the values listed above, `method` can have the value `plain`.

If the command line option accepts a URL argument, an `url:` field can be added to `html-math-method:`.


## Options for wrapper scripts

| command line | defaults file |
|---|---|
| `--dump-args` | `dump-args: true` |
| `--ignore-args` | `ignore-args: true` |

# Templates

When the `-s/--standalone` option is used, pandoc uses a template to add header and footer material that is needed for a self-standing document. To see the default template that is used, just type

```
pandoc -D *FORMAT*
```

where *FORMAT* is the name of the output format. A custom template can be specified using the `--template` option. You can also override the system default templates for a given output format *FORMAT* by putting a file `templates/default.*FORMAT*` in the user data directory (see `--data-dir`, above). *Exceptions:*

- For `odt` output, customize the `default.opendocument` template.
- For `docx` output, customize the `default.openxml` template.
- For `pdf` output, customize the `default.latex` template (or the `default.context` template, if you use `-t context`, or the `default.ms` template, if you use `-t ms`, or the `default.html` template, if you use `-t html`).
- `pptx` has no template.

Note that `docx`, `odt`, and `pptx` output can also be customized using `--reference-doc`. Use a reference doc to adjust the styles in your document; use a template to handle variable interpolation and customize the presentation of metadata, the position of the table of contents, boilerplate text, etc.

Templates contain *variables*, which allow for the inclusion of arbitrary information at any point in the file. They may be set at the command line using the `-V/--variable` option. If a variable is not set, pandoc will look for the key in the document’s metadata, which can be set using either YAML metadata blocks or with the `-M/--metadata` option. In addition, some variables are given default values by pandoc. See Variables below for a list of variables used in pandoc’s default templates.

If you use custom templates, you may need to revise them as pandoc changes. We recommend tracking the changes in the default templates, and modifying your custom templates accordingly. An easy way to do this is to fork the pandoc-templates repository and merge in changes after each pandoc release.


## Template syntax

### Delimiters

To mark variables and control structures in the template, either `$`…`$` or `${`…`}` may be used as delimiters. The styles may also be mixed in the same template, but the opening and closing delimiter must match in each case. The opening delimiter may be followed by one or more spaces or tabs, which will be ignored. The closing delimiter may be preceded by one or more spaces or tabs, which will be ignored.

To include a literal `$` in the document, use `$$`.

### Interpolated variables

A slot for an interpolated variable is a variable name surrounded by matched delimiters. Variable names must begin with a letter and can contain letters, numbers, `_`, `-`, and `.`. The keywords `it`, `if`, `else`, `endif`, `for`, `sep`, and `endfor` may not be used as variable names. Examples:

```
$foo$
$foo.bar.baz$
$foo_bar.baz-bim$
$ foo $
${foo}
${foo.bar.baz}
${foo_bar.baz-bim}
${ foo }
```

Variable names with periods are used to get at structured variable values. So, for example, `employee.salary` will return the value of the `salary` field of the object that is the value of the `employee` field.

- If the value of the variable is a simple value, it will be rendered verbatim. (Note that no escaping is done; the assumption is that the calling program will escape the strings appropriately for the output format.)
- If the value is a list, the values will be concatenated.
- If the value is a map, the string `true` will be rendered.
- Every other value will be rendered as the empty string.

### Conditionals

A conditional begins with `if(variable)` (enclosed in matched delimiters) and ends with `endif` (enclosed in matched delimiters). It may optionally contain an `else` (enclosed in matched delimiters). The `if` section is used if `variable` has a true value, otherwise the `else` section is used (if present). The following values count as true:

- any map
- any array containing at least one true value
- any nonempty string
- boolean True

Note that in YAML metadata (and metadata specified on the command line using `-M/--metadata`), unquoted `true` and `false` will be interpreted as Boolean values. But a variable specified on the command line using `-V/--variable` will always be given a string value. Hence a conditional `if(foo)` will be triggered if you use `-V foo=false`, but not if you use `-M foo=false`.

Examples:

```
$if(foo)$bar$endif$

$if(foo)$
  $foo$
$endif$

$if(foo)$
part one
$else$
part two
$endif$

${if(foo)}bar${endif}

${if(foo)}
  ${foo}
${endif}

${if(foo)}
${ foo.bar }
${else}
no foo!
${endif}
```

The keyword `elseif` may be used to simplify complex nested conditionals:

```
$if(foo)$
XXX
$elseif(bar)$
YYY
$else$
ZZZ
$endif$
```

### For loops

A for loop begins with `for(variable)` (enclosed in matched delimiters) and ends with `endfor` (enclosed in matched delimiters).

- If `variable` is an array, the material inside the loop will be evaluated repeatedly, with `variable` being set to each value of the array in turn, and concatenated.
- If `variable` is a map, the material inside will be set to the map.
- If the value of the associated variable is not an array or a map, a single iteration will be performed on its value.

Examples:

```
$for(foo)$$foo$$sep$, $endfor$

$for(foo)$
  - $foo.last$, $foo.first$
$endfor$

${ for(foo.bar) }
  - ${ foo.bar.last }, ${ foo.bar.first }
${ endfor }

$for(mymap)$
$it.name$: $it.office$
$endfor$
```

You may optionally specify a separator between consecutive values using `sep` (enclosed in matched delimiters). The material between `sep` and the `endfor` is the separator.

```
${ for(foo) }${ foo }${ sep }, ${ endfor }
```

Instead of using `variable` inside the loop, the special anaphoric keyword `it` may be used.

```
${ for(foo.bar) }
  - ${ it.last }, ${ it.first }
${ endfor }
```

### Partials

Partials (subtemplates stored in different files) may be included by using the name of the partial, followed by `()`, for example:

```
${ styles() }
```

Partials will be sought in the directory containing the main template. The file name will be assumed to have the same extension as the main template if it lacks an extension. When calling the partial, the full name including file extension can also be used:

```
${ styles.html() }
```

(If a partial is not found in the directory of the template and the template path is given as a relative path, it will also be sought in the `templates` subdirectory of the user data directory.)

Partials may optionally be applied to variables using a colon:

```
${ date:fancy() }

${ articles:bibentry() }
```

If `articles` is an array, this will iterate over its values, applying the partial `bibentry()` to each one. So the second example above is equivalent to

```
${ for(articles) }
${ it:bibentry() }
${ endfor }
```

Note that the anaphoric keyword `it` must be used when iterating over partials. In the above examples, the `bibentry` partial should contain `it.title` (and so on) instead of `articles.title`.

Final newlines are omitted from included partials.

Partials may include other partials.

A separator between values of an array may be specified in square brackets, immediately after the variable name or partial:

```
${months[, ]}

${articles:bibentry()[; ]}
```

The separator in this case is literal and (unlike with `sep` in an explicit `for` loop) cannot contain interpolated variables or other template directives.

### Nesting

To ensure that content is “nested,” that is, subsequent lines indented, use the `^` directive:

```
$item.number$  $^$$item.description$ ($item.price$)
```

In this example, if `item.description` has multiple lines, they will all be indented to line up with the first line:

```
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
```

To nest multiple lines to the same level, align them with the `^` directive in the template. For example:

```
$item.number$  $^$$item.description$ ($item.price$)
               (Available til $item.sellby$.)
```

will produce

```
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
       (Available til March 30, 2020.)
```

If a variable occurs by itself on a line, preceded by whitespace and not followed by further text or directives on the same line, and the variable’s value contains multiple lines, it will be nested automatically.

### Breakable spaces

Normally, spaces in the template itself (as opposed to values of the interpolated variables) are not breakable, but they can be made breakable in part of the template by using the `~` keyword (ended with another `~`).

```
$~$This long line may break if the document is rendered
with a short line length.$~$
```

### Pipes

A pipe transforms the value of a variable or partial. Pipes are specified using a slash (`/`) between the variable name (or partial) and the pipe name. Example:

```
$for(name)$
$name/uppercase$
$endfor$

$for(metadata/pairs)$
- $it.key$: $it.value$
$endfor$

$employee:name()/uppercase$
```

Pipes may be chained:

```
$for(employees/pairs)$
$it.key/alpha/uppercase$. $it.name$
$endfor$
```

Some pipes take parameters:

```
|----------------------|------------|
$for(employee)$
$it.name.first/uppercase/left 20 "| "$$it.name.salary/right 10 " | " " |"$
$endfor$
|----------------------|------------|
```

Currently the following pipes are predefined:

- `pairs`: Converts a map or array to an array of maps, each with `key` and `value` fields. If the original value was an array, the `key` will be the array index, starting with 1.
- `uppercase`: Converts text to uppercase.
- `lowercase`: Converts text to lowercase.
- `length`: Returns the length of the value: number of characters for a textual value, number of elements for a map or array.
- `reverse`: Reverses a textual value or array, and has no effect on other values.
- `first`: Returns the first value of an array, if applied to a non-empty array; otherwise returns the original value.
- `last`: Returns the last value of an array, if applied to a non-empty array; otherwise returns the original value.
- `rest`: Returns all but the first value of an array, if applied to a non-empty array; otherwise returns the original value.
- `allbutlast`: Returns all but the last value of an array, if applied to a non-empty array; otherwise returns the original value.
- `chomp`: Removes trailing newlines (and breakable space).
- `nowrap`: Disables line wrapping on breakable spaces.
- `alpha`: Converts textual values that can be read as an integer into lowercase alphabetic characters `a..z` (mod 26). This can be used to get lettered enumeration from array indices. To get uppercase letters, chain with `uppercase`.
- `roman`: Converts textual values that can be read as an integer into lowercase roman numerals. This can be used to get lettered enumeration from array indices. To get uppercase roman, chain with `uppercase`.
- `left n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the left, with an optional left and right border. Has no effect on other values. This can be used to align material in tables. Widths are positive integers indicating the number of characters. Borders are strings inside double quotes; literal `"` and `\` characters must be backslash-escaped.
- `right n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the right, and has no effect on other values.
- `center n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the center, and has no effect on other values.
