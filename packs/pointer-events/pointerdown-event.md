---
title: "Element: pointerdown event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event
domain: pointer-events
license: CC-BY-SA-4.0
tags: pointer events model, unified input pointer, pointer capture target, primary pointer detection
fetched: 2026-07-02
---

# Element: pointerdown event

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

- Learn more
- See full compatibility

The `pointerdown` event is fired when a pointer becomes active. For mouse, it is fired when the device transitions from no buttons pressed to at least one button pressed. For touch, it is fired when physical contact is made with the digitizer. For pen, it is fired when the stylus makes physical contact with the digitizer.

This behavior is different from `mousedown` events. When using a physical mouse, `mousedown` events fire whenever any button on a mouse is pressed down. `pointerdown` events fire only upon the first button press; subsequent button presses don't fire `pointerdown` events.

**Note:** For touchscreen browsers that allow direct manipulation, a `pointerdown` event triggers implicit pointer capture, which causes the target to capture all subsequent pointer events as if they were occurring over the capturing target. Accordingly, `pointerover`, `pointerenter`, `pointerleave`, and `pointerout` **will not fire** as long as this capture is set. The capture can be released manually by calling `element.releasePointerCapture` on the target element, or it will be implicitly released after a `pointerup` or `pointercancel` event.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("pointerdown", (event) => { })

onpointerdown = (event) => { }
```

## Event type

A `PointerEvent`. Inherits from `Event`.

## Event properties

*This interface inherits properties from `MouseEvent` and `Event`.*

**`PointerEvent.altitudeAngle` Read only**

Represents the angle between a transducer (a pointer or stylus) axis and the X-Y plane of a device screen.

**`PointerEvent.azimuthAngle` Read only**

Represents the angle between the Y-Z plane and the plane containing both the transducer (a pointer or stylus) axis and the Y axis.

**`PointerEvent.persistentDeviceId` Read only**

A unique identifier for the pointing device generating the `PointerEvent`.

**`PointerEvent.pointerId` Read only**

A unique identifier for the pointer causing the event.

**`PointerEvent.width` Read only**

The width (magnitude on the X axis), in CSS pixels, of the contact geometry of the pointer.

**`PointerEvent.height` Read only**

The height (magnitude on the Y axis), in CSS pixels, of the contact geometry of the pointer.

**`PointerEvent.pressure` Read only**

The normalized pressure of the pointer input in the range `0` to `1`, where `0` and `1` represent the minimum and maximum pressure the hardware is capable of detecting, respectively.

**`PointerEvent.tangentialPressure` Read only**

The normalized tangential pressure of the pointer input (also known as barrel pressure or cylinder stress) in the range `-1` to `1`, where `0` is the neutral position of the control.

**`PointerEvent.tiltX` Read only**

The plane angle (in degrees, in the range of `-90` to `90`) between the Y–Z plane and the plane containing both the pointer (e.g., pen stylus) axis and the Y axis.

**`PointerEvent.tiltY` Read only**

The plane angle (in degrees, in the range of `-90` to `90`) between the X–Z plane and the plane containing both the pointer (e.g., pen stylus) axis and the X axis.

**`PointerEvent.twist` Read only**

The clockwise rotation of the pointer (e.g., pen stylus) around its major axis in degrees, with a value in the range `0` to `359`.

**`PointerEvent.pointerType` Read only**

Indicates the device type that caused the event (mouse, pen, touch, etc.).

**`PointerEvent.isPrimary` Read only**

Indicates if the pointer represents the primary pointer of this pointer type.

## Examples

Using `addEventListener()`:

```js
const para = document.querySelector("p");

para.addEventListener("pointerdown", (event) => {
  console.log("Pointer down event");
});
```

Using the `onpointerdown` event handler property:

```js
const para = document.querySelector("p");

para.onpointerdown = (event) => {
  console.log("Pointer down event");
};
```

## Specifications

| Specification |
|---|
| Pointer Events # the-pointerdown-event |
| Pointer Events # dom-globaleventhandlers-onpointerdown |

## Browser compatibility
