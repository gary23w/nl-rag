---
title: "PerformanceObserver - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver
domain: intersection-observer
license: CC-BY-SA-2.5
tags: intersection observer, lazy loading, viewport visibility, resize observer, mutation observer
fetched: 2026-07-02
---

# PerformanceObserver

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`PerformanceObserver`** interface is used to observe performance measurement events and be notified of new performance entries as they are recorded in the browser's *performance timeline*.

## Constructor

**`PerformanceObserver()`**

Creates and returns a new `PerformanceObserver` object.

## Static properties

**`PerformanceObserver.supportedEntryTypes` Read only**

Returns an array of the `entryType` values supported by the user agent.

## Instance methods

**`PerformanceObserver.observe()`**

Specifies the set of entry types to observe. The performance observer's callback function will be invoked when performance entry is recorded for one of the specified `entryTypes`.

**`PerformanceObserver.disconnect()`**

Stops the performance observer callback from receiving performance entries.

**`PerformanceObserver.takeRecords()`**

Returns the current list of performance entries stored in the performance observer, emptying it out.

## Examples

### Creating a PerformanceObserver

The following example creates a `PerformanceObserver` watching for "mark" (`PerformanceMark`) and "measure" (`PerformanceMeasure`) events. The `perfObserver` callback provides a `list` (`PerformanceObserverEntryList`) which allows you to get observed performance entries.

```js
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
| Performance Timeline # performanceobserver |

## Browser compatibility
