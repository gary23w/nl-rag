---
title: "Reduction strategy"
source: https://en.wikipedia.org/wiki/Reduction_strategy
domain: operational-semantics
license: CC-BY-SA-4.0
tags: operational semantics, structural operational semantics, abstract machine, reduction strategy
fetched: 2026-07-02
---

# Reduction strategy

In rewriting, a **reduction strategy** or rewriting strategy is a relation specifying a rewrite for each object or term, compatible with a given reduction relation. Some authors use the term to refer to an evaluation strategy.

## Definitions

Formally, for an abstract rewriting system $(A,\to )$ , a reduction strategy $\to _{S}$ is a binary relation on A with $\to _{S}\subseteq {\overset {+}{\to }}$ , where ${\overset {+}{\to }}$ is the transitive closure of $\to$ (but not the reflexive closure). In addition the normal forms of the strategy must be the same as the normal forms of the original rewriting system, i.e. for all a , there exists a b with $a\to b$ iff $\exists b'.a\to _{S}b'$ .

A *one step* reduction strategy is one where $\to _{S}\subseteq \to$ . Otherwise it is a *many step* strategy.

A *deterministic* strategy is one where $\to _{S}$ is a partial function, i.e. for each $a\in A$ there is at most one b such that $a\to _{S}b$ . Otherwise it is a *nondeterministic* strategy.

## Term rewriting

In a term rewriting system a rewriting strategy specifies, out of all the reducible subterms (redexes), which one should be reduced (*contracted*) within a term.

One-step strategies for term rewriting include:

- leftmost-innermost: in each step the leftmost of the innermost redexes is contracted, where an innermost redex is a redex not containing any redexes
- leftmost-outermost: in each step the leftmost of the outermost redexes is contracted, where an outermost redex is a redex not contained in any redexes
- rightmost-innermost, rightmost-outermost: similarly

Many-step strategies include:

- parallel-innermost: reduces all innermost redexes simultaneously. This is well-defined because the redexes are pairwise disjoint.
- parallel-outermost: similarly
- Gross-Knuth reduction, also called full substitution or Kleene reduction: all redexes in the term are simultaneously reduced

Parallel outermost and Gross-Knuth reduction are *hypernormalizing* for all almost-orthogonal term rewriting systems, meaning that these strategies will eventually reach a normal form if it exists, even when performing (finitely many) arbitrary reductions between successive applications of the strategy.

Stratego is a domain-specific language designed specifically for programming term rewriting strategies.

## Lambda calculus

In the context of the lambda calculus, *normal-order reduction* refers to leftmost-outermost reduction in the sense given above. Normal-order reduction is normalizing, in the sense that if a term has a normal form, then normal‐order reduction will eventually reach it, hence the name normal. This is known as the standardization theorem.

*Leftmost reduction* is sometimes used to refer to normal order reduction, as with a pre-order traversal the notions coincide, and similarly the leftmost-outermost redex is the redex with leftmost starting character when the lambda term is considered as a string of characters. When "leftmost" is defined using an in-order traversal the notions are distinct. For example, in the term $(\lambda x.x\Omega )(\lambda y.I)$ with $\Omega ,I$ defined here, the leftmost redex of the in-order traversal is $\Omega$ while the leftmost-outermost redex is the entire expression.

*Applicative order reduction* refers to leftmost-innermost reduction. In contrast to normal order, applicative order reduction may not terminate, even when the term has a normal form. For example, using applicative order reduction, the following sequence of reductions is possible: ${\begin{aligned}&(\mathbf {\lambda } x.z)((\lambda w.www)(\lambda w.www))\\\rightarrow &(\lambda x.z)((\lambda w.www)(\lambda w.www)(\lambda w.www))\\\rightarrow &(\lambda x.z)((\lambda w.www)(\lambda w.www)(\lambda w.www)(\lambda w.www))\\\rightarrow &(\lambda x.z)((\lambda w.www)(\lambda w.www)(\lambda w.www)(\lambda w.www)(\lambda w.www))\\&\ldots \end{aligned}}$

But using normal-order reduction, the same starting point reduces quickly to normal form: $(\mathbf {\lambda } x.z)((\lambda w.www)(\lambda w.www))$ $\rightarrow z$

*Full β-reduction* refers to the nondeterministic one-step strategy that allows reducing any redex at each step. Takahashi's *parallel β-reduction* is the strategy that reduces all redexes in the term simultaneously.

### Weak reduction

Normal and applicative order reduction are strong in that they allow reduction under lambda abstractions. In contrast, *weak* reduction does not reduce under a lambda abstraction. *Call-by-name reduction* is the weak reduction strategy that reduces the leftmost outermost redex not inside a lambda abstraction, while *call-by-value reduction* is the weak reduction strategy that reduces the leftmost innermost redex not inside a lambda abstraction. These strategies were devised to reflect the call-by-name and call-by-value evaluation strategies. In fact, applicative order reduction was also originally introduced to model the call-by-value parameter passing technique found in Algol 60 and modern programming languages. When combined with the idea of weak reduction, the resulting call-by-value reduction is indeed a faithful approximation.

Unfortunately, weak reduction is not confluent, and the traditional reduction equations of the lambda calculus are useless, because they suggest relationships that violate the weak evaluation regime. However, it is possible to extend the system to be confluent by allowing a restricted form of reduction under an abstraction, in particular when the redex does not involve the variable bound by the abstraction. For example, λ*x*.(λ*y*.*x*)*z* is in normal form for a weak reduction strategy because the redex (λ*y*.*x*)*z* is contained in a lambda abstraction. But the term λ*x*.(λ*y*.*y*)*z* can still be reduced under the extended weak reduction strategy, because the redex (λ*y*.*y*)*z* does not refer to *x*.

### Optimal reduction

Optimal reduction is motivated by the existence of lambda terms where there does not exist a sequence of reductions which reduces them without duplicating work. For example, consider

```
((λg.(g(g(λx.x))))
 (λh.((λf.(f(f(λz.z))))
      (λw.(h(w(λy.y)))))))
```

It is composed of three nested terms, a=((λg. ... ) (λh.b)), b=((λf. ...) c), and c=(λw. ...). There are only two possible β-reductions to be done here, on a and on b. Reducing the outer a term first results in the inner b term being duplicated, and each copy will have to be reduced, but reducing the inner b term first will duplicate its argument c, which will cause work to be duplicated when the values of h and w are made known.

Optimal reduction is not a reduction strategy for the lambda calculus in a narrow sense because performing β-reduction loses the information about the substituted redexes being shared. Instead it is defined for the *labelled lambda calculus*, an annotated lambda calculus which captures a precise notion of the work that should be shared.

Labels consist of a countably infinite set of atomic labels, and concatenations $ab$ , overlinings ${\overline {a}}$ and underlinings ${\underline {a}}$ of labels. A labelled term is a lambda calculus term where each subterm has a label. The standard initial labeling of a lambda term gives each subterm a unique atomic label. Labelled β-reduction is given by: $((\lambda x.M)^{\alpha }N)^{\beta }\to \beta {\overline {\alpha }}\cdot M[x\mapsto {\underline {\alpha }}\cdot N]$

where $\cdot$ concatenates labels, $\beta \cdot T^{\alpha }=T^{\beta \alpha }$ , and substitution $M[x\mapsto N]$ is defined as follows (using the Barendregt convention): ${\begin{aligned}x^{\alpha }[x\mapsto N]&=\alpha \cdot N&\quad (\lambda y.M)^{\alpha }[x\mapsto N]&=(\lambda y.M[x\mapsto N])^{\alpha }\\y^{\alpha }[x\mapsto N]&=y^{\alpha }&\quad (MN)^{\alpha }[x\mapsto P]&=(M[x\mapsto P]N[x\mapsto P])^{\alpha }\end{aligned}}$ The system can be proven to be confluent. Optimal reduction is then defined to be normal order or leftmost-outermost reduction using reduction by families, i.e. the parallel reduction of all redexes with the same function part label. The strategy is optimal in the sense that it performs the optimal (minimal) number of family reduction steps.

A practical algorithm for optimal reduction was first described in 1989, more than a decade after optimal reduction was first defined in 1974. The Bologna Optimal Higher-order Machine (BOHM) is a prototype implementation of an extension of the technique to interaction nets. Lambdascope is a more recent implementation of optimal reduction, also using interaction nets.

### Call by need reduction

*Call by need reduction* can be defined similarly to optimal reduction as weak leftmost-outermost reduction using parallel reduction of redexes with the same label, for a slightly different labelled lambda calculus. An alternate definition changes the beta rule to an operation that finds the next "needed" computation, evaluates it, and substitutes the result into all locations. This requires extending the beta rule to allow reducing terms that are not syntactically adjacent. As with call-by-name and call-by-value, call-by-need reduction was devised to mimic the behavior of the evaluation strategy known as "call-by-need" or lazy evaluation.
