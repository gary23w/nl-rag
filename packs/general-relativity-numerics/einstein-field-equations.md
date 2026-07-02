---
title: "Einstein field equations"
source: https://en.wikipedia.org/wiki/Einstein_field_equations
domain: general-relativity-numerics
license: CC-BY-SA-4.0
tags: numerical relativity, einstein field equations, adm formalism, gravitational wave modeling
fetched: 2026-07-02
---

# Einstein field equations

In the general theory of relativity, the **Einstein field equations** (**EFE**; also known as **Einstein's equations**) relate the geometry of spacetime to the distribution of matter-energy within it.

The equations were published by Albert Einstein in 1915 in the form of a tensor equation which related the local *spacetime curvature* (expressed by the Einstein tensor) with the local energy, momentum and stress within that spacetime (expressed by the stress–energy tensor).

Analogously to the way that electromagnetic fields are related to the distribution of charges and currents via Maxwell's equations, the EFE relate the spacetime geometry to the distribution of mass–energy, momentum and stress, that is, they determine the metric tensor of spacetime for a given arrangement of stress–energy–momentum in the spacetime. The relationship between the metric tensor and the Einstein tensor allows the EFE to be written as a set of nonlinear partial differential equations when used in this way. The solutions of the EFE are the components of the metric tensor. The inertial trajectories of particles and radiation (geodesics) in the resulting geometry are then calculated using the geodesic equation.

As well as implying local energy–momentum conservation, the EFE reduce to Newton's law of gravitation in the limit of a weak gravitational field and velocities that are much less than the speed of light.

Exact solutions for the EFE can only be found under simplifying assumptions such as symmetry. Special classes of exact solutions are most often studied since they model many gravitational phenomena, such as rotating black holes and the expanding universe. Further simplification is achieved in approximating the spacetime as having only small deviations from flat spacetime, leading to the linearized EFE. These equations are used to study phenomena such as gravitational waves.

## Mathematical form

The Einstein field equations (EFE) may be written in the form:

$G_{\mu \nu }+\Lambda g_{\mu \nu }=\kappa T_{\mu \nu },$

where $G_{\mu \nu }$ is the Einstein tensor, $g_{\mu \nu }$ is the metric tensor, $T_{\mu \nu }$ is the stress–energy tensor, $\Lambda$ is the cosmological constant and $\kappa$ is the Einstein gravitational constant.

The Einstein tensor is defined as

$G_{\mu \nu }=R_{\mu \nu }-{\frac {1}{2}}Rg_{\mu \nu },$

where $R_{\mu \nu }$ is the Ricci curvature tensor, and R is the scalar curvature. This is a symmetric divergenceless second-degree tensor that depends on only the metric tensor and its first and second derivatives.

The **Einstein gravitational constant** is defined as

$\kappa ={\frac {8\pi G}{c^{4}}}\approx 2.07665\times 10^{-43}\,{\textrm {N}}^{-1},$

where G is the Newtonian constant of gravitation and c is the speed of light in vacuum.

The EFE can thus also be written as

$R_{\mu \nu }-{\frac {1}{2}}Rg_{\mu \nu }+\Lambda g_{\mu \nu }=\kappa T_{\mu \nu }.$

In standard units, each term on the left has quantity dimension of L−2.

The expression on the left represents the curvature of spacetime as determined by the metric; the expression on the right represents the stress–energy–momentum content of spacetime. The EFE can then be interpreted as a set of equations dictating how stress–energy–momentum determines the curvature of spacetime.

These equations form the core of the mathematical formulation of general relativity. They readily imply the geodesic equation, which dictates how freely falling test objects move through spacetime.

The EFE is a tensor equation relating a set of symmetric 4 × 4 tensors. Each tensor has 10 independent components. The four Bianchi identities reduce the number of independent equations from 10 to 6, leaving the metric with four gauge-fixing degrees of freedom, which correspond to the freedom to choose a coordinate system.

Although the Einstein field equations were initially formulated in the context of a four-dimensional theory, some theorists have explored their consequences in n dimensions. The equations in contexts outside of general relativity are still referred to as the Einstein field equations. The vacuum field equations (obtained when $T_{\mu \nu }$ is everywhere zero) define Einstein manifolds.

The equations are more complex than they appear. Given a specified distribution of matter and energy in the form of a stress–energy tensor, the EFE are understood to be equations for the metric tensor $g_{\mu \nu }$ , since both the Ricci tensor and scalar curvature depend on the metric in a complicated nonlinear manner. When fully written out, the EFE are a system of ten coupled, nonlinear, hyperbolic-elliptic partial differential equations.

### Sign convention

The above form of the EFE is the standard established by Misner, Thorne, and Wheeler (MTW). The authors analyzed conventions that exist and classified these according to three signs ([S1] [S2] [S3]): ${\begin{aligned}g_{\mu \nu }&=[S1]\times \operatorname {diag} (-1,+1,+1,+1)\\[6pt]{R^{\mu }}_{\alpha \beta \gamma }&=[S2]\times \left(\Gamma _{\alpha \gamma ,\beta }^{\mu }-\Gamma _{\alpha \beta ,\gamma }^{\mu }+\Gamma _{\sigma \beta }^{\mu }\Gamma _{\gamma \alpha }^{\sigma }-\Gamma _{\sigma \gamma }^{\mu }\Gamma _{\beta \alpha }^{\sigma }\right)\\[6pt]G_{\mu \nu }&=[S3]\times \kappa T_{\mu \nu }\end{aligned}}$

The third sign above is related to the choice of convention for the Ricci tensor: $R_{\mu \nu }=[S2]\times [S3]\times {R^{\alpha }}_{\mu \alpha \nu }$

With these definitions Misner, Thorne, and Wheeler classify themselves as (+ + +), whereas Weinberg (1972) is (+ − −), Peebles (1980) and Efstathiou et al. (1990) are (− + +), Rindler (2006), Atwater (1974), Collins Martin & Squires (1989) and Peacock (1999) are (− + −).

Authors including Einstein have used a different sign in their definition for the Ricci tensor which results in the sign of the constant on the right side being negative: $R_{\mu \nu }-{\frac {1}{2}}Rg_{\mu \nu }-\Lambda g_{\mu \nu }=-\kappa T_{\mu \nu }.$

The sign of the cosmological term would change in both these versions if the (+ − − −) metric sign convention is used rather than the MTW (− + + +) metric sign convention adopted here.

### Equivalent formulations

Taking the trace with respect to the metric of both sides of the EFE one gets $R-{\frac {D}{2}}R+D\Lambda =\kappa T,$ where D is the spacetime dimension. Solving for R and substituting this in the original EFE, one gets the following equivalent "trace-reversed" form: $R_{\mu \nu }-{\frac {2}{D-2}}\Lambda g_{\mu \nu }=\kappa \left(T_{\mu \nu }-{\frac {1}{D-2}}Tg_{\mu \nu }\right).$

In $D=4$ dimensions this reduces to $R_{\mu \nu }-\Lambda g_{\mu \nu }=\kappa \left(T_{\mu \nu }-{\frac {1}{2}}T\,g_{\mu \nu }\right).$

Reversing the trace again would restore the original EFE. The trace-reversed form may be more convenient in some cases (for example, when one is interested in weak-field limit and can replace $g_{\mu \nu }$ in the expression on the right with the Minkowski metric without significant loss of accuracy).

## Cosmological constant

In the Einstein field equations $G_{\mu \nu }+\Lambda g_{\mu \nu }=\kappa T_{\mu \nu }\,,$ the term containing the cosmological constant $\Lambda$ was absent from the version in which he originally published them. Einstein then included the term with the cosmological constant to allow for a universe that is not expanding or contracting. This effort was unsuccessful because:

- any desired steady state solution described by this equation is unstable, and
- observations by Edwin Hubble showed that our universe is expanding.

Einstein then abandoned $\Lambda$ , remarking to George Gamow "that the introduction of the cosmological term was the biggest blunder of his life".

The inclusion of this term does not create inconsistencies. For many years the cosmological constant was almost universally assumed to be zero. More recent astronomical observations have shown an accelerating expansion of the universe, and to explain this a positive value of $\Lambda$ is needed. The effect of the cosmological constant is negligible at the scale of a galaxy or smaller.

Einstein thought of the cosmological constant as an independent parameter, but its term in the field equation can also be moved algebraically to the other side and incorporated as part of the stress–energy tensor: $T_{\mu \nu }^{\mathrm {(vac)} }=-{\frac {\Lambda }{\kappa }}g_{\mu \nu }\,.$

This tensor describes a vacuum state with an energy density $\rho _{\text{vac}}$ and isotropic pressure $p_{\text{vac}}$ that are fixed constants and given by $\rho _{\mathrm {vac} }=-p_{\mathrm {vac} }={\frac {\Lambda }{\kappa }},$ where it is assumed that $\Lambda$ has SI unit m−2 and $\kappa$ is defined as above.

The existence of a cosmological constant is thus equivalent to the existence of a vacuum energy and a pressure of opposite sign. This has led to the terms "cosmological constant" and "vacuum energy" being used interchangeably in general relativity.

## Features

### Conservation of energy and momentum

General relativity is consistent with the local conservation of energy and momentum expressed as $\nabla _{\beta }T^{\alpha \beta }={T^{\alpha \beta }}_{;\beta }=0.$

Derivation of local energy–momentum conservation

Contracting the differential Bianchi identity $R_{\alpha \beta [\gamma \delta ;\varepsilon ]}=0$ with $g^{\alpha \beta }$ gives, using the fact that the metric tensor is covariantly constant, i.e. ${g^{\alpha \beta }}_{;\gamma }=0$ , ${R^{\gamma }}_{\beta \gamma \delta ;\varepsilon }+{R^{\gamma }}_{\beta \varepsilon \gamma ;\delta }+{R^{\gamma }}_{\beta \delta \varepsilon ;\gamma }=0$

The antisymmetry of the Riemann tensor allows the second term in the above expression to be rewritten: ${R^{\gamma }}_{\beta \gamma \delta ;\varepsilon }-{R^{\gamma }}_{\beta \gamma \varepsilon ;\delta }+{R^{\gamma }}_{\beta \delta \varepsilon ;\gamma }=0$ which is equivalent to $R_{\beta \delta ;\varepsilon }-R_{\beta \varepsilon ;\delta }+{R^{\gamma }}_{\beta \delta \varepsilon ;\gamma }=0$ using the definition of the Ricci tensor.

Next, contract again with the metric $g^{\beta \delta }\left(R_{\beta \delta ;\varepsilon }-R_{\beta \varepsilon ;\delta }+{R^{\gamma }}_{\beta \delta \varepsilon ;\gamma }\right)=0$ to get ${R^{\delta }}_{\delta ;\varepsilon }-{R^{\delta }}_{\varepsilon ;\delta }+{R^{\gamma \delta }}_{\delta \varepsilon ;\gamma }=0.$

The definitions of the Ricci curvature tensor and the scalar curvature then show that $R_{;\varepsilon }-2{R^{\gamma }}_{\varepsilon ;\gamma }=0,$ which can be rewritten as $\left({R^{\gamma }}_{\varepsilon }-{\tfrac {1}{2}}{g^{\gamma }}_{\varepsilon }R\right)_{;\gamma }=0.$

A final contraction with *g**εδ* gives $\left(R^{\gamma \delta }-{\tfrac {1}{2}}g^{\gamma \delta }R\right)_{;\gamma }=0,$ which by the symmetry of the bracketed term and the definition of the Einstein tensor, gives, after relabelling the indices, ${G^{\alpha \beta }}_{;\beta }=0.$

Using the EFE, this immediately gives, $\nabla _{\beta }T^{\alpha \beta }={T^{\alpha \beta }}_{;\beta }=0$

which expresses the local conservation of stress–energy. This conservation law is a physical requirement. With his field equations Einstein ensured that general relativity is consistent with this conservation condition.

### Nonlinearity

The nonlinearity of the EFE distinguishes general relativity from many other fundamental physical theories. For example, Maxwell's equations of electromagnetism are linear in the electric and magnetic fields, and charge and current distributions (i.e. the sum of two solutions is also a solution); another example is the Schrödinger equation of quantum mechanics, which is linear in the wavefunction.

### Correspondence principle

The EFE reduce to Newton's law of gravity by using both the weak-field approximation and the low-velocity approximation. The constant G appearing in the EFE is determined by making these two approximations.

Derivation of Newton's law of gravity

Newtonian gravitation can be written as the theory of a scalar field, $\Phi$ , which is the gravitational potential in joules per kilogram of the gravitational field $g=-\nabla \Phi$ , see Gauss's law for gravity $\nabla ^{2}\Phi \left({\vec {x}},t\right)=4\pi G\rho \left({\vec {x}},t\right)$ where $\rho$ is the mass density. The orbit of a free-falling particle satisfies ${\ddot {\vec {x}}}(t)={\vec {g}}=-\nabla \Phi \left({\vec {x}}(t),t\right)\,.$

In tensor notation, these become ${\begin{aligned}\Phi _{,ii}&=4\pi G\rho \\{\frac {d^{2}x^{i}}{dt^{2}}}&=-\Phi _{,i}\,.\end{aligned}}$

In general relativity, these equations are replaced by the Einstein field equations in the trace-reversed form $R_{\mu \nu }=K\left(T_{\mu \nu }-{\tfrac {1}{2}}Tg_{\mu \nu }\right)$ for some constant, K , and the geodesic equation ${\frac {d^{2}x^{\alpha }}{d\tau ^{2}}}=-\Gamma _{\beta \gamma }^{\alpha }{\frac {dx^{\beta }}{d\tau }}{\frac {dx^{\gamma }}{d\tau }}\,.$

To see how the latter reduces to the former, we assume that the test particle's velocity is approximately zero ${\frac {dx^{\beta }}{d\tau }}\approx \left({\frac {dt}{d\tau }},0,0,0\right)$ and thus ${\frac {d}{dt}}\left({\frac {dt}{d\tau }}\right)\approx 0$ and that the metric and its derivatives are approximately static and that the squares of deviations from the Minkowski metric are negligible. Applying these simplifying assumptions to the spatial components of the geodesic equation gives ${\frac {d^{2}x^{i}}{dt^{2}}}\approx -\Gamma _{00}^{i}$ where two factors of ${\textstyle {\frac {{\text{d}}t}{{\text{d}}\tau }}}$ have been divided out. This will reduce to its Newtonian counterpart, provided $\Phi _{,i}\approx \Gamma _{00}^{i}={\tfrac {1}{2}}g^{i\alpha }\left(g_{\alpha 0,0}+g_{0\alpha ,0}-g_{00,\alpha }\right)\,.$

Our assumptions force $\alpha =i$ and the time (0) derivatives to be zero. So this simplifies to $2\Phi _{,i}\approx g^{ij}\left(-g_{00,j}\right)\approx -g_{00,i}\,$ which is satisfied by letting $g_{00}\approx -c^{2}-2\Phi \,.$

Turning to the Einstein equations, we only need the time-time component $R_{00}=K\left(T_{00}-{\tfrac {1}{2}}Tg_{00}\right)$ the low speed and static field assumptions imply that $T_{\mu \nu }\approx \operatorname {diag} \left(T_{00},0,0,0\right)\approx \operatorname {diag} \left(\rho c^{4},0,0,0\right)\,.$

So $T=g^{\alpha \beta }T_{\alpha \beta }\approx g^{00}T_{00}\approx -{\frac {1}{c^{2}}}\rho c^{4}=-\rho c^{2}\,$ and thus $K\left(T_{00}-{\tfrac {1}{2}}Tg_{00}\right)\approx K\left(\rho c^{4}-{\tfrac {1}{2}}\left(-\rho c^{2}\right)\left(-c^{2}\right)\right)={\tfrac {1}{2}}K\rho c^{4}\,.$

From the definition of the Ricci tensor $R_{00}=\Gamma _{00,\rho }^{\rho }-\Gamma _{\rho 0,0}^{\rho }+\Gamma _{\rho \lambda }^{\rho }\Gamma _{00}^{\lambda }-\Gamma _{0\lambda }^{\rho }\Gamma _{\rho 0}^{\lambda }.$

Our simplifying assumptions make the squares of $\Gamma$ disappear together with the time derivatives $R_{00}\approx \Gamma _{00,i}^{i}\,.$

Combining the above equations together $\Phi _{,ii}\approx \Gamma _{00,i}^{i}\approx R_{00}=K\left(T_{00}-{\tfrac {1}{2}}Tg_{00}\right)\approx {\tfrac {1}{2}}K\rho c^{4}$ which reduces to the Newtonian field equation provided ${\tfrac {1}{2}}K\rho c^{4}=4\pi G\rho ,$ which will occur if $K={\frac {8\pi G}{c^{4}}}\,.$

## Vacuum field equations

If the energy–momentum tensor $T_{\mu \nu }$ is zero in the region under consideration, then the field equations are also referred to as the vacuum field equations. By setting $T_{\mu \nu }=0$ in the trace-reversed field equations, the vacuum field equations, also known as 'Einstein vacuum equations' (EVE), can be written as $R_{\mu \nu }=0\,.$

In the case of nonzero cosmological constant, the equations are $R_{\mu \nu }={\frac {\Lambda }{{\frac {D}{2}}-1}}g_{\mu \nu }\,.$

The solutions to the vacuum field equations are called vacuum solutions. Flat Minkowski space is the simplest example of a vacuum solution. Nontrivial examples include the Schwarzschild solution and the Kerr solution.

Manifolds with a vanishing Ricci tensor, $R_{\mu \nu }=0$ , are referred to as Ricci-flat manifolds and manifolds with a Ricci tensor proportional to the metric as Einstein manifolds.

## Einstein–Maxwell equations

If the energy–momentum tensor $T_{\mu \nu }$ is that of an electromagnetic field in free space, i.e. if the electromagnetic stress–energy tensor $T^{\alpha \beta }=\,-{\frac {1}{\mu _{0}}}\left({F^{\alpha }}^{\psi }{F_{\psi }}^{\beta }+{\tfrac {1}{4}}g^{\alpha \beta }F_{\psi \tau }F^{\psi \tau }\right)$ is used, then the Einstein field equations are called the *Einstein–Maxwell equations* (with cosmological constant $\Lambda$ , taken to be zero in conventional relativity theory): $G^{\alpha \beta }+\Lambda g^{\alpha \beta }={\frac {\kappa }{\mu _{0}}}\left({F^{\alpha }}^{\psi }{F_{\psi }}^{\beta }+{\tfrac {1}{4}}g^{\alpha \beta }F_{\psi \tau }F^{\psi \tau }\right).$

Additionally, the covariant Maxwell equations are also applicable in free space: ${\begin{aligned}{F^{\alpha \beta }}_{;\beta }&=0\\F_{[\alpha \beta ;\gamma ]}&={\tfrac {1}{3}}\left(F_{\alpha \beta ;\gamma }+F_{\beta \gamma ;\alpha }+F_{\gamma \alpha ;\beta }\right)={\tfrac {1}{3}}\left(F_{\alpha \beta ,\gamma }+F_{\beta \gamma ,\alpha }+F_{\gamma \alpha ,\beta }\right)=0,\end{aligned}}$ where the semicolon represents a covariant derivative, and the brackets denote anti-symmetrization. The first equation asserts that the 4-divergence of the 2-form F is zero, and the second that its exterior derivative is zero. From the latter, it follows by the Poincaré lemma that in a coordinate chart it is possible to introduce an electromagnetic field potential $A_{\alpha }$ such that $F_{\alpha \beta }=A_{\alpha ;\beta }-A_{\beta ;\alpha }=A_{\alpha ,\beta }-A_{\beta ,\alpha }$ in which the comma denotes a partial derivative. This is often taken as equivalent to the covariant Maxwell equation from which it is derived. However, there are global solutions of the equation that may lack a globally defined potential.

## Solutions

The solutions of the Einstein field equations are metrics of spacetime. These metrics describe the structure of the spacetime including the inertial motion of objects in the spacetime. As the field equations are non-linear, they cannot always be completely solved (i.e. without making approximations). For example, there is no known complete solution for a spacetime with two massive bodies in it (which is a theoretical model of a binary star system, for example). However, approximations are usually made in these cases. These are commonly referred to as post-Newtonian approximations. Even so, there are several cases where the field equations have been solved completely, and those are called exact solutions.

The study of exact solutions of Einstein's field equations is one of the activities of cosmology. It leads to the prediction of black holes and to different models of evolution of the universe.

One can also discover new solutions of the Einstein field equations via the method of orthonormal frames as pioneered by Ellis and MacCallum. In this approach, the Einstein field equations are reduced to a set of coupled, nonlinear, ordinary differential equations. As discussed by Hsu and Wainwright, self-similar solutions to the Einstein field equations are fixed points of the resulting dynamical system. New solutions have been discovered using these methods by LeBlanc and Kohli and Haslam.

## Linearized EFE

The nonlinearity of the EFE makes finding exact solutions difficult. One way of solving the field equations is to make an approximation, namely, that far from the source(s) of gravitating matter, the gravitational field is very weak and the spacetime approximates that of Minkowski space. The metric is then written as the sum of the Minkowski metric and a term representing the deviation of the true metric from the Minkowski metric, ignoring higher-power terms. This linearization procedure can be used to investigate the phenomena of gravitational radiation.

## Polynomial form

Despite the EFE as written containing the inverse of the metric tensor, they can be arranged in a form that contains the metric tensor in polynomial form and without its inverse. First, the determinant of the metric in 4 dimensions can be written $\det(g)={\tfrac {1}{24}}\varepsilon ^{\alpha \beta \gamma \delta }\varepsilon ^{\kappa \lambda \mu \nu }g_{\alpha \kappa }g_{\beta \lambda }g_{\gamma \mu }g_{\delta \nu }$ using the Levi-Civita symbol; and the inverse of the metric in 4 dimensions can be written as: $g^{\alpha \kappa }={\frac {{\tfrac {1}{6}}\varepsilon ^{\alpha \beta \gamma \delta }\varepsilon ^{\kappa \lambda \mu \nu }g_{\beta \lambda }g_{\gamma \mu }g_{\delta \nu }}{\det(g)}}\,.$

Substituting this expression of the inverse of the metric into the equations then multiplying both sides by a suitable power of $\det(g)$ to eliminate it from the denominator results in polynomial equations in the metric tensor and its first and second derivatives. The Einstein–Hilbert action from which the equations are derived can also be written in polynomial form by suitable redefinitions of the fields.
