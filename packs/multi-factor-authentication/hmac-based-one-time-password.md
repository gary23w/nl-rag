---
title: "HMAC-based one-time password"
source: https://en.wikipedia.org/wiki/HMAC-based_one-time_password
domain: multi-factor-authentication
license: CC-BY-SA-4.0
tags: multi factor authentication, time based one time password, hmac based one time password, hardware security token, smart card authentication
fetched: 2026-07-02
---

# HMAC-based one-time password

**HMAC-based one-time password** (**HOTP**) is a one-time password (OTP) algorithm based upon a hash-based message authentication code (HMAC). When a client attempts to access a server, a challenge is sent by the destination server to the client. The client then computes a response which represents a one time password. This often forms part of multi-factor authentication protocols such as the Open Authentication initiative (OATH) challenge-response algorithm.

HOTP was published as an informational IETF RFC 4226 in December 2005, documenting the algorithm along with a Java implementation. Since then, the algorithm has been adopted by many companies worldwide (see below). The HOTP algorithm is a freely available open standard.

## Algorithm

The HOTP algorithm provides a method of authentication by symmetric generation of human-readable passwords, or *values*, each used for only one authentication attempt. The one-time property leads directly from the single use of each counter value.

Parties intending to use HOTP must establish some parameters; typically these are specified by the authenticator, and either accepted or not by the authenticated entity:

- A cryptographic hash method *H* (default is SHA-1)
- A secret key *K*, which is an arbitrary byte string and must remain private
- A counter *C*, which is 8 bytes long and counts the number of iterations
- A HOTP value length *d* (6–10, default is 6, and 6–8 is recommended)

Both parties compute the HOTP value derived from the secret key *K* and the counter *C*. Then the authenticator checks its locally generated value against the value supplied by the authenticated.

The authenticator and the authenticated entity increment the counter *C* independently. Since the authenticated entity may increment the counter more than the authenticator, RFC 4226 recommends a resynchronization protocol. It proposes that the authenticator repeatedly try verification ahead of their counter through a window of size *s*. The authenticator's counter continues forward of the value at which verification succeeds, and requires no actions by the authenticated entity.

To protect against brute-force attacks targeting the small size of HOTP values, the RFC also recommends implementing persistent throttling of HOTP verification. This can be achieved by either locking out verification after a small number of failed attempts, or by linearly increasing the delay after each failed attempt.

6-digit codes are commonly provided by proprietary hardware tokens from a number of vendors informing the default value of *d*. Truncation extracts 31 bits or ${\textstyle \log _{10}(2^{31})\approx 9.3}$ decimal digits, meaning that *d* can be at most 10, with the 10th digit adding less variation, taking values of 0, 1, and 2 (i.e., 0.3 digits).

After verification, the authenticator can authenticate itself simply by generating the next HOTP value, returning it, and then the authenticated can generate their own HOTP value to verify it. Note that counters are guaranteed to be synchronised at this point in the process.

The *HOTP value* is the human-readable design output, a *d*-digit decimal number (without omission of leading 0s):

HOTP value

=

HOTP

(

K

,

C

) mod 10

d

.

That is, the value is the *d* least significant base-10 digits of HOTP.

*HOTP* is a truncation of the HMAC of the counter *C* (under the key *K* and hash function *H*):

HOTP

(

K

,

C

) = truncate(HMAC

H

(

K

,

C

)),

where the counter *C* must be used big-endian.

Truncation first takes the 4 least significant bits of the *MAC* and uses them as a byte offset *i*:

truncate(

MAC

) = extract31(

MAC

,

MAC

[(19 × 8 + 4):(19 × 8 + 7)]),

where ":" is used to extract bits from a starting bit number up to and including an ending bit number, where these bit numbers are 0-origin. The use of "19" in the above formula relates to the size of the output from the hash function. With the default of SHA-1, the output is 20 bytes, and so the last byte is byte 19 (0-origin).

That index *i* is used to select 31 bits from *MAC*, starting at bit *i* × 8 + 1:

extract31(

MAC

,

i

) =

MAC

[(

i

× 8 + 1):(

i

× 8 + 4 × 8 − 1)].

31 bits are a single bit short of a 4-byte word. Thus the value can be placed inside such a word without using the sign bit (the most significant bit). This is done to definitely avoid doing modular arithmetic on negative numbers, as this has many differing definitions and implementations.

### Implementation

The following Python code implements the HMAC-SHA1 and HOTP algorithms.

```mw
import hashlib

def hmac_sha1(*, key: bytes, msg: bytes) -> bytes:
    if len(key) > 64:
        key = hashlib.sha1(key).digest()
    else:
        key = key.ljust(64, b'\0')
    o_key_pad = bytes(i ^ 0x5c for i in key)
    i_key_pad = bytes(i ^ 0x36 for i in key)
    return hashlib.sha1(
        o_key_pad +
        hashlib.sha1(i_key_pad + msg).digest()
    ).digest()

def hotp(*, key: bytes, ctr: int, length: int) -> str:
    mac = hmac_sha1(key=key, msg=ctr.to_bytes(8, 'big'))
    offset = mac[-1] & 0xf
    truncated = bytearray(mac[offset:offset+4])
    truncated[0] &= 0x7f
    value = int.from_bytes(truncated, 'big') % (10**length)
    return str(value).rjust(length, '0')
```

### `otpauth://` URI scheme

Some implementations of HOTP and TOTP for smartphones allow users to scan QR codes to add HOTP and TOTP tokens to their authenticator apps. These QR codes contain Uniform Resource Identifiers (URIs) with the scheme `otpauth://`.

HOTP `otpauth://` URIs begin with `otpauth://hotp/` and must contain a label, secret, and counter. The label is encoded as part of the path, while the secret and counter are encoded as query parameters. The URI may optionally contain other fields, such as the number of digits (which defaults to 6), the algorithm used (which defaults to SHA1), and the issuer name.

The secret is encoded as RFC 4648 Base32, with padding omitted. For example, the URI `otpauth://hotp/Wikipedian?secret=JBSWY3DPFQQHO33SNRSCC&counter=42` represents a HOTP token labeled "Wikipedian", with the secret `Hello, world!` encoded as ASCII, and the initial counter 42. When added to an authenticator, it should produce the code `439256`.

## Tokens

Both hardware and software tokens are available from various vendors, for some of them see references below.

Software tokens are available for (nearly) all major mobile/smartphone platforms (J2ME, Android, iPhone, BlackBerry, Maemo, macOS, and Windows Mobile).

## Reception

Although the early reception from some of the computer press was negative during 2004 and 2005, after IETF adopted HOTP as RFC 4226 in December 2005, various vendors started to produce HOTP-compatible tokens and/or whole authentication solutions.

According to the article "Road Map: Replacing Passwords with OTP Authentication" on strong authentication, published by Burton Group (a division of Gartner, Inc.) in 2010, "Gartner's expectation is that the hardware OTP form factor will continue to enjoy modest growth while smartphone OTPs will grow and become the default hardware platform over time."
