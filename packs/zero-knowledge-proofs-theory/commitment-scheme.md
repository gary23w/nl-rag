---
title: "Commitment scheme"
source: https://en.wikipedia.org/wiki/Commitment_scheme
domain: zero-knowledge-proofs-theory
license: CC-BY-SA-4.0
tags: zero knowledge proof, soundness property, completeness property, sigma protocol
fetched: 2026-07-02
---

# Commitment scheme

A **commitment scheme** is a cryptographic primitive that allows one to commit to a chosen value (or chosen statement) while keeping it hidden to others, with the ability to reveal the committed value later. Commitment schemes are designed so that a party cannot change the value or statement after they have committed to it: that is, commitment schemes are *binding*. Commitment schemes have important applications in a number of cryptographic protocols including secure coin flipping, zero-knowledge proofs, and secure computation.

A way to visualize a commitment scheme is to think of a sender as putting a message in a locked box, and giving the box to a receiver. The message in the box is hidden from the receiver, who cannot open the lock themselves. Since the receiver has the box, the message inside cannot be changed—merely revealed if the sender chooses to give them the key at some later time.

Interactions in a commitment scheme take place in two phases:

1. the *commit phase* during which a value is chosen and committed to
2. the *reveal phase* during which the value is revealed by the sender, then the receiver verifies its authenticity

In the above metaphor, the commit phase is the sender putting the message in the box, and locking it. The reveal phase is the sender giving the key to the receiver, who uses it to open the box and verify its contents. The locked box is the commitment, and the key is the proof.

In simple protocols, the commit phase consists of a single message from the sender to the receiver. This message is called *the commitment*. It is essential that the specific value chosen cannot be extracted from the message by the receiver at that time (this is called the *hiding* property). A simple reveal phase would consist of a single message, *the opening*, from the sender to the receiver, followed by a check performed by the receiver. The value chosen during the commit phase must be the only one that the sender can compute and that validates during the reveal phase (this is called the *binding* property).

The concept of commitment schemes was perhaps first formalized by Gilles Brassard, David Chaum, and Claude Crépeau in 1988, as part of various zero-knowledge protocols for NP, based on various types of commitment schemes. But the concept was used prior to that without being treated formally. The notion of commitments appeared earliest in works by Manuel Blum, Shimon Even, and Adi Shamir et al. The terminology seems to have been originated by Blum, although commitment schemes can be interchangeably called **bit commitment schemes**—sometimes reserved for the special case where the committed value is a bit. Prior to that, commitment via one-way hash functions was considered, e.g., as part of, say, Lamport signature, the original one-time one-bit signature scheme.

## Applications

### Coin flipping

Suppose Alice and Bob want to resolve some dispute via coin flipping. If they are physically in the same place, a typical procedure might be:

1. Alice "calls" the coin flip,
2. Bob flips the coin,
3. If Alice's call is correct, she wins, otherwise Bob wins.

If Alice and Bob are not in the same place a problem arises. Once Alice has "called" the coin flip, Bob can stipulate the flip "results" to be whatever is most desirable for him. Similarly, if Alice doesn't announce her "call" to Bob, after Bob flips the coin and announces the result, Alice can report that she called whatever result is most desirable for her. Alice and Bob can use commitments in a procedure that will allow both to trust the outcome:

1. Alice "calls" the coin flip but only tells Bob a *commitment* to her call,
2. Bob flips the coin and reports the result,
3. Alice reveals what she committed to,
4. Bob verifies that Alice's call matches her commitment,
5. If Alice's revelation matches the coin result Bob reported, Alice wins.

For Bob to be able to skew the results to his favor, he must be able to understand the call hidden in Alice's commitment. If the commitment scheme is a good one, Bob cannot skew the results. Similarly, Alice cannot affect the result if she cannot change the value she commits to.

A real-life application of this problem exists, when people (often in media) commit to a decision or give an answer in a "sealed envelope", which is then opened later. "Let's find out if that's what the candidate answered", for example on a game show, can serve as a model of this system.

### Zero-knowledge proofs

One particular motivating example is the use of commitment schemes in zero-knowledge proofs. Commitments are used in zero-knowledge proofs for two main purposes: first, to allow the prover to participate in "cut and choose" proofs where the verifier will be presented with a choice of what to learn, and the prover will reveal only what corresponds to the verifier's choice. Commitment schemes allow the prover to specify all the information in advance, and only reveal what should be revealed later in the proof. Second, commitments are also used in zero-knowledge proofs by the verifier, who will often specify their choices ahead of time in a commitment. This allows zero-knowledge proofs to be composed in parallel without revealing additional information to the prover.

### Signature schemes

The Lamport signature scheme is a digital signature system that relies on maintaining two sets of secret data packets, publishing verifiable hashes of the data packets, and then selectively revealing partial secret data packets in a manner that conforms specifically to the data to be signed. In this way, the prior public commitment to the secret values becomes a critical part of the functioning of the system.

Because the Lamport signature system cannot be used more than once, a system to combine many Lamport key-sets under a single public value that can be tied to a person and verified by others was developed. This system uses trees of hashes to compress many published Lamport-key-commitment sets into a single hash value that can be associated with the prospective author of later-verified data.

### Verifiable secret sharing

Another important application of commitments is in verifiable secret sharing, a critical building block of secure multiparty computation. In a secret sharing scheme, each of several parties receive "shares" of a value that is meant to be hidden from everyone. If enough parties get together, their shares can be used to reconstruct the secret, but even a malicious cabal of insufficient size should learn nothing. Secret sharing is at the root of many protocols for secure computation: in order to securely compute a function of some shared input, the secret shares are manipulated instead. However, if shares are to be generated by malicious parties, it may be important that those shares can be checked for correctness. In a verifiable secret sharing scheme, the distribution of a secret is accompanied by commitments to the individual shares. The commitments reveal nothing that can help a dishonest cabal, but the shares allow each individual party to check to see if their shares are correct.

## Security

Formal definitions of commitment schemes vary strongly in notation and in flavour. The first such flavour is whether the commitment scheme provides perfect or computational security with respect to the hiding or binding properties. Another such flavour is whether the commitment is interactive, i.e. whether both the commit phase and the reveal phase can be seen as being executed by a cryptographic protocol or whether they are non-interactive, consisting of two algorithms *Commit* and *CheckReveal*. In the latter case *CheckReveal* can often be seen as a derandomised version of *Commit*, with the randomness used by *Commit* constituting the opening information.

If the commitment *C* to a value *x* is computed as *C:=Commit(x,open)* with *open* being the randomness used for computing the commitment, then *CheckReveal (C,x,open)* reduces to simply verifying the equation *C=Commit (x,open)*.

Using this notation and some knowledge about mathematical functions and probability theory we formalise different versions of the binding and hiding properties of commitments. The two most important combinations of these properties are perfectly binding and computationally hiding commitment schemes and computationally binding and perfectly hiding commitment schemes. Note that no commitment scheme can be at the same time perfectly binding and perfectly hiding – a computationally unbounded adversary can simply generate *Commit(x,open)* for every value of *x* and *open* until finding a pair that outputs *C*, and in a perfectly binding scheme this uniquely identifies *x*.

### Computational binding

Let *open* be chosen from a set of size $2^{k}$ , i.e., it can be represented as a *k* bit string, and let ${\text{Commit}}_{k}$ be the corresponding commitment scheme. As the size of *k* determines the security of the commitment scheme it is called the security parameter.

Then for all non-uniform probabilistic polynomial time algorithms that output $x,x'$ and $open,open'$ of increasing length *k*, the probability that $x\neq x'$ and ${\text{Commit}}_{k}(x,open)={\text{Commit}}_{k}(x',open')$ is a negligible function in *k*.

This is a form of asymptotic analysis. It is also possible to state the same requirement using concrete security: A commitment scheme *Commit* is $(t,\epsilon )$ secure, if for all algorithms that run in time *t* and output $x,x',open,open'$ the probability that $x\neq x'$ and ${\text{Commit}}(x,open)={\text{Commit}}(x',open')$ is at most $\epsilon$ .

### Perfect, statistical, and computational hiding

Let $U_{k}$ be the uniform distribution over the $2^{k}$ opening values for security parameter *k*. A commitment scheme is respectively perfect, statistical, or computational hiding, if for all $x\neq x'$ the probability ensembles $\{{\text{Commit}}_{k}(x,U_{k})\}_{k\in \mathbb {N} }$ and $\{{\text{Commit}}_{k}(x',U_{k})\}_{k\in \mathbb {N} }$ are equal, statistically close, or computationally indistinguishable.

### Impossibility of universally composable commitment schemes

It is impossible to realize commitment schemes in the universal composability (UC) framework. The reason is that UC commitment has to be *extractable*, as shown by Canetti and Fischlin and explained below.

The ideal commitment functionality, denoted here by *F*, works roughly as follows. Committer *C* sends value *m* to *F*, which stores it and sends "receipt" to receiver *R*. Later, *C* sends "open" to *F*, which sends *m* to *R*.

Now, assume we have a protocol *π* that realizes this functionality. Suppose that the committer *C* is corrupted. In the UC framework, that essentially means that *C* is now controlled by the environment, which attempts to distinguish protocol execution from the ideal process. Consider an environment that chooses a message *m* and then tells *C* to act as prescribed by *π*, as if it has committed to *m*. Note here that in order to realize *F*, the receiver must, after receiving a commitment, output a message "receipt". After the environment sees this message, it tells *C* to open the commitment.

The protocol is only secure if this scenario is indistinguishable from the ideal case, where the functionality interacts with a simulator *S*. Here, *S* has control of *C*. In particular, whenever *R* outputs "receipt", *F* has to do likewise. The only way to do that is for *S* to tell *C* to send a value to *F*. However, note that by this point, *m* is not known to *S*. Hence, when the commitment is opened during protocol execution, it is unlikely that *F* will open to *m*, unless *S* can extract *m* from the messages it received from the environment before *R* outputs the receipt.

However a protocol that is extractable in this sense cannot be statistically hiding. Suppose such a simulator *S* exists. Now consider an environment that, instead of corrupting *C*, corrupts *R* instead. Additionally it runs a copy of *S*. Messages received from *C* are fed into *S*, and replies from *S* are forwarded to *C*.

The environment initially tells *C* to commit to a message *m*. At some point in the interaction, *S* will commit to a value *m′*. This message is handed to *R*, who outputs *m′*. Note that by assumption we have *m' = m* with high probability. Now in the ideal process the simulator has to come up with *m*. But this is impossible, because at this point the commitment has not been opened yet, so the only message *R* can have received in the ideal process is a "receipt" message. We thus have a contradiction.

## Construction

A commitment scheme can either be perfectly binding (it is impossible for Alice to alter her commitment after she has made it, even if she has unbounded computational resources); or perfectly concealing (it is impossible for Bob to find out the commitment without Alice revealing it, even if he has unbounded computational resources); or formulated as an instance-dependent commitment scheme, which is either hiding or binding depending on the solution to another problem. A commitment scheme cannot be both perfectly hiding and perfectly binding at the same time.

### Bit-commitment in the random oracle model

Bit-commitment schemes are trivial to construct in the random oracle model. Given a hash function H with a 3*k* bit output, to commit the *k*-bit message *m*, Alice generates a random *k* bit string *R* and sends Bob H(*R* || *m*). The probability that any *R′*, *m′* exist where *m′* ≠ *m* such that H(*R′* || *m′*) = H(*R* || *m*) is ≈ 2−*k*, but to test any guess at the message *m* Bob will need to make 2*k* (for an incorrect guess) or 2*k*-1 (on average, for a correct guess) queries to the random oracle. We note that earlier schemes based on hash functions, essentially can be thought of schemes based on idealization of these hash functions as random oracle.

### Bit-commitment from any one-way permutation

One can create a bit-commitment scheme from any one-way function that is injective. The scheme relies on the fact that every one-way function can be modified (via the Goldreich-Levin theorem) to possess a computationally hard-core predicate (while retaining the injective property).

Let *f* be an injective one-way function, with *h* a hard-core predicate. Then to commit to a bit *b* Alice picks a random input *x* and sends the triple

$(h,f(x),b\oplus h(x))$

to Bob, where $\oplus$ denotes XOR, *i.e.*, bitwise addition modulo 2. To decommit, Alice simply sends *x* to Bob. Bob verifies by computing *f*(*x*) and comparing to the committed value. This scheme is concealing because for Bob to recover *b* he must recover *h*(*x*). Since *h* is a computationally hard-core predicate, recovering *h*(*x*) from *f*(*x*) with probability greater than one-half is as hard as inverting *f*. Perfect binding follows from the fact that *f* is injective and thus *f*(*x*) has exactly one preimage.

### Bit-commitment from a pseudo-random generator

Note that since we do not know how to construct a one-way permutation from any one-way function, this section reduces the strength of the cryptographic assumption necessary to construct a bit-commitment protocol.

In 1991 Moni Naor showed how to create a bit-commitment scheme from a cryptographically secure pseudorandom number generator. The construction is as follows. If *G* is a pseudo-random generator such that *G* takes *n* bits to 3*n* bits, then if Alice wants to commit to a bit *b*:

- Bob selects a random 3*n*-bit vector *R* and sends *R* to Alice.
- Alice selects a random *n*-bit vector *Y* and computes the 3*n*-bit vector *G*(*Y*).
- If *b*=1 Alice sends *G*(*Y*) to Bob, otherwise she sends the bitwise exclusive-or of *G*(*Y*) and *R* to Bob.

To decommit Alice sends *Y* to Bob, who can then check whether he initially received *G*(*Y*) or *G*(*Y*) $\oplus$ *R*.

This scheme is statistically binding, meaning that even if Alice is computationally unbounded she cannot cheat with probability greater than 2−*n*. For Alice to cheat, she would need to find a *Y'*, such that *G*(*Y'*) = *G*(*Y*) $\oplus$ *R*. If she could find such a value, she could decommit by sending the truth and *Y*, or send the opposite answer and *Y'*. However, *G*(*Y*) and *G*(*Y'*) are only able to produce 2*n* possible values each (that's 22*n*) while *R* is picked out of 23*n* values. She does not pick *R*, so there is a 22*n*/23*n* = 2−*n* probability that a *Y'* satisfying the equation required to cheat will exist.

The concealing property follows from a standard reduction, if Bob can tell whether Alice committed to a zero or one, he can also distinguish the output of the pseudo-random generator *G* from true-random, which contradicts the cryptographic security of *G*.

### A perfectly binding scheme based on the discrete log problem and beyond

Alice chooses a group of prime order *p*, with generator *g*.

Alice randomly picks a secret value *x* from *0* to *p* − 1 to commit to and calculates *c* = *g**x* and publishes *c*. The discrete logarithm problem dictates that from *c*, it is computationally infeasible to compute *x*, so under this assumption, Bob cannot compute *x*. On the other hand, Alice cannot compute a *x′* <> *x*, such that *g**x′* = *c*, so the scheme is binding.

This scheme isn't perfectly concealing as someone could find the commitment if he manages to solve the discrete logarithm problem. In fact, this scheme isn't hiding at all with respect to the standard hiding game, where an adversary should be unable to guess which of two messages he chose were committed to - similar to the IND-CPA game. One consequence of this is that if the space of possible values of *x* is small, then an attacker could simply try them all and the commitment would not be hiding.

A better example of a perfectly binding commitment scheme is one where the commitment is the encryption of *x* under a semantically secure, public-key encryption scheme with perfect completeness, and the decommitment is the string of random bits used to encrypt *x*. An example of an information-theoretically hiding commitment scheme is the Pedersen commitment scheme, which is computationally binding under the discrete logarithm assumption. Additionally to the scheme above, it uses another generator *h* of the prime group and a random number *r*. The commitment is set $c=g^{x}h^{r}$ .

These constructions are tightly related to and based on the algebraic properties of the underlying groups, and the notion originally seemed to be very much related to the algebra. However, it was shown that basing statistically binding commitment schemes on general unstructured assumption is possible, via the notion of interactive hashing for commitments from general complexity assumptions (specifically and originally, based on any one way permutation) as in.

### A perfectly hiding commitment scheme based on RSA

Alice selects N such that $N=p\cdot q$ , where p and q are large secret prime numbers. Additionally, she selects a prime e such that $e>N^{2}$ and $gcd(e,\phi (N^{2}))=1$ . Alice then computes a public number $g_{m}$ as an element of maximum order in the $\mathbb {Z} _{N^{2}}^{*}$ group. Finally, Alice commits to her secret m by first generating a random number r from $\mathbb {Z} _{N^{2}}^{*}$ and then by computing $c=m^{e}g_{m}^{r}$ .

The security of the above commitment relies on the hardness of the RSA problem and has perfect hiding and computational binding.

### Additive and multiplicative homomorphic properties of commitments

The Pedersen commitment scheme introduces an interesting homomorphic property that allows performing addition between two commitments. More specifically, given two messages $m_{1}$ and $m_{2}$ and randomness $r_{1}$ and $r_{2}$ , respectively, it is possible to generate a new commitment such that: $C(m_{1},r_{1})\cdot C(m_{2},r_{2})=C(m_{1}+m_{2},r_{1}+r_{2})$ . Formally:

$C(m_{1},r_{1})\cdot C(m_{2},r_{2})=g^{m_{1}}h^{r_{1}}\cdot g^{m_{2}}h^{r_{2}}=g^{m_{1}+m_{2}}h^{r_{1}+r_{2}}=C(m_{1}+m_{2},r_{1}+r_{2})$

To open the above Pedersen commitment to a new message $m_{1}+m_{2}$ , the randomness $r_{1}$ and $r_{2}$ has to be added.

Similarly, the RSA-based commitment mentioned above has a homomorphic property with respect to the multiplication operation. Given two messages $m_{1}$ and $m_{2}$ with randomness $r_{1}$ and $r_{2}$ , respectively, one can compute: $C(m_{1},r_{1})\cdot C(m_{2},r_{2})=C(m_{1}\cdot m_{2},r_{1}+r_{2})$ . Formally: $C(m_{1},r_{1})\cdot C(m_{2},r_{2})=m_{1}^{e}g_{m}^{r_{1}}\cdot m_{2}^{e}g_{m}^{r_{2}}=(m_{1}\cdot m_{2})^{e}g_{m}^{r_{1}+r_{2}}=C(m_{1}\cdot m_{2},r_{1}+r_{2})$ .

To open the above commitment to a new message $m_{1}\cdot m_{2}$ , the randomness $r_{1}$ and $r_{2}$ has to be added. This newly generated commitment is distributed similarly to a new commitment to $m_{1}\cdot m_{2}$ .

## Partial reveal

Some commitment schemes permit a proof to be given of only a portion of the committed value. In these schemes, the secret value X is a vector of many individually separable values.

$X=(x_{1},x_{2},...,x_{n})$

The commitment C is computed from X in the commit phase. Normally, in the reveal phase, the prover would reveal all of X and some additional proof data (such as R in simple bit-commitment). Instead, the prover is able to reveal any single value from the X vector, and create an efficient proof that it is the authentic i th element of the original vector that created the commitment C . The proof does not require any values of X other than $x_{i}$ to be revealed, and it is impossible to create valid proofs that reveal different values for any of the $x_{i}$ than the true one.

### Vector hashing

Vector hashing is a naive vector commitment partial reveal scheme based on bit-commitment. Values $m_{1},m_{2},...m_{n}$ are chosen randomly. Individual commitments are created by hashing $y_{1}=H(x_{1}||m_{1}),y_{2}=H(x_{2}||m_{2}),...$ . The overall commitment is computed as

$C=H(y_{1}||y_{2}||...||y_{n})$

In order to prove one element of the vector X , the prover reveals the values

$(i,y_{1},y_{2},...,y_{i-1},x_{i},m_{i},y_{i+1},...,y_{n})$

The verifier is able to compute $y_{i}$ from $x_{i}$ and $m_{i}$ , and then is able to verify that the hash of all y values is the commitment C . Unfortunately the proof is $O(n)$ in size and verification time. Alternately, if C is the set of all y values, then the commitment is $O(n)$ in size, and the proof is $O(1)$ in size and verification time. Either way, the commitment or the proof scales with $O(n)$ which is not optimal.

### Merkle tree

A common example of a practical partial reveal scheme is a Merkle tree, in which a binary hash tree is created of the elements of X . This scheme creates commitments that are $O(1)$ in size, and proofs that are $O(\log _{2}{n})$ in size and verification time. The root hash of the tree is the commitment C . To prove that a revealed $x_{i}$ is part of the original tree, only $\log _{2}{n}$ hash values from the tree, one from each level, must be revealed as the proof. The verifier is able to follow the path from the claimed leaf node all the way up to the root, hashing in the sibling nodes at each level, and eventually arriving at a root node value that must equal C .

### KZG commitment

A Kate–Zaverucha–Goldberg (KZG) commitment uses pairing-based cryptography to build a partial reveal scheme with $O(1)$ commitment sizes, proof sizes, and proof verification time. In other words, as n , the number of values in X , increases, the commitments and proofs do not get larger, and the proofs do not take any more effort to verify.

A KZG commitment requires a predetermined set of parameters to create a pairing, and a trusted trapdoor element. For example, a Tate pairing can be used. Assume that $\mathbb {G} _{1},\mathbb {G} _{2}$ are the additive groups, and $\mathbb {G} _{T}$ is the multiplicative group of the pairing. In other words, the pairing is the map $e:\mathbb {G} _{1}\times \mathbb {G} _{2}\rightarrow \mathbb {G} _{T}$ . Let $t\in \mathbb {F} _{p}$ be the trapdoor element (if p is the prime order of $\mathbb {G} _{1}$ and $\mathbb {G} _{2}$ ), and let G and H be the generators of $\mathbb {G} _{1}$ and $\mathbb {G} _{2}$ respectively. As part of the parameter setup, we assume that $G\cdot t^{i}$ and $H\cdot t^{i}$ are known and shared values for arbitrarily many positive integer values of i , while the trapdoor value t itself is discarded and known to no one.

#### Commit

A KZG commitment reformulates the vector of values to be committed as a polynomial. First, we calculate a polynomial such that $p(i)=x_{i}$ for all values of $x_{i}$ in our vector. Lagrange interpolation allows us to compute that polynomial

$p(x)=\sum _{i=0}^{n-1}x_{i}\prod _{0\leq j<n,j\neq i}{\frac {x-j}{i-j}}$

Under this formulation, the polynomial now encodes the vector, where $p(0)=x_{0},p(1)=x_{1},...$ . Let $p_{0},p_{1},...,p_{n-1}$ be the coefficients of p , such that ${\textstyle p(x)=\sum _{i=0}^{n-1}p_{i}x^{i}}$ . The commitment is calculated as

$C=\sum _{i=0}^{n-1}p_{i}Gt^{i}$

This is computed simply as a dot product between the predetermined values $G\cdot t^{i}$ and the polynomial coefficients $p_{i}$ . Since $\mathbb {G} _{1}$ is an additive group with associativity and commutativity, C is equal to simply $G\cdot p(t)$ , since all the additions and multiplications with G can be distributed out of the evaluation. Since the trapdoor value t is unknown, the commitment C is essentially the polynomial evaluated at a number known to no one, with the outcome obfuscated into an opaque element of $\mathbb {G} _{1}$ .

#### Reveal

A KZG proof must demonstrate that the revealed data is the authentic value of $x_{i}$ when C was computed. Let $y=x_{i}$ , the revealed value we must prove. Since the vector of $x_{i}$ was reformulated into a polynomial, we really need to prove that the polynomial p , when evaluated at i , takes on the value y . Simply, we just need to prove that $p(i)=y$ . We will do this by demonstrating that subtracting y from p yields a root at i . Define the polynomial q as

$q(x)={\frac {p(x)-y}{x-i}}$

This polynomial is itself the proof that $p(i)=y$ , because if q exists, then $p(x)-y$ is divisible by $x-i$ , meaning it has a root at i , so $p(i)-y=0$ (or, in other words, $p(i)=y$ ). The KZG proof will demonstrate that q exists and has this property.

The prover computes q through the above polynomial division, then calculates the KZG proof value $\pi$

$\pi =\sum _{i=0}^{n-1}q_{i}Gt^{i}$

This is equal to $G\cdot q(t)$ , as above. In other words, the proof value is the polynomial q again evaluated at the trapdoor value t , hidden in the generator G of $\mathbb {G} _{1}$ .

This computation is only possible if the above polynomials were evenly divisible, because in that case the quotient q is a polynomial, not a rational function. Due to the construction of the trapdoor, it is not possible to evaluate a rational function at the trapdoor value, only to evaluate a polynomial using linear combinations of the precomputed known constants of $G\cdot t^{i}$ . This is why it is impossible to create a proof for an incorrect value of $x_{i}$ .

#### Verify

To verify the proof, the bilinear map of the pairing is used to show that the proof value $\pi$ summarizes a real polynomial q that demonstrates the desired property, which is that $p(x)-y$ was evenly divided by $x-i$ . The verification computation checks the equality

$e(\pi ,H\cdot t-H\cdot i)\ {\stackrel {?}{=}}\ e(C-G\cdot y,H)$

where e is the bilinear map function as above. $H\cdot t$ is a precomputed constant, $H\cdot i$ is computed based on i .

By rewriting the computation in the pairing group $\mathbb {G} _{T}$ , substituting in $\pi =q(t)\cdot G$ and $C=p(t)\cdot G$ , and letting $\tau (x)=e(G,H)^{x}$ be a helper function for lifting into the pairing group, the proof verification is more clear.

$e(\pi ,H\cdot t-H\cdot i)=e(C-G\cdot y,H)$

$e(G\cdot q(t),H\cdot t-H\cdot i)=e(G\cdot p(t)-G\cdot y,H)$

$e(G\cdot q(t),H\cdot (t-i))=e(G\cdot (p(t)-y),H)$

$e(G,H)^{q(t)\cdot (t-i)}=e(G,H)^{p(t)-y}$

$\tau (q(t)\cdot (t-i))=\tau (p(t)-y)$

Assuming that the bilinear map is validly constructed, this demonstrates that $q(x)(x-i)=p(x)-y$ , without the validator knowing what p or q are. The validator can be assured of this because if $\tau (q(t)\cdot (t-i))=\tau (p(t)-y)$ , then the polynomials evaluate to the same output at the trapdoor value $x=t$ . This demonstrates the polynomials are identical, because, if the parameters were validly constructed, the trapdoor value is known to no one, meaning that engineering a polynomial to have a specific value at the trapdoor is impossible (according to the Schwartz–Zippel lemma). If $q(x)(x-i)=p(x)-y$ is now verified to be true, then q is verified to exist, therefore $p(x)-y$ must be polynomial-divisible by $(x-i)$ , so $p(i)-y=0$ due to the factor theorem. This proves that the i th value of the committed vector must have equaled y , since that is the output of evaluating the committed polynomial at i .

Why the bilinear map pairing is used

The utility of the bilinear map pairing is to allow the multiplication of $q(x)$ by $x-i$ to happen securely. These values truly lie in $\mathbb {G} _{1}$ , where division is assumed to be computationally hard. For example, $\mathbb {G} _{1}$ might be an elliptic curve over a finite field, as is common in elliptic-curve cryptography. Then, the division assumption is called the elliptic curve discrete logarithm problem, and this assumption is also what guards the trapdoor value from being computed, making it also a foundation of KZG commitments. In that case, we want to check if $q(x)(x-i)=p(x)-y$ . This cannot be done without a pairing, because with values on the curve of $G\cdot q(x)$ and $G\cdot (x-i)$ , we cannot compute $G\cdot (q(x)(x-i))$ . That would violate the computational Diffie–Hellman assumption, a foundational assumption in elliptic-curve cryptography. We instead use a pairing to sidestep this problem. $q(x)$ is still multiplied by G to get $G\cdot q(x)$ , but the other side of the multiplication is done in the paired group $\mathbb {G} _{2}$ , so, $H\cdot (t-i)$ . We compute $e(G\cdot q(t),H\cdot (t-i))$ , which, due to the bilinearity of the map, is equal to $e(G,H)^{q(t)\cdot (t-i)}$ . In this output group $\mathbb {G} _{T}$ we still have the discrete logarithm problem, so even though we know that value and $e(G,H)$ , we cannot extract the exponent $q(t)\cdot (t-i)$ , preventing any contradiction with discrete logarithm earlier. This value can be compared to $e(G\cdot (p(t)-y),H)=e(G,H)^{p(t)-y}$ though, and if $e(G,H)^{q(t)\cdot (t-i)}=e(G,H)^{p(t)-y}$ we are able to conclude that $q(t)\cdot (t-i)=p(t)-y$ , without ever knowing what the actual value of t is, let alone $q(t)(t-i)$ .

Additionally, a KZG commitment can be extended to prove the values of any arbitrary k values of X (not just one value), with the proof size remaining $O(1)$ , but the proof verification time scales with $O(k)$ . The proof is the same, but instead of subtracting a constant y , we subtract a polynomial that causes multiple roots, at all the locations we want to prove, and instead of dividing by $x-i$ we divide by ${\textstyle \prod _{i}x-i}$ for those same locations.

## Quantum bit commitment

It is an interesting question in quantum cryptography if *unconditionally secure* bit commitment protocols exist on the quantum level, that is, protocols which are (at least asymptotically) binding and concealing even if there are no restrictions on the computational resources. One could hope that there might be a way to exploit the intrinsic properties of quantum mechanics, as in the protocols for unconditionally secure key distribution.

However, this is impossible, as Dominic Mayers showed in 1996 . Any such protocol can be reduced to a protocol where the system is in one of two pure states after the commitment phase, depending on the bit Alice wants to commit. If the protocol is unconditionally concealing, then Alice can unitarily transform these states into each other using the properties of the Schmidt decomposition, effectively defeating the binding property.

One subtle assumption of the proof is that the commit phase must be finished at some point in time. This leaves room for protocols that require a continuing information flow until the bit is unveiled or the protocol is cancelled, in which case it is not binding anymore. More generally, Mayers's proof applies only to protocols that exploit quantum physics but not special relativity. Kent has shown that there exist unconditionally secure protocols for bit commitment that exploit the principle of special relativity stating that information cannot travel faster than light.

## Commitments based on physical unclonable functions

Physical unclonable functions (PUFs) rely on the use of a physical key with internal randomness, which is hard to clone or to emulate. Electronic, optical and other types of PUFs have been discussed extensively in the literature, in connection with their potential cryptographic applications including commitment schemes.
