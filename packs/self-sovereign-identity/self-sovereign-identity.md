---
title: "Self-sovereign identity"
source: https://en.wikipedia.org/wiki/Self-sovereign_identity
domain: self-sovereign-identity
license: CC-BY-SA-4.0
tags: self sovereign identity, user controlled identity, decentralized identifier wallet, verifiable credential holder, digital identity ownership
fetched: 2026-07-02
---

# Self-sovereign identity

**Self-sovereign identity** (**SSI**) is an approach to digital identity that gives individuals control over the information they use to prove who they are to websites, services, and applications across the web. Without SSI, individuals with persistent accounts (identities) across the internet must rely on a number of large identity providers, such as Facebook (Facebook Connect) and Google (Google Sign-In), that have control of the information associated with their identity. If a user chooses not to use a large identity provider, then they have to create new accounts with each service provider, which fragments their web experiences. Self-sovereign identity offers a way to avoid these two undesirable alternatives. In a self-sovereign identity system, the user accesses services in a streamlined and secure manner, while maintaining control over the information associated with their identity. SSI systems are commonly built upon Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs). DIDs provide decentralized, cryptographically verifiable identifiers that enable secure authentication without centralized registries, while verifiable credentials allow trusted issuers to attest to specific claims about an identity subject. These credentials can be presented and verified cryptographically, often without direct interaction with the issuer at the time of verification.

## Background

The TCP/IP protocol provides identifiers for machines, but not for the people and organisations operating the machines. This makes the network-level identifiers on the internet hard to trust and rely on for information and communication for a number of reasons:

1. Hackers can easily change a computer’s hardware or IP address.
2. Services provide identifiers for the user, not the network. The absence of reliable identifiers is one of the primary sources of cybercrime, fraud, and threats to privacy on the internet.

With the advent of blockchain technology, a new model for decentralized identity emerged in 2015. The FIDO Alliance proposed an identity model that was no longer account-based, but identified people through direct, private, peer-to-peer connections secured by public/private key cryptography. Self-Sovereign Identity (SSI) summarises all components of the decentralized identity model: digital wallets, digital credentials, and digital connections.

## Technical aspects

SSI addresses the difficulty of establishing trust in an interaction. In order to be trusted, one party in an interaction will present credentials to the other parties, and those relying on the parties can verify that the credentials came from an issuer that they trust. In this way, the verifier's trust in the issuer is transferred to the credential holder. This basic structure of SSI with three participants is sometimes called "the trust triangle".

It is generally recognized that for an identity system to be self-sovereign, users control the verifiable credentials that they hold, and their consent is required to use those credentials. This reduces the unintended sharing of users' personal data. This is contrasted with the centralized identity paradigm where identity is provided by some outside entity.

In an SSI system, holders generate and control unique identifiers called decentralized identifiers. Most SSI systems are decentralized, where the credentials are managed using crypto wallets and verified using public-key cryptography anchored on a distributed ledger. The credentials may contain data from an issuer's database, a social media account, a history of transactions on an e-commerce site, or attestation from friends or colleagues.

### Blockchain account standards

Some blockchain identity systems use smart contracts as accounts with attachable data and permissions. ERC-725 is a draft Ethereum standard for smart-contract accounts with generic data storage and execution. LUKSO's Universal Profiles apply this model to on-chain profiles, combining a recoverable smart-contract account with public profile data for decentralized applications.

## National digital identity systems

### European Union

The European Union is exploring decentralized digital identity through a number of initiatives including the International Association for Trusted Blockchain Application (INATBA), the EU Blockchain Observatory & Forum and the European SSI Framework. In 2019, the EU created an eIDAS compatible European Self-Sovereign Identity Framework (ESSIF). The ESSIF makes use of decentralized identifiers (DIDs) and the European Blockchain Services Infrastructure (EBSI).

### Korea

The Korean government created a public/private consortium specifically for decentralized identity.

### Germany

In the German and European legal area, there are two regulations that are of particular importance for the topic. These include the eIDAS Regulation, which forms the most important framework for trust in electronic identification in the EU and is a fundamental building block of the digital single market. The European Blockchain Service Infrastructure (EBSI) has provided the SSI eIDAS Bridge, as a technical implementation that enables a substantial level of trust. The eIDAS SSI legal report also describes several scenarios of how SSI can fulfill the necessary regulatory conditions.

Furthermore, the General Data Protection Regulation (GDPR) forms the legal basis for the handling of personal data. The EBSI GDPR Legal Report provides more information on this.

## Concerns

### Implementation and semantic confusion

SSI is a value laden technology whose technical operationalizations differ (see Technical aspects). Therefore, its implementations can vary significantly and embed into the very technology different goals, agenda, and intentions.

The term "self-sovereign identity" can create expectations that individuals have absolute control and ownership over their digital identities, akin to physical possessions. However, in practice, SSI involves complex technical infrastructure, interactions with identity issuers and verifiers, and compliance with legal frameworks. The reality may not align with the perception generated by the term, leading to semantic confusion.

### Digital literacy

Critics argue that SSI may exacerbate social inequalities and exclude those with limited access to technology or digital literacy. SSI assumes reliable internet connectivity, access to compatible devices, and proficiency in navigating digital systems. Consequently, marginalized populations, including the elderly, individuals in developing regions, or those with limited technological resources, may face exclusion and reduced access to the benefits of SSI.
