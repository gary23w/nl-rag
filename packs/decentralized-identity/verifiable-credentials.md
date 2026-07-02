---
title: "Verifiable credentials"
source: https://en.wikipedia.org/wiki/Verifiable_credentials
domain: decentralized-identity
license: CC-BY-SA-4.0
tags: decentralized identity, decentralized identifier, verifiable credentials, self-sovereign identity
fetched: 2026-07-02
---

# Verifiable credentials

**Verifiable credentials** (VCs) are digital credentials which follow the relevant World Wide Web Consortium open standards. They can represent information found in physical credentials, such as a passport or license, as well as new things that have no physical equivalent, such as ownership of a bank account. They have numerous advantages over physical credentials, most notably that they're digitally signed, which makes them tamper-resistant and instantaneously verifiable.

Verifiable credentials can be issued by anyone, about anything, and can be presented to and verified by everyone. The entity that generates the credential is called the *Issuer*. The credential is then given to the *Holder* who stores it for later use. The Holder can then prove something about themselves by presenting their credentials to a *Verifier*.

## Standards

| standard | issuer | link | type |
|---|---|---|---|
| Verifiable Credentials Data Model v2.0 | World Wide Web Consortium | https://www.w3.org/TR/vc-data-model/ | standard |
| Verifiable Credentials Use Cases | World Wide Web Consortium | https://www.w3.org/TR/vc-use-cases/ | technical report |
|   |   |   |   |

## Trust model

The holder of a verifiable credential operates in a triangle of trust, mediating between issuer and verifier.

- The issuer trusts the holder
- The holder trusts the verifier
- The verifier trusts the issuer

Any role in the triangle can be played by a person, an institution, or a machine.

Note that because verifiable credentials can be created by anyone, the verifier decides if they trust the issuer.

## Decentralization

The VC model places the holder of a credential at the center of the identity ecosystem, giving individuals control of their identity attributes. The W3C VC model parallels physical credentials: the user holds cards and can present them to anyone at any time without informing or requiring the permission of the card issuer. Such a model is decentralized and gives much more autonomy and privacy to the participants. This contrasts with the federated identity management (FIM) model, as adopted by SAML and OpenID Connect, which place the identity provider (IdP) in the central role as the dispenser of identity attributes and the determiner of which Service Providers (SPs) it will give them to. In the federated model, the IdP knows every SP that the user visits.

## Verifiable Credentials Data Model 1.0

The data model for verifiable credentials is a World Wide Web Consortium (W3C) Recommendation, "Verifiable Credentials Data Model 1.0 - Expressing verifiable information on the Web", published 19 November 2019.

### Composition

Verifiable Credentials may be expressed using JSON and is typically composed of:

- Context
- Issuer
- Issue timestamp
- Expiry timestamp
- Type
- Subject
- Subject identity attributes
- Cryptographic proof to ensure the integrity and authenticity of the VC

```mw
{
	"verifiableCredential": {
		"@context": [
			"https://www.w3.org/2018/credentials/v1",
			"https://www.w3.org/2018/credentials/examples/v1"
		],
		"id": "0892f680-6aeb-11eb-9bcf-f10d8993fde7",
		"type": [
			"VerifiableCredential",
			"UniversityDegreeCredential"
		],
		"issuer": {
			"id": "did:example:76e12ec712ebc6f1c221ebfeb1f",
			"name": "Acme University"
		},
		"issuanceDate": "2021-05-11T23:09:06.803Z",
		"credentialSubject": {
			"id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
			"degree": {
				"type": "BachelorDegree",
				"name": "Bachelor of Science"
			}
		},
		"proof": {
			"type": "Ed25519Signature2018",
			"created": "2021-05-17T15:25:26Z",
			"jws": "eyJhbGciOiJFZERTQYjY0Il19..nlcAA",
			"proofPurpose": "assertionMethod",
			"verificationMethod": "https://pathToIssuerPublicKey"
		}
	}
}
```

### Aliases

The VC context, defined using the `@context` JSON property, is a JSON-LD construct that allows user friendly terms to be used for JSON properties. According to the VC data model, the value of many properties must be a URI. Whilst these are globally unambiguous, (important for a global data model), they are not user-friendly. Consequently, the `@context` property allows short-form, user-friendly aliases to be defined for each URI. This makes it much easier, and more user-friendly, to specify VCs. An example is given below.

```mw
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "http://example.edu/credentials/3732",
  "type": ["VerifiableCredential", "UniversityDegreeCredential"],
  "issuer": "https://example.edu/issuers/14",
  "issuanceDate": "2010-01-01T19:23:24Z",
  "expirationDate": "2020-01-01T19:23:24Z",
  "credentialSubject": {
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
    "degree": {
      "type": "BachelorDegree",
      "name": "Bachelor of Science and Arts"
    }
  },
  "proof": { 
  }
}
```

W3C VCs are extensible. Any new property can be added to VCs, as determined by the issuer. Standard properties have been defined specifically as extension points. These include the following:

- terms of use - restrictions placed on the use of the VC by the issuer
- schema - defines VC contents
- evidence - information collected by issuer about the subject and/or attributes before issuing the VC
- status - pointers to where a verifier can discover the status of a VC (e.g., whether it has been revoked).

### Subject

The holder of a VC does not always have to be the subject of the credential. It is expected that most users will hold their own VCs, i.e., the holder and the subject will be the same entity. This need not always be the case. For example, when the VC subject is an infant, and the VC is a birth certificate, the holder may be one or both parents.

### Proofs

No proof mechanism is standardized but the data model is flexible enough to support various existing cryptographic mechanisms, such as digital signatures. Proof mechanisms that are in use include: JSON Web Tokens with JSON Web Signatures, JSON-LD proofs, and zero-knowledge proofs using schemes such as IBM's anonymous credentials.

## Transport

Various protocols are specified for carrying VCs from the issuer/IdP to the holder, and the holder to the verifier. Examples include:

- Aries RFC 0036: Issue Credential Protocol 1.0., and Aries RFC 0037: Present Proof Protocol 1.0
- David W Chadwick, Romain Laborde, Arnaud Oglaza, Remi Venant, Samer Wazan, Manreet Nijjar "Improved Identity Management with Verifiable Credentials and FIDO", IEEE Communications Standards Magazine Vol 3, Issue 4, Dec 2019, Pages 14–20

None of these protocols has become standardized. Many people who are experimenting with VCs use HTTPS to carry VCs between the various parties.

## Criticisms and concerns

The security of verifiable credentials in the context of COVID-19 vaccination and test certificates has been questioned. Verifiable credentials have also been subject to usability concerns.

Some have likened anyone being able to issue a verifiable credential being like a shop clerk deciding if they should accept an out-of-state license as proof of age when purchasing alcohol.
