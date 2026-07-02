---
title: "Uncertainty principle (part 2/2)"
source: https://en.wikipedia.org/wiki/Uncertainty_principle
domain: quantum-mechanics
license: CC-BY-SA-4.0
tags: quantum mechanics, schrodinger equation, wave function, uncertainty principle
fetched: 2026-07-02
part: 2/2
---

## Harmonic analysis

In the context of harmonic analysis the uncertainty principle implies that one cannot at the same time localize the value of a function and its Fourier transform. To wit, the following inequality holds, $\left(\int _{-\infty }^{\infty }x^{2}|f(x)|^{2}\,dx\right)\left(\int _{-\infty }^{\infty }\xi ^{2}|{\hat {f}}(\xi )|^{2}\,d\xi \right)\geq {\frac {\|f\|_{2}^{4}}{16\pi ^{2}}}.$

Further mathematical uncertainty inequalities, including the above entropic uncertainty, hold between a function f and its Fourier transform ƒ̂: $H_{x}+H_{\xi }\geq \log(e/2)$

### Signal processing

In the context of time–frequency analysis uncertainty principles are referred to as the **Gabor limit**, after Dennis Gabor, or sometimes the *Heisenberg–Gabor limit*. The basic result, which follows from "Benedicks's theorem", below, is that a function cannot be both time limited and band limited (a function and its Fourier transform cannot both have bounded domain)—see bandlimited versus timelimited. More accurately, the *time-bandwidth* or *duration-bandwidth* product satisfies $\sigma _{t}\sigma _{f}\geq {\frac {1}{4\pi }}\approx 0.08{\text{ cycles}},$ where $\sigma _{t}$ and $\sigma _{f}$ are the standard deviations of the time and frequency energy concentrations respectively. The minimum is attained for a Gaussian-shaped pulse (Gabor wavelet) [For the un-squared Gaussian (i.e. signal amplitude) and its un-squared Fourier transform magnitude $\sigma _{t}\sigma _{f}=1/2\pi$ ; squaring reduces each $\sigma$ by a factor ${\sqrt {2}}$ .] Another common measure is the product of the time and frequency full width at half maximum (of the power/energy), which for the Gaussian equals $2\ln 2/\pi \approx 0.44$ (see bandwidth-limited pulse).

Stated differently, one cannot simultaneously sharply localize a signal f in both the time domain and frequency domain.

When applied to filters, the result implies that one cannot simultaneously achieve a high temporal resolution and high frequency resolution at the same time; a concrete example are the resolution issues of the short-time Fourier transform—if one uses a wide window, one achieves good frequency resolution at the cost of temporal resolution, while a narrow window has the opposite trade-off.

Alternate theorems give more precise quantitative results, and, in time–frequency analysis, rather than interpreting the (1-dimensional) time and frequency domains separately, one instead interprets the limit as a lower limit on the support of a function in the (2-dimensional) time–frequency plane. In practice, the Gabor limit limits the *simultaneous* time–frequency resolution one can achieve without interference; it is possible to achieve higher resolution, but at the cost of different components of the signal interfering with each other.

As a result, in order to analyze signals where the transients are important, the wavelet transform is often used instead of the Fourier.

### Discrete Fourier transform

Let $\left\{\mathbf {x_{n}} \right\}:=x_{0},x_{1},\ldots ,x_{N-1}$ be a sequence of *N* complex numbers and $\left\{\mathbf {X_{k}} \right\}:=X_{0},X_{1},\ldots ,X_{N-1},$ be its discrete Fourier transform.

Denote by $\|x\|_{0}$ the number of non-zero elements in the time sequence $x_{0},x_{1},\ldots ,x_{N-1}$ and by $\|X\|_{0}$ the number of non-zero elements in the frequency sequence $X_{0},X_{1},\ldots ,X_{N-1}$ . Then, $\|x\|_{0}\cdot \|X\|_{0}\geq N.$

This inequality is sharp, with equality achieved when *x* or *X* is a Dirac mass, or more generally when *x* is a nonzero multiple of a Dirac comb supported on a subgroup of the integers modulo *N* (in which case *X* is also a Dirac comb supported on a complementary subgroup, and vice versa).

More generally, if *T* and *W* are subsets of the integers modulo *N*, let $L_{T},R_{W}:\ell ^{2}(\mathbb {Z} /N\mathbb {Z} )\to \ell ^{2}(\mathbb {Z} /N\mathbb {Z} )$ denote the time-limiting operator and band-limiting operators, respectively. Then $\|L_{T}R_{W}\|^{2}\leq {\frac {|T||W|}{|G|}}$ where the norm is the operator norm of operators on the Hilbert space $\ell ^{2}(\mathbb {Z} /N\mathbb {Z} )$ of functions on the integers modulo *N*. This inequality has implications for signal reconstruction.

When *N* is a prime number, a stronger inequality holds: $\|x\|_{0}+\|X\|_{0}\geq N+1.$ Discovered by Terence Tao, this inequality is also sharp.

### Benedicks's theorem

Amrein–Berthier and Benedicks's theorem intuitively says that the set of points where f is non-zero and the set of points where ƒ̂ is non-zero cannot both be small.

Specifically, it is impossible for a function f in *L*2(**R**) and its Fourier transform ƒ̂ to both be supported on sets of finite Lebesgue measure. A more quantitative version is $\|f\|_{L^{2}(\mathbf {R} ^{d})}\leq Ce^{C|S||\Sigma |}{\bigl (}\|f\|_{L^{2}(S^{c})}+\|{\hat {f}}\|_{L^{2}(\Sigma ^{c})}{\bigr )}~.$

One expects that the factor *Ce**C*|*S*||*Σ*| may be replaced by *Ce**C*(|*S*||*Σ*|)1/*d*, which is only known if either S or Σ is convex.

### Hardy's uncertainty principle

The mathematician G. H. Hardy formulated the following uncertainty principle: it is not possible for f and ƒ̂ to both be "very rapidly decreasing". Specifically, if f in $L^{2}(\mathbb {R} )$ is such that $|f(x)|\leq C(1+|x|)^{N}e^{-a\pi x^{2}}$ and $|{\hat {f}}(\xi )|\leq C(1+|\xi |)^{N}e^{-b\pi \xi ^{2}}$ ( $C>0,N$ an integer), then, if *ab* > 1, *f* = 0, while if *ab* = 1, then there is a polynomial P of degree ≤ *N* such that $f(x)=P(x)e^{-a\pi x^{2}}.$

This was later improved as follows: if $f\in L^{2}(\mathbb {R} ^{d})$ is such that $\int _{\mathbb {R} ^{d}}\int _{\mathbb {R} ^{d}}|f(x)||{\hat {f}}(\xi )|{\frac {e^{\pi |\langle x,\xi \rangle |}}{(1+|x|+|\xi |)^{N}}}\,dx\,d\xi <+\infty ~,$ then $f(x)=P(x)e^{-\pi \langle Ax,x\rangle }~,$ where P is a polynomial of degree (*N* − *d*)/2 and A is a real *d* × *d* positive definite matrix.

This result was stated in Beurling's complete works without proof and proved in Hörmander (the case $d=1,N=0$ ) and Bonami, Demange, and Jaming for the general case. Note that Hörmander–Beurling's version implies the case *ab* > 1 in Hardy's Theorem while the version by Bonami–Demange–Jaming covers the full strength of Hardy's Theorem. A different proof of Beurling's theorem based on Liouville's theorem appeared in ref.

A full description of the case *ab* < 1 as well as the following extension to Schwartz class distributions appears in ref.

**Theorem**— If a tempered distribution $f\in {\mathcal {S}}'(\mathbb {R} ^{d})$ is such that $e^{\pi |x|^{2}}f\in {\mathcal {S}}'(\mathbb {R} ^{d})$ and $e^{\pi |\xi |^{2}}{\hat {f}}\in {\mathcal {S}}'(\mathbb {R} ^{d})~,$ then $f(x)=P(x)e^{-\pi \langle Ax,x\rangle }~,$ for some convenient polynomial P and real positive definite matrix A of type *d* × *d*.


## Additional uncertainty relations

### Heisenberg limit

In quantum metrology, and especially interferometry, the **Heisenberg limit** is the optimal rate at which the accuracy of a measurement can scale with the energy used in the measurement. Typically, this is the measurement of a phase (applied to one arm of a beam-splitter) and the energy is given by the number of photons used in an interferometer. Although some claim to have broken the Heisenberg limit, this reflects disagreement on the definition of the scaling resource. Suitably defined, the Heisenberg limit is a consequence of the basic principles of quantum mechanics and cannot be beaten, although the weak Heisenberg limit can be beaten.

### Systematic and statistical errors

The inequalities above focus on the *statistical imprecision* of observables as quantified by the standard deviation $\sigma$ . Heisenberg's original version, however, was dealing with the *systematic error*, a disturbance of the quantum system produced by the measuring apparatus, i.e., an observer effect.

If we let $\varepsilon _{A}$ represent the error (i.e., inaccuracy) of a measurement of an observable *A* and $\eta _{B}$ the disturbance produced on a subsequent measurement of the conjugate variable *B* by the former measurement of *A*, then the inequality proposed by Masanao Ozawa − encompassing both systematic and statistical errors - holds:

$\varepsilon _{A}\,\eta _{B}+\varepsilon _{A}\,\sigma _{B}+\sigma _{A}\,\eta _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

Heisenberg's uncertainty principle, as originally described in the 1927 formulation, mentions only the first term of Ozawa inequality, regarding the *systematic error*. Using the notation above to describe the *error/disturbance* effect of *sequential measurements* (first *A*, then *B*), it could be written as

$\varepsilon _{A}\,\eta _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

The formal derivation of the Heisenberg relation is possible but far from intuitive. It was *not* proposed by Heisenberg, but formulated in a mathematically consistent way only in recent years. Also, it must be stressed that the Heisenberg formulation is not taking into account the intrinsic statistical errors $\sigma _{A}$ and $\sigma _{B}$ . There is increasing experimental evidence that the total quantum uncertainty cannot be described by the Heisenberg term alone, but requires the presence of all the three terms of the Ozawa inequality.

Using the same formalism, it is also possible to introduce the other kind of physical situation, often confused with the previous one, namely the case of *simultaneous measurements* (*A* and *B* at the same time):

$\varepsilon _{A}\,\varepsilon _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

The two simultaneous measurements on *A* and *B* are necessarily *unsharp* or *weak*.

It is also possible to derive an uncertainty relation that, as the Ozawa's one, combines both the statistical and systematic error components, but keeps a form very close to the Heisenberg original inequality. By adding Robertson

$\sigma _{A}\,\sigma _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

and Ozawa relations we obtain $\varepsilon _{A}\eta _{B}+\varepsilon _{A}\,\sigma _{B}+\sigma _{A}\,\eta _{B}+\sigma _{A}\sigma _{B}\geq \left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|.$ The four terms can be written as: $(\varepsilon _{A}+\sigma _{A})\,(\eta _{B}+\sigma _{B})\,\geq \,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|.$ Defining: ${\bar {\varepsilon }}_{A}\,\equiv \,(\varepsilon _{A}+\sigma _{A})$ as the *inaccuracy* in the measured values of the variable *A* and ${\bar {\eta }}_{B}\,\equiv \,(\eta _{B}+\sigma _{B})$ as the *resulting fluctuation* in the conjugate variable *B*, Kazuo Fujikawa established an uncertainty relation similar to the Heisenberg original one, but valid both for *systematic and statistical errors*:

${\bar {\varepsilon }}_{A}\,{\bar {\eta }}_{B}\,\geq \,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

### Quantum entropic uncertainty principle

For many distributions, the standard deviation is not a particularly natural way of quantifying the structure. For example, uncertainty relations in which one of the observables is an angle has little physical meaning for fluctuations larger than one period. Other examples include highly bimodal distributions, or unimodal distributions with divergent variance.

A solution that overcomes these issues is an uncertainty based on entropic uncertainty instead of the product of variances. While formulating the many-worlds interpretation of quantum mechanics in 1957, Hugh Everett III conjectured a stronger extension of the uncertainty principle based on entropic certainty. This conjecture, also studied by I. I. Hirschman and proven in 1975 by W. Beckner and by Iwo Bialynicki-Birula and Jerzy Mycielski is that, for two normalized, dimensionless Fourier transform pairs *f*(*a*) and *g*(*b*) where

$f(a)=\int _{-\infty }^{\infty }g(b)\ e^{2\pi iab}\,db$

and

$\,\,\,g(b)=\int _{-\infty }^{\infty }f(a)\ e^{-2\pi iab}\,da$

the Shannon information entropies $H_{a}=-\int _{-\infty }^{\infty }|f(a)|^{2}\log |f(a)|^{2}\,da,$ and $H_{b}=-\int _{-\infty }^{\infty }|g(b)|^{2}\log |g(b)|^{2}\,db$ are subject to the following constraint,

$H_{a}+H_{b}\geq \log(e/2)$

where the logarithms may be in any base.

The probability distribution functions associated with the position wave function *ψ*(*x*) and the momentum wave function *φ*(*x*) have dimensions of inverse length and momentum respectively, but the entropies may be rendered dimensionless by $H_{x}=-\int |\psi (x)|^{2}\ln \left(x_{0}\,|\psi (x)|^{2}\right)dx=-\left\langle \ln \left(x_{0}\,\left|\psi (x)\right|^{2}\right)\right\rangle$ $H_{p}=-\int |\varphi (p)|^{2}\ln(p_{0}\,|\varphi (p)|^{2})\,dp=-\left\langle \ln(p_{0}\left|\varphi (p)\right|^{2})\right\rangle$ where *x*0 and *p*0 are some arbitrarily chosen length and momentum respectively, which render the arguments of the logarithms dimensionless. Note that the entropies will be functions of these chosen parameters. Due to the Fourier transform relation between the position wave function *ψ*(*x*) and the momentum wavefunction *φ*(*p*), the above constraint can be written for the corresponding entropies as

$H_{x}+H_{p}\geq \log \left({\frac {e\,h}{2\,x_{0}\,p_{0}}}\right)$

where h is the Planck constant.

Depending on one's choice of the *x0 p0* product, the expression may be written in many ways. If *x*0 *p*0 is chosen to be h, then $H_{x}+H_{p}\geq \log \left({\frac {e}{2}}\right)$

If, instead, *x*0 *p*0 is chosen to be $\hbar$ , then $H_{x}+H_{p}\geq \log(e\,\pi )$

If *x*0 and *p*0 are chosen to be unity in whatever system of units are being used, then $H_{x}+H_{p}\geq \log \left({\frac {e\,h}{2}}\right)$ where h is interpreted as a dimensionless number equal to the value of the Planck constant in the chosen system of units. Note that these inequalities can be extended to multimode quantum states, or wavefunctions in more than one spatial dimension.

The quantum entropic uncertainty principle is more restrictive than the Heisenberg uncertainty principle. From the inverse logarithmic Sobolev inequalities $H_{x}\leq {\frac {1}{2}}\log(2e\pi \sigma _{x}^{2}/x_{0}^{2})~,$ $H_{p}\leq {\frac {1}{2}}\log(2e\pi \sigma _{p}^{2}/p_{0}^{2})~,$ (equivalently, from the fact that normal distributions maximize the entropy of all such with a given variance), it readily follows that this entropic uncertainty principle is *stronger than the one based on standard deviations*, because $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}\exp \left(H_{x}+H_{p}-\log \left({\frac {e\,h}{2\,x_{0}\,p_{0}}}\right)\right)\geq {\frac {\hbar }{2}}~.$

In other words, the Heisenberg uncertainty principle, is a consequence of the quantum entropic uncertainty principle, but not vice versa. A few remarks on these inequalities. First, the choice of base e is a matter of popular convention in physics. The logarithm can alternatively be in any base, provided that it be consistent on both sides of the inequality. Second, recall the Shannon entropy has been used, *not* the quantum von Neumann entropy. Finally, the normal distribution saturates the inequality, and it is the only distribution with this property, because it is the maximum entropy probability distribution among those with fixed variance (cf. here for proof).

| Entropic uncertainty of the normal distribution |
|---|
| We demonstrate this method on the ground state of the QHO, which as discussed above saturates the usual uncertainty based on standard deviations. The length scale can be set to whatever is convenient, so we assign $x_{0}={\sqrt {\frac {\hbar }{2m\omega }}}$ ${\begin{aligned}\psi (x)&=\left({\frac {m\omega }{\pi \hbar }}\right)^{1/4}\exp {\left(-{\frac {m\omega x^{2}}{2\hbar }}\right)}\\&=\left({\frac {1}{2\pi x_{0}^{2}}}\right)^{1/4}\exp {\left(-{\frac {x^{2}}{4x_{0}^{2}}}\right)}\end{aligned}}$ The probability distribution is the normal distribution $\|\psi (x)\|^{2}={\frac {1}{x_{0}{\sqrt {2\pi }}}}\exp {\left(-{\frac {x^{2}}{2x_{0}^{2}}}\right)}$ with Shannon entropy ${\begin{aligned}H_{x}&=-\int \|\psi (x)\|^{2}\ln(\|\psi (x)\|^{2}\cdot x_{0})\,dx\\&=-{\frac {1}{x_{0}{\sqrt {2\pi }}}}\int _{-\infty }^{\infty }\exp {\left(-{\frac {x^{2}}{2x_{0}^{2}}}\right)}\ln \left[{\frac {1}{\sqrt {2\pi }}}\exp {\left(-{\frac {x^{2}}{2x_{0}^{2}}}\right)}\right]\,dx\\&={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }\exp {\left(-{\frac {u^{2}}{2}}\right)}\left[\ln({\sqrt {2\pi }})+{\frac {u^{2}}{2}}\right]\,du\\&=\ln({\sqrt {2\pi }})+{\frac {1}{2}}.\end{aligned}}$ A completely analogous calculation proceeds for the momentum distribution. Choosing a standard momentum of $p_{0}=\hbar /x_{0}$ : $\varphi (p)=\left({\frac {2x_{0}^{2}}{\pi \hbar ^{2}}}\right)^{1/4}\exp {\left(-{\frac {x_{0}^{2}p^{2}}{\hbar ^{2}}}\right)}$ $\|\varphi (p)\|^{2}={\sqrt {\frac {2x_{0}^{2}}{\pi \hbar ^{2}}}}\exp {\left(-{\frac {2x_{0}^{2}p^{2}}{\hbar ^{2}}}\right)}$ ${\begin{aligned}H_{p}&=-\int \|\varphi (p)\|^{2}\ln(\|\varphi (p)\|^{2}\cdot \hbar /x_{0})\,dp\\&=-{\sqrt {\frac {2x_{0}^{2}}{\pi \hbar ^{2}}}}\int _{-\infty }^{\infty }\exp {\left(-{\frac {2x_{0}^{2}p^{2}}{\hbar ^{2}}}\right)}\ln \left[{\sqrt {\frac {2}{\pi }}}\exp {\left(-{\frac {2x_{0}^{2}p^{2}}{\hbar ^{2}}}\right)}\right]\,dp\\&={\sqrt {\frac {2}{\pi }}}\int _{-\infty }^{\infty }\exp {\left(-2v^{2}\right)}\left[\ln \left({\sqrt {\frac {\pi }{2}}}\right)+2v^{2}\right]\,dv\\&=\ln \left({\sqrt {\frac {\pi }{2}}}\right)+{\frac {1}{2}}.\end{aligned}}$ The entropic uncertainty is therefore the limiting value ${\begin{aligned}H_{x}+H_{p}&=\ln({\sqrt {2\pi }})+{\frac {1}{2}}+\ln \left({\sqrt {\frac {\pi }{2}}}\right)+{\frac {1}{2}}\\&=1+\ln \pi =\ln(e\pi ).\end{aligned}}$ |

A measurement apparatus will have a finite resolution set by the discretization of its possible outputs into bins, with the probability of lying within one of the bins given by the Born rule. We will consider the most common experimental situation, in which the bins are of uniform size. Let *δx* be a measure of the spatial resolution. We take the zeroth bin to be centered near the origin, with possibly some small constant offset *c*. The probability of lying within the jth interval of width *δx* is $\operatorname {P} [x_{j}]=\int _{(j-1/2)\delta x-c}^{(j+1/2)\delta x-c}|\psi (x)|^{2}\,dx$

To account for this discretization, we can define the Shannon entropy of the wave function for a given measurement apparatus as $H_{x}=-\sum _{j=-\infty }^{\infty }\operatorname {P} [x_{j}]\ln \operatorname {P} [x_{j}].$

Under the above definition, the entropic uncertainty relation is $H_{x}+H_{p}>\ln \left({\frac {e}{2}}\right)-\ln \left({\frac {\delta x\delta p}{h}}\right).$

Here we note that *δx* *δp*/*h* is a typical infinitesimal phase space volume used in the calculation of a partition function. The inequality is also strict and not saturated. Efforts to improve this bound are an active area of research.

| Normal distribution example |
|---|
| We demonstrate this method first on the ground state of the QHO, which as discussed above saturates the usual uncertainty based on standard deviations. $\psi (x)=\left({\frac {m\omega }{\pi \hbar }}\right)^{1/4}\exp {\left(-{\frac {m\omega x^{2}}{2\hbar }}\right)}$ The probability of lying within one of these bins can be expressed in terms of the error function. ${\begin{aligned}\operatorname {P} [x_{j}]&={\sqrt {\frac {m\omega }{\pi \hbar }}}\int _{(j-1/2)\delta x}^{(j+1/2)\delta x}\exp \left(-{\frac {m\omega x^{2}}{\hbar }}\right)\,dx\\&={\sqrt {\frac {1}{\pi }}}\int _{(j-1/2)\delta x{\sqrt {m\omega /\hbar }}}^{(j+1/2)\delta x{\sqrt {m\omega /\hbar }}}e^{u^{2}}\,du\\&={\frac {1}{2}}\left[\operatorname {erf} \left(\left(j+{\frac {1}{2}}\right)\delta x\cdot {\sqrt {\frac {m\omega }{\hbar }}}\right)-\operatorname {erf} \left(\left(j-{\frac {1}{2}}\right)\delta x\cdot {\sqrt {\frac {m\omega }{\hbar }}}\right)\right]\end{aligned}}$ The momentum probabilities are completely analogous. $\operatorname {P} [p_{j}]={\frac {1}{2}}\left[\operatorname {erf} \left(\left(j+{\frac {1}{2}}\right)\delta p\cdot {\frac {1}{\sqrt {\hbar m\omega }}}\right)-\operatorname {erf} \left(\left(j-{\frac {1}{2}}\right)\delta x\cdot {\frac {1}{\sqrt {\hbar m\omega }}}\right)\right]$ For simplicity, we will set the resolutions to $\delta x={\sqrt {\frac {h}{m\omega }}}$ $\delta p={\sqrt {hm\omega }}$ so that the probabilities reduce to $\operatorname {P} [x_{j}]=\operatorname {P} [p_{j}]={\frac {1}{2}}\left[\operatorname {erf} \left(\left(j+{\frac {1}{2}}\right){\sqrt {2\pi }}\right)-\operatorname {erf} \left(\left(j-{\frac {1}{2}}\right){\sqrt {2\pi }}\right)\right]$ The Shannon entropy can be evaluated numerically. ${\begin{aligned}H_{x}=H_{p}&=-\sum _{j=-\infty }^{\infty }\operatorname {P} [x_{j}]\ln \operatorname {P} [x_{j}]\\&=-\sum _{j=-\infty }^{\infty }{\frac {1}{2}}\left[\operatorname {erf} \left(\left(j+{\frac {1}{2}}\right){\sqrt {2\pi }}\right)-\operatorname {erf} \left(\left(j-{\frac {1}{2}}\right){\sqrt {2\pi }}\right)\right]\ln {\frac {1}{2}}\left[\operatorname {erf} \left(\left(j+{\frac {1}{2}}\right){\sqrt {2\pi }}\right)-\operatorname {erf} \left(\left(j-{\frac {1}{2}}\right){\sqrt {2\pi }}\right)\right]\\&\approx 0.3226\end{aligned}}$ The entropic uncertainty is indeed larger than the limiting value. $H_{x}+H_{p}\approx 0.3226+0.3226=0.6452>\ln \left({\frac {e}{2}}\right)-\ln 1\approx 0.3069$ Note that despite being in the optimal case, the inequality is not saturated. |

| Sinc function example |
|---|
| An example of a unimodal distribution with infinite variance is the sinc function. If the wave function is the correctly normalized uniform distribution, $\psi (x)={\begin{cases}{1}/{\sqrt {2a}}&{\text{for }}\|x\|\leq a,\\[8pt]0&{\text{for }}\|x\|>a\end{cases}}$ then its Fourier transform is the sinc function, $\varphi (p)={\sqrt {\frac {a}{\pi \hbar }}}\cdot \operatorname {sinc} \left({\frac {ap}{\hbar }}\right)$ which yields infinite momentum variance despite having a centralized shape. The entropic uncertainty, on the other hand, is finite. Suppose for simplicity that the spatial resolution is just a two-bin measurement, *δx* = *a*, and that the momentum resolution is *δp* = *h*/*a*. Partitioning the uniform spatial distribution into two equal bins is straightforward. We set the offset *c* = 1/2 so that the two bins span the distribution. $\operatorname {P} [x_{0}]=\int _{-a}^{0}{\frac {1}{2a}}\,dx={\frac {1}{2}}$ $\operatorname {P} [x_{1}]=\int _{0}^{a}{\frac {1}{2a}}\,dx={\frac {1}{2}}$ $H_{x}=-\sum _{j=0}^{1}\operatorname {P} [x_{j}]\ln \operatorname {P} [x_{j}]=-{\frac {1}{2}}\ln {\frac {1}{2}}-{\frac {1}{2}}\ln {\frac {1}{2}}=\ln 2$ The bins for momentum must cover the entire real line. As done with the spatial distribution, we could apply an offset. It turns out, however, that the Shannon entropy is minimized when the zeroth bin for momentum is centered at the origin. (The reader is encouraged to try adding an offset.) The probability of lying within an arbitrary momentum bin can be expressed in terms of the sine integral. ${\begin{aligned}\operatorname {P} [p_{j}]&={\frac {a}{\pi \hbar }}\int _{(j-1/2)\delta p}^{(j+1/2)\delta p}\operatorname {sinc} ^{2}\left({\frac {ap}{\hbar }}\right)\,dp\\&={\frac {1}{\pi }}\int _{2\pi (j-1/2)}^{2\pi (j+1/2)}\operatorname {sinc} ^{2}(u)\,du\\&={\frac {1}{\pi }}\left[\operatorname {Si} ((4j+2)\pi )-\operatorname {Si} ((4j-2)\pi )\right]\end{aligned}}$ The Shannon entropy can be evaluated numerically. $H_{p}=-\sum _{j=-\infty }^{\infty }\operatorname {P} [p_{j}]\ln \operatorname {P} [p_{j}]=-\operatorname {P} [p_{0}]\ln \operatorname {P} [p_{0}]-2\cdot \sum _{j=1}^{\infty }\operatorname {P} [p_{j}]\ln \operatorname {P} [p_{j}]\approx 0.53$ The entropic uncertainty is indeed larger than the limiting value. $H_{x}+H_{p}\approx 0.69+0.53=1.22>\ln \left({\frac {e}{2}}\right)-\ln 1\approx 0.31$ |

### Uncertainty relation with three angular momentum components

For a particle of total angular momentum j the following uncertainty relation holds $\sigma _{J_{x}}^{2}+\sigma _{J_{y}}^{2}+\sigma _{J_{z}}^{2}\geq j,$ where $J_{l}$ are angular momentum components. The relation can be derived from $\langle J_{x}^{2}+J_{y}^{2}+J_{z}^{2}\rangle =j(j+1),$ and $\langle J_{x}\rangle ^{2}+\langle J_{y}\rangle ^{2}+\langle J_{z}\rangle ^{2}\leq j.$ The relation can be strengthened as $\sigma _{J_{x}}^{2}+\sigma _{J_{y}}^{2}+F_{Q}[\varrho ,J_{z}]/4\geq j,$ where $F_{Q}[\varrho ,J_{z}]$ is the quantum Fisher information.


## History

In 1925 Heisenberg published the *Umdeutung* (reinterpretation) paper where he showed that central aspect of quantum theory was the non-commutativity: the theory implied that the relative order of position and momentum measurement was significant. Working with Max Born and Pascual Jordan, he continued to develop matrix mechanics, that would become the first modern quantum mechanics formulation.

In March 1926, working in Bohr's institute, Heisenberg realized that the non-commutativity implies the uncertainty principle. Writing to Wolfgang Pauli in February 1927, he worked out the basic concepts.

In his celebrated 1927 paper "*Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik*" ("On the Perceptual Content of Quantum Theoretical Kinematics and Mechanics"), Heisenberg established this expression as the minimum amount of unavoidable momentum disturbance caused by any position measurement, but he did not give a precise definition for the uncertainties Δx and Δ*p*. Instead, he gave some plausible estimates in each case separately. His paper gave an analysis in terms of a microscope that Bohr showed was incorrect; Heisenberg included an addendum to the publication.

In his 1930 Chicago lecture he refined his principle:

| $\Delta x\,\Delta p\gtrsim h$ |   | A1 |
|---|---|---|

Later work broadened the concept. Any two variables that do not commute cannot be measured simultaneously—the more precisely one is known, the less precisely the other can be known. Heisenberg wrote:

> It can be expressed in its simplest form as follows: One can never know with perfect accuracy both of those two important factors which determine the movement of one of the smallest particles—its position and its velocity. It is impossible to determine accurately *both* the position and the direction and speed of a particle *at the same instant*.

Kennard in 1927 first proved the modern inequality:

| $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}$ |   | A2 |
|---|---|---|

where *ħ* = ⁠*h*/2*π*⁠, and *σx*, *σp* are the standard deviations of position and momentum. (Heisenberg only proved relation (**A2**) for the special case of Gaussian states.) In 1929 Robertson generalized the inequality to all observables and in 1930 Schrödinger extended the form to allow non-zero covariance of the operators; this result is referred to as Robertson-Schrödinger inequality.

### Terminology and translation

Throughout the main body of his original 1927 paper, written in German, Heisenberg used the word "Ungenauigkeit", (Eng: Imprecision) to describe the basic theoretical principle. Only in the endnote did he switch to the word "Unsicherheit" (Eng: Uncertainty). Later on, he always used "Unbestimmtheit" (Eng: Indefiniteness). When the English-language version of Heisenberg's textbook, *The Physical Principles of the Quantum Theory*, was published in 1930, however, only the English word "uncertainty" was used, and it became the term in the English language.

### Heisenberg's microscope

The principle is quite counter-intuitive, so the early students of quantum theory had to be reassured that naive measurements to violate it were bound always to be unworkable. One way in which Heisenberg originally illustrated the intrinsic impossibility of violating the uncertainty principle is by using the observer effect of an imaginary microscope as a measuring device.

He imagines an experimenter trying to measure the position and momentum of an electron by shooting a photon at it.

- Problem 1 – If the photon has a short wavelength, and therefore, a large momentum, the position can be measured accurately. But the photon scatters in a random direction, transferring a large and uncertain amount of momentum to the electron. If the photon has a long wavelength and low momentum, the collision does not disturb the electron's momentum very much, but the scattering will reveal its position only vaguely.
- Problem 2 – If a large aperture is used for the microscope, the electron's location can be well resolved (see Rayleigh criterion); but by the principle of conservation of momentum, the transverse momentum of the incoming photon affects the electron's beamline momentum and hence, the new momentum of the electron resolves poorly. If a small aperture is used, the accuracy of both resolutions is the other way around.

The combination of these trade-offs implies that no matter what photon wavelength and aperture size are used, the product of the uncertainty in measured position and measured momentum is greater than or equal to a lower limit, which is (up to a small numerical factor) equal to the Planck constant. Heisenberg did not care to formulate the uncertainty principle as an exact limit, and preferred to use it instead, as a heuristic quantitative statement, correct up to small numerical factors, which makes the radically new noncommutativity of quantum mechanics inevitable.

### Intrinsic quantum uncertainty

Historically, the uncertainty principle has been confused with a related effect in physics, called the observer effect, which notes that measurements of certain systems cannot be made without affecting the system, that is, without changing something in a system. Heisenberg used such an observer effect at the quantum level (see below) as a physical "explanation" of quantum uncertainty. It has since become clearer, however, that the uncertainty principle is inherent in the properties of all wave-like systems, and that it arises in quantum mechanics simply due to the matter wave nature of all quantum objects. Thus, the uncertainty principle actually states a fundamental property of quantum systems and is not a statement about the observational success of current technology.


## Critical reactions

The Copenhagen interpretation of quantum mechanics and Heisenberg's uncertainty principle were, in fact, initially seen as twin targets by detractors. According to the Copenhagen interpretation of quantum mechanics, there is no fundamental reality that the quantum state describes, just a prescription for calculating experimental results. There is no way to say what the state of a system fundamentally is, only what the result of observations might be.

Albert Einstein believed that randomness is a reflection of our ignorance of some fundamental property of reality, while Niels Bohr believed that the probability distributions are fundamental and irreducible, and depend on which measurements we choose to perform. Einstein and Bohr debated the uncertainty principle for many years.

### Ideal detached observer

Wolfgang Pauli called Einstein's fundamental objection to the uncertainty principle "the ideal of the detached observer" (phrase translated from the German):

> "Like the moon has a definite position," Einstein said to me last winter, "whether or not we look at the moon, the same must also hold for the atomic objects, as there is no sharp distinction possible between these and macroscopic objects. Observation cannot *create* an element of reality like a position, there must be something contained in the complete description of physical reality which corresponds to the *possibility* of observing a position, already before the observation has been actually made." I hope, that I quoted Einstein correctly; it is always difficult to quote somebody out of memory with whom one does not agree. It is precisely this kind of postulate which I call the ideal of the detached observer.

— Letter from Pauli to Niels Bohr, February 15, 1955

### Einstein's slit

The first of Einstein's thought experiments challenging the uncertainty principle went as follows:

> Consider a particle passing through a slit of width d. The slit introduces an uncertainty in momentum of approximately ⁠h/d⁠ because the particle passes through the wall. But let us determine the momentum of the particle by measuring the recoil of the wall. In doing so, we find the momentum of the particle to arbitrary accuracy by conservation of momentum.

Bohr's response was that the wall is quantum mechanical as well, and that to measure the recoil to accuracy Δ*p*, the momentum of the wall must be known to this accuracy before the particle passes through. This introduces an uncertainty in the position of the wall and therefore the position of the slit equal to ⁠*h*/Δ*p*⁠, and if the wall's momentum is known precisely enough to measure the recoil, the slit's position is uncertain enough to disallow a position measurement.

A similar analysis with particles diffracting through multiple slits is given by Richard Feynman.

### Einstein's box

Bohr was present when Einstein proposed the thought experiment which has become known as Einstein's box. Einstein argued that "Heisenberg's uncertainty equation implied that the uncertainty in time was related to the uncertainty in energy, the product of the two being related to the Planck constant." Consider, he said, an ideal box, lined with mirrors so that it can contain light indefinitely. The box could be weighed before a clockwork mechanism opened an ideal shutter at a chosen instant to allow one single photon to escape. "We now know, explained Einstein, precisely the time at which the photon left the box." "Now, weigh the box again. The change of mass tells the energy of the emitted light. In this manner, said Einstein, one could measure the energy emitted and the time it was released with any desired precision, in contradiction to the uncertainty principle."

Bohr spent a sleepless night considering this argument, and eventually realized that it was flawed. He pointed out that if the box were to be weighed, say by a spring and a pointer on a scale, "since the box must move vertically with a change in its weight, there will be uncertainty in its vertical velocity and therefore an uncertainty in its height above the table. ... Furthermore, the uncertainty about the elevation above the Earth's surface will result in an uncertainty in the rate of the clock", because of Einstein's own theory of gravity's effect on time. "Through this chain of uncertainties, Bohr showed that Einstein's light box experiment could not simultaneously measure exactly both the energy of the photon and the time of its escape."

### EPR paradox for entangled particles

In 1935, Einstein, Boris Podolsky and Nathan Rosen published an analysis of spatially separated entangled particles (EPR paradox). According to EPR, one could measure the position of one of the entangled particles and the momentum of the second particle, and from those measurements deduce the position and momentum of both particles to any precision, violating the uncertainty principle. In order to avoid such possibility, the measurement of one particle must modify the probability distribution of the other particle instantaneously, possibly violating the principle of locality.

In 1964, John Stewart Bell showed that this assumption can be falsified, since it would imply a certain inequality between the probabilities of different experiments. Experimental results confirm the predictions of quantum mechanics, ruling out EPR's basic assumption of local hidden variables.

### Popper's criticism

Science philosopher Karl Popper approached the problem of indeterminacy as a logician and metaphysical realist. He disagreed with the application of the uncertainty relations to individual particles rather than to ensembles of identically prepared particles, referring to them as "statistical scatter relations". In this statistical interpretation, a *particular* measurement may be made to arbitrary precision without invalidating the quantum theory.

In 1934, Popper published Zur Kritik der Ungenauigkeitsrelationen ("Critique of the Uncertainty Relations") in *Naturwissenschaften*, and in the same year *Logik der Forschung* (translated and updated by the author as *The Logic of Scientific Discovery* in 1959), outlining his arguments for the statistical interpretation. In 1982, he further developed his theory in *Quantum theory and the schism in Physics*, writing:

> [Heisenberg's] formulae are, beyond all doubt, derivable *statistical formulae* of the quantum theory. But they have been *habitually misinterpreted* by those quantum theorists who said that these formulae can be interpreted as determining some upper limit to the *precision of our measurements*. [original emphasis]

Popper proposed an experiment to falsify the uncertainty relations, although he later withdrew his initial version after discussions with Carl Friedrich von Weizsäcker, Heisenberg, and Einstein; Popper sent his paper to Einstein and it may have influenced the formulation of the EPR paradox.

### Free will

Some scientists, including Arthur Compton and Martin Heisenberg, have suggested that the uncertainty principle, or at least the general probabilistic nature of quantum mechanics, could be evidence for the two-stage model of free will. One critique, however, is that apart from the basic role of quantum mechanics as a foundation for chemistry, nontrivial biological mechanisms requiring quantum mechanics are unlikely, due to the rapid decoherence time of quantum systems at room temperature. Proponents of this theory commonly say that this decoherence is overcome by both screening and decoherence-free subspaces found in biological cells.

### Thermodynamics

There is reason to believe that violating the uncertainty principle also strongly implies the violation of the second law of thermodynamics. See Gibbs paradox.

### Rejection of the principle

Uncertainty principles relate quantum particles – electrons for example – to classical concepts – position and momentum. This presumes quantum particles have position and momentum. Edwin C. Kemble pointed out in 1937 that such properties cannot be experimentally verified and assuming they exist gives rise to many contradictions; similarly Rudolf Haag notes that position in quantum mechanics is an attribute of an interaction, say between an electron and a detector, not an intrinsic property. From this point of view the uncertainty principle is not a fundamental quantum property but a concept "carried over from the language of our ancestors", as Kemble says.


## Applications

Since the uncertainty principle is such a basic result in quantum mechanics, typical experiments in quantum mechanics routinely observe aspects of it. All forms of spectroscopy, including particle physics use the relationship to relate measured energy line-width to the lifetime of quantum states. Certain experiments, however, may deliberately test a particular form of the uncertainty principle as part of their main research program. These include, for example, tests of number–phase uncertainty relations in superconducting or quantum optics systems. Applications dependent on the uncertainty principle for their operation include extremely low-noise technology such as that required in gravitational wave interferometers.
