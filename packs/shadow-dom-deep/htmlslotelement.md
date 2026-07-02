---
title: "HTMLSlotElement - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement
domain: shadow-dom-deep
license: CC-BY-SA-4.0
tags: shadow dom internals, shadow root attachment, style encapsulation boundary, slot content projection
fetched: 2026-07-02
---

# HTMLSlotElement

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`HTMLSlotElement`** interface of the Shadow DOM API enables access to the name and assigned nodes of an HTML `<slot>` element.

## Instance properties

*Also inherits properties from its parent interface, `HTMLElement`.*

**`HTMLSlotElement.name`**

A string used to get and set the slot's name.

## Instance methods

*Also inherits methods from its parent interface, `HTMLElement`.*

**`HTMLSlotElement.assign()`**

Sets the manually assigned nodes for this slot to the given nodes.

**`HTMLSlotElement.assignedNodes()`**

Returns a sequence of the nodes assigned to this slot. If the `flatten` option is set to `true`, it returns a sequence of both the nodes assigned to this slot, and the nodes assigned to any other slots that are descendants of this slot. If no assigned nodes are found, it returns the slot's fallback content.

**`HTMLSlotElement.assignedElements()`**

Returns a sequence of the elements assigned to this slot (and no other nodes). If the `flatten` option is set to `true`, it returns a sequence of both the elements assigned to this slot, and the elements assigned to any other slots that are descendants of this slot. If no assigned elements are found, it returns the slot's fallback content.

## Events

*Also inherits events from its parent interface, `HTMLElement`.*

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

**`slotchange`**

Fired on an `HTMLSlotElement` instance (`<slot>` element) when the node(s) contained in that slot change.

## Examples

The following snippet is taken from our slotchange example (see it live also).

```js
let slots = this.shadowRoot.querySelectorAll("slot");
slots[1].addEventListener("slotchange", (e) => {
  let nodes = slots[1].assignedNodes();
  console.log(
    `Element in Slot "${slots[1].name}" changed to "${nodes[0].outerHTML}".`,
  );
});
```

Here we grab references to all the slots, then add a slotchange event listener to the 2nd slot in the template — which is the one that keeps having its contents changed in the example.

Every time the element inserted in the slot changes, we log a report to the console saying which slot has changed, and what the new node inside the slot is.

## Specifications

| Specification |
|---|
| HTML # htmlslotelement |

## Browser compatibility
