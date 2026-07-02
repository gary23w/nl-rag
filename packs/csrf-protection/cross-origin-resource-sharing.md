---
title: "Cross-origin resource sharing"
source: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
domain: csrf-protection
license: CC-BY-SA-4.0
tags: csrf protection, cross-site request forgery, same-origin policy, anti-forgery token
fetched: 2026-07-02
---

# Cross-origin resource sharing

In computing, **cross-origin resource sharing** (**CORS**) is a mechanism to safely bypass the same-origin policy; that is, it allows a web page to access restricted resources from a web server on a domain name different from the domain that served the web page.

A web page may freely embed cross-origin images, stylesheets, scripts, iframes, and videos. Certain "cross-domain" HTTP requests, notably Ajax requests, are forbidden by default by the same-origin security policy. CORS defines a way in which a web browser and server can interact to determine whether it is safe to allow the cross-origin request. It allows for more freedom and functionality than purely same-origin requests, but is more secure than simply allowing all cross-origin requests.

The specification for CORS is included as part of the WHATWG's Fetch Living Standard. This specification describes how CORS is currently implemented in browsers. An earlier specification was published as a W3C Recommendation.

## Technical overview

For HTTP requests made from JavaScript that can't be made by using a <form> tag pointing to another domain or containing non-safelisted headers, the specification mandates that browsers "preflight" the request, soliciting supported methods from the server with an HTTP OPTIONS request method, and then, upon "approval" from the server, sending the actual request with the actual HTTP request method. Servers can also notify clients whether "credentials" (including Cookies and HTTP Authentication data) should be sent with requests.

## Simple request example

Suppose a user visits http://www.example.com and the page attempts a cross-origin request to fetch data from http://service.example.com. A CORS-compatible browser will attempt to make a cross-origin request to service.example.com as follows.

1. The browser sends the GET request with an extra `Origin` HTTP header to service.example.com containing the domain that served the parent page:
  ```
Origin: http://www.example.com
  ```
2. The server at service.example.com sends one of these three responses:
  - The requested data along with an `Access-Control-Allow-Origin` (ACAO) header in its response indicating the requests from the origin are allowed. For example in this case it should be:
    ```
Access-Control-Allow-Origin: http://www.example.com
    ```
  - The requested data along with an `Access-Control-Allow-Origin` (ACAO) header with a wildcard indicating that the requests from all domains are allowed:
    ```
Access-Control-Allow-Origin: *
    ```
  - An error page if the server does not allow a cross-origin request

A wildcard same-origin policy is appropriate when a page or API response is intended to be accessible to any code on any site. A freely available web font on a public hosting service like Google Fonts is an example.

The value of "*" is special in that it does not allow requests to supply credentials, meaning that it does not allow HTTP authentication, client-side SSL certificates, or cookies to be sent in the cross-domain request.

Note that in the CORS architecture, the Access-Control-Allow-Origin header is being set by the external web service (*service.example.com*), not the original web application server (*www.example.com*). Here, *service.example.com* uses CORS to permit the browser to authorize *www.example.com* to make requests to *service.example.com*.

If a site specifies the header "Access-Control-Allow-Credentials:true", third-party sites may be able to carry out privileged actions and retrieve sensitive information.

## Preflight example

When performing certain types of cross-domain Ajax requests, modern browsers that support CORS will initiate an extra "preflight" request to determine whether they have permission to perform the action. Cross-origin requests are preflighted this way because they may have implications to user data.

```
OPTIONS /
Host: service.example.com
Origin: http://www.example.com
Access-Control-Request-Method: PUT
```

If service.example.com is willing to accept the action, it may respond with the following headers:

```
Access-Control-Allow-Origin: http://www.example.com
Access-Control-Allow-Methods: PUT
```

The browser will then make the actual request. If service.example.com does not accept cross-site requests from this origin then it will respond with error to the OPTIONS request and the browser will not make the actual request.

## Headers

The HTTP headers that relate to CORS are:

### Request headers

- `Origin`
- `Host`
- `Access-Control-Request-Method`
- `Access-Control-Request-Headers`

### Response headers

- `Access-Control-Allow-Origin`
- `Access-Control-Allow-Credentials`
- `Access-Control-Expose-Headers`
- `Access-Control-Max-Age`
- `Access-Control-Allow-Methods`
- `Access-Control-Allow-Headers`

## Browser support

CORS is supported by all browsers based on the following layout engines:

- Blink- and Chromium-based browsers (Chrome 28+, Opera 15+, Amazon Silk, Android's 4.4+ WebView and Qt's WebEngine)
- Gecko 1.9.1 (Firefox 3.5, SeaMonkey 2.0) and above.
- MSHTML/Trident 6.0 (Internet Explorer 10) has native support. MSHTML/Trident 4.0 & 5.0 (Internet Explorer 8 & 9) provide partial support via the XDomainRequest object.
- Presto-based browsers (Opera) implement CORS as of Opera 12.00 and Opera Mobile 12, but not Opera Mini.
- WebKit (Initial revision uncertain, Safari 4 and above, Google Chrome 3 and above, possibly earlier).
- Microsoft Edge All versions.

## History

Cross-origin support was originally proposed by Matt Oshry, Brad Porter, and Michael Bodell of Tellme Networks in March 2004 for inclusion in VoiceXML 2.1 to allow safe cross-origin data requests by VoiceXML browsers. The mechanism was deemed general in nature and not specific to VoiceXML and was subsequently separated into an implementation NOTE. The WebApps Working Group of the W3C with participation from the major browser vendors began to formalize the NOTE into a W3C Working Draft on track toward formal W3C Recommendation status.

In May 2006 the first W3C Working Draft was submitted. In March 2009 the draft was renamed to "Cross-Origin Resource Sharing" and in January 2014 it was accepted as a W3C Recommendation.

## CORS vs JSONP

The main advantage of JSONP was its ability to work on legacy browsers which predate CORS support (Opera Mini and Internet Explorer 9 and earlier). CORS is now supported by most modern web browsers, and can be used as a modern alternative to the JSONP pattern. The benefits of CORS are:

- While JSONP supports only the `GET` request method, CORS also supports other types of HTTP requests.
- CORS enables a web programmer to use regular XMLHttpRequest, which supports better error handling than JSONP.
- While JSONP can cause cross-site scripting (XSS) issues when the external site is compromised, CORS allows websites to manually parse responses to increase security.
