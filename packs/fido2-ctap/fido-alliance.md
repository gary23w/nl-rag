---
title: "FIDO Alliance"
source: https://en.wikipedia.org/wiki/FIDO_Alliance
domain: fido2-ctap
license: CC-BY-SA-4.0
tags: fido2 ctap protocol, client to authenticator, webauthn ceremony, universal second factor, hardware security key
fetched: 2026-07-02
---

# FIDO Alliance

Previous logo of the FIDO Alliance

The **FIDO** (**Fast IDentity Online**) **Alliance** is an open industry association launched in February 2013 whose stated mission is to develop and promote authentication standards that "help reduce the world’s over-reliance on passwords". FIDO addresses the lack of interoperability among devices that use strong authentication and reduces the problems users face creating and remembering multiple usernames and passwords.

FIDO supports a full range of authentication technologies, including biometrics such as fingerprint and iris scanners, voice and facial recognition, as well as existing solutions and communications standards, such as Trusted Platform Modules (TPM), USB security tokens, embedded Secure Elements (eSE), smart cards, and near-field communication (NFC). The USB security token device may be used to authenticate using a simple password (e.g. four-digit PIN) or by pressing a button. The specifications emphasize a device-centric model. Authentication over an insecure channel happens using public-key cryptography. The user's device registers the user to a server by registering a public key. To authenticate the user, the device signs a challenge from the server using the private key that it holds. The keys on the device are unlocked by a local user gesture such as a biometric or pressing a button.

FIDO provides two types of user experiences depending on which protocol is used. Both protocols define a common interface at the client for whatever local authentication method the user exercises.

## Specifications

The following open specifications may be obtained from the FIDO web site.

- Universal Authentication Framework (UAF)
  - UAF 1.0 Proposed Standard (December 8, 2014)
  - UAF 1.1 Proposed Standard (February 2, 2017)
  - UAF 1.2 Review Draft (November 28, 2017)

- Universal 2nd Factor (U2F)
  - U2F 1.0 Proposed Standard (October 9, 2014)
  - U2F 1.2 Proposed Standard (July 11, 2017)

- FIDO 2.0 (FIDO2, contributed to the W3C on November 12, 2015)
  - FIDO 2.0 Proposed Standard (September 4, 2015)

- Client to Authenticator Protocol (CTAP)
  - CTAP 2.0 Proposed Standard (September 27, 2017)
  - CTAP 2.0 Implementation Draft (February 27, 2018)

The U2F 1.0 Proposed Standard (October 9, 2014) was the starting point for the specification known as FIDO 2.0 Proposed Standard (September 4, 2015). The latter was formally submitted to the World Wide Web Consortium (W3C) on November 12, 2015. Subsequently, the first Working Draft of the W3C Web Authentication (WebAuthn) standard was published on May 31, 2016. The WebAuthn standard has been revised numerous times since then, becoming a W3C Recommendation on March 4, 2019.

Meanwhile the U2F 1.2 Proposed Standard (July 11, 2017) became the starting point for the Client to Authenticator Protocol 2.0 Proposed Standard, which was published on September 27, 2017. FIDO CTAP 2.0 complements W3C WebAuthn, both of which are in scope for the *FIDO2 Project*.

### FIDO2

The FIDO2 Project is a joint effort between the FIDO Alliance and the World Wide Web Consortium (W3C) whose goal is to create strong authentication for the web. At its core, FIDO2 consists of the W3C Web Authentication (WebAuthn) standard and the FIDO Client to Authenticator Protocol 2 (CTAP2). FIDO2 is based upon previous work done by the FIDO Alliance, in particular the Universal 2nd Factor (U2F) authentication standard.

Taken together, WebAuthn and CTAP specify a standard authentication protocol where the protocol endpoints consist of a user-controlled cryptographic authenticator (such as a smartphone or a hardware security key) and a WebAuthn Relying Party (also called a FIDO2 server). A web user agent (i.e., a web browser) together with a WebAuthn client form an intermediary between the authenticator and the relying party. A single WebAuthn client Device may support multiple WebAuthn clients. For example, a laptop may support multiple clients, one for each conforming user agent running on the laptop. A conforming user agent implements the WebAuthn JavaScript API.

As its name implies, the Client to Authenticator Protocol (CTAP) enables a conforming cryptographic authenticator to interoperate with a WebAuthn client. The CTAP specification refers to two protocol versions called CTAP1/U2F and CTAP2. An authenticator that implements one of these protocols is typically referred to as a U2F authenticator or a FIDO2 authenticator, respectively. A FIDO2 authenticator that also implements the CTAP1/U2F protocol is backward compatible with U2F.

The invention of using a smartphone as a cryptographic authenticator on a computer network is claimed in US patent 7,366,913 filed in 2002.

## Milestones

- (2014-10-09) The U2F 1.0 Proposed Standard was released
- (2014-12-08) The UAF 1.0 Proposed Standard was released
- (2015-06-30) The FIDO Alliance released two new protocols that support Bluetooth technology and near field communication (NFC) as transport protocols for U2F
- (2015-09-04) The FIDO 2.0 Proposed Standard was released
  - FIDO 2.0 Key Attestation Format
  - FIDO 2.0 Signature Format
  - FIDO 2.0 Web API for Accessing FIDO 2.0 Credentials
- (2015-11-12) The FIDO Alliance submitted the FIDO 2.0 Proposed Standard to the World Wide Web Consortium (W3C)
- (2016-02-17) The W3C created the Web Authentication Working Group
- (2017-02-02) The UAF 1.1 Proposed Standard was released
- (2017-07-11) The U2F 1.2 Proposed Standard was released
- (2017-09-27) The Client To Authenticator Protocol 2.0 Proposed Standard was released
- (2017-11-28) The UAF 1.2 Review Draft was released
- (2018-02-27) The Client To Authenticator Protocol 2.0 Implementation Draft was released
- (2019–03) W3C’s Web Authentication (WebAuthn) recommendation – a core component of the FIDO Alliance’s FIDO2 set of specifications – became an official web standard.
- (2019-09-04) FIDO Alliance launched Authenticate,  an annual conference dedicated to user authentication deployment and practices.
- (2019-12-18) FIDO Certification Program reached a milestone of 688 certified products.
- (2021-03-29) A collaborative educational resource combining FIDO authentication with web-based payment standards was launched by the FIDO Alliance, EMVCo, and the W3C.
- (2021-04-20) FIDO Alliance released the FIDO Device Onboard (FDO) protocol to secure Internet of Things (IoT) automated provisioning.
- (2023-06-16) The FIDO UAF 1.2 and CTAP 2.1 specifications were officially adopted as international standards by the International Telecommunication Union (ITU-T)
- (2023-11-02)  FIDO protocols were included by ENISA and ETSI in their architectural guidelines for European eIDAS2 digital identity wallets.
- (2025-04-29) FIDO Alliance established a Payment Working Group (PWG) to define and drive FIDO solutions for payment use cases
- (2026-05-07) Global deployment of active passkeys was estimated to have reached 5 billion in an announcement on World Passkey Day 2026.

## FIDO members

### Board level members

- 1Password
- Amazon
- American Express
- Apple
- Axiad
- Bank of America
- Beyond Identity
- Cisco
- CVS Health
- Daon
- Dashlane
- Dell
- Egis
- Feitian
- Google
- HYPR
- IDEMIA
- infineon
- intel
- Intuit
- Jumio
- LastPass
- Lenovo
- LY Corporation
- Mastercard
- Mercari
- Meta Platforms
- Microsoft
- Nok Nok
- NTT Docomo
- OneSpan
- PayPal
- PNC Bank
- Prove Identity
- Qualcomm
- Raon
- RSA Security
- Samsung
- Thales Group
- TikTok
- Trusona
- US Bank
- Visa
- Wells Fargo
- Yubico

### Sponsor level members

- 1Kosmos
- AIRCUVE
- Akamai Technologies
- AU10TIX
- Avast
- BankAxept
- Bitwarden
- Binance
- Groupement des Cartes Bancaires CB
- JPMorgan Chase
- Coinbase
- CompoSecure
- CyberArk
- Devolutions
- DocuSign
- eBay
- Entersekt
- EXCELSECU
- Fime
- Fujitsu
- Futurae Technologies
- Giesecke+Devrient
- Oppo
- Hedera Hashgraph
- HID Global Corporation
- Hitachi
- HSBC
- Huawei Technologies
- IBM
- IDnow
- Industrial Technology Research Institute
- International Systems Research
- iProov
- JCB Co.
- KDDI
- Keeper (password manager)
- M&T Bank
- Mozilla
- NEC Corporation
- Nomura Research Institute
- Okta, Inc.
- Onfido
- Ping Identity
- Rakuten
- Red Hat
- Academia Sinica
- RoboForm
- Salesforce
- SBI Group
- Sentry Enterprises
- SK Telecom
- Socure
- SoftBank
- SOFTGIKEN
- Sony Corporation
- SSenStone
- Swiss Marketplace Group
- Swissbit
- Target Brands, Inc.
- MITRE Corporation
- Twilio
- The Vanguard Group
- Veridium
- Vingroup
- WiSECURE
- Worldline SA
- Yahoo

### Government level members

- Australian Government
- Ministry of Information and Communications (Vietnam)
- UK Cabinet Office
- Electronic Transactions Development Agency (Thailand)
- Federal Office for Information Security
- Ministry of Digital Affairs (Taiwan)
- Ministry of the Interior (Taiwan)
- National Institute of Standards and Technology
- TELECOM TECHNOLOGY CENTER (Taiwan)
- Telecommunication Technology Association (South Korea)

### Associate level members

List

- 4Auth Limited (trading as tru.ID)
- Accura Scan
- Advanced Card Systems Ltd.
- AirID GmbH
- AItrust Inc.
- Allthenticate
- Amwal Tech
- Anonybit
- Asignio, Inc.
- ASRock Industrial Computer Corp.
- atsec (Beijing) Information Technology Co., Ltd.
- AuthenticID
- AuthentOn
- AuthenTrend
- authID.ai
- Authme Co., Ltd.
- Authsignal Limited
- AuthX Security LLC
- Aware, Inc.
- AXELL CORPORATION
- Azimuth Labs Pte Ltd.
- BIO–key
- Biometric Associates, LP
- BIT4ID S.R.L.
- BixeLab Pty Ltd.
- Buypass AS
- Capy Inc.
- CardLab Innovation ApS
- Cathay Financial Holdings
- Changing Information Technology Inc.
- Chelpis Quantum Tech Co., LTD.
- China Financial Certification Authority
- ChipWon Technology
- Comsign Ltd.
- Coretech Knowledge Inc.
- Crosscert
- Cryptnox SA
- Cyber Street Solutions Corp.
- D–TRUST
- Dai Nippon Printing Co., Ltd
- Dapple Security
- Data Zoo
- Datasec Solutions Pty Ltd
- DDS, Inc.
- DeCloak Intelligences Co.
- Deepnet Security
- Descope Inc.
- e-Smart Systems Limited
- Easy Dynamics
- eDoktor Co, Ltd.
- ELAN Microelectronics Corporation
- emdha TSP
- eMudhra Technologies Limited
- Enpass Technologies Inc.
- Ensurity Technologies
- Entrust Datacard Corporation
- eTunnel Inc.
- EXGEN NETWORKS Co., Ltd.
- Fazpass
- Fingerprint Cards
- Foongtone Technology Co., Ltd.
- Frontegg
- Gallagher North America Inc.
- Gentex Corporation
- GoTrustID Inc.
- HANKO
- HAVENTEC GROUP SERVICES PTY LTD
- Hideez Poland Sp. z.o.o.
- Hypersecu Information Systems, Inc.
- Hyweb Global Technology Co. Ltd
- i-Sprint Innovations Pte Ltd
- ID R&D
- ID.me
- IDEATEC
- Identiv, Inc.
- Identy, Inc.
- IDEX Biometrics
- IDmelon Technologies Inc.
- ImprovelD
- Ingenium Biometrics Ltd
- Intelligent Information Security Technology Inc.
- Intercede
- IP Cube Co., Ltd.
- Kaizen Secure Voiz
- Kelvin Zero Inc.
- Keyless Technologies Ltd.
- Keytos
- KeyXentic
- KICA
- KONA I CO., LTD
- Kridentia Technology Sdn Bhd
- KSIGN
- LC&J Security Solutions
- Ledger
- LIQUID, Inc.
- Locii Innovation Pty Ltd trading as truth
- LoginID
- Loginradius
- LOGITECH EUROPE S.A.
- LuxTrust SA
- Lydsec Digital Technology Co., Ltd.
- Metalenz
- MK Group Joint Stock Company
- Mobile Technologies Limited
- MTRIX GmbH
- National Credit Card Center of ROC
- NEOWAVE
- NEVIS Security AG
- Nihon Jyoho System Co., LTD
- NOX Co., Ltd.
- Nulab Inc.
- Nymi Inc.
- OCR Labs Global
- Octacto Co., Ltd.
- OneLog AG
- Open Source Solution Technology Corporation
- Panasonic Holdings Corporation
- Passbolt
- Penril Datability
- PONE Biometrics
- Precision Biometric India Pvt. Ltd.
- PT Privy Identitas Digital
- QaiWare
- Quado, Inc.
- Quantum Networks
- RF Ideas Inc.
- Rock Solid Knowledge Ltd.
- Scramble ID, Inc.
- Secfense Inc.
- SECIOSS, Inc
- Secret Double Octopus
- SecuGen Corporation
- SecureAuth
- SecureKi
- Securemetric Technology Sdn Bhd
- Secuve Co., Ltd.
- Shenzhen National Engineering Laboratory (aka NELD TV)
- SmartDisplayer Technology
- SoloKeys
- Starfish GmbH & Co. KG
- Stellar Craft, Inc.
- Strivacity
- StrongKey
- Stytch, Inc.
- SurePassID
- SWEMPIRE Co., Ltd.
- Synaptics
- TEMET AG
- TendyRON
- TOKEN2
- Tokenize Inc.
- TOPPAN IDGATE
- Torus Labs Private Limited
- Tradelink Electronic Commerce Limited
- TraitWare Inc.
- Transmit Security
- Trillbit Inc.
- Trinamix GmbH
- Trust Stamp
- TrustAsia Technologies, Inc.
- TRUSTDOCK Inc.
- TruU, Inc.
- TWCA
- UAB 360 IT (NordPass)
- UberEther, Inc.
- Uniken Inc.
- UNIONCOMMUNITY Co., Ltd.
- VALMIDO
- VEAS JSC
- VeroGuard Systems Pty Ltd
- Versasec AB
- VisionLabs B.V.
- VP, Inc.
- VU LLC
- WebComm Technology Co., Ltd.
- WinMagic Corp.
- Wuhan Tianyu Information Industry Co. Ltd.
