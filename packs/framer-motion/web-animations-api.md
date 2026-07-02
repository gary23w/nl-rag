---
title: "Web Animations API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
domain: framer-motion
license: CC-BY-SA-4.0
tags: framer motion, react animation library, declarative motion, spring gesture animation
fetched: 2026-07-02
---

# Web Animations API

The **Web Animations API** allows for synchronizing and timing changes to the presentation of a Web page, i.e., animation of DOM elements. It does so by combining two models: the Timing Model and the Animation Model.

## Concepts and usage

The Web Animations API provides a common language for browsers and developers to describe animations on DOM elements. To get more information on the concepts behind the API and how to use it, read Using the Web Animations API.

## Web Animations interfaces

**`Animation`**

Provides playback controls and a timeline for an animation node or source. Can take an object created with the `KeyframeEffect()` constructor.

**`KeyframeEffect`**

Describes sets of animatable properties and values, called **keyframes** and their timing options. These can then be played using the `Animation()` constructor.

**`AnimationTimeline`**

Represents the timeline of animation. This interface exists to define timeline features (inherited by `DocumentTimeline` and future timeline objects) and is not itself accessed by developers.

**`AnimationEvent`**

Part of the CSS Animations module, capturing the animation name and elapsed time.

**`DocumentTimeline`**

Represents animation timelines, including the default document timeline (accessed using the `Document.timeline` property).

## Extensions to other interfaces

The Web Animations API adds features to `document` and `element`.

### Extensions to the `Document` interface

**`document.timeline`**

The `DocumentTimeline` object representing the default document timeline.

**`document.getAnimations()`**

Returns an Array of `Animation` objects currently in effect on elements in the `document`.

### Extensions to the `Element` interface

**`Element.animate()`**

A shortcut method for creating and playing an animation on an element. It returns the created `Animation` object instance.

**`Element.getAnimations()`**

Returns an Array of `Animation` objects currently affecting an element or which are scheduled to do so in the future.

## Specifications

| Specification |
|---|
| Web Animations |
