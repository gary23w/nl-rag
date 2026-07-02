---
title: "ServiceWorkerRegistration: pushManager property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/pushManager
domain: push-api
license: CC-BY-SA-4.0
tags: push api, push subscription endpoint, push message delivery, web push protocol
fetched: 2026-07-02
---

# ServiceWorkerRegistration: pushManager property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`pushManager`** read-only property of the `ServiceWorkerRegistration` interface returns a reference to the `PushManager` interface for managing push subscriptions; this includes support for subscribing, getting an active subscription, and accessing push permission status.

## Value

A `PushManager` object.

## Examples

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
        console.log(pushSubscription.subscriptionId);
        console.log(pushSubscription.endpoint);
        // The push subscription details needed by the application
        // server are now available, and can be sent to it using,
        // for example, the fetch() API.
      },
      (error) => {
        // During development it often helps to log errors to the
        // console. In a production environment it might make sense to
        // also report information about errors back to the
        // application server.
        console.error(error);
      },
    );
  });
```

## Specifications

| Specification |
|---|
| Push API # dom-serviceworkerregistration-pushmanager |

## Browser compatibility
