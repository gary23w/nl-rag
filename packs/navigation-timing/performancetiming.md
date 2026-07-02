---
title: "PerformanceTiming - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming
domain: navigation-timing
license: CC-BY-SA-4.0
tags: navigation timing api, page load milestones, performance navigation entry, dom content loaded timing
fetched: 2026-07-02
---

# PerformanceTiming

**Deprecated:** This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the compatibility table at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

**Warning:** This interface is deprecated in the Navigation Timing Level 2 specification. Please use the `PerformanceNavigationTiming` interface instead.

The **`PerformanceTiming`** interface is a legacy interface kept for backwards compatibility and contains properties that offer performance timing information for various events which occur during the loading and use of the current page. You get a `PerformanceTiming` object describing your page using the `window.performance.timing` property.

## Instance properties

*The `PerformanceTiming` interface doesn't inherit any properties.*

These properties each describe the time at which a particular point in the page loading process was reached. Some correspond to DOM events; others describe the time at which internal browser operations of interest took place.

Each time is provided as a number representing the moment, in milliseconds since the UNIX epoch.

These properties are listed in the order in which they occur during the navigation process.

**`PerformanceTiming.navigationStart` Read only**

When the prompt for unload terminates on the previous document in the same browsing context. If there is no previous document, this value will be the same as `PerformanceTiming.fetchStart`.

**`PerformanceTiming.unloadEventStart` Read only**

When the `unload` event has been thrown, indicating the time at which the previous document in the window began to unload. If there is no previous document, or if the previous document or one of the needed redirects is not of the same origin, the value returned is `0`.

**`PerformanceTiming.unloadEventEnd` Read only**

When the `unload` event handler finishes. If there is no previous document, or if the previous document, or one of the needed redirects, is not of the same origin, the value returned is `0`.

**`PerformanceTiming.redirectStart` Read only**

When the first HTTP redirect starts. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is `0`.

**`PerformanceTiming.redirectEnd` Read only**

When the last HTTP redirect is completed, that is when the last byte of the HTTP response has been received. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is `0`.

**`PerformanceTiming.fetchStart` Read only**

When the browser is ready to fetch the document using an HTTP request. This moment is *before* the check to any application cache.

**`PerformanceTiming.domainLookupStart` Read only**

When the domain lookup starts. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same as `PerformanceTiming.fetchStart`.

**`PerformanceTiming.domainLookupEnd` Read only**

When the domain lookup is finished. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same as `PerformanceTiming.fetchStart`.

**`PerformanceTiming.connectStart` Read only**

When the request to open a connection is sent to the network. If the transport layer reports an error and the connection establishment is started again, the last connection establishment start time is given. If a persistent connection is used, the value will be the same as `PerformanceTiming.fetchStart`.

**`PerformanceTiming.connectEnd` Read only**

When the connection is opened network. If the transport layer reports an error and the connection establishment is started again, the last connection establishment end time is given. If a persistent connection is used, the value will be the same as `PerformanceTiming.fetchStart`. A connection is considered as opened when all secure connection handshake, or SOCKS authentication, is terminated.

**`PerformanceTiming.secureConnectionStart` Read only**

When the secure connection handshake starts. If no such connection is requested, it returns `0`.

**`PerformanceTiming.requestStart` Read only**

When the browser sent the request to obtain the actual document, from the server or from a cache. If the transport layer fails after the start of the request and the connection is reopened, this property will be set to the time corresponding to the new request.

**`PerformanceTiming.responseStart` Read only**

When the browser received the first byte of the response, from the server from a cache, or from a local resource.

**`PerformanceTiming.responseEnd` Read only**

When the browser received the last byte of the response, or when the connection is closed if this happened first, from the server, the cache, or from a local resource.

**`PerformanceTiming.domLoading` Read only**

When the parser started its work, that is when its `Document.readyState` changes to `'loading'` and the corresponding `readystatechange` event is thrown.

**`PerformanceTiming.domInteractive` Read only**

When the parser finished its work on the main document, that is when its `Document.readyState` changes to `'interactive'` and the corresponding `readystatechange` event is thrown.

**`PerformanceTiming.domContentLoadedEventStart` Read only**

Right before the parser sent the `DOMContentLoaded` event, that is right after all the scripts that need to be executed right after parsing have been executed.

**`PerformanceTiming.domContentLoadedEventEnd` Read only**

Right after all the scripts that need to be executed as soon as possible, in order or not, have been executed.

**`PerformanceTiming.domComplete` Read only**

When the parser finished its work on the main document, that is when its `Document.readyState` changes to `'complete'` and the corresponding `readystatechange` event is thrown.

**`PerformanceTiming.loadEventStart` Read only**

When the `load` event was sent for the current document. If this event has not yet been sent, it returns `0`.

**`PerformanceTiming.loadEventEnd` Read only**

When the `load` event handler terminated, that is when the load event is completed. If this event has not yet been sent, or is not yet completed, it returns `0`.

## Instance methods

*The `PerformanceTiming`* *interface doesn't inherit any methods.*

**`PerformanceTiming.toJSON()`**

Returns a JSON object representing this `PerformanceTiming` object.

## Specifications

| Specification |
|---|
| Navigation Timing Level 2 # dom-performancetiming |

## Browser compatibility
