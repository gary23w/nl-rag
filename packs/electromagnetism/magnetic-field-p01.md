---
title: "Magnetic field (part 1/2)"
source: https://en.wikipedia.org/wiki/Magnetic_field
domain: electromagnetism
license: CC-BY-SA-4.0
tags: classical electromagnetism, electromagnetic field, lorentz force, electromagnetic induction
fetched: 2026-07-02
part: 1/2
---

# Magnetic field

In magnetism and electromagnetism, **magnetic field** is a physical property of space that quantifies the magnetic influence at a given location. Magnetic fields deflect moving electric charges (including electric currents), apply torques on magnets to twist them in the direction of the magnetic field, and attract or repel magnets and magnetic material such as iron. In addition, a time-varying magnetic field induces electrical currents. Magnetic fields are created by magnetic materials and by moving electric charges (including electrical current). The latter is important in creating electromagnets: devices that precisely control magnetic fields by changing the current through the electromagnet.

Magnetic fields are used throughout modern science and technology. In electrical engineering and electromechanics it is important in the design and use of electric motors, generators, transformers, electromagnets, and inductors among many other devices. In material science, magnetic forces give information about the charge carriers in a material through the Hall effect in addition to other uses.

In geology and geophysics, Earth's magnetic field gives information about earth's interior while local magnetic field measurements are used in mineral exploration and other measurements. Too, Earth's magnetic field creates a magnetosphere which shields the Earth's ozone layer and the rest of the planet from the solar wind. In physics the relationship between the magnetic and electric fields forms the field of electrodynamics which is important to understand a wide range of phenomena including light (also known as electromagnetic radiation) and the properties of antenna and transmission lines.

Since both strength and direction of a magnetic field may vary with location, it is described mathematically by assigning a vector to each point of space, making it a vector field. There are two different, but closely related, vector fields which are called "magnetic field". These are written as **B** and **H**. While the best names for these fields is the subject of long running debate, the underlying physics is uncontested.


## Definitions

The international ISO 80000-6 standard defines **magnetic field** as "that component of an electromagnetic field which is characterized by the magnetic field strength vector **H** and the magnetic flux density vector **B**." This standard also defines **B** and **H** as given in the sections below. While there is wide agreement on these definitions of **B** and **H**, there are many alternative names for both (see sidebars in the corresponding sections).

### The B-field

Also known as **magnetic flux density**, the magnetic **B** field causes magnetic forces, magnetic torques and electromagnetic induction. Therefore, it can be defined by any equation that describes these phenomena.

For example, the magnetic field vector **B** at any point can be defined as the vector field that, when used in the Lorentz force law, correctly predicts the force on a moving charged particle at that point:

Lorentz force law

(

vector

form,

SI units

)

$\mathbf {F} =q\mathbf {E} +q(\mathbf {v} \times \mathbf {B} )$

Here **F** is the force on the particle, *q* is the particle's electric charge, **E** is the external electric field, **v**, is the particle's velocity, and × denotes the cross product.

In other words,

> [T]he command, "Measure the direction and magnitude of the vector **B** at such and such a place," calls for the following operations: Take a particle of known charge *q*. Measure the force on *q* at rest, to determine **E**. Then measure the force on the particle when its velocity is **v**; repeat with **v** in some other direction. Now find a **B** that makes the Lorentz force law fit all these results—that is the magnetic field at the place in question.

For more details see Lorentz Force or the § Magnetic force on a charged particle section below.

The SI unit of **B** is tesla (symbol: T). The Gaussian-cgs unit of **B** is the gauss (symbol: G). (The conversion is 1 T ≘ 10000 G.) One nanotesla corresponds to 1 gamma (symbol: γ).

### The H-field

While **B** creates magnetic forces and torques on objects and induces currents in conducting wires, it is not always easy to calculate. For this reason, it is useful to define a magnetic **H** field, also known as **magnetic field strength**, such that:

Definition of the

H

field

(

vector

form,

SI units

)

$\mathbf {H} \equiv {\frac {1}{\mu _{0}}}\mathbf {B} -\mathbf {M} ,$

where $\mu _{0}$ is the vacuum permeability, and **M** is the magnetization vector which represents how magnetized a given region of material is and is defined below. In a vacuum, **B** = μ0**H** making them equivalent to each other. Inside a material they are different.

Defined this way, **H** can in many circumstance be treated as if it is only due to electrical currents with corrections accounting for **H** due to nearby magnetic material. In any case, **B** still needs to be calculated from **H** if forces, torques, induced currents, or energy changes need to be calculated.

The SI unit of **H** is the ampere per metre (A/m) and the Gaussian unit is the oersted (Oe).


## Measurement and visualization

### Magnetometers

Instruments used to measure the local magnetic **B**-field are known as a magnetometers. Important classes of magnetometers include induction magnetometers (or search-coil magnetometers) which measure only varying magnetic fields, rotating coil magnetometers, Hall effect magnetometers, NMR magnetometers, SQUID magnetometers, and fluxgate magnetometers. The magnetic fields of distant astronomical objects are measured through their effects on local charged particles. For instance, electrons spiraling around a field line produce synchrotron radiation that is detectable in radio waves. The finest precision for a magnetic field measurement was attained by Gravity Probe B at 5 aT (5×10−18 T).

The **H**-field cannot be directly measured but can be inferred from the currents that create it.

### Magnetic field lines

Visualizing magnetic fields

Left: the direction of magnetic

field lines

represented by

iron filings

sprinkled on paper placed above a bar magnet.

Right:

compass

needles point in the direction of the local magnetic field, towards a magnet's south pole and away from its north pole.

Magnetic field can be visualized by a set of *magnetic field lines*, that follow the direction of the field at each point. The direction of the magnetic field at any point is parallel to the direction of nearby field lines, and the local density of field lines can be made proportional to its strength. Magnetic field lines are like streamlines in fluid flow, in that they represent a continuous distribution, and a different resolution would show more or fewer lines.

Magnetic field lines have the following properties:

- The direction of the magnetic field is tangent to the field line at any point. A small compass points in the direction of the field line.
- The strength of the field is proportional to the closeness of the lines.
- Magnetic field lines never cross.
- Magnetic field lines form closed loops enclosing electrical currents.
- Magnetic field lines are directed from the north pole to the south pole.

An advantage of using magnetic field lines as a representation is that many laws of magnetism (and electromagnetism) can be stated completely and concisely using simple concepts such as the "number" of field lines through a surface. These concepts can then be "translated" to their mathematical form. For example, the number of field lines through a given surface is the surface integral of the magnetic field.

### Different unit systems

This article uses almost entirely the SI unit system. But other unit systems, most importantly the Gaussian unit system (which is the most used system of cgs units for electromagnetism), are still being used in some disciplines, countries, and textbooks. The equations for each unit system can be, and often are, different for different unit systems.


## Force on moving charges and current

Moving electric charges including electrical currents experience a force due to magnetic **B** fields.

### Magnetic force on a charged particle

A charged particle moving in a **B**-field experiences a *sideways* force that is proportional to the strength of the magnetic field, the component of the velocity that is perpendicular to the magnetic field and the charge of the particle. This force is known as the *Lorentz force*, and is given by:

Lorentz force law

(

vector

form,

SI units

)

$\mathbf {F} =q\mathbf {E} +q(\mathbf {v} \times \mathbf {B} ),$

where **F** is the force, *q* is the electric charge of the particle, **v** is the instantaneous velocity of the particle, and **B** is the magnetic field (in teslas). The direction of force on the charge can be determined by the right-hand rule (see the figure).

The Lorentz force is always perpendicular to both the velocity of the particle and the magnetic field that created it. When a charged particle moves in a static magnetic field, it traces a helical path in which the helix axis is parallel to the magnetic field, and in which the speed of the particle remains constant.

### Force on current-carrying wire

When a wire carrying a steady electric current is placed in an external magnetic field, each of the moving charges in the wire experience the Lorentz force. Together, these forces produce a net macroscopic force on the wire. This force (on a macroscopic current) is often referred to as the *Laplace force*.

For a straight, stationary wire in a uniform magnetic field, this force is given by:

Magnetic force on straight line current

(

vector

form,

SI units

)

$\mathbf {F} =I{\boldsymbol {\ell }}\times \mathbf {B} \,,$

where I is the current and **ℓ** is a vector whose magnitude is the length of the wire, and whose direction is along the wire, aligned with the direction of the current.

If the wire is not straight or the magnetic field is non-uniform, the total force can be computed by applying the formula to each infinitesimal segment of wire $\mathrm {d} {\boldsymbol {\ell }}$ , then adding up all these forces by integration. In this case, the net force on a stationary wire carrying a steady current is

Magnetic force on current of arbitrary shape

(

vector

form,

SI units

)

$\mathbf {F} =I\int (\mathrm {d} {\boldsymbol {\ell }}\times \mathbf {B} )\,.$

This force creates an attractive/repulsive force between 2 parallel wires as the current through each produces a magnetic field that pushes/pulls on the other. Too, a loop of current in a magnetic field will experience a torque due to the different direction of the force on different sides of the loop as describe in the next section.

### Net force and torque on current loops

A magnetic field acting on a current carrying loop produces both a torque and a net force (if the magnetic field is non-uniform). This effect is important for driving certain types of motors and in modeling forces and torques on atoms.

Calculating the torque on a rectangular loop is straightforward. The diagram to the right shows a rectangular loop of current in a uniform magnetic **B** field (with a direction indicated by the green arrows). For simplicity the loop is aligned so that it is along the direction of the magnetic field. The magnetic force on opposite sides of the loop are equal and opposite producing no net force on the loop. The forces on the short sides (here shown as violet arrows), though, produce a net torque equal to the product of the force and the perpendicular distance between them. Denoting the short side length as b, the magnitude of that force is F = IBb using the equation for the magnetic force on a straight wire given in the previous section. The magnitude of the net torque (along dashed axis) is therefore N = IabB. Using the fact that the area A = ab and generalizing for all angles gives

Torque on a current loop

(

vector

form,

SI units

)

$\mathbf {N} =I\mathbf {A} \times \mathbf {B} \,.$

Here the direction of the area **A** is the normal to the area as determined by the right hand grip rule of the current loop. While derived for a rectangular loop this equation is valid for a flat loop of any shape and orientation. As described above, there is no net force on a loop in a uniform magnetic field. However, non-uniform magnetic fields do produce a net force. This net force tends to pull the object in direction of the stronger magnetic field.

### Net force and torque on a magnetic dipole

Since the net force on a loop is proportional to the current of the loop times it area, it is natural to define a quantity **m** called the **magnetic dipole moment** such that

Definition of magnetic dipole moment, m

(

vector

form,

SI units

)

$\mathbf {m} =I\mathbf {A} \,.$

For a sufficiently small current loop, the details of the current loop such as it shape, area, orientation, and current around the loop are all hidden in **m** and otherwise do not matter. Such loops are called magnetic dipoles. All magnetic dipoles with the same dipole moment **m** are affected the same way.

Applying the Lorentz force to a (sufficiently small) current loop of arbitrary shape produces a torque **N** on the magnetic dipole of:

Torque on a magnetic dipole

(

vector

form,

SI units

)

$\mathbf {N} =\mathbf {m} \times \mathbf {B}$

and a force **F** on the magnetic dipole of

Force on a magnetic dipole

(

vector

form,

SI units

)

$\mathbf {F} =\nabla (\mathbf {m} \cdot \mathbf {B} ),$

where $\nabla$ represents the gradient. This force tends to push the magnetic dipole into the direction of increasing **B**.


## Magnetic field due to electrical currents

All moving charged particles produce magnetic fields. Moving point charges, such as electrons, produce complicated but well known magnetic fields that depend on the charge, velocity, and acceleration of the particles. These equations become much simpler when the moving charges form a steady state electrical current, the study of which is called magnetostatics.

### Magnetic field of a long straight wire

In general, magnetic field lines form concentric circles around a current-carrying wire. The direction of such a magnetic field can be determined by using the "right-hand grip rule" (see figure at right). The strength of the magnetic field decreases with distance from the wire. (For an infinite length wire the strength is inversely proportional to the distance.) The magnetic field of a steady current I through a sufficiently long straight wire is:

Magnetic field of infinite wire

(

vector

form,

SI units

)

${\begin{aligned}\mathbf {B} ={\frac {\mu _{0}}{2\pi r}}I\,{\hat {\phi }},\\\mathbf {H} ={\frac {I}{2\pi r}}\,{\hat {\phi }},\end{aligned}}$

where *r* is the perpendicular distance to the wire. The direction ${\hat {\phi }}$ of the magnetic field is tangent to a circle perpendicular to the wire according to the right hand rule.

### Magnetic field of an arbitrarily shaped thin wire

More specifically, the magnetic field generated by a steady current I (a constant flow of electric charges, in which charge neither accumulates nor is depleted at any point) is described by the *Biot–Savart law*:

Biot-Savart Law

(

vector

form,

SI units

)

${\begin{aligned}\mathbf {B} ={\frac {\mu _{0}I}{4\pi }}\int _{\mathrm {wire} }{\frac {\mathrm {d} {\boldsymbol {\ell }}\times \mathbf {\hat {r}} }{r^{2}}},\\\mathbf {H} ={\frac {I}{4\pi }}\int _{\mathrm {wire} }{\frac {\mathrm {d} {\boldsymbol {\ell }}\times \mathbf {\hat {r}} }{r^{2}}},\end{aligned}}$

where the integral sums over the wire length where vector d**ℓ** is the vector line element with direction in the same sense as the current *I*, *μ*0 is the magnetic constant, *r* is the distance between the location of d**ℓ** and the location where the magnetic field is calculated, and **r̂** is a unit vector in the direction of **r**.

### Magnetic field of a solenoid

Bending a current-carrying wire into a loop concentrates the magnetic field inside the loop while weakening it outside. Bending a wire into multiple closely spaced loops to form a coil or 'solenoid' enhances this effect. A device so formed around an iron core may act as an electromagnet, generating a strong, well-controlled magnetic field.

An infinitely long solenoid has a uniform magnetic field inside, and no magnetic field outside. The magnetic field only exists inside of the solenoid and is

Magnetic field of an infinite solenoid

(

vector

form,

SI units

)

$\mathbf {H} =nI,$

where n is the number of turns per unit length of the solenoid and the direction of **H** is along the length of the solenoid. A finite length solenoid produces a more complicated magnetic field that can be evaluated mathematically.

For other examples of using the Biot-Savart law to calculate the magnetic fields for other common current configurations see #Common formulæ below.

### Magnetic field of a flat loop of current (magnetic dipole)

The magnetic field of a circular current loop of radius a and carrying a current I can be calculated straightforwardly from the Biot-Savart law for locations a distance z directly above the center of the loop:

Magnetic field at distance z directly above a circular current loop

(

vector

form,

SI units

)

${\begin{aligned}\mathbf {B} &=\mu _{0}{\frac {\mathbf {m} }{2\pi (a^{2}+z^{2})^{3/2}}}\,,\\\mathbf {H} &={\frac {\mathbf {m} }{2\pi (R^{2}+z^{2})^{3/2}}}\,,\\\end{aligned}}$

where $\mathbf {m} =I\mathbf {A} =I(\pi a^{2}\mathbf {\hat {z}} )$ is the same magnetic dipole moment used in calculating the force and torque on a loop of current in #Net force and torque on a magnetic dipole above. Calculating the on-axis magnetic fields of a square loop (and other flat geometries) yields similar equations that have the same equation at long distances as the circle: $\mathbf {H} ={\frac {\mathbf {m} }{2\pi z^{3}}}$ .

Calculating the magnetic field at a arbitrary location **r** (not just on-axis) from an arbitrarily shaped current loop involves advanced math. But, for sufficiently long distances, the result depends only on the magnetic moment **m** of that loop and simplifies to:

Magnetic field of magnetic dipole

(

vector

form,

SI units

)

$\mathbf {H} _{dip}={\frac {1}{4\pi }}\left[{\frac {3\mathbf {\hat {r}} (\mathbf {m} \cdot \mathbf {\hat {r}} )-\mathbf {m} }{r^{3}}}\right]={\frac {\mathbf {B} _{dip}}{\mu _{0}}}.$

This equation shows that at sufficiently long distances the detailed geometry of a magnet can be replaced by a single quantity, the magnetic dipole moment **m**. This equation, therefore makes a good model for the magnetic field of atoms and can be extended to describe magnetic material. Too, it has some utility in calculating the long distance force between magnets.

### Ampere's law

A slightly more general way of relating the current I to the **B**-field is through Ampère's law:

Ampere's Law

(

vector

form,

SI units

)

${\begin{aligned}\oint \mathbf {B} \cdot \mathrm {d} {\boldsymbol {\ell }}&=\mu _{0}I_{\mathrm {enc} },\\\oint \mathbf {H} \cdot \mathrm {d} {\boldsymbol {\ell }}&=I_{\mathrm {enc} },\end{aligned}}$

where the line integral is over any arbitrary loop and $I_{\text{enc}}$ is the current enclosed by that loop. The $I_{\text{enc}}$ is slightly different for the 2 equations in that **B** includes the difficult to calculate bound current in magnetic material while **H** does not. Ampère's law is always valid for steady currents and can be used to easily calculate the magnetic fields of certain highly symmetric situations such as an infinite wire or an infinite solenoid.

In a modified form that accounts for time varying electric fields, Ampère's law is one of four Maxwell's equations that describe electricity and magnetism.


## Force between magnets

### Magnets

Magnets are objects that both create their own magnetic field and respond to the magnetic field of other magnets and magnetized materials. The interaction between magnets and their interaction with magnetic field is extremely complicated. The correct description involves describing each magnet as being made of many small volumes of magnetic material each of which creates its own magnetic field and responds to the magnetic field of the other volumes. Such models are often extremely complex. Fortunately, in many cases, it is sufficient to understand magnets as objects that have 2 equal but opposite magnetic poles: the magnetic north and south poles. Opposite poles attract with a force that increases with smaller distances while like poles repel in the same way. Such a model is called a *magnetic pole model* and it, in some cases described below, can be used to make good quantitative predictions.

Specifying the force between magnets is quite complicated because it depends on the strength and orientation of both magnets and their distance and direction relative to each other. The force is particularly sensitive to rotations of the magnets due to magnetic torque. The force on each magnet depends on its magnetic moment and the magnetic field of the other. For short distances (small r) the forces can be quite strong but it decreases quite rapidly (1/r4) for large distances.

### Force between magnets at long distances (dipole–dipole interaction)

For 2 sufficiently small magnets, such as 2 atoms far enough away from each other, the magnetic force can be represented as that of two infinitesimally small dipoles. Using vector notation, the force, **F** of a magnetic dipole **m**1 on the magnetic dipole **m**2 is:

The magnetic dipole–dipole interaction

(

vector

form,

SI units

)

$\mathbf {F} ={\frac {3\mu _{0}}{4\pi r^{5}}}\left[(\mathbf {m} _{1}\cdot \mathbf {r} )\mathbf {m} _{2}+(\mathbf {m} _{2}\cdot \mathbf {r} )\mathbf {m} _{1}+(\mathbf {m} _{1}\cdot \mathbf {m} _{2})\mathbf {r} -{\frac {5(\mathbf {m} _{1}\cdot \mathbf {r} )(\mathbf {m} _{2}\cdot \mathbf {r} )}{r^{2}}}\mathbf {r} \right]$

where **r** is the distance-vector from dipole moment **m**1 to dipole moment **m**2, with *r* = ‖***r***‖. The force acting on **m**1 is in the opposite direction. The net force depends on the orientation of both dipole moments relative to each other and relative to the distance-vector between them and it decreases rapidly (proportional to 1/r4).

### Force between magnets at moderate distance (Coulomb's law for magnetism)

For moderate distances it is often to sufficient model the force between magnets as the ***H**-field* of one magnet pushes and pulls on *both* poles of a second magnet. If this **H**-field is the same at both poles of the second magnet then there is no net force on that magnet since the force is opposite for opposite poles. If, however, the magnetic field of the first magnet is *nonuniform* (such as the **H** near one of its poles), each pole of the second magnet sees a different field and is subject to a different force. This difference in the two forces moves the magnet in the direction of increasing magnetic field and may also cause a net torque.

If both poles are small enough to be represented as single points then they can be considered to be point magnetic charges. Classically, the force **F** between two magnetic poles is given by:

Coulomb's law for magnetism (force between poles)

(

vector

form,

SI units

)

$\mathbf {F} ={{\mu q_{m1}q_{m2}} \over {4\pi r^{2}}}\mathbf {\hat {r}}$

where qm1 and qm2 are the **magnetic pole strengths** of each magnet (SI unit: ampere-meter), *μ* is the permeability of the intervening medium, and **r** is the separation distance between the 2 poles. Note that for 2 magnets (each having 2 poles) the sum of 4 forces is needed: each of the 2 poles of one magnet exerts a separate force on each of the 2 poles of the second magnet.

The pole description is useful to practicing magneticians who design real-world magnets, but real magnets have a pole distribution more complex than a single north and south. Therefore, implementation of the pole idea is not simple. In some cases, one of the more complex formulas given below will be more useful.

### Magnetic force at small distances (pull force)

The mechanical force between two nearby magnetized surfaces can be calculated with the following equation. The equation is valid only for cases in which the effect of fringing is negligible and the volume of the air gap is much smaller than that of the magnetized material, the force for each magnetized surface is:

Magnetic pull between nearly touching magnetic poles (magnetic pole nearly touching iron)

(

vector

form,

SI units

)

$F={\frac {\mu _{0}H^{2}A}{2}}={\frac {B^{2}A}{2\mu _{0}}}$

where *A* is the surface area of the magnetic pole and μ0 is the permeability of free space. This equation is also valid for the force of a magnetic pole on iron that is either almost touching or touching the magnetic pole.

### Magnetic torque on permanent magnets

If two like poles of two separate magnets are brought near each other, and one of the magnets is allowed to turn, it promptly rotates to align itself with the first. In this example, the magnetic field of the stationary magnet creates a *magnetic torque* on the magnet that is free to rotate. This magnetic torque **N** tends to align a magnet's poles with the magnetic field lines. A compass, therefore, turns to align itself with Earth's magnetic field.

Torque on a dipole

In the pole model of a dipole, an

H

field (to right) causes equal but opposite forces on a N pole (

+

q

) and a S pole (

−

q

) creating a torque.

Equivalently, a

B

field induces the same torque on a current loop with the same magnetic dipole moment.

Mathematically, the torque **N** on a small magnet is proportional both to the applied magnetic field and to the magnetic moment **m** of the magnet:

Magnetic torque

(

vector

form,

SI units

)

${\boldsymbol {N}}=\mathbf {m} \times \mathbf {B}$

where × represents the vector cross product. This equation includes all of the qualitative information included above. There is no torque on a magnet if **m** is in the same direction as the magnetic field, since the cross product is zero for two vectors that are in the same direction. Further, all other orientations feel a torque that twists them toward the direction of magnetic field.


## Magnetic field due to magnetized material

Most materials respond to an applied magnetic field by becoming magnetized (at least temporarily) which causes them to produce their own magnetic field. Typically, the response is weak and exists only when the magnetic field is applied. There are many different types of material that respond differently to the applied magnetic field.

### Types of magnetic materials

The term *magnet* is typically reserved for objects that produce their own persistent magnetic field even in the absence of an applied magnetic field. Only certain classes of materials can do this. Most materials, however, produce a magnetic field in response to an applied magnetic field – a phenomenon known as magnetism. There are several types of magnetism, and all materials exhibit at least one of them.

The overall magnetic behavior of a material can vary widely, depending on the structure of the material, particularly on its electron configuration. It can also vary with temperature, pressure, and magnetic field strength such that a given material may have more than one magnetic phase. Several forms of magnetic behavior have been observed in different materials, including:

- Diamagnetism produces a magnetization that opposes the magnetic field.
- Paramagnetism produces a magnetization in the same direction as the applied magnetic field.
- Ferromagnetism and the closely related Ferrimagnetism and Antiferromagnetism can produce a magnetization independent of the applied magnetic field with a complicated and often hysteretic relationship. Materials in these states can be used to make permanent magnets.
- Superconductivity (and ferromagnetic superconductors) is characterized by perfect conductivity below a critical temperature and magnetic field. They also are highly magnetic and can be perfect diamagnets below a lower critical magnetic field. Superconductors often have a broad range of temperatures and magnetic fields (the so-named mixed state) under which they exhibit a complicated and often hysteretic relationship between how the material is magnetized and the applied magnetic field.

In the case of paramagnetism and diamagnetism, the relationship between the applied magnetic field and the magnetization is often linear. However, superconductors and ferromagnets have a more complicated relation between the applied magnetic field and magnetization produced (see magnetic hysteresis). *Permanent magnets* are objects that produce their own persistent magnetic fields. They are made of ferromagnetic materials, such as iron and nickel, that have been magnetized.

### Magnetic dipole moment

The Amperian loop model

A current loop (ring) that goes into the page at the x and comes out at the dot produces a

B

-field (lines). As the radius of the current loop shrinks, the fields produced become identical to an abstract "magnetic dipole" (represented by an arrow pointing to the right).

The magnetic field of magnetized material is created at the atomic level. The proper description of this effect involves quantum mechanics. Fortunately, the net effect of adding up these magnetic interactions can often be calculated using much simpler models for the magnetic field created by the constituent atoms in the magnetic material. This occurs because at large enough distance (or equivalently for small enough magnets) all the magnetic properties of any magnetic object can be described by a single (vector) quantity, the magnetic dipole moment, **m**. (See § Magnetic field of a flat loop of current (magnetic dipole) and § Net force and torque on a magnetic dipole above). Objects that can be modeled this way, for example atoms, are called magnetic dipoles.

Magnetic dipoles, therefore, are the building blocks of magnetization. The magnetic field produced by magnetized material then is the net magnetic field of these dipoles. Too, the net force (and torque) on a magnetized material is a result of adding up the forces and torques on the individual dipoles that make up the magnetized material.

### Magnetization

The *magnetization* vector field **M** represents how strongly a region of material is magnetized. It is defined as the net magnetic dipole moment per unit volume of that region. The magnetization of a uniformly magnetized magnet is therefore a constant, equal to the magnetic moment **m** of the magnet divided by its volume. Since the SI unit of magnetic moment is A⋅m2, the SI unit of magnetization **M** is ampere per meter, identical to that of the **H**-field.

The magnetization **M** field of a region points in the direction of the average magnetic dipole moment in that region. Magnetization field lines, therefore, begin (inside the magnetized material) near the magnetic south pole and ends (inside the magnetized material) near the magnetic north pole. (Magnetization does not exist outside magnetized material.)

In the Amperian loop model, the magnetization is due to combining many tiny magnetic dipole loops to form a resultant current called *bound current*. This bound current, then, is the source of the magnetic **B** field due to the magnet. Given the definition of the magnetic dipole, the magnetization field follows a similar law to that of Ampere's law:

Relation between M and bound current

(

vector

form,

SI units

)

$\oint \mathbf {M} \cdot \mathrm {d} {\boldsymbol {\ell }}=I_{\mathrm {b} }\,,$

where the integral is a line integral over any closed loop and *I*b is the bound current enclosed by that closed loop.

Unlike the magnetic **B** field-lines which cannot begin nor end, magnetization field lines can begin and end. Indeed they must begin and end where they intersects the boundary of the magnetized material (at magnetic poles) because the magnetization field only exists inside of a material. This is analogous to electric field-lines which begin and end at electrical charges. It is therefore possible to define a 'magnetic charge' qm such that for a given region the net 'magnetic charge' is:

Relation between M and fictitious magnetic charge

(

vector

form,

SI units

)

$\oint _{S}\mu _{0}\mathbf {M} \cdot \mathrm {d} \mathbf {A} =-q_{\mathrm {m} }\,,$

where the integral is a closed surface integral over the closed surface *S* and *q*M is the "magnetic charge" (in units of magnetic flux) enclosed by *S*. (A closed surface completely surrounds a region with no holes to let any field lines escape.) The negative sign occurs because the magnetization field moves from south to north. No such magnetic charge exists; rather it is a convenient analogy that allows the use of much of the machinery developed for electrostatics with electric charge to be applied to magnetization with its fictitious magnetic charge. For example the net magnetic charge of a pole is defined as a **magnetic pole strength** qm.

### Relation between B, H, and M

Using the above definition of **M** it is now possible to define the magnetic **H** field

Definition of H

(

vector

form,

SI units

)

$\mathbf {H} \ \equiv \ {\frac {\mathbf {B} }{\mu _{0}}}-\mathbf {M} .$

From this equation, it is evident that outside of a magnetic material (where $\mathbf {M} =0$ ) that $\mathbf {B} =\mu _{0}\mathbf {H}$ . Outside a magnetic material, therefore, **B** and **H** are functionally identical just with different units since $\mu _{0}$ is a constant.

In terms of the H-field, Ampere's law is:

Relation between H and free current

(

vector

form,

SI units

)

$\oint \mathbf {H} \cdot \mathrm {d} {\boldsymbol {\ell }}=\oint \left({\frac {\mathbf {B} }{\mu _{0}}}-\mathbf {M} \right)\cdot \mathrm {d} {\boldsymbol {\ell }}=I_{\mathrm {tot} }-I_{\mathrm {b} }=I_{\mathrm {f} },$

where If represents the 'free current' enclosed by the loop so that the line integral of **H** does not depend at all on the bound currents.

Similarly, a surface integral of **H** over any closed surface is independent of the free currents and picks out the "magnetic charges" within that closed surface:

Relation between H and fictitious magnetic charge

(

vector

form,

SI units

)

$\oint _{S}\mu _{0}\mathbf {H} \cdot \mathrm {d} \mathbf {A} =\oint _{S}(\mathbf {B} -\mu _{0}\mathbf {M} )\cdot \mathrm {d} \mathbf {A} =0-(-q_{\mathrm {M} })=q_{\mathrm {m} }\,,$

which does not depend on the free currents.

The **H**-field, therefore, can be separated into two independent parts: $\mathbf {H} =\mathbf {H} _{0}+\mathbf {H} _{\mathrm {d} }$ , where **H**0 is the applied magnetic field due only to the free currents and **H**d is the demagnetizing field due only to the bound currents which can equivalently be expressed in terms of the fictitious magnetic charge qm. The magnetic **H**-field, therefore, re-factors the bound current in terms of "magnetic charges". The **H** field lines loop only around "free current" and, unlike the magnetic **B** field, begins and ends near magnetic poles as well.

### Constitutive relation between B and H

For many materials (particularly diamagnetic and paramagnetic materials) the relationship between **B** and **H** is linear:

Constitutive relation between B and H

(

vector

form,

SI units

)

$\mathbf {B} =\mu \mathbf {H} ,$

where *μ* is a material dependent parameter called the permeability. In some cases the permeability may be a second rank tensor so that **H** may not point in the same direction as **B**. These relations between **B** and **H** are examples of constitutive equations.

### Boundary conditions for B and H

In many real world applications such as small magnetic object inside of an extended applied magnetic field, the constitutive relation is not sufficient even if the material is linear. This is because the **H**-field that the material experiences is not the same as the **H** applied. In such cases, the magnetic field can still be calculated but care must be taken to distinguish the change of the magnetic field across the boundary of the magnetic object. These relations in the most simplified form (in terms of **H** only in a linear material and without and free current) are:

Boundary Conditions for H (no free current)

(

scalar form,

SI units

)

${\begin{aligned}H_{1t}&=H_{2t}\,,\\\mu _{1}H_{1N}&=\mu _{2}H_{2n}\,,\end{aligned}}$

where the subscript t represents the tangential component of **H** and n represents its normal component.


## Electrodynamics

For time varying magnetic fields (and more generally changing electrical currents or accelerating electrical charges), the magnetic and electric fields become linked such that a change in one induces the other. Together, the electric and magnetic fields form an electromagnetic field. The study of how the electric and magnetic fields interact in this way is called electrodynamics and includes many phenomenon that are important in physics and electrical engineering. It underlies transformers, and the generation and transmission of electrical power through wires and through space in the form of electromagnetic radiation of which light is one form. Too, it allow magnetic fields to store and transmit energy.

### Magnetic flux rule

A time varying magnetic field through a loop of wire induces a current (more properly an EMF) through that loop. This is known as electromagnetic induction and is important for many electronic devices such as inductors, transformers, and electrical generators. The equation governing this is known as the **flux rule** or Faraday's law of induction:

Magnetic flux rule (Faraday's law of induction)

(

vector

form,

SI units

)

${\mathcal {E}}=-{\frac {\mathrm {d} \Phi }{\mathrm {d} t}}\,,$

where ${\mathcal {E}}$ is the electromotive force (or *EMF*, the voltage generated around a closed loop) and Φ is the magnetic flux—the product of the area times the magnetic field normal to that area. (This definition of magnetic flux is why **B** is often referred to as *magnetic flux density*.) The negative sign represents the fact that any current generated by a changing magnetic field in a coil produces a magnetic field that *opposes* the *change* in the magnetic field that induced it. This phenomenon is known as Lenz's law.

### Stored energy

Energy is needed to generate a magnetic field both to work against the electric field that a changing magnetic field creates and to change the magnetization of any material within the magnetic field. The energy density of just creating the field at a given region is:

Magnetic energy density in vacuum

(

vector

form,

SI units

)

$u_{mag}={\frac {\mathbf {B} \cdot \mathbf {B} }{2\mu _{0}}}\,.$

For non-dispersive materials, the energy used to magnetize the material is released when the magnetic field is destroyed so that the energy can be modeled as being stored in the magnetic field. If the non-dispersive material is also linear (such that **B** = *μ***H** where *μ* is frequency-independent), then the total energy density stored in the magnetic field and in magnetizing the material at a location is:

Magnetic energy density in linear material

(

vector

form,

SI units

)

$u_{mag}={\frac {\mathbf {B} \cdot \mathbf {H} }{2}}={\frac {\mathbf {B} \cdot \mathbf {B} }{2\mu }}={\frac {\mu \mathbf {H} \cdot \mathbf {H} }{2}}\,.$

The above equation cannot be used for nonlinear materials, though. In general, the incremental amount of work per unit volume *δW* needed to cause a small change of magnetic field *δ***B** is:

Differential work done (per unit volume) in creating a magnetic field in the presence of a material

(

vector

form,

SI units

)

$\delta W=\mathbf {H} \cdot \delta \mathbf {B} \,.$

Once the relationship between **H** and **B** is known this equation is used to determine the work needed to reach a given magnetic state. For hysteretic materials such as ferromagnets and superconductors, the work needed also depends on how the magnetic field is created. For linear non-dispersive materials, though, the general equation leads directly to the simpler energy density equation given above.

### Poynting vector

Magnetic field, together with the electric field, transmit electrical power. The amount of electrical power (per unit area) transmitted this way is called the **poynting vector**, **S**, which depends on the magnetic field as the cross product:

The Poynting vector (power per unit area passing a given point)

(

vector

form,

SI units

)

$\mathbf {S} =\mathbf {E} \times \mathbf {H} \,,$

where **E** is the electric field. Note that this power includes both the power transmitted by the electric and magnetic fields and the energy absorbed and emitted by magnetizing and polarizing the material. Too, this equation only works for linear non-dispersive materials. This equations is also valid in a vacuum where **H** = **B**/μ0.

The time average of the poynting vector is known as irradiance and is an important quantity in optics that describes how intense light is at a given point.

### Maxwell's equations

It is sometimes useful to calculate the magnetic field for a given set of time varying charges and currents, without having to use the complicated equations used to directly calculate it. An example of this is calculating the magnetic field of a light wave as it reflects and refracts at a surface. In such cases Maxwell's equations are used to solve for both the magnetic and electric fields. (In electrodynamics the electric and magnetic fields are coupled.)

Maxwell's equations are a powerful set of differential equations that allows the calculation of the magnetic and electric fields for simple (and complex using computers and Finite Element Analysis) geometries. Maxwell's Equations together with the Lorentz force law form a complete description of classical electrodynamics including both electricity and magnetism.

Maxwell's equations takes advantage of the fact that all vector fields (such as the electric and magnetic fields) can be expressed in terms of 2 types of *sources* and an appropriate set of boundary conditions. The first type of *source* (an outflow source) causes the vector field to flow out (or in for a sink) to a given point. The second (or circulation) source causes the vector field to rotate around a given point (forming vortices). Both of these sources have well defined definitions and can be calculated from the vector field they create using a well-understood vector operator.

The divergence of a vector field **A**, **∇** · **A** is defined such that applying the divergence operator to a given vector field will yield the outflow sources. The curl is defined such that **∇** × **A** yields the circulation source. An example of the power of these vector operators is: since it is an experimental fact that magnetic charges do not exist (and therefore there are no source nor sinks of **B**) the divergence of **B** must be zero, **∇** · **B** = 0, which is one of Maxwell's equations.

Maxwell's equation has 2 major versions: a microscopic version which necessitates knowing all of the charges and currents (including the complex ones at the atomic level) and the macroscopic version which depends only on the know 'free' charge and 'free' currents. Here the term 'free' means any charge or current that is directly controlled by the experiment and does not include the atomic level 'bound' charges and currents in a material which happen as a response to the electric and magnetic fields present in that material.

Maxwell's macroscopic equations are written as:

Maxwell's equations in matter

(

vector

form,

SI units

)

${\begin{aligned}\nabla \cdot \mathbf {D} \,\,\,&=\rho _{f}\\\nabla \cdot \mathbf {B} \,\,\,&=0\\\nabla \times \mathbf {E} &=-{\frac {\partial \mathbf {B} }{\partial t}}\\\nabla \times \mathbf {H} &=\mathbf {J} _{f}+{\frac {\partial \mathbf {D} }{\partial t}}\,.\end{aligned}}$

In these equations, $\mathbf {D}$ is the electric displacement field, $\mathbf {E}$ the electric field, $\rho _{f}$ the free electric charge density, and $\mathbf {J} _{f}$ the free current density.

The first of Maxwell's equations is known as Gauss' Law but does not involve magnetic field so does not warrant further discussion here. The second equation is Gauss' law for magnetism which reflects the non-existence of magnetic charge and allows **B** to be determined as the curl of a vector potential **A**. The third equation is Faraday's law of induction. And, the fourth equation is Ampère's law with Maxwell's correction.
