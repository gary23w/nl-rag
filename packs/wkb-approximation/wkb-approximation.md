---
title: "WKB approximation"
source: https://en.wikipedia.org/wiki/WKB_approximation
domain: wkb-approximation
license: CC-BY-SA-4.0
tags: wkb approximation, eikonal equation, semiclassical physics, stokes phenomenon
fetched: 2026-07-02
---

# WKB approximation

In mathematical physics, the **WKB approximation** or **WKB method** is a technique for finding approximate solutions to linear differential equations with spatially varying coefficients. It is typically used for a semiclassical calculation in quantum mechanics in which the wave function is recast as an exponential function, semiclassically expanded, and then either the amplitude or the phase is taken to be changing slowly.

The name is an initialism for **Wentzel–Kramers–Brillouin**. It is also known as the **LG** or **Liouville–Green method**. Other often-used letter combinations include **JWKB** and **WKBJ**, where the "J" stands for Jeffreys.

## Brief history

This method is named after physicists Gregor Wentzel, Hendrik Anthony Kramers, and Léon Brillouin, who all developed it in 1926. In 1923, mathematician Harold Jeffreys had developed a general method of approximating solutions to linear, second-order differential equations, a class that includes the Schrödinger equation. The Schrödinger equation itself was not developed until two years later, and Wentzel, Kramers, and Brillouin were apparently unaware of this earlier work, so Jeffreys is often neglected credit. Early texts in quantum mechanics contain any number of combinations of their initials, including WBK, BWK, WKBJ, JWKB and BWKJ. An authoritative discussion and critical survey has been given by Robert B. Dingle.

Earlier appearances of essentially equivalent methods are: Francesco Carlini in 1817, Joseph Liouville in 1837, George Green in 1837, Lord Rayleigh in 1912 and Richard Gans in 1915. Liouville and Green may be said to have founded the method in 1837, and it is also commonly referred to as the Liouville–Green or LG method.

The important contribution of Jeffreys, Wentzel, Kramers, and Brillouin to the method was the inclusion of the treatment of turning points, connecting the evanescent and oscillatory solutions at either side of the turning point. For example, this may occur in the Schrödinger equation, due to a potential energy hill.

## Formulation

The WKB method approximates the solution of a differential equation whose highest derivative is multiplied by a small parameter $\varepsilon$ . For a differential equation $\varepsilon {\frac {d^{n}y}{dx^{n}}}+a(x){\frac {d^{n-1}y}{dx^{n-1}}}+\cdots +k(x){\frac {dy}{dx}}+m(x)y=0,$ assume a solution of the form of an asymptotic series expansion $y(x)\sim \exp \left[{\frac {1}{\delta }}\sum _{n=0}^{\infty }\delta ^{n}S_{n}(x)\right]$ in the limit $\delta \rightarrow 0$ . The asymptotic scaling of $\delta$ in terms of $\varepsilon$ will be determined by the equation. See the example below.

Substituting the above ansatz into the differential equation and cancelling out the exponential terms allows one to solve for an arbitrary number of terms $S_{n}(x)$ in the expansion.

WKB theory is a special case of multiple scale analysis.

## An example

This example comes from the text of Carl M. Bender and Steven Orszag. Consider the second-order homogeneous linear differential equation $\varepsilon ^{2}{\frac {d^{2}y}{dx^{2}}}=Q(x)\,y,$ where $Q(x)\neq 0$ . Substituting $y(x)=\exp \left[{\frac {1}{\delta }}\sum _{n=0}^{\infty }\delta ^{n}S_{n}(x)\right]$ results in the equation $\varepsilon ^{2}\left[{\frac {1}{\delta ^{2}}}\left(\sum _{n=0}^{\infty }\delta ^{n}S_{n}^{\prime }\right)^{2}+{\frac {1}{\delta }}\sum _{n=0}^{\infty }\delta ^{n}S_{n}^{\prime \prime }\right]=Q(x).$ To leading order in $\varepsilon$ (assuming, for the moment, the series will be asymptotically consistent), the above can be approximated as ${\frac {\varepsilon ^{2}}{\delta ^{2}}}{S_{0}^{\prime }}^{2}+{\frac {2\varepsilon ^{2}}{\delta }}S_{0}^{\prime }S_{1}^{\prime }+{\frac {\varepsilon ^{2}}{\delta }}S_{0}^{\prime \prime }=Q(x).$ In the limit $\delta \rightarrow 0$ , the dominant balance is given by ${\frac {\varepsilon ^{2}}{\delta ^{2}}}{S_{0}^{\prime }}^{2}\sim Q(x).$ So $\delta$ is proportional to $\varepsilon$ . Setting them equal and comparing powers yields $\varepsilon ^{0}:\quad {S_{0}^{\prime }}^{2}=Q(x),$ which can be recognized as the eikonal equation, with solution $S_{0}(x)=\pm \int _{x_{0}}^{x}{\sqrt {Q(x')}}\,dx'.$ Considering first-order powers of $\varepsilon$ fixes $\varepsilon ^{1}:\quad 2S_{0}^{\prime }S_{1}^{\prime }+S_{0}^{\prime \prime }=0.$ This has the solution $S_{1}(x)=-{\frac {1}{4}}\ln Q(x)+k_{1},$ where $k_{1}$ is an arbitrary constant.

We now have a pair of approximations to the system (a pair, because $S_{0}$ can take two signs); the first-order WKB approximation will be a linear combination of the two: $y(x)\approx c_{1}Q^{-{\frac {1}{4}}}(x)\exp \left({\frac {1}{\varepsilon }}\int _{x_{0}}^{x}{\sqrt {Q(t)}}\,dt\right)+c_{2}Q^{-{\frac {1}{4}}}(x)\exp \left(-{\frac {1}{\varepsilon }}\int _{x_{0}}^{x}{\sqrt {Q(t)}}\,dt\right).$ Higher-order terms can be obtained by looking at equations for higher powers of $\delta$ . Explicitly, $2S_{0}^{\prime }S_{n}^{\prime }+S_{n-1}^{\prime \prime }+\sum _{j=1}^{n-1}S_{j}^{\prime }S_{n-j}^{\prime }=0$ for $n\geq 2$ .

### Precision of the asymptotic series

The asymptotic series for *y*(*x*) is usually a divergent series, whose general term $\delta ^{n}S_{n}(x)$ starts to increase after a certain value $n=n_{\textrm {max}}$ . Therefore, the smallest error achieved by the WKB method is at best of the order of the last included term.

For the equation $\varepsilon ^{2}{\frac {d^{2}y}{dx^{2}}}=Q(x)y,$ with $Q(x)<0$ an analytic function, the value $n_{\max }$ and the magnitude of the last term can be estimated as follows: $n_{\max }\approx {\frac {2}{\varepsilon }}\left|\int _{x_{0}}^{x_{\ast }}{\sqrt {-Q(z)}}\,dz\right|,$ $\delta ^{n_{\max }}S_{n_{\max }}(x_{0})\approx {\sqrt {\frac {2\pi }{n_{\max }}}}e^{-n_{\max }},$ where $x_{0}$ is the point at which $y(x_{0})$ needs to be evaluated and $x_{\ast }$ is the (complex) turning point where $Q(x_{\ast })=0$ , closest to $x=x_{0}$ .

The number $n_{\max }$ can be interpreted as the number of oscillations between $x_{0}$ and the closest turning point.

If $\varepsilon ^{-1}Q(x)$ is a slowly changing function, $\varepsilon \left|{\frac {dQ}{dx}}\right|\ll Q^{2},^{{\text{[might be }}Q^{3/2}{\text{?]}}}$ the number $n_{\max }$ will be large, and the minimum error of the asymptotic series will be exponentially small.

## Application in non-relativistic quantum mechanics

The above example may be applied specifically to the one-dimensional, time-independent Schrödinger equation, $-{\frac {\hbar ^{2}}{2m}}{\frac {d^{2}}{dx^{2}}}\Psi (x)+V(x)\Psi (x)=E\Psi (x),$ which can be rewritten as ${\frac {d^{2}}{dx^{2}}}\Psi (x)={\frac {2m}{\hbar ^{2}}}\left(V(x)-E\right)\Psi (x).$ Approximation away from the turning points

The wave function can be rewritten as the exponential of another function S (closely related to the action), which could be complex,

$\Psi (\mathbf {x} )=e^{iS(\mathbf {x} )/\hbar },$ so that its substitution in Schrödinger's equation gives: $i\hbar \nabla ^{2}S(\mathbf {x} )-\left(\nabla S(\mathbf {x} )\right)^{2}=2m\left(V(\mathbf {x} )-E\right),$ Next, the semi-classical approximation is used. This means that each function is expanded as a power series in $\hbar$ : $S=S_{0}+\hbar S_{1}+\hbar ^{2}S_{2}+\cdots$ Substituting in the equation, and only retaining terms up to first order in $\hbar$ , one gets $\left(\nabla S_{0}+\hbar \nabla S_{1}\right)^{2}-i\hbar \left(\nabla ^{2}S_{0}\right)=2m\left(E-V(\mathbf {x} )\right),$ which gives the following two relations: ${\begin{aligned}\left(\nabla S_{0}\right)^{2}=2m\left(E-V(\mathbf {x} )\right)&=\left(p(\mathbf {x} )\right)^{2}\\[1ex]2\nabla S_{0}\cdot \nabla S_{1}-i\nabla ^{2}S_{0}&=0.\end{aligned}}$ These can be solved for one-dimension systems. The first equation can be solved by $S_{0}(x)=\pm \int {\sqrt {2m\left(E-V(x)\right)}}\,dx=\pm \int p(x)\,dx,$ and the second equation computed for the possible values of the above, is generally expressed as: $\Psi (x)\approx C_{+}{\frac {e^{+{\frac {i}{\hbar }}\int p(x)\,dx}}{\sqrt {|p(x)|}}}+C_{-}{\frac {e^{-{\frac {i}{\hbar }}\int p(x)\,dx}}{\sqrt {|p(x)|}}}$ Thus, the resulting wave function in first order WKB approximation is presented as,

$\Psi (x)\approx {\frac {C_{+}e^{+{\frac {i}{\hbar }}\int {\sqrt {2m\left(E-V(x)\right)}}\,dx}+C_{-}e^{-{\frac {i}{\hbar }}\int {\sqrt {2m\left(E-V(x)\right)}}\,dx}}{\sqrt[{4}]{2m\left|E-V(x)\right|}}}$

In the classically allowed region, namely the region where $V(x)<E$ the integrand in the exponent is imaginary and the approximate wave function is oscillatory. In the classically forbidden region $V(x)>E$ , the solutions are growing or decaying. It is evident in the denominator that both of these approximate solutions become singular near the classical **turning points**, where $E=V(x)$ , and cannot be valid. (The turning points are the points where the classical particle changes direction.)

Hence, when $E>V(x)$ , the wave function can be chosen to be expressed as: $\Psi (x')\approx {\frac {1}{\sqrt {|p(x)|}}}\left[C\cos \left({\frac {1}{\hbar }}\int \left|p(x)\right|dx+\alpha \right)+D\sin \left(-{\frac {1}{\hbar }}\int \left|p(x)\right|dx+\alpha \right)\right]$ and for $V(x)>E$ , $\Psi (x')\approx {\frac {C_{+}e^{-{\frac {1}{\hbar }}\int |p(x)|\,dx}}{\sqrt {|p(x)|}}}+{\frac {C_{-}e^{+{\frac {1}{\hbar }}\int |p(x)|\,dx}}{\sqrt {|p(x)|}}}.$ The integration in this solution is computed between the classical turning point and the arbitrary position $x'$ .

### Validity of WKB solutions

From the condition: $\left(S_{0}'(x)\right)^{2}-\left(p(x)\right)^{2}+\hbar \left(2S_{0}'(x)S_{1}'(x)-iS_{0}''(x)\right)=0$

It follows that: ${\textstyle \hbar \left|2S_{0}'(x)S_{1}'(x)\right|+\hbar \left|iS_{0}''(x)\right|\ll \left|(S_{0}'(x))^{2}\right|+\left|(p(x))^{2}\right|}$

For which the following two inequalities are equivalent since the terms in either side are equivalent, as used in the WKB approximation:

${\begin{aligned}\hbar \left|S_{0}''(x)\right|&\ll \left|(S_{0}'(x))^{2}\right|\\2\hbar \left|S_{0}'S_{1}'\right|&\ll \left|(p'(x))^{2}\right|\end{aligned}}$

The first inequality can be used to show the following:

${\begin{aligned}\hbar \left|S_{0}''(x)\right|&\ll \left|p(x)\right|^{2}\\[6pt]{\frac {1}{2}}{\frac {\hbar }{|p(x)|}}\left|{\frac {dp^{2}}{dx}}\right|&\ll \left|p(x)\right|^{2}\\[6pt]\lambda \left|{\frac {dV}{dx}}\right|&\ll {\frac {\left|p\right|^{2}}{m}}\\\end{aligned}}$

where ${\textstyle |S_{0}'(x)|=|p(x)|}$ is used and ${\textstyle \lambda (x)}$ is the local de Broglie wavelength of the wave function. The inequality implies that the variation of potential is assumed to be slowly varying. This condition can also be restated as the fractional change of ${\textstyle E-V(x)}$ or that of the momentum ${\textstyle p(x)}$ , over the wavelength ${\textstyle \lambda }$ , being much smaller than ${\textstyle 1}$ .

Similarly it can be shown that ${\textstyle \lambda (x)}$ also has restrictions based on underlying assumptions for the WKB approximation that: $\left|{\frac {d\lambda }{dx}}\right|\ll 1$ which implies that the de Broglie wavelength of the particle is slowly varying.

### Behavior near the turning points

We now consider the behavior of the wave function near the turning points. For this, we need a different method. Near the first turning points, $x_{1}$ , the term ${\textstyle {\frac {2m}{\hbar ^{2}}}\left(V(x)-E\right)}$ can be expanded in a power series, ${\frac {2m}{\hbar ^{2}}}\left(V(x)-E\right)=U_{1}\cdot (x-x_{1})+U_{2}\cdot (x-x_{1})^{2}+\cdots \;.$ To first order, one finds ${\frac {d^{2}}{dx^{2}}}\Psi (x)=U_{1}\cdot (x-x_{1})\cdot \Psi (x).$ This differential equation is known as the Airy equation, and the solution may be written in terms of Airy functions, ${\begin{aligned}\Psi (x)&=C_{A}\operatorname {Ai} \left({\sqrt[{3}]{U_{1}}}\cdot (x-x_{1})\right)+C_{B}\operatorname {Bi} \left({\sqrt[{3}]{U_{1}}}\cdot (x-x_{1})\right)\\[6pt]&=C_{A}\operatorname {Ai} \left(u\right)+C_{B}\operatorname {Bi} \left(u\right).\end{aligned}}$ Although for any fixed value of $\hbar$ , the wave function is bounded near the turning points, the wave function will be peaked there, as can be seen in the images above. As $\hbar$ gets smaller, the height of the wave function at the turning points grows. It also follows from this approximation that: ${\begin{aligned}{\frac {1}{\hbar }}\int p(x)\,dx&={\sqrt {U_{1}}}\int {\sqrt {x-a}}\,dx\\&={\frac {2}{3}}\left[{\sqrt[{3}]{U_{1}}}\left(x-a\right)\right]^{\frac {3}{2}}={\frac {2}{3}}u^{\frac {3}{2}}.\end{aligned}}$

### Connection conditions

It now remains to construct a global (approximate) solution to the Schrödinger equation. For the wave function to be square-integrable, we must take only the exponentially decaying solution in the two classically forbidden regions. These must then "connect" properly through the turning points to the classically allowed region. For most values of *E*, this matching procedure will not work: The function obtained by connecting the solution near $+\infty$ to the classically allowed region will not agree with the function obtained by connecting the solution near $-\infty$ to the classically allowed region. The requirement that the two functions agree imposes a condition on the energy *E*, which will give an approximation to the exact quantum energy levels.

The wavefunction's coefficients can be calculated for a simple problem shown in the figure. Let the first turning point, where the potential is decreasing over x, occur at $x=x_{1}$ and the second turning point, where potential is increasing over x, occur at $x=x_{2}$ . Given that we expect wavefunctions to be of the following form, we can calculate their coefficients by connecting the different regions using Airy and Bairy functions.

${\begin{aligned}\Psi _{V>E}(x)&\approx u^{-{\frac {1}{4}}}\left[A\exp \left({\tfrac {2}{3}}u^{\frac {3}{2}}\right)+B\exp \left(-{\tfrac {2}{3}}u^{\frac {3}{2}}\right)\right]\\[6pt]\Psi _{E>V}(x)&\approx u^{-{\frac {1}{4}}}\left[C\cos \left({\tfrac {2}{3}}u^{\frac {3}{2}}-\alpha \right)+D\sin \left({\tfrac {2}{3}}u^{\frac {3}{2}}-\alpha \right)\right]\\\end{aligned}}$

#### First classical turning point

For $U_{1}<0$ ie. decreasing potential condition or $x=x_{1}$ in the given example shown by the figure, we require the exponential function to decay for negative values of x so that wavefunction for it to go to zero. Considering Bairy functions to be the required connection formula, we get:

${\begin{aligned}\operatorname {Bi} (u)&\to -{\frac {1}{\sqrt {\pi }}}{\frac {1}{\sqrt[{4}]{u}}}\sin \left({\frac {2}{3}}|u|^{\frac {3}{2}}-{\frac {\pi }{4}}\right)&{\text{where}}\quad u\to -\infty \\[1ex]\operatorname {Bi} (u)&\to {\frac {1}{\sqrt {\pi }}}{\frac {1}{\sqrt[{4}]{u}}}\exp \left({\frac {2}{3}}u^{\frac {3}{2}}\right)&{\textrm {where}}\quad u\to +\infty \end{aligned}}$

We cannot use Airy function since it gives growing exponential behaviour for negative x. When compared to WKB solutions and matching their behaviours at $\pm \infty$ , we conclude:

$A=-D=N$ , $B=C=0$ and $\alpha ={\frac {\pi }{4}}$ .

Thus, letting some normalization constant be N , the wavefunction is given for increasing potential (with x) as:

$\Psi _{\text{WKB}}(x)={\frac {N}{\sqrt {|p(x)|}}}\cdot {\begin{cases}-\exp \left(-Q_{1}(x)\right)&{\text{if }}x<x_{1}\\\sin \left(Q_{1}(x)-{\frac {\pi }{4}}\right)&{\text{if }}x_{2}>x>x_{1}\\\end{cases}}$ where ${\textstyle Q_{1}(x)={\frac {1}{\hbar }}\int _{x}^{x_{1}}|p(x')|\,dx'}$ .

#### Second classical turning point

For $U_{1}>0$ ie. increasing potential condition or $x=x_{2}$ in the given example shown by the figure, we require the exponential function to decay for positive values of x so that wavefunction for it to go to zero. Considering Airy functions to be the required connection formula, we get:

${\begin{aligned}\operatorname {Ai} (u)&\rightarrow {\frac {1}{2{\sqrt {\pi }}}}{\frac {1}{\sqrt[{4}]{u}}}e^{-{\frac {2}{3}}u^{\frac {3}{2}}}&{\textrm {where,}}\quad u\rightarrow +\infty \\\operatorname {Ai} (u)&\rightarrow {\frac {1}{\sqrt {\pi }}}{\frac {1}{\sqrt[{4}]{u}}}\cos {\left({\frac {2}{3}}|u|^{\frac {3}{2}}-{\frac {\pi }{4}}\right)}&{\textrm {where,}}\quad u\rightarrow -\infty \\\end{aligned}}$

We cannot use Airy function of the second order since it gives growing exponential behaviour for positive x. When compared to WKB solutions and matching their behaviours at $\pm \infty$ , we conclude:

$2B=C=N'$ , $D=A=0$ and $\alpha ={\frac {\pi }{4}}$ .

Thus, letting some normalization constant be $N'$ , the wavefunction is given for increasing potential (with x) as:

$\Psi _{\text{WKB}}(x)={\begin{cases}{\frac {N'}{\sqrt {|p(x)|}}}\cos \left(Q_{2}(x)-{\frac {\pi }{4}}\right)&{\text{if }}x_{1}<x<x_{2}\\{\frac {N'}{2{\sqrt {|p(x)|}}}}\exp \left(Q_{2}(x)\right)&{\text{if }}x>x_{2}\end{cases}}$ where ${\textstyle Q_{2}(x)={\frac {1}{\hbar }}\int _{x}^{x_{2}}\left|p(x')\right|dx'}$ .

#### Common oscillating wavefunction

Matching the two solutions for region $x_{1}<x<x_{2}$ , it is required that the difference between the angles in these functions is $\pi (n+1/2)$ where the ${\frac {\pi }{2}}$ phase difference accounts for changing cosine to sine for the wavefunction and $n\pi$ difference since negation of the function can occur by letting $N=(-1)^{n}N'$ . Thus: $\int _{x_{1}}^{x_{2}}{\sqrt {2m\left(E-V(x)\right)}}\,dx=\left(n+{\tfrac {1}{2}}\right)\pi \hbar ,$ Where *n* is a non-negative integer. This condition can also be rewritten as saying that:

The area enclosed by the classical energy curve is

$2\pi \hbar (n+1/2)$

.

Either way, the condition on the energy is a version of the Bohr–Sommerfeld quantization condition, with a "Maslov correction" equal to 1/2.

It is possible to show that after piecing together the approximations in the various regions, one obtains a good approximation to the actual eigenfunction. In particular, the Maslov-corrected Bohr–Sommerfeld energies are good approximations to the actual eigenvalues of the Schrödinger operator. Specifically, the error in the energies is small compared to the typical spacing of the quantum energy levels. Thus, although the "old quantum theory" of Bohr and Sommerfeld was ultimately replaced by the Schrödinger equation, some vestige of that theory remains, as an approximation to the eigenvalues of the appropriate Schrödinger operator.

#### General connection conditions

Thus, from the two cases the connection formula is obtained at a classical turning point, $x=a$ :

${\frac {N}{\sqrt {|p(x)|}}}\sin {\left({\frac {1}{\hbar }}\int _{x}^{a}|p(x)|dx-{\frac {\pi }{4}}\right)}\Longrightarrow -{\frac {N}{\sqrt {|p(x)|}}}\exp {\left({\frac {1}{\hbar }}\int _{a}^{x}|p(x)|dx\right)}$

and:

${\frac {N'}{\sqrt {|p(x)|}}}\cos {\left({\frac {1}{\hbar }}\int _{x}^{a}|p(x)|dx-{\frac {\pi }{4}}\right)}\Longleftarrow {\frac {N'}{2{\sqrt {|p(x)|}}}}\exp {\left(-{\frac {1}{\hbar }}\int _{a}^{x}|p(x)|dx\right)}$

The WKB wavefunction at the classical turning point away from it is approximated by oscillatory sine or cosine function in the classically allowed region, represented in the left and growing or decaying exponentials in the forbidden region, represented in the right. The implication follows due to the dominance of growing exponential compared to decaying exponential. Thus, the solutions of oscillating or exponential part of wavefunctions can imply the form of wavefunction on the other region of potential as well as at the associated turning point.

### Probability density

One can then compute the probability density associated to the approximate wave function. The probability that the quantum particle will be found in the classically forbidden region is small. In the classically allowed region, meanwhile, the probability the quantum particle will be found in a given interval is approximately the *fraction of time the classical particle spends in that interval* over one period of motion. Since the classical particle's velocity goes to zero at the turning points, it spends more time near the turning points than in other classically allowed regions. This observation accounts for the peak in the wave function (and its probability density) near the turning points.

Applications of the WKB method to Schrödinger equations with a large variety of potentials and comparison with perturbation methods and path integrals are treated in Müller-Kirsten.

## Examples in quantum mechanics

Although WKB potential only applies to smoothly varying potentials, in the examples where rigid walls produce infinities for potential, the WKB approximation can still be used to approximate wavefunctions in regions of smoothly varying potentials. Since the rigid walls have highly discontinuous potential, the connection condition cannot be used at these points and the results obtained can also differ from that of the above treatment.

### Bound states for 1 rigid wall

The potential of such systems can be given in the form:

$V(x)={\begin{cases}V(x)&{\text{if }}x\geq x_{1}\\\infty &{\text{if }}x<x_{1}\\\end{cases}}$

where ${\textstyle x_{1}<x_{2}}$ .

Finding wavefunction in bound region, i.e., within classical turning points ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ , by considering approximations far from ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ respectively we have two solutions:

${\begin{aligned}\Psi _{\text{WKB}}(x)&={\frac {A}{\sqrt {|p(x)|}}}\sin {\left({\frac {1}{\hbar }}\int _{x}^{x_{1}}|p(x)|dx+\alpha \right)}\\\Psi _{\text{WKB}}(x)&={\frac {B}{\sqrt {|p(x)|}}}\cos {\left({\frac {1}{\hbar }}\int _{x}^{x_{2}}|p(x)|dx+\beta \right)}\end{aligned}}$

Since wavefunction must vanish near ${\textstyle x_{1}}$ , we conclude ${\textstyle \alpha =0}$ . For airy functions near ${\textstyle x_{2}}$ , we require ${\textstyle \beta =-{\frac {\pi }{4}}}$ . We require that angles within these functions have a phase difference $\pi (n+1/2)$ where the ${\frac {\pi }{2}}$ phase difference accounts for changing sine to cosine and $n\pi$ allowing $B=(-1)^{n}A$ .

${\frac {1}{\hbar }}\int _{x_{1}}^{x_{2}}|p(x)|dx=\pi \left(n+{\frac {3}{4}}\right)$ Where *n* is a non-negative integer. Note that the right hand side of this would instead be $\pi (n-1/4)$ if n was only allowed to non-zero natural numbers.

Thus we conclude that, for ${\textstyle n=1,2,3,\cdots }$ $\int _{x_{1}}^{x_{2}}{\sqrt {2m\left(E-V(x)\right)}}\,dx=\left(n-{\frac {1}{4}}\right)\pi \hbar$ In 3 dimensions with spherically symmetry, the same condition holds where the position x is replaced by radial distance r, due to its similarity with this problem.

### Bound states within 2 rigid wall

The potential of such systems can be given in the form:

$V(x)={\begin{cases}\infty &{\text{if }}x>x_{2}\\V(x)&{\text{if }}x_{2}\geq x\geq x_{1}\\\infty &{\text{if }}x<x_{1}\\\end{cases}}$

where ${\textstyle x_{1}<x_{2}}$ .

For ${\textstyle E\geq V(x)}$ between ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ which are thus the classical turning points, by considering approximations far from ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ respectively we have two solutions:

${\begin{aligned}\Psi _{\text{WKB}}(x)&={\frac {A}{\sqrt {|p(x)|}}}\sin \left({\frac {1}{\hbar }}\int _{x}^{x_{1}}|p(x)|dx\right)\\\Psi _{\text{WKB}}(x)&={\frac {B}{\sqrt {|p(x)|}}}\sin \left({\frac {1}{\hbar }}\int _{x}^{x_{2}}|p(x)|dx\right)\end{aligned}}$

Since wavefunctions must vanish at ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ . Here, the phase difference only needs to account for $n\pi$ which allows $B=(-1)^{n}A$ . Hence the condition becomes:

$\int _{x_{1}}^{x_{2}}{\sqrt {2m\left(E-V(x)\right)}}\,dx=n\pi \hbar$ where ${\textstyle n=1,2,3,\cdots }$ but not equal to zero since it makes the wavefunction zero everywhere.

### Quantum bouncing ball

Consider the following potential a bouncing ball is subjected to:

$V(x)={\begin{cases}mgx&{\text{if }}x\geq 0\\\infty &{\text{if }}x<0\end{cases}}$

The wavefunction solutions of the above can be solved using the WKB method by considering only odd parity solutions of the alternative potential $V(x)=mg|x|$ . The classical turning points are identified ${\textstyle x_{1}=-{E \over mg}}$ and ${\textstyle x_{2}={E \over mg}}$ . Thus applying the quantization condition obtained in WKB:

$\int _{x_{1}}^{x_{2}}{\sqrt {2m\left(E-V(x)\right)}}\,dx=(n_{\text{odd}}+1/2)\pi \hbar$

Letting ${\textstyle n_{\text{odd}}=2n-1}$ where ${\textstyle n=1,2,3,\cdots }$ , solving for ${\textstyle E}$ with given $V(x)=mg|x|$ , we get the quantum mechanical energy of a bouncing ball:

$E={\left(3\left(n-{\frac {1}{4}}\right)\pi \right)^{\frac {2}{3}} \over 2}(mg^{2}\hbar ^{2})^{\frac {1}{3}}.$

This result is also consistent with the use of equation from bound state of one rigid wall without needing to consider an alternative potential.

### Quantum tunneling

The potential of such systems can be given in the form:

$V(x)={\begin{cases}0&{\text{if }}x<x_{1}\\V(x)&{\text{if }}x_{2}\geq x\geq x_{1}\\0&{\text{if }}x>x_{2}\\\end{cases}}$

where ${\textstyle x_{1}<x_{2}}$ .

Its solutions for an incident wave is given as

$\psi (x)={\begin{cases}Ae^{ik_{0}x}+Be^{-ik_{0}x}&{\text{if }}x<x_{1}\\[1ex]{\frac {C}{\sqrt {|p(x)|}}}\exp \left(-{\frac {1}{\hbar }}\int _{x_{1}}^{x}|p(x)|dx\right)&{\text{if }}x_{2}\geq x\geq x_{1}\\[1ex]De^{ik_{0}x}&{\text{if }}x>x_{2}\end{cases}}$

with $k_{0}=p_{0}/\hbar$ , where the wavefunction in the classically forbidden region is the WKB approximation but neglecting the growing exponential. This is a fair assumption for wide potential barriers through which the wavefunction is not expected to grow to high magnitudes.

By the requirement of continuity of wavefunction and its derivatives, the following relation can be shown: ${\frac {|D|^{2}}{|A|^{2}}}={\frac {4}{(1+{a_{1}^{2}}/{p_{0}^{2}})}}{\frac {a_{1}}{a_{2}}}\exp \left(-{\frac {2}{\hbar }}\int _{x_{1}}^{x_{2}}|p(x')|dx'\right)$

where $a_{1}=|p(x_{1})|$ and $a_{2}=|p(x_{2})|$ .

Using ${\textstyle \mathbf {J} (\mathbf {x} ,t)={\frac {i\hbar }{2m}}\left(\psi ^{*}\nabla \psi -\psi \nabla \psi ^{*}\right)}$ we express the values without signs as:

${\begin{aligned}J_{\text{inc.}}&={\tfrac {\hbar }{2m}}\left({\tfrac {2p_{0}}{\hbar }}|A|^{2}\right)\\J_{\text{ref.}}&={\tfrac {\hbar }{2m}}\left({\tfrac {2p_{0}}{\hbar }}|B|^{2}\right)\\J_{\text{trans.}}&={\tfrac {\hbar }{2m}}\left({\tfrac {2p_{0}}{\hbar }}|D|^{2}\right)\end{aligned}}$

Thus, the transmission coefficient is found to be:

$T={\frac {|D|^{2}}{|A|^{2}}}={\frac {4}{\left(1+{a_{1}^{2}}/{p_{0}^{2}}\right)}}{\frac {a_{1}}{a_{2}}}\exp \left(-{\frac {2}{\hbar }}\int _{x_{1}}^{x_{2}}|p(x')|dx'\right)$

where ${\textstyle p(x)={\sqrt {2m\left(E-V(x)\right)}}}$ , $a_{1}=|p(x_{1})|$ and $a_{2}=|p(x_{2})|$ . The result can be stated as ${\textstyle T\sim ~e^{-2\gamma }}$ where ${\textstyle \gamma =\int _{x_{1}}^{x_{2}}|p(x')|dx'}$ .

## Exact WKB

The above theory is not entirely rigorous, because of the divergence of the asymptotic series. A modification of this is possible and a convergent series has been constructed by Gérard and Grigis, based on previous work by Ecalle and Voros. An application to the non-self-adjoint Dirac operator followed and this has made possible the rigorous justification of the asymptotic study of the semiclassical behavior of the associated NLS equation.
