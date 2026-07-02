---
title: "Integrated Windows Authentication"
source: https://en.wikipedia.org/wiki/Integrated_Windows_Authentication
domain: single-sign-on-deep
license: CC-BY-SA-4.0
tags: single sign on, central authentication service, integrated windows authentication, kerberos authentication, identity provider
fetched: 2026-07-02
---

# Integrated Windows Authentication

**Integrated Windows Authentication** (**IWA**) is a term associated with Microsoft products that refers to the SPNEGO, Kerberos, and NTLMSSP authentication protocols with respect to SSPI functionality introduced with Microsoft Windows 2000 and included with later Windows NT-based operating systems. The term is used more commonly for the automatically authenticated connections between Microsoft Internet Information Services, Internet Explorer, and other Active Directory aware applications.

IWA is also known by several names like *HTTP Negotiate authentication*, *NT Authentication*, *NTLM Authentication*, *Domain authentication*, *Windows Integrated Authentication*, *Windows NT Challenge/Response authentication*, or simply *Windows Authentication*.

## Overview

Integrated Windows Authentication uses the security features of Windows clients and servers. Unlike Basic Authentication or Digest Authentication, initially, it does not prompt users for a user name and password. The current Windows user information on the client computer is supplied by the web browser through a cryptographic exchange involving hashing with the Web server. If the authentication exchange initially fails to identify the user, the web browser will prompt the user for a Windows user account user name and password.

Integrated Windows Authentication itself is not a standard or an authentication protocol. When IWA is selected as an option of a program (e.g. within the *Directory Security* tab of the IIS site properties dialog) this implies that underlying security mechanisms should be used in a preferential order. If the Kerberos provider is functional and a Kerberos ticket can be obtained for the target, and any associated settings permit Kerberos authentication to occur (e.g. Intranet sites settings in Internet Explorer), the Kerberos 5 protocol will be attempted. Otherwise NTLMSSP authentication is attempted. Similarly, if Kerberos authentication is attempted, yet it fails, then NTLMSSP is attempted. IWA uses SPNEGO to allow initiators and acceptors to negotiate either Kerberos or NTLMSSP. Third party utilities have extended the Integrated Windows Authentication paradigm to UNIX, Linux and Mac systems.

## Supported web browsers

Integrated Windows Authentication works with most modern web browsers, but does not work over some HTTP proxy servers. Therefore, it is best for use in intranets where all the clients are within a single domain. It may work with other web browsers if they have been configured to pass the user's logon credentials to the server that is requesting authentication. Where a proxy itself requires NTLM authentication, some applications like Java may not work because the protocol is not described in RFC-2069 for proxy authentication.

- Internet Explorer 2 and later versions.
- In Mozilla Firefox on Windows operating systems, the names of the domains/websites to which the authentication is to be passed can be entered (comma delimited for multiple domains) for the "*network.negotiate-auth.trusted-uris*" (for Kerberos) or in the "*network.automatic-ntlm-auth.trusted-uris*" (NTLM) Preference Name on the *about:config* page. On the Macintosh operating systems this works if you have a kerberos ticket (use negotiate). Some websites may also require configuring the "*network.negotiate-auth.delegation-uris*".
- Opera 9.01 and later versions can use NTLM/Negotiate, but will use Basic or Digest authentication if that is offered by the server.
- Google Chrome works as of 8.0.
- Safari works, once you have a Kerberos ticket.
- Microsoft Edge 77 and later.

## Supported mobile browsers

iOS natively supports Kerberos via Kerberos Single Sign-on extension. Configuring the extension enables Safari and Edge to use Kerberos.

Android has SPNEGO support in Chrome which is adding Kerberos support with a solution like Hypergate Authenticator.
