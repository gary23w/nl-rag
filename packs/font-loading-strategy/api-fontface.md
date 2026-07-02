---
title: "FontFace - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/FontFace
domain: font-loading-strategy
license: CC-BY-SA-4.0
tags: web font loading, font-display swap, font face rule, css font loading api
fetched: 2026-07-02
---

# FontFace

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`FontFace`** interface of the CSS Font Loading API represents a single usable font face.

This interface defines the source of a font face, either a URL to an external resource or a buffer, and font properties such as `style`, `weight`, and so on. For URL font sources it allows authors to trigger when the remote font is fetched and loaded, and to track loading status.

## Constructor

**`FontFace()`**

Constructs and returns a new `FontFace` object, built from an external resource described by a URL or from an `ArrayBuffer`.

## Instance properties

**`FontFace.ascentOverride`**

A string that retrieves or sets the *ascent metric* of the font. It is equivalent to the `ascent-override` descriptor.

**`FontFace.descentOverride`**

A string that retrieves or sets the *descent metric* of the font. It is equivalent to the `descent-override` descriptor.

**`FontFace.display`**

A string that determines how a font face is displayed based on whether and when it is downloaded and ready to use.

**`FontFace.family`**

A string that retrieves or sets the *family* of the font. It is equivalent to the `font-family` descriptor.

**`FontFace.featureSettings`**

A string that retrieves or sets infrequently used font features that are not available from a font's variant properties. It is equivalent to the CSS `font-feature-settings` property.

**`FontFace.lineGapOverride`**

A string that retrieves or sets the *line-gap metric* of the font. It is equivalent to the `line-gap-override` descriptor.

**`FontFace.loaded` Read only**

Returns a `Promise` that resolves with the current `FontFace` object when the font specified in the object's constructor is done loading or rejects with a `SyntaxError` `DOMException`.

**`FontFace.status` Read only**

Returns an enumerated value indicating the status of the font, one of `"unloaded"`, `"loading"`, `"loaded"`, or `"error"`.

**`FontFace.stretch`**

A string that retrieves or sets how the font *stretches*. It is equivalent to the `font-stretch` descriptor.

**`FontFace.style`**

A string that retrieves or sets the *style* of the font. It is equivalent to the `font-style` descriptor.

**`FontFace.unicodeRange`**

A string that retrieves or sets the *range of unicode code points* encompassing the font. It is equivalent to the `unicode-range` descriptor.

**`FontFace.variant`**

A string that retrieves or sets the *variant* of the font.

**`FontFace.variationSettings`**

A string that retrieves or sets the *variation settings* of the font. It is equivalent to the `font-variation-settings` descriptor.

**`FontFace.weight`**

A string that contains the *weight* of the font. It is equivalent to the `font-weight` descriptor.

**`FontFace.load()`**

Loads a font based on current object's constructor-passed requirements, including a location or source buffer, and returns a `Promise` that resolves with the current FontFace object.

## Examples

The code below defines a font face using data at the URL "my-font.woff" with a few font descriptors. Just to show how it works, we then define the `stretch` descriptor using a property.

```js
// Define a FontFace
const font = new FontFace("my-font", 'url("my-font.woff")', {
  style: "italic",
  weight: "400",
});

font.stretch = "condensed";
```

Next we load the font using `FontFace.load()` and use the returned promise to track completion or report an error.

```js
// Load the font
font.load().then(
  () => {
    // Resolved - add font to document.fonts
  },
  (err) => {
    console.error(err);
  },
);
```

To actually *use* the font we will need to add it to a `FontFaceSet`. We could do that before or after loading the font.

For additional examples see CSS Font Loading API > Examples.

## Specifications

| Specification |
|---|
| CSS Font Loading Module Level 3 # fontface-interface |

## Browser compatibility
