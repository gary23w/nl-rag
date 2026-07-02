---
title: "HTMLTemplateElement - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement
domain: web-components
license: CC-BY-SA-2.5
tags: web components, custom elements, html template element, customelementregistry
fetched: 2026-07-02
---

# HTMLTemplateElement

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`HTMLTemplateElement`** interface enables access to the contents of an HTML `<template>` element.

**Note:** An HTML parser can create either an `HTMLTemplateElement` or a `ShadowRoot` when it parses a `<template>` element, depending on the `<template>` attributes. If an `HTMLTemplateElement` is created the "shadow" attributes are reflected from the template. However these are not useful, because an `HTMLTemplateElement` is not a shadow root and cannot subsequently be changed to a shadow root.

## Instance properties

*This interface inherits the properties of `HTMLElement`.*

**`content` Read only**

A read-only `DocumentFragment` which contains the DOM subtree representing the `<template>` element's template contents.

**`shadowRootMode`**

A string that reflects the value of the `shadowrootmode` attribute of the associated `<template>` element.

**`shadowRootDelegatesFocus`**

A boolean that reflects the value of the `shadowrootdelegatesfocus` attribute of the associated `<template>` element.

**`shadowRootClonable`**

A boolean that reflects the value of the `shadowrootclonable` attribute of the associated `<template>` element.

**`shadowRootCustomElementRegistry`**

A string that reflects the value of the `shadowrootcustomelementregistry` attribute of the associated `<template>` element, indicating that the declarative shadow root will use a scoped `CustomElementRegistry`.

**`shadowRootSerializable`**

A boolean that reflects the value of the `shadowrootserializable` attribute of the associated `<template>` element.

**`shadowRootSlotAssignment`**

A string that reflects the value of the `shadowrootslotassignment` attribute of the associated `<template>` element.

## Instance methods

*This interface inherits the methods of `HTMLElement`.*

## Specifications

| Specification |
|---|
| HTML # htmltemplateelement |

## Browser compatibility
