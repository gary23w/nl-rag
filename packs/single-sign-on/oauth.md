---
title: "OAuth"
source: https://en.wikipedia.org/wiki/OAuth
domain: single-sign-on
license: CC-BY-SA-4.0
tags: single sign on, security assertion markup language, openid connect, federated identity, oauth authorization
fetched: 2026-07-02
---

# OAuth

**OAuth** (short for **open authorization**) is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites but without giving them the passwords. This mechanism is used by companies such as Amazon, Google, Meta Platforms, Microsoft, and Twitter to permit users to share information about their accounts with third-party applications or websites.

Generally, the OAuth protocol provides a way for resource owners to provide a client application with secure delegated access to server resources. It specifies a process for resource owners to authorize third-party access to their server resources without providing credentials. Designed specifically to work with Hypertext Transfer Protocol (HTTP), OAuth essentially allows access tokens to be issued to third-party clients by an authorization server, with the approval of the resource owner. The third party then uses the access token to access the protected resources hosted by the resource server.

## History

OAuth began in November 2006 when Blaine Cook was developing an OpenID implementation for Twitter. Meanwhile, Ma.gnolia needed a solution to allow its members with OpenIDs to authorize Mac OS X Dashboard widgets to access their service. Cook, Chris Messina and Larry Halff from Magnolia met with David Recordon to discuss using OpenID with the Twitter and Magnolia APIs to delegate authentication. They concluded that there were no open standards for API access delegation.

The OAuth discussion group was created in April 2007, for a small group of implementers to write the draft proposal for an open protocol. DeWitt Clinton from Google learned of the OAuth project, and expressed his interest in supporting the effort. In July 2007, the team drafted an initial specification. Eran Hammer joined and coordinated the many OAuth contributions creating a more formal specification. On 3 October 2007, the OAuth Core 1.0 final draft was released.

At the 73rd Internet Engineering Task Force (IETF) meeting in Minneapolis in November 2008, an OAuth BoF was held to discuss bringing the protocol into the IETF for further standardization work. The event was well attended and there was wide support for formally chartering an OAuth working group within the IETF.

The OAuth 1.0 protocol was published as RFC 5849, an informational Request for Comments, in April 2010. Since 31 August 2010, all third party Twitter applications have been required to use OAuth.

The OAuth 2.0 framework was published considering additional use cases and extensibility requirements gathered from the wider IETF community. Albeit being built on the OAuth 1.0 deployment experience, OAuth 2.0 is not backwards compatible with OAuth 1.0. OAuth 2.0 was published as RFC 6749 and the Bearer Token Usage specification as RFC 6750, both standards track Requests for Comments, in October 2012.

As of November 2024, the OAuth 2.1 Authorization Framework draft is a work in progress. It consolidates the functionality in RFCs OAuth 2.0, OAuth 2.0 for Native Apps, Proof Key for Code Exchange, OAuth 2.0 for Browser-Based Apps, OAuth Security Best Current, and Bearer Token Usage.

## Security issues

### OAuth 1.0

On 23 April 2009, a session fixation security flaw in the 1.0 protocol was announced. It affects the OAuth authorization flow (also known as "3-legged OAuth") in OAuth Core 1.0 Section 6. Version 1.0a of the OAuth Core protocol was issued to address this issue.

### OAuth 2.0

In January 2013, the Internet Engineering Task Force published a threat model for OAuth 2.0. Among the threats outlined is one called "Open Redirector"; in early 2014, a variant of this was described under the name "Covert Redirect" by Wang Jing.

OAuth 2.0 has been analyzed using formal web protocol analysis. This analysis revealed that in setups with multiple authorization servers, one of which is behaving maliciously, clients can become confused about the authorization server to use and may forward secrets to the malicious authorization server (AS Mix-Up Attack). This prompted the creation of a new best current practice internet draft that sets out to define a new security standard for OAuth 2.0. Assuming a fix against the AS Mix-Up Attack in place, the security of OAuth 2.0 has been proven under strong attacker models using formal analysis.

One implementation of OAuth 2.0 with numerous security flaws has been exposed.

In April and May 2017, about one million users of Gmail (less than 0.1% of users as of May 2017) were targeted by an OAuth-based phishing attack, receiving an email purporting to be from a colleague, employer or friend wanting to share a document on Google Docs. Those who clicked on the link within the email were directed to sign in and allow a potentially malicious third-party program called "Google Apps" to access their "email account, contacts and online documents". Within "approximately one hour", the phishing attack was stopped by Google, who advised those who had given "Google Apps" access to their email to revoke such access and change their passwords.

In the draft of OAuth 2.1 the use of the PKCE (RFC 7636) extension for native apps has been recommended to all kinds of OAuth clients, including web applications and other confidential clients in order to prevent malicious browser extensions from performing OAuth 2.0 code injection attacks.

## Types

OAuth framework specifies several grant types for different use cases. Some of the most common OAuth grant types are:

- Authorization Code
- PKCE
- Client Credentials
- Device Code
- Refresh Token
- Resource Owner Password Credentials (ROPC)

## Uses

Facebook's Graph API only supports OAuth 2.0. Google supports OAuth 2.0 as the recommended authorization mechanism for all of its APIs. Microsoft also supports OAuth 2.0 for various APIs and its Azure Active Directory service, which is used to secure many Microsoft and third party APIs.

OAuth can be used as an authorizing mechanism to access secured RSS/Atom feeds. Access to RSS/ATOM feeds that require authentication has always been an issue. For example, an RSS feed from a secured Google Site could not have been accessed using Google Reader. Instead, three-legged OAuth would have been used to authorize that RSS client to access the feed from the Google Site.

Free software client implementations of the OAuth2 protocol such as the LibreOffice OAuth2OOo extension allows access to remote resources (ie: via the Google API or the Microsoft Graph API and OAuth 2.0) and possibly even with the LibreOffice Basic language. This makes it very easy to write and use HTTP requests supporting the OAuth 2.0 protocol in LibreOffice macros.

## OAuth and other standards

OAuth is a service that is complementary to and distinct from OpenID. OAuth is unrelated to OATH, which is a reference architecture for authentication, not a standard for authorization. However, OAuth is directly related to OpenID Connect (OIDC), since OIDC is an authentication layer built on top of OAuth 2.0. OAuth is also unrelated to XACML, which is an authorization policy standard. OAuth can be used in conjunction with XACML, where OAuth is used for ownership consent and access delegation whereas XACML is used to define the authorization policies (e.g., managers can view documents in their region).

### OpenID vis-à-vis pseudo-authentication using OAuth

OAuth is an *authorization* protocol, rather than an *authentication* protocol. Using OAuth on its own as an authentication method may be referred to as pseudo-authentication. The following diagrams highlight the differences between using OpenID (specifically designed as an authentication protocol) and OAuth for authorization.

The communication flow in both processes is similar:

1. (Not pictured) The user requests a resource or site login from the application.
2. The site sees that the user is not authenticated. It formulates a request for the identity provider, encodes it, and sends it to the user as part of a redirect URL.
3. The user's browser makes a request to the redirect URL for the identity provider, including the application's request
4. If necessary, the identity provider authenticates the user (perhaps by asking them for their username and password)
5. Once the identity provider is satisfied that the user is sufficiently authenticated, it processes the application's request, formulates a response, and sends that back to the user along with a redirect URL back to the application.
6. The user's browser requests the redirect URL that goes back to the application, including the identity provider's response
7. The application decodes the identity provider's response, and carries on accordingly.
8. (OAuth only) The response includes an access token which the application can use to gain direct access to the identity provider's services on the user's behalf.

The crucial difference is that in the OpenID *authentication* use case, the response from the identity provider is an assertion of identity; while in the OAuth *authorization* use case, the identity provider is also an API provider, and the response from the identity provider is an access token that may grant the application ongoing access to some of the identity provider's APIs, on the user's behalf. The access token acts as a kind of "valet key" that the application can include with its requests to the identity provider, which prove that it has permission from the user to access those APIs.

Because the identity provider typically (but not always) authenticates the user as part of the process of granting an OAuth access token, it is tempting to view a successful OAuth access token request as an authentication method itself. However, because OAuth was not designed with this use case in mind, making this assumption can lead to major security flaws.

(OpenID vs. pseudo-authentication using OAuth)

### OAuth and XACML

XACML is a policy-based, attribute-based access control authorization framework. It provides:

- An access control architecture.
- A policy language with which to express a wide range of access control policies including policies that can use consents handled / defined via OAuth.
- A request / response scheme to send and receive authorization requests.

XACML and OAuth can be combined to deliver a more comprehensive approach to authorization. OAuth does not provide a policy language with which to define access control policies. XACML can be used for its policy language.

Where OAuth focuses on delegated access (I, the user, grant Twitter access to my Facebook wall), and identity-centric authorization, XACML takes an attribute-based approach which can consider attributes of the user, the action, the resource, and the context (who, what, where, when, how). With XACML it is possible to define policies such as

- Managers can view documents in their department
- Managers can edit documents they own in draft mode

XACML provides more fine-grained access control than OAuth does. OAuth is limited in granularity to the coarse functionality (the scopes) exposed by the target service. As a result, it often makes sense to combine OAuth and XACML together where OAuth will provide the delegated access use case and consent management and XACML will provide the authorization policies that work on the applications, processes, and data.

Lastly, XACML can work transparently across multiple stacks (APIs, web SSO, ESBs, home-grown apps, databases...). OAuth focuses exclusively on HTTP-based apps.

## Controversy

Eran Hammer resigned from his role of lead author for the OAuth 2.0 project, withdrew from the IETF working group, and removed his name from the specification in July 2012. Hammer cited a conflict between web and enterprise cultures as his reason for leaving, noting that IETF is a community that is "all about enterprise use cases" and "not capable of simple". "What is now offered is a blueprint for an authorization protocol", he noted, "that is the enterprise way", providing a "whole new frontier to sell consulting services and integration solutions". In comparing OAuth 2.0 with OAuth 1.0, Hammer points out that it has become "more complex, less interoperable, less useful, more incomplete, and most importantly, less secure". He explains how architectural changes for 2.0 unbound tokens from clients, removed all signatures and cryptography at a protocol level and added expiring tokens (because tokens could not be revoked) while complicating the processing of authorization. Numerous items were left unspecified or unlimited in the specification because "as has been the nature of this working group, no issue is too small to get stuck on or leave open for each implementation to decide."

David Recordon later also removed his name from the specifications for unspecified reasons. Dick Hardt took over the editor role, and the framework was published in October 2012.

David Harris, author of the email client Pegasus Mail, has criticised OAuth 2.0 as "an absolute dog's breakfast", requiring developers to write custom modules specific to each service (Gmail, Microsoft Mail services, etc.), and to register specifically with them.
