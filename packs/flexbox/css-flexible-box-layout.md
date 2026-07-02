---
title: "CSS flexible box layout - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout
domain: flexbox
license: CC-BY-SA-2.5
tags: flexbox, flexible box layout, flex container, justify-content, align-items
fetched: 2026-07-02
---

# CSS flexible box layout

The **CSS flexible box layout** module defines a CSS box model optimized for user interface design, and the layout of items in one dimension. In the flex layout model, the children of a flex container can be laid out in any direction, and can "flex" their sizes, either growing to fill unused space or shrinking to avoid overflowing the parent. Both horizontal and vertical alignment of the children can be easily manipulated.

## Flexible box layout in action

In the following example, a container has been set to `display: flex`, which means that the three child items become flex items. The value of `justify-content` has been set to `space-between` in order to space the items out evenly on the main axis. An equal amount of space is placed between each item with the left and right items being flush with the edges of the flex container. You can also see that the items are stretching on the cross axis, due to the default value of `align-items` being `stretch`. The items stretch to the height of the flex container, making them each appear as tall as the tallest item.

```html
<div class="box">
  <div>One</div>
  <div>Two</div>
  <div>Three <br />has <br />extra <br />text</div>
</div>
```

```css
body {
  font-family: sans-serif;
}

.box {
  border: 2px dotted rgb(96 139 168);
  display: flex;
  justify-content: space-between;
}

.box > * {
  border: 2px solid rgb(96 139 168);
  border-radius: 5px;
  background-color: rgb(96 139 168 / 0.2);
  padding: 1em;
}
```

## Reference

### Properties

- `align-content`
- `align-items`
- `align-self`
- `flex`
- `flex-basis`
- `flex-direction`
- `flex-flow`
- `flex-grow`
- `flex-shrink`
- `flex-wrap`
- `justify-content`

### Glossary terms

- Flexbox
- Flex container
- Flex item
- Main axis
- Cross axis
- Flex

## Guides

**Basic concepts of flexbox**

An overview of the features of Flexbox.

**Relationship of flexbox to other layout methods**

How Flexbox relates to other layout methods and other CSS specifications.

**Aligning items in a flex container**

How the box alignment properties work with Flexbox.

**Ordering flex items**

Explaining the different ways to change the order and direction of items, and covering the potential issues in doing so.

**Controlling ratios of flex items along the main axis**

Explaining the flex-grow, flex-shrink and flex-basis properties.

**Mastering wrapping of flex items**

How to create flex containers with multiple lines and control the display of the items in those lines.

**Typical use cases of flexbox**

Common design patterns that are typical Flexbox use cases.

**CSS layout: flexbox**

Learn how to use flexbox layout to create web layouts.

**Box alignment in flexbox**

Details features of CSS box alignment which are specific to flexbox.

CSS display module

- `display`
- `order`

CSS box alignment module

- `align-content`
- `align-items`
- `align-self`
- `justify-items`
- `place-content`
- `place-items`

CSS gaps module

- `column-gap`
- `gap`
- `row-gap`

CSS box sizing module

- `aspect-ratio`
- `max-content` value
- `min-content` value
- `fit-content` value
- intrinsic size glossary term

## Specifications

| Specification |
|---|
| CSS Flexible Box Layout Module Level 1 |
