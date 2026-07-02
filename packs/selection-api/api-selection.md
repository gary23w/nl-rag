---
title: "Selection - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Selection
domain: selection-api
license: CC-BY-SA-4.0
tags: selection api, text selection range, user selected content, caret anchor focus
fetched: 2026-07-02
---

# Selection

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

A **`Selection`** object represents the range of text selected by the user or the current position of the caret. Each `document` is associated with a unique selection object, which can be retrieved by `document.getSelection()` or `window.getSelection()` and then be examined and modified.

A user may make a selection from left to right (in document order) or right to left (reverse of document order). The ***anchor*** is where the user began the selection and the ***focus*** is where the user ends the selection. If you make a selection with a desktop mouse, the anchor is placed where you pressed the mouse button, and the focus is placed where you released the mouse button.

**Note:** *Anchor* and *focus* should not be confused with the *start* and *end* positions of a selection. The anchor can be placed before the focus or vice versa, depending on the direction you made your selection.

## Instance properties

**`Selection.anchorNode` Read only**

Returns the `Node` in which the selection begins. Can return `null` if selection never existed in the document (e.g., an iframe that was never clicked on).

**`Selection.anchorOffset` Read only**

Returns a number representing the offset of the selection's anchor within the `anchorNode`. If `anchorNode` is a text node, this is the number of characters within anchorNode preceding the anchor. If `anchorNode` is an element, this is the number of child nodes of the `anchorNode` preceding the anchor.

**`Selection.direction` Read only**

A string describing the direction of the current selection.

**`Selection.focusNode` Read only**

Returns the `Node` in which the selection ends. Can return `null` if selection never existed in the document (e.g., an iframe that was never clicked on).

**`Selection.focusOffset` Read only**

Returns a number representing the offset of the selection's focus within the `focusNode`. If `focusNode` is a text node, this is the number of characters within `focusNode` preceding the focus. If `focusNode` is an element, this is the number of child nodes of the `focusNode` preceding the focus.

**`Selection.isCollapsed` Read only**

Returns a Boolean indicating whether the selection's start and end points are at the same position.

**`Selection.rangeCount` Read only**

Returns the number of ranges in the selection.

**`Selection.type` Read only**

Returns a string describing the type of the current selection.

## Instance methods

**`Selection.addRange()`**

A `Range` object that will be added to the selection.

**`Selection.collapse()`**

Collapses the current selection to a single point.

**`Selection.collapseToEnd()`**

Collapses the selection to the end of the last range in the selection.

**`Selection.collapseToStart()`**

Collapses the selection to the start of the first range in the selection.

**`Selection.containsNode()`**

Indicates if a certain node is part of the selection.

**`Selection.deleteFromDocument()`**

Deletes the selection's content from the document.

**`Selection.empty()`**

Removes all ranges from the selection, leaving the `anchorNode` and `focusNode` properties equal to `null` and nothing selected.

**`Selection.extend()`**

Moves the focus of the selection to a specified point.

**`Selection.getComposedRanges()`**

Returns an array of `StaticRange` objects, each that represents a selection that might cross shadow DOM boundaries.

**`Selection.getRangeAt()`**

Returns a `Range` object representing one of the ranges currently selected.

**`Selection.modify()`**

Changes the current selection.

**`Selection.removeRange()`**

Removes a range from the selection.

**`Selection.removeAllRanges()`**

Removes all ranges from the selection.

**`Selection.selectAllChildren()`**

Adds all the children of the specified node to the selection.

**`Selection.setBaseAndExtent()`**

Sets the selection to be a range including all or parts of two specified DOM nodes, and any content located between them.

**`Selection.setPosition()`**

Collapses the current selection to a single point.

**`Selection.toString()`**

Returns a string currently being represented by the selection object, i.e., the currently selected text.
