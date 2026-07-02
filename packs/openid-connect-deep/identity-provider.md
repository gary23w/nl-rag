---
title: "Identity provider"
source: https://en.wikipedia.org/wiki/Identity_provider
domain: openid-connect-deep
license: CC-BY-SA-4.0
tags: openid connect, id token claims, userinfo endpoint, oidc authentication flow, claims based identity
fetched: 2026-07-02
---

# Identity provider

An **identity provider** (abbreviated **IdP**, **IDP**, or **idp**) is a system entity that creates, maintains, and manages identity information for principals and also provides authentication services to relying applications within a federation or distributed network. Identity providers offer user authentication as a service. Relying party applications, such as web applications, outsource the user authentication step to a trusted identity provider. Such a relying party application is said to be *federated*, that is, it consumes federated identity.

An identity provider is “a trusted provider that lets you use single sign-on (SSO) to access other websites.” SSO enhances usability by reducing password fatigue. It also provides better security by decreasing the potential attack surface.

Identity providers can facilitate connections between cloud computing resources and users, thus decreasing the need for users to re-authenticate when using mobile and roaming applications.

## Types of identity providers

### OpenID provider

OpenID Connect (OIDC) is an identity layer on top of OAuth. In the domain model associated with OIDC, an identity provider is a special type of OAuth 2.0 authorization server. Specifically, a system entity called an OpenID Provider issues JSON-formatted identity tokens to OIDC relying parties via a RESTful HTTP API.

### SAML identity provider

The Security Assertion Markup Language (SAML) is a set of profiles for exchanging authentication and authorization data across security domains. In the SAML domain model, an identity provider is a special type of authentication authority. Specifically, a SAML identity provider is a system entity that issues authentication assertions in conjunction with an SSO profile of SAML. A relying party that consumes these authentication assertions is called a SAML service provider.
