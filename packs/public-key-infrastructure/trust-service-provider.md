---
title: "Trust service provider"
source: https://en.wikipedia.org/wiki/Trust_service_provider
domain: public-key-infrastructure
license: CC-BY-SA-4.0
tags: public key infrastructure, certificate authority, certificate revocation list, online certificate status protocol, trust service provider
fetched: 2026-07-02
---

# Trust service provider

A **trust service provider** (**TSP**) is a person or legal entity providing and preserving digital certificates to create and validate electronic signatures and to authenticate their signatories as well as websites in general. Trust service providers are qualified certificate authorities required in the European Union and in Switzerland in the context of regulated electronic signing procedures.

## History

The term *trust service provider* was coined by the European Parliament and the European Council as important and relevant authority providing non-repudiation to a regulated electronic signing procedure. It was first brought up in the Electronic Signatures Directive 1999/93/EC and was initially named *certification-service provider.* The directive was repealed by the eIDAS Regulation which became official on July 1, 2016. A regulation is a binding legislative act that requires all EU member states to follow.

## Description

The trust service provider has the responsibility to assure the integrity of electronic identification for signatories and services through strong mechanisms for authentication, electronic signatures and digital certificates. eIDAS defines the standards for how trust service providers are to perform their services of authentication and non-repudiation. The regulation provides guidance to EU member states on how trust service providers shall be regulated and recognized.

A trust service is defined as an electronic service that entails one of three possible actions. First it may concern the creation, the verification or the validation of electronic signatures, as well as time stamps or seals, electronically registered delivery services and certifications that are required with these services. The second action entails the creation, the verification as well as the validation of certificates that are used to authenticate websites. The third action is the preservation of these electronic signatures, the seals or the related certificates.

To be elevated to the level of a qualified trust service, the service must meet the requirements set under the eIDAS Regulation. Trust services provide a trust framework that facilitates continued relations for electronic transactions that are conducted between participating EU member states and organizations.

## Role of a qualified trust service provider

The qualified trust service provider plays an important role in the process of qualified electronic signing. The trust service providers must be given qualified status and permission for a supervisory government body to provide qualified digital certificates which can be used to create qualified electronic signatures. eIDAS requires that the EU will maintain an EU Trust List that lists the providers and services that have received qualified status. A trust service provider is not entitled to provide qualified trust services if they are not on the EU Trust List.

Trust service providers that are on the EU Trust List are required to follow the strict guidelines established under eIDAS. They need to provide stamps valid in time and date, when creating certificates. Signatures that have expired certificates need to be revoked immediately. The EU obliges the trust service providers to deliver appropriate training for all personnel employed by the trust service provider. They shall further provide tools such as software and hardware that is trustworthy and capable of preventing forgeries of the certificates that are produced.

## Vision

One of the major intents of eIDAS was to facilitate both public and business services, especially those that are conducted between parties across EU Member state borders. These transactions can now be safely expedited through the means of electronic signing and the services that are provided by trust service providers in regards to ensuring the integrity of those signatures.

EU member states are required through eIDAS to establish “points of single contact” (PSCs) for trust services that ensure that electronic ID schemes can be used for cross-board public sector transactions, including the exchange and access of healthcare information across borders.

## Legal perspective of electronic signatures created by trust service providers

While an advanced electronic signature is legally binding under eIDAS, a qualified electronic signature which has been created by a qualified trust service provider carries a higher probative value when used as evidence in court. Because the signature's authorship is considered non-repudiable, the authenticity of the signature cannot be easily challenged. EU member states are obligated to accept qualified electronic signatures that have been created with qualified certificate from other Member states as valid. According to the eIDAS Regulation, i.e. Article 24 (2), a signature created with a qualified certificate has the same legal value as a handwritten signature in court.

The standards are evolving. Additional standards including policy definitions for trust service providers are under development by the European Telecommunication Standards Institute ETSI.

## Global perspective

The Swiss digital signing standard ZertES has defined a comparable concept of certificate service providers. Certificate service providers need to be audited by conformity assessment bodies that have been appointed by the Schweizerische Akkreditierungsstelle. In the United States the NIST Digital Signature Standard (DSS) in its current release does not know anything comparable to a qualified trust service provider which would allow to enhance non-repudiation through the signatory's qualified certificate. However authors of the forthcoming review and commentators are publicly discussing an amendment similar to the eIDAS and ZertES approach of trusted service provision. To allow for stringent and non-repudiable global transactions and legal relevance, an international harmonization would be required.

## Controversy

Several research institutes and associations expressed their concern with respect to the establishment of a small group of centralized trust service providers per country which authenticate digital transactions. They state that this construct may have negative impact on privacy. Given the central role of trust service providers in many transactions, the Council of European Professional Informatics Societies (CEPIS) fears that trust service providers would gain and collect information of the distinguishing attributes of the citizens, which are subject of authentication. With regard to their requirement to preserve data and resulting expected efforts to keep evidence for potential liability requests on inaccurate ID, CEPIS sees the risk that trust service providers could create and store log entries of all authentication processes. The information gained allows for monitoring and for the profiling of the involved citizens. If the transaction counterpart also identifies himself, user interests and their communication behaviour will additionally sharpen the profiles gained. Big data analysis would allow for far-reaching insights into the citizens' privacy and relationships. The direct connection to the qualifying governmental bodies could allow those to gain access to the gained data and profiles.

Another publication claims that to truly take advantage of the secure and seamless cross-border electronic transactions, assurance levels, definitions and technical deployment need to be specified more precisely.

In 2021, relatively vague proposed updates to eIDAS would require browsers to pass on assurances from TSPs to their users. This would apparently involve the incorporation of government-specified TSPs in parallel with the existing multi-stakeholder processes used by browsers to establish trust in Certificate authorities. The Internet Society and Mozilla asserted a variety of issues with the proposals.

In 2024, concerns were also raised about the fundamental security implications of entrusting private key custody to trust service providers, emphasizing that such delegation may undermine user autonomy by removing exclusive control over cryptographic keys.
