---
title: "Geolocation: watchPosition() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition
domain: geolocation-api
license: CC-BY-SA-4.0
tags: geolocation api, device position coordinates, watch position updates, location permission prompt
fetched: 2026-07-02
---

# Geolocation: watchPosition() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`watchPosition()`** method of the `Geolocation` interface is used to register a handler function that will be called automatically each time the position of the device changes. You can also, optionally, specify an error handling callback function.

Note that in addition to requiring a secure context this feature may be blocked by the `geolocation` `Permissions-Policy`, and also requires that explicit permission be granted by the user. If required, the user will be prompted when this method is called. The permission state can be queried using the `geolocation` user permission in the Permissions API.

## Syntax

```js
watchPosition(success)
watchPosition(success, error)
watchPosition(success, error, options)
```

### Parameters

**`success`**

A callback function that takes a `GeolocationPosition` object as an input parameter.

**`error` Optional**

An optional callback function that takes a `GeolocationPositionError` object as an input parameter.

**`options` Optional**

An optional object that provides configuration options for the location watch. See `Geolocation.getCurrentPosition()` for more details on possible options.

### Return value

An integer ID that identifies the registered handler. The ID can be passed to the `Geolocation.clearWatch()` to unregister the handler.

## Examples

```js
let id;
let target;
let options;

function success(pos) {
  const crd = pos.coords;

  if (target.latitude === crd.latitude && target.longitude === crd.longitude) {
    console.log("Congratulations, you reached the target");
    navigator.geolocation.clearWatch(id);
  }
}

function error(err) {
  console.error(`ERROR(${err.code}): ${err.message}`);
}

target = {
  latitude: 0,
  longitude: 0,
};

options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0,
};

id = navigator.geolocation.watchPosition(success, error, options);
```

## Specifications

| Specification |
|---|
| Geolocation # watchposition-method |

## Browser compatibility
