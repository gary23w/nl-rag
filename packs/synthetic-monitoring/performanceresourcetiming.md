---
title: "PerformanceResourceTiming - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming
domain: synthetic-monitoring
license: CC-BY-SA-4.0
tags: synthetic monitoring, scripted uptime probe, website availability check, lab performance measurement
fetched: 2026-07-02
---

# PerformanceResourceTiming

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`PerformanceResourceTiming`** interface enables retrieval and analysis of detailed network timing data regarding the loading of an application's resources. An application can use the timing metrics to determine, for example, the length of time it takes to fetch a specific resource, such as an `XMLHttpRequest`, `<SVG>`, image, or script.

## Description

The interface's properties create a resource loading timeline with high-resolution timestamps for network events such as redirect start and end times, fetch start, DNS lookup start and end times, response start and end times, and more. Additionally, the interface extends `PerformanceEntry` with other properties which provide data about the size of the fetched resource as well as the type of resource that initiated the fetch.

### Typical resource timing metrics

The properties of this interface allow you to calculate certain resource timing metrics. Common use cases include:

- Measuring TCP handshake time (`connectEnd` - `connectStart`)
- Measuring DNS lookup time (`domainLookupEnd` - `domainLookupStart`)
- Measuring redirection time (`redirectEnd` - `redirectStart`)
- Measuring interim request time (`firstInterimResponseStart` - `finalResponseHeadersStart`)
- Measuring request time (`responseStart` - `requestStart`)
- Measuring document request time (`finalResponseHeadersStart` - `requestStart`)
- Measuring TLS negotiation time (`requestStart` - `secureConnectionStart`)
- Measuring time to fetch (without redirects) (`responseEnd` - `fetchStart`)
- Measuring ServiceWorker processing time (`fetchStart` - `workerStart`)
- Checking if content was compressed (`decodedBodySize` should not be `encodedBodySize`)
- Checking if local caches were hit (`transferSize` should be `0`)
- Checking if modern and fast protocols are used (`nextHopProtocol` should be HTTP/2 or HTTP/3)
- Checking if the correct resources are render-blocking (`renderBlockingStatus`)

### Managing resource buffer sizes

By default only 250 resource timing entries are buffered. For more information see the resource buffer sizes of the Resource Timing guide.

### Cross-origin timing information

Many of the resource timing properties are restricted to return `0` or an empty string when the resource is a cross-origin request. To expose cross-origin timing information, the `Timing-Allow-Origin` HTTP response header needs to be set.

The properties which are returned as `0` by default when loading a resource from an origin other than the one of the web page itself: `redirectStart`, `redirectEnd`, `domainLookupStart`, `domainLookupEnd`, `connectStart`, `connectEnd`, `secureConnectionStart`, `requestStart`, and `responseStart`.

For example, to allow `https://developer.mozilla.org` to see resource timing information, the cross-origin resource should send:

```http
Timing-Allow-Origin: https://developer.mozilla.org
```

## Instance properties

### Inherited from `PerformanceEntry`

This interface extends the following `PerformanceEntry` properties for resource performance entry types by qualifying and constraining them as follows:

**`PerformanceEntry.duration` Read only**

Returns a `timestamp` that is the difference between the `responseEnd` and the `startTime` properties.

**`PerformanceEntry.entryType` Read only**

Returns `"resource"`.

**`PerformanceEntry.name` Read only**

Returns the resource's URL.

**`PerformanceEntry.startTime` Read only**

Returns the `timestamp` for the time a resource fetch started. This value is equivalent to `PerformanceResourceTiming.fetchStart`.

### Timestamps

The interface supports the following timestamp properties which you can see in the diagram and are listed in the order in which they are recorded for the fetching of a resource. An alphabetical listing is shown in the navigation, at left.

(Timestamp diagram listing timestamps in the order in which they are recorded for the fetching of a resource)

**`PerformanceResourceTiming.redirectStart` Read only**

A `DOMHighResTimeStamp` that represents the start time of the fetch which initiates the redirect.

**`PerformanceResourceTiming.redirectEnd` Read only**

A `DOMHighResTimeStamp` immediately after receiving the last byte of the response of the last redirect.

**`PerformanceResourceTiming.workerStart` Read only**

Returns a `DOMHighResTimeStamp` immediately before dispatching the `FetchEvent` if a Service Worker thread is already running, or immediately before starting the Service Worker thread if it is not already running. If the resource is not intercepted by a Service Worker the property will always return 0.

**`PerformanceResourceTiming.fetchStart` Read only**

A `DOMHighResTimeStamp` immediately before the browser starts to fetch the resource.

**`PerformanceResourceTiming.domainLookupStart` Read only**

A `DOMHighResTimeStamp` immediately before the browser starts the domain name lookup for the resource.

**`PerformanceResourceTiming.domainLookupEnd` Read only**

A `DOMHighResTimeStamp` representing the time immediately after the browser finishes the domain name lookup for the resource.

**`PerformanceResourceTiming.connectStart` Read only**

A `DOMHighResTimeStamp` immediately before the browser starts to establish the connection to the server to retrieve the resource.

**`PerformanceResourceTiming.secureConnectionStart` Read only**

A `DOMHighResTimeStamp` immediately before the browser starts the handshake process to secure the current connection.

**`PerformanceResourceTiming.connectEnd` Read only**

A `DOMHighResTimeStamp` immediately after the browser finishes establishing the connection to the server to retrieve the resource.

**`PerformanceResourceTiming.requestStart` Read only**

A `DOMHighResTimeStamp` immediately before the browser starts requesting the resource from the server.

**`PerformanceResourceTiming.firstInterimResponseStart` Read only**

A `DOMHighResTimeStamp` that represents the interim response time (for example, 100 Continue or 103 Early Hints).

**`PerformanceResourceTiming.responseStart` Read only**

A `DOMHighResTimeStamp` immediately after the browser receives the first byte of the response from the server (which may be an interim response).

**`PerformanceResourceTiming.finalResponseHeadersStart` Read only**

A `DOMHighResTimeStamp` that represents the final headers response time (for example, 200 Success), after any interim response time.

**`PerformanceResourceTiming.responseEnd` Read only**

A `DOMHighResTimeStamp` immediately after the browser receives the last byte of the resource or immediately before the transport connection is closed, whichever comes first.

### Additional resource information

Additionally, this interface exposes the following properties containing more information about a resource:

**`PerformanceResourceTiming.contentType` Read only**

A string representing a minimized and standardized version of the MIME-type of the fetched resource.

**`PerformanceResourceTiming.decodedBodySize` Read only**

A number that is the size (in octets) received from the fetch (HTTP or cache) of the message body, after removing any applied content encoding.

**`PerformanceResourceTiming.deliveryType` Read only**

Indicates how the resource was delivered — for example from the cache or from a navigational prefetch.

**`PerformanceResourceTiming.encodedBodySize` Read only**

A number representing the size (in octets) received from the fetch (HTTP or cache), of the payload body, before removing any applied content encodings.

**`PerformanceResourceTiming.initiatorType` Read only**

A string representing the web platform feature that initiated the performance entry.

**`PerformanceResourceTiming.nextHopProtocol` Read only**

A string representing the network protocol used to fetch the resource, as identified by the ALPN Protocol ID (RFC7301).

**`PerformanceResourceTiming.renderBlockingStatus` Read only**

A string representing the render-blocking status. Either `"blocking"` or `"non-blocking"`.

**`PerformanceResourceTiming.responseStatus` Read only**

A number representing the HTTP response status code returned when fetching the resource.

**`PerformanceResourceTiming.transferSize` Read only**

A number representing the size (in octets) of the fetched resource. The size includes the response header fields plus the response payload body.

**`PerformanceResourceTiming.serverTiming` Read only**

An array of `PerformanceServerTiming` entries containing server timing metrics.

## Instance methods

**`PerformanceResourceTiming.toJSON()`**

Returns a JSON representation of the `PerformanceResourceTiming` object.

## Examples

### Logging resource timing information

Example using a `PerformanceObserver`, which notifies of new `resource` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

```js
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(entry);
  });
});

observer.observe({ type: "resource", buffered: true });
```

Example using `Performance.getEntriesByType()`, which only shows `resource` performance entries present in the browser's performance timeline at the time you call this method:

```js
const resources = performance.getEntriesByType("resource");
resources.forEach((entry) => {
  console.log(entry);
});
```

## Specifications

| Specification |
|---|
| Resource Timing # performanceresourcetiming |

## Browser compatibility
