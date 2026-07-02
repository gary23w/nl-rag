---
title: "Time-based one-time password"
source: https://en.wikipedia.org/wiki/Time-based_one-time_password
domain: multi-factor-authentication
license: CC-BY-SA-4.0
tags: multi factor authentication, time based one time password, hmac based one time password, hardware security token, smart card authentication
fetched: 2026-07-02
---

# Time-based one-time password

**Time-based one-time password** (**TOTP**) is a computer algorithm that generates a one-time password (OTP) using the current time as a source of uniqueness. As an extension of the HMAC-based one-time password (HOTP) algorithm, it has been adopted as Internet Engineering Task Force (IETF) standard RFC 6238.

TOTP is a cornerstone of the Initiative for Open Authentication (OATH) and is used in a number of two-factor authentication (2FA) systems.

## History

Through the collaboration of several OATH members, a TOTP draft was developed in order to create an industry-backed standard. It complements the event-based one-time standard HOTP, and it offers end user organizations and enterprises more choice in selecting technologies that best fit their application requirements and security guidelines. In 2008, OATH submitted a draft version of the specification to the IETF. This version incorporates all the feedback and commentary that the authors received from the technical community based on the prior versions submitted to the IETF. In May 2011, TOTP officially became RFC 6238.

## Algorithm

To establish TOTP authentication, the authenticatee and authenticator must pre-establish both the HOTP parameters and the following TOTP parameters:

- *T*0, the Unix time from which to start counting time steps (default is 0),
- *TX*, an interval which will be used to calculate the value of the counter *CT* (default is 30 seconds).

Both the authenticator and the authenticatee compute the TOTP value, then the authenticator checks whether the TOTP value supplied by the authenticatee matches the locally generated TOTP value. Some authenticators allow values that should have been generated before or after the current time in order to account for slight clock skews, network latency and user delays.

TOTP uses the HOTP algorithm, replacing the counter with a non-decreasing value based on the current time:

TOTP value(*K*) = HOTP value(*K*, *CT*),

calculating counter value $C_{T}=\left\lfloor {\frac {T-T_{0}}{T_{X}}}\right\rfloor ,$ where

- *CT* is the count of the number of durations *TX* between *T*0 and *T*,
- *T* is the current time in seconds since a particular epoch,
- *T*0 is the epoch as specified in seconds since the Unix epoch (e.g. if using Unix time, then *T*0 is 0),
- *TX* is the length of one-time duration (e.g. 30 seconds).

### `otpauth://` URI scheme

Some implementations of TOTP for smartphones allow users to scan QR codes to add HOTP and TOTP tokens to their authenticator apps. These QR codes contain Uniform Resource Identifiers (URIs) with the scheme `otpauth://`.

TOTP `otpauth://` URIs begin with `otpauth://totp/` and must contain a label and secret. The label is encoded as part of the path, while the secret is encoded as query parameters. The URI may optionally contain other fields, such as the number of digits (which defaults to 6), the algorithm used (which defaults to SHA1), the period (which defaults to 30 seconds), and the issuer name.

The secret is encoded as RFC 4648 Base32, with padding omitted. For example, the URI `otpauth://totp/Wikipedian?secret=JBSWY3DPFQQHO33SNRSCC` represents a TOTP token labeled "Wikipedian" with the secret `Hello, world!` encoded as ASCII.

## Security

Unlike passwords, TOTP codes are only valid for a limited time. However, users must enter TOTP codes into an authentication page, which creates the potential for phishing attacks. However, due to the short window in which TOTP codes are valid, attackers must proxy the credentials in real time.

TOTP credentials are also based on a shared secret known to both the client and the server, creating multiple locations from which a secret can be stolen. An attacker with access to this shared secret could generate new, valid TOTP codes at will. This can be a particular problem if the attacker breaches a large authentication database.
