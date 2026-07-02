---
title: "Laplace transform (part 1/2)"
source: https://en.wikipedia.org/wiki/Laplace_transform
domain: ordinary-differential-equations
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, boundary value problem, laplace transform
fetched: 2026-07-02
part: 1/2
---

# Laplace transform

In mathematics, the **Laplace transform**, named after Pierre-Simon Laplace (/ləˈplɑːs/), is an integral transform that converts a function of a real variable (usually ⁠ t ⁠, in the *time domain*) to a function of a complex variable s (in the complex-valued frequency domain, also known as ***s*-domain** or ***s*-plane**). The functions are often denoted using a lowercase symbol for the time-domain function and the corresponding uppercase symbol for the frequency-domain function, e.g. $x(t)$ and ⁠ $X(s)$ ⁠.

The transform is useful for converting differentiation and integration in the time domain into the algebraic operations multiplication and division in the Laplace domain (analogous to how logarithms are useful for simplifying multiplication and division into addition and subtraction). This gives the transform many applications in science and engineering, mostly as a tool for solving linear differential equations and dynamical systems by replacing ordinary differential equations and integral equations with algebraic polynomial equations, and by replacing convolution with multiplication.

For example, through the Laplace transform, the equation of the simple harmonic oscillator (Hooke's law) $x''(t)+kx(t)=0$ is converted into the algebraic equation $s^{2}X(s)-sx(0)-x'(0)+kX(s)=0,$ which incorporates the initial conditions $x(0)$ and ⁠ $x'(0)$ ⁠, and can be solved for the unknown function ⁠ $X(s)$ ⁠. Once solved, the inverse Laplace transform can be used to transform it to the original domain. This is often aided by referencing tables such as that given below.

The Laplace transform is defined (for suitable functions ⁠ f ⁠) by the integral ${\mathcal {L}}\{f\}(s)=\int _{0}^{\infty }f(t)e^{-st}\,dt,$ where ⁠ s ⁠ is a complex number.

The Laplace transform is related to many other transforms. It is essentially the same as the Mellin transform and is closely related to the Fourier transform. Unlike for the Fourier transform, the Laplace transform of a function is often an analytic function, meaning that it can be expressed as a power series that converges locally, the coefficients of which represent the moments of the original function. Moreover, the techniques of complex analysis, especially contour integrals, can be used for simplifying calculations.


## History

The Laplace transform is named after mathematician and astronomer Pierre-Simon, Marquis de Laplace, who used a similar transform in his work on probability theory. Laplace wrote extensively about the use of generating functions (1814), and the integral form of the Laplace transform evolved naturally as a result.

Laplace's use of generating functions was similar to what is now known as the z-transform, and he gave little attention to the continuous variable case which was discussed by Niels Henrik Abel.

From 1744, Leonhard Euler investigated integrals of the form $z=\int X(x)e^{ax}\,dx\quad {\text{ and }}\quad z=\int X(x)x^{A}\,dx$ as solutions of differential equations, introducing in particular the gamma function. Joseph-Louis Lagrange was an admirer of Euler and, in his work on integrating probability density functions, investigated expressions of the form $\int X(x)e^{-ax}a^{x}\,dx,$ which resembles a Laplace transform.

These types of integrals seem first to have attracted Laplace's attention in 1782, where he was following in the spirit of Euler in using the integrals themselves as solutions of equations. However, in 1785, Laplace took the critical step forward when, rather than simply looking for a solution in the form of an integral, he started to apply the transforms in the sense that was later to become popular. He used an integral of the form $\int x^{s}\varphi (x)\,dx,$ akin to a Mellin transform, to transform the whole of a difference equation, in order to look for solutions of the transformed equation. He then went on to apply the Laplace transform in the same way and started to derive some of its properties, beginning to appreciate its potential power.

Laplace also recognised that Joseph Fourier's method of Fourier series for solving the diffusion equation could only apply to a limited region of space, because those solutions were periodic. In 1809, Laplace applied his transform to find solutions that diffused indefinitely in space. In 1821, Cauchy developed an operational calculus for the Laplace transform that could be used to study linear differential equations in much the same way the transform is now used in basic engineering. This method was popularized, and perhaps rediscovered, by Oliver Heaviside around the turn of the century.

Bernhard Riemann used the Laplace transform in his 1859 paper *On the number of primes less than a given magnitude*, in which he also developed the inversion theorem. Riemann used the Laplace transform to develop the functional equation of the Riemann zeta function, and his method is still used to relate the modular transformation law of the Jacobi theta function, which is readily proved via Poisson summation, to the functional equation.

Hjalmar Mellin was among the first to study the Laplace transform rigorously in the Karl Weierstrass school of analysis, and apply it to the study of differential equations and special functions, at the turn of the 20th century. At around the same time, Heaviside was busy with his operational calculus. Thomas Joannes Stieltjes considered a generalization of the Laplace transform connected to his work on moments. Other contributors in this time period included Mathias Lerch, Oliver Heaviside, and Thomas Bromwich.

In 1929, Vannevar Bush and Norbert Wiener published *Operational Circuit Analysis* as a text for engineering analysis of electrical circuits, applying both Fourier transforms and operational calculus, and in which they included one of the first predecessors of the modern table of Laplace transforms. In 1934, Raymond Paley and Norbert Wiener published the important work *Fourier transforms in the complex domain*, about what is now called the Laplace transform (see below). Also during the 30s, the Laplace transform was instrumental in Godfrey Harold Hardy and John Edensor Littlewood's study of tauberian theorems, and this application was later expounded on by Widder (1941), who developed other aspects of the theory such as a new method for inversion. Edward Charles Titchmarsh wrote the influential *Introduction to the theory of the Fourier integral* (1937).

The current widespread use of the transform (mainly in engineering) came about during and soon after World War II, replacing the earlier Heaviside operational calculus. The advantages of the Laplace transform had been emphasized by Gustav Doetsch.


## Formal definition

The Laplace transform of a function *f*(*t*), defined for all real numbers *t* ≥ 0, is the function *F*(*s*) defined by

$F(s)=\int _{0}^{\infty }f(t)e^{-st}\,dt,$    (Eq. 1)

where s is a complex frequency-domain parameter ${\textstyle s=\sigma +i\omega }$ with real numbers σ and ω.

An alternate notation for the Laplace transform is ${\mathcal {L}}\{f\}$ instead of *F*. Thus $F(s)={\mathcal {L}}\{f\}(s)$ in functional notation. This is often written, especially in engineering settings, as ⁠ $F(s)={\mathcal {L}}\{f(t)\}$ ⁠, with the understanding that the dummy variable t does not appear in the function ⁠ $F(s)$ ⁠.

The meaning of the integral depends on types of functions of interest. A necessary condition for existence of the integral is that f must be locally integrable on [0, ∞). For locally integrable functions that decay at infinity or are of exponential type (⁠ $\vert f(t)\vert \leq Ae^{B\vert t\vert }$ ⁠), the integral can be understood to be a (proper) Lebesgue integral. However, for many applications it is necessary to regard it as a conditionally convergent improper integral at ∞. Still more generally, the integral can be understood in a weak sense, and this is dealt with below.

One can define the Laplace transform of a finite Borel measure μ by the Lebesgue integral ${\mathcal {L}}\{\mu \}(s)=\int _{[0,\infty )}e^{-st}\,d\mu (t).$

An important special case is where μ is a probability measure, for example, the Dirac delta function. In operational calculus, the Laplace transform of a measure is often treated as though the measure came from a probability density function f. In that case, to avoid potential confusion, one often writes ${\mathcal {L}}\{f\}(s)=\int _{0^{-}}^{\infty }f(t)e^{-st}\,dt,$ where the lower limit of 0− is shorthand notation for $\lim _{\varepsilon \to 0^{+}}\int _{-\varepsilon }^{\infty }.$

This limit emphasizes that any point mass located at 0 is entirely captured by the Laplace transform. Although with the Lebesgue integral, it is not necessary to take such a limit, it does appear more naturally in connection with the Laplace–Stieltjes transform.

### Bilateral Laplace transform

When one says "the Laplace transform" without qualification, the unilateral or one-sided transform is usually intended. The Laplace transform can be alternatively defined as the *bilateral Laplace transform*, or two-sided Laplace transform, by extending the limits of integration to be the entire real axis. If that is done, the common unilateral transform becomes a special case of the bilateral transform, where the definition of the function being transformed includes being multiplied by the Heaviside step function.

The bilateral Laplace transform *F*(*s*) is defined as follows:

$F(s)=\int _{-\infty }^{\infty }e^{-st}f(t)\,dt.$    (Eq. 2)

An alternate notation for the bilateral Laplace transform is ⁠ ${\mathcal {B}}\{f\}$ ⁠, instead of F.

### Inverse Laplace transform

Two integrable functions have the same Laplace transform only if they differ on a set of Lebesgue measure zero. This means that, on the range of the transform, there is an inverse transform. In fact, besides integrable functions, the Laplace transform is a one-to-one mapping from one function space into another in many other function spaces as well, although there is usually no easy characterization of the range.

Typical function spaces in which this is true include the spaces of bounded continuous functions, the space *L*∞(0, ∞), or more generally tempered distributions on (0, ∞). The Laplace transform is also defined and injective for suitable spaces of tempered distributions.

In these cases, the image of the Laplace transform lives in a space of analytic functions in the region of convergence. The inverse Laplace transform is given by the following complex integral, which is known by various names (the **Bromwich integral**, the **Fourier–Mellin integral**, and **Mellin's inverse formula**):

$f(t)={\mathcal {L}}^{-1}\{F\}(t)={\frac {1}{2\pi i}}\lim _{T\to \infty }\int _{\gamma -iT}^{\gamma +iT}e^{st}F(s)\,ds,$    (Eq. 3)

where γ is a real number so that the contour path of integration is in the region of convergence of *F*(*s*). In most applications, the contour can be closed, allowing the use of the residue theorem. An alternative formula for the inverse Laplace transform is given by Post's inversion formula. The limit here is interpreted in the weak-* topology.

In practice, it is typically more convenient to decompose a Laplace transform into known transforms of functions obtained from a table and construct the inverse by inspection.

### Probability theory

In pure and applied probability, the Laplace transform is defined as an expected value. If X is a random variable with probability density function f, then the Laplace transform of f is given by the expectation ${\mathcal {L}}\{f\}(s)=\operatorname {E} \left[e^{-sX}\right],$ where $\operatorname {E} [r]$ is the expectation of random variable ⁠ r ⁠.

By convention, this is referred to as the Laplace transform of the random variable X itself. Here, replacing s by −*t* gives the moment generating function of X. The Laplace transform has applications throughout probability theory, including first passage times of stochastic processes such as Markov chains, and renewal theory.

Of particular use is the ability to recover the cumulative distribution function of a continuous random variable X by means of the Laplace transform as follows: $F_{X}(x)={\mathcal {L}}^{-1}\left\{{\frac {1}{s}}\operatorname {E} \left[e^{-sX}\right]\right\}(x)={\mathcal {L}}^{-1}\left\{{\frac {1}{s}}{\mathcal {L}}\{f\}(s)\right\}(x).$

### Algebraic construction

The Laplace transform can be alternatively defined in a purely algebraic manner by applying a field of fractions construction to the convolution ring of functions on the positive half-line. The resulting space of abstract operators is exactly equivalent to Laplace space, but in this construction the forward and reverse transforms never need to be explicitly defined (avoiding the related difficulties with proving convergence).


## Region of convergence

If *f* is a locally integrable function (or more generally a Borel measure locally of bounded variation), then the Laplace transform *F*(*s*) of *f* converges provided that the limit $\lim _{R\to \infty }\int _{0}^{R}f(t)e^{-st}\,dt$ exists.

The Laplace transform converges absolutely if the integral $\int _{0}^{\infty }\left|f(t)e^{-st}\right|\,dt$ exists as a proper Lebesgue integral. The Laplace transform is usually understood as conditionally convergent, meaning that it converges in the former but not in the latter sense.

The set of values for which *F*(*s*) converges absolutely is either of the form Re(*s*) > *a* or Re(*s*) ≥ *a*, where *a* is an extended real constant with −∞ ≤ *a* ≤ ∞ (a consequence of the dominated convergence theorem). The constant *a* is known as the abscissa of absolute convergence, and depends on the growth behavior of *f*(*t*). Analogously, the two-sided transform converges absolutely in a strip of the form *a* < Re(*s*) < *b*, and possibly including the lines Re(*s*) = *a* or Re(*s*) = *b*. The subset of values of *s* for which the Laplace transform converges absolutely is called the region of absolute convergence, or the domain of absolute convergence. In the two-sided case, it is sometimes called the strip of absolute convergence. The Laplace transform is analytic in the region of absolute convergence: this is a consequence of Fubini's theorem and Morera's theorem.

Similarly, the set of values for which *F*(*s*) converges (conditionally or absolutely) is known as the region of conditional convergence, or simply the **region of convergence** (ROC). If the Laplace transform converges (conditionally) at *s* = *s*0, then it automatically converges for all *s* with Re(*s*) > Re(*s*0). Therefore, the region of convergence is a half-plane of the form Re(*s*) > *a*, possibly including some points of the boundary line Re(*s*) = *a*.

In the region of convergence Re(*s*) > Re(*s*0), the Laplace transform of *f* can be expressed by integrating by parts as the integral $F(s)=(s-s_{0})\int _{0}^{\infty }e^{-(s-s_{0})t}\beta (t)\,dt,\quad \beta (u)=\int _{0}^{u}e^{-s_{0}t}f(t)\,dt.$

That is, *F*(*s*) can effectively be expressed, in the region of convergence, as the absolutely convergent Laplace transform of some other function. In particular, it is analytic. In its most general form, the Laplace transform gives a one-to-one correspondence between the holomorphic functions which, for some ⁠ $\sigma \in \mathbb {R}$ ⁠, are defined on $\{s\in \mathbb {C} \ \vert \ \mathrm {Re} (s)>\sigma \}$ and are bounded there in absolute value by a polynomial, and the distributions on the real line supported on ⁠ $[0,\infty )$ ⁠ which become tempered distributions after multiplied by $e^{-\sigma t}$ for some ⁠ $\sigma$ ⁠.

There are several Paley–Wiener theorems concerning the relationship between the decay properties of *f*, and the properties of the Laplace transform within the region of convergence.

In engineering applications, a function corresponding to a linear time-invariant (LTI) system is *stable* if every bounded input produces a bounded output. This is equivalent to the absolute convergence of the Laplace transform of the impulse response function in the region Re(*s*) ≥ 0. As a result, LTI systems are stable, provided that the poles of the Laplace transform of the impulse response function have negative real part.

This ROC is used in knowing about the causality and stability of a system.


## Properties and theorems

The Laplace transform's key property is that it converts differentiation and integration in the time domain into multiplication and division by *s* in the Laplace domain. Thus, the Laplace variable *s* is also known as an *operator variable* in the Laplace domain: either the *derivative operator* or (for *s*−1) the *integration operator*.

Given the functions *f*(*t*) and *g*(*t*), and their respective Laplace transforms *F*(*s*) and *G*(*s*), ${\begin{aligned}f(t)&={\mathcal {L}}^{-1}\{F(s)\},\\g(t)&={\mathcal {L}}^{-1}\{G(s)\},\end{aligned}}$

the following table is a list of properties of unilateral Laplace transform:

| Property | Time domain | *s* domain | Comment |
|---|---|---|---|
| Linearity | $af(t)+bg(t)\$ | $aF(s)+bG(s)\$ | Can be proved using basic rules of integration. |
| Frequency-domain derivative | $tf(t)\$ | $-F'(s)\$ | *F*′ is the first derivative of *F* with respect to *s*. |
| Frequency-domain general derivative | $t^{n}f(t)\$ | $(-1)^{n}F^{(n)}(s)\$ | More general form, *n*th derivative of *F*(*s*). |
| Derivative | $f'(t)\$ | $sF(s)-f(0^{-})\$ | *f* is assumed to be a differentiable function, and its derivative is assumed to be of exponential type. This can then be obtained by integration by parts |
| Second derivative | $f''(t)\$ | ${\textstyle s^{2}F(s)-sf(0^{-})-f'(0^{-})\ }$ | *f* is assumed twice differentiable and the second derivative to be of exponential type. Follows by applying the Differentiation property to *f*′(*t*). |
| General derivative | $f^{(n)}(t)\$ | $s^{n}F(s)-\sum _{k=1}^{n}s^{n-k}f^{(k-1)}(0^{-})\$ | *f* is assumed to be *n*-times differentiable, with *n*th derivative of exponential type. Follows by mathematical induction. |
| Frequency-domain integration | ${\frac {1}{t}}f(t)\$ | $\int _{s}^{\infty }F(\sigma )\,d\sigma \$ | This is deduced using the nature of frequency differentiation and conditional convergence. |
| Time-domain integration | $\int _{0}^{t}f(\tau )\,d\tau =(u*f)(t)$ | ${1 \over s}F(s)$ | *u*(*t*) is the Heaviside step function and (*u* ∗ *f*)(*t*) is the convolution of *u*(*t*) and *f*(*t*). |
| Frequency shifting | $e^{at}f(t)$ | $F(s-a)$ |   |
| Time shifting | $f(t-a)u(t-a)$ $f(t)u(t-a)\$ | $e^{-as}F(s)\$ $e^{-as}{\mathcal {L}}\{f(t+a)\}$ | *a* > 0, *u*(*t*) is the Heaviside step function |
| Time scaling | $f(at)$ | ${\frac {1}{a}}F\left({s \over a}\right)$ | *a* > 0 |
| Multiplication | $f(t)g(t)$ | ${\frac {1}{2\pi i}}\lim _{T\to \infty }\int _{c-iT}^{c+iT}F(\sigma )G(s-\sigma )\,d\sigma \$ | The integration is done along the vertical line Re(*σ*) = *c* that lies entirely within the region of convergence of *F*. |
| Convolution | $(f*g)(t)=\int _{0}^{t}f(\tau )g(t-\tau )\,d\tau$ | $F(s)\cdot G(s)\$ |   |
| Circular convolution | $(f*g)(t)=\int _{0}^{T}f(\tau )g(t-\tau )\,d\tau$ | $F(s)\cdot G(s)\$ | For periodic functions with period *T*. |
| Complex conjugation | $f^{*}(t)$ | $F^{*}(s^{*})$ |   |
| Periodic function | $f(t)$ | ${1 \over 1-e^{-Ts}}\int _{0}^{T}e^{-st}f(t)\,dt$ | *f*(*t*) is a periodic function of period *T* so that *f*(*t*) = *f*(*t* + *T*), for all *t* ≥ 0. This is the result of the time shifting property and the geometric series. |
| Periodic summation | $f_{P}(t)=\sum _{n=0}^{\infty }f(t-Tn)$ $f_{P}(t)=\sum _{n=0}^{\infty }(-1)^{n}f(t-Tn)$ | $F_{P}(s)={\frac {1}{1-e^{-Ts}}}F(s)$ $F_{P}(s)={\frac {1}{1+e^{-Ts}}}F(s)$ |   |

**Initial value theorem**

$f(0^{+})=\lim _{s\to \infty }{sF(s)}.$

**Final value theorem**

⁠

$f(\infty )=\lim _{s\to 0}{sF(s)}$

⁠

, if all

poles

of

$sF(s)$

are in the left half-plane.

The final value theorem is useful because it gives the long-term behaviour without having to perform

partial fraction

decompositions (or other difficult algebra). If

F

(

s

)

has a pole in the right-hand plane or poles on the imaginary axis (e.g., if

$f(t)=e^{t}$

or

⁠

$f(t)=\sin(t)$

⁠

), then the behaviour of this formula is undefined.

### Relation to power series

The Laplace transform can be viewed as a continuous analogue of a power series. If *a*(*n*) is a discrete function of a positive integer *n*, then the power series associated to *a*(*n*) is the series $\sum _{n=0}^{\infty }a(n)x^{n}$ where *x* is a real variable (see *Z-transform*). Replacing summation over *n* with integration over *t*, a continuous version of the power series becomes $\int _{0}^{\infty }f(t)x^{t}\,dt$ where the discrete function *a*(*n*) is replaced by the continuous one *f*(*t*).

Changing the base of the power from *x* to *e* gives $\int _{0}^{\infty }f(t)\left(e^{\ln {x}}\right)^{t}\,dt$

For this to converge for, say, all bounded functions *f*, it is necessary to require that ln *x* < 0. Making the substitution −*s* = ln *x* gives just the Laplace transform: $\int _{0}^{\infty }f(t)e^{-st}\,dt$

In other words, the Laplace transform is a continuous analog of a power series, in which the discrete parameter *n* is replaced by the continuous parameter *t*, and *x* is replaced by *e*−*s*.

Analogously to a power series, if ⁠ $a(n)=O(\rho ^{-n})$ ⁠, then the power series converges to an analytic function in ⁠ $\vert x\vert <\rho$ ⁠, if ⁠ $f(t)=O(e^{-\sigma t})$ ⁠, the Laplace transform converges to an analytic function for ⁠ $\Re (s)>\sigma$ ⁠.

### Relation to moments

The quantities $\mu _{n}=\int _{0}^{\infty }t^{n}f(t)\,dt$ are the *moments* of the function *f*. If the first *n* moments of *f* converge absolutely, then by repeated differentiation under the integral, $(-1)^{n}({\mathcal {L}}f)^{(n)}(0)=\mu _{n}.$ This is of special significance in probability theory, where the moments of a random variable *X* are given by the expectation values ⁠ $\mu _{n}=\operatorname {E} [X^{n}]$ ⁠. Then, the relation holds $\mu _{n}=(-1)^{n}{\frac {d^{n}}{ds^{n}}}\operatorname {E} \left[e^{-sX}\right](0).$

### Transform of a function's derivative

It is often convenient to use the differentiation property of the Laplace transform to find the transform of a function's derivative. This can be derived from the basic expression for a Laplace transform as follows: ${\begin{aligned}{\mathcal {L}}\left\{f(t)\right\}&=\int _{0^{-}}^{\infty }e^{-st}f(t)\,dt\\[6pt]&=\left[{\frac {f(t)e^{-st}}{-s}}\right]_{0^{-}}^{\infty }-\int _{0^{-}}^{\infty }{\frac {e^{-st}}{-s}}f'(t)\,dt\quad {\text{(by parts)}}\\[6pt]&=\left[-{\frac {f(0^{-})}{-s}}\right]+{\frac {1}{s}}{\mathcal {L}}\left\{f'(t)\right\},\end{aligned}}$ yielding ${\mathcal {L}}\{f'(t)\}=s\cdot {\mathcal {L}}\{f(t)\}-f(0^{-}),$ and in the bilateral case, ${\mathcal {L}}\{f'(t)\}=s\int _{-\infty }^{\infty }e^{-st}f(t)\,dt=s\cdot {\mathcal {L}}\{f(t)\}.$

The general result ${\mathcal {L}}\left\{f^{(n)}(t)\right\}=s^{n}\cdot {\mathcal {L}}\{f(t)\}-s^{n-1}f(0^{-})-\cdots -f^{(n-1)}(0^{-}),$ where $f^{(n)}$ denotes the *n*th derivative of *f*, can then be established with an inductive argument.

### Evaluating integrals over the positive real axis

A useful property of the Laplace transform is the following: $\int _{0}^{\infty }f(x)g(x)\,dx=\int _{0}^{\infty }({\mathcal {L}}f)(s)\cdot ({\mathcal {L}}^{-1}g)(s)\,ds$ under suitable assumptions on the behaviour of ⁠ f ⁠ and ⁠ g ⁠ in a right neighbourhood of 0 and on the decay rate of ⁠ f ⁠ and ⁠ g ⁠ in a left neighbourhood of ⁠ $\infty$ ⁠. The above formula is a variation of integration by parts, with the operators ${\frac {d}{dx}}$ and $\int \,dx$ being replaced by ${\mathcal {L}}$ and ⁠ ${\mathcal {L}}^{-1}$ ⁠. Let us prove the equivalent formulation: $\int _{0}^{\infty }({\mathcal {L}}f)(x)g(x)\,dx=\int _{0}^{\infty }f(s)({\mathcal {L}}g)(s)\,ds.$

By plugging in $({\mathcal {L}}f)(x)=\int _{0}^{\infty }f(s)e^{-sx}\,ds$ the left-hand side turns into: $\int _{0}^{\infty }\int _{0}^{\infty }f(s)g(x)e^{-sx}\,ds\,dx,$ but assuming Fubini's theorem holds, by reversing the order of integration we get the wanted right-hand side.

This method can be used to compute integrals that would otherwise be difficult to compute using elementary methods of real calculus. For example, $\int _{0}^{\infty }{\frac {\sin x}{x}}dx=\int _{0}^{\infty }{\mathcal {L}}(1)(x)\sin xdx=\int _{0}^{\infty }1\cdot {\mathcal {L}}(\sin )(x)dx=\int _{0}^{\infty }{\frac {dx}{x^{2}+1}}={\frac {\pi }{2}}.$


## Relationship to other transforms

### Laplace–Stieltjes transform

The (unilateral) Laplace–Stieltjes transform of a function *g* : ℝ → ℝ is defined by the Lebesgue–Stieltjes integral $\{{\mathcal {L}}^{*}g\}(s)=\int _{0}^{\infty }e^{-st}\,d\,g(t)~.$

The function *g* is assumed to be of bounded variation. If *g* is the antiderivative of *f*: $g(x)=\int _{0}^{x}f(t)\,d\,t$

then the Laplace–Stieltjes transform of g and the Laplace transform of f coincide. In general, the Laplace–Stieltjes transform is the Laplace transform of the Stieltjes measure associated to g. So in practice, the only distinction between the two transforms is that the Laplace transform is thought of as operating on the density function of the measure, whereas the Laplace–Stieltjes transform is thought of as operating on its cumulative distribution function.

### Fourier transform

Let f be a complex-valued Lebesgue integrable function supported on ⁠ $[0,\infty )$ ⁠, and let $F(s)={\mathcal {L}}f(s)$ be its Laplace transform. Then, within the region of convergence, we have $F(\sigma +i\tau )=\int _{0}^{\infty }f(t)e^{-\sigma t}e^{-i\tau t}\,dt,$ which is the Fourier transform of the function ⁠ $f(t)e^{-\sigma t}$ ⁠.

Indeed, the Fourier transform is a special case (under certain conditions) of the bilateral Laplace transform. The main difference is that the Fourier transform of a function is a complex function of a *real* variable (frequency ⁠ $\tau$ ⁠), the Laplace transform of a function is a complex function of a *complex* variable (damping factor $\sigma$ and frequency ⁠ $\tau$ ⁠). The Laplace transform is usually restricted to transformation of functions of *t* with *t* ≥ 0. A consequence of this restriction is that the Laplace transform of a function is a holomorphic function of the variable *s*. Unlike the Fourier transform, the Laplace transform of a distribution is generally a well-behaved function. Techniques of complex variables can also be used to directly study Laplace transforms. As a holomorphic function, the Laplace transform has a power series representation. This power series expresses a function as a linear superposition of moments of the function. This perspective has applications in probability theory.

Formally, the Fourier transform is equivalent to evaluating the bilateral Laplace transform with imaginary argument *s* = *iω* when the condition explained below is fulfilled, ${\begin{aligned}{\hat {f}}(\omega )&={\mathcal {F}}\{f(t)\}\\[4pt]&={\mathcal {L}}\{f(t)\}|_{s=i\omega }=F(s)|_{s=i\omega }\\[4pt]&=\int _{-\infty }^{\infty }e^{-i\omega t}f(t)\,dt~.\end{aligned}}$

This convention of the Fourier transform (⁠ ${\hat {f}}_{3}(\omega )$ ⁠ in *Fourier transform § Other conventions*) requires a factor of ⁠1/2*π*⁠ on the inverse Fourier transform. This relationship between the Laplace and Fourier transforms is often used to determine the frequency spectrum of a signal or dynamical system.

The above relation is valid as stated if and only if the region of convergence (ROC) of *F*(*s*) contains the imaginary axis, *σ* = 0.

For example, the function *f*(*t*) = cos(*ω*0*t*) has a Laplace transform *F*(*s*) = *s*/(*s*2 + *ω*02) whose ROC is Re(*s*) > 0. As *s* = *iω*0 is a pole of *F*(*s*), substituting *s* = *iω* in *F*(*s*) does not yield the Fourier transform of *f*(*t*)*u*(*t*), which contains terms proportional to the Dirac delta functions *δ*(*ω* ± *ω*0).

However, a relation of the form $\lim _{\sigma \to 0^{+}}F(\sigma +i\omega )={\hat {f}}(\omega )$ holds under much weaker conditions. For instance, this holds for the above example provided that the limit is understood as a weak limit of measures (see vague topology). General conditions relating the limit of the Laplace transform of a function on the boundary to the Fourier transform take the form of Paley–Wiener theorems.

### Mellin transform

The Mellin transform and its inverse are related to the two-sided Laplace transform by a change of variables.

If in the Mellin transform $G(s)={\mathcal {M}}\{g(\theta )\}=\int _{0}^{\infty }\theta ^{s}g(\theta )\,{\frac {d\theta }{\theta }}$ we set *θ* = *e*−*t* we get a two-sided Laplace transform.

### Z-transform

The unilateral or one-sided Z-transform is the Laplace transform of an ideally sampled signal with the substitution of $z{\stackrel {\mathrm {def} }{{}={}}}e^{sT},$ where *T* = 1/*fs* is the sampling interval (in units of time e.g., seconds) and *fs* is the sampling rate (in samples per second or hertz).

Let $\Delta _{T}(t)\ {\stackrel {\mathrm {def} }{=}}\ \sum _{n=0}^{\infty }\delta (t-nT)$ be a sampling impulse train (also called a Dirac comb) and ${\begin{aligned}x_{q}(t)&{\stackrel {\mathrm {def} }{{}={}}}x(t)\Delta _{T}(t)=x(t)\sum _{n=0}^{\infty }\delta (t-nT)\\&=\sum _{n=0}^{\infty }x(nT)\delta (t-nT)=\sum _{n=0}^{\infty }x[n]\delta (t-nT)\end{aligned}}$ be the sampled representation of the continuous-time *x*(*t*) $x[n]{\stackrel {\mathrm {def} }{{}={}}}x(nT)~.$

The Laplace transform of the sampled signal *x**q*(*t*) is ${\begin{aligned}X_{q}(s)&=\int _{0^{-}}^{\infty }x_{q}(t)e^{-st}\,dt\\&=\int _{0^{-}}^{\infty }\sum _{n=0}^{\infty }x[n]\delta (t-nT)e^{-st}\,dt\\&=\sum _{n=0}^{\infty }x[n]\int _{0^{-}}^{\infty }\delta (t-nT)e^{-st}\,dt\\&=\sum _{n=0}^{\infty }x[n]e^{-nsT}~.\end{aligned}}$

This is the precise definition of the unilateral Z-transform of the discrete function *x*[*n*] $X(z)=\sum _{n=0}^{\infty }x[n]z^{-n}$ with the substitution of *z* → *e**sT*.

Comparing the last two equations, we find the relationship between the unilateral Z-transform and the Laplace transform of the sampled signal, $X_{q}(s)=X(z){\Big |}_{z=e^{sT}}.$

The similarity between the Z- and Laplace transforms is expanded upon in the theory of time scale calculus.

### Borel transform

The integral form of the Borel transform $F(s)=\int _{0}^{\infty }f(z)e^{-sz}\,dz$ is a special case of the Laplace transform for *f* an entire function of exponential type, meaning that $|f(z)|\leq Ae^{B|z|}$ for some constants *A* and *B*. The generalized Borel transform allows a different weighting function to be used, rather than the exponential function, to transform functions not of exponential type. Nachbin's theorem gives necessary and sufficient conditions for the Borel transform to be well defined.

### Fundamental relationships

Since an ordinary Laplace transform can be written as a special case of a two-sided transform, and since the two-sided transform can be written as the sum of two one-sided transforms, the theory of the Laplace-, Fourier-, Mellin-, and Z-transforms are at bottom the same subject. However, a different point of view and different characteristic problems are associated with each of these four major integral transforms.


## Table of selected Laplace transforms

The following table provides Laplace transforms for many common functions of a single variable. For definitions and explanations, see the *Explanatory Notes* at the end of the table.

Because the Laplace transform is a linear operator,

- The Laplace transform of a sum is the sum of Laplace transforms of each term. ${\mathcal {L}}\{f(t)+g(t)\}={\mathcal {L}}\{f(t)\}+{\mathcal {L}}\{g(t)\}$
- The Laplace transform of a multiple of a function is that multiple times the Laplace transformation of that function. ${\mathcal {L}}\{af(t)\}=a{\mathcal {L}}\{f(t)\}$

Using this linearity, and various trigonometric, hyperbolic, and complex number (etc.) properties and/or identities, some Laplace transforms can be obtained from others more quickly than by using the definition directly.

The unilateral Laplace transform takes as input a function whose time domain is the non-negative reals, which is why all of the time domain functions in the table below are multiples of the Heaviside step function, *u*(*t*).

The entries of the table that involve a time delay *τ* are required to be causal (meaning that *τ* > 0). A causal system is a system where the impulse response *h*(*t*) is zero for all time t prior to *t* = 0. In general, the region of convergence for causal systems is not the same as that of anticausal systems.

| Function | Time domain $f(t)={\mathcal {L}}^{-1}\{F(s)\}$ | Laplace s-domain $F(s)={\mathcal {L}}\{f(t)\}$ | Region of convergence | Reference |
|---|---|---|---|---|
| unit impulse | $\delta (t)\$ | 1 | all *s* | inspection |
| delayed impulse | $\delta (t-\tau )\$ | $e^{-\tau s}\$ | all *s* | time shift of unit impulse |
| unit step | $u(t)\$ | ${1 \over s}$ | $\operatorname {Re} (s)>0$ | integrate unit impulse |
| delayed unit step | $u(t-\tau )\$ | ${\frac {1}{s}}e^{-\tau s}$ | $\operatorname {Re} (s)>0$ | time shift of unit step |
| product of delayed function and delayed step | $f(t-\tau )u(t-\tau )$ | $e^{-s\tau }{\mathcal {L}}\{f(t)\}$ |   | u-substitution, $u=t-\tau$ |
| rectangular impulse | $u(t)-u(t-\tau )$ | ${\frac {1}{s}}(1-e^{-\tau s})$ | $\operatorname {Re} (s)>0$ |   |
| ramp | $t\cdot u(t)\$ | ${\frac {1}{s^{2}}}$ | $\operatorname {Re} (s)>0$ | integrate unit impulse twice |
| *n*th power (for integer *n*) | $t^{n}\cdot u(t)$ | ${n! \over s^{n+1}}$ | $\operatorname {Re} (s)>0$ (*n* > −1) | integrate unit step *n* times |
| *q*th power (for complex *q*) | $t^{q}\cdot u(t)$ | ${\operatorname {\Gamma } (q+1) \over s^{q+1}}$ | $\operatorname {Re} (s)>0$ $\operatorname {Re} (q)>-1$ |   |
| *n*th root | ${\sqrt[{n}]{t}}\cdot u(t)$ | ${1 \over s^{{\frac {1}{n}}+1}}\operatorname {\Gamma } \left({\frac {1}{n}}+1\right)$ | $\operatorname {Re} (s)>0$ | Set *q* = 1/*n* above. |
| *n*th power with frequency shift | $t^{n}e^{-\alpha t}\cdot u(t)$ | ${\frac {n!}{(s+\alpha )^{n+1}}}$ | $\operatorname {Re} (s)>-\alpha$ | Integrate unit step, apply frequency shift |
| delayed *n*th power with frequency shift | $(t-\tau )^{n}e^{-\alpha (t-\tau )}\cdot u(t-\tau )$ | ${\frac {n!\cdot e^{-\tau s}}{(s+\alpha )^{n+1}}}$ | $\operatorname {Re} (s)>-\alpha$ | integrate unit step, apply frequency shift, apply time shift |
| exponential decay | $e^{-\alpha t}\cdot u(t)$ | ${1 \over s+\alpha }$ | $\operatorname {Re} (s)>-\alpha$ | Frequency shift of unit step |
| two-sided exponential decay (only for bilateral transform) | $e^{-\alpha \|t\|}\$ | ${2\alpha \over \alpha ^{2}-s^{2}}$ | $-\alpha <\operatorname {Re} (s)<\alpha$ | Frequency shift of unit step |
| exponential approach | $(1-e^{-\alpha t})\cdot u(t)\$ | ${\frac {\alpha }{s(s+\alpha )}}$ | $\operatorname {Re} (s)>0$ | unit step minus exponential decay |
| sine | $\sin(\omega t)\cdot u(t)\$ | ${\omega \over s^{2}+\omega ^{2}}$ | $\operatorname {Re} (s)>0$ |   |
| cosine | $\cos(\omega t)\cdot u(t)\$ | ${s \over s^{2}+\omega ^{2}}$ | $\operatorname {Re} (s)>0$ |   |
| hyperbolic sine | $\sinh(\alpha t)\cdot u(t)\$ | ${\alpha \over s^{2}-\alpha ^{2}}$ | $\operatorname {Re} (s)>\left\|\alpha \right\|$ |   |
| hyperbolic cosine | $\cosh(\alpha t)\cdot u(t)\$ | ${s \over s^{2}-\alpha ^{2}}$ | $\operatorname {Re} (s)>\left\|\alpha \right\|$ |   |
| exponentially decaying sine wave | $e^{-\alpha t}\sin(\omega t)\cdot u(t)\$ | ${\omega \over (s+\alpha )^{2}+\omega ^{2}}$ | $\operatorname {Re} (s)>-\alpha$ |   |
| exponentially decaying cosine wave | $e^{-\alpha t}\cos(\omega t)\cdot u(t)\$ | ${s+\alpha \over (s+\alpha )^{2}+\omega ^{2}}$ | $\operatorname {Re} (s)>-\alpha$ |   |
| natural logarithm | $\ln(t)\cdot u(t)$ | $-{1 \over s}\left[\ln(s)+\gamma \right]$ | $\operatorname {Re} (s)>0$ |   |
| Bessel function of the first kind, of order *n* | $J_{n}(\omega t)\cdot u(t)$ | ${\frac {\left({\sqrt {s^{2}+\omega ^{2}}}-s\right)^{\!n}}{\omega ^{n}{\sqrt {s^{2}+\omega ^{2}}}}}$ | $\operatorname {Re} (s)>0$ (*n* > −1) |   |
| Error function | $\operatorname {erf} (t)\cdot u(t)$ | ${\frac {1}{s}}e^{s^{2}/4}\!\left(1-\operatorname {erf} {\frac {s}{2}}\right)$ | $\operatorname {Re} (s)>0$ |   |
| **Explanatory notes:** *u*(*t*) represents the Heaviside step function. *δ* represents the Dirac delta function. Γ(*z*) represents the gamma function. *γ* is the Euler–Mascheroni constant. *t*, a real number, typically represents *time*, although it can represent *any* independent dimension. *s* is the complex frequency domain parameter, and Re(*s*) is its real part. *α*, *β*, *τ*, and *ω* are real numbers. *n* is an integer. |   |   |   |   |


## *s*-domain equivalent circuits and impedances

The Laplace transform is often used in circuit analysis by conversions to the *s*-domain of circuit elements. Circuit elements can be transformed into impedances, very similar to phasor impedances.

Here is a summary of equivalents:

Note that the resistor is exactly the same in the time domain and the *s*-domain. The sources are put in if there are initial conditions on the circuit elements. For example, if a capacitor has an initial voltage across it, or if the inductor has an initial current through it, the sources inserted in the *s*-domain account for that.

The equivalents for current and voltage sources are derived from the transformations in the table above.
