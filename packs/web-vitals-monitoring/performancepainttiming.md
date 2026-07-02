---
title: "PerformancePaintTiming - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformancePaintTiming
domain: web-vitals-monitoring
license: CC-BY-SA-4.0
tags: web vitals monitoring, performance entry timeline, performance mark measure, user timing metrics
fetched: 2026-07-02
---

# PerformancePaintTiming

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`PerformancePaintTiming`** interface provides timing information about "paint" (also called "render") operations during web page construction. "Paint" refers to conversion of the render tree to on-screen pixels.

There are two key paint moments this API provides:

- First Paint (FP): Time when anything is rendered. Note that the marking of the first paint is optional, not all user agents report it.
- First Contentful Paint (FCP): Time when the first bit of DOM text or image content is rendered.

A third key paint moment is provided by the `LargestContentfulPaint` API:

- Largest Contentful Paint (LCP): Render time of the largest image or text block visible within the viewport, recorded from when the page first begins to load.

The data this API provides helps you minimize the time that users have to wait before they can see the site's content start to appear. Decreasing the time until these key paint moments make sites feel more responsive, performant, and engaging for your users.

Like other Performance APIs, this API extends `PerformanceEntry`.

## Instance properties

This interface directly defines the following properties:

**`PerformancePaintTiming.paintTime`**

Returns the `timestamp` when the rendering phase ended and the paint phase started.

**`PerformancePaintTiming.presentationTime`**

Returns the `timestamp` when the painted pixels were actually drawn on the screen.

It also extends the following `PerformanceEntry` properties, qualifying and constraining them as described:

**`PerformanceEntry.entryType`**

Returns `"paint"`.

**`PerformanceEntry.name`**

Returns either `"first-paint"` or `"first-contentful-paint"`.

**`PerformanceEntry.startTime`**

Returns the `timestamp` when the paint occurred.

**`PerformanceEntry.duration`**

Returns 0.

## Instance methods

**`PerformancePaintTiming.toJSON()`**

Returns a JSON representation of the `PerformancePaintTiming` object.

## Examples

### Getting basic paint timings

Example using a `PerformanceObserver`, which notifies of new `paint` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

```js
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(
      `The time to ${entry.name} was ${entry.startTime} milliseconds.`,
    );
    // Logs "The time to first-paint was 386.7999999523163 milliseconds."
    // Logs "The time to first-contentful-paint was 400.6999999284744 milliseconds."
  });
});

observer.observe({ type: "paint", buffered: true });
```

Example using `Performance.getEntriesByType()`, which only shows `paint` performance entries present in the browser's performance timeline at the time you call this method:

```js
const entries = performance.getEntriesByType("paint");
entries.forEach((entry) => {
  console.log(`The time to ${entry.name} was ${entry.startTime} milliseconds.`);
  // Logs "The time to first-paint was 386.7999999523163 milliseconds."
  // Logs "The time to first-contentful-paint was 400.6999999284744 milliseconds."
});
```

### Getting separate paint and presentation timings

The `paintTime` and `presentationTime` properties enable you to retrieve specific timings for the paint phase starting and the painted pixels being drawn on the screen. The `paintTime` is broadly interoperable, whereas the `presentationTime` is implementation-dependent.

This example builds on the earlier `Performance.getEntriesByType()` example, showing how to check for `paintTime` and `presentationTime` support and retrieve those values if they are available. In non-supporting browsers, the code retrieves the `loadTime`.

```js
const entries = performance.getEntriesByType("paint");
entries.forEach((entry) => {
  if (entry.presentationTime) {
    console.log(
      "paintTime:",
      entry.paintTime,
      "presentationTime:",
      entry.presentationTime,
    );
  } else if (entry.paintTime) {
    console.log("paintTime:", entry.paintTime);
  } else {
    console.log("loadTime", entry.loadTime);
  }
});
```

## Specifications

| Specification |
|---|
| Paint Timing # sec-PerformancePaintTiming |

## Browser compatibility
