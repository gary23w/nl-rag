---
title: "SAML 2.0 (part 2/2)"
source: https://en.wikipedia.org/wiki/SAML_2.0
domain: saml-deep
license: CC-BY-SA-4.0
tags: saml assertion, saml2 protocol, saml metadata exchange, service provider sso, identity provider initiated
fetched: 2026-07-02
part: 2/2
---

## SAML 2.0 profiles

In SAML 2.0, as in SAML 1.1, the primary use case is still Web Browser SSO, but the scope of SAML 2.0 is broader than previous versions of SAML, as suggested in the following exhaustive list of profiles:

- SSO Profiles
  - Web browser SSO profile
  - Enhanced Client or Proxy (ECP) Profile
  - Identity Provider Discovery Profile
  - Single Logout Profile
  - Name Identifier Management Profile
- Artifact Resolution Profile
- Assertion Query/Request Profile
- Name Identifier Mapping Profile
- SAML Attribute Profiles
  - Basic Attribute Profile
  - X.500/LDAP Attribute Profile
  - UUID Attribute Profile
  - DCE PAC Attribute Profile
  - XACML Attribute Profile

Although the number of supported profiles is quite large, the Profiles specification (SAMLProf) is simplified since the binding aspects of each profile have been factored out into a separate Bindings specification (SAMLBind).

### Web browser SSO profile

SAML 2.0 specifies a *Web Browser SSO Profile* involving an identity provider (IdP), a service provider (SP), and a principal wielding an HTTP user agent. The service provider has four bindings from which to choose while the identity provider has three, which leads to twelve possible deployment scenarios. We outline three of those deployment scenarios below.

#### SP redirect request; IdP POST response

This is one of the most common scenarios. The service provider sends a SAML Request to the IdP SSO Service using the HTTP-Redirect Binding. The identity provider returns the SAML Response to the SP Assertion Consumer Service using the HTTP-POST Binding.

The message flow begins with a request for a secured resource at the service provider.

**1. Request the target resource at the SP**

The principal (via an HTTP user agent) requests a target resource at the service provider:

```
 https://sp.example.com/myresource
```

The service provider performs a security check on behalf of the target resource. If a valid security context at the service provider already exists, skip steps 2–7.

The service provider may use any kind of mechanism to discover the identity provider that will be used, e.g., ask the user, use a preconfigured IdP, etc.

**2. Redirect to IdP SSO Service**

The service provider generates an appropriate SAMLRequest (and RelayState, if any), then redirects the browser to the IdP SSO Service using a standard HTTP 302 redirect.

```mw
302 Redirect
Location: https://idp.example.org/SAML2/SSO/Redirect?SAMLRequest=request&RelayState=token
```

The `RelayState` token is an opaque reference to state information maintained at the service provider. The value of the `SAMLRequest` parameter is a deflated, base64-encoded and URL-encoded value of an `<samlp:AuthnRequest>` element:

```mw
  <samlp:AuthnRequest
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_1"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:59Z"
    AssertionConsumerServiceIndex="0">
    <saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
    <samlp:NameIDPolicy
      AllowCreate="true"
      Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"/>
  </samlp:AuthnRequest>
```

The SAMLRequest may be signed using the SP signing key. Typically, however, this is not necessary.

**3. Request the SSO Service at the IdP**

The user agent issues a GET request to the SSO service at the identity provider:

```mw
GET /SAML2/SSO/Redirect?SAMLRequest=request&RelayState=token HTTP/1.1
Host: idp.example.org
```

where the values of the `SAMLRequest` and `RelayState` parameters are the same as those provided in the redirect. The SSO Service at the identity provider processes the `<samlp:AuthnRequest>` element (by URL-decoding, base64-decoding and inflating the request, in that order) and performs a security check. If the user does not have a valid security context, the identity provider identifies the user with any mechanism (details omitted).

**4. Respond with an XHTML form**

The SSO Service validates the request and responds with a document containing an XHTML form:

```mw
  <form method="post" action="https://sp.example.com/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLResponse" value="response" />
    <input type="hidden" name="RelayState" value="token" />
    ...
    <input type="submit" value="Submit" />
  </form>
```

The value of the `RelayState` parameter has been preserved from step 3. The value of the `SAMLResponse` parameter is the base64 encoding of the following `<samlp:Response>` element:

```mw
  <samlp:Response
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_2"
    InResponseTo="identifier_1"
    Version="2.0"
    IssueInstant="2004-12-05T09:22:05Z"
    Destination="https://sp.example.com/SAML2/SSO/POST">
    <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
    <samlp:Status>
      <samlp:StatusCode
        Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
    </samlp:Status>
    <saml:Assertion
      xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
      ID="identifier_3"
      Version="2.0"
      IssueInstant="2004-12-05T09:22:05Z">
      <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
      <!-- a POSTed assertion MUST be signed -->
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
            InResponseTo="identifier_1"
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
        SessionIndex="identifier_3">
        <saml:AuthnContext>
          <saml:AuthnContextClassRef>
            urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
         </saml:AuthnContextClassRef>
        </saml:AuthnContext>
      </saml:AuthnStatement>
    </saml:Assertion>
  </samlp:Response>
```

**5. Request the Assertion Consumer Service at the SP**

The user agent issues a POST request to the Assertion Consumer Service at the service provider:

```mw
POST /SAML2/SSO/POST HTTP/1.1
Host: sp.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: nnn
 
SAMLResponse=response&RelayState=token
```

where the values of the `SAMLResponse` and `RelayState` parameters are taken from the XHTML form at step 4.

**6. Redirect to the target resource**

The assertion consumer service processes the response, creates a security context at the service provider and redirects the user agent to the target resource.

**7. Request the target resource at the SP again**

The user agent requests the target resource at the service provider (again):

```
 https://sp.example.com/myresource
```

**8. Respond with requested resource**

Since a security context exists, the service provider returns the resource to the user agent.

#### SP POST Request; IdP POST Response

This is a relatively simple deployment of the SAML 2.0 Web Browser SSO Profile (SAMLProf) where both the service provider (SP) and the identity provider (IdP) use the HTTP POST binding.

The message flow begins with a request for a secured resource at the SP.

**1. Request the target resource at the SP**

The principal (via an HTTP user agent) requests a target resource at the service provider:

```
 https://sp.example.com/myresource
```

The service provider performs a security check on behalf of the target resource. If a valid security context at the service provider already exists, skip steps 2–7.

**2. Respond with an XHTML form**

The service provider responds with a document containing an XHTML form:

```mw
  <form method="post" action="https://idp.example.org/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLRequest" value="request" />
    <input type="hidden" name="RelayState" value="token" />
    ...
    <input type="submit" value="Submit" />
  </form>
```

The `RelayState` token is an opaque reference to state information maintained at the service provider. The value of the `SAMLRequest` parameter is the base64 encoding of the following `<samlp:AuthnRequest>` element:

```mw
  <samlp:AuthnRequest
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_1"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:59Z"
    AssertionConsumerServiceIndex="0">
    <saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
    <samlp:NameIDPolicy
      AllowCreate="true"
      Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"/>
  </samlp:AuthnRequest>
```

Before the `<samlp:AuthnRequest>` element is inserted into the XHTML form, it is first base64-encoded.

**3. Request the SSO Service at the IdP**

The user agent issues a POST request to the SSO service at the identity provider:

```mw
POST /SAML2/SSO/POST HTTP/1.1
Host: idp.example.org
Content-Type: application/x-www-form-urlencoded
Content-Length: nnn

SAMLRequest=request&RelayState=token
```

where the values of the `SAMLRequest` and `RelayState` parameters are taken from the XHTML form at step 2. The SSO service processes the `<samlp:AuthnRequest>` element (by URL-decoding, base64-decoding and inflating the request, in that order) and performs a security check. If the user does not have a valid security context, the identity provider identifies the user (details omitted).

**4. Respond with an XHTML form**

The SSO service validates the request and responds with a document containing an XHTML form:

```mw
  <form method="post" action="https://sp.example.com/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLResponse" value="response" />
    <input type="hidden" name="RelayState" value="token" />
    ...
    <input type="submit" value="Submit" />
  </form>
```

The value of the `RelayState` parameter has been preserved from step 3. The value of the `SAMLResponse` parameter is the base64 encoding of the following `<samlp:Response>` element:

```mw
  <samlp:Response
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_2"
    InResponseTo="identifier_1"
    Version="2.0"
    IssueInstant="2004-12-05T09:22:05Z"
    Destination="https://sp.example.com/SAML2/SSO/POST">
    <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
    <samlp:Status>
      <samlp:StatusCode
        Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
    </samlp:Status>
    <saml:Assertion
      xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
      ID="identifier_3"
      Version="2.0"
      IssueInstant="2004-12-05T09:22:05Z">
      <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
      <!-- a POSTed assertion MUST be signed -->
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
            InResponseTo="identifier_1"
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
        SessionIndex="identifier_3">
        <saml:AuthnContext>
          <saml:AuthnContextClassRef>
            urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
         </saml:AuthnContextClassRef>
        </saml:AuthnContext>
      </saml:AuthnStatement>
    </saml:Assertion>
  </samlp:Response>
```

**5. Request the Assertion Consumer Service at the SP**

The user agent issues a POST request to the assertion consumer service at the service provider:

```mw
POST /SAML2/SSO/POST HTTP/1.1
Host: sp.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: nnn
 
SAMLResponse=response&RelayState=token
```

where the values of the `SAMLResponse` and `RelayState` parameters are taken from the XHTML form at step 4.

**6. Redirect to the target resource**

The assertion consumer service processes the response, creates a security context at the service provider and redirects the user agent to the target resource.

**7. Request the target resource at the SP again**

The user agent requests the target resource at the service provider (again):

```
 https://sp.example.com/myresource
```

**8. Respond with requested resource**

Since a security context exists, the service provider returns the resource to the user agent.

#### SP redirect artifact; IdP redirect artifact

This is a complex deployment of the SAML 2.0 Web Browser SSO Profile (SAMLProf) where both the service provider (SP) and the identity provider (IdP) use the HTTP Artifact binding. Both artifacts are delivered to their respective endpoints via HTTP GET.

The message flow begins with a request for a secured resource at the SP:

**1. Request the target resource at the SP**

The principal (via an HTTP user agent) requests a target resource at the service provider:

```
 https://sp.example.com/myresource
```

The service provider performs a security check on behalf of the target resource. If a valid security context at the service provider already exists, skip steps 2–11.

**2. Redirect to the Single Sign-on (SSO) Service at the IdP**

The service provider redirects the user agent to the single sign-on (SSO) service at the identity provider. A `RelayState` parameter and a `SAMLart` parameter are appended to the redirect URL.

**3. Request the SSO Service at the IdP**

The user agent requests the SSO service at the identity provider:

```
 https://idp.example.org/SAML2/SSO/Artifact?SAMLart=artifact_1&RelayState=token
```

where `*token*` is an opaque reference to state information maintained at the service provider and `*artifact_1*` is a SAML artifact, both issued at step 2.

**4. Request the Artifact Resolution Service at the SP**

The SSO service dereferences the artifact by sending a `<samlp:ArtifactResolve>` element bound to a SAML SOAP message to the artifact resolution service at the service provider:

```mw
  <samlp:ArtifactResolve
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_1"
    Version="2.0"
    IssueInstant="2004-12-05T09:21:58Z"
    Destination="https://sp.example.com/SAML2/ArtifactResolution">
    <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
    <!-- an ArtifactResolve message SHOULD be signed -->
    <ds:Signature
      xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
    <samlp:Artifact>''artifact_1''</samlp:Artifact>
  </samlp:ArtifactResolve>
```

where the value of the `<samlp:Artifact>` element is the SAML artifact transmitted at step 3.

**5. Respond with a SAML AuthnRequest**

The artifact resolution service at the service provider returns a `<samlp:ArtifactResponse>` element (containing an `<samlp:AuthnRequest>` element) bound to a SAML SOAP message to the SSO service at the identity provider:

```mw
  <samlp:ArtifactResponse
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    ID="identifier_2"
    InResponseTo="identifier_1"
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
      ID="identifier_3"
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

The SSO service processes the `<samlp:AuthnRequest>` element and performs a security check. If the user does not have a valid security context, the identity provider identifies the user (details omitted).

**6. Redirect to the Assertion Consumer Service**

The SSO service at the identity provider redirects the user agent to the assertion consumer service at the service provider. The previous `RelayState` parameter and a new `SAMLart` parameter are appended to the redirect URL.

**7. Request the Assertion Consumer Service at the SP**

The user agent requests the assertion consumer service at the service provider:

```
 https://sp.example.com/SAML2/SSO/Artifact?SAMLart=artifact_2&RelayState=token
```

where `*token*` is the token value from step 3 and `*artifact_2*` is the SAML artifact issued at step 6.

**8. Request the Artifact Resolution Service at the IdP**

The assertion consumer service dereferences the artifact by sending a `<samlp:ArtifactResolve>` element bound to a SAML SOAP message to the artifact resolution service at the identity provider:

```mw
  <samlp:ArtifactResolve
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="identifier_4"
    Version="2.0"
    IssueInstant="2004-12-05T09:22:04Z"
    Destination="https://idp.example.org/SAML2/ArtifactResolution">
    <saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
    <!-- an ArtifactResolve message SHOULD be signed -->
    <ds:Signature
      xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
    <samlp:Artifact>''artifact_2''</samlp:Artifact>
  </samlp:ArtifactResolve>
```

where the value of the `<samlp:Artifact>` element is the SAML artifact transmitted at step 7.

**9. Respond with a SAML Assertion**

The artifact resolution service at the identity provider returns a `<samlp:ArtifactResponse>` element (containing an `<samlp:Response>` element) bound to a SAML SOAP message to the assertion consumer service at the service provider:

```mw
  <samlp:ArtifactResponse
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    ID="identifier_5"
    InResponseTo="identifier_4"
    Version="2.0"
    IssueInstant="2004-12-05T09:22:05Z">
    <!-- an ArtifactResponse message SHOULD be signed -->
    <ds:Signature
      xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
    <samlp:Status>
      <samlp:StatusCode
        Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
    </samlp:Status>
    <samlp:Response
      xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
      xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
      ID="identifier_6"
      InResponseTo="identifier_3"
      Version="2.0"
      IssueInstant="2004-12-05T09:22:05Z"
      Destination="https://sp.example.com/SAML2/SSO/Artifact">
      <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
      <ds:Signature
        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
      <samlp:Status>
        <samlp:StatusCode
          Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
      </samlp:Status>
      <saml:Assertion
        xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
        ID="identifier_7"
        Version="2.0"
        IssueInstant="2004-12-05T09:22:05Z">
        <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
        <!-- a Subject element is required -->
        <saml:Subject>
          <saml:NameID
            Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">
            user@mail.example.org
          </saml:NameID>
          <saml:SubjectConfirmation
            Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
            <saml:SubjectConfirmationData
              InResponseTo="identifier_3"
              Recipient="https://sp.example.com/SAML2/SSO/Artifact"
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
          SessionIndex="identifier_7">
          <saml:AuthnContext>
            <saml:AuthnContextClassRef>
              urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
           </saml:AuthnContextClassRef>
          </saml:AuthnContext>
        </saml:AuthnStatement>
      </saml:Assertion>
    </samlp:Response>
  </samlp:ArtifactResponse>
```

**10. Redirect to the target resource**

The assertion consumer service processes the response, creates a security context at the service provider and redirects the user agent to the target resource.

**11. Request the target resource at the SP again**

The user agent requests the target resource at the service provider (again):

```
 https://sp.example.com/myresource
```

**12. Respond with the requested resource**

Since a security context exists, the service provider returns the resource to the user agent.

### Identity provider discovery profile

The SAML 2.0 *Identity Provider Discovery Profile* introduces the following concepts:

- **Common Domain**
- **Common Domain Cookie**
- **Common Domain Cookie Writing Service**
- **Common Domain Cookie Reading Service**

As a hypothetical example of a *Common Domain*, let's suppose Example UK (example.co.uk) and Example Deutschland (example.de) belong to the virtual organization Example Global Alliance (example.com). In this example, the domain **example.com** is the common domain. Both Example UK and Example Deutschland have a presence in this domain (uk.example.com and de.example.com, resp.).

The *Common Domain Cookie* is a secure browser cookie scoped to the common domain. For each browser user, this cookie stores a history list of recently visited IdPs. The name and value of the cookie are specified in the IdP Discovery Profile (SAMLProf).

After a successful act of authentication, the IdP requests the *Common Domain Cookie Writing Service*. This service appends the IdP's unique identifier to the common domain cookie. The SP, when it receives an unauthenticated request for a protected resource, requests the *Common Domain Cookie Reading Service* to discover the browser user's most recently used IdP.

### Assertion query/request profile

The *Assertion Query/Request Profile* is a general profile that accommodates numerous types of so-called *queries* using the following SAML 2.0 elements:

- the `<samlp:AssertionIDRequest>` element, which is used to request an assertion given its unique identifier (`ID`)
- the `<samlp:SubjectQuery>` element, which is an abstract extension point that allows new subject-based SAML queries to be defined
- the `<samlp:AuthnQuery>` element, which is used to request **existing** authentication assertions about a given subject from an Authentication Authority
- the `<samlp:AttributeQuery>` element, which is used to request attributes about a given subject from an Attribute Authority
- the `<samlp:AuthzDecisionQuery>` element, which is used to request an authorization decision from a trusted third party

The SAML SOAP binding is often used in conjunction with queries.

#### SAML attribute query

The *Attribute Query* is perhaps the most important type of SAML query. Often a requester, acting on behalf of the principal, queries an identity provider for attributes. Below we give an example of a query issued by a principal directly:

```mw
  <samlp:AttributeQuery
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    ID="aaf23196-1773-2113-474a-fe114412ab72"
    Version="2.0"
    IssueInstant="2006-07-17T20:31:40Z">
    <saml:Issuer
      Format="urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName">
      CN=trscavo@example.com,OU=User,O=NCSA-TEST,C=US
    </saml:Issuer>
    <saml:Subject>
      <saml:NameID
        Format="urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName">
        CN=trscavo@example.com,OU=User,O=NCSA-TEST,C=US
      </saml:NameID>
    </saml:Subject>
    <saml:Attribute
      NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
      Name="urn:oid:2.5.4.42"
      FriendlyName="givenName">
    </saml:Attribute>
    <saml:Attribute
      NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
      Name="urn:oid:1.3.6.1.4.1.1466.115.121.1.26"
      FriendlyName="mail">
    </saml:Attribute>
  </samlp:AttributeQuery>
```

Note that the `Issuer` is the `Subject` in this case. This is sometimes called an *attribute self-query*. An identity provider might return the following assertion, wrapped in a `<samlp:Response>` element (not shown):

```mw
  <saml:Assertion
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
    ID="_33776a319493ad607b7ab3e689482e45"
    Version="2.0"
    IssueInstant="2006-07-17T20:31:41Z">
    <saml:Issuer>https://idp.example.org/SAML2</saml:Issuer>
    <ds:Signature>...</ds:Signature>
    <saml:Subject>
      <saml:NameID
        Format="urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName">
        CN=trscavo@example.com,OU=User,O=NCSA-TEST,C=US
      </saml:NameID>
      <saml:SubjectConfirmation
        Method="urn:oasis:names:tc:SAML:2.0:cm:holder-of-key">
        <saml:SubjectConfirmationData>
          <ds:KeyInfo>
            <ds:X509Data>
              <!-- principal's X.509 cert -->
              <ds:X509Certificate>
  MIICiDCCAXACCQDE+9eiWrm62jANBgkqhkiG9w0BAQQFADBFMQswCQYDVQQGEwJV
  UzESMBAGA1UEChMJTkNTQS1URVNUMQ0wCwYDVQQLEwRVc2VyMRMwEQYDVQQDEwpT
  UC1TZXJ2aWNlMB4XDTA2MDcxNzIwMjE0MVoXDTA2MDcxODIwMjE0MVowSzELMAkG
  A1UEBhMCVVMxEjAQBgNVBAoTCU5DU0EtVEVTVDENMAsGA1UECxMEVXNlcjEZMBcG
  A1UEAwwQdHJzY2F2b0B1aXVjLmVkdTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkC
  gYEAv9QMe4lRl3XbWPcflbCjGK9gty6zBJmp+tsaJINM0VaBaZ3t+tSXknelYife
  nCc2O3yaX76aq53QMXy+5wKQYe8Rzdw28Nv3a73wfjXJXoUhGkvERcscs9EfIWcC
  g2bHOg8uSh+Fbv3lHih4lBJ5MCS2buJfsR7dlr/xsadU2RcCAwEAATANBgkqhkiG
  9w0BAQQFAAOCAQEAdyIcMTob7TVkelfJ7+I1j0LO24UlKvbLzd2OPvcFTCv6fVHx
  Ejk0QxaZXJhreZ6+rIdiMXrEzlRdJEsNMxtDW8++sVp6avoB5EX1y3ez+CEAIL4g
  cjvKZUR4dMryWshWIBHKFFul+r7urUgvWI12KbMeE9KP+kiiiiTskLcKgFzngw1J
  selmHhTcTCrcDocn5yO2+d3dog52vSOtVFDBsBuvDixO2hv679JR6Hlqjtk4GExp
  E9iVI0wdPE038uQIJJTXlhsMMLvUGVh/c0ReJBn92Vj4dI/yy6PtY/8ncYLYNkjg
  oVN0J/ymOktn9lTlFyTiuY4OuJsZRO1+zWLy9g==
              </ds:X509Certificate>
            </ds:X509Data>
          </ds:KeyInfo>
        </saml:SubjectConfirmationData>
      </saml:SubjectConfirmation>
    </saml:Subject>
    <!-- assertion lifetime constrained by principal's X.509 cert -->
    <saml:Conditions
      NotBefore="2006-07-17T20:31:41Z"
      NotOnOrAfter="2006-07-18T20:21:41Z">
    </saml:Conditions>
    <saml:AuthnStatement
      AuthnInstant="2006-07-17T20:31:41Z">
      <saml:AuthnContext>
        <saml:AuthnContextClassRef>
            urn:oasis:names:tc:SAML:2.0:ac:classes:TLSClient
        </saml:AuthnContextClassRef>
      </saml:AuthnContext>
    </saml:AuthnStatement>
    <saml:AttributeStatement>
      <saml:Attribute
        xmlns:x500="urn:oasis:names:tc:SAML:2.0:profiles:attribute:X500"
        x500:Encoding="LDAP"
        NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
        Name="urn:oid:2.5.4.42"
        FriendlyName="givenName">
        <saml:AttributeValue
          xsi:type="xs:string">Tom</saml:AttributeValue>
      </saml:Attribute>
      <saml:Attribute
        xmlns:x500="urn:oasis:names:tc:SAML:2.0:profiles:attribute:X500"
        x500:Encoding="LDAP"
        NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
        Name="urn:oid:1.3.6.1.4.1.1466.115.121.1.26"
        FriendlyName="mail">
        <saml:AttributeValue
          xsi:type="xs:string">trscavo@example.org</saml:AttributeValue>
      </saml:Attribute>
    </saml:AttributeStatement>
  </saml:Assertion>
```

In contrast to the BearerAssertion shown earlier, this assertion has a longer lifetime corresponding to the lifetime of the X.509 certificate that the principal used to authenticate to the identity provider. Moreover, since the assertion is signed, the user can push this assertion to a relying party, and as long as the user can prove possession of the corresponding private key (hence the name "holder-of-key"), the relying party can be assured that the assertion is authentic.

Quite literally, metadata is what makes SAML work (or work well). Some important uses of metadata include:

- A service provider prepares to transmit a `<samlp:AuthnRequest>` element to an identity provider via the browser. How does the service provider know the identity provider is authentic and not some evil identity provider trying to phish the user's password? The service provider consults its list of trusted identity providers **in metadata** before issuing an authentication request.
- In the previous scenario, how does the service provider know where to send the user with the authentication request? The service provider looks up a pre-arranged endpoint location of the trusted identity provider **in metadata**.
- An identity provider receives a `<samlp:AuthnRequest>` element from a service provider via the browser. How does the identity provider know the service provider is authentic and not some evil service provider trying to harvest personally identifiable information regarding the user? The identity provider consults its list of trusted service providers **in metadata** before issuing an authentication response.
- In the previous scenario, how does the identity provider encrypt the SAML assertion so that the trusted service provider (and only the trusted service provider) can decrypt the assertion. The identity provider uses the service provider's encryption certificate **in metadata** to encrypt the assertion.
- Continuing with the previous scenario, how does the identity provider know where to send the user with the authentication response? The identity provider looks up a pre-arranged endpoint location of the trusted service provider **in metadata**.
- How does the service provider know that the authentication response came from a trusted identity provider? The service provider verifies the signature on the assertion using the public key of the identity provider **from metadata**.
- How does the service provider know where to resolve an artifact received from a trusted identity provider? The service provider looks up the pre-arranged endpoint location of the identity provider's artifact resolution service **from metadata**.

Metadata ensures a secure transaction between an identity provider and a service provider. Before metadata, trust information was encoded into the implementation in a proprietary manner. Now the sharing of trust information is facilitated by standard metadata. SAML 2.0 provides a well-defined, interoperable metadata format that entities can leverage to bootstrap the trust process.

An identity provider publishes data about itself in an `<md:EntityDescriptor>` element:

```mw
  <md:EntityDescriptor entityID="https://idp.example.org/SAML2" validUntil="2013-03-22T23:00:00Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <!-- insert md:IDPSSODescriptor element (below) -->
    <md:Organization>
      <md:OrganizationName xml:lang="en">Some Non-profit Organization of New York</md:OrganizationName>
      <md:OrganizationDisplayName xml:lang="en">Some Non-profit Organization</md:OrganizationDisplayName>
      <md:OrganizationURL xml:lang="en">https://www.example.org/</md:OrganizationURL>
    </md:Organization>
    <md:ContactPerson contactType="technical">
      <md:SurName>SAML Technical Support</md:SurName>
      <md:EmailAddress>mailto:saml-support@example.org</md:EmailAddress>
    </md:ContactPerson>
  </md:EntityDescriptor>
```

Note the following details about this entity descriptor:

- The `entityID` attribute is the unique identifier of the entity.
- The `validUntil` attribute gives the expiration date of the metadata.
- The `<ds:Signature>` element (which has been omitted for simplicity) contains a digital signature that ensures the authenticity and integrity of the metadata.
- The organization identified in the `<md:Organization>` element is "responsible for the entity" described by the entity descriptor (section 2.3.2 of SAMLMeta).
- The contact information in the `<md:ContactPerson>` element identifies a technical contact responsible for the entity. Multiple contacts and contact types are possible. See section 2.3.2.2 of SAMLMeta.

By definition, an identity provider manages an SSO service that supports the SAML Web Browser SSO profile specified in SAMLProf. See, for example, the identity provider described in the `<md:IDPSSODescriptor>` element shown in the next section.

The SSO service at the identity provider is described in an `<md:IDPSSODescriptor>` element:

```mw
  <md:IDPSSODescriptor
    protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      <ds:KeyInfo>...</ds:KeyInfo>
    </md:KeyDescriptor>
    <md:ArtifactResolutionService isDefault="true" index="0"
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP"
      Location="https://idp.example.org/SAML2/ArtifactResolution"/>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat>
    <md:SingleSignOnService
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
      Location="https://idp.example.org/SAML2/SSO/Redirect"/>
    <md:SingleSignOnService
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
      Location="https://idp.example.org/SAML2/SSO/POST"/>
    <md:SingleSignOnService
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact"
      Location="https://idp.example.org/SAML2/Artifact"/>
    <saml:Attribute
      NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
      Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.1"
      FriendlyName="eduPersonAffiliation">
      <saml:AttributeValue>member</saml:AttributeValue>
      <saml:AttributeValue>student</saml:AttributeValue>
      <saml:AttributeValue>faculty</saml:AttributeValue>
      <saml:AttributeValue>employee</saml:AttributeValue>
      <saml:AttributeValue>staff</saml:AttributeValue>
    </saml:Attribute>
  </md:IDPSSODescriptor>
```

The previous metadata element describes the SSO service at the identity provider. Note the following details about this element:

- The identity provider software is configured with a private SAML signing key and/or a private back-channel TLS key. The corresponding public key is included in the `<md:KeyDescriptor use="signing">` element in IdP metadata. The key material has been omitted from the key descriptor for brevity.
- The `Binding` attribute of the `<md:ArtifactResolutionService>` element indicates that the SAML SOAP binding (SAMLBind) should be used for artifact resolution.
- The `Location` attribute of the `<md:ArtifactResolutionService>` element is used in step 8 of the "double artifact" profile.
- The value of the `index` attribute of the `<md:ArtifactResolutionService>` element is used as the `EndpointIndex` in the construction of a SAML type 0x0004 artifact.
- The `<md:NameIDFormat>` elements indicate what SAML name identifier formats (SAMLCore) the SSO service supports.
- The `Binding` attributes of the `<md:SingleSignOnService>` elements are standard URIs specified in the SAML 2.0 Binding specification (SAMLBind).
- The `Location` attribute of the `<md:SingleSignOnService>` element that supports the HTTP POST binding is used in step 2 of the "double POST" profile.
- The `Location` attribute of the `<md:SingleSignOnService>` element that supports the HTTP Artifact binding is used in step 2 of the "double artifact" profile.
- The `<saml:Attribute>` element describes an attribute that the identity provider is willing to assert (subject to policy). The `<saml:AttributeValue>` elements enumerate the possible values the attribute may take on.

As noted at the beginning of this section, the values of the `Location` attributes are used by a service provider to route SAML messages, which minimizes the possibility of a rogue identity provider orchestrating a man-in-the-middle attack.

Like the identity provider, a service provider publishes data about itself in an `<md:EntityDescriptor>` element:

```mw
  <md:EntityDescriptor entityID="https://sp.example.com/SAML2" validUntil="2013-03-22T23:00:00Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <!-- insert md:SPSSODescriptor element (see below) -->
    <md:Organization>
      <md:OrganizationName xml:lang="en">Some Commercial Vendor of California</md:OrganizationName>
      <md:OrganizationDisplayName xml:lang="en">Some Commercial Vendor</md:OrganizationDisplayName>
      <md:OrganizationURL xml:lang="en">https://www.example.com/</md:OrganizationURL>
    </md:Organization>
    <md:ContactPerson contactType="technical">
      <md:SurName>SAML Technical Support</md:SurName>
      <md:EmailAddress>mailto:saml-support@example.com</md:EmailAddress>
    </md:ContactPerson>
  </md:EntityDescriptor>
```

Note the following details about this entity descriptor:

- The `entityID` attribute is the unique identifier of the entity.
- The `validUntil` attribute gives the expiration date of the metadata.
- The `<ds:Signature>` element (which has been omitted for simplicity) contains a digital signature that ensures the authenticity and integrity of the metadata.
- The organization identified in the `<md:Organization>` element is "responsible for the entity" described by the entity descriptor (section 2.3.2 of SAMLMeta).
- The contact information in the `<md:ContactPerson>` element identifies a technical contact responsible for the entity. Multiple contacts and contact types are possible. See section 2.3.2.2 of SAMLMeta.

By definition, a service provider manages an assertion consumer service that supports the SAML Web Browser SSO profile specified in SAMLProf. See, for example, the service provider described in the `<md:SPSSODescriptor>` element shown in the next section.

The assertion consumer service is contained in an `<md:SPSSODescriptor>` element:

```mw
  <md:SPSSODescriptor
    protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      <ds:KeyInfo>...</ds:KeyInfo>
    </md:KeyDescriptor>
    <md:KeyDescriptor use="encryption">
      <ds:KeyInfo>...</ds:KeyInfo>
    </md:KeyDescriptor>
    <md:ArtifactResolutionService isDefault="true" index="0"
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP"
      Location="https://sp.example.com/SAML2/ArtifactResolution"/>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat>
    <md:AssertionConsumerService isDefault="true" index="0"
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
      Location="https://sp.example.com/SAML2/SSO/POST"/>
    <md:AssertionConsumerService index="1"
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact"
      Location="https://sp.example.com/SAML2/Artifact"/>
    <md:AttributeConsumingService isDefault="true" index="1">
      <md:ServiceName xml:lang="en">Service Provider Portal</md:ServiceName>
      <md:RequestedAttribute
        NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
        Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.1"
        FriendlyName="eduPersonAffiliation">
      </md:RequestedAttribute>
    </md:AttributeConsumingService>
  </md:SPSSODescriptor>
```

Note the following details about the `<md:SPSSODescriptor>` metadata element:

- The service provider software is configured with a private SAML signing key and/or a private back-channel TLS key. The corresponding public key is included in the `<md:KeyDescriptor use="signing">` element in SP metadata. The key material has been omitted from the key descriptor for brevity.
- Likewise the service provider software is configured with a private SAML decryption key. A public SAML encryption key is included in the `<md:KeyDescriptor use="encryption">` element in SP metadata. The key material has been omitted from the key descriptor for brevity.
- The `index` attribute of an `<md:AssertionConsumerService>` element is used as the value of the `AssertionConsumerServiceIndex` attribute in a `<samlp:AuthnRequest>` element.
- The `Binding` attributes of the `<md:AssertionConsumerService>` elements are standard URIs specified in the SAML 2.0 Binding specification (SAMLBind).
- The `Location` attribute of the `<md:AssertionConsumerService>` element that supports the HTTP POST binding (`index="0"`) is used in step 4 of the "double POST" profile.
- The `Location` attribute of the `<md:AssertionConsumerService>` element that supports the HTTP Artifact binding (`index="1"`) is used in step 6 of the "double artifact" profile.
- The `<md:AttributeConsumingService>` element is used by the identity provider to formulate an `<saml:AttributeStatement>` element that is pushed to the service provider in conjunction with Web Browser SSO.
- The `index` attribute of the `<md:AttributeConsumingService>` element is used as the value of the `AttributeConsumingServiceIndex` attribute in a `<samlp:AuthnRequest>` element.

As noted at the beginning of this section, the values of the `Location` attributes are used by an identity provider to route SAML messages, which minimizes the possibility of a rogue service provider orchestrating a man-in-the-middle attack.

In the previous examples, each `<md:EntityDescriptor>` element is shown to be digitally signed. In practice, however, multiple `<md:EntityDescriptor>` elements are grouped together under an `<md:EntitiesDescriptor>` element with a single digital signature over the entire aggregate:

```mw
  <md:EntitiesDescriptor validUntil="2013-03-22T23:00:00Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <md:EntityDescriptor entityID="https://idp.example.org/SAML2">
      ...
    </md:EntityDescriptor>
    <md:EntityDescriptor entityID="https://sp.example.com/SAML2">
      ...
    </md:EntityDescriptor>
  </md:EntitiesDescriptor>
```

Note the following details about the above `<md:EntitiesDescriptor>` element:

- The digital signature (which has been omitted for brevity) covers the entire aggregate.
- The `validUntil` XML attribute has been elevated to the parent element, implying that the expiration date applies to each child element.
- The XML namespace declarations have been elevated to the parent element to avoid redundant namespace declarations.

Typically metadata aggregates are published by trusted third parties called *federations* who vouch for the integrity of all the metadata in the aggregate. Note that metadata aggregates can be very large, composed of hundreds or even thousands of entities per aggregate.
