---
title: "Range - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Range
domain: selection-api
license: CC-BY-SA-4.0
tags: selection api, text selection range, user selected content, caret anchor focus
fetched: 2026-07-02
---

# Range

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`Range`** interface represents a fragment of a document that can contain nodes and parts of text nodes.

A range can be created by using the `Document.createRange()` method. Range objects can also be retrieved by using the `getRangeAt()` method of the `Selection` object or the `caretRangeFromPoint()` method of the `Document` object.

There also is the `Range()` constructor available.

## Constructor

**`Range()`**

Returns a `Range` object with the global `Document` as its start and end.

## Instance properties

*Also inherits properties from its parent interface, `AbstractRange`.*

**`Range.commonAncestorContainer` Read only**

Returns the deepest `Node` that contains the `startContainer` and `endContainer` nodes.

## Instance methods

*There are no inherited methods.*

**`Range.collapse()`**

Collapses the `Range` to one of its boundary points.

**`Range.compareBoundaryPoints()`**

Compares the boundary points of the `Range` with another `Range`.

**`Range.compareNode()`**

Returns a constant representing whether the `Node` is before, after, inside, or surrounding the range.

**`Range.comparePoint()`**

Returns -1, 0, or 1 indicating whether the point occurs before, inside, or after the `Range`.

**`Range.cloneContents()`**

Returns a `DocumentFragment` copying the nodes of a `Range`.

**`Range.cloneRange()`**

Returns a `Range` object with boundary points identical to the cloned `Range`.

**`Range.createContextualFragment()`**

Returns a `DocumentFragment` created from a given string of code.

**`Range.deleteContents()`**

Removes the contents of a `Range` from the `Document`.

**`Range.detach()`**

Does nothing. Kept for compatibility.

**`Range.extractContents()`**

Moves contents of a `Range` from the document tree into a `DocumentFragment`.

**`Range.getBoundingClientRect()`**

Returns a `DOMRect` object which bounds the entire contents of the `Range`; this would be the union of all the rectangles returned by `range.getClientRects()`.

**`Range.getClientRects()`**

Returns a list of `DOMRect` objects that aggregates the results of `Element.getClientRects()` for all the elements in the `Range`.

**`Range.isPointInRange()`**

Returns a `boolean` indicating whether the given point is in the `Range`.

**`Range.insertNode()`**

Insert a `Node` at the start of a `Range`.

**`Range.intersectsNode()`**

Returns a `boolean` indicating whether the given node intersects the `Range`.

**`Range.selectNode()`**

Sets the `Range` to contain the `Node` and its contents.

**`Range.selectNodeContents()`**

Sets the `Range` to contain the contents of a `Node`.

**`Range.setEnd()`**

Sets the end position of a `Range`.

**`Range.setStart()`**

Sets the start position of a `Range`.

**`Range.setEndAfter()`**

Sets the end position of a `Range` relative to another `Node`.

**`Range.setEndBefore()`**

Sets the end position of a `Range` relative to another `Node`.

**`Range.setStartAfter()`**

Sets the start position of a `Range` relative to another `Node`.

**`Range.setStartBefore()`**

Sets the start position of a `Range` relative to another `Node`.

**`Range.surroundContents()`**

Moves content of a `Range` into a new `Node`.

**`Range.toString()`**

Returns the text of the `Range`.

## Specifications

| Specification |
|---|
| DOM # interface-range |
| DOM Parsing and Serialization # extensions-to-the-range-interface |
| CSSOM View Module # extensions-to-the-range-interface |

## Browser compatibility
