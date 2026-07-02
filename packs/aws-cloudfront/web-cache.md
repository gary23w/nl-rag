---
title: "Web cache"
source: https://en.wikipedia.org/wiki/Web_cache
domain: aws-cloudfront
license: CC-BY-SA-4.0
tags: aws cloudfront, cloud cdn, content delivery, edge cache
fetched: 2026-07-02
---

# Web cache

A **web cache** (or **HTTP cache**) is a system for optimizing the World Wide Web. It is implemented both client-side and server-side. The caching of multimedia and other files can result in less overall delay when browsing the Web.

## Parts of the system

### Forward and reverse

A forward cache is a cache outside the web server's network, e.g. in the client's web browser, in an Internet service provider, or within a corporate network. A network-aware forward cache only caches heavily accessed items. A proxy server sitting between the client and web server can evaluate HTTP headers and choose whether to store web content.

A reverse cache sits in front of one or more web servers, accelerating requests from the Internet and reducing peak server load. This is usually a content delivery network (CDN) that retains copies of web content at various points throughout a network.

### HTTP options

The Hypertext Transfer Protocol (HTTP) defines three basic mechanisms for controlling caches: freshness, validation, and invalidation. This is specified in the header of HTTP response messages from the server.

Freshness allows a response to be used without re-checking it on the origin server, and can be controlled by both the server and the client. For example, the Expires response header gives a date when the document becomes stale, and the Cache-Control: max-age directive tells the cache how many seconds the response is fresh for.

Validation can be used to check whether a cached response is still good after it becomes stale. For example, if the response has a Last-Modified header, a cache can make a *conditional request* using the If-Modified-Since header to see if it has changed. The ETag (entity tag) mechanism also allows for both strong and weak validation.

Invalidation is usually a side effect of another request that passes through the cache. For example, if a URL associated with a cached response subsequently gets a POST, PUT or DELETE request, the cached response will be invalidated. Many CDNs and manufacturers of network equipment have replaced this standard HTTP cache control with dynamic caching.

## Legality

In 1998, the Digital Millennium Copyright Act added rules to the United States Code (17 U.S.C. §: 512) that exempts system operators from copyright liability for the purposes of caching.

## Server-side software

This is a list of server-side web caching software.

| Name | Operating system | Forward mode | Reverse mode | License |   |   |
|---|---|---|---|---|---|---|
| Windows | Unix-like | Other |   |   |   |   |
| Apache HTTP Server | Yes | OS X, Linux, Unix, FreeBSD, Solaris, Novell NetWare | OS/2, TPF, OpenVMS, eComStation | Yes |   | Apache 2.0 |
| aiScaler Dynamic Cache Control | No | Linux | No |   |   | Proprietary |
| ApplianSys CACHEbox | No | Linux | No |   |   | Proprietary |
| Blue Coat ProxySG | No | No | SGOS | Yes | Yes | Proprietary |
| Nginx | Yes | Linux, BSD, OS X, Solaris, AIX, HP-UX | Yes | Yes | Yes | 2-clause BSD-like |
| Microsoft Forefront Threat Management Gateway | Yes | No | No | Yes | Yes | Proprietary |
| Polipo | Yes | OS X, Linux, OpenWrt, FreeBSD | ? | Yes | Yes | MIT License |
| Squid | Yes | Linux | ? | Yes | Yes | GPL |
| Apache Traffic Server | ? | Linux | ? | Yes | Yes | Apache 2.0 |
| Untangle | No | Linux | No | Yes | Yes | Proprietary |
| Varnish | No | Linux | No | Needs a VMOD | Yes | BSD |
| WinGate | Yes | No | No | Yes | Yes | Proprietary (Free for 8 users) |
| Nuster | No | Linux | No | Yes | Yes | GPL |
| McAfee Web Gateway | No | McAfee Linux Operating System | No | Yes | Yes | Proprietary |
