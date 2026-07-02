---
title: "Content Security Policy"
source: https://en.wikipedia.org/wiki/Content_Security_Policy
domain: helmet-security
license: CC-BY-SA-4.0
tags: helmet security, http security headers, content security policy header, express hardening
fetched: 2026-07-02
---

# Content Security Policy

**Content Security Policy** (**CSP**) is a computer security standard introduced to prevent cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. It is a Candidate Recommendation of the W3C working group on Web Application Security, widely supported by modern web browsers. CSP provides a standard method for website owners to declare approved origins of content that browsers should be allowed to load on that website—covered types are JavaScript, CSS, HTML frames, web workers, fonts, images, embeddable objects such as Java applets, ActiveX, audio and video files, and other HTML5 features.

## Status

The standard, originally named Content Restrictions, was proposed by Robert Hansen in 2004, first implemented in Firefox 4 and quickly picked up by other browsers. Version 1 of the standard was published in 2012 as W3C candidate recommendation and quickly with further versions (Level 2) published in 2014. As of 2023, the draft of Level 3 is being developed with the new features being quickly adopted by the web browsers.

The following header names are in use as part of experimental CSP implementations:

- `Content-Security-Policy` – standard header name proposed by the W3C document. Google Chrome supports this as of version 25. Firefox supports this as of version 23, released on 6 August 2013. WebKit supports this as of version 528 (nightly build). Chromium-based Microsoft Edge support is similar to Chrome's.
- `X-WebKit-CSP` – deprecated, experimental header introduced into Google Chrome, Safari and other WebKit-based web browsers in 2011.
- `X-Content-Security-Policy` – deprecated, experimental header introduced in Gecko 2 based browsers (Firefox 4 to Firefox 22, Thunderbird 3.3, SeaMonkey 2.1).

A website can declare multiple CSP headers, also mixing enforcement and report-only ones. Each header will be processed separately by the browser.

CSP can also be delivered within the HTML code using a meta tag, although in this case its effectiveness will be limited.

Internet Explorer 10 and Internet Explorer 11 also support CSP, but only sandbox directive, using the experimental `X-Content-Security-Policy` header.

A number of web application frameworks support CSP, for example AngularJS (natively) and Django (middleware). Instructions for Ruby on Rails have been posted by GitHub. Web framework support is however only required if the CSP contents somehow depend on the web application's state—such as usage of the `nonce` origin. Otherwise, the CSP is rather static and can be delivered from web application tiers above the application, for example on load balancer or web server.

### Bypasses

In December 2015 and December 2016, a few methods of bypassing `'nonce'` allowlisting origins were published. In January 2016, another method was published, which leverages server-wide CSP allowlisting to exploit old and vulnerable versions of JavaScript libraries hosted at the same server (frequent case with CDN servers). In May 2017 one more method was published to bypass CSP using web application frameworks code.

## Mode of operation

If the `Content-Security-Policy` header is present in the server response, a compliant client enforces the declarative allowlist policy. One example goal of a policy is a stricter execution mode for JavaScript in order to prevent certain cross-site scripting attacks. In practice this means that a number of features are disabled by default:

- Inline JavaScript code
  - `<script>` blocks,
  - DOM event handlers as HTML attributes (e.g. `onclick`)
  - The `javascript:` links
- Inline CSS statements
  - `<style>` block
  - `style` attributed to HTML elements
- Dynamic JavaScript code evaluation
  - `eval()`
  - string arguments for `setTimeout` and `setInterval` functions
  - `new Function()` constructor
- Dynamic CSS statements
  - `CSSStyleSheet.insertRule()` method

While using CSP in a new application may be quite straightforward, especially with CSP-compatible JavaScript framework, existing applications may require some refactoring—or relaxing the policy. Recommended coding practice for CSP-compatible web applications is to load code from external source files (`<script src>`), parse JSON instead of evaluating it and use `EventTarget.addEventListener()` to set event handlers.
