---
title: "Decisional Diffie–Hellman assumption"
source: https://en.wikipedia.org/wiki/Decisional_Diffie%E2%80%93Hellman_assumption
domain: cryptographic-hardness
license: CC-BY-SA-4.0
tags: cryptographic hardness assumption, computational hardness, learning with errors, discrete logarithm assumption
fetched: 2026-07-02
---

# Decisional Diffie–Hellman assumption

The **decisional Diffie–Hellman (DDH) assumption** is a computational hardness assumption about a certain problem involving discrete logarithms in cyclic groups. It is used as the basis to prove the security of many cryptographic protocols, most notably the ElGamal and Cramer–Shoup cryptosystems.

## Definition

Consider a (multiplicative) cyclic group G of order q , and with generator g . The DDH assumption states that, given $g^{a}$ and $g^{b}$ for uniformly and independently chosen $a,b\in \mathbb {Z} _{q}$ , the value $g^{ab}$ "looks like" a random element in G .

This intuitive notion can be formally stated by saying that the following two probability distributions are computationally indistinguishable (in the security parameter, $n=\log(q)$ ):

- $(g^{a},g^{b},g^{ab})$ , where a and b are randomly and independently chosen from $\mathbb {Z} _{q}$ .
- $(g^{a},g^{b},g^{c})$ , where $a,b,c$ are randomly and independently chosen from $\mathbb {Z} _{q}$ .

Triples of the first kind are often called **DDH triplet** or **DDH tuples**.

## Relation to other assumptions

The DDH assumption is related to the discrete log assumption. If it were possible to efficiently compute discrete logs in G , then the DDH assumption would not hold in G . Given $(g^{a},g^{b},z)$ , one could efficiently decide whether $z=g^{ab}$ by first taking the discrete $\log _{g}$ of $g^{a}$ , and then comparing z with $(g^{b})^{a}$ .

DDH is considered to be a **stronger** assumption than the discrete logarithm assumption, because there are groups for which computing discrete logs is believed to be hard (and thus the DL Assumption is believed to be true), but detecting DDH tuples is easy (and thus DDH is false). Because of this, requiring that the DDH assumption holds in a group is believed to be a more restrictive requirement than DL.

The DDH assumption is also related to the computational Diffie–Hellman assumption (CDH). If it were possible to efficiently compute $g^{ab}$ from $(g^{a},g^{b})$ , then one could easily distinguish the two probability distributions above. CDH is considered to be a stronger assumption than DDH because if CDH is solved, which means we can get $g^{ab}$ , the answer to DDH will become obvious.

## Other properties

The problem of detecting DDH tuples is random self-reducible, meaning, roughly, that if it is hard for even a small fraction of inputs, it is hard for almost all inputs; if it is easy for even a small fraction of inputs, it is easy for almost all inputs.

## Groups for which DDH is assumed to hold

When using a cryptographic protocol whose security depends on the DDH assumption, it is important that the protocol is implemented using groups where DDH is believed to hold:

- The subgroup $\mathbb {G} _{q}$ of k -th residues modulo a prime $p=kq+1$ , where q is also a large prime (also called a Schnorr group). For the case of $k=2$ , this corresponds to the group of quadratic residues modulo a safe prime.
- The quotient group $\mathbb {Z} _{p}^{*}/\{1,-1\}$ for a safe prime $p=2q+1$ , which consists of the cosets $\{\{1,-1\},\ldots \{q,-q\}\}$ . These cosets $\{x,-x\}$ can be represented by x , which implies $\mathbb {Z} _{p}^{*}/\{1,-1\}\equiv \{1,\ldots ,q\}$ . Since $\mathbb {Z} _{p}^{*}/\{1,-1\}$ and $\mathbb {G} _{q}$ are isomorphic, and the isomorphism can be computed efficiently in both direction, DDH is equally hard in both groups.
- A prime-order elliptic curve E over the field $GF(p)$ , where p is prime, provided E has large embedding degree.
- A Jacobian of a hyper-elliptic curve over the field $GF(p)$ with a prime number of reduced divisors, where p is prime, provided the Jacobian has large embedding degree.

Importantly, the DDH assumption **does not hold** in the multiplicative group $\mathbb {Z} _{p}^{*}$ , where p is prime. This is because if g is a generator of $\mathbb {Z} _{p}^{*}$ , then the Legendre symbol of $g^{a}$ reveals if a is even or odd. Given $g^{a}$ , $g^{b}$ and $g^{ab}$ , one can thus efficiently compute and compare the least significant bit of a , b and $ab$ , respectively, which provides a probabilistic method to distinguish $g^{ab}$ from a random group element.

The DDH assumption does not hold on elliptic curves over $GF(p)$ with small embedding degree (say, less than $\log ^{2}(p)$ ), a class which includes supersingular elliptic curves. This is because the Weil pairing or Tate pairing can be used to solve the problem directly as follows: given $P,aP,bP,cP$ on such a curve, one can compute $e(P,cP)$ and $e(aP,bP)$ . By the bilinearity of the pairings, the two expressions are equal if and only if $ab=c$ modulo the order of P . If the embedding degree is large (say around the size of p ) then the DDH assumption will still hold because the pairing cannot be computed. Even if the embedding degree is small, there are some subgroups of the curve in which the DDH assumption is believed to hold.
