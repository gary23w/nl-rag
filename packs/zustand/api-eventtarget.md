---
title: "EventTarget - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget
domain: zustand
license: CC-BY-SA-4.0
tags: zustand store, hook-based state, minimal state management, zustand selector
fetched: 2026-07-02
---

# EventTarget

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`EventTarget`** interface is implemented by objects that can receive events and may have listeners for them. In other words, any target of events implements the three methods associated with this interface.

`Element`, and its children, as well as `Document` and `Window`, are the most common event targets, but other objects can be event targets, too. For example `IDBRequest`, `AudioNode`, and `AudioContext` are also event targets.

Many event targets (including elements, documents, and windows) also support registering event handlers via `onevent` properties and attributes.

## Constructor

**`EventTarget()`**

Creates a new `EventTarget` object instance.

## Instance methods

**`EventTarget.addEventListener()`**

Registers an event handler of a specific event type on the `EventTarget`.

**`EventTarget.removeEventListener()`**

Removes an event listener from the `EventTarget`.

**`EventTarget.dispatchEvent()`**

Dispatches an event to this `EventTarget`.

## Specifications

| Specification |
|---|
| DOM # interface-eventtarget |

## Browser compatibility
