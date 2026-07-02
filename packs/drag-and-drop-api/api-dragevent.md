---
title: "DragEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/DragEvent
domain: drag-and-drop-api
license: CC-BY-SA-4.0
tags: html drag and drop, data transfer object, draggable attribute element, drop target zone
fetched: 2026-07-02
---

# DragEvent

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

- Learn more
- See full compatibility

The **`DragEvent`** interface is a DOM event that represents a drag and drop interaction. The user initiates a drag by placing a pointer device (such as a mouse) on the touch surface and then dragging the pointer to a new location (such as another DOM element). Applications are free to interpret a drag and drop interaction in an application-specific way.

This interface inherits properties from `MouseEvent` and `Event`.

## Instance properties

**`DragEvent.dataTransfer` Read only**

The data that is transferred during a drag and drop interaction.

## Constructors

Although this interface has a constructor, it is not possible to create a useful DataTransfer object from script, since `DataTransfer` objects have a processing and security model that is coordinated by the browser during drag-and-drops.

**`DragEvent()`**

Creates a synthetic and untrusted DragEvent.

## Event types

**`drag`**

This event is fired when an element or text selection is being dragged.

**`dragend`**

This event is fired when a drag operation is being ended (by releasing a mouse button or hitting the escape key).

**`dragenter`**

This event is fired when a dragged element or text selection enters a valid drop target.

**`dragleave`**

This event is fired when a dragged element or text selection leaves a valid drop target.

**`dragover`**

This event is fired continuously when an element or text selection is being dragged and the mouse pointer is over a valid drop target (every 50 ms WHEN mouse is not moving ELSE much faster between 5 ms (slow movement) and 1ms (fast movement) approximately. This firing pattern is different than `mouseover` ).

**`dragstart`**

This event is fired when the user starts dragging an element or text selection.

**`drop`**

This event is fired when an element or text selection is dropped on a valid drop target.

## Example

An Example of each property, constructor, event type and global event handlers is included in their respective reference page.

## Specifications

| Specification |
|---|
| HTML # the-dragevent-interface |

## Browser compatibility
