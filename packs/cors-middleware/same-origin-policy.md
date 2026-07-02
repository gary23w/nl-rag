---
title: "Same-origin policy"
source: https://en.wikipedia.org/wiki/Same-origin_policy
domain: cors-middleware
license: CC-BY-SA-4.0
tags: cors middleware, cross-origin resource sharing, preflight request, same-origin policy
fetched: 2026-07-02
---

# Same-origin policy

In computing, the **same-origin policy** (**SOP**) is a concept in the web application security model. Under the policy, a web browser permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same *origin*. An origin is defined as a combination of URI scheme, host name, and port number. This policy prevents a malicious script on one page from obtaining access to sensitive data on another web page through that page's Document Object Model (DOM).

This mechanism bears a particular significance for modern web applications that extensively depend on HTTPS cookies to maintain authenticated user sessions, as servers act based on the HTTP cookie information to reveal sensitive information or perform state-changing actions. A strict separation between content provided by unrelated sites must be maintained on the client-side to prevent the loss of data confidentiality or integrity.

The same-origin policy applies only to scripts. This means that resources such as images, CSS, and dynamically loaded scripts can be accessed across origins via the corresponding HTML tags (with fonts being a notable exception). Attacks take advantage of the fact that the same origin policy does not apply to HTML tags.

There are some mechanisms available to relax the SOP; one of them is cross-origin resource sharing (CORS).

## History

The concept of same-origin policy was introduced by Netscape Navigator 2.02 in 1995, shortly after the introduction of JavaScript in Netscape 2.0. JavaScript enabled scripting on web pages, and in particular programmatic access to the DOM.

The policy was originally designed to protect access to the DOM, but has since been broadened to protect sensitive parts of the global JavaScript object.

## Implementation

All modern browsers implement some form of the same-origin policy as it is an important security cornerstone. The policies are not required to match an exact specification but are often extended to define roughly compatible security boundaries for other web technologies, such as Microsoft Silverlight, Adobe Flash, or Adobe Acrobat, or for mechanisms other than direct DOM manipulation, such as XMLHttpRequest.

## Origin determination rules

The algorithm used to calculate the "origin" of a URI is specified in RFC 6454, Section 4. For absolute URIs, the origin is the triple {scheme, host, port}. If the URI does not use a hierarchical element as a naming authority (see RFC 3986, Section 3.2) or if the URI is not an absolute URI, then a globally unique identifier is used. Two resources are considered to be of the same origin if and only if all these values are exactly the same.

To illustrate, the following table gives an overview of typical outcomes for checks against the URL "**http://www.example.com/dir/page.html**".

| Compared URL | Outcome | Reason |
|---|---|---|
| **http://www.example.com**/dir/page2.html | Success | Same scheme, host and port |
| **http://www.example.com**/dir2/other.html | Success | Same scheme, host and port |
| **http://**username:password@**www.example.com**/dir2/other.html | Success | Same scheme, host and port |
| http://www.example.com:**80**/dir/other.html | Success | Most modern browsers implicitly assign the protocol's default port when omitted. |
| http://www.example.com:**81**/dir/other.html | Failure | Same scheme and host but different port |
| **https**://www.example.com/dir/other.html | Failure | Different scheme |
| http://**en.example.com**/dir/other.html | Failure | Different host |
| http://**example.com**/dir/other.html | Failure | Different host (exact match required) |
| http://**v2.www.example.com**/dir/other.html | Failure | Different host (exact match required) |
| **data**:image/gif;base64,R0lGODlhAQABAAAAACwAAAAAAQABAAA= | Failure | Different scheme |

Unlike other browsers, Internet Explorer does not include the port in the calculation of the origin, using the Security Zone in its place.

## Read access to sensitive cross-origin responses via reusable authentication

The same-origin policy protects against reusing authenticated sessions across origins. The following example illustrates a potential security risk that could arise without the same-origin policy. Assume that a user is visiting a banking website and doesn't log out. Then, the user goes to another site that has malicious JavaScript code that requests data from the banking site. Because the user is still logged in on the banking site, the malicious code could do anything the user could do on the banking site. For example, it could get a list of the user's last transactions, create a new transaction, etc. This is because, in the original spirit of a World Wide Web, browsers are required to tag along authentication details such as session cookies and platform-level kinds of the Authorization request header to the banking site based on the domain of the banking site.

The bank site owners would expect that regular browsers of users visiting the malicious site do not allow the code loaded from the malicious site access the banking session cookie or platform-level authorization. While it is true that JavaScript has no direct access to the banking session cookie, it could still send and receive requests to the banking site with the banking site's session cookie. Same Origin Policy was introduced as a requirement for security-minded browsers to deny read access to responses from across origins, with the assumption that the majority of users choose to use compliant browsers. The policy does not deny writes. Counteracting the abuse of the write permission requires additional CSRF protections by the target sites.

## Relaxing the same-origin policy

In some circumstances, the same-origin policy is too restrictive, posing problems for large websites that use multiple subdomains. At first, a number of workarounds such as using the fragment identifier or the `window.name` property were used to pass data between documents residing in different domains. Modern browsers support multiple techniques for relaxing the same-origin policy in a controlled manner:

### Data tainting

Netscape Navigator briefly contained a taint checking feature. The feature was experimentally introduced in 1997 as part of Netscape 3. The feature was turned off by default, but if enabled by a user it would allow websites to attempt to read JavaScript properties of windows and frames belonging to a different domain. The browser would then ask the user whether to permit the access in question.

### document.domain property

If two windows (or frames) contain scripts that set domain to the same value, the same-origin policy is relaxed for these two windows, and each window can interact with the other. For example, cooperating scripts in documents loaded from orders.example.com and catalog.example.com might set their `document.domain` properties to “example.com”, thereby making the documents appear to have the same origin and enabling each document to read properties of the other. Setting this property implicitly sets the port to null, which most browsers will interpret differently from port 80 or even an unspecified port. To assure that access will be allowed by the browser, set the document.domain property of both pages.

The `document.domain` concept was introduced as part of Netscape Navigator 3, released in 1996.

### Cross-origin resource sharing

The other technique for relaxing the same-origin policy is standardized under the name cross-origin resource sharing (CORS). This standard extends HTTP with a new `Origin` request header and a new `Access-Control-Allow-Origin` response header. It allows servers to use a header to explicitly list origins that may request a file or to use a wildcard and allow a file to be requested by any site. Browsers such as Firefox 3.5, Safari 4 and Internet Explorer 10 use this header to allow the cross-origin HTTP requests with XMLHttpRequest that would otherwise have been forbidden by the same-origin policy.

### Cross-document messaging

Another technique, cross-document messaging, allows a script from one page to pass textual messages to a script on another page regardless of the script origins. Calling the postMessage() method on a Window object asynchronously fires an "onmessage" event in that window, triggering any user-defined event handlers. A script in one page still cannot directly access methods or variables in the other page, but they can communicate safely through this message-passing technique.

### JSONP

Since HTML `<script>` elements are allowed to retrieve and execute content from other domains, a page can bypass the same-origin policy and receive JSON data from a different domain by loading a resource that returns a JSONP payload. JSONP payloads consist of an internal JSON payload wrapped by a pre-defined function call. When the script resource is loaded by the browser, the designated callback function will be invoked to process the wrapped JSON payload.

### WebSockets

Modern browsers will permit a script to connect to a WebSocket address without applying the same-origin policy. However, they recognize when a WebSocket URI is used, and insert an **Origin:** header into the request that indicates the origin of the script requesting the connection. To ensure cross-site security, the WebSocket server must verify that that origin is permitted to receive a reply.

## Corner cases

The behavior of same-origin checks and related mechanisms is not well-defined in a number of corner cases such as for pseudo-protocols that do not have a clearly defined host name or port associated with their URLs (file:, data:, etc.). This historically caused a fair number of security problems, such as the generally undesirable ability of any locally stored HTML file to access all other files on the disk, or communicate with any site on the Internet.

Lastly, certain types of attacks, such as DNS rebinding or server-side proxies, permit the host name check to be partly subverted, and make it possible for rogue web pages to directly interact with sites through addresses other than their "true", canonical origin. The impact of such attacks is limited to very specific scenarios, since the browser still believes that it is interacting with the attacker's site, and therefore does not disclose third-party cookies or other sensitive information to the attacker.

## Attacks

### Reading information

Even when same-origin policy is in effect (without being relaxed by Cross-Origin Resource Sharing), certain cross-origin attacks can be performed. WebRTC can be used to find out the internal IP address of a victim. If attempting to connect to a cross-origin port, responses cannot be read in face of same-origin policy, but a JavaScript can still make inferences on whether the port is open or closed by checking if the onload/onerror event fires, or if we get a timeout. This gives opportunities for cross-origin portscanning.

Further, JavaScript snippets can use techniques like cross-site leaks to exploit long-standing information leakages in the browser to infer information cross-origin. These attacks can be counteracted by implementing a Cross-Origin Resource Policy (CORP) header, which allows a website owner to block cross-origin or cross-site resources, like images, videos, and stylesheets. CORP can also block JavaScript-initiated `fetch` requests, but only if they are sent with the `no-cors` request mode.

### Writing information (CSRF)

The same-origin policy does not prevent the browser from making GET, POST, OPTIONS, and TRACE requests; it only prevents the responses from being read by user code. Therefore, if an endpoint uses one of these "safe" request methods to write information or perform an action on a user's behalf, it can be exploited by attackers.

### Leaking or writing information via cookies

Note that the same-origin policy does not apply to cookies for historical reasons. If multiple adversarial sites are deployed on the same hostname with different port numbers, contrary to the SOP, all cookies set by any of the sites are shared. This can be used to leak users' session tokens and steal account information. Therefore, web services should be separated by differentiating subdomains rather than port numbers.
