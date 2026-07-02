---
title: "Ring signature"
source: https://en.wikipedia.org/wiki/Ring_signature
domain: monero-privacy
license: CC-BY-SA-4.0
tags: monero, xmr cryptocurrency, ring signature, privacy coin
fetched: 2026-07-02
---

# Ring signature

In cryptography, a **ring signature** is a type of digital signature that can be performed by any member of a set of users that each have keys. Therefore, a message signed with a ring signature is endorsed by someone in a particular set of people. One of the security properties of a ring signature is that it should be computationally infeasible to determine *which* of the set's members' keys was used to produce the signature. Ring signatures are similar to group signatures but differ in two key ways: first, there is no way to revoke the anonymity of an individual signature; and second, any set of users can be used as a signing set without additional setup.

Ring signatures were invented by Ron Rivest, Adi Shamir, and Yael Tauman Kalai, and introduced at ASIACRYPT in 2001. The name, *ring signature*, comes from the ring-like structure of the signature algorithm.

## Definition

Suppose that a set of entities each have public/private key pairs, (*P*1, *S*1), (*P*2, *S*2), ..., (*P**n*, *S**n*). Party *i* can compute a ring signature σ on a message *m*, on input (*m*, *S**i*, *P*1, ..., *P**n*). Anyone can check the validity of a ring signature given σ, *m*, and the public keys involved, *P*1, ..., *P**n*. If a ring signature is properly computed, it should pass the check. On the other hand, it should be hard for anyone to create a valid ring signature on any message for any set without knowing any of the private keys for that set.

## Applications and modifications

In the original paper, Rivest, Shamir, and Tauman described ring signatures as a way to leak a secret. For instance, a ring signature could be used to provide an anonymous signature from "a high-ranking White House official", without revealing which official signed the message. Ring signatures are right for this application because the anonymity of a ring signature cannot be revoked, and because the group for a ring signature can be improvised.

Another application, also described in the original paper, is for deniable signatures. Here the sender and the recipient of a message form a group for the ring signature, then the signature is valid to the recipient, but anyone else will be unsure whether the recipient or the sender was the actual signer. Thus, such a signature is convincing, but cannot be transferred beyond its intended recipient.

There were various works, introducing new features and based on different assumptions:

**Threshold ring signatures**

Unlike standard "

t

-out-of-

n

"

threshold signature

, where

t

of

n

users should collaborate to sign a message, this variant of a ring signature requires

t

users to cooperate in the ring signing

protocol

. Namely,

t

parties

S

1

, ...,

S

t

∈ {

P

1

, ...,

P

n

} can compute a (

t

,

n

)-ring signature, σ, on a message,

m

, on input (

m

,

S

1

, ...,

S

t

,

P

1

, ...,

P

n

).

**Linkable ring signatures**

The property of linkability allows one to determine whether any two signatures have been produced by the same member (under the same private key). The identity of the signer is nevertheless preserved. One of the possible applications can be an offline

e-cash system

.

**Traceable ring signature**

In addition to the previous scheme the public key of the signer is revealed (if they issue more than one signatures under the same private key). An

e-voting system

can be implemented using this protocol.

## Efficiency

Most of the proposed algorithms have asymptotic output size $O(n)$ ; i.e., the size of the resulting signature increases linearly with the size of input (number of public keys). That means that such schemes are impracticable for real use cases with sufficiently large n (for example, an e-voting with millions of participants). But for some application with relatively small median input size such estimate may be acceptable. CryptoNote implements $O(n)$ ring signature scheme by Fujisaki and Suzuki in p2p payments to achieve sender's untraceability.

More efficient algorithms have appeared recently. There are schemes with the sublinear size of the signature, as well as with constant size.

## Implementation

### Original scheme

The original paper describes an RSA based ring signature scheme, as well as one based on Rabin. They define a keyed "combining function" $C_{k,v}(y_{1},y_{2},\dots ,y_{n})$ which takes a key k , an initialization value v , and a list of arbitrary values $y_{1},\dots y_{n}$ . $y_{i}$ is defined as $g_{i}(x_{i})$ , where $g_{i}$ is a trap-door function (i.e. an RSA public key in the case of RSA based ring signatures).

The function $C_{k,v}(y_{1},y_{2},\dots ,y_{n})$ is called the ring equation, and is defined below. The equation is based on a symmetric encryption function $E_{k}$ :

$C_{k,v}(y_{1},y_{2},\dots ,y_{n})=E_{k}(y_{n}\oplus E_{k}(y_{n-1}\oplus E_{k}(\dots \oplus E_{k}(y_{1}\oplus v)\dots )))$

It outputs a single value z which is forced to be equal to v . The equation $v=C_{k,v}(y_{1},y_{2},\dots ,y_{n})$ can be solved as long as at least one $y_{i}$ , and by extension $x_{i}$ , can be freely chosen. Under the assumptions of RSA, this implies knowledge of at least one of the inverses of the trap door functions $g_{i}^{-1}$ (i.e. a private key), since $g_{i}^{-1}(y_{i})=x_{i}$ .

#### Signature generation

Generating a ring signature involves six steps. The plaintext is signified by m , the ring's public keys by $P_{1},P_{2},\dots ,P_{n}$ .

1. Calculate the key $k={\mathcal {H}}(m)$ , using a cryptographic hash function. This step assumes a random oracle for ${\mathcal {H}}$ , since k will be used as key for $E_{k}$ .
2. Pick a random glue value v .
3. Pick random $x_{i}$ for all ring members but yourself ( $x_{s}$ will be calculated using the **s**igner's private key), and calculate corresponding $y_{i}=g_{i}(x_{i})$ .
4. Solve the ring equation for $y_{s}$
5. Calculate $x_{s}$ using the signer's private key: $x_{s}=g_{s}^{-1}(y_{s})$
6. The ring signature now is the $(2n+1)$ -tuple $(P_{1},P_{2},\dots ,P_{n};v;x_{1},x_{2},\dots ,x_{n})$

#### Signature verification

Signature verification involves three steps.

1. Apply the public key trap door on all $x_{i}$ : $y_{i}=g_{i}(x_{i})$ .
2. Calculate the symmetric key $k={\mathcal {H}}(m)$ .
3. Verify that the ring equation holds $C_{k,v}(y_{1},y_{2},\dots ,y_{n})=v$ .

#### Python implementation

Here is a Python implementation of the original paper using RSA. Requires third-party module PyCryptodome.

```mw
import os
import hashlib
import random
import Crypto.PublicKey.RSA

import functools

class Ring:
    """RSA implementation."""

    def __init__(self, k, L: int = 1024) -> None:
        self.k = k
        self.l = L
        self.n = len(k)
        self.q = 1 << (L - 1)

    def sign_message(self, m: str, z: int):
        """Sign a message."""
        self._permut(m)
        s = [None] * self.n
        u = random.randint(0, self.q)
        c = v = self._E(u)

        first_range = list(range(z + 1, self.n))
        second_range = list(range(z))
        whole_range = first_range + second_range

        for i in whole_range:
            s[i] = random.randint(0, self.q)
            e = self._g(s[i], self.k[i].e, self.k[i].n)
            v = self._E(v ^ e)
            if (i + 1) % self.n == 0:
                c = v

        s[z] = self._g(v ^ u, self.k[z].d, self.k[z].n)
        return [c] + s

    def verify_message(self, m: str, X) -> bool:
        """Verify a message."""
        self._permut(m)

        def _f(i):
            return self._g(X[i + 1], self.k[i].e, self.k[i].n)

        y = map(_f, range(len(X) - 1))
        y = list(y)

        def _g(x, i):
            return self._E(x ^ y[i])

        r = functools.reduce(_g, range(self.n), X[0])
        return r == X[0]

    def _permut(self, m):
        msg = m.encode("utf-8")
        self.p = int(hashlib.sha1(msg).hexdigest(), 16)

    def _E(self, x):
        msg = f"{x}{self.p}".encode("utf-8")
        return int(hashlib.sha1(msg).hexdigest(), 16)

    def _g(self, x, e, n):
        q, r = divmod(x, n)
        if ((q + 1) * n) <= ((1 << self.l) - 1):
            result = q * n + pow(r, e, n)
        else:
            result = x
        return result
```

To sign and verify 2 messages in a ring of 4 users:

```mw
size = 4
msg1, msg2 = "hello", "world!"

def _rn(_):
    return Crypto.PublicKey.RSA.generate(1024, os.urandom)

key = map(_rn, range(size))
key = list(key)

r = Ring(key)

for i in range(size):
    signature_1 = r.sign_message(msg1, i)
    signature_2 = r.sign_message(msg2, i)
    assert r.verify_message(msg1, signature_1) and r.verify_message(msg2, signature_2) and not r.verify_message(msg1, signature_2)
```

## Cryptocurrencies

Monero and several other cryptocurrencies use this technology.
