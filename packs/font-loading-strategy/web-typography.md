---
title: "Web typography"
source: https://en.wikipedia.org/wiki/Web_typography
domain: font-loading-strategy
license: CC-BY-SA-4.0
tags: web font loading, font-display swap, font face rule, css font loading api
fetched: 2026-07-02
---

# Web typography

**Web typography**, like typography generally, is the design of pages – their layout and typeface choices. Unlike traditional print-based typography (where the page is fixed once typeset), pages intended for display on the World Wide Web have additional technical challenges and – given its ability to change the presentation dynamically – additional opportunities. Early web page designs were very simple due to technology limitations; modern designs use Cascading Style Sheets (CSS), JavaScript and other techniques to deliver the typographer's and the client's vision.

When HTML was first created, typefaces and styles were controlled exclusively by the settings of each web browser. There was no mechanism for individual Web pages to control font display until Netscape introduced the `font` element in 1995, which was then standardized in the HTML 3.2 specification. However, the computer font specified by the `font` element had to be installed on the user's computer or a fallback font, such as a browser's default sans-serif or monospace font, would be used. The first CSS specification was published in 1996 and provided the same capabilities.

The CSS2 specification was released in 1998 and attempted to improve the font selection process by adding font matching, synthesis and download. These techniques did not gain much use, and were removed in the CSS2.1 specification. However, Internet Explorer added support for the font downloading feature in version 4.0, released in 1997. Font downloading was later included in the CSS3 fonts module, and has since been implemented in Safari 3.1, Opera 10 and Mozilla Firefox 3.5. This has subsequently increased interest in Web typography, as well as the use of font downloading.

## CSS1

In the first CSS specification, authors specified font characteristics via a series of properties:

- `font-family`
- `font-style`
- `font-variant`
- `font-weight`
- `font-size`

All fonts were identified solely by name. Beyond the properties mentioned above, designers had no way to style fonts, and no mechanism existed to select fonts not present on the client system.

### Web-safe fonts

**Web-safe fonts** are computer fonts that may reasonably be expected to be present on a wide range of computer systems, and used by Web content authors to increase the likelihood that content displays in their chosen font. If a visitor to a Web site does not have the specified font, their browser tries to select a similar alternative, based on the author-specified fallback fonts and generic families or it uses font substitution defined in the visitor's operating system.

### Microsoft's Core fonts for the Web

To ensure that all Web users had a basic set of fonts, Microsoft started the Core fonts for the Web initiative in 1996 (terminated in 2002). Released fonts include Arial, Courier New, Times New Roman, Comic Sans, Impact, Georgia, Trebuchet, Webdings and Verdana—under an EULA that made them freely distributable but also limited some rights to their use. Their high penetration rate has made them a staple for Web designers. However, most Linux distributions don't include these fonts by default.

CSS2 attempted to increase the tools available to Web developers by adding font synthesis, improved font matching and the ability to download remote fonts.

Some CSS2 font properties were removed from CSS2.1 and later included in CSS3.

### Fallback fonts

The CSS specification allows for multiple fonts to be listed as fallback fonts. In CSS, the `font-family` property accepts a list of comma-separated font faces to use, like so:

```mw
font-family: "Nimbus Sans L", Helvetica, Arial, sans-serif;
```

The first font specified is the preferred font. If this font is not available, the Web browser attempts to use the next font in the list. If none of the fonts specified are found, the browser displays its default font. This same process also happens on a per-character basis if the browser tries to display a character not present in the specified font.

### Generic font families

To give Web designers some control over the appearance of fonts on their Web pages, even when the specified fonts are not available, the CSS specification allows the use of several generic font families. These families are designed to split fonts into several categories based on their general appearance. They are commonly specified as the last in a series of fallback fonts, as a last resort in the event that none of the fonts specified by the author are available. For several years, there were five generic families:

Sans-serif

Fonts that do not have decorative markings, or serifs, on their letters. These fonts are often considered easier to read on screens.

Serif

Fonts that have decorative markings, or serifs, present on their characters. These fonts are traditionally used in printed books.

Monospace

Fonts in which all characters are equally wide.

Cursive

Fonts that resemble cursive writing. These fonts may have a decorative appearance, but they can be difficult to read at small sizes, so they are generally used sparingly.

Fantasy

Fonts that may contain symbols or other decorative properties, but still represent the specified character.

### CSS fonts working draft 4 with lesser browser support

As of February 2024, the CSS Working Group of W3C proposes that systems specify a default font using `ui` tags; as of the same date, these are not widely supported yet.

- System-ui Default fonts on a given system: the purpose of this option is to allow web content to integrate with the look and feel of the native OS.
- ui-serif Default fonts on a given system in a serif style
- ui-sans-serif Default fonts on a given system in a sans-serif style
- ui-monospace Default fonts on a given system in a monospace style
- ui-rounded Default fonts on a given system in a rounded style
- Emoji Fonts using emoji
- Math Fonts for complex mathematical formula and expressions.
- Fangsong (Chinese: 仿宋体)
  - Chinese typefaces that are between serif Song and cursive Kai forms. This style is often used for government documents.

## Web fonts

### History

A technique to refer to and automatically download remote fonts was first specified in the CSS2 specification, which introduced the `@font-face` construct. At the time, fetching font files from the web was controversial because fonts meant to be used only for certain web pages could also be downloaded and installed in breach of the font license.

Microsoft first added support for downloadable EOT fonts in Internet Explorer 4 in 1997. Authors had to use the proprietary WEFT tool to create a subsetted font file for each page. EOT showed that webfonts could work and the format saw some use in writing systems not supported by common operating systems. However, the format never gained widespread acceptance and was ultimately rejected by W3C.

In 2006, Håkon Wium Lie started a campaign against using EOT and rather have web browsers support commonly used font formats. Support for the commonly used TrueType and OpenType font formats has since been implemented in Safari 3.1, Opera 10, Mozilla Firefox 3.5 and Internet Explorer 9.

In 2010, the WOFF compression method for TrueType and OpenType fonts was submitted to W3C by the Mozilla Foundation, Opera Software and Microsoft, and browsers have since added support.

Google Fonts was launched in 2010 to serve webfonts under open-source licenses. By 2016, more than 800 webfont families are available.

Webfonts have become an important tool for web designers and as of 2016 a majority of sites use webfonts.

### File formats

By using a specific CSS `@font-face` embedding technique it is possible to embed fonts such that they work with IE4+, Firefox 3.5+, Safari 3.1+, Opera 10+ and Chrome 4.0+. This allows the vast majority of Web users to access this functionality. Some commercial foundries object to the redistribution of their fonts. For example, Hoefler & Frere-Jones says that, while they "...enthusiastically [support] the emergence of a more expressive Web in which designers can safely and reliably use high-quality fonts online," the current delivery of fonts using `@font-face` is considered "illegal distribution" by the foundry and is not permitted. Instead, Hoefler & Co. offer a proprietary font delivery system rooted in the cloud. Many other commercial type foundries address the redistribution of their fonts by offering a specific license, known as a web font license, which permits the use of the font software to display content on the web, a use normally prohibited by basic desktop licenses. Naturally this does not interfere with fonts and foundries under free licences.

#### TrueDoc

TrueDoc, while not specifically a webfont specification, was the first standard for embedding fonts. It was developed by the type foundry Bitstream in 1994, and became natively supported in Netscape Navigator 4, in 1996. Due to open source license restrictions, with Netscape unable to release Bitstream's source code, native support for the technology ended when Netscape Navigator 6 was released. An ActiveX plugin was available to add support for TrueDoc to Internet Explorer, but the technology had to compete against Microsoft's Embedded OpenType fonts, which had natively supported in their Internet Explorer browser since version 4.0. Another impediment was the lack of open-source or free tool to create webfonts in TrueDoc format, whereas Microsoft made available a free Web Embedding Fonts Tool to create webfonts in their format.

#### Embedded OpenType

Internet Explorer has supported font embedding through the proprietary Embedded OpenType standard since version 4.0. It uses digital rights management techniques to help prevent fonts from being copied and used without a license. A simplified subset of EOT has been formalized under the name of CWT (*Compatibility Web Type*, formerly *EOT-Lite*)

#### Scalable Vector Graphics

Web typography applies to SVG in two ways:

1. All versions of the SVG 1.1 specification, including the SVGT subset, define a font module allowing the creation of fonts within an SVG document. Safari introduced support for many of these properties in version 3. Opera added preliminary support in version 8.0, with support for more properties in 9.0.
2. The SVG specification lets CSS apply to SVG documents in a similar manner to HTML documents, and the `@font-face` rule can be applied to text in SVG documents. Opera added support for this in version 10, and WebKit since version 325 also supports this method using SVG fonts only.

#### Scalable Vector Graphics Fonts

SVG fonts was a W3C standard of fonts using SVG graphic that became a subset of OpenType fonts. It allowed multicolor or animated fonts. It was first a subset of SVG 1.1 specifications but it has been deprecated in the SVG 2.0 specification. The SVG fonts as independent format is supported by most browsers apart from IE and Firefox, and is deprecated in Chrome (and Chromium). That's now generally deprecated; the standard that most browser vendor agreed with is SVG font subset included in OpenType (and then WOFF superset, see below), called SVGOpenTypeFonts. Firefox has supported SVG OpenType since Firefox 26.

#### TrueType/OpenType

Linking to industry-standard *TrueType* (TTF) and *OpenType* (TTF/OTF) fonts is supported by Mozilla Firefox 3.5+, Opera 10+, Safari 3.1+, and Google Chrome 4.0+. Internet Explorer 9+ supports only those fonts with embedding permissions set to installable.

#### Web Open Font Format

The Web Open Font Format (WOFF) is essentially OpenType or TrueType with compression and additional metadata. WOFF is supported by Mozilla Firefox 3.6+, Google Chrome 5+, Opera Presto, and is supported by Internet Explorer 9 (since March 14, 2011). Support is available on Mac OS X Lion's Safari from release 5.1.

## Unicode fonts

The term *Unicode font* is a computer font that maps glyphs to code points defined in the Unicode Standard. The term has become redundant since the vast majority of modern computer fonts use Unicode mappings, even those fonts which only include glyphs for a single writing system, or even only support the basic Latin alphabet. Fonts which support a wide range of Unicode scripts and Unicode symbols are sometimes referred to as "pan-Unicode fonts", although as the maximum number of glyphs that can be defined in a TrueType font is restricted to 65,535, it is not possible for a single font to provide individual glyphs for all defined Unicode characters (159,801 characters, with Unicode 17.0).

Only two fonts available by default on the Windows platform, Microsoft Sans Serif and Lucida Sans Unicode, provide a wide Unicode character repertoire.

On free and open-source software platforms such as Linux, GNU Unifont and GNU FreeFont provide a wide range of characters. On ChromeOS, Google's Noto fonts support (or are planned to support) all the scripts encoded in the Unicode standard

## Alternatives

A common hurdle in Web design is the design of mockups that include fonts that are not Web-safe. There are a number of solutions for situations like this. One common solution is to replace the text with a similar Web-safe font or use a series of similar-looking fallback fonts.

Another technique is *image replacement*. This practice involves overlaying text with an image containing the same text written in the desired font. This is good for aesthetic purposes, but prevents text selection, increases bandwidth use, is bad for search engine optimization, and makes the text inaccessible for users with disabilities.

In the past, Flash-based solutions such as sIFR were used. This is similar to image replacement techniques, though the text is selectable and rendered as a vector. However, this method requires the presence of a proprietary plugin on a client's system.

Another solution is using JavaScript to replace the text with VML (for Internet Explorer) or SVG (for all other browsers).
