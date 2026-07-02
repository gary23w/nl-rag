---
title: "Clients - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Clients
domain: service-workers
license: CC-BY-SA-2.5
tags: service worker, offline caching, cache storage api, background sync
fetched: 2026-07-02
---

# Clients

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2018.

- Learn more
- See full compatibility

**Note:** This feature is only available in Service Workers.

The `Clients` interface provides access to `Client` objects. Access it via `self`.clients within a service worker.

## Instance methods

**`Clients.get()`**

Returns a `Promise` for a `Client` matching a given `id`.

**`Clients.matchAll()`**

Returns a `Promise` for an array of `Client` objects. An options argument allows you to control the types of clients returned.

**`Clients.openWindow()`**

Opens a new browser window for a given URL and returns a `Promise` for the new `WindowClient`.

**`Clients.claim()`**

Allows an active service worker to set itself as the `controller` for all clients within its `scope`.

## Examples

The following example shows an existing chat window or creates a new one when the user clicks a notification.

```js
addEventListener("notificationclick", (event) => {
  event.waitUntil(
    (async () => {
      const allClients = await clients.matchAll({
        includeUncontrolled: true,
      });

      let chatClient;

      // Let's see if we already have a chat window open:
      for (const client of allClients) {
        const url = new URL(client.url);

        if (url.pathname === "/chat/") {
          // Excellent, let's use it!
          client.focus();
          chatClient = client;
          break;
        }
      }

      // If we didn't find an existing chat window,
      // open a new one:
      chatClient ??= await clients.openWindow("/chat/");

      // Message the client:
      chatClient.postMessage("New chat messages!");
    })(),
  );
});
```

## Specifications

| Specification |
|---|
| Service Workers Nightly # clients-interface |

## Browser compatibility
