---
title: "HSTS - Glossary"
source: https://developer.mozilla.org/en-US/docs/Glossary/HSTS
domain: http-strict-transport-security
license: CC-BY-SA-4.0
tags: http strict transport security, hsts header, https enforcement, transport layer security
fetched: 2026-07-02
---

# HSTS

**HTTP Strict Transport Security** lets a website inform the browser that it should never load the site using HTTP and should automatically convert all attempts to access the site using HTTP to HTTPS requests instead. It consists in one HTTP header, `Strict-Transport-Security`, sent by the server with the resource.

In other words, it tells the browser that changing the protocol from HTTP to HTTPS in a URL works (and is more secure) and asks the browser to do it for every request.
