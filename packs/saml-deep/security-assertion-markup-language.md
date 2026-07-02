---
title: "SAML"
source: https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language
domain: saml-deep
license: CC-BY-SA-4.0
tags: saml assertion, saml2 protocol, saml metadata exchange, service provider sso, identity provider initiated
fetched: 2026-07-02
---

# SAML

(Redirected from

Security Assertion Markup Language

)

**Security Assertion Markup Language** (**SAML**, pronounced *SAM-el*, /ˈsæməl/) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider. SAML is an XML-based markup language for security assertions (statements that service providers use to make access-control decisions). SAML is also:

- A set of XML-based protocol messages
- A set of protocol message bindings
- A set of profiles (utilizing all of the above)

An important use case that SAML addresses is web-browser single sign-on (SSO). Single sign-on is relatively easy to accomplish within a security domain (using cookies, for example) but extending SSO across security domains is more difficult and resulted in the proliferation of non-interoperable proprietary technologies. The SAML Web Browser SSO profile was specified and standardized to promote interoperability. In practice, SAML SSO is most commonly used for authentication into cloud-based business software.

## Overview

The SAML specification defines three roles: the principal (typically a human user), the identity provider (IdP) and the service provider (SP). In the primary use case addressed by SAML, the principal requests a service from the service provider. The service provider requests and obtains an authentication assertion from the identity provider. On the basis of this assertion, the service provider can make an access control decision, that is, it can decide whether to perform the service for the connected principal.

At the heart of the SAML assertion is a subject (a principal within the context of a particular security domain) about which something is being asserted. The subject is usually (but not necessarily) a human. As in the SAML 2.0 Technical Overview, the terms subject and principal are used interchangeably.

Before delivering the subject-based assertion from Identity Provider to the Service Provider, the Identity Provider may request some information from the principal (such as a user name and password) in order to authenticate the principal. SAML specifies the content of the assertion that is passed from the Identity Provider to the Service Provider. In SAML, one Identity Provider may provide SAML assertions to many Service Providers. Similarly, one Service Provider (SP) may rely on and trust assertions from many independent Identity Providers (IdP).

SAML does not specify the method of authentication at the identity provider. The IdP may use a username and password, or some other form of authentication, including multi-factor authentication or Kerberos tickets. A directory service such as RADIUS or LDAP that allows users to log in with a user name and password is a typical source of authentication tokens at an identity provider. The popular Internet social networking services also provide identity services that in theory could be used to support SAML exchanges.

## History

The Organization for the Advancement of Structured Information Standards (OASIS) Security Services Technical Committee (SSTC), which met for the first time in January 2001, was chartered "to define an XML framework for exchanging authentication and authorization information." To this end, the following intellectual property was contributed to the SSTC during the first two months of that year:

- *Security Services Markup Language* (S2ML) from Netegrity
- *AuthXML* from Securant
- *XML Trust Assertion Service Specification* (X-TASS) from VeriSign
- *Information Technology Markup Language* (ITML) from Jamcracker

Building on these initial contributions, in November 2002 OASIS announced the Security Assertion Markup Language (SAML) 1.0 specification as an OASIS Standard.

Meanwhile, the Liberty Alliance, a large consortium of companies, non-profit and government organizations, proposed an extension to the SAML standard called the Liberty Identity Federation Framework (ID-FF). Like its SAML predecessor, Liberty ID-FF proposed a standardized, cross-domain, web-based, single sign-on framework. In addition, Liberty described a *circle of trust* where each participating domain is trusted to accurately document the processes used to identify a user, the type of authentication system used, and any policies associated with the resulting authentication credentials. Other members of the circle of trust could then examine these policies to determine whether to trust such information.

While Liberty was developing ID-FF, the SSTC began work on a minor upgrade to the SAML standard. The resulting SAML 1.1 specification was ratified by the SSTC in September 2003. Then, in November of that same year, Liberty contributed ID-FF 1.2 to OASIS, thereby sowing the seeds for the next major version of SAML. In March 2005, SAML 2.0 was announced as an OASIS Standard. SAML 2.0 represents the convergence of Liberty ID-FF and proprietary extensions contributed by the Shibboleth project, as well as early versions of SAML itself. Most SAML implementations support v2.0 while many still support v1.1 for backward compatibility. By January 2008, deployments of SAML 2.0 became common in government, higher education, and commercial enterprises worldwide.

## Versions

SAML has undergone one minor and one major revision since 1.0.

- SAML 1.0 was adopted as an OASIS Standard in November 2002
- SAML 1.1 was ratified as an OASIS Standard in September 2003
- SAML 2.0 became an OASIS Standard in March 2005

The Liberty Alliance contributed its Identity Federation Framework (ID-FF) to the OASIS SSTC in September 2003:

- ID-FF 1.1 was released in April 2003
- ID-FF 1.2 was finalized in November 2003

Versions 1.0 and 1.1 of SAML are similar even though small differences exist., however, the differences between SAML 2.0 and SAML 1.1 are substantial. Although the two standards address the same use case, SAML 2.0 is incompatible with its predecessor.

Although ID-FF 1.2 was contributed to OASIS as the basis of SAML 2.0, there are some important differences between SAML 2.0 and ID-FF 1.2. In particular, the two specifications, despite their common roots, are incompatible.

## Design

SAML is built upon a number of existing standards:

- Extensible Markup Language (XML): Most SAML exchanges are expressed in a standardized dialect of XML, which is the root for the name SAML (Security Assertion Markup Language).
- XML Schema (XSD): SAML assertions and protocols are specified (in part) using XML Schema.
- XML Signature: Both SAML 1.1 and SAML 2.0 use digital signatures (based on the XML Signature standard) for authentication and message integrity.
- XML Encryption: Using XML Encryption, SAML 2.0 provides elements for encrypted name identifiers, encrypted attributes, and encrypted assertions (SAML 1.1 does not have encryption capabilities). XML Encryption is reported to have severe security concerns.
- Hypertext Transfer Protocol (HTTP): SAML relies heavily on HTTP as its communications protocol.
- Simple Object Access Protocol (SOAP): SAML specifies the use of SOAP, specifically SOAP 1.1 .

SAML defines XML-based assertions and protocols, bindings, and profiles. The term *SAML Core* refers to the general syntax and semantics of SAML assertions as well as the protocol used to request and transmit those assertions from one system entity to another. *SAML protocol* refers to **what** is transmitted, not **how** (the latter is determined by the choice of binding). So SAML Core defines "bare" SAML assertions along with SAML request and response elements.

A *SAML binding* determines how SAML requests and responses map onto standard messaging or communications protocols. An important (synchronous) binding is the SAML SOAP binding.

A *SAML profile* is a concrete manifestation of a defined use case using a particular combination of assertions, protocols and bindings.

### Assertions

A SAML *assertion* contains a packet of security information:

```
 <saml:Assertion ...>
   ..
 </saml:Assertion>
```

Loosely speaking, a relying party interprets an assertion as follows:

> Assertion *A* was issued at time *t* by issuer *R* regarding subject *S* provided conditions *C* are valid.

SAML assertions are usually transferred from identity providers to service providers. Assertions contain *statements* that service providers use to make access-control decisions. Three types of statements are provided by SAML:

1. Authentication statements
2. Attribute statements
3. Authorization decision statements

*Authentication statements* assert to the service provider that the principal did indeed authenticate with the identity provider at a particular time using a particular method of authentication. Other information about the authenticated principal (called the *authentication context*) may be disclosed in an authentication statement.

An *attribute statement* asserts that a principal is associated with certain attributes. An *attribute* is simply a name–value pair. Relying parties use attributes to make access-control decisions.

An *authorization decision statement* asserts that a principal is permitted to perform action *A* on resource *R* given evidence *E*. The expressiveness of authorization decision statements in SAML is intentionally limited. More-advanced use cases are encouraged to use XACML instead.

### Protocols

A SAML *protocol* describes how certain SAML elements (including assertions) are packaged within SAML request and response elements, and gives the processing rules that SAML entities must follow when producing or consuming these elements. For the most part, a SAML protocol is a simple request-response protocol.

The most important type of SAML protocol request is called a *query*. A service provider makes a query directly to an identity provider over a secure back channel. Thus query messages are typically bound to SOAP.

Corresponding to the three types of statements, there are three types of SAML queries:

1. Authentication query
2. Attribute query
3. Authorization decision query

The result of an attribute query is a SAML response containing an assertion, which itself contains an attribute statement. See the SAML 2.0 topic for an example of attribute query/response.

Beyond queries, SAML 1.1 specifies no other protocols.

SAML 2.0 expands the notion of *protocol* considerably. The following protocols are described in detail in SAML 2.0 Core:

- Assertion Query and Request Protocol
- Authentication Request Protocol
- Artifact Resolution Protocol
- Name Identifier Management Protocol
- Single Logout Protocol
- Name Identifier Mapping Protocol

Most of these protocols are new in SAML 2.0.

### Bindings

A SAML *binding* is a mapping of a SAML protocol message onto standard messaging formats and/or communications protocols. For example, the SAML SOAP binding specifies how a SAML message is encapsulated in a SOAP envelope, which itself is bound to an HTTP message.

SAML 1.1 specifies just one binding, the SAML SOAP Binding. In addition to SOAP, implicit in SAML 1.1 Web Browser SSO are the precursors of the HTTP POST Binding, the HTTP Redirect Binding, and the HTTP Artifact Binding. These are not defined explicitly, however, and are only used in conjunction with SAML 1.1 Web Browser SSO. The notion of binding is not fully developed until SAML 2.0.

SAML 2.0 completely separates the binding concept from the underlying profile. In fact, there is a brand new binding specification in SAML 2.0 that defines the following standalone bindings:

- SAML SOAP Binding (based on SOAP 1.1)
- Reverse SOAP (PAOS) Binding
- HTTP Redirect (GET) Binding
- HTTP POST Binding
- HTTP Artifact Binding
- SAML URI Binding

This reorganization provides tremendous flexibility: taking just Web Browser SSO alone as an example, a service provider can choose from four bindings (HTTP Redirect, HTTP POST and two flavors of HTTP Artifact), while the identity provider has three binding options (HTTP POST plus two forms of HTTP Artifact), for a total of twelve possible deployments of the SAML 2.0 Web Browser SSO Profile.

### Profiles

A SAML *profile* describes in detail how SAML assertions, protocols, and bindings combine to support a defined use case. The most important SAML profile is the Web Browser SSO Profile.

SAML 1.1 specifies two forms of Web Browser SSO, the Browser/Artifact Profile and the Browser/POST Profile. The latter passes assertions *by value* whereas Browser/Artifact passes assertions *by reference*. As a consequence, Browser/Artifact requires a back-channel SAML exchange over SOAP. In SAML 1.1, all flows begin with a request at the identity provider for simplicity. Proprietary extensions to the basic IdP-initiated flow have been proposed (by Shibboleth, for example).

The Web Browser SSO Profile was completely refactored for SAML 2.0. Conceptually, SAML 1.1 Browser/Artifact and Browser/POST are special cases of SAML 2.0 Web Browser SSO. The latter is considerably more flexible than its SAML 1.1 counterpart due to the new "plug-and-play" binding design of SAML 2.0. Unlike previous versions, SAML 2.0 browser flows begin with a request at the service provider. This provides greater flexibility, but SP-initiated flows naturally give rise to the so-called *Identity Provider Discovery* problem, the focus of much research today. In addition to Web Browser SSO, SAML 2.0 introduces numerous new profiles:

- SSO Profiles
  - Web Browser SSO Profile
  - Enhanced Client or Proxy (ECP) Profile
  - Identity Provider Discovery Profile
  - Single Logout Profile
  - Name Identifier Management Profile
- Artifact Resolution Profile
- Assertion Query/Request Profile
- Name Identifier Mapping Profile
- SAML Attribute Profiles

Aside from the SAML Web Browser SSO Profile, some important third-party profiles of SAML include:

- OASIS Web Services Security (WSS) Technical Committee
- Liberty Alliance
- OASIS eXtensible Access Control Markup Language (XACML) Technical Committee

### Security

The SAML specifications recommend, and in some cases mandate, a variety of security mechanisms:

- TLS 1.0+ for transport-level security
- XML Signature and XML Encryption for message-level security

Requirements are often phrased in terms of (mutual) authentication, integrity, and confidentiality, leaving the choice of security mechanism to implementers and deployers.

## Use

The primary SAML use case is called *Web Browser Single Sign-On (SSO)*. A user utilizes a *user agent* (usually a web browser) to request a web resource protected by a SAML *service provider*. The service provider, wishing to know the identity of the requesting user, issues an authentication request to a SAML *identity provider* through the user agent. The resulting protocol flow is depicted in the following diagram.

**1. Request the target resource at the SP (SAML 2.0 only)**

The principal (via an HTTPs user agent) requests a target resource at the service provider:

```
https://sp.example.com/myresource
```

The service provider performs a security check on behalf of the target resource. If a valid security context at the service provider already exists, skip steps 2–7.

**2. Redirect to the SSO Service at the IdP (SAML 2.0 only)**

The service provider determines the user's preferred identity provider (by unspecified means) and redirects the user agent to the SSO Service at the identity provider:

```
https://idp.example.org/SAML2/SSO/Redirect?SAMLRequest=request
```

The value of the

SAMLRequest

parameter (denoted by the placeholder

request

above) is the

Base64

encoding of a

deflated

<samlp:AuthnRequest>

element.

**3. Request the SSO Service at the IdP (SAML 2.0 only)**

The user agent issues a GET request to the SSO service at the URL from step 2. The SSO service processes the

AuthnRequest

(sent via the

SAMLRequest

URL query parameter) and performs a security check. If the user does not have a valid security context, the identity provider identifies the user (details omitted).

**4. Respond with an XHTML form**

The SSO service validates the request and responds with a document containing an XHTML form:

```mw
  <form method="post" action="https://sp.example.com/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLResponse" value="response" />
    ...
    <input type="submit" value="Submit" />
  </form>
```

The value of the

SAMLResponse

element (denoted by the placeholder

response

above) is the base64 encoding of a

<samlp:Response>

element.

**5. Request the Assertion Consumer Service at the SP**

The user agent issues a POST request to the assertion consumer service at the service provider. The value of the

SAMLResponse

parameter is taken from the XHTML form at step 4.

**6. Redirect to the target resource**

The assertion consumer service processes the response, creates a security context at the service provider and redirects the user agent to the target resource.

**7. Request the target resource at the SP again**

The user agent requests the target resource at the service provider (again):

```
https://sp.example.com/myresource
```

**8. Respond with requested resource**

Since a security context exists, the service provider returns the resource to the user agent.

In SAML 1.1, the flow begins with a request to the identity provider's inter-site transfer service at step 3.

In the example flow above, all depicted exchanges are *front-channel exchanges*, that is, an HTTP user agent (browser) communicates with a SAML entity at each step. In particular, there are no *back-channel exchanges* or direct communications between the service provider and the identity provider. Front-channel exchanges lead to simple protocol flows where all messages are passed *by value* using a simple HTTP binding (GET or POST). Indeed, the flow outlined in the previous section is sometimes called the *Lightweight Web Browser SSO Profile*.

Alternatively, for increased security or privacy, messages may be passed *by reference*. For example, an identity provider may supply a reference to a SAML assertion (called an *artifact*) instead of transmitting the assertion directly through the user agent. Subsequently, the service provider requests the actual assertion via a back channel. Such a back-channel exchange is specified as a SOAP message exchange (SAML over SOAP over HTTP). In general, any SAML exchange over a secure back channel is conducted as a SOAP message exchange.

On the back channel, SAML specifies the use of SOAP 1.1. The use of SOAP as a binding mechanism is optional, however. Any given SAML deployment will choose whatever bindings are appropriate.
