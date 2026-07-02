---
title: "XMLHttpRequest"
source: https://en.wikipedia.org/wiki/XMLHttpRequest
domain: axios-http
license: CC-BY-SA-4.0
tags: axios http, promise http client, javascript ajax, request interceptor
fetched: 2026-07-02
---

# XMLHttpRequest

**XMLHttpRequest** (**XHR**) is an API in the form of a JavaScript object whose methods transmit HTTP requests from a web browser to a web server. The methods allow a browser-based application to send requests to the server after page loading is complete, and receive information back. XMLHttpRequest is a component of Ajax programming. Prior to Ajax, hyperlinks and form submissions were the primary mechanisms for interacting with the server, often replacing the current page with another one.

## History

The concept behind `XMLHttpRequest` was conceived in 2000 by the developers of Microsoft Outlook. The concept was then implemented within the Internet Explorer 5 browser (1999). However, the original syntax did not use the `XMLHttpRequest` identifier. Instead, the developers used the identifiers `ActiveXObject("Msxml2.XMLHTTP")` and `ActiveXObject("Microsoft.XMLHTTP")`. As of Internet Explorer 7 (2006), all browsers support the `XMLHttpRequest` identifier.

The `XMLHttpRequest` identifier is now the *de facto* standard in all the major browsers, including Mozilla's Gecko layout engine (2002), Safari 1.2 (2004) and Opera 8.0 (2005).

### Standards

The World Wide Web Consortium (W3C) published a *Working Draft* specification for the `XMLHttpRequest` object on April 5, 2006. On February 25, 2008, the W3C published the *Working Draft Level 2* specification. Level 2 added methods to monitor event progress, allow cross-site requests, and handle byte streams. At the end of 2011, the Level 2 specification was absorbed into the original specification.

At the end of 2012, the WHATWG took over development and maintains a living document using Web IDL.

## Usage

Example in TypeScript.

```mw
// Create XMLHttpRequest object
const xhr = new XMLHttpRequest();

// Configure request: GET method, URL, Async flag (true) makes script not stop while waiting for response
xhr.open('GET', 'https://example.com', true);

// Set event listeners

xhr.onload = () => {
    // The request is done. Log response status code and text
    console.log(xhr.status, xhr.responseText);
};

xhr.onerror = () => {
    console.log('Network error occurred');
};

// Send request
xhr.send();
```

Aside from these general steps, `XMLHttpRequest` has many options to control how the request is sent and how the response is processed. Custom header fields can be added to the request to indicate how the server should fulfill it, and data can be uploaded to the server by providing it in the "send" call. The response can be parsed from the JSON format into a readily usable JavaScript object, or processed gradually as it arrives rather than waiting for the entire text. The request can be aborted prematurely or set to fail if not completed in a specified amount of time.

## Cross-domain requests

In the early development of the World Wide Web, it was found possible to breach users' security by the use of JavaScript to exchange information from one web site with that from another less reputable one. All modern browsers therefore implement a same origin policy that prevents many such attacks, such as cross-site scripting. `XMLHttpRequest` data is subject to this security policy, but sometimes web developers want to intentionally circumvent its restrictions. This is sometimes due to the legitimate use of subdomains as, for example, making an `XMLHttpRequest` from a page created by `foo.example.com` for information from `bar.example.com` will normally fail.

Various alternatives exist to circumvent this security feature, including using JSONP, Cross-Origin Resource Sharing (CORS) or alternatives with plugins such as Flash or Silverlight (both now deprecated). Cross-origin XMLHttpRequest is specified in W3C's `XMLHttpRequest` Level 2 specification. Internet Explorer did not implement CORS until version 10. The two previous versions (8 and 9) offered similar functionality through the XDomainRequest (XDR) API. CORS is now supported by all modern browsers (desktop and mobile).

The CORS protocol has several restrictions, with two models of support. The *simple* model does not allow setting custom request headers and omits cookies. Further, only the HEAD, GET and POST request methods are supported, and POST only allows the following MIME types: "text/plain", "application/x-www-urlencoded" and "multipart/form-data". Only "text/plain" was initially supported. The other model detects when one of the *non-simple* features are requested and sends a *pre-flight request* to the server to negotiate the feature.

## Fetch alternative

Program flow using asynchronous XHR callbacks can present difficulty with readability and maintenance. ECMAScript 2015 (ES6) added the promise construct to simplify asynchronous logic. Browsers have since implemented the alternative `fetch()` interface to achieve the same functionality as XHR using promises instead of callbacks.

Fetch is also standardized by WHATWG.

### Example

```mw
fetch('/api/message')
    .then((response: Response) => {
        if (response.status !== 200) {
            throw new Error('Request failed');
        }
        return response.text();
    })
    .then((text: string) => {
        console.log(text);
    })
    .catch((error: Error) => {
        console.error(error.message);
    });
```
