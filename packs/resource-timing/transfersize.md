---
title: "PerformanceResourceTiming: transferSize property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/transferSize
domain: resource-timing
license: CC-BY-SA-4.0
tags: resource timing api, resource fetch timing, network request phases, transfer size metric
fetched: 2026-07-02
---

# PerformanceResourceTiming: transferSize property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`transferSize`** read-only property represents the size (in octets) of the fetched resource. The size includes the response header fields plus the response payload body (as defined by RFC7230).

If the resource is fetched from a local cache, or if it is a cross-origin resource, this property returns zero.

## Value

The `transferSize` property can have the following values:

- A number representing the size (in octets) of the fetched resource. The size includes the response header fields plus the response payload body (RFC7230).
- `0` if the resource was instantaneously retrieved from a cache.
- `0` if the resource is a cross-origin request and no `Timing-Allow-Origin` HTTP response header is used.

## Examples

### Checking if a cache was hit

For environments not supporting the `responseStatus` property, the `transferSize` property can be used to determine cache hits. If `transferSize` is zero and the resource has a non-zero decoded body size (meaning the resource is same-origin or has `Timing-Allow-Origin`), the resource was fetched from a local cache.

Example using a `PerformanceObserver`, which notifies of new `resource` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

```js
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    if (entry.transferSize === 0 && entry.decodedBodySize > 0) {
      console.log(`${entry.name} was loaded from cache`);
    }
  });
});

observer.observe({ type: "resource", buffered: true });
```

Example using `Performance.getEntriesByType()`, which only shows `resource` performance entries present in the browser's performance timeline at the time you call this method:

```js
const resources = performance.getEntriesByType("resource");
resources.forEach((entry) => {
  if (entry.transferSize === 0 && entry.decodedBodySize > 0) {
    console.log(`${entry.name} was loaded from cache`);
  }
});
```

### Cross-origin content size information

If the value of the `transferSize` property is `0` and wasn't loaded from a local cache, the resource might be a cross-origin request. To expose cross-origin content size information, the `Timing-Allow-Origin` HTTP response header needs to be set.

For example, to allow `https://developer.mozilla.org` to see content sizes, the cross-origin resource should send:

```http
Timing-Allow-Origin: https://developer.mozilla.org
```

## Specifications

| Specification |
|---|
| Resource Timing # dom-performanceresourcetiming-transfersize |

## Browser compatibility
