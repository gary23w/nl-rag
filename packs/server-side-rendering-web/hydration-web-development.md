---
title: "Hydration (web development)"
source: https://en.wikipedia.org/wiki/Hydration_(web_development)
domain: server-side-rendering-web
license: CC-BY-SA-4.0
tags: server side rendering, client side hydration, dynamic web page, server-side scripting
fetched: 2026-07-02
---

# Hydration (web development)

In web development, **hydration** or **rehydration** is a technique in which client-side JavaScript converts a web page that is static from the perspective of the web browser, delivered either through static rendering or server-side rendering, into a dynamic web page by attaching event handlers to the HTML elements in the DOM. Because the HTML is pre-rendered on a server, this allows for a fast "first contentful paint" (when useful data is first displayed to the user), but there is a period of time afterward where the page appears to be fully loaded and interactive, but is not until the client-side JavaScript is executed and event handlers have been attached.

Frameworks that use hydration include Next.js and Nuxt. React v16.0 introduced a "hydrate" function, which hydrates an element, in its API.

## Variations

### Streaming server-side rendering

*Streaming server-side rendering* allows one to send HTML in chunks that the browser can progressively render as it is received. This can provide a fast first paint and first contentful paint as HTML markup arrives to users faster.

### Progressive rehydration

In *progressive rehydration*, individual pieces of a server-rendered application are “booted up” over time, rather than the current common approach of initializing the entire application at once. This can help reduce the amount of JavaScript required to make pages interactive, since client-side upgrading of low priority parts of the page can be deferred to prevent blocking the main thread. It can also help avoid one of the most common server-side rendering rehydration pitfalls, where a server-rendered DOM tree gets destroyed and then immediately rebuilt – most often because the initial synchronous client-side render required data that wasn't quite ready, perhaps awaiting Promise resolution.

### Partial rehydration

*Partial rehydration* has proven difficult to implement. This approach is an extension of the idea of progressive rehydration, where the individual pieces (components/views/trees) to be progressively rehydrated are analyzed and those with little interactivity or no reactivity are identified. For each of these mostly-static parts, the corresponding JavaScript code is then transformed into inert references and decorative functionality, reducing their client-side footprint to near-zero. The partial hydration approach comes with its own issues and compromises. It poses some interesting challenges for caching, and client-side navigation means it cannot be assumed that server-rendered HTML for inert parts of the application will be available without a full page load.

One framework that supports partial rehydration is Elder.js, which is based on Svelte.

### Trisomorphic rendering

*Trisomorphic rendering* is a technique which uses streaming server-side rendering for initial/non-JavaScript navigations, and then uses service workers to take on rendering of HTML for navigations after it has been installed. This can keep cached components and templates up to date and enables SPA-style navigations for rendering new views in the same session. This approach works best when one can share the same templating and routing code between the server, client page, and service worker.
