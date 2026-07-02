---
title: "SAML metadata"
source: https://en.wikipedia.org/wiki/SAML_metadata
domain: saml-deep
license: CC-BY-SA-4.0
tags: saml assertion, saml2 protocol, saml metadata exchange, service provider sso, identity provider initiated
fetched: 2026-07-02
---

# SAML metadata

The **SAML metadata** standard belongs to the family of XML-based standards known as the Security Assertion Markup Language (SAML) published by OASIS in 2005. A SAML metadata document describes a SAML deployment such as a SAML identity provider or a SAML service provider. Deployments share metadata to establish a baseline of trust and interoperability.

## Overview

To securely interoperate, partners share metadata in whatever form and by whatever means possible. In any case, at least the following metadata must be shared:

- Entity ID
- Protocol endpoints (bindings and locations)

Every SAML system entity has an entity ID, a globally-unique identifier used in software configurations, relying-party databases, and client-side cookies. On the wire, every SAML protocol message contains the entity ID of the issuer.

For authentication purposes, a SAML message may be digitally signed by the issuer. To verify the signature on the message, the message receiver uses a public key known to belong to the issuer. Similarly, to encrypt a message, a public encryption key belonging to the ultimate receiver must be known to the issuer. In both situations—signing and encryption—trusted public keys must be shared in advance.

Once the message is signed and encrypted, the issuer sends the message to a trusted protocol endpoint, the location of which must be known in advance. Upon receipt, the message receiver decrypts the message (using its own private decryption key) and verifies the signature (using a trusted public key in metadata) before mapping the entity ID in the message to a trusted partner.

The previous scenario requires each party to know the other in advance. To establish a baseline of trust, parties share metadata with each other. Initially, this may be as simple as sharing information via email. Over time, as the number of SAML partners grows, the natural tendency is to automate the metadata sharing process.

To fully automate the metadata sharing process, a standard file format is needed. To this end, the SAML V2.0 Metadata specification defines a standard representation for SAML metadata that simplifies the configuration of SAML software and makes it possible to create secure, automated processes for metadata sharing.

As SAML technology has matured, the importance of SAML metadata has steadily increased. Today an implementation that supports SAML web browser single sign-on requires a schema-valid SAML metadata file for each SAML partner. (See the SAML V2.0 Profiles specification for more information about SAML web browser SSO.)

The term *static metadata* refers to a metadata file that is configured directly into the SAML application by an administrator. In doing so, the administrator becomes responsible for the maintenance of the metadata regardless of how the metadata was obtained in the first place. Thus static metadata contributes to the overall static configuration of the SAML application.

Unfortunately, SAML metadata is inherently non-static as illustrated by the following typical scenario between a SAML identity provider (IdP) and a SAML service provider (SP). Suppose an IdP owner obtains SAML metadata from an SP partner. Perhaps the SP metadata is transmitted to the IdP owner via email, or maybe the IdP owner logs into a protected web app and downloads the SP metadata via a browser. Regardless of how the metadata is obtained, the result is the same: the IdP owner configures the SP metadata directly into the IdP software.

Now suppose the SP metadata contains a public encryption key. Presumably, the corresponding private decryption key is configured into the SP software. If the private decryption key is compromised (or otherwise needs to be replaced), the public encryption key in the SP metadata is no longer trustworthy and must be replaced as well.

Since the SP metadata is statically configured in the IdP software, only the IdP owner can replace the public encryption key in the SP metadata. In this sense, *the IdP owner is responsible for the SP metadata.* This mismatch leads to interoperability issues.

The same is true on the SP side. By statically configuring IdP metadata into the SP software, the SP owner implicitly accepts the responsibility to maintain the IdP metadata when something changes. Since an IdP (or SP) typically has many partners, static metadata configuration clearly does not scale, and moreover, change management associated with static metadata is difficult at best.

Not surprisingly, metadata sharing processes yearn to be automated. Every metadata file that is statically configured into the SAML application by an administrator incurs technical debt. The accumulation of this debt prevents the SAML deployment from scaling to its potential.

To avoid excessive technical debt, the metadata sharing process must be automated. One approach is to enlist the help of a trusted third party whose responsibility it is to collect, curate, and distribute metadata across the network. Curated metadata is consistently formatted, more likely to be free of vulnerabilities (intentional or otherwise), and therefore safe to use.

In the case of SAML metadata, this trusted third party is called a *SAML federation.* The community of SAML deployers comprising the federation willingly conform to one or more profiles of SAML to promote interoperability and trust. To that end, federation participants often share a central infrastructure for metadata sharing, which allows the federation to scale to thousands of interoperable SAML deployments.

## History

Now let's retrace some of the steps that led to the publication of the SAML V2.0 Metadata specification in March 2005. A turning point occurred on 14 November 2003—our story starts there.

### Historical origins

In response to Microsoft Passport, the Liberty Alliance conceived the *Identity Federation Framework*, a federation technology developed over a three-year period between 2002 and 2004. (The previously mentioned history of SAML provides context for ID-FF.) On 14 November 2003, Liberty contributed ID-FF 1.2 to OASIS. The contribution included a document entitled *Liberty Metadata Description and Discovery Specification Version 1.0,* which included the following design goals:

1. "whois for SAML federations" (based on the `Organization` and `ContactPerson` elements in metadata)
2. dynamic discovery of metadata (with resolution via DNS and Well-Known Location)
3. document-level security using XML Signature

As it turns out, all of those goals were preserved in the OASIS SAML V2.0 Metadata Standard described later in this article.

The schema document included with the legacy Liberty ID-FF 1.2 archive is identified as Liberty Metadata Version 1.1 whereas Liberty Metadata Version 1.0 was contributed to OASIS. The apparent contradiction was explained by the schema's author. (Peter Davis, Personal Communication) Between November 2003 (when Version 1.0 was contributed to OASIS) and December 2004 (when Version 1.1 was completed by Liberty), development of the Liberty metadata specification continued in parallel with the OASIS work stream. See the chart below for a visual representation. The arrows in the chart indicate dependencies while the dashed lines indicate equivalencies.

Relevant references into the Liberty work stream are given at the end of this article. The original metadata schema contributed to OASIS is listed in its entirety in section 7 of the Liberty Metadata Version 1.0 specification. Similarly, the specification for Liberty Metadata Version 1.1 includes a listing of the Version 1.1 schema. Both the Version 1.0 schema and the Version 1.1 schema are linked here courtesy of the Internet Archive's Wayback Machine.

### Post-November 2003

Over the next thirteen months, from November 2003 to December 2004, the OASIS Security Services (SAML) Technical Committee (SSTC) molded the Liberty metadata specification into what eventually became known as SAML Metadata. During that time, the SSTC generalized the metadata specification to include support for multiple protocols (including non-SAML protocols) but more importantly, the Liberty metadata schema was retrofitted with numerous extension points. Historically, the extensibility of SAML Metadata has had important consequences, as we shall see.

By March 2004, most of the Liberty contribution was incorporated into the OASIS work stream. From that point onward, the Liberty and OASIS work streams progressed concurrently (but not independently since the same people were working on both specifications). Between March and July 2004, the fledgling SAML Metadata specification underwent significant churn.

In July 2004, the SSTC issued a public call for comments covering a complete set of SAML V2.0 draft specifications. Included in that specification set was a working draft of a newly forged SAML V2.0 Metadata specification.

In retrospect, it appears as though the bulk of the SAML V2.0 Metadata specification was developed between March and July 2004, but clearly the SAML V2.0 Metadata Standard sprung from the loins of the Liberty Alliance, specifically Liberty Metadata Version 1.0. Consequently, to understand the origins of SAML Metadata, one must study the provenance of Liberty metadata.

The remaining history of SAML Metadata is mostly OASIS administrative process. After the final Committee Draft was published in November 2004, the SSTC began the standardization process in January 2005. Finally, on 5 March 2005, OASIS announced the newly ratified SAML V2.0 Standard.

The V2.0 specification set (see the References section for a complete list) included the final SAML V2.0 Metadata specification. A decade later, in September 2015, OASIS published a revised SAML Metadata specification with errata. As a result, the original metadata specification was deprecated, as were the other documents in the original 2.0 specification set.

During the intervening decade, between 2005 and 2015, the SSTC developed a number of "Post-V2.0" draft specifications. Some of these draft documents became Committee Specifications. A select subset of these Committee Specifications are listed in the References section at the end of this article.

### Pre-November 2003

As it turns out, the influence of the Liberty Identity Federation Framework on SAML Metadata predates the contribution of ID-FF 1.2 in November 2003. Apparently the SSTC was dabbling in metadata in parallel with the Liberty Alliance. An excerpt from a draft metadata specification published in September 2003 bears this out:

> This document defines metadata that describe the elements and attributes required to use the SAML Web Browser SSO Profiles. Since the Liberty Alliance Web SSO Profiles are directly based on the SAML Web SSO Profiles, the metadata defined in this document borrows extensively from the metadata definitions in the draft Liberty Alliance 1.2 specifications. (Excerpted from "Metadata for SAML 2.0 Web Browser SSO Profiles")

The revision history at the end of that draft document gives the following characterization of itself: "Initial draft based on Draft 07 of SAML 1.1 Metadata specification." In other words, earlier draft documents were published. Indeed, the revision history at the end of the previous draft shows a trail of metadata specifications dating back to November 2002.

Following the document trail, the influence of Liberty ID-FF on SAML metadata can be traced to a draft specification published in April 2003. This is the first known OASIS document that references Liberty ID-FF, specifically, Liberty Metadata Version 1.0-06, an early version of the Liberty Metadata specification about which little is known. It is, however, clear that "Metadata for SAML 1.1 Web Browser Profiles" was intended to be a companion to the SAML V1.1 Standard but of course we know that V1.1 does not specify the use of metadata. See the next section for relevant conjecture.

Two early metadata schema may be of interest:

1. In June 2002, barely a month after the SSTC completed its work on what was to become the SAML V1.0 Standard, the Shibboleth project developed a metadata schema consisting of `<OriginSite>` and `<DestinationSite>` elements. This schema would drive the initial versions of the Shibboleth IdP software.
2. In February 2003, the SSTC released a draft schema for a metadata specification entitled "Metadata for SAML 1.0 Web Browser Profiles." That schema remains a curiosity, however, since the very next version of that document stream (and all subsequent versions) would exhibit the Liberty metadata syntax.

There is no evidence to suggest that either of these early attempts to define a metadata schema had any appreciable effect on the development of the Liberty metadata schema.

### Historical summary

We know that metadata standards for SAML V1.0 or SAML V1.1 were never published. We also know that the necessary IPR for Liberty Metadata was not in place until November 2003. With that, we offer the following summary and conjecture:

1. A draft specification entitled "Metadata for SAML 1.0 Web Browser Profiles" was the first known SAML metadata specification. The document is dated 12 November 2002, which is one week **after** the SAML V1.0 Standard was announced, which is curious. In any case, the metadata syntax used in that document is completely different from what we now know as SAML Metadata. That document was never published and its origins remain a mystery.
2. A draft specification entitled "Metadata for SAML 1.1 Web Browser Profiles" was the first known SAML metadata specification based on Liberty ID-FF. It was completed in April 2003. The title of the draft specification makes it clear that the SSTC knew that SAML V1.1 was coming and moreover SAML metadata was to be included in the SAML V1.1 Standard.
3. Unfortunately that did not happen since the necessary IPR was not in place when the SAML V1.1 Standard was announced. Indeed, the formal contribution of Liberty ID-FF 1.2 to OASIS occurred two months **after** the announcement of the SAML V1.1 Standard in September 2003.
4. In September 2003, less than two weeks after the announcement of the SAML V1.1 Standard, the SSTC set its sights on SAML V2.0 by forking the document stream and renaming the draft document: "Metadata for SAML 2.0 Web Browser Profiles."
5. SAML Metadata came to life between March and July 2004. The SSTC issued a public call for comments that included a candidate SAML Metadata specification.
6. The final SAML Metadata specification was included in the SAML V2.0 Standard specification set announced in March 2005.
7. For the next 10 years, the specification documents evolved (but the schema remained stable). A specification for SAML V2.0 Metadata with Errata (SAMLMeta20Errata) was published in September 2015.

### Post-V2.0 specifications

As mentioned earlier, the SAML V2.0 Metadata Schema has numerous extension points. This feature led to a proliferation of "Post-V2.0" specifications that extended the standard in several directions. The more popular metadata extensions are listed below for convenience (see the examples for specific use cases):

1. *SAML V2.0 Metadata Extensions for Registration and Publication Information Version 1.0.*
2. *SAML V2.0 Metadata Extension for Entity Attributes.*
3. *SAML V2.0 Metadata Extensions for Login and Discovery User Interface Version 1.0.*
4. *Identity Provider Discovery Service Protocol and Profile.*
5. *Service Provider Request Initiation Protocol and Profile Version 1.0.*
6. *SAML V2.0 Metadata Profile for Algorithm Support Version 1.0.*

An important "Post-V2.0" specification is the *SAML V2.0 Metadata Interoperability Profile,* which builds on the premise that a formal public key infrastructure (PKI) can be extremely complex and in some cases intractable (it is well known, for example, that browser-facing TLS certificate revocation is broken). In essence, the *Metadata Interoperability Profile* is an attempt to provide a workable key revocation mechanism for SAML federations.

Since its publication in August 2009, the *Metadata Interoperability Profile* has been a particularly influential document, especially in higher education (see, for example, the certificate-related requirements for deployers in one large R&E federation). Metadata interoperability plays a key role in a formal implementation profile published by the Kantara Initiative:

> Implementations MUST support the interpretation and application of metadata as defined by the SAML V2.0 Metadata Interoperability Profile. It follows that implementations MUST be capable of interoperating (leading to success or failure as dictated by default configuration) with any number of SAML peers for which metadata is available, without additional inputs or separate configuration.

Indeed, the key feature that distinguishes a scalable SAML implementation (from one that is not) is metadata interoperability.

In this section we give concrete examples of the SAML *entity descriptor,* the basic unit of policy and interoperability in SAML metadata. Each of the examples includes the following metadata bits:

- Entity ID and entity attributes
- Role descriptor (describing either a SAML identity provider or a SAML service provider)
  - User interface elements
  - Signing keys or encryption keys
  - Single sign-on protocol endpoints
- Registration and publication info
- Organization and contact info (for human readers)

In the examples below, a particular URI in metadata (such as an `entityID` or an endpoint location) maps to a responsible party via the URI's domain component:

- The organization that owns domain `example.info` is responsible for an unspecified SAML entity (such as an identity provider or a service provider)
- The organization that owns domain `example.org` is responsible for a SAML identity provider
- The organization that owns domain `example.com` is responsible for a SAML service provider
- The organization that owns domain `example.net` is a trusted 3rd party responsible for metadata registration and publication

Note that SAML metadata describes all parties involved in metadata-driven SAML Web Browser SSO except the browser user. (See the SAML V2.0 Profiles specification for more information about SAML web browser SSO.)

The following code sample illustrates the common technical features of a SAML `<md:EntityDescriptor>` element:

```mw
  <md:EntityDescriptor entityID="https://sso.example.info/entity" validUntil="2017-08-30T19:10:29Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:mdrpi="urn:oasis:names:tc:SAML:metadata:rpi"
    xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <md:Extensions>
      <mdrpi:RegistrationInfo registrationAuthority="https://registrar.example.net"/>
      <mdrpi:PublicationInfo creationInstant="2017-08-16T19:10:29Z" publisher="https://registrar.example.net"/>
      <mdattr:EntityAttributes>
        <saml:Attribute Name="http://registrar.example.net/entity-category" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
          <saml:AttributeValue>https://registrar.example.net/category/self-certified</saml:AttributeValue>
        </saml:Attribute>
      </mdattr:EntityAttributes>
    </md:Extensions>
    <!-- insert one or more concrete instances of the md:RoleDescriptor abstract type (see below) -->
    <md:Organization>
      <md:OrganizationName xml:lang="en">...</md:OrganizationName>
      <md:OrganizationDisplayName xml:lang="en">...</md:OrganizationDisplayName>
      <md:OrganizationURL xml:lang="en">https://www.example.info/</md:OrganizationURL>
    </md:Organization>
    <md:ContactPerson contactType="technical">
      <md:SurName>SAML Technical Support</md:SurName>
      <md:EmailAddress>mailto:technical-support@example.info</md:EmailAddress>
    </md:ContactPerson>
  </md:EntityDescriptor>
```

Note the following details about this general entity descriptor:

- The `entityID` attribute is the unique identifier of the entity. Note well that the `entityID` is an immutable name for the entity, not a location.
- The `validUntil` attribute gives the expiration date of the metadata.
- The `<ds:Signature>` element (which has been omitted for simplicity) contains a digital signature that ensures the authenticity and integrity of the metadata. The signatory is assumed to be a trusted 3rd party called a *metadata registrar*.
- The `<mdrpi:RegistrationInfo>` extension element asserts an identifier for the metadata registrar.
- The `<mdrpi:PublicationInfo>` extension element asserts the metadata publisher (which happens to be the same as the registrar). The `creationInstant` attribute gives the precise instant the metadata was created. Comparing the value of the `creationInstant` attribute to the value of the `validUntil` attribute, we see that the metadata is valid for two weeks.
- The `<mdattr:EntityAttributes>` extension element includes a single entity attribute. The entity attribute claims that the entity is "self-certified," a presumably desirable quality.
- The organization identified in the `<md:Organization>` element is "responsible for the entity" described by the entity descriptor (section 2.3.2 of SAMLMeta). The `<md:Organization>` element contains one or more language-qualified child elements of each type.
- The contact information in the `<md:ContactPerson>` element identifies a technical contact responsible for the entity. Multiple contacts and contact types are possible. See section 2.3.2.2 of SAMLMeta.

The all-important role descriptor has been omitted from this initial example for brevity. The SAML metadata specification defines numerous concrete instances of the **md:RoleDescriptor** abstract type (section 2.4.1 of SAMLMeta). The two most important roles are described by the `<md:IDPSSODescriptor>` element and the `<md:SPSSODescriptor>` element. Each of these role descriptors is illustrated in the subsections below.

A SAML identity provider manages a Single Sign-On Service endpoint that receives authentication requests from service providers. The entity descriptor for an identity provider in that role contains an `<md:IDPSSODescriptor>` element, which itself contains at least one `<md:SingleSignOnService>` endpoint. The following example illustrates two such endpoints:

```mw
  <md:EntityDescriptor entityID="https://sso.example.org/idp" validUntil="2017-08-30T19:10:29Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:mdrpi="urn:oasis:names:tc:SAML:metadata:rpi"
    xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute"
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <md:Extensions>
      <mdrpi:RegistrationInfo registrationAuthority="https://registrar.example.net"/>
      <mdrpi:PublicationInfo creationInstant="2017-08-16T19:10:29Z" publisher="https://registrar.example.net"/>
      <mdattr:EntityAttributes>
        <saml:Attribute Name="http://registrar.example.net/entity-category" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
          <saml:AttributeValue>https://registrar.example.net/category/self-certified</saml:AttributeValue>
        </saml:Attribute>
      </mdattr:EntityAttributes>
    </md:Extensions>
    <md:IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
      <md:Extensions>
        <mdui:UIInfo>
          <mdui:DisplayName xml:lang="en">Example.org</mdui:DisplayName>
          <mdui:Description xml:lang="en">The identity provider at Example.org</mdui:Description>
          <mdui:Logo height="32" width="32" xml:lang="en">https://idp.example.org/myicon.png</mdui:Logo>
        </mdui:UIInfo>
      </md:Extensions>
      <md:KeyDescriptor use="signing">
        <ds:KeyInfo>...</ds:KeyInfo>
      </md:KeyDescriptor>
      <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://idp.example.org/SAML2/SSO/Redirect"/>
      <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://idp.example.org/SAML2/SSO/POST"/>
    </md:IDPSSODescriptor>
    <md:Organization>
      <md:OrganizationName xml:lang="en">Example.org Non-Profit Org</md:OrganizationName>
      <md:OrganizationDisplayName xml:lang="en">Example.org</md:OrganizationDisplayName>
      <md:OrganizationURL xml:lang="en">https://www.example.org/</md:OrganizationURL>
    </md:Organization>
    <md:ContactPerson contactType="technical">
      <md:SurName>SAML Technical Support</md:SurName>
      <md:EmailAddress>mailto:technical-support@example.org</md:EmailAddress>
    </md:ContactPerson>
  </md:EntityDescriptor>
```

The content of the `<md:IDPSSODescriptor>` element describes the Single Sign-On Service at the identity provider. Note the following details about this element:

- The `<mdui:UIInfo>` container contains a set of language-qualified extension elements used to build dynamic user interfaces at the service provider. The most important user interface at the service provider is the identity provider discovery interface.
- The identity provider software is presumably configured with a private SAML signing key. The corresponding public key is included in the `<md:KeyDescriptor use="signing">` element. In the above example, the key material has been omitted from the key descriptor for brevity.
- The `Binding` attributes of the `<md:SingleSignOnService>` elements are standard URIs specified in the SAML 2.0 Binding specification (SAMLBind).

The values of the `md:SingleSignOnService/@Location` attributes in identity provider metadata are used by a service provider to route SAML messages, which minimizes the possibility of a rogue identity provider orchestrating a man-in-the-middle attack.

A SAML service provider manages an Assertion Consumer Service endpoint that receives authentication assertions from identity providers. The entity descriptor for a service provider in that role contains an `<md:SPSSODescriptor>` element, which itself contains at least one `<md:AssertionConsumerService>` endpoint. The following example illustrates such an endpoint:

```mw
  <md:EntityDescriptor entityID="https://sso.example.com/portal" validUntil="2017-08-30T19:10:29Z"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:mdrpi="urn:oasis:names:tc:SAML:metadata:rpi"
    xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute"
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
    xmlns:idpdisc="urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <!-- insert ds:Signature element (omitted) -->
    <md:Extensions>
      <mdrpi:RegistrationInfo registrationAuthority="https://registrar.example.net"/>
      <mdrpi:PublicationInfo creationInstant="2017-08-16T19:10:29Z" publisher="https://registrar.example.net"/>
      <mdattr:EntityAttributes>
        <saml:Attribute Name="http://registrar.example.net/entity-category" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
          <saml:AttributeValue>https://registrar.example.net/category/self-certified</saml:AttributeValue>
        </saml:Attribute>
      </mdattr:EntityAttributes>
    </md:Extensions>
    <md:SPSSODescriptor WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
      <md:Extensions>
        <mdui:UIInfo>
          <mdui:DisplayName xml:lang="en">Example.com Vendor Service</mdui:DisplayName>
          <mdui:InformationURL xml:lang="en">https://service.example.com/about.html</mdui:InformationURL>
          <mdui:PrivacyStatementURL xml:lang="en">https://service.example.com/privacy.html</mdui:PrivacyStatementURL>
          <mdui:Logo height="32" width="32" xml:lang="en">https://service.example.com/myicon.png</mdui:Logo>
        </mdui:UIInfo>
        <idpdisc:DiscoveryResponse index="0" Binding="urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol" Location="https://service.example.com/SAML2/Login"/>
      </md:Extensions>
      <md:KeyDescriptor use="encryption">
        <ds:KeyInfo>...</ds:KeyInfo>
      </md:KeyDescriptor>
      <md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat>
      <md:AssertionConsumerService index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://service.example.com/SAML2/SSO/POST"/>
      <md:AttributeConsumingService index="0">
        <md:ServiceName xml:lang="en">Example.com Employee Portal</md:ServiceName>
        <md:RequestedAttribute isRequired="true"
          NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
          Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.13" FriendlyName="eduPersonUniqueId"/>
        <md:RequestedAttribute
          NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
          Name="urn:oid:0.9.2342.19200300.100.1.3" FriendlyName="mail"/>
      </md:AttributeConsumingService>
    </md:SPSSODescriptor>
    <md:Organization>
      <md:OrganizationName xml:lang="en">Example.com Inc.</md:OrganizationName>
      <md:OrganizationDisplayName xml:lang="en">Example.com</md:OrganizationDisplayName>
      <md:OrganizationURL xml:lang="en">https://www.example.com/</md:OrganizationURL>
    </md:Organization>
    <md:ContactPerson contactType="technical">
      <md:SurName>SAML Technical Support</md:SurName>
      <md:EmailAddress>mailto:technical-support@example.com</md:EmailAddress>
    </md:ContactPerson>
  </md:EntityDescriptor>
```

The content of the `<md:SPSSODescriptor>` element describes the Assertion Consumer Service at the service provider. Note the following details about this element:

- The `WantAssertionsSigned` attribute on the `<md:SPSSODescriptor>` element declares that the service provider wants the `<saml:Assertion>` element to be digitally signed. This attribute causes a metadata-aware identity provider to auto-configure itself at run time.
- The `<mdui:UIInfo>` extension element contains a set of language-qualified extension elements used to build dynamic user interfaces at the identity provider. Two important user interfaces at the identity provider are the login page and the user consent interface.
- The `<idpdisc:DiscoveryResponse>` extension element defines an endpoint used in conjunction with identity provider discovery.
- The service provider software is presumably configured with a private SAML decryption key. A public SAML encryption key is included in the `<md:KeyDescriptor use="encryption">` element. In the above example, the key material has been omitted from the key descriptor for brevity.
- The `<md:NameIDFormat>` element gives the desired format of the `<saml:NameID>` element in the SAML assertion. The presence of this element causes a metadata-aware identity provider to auto-configure itself at run time.
- The `index` attribute of an `<md:AssertionConsumerService>` element is used as the value of the `AssertionConsumerServiceIndex` attribute in a `<samlp:AuthnRequest>` element.
- The `Binding` attribute of the `<md:AssertionConsumerService>` element is a standard URI specified in the SAML 2.0 Binding specification (SAMLBind).
- The `<md:AttributeConsumingService>` element is used by the identity provider to formulate an `<saml:AttributeStatement>` element that is pushed to the service provider in conjunction with SAML Web Browser SSO.
- The `index` attribute of the `<md:AttributeConsumingService>` element is used as the value of the `AttributeConsumingServiceIndex` attribute in a `<samlp:AuthnRequest>` element.

The value of the `md:AssertionConsumerService/@Location` attribute in service provider metadata is used by an identity provider to route SAML messages, which minimizes the possibility of a rogue service provider orchestrating a man-in-the-middle attack.

The following SAML protocol flow is intended to illustrate the use of metadata at various stages of SAML web browser SSO. (See the SAML V2.0 Profiles specification for more information about SAML web browser SSO.)

Trusted SAML metadata ensures a secure transaction between a SAML identity provider (IdP) and a SAML service provider (SP). Before metadata, trust information was encoded into the implementation in a proprietary manner. Now the sharing of trust information is facilitated by standard metadata. The SAML 2.0 Metadata Standard provides a well-defined, interoperable metadata format that entities can use to bootstrap the trust process.

The following sequence illustrates the use of SAML metadata to drive the SAML protocol flow.

### 1. Request the target resource at the SP

A browser user requests a web application resource protected by a SAML service provider:

```
 https://sp.example.com/myresource
```

If a valid security context for the user principal already exists at the service provider, skip steps 2–13.

### 2. Redirect to the Discovery Service

Before the service provider can initiate the SAML protocol flow at step 6, the browser user's preferred identity provider must be known. There are numerous ways to do this. For illustration purposes, the service provider will use a local Discovery Service that conforms to the *Identity Provider Discovery Service Protocol and Profile.*

The service provider redirects the browser user to the Discovery Service:

```mw
302 Redirect
Location: https://ds.example.com/idpdisc?entityID=https%3A%2F%2Fsso.example.org%2Fportal
```

Note that the SP `entityID` is included in the redirect URL as specified by the discovery protocol.

### 3. Request the Discovery Service

The browser user requests the Discovery Service by virtue of the redirect:

```mw
GET /idpdisc?entityID=https%3A%2F%2Fsso.example.org%2Fportal HTTP/1.1
Host: ds.example.com
```

> **Trusted service providers in metadata** How does the Discovery Service know the service provider is authentic and not some evil impostor trying to learn the user's identity provider for nefarious purposes?
> 
> The Discovery Service consults its list of trusted service providers **in metadata** before issuing a response.

**(Discover the user's preferred IdP)**

The Discovery Service discovers the browser user's preferred identity provider by unspecified means.

> **User interface elements in metadata** How does the Discovery Service construct an appropriate discovery interface?
> 
> The Discovery Service consults its trusted metadata store to determine an appropriate list of trusted identity providers to present to the browser user. The `<mdui:UIInfo>` user interface elements **in metadata** may be used to construct a dynamic discovery interface.

### 4. Redirect to the Discovery Response endpoint at the SP

The Discovery Service now redirects the browser user to a Discovery Response endpoint at the service provider:

```mw
302 Redirect
Location: https://sp.example.com/SAML2/Login?entityID=https%3A%2F%2Fsso.example.org%2Fidp
```

Note that the IdP `entityID` is included in the redirect URL as specified by the discovery protocol.

> **Trusted endpoint locations in metadata** How does the Discovery Service know where to send the user with the IdP `entityID`?
> 
> The Discovery Service looks up a pre-arranged Discovery Response endpoint location of the trusted service provider **in metadata**.

### 5. Request the Discovery Response endpoint at the SP

The browser user requests the Discovery Response endpoint at the service provider by virtue of the redirect:

```mw
GET /SAML2/Login?entityID=https%3A%2F%2Fsso.example.org%2Fidp HTTP/1.1
Host: sp.example.com
```

The Discovery Response endpoint at the service provider conforms to the *Identity Provider Discovery Service Protocol and Profile.*

> **Trusted identity providers in metadata**
> 
> How does the service provider know that the identity provider given by the `entityID` in the discovery protocol URL is authentic and not some evil identity provider trying to phish the user's password?
> 
> The service provider consults its list of trusted identity providers **in metadata** before issuing a SAML Request at the next step. If the service provider can **not** determine if the identity provider in question is trusted, the browser user **must not** be redirected to the IdP. This is why it is imperative that *IdP metadata **must** be trusted metadata.*

### 6. Redirect to SSO Service at the IdP

The service provider generates a relevant `<samlp:AuthnRequest>` element, encodes a SAML Request in an URL query string, and then redirects the browser user to the Single Sign-On Service at the identity provider:

```mw
302 Redirect
Location: https://idp.example.org/SAML2/SSO/Redirect?SAMLRequest=request&RelayState=token
```

For an outline how to construct the query string, see the corresponding SAML protocol flow in the SAML 2.0 article. Refer to SAMLCore for details.

> **Trusted endpoint locations in metadata** How does the service provider know where to send the user with the SAML Request?
> 
> The service provider looks up a pre-arranged endpoint location of the trusted identity provider **in metadata**.

### 7. Request the SSO Service at the IdP

The browser user requests the Single Sign-On Service endpoint at the identity provider by virtue of the redirect:

```mw
GET /SAML2/SSO/Redirect?SAMLRequest=request&RelayState=token HTTP/1.1
Host: idp.example.org
```

> **Trusted service providers in metadata** How does the identity provider know the service provider is authentic and not some evil service provider trying to harvest personally identifiable information regarding the user?
> 
> The identity provider consults its list of trusted service providers **in metadata** before issuing a response.

### 8. Respond with the login page

The identity provider returns a login page to the user's browser. The login page contains an HTML form similar to the following:

```mw
  <form method="post" action="https://idp.example.com/login-response" ...>
    Username:<br>
    <input type="text" name="username"><br>
    Password:<br>
    <input type="password" name="password">
    ...
    <input type="submit" value="Submit" />
  </form>
```

> **User interface elements in metadata** To reassure the browser user, the IdP personalizes the login page using the `<mdui:UIInfo>` user interface elements **in metadata.**

### 9. Submit the login form

The browser user submits the HTML form to the identity provider:

```mw
POST /login-response HTTP/1.1
Host: idp.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: nnn
 
username=username&password=password
```

**(Issue a SAML Assertion for the user)**

At this point, the identity provider knows the identity of the user principal and so the identity provider constructs a SAML Assertion on behalf of the user principal. For a concrete example of such an Assertion, see the corresponding SAML protocol flow in the SAML 2.0 article. As always, refer to SAMLCore for details.

The `<saml:NameID>` element in the SAML Assertion encodes an identifier for the user principal. In this case, the identity provider includes a SAML2 Transient NameID (SAMLCore) in the SAML Assertion.

> **NameID format in metadata** Why does the identity provider use a Transient NameID format in the SAML Assertion (as opposed to some other format)?
> 
> Assuming the `<samlp:AuthnRequest>` element issued by the service provider does not request otherwise, a metadata-aware IdP will consult the `<md:NameIDFormat>` elements **in metadata** (if any) to determine the NameID format.

The identity provider includes two user attributes in the SAML Assertion: `eduPersonUniqueId` and `mail`.

> **Requested attributes in metadata** Why does the identity provider include attributes `eduPersonUniqueId` and `mail` in the assertion and not some other attributes?
> 
> A metadata-aware IdP will consult the `<md:RequestedAttribute>` elements **in metadata** (if any) to learn the attribute requirements of the service provider.

Operationally, the identity provider digitally signs and encrypts the SAML Assertion, wraps the Assertion in a SAML Response, and then signs the Response object as well. Typically the identity provider signs the Response alone but in this case both the Assertion and the Response are digitally signed.

> **WantAssertionsSigned attribute in metadata** How does the identity provider know that the service provider wants the Assertion itself to be digitally signed?
> 
> At run time, the identity provider observes that the `WantAssertionsSigned` XML attribute **in metadata** is set to true.

> **Trusted encryption certificate in metadata** How does the identity provider encrypt the SAML Assertion so that the service provider (and only the service provider) can decrypt it?
> 
> At run time, the identity provider uses the service provider's encryption certificate **in metadata** to encrypt the Assertion.

### 10. Respond with the SAML Response page

The identity provider returns an XHTML document to the user's browser. The document contains a SAML Response encoded in an XHTML form as follows:

```mw
  <form method="post" action="https://sp.example.com/SAML2/SSO/POST" ...>
    <input type="hidden" name="SAMLResponse" value="response" />
    <input type="hidden" name="RelayState" value="token" />
    ...
    <input type="submit" value="Submit" />
  </form>
```

> **Trusted endpoint locations in metadata** How does the identity provider know where to send the user with the SAML Response?
> 
> The identity provider looks up a pre-arranged endpoint location of the trusted service provider **in metadata**.

### 11. Request the Assertion Consumer Service at the SP

The XHTML form is automatically submitted by the browser (due to a small bit of JavaScript on the page):

```mw
POST /SAML2/SSO/POST HTTP/1.1
Host: sp.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: nnn
 
SAMLResponse=response&RelayState=token
```

> **Trusted signing certificate in metadata** How does the service provider know that the SAML Response came from a trusted identity provider?
> 
> The service provider verifies the digital signature on the Response using the public key of the identity provider **in metadata**. After decrypting the signature on the Assertion object, the service provider verifies the signature on the Assertion as well.

### 12. Redirect to the target resource

The service provider creates a security context for the user principal and redirects the browser user to the original web application resource:

```mw
302 Redirect
Location: https://sp.example.com/myresource
```

### 13. Request the target resource at the SP again

Finally the browser user requests the target resource at the service provider by virtue of the redirect:

```
 https://sp.example.com/myresource
```

### 14. Respond with requested resource

Since a security context exists, the service provider returns the resource to the browser user agent as requested.
