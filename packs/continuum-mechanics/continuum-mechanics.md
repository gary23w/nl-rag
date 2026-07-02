---
title: "Continuum mechanics"
source: https://en.wikipedia.org/wiki/Continuum_mechanics
domain: continuum-mechanics
license: CC-BY-SA-4.0
tags: continuum mechanics, stress tensor, constitutive equation, deformation gradient
fetched: 2026-07-02
---

# Continuum mechanics

**Continuum mechanics** is a branch of mechanics that deals with the deformation of and transmission of forces through materials modeled as a ***continuous medium*** (also called a ***continuum***) rather than as discrete particles.

Continuum mechanics deals with *deformable bodies*, as opposed to rigid bodies. A continuum model assumes that the substance of the object completely fills the space it occupies. While ignoring the fact that matter is made of atoms, this provides a sufficiently accurate description of matter on length scales much greater than that of inter-atomic distances. The concept of a continuous medium allows for intuitive analysis of bulk matter by using differential equations that describe the behavior of such matter according to physical laws, such as mass conservation, momentum conservation, and energy conservation. Information about the specific material is expressed in constitutive relationships.

Continuum mechanics treats the physical properties of solids and fluids independently of any particular coordinate system in which they are observed. These properties are represented by tensors, which are mathematical objects with the salient property of being independent of coordinate systems. This permits definition of physical properties at any point in the continuum, according to mathematically convenient continuous functions. The theories of elasticity, plasticity and fluid mechanics are based on the concepts of continuum mechanics.

## Concept of a continuum

The concept of a continuum underlies the mathematical framework for studying large-scale forces and deformations in materials. Although materials are composed of discrete atoms and molecules, separated by empty space or microscopic cracks and crystallographic defects, physical phenomena can often be modeled by considering a substance distributed throughout some region of space. A continuum is a body that can be continually sub-divided into infinitesimal elements with local material properties defined at any particular point. Properties of the bulk material can therefore be described by almost everywhere smooth functions of position in the continuum, and their evolution with time can be studied using calculus.

Apart from the assumption of continuity, two other independent assumptions are often employed in the study of continuum mechanics. These are homogeneity (assumption of identical properties at all locations) and isotropy (assumption of directionally invariant vector properties). If these auxiliary assumptions are not globally applicable, the material may be segregated into sections where they are applicable in order to simplify the analysis. For more complex cases, one or both of these assumptions can be dropped. In these cases, computational methods are often used to solve the differential equations describing the evolution of material properties.

## Major areas

| **Continuum mechanics** The study of the physics of continuous materials | Solid mechanics The study of the physics of continuous materials with a defined rest shape. | Elasticity Describes materials that return to their rest shape after applied stresses are removed. |
|---|---|---|
| Plasticity Describes materials that permanently deform after a sufficient applied stress. | Rheology The study of materials with both solid and fluid characteristics. |   |
| Fluid mechanics The study of the physics of continuous materials which deform when subjected to a force. | Non-Newtonian fluid Do not undergo strain rates proportional to the applied shear stress. |   |
| Newtonian fluids undergo strain rates proportional to the applied shear stress. |   |   |

An additional area of continuum mechanics comprises elastomeric foams, which exhibit a curious hyperbolic stress-strain relationship. The elastomer is a true continuum, but a homogeneous distribution of voids gives it unusual properties.

## Formulation of models

Continuum mechanics models begin by assigning a region in three-dimensional Euclidean space to the material body ${\mathcal {B}}$ being modeled. The points within this region are called particles or material points. Different *configurations* or states of the body correspond to different regions in Euclidean space. The region corresponding to the body's configuration at time t is labeled $\kappa _{t}({\mathcal {B}})$ .

A particular particle within the body in a particular configuration is characterized by a position vector

$\mathbf {x} =\sum _{i=1}^{3}x_{i}\mathbf {e} _{i},$

where $\mathbf {e} _{i}$ are the coordinate vectors in some frame of reference chosen for the problem (See figure 1). This vector can be expressed as a function of the particle position $\mathbf {X}$ in some *reference configuration*, for example the configuration at the initial time, so that

$\mathbf {x} =\kappa _{t}(\mathbf {X} ).$

This function needs to have various properties so that the model makes physical sense. $\kappa _{t}(\cdot )$ needs to be:

- continuous in time, so that the body changes in a way which is realistic,
- globally invertible at all times, so that the body cannot intersect itself,
- orientation-preserving, as transformations which produce mirror reflections are not possible in nature.

For the mathematical formulation of the model, $\kappa _{t}(\cdot )$ is also assumed to be twice continuously differentiable, so that differential equations describing the motion may be formulated.

## Forces in a continuum

A solid is a deformable body that possesses shear strength, *sc.* a solid can support shear forces (forces parallel to the material surface on which they act). Fluids, on the other hand, do not sustain shear forces.

Following the classical dynamics of Isaac Newton and Leonhard Euler, the motion of a material body is produced by the action of externally applied forces which are assumed to be of two kinds: surface forces $\mathbf {F} _{C}$ and body forces $\mathbf {F} _{B}$ . Thus, the total force ${\mathcal {F}}$ applied to a body or to a portion of the body can be expressed as:

${\mathcal {F}}=\mathbf {F} _{C}+\mathbf {F} _{B}$

### Surface forces

*Surface forces* or *contact forces*, expressed as force per unit area, can act either on the bounding surface of the body, as a result of mechanical contact with other bodies, or on imaginary internal surfaces that bound portions of the body, as a result of the mechanical interaction between the parts of the body to either side of the surface (Euler-Cauchy's stress principle). When a body is acted upon by external contact forces, internal contact forces are then transmitted from point to point inside the body to balance their action, according to Newton's third law of motion of conservation of linear momentum and angular momentum (for continuous bodies these laws are called the Euler's equations of motion). The internal contact forces are related to the body's deformation through constitutive equations. The internal contact forces may be mathematically described by how they relate to the motion of the body, independent of the body's material makeup.

The distribution of internal contact forces throughout the volume of the body is assumed to be continuous. Therefore, there exists a *contact force density* or *Cauchy traction field* $\mathbf {T} (\mathbf {n} ,\mathbf {x} ,t)$ that represents this distribution in a particular configuration of the body at a given time $t\,\!$ . It is not a vector field because it depends not only on the position $\mathbf {x}$ of a particular material point, but also on the local orientation of the surface element as defined by its normal vector $\mathbf {n}$ .

Any differential area $dS\,\!$ with normal vector $\mathbf {n}$ of a given internal surface area $S\,\!$ , bounding a portion of the body, experiences a contact force $d\mathbf {F} _{C}\,\!$ arising from the contact between both portions of the body on each side of $S\,\!$ , and it is given by

$d\mathbf {F} _{C}=\mathbf {T} ^{(\mathbf {n} )}\,dS$

where $\mathbf {T} ^{(\mathbf {n} )}$ is the *surface traction*, also called *stress vector*, *traction*, or *traction vector*. The stress vector is a frame-indifferent vector (see Euler-Cauchy's stress principle).

The total contact force on the particular internal surface $S\,\!$ is then expressed as the sum (surface integral) of the contact forces on all differential surfaces $dS\,\!$ :

$\mathbf {F} _{C}=\int _{S}\mathbf {T} ^{(\mathbf {n} )}\,dS$

In continuum mechanics a body is considered stress-free if the only forces present are those inter-atomic forces (ionic, metallic, and van der Waals forces) required to hold the body together and to keep its shape in the absence of all external influences, including gravitational attraction. Stresses generated during manufacture of the body to a specific configuration are also excluded when considering stresses in a body. Therefore, the stresses considered in continuum mechanics are only those produced by deformation of the body, *sc.* only relative changes in stress are considered, not the absolute values of stress.

### Body forces

*Body forces* are forces originating from sources outside of the body that act on the volume (or mass) of the body. Saying that body forces are due to outside sources implies that the interaction between different parts of the body (internal forces) are manifested through the contact forces alone. These forces arise from the presence of the body in force fields, *e.g.* gravitational field (gravitational forces) or electromagnetic field (electromagnetic forces), or from inertial forces when bodies are in motion. As the mass of a continuous body is assumed to be continuously distributed, any force originating from the mass is also continuously distributed. Thus, body forces are specified by vector fields which are assumed to be continuous over the entire volume of the body, *i.e.* acting on every point in it. Body forces are represented by a body force density $\mathbf {b} (\mathbf {x} ,t)$ (per unit of mass), which is a frame-indifferent vector field.

In the case of gravitational forces, the intensity of the force depends on, or is proportional to, the mass density $\mathbf {\rho } (\mathbf {x} ,t)\,\!$ of the material, and it is specified in terms of force per unit mass ( $b_{i}\,\!$ ) or per unit volume ( $p_{i}\,\!$ ). These two specifications are related through the material density by the equation $\rho b_{i}=p_{i}\,\!$ . Similarly, the intensity of electromagnetic forces depends upon the strength (electric charge) of the electromagnetic field.

The total body force applied to a continuous body is expressed as

$\mathbf {F} _{B}=\int _{V}\mathbf {b} \,dm=\int _{V}\rho \mathbf {b} \,dV$

Body forces and contact forces acting on the body lead to corresponding moments of force (torques) relative to a given point. Thus, the total applied torque ${\mathcal {M}}$ about the origin is given by

${\mathcal {M}}=\mathbf {M} _{C}+\mathbf {M} _{B}$

In certain situations, not commonly considered in the analysis of the mechanical behavior of materials, it becomes necessary to include two other types of forces: these are *couple stresses* (surface couples, contact torques) and *body moments*. Couple stresses are moments per unit area applied on a surface. Body moments, or body couples, are moments per unit volume or per unit mass applied to the volume of the body. Both are important in the analysis of stress for a polarized dielectric solid under the action of an electric field, materials where the molecular structure is taken into consideration (*e.g.* bones), solids under the action of an external magnetic field, and the dislocation theory of metals.

Materials that exhibit body couples and couple stresses in addition to moments produced exclusively by forces are called *polar materials*. *Non-polar materials* are then those materials with only moments of forces. In the classical branches of continuum mechanics the development of the theory of stresses is based on non-polar materials.

Thus, the sum of all applied forces and torques (with respect to the origin of the coordinate system) in the body can be given by

${\mathcal {F}}=\int _{V}\mathbf {a} \,dm=\int _{S}\mathbf {T} \,dS+\int _{V}\rho \mathbf {b} \,dV$

${\mathcal {M}}=\int _{S}\mathbf {r} \times \mathbf {T} \,dS+\int _{V}\mathbf {r} \times \rho \mathbf {b} \,dV$

## Kinematics: motion and deformation

A change in the configuration of a continuum body results in a displacement. The displacement of a body has two components: a rigid-body displacement and a deformation. A rigid-body displacement consists of a simultaneous translation and rotation of the body without changing its shape or size. Deformation implies the change in shape and/or size of the body from an initial or undeformed configuration $\kappa _{0}({\mathcal {B}})$ to a current or deformed configuration $\kappa _{t}({\mathcal {B}})$ (Figure 2).

The motion of a continuum body is a continuous time sequence of displacements. Thus, the material body will occupy different configurations at different times so that a particle occupies a series of points in space which describe a path line.

There is continuity during motion or deformation of a continuum body in the sense that:

- The material points forming a closed curve at any instant will always form a closed curve at any subsequent time.
- The material points forming a closed surface at any instant will always form a closed surface at any subsequent time and the matter within the closed surface will always remain within.

It is convenient to identify a reference configuration or initial condition which all subsequent configurations are referenced from. The reference configuration need not be one that the body will ever occupy. Often, the configuration at $t=0$ is considered the reference configuration, $\kappa _{0}({\mathcal {B}})$ . The components $X_{i}$ of the position vector $\mathbf {X}$ of a particle, taken with respect to the reference configuration, are called the material or reference coordinates.

When analyzing the motion or deformation of solids, or the flow of fluids, it is necessary to describe the sequence or evolution of configurations throughout time. One description for motion is made in terms of the material or referential coordinates, called material description or Lagrangian description.

### Lagrangian description

In the Lagrangian description the position and physical properties of the particles are described in terms of the material or referential coordinates and time. In this case **the reference configuration is the configuration at $t=0$**. An observer standing in the frame of reference observes the changes in the position and physical properties as the material body moves in space as time progresses. The results obtained are independent of the choice of initial time and reference configuration, $\kappa _{0}({\mathcal {B}})$ . This description is normally used in solid mechanics.

In the Lagrangian description, the motion of a continuum body is expressed by the mapping function $\chi (\cdot )$ (Figure 2),

$\mathbf {x} =\chi (\mathbf {X} ,t)$

which is a mapping of the initial configuration $\kappa _{0}({\mathcal {B}})$ onto the current configuration $\kappa _{t}({\mathcal {B}})$ , giving a geometrical correspondence between them, i.e. giving the position vector $\mathbf {x} =x_{i}\mathbf {e} _{i}$ that a particle X , with a position vector $\mathbf {X}$ in the undeformed or reference configuration $\kappa _{0}({\mathcal {B}})$ , will occupy in the current or deformed configuration $\kappa _{t}({\mathcal {B}})$ at time t . The components $x_{i}$ are called the spatial coordinates.

Physical and kinematic properties $P_{ij\ldots }$ , i.e. thermodynamic properties and flow velocity, which describe or characterize features of the material body, are expressed as continuous functions of position and time, i.e. $P_{ij\ldots }=P_{ij\ldots }(\mathbf {X} ,t)$ .

The material derivative of any property $P_{ij\ldots }$ of a continuum, which may be a scalar, vector, or tensor, is the time rate of change of that property for a specific group of particles of the moving continuum body. The material derivative is also known as the *substantial derivative*, or *comoving derivative*, or *convective derivative*. It can be thought as the rate at which the property changes when measured by an observer traveling with that group of particles.

In the Lagrangian description, the material derivative of $P_{ij\ldots }$ is simply the partial derivative with respect to time, and the position vector $\mathbf {X}$ is held constant as it does not change with time. Thus, we have

${\frac {d}{dt}}[P_{ij\ldots }(\mathbf {X} ,t)]={\frac {\partial }{\partial t}}[P_{ij\ldots }(\mathbf {X} ,t)]$

The instantaneous position $\mathbf {x}$ is a property of a particle, and its material derivative is the *instantaneous flow velocity* $\mathbf {v}$ of the particle. Therefore, the flow velocity field of the continuum is given by

$\mathbf {v} ={\dot {\mathbf {x} }}={\frac {d\mathbf {x} }{dt}}={\frac {\partial \chi (\mathbf {X} ,t)}{\partial t}}$

Similarly, the acceleration field is given by

$\mathbf {a} ={\dot {\mathbf {v} }}={\ddot {\mathbf {x} }}={\frac {d^{2}\mathbf {x} }{dt^{2}}}={\frac {\partial ^{2}\chi (\mathbf {X} ,t)}{\partial t^{2}}}$

Continuity in the Lagrangian description is expressed by the spatial and temporal continuity of the mapping from the reference configuration to the current configuration of the material points. All physical quantities characterizing the continuum are described this way. In this sense, the function $\chi (\cdot )$ and $P_{ij\ldots }(\cdot )$ are single-valued and continuous, with continuous derivatives with respect to space and time to whatever order is required, usually to the second or third.

### Eulerian description

Continuity allows for the inverse of $\chi (\cdot )$ to trace backwards where the particle currently located at $\mathbf {x}$ was located in the initial or referenced configuration $\kappa _{0}({\mathcal {B}})$ . In this case the description of motion is made in terms of the spatial coordinates, in which case is called the spatial description or Eulerian description, i.e. **the current configuration is taken as the reference configuration**.

The Eulerian description, focuses on the current configuration $\kappa _{t}({\mathcal {B}})$ , giving attention to what is occurring at a fixed point in space as time progresses, instead of giving attention to individual particles as they move through space and time. This approach is conveniently applied in the study of fluid flow where the kinematic property of greatest interest is the rate at which change is taking place rather than the shape of the body of fluid at a reference time.

Mathematically, the motion of a continuum using the Eulerian description is expressed by the mapping function

$\mathbf {X} =\chi ^{-1}(\mathbf {x} ,t)$

which provides a tracing of the particle which now occupies the position $\mathbf {x}$ in the current configuration $\kappa _{t}({\mathcal {B}})$ to its original position $\mathbf {X}$ in the initial configuration $\kappa _{0}({\mathcal {B}})$ .

A necessary and sufficient condition for this inverse function to exist is that the determinant of the Jacobian matrix, often referred to simply as the Jacobian, should be different from zero. Thus,

$J=\left|{\frac {\partial \chi _{i}}{\partial X_{J}}}\right|=\left|{\frac {\partial x_{i}}{\partial X_{J}}}\right|\neq 0$

In the Eulerian description, the physical properties $P_{ij\ldots }$ are expressed as

$P_{ij\ldots }=P_{ij\ldots }(\mathbf {X} ,t)=P_{ij\ldots }[\chi ^{-1}(\mathbf {x} ,t),t]=p_{ij\ldots }(\mathbf {x} ,t)$

where the functional form of $P_{ij\ldots }$ in the Lagrangian description is not the same as the form of $p_{ij\ldots }$ in the Eulerian description.

The material derivative of $p_{ij\ldots }(\mathbf {x} ,t)$ , using the chain rule, is then

${\frac {d}{dt}}[p_{ij\ldots }(\mathbf {x} ,t)]={\frac {\partial }{\partial t}}[p_{ij\ldots }(\mathbf {x} ,t)]+{\frac {\partial }{\partial x_{k}}}[p_{ij\ldots }(\mathbf {x} ,t)]{\frac {dx_{k}}{dt}}$

The first term on the right-hand side of this equation gives the *local rate of change* of the property $p_{ij\ldots }(\mathbf {x} ,t)$ occurring at position $\mathbf {x}$ . The second term of the right-hand side is the *convective rate of change* and expresses the contribution of the particle changing position in space (motion).

Continuity in the Eulerian description is expressed by the spatial and temporal continuity and continuous differentiability of the flow velocity field. All physical quantities are defined this way at each instant of time, in the current configuration, as a function of the vector position $\mathbf {x}$ .

### Displacement field

The vector joining the positions of a particle P in the undeformed configuration and deformed configuration is called the displacement vector $\mathbf {u} (\mathbf {X} ,t)=u_{i}\mathbf {e} _{i}$ , in the Lagrangian description, or $\mathbf {U} (\mathbf {x} ,t)=U_{J}\mathbf {E} _{J}$ , in the Eulerian description.

A *displacement field* is a vector field of all displacement vectors for all particles in the body, which relates the deformed configuration with the undeformed configuration. It is convenient to do the analysis of deformation or motion of a continuum body in terms of the displacement field, In general, the displacement field is expressed in terms of the material coordinates as

$\mathbf {u} (\mathbf {X} ,t)=\mathbf {b} +\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=\alpha _{iJ}b_{J}+x_{i}-\alpha _{iJ}X_{J}$

or in terms of the spatial coordinates as

$\mathbf {U} (\mathbf {x} ,t)=\mathbf {b} +\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=b_{J}+\alpha _{Ji}x_{i}-X_{J}\,$

where $\alpha _{Ji}$ are the direction cosines between the material and spatial coordinate systems with unit vectors $\mathbf {E} _{J}$ and $\mathbf {e} _{i}$ , respectively. Thus

$\mathbf {E} _{J}\cdot \mathbf {e} _{i}=\alpha _{Ji}=\alpha _{iJ}$

and the relationship between $u_{i}$ and $U_{J}$ is then given by

$u_{i}=\alpha _{iJ}U_{J}\qquad {\text{or}}\qquad U_{J}=\alpha _{Ji}u_{i}$

Knowing that

$\mathbf {e} _{i}=\alpha _{iJ}\mathbf {E} _{J}$

then

$\mathbf {u} (\mathbf {X} ,t)=u_{i}\mathbf {e} _{i}=u_{i}(\alpha _{iJ}\mathbf {E} _{J})=U_{J}\mathbf {E} _{J}=\mathbf {U} (\mathbf {x} ,t)$

It is common to superimpose the coordinate systems for the undeformed and deformed configurations, which results in $\mathbf {b} =0$ , and the direction cosines become Kronecker deltas, i.e.

$\mathbf {E} _{J}\cdot \mathbf {e} _{i}=\delta _{Ji}=\delta _{iJ}$

Thus, we have

$\mathbf {u} (\mathbf {X} ,t)=\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=x_{i}-\delta _{iJ}X_{J}$

or in terms of the spatial coordinates as

$\mathbf {U} (\mathbf {x} ,t)=\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=\delta _{Ji}x_{i}-X_{J}$

## Governing equations

Continuum mechanics deals with the behavior of materials that can be approximated as continuous for certain length and time scales. The equations that govern the mechanics of such materials include the balance laws for mass, momentum, and energy. Kinematic relations and constitutive equations are needed to complete the system of governing equations. Physical restrictions on the form of the constitutive relations can be applied by requiring that the second law of thermodynamics be satisfied under all conditions. In the continuum mechanics of solids, the second law of thermodynamics is satisfied if the Clausius–Duhem form of the entropy inequality is satisfied.

The balance laws express the idea that the rate of change of a quantity (mass, momentum, energy) in a volume must arise from three causes:

1. the physical quantity itself flows through the surface that bounds the volume,
2. there is a source of the physical quantity on the surface of the volume, or/and,
3. there is a source of the physical quantity inside the volume.

Let $\Omega$ be the body (an open subset of Euclidean space) and let $\partial \Omega$ be its surface (the boundary of $\Omega$ ).

Let the motion of material points in the body be described by the map

$\mathbf {x} ={\boldsymbol {\chi }}(\mathbf {X} )=\mathbf {x} (\mathbf {X} )$

where $\mathbf {X}$ is the position of a point in the initial configuration and $\mathbf {x}$ is the location of the same point in the deformed configuration.

The deformation gradient is given by

${\boldsymbol {F}}={\frac {\partial \mathbf {x} }{\partial \mathbf {X} }}=\nabla \mathbf {x} ~.$

### Balance laws

Let $f(\mathbf {x} ,t)$ be a physical quantity that is flowing through the body. Let $g(\mathbf {x} ,t)$ be sources on the surface of the body and let $h(\mathbf {x} ,t)$ be sources inside the body. Let $\mathbf {n} (\mathbf {x} ,t)$ be the outward unit normal to the surface $\partial \Omega$ . Let $\mathbf {v} (\mathbf {x} ,t)$ be the flow velocity of the physical particles that carry the physical quantity that is flowing. Also, let the speed at which the bounding surface $\partial \Omega$ is moving be $u_{n}$ (in the direction $\mathbf {n}$ ).

Then, balance laws can be expressed in the general form

${\cfrac {d}{dt}}\left[\int _{\Omega }f(\mathbf {x} ,t)~{\text{dV}}\right]=\int _{\partial \Omega }f(\mathbf {x} ,t)[u_{n}(\mathbf {x} ,t)-\mathbf {v} (\mathbf {x} ,t)\cdot \mathbf {n} (\mathbf {x} ,t)]~{\text{dA}}+\int _{\partial \Omega }g(\mathbf {x} ,t)~{\text{dA}}+\int _{\Omega }h(\mathbf {x} ,t)~{\text{dV}}~.$

The functions $f(\mathbf {x} ,t)$ , $g(\mathbf {x} ,t)$ , and $h(\mathbf {x} ,t)$ can be scalar valued, vector valued, or tensor valued - depending on the physical quantity that the balance equation deals with. If there are internal boundaries in the body, jump discontinuities also need to be specified in the balance laws.

If we take the Eulerian point of view, it can be shown that the balance laws of mass, momentum, and energy for a solid can be written as (assuming the source term is zero for the mass and angular momentum equations)

${\begin{aligned}{\dot {\rho }}+\rho ({\boldsymbol {\nabla }}\cdot \mathbf {v} )&=0&&\qquad {\text{Balance of Mass}}\\\rho ~{\dot {\mathbf {v} }}-{\boldsymbol {\nabla }}\cdot {\boldsymbol {\sigma }}-\rho ~\mathbf {b} &=0&&\qquad {\text{Balance of Linear Momentum (Cauchy's first law of motion)}}\\{\boldsymbol {\sigma }}&={\boldsymbol {\sigma }}^{T}&&\qquad {\text{Balance of Angular Momentum (Cauchy's second law of motion)}}\\\rho ~{\dot {e}}-{\boldsymbol {\sigma }}:({\boldsymbol {\nabla }}\mathbf {v} )+{\boldsymbol {\nabla }}\cdot \mathbf {q} -\rho ~s&=0&&\qquad {\text{Balance of Energy.}}\end{aligned}}$

In the above equations $\rho (\mathbf {x} ,t)$ is the mass density (current), ${\dot {\rho }}$ is the material time derivative of $\rho$ , $\mathbf {v} (\mathbf {x} ,t)$ is the particle velocity, ${\dot {\mathbf {v} }}$ is the material time derivative of $\mathbf {v}$ , ${\boldsymbol {\sigma }}(\mathbf {x} ,t)$ is the Cauchy stress tensor, $\mathbf {b} (\mathbf {x} ,t)$ is the body force density, $e(\mathbf {x} ,t)$ is the internal energy per unit mass, ${\dot {e}}$ is the material time derivative of e , $\mathbf {q} (\mathbf {x} ,t)$ is the heat flux vector, and $s(\mathbf {x} ,t)$ is an energy source per unit mass. The operators used are defined below.

With respect to the reference configuration (the Lagrangian point of view), the balance laws can be written as

${\begin{aligned}\rho ~\det({\boldsymbol {F}})-\rho _{0}&=0&&\qquad {\text{Balance of Mass}}\\\rho _{0}~{\ddot {\mathbf {x} }}-{\boldsymbol {\nabla }}_{\circ }\cdot {\boldsymbol {P}}-\rho _{0}~\mathbf {b} &=0&&\qquad {\text{Balance of Linear Momentum}}\\{\boldsymbol {F}}\cdot {\boldsymbol {P}}^{T}&={\boldsymbol {P}}\cdot {\boldsymbol {F}}^{T}&&\qquad {\text{Balance of Angular Momentum}}\\\rho _{0}~{\dot {e}}-{\boldsymbol {P}}:{\dot {\boldsymbol {F}}}+{\boldsymbol {\nabla }}_{\circ }\cdot \mathbf {q} -\rho _{0}~s&=0&&\qquad {\text{Balance of Energy.}}\end{aligned}}$

In the above, ${\boldsymbol {P}}$ is the first Piola-Kirchhoff stress tensor, and $\rho _{0}$ is the mass density in the reference configuration. The first Piola-Kirchhoff stress tensor is related to the Cauchy stress tensor by

${\boldsymbol {P}}=J~{\boldsymbol {\sigma }}\cdot {\boldsymbol {F}}^{-T}~{\text{where}}~J=\det({\boldsymbol {F}})$

We can alternatively define the nominal stress tensor ${\boldsymbol {N}}$ which is the transpose of the first Piola-Kirchhoff stress tensor such that

${\boldsymbol {N}}={\boldsymbol {P}}^{T}=J~{\boldsymbol {F}}^{-1}\cdot {\boldsymbol {\sigma }}~.$

Then the balance laws become

${\begin{aligned}\rho ~\det({\boldsymbol {F}})-\rho _{0}&=0&&\qquad {\text{Balance of Mass}}\\\rho _{0}~{\ddot {\mathbf {x} }}-{\boldsymbol {\nabla }}_{\circ }\cdot {\boldsymbol {N}}^{T}-\rho _{0}~\mathbf {b} &=0&&\qquad {\text{Balance of Linear Momentum}}\\{\boldsymbol {F}}\cdot {\boldsymbol {N}}&={\boldsymbol {N}}^{T}\cdot {\boldsymbol {F}}^{T}&&\qquad {\text{Balance of Angular Momentum}}\\\rho _{0}~{\dot {e}}-{\boldsymbol {N}}^{T}:{\dot {\boldsymbol {F}}}+{\boldsymbol {\nabla }}_{\circ }\cdot \mathbf {q} -\rho _{0}~s&=0&&\qquad {\text{Balance of Energy.}}\end{aligned}}$

#### Operators

The operators in the above equations are defined as

${\begin{aligned}{\boldsymbol {\nabla }}\mathbf {v} &=\sum _{i,j=1}^{3}{\frac {\partial v_{i}}{\partial x_{j}}}\mathbf {e} _{i}\otimes \mathbf {e} _{j}=v_{i,j}\mathbf {e} _{i}\otimes \mathbf {e} _{j}~;\\[1ex]{\boldsymbol {\nabla }}\cdot \mathbf {v} &=\sum _{i=1}^{3}{\frac {\partial v_{i}}{\partial x_{i}}}=v_{i,i}~;\\[1ex]{\boldsymbol {\nabla }}\cdot {\boldsymbol {S}}&=\sum _{i,j=1}^{3}{\frac {\partial S_{ij}}{\partial x_{j}}}~\mathbf {e} _{i}=\sigma _{ij,j}~\mathbf {e} _{i}~.\end{aligned}}$

where $\mathbf {v}$ is a vector field, ${\boldsymbol {S}}$ is a second-order tensor field, and $\mathbf {e} _{i}$ are the components of an orthonormal basis in the current configuration. Also,

${\begin{aligned}{\boldsymbol {\nabla }}_{\circ }\mathbf {v} &=\sum _{i,j=1}^{3}{\frac {\partial v_{i}}{\partial X_{j}}}\mathbf {E} _{i}\otimes \mathbf {E} _{j}=v_{i,j}\mathbf {E} _{i}\otimes \mathbf {E} _{j}~;\\[1ex]{\boldsymbol {\nabla }}_{\circ }\cdot \mathbf {v} &=\sum _{i=1}^{3}{\frac {\partial v_{i}}{\partial X_{i}}}=v_{i,i}~;\\[1ex]{\boldsymbol {\nabla }}_{\circ }\cdot {\boldsymbol {S}}&=\sum _{i,j=1}^{3}{\frac {\partial S_{ij}}{\partial X_{j}}}~\mathbf {E} _{i}=S_{ij,j}~\mathbf {E} _{i}\end{aligned}}$

where $\mathbf {v}$ is a vector field, ${\boldsymbol {S}}$ is a second-order tensor field, and $\mathbf {E} _{i}$ are the components of an orthonormal basis in the reference configuration.

The inner product is defined as

${\boldsymbol {A}}:{\boldsymbol {B}}=\sum _{i,j=1}^{3}A_{ij}~B_{ij}=\operatorname {trace} ({\boldsymbol {A}}{\boldsymbol {B}}^{T})~.$

### Clausius–Duhem inequality

The Clausius–Duhem inequality can be used to express the second law of thermodynamics for elastic-plastic materials. This inequality is a statement concerning the irreversibility of natural processes, especially when energy dissipation is involved.

Just like in the balance laws in the previous section, we assume that there is a flux of a quantity, a source of the quantity, and an internal density of the quantity per unit mass. The quantity of interest in this case is the entropy. Thus, we assume that there is an entropy flux, an entropy source, an internal mass density $\rho$ and an internal specific entropy (i.e. entropy per unit mass) $\eta$ in the region of interest.

Let $\Omega$ be such a region and let $\partial \Omega$ be its boundary. Then the second law of thermodynamics states that the rate of increase of $\eta$ in this region is greater than or equal to the sum of that supplied to $\Omega$ (as a flux or from internal sources) and the change of the internal entropy density $\rho \eta$ due to material flowing in and out of the region.

Let $\partial \Omega$ move with a flow velocity $u_{n}$ and let particles inside $\Omega$ have velocities $\mathbf {v}$ . Let $\mathbf {n}$ be the unit outward normal to the surface $\partial \Omega$ . Let $\rho$ be the density of matter in the region, ${\bar {q}}$ be the entropy flux at the surface, and r be the entropy source per unit mass. Then the entropy inequality may be written as

${\cfrac {d}{dt}}\left(\int _{\Omega }\rho ~\eta ~{\text{dV}}\right)\geq \int _{\partial \Omega }\rho ~\eta ~(u_{n}-\mathbf {v} \cdot \mathbf {n} )~{\text{dA}}+\int _{\partial \Omega }{\bar {q}}~{\text{dA}}+\int _{\Omega }\rho ~r~{\text{dV}}.$

The scalar entropy flux can be related to the vector flux at the surface by the relation ${\bar {q}}=-{\boldsymbol {\psi }}(\mathbf {x} )\cdot \mathbf {n}$ . Under the assumption of incrementally isothermal conditions, we have

${\boldsymbol {\psi }}(\mathbf {x} )={\cfrac {\mathbf {q} (\mathbf {x} )}{T}}~;~~r={\cfrac {s}{T}}$

where $\mathbf {q}$ is the heat flux vector, s is an energy source per unit mass, and T is the absolute temperature of a material point at $\mathbf {x}$ at time t .

We then have the Clausius–Duhem inequality in integral form:

${{\cfrac {d}{dt}}\left(\int _{\Omega }\rho ~\eta ~{\text{dV}}\right)\geq \int _{\partial \Omega }\rho ~\eta ~(u_{n}-\mathbf {v} \cdot \mathbf {n} )~{\text{dA}}-\int _{\partial \Omega }{\cfrac {\mathbf {q} \cdot \mathbf {n} }{T}}~{\text{dA}}+\int _{\Omega }{\cfrac {\rho ~s}{T}}~{\text{dV}}.}$

We can show that the entropy inequality may be written in differential form as

${\rho ~{\dot {\eta }}\geq -{\boldsymbol {\nabla }}\cdot \left({\cfrac {\mathbf {q} }{T}}\right)+{\cfrac {\rho ~s}{T}}.}$

In terms of the Cauchy stress and the internal energy, the Clausius–Duhem inequality may be written as

${\rho ~({\dot {e}}-T~{\dot {\eta }})-{\boldsymbol {\sigma }}:{\boldsymbol {\nabla }}\mathbf {v} \leq -{\cfrac {\mathbf {q} \cdot {\boldsymbol {\nabla }}T}{T}}.}$

## Validity

The validity of the continuum assumption may be verified by a theoretical analysis, in which either some clear periodicity is identified or statistical homogeneity and ergodicity of the microstructure exist. More specifically, the continuum hypothesis hinges on the concepts of a representative elementary volume and separation of scales based on the Hill–Mandel condition. This condition provides a link between an experimentalist's and a theoretician's viewpoint on constitutive equations (linear and nonlinear elastic/inelastic or coupled fields) as well as a way of spatial and statistical averaging of the microstructure. When the separation of scales does not hold, or when one wants to establish a continuum of a finer resolution than the size of the representative volume element (RVE), a statistical volume element (SVE) is employed, which results in random continuum fields. The latter then provide a micromechanics basis for stochastic finite elements (SFE). The levels of SVE and RVE link continuum mechanics to statistical mechanics. Experimentally, the RVE can only be evaluated when the constitutive response is spatially homogenous.

## Applications

- Continuum mechanics
  - Solid mechanics
  - Fluid mechanics
- Engineering
  - Civil engineering
  - Mechanical engineering
  - Aerospace engineering
  - Biomedical engineering
  - Chemical engineering
