---
title: "FormData - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/FormData
domain: yup-validation
license: CC-BY-SA-4.0
tags: yup validation, object schema validation, form schema, javascript validator
fetched: 2026-07-02
---

# FormData

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`FormData`** interface provides a way to construct a set of key/value pairs representing form fields and their values, which can be sent using the `fetch()`, `XMLHttpRequest.send()` or `navigator.sendBeacon()` methods. It uses the same format a form would use if the encoding type were set to `"multipart/form-data"`.

You can also pass it directly to the `URLSearchParams` constructor if you want to generate query parameters in the way a `<form>` would do if it were using simple `GET` submission.

An object implementing `FormData` can directly be used in a `for...of` structure, instead of `entries()`: `for (const p of myFormData)` is equivalent to `for (const p of myFormData.entries())`.

## Constructor

**`FormData()`**

Creates a new `FormData` object.

## Instance methods

**`FormData.append()`**

Appends a new value onto an existing key inside a `FormData` object, or adds the key if it does not already exist.

**`FormData.delete()`**

Deletes a key/value pair from a `FormData` object.

**`FormData.entries()`**

Returns an iterator that iterates through all key/value pairs contained in the `FormData`.

**`FormData.get()`**

Returns the first value associated with a given key from within a `FormData` object.

**`FormData.getAll()`**

Returns an array of all the values associated with a given key from within a `FormData`.

**`FormData.has()`**

Returns whether a `FormData` object contains a certain key.

**`FormData.keys()`**

Returns an iterator iterates through all keys of the key/value pairs contained in the `FormData`.

**`FormData.set()`**

Sets a new value for an existing key inside a `FormData` object, or adds the key/value if it does not already exist.

**`FormData.values()`**

Returns an iterator that iterates through all values contained in the `FormData`.

## Specifications

| Specification |
|---|
| XMLHttpRequest # interface-formdata |

## Browser compatibility
