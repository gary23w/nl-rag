---
title: "Notification: permission static property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Notification/permission_static
domain: notifications-api
license: CC-BY-SA-4.0
tags: notifications api, desktop notification permission, notification event handling, system notification banner
fetched: 2026-07-02
---

# Notification: permission static property

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`permission`** read-only static property of the `Notification` interface indicates the current permission granted by the user for the current origin to display web notifications.

## Value

A string representing the current permission. The value can be:

**`granted`**

The user has explicitly granted permission for the current origin to display system notifications.

**`denied`**

The user has explicitly denied permission for the current origin to display system notifications.

**`default`**

The user decision is unknown; in this case the application will act as if permission was `denied`.

## Examples

The following snippet could be used if you wanted to first check whether notifications are supported, then check if permission has been granted for the current origin to send notifications, then request permission if required, before then sending a notification.

```js
function notifyMe() {
  if (!("Notification" in window)) {
    // Check if the browser supports notifications
    alert("This browser does not support desktop notification");
  } else if (Notification.permission === "granted") {
    // Check whether notification permissions have already been granted;
    // if so, create a notification
    const notification = new Notification("Hi there!");
    // …
  } else if (Notification.permission !== "denied") {
    // We need to ask the user for permission
    Notification.requestPermission().then((permission) => {
      // If the user accepts, let's create a notification
      if (permission === "granted") {
        const notification = new Notification("Hi there!");
        // …
      }
    });
  }

  // At last, if the user has denied notifications, and you
  // want to be respectful there is no need to bother them anymore.
}
```

## Specifications

| Specification |
|---|
| Notifications API # dom-notification-permission |

## Browser compatibility
