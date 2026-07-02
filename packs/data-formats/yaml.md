---
title: "YAML"
source: https://en.wikipedia.org/wiki/YAML
domain: data-formats
license: CC-BY-SA-4.0
tags: json, yaml, toml, xml, csv, base64, markdown
fetched: 2026-07-02
---

# YAML

**YAML** (/ˈjæməl/ ⓘ *YAM-əl*) is a human-readable data serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted. YAML targets many of the same communications applications as Extensible Markup Language (XML) but has a minimal syntax that intentionally differs from Standard Generalized Markup Language (SGML). It uses Python-style indentation to indicate nesting and does not require quotes around most string values (it also supports JSON style `[...]` and `{...}` mixed in the same file).

Custom data types are allowed, but YAML natively encodes scalars (such as strings, integers, and floats), lists, and associative arrays (also known as maps, dictionaries or hashmaps). These data types are based on the Perl programming language, though all commonly used high-level programming languages share very similar concepts. The colon-centered syntax, used for expressing key-value pairs, is inspired by electronic mail headers as defined in RFC 822, and the document separator `---` is borrowed from MIME (RFC 2046). Escape sequences are reused from C, and whitespace wrapping for multi-line strings is inspired by HTML. Lists and hashes can contain nested lists and hashes, forming a tree structure; arbitrary graphs can be represented using YAML aliases (similar to XML in SOAP). YAML is intended to be read and written in streams, a feature inspired by SAX.

Support for reading and writing YAML is available for many programming languages. Some source-code editors such as Vim, Emacs, and various integrated development environments have features that make editing YAML easier, such as folding up nested structures or automatically highlighting syntax errors.

The official recommended filename extension for YAML files has been `.yaml` since 2006. In 2024, the MIME type `application/yaml` has been finalized.

## History and name

YAML (/ˈjæməl/, rhymes with *camel*) was first proposed by Clark Evans in 2001, who designed it together with Ingy döt Net and Oren Ben-Kiki. Originally YAML was said to mean *Yet Another Markup Language*, because it was released in an era that saw a proliferation of markup languages for presentation and connectivity (HTML, XML, SGML, etc.). Its initial name was intended as a tongue-in-cheek reference to the technology landscape, referencing its purpose as a markup language with the yet another construct, but it was then repurposed between December 2001 and April 2002 as *YAML Ain't Markup Language*, a recursive acronym, to distinguish its purpose as data-oriented rather than document markup.

## Versions

| Version | Release date |
|---|---|
| YAML 1.0 | 29 January 2004 |
| YAML 1.1 | 18 January 2005 |
| YAML 1.2.0 | 21 July 2009 |
| YAML 1.2.1 | 1 October 2009 |
| YAML 1.2.2 | 1 October 2021 |

## Design

### Syntax

A cheat sheet and full specification are available at the official site. The following is a synopsis of the basic elements.

YAML accepts the entire Unicode character set, except for some control characters, and may be encoded in any one of UTF-8, UTF-16 or UTF-32. (Though UTF-32 is not mandatory, it is required for a parser to have JSON compatibility.)

- Whitespace indentation is used for denoting structure; however, tab characters are not allowed as part of that indentation.
- Comments begin with the number sign (`#`), can start anywhere on a line and continue until the end of the line. Comments must be separated from other tokens by whitespace characters. If `#` characters appear inside of a string, then they are number sign (`#`) literals.
- List members are denoted by a leading hyphen (`-`) with one member per line.
  - A list can also be specified by enclosing text in square brackets (`[...]`) with each entry separated by a comma.
- An associative array entry is represented using colon space in the form *key: value* with one entry per line. YAML requires the colon be followed by a space so that url-style strings like `http://www.wikipedia.org` can be represented without needing to be enclosed in quotes.
  - A question mark can be used in front of a key, in the form "?key: value" to allow the key to contain leading dashes, square brackets, etc., without quotes.
  - An associative array can also be specified by text enclosed in curly braces (`{...}`), with keys separated from values by colon and the entries separated by commas (spaces are not required to retain compatibility with JSON).
- Strings (one type of scalar in YAML) are ordinarily unquoted, but may be enclosed in double-quotes (`"`), or single-quotes (`'`).
  - Within double-quotes, special characters may be represented with C-style escape sequences starting with a backslash (`\`). According to the documentation the only octal escape supported is `\0`.
  - Within single quotes the only supported escape sequence is a doubled single quote (`''`) denoting the single quote itself as in `'don''t'`.
- Block scalars are delimited with indentation with optional modifiers to preserve (`|`) or fold (`>`) newlines.
- Multiple documents within a single stream are separated by three hyphens (`---`).
  - Three periods (`...`) optionally end a document within a stream.
- Repeated nodes are initially denoted by an ampersand (`&`) and thereafter referenced with an asterisk (`*`).
- Nodes may be labeled with a type or tag using a double exclamation mark (`!!`) followed by a string, which can be expanded into a URI.
- YAML documents in a stream may be preceded by "directives" composed of a percent sign (`%`) followed by a name and space-delimited parameters. Two directives are defined in YAML 1.1:
  - The %YAML directive is used for identifying the version of YAML in a given document.
  - The %TAG directive is used as a shortcut for URI prefixes. These shortcuts may then be used in node type tags.

### Basic components

Conventional block format uses a hyphen+space to begin a new item in list.

```mw
--- # Favorite movies
- Casablanca
- North by Northwest
- The Man Who Wasn't There
```

Optional inline format is delimited by comma+space and enclosed in brackets (similar to JSON).

```mw
--- # Shopping list
[milk, pumpkin pie, eggs, juice]
```

Keys are separated from values by a colon+space. Indented blocks, common in YAML data files, use indentation and new lines to separate the key/value pairs. Inline blocks, common in YAML data streams, use comma+space to separate the key/value pairs between braces.

```mw
--- # Indented Block
  name: John Smith
  age: 33
--- # Inline Block
{name: John Smith, age: 33}
```

Strings do not require quotation marks. There are two ways to write multi-line strings, one preserving newlines (using the `|` character) and one that folds the newlines (using the `>` character), both followed by a newline character.

```mw
data: |
   There once was a tall man from Ealing
   Who got on a bus to Darjeeling
       It said on the door
       "Please don't sit on the floor"
   So he carefully sat on the ceiling
```

By default, the leading indentation (of the first line) and trailing whitespace are stripped, though other behavior can be explicitly specified.

```mw
data: >
   Wrapped text
   will be folded
   into a single
   paragraph

   Blank lines denote
   paragraph breaks
```

Folded text converts newlines to spaces and removes leading whitespace.

```mw
--- # The Smiths
- {name: John Smith, age: 33}
- name: Mary Smith
  age: 27
- [name, age]: [Rae Smith, 4]   # sequences as keys are supported
--- # People, by gender
men: [John Smith, Bill Jones]
women:
  - Mary Smith
  - Susan Williams
```

Objects and lists are important components in yaml and can be mixed. The first example is a list of key-value objects, all people from the Smith family. The second lists them by gender; it is a key-value object containing two lists.

### Advanced components

Features that distinguish YAML from the capabilities of other data-serialization languages are structures, and data and composite keys.

YAML structures enable storage of multiple documents within a single file, usage of references for repeated nodes, and usage of arbitrary nodes as keys.

For clarity, compactness, and avoiding data entry errors, YAML provides node anchors (using `&`) and references (using `*`). References to the anchor work for all data types (see the ship-to reference in the example below).

Below is an example of a queue in an instrument sequencer in which two steps are referenced without being fully described.

```mw
--- # Sequencer protocols for Laser eye surgery
- step:  &id001                  # defines anchor label &id001
    instrument:      Lasik 2000
    pulseEnergy:     5.4
    pulseDuration:   12
    repetition:      1000
    spotSize:        1mm

- step: &id002
    instrument:      Lasik 2000
    pulseEnergy:     5.0
    pulseDuration:   10
    repetition:      500
    spotSize:        2mm
- Instrument1: *id001   # refers to the first step (with anchor &id001)
- Instrument2: *id002   # refers to the second step
```

Explicit data typing is seldom seen in the majority of YAML documents since YAML autodetects simple types. Data types can be divided into three categories: core, defined, and user-defined. Core are ones expected to exist in any parser (e.g. floats, ints, strings, lists, maps, ...). Many more advanced data types, such as binary data, are defined in the YAML specification but not supported in all implementations. Finally YAML defines a way to extend the data type definitions locally to accommodate user-defined classes, structures or primitives (e.g. quad-precision floats).

YAML autodetects the datatype of the entity, but sometimes one wants to cast the datatype explicitly. The most common situation is where a single-word string that looks like a number, Boolean or tag requires disambiguation by surrounding it with quotes or using an explicit datatype tag.

```mw
---
a: 123                     # an integer
b: "123"                   # a string, disambiguated by quotes
c: 123.0                   # a float
d: !!float 123             # also a float via explicit data type prefixed by (!!)
e: !!str 123               # a string, disambiguated by explicit type
f: !!str Yes               # a string via explicit type
g: Yes                     # a Boolean True (yaml1.1), string "Yes" (yaml1.2)
h: Yes we have No bananas  # a string, "Yes" and "No" disambiguated by context.
```

Not every implementation of YAML has every specification-defined data type. These built-in types use a double-exclamation sigil prefix (`!!`). Particularly interesting ones not shown here are sets, ordered maps, timestamps, and hexadecimal. Here is an example of base64-encoded binary data.

```mw
---
picture: !!binary |
  R0lGODdhDQAIAIAAAAAAANn
  Z2SwAAAAADQAIAAACF4SDGQ
  ar3xxbJ9p0qa7R0YxwzaFME
  1IAADs=
```

Many implementations of YAML can support user-defined data types for object serialization. Local data types are not universal data types but are defined in the application using the YAML parser library. Local data types use a single exclamation mark (`!`).

YAML supports composite keys, which consist of multiple values. Such keys are useful for coordinate transformations, multi-field identifiers, test cases with compound conditions, and the like.

```mw
--- # Transform between two systems of coordinates
  transform:
      {x: 1, y: 2}: {x: 3, y: 4}
      {x: 5, y: 6}: {x: 7, y: 8}
```

### Example

Data-structure hierarchy is maintained by outline indentation.

```mw
---
receipt:     Oz-Ware Purchase Invoice
date:        2012-08-06
customer:
    first_name:   Dorothy
    family_name:  Gale

items:
    - part_no:   A4786
      descrip:   Water Bucket (Filled)
      price:     1.47
      quantity:  4

    - part_no:   E1628
      descrip:   High Heeled "Ruby" Slippers
      size:      8
      price:     133.7
      quantity:  1

bill-to:  &id001
    street: |
            123 Tornado Alley
            Suite 16
    city:   East Centerville
    state:  KS

ship-to:  *id001

specialDelivery:  >
    Follow the Yellow Brick
    Road to the Emerald City.
    Pay no attention to the
    man behind the curtain.
...
```

Notice that strings do not require enclosure in quotation marks. The specific number of spaces in the indentation is unimportant as long as parallel elements have the same left justification and the hierarchically nested elements are indented further. This sample document defines an associative array with 7 top level keys: one of the keys, "items", contains a 2-element list, each element of which is itself an associative array with differing keys. Relational data and redundancy removal are displayed: the "ship-to" associative array content is copied from the "bill-to" associative array's content as indicated by the anchor (`&`) and reference (`*`) labels. Optional blank lines can be added for readability. Multiple documents can exist in a single file/stream and are separated by `---`. An optional `...` can be used at the end of a file (useful for signaling an end in streamed communications without closing the pipe).

## Features

### Indented delimiting

Because YAML primarily relies on outline indentation for structure, it is especially resistant to delimiter collision. YAML's insensitivity to quotation marks and braces in scalar values means one may embed XML, JSON or even YAML documents inside a YAML document by simply indenting it in a block literal (using `|` or `>`):

```mw
---
example: >
        HTML goes into YAML without modification
message: |

        <blockquote style="font: italic 1em serif">
        <p>"Three is always greater than two,
           even for large values of two"</p>
        <p>--Author Unknown</p>
        </blockquote>
date: 2007-06-01
```

YAML may be placed in JSON by quoting and escaping all interior quotation marks. YAML may be placed in XML by escaping reserved characters (`<`, `>`, `&`, `'`, `"`) and converting whitespace, or by placing it in a CDATA section.

### Non-hierarchical data models

Unlike JSON, which can only represent data in a hierarchical model with each child node having a single parent, YAML also offers a simple relational scheme that allows repeats of identical data to be referenced from two or more points in the tree rather than entered redundantly at those points. This is similar to the facility IDREF built into XML. The YAML parser then expands these references into the fully populated data structures they imply when read in, so whatever program is using the parser does not have to be aware of a relational encoding model, unlike XML processors, which do not expand references. This expansion can enhance readability while reducing data entry errors in configuration files or processing protocols where many parameters remain the same in a sequential series of records while only a few vary. An example being that "ship-to" and "bill-to" records in an invoice are nearly always the same data.

### Security

YAML is purely a data-representation language and thus has no executable commands. While validation and safe parsing is inherently possible in any data language, implementation is such a notorious pitfall that YAML's lack of an associated command language may be a relative security benefit.

However, YAML allows language-specific tags so that arbitrary local objects can be created by a parser that supports those tags. Any YAML parser that allows sophisticated object instantiation to be executed opens the potential for an injection attack. Perl parsers that allow loading of objects of arbitrary classes create so-called "blessed" values. Using these values may trigger unexpected behavior, e.g. if the class uses overloaded operators. This may lead to execution of arbitrary Perl code.

The situation is similar for Python or Ruby parsers. According to the PyYAML documentation:

> Note that the ability to construct an arbitrary Python object may be dangerous if you receive a YAML document from an untrusted source such as the Internet. The function `yaml.safe_load` limits this ability to simple Python objects like integers or lists. [...]
> 
> PyYAML allows you to construct a Python object of any type. Even instances of Python classes can be constructed using the `!!python/object` tag.

### Data processing and representation

The YAML specification identifies an *instance document* as a "Presentation" or "character stream". The primary logical structures in a YAML instance document are scalars, sequences, and mappings. The YAML specification also indicates some basic constraints that apply to these primary logical structures. For example, according to the specification, mapping keys do not have an order. In every case where node order is significant, a sequence must be used.

Moreover, in defining conformance for YAML processors, the YAML specification defines two primary operations: *dump* and *load*. All YAML-compliant processors must provide *at least* one of these operations, and may optionally provide both. Finally, the YAML specification defines an *information model* or "representation graph", which must be created during processing for both *dump* and *load* operations, although this representation need not be made available to the user through an API.

## Comparison with other serialization formats

### Comparison with JSON

JSON syntax is a basis of YAML version 1.2, which was promulgated with the express purpose of bringing YAML "into compliance with JSON as an official subset". Though prior versions of YAML were not strictly compatible, the discrepancies were rarely noticeable, and most JSON documents can be parsed by some YAML parsers such as Syck. This is because JSON's semantic structure is equivalent to the optional "inline-style" of writing YAML. While extended hierarchies can be written in inline-style like JSON, this is not a recommended YAML style except when it aids clarity.

YAML has many additional features not present in JSON, including comments, extensible data types, relational anchors, strings without quotation marks, and mapping types preserving key order.

Due to the conciseness, JSON serialization and deserialization is much faster than YAML.

### Comparison with TOML

TOML was designed to be an advancement of the .ini file format. YAML makes minimal use of indicator characters compared to TOML's strict requirement of quotation marks and square brackets. YAML's use of significant indentation has been contrasted with the dot notation of TOML's key and table names to convey the same semantic structure. Opinions differ on which convention leads to more-readable configuration files.

### Comparison with XML

YAML lacks the notion of tag attributes that are found in XML. Instead YAML has extensible type declarations (including class types for objects).

YAML itself does not have XML's language-defined document schema descriptors that allow, for example, a document to self-validate. However, there are several externally defined schema descriptor languages for YAML (e.g. Doctrine, Kwalify and Rx) that fulfill that role. Moreover, the semantics provided by YAML's language-defined type declarations in the YAML document itself frequently relaxes the need for a validator in simple, common situations. Additionally, YAXML, which represents YAML data structures in XML, allows XML schema importers and output mechanisms like XSLT to be applied to YAML.

Comparison of data-serialization formats provides a more comprehensive comparison of YAML with other serialization formats.

## Software (emitters and parsers)

For fixed data structures, YAML files can simply be generated using *print* commands that write both the data and the YAML specific decoration. To dump varying, or complex, hierarchical data, however, a dedicated YAML *emitter* is preferable. Similarly, simple YAML files (e.g. key-value pairs) are readily parsed with regular expressions. For more complex, or varying, data structures, a formal YAML *parser* is recommended.

YAML emitters and parsers exist for many popular languages. Most of them are written in the native language itself. Some are language bindings of the C library *libyaml*; they may run faster. There used to be another C library, called *Syck*, written and orphaned by why the lucky stiff: it is unmaintained, there is no authoritative source bundle, and the web site has been hijacked. Hence the only recommendable C library is *libyaml*. It was originally developed by Kirill Simonov. In 2018, development was resumed by the new maintainers Ian Cordasco and Ingy döt Net.

C++ programmers have the choice between the C library *libyaml* and the C++ library *libyaml-cpp*. Both have completely independent code bases and completely different APIs. The library *libyaml-cpp* still has a major version number of 0, indicating that the API may change at any moment, as happened indeed after version 0.3. There is a grammar-focused implementation written in C#, with an aim on extensions for the nested elements.

Some implementations of YAML, such as Perl's YAML.pm, will load an entire file (stream) and parse it *en masse*. Other implementations like PyYaml are lazy and iterate over the next document only upon request. For very large files in which one plans to handle the documents independently, instantiating the entire file before processing may be prohibitive. Thus in YAML.pm, occasionally one must chunk a file into documents and parse those individually. YAML makes this easy, since this simply requires splitting on the document end marker, which is defined as three periods at the start of a line followed by a whitespace (and possible a comment). This marker is forbidden in content.

## Criticism

YAML has been criticized for its significant whitespace, confusing features, insecure defaults, and its complex and ambiguous specification:

- In dynamic languages (Python, Ruby, PHP) configuration files can execute commands without the users realizing it:

```mw
!!python/object/apply:os.system
args: ['ls /']
```

In static, compiled languages, this instantiation is complex to achieve and is quite often not implemented.

- Editing large YAML files is difficult, as indentation errors can go unnoticed.
- Type autodetection is a source of errors. For example, unquoted `Yes` and `No` are converted to Booleans; software version numbers might be converted to floats.
- Truncated files are often interpreted as valid YAML due to the absence of terminators.
- The complexity of the standard led to inconsistent implementations and making the language non-portable.

The perceived flaws and complexity of YAML has led to the emergence of stricter alternatives such as StrictYAML and NestedText.
