---
title: "Gauss's law"
source: https://en.wikipedia.org/wiki/Gauss's_law
domain: maxwell-equations
license: CC-BY-SA-4.0
tags: maxwell's equations, gauss's law, displacement current, electromagnetic wave equation
fetched: 2026-07-02
---

# Gauss's law

In electromagnetism, **Gauss's law**, also known as **Gauss's flux theorem** or sometimes **Gauss's theorem**, is one of Maxwell's equations. It is an application of the divergence theorem, and it relates the distribution of electric charge to the resulting electric field.

## Definition

In its integral form, it states that the flux of the electric field out of an arbitrary closed surface is proportional to the electric charge enclosed by the surface, irrespective of how that charge is distributed. Even though the law alone is insufficient to determine the electric field across a surface enclosing any charge distribution, this may be possible in cases where symmetry mandates uniformity of the field. Where no such symmetry exists, Gauss's law can be used in its differential form, which states that the divergence of the electric field is proportional to the local density of charge.

The law was first formulated by Joseph-Louis Lagrange in 1773, followed by Carl Friedrich Gauss in 1835, both in the context of the attraction of ellipsoids. It is one of Maxwell's equations, which forms the basis of classical electrodynamics. Gauss's law can be used to derive Coulomb's law, and vice versa.

## Qualitative description

In words, Gauss's law states:

The net

electric flux

through any hypothetical

closed surface

is equal to

1/

ε

0

times the net

electric charge

enclosed within that closed surface. The closed surface is also referred to as

Gaussian surface

.

Gauss's law has a close mathematical similarity with a number of laws in other areas of physics, such as Gauss's law for magnetism and Gauss's law for gravity. In fact, any inverse-square law can be formulated in a way similar to Gauss's law: for example, Gauss's law itself is essentially equivalent to Coulomb's law, and Gauss's law for gravity is essentially equivalent to Newton's law of gravity, both of which are inverse-square laws.

The law can be expressed mathematically using vector calculus in integral form and differential form; both are equivalent since they are related by the divergence theorem, also called Gauss's theorem. Each of these forms in turn can also be expressed two ways: In terms of a relation between the electric field **E** and the total electric charge, or in terms of the electric displacement field **D** and the *free* electric charge.

## Equation involving the E field

Gauss's law can be stated using either the electric field **E** or the electric displacement field **D**. This section shows some of the forms with **E**; the form with **D** is below, as are other forms with **E**.

### Integral form

Gauss's law may be expressed as:

$\Phi _{E}={\frac {Q}{\varepsilon _{0}}}$

where Φ*E* is the electric flux through a closed surface S enclosing any volume V, Q is the total charge enclosed within V, and *ε*0 is the electric constant. The electric flux Φ*E* is defined as a surface integral of the electric field:

$\Phi _{E}=$

$\scriptstyle _{S}$

$\mathbf {E} \cdot \mathrm {d} \mathbf {A}$

where **E** is the electric field, d**A** is a vector representing an infinitesimal element of area of the surface, and · represents the dot product of two vectors.

In a curved spacetime, the flux of an electromagnetic field through a closed surface is expressed as

$\Phi _{E}=c$

$\scriptstyle _{S}$

$F^{\kappa 0}{\sqrt {-g}}\,\mathrm {d} S_{\kappa }$

where c is the speed of light; $F^{\kappa 0}$ denotes the time components of the electromagnetic tensor; g is the determinant of metric tensor; $\mathrm {d} S_{\kappa }=\mathrm {d} S^{ij}=\mathrm {d} x^{i}\mathrm {d} x^{j}$ is an orthonormal element of the two-dimensional surface surrounding the charge Q ; indices $i,j,\kappa =1,2,3$ and do not match each other.

Since the flux is defined as an *integral* of the electric field, this expression of Gauss's law is called the *integral form*.

In problems involving conductors set at known potentials, the potential away from them is obtained by solving Laplace's equation, either analytically or numerically. The electric field is then calculated as the potential's negative gradient. Gauss's law makes it possible to find the distribution of electric charge: The charge in any given region of the conductor can be deduced by integrating the electric field to find the flux through a small box whose sides are perpendicular to the conductor's surface and by noting that the electric field is perpendicular to the surface, and zero inside the conductor.

The reverse problem, when the electric charge distribution is known and the electric field must be computed, is much more difficult. The total flux through a given surface gives little information about the electric field, and can go in and out of the surface in arbitrarily complicated patterns.

An exception is if there is some symmetry in the problem, which mandates that the electric field passes through the surface in a uniform way. Then, if the total flux is known, the field itself can be deduced at every point. Common examples of symmetries which lend themselves to Gauss's law include: cylindrical symmetry, planar symmetry, and spherical symmetry. See the article Gaussian surface for examples where these symmetries are exploited to compute electric fields.

### Differential form

By the divergence theorem, Gauss's law can alternatively be written in the *differential form*: $\nabla \cdot \mathbf {E} ={\frac {\rho }{\varepsilon _{0}}}$

where ∇ · **E** is the divergence of the electric field, *ε*0 is the vacuum permittivity and ρ is the total volume charge density (charge per unit volume).

### Equivalence of integral and differential forms

The integral and differential forms are mathematically equivalent, by the divergence theorem. Here is the argument more specifically.

Outline of proof

The integral form of Gauss's law is:

${\scriptstyle _{S}}$

$\mathbf {E} \cdot \mathrm {d} \mathbf {A}$

$={\frac {Q}{\varepsilon _{0}}}$

for any closed surface S containing charge Q. By the divergence theorem, this equation is equivalent to:

$\iiint _{V}\nabla \cdot \mathbf {E} \,\mathrm {d} V={\frac {Q}{\varepsilon _{0}}}$

for any volume V containing charge Q. By the relation between charge and charge density, this equation is equivalent to: $\iiint _{V}\nabla \cdot \mathbf {E} \,\mathrm {d} V=\iiint _{V}{\frac {\rho }{\varepsilon _{0}}}\,\mathrm {d} V$ for any volume V. In order for this equation to be *simultaneously true* for *every* possible volume V, it is necessary (and sufficient) for the integrands to be equal everywhere. Therefore, this equation is equivalent to:

$\nabla \cdot \mathbf {E} ={\frac {\rho }{\varepsilon _{0}}}.$ Thus the integral and differential forms are equivalent.

## Equation involving the D field

### Free, bound, and total charge

The electric charge that arises in the simplest textbook situations would be classified as "free charge"—for example, the charge which is transferred in static electricity, or the charge on a capacitor plate. In contrast, "bound charge" arises only in the context of dielectric (polarizable) materials. (All materials are polarizable to some extent.) When such materials are placed in an external electric field, the electrons remain bound to their respective atoms, but shift a microscopic distance in response to the field, so that they're more on one side of the atom than the other. All these microscopic displacements add up to give a macroscopic net charge distribution, and this constitutes the "bound charge".

Although microscopically all charge is fundamentally the same, there are often practical reasons for wanting to treat bound charge differently from free charge. The result is that the more fundamental Gauss's law, in terms of **E** (above), is sometimes put into the equivalent form below, which is in terms of **D** and the free charge only.

### Integral form

This formulation of Gauss's law states the total charge form:

$\Phi _{D}=Q_{\mathrm {free} }$

where Φ*D* is the **D**-field flux through a surface S which encloses a volume V, and *Q*free is the free charge contained in V. The flux Φ*D* is defined analogously to the flux Φ*E* of the electric field **E** through S:

$\Phi _{D}=$

${\scriptstyle _{S}}$

$\mathbf {D} \cdot \mathrm {d} \mathbf {A}$

### Differential form

The differential form of Gauss's law, involving free charge only, states: $\nabla \cdot \mathbf {D} =\rho _{\mathrm {free} }$

where ∇ · **D** is the divergence of the electric displacement field, and *ρ*free is the free electric charge density.

## Equivalence of total and free charge statements

Proof that the formulations of Gauss's law in terms of free charge are equivalent to the formulations involving total charge.

In this proof, we will show that the equation $\nabla \cdot \mathbf {E} ={\dfrac {\rho }{\varepsilon _{0}}}$ is equivalent to the equation $\nabla \cdot \mathbf {D} =\rho _{\mathrm {free} }$ Note that we are only dealing with the differential forms, not the integral forms, but that is sufficient since the differential and integral forms are equivalent in each case, by the divergence theorem.

We introduce the polarization density **P**, which has the following relation to **E** and **D**: $\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P}$ and the following relation to the bound charge: $\rho _{\mathrm {bound} }=-\nabla \cdot \mathbf {P}$ Now, consider the three equations: ${\begin{aligned}\rho _{\mathrm {bound} }&=\nabla \cdot (-\mathbf {P} )\\\rho _{\mathrm {free} }&=\nabla \cdot \mathbf {D} \\\rho &=\nabla \cdot (\varepsilon _{0}\mathbf {E} )\end{aligned}}$ The key insight is that the sum of the first two equations is the third equation. This completes the proof: The first equation is true by definition, and therefore the second equation is true if and only if the third equation is true. So the second and third equations are equivalent, which is what we wanted to prove.

## Equation for linear materials

In homogeneous, isotropic, nondispersive, linear materials, there is a simple relationship between **E** and **D**:

$\mathbf {D} =\varepsilon \mathbf {E}$

where ε is the permittivity of the material. For the case of vacuum (aka free space), *ε* = *ε*0. Under these circumstances, Gauss's law modifies to

$\Phi _{E}={\frac {Q_{\mathrm {free} }}{\varepsilon }}$

for the integral form, and

$\nabla \cdot \mathbf {E} ={\frac {\rho _{\mathrm {free} }}{\varepsilon }}$

for the differential form.

## Relation to Coulomb's law

### Deriving Gauss's law from Coulomb's law

Strictly speaking, Gauss's law cannot be derived from Coulomb's law alone, since Coulomb's law gives the electric field due to an individual, electrostatic point charge only. However, Gauss's law *can* be proven from Coulomb's law if it is assumed, in addition, that the electric field obeys the superposition principle. The superposition principle states that the resulting field is the vector sum of fields generated by each particle (or the integral, if the charges are distributed smoothly in space).

Outline of proof

Coulomb's law states that the electric field due to a stationary point charge is: $\mathbf {E} (\mathbf {r} )={\frac {q}{4\pi \varepsilon _{0}}}{\frac {\mathbf {e} _{r}}{r^{2}}}$ where

- **e***r* is the radial unit vector,
- r is the radius, |**r**|,
- *ε*0 is the electric constant,
- q is the charge of the particle, which is assumed to be located at the origin.

Using the expression from Coulomb's law, we get the total field at **r** by using an integral to sum the field at **r** due to the infinitesimal charge at each other point **s** in space, to give $\mathbf {E} (\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\int {\frac {\rho (\mathbf {s} )(\mathbf {r} -\mathbf {s} )}{|\mathbf {r} -\mathbf {s} |^{3}}}\,\mathrm {d} ^{3}\mathbf {s}$ where ρ is the charge density. If we take the divergence of both sides of this equation with respect to **r**, and use the known theorem

$\nabla \cdot \left({\frac {\mathbf {r} }{|\mathbf {r} |^{3}}}\right)=4\pi \delta (\mathbf {r} )$ where *δ*(**r**) is the Dirac delta function, the result is $\nabla \cdot \mathbf {E} (\mathbf {r} )={\frac {1}{\varepsilon _{0}}}\int \rho (\mathbf {s} )\,\delta (\mathbf {r} -\mathbf {s} )\,\mathrm {d} ^{3}\mathbf {s}$

Using the "sifting property" of the Dirac delta function, we arrive at $\nabla \cdot \mathbf {E} (\mathbf {r} )={\frac {\rho (\mathbf {r} )}{\varepsilon _{0}}},$ which is the differential form of Gauss's law, as desired.

Since Coulomb's law only applies to stationary charges, there is no reason to expect Gauss's law to hold for moving charges based on this derivation alone. In fact, Gauss's law does hold for moving charges, and, in this respect, Gauss's law is more general than Coulomb's law.

Proof (without Dirac Delta)

Let $\Omega \subseteq R^{3}$ be a bounded open set, and $\mathbf {E} _{0}(\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\int _{\Omega }\rho (\mathbf {r} '){\frac {\mathbf {r} -\mathbf {r} '}{\left|\mathbf {r} -\mathbf {r} '\right|^{3}}}d^{3}r'\equiv {\frac {1}{4\pi \varepsilon _{0}}}\int _{\Omega }e(\mathbf {r,\mathbf {r} '} )d^{3}r'$ be the electric field, with $\rho (\mathbf {r} ')$ a continuous function (density of charge).

It is true for all $\mathbf {r} \neq \mathbf {r'}$ that $\nabla _{\mathbf {r} }\cdot \mathbf {e} (\mathbf {r,r'} )=0$ .

Consider now a compact set $V\subseteq R^{3}$ having a piecewise smooth boundary $\partial V$ such that $\Omega \cap V=\emptyset$ . It follows that $e(\mathbf {r,\mathbf {r} '} )\in C^{1}(V\times \Omega )$ and so, for the divergence theorem:

$\oint _{\partial V}\mathbf {E} _{0}\cdot d\mathbf {S} =\int _{V}\mathbf {\nabla } \cdot \mathbf {E} _{0}\,dV$

But because $e(\mathbf {r,\mathbf {r} '} )\in C^{1}(V\times \Omega )$ ,

$\mathbf {\nabla } \cdot \mathbf {E} _{0}(\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\int _{\Omega }\nabla _{\mathbf {r} }\cdot e(\mathbf {r,\mathbf {r} '} ){\mathrm {d} \mathbf {r} '}=0$ for the argument above ( $\Omega \cap V=\emptyset \implies \forall \mathbf {r} \in V\ \ \forall \mathbf {r'} \in \Omega \ \ \ \mathbf {r} \neq \mathbf {r'}$ and then $\nabla _{\mathbf {r} }\cdot \mathbf {e} (\mathbf {r,r'} )=0$ )

Therefore the flux through a closed surface generated by some charge density outside (the surface) is null.

Now consider $\mathbf {r} _{0}\in \Omega$ , and $B_{R}(\mathbf {r} _{0})\subseteq \Omega$ as the sphere centered in $\mathbf {r} _{0}$ having R as radius (it exists because $\Omega$ is an open set).

Let $\mathbf {E} _{B_{R}}$ and $\mathbf {E} _{C}$ be the electric field created inside and outside the sphere respectively. Then,

$\mathbf {E} _{B_{R}}={\frac {1}{4\pi \varepsilon _{0}}}\int _{B_{R}(\mathbf {r} _{0})}e(\mathbf {r,\mathbf {r} '} ){\mathrm {d} \mathbf {r} '}$

,

$\mathbf {E} _{C}={\frac {1}{4\pi \varepsilon _{0}}}\int _{\Omega \setminus B_{R}(\mathbf {r} _{0})}e(\mathbf {r,\mathbf {r} '} ){\mathrm {d} \mathbf {r} '}$

and

$\mathbf {E} _{B_{R}}+\mathbf {E} _{C}=\mathbf {E} _{0}$

$\Phi (R)=\oint _{\partial B_{R}(\mathbf {r} _{0})}\mathbf {E} _{0}\cdot d\mathbf {S} =\oint _{\partial B_{R}(\mathbf {r} _{0})}\mathbf {E} _{B_{R}}\cdot d\mathbf {S} +\oint _{\partial B_{R}(\mathbf {r} _{0})}\mathbf {E} _{C}\cdot d\mathbf {S} =\oint _{\partial B_{R}(\mathbf {r} _{0})}\mathbf {E} _{B_{R}}\cdot d\mathbf {S}$

The last equality follows by observing that $(\Omega \setminus B_{R}(\mathbf {r} _{0}))\cap B_{R}(\mathbf {r} _{0})=\emptyset$ , and the argument above.

The RHS is the electric flux generated by a charged sphere, and so:

$\Phi (R)={\frac {Q(R)}{\varepsilon _{0}}}={\frac {1}{\varepsilon _{0}}}\int _{B_{R}(\mathbf {r} _{0})}\rho (\mathbf {r} '){\mathrm {d} \mathbf {r} '}={\frac {1}{\varepsilon _{0}}}\rho (\mathbf {r} '_{c})|B_{R}(\mathbf {r} _{0})|$ with $r'_{c}\in \ B_{R}(\mathbf {r} _{0})$

Where the last equality follows by the mean value theorem for integrals. Using the squeeze theorem and the continuity of $\rho$ , one arrives at:

$\mathbf {\nabla } \cdot \mathbf {E} _{0}(\mathbf {r} _{0})=\lim _{R\to 0}{\frac {1}{|B_{R}(\mathbf {r} _{0})|}}\Phi (R)={\frac {1}{\varepsilon _{0}}}\rho (\mathbf {r} _{0})$

### Deriving Coulomb's law from Gauss's law

Strictly speaking, Coulomb's law cannot be derived from Gauss's law alone, since Gauss's law does not give any information regarding the curl of **E** (see Helmholtz decomposition and Faraday's law). However, Coulomb's law *can* be proven from Gauss's law if it is assumed, in addition, that the electric field from a point charge is spherically symmetric (this assumption, like Coulomb's law itself, is exactly true if the charge is stationary, and approximately true if the charge is in motion).

Outline of proof

Taking S in the integral form of Gauss's law to be a spherical surface of radius r, centered at the point charge Q, we have

$\oint _{S}\mathbf {E} \cdot d\mathbf {A} ={\frac {Q}{\varepsilon _{0}}}$

By the assumption of spherical symmetry, the integrand is a constant which can be taken out of the integral. The result is $4\pi r^{2}{\hat {\mathbf {r} }}\cdot \mathbf {E} (\mathbf {r} )={\frac {Q}{\varepsilon _{0}}}$ where **r̂** is a unit vector pointing radially away from the charge. Again by spherical symmetry, **E** points in the radial direction, and so we get $\mathbf {E} (\mathbf {r} )={\frac {Q}{4\pi \varepsilon _{0}}}{\frac {\hat {\mathbf {r} }}{r^{2}}}$ which is essentially equivalent to Coulomb's law. Thus the inverse-square law dependence of the electric field in Coulomb's law follows from Gauss's law.
