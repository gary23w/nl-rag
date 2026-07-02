---
title: "<bdo> HTML bidirectional text override element - HTML"
source: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo
domain: unicode-bidi-web
license: CC-BY-SA-4.0
tags: bidirectional text, unicode bidi property, right-to-left script, writing mode direction
fetched: 2026-07-02
---

# `<bdo>` HTML bidirectional text override element

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`<bdo>`** HTML element overrides the current directionality of text, so that the text within is rendered in a different direction.

## Try it

```html
<h1>Famous seaside songs</h1>

<p>The English song "Oh I do like to be beside the seaside"</p>

<p>
  Looks like this in Hebrew:
  <span dir="rtl">אה, אני אוהב להיות ליד חוף הים</span>
</p>

<p>
  In the computer's memory, this is stored as
  <bdo dir="ltr">אה, אני אוהב להיות ליד חוף הים</bdo>
</p>
```

```css
html {
  font-family: sans-serif;
}

bdo {
  /* Add your styles here */
}
```

The text's characters are drawn from the starting point in the given direction; the individual characters' orientation is not affected (so characters don't get drawn backward, for example).

## Attributes

This element's attributes include the global attributes.

**`dir`**

The direction in which text should be rendered in this element's contents. Possible values are:

- `ltr`: Indicates that the text should go in a left-to-right direction.
- `rtl`: Indicates that the text should go in a right-to-left direction.

## Examples

```html
<!-- Switch text direction -->
<p>This text will go left to right.</p>
<p><bdo dir="rtl">This text will go right to left.</bdo></p>
```

### Result
