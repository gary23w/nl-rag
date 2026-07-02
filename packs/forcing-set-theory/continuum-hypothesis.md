---
title: "Continuum hypothesis"
source: https://en.wikipedia.org/wiki/Continuum_hypothesis
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Continuum hypothesis

In mathematics, specifically set theory, the **continuum hypothesis** (abbreviated **CH**) is a hypothesis about the possible sizes of infinite sets. It states:

> There is no set whose cardinality is strictly between that of the integers and the real numbers.

The name of the hypothesis comes from the term *continuum* for the real numbers. In Zermelo–Fraenkel set theory with the axiom of choice (ZFC), this is equivalent to the following equation in aleph numbers: $2^{\aleph _{0}}=\aleph _{1}$ , or even shorter with beth numbers: $\beth _{1}=\aleph _{1}$ .

The continuum hypothesis was advanced by Georg Cantor in 1878. It became one of the most studied problems in set theory, and establishing its truth or falsehood was the first of Hilbert's 23 problems presented in 1900. The answer to this problem is independent of ZFC. This means the axioms of ZFC can neither prove nor disprove the continuum hypothesis, meaning either the continuum hypothesis or its negation can be added as an axiom to ZFC set theory, with the resulting theory being consistent if and only if ZFC is consistent. This independence was proved in 1963 by Paul Cohen, complementing earlier work by Kurt Gödel in 1940.

The **generalized continuum hypothesis** states that $\aleph _{\alpha +1}=2^{\aleph _{\alpha }}$ for every ordinal $\alpha$ .

## History

The continuum hypothesis was first introduced by Georg Cantor in his 1878 paper "Ein Beitrag zur Mannigfaltigkeitslehre", in a form now called the weak continuum hypothesis which is equivalent to the standard formulation under the then-undeveloped axiom of choice. Cantor initially presented the weak continuum hypothesis as a theorem, but did not give a proof and later became uncertain of it. On 25 October 1882, Cantor wrote to his correspondent Gösta Mittag-Leffler, and formulated the continuum hypothesis (CH) in its modern form and gave his belief he could prove it. By the 1890s, many mathematicians in Germany and France were aware of the problem. Cantor tried for many years to prove CH but never succeeded.

It became the first on David Hilbert's list of important open questions that was presented at the International Congress of Mathematicians (ICM) in the year 1900 in Paris. At that point, axiomatic set theory was not yet formulated.

Many erroneous proofs and disproofs of CH were given. As early as 1884, Paul Tannery claimed to prove CH, but the proof was erroneous. In 1890, Beppo Levi claimed to have a proof from assuming that every subset of the real numbers has the Baire property, but no proof was ever published. At the 1904 ICM in Heidelberg, Gyula Kőnig announced he had disproven CH, drawing wide attention that even reached the Grand Duke of Baden Frederick I via Felix Klein, but a flaw in the proof was found the next day. Felix Bernstein also published an attempted proof of CH in 1904, but it was wrong and attracted little response. In 1926, Hilbert claimed to have solved the continuum hypothesis and gave a proof sketch, but this was also incorrect, although it influenced later ideas in recursion theory.

In 1906, Kőnig revised part of his attempted CH disproof and established Kőnig's theorem, which by using the concept of cofinality introduced in 1908 by Felix Hausdorff, shows that result that $2^{\aleph _{0}}$ cannot equal $\aleph _{\alpha }$ for $\alpha$ with cofinality $\omega$ . For example, $2^{\aleph _{0}}\neq \aleph _{\omega }$ . Hausdorff formulated the question of whether $2^{\aleph _{\alpha }}=\aleph _{\alpha +1}$ for all ordinals $\alpha$ , which would be named the *generalized continuum hypothesis* by Alfred Tarski in 1925. In 1923, Thoralf Skolem conjectured that CH could not be settled by the axioms of Zermelo set theory.

Kurt Gödel proved in 1940 that the negation of the continuum hypothesis, i.e., the existence of a set with intermediate cardinality, could not be proved in standard set theory. The second half of the independence of the continuum hypothesis – i.e., unprovability of the nonexistence of an intermediate-sized set – was proved in 1963 by Paul Cohen.

## Cardinality of infinite sets

Two sets are said to have the same *cardinality* or *cardinal number* if there exists a bijection (a one-to-one correspondence) between them. Intuitively, for two sets S and T to have the same cardinality means that it is possible to "pair off" elements of S with elements of T in such a fashion that every element of S is paired off with exactly one element of T and vice versa. Hence, the set $\{{\text{banana}},{\text{apple}},{\text{pear}}\}$ has the same cardinality as $\{{\text{yellow}},{\text{red}},{\text{green}}\}$ despite the sets themselves containing different elements.

With infinite sets such as the set of integers or rational numbers, the existence of a bijection between two sets becomes more difficult to demonstrate. The rational numbers $\mathbb {Q}$ seemingly form a counterexample to the continuum hypothesis: the integers form a proper subset of the rationals, which themselves form a proper subset of the reals, so intuitively, there are more rational numbers than integers and more real numbers than rational numbers. However, this intuitive analysis is flawed since it does not take into account the fact that all three sets are infinite. Perhaps more importantly, it in fact conflates the concept of "size" of the set $\mathbb {Q}$ with the order or topological structure placed on it. In fact, it turns out the rational numbers can actually be placed in one-to-one correspondence with the integers, and therefore the set of rational numbers is the same size (*cardinality*) as the set of integers: they are both countable sets.

Cantor gave two proofs that the cardinality of the set of integers is strictly smaller than that of the set of real numbers (see Cantor's first uncountability proof and Cantor's diagonal argument). His proofs, however, give no indication of the extent to which the cardinality of the integers is less than that of the real numbers. Cantor proposed the continuum hypothesis as a possible solution to this question.

In simple terms, the Continuum Hypothesis (CH) states that the set of real numbers has minimal possible cardinality which is greater than the cardinality of the set of integers. That is, every infinite set $S\subseteq \mathbb {R}$ of real numbers can either be mapped one-to-one into the integers or the real numbers can be mapped one-to-one into S . Since the real numbers are equinumerous with the powerset of the integers, i.e. $|\mathbb {R} |=2^{\aleph _{0}}$ , CH can be restated as follows:

**Continuum Hypothesis**— $\nexists S\colon \aleph _{0}<|S|<2^{\aleph _{0}}$ .

Assuming the axiom of choice, there is a unique smallest cardinal number $\aleph _{1}$ greater than $\aleph _{0}$ , and the continuum hypothesis is in turn equivalent to the equality $2^{\aleph _{0}}=\aleph _{1}$ .

## Independence from ZFC

The independence of the continuum hypothesis (CH) from Zermelo–Fraenkel set theory (ZF) follows from combined work of Kurt Gödel and Paul Cohen.

Gödel showed that CH cannot be disproved from ZF, even if the axiom of choice (AC) is adopted, i.e. from ZFC. Gödel's proof shows that both CH and AC hold in the constructible universe L , an inner model of ZF set theory, assuming only the axioms of ZF. The existence of an inner model of ZF in which additional axioms hold shows that the additional axioms are (relatively) consistent with ZF, provided ZF itself is consistent. The latter condition cannot be proved in ZF itself, due to Gödel's incompleteness theorems, but is widely believed to be true and can be proved in stronger set theories.

Cohen showed that CH cannot be proven from the ZFC axioms, completing the overall independence proof. To prove his result, Cohen developed the method of forcing, which has become a standard tool in set theory. Essentially, this method begins with a model of ZF in which CH holds and constructs another model which contains more sets than the original in a way that CH does not hold in the new model. Cohen was awarded the Fields Medal in 1966 for his proof.

Cohen's independence proof shows that CH is independent of ZFC. Further research has shown that CH is independent of all known *large cardinal axioms* in the context of ZFC. Moreover, it has been shown that the cardinality of the continuum ${\mathfrak {c}}=2^{\aleph _{0}}$ can be any cardinal consistent with Kőnig's theorem. A result of Solovay, proved shortly after Cohen's result on the independence of the continuum hypothesis, shows that in any model of ZFC, if $\kappa$ is a cardinal of uncountable cofinality, then there is a forcing extension in which $2^{\aleph _{0}}=\kappa$ . However, per Kőnig's theorem, it is not consistent to assume $2^{\aleph _{0}}$ is $\aleph _{\omega }$ or $\aleph _{\omega _{1}+\omega }$ or any cardinal with cofinality $\omega$ .

The continuum hypothesis is closely related to many statements in analysis, point-set topology and measure theory. As a result of its independence, many substantial conjectures in those fields have subsequently been shown to be independent as well.

The independence from ZFC means that proving or disproving the CH within ZFC is impossible. However, Gödel and Cohen's negative results are not universally accepted as disposing of all interest in the continuum hypothesis. The continuum hypothesis remains an active topic of research: see Woodin and Koellner for an overview of the current research status.

The continuum hypothesis and the axiom of choice were among the first genuinely mathematical statements shown to be independent of ZF set theory. Although the existence of some statements independent of ZFC had already been known more than two decades prior: for example, assuming good soundness properties and the consistency of ZFC, Gödel's incompleteness theorems published in 1931 establish that there is a formal statement Con(ZFC) (one for each appropriate Gödel numbering scheme) expressing the consistency of ZFC, that is also independent of it. The latter independence result indeed holds for many theories.

## Arguments for and against the continuum hypothesis

Gödel believed that CH is false, and that his proof that CH is consistent with ZFC only shows that the Zermelo–Fraenkel axioms do not adequately characterize the universe of sets. Gödel was a Platonist and therefore had no problems with asserting the truth and falsehood of statements independent of their provability. Cohen, though a formalist, also tended towards rejecting CH.

Historically, mathematicians who favored a "rich" and "large" universe of sets were against CH, while those favoring a "neat" and "controllable" universe favored CH. Parallel arguments were made for and against the axiom of constructibility, which implies CH. More recently, Matthew Foreman has pointed out that ontological maximalism can actually be used to argue in favor of CH, because among models that have the same reals, models with "more" sets of reals have a better chance of satisfying CH.

Another viewpoint is that the conception of set is not specific enough to determine whether CH is true or false. This viewpoint was advanced as early as 1923 by Skolem, even before Gödel's first incompleteness theorem. Skolem argued on the basis of what is now known as Skolem's paradox, and it was later supported by the independence of CH from the axioms of ZFC since these axioms are enough to establish the elementary properties of sets and cardinalities. In order to argue against this viewpoint, it would be sufficient to demonstrate new axioms that are supported by intuition and resolve CH in one direction or another. Although the axiom of constructibility does resolve CH, it is not generally considered to be intuitively true any more than CH is generally considered to be false.

At least two other axioms have been proposed that have implications for the continuum hypothesis, although these axioms have not currently found wide acceptance in the mathematical community. In 1986, Chris Freiling presented an argument against CH by showing that the negation of CH is equivalent to Freiling's axiom of symmetry, a statement derived by arguing from particular intuitions about probabilities. Freiling believes this axiom is "intuitively clear" but others have disagreed.

A difficult argument against CH developed by W. Hugh Woodin has attracted considerable attention since the year 2000. Foreman does not reject Woodin's argument outright but urges caution. Woodin proposed a new hypothesis that he labeled the "(*)-axiom", or "Star axiom". The Star axiom would imply that $2^{\aleph _{0}}$ is $\aleph _{2}$ , thus falsifying CH. The Star axiom was bolstered by an independent May 2021 proof showing the Star axiom can be derived from a variation of Martin's maximum. However, Woodin stated in the 2010s that he now instead believes CH to be true, based on his belief in his new "ultimate L" conjecture.

Solomon Feferman argued that CH is not a definite mathematical problem. He proposed a theory of "definiteness" using a semi-intuitionistic subsystem of ZF that accepts classical logic for bounded quantifiers but uses intuitionistic logic for unbounded ones, and suggested that a proposition $\phi$ is mathematically "definite" if the semi-intuitionistic theory can prove $(\phi \lor \neg \phi )$ . He conjectured that CH is not definite according to this notion, and proposed that CH should, therefore, be considered not to have a truth value. Peter Koellner wrote a critical commentary on Feferman's article.

Joel David Hamkins proposes a multiverse approach to set theory and argues that "the continuum hypothesis is settled on the multiverse view by our extensive knowledge about how it behaves in the multiverse, and, as a result, it can no longer be settled in the manner formerly hoped for". In a related vein, Saharon Shelah wrote that he does "not agree with the pure Platonic view that the interesting problems in set theory can be decided, that we just have to discover the additional axiom. My mental picture is that we have many possible set theories, all conforming to ZFC".

## Generalized continuum hypothesis

The *generalized continuum hypothesis* (GCH) states that if an infinite set's cardinality lies between that of an infinite set S and that of the power set ${\mathcal {P}}(S)$ of S, then it has the same cardinality as either S or ${\mathcal {P}}(S)$ . That is, for any infinite cardinal $\lambda$ there is no cardinal $\kappa$ such that $\lambda <\kappa <2^{\lambda }$ . GCH is equivalent to:

$\aleph _{\alpha +1}=2^{\aleph _{\alpha }}$

for every

ordinal

$\alpha$

(occasionally called *Cantor's aleph hypothesis*).

The beth numbers provide an alternative notation for this condition: $\aleph _{\alpha }=\beth _{\alpha }$ for every ordinal $\alpha$ . The continuum hypothesis is the special case for the ordinal $\alpha =1$ . GCH was first suggested by Philip Jourdain. For the early history of GCH, see Moore.

Like CH, GCH is also independent of ZFC, but Sierpiński proved that ZF + GCH implies the axiom of choice (AC) (and therefore the negation of the axiom of determinacy, AD), so choice and GCH are not independent in ZF; there are no models of ZF in which GCH holds and AC fails. To prove this, Sierpiński showed GCH implies that every cardinality n is smaller than some aleph number, and thus can be ordered. This is done by showing that n is smaller than $2^{\aleph _{0}+n}$ which is smaller than its own Hartogs number—this uses the equality $2^{\aleph _{0}+n}\,=\,2\cdot \,2^{\aleph _{0}+n}$ ; for the full proof, see Gillman.

Kurt Gödel showed that GCH is a consequence of ZF + V=L (the axiom that every set is constructible relative to the ordinals), and is therefore consistent with ZFC. As GCH implies CH, Cohen's model in which CH fails is a model in which GCH fails, and thus GCH is not provable from ZFC. W. B. Easton used the method of forcing developed by Cohen to prove Easton's theorem, which shows it is consistent with ZFC for arbitrarily large cardinals $\aleph _{\alpha }$ to fail to satisfy $2^{\aleph _{\alpha }}=\aleph _{\alpha +1}$ . Much later, Foreman and Woodin proved that (assuming the consistency of very large cardinals) it is consistent that $2^{\kappa }>\kappa ^{+}$ holds for every infinite cardinal $\kappa$ . Later Woodin extended this by showing the consistency of $2^{\kappa }=\kappa ^{++}$ for every $\kappa$ . Carmi Merimovich showed that, for each *n* ≥ 1, it is consistent with ZFC that for each infinite cardinal κ, 2*κ* is the nth successor of κ (assuming the consistency of some large cardinal axioms). On the other hand, László Patai proved that if γ is an ordinal and for each infinite cardinal κ, 2*κ* is the γth successor of κ, then γ is finite.

For any infinite sets A and B, if there is an injection from A to B then there is an injection from subsets of A to subsets of B. Thus for any infinite cardinals A and B, $A<B\to 2^{A}\leq 2^{B}$ . If A and B are finite, the stronger inequality $A<B\to 2^{A}<2^{B}$ holds. GCH implies that this strict, stronger inequality holds for infinite cardinals as well as finite cardinals.

### Implications of GCH for cardinal exponentiation

Although the generalized continuum hypothesis refers directly only to cardinal exponentiation with 2 as the base, one can deduce from it the values of cardinal exponentiation $\aleph _{\alpha }^{\aleph _{\beta }}$ in all cases. GCH implies that for ordinals α and β:

- $\aleph _{\alpha }^{\aleph _{\beta }}=\aleph _{\beta +1}$ when *α* ≤ *β*+1;
- $\aleph _{\alpha }^{\aleph _{\beta }}=\aleph _{\alpha }$ when *β*+1 < *α* and $\aleph _{\beta }<\operatorname {cf} (\aleph _{\alpha })$ , where **cf** is the cofinality operation; and
- $\aleph _{\alpha }^{\aleph _{\beta }}=\aleph _{\alpha +1}$ when *β*+1 < *α* and $\aleph _{\beta }\geq \operatorname {cf} (\aleph _{\alpha })$ .

The first equality (when *α* ≤ *β*+1) follows from:

$\aleph _{\alpha }^{\aleph _{\beta }}\leq \aleph _{\beta +1}^{\aleph _{\beta }}=(2^{\aleph _{\beta }})^{\aleph _{\beta }}=2^{\aleph _{\beta }\cdot \aleph _{\beta }}=2^{\aleph _{\beta }}=\aleph _{\beta +1}$ while:

$\aleph _{\beta +1}=2^{\aleph _{\beta }}\leq \aleph _{\alpha }^{\aleph _{\beta }}.$

The third equality (when *β*+1 < *α* and $\aleph _{\beta }\geq \operatorname {cf} (\aleph _{\alpha })$ ) follows from:

$\aleph _{\alpha }^{\aleph _{\beta }}\geq \aleph _{\alpha }^{\operatorname {cf} (\aleph _{\alpha })}>\aleph _{\alpha }$

by Kőnig's theorem, while:

$\aleph _{\alpha }^{\aleph _{\beta }}\leq \aleph _{\alpha }^{\aleph _{\alpha }}\leq (2^{\aleph _{\alpha }})^{\aleph _{\alpha }}=2^{\aleph _{\alpha }\cdot \aleph _{\alpha }}=2^{\aleph _{\alpha }}=\aleph _{\alpha +1}$
