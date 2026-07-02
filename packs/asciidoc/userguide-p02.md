---
title: "AsciiDoc User Guide (part 2/5)"
source: https://asciidoc.org/userguide.html
domain: asciidoc
license: CC-BY-SA-4.0
tags: asciidoc markup, lightweight markup, asciidoctor docs, text markup
fetched: 2026-07-02
part: 2/5
---

## 14. AttributeList Element

An *AttributeList* block element is an attribute list on a line by itself:

- *AttributeList* attributes are only applied to the immediately following block element — the attributes are made available to the block’s markup template.
- Multiple contiguous *AttributeList* elements are additively combined in the order they appear.
- The first positional attribute in the list is often used to specify the ensuing element’s style.

### 14.1. Attribute value substitution

By default, only substitutions that take place inside attribute list values are attribute references, this is because not all attributes are destined to be marked up and rendered as text (for example the table *cols* attribute). To perform normal inline text substitutions (special characters, quotes, macros, replacements) on an attribute value you need to enclose it in single quotes. In the following quote block the second attribute value in the AttributeList is quoted to ensure the *http* macro is expanded to a hyperlink.

```
[quote,'https://en.wikipedia.org/wiki/Samuel_Johnson[Samuel Johnson]']

_____________________________________________________________________

Sir, a woman's preaching is like a dog's walking on his hind legs. It

is not done well; but you are surprised to find it done at all.

_____________________________________________________________________
```

### 14.2. Common attributes

Most block elements support the following attributes:

| Name | Backends | Description |
|---|---|---|
| *id* | html4, html5, xhtml11, docbook | Unique identifier typically serve as link targets. Can also be set by the *BlockId* element. |
| *role* | html4, html5, xhtml11, docbook | Role contains a string used to classify or subclassify an element and can be applied to AsciiDoc block elements. The AsciiDoc *role* attribute is translated to the *role* attribute in DocBook outputs and is included in the *class* attribute in HTML outputs, in this respect it behaves like the quoted text role attribute. DocBook XSL Stylesheets translate DocBook *role* attributes to HTML *class* attributes; CSS can then be used to style the generated HTML. |
| *reftext* | docbook | *reftext* is used to set the DocBook *xreflabel* attribute. The *reftext* attribute can an also be set by the *BlockId* element. |
| *floatstyle* | docbook | *floatstyle* is used to specify the floatstyle attribute for the titled table, example, image and equation blocks. This is useful when used in conjunction with the dblatex toolchain. A typical example would be to specify the value as *floatstyle="[htbp]"*. |


## 15. Paragraphs

Paragraphs are blocks of text terminated by a blank line, the end of file, or the start of a delimited block or a list. There are three paragraph syntaxes: normal, indented (literal) and admonition which are rendered, by default, with the corresponding paragraph style.

Each syntax has a default style, but you can explicitly apply any paragraph style to any paragraph syntax. You can also apply delimited block styles to single paragraphs.

The built-in paragraph styles are: *normal*, *literal*, *verse*, *quote*, *listing*, *TIP*, *NOTE*, *IMPORTANT*, *WARNING*, *CAUTION*, *abstract*, *partintro*, *comment*, *example*, *sidebar*, *source*, *music*, *latex*, *graphviz*.

### 15.1. normal paragraph syntax

Normal paragraph syntax consists of one or more non-blank lines of text. The first line must start hard against the left margin (no intervening white space). The default processing expectation is that of a normal paragraph of text.

### 15.2. literal paragraph syntax

Literal paragraphs are rendered verbatim in a monospaced font without any distinguishing background or border. By default there is no text formatting or substitutions within Literal paragraphs apart from Special Characters and Callouts.

The *literal* style is applied implicitly to indented paragraphs i.e. where the first line of the paragraph is indented by one or more space or tab characters. For example:

```
  Consul *necessitatibus* per id,

  consetetur, eu pro everti postulant

  homero verear ea mea, qui.
```

Renders:

```
Consul *necessitatibus* per id,

consetetur, eu pro everti postulant

homero verear ea mea, qui.
```

| (Note) | Because lists can be indented it’s possible for your indented paragraph to be misinterpreted as a list — in situations like this apply the *literal* style to a normal paragraph. |
|---|---|

Instead of using a paragraph indent you could apply the *literal* style explicitly, for example:

```
[literal]

Consul *necessitatibus* per id,

consetetur, eu pro everti postulant

homero verear ea mea, qui.
```

Renders:

```
Consul *necessitatibus* per id,

consetetur, eu pro everti postulant

homero verear ea mea, qui.
```

### 15.3. quote and verse paragraph styles

The optional *attribution* and *citetitle* attributes (positional attributes 2 and 3) specify the author and source respectively.

The *verse* style retains the line breaks, for example:

```
[verse, William Blake, from Auguries of Innocence]

To see a world in a grain of sand,

And a heaven in a wild flower,

Hold infinity in the palm of your hand,

And eternity in an hour.
```

Which is rendered as:

```
To see a world in a grain of sand,

And a heaven in a wild flower,

Hold infinity in the palm of your hand,

And eternity in an hour.
```

from Auguries of Innocence

— William Blake

The *quote* style flows the text at left and right margins, for example:

```
[quote, Bertrand Russell, The World of Mathematics (1956)]

A good notation has subtlety and suggestiveness which at times makes

it almost seem like a live teacher.
```

Which is rendered as:

A good notation has subtlety and suggestiveness which at times makes it almost seem like a live teacher.

The World of Mathematics (1956)

— Bertrand Russell

### 15.4. Admonition Paragraphs

*TIP*, *NOTE*, *IMPORTANT*, *WARNING* and *CAUTION* admonishment paragraph styles are generated by placing `NOTE:`, `TIP:`, `IMPORTANT:`, `WARNING:` or `CAUTION:` as the first word of the paragraph. For example:

```
NOTE: This is an example note.
```

Alternatively, you can specify the paragraph admonition style explicitly using an AttributeList element. For example:

```
[NOTE]

This is an example note.
```

Renders:

| (Note) | This is an example note. |
|---|---|

| (Tip) | If your admonition requires more than a single paragraph use an admonition block instead. |
|---|---|

#### 15.4.1. Admonition Icons and Captions

| (Note) | Admonition customization with `icons`, `iconsdir`, `icon` and `caption` attributes does not apply when generating DocBook output. If you are going the DocBook route then the `a2x(1)` `--no-icons` and `--icons-dir` options can be used to set the appropriate XSL Stylesheets parameters. |
|---|---|

By default the `asciidoc(1)` HTML backends generate text captions instead of admonition icon image links. To generate links to icon images define the `icons` attribute, for example using the `-a icons` command-line option.

The `iconsdir` attribute sets the location of linked icon images.

You can override the default icon image using the `icon` attribute to specify the path of the linked image. For example:

```
[icon="./images/icons/wink.png"]

NOTE: What lovely war.
```

Use the `caption` attribute to customize the admonition captions (not applicable to `docbook` backend). The following example suppresses the icon image and customizes the caption of a *NOTE* admonition (undefining the `icons` attribute with `icons=None` is only necessary if admonition icons have been enabled):

```
[icons=None, caption="My Special Note"]

NOTE: This is my special note.
```

This subsection also applies to Admonition Blocks.


## 16. Delimited Blocks

Delimited blocks are blocks of text enveloped by leading and trailing delimiter lines (normally a series of four or more repeated characters). The behavior of Delimited Blocks is specified by entries in configuration file `[blockdef-*]` sections.

### 16.1. Predefined Delimited Blocks

AsciiDoc ships with a number of predefined DelimitedBlocks (see the `asciidoc.conf` configuration file in the `asciidoc(1)` program directory):

Predefined delimited block underlines:

```
CommentBlock:     //////////////////////////

PassthroughBlock: ++++++++++++++++++++++++++

ListingBlock:     --------------------------

LiteralBlock:     ..........................

SidebarBlock:     **************************

QuoteBlock:       __________________________

ExampleBlock:     ==========================

OpenBlock:        --
```

|   | Attributes | Callouts | Macros | Quotes | Replacements | Special chars | Special words |
|---|---|---|---|---|---|---|---|
| *PassthroughBlock* | Yes | No | Yes | No | No | No | No |
| *ListingBlock* | No | Yes | No | No | No | Yes | No |
| *LiteralBlock* | No | Yes | No | No | No | Yes | No |
| *SidebarBlock* | Yes | No | Yes | Yes | Yes | Yes | Yes |
| *QuoteBlock* | Yes | No | Yes | Yes | Yes | Yes | Yes |
| *ExampleBlock* | Yes | No | Yes | Yes | Yes | Yes | Yes |
| *OpenBlock* | Yes | No | Yes | Yes | Yes | Yes | Yes |

### 16.2. Listing Blocks

*ListingBlocks* are rendered verbatim in a monospaced font, they retain line and whitespace formatting and are often distinguished by a background or border. There is no text formatting or substitutions within Listing blocks apart from Special Characters and Callouts. Listing blocks are often used for computer output and file listings.

Here’s an example:

```
--------------------------------------

#include <stdio.h>

int main() {

   printf("Hello World!\n");

   exit(0);

}

--------------------------------------
```

Which will be rendered like:

```
#include <stdio.h>

int main() {

    printf("Hello World!\n");

    exit(0);

}
```

By convention filter blocks use the listing block syntax and are implemented as distinct listing block styles.

### 16.3. Literal Blocks

*LiteralBlocks* are rendered just like literal paragraphs. Example:

```
...................................

Consul *necessitatibus* per id,

consetetur, eu pro everti postulant

homero verear ea mea, qui.

...................................
```

Renders:

```
Consul *necessitatibus* per id,

consetetur, eu pro everti postulant

homero verear ea mea, qui.
```

If the *listing* style is applied to a LiteralBlock it will be rendered as a ListingBlock (this is handy if you have a listing containing a ListingBlock).

A sidebar is a short piece of text presented outside the narrative flow of the main text. The sidebar is normally presented inside a bordered box to set it apart from the main text.

The sidebar body is treated like a normal section body.

Here’s an example:

```
.An Example Sidebar

************************************************

Any AsciiDoc SectionBody element (apart from

SidebarBlocks) can be placed inside a sidebar.

************************************************
```

Which will be rendered like:

An Example Sidebar

Any AsciiDoc SectionBody element (apart from SidebarBlocks) can be placed inside a sidebar.

### 16.5. Comment Blocks

The contents of *CommentBlocks* are not processed; they are useful for annotations and for excluding new or outdated content that you don’t want displayed. CommentBlocks are never written to output files. Example:

```
//////////////////////////////////////////

CommentBlock contents are not processed by

asciidoc(1).

//////////////////////////////////////////
```

See also Comment Lines.

| (Note) | System macros are executed inside comment blocks. |
|---|---|

### 16.6. Passthrough Blocks

By default the block contents is subject only to *attributes* and *macros* substitutions (use an explicit *subs* attribute to apply different substitutions). PassthroughBlock content will often be backend specific. Here’s an example:

```
[subs="quotes"]

++++++++++++++++++++++++++++++++++++++

<table border="1"><tr>

  <td>*Cell 1*</td>

  <td>*Cell 2*</td>

</tr></table>

++++++++++++++++++++++++++++++++++++++
```

The following styles can be applied to passthrough blocks:

**pass**

No substitutions are performed. This is equivalent to `subs="none"`.

**asciimath, latexmath**

By default no substitutions are performed, the contents are rendered as mathematical formulas.

### 16.7. Quote Blocks

*QuoteBlocks* are used for quoted passages of text. There are two styles: *quote* and *verse*. The style behavior is identical to quote and verse paragraphs except that blocks can contain multiple paragraphs and, in the case of the *quote* style, other section elements. The first positional attribute sets the style, if no attributes are specified the *quote* style is used. The optional *attribution* and *citetitle* attributes (positional attributes 2 and 3) specify the quote’s author and source. For example:

```
[quote, Sir Arthur Conan Doyle, The Adventures of Sherlock Holmes]

____________________________________________________________________

As he spoke there was the sharp sound of horses' hoofs and

grating wheels against the curb, followed by a sharp pull at the

bell. Holmes whistled.

"A pair, by the sound," said he. "Yes," he continued, glancing

out of the window. "A nice little brougham and a pair of

beauties. A hundred and fifty guineas apiece. There's money in

this case, Watson, if there is nothing else."

____________________________________________________________________
```

Which is rendered as:

As he spoke there was the sharp sound of horses' hoofs and grating wheels against the curb, followed by a sharp pull at the bell. Holmes whistled.

"A pair, by the sound," said he. "Yes," he continued, glancing out of the window. "A nice little brougham and a pair of beauties. A hundred and fifty guineas apiece. There’s money in this case, Watson, if there is nothing else."

The Adventures of Sherlock Holmes

— Sir Arthur Conan Doyle

### 16.8. Example Blocks

*ExampleBlocks* encapsulate the DocBook Example element and are used for, well, examples. Example blocks can be titled by preceding them with a *BlockTitle*. DocBook toolchains will normally automatically number examples and generate a *List of Examples* backmatter section.

Example blocks are delimited by lines of equals characters and can contain any block elements apart from Titles, BlockTitles and Sidebars) inside an example block. For example:

```
.An example

=====================================================================

Qui in magna commodo, est labitur dolorum an. Est ne magna primis

adolescens.

=====================================================================
```

Renders:

Example 1. An example

Qui in magna commodo, est labitur dolorum an. Est ne magna primis adolescens.

A title prefix that can be inserted with the `caption` attribute (HTML backends). For example:

```
[caption="Example 1: "]

.An example with a custom caption

=====================================================================

Qui in magna commodo, est labitur dolorum an. Est ne magna primis

adolescens.

=====================================================================
```

### 16.9. Admonition Blocks

The *ExampleBlock* definition includes a set of admonition styles (*NOTE*, *TIP*, *IMPORTANT*, *WARNING*, *CAUTION*) for generating admonition blocks (admonitions containing more than a single paragraph). Just precede the *ExampleBlock* with an attribute list specifying the admonition style name. For example:

```
[NOTE]

.A NOTE admonition block

=====================================================================

Qui in magna commodo, est labitur dolorum an. Est ne magna primis

adolescens.

. Fusce euismod commodo velit.

. Vivamus fringilla mi eu lacus.

  .. Fusce euismod commodo velit.

  .. Vivamus fringilla mi eu lacus.

. Donec eget arcu bibendum

  nunc consequat lobortis.

=====================================================================
```

Renders:

| (Note) | A NOTE admonition block Qui in magna commodo, est labitur dolorum an. Est ne magna primis adolescens. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis. |
|---|---|

See also Admonition Icons and Captions.

### 16.10. Open Blocks

Open blocks are special:

- The open block delimiter is line containing two hyphen characters (instead of four or more repeated characters).
- They can be used to group block elements for List item continuation.
- Open blocks can be styled to behave like any other type of delimited block. The following built-in styles can be applied to open blocks: *literal*, *verse*, *quote*, *listing*, *TIP*, *NOTE*, *IMPORTANT*, *WARNING*, *CAUTION*, *abstract*, *partintro*, *comment*, *example*, *sidebar*, *source*, *music*, *latex*, *graphviz*. For example, the following open block and listing block are functionally identical: `[listing] -- Lorum ipsum ... --` `--------------- Lorum ipsum ... ---------------`
- An unstyled open block groups section elements but otherwise does nothing.

Open blocks are used to generate document abstracts and book part introductions:

- Apply the *abstract* style to generate an abstract, for example: `[abstract] -- In this paper we will ... --` Apply the *partintro* style to generate a book part introduction for a multi-part book, for example: `[partintro] .Optional part introduction title -- Optional part introduction goes here. --`


## 17. Lists

List types

- Bulleted lists. Also known as itemized or unordered lists.
- Numbered lists. Also called ordered lists.
- Labeled lists. Sometimes called variable or definition lists.
- Callout lists (a list of callout annotations).

List behavior

- List item indentation is optional and does not determine nesting, indentation does however make the source more readable.
- Another list or a literal paragraph immediately following a list item will be implicitly included in the list item; use list item continuation to explicitly append other block elements to a list item.
- A comment block or a comment line block macro element will terminate a list — use inline comment lines to put comments inside lists.
- The `listindex` intrinsic attribute is the current list item index (1..). If this attribute is used outside a list then it’s value is the number of items in the most recently closed list. Useful for displaying the number of items in a list.

### 17.1. Bulleted Lists

Bulleted list items start with a single dash or one to five asterisks followed by some white space then some text. Bulleted list syntaxes are:

```
- List item.

* List item.

** List item.

*** List item.

**** List item.

***** List item.
```

### 17.2. Numbered Lists

List item numbers are explicit or implicit.

Explicit numbering

List items begin with a number followed by some white space then the item text. The numbers can be decimal (arabic), roman (upper or lower case) or alpha (upper or lower case). Decimal and alpha numbers are terminated with a period, roman numbers are terminated with a closing parenthesis. The different terminators are necessary to ensure *i*, *v* and *x* roman numbers are are distinguishable from *x*, *v* and *x* alpha numbers. Examples:

```
1.   Arabic (decimal) numbered list item.

a.   Lower case alpha (letter) numbered list item.

F.   Upper case alpha (letter) numbered list item.

iii) Lower case roman numbered list item.

IX)  Upper case roman numbered list item.
```

Implicit numbering

List items begin one to five period characters, followed by some white space then the item text. Examples:

```
. Arabic (decimal) numbered list item.

.. Lower case alpha (letter) numbered list item.

... Lower case roman numbered list item.

.... Upper case alpha (letter) numbered list item.

..... Upper case roman numbered list item.
```

You can use the *style* attribute (also the first positional attribute) to specify an alternative numbering style. The numbered list style can be one of the following values: *arabic*, *loweralpha*, *upperalpha*, *lowerroman*, *upperroman*.

Here are some examples of bulleted and numbered lists:

```
- Praesent eget purus quis magna eleifend eleifend.

  1. Fusce euismod commodo velit.

    a. Fusce euismod commodo velit.

    b. Vivamus fringilla mi eu lacus.

    c. Donec eget arcu bibendum nunc consequat lobortis.

  2. Vivamus fringilla mi eu lacus.

    i)  Fusce euismod commodo velit.

    ii) Vivamus fringilla mi eu lacus.

  3. Donec eget arcu bibendum nunc consequat lobortis.

  4. Nam fermentum mattis ante.

- Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

  * Fusce euismod commodo velit.

  ** Qui in magna commodo, est labitur dolorum an. Est ne magna primis

     adolescens. Sit munere ponderum dignissim et. Minim luptatum et

     vel.

  ** Vivamus fringilla mi eu lacus.

  * Donec eget arcu bibendum nunc consequat lobortis.

- Nulla porttitor vulputate libero.

  . Fusce euismod commodo velit.

  . Vivamus fringilla mi eu lacus.

[upperroman]

    .. Fusce euismod commodo velit.

    .. Vivamus fringilla mi eu lacus.

  . Donec eget arcu bibendum nunc consequat lobortis.
```

Which render as:

- Praesent eget purus quis magna eleifend eleifend. Fusce euismod commodo velit. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis. Vivamus fringilla mi eu lacus. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis. Nam fermentum mattis ante.
- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Fusce euismod commodo velit. Qui in magna commodo, est labitur dolorum an. Est ne magna primis adolescens. Sit munere ponderum dignissim et. Minim luptatum et vel. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis.
- Nulla porttitor vulputate libero. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Fusce euismod commodo velit. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis.

A predefined *compact* option is available to bulleted and numbered lists — this translates to the DocBook *spacing="compact"* lists attribute which may or may not be processed by the DocBook toolchain. Example:

```
[options="compact"]

- Compact list item.

- Another compact list item.
```

| (Tip) | To apply the *compact* option globally define a document-wide *compact-option* attribute, e.g. using the `-a compact-option` command-line option. |
|---|---|

You can set the list start number using the *start* attribute (works for HTML outputs and DocBook outputs processed by DocBook XSL Stylesheets). Example:

```
[start=7]

. List item 7.

. List item 8.
```

### 17.3. Labeled Lists

Labeled list items consist of one or more text labels followed by the text of the list item.

An item label begins a line with an alphanumeric character hard against the left margin and ends with two, three or four colons or two semi-colons. A list item can have multiple labels, one per line.

The list item text consists of one or more lines of text starting after the last label (either on the same line or a new line) and can be followed by nested List or ListParagraph elements. Item text can be optionally indented.

Here are some examples:

```
In::

Lorem::

  Fusce euismod commodo velit.

  Fusce euismod commodo velit.

Ipsum:: Vivamus fringilla mi eu lacus.

  * Vivamus fringilla mi eu lacus.

  * Donec eget arcu bibendum nunc consequat lobortis.

Dolor::

  Donec eget arcu bibendum nunc consequat lobortis.

  Suspendisse;;

    A massa id sem aliquam auctor.

  Morbi;;

    Pretium nulla vel lorem.

  In;;

    Dictum mauris in urna.

    Vivamus::: Fringilla mi eu lacus.

    Donec:::   Eget arcu bibendum nunc consequat lobortis.
```

Which render as:

**In**

**Lorem**

Fusce euismod commodo velit.

```
Fusce euismod commodo velit.
```

**Ipsum**

Vivamus fringilla mi eu lacus.

- Vivamus fringilla mi eu lacus.
- Donec eget arcu bibendum nunc consequat lobortis.

**Dolor**

Donec eget arcu bibendum nunc consequat lobortis.

**Suspendisse**

A massa id sem aliquam auctor.

**Morbi**

Pretium nulla vel lorem.

**In**

Dictum mauris in urna.

**Vivamus**

Fringilla mi eu lacus.

**Donec**

Eget arcu bibendum nunc consequat lobortis.

#### 17.3.1. Horizontal labeled list style

The *horizontal* labeled list style (also the first positional attribute) places the list text side-by-side with the label instead of under the label. Here is an example:

```
[horizontal]

*Lorem*:: Fusce euismod commodo velit.  Qui in magna commodo, est

labitur dolorum an. Est ne magna primis adolescens.

  Fusce euismod commodo velit.

*Ipsum*:: Vivamus fringilla mi eu lacus.

- Vivamus fringilla mi eu lacus.

- Donec eget arcu bibendum nunc consequat lobortis.

*Dolor*::

  - Vivamus fringilla mi eu lacus.

  - Donec eget arcu bibendum nunc consequat lobortis.
```

Which render as:

| **Lorem** | Fusce euismod commodo velit. Qui in magna commodo, est labitur dolorum an. Est ne magna primis adolescens. `Fusce euismod commodo velit.` |
|---|---|
| **Ipsum** | Vivamus fringilla mi eu lacus. Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis. |
| **Dolor** | Vivamus fringilla mi eu lacus. Donec eget arcu bibendum nunc consequat lobortis. |

| (Note) | Current PDF toolchains do not make a good job of determining the relative column widths for horizontal labeled lists. Nested horizontal labeled lists will generate DocBook validation errors because the *DocBook XML V4.2* DTD does not permit nested informal tables (although DocBook XSL Stylesheets and dblatex process them correctly). The label width can be set as a percentage of the total width by setting the *width* attribute e.g. `width="10%"` |
|---|---|

### 17.4. Question and Answer Lists

AsciiDoc comes pre-configured with a *qanda* style labeled list for generating DocBook question and answer (Q&A) lists. Example:

```
[qanda]

Question one::

        Answer one.

Question two::

        Answer two.
```

Renders:

1. *Question one* Answer one.
2. *Question two* Answer two.

### 17.5. Glossary Lists

AsciiDoc comes pre-configured with a *glossary* style labeled list for generating DocBook glossary lists. Example:

```
[glossary]

A glossary term::

    The corresponding definition.

A second glossary term::

    The corresponding definition.
```

For working examples see the `article.txt` and `book.txt` documents in the AsciiDoc `./doc` distribution directory.

| (Note) | To generate valid DocBook output glossary lists must be located in a section that uses the *glossary* section markup template. |
|---|---|

### 17.6. Bibliography Lists

AsciiDoc comes with a predefined *bibliography* bulleted list style generating DocBook bibliography entries. Example:

```
[bibliography]

.Optional list title

- [[[taoup]]] Eric Steven Raymond. 'The Art of UNIX

  Programming'. Addison-Wesley. ISBN 0-13-142901-9.

- [[[walsh-muellner]]] Norman Walsh & Leonard Muellner.

  'DocBook - The Definitive Guide'. O'Reilly & Associates. 1999.

  ISBN 1-56592-580-7.
```

The `[[[<reference>]]]` syntax is a bibliography entry anchor, it generates an anchor named `<reference>` and additionally displays `[<reference>]` at the anchor position. For example `[[[taoup]]]` generates an anchor named `taoup` that displays `[taoup]` at the anchor position. Cite the reference from elsewhere your document using `<<taoup>>`, this displays a hyperlink (`[taoup]`) to the corresponding bibliography entry anchor.

For working examples see the `article.txt` and `book.txt` documents in the AsciiDoc `./doc` distribution directory.

| (Note) | To generate valid DocBook output bibliography lists must be located in a bibliography section. |
|---|---|

### 17.7. List Item Continuation

Another list or a literal paragraph immediately following a list item is implicitly appended to the list item; to append other block elements to a list item you need to explicitly join them to the list item with a *list continuation* (a separator line containing a single plus character). Multiple block elements can be appended to a list item using list continuations (provided they are legal list item children in the backend markup).

Here are some examples of list item continuations: list item one contains multiple continuations; list item two is continued with an OpenBlock containing multiple elements:

```
1. List item one.

+

List item one continued with a second paragraph followed by an

Indented block.

+

.................

$ ls *.sh

$ mv *.sh ~/tmp

.................

+

List item continued with a third paragraph.

2. List item two continued with an open block.

+

--

This paragraph is part of the preceding list item.

a. This list is nested and does not require explicit item continuation.

+

This paragraph is part of the preceding list item.

b. List item b.

This paragraph belongs to item two of the outer list.

--
```

Renders:

1. List item one. List item one continued with a second paragraph followed by an Indented block. `$ ls *.sh $ mv *.sh ~/tmp` List item continued with a third paragraph.
2. List item two continued with an open block. This paragraph is part of the preceding list item. This list is nested and does not require explicit item continuation. This paragraph is part of the preceding list item. List item b. This paragraph belongs to item two of the outer list.


## 18. Footnotes

The shipped AsciiDoc configuration includes three footnote inline macros:

**`footnote:[<text>]`**

Generates a footnote with text `<text>`.

**`footnoteref:[<id>,<text>]`**

Generates a footnote with a reference ID `<id>` and text `<text>`.

**`footnoteref:[<id>]`**

Generates a reference to the footnote with ID `<id>`.

The footnote text can span multiple lines.

The *xhtml11* and *html5* backends render footnotes dynamically using JavaScript; *html4* outputs do not use JavaScript and leave the footnotes inline; *docbook* footnotes are processed by the downstream DocBook toolchain.

Example footnotes:

```
A footnote footnote:[An example footnote.];

a second footnote with a reference ID footnoteref:[note2,Second footnote.];

finally a reference to the second footnote footnoteref:[note2].
```

Renders:

A footnote [An example footnote.] ; a second footnote with a reference ID [Second footnote.] ; finally a reference to the second footnote [note2] .


## 19. Indexes

The shipped AsciiDoc configuration includes the inline macros for generating DocBook index entries.

**`indexterm:[<primary>,<secondary>,<tertiary>]`**

**`(((<primary>,<secondary>,<tertiary>)))`**

This inline macro generates an index term (the `<secondary>` and `<tertiary>` positional attributes are optional). Example: `indexterm:[Tigers,Big cats]` (or, using the alternative syntax `(((Tigers,Big cats)))`. Index terms that have secondary and tertiary entries also generate separate index terms for the secondary and tertiary entries. The index terms appear in the index, not the primary text flow.

**`indexterm2:[<primary>]`**

**`((<primary>))`**

This inline macro generates an index term that appears in both the index and the primary text flow. The `<primary>` should not be padded to the left or right with white space characters.

For working examples see the `article.txt` and `book.txt` documents in the AsciiDoc `./doc` distribution directory.

| (Note) | Index entries only really make sense if you are generating DocBook markup — DocBook conversion programs automatically generate an index at the point an *Index* section appears in source document. |
|---|---|


## 20. Callouts

Callouts are a mechanism for annotating verbatim text (for example: source code, computer output and user input). Callout markers are placed inside the annotated text while the actual annotations are presented in a callout list after the annotated text. Here’s an example:

```
 .MS-DOS directory listing

 -----------------------------------------------------

 10/17/97   9:04         <DIR>    bin

 10/16/97  14:11         <DIR>    DOS            <1>

 10/16/97  14:40         <DIR>    Program Files

 10/16/97  14:46         <DIR>    TEMP

 10/17/97   9:04         <DIR>    tmp

 10/16/97  14:37         <DIR>    WINNT

 10/16/97  14:25             119  AUTOEXEC.BAT   <2>

  2/13/94   6:21          54,619  COMMAND.COM    <2>

 10/16/97  14:25             115  CONFIG.SYS     <2>

 11/16/97  17:17      61,865,984  pagefile.sys

  2/13/94   6:21           9,349  WINA20.386     <3>

 -----------------------------------------------------

 <1> This directory holds MS-DOS.

 <2> System startup code for DOS.

 <3> Some sort of Windows 3.1 hack.
```

Which renders:

MS-DOS directory listing

```
10/17/97   9:04         <DIR>    bin

10/16/97  14:11         <DIR>    DOS            

10/16/97  14:40         <DIR>    Program Files

10/16/97  14:46         <DIR>    TEMP

10/17/97   9:04         <DIR>    tmp

10/16/97  14:37         <DIR>    WINNT

10/16/97  14:25             119  AUTOEXEC.BAT   

 2/13/94   6:21          54,619  COMMAND.COM    

10/16/97  14:25             115  CONFIG.SYS     

11/16/97  17:17      61,865,984  pagefile.sys

 2/13/94   6:21           9,349  WINA20.386     
```

| (1) | This directory holds MS-DOS. |
|---|---|
| (2) | System startup code for DOS. |
| (3) | Some sort of Windows 3.1 hack. |

Explanation

- The callout marks are whole numbers enclosed in angle brackets —  they refer to the correspondingly numbered item in the following callout list.
- By default callout marks are confined to *LiteralParagraphs*, *LiteralBlocks* and *ListingBlocks* (although this is a configuration file option and can be changed).
- Callout list item numbering is fairly relaxed — list items can start with `<n>`, `n>` or `>` where `n` is the optional list item number (in the latter case list items starting with a single `>` character are implicitly numbered starting at one).
- Callout lists should not be nested.
- Callout lists cannot be used within tables.
- Callout lists start list items hard against the left margin.
- If you want to present a number inside angle brackets you’ll need to escape it with a backslash to prevent it being interpreted as a callout mark.

| (Note) | Define the AsciiDoc *icons* attribute (for example using the `-a icons` command-line option) to display callout icons. |
|---|---|

### 20.1. Implementation Notes

Callout marks are generated by the *callout* inline macro while callout lists are generated using the *callout* list definition. The *callout* macro and *callout* list are special in that they work together. The *callout* inline macro is not enabled by the normal *macros* substitutions option, instead it has its own *callouts* substitution option.

The following attributes are available during inline callout macro substitution:

**`{index}`**

The callout list item index inside the angle brackets.

**`{coid}`**

An identifier formatted like `CO<listnumber>-<index>` that uniquely identifies the callout mark. For example `CO2-4` identifies the fourth callout mark in the second set of callout marks.

The `{coids}` attribute can be used during callout list item substitution — it is a space delimited list of callout IDs that refer to the explanatory list item.

### 20.2. Including callouts in included code

You can annotate working code examples with callouts — just remember to put the callouts inside source code comments. This example displays the `test.py` source file (containing a single callout) using the *source* (code highlighter) filter:

AsciiDoc source

```
 [source,python]

 -------------------------------------------

 \include::test.py[]

 -------------------------------------------

 <1> Print statement.
```

Included

test.py

source

```
print 'Hello World!'   # <1>
```
