---
title: "XML Signature"
source: https://en.wikipedia.org/wiki/XML_Signature
domain: saml-security
license: CC-BY-SA-4.0
tags: security assertion markup language, saml assertion validation, xml signature wrapping defense, identity federation security
fetched: 2026-07-02
---

# XML Signature

**XML Signature** (also called *XMLDSig*, *XML-DSig*, *XML-Sig*) defines an XML syntax for digital signatures and is defined in the W3C recommendation XML Signature Syntax and Processing. Functionally, it has much in common with PKCS #7 but is more extensible and geared towards signing XML documents. It is used by various Web technologies such as SOAP, SAML, and others.

XML signatures can be used to sign data–a **resource**–of any type, typically XML documents, but anything that is accessible via a URL can be signed. An XML signature used to sign a resource outside its containing XML document is called a detached signature; if it is used to sign some part of its containing document, it is called an **enveloped** signature; if it contains the signed data within itself it is called an **enveloping** signature.

## Structure

An XML Signature consists of a `Signature` element in the `http://www.w3.org/2000/09/xmldsig#` namespace. The basic structure is as follows:

```mw
<Signature>
  <SignedInfo>
    <CanonicalizationMethod />
    <SignatureMethod />
    <Reference>
       <Transforms />
       <DigestMethod />
       <DigestValue />
    </Reference>
    <Reference /> etc.
  </SignedInfo>
  <SignatureValue />
  <KeyInfo />
  <Object />
</Signature>
```

- The `SignedInfo` element contains or references the signed data and specifies what algorithms are used.
  - The `SignatureMethod` and `CanonicalizationMethod` elements are used by the `SignatureValue` element and are included in `SignedInfo` to protect them from tampering.
  - One or more `Reference` elements specify the resource being signed by URI reference and any transformations to be applied to the resource prior to signing.
    - `Transforms` contains the transformations applied to the resource prior to signing. A transformation can be a XPath-expression that selects a defined subset of the document tree.
    - `DigestMethod` specifies the hash algorithm before applying the hash.
    - `DigestValue` contains the Base64 encoded result of applying the hash algorithm to the transformed resource(s) defined in the `Reference` element attributes.
- The `SignatureValue` element contains the Base64 encoded signature result - the signature generated with the parameters specified in the `SignatureMethod` element - of the `SignedInfo` element after applying the algorithm specified by the `CanonicalizationMethod`.
- `KeyInfo` element optionally allows the signer to provide recipients with the key that validates the signature, usually in the form of one or more X.509 digital certificates. The relying party must identify the key from context if `KeyInfo` is not present.
- The `Object` element (optional) contains the signed data if this is an *enveloping signature*.

## Validation and security considerations

When validating an XML Signature, a procedure called **Core Validation** is followed.

1. **Reference Validation:** Each `Reference`'s digest is verified by retrieving the corresponding resource and applying any transforms and then the specified digest method to it. The result is compared to the recorded `DigestValue`; if they do not match, validation fails.
2. **Signature Validation:** The `SignedInfo` element is serialized using the canonicalization method specified in `CanonicalizationMethod`, the key data is retrieved using `KeyInfo` or by other means, and the signature is verified using the method specified in `SignatureMethod`.

This procedure establishes whether the resources were really signed by the alleged party. However, because of the extensibility of the canonicalization and transform methods, the verifying party must also make sure that what was actually signed or digested is really what was present in the original data, in other words, that the algorithms used there can be trusted not to change the meaning of the signed data.

Because the signed document's structure can be tampered with leading to "signature wrapping" attacks, the validation process should also cover XML document structure. Signed element and signature element should be selected using absolute XPath expression, not `getElementByName` methods.

## XML canonicalization

The creation of XML Signatures is substantially more complex than the creation of an ordinary digital signature because a given XML Document (an "Infoset", in common usage among XML developers) may have more than one legal serialized representation. For example, whitespace inside an XML Element is not syntactically significant, so that `<Elem >` is syntactically identical to `<Elem>`.

Since the digital signature ensures data integrity, a single-byte difference would cause the signature to vary. Moreover, if an XML document is transferred from computer to computer, the line terminator may be changed from CR to LF to CR LF, etc. A program that digests and validates an XML document may later render the XML document in a different way, e.g. adding excess space between attribute definitions with an element definition, or using relative (vs. absolute) URLs, or by reordering namespace definitions. Canonical XML is especially important when an XML Signature refers to a remote document, which may be rendered in time-varying ways by an errant remote server.

To avoid these problems and guarantee that logically-identical XML documents give identical digital signatures, an XML canonicalization transform (frequently abbreviated **C14n**) is employed when signing XML documents (for signing the `SignedInfo`, a canonicalization is mandatory). These algorithms guarantee that semantically-identical documents produce exactly identical serialized representations.

Another complication arises because of the way that the default canonicalization algorithm handles namespace declarations; frequently a signed XML document needs to be embedded in another document; in this case the original canonicalization algorithm will not yield the same result as if the document is treated alone. For this reason, the so-called *Exclusive Canonicalization*, which serializes XML namespace declarations independently of the surrounding XML, was created.

## Benefits

XML Signature is more flexible than other forms of digital signatures such as Pretty Good Privacy and Cryptographic Message Syntax, because it does not operate on binary data, but on the XML Infoset, allowing to work on subsets of the data (this is also possible with binary data in non-standard ways, for example encoding blocks of binary data in base64 ASCII), having various ways to bind the signature and signed information, and perform transformations. Another core concept is canonicalization, that is to sign only the "essence", eliminating meaningless differences like whitespace and line endings.

## Issues

There are criticisms directed at the architecture of XML security in general, and at the suitability of XML canonicalization in particular as a front end to signing and encrypting XML data due to its complexity, inherent processing requirement, and poor performance characteristics. The argument is that performing XML canonicalization causes excessive latency that is simply too much to overcome for transactional, performance sensitive SOA applications.

These issues are being addressed in the XML Security Working Group.

Without proper policy and implementation the use of XML Dsig in SOAP and WS-Security can lead to vulnerabilities, such as XML signature wrapping.

## Applications

An example of applications of XML Signatures:

- Digital signing of XBRL annual reports by auditors in the Netherlands. A PKIoverheid X.509 certificate, approved by the Royal National Institute of Chartered Accountants, is required. The electronic signature is legally binding. The SBR Assurance standard is part of the Dutch Standard Business Reporting program.
