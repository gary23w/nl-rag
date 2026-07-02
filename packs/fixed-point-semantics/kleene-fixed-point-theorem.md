---
title: "Kleene fixed-point theorem"
source: https://en.wikipedia.org/wiki/Kleene_fixed-point_theorem
domain: fixed-point-semantics
license: CC-BY-SA-4.0
tags: least fixed point, Kleene fixed-point theorem, Knaster-Tarski theorem, fixed-point combinator
fetched: 2026-07-02
---

# Kleene fixed-point theorem

In the mathematical areas of order and lattice theory, the **Kleene fixed-point theorem**, named after American mathematician Stephen Cole Kleene, states the following:

Kleene Fixed-Point Theorem.

Suppose

$(L,\sqsubseteq )$

is a

directed-complete partial order

(dcpo) with a least element, and let

$f:L\to L$

be a

Scott-continuous

(and therefore

monotone

)

function

. Then

f

has a

least fixed point

, which is the

supremum

of the ascending Kleene chain of

$f.$

The **ascending Kleene chain** of *f* is the chain

$\bot \sqsubseteq f(\bot )\sqsubseteq f(f(\bot ))\sqsubseteq \cdots \sqsubseteq f^{n}(\bot )\sqsubseteq \cdots$

obtained by iterating *f* on the least element ⊥ of *L*. Expressed in a formula, the theorem states that

${\textrm {lfp}}(f)=\sup \left(\left\{f^{n}(\bot )\mid n\in \mathbb {N} \right\}\right)$

where ${\textrm {lfp}}$ denotes the least fixed point.

Although Tarski's fixed point theorem does not consider how fixed points can be computed by iterating *f* from some seed (also, it pertains to monotone functions on complete lattices), this result is often attributed to Alfred Tarski who proves it for additive functions. Moreover, the Kleene fixed-point theorem can be extended to monotone functions using transfinite iterations.

## Proof

Source:

We first have to show that the ascending Kleene chain of f exists in L . To show that, we prove the following:

Lemma.

If

L

is a dcpo with a least element, and

$f:L\to L$

is Scott-continuous, then

$f^{n}(\bot )\sqsubseteq f^{n+1}(\bot ),n\in \mathbb {N} _{0}$

Proof.

We use induction:

- Assume n = 0. Then $f^{0}(\bot )=\bot \sqsubseteq f^{1}(\bot ),$ since $\bot$ is the least element.
- Assume n > 0. Then we have to show that $f^{n}(\bot )\sqsubseteq f^{n+1}(\bot )$ . By rearranging we get $f(f^{n-1}(\bot ))\sqsubseteq f(f^{n}(\bot ))$ . By inductive assumption, we know that $f^{n-1}(\bot )\sqsubseteq f^{n}(\bot )$ holds, and because f is monotone (property of Scott-continuous functions), the result holds as well.

As a corollary of the Lemma we have the following directed ω-chain:

$\mathbb {M} =\{\bot ,f(\bot ),f(f(\bot )),\ldots \}.$

From the definition of a dcpo it follows that $\mathbb {M}$ has a supremum, call it $m.$ What remains now is to show that m is the least fixed-point.

First, we show that m is a fixed point, i.e. that $f(m)=m$ . Because f is Scott-continuous, $f(\sup(\mathbb {M} ))=\sup(f(\mathbb {M} ))$ , that is $f(m)=\sup(f(\mathbb {M} ))$ . Also, since $\mathbb {M} =f(\mathbb {M} )\cup \{\bot \}$ and because $\bot$ has no influence in determining the supremum we have: $\sup(f(\mathbb {M} ))=\sup(\mathbb {M} )$ . It follows that $f(m)=m$ , making m a fixed-point of f .

The proof that m is in fact the *least* fixed point can be done by showing that any element in $\mathbb {M}$ is smaller than any fixed-point of f (because by property of supremum, if all elements of a set $D\subseteq L$ are smaller than an element of L then also $\sup(D)$ is smaller than that same element of L ). This is done by induction: Assume k is some fixed-point of f . We now prove by induction over i that $\forall i\in \mathbb {N} :f^{i}(\bot )\sqsubseteq k$ . The base of the induction $(i=0)$ obviously holds: $f^{0}(\bot )=\bot \sqsubseteq k,$ since $\bot$ is the least element of L . As the induction hypothesis, we may assume that $f^{i}(\bot )\sqsubseteq k$ . We now do the induction step: From the induction hypothesis and the monotonicity of f (again, implied by the Scott-continuity of f ), we may conclude the following: $f^{i}(\bot )\sqsubseteq k~\implies ~f^{i+1}(\bot )\sqsubseteq f(k).$ Now, by the assumption that k is a fixed-point of $f,$ we know that $f(k)=k,$ and from that we get $f^{i+1}(\bot )\sqsubseteq k.$
