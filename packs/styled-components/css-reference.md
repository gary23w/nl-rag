---
title: "CSS reference - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
domain: styled-components
license: CC-BY-SA-4.0
tags: styled components, css-in-js, component-scoped styling, tagged template css
fetched: 2026-07-02
---

# CSS reference

Use this **CSS reference** to browse an alphabetical index of all of the standard CSS properties, pseudo-classes, pseudo-elements, data types, functional notations and at-rules. You can also browse key CSS concepts and a list of selectors organized by type. Also included is a brief DOM-CSS / CSSOM reference.

## Basic rule syntax

### Style rule syntax

```
style-rule ::=
    selectors-list {
      properties-list
    }
```

Where:

```
selectors-list ::=
    selector[:pseudo-class] [::pseudo-element]
    [, selectors-list]

properties-list ::=
    [property : value] [; properties-list]
```

See the index of *selectors*, *pseudo-classes*, and *pseudo-elements* below. The syntax for each specified *value* depends on the data type defined for each specified *property*.

#### Style rule examples

```css
strong {
  color: red;
}

div.menu-bar li:hover > ul {
  display: block;
}
```

For a beginner-level introduction to the syntax of selectors, see our guide on CSS Selectors. Be aware that any syntax error in a rule definition invalidates the entire rule. Invalid rules are ignored by the browser. Note that CSS rule definitions are entirely (Unicode) text-based, whereas DOM-CSS / CSSOM (the rule management system) is object-based.

### At-rule syntax

As the structure of at-rules varies widely, please see At-rule to find the syntax of the specific one you want.

## Index

**Note:** This index does not include SVG-exclusive presentation attributes, which can be used as CSS properties on SVG elements.

**Note:** The property names in this index do **not** include the JavaScript names which do differ from the CSS standard names.

### -

- `-webkit-text-fill-color CSS property`
- `-webkit-text-stroke CSS property`
- `-webkit-text-stroke-color CSS property`
- `-webkit-text-stroke-width CSS property`

### A

- `Attribute selectors`
- `abs() CSS function`
- `<absolute-size> CSS type`
- `accent-color CSS property`
- `acos() CSS function`
- `:active CSS pseudo-class`
- `:active-view-transition CSS pseudo-class`
- `:active-view-transition-type() CSS pseudo-class`
- `additive-symbols CSS at-rule descriptor (@counter-style)`
- `::after CSS pseudo-element`
- `align-content CSS property`
- `align-items CSS property`
- `align-self CSS property`
- `alignment-baseline CSS property`
- `all CSS property`
- `alpha() CSS function`
- `<alpha-value> CSS type`
- `anchor() CSS function`
- `anchor-name CSS property`
- `anchor-scope CSS property`
- `anchor-size() CSS function`
- `<angle-percentage> CSS type`
- `<angle> CSS type`
- `animation CSS property`
- `animation-composition CSS property`
- `animation-delay CSS property`
- `animation-direction CSS property`
- `animation-duration CSS property`
- `animation-fill-mode CSS property`
- `animation-iteration-count CSS property`
- `animation-name CSS property`
- `animation-play-state CSS property`
- `animation-range CSS property`
- `animation-range-end CSS property`
- `animation-range-start CSS property`
- `animation-timeline CSS property`
- `animation-timing-function CSS property`
- `:any-link CSS pseudo-class`
- `appearance CSS property`
- `ascent-override CSS at-rule descriptor (@font-face)`
- `asin() CSS function`
- `aspect-ratio CSS property`
- `atan() CSS function`
- `atan2() CSS function`
- `attr() CSS function`
- `:autofill CSS pseudo-class`
- `<axis> CSS type`

### B

- `::backdrop CSS pseudo-element`
- `backdrop-filter CSS property`
- `backface-visibility CSS property`
- `background CSS property`
- `background-attachment CSS property`
- `background-blend-mode CSS property`
- `background-clip CSS property`
- `background-color CSS property`
- `background-image CSS property`
- `background-origin CSS property`
- `background-position CSS property`
- `background-position-x CSS property`
- `background-position-y CSS property`
- `background-repeat CSS property`
- `background-repeat-x CSS property`
- `background-repeat-y CSS property`
- `background-size CSS property`
- `base-palette CSS at-rule descriptor (@font-palette-values)`
- `<baseline-position> CSS type`
- `baseline-shift CSS property`
- `baseline-source CSS property`
- `<basic-shape> CSS type`
- `::before CSS pseudo-element`
- `:blank CSS pseudo-class`
- `<blend-mode> CSS type`
- `block-size CSS property`
- `blur() CSS function`
- `border CSS property`
- `border-block CSS property`
- `border-block-color CSS property`
- `border-block-end CSS property`
- `border-block-end-color CSS property`
- `border-block-end-style CSS property`
- `border-block-end-width CSS property`
- `border-block-start CSS property`
- `border-block-start-color CSS property`
- `border-block-start-style CSS property`
- `border-block-start-width CSS property`
- `border-block-style CSS property`
- `border-block-width CSS property`
- `border-bottom CSS property`
- `border-bottom-color CSS property`
- `border-bottom-left-radius CSS property`
- `border-bottom-right-radius CSS property`
- `border-bottom-style CSS property`
- `border-bottom-width CSS property`
- `border-collapse CSS property`
- `border-color CSS property`
- `border-end-end-radius CSS property`
- `border-end-start-radius CSS property`
- `border-image CSS property`
- `border-image-outset CSS property`
- `border-image-repeat CSS property`
- `border-image-slice CSS property`
- `border-image-source CSS property`
- `border-image-width CSS property`
- `border-inline CSS property`
- `border-inline-color CSS property`
- `border-inline-end CSS property`
- `border-inline-end-color CSS property`
- `border-inline-end-style CSS property`
- `border-inline-end-width CSS property`
- `border-inline-start CSS property`
- `border-inline-start-color CSS property`
- `border-inline-start-style CSS property`
- `border-inline-start-width CSS property`
- `border-inline-style CSS property`
- `border-inline-width CSS property`
- `border-left CSS property`
- `border-left-color CSS property`
- `border-left-style CSS property`
- `border-left-width CSS property`
- `border-radius CSS property`
- `border-right CSS property`
- `border-right-color CSS property`
- `border-right-style CSS property`
- `border-right-width CSS property`
- `border-spacing CSS property`
- `border-start-end-radius CSS property`
- `border-start-start-radius CSS property`
- `border-style CSS property`
- `border-top CSS property`
- `border-top-color CSS property`
- `border-top-left-radius CSS property`
- `border-top-right-radius CSS property`
- `border-top-style CSS property`
- `border-top-width CSS property`
- `border-width CSS property`
- `bottom CSS property`
- `box-decoration-break CSS property`
- `<box-edge> CSS type`
- `box-shadow CSS property`
- `box-sizing CSS property`
- `break-after CSS property`
- `break-before CSS property`
- `break-inside CSS property`
- `brightness() CSS function`
- `:buffering CSS pseudo-class`

### C

- `Class selectors`
- `Custom properties (--*): CSS variables`
- `calc() CSS function`
- `<calc-keyword> CSS type`
- `calc-size() CSS function`
- `<calc-sum> CSS type`
- `caption-side CSS property`
- `caret CSS property`
- `caret-animation CSS property`
- `caret-color CSS property`
- `caret-shape CSS property`
- `@charset CSS at-rule`
- `:checked CSS pseudo-class`
- `::checkmark CSS pseudo-element`
- `circle() CSS function`
- `clamp() CSS function`
- `clear CSS property`
- `clip-path CSS property`
- `clip-rule CSS property`
- `color CSS property`
- `color() CSS function`
- `color-interpolation CSS property`
- `color-interpolation-filters CSS property`
- `<color-interpolation-method> CSS type`
- `color-mix() CSS function`
- `@color-profile CSS at-rule`
- `color-scheme CSS property`
- `<color> CSS type`
- `::column CSS pseudo-element`
- `column-count CSS property`
- `column-fill CSS property`
- `column-gap CSS property`
- `column-height CSS property`
- `column-rule CSS property`
- `column-rule-color CSS property`
- `column-rule-style CSS property`
- `column-rule-width CSS property`
- `column-span CSS property`
- `column-width CSS property`
- `column-wrap CSS property`
- `columns CSS property`
- `conic-gradient() CSS function`
- `contain CSS property`
- `contain-intrinsic-block-size CSS property`
- `contain-intrinsic-height CSS property`
- `contain-intrinsic-inline-size CSS property`
- `contain-intrinsic-size CSS property`
- `contain-intrinsic-width CSS property`
- `@container CSS at-rule`
- `container CSS property`
- `container-name CSS property`
- `container-type CSS property`
- `content CSS property`
- `<content-distribution> CSS type`
- `<content-position> CSS type`
- `content-visibility CSS property`
- `contrast() CSS function`
- `contrast-color() CSS function`
- `corner-block-end-shape CSS property`
- `corner-block-start-shape CSS property`
- `corner-bottom-left-shape CSS property`
- `corner-bottom-right-shape CSS property`
- `corner-bottom-shape CSS property`
- `corner-end-end-shape CSS property`
- `corner-end-start-shape CSS property`
- `corner-inline-end-shape CSS property`
- `corner-inline-start-shape CSS property`
- `corner-left-shape CSS property`
- `corner-right-shape CSS property`
- `corner-shape CSS property`
- `<corner-shape-value> CSS type`
- `corner-start-end-shape CSS property`
- `corner-start-start-shape CSS property`
- `corner-top-left-shape CSS property`
- `corner-top-right-shape CSS property`
- `corner-top-shape CSS property`
- `cos() CSS function`
- `counter() CSS function`
- `counter-increment CSS property`
- `counter-reset CSS property`
- `counter-set CSS property`
- `@counter-style CSS at-rule`
- `counters() CSS function`
- `cross-fade() CSS function`
- `cubic-bezier() CSS function`
- `::cue CSS pseudo-element`
- `:current CSS pseudo-class`
- `cursor CSS property`
- `<custom-ident> CSS type`
- `@custom-media CSS at-rule`
- `cx CSS property`
- `cy CSS property`

### D

- `d CSS property`
- `<dashed-function> CSS type`
- `<dashed-ident> CSS type`
- `:default CSS pseudo-class`
- `:defined CSS pseudo-class`
- `descent-override CSS at-rule descriptor (@font-face)`
- `::details-content CSS pseudo-element`
- `device-cmyk() CSS function`
- `<dimension> CSS type`
- `:dir() CSS pseudo-class`
- `direction CSS property`
- `:disabled CSS pseudo-class`
- `display CSS property`
- `<display-box> CSS type`
- `<display-inside> CSS type`
- `<display-internal> CSS type`
- `<display-legacy> CSS type`
- `<display-listitem> CSS type`
- `<display-outside> CSS type`
- `dominant-baseline CSS property`
- `drop-shadow() CSS function`
- `dynamic-range-limit CSS property`
- `dynamic-range-limit-mix() CSS function`

### E

- `<easing-function> CSS type`
- `element() CSS function`
- `ellipse() CSS function`
- `:empty CSS pseudo-class`
- `empty-cells CSS property`
- `:enabled CSS pseudo-class`
- `env() CSS function`
- `exp() CSS function`

### F

- `fallback CSS at-rule descriptor (@counter-style)`
- `field-sizing CSS property`
- `::file-selector-button CSS pseudo-element`
- `fill CSS property`
- `fill-opacity CSS property`
- `fill-rule CSS property`
- `filter CSS property`
- `<filter-function> CSS type`
- `:first CSS pseudo-class`
- `:first-child CSS pseudo-class`
- `::first-letter CSS pseudo-element`
- `::first-line CSS pseudo-element`
- `:first-of-type CSS pseudo-class`
- `fit-content CSS keyword`
- `fit-content() CSS function`
- `flex CSS property`
- `flex-basis CSS property`
- `flex-direction CSS property`
- `flex-flow CSS property`
- `flex-grow CSS property`
- `flex-shrink CSS property`
- `flex-wrap CSS property`
- `<flex> CSS type`
- `float CSS property`
- `flood-color CSS property`
- `flood-opacity CSS property`
- `:focus CSS pseudo-class`
- `:focus-visible CSS pseudo-class`
- `:focus-within CSS pseudo-class`
- `font CSS property`
- `font-display CSS at-rule descriptor (@font-face)`
- `font-display CSS at-rule descriptor (@font-feature-values)`
- `@font-face CSS at-rule`
- `font-family CSS at-rule descriptor (@font-face)`
- `font-family CSS at-rule descriptor (@font-palette-values)`
- `font-family CSS property`
- `font-feature-settings CSS at-rule descriptor (@font-face)`
- `font-feature-settings CSS property`
- `@font-feature-values CSS at-rule`
- `font-kerning CSS property`
- `font-language-override CSS property`
- `font-optical-sizing CSS property`
- `font-palette CSS property`
- `@font-palette-values CSS at-rule`
- `font-size CSS property`
- `font-size-adjust CSS property`
- `font-stretch CSS at-rule descriptor (@font-face)`
- `font-stretch CSS property`
- `font-style CSS at-rule descriptor (@font-face)`
- `font-style CSS property`
- `font-synthesis CSS property`
- `font-synthesis-position CSS property`
- `font-synthesis-small-caps CSS property`
- `font-synthesis-style CSS property`
- `font-synthesis-weight CSS property`
- `font-variant CSS property`
- `font-variant-alternates CSS property`
- `font-variant-caps CSS property`
- `font-variant-east-asian CSS property`
- `font-variant-emoji CSS property`
- `font-variant-ligatures CSS property`
- `font-variant-numeric CSS property`
- `font-variant-position CSS property`
- `font-variation-settings CSS at-rule descriptor (@font-face)`
- `font-variation-settings CSS property`
- `font-weight CSS at-rule descriptor (@font-face)`
- `font-weight CSS property`
- `font-width CSS at-rule descriptor (@font-face)`
- `font-width CSS property`
- `forced-color-adjust CSS property`
- `<frequency-percentage> CSS type`
- `<frequency> CSS type`
- `:fullscreen CSS pseudo-class`
- `@function CSS at-rule`
- `:future CSS pseudo-class`

### G

- `gap CSS property`
- `<generic-family> CSS type`
- `<gradient> CSS type`
- `::grammar-error CSS pseudo-element`
- `grayscale() CSS function`
- `grid CSS property`
- `grid-area CSS property`
- `grid-auto-columns CSS property`
- `grid-auto-flow CSS property`
- `grid-auto-rows CSS property`
- `grid-column CSS property`
- `grid-column-end CSS property`
- `grid-column-start CSS property`
- `grid-row CSS property`
- `grid-row-end CSS property`
- `grid-row-start CSS property`
- `grid-template CSS property`
- `grid-template-areas CSS property`
- `grid-template-columns CSS property`
- `grid-template-rows CSS property`

### H

- `hanging-punctuation CSS property`
- `:has() CSS pseudo-class`
- `:has-slotted CSS pseudo-class`
- `:heading CSS pseudo-class`
- `:heading() CSS pseudo-class`
- `height CSS property`
- `<hex-color> CSS type`
- `::highlight() CSS pseudo-element`
- `:host CSS pseudo-class`
- `:host() CSS pseudo-class`
- `:hover CSS pseudo-class`
- `hsl() CSS function`
- `<hue-interpolation-method> CSS type`
- `hue-rotate() CSS function`
- `<hue> CSS type`
- `hwb() CSS function`
- `hyphenate-character CSS property`
- `hyphenate-limit-chars CSS property`
- `hyphens CSS property`
- `hypot() CSS function`

### I

- `ID selectors`
- `<ident> CSS type`
- `if() CSS function`
- `image() CSS function`
- `image-orientation CSS property`
- `image-rendering CSS property`
- `image-resolution CSS property`
- `image-set() CSS function`
- `<image> CSS type`
- `@import CSS at-rule`
- `!important CSS keyword`
- `:in-range CSS pseudo-class`
- `:indeterminate CSS pseudo-class`
- `inherit CSS keyword`
- `inherits CSS at-rule descriptor (@property)`
- `initial CSS keyword`
- `initial-letter CSS property`
- `initial-value CSS at-rule descriptor (@property)`
- `inline-size CSS property`
- `inset CSS property`
- `inset() CSS function`
- `inset-block CSS property`
- `inset-block-end CSS property`
- `inset-block-start CSS property`
- `inset-inline CSS property`
- `inset-inline-end CSS property`
- `inset-inline-start CSS property`
- `<integer> CSS type`
- `interactivity CSS property`
- `interest-delay CSS property`
- `interest-delay-end CSS property`
- `interest-delay-start CSS property`
- `:interest-source CSS pseudo-class`
- `:interest-target CSS pseudo-class`
- `interpolate-size CSS property`
- `:invalid CSS pseudo-class`
- `invert() CSS function`
- `:is() CSS pseudo-class`
- `isolation CSS property`

### J

- `justify-content CSS property`
- `justify-items CSS property`
- `justify-self CSS property`

### K

- `Keyframe selectors`
- `@keyframes CSS at-rule`

### L

- `lab() CSS function`
- `:lang() CSS pseudo-class`
- `:last-child CSS pseudo-class`
- `:last-of-type CSS pseudo-class`
- `@layer CSS at-rule`
- `layer() CSS function`
- `lch() CSS function`
- `left CSS property`
- `:left CSS pseudo-class`
- `<length-percentage> CSS type`
- `<length> CSS type`
- `letter-spacing CSS property`
- `light-dark() CSS function`
- `lighting-color CSS property`
- `line-break CSS property`
- `line-clamp CSS property`
- `line-gap-override CSS at-rule descriptor (@font-face)`
- `line-height CSS property`
- `line-height-step CSS property`
- `<line-style> CSS type`
- `linear() CSS function`
- `linear-gradient() CSS function`
- `:link CSS pseudo-class`
- `list-style CSS property`
- `list-style-image CSS property`
- `list-style-position CSS property`
- `list-style-type CSS property`
- `:local-link CSS pseudo-class`
- `log() CSS function`

### M

- `margin CSS property`
- `margin-block CSS property`
- `margin-block-end CSS property`
- `margin-block-start CSS property`
- `margin-bottom CSS property`
- `margin-inline CSS property`
- `margin-inline-end CSS property`
- `margin-inline-start CSS property`
- `margin-left CSS property`
- `margin-right CSS property`
- `margin-top CSS property`
- `margin-trim CSS property`
- `marker CSS property`
- `::marker CSS pseudo-element`
- `marker-end CSS property`
- `marker-mid CSS property`
- `marker-start CSS property`
- `mask CSS property`
- `mask-border CSS property`
- `mask-border-mode CSS property`
- `mask-border-outset CSS property`
- `mask-border-repeat CSS property`
- `mask-border-slice CSS property`
- `mask-border-source CSS property`
- `mask-border-width CSS property`
- `mask-clip CSS property`
- `mask-composite CSS property`
- `mask-image CSS property`
- `mask-mode CSS property`
- `mask-origin CSS property`
- `mask-position CSS property`
- `mask-repeat CSS property`
- `mask-size CSS property`
- `mask-type CSS property`
- `math-depth CSS property`
- `math-shift CSS property`
- `math-style CSS property`
- `matrix() CSS function`
- `matrix3d() CSS function`
- `max() CSS function`
- `max-block-size CSS property`
- `max-content CSS keyword`
- `max-height CSS property`
- `max-inline-size CSS property`
- `max-width CSS property`
- `@media CSS at-rule`
- `min() CSS function`
- `min-block-size CSS property`
- `min-content CSS keyword`
- `min-height CSS property`
- `min-inline-size CSS property`
- `min-width CSS property`
- `minmax() CSS function`
- `mix-blend-mode CSS property`
- `mod() CSS function`
- `:modal CSS pseudo-class`
- `:muted CSS pseudo-class`

### N

- `Namespace separator`
- `<named-color> CSS type`
- `@namespace CSS at-rule`
- `negative CSS at-rule descriptor (@counter-style)`
- `& nesting selector`
- `:not() CSS pseudo-class`
- `:nth-child() CSS pseudo-class`
- `:nth-last-child() CSS pseudo-class`
- `:nth-last-of-type() CSS pseudo-class`
- `:nth-of-type() CSS pseudo-class`
- `<number> CSS type`

### O

- `object-fit CSS property`
- `object-position CSS property`
- `object-view-box CSS property`
- `offset CSS property`
- `offset-anchor CSS property`
- `offset-distance CSS property`
- `offset-path CSS property`
- `offset-position CSS property`
- `offset-rotate CSS property`
- `oklab() CSS function`
- `oklch() CSS function`
- `:only-child CSS pseudo-class`
- `:only-of-type CSS pseudo-class`
- `opacity CSS property`
- `opacity() CSS function`
- `:open CSS pseudo-class`
- `:optional CSS pseudo-class`
- `order CSS property`
- `orphans CSS property`
- `:out-of-range CSS pseudo-class`
- `outline CSS property`
- `outline-color CSS property`
- `outline-offset CSS property`
- `outline-style CSS property`
- `outline-width CSS property`
- `overflow CSS property`
- `overflow-anchor CSS property`
- `overflow-block CSS property`
- `overflow-clip-margin CSS property`
- `overflow-inline CSS property`
- `<overflow-position> CSS type`
- `overflow-wrap CSS property`
- `overflow-x CSS property`
- `overflow-y CSS property`
- `<overflow> CSS type`
- `overlay CSS property`
- `override-colors CSS at-rule descriptor (@font-palette-values)`
- `overscroll-behavior CSS property`
- `overscroll-behavior-block CSS property`
- `overscroll-behavior-inline CSS property`
- `overscroll-behavior-x CSS property`
- `overscroll-behavior-y CSS property`

### P

- `pad CSS at-rule descriptor (@counter-style)`
- `padding CSS property`
- `padding-block CSS property`
- `padding-block-end CSS property`
- `padding-block-start CSS property`
- `padding-bottom CSS property`
- `padding-inline CSS property`
- `padding-inline-end CSS property`
- `padding-inline-start CSS property`
- `padding-left CSS property`
- `padding-right CSS property`
- `padding-top CSS property`
- `@page CSS at-rule`
- `page CSS property`
- `page-orientation CSS at-rule descriptor (@page)`
- `paint() CSS function`
- `paint-order CSS property`
- `palette-mix() CSS function`
- `::part() CSS pseudo-element`
- `:past CSS pseudo-class`
- `path() CSS function`
- `:paused CSS pseudo-class`
- `<percentage> CSS type`
- `perspective CSS property`
- `perspective() CSS function`
- `perspective-origin CSS property`
- `::picker() CSS pseudo-element`
- `::picker-icon CSS pseudo-element`
- `:picture-in-picture CSS pseudo-class`
- `place-content CSS property`
- `place-items CSS property`
- `place-self CSS property`
- `::placeholder CSS pseudo-element`
- `:placeholder-shown CSS pseudo-class`
- `:playing CSS pseudo-class`
- `pointer-events CSS property`
- `polygon() CSS function`
- `:popover-open CSS pseudo-class`
- `position CSS property`
- `position-anchor CSS property`
- `position-area CSS property`
- `<position-area> CSS type`
- `@position-try CSS at-rule`
- `position-try CSS property`
- `position-try-fallbacks CSS property`
- `position-try-order CSS property`
- `position-visibility CSS property`
- `<position> CSS type`
- `pow() CSS function`
- `prefix CSS at-rule descriptor (@counter-style)`
- `print-color-adjust CSS property`
- `progress() CSS function`
- `@property CSS at-rule`

### Q

- `quotes CSS property`

### R

- `r CSS property`
- `radial-gradient() CSS function`
- `random() CSS function`
- `range CSS at-rule descriptor (@counter-style)`
- `<ratio> CSS type`
- `ray() CSS function`
- `:read-only CSS pseudo-class`
- `:read-write CSS pseudo-class`
- `reading-flow CSS property`
- `reading-order CSS property`
- `rect() CSS function`
- `<relative-size> CSS type`
- `rem() CSS function`
- `repeat() CSS function`
- `repeating-conic-gradient() CSS function`
- `repeating-linear-gradient() CSS function`
- `repeating-radial-gradient() CSS function`
- `:required CSS pseudo-class`
- `resize CSS property`
- `<resolution> CSS type`
- `revert CSS keyword`
- `revert-layer CSS keyword`
- `revert-rule`
- `rgb() CSS function`
- `right CSS property`
- `:right CSS pseudo-class`
- `:root CSS pseudo-class`
- `rotate CSS property`
- `rotate() CSS function`
- `rotate3d() CSS function`
- `rotateX() CSS function`
- `rotateY() CSS function`
- `rotateZ() CSS function`
- `round() CSS function`
- `row-gap CSS property`
- `ruby-align CSS property`
- `ruby-overhang CSS property`
- `ruby-position CSS property`
- `<rule-list> CSS type`
- `rx CSS property`
- `ry CSS property`

### S

- `Selector list`
- `saturate() CSS function`
- `scale CSS property`
- `scale() CSS function`
- `scale3d() CSS function`
- `scaleX() CSS function`
- `scaleY() CSS function`
- `scaleZ() CSS function`
- `@scope CSS at-rule`
- `:scope CSS pseudo-class`
- `scroll() CSS function`
- `scroll-behavior CSS property`
- `::scroll-button() CSS pseudo-element`
- `scroll-initial-target CSS property`
- `scroll-margin CSS property`
- `scroll-margin-block CSS property`
- `scroll-margin-block-end CSS property`
- `scroll-margin-block-start CSS property`
- `scroll-margin-bottom CSS property`
- `scroll-margin-inline CSS property`
- `scroll-margin-inline-end CSS property`
- `scroll-margin-inline-start CSS property`
- `scroll-margin-left CSS property`
- `scroll-margin-right CSS property`
- `scroll-margin-top CSS property`
- `::scroll-marker CSS pseudo-element`
- `scroll-marker-group CSS property`
- `::scroll-marker-group CSS pseudo-element`
- `scroll-padding CSS property`
- `scroll-padding-block CSS property`
- `scroll-padding-block-end CSS property`
- `scroll-padding-block-start CSS property`
- `scroll-padding-bottom CSS property`
- `scroll-padding-inline CSS property`
- `scroll-padding-inline-end CSS property`
- `scroll-padding-inline-start CSS property`
- `scroll-padding-left CSS property`
- `scroll-padding-right CSS property`
- `scroll-padding-top CSS property`
- `scroll-snap-align CSS property`
- `scroll-snap-stop CSS property`
- `scroll-snap-type CSS property`
- `scroll-target-group CSS property`
- `scroll-timeline CSS property`
- `scroll-timeline-axis CSS property`
- `scroll-timeline-name CSS property`
- `scrollbar-color CSS property`
- `scrollbar-gutter CSS property`
- `scrollbar-width CSS property`
- `::search-text CSS pseudo-element`
- `:seeking CSS pseudo-class`
- `::selection CSS pseudo-element`
- `<self-position> CSS type`
- `sepia() CSS function`
- `shape() CSS function`
- `shape-image-threshold CSS property`
- `shape-margin CSS property`
- `shape-outside CSS property`
- `shape-rendering CSS property`
- `sibling-count() CSS function`
- `sibling-index() CSS function`
- `sign() CSS function`
- `sin() CSS function`
- `size CSS at-rule descriptor (@page)`
- `size-adjust CSS at-rule descriptor (@font-face)`
- `skew() CSS function`
- `skewX() CSS function`
- `skewY() CSS function`
- `::slotted() CSS pseudo-element`
- `speak-as CSS at-rule descriptor (@counter-style)`
- `speak-as CSS property`
- `::spelling-error CSS pseudo-element`
- `sqrt() CSS function`
- `src CSS at-rule descriptor (@font-face)`
- `:stalled CSS pseudo-class`
- `@starting-style CSS at-rule`
- `:state() CSS pseudo-class`
- `steps() CSS function`
- `stop-color CSS property`
- `stop-opacity CSS property`
- `<string> CSS type`
- `stroke CSS property`
- `stroke-dasharray CSS property`
- `stroke-dashoffset CSS property`
- `stroke-linecap CSS property`
- `stroke-linejoin CSS property`
- `stroke-miterlimit CSS property`
- `stroke-opacity CSS property`
- `stroke-width CSS property`
- `suffix CSS at-rule descriptor (@counter-style)`
- `superellipse() CSS function`
- `@supports CSS at-rule`
- `symbols CSS at-rule descriptor (@counter-style)`
- `symbols() CSS function`
- `syntax CSS at-rule descriptor (@property)`
- `system CSS at-rule descriptor (@counter-style)`
- `<system-color> CSS type`

### T

- `Type selectors`
- `tab-size CSS property`
- `table-layout CSS property`
- `tan() CSS function`
- `:target CSS pseudo-class`
- `:target-after CSS pseudo-class`
- `:target-before CSS pseudo-class`
- `:target-current CSS pseudo-class`
- `::target-text CSS pseudo-element`
- `text-align CSS property`
- `text-align-last CSS property`
- `text-anchor CSS property`
- `text-autospace CSS property`
- `text-box CSS property`
- `text-box-edge CSS property`
- `text-box-trim CSS property`
- `text-combine-upright CSS property`
- `text-decoration CSS property`
- `text-decoration-color CSS property`
- `text-decoration-inset CSS property`
- `text-decoration-line CSS property`
- `text-decoration-skip-ink CSS property`
- `text-decoration-style CSS property`
- `text-decoration-thickness CSS property`
- `<text-edge> CSS type`
- `text-emphasis CSS property`
- `text-emphasis-color CSS property`
- `text-emphasis-position CSS property`
- `text-emphasis-style CSS property`
- `text-indent CSS property`
- `text-justify CSS property`
- `text-orientation CSS property`
- `text-overflow CSS property`
- `text-rendering CSS property`
- `text-shadow CSS property`
- `text-size-adjust CSS property`
- `text-spacing-trim CSS property`
- `text-transform CSS property`
- `text-underline-offset CSS property`
- `text-underline-position CSS property`
- `text-wrap CSS property`
- `text-wrap-mode CSS property`
- `text-wrap-style CSS property`
- `<time-percentage> CSS type`
- `<time> CSS type`
- `<timeline-range-name> CSS type`
- `timeline-scope CSS property`
- `top CSS property`
- `touch-action CSS property`
- `transform CSS property`
- `transform-box CSS property`
- `<transform-function> CSS type`
- `transform-origin CSS property`
- `transform-style CSS property`
- `transition CSS property`
- `transition-behavior CSS property`
- `transition-delay CSS property`
- `transition-duration CSS property`
- `transition-property CSS property`
- `transition-timing-function CSS property`
- `translate CSS property`
- `translate() CSS function`
- `translate3d() CSS function`
- `translateX() CSS function`
- `translateY() CSS function`
- `translateZ() CSS function`
- `type() CSS function`

### U

- `Universal selectors`
- `unicode-bidi CSS property`
- `unicode-range CSS at-rule descriptor (@font-face)`
- `unset CSS keyword`
- `url() CSS function`
- `<url> CSS type`
- `:user-invalid CSS pseudo-class`
- `user-select CSS property`
- `:user-valid CSS pseudo-class`

### V

- `:valid CSS pseudo-class`
- `var() CSS function`
- `vector-effect CSS property`
- `vertical-align CSS property`
- `view() CSS function`
- `view-timeline CSS property`
- `view-timeline-axis CSS property`
- `view-timeline-inset CSS property`
- `view-timeline-name CSS property`
- `@view-transition CSS at-rule`
- `::view-transition CSS pseudo-element`
- `view-transition-class CSS property`
- `::view-transition-group() CSS pseudo-element`
- `::view-transition-image-pair() CSS pseudo-element`
- `view-transition-name CSS property`
- `::view-transition-new() CSS pseudo-element`
- `::view-transition-old() CSS pseudo-element`
- `view-transition-scope CSS property`
- `visibility CSS property`
- `:visited CSS pseudo-class`
- `:volume-locked CSS pseudo-class`

### W

- `:where() CSS pseudo-class`
- `white-space CSS property`
- `white-space-collapse CSS property`
- `widows CSS property`
- `width CSS property`
- `will-change CSS property`
- `word-break CSS property`
- `word-spacing CSS property`
- `writing-mode CSS property`

### X

- `x CSS property`
- `:xr-overlay CSS pseudo-class`
- `xywh() CSS function`

### Y

- `y CSS property`

### Z

- `z-index CSS property`
- `zoom CSS property`

## Selectors

The following are the various selectors, which allow styles to be conditional based on various features of elements within the DOM.

### Basic selectors

**Basic selectors** are fundamental selectors; these are the most basic selectors that are frequently combined to create other, more complex selectors.

- Universal selector `*`
- Type selector `elementname`
- Class selector `.classname`
- ID selector `#idname`
- Attribute selector `[attr=value]`

### Grouping selectors

**Selector list `A, B`**

Specifies that both `A` and `B` elements are selected. This is a grouping method to select several matching elements.

### Combinators

Combinators are selectors that establish a relationship between two or more simple selectors, such as "`A` is a child of `B`" or "`A` is adjacent to `B`", creating a complex selector.

**Next-sibling combinator `A + B`**

Specifies that the elements selected by both `A` and `B` have the same parent and that the element selected by `B` immediately follows the element selected by `A` horizontally.

**Subsequent-sibling combinator `A ~ B`**

Specifies that the elements selected by both `A` and `B` share the same parent and that the element selected by `A` comes before—but not necessarily immediately before—the element selected by `B`.

**Child combinator `A > B`**

Specifies that the element selected by `B` is the direct child of the element selected by `A`.

**Descendant combinator `A B`**

Specifies that the element selected by `B` is a descendant of the element selected by `A`, but is not necessarily a direct child.

**Column combinator `A || B`**

Specifies that the element selected by `B` is located within the table column specified by `A`. Elements which span multiple columns are considered to be a member of all of those columns.

### Pseudo

**Pseudo classes `:`**

Specifies a special state of the selected element(s).

**Pseudo elements `::`**

Represents entities that are not included in HTML.

See also selectors in the Selectors specification and the pseudo-element specification.

## Concepts

### Syntax and semantics

- CSS syntax
- At-rules
- Cascade
- Comments
- Descriptor
- Inheritance
- Shorthand properties
- Specificity
- Values
- Value definition syntax
- CSS values and units
- CSS functional notations

### Values

- Actual value
- Computed value
- Initial value
- Resolved value
- Specified value
- Used value

### Layout

- Block formatting context
- Box model
- Containing block
- Layout mode
- Margin collapsing
- Replaced elements
- Stacking context
- Visual formatting model

## DOM-CSS / CSSOM

### Major object types

- `Document.styleSheets`
- `HTMLElement.style`
- `Element.className`
- `Element.classList`
- `StyleSheetList`
- `CSSRuleList`
- `CSSRule`
- `CSSStyleRule`
- `CSSStyleDeclaration`

### Important methods

- `CSSStyleSheet.insertRule()`
- `CSSStyleSheet.deleteRule()`
