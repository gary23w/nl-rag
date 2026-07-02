---
title: "pointer-events CSS property - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events
domain: clickjacking-defense
license: CC-BY-SA-4.0
tags: clickjacking defense, x-frame-options header, ui redress attack, frame busting script
fetched: 2026-07-02
---

# `pointer-events` CSS property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`pointer-events`** CSS property sets under what circumstances (if any) a particular graphic element can become the target of pointer events.

## Try it

```css
pointer-events: auto;
```

```css
pointer-events: none;
```

```css
pointer-events: stroke; /* SVG-only */
```

```css
pointer-events: fill; /* SVG-only */
```

```html
<section class="flex-column" id="default-example">
  <div id="example-element">
    <p>
      <a href="#">example link</a>
    </p>
    <p>
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <a xlink:href="#">
          <circle
            cx="50"
            cy="50"
            fill="#3E6E84"
            r="40"
            stroke="#ffb500"
            stroke-width="5"></circle>
          <text fill="white" text-anchor="middle" x="50" y="55">SVG</text>
        </a>
      </svg>
    </p>
  </div>
</section>
```

```css
#example-element {
  font-weight: bold;
}

#example-element a {
  color: #009e5f;
}

#example-element svg {
  width: 10em;
  height: 10em;
}
```

## Syntax

```css
/* Keyword values */
pointer-events: auto;
pointer-events: none;

/* Values used in SVGs */
pointer-events: visiblePainted;
pointer-events: visibleFill;
pointer-events: visibleStroke;
pointer-events: visible;
pointer-events: painted;
pointer-events: fill;
pointer-events: stroke;
pointer-events: bounding-box;
pointer-events: all;

/* Global values */
pointer-events: inherit;
pointer-events: initial;
pointer-events: revert;
pointer-events: revert-layer;
pointer-events: unset;
```

The `pointer-events` property is specified as a single keyword chosen from the list of values below.

### Values

**`auto`**

The element behaves as it would if the `pointer-events` property were not specified. In SVG content, this value and the value `visiblePainted` have the same effect.

**`none`**

The element on its own is never the target of pointer events. However its subtree could be kept targetable by setting `pointer-events` to some other value. In these circumstances, pointer events will trigger event listeners on this parent element as appropriate on their way to or from the descendant during the event capture and bubble phases.

**Note:** The `pointerenter` and `pointerleave` events are fired when a pointing device is moved into an element or one of its descendants. So, even if `pointer-events: none` is set on the parent and not set on children, the events are triggered on the parent after the pointer is moved in or out of a descendant.

#### SVG only (experimental for HTML)

**`visiblePainted`**

SVG only (experimental for HTML). The element can only be the target of a pointer event when the `visibility` property is set to `visible` and e.g., when a mouse cursor is over the interior (i.e., 'fill') of the element and the `fill` property is set to a value other than `none`, or when a mouse cursor is over the perimeter (i.e., 'stroke') of the element and the `stroke` property is set to a value other than `none`.

**`visibleFill`**

SVG only. The element can only be the target of a pointer event when the `visibility` property is set to `visible` and when e.g., a mouse cursor is over the interior (i.e., fill) of the element. The value of the `fill` property does not affect event processing.

**`visibleStroke`**

SVG only. The element can only be the target of a pointer event when the `visibility` property is set to `visible` and e.g., when the mouse cursor is over the perimeter (i.e., stroke) of the element. The value of the `stroke` property does not affect event processing.

**`visible`**

SVG only (experimental for HTML). The element can be the target of a pointer event when the `visibility` property is set to `visible` and e.g., the mouse cursor is over either the interior (i.e., fill) or the perimeter (i.e., stroke) of the element. The values of the `fill` and `stroke` do not affect event processing.

**`painted`**

SVG only (experimental for HTML). The element can only be the target of a pointer event when e.g., the mouse cursor is over the interior (i.e., 'fill') of the element and the `fill` property is set to a value other than `none`, or when the mouse cursor is over the perimeter (i.e., 'stroke') of the element and the `stroke` property is set to a value other than `none`. The value of the `visibility` property does not affect event processing.

**`fill`**

SVG only. The element can only be the target of a pointer event when the pointer is over the interior (i.e., fill) of the element. The values of the `fill` and `visibility` properties do not affect event processing.

**`stroke`**

SVG only. The element can only be the target of a pointer event when the pointer is over the perimeter (i.e., stroke) of the element. The values of the `stroke` and `visibility` properties do not affect event processing.

**`bounding-box`**

SVG only. The element can only be the target of a pointer event when the pointer is over the bounding box of the element.

**`all`**

SVG only (experimental for HTML). The element can only be the target of a pointer event when the pointer is over the interior (i.e., fill) or the perimeter (i.e., stroke) of the element. The values of the `fill`, `stroke`, and `visibility` properties do not affect event processing.

## Description

When this property is unspecified, the same characteristics of the `visiblePainted` value apply to SVG content.

In addition to indicating that the element is not the target of pointer events, the value `none` instructs the pointer event to go "through" the element and target whatever is "underneath" that element instead.

Note that preventing an element from being the target of pointer events by using `pointer-events` does *not* necessarily mean that pointer event listeners on that element *cannot* or *will not* be triggered. If one of the element's children has `pointer-events` explicitly set to *allow* that child to be the target of pointer events, then any events targeting that child will pass through the parent as the event travels along the parent chain, and trigger event listeners on the parent as appropriate. Of course any pointer activity at a point on the screen that is covered by the parent but not by the child will not be caught by either the child or the parent (it will go "through" the parent and target whatever is underneath).

Elements with `pointer-events: none` will still receive focus through sequential keyboard navigation using the Tab key.

## Formal definition

| Initial value | `auto` |
|---|---|
| Applies to | all elements |
| Inherited | yes |
| Computed value | as specified |
| Animation type | discrete |

## Formal syntax

```
pointer-events = 
  auto            |
  bounding-box    |
  visiblePainted  |
  visibleFill     |
  visibleStroke   |
  visible         |
  painted         |
  fill            |
  stroke          |
  all             |
  none            
```

## Examples

### Disabling pointer events on all images

This example disables pointer events (clicking, dragging, hovering, etc.) on all images.

```css
img {
  pointer-events: none;
}
```

### Disabling pointer events on a single link

This example disables pointer events on the link to `http://example.com`.

#### HTML

```html
<ul>
  <li><a href="https://developer.mozilla.org">MDN</a></li>
  <li><a href="http://example.com">example.com</a></li>
</ul>
```

#### CSS

```css
a[href="http://example.com"] {
  pointer-events: none;
}
```

#### Result

## Specifications

| Specification |
|---|
| CSS Basic User Interface Module Level 4 # pointer-events-control |
| Scalable Vector Graphics (SVG) 2 # PointerEventsProperty |

## Browser compatibility
