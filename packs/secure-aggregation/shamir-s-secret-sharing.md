---
title: "Shamir's secret sharing"
source: https://en.wikipedia.org/wiki/Shamir's_secret_sharing
domain: secure-aggregation
license: CC-BY-SA-4.0
tags: secure aggregation, secure multiparty computation, secret sharing scheme, federated aggregation, oblivious transfer
fetched: 2026-07-02
---

# Shamir's secret sharing

**Shamir's secret sharing** (SSS) is an efficient secret sharing algorithm for distributing private information (the "secret") among a group, first developed by Adi Shamir in 1979. The secret cannot be revealed unless a minimum number of the group's members act together to pool their knowledge. To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient number of shares are combined. SSS has the property of information-theoretic security, meaning that even if an attacker steals some shares, it is impossible for the attacker to reconstruct the secret unless they have stolen a sufficient number of shares.

Shamir's secret sharing is used in some applications to share the access keys to a master secret.

## High-level explanation

SSS is used to secure a secret in a distributed form, most often to secure encryption keys. The secret is split into multiple shares, which individually do not give any information about the secret.

To reconstruct a secret secured by SSS, a number of shares is needed, called the *threshold*. No information about the secret can be gained from any number of shares below the threshold (a property called perfect secrecy). In this sense, SSS is a generalisation of the one-time pad (which can be viewed as SSS with a two-share threshold and two shares in total).

### Application example

A company needs to secure their vault. If a *single* person knows the code to the vault, the code might be lost or unavailable when the vault needs to be opened. If there are *several* people who know the code, they may not trust each other to always act honestly.

SSS can be used in this situation to generate shares of the vault's code which are distributed to authorized individuals in the company. The minimum threshold and number of shares given to each individual can be selected such that the vault is accessible only by (groups of) authorized individuals. If fewer shares than the threshold are presented, the vault cannot be opened.

By accident, coercion or as an act of opposition, some individuals might present incorrect information for their shares. If the total of correct shares fails to meet the minimum threshold, the vault remains locked.

### Use cases

Shamir's secret sharing can be used to

- share a key for decrypting the root key of a password manager,
- recover a user key for encrypted email access,
- share the passphrase used to recreate a master secret, which is in turn used to access a cryptocurrency wallet and
- recover the combination to a physical safe.

## Properties and weaknesses

SSS has useful properties, but also weaknesses that means that it is unsuited to some uses.

Useful properties include:

1. **Secure**: The scheme has information-theoretic security.
2. **Minimal**: The size of each piece does not exceed the size of the original data.
3. **Extensible**: For any given threshold, shares can be dynamically added or deleted without affecting existing shares
4. **Dynamic**: Security can be enhanced without changing the secret, but by changing the polynomial occasionally (keeping the same free term) and constructing a new share for each of the participants.
5. **Flexible**: In organizations where hierarchy is important, each participant can be issued different numbers of shares according to their importance inside the organization. For instance, with a *threshold* of 3, the president could unlock the safe alone if given three shares, while three secretaries with one share each must combine their shares to unlock the safe.

Weaknesses include:

1. **No verifiable secret sharing**: During the share reassembly process, SSS does not provide a way to verify the correctness of each share being used. Verifiable secret sharing aims to verify that shareholders are honest and not submitting fake shares.
2. **Single point of failure**: The secret must exist in one place when it is split into shares, and again in one place when it is reassembled. These are attack points, and other schemes including multisignature eliminate at least one of these single points of failure.

## History

Adi Shamir first formulated the scheme in 1979.

## Mathematical principle

The scheme exploits the Lagrange interpolation theorem, specifically that k points on the polynomial uniquely determines a polynomial of degree less than or equal to $k-1$ . For instance, 2 points are sufficient to define a line, 3 points are sufficient to define a parabola, 4 points to define a cubic curve and so forth.

## Mathematical formulation

Shamir's secret sharing is an ideal and perfect $\left(k,n\right)$ -*threshold scheme* based on polynomial interpolation over finite fields. In such a scheme, the aim is to divide a secret S (for example, the combination to a safe) into n pieces of data $S_{1},\ldots ,S_{n}$ (known as *shares*) in such a way that:

1. Knowledge of any k or more shares $S_{i}$ makes S computable. That is, the entire secret S can be reconstructed from any combination of k shares.
2. Knowledge of any $k-1$ or fewer shares $S_{i}$ leaves S completely undetermined, in the sense that the possible values for S remain as likely with knowledge of up to $k-1$ shares as with knowledge of 0 shares. The secret S cannot be reconstructed with fewer than k shares.

If $n=k$ , then all of the shares are needed to reconstruct the secret S .

Assume that the secret S can be represented as an element $a_{0}$ of a finite field $\mathrm {GF} (q)$ (where q is greater than the number n of shares being generated). Randomly choose $k-1$ elements, $a_{1},\cdots ,a_{k-1}$ , from $\mathrm {GF} (q)$ and construct the polynomial $f\left(x\right)=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots +a_{k-1}x^{k-1}$ . Compute any n points out on the curve, for instance set $i=1,\ldots ,n$ to find points $\left(i,f\left(i\right)\right)$ . Every participant is given a point (a non-zero input to the polynomial, and the corresponding output). Given any subset of k of these pairs, $a_{0}$ can be obtained using interpolation, with one possible formula for doing so being $a_{0}=f(0)=\sum _{j=0}^{k-1}y_{j}\prod _{\begin{smallmatrix}m\,=\,0\\m\,\neq \,j\end{smallmatrix}}^{k-1}{\frac {x_{m}}{x_{m}-x_{j}}}$ , where the list of points on the polynomial is given as k pairs of the form $(x_{i},y_{i})$ . Note that $f(0)$ is equal to the first coefficient of polynomial $f(x)$ .

More generally, any value $f(\alpha )$ , where $\alpha \in \mathrm {GF} (q)$ , may be used as the secret instead of $f(0)$ . The leading coefficient $a_{k-1}$ may similarly be interpreted as the value $f(\infty )$ on the projective line and can also be used as the secret. These are precisely the polynomial-derived quantities that remain perfectly hidden from every coalition of fewer than k participants. In contrast, other linear combinations of the polynomial coefficients, including the intermediate coefficients, $a_{1},\ldots ,a_{k-2}$ , may be determined by some coalitions of fewer than k participants.

## Example calculation

The following example illustrates the basic idea. Note, however, that calculations in the example are done using integer arithmetic rather than using finite field arithmetic to make the idea easier to understand. Therefore, the example below does not provide perfect secrecy and is not a proper example of Shamir's scheme. The next example will explain the problem.

### Preparation

Suppose that the secret to be shared is 1234 $(S=1234)$ .

In this example, the secret will be split into 6 shares $(n=6)$ , where any subset of 3 shares $(k=3)$ is sufficient to reconstruct the secret. $k-1=2$ numbers are taken at random. Let them be 166 and 94.

This yields coefficients

$(a_{0}=1234;a_{1}=166;a_{2}=94),$

where

$a_{0}$

is the secret

The polynomial to produce secret shares (points) is therefore:

$f(x)=1234+166x+94x^{2}$

Six points $D_{x-1}=(x,f(x))$ from the polynomial are constructed as:

$D_{0}=(1,1494);D_{1}=(2,1942);D_{2}=(3,2578);D_{3}=(4,3402);D_{4}=(5,4414);D_{5}=(6,5614)$

Each participant in the scheme receives a different point (a pair of x and $f(x)$ ). Because $D_{x-1}$ is used instead of $D_{x}$ the points start from $(1,f(1))$ and not $(0,f(0))$ . This is necessary because $f(0)$ is the secret.

### Reconstruction

In order to reconstruct the secret, any 3 points are sufficient

Consider using the 3 points $\left(x_{0},y_{0}\right)=\left(2,1942\right);\left(x_{1},y_{1}\right)=\left(4,3402\right);\left(x_{2},y_{2}\right)=\left(5,4414\right)$ .

Computing the Lagrange basis polynomials:

$\ell _{0}(x)={\frac {x-x_{1}}{x_{0}-x_{1}}}\cdot {\frac {x-x_{2}}{x_{0}-x_{2}}}={\frac {x-4}{2-4}}\cdot {\frac {x-5}{2-5}}={\frac {1}{6}}x^{2}-{\frac {3}{2}}x+{\frac {10}{3}}$

$\ell _{1}(x)={\frac {x-x_{0}}{x_{1}-x_{0}}}\cdot {\frac {x-x_{2}}{x_{1}-x_{2}}}={\frac {x-2}{4-2}}\cdot {\frac {x-5}{4-5}}=-{\frac {1}{2}}x^{2}+{\frac {7}{2}}x-5$

$\ell _{2}(x)={\frac {x-x_{0}}{x_{2}-x_{0}}}\cdot {\frac {x-x_{1}}{x_{2}-x_{1}}}={\frac {x-2}{5-2}}\cdot {\frac {x-4}{5-4}}={\frac {1}{3}}x^{2}-2x+{\frac {8}{3}}$

Using the formula for polynomial interpolation, $f(x)$ is:

${\begin{aligned}f(x)&=\sum _{j=0}^{2}y_{j}\cdot \ell _{j}(x)\\[6pt]&=y_{0}\ell _{0}(x)+y_{1}\ell _{1}(x)+y_{2}\ell _{2}(x)\\[6pt]&=1942\left({\frac {1}{6}}x^{2}-{\frac {3}{2}}x+{\frac {10}{3}}\right)+3402\left(-{\frac {1}{2}}x^{2}+{\frac {7}{2}}x-5\right)+4414\left({\frac {1}{3}}x^{2}-2x+{\frac {8}{3}}\right)\\[6pt]&=1234+166x+94x^{2}\end{aligned}}$

Recalling that the secret is the free coefficient, which means that $S=1234$ , and the secret has been recovered.

### Computationally efficient approach

Using polynomial interpolation to find a coefficient in a source polynomial $S=f(0)$ using Lagrange polynomials is not efficient, since unused constants are calculated.

Considering this, an optimized formula to use Lagrange polynomials to find $f(0)$ is defined as follows:

$f(0)=\sum _{j=0}^{k-1}y_{j}\prod _{\begin{smallmatrix}m\,=\,0\\m\,\neq \,j\end{smallmatrix}}^{k-1}{\frac {x_{m}}{x_{m}-x_{j}}}$

### Problem of using integer arithmetic

Although the simplified version of the method demonstrated above, which uses integer arithmetic rather than finite field arithmetic, works, there is a security problem: Eve gains information about S with every $D_{i}$ that she finds.

Suppose that she finds the point $D=(2,1942)$ . She still does not have $k=3$ points, so in theory she should not have gained any more information about S . But she could combine the information from the point with the public information: $n=6,k=3,f(x)=a_{0}+a_{1}x+\cdots +a_{k-1}x^{k-1},a_{0}=S,a_{i}\in \mathbb {Z}$ . Doing so, Eve could perform the following algebra:

1. Fill the formula for $f(x)$ with S and the value of $k:f(x)=S+a_{1}x+\cdots +a_{k-1}x^{k-1}\Rightarrow {}f(x)=S+a_{1}x+a_{2}x^{2}$
2. Fill (1) with the values of D 's x and $f(x):1942=S+a_{1}2+a_{2}2^{2}\Rightarrow {}S=1942-2a_{1}-4a_{2}$

which leads her to the information that S is even.

### Solution using finite field arithmetic

The above attack exploits constraints on the values that the polynomial may take by virtue of how it was constructed: the polynomial must have coefficients that are integers, and the polynomial must take an integer as value when evaluated at each of the coordinates used in the scheme. This reduces its possible values at unknown points, including the resultant secret, given fewer than k shares.

This problem can be remedied by using finite field arithmetic. A finite field always has size $q=p^{r}$ , where p is a prime and r is a positive integer. The size q of the field must satisfy $q>n$ , and that q is greater than the number of possible values for the secret, though the latter condition may be circumvented by splitting the secret into smaller secret values, and applying the scheme to each of these. In our example below, we use a prime field (i.e. *r* = 1). The figure shows a polynomial curve over a finite field.

In practice this is only a small change. The order *q* of the field (i.e. the number of values that it has) must be chosen to be greater than the number of participants and the number of values that the secret $a_{0}=S$ may take. All calculations involving the polynomial must also be calculated over the field (mod *p* in our example, in which $p=q$ is taken to be a prime) instead of over the integers. Both the choice of the field and the mapping of the secret to a value in this field are considered to be publicly known.

For this example, choose $p=1613$ , so the polynomial becomes $f(x)=1234+166x+94x^{2}{\bmod {1613}}$ which gives the points: $(1,1494);(2,329);(3,965);(4,176);(5,1188);(6,775)$

This time Eve doesn't gain any information when she finds a $D_{x}$ (until she has k points).

Suppose again that Eve finds $D_{0}=\left(1,1494\right)$ and $D_{1}=\left(2,329\right)$ , and the public information is: $n=6,k=3,p=1613,f(x)=a_{0}+a_{1}x+\dots +a_{k-1}x^{k-1}\mod {p},a_{0}=S,a_{i}\in \mathbb {N}$ . Attempting the previous attack, Eve can:

1. Fill the $f(x)$ -formula with S and the value of k and p : $f(x)=S+a_{1}x+\dots +a_{3-1}x^{3-1}\mod 1613$
2. Fill (1) with the values of $D_{0}$ 's x and $f(x):1494\equiv S+a_{1}1+a_{2}1^{2}{\pmod {1613}}\Rightarrow {}1494\equiv S+a_{1}+a_{2}{\pmod {1613}}$
3. Fill (1) with the values of $D_{1}$ 's x and $f(x):1942\equiv S+a_{1}2+a_{2}2^{2}{\pmod {1613}}\Rightarrow {}1942\equiv S+2a_{1}+4a_{2}{\pmod {1613}}$
4. Subtract (3)-(2): $(1942-1494)\equiv (S-S)+(2a_{1}-a_{1})+(4a_{2}-a_{2}){\pmod {1613}}\Rightarrow {}448\equiv a_{1}+3a_{2}{\pmod {1613}}$ and rewrite this as $a_{1}\equiv 448-3a_{2}{\pmod {1613}}$

There are p possible values for $a_{1}$ . She knows that $[448,445,442,\ldots ]$ always decreases by 3, so if p were divisible by 3 she could conclude $a_{1}\in [1,4,7,\ldots ]$ . However, p is prime, so she can not conclude this. Thus, using a finite field avoids this possible attack.

Also, even though Eve can conclude that $S\equiv 1046+2a_{2}{\pmod {1613}}$ , it does not provide any additional information, since the "wrapping around" behavior of modular arithmetic prevents the leakage of "S is even", unlike the example with integer arithmetic above.

## Python code

For purposes of keeping the code clearer, a prime field is used here. In practice, for convenience a scheme constructed using a smaller binary field may be separately applied to small substrings of bits of the secret (e.g. GF(256) for byte-wise application, where GF is Galois Field), without loss of security. The strict condition that the size of the field must be larger than the number of shares must still be respected (e.g., if the number of shares could exceed 255, the field GF(256) might be replaced by say GF(65536)).

```mw
"""
The following Python implementation of Shamir's secret sharing is
released into the Public Domain under the terms of CC0 and OWFa:
https://creativecommons.org/publicdomain/zero/1.0/
http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0

See the bottom few lines for usage. Tested on Python 2 and 3.
"""

from __future__ import division
from __future__ import print_function

import random
import functools

# 12th Mersenne Prime
_PRIME = 2 ** 127 - 1

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(secret, minimum, shares, prime=_PRIME):
    """
    Generates a random shamir pool for a given secret, returns share points.
    """
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [secret] + [_RINT(prime - 1) for i in range(minimum - 1)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1). This can
    be computed via the extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain this, the result will be such that:
    den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (points (x,y) on the polynomial).
    """
    if len(shares) < 3:
        raise ValueError("need at least three shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s, prime)

def main():
    """Main function"""
    secret = 1234
    shares = make_random_shares(secret, minimum=3, shares=6)

    print('Secret:                                                     ',
          secret)
    print('Shares:')
    if shares:
        for share in shares:
            print('  ', share)

    print('Secret recovered from minimum subset of shares:             ',
          recover_secret(shares[:3]))
    print('Secret recovered from a different minimum subset of shares: ',
          recover_secret(shares[-3:]))

if __name__ == '__main__':
    main()
```
