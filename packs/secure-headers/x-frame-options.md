---
title: "List of HTTP header fields"
source: https://en.wikipedia.org/wiki/X-Frame-Options
domain: secure-headers
license: CC-BY-SA-4.0
tags: http security headers, response header hardening, referrer policy header, permissions policy header
fetched: 2026-07-02
---

# List of HTTP header fields

(Redirected from

X-Frame-Options

)

This article lists standard and notable non-standard HTTP header fields.

A core set of fields is standardized by the Internet Engineering Task Force (IETF) in RFC 9110 and 9111. The Field Names, Header Fields and Repository of Provisional Registrations are maintained by the IANA. Additional fields may be defined by a web application.

In the past, non-standard header field names were prefixed with `X-` but this convention was deprecated in June 2012 because of the inconveniences it caused when non-standard fields became standard. An earlier restriction on use of `Downgraded-` was lifted in March 2013.

A few field values can contain comments (i.e. in User-Agent, Server, Via fields), which can be ignored by software.

Many field values may contain a quality (*q*) key-value pair separated by equals sign, specifying a weight to use in content negotiation. For example, a browser may indicate that it accepts information in German or English, with German as preferred by setting the *q* value for `de` higher than that of `en`, as follows:

`Accept-Language: de; q=1.0, en; q=0.5`

## Request fields

This section lists header fields used in a request.

### Standard request fields

#### A-IM

[RFC 3229, permanent] Acceptable instance-manipulations for the request.

For example: `A-IM: feed`

#### Accept

[RFC 9110, permanent] Media type(s) that is/are acceptable for the response. See Content negotiation.

For example: `Accept: text/html`

#### Accept-Charset

[RFC 9110, permanent] Character sets that are acceptable.

For example: `Accept-Charset: utf-8`

#### Accept-Datetime

[RFC 7089, provisional] Acceptable version in time.

For example: `Accept-Datetime: Thu, 31 May 2007 20:35:00 GMT`

#### Accept-Encoding

[RFC 9110, permanent] List of acceptable encodings. See HTTP compression.

For example: `Accept-Encoding: gzip, deflate`

#### Accept-Language

[RFC 9110, permanent] List of acceptable human languages for response. See Content negotiation.

For example: `Accept-Language: en-US`

#### Access-Control-Request-Method, Access-Control-Request-Headers

[permanent] Initiates a request for cross-origin resource sharing with Origin (below).

For example: `Access-Control-Request-Method: GET`

#### Authorization

[RFC 9110, permanent] Authentication credentials for HTTP authentication.

For example: `Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

#### Cache-Control

[RFC 9111, permanent] Used to specify directives that *must* be obeyed by all caching mechanisms along the request-response chain. Per HTTP/1.1, the `no-cache` value allows the browser to tell the server and intermediate caches that it wants a fresh version of the resource. The HTTP/1.0, `Pragma: no-cache` header field has the same purpose.

The behavior of `Pragma: no-cache` in a *response* is not specified yet some user agents support it. HTTP/1.1 specifically warns against relying on this behavior.

For example: `Cache-Control: no-cache`

#### Connection

[RFC 9110, permanent] Control options for the current connection and list of hop-by-hop request fields. Must not be used with HTTP/2.

For example: `Connection: keep-alive` `Connection: Upgrade`

#### Content-Digest

[RFC 9530, Digest Fields] Content-Digest header enables verification of message content integrity by computing a digest over the literal bytes transmitted in the HTTP message. This digest reflects the content after applying transformations like Content-Encoding, matching exactly what travels across the network.

#### Content-Encoding

[RFC 9110, permanent] The type of encoding used on the data. See HTTP compression.

For example: `Content-Encoding: gzip`

#### Content-Length

[RFC 9110, permanent] The length of the request body in octets (8-bit bytes).

For example: `Content-Length: 348`

#### Content-MD5

[RFC 1544, 1864, 4021, obsolete] A Base64-encoded binary MD5 sum of the content of the request body.

For example: `Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`

#### Content-Type

[RFC 9110, permanent] The Media type of the body of the request (used with POST and PUT requests).

For example: `Content-Type: application/x-www-form-urlencoded`

[RFC 2965, 6265, permanent] An HTTP cookie previously sent by the server with `Set-Cookie` (below).

For example: `Cookie: $Version=1; Skin=new;`

#### Date

[RFC 9110, permanent] The date and time at which the message was originated (in "HTTP-date" format as defined by RFC 9110: HTTP Semantics, section 5.6.7 "Date/Time Formats").

For example: `Date: Tue, 15 Nov 1994 08:12:31 GMT`

#### Expect

[RFC 9110, permanent] Indicates that particular server behaviors are required by the client.

For example: `Expect: 100-continue`

#### Forwarded

[RFC 7239, permanent] Disclose original information of a client connecting to a web server through an HTTP proxy.

For example: `Forwarded: for=192.0.2.60;proto=http;by=203.0.113.43` `Forwarded: for=192.0.2.43, for=198.51.100.17`

#### From

[RFC 9110, permanent] The email address of the user making the request.

For example: `From: user@example.com`

#### Host

[RFC 9110, 9113, permanent] The domain name of the server (for virtual hosting), and the TCP port number on which the server is listening. The port number may be omitted if the port is the standard port for the service requested. Mandatory since HTTP/1.1. If the request is generated directly in HTTP/2, it should not be used.

For example: `Host: en.wikipedia.org:8080` `Host: en.wikipedia.org`

#### HTTP2-Settings

[RFC 7540, 9113, obsolete] A request that upgrades from HTTP/1.1 to HTTP/2 MUST include exactly one `HTTP2-Settings` header field. The `HTTP2-Settings` header field is a connection-specific header field that includes parameters that govern the HTTP/2 connection, provided in anticipation of the server accepting the request to upgrade.

For example: `HTTP2-Settings: token64`

#### If-Match

[RFC 9110, permanent] Only perform the action if the client supplied entity matches the same entity on the server. This is mainly for methods like PUT to only update a resource if it has not been modified since the user last updated it.

For example: `If-Match: "737060cd8c284d8af7ad3082f209582d"`

#### If-Modified-Since

[RFC 9110, permanent] Allows a *304 Not Modified* to be returned if content is unchanged.

For example: `If-Modified-Since: Sat, 29 Oct 1994 19:43:31 GMT`

#### If-None-Match

[RFC 9110, permanent] Allows a *304 Not Modified* to be returned if content is unchanged, see HTTP ETag.

For example: `If-None-Match: "737060cd8c284d8af7ad3082f209582d"`

#### If-Range

[RFC 9110, permanent] If the entity is unchanged, send me the part(s) that I am missing; otherwise, send me the entire new entity.

For example: `If-Range: "737060cd8c284d8af7ad3082f209582d"`

#### If-Unmodified-Since

[RFC 9110, permanent] Only send the response if the entity has not been modified since a specific time.

For example: `If-Unmodified-Since: Sat, 29 Oct 1994 19:43:31 GMT`

#### Max-Forwards

[RFC 9110, permanent] Limit the number of times the message can be forwarded through proxies or gateways.

For example: `Max-Forwards: 10`

#### Origin

[RFC 6454, permanent] Initiates a request for cross-origin resource sharing (asks server for Access-Control-* response fields).

For example: `Origin: http://www.example-social-network.com`

#### Pragma

[RFC 9111, outdated] Implementation-specific fields that may have various effects anywhere along the request-response chain.

For example: `Pragma: no-cache`

#### Prefer

[RFC 7240, permanent] Allows client to request that certain behaviors be employed by a server while processing a request.

For example: `Prefer: return=representation`

#### Proxy-Authorization

[RFC 9110, permanent] Authorization credentials for connecting to a proxy.

For example: `Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

#### Range

[RFC 9110, permanent] Request only part of an entity. Bytes are numbered from 0. See Byte serving.

For example: `Range: bytes=500-999`

#### Referer [*sic*]

[RFC 9110, permanent] The address of the previous web page from which a link to the currently requested page was followed.

Although the intended term is actually spelled "referrer", the misspelling is in the RFC as well as in most implementations, and is therefore considered correct terminology.

For example: `Referer: http://en.wikipedia.org/wiki/Main_Page`

#### TE

[RFC 9110, permanent] The transfer encodings the user agent is willing to accept: the same values as for the response header field Transfer-Encoding can be used, plus the "trailers" value (related to the "chunked" transfer method) to notify the server it expects to receive additional fields in the trailer after the last, zero-sized, chunk. Only `trailers` is supported in HTTP/2.

For example: `TE: trailers, deflate`

#### Trailer

[RFC 9110, permanent] The Trailer general field value indicates that the given set of header fields is present in the trailer of a message encoded with chunked transfer coding.

For example: `Trailer: Max-Forwards`

#### Transfer-Encoding

[RFC 9110, permanent] The form of encoding used to safely transfer the entity to the user. Currently defined methods are: chunked, compress, deflate, gzip, identity. Must not be used with HTTP/2.

For example: `Transfer-Encoding: chunked`

#### User-Agent

[RFC 9110, permanent] The user agent string of the user agent.

For example: `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0`

#### Upgrade

[RFC 9110, permanent] Ask the server to upgrade to another protocol. Must not be used in HTTP/2.

For example: `Upgrade: h2c, HTTPS/1.3, IRC/6.9, RTA/x11, websocket`

#### Via

[RFC 9110, permanent] Informs the server of proxies through which the request was sent.

For example: `Via: 1.0 fred, 1.1 example.com (Apache/1.1)`

#### Warning

[RFC 7234, 9111, obsolete] A warning about a possible problem with the entity body. Since this header is often neither sent by servers nor acknowledged by clients, this header and its codes were obsoleted by the HTTP Working Group in 2022 with RFC 9111.

The following caching related warning codes were specified under RFC 7234.

**110 Response is Stale**

The response provided by a cache is stale (the content's age exceeds a maximum age set by a Cache-Control header or heuristically chosen lifetime).

**111 Revalidation Failed**

The cache was unable to validate the response, due to an inability to reach the origin server.

**112 Disconnected Operation**

The cache is intentionally disconnected from the rest of the network.

**113 Heuristic Expiration**

The cache heuristically chose a freshness lifetime greater than 24 hours and the response's age is greater than 24 hours.

**199 Miscellaneous Warning**

Arbitrary, non-specific warning. The warning text may be logged or presented to the user.

**214 Transformation Applied**

Added by a proxy if it applies any transformation to the representation, such as changing the content encoding, media type or the like.

**299 Miscellaneous Persistent Warning**

Same as 199, but indicating a persistent warning.

For example: `Warning: 199 Miscellaneous warning`

### Common non-standard request fields

#### Upgrade-Insecure-Requests

Tells a server which (presumably in the middle of a HTTP -> HTTPS migration) hosts mixed content that the client would prefer redirection to HTTPS and can handle `Content-Security-Policy: upgrade-insecure-requests`

For example: `Upgrade-Insecure-Requests: 1`

#### X-Requested-With

Mainly used to identify Ajax requests (most JavaScript frameworks send this field with value of `XMLHttpRequest`); this also identifies Android apps using WebView.

For example: `X-Requested-With: XMLHttpRequest`

#### DNT

Requests a web application to disable their tracking of a user. This is Mozilla's version of the X-Do-Not-Track header field (since Firefox 4.0 Beta 11). Safari and IE9 also have support for this field. On March 7, 2011, a draft proposal was submitted to IETF. The W3C Tracking Protection Working Group is producing a specification.

For example:

`DNT: 1` (Do Not Track Enabled)

`DNT: 0` (Do Not Track Disabled)

#### X-Forwarded-For

A *de facto* standard for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer. Superseded by *Forwarded* header.

For example: `X-Forwarded-For: client1, proxy1, proxy2` `X-Forwarded-For: 129.78.138.66, 129.78.64.103`

#### X-Forwarded-Host

A *de facto* standard for identifying the original host requested by the client in the `Host` HTTP request header, since the host name and/or port of the reverse proxy (load balancer) may differ from the origin server handling the request. Superseded by *Forwarded* header.

For example:

`X-Forwarded-Host: en.wikipedia.org:8080`

`X-Forwarded-Host: en.wikipedia.org`

#### X-Forwarded-Proto

A *de facto* standard for identifying the originating protocol of an HTTP request, since a reverse proxy (or a load balancer) may communicate with a web server using HTTP even if the request to the reverse proxy is HTTPS. An alternative form of the header (X-ProxyUser-Ip) is used by Google clients talking to Google servers. Superseded by *Forwarded* header.

For example: `X-Forwarded-Proto: https`

#### Front-End-Https

Non-standard header field used by Microsoft applications and load-balancers.

For example: `Front-End-Https: on`

#### X-Http-Method-Override

Requests a web application to override the method specified in the request (typically POST) with the method given in the header field (typically PUT or DELETE). This can be used when a user agent or firewall prevents PUT or DELETE methods from being sent directly (this is either a bug in the software component, which ought to be fixed, or an intentional configuration, in which case bypassing it may be the wrong thing to do).

For example: `X-HTTP-Method-Override: DELETE`

#### X-ATT-DeviceId

Allows easier parsing of the MakeModel/Firmware that is usually found in the User-Agent String of AT&T Devices.

For example: `X-Att-Deviceid: GT-P7320/P7320XXLPG`

#### X-Wap-Profile

Links to an XML file on the Internet with a full description and details about the device currently connecting. In the example to the right is an XML file for an AT&T Samsung Galaxy S2.

For example: `x-wap-profile: http://wap.samsungmobile.com/uaprof/SGH-I777.xml`

#### Proxy-Connection

Implemented as a misunderstanding of the HTTP specifications. Common because of mistakes in implementations of early HTTP versions. Has exactly the same functionality as standard Connection field. Must not be used with HTTP/2.

For example: `Proxy-Connection: keep-alive`

#### X-UIDH

Server-side deep packet inspection of a unique ID identifying customers of Verizon Wireless; also known as "perma-cookie" or "supercookie".

For example: `X-UIDH: ...`

#### X-Csrf-Token

Used to prevent cross-site request forgery. Alternative header names are: `X-CSRFToken` and `X-XSRF-TOKEN`.

For example: `X-Csrf-Token: i8XNjC4b8KVok4uw5RftR38Wgp2BFwql`

#### X-Request-ID, X-Correlation-ID, Correlation-ID

Correlates HTTP requests between a client and server. Superseded by the traceparent header.

For example: `X-Request-ID: f058ebd6-02f7-4d3f-942e-904344e8cde5`

#### Save-Data

The Save-Data client hint request header available in Chrome, Opera, and Yandex browsers lets developers deliver lighter, faster applications to users who opt-in to data saving mode in their browser.

For example: `Save-Data: on`

#### Sec-GPC

The Sec-GPC (Global Privacy Control) request header indicates whether the user consents to a website or service selling or sharing their personal information with third parties.

For example: `Sec-GPC: 1`

## Response fields

This section lists header fields used in a response.

### Standard response fields

#### Accept-CH

[RFC 8942, experimental] Requests HTTP Client Hints.

For example: `Accept-CH: UA, Platform`

#### Access-Control-Allow-Origin, Access-Control-Allow-Credentials, Access-Control-Expose-Headers, Access-Control-Max-Age, Access-Control-Allow-Methods, Access-Control-Allow-Headers

[RFC 7480, permanent] Specifying which web sites can participate in cross-origin resource sharing.

For example: `Access-Control-Allow-Origin: *`

#### Accept-Patch

[RFC 5789, permanent] Specifies which patch document formats this server supports.

For example: `Accept-Patch: text/example;charset=utf-8`

#### Accept-Ranges

[RFC 9110, permanent] What partial content range types this server supports via byte serving.

For example: `Accept-Ranges: bytes`

#### Age

[RFC 9111, permanent] The age the object has been in a proxy cache in seconds.

For example: `Age: 12`

#### Allow

[RFC 9110, permanent] Valid methods for a specified resource. To be used for a *405 Method not allowed*.

For example: `Allow: GET, HEAD`

#### Alt-Svc

[RFC 7838, permanent] A server uses "Alt-Svc" header (meaning Alternative Services) to indicate that its resources can also be accessed at a different network location (host or port) or using a different protocol. When using HTTP/2, servers should instead send an ALTSVC frame.

For example: `Alt-Svc: http/1.1="http2.example.com:8001"; ma=7200`

#### Cache-Control

[RFC 9111, permanent] Tells all caching mechanisms from server to client whether they may cache the response. A numeric value is in seconds.

If a web server responds with `Cache-Control: no-cache`, then a web browser or other caching system (intermediate proxies) must not use the response to satisfy subsequent requests without first checking with the originating server (this process is called validation). This header field is part of HTTP/1.1, and is ignored by some caches and browsers. It may be simulated by setting the `Expires` HTTP/1.0 header field value to a time earlier than the response time. Notice that `no-cache` is not instructing the browser or proxies about whether or not to cache the content. It tells the browser and proxies to validate the cache content with the server before using it (this is done via `If-Modified-Since`, `If-Unmodified-Since`, `If-Match`, and `If-None-Match`). Sending a `no-cache` value thus instructs a browser or proxy to not use the cache contents merely based on "freshness criteria" of the cache content. Another common way to prevent old content from being shown to the user without validation is `Cache-Control: max-age=0` which instructs the user agent that the content is stale and should be validated before use.

The value `no-store` instructs a browser to *not* cache the response, yet the browser is allowed to cache it none-the-less. In particular, the HTTP/1.1 definition draws a distinction between history stores and caches. If the user navigates back to a previous page, a browser may show a page that was stored on disk in the history store. This is correct behavior according to the specification. Many user agents provide different behavior in loading pages from the history store or cache depending on whether the protocol is HTTP or HTTPS.

For example: `Cache-Control: max-age=3600`

#### Connection

[RFC 9110, permanent] Control options for the current connection and list of hop-by-hop response fields. Must not be used with HTTP/2.

For example: `Connection: close`

#### Content-Disposition

[RFC 2616, 4021, 6266, permanent] An opportunity to raise a "File Download" dialogue box for a known MIME type with binary format or suggest a filename for dynamic content. Quotes are necessary with special characters.

For example: `Content-Disposition: attachment; filename="fname.ext"`

#### Content-Encoding

[RFC 9110, permanent] The type of encoding used on the data. See HTTP compression.

For example: `Content-Encoding: gzip`

#### Content-Language

[RFC 9110, permanent] The natural language or languages of the intended audience for the enclosed content.

For example: `Content-Language: da`

#### Content-Length

[RFC 9110, permanent] The length of the response body in octets (8-bit bytes).

For example: `Content-Length: 348`

#### Content-Location

[RFC 9110, permanent] An alternate location for the returned data.

For example: `Content-Location: /index.htm`

#### Content-MD5

[RFC 1544, 1864, 4021, obsolete] A Base64-encoded binary MD5 sum of the content of the response.

For example: `Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`

#### Content-Range

[RFC 9110, permanent] Where in a full body message this partial message belongs.

For example: `Content-Range: bytes 21010-47021/47022`

#### Content-Type

[RFC 9110, permanent] The MIME type of this content.

For example: `Content-Type: text/html; charset=utf-8`

#### Date

[RFC 9110, permanent] The date and time that the message was sent (in "HTTP-date" format as defined by RFC 9110).

For example: `Date: Tue, 15 Nov 1994 08:12:31 GMT`

#### Delta-Base

[RFC 3229, permanent] Specifies the delta-encoding entity tag of the response.

For example: `Delta-Base: "abc"`

#### ETag

[RFC 9110, permanent] An identifier for a specific version of a resource, often a message digest.

For example: `ETag: "737060cd8c284d8af7ad3082f209582d"`

#### Expires

[RFC 9111, permanent] Gives the date/time after which the response is considered stale (in "HTTP-date" format as defined by RFC 9110).

For example: `Expires: Thu, 01 Dec 1994 16:00:00 GMT`

#### IM

[RFC 3229, permanent] Instance-manipulations applied to the response.

For example: `IM: feed`

#### Last-Modified

[RFC 9110, permanent] The last modified date for the requested object (in "HTTP-date" format as defined by RFC 9110).

For example: `Last-Modified: Tue, 15 Nov 1994 12:45:26 GMT`

#### Link

[RFC 8288, permanent] Used to express a typed relationship with another resource, where the relation type is defined by RFC 8288.

For example: `Link: </feed>; rel="alternate"`

#### Location

[RFC 9110, permanent] Used in redirection, or when a new resource has been created.

For example: `Location: http://www.w3.org/pub/WWW/People.html`

For example: `Location: /pub/WWW/People.html`

#### P3P

[RFC 2626, permanent] This field is supposed to set P3P policy, in the form of `P3P:CP="your_compact_policy"`. However, P3P did not take off, most browsers have never fully implemented it; a lot of websites set this field with fake policy text, enough to fool browsers into thinking a P3P policy existed and granting permissions for third party cookies.

For example: `P3P: CP="This is not a P3P policy! See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."`

#### Pragma

[RFC 9111, permanent] Implementation-specific fields that may have various effects anywhere along the request-response chain.

For example: `Pragma: no-cache`

#### Preference-Applied

[RFC 7240, permanent] Indicates which Prefer tokens were honored by the server and applied to the processing of the request.

For example: `Preference-Applied: return=representation`

#### Proxy-Authenticate

[RFC 9110, permanent] Request authentication to access the proxy.

For example: `Proxy-Authenticate: Basic`

#### Public-Key-Pins

[RFC 7469, permanent] HTTP Public Key Pinning, announces hash of website's authentic TLS certificate.

For example: `Public-Key-Pins: max-age=2592000; pin-sha256="E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g=";`

#### Retry-After

[RFC 9110, permanent] If an entity is temporarily unavailable, this instructs the client to try again later. Value could be a specified period of time (in seconds) or a HTTP-date.

For example 1: `Retry-After: 120` For example 2: `Retry-After: Fri, 07 Nov 2014 23:59:59 GMT`

#### Server

[RFC 9110, permanent] A name for the server.

For example: `Server: Apache/2.4.1 (Unix)`

[RFC 6265, permanent] An HTTP cookie.

For example: `Set-Cookie: CookieName=CookieValue; Max-Age=3600; Version=1`

#### Strict-Transport-Security

[RFC 6797, permanent] A HSTS Policy informing the HTTP client how long to cache the HTTPS-only policy and whether this applies to subdomains.

For example: `Strict-Transport-Security: max-age=16070400; includeSubDomains`

#### Trailer

[RFC 9110, permanent] The Trailer general field value indicates that the given set of header fields is present in the trailer of a message encoded with chunked transfer coding.

For example: `Trailer: Max-Forwards`

#### Transfer-Encoding

[RFC 9110, permanent] The form of encoding used to safely transfer the entity to the user. Currently defined methods are: chunked, compress, deflate, gzip, identity. Must not be used with HTTP/2.

For example: `Transfer-Encoding: chunked`

#### Tk

[RFC 2295, permanent] Tracking Status header, value suggested to be sent in response to a DNT (do-not-track) request. Possible values:

- "!" — under construction
- "?" — dynamic
- "G" — gateway to multiple parties
- "N" — not tracking
- "T" — tracking
- "C" — tracking with consent
- "P" — tracking only if consented
- "D" — disregarding DNT
- "U" — updated

For example: `Tk: ?`

#### Upgrade

[RFC 9110, permanent] Ask the client to upgrade to another protocol. Must not be used in HTTP/2.

For example: `Upgrade: h2c, HTTPS/1.3, IRC/6.9, RTA/x11, websocket`

#### Vary

[RFC 9110, permanent] Tells downstream proxies how to match future request headers to decide whether the cached response can be used rather than requesting a fresh one from the origin server.

For example 1: `Vary: *` For example 2: `Vary: Accept-Language`

#### Via

[RFC 9110, permanent] Informs the client of proxies through which the response was sent.

For example: `Via: 1.0 fred, 1.1 example.com (Apache/1.1)`

#### Warning

[RFC 7234, RFC 9111, obsolete] A general warning about possible problems with the entity body.

For example: `Warning: 199 Miscellaneous warning`

#### WWW-Authenticate

[RFC 9110, permanent] Indicates the authentication scheme that should be used to access the requested entity.

For example: `WWW-Authenticate: Basic`

#### X-Frame-Options

[RFC 7034, obsolete] Clickjacking protection: `deny` - no rendering within a frame, `sameorigin` - no rendering if origin mismatch, `allow-from` - allow from specified location, `allowall` - non-standard, allow from any location.

For example: `X-Frame-Options: deny`

### Common non-standard response fields

#### Content-Security-Policy, X-Content-Security-Policy, X-WebKit-CSP

Content Security Policy definition.

For example: `X-WebKit-CSP: default-src 'self'`

#### Expect-CT

Notify to prefer to enforce Certificate Transparency.

For example: `Expect-CT: max-age=604800, enforce, report-uri="https://example.example/report"`

#### NEL

Used to configure network request logging.

For example: `NEL: { "report_to": "name_of_reporting_group", "max_age": 12345, "include_subdomains": false, "success_fraction": 0.0, "failure_fraction": 1.0 }`

#### Permissions-Policy

To allow or disable different features or APIs of the browser.

For example: `Permissions-Policy: fullscreen=(), camera=(), microphone=(), geolocation=(), interest-cohort=()`

#### Refresh

Tells the browser to refresh the page or redirect to a different URL, either after a given number of seconds (`0` meaning immediately), or when a new resource has been created. Introduced by Netscape in 1995 and has since become a de facto standard supported by most web browsers. Was eventually standardized in the HTML Living Standard in 2017.

For example: `Refresh: 5; url=http://www.w3.org/pub/WWW/People.html`

#### Report-To

Instructs the user agent to store reporting endpoints for an origin.

For example: `Report-To: { "group": "csp-endpoint", "max_age": 10886400, "endpoints": [ { "url": "https-url-of-site-which-collects-reports" } ] }`

#### Status

CGI header field specifying the status of the HTTP response. Normal HTTP responses use a separate "Status-Line" instead, defined by RFC 9110.

For example: `Status: 200 OK`

#### Timing-Allow-Origin

The `Timing-Allow-Origin` response header specifies origins that are allowed to see values of attributes retrieved via features of the Resource Timing API, which would otherwise be reported as zero due to cross-origin restrictions.

For example: `Timing-Allow-Origin: *` `Timing-Allow-Origin: <origin>[, <origin>]*`

#### X-Content-Duration

Provide the duration of the audio or video in seconds. Not supported by current browsers – the header was only supported by Gecko browsers, from which support was removed in 2015.

For example: `X-Content-Duration: 42.666`

#### X-Content-Type-Options

The only defined value, "nosniff", prevents Internet Explorer from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome, when downloading extensions.

For example: `X-Content-Type-Options: nosniff`

#### X-Powered-By

Specifies the technology (e.g. ASP.NET, PHP, JBoss) supporting the web application (version details are often in `X-Runtime`, `X-Version`, or `X-AspNet-Version`).

For example: `X-Powered-By: PHP/5.4.0`

#### X-Redirect-By

Specifies the component that is responsible for a particular redirect.

For example: `X-Redirect-By: WordPress` `X-Redirect-By: Polylang`

#### X-Request-ID, X-Correlation-ID

Correlates HTTP requests between a client and server.

For example: `X-Request-ID: f058ebd6-02f7-4d3f-942e-904344e8cde5`

#### X-UA-Compatible

Recommends the preferred rendering engine (often a backward-compatibility mode) to use to display the content. Also used to activate Chrome Frame in Internet Explorer. In HTML Standard, only the `IE=edge` value is defined.

For example:

`X-UA-Compatible: IE=edge` `X-UA-Compatible: IE=EmulateIE7` `X-UA-Compatible: Chrome=1`

#### X-XSS-Protection

Cross-site scripting (XSS) filter

For example: `X-XSS-Protection: 1; mode=block`
