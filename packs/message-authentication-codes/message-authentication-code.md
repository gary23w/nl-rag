---
title: "Message authentication code"
source: https://en.wikipedia.org/wiki/Message_authentication_code
domain: message-authentication-codes
license: CC-BY-SA-4.0
tags: message authentication code, hmac construction, keyed hash integrity, constant time comparison
fetched: 2026-07-02
---

# Message authentication code

In cryptography, a **message authentication code** (**MAC**), sometimes known as an **authentication tag**, is a short piece of information used for authenticating and integrity-checking a message. In other words, it is used to confirm that the message came from the stated sender (its authenticity) and has not been changed (its integrity). The MAC value allows verifiers (who also possess a secret key) to detect any changes to the message content.

## Terminology

The term **message integrity code** (**MIC**) is frequently substituted for the term *MAC*, especially in communications to distinguish it from the use of the latter as *Media Access Control* (as in *MAC address*). However, some authors use MIC to refer to a message digest, which aims only to uniquely but opaquely identify a single message. As such, it is recommended to avoid the term *message integrity code* (MIC), and instead use *checksum*, *error detection code*, *hash*, **keyed hash**, *message authentication code*, or *protected checksum*.

## Definitions

Informally, a message authentication code system consists of three algorithms:

- A key generation algorithm selects a key from the key space uniformly at random.
- A MAC generation algorithm efficiently returns a tag given the key and the message.
- A verifying algorithm efficiently verifies the authenticity of the message given the same key and the tag. That is, return *accepted* when the message and tag are not tampered with or forged, and otherwise return *rejected*.

A secure message authentication code must resist attempts by an adversary to forge tags, for arbitrary, selected, or all messages, including under conditions of known- or chosen-message. It should be computationally infeasible to compute a valid tag of the given message without knowledge of the key, even if for the worst case, we assume the adversary knows the tag of any message but the one in question.

Formally, a **message authentication code** (**MAC**) system is a triple of efficient algorithms (*G*, *S*, *V*) satisfying:

- *G* (key-generator) gives the key *k* on input 1*n*, where *n* is the security parameter.
- *S* (signing) outputs a tag *t* on the key *k* and the input string *x*.
- *V* (verifying) outputs *accepted* or *rejected* on inputs: the key *k*, the string *x* and the tag *t*.

*S* and *V* must satisfy the following:

Pr [

k

←

G

(1

n

),

V

(

k

,

x

,

S

(

k

,

x

) ) =

accepted

] = 1

.

A MAC is **unforgeable** if for every efficient adversary *A*

Pr [

k

←

G

(1

n

), (

x

,

t

) ←

A

S

(

k

, · )

(1

n

),

x

∉ Query(

A

S

(

k

, · )

, 1

n

),

V

(

k

,

x

,

t

) =

accepted

] < negl(

n

)

,

where *A**S*(*k*, · ) denotes that *A* has access to the oracle *S*(*k*, · ), and Query(*A**S*(*k*, · ), 1*n*) denotes the set of the queries on *S* made by *A*, which knows *n*. Clearly we require that any adversary cannot directly query the string *x* on *S*, since otherwise a valid tag can be easily obtained by that adversary.

## Security

While MAC functions are similar to cryptographic hash functions, they possess different security requirements. To be considered secure, a MAC function must resist existential forgery under chosen-message attacks. This means that even if an attacker has access to an oracle which possesses the secret key and generates MACs for messages of the attacker's choosing, the attacker cannot guess the MAC for other messages (which were not used to query the oracle) without performing infeasible amounts of computation.

MACs differ from digital signatures as MAC values are both generated and verified using the same secret key. This implies that the sender and receiver of a message must agree on the same key before initiating communications, as is the case with symmetric encryption. For the same reason, MACs do not provide the property of non-repudiation offered by signatures specifically in the case of a network-wide shared secret key: any user who can verify a MAC is also capable of generating MACs for other messages. In contrast, a digital signature is generated using the private key of a key pair, which is public-key cryptography. Since this private key is only accessible to its holder, a digital signature proves that a document was signed by none other than that holder. Thus, digital signatures do offer non-repudiation. However, non-repudiation can be provided by systems that securely bind key usage information to the MAC key; the same key is in the possession of two people, but one has a copy of the key that can be used for MAC generation while the other has a copy of the key in a hardware security module that only permits MAC verification. This is commonly done in the finance industry.

While the primary goal of a MAC is to prevent forgery by adversaries without knowledge of the secret key, this is insufficient in certain scenarios. When an adversary is able to control the MAC key, stronger guarantees are needed, akin to collision resistance or preimage security in hash functions. For MACs, these concepts are known as *commitment* and *context-discovery* security.

## Implementation

MAC algorithms can be constructed from other cryptographic primitives, like cryptographic hash functions (as in the case of HMAC) or from block cipher algorithms (OMAC, CCM, GCM, and PMAC). However many of the fastest MAC algorithms, like UMAC-VMAC and Poly1305-AES, are constructed based on universal hashing.

Intrinsically keyed hash algorithms such as SipHash are also by definition MACs; they can be even faster than universal-hashing based MACs.

Additionally, the MAC algorithm can deliberately combine two or more cryptographic primitives, so as to maintain protection even if one of them is later found to be vulnerable. For instance, in Transport Layer Security (TLS) versions before 1.2, the input data is split in halves that are each processed with a different hashing primitive (SHA-1 and SHA-2) then XORed together to output the MAC.

### One-time MAC

Universal hashing and in particular pairwise independent hash functions provide a secure message authentication code as long as the key is used at most once. This can be seen as the one-time pad for authentication.

The simplest such pairwise independent hash function is defined by the random key, *key* = (*a*, *b*), and the MAC tag for a message *m* is computed as *tag* = (*am* + *b*) mod *p*, where *p* is prime.

More generally, *k*-independent hashing functions provide a secure message authentication code as long as the key is used less than *k* times for *k*-ways independent hashing functions.

Message authentication codes and data origin authentication have been also discussed in the framework of quantum cryptography. By contrast to other cryptographic tasks, such as key distribution, for a rather broad class of quantum MACs it has been shown that quantum resources do not offer any advantage over unconditionally secure one-time classical MACs.

## Standards

Various standards exist that define MAC algorithms. These include:

- FIPS PUB 113 *Computer Data Authentication*, withdrawn in 2002, defines an algorithm based on DES.
- FIPS PUB 198-1 *The Keyed-Hash Message Authentication Code (HMAC)*
- NIST SP800-185 *SHA-3 Derived Functions: cSHAKE, KMAC, TupleHash, and ParallelHash*
- ISO/IEC 9797-1 *Mechanisms using a block cipher*
- ISO/IEC 9797-2 *Mechanisms using a dedicated hash-function*
- ISO/IEC 9797-3 *Mechanisms using a universal hash-function*
- ISO/IEC 29192-6 *Lightweight cryptography - Message authentication codes*

ISO/IEC 9797-1 and -2 define generic models and algorithms that can be used with any block cipher or hash function, and a variety of different parameters. These models and parameters allow more specific algorithms to be defined by nominating the parameters. For example, the FIPS PUB 113 algorithm is functionally equivalent to ISO/IEC 9797-1 MAC algorithm 1 with padding method 1 and a block cipher algorithm of DES.

## An example of MAC use

In this example, the sender of a message runs it through a MAC algorithm to produce a MAC data tag. The message and the MAC tag are then sent to the receiver. The receiver in turn runs the message portion of the transmission through the same MAC algorithm using the same key, producing a second MAC data tag. The receiver then compares the first MAC tag received in the transmission to the second generated MAC tag. If they are identical, the receiver can safely assume that the message was not altered or tampered with during transmission (data integrity).

However, to allow the receiver to be able to detect replay attacks, the message itself must contain data that assures that this same message can only be sent once (e.g. time stamp, sequence number or use of a one-time MAC). Otherwise an attacker could – without even understanding its content – record this message and play it back at a later time, producing the same result as the original sender.
