---
title: "Noether's theorem (part 2/2)"
source: https://en.wikipedia.org/wiki/Noether's_theorem
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
part: 2/2
---

## Derivations

### One independent variable

Consider the simplest case, a system with one independent variable, time. Suppose the dependent variables **q** are such that the action integral

$I=\int _{t_{1}}^{t_{2}}L[\mathbf {q} [t],{\dot {\mathbf {q} }}[t],t]\,dt$

is invariant under brief infinitesimal variations in the dependent variables. In other words, they satisfy the Euler–Lagrange equations

${\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}[t]={\frac {\partial L}{\partial \mathbf {q} }}[t].$

And suppose that the integral is invariant under a continuous symmetry. Mathematically such a symmetry is represented as a flow, **φ**, which acts on the variables as follows

${\begin{aligned}t&\rightarrow t'=t+\varepsilon T\\\mathbf {q} [t]&\rightarrow \mathbf {q} '[t']=\varphi [\mathbf {q} [t],\varepsilon ]=\varphi [\mathbf {q} [t'-\varepsilon T],\varepsilon ]\end{aligned}}$

where *ε* is a real variable indicating the amount of flow, and *T* is a real constant (which could be zero) indicating how much the flow shifts time.

${\dot {\mathbf {q} }}[t]\rightarrow {\dot {\mathbf {q} }}'[t']={\frac {d}{dt}}\varphi [\mathbf {q} [t],\varepsilon ]={\frac {\partial \varphi }{\partial \mathbf {q} }}[\mathbf {q} [t'-\varepsilon T],\varepsilon ]{\dot {\mathbf {q} }}[t'-\varepsilon T].$

The action integral flows to

${\begin{aligned}I'[\varepsilon ]&=\int _{t_{1}+\varepsilon T}^{t_{2}+\varepsilon T}L[\mathbf {q} '[t'],{\dot {\mathbf {q} }}'[t'],t']\,dt'\\[6pt]&=\int _{t_{1}+\varepsilon T}^{t_{2}+\varepsilon T}L[\varphi [\mathbf {q} [t'-\varepsilon T],\varepsilon ],{\frac {\partial \varphi }{\partial \mathbf {q} }}[\mathbf {q} [t'-\varepsilon T],\varepsilon ]{\dot {\mathbf {q} }}[t'-\varepsilon T],t']\,dt'\end{aligned}}$

which may be regarded as a function of *ε*. Calculating the derivative at *ε* = 0 and using Leibniz's rule, we get

${\begin{aligned}0={\frac {dI'}{d\varepsilon }}[0]={}&L[\mathbf {q} [t_{2}],{\dot {\mathbf {q} }}[t_{2}],t_{2}]T-L[\mathbf {q} [t_{1}],{\dot {\mathbf {q} }}[t_{1}],t_{1}]T\\[6pt]&{}+\int _{t_{1}}^{t_{2}}{\frac {\partial L}{\partial \mathbf {q} }}\left(-{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}T+{\frac {\partial \varphi }{\partial \varepsilon }}\right)+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\left(-{\frac {\partial ^{2}\varphi }{(\partial \mathbf {q} )^{2}}}{\dot {\mathbf {q} }}^{2}T+{\frac {\partial ^{2}\varphi }{\partial \varepsilon \partial \mathbf {q} }}{\dot {\mathbf {q} }}-{\frac {\partial \varphi }{\partial \mathbf {q} }}{\ddot {\mathbf {q} }}T\right)\,dt.\end{aligned}}$

Notice that the Euler–Lagrange equations imply

${\begin{aligned}{\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}T\right)&=\left({\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right){\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\left({\frac {d}{dt}}{\frac {\partial \varphi }{\partial \mathbf {q} }}\right){\dot {\mathbf {q} }}T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\ddot {\mathbf {q} }}\,T\\[6pt]&={\frac {\partial L}{\partial \mathbf {q} }}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\left({\frac {\partial ^{2}\varphi }{(\partial \mathbf {q} )^{2}}}{\dot {\mathbf {q} }}\right){\dot {\mathbf {q} }}T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\ddot {\mathbf {q} }}\,T.\end{aligned}}$

Substituting this into the previous equation, one gets

${\begin{aligned}0={\frac {dI'}{d\varepsilon }}[0]={}&L[\mathbf {q} [t_{2}],{\dot {\mathbf {q} }}[t_{2}],t_{2}]T-L[\mathbf {q} [t_{1}],{\dot {\mathbf {q} }}[t_{1}],t_{1}]T-{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}[t_{2}]T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}[t_{1}]T\\[6pt]&{}+\int _{t_{1}}^{t_{2}}{\frac {\partial L}{\partial \mathbf {q} }}{\frac {\partial \varphi }{\partial \varepsilon }}+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial ^{2}\varphi }{\partial \varepsilon \partial \mathbf {q} }}{\dot {\mathbf {q} }}\,dt.\end{aligned}}$

Again using the Euler–Lagrange equations we get

${\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \varepsilon }}\right)=\left({\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right){\frac {\partial \varphi }{\partial \varepsilon }}+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial ^{2}\varphi }{\partial \varepsilon \partial \mathbf {q} }}{\dot {\mathbf {q} }}={\frac {\partial L}{\partial \mathbf {q} }}{\frac {\partial \varphi }{\partial \varepsilon }}+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial ^{2}\varphi }{\partial \varepsilon \partial \mathbf {q} }}{\dot {\mathbf {q} }}.$

Substituting this into the previous equation, one gets

${\begin{aligned}0={}&L[\mathbf {q} [t_{2}],{\dot {\mathbf {q} }}[t_{2}],t_{2}]T-L[\mathbf {q} [t_{1}],{\dot {\mathbf {q} }}[t_{1}],t_{1}]T-{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}[t_{2}]T+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}[t_{1}]T\\[6pt]&{}+{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \varepsilon }}[t_{2}]-{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \varepsilon }}[t_{1}].\end{aligned}}$

From which one can see that

$\left({\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \mathbf {q} }}{\dot {\mathbf {q} }}-L\right)T-{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \varepsilon }}$

is a constant of the motion, i.e., it is a conserved quantity. Since φ[**q**, 0] = **q**, we get ${\frac {\partial \varphi }{\partial \mathbf {q} }}=1$ and so the conserved quantity simplifies to

$\left({\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\dot {\mathbf {q} }}-L\right)T-{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}{\frac {\partial \varphi }{\partial \varepsilon }}.$

To avoid excessive complication of the formulas, this derivation assumed that the flow does not change as time passes. The same result can be obtained in the more general case.

### Geometric derivation

Noether's theorem can be seen as a consequence of the fundamental theorem of calculus (known by various names in physics such as the Generalized Stokes theorem or the Gradient theorem): for a function ${\textstyle S}$ analytical in a domain ${\textstyle {\cal {D}}}$ , $\int _{\cal {\cal {P}}}dS=0$

where ${\textstyle {\cal {P}}}$ is a closed path in ${\textstyle {\cal {D}}}$ . Here, the *function* ${\textstyle S(\mathbf {q} ,t)}$ is the action *function* that is computed by the integration of the Lagrangian over optimal trajectories or equivalently obtained through the Hamilton-Jacobi equation. As ${\textstyle \partial S/\partial \mathbf {q} =\mathbf {p} }$ (where ${\textstyle \mathbf {p} }$ is the momentum) and ${\textstyle \partial S/\partial t=-H}$ (where ${\textstyle H}$ is the Hamiltonian), the differential of this function is given by ${\textstyle dS=\mathbf {p} d\mathbf {q} -Hdt}$ .

Using the geometrical approach, the conserved quantity for a symmetry in Noether's sense can be derived. The symmetry is expressed as an infinitesimal transformation: ${\begin{aligned}\mathbf {q'} &=&\mathbf {q} +\epsilon \phi _{\mathbf {q} }(\mathbf {q} ,t)\\t'&=&t+\epsilon \phi _{t}(\mathbf {q} ,t)\end{aligned}}$ Let ${\textstyle {\cal {C}}}$ be an optimal trajectory and ${\textstyle {\cal {C}}'}$ its image under the above transformation ${\textstyle (\phi _{\mathbf {q} },\phi _{t})^{T}}$ (which is also an optimal trajectory). The closed path ${\textstyle {\cal {P}}}$ of integration is chosen as ${\textstyle ABB'A'}$ , where the branches ${\textstyle AB}$ and ${\textstyle A'B'}$ are given ${\textstyle {\cal {C}}}$ and ${\textstyle {\cal {C}}'}$ . By the hypothesis of Noether theorem, to the first order in ${\textstyle \epsilon }$ , $\int _{\cal {C}}dS=\int _{{\cal {C}}'}dS$ therefore, $\int _{A}^{A'}dS=\int _{B}^{B'}dS$ By definition, on the ${\textstyle AA'}$ branch we have ${\textstyle d\mathbf {q} =\epsilon \phi _{\mathbf {q} }(\mathbf {q} ,t)}$ and ${\textstyle dt=\epsilon \phi _{t}(\mathbf {q} ,t)}$ . Therefore, to the first order in ${\textstyle \epsilon }$ , the quantity $I=\mathbf {p} \phi _{\mathbf {q} }-H\phi _{t}$ is conserved along the trajectory.

### Field-theoretic derivation

Noether's theorem may also be derived for tensor fields $\varphi ^{A}$ where the index *A* ranges over the various components of the various tensor fields. These field quantities are functions defined over a four-dimensional space whose points are labeled by coordinates *x*μ where the index *μ* ranges over time (*μ* = 0) and three spatial dimensions (*μ* = 1, 2, 3). These four coordinates are the independent variables; and the values of the fields at each event are the dependent variables. Under an infinitesimal transformation, the variation in the coordinates is written

$x^{\mu }\rightarrow \xi ^{\mu }=x^{\mu }+\delta x^{\mu }$

whereas the transformation of the field variables is expressed as

$\varphi ^{A}\rightarrow \alpha ^{A}\left(\xi ^{\mu }\right)=\varphi ^{A}\left(x^{\mu }\right)+\delta \varphi ^{A}\left(x^{\mu }\right)\,.$

By this definition, the field variations $\delta \varphi ^{A}$ result from two factors: intrinsic changes in the field themselves and changes in coordinates, since the transformed field *α**A* depends on the transformed coordinates ξμ. To isolate the intrinsic changes, the field variation at a single point *x*μ may be defined

$\alpha ^{A}\left(x^{\mu }\right)=\varphi ^{A}\left(x^{\mu }\right)+{\bar {\delta }}\varphi ^{A}\left(x^{\mu }\right)\,.$

If the coordinates are changed, the boundary of the region of space–time over which the Lagrangian is being integrated also changes; the original boundary and its transformed version are denoted as Ω and Ω', respectively.

Noether's theorem begins with the assumption that a specific transformation of the coordinates and field variables does not change the action, which is defined as the integral of the Lagrangian density over the given region of spacetime. Expressed mathematically, this assumption may be written as

$\int _{\Omega ^{\prime }}L\left(\alpha ^{A},{\alpha ^{A}}_{,\nu },\xi ^{\mu }\right)d^{4}\xi -\int _{\Omega }L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)d^{4}x=0$

where the comma subscript indicates a partial derivative with respect to the coordinate(s) that follows the comma, e.g.

${\varphi ^{A}}_{,\sigma }={\frac {\partial \varphi ^{A}}{\partial x^{\sigma }}}\,.$

Since ξ is a dummy variable of integration, and since the change in the boundary Ω is infinitesimal by assumption, the two integrals may be combined using the four-dimensional version of the divergence theorem into the following form

$\int _{\Omega }\left\{\left[L\left(\alpha ^{A},{\alpha ^{A}}_{,\nu },x^{\mu }\right)-L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\right]+{\frac {\partial }{\partial x^{\sigma }}}\left[L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\delta x^{\sigma }\right]\right\}d^{4}x=0\,.$

The difference in Lagrangians can be written to first-order in the infinitesimal variations as

$\left[L\left(\alpha ^{A},{\alpha ^{A}}_{,\nu },x^{\mu }\right)-L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\right]={\frac {\partial L}{\partial \varphi ^{A}}}{\bar {\delta }}\varphi ^{A}+{\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\bar {\delta }}{\varphi ^{A}}_{,\sigma }\,.$

However, because the variations are defined at the same point as described above, the variation and the derivative can be done in reverse order; they commute

${\bar {\delta }}{\varphi ^{A}}_{,\sigma }={\bar {\delta }}{\frac {\partial \varphi ^{A}}{\partial x^{\sigma }}}={\frac {\partial }{\partial x^{\sigma }}}\left({\bar {\delta }}\varphi ^{A}\right)\,.$

Using the Euler–Lagrange field equations

${\frac {\partial }{\partial x^{\sigma }}}\left({\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}\right)={\frac {\partial L}{\partial \varphi ^{A}}}$

the difference in Lagrangians can be written neatly as

${\begin{aligned}&\left[L\left(\alpha ^{A},{\alpha ^{A}}_{,\nu },x^{\mu }\right)-L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\right]\\[4pt]={}&{\frac {\partial }{\partial x^{\sigma }}}\left({\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}\right){\bar {\delta }}\varphi ^{A}+{\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\bar {\delta }}{\varphi ^{A}}_{,\sigma }={\frac {\partial }{\partial x^{\sigma }}}\left({\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\bar {\delta }}\varphi ^{A}\right).\end{aligned}}$

Thus, the change in the action can be written as

$\int _{\Omega }{\frac {\partial }{\partial x^{\sigma }}}\left\{{\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\bar {\delta }}\varphi ^{A}+L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\delta x^{\sigma }\right\}d^{4}x=0\,.$

Since this holds for any region Ω, the integrand must be zero

${\frac {\partial }{\partial x^{\sigma }}}\left\{{\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\bar {\delta }}\varphi ^{A}+L\left(\varphi ^{A},{\varphi ^{A}}_{,\nu },x^{\mu }\right)\delta x^{\sigma }\right\}=0\,.$

For any combination of the various symmetry transformations, the perturbation can be written

${\begin{aligned}\delta x^{\mu }&=\varepsilon X^{\mu }\\\delta \varphi ^{A}&=\varepsilon \Psi ^{A}={\bar {\delta }}\varphi ^{A}+\varepsilon {\mathcal {L}}_{X}\varphi ^{A}\end{aligned}}$

where ${\mathcal {L}}_{X}\varphi ^{A}$ is the Lie derivative of $\varphi ^{A}$ in the *X**μ* direction. When $\varphi ^{A}$ is a scalar or ${X^{\mu }}_{,\nu }=0$ ,

${\mathcal {L}}_{X}\varphi ^{A}={\frac {\partial \varphi ^{A}}{\partial x^{\mu }}}X^{\mu }\,.$

These equations imply that the field variation taken at one point equals

${\bar {\delta }}\varphi ^{A}=\varepsilon \Psi ^{A}-\varepsilon {\mathcal {L}}_{X}\varphi ^{A}\,.$

Differentiating the above divergence with respect to *ε* at *ε* = 0 and changing the sign yields the conservation law

${\frac {\partial }{\partial x^{\sigma }}}j^{\sigma }=0$

where the conserved current equals

$j^{\sigma }=\left[{\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}{\mathcal {L}}_{X}\varphi ^{A}-L\,X^{\sigma }\right]-\left({\frac {\partial L}{\partial {\varphi ^{A}}_{,\sigma }}}\right)\Psi ^{A}\,.$

### Manifold/fiber bundle derivation

Suppose we have an *n*-dimensional oriented Riemannian or more generally Lorentzian manifold, *M* and a target manifold *T*. Let ${\mathcal {C}}$ be the configuration space of smooth functions from *M* to *T*. (More generally, we can have smooth sections of a fiber bundle *T* over *M*.)

Examples of this *M* in physics include:

- In classical mechanics, in the Hamiltonian formulation, *M* is the one-dimensional manifold $\mathbb {R}$ , representing time and the target space is the cotangent bundle of space of generalized positions.
- In field theory, *M* is the spacetime manifold and the target space is the set of values the fields can take at any given point. For example, if there are *m* real-valued scalar fields, $\varphi _{1},\ldots ,\varphi _{m}$ , then the target manifold is $\mathbb {R} ^{m}$ . If the field is a real vector field, then the target manifold is isomorphic to $\mathbb {R} ^{3}$ .

Now suppose there is a functional

${\mathcal {S}}\colon {\mathcal {C}}\rightarrow \mathbb {R} ,$

called the action. (It takes values in $\mathbb {R}$ , rather than $\mathbb {C}$ ; this is for physical reasons, and is unimportant for this proof.)

To get to the usual version of Noether's theorem, we need additional restrictions on the action. We assume ${\mathcal {S}}[\varphi ]$ is the integral over *M* of a function

${\mathcal {L}}(\varphi ,\partial _{\mu }\varphi ,x)$

called the Lagrangian density, depending on $\varphi$ , its derivative and the position. In other words, for $\varphi$ in ${\mathcal {C}}$

${\mathcal {S}}[\varphi ]\,=\,\int _{M}{\mathcal {L}}[\varphi (x),\partial _{\mu }\varphi (x),x]\,d^{n}x.$

Suppose we are given boundary conditions, i.e., a specification of the value of $\varphi$ at the boundary if *M* is compact, or some limit on $\varphi$ as *x* approaches ∞. Then the subspace of ${\mathcal {C}}$ consisting of functions $\varphi$ such that all functional derivatives of ${\mathcal {S}}$ at $\varphi$ are zero, that is:

${\frac {\delta {\mathcal {S}}[\varphi ]}{\delta \varphi (x)}}=0$

and that $\varphi$ satisfies the given boundary conditions, is the subspace of on shell solutions. (See principle of stationary action)

Now, suppose we have an infinitesimal transformation on ${\mathcal {C}}$ , generated by a functional derivation *Q*, such that

$Q\left[\int _{N}{\mathcal {L}}\,\mathrm {d} ^{n}x\right]=\int _{\partial N}f^{\mu }[\varphi (x),\partial \varphi ,\partial \partial \varphi ,\ldots ]\,ds_{\mu }$

for all compact submanifolds *N* of dimension n or in other words,

$Q[{\mathcal {L}}(x)]=\partial _{\mu }f^{\mu }(x)$

for all *x*, where we set

${\mathcal {L}}(x)={\mathcal {L}}[\varphi (x),\partial _{\mu }\varphi (x),x]\;.$

If this holds on shell and off shell, we say *Q* generates an off-shell symmetry. If this only holds on shell, we say *Q* generates an on-shell symmetry. If the symmetry generated by *Q* integrates to a continuous symmetry, we say that *Q* is the generator of a one parameter symmetry Lie group.

Now, for any *N*, because of the Euler–Lagrange theorem, we have on shell (and only on-shell)

${\begin{aligned}Q\left[\int _{N}{\mathcal {L}}\,\mathrm {d} ^{n}x\right]&=\int _{N}\left[{\frac {\partial {\mathcal {L}}}{\partial \varphi }}-\partial _{\mu }{\frac {\partial {\mathcal {L}}}{\partial (\partial _{\mu }\varphi )}}\right]Q[\varphi ]\,\mathrm {d} ^{n}x+\int _{\partial N}{\frac {\partial {\mathcal {L}}}{\partial (\partial _{\mu }\varphi )}}Q[\varphi ]\,\mathrm {d} s_{\mu }\\&=\int _{\partial N}f^{\mu }\,\mathrm {d} s_{\mu }.\end{aligned}}$

Since this is true for any *N*, we have

$\partial _{\mu }\left[{\frac {\partial {\mathcal {L}}}{\partial (\partial _{\mu }\varphi )}}Q[\varphi ]-f^{\mu }\right]=0\;.$

But this is the continuity equation for the current $J^{\mu }$ defined by:

$J^{\mu }\,:=\,{\frac {\partial {\mathcal {L}}}{\partial (\partial _{\mu }\varphi )}}Q[\varphi ]-f^{\mu },$

which is called the **Noether current** associated with the symmetry. The continuity equation tells us that if we integrate this current over a space-like slice, we get a conserved quantity called the Noether charge (provided, of course, if *M* is noncompact, the currents fall off sufficiently fast at infinity).

Noether's theorem is an on shell theorem: it relies on the use of the equations of motion—the classical path. It reflects the relation between the boundary conditions and the variational principle. Assuming no boundary terms in the action, Noether's theorem implies that

$\int _{\partial N}J^{\mu }ds_{\mu }=0\;.$

The quantum analogs of Noether's theorem involving expectation values (e.g., ${\textstyle \left\langle \int \partial \cdot {\textbf {J}}~d^{4}x\right\rangle =0}$ ) probing off shell quantities as well are the Ward–Takahashi identities.

### Generalization to Lie algebras

Suppose we have two symmetry derivations *Q*1 and *Q*2. Then, [*Q*1, *Q*2] is also a symmetry derivation. Let us see this explicitly. Let us say $Q_{1}[{\mathcal {L}}]=\partial _{\mu }f_{1}^{\mu }$ and $Q_{2}[{\mathcal {L}}]=\partial _{\mu }f_{2}^{\mu }$

Then, $[Q_{1},Q_{2}][{\mathcal {L}}]=Q_{1}[Q_{2}[{\mathcal {L}}]]-Q_{2}[Q_{1}[{\mathcal {L}}]]=\partial _{\mu }f_{12}^{\mu }$ where $f_{12}^{\mu }=Q_{1}[f_{2}^{\mu }]-Q_{2}[f_{1}^{\mu }]$ . So, $j_{12}^{\mu }=\left({\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}\right)(Q_{1}[Q_{2}[\varphi ]]-Q_{2}[Q_{1}[\varphi ]])-f_{12}^{\mu }.$

This shows we can extend Noether's theorem to larger Lie algebras in a natural way.

### Generalization of the proof

This applies to *any* local symmetry derivation *Q* satisfying *QS* ≈ 0, and also to more general local functional differentiable actions, including ones where the Lagrangian depends on higher derivatives of the fields. Let *ε* be any arbitrary smooth function of the spacetime (or time) manifold such that the closure of its support is disjoint from the boundary. *ε* is a test function. Then, because of the variational principle (which does *not* apply to the boundary, by the way), the derivation distribution q generated by *q*[*ε*][Φ(*x*)] = *ε*(*x*)*Q*[Φ(*x*)] satisfies *q*[*ε*][*S*] ≈ 0 for every *ε*, or more compactly, *q*(*x*)[*S*] ≈ 0 for all *x* not on the boundary (but remember that *q*(*x*) is a shorthand for a derivation *distribution*, not a derivation parametrized by *x* in general). This is the generalization of Noether's theorem.

To see how the generalization is related to the version given above, assume that the action is the spacetime integral of a Lagrangian that only depends on $\varphi$ and its first derivatives. Also, assume

$Q[{\mathcal {L}}]\approx \partial _{\mu }f^{\mu }$

Then,

${\begin{aligned}q[\varepsilon ][{\mathcal {S}}]&=\int q[\varepsilon ][{\mathcal {L}}]d^{n}x\\[6pt]&=\int \left\{\left({\frac {\partial }{\partial \varphi }}{\mathcal {L}}\right)\varepsilon Q[\varphi ]+\left[{\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}\right]\partial _{\mu }(\varepsilon Q[\varphi ])\right\}d^{n}x\\[6pt]&=\int \left\{\varepsilon Q[{\mathcal {L}}]+\partial _{\mu }\varepsilon \left[{\frac {\partial }{\partial \left(\partial _{\mu }\varphi \right)}}{\mathcal {L}}\right]Q[\varphi ]\right\}\,d^{n}x\\[6pt]&\approx \int \varepsilon \partial _{\mu }\left\{f^{\mu }-\left[{\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}\right]Q[\varphi ]\right\}\,d^{n}x\end{aligned}}$

for all $\varepsilon$ .

More generally, if the Lagrangian depends on higher derivatives, then

$\partial _{\mu }\left[f^{\mu }-\left[{\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}\right]Q[\varphi ]-2\left[{\frac {\partial }{\partial (\partial _{\mu }\partial _{\nu }\varphi )}}{\mathcal {L}}\right]\partial _{\nu }Q[\varphi ]+\partial _{\nu }\left[\left[{\frac {\partial }{\partial (\partial _{\mu }\partial _{\nu }\varphi )}}{\mathcal {L}}\right]Q[\varphi ]\right]-\,\dotsm \right]\approx 0.$


## Examples

### Example 1: Conservation of energy

Looking at the specific case of a Newtonian particle of mass *m*, coordinate *x*, moving under the influence of a potential *V*, coordinatized by time *t*. The action, *S*, is:

${\begin{aligned}{\mathcal {S}}[x]&=\int L\left[x(t),{\dot {x}}(t)\right]\,dt\\&=\int \left({\frac {m}{2}}\sum _{i=1}^{3}{\dot {x}}_{i}^{2}-V(x(t))\right)\,dt.\end{aligned}}$

The first term in the brackets is the kinetic energy of the particle, while the second is its potential energy. Consider the generator of time translations $Q={\frac {d}{dt}}$ . In other words, $Q[x(t)]={\dot {x}}(t)$ . The coordinate *x* has an explicit dependence on time, whilst *V* does not; consequently:

$Q[L]={\frac {d}{dt}}\left[{\frac {m}{2}}\sum _{i}{\dot {x}}_{i}^{2}-V(x)\right]=m\sum _{i}{\dot {x}}_{i}{\ddot {x}}_{i}-\sum _{i}{\frac {\partial V(x)}{\partial x_{i}}}{\dot {x}}_{i}$

so we can set

$L={\frac {m}{2}}\sum _{i}{\dot {x}}_{i}^{2}-V(x).$

Then,

${\begin{aligned}j&=\sum _{i=1}^{3}{\frac {\partial L}{\partial {\dot {x}}_{i}}}Q[x_{i}]-L\\&=m\sum _{i}{\dot {x}}_{i}^{2}-\left[{\frac {m}{2}}\sum _{i}{\dot {x}}_{i}^{2}-V(x)\right]\\[3pt]&={\frac {m}{2}}\sum _{i}{\dot {x}}_{i}^{2}+V(x).\end{aligned}}$

The right hand side is the energy, and Noether's theorem states that $dj/dt=0$ (i.e. the principle of conservation of energy is a consequence of invariance under time translations).

More generally, if the Lagrangian does not depend explicitly on time, the quantity

$\sum _{i=1}^{3}{\frac {\partial L}{\partial {\dot {x}}_{i}}}{\dot {x_{i}}}-L$

(called the Hamiltonian) is conserved.

### Example 2: Conservation of center of momentum

Still considering 1-dimensional time, let

${\begin{aligned}{\mathcal {S}}\left[{\vec {x}}\right]&=\int {\mathcal {L}}\left[{\vec {x}}(t),{\dot {\vec {x}}}(t)\right]dt\\[3pt]&=\int \left[\sum _{\alpha =1}^{N}{\frac {m_{\alpha }}{2}}\left({\dot {\vec {x}}}_{\alpha }\right)^{2}-\sum _{\alpha <\beta }V_{\alpha \beta }\left({\vec {x}}_{\beta }-{\vec {x}}_{\alpha }\right)\right]dt,\end{aligned}}$

for N Newtonian particles where the potential only depends pairwise upon the relative displacement.

For ${\vec {Q}}$ , consider the generator of Galilean transformations (i.e. a change in the frame of reference). In other words,

$Q_{i}\left[x_{\alpha }^{j}(t)\right]=t\delta _{i}^{j}.$

And

${\begin{aligned}Q_{i}[{\mathcal {L}}]&=\sum _{\alpha }m_{\alpha }{\dot {x}}_{\alpha }^{i}-\sum _{\alpha <\beta }t\partial _{i}V_{\alpha \beta }\left({\vec {x}}_{\beta }-{\vec {x}}_{\alpha }\right)\\&=\sum _{\alpha }m_{\alpha }{\dot {x}}_{\alpha }^{i}.\end{aligned}}$

This has the form of ${\textstyle {\frac {d}{dt}}\sum _{\alpha }m_{\alpha }x_{\alpha }^{i}}$ so we can set

${\vec {f}}=\sum _{\alpha }m_{\alpha }{\vec {x}}_{\alpha }.$

Then,

${\begin{aligned}{\vec {j}}&=\sum _{\alpha }\left({\frac {\partial }{\partial {\dot {\vec {x}}}_{\alpha }}}{\mathcal {L}}\right)\cdot {\vec {Q}}\left[{\vec {x}}_{\alpha }\right]-{\vec {f}}\\[6pt]&=\sum _{\alpha }\left(m_{\alpha }{\dot {\vec {x}}}_{\alpha }t-m_{\alpha }{\vec {x}}_{\alpha }\right)\\[3pt]&={\vec {P}}t-M{\vec {x}}_{CM}\end{aligned}}$

where ${\vec {P}}$ is the total momentum, *M* is the total mass and ${\vec {x}}_{CM}$ is the center of mass. Noether's theorem states:

${\frac {d{\vec {j}}}{dt}}=0\Rightarrow {\vec {P}}-M{\dot {\vec {x}}}_{CM}=0.$

### Example 3: Conformal transformation

Both examples 1 and 2 are over a 1-dimensional manifold (time). An example involving spacetime is a conformal transformation of a massless real scalar field with a quartic potential in (3 + 1)-Minkowski spacetime.

${\begin{aligned}{\mathcal {S}}[\varphi ]&=\int {\mathcal {L}}\left[\varphi (x),\partial _{\mu }\varphi (x)\right]d^{4}x\\[3pt]&=\int \left({\frac {1}{2}}\partial ^{\mu }\varphi \partial _{\mu }\varphi -\lambda \varphi ^{4}\right)d^{4}x\end{aligned}}$

For *Q*, consider the generator of a spacetime rescaling. In other words,

$Q[\varphi (x)]=x^{\mu }\partial _{\mu }\varphi (x)+\varphi (x).$

The second term on the right hand side is due to the "conformal weight" of $\varphi$ . And

$Q[{\mathcal {L}}]=\partial ^{\mu }\varphi \left(\partial _{\mu }\varphi +x^{\nu }\partial _{\mu }\partial _{\nu }\varphi +\partial _{\mu }\varphi \right)-4\lambda \varphi ^{3}\left(x^{\mu }\partial _{\mu }\varphi +\varphi \right).$

This has the form of

$\partial _{\mu }\left[{\frac {1}{2}}x^{\mu }\partial ^{\nu }\varphi \partial _{\nu }\varphi -\lambda x^{\mu }\varphi ^{4}\right]=\partial _{\mu }\left(x^{\mu }{\mathcal {L}}\right)$

(where we have performed a change of dummy indices) so set

$f^{\mu }=x^{\mu }{\mathcal {L}}.$

Then

${\begin{aligned}j^{\mu }&=\left[{\frac {\partial }{\partial (\partial _{\mu }\varphi )}}{\mathcal {L}}\right]Q[\varphi ]-f^{\mu }\\&=\partial ^{\mu }\varphi \left(x^{\nu }\partial _{\nu }\varphi +\varphi \right)-x^{\mu }\left({\frac {1}{2}}\partial ^{\nu }\varphi \partial _{\nu }\varphi -\lambda \varphi ^{4}\right).\end{aligned}}$

Noether's theorem states that $\partial _{\mu }j^{\mu }=0$ (as one may explicitly check by substituting the Euler–Lagrange equations into the left hand side).

If one tries to find the Ward–Takahashi analog of this equation, one runs into a problem because of anomalies.


## Applications

Application of Noether's theorem allows physicists to gain insights into any general theory in physics, by just analyzing the various transformations that would make the form of the laws involved invariant. For example:

- Invariance of an isolated system with respect to spatial translation (in other words, that the laws of physics are the same at all locations in space) gives the law of conservation of linear momentum (which states that the total linear momentum of an isolated system is constant)
- Invariance of an isolated system with respect to time translation (i.e. that the laws of physics are the same at all points in time) gives the law of conservation of energy (which states that the total energy of an isolated system is constant)
- Invariance of an isolated system with respect to rotation (i.e., that the laws of physics are the same with respect to all angular orientations in space) gives the law of conservation of angular momentum (which states that the total angular momentum of an isolated system is constant)
- Invariance of an isolated system with respect to Lorentz boosts (i.e., that the laws of physics are the same with respect to all inertial reference frames) gives the center-of-mass theorem (which states that the center-of-mass of an isolated system moves at a constant velocity).

In quantum field theory, the analog to Noether's theorem, the Ward–Takahashi identity, yields further conservation laws, such as the conservation of electric charge from the invariance with respect to a change in the phase factor of the complex field of the charged particle and the associated gauge of the electric potential and vector potential.

The Noether charge is also used in calculating the entropy of stationary black holes.
