---
title: "Poincaré–Lindstedt method"
source: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Lindstedt_method
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
---

# Poincaré–Lindstedt method

In perturbation theory, the **Poincaré–Lindstedt method** or **Lindstedt–Poincaré method** is a technique for uniformly approximating periodic solutions to ordinary differential equations, when regular perturbation approaches fail. The method removes secular terms—terms growing without bound—arising in the straightforward application of perturbation theory to weakly nonlinear problems with finite oscillatory solutions.

The method is named after Henri Poincaré, and Anders Lindstedt.

> All efforts of geometers in the second half of this century have had as main objective the elimination of secular terms.

— Henri Poincaré, Les Méthodes Nouvelles de la Mécanique Céleste, preface to volume I

The article gives several examples. The theory can be found in Chapter 10 of Nonlinear Differential Equations and Dynamical Systems by Verhulst.

## Example: the Duffing equation

The undamped, unforced Duffing equation is given by

${\ddot {x}}+x+\varepsilon \,x^{3}=0\,$

for *t* > 0, with 0 < *ε* ≪ 1.

Consider initial conditions

$x(0)=1,\,$

${\dot {x}}(0)=0.\,$

A perturbation-series solution of the form *x*(*t*) = *x*0(*t*) + *ε* *x*1(*t*) + ... is sought. The first two terms of the series are

$x(t)=\cos(t)+\varepsilon \left[{\tfrac {1}{32}}\,\left(\cos(3t)-\cos(t)\right)-{\tfrac {3}{8}}\,t\,\sin(t)\right]+\cdots .\,$

This approximation grows without bound in time, which is inconsistent with the physical system that the equation models. The term responsible for this unbounded growth, called the **secular term**, is $t\sin(t)$ . The Poincaré–Lindstedt method allows for the creation of an approximation that is accurate for all time, as follows.

In addition to expressing the solution itself as an asymptotic series, form another series with which to scale time *t*:

$\tau =\omega t,\,$

where

$\omega =\omega _{0}+\varepsilon \omega _{1}+\cdots .\,$

We have the leading order $\omega _{0}=1$ , because when $\varepsilon =0$ , the equation has solution $x=\cos(t)$ . Then the original problem becomes

$\omega ^{2}\,x''(\tau )+x(\tau )+\varepsilon \,x^{3}(\tau )=0\,$

Now search for a solution of the form *x*(*τ*) = *x*0(*τ*) + *ε* *x*1(*τ*) + ... . The following solutions for the zeroth and first order problem in $\varepsilon$ are obtained:

${\begin{aligned}x_{0}&=\cos(\tau )\\{\text{and }}x_{1}&={\tfrac {1}{32}}\,\left(\cos(3\tau )-\cos(\tau )\right)+\left(\omega _{1}-{\tfrac {3}{8}}\right)\,\tau \,\sin(\tau ).\end{aligned}}$

So the secular term can be removed through the choice: *ω*1 = ⁠3/8⁠. Higher orders of accuracy can be obtained by continuing the perturbation analysis along this way. As of now, the approximation—correct up to first order in *ε*—is

$x(t)\approx \cos {\Bigl (}\left(1+{\tfrac {3}{8}}\,\varepsilon \right)\,t{\Bigr )}+{\tfrac {1}{32}}\,\varepsilon \,\left[\cos {\Bigl (}3\left(1+{\tfrac {3}{8}}\,\varepsilon \,\right)\,t{\Bigr )}-\cos {\Bigl (}\left(1+{\tfrac {3}{8}}\,\varepsilon \,\right)\,t{\Bigr )}\right].\,$

## Example: the van der Pol oscillator

We solve the van der Pol oscillator only up to order 2. This method can be continued indefinitely in the same way, where the order-n term $\epsilon ^{n}x_{n}$ consists of a harmonic term $a_{n}\cos(t)+b_{n}\cos(t)$ , plus some super-harmonic terms $a_{n,2}\cos(2t)+b_{n,2}\cos(2t)+\cdots$ . The coefficients of the super-harmonic terms are solved directly, and the coefficients of the harmonic term are determined by expanding down to order-(n+1), and eliminating its secular term.

See chapter 10 of for a derivation up to order 3, and for a computer derivation up to order 164.

Consider the van der Pol oscillator with equation ${\ddot {x}}+\epsilon (x^{2}-1){\dot {x}}+x=0$ where $\epsilon$ is a small positive number. Perform substitution to the second order:

> $\tau =\omega t,\,$   where   $\omega =1+\epsilon \omega _{1}+\epsilon ^{2}\omega _{2}+O(\epsilon ^{3})$

which yields the equation $\omega ^{2}{\ddot {x}}+\omega \epsilon (x^{2}-1){\dot {x}}+x=0$ Now plug in $x=x_{0}+\epsilon x_{1}+\epsilon ^{2}x_{2}+O(\epsilon ^{3})$ , and we have three equations, for the orders $1,\epsilon ,\epsilon ^{2}$ respectively: ${\begin{cases}{\ddot {x}}_{0}+x_{0}=0\\{\ddot {x}}_{1}+x_{1}+2\omega _{1}{\ddot {x}}_{0}+(x_{0}^{2}-1){\dot {x}}_{0}=0\\{\ddot {x}}_{2}+x_{2}+(\omega _{1}^{2}+2\omega _{2}){\ddot {x}}_{0}+2\omega _{1}{\ddot {x}}_{1}+2x_{0}x_{1}{\dot {x}}_{0}+\omega _{1}(x_{0}^{2}-1){\dot {x}}_{0}+{\dot {x}}_{1}(x_{0}^{2}-1)=0\end{cases}}$ The first equation has general solution $x_{0}=A\cos(\tau +\phi )$ . Pick origin of time such that $\phi =0$ . Then plug it into the second equation to obtain (after some trigonometric identities) ${\ddot {x}}_{1}+x_{1}+(A-A^{3}/4)\sin \tau -2\omega _{1}A\cos \tau -(A^{3}/4)\sin(3\tau )=0$ To eliminate the secular term, we must set both $\sin \tau ,\cos \tau$ coefficients to zero, thus we have ${\begin{cases}A=A^{3}/4\\2\omega _{1}A=0\end{cases}}$ yielding $A=2,\omega _{1}=0$ . In particular, we found that when $\epsilon$ increases from zero to a small positive constant, all circular orbits in phase space are destroyed, except the one at radius 2. Now solving ${\ddot {x}}_{1}+x_{1}=2\sin(3\tau )$ yields $x_{1}=B\cos(\tau +\phi )-{\frac {1}{4}}\sin(3\tau )$ . We can always absorb $\epsilon B\cos(\tau +\phi )$ term into $x_{0}$ , so we can WLOG have just $x_{1}=-{\frac {1}{4}}\sin(3\tau )$ .

Now plug into the second equation to obtain ${\ddot {x}}_{2}+x_{2}-(4\omega _{2}+1/4)\cos \tau -{\frac {3}{4}}\cos 3\tau -{\frac {5}{4}}\cos 5\tau =0$ To eliminate the secular term, we set $\omega _{2}=-{\frac {1}{16}}$ .

Thus we find that $\omega =1-{\frac {1}{16}}\epsilon ^{2}+O(\epsilon ^{3})$ .

## Example: Mathieu equation

This is an example of parametric resonance.

Consider the Mathieu equation ${\ddot {x}}+(1+b\epsilon ^{2}+\epsilon \cos(t))x=0$ , where b is a constant, and $\epsilon$ is small. The equation's solution would have two time-scales, one fast-varying on the order of t , and another slow-varying on the order of $T=\epsilon ^{2}t$ . So expand the solution as $x(t)=x_{0}(t,T)+\epsilon x_{1}(t,T)+\epsilon ^{2}x_{2}(t,T)+O(\epsilon ^{3})$ Now plug into the Mathieu equation and expand to obtain ${\begin{cases}\partial _{t}^{2}x_{0}+x_{0}=0\\\partial _{t}^{2}x_{1}+x_{1}=-\cos(t)x_{0}\\\partial _{t}^{2}x_{2}+x_{2}=-bx_{0}-2\partial _{tT}x_{0}-\cos(t)x_{1}\end{cases}}$ As before, we have the solutions ${\begin{cases}x_{0}=A\cos(t)+B\sin(t)\\x_{1}=-{\frac {A}{2}}+{\frac {A}{6}}\cos(2t)+{\frac {B}{6}}\sin(2t)\end{cases}}$ The secular term coefficients in the third equation are ${\begin{cases}{\frac {1}{12}}\left(-12bA+5A-24B'\right)\\{\frac {1}{12}}\left(24A'-12bB-B\right)\end{cases}}$ Setting them to zero, we find the equations of motion:

${\frac {d}{dT}}{\begin{bmatrix}A\\B\end{bmatrix}}={\begin{bmatrix}0&{\frac {1}{2}}({\frac {1}{12}}+b)\\{\frac {1}{2}}({\frac {5}{12}}-b)&0\\\end{bmatrix}}{\begin{bmatrix}A\\B\end{bmatrix}}$

Its determinant is ${\frac {1}{4}}(b-5/12)(b+1/12)$ , and so when $b\in (-1/12,5/12)$ , the origin is a saddle point, so the amplitude of oscillation ${\sqrt {A^{2}+B^{2}}}$ grows unboundedly.

In other words, when the angular frequency (in this case, 1 ) in the parameter is sufficiently close to the angular frequency (in this case, ${\sqrt {1+b\epsilon ^{2}}}$ ) of the original oscillator, the oscillation grows unboundedly, like a child swinging on a swing pumping all the way to the moon.

## Shohat expansion

For the van der Pol oscillator, we have $\omega \sim 1/\epsilon$ for large $\epsilon$ , so as $\epsilon$ becomes large, the serial expansion of $\omega$ in terms of $\epsilon$ diverges and we would need to keep more and more terms of it to keep $\omega$ bounded. This suggests to us a parametrization that is bounded: $r:={\frac {\epsilon }{1+\epsilon }}$ Then, using serial expansions $\epsilon \omega =r+c_{2}r^{2}+c_{3}r^{3}+c_{4}r^{4}+\cdots$ and $x=x_{0}+rx_{1}+r^{2}x_{2}+\cdots$ , and using the same method of eliminating the secular terms, we find $c_{2}=1,c_{3}={\frac {15}{16}},c_{4}={\frac {13}{16}}$ .

Because $\lim _{\epsilon \to \infty }r=1$ , the expansion $\epsilon \omega =r+c_{2}r^{2}+c_{3}r^{3}+c_{4}r^{4}+\cdots$ allows us to take a finite number of terms for the series on the right, and it would converge to a finite value at $\epsilon \to \infty$ limit. Then we would have $\omega \sim 1/\epsilon$ , which is exactly the desired asymptotic behavior. This is the idea behind Shohat expansion.

The exact asymptotic constant is $\epsilon \omega \to {\frac {2\pi }{3-2\ln 2}}=3.8936\cdots$ , which as we can see is approached by $1+c_{2}+c_{3}+c_{4}=3.75$ .

## References and notes

1. *Drazin, P.G. (1992), *Nonlinear systems*, Cambridge University Press, ISBN 0-521-40668-4*, pp. 181–186.
2. *Strogatz, Steven (2019). "Exercise 7.6.19, 7.6.21". *Nonlinear dynamics and chaos : with applications to physics, biology, chemistry, and engineering* (2nd ed.). Boca Raton. ISBN 978-0-367-09206-1. OCLC 1112373147.*
3. *Poincaré, H. (1957) [1893], *Les Méthodes Nouvelles de la Mécanique Célèste*, vol. II, New York: Dover Publ.*, §123–§128.
4. A. Lindstedt, Abh. K. Akad. Wiss. St. Petersburg 31, No. 4 (1882)
5. *Verhulst, Ferdinand (1996). *Nonlinear Differential Equations and Dynamical Systems*. Universitext. Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-642-61453-8. ISBN 978-3-540-60934-6.*
6. J. David Logan. *Applied Mathematics*, Second Edition, John Wiley & Sons, 1997. ISBN 0-471-16513-1.
7. The Duffing equation has an invariant energy $\scriptstyle E={\tfrac {1}{2}}\,{\dot {x}}^{2}+{\tfrac {1}{2}}\,x^{2}+{\tfrac {1}{4}}\,\varepsilon \,x^{4}$  = constant, as can be seen by multiplying the Duffing equation with $\scriptstyle {\dot {x}}$ and integrating with respect to time *t*. For the example considered, from its initial conditions, is found: *E* = ⁠1/2⁠ + ⁠1/4⁠ *ε*.
8. *Andersen, C. M.; Geer, James F. (June 1982). "Power Series Expansions for the Frequency and Period of the Limit Cycle of the Van Der Pol Equation". *SIAM Journal on Applied Mathematics*. **42** (3): 678–693. doi:10.1137/0142047. ISSN 0036-1399.*
9. *Bellman, Richard (2003). "2.5. The Shohat Expansion". *Perturbation techniques in mathematics, engineering & physics*. Mineola, N.Y.: Dover Publications. ISBN 0-486-43258-0. OCLC 51942387.*

Retrieved from "

https://en.wikipedia.org/w/index.php?title=Poincaré–Lindstedt_method&oldid=1311082139

"
