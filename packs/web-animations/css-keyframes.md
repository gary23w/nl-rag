---
title: "@keyframes CSS at-rule - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes
domain: web-animations
license: CC-BY-SA-2.5
tags: web animations api, keyframe animation, css transition, animation timeline
fetched: 2026-07-02
---

# `@keyframes` CSS at-rule

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`@keyframes`** CSS at-rule controls the intermediate steps in a CSS animation sequence by defining styles for keyframes (or waypoints) along the animation sequence. This gives more control over the intermediate steps of the animation sequence than transitions.

## Syntax

```css
@keyframes slide-in {
  from {
    transform: translateX(0%);
  }

  to {
    transform: translateX(100%);
  }
}
```

### Values

**`<keyframes-name>`**

A case-sensitive `<custom-ident>` or string naming the keyframe list.

**`from`**

Equivalent to the value `0%`.

**`to`**

Equivalent to the value `100%`.

**`<percentage>`**

A percentage through the animation sequence at which the specified keyframe should occur.

**`<timeline-range-name>` `<percentage>`**

A percentage through the specified `animation-range` at which the specified keyframe should occur.

## Description

To use keyframes, create a `@keyframes` rule with a name that is then used by the `animation-name` property to match an animation to its keyframe declaration. Each `@keyframes` rule contains a style list of keyframe selectors, which specify percentages along the animation when the keyframe occurs, and a block containing the styles for that keyframe.

You can list the keyframe percentages in any order; they will be handled in the order they should occur.

JavaScript can access the `@keyframes` at-rule with the CSS object model interface `CSSKeyframesRule`.

### Valid keyframe lists

If a keyframe rule doesn't specify the start or end states of the animation (that is, `0%`/`from` and `100%`/`to`), browsers will use the element's existing styles for the start/end states. This can be used to animate an element from its initial state and back.

Properties that can't be animated in keyframe rules are ignored, but supported properties will still be animated.

### Resolving duplicates

If multiple keyframe sets exist for a given name, the last one encountered by the parser is used. `@keyframes` rules don't cascade, so animations never derive keyframes from more than one rule set.

If a given animation time offset is duplicated, all keyframes in the `@keyframes` rule for that percentage are used for that frame. There is cascading within a `@keyframes` rule if multiple keyframes specify the same percentage values.

### When properties are left out of some keyframes

Properties that aren't specified in every keyframe are interpolated if possible — properties that can't be interpolated are dropped from the animation. For example:

```css
@keyframes identifier {
  0% {
    top: 0;
    left: 0;
  }
  30% {
    top: 50px;
  }
  68%,
  72% {
    left: 50px;
  }
  100% {
    top: 100px;
    left: 100%;
  }
}
```

Here, the `top` property animates using the `0%`, `30%`, and `100%` keyframes, and `left` animates using the `0%`, `68%`, `72%` and `100%` keyframes.

### When a keyframe is defined multiple times

If a keyframe is defined multiple times but not all affected properties are in each keyframe, all values specified in these keyframes are considered. For example:

```css
@keyframes identifier {
  0% {
    top: 0;
  }
  50% {
    top: 30px;
    left: 20px;
  }
  50% {
    top: 10px;
  }
  100% {
    top: 0;
  }
}
```

In this example, at the `50%` keyframe, the values used are `top: 10px` and `left: 20px`.

### `!important` in a keyframe

Declarations in a keyframe qualified with the `important` flag set are ignored.

```css
@keyframes important1 {
  0% {
    margin-top: 50px;
  }
  50% {
    margin-top: 150px !important; /* ignored */
  }
  100% {
    margin-top: 100px;
  }
}

@keyframes important2 {
  from {
    margin-top: 50px;
    margin-bottom: 100px;
  }
  to {
    margin-top: 150px !important; /* ignored */
    margin-bottom: 50px;
  }
}
```

## Formal syntax

```
@keyframes = 
  @keyframes <keyframes-name> { <qualified-rule-list> }  

<keyframes-name> = 
  <custom-ident>  |
  <string>        
```

## Examples

### CSS animation examples

See Using CSS animations and scroll-driven animations for examples.

## Specifications

| Specification |
|---|
| CSS Animations Level 1 # keyframes |

## Browser compatibility
