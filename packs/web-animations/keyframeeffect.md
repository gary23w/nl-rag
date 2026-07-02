---
title: "KeyframeEffect - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/KeyframeEffect
domain: web-animations
license: CC-BY-SA-2.5
tags: web animations api, keyframe animation, css transition, animation timeline
fetched: 2026-07-02
---

# KeyframeEffect

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`KeyframeEffect`** interface of the Web Animations API lets us create sets of animatable properties and values, called **keyframes.** These can then be played using the `Animation()` constructor.

## Constructor

**`KeyframeEffect()`**

Returns a new `KeyframeEffect` object instance, and also allows you to clone an existing keyframe effect object instance.

## Instance properties

**`KeyframeEffect.target`**

Gets and sets the element, or originating element of the pseudo-element, being animated by this object. This may be `null` for animations that do not target a specific element or pseudo-element.

**`KeyframeEffect.pseudoElement`**

Gets and sets the selector of the pseudo-element being animated by this object. This may be `null` for animations that do not target a pseudo-element.

**`KeyframeEffect.iterationComposite`**

Gets and sets the iteration composite operation for resolving the property value changes of this keyframe effect.

**`KeyframeEffect.composite`**

Gets and sets the composite operation property for resolving the property value changes between this and other keyframe effects.

## Instance methods

*This interface inherits some of its methods from its parent, `AnimationEffect`.*

**`AnimationEffect.getComputedTiming()`**

Returns the calculated, current timing values for this keyframe effect.

**`KeyframeEffect.getKeyframes()`**

Returns the computed keyframes that make up this effect along with their computed keyframe offsets.

**`AnimationEffect.getTiming()`**

Returns the object associated with the animation containing all the animation's timing values.

**`KeyframeEffect.setKeyframes()`**

Replaces the set of keyframes that make up this effect.

**`AnimationEffect.updateTiming()`**

Updates the specified timing properties.

## Examples

In the following example, the KeyframeEffect constructor is used to create a set of keyframes that dictate how the rofl emoji should roll on the floor:

```js
const emoji = document.querySelector("div"); // element to animate

const rollingKeyframes = new KeyframeEffect(
  emoji,
  [
    { transform: "translateX(0) rotate(0)" }, // keyframe
    { transform: "translateX(200px) rotate(1.3turn)" }, // keyframe
  ],
  {
    // keyframe options
    duration: 2000,
    direction: "alternate",
    easing: "ease-in-out",
    iterations: "Infinity",
  },
);

const rollingAnimation = new Animation(rollingKeyframes, document.timeline);

// play rofl animation
rollingAnimation.play();
```

```html
<div>🤣</div>
```

```css
body {
  box-shadow: 0 5px 5px pink;
}

div {
  width: fit-content;
  margin-left: calc(50% - 132px);
  font-size: 64px;
  user-select: none;
  margin-top: 1rem;
}
```

## Specifications

| Specification |
|---|
| Web Animations # the-keyframeeffect-interface |

## Browser compatibility
