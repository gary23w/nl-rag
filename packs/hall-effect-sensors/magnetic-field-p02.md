---
title: "Magnetic field (part 2/2)"
source: https://en.wikipedia.org/wiki/Magnetic_field
domain: hall-effect-sensors
license: CC-BY-SA-4.0
tags: hall effect sensor, magnetic field sensing, wiegand effect, reed switch
fetched: 2026-07-02
part: 2/2
---

## Advanced formulations

### Magnetic vector potential

In deriving advanced equations and in advanced topics such as quantum mechanics and relativity, it is often easier to work with a *potential formulation* of electrodynamics rather than in terms of the electric and magnetic fields. In this representation, the *magnetic vector potential* **A**, and the electric scalar potential *φ*, are defined such that:

Definition of the vector A and scalar φ potentials

(

vector

form,

SI units

)

${\begin{aligned}\mathbf {B} &=\nabla \times \mathbf {A} ,\\\mathbf {E} &=-\nabla \varphi -{\frac {\partial \mathbf {A} }{\partial t}}.\end{aligned}}$

The vector potential, ***A*** given by this form may be interpreted as a *generalized potential momentum per unit charge* just as *φ* is interpreted as a *generalized potential energy per unit charge*. There are multiple choices one can make for the potential fields that satisfy the above condition. However, the choice of potentials is represented by its respective gauge condition.

Maxwell's equations when expressed in terms of the potentials can be cast into a form that explicitly agrees with special relativity. Together, **A** and *φ* form the four-potential. Using the four potential instead of electric and magnetic fields is much simpler—and it can be easily adapted to work with quantum mechanics.

### Magnetic and electric fields are different aspects of the same phenomenon

Magnetic field is inherently a relativistic phenomena. More specifically, both electric and magnetic fields are the same phenomenon as seen in different reference frames: An electric force perceived by one observer may be perceived by another (in a different frame of reference) as a magnetic force, or a mixture of electric and magnetic forces. (Here different reference frames means one reference frame is moving relative to the other.) For relativistic phenomena, a lorentz transformation must be used to move (or transform) from one reference system to another.

It is a straightforward task to show how the electric and magnetic fields transform from one reference frame to another. The transformation rules, however are quite messy. One simple example is to examine how Coulomb's Law (which is a pure electric field of a charged particle in it own rest frame) transforms to a moving reference frame. A point in the moving reference frame will experience a magnetic field of:

Magnetic (and electric) field of a uniformly moving point charge

(

vector

form,

SI units

)

$\mathbf {B} ={\frac {q}{4\pi \varepsilon _{0}r^{3}}}{\frac {1-\beta ^{2}}{(1-\beta ^{2}\sin ^{2}\theta )^{3/2}}}{\frac {\mathbf {v} \times \mathbf {r} }{c^{2}}}={\frac {\mathbf {v} \times \mathbf {E} }{c^{2}}}\,,$

where q is the charge of the point source, $\varepsilon _{0}$ is the vacuum permittivity, $\mathbf {r}$ is the position vector from the point source to the point in space, $\mathbf {v}$ is the velocity vector of the charged particle, $\beta$ is the ratio of speed of the charged particle divided by the speed of light and $\theta$ is the angle between $\mathbf {r}$ and $\mathbf {v}$ .

Formally, special relativity combines the electric and magnetic fields into a rank-2 tensor, called the *electromagnetic tensor*. Changing reference frames *mixes* these components. This is analogous to the way that special relativity *mixes* space and time into spacetime, and mass, momentum, and energy into four-momentum. Similarly, the energy stored in a magnetic field is mixed with the energy stored in an electric field in the electromagnetic stress–energy tensor.

### Magnetic field of arbitrarily moving point charge

The solution of maxwell's equations for electric and magnetic field of a point charge is expressed in terms of retarded time or the time at which the particle in the past causes the field at the point, given that the influence travels across space at the speed of light. The retarded time for a point particle is given as solution of:

Definition of retarded time (which enforces causality)

(

vector

form,

SI units

)

$t_{r}=\mathbf {t} -{\frac {\left|\mathbf {r} -\mathbf {r} _{s}(t_{r})\right|}{c}}\,,$

where the retarded time ${\textstyle t_{r}}$ is the time at which the source's contribution of the field originated, ${\textstyle r_{s}(t)}$ is the position vector of the particle as function of time, ${\textstyle \mathbf {r} }$ is the point in space, ${\textstyle \mathbf {t} }$ is the time at which fields are measured and ${\textstyle c}$ is the speed of light. Any arbitrary motion of point charge causes electric and magnetic fields as follows:

Magnetic (and electric) field of an arbitrarily moving point charge

(

vector

form,

SI units

)

${\begin{aligned}\mathbf {B} (\mathbf {r} ,\mathbf {t} )&={\frac {\mu _{0}}{4\pi }}\left[{\frac {qc({\boldsymbol {\beta }}_{s}\times \mathbf {n} _{s})}{\gamma ^{2}{\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)}^{3}{\left|\mathbf {r} -\mathbf {r} _{s}\right|}^{2}}}+{\frac {q\mathbf {n} _{s}\times \left(\mathbf {n} _{s}\times \left(\left(\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}\right)\times {\dot {{\boldsymbol {\beta }}_{s}}}\right)\right)}{{\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)}^{3}\left|\mathbf {r} -\mathbf {r} _{s}\right|}}\right]_{t=t_{r}}\\[1ex]&={\frac {\mathbf {n} _{s}(t_{r})}{c}}\times \mathbf {E} (\mathbf {r} ,\mathbf {t} \,,)\end{aligned}}$

where q is the charge of the point source, $n_{s}$ is a unit vector pointing from charged particle to the point in space, ${\boldsymbol {\beta }}_{s}(t)$ is the velocity of the particle divided by the speed of light and $\gamma (t)$ is the corresponding Lorentz factor.

### Quantum electrodynamics

The classical electromagnetic field incorporated into quantum mechanics forms what is known as the semi-classical theory of radiation. However, it is not able to make experimentally observed predictions such as spontaneous emission process or Lamb shift implying the need for quantization of fields. In modern physics, the electromagnetic field is understood to be not a *classical* field, but rather a quantum field; it is represented not as a vector of three numbers at each point, but as a vector of three quantum operators at each point. The most accurate modern description of the electromagnetic interaction (and much else) is *quantum electrodynamics* (QED), which is incorporated into a more complete theory known as the *Standard Model of particle physics*.

In QED, the magnitude of the electromagnetic interactions between charged particles (and their antiparticles) is computed using perturbation theory. These rather complex formulas produce a remarkable pictorial representation as Feynman diagrams in which virtual photons are exchanged.

Predictions of QED agree with experiments to an extremely high degree of accuracy: currently about 10−12 (and limited by experimental errors); for details see precision tests of QED. This makes QED one of the most accurate physical theories constructed thus far.

All equations in this article are in the classical approximation, which is less accurate than the quantum description mentioned here. However, under most everyday circumstances, the difference between the two theories is negligible.


## Applications

### Uses in geology

#### Earth's magnetic field

The Earth's magnetic field is produced by convection of a liquid iron alloy in the outer core. In a dynamo process, the movements drive a feedback process in which electric currents create electric and magnetic fields that in turn act on the currents.

The field at the surface of the Earth is approximately the same as if a giant bar magnet were positioned at the center of the Earth and tilted at an angle of about 11° off the rotational axis of the Earth (see the figure). The north pole of a magnetic compass needle points roughly north, toward the North Magnetic Pole. However, because a magnetic pole is attracted to its opposite, the North Magnetic Pole is actually the south pole of the geomagnetic field. This confusion in terminology arises because the pole of a magnet is defined by the geographical direction it points.

Earth's magnetic field is not constant—the strength of the field and the location of its poles vary. Moreover, the poles periodically reverse their orientation in a process called geomagnetic reversal. The most recent reversal occurred 780,000 years ago.

#### Magnetic surveys

**Magnetic surveying** is one of a number of methods used in archaeological geophysics. Magnetic surveys record spatial variation in the Earth's magnetic field. In archaeology, magnetic surveys are used to detect and map archaeological artefacts and features. Magnetic surveys are used in both terrestrial and marine archaeology. In terrestrial archaeology, magnetic surveys are typically used for detailed mapping of archaeological features on known archaeological sites. More exceptionally, magnetometers are used for low-resolution exploratory surveys. Magnetic survey help to prove that a survey area has the potential for more detailed studies and scientific excavation. Magnetic surveys are extremely useful in the excavation and exploration of underwater archaeological sites. In maritime archaeology, these are often used to map the geology of wreck sites and determine the composition of magnetic materials found on the seafloor.

Measuring the Earths' magnetic field is a very useful tool in mineral exploration, oil exploration, and geological mapping. To cover large areas with uniform data, aircraft such as helicopters, airplanes, and drones are employed. The amount of detail is a function of flight height and sample density, in addition to instrument sensitivity. For surveys, drones are used which helps greatly in the process. Aeromagnetic surveys are also used to perform reconnaissance mapping of unexploded ordnance.

### Uses in engineering

#### Rotating magnetic fields

The *rotating magnetic field* is a common design principle in the operation of alternating-current motors. A permanent magnet in such a field rotates so as to maintain its alignment with the external field.

Magnetic torque is used to drive electric motors. In one simple motor design, a magnet is fixed to a freely rotating shaft and is subjected to a magnetic field from an array of electromagnets. By continuously switching the electric current through each of the electromagnets, thereby flipping the polarity of their magnetic fields, like poles are kept next to the rotor; the resultant torque is transferred to the shaft.

A rotating magnetic field can be constructed using two coils at right angles with a phase difference of 90 degrees between their AC currents. In practice, three-phase systems are used where the three currents are equal in magnitude and have a phase difference of 120 degrees. Three similar coils at mutual geometrical angles of 120 degrees create the rotating magnetic field. The ability of the three-phase system to create a rotating field, utilized in electric motors, is one of the main reasons why three-phase systems dominate the world's electrical power supply systems.

Synchronous motors use DC-voltage-fed rotor windings, which lets the excitation of the machine be controlled—and induction motors use short-circuited rotors (instead of a magnet) following the rotating magnetic field of a multicoiled stator. The short-circuited turns of the rotor develop eddy currents induced by the rotating field of the stator, and these currents in turn produce a torque on the rotor through the Lorentz force.

The Italian physicist Galileo Ferraris and the Serbian-American electrical engineer Nikola Tesla independently researched the use of rotating magnetic fields in electric motors. In 1888, Ferraris published his research in a paper to the *Royal Academy of Sciences* in Turin and Tesla gained U.S. patent 381,968 for his work.

#### Magnetic circuits

An important use of **H** is in *magnetic circuits*. A magnetic circuit is made up of one or more closed loop paths containing a magnetic flux. The flux is usually generated by permanent magnets or electromagnets and confined to the path by magnetic cores consisting of ferromagnetic materials like iron, although there may be air gaps or other materials in the path. Magnetic circuits are employed to efficiently channel magnetic fields in many devices such as electric motors, generators, transformers, relays, lifting electromagnets, SQUIDs, galvanometers, and magnetic recording heads.

The relation between the magnetic properties of a magnetic circuit can be described by Hopkinson's law, which bears a superficial resemblance to Ohm's law in electrical circuits, resulting in a one-to-one correspondence between properties of a magnetic circuit and an analogous electric circuit. Using this concept the magnetic fields of complex devices such as transformers can be quickly solved using the methods and techniques developed for electrical circuits. Hopkinson's law is:

Hopkinson's Law

$\Phi ={\frac {F}{R}}_{\mathrm {m} },$

where ${\textstyle \Phi =\int \mathbf {B} \cdot \mathrm {d} \mathbf {A} }$ is the magnetic flux in the circuit, ${\textstyle F=\int \mathbf {H} \cdot \mathrm {d} {\boldsymbol {\ell }}}$ is the magnetomotive force applied to the circuit, and *R*m is the magnetic reluctance of the circuit. Here the reluctance *R*m is a quantity similar in nature to resistance for the flux. Using this analogy it is straightforward to calculate the magnetic flux of complicated magnetic field geometries, by using all the available techniques of circuit theory.

#### Magnetic levitation

**Magnetic levitation** (**maglev**) or **magnetic suspension** is a method by which an object is suspended with no support other than magnetic fields. Magnetic force is used to counteract the effects of the gravitational force and any other forces. The two primary issues involved in magnetic levitation are (a) lifting forces – providing an upward force sufficient to counteract gravity, and (b) stability – ensuring that the system does not spontaneously slide or flip into a configuration where the lift is neutralized.

Magnetic levitation is used for maglev trains, contactless melting, magnetic bearings, and for product display purposes.

### Uses in material science

Magnetic field affects materials in a large number of ways.

#### Hall effect

The charge carriers of a current-carrying conductor placed in a transverse magnetic field experience a sideways Lorentz force; this results in a charge separation in a direction perpendicular to the current and to the magnetic field. The resultant voltage in that direction is proportional to the applied magnetic field. This is known as the *Hall effect*.

The *Hall effect* is often used to measure the magnitude of a magnetic field. It is used as well to find the sign of the dominant charge carriers in materials such as semiconductors (negative electrons or positive holes).

### Largest magnitude magnetic fields

The largest magnitude magnetic field produced over a macroscopic volume outside a lab setting is 2.8 kT (VNIIEF in Sarov, Russia, 1998). The largest magnitude magnetic field produced in a laboratory over a macroscopic volume was 1.2 kT by researchers at the University of Tokyo in 2018. The largest magnitude microscopic magnetic fields produced in a laboratory occur in particle accelerators, such as RHIC, inside the collisions of heavy ions, where microscopic fields reach 1014 T. Magnetars have the strongest known macroscopic magnetic fields of any naturally occurring object, ranging from 0.1 to 100 GT (108 to 1011 T).


## Common formulae

| Steady current configuration | Figure | Magnetic field |   |
|---|---|---|---|
| Finite beam of current |   | $B={\frac {\mu _{0}I}{4\pi x}}(\cos \theta _{1}+\cos \theta _{2})$ where I is the uniform current throughout the beam, with the direction of magnetic field as shown. |   |
| Infinite wire |   | $B={\frac {\mu _{0}I}{2\pi x}}$ where I is the uniform current flowing through the wire with the direction of magnetic field as shown. |   |
| Infinite cylindrical wire |   | $B={\frac {\mu _{0}I}{2\pi x}}$ outside the wire carrying a current I uniformly, with the direction of magnetic field as shown. | $B={\frac {\mu _{0}Ix}{2\pi R^{2}}}$ inside the wire carrying a current I uniformly, with the direction of magnetic field as shown. |
| Circular loop |   | $\mathbf {B} ={\frac {\mu _{0}IR^{2}}{2(x^{2}+R^{2})^{3/2}}}{\hat {\mathbf {x} }}$ along the axis of the loop, where I is the uniform current flowing through the loop. |   |
| Solenoid |   | $B={\frac {\mu _{0}nI}{2}}(\cos \theta _{1}+\cos \theta _{2})$ along the axis of the solenoid carrying current I with n , uniform number of loops of currents per length of solenoid; and the direction of magnetic field as shown. |   |
| Infinite solenoid |   | $\mathbf {B} =0$ outside the solenoid carrying current I with n , uniform number of loops of currents per length of solenoid. | $B=\mu _{0}nI$ inside the solenoid carrying current I with n , uniform number of loops of currents per length of solenoid, with the direction of magnetic field as shown. |
| Circular Toroid |   | $B={\frac {\mu _{0}NI}{2\pi R}}$ along the bulk of the circular toroid carrying uniform current I through N number of uniformly distributed poloidal loops, with the direction of magnetic field as indicated. |   |
| Magnetic Dipole |   | $\mathbf {B} =-{\frac {\mu _{0}\mathbf {m} }{4\pi r^{3}}},$ on the equatorial plane, where $\mathbf {m}$ is the magnetic dipole moment. | $\mathbf {B} ={\frac {\mu _{0}\mathbf {m} }{2\pi {\|x\|}^{3}}},$ on the axial plane (given that $x\gg R$ ), where x can also be negative to indicate position at the opposite direction on the axis, and $\mathbf {m}$ is the magnetic dipole moment. |

Additional magnetic field values can be found through the magnetic field of a finite beam, for example, that the magnetic field of an arc of angle $\theta$ and radius R at the center is $B={\mu _{0}\theta I \over 4\pi R}$ , or that the magnetic field at the center of a N-sided regular polygon of side a is $B={\mu _{0}NI \over \pi a}\sin {\pi \over N}\tan {\pi \over N}$ , both outside of the plane with proper directions as inferred by right hand thumb rule.


## History

### Early developments

While magnets and some properties of magnetism were known to ancient societies, the research of magnetic fields began in 1269 when French scholar Petrus Peregrinus de Maricourt mapped out the magnetic field on the surface of a spherical magnet using iron needles. Noting the resulting field lines crossed at two points he named those points "poles" in analogy to Earth's poles. He also articulated the principle that magnets always have both a north and south pole, no matter how finely one slices them.

In 1600 (almost three centuries later), William Gilbert of Colchester published *De Magnete*. In *De Magnete*, Gilbert replicated Petrus Peregrinus' work and was the first to state explicitly that Earth is a magnet. Too, he argued that electricity and magnetism were separate phenomenon.

### Magnetostatics

In 1750, John Michell stated that magnetic poles attract and repel in accordance with an inverse square law Charles-Augustin de Coulomb experimentally verified this in 1785 and stated explicitly that north and south poles cannot be separated. Building on this force between poles, Siméon Denis Poisson (1781–1840) created the first successful model of the magnetic field, which he presented in 1824.

Three discoveries in 1820 challenged this foundation of magnetism. Hans Christian Ørsted demonstrated that a current-carrying wire is surrounded by a circular magnetic field. Then André-Marie Ampère showed that parallel wires with currents attract one another if the currents are in the same direction and repel if they are in opposite directions. Finally, Jean-Baptiste Biot and Félix Savart announced empirical results about the forces that a current-carrying long, straight wire exerted on a small magnet, determining the forces were inversely proportional to the perpendicular distance from the wire to the magnet. Laplace later deduced a law of force based on the differential action of a differential section of the wire, which became known as the Biot–Savart law, as Laplace did not publish his findings.

Extending these experiments, Ampère published his own successful model of magnetism in 1825. In it, he showed the equivalence of electrical currents to magnets and proposed that magnetism is due to perpetually flowing loops of current instead of the dipoles of magnetic charge in Poisson's model. Further, Ampère derived both Ampère's force law describing the force between two currents and Ampère's law, which, like the Biot–Savart law, correctly described the magnetic field generated by a steady current.

### Electrodynamics

Also in his 1825 work, Ampère introduced the term electrodynamics to describe the relationship between electricity and magnetism.

In 1831, Michael Faraday discovered electromagnetic induction when he found that a changing magnetic field generates an encircling electric field, formulating what is now known as Faraday's law of induction. Later, Franz Ernst Neumann proved that, for a moving conductor in a magnetic field, induction is a consequence of Ampère's force law. In the process, he introduced the magnetic vector potential, which was later shown to be equivalent to the underlying mechanism proposed by Faraday. In 1850, Lord Kelvin, then known as William Thomson, distinguished between two magnetic fields now denoted **H** and **B**. The former applied to Poisson's model and the latter to Ampère's model and induction. Further, he derived how **H** and **B** relate to each other and coined the term *permeability*.

Between 1861 and 1865, James Clerk Maxwell developed and published Maxwell's equations, which explained and united all of classical electricity and magnetism. The first set of these equations was published in a paper entitled *On Physical Lines of Force* in 1861. These equations were valid but incomplete. Maxwell completed his set of equations in his later 1865 paper *A Dynamical Theory of the Electromagnetic Field* and demonstrated the fact that light is an electromagnetic wave. Heinrich Hertz published papers in 1887 and 1888 experimentally confirming this fact.

### Modern developments

In 1887, Tesla developed an induction motor that ran on alternating current. The motor used polyphase current, which generated a rotating magnetic field to turn the motor (a principle that Tesla claimed to have conceived in 1882). Tesla received a patent for his electric motor in May 1888. In 1885, Galileo Ferraris independently researched rotating magnetic fields and subsequently published his research in a paper to the *Royal Academy of Sciences* in Turin, just two months before Tesla was awarded his patent, in March 1888.

The twentieth century showed that classical electrodynamics is already consistent with special relativity, and extended classical electrodynamics to work with quantum mechanics. Albert Einstein, in his paper of 1905 that established relativity, showed that both the electric and magnetic fields are part of the same phenomena viewed from different reference frames. Finally, the emergent field of quantum mechanics was merged with electrodynamics to form quantum electrodynamics (or QED). QED mathematically describes all phenomena involving electrically charged particles interacting by means of exchange of photons and represents the quantum counterpart of classical electromagnetism giving a complete account of matter and light interaction.


## Links, references, and notes
