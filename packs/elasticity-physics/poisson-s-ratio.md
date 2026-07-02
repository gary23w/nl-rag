---
title: "Poisson's ratio"
source: https://en.wikipedia.org/wiki/Poisson's_ratio
domain: elasticity-physics
license: CC-BY-SA-4.0
tags: elasticity theory, hooke's law, young's modulus, shear modulus
fetched: 2026-07-02
---

# Poisson's ratio

In materials science and solid mechanics, **Poisson's ratio** (symbol: **ν** (nu)) is a measure of the **Poisson effect**, the deformation (expansion or contraction) of a material in directions perpendicular to the specific direction of loading. The value of Poisson's ratio is the negative of the ratio of transverse strain to axial strain. For small values of these changes, ν is the amount of transversal elongation divided by the amount of axial compression.

Most materials have Poisson's ratio values ranging between 0.0 and 0.5. For soft materials, such as rubber, where the bulk modulus is much higher than the shear modulus, Poisson's ratio is near 0.5. For open-cell polymer foams, Poisson's ratio is near zero, since the cells tend to collapse in compression. Many typical solids have Poisson's ratios in the range of 0.2 to 0.3.

The ratio is named after the French mathematician and physicist Siméon Poisson.

## Definition

Assuming that the material is stretched or compressed in only one direction (the x or y axis in the diagram):

$\nu =-{\frac {d\varepsilon _{\mathrm {trans} }}{d\varepsilon _{\mathrm {axial} }}}=-{\frac {d\varepsilon _{\mathrm {y} }}{d\varepsilon _{\mathrm {x} }}}=-{\frac {d\varepsilon _{\mathrm {z} }}{d\varepsilon _{\mathrm {x} }}}$

where

- ν is the resulting Poisson's ratio,
- *ε*trans is transverse strain
- *ε*axial is axial strain

and positive strain indicates extension and negative strain indicates contraction.

## Origin

Poisson's ratio is a measure of the Poisson effect, the phenomenon in which a material tends to expand in directions perpendicular to the direction of compression. Conversely, if the material is stretched rather than compressed, it usually tends to contract in the directions transverse to the direction of stretching. It is a common observation when a rubber band is stretched, it becomes noticeably thinner. Again, the Poisson ratio will be the ratio of relative contraction to relative expansion and will have the same value as above. In certain rare cases, a material will actually shrink in the transverse direction when compressed (or expand when stretched), which will yield a negative value of the Poisson ratio.

The Poisson's ratio of a stable, isotropic, linear elastic material must be between −1.0 and +0.5 because of the requirement for Young's modulus, the shear modulus and bulk modulus to have positive values. Most materials have Poisson's ratio values ranging between 0.0 and 0.5. A perfectly incompressible isotropic material deformed elastically at small strains would have a Poisson's ratio of exactly 0.5. Most steels and rigid polymers when used within their design limits (before yield) exhibit values of about 0.3, increasing to 0.5 for post-yield deformation which occurs largely at constant volume. Rubber has a Poisson ratio of nearly 0.5. Cork's Poisson ratio is close to 0, showing very little lateral expansion when compressed. Glass is between 0.18 and 0.30. Some materials, e.g. some polymer foams, origami folds, and certain cells can exhibit negative Poisson's ratio, and are referred to as auxetic materials. If these auxetic materials are stretched in one direction, they become thicker in the perpendicular direction. In contrast, some anisotropic materials, such as carbon nanotubes, zigzag-based folded sheet materials, and honeycomb auxetic metamaterials to name a few, can exhibit one or more Poisson's ratios above 0.5 in certain directions.

## Changing geometry

### Length change

For a cube stretched in the x-direction (see Figure 1) with a length increase of Δ*L* in the x-direction, and a length decrease of Δ*L*′ in the y- and z-directions, the infinitesimal diagonal strains are given by

$d\varepsilon _{x}={\frac {dx}{x}},\qquad d\varepsilon _{y}={\frac {dy}{y}},\qquad d\varepsilon _{z}={\frac {dz}{z}}.$

If Poisson's ratio is constant through deformation, integrating these expressions and using the definition of Poisson's ratio gives

$-\nu \int _{L}^{L+\Delta L}{\frac {dx}{x}}=\int _{L}^{L+\Delta L'}{\frac {dy}{y}}=\int _{L}^{L+\Delta L'}{\frac {dz}{z}}.$

Solving and exponentiating, the relationship between Δ*L* and Δ*L*′ is then

$\left(1+{\frac {\Delta L}{L}}\right)^{-\nu }=1+{\frac {\Delta L'}{L}}.$

For very small values of Δ*L* and Δ*L*′, the first-order approximation yields:

$\nu \approx -{\frac {\Delta L'}{\Delta L}}.$

### Volumetric change

The relative change of volume ⁠Δ*V*/*V*⁠ of a cube due to the stretch of the material can now be calculated. Since *V* = *L*3 and

$V+\Delta V=(L+\Delta L)\left(L+\Delta L'\right)^{2}$

one can derive

${\frac {\Delta V}{V}}=\left(1+{\frac {\Delta L}{L}}\right)\left(1+{\frac {\Delta L'}{L}}\right)^{2}-1$

Using the above derived relationship between Δ*L* and Δ*L*′:

${\frac {\Delta V}{V}}=\left(1+{\frac {\Delta L}{L}}\right)^{1-2\nu }-1$

and for very small values of Δ*L* and Δ*L*′, the first-order approximation yields:

${\frac {\Delta V}{V}}\approx (1-2\nu ){\frac {\Delta L}{L}}$

For isotropic materials we can use Lamé's relation

$\nu \approx {\frac {1}{2}}-{\frac {E}{6K}}$

where K is bulk modulus and E is Young's modulus.

### Width change

If a rod with diameter (or width, or thickness) d and length L is subject to tension so that its length will change by Δ*L* then its diameter d will change by:

${\frac {\Delta d}{d}}=-\nu {\frac {\Delta L}{L}}$

The above formula is true only in the case of small deformations; if deformations are large then the following (more precise) formula can be used:

$\Delta d=-d\left(1-{\left(1+{\frac {\Delta L}{L}}\right)}^{-\nu }\right)$

where

- d is original diameter
- Δ*d* is rod diameter change
- ν is Poisson's ratio
- L is original length, before stretch
- Δ*L* is the change of length.

The value is negative because it decreases with increase of length

## Characteristic materials

### Isotropic

For a linear isotropic material subjected only to compressive (i.e. normal) forces, the deformation of a material in the direction of one axis will produce a deformation of the material along the other axis in three dimensions. Thus it is possible to generalize Hooke's law (for compressive forces) into three dimensions:

${\begin{aligned}\varepsilon _{xx}&={\frac {1}{E}}\left[\sigma _{xx}-\nu \left(\sigma _{yy}+\sigma _{zz}\right)\right]\\[6px]\varepsilon _{yy}&={\frac {1}{E}}\left[\sigma _{yy}-\nu \left(\sigma _{zz}+\sigma _{xx}\right)\right]\\[6px]\varepsilon _{zz}&={\frac {1}{E}}\left[\sigma _{zz}-\nu \left(\sigma _{xx}+\sigma _{yy}\right)\right]\end{aligned}}$

where:

- *ε**xx*, *ε**yy*, and *ε**zz* are strain in the direction of x, y and z
- *σ**xx*, *σ**yy*, and *σ**zz* are stress in the direction of x, y and z
- E is Young's modulus (the same in all directions for isotropic materials)
- ν is Poisson's ratio (the same in all directions for isotropic materials)

these equations can be all synthesized in the following:

$\varepsilon _{ii}={\frac {1}{E}}\left[\sigma _{ii}(1+\nu )-\nu \sum _{k}\sigma _{kk}\right]$

In the most general case, also shear stresses will hold as well as normal stresses, and the full generalization of Hooke's law is given by:

$\varepsilon _{ij}={\frac {1}{E}}\left[\sigma _{ij}(1+\nu )-\nu \delta _{ij}\sum _{k}\sigma _{kk}\right]$

where *δ**ij* is the Kronecker delta. The Einstein notation is usually adopted:

$\sigma _{kk}\equiv \sum _{l}\delta _{kl}\sigma _{kl}$

to write the equation simply as:

$\varepsilon _{ij}={\frac {1}{E}}\left[\sigma _{ij}(1+\nu )-\nu \delta _{ij}\sigma _{kk}\right]$

### Anisotropic

For anisotropic materials, the Poisson ratio depends on the direction of extension and transverse deformation

${\begin{aligned}\nu (\mathbf {n} ,\mathbf {m} )&=-E\left(\mathbf {n} \right)s_{ij\alpha \beta }n_{i}n_{j}m_{\alpha }m_{\beta }\\[4px]E^{-1}(\mathbf {n} )&=s_{ij\alpha \beta }n_{i}n_{j}n_{\alpha }n_{\beta }\end{aligned}}$

Here ν is Poisson's ratio, E is Young's modulus, **n** is a unit vector directed along the direction of extension, **m** is a unit vector directed perpendicular to the direction of extension. Poisson's ratio has a different number of special directions depending on the type of anisotropy.

### Orthotropic

Orthotropic materials have three mutually perpendicular planes of symmetry in their material properties. An example is wood, which is most stiff (and strong) along the grain, and less so in the other directions.

Then Hooke's law can be expressed in matrix form as

${\begin{bmatrix}\epsilon _{xx}\\\epsilon _{yy}\\\epsilon _{zz}\\2\epsilon _{yz}\\2\epsilon _{zx}\\2\epsilon _{xy}\end{bmatrix}}={\begin{bmatrix}{\tfrac {1}{E_{x}}}&-{\tfrac {\nu _{yx}}{E_{y}}}&-{\tfrac {\nu _{zx}}{E_{z}}}&0&0&0\\-{\tfrac {\nu _{xy}}{E_{x}}}&{\tfrac {1}{E_{y}}}&-{\tfrac {\nu _{zy}}{E_{z}}}&0&0&0\\-{\tfrac {\nu _{xz}}{E_{x}}}&-{\tfrac {\nu _{yz}}{E_{y}}}&{\tfrac {1}{E_{z}}}&0&0&0\\0&0&0&{\tfrac {1}{G_{yz}}}&0&0\\0&0&0&0&{\tfrac {1}{G_{zx}}}&0\\0&0&0&0&0&{\tfrac {1}{G_{xy}}}\\\end{bmatrix}}{\begin{bmatrix}\sigma _{xx}\\\sigma _{yy}\\\sigma _{zz}\\\sigma _{yz}\\\sigma _{zx}\\\sigma _{xy}\end{bmatrix}}$

where

- *E**i* is the Young's modulus along axis i
- *G**ij* is the shear modulus in direction j on the plane whose normal is in direction i
- *ν**ij* is the Poisson ratio that corresponds to a contraction in direction j when an extension is applied in direction i.

The Poisson ratio of an orthotropic material is different in each direction (x, y and z). However, the symmetry of the stress and strain tensors implies that not all the six Poisson's ratios in the equation are independent. There are only nine independent material properties: three elastic moduli, three shear moduli, and three Poisson's ratios. The remaining three Poisson's ratios can be obtained from the relations

${\frac {\nu _{yx}}{E_{y}}}={\frac {\nu _{xy}}{E_{x}}}\,,\qquad {\frac {\nu _{zx}}{E_{z}}}={\frac {\nu _{xz}}{E_{x}}}\,,\qquad {\frac {\nu _{yz}}{E_{y}}}={\frac {\nu _{zy}}{E_{z}}}$

From the above relations we can see that if *E**x* > *E**y* then *ν**xy* > *ν**yx*. The larger ratio (in this case *ν**xy*) is called the **major Poisson ratio** while the smaller one (in this case *ν**yx*) is called the **minor Poisson ratio**. We can find similar relations between the other Poisson ratios.

### Transversely isotropic

Transversely isotropic materials have a plane of isotropy in which the elastic properties are isotropic. If we assume that this plane of isotropy is the yz-plane, then Hooke's law takes the form

${\begin{bmatrix}\epsilon _{xx}\\\epsilon _{yy}\\\epsilon _{zz}\\2\epsilon _{yz}\\2\epsilon _{zx}\\2\epsilon _{xy}\end{bmatrix}}={\begin{bmatrix}{\tfrac {1}{E_{x}}}&-{\tfrac {\nu _{yx}}{E_{y}}}&-{\tfrac {\nu _{zx}}{E_{z}}}&0&0&0\\-{\tfrac {\nu _{xy}}{E_{x}}}&{\tfrac {1}{E_{y}}}&-{\tfrac {\nu _{zy}}{E_{z}}}&0&0&0\\-{\tfrac {\nu _{xz}}{E_{x}}}&-{\tfrac {\nu _{yz}}{E_{y}}}&{\tfrac {1}{E_{z}}}&0&0&0\\0&0&0&{\tfrac {1}{G_{\rm {yz}}}}&0&0\\0&0&0&0&{\tfrac {1}{G_{\rm {zx}}}}&0\\0&0&0&0&0&{\tfrac {1}{G_{\rm {xy}}}}\\\end{bmatrix}}{\begin{bmatrix}\sigma _{xx}\\\sigma _{yy}\\\sigma _{zz}\\\sigma _{yz}\\\sigma _{zx}\\\sigma _{xy}\end{bmatrix}}$

where we have used the yz-plane of isotropy to reduce the number of constants, that is,

$E_{y}=E_{z},\qquad \nu _{xy}=\nu _{xz},\qquad \nu _{yx}=\nu _{zx}.$

.

The symmetry of the stress and strain tensors implies that

${\frac {\nu _{xy}}{E_{x}}}={\frac {\nu _{yx}}{E_{y}}},\qquad \nu _{yz}=\nu _{zy}.$

This leaves us with six independent constants *E**x*, *E**y*, *G**xy*, *G**yz*, *ν**xy*, *ν**yz*. However, transverse isotropy gives rise to a further constraint between *G**yz* and *E**y*, *ν**yz* which is

$G_{yz}={\frac {E_{y}}{2\left(1+\nu _{yz}\right)}}.$

Therefore, there are five independent elastic material properties, two of which are Poisson's ratios. For the assumed plane of symmetry, the larger of *ν**xy* and *ν**yx* is the major Poisson ratio. The other major and minor Poisson ratios are equal.

## Values for different materials

| Material | Poisson's ratio |
|---|---|
| rubber | 0.4999 |
| gold | 0.42-0.44 (0.43) |
| saturated clay | 0.40-0.49 (0.45) |
| magnesium | 0.252-0.289 (0.271) |
| titanium | 0.265-0.34 (0.303) |
| copper | 0.33 |
| aluminium alloy | 0.32 |
| clay | 0.30-0.45 (0.38) |
| stainless steel | 0.30-0.31 (0.31) |
| steel | 0.27-0.30 (0.29) |
| cast iron | 0.21-0.26 (0.24) |
| sand | 0.20-0.455 (0.328) |
| concrete | 0.1-0.2 (0.2) |
| glass | 0.18-0.3 (0.24) |
| metallic glasses | 0.276-0.409 (0.343) |
| foam | 0.10-0.50 (0.3) |
| cork | 0.0 |

| Material | Plane of symmetry | *ν**xy* | *ν**yx* | *ν**yz* | *ν**zy* | *ν**zx* | *ν**xz* |
|---|---|---|---|---|---|---|---|
| Nomex honeycomb core | xy, ribbon in x direction | 0.49 | 0.69 | 0.01 | 2.75 | 3.88 | 0.01 |
| glass fiber epoxy resin | xy | 0.29 | 0.32 | 0.06 | 0.06 | 0.32 |   |

| Material | Poisson's ratio |
|---|---|
| aluminium | 0.35 |
| beryllium | 0.032 |
| bismuth | 0.33 |
| cadmium | 0.30 |
| calcium | 0.31 |
| cerium | 0.24 |
| chromium | 0.21 |
| cobalt | 0.31 |
| copper | 0.34 |
| dysprosium | 0.25 |
| erbium | 0.24 |
| europium | 0.15 |
| gadolinium | 0.26 |
| gold | 0.44 |
| hafnium | 0.37 |
| holmium | 0.23 |
| iridium | 0.26 |
| iron | 0.29 |
| lanthanum | 0.28 |
| lead | 0.44 |
| lutetium | 0.26 |
| magnesium | 0.29 |
| molybdenum | 0.31 |
| neodymium | 0.28 |
| nickel | 0.31 |
| niobium | 0.40 |
| osmium | 0.25 |
| palladium | 0.39 |
| platinum | 0.38 |
| plutonium | 0.21 |
| praseodymium | 0.28 |
| promethium | 0.28 |
| rhenium | 0.30 |
| rhodium | 0.26 |
| ruthenium | 0.30 |
| samarium | 0.27 |
| scandium | 0.28 |
| selenium | 0.33 |
| silver | 0.37 |
| strontium | 0.28 |
| tantalum | 0.34 |
| terbium | 0.26 |
| thallium | 0.45 |
| thorium | 0.27 |
| thulium | 0.21 |
| tin | 0.36 |
| titanium | 0.32 |
| tungsten | 0.28 |
| uranium | 0.23 |
| vanadium | 0.37 |
| ytterbium | 0.21 |
| yttrium | 0.24 |
| zinc | 0.25 |
| zirconium | 0.34 |

### Negative Poisson's ratio materials

Some materials, known as auxetic, display a negative Poisson's ratio. When subjected to positive strain in a longitudinal axis, the transverse strain in the material will actually be positive (i.e. it will increase the cross sectional area). For these materials, it is usually due to uniquely oriented, hinged molecular bonds. In order for these bonds to stretch in the longitudinal direction, the hinges must 'open' in the transverse direction, effectively exhibiting a positive strain. This can also be done in a structured way and lead to new aspects in material design, such as for mechanical metamaterials.

Studies have shown that certain solid wood types display negative Poisson's ratio exclusively during a compression creep test. Initially, the compression creep test shows positive Poisson's ratios, but gradually decreases until it reaches negative values. Consequently, this also shows that Poisson's ratio for wood is time-dependent during constant loading, meaning that the strain in the axial and transverse direction do not increase in the same rate.

Media with engineered microstructure may exhibit negative Poisson's ratio. In a simple case auxeticity is obtained removing material and creating a periodic porous media. Lattices can reach lower values of Poisson's ratio, which can be indefinitely close to the limiting value −1 in the isotropic case.

More than three hundred crystalline materials have negative Poisson's ratio. For example, Li, Na, K, Cu, Rb, Ag, Fe, Ni, Co, Cs, Au, Be, Ca, Zn Sr, Sb, MoS2 and others.

## Poisson function

At finite strains, the relationship between the transverse and axial strains *ε*trans and *ε*axial is typically not well described by the Poisson ratio. In fact, the Poisson ratio is often considered a function of the applied strain in the large strain regime. In such instances, the Poisson ratio is replaced by the Poisson function, for which there are several competing definitions. Defining the transverse stretch *λ*trans = *ε*trans + 1 and axial stretch *λ*axial = *ε*axial + 1, where the transverse stretch is a function of the axial stretch, the most common are the Hencky, Biot, Green, and Almansi functions:

${\begin{aligned}\nu ^{\text{Hencky}}&=-{\frac {\ln \lambda _{\text{trans}}}{\ln \lambda _{\text{axial}}}}\\[6pt]\nu ^{\text{Biot}}&={\frac {1-\lambda _{\text{trans}}}{\lambda _{\text{axial}}-1}}\\[6pt]\nu ^{\text{Green}}&={\frac {1-\lambda _{\text{trans}}^{2}}{\lambda _{\text{axial}}^{2}-1}}\\[6pt]\nu ^{\text{Almansi}}&={\frac {\lambda _{\text{trans}}^{-2}-1}{1-\lambda _{\text{axial}}^{-2}}}\end{aligned}}$

## Applications of Poisson's effect

One area in which Poisson's effect has a considerable influence is in pressurized pipe flow. When the air or liquid inside a pipe is highly pressurized it exerts a uniform force on the inside of the pipe, resulting in a hoop stress within the pipe material. Due to Poisson's effect, this hoop stress will cause the pipe to increase in diameter and slightly decrease in length. The decrease in length, in particular, can have a noticeable effect upon the pipe joints, as the effect will accumulate for each section of pipe joined in series. A restrained joint may be pulled apart or otherwise prone to failure.

Another area of application for Poisson's effect is in the realm of structural geology. Rocks, like most materials, are subject to Poisson's effect while under stress. In a geological timescale, excessive erosion or sedimentation of Earth's crust can either create or remove large vertical stresses upon the underlying rock. This rock will expand or contract in the vertical direction as a direct result of the applied stress, and it will also deform in the horizontal direction as a result of Poisson's effect. This change in strain in the horizontal direction can affect or form joints and dormant stresses in the rock.

Although cork was historically chosen to seal wine bottles for other reasons (including its inert nature, impermeability, flexibility, sealing ability, and resilience), cork's Poisson's ratio of zero provides another advantage. As the cork is inserted into the bottle, the upper part which is not yet inserted does not expand in diameter as it is compressed axially. The force needed to insert a cork into a bottle arises only from the friction between the cork and the bottle due to the radial compression of the cork. If the stopper were made of rubber, for example, with a Poisson's ratio of about 0.5, there would be a relatively large additional force required to overcome the radial expansion of the upper part of the rubber stopper.

Most car mechanics are aware that it is hard to pull a rubber hose (such as a coolant hose) off a metal pipe stub, as the tension of pulling causes the diameter of the hose to shrink, gripping the stub tightly. (This is the same effect as shown in a Chinese finger trap.) Hoses can more easily be pushed off stubs instead using a wide flat blade.
