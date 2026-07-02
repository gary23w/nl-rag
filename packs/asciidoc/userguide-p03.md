---
title: "AsciiDoc User Guide (part 3/5)"
source: https://asciidoc.org/userguide.html
domain: asciidoc
license: CC-BY-SA-4.0
tags: asciidoc markup, lightweight markup, asciidoctor docs, text markup
fetched: 2026-07-02
part: 3/5
---

## 21. Macros

Macros are a mechanism for substituting parametrized text into output documents.

Macros have a *name*, a single *target* argument and an *attribute list*. The usual syntax is `<name>:<target>[<attrlist>]` (for inline macros) and `<name>::<target>[<attrlist>]` (for block macros). Here are some examples:

```
https://docbook.org/[DocBook.org]

include::chapt1.txt[tabsize=2]

mailto:srackham@gmail.com[]
```

Macro behavior

- `<name>` is the macro name. It can only contain letters, digits or dash characters and cannot start with a dash.
- The optional `<target>` cannot contain white space characters.
- `<attrlist>` is a list of attributes enclosed in square brackets.
- `]` characters inside attribute lists must be escaped with a backslash.
- Expansion of macro references can normally be escaped by prefixing a backslash character (see the AsciiDoc *FAQ* for examples of exceptions to this rule).
- Attribute references in block macros are expanded.
- The substitutions performed prior to Inline macro macro expansion are determined by the inline context.
- Macros are processed in the order they appear in the configuration file(s).
- Calls to inline macros can be nested inside different inline macros (an inline macro call cannot contain a nested call to itself).
- In addition to `<name>`, `<target>` and `<attrlist>` the `<passtext>` and `<subslist>` named groups are available to passthrough macros. A macro is a passthrough macro if the definition includes a `<passtext>` named group.

### 21.1. Inline Macros

Inline Macros occur in an inline element context. Predefined Inline macros include *URLs*, *image* and *link* macros.

#### 21.1.1. URLs

*http*, *https*, *ftp*, *file*, *mailto* and *callto* URLs are rendered using predefined inline macros.

- If you don’t need a custom link caption you can enter the *http*, *https*, *ftp*, *file* URLs and email addresses without any special macro syntax.
- If the `<attrlist>` is empty the URL is displayed.

Here are some examples:

```
https://docbook.org/[DocBook.org]

https://docbook.org/

mailto:joe.bloggs@foobar.com[email Joe Bloggs]

joe.bloggs@foobar.com
```

Which are rendered:

DocBook.org

https://docbook.org/

email Joe Bloggs

joe.bloggs@foobar.com

If the `<target>` necessitates space characters use `%20`, for example `large%20image.png`.

#### 21.1.2. Internal Cross References

Two AsciiDoc inline macros are provided for creating hypertext links within an AsciiDoc document. You can use either the standard macro syntax or the (preferred) alternative.

##### anchor

Used to specify hypertext link targets:

```
[[<id>,<xreflabel>]]

anchor:<id>[<xreflabel>]
```

The `<id>` is a unique string that conforms to the output markup’s anchor syntax. The optional `<xreflabel>` is the text to be displayed by captionless *xref* macros that refer to this anchor. The optional `<xreflabel>` is only really useful when generating DocBook output. Example anchor:

```
[[X1]]
```

You may have noticed that the syntax of this inline element is the same as that of the BlockId block element, this is no coincidence since they are functionally equivalent.

##### xref

Creates a hypertext link to a document anchor.

```
<<<id>,<caption>>>

xref:<id>[<caption>]
```

The `<id>` refers to an anchor ID. The optional `<caption>` is the link’s displayed text. Example:

```
<<X21,attribute lists>>
```

If `<caption>` is not specified then the displayed text is auto-generated:

- The AsciiDoc *xhtml11* and *html5* backends display the `<id>` enclosed in square brackets.
- If DocBook is produced the DocBook toolchain is responsible for the displayed text which will normally be the referenced figure, table or section title number followed by the element’s title text.

Here is an example:

```
[[tiger_image]]

.Tyger tyger

image::tiger.png[]

This can be seen in <<tiger_image>>.
```

#### 21.1.3. Linking to Local Documents

Hypertext links to files on the local file system are specified using the *link* inline macro.

```
link:<target>[<caption>]
```

The *link* macro generates relative URLs. The link macro `<target>` is the target file name (relative to the file system location of the referring document). The optional `<caption>` is the link’s displayed text. If `<caption>` is not specified then `<target>` is displayed. Example:

```
link:downloads/foo.zip[download foo.zip]
```

You can use the `<filename>#<id>` syntax to refer to an anchor within a target document but this usually only makes sense when targeting HTML documents.

#### 21.1.4. Images

Inline images are inserted into the output document using the *image* macro. The inline syntax is:

```
image:<target>[<attributes>]
```

The contents of the image file `<target>` is displayed. To display the image its file format must be supported by the target backend application. HTML and DocBook applications normally support PNG or JPG files.

`<target>` file name paths are relative to the location of the referring document.

Image macro attributes

- The optional *alt* attribute is also the first positional attribute, it specifies alternative text which is displayed if the output application is unable to display the image file (see also Use of ALT texts in IMGs). For example: `image:images/logo.png[Company Logo]`
- The optional *title* attribute provides a title for the image. The block image macro renders the title alongside the image. The inline image macro displays the title as a popup “tooltip” in visual browsers (AsciiDoc HTML outputs only).
- The optional `width` and `height` attributes scale the image size and can be used in any combination. The units are pixels. The following example scales the previous example to a height of 32 pixels: `image:images/logo.png["Company Logo",height=32]`
- The optional `link` attribute is used to link the image to an external document. The following example links a screenshot thumbnail to a full size version: `image:screen-thumbnail.png[height=32,link="screen.png"]`
- The optional `scaledwidth` attribute is only used in DocBook block images (specifically for PDF documents). The following example scales the images to 75% of the available print width: `image::images/logo.png[scaledwidth="75%",alt="Company Logo"]`
- The image `scale` attribute sets the DocBook `imagedata` element `scale` attribute.
- The optional `align` attribute aligns block macro images horizontally. Allowed values are `center`, `left` and `right`. For example: `image::images/tiger.png["Tiger image",align="left"]`
- The optional `float` attribute floats the image `left` or `right` on the page (works with HTML outputs only, has no effect on DocBook outputs). `float` and `align` attributes are mutually exclusive. Use the `unfloat::[]` block macro to stop floating.

See comment block macro.

### 21.2. Block Macros

A Block macro reference must be contained in a single line separated either side by a blank line or a block delimiter.

Block macros behave just like Inline macros, with the following differences:

- They occur in a block context.
- The default syntax is `<name>::<target>[<attrlist>]` (two colons, not one).
- Markup template section names end in `-blockmacro` instead of `-inlinemacro`.

#### 21.2.1. Block Identifier

The Block Identifier macro sets the `id` attribute and has the same syntax as the anchor inline macro since it performs essentially the same function — block templates use the `id` attribute as a block element ID. For example:

```
[[X30]]
```

This is equivalent to the `[id="X30"]` AttributeList element).

#### 21.2.2. Images

The *image* block macro is used to display images in a block context. The syntax is:

```
image::<target>[<attributes>]
```

The block `image` macro has the same macro attributes as it’s inline image macro counterpart.

| (Warning) | Unlike the inline `image` macro, the entire block `image` macro must be on a single line. |
|---|---|

Block images can be titled by preceding the *image* macro with a *BlockTitle*. DocBook toolchains normally number titled block images and optionally list them in an automatically generated *List of Figures* backmatter section.

This example:

```
.Main circuit board

image::images/layout.png[J14P main circuit board]
```

is equivalent to:

```
image::images/layout.png["J14P main circuit board", title="Main circuit board"]
```

A title prefix that can be inserted with the `caption` attribute (HTML backends). For example:

```
.Main circuit board

[caption="Figure 2: "]

image::images/layout.png[J14P main circuit board]
```

Embedding images in XHTML documents

If you define the `data-uri` attribute then images will be embedded in XHTML outputs using the data URI scheme. You can use the *data-uri* attribute with the *xhtml11* and *html5* backends to produce single-file XHTML documents with embedded images and CSS, for example:

```
$ asciidoc -a data-uri mydocument.txt
```

| (Note) | All current popular browsers support data URIs, although versions of Internet Explorer prior to version 8 do not. Some browsers limit the size of data URIs. |
|---|---|

#### 21.2.3. Comment Lines

Single lines starting with two forward slashes hard up against the left margin are treated as comments. Comment lines do not appear in the output unless the *showcomments* attribute is defined. Comment lines have been implemented as both block and inline macros so a comment line can appear as a stand-alone block or within block elements that support inline macro expansion. Example comment line:

```
// This is a comment.
```

If the *showcomments* attribute is defined comment lines are written to the output:

- In DocBook the comment lines are enclosed by the *remark* element (which may or may not be rendered by your toolchain).
- The *showcomments* attribute does not expose Comment Blocks. Comment Blocks are never passed to the output.

### 21.3. System Macros

System macros are block macros that perform a predefined task and are hardwired into the `asciidoc(1)` program.

- You can escape system macros with a leading backslash character (as you can with other macros).
- The syntax and tasks performed by system macros is built into `asciidoc(1)` so they don’t appear in configuration files. You can however customize the syntax by adding entries to a configuration file `[macros]` section.

#### 21.3.1. Include Macros

The `include` and `include1` system macros to include the contents of a named file into the source document.

The `include` macro includes a file as if it were part of the parent document — tabs are expanded and system macros processed. The contents of `include1` files are not subject to tab expansion or system macro processing nor are attribute or lower priority substitutions performed. The `include1` macro’s intended use is to include verbatim embedded CSS or scripts into configuration file headers. Example:

```
include::chapter1.txt[tabsize=4]
```

Include macro behavior

- If the included file name is specified with a relative path then the path is relative to the location of the referring document.
- Include macros can appear inside configuration files.
- Files included from within *DelimitedBlocks* are read to completion to avoid false end-of-block underline termination.
- Attribute references are expanded inside the include *target*; if an attribute is undefined then the included file is silently skipped.
- The *tabsize* macro attribute sets the number of space characters to be used for tab expansion in the included file (not applicable to `include1` macro).
- The *depth* macro attribute sets the maximum permitted number of subsequent nested includes (not applicable to `include1` macro which does not process nested includes). Setting *depth* to *1* disables nesting inside the included file. By default, nesting is limited to a depth of ten.
- The `lines` macro attribute can be used to include specific lines of the file. You can specify a range of pages by using `..` between the two numbers, for example `1..10` would include the first 10 lines. You can include multiple ranges or invdividual pages by using a comma or semi-colon, for example `1..10,45,50..60`.
- If the *warnings* attribute is set to *False* (or any other Python literal that evaluates to boolean false) then no warning message is printed if the included file does not exist. By default *warnings* are enabled.
- Internally the `include1` macro is translated to the `include1` system attribute which means it must be evaluated in a region where attribute substitution is enabled. To inhibit nested substitution in included files it is preferable to use the `include` macro and set the attribute `depth=1`.

#### 21.3.2. Conditional Inclusion Macros

Lines of text in the source document can be selectively included or excluded from processing based on the existence (or not) of a document attribute.

Document text between the `ifdef` and `endif` macros is included if a document attribute is defined:

```
ifdef::<attribute>[]

:

endif::<attribute>[]
```

Document text between the `ifndef` and `endif` macros is not included if a document attribute is defined:

```
ifndef::<attribute>[]

:

endif::<attribute>[]
```

`<attribute>` is an attribute name which is optional in the trailing `endif` macro.

If you only want to process a single line of text then the text can be put inside the square brackets and the `endif` macro omitted, for example:

```
ifdef::revnumber[Version number 42]
```

Is equivalent to:

```
ifdef::revnumber[]

Version number 42

endif::revnumber[]
```

*ifdef* and *ifndef* macros also accept multiple attribute names:

- Multiple *,* separated attribute names evaluate to defined if one or more of the attributes is defined, otherwise it’s value is undefined.
- Multiple *+* separated attribute names evaluate to defined if all of the attributes is defined, otherwise it’s value is undefined.

Document text between the `ifeval` and `endif` macros is included if the Python expression inside the square brackets is true. Example:

```
ifeval::[{rs458}==2]

:

endif::[]
```

- Document attribute references are expanded before the expression is evaluated.
- If an attribute reference is undefined then the expression is considered false.

Take a look at the `*.conf` configuration files in the AsciiDoc distribution for examples of conditional inclusion macro usage.

#### 21.3.3. Executable system macros

The *eval*, *sys* and *sys2* block macros exhibit the same behavior as their same named system attribute references. The difference is that system macros occur in a block macro context whereas system attributes are confined to inline contexts where attribute substitution is enabled.

The following example displays a long directory listing inside a literal block:

```
------------------

sys::[ls -l *.txt]

------------------
```

| (Note) | There are no block macro versions of the *eval3* and *sys3* system attributes. |
|---|---|

#### 21.3.4. Template System Macro

The `template` block macro allows the inclusion of one configuration file template section within another. The following example includes the `[admonitionblock]` section in the `[admonitionparagraph]` section:

```
[admonitionparagraph]

template::[admonitionblock]
```

Template macro behavior

- The `template::[]` macro is useful for factoring configuration file markup.
- `template::[]` macros cannot be nested.
- `template::[]` macro expansion is applied after all configuration files have been read.

### 21.4. Passthrough macros

Passthrough macros are analogous to passthrough blocks and are used to pass text directly to the output. The substitution performed on the text is determined by the macro definition but can be overridden by the `<subslist>`. The usual syntax is `<name>:<subslist>[<passtext>]` (for inline macros) and `<name>::<subslist>[<passtext>]` (for block macros). Passthroughs, by definition, take precedence over all other text substitutions.

**pass**

Inline and block. Passes text unmodified (apart from explicitly specified substitutions). Examples:

```
pass:[<q>To be or not to be</q>]

pass:attributes,quotes[<u>the '{author}'</u>]
```

**asciimath, latexmath**

Inline and block. Passes text unmodified. Used for mathematical formulas.

**+++**

Inline and block. The triple-plus passthrough is functionally identical to the *pass* macro but you don’t have to escape `]` characters and you can prefix with quoted attributes in the inline version. Example:

```
Red [red]+++`sum_(i=1)\^n i=(n(n+1))/2`$+++ AsciiMath formula
```

**$$**

Inline and block. The double-dollar passthrough is functionally identical to the triple-plus passthrough with one exception: special characters are escaped. Example:

```
$$`[[a,b],[c,d]]((n),(k))`$$
```

**`**

Text quoted with single backtick characters constitutes an *inline literal* passthrough. The enclosed text is rendered in a monospaced font and is only subject to special character substitution. This makes sense since monospace text is usually intended to be rendered literally and often contains characters that would otherwise have to be escaped. If you need monospaced text containing inline substitutions use a plus character instead of a backtick.

### 21.5. Macro Definitions

Each entry in the configuration `[macros]` section is a macro definition which can take one of the following forms:

**`<pattern>=<name>[<subslist]`**

Inline macro definition.

**`<pattern>=#<name>[<subslist]`**

Block macro definition.

**`<pattern>=+<name>[<subslist]`**

System macro definition.

**`<pattern>`**

Delete the existing macro with this `<pattern>`.

`<pattern>` is a Python regular expression and `<name>` is the name of a markup template. If `<name>` is omitted then it is the value of the regular expression match group named *name*. The optional `[<subslist]` is a comma-separated list of substitution names enclosed in `[]` brackets, it sets the default substitutions for passthrough text, if omitted then no passthrough substitutions are performed.

Pattern named groups

The following named groups can be used in macro `<pattern>` regular expressions and are available as markup template attributes:

**name**

The macro name.

**target**

The macro target.

**attrlist**

The macro attribute list.

**passtext**

Contents of this group are passed unmodified to the output subject only to *subslist* substitutions.

**subslist**

Processed as a comma-separated list of substitution names for *passtext* substitution, overrides the the macro definition *subslist*.

Here’s what happens during macro substitution

- Each contextually relevant macro *pattern* from the `[macros]` section is matched against the input source line.
- If a match is found the text to be substituted is loaded from a configuration markup template section named like `<name>-inlinemacro` or `<name>-blockmacro` (depending on the macro type).
- Global and macro attribute list attributes are substituted in the macro’s markup template.
- The substituted template replaces the macro reference in the output document.


## 22. HTML 5 audio and video block macros

The *html5* backend *audio* and *video* block macros generate the HTML 5 *audio* and *video* elements respectively. They follow the usual AsciiDoc block macro syntax `<name>::<target>[<attrlist>]` where:

| `<name>` | *audio* or *video*. |
|---|---|
| `<target>` | The URL or file name of the video or audio file. |
| `<attrlist>` | A list of named attributes (see below). |

| Name | Value |
|---|---|
| options | A comma separated list of one or more of the following items: *autoplay*, *loop* which correspond to the same-named HTML 5 *audio* element boolean attributes. By default the player *controls* are enabled, include the *nocontrols* option value to hide them. |

| Name | Value |
|---|---|
| height | The height of the player in pixels. |
| width | The width of the player in pixels. |
| poster | The URL or file name of an image representing the video. |
| options | A comma separated list of one or more of the following items: *autoplay*, *loop* and *nocontrols*. The *autoplay* and *loop* options correspond to the same-named HTML 5 *video* element boolean attributes. By default the player *controls* are enabled, include the *nocontrols* option value to hide them. |

Examples:

```
audio::images/example.ogg[]

video::gizmo.ogv[width=200,options="nocontrols,autoplay"]

.Example video

video::gizmo.ogv[]

video::http://www.808.dk/pics/video/gizmo.ogv[]
```

If your needs are more complex put raw HTML 5 in a markup block, for example (from http://www.808.dk/?code-html-5-video):

```
++++

<video poster="pics/video/gizmo.jpg" id="video" style="cursor: pointer;" >

  <source src="pics/video/gizmo.mp4" />

  <source src="pics/video/gizmo.webm" type="video/webm" />

  <source src="pics/video/gizmo.ogv" type="video/ogg" />

  Video not playing? <a href="pics/video/gizmo.mp4">Download file</a> instead.

</video>

<script type="text/javascript">

  var video = document.getElementById('video');

  video.addEventListener('click',function(){

    video.play();

  },false);

</script>

++++
```


## 23. Tables

The AsciiDoc table syntax looks and behaves like other delimited block types and supports standard block configuration entries. Formatting is easy to read and, just as importantly, easy to enter.

- Cells and columns can be formatted using built-in customizable styles.
- Horizontal and vertical cell alignment can be set on columns and cell.
- Horizontal and vertical cell spanning is supported.

Use tables sparingly

When technical users first start creating documents, tables (complete with column spanning and table nesting) are often considered very important. The reality is that tables are seldom used, even in technical documentation.

Try this exercise: thumb through your library of technical books, you’ll be surprised just how seldom tables are actually used, even less seldom are tables containing block elements (such as paragraphs or lists) or spanned cells. This is no accident, like figures, tables are outside the normal document flow — tables are for consulting not for reading.

Tables are designed for, and should normally only be used for, displaying column oriented tabular data.

### 23.1. Example tables

| 1 | 2 | A |
|---|---|---|
| 3 | 4 | B |
| 5 | 6 | C |

AsciiDoc source

```
[width="15%"]

|=======

|1 |2 |A

|3 |4 |B

|5 |6 |C

|=======
```

|   | Columns 2 and 3 |   |
|---|---|---|
| **footer 1** | `footer 2` | *footer 3* |
| **1** | `Item 1` | *Item 1* |
| **2** | `Item 2` | *Item 2* |
| **3** | `Item 3` | *Item 3* |
| **4** | `Item 4` | *Item 4* |

AsciiDoc source

```
.An example table

[width="50%",cols=">s,^m,e",frame="topbot",options="header,footer"]

|==========================

|      2+|Columns 2 and 3

|1       |Item 1  |Item 1

|2       |Item 2  |Item 2

|3       |Item 3  |Item 3

|4       |Item 4  |Item 4

|footer 1|footer 2|footer 3

|==========================
```

| Date | Duration | Avg HR | Notes |
|---|---|---|---|
| 22-Aug-08 | 10:24 | 157 | Worked out MSHR (max sustainable heart rate) by going hard for this interval. |
| 22-Aug-08 | 23:03 | 152 | Back-to-back with previous interval. |
| 24-Aug-08 | 40:00 | 145 | Moderately hard interspersed with 3x 3min intervals (2min hard + 1min really hard taking the HR up to 160). |

Short cells can be entered horizontally, longer cells vertically. The default behavior is to strip leading and trailing blank lines within a cell. These characteristics aid readability and data entry.

AsciiDoc source

```
.Windtrainer workouts

[width="80%",cols="3,^2,^2,10",options="header"]

|=========================================================

|Date |Duration |Avg HR |Notes

|22-Aug-08 |10:24 | 157 |

Worked out MSHR (max sustainable heart rate) by going hard

for this interval.

|22-Aug-08 |23:03 | 152 |

Back-to-back with previous interval.

|24-Aug-08 |40:00 | 145 |

Moderately hard interspersed with 3x 3min intervals (2min

hard + 1min really hard taking the HR up to 160).

|=========================================================
```

| ID | Customer Name | Contact Name | Customer Address | Phone |
|---|---|---|---|---|
| AROUT | Around the Horn | Thomas Hardy | 120 Hanover Sq. London | (171) 555-7788 |
| BERGS | Berglunds snabbkop | Christina Berglund | Berguvsvagen 8 Lulea | 0921-12 34 65 |
| BLAUS | Blauer See Delikatessen | Hanna Moos | Forsterstr. 57 Mannheim | 0621-08460 |
| BLONP | Blondel pere et fils | Frederique Citeaux | 24, place Kleber Strasbourg | 88.60.15.31 |
| BOLID | Bolido Comidas preparadas | Martin Sommer | C/ Araquil, 67 Madrid | (91) 555 22 82 |
| BONAP | Bon app' | Laurence Lebihan | 12, rue des Bouchers Marseille | 91.24.45.40 |
| BOTTM | Bottom-Dollar Markets | Elizabeth Lincoln | 23 Tsawassen Blvd. Tsawassen | (604) 555-4729 |
| BSBEV | B’s Beverages | Victoria Ashworth | Fauntleroy Circus London | (171) 555-1212 |
| CACTU | Cactus Comidas para llevar | Patricio Simpson | Cerrito 333 Buenos Aires | (1) 135-5555 |

AsciiDoc source

```
[format="csv",cols="^1,4*2",options="header"]

|===================================================

ID,Customer Name,Contact Name,Customer Address,Phone

include::customers.csv[]

|===================================================
```

| *1* | **2** | 3 | **4** |
|---|---|---|---|
| *5* | `6` | `7` |   |
| *8* |   |   |   |
| *9* | `10` |   |   |

AsciiDoc source

```
[cols="e,m,^,>s",width="25%"]

|============================

|1 >s|2 |3 |4

^|5 2.2+^.^|6 .3+<.>m|7

^|8

|9 2+>|10

|============================
```

### 23.2. Table input data formats

AsciiDoc table data can be *psv*, *dsv* or *csv* formatted. The default table format is *psv*.

AsciiDoc *psv* (*Prefix Separated Values*) and *dsv* (*Delimiter Separated Values*) formats are cell oriented — the table is treated as a sequence of cells — there are no explicit row separators.

- *psv* prefixes each cell with a separator whereas *dsv* delimits cells with a separator.
- *psv* and *dsv* separators are Python regular expressions.
- The default *psv* separator contains cell specifier related named regular expression groups.
- The default *dsv* separator is `:|\n` (a colon or a new line character).
- *psv* and *dsv* cell separators can be escaped by preceding them with a backslash character.

Here are four *psv* cells (the second item spans two columns; the last contains an escaped separator):

```
|One 2+|Two and three |A \| separator character
```

*csv* is the quasi-standard row oriented *Comma Separated Values (CSV)* format commonly used to import and export spreadsheet and database data.

### 23.3. Table attributes

Tables can be customized by the following attributes:

**format**

*psv* (default), *dsv* or *csv* (See Table Data Formats).

**separator**

The cell separator. A Python regular expression (*psv* and *dsv* formats) or a single character (*csv* format).

**frame**

Defines the table border and can take the following values: *topbot* (top and bottom), *all* (all sides), *none* and *sides* (left and right sides). The default value is *all*.

**grid**

Defines which ruler lines are drawn between table rows and columns. The *grid* attribute value can be any of the following values: *none*, *cols*, *rows* and *all*. The default value is *all*.

**align**

Use the *align* attribute to horizontally align the table on the page (works with HTML outputs only, has no effect on DocBook outputs). The following values are valid: *left*, *right*, and *center*.

**float**

Use the *float* attribute to float the table *left* or *right* on the page (works with HTML outputs only, has no effect on DocBook outputs). Floating only makes sense in conjunction with a table *width* attribute value of less than 100% (otherwise the table will take up all the available space). *float* and *align* attributes are mutually exclusive. Use the `unfloat::[]` block macro to stop floating.

**halign**

Use the *halign* attribute to horizontally align all cells in a table. The following values are valid: *left*, *right*, and *center* (defaults to *left*). Overridden by Column specifiers and Cell specifiers.

**valign**

Use the *valign* attribute to vertically align all cells in a table. The following values are valid: *top*, *bottom*, and *middle* (defaults to *top*). Overridden by Column specifiers and Cell specifiers.

**options**

The *options* attribute can contain comma separated values, for example: *header*, *footer*. By default header and footer rows are omitted. See attribute options for a complete list of available table options.

**cols**

The *cols* attribute is a comma separated list of column specifiers. For example `cols="2<p,2*,4p,>"`.

- If *cols* is present it must specify all columns.
- If the *cols* attribute is not specified the number of columns is calculated as the number of data items in the **first line** of the table.
- The degenerate form for the *cols* attribute is an integer specifying the number of columns e.g. `cols=4`.

**width**

The *width* attribute is expressed as a percentage value (*"1%"*…*"99%"*). The width specifies the table width relative to the available width. HTML backends use this value to set the table width attribute. It’s a bit more complicated with DocBook, see the DocBook table widths sidebar.

**filter**

The *filter* attribute defines an external shell command that is invoked for each cell. The built-in *asciidoc* table style is implemented using a filter.

DocBook table widths

The AsciiDoc docbook backend generates CALS tables. CALS tables do not support a table width attribute — table width can only be controlled by specifying absolute column widths.

Specifying absolute column widths is not media independent because different presentation media have different physical dimensions. To get round this limitation both DocBook XSL Stylesheets and dblatex have implemented table width processing instructions for setting the table width as a percentage of the available width. AsciiDoc emits these processing instructions if the *width* attribute is set along with proportional column widths (the AsciiDoc docbook backend *pageunits* attribute defaults to ***).

To generate DocBook tables with absolute column widths set the *pageunits* attribute to a CALS absolute unit such as *pt* and set the *pagewidth* attribute to match the width of the presentation media.

### 23.4. Column Specifiers

Column specifiers define how columns are rendered and appear in the table cols attribute. A column specifier consists of an optional column multiplier followed by optional alignment, width and style values and is formatted like:

```
[<multiplier>*][<align>][<width>][<style>]
```

- All components are optional. The multiplier must be first and the style last. The order of `<align>` or `<width>` is not important.
- Column `<width>` can be either an integer proportional value (1…) or a percentage (1%…100%). The default value is 1. To ensure portability across different backends, there is no provision for absolute column widths (not to be confused with output column width markup attributes which are available in both percentage and absolute units).
- The *<align>* column alignment specifier is formatted like: `[<horizontal>][.<vertical>]` Where `<horizontal>` and `<vertical>` are one of the following characters: `<`, `^` or `>` which represent *left*, *center* and *right* horizontal alignment or *top*, *middle* and *bottom* vertical alignment respectively.
- A `<multiplier>` can be used to specify repeated columns e.g. `cols="4*<"` specifies four left-justified columns. The default multiplier value is 1.
- The `<style>` name specifies a table style to used to markup column cells (you can use the full style names if you wish but the first letter is normally sufficient).
- Column specific styles are not applied to header rows.

### 23.5. Cell Specifiers

Cell specifiers allow individual cells in *psv* formatted tables to be spanned, multiplied, aligned and styled. Cell specifiers prefix *psv* `|` delimiters and are formatted like:

```
[<span>*|+][<align>][<style>]
```

- *<span>* specifies horizontal and vertical cell spans (*+* operator) or the number of times the cell is replicated (*** operator). *<span>* is formatted like: `[<colspan>][.<rowspan>]` Where `<colspan>` and `<rowspan>` are integers specifying the number of columns and rows to span.
- `<align>` specifies horizontal and vertical cell alignment an is the same as in column specifiers.
- A `<style>` value is the first letter of table style name.

For example, the following *psv* formatted cell will span two columns and the text will be centered and emphasized:

```
`2+^e| Cell text`
```

### 23.6. Table styles

Table styles can be applied to the entire table (by setting the *style* attribute in the table’s attribute list) or on a per column basis (by specifying the style in the table’s cols attribute). Table data can be formatted using the following predefined styles:

**default**

The default style: AsciiDoc inline text formatting; blank lines are treated as paragraph breaks.

**emphasis**

Like default but all text is emphasised.

**monospaced**

Like default but all text is in a monospaced font.

**strong**

Like default but all text is bold.

**header**

Apply the same style as the table header. Normally used to create a vertical header in the first column.

**asciidoc**

With this style table cells can contain any of the AsciiDoc elements that are allowed inside document sections. This style runs `asciidoc(1)` as a filter to process cell contents. See also Docbook table limitations.

**literal**

No text formatting; monospaced font; all line breaks are retained (the same as the AsciiDoc LiteralBlock element).

**verse**

All line breaks are retained (just like the AsciiDoc verse paragraph style).

### 23.7. Markup attributes

AsciiDoc makes a number of attributes available to table markup templates and tags. Column specific attributes are available when substituting the *colspec* cell data tags.

**pageunits**

DocBook backend only. Specifies table column absolute width units. Defaults to ***.

**pagewidth**

DocBook backend only. The nominal output page width in *pageunit* units. Used to calculate CALS tables absolute column and table widths. Defaults to *425*.

**tableabswidth**

Integer value calculated from *width* and *pagewidth* attributes. In *pageunit* units.

**tablepcwidth**

Table width expressed as a percentage of the available width. Integer value (0..100).

**colabswidth**

Integer value calculated from *cols* column width, *width* and *pagewidth* attributes. In *pageunit* units.

**colpcwidth**

Column width expressed as a percentage of the table width. Integer value (0..100).

**colcount**

Total number of table columns.

**rowcount**

Total number of table rows.

**halign**

Horizontal cell content alignment: *left*, *right* or *center*.

**valign**

Vertical cell content alignment: *top*, *bottom* or *middle*.

**colnumber, colstart**

The number of the leftmost column occupied by the cell (1…).

**colend**

The number of the rightmost column occupied by the cell (1…).

**colspan**

Number of columns the cell should span.

**rowspan**

Number of rows the cell should span (1…).

**morerows**

Number of additional rows the cell should span (0…).

### 23.8. Nested tables

An alternative *psv* separator character *!* can be used (instead of *|*) in nested tables. This allows a single level of table nesting. Columns containing nested tables must use the *asciidoc* style. An example can be found in `./examples/website/newtables.txt`.

### 23.9. DocBook table limitations

Fully implementing tables is not trivial, some DocBook toolchains do better than others. AsciiDoc HTML table outputs are rendered correctly in all the popular browsers — if your DocBook generated tables don’t look right compare them with the output generated by the AsciiDoc *xhtml11* backend or try a different DocBook toolchain. Here is a list of things to be aware of:

- Although nested tables are not legal in DocBook 4 the FOP and dblatex toolchains will process them correctly. If you use `a2x(1)` you will need to include the `--no-xmllint` option to suppress DocBook validation errors. (Note) In theory you can nest DocBook 4 tables one level using the *entrytbl* element, but not all toolchains process *entrytbl*.
- DocBook only allows a subset of block elements inside table cells so not all AsciiDoc elements produce valid DocBook inside table cells. If you get validation errors running `a2x(1)` try the `--no-xmllint` option, toolchains will often process nested block elements such as sidebar blocks and floating titles correctly even though, strictly speaking, they are not legal.
- Text formatting in cells using the *monospaced* table style will raise validation errors because the DocBook *literal* element was not designed to support formatted text (using the *literal* element is a kludge on the part of AsciiDoc as there is no easy way to set the font style in DocBook.
- Cell alignments are ignored for *verse*, *literal* or *asciidoc* table styles.


## 24. Manpage Documents

Sooner or later, if you program in a UNIX environment, you’re going to have to write a man page.

By observing a couple of additional conventions (detailed below) you can write AsciiDoc files that will generate HTML and PDF man pages plus the native manpage roff format. The easiest way to generate roff manpages from AsciiDoc source is to use the `a2x(1)` command. The following example generates a roff formatted manpage file called `asciidoc.1` (`a2x(1)` uses `asciidoc(1)` to convert `asciidoc.1.txt` to DocBook which it then converts to roff using DocBook XSL Stylesheets):

```
a2x --doctype manpage --format manpage asciidoc.1.txt
```

Viewing and printing manpage files

Use the `man(1)` command to view the manpage file:

```
$ man -l asciidoc.1
```

To print a high quality man page to a postscript printer:

```
$ man -l -Tps asciidoc.1 | lpr
```

You could also create a PDF version of the man page by converting PostScript to PDF using `ps2pdf(1)`:

```
$ man -l -Tps asciidoc.1 | ps2pdf - asciidoc.1.pdf
```

The `ps2pdf(1)` command is included in the Ghostscript distribution.

To find out more about man pages view the `man(7)` manpage (`man 7 man` and `man man-pages` commands).

### 24.1. Document Header

A manpage document Header is mandatory. The title line contains the man page name followed immediately by the manual section number in brackets, for example *ASCIIDOC(1)*. The title name should not contain white space and the manual section number is a single digit optionally followed by a single character.

### 24.2. The NAME Section

The first manpage section is mandatory, must be titled *NAME* and must contain a single paragraph (usually a single line) consisting of a list of one or more comma separated command name(s) separated from the command purpose by a dash character. The dash must have at least one white space character on either side. For example:

```
printf, fprintf, sprintf - print formatted output
```

### 24.3. The SYNOPSIS Section

The second manpage section is mandatory and must be titled *SYNOPSIS*.

### 24.4. refmiscinfo attributes

In addition to the automatically created man page intrinsic attributes you can assign DocBook refmiscinfo element *source*, *version* and *manual* values using AsciiDoc `{mansource}`, `{manversion}` and `{manmanual}` attributes respectively. This example is from the AsciiDoc header of a man page source file:

```
:man source:   AsciiDoc

:man version:  {revnumber}

:man manual:   AsciiDoc Manual
```


## 25. Mathematical Formulas

The *asciimath* and *latexmath* passthrough blocks along with the *asciimath* and *latexmath* passthrough macros provide a (backend dependent) mechanism for rendering mathematical formulas. You can use the following math markups:

### 25.1. LaTeX Math

LaTeX math can be included in documents that are processed by dblatex(1). Example inline formula:

```
latexmath:[$C = \alpha + \beta Y^{\gamma} + \epsilon$]
```

For more examples see the AsciiDoc website or the distributed `doc/latexmath.txt` file.

### 25.2. MathJax

MathJax allows LaTeX Math style formulas to be included in XHTML documents generated via the AsciiDoc *xhtml11* and *html5* backends. This route overcomes several restrictions of the MathML-based approaches, notably, restricted support of MathML by many mainstream browsers. To enable *MathJax* support you must define the *mathjax* attribute, for example using the `-a mathjax` command-line option. Equations are specified as explained above using the *latexmath* passthrough blocks. By default, rendering of equations with *MathJax* requires a working internet connection and will thus not work if you are offline (but it can be configured differently).

### 25.3. LaTeXMathML

*LaTeXMathML* allows LaTeX Math style formulas to be included in XHTML documents generated using the AsciiDoc *xhtml11* and *html5* backends. AsciiDoc uses the original LaTeXMathML by Douglas Woodall. *LaTeXMathML* is derived from ASCIIMath and is for users who are more familiar with or prefer using LaTeX math formulas (it recognizes a subset of LaTeX Math, the differences are documented on the *LaTeXMathML* web page). To enable LaTeXMathML support you must define the *latexmath* attribute, for example using the `-a latexmath` command-line option. Example inline formula:

```
latexmath:[$\sum_{n=1}^\infty \frac{1}{2^n}$]
```

For more examples see the AsciiDoc website or the distributed `doc/latexmathml.txt` file.

| (Note) | The *latexmath* macro used to include *LaTeX Math* in DocBook outputs is not the same as the *latexmath* macro used to include *LaTeX MathML* in XHTML outputs. *LaTeX Math* applies to DocBook outputs that are processed by dblatex and is normally used to generate PDF files. *LaTeXMathML* is very much a subset of *LaTeX Math* and applies to XHTML documents. This remark does not apply to *MathJax* which does not use any of the *latexmath* macros (but only requires the *latexmath* passthrough blocks for identification of the equations). |
|---|---|

### 25.4. ASCIIMath

ASCIIMath formulas can be included in XHTML documents generated using the *xhtml11* and *html5* backends. To enable ASCIIMath support you must define the *asciimath* attribute, for example using the `-a asciimath` command-line option. Example inline formula:

```
asciimath:[`x/x={(1,if x!=0),(text{undefined},if x=0):}`]
```

For more examples see the AsciiDoc website or the distributed `doc/asciimath.txt` file.

### 25.5. MathML

MathML is a low level XML markup for mathematics. AsciiDoc has no macros for MathML but users familiar with this markup could use passthrough macros and passthrough blocks to include MathML in output documents.
