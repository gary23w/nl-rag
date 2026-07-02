---
title: "SAML 2.0 (part 1/2)"
source: https://en.wikipedia.org/wiki/SAML_2.0
domain: saml-security
license: CC-BY-SA-4.0
tags: security assertion markup language, saml assertion validation, xml signature wrapping defense, identity federation security
fetched: 2026-07-02
part: 1/2
---

# SAML 2.0

**Security Assertion Markup Language** (**SAML**) **2.0** is a version of the SAML standard for exchanging authentication and authorization identities between security domains. SAML 2.0 is an XML-based protocol that uses security tokens containing assertions to pass information about a principal (usually an end user) between a SAML authority, named an Identity Provider, and a SAML consumer, named a Service Provider. SAML 2.0 enables web-based, cross-domain single sign-on (SSO), which helps reduce the administrative overhead of distributing multiple authentication tokens to the user. SAML 2.0 was ratified as an OASIS Standard in March 2005, replacing SAML 1.1. The critical aspects of SAML 2.0 are covered in detail in the official documents SAMLCore, SAMLBind, SAMLProf, and SAMLMeta.

Some 30 individuals from more than 24 companies and organizations were involved in the creation of SAML 2.0. In particular, and of special note, Liberty Alliance donated its Identity Federation Framework (ID-FF) specification to OASIS, which became the basis of the SAML 2.0 specification. Thus SAML 2.0 represents the convergence of SAML 1.1, Liberty ID-FF 1.2 Archived 2021-02-24 at the Wayback Machine, and Shibboleth 1.3.


## SAML 2.0 assertions

An assertion is a package of information that supplies zero or more statements made by a SAML authority. SAML assertions are usually made about a subject, represented by the `<Subject>` element. The SAML 2.0 specification defines three different kinds of assertion statements that can be created by a SAML authority. All SAML-defined statements are associated with a subject. The three kinds of assertion statements are defined as follows:

- Authentication Statement: The assertion subject was authenticated by a particular means at a particular time.
- Attribute Statement: The assertion subject is associated with the supplied attributes.
- Authorization Decision Statement: A request to allow the assertion subject to access the specified resource has been granted or denied.

An important type of SAML assertion is the so-called "bearer" assertion used to facilitate Web Browser SSO. Here is an example of a short-lived bearer assertion issued by an identity provider (https://idp.example.org/SAML2) to a service provider (https://sp.example.com/SAML2). The assertion includes both an Authentication Assertion `<saml:AuthnStatement>` and an Attribute Assertion `<saml:AttributeStatement>`, which presumably the service provider uses to make an access control decision. The prefix `saml:` represents the SAML V2.0 assertion namespace.

### Example of SAML

```mw
<saml:Assertion
   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
   xmlns:xs="http://www.w3.org/2001/XMLSchema"
   ID="_d71a3a8e9fcc45c9e9d248ef7049393fc8f04e5f75"
   Version="2.0"
   IssueInstant="2004-12-05T09:22:05Z">
   <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
   <ds:Signature
     xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
   <saml:Subject>
     <saml:NameID
       Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient">
       3f7b3dcf-1674-4ecd-92c8-1544f346baf8
     </saml:NameID>
     <saml:SubjectConfirmation
       Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
       <saml:SubjectConfirmationData
         InResponseTo="aaf23196-1773-2113-474a-fe114412ab72"
         Recipient="https://sp.example.com/SAML2/SSO/POST"
         NotOnOrAfter="2004-12-05T09:27:05Z"/>
     </saml:SubjectConfirmation>
   </saml:Subject>
   <saml:Conditions
     NotBefore="2004-12-05T09:17:05Z"
     NotOnOrAfter="2004-12-05T09:27:05Z">
     <saml:AudienceRestriction>
       <saml:Audience>https://sp.example.com/SAML2</saml:Audience>
     </saml:AudienceRestriction>
   </saml:Conditions>
   <saml:AuthnStatement
     AuthnInstant="2004-12-05T09:22:00Z"
     SessionIndex="b07b804c-7c29-ea16-7300-4f3d6f7928ac">
     <saml:AuthnContext>
       <saml:AuthnContextClassRef>
         urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
       </saml:AuthnContextClassRef>
     </saml:AuthnContext>
   </saml:AuthnStatement>
   <saml:AttributeStatement>
     <saml:Attribute
       xmlns:x500="urn:oasis:names:tc:SAML:2.0:profiles:attribute:X500"
       x500:Encoding="LDAP"
       NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
       Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.1"
       FriendlyName="eduPersonAffiliation">
       <saml:AttributeValue
         xsi:type="xs:string">member</saml:AttributeValue>
       <saml:AttributeValue
         xsi:type="xs:string">staff</saml:AttributeValue>
     </saml:Attribute>
   </saml:AttributeStatement>
 </saml:Assertion>
```

Note that in the above example the `<saml:Assertion>` element contains the following child elements:

- a `<saml:Issuer>` element, which contains the unique identifier of the identity provider
- a `<ds:Signature>` element, which contains an integrity-preserving digital signature (not shown) over the `<saml:Assertion>` element
- a `<saml:Subject>` element, which identifies the authenticated principal (but in this case the identity of the principal is hidden behind an opaque transient identifier, for reasons of privacy)
- a `<saml:Conditions>` element, which gives the conditions under which the assertion is to be considered *valid*
- a `<saml:AuthnStatement>` element, which describes the act of authentication at the identity provider
- a `<saml:AttributeStatement>` element, which asserts a multi-valued attribute associated with the authenticated principal

In words, the assertion encodes the following information:

> The assertion ("b07b804c-7c29-ea16-7300-4f3d6f7928ac") was issued at time "2004-12-05T09:22:05Z" by identity provider (https://idp.example.org/SAML2) regarding subject (3f7b3dcf-1674-4ecd-92c8-1544f346baf8) exclusively for service provider (https://sp.example.com/SAML2).

The authentication statement, in particular, asserts the following:

> The principal identified in the `<saml:Subject>` element was authenticated at time "2004-12-05T09:22:00Z" by means of a password sent over a protected channel.

Likewise the attribute statement asserts that:

> The principal identified in the `<saml:Subject>` element has the 'staff' and 'member' attributes at this institution.


## SAML 2.0 protocols

The following protocols are specified in SAMLCore:

- Assertion Query and Request Protocol
- Authentication Request Protocol
- Artifact Resolution Protocol
- Name Identifier Management Protocol
- Single Logout Protocol
- Name Identifier Mapping Protocol

The most important of these protocols—the Authentication Request Protocol—is discussed in detail below.

### Authentication Request Protocol

In SAML 1.1 Web Browser SSO Profiles are initiated by the Identity Provider (IDP), that is, an unsolicited `<samlp:Response>` element is transmitted from the identity provider to the service provider (via the browser). (The prefix `samlp:` denotes the SAML protocol namespace.)

In SAML 2.0, however, the flow begins at the service provider who issues an explicit authentication request to the identity provider. The resulting *Authentication Request Protocol* is a significant new feature of SAML 2.0.

When a principal (or an entity acting on the principal's behalf) wishes to obtain an assertion containing an authentication statement, a `<samlp:AuthnRequest>` element is transmitted to the identity provider:

```mw
  <samlp:AuthnRequest
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="aaf23196-1773-2113-474a-fe114412ab72"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:59Z"
    AssertionConsumerServiceIndex="0"
    AttributeConsumingServiceIndex="0">
    <saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
    <samlp:NameIDPolicy
      AllowCreate="true"
      Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"/>
  </samlp:AuthnRequest>
```

The above `<samlp:AuthnRequest>` element, which implicitly requests an assertion containing an authentication statement, was evidently issued by a service provider (https://sp.example.com/SAML2) and subsequently presented to the identity provider (via the browser). The identity provider authenticates the principal (if necessary) and issues an authentication response, which is transmitted back to the service provider (again via the browser).

### Artifact Resolution Protocol

A SAML message is transmitted from one entity to another either *by value* or *by reference*. A reference to a SAML message is called an *artifact*. The receiver of an artifact resolves the reference by sending a `<samlp:ArtifactResolve>` request directly to the issuer of the artifact, who then responds with the actual message referenced by the artifact.

Suppose, for example, that an identity provider sends the following `<samlp:ArtifactResolve>` request directly to a service provider (via a back channel):

```mw
  <samlp:ArtifactResolve
 xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
  xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="_cce4ee769ed970b501d680f697989d14"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:58Z">
    <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
    <!-- an ArtifactResolve message SHOULD be signed -->
    <ds:Signature
      xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
    <samlp:Artifact>AAQAAMh48/1oXIM+sDo7Dh2qMp1HM4IF5DaRNmDj6RdUmllwn9jJHyEgIi8=</samlp:Artifact>
  </samlp:ArtifactResolve>
```

In response, the service provider returns the SAML element referenced by the enclosed artifact. This protocol forms the basis of the HTTP Artifact Binding.


## SAML 2.0 bindings

The *bindings* supported by SAML 2.0 are outlined in the Bindings specification (SAMLBind):

- SAML SOAP Binding (based on SOAP 1.1)
- Reverse SOAP (PAOS) Binding
- HTTP Redirect Binding
- HTTP POST Binding
- HTTP Artifact Binding
- SAML URI Binding

For Web Browser SSO, the HTTP Redirect Binding and the HTTP POST Binding are commonly used. For example, the service provider may use HTTP Redirect to send a request while the identity provider uses HTTP POST to transmit the response. This example illustrates that an entity's choice of binding is independent of its partner's choice of binding.

### HTTP Redirect Binding

SAML protocol messages can be carried directly in the URL query string of an HTTP GET request. Since the length of URLs is limited in practice, the HTTP Redirect binding is suitable for short messages, such as the `<samlp:AuthnRequest>` message. Longer messages (e.g. those containing signed or encrypted SAML assertions, such as SAML Responses) are usually transmitted via other bindings such as the HTTP POST Binding.

SAML requests or responses transmitted via HTTP Redirect have a `SAMLRequest` or `SAMLResponse` query string parameter, respectively. Before it's sent, the message is deflated (without header and checksum), base64-encoded, and URL-encoded, in that order. Upon receipt, the process is reversed to recover the original message.

For example, encoding the `<samlp:AuthnRequest>` message above yields:

```
 https://idp.example.org/SAML2/SSO/Redirect?SAMLRequest=fZFfa8IwFMXfBb9DyXvaJtZ1BqsURRC2
 Mabbw95ivc5Am3TJrXPffmmLY3%2FA15Pzuyf33On8XJXBCaxTRmeEhTEJQBdmr%2FRbRp63K3pL5rPhYOpkVdY
 ib%2FCon%2BC9AYfDQRB4WDvRvWWksVoY6ZQTWlbgBBZik9%2FfCR7GorYGTWFK8pu6DknnwKL%2FWEetlxmR8s
 BHbHJDWZqOKGdsRJM0kfQAjCUJ43KX8s78ctnIz%2Blp5xpYa4dSo1fjOKGM03i8jSeCMzGevHa2%2FBK5MNo1F
 dgN2JMqPLmHc0b6WTmiVbsGoTf5qv66Zq2t60x0wXZ2RKydiCJXh3CWVV1CWJgqanfl0%2Bin8xutxYOvZL18NK
 UqPlvZR5el%2BVhYkAgZQdsA6fWVsZXE63W2itrTQ2cVaKV2CjSSqL1v9P%2FAXv4C
```

The above message (formatted for readability) may be signed for additional security. In practice, all the data contained in a `<samlp:AuthnRequest>`, such as `Issuer` which contains the SP ID, and `NameIDPolicy`, has been agreed between IdP and SP beforehand (via manual information exchange or via SAML metadata). In that case signing the request is not a security constraint. When the `<samlp:AuthnRequest>` contains information not known by the IdP beforehand, such as Assertion Consumer Service URL, signing the request is recommended for security purposes.

### HTTP POST Binding

In the following example, both the service provider and the identity provider use an HTTP POST binding. Initially, the service provider responds to a request from the user agent with a document containing an XHTML form:

```mw
  <form method="post" action="https://idp.example.org/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLRequest" value="''request''" />
    ... other input parameter....
  </form>
```

The value of the `SAMLRequest` parameter is the base64-encoding of a `<samlp:AuthnRequest>` element, which is transmitted to the identity provider via the browser. The SSO service at the identity provider validates the request and responds with a document containing another XHTML form:

```mw
  <form method="post" action="https://sp.example.com/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLResponse" value="''response''" />
    ...
  </form>
```

The value of the `SAMLResponse` parameter is the base64 encoding of a `<samlp:Response>` element, which likewise is transmitted to the service provider via the browser.

To automate the submission of the form, the following line of JavaScript may appear anywhere on the XHTML page:

```mw
  window.onload = function () { document.forms[0].submit(); }
```

This assumes, of course, that the first form element in the page contains the above SAMLResponse containing `form` element (`forms[0]`).

### HTTP Artifact Binding

The HTTP Artifact Binding uses the Artifact Resolution Protocol and the SAML SOAP Binding (over HTTP) to resolve a SAML message by reference. Consider the following specific example. Suppose a service provider wants to send a `<samlp:AuthnRequest>` message to an identity provider. Initially, the service provider transmits an artifact to the identity provider via an HTTP redirect:

```
 https://idp.example.org/SAML2/SSO/Artifact?SAMLart=artifact
```

Next the identity provider sends a `<samlp:ArtifactResolve>` request (such as the ArtifactResolveRequest shown earlier) directly to the service provider via a back channel. Finally, the service provider returns a `<samlp:ArtifactResponse>` element containing the referenced `<samlp:AuthnRequest>` message:

```mw
  <samlp:ArtifactResponse
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    ID="_d84a49e5958803dedcff4c984c2b0d95"
    InResponseTo="_cce4ee769ed970b501d680f697989d14"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:59Z">
    <!-- an ArtifactResponse message SHOULD be signed -->
    <ds:Signature
      xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
    <samlp:Status>
      <samlp:StatusCode
        Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
    </samlp:Status>
    <samlp:AuthnRequest
      xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
      xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
      ID="_306f8ec5b618f361c70b6ffb1480eade"
      Version="2.0"
      IssueInstant="2004-12-05T09:21:59Z"
      Destination="https://idp.example.org/SAML2/SSO/Artifact"
      ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact"
      AssertionConsumerServiceURL="https://sp.example.com/SAML2/SSO/Artifact">
      <saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
      <samlp:NameIDPolicy
        AllowCreate="false"
        Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"/>
    </samlp:AuthnRequest>
  </samlp:ArtifactResponse>
```

Of course the flow can go in the other direction as well, that is, the identity provider may issue an artifact, and in fact this is more common. See, for example, the "double artifact" profile example later in this topic.

#### Artifact format

In general, a SAML 2.0 *artifact* is defined as follows (SAMLBind):

```
 SAML_artifact := B64 (TypeCode EndpointIndex RemainingArtifact)
 TypeCode      := Byte1Byte2
 EndpointIndex := Byte1Byte2
```

Thus a SAML 2.0 artifact consists of three components: a two-byte `TypeCode`, a two-byte `EndpointIndex`, and an arbitrary sequence of bytes called the `RemainingArtifact`. These three pieces of information are concatenated and base64-encoded to yield the complete artifact.

The `TypeCode` uniquely identifies the artifact format. SAML 2.0 predefines just one such artifact, of type 0x0004. The `EndpointIndex` is a reference to a particular artifact resolution endpoint managed by the artifact issuer (which may be either the IdP or the SP, as mentioned earlier). The `RemainingArtifact`, which is determined by the type definition, is the "meat" of the artifact.

The format of a *type 0x0004 artifact* is further defined as follows:

```
 TypeCode            := 0x0004
 RemainingArtifact   := SourceId MessageHandle
 SourceId            := 20-byte_sequence
 MessageHandle       := 20-byte_sequence
```

Thus a type 0x0004 artifact is of size 44 bytes (unencoded). The `SourceId` is an arbitrary sequence of bytes, although in practice, the `SourceId` is the SHA-1 hash of the issuer's entityID. The `MessageHandle` is a random sequence of bytes that references a SAML message that the artifact issuer is willing to produce on-demand.

For example, consider this hex-encoded type 0x0004 artifact:

```
 00040000c878f3fd685c833eb03a3b0e1daa329d47338205e436913660e3e917549a59709fd8c91f2120222f
```

If you look closely, you can see the `TypeCode` (0x0004) and the `EndpointIndex` (0x0000) at the front of the artifact. The next 20 bytes are the SHA-1 hash of the issuer's entityID (https://idp.example.org/SAML2) followed by 20 random bytes. The base64-encoding of these 44 bytes is what you see in the ArtifactResolveRequest example above.
