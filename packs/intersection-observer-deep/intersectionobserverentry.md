---
title: "IntersectionObserverEntry - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry
domain: intersection-observer-deep
license: CC-BY-SA-4.0
tags: intersection observer internals, root margin threshold, intersection ratio callback, viewport visibility tracking
fetched: 2026-07-02
---

# IntersectionObserverEntry

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`IntersectionObserverEntry`** interface of the Intersection Observer API describes the intersection between the target element and its root container at a specific moment of transition.

Instances of `IntersectionObserverEntry` are delivered to an `IntersectionObserver` callback in its `entries` parameter; otherwise, these objects can only be obtained by calling `IntersectionObserver.takeRecords()`.

## Constructor

**`IntersectionObserverEntry()`**

Creates a new `IntersectionObserverEntry` object.

## Instance properties

**`IntersectionObserverEntry.boundingClientRect` Read only**

Returns the bounds rectangle of the target element as a `DOMRectReadOnly`. The bounds are computed as described in the documentation for `Element.getBoundingClientRect()`.

**`IntersectionObserverEntry.intersectionRatio` Read only**

Returns the ratio of the `intersectionRect` to the `boundingClientRect`.

**`IntersectionObserverEntry.intersectionRect` Read only**

Returns a `DOMRectReadOnly` representing the target's visible area.

**`IntersectionObserverEntry.isIntersecting` Read only**

A Boolean value which is `true` if the target element intersects with the intersection observer's root. If this is `true`, then, the `IntersectionObserverEntry` describes a transition into a state of intersection; if it's `false`, then you know the transition is from intersecting to not-intersecting.

**`IntersectionObserverEntry.rootBounds` Read only**

Returns a `DOMRectReadOnly` for the intersection observer's root.

**`IntersectionObserverEntry.target` Read only**

The `Element` whose intersection with the root changed.

**`IntersectionObserverEntry.time` Read only**

A `DOMHighResTimeStamp` indicating the time at which the intersection was recorded, relative to the `IntersectionObserver`'s time origin.

## Instance methods

*This interface has no methods.*

## Specifications

| Specification |
|---|
| Intersection Observer # intersection-observer-entry |

## Browser compatibility
