---
title: "Decentralized identifier"
source: https://en.wikipedia.org/wiki/Decentralized_identifier
domain: self-sovereign-identity
license: CC-BY-SA-4.0
tags: self sovereign identity, user controlled identity, decentralized identifier wallet, verifiable credential holder, digital identity ownership
fetched: 2026-07-02
---

# Decentralized identifier

A **decentralized identifier (DID)** is a type of globally unique identifier that enables an entity to be identified in a manner that is verifiable, persistent (as long as the DID controller desires), and does not require the use of a centralized registry. DIDs enable a new model of decentralized digital identity that is often referred to as a self-sovereign identity (SSI). This emerging model of digital identity, based on DIDs and SSIs, puts users in full control of their identity data and addresses key limitations of centralized and federated identity providers, including security vulnerabilities, large-scale data breaches, limited privacy protections, and insufficient user control. The DIDs are an important component of decentralized web applications. A decentralized identity management system based on Decentralized Identifiers and Self-Sovereign Identity principles, usually starts from a reference architecture involving Issuers, Holders, and Verifiers, with digital wallets or agents acting on behalf of identity subjects, and a specific identity infrastructure that supports issuance, validation and revocation of credentials.

## DID documents

A decentralized identifier resolves (points) to a **DID document**, a set of data describing the DID subject, including mechanisms, such as cryptographic public keys, that the DID subject or a DID delegate can use to authenticate itself and prove its association with the DID.

## DID methods

Just as there are many different types of URIs, all of which conform to the URI standard, there are many different types of **DID methods**, all of which must conform to the DID standard. Each DID method specification must define:

- The name of the DID method (which must appear between the first and second colon, e.g., did:**example**:).
- The structure of the unique identifier that must follow the second colon.
- The technical specifications for how a DID resolver can apply the CRUD operations to create, read, update, and deactivate a DID document using that method.

The W3C DID Working Group maintains a registry of DID methods.

## Usage of DIDs

A DID identifies any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) that the controller of the DID decides that it identifies. DIDs are designed to enable the controller of a DID to prove control over it and to be implemented independently of any centralized registry, identity provider, or certificate authority. DIDs are URIs that associate a DID subject with a DID document. Each DID document can express cryptographic material, verification methods, and service endpoints to enable trusted interactions associated with the DID subject. A DID document might contain additional semantics about the subject that it identifies. A DID document might also contain the DID subject itself (e.g. a data model).

National efforts include the European Digital Identity (EUDI) Wallet as a part of eIDAS 2.0 in the European Union, and China Real-Name Decentralized Identifier System (China RealDID) under China's Ministry of Public Security. The AT Protocol and applications powered by the protocol such as Bluesky use DIDs for their identity system in order to give users full control over their identity, including where their data is stored. The protocol uses its own DID method, did:plc, as well as a general domain-based method with did:web.

Persona is an identity verification company founded in 2018. Its product consists of uploading a government-issued ID and potentially taking a selfie to confirm the user's identity and give them a DID identity. The service is used by the LinkedIn professional networking site, the Discord and Reddit social media networks, the Roblox video game platform, and the OpenAI artificial intelligence company.

Polygon ID is a privacy-focused digital identity solution developed by Polygon, a blockchain scaling platform. It leverages zero-knowledge proofs (ZKPs) to allow users to verify specific aspects of their identity—such as age or residency—without revealing underlying personal data. This enables secure and private interactions with services that require identity verification, such as financial platforms, voting systems, or DAO governance, while preserving user anonymity. Polygon ID is already being explored by governments and organizations seeking compliant and privacy-preserving identity systems in Web3 environments.

## Standardization efforts

The W3C DID Working Group developed a specification for decentralized identifiers to standardize the core architecture, data model, and representation of DIDs.

The W3C approved the DID 1.0 specification as a W3C Recommendation on July 19, 2022.

The Decentralized Identity Foundation (DIF) published a Dynamic Traveler Profile Generation Specification in June 2023, for use cases in the travel industry.
