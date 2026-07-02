---
title: "Metrics Data Model (part 2/2)"
source: https://opentelemetry.io/docs/specs/otel/metrics/data-model/
domain: exemplars-metrics
license: CC-BY-SA-4.0
tags: metric exemplar, trace to metric link, histogram exemplar, high resolution sample
fetched: 2026-07-02
part: 2/2
---

## Resets and Gaps

**Status**: Development

When the `StartTimeUnixNano` field is present, it allows the consumer to observe when there are gaps and overlapping writers in a stream. Correctly used, the consumer can observe both transient and ongoing violations of the single-writer principle as well as reset events. In an unbroken sequence of observations, the `StartTimeUnixNano` always matches either the `TimeUnixNano` or the `StartTimeUnixNano` of other points in the same sequence. For the initial points in an unbroken sequence:

- When `StartTimeUnixNano` is less than `TimeUnixNano`, a new unbroken sequence of observations begins with a “true” reset at a known start time. The zero value is implicit, it is not necessary to record the starting point.
- When `StartTimeUnixNano` equals `TimeUnixNano`, a new unbroken sequence of observations begins with a reset at an unknown start time. The initial observed value is recorded to indicate that an unbroken sequence of observations resumes. These points have zero duration, and indicate that nothing is known about previously-reported points and that data may have been lost.

For subsequent points in an unbroken sequence:

- For points with delta aggregation temporality, the `StartTimeUnixNano` of each point matches the `TimeUnixNano` of the preceding point
- Otherwise, the `StartTimeUnixNano` of each point matches the `StartTimeUnixNano` of the initial observation.

A metric stream has a gap, where it is implicitly undefined, anywhere there is a range of time such that no point covers that range range with its `StartTimeUnixNano` and `TimeUnixNano` fields.

### Cumulative streams: handling unknown start time

An unbroken stream of observations is resumed with a zero-duration point and non-zero value, as described above. For points with cumulative aggregation temporality, the rate contributed to the timeseries by each point depends on the prior point value in the stream.

To correctly compute the rate contribution of the first point in an unbroken sequence requires knowing whether it is the first point. Unknown start-time reset points appear with `TimeUnixNano` equal to the `StartTimeUnixNano` of a stream of points, in which case the rate contribution of the first point is considered zero. An earlier sequence of observations is expected to have reported the same cumulative state prior to a gap in observations.

The presence or absence of a point with `TimeUnixNano` equal to the `StartTimeUnixNano` indicates how to count rate contribution from the first point in a sequence. If the first point in an unknown start-time reset sequence is lost, the consumer of this data might overcount the rate contribution of the second point, as it then appears like a “true” reset.

Various approaches can be taken to avoid overcounting. A system could use state from earlier in the stream to resolve start-time ambiguity, for example.

### Cumulative streams: inserting true reset points

The absolute value of the cumulative counter is often considered meaningful, but when the cumulative value is only used to calculate a rate function, it is possible to drop the initial unknown start-time reset point, but remember the initially observed value in order to modify subsequent observations. Later in the cumulative sequence are output relative to the initial value, thus appears as a true reset offset by an unknown constant.

This process is known as inserting true reset points, a special case of reaggregation for cumulative series.


## Overlap

**Status**: Development

Overlap occurs when more than one metric data point is defined for a metric stream within a time window. Overlap is usually caused through mis-configuration, and it can lead to serious mis-interpretation of the data. `StartTimeUnixNano` is recommended so that consumers can recognize and response to overlapping points.

We define three principles for handling overlap:

- Resolution (correction via dropping points)
- Observability (allowing the data to flow to backends)
- Interpolation (correction via data manipulation)

### Overlap resolution

When more than one process writes the same metric data stream, OTLP data points may appear to overlap. This condition typically results from misconfiguration, but can also result from running identical processes (indicative of operating system or SDK bugs, like missing process attributes). When there are overlapping points, receivers SHOULD eliminate points so that there are no overlaps. Which data to select in overlapping cases is not specified.

### Overlap observability

OpenTelemetry collectors SHOULD export telemetry when they observe overlapping points in data streams, so that the user can monitor for erroneous configurations.

### Overlap interpolation

When one process starts just as another exits, the appearance of overlapping points may be expected. In this case, OpenTelemetry collectors SHOULD modify points at the change-over using interpolation for Sum data points, to reduce gaps to zero width in these cases, without any overlap.


## Stream Manipulations

**Status**: Development

Pending introduction.

### Sums: Delta-to-Cumulative

While OpenTelemetry (and some metric backends) allows both Delta and Cumulative sums to be reported, the timeseries model we target does not support delta counters. To this end, converting from delta to cumulative needs to be defined so that backends can use this mechanism.

Note

This is not the only possible Delta to Cumulative algorithm. It is just one possible implementation that fits the OTel Data Model.

Converting from delta points to cumulative point is inherently a stateful operation. To successfully translate, we need all incoming delta points to reach one destination which can keep the current counter state and generate a new cumulative stream of data (see single writer principle).

The algorithm is scheduled out as follows:

- Upon receiving the first Delta point for a given counter we set up the following:
  - A new counter which stores the cumulative sum, set to the initial counter.
  - A start time that aligns with the start time of the first point.
  - A “last seen” time that aligns with the time of the first point.
- Upon receiving future Delta points, we do the following:
  - If the next point aligns with the expected next-time window (see detecting delta restarts)
    - Update the “last seen” time to align with the time of the current point.
    - Add the current value to the cumulative counter
    - Output a new cumulative point with the original start time and current last seen time and count.
  - if the current point precedes the start time, then drop this point. Note: there are algorithms which can deal with late arriving points.
  - if the next point does NOT align with the expected next-time window, then reset the counter following the same steps performed as if the current point was the first point seen.

#### Sums: detecting alignment issues

When the next delta sum reported for a given metric stream does not align with where we expect it, one of several things could have occurred:

- The process reporting metrics was rebooted, leading to a new reporting interval for the metric.
- A Single-Writer principle violation where multiple processes are reporting the same metric stream.
- There was a lost data point, or dropped information.

In all of these scenarios we do our best to give any cumulative metric knowledge that some data was lost, and reset the counter.

We detect alignment via two mechanisms:

- If the incoming delta time interval has significant overlap with the previous time interval, we assume a violation of the single-writer principle and can be handled with one of the following options:
  - Simply report the inconsistencies in time intervals, as the error condition could be caused by a misconfiguration.
  - Eliminate the overlap / deduplicate on the receiver side.
  - Correct the inconsistent time intervals by differentiating the given `Resource` and `Attribute` set used from overlapping time.
- If the incoming delta time interval has a significant gap from the last seen time, we assume some kind of reboot/restart and reset the cumulative counter.

#### Sums: Missing Timestamps

One degenerate case for the delta-to-cumulative algorithm is when timestamps are missing from metric data points. While this shouldn’t be the case when using OpenTelemetry generated metrics, it can occur when adapting other metric formats, e.g. StatsD counts.

In this scenario, the algorithm listed above would reset the cumulative sum on every data point due to not being able to determine alignment or point overlap. For comparison, see the simple logic used in statsd sums where all points are added, and lost points are ignored.
