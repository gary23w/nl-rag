---
title: "PerformanceEntry - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry
domain: performance-observer
license: CC-BY-SA-4.0
tags: performance observer api, performance entry buffer, observe entry types, buffered performance records
fetched: 2026-07-02
---

# PerformanceEntry

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`PerformanceEntry`** object encapsulates a single performance metric that is part of the browser's performance timeline.

The Performance API offers built-in metrics which are specialized subclasses of `PerformanceEntry`. This includes entries for resource loading, event timing, and more.

A performance entry can also be created by calling the `Performance.mark()` or `Performance.measure()` methods at an explicit point in an application. This allows you to add your own metrics to the performance timeline.

The `PerformanceEntry` instances will always be one of the following subclasses:

- `LargestContentfulPaint`
- `LayoutShift`
- `PerformanceEventTiming`
- `PerformanceLongAnimationFrameTiming`
- `PerformanceLongTaskTiming`
- `PerformanceMark`
- `PerformanceMeasure`
- `PerformanceNavigationTiming`
- `PerformancePaintTiming`
- `PerformanceResourceTiming`
- `PerformanceScriptTiming`
- `PerformanceServerTiming`
- `TaskAttributionTiming`
- `VisibilityStateEntry`

## Instance properties

**`PerformanceEntry.name` Read only**

A string representing the name for a performance entry. The value depends on the subtype.

**`PerformanceEntry.entryType` Read only**

A string representing the type of performance metric. For example, `"mark"` when `PerformanceMark` is used.

**`PerformanceEntry.startTime` Read only**

A `DOMHighResTimeStamp` representing the starting time for the performance metric.

**`PerformanceEntry.duration` Read only**

A `DOMHighResTimeStamp` representing the duration of the performance entry.

## Instance methods

**`PerformanceEntry.toJSON()`**

Returns a JSON representation of the `PerformanceEntry` object.

## Example

### Working with performance entries

The following example creates `PerformanceEntry` objects that are of the types `PerformanceMark` and `PerformanceMeasure`. The `PerformanceMark` and `PerformanceMeasure` subclasses inherit the `duration`, `entryType`, `name`, and `startTime` properties from `PerformanceEntry` and set them to their appropriate values.

```js
// Place at a location in the code that starts login
performance.mark("login-started");

// Place at a location in the code that finishes login
performance.mark("login-finished");

// Measure login duration
performance.measure("login-duration", "login-started", "login-finished");

function perfObserver(list, observer) {
  list.getEntries().forEach((entry) => {
    if (entry.entryType === "mark") {
      console.log(`${entry.name}'s startTime: ${entry.startTime}`);
    }
    if (entry.entryType === "measure") {
      console.log(`${entry.name}'s duration: ${entry.duration}`);
    }
  });
}
const observer = new PerformanceObserver(perfObserver);
observer.observe({ entryTypes: ["measure", "mark"] });
```

## Specifications

| Specification |
|---|
| Performance Timeline # performanceentry |

## Browser compatibility
