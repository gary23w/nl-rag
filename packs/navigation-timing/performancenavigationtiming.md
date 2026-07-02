---
title: "PerformanceNavigationTiming - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming
domain: navigation-timing
license: CC-BY-SA-4.0
tags: navigation timing api, page load milestones, performance navigation entry, dom content loaded timing
fetched: 2026-07-02
---

# PerformanceNavigationTiming

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2021.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`PerformanceNavigationTiming`** interface provides methods and properties to store and retrieve metrics regarding the browser's document navigation events. For example, this interface can be used to determine how much time it takes to load or unload a document.

Only the current document is included in the performance timeline, so there is only one `PerformanceNavigationTiming` object in the performance timeline. It inherits all of the properties and methods of `PerformanceResourceTiming` and `PerformanceEntry`.

The following diagram shows all of the timestamp properties defined in `PerformanceNavigationTiming`.

(Timestamp diagram listing timestamps in the order in which they are recorded for the fetching of a document)

## Instance properties

This interface extends the following `PerformanceEntry` properties by qualifying and constraining them as follows:

**`PerformanceEntry.entryType` Read only**

Returns `"navigation"`.

**`PerformanceEntry.name` Read only**

Returns the document's URL. Note that text fragments, and any other fragment directives, are stripped from the URL.

**`PerformanceEntry.startTime` Read only**

Returns a `DOMHighResTimeStamp` with a value of `0`.

**`PerformanceEntry.duration` Read only**

Returns a `timestamp` that is the difference between the `PerformanceNavigationTiming.loadEventEnd` and `PerformanceEntry.startTime` properties.

This interface also extends the following `PerformanceResourceTiming` properties by qualifying and constraining them as follows:

**`PerformanceResourceTiming.initiatorType` Read only**

Returns `"navigation"`.

The interface also supports the following properties:

**`PerformanceNavigationTiming.activationStart` Read only**

A `DOMHighResTimeStamp` representing the time between when a document starts prerendering and when it is activated.

**`PerformanceNavigationTiming.confidence` Read only**

A `PerformanceTimingConfidence` object containing information that indicates whether a performance record reflects typical application performance, or is likely affected by external factors.

**`PerformanceNavigationTiming.criticalCHRestart` Read only**

A `DOMHighResTimeStamp` representing the time at which the connection restart occurred due to `Critical-CH` HTTP response header mismatch.

**`PerformanceNavigationTiming.domComplete` Read only**

A `DOMHighResTimeStamp` representing the time immediately before the user agent sets the document's `readyState` to `"complete"`.

**`PerformanceNavigationTiming.domContentLoadedEventEnd` Read only**

A `DOMHighResTimeStamp` representing the time immediately after the current document's `DOMContentLoaded` event handler completes.

**`PerformanceNavigationTiming.domContentLoadedEventStart` Read only**

A `DOMHighResTimeStamp` representing the time immediately before the current document's `DOMContentLoaded` event handler starts.

**`PerformanceNavigationTiming.domInteractive` Read only**

A `DOMHighResTimeStamp` representing the time immediately before the user agent sets the document's `readyState` to `"interactive"`.

**`PerformanceNavigationTiming.loadEventEnd` Read only**

A `DOMHighResTimeStamp` representing the time immediately after the current document's `load` event handler completes.

**`PerformanceNavigationTiming.loadEventStart` Read only**

A `DOMHighResTimeStamp` representing the time immediately before the current document's `load` event handler starts.

**`PerformanceNavigationTiming.notRestoredReasons` Read only**

A `NotRestoredReasons` object providing report data on reasons why the current document was blocked from using the back/forward cache (bfcache) on navigation.

**`PerformanceNavigationTiming.redirectCount` Read only**

A number representing the number of redirects since the last non-redirect navigation in the current browsing context.

**`PerformanceNavigationTiming.type` Read only**

A string representing the navigation type. Either `"navigate"`, `"reload"`, or `"back_forward"`.

**`PerformanceNavigationTiming.unloadEventEnd` Read only**

A `DOMHighResTimeStamp` representing the time immediately after the current document's `unload` event handler completes.

**`PerformanceNavigationTiming.unloadEventStart` Read only**

A `DOMHighResTimeStamp` representing the time immediately before the current document's `unload` event handler starts.

## Instance methods

**`PerformanceNavigationTiming.toJSON()`**

Returns a JSON representation of the `PerformanceNavigationTiming` object.

## Specifications

| Specification |
|---|
| Navigation Timing Level 2 # sec-PerformanceNavigationTiming |

## Browser compatibility
