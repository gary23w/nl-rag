---
title: "HTTP Strict Transport Security"
source: https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
domain: http-strict-transport-security
license: CC-BY-SA-4.0
tags: http strict transport security, hsts header, https enforcement, transport layer security
fetched: 2026-07-02
---

# HTTP Strict Transport Security

**HTTP Strict Transport Security** (**HSTS**) is a policy mechanism that helps to protect websites against man-in-the-middle attacks such as protocol downgrade attacks and cookie hijacking. It allows web servers to declare that web browsers (or other complying user agents) should automatically interact with it using only HTTPS connections, which provide Transport Layer Security (TLS/SSL), unlike the insecure HTTP used alone. HSTS is an IETF standards track protocol and is specified in RFC 6797.

The HSTS Policy is communicated by the server to the user agent via an HTTP response header field named `Strict-Transport-Security`. HSTS Policy specifies a period of time during which the user agent should only access the server in a secure fashion. Websites using HSTS often do not accept clear text HTTP, either by rejecting connections over HTTP or systematically redirecting users to HTTPS (though this is not required by the specification). The consequence of this is that a user-agent not capable of doing TLS will not be able to connect to the site.

The protection normally only applies after a user has visited the site at least once, relying on the principle of "trust on first use". The way this protection works is that when a user entering or selecting an HTTP (not HTTPS) URL to the site, the client, such as a Web browser, will automatically upgrade to HTTPS without making an HTTP request, thereby preventing any HTTP man-in-the-middle attack from occurring. To counteract this problem, an HSTS preload list maintained by Google Chrome and used by other major web browsers is maintained. If a domain is on this list, the browser skips the initial request and encrypts all communication immediately. Additional domains can be registered at no cost.

## Specification history

The HSTS specification was published as RFC 6797 on 19 November 2012 after being approved on 2 October 2012 by the IESG for publication as a Proposed Standard RFC. The authors originally submitted it as an Internet Draft on 17 June 2010. With the conversion to an Internet Draft, the specification name was altered from "Strict Transport Security" (STS) to "HTTP Strict Transport Security", because the specification applies only to HTTP. The HTTP response header field defined in the HSTS specification however remains named "Strict-Transport-Security".

The last so-called "community version" of the then-named "STS" specification was published on 18 December 2009, with revisions based on community feedback.

The original draft specification by Jeff Hodges from PayPal, Collin Jackson, and Adam Barth was published on 18 September 2009.

The HSTS specification is based on original work by Jackson and Barth as described in their paper "ForceHTTPS: Protecting High-Security Web Sites from Network Attacks".

Additionally, HSTS is the realization of one facet of an overall vision for improving web security, put forward by Jeff Hodges and Andy Steingruebl in their 2010 paper *The Need for Coherent Web Security Policy Framework(s)*.

## HSTS mechanism overview

A server implements an HSTS policy by supplying a header over an HTTPS connection (HSTS headers over HTTP are ignored). For example, a server could send a header such that future requests to the domain for the next year (max-age is specified in seconds; 31,536,000 is equal to one non-leap year) use only HTTPS: `Strict-Transport-Security: max-age=31536000`.

When a web application issues HSTS Policy to user agents, conformant user agents behave as follows:

1. Automatically turn any insecure links referencing the web application into secure links (e.g. `http://example.com/some/page/` will be modified to `https://example.com/some/page/` *before* accessing the server).
2. If the security of the connection cannot be ensured (e.g. the server's TLS certificate is not trusted), the user agent must terminate the connection and should not allow the user to access the web application.

This helps protect web application users against some passive (eavesdropping) and active network attacks. A man-in-the-middle attacker has a greatly reduced ability to intercept requests and responses between a user and a web application server while the user's browser has HSTS Policy in effect for that web application.

## Applicability

The most important security vulnerability that HSTS can fix is SSL-stripping man-in-the-middle attacks, first publicly introduced by Moxie Marlinspike in his 2009 BlackHat Federal talk "New Tricks For Defeating SSL In Practice". The SSL (and TLS) stripping attack works by transparently converting a secure HTTPS connection into a plain HTTP connection. The user can see that the connection is insecure, but crucially there is no way of knowing whether the connection *should* be secure. At the time of Marlinspike's talk, many websites did not use TLS/SSL, therefore there was no way of knowing (without prior knowledge) whether the use of plain HTTP was due to an attack, or simply because the website had not implemented TLS/SSL. Additionally, no warnings are presented to the user during the downgrade process, making the attack fairly subtle to all but the most vigilant. Marlinspike's sslstrip tool, presented at Black Hat DC 2009, fully automates the attack.

HSTS addresses this problem by informing the browser that connections to the site should always use TLS/SSL. The HSTS header can be stripped by the attacker if this is the user's first visit. Google Chrome, Mozilla Firefox, Internet Explorer, and Microsoft Edge attempt to limit this problem by including a "pre-loaded" list of HSTS sites. Unfortunately this solution cannot scale to include all websites on the internet. See limitations, below.

HSTS can also help to prevent having one's cookie-based website login credentials stolen by widely available tools such as Firesheep.

Because HSTS is time limited, it is sensitive to attacks involving shifting the victim's computer time e.g. using false NTP packets.

## Limitations

The initial request remains unprotected from active attacks if it uses an insecure protocol such as plain HTTP or if the URI for the initial request was obtained over an insecure channel. The same applies to the first request after the activity period specified in the advertised HSTS Policy `max-age` (sites should set a period of several days or months depending on user activity and behavior).

### Solutions with preload list

Google Chrome, Mozilla Firefox, and Internet Explorer/Microsoft Edge address this limitation by implementing a "HSTS preloaded list", which is a list that contains known sites supporting HSTS. This list is distributed with the browser so that it uses HTTPS for the initial request to the listed sites as well. As previously mentioned, these pre-loaded lists cannot scale to cover the entire Web. A potential solution might be achieved by using DNS records to declare HSTS Policy, and accessing them securely via DNSSEC, optionally with certificate fingerprints to ensure validity (which requires running a validating resolver to avoid last mile issues).

Junade Ali has noted that HSTS is ineffective against the use of false domains; by using DNS-based attacks, it is possible for a man-in-the-middle interceptor to serve traffic from an artificial domain which is not on the HSTS Preload list, this can be made possible by DNS Spoofing Attacks, or simply a domain name that misleadingly resembles the real domain name such as *www.example.org* instead of *www.example.com*.

Even with an HSTS preloaded list, HSTS cannot prevent advanced attacks against TLS itself, such as the BEAST or CRIME attacks introduced by Juliano Rizzo and Thai Duong. Attacks against TLS itself are orthogonal to HSTS policy enforcement. Neither can it protect against attacks on the server - if someone compromises it, it will happily serve any content over TLS.

### Privacy issues

HSTS can be used to near-indelibly tag visiting browsers with recoverable identifying data (supercookies) which can persist in and out of browser "incognito" privacy modes. By creating a web page that makes multiple HTTP requests to selected domains, for example, if twenty browser requests to twenty different domains are used, theoretically over one million visitors can be distinguished (220) due to the resulting requests arriving via HTTP vs. HTTPS; the latter being the previously recorded binary "bits" established earlier via HSTS headers.

## Browser support

- Chromium and Google Chrome since version 4.0.211.0
- Firefox since version 4; with Firefox 17, Mozilla integrates a list of websites supporting HSTS.
- Opera since version 12
- Safari since OS X Mavericks (version 10.9, late 2013)
- Internet Explorer 11 on Windows 8.1 and Windows 7 with KB3058515 installed (Released as a Windows Update in June 2015)
- Microsoft Edge and Internet Explorer 11 on Windows 10
- BlackBerry 10 Browser and WebView since BlackBerry OS 10.3.3.

## Deployment best practices

Depending on the actual deployment there are certain threats (e.g. cookie injection attacks) that can be avoided by following best practices.

- HSTS hosts should declare HSTS policy at their top-level domain name. For example, an HSTS host at https://sub.example.com should also answer with the HSTS header at https://example.com. The header should specify the `includeSubDomains` directive.
- In addition to HSTS deployment, a host for https://www.example.com should include a request to a resource from https://example.com to make sure that HSTS for the parent domain is set and protects the user from potential cookie injection attacks performed by a MITM that would inject a reference to the parent domain (or even http://nonexistentpeer.example.com), which the attacker then would answer.
