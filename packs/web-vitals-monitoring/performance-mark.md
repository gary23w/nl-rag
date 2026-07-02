---
title: "Performance: mark() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark
domain: web-vitals-monitoring
license: CC-BY-SA-4.0
tags: web vitals monitoring, performance entry timeline, performance mark measure, user timing metrics
fetched: 2026-07-02
---

# Performance: mark() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`mark()`** method creates a named `PerformanceMark` object representing a high resolution timestamp marker in the browser's performance timeline.

## Syntax

```js
mark(name)
mark(name, markOptions)
```

### Parameters

**`name`**

A string representing the name of the mark. Must not be the same name as one of the properties of the deprecated `PerformanceTiming` interface.

**`markOptions` Optional**

An object for specifying a timestamp and additional metadata for the mark.

**`detail` Optional**

Arbitrary metadata to include in the mark. Defaults to `null`. Must be structured-cloneable.

**`devtools` Optional**

Some browsers have use a structured `devtools` object within the `detail` object as part of an Extensibility API that surfaces these in custom tracks in performance traces. See the Chrome's Extensibility API documentation for more information.

**`dataType`**

A string which must be set to `marker`. Identifies as a marker.

**`color` Optional**

Defaults to `"primary"`. Must be one of `"primary"`, `"primary-light"`, `"primary-dark"`, `"secondary"`, `"secondary-light"`, `"secondary-dark"`, `"tertiary"`, `"tertiary-light"`, `"tertiary-dark"`, `"error"`.

**`properties` Optional**

Array of key-value pairs. Values can be any JSON-compatible type.

**`tooltipText` Optional**

Short description for tooltip.

**`startTime` Optional**

`DOMHighResTimeStamp` to use as the mark time. Defaults to `performance.now()`.

### Return value

The `PerformanceMark` entry that was created.

### Exceptions

- `SyntaxError`: Thrown if the `name` is one of the properties of the deprecated `PerformanceTiming` interface. See the example below.
- `TypeError`: Thrown if `startTime` is negative.

## Examples

### Creating named markers

The following example uses `mark()` to create named `PerformanceMark` entries. You can create several marks with the same name. You can also assign them, to have a reference to the `PerformanceMark` object that has been created.

```js
performance.mark("login-started");
performance.mark("login-started");
performance.mark("login-finished");
performance.mark("form-sent");

const videoMarker = performance.mark("video-loaded");
```

### Creating markers with details

The performance mark is configurable using the `markOptions` object where you can put additional information in the `detail` property, which can be of any type.

```js
performance.mark("login-started", {
  detail: "Login started using the login button in the top menu.",
});

performance.mark("login-started", {
  detail: { htmlElement: myElement.id },
});
```

### Creating markers with a different start time

The default timestamp of the `mark()` method is `performance.now()`. You can set it to a different time using the `startTime` option in `markOptions`.

```js
performance.mark("start-checkout", {
  startTime: 20.0,
});

performance.mark("login-button-pressed", {
  startTime: myEvent.timeStamp,
});
```

### DevTools Extensibility API

For browsers that support the Extensibility API you can use the `detail` parameter to provide more details in a `devtools` object that will be used to display this in performance profiles:

```js
// Marker indicating when the processed image was uploaded
performance.mark("Image Upload", {
  detail: {
    devtools: {
      dataType: "marker",
      color: "secondary",
      properties: [
        ["Image Size", "2.5MB"],
        ["Upload Destination", "Cloud Storage"],
      ],
      tooltipText: "Processed image uploaded",
    },
  },
});
```

### Reserved names

Note in order to maintain backwards compatibility, names that are part of the deprecated `PerformanceTiming` interface can't be used. The following example throws:

```js
performance.mark("navigationStart");
// SyntaxError: "navigationStart" is part of
// the PerformanceTiming interface,
// and cannot be used as a mark name
```

## Specifications

| Specification |
|---|
| User Timing # dom-performance-mark |

## Browser compatibility
