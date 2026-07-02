---
title: "Canonical transformation (part 1/2)"
source: https://en.wikipedia.org/wiki/Canonical_transformation
domain: hamiltonian-mechanics
license: CC-BY-SA-4.0
tags: hamiltonian mechanics, phase space, canonical transformation, poisson bracket
fetched: 2026-07-02
part: 1/2
---

# Canonical transformation

In Hamiltonian mechanics, a **canonical transformation** is a change of canonical coordinates (**q**, **p**) → (**Q**, **P**) that preserves the form of Hamilton's equations. This is sometimes known as *form invariance*. Although Hamilton's equations are preserved, it need not preserve the explicit form of the Hamiltonian itself. Canonical transformations are useful in their own right, and also form the basis for the Hamilton–Jacobi equations (a useful method for calculating conserved quantities) and Liouville's theorem (itself the basis for classical statistical mechanics).

Since Lagrangian mechanics is based on generalized coordinates, transformations of the coordinates **q** → **Q** do not affect the form of Lagrange's equations and, hence, do not affect the form of Hamilton's equations if the momentum is simultaneously changed by a Legendre transformation into $P_{i}={\frac {\partial L}{\partial {\dot {Q}}_{i}}}\ ,$ where $\left\{\ (P_{1},Q_{1}),\ (P_{2},Q_{2}),\ (P_{3},Q_{3}),\ \ldots \ \right\}$ are the new coordinates, grouped in canonical conjugate pairs of momenta $P_{i}$ and corresponding positions $Q_{i},$ for $i=1,2,\ldots \ N,$ with N being the number of degrees of freedom in both coordinate systems.

Therefore, coordinate transformations (also called *point transformations*) are a *type* of canonical transformation. However, the class of canonical transformations is much broader, since the old generalized coordinates, momenta and even time may be combined to form the new generalized coordinates and momenta. Canonical transformations that do not include the time explicitly are called *restricted canonical transformations* (many textbooks consider only this type).

Modern mathematical descriptions of canonical transformations are considered under the broader topic of symplectomorphism which covers the subject with advanced mathematical prerequisites such as cotangent bundles, exterior derivatives and symplectic manifolds.


## Notation

Boldface variables such as **q** represent a list of N generalized coordinates that need not transform like a vector under rotation and similarly **p** represents the corresponding generalized momentum, e.g., ${\begin{aligned}\mathbf {q} &\equiv \left(q_{1},q_{2},\ldots ,q_{N-1},q_{N}\right)\\\mathbf {p} &\equiv \left(p_{1},p_{2},\ldots ,p_{N-1},p_{N}\right).\end{aligned}}$

A dot over a variable or list signifies the time derivative, e.g., ${\dot {\mathbf {q} }}\equiv {\frac {d\mathbf {q} }{dt}}$ and the equalities are read to be satisfied for all coordinates, for example: ${\dot {\mathbf {p} }}=-{\frac {\partial f}{\partial \mathbf {q} }}\quad \Longleftrightarrow \quad {\dot {p_{i}}}=-{\frac {\partial f}{\partial {q_{i}}}}\quad (i=1,\dots ,N).$

The dot product notation between two lists of the same number of coordinates is a shorthand for the sum of the products of corresponding components, e.g., $\mathbf {p} \cdot \mathbf {q} \equiv \sum _{k=1}^{N}p_{k}q_{k}.$

The dot product (also known as an "inner product") maps the two coordinate lists into one variable representing a single numerical value. The coordinates after transformation are similarly labelled with **Q** for transformed generalized coordinates and **P** for transformed generalized momentum.


## Conditions for restricted canonical transformation

Restricted canonical transformations are coordinate transformations where transformed coordinates **Q** and **P** do not have explicit time dependence, i.e., ${\textstyle \mathbf {Q} =\mathbf {Q} (\mathbf {q} ,\mathbf {p} )}$ and ${\textstyle \mathbf {P} =\mathbf {P} (\mathbf {q} ,\mathbf {p} )}$ . The functional form of Hamilton's equations is

${\begin{aligned}{\dot {\mathbf {p} }}&=-{\frac {\partial H}{\partial \mathbf {q} }}\,,&{\dot {\mathbf {q} }}&={\frac {\partial H}{\partial \mathbf {p} }}\end{aligned}}$

In general, a transformation (**q**, **p**) → (**Q**, **P**) does not preserve the form of Hamilton's equations but in the case of a time independent transformation some simplifications are possible. Following the formal definition for a canonical transformation, it can be shown that for this type of transformation, the new Hamiltonian (sometimes called the Kamiltonian) can be expressed as:

$K(\mathbf {Q} ,\mathbf {P} ,t)=H(q(\mathbf {Q} ,\mathbf {P} ),p(\mathbf {Q} ,\mathbf {P} ),t)+{\frac {\partial G}{\partial t}}(t)$

where it differs from the Hamiltonian by a partial time derivative of a function known as a generator, which reduces to being only a function of time for restricted canonical transformations.

In addition to leaving the form of the Hamiltonian unchanged, the Kamiltonian also permits the use of the unchanged Hamiltonian in Hamilton's equations of motion due to the above form as:

${\begin{alignedat}{3}{\dot {\mathbf {P} }}&=-{\frac {\partial K}{\partial \mathbf {Q} }}&&=-\left({\frac {\partial H}{\partial \mathbf {Q} }}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\{\dot {\mathbf {Q} }}&=\,\,\,\,{\frac {\partial K}{\partial \mathbf {P} }}&&=\,\,\,\,\,\left({\frac {\partial H}{\partial \mathbf {P} }}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\\end{alignedat}}$

Although the class of canonical transformations is larger than that which can be obtained with this restricted formulation, the restricted version provides a good starting point to obtain results that can be further generalized. All of the following conditions, with the exception of bilinear invariance condition, can be generalized for the full class of canonical transformations, including time dependence.

### Indirect conditions

Since restricted transformations have no explicit time dependence (by definition), the time derivative of a new generalized coordinate *Qm* is

${\begin{aligned}{\dot {Q}}_{m}&={\frac {\partial Q_{m}}{\partial \mathbf {q} }}\cdot {\dot {\mathbf {q} }}+{\frac {\partial Q_{m}}{\partial \mathbf {p} }}\cdot {\dot {\mathbf {p} }}\\&={\frac {\partial Q_{m}}{\partial \mathbf {q} }}\cdot {\frac {\partial H}{\partial \mathbf {p} }}-{\frac {\partial Q_{m}}{\partial \mathbf {p} }}\cdot {\frac {\partial H}{\partial \mathbf {q} }}\\&=\lbrace Q_{m},H\rbrace \end{aligned}}$ where {⋅, ⋅} is the Poisson bracket.

Similarly for the identity for the conjugate momentum, *Pm* using the form of the "Kamiltonian" it follows that:

${\begin{aligned}{\frac {\partial K(\mathbf {Q} ,\mathbf {P} ,t)}{\partial P_{m}}}&={\frac {\partial K(\mathbf {Q} (\mathbf {q} ,\mathbf {p} ),\mathbf {P} (\mathbf {q} ,\mathbf {p} ),t)}{\partial \mathbf {q} }}\cdot {\frac {\partial \mathbf {q} }{\partial P_{m}}}+{\frac {\partial K(\mathbf {Q} (\mathbf {q} ,\mathbf {p} ),\mathbf {P} (\mathbf {q} ,\mathbf {p} ),t)}{\partial \mathbf {p} }}\cdot {\frac {\partial \mathbf {p} }{\partial P_{m}}}\\[1ex]&={\frac {\partial H(\mathbf {q} ,\mathbf {p} ,t)}{\partial \mathbf {q} }}\cdot {\frac {\partial \mathbf {q} }{\partial P_{m}}}+{\frac {\partial H(\mathbf {q} ,\mathbf {p} ,t)}{\partial \mathbf {p} }}\cdot {\frac {\partial \mathbf {p} }{\partial P_{m}}}\\[1ex]&={\frac {\partial H}{\partial \mathbf {q} }}\cdot {\frac {\partial \mathbf {q} }{\partial P_{m}}}+{\frac {\partial H}{\partial \mathbf {p} }}\cdot {\frac {\partial \mathbf {p} }{\partial P_{m}}}\end{aligned}}$

Due to the form of the Hamiltonian equations of motion,

${\begin{aligned}{\dot {\mathbf {P} }}&=-{\frac {\partial K}{\partial \mathbf {Q} }}\\{\dot {\mathbf {Q} }}&=\,\,\,\,{\frac {\partial K}{\partial \mathbf {P} }}\end{aligned}}$

if the transformation is canonical, the two derived results must be equal, resulting in the equations:

${\begin{aligned}\left({\frac {\partial Q_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} }&=-\left({\frac {\partial q_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} }\\\left({\frac {\partial Q_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} }&=\left({\frac {\partial p_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} }\end{aligned}}$

The analogous argument for the generalized momenta *Pm* leads to two other sets of equations:

${\begin{aligned}\left({\frac {\partial P_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} }&=\left({\frac {\partial q_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} }\\\left({\frac {\partial P_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} }&=-\left({\frac {\partial p_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} }\end{aligned}}$

These are the **indirect conditions** to check whether a given transformation is canonical.

### Symplectic condition

Sometimes the Hamiltonian relations are represented as:

${\dot {\eta }}=J\nabla _{\eta }H$

Where ${\textstyle J:={\begin{pmatrix}0&I_{n}\\-I_{n}&0\\\end{pmatrix}},}$

and ${\textstyle \mathbf {\eta } ={\begin{bmatrix}q_{1}\\\vdots \\q_{n}\\p_{1}\\\vdots \\p_{n}\\\end{bmatrix}}}$ . Similarly, let ${\textstyle \mathbf {\varepsilon } ={\begin{bmatrix}Q_{1}\\\vdots \\Q_{n}\\P_{1}\\\vdots \\P_{n}\\\end{bmatrix}}}$ .

From the relation of partial derivatives, converting the ${\dot {\eta }}=J\nabla _{\eta }H$ relation in terms of partial derivatives with new variables gives ${\dot {\eta }}=J(M^{T}\nabla _{\varepsilon }H)$ where ${\textstyle M:={\frac {\partial (\mathbf {Q} ,\mathbf {P} )}{\partial (\mathbf {q} ,\mathbf {p} )}}}$ . Similarly for ${\textstyle {\dot {\varepsilon }}}$ ,

${\dot {\varepsilon }}=M{\dot {\eta }}=MJM^{T}\nabla _{\varepsilon }H$

Due to form of the Hamiltonian equations for ${\textstyle {\dot {\varepsilon }}}$ ,

${\dot {\varepsilon }}=J\nabla _{\varepsilon }K=J\nabla _{\varepsilon }H$

where ${\textstyle \nabla _{\varepsilon }K=\nabla _{\varepsilon }H}$ can be used due to the form of Kamiltonian. Equating the two equations gives the symplectic condition as:

$MJM^{T}=J$

The left hand side of the above is called the Poisson matrix of $\varepsilon$ , denoted as ${\textstyle {\mathcal {P}}(\varepsilon )=MJM^{T}}$ . Similarly, a Lagrange matrix of $\eta$ can be constructed as ${\textstyle {\mathcal {L}}(\eta )=M^{T}JM}$ . It can be shown that the symplectic condition is also equivalent to ${\textstyle M^{T}JM=J}$ by using the ${\textstyle J^{-1}=-J}$ property. The set of all matrices ${\textstyle M}$ which satisfy symplectic conditions form a symplectic group. The symplectic conditions are equivalent with indirect conditions as they both lead to the equation ${\textstyle {\dot {\varepsilon }}=J\nabla _{\varepsilon }H}$ , which is used in both of the derivations.

### Invariance of the Poisson bracket

The Poisson bracket which is defined as: $\{u,v\}_{\eta }:=\sum _{i=1}^{n}\left({\frac {\partial u}{\partial q_{i}}}{\frac {\partial v}{\partial p_{i}}}-{\frac {\partial u}{\partial p_{i}}}{\frac {\partial v}{\partial q_{i}}}\right)$ can be represented in matrix form as:

$\{u,v\}_{\eta }:=(\nabla _{\eta }u)^{T}J(\nabla _{\eta }v)$

Hence using partial derivative relations and symplectic condition gives: $\{u,v\}_{\eta }=(\nabla _{\eta }u)^{T}J(\nabla _{\eta }v)=(M^{T}\nabla _{\varepsilon }u)^{T}J(M^{T}\nabla _{\varepsilon }v)=(\nabla _{\varepsilon }u)^{T}MJM^{T}(\nabla _{\varepsilon }v)=(\nabla _{\varepsilon }u)^{T}J(\nabla _{\varepsilon }v)=\{u,v\}_{\varepsilon }$

The symplectic condition can also be recovered by taking ${\textstyle u=\varepsilon _{i}}$ and ${\textstyle v=\varepsilon _{j}}$ which shows that ${\textstyle (MJM^{T})_{ij}=J_{ij}}$ . Thus these conditions are equivalent to symplectic conditions. Furthermore, it can be seen that ${\textstyle {\mathcal {P}}_{ij}(\varepsilon )=\{\varepsilon _{i},\varepsilon _{j}\}_{\eta }=(MJM^{T})_{ij}}$ , which is also the result of explicitly calculating the matrix element by expanding it.

### Invariance of the Lagrange bracket

The Lagrange bracket which is defined as:

$[u,v]_{\eta }:=\sum _{i=1}^{n}\left({\frac {\partial q_{i}}{\partial u}}{\frac {\partial p_{i}}{\partial v}}-{\frac {\partial p_{i}}{\partial u}}{\frac {\partial q_{i}}{\partial v}}\right)$

can be represented in matrix form as:

$[u,v]_{\eta }:=\left({\frac {\partial \eta }{\partial u}}\right)^{T}J\left({\frac {\partial \eta }{\partial v}}\right)$

Using similar derivation, gives:

$[u,v]_{\varepsilon }=(\partial _{u}\varepsilon )^{T}\,J\,(\partial _{v}\varepsilon )=(M\,\partial _{u}\eta )^{T}\,J\,(M\,\partial _{v}\eta )=(\partial _{u}\eta )^{T}\,M^{T}JM\,(\partial _{v}\eta )=(\partial _{u}\eta )^{T}\,J\,(\partial _{v}\eta )=[u,v]_{\eta }$

The symplectic condition can also be recovered by taking ${\textstyle u=\eta _{i}}$ and ${\textstyle v=\eta _{j}}$ which shows that ${\textstyle (M^{T}JM)_{ij}=J_{ij}}$ . Thus these conditions are equivalent to symplectic conditions. Furthermore, it can be seen that ${\textstyle {\mathcal {L}}_{ij}(\eta )=[\eta _{i},\eta _{j}]_{\varepsilon }=(M^{T}JM)_{ij}}$ , which is also the result of explicitly calculating the matrix element by expanding it.

### Bilinear invariance conditions

These set of conditions only apply to restricted canonical transformations or canonical transformations that are independent of time variable.

Consider arbitrary variations of two kinds, in a single pair of generalized coordinate and the corresponding momentum:

${\textstyle d\varepsilon =(dq_{1},dp_{1},0,0,\ldots ),\quad \delta \varepsilon =(\delta q_{1},\delta p_{1},0,0,\ldots ).}$

The area of the infinitesimal parallelogram is given by:

${\textstyle \delta a(12)=dq_{1}\delta p_{1}-\delta q_{1}dp_{1}={(\delta \varepsilon )}^{T}\,J\,d\varepsilon .}$

It follows from the ${\textstyle M^{T}JM=J}$ symplectic condition that the infinitesimal area is conserved under canonical transformation:

${\textstyle \delta a(12)={(\delta \varepsilon )}^{T}\,J\,d\varepsilon ={(M\delta \eta )}^{T}\,J\,Md\eta ={(\delta \eta )}^{T}\,M^{T}JM\,d\eta ={(\delta \eta )}^{T}\,J\,d\eta =\delta A(12).}$

Note that the new coordinates need not be completely oriented in one coordinate momentum plane.

Hence, the condition is more generally stated as an invariance of the form ${\textstyle {(d\varepsilon )}^{T}\,J\,\delta \varepsilon }$ under canonical transformation, expanded as:

$\sum \delta q\cdot dp-\delta p\cdot dq=\sum \delta Q\cdot dP-\delta P\cdot dQ$

If the above is obeyed for any arbitrary variations, it would be only possible if the indirect conditions are met. The form of the equation, ${\textstyle {v}^{T}\,J\,w}$ is also known as a symplectic product of the vectors ${\textstyle {v}}$ and ${\textstyle w}$ and the bilinear invariance condition can be stated as a local conservation of the symplectic product.


## Liouville's theorem

The indirect conditions allow us to prove Liouville's theorem, which states that the *volume* in phase space is conserved under canonical transformations, i.e.,

$\int \mathrm {d} \mathbf {q} \,\mathrm {d} \mathbf {p} =\int \mathrm {d} \mathbf {Q} \,\mathrm {d} \mathbf {P}$

By calculus, the latter integral must equal the former times the determinant of Jacobian M

$\int \mathrm {d} \mathbf {Q} \,\mathrm {d} \mathbf {P} =\int \det(M)\,\mathrm {d} \mathbf {q} \,\mathrm {d} \mathbf {p}$ Where ${\textstyle M:={\frac {\partial (\mathbf {Q} ,\mathbf {P} )}{\partial (\mathbf {q} ,\mathbf {p} )}}}$

Exploiting the "division" property of Jacobians yields $M\equiv {\frac {\partial (\mathbf {Q} ,\mathbf {P} )}{\partial (\mathbf {q} ,\mathbf {P} )}}\left/{\frac {\partial (\mathbf {q} ,\mathbf {p} )}{\partial (\mathbf {q} ,\mathbf {P} )}}\right.$

Eliminating the repeated variables gives $M\equiv {\frac {\partial (\mathbf {Q} )}{\partial (\mathbf {q} )}}\left/{\frac {\partial (\mathbf {p} )}{\partial (\mathbf {P} )}}\right.$

Application of the **indirect conditions** above yields $\operatorname {det} (M)=1$ .


## Generating function approach

To *guarantee* a valid transformation between (**q**, **p**, *H*) and (**Q**, **P**, *K*), we may resort to a direct **generating function** approach. Both sets of variables must obey Hamilton's principle. That is the action integral over the Lagrangians ${\mathcal {L}}_{qp}=\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)$ and ${\mathcal {L}}_{QP}=\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)$ , obtained from the respective Hamiltonian via an "inverse" Legendre transformation, must be stationary in both cases (so that one can use the Euler–Lagrange equations to arrive at Hamiltonian equations of motion of the designated form; as it is shown for example here):

${\begin{aligned}\delta \int _{t_{1}}^{t_{2}}\left[\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)\right]dt&=0\\\delta \int _{t_{1}}^{t_{2}}\left[\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)\right]dt&=0\end{aligned}}$

One way for both variational integral equalities to be satisfied is to have

$\lambda \left[\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)\right]=\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {dG}{dt}}$

Lagrangians are not unique: one can always multiply by a constant λ and add a total time derivative ⁠*dG*/*dt*⁠ and yield the same equations of motion (as discussed on Wikibooks). In general, the scaling factor λ is set equal to one; canonical transformations for which *λ* ≠ 1 are called **extended canonical transformations**. ⁠*dG*/*dt*⁠ is kept, otherwise the problem would be rendered trivial and there would be not much freedom for the new canonical variables to differ from the old ones.

Here G is a generating function of one old canonical coordinate (**q** or **p**), one new canonical coordinate (**Q** or **P**) and (possibly) the time t. Thus, there are four basic types of generating functions (although mixtures of these four types can exist), depending on the choice of variables. As will be shown below, the generating function will define a transformation from old to new canonical coordinates, and any such transformation (**q**, **p**) → (**Q**, **P**) is guaranteed to be canonical.

The various generating functions and its properties tabulated below is discussed in detail:

| Generating function | Generating function derivatives | Transformed Hamiltonian | Trivial cases |   |   |   |
|---|---|---|---|---|---|---|
| $G=G_{1}(q,Q,t)$ | $p={\frac {\partial G_{1}}{\partial q}}$ | $P=-{\frac {\partial G_{1}}{\partial Q}}$ | ${\textstyle K=H+{\frac {\partial G}{\partial t}}}$ | $G_{1}=qQ$ | $Q=p$ | $P=-q$ |
| $G=G_{2}(q,P,t)-QP$ | $p={\frac {\partial G_{2}}{\partial q}}$ | $Q={\frac {\partial G_{2}}{\partial P}}$ | $G_{2}=qP$ | $Q=q$ | $P=p$ |   |
| $G=G_{3}(p,Q,t)+qp$ | $q=-{\frac {\partial G_{3}}{\partial p}}$ | $P=-{\frac {\partial G_{3}}{\partial Q}}$ | $G_{3}=pQ$ | $Q=-q$ | $P=-p$ |   |
| $G=G_{4}(p,P,t)+qp-QP$ | $q=-{\frac {\partial G_{4}}{\partial p}}$ | $Q={\frac {\partial G_{4}}{\partial P}}$ | $G_{4}=pP$ | $Q=p$ | $P=-q$ |   |

### Type 1 generating function

The type 1 generating function *G*1 depends only on the old and new generalized coordinates ${\textstyle G\equiv G_{1}(\mathbf {q} ,\mathbf {Q} ,t)}$ . To derive the implicit transformation, we expand the defining equation above $\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)=\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {\partial G_{1}}{\partial t}}+{\frac {\partial G_{1}}{\partial \mathbf {q} }}\cdot {\dot {\mathbf {q} }}+{\frac {\partial G_{1}}{\partial \mathbf {Q} }}\cdot {\dot {\mathbf {Q} }}$

Since the new and old coordinates are each independent, the following 2*N* + 1 equations must hold

${\begin{aligned}\mathbf {p} &={\frac {\partial G_{1}}{\partial \mathbf {q} }}\\\mathbf {P} &=-{\frac {\partial G_{1}}{\partial \mathbf {Q} }}\\K&=H+{\frac {\partial G_{1}}{\partial t}}\end{aligned}}$

These equations define the transformation (**q**, **p**) → (**Q**, **P**) as follows: The *first* set of N equations ${\textstyle \ \mathbf {p} ={\frac {\ \partial G_{1}\ }{\partial \mathbf {q} }}\ }$ define relations between the new generalized coordinates **Q** and the old canonical coordinates (**q**, **p**). Ideally, one can invert these relations to obtain formulae for each *Qk* as a function of the old canonical coordinates. Substitution of these formulae for the **Q** coordinates into the *second* set of N equations ${\textstyle \mathbf {P} =-{\frac {\partial G_{1}}{\partial \mathbf {Q} }}}$ yields analogous formulae for the new generalized momenta **P** in terms of the old canonical coordinates (**q**, **p**). We then invert both sets of formulae to obtain the *old* canonical coordinates (**q**, **p**) as functions of the *new* canonical coordinates (**Q**, **P**). Substitution of the inverted formulae into the final equation ${\textstyle K=H+{\frac {\partial G_{1}}{\partial t}}}$ yields a formula for K as a function of the new canonical coordinates (**Q**, **P**).

In practice, this procedure is easier than it sounds, because the generating function is usually simple. For example, let ${\textstyle G_{1}\equiv \mathbf {q} \cdot \mathbf {Q} }$ . This results in swapping the generalized coordinates for the momenta and vice versa

${\begin{aligned}\mathbf {p} &={\frac {\partial G_{1}}{\partial \mathbf {q} }}=\mathbf {Q} \\\mathbf {P} &=-{\frac {\partial G_{1}}{\partial \mathbf {Q} }}=-\mathbf {q} \end{aligned}}$

and *K* = *H*. This example illustrates how independent the coordinates and momenta are in the Hamiltonian formulation; they are equivalent variables.

### Type 2 generating function

The type 2 generating function $G_{2}(\mathbf {q} ,\mathbf {P} ,t)$ depends only on the old generalized coordinates and the new generalized momenta ${\textstyle G\equiv G_{2}(\mathbf {q} ,\mathbf {P} ,t)-\mathbf {Q} \cdot \mathbf {P} }$ where the $-\mathbf {Q} \cdot \mathbf {P}$ terms represent a Legendre transformation to change the right-hand side of the equation below. To derive the implicit transformation, we expand the defining equation above

$\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)=-\mathbf {Q} \cdot {\dot {\mathbf {P} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {\partial G_{2}}{\partial t}}+{\frac {\partial G_{2}}{\partial \mathbf {q} }}\cdot {\dot {\mathbf {q} }}+{\frac {\partial G_{2}}{\partial \mathbf {P} }}\cdot {\dot {\mathbf {P} }}$

Since the old coordinates and new momenta are each independent, the following 2*N* + 1 equations must hold

${\begin{aligned}\mathbf {p} &={\frac {\partial G_{2}}{\partial \mathbf {q} }}\\\mathbf {Q} &={\frac {\partial G_{2}}{\partial \mathbf {P} }}\\K&=H+{\frac {\partial G_{2}}{\partial t}}\end{aligned}}$

These equations define the transformation (**q**, **p**) → (**Q**, **P**) as follows: The *first* set of N equations ${\textstyle \mathbf {p} ={\frac {\partial G_{2}}{\partial \mathbf {q} }}}$ define relations between the new generalized momenta **P** and the old canonical coordinates (**q**, **p**). Ideally, one can invert these relations to obtain formulae for each *Pk* as a function of the old canonical coordinates. Substitution of these formulae for the **P** coordinates into the *second* set of N equations ${\textstyle \mathbf {Q} ={\frac {\partial G_{2}}{\partial \mathbf {P} }}}$ yields analogous formulae for the new generalized coordinates **Q** in terms of the old canonical coordinates (**q**, **p**). We then invert both sets of formulae to obtain the *old* canonical coordinates (**q**, **p**) as functions of the *new* canonical coordinates (**Q**, **P**). Substitution of the inverted formulae into the final equation ${\textstyle K=H+{\frac {\partial G_{2}}{\partial t}}}$ yields a formula for K as a function of the new canonical coordinates (**Q**, **P**).

In practice, this procedure is easier than it sounds, because the generating function is usually simple. For example, let ${\textstyle G_{2}\equiv \mathbf {g} (\mathbf {q} ;t)\cdot \mathbf {P} }$ where **g** is a set of N functions. This results in a point transformation of the generalized coordinates ${\textstyle \mathbf {Q} ={\frac {\partial G_{2}}{\partial \mathbf {P} }}=\mathbf {g} (\mathbf {q} ;t)}$ .

### Type 3 generating function

The type 3 generating function $G_{3}(\mathbf {p} ,\mathbf {Q} ,t)$ depends only on the old generalized momenta and the new generalized coordinates ${\textstyle G\equiv G_{3}(\mathbf {p} ,\mathbf {Q} ,t)+\mathbf {q} \cdot \mathbf {p} }$ where the $\mathbf {q} \cdot \mathbf {p}$ terms represent a Legendre transformation to change the left-hand side of the equation below. To derive the implicit transformation, we expand the defining equation above $-\mathbf {q} \cdot {\dot {\mathbf {p} }}-H(\mathbf {q} ,\mathbf {p} ,t)=\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {\partial G_{3}}{\partial t}}+{\frac {\partial G_{3}}{\partial \mathbf {p} }}\cdot {\dot {\mathbf {p} }}+{\frac {\partial G_{3}}{\partial \mathbf {Q} }}\cdot {\dot {\mathbf {Q} }}$

Since the new and old coordinates are each independent, the following 2*N* + 1 equations must hold

${\begin{aligned}\mathbf {q} &=-{\frac {\partial G_{3}}{\partial \mathbf {p} }}\\\mathbf {P} &=-{\frac {\partial G_{3}}{\partial \mathbf {Q} }}\\K&=H+{\frac {\partial G_{3}}{\partial t}}\end{aligned}}$

These equations define the transformation (**q**, **p**) → (**Q**, **P**) as follows: The *first* set of N equations ${\textstyle \mathbf {q} =-{\frac {\partial G_{3}}{\partial \mathbf {p} }}}$ define relations between the new generalized coordinates **Q** and the old canonical coordinates (**q**, **p**). Ideally, one can invert these relations to obtain formulae for each *Qk* as a function of the old canonical coordinates. Substitution of these formulae for the **Q** coordinates into the *second* set of N equations ${\textstyle \mathbf {P} =-{\frac {\partial G_{3}}{\partial \mathbf {Q} }}}$ yields analogous formulae for the new generalized momenta **P** in terms of the old canonical coordinates (**q**, **p**). We then invert both sets of formulae to obtain the *old* canonical coordinates (**q**, **p**) as functions of the *new* canonical coordinates (**Q**, **P**). Substitution of the inverted formulae into the final equation ${\textstyle K=H+{\frac {\partial G_{3}}{\partial t}}}$ yields a formula for K as a function of the new canonical coordinates (**Q**, **P**).

In practice, this procedure is easier than it sounds, because the generating function is usually simple.

### Type 4 generating function

The type 4 generating function $G_{4}(\mathbf {p} ,\mathbf {P} ,t)$ depends only on the old and new generalized momenta ${\textstyle G\equiv G_{4}(\mathbf {p} ,\mathbf {P} ,t)+\mathbf {q} \cdot \mathbf {p} -\mathbf {Q} \cdot \mathbf {P} }$ where the $\mathbf {q} \cdot \mathbf {p} -\mathbf {Q} \cdot \mathbf {P}$ terms represent a Legendre transformation to change both sides of the equation below. To derive the implicit transformation, we expand the defining equation above

$-\mathbf {q} \cdot {\dot {\mathbf {p} }}-H(\mathbf {q} ,\mathbf {p} ,t)=-\mathbf {Q} \cdot {\dot {\mathbf {P} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {\partial G_{4}}{\partial t}}+{\frac {\partial G_{4}}{\partial \mathbf {p} }}\cdot {\dot {\mathbf {p} }}+{\frac {\partial G_{4}}{\partial \mathbf {P} }}\cdot {\dot {\mathbf {P} }}$

Since the new and old coordinates are each independent, the following 2*N* + 1 equations must hold

${\begin{aligned}\mathbf {q} &=-{\frac {\partial G_{4}}{\partial \mathbf {p} }}\\\mathbf {Q} &={\frac {\partial G_{4}}{\partial \mathbf {P} }}\\K&=H+{\frac {\partial G_{4}}{\partial t}}\end{aligned}}$

These equations define the transformation (**q**, **p**) → (**Q**, **P**) as follows: The *first* set of N equations ${\textstyle \mathbf {q} =-{\frac {\partial G_{4}}{\partial \mathbf {p} }}}$ define relations between the new generalized momenta **P** and the old canonical coordinates (**q**, **p**). Ideally, one can invert these relations to obtain formulae for each *Pk* as a function of the old canonical coordinates. Substitution of these formulae for the **P** coordinates into the *second* set of N equations ${\textstyle \mathbf {Q} ={\frac {\partial G_{4}}{\partial \mathbf {P} }}}$ yields analogous formulae for the new generalized coordinates **Q** in terms of the old canonical coordinates (**q**, **p**). We then invert both sets of formulae to obtain the *old* canonical coordinates (**q**, **p**) as functions of the *new* canonical coordinates (**Q**, **P**). Substitution of the inverted formulae into the final equation ${\textstyle K=H+{\frac {\partial G_{4}}{\partial t}}}$ yields a formula for K as a function of the new canonical coordinates (**Q**, **P**).

### Limitations on the four types of generating functions

Considering $G_{2}(\mathbf {q} ,\mathbf {P} ,t)$ as an example, using generating function of second kind: ${\textstyle {p}_{i}={\frac {\partial G_{2}}{\partial {q}_{i}}}}$ and ${\textstyle {Q}_{i}={\frac {\partial G_{2}}{\partial {P}_{i}}}}$ , the first set of equations consisting of variables ${\textstyle \mathbf {p} }$ , ${\textstyle \mathbf {q} }$ and ${\textstyle \mathbf {P} }$ has to be inverted to get ${\textstyle \mathbf {P} (\mathbf {q} ,\mathbf {p} )}$ . This process is possible when the matrix defined by ${\textstyle a_{ij}={\frac {\partial {p}_{i}(\mathbf {q} ,\mathbf {P} )}{\partial P_{j}}}}$ is non-singular using the inverse function theorem, and can be restated as the following relation.

$\left|{\begin{array}{l l l}{\displaystyle {\frac {\partial ^{2}G_{2}}{\partial P_{1}\partial q_{1}}}}&{\cdots }&{\displaystyle {\frac {\partial ^{2}G_{2}}{\partial P_{1}\partial q_{n}}}}\\{\quad \vdots }&{\ddots }&{\quad \vdots }\\{\displaystyle {\frac {\partial ^{2}G_{2}}{\partial P_{n}\partial q_{1}}}}&{\cdots }&{\displaystyle {\frac {\partial ^{2}G_{2}}{\partial P_{n}\partial q_{n}}}}\end{array}}\right|{\neq 0}$

Hence, restrictions are placed on generating functions to have the matrices: ${\textstyle \left[{\frac {\partial ^{2}G_{1}}{\partial Q_{j}\partial q_{i}}}\right]}$ , ${\textstyle \left[{\frac {\partial ^{2}G_{2}}{\partial P_{j}\partial q_{i}}}\right]}$ , ${\textstyle \left[{\frac {\partial ^{2}G_{3}}{\partial p_{j}\partial Q_{i}}}\right]}$ and ${\textstyle \left[{\frac {\partial ^{2}G_{4}}{\partial p_{j}\partial P_{i}}}\right]}$ , being non-singular. These conditions also correspond to local invertibility of the coordinates. From these restrictions, it can be stated that type 1 and type 4 generating functions always have a non-singular ${\textstyle \left[{\frac {\partial Q_{i}(\mathbf {q} ,\mathbf {p} )}{\partial p_{j}}}\right]}$ matrix whereas type 2 and type 3 generating functions always have a non-singular ${\textstyle \left[{\frac {\partial P_{i}(\mathbf {q} ,\mathbf {p} )}{\partial p_{j}}}\right]}$ matrix. Hence, the canonical transformations resulting from these four generating functions alone are not completely general.

### Generalized use of generating functions

In other words, since (**Q**, **P**) and (**q**, **p**) are each 2*N* independent functions, it follows that to have generating function of the form ${\textstyle G_{1}(\mathbf {q} ,\mathbf {Q} ,t)}$ and $G_{4}(\mathbf {p} ,\mathbf {P} ,t)$ or $G_{2}(\mathbf {q} ,\mathbf {P} ,t)$ and $G_{3}(\mathbf {p} ,\mathbf {Q} ,t)$ , the corresponding Jacobian matrices ${\textstyle \left[{\frac {\partial Q_{i}}{\partial p_{j}}}\right]}$ and ${\textstyle \left[{\frac {\partial P_{i}}{\partial p_{j}}}\right]}$ are restricted to be non singular, ensuring that the generating function is a function of 2*N* + 1 independent variables. However, as a feature of canonical transformations, it is always possible to choose 2*N* such independent functions from sets (**q**, **p**) or (**Q**, **P**), to form a generating function representation of canonical transformations, including the time variable. Hence, it can be proven that every finite canonical transformation can be given as a closed but implicit form that is a variant of the given four simple forms.

| Proof |
|---|
| Consider taking a full set of generalized coordinates ${\textstyle \{q_{1},q_{2},\ldots ,q_{N-1},q_{N}\}}$ and adding to the set, while preserving local invertibility of coordinates in the set, as many transformed coordinates as possible, labelled ${\textstyle \{Q_{1},Q_{2},\ldots ,Q_{k}\}}$ without loss of generality. It can be shown that the set, ${\textstyle \{q_{1},\ldots ,q_{N},Q_{1},\ldots ,Q_{k},P_{k+1},\ldots ,P_{N}\}}$ is a set of locally independent coordinates. Proof of local invertibility of the set of coordinates is given by proving non singularity of ${\textstyle {\frac {\partial (Q_{1},\ldots ,Q_{k},P_{k+1},\ldots ,P_{N})}{\partial (p_{1},\ldots ,p_{N})}}}$ or the non existence of a non trivial null eigenvector such that ${\textstyle \sum _{a}\epsilon _{a}{\frac {\partial Q_{a}}{\partial p_{s}}}+\sum _{b}\eta _{b}{\frac {\partial P_{b}}{\partial p_{s}}}=0,\,\forall s}$ where the index ${\textstyle a=1,\ldots ,k}$ and ${\textstyle b=k+1,\ldots ,N}$ . Letting ${\textstyle Q_{b}=f_{b}(q_{s},Q_{a})}$ and assuming the existence of a null eigenvector in the following derivation: ${\textstyle \eta _{b'}=\sum _{a}\epsilon _{a}\{Q_{b'},Q_{a}\}+\sum _{b}\eta _{b}\{Q_{b'},P_{b}\}=\sum _{s}{\frac {\partial f_{b'}}{\partial q_{s}}}(\sum _{a}\epsilon _{a}{\frac {\partial Q_{a}}{\partial p_{s}}}+\sum _{b}\eta _{b}{\frac {\partial P_{b}}{\partial p_{s}}})=0}$ Hence all ${\textstyle \eta _{b}=0}$ . By condition of local invertibility it follows that for the remaining part of the equation, ${\textstyle \sum {\frac {\partial Q_{a}}{\partial p_{i}}}\epsilon _{i}=\delta Q_{a}(p_{1},\ldots ,p_{N})=0\implies \epsilon _{i}=0\quad \forall \,a=1,\ldots ,k}$ thereby showing that the only null eigenvector ${\textstyle {\frac {\partial (Q_{1},\ldots ,Q_{k},P_{k+1},\ldots ,P_{N})}{\partial (p_{1},\ldots ,p_{N})}}}$ is the trivial vector implying that it is a non singular matrix. Hence it is shown that it is possible to take sets such as ${\textstyle \{q_{1},\ldots ,q_{N},Q_{1},\ldots ,Q_{k},P_{k+1},\ldots ,P_{N}\}}$ that is a combination of new and old coordinates that preserves the 2*N* independent variables property which can be used to interpret any coordinate transform as arising from a generating function on these set of coordinates. |


## Canonical transformation conditions

### Canonical transformation relations

From: $K=H+{\frac {\partial G}{\partial t}}$ , calculate ${\textstyle {\frac {\partial (K-H)}{\partial P}}}$ :

${\begin{aligned}\left({\frac {\partial (K-H)}{\partial P}}\right)_{Q,P,t}&={\frac {\partial K}{\partial P}}-{\frac {\partial H}{\partial p}}{\frac {\partial p}{\partial P}}-{\frac {\partial H}{\partial q}}{\frac {\partial q}{\partial P}}-{\frac {\partial H}{\partial t}}\left({\frac {\partial t}{\partial P}}\right)_{Q,P,t}\\&={\dot {Q}}+{\dot {p}}{\frac {\partial q}{\partial P}}-{\dot {q}}{\frac {\partial p}{\partial P}}\\&={\frac {\partial Q}{\partial t}}+{\frac {\partial Q}{\partial q}}\cdot {\dot {q}}+{\frac {\partial Q}{\partial p}}\cdot {\dot {p}}+{\dot {p}}{\frac {\partial q}{\partial P}}-{\dot {q}}{\frac {\partial p}{\partial P}}\\&={\dot {q}}\left({\frac {\partial Q}{\partial q}}-{\frac {\partial p}{\partial P}}\right)+{\dot {p}}\left({\frac {\partial q}{\partial P}}+{\frac {\partial Q}{\partial p}}\right)+{\frac {\partial Q}{\partial t}}\end{aligned}}$ Since the left hand side is ${\textstyle {\frac {\partial (K-H)}{\partial P}}={\frac {\partial }{\partial P}}\left({\frac {\partial G}{\partial t}}\right){\bigg |}_{Q,P,t}}$ which is independent of dynamics of the particles, equating coefficients of ${\textstyle {\dot {q}}}$ and ${\textstyle {\dot {p}}}$ to zero, canonical transformation rules are obtained. This step is equivalent to equating the left hand side as ${\textstyle {\frac {\partial (K-H)}{\partial P}}={\frac {\partial Q}{\partial t}}}$ .

Since the left hand side is ${\textstyle {\frac {\partial (K-H)}{\partial P}}={\frac {\partial }{\partial P}}\left({\frac {\partial G}{\partial t}}\right){\bigg |}_{Q,P,t}}$ which is independent of dynamics of the particles, equating coefficients of ${\textstyle {\dot {q}}}$ and ${\textstyle {\dot {p}}}$ to zero, canonical transformation rules are obtained. This step is equivalent to equating the left hand side as ${\textstyle {\frac {\partial (K-H)}{\partial P}}={\frac {\partial Q}{\partial t}}}$ .

Similarly:

${\begin{aligned}\left({\frac {\partial (K-H)}{\partial Q}}\right)_{Q,P,t}&={\frac {\partial K}{\partial Q}}-{\frac {\partial H}{\partial p}}{\frac {\partial p}{\partial Q}}-{\frac {\partial H}{\partial q}}{\frac {\partial q}{\partial Q}}-{\frac {\partial H}{\partial t}}\left({\frac {\partial t}{\partial Q}}\right)_{Q,P,t}\\&=-{\dot {P}}+{\dot {p}}{\frac {\partial q}{\partial Q}}-{\dot {q}}{\frac {\partial p}{\partial Q}}\\&=-{\frac {\partial P}{\partial t}}-{\frac {\partial P}{\partial q}}\cdot {\dot {q}}-{\frac {\partial P}{\partial p}}\cdot {\dot {p}}+{\dot {p}}{\frac {\partial q}{\partial Q}}-{\dot {q}}{\frac {\partial p}{\partial Q}}\\&=-\left({\dot {q}}\left({\frac {\partial P}{\partial q}}+{\frac {\partial p}{\partial Q}}\right)+{\dot {p}}\left({\frac {\partial P}{\partial p}}-{\frac {\partial q}{\partial Q}}\right)+{\frac {\partial P}{\partial t}}\right)\end{aligned}}$

Similarly the canonical transformation rules are obtained by equating the left hand side as ${\textstyle {\frac {\partial (K-H)}{\partial Q}}=-{\frac {\partial P}{\partial t}}}$ .

The above two relations can be combined in matrix form as: ${\textstyle J\left(\nabla _{\varepsilon }{\frac {\partial G}{\partial t}}\right)={\frac {\partial \varepsilon }{\partial t}}}$ (which will also retain same form for extended canonical transformation) where the result ${\textstyle {\frac {\partial G}{\partial t}}=K-H}$ , has been used. The canonical transformation relations are hence said to be equivalent to ${\textstyle J\left(\nabla _{\varepsilon }{\frac {\partial G}{\partial t}}\right)={\frac {\partial \varepsilon }{\partial t}}}$ in this context.

The canonical transformation relations can now be restated to include time dependence:

${\begin{aligned}\left({\frac {\partial Q_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=-\left({\frac {\partial q_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\\left({\frac {\partial Q_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=\left({\frac {\partial p_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\end{aligned}}$

${\begin{aligned}\left({\frac {\partial P_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=\left({\frac {\partial q_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\\left({\frac {\partial P_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=-\left({\frac {\partial p_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\end{aligned}}$

Since ${\textstyle {\frac {\partial (K-H)}{\partial P}}={\frac {\partial Q}{\partial t}}}$ and ${\textstyle {\frac {\partial (K-H)}{\partial Q}}=-{\frac {\partial P}{\partial t}}}$ , if **Q** and **P** do not explicitly depend on time, ${\textstyle K=H+{\frac {\partial G}{\partial t}}(t)}$ can be taken. The analysis of restricted canonical transformations is hence consistent with this generalization.

### Symplectic condition

Applying transformation of coordinates formula for $\nabla _{\eta }H=M^{T}\nabla _{\varepsilon }H$ , in Hamiltonian's equations gives:

${\dot {\eta }}=J\nabla _{\eta }H=J(M^{T}\nabla _{\varepsilon }H)$

Similarly for ${\textstyle {\dot {\varepsilon }}}$ :

${\dot {\varepsilon }}=M{\dot {\eta }}+{\frac {\partial \varepsilon }{\partial t}}=MJM^{T}\nabla _{\varepsilon }H+{\frac {\partial \varepsilon }{\partial t}}$

or:

${\dot {\varepsilon }}=J\nabla _{\varepsilon }K=J\nabla _{\varepsilon }H+J\nabla _{\varepsilon }\left({\frac {\partial G}{\partial t}}\right)$

Where the last terms of each equation cancel due to ${\textstyle J\left(\nabla _{\varepsilon }{\frac {\partial G}{\partial t}}\right)={\frac {\partial \varepsilon }{\partial t}}}$ condition from canonical transformations. Hence leaving the symplectic relation: ${\textstyle MJM^{T}=J}$ which is also equivalent with the condition ${\textstyle M^{T}JM=J}$ . It follows from the above two equations that the symplectic condition implies the equation ${\textstyle J\left(\nabla _{\varepsilon }{\frac {\partial G}{\partial t}}\right)={\frac {\partial \varepsilon }{\partial t}}}$ , from which the indirect conditions can be recovered. Thus, symplectic conditions and indirect conditions can be said to be equivalent in the context of using generating functions.

### Invariance of the Poisson and Lagrange brackets

Since ${\textstyle {\mathcal {P}}_{ij}(\varepsilon )=\{\varepsilon _{i},\varepsilon _{j}\}_{\eta }=(MJM^{T})_{ij}=J_{ij}}$ and ${\textstyle {\mathcal {L}}_{ij}(\eta )=[\eta _{i},\eta _{j}]_{\varepsilon }=(M^{T}JM)_{ij}=J_{ij}}$ where the symplectic condition is used in the last equalities. Using ${\textstyle \{\varepsilon _{i},\varepsilon _{j}\}_{\varepsilon }=[\eta _{i},\eta _{j}]_{\eta }=J_{ij}}$ , the equalities ${\textstyle \{\varepsilon _{i},\varepsilon _{j}\}_{\eta }=\{\varepsilon _{i},\varepsilon _{j}\}_{\varepsilon }}$ and ${\textstyle [\eta _{i},\eta _{j}]_{\varepsilon }=[\eta _{i},\eta _{j}]_{\eta }}$ are obtained which imply the invariance of Poisson and Lagrange brackets.


## Extended canonical transformation

### Canonical transformation relations

By solving for:

$\lambda \left[\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t)\right]=\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)+{\frac {dG}{dt}}$

with various forms of generating function, the relation between K and H goes as ${\textstyle {\frac {\partial G}{\partial t}}=K-\lambda H}$ instead, which also applies for ${\textstyle \lambda =1}$ case.

All results presented below can also be obtained by replacing ${\textstyle q\rightarrow {\sqrt {\lambda }}q}$ , ${\textstyle p\rightarrow {\sqrt {\lambda }}p}$ and ${\textstyle H\rightarrow {\lambda }H}$ from known solutions, since it retains the form of Hamilton's equations. The extended canonical transformations are hence said to be result of a canonical transformation ( ${\textstyle \lambda =1}$ ) and a trivial canonical transformation ( ${\textstyle \lambda \neq 1}$ ) which has ${\textstyle MJM^{T}=\lambda J}$ (for the given example, ${\textstyle M={\sqrt {\lambda }}I}$ which satisfies the condition).

Using same steps previously used in previous generalization, with ${\textstyle {\frac {\partial G}{\partial t}}=K-\lambda H}$ in the general case, and retaining the equation ${\textstyle J\left(\nabla _{\varepsilon }{\frac {\partial g}{\partial t}}\right)={\frac {\partial \varepsilon }{\partial t}}}$ , extended canonical transformation partial differential relations are obtained as:

${\begin{aligned}\left({\frac {\partial Q_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=-\lambda \left({\frac {\partial q_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\\left({\frac {\partial Q_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=\lambda \left({\frac {\partial p_{n}}{\partial P_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\end{aligned}}$

${\begin{aligned}\left({\frac {\partial P_{m}}{\partial p_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=\lambda \left({\frac {\partial q_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\\\left({\frac {\partial P_{m}}{\partial q_{n}}}\right)_{\mathbf {q} ,\mathbf {p} ,t}&=-\lambda \left({\frac {\partial p_{n}}{\partial Q_{m}}}\right)_{\mathbf {Q} ,\mathbf {P} ,t}\end{aligned}}$

### Symplectic condition

Following the same steps to derive the symplectic conditions, as:

${\dot {\eta }}=J\nabla _{\eta }H=J(M^{T}\nabla _{\varepsilon }H)$

and

${\dot {\varepsilon }}=M{\dot {\eta }}+{\frac {\partial \varepsilon }{\partial t}}=MJM^{T}\nabla _{\varepsilon }H+{\frac {\partial \varepsilon }{\partial t}}$ where using ${\textstyle {\frac {\partial G}{\partial t}}=K-\lambda H}$ instead gives:

${\dot {\varepsilon }}=J\nabla _{\varepsilon }K=\lambda J\nabla _{\varepsilon }H+J\nabla _{\varepsilon }\left({\frac {\partial G}{\partial t}}\right)$

The second part of each equation cancel. Hence the condition for extended canonical transformation instead becomes: ${\textstyle MJM^{T}=\lambda J}$ .

### Poisson and Lagrange brackets

The Poisson brackets are changed as follows:

$\{u,v\}_{\eta }=(\nabla _{\eta }u)^{T}J(\nabla _{\eta }v)=(M^{T}\nabla _{\varepsilon }u)^{T}J(M^{T}\nabla _{\varepsilon }v)=(\nabla _{\varepsilon }u)^{T}MJM^{T}(\nabla _{\varepsilon }v)=\lambda (\nabla _{\varepsilon }u)^{T}J(\nabla _{\varepsilon }v)=\lambda \{u,v\}_{\varepsilon }$

whereas, the Lagrange brackets are changed as:

$[u,v]_{\varepsilon }=(\partial _{u}\varepsilon )^{T}\,J\,(\partial _{v}\varepsilon )=(M\,\partial _{u}\eta )^{T}\,J\,(M\,\partial _{v}\eta )=(\partial _{u}\eta )^{T}\,M^{T}JM\,(\partial _{v}\eta )=\lambda (\partial _{u}\eta )^{T}\,J\,(\partial _{v}\eta )=\lambda [u,v]_{\eta }$

Hence, the Poisson bracket scales by the inverse of ${\textstyle \lambda }$ whereas the Lagrange bracket scales by a factor of ${\textstyle \lambda }$ .
