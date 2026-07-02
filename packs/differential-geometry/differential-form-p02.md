---
title: "Differential form (part 2/2)"
source: https://en.wikipedia.org/wiki/Differential_form
domain: differential-geometry
license: CC-BY-SA-4.0
tags: differential geometry, smooth manifold, riemannian manifold, curvature tensor
fetched: 2026-07-02
part: 2/2
---

## Applications in physics

Differential forms arise in some important physical contexts. For example, in Maxwell's theory of electromagnetism, the **Faraday 2-form**, or electromagnetic field strength, is $\mathbf {F} ={\frac {1}{2}}f_{ab}\,dx^{a}\wedge dx^{b}\,,$ where the $f_{ab}$ are formed from the electromagnetic fields ${\vec {E}}$ and ${\vec {B}}$ ; e.g., $f_{12}=E_{z}/c$ , $f_{23}=-B_{z}$ , or equivalent definitions.

This form is a special case of the curvature form on the U(1) principal bundle on which both electromagnetism and general gauge theories may be described. The connection form for the principal bundle is the vector potential, typically denoted by $\mathbf {A}$ , when represented in some gauge. One then has $\mathbf {F} =d\mathbf {A} .$

The **current 3-form** is $\mathbf {J} ={\frac {1}{6}}j^{a}\,\varepsilon _{abcd}\,dx^{b}\wedge dx^{c}\wedge dx^{d}\,,$ where $j^{a}$ are the four components of the current density. (Here it is a matter of convention to write $F_{ab}$ instead of $f_{ab}$ , i.e. to use capital letters, and to write $J^{a}$ instead of $j_{a}$ . However, the vector rsp. tensor components and the above-mentioned forms have different physical dimensions. Moreover, by decision of an international commission of the International Union of Pure and Applied Physics, the magnetic polarization vector has been called ${\vec {J}}$ for several decades, and by some publishers $\mathbf {J}$ ; i.e., the same name is used for different quantities.)

Using the above-mentioned definitions, Maxwell's equations can be written very compactly in geometrized units as ${\begin{aligned}d{\mathbf {F} }&=\mathbf {0} \\d{\star \mathbf {F} }&=\mathbf {J} ,\end{aligned}}$ where $\star$ denotes the Hodge star operator. Similar considerations describe the geometry of gauge theories in general.

The 2 -form ${\star }\mathbf {F}$ , which is dual to the Faraday form, is also called **Maxwell 2-form**.

Electromagnetism is an example of a U(1) gauge theory. Here the Lie group is ${\text{U}}(1)$ , the one-dimensional unitary group, which is in particular abelian. There are gauge theories, such as Yang–Mills theory, in which the Lie group is not abelian. In that case, one gets relations which are similar to those described here. The analog of the field $\mathbf {F}$ in such theories is the curvature form of the connection, which is represented in a gauge by a Lie algebra-valued one-form $\mathbf {A}$ . The Yang–Mills field $\mathbf {F}$ is then defined by $\mathbf {F} =d\mathbf {A} +\mathbf {A} \wedge \mathbf {A} .$

In the abelian case, such as electromagnetism, $\mathbf {A} \wedge \mathbf {A} =0$ , but this does not hold in general. Likewise the field equations are modified by additional terms involving exterior products of $\mathbf {A}$ and $\mathbf {F}$ , owing to the structure equations of the gauge group.


## Applications in geometric measure theory

Numerous minimality results for complex analytic manifolds are based on the Wirtinger inequality for 2-forms. A succinct proof may be found in Herbert Federer's classic text *Geometric Measure Theory*. The Wirtinger inequality is also a key ingredient in Gromov's inequality for complex projective space in systolic geometry.
