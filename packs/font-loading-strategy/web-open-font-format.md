---
title: "Web Open Font Format"
source: https://en.wikipedia.org/wiki/Web_Open_Font_Format
domain: font-loading-strategy
license: CC-BY-SA-4.0
tags: web font loading, font-display swap, font face rule, css font loading api
fetched: 2026-07-02
---

# Web Open Font Format

The **Web Open Font Format** (**WOFF**) is a font format for use in web pages. WOFF files are OpenType or TrueType fonts, with format-specific compression applied and additional XML metadata added. The two primary goals are first to distinguish font files intended for use as web fonts from fonts files intended for use in desktop applications via local installation, and second to reduce web font latency when fonts are transferred from a server to a client over a network connection.

## Standardization

The first draft of WOFF 1 was published in 2009 by Jonathan Kew, Tal Leming, and Erik van Blokland, with reference conversion code written by Jonathan Kew. Following the submission of WOFF to the World Wide Web Consortium (W3C) by the Mozilla Foundation, Opera Software and Microsoft in April 2010, the W3C commented that it expected WOFF to soon become the "single, interoperable [font] format" supported by all browsers. The W3C published WOFF as a working draft in July 2010. The final draft was published as a W3C Recommendation on 13 December 2012.

WOFF 2.0 significantly improved compression efficiency compared to WOFF 1.0, primarily through the introduction of Brotli, a new byte-level compression algorithm developed by Jyrki Alakuijala and Zoltan Szabadka. Brotli's effectiveness led to its widespread adoption, notably for HTTP content encoding. WOFF 2.0 was standardized as a W3C Recommendation in March 2018, with Google providing the reference implementation.

Each version of the format has received the backing of many type foundries.

## Specification

WOFF is a wrapper containing SFNT-based fonts (TrueType or OpenType) that have been compressed using a WOFF-specific encoding tool so they can be embedded in a Web page. WOFF Version 1 uses the widely available zlib compression (specifically, the compress2 function), typically resulting in a file size reduction for TrueType files of over 40%. Since OpenType CFF files (with PostScript glyph outlines) are already compressed, their reduction is typically smaller.

## Browser support

Major web browsers support WOFF:

- Firefox since version 3.6
- Google Chrome since version 6.0
- Internet Explorer since version 9
- Konqueror since KDE 4.4.1
- Microsoft Edge
- Opera since version 11.10 (Presto 2.7.81)
- Safari 5.1
- other WebKit-based browsers since WebKit build 528

WOFF 2.0 is supported in:

- Google Chrome (since version 36),
- Edge (since version 14),
- Opera (since version 26),
- Firefox (since version 35)
- Safari (since version 10).

Some browsers enforce a same-origin policy, preventing WOFF fonts from being used across different domains. This restriction is part of the CSS 3 Fonts module, where it applies to all font formats and can be overridden by the server providing the font.

Some servers may require the manual addition of WOFF's MIME type to serve the files correctly. Since February 2017, the proper MIME type is `font/woff` for WOFF 1.0 and `font/woff2` for WOFF 2.0. Prior to February 2017, the standard MIME type for WOFF 1.0 was `application/font-woff`, and some applications may still use the old type, though it is now deprecated.
