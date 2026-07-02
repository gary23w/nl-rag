---
title: "AsciiDoc User Guide (part 4/5)"
source: https://asciidoc.org/userguide.html
domain: asciidoc
license: CC-BY-SA-4.0
tags: asciidoc markup, lightweight markup, asciidoctor docs, text markup
fetched: 2026-07-02
part: 4/5
---

## 26. Configuration Files

AsciiDoc source file syntax and output file markup is largely controlled by a set of cascading, text based, configuration files. At runtime The AsciiDoc default configuration files are combined with optional user and document specific configuration files.

### 26.1. Configuration File Format

Configuration files contain named sections. Each section begins with a section name in square brackets []. The section body consists of the lines of text between adjacent section headings.

- Section names consist of one or more alphanumeric, underscore or dash characters and cannot begin or end with a dash.
- Lines starting with a *#* character are treated as comments and ignored.
- If the section name is prefixed with a *+* character then the section contents is appended to the contents of an already existing same-named section.
- Otherwise same-named sections and section entries override previously loaded sections and section entries (this is sometimes referred to as *cascading*). Consequently, downstream configuration files need only contain those sections and section entries that need to be overridden.

| (Tip) | When creating custom configuration files you only need to include the sections and entries that differ from the default configuration. |
|---|---|

| (Tip) | The best way to learn about configuration files is to read the default configuration files in the AsciiDoc distribution in conjunction with `asciidoc(1)` output files. You can view configuration file load sequence by turning on the `asciidoc(1)` `-v` (`--verbose`) command-line option. |
|---|---|

AsciiDoc reserves the following section names for specific purposes:

**miscellaneous**

Configuration options that don’t belong anywhere else.

**attributes**

Attribute name/value entries.

**specialcharacters**

Special characters reserved by the backend markup.

**tags**

Backend markup tags.

**quotes**

Definitions for quoted inline character formatting.

**specialwords**

Lists of words and phrases singled out for special markup.

**replacements, replacements2, replacements3**

Find and replace substitution definitions.

**specialsections**

Used to single out special section names for specific markup.

**macros**

Macro syntax definitions.

**titles**

Heading, section and block title definitions.

**paradef-***

Paragraph element definitions.

**blockdef-***

DelimitedBlock element definitions.

**listdef-***

List element definitions.

**listtags-***

List element tag definitions.

**tabledef-***

Table element definitions.

**tabletags-***

Table element tag definitions.

Each line of text in these sections is a *section entry*. Section entries share the following syntax:

**name=value**

The entry value is set to value.

**name=**

The entry value is set to a zero length string.

**name!**

The entry is undefined (deleted from the configuration). This syntax only applies to *attributes* and *miscellaneous* sections.

Section entry behavior

- All equals characters inside the `name` must be escaped with a backslash character.
- `name` and `value` are stripped of leading and trailing white space.
- Attribute names, tag entry names and markup template section names consist of one or more alphanumeric, underscore or dash characters. Names should not begin or end with a dash.
- A blank configuration file section (one without any entries) deletes any preceding section with the same name (applies to non-markup template sections).

### 26.2. Miscellaneous section

The optional `[miscellaneous]` section specifies the following `name=value` options:

**newline**

Output file line termination characters. Can include any valid Python string escape sequences. The default value is `\r\n` (carriage return, line feed). Should not be quoted or contain explicit spaces (use `\x20` instead). For example:

```
$ asciidoc -a 'newline=\n' -b docbook mydoc.txt
```

**outfilesuffix**

The default extension for the output file, for example `outfilesuffix=.html`. Defaults to backend name.

**tabsize**

The number of spaces to expand tab characters, for example `tabsize=4`. Defaults to 8. A *tabsize* of zero suppresses tab expansion (useful when piping included files through block filters). Included files can override this option using the *tabsize* attribute.

**pagewidth, pageunits**

These global table related options are documented in the Table Configuration File Definitions sub-section.

| (Note) | `[miscellaneous]` configuration file entries can be set using the `asciidoc(1)` `-a` (`--attribute`) command-line option. |
|---|---|

### 26.3. Titles section

**sectiontitle**

Two line section title pattern. The entry value is a Python regular expression containing the named group *title*.

**underlines**

A comma separated list of document and section title underline character pairs starting with the section level 0 and ending with section level 4 underline. The default setting is:

```
underlines="==","--","~~","^^","++"
```

**sect0…sect4**

One line section title patterns. The entry value is a Python regular expression containing the named group *title*.

**blocktitle**

BlockTitle element pattern. The entry value is a Python regular expression containing the named group *title*.

**subs**

A comma separated list of substitutions that are performed on the document header and section titles. Defaults to *normal* substitution.

### 26.4. Tags section

The `[tags]` section contains backend tag definitions (one per line). Tags are used to translate AsciiDoc elements to backend markup.

An AsciiDoc tag definition is formatted like `<tagname>=<starttag>|<endtag>`. For example:

```
emphasis=<em>|</em>
```

In this example `asciidoc(1)` replaces the | character with the emphasized text from the AsciiDoc input file and writes the result to the output file.

Use the `{brvbar}` attribute reference if you need to include a | pipe character inside tag text.

### 26.5. Attributes section

The optional `[attributes]` section contains predefined attributes.

If the attribute value requires leading or trailing spaces then the text text should be enclosed in quotation mark (") characters.

To delete a attribute insert a `name!` entry in a downstream configuration file or use the `asciidoc(1)` `--attribute name!` command-line option (an attribute name suffixed with a `!` character deletes the attribute)

### 26.6. Special Characters section

The `[specialcharacters]` section specifies how to escape characters reserved by the backend markup. Each translation is specified on a single line formatted like:

```
<special_character>=<translated_characters>
```

Special characters are normally confined to those that resolve markup ambiguity (in the case of HTML and XML markups the ampersand, less than and greater than characters). The following example causes all occurrences of the `<` character to be replaced by `&lt;`.

```
<=&lt;
```

### 26.7. Quoted Text section

Quoting is used primarily for text formatting. The `[quotes]` section defines AsciiDoc quoting characters and their corresponding backend markup tags. Each section entry value is the name of a of a `[tags]` section entry. The entry name is the character (or characters) that quote the text. The following examples are taken from AsciiDoc configuration files:

```
[quotes]

_=emphasis
```

```
[tags]

emphasis=<em>|</em>
```

You can specify the left and right quote strings separately by separating them with a | character, for example:

```
``|''=quoted
```

Omitting the tag will disable quoting, for example, if you don’t want superscripts or subscripts put the following in a custom configuration file or edit the global `asciidoc.conf` configuration file:

```
[quotes]

^=

~=
```

Unconstrained quotes are differentiated from constrained quotes by prefixing the tag name with a hash character, for example:

```
__=#emphasis
```

Quoted text behavior

- Quote characters must be non-alphanumeric.
- To minimize quoting ambiguity try not to use the same quote characters in different quote types.

### 26.8. Special Words section

The `[specialwords]` section is used to single out words and phrases that you want to consistently format in some way throughout your document without having to repeatedly specify the markup. The name of each entry corresponds to a markup template section and the entry value consists of a list of words and phrases to be marked up. For example:

```
[specialwords]

strongwords=NOTE IMPORTANT
```

```
[strongwords]

<strong>{words}</strong>
```

The examples specifies that any occurrence of `NOTE` or `IMPORTANT` should appear in a bold font.

Words and word phrases are treated as Python regular expressions: for example, the word `^NOTE` would only match `NOTE` if appeared at the start of a line.

AsciiDoc comes with three built-in Special Word types: *emphasizedwords*, *monospacedwords* and *strongwords*, each has a corresponding (backend specific) markup template section. Edit the configuration files to customize existing Special Words and to add new ones.

Special word behavior

- Word list entries must be separated by space characters.
- Word list entries with embedded spaces should be enclosed in quotation (") characters.
- A `[specialwords]` section entry of the form `name=word1 [word2…]` adds words to existing `name` entries.
- A `[specialwords]` section entry of the form `name` undefines (deletes) all existing `name` words.
- Since word list entries are processed as Python regular expressions you need to be careful to escape regular expression special characters.
- By default Special Words are substituted before Inline Macros, this may lead to undesirable consequences. For example the special word `foobar` would be expanded inside the macro call `http://www.foobar.com[]`. A possible solution is to emphasize whole words only by defining the word using regular expression characters, for example `\bfoobar\b`.
- If the first matched character of a special word is a backslash then the remaining characters are output without markup i.e. the backslash can be used to escape special word markup. For example the special word `\\?\b[Tt]en\b` will mark up the words `Ten` and `ten` only if they are not preceded by a backslash.

### 26.9. Replacements section

`[replacements]`, `[replacements2]` and `[replacements3]` configuration file entries specify find and replace text and are formatted like:

```
<find_pattern>=<replacement_text>
```

The find text can be a Python regular expression; the replace text can contain Python regular expression group references.

Use Replacement shortcuts for often used macro references, for example (the second replacement allows us to backslash escape the macro name):

```
NEW!=image:./images/smallnew.png[New!]

\\NEW!=NEW!
```

The only difference between the three replacement types is how they are applied. By default *replacements* and *replacements2* are applied in normal substitution contexts whereas *replacements3* needs to be configured explicitly and should only be used in backend configuration files.

Replacement behavior

- The built-in replacements can be escaped with a backslash.
- If the find or replace text has leading or trailing spaces then the text should be enclosed in quotation (") characters.
- Since the find text is processed as a regular expression you need to be careful to escape regular expression special characters.
- Replacements are performed in the same order they appear in the configuration file replacements section.

### 26.10. Markup Template Sections

Markup template sections supply backend markup for translating AsciiDoc elements. Since the text is normally backend dependent you’ll find these sections in the backend specific configuration files. Template sections differ from other sections in that they contain a single block of text instead of per line *name=value* entries. A markup template section body can contain:

- Attribute references
- System macro calls.
- A document content placeholder

The document content placeholder is a single | character and is replaced by text from the source element. Use the `{brvbar}` attribute reference if you need a literal | character in the template.

### 26.11. Configuration file names, precedence and locations

Configuration files have a `.conf` file name extension; they are loaded from the following locations:

1. The directory containing the asciidoc executable.
2. If there is no `asciidoc.conf` file in the directory containing the asciidoc executable then load from the global configuration directory (normally `/etc/asciidoc` or `/usr/local/etc/asciidoc`) i.e. the global configuration files directory is skipped if AsciiDoc configuration files are installed in the same directory as the asciidoc executable. This allows both a system wide copy and multiple local copies of AsciiDoc to coexist on the same host PC.
3. The user’s `$HOME/.asciidoc` directory (if it exists).
4. The directory containing the AsciiDoc source file.
5. Explicit configuration files specified using: The `conf-files` attribute (one or more file names separated by a `|` character). These files are loaded in the order they are specified and prior to files specified using the `--conf-file` command-line option. The `asciidoc(1)` `--conf-file`) command-line option. The `--conf-file` option can be specified multiple times, in which case configuration files will be processed in the same order they appear on the command-line.
6. Backend plugin configuration files are loaded from subdirectories named like `backends/<backend>` in locations 1, 2 and 3.
7. Filter configuration files are loaded from subdirectories named like `filters/<filter>` in locations 1, 2 and 3.

Configuration files from the above locations are loaded in the following order:

- The `[attributes]` section only from: `asciidoc.conf` in location 3 Files from location 5. This first pass makes locally set attributes available in the global `asciidoc.conf` file.
- `asciidoc.conf` from locations 1, 2, 3.
- *attributes*, *titles* and *specialcharacters* sections from the `asciidoc.conf` in location 4.
- The document header is parsed at this point and we can assume the *backend* and *doctype* have now been defined.
- Backend plugin `<backend>.conf` and `<backend>-<doctype>.conf` files from locations 6. If a backend plugin is not found then try locations 1, 2 and 3 for `<backend>.conf` and `<backend>-<doctype>.conf` backend configuration files.
- Filter conf files from locations 7.
- `lang-<lang>.conf` from locations 1, 2, 3.
- `asciidoc.conf` from location 4.
- `<backend>.conf` and `<backend>-<doctype>.conf` from location 4.
- Filter conf files from location 4.
- `<docfile>.conf` and `<docfile>-<backend>.conf` from location 4.
- Configuration files from location 5.

Where:

- `<backend>` and `<doctype>` are values specified by the `asciidoc(1)` `-b` (`--backend`) and `-d` (`--doctype`) command-line options.
- `<infile>` is the path name of the AsciiDoc input file without the file name extension.
- `<lang>` is a two letter country code set by the the AsciiDoc *lang* attribute.

| (Note) | The backend and language global configuration files are loaded **after** the header has been parsed. This means that you can set most attributes in the document header. Here’s an example header: `Life's Mysteries ================ :author: Hu Nose :doctype: book :toc: :icons: :data-uri: :lang: en :encoding: iso-8859-1` Attributes set in the document header take precedence over configuration file attributes. |
|---|---|

| (Tip) | Use the `asciidoc(1)` `-v` (`--verbose`) command-line option to see which configuration files are loaded and the order in which they are loaded. |
|---|---|


## 27. Document Attributes

A document attribute is comprised of a *name* and a textual *value* and is used for textual substitution in AsciiDoc documents and configuration files. An attribute reference (an attribute name enclosed in braces) is replaced by the corresponding attribute value. Attribute names are case insensitive and can only contain alphanumeric, dash and underscore characters.

There are four sources of document attributes (from highest to lowest precedence):

- Command-line attributes.
- AttributeEntry, AttributeList, Macro and BlockId elements.
- Configuration file `[attributes]` sections.
- Intrinsic attributes.

Within each of these divisions the last processed entry takes precedence.

| (Note) | If an attribute is not defined then the line containing the attribute reference is dropped. This property is used extensively in AsciiDoc configuration files to facilitate conditional markup generation. |
|---|---|


## 28. Attribute Entries

The `AttributeEntry` block element allows document attributes to be assigned within an AsciiDoc document. Attribute entries are added to the global document attributes dictionary. The attribute name/value syntax is a single line like:

```
:<name>: <value>
```

For example:

```
:Author Initials: JB
```

This will set an attribute reference `{authorinitials}` to the value *JB* in the current document.

To delete (undefine) an attribute use the following syntax:

```
:<name>!:
```

AttributeEntry behavior

- The attribute entry line begins with colon — no white space allowed in left margin.
- AsciiDoc converts the `<name>` to a legal attribute name (lower case, alphanumeric, dash and underscore characters only — all other characters deleted). This allows more human friendly text to be used.
- Leading and trailing white space is stripped from the `<value>`.
- Lines ending in a space followed by a plus character are continued to the next line, for example: `:description: AsciiDoc is a text document format for writing notes, + documentation, articles, books, slideshows, web pages + and man pages.`
- If the `<value>` is blank then the corresponding attribute value is set to an empty string.
- Attribute references contained in the entry `<value>` will be expanded.
- By default AttributeEntry values are substituted for `specialcharacters` and `attributes` (see above), if you want to change or disable AttributeEntry substitution use the pass:[] inline macro syntax.
- Attribute entries in the document Header are available for header markup template substitution.
- Attribute elements override configuration file and intrinsic attributes but do not override command-line attributes.

Here are some more attribute entry examples:

```
AsciiDoc User Manual

====================

:author:    Stuart Rackham

:email:     srackham@gmail.com

:revdate:   April 23, 2004

:revnumber: 5.1.1
```

Which creates these attributes:

```
{author}, {firstname}, {lastname}, {authorinitials}, {email},

{revdate}, {revnumber}
```

The previous example is equivalent to this document header:

```
AsciiDoc User Manual

====================

Stuart Rackham <srackham@gmail.com>

5.1.1, April 23, 2004
```

### 28.1. Setting configuration entries

A variant of the Attribute Entry syntax allows configuration file section entries and markup template sections to be set from within an AsciiDoc document:

```
:<section_name>.[<entry_name>]: <entry_value>
```

Where `<section_name>` is the configuration section name, `<entry_name>` is the name of the entry and `<entry_value>` is the optional entry value. This example sets the default labeled list style to *horizontal*:

```
:listdef-labeled.style: horizontal
```

It is exactly equivalent to a configuration file containing:

```
[listdef-labeled]

style=horizontal
```

- If the `<entry_name>` is omitted then the entire section is substituted with the `<entry_value>`. This feature should only be used to set markup template sections. The following example sets the *xref2* inline macro markup template: `:xref2-inlinemacro.: <a href="#{1}">{2?{2}}</a>`
- No substitution is performed on configuration file attribute entries and they cannot be undefined.
- This feature can only be used in attribute entries — configuration attributes cannot be set using the `asciidoc(1)` command `--attribute` option.

Attribute entries promote clarity and eliminate repetition

URLs and file names in AsciiDoc macros are often quite long — they break paragraph flow and readability suffers. The problem is compounded by redundancy if the same name is used repeatedly. Attribute entries can be used to make your documents easier to read and write, here are some examples:

```
:1:         http://freshmeat.sourceforge.net/projects/asciidoc/

:homepage:  https://asciidoc.org[AsciiDoc home page]

:new:       image:./images/smallnew.png[]

:footnote1: footnote:[A meaningless latin term]
```

```
Using previously defined attributes: See the {1}[Freshmeat summary]

or the {homepage} for something new {new}. Lorem ispum {footnote1}.
```

Note

- The attribute entry definition must precede it’s usage.
- You are not limited to URLs or file names, entire macro calls or arbitrary lines of text can be abbreviated.
- Shared attributes entries could be grouped into a separate file and included in multiple documents.


## 29. Attribute Lists

- An attribute list is a comma separated list of attribute values.
- The entire list is enclosed in square brackets.
- Attribute lists are used to pass parameters to macros, blocks (using the AttributeList element) and inline quotes.

The list consists of zero or more positional attribute values followed by zero or more named attribute values. Here are three examples: a single unquoted positional attribute; three unquoted positional attribute values; one positional attribute followed by two named attributes; the unquoted attribute value in the final example contains comma (`&#44;`) and double-quote (`&#34;`) character entities:

```
[Hello]

[quote, Bertrand Russell, The World of Mathematics (1956)]

["22 times", backcolor="#0e0e0e", options="noborders,wide"]

[A footnote&#44; &#34;with an image&#34; image:smallnew.png[]]
```

Attribute list behavior

- If one or more attribute values contains a comma the all string values must be quoted (enclosed in double quotation mark characters).
- If the list contains any named or quoted attributes then all string attribute values must be quoted.
- To include a double quotation mark (") character in a quoted attribute value the the quotation mark must be escaped with a backslash.
- List attributes take precedence over existing attributes.
- List attributes can only be referenced in configuration file markup templates and tags, they are not available elsewhere in the document.
- Setting a named attribute to `None` undefines the attribute.
- Positional attributes are referred to as `{1}`,`{2}`,`{3}`,…
- Attribute `{0}` refers to the entire list (excluding the enclosing square brackets).
- Named attribute names cannot contain dash characters.

### 29.1. Options attribute

If the attribute list contains an attribute named `options` it is processed as a comma separated list of option names:

- Each name generates an attribute named like `<option>-option` (where `<option>` is the option name) with an empty string value. For example `[options="opt1,opt2,opt3"]` is equivalent to setting the following three attributes `[opt1-option="",opt2-option="",opt2-option=""]`.
- If you define a an option attribute globally (for example with an attribute entry) then it will apply to all elements in the document.
- AsciiDoc implements a number of predefined options which are listed in the Attribute Options appendix.

### 29.2. Macro Attribute lists

Macros calls are suffixed with an attribute list. The list may be empty but it cannot be omitted. List entries are used to pass attribute values to macro markup templates.


## 30. Attribute References

An attribute reference is an attribute name (possibly followed by an additional parameters) enclosed in curly braces. When an attribute reference is encountered it is evaluated and replaced by its corresponding text value. If the attribute is undefined the line containing the attribute is dropped.

There are three types of attribute reference: *Simple*, *Conditional* and *System*.

Attribute reference evaluation

- You can suppress attribute reference expansion by placing a backslash character immediately in front of the opening brace character.
- By default attribute references are not expanded in *LiteralParagraphs*, *ListingBlocks* or *LiteralBlocks*.
- Attribute substitution proceeds line by line in reverse line order.
- Attribute reference evaluation is performed in the following order: *Simple* then *Conditional* and finally *System*.

### 30.1. Simple Attributes References

Simple attribute references take the form `{<name>}`. If the attribute name is defined its text value is substituted otherwise the line containing the reference is dropped from the output.

### 30.2. Conditional Attribute References

Additional parameters are used in conjunction with attribute names to calculate a substitution value. Conditional attribute references take the following forms:

**`{<names>=<value>}`**

`<value>` is substituted if the attribute `<names>` is undefined otherwise its value is substituted. `<value>` can contain simple attribute references.

**`{<names>?<value>}`**

`<value>` is substituted if the attribute `<names>` is defined otherwise an empty string is substituted. `<value>` can contain simple attribute references.

**`{<names>!<value>}`**

`<value>` is substituted if the attribute `<names>` is undefined otherwise an empty string is substituted. `<value>` can contain simple attribute references.

**`{<names>#<value>}`**

`<value>` is substituted if the attribute `<names>` is defined otherwise the undefined attribute entry causes the containing line to be dropped. `<value>` can contain simple attribute references.

**`{<names>%<value>}`**

`<value>` is substituted if the attribute `<names>` is not defined otherwise the containing line is dropped. `<value>` can contain simple attribute references.

**`{<names>@<regexp>:<value1>[:<value2>]}`**

`<value1>` is substituted if the value of attribute `<names>` matches the regular expression `<regexp>` otherwise `<value2>` is substituted. If attribute `<names>` is not defined the containing line is dropped. If `<value2>` is omitted an empty string is assumed. The values and the regular expression can contain simple attribute references. To embed colons in the values or the regular expression escape them with backslashes.

**`{<names>$<regexp>:<value1>[:<value2>]}`**

Same behavior as the previous ternary attribute except for the following cases:

**`{<names>$<regexp>:<value>}`**

Substitutes `<value>` if `<names>` matches `<regexp>` otherwise the result is undefined and the containing line is dropped.

**`{<names>$<regexp>::<value>}`**

Substitutes `<value>` if `<names>` does not match `<regexp>` otherwise the result is undefined and the containing line is dropped.

The attribute `<names>` parameter normally consists of a single attribute name but it can be any one of the following:

- A single attribute name which evaluates to the attributes value.
- Multiple *,* separated attribute names which evaluates to an empty string if one or more of the attributes is defined, otherwise it’s value is undefined.
- Multiple *+* separated attribute names which evaluates to an empty string if all of the attributes are defined, otherwise it’s value is undefined.

Conditional attributes with single attribute names are evaluated first so they can be used inside the multi-attribute conditional `<value>`.

#### 30.2.1. Conditional attribute examples

Conditional attributes are mainly used in AsciiDoc configuration files — see the distribution `.conf` files for examples.

**Attribute equality test**

If `{backend}` is *docbook45* or *xhtml11* the example evaluates to “DocBook 4.5 or XHTML 1.1 backend” otherwise it evaluates to “some other backend”:

```
{backend@docbook45|xhtml11:DocBook 4.5 or XHTML 1.1 backend:some other backend}
```

**Attribute value map**

This example maps the `frame` attribute values [`topbot`, `all`, `none`, `sides`] to [`hsides`, `border`, `void`, `vsides`]:

```
{frame@topbot:hsides}{frame@all:border}{frame@none:void}{frame@sides:vsides}
```

### 30.3. System Attribute References

System attribute references generate the attribute text value by executing a predefined action that is parametrized by one or more arguments. The syntax is `{<action>:<arguments>}`.

**`{counter:<attrname>[:<seed>]}`**

Increments the document attribute (if the attribute is undefined it is set to `1`). Returns the new attribute value.

- Counters generate global (document wide) attributes.
- The optional `<seed>` specifies the counter’s initial value; it can be a number or a single letter; defaults to *1*.
- `<seed>` can contain simple and conditional attribute references.
- The *counter* system attribute will not be executed if the containing line is dropped by the prior evaluation of an undefined attribute.

**`{counter2:<attrname>[:<seed>]}`**

Same as `counter` except the it always returns a blank string.

**`{eval:<expression>}`**

Substitutes the result of the Python `<expression>`.

- If `<expression>` evaluates to `None` or `False` the reference is deemed undefined and the line containing the reference is dropped from the output.
- If the expression evaluates to `True` the attribute evaluates to an empty string.
- `<expression>` can contain simple and conditional attribute references.
- The *eval* system attribute can be nested inside other system attributes.

**`{eval3:<command>}`**

Passthrough version of `{eval:<expression>}` — the generated output is written directly to the output without any further substitutions.

**`{include:<filename>}`**

Substitutes contents of the file named `<filename>`.

- The included file is read at the time of attribute substitution.
- If the file does not exist a warning is emitted and the line containing the reference is dropped from the output file.
- Tabs are expanded based on the current *tabsize* attribute value.

**`{set:<attrname>[!][:<value>]}`**

Sets or unsets document attribute. Normally only used in configuration file markup templates (use AttributeEntries in AsciiDoc documents).

- If the attribute name is followed by an exclamation mark the attribute becomes undefined.
- If `<value>` is omitted the attribute is set to a blank string.
- `<value>` can contain simple and conditional attribute references.
- Returns a blank string unless the attribute is undefined in which case the return value is undefined and the enclosing line will be dropped.

**`{set2:<attrname>[!][:<value>]}`**

Same as `set` except that the attribute scope is local to the template.

**`{sys:<command>}`**

Substitutes the stdout generated by the execution of the shell `<command>`.

**`{sys2:<command>}`**

Substitutes the stdout and stderr generated by the execution of the shell `<command>`.

**`{sys3:<command>}`**

Passthrough version of `{sys:<command>}` — the generated output is written directly to the output without any further substitutions.

**`{template:<template>}`**

Substitutes the contents of the configuration file section named `<template>`. Attribute references contained in the template are substituted.

System reference behavior

- System attribute arguments can contain non-system attribute references.
- Closing brace characters inside system attribute arguments must be escaped with a backslash.


## 31. Intrinsic Attributes

Intrinsic attributes are simple attributes that are created automatically from: AsciiDoc document header parameters; `asciidoc(1)` command-line arguments; attributes defined in the default configuration files; the execution context. Here’s the list of predefined intrinsic attributes:

```
{amp}                 ampersand (&) character entity

{asciidoc-args}       used to pass inherited arguments to asciidoc filters

{asciidoc-confdir}    the asciidoc(1) global configuration directory

{asciidoc-dir}        the asciidoc(1) application directory

{asciidoc-file}       the full path name of the asciidoc(1) script

{asciidoc-version}    the version of asciidoc(1)

{author}              author's full name

{authored}            empty string '' if {author} or {email} defined,

{authorinitials}      author initials (from document header)

{backend-<backend>}   empty string ''

{<backend>-<doctype>} empty string ''

{backend}             document backend specified by `-b` option

{backend-confdir}     the directory containing the <backend>.conf file

{backslash}           backslash character

{basebackend-<base>}  empty string ''

{basebackend}         html or docbook

{blockname}           current block name (note 8).

{brvbar}              broken vertical bar (|) character

{docdate}             document last modified date (note 9)

{docdir}              document input directory name  (note 5)

{docfile}             document file name  (note 5)

{docname}             document file name without extension (note 6)

{doctime}             document last modified time (note 9)

{doctitle}            document title (from document header)

{doctype-<doctype>}   empty string ''

{doctype}             document type specified by `-d` option

{email}               author's email address (from document header)

{empty}               empty string ''

{encoding}            specifies input and output encoding

{filetype-<fileext>}  empty string ''

{filetype}            output file name file extension

{firstname}           author first name (from document header)

{gt}                  greater than (>) character entity

{id}                  running block id generated by BlockId elements

{indir}               input file directory name (note 2,5)

{infile}              input file name (note 2,5)

{lastname}            author last name (from document header)

{ldquo}               Left double quote character (note 7)

{level}               title level 1..4 (in section titles)

{listindex}           the list index (1..) of the most recent list item

{localdate}           the current date (note 9)

{localtime}           the current time (note 9)

{lsquo}               Left single quote character (note 7)

{lt}                  less than (<) character entity

{manname}             manpage name (defined in NAME section)

{manpurpose}          manpage (defined in NAME section)

{mantitle}            document title minus the manpage volume number

{manvolnum}           manpage volume number (1..8) (from document header)

{middlename}          author middle name (from document header)

{nbsp}                non-breaking space character entity

{notitle}             do not display the document title

{outdir}              document output directory name (note 2)

{outfile}             output file name (note 2)

{plus}                plus character

{python}              the full path name of the Python interpreter executable

{rdquo}               right double quote character (note 7)

{reftext}             running block xreflabel generated by BlockId elements

{revdate}             document revision date (from document header)

{revnumber}           document revision number (from document header)

{rsquo}               right single quote character (note 7)

{sectnum}             formatted section number (in section titles)

{sp}                  space character

{showcomments}        send comment lines to the output

{title}               section title (in titled elements)

{two-colons}          two colon characters

{two-semicolons}      two semicolon characters

{user-dir}            the ~/.asciidoc directory (if it exists)

{verbose}             defined as '' if --verbose command option specified

{wj}                  word-joiner

{zwsp}                zero-width space character entity
```

| (Note) | Intrinsic attributes are global so avoid defining custom attributes with the same names. `{outfile}`, `{outdir}`, `{infile}`, `{indir}` attributes are effectively read-only (you can set them but it won’t affect the input or output file paths). See also the Backend Attributes section for attributes that relate to AsciiDoc XHTML file generation. The entries that translate to blank strings are designed to be used for conditional text inclusion. You can also use the `ifdef`, `ifndef` and `endif` System macros for conditional inclusion. [Conditional inclusion using `ifdef` and `ifndef` macros differs from attribute conditional inclusion in that the former occurs when the file is read while the latter occurs when the contents are written.] `{docfile}` and `{docdir}` refer to root document specified on the `asciidoc(1)` command-line; `{infile}` and `{indir}` refer to the current input file which may be the root document or an included file. When the input is being read from the standard input (`stdin`) these attributes are undefined. If the input file is the standard input and the output file is not the standard output then `{docname}` is the output file name sans file extension. See non-English usage of quotation marks. The `{blockname}` attribute identifies the style of the current block. It applies to delimited blocks, lists and tables. Here is a list of `{blockname}` values (does not include filters or custom block and style names): delimited blocks comment, sidebar, open, pass, literal, verse, listing, quote, example, note, tip, important, caution, warning, abstract, partintro lists arabic, loweralpha, upperalpha, lowerroman, upperroman, labeled, labeled3, labeled4, qanda, horizontal, bibliography, glossary tables table If the `SOURCE_DATE_EPOCH` environment variable is set to a UNIX timestamp, then the `{docdate}`, `{doctime}`, `{localdate}`, and `{localtime}` attributes are computed in the UTC time zone, with any timestamps newer than `SOURCE_DATE_EPOCH` replaced by `SOURCE_DATE_EPOCH`. (This helps software using AsciiDoc to build reproducibly.) |
|---|---|


## 32. Block Element Definitions

The syntax and behavior of Paragraph, DelimitedBlock, List and Table block elements is determined by block definitions contained in AsciiDoc configuration file sections.

Each definition consists of a section title followed by one or more section entries. Each entry defines a block parameter controlling some aspect of the block’s behavior. Here’s an example:

```
[blockdef-listing]

delimiter=^-{4,}$

template=listingblock

presubs=specialcharacters,callouts
```

Configuration file block definition sections are processed incrementally after each configuration file is loaded. Block definition section entries are merged into the block definition, this allows block parameters to be overridden and extended by later loading configuration files.

AsciiDoc Paragraph, DelimitedBlock, List and Table block elements share a common subset of configuration file parameters:

**delimiter**

A Python regular expression that matches the first line of a block element — in the case of DelimitedBlocks and Tables it also matches the last line.

**template**

The name of the configuration file markup template section that will envelope the block contents. The pipe (*|*) character is substituted for the block contents. List elements use a set of (list specific) tag parameters instead of a single template. The template name can contain attribute references allowing dynamic template selection a the time of template substitution.

**options**

A comma delimited list of element specific option names. In addition to being used internally, options are available during markup tag and template substitution as attributes with an empty string value named like `<option>-option` (where `<option>` is the option name). See attribute options for a complete list of available options.

**subs, presubs, postsubs**

- *presubs* and *postsubs* are lists of comma separated substitutions that are performed on the block contents. *presubs* is applied first, *postsubs* (if specified) second.
- *subs* is an alias for *presubs*.
- If a *filter* is allowed (Paragraphs, DelimitedBlocks and Tables) and has been specified then *presubs* and *postsubs* substitutions are performed before and after the filter is run respectively.
- Allowed values: *specialcharacters*, *quotes*, *specialwords*, *replacements*, *macros*, *attributes*, *callouts*.
- The following composite values are also allowed: *none* No substitutions. *normal* The following substitutions in the following order: *specialcharacters*, *quotes*, *attributes*, *specialwords*, *replacements*, *macros*, *replacements2*. *verbatim* The following substitutions in the following order: *specialcharacters* and *callouts*.
- *normal* and *verbatim* substitutions can be redefined by with `subsnormal` and `subsverbatim` entries in a configuration file `[miscellaneous]` section.
- The substitutions are processed in the order in which they are listed and can appear more than once.

**filter**

This optional entry specifies an executable shell command for processing block content (Paragraphs, DelimitedBlocks and Tables). The filter command can contain attribute references.

**posattrs**

Optional comma separated list of positional attribute names. This list maps positional attributes (in the block’s attribute list) to named block attributes. The following example, from the QuoteBlock definition, maps the first and section positional attributes:

```
posattrs=attribution,citetitle
```

**style**

This optional parameter specifies the default style name.

**<stylename>-style**

Optional style definition (see Styles below).

The following block parameters behave like document attributes and can be set in block attribute lists and style definitions: *template*, *options*, *subs*, *presubs*, *postsubs*, *filter*.

### 32.1. Styles

A style is a set of block parameter bundled as a single named parameter. The following example defines a style named *verbatim*:

```
verbatim-style=template="literalblock",subs="verbatim"
```

If a block’s attribute list contains a *style* attribute then the corresponding style parameters are be merged into the default block definition parameters.

- All style parameter names must be suffixed with `-style` and the style parameter value is in the form of a list of named attributes.
- The *template* style parameter is mandatory, other parameters can be omitted in which case they inherit their values from the default block definition parameters.
- Multi-item style parameters (*subs*,*presubs*,*postsubs*,*posattrs*) must be specified using Python tuple syntax (rather than a simple list of values as they in separate entries) e.g. `postsubs=("callouts",)` not `postsubs="callouts"`.

### 32.2. Paragraphs

Paragraph translation is controlled by `[paradef-*]` configuration file section entries. Users can define new types of paragraphs and modify the behavior of existing types by editing AsciiDoc configuration files.

Here is the shipped Default paragraph definition:

```
[paradef-default]

delimiter=(?P<text>\S.*)

template=paragraph
```

The normal paragraph definition has a couple of special properties:

1. It must exist and be defined in a configuration file section named `[paradef-default]`.
2. Irrespective of its position in the configuration files default paragraph document matches are attempted only after trying all other paragraph types.

Paragraph specific block parameter notes:

**delimiter**

This regular expression must contain the named group *text* which matches the text on the first line. Paragraphs are terminated by a blank line, the end of file, or the start of a DelimitedBlock.

**options**

The *listelement* option specifies that paragraphs of this type will automatically be considered part of immediately preceding list items. The *skip* option causes the paragraph to be treated as a comment (see CommentBlocks).

Paragraph processing proceeds as follows:

1. The paragraph text is aligned to the left margin.
2. Optional *presubs* inline substitutions are performed on the paragraph text.
3. If a filter command is specified it is executed and the paragraph text piped to its standard input; the filter output replaces the paragraph text.
4. Optional *postsubs* inline substitutions are performed on the paragraph text.
5. The paragraph text is enveloped by the paragraph’s markup template and written to the output file.

### 32.3. Delimited Blocks

DelimitedBlock *options* values are:

**sectionbody**

The block contents are processed as a SectionBody.

**skip**

The block is treated as a comment (see CommentBlocks). Preceding attribute lists and block titles are not consumed.

*presubs*, *postsubs* and *filter* entries are ignored when *sectionbody* or *skip* options are set.

DelimitedBlock processing proceeds as follows:

1. Optional *presubs* substitutions are performed on the block contents.
2. If a filter is specified it is executed and the block’s contents piped to its standard input. The filter output replaces the block contents.
3. Optional *postsubs* substitutions are performed on the block contents.
4. The block contents is enveloped by the block’s markup template and written to the output file.

| (Tip) | Attribute expansion is performed on the block filter command before it is executed, this is useful for passing arguments to the filter. |
|---|---|

### 32.4. Lists

List behavior and syntax is determined by `[listdef-*]` configuration file sections. The user can change existing list behavior and add new list types by editing configuration files.

List specific block definition notes:

**type**

This is either *bulleted*,*numbered*,*labeled* or *callout*.

**delimiter**

A Python regular expression that matches the first line of a list element entry. This expression can contain the named groups *text* (bulleted groups), *index* and *text* (numbered lists), *label* and *text* (labeled lists).

**tags**

The `<name>` of the `[listtags-<name>]` configuration file section containing list markup tag definitions. The tag entries (*list*, *entry*, *label*, *term*, *text*) map the AsciiDoc list structure to backend markup; see the *listtags* sections in the AsciiDoc distributed backend `.conf` configuration files for examples.

### 32.5. Tables

Table behavior and syntax is determined by `[tabledef-*]` and `[tabletags-*]` configuration file sections. The user can change existing table behavior and add new table types by editing configuration files. The following `[tabledef-*]` section entries generate table output markup elements:

**colspec**

The table *colspec* tag definition.

**headrow, footrow, bodyrow**

Table header, footer and body row tag definitions. *headrow* and *footrow* table definition entries default to *bodyrow* if they are undefined.

**headdata, footdata, bodydata**

Table header, footer and body data tag definitions. *headdata* and *footdata* table definition entries default to *bodydata* if they are undefined.

**paragraph**

If the *paragraph* tag is specified then blank lines in the cell data are treated as paragraph delimiters and marked up using this tag.

Table behavior is also influenced by the following `[miscellaneous]` configuration file entries:

**pagewidth**

This integer value is the printable width of the output media. See table attributes.

**pageunits**

The units of width in output markup width attribute values.

Table definition behavior

- The output markup generation is specifically designed to work with the HTML and CALS (DocBook) table models, but should be adaptable to most XML table schema.
- Table definitions can be “mixed in” from multiple cascading configuration files.
- New table definitions inherit the default table and table tags definitions (`[tabledef-default]` and `[tabletags-default]`) so you only need to override those conf file entries that require modification.
