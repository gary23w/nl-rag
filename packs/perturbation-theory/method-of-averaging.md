---
title: "Method of averaging"
source: https://en.wikipedia.org/wiki/Method_of_averaging
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
---

# Method of averaging

In mathematics, more specifically in dynamical systems, the **method of averaging** (also called averaging theory) exploits systems containing time-scales separation: a *fast oscillation* **versus** a *slow drift*. It suggests that we perform an averaging over a given amount of time in order to iron out the fast oscillations and observe the qualitative behavior from the resulting dynamics. The approximated solution holds under finite time inversely proportional to the parameter denoting the slow time scale. It turns out to be a customary problem where there exists the trade off between how good is the approximated solution balanced by how much time it holds to be close to the original solution.

More precisely, the system has the following form ${\dot {x}}=\varepsilon f(x,t,\varepsilon ),\quad 0\leq \varepsilon \ll 1$ of a phase space variable $x.$ The *fast oscillation* is given by f **versus** a *slow drift* of ${\dot {x}}$ . The averaging method yields an autonomous dynamical system ${\dot {y}}=\varepsilon {\frac {1}{T}}\int _{0}^{T}f(y,s,0)~ds=:\varepsilon {\bar {f}}(y)$ which approximates the solution curves of ${\dot {x}}$ inside a connected and compact region of the phase space and over time of $1/\varepsilon$ .

Under the validity of this averaging technique, the asymptotic behavior of the original system is captured by the dynamical equation for y . In this way, qualitative methods for autonomous dynamical systems may be employed to analyze the equilibria and more complex structures, such as slow manifold and invariant manifolds, as well as their stability in the phase space of the averaged system.

In addition, in a physical application it might be reasonable or natural to replace a mathematical model, which is given in the form of the differential equation for ${\dot {x}}$ , with the corresponding averaged system ${\dot {y}}$ , in order to use the averaged system to make a prediction and then test the prediction against the results of a physical experiment.

The averaging method has a long history, which is deeply rooted in perturbation problems that arose in celestial mechanics (see, for example in ).

## First example

Consider a perturbed logistic growth ${\dot {x}}=\varepsilon (x(1-x)+\sin {t})\quad \quad x\in \mathbb {R} ,\quad 0\leq \varepsilon \ll 1,$ and the averaged equation ${\dot {y}}=\varepsilon y(1-y)\qquad y\in \mathbb {R} .$ The purpose of the method of averaging is to tell us the qualitative behavior of the vector field when we average it over a period of time. It guarantees that the solution $y(t)$ approximates $x(t)$ for times $t={\mathcal {O}}(1/\varepsilon ).$ **Exceptionally:** in this example the approximation is even better, it is valid for all times. We present it in a section below.

## Definitions

We assume the vector field $f:\mathbb {R} ^{n}\times \mathbb {R} \times \mathbb {R} \to \mathbb {R} ^{n}$ to be of differentiability class $C^{r}$ with $r\geq 2$ (or even we will only say smooth), which we will denote $f\in C^{r}(\mathbb {R} ^{n}\times \mathbb {R} \times \mathbb {R} ^{+};\mathbb {R} ^{n})$ . We expand this time-dependent vector field in a Taylor series (in powers of $\varepsilon$ ) with remainder $f^{[k+1]}(x,t,\varepsilon )$ . We introduce the following notation: $f(x,t,\varepsilon )=f^{0}(x,t)+\varepsilon f^{1}(x,t)+\dots +\varepsilon ^{k}f^{k}(x,t)+\varepsilon ^{k+1}f^{[k+1]}(x,t,\varepsilon ),$ where $f^{j}={\frac {f^{(j)}(x,t,0)}{j!}}$ is the j -th derivative with $0\leq j\leq k$ . As we are concerned with averaging problems, in general $f^{0}(x,t)$ is zero, so it turns out that we will be interested in vector fields given by $f(x,t,\varepsilon )=\varepsilon f^{[1]}(x,t,\varepsilon )=\varepsilon f^{1}(x,t)+\varepsilon ^{2}f^{[2]}(x,t,\varepsilon ).$ Besides, we define the following initial value problem to be in the **standard form**: ${\dot {x}}=\varepsilon f^{1}(x,t)+\varepsilon ^{2}f^{[2]}(x,t,\varepsilon ),\qquad x(0,\varepsilon )=:x_{0}\in D\subseteq \mathbb {R} ^{n},\quad 0\leq \varepsilon \ll 1.$

## Theorem: averaging in the periodic case

Consider for every $D\subset \mathbb {R} ^{n}$ connected and bounded and every $\varepsilon _{0}>0$ there exist $L>0$ and $\varepsilon \leq \varepsilon _{0}$ such that the original system (a non-autonomous dynamical system) given by ${\dot {x}}=\varepsilon f^{1}(x,t)+\varepsilon ^{2}f^{[2]}(x,t,\varepsilon ),\qquad x_{0}\in D\subseteq \mathbb {R} ^{n},\quad 0\leq \varepsilon \ll 1,$ has solution $x(t,\varepsilon )$ , where $f^{1}\in C^{r}(D\times \mathbb {R$ is periodic with period T and $f^{[2]}\in C^{r}(D\times \mathbb {R} \times \mathbb {R} ^{+};\mathbb {R} ^{n})$ both with $r\geq 2$ bounded on bounded sets. Then there exists a constant $c>0$ such that the solution $y(t,\varepsilon )$ of the *averaged* *system* (autonomous dynamical system) is ${\dot {y}}=\varepsilon {\frac {1}{T}}\int _{0}^{T}f^{1}(y,s)~ds=:\varepsilon {\bar {f}}^{1}(y),\quad y(0,\varepsilon )=x_{0}$ is $\|x(t,\varepsilon )-y(t,\varepsilon )\|<c\varepsilon$ for $0\leq \varepsilon \leq \varepsilon _{0}$ and $0\leq t\leq L/\varepsilon$ .

### Remarks

- There are two approximations in this what is called *first approximation* estimate: reduction to the average of the vector field and negligence of ${\mathcal {O}}(\varepsilon ^{2})$ terms.
- Uniformity with respect to the initial condition $x_{0}$ : if we vary $x_{0}$ this affects the estimation of L and c . The proof and discussion of this can be found in J. Murdock's book.
- Reduction of regularity: there is a more general form of this theorem which requires only $f^{1}$ to be Lipschitz and $f^{[2]}$ continuous. It is a more recent proof and can be seen in Sanders *et al.*. The theorem statement presented here is due to the proof framework proposed by Krylov-Bogoliubov which is based on an introduction of a near-identity transformation. The advantage of this method is the extension to more general settings such as infinite-dimensional systems - partial differential equation or delay differential equations.
- J. Hale presents generalizations to almost periodic vector-fields.

### Strategy of the proof

Krylov-Bogoliubov realized that the slow dynamics of the system determines the leading order of the asymptotic solution.

In order to prove it, they proposed a *near-identity transformation,* which turned out to be a change of coordinates with its own time-scale transforming the original system to the averaged one.

#### Sketch of the proof

1. Determination of a near-identity transformation: the smooth mapping $y\mapsto U(y,t,\varepsilon )=y+\varepsilon u^{[1]}(y,t,\varepsilon )$ where $u^{[1]}$ is assumed to be regular enough and T periodic. The proposed change of coordinates is given by $x=U(y,t,\varepsilon )$ .
2. Choose an appropriate $u^{[1]}$ solving the **homological equation** of the averaging theory: ${\frac {\partial u^{[1]}}{\partial t}}=f^{1}(y,t)-{\bar {f}}^{1}(y)$ .
3. Change of coordinates carries the original system to ${\dot {y}}=\varepsilon {\bar {f}}^{1}(y)+\varepsilon ^{2}f_{*}^{[2]}(y,t,\varepsilon ).$
4. Estimation of error due to truncation and comparison to the original variable.

## Non-autonomous class of systems: more examples

Along the history of the averaging technique, there is class of system extensively studied which give us meaningful examples we will discuss below. The class of system is given by: ${\ddot {z}}+z=\varepsilon g(z,{\dot {z}},t),\qquad z\in \mathbb {R} ,\quad z(0)=z_{0}~\mathrm {and} ~{\dot {z}}(0)=v_{0},$ where g is smooth. This system is similar to a linear system with a small nonlinear perturbation given by ${\begin{bmatrix}0\\\varepsilon ~g(z,{\dot {z}},t)\end{bmatrix}}$ : ${\begin{aligned}{\dot {z_{1}}}&=z_{2},&z_{1}(0)&=z_{0}\\{\dot {z_{2}}}&=-z_{1}+\varepsilon g(z_{1},z_{2},t),&z_{2}(0)&=v_{0},\end{aligned}}$ differing from the standard form. Hence there is a necessity to perform a transformation to make it in the standard form explicitly. We are able to change coordinates using variation of constants method. We look at the unperturbed system, i.e. $\varepsilon =0$ , given by ${\begin{bmatrix}{\dot {z_{1}}}\\{\dot {z_{2}}}\end{bmatrix}}={\begin{bmatrix}0&1\\-1&0\end{bmatrix}}{\begin{bmatrix}z_{1}\\z_{2}\end{bmatrix}}=A{\begin{bmatrix}z_{1}\\z_{2}\end{bmatrix}}$

which has the fundamental solution $\Phi (t)=e^{At}$ corresponding to a rotation. Then the time-dependent change of coordinates is $z(t)=\Phi (t)x$ where x is the coordinates respective to the standard form.

If we take the time derivative in both sides and invert the fundamental matrix we obtain ${\dot {x}}=\varepsilon e^{-At}{\begin{bmatrix}0\\~{\tilde {g}}(x,{\dot {x}},t)\end{bmatrix}}~{\text{ with }}~{\tilde {g}}(x,{\dot {x}},t)=g(\cos(t)x(t)+\sin(t){\dot {x}}(t),-\sin(t)x(t)+\cos(t){\dot {x}}(t),t).$

### Remarks

- The same can be done to time-dependent linear parts. Although the fundamental solution may be non-trivial to write down explicitly, the procedure is similar. See Sanders *et al.* for further details.
- If the eigenvalues of A are not all purely imaginary this is called hyperbolicity condition. For this occasion, the perturbation equation may present some serious problems even whether g is bounded, since the solution grows exponentially fast. However, qualitatively, we may be able to know the asymptotic solution, such as Hartman-Grobman results and more.
- Occasionally, polar coordinates may yield standard forms that are simpler to analyze. Consider $z_{1}=r\sin(t-\phi )~{\text{and}}~z_{2}=r\cos(t-\phi )$ , which determines the initial condition $(r(0),\phi (0))$ and the system ${\begin{bmatrix}{\dot {r}}\\{\dot {\phi }}\end{bmatrix}}=\varepsilon {\begin{bmatrix}\cos(t-\phi )g(r\sin(t-\phi ),r\cos(t-\phi ),t)\\{\frac {1}{r}}\sin(t-\phi )g(r\sin(t-\phi ),r\cos(t-\phi ),t)\end{bmatrix}}.$

If $g\in C^{1}$ we may apply averaging so long as a neighborhood of the origin is excluded (since the polar coordinates fail): ${\begin{array}{rcl}{\bar {f}}_{1}^{1}(r)&=&\displaystyle {\frac {1}{2\pi }}\int _{0}^{2\pi }\cos(s-\phi )g(r\sin(s-\phi ),r\cos(s-\phi ),s)ds\\[4pt]{\bar {f}}_{2}^{1}(r)&=&\displaystyle {\frac {1}{2\pi r}}\int _{0}^{2\pi }\sin(s-\phi )g(r\sin(s-\phi ),r\cos(s-\phi ),s)ds,\end{array}}$ where the averaged system is ${\begin{array}{lcr}{\dot {\bar {r}}}=\varepsilon {\bar {f}}_{1}^{1}({\bar {r}})\\{\dot {\bar {\phi }}}=\varepsilon {\bar {f}}_{2}^{1}({\bar {r}}).\end{array}}$

### Example: Misleading averaging results

The method contains some assumptions and restrictions. These limitations play important role when we average the original equation which is not into the standard form, and we can discuss counterexample of it. The following example in order to discourage this hurried averaging: ${\ddot {z}}+4\varepsilon \cos ^{2}{(t)}{\dot {z}}+z=0,\qquad z(0)=0,\quad {\dot {z}}(0)=1,$ where we put $g(z,{\dot {z}},t)=-4\cos ^{2}(t){\dot {z}}$ following the previous notation.

This systems corresponds to a damped harmonic oscillator where the damping term oscillates between 0 and $4\varepsilon$ . Averaging the friction term over one cycle of $2\pi$ yields the equation: ${\ddot {\bar {z}}}+2\varepsilon {\dot {\bar {z}}}+{\bar {z}}=0,\qquad {\bar {z}}(0)=0,\quad {\dot {\bar {z}}}(0)=1.$ The solution is ${\bar {z}}(t)={\frac {1}{(1-\varepsilon ^{2})^{\frac {1}{2}}}}e^{-\varepsilon t}\sin {((1-\varepsilon ^{2})^{\frac {1}{2}}t)}.$ which the convergence rate to the origin is $\varepsilon$ . The averaged system obtained from the standard form yields: ${\begin{array}{lcr}{\dot {\bar {r}}}=-{\frac {1}{2}}\varepsilon {\bar {r}}(2+\cos(2{\bar {\phi }})),~{\bar {r}}(0)=1\\{\dot {\bar {\phi }}}={\frac {1}{2}}\varepsilon \sin(2{\bar {\phi }}),~{\bar {\phi }}(0)=0,\end{array}}$ which in the rectangular coordinate shows explicitly that indeed the rate of convergence to the origin is ${\textstyle {\frac {3}{2}}\varepsilon }$ differing from the previous crude averaged system: $y(t)=e^{-{\frac {3}{2}}\varepsilon t}\sin {t}$

### Example: Van der Pol Equation

Van der Pol was concerned with obtaining approximate solutions for equations of the type ${\ddot {z}}+\varepsilon (1-z^{2}){\dot {z}}+z=0,$ where $g(z,{\dot {z}},t)=(1-z^{2}){\dot {z}}$ following the previous notation. This system is often called the Van der Pol oscillator. Applying periodic averaging to this nonlinear oscillator provides qualitative knowledge of the phase space without solving the system explicitly.

The averaged system is ${\begin{array}{lcr}{\dot {\bar {r}}}={\frac {1}{2}}\varepsilon {\bar {r}}(1-{\frac {1}{4}}{\bar {r}}^{2})\\{\dot {\bar {\phi }}}=0,\end{array}}$ and we can analyze the fixed points and their stability. There is an unstable fixed point at the origin and a stable limit cycle represented by ${\bar {r}}=2$ .

The existence of such stable limit-cycle can be stated as a theorem.

**Theorem (Existence of a periodic orbit)****:** If $p_{0}$ is a hyperbolic fixed point of ${\dot {y}}=\varepsilon {\bar {f}}^{1}(y)$ Then there exists $\varepsilon _{0}>0$ such that for all $0<\varepsilon <\varepsilon _{0}$ , ${\dot {x}}=\varepsilon f^{1}(x,t)+\varepsilon ^{2}f^{[2]}(x,t,\varepsilon )$ has a unique hyperbolic periodic orbit $\gamma _{\varepsilon }(t)=p_{0}+{\mathcal {O}}(\varepsilon )$ of the same stability type as $p_{0}$ .

The proof can be found at Guckenheimer and Holmes, Sanders *et al.* and for the angle case in Chicone.

### Example: Restricting the time interval

The average theorem assumes existence of a connected and bounded region $D\subset \mathbb {R} ^{n}$ which affects the time interval L of the result validity. The following example points it out. Consider the ${\ddot {z}}+z=8\varepsilon \cos {(t)}{\dot {z}}^{2},~z(0)=0,~{\dot {z}}(0)=1,$ where $g(z,{\dot {z}},t)=8{\dot {z}}^{2}\cos(t)$ . The averaged system consists of ${\begin{array}{lcr}{\dot {\bar {r}}}=3\varepsilon {\bar {r}}^{2}\cos({\bar {\phi }}),~{\bar {r}}(0)=1\\{\dot {\bar {\phi }}}=-\varepsilon {\bar {r}}\sin({\bar {\phi }}),~{\bar {\phi }}(0)=0,\end{array}}$ which under this initial condition indicates that the original solution behaves like $z(t)={\frac {\sin(t)}{1-3\varepsilon t}}+{\mathcal {O}}(\varepsilon ),$ where it holds on a bounded region over $0\leq \varepsilon t\leq L<{\frac {1}{3}}$ .

### Damped Pendulum

Consider a damped pendulum whose point of suspension is vibrated vertically by a small amplitude, high frequency signal (this is usually known as *dithering*). The equation of motion for such a pendulum is given by $m(l{\ddot {\theta }}-ak\omega ^{2}\sin \omega t\sin \theta )=-mg\sin \theta -k(l{\dot {\theta }}+a\omega \cos \omega t\sin \theta )$ where $a\sin \omega t$ describes the motion of the suspension point, k describes the damping of the pendulum, and $\theta$ is the angle made by the pendulum with the vertical.

The phase space form of this equation is given by ${\begin{aligned}{\dot {t}}&=1\\{\dot {\theta }}&=p\\{\dot {p}}&={\frac {1}{ml}}(mak\omega ^{2}\sin \omega t\sin \theta -mg\sin \theta -k(lp+a\omega \cos \omega t\sin \theta ))\end{aligned}}$ where we have introduced the variable p and written the system as an *autonomous*, first-order system in $(t,\theta ,p)$ -space.

Suppose that the angular frequency of the vertical vibrations, $\omega$ , is much greater than the natural frequency of the pendulum, ${\textstyle {\sqrt {g/l}}}$ . Suppose also that the amplitude of the vertical vibrations, a , is much less than the length l of the pendulum. The pendulum's trajectory in phase space will trace out a spiral around a curve C , moving along C at the slow rate ${\sqrt {g/l}}$ but moving around it at the fast rate $\omega$ . The radius of the spiral around C will be small and proportional to a . The average behaviour of the trajectory, over a timescale much larger than $2\pi /\omega$ , will be to follow the curve C .

## Extension error estimates

Average technique for initial value problems has been treated up to now with an validity error estimates of order $1/\varepsilon$ . However, there are circumstances where the estimates can be extended for further times, even the case for all times. Below we deal with a system containing an asymptotically stable fixed point. Such situation recapitulates what is illustrated in Figure 1.

**Theorem (Eckhaus** **/Sanchez-Palencia** **)** Consider the initial value problem ${\dot {x}}=\varepsilon f^{1}(x,t),\qquad x_{0}\in D\subseteq \mathbb {R} ^{n},\quad 0\leq \varepsilon \ll 1.$ Suppose ${\dot {y}}=\varepsilon \lim _{T\to \infty }{\frac {1}{T}}\int _{0}^{T}f^{1}(y,s)~ds=:\varepsilon {\bar {f}}^{1}(y),\quad y(0,\varepsilon )=x_{0}$ exists and contains an asymptotically stable fixed point $y=0$ in the linear approximation. Moreover, ${\bar {f}}^{1}$ is continuously differentiable with respect to y in D and has a domain of attraction $D^{0}\subset D$ . For any compact $K\subset D^{0}$ and for all $x_{0}\in K$ $\|x(t)-y(t)\|={\mathcal {O}}(\delta (\varepsilon )),\quad 0\leq t<\infty ,$ with $\delta (\varepsilon )=o(1)$ in the general case and ${\mathcal {O}}(\varepsilon )$ in the periodic case.
