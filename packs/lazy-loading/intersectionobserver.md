---
title: "IntersectionObserver - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver
domain: lazy-loading
license: CC-BY-SA-4.0
tags: lazy loading images, intersection observer, loading attribute, deferred asset loading
fetched: 2026-07-02
---

# IntersectionObserver

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`IntersectionObserver`** interface of the Intersection Observer API provides a way to asynchronously observe changes in the intersection of a target element with an ancestor element or with a top-level document's viewport. The ancestor element or viewport is referred to as the root.

When an `IntersectionObserver` is created, it's configured to watch for given ratios of visibility within the root. The configuration cannot be changed once the `IntersectionObserver` is created, so a given observer object is only useful for watching for specific changes in degree of visibility; however, you can watch multiple target elements with the same observer.

## Constructor

**`IntersectionObserver()`**

Creates a new `IntersectionObserver` object which will execute a specified callback function when it detects that a target element's visibility has crossed one or more thresholds.

## Instance properties

**`IntersectionObserver.delay` Read only**

An integer indicating the minimum delay between notifications from this observer.

**`IntersectionObserver.root` Read only**

The `Element` or `Document` whose bounds are used as the bounding box when testing for intersection. If no `root` value was passed to the constructor or its value is `null`, the top-level document's viewport is used.

**`IntersectionObserver.rootMargin` Read only**

An offset rectangle applied to the root's bounding box when calculating intersections, effectively shrinking or growing the root for calculation purposes. The value returned by this property may not be the same as the one specified when calling the constructor as it may be changed to match internal requirements. Each offset can be expressed in pixels (`px`) or percentages (`%`). The default is "0px 0px 0px 0px".

**`IntersectionObserver.scrollMargin` Read only**

An offset rectangle applied to each scroll container on the path from intersection root to target, effectively shrinking or growing the clip rectangles used to calculate intersections. The value returned by this property may not be the same as the one specified when calling the constructor.

**`IntersectionObserver.thresholds` Read only**

A list of thresholds, sorted in increasing numeric order, where each threshold is a ratio of intersection area to bounding box area of an observed target. Notifications for a target are generated when any of the thresholds are crossed for that target. If no value was passed to the constructor, 0 is used.

**`IntersectionObserver.trackVisibility` Read only**

A boolean indicating whether this `IntersectionObserver` is checking that the target does not have compromised visibility.

## Instance methods

**`IntersectionObserver.disconnect()`**

Stops the `IntersectionObserver` object from observing any target.

**`IntersectionObserver.observe()`**

Tells the `IntersectionObserver` a target element to observe.

**`IntersectionObserver.takeRecords()`**

Returns an array of `IntersectionObserverEntry` objects for all observed targets.

**`IntersectionObserver.unobserve()`**

Tells the `IntersectionObserver` to stop observing a particular target element.

## Examples

```js
const intersectionObserver = new IntersectionObserver((entries) => {
  // If intersectionRatio is 0, the target is out of view
  // and we do not need to do anything.
  if (entries[0].intersectionRatio <= 0) return;

  loadItems(10);
  console.log("Loaded new items");
});
// start observing
intersectionObserver.observe(document.querySelector(".scrollerFooter"));
```

## Specifications

| Specification |
|---|
| Intersection Observer # intersection-observer-interface |

## Browser compatibility
