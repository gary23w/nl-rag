---
title: "PerformanceObserverEntryList - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserverEntryList
domain: performance-observer
license: CC-BY-SA-4.0
tags: performance observer api, performance entry buffer, observe entry types, buffered performance records
fetched: 2026-07-02
---

# PerformanceObserverEntryList

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`PerformanceObserverEntryList`** interface is a list of performance events that were explicitly observed via the `observe()` method.

## Instance methods

**`PerformanceObserverEntryList.getEntries()`**

Returns a list of all explicitly observed `PerformanceEntry` objects.

**`PerformanceObserverEntryList.getEntriesByType()`**

Returns a list of all explicitly observed `PerformanceEntry` objects of the given entry type.

**`PerformanceObserverEntryList.getEntriesByName()`**

Returns a list of all explicitly observed `PerformanceEntry` objects based on the given name and entry type.

## Example

### Using PerformanceObserverEntryList

In the following example, `list` is the `PerformanceObserverEntryList` object. The `getEntries()` method is called to get all explicitly observed `PerformanceEntry` objects which are "measure" and "mark" in this case.

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
| Performance Timeline # performanceobserverentrylist-interface |

## Browser compatibility
