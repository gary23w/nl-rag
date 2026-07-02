---
title: "Strain (mechanics)"
source: https://en.wikipedia.org/wiki/Strain_(mechanics)
domain: continuum-mechanics
license: CC-BY-SA-4.0
tags: continuum mechanics, stress tensor, constitutive equation, deformation gradient
fetched: 2026-07-02
---

# Strain (mechanics)

In mechanics, **strain** is defined as relative deformation, compared to a *reference* position configuration. Different equivalent choices may be made for the expression of a strain field depending on whether it is defined with respect to the initial or the final configuration of the body and on whether the metric tensor or its dual is considered.

Strain has dimension of a length ratio, with SI base units of meter per meter (m/m). Hence strains are dimensionless and are usually expressed as a decimal fraction or a percentage. Parts-per notation is also used, e.g., parts per million or parts per billion (sometimes called "microstrains" and "nanostrains", respectively), corresponding to μm/m and nm/m.

Strain can be formulated as the spatial derivative of displacement: ${\boldsymbol {\varepsilon }}\doteq {\cfrac {\partial }{\partial \mathbf {X} }}\left(\mathbf {x} -\mathbf {X} \right)={\boldsymbol {F}}'-{\boldsymbol {I}},$ where **I** is the identity tensor. The displacement of a body may be expressed in the form **x** = ***F***(**X**), where **X** is the reference position of material points of the body; displacement has units of length and does not distinguish between rigid body motions (translations and rotations) and deformations (changes in shape and size) of the body. The spatial derivative of a uniform translation is zero, thus strains measure how much a given displacement differs locally from a rigid-body motion.

A strain is in general a tensor quantity. Physical insight into strains can be gained by observing that a given strain can be decomposed into normal and shear components. The amount of stretch or compression along material line elements or fibers is the *normal strain*, and the amount of distortion associated with the sliding of plane layers over each other is the *shear strain*, within a deforming body. This could be applied by elongation, shortening, or volume changes, or angular distortion.

The state of strain at a material point of a continuum body is defined as the totality of all the changes in length of material lines or fibers, the *normal strain*, which pass through that point and also the totality of all the changes in the angle between pairs of lines initially perpendicular to each other, the *shear strain*, radiating from this point. However, it is sufficient to know the normal and shear components of strain on a set of three mutually perpendicular directions.

If there is an increase in length of the material line, the normal strain is called *tensile strain*; otherwise, if there is reduction or compression in the length of the material line, it is called *compressive strain*.

## Strain regimes

Depending on the amount of strain, or local deformation, the analysis of deformation is subdivided into three deformation theories:

- Finite strain theory, also called *large strain theory*, *large deformation theory*, deals with deformations in which both rotations and strains are arbitrarily large. In this case, the undeformed and deformed configurations of the continuum are significantly different and a clear distinction has to be made between them. This is commonly the case with elastomers, plastically-deforming materials and other fluids and biological soft tissue.
- Infinitesimal strain theory, also called *small strain theory*, *small deformation theory*, *small displacement theory*, or *small displacement-gradient theory* where strains and rotations are both small. In this case, the undeformed and deformed configurations of the body can be assumed identical. The infinitesimal strain theory is used in the analysis of deformations of materials exhibiting elastic behavior, such as materials found in mechanical and civil engineering applications, e.g. concrete and steel.
- *Large-displacement* or *large-rotation theory*, which assumes small strains but large rotations and displacements.

## Strain measures

In each of these theories the strain is then defined differently. The *engineering strain* is the most common definition applied to materials used in mechanical and structural engineering, which are subjected to very small deformations. On the other hand, for some materials, e.g., elastomers and polymers, subjected to large deformations, the engineering definition of strain is not applicable, e.g. typical engineering strains greater than 1%; thus other more complex definitions of strain are required, such as *stretch*, *logarithmic strain*, *Green strain*, and *Almansi strain*.

### Engineering strain

**Engineering strain**, also known as **Cauchy strain**, is expressed as the ratio of total deformation to the initial dimension of the material body on which forces are applied. In the case of a material line element or fiber axially loaded, its elongation gives rise to an *engineering normal strain* or *engineering extensional strain* e, which equals the *relative elongation* or the change in length Δ*L* per unit of the original length L of the line element or fibers (in meters per meter). The normal strain is positive if the material fibers are stretched and negative if they are compressed. Thus, we have $e={\frac {\Delta L}{L}}={\frac {l-L}{L}}$ , where e is the *engineering normal strain*, L is the original length of the fiber and l is the final length of the fiber.

The *true shear strain* is defined as the change in the angle (in radians) between two material line elements initially perpendicular to each other in the undeformed or initial configuration. The *engineering shear strain* is defined as the tangent of that angle, and is equal to the length of deformation at its maximum divided by the perpendicular length in the plane of force application, which sometimes makes it easier to calculate.

### Stretch ratio

The **stretch ratio** or **extension ratio** (symbol λ) is an alternative measure related to the extensional or normal strain of an axially loaded differential line element. It is defined as the ratio between the final length l and the initial length L of the material line. $\lambda ={\frac {l}{L}}$

The extension ratio λ is related to the engineering strain *e* by $e=\lambda -1$ This equation implies that when the normal strain is zero, so that there is no deformation, the stretch ratio is equal to unity.

The stretch ratio is used in the analysis of materials that exhibit large deformations, such as elastomers, which can sustain stretch ratios of 3 or 4 before they fail. On the other hand, traditional engineering materials, such as concrete or steel, fail at much lower stretch ratios.

### Logarithmic strain

The **logarithmic strain** ε, also called, *true strain* or *Hencky strain*. Considering an incremental strain (Ludwik) $\delta \varepsilon ={\frac {\delta l}{l}}$ the logarithmic strain is obtained by integrating this incremental strain: ${\begin{aligned}\int \delta \varepsilon &=\int _{L}^{l}{\frac {\delta l}{l}}\\\varepsilon &=\ln \left({\frac {l}{L}}\right)=\ln(\lambda )\\&=\ln(1+e)\\&=e-{\frac {e^{2}}{2}}+{\frac {e^{3}}{3}}-\cdots \end{aligned}}$ where e is the engineering strain. The logarithmic strain provides the correct measure of the final strain when deformation takes place in a series of increments, taking into account the influence of the strain path.

### Green strain

The Green strain is defined as: $\varepsilon _{G}={\tfrac {1}{2}}\left({\frac {l^{2}-L^{2}}{L^{2}}}\right)={\tfrac {1}{2}}(\lambda ^{2}-1)$

### Almansi strain

The Euler-Almansi strain is defined as $\varepsilon _{E}={\tfrac {1}{2}}\left({\frac {l^{2}-L^{2}}{l^{2}}}\right)={\tfrac {1}{2}}\left(1-{\frac {1}{\lambda ^{2}}}\right)$

## Strain tensor

The (infinitesimal) **strain tensor** (symbol ${\boldsymbol {\varepsilon }}$ ) is defined in the International System of Quantities (ISQ), more specifically in ISO 80000-4 (Mechanics), as a "tensor quantity representing the deformation of matter caused by stress. Strain tensor is symmetric and has three linear strain and three shear strain (Cartesian) components." ISO 80000-4 further defines **linear strain** as the "quotient of change in length of an object and its length" and **shear strain** as the "quotient of parallel displacement of two surfaces of a layer and the thickness of the layer". Thus, strains are classified as either *normal* or *shear*. A *normal strain* is perpendicular to the face of an element, and a *shear strain* is parallel to it. These definitions are consistent with those of normal stress and shear stress.

The strain tensor can then be expressed in terms of normal and shear components as: ${\underline {\underline {\boldsymbol {\varepsilon }}}}={\begin{bmatrix}\varepsilon _{xx}&\varepsilon _{xy}&\varepsilon _{xz}\\\varepsilon _{yx}&\varepsilon _{yy}&\varepsilon _{yz}\\\varepsilon _{zx}&\varepsilon _{zy}&\varepsilon _{zz}\\\end{bmatrix}}={\begin{bmatrix}\varepsilon _{xx}&{\tfrac {1}{2}}\gamma _{xy}&{\tfrac {1}{2}}\gamma _{xz}\\{\tfrac {1}{2}}\gamma _{yx}&\varepsilon _{yy}&{\tfrac {1}{2}}\gamma _{yz}\\{\tfrac {1}{2}}\gamma _{zx}&{\tfrac {1}{2}}\gamma _{zy}&\varepsilon _{zz}\\\end{bmatrix}}$

### Geometric setting

Consider a two-dimensional, infinitesimal, rectangular material element with dimensions *dx* × *dy*, which, after deformation, takes the form of a rhombus. The deformation is described by the displacement field **u**. From the geometry of the adjacent figure we have $\mathrm {length} (AB)=dx$ and ${\begin{aligned}\mathrm {length} (ab)&={\sqrt {\left(dx+{\frac {\partial u_{x}}{\partial x}}dx\right)^{2}+\left({\frac {\partial u_{y}}{\partial x}}dx\right)^{2}}}\\&={\sqrt {dx^{2}\left(1+{\frac {\partial u_{x}}{\partial x}}\right)^{2}+dx^{2}\left({\frac {\partial u_{y}}{\partial x}}\right)^{2}}}\\&=dx~{\sqrt {\left(1+{\frac {\partial u_{x}}{\partial x}}\right)^{2}+\left({\frac {\partial u_{y}}{\partial x}}\right)^{2}}}\end{aligned}}$ For very small displacement gradients the squares of the derivative of $u_{y}$ and $u_{x}$ are negligible and we have $\mathrm {length} (ab)\approx dx\left(1+{\frac {\partial u_{x}}{\partial x}}\right)=dx+{\frac {\partial u_{x}}{\partial x}}dx$

### Normal strain

For an isotropic material that obeys Hooke's law, a normal stress will cause a normal strain. Normal strains produce *dilations*.

The normal strain in the x-direction of the rectangular element is defined by $\varepsilon _{x}={\frac {\text{extension}}{\text{original length}}}={\frac {\mathrm {length} (ab)-\mathrm {length} (AB)}{\mathrm {length} (AB)}}={\frac {\partial u_{x}}{\partial x}}$ Similarly, the normal strain in the y- and z-directions becomes $\varepsilon _{y}={\frac {\partial u_{y}}{\partial y}}\quad ,\qquad \varepsilon _{z}={\frac {\partial u_{z}}{\partial z}}$

### Shear strain

The engineering shear strain (*γxy*) is defined as the change in angle between lines *AC* and *AB*. Therefore, $\gamma _{xy}=\alpha +\beta$

From the geometry of the figure, we have ${\begin{aligned}\tan \alpha &={\frac {{\tfrac {\partial u_{y}}{\partial x}}dx}{dx+{\tfrac {\partial u_{x}}{\partial x}}dx}}={\frac {\tfrac {\partial u_{y}}{\partial x}}{1+{\tfrac {\partial u_{x}}{\partial x}}}}\\\tan \beta &={\frac {{\tfrac {\partial u_{x}}{\partial y}}dy}{dy+{\tfrac {\partial u_{y}}{\partial y}}dy}}={\frac {\tfrac {\partial u_{x}}{\partial y}}{1+{\tfrac {\partial u_{y}}{\partial y}}}}\end{aligned}}$ For small displacement gradients we have ${\frac {\partial u_{x}}{\partial x}}\ll 1~;~~{\frac {\partial u_{y}}{\partial y}}\ll 1$ For small rotations, i.e. α and β are ≪ 1 we have tan *α* ≈ *α*, tan *β* ≈ *β*. Therefore, $\alpha \approx {\frac {\partial u_{y}}{\partial x}}~;~~\beta \approx {\frac {\partial u_{x}}{\partial y}}$ thus $\gamma _{xy}=\alpha +\beta ={\frac {\partial u_{y}}{\partial x}}+{\frac {\partial u_{x}}{\partial y}}$ By interchanging x and y and *ux* and *uy*, it can be shown that *γxy* = *γyx*.

Similarly, for the yz- and xz-planes, we have $\gamma _{yz}=\gamma _{zy}={\frac {\partial u_{y}}{\partial z}}+{\frac {\partial u_{z}}{\partial y}}\quad ,\qquad \gamma _{zx}=\gamma _{xz}={\frac {\partial u_{z}}{\partial x}}+{\frac {\partial u_{x}}{\partial z}}$

### Volume strain

The volumetric strain, also called bulk strain, is the relative variation of the volume, as arising from *dilation* or *compression*; it is the first strain invariant or trace of the tensor: $\delta ={\frac {\Delta V}{V_{0}}}=I_{1}=\varepsilon _{11}+\varepsilon _{22}+\varepsilon _{33}$ Actually, if we consider a cube with an edge length *a*, it is a quasi-cube after the deformation (the variations of the angles do not change the volume) with the dimensions $a\cdot (1+\varepsilon _{11})\times a\cdot (1+\varepsilon _{22})\times a\cdot (1+\varepsilon _{33})$ and *V*0 = *a*3, thus ${\frac {\Delta V}{V_{0}}}={\frac {\left(1+\varepsilon _{11}+\varepsilon _{22}+\varepsilon _{33}+\varepsilon _{11}\cdot \varepsilon _{22}+\varepsilon _{11}\cdot \varepsilon _{33}+\varepsilon _{22}\cdot \varepsilon _{33}+\varepsilon _{11}\cdot \varepsilon _{22}\cdot \varepsilon _{33}\right)\cdot a^{3}-a^{3}}{a^{3}}}$ as we consider small deformations, $1\gg \varepsilon _{ii}\gg \varepsilon _{ii}\cdot \varepsilon _{jj}\gg \varepsilon _{11}\cdot \varepsilon _{22}\cdot \varepsilon _{33}$ therefore the formula.

(Real variation of volume (top) and the approximated one (bottom): the green drawing shows the estimated volume and the orange drawing the neglected volume)

In case of pure shear, we can see that there is no change of the volume.

## Metric tensor

A strain field associated with a displacement is defined, at any point, by the change in length of the tangent vectors representing the speeds of arbitrarily parametrized curves passing through that point. A basic geometric result, due to Fréchet, von Neumann and Jordan, states that, if the lengths of the tangent vectors fulfil the axioms of a norm and the parallelogram law, then the length of a vector is the square root of the value of the quadratic form associated, by the polarization formula, with a positive definite bilinear map called the metric tensor.
