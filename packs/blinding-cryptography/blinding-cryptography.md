---
title: "Blinding (cryptography)"
source: https://en.wikipedia.org/wiki/Blinding_(cryptography)
domain: blinding-cryptography
license: CC-BY-SA-4.0
tags: cryptographic blinding, rsa blinding defense, message randomization countermeasure, side channel blinding
fetched: 2026-07-02
---

# Blinding (cryptography)

In cryptography, **blinding** first became known in the context of blind signatures, where the message author *blinds* the message with a random *blinding factor*, the signer then signs it and the message author "*unblinds"* it*;* signer and message author are different parties.

Since the late 1990s, **blinding** mostly refers to countermeasures against side-channel attacks on encryption devices, where the random *blinding* and the "*unblinding"* happen on the encryption devices. The techniques used for blinding signatures were adapted to prevent attackers from knowing the input to the modular exponentiation function for Diffie-Hellman or RSA.

Blinding must be applied with care, for example Rabin–Williams signatures. If blinding is applied to the formatted message but the random value does not honor Jacobi requirements on *p* and *q*, then it could lead to private key recovery. A demonstration of the recovery can be seen in CVE-2015-2141 discovered by Evgeny Sidorov.

Side-channel attacks allow an adversary to recover information about the input to a cryptographic operation within an asymmetric encryption scheme, by measuring something other than the algorithm's result, e.g., power consumption, computation time, or radio-frequency emanations by a device. Typically these attacks depend on the attacker knowing the characteristics of the algorithm, as well as (some) inputs. In this setting, blinding serves to alter the algorithm's input into some unpredictable state. Depending on the characteristics of the blinding function, this can prevent some or all leakage of useful information. Note that security depends also on the resistance of the blinding functions themselves to side-channel attacks.

## Examples

- In RSA blinding involves computing the blinding operation *E*(*x*) = *(xr)e* mod *N*, where *r* is a random integer between 1 and *N* and relatively prime to *N* (i.e. gcd(*r*, *N*) = 1), *x* is the plaintext, *e* is the public RSA exponent and *N* is the RSA modulus. As usual, the decryption function *f*(*z*) = *zd* mod *N* is applied thus giving *f*(*E*(*x*)) = *(xr)ed* mod *N* = *xr* mod *N*. Finally it is unblinded using the function *D*(*z*) = *zr*−1 mod *N*. Multiplying *xr* mod *N* by *r−1* mod *N* yields *x*, as desired. When decrypting in this manner, an adversary who is able to measure time taken by this operation would not be able to make use of this information (by applying timing attacks RSA is known to be vulnerable to) as they does not know the constant *r* and hence has no knowledge of the real input fed to the RSA primitives.

- Blinding in GPG 1.x
