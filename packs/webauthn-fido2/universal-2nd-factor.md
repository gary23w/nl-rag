---
title: "Universal 2nd Factor"
source: https://en.wikipedia.org/wiki/Universal_2nd_Factor
domain: webauthn-fido2
license: CC-BY-SA-4.0
tags: webauthn, fido2 authentication, fido alliance, client to authenticator protocol, hardware security key
fetched: 2026-07-02
---

# Universal 2nd Factor

**Universal 2nd Factor** (**U2F**) is an open standard that strengthens and simplifies two-factor authentication (2FA) using specialized Universal Serial Bus (USB), near-field communication (NFC), or Bluetooth Low Energy (BLE) devices based on similar security technology found in smart cards. It is superseded by the FIDO2 Project, which includes the W3C Web Authentication (WebAuthn) standard and the FIDO Alliance's Client to Authenticator Protocol 2 (CTAP2).

While initially developed by Google and Yubico, with contribution from NXP Semiconductors, the standard is now hosted by the FIDO Alliance.

While time-based one-time password (TOTPs) (e.g. 6-digit codes generated on Google Authenticator) were a significant improvement over SMS-based security codes, a number of security vulnerabilities were still possible to exploit, which U2F sought to improve. Specifically:

| Issue | TOTP | U2F |
|---|---|---|
| Shared secret | Plaintext or QR code transmission of shared secret between server and user Shared secret may be stored in plaintext on server | Transmission of public key challenge / response Private key only stored on user hardware device |
| Man-in-the-middle attack | Plaintext code response vulnerable to interception and MITM attack if user has been phished by malicious website | Challenge / response is signed (encoding originating domain/website) to prevent interception and reuse |
| Convenience / eavesdropping | Plaintext code is displayed and typed by user manually, visually Prone to mistyping, error | Transmission / creation of authentication code is via USB or NFC between hardware key and computer without manual typing steps |

In terms of disadvantages, one significant difference and potential drawback to be considered regarding hardware-based U2F solutions is that unlike with TOTP shared-secret methods, there is no possibility of "backing up" recovery codes or shared secrets. If a hardware duplicate or alternative hardware key is not kept and the original U2F hardware key is lost, no recovery of the key is possible (because the private key exists only in hardware). Therefore, for services that do not provide any alternative account recovery method, the use of U2F should be carefully considered.

## Design

The USB devices communicate with the host computer using the human interface device (HID) protocol, the same protocol used by mice, keyboards, and other input devices. This avoids the need for the user to install special hardware driver software in the host computer and permits application software (such as a browser) to directly access the security features of the device without user effort other than possessing and inserting the device. Once communication is established, the application exercises a challenge–response authentication with the device using public-key cryptography methods and a secret unique device key manufactured into the device.

## Vulnerabilities

The device key is vulnerable to malicious manufacturer duplication.

In 2020, independent security researchers found a method to extract private keys from Google Titan Key, a popular U2F hardware security token. The method required physical access to the key for several hours, several thousand euros-worth of equipment, and was destructive to the plastic case of the key. The attackers concluded that the difficulty of the attack meant that people were still safer to use the keys than not. The attack was possible due to a vulnerability in the A700X microchip made by NXP Semiconductors, which is also used in security tokens made by Feitian and Yubico, meaning that those tokens are also vulnerable. The vulnerability was responsibly disclosed to the affected manufacturers so that it might be fixed in future products.

## Support and use

U2F security keys are supported by Google Chrome since version 38, Firefox since version 57 and Opera since version 40. U2F security keys can be used as an additional method of two-step verification on online services that support the U2F protocol, including Google, Azure, Dropbox, GitHub, GitLab, Bitbucket, Nextcloud, Facebook, and others.

Chrome, Firefox, and Opera were, as of 2015, the only browsers supporting U2F natively. Microsoft has enabled FIDO 2.0 support for Windows 10's Windows Hello login platform. Microsoft Edge browser gained support for U2F in the October 2018 Windows Update. Microsoft accounts, including Office 365, OneDrive, and other Microsoft services, do not yet have U2F support. Mozilla has integrated it into Firefox 57, and enabled it by default in Firefox 60 and Thunderbird 60. Microsoft Edge starting from build 17723 support FIDO2. As of iOS and iPadOS 13.3 Apple now supports U2F in the Safari browser on those platforms.

## Specifications

The U2F standard has undergone two major revisions:

- U2F 1.0 Proposed Standard (October 9, 2014)
- U2F 1.2 Proposed Standard (April 11, 2017)

Additional specification documents may be obtained from the FIDO web site.

The U2F 1.0 Proposed Standard (October 9, 2014) was the starting point for a short-lived specification known as the FIDO 2.0 Proposed Standard (September 4, 2015). The latter was formally submitted to the World Wide Web Consortium (W3C) on November 12, 2015. Subsequently, the first Working Draft of the W3C Web Authentication (WebAuthn) standard was published on May 31, 2016. The WebAuthn standard has been revised numerous times since then, becoming a W3C Recommendation on March 4, 2019.

Meanwhile the U2F 1.2 Proposed Standard (April 11, 2017) became the starting point for the Client to Authenticator Protocol (CTAP) Proposed Standard, which was published on September 27, 2017. FIDO CTAP complements W3C WebAuthn, both of which are in scope for the FIDO2 Project.

WebAuthn and CTAP provide a complete replacement for U2F, which has been renamed "CTAP1" in the latest version of the FIDO2 standard. The WebAuthn protocol is backward-compatible (via the AppID extension) with U2F-only security keys but the U2F protocol is not compatible with a WebAuthn-only authenticator. Some authenticators support both U2F and WebAuthn while some WebAuthn clients support keys created via the legacy U2F API.
