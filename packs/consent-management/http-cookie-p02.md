---
title: "HTTP cookie (part 2/2)"
source: https://en.wikipedia.org/wiki/HTTP_cookie
domain: consent-management
license: CC-BY-SA-4.0
tags: consent management platform, informed consent record, cookie consent banner, privacy policy disclosure, do not track
fetched: 2026-07-02
part: 2/2
---

## Alternatives to cookies

Some of the operations that can be done using cookies can also be done using other mechanisms.

### Authentication and session management

#### JSON Web Tokens

A JSON Web Token (JWT) is a self-contained packet of information that can be used to store user identity and authenticity information. This allows them to be used in place of session cookies. Unlike cookies, which are automatically attached to each HTTP request by the browser, JWTs must be explicitly attached to each HTTP request by the web application.

#### HTTP authentication

The HTTP protocol includes the basic access authentication and the digest access authentication protocols, which allow access to a web page only when the user has provided the correct username and password. If the server requires such credentials for granting access to a web page, the browser requests them from the user and, once obtained, the browser stores and sends them in every subsequent page request. This information can be used to track the user.

#### URL (query string)

The query string part of the URL is the part that is typically used for this purpose, but other parts can be used as well. The Java Servlet and PHP session mechanisms both use this method if cookies are not enabled.

This method consists of the web server appending query strings containing a unique session identifier to all the links inside of a web page. When the user follows a link, the browser sends the query string to the server, allowing the server to identify the user and maintain state.

These kinds of query strings are very similar to cookies in that both contain arbitrary pieces of information chosen by the server and both are sent back to the server on every request. However, there are some differences. Since a query string is part of a URL, if that URL is later reused, the same attached piece of information will be sent to the server, which could lead to confusion. For example, if the preferences of a user are encoded in the query string of a URL and the user sends this URL to another user by e-mail, those preferences will be used for that other user as well.

Moreover, if the same user accesses the same page multiple times from different sources, there is no guarantee that the same query string will be used each time. For example, if a user visits a page by coming from a page *internal to the site* the first time, and then visits the same page by coming from an *external search engine* the second time, the query strings would likely be different. If cookies were used in this situation, the cookies would be the same.

Other drawbacks of query strings are related to security. Storing data that identifies a session in a query string enables session fixation attacks, referer logging attacks and other security exploits. Transferring session identifiers as HTTP cookies is more secure.

#### Hidden form fields

Another form of session tracking is to use web forms with hidden fields. This technique is very similar to using URL query strings to hold the information and has many of the same advantages and drawbacks. In fact, if the form is handled with the HTTP GET method, then this technique is similar to using URL query strings, since the GET method adds the form fields to the URL as a query string. But most forms are handled with HTTP POST, which causes the form information, including the hidden fields, to be sent in the HTTP request body, which is neither part of the URL, nor of a cookie.

This approach presents two advantages from the point of view of the tracker. First, having the tracking information placed in the HTTP request body rather than in the URL means it will not be noticed by the average user. Second, the session information is not copied when the user copies the URL (to bookmark the page or send it via email, for example).

#### window.name DOM property

All current web browsers can store a fairly large amount of data (2–32 MB) via JavaScript using the DOM property `window.name`. This data can be used instead of session cookies. The technique can be coupled with JSON/JavaScript objects to store complex sets of session variables on the client side.

The downside is that every separate window or tab will initially have an empty `window.name` property when opened.

In some respects, this can be more secure than cookies because its contents are not automatically sent to the server on every request like cookies are, so it is not vulnerable to network cookie sniffing attacks.

### Tracking

#### IP address

Some users may be tracked based on the IP address of the computer requesting the page. The server knows the IP address of the computer running the browser (or the proxy, if any is used) and could theoretically link a user's session to this IP address.

However, IP addresses are generally not a reliable way to track a session or identify a user. Many computers designed to be used by a single user, such as office PCs or home PCs, are behind a network address translator (NAT). This means that several PCs will share a public IP address. Furthermore, some systems, such as Tor, are designed to retain Internet anonymity, rendering tracking by IP address impractical, impossible, or a security risk.

#### ETag

Because ETags are cached by the browser, and returned with subsequent requests for the same resource, a tracking server can simply repeat any ETag received from the browser to ensure an assigned ETag persists indefinitely (in a similar way to persistent cookies). Additional caching header fields can also enhance the preservation of ETag data.

ETags can be flushed in some browsers by clearing the browser cache.

#### Browser cache

The browser cache can also be used to store information that can be used to track individual users. This technique takes advantage of the fact that the web browser will use resources stored within the cache instead of downloading them from the website when it determines that the cache already has the most up-to-date version of the resource.

For example, a website could serve a JavaScript file with code that sets a unique identifier for the user (for example, `var userId = 3243242;`). After the user's initial visit, every time the user accesses the page, this file will be loaded from the cache instead of downloaded from the server. Thus, its content will never change.

#### Browser fingerprint

A browser fingerprint is information collected about a browser's configuration, such as version number, screen resolution, and operating system, for the purpose of identification. Fingerprints can be used to fully or partially identify individual users or devices even when cookies are turned off.

Basic web browser configuration information has long been collected by web analytics services in an effort to accurately measure real human web traffic and discount various forms of click fraud. With the assistance of client-side scripting languages, collection of much more esoteric parameters is possible. Assimilation of such information into a single string constitutes a device fingerprint. In 2010, EFF measured at least 18.1 bits of entropy possible from browser fingerprinting. Canvas fingerprinting, a more recent technique, claims to add another 5.7 bits.

### Web storage

Some web browsers support persistence mechanisms which allow the page to store the information locally for later use.

The HTML5 standard (which most modern web browsers support to some extent) includes a JavaScript API called Web storage that allows two types of storage: local storage and session storage. Local storage behaves similarly to persistent cookies while session storage behaves similarly to session cookies, except that session storage is tied to an individual tab/window's lifetime (AKA a page session), not to a whole browser session like session cookies.

Internet Explorer supports persistent information in the browser's history, in the browser's favorites, in an XML store ("user data"), or directly within a web page saved to disk.

Some web browser plugins include persistence mechanisms as well. For example, Adobe Flash has Local shared object and Microsoft Silverlight has Isolated storage.
