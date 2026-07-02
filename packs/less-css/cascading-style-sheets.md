---
title: "CSS - Wikipedia"
source: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
domain: less-css
license: CC-BY-SA-4.0
tags: less css, less style sheet, css preprocessor language, less mixin
fetched: 2026-07-02
---

# CSS

(Redirected from

Cascading Style Sheets

)

**Cascading Style Sheets** (**CSS**) is a style sheet language used for specifying the presentation and styling of a document written in a markup language, such as HTML or XML (including XML dialects such as SVG, MathML, or XHTML). CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.

CSS is designed to enable the separation of content and presentation, including layout, colors, and fonts. This separation can improve content accessibility, since the content can be written without concern for its presentation; provide more flexibility and control in the specification of presentation characteristics; enable multiple web pages to share formatting by specifying the relevant CSS in a separate .css file, which reduces complexity and repetition in the structural content; and enable the .css file to be cached to improve the page load speed between the pages that share the file and its formatting.

Separation of formatting and content also makes it feasible to present the same markup page in different styles for different rendering methods, such as on-screen, in print, by voice (via speech-based browser or screen reader), and on Braille-based tactile devices. CSS also has rules for alternative formatting if the content is accessed on a mobile device.

The name *cascading* comes from the specified priority scheme to determine which declaration applies if more than one declaration of a property match a particular element. This cascading priority scheme is predictable.

The CSS specifications are maintained by the World Wide Web Consortium (W3C). Internet media type (MIME type) `text/css` is registered for use with CSS by RFC 2318 (March 1998). The W3C operates a free CSS validation service for CSS documents.

In addition to HTML, other markup languages support the use of CSS including XHTML, plain XML, SVG, and XUL. CSS is also used in the GTK widget toolkit.

## Syntax

CSS has a simple syntax and uses a number of English keywords to specify the names of various style properties.

### Style sheet

A style sheet consists of a list of *rules*. Each rule or rule-set consists of one or more *selectors*, and a *declaration block*.

### Selector

In CSS, *selectors* declare which part of the markup a style applies to by matching tags and attributes in the markup itself.

#### Selector types

Selectors may apply to the following:

- all elements of a specific type, e.g. the second-level headers h2
- elements specified by attribute, in particular:
  - *id*: an identifier unique within the document, denoted in the selector language by a hash prefix e.g. `#id`
  - *class*: an identifier that can annotate multiple elements in a document, denoted by a dot prefix e.g. `.classname` (the phrase "CSS class", although sometimes used, is a misnomer, as element classes—specified with the HTML class attribute—is a markup feature that is distinct from browsers' CSS subsystems, and the related W3C/WHATWG standards work on document styles; see RDF and microformats for the origins of the "class" system of the Web content model)
- elements depending on how they are placed relative to others in the document tree.

Classes and IDs are case-sensitive, start with letters, and can include alphanumeric characters, hyphens, and underscores. A class may apply to any number of instances of any element. An ID may only be applied to a single element.

#### Pseudo-classes

*Pseudo-classes* are used in CSS selectors to permit formatting based on information that is not contained in the document tree.

One example of a widely used pseudo-class is `:hover`, which identifies content only when the user "points to" the visible element, usually by holding the mouse cursor over it. It is appended to a selector as in `a:hover` or `#elementid:hover`.

A pseudo-class classifies document elements, such as `:link` or `:visited`, whereas a *pseudo-element* makes a selection that may consist of partial elements, such as `::first-line` or `::first-letter`. Note the distinction between the double-colon notation used for pseudo-elements and the single-colon notation used for pseudo-classes.

#### Combinators

Multiple simple selectors may be joined using combinators to specify elements by location, element type, id, class, or any combination thereof. The order of the selectors is important. For example, `div .myClass {color: red;}` applies to all elements of class myClass that are inside div elements, whereas `.myClass div {color: red;}` applies to all div elements that are inside elements of class myClass. This is not to be confused with concatenated identifiers such as `div.myClass {color: red;}` which applies to div elements of class myClass.

#### Summary of selector syntax

The following table provides a summary of selector syntax indicating usage and the version of CSS that introduced it.

| Pattern | Matches | First defined in CSS level |
|---|---|---|
| `E` | an element of type E | 1 |
| `E:link` | an E element that is the source anchor of a hyperlink whose target is either not yet visited (:link) or already visited (:visited) | 1 |
| `E:visited` |   |   |
| `E:active` | an E element during certain user actions | 1 |
| `E:hover` | 2 |   |
| `E:focus` |   |   |
| `E::first-line` | the first formatted line of an E element | 1 |
| `E::first-letter` | the first formatted letter of an E element | 1 |
| `.c` | all elements with class="c" | 1 |
| `#myid` | the element with id="myid" | 1 |
| `E.warning` | an E element whose class is "warning" (the document language specifies how class is determined) | 1 |
| `E#myid` | an E element with ID equal to "myid" | 1 |
| `.c#myid` | the element with class="c" and ID equal to "myid" | 1 |
| `E F` | an F element descendant of an E element | 1 |
| `*` | any element | 2 |
| `E[foo]` | an E element with a "foo" attribute | 2 |
| `E[foo="bar"]` | an E element whose "foo" attribute value is exactly equal to "bar" | 2 |
| `E[foo~="bar"]` | an E element whose "foo" attribute value is a list of whitespace-separated values, one of which is exactly equal to "bar" | 2 |
| `E[foo\|="en"]` | an E element whose "foo" attribute has a hyphen-separated list of values beginning (from the left) with "en" | 2 |
| `E:first-child` | an E element, first child of its parent | 2 |
| `E:lang(fr)` | an element of type E in language "fr" (the document language specifies how language is determined) | 2 |
| `E::before` | generated content before an E element's content | 2 |
| `E::after` | generated content after an E element's content | 2 |
| `E > F` | an F element child of an E element | 2 |
| `E + F` | an F element immediately preceded by an E element | 2 |
| `E[foo^="bar"]` | an E element whose "foo" attribute value begins exactly with the string "bar" | 3 |
| `E[foo$="bar"]` | an E element whose "foo" attribute value ends exactly with the string "bar" | 3 |
| `E[foo*="bar"]` | an E element whose "foo" attribute value contains the substring "bar" | 3 |
| `E:root` | an E element, root of the document | 3 |
| `E:nth-child(n)` | an E element, the n-th child of its parent | 3 |
| `E:nth-last-child(n)` | an E element, the n-th child of its parent, counting from the last one | 3 |
| `E:nth-of-type(n)` | an E element, the n-th sibling of its type | 3 |
| `E:nth-last-of-type(n)` | an E element, the n-th sibling of its type, counting from the last one | 3 |
| `E:last-child` | an E element, last child of its parent | 3 |
| `E:first-of-type` | an E element, first sibling of its type | 3 |
| `E:last-of-type` | an E element, last sibling of its type | 3 |
| `E:only-child` | an E element, only child of its parent | 3 |
| `E:only-of-type` | an E element, only sibling of its type | 3 |
| `E:empty` | an E element that has no children (including text nodes) | 3 |
| `E:target` | an E element being the target of the referring URI | 3 |
| `E:enabled` | a user interface element E that is enabled | 3 |
| `E:disabled` | a user interface element E that is disabled | 3 |
| `E:checked` | a user interface element E that is checked (for instance a radio button or checkbox) | 3 |
| `E:not(s)` | an E element that does not match simple selector s | 3 |
| `E ~ F` | an F element preceded by an E element | 3 |
| `E:has(s)` | an E element that contains an element matching simple selector s | 4 |

### Declaration block

A declaration block consists of a pair of braces (`{}`) enclosing a semicolon-separated list of *declarations*.

#### Declaration

Each declaration itself consists of a *property*, a colon (`:`), and a *value*. Optional white-space may be around the declaration block, declarations, colons, and semi-colons for readability.

#### Properties

Properties are specified in the CSS standard. Each property has a set of possible values. Some properties can affect any type of element, and others apply only to particular groups of elements.

#### Values

Values may be keywords, such as "center" or "inherit", or numerical values, such as `200px` (200 pixels), `50vw` (50 percent of the viewport width) or 80% (80 percent of the parent element's width).

Color values can be specified with keywords (e.g. "`red`"), hexadecimal values (e.g. `#FF0000`, also abbreviated as `#F00`), RGB values on a 0 to 255 scale (e.g. `rgb(255, 0, 0)`), RGBA values that specify both color and alpha transparency (e.g. `rgba(255, 0, 0, 0.8)`), or HSL or HSLA values (e.g. `hsl(0 100% 50%)`, `hsl(0 100% 50% / 0.8)`).

Non-zero numeric values representing linear measures must include a length unit, which is either an alphabetic code or abbreviation, as in `200px` or `50vw`; or a percentage sign, as in `80%`. Some units – `cm` (centimetre); `in` (inch); `mm` (millimetre); `pc` (pica); and `pt` (point) – are *absolute*, which means that the rendered dimension does not depend upon the structure of the page; others – `em` (em); `ex` (ex) and `px` (pixel) – are *relative*, which means that factors such as the font size of a parent element can affect the rendered measurement. These eight units were a feature of CSS 1 and retained in all subsequent revisions. The proposed CSS Values and Units Module Level 3 will, if adopted as a W3C Recommendation, provide seven further length units: `ch`; `Q`; `rem`; `vh`; `vmax`; `vmin`; and `vw`.

### Use

Before CSS, nearly all presentational attributes of HTML documents were contained within the HTML markup. That is, all font colors, background styles, element alignments, borders, and sizes had to be explicitly described (often repeatedly) within the HTML. CSS lets authors move much of that information to another file, the style sheet, resulting in considerably simpler HTML. And additionally, as more and more devices are able to access responsive web pages, different screen sizes and layouts begin to appear. Customizing a website for each device size is costly and increasingly difficult. The modular nature of CSS means that styles can be reused in different parts of a site or even across sites, promoting consistency and efficiency.

For example, headings (`h1` elements), sub-headings (`h2`), sub-sub-headings (`h3`), etc., are defined structurally using HTML. In print and on the screen, choice of font, size, color and emphasis for these elements is *presentational*.

Before CSS, document authors who wanted to assign such typographic characteristics to, say, all `h2` headings had to repeat HTML presentational markup for each occurrence of that heading type. This made documents more complex, larger, and more error-prone and difficult to maintain. CSS allows the separation of presentation from structure. CSS can define color, font, text alignment, size, borders, spacing, layout and many other typographic characteristics, and can do so independently for on-screen and printed views. CSS also defines non-visual styles, such as reading speed and emphasis for aural text readers. The W3C has now deprecated the use of all presentational HTML markup.

For example, under pre-CSS HTML, a heading element defined with red text would be written as:

```mw
<h1><font color="red">Chapter 1.</font></h1>
```

Using CSS, the same element can be coded using style properties instead of HTML presentational attributes:

```mw
<h1 style="color: red;">Chapter 1.</h1>
```

The advantages of this may not be immediately clear but the power of CSS becomes more apparent when the style properties are placed in an internal style element or, even better, an external CSS file. For example, suppose the document contains the style element:

```mw
<style>
    h1 {
        color: red;
    }
</style>
```

All `h1` elements in the document will then automatically become red without requiring any explicit code. If the author later wanted to make `h1` elements blue instead, this could be done by changing the style element to:

```mw
<style>
    h1 {
        color: blue;
    }
</style>
```

rather than by laboriously going through the document and changing the color for each individual `h1` element.

The styles can also be placed in an external CSS file, as described below, and loaded using syntax similar to:

```mw
<link href="path/to/file.css" rel="stylesheet" type="text/css">
```

This further decouples the styling from the HTML document and makes it possible to restyle multiple documents by simply editing a shared external CSS file.
