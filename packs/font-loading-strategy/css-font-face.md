---
title: "@font-face CSS at-rule - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face
domain: font-loading-strategy
license: CC-BY-SA-4.0
tags: web font loading, font-display swap, font face rule, css font loading api
fetched: 2026-07-02
---

# `@font-face` CSS at-rule

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`@font-face`** CSS at-rule specifies a custom font with which to display text; the font can be loaded from either a remote server or a locally-installed font on the user's own computer.

## Syntax

```css
@font-face {
  font-family: "Trickster";
  src:
    local("Trickster"),
    url("trickster-COLRv1.otf") format("opentype") tech(color-COLRv1),
    url("trickster-outline.otf") format("opentype"),
    url("trickster-outline.woff2") format("woff2");
}
```

### Descriptors

**`ascent-override`**

Defines the ascent metric for the font.

**`descent-override`**

Defines the descent metric for the font.

**`font-display`**

Determines how a font face is displayed based on whether and when it is downloaded and ready to use.

**`font-family`**

Specifies a name that will be used as the font face value for font properties. A `font-family` name is required for the `@font-face` rule to be valid.

**`font-stretch`**

A `font-stretch` value. Accepts two values to specify a range that is supported by a font face, for example `font-stretch: 50% 200%;`

**`font-style`**

A `font-style` value. Accepts two values to specify a range that is supported by a font face, for example `font-style: oblique 20deg 50deg;`

**`font-weight`**

A `font-weight` value. Accepts two values to specify a range that is supported by a font face, for example `font-weight: 100 400;`

**`font-feature-settings`**

Allows control over advanced typographic features in OpenType fonts.

**`font-variation-settings`**

Allows low-level control over OpenType or TrueType font variations, by specifying the four-letter axis names of the features to vary, along with their variation values.

**`line-gap-override`**

Defines the line gap metric for the font.

**`size-adjust`**

Defines a multiplier for glyph outlines and metrics associated with this font. This makes it easier to harmonize the designs of various fonts when rendered at the same font size.

**`src`**

Specifies references to font resources including hints about the font format and technology. A `src` is required for the `@font-face` rule to be valid.

**`unicode-range`**

The range of Unicode code points to be used from the font.

## Description

It's common to use both `url()` and `local()` together, so that the user's installed copy of the font is used if available, falling back to downloading a copy of the font if it's not found on the user's device.

If the `local()` function is provided, specifying a font name to look for on the user's device, and if the user agent finds a match, that local font is used. Otherwise, the font resource specified using the `url()` function is downloaded and used.

Browsers attempt to load resources in their list declaration order, so usually `local()` should be written before `url()`. Both functions are optional, so a rule block containing only one or more `local()` without `url()` is possible. If more specific fonts with `format()` or `tech()` values are desired, these should be listed *before* versions that don't have these values, as the less specific variant would otherwise be tried and used first.

For web delivery, it's generally best to serve fonts in WOFF2 format, because it compresses fonts more efficiently than older formats like WOFF or OpenType, reducing file size and improving load times. WOFF2 is also well supported in modern browsers, making it a safe default choice for most websites.

By allowing authors to provide their own fonts, `@font-face` makes it possible to design content without being limited to the so-called "web-safe" fonts (that is, the fonts that are so common that they're considered to be universally available). The ability to specify the name of a locally-installed font to look for and use makes it possible to customize the font beyond the basics while making it possible to do so without relying on an internet connection.

**Note:** Fallback strategies for loading fonts on older browsers are described in the `src` descriptor page.

The `@font-face` at-rule may be used not only at the top level of a CSS, but also inside any CSS conditional-group at-rule.

### Font MIME Types

| Format | MIME type |
|---|---|
| TrueType | `font/ttf` |
| OpenType | `font/otf` |
| Web Open Font Format | `font/woff` |
| Web Open Font Format 2 | `font/woff2` |
