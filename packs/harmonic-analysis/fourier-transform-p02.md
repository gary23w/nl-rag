---
title: "Fourier transform (part 2/4)"
source: https://en.wikipedia.org/wiki/Fourier_transform
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
part: 2/4
---

## Complex domain

The integral for the Fourier transform ${\widehat {f}}(\xi )=\int _{-\infty }^{\infty }e^{-2i\pi t\xi }f(t)\,dt$ can be studied for complex values of its argument ξ. Depending on the properties of f, this might not converge off the real axis at all, or it might converge to a complex analytic function for all values of *ξ* = *σ* + *iτ*, or something in between.

The Paley–Wiener theorem says that f is smooth (i.e., n-times differentiable for all positive integers n) and compactly supported if and only if *f̂* (*σ* + *iτ*) is a holomorphic function for which there exists a constant *a* > 0 such that for any integer *n* ≥ 0, $\left\vert \xi ^{n}{\widehat {f}}(\xi )\right\vert \leq C_{n}e^{2\pi a\vert \tau \vert }$ for some constant C_n. (In this case, f is supported on [−*a*, *a*].) This can be expressed by saying that *f̂* is an entire function that is rapidly decreasing in σ (for fixed τ) and of exponential growth in τ (uniformly in σ).

(If f is not smooth, but only *L*2, a corresponding version holds with the rapid-decrease condition replaced by the appropriate *L*2 condition.) The space of such functions of a complex variable is called the Paley–Wiener space. This theorem has been generalised to semisimple Lie groups.

If f is supported on the half-line *t* ≥ 0, then f is said to be "causal" because the impulse response function of a physically realisable filter must have this property, as no effect can precede its cause. Paley and Wiener showed that then, under suitable integrability hypotheses, *f̂* extends to a holomorphic function on the complex lower half-plane *τ* < 0 that tends to zero as τ goes to −∞. A simple converse in this form is false; precise converses require additional growth or Hardy-space hypotheses.

### Laplace transform

The Fourier transform *f̂*(*ξ*) is related to the Laplace transform *F*(*s*), which is also used for the solution of differential equations and the analysis of filters.

It may happen that a function f for which the Fourier integral does not converge on the real axis at all nevertheless has a complex Fourier transform defined in some region of the complex plane.

For example, if f is causal and of exponential growth, i.e., $f(t)=0\quad (t<0),\qquad \vert f(t)\vert <Ce^{at}\quad (t\geq 0)$ for some constants *C*, *a* ≥ 0, then ${\widehat {f}}(i\tau )=\int _{0}^{\infty }e^{2\pi \tau t}f(t)\,dt,$ convergent for all 2π*τ* < −*a*, is a one-sided Laplace transform of f.

The usual one-sided version of the Laplace transform is $F(s)=\int _{0}^{\infty }f(t)e^{-st}\,dt.$

If f is causal and the integrals converge, then ⁠ ${\widehat {f}}(i\tau )=F(-2\pi \tau )$ ⁠. Thus, extending the Fourier transform to the complex domain means it includes the Laplace transform as a special case in the case of causal functions—but with the change of variable *s* = *i*2π*ξ*.

From another, perhaps more classical viewpoint, the Laplace transform by its form involves an additional exponential regulating term that lets it converge outside of the imaginary line where the Fourier transform is defined. As such it can converge for functions and integrals with at most exponential growth in the regulated direction, whereas the original Fourier decomposition cannot, enabling analysis of systems with divergent or critical elements. Two particular examples from linear signal processing are the construction of allpass filter networks from critical comb and mitigating filters via exact pole-zero cancellation on the unit circle. Such designs are common in audio processing, where highly nonlinear phase response is sought for, as in reverb.

Furthermore, when extended pulselike impulse responses are sought for signal processing work, the easiest way to produce them is to have one circuit that produces a divergent time response, and then to cancel its divergence through a delayed opposite and compensatory response. There, only the delay circuit in-between admits a classical Fourier description, which is critical. Both the circuits to the side are unstable, and do not admit a convergent Fourier decomposition. However, they do admit a Laplace domain description, with compatible half-planes of convergence in the complex plane (or in the discrete case, the Z-plane), wherein their effects cancel.

In modern mathematics the Laplace transform is conventionally subsumed under the aegis of Fourier methods. Both of them are subsumed by the far more general, and more abstract, idea of harmonic analysis.

### Inversion

Still with ⁠ $\xi =\sigma +i\tau$ ⁠, if ${\widehat {f}}$ is complex analytic for *a* ≤ *τ* ≤ *b* and has sufficient decay in horizontal strips, then $\int _{-\infty }^{\infty }{\widehat {f}}(\sigma +ia)e^{i2\pi (\sigma +ia)t}\,d\sigma =\int _{-\infty }^{\infty }{\widehat {f}}(\sigma +ib)e^{i2\pi (\sigma +ib)t}\,d\sigma$ by Cauchy's integral theorem. Therefore, the Fourier inversion formula can use integration along different lines, parallel to the real axis.

Theorem: If *f*(*t*) = 0 for *t* < 0, and |*f*(*t*)| < *Ce**at* for some constants *C*, *a* > 0 and *t* ≥ 0, then $f(t)=\int _{-\infty }^{\infty }{\widehat {f}}(\sigma +i\tau )e^{i2\pi (\sigma +i\tau )t}\,d\sigma ,$ for any *τ* < −⁠*a*/2π⁠, under the usual hypotheses for Fourier inversion.

This theorem implies the Mellin inversion formula for the Laplace transformation, $f(t)={\frac {1}{i2\pi }}\int _{b-i\infty }^{b+i\infty }F(s)e^{st}\,ds$ for any *b* > *a*, where *F*(*s*) is the Laplace transform of *f*(*t*).

The hypotheses can be weakened, as in standard Fourier inversion results, to *f*(*t*) *e*−*at* being *L*1, provided that f be of bounded variation in a closed neighborhood of t (cf. Dini test), the value of f at t be taken to be the arithmetic mean of the left and right limits, and that the integrals be taken in the sense of Cauchy principal values.

*L*2 versions of these inversion formulas are also available.


## Fourier transform on Euclidean space

The Fourier transform can be defined in any arbitrary number of dimensions n. As with the one-dimensional case, there are many conventions. For an integrable function *f*(**x**), this article takes the definition: ${\widehat {f}}({\boldsymbol {\xi }})={\mathcal {F}}(f)({\boldsymbol {\xi }})=\int _{\mathbb {R} ^{n}}f(\mathbf {x} )e^{-i2\pi {\boldsymbol {\xi }}\cdot \mathbf {x} }\,d\mathbf {x}$ where **x** and **ξ** are n-dimensional vectors, and **x** · **ξ** is the dot product of the vectors. Alternatively, **ξ** can be viewed as belonging to the dual vector space ⁠ $\mathbb {R} ^{n\star }$ ⁠, in which case the dot product becomes the contraction of **x** and **ξ**, usually written as ⟨**x**, **ξ**⟩.

All of the basic properties listed above hold for the n-dimensional Fourier transform, as do Plancherel's and Parseval's theorem. When the function is integrable, the Fourier transform is still uniformly continuous and the Riemann–Lebesgue lemma holds.

### Uncertainty principle

Generally speaking, the more concentrated *f*(*x*) is, the more spread out its Fourier transform *f̂*(*ξ*) must be. In particular, the scaling property of the Fourier transform may be seen as saying: if we squeeze a function in x, its Fourier transform stretches out in ξ. It is not possible to arbitrarily concentrate both a function and its Fourier transform.

The trade-off between the compaction of a function and its Fourier transform can be formalized in the form of an uncertainty principle by viewing a function and its Fourier transform as conjugate variables with respect to the symplectic form on the time–frequency domain: from the point of view of the linear canonical transformation, the Fourier transform is rotation by 90° in the time–frequency domain, and preserves the symplectic form.

Suppose *f*(*x*) is an integrable and square-integrable function. Without loss of generality, assume that *f*(*x*) is normalized: $\int _{-\infty }^{\infty }|f(x)|^{2}\,dx=1.$

It follows from the Plancherel theorem that *f̂*(*ξ*) is also normalized.

The spread around *x* = 0 may be measured by the *dispersion about zero* defined by $D_{0}(f)=\int _{-\infty }^{\infty }x^{2}|f(x)|^{2}\,dx.$

In probability terms, this is the second moment of |*f*(*x*)|2 about zero.

The uncertainty principle states that, if *f*(*x*) is absolutely continuous and the functions *x*·*f*(*x*) and *f*′(*x*) are square integrable, then $D_{0}(f)D_{0}({\widehat {f}})\geq {\frac {1}{16\pi ^{2}}}.$

The equality is attained only in the case ${\begin{aligned}f(x)&=C_{1}\,e^{-\pi {\frac {x^{2}}{\sigma ^{2}}}}\\\therefore {\widehat {f}}(\xi )&=\sigma C_{1}\,e^{-\pi \sigma ^{2}\xi ^{2}}\end{aligned}}$ where *σ* > 0 is arbitrary and *C*1 = ⁠4√2/√*σ*⁠ so that f is *L*2-normalized. In other words, where f is a (normalized) Gaussian function with variance *σ*2/2π, centered at zero, and its Fourier transform is a Gaussian function with variance *σ*−2/2π. Gaussian functions are examples of Schwartz functions (see the discussion on tempered distributions below).

In fact, this inequality implies that: $\left(\int _{-\infty }^{\infty }(x-x_{0})^{2}|f(x)|^{2}\,dx\right)\left(\int _{-\infty }^{\infty }(\xi -\xi _{0})^{2}\left|{\widehat {f}}(\xi )\right|^{2}\,d\xi \right)\geq {\frac {1}{16\pi ^{2}}},\quad \forall x_{0},\xi _{0}\in \mathbb {R} .$ In quantum mechanics, the momentum and position wave functions are Fourier transform pairs, up to a factor of the Planck constant. With this constant properly taken into account, the inequality above becomes the statement of the Heisenberg uncertainty principle.

A stronger uncertainty principle is the Hirschman uncertainty principle, which is expressed as: $H\left(\left|f\right|^{2}\right)+H\left(\left|{\widehat {f}}\right|^{2}\right)\geq \log \left({\frac {e}{2}}\right)$ where *H*(*p*) is the differential entropy of the probability density function *p*(*x*): $H(p)=-\int _{-\infty }^{\infty }p(x)\log {\bigl (}p(x){\bigr )}\,dx$ where the logarithms may be in any base that is consistent. The equality is attained for a Gaussian, as in the previous case.

### Sine and cosine transforms

Fourier's original formulation of the transform did not use complex numbers, but rather sines and cosines. Statisticians and others still use this form. An absolutely integrable function f for which Fourier inversion holds can be expanded in terms of genuine frequencies (avoiding negative frequencies, which are sometimes considered hard to interpret physically) λ by $f(t)=\int _{0}^{\infty }{\bigl (}a(\lambda )\cos(2\pi \lambda t)+b(\lambda )\sin(2\pi \lambda t){\bigr )}\,d\lambda .$

This is called an expansion as a trigonometric integral, or a Fourier integral expansion. The coefficient functions a and b can be found by using variants of the Fourier cosine transform and the Fourier sine transform (the normalisations are, again, not standardised): $a(\lambda )=2\int _{-\infty }^{\infty }f(t)\cos(2\pi \lambda t)\,dt$ and $b(\lambda )=2\int _{-\infty }^{\infty }f(t)\sin(2\pi \lambda t)\,dt.$

Older literature refers to the two transform functions, the Fourier cosine transform, a, and the Fourier sine transform, b.

The function f can be recovered from the sine and cosine transform using $f(t)=2\int _{0}^{\infty }\int _{-\infty }^{\infty }f(\tau )\cos {\bigl (}2\pi \lambda (\tau -t){\bigr )}\,d\tau \,d\lambda .$ together with trigonometric identities. This is referred to as Fourier's integral formula.

### Spherical harmonics

Let the set of homogeneous harmonic polynomials of degree k on **R***n* be denoted by **A***k*. The set **A***k* consists of the solid spherical harmonics of degree k. The solid spherical harmonics play a similar role in higher dimensions to the Hermite polynomials in dimension one. Specifically, if *f*(*x*) = *e*−π|*x*|2*P*(*x*) for some *P*(*x*) in **A***k*, then ⁠ ${\widehat {f}}(\xi )=i^{-k}f(\xi )$ ⁠. Let the set **H***k* be the closure in *L*2(**R***n*) of linear combinations of functions of the form *f*(|*x*|)*P*(*x*) where *P*(*x*) is in **A***k*. The space *L*2(**R***n*) is then a direct sum of the spaces **H***k* and the Fourier transform maps each space **H***k* to itself and it is possible to characterize the action of the Fourier transform on each space **H***k*.

Let *f*(*x*) = *f*0(|*x*|)*P*(*x*) (with *P*(*x*) in **A***k*), then ${\widehat {f}}(\xi )=F_{0}(|\xi |)P(\xi )$ where $F_{0}(r)=2\pi i^{-k}r^{-{\frac {n+2k-2}{2}}}\int _{0}^{\infty }f_{0}(s)J_{\frac {n+2k-2}{2}}(2\pi rs)s^{\frac {n+2k}{2}}\,ds.$

Here *J*(*n* + 2*k* − 2)/2 denotes the Bessel function of the first kind with order ⁠*n* + 2*k* − 2/2⁠. When *k* = 0 this gives a useful formula for the Fourier transform of a radial function. This is essentially the Hankel transform. Moreover, there is a simple recursion relating the cases *n* + 2 and n allowing to compute, e.g., the three-dimensional Fourier transform of a radial function from the one-dimensional one.

### Restriction problems

In higher dimensions it becomes interesting to study *restriction problems* for the Fourier transform. The Fourier transform of an integrable function is continuous and the restriction of this function to any set is defined. But for a square-integrable function the Fourier transform could be a general *class* of square integrable functions. As such, the restriction of the Fourier transform of an *L*2(**R***n*) function cannot be defined on sets of measure 0. It is still an active area of study to understand restriction problems in *L**p* for 1 < *p* < 2. It is possible in some cases to define the restriction of a Fourier transform to a set S, provided S has non-zero curvature. The case when S is the unit sphere in **R***n* is of particular interest. In this case the Tomas–Stein restriction theorem states that the restriction of the Fourier transform to the unit sphere in **R***n* is a bounded operator on *L**p* provided 1 ≤ *p* ≤ ⁠2*n* + 2/*n* + 3⁠.

One notable difference between the Fourier transform in 1 dimension versus higher dimensions concerns the partial sum operator. Consider an increasing collection of measurable sets *E**R* indexed by *R* ∈ (0, ∞): such as balls of radius R centered at the origin, or cubes of side 2*R*. For a given integrable function f, consider the function fR defined by: $f_{R}(x)=\int _{E_{R}}{\widehat {f}}(\xi )e^{i2\pi x\cdot \xi }\,d\xi ,\quad x\in \mathbb {R} ^{n}.$

Suppose in addition that *f* ∈ *L**p*(**R***n*). For *n* = 1 and 1 < *p* < ∞, if one takes *ER* = (−*R*, *R*), then fR converges to f in *L**p* as R tends to infinity, by the boundedness of the Hilbert transform. Naively one may hope the same holds true for *n* > 1. In the case that ER is taken to be a cube with side length R, then convergence still holds. Another natural candidate is the Euclidean ball *E**R* = {*ξ* : |*ξ*| < *R*}. In order for this partial sum operator to converge, it is necessary that the multiplier for the unit ball be bounded in *L**p*(**R***n*). For *n* ≥ 2 it is a celebrated theorem of Charles Fefferman that the multiplier for the unit ball is never bounded unless *p* = 2. In fact, when *p* ≠ 2, this shows that not only may fR fail to converge to f in *L**p*, but for some functions *f* ∈ *L**p*(**R***n*), fR is not even an element of *L**p*.


## Fourier transform on function spaces

The definition of the Fourier transform naturally extends from $L^{1}(\mathbb {R} )$ to ⁠ $L^{1}(\mathbb {R} ^{n})$ ⁠. That is, if $f\in L^{1}(\mathbb {R} ^{n})$ then the Fourier transform ${\mathcal {F}}:L^{1}(\mathbb {R} ^{n})\to L^{\infty }(\mathbb {R} ^{n})$ is given by $f(x)\mapsto {\widehat {f}}(\xi )=\int _{\mathbb {R} ^{n}}f(x)e^{-i2\pi \xi \cdot x}\,dx,\quad \forall \xi \in \mathbb {R} ^{n}.$ This operator is bounded as $\sup _{\xi \in \mathbb {R} ^{n}}\left\vert {\widehat {f}}(\xi )\right\vert \leq \int _{\mathbb {R} ^{n}}\vert f(x)\vert \,dx,$ which shows that its operator norm is bounded by 1. The Riemann–Lebesgue lemma shows that if $f\in L^{1}(\mathbb {R} ^{n})$ then its Fourier transform actually belongs to the space of continuous functions that vanish at infinity, i.e., ⁠ ${\widehat {f}}\in C_{0}(\mathbb {R} ^{n})\subset L^{\infty }(\mathbb {R} ^{n})$ ⁠. Furthermore, the image of $L^{1}$ under ${\mathcal {F}}$ is a strict subset of ⁠ $C_{0}(\mathbb {R} ^{n})$ ⁠.

Similarly to the case of one variable, the Fourier transform can be defined on ⁠ $L^{2}(\mathbb {R} ^{n})$ ⁠. The Fourier transform in $L^{2}(\mathbb {R} ^{n})$ is no longer given by an ordinary Lebesgue integral, although it can be computed by an improper integral, i.e., ${\widehat {f}}(\xi )=\lim _{R\to \infty }\int _{|x|\leq R}f(x)e^{-i2\pi \xi \cdot x}\,dx$ where the limit is taken in the *L*2 sense.

Furthermore, ${\mathcal {F}}:L^{2}(\mathbb {R} ^{n})\to L^{2}(\mathbb {R} ^{n})$ is a unitary operator. For an operator to be unitary it is sufficient to show that it is bijective and preserves the inner product. The Fourier inversion theorem implies that the transform is bijective. Also, for any *f*, *g* ∈ *L*2(**R***n*) we have $\int _{\mathbb {R} ^{n}}f(x){\mathcal {F}}g(x)\,dx=\int _{\mathbb {R} ^{n}}{\mathcal {F}}f(x)g(x)\,dx.$ So ${\begin{aligned}\int _{\mathbb {R} ^{n}}{\overline {{\mathcal {F}}f(x)}}{\mathcal {F}}g(x)\,dx&=\int _{\mathbb {R} ^{n}}{\mathcal {F}}^{-1}{\overline {f(x)}}{\mathcal {F}}g(x)\,dx\\&=\int _{\mathbb {R} ^{n}}{\mathcal {F}}{\mathcal {F}}^{-1}{\overline {f(x)}}g(x)\,dx=\int _{\mathbb {R} ^{n}}{\overline {f(x)}}g(x)\,dx\end{aligned}}$

So the transform preserves the inner product.

### On other *L**p*

For ⁠ $1<p<2$ ⁠, the Fourier transform can be defined on $L^{p}(\mathbb {R} )$ by Riesz–Thorin interpolation, which amounts to decomposing such functions into a fat tail part $|f|\leq 1$ in *L*2 plus a fat body part $|f|>1$ in *L*1. In each of these spaces, the Fourier transform of a function in *L**p*(**R***n*) is in *L**q*(**R***n*), where *q* = ⁠*p*/*p* − 1⁠ is the Hölder conjugate of p (by the Hausdorff–Young inequality). However, except for *p* = 2, the image is not easily characterized. Further extensions become more technical. The Fourier transform of functions in *L**p* for the range 2 < *p* < ∞ requires the study of distributions. In fact, it can be shown that there are functions in *L**p* with *p* > 2 so that the Fourier transform is not defined as a function.

### Tempered distributions

One might consider enlarging the domain of the Fourier transform from $L^{1}+L^{2}$ by considering generalized functions, or distributions. A distribution on $\mathbb {R} ^{n}$ is a continuous linear functional on the space $C_{c}^{\infty }(\mathbb {R} ^{n})$ of compactly supported smooth functions (i.e. bump functions), equipped with a suitable topology. Since $C_{c}^{\infty }(\mathbb {R} ^{n})$ is dense in ⁠ $L^{2}(\mathbb {R} ^{n})$ ⁠, the Plancherel theorem allows one to extend the definition of the Fourier transform to general functions in $L^{2}(\mathbb {R} ^{n})$ by continuity arguments. The strategy is then to consider the action of the Fourier transform on $C_{c}^{\infty }(\mathbb {R} ^{n})$ and pass to distributions by duality. The obstruction to doing this is that the Fourier transform does not map $C_{c}^{\infty }(\mathbb {R} ^{n})$ to ⁠ $C_{c}^{\infty }(\mathbb {R} ^{n})$ ⁠. In fact the Fourier transform of an element in $C_{c}^{\infty }(\mathbb {R} ^{n})$ can not vanish on an open set; see the above discussion on the uncertainty principle.

The Fourier transform can also be defined for tempered distributions ⁠ ${\mathcal {S}}'(\mathbb {R} ^{n})$ ⁠, dual to the space of Schwartz functions ⁠ ${\mathcal {S}}(\mathbb {R} ^{n})$ ⁠. A Schwartz function is a smooth function that decays at infinity, along with all of its derivatives, hence $C_{c}^{\infty }(\mathbb {R} ^{n})\subset {\mathcal {S}}(\mathbb {R} ^{n})$ and: ${\mathcal {F}}:C_{c}^{\infty }(\mathbb {R} ^{n})\rightarrow {\mathcal {S}}(\mathbb {R} ^{n})\setminus C_{c}^{\infty }(\mathbb {R} ^{n}).$ The Fourier transform is an automorphism of the Schwartz space and, by duality, also an automorphism of the space of tempered distributions. The tempered distributions include well-behaved functions of polynomial growth, distributions of compact support as well as all the integrable functions mentioned above.

For the definition of the Fourier transform of a tempered distribution, let f and g be integrable functions, and let ${\widehat {f}}$ and ${\widehat {g}}$ be their Fourier transforms respectively. Then the Fourier transform obeys the following multiplication formula, $\int _{\mathbb {R} ^{n}}{\widehat {f}}(x)g(x)\,dx=\int _{\mathbb {R} ^{n}}f(x){\widehat {g}}(x)\,dx.$

Every integrable function f defines (induces) a distribution $T_{f}$ by the relation $T_{f}(\varphi )=\int _{\mathbb {R} ^{n}}f(x)\varphi (x)\,dx,\quad \forall \varphi \in {\mathcal {S}}(\mathbb {R} ^{n}).$ So it makes sense to define the Fourier transform of a tempered distribution $T_{f}\in {\mathcal {S}}'(\mathbb {R} )$ by the duality: $\langle {\widehat {T}}_{f},\varphi \rangle =\langle T_{f},{\widehat {\varphi }}\rangle ,\quad \forall \varphi \in {\mathcal {S}}(\mathbb {R} ^{n}).$ Extending this to all tempered distributions T gives the general definition of the Fourier transform.

Distributions can be differentiated and the above-mentioned compatibility of the Fourier transform with differentiation and convolution remains true for tempered distributions.


## Generalizations

### Fourier–Stieltjes transform on measurable spaces

The Fourier transform of a finite Borel measure μ on **R***n*, given by the bounded, uniformly continuous function: ${\widehat {\mu }}(\xi )=\int _{\mathbb {R} ^{n}}e^{-i2\pi x\cdot \xi }\,d\mu ,$ is called the *Fourier–Stieltjes transform* due to its connection with the Riemann-Stieltjes integral representation of (Radon) measures. If $\mu$ is the probability distribution of a random variable X then its Fourier–Stieltjes transform is, by definition, a characteristic function. If, in addition, the probability distribution has a probability density function, this definition is subject to the usual Fourier transform. Stated more generally, when $\mu$ is absolutely continuous with respect to the Lebesgue measure, i.e., $d\mu =f(x)\,dx,$ then ${\widehat {\mu }}(\xi )={\widehat {f}}(\xi ),$ and the Fourier-Stieltjes transform reduces to the usual definition of the Fourier transform. That is, the notable difference with the Fourier transform of integrable functions is that the Fourier-Stieltjes transform need not vanish at infinity, i.e., the Riemann–Lebesgue lemma fails for measures.

Bochner's theorem characterizes which functions may arise as the Fourier–Stieltjes transform of a positive measure on the circle.

One example of a finite Borel measure that is not a function is the Dirac measure. Its Fourier transform is a constant function (whose value depends on the form of the Fourier transform used).

### Locally compact abelian groups

The Fourier transform may be generalized to any locally compact abelian group, i.e., an abelian group that is also a locally compact Hausdorff space such that the group operation is continuous. If G is a locally compact abelian group, it has a translation invariant measure μ, called Haar measure. For a locally compact abelian group G, the set of irreducible, i.e. one-dimensional, unitary representations are called its characters. With its natural group structure and the topology of uniform convergence on compact sets (that is, the topology induced by the compact-open topology on the space of all continuous functions from G to the circle group), the set of characters Ĝ is itself a locally compact abelian group, called the *Pontryagin dual* of G. For a function f in *L*1(*G*), its Fourier transform is defined by ${\widehat {f}}(\xi )=\int _{G}{\overline {\xi (x)}}f(x)\,d\mu \quad {\text{for any }}\xi \in {\widehat {G}}.$

The Riemann–Lebesgue lemma holds in this case; *f̂*(*ξ*) is a function vanishing at infinity on Ĝ.

The Fourier transform on T = R/Z is an example; here T is a locally compact abelian group, and the Haar measure μ on T can be thought of as the Lebesgue measure on [0,1). Consider a representation of T on the complex plane C thought of as a 1-dimensional complex vector space. There is a group of such representations (which are irreducible since C is 1-dim) $\{e_{k}:T\rightarrow GL_{1}(C)=C^{*}\mid k\in Z\}$ where $e_{k}(x)=e^{i2\pi kx}$ for ⁠ $x\in T$ ⁠.

The character of such representation, that is the trace of $e_{k}(x)$ (thought of as a one-by-one matrix) for each $x\in T$ and ⁠ $k\in Z$ ⁠, is $e^{i2\pi kx}$ itself. Now, in the case of representations of finite groups, the character table of a group G consists of rows of vectors such that each row is the character of one irreducible representation of G, and these vectors form an orthonormal basis of the space of class (meaning conjugation-invariant) functions that map from G to C by Schur's lemma. The group T is no longer finite but still compact, and it preserves the orthonormality of the character table. Each row of the table is the function $e_{k}(x)$ of ⁠ $x\in T$ ⁠, and the inner product between two class functions (all functions being class functions since T is abelian) $f,g\in L^{2}(T,d\mu )$ is defined as ${\textstyle \langle f,g\rangle ={\frac {1}{|T|}}\int _{[0,1)}f(y){\overline {g}}(y)d\mu (y)}$ with the normalizing factor ⁠ $\vert T\vert =1$ ⁠. The sequence $\{e_{k}\mid k\in Z\}$ is an orthonormal basis of the space of class functions ⁠ $L^{2}(T,d\mu )$ ⁠.

For any representation V of a finite group G, $\chi _{v}$ can be expressed as the span ${\textstyle \sum _{i}\left\langle \chi _{v},\chi _{v_{i}}\right\rangle \chi _{v_{i}}}$ ( $V_{i}$ are the irreducible representations of G), such that ⁠ $\textstyle \left\langle \chi _{v},\chi _{v_{i}}\right\rangle ={\frac {1}{\vert G\vert }}\sum _{g\in G}\chi _{v}(g){\overline {\chi }}_{v_{i}}(g)$ ⁠. Similarly for $G=T$ and ⁠ $f\in L^{2}(T,d\mu )$ ⁠, ⁠ $\textstyle f(x)=\sum _{k\in Z}{\widehat {f}}(k)e_{k}$ ⁠. The Pontriagin dual ${\widehat {T}}$ is $\{e_{k}\}(k\in Z)$ and for ⁠ $f\in L^{2}(T,d\mu )$ ⁠, ${\textstyle {\widehat {f}}(k)={\frac {1}{|T|}}\int _{[0,1)}f(y)e^{-i2\pi ky}dy}$ is its Fourier transform for ⁠ $e_{k}\in {\widehat {T}}$ ⁠.

### Gelfand transform

The Fourier transform is also a special case of the Gelfand transform. In this particular context, it is closely related to the Pontryagin duality map defined above.

Given an abelian locally compact Hausdorff topological group G, as before we consider the space *L*1(*G*), defined using a Haar measure. With convolution as multiplication, *L*1(*G*) is an abelian Banach algebra. It also has an involution * given by $f^{*}(g)={\overline {f\left(g^{-1}\right)}}.$

Taking the completion with respect to the largest possible *C**-norm gives its enveloping *C**-algebra, called the group *C**-algebra *C**(*G*) of G. (Any *C**-norm on *L*1(*G*) is bounded by the *L*1 norm, therefore their supremum exists.)

Given any abelian *C**-algebra A, the Gelfand transform gives an isomorphism between A and *C*0(*A*^), where *A*^ is the multiplicative linear functionals, i.e. one-dimensional representations, on A with the weak-* topology. The map is simply given by $a\mapsto {\bigl (}\varphi \mapsto \varphi (a){\bigr )}.$ It turns out that the multiplicative linear functionals of *C**(*G*), after suitable identification, are exactly the characters of G, and the Gelfand transform, when restricted to the dense subset *L*1(*G*), is the Fourier–Pontryagin transform.

### Compact non-abelian groups

The Fourier transform can also be defined for functions on a non-abelian group, provided that the group is compact. Removing the assumption that the underlying group is abelian, irreducible unitary representations need not always be one-dimensional. This means the Fourier transform on a non-abelian group takes values as Hilbert space operators. The Fourier transform on compact groups is a major tool in representation theory and non-commutative harmonic analysis.

Let G be a compact Hausdorff topological group, and let λ be its normalized Haar measure. Let Σ denote the collection of all isomorphism classes of finite-dimensional irreducible unitary representations, along with a definite choice of representation *U*(*σ*) on the Hilbert space *Hσ* of finite dimension *dσ* for each *σ* ∈ Σ.

For *f* ∈ *L*1(*G*), the Fourier transform of f at σ is the operator on *Hσ* defined by ${\widehat {f}}(\sigma )=\int _{G}f(g)U_{g^{-1}}^{(\sigma )}\,d\lambda (g).$ Equivalently, $\left\langle {\widehat {f}}(\sigma )\xi ,\eta \right\rangle _{H_{\sigma }}=\int _{G}f(g)\left\langle U_{g^{-1}}^{(\sigma )}\xi ,\eta \right\rangle \,d\lambda (g).$ Since *U*(*σ*) is unitary, this may also be written using the adjoint ${U^{(\sigma )}}_{g}^{*}$ .

If μ is a finite complex Borel measure on G, then the Fourier–Stieltjes transform of μ is the operator on *Hσ* defined by ${\widehat {\mu }}(\sigma )=\int _{G}U_{g^{-1}}^{(\sigma )}\,d\mu (g),$ or, weakly, $\left\langle {\widehat {\mu }}(\sigma )\xi ,\eta \right\rangle _{H_{\sigma }}=\int _{G}\left\langle U_{g^{-1}}^{(\sigma )}\xi ,\eta \right\rangle \,d\mu (g).$ If μ is absolutely continuous with respect to λ, represented as $d\mu =f\,d\lambda$ for some *f* ∈ *L*1(*G*), one identifies the Fourier transform of f with the Fourier–Stieltjes transform of μ.

The mapping $\mu \mapsto {\widehat {\mu }}$ is injective and sends finite measures to bounded fields of operators (\widehat\mu(\sigma))σ∈Σ, with $\sup _{\sigma \in \Sigma }\|{\widehat {\mu }}(\sigma )\|\leq \|\mu \|.$ Thus it may be viewed as a representation of the Banach algebra *M*(*G*) of finite Borel measures, with multiplication given by convolution of measures. With the convention above, convolution corresponds to operator multiplication with the order reversed: ${\widehat {\mu *\nu }}(\sigma )={\widehat {\nu }}(\sigma ){\widehat {\mu }}(\sigma ).$ Using the alternative convention \widehat f(\sigma)=\int_G f(g)U^{(\sigma)}_g\,d\lambda(g) reverses this order. The involution on *M*(*G*) is given, for absolutely continuous measures, by $f^{*}(g)={\overline {f(g^{-1})}},$ since compact groups are unimodular.

The Peter–Weyl theorem holds, and a version of the Fourier inversion formula follows: if *f* ∈ *L*2(*G*), then $f(g)=\sum _{\sigma \in \Sigma }d_{\sigma }\operatorname {tr} \left({\widehat {f}}(\sigma )U_{g}^{(\sigma )}\right),$ where the summation is understood as convergent in the *L*2 sense. The corresponding Plancherel formula is $\|f\|_{2}^{2}=\sum _{\sigma \in \Sigma }d_{\sigma }\|{\widehat {f}}(\sigma )\|_{\mathrm {HS} }^{2},$ where ||·||HS denotes the Hilbert–Schmidt norm.

The generalization of the Fourier transform to the noncommutative situation has also in part contributed to the development of noncommutative geometry. In this context, a categorical generalization of the Fourier transform to noncommutative groups is Tannaka–Krein duality, which replaces the group of characters with the category of representations. However, this is no longer simply a transform of scalar-valued functions into scalar-valued functions.


## Alternatives

In signal processing terms, a function (of time) is a representation of a signal with perfect *time resolution*, but no frequency information, while the Fourier transform has perfect *frequency resolution*, but no time information: the magnitude of the Fourier transform at a point is how much frequency content there is, but location is only given by phase (argument of the Fourier transform at a point), and standing waves are not localized in time – a sine wave continues out to infinity, without decaying. This limits the usefulness of the Fourier transform for analyzing signals that are localized in time, notably transients, or any signal of finite extent.

As alternatives to the Fourier transform, in time–frequency analysis, one uses time–frequency transforms or time–frequency distributions to represent signals in a form that has some time information and some frequency information – by the uncertainty principle, there is a trade-off between these. These can be generalizations of the Fourier transform, such as the short-time Fourier transform, fractional Fourier transform, synchrosqueezing Fourier transform, or other functions to represent signals, as in wavelet transforms and chirplet transforms, with the wavelet analog of the Fourier transform being the continuous wavelet transform.


## Example

The following figures provide a visual illustration of how the Fourier transform's integral measures whether a frequency is present in a particular function. The first image depicts the function ⁠ $f(t)=\cos(2\pi \ 3t)\ e^{-\pi t^{2}}$ ⁠, which is a 3 Hz cosine wave (the first term) shaped by a Gaussian envelope function (the second term) that smoothly turns the wave on and off. The next 2 images show the product ⁠ $f(t)e^{-i2\pi 3t}$ ⁠, which must be integrated to calculate the Fourier transform at +3 Hz. The real part of the integrand has a non-negative average value, because the alternating signs of $f(t)$ and $\operatorname {Re} (e^{-i2\pi 3t})$ oscillate at the same rate and in phase, whereas $f(t)$ and $\operatorname {Im} (e^{-i2\pi 3t})$ oscillate at the same rate but with orthogonal phase. The absolute value of the Fourier transform at +3 Hz is 0.5, which is relatively large. When added to the Fourier transform at -3 Hz (which is identical because we started with a real signal), we find that the amplitude of the 3 Hz frequency component is 1.

However, when you try to measure a frequency that is not present, both the real and imaginary component of the integral vary rapidly between positive and negative values. For instance, the red curve is looking for 5 Hz. The absolute value of its integral is nearly zero, indicating that almost no 5 Hz component was in the signal. The general situation is usually more complicated than this, but heuristically this is how the Fourier transform measures how much of an individual frequency is present in a function ⁠ $f(t)$ ⁠.

- (Real and imaginary parts of the integrand for its Fourier transform at +5 Hz.) Real and imaginary parts of the integrand for its Fourier transform at +5 Hz.
- (Magnitude of its Fourier transform, with +3 and +5 Hz labeled.) Magnitude of its Fourier transform, with +3 and +5 Hz labeled.

To re-enforce an earlier point, the reason for the response at $\xi =-3$ Hz is because $\cos(2\pi 3t)$ and $\cos(2\pi (-3)t)$ are indistinguishable. The transform of   $e^{i2\pi 3t}\cdot e^{-\pi t^{2}}$   would have just one response, whose amplitude is the integral of the smooth envelope: ⁠ $e^{-\pi t^{2}}$ ⁠, whereas   $\operatorname {Re} (f(t)\cdot e^{-i2\pi 3t})$ is ⁠ $e^{-\pi t^{2}}(1+\cos(2\pi 6t))/2$ ⁠.
