---
title: "paint() CSS function - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/paint
domain: css-paint-api
license: CC-BY-SA-4.0
tags: css painting api, paint worklet registration, programmatic css background, custom paint function
fetched: 2026-07-02
---

# `paint()` CSS function

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`paint()`** CSS function defines an `<image>` value generated with a PaintWorklet.

## Syntax

```css
paint(workletName, ...parameters)
```

where:

***workletName***

The name of the registered worklet.

***parameters* Optional**

Optional additional parameters to pass to the paintWorklet

## Formal syntax

```
<paint()> = 
  paint( <ident> , <declaration-value>? )  
```

## Examples

### Basic CSS paint() usage

Given the following HTML:

```html
<ul>
  <li>item 1</li>
  <li>item 2</li>
  <li>item 3</li>
  <li>item 4</li>
  <li>item 5</li>
  <li>item 6</li>
  <li>item 7</li>
  <li>item 8</li>
  <li>item 9</li>
  <li>item 10</li>
  <li>item N</li>
</ul>
```

In JavaScript, we register the paint worklet:

```js
CSS.paintWorklet.addModule(
  "https://mdn.github.io/houdini-examples/cssPaint/intro/worklets/boxbg.js",
);
```

In the CSS, we define the `background-image` as a `paint()` type with the worklet name, `boxbg`, along with any variables (ex. `--box-color` and `--width-subtractor`) the worklet will use:

```css
body {
  font: 1.2em / 1.2 sans-serif;
}
li {
  background-image: paint(boxbg);
  --box-color: hsl(55 90% 60%);
}

li:nth-of-type(3n) {
  --box-color: hsl(155 90% 60%);
  --width-subtractor: 20;
}

li:nth-of-type(3n + 1) {
  --box-color: hsl(255 90% 60%);
  --width-subtractor: 40;
}
```

### CSS paint() with parameters

You can pass optional arguments in the CSS `paint()` function. In this example, we passed two arguments that control whether the `background-image` on a group of list items is `filled` or has a `stroke` outline, and the `width` of that outline:

```html
<ul>
  <li>item 1</li>
  <li>item 2</li>
  <li>item 3</li>
  <li>item 4</li>
  <li>item 5</li>
  <li>item 6</li>
  <li>item 7</li>
  <li>item 8</li>
  <li>item 9</li>
  <li>item 10</li>
  <li>item N</li>
</ul>
```

```js
CSS.paintWorklet.addModule(
  "https://mdn.github.io/houdini-examples/cssPaint/intro/worklets/hilite.js",
);
```

```css
body {
  font: 1.2em / 1.2 sans-serif;
}

li {
  --box-color: hsl(55 90% 60% / 100%);
  background-image: paint(hollow-highlights, stroke, 2px);
}

li:nth-of-type(3n) {
  --box-color: hsl(155 90% 60% / 100%);
  background-image: paint(hollow-highlights, filled, 3px);
}

li:nth-of-type(3n + 1) {
  --box-color: hsl(255 90% 60% / 100%);
  background-image: paint(hollow-highlights, stroke, 1px);
}
```

We've included a custom property in the selector block defining a boxColor. Custom properties are accessible to the PaintWorklet.

## Specifications

| Specification |
|---|
| CSS Painting API Level 1 # paint-notation |

## Browser compatibility
