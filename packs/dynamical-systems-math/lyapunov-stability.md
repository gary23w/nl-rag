---
title: "Lyapunov stability"
source: https://en.wikipedia.org/wiki/Lyapunov_stability
domain: dynamical-systems-math
license: CC-BY-SA-4.0
tags: dynamical system, phase space, bifurcation theory, lyapunov stability
fetched: 2026-07-02
---

# Lyapunov stability

Various types of stability may be discussed for the solutions of differential equations or difference equations describing dynamical systems. The most important type is that concerning the stability of solutions near to a point of equilibrium. This may be discussed by the theory of Aleksandr Lyapunov. In simple terms, if the solutions that start out near an equilibrium point $x_{e}$ stay near $x_{e}$ forever, then $x_{e}$ is **Lyapunov stable**. More strongly, if $x_{e}$ is Lyapunov stable and all solutions that start out near $x_{e}$ converge to $x_{e}$ , then $x_{e}$ is said to be ***asymptotically stable*** (see asymptotic analysis). The notion of *exponential stability* guarantees a minimal rate of decay, i.e., an estimate of how quickly the solutions converge. The idea of Lyapunov stability can be extended to infinite-dimensional manifolds, where it is known as structural stability, which concerns the behavior of different but "nearby" solutions to differential equations. Input-to-state stability (ISS) applies Lyapunov notions to systems with inputs.

## History

Lyapunov stability is named after Aleksandr Mikhailovich Lyapunov, a Russian mathematician who defended the thesis *The General Problem of Stability of Motion* at Kharkov University (now *VN Karazin Kharkiv National University*) in 1892. A. M. Lyapunov was a pioneer in successful endeavors to develop a global approach to the analysis of the stability of nonlinear dynamical systems by comparison with the widely spread local method of linearizing them about points of equilibrium. His work, initially published in Russian and then translated to French, received little attention for many years. The mathematical theory of stability of motion, founded by A. M. Lyapunov, considerably anticipated the time for its implementation in science and technology. Moreover Lyapunov did not himself make application in this field, his own interest being in the stability of rotating fluid masses with astronomical application. He did not have doctoral students who followed the research in the field of stability and his own destiny was terribly tragic because of his suicide in 1918. For several decades the theory of stability sank into complete oblivion. The Russian-Soviet mathematician and mechanician Nikolay Gur'yevich Chetaev working at the Kazan Aviation Institute in the 1930s was the first who realized the incredible magnitude of the discovery made by A. M. Lyapunov. The contribution to the theory made by N. G. Chetaev was so significant that many mathematicians, physicists and engineers consider him Lyapunov's direct successor and the next-in-line scientific descendant in the creation and development of the mathematical theory of stability.

The interest in it suddenly skyrocketed during the Cold War period when the so-called "Second Method of Lyapunov" (see below) was found to be applicable to the stability of aerospace guidance systems which typically contain strong nonlinearities not treatable by other methods. A large number of publications appeared then and since in the control and systems literature. More recently the concept of the Lyapunov exponent (related to Lyapunov's First Method of discussing stability) has received wide interest in connection with chaos theory. Lyapunov stability methods have also been applied to finding equilibrium solutions in traffic assignment problems.

## Definition for continuous-time systems

Consider an autonomous nonlinear dynamical system

${\dot {x}}=f(x(t)),\;\;\;\;x(0)=x_{0}$

,

where $x(t)\in {\mathcal {D}}\subseteq \mathbb {R} ^{n}$ denotes the system state vector, ${\mathcal {D}}$ an open set containing the origin, and $f:{\mathcal {D}}\rightarrow \mathbb {R} ^{n}$ is a continuous vector field on ${\mathcal {D}}$ . Suppose f has an equilibrium at $x_{e}$ , so that $f(x_{e})=0$ . Then:

1. This equilibrium is said to be **Lyapunov stable** if for every $\epsilon >0$ there exists a $\delta >0$ such that if $\|x(0)-x_{e}\|<\delta$ then for every $t\geq 0$ we have $\|x(t)-x_{e}\|<\epsilon$ .
2. The equilibrium of the above system is said to be **asymptotically stable** if it is Lyapunov stable and there exists $\delta >0$ such that if $\|x(0)-x_{e}\|<\delta$ then $\lim _{t\rightarrow \infty }\|x(t)-x_{e}\|=0$ .
3. The equilibrium of the above system is said to be **exponentially stable** if it is asymptotically stable and there exist $\alpha >0,~\beta >0,~\delta >0$ such that if $\|x(0)-x_{e}\|<\delta$ then $\|x(t)-x_{e}\|\leq \alpha \|x(0)-x_{e}\|e^{-\beta t}$ for all $t\geq 0$ .

Conceptually, the meanings of the above terms are the following:

1. Lyapunov stability of an equilibrium means that solutions starting "close enough" to the equilibrium (within a distance $\delta$ from it) remain "close enough" forever (within a distance $\epsilon$ from it). Note that this must be true for *any* $\epsilon$ that one may want to choose.
2. Asymptotic stability means that solutions that start close enough not only remain close enough but also eventually converge to the equilibrium.
3. Exponential stability means that solutions not only converge, but in fact converge faster than or at least as fast as a particular known rate $\alpha \|x(0)-x_{e}\|e^{-\beta t}$ .

The trajectory *$\phi (t)$* is (locally) *attractive* if

$\|x(t)-\phi (t)\|\rightarrow 0$

as

$t\rightarrow \infty$

for all trajectories $x(t)$ that start close enough to $\phi (t)$ , and *globally attractive* if this property holds for all trajectories.

That is, if *x* belongs to the interior of its stable manifold, it is *asymptotically stable* if it is both attractive and stable. (There are examples showing that attractivity does not imply asymptotic stability. Such examples are easy to create using homoclinic connections.)

If the Jacobian of the dynamical system at an equilibrium happens to be a stability matrix (i.e., if the real part of each eigenvalue is strictly negative), then the equilibrium is asymptotically stable.

### System of deviations

Instead of considering stability only near an equilibrium point (a constant solution $x(t)=x_{e}$ ), one can formulate similar definitions of stability near an arbitrary solution $x(t)=\phi (t)$ . However, one can reduce the more general case to that of an equilibrium by a change of variables called a "system of deviations". Define $y=x-\phi (t)$ , obeying the differential equation:

${\dot {y}}=f(t,y+\phi (t))-{\dot {\phi }}(t)=g(t,y)$

.

This is no longer an autonomous system, but it has a guaranteed equilibrium point at $y=0$ whose stability is equivalent to the stability of the original solution $x(t)=\phi (t)$ .

### Lyapunov's second method for stability

Lyapunov, in his original 1892 work, proposed two methods for demonstrating stability. The first method developed the solution in a series which was then proved convergent within limits. The second method, which is now referred to as the **Lyapunov stability criterion** or the Direct Method, makes use of a *Lyapunov function V(x)* which has an analogy to the potential function of classical dynamics. It is introduced as follows for a system ${\dot {x}}=f(x)$ having a point of equilibrium at $x=0$ . Consider a function $V:\mathbb {R} ^{n}\rightarrow \mathbb {R}$ such that

- $V(x)=0$ if and only if $x=0$
- $V(x)>0$ if and only if $x\neq 0$
- ${\dot {V}}(x)={\frac {d}{dt}}V(x)=\sum _{i=1}^{n}{\frac {\partial V}{\partial x_{i}}}f_{i}(x)=\nabla V\cdot f(x)\leq 0$ for all values of $x\neq 0$ . Note: for asymptotic stability, ${\dot {V}}(x)<0$ for $x\neq 0$ is required.

Then *V(x)* is called a Lyapunov function and the system is stable in the sense of Lyapunov. (Note that $V(0)=0$ is required; otherwise for example $V(x)=1/(1+|x|)$ would "prove" that ${\dot {x}}(t)=x$ is locally stable.) An additional condition called "properness" or "radial unboundedness" is required in order to conclude global stability. Global asymptotic stability (GAS) follows similarly.

It is easier to visualize this method of analysis by thinking of a physical system (e.g. vibrating spring and mass) and considering the energy of such a system. If the system loses energy over time and the energy is never restored then eventually the system must grind to a stop and reach some final resting state. This final state is called the attractor. However, finding a function that gives the precise energy of a physical system can be difficult, and for abstract mathematical systems, economic systems or biological systems, the concept of energy may not be applicable.

Lyapunov's realization was that stability can be proven without requiring knowledge of the true physical energy, provided a Lyapunov function can be found to satisfy the above constraints.

## Definition for discrete-time systems

The definition for discrete-time systems is almost identical to that for continuous-time systems. The definition below provides this, using an alternate language commonly used in more mathematical texts.

Let (*X*, *d*) be a metric space and *f* : *X* → *X* a continuous function. A point *x* in *X* is said to be **Lyapunov stable**, if,

$\forall \epsilon >0\ \exists \delta >0\ \forall y\in X\ \left[d(x,y)<\delta \Rightarrow \forall n\in \mathbf {N} \ d\left(f^{n}(x),f^{n}(y)\right)<\epsilon \right].$

We say that *x* is **asymptotically stable** if it belongs to the interior of its stable set, *i.e.* if,

$\exists \delta >0\left[d(x,y)<\delta \Rightarrow \lim _{n\to \infty }d\left(f^{n}(x),f^{n}(y)\right)=0\right].$

## Stability for linear state space models

A linear state space model

${\dot {\textbf {x}}}=A{\textbf {x}}$

,

where A is a finite matrix, is asymptotically stable (in fact, exponentially stable) if all real parts of the eigenvalues of A are negative. This condition is equivalent to the following one:

$A^{\textsf {T}}M+MA$

is negative definite for some positive definite matrix $M=M^{\textsf {T}}$ . (The relevant Lyapunov function is $V(x)=x^{\textsf {T}}Mx$ .)

Correspondingly, a time-discrete linear state space model

${\textbf {x}}_{t+1}=A{\textbf {x}}_{t}$

is asymptotically stable (in fact, exponentially stable) if all the eigenvalues of A have a modulus smaller than one.

This latter condition has been generalized to switched systems: a linear switched discrete time system (ruled by a set of matrices $\{A_{1},\dots ,A_{m}\}$ )

${{\textbf {x}}_{t+1}}=A_{i_{t}}{\textbf {x}}_{t},\quad A_{i_{t}}\in \{A_{1},\dots ,A_{m}\}$

is asymptotically stable (in fact, exponentially stable) if the joint spectral radius of the set $\{A_{1},\dots ,A_{m}\}$ is smaller than one.

## Stability for systems with inputs

A system with inputs (or controls) has the form

${\dot {\textbf {x}}}={\textbf {f}}({\textbf {x}},{\textbf {u}})$

where the (generally time-dependent) input u(t) may be viewed as a *control*, *external input*, *stimulus*, *disturbance*, or *forcing function*. It has been shown that near to a point of equilibrium which is Lyapunov stable the system remains stable under small disturbances. For larger input disturbances the study of such systems is the subject of control theory and applied in control engineering. For systems with inputs, one must quantify the effect of inputs on the stability of the system. The main two approaches to this analysis are BIBO stability (for linear systems) and input-to-state stability (ISS) (for nonlinear systems)

## Example

This example shows a system where a Lyapunov function can be used to prove Lyapunov stability but cannot show asymptotic stability. Consider the following equation, based on the Van der Pol oscillator equation with the friction term changed:

${\ddot {y}}+y-\varepsilon \left({\frac {{\dot {y}}^{3}}{3}}-{\dot {y}}\right)=0.$

Let

$x_{1}=y,x_{2}={\dot {y}}$

so that the corresponding system is

${\begin{aligned}&{\dot {x}}_{1}=x_{2},\\&{\dot {x}}_{2}=-x_{1}+\varepsilon \left({\frac {x_{2}^{3}}{3}}-{x_{2}}\right).\end{aligned}}$

The origin $x_{1}=0,\ x_{2}=0$ is the only equilibrium point. Let us choose as a Lyapunov function

$V={\frac {1}{2}}\left(x_{1}^{2}+x_{2}^{2}\right)$

which is clearly positive definite. Its derivative is

${\dot {V}}=x_{1}{\dot {x}}_{1}+x_{2}{\dot {x}}_{2}=x_{1}x_{2}-x_{1}x_{2}+\varepsilon {\frac {x_{2}^{4}}{3}}-\varepsilon {x_{2}^{2}}=\varepsilon {\frac {x_{2}^{4}}{3}}-\varepsilon {x_{2}^{2}}.$

It seems that if the parameter $\varepsilon$ is positive, stability is asymptotic for $x_{2}^{2}<3.$ But this is wrong, since ${\dot {V}}$ does not depend on $x_{1}$ , and will be 0 everywhere on the $x_{1}$ axis. The equilibrium is Lyapunov stable but not asymptotically stable.

## Barbalat's lemma and stability of time-varying systems

It may be difficult to find a Lyapunov function with a negative definite derivative as required by the Lyapunov stability criterion, however a function V with ${\dot {V}}$ that is only negative semi-definite may be available. In autonomous systems, the invariant set theorem can be applied to prove asymptotic stability, but this theorem is not applicable when the dynamics are a function of time.

Instead, Barbalat's lemma allows for Lyapunov-like analysis of these non-autonomous systems. The lemma is motivated by the following observations. Assuming f is a function of time only:

- Having ${\dot {f}}(t)\to 0$ does not imply that $f(t)$ has a limit at $t\to \infty$ . For example, $f(t)=\sin(\ln(t)),\;t>0$ .
- Having $f(t)$ approaching a limit as $t\to \infty$ does not imply that ${\dot {f}}(t)\to 0$ . For example, $f(t)=\sin \left(t^{2}\right)/t,\;t>0$ .
- Having $f(t)$ lower bounded and decreasing ( ${\dot {f}}\leq 0$ ) implies it converges to a limit. But it does not say whether or not ${\dot {f}}\to 0$ as $t\to \infty$ .

Barbalat's Lemma says: If $f(t)$ has a finite limit as $t\to \infty$ and if ${\dot {f}}$ is uniformly continuous (a sufficient condition for uniform continuity is that ${\ddot {f}}$ is bounded), then ${\dot {f}}(t)\to 0$ as $t\to \infty$ .

An alternative version is as follows: Let $p\in [1,\infty )$ and $q\in (1,\infty ]$ . If $f\in L^{p}(0,\infty )$ and ${\dot {f}}\in L^{q}(0,\infty )$ , then $f(t)\to 0$ as $t\to \infty .$

In the following form the Lemma is true also in the vector valued case: Let $f(t)$ be a uniformly continuous function with values in a Banach space E and assume that $\textstyle \int _{0}^{t}f(\tau )\mathrm {d} \tau$ has a finite limit as $t\to \infty$ . Then $f(t)\to 0$ as $t\to \infty$ .

The following example is taken from page 125 of Slotine and Li's book *Applied Nonlinear Control*.

Consider a non-autonomous system

${\dot {e}}=-e+g\cdot w(t)$

${\dot {g}}=-e\cdot w(t).$

This is non-autonomous because the input w is a function of time. Assume that the input $w(t)$ is bounded.

Taking $V=e^{2}+g^{2}$ gives ${\dot {V}}=-2e^{2}\leq 0.$

This says that $V(t)\leq V(0)$ by first two conditions and hence e and g are bounded. But it does not say anything about the convergence of e to zero, as ${\dot {V}}$ is only negative semi-definite (note g can be non-zero when ${\dot {V}}$ =0) and the dynamics are non-autonomous.

Using Barbalat's lemma:

${\ddot {V}}=-4e(-e+g\cdot w)$

.

This is bounded because e , g and w are bounded. This implies ${\dot {V}}\to 0$ as $t\to \infty$ and hence $e\to 0$ . This proves that the error converges.

## Stability of time-varying systems with vanishing and bounded perturbations

Consider the auxiliary differential equation ${\dot {v}}(t)=-q(t)\beta (v(t))+e(t),$ for all $t\geq t_{0}$ , with state $v\in \mathbb {R}$ and initial condition $v(t_{0})\geq 0$ . The function $\beta \in C^{0}(\mathbb {R} ,\mathbb {R} )$ is strictly increasing and satisfies $\beta (0)=0$ . The functions e and q belong to $C^{0}(\mathbb {R} ,\mathbb {R} _{+})$ . The importance of the prior differential equation is that a wide class of Lyapunov inequalities can be linked to it by a comparison principle.

Assume that for all $t\geq t_{0}$ , $q(t)>0$ and with $\int _{t_{0}}^{\infty }q(t)\,dt=\infty$ and $\lim _{t\to \infty }{\frac {e(t)}{q(t)}}=L\in \mathbb {R} _{+}\cup \{\infty \}.$ The prior property indicates a bounded perturbation when $L>0$ is finite and a vanishing perturbation when $L=0$ .

For each initial condition $v(t_{0})\geq 0$ and each solution $v(t)$ with maximal interval of existence $[t_{0},\omega )$ , where $t_{0}<\omega \leq \infty$ , the following properties hold:

1. $v(t)\geq 0$ for all $t\in [t_{0},\omega )$ .
2. If $L\in [0,\infty )$ and $L\in \mathrm {Range} \{\beta \}$ , then $\omega =\infty$ , $\|v\|_{\infty }<\infty$ and $\lim _{t\to \infty }v(t)=\beta ^{-1}(L)$ .
3. If $L=\infty$ , v is not uniformly zero, and $\lim _{s\to \infty }\beta (s)=\infty$ , then $\omega =\infty$ and $\lim _{t\to \infty }v(t)=\infty$ .

The prior results have been also derived in the literature within different contexts; see, e.g., .

## Lyapunov stability of time-varying systems with unbounded perturbations

Consider the system: : ${\dot {\zeta }}(t)=g{\big (}t,\zeta (t){\big )};t\geq t_{0},$ $\zeta (t_{0})=\zeta _{0},$ where $(t_{0},\zeta _{0})\in \mathbb {R} \times \mathbb {R} ^{m}$ , solution $\zeta (t)$ in $\mathbb {R} ^{m}$ ( m is a strictly positive integer), and a well-defined function $g:[t_{0},\infty )\times \mathbb {R} ^{m}\rightarrow \mathbb {R} ^{m}$ with $g(t,0)=0$ , $\forall t\geq t_{0}$ .

Assume that the system satisfies Carathéodory conditions; that is the mapping $t\mapsto g(t,\zeta )$ is locally essentially bounded on $[t_{0},\infty )\times \mathbb {R} ^{m}$ , is measurable for every $\zeta \in \mathbb {R} ^{m}$ and is continuous for almost every $t\geq t_{0}$ . The system admits a locally absolutely continuous local Carathéodory solution that is defined on a maximal interval $[t_{0},\omega )$ .

Assume that there exist constants $\alpha >0$ , $\beta >0$ with $\alpha <\beta$ , locally absolutely continuous functions $r_{1}\in C^{0}(\mathbb {R} ,\mathbb {R} )$ , $r_{2}\in C^{0}(\mathbb {R} ,\mathbb {R} )$ and a Lebesgue measurable function $h:\mathbb {R} \rightarrow \mathbb {R}$ satisfying the following:

(i) $(-1)^{\alpha }=-1$ and $(-1)^{\beta }$ is well-defined (we do not need $(-1)^{\beta }$ to be well-defined if the positivity of solutions is guaranteed).

(ii) $r_{1}(t)>0$ , $r_{2}(t)>0$ , $\forall t>t_{0}$ and $h(t)>0$ for almost all $t>t_{0}$ .

(iii) $\lim _{t\rightarrow \infty }{\frac {r_{2}(t)}{r_{1}(t)}}=\infty$ (from which it follows that the perturbation is unbounded, as illustrated by the Lyapunov inequality given later).

(iv) $\lim _{t\rightarrow \infty }\Lambda (t)=0$ , where $\Lambda (t):={\frac {r_{1}(t){\dot {r}}_{2}(t)-{\dot {r}}_{1}(t)r_{2}(t)}{h(t)(r_{1}(t))^{\frac {2\beta -\alpha -1}{\beta -\alpha }}(r_{2}(t))^{\frac {\beta -2\alpha +1}{\beta -\alpha }}}},{\mbox{ for almost all }}t>t_{0}.$

(v) for each solution $\zeta (t)$ of the system with maximal interval of existence $[t_{0},\omega )$ , there exist positive constants $\delta$ , $\sigma$ , $c_{1}$ , $c_{2}$ , and a Lyapunov function $V\in C^{1}(\mathbb {R} \times \mathbb {R} ^{m},\mathbb {R} _{+})$ , satisfying (for almost every $t\in (t_{0},\omega )$ that satisfies $V(t,\zeta (t))<\delta$ ):

$c_{1}|\kappa |^{\sigma }\leq V(t,\kappa )\leq c_{2}|\kappa |^{\sigma },\forall t\in \mathbb {R} ,\forall \kappa \in \mathbb {R} ^{m},$

$\nabla V(t,\zeta (t))\cdot g(t,\zeta (t))\leq {\big (}-r_{1}(t)V^{\alpha }(t,\zeta (t))+r_{2}(t)V^{\beta }(t,\zeta (t)){\big )}h(t).$

Then, there exists $c_{3}>0$ such that for each $|\zeta _{0}|<c_{3}$ , one get $\omega =\infty$ and $|\zeta (t)|\leq {\sqrt[{\sigma }]{\frac {c_{2}}{c_{1}}}}|\zeta _{0}|,\forall t\geq t_{0},$ so that $\zeta =0$ is uniformly stable. Furthermore, the origin is asymptotically stable.

## Example

The time-varying population growth model with Allee effect can be represented by

${\dot {N}}(t)=R(t)N(t)\left({\frac {N(t)}{A(t)}}-1\right)\left(1-{\frac {N(t)}{K(t)}}\right),$

where $t\geq t_{0}$ , state $N(t)\in \mathbb {R}$ , a Lebesgue measurable function $R:\mathbb {R} \rightarrow \mathbb {R}$ with $R(t)>0$ for almost all $t>t_{0}$ , and locally absolutely continuous functions $A\in C^{0}(\mathbb {R} ,\mathbb {R} )$ and $K\in C^{0}(\mathbb {R} ,\mathbb {R} )$ so that $A(t)>0$ and $K(t)>0$ for all $t>t_{0}$ .

The right-hand side of the equation is locally Lipschitz in N and thus a unique solution exists with a maximal interval of existence $[t_{0},\omega )$ . The origin $N=0$ is an equilibrium point. We aim to derive conditions that make $N=0$ a uniformly stable and an asymptotically stable extinction equilibrium. To this end, assume that

$\int _{t_{0}}^{\infty }R(t)dt=\infty ,$

$\lim _{t\rightarrow \infty }\left({\frac {1}{A(t)}}+{\frac {1}{K(t)}}\right)=\infty ,$

and

$\lim _{t\rightarrow \infty }\left({\frac {{\dot {A}}(t)(K(t))^{2}+{\dot {K}}(t)(A(t))^{2}}{R(t)A(t)K(t)(A(t)+K(t))}}\right)=0.$

Let $V=N^{2}$ . The inequality is satisfied with $c_{1}=1$ , $c_{2}=1$ and $\sigma =2$ . Simple computations yield

${\dot {V}}(t)\leq 2R(t)\left(-V(t)+\left({\frac {1}{A(t)}}+{\frac {1}{K(t)}}\right)V^{\frac {3}{2}}(t)\right){\mbox{ for almost all }}t>t_{0},$

which has the form of the inequality with $\alpha =1$ , $\beta ={\frac {3}{2}}$ , $h(t)=2R(t)$ , $r_{1}(t)=1$ , $r_{2}(t)={\frac {1}{A(t)}}+{\frac {1}{K(t)}}$ and $\delta$ is arbitrary in $(t_{0},\infty )$ . Moreover, one can easily show the function $\Lambda (t)$ goes to zero as t goes to infinity. Thus, all conditions are satisfied and thus there exists $c_{3}>0$ such that for each $|N_{0}|<c_{3}$ , one get $\omega =\infty$ and

$|N(t)|\leq {\sqrt[{\sigma }]{\frac {c_{2}}{c_{1}}}}|N_{0}|,\forall t\geq t_{0},$

and hence $N=0$ is uniformly stable. In fact, $N=0$ is uniformly stable and is asymptotically stable.
