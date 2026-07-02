---
title: "Radon–Nikodym theorem"
source: https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem
domain: measure-theory
license: CC-BY-SA-4.0
tags: measure theory, lebesgue integration, lebesgue measure, borel set
fetched: 2026-07-02
---

# Radon–Nikodym theorem

In mathematics, the **Radon–Nikodym theorem**, named after Johann Radon and Otto M. Nikodym, is a result in measure theory that expresses the relationship between two measures defined on the same measurable space. A *measure* is a set function that assigns a consistent magnitude to the measurable subsets of a measurable space. Examples of a measure include area and volume, where the subsets are sets of points; or the probability of an event, which is a subset of possible outcomes within a wider probability space.

One way to derive a new measure from one already given is to assign a density to each point of the space, then integrate over the measurable subset of interest. This can be expressed as

$\nu (A)=\int _{A}f\,d\mu ,$

where $\nu$ is the new measure being defined for any measurable subset A and the function f is the density at a given point. The integral is with respect to an existing measure $\mu$ , which may often be the canonical Lebesgue measure on the real line $\mathbb {R}$ or the n -dimensional Euclidean space $\mathbb {R} ^{n}$ (corresponding to our standard notions of length, area and volume). For example, if f represented mass density and $\mu$ was the Lebesgue measure in three-dimensional space $\mathbb {R} ^{3}$ , then $\nu (A)$ would equal the total mass in a spatial region A .

The Radon–Nikodym theorem essentially states that, under certain conditions, any measure $\nu$ can be expressed in this way with respect to another measure $\mu$ on the same space. The function f is then called the **Radon–Nikodym derivative** and is denoted by $d\nu /d\mu$ . An important application is in probability theory, leading to the probability density function of a random variable.

The theorem is named after Johann Radon, who proved the theorem for the special case where the underlying space is $\mathbb {R} ^{n}$ in 1913, and for Otto Nikodym who proved the general case in 1930. In 1936, Hans Freudenthal generalized the Radon–Nikodym theorem by proving the Freudenthal spectral theorem, a result in Riesz space theory; this contains the Radon–Nikodym theorem as a special case.

A Banach space Y is said to have the Radon–Nikodym property if the generalization of the Radon–Nikodym theorem also holds (with the necessary adjustments made) for functions with values in Y . All Hilbert spaces have the Radon–Nikodym property.

## Formal description

### Radon–Nikodym theorem

The **Radon–Nikodym theorem** involves a measurable space $(X,\Sigma )$ on which two σ-finite measures are defined, $\mu$ and $\nu .$ It states that, if $\nu \ll \mu$ (that is, if $\nu$ is absolutely continuous with respect to $\mu$ ), then there exists a $\Sigma$ -measurable function $f:X\to [0,\infty ),$ such that for any measurable set $A\in \Sigma ,$ $\nu (A)=\int _{A}f\,d\mu .$

### Radon–Nikodym derivative

The function f satisfying the above equality is *uniquely defined up to a $\mu$ -null set*, that is, if g is another function which satisfies the same property, then $f=g$ $\mu$ -almost everywhere. The function f is commonly written $d\nu /d\mu$ and is called the **Radon–Nikodym derivative**. The choice of notation and the name of the function reflects the fact that the function is analogous to a derivative in calculus in the sense that it describes the rate of change of density of one measure with respect to another (the way the Jacobian determinant is used in multivariable integration).

### Extension to signed or complex measures

A similar theorem can be proven for signed and complex measures: namely, that if $\mu$ is a nonnegative σ-finite measure, and $\nu$ is a finite-valued signed or complex measure such that $\nu \ll \mu ,$ that is, $\nu$ is absolutely continuous with respect to $\mu ,$ then there is a $\mu$ -integrable real- or complex-valued function g on X such that for every measurable set $A,$ $\nu (A)=\int _{A}g\,d\mu .$

## Examples

In the following examples, the set X is the real interval $[0,1]$ , and $\Sigma$ is the Borel sigma-algebra on X .

1. Let $\mu$ be the length measure on X , and let $\nu$ assign to each subset Y of X twice the length of Y . Then ${\textstyle {\frac {d\nu }{d\mu }}=2}$ .
2. Let $\mu$ be the length measure on X , and let $\nu$ assign to each subset Y of X the number of points from the set $\{0.1,\dots ,0.9\}$ that are contained in Y . Then $\nu$ is not absolutely continuous with respect to $\mu$ since it assigns non-zero measure to zero-length points. Indeed, there is no derivative ${\textstyle {\frac {d\nu }{d\mu }}}$ : there is no finite function that, when integrated e.g. from $(0.1-\varepsilon )$ to $(0.1+\varepsilon )$ , gives 1 for all $\varepsilon >0$ .
3. $\mu =\nu +\delta _{0}$ , where $\nu$ is the length measure on X and $\delta _{0}$ is the Dirac measure on 0 (it assigns a measure of 1 to any set containing 0 and a measure of 0 to any other set). Then, $\nu$ is absolutely continuous with respect to $\mu$ , and ${\textstyle {\frac {d\nu }{d\mu }}=1_{X\setminus \{0\}}}$ – the derivative is 0 at $x=0$ and 1 at $x>0$ .

## Properties

- Let *ν*, *μ*, and *λ* be σ-finite measures on the same measurable space. If *ν* ≪ *λ* and *μ* ≪ *λ* (*ν* and *μ* are both absolutely continuous with respect to *λ*), then ${\frac {d(\nu +\mu )}{d\lambda }}={\frac {d\nu }{d\lambda }}+{\frac {d\mu }{d\lambda }}\quad \lambda {\text{-almost everywhere}}.$
- If *ν* ≪ *μ* ≪ *λ*, then ${\frac {d\nu }{d\lambda }}={\frac {d\nu }{d\mu }}{\frac {d\mu }{d\lambda }}\quad \lambda {\text{-almost everywhere}}.$
- In particular, if *μ* ≪ *ν* and *ν* ≪ *μ*, then ${\frac {d\mu }{d\nu }}=\left({\frac {d\nu }{d\mu }}\right)^{-1}\quad \nu {\text{-almost everywhere}}.$
- If *μ* ≪ *λ* and g is a *μ*-integrable function, then $\int _{X}g\,d\mu =\int _{X}g{\frac {d\mu }{d\lambda }}\,d\lambda .$
- If *ν* is a finite signed or complex measure, then ${d|\nu | \over d\mu }=\left|{d\nu \over d\mu }\right|.$

## Applications

### Probability theory

The theorem is very important in extending the ideas of probability theory from probability masses and probability densities defined over real numbers to probability measures defined over arbitrary sets. It tells if and how it is possible to change from one probability measure to another. Specifically, the probability density function of a random variable is the Radon–Nikodym derivative of the induced measure with respect to some base measure (usually the Lebesgue measure for continuous random variables).

For example, it can be used to prove the existence of conditional expectation for probability measures. The latter itself is a key concept in probability theory, as conditional probability is just a special case of it.

### Financial mathematics

Amongst other fields, financial mathematics uses the theorem extensively, in particular via the Girsanov theorem. Such changes of probability measure are the cornerstone of the rational pricing of derivatives and are used for converting actual probabilities into those of the risk neutral probabilities.

### Information divergences

If *μ* and *ν* are measures over X, and *μ* ≪ *ν*

- The Kullback–Leibler divergence from *ν* to *μ* is defined to be $D_{\text{KL}}(\mu \parallel \nu )=\int _{X}\log \left({\frac {d\mu }{d\nu }}\right)\;d\mu .$
- For *α* > 0, *α* ≠ 1 the Rényi divergence of order *α* from *ν* to *μ* is defined to be $D_{\alpha }(\mu \parallel \nu )={\frac {1}{\alpha -1}}\log \left(\int _{X}\left({\frac {d\mu }{d\nu }}\right)^{\alpha -1}\;d\mu \right).$

## The assumption of σ-finiteness

The Radon–Nikodym theorem above makes the assumption that the measure *μ* with respect to which one computes the rate of change of *ν* is σ-finite.

### Negative example

Here is an example when *μ* is not σ-finite and the Radon–Nikodym theorem fails to hold.

Consider the Borel σ-algebra on the real line. Let the counting measure, μ, of a Borel set A be defined as the number of elements of A if A is finite, and ∞ otherwise. One can check that μ is indeed a measure. It is not σ-finite, as not every Borel set is at most the union of countably many finite sets. Let ν be the usual Lebesgue measure on this Borel algebra. Then, ν is absolutely continuous with respect to μ, since for a set A one has *μ*(*A*) = 0 only if A is the empty set, and then *ν*(*A*) is also zero.

Assume that the Radon–Nikodym theorem holds, that is, for some measurable function *f* one has

$\nu (A)=\int _{A}f\,d\mu$

for all Borel sets. Taking A to be a singleton set, *A* = {*a*}, and using the above equality, one finds

$0=f(a)$

for all real numbers a. This implies that the function  *f* , and therefore the Lebesgue measure ν, is zero, which is a contradiction.

### Positive result

Assuming $\nu \ll \mu ,$ the Radon–Nikodym theorem also holds if $\mu$ is localizable and $\nu$ is *accessible with respect to* $\mu$ , i.e., $\nu (A)=\sup\{\nu (B):B\in {\cal {P}}(A)\cap \mu ^{\operatorname {pre} }(\mathbb {R} _{\geq 0})\}$ for all $A\in \Sigma .$

## Proof

This section gives a measure-theoretic proof of the theorem. There is also a functional-analytic proof, using Hilbert space methods, that was first given by von Neumann.

For finite measures μ and ν, the idea is to consider functions  *f*  with *f dμ* ≤ *dν*. The supremum of all such functions, along with the monotone convergence theorem, then furnishes the Radon–Nikodym derivative. The fact that the remaining part of μ is singular with respect to ν follows from a technical fact about finite measures. Once the result is established for finite measures, extending to σ-finite, signed, and complex measures can be done naturally. The details are given below.

### For finite measures

**Constructing an extended-valued candidate** First, suppose μ and ν are both finite-valued nonnegative measures. Let F be the set of those extended-value measurable functions *f*  : *X* → [0, ∞] such that:

$\forall A\in \Sigma :\qquad \int _{A}f\,d\mu \leq \nu (A)$

*F* ≠ ∅, since it contains at least the zero function. Now let *f*1,  *f*2 ∈ *F*, and suppose A is an arbitrary measurable set, and define:

${\begin{aligned}A_{1}&=\left\{x\in A:f_{1}(x)>f_{2}(x)\right\},\\A_{2}&=\left\{x\in A:f_{2}(x)\geq f_{1}(x)\right\}.\end{aligned}}$

Then one has

$\int _{A}\max \left\{f_{1},f_{2}\right\}\,d\mu =\int _{A_{1}}f_{1}\,d\mu +\int _{A_{2}}f_{2}\,d\mu \leq \nu \left(A_{1}\right)+\nu \left(A_{2}\right)=\nu (A),$

and therefore, max{ *f* 1,  *f* 2} ∈ *F*.

Now, let { *fn* } be a sequence of functions in F such that

$\lim _{n\to \infty }\int _{X}f_{n}\,d\mu =\sup _{f\in F}\int _{X}f\,d\mu .$

By replacing  *fn*  with the maximum of the first n functions, one can assume that the sequence { *fn* } is increasing. Let g be an extended-valued function defined as

$g(x):=\lim _{n\to \infty }f_{n}(x).$

By Lebesgue's monotone convergence theorem, one has

$\lim _{n\to \infty }\int _{A}f_{n}\,d\mu =\int _{A}\lim _{n\to \infty }f_{n}(x)\,d\mu (x)=\int _{A}g\,d\mu \leq \nu (A)$

for each *A* ∈ Σ, and hence, *g* ∈ *F*. Also, by the construction of g,

$\int _{X}g\,d\mu =\sup _{f\in F}\int _{X}f\,d\mu .$

**Proving equality** Now, since *g* ∈ *F*,

$\nu _{0}(A):=\nu (A)-\int _{A}g\,d\mu$

defines a nonnegative measure on Σ. To prove equality, we show that *ν*0 = 0.

Suppose ν0 ≠ 0; then, since μ is finite, there is an *ε* > 0 such that *ν*0(*X*) > *ε μ*(*X*). To derive a contradiction from ν0 ≠ 0, we look for a positive set *P* ∈ Σ for the signed measure *ν*0 − *ε μ* (i.e. a measurable set P, all of whose measurable subsets have non-negative *ν*0 − *εμ* measure), where also P has positive μ-measure. Conceptually, we're looking for a set P, where *ν*0 ≥ *ε μ* in every part of P. A convenient approach is to use the Hahn decomposition (*P*, *N*) for the signed measure *ν*0 − *ε μ*.

Note then that for every *A* ∈ Σ one has *ν*0(*A* ∩ *P*) ≥ *ε μ*(*A* ∩ *P*), and hence,

${\begin{aligned}\nu (A)&=\int _{A}g\,d\mu +\nu _{0}(A)\\&\geq \int _{A}g\,d\mu +\nu _{0}(A\cap P)\\&\geq \int _{A}g\,d\mu +\varepsilon \mu (A\cap P)=\int _{A}\left(g+\varepsilon 1_{P}\right)\,d\mu ,\end{aligned}}$

where 1*P* is the indicator function of P. Also, note that *μ*(*P*) > 0 as desired; for if *μ*(*P*) = 0, then (since ν is absolutely continuous in relation to μ) *ν*0(*P*) ≤ *ν*(*P*) = 0, so *ν*0(*P*) = 0 and

$\nu _{0}(X)-\varepsilon \mu (X)=\left(\nu _{0}-\varepsilon \mu \right)(N)\leq 0,$

contradicting the fact that *ν*0(*X*) > *εμ*(*X*).

Then, since also

$\int _{X}\left(g+\varepsilon 1_{P}\right)\,d\mu \leq \nu (X)<+\infty ,$

*g* + *ε* 1*P* ∈ *F* and satisfies

$\int _{X}\left(g+\varepsilon 1_{P}\right)\,d\mu >\int _{X}g\,d\mu =\sup _{f\in F}\int _{X}f\,d\mu .$

This is impossible because it violates the definition of a supremum; therefore, the initial assumption that *ν*0 ≠ 0 must be false. Hence, *ν*0 = 0, as desired.

**Restricting to finite values** Now, since g is μ-integrable, the set {*x* ∈ *X* : *g*(*x*) = ∞} is μ-null. Therefore, if a  *f*  is defined as

$f(x)={\begin{cases}g(x)&{\text{if }}g(x)<\infty \\0&{\text{otherwise,}}\end{cases}}$

then *f* has the desired properties.

**Uniqueness** As for the uniqueness, let  *f*, *g* : *X* → [0, ∞) be measurable functions satisfying

$\nu (A)=\int _{A}f\,d\mu =\int _{A}g\,d\mu$

for every measurable set A. Then, *g* − *f*  is μ-integrable, and

$\int _{A}(g-f)\,d\mu =0.$

(Recall that we can split the integral into two as long as they are measurable and non-negative)

In particular, for *A* = {*x* ∈ *X* : *f*(*x*) > *g*(*x*)}, or {*x* ∈ *X* : *f*(*x*) < *g*(*x*)}. It follows that

$\int _{X}(g-f)^{+}\,d\mu =0=\int _{X}(g-f)^{-}\,d\mu ,$

and so, that (*g* − *f* )+ = 0 μ-almost everywhere; the same is true for (*g* − *f* )−, and thus, *f* = *g* μ-almost everywhere, as desired.

### For σ-finite positive measures

If μ and ν are σ-finite, then X can be written as the union of a sequence {*Bn*}*n* of disjoint sets in Σ, each of which has finite measure under both μ and ν. For each n, by the finite case, there is a Σ-measurable function  *fn*  : *Bn* → [0, ∞) such that

$\nu _{n}(A)=\int _{A}f_{n}\,d\mu$

for each Σ-measurable subset A of *Bn*. The sum ${\textstyle \left(\sum _{n}f_{n}1_{B_{n}}\right):=f}$ of those functions is then the required function such that ${\textstyle \nu (A)=\int _{A}f\,d\mu }$ .

As for the uniqueness, since each of the *fn* is μ-almost everywhere unique, so is *f*.

### For signed and complex measures

If ν is a σ-finite signed measure, then it can be Hahn–Jordan decomposed as *ν* = *ν*+ − *ν*− where one of the measures is finite. Applying the previous result to those two measures, one obtains two functions, *g*, *h* : *X* → [0, ∞), satisfying the Radon–Nikodym theorem for *ν*+ and *ν*− respectively, at least one of which is μ-integrable (i.e., its integral with respect to μ is finite). It is clear then that *f* = *g* − *h* satisfies the required properties, including uniqueness, since both g and h are unique up to μ-almost everywhere equality.

If ν is a complex measure, it can be decomposed as *ν* = *ν*1 + *iν*2, where both *ν*1 and *ν*2 are finite-valued signed measures. Applying the above argument, one obtains two functions, *g*, *h* : *X* → [0, ∞), satisfying the required properties for *ν*1 and *ν*2, respectively. Clearly, *f* = *g* + *ih* is the required function.

## The Lebesgue decomposition theorem

Lebesgue's decomposition theorem shows that the assumptions of the Radon–Nikodym theorem can be found even in a situation which is seemingly more general. Consider a σ-finite positive measure $\mu$ on the measure space $(X,\Sigma )$ and a σ-finite signed measure $\nu$ on $\Sigma$ , without assuming any absolute continuity. Then there exist unique signed measures $\nu _{a}$ and $\nu _{s}$ on $\Sigma$ such that $\nu =\nu _{a}+\nu _{s}$ , $\nu _{a}\ll \mu$ , and $\nu _{s}\perp \mu$ . The Radon–Nikodym theorem can then be applied to the pair $\nu _{a},\mu$ .
