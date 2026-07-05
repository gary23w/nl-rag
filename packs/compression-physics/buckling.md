---
title: "Buckling"
source: https://en.wikipedia.org/wiki/Buckling
domain: compression-physics
license: CC-BY-SA-4.0
tags: compression physics
fetched: 2026-07-05
---

# Buckling

In structural engineering, **buckling** is the sudden change in shape (deformation) of a structural component under load, such as the bowing of a column under compression or the wrinkling of a plate under shear. If a structure is subjected to a gradually increasing load, when the load reaches a critical level, a member may suddenly change shape and the structure and component is said to have *buckled*. Euler's critical load and Johnson's parabolic formula are used to determine the buckling stress of a column.

Buckling may occur even though the stresses that develop in the structure are well below those needed to cause failure in the material of which the structure is composed. Further loading may cause significant and somewhat unpredictable deformations, possibly leading to complete loss of the member's load-carrying capacity. However, if the deformations that occur after buckling do not cause the complete collapse of that member, the member will continue to support the load that caused it to buckle. If the buckled member is part of a larger assemblage of components such as a building, any load applied to the buckled part of the structure beyond that which caused the member to buckle will be redistributed within the structure. Some aircraft are designed for thin skin panels to continue carrying load even in the buckled state.

## Forms of buckling

### Columns

The ratio of the effective length of a column to the least radius of gyration of its cross section is called the slenderness ratio (sometimes expressed with the Greek letter lambda, λ). This ratio affords a means of classifying columns and their failure mode. The slenderness ratio is important for design considerations. All the following are approximate values used for convenience.

If the load on a column is applied through the center of gravity (centroid) of its cross section, it is called an axial load. A load at any other point in the cross section is known as an eccentric load. A short column under the action of an axial load will fail by direct compression before it buckles, but a long column loaded in the same manner will fail by springing suddenly outward laterally (buckling) in a bending mode. The buckling mode of deflection is considered a failure mode, and it generally occurs before the axial compression stresses (direct compression) can cause failure of the material by yielding or fracture of that compression member. However, intermediate-length columns will fail by a combination of direct compressive stress and bending.

In particular:

- A short steel column is one whose slenderness ratio does not exceed 50; an intermediate length steel column has a slenderness ratio ranging from about 50 to 200, and its behavior is dominated by the strength limit of the material, while a long steel column may be assumed to have a slenderness ratio greater than 200 and its behavior is dominated by the modulus of elasticity of the material.
- A short concrete column is one having a ratio of unsupported length to least dimension of the cross section equal to or less than 10. If the ratio is greater than 10, it is considered a long column (sometimes referred to as a slender column).
- Timber columns may be classified as short columns if the ratio of the length to least dimension of the cross section is equal to or less than 10. The dividing line between intermediate and long timber columns cannot be readily evaluated. One way of defining the lower limit of long timber columns would be to set it as the smallest value of the ratio of length to least cross sectional area that would just exceed a certain constant K of the material. Since K depends on the modulus of elasticity and the allowable compressive stress parallel to the grain, it can be seen that this arbitrary limit would vary with the species of the timber. The value of K is given in most structural handbooks.

The theory of the behavior of columns was investigated in 1757 by mathematician Leonhard Euler. He derived the formula, termed Euler's critical load, that gives the maximum axial load that a long, slender, ideal column can carry without buckling. An ideal column is one that is:

- perfectly straight
- made of a homogeneous material
- free from initial stress.

When the applied load reaches the Euler load, sometimes called the critical load, the column comes to be in a state of unstable equilibrium. At that load, the introduction of the slightest lateral force will cause the column to fail by suddenly "jumping" to a new configuration, and the column is said to have buckled. This is what happens when a person stands on an empty aluminum can and then taps the sides briefly, causing it to then become instantly crushed (the vertical sides of the can may be understood as an infinite series of extremely thin columns). The formula derived by Euler for long slender columns is

$F_{c}={\frac {\pi ^{2}EI}{(KL)^{2}}}$

where

- $F_{c}$ , maximum or critical force (vertical load on column),
- E , modulus of elasticity,
- I , smallest area moment of inertia (second moment of area) of the cross section of the column,
- L , unsupported length of column,
- K , column effective length factor, whose value depends on the conditions of end support of the column, as follows.
  - For both ends pinned (hinged, free to rotate), $K=1.0$ .
  - For both ends fixed, $K=0.50$ .
  - For one end fixed and the other end pinned, $K\approx 0.699$ .
  - For one end fixed and the other end free to move laterally, $K=2.0$ .
- $KL$ is the effective length of the column.

Examination of this formula reveals the following facts with regard to the load-bearing ability of slender columns.

- The elasticity of the material of the column and not the compressive strength of the material of the column determines the column's buckling load.
- The buckling load is directly proportional to the second moment of area of the cross section.
- The boundary conditions have a considerable effect on the critical load of slender columns. The boundary conditions determine the mode of bending of the column and the distance between inflection points on the displacement curve of the deflected column. The inflection points in the deflection shape of the column are the points at which the curvature of the column changes sign and are also the points at which the column's internal bending moments of the column are zero. The closer the inflection points are, the greater the resulting axial load capacity (bucking load) of the column.

A conclusion from the above is that the buckling load of a column may be increased by changing its material to one with a higher modulus of elasticity (E), or changing the design of the column's cross section so as to increase its moment of inertia. The latter can be done without increasing the weight of the column by distributing the material as far from the principal axis of the column's cross section as possible. For most purposes, the most effective use of the material of a column is that of a tubular section.

Another insight that may be gleaned from this equation is the effect of length on critical load. Doubling the unsupported length of the column quarters the allowable load. The restraint offered by the end connections of a column also affects its critical load. If the connections are perfectly rigid (not allowing rotation of its ends), the critical load will be four times that for a similar column where the ends are pinned (allowing rotation of its ends).

Since the radius of gyration is defined as the square root of the ratio of the column's moment of inertia about an axis to its cross sectional area, the above Euler formula may be reformatted by substituting the radius of gyration $Ar^{2}$ for I :

$\sigma ={\frac {F}{A}}={\frac {\pi ^{2}E}{(l/r)^{2}}}$

where $\sigma =F/A$ is the stress that causes buckling in the column, and $l/r$ is the slenderness ratio.

Since structural columns are commonly of intermediate length, the Euler formula has little practical application for ordinary design. Issues that cause deviation from the pure Euler column behaviour include imperfections in geometry of the column in combination with plasticity/non-linear stress strain behaviour of the column's material. Consequently, a number of empirical column formulae have been developed that agree with test data, all of which embody the slenderness ratio. Due to the uncertainty in the behavior of columns, for design, appropriate safety factors are introduced into these formulae. One such formula is the Perry Robertson formula which estimates the critical buckling load based on an assumed small initial curvature, hence an eccentricity of the axial load. The Rankine Gordon formula, named for William John Macquorn Rankine and Perry Hugesworth Gordon (1899 – 1966), is also based on experimental results and suggests that a column will buckle at a load *F*max given by: ${\frac {1}{F_{\max }}}={\frac {1}{F_{e}}}+{\frac {1}{F_{c}}}$

where $F_{e}$ is the Euler maximum load and $F_{c}$ is the maximum compressive load. This formula typically produces a conservative estimate of $F_{\max }$ .

#### Self-buckling

A free-standing, vertical column, with density $\rho$ , Young's modulus E , and cross-sectional area A , will buckle under its own weight if its height exceeds a certain critical value:

$h_{\text{crit}}=\left({\frac {9B^{2}}{4}}\,{\frac {EI}{\rho gA}}\right)^{\frac {1}{3}}$

where g is the acceleration due to gravity, I is the second moment of area of the beam cross section, and B is the first zero of the Bessel function of the first kind of order −1/3, which is equal to 1.86635086...

### Thin-walled rings

The stability of uniformly compressed thin-walled elastic rings has a long and well-established history, shaped by a number of significant contributions. Most scholars agree that Levy's groundbreaking study from 1884 served as the theoretical foundation for further studies on the buckling of circular rings.

A thin-walled ring of thickness t and mean radius R , subjected to a uniformly distributed radial load q , may in fact lose its initial circular configuration when the applied load reaches a critical value. This instability phenomenon is characterized by the transition from the undeformed circular shape to a non-circular equilibrium configuration and represents one of the fundamental structural instability problems in elasticity theory.

Due to their close relationship to the popular Donnell approximations used in shell structure analysis , the governing equations for circular rings are very significant. A great deal of research of the predominant buckling modes of submarine and submersible pressure hulls, as well as other thin-walled cylindrical structures exposed to external pressure, as indicated in the engineering examples below, is based on similar assumptions.

For the case of fluid-pressure loading, in which the external pressure remains normal to the deformed surface throughout the deformation process, the critical buckling pressure is given by

$q_{cr}={\frac {3EI}{R^{2}}}$

where E is the Young's modulus of the material and I is the second moment of area of the ring cross-section. For so-called dead loads, which remain constant in both magnitude and direction during deformation, the corresponding critical buckling pressure is

$q_{cr}={\frac {4EI}{R^{2}}}$

Following Levy's original derivation, the ring axis is commonly assumed to be inextensible. More recent studies, however, have investigated the influence of axis deformability on the buckling and post-buckling response of thin rings . Actually, accounting for the extensibility of the ring axis a more complete and physically consistent description of the post-buckling behaviour can be obtained.

### Plate buckling

A plate is a 3-dimensional structure defined as having a width of comparable size to its length, with a thickness that is very small in comparison to its other two dimensions. Similar to columns, thin plates experience out-of-plane buckling deformations when subjected to critical loads; however, contrasted to column buckling, plates under buckling loads can continue to carry loads, called local buckling. This phenomenon is incredibly useful in numerous systems, as it allows systems to be engineered to provide greater loading capacities.

For a rectangular plate, supported along every edge, loaded with a uniform compressive force per unit length, the derived governing equation can be stated by:

${\frac {\partial ^{4}w}{\partial x^{4}}}+2{\frac {\partial ^{4}w}{\partial x^{2}\partial y^{2}}}+{\frac {\partial ^{4}w}{\partial y^{4}}}={\frac {12\left(1-\nu ^{2}\right)}{Et^{3}}}\left(-N_{x}{\frac {\partial ^{2}w}{\partial x^{2}}}\right)$

where

- w , out-of-plane deflection
- $N_{x}$ , uniformly distributed compressive load
- $\nu$ , Poisson's ratio
- E , modulus of elasticity
- t , thickness

The solution to the deflection can be expanded into two harmonic functions shown:

$w=\sum _{m=1}^{\infty }\sum _{n=1}^{\infty }w_{mn}\sin \left({\frac {m\pi x}{a}}\right)\sin \left({\frac {n\pi y}{b}}\right)$

where

- m , number of half sine curvatures that occur lengthwise
- n , number of half sine curvatures that occur widthwise
- a , length of specimen
- b , width of specimen

The previous equation can be substituted into the earlier differential equation where n equals 1. $N_{x}$ can be separated providing the equation for the critical compressive loading of a plate:

$N_{x,cr}=k_{cr}{\frac {\pi ^{2}Et^{3}}{12\left(1-\nu ^{2}\right)b^{2}}}$

where the buckling coefficient $k_{cr}$ , is given by: $k_{cr}=\left({\frac {mb}{a}}+{\frac {a}{mb}}\right)^{2}$

The buckling coefficient is influenced by the aspect of the specimen, a / ${b}$ , and the number of lengthwise curvatures. For an increasing number of such curvatures, the aspect ratio produces a varying buckling coefficient; but each relation provides a minimum value for each m . This minimum value can then be used as a constant, independent from both the aspect ratio and m .

Given stress is found by the load per unit area, the following expression is found for the critical stress: $\sigma _{cr}=k_{cr}{\frac {\pi ^{2}E}{12\left(1-\nu ^{2}\right)\left({\frac {b}{t}}\right)^{2}}}$

From the derived equations, it can be seen the close similarities between the critical stress for a column and for a plate. As the width b shrinks, the plate acts more like a column as it increases the resistance to buckling along the plate's width. The increase of a allows for an increase of the number of sine waves produced by buckling along the length, but also increases the resistance from the buckling along the width. This creates the preference of the plate to buckle in such a way to equal the number of curvatures both along the width and length. Due to boundary conditions, when a plate is loaded with a critical stress and buckles, the edges perpendicular to the load cannot deform out-of-plane and will therefore continue to carry the stresses. This creates a non-uniform compressive loading along the ends, where the stresses are imposed on half of the effective width on either side of the specimen, given by the following:

${\frac {b_{\text{eff}}}{b}}\approx {\sqrt {{\frac {\sigma _{cr}}{\sigma _{y}}}\left(1-1.022{\sqrt {\frac {\sigma _{cr}}{\sigma _{y}}}}\right)}}$

where

- $b_{\text{eff}}$ , effective width
- $\sigma _{y}$ , yielding stress

As the loaded stress increases, the effective width continues to shrink; if the stresses on the ends ever reach the yield stress, the plate will fail. This is what allows the buckled structure to continue supporting loadings. When the axial load over the critical load is plotted against the displacement, the fundamental path is shown. It demonstrates the plate's similarity to a column under buckling; however, past the buckling load, the fundamental path bifurcates into a secondary path that curves upward, providing the ability to be subjected to higher loads past the critical load.

### Flexural-torsional buckling

Flexural-torsional buckling can be described as a combination of bending and twisting response of a member in compression. Such a deflection mode must be considered for design purposes. This mostly occurs in columns with "open" cross-sections and hence have a low torsional stiffness, such as channels, structural tees, double-angle shapes, and equal-leg single angles. Circular cross sections do not experience such a mode of buckling.

### Lateral-torsional buckling

When a simply supported beam is loaded in bending, the top side is in compression, and the bottom side is in tension. If the beam is not supported in the lateral direction (i.e., perpendicular to the plane of bending), and the flexural load increases to a critical limit, the beam will experience a lateral deflection of the compression flange as it buckles locally. The lateral deflection of the compression flange is restrained by the beam web and tension flange, but for an open section the twisting mode is more flexible, hence the beam both twists and deflects laterally in a failure mode known as *lateral-torsional buckling*. In wide-flange sections (with high lateral bending stiffness), the deflection mode will be mostly twisting in torsion. In narrow-flange sections, the bending stiffness is lower and the column's deflection will be closer to that of lateral bucking deflection mode.

The use of closed sections such as square hollow section will mitigate the effects of lateral-torsional buckling by virtue of their high torsional stiffness.

*C**b* is a modification factor used in the equation for nominal flexural strength when determining lateral-torsional buckling. The reason for this factor is to allow for non-uniform moment diagrams when the ends of a beam segment are braced. The conservative value for *C**b* can be taken as 1, regardless of beam configuration or loading, but in some cases it may be excessively conservative. *C**b* is always equal to or greater than 1, never less. For cantilevers or overhangs where the free end is unbraced, Cb is equal to 1. Tables of values of *C**b* for simply supported beams exist.

If an appropriate value of *C**b* is not given in tables, it can be obtained via the following formula:

$C_{b}={\frac {12.5M_{\max }}{2.5M_{\max }+3M_{A}+4M_{B}+3M_{C}}}$

where

- $M_{\max }$ , absolute value of maximum moment in the unbraced segment,
- $M_{A}$ , absolute value of maximum moment at quarter point of the unbraced segment,
- $M_{B}$ , absolute value of maximum moment at centerline of the unbraced segment,
- $M_{C}$ , absolute value of maximum moment at three-quarter point of the unbraced segment,

The result is the same for all unit systems.

### Plastic buckling

The buckling strength of a member is less than the elastic buckling strength of a structure if the material of the member is stressed beyond the elastic material range and into the non-linear (plastic) material behavior range. When the compression load is near the buckling load, the structure will bend significantly and the material of the column will diverge from a linear stress-strain behavior. The stress-strain behavior of materials is not strictly linear even below the yield point, hence the modulus of elasticity decreases as stress increases, and significantly so as the stresses approach the material's yield strength. This reduced material rigidity reduces the buckling strength of the structure and results in a buckling load less than that predicted by the assumption of linear elastic behavior.

A more accurate approximation of the buckling load can be had by the use of the tangent modulus of elasticity, Et, which is less than the elastic modulus, in place of the elastic modulus of elasticity. The tangent is equal to the elastic modulus and then decreases beyond the proportional limit. The tangent modulus is a line drawn tangent to the stress-strain curve at a particular value of strain (in the elastic section of the stress-strain curve, the tangent modulus is equal to the elastic modulus). Plots of the tangent modulus of elasticity for a variety of materials are available in standard references.

### Crippling

Sections that are made up of flanged plates such as a channel, can still carry load in the corners after the flanges have locally buckled. Crippling is failure of the complete section.

### Diagonal tension

Because of the thin skins typically used in aerospace applications, skins may buckle at low load levels. However, once buckled, instead of being able to transmit shear forces, they are still able to carry load through *diagonal tension* (DT) stresses in the web. This results in a non-linear behaviour in the load carrying behaviour of these details. The ratio of the actual load to the load at which buckling occurs is known as the *buckling ratio* of a sheet. High buckling ratios may lead to excessive wrinkling of the sheets which may then fail through yielding of the wrinkles. Although they may buckle, thin sheets are designed to not permanently deform and return to an unbuckled state when the applied loading is removed. Repeated buckling may lead to fatigue failures.

Sheets under diagonal tension are supported by stiffeners that as a result of sheet buckling carry a distributed load along their length, and may in turn result in these structural members failing under buckling.

Thicker plates may only partially form a diagonal tension field and may continue to carry some of the load through shear. This is known as *incomplete diagonal tension* (IDT). This behavior was studied by Wagner and these beams are sometimes known as Wagner beams.

Diagonal tension may also result in a pulling force on any fasteners such as rivets that are used to fasten the web to the supporting members. Fasteners and sheets must be designed to resist being pulled off their supports.

### Dynamic buckling

If a column is loaded suddenly and then the load released, the column can sustain a much higher load than its static (slowly applied) buckling load. This can happen in a long, unsupported column used as a drop hammer. The duration of compression at the impact end is the time required for a stress wave to travel along the column to the other (free) end and back down as a relief wave. Maximum buckling occurs near the impact end at a wavelength much shorter than the length of the rod, and at a stress many times the buckling stress of a statically loaded column. The critical condition for buckling amplitude to remain less than about 25 times the effective rod straightness imperfection at the buckle wavelength is

$\sigma L=\rho c^{2}h$

where $\sigma$ is the impact stress, L is the length of the rod, c is the elastic wave speed, and h is the smaller lateral dimension of a rectangular rod. Because the buckle wavelength depends only on $\sigma$ and h , this same formula holds for thin cylindrical shells of thickness h .

## Theory

### Energy method

Often it is very difficult to determine the exact buckling load in complex structures using the Euler formula, due to the difficulty in determining the constant K. Therefore, maximum buckling load is often approximated using energy conservation and referred to as an energy method in structural analysis.

The first step in this method is to assume a displacement mode and a function that represents that displacement. This function must satisfy the most important boundary conditions, such as displacement and rotation. The more accurate the displacement function, the more accurate the result.

The method assumes that the system (the column) is a conservative system in which energy is not dissipated as heat, hence the energy added to the column by the applied external forces is stored in the column in the form of strain energy.

$U_{\text{applied}}=U_{\text{strain}}$

In this method, there are two equations used (for small deformations) to approximate the "strain" energy (the potential energy stored as elastic deformation of the structure) and "applied" energy (the work done on the system by external forces).

${\begin{aligned}U_{\text{strain}}&={\frac {E}{2}}\int I(x)(w_{xx}(x))^{2}\,\mathrm {d} x\\U_{\text{applied}}&={\frac {P_{\text{crit}}}{2}}\int (w_{x}(x))^{2}\,\mathrm {d} x\end{aligned}}$

where $w(x)$ is the displacement function and the subscripts x and $xx$ refer to the first and second derivatives of the displacement.

### Single-degree-of-freedom models

Using the concept of *total potential energy*, V , it is possible to identify four fundamental forms of buckling found in structural models with one degree of freedom. We start by expressing $V=U-P\Delta$ where U is the strain energy stored in the structure, P is the applied *conservative* load and $\Delta$ is the distance moved by P in its direction. Using the axioms of elastic instability theory, namely that equilibrium is any point where V is stationary with respect to the coordinate measuring the degree(s) of freedom and that these points are only stable if V is a local minimum and unstable if otherwise (e.g. maximum or a point of inflection).

These four forms of elastic buckling are the *saddle-node bifurcation* or *limit point*; the *supercritical* or *stable-symmetric* bifurcation; the *subcritical* or *unstable-symmetric* bifurcation; and the *transcritical* or *asymmetric* bifurcation. All but the first of these examples is a form of *pitchfork bifurcation*. Simple models for each of these types of buckling behaviour are shown in the figures below, along with the associated bifurcation diagrams.

| Limit Point | Stable-symmetric bifurcation |
|---|---|
|   |   |
| Unstable-symmetric bifurcation | Asymmetric bifurcation |
|   |   |

|   |   |
|---|---|
|   |   |

## Engineering examples

### Bicycle wheels

A conventional bicycle wheel consists of a thin rim kept under high compressive stress by the (roughly normal) inward pull of a large number of spokes. It can be considered as a loaded column that has been bent into a circle. If spoke tension is increased beyond a safe level or if part of the rim is subject to a certain lateral force, the wheel spontaneously fails into a characteristic saddle shape (sometimes called a "taco" or a "pringle") like a three-dimensional Euler column. If this is a purely elastic deformation the rim will resume its proper plane shape if spoke tension is reduced or a lateral force from the opposite direction is applied.

### Roads

Buckling is a failure mode in pavement materials, primarily with concrete, since asphalt is more flexible. Radiant heat from the sun is absorbed in the road surface, causing it to expand, forcing adjacent pieces to push against each other. If the stress is sufficient, the pavement can lift and crack without warning. Traversing a buckled section can be jarring to automobile drivers, described as running over a speed hump at highway speeds.

### Rail tracks

Similarly, rail tracks also expand when heated, and can fail by buckling, a phenomenon called **sun kink**. It is more common for rails to move laterally, often pulling the underlying ties (sleepers) along.

Sun kink can lead to railroads drastically reducing the speed of trains, leading to delays and cancellations. This is done to avoid derailment. Intensifying heat waves due to climate change doubled the number of hours of heat related delays in 2023, compared to 2018.

These accidents were deemed to be sun kink-related (*more information available at List of rail accidents (2000–2009)*):

- December 27, 1989: Wentworthville derailment, near Wentworthville, Australia.
- April 18, 2002 Amtrak *Auto-Train* derailment, off CSX tracks, near Crescent City, Florida.
- July 29, 2002 Amtrak *Capitol Limited* derailment, off CSX tracks, near Kensington, Maryland.
- July 8, 2010 CSX train derailment in Waxhaw, North Carolina.
- July 6, 2012 WMATA Metrorail train derailment near West Hyattsville station, Maryland.

The Federal Railroad Administration issued a Safety Advisory on July 11, 2012 alerting railroad operators to inspect tracks for "buckling-prone conditions." The Advisory included a brief summary of four derailments that had occurred between June 23 to July 4 that appeared to be "heat related incidents."

### Pipes and pressure vessels

Pipes and pressure vessels subject to external overpressure and implosion, caused for example by steam cooling within the pipe and condensing into water with subsequent massive pressure drop, risk buckling due to compressive hoop stresses. Design rules for calculation of the required wall thickness or reinforcement rings are given in various piping and pressure vessel codes.

Buckling is a major failure mode in submarine and submersible hulls.

### Super- and hypersonic aerospace vehicles

Aerothermal heating can lead to buckling of surface panels on super- and hypersonic aerospace vehicles such as high-speed aircraft, rockets and reentry vehicles. If buckling is caused by aerothermal loads, the situation can be further complicated by enhanced heat transfer in areas where the structure deforms towards the flow-field.
