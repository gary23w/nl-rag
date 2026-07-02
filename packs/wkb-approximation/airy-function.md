---
title: "Airy function"
source: https://en.wikipedia.org/wiki/Airy_function
domain: wkb-approximation
license: CC-BY-SA-4.0
tags: wkb approximation, eikonal equation, semiclassical physics, stokes phenomenon
fetched: 2026-07-02
---

# Airy function

In mathematics, the **Airy function** (or **Airy function of the first kind**) $\mathbf {Ai({\boldsymbol {x}})}$ is a special function named after the British astronomer George Biddell Airy. The function $\operatorname {Ai} (x)$ and the related function $\mathbf {Bi({\boldsymbol {x}})}$ are linearly independent solutions to the differential equation ${\frac {d^{2}y}{dx^{2}}}-xy=0,$ known as the **Airy equation** or the **Stokes equation**.

Because the solution of the linear differential equation ${\frac {d^{2}y}{dx^{2}}}-ky=0$ is oscillatory for $k<0$ and exponential for $k>0$ , the Airy functions are oscillatory for $x<0$ and exponential for $x>0$ . In fact, the Airy equation is the simplest second-order linear differential equation with a turning point (a point where the character of the solutions changes from oscillatory to exponential).

## Definitions

For real values of x , the Airy function of the first kind can be defined by the improper Riemann integral

$\operatorname {Ai} (x)={\dfrac {1}{\pi }}\int _{0}^{\infty }\!\cos \left({\dfrac {t^{3}}{3}}+xt\right)\,dt$

,

which converges by Dirichlet's test. The Airy equation

$y''-xy=0$

has two linearly independent solutions. Up to scalar multiplication, $\operatorname {Ai} (x)$ is the solution subject to the condition $y\to 0$ as $x\to \infty$ . The standard choice for the other solution is the Airy function of the second kind, denoted $\operatorname {Bi} (x)$ . It is defined as the solution with the same amplitude of oscillation as $\operatorname {Ai} (x)$ as $x\to \infty$ which differs in phase by $\pi /2$ :

$\operatorname {Bi} (x)={\frac {1}{\pi }}\int _{0}^{\infty }\left[\exp \left(-{\tfrac {t^{3}}{3}}+xt\right)+\sin \left({\tfrac {t^{3}}{3}}+xt\right)\,\right]dt.$

## Properties

The values of $\operatorname {Ai} (x)$ and $\operatorname {Bi} (x)$ and their derivatives at $x=0$ are given by ${\begin{aligned}\operatorname {Ai} (0)&{}={\frac {1}{3^{2/3}\,\Gamma \!\left({\frac {2}{3}}\right)}},&\quad \operatorname {Ai} '(0)&{}=-{\frac {1}{3^{1/3}\,\Gamma \!\left({\frac {1}{3}}\right)}},\\\operatorname {Bi} (0)&{}={\frac {1}{3^{1/6}\,\Gamma \!\left({\frac {2}{3}}\right)}},&\quad \operatorname {Bi} '(0)&{}={\frac {3^{1/6}}{\Gamma \!\left({\frac {1}{3}}\right)}}.\end{aligned}}$ Here, $\Gamma$ denotes the gamma function. It follows that the Wronskian of $\operatorname {Ai} (x)$ and $\operatorname {Bi} (x)$ is $1/\pi$ .

When x is positive, $\operatorname {Ai} (x)$ is positive, convex, and decreasing exponentially to zero, while $\operatorname {Bi} (x)$ is positive, convex, and increasing exponentially. When x is negative, $\operatorname {Ai} (x)$ and $\operatorname {Bi} (x)$ oscillate around zero with ever-increasing frequency and ever-decreasing amplitude as $x\to -\infty$ . This is supported by the asymptotic formulae below for the Airy functions.

The Airy functions are orthogonal in the sense that

$\int _{-\infty }^{\infty }\operatorname {Ai} (t+x)\operatorname {Ai} (t+y)dt=\delta (x-y),$

again using an improper Riemann integral.

### Real zeros of Ai(*x*) and its derivative Ai′(*x*)

Neither $\operatorname {Ai} (x)$ nor its derivative $\operatorname {Ai} '(x)$ have positive real zeros. The "first" real zeros (i.e. nearest to $x=0$ ) are:

- "first" zeros of Ai(*x*) are at *x* ≈ −2.33811, −4.08795, −5.52056, −6.78671, ...
- "first" zeros of its derivative Ai'(*x*) are at *x* ≈ −1.01879, −3.24820, −4.82010, −6.16331, ...

## Asymptotic formulae

As explained below, the Airy functions can be extended to the complex plane, giving entire functions. The asymptotic behaviour of the Airy functions as |z| goes to infinity at a constant value of arg(*z*) depends on arg(*z*): this is called the Stokes phenomenon. For |arg(*z*)| < *π* we have the following asymptotic formula for Ai(*z*):

$\operatorname {Ai} (z)\sim {\dfrac {1}{2{\sqrt {\pi }}\,z^{1/4}}}\exp \left(-{\frac {2}{3}}z^{3/2}\right)\left[\sum _{n=0}^{\infty }{\dfrac {(-1)^{n}\,\Gamma \!\left(n+{\frac {5}{6}}\right)\,\Gamma \!\left(n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{n}}{2\pi \,n!\,z^{3n/2}}}\right].$ or $\operatorname {Ai} (z)\sim {\dfrac {e^{-\zeta }}{4\pi ^{3/2}\,z^{1/4}}}\left[\sum _{n=0}^{\infty }{\dfrac {\Gamma \!\left(n+{\frac {5}{6}}\right)\,\Gamma \!\left(n+{\frac {1}{6}}\right)}{n!(-2\zeta )^{n}}}\right].$ where $\zeta ={\tfrac {2}{3}}z^{3/2}.$ In particular, the first few terms are $\operatorname {Ai} (z)={\frac {e^{-\zeta }}{2\pi ^{1/2}z^{1/4}}}\left(1-{\frac {5}{72\zeta }}+{\frac {385}{10368\zeta ^{2}}}+O(\zeta ^{-3})\right)$ There is a similar one for Bi(*z*), but only applicable when |arg(*z*)| < *π*/3:

$\operatorname {Bi} (z)\sim {\frac {1}{{\sqrt {\pi }}\,z^{1/4}}}\exp \left({\frac {2}{3}}z^{3/2}\right)\left[\sum _{n=0}^{\infty }{\dfrac {\Gamma \!\left(n+{\frac {5}{6}}\right)\,\Gamma \!\left(n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{n}}{2\pi \,n!\,z^{3n/2}}}\right].$ A more accurate formula for Ai(*z*) and a formula for Bi(*z*) when *π*/3 < |arg(*z*)| < *π* or, equivalently, for Ai(−*z*) and Bi(−*z*) when |arg(*z*)| < 2*π*/3 but not zero, are: ${\begin{aligned}\operatorname {Ai} (-z)\sim &{}\ {\frac {1}{{\sqrt {\pi }}\,z^{1/4}}}\sin \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {5}{6}}\right)\,\Gamma \!\left(2n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{2n}}{2\pi \,(2n)!\,z^{3n}}}\right]\\[6pt]&{}-{\frac {1}{{\sqrt {\pi }}\,z^{1/4}}}\cos \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {11}{6}}\right)\,\Gamma \!\left(2n+{\frac {7}{6}}\right)\left({\frac {3}{4}}\right)^{2n+1}}{2\pi \,(2n+1)!\,z^{3n\,+\,3/2}}}\right]\\[6pt]\operatorname {Bi} (-z)\sim &{}{\frac {1}{{\sqrt {\pi }}\,z^{1/4}}}\cos \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {5}{6}}\right)\,\Gamma \!\left(2n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{2n}}{2\pi \,(2n)!\,z^{3n}}}\right]\\[6pt]&{}+{\frac {1}{{\sqrt {\pi }}\,z^{\frac {1}{4}}}}\sin \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {11}{6}}\right)\,\Gamma \!\left(2n+{\frac {7}{6}}\right)\left({\frac {3}{4}}\right)^{2n+1}}{2\pi \,(2n+1)!\,z^{3n\,+\,3/2}}}\right].\end{aligned}}$

When |arg(*z*)| = 0 these are good approximations but are not asymptotic because the ratio between Ai(−*z*) or Bi(−*z*) and the above approximation goes to infinity whenever the sine or cosine goes to zero. Asymptotic expansions for these limits are also available. These are listed in Abramowitz and Stegun (1983) and Olver (1974).

One is also able to obtain asymptotic expressions for the derivatives Ai'(z) and Bi'(z). Similarly to before, when |arg(*z*)| < *π*:

$\operatorname {Ai} '(z)\sim -{\dfrac {z^{1/4}}{2{\sqrt {\pi }}\,}}\exp \left(-{\frac {2}{3}}z^{3/2}\right)\left[\sum _{n=0}^{\infty }{\frac {1+6n}{1-6n}}{\dfrac {(-1)^{n}\,\Gamma \!\left(n+{\frac {5}{6}}\right)\,\Gamma \!\left(n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{n}}{2\pi \,n!\,z^{3n/2}}}\right].$

When |arg(*z*)| < *π*/3 we have:

$\operatorname {Bi} '(z)\sim {\frac {z^{1/4}}{{\sqrt {\pi }}\,}}\exp \left({\frac {2}{3}}z^{3/2}\right)\left[\sum _{n=0}^{\infty }{\frac {1+6n}{1-6n}}{\dfrac {\Gamma \!\left(n+{\frac {5}{6}}\right)\,\Gamma \!\left(n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{n}}{2\pi \,n!\,z^{3n/2}}}\right].$

Similarly, an expression for Ai'(−*z*) and Bi'(−*z*) when |arg(*z*)| < 2*π*/3 but not zero, are

${\begin{aligned}\operatorname {Ai} '(-z)\sim &{}-{\frac {z^{1/4}}{{\sqrt {\pi }}\,}}\cos \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\frac {1+12n}{1-12n}}{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {5}{6}}\right)\,\Gamma \!\left(2n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{2n}}{2\pi \,(2n)!\,z^{3n}}}\right]\\[6pt]&{}-{\frac {z^{1/4}}{{\sqrt {\pi }}\,}}\sin \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\frac {7+12n}{-5-12n}}{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {11}{6}}\right)\,\Gamma \!\left(2n+{\frac {7}{6}}\right)\left({\frac {3}{4}}\right)^{2n+1}}{2\pi \,(2n+1)!\,z^{3n\,+\,3/2}}}\right]\\[6pt]\operatorname {Bi} '(-z)\sim &{}\ {\frac {z^{1/4}}{{\sqrt {\pi }}\,}}\sin \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\frac {1+12n}{1-12n}}{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {5}{6}}\right)\,\Gamma \!\left(2n+{\frac {1}{6}}\right)\left({\frac {3}{4}}\right)^{2n}}{2\pi \,(2n)!\,z^{3n}}}\right]\\[6pt]&{}-{\frac {z^{1/4}}{{\sqrt {\pi }}\,}}\cos \left({\frac {2}{3}}z^{3/2}+{\frac {\pi }{4}}\right)\left[\sum _{n=0}^{\infty }{\frac {7+12n}{-5-12n}}{\dfrac {(-1)^{n}\,\Gamma \!\left(2n+{\frac {11}{6}}\right)\,\Gamma \!\left(2n+{\frac {7}{6}}\right)\left({\frac {3}{4}}\right)^{2n+1}}{2\pi \,(2n+1)!\,z^{3n\,+\,3/2}}}\right]\\\end{aligned}}$

## Complex arguments

We can extend the definition of the Airy function to the complex plane by $\operatorname {Ai} (z)={\frac {1}{2\pi i}}\int _{C}\exp \left({\tfrac {t^{3}}{3}}-zt\right)\,dt,$ where the integral is over a path *C* starting at the point at infinity with argument −*π*/3 and ending at the point at infinity with argument π/3. Alternatively, we can use the differential equation *y*′′ − *xy* = 0 to extend Ai(*x*) and Bi(*x*) to entire functions on the complex plane.

The asymptotic formula for Ai(*x*) is still valid in the complex plane if the principal value of *x*2/3 is taken and x is bounded away from the negative real axis. The formula for Bi(*x*) is valid provided x is in the sector $x\in \mathbb {C} :\left|\arg(x)\right|<{\tfrac {\pi }{3}}-\delta$ for some positive δ. Finally, the formulae for Ai(−*x*) and Bi(−*x*) are valid if *x* is in the sector $x\in \mathbb {C} :\left|\arg(x)\right|<{\tfrac {2\pi }{3}}-\delta .$

It follows from the asymptotic behaviour of the Airy functions that both Ai(*x*) and Bi(*x*) have an infinity of zeros on the negative real axis. The function Ai(*x*) has no other zeros in the complex plane, while the function Bi(*x*) also has infinitely many zeros in the sector $z\in \mathbb {C} :{\tfrac {\pi }{3}}<\left|\arg(z)\right|<{\tfrac {\pi }{2}}.$

### Plots

| $\Re \left[\operatorname {Ai} (x+iy)\right]$ | $\Im \left[\operatorname {Ai} (x+iy)\right]$ | $\left\|\operatorname {Ai} (x+iy)\right\|\,$ | $\operatorname {arg} \left[\operatorname {Ai} (x+iy)\right]\,$ |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |

| $\Re \left[\operatorname {Bi} (x+iy)\right]$ | $\Im \left[\operatorname {Bi} (x+iy)\right]$ | $\left\|\operatorname {Bi} (x+iy)\right\|\,$ | $\operatorname {arg} \left[\operatorname {Bi} (x+iy)\right]\,$ |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |

## Relation to other special functions

For positive arguments, the Airy functions are related to the modified Bessel functions: ${\begin{aligned}\operatorname {Ai} (x)&{}={\frac {1}{\pi }}{\sqrt {\frac {x}{3}}}\,K_{1/3}\!\left({\frac {2}{3}}x^{3/2}\right),\\\operatorname {Bi} (x)&{}={\sqrt {\frac {x}{3}}}\left[I_{1/3}\!\left({\frac {2}{3}}x^{3/2}\right)+I_{-1/3}\!\left({\frac {2}{3}}x^{3/2}\right)\right].\end{aligned}}$ Here, *I*±1/3 and *K*1/3 are solutions of $x^{2}y''+xy'-\left(x^{2}+{\tfrac {1}{9}}\right)y=0.$

The first derivative of the Airy function is $\operatorname {Ai'} (x)=-{\frac {x}{\pi {\sqrt {3}}}}\,K_{2/3}\!\left({\frac {2}{3}}x^{3/2}\right).$

Functions *K*1/3 and *K*2/3 can be represented in terms of rapidly convergent integrals (see also modified Bessel functions)

For negative arguments, the Airy function are related to the Bessel functions: ${\begin{aligned}\operatorname {Ai} (-x)&{}={\sqrt {\frac {x}{9}}}\left[J_{1/3}\!\left({\frac {2}{3}}x^{3/2}\right)+J_{-1/3}\!\left({\frac {2}{3}}x^{3/2}\right)\right],\\\operatorname {Bi} (-x)&{}={\sqrt {\frac {x}{3}}}\left[J_{-1/3}\!\left({\frac {2}{3}}x^{3/2}\right)-J_{1/3}\!\left({\frac {2}{3}}x^{3/2}\right)\right].\end{aligned}}$ Here, *J*±1/3 are solutions of $x^{2}y''+xy'+\left(x^{2}-{\frac {1}{9}}\right)y=0.$

The Scorer's functions Hi(*x*) and -Gi(*x*) solve the equation *y*′′ − *xy* = 1/π. They can also be expressed in terms of the Airy functions: ${\begin{aligned}\operatorname {Gi} (x)&{}=\operatorname {Bi} (x)\int _{x}^{\infty }\operatorname {Ai} (t)\,dt+\operatorname {Ai} (x)\int _{0}^{x}\operatorname {Bi} (t)\,dt,\\\operatorname {Hi} (x)&{}=\operatorname {Bi} (x)\int _{-\infty }^{x}\operatorname {Ai} (t)\,dt-\operatorname {Ai} (x)\int _{-\infty }^{x}\operatorname {Bi} (t)\,dt.\end{aligned}}$

## Integration

Abel's identity shows that the Wronskian

$W(\operatorname {Ai} ,\operatorname {Bi} )$

is constant. As was noted earlier, it evaluates to ${\frac {1}{\pi }}$ . The fact that the quotient rule is equivalent to

$\left({\frac {f}{g}}\right)'={\frac {W(g,f)}{g^{2}}}$

grants various integrals a closed form that would otherwise be unattainable.

$\int {\frac {1}{\operatorname {Ai} (x)\operatorname {Bi} (x)}}\,\mathrm {d} x=\pi \ln \left|{\frac {\operatorname {Bi} (x)}{\operatorname {Ai} (x)}}\right|+C$

$\int {\frac {1}{\operatorname {Ai} ^{2}(x)+\operatorname {Bi} ^{2}(x)}}\,\mathrm {d} x=\pi \arctan \left({\frac {\operatorname {Bi} (x)}{\operatorname {Ai} (x)}}\right)+C$

$\int {\frac {e^{\frac {\operatorname {Bi} (x)}{\operatorname {Ai} (x)}}}{\operatorname {Ai} (x)\operatorname {Bi} (x)}}\,\mathrm {d} x=\pi \operatorname {Ei} \left({\frac {\operatorname {Bi} (x)}{\operatorname {Ai} (x)}}\right)+C$

## Fourier transform

Using the definition of the Airy function Ai(*x*), it is straightforward to show that its Fourier transform is given by ${\mathcal {F}}(\operatorname {Ai} )(k):=\int _{-\infty }^{\infty }\operatorname {Ai} (x)\ e^{-2\pi ikx}\,dx=e^{{\frac {i}{3}}(2\pi k)^{3}}.$ This can be obtained by taking the Fourier transform of the Airy equation. Let ${\textstyle {\hat {y}}={\frac {1}{2\pi i}}\int ye^{-ikx}dx}$ . Then, $i{\hat {y}}'+k^{2}{\hat {y}}=0$ , which then has solutions ${\hat {y}}=Ce^{ik^{3}/3}.$ There is only one dimension of solutions because the Fourier transform requires y to decay to zero fast enough; Bi grows to infinity exponentially fast, so it cannot be obtained via a Fourier transform.

## Applications

### Quantum mechanics

The Airy function is the solution to the time-independent Schrödinger equation for a particle confined within a triangular potential well and for a particle in a one-dimensional constant force field. For the same reason, it also serves to provide uniform semiclassical approximations near a turning point in the WKB approximation, when the potential may be locally approximated by a linear function of position. The triangular potential well solution is directly relevant for the understanding of electrons trapped in semiconductor heterojunctions.

### Optics

A transversally asymmetric optical beam, where the electric field profile is given by the Airy function, has the interesting property that its maximum intensity *accelerates* towards one side instead of propagating in a straight line as is the case in symmetric beams. This is at expense of the low-intensity tail being spread in the opposite direction, so the overall momentum of the beam is of course conserved.

### Caustics

The Airy function underlies the form of the intensity near an optical directional caustic, such as that of the rainbow (called supernumerary rainbow). Historically, this was the mathematical problem that led Airy to develop this special function. In 1841, William Hallowes Miller experimentally measured the analog to supernumerary rainbow by shining light through a thin cylinder of water, then observing through a telescope. He observed up to 30 bands.

The Airy function is the universal local model near a fold caustic (in semiclassical optics). The phase shift by $\pi /4$ in the asymptotic expansion of $\operatorname {Ai} (-x)$ is the local form of the Maslov phase correction, which globally is encoded by the Maslov index.

### Probability

In the mid-1980s, the Airy function was found to be intimately connected to Chernoff's distribution.

The Airy function also appears in the definition of Tracy–Widom distribution which describes the law of largest eigenvalues in Random matrix. Due to the intimate connection of random matrix theory with the Kardar–Parisi–Zhang equation, there are central processes constructed in KPZ such as the Airy process.

## History

The Airy function is named after the British astronomer and physicist George Biddell Airy (1801–1892), who encountered it in his early study of optics in physics. The notation Ai(*x*) was introduced by Harold Jeffreys. Airy had become the British Astronomer Royal in 1835, and he held that post until his retirement in 1881.
