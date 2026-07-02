---
title: "AsciiDoc User Guide (part 5/5)"
source: https://asciidoc.org/userguide.html
domain: asciidoc
license: CC-BY-SA-4.0
tags: asciidoc markup, lightweight markup, asciidoctor docs, text markup
fetched: 2026-07-02
part: 5/5
---

## 33. Filters

AsciiDoc filters allow external commands to process AsciiDoc *Paragraphs*, *DelimitedBlocks* and *Table* content. Filters are primarily an extension mechanism for generating specialized outputs. Filters are implemented using external commands which are specified in configuration file definitions.

There’s nothing special about the filters, they’re just standard UNIX filters: they read text from the standard input, process it, and write to the standard output.

The `asciidoc(1)` command `--filter` option can be used to install and remove filters. The same option is used to unconditionally load a filter.

Attribute substitution is performed on the filter command prior to execution — attributes can be used to pass parameters from the AsciiDoc source document to the filter.

| (Warning) | Filters sometimes included executable code. Before installing a filter you should verify that it is from a trusted source. |
|---|---|

If the filter command does not specify a directory path then `asciidoc(1)` recursively searches for the executable filter command:

- First it looks in the user’s `$HOME/.asciidoc/filters` directory.
- Next the global filters directory (usually `/etc/asciidoc/filters` or `/usr/local/etc/asciidoc`) directory is searched.
- Then it looks in the `asciidoc(1)` `./filters` directory.
- Finally it relies on the executing shell to search the environment search path (`$PATH`).

Standard practice is to install each filter in it’s own sub-directory with the same name as the filter’s style definition. For example the music filter’s style name is *music* so it’s configuration and filter files are stored in the `filters/music` directory.

### 33.2. Filter Configuration Files

Filters are normally accompanied by a configuration file containing a Paragraph or DelimitedBlock definition along with corresponding markup templates.

While it is possible to create new *Paragraph* or *DelimitedBlock* definitions the preferred way to implement a filter is to add a style to the existing Paragraph and ListingBlock definitions (all filters shipped with AsciiDoc use this technique). The filter is applied to the paragraph or delimited block by preceding it with an attribute list: the first positional attribute is the style name, remaining attributes are normally filter specific parameters.

`asciidoc(1)` auto-loads all `.conf` files found in the filter search paths unless the container directory also contains a file named `__noautoload__` (see previous section). The `__noautoload__` feature is used for filters that will be loaded manually using the `--filter` option.

### 33.3. Example Filter

AsciiDoc comes with a toy filter for highlighting source code keywords and comments. See also the `./filters/code/code-filter-readme.txt` file.

| (Note) | The purpose of this toy filter is to demonstrate how to write a filter — it’s much to simplistic to be passed off as a code syntax highlighter. If you want a full featured multi-language highlighter use the source code highlighter filter. |
|---|---|

### 33.4. Built-in filters

The AsciiDoc distribution includes *source*, *music*, *latex* and *graphviz* filters, details are on the AsciiDoc website.

| Filter name | Description |
|---|---|
| *music* | A music filter is included in the distribution `./filters/` directory. It translates music in LilyPond or ABC notation to standard classical notation. |
| *source* | A source code highlight filter is included in the distribution `./filters/` directory. |
| *latex* | The AsciiDoc LaTeX filter translates LaTeX source to an image that is automatically inserted into the AsciiDoc output documents. |
| *graphviz* | Gouichi Iisaka has written a Graphviz filter for AsciiDoc. Graphviz generates diagrams from a textual specification. Gouichi Iisaka’s Graphviz filter is included in the AsciiDoc distribution. Here are some AsciiDoc Graphviz examples. |

### 33.5. Filter plugins

Filter plugins are a mechanism for distributing AsciiDoc filters. A filter plugin is a Zip file containing the files that constitute a filter. The `asciidoc(1)` `--filter` option is used to load and manage filer plugins.

- Filter plugins take precedence over built-in filters with the same name.
- By default filter plugins are installed in `$HOME/.asciidoc/filters/<filter>` where `<filter>` is the filter name.


## 34. Plugins

The AsciiDoc plugin architecture is an extension mechanism that allows additional backends, filters and themes to be added to AsciiDoc.

- A plugin is a Zip file containing an AsciiDoc backend, filter or theme (configuration files, stylesheets, scripts, images).
- The `asciidoc(1)` `--backend`, `--filter` and `--theme` command-line options are used to load and manage plugins. Each of these options responds to the plugin management *install*, *list*, *remove* and *build* commands.
- The plugin management command names are reserved and cannot be used for filter, backend or theme names.
- The plugin Zip file name always begins with the backend, filter or theme name.

Plugin commands and conventions are documented in the `asciidoc(1)` man page. You can find lists of plugins on the AsciiDoc website.


## 35. Help Commands

The `asciidoc(1)` command has a `--help` option which prints help topics to stdout. The default topic summarizes `asciidoc(1)` usage:

```
$ asciidoc --help
```

To print a help topic specify the topic name as a command argument. Help topic names can be shortened so long as they are not ambiguous. Examples:

```
$ asciidoc --help manpage

$ asciidoc -h m              # Short version of previous example.

$ asciidoc --help syntax

$ asciidoc -h s              # Short version of previous example.
```

### 35.1. Customizing Help

To change, delete or add your own help topics edit a help configuration file. The help file name `help-<lang>.conf` is based on the setting of the `lang` attribute, it defaults to `help.conf` (English). The help file location will depend on whether you want the topics to apply to all users or just the current user.

The help topic files have the same named section format as other configuration files. The `help.conf` files are stored in the same locations and loaded in the same order as other configuration files.

When the `--help` command-line option is specified AsciiDoc loads the appropriate help files and then prints the contents of the section whose name matches the help topic name. If a topic name is not specified `default` is used. You don’t need to specify the whole help topic name on the command-line, just enough letters to ensure it’s not ambiguous. If a matching help file section is not found a list of available topics is printed.


## 36. Tips and Tricks

### 36.1. Know Your Editor

Writing AsciiDoc documents will be a whole lot more pleasant if you know your favorite text editor. Learn how to indent and reformat text blocks, paragraphs, lists and sentences. Tips for *vim* users follow.

### 36.2. Vim Commands for Formatting AsciiDoc

#### 36.2.1. Text Wrap Paragraphs

Use the vim `:gq` command to reformat paragraphs. Setting the *textwidth* sets the right text wrap margin; for example:

```
:set textwidth=70
```

To reformat a paragraph:

1. Position the cursor at the start of the paragraph.
2. Type `gq}`.

Execute `:help gq` command to read about the vim gq command.

| (Tip) | Assign the `gq}` command to the Q key with the `nnoremap Q gq}` command or put it in your `~/.vimrc` file to so it’s always available (see the Example `~/.vimrc` file). Put `set` commands in your `~/.vimrc` file so you don’t have to enter them manually. The Vim website (https://www.vim.org/) has a wealth of resources, including scripts for automated spell checking and ASCII Art drawing. |
|---|---|

#### 36.2.2. Format Lists

The `gq` command can also be used to format bulleted, numbered and callout lists. First you need to set the `comments`, `formatoptions` and `formatlistpat` (see the Example `~/.vimrc` file).

Now you can format simple lists that use dash, asterisk, period and plus bullets along with numbered ordered lists:

1. Position the cursor at the start of the list.
2. Type `gq}`.

#### 36.2.3. Indent Paragraphs

Indent whole paragraphs by indenting the fist line with the desired indent and then executing the `gq}` command.

#### 36.2.4. Example `~/.vimrc` File

```
" Use bold bright fonts.

set background=dark

" Show tabs and trailing characters.

"set listchars=tab:»·,trail:·,eol:¬

set listchars=tab:»·,trail:·

set list

" Reformat paragraphs and list.

nnoremap <Leader>r gq}

" Delete trailing white space and Dos-returns and to expand tabs to spaces.

nnoremap <Leader>t :set et<CR>:retab!<CR>:%s/[\r \t]\+$//<CR>

autocmd BufRead,BufNewFile *.txt,*.asciidoc,README,TODO,CHANGELOG,NOTES,ABOUT

        \ setlocal autoindent expandtab tabstop=8 softtabstop=2 shiftwidth=2 filetype=asciidoc

        \ textwidth=70 wrap formatoptions=tcqn

        \ formatlistpat=^\\s*\\d\\+\\.\\s\\+\\\\|^\\s*<\\d\\+>\\s\\+\\\\|^\\s*[a-zA-Z.]\\.\\s\\+\\\\|^\\s*[ivxIVX]\\+\\.\\s\\+

        \ comments=s1:/*,ex:*/,://,b:#,:%,:XCOMM,fb:-,fb:*,fb:+,fb:.,fb:>
```

### 36.3. Troubleshooting

AsciiDoc diagnostic features are detailed in the Diagnostics appendix.

### 36.4. Gotchas

**Incorrect character encoding**

If you get an error message like `'UTF-8' codec can't decode ...` then you source file contains invalid UTF-8 characters — set the AsciiDoc encoding attribute for the correct character set (typically ISO-8859-1 (Latin-1) for European languages).

**Invalid output**

AsciiDoc attempts to validate the input AsciiDoc source but makes no attempt to validate the output markup, it leaves that to external tools such as `xmllint(1)` (integrated into `a2x(1)`). Backend validation cannot be hardcoded into AsciiDoc because backends are dynamically configured. The following example generates valid HTML but invalid DocBook (the DocBook `literal` element cannot contain an `emphasis` element):

```
+monospaced text with an _emphasized_ word+
```

**Misinterpreted text formatting**

You can suppress markup expansion by placing a backslash character immediately in front of the element. The following example suppresses inline monospaced formatting:

```
\+1 for C++.
```

**Overlapping text formatting**

Overlapping text formatting will generate illegal overlapping markup tags which will result in downstream XML parsing errors. Here’s an example:

```
Some *strong markup _that overlaps* emphasized markup_.
```

**Ambiguous underlines**

A DelimitedBlock can immediately follow a paragraph without an intervening blank line, but be careful, a single line paragraph underline may be misinterpreted as a section title underline resulting in a “closing block delimiter expected” error.

**Ambiguous ordered list items**

Lines beginning with numbers at the end of sentences will be interpreted as ordered list items. The following example (incorrectly) begins a new list with item number 1999:

```
He was last sighted in

1999. Since then things have moved on.
```

The *list item out of sequence* warning makes it unlikely that this problem will go unnoticed.

**Special characters in attribute values**

Special character substitution precedes attribute substitution so if attribute values contain special characters you may, depending on the substitution context, need to escape the special characters yourself. For example:

```
$ asciidoc -a 'orgname=Bill &amp; Ben Inc.' mydoc.txt
```

**Attribute lists**

If any named attribute entries are present then all string attribute values must be quoted. For example:

```
["Desktop screenshot",width=32]
```

### 36.5. Combining separate documents

You have a number of stand-alone AsciiDoc documents that you want to process as a single document. Simply processing them with a series of `include` macros won’t work because the documents contain (level 0) document titles. The solution is to create a top level wrapper document and use the `leveloffset` attribute to push them all down one level. For example:

```
Combined Document Title

=======================

// Push titles down one level.

:leveloffset: 1

include::document1.txt[]

// Return to normal title levels.

:leveloffset: 0

A Top Level Section

-------------------

Lorum ipsum.

// Push titles down one level.

:leveloffset: 1

include::document2.txt[]

include::document3.txt[]
```

The document titles in the included documents will now be processed as level 1 section titles, level 1 sections as level 2 sections and so on.

- Put a blank line between the `include` macro lines to ensure the title of the included document is not seen as part of the last paragraph of the previous document.
- You won’t want non-title document header lines (for example, Author and Revision lines) in the included files — conditionally exclude them if they are necessary for stand-alone processing.

### 36.6. Processing document sections separately

You have divided your AsciiDoc document into separate files (one per top level section) which are combined and processed with the following top level document:

```
Combined Document Title

=======================

Joe Bloggs

v1.0, 12-Aug-03

include::section1.txt[]

include::section2.txt[]

include::section3.txt[]
```

You also want to process the section files as separate documents. This is easy because `asciidoc(1)` will quite happily process `section1.txt`, `section2.txt` and `section3.txt` separately — the resulting output documents contain the section but have no document title.

### 36.7. Processing document snippets

Use the `-s` (`--no-header-footer`) command-line option to suppress header and footer output, this is useful if the processed output is to be included in another file. For example:

```
$ asciidoc -sb docbook section1.txt
```

`asciidoc(1)` can be used as a filter, so you can pipe chunks of text through it. For example:

```
$ echo 'Hello *World!*' | asciidoc -s -

<div class="paragraph"><p>Hello <strong>World!</strong></p></div>
```

### 36.8. Badges in HTML page footers

See the `[footer]` section in the AsciiDoc distribution `xhtml11.conf` configuration file.

### 36.9. Pretty printing AsciiDoc output

If the indentation and layout of the `asciidoc(1)` output is not to your liking you can:

1. Change the indentation and layout of configuration file markup template sections. The `{empty}` attribute is useful for outputting trailing blank lines in markup templates.
2. Use HTML Tidy program to tidy `asciidoc(1)` output. Example: `$ asciidoc -b docbook -o - mydoc.txt | tidy -indent -xml >mydoc.xml`
3. Use the `xmllint(1)` format option. Example: `$ xmllint --format mydoc.xml`

### 36.10. Supporting minor DocBook DTD variations

The conditional inclusion of DocBook SGML markup at the end of the distribution `docbook45.conf` file illustrates how to support minor DTD variations. The included sections override corresponding entries from preceding sections.

### 36.11. Creating stand-alone HTML documents

If you’ve ever tried to send someone an HTML document that includes stylesheets and images you’ll know that it’s not as straight-forward as exchanging a single file. AsciiDoc has options to create stand-alone documents containing embedded images, stylesheets and scripts. The following AsciiDoc command creates a single file containing embedded images, CSS stylesheets, and JavaScript (for table of contents and footnotes):

```
$ asciidoc -a data-uri -a icons -a toc -a max-width=55em article.txt
```

You can view the HTML file here: https://asciidoc.org/article-standalone.html

### 36.12. Shipping stand-alone AsciiDoc source

Reproducing presentation documents from someone else’s source has one major problem: unless your configuration files are the same as the creator’s you won’t get the same output.

The solution is to create a single backend specific configuration file using the `asciidoc(1)` `-c` (`--dump-conf`) command-line option. You then ship this file along with the AsciiDoc source document plus the `asciidoc.py` script. The only end user requirement is that they have Python installed (and that they consider you a trusted source). This example creates a composite HTML configuration file for `mydoc.txt`:

```
$ asciidoc -cb xhtml11 mydoc.txt > mydoc-xhtml11.conf
```

Ship `mydoc.txt`, `mydoc-html.conf`, and `asciidoc.py`. With these three files (and a Python interpreter) the recipient can regenerate the HMTL output:

```
$ ./asciidoc.py -eb xhtml11 mydoc.txt
```

The `-e` (`--no-conf`) option excludes the use of implicit configuration files, ensuring that only entries from the `mydoc-html.conf` configuration are used.

### 36.13. Inserting blank space

Adjust your style sheets to add the correct separation between block elements. Inserting blank paragraphs containing a single non-breaking space character `{nbsp}` works but is an ad hoc solution compared to using style sheets.

### 36.14. Closing open sections

You can close off section tags up to level `N` by calling the `eval::[Section.setlevel(N)]` system macro. This is useful if you want to include a section composed of raw markup. The following example includes a DocBook glossary division at the top section level (level 0):

```
ifdef::basebackend-docbook[]

eval::[Section.setlevel(0)]

+++++++++++++++++++++++++++++++

<glossary>

  <title>Glossary</title>

  <glossdiv>

  ...

  </glossdiv>

</glossary>

+++++++++++++++++++++++++++++++

endif::basebackend-docbook[]
```

### 36.15. Validating output files

Use `xmllint(1)` to check the AsciiDoc generated markup is both well formed and valid. Here are some examples:

```
$ xmllint --nonet --noout --valid docbook-file.xml

$ xmllint --nonet --noout --valid xhtml11-file.html

$ xmllint --nonet --noout --valid --html html4-file.html
```

The `--valid` option checks the file is valid against the document type’s DTD, if the DTD is not installed in your system’s catalog then it will be fetched from its Internet location. If you omit the `--valid` option the document will only be checked that it is well formed.

The online W3C Markup Validation Service is the defacto standard when it comes to validating HTML (it validates all HTML standards including HTML5).


## Glossary

**Block element**

An AsciiDoc block element is a document entity composed of one or more whole lines of text.

**Inline element**

AsciiDoc inline elements occur within block element textual content, they perform formatting and substitution tasks.

**Formal element**

An AsciiDoc block element that has a BlockTitle. Formal elements are normally listed in front or back matter, for example lists of tables, examples and figures.

**Verbatim element**

The word verbatim indicates that white space and line breaks in the source document are to be preserved in the output document.


## Appendix A: Migration Notes

### Version 7 to version 8

- A new set of quotes has been introduced which may match inline text in existing documents — if they do you’ll need to escape the matched text with backslashes.
- The index entry inline macro syntax has changed — if your documents include indexes you may need to edit them.
- Replaced `a2x(1)` `--no-icons` and `--no-copy` options with their negated equivalents: `--icons` and `--copy` respectively. The default behavior has also changed — the use of icons and copying of icon and CSS files must be specified explicitly with the `--icons` and `--copy` options.

The rationale for the changes can be found in the AsciiDoc `CHANGELOG`.

| (Note) | If you want to disable unconstrained quotes, the new alternative constrained quotes syntax and the new index entry syntax then you can define the attribute `asciidoc7compatible` (for example by using the `-a asciidoc7compatible` command-line option). |
|---|---|


## Appendix B: Packager Notes

Read the `README` and `INSTALL` files (in the distribution root directory) for install prerequisites and procedures. The distribution `Makefile.in` (used by `configure` to generate the `Makefile`) is the canonical installation procedure.


## Appendix C: AsciiDoc Safe Mode

AsciiDoc *safe mode* skips potentially dangerous scripted sections in AsciiDoc source files by inhibiting the execution of arbitrary code or the inclusion of arbitrary files.

The safe mode is disabled by default, it can be enabled with the `asciidoc(1)` `--safe` command-line option.

Safe mode constraints

- `eval`, `sys` and `sys2` executable attributes and block macros are not executed.
- `include::<filename>[]` and `include1::<filename>[]` block macro files must reside inside the parent file’s directory.
- `{include:<filename>}` executable attribute files must reside inside the source document directory.
- Passthrough Blocks are dropped.

| (Warning) | The safe mode is not designed to protect against unsafe AsciiDoc configuration files. Be especially careful when: Implementing filters. Implementing elements that don’t escape special characters. Accepting configuration files from untrusted sources. |
|---|---|


## Appendix D: Using AsciiDoc with non-English Languages

AsciiDoc can process UTF-8 character sets but there are some things you need to be aware of:

- If you are generating output documents using a DocBook toolchain then you should set the AsciiDoc `lang` attribute to the appropriate language (it defaults to `en` (English)). This will ensure things like table of contents, figure and table captions and admonition captions are output in the specified language. For example: `$ a2x -a lang=es doc/article.txt`
- If you are outputting HTML directly from `asciidoc(1)` you’ll need to set the various `*_caption` attributes to match your target language (see the list of captions and titles in the `[attributes]` section of the distribution `lang-*.conf` files). The easiest way is to create a language `.conf` file (see the AsciiDoc’s `lang-en.conf` file). (Note) You still use the *NOTE*, *CAUTION*, *TIP*, *WARNING*, *IMPORTANT* captions in the AsciiDoc source, they get translated in the HTML output file.
- `asciidoc(1)` automatically loads configuration files named like `lang-<lang>.conf` where `<lang>` is a two letter language code that matches the current AsciiDoc `lang` attribute. See also Configuration File Names and Locations.


## Appendix E: Vim Syntax Highlighter

Syntax highlighting is incredibly useful, in addition to making reading AsciiDoc documents much easier syntax highlighting also helps you catch AsciiDoc syntax errors as you write your documents.

If you use the Vim editor, it comes with an AsciiDoc syntax highlighter pre-included. By default, it will activate for files that use the .asciidoc or .adoc file extensions.

Alternatively, to enable syntax highlighting for the current document or other extensions:

- Put a Vim *autocmd* in your Vim configuration file (see the example vimrc file).
- or execute the Vim command `:set syntax=asciidoc`.
- or add the following line to the end of you AsciiDoc source files: `// vim: set syntax=asciidoc:`


## Appendix F: Attribute Options

Here is the list of predefined attribute list options:

| Option | Backends | AsciiDoc Elements | Description |
|---|---|---|---|
| *autowidth* | xhtml11, html5, html4 | table | The column widths are determined by the browser, not the AsciiDoc *cols* attribute. If there is no *width* attribute the table width is also left up to the browser. |
| *unbreakable* | xhtml11, html5 | block elements | *unbreakable* attempts to keep the block element together on a single printed page c.f. the *breakable* and *unbreakable* docbook (XSL/FO) options below. |
| *breakable, unbreakable* | docbook (XSL/FO) | table, example, block image | The *breakable* options allows block elements to break across page boundaries; *unbreakable* attempts to keep the block element together on a single page. If neither option is specified the default XSL stylesheet behavior prevails. |
| *compact* | docbook, xhtml11, html5 | bulleted list, numbered list | Minimizes vertical space in the list |
| *footer* | docbook, xhtml11, html5, html4 | table | The last row of the table is rendered as a footer. |
| *header* | docbook, xhtml11, html5, html4 | table | The first row of the table is rendered as a header. |
| *pgwide* | docbook (XSL/FO) | table, block image, horizontal labeled list | Specifies that the element should be rendered across the full text width of the page irrespective of the current indentation. |
| *strong* | xhtml11, html5, html4 | labeled lists | Emboldens label text. |


## Appendix G: Diagnostics

The `asciidoc(1)` `--verbose` command-line option prints additional information to stderr: files processed, filters processed, warnings, system attribute evaluation.

A special attribute named *trace* enables the output of element-by-element diagnostic messages detailing output markup generation to stderr. The *trace* attribute can be set on the command-line or from within the document using Attribute Entries (the latter allows tracing to be confined to specific portions of the document).

- Trace messages print the source file name and line number and the trace name followed by related markup.
- *trace names* are normally the names of AsciiDoc elements (see the list below).
- The trace message is only printed if the *trace* attribute value matches the start of a *trace name*. The *trace* attribute value can be any Python regular expression. If a trace value is not specified all trace messages will be printed (this can result in large amounts of output if applied to the whole document).
- In the case of inline substitutions: The text before and after the substitution is printed; the before text is preceded by a line containing `<<<` and the after text by a line containing `>>>`. The *subs* trace value is an alias for all inline substitutions.

Trace names

```
<blockname> block close

<blockname> block open

<subs>

dropped line (a line containing an undefined attribute reference).

floating title

footer

header

list close

list entry close

list entry open

list item close

list item open

list label close

list label open

list open

macro block (a block macro)

name (man page NAME section)

paragraph

preamble close

preamble open

push blockname

pop blockname

section close

section open: level <level>

subs (all inline substitutions)

table
```

Where:

- `<level>` is section level number *0…4*.
- `<blockname>` is a delimited block name: *comment*, *sidebar*, *open*, *pass*, *listing*, *literal*, *quote*, *example*.
- `<subs>` is an inline substitution type: *specialcharacters*,*quotes*,*specialwords*, *replacements*, *attributes*,*macros*,*callouts*, *replacements2*, *replacements3*.

Command-line examples:

1. Trace the entire document. `$ asciidoc -a trace mydoc.txt`
2. Trace messages whose names start with `quotes` or `macros`: `$ asciidoc -a 'trace=quotes|macros' mydoc.txt`
3. Print the first line of each trace message: `$ asciidoc -a trace mydoc.txt 2>&1 | grep ^TRACE:`

Attribute Entry examples:

1. Begin printing all trace messages: `:trace:`
2. Print only matched trace messages: `:trace: quotes|macros`
3. Turn trace messages off: `:trace!:`


## Appendix H: Backend Attributes

This table contains a list of optional attributes that influence the generated outputs.

| Name | Backends | Description |
|---|---|---|
| *badges* | xhtml11, html5 | Link badges (*XHTML 1.1* and *CSS*) in document footers. By default badges are omitted (*badges* is undefined). (Note) The path names of images, icons and scripts are relative path names to the output document not the source document. |
| *data-uri* | xhtml11, html5 | Embed images using the data: uri scheme. |
| *css-signature* | html5, xhtml11 | Set a *CSS signature* for the document (sets the *id* attribute of the HTML *body* element). CSS signatures provide a mechanism that allows users to personalize the document appearance. The term *CSS signature* was coined by Eric Meyer. |
| *disable-javascript* | xhtml11, html5 | If the `disable-javascript` attribute is defined the `asciidoc.js` JavaScript is not embedded or linked to the output document. By default AsciiDoc automatically embeds or links the `asciidoc.js` JavaScript to the output document. The script dynamically generates table of contents and footnotes. |
| *docinfo, docinfo1, docinfo2* | All backends | These three attributes control which document information files will be included in the the header of the output file: docinfo Include `<filename>-docinfo.<ext>` docinfo1 Include `docinfo.<ext>` docinfo2 Include `docinfo.<ext>` and `<filename>-docinfo.<ext>` Where `<filename>` is the file name (sans extension) of the AsciiDoc input file and `<ext>` is `.html` for HTML outputs or `.xml` for DocBook outputs. If the input file is the standard input then the output file name is used. The following example will include the `mydoc-docinfo.xml` docinfo file in the DocBook `mydoc.xml` output file: `$ asciidoc -a docinfo -b docbook mydoc.txt` This next example will include `docinfo.html` and `mydoc-docinfo.html` docinfo files in the HTML output file: `$ asciidoc -a docinfo2 -b html4 mydoc.txt` |
| *encoding* | html4, html5, xhtml11, docbook | Set the input and output document character set encoding. For example the `--attribute encoding=ISO-8859-1` command-line option will set the character set encoding to `ISO-8859-1`. The default encoding is UTF-8. This attribute specifies the character set in the output document. The encoding name must correspond to a Python codec name or alias. The *encoding* attribute can be set using an AttributeEntry inside the document header. For example: `:encoding: ISO-8859-1` |
| *hr* | html4 | Defines the *html4* inter-section horizontal ruler element. By default *html4* top level sections are separated by a horizontal ruler element, undefine this attribute or set it to an empty string if you do not want them. The default *html4* backend value for the *hr* attribute is `<hr>`. |
| *icons* | xhtml11, html5 | Link admonition paragraph and admonition block icon images and badge images. By default *icons* is undefined and text is used in place of icon images. |
| *iconsdir* | html4, html5, xhtml11, docbook | The name of the directory containing linked admonition icons, navigation icons and the `callouts` sub-directory (the `callouts` sub-directory contains callout number images). *iconsdir* defaults to `./images/icons`. If admonition icons are embedded using the data-uri scheme then the *iconsdir* attribute defaults to the location of the icons installed in the AsciiDoc configuration directory. |
| *imagesdir* | html4, html5, xhtml11, docbook | If this attribute is defined it is prepended to the target image file name paths in inline and block image macros. |
| *keywords, description, title* | html4, html5, xhtml11 | The *keywords* and *description* attributes set the correspondingly named HTML meta tag contents; the *title* attribute sets the HTML title tag contents. Their principle use is for SEO (Search Engine Optimisation). All three are optional, but if they are used they must appear in the document header (or on the command-line). If *title* is not specified the AsciiDoc document title is used. |
| *linkcss* | html5, xhtml11 | Link CSS stylesheets and JavaScripts. By default *linkcss* is undefined in which case stylesheets and scripts are automatically embedded in the output document. |
| *max-width* | html5, xhtml11 | Set the document maximum display width (sets the *body* element CSS *max-width* property). |
| *numbered* | html4, html5, xhtml11, docbook (XSL Stylesheets) | Adds section numbers to section titles. The *docbook* backend ignores *numbered* attribute entries after the document header. |
| *plaintext* | All backends | If this global attribute is defined all inline substitutions are suppressed and block indents are retained. This option is useful when dealing with large amounts of imported plain text. |
| *quirks* | xhtml11 | Include the `xhtml11-quirks.conf` configuration file and `xhtml11-quirks.css` stylesheet to work around IE6 browser incompatibilities. This feature is deprecated and its use is discouraged — documents are still viewable in IE6 without it. |
| *revremark* | docbook | A short summary of changes in this document revision. Must be defined prior to the first document section. The document also needs to be dated to output this attribute. |
| *footer-style* | html4, html5, xhtml11 | Changes the "Last updated" field in the footer of the document or removes this field and the revision number (in the footer only). Can take 3 values: none : Don’t display the "Last updated" and "Revision number" fields in the footer of the document revdate : The "Last updated" field’s date in the footer will be the revision date specified in the document (`revdate` attribute) default (or any other value) : The "Last updated" field’s date in the footer will be the date of the input file modification This attribute can be set, for example, using `:footer-style: revdate` in the header of the file or using the `--attribute footer-style=revdate` command-line option. |
| *scriptsdir* | html5, xhtml11 | The name of the directory containing linked JavaScripts. See HTML stylesheets and JavaScript locations. |
| *sgml* | docbook45 | The `--backend=docbook45` command-line option produces DocBook 4.5 XML. You can produce the older DocBook SGML format using the `--attribute sgml` command-line option. |
| *stylesdir* | html5, xhtml11 | The name of the directory containing linked or embedded stylesheets. See HTML stylesheets and JavaScript locations. |
| *stylesheet* | html5, xhtml11 | The file name of an optional additional CSS stylesheet. |
| *theme* | html5, xhtml11 | Use alternative stylesheet (see Stylesheets). |
| *toc* | html5, xhtml11, docbook (XSL Stylesheets) | Adds a table of contents to the start of an article or book document. The `toc` attribute can be specified using the `--attribute toc` command-line option or a `:toc:` attribute entry in the document header. The *toc* attribute is defined by default when the *docbook* backend is used. To disable table of contents generation undefine the *toc* attribute by putting a `:toc!:` attribute entry in the document header or from the command-line with an `--attribute toc!` option. **xhtml11 and html5 backends** JavaScript needs to be enabled in your browser. The following example generates a numbered table of contents using a JavaScript embedded in the `mydoc.html` output document: `$ asciidoc -a toc -a numbered mydoc.txt` |
| *toc2* | html5, xhtml11 | Adds a scrollable table of contents in the left hand margin of an article or book document. Use the *max-width* attribute to change the content width. In all other respects behaves the same as the *toc* attribute. |
| *toc-placement* | html5, xhtml11 | When set to *auto* (the default value) `asciidoc(1)` will place the table of contents in the document header. When *toc-placement* is set to *manual* the TOC can be positioned anywhere in the document by placing the `toc::[]` block macro at the point you want the TOC to appear. (Note) If you use *toc-placement* then you also have to define the toc attribute. |
| *toc-title* | html5, xhtml11 | Sets the table of contents title (defaults to *Table of Contents*). |
| *toclevels* | html5, xhtml11 | Sets the number of title levels (1..4) reported in the table of contents (see the *toc* attribute above). Defaults to 2 and must be used with the *toc* attribute. Example usage: `$ asciidoc -a toc -a toclevels=3 doc/asciidoc.txt` |


## Appendix I: License

Free use of this software is granted under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Copyright © 2002-2013 Stuart Rackham.

Copyright © 2013-2022 AsciiDoc Contributors.
