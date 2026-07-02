---
title: "Well-known URI"
source: https://en.wikipedia.org/wiki/Well-known_URI
domain: well-known-uri
license: CC-BY-SA-4.0
tags: well-known uri, well-known resource path, site metadata discovery, webfinger discovery
fetched: 2026-07-02
---

# Well-known URI

A **well-known URI** is a Uniform Resource Identifier for URL path prefixes that start with `/.well-known/`. They are implemented in webservers so that requests to the servers for **well-known services** or information are available at URL consistent **well-known locations** across servers.

## Description

Well-known URIs are Uniform Resource Identifiers defined by the IETF in RFC 8615. They are URL path prefixes that start with `/.well-known/`. This implementation is in response to the common expectation for web-based protocols to require certain services or information be available at URLs consistent across servers, regardless of the way URL paths are organized on a particular host. The URIs are implemented in webservers so that requests to the servers for well-known services or information are available at URLs consistently in well-known locations across servers.

The IETF has defined a simple way for web servers to hold metadata that any user agent (e.g., web browser) can request. The metadata is useful for various tasks, including directing a web user to use a mobile app instead of the website or indicating the different ways that the site can be secured. The well-known locations are used by web servers to share metadata with user agents; sometimes these are files and sometimes these are requests for information from the web server software itself. The way to declare the different metadata requests that can be provided is standardized by the IETF so that other developers know how to find and use this information.

### Use

The path well-known URI begins with the characters `/.well-known/`, and whose scheme is "HTTP", "HTTPS", or another scheme that has explicitly been specified to use well-known URIs. As an example, if an application hosts the service "example", the corresponding well-known URIs on `https://www.example.com/` would start with `https://www.example.com/.well-known/example`.

Information shared by a web site as a well-known service is expected to meet a specific standard. Specifications that need to define a resource for such site-wide metadata can register their use with the Internet Assigned Numbers Authority (IANA) to avoid collisions and minimize impingement upon sites' URI space.

## List of well-known URIs

The list below describes known standards for .well-known services that a web server can implement.

| URI suffix | Description | Reference | Date of IANA registration |
|---|---|---|---|
| acme-challenge | Automated Certificate Management Environment (ACME) |   | 2019-03-01 |
| agent-card.json | Details for an A2A Server's Agent Card |   |   |
| ai-plugin.json | Manifest for a ChatGPT plugin |   |   |
| apple-app-site-association | An Apple service that enables secure data exchange between iOS and a website |   |   |
| apple-developer-merchantid-domain-association | Apple Pay |   |   |
| appspecific | Used by some application to get some informations about the application (e.g. chrome devtools: appspecific/com.chrome.devtools.json) |   |   |
| ashrae | BACnet – A data communication protocol for building automation and control networks |   | 2016-01-22 |
| assetlinks.json | AssetLinks protocol used to identify one or more digital assets (such as web sites or mobile apps) that are related to the hosting web site in some fashion |   | 2015-09-28 |
| atproto-did | Handle-to-DID resolution for AT Protocol |   |   |
| autoconfig/mail | Mozilla Thunderbird mail autoconfiguration service |   |   |
| browserid | Mozilla Persona |   |   |
| caldav | Calendaring Extensions to WebDAV (CalDAV) and vCard Extensions to WebDAV (CardDAV) |   |   |
| carddav | Calendaring Extensions to WebDAV (CalDAV) and vCard Extensions to WebDAV (CardDAV) |   |   |
| change-password | Helps password managers find the URL for changing client account passwords |   |   |
| coap | CoAP (Constrained Application Protocol) over TCP, TLS, and WebSockets |   | 2017-12-22 |
| com.apple.remotemanagement | Apple-Account–based user enrollment for mobile device management |   |   |
| com.chrome.devtools.json | Automatic Workspace Folders - Chromium DevTools Ecosystem Guide for Web development tools |   |   |
| core | Constrained RESTful Environments (CoRE) Link Format |   |   |
| csvm | CSV metadata, Model for Tabular Data and Metadata on the Web |   | 2015-09-28 |
| dat | Links domain to Dat identifier, used by Beaker web browser |   |   |
| did.json | did:web Decentralized Identifiers (DIDs) for the Web |   |   |
| discord | Domain verification for Discord account connection |   |   |
| dnt | Site-wide tracking status resource |   | 2015-08-19 |
| dnt-policy.txt | A privacy-friendly Do Not Track (DNT) Policy |   | 2015-08-19 |
| est | Enrollment over Secure Transport (EST) |   | 2013-08-16 |
| genid | Resource Description Framework (RDF) Skolem IRIs |   | 2012-11-15 |
| gpc.json | Global Privacy Control (GPC) |   |   |
| hoba | HTTP Origin-Bound Authentication (HOBA) |   | 2015-01-20 |
| host-meta | Web Host Metadata |   |   |
| host-meta.json | Web Host Metadata |   |   |
| http-opportunistic | Opportunistic Security for HTTP/2 |   | 2017-03-20 |
| keybase.txt | Used by the Keybase project to identify a proof that one or more people whose public keys may be retrieved using the Keybase service have administrative control over the origin server from which it is retrieved |   | 2014-04-08 |
| keyparc | Used by the Bloombase Keyparc project to secure online digital assets using cryptography over web services |   | 2012-09-23 |
| matrix | Provides discovery for both client and server APIs to the Matrix federated protocol |   |   |
| mercure | Discovery of Mercure hubs. Mercure is a protocol enabling the pushing of data updates to web browsers and other HTTP clients in a fast, reliable and battery-efficient way. |   |   |
| mta-sts.txt | SMTP MTA Strict Transport Security Policy |   | 2018-06-21 |
| ni | Naming Things with Hashes |   |   |
| nodeinfo | Metadata for federated social networking servers |   |   |
| nostr.json | Discovery of Nostr public keys and related relays, according to NIP-05 |   | 2024-03-18 |
| oauth-authorization-server | OAuth Authorization Server Metadata |   | 2018-03-27 |
| openid-configuration | OpenID Connect |   | 2013-08-27 |
| openorg | Organisation Profile Document |   | 2015-05-29 |
| openpgpkey | OpenPGP Web Key Service |   |   |
| org.flathub.VerifiedApps.txt | Verifies that an app is associated with given domain in Flathub |   |   |
| passkey-endpoints | Formally advertises support for passkeys and provides direct links for enrollment and management for password managers to automatically create/upgrade. |   |   |
| pki-validation | CA/Browser Forum's Baseline Requirements Certificate Policy for the Issuance and Management of Publicly-Trusted Certificates |   | 2017-02-06 |
| posh | PKIX over Secure HTTP (POSH) |   | 2015-09-20 |
| privacy-sandbox-attestations.json | The Google Chrome Privacy Sandbox attestation file |   |   |
| pubvendors.json | The IAB pubvendors.json tech spec, which provide a standard for publishers to publicly declare the vendors that they work with, and their respective data rights/configuration |   | 2020-09-07 |
| reload-config | REsource LOcation And Discovery (RELOAD) Base Protocol |   |   |
| repute-template | A Reputation Query Protocol |   | 2013-09-30 |
| resourcesync | ResourceSync Framework Specification |   | 2017-05-26 |
| security.txt | Standard to help organizations define the process for security researchers to disclose security vulnerabilities |   | 2018-08-20 |
| smart-configuration | SMART on FHIR configuration metadata, including OAuth authorization_endpoint and token_endpoint URLs |   | 2023-03-01 |
| statements.txt | Standard for collective contract signing |   |   |
| stun-key | Session Traversal Utilities for NAT (STUN) Extension for Third-Party Authorization |   | 2015-06-12 |
| tdmrep.json | Domain-wide TDM (Text and Data Mining) reservation |   |   |
| time | Time over HTTPS specification |   | 2015-12-09 |
| timezone | Time Zone Data Distribution Service |   | 2015-08-03 |
| traffic-advice | Prefetch control (proposal; implemented in Chrome Privacy Preserving Prefetch Proxy crawler) |   |   |
| uma2-configuration | User-Managed Access (UMA) 2.0 grant for OAuth 2.0 authorization |   | 2017-06-20 |
| vercel/flags | Overridable Feature Flag's for Vercel's Toolbar |   |   |
| void | Describing Linked Datasets with the VoID Vocabulary |   | 2011-05-11 |
| wasm-pkg/registry.json | WebAssembly registry |   |   |
| webauthn | WebAuthn Related Origins |   |   |
| webfinger | WebFinger |   | 2013-03-15, 2013-09-06 |
| workflow | Workflow Development Kit Routes |   |   |
| xrp-ledger.toml | XRP ledger node & account information |   |   |
| ai-catalog.json | Agentic Resource Discovery Specification |   |   |
