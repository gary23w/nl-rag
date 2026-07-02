---
title: "PushManager - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PushManager
domain: push-api
license: CC-BY-SA-4.0
tags: push api, push subscription endpoint, push message delivery, web push protocol
fetched: 2026-07-02
---

# PushManager

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`PushManager`** interface of the Push API provides a way to receive notifications from third-party servers as well as request URLs for push notifications.

This interface is accessed via the `ServiceWorkerRegistration.pushManager` property.

## Static properties

**`PushManager.supportedContentEncodings`**

Returns an array of supported content codings that can be used to encrypt the payload of a push message.

## Instance methods

**`PushManager.getSubscription()`**

Retrieves an existing push subscription. It returns a `Promise` that resolves to a `PushSubscription` object containing details of an existing subscription. If no existing subscription exists, this resolves to a `null` value.

**`PushManager.permissionState()`**

Returns a `Promise` that resolves to the permission state of the current `PushManager`, which will be one of `'granted'`, `'denied'`, or `'prompt'`.

**`PushManager.subscribe()`**

Subscribes to a push service. It returns a `Promise` that resolves to a `PushSubscription` object containing details of a push subscription. A new push subscription is created if the current service worker does not have an existing subscription.

### Deprecated methods

**`PushManager.hasPermission()`**

Returns a `Promise` that resolves to the `PushPermissionStatus` of the requesting webapp, which will be one of `granted`, `denied`, or `default`. Replaced by `PushManager.permissionState()`.

**`PushManager.register()`**

Subscribes to a push subscription. Replaced by `PushManager.subscribe()`.

**`PushManager.registrations()`**

Retrieves existing push subscriptions. Replaced by `PushManager.getSubscription()`.

**`PushManager.unregister()`**

Unregisters and deletes a specified subscription endpoint. In the updated API, a subscription is unregistered by calling the `PushSubscription.unsubscribe()` method.

## Example

```js
this.onpush = (event) => {
  console.log(event.data);
  // From here we can write the data to IndexedDB, send it to any open
  // windows, display a notification, etc.
};

navigator.serviceWorker
  .register("serviceworker.js")
  .then((serviceWorkerRegistration) => {
    serviceWorkerRegistration.pushManager.subscribe().then(
      (pushSubscription) => {
        console.log(pushSubscription.endpoint);
        // The push subscription details needed by the application
        // server are now available, and can be sent to it using,
        // for example, the fetch() API.
      },
      (error) => {
        console.error(error);
      },
    );
  });
```

## Specifications

| Specification |
|---|
| Push API # pushmanager-interface |

## Browser compatibility
