---
title: "JSON Web Signature"
source: https://en.wikipedia.org/wiki/JSON_Web_Signature
domain: jwt-security-pitfalls
license: CC-BY-SA-4.0
tags: json web token, jwt security pitfalls, token signature validation, algorithm confusion defense
fetched: 2026-07-02
---

# JSON Web Signature

A **JSON Web Signature** (abbreviated **JWS**) is an IETF-proposed standard (RFC 7515) for signing arbitrary data. This is used as the basis for a variety of web-based technologies including JSON Web Token.

## Purpose

JWS is a way to ensure integrity of information in a highly serializable, machine-readable format. That means that it is information, along with proof that the information hasn't changed since being signed. It can be used for sending information from one web site to another, and is especially aimed at communications on the web. It even contains a compact form optimized for applications like URI query parameters.

### Examples

#### Web commerce

JWS can be used for applications in which digitally signed information must be sent in a machine-readable format, such as e-commerce. For example, say a user named Bob is browsing widget prices on a web site (widgets.com), and wishes to get a quote on one of them. Then widgets.com could provide Bob with a JWS object containing all relevant information about the widget, including the price, then sign it using their private key. Then Bob would have a non-repudiable price quote for the product.

#### Access to third-party resources

Maybe Widgets.com and WidgetStorage.com have a deal in which WidgetStorage.com will accept coupons from Widgets.com in exchange for traffic. Widgets.com could issue JWS giving Bob a 10% discount on the WidgetStorage.com site. Again, because the data is signed, WidgetStorage can know that Widgets.com emitted this. If the data was not signed, then Bob could change his discount to 50% and no one would know just from looking at the data.

## Limitations

JWS is one of the standards in the JOSE series and is meant to be used in combination with them. For example, for encryption JSON Web Encryption (JWE) is supposed to be used in conjunction.

As of 2015, JWS was a proposed standard, and was part of several other IETF proposed standards, and there was code available on the web to implement the proposed standard.
