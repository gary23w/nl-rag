---
title: "Fourier transform (part 1/4)"
source: https://en.wikipedia.org/wiki/Fourier_transform
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
part: 1/4
---

# Fourier transform

In mathematics, the **Fourier transform** (**FT**) is an integral transform that takes a function as input and outputs another function that describes the extent to which various frequencies are present in the original function. The output of the transform is a complex valued function of frequency. The term *Fourier transform* refers to both the mathematical operation and to this complex-valued function. When a distinction needs to be made, the output of the operation is sometimes called the frequency domain representation of the original function. The Fourier transform is analogous to decomposing the sound of a musical chord into the intensities of its constituent pitches.

Functions that are localized in the time domain have Fourier transforms that are spread out across the frequency domain and vice versa, a phenomenon known as the uncertainty principle. The critical case for this principle is the Gaussian function, of substantial importance in probability theory and statistics as well as in the study of physical phenomena exhibiting normal distribution (e.g., diffusion). The Fourier transform of a Gaussian function is another Gaussian function. Joseph Fourier introduced sine and cosine transforms (which correspond to the imaginary and real components of the modern Fourier transform) in his study of heat transfer, where Gaussian functions appear as solutions of the heat equation.

The Fourier transform can be formally defined as an improper Riemann integral, making it an integral transform, although this definition is not suitable for many applications requiring a more sophisticated integration theory. For example, many relatively simple applications use the Dirac delta function, which can be treated formally as if it were a function, but the justification requires a mathematically more sophisticated viewpoint.

The Fourier transform can also be generalized to functions of several variables on Euclidean space, sending a function of 3-dimensional "position space" to a function of 3-dimensional momentum (or a function of space and time to a function of 4-momentum). This idea makes the spatial Fourier transform very natural in the study of waves, as well as in quantum mechanics, where it is important to be able to represent wave solutions as functions of either position or momentum and sometimes both. In general, functions to which Fourier methods are applicable are complex-valued, and possibly vector-valued. Still further generalization is possible to functions on groups, which, besides the original Fourier transform on **R** or **R***n*, notably includes the discrete-time Fourier transform (DTFT, group = **Z**), the discrete Fourier transform (DFT, group = **Z** mod *N*) and the Fourier series or circular Fourier transform (group = *S*1, the unit circle ≈ closed finite interval with endpoints identified). The latter is routinely employed to handle periodic functions. The fast Fourier transform (FFT) is an algorithm for computing the DFT.


## Definition

The Fourier transform of a Lebesgue integrable complex-valued function $f(x)$ on the real line, is the complex valued function ⁠ ${\widehat {f}}(\xi )$ ⁠, defined by the integral

Fourier transform

| ${\widehat {f}}(\xi )=\int _{-\infty }^{\infty }f(x)\ e^{-i2\pi \xi x}\,dx,\quad \forall \xi \in \mathbb {R} .$ |   | Eq.1 |
|---|---|---|

When $f(x)$ is (Lebesgue) integrable over the whole real line, the above integral converges for all $\xi \in \mathbb {R}$ , and ${\widehat {f}}(\xi )$ is a uniformly continuous function of $\xi$ which decays to zero as ⁠ $\xi \to \infty$ ⁠.

However, the Fourier transform can also be defined for (generalized) functions for which the Lebesgue integral **Eq.1** does not make sense. Interpreting the integral suitably (e.g. as an improper integral for locally integrable functions) extends the Fourier transform to functions that are not necessarily integrable over the whole real line. More generally, the Fourier transform also applies to generalized functions like the Dirac delta (and all other tempered distributions), in which case it is defined by duality rather than an integral.

First introduced in Fourier's *Analytical Theory of Heat*., the corresponding inversion formula for functions satisfying sufficient regularity and decay properties is given by the Fourier inversion theorem, i.e.,

Inverse transform

| $f(x)=\int _{-\infty }^{\infty }{\widehat {f}}(\xi )\ e^{i2\pi \xi x}\,d\xi ,\quad \forall x\in \mathbb {R} .$ |   | Eq.2 |
|---|---|---|

The functions f and ${\widehat {f}}$ are referred to as a **Fourier transform pair**.  A common notation for designating transform pairs is: $f(x)\ {\stackrel {\mathcal {F}}{\longleftrightarrow }}\ {\widehat {f}}(\xi ).$ For example, the Fourier transform of the delta function is the constant function ⁠ 1 ⁠: $\delta (x)\ {\stackrel {\mathcal {F}}{\longleftrightarrow }}\ 1.$

### Angular frequency (*ω*)

When the independent variable (⁠ x ⁠) represents *time* (often denoted by ⁠ t ⁠), the transform variable (⁠ $\xi$ ⁠) represents frequency (often denoted by ⁠ f ⁠). For example, if time has the unit second, then frequency has the unit hertz. The transform variable can also be written in terms of angular frequency, ⁠ $\omega =2\pi \xi$ ⁠, with the unit radian per second.

The substitution $\xi ={\tfrac {\omega }{2\pi }}$ into **Eq.1** produces this convention, where function ${\widehat {f}}$ is relabeled ⁠ ${\widehat {f}}_{1}$ ⁠: ${\begin{aligned}{\widehat {f}}_{3}(\omega )&\triangleq \int _{-\infty }^{\infty }f(x)\cdot e^{-i\omega x}\,dx={\widehat {f}}_{1}\left({\tfrac {\omega }{2\pi }}\right),\\f(x)&={\frac {1}{2\pi }}\int _{-\infty }^{\infty }{\widehat {f}}_{3}(\omega )\cdot e^{i\omega x}\,d\omega .\end{aligned}}$ Unlike the **Eq.1** definition, the Fourier transform is no longer a unitary transformation, and there is less symmetry between the formulas for the transform and its inverse. Those properties are restored by splitting the $2\pi$ factor evenly between the transform and its inverse, which leads to another convention: ${\begin{aligned}{\widehat {f}}_{2}(\omega )&\triangleq {\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }f(x)\cdot e^{-i\omega x}\,dx={\frac {1}{\sqrt {2\pi }}}\ \ {\widehat {f}}_{1}\left({\tfrac {\omega }{2\pi }}\right),\\f(x)&={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }{\widehat {f}}_{2}(\omega )\cdot e^{i\omega x}\,d\omega .\end{aligned}}$ Variations of all three conventions can be created by conjugating the complex-exponential kernel of both the forward and the reverse transform. The signs must be opposites.

| ordinary frequency ξ (Hz) | unitary | ${\begin{aligned}{\widehat {f}}_{1}(\xi )\ &\triangleq \ \int _{-\infty }^{\infty }f(x)\,e^{-i2\pi \xi x}\,dx={\sqrt {2\pi }}\ \ {\widehat {f}}_{2}(2\pi \xi )={\widehat {f}}_{3}(2\pi \xi )\\f(x)&=\int _{-\infty }^{\infty }{\widehat {f}}_{1}(\xi )\,e^{i2\pi x\xi }\,d\xi \end{aligned}}$ |
|---|---|---|
| angular frequency ω (rad/s) | unitary | ${\begin{aligned}{\widehat {f}}_{2}(\omega )\ &\triangleq \ {\frac {1}{\sqrt {2\pi }}}\ \int _{-\infty }^{\infty }f(x)\,e^{-i\omega x}\,dx={\frac {1}{\sqrt {2\pi }}}\ \ {\widehat {f}}_{1}\!\left({\frac {\omega }{2\pi }}\right)={\frac {1}{\sqrt {2\pi }}}\ \ {\widehat {f}}_{3}(\omega )\\f(x)&={\frac {1}{\sqrt {2\pi }}}\ \int _{-\infty }^{\infty }{\widehat {f}}_{2}(\omega )\,e^{i\omega x}\,d\omega \end{aligned}}$ |
| non-unitary | ${\begin{aligned}{\widehat {f}}_{3}(\omega )\ &\triangleq \ \int _{-\infty }^{\infty }f(x)\,e^{-i\omega x}\,dx={\widehat {f}}_{1}\left({\frac {\omega }{2\pi }}\right)={\sqrt {2\pi }}\ \ {\widehat {f}}_{2}(\omega )\\f(x)&={\frac {1}{2\pi }}\int _{-\infty }^{\infty }{\widehat {f}}_{3}(\omega )\,e^{i\omega x}\,d\omega \end{aligned}}$ |   |

| ordinary frequency ξ (Hz) | unitary | ${\begin{aligned}{\widehat {f}}_{1}(\xi )\ &\triangleq \ \int _{\mathbb {R} ^{n}}f(x)e^{-i2\pi \xi \cdot x}\,dx=(2\pi )^{\frac {n}{2}}{\widehat {f}}_{2}(2\pi \xi )={\widehat {f}}_{3}(2\pi \xi )\\f(x)&=\int _{\mathbb {R} ^{n}}{\widehat {f}}_{1}(\xi )e^{i2\pi \xi \cdot x}\,d\xi \end{aligned}}$ |
|---|---|---|
| angular frequency ω (rad/s) | unitary | ${\begin{aligned}{\widehat {f}}_{2}(\omega )\ &\triangleq \ {\frac {1}{(2\pi )^{\frac {n}{2}}}}\int _{\mathbb {R} ^{n}}f(x)e^{-i\omega \cdot x}\,dx={\frac {1}{(2\pi )^{\frac {n}{2}}}}{\widehat {f}}_{1}\!\left({\frac {\omega }{2\pi }}\right)={\frac {1}{(2\pi )^{\frac {n}{2}}}}{\widehat {f}}_{3}(\omega )\\f(x)&={\frac {1}{(2\pi )^{\frac {n}{2}}}}\int _{\mathbb {R} ^{n}}{\widehat {f}}_{2}(\omega )e^{i\omega \cdot x}\,d\omega \end{aligned}}$ |
| non-unitary | ${\begin{aligned}{\widehat {f}}_{3}(\omega )\ &\triangleq \ \int _{\mathbb {R} ^{n}}f(x)e^{-i\omega \cdot x}\,dx={\widehat {f}}_{1}\left({\frac {\omega }{2\pi }}\right)=(2\pi )^{\frac {n}{2}}{\widehat {f}}_{2}(\omega )\\f(x)&={\frac {1}{(2\pi )^{n}}}\int _{\mathbb {R} ^{n}}{\widehat {f}}_{3}(\omega )e^{i\omega \cdot x}\,d\omega \end{aligned}}$ |   |

### Lebesgue integrable functions

A measurable function $f:\mathbb {R} \to \mathbb {C}$ is called (Lebesgue) integrable if the Lebesgue integral of its absolute value is finite: $\|f\|_{1}=\int _{\mathbb {R} }|f(x)|\,dx<\infty .$ If f is Lebesgue integrable then the Fourier transform, given by **Eq.1**, is well-defined for all ⁠ $\xi \in \mathbb {R}$ ⁠. Furthermore, ${\widehat {f}}\in L^{\infty }\cap C_{0}(\mathbb {R} )$ is bounded, uniformly continuous and (by the Riemann–Lebesgue lemma) vanishing at infinity. Here $C_{0}(\mathbb {R} )$ denotes the space of continuous functions on $\mathbb {R}$ that approach 0 as x approaches positive or negative infinity.

The space $L^{1}(\mathbb {R} )$ is the space of measurable functions for which the norm $\|f\|_{1}$ is finite, modulo the equivalence relation of equality almost everywhere. The Fourier transform on $L^{1}(\mathbb {R} )$ is one-to-one. However, there is no easy characterization of the image, and thus no easy characterization of the inverse transform. In particular, **Eq.2** is no longer valid, as it was stated only under the hypothesis that $f(x)$ was "sufficiently nice" (e.g., $f(x)$ decays with all derivatives).

While **Eq.1** defines the Fourier transform for (complex-valued) functions in ⁠ $L^{1}(\mathbb {R} )$ ⁠, it is not well-defined for other integrability classes, most importantly the space of square-integrable functions ⁠ $L^{2}(\mathbb {R} )$ ⁠. For example, the function $f(x)=(1+x^{2})^{-1/2}$ is in $L^{2}$ but not $L^{1}$ and therefore the Lebesgue integral **Eq.1** does not exist. However, the Fourier transform on the dense subspace $L^{1}\cap L^{2}(\mathbb {R} )\subset L^{2}(\mathbb {R} )$ admits a unique continuous extension to a unitary operator on ⁠ $L^{2}(\mathbb {R} )$ ⁠. This extension is important in part because, unlike the case of ⁠ $L^{1}$ ⁠, the Fourier transform is an automorphism of the space ⁠ $L^{2}(\mathbb {R} )$ ⁠.

In such cases, the Fourier transform can be obtained explicitly by regularizing the integral, and then passing to a limit. In practice, the integral is often regarded as an improper integral instead of a proper Lebesgue integral, but sometimes for convergence one needs to use weak limit or principal value instead of the (pointwise) limits implicit in an improper integral. Titchmarsh (1986) and Dym & McKean (1985) each gives three rigorous ways of extending the Fourier transform to square integrable functions using this procedure. A general principle in working with the $L^{2}$ Fourier transform is that finite linear combinations of Gaussians are dense in ⁠ $L^{1}\cap L^{2}$ ⁠, and the various features of the Fourier transform, such as its unitarity, are easily inferred for Gaussians. Many of the properties of the Fourier transform can then be proven from two facts about Gaussians:

- that $e^{-\pi x^{2}}$ is its own Fourier transform; and
- that the Gaussian integral ⁠ $\textstyle \int _{-\infty }^{\infty }e^{-\pi x^{2}}\,dx=1$ ⁠.

A feature of the $L^{1}$ Fourier transform is that it is a homomorphism of Banach algebras from $L^{1}$ equipped with the convolution operation to the Banach algebra of continuous functions under the $L^{\infty }$ (supremum) norm. The conventions chosen in this article are those of harmonic analysis, such that the Fourier transform is both unitary on ⁠ $L^{2}$ ⁠ and an algebra homomorphism from ⁠ ${1}$ ⁠ to ⁠ $L^{\infty }$ ⁠, without renormalizing the Lebesgue measure.


## Background

### History

In 1822, Fourier claimed (see *Joseph Fourier § The Analytic Theory of Heat*) that any function, whether continuous or discontinuous, can be expanded into a series of sines. That important work was corrected and expanded upon by others to provide the foundation for the various forms of the Fourier transform used since.

### Complex sinusoids

The red

sinusoid

can be described by peak amplitude (1), peak-to-peak (2),

RMS

(3), and

wavelength

(4). The red and blue sinusoids have a phase difference of

θ

.

In general, the coefficients ${\widehat {f}}(\xi )$ are complex numbers, which have two equivalent forms (see *Euler's formula*): ${\widehat {f}}(\xi )=\underbrace {Ae^{i\theta }} _{\text{polar coordinate form}}=\underbrace {A\cos(\theta )+iA\sin(\theta )} _{\text{rectangular coordinate form}}.$

The product with $e^{i2\pi \xi x}$ (**Eq.2**) has these forms: ${\begin{aligned}{\widehat {f}}(\xi )\cdot e^{i2\pi \xi x}&=Ae^{i\theta }\cdot e^{i2\pi \xi x}\\[6pt]&=\underbrace {Ae^{i(2\pi \xi x+\theta )}} _{\text{polar coordinate form}}\\[6pt]&=\underbrace {A\cos(2\pi \xi x+\theta )+iA\sin(2\pi \xi x+\theta )} _{\text{rectangular coordinate form}},\end{aligned}}$ which conveys both amplitude and phase of frequency ⁠ $\xi$ ⁠. Likewise, the intuitive interpretation of **Eq.1** is that multiplying $f(x)$ by $e^{-i2\pi \xi x}$ has the effect of subtracting $\xi$ from every frequency component of function ⁠ $f(x)$ ⁠. Only the component that was at frequency $\xi$ can produce a non-zero value of the infinite integral, because (at least formally) all the other shifted components are oscillatory and integrate to zero (see *§ Example*).

It is noteworthy how easily the product was simplified using the polar form, and how easily the rectangular form was deduced by an application of Euler's formula.

### Negative frequency

Euler's formula introduces the possibility of negative ⁠ $\xi$ ⁠. **Eq.1** is defined ⁠ $\forall \xi \in \mathbb {R}$ ⁠. Only certain complex-valued $f(x)$ have transforms ⁠ ${\widehat {f}}=0,\ \forall \ \xi <0$ ⁠. (See *Analytic signal*; a simple example is ⁠ $e^{i2\pi \xi _{0}x}\ (\xi _{0}>0)$ ⁠.)  But negative frequency is necessary to characterize all other complex-valued ⁠ $f(x)$ ⁠, found in signal processing, partial differential equations, radar, nonlinear optics, quantum mechanics, and others.

For a real-valued ⁠ $f(x)$ ⁠, **Eq.1** has the symmetry property ${\widehat {f}}(-\xi )={\widehat {f}}^{*}(\xi )$ (see *§ Conjugation* below). This redundancy enables **Eq.2** to distinguish $f(x)=\cos(2\pi \xi _{0}x)$ from ⁠ $e^{i2\pi \xi _{0}x}$ ⁠. But it cannot determine the actual sign of ⁠ $\xi _{0}$ ⁠, because $\cos(2\pi \xi _{0}x)$ and $\cos(2\pi (-\xi _{0})x)$ are indistinguishable on just the real numbers line.

### Fourier transform for periodic functions

The Fourier transform of a periodic function cannot be defined using the integral formula directly. In order for integral in **Eq.1** to be defined the function must be absolutely integrable. Instead it is common to use Fourier series. It is possible to extend the definition to include periodic functions by viewing them as tempered distributions.

This makes it possible to see a connection between the Fourier series and the Fourier transform for periodic functions that have a convergent Fourier series. If $f(x)$ is a periodic function, with period ⁠ P ⁠, that has a convergent Fourier series, then: ${\widehat {f}}(\xi )=\sum _{n=-\infty }^{\infty }c_{n}\cdot \delta \left(\xi -{\tfrac {n}{P}}\right),$ where $c_{n}$ are the Fourier series coefficients of ⁠ f ⁠, and $\delta$ is the Dirac delta function. In other words, the Fourier transform is a Dirac comb function whose *teeth* are multiplied by the Fourier series coefficients.

### Sampling the Fourier transform

The Fourier transform of an integrable function f can be sampled at regular intervals of arbitrary length ⁠ $1/P$ ⁠. These samples can be deduced from one cycle of a periodic function ⁠ $f_{P}$ ⁠, which has Fourier series coefficients proportional to those samples by the Poisson summation formula: $f_{P}(x)\triangleq \sum _{n=-\infty }^{\infty }f(x+nP)={\frac {1}{P}}\sum _{k=-\infty }^{\infty }{\widehat {f}}\left({\tfrac {k}{P}}\right)e^{i2\pi {\frac {k}{P}}x},\quad \forall k\in \mathbb {Z} .$

The integrability of f ensures the periodic summation converges. Therefore, the samples ${\widehat {f}}({\tfrac {k}{P}})$ can be determined by Fourier series analysis: ${\widehat {f}}\left({\tfrac {k}{P}}\right)=\int _{P}f_{P}(x)\cdot e^{-i2\pi {\frac {k}{P}}x}\,dx.$

When $f(x)$ has compact support, $f_{P}(x)$ has a finite number of terms within the interval of integration. When $f(x)$ does not have compact support, numerical evaluation of $f_{P}(x)$ requires an approximation, such as tapering $f(x)$ or truncating the number of terms.


## Units

The frequency variable must have inverse units to the units of the original function's domain (typically named t or ⁠ x ⁠). For example, if t is measured in seconds, $\xi$ should be in cycles per second or hertz. If the scale of time is in units of $2\pi$ seconds, then another Greek letter $\omega$ is typically used instead to represent angular frequency (where ⁠ $\omega =2\pi \xi$ ⁠) in units of radians per second. If using x for units of length, then $\xi$ must be in inverse length, e.g., wavenumbers. That is to say, there are two versions of the real line: one that is the range of t and measured in units of ⁠ t ⁠, and the other that is the range of $\xi$ and measured in inverse units to the units of ⁠ t ⁠. These two distinct versions of the real line cannot be equated with each other. Therefore, the Fourier transform goes from one space of functions to a different space of functions: functions that have a different domain of definition.

In general, $\xi$ must always be taken to be a linear form on the space of its domain, which is to say that the second real line is the dual space of the first real line. (See the article *Linear algebra* for a more formal explanation and for more details.) This point of view becomes essential in generalizations of the Fourier transform to general symmetry groups, including the case of Fourier series.

That there is no one preferred way (often, one says "no canonical way") to compare the two versions of the real line that are involved in the Fourier transform—fixing the units on one line does not force the scale of the units on the other line—is the reason for the plethora of rival conventions on the definition of the Fourier transform. The various definitions resulting from different choices of units differ by various constants.

In other conventions, the Fourier transform has i in the exponent instead of −*i*, and vice versa for the inversion formula. This convention is common in modern physics and is the default for Wolfram Alpha, and does not mean that the frequency has become negative, since there is no canonical definition of positivity for frequency of a complex wave. It simply means that ${\widehat {f}}(\xi )$ is the amplitude of the wave ⁠ $e^{-i2\pi \xi x}$ ⁠ instead of the wave  $e^{i2\pi \xi x}$ (the former, with its minus sign, is often seen in the time dependence for sinusoidal plane-wave solutions of the electromagnetic wave equation, or in the time dependence for quantum wave functions). Many of the identities involving the Fourier transform remain valid in those conventions, provided all terms that explicitly involve *i* have it replaced by −*i*. In electrical engineering the letter *j* is typically used for the imaginary unit instead of *i* because *i* is used for current.

When using dimensionless units, the constant factors might not be written in the transform definition. For instance, in probability theory, the characteristic function Φ of the probability density function ⁠ f ⁠ of a random variable ⁠ X ⁠ of continuous type is defined without a negative sign in the exponential, and since the units of ⁠ x ⁠ are ignored, there is no ⁠ $2\pi$ ⁠ either: $\varphi (\lambda )=\int _{-\infty }^{\infty }f(x)e^{i\lambda x}\,dx.$

In probability theory and mathematical statistics, the use of the Fourier—Stieltjes transform is preferred, because many random variables are not of continuous type, and do not possess a density function, and one must treat not functions but distributions, i.e., measures that possess "atoms".

From the higher point of view of group characters, which is much more abstract, all these arbitrary choices disappear, as will be explained in the later section of this article, which treats the notion of the Fourier transform of a function on a locally compact abelian group.


## Properties

Let $f(x)$ and $h(x)$ represent *integrable functions* Lebesgue-measurable on the real line satisfying: $\int _{-\infty }^{\infty }|f(x)|\,dx<\infty .$ We denote the Fourier transforms of these functions as ${\widehat {f}}(\xi )$ and ${\widehat {h}}(\xi )$ respectively.

### Basic properties

The Fourier transform has the following basic properties:

#### Linearity

$a\ f(x)+b\ h(x)\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ a\ {\widehat {f}}(\xi )+b\ {\widehat {h}}(\xi );\quad \ a,b\in \mathbb {C}$

#### Time shifting

$f(x-x_{0})\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ e^{-i2\pi x_{0}\xi }\ {\widehat {f}}(\xi );\quad \ x_{0}\in \mathbb {R}$

#### Frequency shifting

$e^{i2\pi \xi _{0}x}f(x)\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ {\widehat {f}}(\xi -\xi _{0});\quad \ \xi _{0}\in \mathbb {R}$

#### Time scaling

$f(ax)\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ {\frac {1}{|a|}}{\widehat {f}}\left({\frac {\xi }{a}}\right);\quad \ a\neq 0$ The case $a=-1$ leads to the *time-reversal property*: $f(-x)\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ {\widehat {f}}(-\xi )$

$\scriptstyle f(t)$

$\scriptstyle {\widehat {f}}(\omega )$

$\scriptstyle g(t)$

$\scriptstyle {\widehat {g}}(\omega )$

$\scriptstyle t$

$\scriptstyle \omega$

$\scriptstyle t$

$\scriptstyle \omega$

The transform of an even-symmetric real-valued function

⁠

$f(t)=f_{_{\text{RE}}}$

⁠

is also an even-symmetric real-valued function (

⁠

${\widehat {f}}\!_{_{\text{RE}}}$

⁠

). The time-shift,

⁠

$g(t)=g_{_{\text{RE}}}+g_{_{\text{RO}}}$

⁠

, creates an imaginary component,

⁠

$i\ {\widehat {g\ \!}}_{_{\text{IO}}}$

⁠

. (See

§ Symmetry

.)

#### Symmetry

When the real and imaginary parts of a complex function are decomposed into their even and odd parts, there are four components, denoted below by the subscripts RE, RO, IE, and IO. And there is a one-to-one mapping between the four components of a complex time function and the four components of its complex frequency transform:

${\begin{array}{rlcccccccc}{\mathsf {Time\ domain}}&f&=&f_{_{\text{RE}}}&+&f_{_{\text{RO}}}&+&i\ f_{_{\text{IE}}}&+&\underbrace {i\ f_{_{\text{IO}}}} \\&{\Bigg \Updownarrow }{\mathcal {F}}&&{\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}&&\ \ {\Bigg \Updownarrow }{\mathcal {F}}\\{\mathsf {Frequency\ domain}}&{\widehat {f}}&=&{\widehat {f}}\!_{_{\text{RE}}}&+&\overbrace {i\ {\widehat {f}}\!_{_{\text{IO}}}} &+&i\ {\widehat {f}}\!_{_{\text{IE}}}&+&{\widehat {f}}\!_{_{\text{RO}}}\end{array}}$

From this, various relationships are apparent, for example:

- The transform of a real-valued function (⁠ $f_{_{\text{RE}}}+f_{_{\text{RO}}}$ ⁠) is the *conjugate symmetric* function ⁠ ${\widehat {f}}\!_{_{\text{RE}}}+i\ {\widehat {f}}\!_{_{\text{IO}}}$ ⁠. Conversely, a *conjugate symmetric* transform implies a real-valued time-domain.
- The transform of an imaginary-valued function (⁠ $i\ f_{_{\text{IE}}}+i\ f_{_{\text{IO}}}$ ⁠) is the *conjugate antisymmetric* function ⁠ ${\widehat {f}}\!_{_{\text{RO}}}+i\ {\widehat {f}}\!_{_{\text{IE}}}$ ⁠, and the converse is true.
- The transform of a *conjugate symmetric* function $(f_{_{\text{RE}}}+i\ f_{_{\text{IO}}})$ is the real-valued function ⁠ ${\widehat {f}}\!_{_{\text{RE}}}+{\widehat {f}}\!_{_{\text{RO}}}$ ⁠, and the converse is true.
- The transform of a *conjugate antisymmetric* function $(f_{_{\text{RO}}}+i\ f_{_{\text{IE}}})$ is the imaginary-valued function ⁠ $i\ {\widehat {f}}\!_{_{\text{IE}}}+i\ {\widehat {f}}\!_{_{\text{IO}}}$ ⁠, and the converse is true.

#### Conjugation

${\bigl (}f(x){\bigr )}^{*}\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ \left({\widehat {f}}(-\xi )\right)^{*}$ (Note: the ⁠ * ⁠ denotes complex conjugation.)

In particular, if f is *real*, then ${\widehat {f}}$ is conjugate symmetric (a.k.a. Hermitian function): ${\widehat {f}}(-\xi )={\bigl (}{\widehat {f}}(\xi ){\bigr )}^{*}.$

If f is purely imaginary, then ${\widehat {f}}$ is odd symmetric: ${\widehat {f}}(-\xi )=-({\widehat {f}}(\xi ))^{*}.$

#### Real and imaginary parts

$\operatorname {Re} \{f(x)\}\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ {\tfrac {1}{2}}\left({\widehat {f}}(\xi )+{\bigl (}{\widehat {f}}(-\xi ){\bigr )}^{*}\right)$ $\operatorname {Im} \{f(x)\}\ \ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ \ {\tfrac {1}{2i}}\left({\widehat {f}}(\xi )-{\bigl (}{\widehat {f}}(-\xi ){\bigr )}^{*}\right)$

#### Zero frequency component

Substituting $\xi =0$ in the definition, we obtain: ${\widehat {f}}(0)=\int _{-\infty }^{\infty }f(x)\,dx.$

The integral of f over its domain is the total mass or DC bias of the function.

### Uniform continuity and the Riemann–Lebesgue lemma

The Fourier transform may be defined in some cases for non-integrable functions, but the Fourier transforms of integrable functions have several strong properties.

The Fourier transform ${\widehat {f}}$ of any integrable function f is uniformly continuous and $\left\|{\widehat {f}}\right\|_{\infty }\leq \left\|f\right\|_{1}$

By the *Riemann–Lebesgue lemma*, ${\widehat {f}}(\xi )\to 0{\text{ as }}|\xi |\to \infty .$

However, ${\widehat {f}}$ need not be integrable. For example, the Fourier transform of the rectangular function, which is integrable, is the sinc function, which is not Lebesgue integrable, because its improper integrals behave analogously to the alternating harmonic series, in converging to a sum without being absolutely convergent.

It is not generally possible to write the *inverse transform* as a Lebesgue integral. However, when both f and ${\widehat {f}}$ are integrable, the inverse equality $f(x)=\int _{-\infty }^{\infty }{\widehat {f}}(\xi )e^{i2\pi x\xi }\,d\xi$ holds for almost every x. As a result, the Fourier transform is injective on *L*1(**R**).

### Plancherel theorem and Parseval's theorem

Let ⁠ $f(x)$ ⁠ and ⁠ $g(x)$ ⁠ be integrable, and let ⁠ ${\widehat {f}}$ ⁠ and ⁠ ${\widehat {g}}$ ⁠ be their Fourier transforms. If ⁠ $f(x)$ ⁠ and ⁠ $g(x)$ ⁠ are also square-integrable, then the Parseval formula follows: $\langle f,g\rangle _{L^{2}}=\int _{-\infty }^{\infty }f(x){\overline {g(x)}}\,dx=\int _{-\infty }^{\infty }{\widehat {f}}(\xi ){\overline {{\widehat {g}}(\xi )}}\,d\xi ,$ where the bar denotes complex conjugation.

The Plancherel theorem, which follows from the above, states that $\|f\|_{L^{2}}^{2}=\int _{-\infty }^{\infty }\left|f(x)\right|^{2}\,dx=\int _{-\infty }^{\infty }\left|{\widehat {f}}(\xi )\right|^{2}\,d\xi .$

Plancherel's theorem makes it possible to extend the Fourier transform, by a continuity argument, to a unitary operator on ⁠ $L^{2}(\mathbb {R} )$ ⁠. On ⁠ $L^{1}(\mathbb {R} )\cap L^{2}(\mathbb {R} )$ ⁠, this extension agrees with original Fourier transform defined on ⁠ $L^{1}(\mathbb {R} )$ ⁠, thus enlarging the domain of the Fourier transform to ⁠ $L^{1}(\mathbb {R} )+L^{2}(\mathbb {R} )$ ⁠ (and consequently to ⁠ $L^{p}(\mathbb {R} )$ ⁠ for ⁠ $1\leq p\leq 2$ ⁠). Plancherel's theorem has the interpretation in the sciences that the Fourier transform preserves the energy of the original quantity. The terminology of these formulas is not quite standardised. Parseval's theorem was proved only for Fourier series, and was first proved by Lyapunov. But Parseval's formula makes sense for the Fourier transform as well, and so even though in the context of the Fourier transform it was proved by Plancherel, it is still often referred to as Parseval's formula, or Parseval's relation, or even Parseval's theorem.

See *Pontryagin duality* for a general formulation of this concept in the context of locally compact abelian groups.

### Convolution theorem

The Fourier transform translates between convolution and multiplication of functions. If ⁠ $f(x)$ ⁠ and ⁠ $g(x)$ ⁠ are integrable functions with Fourier transforms ⁠ ${\widehat {f}}$ ⁠ and ⁠ ${\widehat {g}}(\xi )$ ⁠ respectively, then the Fourier transform of the convolution is given by the product of the Fourier transforms ⁠ ${\widehat {f}}$ ⁠ and ⁠ ${\widehat {g}}$ ⁠ (under other conventions for the definition of the Fourier transform a constant factor may appear).

This means that if: $h(x)=(f*g)(x)=\int _{-\infty }^{\infty }f(y)g(x-y)\,dy,$ where ∗ denotes the convolution operation, then: ${\widehat {h}}(\xi )={\widehat {f}}(\xi )\,{\widehat {g}}(\xi ).$

In linear time invariant (LTI) system theory, it is common to interpret ⁠ $g(x)$ ⁠ as the impulse response of an LTI system with input ⁠ $f(x)$ ⁠ and output ⁠ $h(x)$ ⁠, since substituting the unit impulse for ⁠ $f(x)$ ⁠ yields ⁠ $h(x)=g(x)$ ⁠. In this case, ⁠ ${\widehat {g}}(\xi )$ ⁠ represents the frequency response of the system.

Conversely, if ⁠ $f(x)$ ⁠ can be decomposed as the product of two square integrable functions ⁠ $p(x)$ ⁠ and ⁠ $q(x)$ ⁠, then the Fourier transform of ⁠ $f(x)$ ⁠ is given by the convolution of the respective Fourier transforms ⁠ ${\widehat {p}}(\xi )$ ⁠ and ⁠ ${\widehat {q}}(\xi )$ ⁠.

### Cross-correlation theorem

In an analogous manner, it can be shown that if ⁠ $h(x)$ ⁠ is the cross-correlation of ⁠ $f(x)$ ⁠ and ⁠ $g(x)$ ⁠: $h(x)=(f\star g)(x)=\int _{-\infty }^{\infty }{\overline {f(y)}}g(x+y)\,dy$ then the Fourier transform of ⁠ $h(x)$ ⁠ is: ${\widehat {h}}(\xi )={\overline {{\widehat {f}}(\xi )}}\,{\widehat {g}}(\xi ).$

As a special case, the autocorrelation of function ⁠ $f(x)$ ⁠ is: $h(x)=(f\star f)(x)=\int _{-\infty }^{\infty }{\overline {f(y)}}f(x+y)\,dy$ for which ${\widehat {h}}(\xi )={\overline {{\widehat {f}}(\xi )}}{\widehat {f}}(\xi )=\left|{\widehat {f}}(\xi )\right|^{2}.$

### Differentiation

Suppose *f*(*x*) is differentiable almost everywhere, and both ⁠ f ⁠ and its derivative ⁠ $f'$ ⁠ are integrable (in ⁠ $L^{1}(\mathbb {R} )$ ⁠). Then the Fourier transform of the derivative is given by ${\widehat {f'}}(\xi )={\mathcal {F}}\left\{{\frac {d}{dx}}f(x)\right\}=i2\pi \xi {\widehat {f}}(\xi ).$ More generally, the Fourier transformation of the ⁠ n ⁠th derivative ⁠ $f^{(n)}$ ⁠ is given by ${\widehat {f^{(n)}}}(\xi )={\mathcal {F}}\left\{{\frac {d^{n}}{dx^{n}}}f(x)\right\}=(i2\pi \xi )^{n}{\widehat {f}}(\xi ).$

Analogously, ⁠ ${\mathcal {F}}^{-1}\left\{{\frac {d^{n}}{d\xi ^{n}}}{\widehat {f}}(\xi )\right\}=(-i2\pi x)^{n}f(x)$ ⁠, so ⁠ ${\mathcal {F}}\left\{x^{n}f(x)\right\}=\left({\frac {i}{2\pi }}\right)^{n}{\frac {d^{n}}{d\xi ^{n}}}{\widehat {f}}(\xi )$ ⁠.

By applying the Fourier transform and using these formulas, some ordinary differential equations can be transformed into algebraic equations, which are much easier to solve. These formulas also give rise to the rule of thumb "⁠ $f(x)$ ⁠ is smooth if and only if ⁠ ${\widehat {f}}(\xi )$ ⁠ quickly falls to ⁠ 0 ⁠ for ⁠ $\vert \xi \vert \to \infty$ ⁠". By using the analogous rules for the inverse Fourier transform, one can also say "⁠ $f(x)$ ⁠ quickly falls to ⁠ 0 ⁠ for ⁠ $\vert x\vert \to \infty$ ⁠ if and only if ⁠ ${\widehat {f}}(\xi )$ ⁠ is smooth."

### Eigenfunctions

The Fourier transform is a linear transform that has eigenfunctions obeying ⁠ ${\mathcal {F}}[\psi ]=\lambda \psi$ ⁠, with ⁠ $\lambda \in \mathbb {C}$ ⁠.

A set of eigenfunctions is found by noting that the homogeneous differential equation $\left[U\left({\frac {1}{2\pi }}{\frac {d}{dx}}\right)+U(x)\right]\psi (x)=0$ leads to eigenfunctions $\psi (x)$ of the Fourier transform ${\mathcal {F}}$ as long as the form of the equation remains invariant under Fourier transform. In other words, every solution $\psi (x)$ and its Fourier transform ${\widehat {\psi }}(\xi )$ obey the same equation. Assuming uniqueness of the solutions, every solution $\psi (x)$ must therefore be an eigenfunction of the Fourier transform. The form of the equation remains unchanged under Fourier transform if $U(x)$ can be expanded in a power series in which for all terms the same factor of either one of ⁠ $\pm 1$ ⁠, ⁠ $\pm i$ ⁠ arises from the factors $i^{n}$ introduced by the differentiation rules upon Fourier transforming the homogeneous differential equation because this factor may then be cancelled. The simplest allowable $U(x)=x$ leads to the standard normal distribution.

More generally, a set of eigenfunctions is also found by noting that the differentiation rules imply that the ordinary differential equation $\left[W\left({\frac {i}{2\pi }}{\frac {d}{dx}}\right)+W(x)\right]\psi (x)=C\psi (x)$ with C constant and $W(x)$ being a non-constant even function remains invariant in form when applying the Fourier transform ${\mathcal {F}}$ to both sides of the equation. The simplest example is provided by ⁠ $W(x)=x^{2}$ ⁠, which is equivalent to considering the Schrödinger equation for the quantum harmonic oscillator. The corresponding solutions provide an important choice of an orthonormal basis for *L*2(**R**) and are given by the "physicist's" Hermite functions. Equivalently one may use $\psi _{n}(x)={\frac {\sqrt[{4}]{2}}{\sqrt {n!}}}e^{-\pi x^{2}}\mathrm {He} _{n}\left(2x{\sqrt {\pi }}\right),$ where ⁠ $\mathrm {He} _{n}(x)$ ⁠ are the "probabilist's" Hermite polynomials, defined as $\mathrm {He} _{n}(x)=(-1)^{n}e^{{\frac {1}{2}}x^{2}}\left({\frac {d}{dx}}\right)^{n}e^{-{\frac {1}{2}}x^{2}}.$

Under this convention for the Fourier transform, we have that ${\widehat {\psi }}_{n}(\xi )=(-i)^{n}\psi _{n}(\xi ).$

In other words, the Hermite functions form a complete orthonormal system of eigenfunctions for the Fourier transform on ⁠ $L^{2}(\mathbb {R} )$ ⁠. However, this choice of eigenfunctions is not unique. Because of ${\mathcal {F}}^{4}=\mathrm {id}$ there are only four different eigenvalues of the Fourier transform (the fourth roots of unity ⁠ $\pm 1$ ⁠ and ⁠ $\pm i$ ⁠) and any linear combination of eigenfunctions with the same eigenvalue gives another eigenfunction. As a consequence of this, it is possible to decompose *L*2(**R**) as a direct sum of four spaces *H*0, *H*1, *H*2, and *H*3 where the Fourier transform acts on H*k* simply by multiplication by *i**k*.

Since the complete set of Hermite functions *ψn* provides a resolution of the identity they diagonalize the Fourier operator, i.e. the Fourier transform can be represented by such a sum of terms weighted by the above eigenvalues, and these sums can be explicitly summed: ${\mathcal {F}}[f](\xi )=\int dxf(x)\sum _{n\geq 0}(-i)^{n}\psi _{n}(x)\psi _{n}(\xi )~.$

This approach to define the Fourier transform was first proposed by Norbert Wiener. Among other properties, Hermite functions decrease exponentially fast in both frequency and time domains, and they are thus used to define a generalization of the Fourier transform, namely the fractional Fourier transform used in time–frequency analysis. In physics, this transform was introduced by Edward Condon. This change of basis becomes possible because the Fourier transform is a unitary transform when using the right conventions. Consequently, under the proper conditions it may be expected to result from a self-adjoint generator N via ${\mathcal {F}}[\psi ]=e^{-itN}\psi .$

The operator N is the number operator of the quantum harmonic oscillator written as $N\equiv {\frac {1}{4\pi }}\left(2\pi x-{\frac {\partial }{\partial x}}\right)\left(2\pi x+{\frac {\partial }{\partial x}}\right)=-{\frac {1}{4\pi }}{\frac {\partial ^{2}}{\partial x^{2}}}+\pi x^{2}-{\frac {1}{2}}.$

It can be interpreted as the generator of fractional Fourier transforms for arbitrary values of t, and of the conventional continuous Fourier transform ${\mathcal {F}}$ for the particular value ⁠ $t=\pi /2$ ⁠, with the Mehler kernel implementing the corresponding active transform. The eigenfunctions of N are the Hermite functions ⁠ $\psi _{n}(x)$ ⁠, which are therefore also eigenfunctions of ⁠ ${\mathcal {F}}$ ⁠.

Upon extending the Fourier transform to distributions the Dirac comb is also an eigenfunction of the Fourier transform.

### Inversion and periodicity

Under suitable conditions on the function ⁠ f ⁠, it can be recovered from its Fourier transform ⁠ ${\widehat {f}}$ ⁠. Indeed, denoting the Fourier transform operator by ⁠ ${\mathcal {F}}$ ⁠, so ⁠ ${\mathcal {F}}f:={\widehat {f}}$ ⁠, then for suitable functions, applying the Fourier transform twice simply flips the function: ⁠ $\left({\mathcal {F}}^{2}f\right)(x)=f(-x)$ ⁠, which can be interpreted as "reversing time". Since reversing time is two-periodic, applying this twice yields ⁠ ${\mathcal {F}}^{4}(f)=f$ ⁠, so the Fourier transform operator is four-periodic, and similarly the inverse Fourier transform can be obtained by applying the Fourier transform three times: ⁠ ${\mathcal {F}}^{3}\left({\widehat {f}}\right)=f$ ⁠. In particular the Fourier transform is invertible (under suitable conditions).

More precisely, defining the *parity operator* ${\mathcal {P}}$ such that ⁠ $({\mathcal {P}}f)(x)=f(-x)$ ⁠, we have: ${\begin{aligned}{\mathcal {F}}^{0}&=\mathrm {id} ,\\{\mathcal {F}}^{1}&={\mathcal {F}},\\{\mathcal {F}}^{2}&={\mathcal {P}},\\{\mathcal {F}}^{3}&={\mathcal {F}}^{-1}={\mathcal {P}}\circ {\mathcal {F}}={\mathcal {F}}\circ {\mathcal {P}},\\{\mathcal {F}}^{4}&=\mathrm {id} \end{aligned}}$ These equalities of operators require careful definition of the space of functions in question, defining equality of functions (equality at every point? equality almost everywhere?) and defining equality of operators – that is, defining the topology on the function space and operator space in question. These are not true for all functions, but are true under various conditions, which are the content of the various forms of the Fourier inversion theorem.

This fourfold periodicity of the Fourier transform is similar to a rotation of the plane by 90°, particularly as the two-fold iteration yields a reversal, and in fact this analogy can be made precise. While the Fourier transform can simply be interpreted as switching the time domain and the frequency domain, with the inverse Fourier transform switching them back, more geometrically it can be interpreted as a rotation by 90° in the time–frequency domain (considering time as the ⁠ x ⁠-axis and frequency as the ⁠ y ⁠-axis), and the Fourier transform can be generalized to the fractional Fourier transform, which involves rotations by other angles. This can be further generalized to linear canonical transformations, which can be visualized as the action of the special linear group SL2(**R**) on the time–frequency plane, with the preserved symplectic form corresponding to the uncertainty principle, below. This approach is particularly studied in signal processing, under time–frequency analysis.

### Connection with the Heisenberg group

The Heisenberg group is a certain group of unitary operators on the Hilbert space *L*2(**R**) of square integrable complex valued functions f on the real line, generated by the translations (*Ty f*)(*x*) = *f* (*x* + *y*) and multiplication by *e**i*2π*ξx*, (*Mξ f*)(*x*) = *e**i*2π*ξx* *f* (*x*). These operators do not commute, as their (group) commutator is $\left(M_{\xi }^{-1}T_{y}^{-1}M_{\xi }T_{y}f\right)(x)=e^{i2\pi \xi y}f(x),$ which is multiplication by the constant (independent of x) *e**i*2π*ξy* ∈ *U*(1) (the circle group of unit modulus complex numbers). As an abstract group, the Heisenberg group is the three-dimensional Lie group of triples (*x*, *ξ*, *z*) ∈ **R**2 × *U*(1), with the group law $\left(x_{1},\xi _{1},t_{1}\right)\cdot \left(x_{2},\xi _{2},t_{2}\right)=\left(x_{1}+x_{2},\xi _{1}+\xi _{2},t_{1}t_{2}e^{-2i\pi x_{1}\xi _{2}}\right).$

Denote the Heisenberg group by *H*1. The above procedure describes not only the group structure, but also a standard unitary representation of *H*1 on a Hilbert space, which we denote by *ρ* : *H*1 → *B*(*L*2(**R**)). Define the linear automorphism of **R**2 by $J{\begin{pmatrix}x\\\xi \end{pmatrix}}={\begin{pmatrix}-\xi \\x\end{pmatrix}}$ so that *J*2 = −*I*. This J can be extended to a unique automorphism of *H*1: $j\left(x,\xi ,t\right)=\left(-\xi ,x,te^{-i2\pi \xi x}\right).$

According to the Stone–von Neumann theorem, the unitary representations ρ and *ρ* ∘ *j* are unitarily equivalent, so there is a unique intertwiner *W* ∈ *U*(*L*2(**R**)) such that $\rho \circ j=W\rho W^{*}.$ This operator W is the Fourier transform.

Many of the standard properties of the Fourier transform are immediate consequences of this more general framework. For example, the square of the Fourier transform, *W*2, is an intertwiner associated with *J*2 = −*I*, and so we have (*W*2*f*)(*x*) = *f* (−*x*) is the reflection of the original function f.
