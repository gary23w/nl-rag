---
title: "Compressive strength"
source: https://en.wikipedia.org/wiki/Compressive_strength
domain: compression-physics
license: CC-BY-SA-4.0
tags: compression physics
fetched: 2026-07-05
---

# Compressive strength

In mechanics, **compressive strength** (or **compression strength**) is the capacity of a material or structure to withstand loads tending to reduce size (compression). It is opposed to *tensile strength*, which withstands loads tending to elongate, resisting tension (being pulled apart). In the study of strength of materials, compressive strength, tensile strength, and shear strength can be analyzed independently.

Some materials fracture at their compressive strength limit; others deform irreversibly, so a given amount of deformation may be considered as the limit for compressive load. Compressive strength is a key value for design of structures.

Compressive strength is often measured on a universal testing machine. Measurements of compressive strength are affected by the specific test method and conditions of measurement. Compressive strengths are usually reported in relationship to a specific technical standard.

## Introduction

Tension

Compression

When a specimen of material is loaded in such a way that it extends it is said to be in *tension*. On the other hand, if the material compresses and shortens it is said to be in *compression*.

On an atomic level, molecules or atoms are forced together when in compression, whereas they are pulled apart when in tension. Since atoms in solids always try to find an equilibrium position, and distance between other atoms, forces arise throughout the entire material which oppose both tension or compression. The phenomena prevailing on an atomic level are therefore similar.

The "strain" is the relative change in length under applied stress; positive strain characterizes an object under tension load which tends to lengthen it, and a compressive stress that shortens an object gives negative strain. Tension tends to pull small sideways deflections back into alignment, while compression tends to amplify such deflection into buckling.

Compressive strength is measured on materials, components, and structures.

The ultimate compressive strength of a material is the maximum uniaxial compressive stress that it can withstand before complete failure. This value is typically determined through a compressive test conducted using a universal testing machine. During the test, a steadily increasing uniaxial compressive load is applied to the test specimen until it fails. The specimen, often cylindrical in shape, experiences both axial shortening and lateral expansion under the load. As the load increases, the machine records the corresponding deformation, plotting a stress–strain curve that would look similar to the following:

The compressive strength of the material corresponds to the stress at the red point shown on the curve. In a compression test, there is a linear region where the material follows Hooke's law. Hence, for this region, $\sigma =E\varepsilon ,$ where, this time, E refers to the Young's modulus for compression. In this region, the material deforms elastically and returns to its original length when the stress is removed.

This linear region terminates at what is known as the yield point. Above this point the material behaves plastically and will not return to its original length once the load is removed.

There is a difference between the engineering stress and the true stress. By its basic definition the uniaxial stress is given by:

${\acute {\sigma }}={\frac {F}{A}},$ where F is load applied [N] and A is area [m2].

As stated, the area of the specimen varies on compression. In reality therefore the area is some function of the applied load i.e. *A* = *f* (*F*). Indeed, stress is defined as the force divided by the area at the start of the experiment. This is known as the engineering stress, and is defined by $\sigma _{e}={\frac {F}{A_{0}}},$ where *A*0 is the original specimen area [m2].

Correspondingly, the engineering strain is defined by $\varepsilon _{e}={\frac {l-l_{0}}{l_{0}}},$ where l is the current specimen length [m] and *l*0 is the original specimen length [m]. True strain, also known as logarithmic strain or natural strain, provides a more accurate measure of large deformations, such as in materials like ductile metals ${\acute {\epsilon }}=\ln(l/l_{o})=ln(1+\epsilon _{e})$ The compressive strength therefore corresponds to the point on the engineering stress–strain curve $\left(\varepsilon _{e}^{*},\sigma _{e}^{*}\right)$ defined by $\sigma _{e}^{*}={\frac {F^{*}}{A_{0}}}$ $\varepsilon _{e}^{*}={\frac {l^{*}-l_{0}}{l_{0}}},$

where *F** is the load applied just before crushing and *l** is the specimen length just before crushing.

## Deviation of engineering stress from true stress

When a uniaxial compressive load is applied to an object it will become shorter and spread laterally so its original cross sectional area ( ${\textstyle A_{o}}$ ) increases to the loaded area ( ${\textstyle A}$ ). Thus the true stress ( ${\acute {\sigma }}=F/A$ ) deviates from engineering stress ( $\sigma _{e}=F/A_{o}$ ). Tests that measure the engineering stress at the point of failure in a material are often sufficient for many routine applications, such as quality control in concrete production. However, determining the true stress in materials under compressive loads is important for research focused on the properties on new materials and their processing.

The geometry of test specimens and friction can significantly influence the results of compressive stress tests. Friction at the contact points between the testing machine and the specimen can restrict the lateral expansion at its ends (also known as 'barreling') leading to non-uniform stress distribution. This is discussed in section on contact with friction.

### Frictionless contact

With a compressive load on a test specimen it will become shorter and spread laterally so its cross sectional area increases and the true compressive stress is ${\acute {\sigma }}=F/A$ and the engineering stress is ${\sigma _{e}}=F/A_{o}$ The cross sectional area ( ${\textstyle A}$ ) and consequently the stress ( ${\textstyle {\acute {\sigma }}}$ ) are uniform along the length of the specimen because there are no external lateral constraints. This condition represents an ideal test condition. For all practical purposes the volume of a high bulk modulus material (e.g. solid metals) is not changed by uniaxial compression. So $Al=A_{o}l_{o}$ Using the strain equation from above $A=A_{o}/(1+\epsilon _{e})$ and ${\acute {\sigma }}=\sigma _{e}(1+\epsilon _{e})$ Note that compressive strain is negative, so the true stress ( ${\acute {\sigma }}$ ) is less than the engineering stress ( ${\textstyle \sigma _{e}}$ ). The true strain ( ${\acute {\epsilon }}$ ) can be used in these formulas instead of engineering strain ( ${\textstyle \epsilon _{e}}$ ) when the deformation is large.

### Contact with friction

As the load is applied, friction at the interface between the specimen and the test machine restricts the lateral expansion at its ends. This has two effects:

- It can cause non-uniform stress distribution across the specimen, with higher stress at the centre and lower stress at the edges, which affects the accuracy of the result.
- It causes a barreling effect (bulging at the centre) in ductile materials. This changes the specimen's geometry and affects its load-bearing capacity, leading to a higher apparent compressive strength.

Various methods can be used to reduce the friction according to the application:

- Applying a suitable lubricant, such as MoS2, oil or grease; however, care must be taken not to affect the material properties with the lubricant used.
- Use of PTFE or other low-friction sheets between the test machine and specimen.
- A spherical or self-aligning test fixture, which can minimize friction by applying the load more evenly across the specimen's surface.

Three methods can be used to compensate for the effects of friction on the test result:

1. Correction formulas
2. Geometric extrapolation
3. Finite element analysis

#### Correction formulas

Round test specimens made from ductile materials with a high bulk modulus, such as metals, tend to form a barrel shape under axial compressive loading due to frictional contact at the ends. For this case the equivalent true compressive stress for this condition can be calculated using ${\acute {\sigma }}=C\sigma _{a}$ where

$C={(1-2R/d_{2})\ln(1-d_{2})/(2R))}^{-1}$

$R=(l^{2}+(d_{2}-d_{1})^{2})/(4(d_{2}-d_{1}))$

$\sigma _{a}=4F/(\pi d_{2}^{2})$

l

is the loaded length of the test specimen,

$d_{1}$

is the loaded diameter of the test specimen at its ends, and

$d_{2}$

is the maximum loaded diameter of the test specimen.

Note that if there is frictionless contact between the ends of the specimen and the test machine, the bulge radius becomes infinite ( ${\textstyle R=\infty }$ ) and ${\textstyle C=1}$ . In this case, the formulas yield the same result as ${\textstyle {\acute {\sigma }}=\sigma _{e}(1+\epsilon _{e})}$ because ${\textstyle \sigma _{a}}$ changes according to the ratio $(d_{o}/d_{2})^{2}$ .

The parameters ( ${\textstyle F,d_{1},d_{2},l}$ ) obtained from a test result can be used with these formulas to calculate the equivalent true stress ${\textstyle {\acute {\sigma }}}$ at failure.

The graph of specimen shape effect shows how the ratio of true stress to engineering stress (σ´/σe) varies with the aspect ratio of the test specimen ( ${\textstyle d_{o}/l_{o}}$ ). The curves were calculated using the formulas provided above, based on the specific values presented in the table for specimen shape effect calculations. For the curves where end restraint is applied to the specimens, they are assumed to be fully laterally restrained, meaning that the coefficient of friction at the contact points between the specimen and the testing machine is greater than or equal to one (μ ⩾ 1). As shown in the graph, as the relative length of the specimen increases ( ${\textstyle d_{o}/l_{o}\rightarrow 0}$ ), the ratio of true to engineering stress ( ${\acute {\sigma }}/\sigma _{e}$ ) approaches the value corresponding to frictionless contact between the specimen and the machine, which is the ideal test condition.

|   | Frictionless | Laterally Constrained |
|---|---|---|
| Constant volume | $\pi l_{o}d_{o}^{2}/4=\pi l(d_{2}^{2}+d_{1}^{2})/12$ |   |
| Equal diameters | $d_{1}=d_{2}$ | $d_{o}=d_{1}$ |
| Solve for $d_{2}$ | $\pi l_{o}d_{o}^{2}/4=\pi l(d_{2}^{2}+d_{2}^{2})/12$ | $\pi l_{o}d_{o}^{2}/4=\pi l(d_{2}^{2}+d_{o}^{2})/12$ |
| $d_{2}=d_{o}{\sqrt {l_{o}/l}}$ | $d_{2}=3d_{o}{\sqrt {(3l_{o}/l-1)/18}}$ |   |
| Equivalent stress ratio | ${\acute {\sigma }}/\sigma _{a}=1$ | ${\acute {\sigma }}/\sigma _{a}=C$ |
| Engineering stress | $\sigma _{e}=4F/\pi d_{o}^{2}$ |   |
| Average stress | $\sigma _{a}=4F/\pi d_{2}^{2}$ |   |
| Average stress ratio | $\sigma _{a}/\sigma _{e}=(d_{o}/d_{2})^{2}$ |   |
| True strain | ${\acute {\epsilon }}=\ln(l/l_{o})$ |   |

#### Geometric extrapolation

As shown in the section on correction formulas, as the length of test specimens is increased and their aspect ratio approaches zero ( $d_{o}/l_{o}\longrightarrow 0$ ), the compressive stresses (σ) approach the true value (σ′). However, conducting tests with excessively long specimens is impractical, as they would fail by buckling before reaching the material's true compressive strength. To overcome this, a series of tests can be conducted using specimens with varying aspect ratios, and the true compressive strength can then be determined through extrapolation.

#### Finite element analysis

## Comparison of compressive and tensile strengths

Concrete and ceramics typically have much higher compressive strengths than tensile strengths. Composite materials, such as glass fiber epoxy matrix composite, tend to have higher tensile strengths than compressive strengths. Metals are difficult to test to failure in tension vs compression. In compression metals fail from buckling/crumbling/45° shear which is much different (though higher stresses) than tension which fails from defects or necking down.

## Compressive failure modes

There are various modes of ductile failure for structural members in compression. The most common is Flexural Buckling, where the member will bend outward without initially fracturing. This failure mode depends on the slenderness ratio, a ratio between the effective length of the member and the radius of gyration. Another common ductile failure mode for compression members is yielding. Compressive yielding occurs in members with a low slenderness ratio, meaning they are short and wide. Other possible compressive failure modes for ductile materials, include local buckling, where only part of the member fails, flexural-torsional buckling, where a member both twists and buckles laterally, and torsional buckling where the member only twists and does not move laterally.

A brittle material in compression typically will fail by axial splitting, shear fracture, or ductile failure depending on the level of constraint in the direction perpendicular to the direction of loading. If there is no constraint (also called confining pressure), the brittle material is likely to fail by axial splitting. Moderate confining pressure often results in shear fracture, while high confining pressure often leads to ductile failure, even in brittle materials.

Axial Splitting relieves elastic energy in brittle material by releasing strain energy in the directions perpendicular to the applied compressive stress. As defined by a materials Poisson ratio a material compressed elastically in one direction will strain in the other two directions. During axial splitting a crack may release that tensile strain by forming a new surface parallel to the applied load. The material then proceeds to separate in two or more pieces. Hence the axial splitting occurs most often when there is no confining pressure, i.e. a lesser compressive load on axis perpendicular to the main applied load. The material now split into micro columns will feel different frictional forces either due to inhomogeneity of interfaces on the free end or stress shielding. In the case of stress shielding, inhomogeneity in the materials can lead to different Young's modulus. This will in turn cause the stress to be disproportionately distributed, leading to a difference in frictional forces. In either case this will cause the material sections to begin bending and lead to ultimate failure.

### Microcracking

Microcracks are a leading cause of failure under compression for brittle and quasi-brittle materials. Sliding along crack tips leads to tensile forces along the tip of the crack. Microcracks tend to form around any pre-existing crack tips. In all cases it is the overall global compressive stress interacting with local microstructural anomalies to create local areas of tension.  Microcracks can stem from a few factors.

1. Porosity is the controlling factor for compressive strength in many materials. Microcracks can form around pores, until about they reach approximately the same size as their parent pores. (a)
2. Stiff inclusions within a material such as a precipitate can cause localized areas of tension. (b) When inclusions are grouped up or larger, this effect can be amplified.
3. Even without pores or stiff inclusions, a material can develop microcracks between weak inclined (relative to applied stress) interfaces. These interfaces can slip and create a secondary crack. These secondary cracks can continue opening, as the slip of the original interfaces keeps opening the secondary crack (c). The slipping of interfaces alone is not solely responsible for secondary crack growth as inhomogeneities in the material's Young's modulus can lead to an increase in effective misfit strain. Cracks that grow this way are known as wingtip microcracks.

The growth of microcracks is not the growth of the original crack or imperfection. The cracks that nucleate do so perpendicular to the original crack and are known as secondary cracks. The figure below emphasizes this point for wingtip cracks.

These secondary cracks can grow to as long as 10–15 times the length of the original cracks in simple (uniaxial) compression. However, if a transverse compressive load is applied. The growth is limited to a few integer multiples of the original crack's length.

#### Shear bands

If the sample size is large enough such that the worse defect's secondary cracks cannot grow large enough to break the sample, other defects within the sample will begin to grow secondary cracks as well. This will occur homogeneously over the entire sample. These micro-cracks form an echelon that can form an "intrinsic" fracture behavior, the nucleus of a shear fault instability. Shown right:

Eventually this leads the material deforming non-homogeneously. That is the strain caused by the material will no longer vary linearly with the load. Creating localized shear bands on which the material will fail according to deformation theory. "The onset of localized banding does not necessarily constitute final failure of a material element, but it presumably is at least the beginning of the primary failure process under compressive loading."

## Typical values

| Material | Rs (MPa) |
|---|---|
| Steel | 250–1,500 |
| Porcelain | 20–1,000 |
| Adult Bone | 135–170 for males; 100–150 for females |
| Concrete | 17–70 |
| Ice (−5 to −20 °C) | 5–25 |
| Ice (0 °C) | 3 |
| Styrofoam | ~1 |

## Compressive strength of concrete

For designers, compressive strength is one of the most important engineering properties of concrete. It is standard industrial practice that the compressive strength of a given concrete mix is classified by grade. Cubic or cylindrical samples of concrete are tested under a compression testing machine to measure this value. Test requirements vary by country based on their differing design codes. Use of a compressometer is common.

The compressive strength of concrete is given in terms of the characteristic compressive strength of 150 mm size cubes tested after 28 days (fck). In field, compressive strength tests are also conducted at interim duration i.e. after 7 days to verify the anticipated compressive strength expected after 28 days. The same is done to be forewarned of an event of failure and take necessary precautions. The **characteristic strength** is defined as the **strength** of the **concrete** below which not more than 5% of the test results are expected to fall.

For design purposes, this compressive strength value is restricted by dividing with a factor of safety, whose value depends on the design philosophy used.

The construction industry is often involved in a wide array of testing. In addition to simple compression testing, testing standards such as ASTM C39, ASTM C109, ASTM C469, ASTM C1609 are among the test methods that can be followed to measure the mechanical properties of concrete. When measuring the compressive strength and other material properties of concrete, testing equipment that can be manually controlled or servo-controlled may be selected depending on the procedure followed. Certain test methods specify or limit the loading rate to a certain value or a range, whereas other methods request data based on test procedures run at very low rates.

Ultra-high performance concrete (UHPC) is defined as having a compressive strength over 150 MPa.
