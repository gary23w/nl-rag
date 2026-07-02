---
title: "Content negotiation"
source: https://en.wikipedia.org/wiki/Content_negotiation
domain: problem-details-rfc
license: CC-BY-SA-4.0
tags: problem details format, http api error format, machine-readable errors, error response schema
fetched: 2026-07-02
---

# Content negotiation

In computing, **content negotiation** refers to mechanisms defined as a part of HTTP that make it possible to serve different versions of a document (or more generally, representations of a resource) at the same URI, so that user agents can specify which version fits their capabilities the best. One classical use of this mechanism is to serve an image in GIF or PNG format, so that a browser that cannot display PNG images (e.g. MS Internet Explorer 4) will be served the GIF version.

A resource may be available in several different representations; for example, it might be available in different languages or different media types. One way of selecting the most appropriate choice is to give the user an index page and let them select the most appropriate choice; however it is often possible to automate the choice based on some selection criteria.

## Mechanisms

HTTP provides for several different content negotiation mechanisms including: server-driven (or proactive), agent-driven (or reactive), transparent, and/or hybrid combinations thereof.

### Server-driven

Server-driven or proactive content negotiation is performed by algorithms on the server which choose among the possible variant representations. This is commonly performed based on user agent-provided acceptance criteria.

To summarize how this works, when a user agent submits a request to a server, the user agent informs the server what media types or other aspects of content presentation it understands with ratings of how well it understands them. More precisely, the user agent provides HTTP headers that lists acceptable aspects of the resource and quality factors for them. The server is then able to supply the version of the resource that best fits the user agent's needs.

For example, a browser could indicate that it would like information in German by setting the `Accept-Language` like this:

`Accept-Language: de`

The browser may instead say that German is preferred, if possible, but that English is also acceptable by setting:

`Accept-Language: de; q=1.0, en; q=0.5`

Where the 'q' - quality - factor for German is higher than that for English.

Multiple HTTP headers are often supplied together for content format or, specifically media type, language and a few other aspects of a resource. In addition to the commonly used `Accept` header for Media Type, the `Accept-Language` header for language negotiation, RFC 7231 also describes `Accept-Charset` & `Accept-Encodings` for character encodings and content codings (compression) respectively.

An example of a more complex request is where a browser sends headers about language indicating German is preferred but that English is acceptable, as above, and that, regarding formats, HTML (`text/html`) is preferred over other text types (`text/*`), GIF (`image/gif`) or JPEG (`image/jpg`) images are preferred over other image formats (`image/*`) but that any other media type (`*/*`) is accepted as a last resort:

```mw
Accept-Language: de; q=1.0, en; q=0.5
Accept: text/html; q=1.0, text/*; q=0.8, image/gif; q=0.6, image/jpeg; q=0.6, image/*; q=0.5, */*; q=0.1
```

In addition to aspects of server-driven content negotiation by content type and by language specified in RFC 7231, there are extensions defining other aspects of content negotiation, such as *Memento* which describes use of a `Accept-Datetime` header to retrieve version of a resource's representation at particular points in time and the IETF/W3C's *Content Negotiation by Profile* which describes use of an `Accept-Profile` header to retrieve resource representations conforming to data profiles.

Neither RFC 7231 nor the more recent related specifications such as *Content Negotiation by Profile* specify how to resolve trade-offs in cases where different headers specify conflicting requirements, such as, in the above example, choosing between an HTML page in English and a GIF image in German.

### Agent-driven

Agent-driven or reactive content negotiation is performed by algorithms in the user-agent which choose among the possible variant representations. This is commonly performed based on a server provided list of representations and metadata about them.

To summarize how this works, when a user agent submits a request to a server, the server informs the user-agent which representations it has available as well as any metadata it has about each representation (e.g., content-type, quality, language, etc.). The user-agent then resubmits the request to a specific URL for the chosen representation. This can be automatically chosen by the user-agent or the user-agent can present the user with the choices and the user can directly choose such. More precisely, the server responds with either 300 Multiple Choices or 406 Not Acceptable (when server-driven, user-agent acceptance criteria are provided but the server cannot automatically make a selection). Unfortunately HTTP leaves the format of the list of representations and metadata along with selection mechanisms unspecified.
