---
title: "HTMLTemplateElement: shadowRootMode property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement/shadowRootMode
domain: declarative-shadow-dom
license: CC-BY-SA-4.0
tags: declarative shadow dom, shadowrootmode attribute, server rendered shadow tree, template shadowroot parsing
fetched: 2026-07-02
---

# HTMLTemplateElement: shadowRootMode property

Baseline

2024

Newly available

Since February 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

The **`shadowRootMode`** property of the `HTMLTemplateElement` interface reflects the value of the `shadowrootmode` attribute of the associated `<template>` element.

**Note:** This property is not useful for developers, and is only documented for completeness. If a `<template>` element is used to declaratively create a `ShadowRoot`, then this object and property do not exist. Otherwise, if an `HTMLTemplateElement` is created, the value of this property is irrelevant because the object is not a shadow root and cannot subsequently be changed to a shadow root.

## Value

Reflects the value of the `shadowrootmode` attribute of the associated `<template>` element.

## Specifications

| Specification |
|---|
| HTML # dom-template-shadowrootmode |

## Browser compatibility
