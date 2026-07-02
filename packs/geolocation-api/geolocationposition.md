---
title: "GeolocationPosition - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
domain: geolocation-api
license: CC-BY-SA-4.0
tags: geolocation api, device position coordinates, watch position updates, location permission prompt
fetched: 2026-07-02
---

# GeolocationPosition

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`GeolocationPosition`** interface represents the position of the concerned device at a given time. The position, represented by a `GeolocationCoordinates` object, comprehends the 2D position of the device, on a spheroid representing the Earth, but also its altitude and its speed.

## Instance properties

*The `GeolocationPosition` interface doesn't inherit any properties.*

**`GeolocationPosition.coords` Read only**

Returns a `GeolocationCoordinates` object defining the current location.

**`GeolocationPosition.timestamp` Read only**

Returns a timestamp, given as Unix time in milliseconds, representing the time at which the location was retrieved.

## Instance methods

*The `GeolocationPosition` interface doesn't inherit any methods.*

**`GeolocationPosition.toJSON()`**

Returns a JSON representation of the `GeolocationPosition` object and enables serialization with `JSON.stringify()`.

## Specifications

| Specification |
|---|
| Geolocation # position_interface |

## Browser compatibility
