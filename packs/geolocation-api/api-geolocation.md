---
title: "Geolocation - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation
domain: geolocation-api
license: CC-BY-SA-4.0
tags: geolocation api, device position coordinates, watch position updates, location permission prompt
fetched: 2026-07-02
---

# Geolocation

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`Geolocation`** interface represents an object able to obtain the position of the device programmatically. It gives Web content access to the location of the device. This allows a website or app to offer customized results based on the user's location.

An object with this interface is obtained using the `navigator.geolocation` property implemented by the `Navigator` object.

**Note:** For security reasons, when a web page tries to access location information, the user is notified and asked to grant permission. Be aware that each browser has its own policies and methods for requesting this permission.

## Instance properties

*The `Geolocation` interface neither implements, nor inherits any property.*

## Instance methods

*The `Geolocation` interface doesn't inherit any method.*

**`Geolocation.getCurrentPosition()`**

Determines the device's current location and gives back a `GeolocationPosition` object with the data.

**`Geolocation.watchPosition()`**

Returns a `long` value representing the newly established callback function to be invoked whenever the device location changes.

**`Geolocation.clearWatch()`**

Removes the particular handler previously installed using `watchPosition()`.

## Specifications

| Specification |
|---|
| Geolocation # geolocation_interface |

## Browser compatibility
