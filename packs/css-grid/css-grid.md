---
title: "grid CSS property - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/grid
domain: css-grid
license: CC-BY-SA-2.5
tags: css grid, grid layout, grid template, grid auto-placement
fetched: 2026-07-02
---

# `grid` CSS property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

- Learn more
- See full compatibility

The **`grid`** CSS property is a shorthand property that sets all of the explicit and implicit grid properties in a single declaration.

Using `grid` you specify one axis using `grid-template-rows` or `grid-template-columns`, you then specify how content should auto-repeat in the other axis using the implicit grid properties: `grid-auto-rows`, `grid-auto-columns`, and `grid-auto-flow`.

## Try it

```css
grid: auto-flow / 1fr 1fr 1fr;
```

```css
grid: auto-flow dense / 40px 40px 1fr;
```

```css
grid: repeat(3, 80px) / auto-flow;
```

```html
<section class="default-example" id="default-example">
  <div class="example-container">
    <div class="transition-all" id="example-element">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
    </div>
  </div>
</section>
```

```css
#example-element {
  border: 1px solid #c5c5c5;
  display: grid;
  grid-gap: 10px;
  width: 200px;
}

#example-element :nth-child(1) {
  background-color: rgb(0 0 255 / 0.2);
  border: 3px solid blue;
}

#example-element :nth-child(2) {
  background-color: rgb(255 0 200 / 0.2);
  border: 3px solid rebeccapurple;
  grid-column: auto / span 3;
  grid-row: auto / span 2;
}

#example-element :nth-child(3) {
  background-color: rgb(94 255 0 / 0.2);
  border: 3px solid green;
  grid-column: auto / span 2;
}
```

**Note:** The sub-properties you don't specify are set to their initial value, as normal for shorthands. Also, the gutter properties are NOT reset by this shorthand.

## Constituent properties

This property is a shorthand for the following CSS properties:

- `grid-auto-columns`
- `grid-auto-flow`
- `grid-auto-rows`
- `grid-template-areas`
- `grid-template-columns`
- `grid-template-rows`

## Syntax

```css
/* <'grid-template'> values */
grid: none;
grid: "a" 100px "b" 1fr;
grid: [line-name1] "a" 100px [line-name2];
grid: "a" 200px "b" min-content;
grid: "a" minmax(100px, max-content) "b" 20%;
grid: 100px / 200px;
grid: minmax(400px, min-content) / repeat(auto-fill, 50px);

/* <'grid-template-rows'> /
   [ auto-flow && dense? ] <'grid-auto-columns'>? values */
grid: 200px / auto-flow;
grid: 30% / auto-flow dense;
grid: repeat(3, 200px) / auto-flow 300px;
grid: [line1] minmax(20em, max-content) / auto-flow dense 40%;

/* [ auto-flow && dense? ] <'grid-auto-rows'>? /
   <'grid-template-columns'> values */
grid: auto-flow / 200px;
grid: auto-flow dense / 30%;
grid: auto-flow 300px / repeat(3, 200px);
grid: auto-flow dense 40% / [line1] minmax(20em, max-content);

/* Global values */
grid: inherit;
grid: initial;
grid: revert;
grid: revert-layer;
grid: unset;
```

### Values

**`<'grid-template'>`**

Defines the `grid-template` including `grid-template-columns`, `grid-template-rows` and `grid-template-areas`.

**`<'grid-template-rows'> / [ auto-flow && dense? ] <'grid-auto-columns'>?`**

Sets up an auto-flow by setting the row tracks explicitly via the `grid-template-rows` property (and the `grid-template-columns` property to `none`) and specifying how to auto-repeat the column tracks via `grid-auto-columns` (and setting `grid-auto-rows` to `auto`). `grid-auto-flow` is also set to `column` accordingly, with `dense` if it's specified.

All other `grid` sub-properties are reset to their initial values.

**`[ auto-flow && dense? ] <'grid-auto-rows'>? / <'grid-template-columns'>`**

Sets up an auto-flow by setting the column tracks explicitly via the `grid-template-columns` property (and the `grid-template-rows` property to `none`) and specifying how to auto-repeat the row tracks via `grid-auto-rows` (and setting `grid-auto-columns` to `auto`). `grid-auto-flow` is also set to `row` accordingly, with `dense` if it's specified.

All other `grid` sub-properties are reset to their initial values.

## Formal definition

| Initial value | as each of the properties of the shorthand: `grid-template-rows`: `none``grid-template-columns`: `none``grid-template-areas`: `none``grid-auto-rows`: `auto``grid-auto-columns`: `auto``grid-auto-flow`: `row``grid-column-gap`: `0``grid-row-gap`: `0``column-gap`: `normal``row-gap`: `normal` |
|---|---|
| Applies to | grid containers |
| Inherited | no |
| Percentages | as each of the properties of the shorthand: `grid-template-rows`: refer to corresponding dimension of the content area`grid-template-columns`: refer to corresponding dimension of the content area`grid-auto-rows`: refer to corresponding dimension of the content area`grid-auto-columns`: refer to corresponding dimension of the content area |
| Computed value | as each of the properties of the shorthand: `grid-template-rows`: as specified, but with relative lengths converted into absolute lengths`grid-template-columns`: as specified, but with relative lengths converted into absolute lengths`grid-template-areas`: as specified`grid-auto-rows`: the percentage as specified or the absolute length`grid-auto-columns`: the percentage as specified or the absolute length`grid-auto-flow`: as specified`grid-column-gap`: the percentage as specified or the absolute length`grid-row-gap`: the percentage as specified or the absolute length`column-gap`: as specified, with <length>s made absolute, and normal computing to zero except on multi-column elements`row-gap`: as specified, with <length>s made absolute, and normal computing to zero except on multi-column elements |
| Animation type | as each of the properties of the shorthand: `grid-template-rows`: simple list of length, percentage, or calc, provided the only differences are in the values of the length, percentage, or calc components in the list`grid-template-columns`: simple list of length, percentage, or calc, provided the only differences are in the values of the length, percentage, or calc components in the list`grid-template-areas`: discrete`grid-auto-rows`: by computed value type`grid-auto-columns`: by computed value type`grid-auto-flow`: discrete`grid-column-gap`: a length`grid-row-gap`: a length`column-gap`: a length, percentage or calc();`row-gap`: a length, percentage or calc(); |

## Formal syntax

```
grid = 
  <'grid-template'>                                   |
  <'grid-template-rows'> / [ auto-flow && dense? ] <'grid-auto-columns'>?  |
  [ auto-flow && dense? ] <'grid-auto-rows'>? / <'grid-template-columns'>  

<grid-template> = 
  none                                                |
  [ <'grid-template-rows'> / <'grid-template-columns'> ]  |
  [ <line-names>? <string> <track-size>? <line-names>? ]+ [ / <explicit-track-list> ]?  

<grid-template-rows> = 
  none                       |
  <track-list>               |
  <auto-track-list>          |
  subgrid <line-name-list>?  

<grid-auto-columns> = 
  <track-size>+  

<grid-auto-rows> = 
  <track-size>+  

<grid-template-columns> = 
  none                       |
  <track-list>               |
  <auto-track-list>          |
  subgrid <line-name-list>?  

<line-names> = 
  '[' <custom-ident>* ']'  

<track-size> = 
  <track-breadth>                                   |
  minmax( <inflexible-breadth> , <track-breadth> )  |
  fit-content( <length-percentage [0,∞]> )          

<explicit-track-list> = 
  [ <line-names>? <track-size> ]+ <line-names>?  

<track-list> = 
  [ <line-names>? [ <track-size> | <track-repeat> ] ]+ <line-names>?  

<auto-track-list> = 
  [ <line-names>? [ <fixed-size> | <fixed-repeat> ] ]* <line-names>? <auto-repeat> [ <line-names>? [ <fixed-size> | <fixed-repeat> ] ]* <line-names>?  

<line-name-list> = 
  [ <line-names> | <name-repeat> ]+  

<track-breadth> = 
  <length-percentage [0,∞]>  |
  <flex [0,∞]>               |
  min-content                |
  max-content                |
  auto                       

<inflexible-breadth> = 
  <length-percentage [0,∞]>  |
  min-content                |
  max-content                |
  auto                       

<length-percentage> = 
  <length>      |
  <percentage>  

<track-repeat> = 
  repeat( [ <integer [1,∞]> ] , [ <line-names>? <track-size> ]+ <line-names>? )  

<fixed-size> = 
  <fixed-breadth>                                   |
  minmax( <fixed-breadth> , <track-breadth> )       |
  minmax( <inflexible-breadth> , <fixed-breadth> )  

<fixed-repeat> = 
  repeat( [ <integer [1,∞]> ] , [ <line-names>? <fixed-size> ]+ <line-names>? )  

<auto-repeat> = 
  repeat( [ auto-fill | auto-fit ] , [ <line-names>? <track-size> ]+ <line-names>? )  

<name-repeat> = 
  repeat( [ <integer [1,∞]> | auto-fill ] , <line-names>+ )  

<integer> = 
  <number-token>  

<fixed-breadth> = 
  <length-percentage [0,∞]>  
```

## Examples

### Creating a grid layout

#### HTML

```html
<div id="container">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
```

#### CSS

```css
#container {
  display: grid;
  grid: repeat(2, 60px) / auto-flow 80px;
}

#container > div {
  background-color: #8ca0ff;
  width: 50px;
  height: 50px;
}
```

#### Result

## Specifications

| Specification |
|---|
| CSS Grid Layout Module Level 2 # grid-shorthand |

## Browser compatibility
