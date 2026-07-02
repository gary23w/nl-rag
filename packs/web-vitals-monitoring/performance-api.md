---
title: "Performance APIs - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
domain: web-vitals-monitoring
license: CC-BY-SA-4.0
tags: web vitals monitoring, performance entry timeline, performance mark measure, user timing metrics
fetched: 2026-07-02
---

# Performance APIs

**Note:** This feature is available in Web Workers.

The Performance API is a group of standards used to measure the performance of web applications.

## Concepts and usage

To ensure web applications are fast, it's important to measure and analyze various performance metrics. The Performance API provides important built-in metrics and the ability to add your own measurements to the browser's performance timeline. The performance timeline contains high precision timestamps and can be displayed in developer tools. You can also send its data to analytics end points to record performance metrics over time.

Each performance metric is represented by a single `PerformanceEntry`. A performance entry has a `name`, a `duration`, a `startTime`, and a `type`. All performance metrics extend the `PerformanceEntry` interface and qualify it further.

Most of the performance entries are recorded for you without you having to do anything, and are then accessible either through `Performance.getEntries()` or (preferably) through `PerformanceObserver`. For example, `PerformanceEventTiming` entries are recorded for events that take longer than a set threshold. But the Performance API also enables you to define and record your own custom events, using the `PerformanceMark` and `PerformanceMeasure` interfaces.

The main `Performance` interface is available in both `Window` and `Worker` global scopes, and enables you to add custom performance entries, to clear performance entries, and to retrieve performance entries.

The `PerformanceObserver` interface enables you to listen for various types of performance entry as they are recorded.

For more conceptual information, see the Performance API guides below.

(UML diagram of Performance APIs)

## Reference

The following interfaces are present in the Performance API:

**`EventCounts`**

A read-only map returned by `performance.eventCounts` containing the number of events which have been dispatched per event type.

**`LargestContentfulPaint`**

Measures the render time of the largest image or text block visible within the viewport, recorded from when the page first begins to load.

**`LayoutShift`**

Provides insights into the layout stability of web pages based on movements of the elements on the page.

**`LayoutShiftAttribution`**

Provides debugging information about elements which have shifted.

**`NotRestoredReasonDetails`**

Represents a single reason why a navigated page was blocked from using the back/forward cache (bfcache).

**`NotRestoredReasons`**

Provides report data containing reasons why the current document was blocked from using the back/forward cache (bfcache) on navigation.

**`Performance`**

Main interface to access performance measurements. Available to window and worker contexts using `Window.performance` or `WorkerGlobalScope.performance`.

**`PerformanceElementTiming`**

Measures rendering timestamps of specific elements.

**`PerformanceEntry`**

An entry on the performance timeline encapsulating a single performance metric. All performance metrics inherit from this interface.

**`PerformanceEventTiming`**

Measures latency of events and Interaction to Next Paint (INP).

**`PerformanceLongAnimationFrameTiming`**

Provides metrics on long animation frames (LoAFs) that occupy rendering and block other tasks from being executed.

**`PerformanceLongTaskTiming`**

Provides metrics on long tasks that occupy rendering and block other tasks from being executed.

**`PerformanceMark`**

Custom marker for your own entry on the performance timeline.

**`PerformanceMeasure`**

Custom time measurement between two performance entries.

**`PerformanceNavigationTiming`**

Measures document navigation events, like how much time it takes to load a document.

**`PerformanceObserver`**

Listens for new performance entries as they are recorded in the performance timeline.

**`PerformanceObserverEntryList`**

List of entries that were observed in a performance observer.

**`PerformancePaintTiming`**

Measures render operations during web page construction.

**`PerformanceResourceTiming`**

Measures network loading metrics such as redirect start and end times, fetch start, DNS lookup start and end times, response start and end times for resources such as images, scripts, fetch calls, etc.

**`PerformanceScriptTiming`**

Provides metrics on individual scripts causing long animation frames (LoAFs).

**`PerformanceServerTiming`**

Surfaces server metrics that are sent with the response in the `Server-Timing` HTTP header.

**`TaskAttributionTiming`**

Identifies the type of task and the container that is responsible for the long task.

**`VisibilityStateEntry`**

Measures the timing of page visibility state changes, i.e., when a tab changes from the foreground to the background or vice versa.

## Guides

The following guides help you to understand key concepts of the Performance API and provide an overview about its abilities:

- Performance data: Collecting, accessing, and working with performance data.
- High precision timing: Measuring with high precision time and monotonic clocks.
- Resource timing: Measuring network timing for fetched resources, such as images, CSS, and JavaScript.
- Navigation timing: Measuring navigation timing of a document.
- User timing: Measuring and recording performance data custom to your application.
- Server timing: Collecting server-side metrics.
- Long animation frame timing: Collecting metrics on long animation frames (LoAFs) and their causes.
- Monitoring bfcache blocking reasons: Reporting on why the current document was blocked from using the back/forward cache (bfcache).

## Specifications

| Specification |
|---|
| Element Timing API |
| Event Timing API |
| High Resolution Time |
| Largest Contentful Paint |
| Layout Instability API |
| Long Tasks API |
| Navigation Timing Level 2 |
| Paint Timing |
| Performance Timeline |
| Resource Timing |
| Server Timing |
| User Timing |
| Long Animation Frames API |
| Measure Memory API |
| HTML # the-visibilitystateentry-interface |
| HTML # the-notrestoredreasons-interface |
