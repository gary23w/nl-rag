---
title: "MutationRecord - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord
domain: mutation-observer
license: CC-BY-SA-4.0
tags: mutation observer api, dom tree change watch, mutation record list, observe child list
fetched: 2026-07-02
---

# MutationRecord

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`MutationRecord`** is a read-only interface that represents an individual DOM mutation observed by a `MutationObserver`. It is the object inside the array passed to the callback of a `MutationObserver`.

## Instance properties

**`MutationRecord.addedNodes` Read only**

The nodes added by a mutation. Will be an empty `NodeList` if no nodes were added.

**`MutationRecord.attributeName` Read only**

The name of the changed attribute as a string, or `null`.

**`MutationRecord.attributeNamespace` Read only**

The namespace of the changed attribute as a string, or `null`.

**`MutationRecord.nextSibling` Read only**

The next sibling of the added or removed nodes, or `null`.

**`MutationRecord.oldValue` Read only**

The value depends on the `MutationRecord.type`:

- For `attributes`, it is the value of the changed attribute before the change.
- For `characterData`, it is the data of the changed node before the change.
- For `childList`, it is `null`.

**`MutationRecord.previousSibling` Read only**

The previous sibling of the added or removed nodes, or `null`.

**`MutationRecord.removedNodes` Read only**

The nodes removed by a mutation. Will be an empty `NodeList` if no nodes were removed.

**`MutationRecord.target` Read only**

The node the mutation affected, depending on the `MutationRecord.type`.

- For `attributes`, it is the element whose attribute changed.
- For `characterData`, it is the `CharacterData` node.
- For `childList`, it is the node whose children changed.

**`MutationRecord.type` Read only**

A string representing the type of mutation: `attributes` if the mutation was an attribute mutation, `characterData` if it was a mutation to a `CharacterData` node, and `childList` if it was a mutation to the tree of nodes.

## Specifications

| Specification |
|---|
| DOM # interface-mutationrecord |

## Browser compatibility
