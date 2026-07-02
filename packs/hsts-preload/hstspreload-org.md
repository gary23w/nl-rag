---
title: "HSTS Preload List Submission"
source: https://hstspreload.org/
domain: hsts-preload
license: CC-BY-SA-4.0
tags: http strict transport security, hsts preload list, ssl stripping defense, https enforcement policy
fetched: 2026-07-02
---

## Preloading HSTS

Since sites tell the browser that they support HSTS when the browser visits, the browser cannot know a site's HSTS policy before the user has visited the site for the first time. As a result, the browser can not require HTTPS until after the first time it has connected to the site, possibly leaving the user unprotected. After this first load, the web browser has the site's HSTS policy and is able to require HTTPS for all subsequent loads.

To account for this first-load problem, Chrome maintains a list of domains that have a strong HSTS policy and are HTTPS only. This HSTS preload list is built into Chrome. Requests to these domains will only be made over HTTPS; any HTTP requests will be upgraded to HTTPS and fail to connect if HTTPS is unavailable. Other major browsers (Firefox, Safari, IE 11 and Edge) also have HSTS preload lists based on the Chrome list.

Many browsers (Chrome, Safari) will automatically upgrade all HTTP navigations to HTTPS, regardless of the domain's HSTS policy. HSTS preloading only provides value when these upgrades fail in the presence of an active attacker. The benefits provided by HSTS preloading are minimal compared to the benefits provided by HSTS. While HSTS is recommended, **HSTS *preloading* is not recommended**.

## Submission Requirements

If a site sends the `preload` directive in an HSTS header, it is considered to be requesting inclusion in the preload list and may be submitted via the form on this site.

In order to be accepted to the HSTS preload list through this form, your site must satisfy the following set of requirements:

1. Serve a valid **certificate**.
2. **Redirect** from HTTP to HTTPS on the same host, if you are listening on port 80.
3. Serve all **subdomains** over HTTPS.
  - In particular, you must support HTTPS for the `www` subdomain if a DNS record for that subdomain exists.
  - **Note:** HSTS preloading applies to *all* subdomains, including internal subdomains that are not publicly accessible.
4. Serve an **HSTS header** on the base domain for HTTPS requests:
  - The `max-age` must be at least `31536000` seconds (1 year).
  - The `includeSubDomains` directive must be specified.
  - The `preload` directive must be specified.
  - If you are serving an additional redirect from your HTTPS site, that redirect must still have the HSTS header (rather than the page it redirects to).

For more details on HSTS, please see RFC 6797. Here is an example of a valid HSTS header:

`Strict-Transport-Security:` `max-age=63072000; includeSubDomains; preload`

You can check the status of your request by entering the domain name again in the form above, or consult the current Chrome preload list by visiting `chrome://net-internals/#hsts` in your browser. Note that new entries are hardcoded into the Chrome source code and can take several months before they reach the stable version.

## Continued Requirements

You must make sure your site continues to satisfy the submission requirements at all times. Note that removing the `preload` directive from your header will make your site immediately eligible for the removal form, and that sites may be removed automatically in the future for failing to keep up the requirements.

In particular, the requirements above apply to all domains submitted through `hstspreload.org` on or after **October 11, 2017** (i.e. preloaded after Chrome 63)

The same requirements apply to earlier domains submitted on or after **February 29, 2016** (i.e. preloaded after Chrome 50), except that the required max-age for those domains is only `10886400` seconds.

## Preloading Should Be Opt-In

If you maintain a project that provides HTTPS configuration advice or provides an option to enable HSTS, **do not include the `preload` directive by default**. We get regular emails from site operators who tried out HSTS this way, only to find themselves on the preload list without realizing that some subdomains cannot support HTTPS. Removal tends to be slow and painful for those sites.

Projects that support or advise about HSTS and HSTS preloading should ensure that site operators understand the long-term consequences of preloading before they turn it on for a given domain. They should also be informed that they need to meet additional requirements and submit their site to hstspreload.org to ensure that it is successfully preloaded (i.e. to get the full protection of the intended configuration).
