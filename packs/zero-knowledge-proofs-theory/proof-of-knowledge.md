---
title: "Proof of knowledge"
source: https://en.wikipedia.org/wiki/Proof_of_knowledge
domain: zero-knowledge-proofs-theory
license: CC-BY-SA-4.0
tags: zero knowledge proof, soundness property, completeness property, sigma protocol
fetched: 2026-07-02
---

# Proof of knowledge

In cryptography, a **proof of knowledge** is an interactive proof in which the prover succeeds in 'convincing' a verifier that the prover knows something. What it means for a machine to 'know something' is defined in terms of computation. A machine 'knows something', if this something can be computed, given the machine as an input. As the program of the prover does not necessarily spit out the knowledge itself (as is the case for zero-knowledge proofs), a machine with a different program, called the knowledge extractor is introduced to capture this idea. We are mostly interested in what can be proven by polynomial time bounded machines. In this case, the set of knowledge elements is limited to a set of witnesses of some language in NP.

Let x be a statement of language L in NP, and $W(x)$ the set of witnesses for x that should be accepted in the proof. This allows us to define the following relation: $R=\{(x,w):x\in L,w\in W(x)\}$ .

A proof of knowledge for relation R with knowledge error $\kappa$ is a two party protocol with a prover P and a verifier V with the following two properties:

1. **Completeness**: If $(x,w)\in R$ , then the prover P who knows witness w for x succeeds in convincing the verifier V of his knowledge. More formally: $\Pr(P(x,w)\leftrightarrow V(x)\rightarrow 1)=1$ , i.e. given the interaction between the prover P and the verifier V, the probability that the verifier is convinced is 1.
2. **Validity**: Validity requires that the success probability of a knowledge extractor E in extracting the witness, given oracle access to a possibly malicious prover ${\tilde {P}}$ , must be at least as high as the success probability of the prover ${\tilde {P}}$ in convincing the verifier. This property guarantees that no prover that doesn't know the witness can succeed in convincing the verifier.

## Details on the definition

This is a more rigorous definition of **Validity**:

Let R be a witness relation, $W(x)$ the set of all witnesses for public value x , and $\kappa$ the knowledge error. A proof of knowledge is $\kappa$ -valid if there exists a polynomial-time machine E , given oracle access to ${\tilde {P}}$ , such that for every ${\tilde {P}}$ , it is the case that $E^{{\tilde {P}}(x)}(x)\in W(x)\cup \{\bot \}$ and $\Pr(E^{{\tilde {P}}(x)}(x)\in W(x))\geq \Pr({\tilde {P}}(x)\leftrightarrow V(x)\rightarrow 1)-\kappa (x).$

The result $\bot$ signifies that the Turing machine E did not come to a conclusion.

The knowledge error $\kappa (x)$ denotes the probability that the verifier V might accept x , even though the prover does in fact not know a witness w . The knowledge extractor E is used to express what is meant by the knowledge of a Turing machine. If E can extract w from ${\tilde {P}}$ , we say that ${\tilde {P}}$ knows the value of w .

This definition of the validity property is a combination of the validity and strong validity properties. For small knowledge errors $\kappa (x)$ , such as e.g. $2^{-80}$ or $1/\mathrm {poly} (|x|)$ , it can be seen as being stronger than the **soundness** of ordinary interactive proofs.

## Relation to general interactive proofs

In order to define a specific proof of knowledge, one need not only define the language, but also the witnesses the verifier should know. In some cases proving membership in a language may be easy, while computing a specific witness may be hard. This is best explained using an example:

Let $\langle g\rangle$ be a cyclic group with generator g in which solving the discrete logarithm problem is believed to be hard. Deciding membership of the language $L=\{x\mid g^{w}=x\}$ is trivial, as every x is in $\langle g\rangle$ . However, finding the witness w such that $g^{w}=x$ holds corresponds to solving the discrete logarithm problem.

## Protocols

### Schnorr protocol

One of the simplest and frequently used proofs of knowledge, the *proof of knowledge of a discrete logarithm*, is due to Schnorr. The protocol is defined for a cyclic group $G_{q}$ of order q with generator g .

In order to prove knowledge of $x=\log _{g}y$ , the prover interacts with the verifier as follows:

1. In the first round the prover commits himself to randomness r ; therefore the first message $t=g^{r}$ is also called *commitment*.
2. The verifier replies with a *challenge* c chosen at random.
3. After receiving c , the prover sends the third and last message (the *response*) $s=r+cx$ reduced modulo the order of the group.

The verifier accepts, if $g^{s}=ty^{c}$ .

We can see this is a valid proof of knowledge because it has an extractor that works as follows:

1. Simulate the prover to output $t=g^{r}$ . The prover is now in state Q .
2. Generate random value $c_{1}$ and input it to the prover. It outputs $s_{1}=r+c_{1}x$ .
3. Rewind the prover to state Q . Now generate a different random value $c_{2}$ and input it to the prover to get $s_{2}=r+c_{2}x$ .
4. Output $(s_{1}-s_{2})(c_{1}-c_{2})^{-1}$ .

Since $(s_{1}-s_{2})=(r+c_{1}x)-(r+c_{2}x)=x(c_{1}-c_{2})$ , the output of the extractor is precisely x .

This protocol happens to be zero-knowledge, though that property is not required for a proof of knowledge.

### Sigma protocols

Protocols which have the above three-move structure (commitment, challenge and response) are called *sigma protocols*. The naming originates from Sig, referring to the zig-zag symbolizing the three moves of the protocol, and MA, an abbreviation of "Merlin-Arthur". Sigma protocols exist for proving various statements, such as those pertaining to discrete logarithms. Using these proofs, the prover can not only prove the knowledge of the discrete logarithm, but also that the discrete logarithm is of a specific form. For instance, it is possible to prove that two logarithms of $y_{1}$ and $y_{2}$ with respect to bases $g_{1}$ and $g_{2}$ are equal or fulfill some other linear relation. For *a* and *b* elements of $Z_{q}$ , we say that the prover proves knowledge of $x_{1}$ and $x_{2}$ such that $y_{1}=g_{1}^{x_{1}}\land y_{2}=g_{2}^{x_{2}}$ and $x_{2}=ax_{1}+b$ . Equality corresponds to the special case where *a* = 1 and *b* = 0. As $x_{2}$ can be trivially computed from $x_{1}$ this is equivalent to proving knowledge of an *x* such that $y_{1}=g_{1}^{x}\land y_{2}={(g_{2}^{a})}^{x}g_{2}^{b}$ .

This is the intuition behind the following notation, which is commonly used to express what exactly is proven by a proof of knowledge.

$PK\{(x):y_{1}=g_{1}^{x}\land y_{2}={(g_{2}^{a})}^{x}g_{2}^{b}\},$

states that the prover knows an *x* that fulfills the relation above.

## Applications

Proofs of knowledge are useful tool for the construction of identification protocols, and in their non-interactive variant, signature schemes. Such schemes are:

- Schnorr signature

They are also used in the construction of group signature and anonymous digital credential systems.
