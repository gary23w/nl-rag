---
title: "Final value theorem"
source: https://en.wikipedia.org/wiki/Final_value_theorem
domain: laplace-transform
license: CC-BY-SA-4.0
tags: laplace transform, inverse laplace transform, transfer function, final value theorem
fetched: 2026-07-02
---

# Final value theorem

In mathematical analysis, the **final value theorem** (FVT) is one of several similar theorems used to relate frequency domain expressions to the time domain behavior as time approaches infinity. Mathematically, if $f(t)$ in continuous time has (unilateral) Laplace transform $F(s)$ , then a final value theorem establishes conditions under which $\lim _{t\,\to \,\infty }f(t)=\lim _{s\,\to \,0}{sF(s)}.$ Likewise, if $f[k]$ in discrete time has (unilateral) Z-transform $F(z)$ , then a final value theorem establishes conditions under which $\lim _{k\,\to \,\infty }f[k]=\lim _{z\,\to \,1}{(z-1)F(z)}.$

An Abelian final value theorem makes assumptions about the time-domain behavior of $f(t){\text{ (or }}f[k])$ to calculate ${\textstyle \lim _{s\,\to \,0}{sF(s)}.}$ Conversely, a Tauberian final value theorem makes assumptions about the frequency-domain behaviour of $F(s)$ to calculate $\lim _{t\to \infty }f(t)$ ${\text{(or }}\lim _{k\to \infty }f[k])$ (see Abelian and Tauberian theorems for integral transforms).

## Final value theorems for the Laplace transform

### Deducing lim*t* → ∞ *f*(*t*)

In the following statements, the notation ${\text{‘}}s\to 0{\text{’}}$ means that s approaches 0, whereas ${\text{‘}}s\downarrow 0{\text{’}}$ means that s approaches 0 through the positive numbers.

#### Standard Final Value Theorem

Suppose that every pole of $F(s)$ is either in the open left half plane or at the origin, and that $F(s)$ has at most a single pole at the origin. Then $\lim _{t\to \infty }f(t)=\lim _{s\to 0}sF(s).$

#### Final Value Theorem using Laplace transform of the derivative

Suppose that $f(t)$ and $f'(t)$ both have Laplace transforms that exist for all $s>0.$ If $\lim _{t\to \infty }f(t)$ exists and $\lim _{s\,\to \,0}{sF(s)}$ exists then $\lim _{t\to \infty }f(t)=\lim _{s\,\to \,0}{sF(s)}.$

*Remark*

Both limits must exist for the theorem to hold. For example, if $f(t)=\sin(t)$ then $\lim _{t\to \infty }f(t)$ does not exist, but $\lim _{s\,\to \,0}{sF(s)}=\lim _{s\,\to \,0}{\frac {s}{s^{2}+1}}=0.$

#### Improved Tauberian converse Final Value Theorem

Suppose that $f:(0,\infty )\to \mathbb {C}$ is bounded and differentiable, and that $tf'(t)$ is also bounded on $(0,\infty )$ . If $sF(s)\to L\in \mathbb {C}$ as $s\to 0$ then $\lim _{t\to \infty }f(t)=L.$

#### Extended Final Value Theorem

Suppose that F is a proper rational function and that every pole of F is either in the open left half-plane or at the origin. Then one of the following occurs:

1. $sF(s)\to L\in \mathbb {R}$ as $s\downarrow 0,$ and $\lim _{t\to \infty }f(t)=L.$
2. $sF(s)\to +\infty \in \mathbb {R}$ as $s\downarrow 0,$ and $f(t)\to +\infty$ as $t\to \infty .$
3. $sF(s)\to -\infty \in \mathbb {R}$ as $s\downarrow 0,$ and $f(t)\to -\infty$ as $t\to \infty .$

In particular, if $s=0$ is a multiple pole of $F(s)$ then case 2 or 3 applies $(f(t)\to +\infty {\text{ or }}f(t)\to -\infty ).$

#### Generalized Final Value Theorem

Suppose that $f(t)$ is Laplace transformable. Let $\lambda >-1$ . If ${\textstyle \lim _{t\to \infty }{\frac {f(t)}{t^{\lambda }}}}$ exists and ${\textstyle \lim _{s\downarrow 0}{s^{\lambda +1}F(s)}}$ exists then

$\lim _{t\to \infty }{\frac {f(t)}{t^{\lambda }}}={\frac {1}{\Gamma (\lambda +1)}}\lim _{s\downarrow 0}{s^{\lambda +1}F(s)},$

where $\Gamma (x)$ denotes the Gamma function.

#### Applications

Final value theorems for obtaining $\lim _{t\to \infty }f(t)$ have applications in establishing the long-term stability of a system.

### Deducing lim*s* → 0 *s* *F*(*s*)

#### Abelian Final Value Theorem

Suppose that $f:(0,\infty )\to \mathbb {C}$ is bounded and measurable and $\lim _{t\to \infty }f(t)=\alpha \in \mathbb {C} .$ Then $F(s)$ exists for all $s>0$ and $\lim _{s\,\downarrow \,0}{sF(s)}=\alpha .$

*Elementary proof*

Suppose for convenience that $|f(t)|\leq 1$ on $(0,\infty ),$ and let $\alpha =\lim _{t\to \infty }f(t)$ . Let $\epsilon >0,$ and choose A so that $|f(t)-\alpha |<\epsilon$ for all $t>A.$ Since $s\int _{0}^{\infty }e^{-st}\,\mathrm {d} t=1,$ for every $s>0$ we have

$sF(s)-\alpha =s\int _{0}^{\infty }(f(t)-\alpha )e^{-st}\,\mathrm {d} t;$

hence

$|sF(s)-\alpha |\leq s\int _{0}^{A}|f(t)-\alpha |e^{-st}\,\mathrm {d} t+s\int _{A}^{\infty }|f(t)-\alpha |e^{-st}\,\mathrm {d} t\leq 2s\int _{0}^{A}e^{-st}\,\mathrm {d} t+\epsilon s\int _{A}^{\infty }e^{-st}\,\mathrm {d} t\equiv I+II.$

Now for every $s>0$ we have

$II<\epsilon s\int _{0}^{\infty }e^{-st}\,\mathrm {d} t=\epsilon .$

On the other hand, since $A<\infty$ is fixed it is clear that $\lim _{s\to 0}I=0$ , and so $|sF(s)-\alpha |<\epsilon$ if $s>0$ is small enough.

#### Final Value Theorem using Laplace transform of the derivative

Suppose that all of the following conditions are satisfied:

1. $f:(0,\infty )\to \mathbb {C}$ is continuously differentiable and both f and $f'$ have a Laplace transform
2. $f'$ is absolutely integrable - that is, $\int _{0}^{\infty }|f'(\tau )|\,\mathrm {d} \tau$ is finite
3. $\lim _{t\to \infty }f(t)$ exists and is finite

Then $\lim _{s\to 0^{+}}sF(s)=\lim _{t\to \infty }f(t).$

*Remark*

The proof uses the dominated convergence theorem.

#### Final Value Theorem for the mean of a function

Let $f:(0,\infty )\to \mathbb {C}$ be a continuous and bounded function such that such that the following limit exists

$\lim _{T\to \infty }{\frac {1}{T}}\int _{0}^{T}f(t)\,dt=\alpha \in \mathbb {C}$

Then $\lim _{s\,\to \,0,\,s>0}{sF(s)}=\alpha .$

#### Final Value Theorem for asymptotic sums of periodic functions

Suppose that $f:[0,\infty )\to \mathbb {R}$ is continuous and absolutely integrable in $[0,\infty ).$ Suppose further that f is asymptotically equal to a finite sum of periodic functions $f_{\mathrm {as} },$ that is

$|f(t)-f_{\mathrm {as} }(t)|<\phi (t),$

where $\phi (t)$ is absolutely integrable in $[0,\infty )$ and vanishes at infinity. Then

$\lim _{s\to 0}sF(s)=\lim _{t\to \infty }{\frac {1}{t}}\int _{0}^{t}f(x)\,\mathrm {d} x.$

#### Final Value Theorem for a function that diverges to infinity

Let $f(t):[0,\infty )\to \mathbb {R}$ satisfy all of the following conditions:

1. $f(t)$ is infinitely differentiable at zero
2. $f^{(k)}(t)$ has a Laplace transform for all non-negative integers k
3. $f(t)$ diverges to infinity as $t\to \infty$

Let $F(s)$ be the Laplace transform of $f(t)$ . Then $sF(s)$ diverges to infinity as $s\downarrow 0.$

#### Final Value Theorem for improperly integrable functions (Abel's theorem for integrals)

Let $h:[0,\infty )\to \mathbb {R}$ be measurable and such that the (possibly improper) integral $f(x):=\int _{0}^{x}h(t)\,\mathrm {d} t$ converges for $x\to \infty .$ Then $\int _{0}^{\infty }h(t)\,\mathrm {d} t:=\lim _{x\to \infty }f(x)=\lim _{s\downarrow 0}\int _{0}^{\infty }e^{-st}h(t)\,\mathrm {d} t.$ This is a version of Abel's theorem.

To see this, notice that $f'(t)=h(t)$ and apply the final value theorem to f after an integration by parts: For $s>0,$

$s\int _{0}^{\infty }e^{-st}f(t)\,\mathrm {d} t={\Big [}-e^{-st}f(t){\Big ]}_{t=o}^{\infty }+\int _{0}^{\infty }e^{-st}f'(t)\,\mathrm {d} t=\int _{0}^{\infty }e^{-st}h(t)\,\mathrm {d} t.$

By the final value theorem, the left-hand side converges to $\lim _{x\to \infty }f(x)$ for $s\to 0.$

To establish the convergence of the improper integral $\lim _{x\to \infty }f(x)$ in practice, Dirichlet's test for improper integrals is often helpful. An example is the Dirichlet integral.

#### Applications

Final value theorems for obtaining $\lim _{s\,\to \,0}{sF(s)}$ have applications in probability and statistics to calculate the moments of a random variable. Let $R(x)$ be cumulative distribution function of a continuous random variable X and let $\rho (s)$ be the Laplace–Stieltjes transform of $R(x).$ Then the n -th moment of X can be calculated as $E[X^{n}]=(-1)^{n}\left.{\frac {d^{n}\rho (s)}{ds^{n}}}\right|_{s=0}.$ The strategy is to write ${\frac {d^{n}\rho (s)}{ds^{n}}}={\mathcal {F}}{\bigl (}G_{1}(s),G_{2}(s),\dots ,G_{k}(s),\dots {\bigr )},$ where ${\mathcal {F}}(\dots )$ is continuous and for each $k,$ $G_{k}(s)=sF_{k}(s)$ for a function $F_{k}(s).$ For each $k,$ put $f_{k}(t)$ as the inverse Laplace transform of $F_{k}(s),$ obtain $\lim _{t\to \infty }f_{k}(t),$ and apply a final value theorem to deduce $\lim _{s\,\to \,0}{G_{k}(s)}=\lim _{s\,\to \,0}{sF_{k}(s)}=\lim _{t\to \infty }f_{k}(t).$ Then

$\left.{\frac {d^{n}\rho (s)}{ds^{n}}}\right|_{s=0}={\mathcal {F}}{\Bigl (}\lim _{s\,\to \,0}G_{1}(s),\lim _{s\,\to \,0}G_{2}(s),\dots ,\lim _{s\,\to \,0}G_{k}(s),\dots {\Bigr )},$

and hence $E[X^{n}]$ is obtained.

### Examples

#### Example where FVT holds

For example, for a system described by transfer function

$H(s)={\frac {6}{s+2}},$

the impulse response converges to

$\lim _{t\to \infty }h(t)=\lim _{s\to 0}{\frac {6s}{s+2}}=0.$

That is, the system returns to zero after being disturbed by a short impulse. However, the Laplace transform of the unit step response is

$G(s)={\frac {1}{s}}{\frac {6}{s+2}}$

and so the step response converges to

$\lim _{t\to \infty }g(t)=\lim _{s\to 0}{\frac {s}{s}}{\frac {6}{s+2}}={\frac {6}{2}}=3$

So a zero-state system will follow an exponential rise to a final value of 3.

#### Example where FVT does not hold

For a system described by the transfer function

$H(s)={\frac {9}{s^{2}+9}},$

the final value theorem *appears* to predict the final value of the impulse response to be 0 and the final value of the step response to be 1. However, neither time-domain limit exists, and so the final value theorem predictions are not valid. In fact, both the impulse response and step response oscillate, and (in this special case) the final value theorem describes the average values around which the responses oscillate.

There are two checks performed in Control theory which confirm valid results for the Final Value Theorem:

1. All non-zero roots of the denominator of $H(s)$ must have negative real parts.
2. $H(s)$ must not have more than one pole at the origin.

Rule 1 was not satisfied in this example, in that the roots of the denominator are $0+j3$ and $0-j3.$

## Final value theorems for the Z transform

### Deducing lim*k* → ∞ *f*[*k*]

#### Final Value Theorem

If $\lim _{k\to \infty }f[k]$ exists and $\lim _{z\,\to \,1}{(z-1)F(z)}$ exists then $\lim _{k\to \infty }f[k]=\lim _{z\,\to \,1}{(z-1)F(z)}.$

## Final value of linear systems

### Continuous-time LTI systems

Final value of the system

${\dot {\mathbf {x} }}(t)=\mathbf {A} \mathbf {x} (t)+\mathbf {B} \mathbf {u} (t)$

$\mathbf {y} (t)=\mathbf {C} \mathbf {x} (t)$

in response to a step input $\mathbf {u} (t)$ with amplitude R is:

$\lim _{t\to \infty }\mathbf {y} (t)=-\mathbf {CA} ^{-1}\mathbf {B} R$

### Sampled-data systems

The sampled-data system of the above continuous-time LTI system at the aperiodic sampling times $t_{i},i=1,2,...$ is the discrete-time system

${\mathbf {x} }(t_{i+1})=\mathbf {\Phi } (h_{i})\mathbf {x} (t_{i})+\mathbf {\Gamma } (h_{i})\mathbf {u} (t_{i})$

$\mathbf {y} (t_{i})=\mathbf {C} \mathbf {x} (t_{i})$

where $h_{i}=t_{i+1}-t_{i}$ and

$\mathbf {\Phi } (h_{i})=e^{\mathbf {A} h_{i}}$

,

$\mathbf {\Gamma } (h_{i})=\int _{0}^{h_{i}}e^{\mathbf {A} s}\,\mathrm {d} s$

The final value of this system in response to a step input $\mathbf {u} (t)$ with amplitude R is the same as the final value of its original continuous-time system.
