---
title: "Fracture mechanics"
source: https://en.wikipedia.org/wiki/Fracture_mechanics
domain: materials-science
license: CC-BY-SA-4.0
tags: materials science, crystallographic defect, grain boundary, mechanical properties
fetched: 2026-07-02
---

# Fracture mechanics

**Fracture mechanics** is the field of mechanics concerned with the study of the propagation of cracks in materials. It uses methods of analytical solid mechanics to calculate the driving force on a crack and those of experimental solid mechanics to characterize the material's resistance to fracture.

Theoretically, the stress ahead of a sharp crack tip becomes infinite and cannot be used to describe the state around a crack. Fracture mechanics is used to characterise the loads on a crack, typically using a single parameter to describe the complete loading state at the crack tip. A number of different parameters have been developed. When the **plastic zone** at the tip of the crack is small relative to the crack length the stress state at the crack tip is the result of elastic forces within the material and is termed **linear elastic fracture mechanics** (**LEFM**) and can be characterised using the stress intensity factor K . Although the load on a crack can be arbitrary, in 1957 G. Irwin found any state could be reduced to a combination of three independent stress intensity factors:

- **Mode I** – Opening mode (a tensile stress normal to the plane of the crack),
- **Mode II** – Sliding mode (a shear stress acting parallel to the plane of the crack and perpendicular to the crack front), and
- **Mode III** – Tearing mode (a shear stress acting parallel to the plane of the crack and parallel to the crack front).

When the size of the plastic zone at the crack tip is too large, **elastic-plastic fracture mechanics** can be used with parameters such as the J-integral or the crack tip opening displacement.

The characterising parameter describes the state of the crack tip which can then be related to experimental conditions to ensure similitude. Crack growth occurs when the parameters typically exceed certain critical values. Corrosion may cause a crack to slowly grow when the stress corrosion stress intensity threshold is exceeded. Similarly, small flaws may result in crack growth when subjected to cyclic loading. Known as fatigue, it was found that for long cracks, the rate of growth is largely governed by the range of the stress intensity $\Delta K$ experienced by the crack due to the applied loading. Fast fracture will occur when the stress intensity exceeds the fracture toughness of the material. The prediction of crack growth is at the heart of the damage tolerance mechanical design discipline.

## Motivation

The processes of material manufacture, processing, machining, and forming may introduce flaws in a finished mechanical component. Arising from the manufacturing process, interior and surface flaws are found in all metal structures. Not all such flaws are unstable under service conditions. Fracture mechanics is the analysis of flaws to discover those that are safe (that is, do not grow) and those that are liable to propagate as cracks and so cause failure of the flawed structure. Despite these inherent flaws, it is possible to achieve through damage tolerance analysis the safe operation of a structure. Fracture mechanics as a subject for critical study has barely been around for a century and thus is relatively new.

Fracture mechanics should attempt to provide quantitative answers to the following questions:

1. What is the strength of the component as a function of crack size?
2. What crack size can be tolerated under service loading, i.e. what is the maximum permissible crack size?
3. How long does it take for a crack to grow from a certain initial size, for example the minimum detectable crack size, to the maximum permissible crack size?
4. What is the service life of a structure when a certain pre-existing flaw size (e.g. a manufacturing defect) is assumed to exist?
5. During the period available for crack detection how often should the structure be inspected for cracks?

## Linear elastic fracture mechanics

### Griffith's criterion

Fracture mechanics was developed during World War I by English aeronautical engineer A. A. Griffith – thus the term **Griffith crack** – to explain the failure of brittle materials. Griffith's work was motivated by two contradictory facts:

- The stress needed to fracture bulk glass is around 100 MPa (15,000 psi).
- The theoretical stress needed for breaking atomic bonds of glass is approximately 10,000 MPa (1,500,000 psi).

A theory was needed to reconcile these conflicting observations. Also, experiments on glass fibers that Griffith himself conducted suggested that the fracture stress increases as the fiber diameter decreases. Hence the uniaxial tensile strength, which had been used extensively to predict material failure before Griffith, could not be a specimen-independent material property. Griffith suggested that the low fracture strength observed in experiments, as well as the size-dependence of strength, was due to the presence of microscopic flaws in the bulk material.

To verify the flaw hypothesis, Griffith introduced an artificial flaw in his experimental glass specimens. The artificial flaw was in the form of a surface crack which was much larger than other flaws in a specimen. The experiments showed that the product of the square root of the flaw length ( a ) and the stress at fracture ( $\sigma _{f}$ ) was nearly constant, which is expressed by the equation:

$\sigma _{f}{\sqrt {a}}\approx C$

An explanation of this relation in terms of linear elasticity theory is problematic. Linear elasticity theory predicts that stress (and hence the strain) at the tip of a sharp flaw in a linear elastic material is infinite. To avoid that problem, Griffith developed a thermodynamic approach to explain the relation that he observed.

The growth of a crack, the extension of the surfaces on either side of the crack, requires an increase in the surface energy. Griffith found an expression for the constant C in terms of the surface energy of the crack by solving the elasticity problem of a finite crack in an elastic plate. Briefly, the approach was:

- Compute the potential energy stored in a perfect specimen under a uniaxial tensile load.
- Fix the boundary so that the applied load does no work and then introduce a crack into the specimen. The crack relaxes the stress and hence reduces the elastic energy near the crack faces. On the other hand, the crack increases the total surface energy of the specimen.
- Compute the change in the free energy (surface energy − elastic energy) as a function of the crack length. Failure occurs when the free energy attains a peak value at a critical crack length, beyond which the free energy decreases as the crack length increases, i.e. by causing fracture. Using this procedure, Griffith found that

$C={\sqrt {\cfrac {2E\gamma }{\pi }}}$

where E is the Young's modulus of the material and $\gamma$ is the surface energy density of the material. Assuming $E=62\ {\text{GPa}}$ and $\gamma =1\ {\text{J/m}}^{2}$ gives excellent agreement of Griffith's predicted fracture stress with experimental results for glass.

For the simple case of a thin rectangular plate with a crack perpendicular to the load, the energy release rate, G , becomes:

$G={\frac {\pi \sigma ^{2}a}{E}}\,$

where $\sigma$ is the applied stress, a is half the crack length, and E is the Young's modulus, which for the case of plane strain should be divided by the plate stiffness factor $(1-\nu ^{2})$ . The strain energy release rate can physically be understood as: *the rate at which energy is absorbed by growth of the crack*.

However, we also have that:

$G_{c}={\frac {\pi \sigma _{f}^{2}a}{E}}\,$

If G ≥ $G_{c}$ , this is the criterion for which the crack will begin to propagate.

For materials highly deformed before crack propagation, the linear elastic fracture mechanics formulation is no longer applicable and an adapted model is necessary to describe the stress and displacement field close to crack tip, such as on fracture of soft materials.

### Irwin's modification

> *Griffith's work was largely ignored by the engineering community until the early 1950s. The reasons for this appear to be (a) in the actual structural materials the level of energy needed to cause fracture is orders of magnitude higher than the corresponding surface energy, and (b) in structural materials there are always some inelastic deformations around the crack front that would make the assumption of linear elastic medium with infinite stresses at the crack tip highly unrealistic.*

Griffith's theory provides excellent agreement with experimental data for brittle materials such as glass. For ductile materials such as steel, although the relation $\sigma _{f}{\sqrt {a}}=C$ still holds, the surface energy (*γ*) predicted by Griffith's theory is usually unrealistically high. A group working under G. R. Irwin at the U.S. Naval Research Laboratory (NRL) during World War II realized that plasticity must play a significant role in the fracture of ductile materials.

In ductile materials (and even in materials that appear to be brittle), a plastic zone develops at the tip of the crack. As the applied load increases, the plastic zone increases in size until the crack grows and the elastically strained material behind the crack tip unloads. The plastic loading and unloading cycle near the crack tip leads to the dissipation of energy as heat. Hence, a dissipative term has to be added to the energy balance relation devised by Griffith for brittle materials. In physical terms, additional energy is needed for crack growth in ductile materials as compared to brittle materials.

Irwin's strategy was to partition the energy into two parts:

- the stored elastic strain energy which is released as a crack grows. This is the thermodynamic driving force for fracture.
- the dissipated energy which includes plastic dissipation and the surface energy (and any other dissipative forces that may be at work). The dissipated energy provides the thermodynamic resistance to fracture.

Then the total energy is:

$G=2\gamma +G_{p}$

where $\gamma$ is the surface energy and $G_{p}$ is the plastic dissipation (and dissipation from other sources) per unit area of crack growth.

The modified version of Griffith's energy criterion can then be written as

$\sigma _{f}{\sqrt {a}}={\sqrt {\cfrac {E~G}{\pi }}}.$

For brittle materials such as glass, the surface energy term dominates and $G\approx 2\gamma =2\,\,{\text{J/m}}^{2}$ . For ductile materials such as steel, the plastic dissipation term dominates and $G\approx G_{p}=1000\,\,{\text{J/m}}^{2}$ . For polymers close to the glass transition temperature, we have intermediate values of G between 2 and 1000 ${\text{J/m}}^{2}$ .

### Stress intensity factor

Another significant achievement of Irwin and his colleagues was to find a method of calculating the amount of energy available for fracture in terms of the asymptotic stress and displacement fields around a crack front in a linear elastic solid. This asymptotic expression for the stress field in mode I loading is related to the stress intensity factor $K_{I}$ following:

$\sigma _{ij}=\left({\cfrac {K_{I}}{\sqrt {2\pi r}}}\right)~f_{ij}(\theta )$

where $\sigma _{ij}$ are the Cauchy stresses, r is the distance from the crack tip, $\theta$ is the angle with respect to the plane of the crack, and $f_{ij}$ are functions that depend on the crack geometry and loading conditions. Irwin called the quantity K the stress intensity factor. Since the quantity $f_{ij}$ is dimensionless, the stress intensity factor can be expressed in units of ${\text{MPa}}{\sqrt {\text{m}}}$ .

Stress intensity replaced strain energy release rate and a term called fracture toughness replaced surface weakness energy. Both of these terms are simply related to the energy terms that Griffith used:

$K_{I}=\sigma {\sqrt {\pi a}}\,$

and

$K_{c}={\begin{cases}{\sqrt {EG_{c}}}&{\text{for plane stress}}\\\\{\sqrt {\cfrac {EG_{c}}{1-\nu ^{2}}}}&{\text{for plane strain}}\end{cases}}$

where $K_{I}$ is the mode I stress intensity, $K_{c}$ the fracture toughness, and $\nu$ is Poisson's ratio.

Fracture occurs when $K_{I}\geq K_{c}$ . For the special case of plane strain deformation, $K_{c}$ becomes $K_{Ic}$ and is considered a material property. The subscript I arises because of the different ways of loading a material to enable a crack to propagate. It refers to so-called "mode I " loading as opposed to mode $II$ or $III$ :

The expression for $K_{I}$ will be different for geometries other than the center-cracked infinite plate, as discussed in the article on the stress intensity factor. Consequently, it is necessary to introduce a dimensionless correction factor, Y , in order to characterize the geometry. This correction factor, also often referred to as the *geometric shape factor*, is given by empirically determined series and accounts for the type and geometry of the crack or notch. We thus have:

$K_{I}=Y\sigma {\sqrt {\pi a}}\,$

where Y is a function of the crack length and width of sheet given, for a sheet of finite width W containing a through-thickness crack of length $2a$ , by:

$Y\left({\frac {a}{W}}\right)={\sqrt {\sec \left({\frac {\pi a}{W}}\right)}}\,$

### Strain energy release

Irwin was the first to observe that if the size of the plastic zone around a crack is small compared to the size of the crack, the energy required to grow the crack will not be critically dependent on the state of stress (the plastic zone) at the crack tip. In other words, a purely elastic solution may be used to calculate the amount of energy available for fracture.

The energy release rate for crack growth or *strain energy release rate* may then be calculated as the change in elastic strain energy per unit area of crack growth, i.e.,

$G:=\left[{\cfrac {\partial U}{\partial a}}\right]_{P}=-\left[{\cfrac {\partial U}{\partial a}}\right]_{u}$

where *U* is the elastic energy of the system and *a* is the crack length. Either the load *P* or the displacement *u* are constant while evaluating the above expressions.

Irwin showed that for a mode I crack (opening mode) the strain energy release rate and the stress intensity factor are related by:

$G=G_{I}={\begin{cases}{\cfrac {K_{I}^{2}}{E}}&{\text{plane stress}}\\{\cfrac {(1-\nu ^{2})K_{I}^{2}}{E}}&{\text{plane strain}}\end{cases}}$

where *E* is the Young's modulus, *ν* is Poisson's ratio, and *K*I is the stress intensity factor in mode I. Irwin also showed that the strain energy release rate of a planar crack in a linear elastic body can be expressed in terms of the mode I, mode II (sliding mode), and mode III (tearing mode) stress intensity factors for the most general loading conditions.

Next, Irwin adopted the additional assumption that the size and shape of the energy dissipation zone remains approximately constant during brittle fracture. This assumption suggests that the energy needed to create a unit fracture surface is a constant that depends only on the material. This new material property was given the name *fracture toughness* and designated *G*Ic. Today, it is the critical stress intensity factor *K*Ic, found in the plane strain condition, which is accepted as the defining property in linear elastic fracture mechanics.

### Crack tip plastic zone

In theory the stress at the crack tip where the radius is nearly zero, would tend to infinity. This would be considered a stress singularity, which is not possible in real-world applications. For this reason, in numerical studies in the field of fracture mechanics, it is often appropriate to represent cracks as round tipped notches, with a geometry dependent region of stress concentration replacing the crack-tip singularity. In actuality, the stress concentration at the tip of a crack within real materials has been found to have a finite value but larger than the nominal stress applied to the specimen.

Nevertheless, there must be some sort of mechanism or property of the material that prevents such a crack from propagating spontaneously. The assumption is, the plastic deformation at the crack tip effectively blunts the crack tip. This deformation depends primarily on the applied stress in the applicable direction (in most cases, this is the y-direction of a regular Cartesian coordinate system), the crack length, and the geometry of the specimen. To estimate how this plastic deformation zone extended from the crack tip, Irwin equated the yield strength of the material to the far-field stresses of the y-direction along the crack (x direction) and solved for the effective radius. From this relationship, and assuming that the crack is loaded to the critical stress intensity factor, Irwin developed the following expression for the idealized radius of the zone of plastic deformation at the crack tip:

$r_{p}={\frac {K_{C}^{2}}{2\pi \sigma _{Y}^{2}}}$

Models of ideal materials have shown that this zone of plasticity is centered at the crack tip. This equation gives the approximate ideal radius of the plastic zone deformation beyond the crack tip, which is useful to many structural scientists because it gives a good estimate of how the material behaves when subjected to stress. In the above equation, the parameters of the stress intensity factor and indicator of material toughness, $K_{C}$ , and the yield stress, $\sigma _{Y}$ , are of importance because they illustrate many things about the material and its properties, as well as about the plastic zone size. For example, if $K_{c}$ is high, then it can be deduced that the material is tough, and if $\sigma _{Y}$ is low, one knows that the material is more ductile. The ratio of these two parameters is important to the radius of the plastic zone. For instance, if $\sigma _{Y}$ is small, then the squared ratio of $K_{C}$ to $\sigma _{Y}$ is large, which results in a larger plastic radius. This implies that the material can plastically deform, and, therefore, is tough. This estimate of the size of the plastic zone beyond the crack tip can then be used to more accurately analyze how a material will behave in the presence of a crack.

The same process as described above for a single event loading also applies and to cyclic loading. If a crack is present in a specimen that undergoes cyclic loading, the specimen will plastically deform at the crack tip and delay the crack growth. In the event of an overload or excursion, this model changes slightly to accommodate the sudden increase in stress from that which the material previously experienced. At a sufficiently high load (overload), the crack grows out of the plastic zone that contained it and leaves behind the pocket of the original plastic deformation. Now, assuming that the overload stress is not sufficiently high as to completely fracture the specimen, the crack will undergo further plastic deformation around the new crack tip, enlarging the zone of residual plastic stresses. This process further toughens and prolongs the life of the material because the new plastic zone is larger than what it would be under the usual stress conditions. This allows the material to undergo more cycles of loading. This idea can be illustrated further by the graph of Aluminum with a center crack undergoing overloading events.

### Limitations

But a problem arose for the NRL researchers because naval materials, e.g., ship-plate steel, are not perfectly elastic but undergo significant plastic deformation at the tip of a crack. One basic assumption in Irwin's linear elastic fracture mechanics is small scale yielding, the condition that the size of the plastic zone is small compared to the crack length. However, this assumption is quite restrictive for certain types of failure in structural steels though such steels can be prone to brittle fracture, which has led to a number of catastrophic failures.

Linear-elastic fracture mechanics is of limited practical use for structural steels and Fracture toughness testing can be expensive.

## Elastic–plastic fracture mechanics

Most engineering materials show some nonlinear elastic and inelastic behavior under operating conditions that involve large loads. In such materials the assumptions of linear elastic fracture mechanics may not hold, that is,

- the plastic zone at a crack tip may have a size of the same order of magnitude as the crack size
- the size and shape of the plastic zone may change as the applied load is increased and also as the crack length increases.

Therefore, a more general theory of crack growth is needed for elastic-plastic materials that can account for:

- the local conditions for initial crack growth which include the nucleation, growth, and coalescence of voids (decohesion) at a crack tip.
- a global energy balance criterion for further crack growth and unstable fracture.

### CTOD

Historically, the first parameter for the determination of fracture toughness in the elasto-plastic region was the crack tip opening displacement (CTOD) or "opening at the apex of the crack" indicated. This parameter was determined by Wells during the studies of structural steels, which due to the high toughness could not be characterized with the linear elastic fracture mechanics model. He noted that, before the fracture happened, the walls of the crack were leaving and that the crack tip, after fracture, ranged from acute to rounded off due to plastic deformation. In addition, the rounding of the crack tip was more pronounced in steels with superior toughness.

There are a number of alternative definitions of CTOD. In the two most common definitions, CTOD is the displacement at the original crack tip and the 90 degree intercept. The latter definition was suggested by Rice and is commonly used to infer CTOD in finite element models of such. Note that these two definitions are equivalent if the crack tip blunts in a semicircle.

Most laboratory measurements of CTOD have been made on edge-cracked specimens loaded in three-point bending. Early experiments used a flat paddle-shaped gage that was inserted into the crack; as the crack opened, the paddle gage rotated, and an electronic signal was sent to an x-y plotter. This method was inaccurate, however, because it was difficult to reach the crack tip with the paddle gage. Today, the displacement V at the crack mouth is measured, and the CTOD is inferred by assuming the specimen halves are rigid and rotate about a hinge point (the crack tip).

### R-curve

An early attempt in the direction of elastic-plastic fracture mechanics was Irwin's **crack extension resistance curve**, Crack growth resistance curve or **R-curve**. This curve acknowledges the fact that the resistance to fracture increases with growing crack size in elastic-plastic materials. The R-curve is a plot of the total energy dissipation rate as a function of the crack size and can be used to examine the processes of slow stable crack growth and unstable fracture. However, the R-curve was not widely used in applications until the early 1970s. The main reasons appear to be that the R-curve depends on the geometry of the specimen and the crack driving force may be difficult to calculate.

### J-integral

In the mid-1960s James R. Rice (then at Brown University) and G. P. Cherepanov independently developed a new toughness measure to describe the case where there is sufficient crack-tip deformation that the part no longer obeys the linear-elastic approximation. Rice's analysis, which assumes non-linear elastic (or monotonic deformation theory plastic) deformation ahead of the crack tip, is designated the J-integral. This analysis is limited to situations where plastic deformation at the crack tip does not extend to the furthest edge of the loaded part. It also demands that the assumed non-linear elastic behavior of the material is a reasonable approximation in shape and magnitude to the real material's load response. The elastic-plastic failure parameter is designated JIc and is conventionally converted to KIc using the equation below. Also note that the J integral approach reduces to the Griffith theory for linear-elastic behavior.

The mathematical definition of J-integral is as follows:

$J=\int _{\Gamma }(w\,dy-T_{i}{\frac {\partial u_{i}}{\partial x}}\,ds)\quad {\text{with}}\quad w=\int _{0}^{\varepsilon _{ij}}\sigma _{ij}\,d\varepsilon _{ij}$

where

$\Gamma$

is an arbitrary path clockwise around the apex of the crack,

w

is the density of strain energy,

$T_{i}$

are the components of the vectors of traction,

$u_{i}$

are the components of the displacement vectors,

$ds$

is an incremental length along the path

$\Gamma$

, and

$\sigma _{ij}$

and

$\varepsilon _{ij}$

are the stress and strain tensors.

Since engineers became accustomed to using *K*Ic to characterise fracture toughness, a relation has been used to reduce *J*Ic to it:

$K_{Ic}={\sqrt {E^{*}J_{Ic}}}\,$

where

$E^{*}=E$

for

plane stress

and

$E^{*}={\frac {E}{1-\nu ^{2}}}$

for plane strain.

### Cohesive zone model

When a significant region around a crack tip has undergone plastic deformation, other approaches can be used to determine the possibility of further crack extension and the direction of crack growth and branching. A simple technique that is easily incorporated into numerical calculations is the *cohesive zone model* method which is based on concepts proposed independently by Barenblatt and Dugdale in the early 1960s. The relationship between the Dugdale-Barenblatt models and Griffith's theory was first discussed by Willis in 1967. The equivalence of the two approaches in the context of brittle fracture was shown by Rice in 1968.

### Transition flaw size

Let a material have a yield strength $\sigma _{Y}$ and a fracture toughness in mode I $K_{Ic}$ . Based on fracture mechanics, the material will fail at stress $\sigma _{\text{fail}}=K_{Ic}/{\sqrt {\pi a}}$ . Based on plasticity, the material will yield when $\sigma _{fail}=\sigma _{Y}$ . These curves intersect when $a=K_{Ic}^{2}/\pi \sigma _{Y}^{2}$ . This value of a is called as **transition flaw size** $a_{t}$ ., and depends on the material properties of the structure. When the $a<a_{t}$ , the failure is governed by plastic yielding, and when $a>a_{t}$ the failure is governed by fracture mechanics. The value of $a_{t}$ for engineering alloys is 100 mm and for ceramics is 0.001 mm. If we assume that manufacturing processes can give rise to flaws in the order of micrometers, then, it can be seen that ceramics are more likely to fail by fracture, whereas engineering alloys would fail by plastic deformation.

## Concrete fracture analysis

**Concrete fracture analysis** is part of fracture mechanics that studies crack propagation and related failure modes in concrete. As it is widely used in construction, fracture analysis and modes of reinforcement are an important part of the study of concrete, and different concretes are characterized in part by their fracture properties. Common fractures include the cone-shaped fractures that form around anchors under tensile strength.

Bažant (1983) proposed a crack band model for materials like concrete whose homogeneous nature changes randomly over a certain range. He also observed that in plain concrete, the size effect has a strong influence on the critical stress intensity factor, and proposed the relation

> $\sigma$ = $\tau$ / √(1+{ d / $\lambda$ $\delta$ }),

where $\sigma$ = stress intensity factor, $\tau$ = tensile strength, d = size of specimen, $\delta$ = maximum aggregate size, and $\lambda$ = an empirical constant.

## Atomistic Fracture Mechanics

Atomistic Fracture Mechanics (AFM) is a relatively new field that studies the behavior and properties of materials at the atomic scale when subjected to fracture. It integrates concepts from fracture mechanics with atomistic simulations to understand how cracks initiate, propagate, and interact with the microstructure of materials. By using techniques like Molecular Dynamics (MD) simulations, AFM can provide insights into the fundamental mechanisms of crack formation and growth, the role of atomic bonds, and the influence of material defects and impurities on fracture behavior.
