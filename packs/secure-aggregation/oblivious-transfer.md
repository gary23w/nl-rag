---
title: "Oblivious transfer"
source: https://en.wikipedia.org/wiki/Oblivious_transfer
domain: secure-aggregation
license: CC-BY-SA-4.0
tags: secure aggregation, secure multiparty computation, secret sharing scheme, federated aggregation, oblivious transfer
fetched: 2026-07-02
---

# Oblivious transfer

In cryptography, an **oblivious transfer** (**OT**) protocol is a type of protocol in which a sender transfers one of potentially many pieces of information to a receiver, but remains oblivious as to what piece (if any) has been transferred.

The first form of oblivious transfer was introduced in 1981 by Michael O. Rabin. In this form, the sender sends a message to the receiver with probability 1/2, while the sender remains oblivious as to whether or not the receiver received the message. Rabin's oblivious transfer scheme is based on the RSA cryptosystem. A more useful form of oblivious transfer called **1–2 oblivious transfer** or "1 out of 2 oblivious transfer", was developed later by Shimon Even, Oded Goldreich, and Abraham Lempel, in order to build protocols for secure multiparty computation. It is generalized to "1 out of *n* oblivious transfer" where the user gets exactly one database element without the server getting to know which element was queried, and without the user knowing anything about the other elements that were not retrieved. The latter notion of oblivious transfer is a strengthening of private information retrieval, in which the database is not kept private.

Claude Crépeau showed that Rabin's oblivious transfer is equivalent to 1–2 oblivious transfer.

Further work has revealed oblivious transfer to be a fundamental and important problem in cryptography. It is considered one of the critical problems in the field, because of the importance of the applications that can be built based on it. In particular, it is complete for secure multiparty computation: that is, given an implementation of oblivious transfer it is possible to securely evaluate any polynomial time computable function without any additional primitive.

## Rabin's oblivious transfer protocol

In Rabin's oblivious transfer protocol, the sender generates an RSA public modulus *N*=*pq* where *p* and *q* are large prime numbers, and an exponent *e* relatively prime to *λ(N)* = (*p* − 1)(*q* − 1). The sender encrypts the message *m* as *m**e* mod *N*.

1. The sender sends *N*, *e*, and *m**e* mod *N* to the receiver.
2. The receiver picks a random *x* modulo *N* and sends *x*2 mod *N* to the sender. Note that gcd(*x*,*N*) = 1 with overwhelming probability, which ensures that there are 4 square roots of *x*2 mod *N*.
3. The sender finds a square root *y* of *x*2 mod *N* and sends *y* to the receiver.

If the receiver finds *y* is neither *x* nor −*x* modulo *N*, the receiver will be able to factor *N* and therefore decrypt *m**e* to recover *m* (see Rabin encryption for more details). However, if *y* is *x* or −*x* mod *N*, the receiver will have no information about *m* beyond the encryption of it. Since every quadratic residue modulo *N* has four square roots, the probability that the receiver learns *m* is 1/2.

## 1–2 oblivious transfer

In a 1–2 oblivious transfer protocol, Alice the sender has two messages *m*0 and *m*1, and wants to ensure that the receiver only learns one. Bob, the receiver, has a bit *b* and wishes to receive *m**b* without Alice learning *b*. The protocol of Even, Goldreich, and Lempel (which the authors attribute partially to Silvio Micali) is general, but can be instantiated using RSA encryption as follows.

| Alice (sender) |   | Bob (receiver) |   |   |   |   |
|---|---|---|---|---|---|---|
| Calculus | Secret | Public | Public | Secret | Calculus |   |
| Messages to be sent | $m_{0},m_{1}$ |   |   |   |   |   |
| Generate RSA key pair and send public portion to Bob | d | $N,e$ | $\Rightarrow$ | $N,e$ |   | Receive public key |
| Generate two random messages |   | $x_{0},x_{1}$ | $\Rightarrow$ | $x_{0},x_{1}$ |   | Receive random messages |
|   |   |   |   |   | $k,b$ | Choose $b\in \{0,1\}$ and generate random k |
|   |   | v | $\Leftarrow$ | $v=(x_{b}+k^{e}){\bmod {N}}$ |   | Compute the encryption of k , blind with $x_{b}$ and send to Alice |
| One of these will equal k , but Alice does not know which | ${\begin{aligned}k_{0}&=(v-x_{0})^{d}{\bmod {N}}\\k_{1}&=(v-x_{1})^{d}{\bmod {N}}\end{aligned}}$ |   |   |   |   |   |
| Send both messages to Bob |   | ${\begin{aligned}m'_{0}=(m_{0}+k_{0}){\bmod {N}}\\m'_{1}=(m_{1}+k_{1}){\bmod {N}}\end{aligned}}$ | $\Rightarrow$ | $m'_{0},m'_{1}$ |   | Receive both messages |
|   |   |   |   |   | $m_{b}=(m'_{b}-k){\bmod {N}}$ | Bob decrypts the $m'_{b}$ , since he knows which $x_{b}$ he selected earlier |

1. Alice has two messages, $m_{0},m_{1}$ , and wants to send exactly one of them to Bob. Bob does not want Alice to know which one he receives.
2. Alice generates an RSA key pair, comprising the modulus N , the public exponent e and the private exponent d .
3. She also generates two random values, $x_{0},x_{1}$ , and sends them to Bob along with her public modulus and exponent.
4. Bob picks b to be either 0 or 1 and selects $x_{b}$ .
5. Bob generates a random value k and uses it to blind $x_{b}$ by computing $v=(x_{b}+k^{e}){\bmod {N}}$ , which he sends to Alice.
6. Alice combines v with both of her random values to produce $k_{0}=(v-x_{0})^{d}{\bmod {N}}$ and $k_{1}=(v-x_{1})^{d}{\bmod {N}}$ . Now $k_{b}$ will be equal to $k,$ and the other will be a meaningless random value. However, since Alice does not know the value of b that Bob chose, she cannot determine which of $k_{0}$ and $k_{1}$ is equal to k .
7. She combines the two secret messages with each of the possible keys, $m'_{0}=(m_{0}+k_{0}){\bmod {N}}$ and $m'_{1}=(m_{1}+k_{1}){\bmod {N}}$ , and sends them both to Bob.
8. Bob knows k , so he is able to compute $m_{b}=(m'_{b}-k){\bmod {N}}$ . However, since he does not know d , he cannot compute $k_{1-b}=(v-x_{1-b})^{d}{\bmod {N}}$ and so cannot determine $(m_{1-b}){\bmod {N}}$ .

## 1-out-of-*n* oblivious transfer and *k*-out-of-*n* oblivious transfer

A 1-out-of-*n* oblivious transfer protocol can be defined as a natural generalization of a 1-out-of-2 oblivious transfer protocol. Specifically, a sender has *n* messages, and the receiver has an index *i*, and the receiver wishes to receive the *i*-th among the sender's messages, without the sender learning *i*, while the sender wants to ensure that the receiver receive only one of the *n* messages.

1-out-of-*n* oblivious transfer is incomparable to private information retrieval (PIR). On the one hand, 1-out-of-*n* oblivious transfer imposes an additional privacy requirement for the database: namely, that the receiver learn at most one of the database entries. On the other hand, PIR requires communication sublinear in *n*, whereas 1-out-of-*n* oblivious transfer has no such requirement. However, assuming single server PIR is a sufficient assumption in order to construct 1-out-of-2 Oblivious Transfer.

1-out-of-*n* oblivious transfer protocol with sublinear communication was first constructed (as a generalization of single-server PIR) by Eyal Kushilevitz and Rafail Ostrovsky. More efficient constructions were proposed by Moni Naor and Benny Pinkas, William Aiello, Yuval Ishai and Omer Reingold, Sven Laur and Helger Lipmaa. In 2017, Kolesnikov et al., proposed an efficient 1-n oblivious transfer protocol which requires roughly 4x the cost of 1-2 oblivious transfer in amortized setting.

Brassard, Crépeau and Robert further generalized this notion to *k*-*n* oblivious transfer, wherein the receiver obtains a set of *k* messages from the *n* message collection. The set of *k* messages may be received simultaneously ("non-adaptively"), or they may be requested consecutively, with each request based on previous messages received.

## Generalized oblivious transfer

*k*-*n* Oblivious transfer is a special case of generalized oblivious transfer, which was presented by Ishai and Kushilevitz. In that setting, the sender has a set *U* of *n* messages, and the transfer constraints are specified by a collection *A* of permissible subsets of *U*. The receiver may obtain any subset of the messages in *U* that appears in the collection *A*. The sender should remain oblivious of the selection made by the receiver, while the receiver cannot learn the value of the messages outside the subset of messages that he chose to obtain. The collection *A* is monotone decreasing, in the sense that it is closed under containment (i.e., if a given subset *B* is in the collection *A*, so are all of the subsets of *B*). The solution proposed by Ishai and Kushilevitz uses the parallel invocations of 1-2 oblivious transfer while making use of a special model of private protocols. Later on, other solutions that are based on secret sharing were published – one by Bhavani Shankar, Kannan Srinathan, and C. Pandu Rangan, and another by Tamir Tassa.

## Origins

In the early seventies Stephen Wiesner introduced a primitive called **multiplexing** in his seminal paper "Conjugate Coding", which was the starting point of quantum cryptography. Unfortunately it took more than ten years to be published. Even though this primitive was equivalent to what was later called *1–2 oblivious transfer*, Wiesner did not see its application to cryptography.

## Quantum oblivious transfer

Protocols for oblivious transfer can be implemented with quantum systems. In contrast to other tasks in quantum cryptography, like quantum key distribution, it has been shown that quantum oblivious transfer cannot be implemented with unconditional security, i.e. the security of quantum oblivious transfer protocols cannot be guaranteed only from the laws of quantum physics.
