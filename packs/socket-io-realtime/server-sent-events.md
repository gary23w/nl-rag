---
title: "Server-sent events"
source: https://en.wikipedia.org/wiki/Server-sent_events
domain: socket-io-realtime
license: CC-BY-SA-4.0
tags: socket.io realtime, bidirectional event messaging, realtime websocket rooms, event emitter transport
fetched: 2026-07-02
---

# Server-sent events

**Server-Sent Events** (**SSE**) is a server push technology enabling a client to receive automatic updates from a server via an HTTP connection, and describes how servers can initiate data transmission towards clients once an initial client connection has been established. They are commonly used to send message updates or continuous data streams to a browser client and designed to enhance native, cross-browser streaming through a JavaScript API called EventSource, through which a client requests a particular URL in order to receive an event stream. The EventSource API is standardized as part of HTML Living Standard by the WHATWG. The media type for SSE is `text/event-stream`.

All modern browsers support server-sent events: Firefox 6+, Google Chrome 6+, Opera 11.5+, Safari 5+, Microsoft Edge 79+, Brave. Since SSE does not use either persistent connections nor chunked transfer encoding, HTTP/1.1 is not a technical requirement.

## History

The SSE mechanism was first specified by Ian Hickson as part of the "WHATWG Web Applications 1.0" proposal starting in 2004. In September 2006, the Opera web browser implemented the experimental technology in a feature called "Server-Sent Events".

The W3C published Server-Sent Events as a Recommendation on February 3, 2015, after years of development through Working Drafts and Candidate Recommendations.

## Example

```mw
var source = new EventSource('updates.cgi');
source.onmessage = function (event) {
  alert(event.data);
};
```

## Technology

When sending high-frequency data , the server must manage backpressure to prevent saturating clients. This is mitigated in the following ways:

- Client-side buffering: Browsers have limited buffer space for incoming server-sent events
- Adaptive rate limiting: Servers can adjust event frequency and monitor connection health
- Event batching: Combining multiple events into larger and less frequent transmissions
