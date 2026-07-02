---
title: "<rect> - SVG"
source: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect
domain: svg-graphics
license: CC-BY-SA-2.5
tags: svg vector, scalable vector graphics, svg path, xml vector
fetched: 2026-07-02
---

# <rect>

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`<rect>`** SVG element is a basic SVG shape that draws rectangles, defined by their position, width, and height. The rectangles may have their corners rounded.

## Usage context

| Categories | Basic shape element, Graphics element, Shape element |
|---|---|
| Permitted content | Any number of the following elements, in any order: Animation elements Descriptive elements |

## Attributes

**`x`**

The x coordinate of the rect. *Value type*: **<length>** | **<percentage>**; *Default value*: `0`; *Animatable*: **yes**

**`y`**

The y coordinate of the rect. *Value type*: **<length>** | **<percentage>**; *Default value*: `0`; *Animatable*: **yes**

**`width`**

The width of the rect. *Value type*: `auto` | **<length>** | **<percentage>**; *Default value*: `auto`; *Animatable*: **yes**

**`height`**

The height of the rect. *Value type*: `auto` | **<length>** | **<percentage>**; *Default value*: `auto`; *Animatable*: **yes**

**`rx`**

The horizontal corner radius of the rect. Defaults to `ry` if it is specified. *Value type*: `auto` | **<length>** | **<percentage>**; *Default value*: `auto`; *Animatable*: **yes**

**`ry`**

The vertical corner radius of the rect. Defaults to `rx` if it is specified. *Value type*: `auto` | **<length>** | **<percentage>**; *Default value*: `auto`; *Animatable*: **yes**

**`pathLength`**

The total length of the rectangle's perimeter, in user units. *Value type*: **<number>**; *Default value*: *none*; *Animatable*: **yes**

**Note:** Starting with SVG2, `x`, `y`, `width`, `height`, `rx` and `ry` are *Geometry Properties*, meaning those attributes can also be used as CSS properties for that element.

## DOM Interface

This element implements the `SVGRectElement` interface.

## Example

```css
html,
body,
svg {
  height: 100%;
}
```

```html
<svg viewBox="0 0 220 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Regular rectangle -->
  <rect width="100" height="100" />

  <!-- Rounded corner rectangle -->
  <rect x="120" width="100" height="100" rx="15" />
</svg>
```

## Specifications

| Specification |
|---|
| Scalable Vector Graphics (SVG) 2 # RectElement |

## Browser compatibility
