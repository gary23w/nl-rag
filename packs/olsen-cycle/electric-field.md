---
title: "Electric field"
source: https://en.wikipedia.org/wiki/Electric_field
domain: olsen-cycle
license: CC-BY-SA-4.0
tags: olsen cycle
fetched: 2026-07-04
---

# Electric field

An **electric field** (sometimes called **E-field**) is a physical field that surrounds electrically charged particles such as electrons. In classical electromagnetism, the electric field of a single charge (or group of charges) describes their capacity to exert attractive or repulsive forces on another charged object. Charged particles exert attractive forces on each other when the sign of their charges are opposite, one being positive while the other is negative, and repel each other when the signs of the charges are the same. Because these forces are exerted mutually, two charges must be present for the forces to take place. These forces are described by Coulomb's law, which says that the greater the magnitude of the charges, the greater the force, and the greater the distance between them, the weaker the force. Informally, the greater the charge of an object, the stronger its electric field. Similarly, an electric field is stronger nearer charged objects and weaker further away. Electric fields originate from electric charges and time-varying electric currents. Electric fields and magnetic fields are both manifestations of the electromagnetic field. Electromagnetism is one of the four fundamental interactions of nature.

Electric fields are important in many areas of physics, and are exploited in electrical technology. For example, in atomic physics and chemistry, the interaction in the electric field between the atomic nucleus and electrons is the force that holds these particles together in atoms. Similarly, the interaction in the electric field between atoms is the force responsible for chemical bonding that result in molecules.

The electric field is defined as a vector field that associates to each point in space the force per unit of charge exerted on an infinitesimal positive test charge at rest at that point. The SI unit for the electric field is the volt per meter (V/m), which is equal to the newton per coulomb (N/C).

## Description

The electric field is defined at each point in space as the force that would be experienced by an infinitesimally small stationary positive test charge at that point divided by the charge. The electric field is defined in terms of force, and force is a vector (i.e. having both magnitude and direction), so it follows that an electric field may be described by a vector field. The electric field acts between two charges similarly to the way that the gravitational field acts between two masses, as they both obey an inverse-square law with distance. This is the basis for Coulomb's law, which states that, for stationary charges, the electric field varies with the source charge and varies inversely with the square of the distance from the source. This means that if the source charge were doubled, the electric field would double, and if you move twice as far away from the source, the field at that point would be only one-quarter its original strength.

The electric field can be visualized with a set of lines whose direction at each point is the same as those of the field, a concept introduced by Michael Faraday, whose term 'lines of force' is still sometimes used. This illustration has the useful property that, when drawn so that each line represents the same amount of flux, the strength of the field is proportional to the density of the lines. Field lines due to stationary charges have several important properties, including that they always originate from positive charges and terminate at negative charges, they enter all good conductors at right angles, and they never cross or close in on themselves. The field lines are a representative concept; the field actually permeates all the intervening space between the lines. More or fewer lines may be drawn depending on the precision to which it is desired to represent the field. The study of electric fields created by stationary charges is called electrostatics.

Faraday's law describes the relationship between a time-varying magnetic field and the electric field. One way of stating Faraday's law is that the curl of the electric field is equal to the negative time derivative of the magnetic field. In the absence of time-varying magnetic field, the electric field is therefore called conservative (i.e. curl-free). This implies there are two kinds of electric fields: electrostatic fields and fields arising from time-varying magnetic fields. While the curl-free nature of the static electric field allows for a simpler treatment using electrostatics, time-varying magnetic fields are generally treated as a component of a unified electromagnetic field. The study of magnetic and electric fields that change over time is called electrodynamics.

## Mathematical formulation

Electric fields are caused by electric charges, described by Gauss's law, and time varying magnetic fields, described by Faraday's law of induction. Together, these laws are enough to define the behavior of the electric field. However, since the magnetic field is described as a function of electric field, the equations of both fields are coupled and together form Maxwell's equations that describe both fields as a function of charges and currents.

### Electrostatics

In the special case of a steady state (stationary charges and currents), the Maxwell-Faraday inductive effect disappears. The resulting two equations (Gauss's law $\nabla \cdot \mathbf {E} ={\frac {\rho }{\varepsilon _{0}}}$ and Faraday's law with no induction term $\nabla \times \mathbf {E} =0$ ), taken together, are equivalent to Coulomb's law, which states that a particle with electric charge $q_{1}$ at position $\mathbf {r} _{1}$ exerts a force on a particle with charge $q_{0}$ at position $\mathbf {r} _{0}$ of: $\mathbf {F} _{01}={\frac {q_{1}q_{0}}{4\pi \varepsilon _{0}}}{{\hat {\mathbf {r} }}_{01} \over {|\mathbf {r} _{01}|}^{2}}={\frac {q_{1}q_{0}}{4\pi \varepsilon _{0}}}{\mathbf {r} _{01} \over {|\mathbf {r} _{01}|}^{3}}$ where

- $\mathbf {F} _{01}$ is the force on charged particle $q_{0}$ caused by charged particle $q_{1}$ .
- *ε*0 is the permittivity of free space.
- ${\hat {\mathbf {r} }}_{01}$ is a unit vector directed from $\mathbf {r} _{1}$ to $\mathbf {r} _{0}$ .
- $\mathbf {r} _{01}$ is the displacement vector from $\mathbf {r} _{1}$ to $\mathbf {r} _{0}$ .

Note that $\varepsilon _{0}$ must be replaced with $\varepsilon$ , permittivity, when charges are in non-empty media. When the charges $q_{0}$ and $q_{1}$ have the same sign this force is positive, directed away from the other charge, indicating the particles repel each other. When the charges have unlike signs the force is negative, indicating the particles attract. To make it easy to calculate the Coulomb force on any charge at position $\mathbf {r} _{0}$ this expression can be divided by $q_{0}$ leaving an expression that only depends on the other charge (the *source* charge) $\mathbf {E} _{1}(\mathbf {r} _{0})={\frac {\mathbf {F} _{01}}{q_{0}}}={\frac {q_{1}}{4\pi \varepsilon _{0}}}{{\hat {\mathbf {r} }}_{01} \over {|\mathbf {r} _{01}|}^{2}}={\frac {q_{1}}{4\pi \varepsilon _{0}}}{\mathbf {r} _{01} \over {|\mathbf {r} _{01}|}^{3}}$ where $\mathbf {E} _{1}(\mathbf {r} _{0})$ is the component of the electric field at $q_{0}$ due to $q_{1}$ .

This is the *electric field* at point $\mathbf {r} _{0}$ due to the point charge $q_{1}$ ; it is a vector-valued function equal to the Coulomb force per unit charge that a positive point charge would experience at the position $\mathbf {r} _{0}$ . Since this formula gives the electric field magnitude and direction at any point $\mathbf {r} _{0}$ in space (except at the location of the charge itself, $\mathbf {r} _{1}$ , where it becomes infinite) it defines a vector field. From the above formula it can be seen that the electric field due to a point charge is everywhere directed away from the charge if it is positive, and toward the charge if it is negative, and its magnitude decreases with the inverse square of the distance from the charge.

The Coulomb force on a charge of magnitude q at any point in space is equal to the product of the charge and the electric field at that point $\mathbf {F} =q\mathbf {E} .$ The SI unit of the electric field is the newton per coulomb (N/C), or volt per meter (V/m); in terms of the SI base units it is kg⋅m⋅s−3⋅A−1.

### Superposition principle

Due to the linearity of Maxwell's equations, electric fields satisfy the superposition principle, which states that the total electric field, at a point, due to a collection of charges is equal to the vector sum of the electric fields at that point due to the individual charges. This principle is useful in calculating the field created by multiple point charges. If charges $q_{1},q_{2},\dots ,q_{n}$ are stationary in space at points $\mathbf {R} _{1},\mathbf {R} _{2},\dots ,\mathbf {R} _{n}$ , in the absence of currents, the superposition principle says that the resulting field is the sum of fields generated by each particle as described by Coulomb's law: ${\begin{aligned}\mathbf {E} (\mathbf {r} )=\mathbf {E} _{1}(\mathbf {r} )+\mathbf {E} _{2}(\mathbf {r} )+\dots +\mathbf {E} _{n}(\mathbf {r} )={1 \over 4\pi \varepsilon _{0}}\sum _{i=1}^{n}q_{i}{{\hat {\mathbf {r} }}_{i} \over {|\mathbf {r} _{i}|}^{2}}={1 \over 4\pi \varepsilon _{0}}\sum _{i=1}^{n}q_{i}{\mathbf {r} _{i} \over {|\mathbf {r} _{i}|}^{3}}\end{aligned}}$ where

- ${\hat {\mathbf {r} }}_{i}$ is the unit vector in the direction from point $\mathbf {R} _{i}$ to point $\mathbf {r}$
- $\mathbf {r} _{i}$ is the displacement vector from point $\mathbf {R} _{i}$ to point $\mathbf {r}$ .

### Continuous charge distributions

The superposition principle allows for the calculation of the electric field due to a distribution of charge density $\rho (\mathbf {r} )$ . By considering the charge $\rho (\mathbf {r} ')dv$ in each small volume of space $dv$ at point $\mathbf {r} '$ as a point charge, the resulting electric field, $d\mathbf {E} (\mathbf {r} )$ , at point $\mathbf {r}$ can be calculated as $d\mathbf {E} (\mathbf {r} )={\frac {\rho (\mathbf {r} ')}{4\pi \varepsilon _{0}}}{{\hat {\mathbf {r} }}' \over {|\mathbf {r} '|}^{2}}dv={\frac {\rho (\mathbf {r} ')}{4\pi \varepsilon _{0}}}{\mathbf {r} ' \over {|\mathbf {r} '|}^{3}}dv$ where

- ${\hat {\mathbf {r} }}'$ is the unit vector pointing from $\mathbf {r} '$ to $\mathbf {r}$ .
- $\mathbf {r} '$ is the displacement vector from $\mathbf {r} '$ to $\mathbf {r}$ .

The total field is found by summing the contributions from all the increments of volume by integrating the charge density over the volume V : $\mathbf {E} (\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\iiint _{V}\,\rho (\mathbf {r} '){\mathbf {r} ' \over {|\mathbf {r} '|}^{3}}dv$

Similar equations follow for a surface charge with surface charge density $\sigma (\mathbf {r} ')$ on surface S $\mathbf {E} (\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\iint _{S}\,\sigma (\mathbf {r} '){\mathbf {r} ' \over {|\mathbf {r} '|}^{3}}da,$ and for line charges with linear charge density $\lambda (\mathbf {r} ')$ on line L $\mathbf {E} (\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\int _{L}\,\lambda (\mathbf {r} '){\mathbf {r} ' \over {|\mathbf {r} '|}^{3}}d\ell .$

### Electric potential

If a system is static, such that magnetic fields are not time-varying, then by Faraday's law, the electric field is curl-free. In this case, one can define an electric potential, that is, a function $\varphi$ such that $\mathbf {E} =-\nabla \varphi$ . This is analogous to the gravitational potential. The difference between the electric potential at two points in space is called the potential difference (or voltage) between the two points.

In general, however, the electric field cannot be described independently of the magnetic field. Given the magnetic vector potential, **A**, defined so that ⁠ $\mathbf {B} =\nabla \times \mathbf {A}$ ⁠, one can still define an electric potential $\varphi$ such that: $\mathbf {E} =-\nabla \varphi -{\frac {\partial \mathbf {A} }{\partial t}},$ where $\nabla \varphi$ is the gradient of the electric potential and ${\frac {\partial \mathbf {A} }{\partial t}}$ is the partial derivative of **A** with respect to time.

Faraday's law of induction can be recovered by taking the curl of that equation $\nabla \times \mathbf {E} =-{\frac {\partial (\nabla \times \mathbf {A} )}{\partial t}}=-{\frac {\partial \mathbf {B} }{\partial t}},$ which justifies, a posteriori, the previous form for **E**.

### Continuous vs. discrete charge representation

The equations of electromagnetism are best described in a continuous description. However, charges are sometimes best described as discrete points; for example, some models may describe electrons as point sources where charge density is infinite on an infinitesimal section of space.

A charge q located at $\mathbf {r} _{0}$ can be described mathematically as a charge density ⁠ $\rho (\mathbf {r} )=q\delta (\mathbf {r} -\mathbf {r} _{0})$ ⁠, where the Dirac delta function (in three dimensions) is used. Conversely, a charge distribution can be approximated by many small point charges.

## Electrostatic fields

Electrostatic fields are electric fields that do not change with time. Such fields are present when systems of charged matter are stationary, or when electric currents are unchanging. In that case, Coulomb's law fully describes the field.

### Parallels between electrostatic and gravitational fields

Coulomb's law, which describes the interaction of electric charges: $\mathbf {F} =q\left({\frac {Q}{4\pi \varepsilon _{0}}}{\frac {\mathbf {\hat {r}} }{|\mathbf {r} |^{2}}}\right)=q\mathbf {E}$ is similar to Newton's law of universal gravitation: $\mathbf {F} =m\left(-GM{\frac {\mathbf {\hat {r}} }{|\mathbf {r} |^{2}}}\right)=m\mathbf {g}$ (where ${\textstyle \mathbf {\hat {r}} =\mathbf {\frac {r}{|r|}} }$ ).

This suggests similarities between the electric field **E** and the gravitational field **g**, or their associated potentials. Mass is sometimes called "gravitational charge".

Electrostatic and gravitational forces both are central, conservative and obey an inverse-square law.

### Uniform fields

A uniform field is one in which the electric field is constant at every point. It can be approximated by placing two conducting plates parallel to each other and maintaining a voltage (potential difference) between them; it is only an approximation because of boundary effects (near the edge of the planes, the electric field is distorted because the plane does not continue). Assuming infinite planes, the magnitude of the electric field *E* is: $E=-{\frac {\Delta V}{d}},$ where Δ*V* is the potential difference between the plates and *d* is the distance separating the plates. The negative sign arises as positive charges repel, so a positive charge will experience a force away from the positively charged plate, in the opposite direction to that in which the voltage increases. In micro- and nano-applications, for instance in relation to semiconductors, a typical magnitude of an electric field is in the order of 106 V⋅m−1, achieved by applying a voltage of the order of 1 volt between conductors spaced 1 μm apart.

### Electric field lines

A convenient way to plot the electric field that works even for complex electric fields is to use field lines. Here the magnitude and direction of an electric field in a region is represented by a number of non-intersecting curved lines that span the region. If plotted correctly, the direction of the electric field at any given point is represented by the direction of nearby lines while the magnitude is represented by the density of the field lines in that region.

Electric field lines do not intersect. They begin at positive charge (or extend from infinity) and end at negative charge (or extend to infinity). Further the number of field lines from a given charge must be proportional to that charge. Electrostatic fields cannot form closed loops. (See the figure for an example of a complex electric field line diagram made for a positive point charge which induces electrical charge on the surfaces of 3 nearby conductors.

Field lines can only approximately represent the electric field in a given region. (It takes an infinite number of field lines to represent the electric field perfectly.) Nevertheless, these diagrams are useful at illustrating how the electric field changes over a given region.

## Electromagnetic fields

Electromagnetic fields are electric and magnetic fields, which may change with time, for instance when charges are in motion. Moving charges produce a magnetic field in accordance with Ampère's circuital law (with Maxwell's addition), which, along with Maxwell's other equations, defines the magnetic field, $\mathbf {B}$ , in terms of its curl: $\nabla \times \mathbf {B} =\mu _{0}\left(\mathbf {J} +\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\right),$ where $\mathbf {J}$ is the current density, $\mu _{0}$ is the vacuum permeability, and $\varepsilon _{0}$ is the vacuum permittivity.

Both the electric current density and the partial derivative of the electric field with respect to time, contribute to the curl of the magnetic field. In addition, the Maxwell–Faraday equation states $\nabla \times \mathbf {E} =-{\frac {\partial \mathbf {B} }{\partial t}}.$ These represent two of Maxwell's four equations and they intricately link the electric and magnetic fields together, resulting in the electromagnetic field. The equations represent a set of four coupled multi-dimensional partial differential equations which, when solved for a system, describe the combined behavior of the electromagnetic fields. In general, the force experienced by a test charge in an electromagnetic field is given by the Lorentz force law: $\mathbf {F} =q\mathbf {E} +q\mathbf {v} \times \mathbf {B} .$

## Energy in the electric field

The total energy per unit volume stored by the electromagnetic field is $u_{\text{EM}}={\frac {\varepsilon }{2}}|\mathbf {E} |^{2}+{\frac {1}{2\mu }}|\mathbf {B} |^{2}$ where ε is the permittivity of the medium in which the field exists, $\mu$ its magnetic permeability, and **E** and **B** are the electric and magnetic field vectors.

As **E** and **B** fields are coupled, it would be misleading to split this expression into "electric" and "magnetic" contributions. In particular, an electrostatic field in any given frame of reference in general transforms into a field with a magnetic component in a relatively moving frame. Accordingly, decomposing the electromagnetic field into an electric and magnetic component is frame-specific, and similarly for the associated energy.

The total energy *U*EM stored in the electromagnetic field in a given volume *V* is $U_{\text{EM}}={\frac {1}{2}}\int _{V}\left(\varepsilon |\mathbf {E} |^{2}+{\frac {1}{\mu }}|\mathbf {B} |^{2}\right)dV\,.$

## Electric displacement field

### Definitive equation of vector fields

In the presence of matter, it is helpful to extend the notion of the electric field into three vector fields: $\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P}$ where **P** is the electric polarization – the volume density of electric dipole moments, and **D** is the electric displacement field. Since **E** and **P** are defined separately, this equation can be used to define **D**. The physical interpretation of **D** is not as clear as **E** (effectively the field applied to the material) or **P** (induced field due to the dipoles in the material), but still serves as a convenient mathematical simplification, since Maxwell's equations can be simplified in terms of free charges and currents.

### Constitutive relation

The **E** and **D** fields are related by the permittivity of the material, *ε*.

For linear, homogeneous, isotropic materials **E** and **D** are proportional and constant throughout the region, there is no position dependence: $\mathbf {D} (\mathbf {r} )=\varepsilon \mathbf {E} (\mathbf {r} ).$

For inhomogeneous materials, there is a position dependence throughout the material: $\mathbf {D} (\mathbf {r} )=\varepsilon (\mathbf {r} )\mathbf {E} (\mathbf {r} )$

For anisotropic materials the **E** and **D** fields are not parallel, and so **E** and **D** are related by the permittivity tensor (a 2nd order tensor field), in component form: $D_{i}=\varepsilon _{ij}E_{j}$

For non-linear media, **E** and **D** are not proportional. Materials can have varying extents of linearity, homogeneity and isotropy.

## Relativistic effects on electric field

### Point charge in uniform motion

The invariance of the form of Maxwell's equations under Lorentz transformation can be used to derive the electric field of a uniformly moving point charge. The charge of a particle is considered frame invariant, as supported by experimental evidence. Alternatively the electric field of uniformly moving point charges can be derived from the Lorentz transformation of four-force experienced by test charges in the source's rest frame given by Coulomb's law and assigning electric field and magnetic field by their definition given by the form of Lorentz force. However the following equation is only applicable when no acceleration is involved in the particle's history where Coulomb's law can be considered or symmetry arguments can be used for solving Maxwell's equations in a simple manner. The electric field of such a uniformly moving point charge is hence given by: $\mathbf {E} ={\frac {q}{4\pi \varepsilon _{0}r^{3}}}{\frac {1-\beta ^{2}}{(1-\beta ^{2}\sin ^{2}\theta )^{3/2}}}\mathbf {r} ,$ where q is the charge of the point source, $\mathbf {r}$ is the position vector from the point source to the point in space, $\beta$ is the ratio of observed speed of the charge particle to the speed of light and $\theta$ is the angle between $\mathbf {r}$ and the observed velocity of the charged particle.

The above equation reduces to that given by Coulomb's law for non-relativistic speeds of the point charge. Spherical symmetry is not satisfied due to breaking of symmetry in the problem by specification of direction of velocity for calculation of field. To illustrate this, field lines of moving charges are sometimes represented as unequally spaced radial lines which would appear equally spaced in a co-moving reference frame.

### Propagation of disturbances in electric fields

Special theory of relativity imposes the principle of locality, that requires cause and effect to be time-like separated events where the causal efficacy does not travel faster than the speed of light. Maxwell's laws are found to confirm to this view since the general solutions of fields are given in terms of retarded time which indicate that electromagnetic disturbances travel at the speed of light. Advanced time, which also provides a solution for Maxwell's law are ignored as an unphysical solution.

For the motion of a charged particle, considering for example the case of a moving particle with the above described electric field coming to an abrupt stop, the electric fields at points far from it do not immediately revert to that classically given for a stationary charge. On stopping, the field around the stationary points begin to revert to the expected state and this effect propagates outwards at the speed of light while the electric field lines far away from this will continue to point radially towards an assumed moving charge. This virtual particle will never be outside the range of propagation of the disturbance in electromagnetic field, since charged particles are restricted to have speeds slower than that of light, which makes it impossible to construct a Gaussian surface in this region that violates Gauss's law. Another technical difficulty that supports this is that charged particles travelling faster than or equal to speed of light no longer have a unique retarded time. Since electric field lines are continuous, an electromagnetic pulse of radiation is generated that connects at the boundary of this disturbance travelling outwards at the speed of light. In general, any accelerating point charge radiates electromagnetic waves however, non-radiating acceleration is possible in a systems of charges.

### Arbitrarily moving point charge

For arbitrarily moving point charges, propagation of potential fields such as Lorenz gauge fields at the speed of light needs to be accounted for by using Liénard–Wiechert potential. Since the potentials satisfy Maxwell's equations, the fields derived for point charge also satisfy Maxwell's equations. The electric field is expressed as: $\mathbf {E} (\mathbf {r} ,\mathbf {t} )={\frac {q}{4\pi \varepsilon _{0}}}\left({\frac {\left(\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}\right)}{\gamma ^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}\left|\mathbf {r} -\mathbf {r} _{s}\right|^{2}}}+{\frac {\mathbf {n} _{s}\times \left(\left(\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}\right)\times {\dot {{\boldsymbol {\beta }}_{s}}}\right)}{c\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}\left|\mathbf {r} -\mathbf {r} _{s}\right|}}\right)_{t=t_{r}}$ where q is the charge of the point source, ${\textstyle {t_{r}}}$ is retarded time or the time at which the source's contribution of the electric field originated, ${\textstyle {r}_{s}(t)}$ is the position vector of the particle, ${\textstyle \mathbf {n} _{s}(\mathbf {r} ,t)}$ is a unit vector pointing from charged particle to the point in space, ${\textstyle {\boldsymbol {\beta }}_{s}(t)}$ is the velocity of the particle divided by the speed of light, and ${\textstyle \gamma (t)}$ is the corresponding Lorentz factor. The retarded time is given as solution of: $t_{r}=t-{\frac {|\mathbf {r} -\mathbf {r} _{s}(t_{r})|}{c}}$

The uniqueness of solution for ${\textstyle {t_{r}}}$ for given t , $\mathbf {r}$ and $r_{s}(t)$ is valid for charged particles moving slower than speed of light. Electromagnetic radiation of accelerating charges is known to be caused by the acceleration dependent term in the electric field from which relativistic correction for Larmor formula is obtained.

There exist yet another set of solutions for Maxwell's equation of the same form but for advanced time ${\textstyle {t_{a}}}$ instead of retarded time given as a solution of:

$t_{a}=t+{\frac {\left|\mathbf {r} -\mathbf {r} _{s}(t_{a})\right|}{c}}$

Since the physical interpretation of this indicates that the electric field at a point is governed by the particle's state at a point of time in the future, it is considered as an unphysical solution and hence neglected. However, there have been theories exploring the advanced time solutions of Maxwell's equations, such as Feynman Wheeler absorber theory.

The above equation, although consistent with that of uniformly moving point charges as well as its non-relativistic limit, are not corrected for quantum-mechanical effects.

## Common formulas

| Static charge configuration | Figure | Electric field |   |
|---|---|---|---|
| Infinite wire |   | $\mathbf {E} ={\frac {\lambda }{2\pi \varepsilon _{0}x}}{\hat {\mathbf {x} }},$ where $\lambda$ is uniform linear charge density. |   |
| Infinitely large surface |   | $\mathbf {E} ={\frac {\sigma }{2\varepsilon _{0}}}{\hat {\mathbf {x} }},$ where $\sigma$ is uniform surface charge density. |   |
| Infinitely long cylindrical volume |   | $\mathbf {E} ={\frac {\lambda }{2\pi \varepsilon _{0}x}}{\hat {\mathbf {x} }},$ where $\lambda$ is uniform linear charge density. |   |
| Spherical volume |   | $\mathbf {E} ={\frac {Q}{4\pi \varepsilon _{0}x^{2}}}{\hat {\mathbf {x} }},$ outside the sphere, where Q is the total charge uniformly distributed in the volume. | $\mathbf {E} ={\frac {Qr}{4\pi \varepsilon _{0}R^{3}}}{\hat {\mathbf {r} }},$ inside the sphere, where Q is the total charge uniformly distributed in the volume. |
| Spherical surface |   | $\mathbf {E} ={\frac {Q}{4\pi \varepsilon _{0}x^{2}}}{\hat {\mathbf {x} }},$ outside the sphere, where Q is the total charge uniformly distributed on the surface. | $\mathbf {E} =0,$ inside the sphere for uniform charge distribution. |
| Charged Ring |   | $\mathbf {E} ={\frac {Qx}{4\pi \varepsilon _{0}(R^{2}+x^{2})^{3/2}}}{\hat {\mathbf {x} }},$ on the axis, where Q is the total charge uniformly distributed on the ring. |   |
| Charged Disc |   | $\mathbf {E} ={\frac {\sigma }{2\varepsilon _{0}}}\left[1-{\frac {x}{\sqrt {x^{2}+R^{2}}}}\right]{\hat {\mathbf {x} }},$ on the axis, where $\sigma$ is the uniform surface charge density. |   |
| Electric Dipole |   | $\mathbf {E} =-{\frac {\mathbf {p} }{4\pi \varepsilon _{0}r^{3}}},$ on the equatorial plane, where $\mathbf {p}$ is the electric dipole moment. | $\mathbf {E} ={\frac {\mathbf {p} }{2\pi \varepsilon _{0}x^{3}}},$ on the axis (given that $x\gg d$ ), where x can also be negative to indicate position at the opposite direction on the axis, and $\mathbf {p}$ is the electric dipole moment. |

Electric field infinitely close to a conducting surface in electrostatic equilibrium having charge density $\sigma$ at that point is ${\textstyle {\frac {\sigma }{\varepsilon _{0}}}{\hat {\mathbf {x} }}}$ since charges are only formed on the surface and the surface at the infinitesimal scale resembles an infinite 2D plane. In the absence of external fields, spherical conductors exhibit a uniform charge distribution on the surface and hence have the same electric field as that of uniform spherical surface distribution.
