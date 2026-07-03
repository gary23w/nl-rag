---
title: "ASN.1"
source: https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One
domain: iso-development-environment
license: CC-BY-SA-4.0
tags: iso development environment
fetched: 2026-07-03
---

# ASN.1

(Redirected from

Abstract Syntax Notation One

)

**Abstract Syntax Notation One** (**ASN.1**) is a standard interface description language (IDL) for defining data structures that can be serialized and deserialized in a cross-platform way. It is broadly used in telecommunications and computer networking, and especially in cryptography.

Protocol developers define data structures in ASN.1 modules, which are generally a section of a broader standards document written in the ASN.1 language. The advantage is that the ASN.1 description of the data encoding is independent of a particular computer or programming language. Because ASN.1 is both human-readable and machine-readable, an ASN.1 compiler can compile modules into libraries of code, codecs, that decode or encode the data structures. Some ASN.1 compilers can produce code to encode or decode several encodings, e.g. packed, BER or XML.

ASN.1 is a joint standard of the International Telecommunication Union Telecommunication Standardization Sector (ITU-T) in ITU-T Study Group 17 and International Organization for Standardization/International Electrotechnical Commission (ISO/IEC), originally defined in 1984 as part of CCITT X.409:1984. In 1988, ASN.1 moved to its own standard, **X.208**, due to wide applicability. The substantially revised 1995 version is covered by the **X.680**–**X.683** series. The latest revision of the X.680 series of recommendations is the 6.0 Edition, published in 2021.

## Structure

- X.680 defines the basic lexical items of the ASN.1 language (special tokens, format of basic literal values, etc.). It defines the syntax of a "module definition", the definition of a module within a protocol. A module definition can contain data types, predefined *information objects* written in those data types (detailed syntax in X.681), constraint elements (detailed syntax in X.682), among other things.
- X.681 defines the syntax of an *information object*, which allows for objects in custom datatypes to be represented in the language (akin to object literals in other languages). It also defines a way to reference a specific value from an object using a dot notation as if it is a table.
- X.682 defines *constraint elements*, which can be used to apply more advanced constraints in a module.
- X.683, *Parameterization of ASN.1 specifications*, allows assignments and definitions to vary according to parameters.

## Language support

ASN.1 is a data type declaration notation. It does not define how to manipulate a variable of such a type. Manipulation of variables is defined in other languages such as SDL (Specification and Description Language) for executable modeling or TTCN-3 (Testing and Test Control Notation) for conformance testing. Both these languages natively support ASN.1 declarations. It is possible to import an ASN.1 module and declare a variable of any of the ASN.1 types declared in the module.

## Applications

ASN.1 is used to define a large number of protocols. Its most extensive uses continue to be telecommunications, cryptography, and biometrics.

| Protocol | Specification | Specified or customary encoding rules | Uses |
|---|---|---|---|
| Interledger Protocol | ILPV4 Specification | Octet Encoding Rules |   |
| NTCIP 1103 - Transport Management Protocols | NTCIP 1103 | Octet Encoding Rules | Traffic, Transportation, and Infrastructure Management |
| X.500 Directory Services | The ITU X.500 Recommendation Series | Basic Encoding Rules, Distinguished Encoding Rules | LDAP, TLS (X.509) Certificates, Authentication |
| Lightweight Directory Access Protocol (LDAP) | RFC 4511 | Basic Encoding Rules |   |
| PKCS Cryptography Standards | PKCS Cryptography Standards | Basic Encoding Rules and Distinguished Encoding Rules | Asymmetric Keys, certificate bundles |
| X.400 Message Handling | The ITU X.400 Recommendation Series |   | An early competitor to email |
| EMV | EMVCo Publications |   | Payment cards |
| T.120 Multimedia conferencing | The ITU T.120 Recommendation Series | Basic Encoding Rules, Packed Encoding Rules | Microsoft's Remote Desktop Protocol (RDP) |
| Simple Network Management Protocol (SNMP) | RFC 1157 | Basic Encoding Rules | Managing and monitoring networks and computers, particularly characteristics pertaining to performance and reliability |
| Common Management Information Protocol (CMIP) | ITU Recommendation X.711 |   | A competitor to SNMP but more capable and not nearly as popular |
| Signalling System No. 7 (SS7) | The ITU Q.700 Recommendation Series |   | Managing telephone connections over the Public Switched Telephone Network (PSTN) |
| ITU H-Series Multimedia Protocols | The ITU H.200, H.300, and H.400 Recommendation Series |   | Voice over Internet Protocol (VoIP) |
| BioAPI Interworking Protocol (BIP) | ISO/IEC 24708:2008 |   |   |
| Common Biometric Exchange Formats Framework (CBEFF) | NIST IR 6529-A | Basic Encoding Rules |   |
| Authentication Contexts for Biometrics (ACBio) | ISO/IEC 24761:2019 |   |   |
| Computer-supported telecommunications applications (CSTA) | [1] | Basic Encoding Rules |   |
| Dedicated short-range communications (DSRC) | SAE J2735 | Packed Encoding Rules | Vehicle communication |
| IEEE 802.11p (IEEE WAVE) | IEEE 1609.2 |   | Vehicle communication |
| Intelligent Transport Systems (ETSI ITS) | ETSI EN 302 637 2 (CAM) ETSI EN 302 637 3 (DENM) | Unaligned Packed Encoding Rules | Vehicle communication |
| Global System for Mobile Communications (GSM) | [2] |   | 2G Mobile Phone Communications |
| General Packet Radio Service (GPRS) / Enhanced Data rates for GSM Evolution (EDGE) | [3] |   | 2.5G Mobile Phone Communications |
| Universal Mobile Telecommunications System (UMTS) | [4] |   | 3G Mobile Phone Communications |
| Long-Term Evolution (LTE) | [5] |   | 4G Mobile Phone Communications |
| 5G | [6] |   | 5G Mobile Phone Communications |
| Common Alerting Protocol (CAP) | [7] | XML Encoding Rules | Exchanging Alert Information, such as Amber Alerts |
| Controller–pilot data link communications (CPDLC) |   |   | Aeronautics communications |
| Space Link Extension Services (SLE) |   |   | Space systems communications |
| Manufacturing Message Specification (MMS) | ISO 9506-1:2003 |   | Manufacturing |
| File Transfer, Access and Management (FTAM) |   |   | An early and more capable competitor to File Transfer Protocol, but its rarely used anymore. |
| Remote Operations Service Element protocol (ROSE) | ITU Recommendations X.880, X.881, and X.882 |   | An early form of Remote procedure call |
| Association Control Service Element (ACSE) | ITU Recommendation X.227 |   |   |
| Building Automation and Control Networks Protocol (BACnet) | ASHRAE 135-2020 | BACnet Encoding Rules | Building automation and control, such as with fire alarms, elevators, HVAC systems, etc. |
| Kerberos | RFC 4120 | Basic Encoding Rules | Secure authentication |
| WiMAX 2 |   |   | Wide Area Networks |
| Intelligent Network | The ITU Q.1200 Recommendation Series |   | Telecommunications and computer networking |
| X2AP |   | Basic Aligned Packed Encoding Rules |   |
| Lawful Interception (LI) Handover Interface | ETSI TS 102 232-1 |   | Lawful Interception |

## Encodings

ASN.1 is closely associated with a set of encoding rules that specify how to represent a data structure as a series of bytes. The standard ASN.1 encoding rules include:

ASN.1 Encoding Rules

Encoding rules

Object identifier

Specification

Unit of serialization

Encoded elements discernable without foreknowledge of specification

Octet aligned

Encoding control

Description

Dotted

IRI

Basic Encoding Rules

(BER)

2.1.1

/Joint‑ISO‑ITU‑T/ASN.1/

Basic-Encoding

ITU X.690

Octet

Yes

Yes

No

The first specified encoding rules. Encodes elements as tag-length-value (TLV) sequences. Typically provides several options as to how data values are to be encoded. This is one of the most flexible encoding rules.

Distinguished Encoding Rules

(DER)

2.1.2.1

/Joint‑ISO‑ITU‑T/ASN.1/

BER‑Derived/

Distinguished‑Encoding

ITU X.690

Octet

Yes

Yes

No

A restricted subset of the BER. Typically used for things that are digitally-signed because, since the DER allow for fewer options for encoding, and because DER-encoded values are more likely to be re-encoded on the exact same bytes, digital signatures produced by a given abstract value will be the same across implementations and digital signatures produced over DER-encoded data will be less susceptible to collision-based attacks.

Canonical Encoding Rules

(CER)

2.1.2.0

/Joint‑ISO‑ITU‑T/ASN.1/

BER‑Derived/

Canonical‑Encoding

ITU X.690

Octet

Yes

Yes

No

A restricted subset of the BER. Employs almost all of the same restrictions as the DER but the noteworthy difference is that the CER specify that many large values (especially strings) are to be "chopped up" into individual substring elements at the 1000-byte or 1000-character mark (depending on the data type).

Packed Encoding Rules

Unaligned (PER-U/UPER)

2.1.3.0.1

/Joint‑ISO‑ITU‑T/ASN.1/

Packed‑Encoding/

Basic/Unaligned

ITU X.691

Bit

No

No

No

Encodes values on bits. Sometimes simply called "PER". The PERs in general are capable of producing very compact encodings, but at the expense of complexity; they are also highly dependent upon constraints placed on data types.

Packed Encoding Rules

Aligned (PER-A/APER)

2.1.3.0.0

/Joint‑ISO‑ITU‑T/ASN.1/

Packed‑Encoding/

Basic/Aligned

ITU X.691

Bit

No

Yes

No

Encodes values on bits, but if the bits encoded are not evenly divisible by eight, padding bits are added until an integral number of octets encode the value.

Canonical Packed

Encoding Rules Unaligned

(CPER-U)

2.1.3.1.1

/Joint‑ISO‑ITU‑T/ASN.1/

Packed‑Encoding/

Canonical/Unaligned

ITU X.691

Bit

No

No

No

A variant of the PER-U that specifies a single way of encoding values. Sometimes simply called "CPER". The CPERs have a similar relationship to the PERs that the DER and the CER have to the BER.

Canonical Packed

Encoding Rules Aligned

(CPER-A)

2.1.3.1.0

/Joint‑ISO‑ITU‑T/ASN.1/

Packed‑Encoding/

Canonical/Aligned

ITU X.691

Bit

No

Yes

No

A variant of the PER-A that specifies a single way of encoding values.

Basic XML

Encoding Rules

(XER)

2.1.5.0

/Joint‑ISO‑ITU‑T/ASN.1/

XML‑Encoding/

Basic

ITU X.693

Character

Yes

Yes

ECN

Encodes ASN.1 data as XML.

Canonical XML

Encoding Rules

(CXER)

2.1.5.1

/Joint‑ISO‑ITU‑T/ASN.1/

XML‑Encoding/

Canonical

ITU X.693

Character

Yes

Yes

ECN

Variant of XER that produces only one possible encoding for a given value.

Extended XML

Encoding Rules

(EXER)

2.1.5.2

/Joint‑ISO‑ITU‑T/ASN.1/

XML‑Encoding/

Extended

ITU X.693

Character

Yes

Yes

ECN

Variant of XER that adds options and instructions controlling stylistic choices of the encoder.

Octet Encoding Rules

(OER)

2.1.6.0

/Joint‑ISO‑ITU‑T/ASN.1/

OER‑Encoding/

Basic

ITU X.696

Octet

No

Yes

No

A set of encoding rules that encodes values on octets, but does not encode tags or length determinants like the BER does. Data values encoded using the OER often look like those found in "record-based" protocols. The OER were designed to be easy to implement and to produce encodings more compact than those produced by the BER. In addition to reducing the effort of developing encoder/decoders, the use of OER can decrease bandwidth utilization (though not as much as the PER), save CPU cycles, and lower encoding/decoding latency.

ITU X.696 OER is derived from a largely-compatible "OER" defined in NEMA's NTCIP 1102. NEMA's OER is in turn a clarified and expanded version of the unfortunately-named NEMA Packed Encoding Rules (NEMA PER).

Canonical Octet

Encoding Rules

(COER)

2.1.6.1

/Joint‑ISO‑ITU‑T/ASN.1/

OER‑Encoding/

Canonical

ITU X.696

Octet

No

Yes

No

Variant of OER where each value only has one possible octet representation.

JSON

Encoding Rules

(JER)

2.1.7

ITU X.697

Character

Yes

Yes

ECN

Encodes ASN.1 data as JSON. The ASCII-only version is canonical, i.e. each value only has one possible octet representation. The rest are not.

Generic String

Encoding Rules

(GSER)

1.2.36.

79672281.

0.0

/ISO/Member‑Body/AU/Adacel/0/GSER

RFC

3641

Character

Yes

Yes

RFC

4792

Intended to represent encoded data to the user or input data from the user, in a very straightforward format similar to the ASN.1's value notation. GSER was originally designed for the

Lightweight Directory Access Protocol

(LDAP) and is rarely used outside of it.

The use of GSER in actual protocols is discouraged since not all character string encodings supported by ASN.1 can be reproduced in it.

Customization of encoding occurs through instead of ECN.

Robust XML

Encoding Rules (RXER)

1.2.36.

79672281.

0.2

/ISO/Member‑Body/AU/Adacel/0/RXER

RFC

4910

Character

Yes

Yes

RFC

4911

XML format designed for the

Lightweight Directory Access Protocol

(LDAP).

BACnet

Encoding Rules

(BACnetER)

ASHRAE 135

ISO 16484-5

Octet

Yes

Yes

ECN

Encodes elements as tag-length-value (TLV) sequences like the Basic Encoding Rules (BER) does. Example messages can be found in Karg (2012);

Karg also maintains an open-source implementation of a

BACnet

stack, in which code for reading and writing this format can be found.

Signalling Specific

Encoding Rules

(SER)

France Telecom R&D Internal Document

Octet

Yes

Yes

No

Used primarily in telecommunications related protocols, such as GSM and SS7. Designed to produce an identical encoding from ASN.1 that previously existing protocols not specified in ASN.1 would produce.

Lightweight Encoding Rules

(LWER)

Internal document by INRIA.

Memory Word

Yes

No

Originates from an internal document produced by

INRIA

detailing the "Flat Tree Light Weight Syntax" (FTLWS).

Abandoned in 1997 due to the superior performance of the Packed Encoding Rules (PER).

Optionally Big-Endian or Little-Endian transmission as well as 8-bit, 16-bit, and 32-bit memory words. (Therefore, there are six variants, since there are six combinations of those options.)

Minimum Bit

Encoding Rules

(MBER)

Bit

No

No

No

Proposed in the 1980s. Meant to be as compact as possible, like the later Packed Encoding Rules (PER). Never extended to all ASN.1 data types.

High Speed

Coding Rules

"Coding Rules for High Speed Networks"

No

Definition of these encoding rules were a byproduct of INRIA's work on the Flat Tree Light Weight Syntax (FTLWS).

### Encoding Control Notation

ASN.1 recommendations provide a number of predefined encoding rules. If none of the existing encoding rules are suitable, the Encoding Control Notation (ECN, X.692) provides a way for a user to define his or her own customized encoding rules.

### Relation to Privacy-Enhanced Mail (PEM) Encoding

Privacy-Enhanced Mail (PEM) encoding is entirely unrelated to ASN.1 and its codecs, but encoded ASN.1 data, which is often binary, is often PEM-encoded so that it can be transmitted as textual data, e.g. over SMTP relays, or through copy/paste buffers.

## As computer files

ASN.1 language and encoding specifications do not specify details such as what filename extension to use when a chunk of data is stored as a file on a computer. Nevertheless, some conventions have arisen:

- ASN.1-language text: extensions of `.asn1` and `.all` have been used for general files. `.asn` has been used for files only containing module definitions and `.prt` for files only containing value definitions.
- BER-encoded data: `.ber` has been used. There is also a proposed MIME type `application/ber-stream` which includes a `protocol` parameter specifying an associated OID.
- DER-encoded data: `.der`. For DER-encoded X.509 certificates, `.cer` and `.crt` in addition to `.der`. The MIME type `application/x-x509-ca-cert` is specifically for DER-encoded certificates, not general DER data.
- Other encoded data: `asn1c` sample files use `.xer` for XER, `.per` for PER, and `.coer` for COER.

## Example

### Module and constraint

This is an example ASN.1 module defining the messages (data structures) of a fictitious Foo Protocol:

```mw
FooProtocol DEFINITIONS ::= BEGIN

    FooQuestion ::= SEQUENCE {
        trackingNumber INTEGER,
        question       IA5String
    }

    FooAnswer ::= SEQUENCE {
        questionNumber INTEGER,
        answer         BOOLEAN
    }

END
```

This could be a specification published by creators of Foo Protocol. Conversation flows, transaction interchanges, and states are not defined in ASN.1, but are left to other notations and textual description of the protocol.

ASN.1 supports constraints on values and sizes, and extensibility. The above specification can be changed to:

```mw
FooProtocol DEFINITIONS ::= BEGIN

    FooQuestion ::= SEQUENCE {
        trackingNumber INTEGER(0..199),
        question       IA5String
    }

    FooAnswer ::= SEQUENCE {
        questionNumber INTEGER(10..20),
        answer         BOOLEAN
    }

    FooHistory ::= SEQUENCE {
        questions SEQUENCE(SIZE(0..10)) OF FooQuestion,
        answers   SEQUENCE(SIZE(1..10)) OF FooAnswer,
        anArray   SEQUENCE(SIZE(100))  OF INTEGER(0..1000),
        ...
    }

END
```

This change constrains trackingNumbers to have a value between 0 and 199 inclusive, and questionNumbers to have a value between 10 and 20 inclusive. The size of the questions array can be between 0 and 10 elements, with the answers array between 1 and 10 elements. The anArray field is a fixed length 100 element array of integers that must be in the range 0 to 1000. The '...' extensibility marker means that the FooHistory message specification may have additional fields in future versions of the specification; systems compliant with one version should be able to receive and transmit transactions from a later version, though able to process only the fields specified in the earlier version. Good ASN.1 compilers will generate (in C, C++, Java, etc.) source code that will automatically check that transactions fall within these constraints. Transactions that violate the constraints should not be accepted from, or presented to, the application. Constraint management in this layer significantly simplifies protocol specification because the applications will be protected from constraint violations, reducing risk and cost.

The above examples only make use of syntax from X.680. More advanced constraints from X.682 are not used.

### Example PDU

Assuming a message that complies with the Foo Protocol and that will be sent to the receiving party, this particular message (protocol data unit (PDU)) is:

```mw
myQuestion FooQuestion ::= {
    trackingNumber     5,
    question           "Anybody there?"
}
```

To send the myQuestion message through the network, the message is serialized (encoded) as a series of bytes using one of the encoding rules. The Foo protocol specification should explicitly name one set of encoding rules to use, so that users of the Foo protocol know which one they should use and expect.

The above is an example of X.681, specifically of the *ObjectAssignment* construct.

### Example encoded in DER

Below is the data structure shown above as myQuestion encoded in DER format (all numbers are in hexadecimal):

```
30 13 02 01 05 16 0e 41 6e 79 62 6f 64 79 20 74 68 65 72 65 3f
```

DER is a type–length–value encoding, so the sequence above can be interpreted, with reference to the standard SEQUENCE, INTEGER, and IA5String types, as follows:

```
30 — type tag indicating SEQUENCE
13 — length in octets of value that follows
  02 — type tag indicating INTEGER
  01 — length in octets of value that follows
    05 — value (5)
  16 — type tag indicating IA5String 
     (IA5 means the full 7-bit ISO 646 set, including variants, 
      but is generally US-ASCII)
  0e — length in octets of value that follows
    41 6e 79 62 6f 64 79 20 74 68 65 72 65 3f — value ("Anybody there?")
```

### Example encoded in XER

Alternatively, it is possible to encode the same ASN.1 data structure with XML Encoding Rules (XER) to achieve greater human readability "over the wire". It would then appear as the following 108 octets, (space count includes the spaces used for indentation):

```mw
<FooQuestion>
    <trackingNumber>5</trackingNumber>
    <question>Anybody there?</question>
</FooQuestion>
```

### Example encoded in PER, either aligned or unaligned

Alternatively, if Packed Encoding Rules Unaligned are employed, the following 122 bits (16 octets amount to 128 bits, but here only 122 bits carry information and the last 6 bits are merely padding) will be produced:

```
01 05 0e 83 bb ce 2d f9 3c a0 e9 a3 2f 2c af c0
```

In this format, type tags for the required elements are not encoded, so it cannot be parsed without knowing the expected schemas used to encode. Additionally, the bytes for the value of the IA5String are packed using 7-bit units instead of 8-bit units, because the encoder knows that encoding an IA5String byte value requires only 7 bits. However the length bytes are still encoded here, even for the first integer tag 01 (but a PER packer could also omit it if it knows that the allowed value range fits on 8 bits, and it could even compact the single value byte 05 with less than 8 bits, if it knows that allowed values can only fit in a smaller range).

The last 6 bits in the encoded PER are padded with null bits in the 6 least significant bits of the last byte c0 : these extra bits may not be transmitted or used for encoding something else if this sequence is inserted as a part of a longer unaligned PER sequence.

This means that unaligned PER data is essentially an ordered stream of bits, and not an ordered stream of bytes like with aligned PER, and that it will be a bit more complex to decode by software on usual processors because it will require additional contextual bit-shifting and masking and not direct byte addressing (but the same remark would be true with modern processors and memory/storage units whose minimum addressable unit is larger than 1 octet). However modern processors and signal processors include hardware support for fast internal decoding of bit streams with automatic handling of computing units that are crossing the boundaries of addressable storage units (this is needed for efficient processing in data codecs for compression/decompression or with some encryption/decryption algorithms).

For comparison, Packed Encoding Rules Aligned produces instead:

```
01 05 0e 41 6e 79 62 6f 64 79 20 74 68 65 72 65 3f
```

This format is octet-aligned. In this case, each octet is padded individually with null bits on their unused most significant bits.

## Tools

Most of the tools supporting ASN.1 do the following:

- parse the ASN.1 files,
- generates the equivalent declaration in a programming language (like C or C++),
- generates the encoding and decoding functions based on the previous declarations.

A list of tools supporting ASN.1 can be found on the ITU-T Tool web page.

### Online tools

- ASN1 Play
- ASN1 Web Tool (very limited)
- ASN1 Playground (sandbox)
- ASN.1 JavaScript decoder

## Comparison to similar schemes

ASN.1 is similar in purpose and use to Google Protocol Buffers and Apache Thrift, which are also interface description languages for cross-platform data serialization. Like those languages, it has a schema (in ASN.1, called a "module"), and a set of encodings, typically type–length–value encodings. Unlike them, ASN.1 does not provide a single and readily usable open-source implementation, and is published as a specification to be implemented by third-party vendors. However, ASN.1, defined in 1984, predates them by many years. It also includes a wider variety of basic data types, some of which are obsolete, and has more options for extensibility. A single ASN.1 message can include data from multiple modules defined in multiple standards, even standards defined years apart.

ASN.1 also includes built-in support for constraints on values and sizes. For instance, a module can specify an integer field that must be in the range 0 to 100. The length of a sequence of values (an array) can also be specified, either as a fixed length or a range of permitted lengths. Constraints can also be specified as logical combinations of sets of basic constraints.

Values used as constraints can either be literals used in the PDU specification, or ASN.1 values specified elsewhere in the schema file. Some ASN.1 tools will make these ASN.1 values available to programmers in the generated source code. Used as constants for the protocol being defined, developers can use these in the protocol's logic implementation. Thus all the PDUs and protocol constants can be defined in the schema, and all implementations of the protocol in any supported language draw upon those values. This avoids the need for developers to hand code protocol constants in their implementation's source code. This significantly aids protocol development; the protocol's constants can be altered in the ASN.1 schema and all implementations are updated simply by recompiling, promoting a rapid and low risk development cycle.

If the ASN.1 tools properly implement constraints checking in the generated source code, this acts to automatically validate protocol data during program operation. Generally ASN.1 tools will include constraints checking into the generated serialization / deserialization routines, raising errors or exceptions if out-of-bounds data is encountered. It is complex to implement all aspects of ASN.1 constraints in an ASN.1 compiler. Not all tools support the full range of possible constraints expressions. XML schema and JSON schema both support similar constraints concepts. Tool support for constraints varies. Microsoft's xsd.exe compiler ignores them.

### Schema translation

Some ASN.1 tools are able to translate between ASN.1 and XML schema (XSD). The translation is standardised by the ITU. This makes it possible for a protocol to be defined in ASN.1, and also automatically in XSD. Thus it is possible (though perhaps ill-advised) to have in a project an XSD schema being compiled by ASN.1 tools producing source code that serializes objects to/from JSON wireformat. A more practical use is to permit other sub-projects to consume an XSD schema instead of an ASN.1 schema, perhaps suiting tools availability for the sub-projects language of choice, with XER used as the protocol wireformat.

OSS Nokalva offers a tool for converting a JSON data object or a JSON schema into an ASN.1 definition. There is not yet a tool for generating a JSON schema describing the JER-encoded structure of an ASN.1 data structure.

OSS Nokalva also offers a tool for converting a Protocol Buffers schema into an ASN.1 definition.

### Schema-optional formats

Many programming languages define language-specific serialization formats. For instance, Python's "pickle" module and Ruby's "Marshal" module. These formats do not require a schema. They are generally language-specific, which makes them easier to use in ad hoc storage scenarios, but inappropriate for communications protocols.

JSON and XML similarly do not require a schema, making them easy to use. They are also both cross-platform standards that are broadly popular for communications protocols, particularly when combined with a JSON schema or XML schema.

### Protocol definitions on different levels

ASN.1 is visually similar to Augmented Backus-Naur form (ABNF), which is used to define many Internet protocols like HTTP and SMTP. However, in practice they are quite different: ASN.1 defines a data structure, which can be encoded in various ways (e.g. JSON, XML, binary). ABNF, on the other hand, defines the encoding ("syntax") at the same time it defines the data structure ("semantics"). ABNF tends to be used more frequently for defining textual, human-readable protocols, and generally is not used to define type–length–value encodings.

ASN.1 is also visually similar to CSN.1. However, CSN.1 also defines the encoding of an object, specifically on the bit level.
