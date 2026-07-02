---
title: "<path> - SVG"
source: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path
domain: svg-graphics
license: CC-BY-SA-2.5
tags: svg vector, scalable vector graphics, svg path, xml vector
fetched: 2026-07-02
---

# <path>

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`<path>`** SVG element is the generic element to define a shape. All the basic shapes can be created with a path element.

## Usage context

| Categories | Graphics element, Shape element |
|---|---|
| Permitted content | Any number of the following elements, in any order: Animation elements Descriptive elements |

## Attributes

**`d`**

This attribute defines the shape of the path. *Value type*: **<string>**; *Default value*: `''`; *Animatable*: **yes**

**`pathLength`**

This attribute lets authors specify the total length for the path, in user units. *Value type*: **<number>**; *Default value*: *none*; *Animatable*: **yes**

## DOM Interface

This element implements the `SVGPathElement` interface.

## Example

```css
html,
body,
svg {
  height: 100%;
}
```

```html
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path
    d="M 10,30
           A 20,20 0,0,1 50,30
           A 20,20 0,0,1 90,30
           Q 90,60 50,90
           Q 10,60 10,30 z" />
</svg>
```

## Specifications

| Specification |
|---|
| Scalable Vector Graphics (SVG) 2 # PathElement |

## Browser compatibility
