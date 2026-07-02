---
title: "Faraday's law of induction"
source: https://en.wikipedia.org/wiki/Faraday's_law_of_induction
domain: maxwell-equations
license: CC-BY-SA-4.0
tags: maxwell's equations, gauss's law, displacement current, electromagnetic wave equation
fetched: 2026-07-02
---

# Faraday's law of induction

Motional emf, induced by moving a conductor through a magnetic field.

Transformer emf, induced by a changing magnetic field.

In electromagnetism, **Faraday's law of induction** describes how a changing magnetic field can induce an electric current in a circuit. This phenomenon, known as electromagnetic induction, is the fundamental operating principle of transformers, inductors, and many types of electric motors, generators and solenoids.

In the literature, however, *Faraday's law* is used to refer to two closely related but technically distinct statements, either of which can be used to explain the phenomenon of induced current described above. One is the **Maxwell–Faraday equation**, one of Maxwell's equations, which states that a time-varying magnetic field is always accompanied by a circulating electric field. This law applies to the fields themselves and does not require the presence of a physical circuit.

The other is **Faraday's flux rule**, or the **Faraday–Lenz law**, which relates the electromotive force (emf) around a closed conducting loop to the time rate of change of magnetic flux through the loop. This rule can be derived from the first in specific context of a closed circuit. The flux rule accounts for two mechanisms by which an emf can be generated. In *transformer emf*, a time-varying magnetic field induces an electric field as described by the Maxwell–Faraday equation, and the electric field drives a current around the loop. In *motional emf*, the circuit moves through a magnetic field, and the emf arises from the magnetic component of the Lorentz force acting on the charges in the conductor.

Historically, the differing explanations for motional emf and transformer emf posed a conceptual problem, since the observed current depends only on relative motion, but the physical explanations were different in the two cases. In special relativity, this distinction is understood as frame-dependent: what appears as a magnetic force in one frame may appear as an induced electric field in another.

## History

In 1820, Hans Christian Ørsted demonstrated that an electric current produces a magnetic field, showing that a compass needle could be deflected by a nearby current-carrying wire. This discovery prompted scientists to ask whether the reverse was also true—whether a magnetic field could generate an electric current.

Initial experiments revealed that a static magnetic field had no effect on a nearby circuit: simply placing a magnet near a wire loop produced no current. The breakthrough came in 1831, when Michael Faraday demonstrated that a changing magnetic field could indeed induce an electric current in a circuit. Independently, Joseph Henry made similar observations in 1832, though Faraday was the first to publish his findings.

Faraday's notebook on August 29, 1831 describes an experimental demonstration of induction. He wrapped two coils of wire around opposite sides of an iron ring, forming a primitive toroidal transformer. When he connected one coil to a battery, he observed a brief deflection in a galvanometer attached to the second coil. He concluded that a changing current in the first coil created a changing magnetic field in the ring, which in turn induced a current in the second coil. He described this as a "wave of electricity" propagated through the iron.

Over the following months, Faraday discovered other manifestations of electromagnetic induction. He observed transient currents when a bar magnet was rapidly moved into or out of a coil of wire. He also built a device, now known as Faraday's disk or homopolar generator, that produced a steady (DC) current by rotating a copper disk in the presence of a stationary magnet, using a sliding electrical contact.

Faraday explained these phenomena using the concept of lines of force. However, his theoretical ideas were met with skepticism, as they were not formulated mathematically.

Lenz's law, formulated by Emil Lenz in 1834, describes "flux through the circuit", and gives the direction of the induced emf and current resulting from electromagnetic induction (elaborated upon in the examples below).

The laws of induction of electric currents in mathematical form were established by Franz Ernst Neumann in 1845. Wilhelm Eduard Weber also provided a formulation in terms of Weber electrodynamics.

Starting in 1851, Riccardo Felici carried out several experiments on induction based on Neumann. Felici came up with Felici's law, a version of the law of induction.

James Clerk Maxwell later gave Faraday's insights mathematical expression, incorporating them into his broader electromagnetic theory in the early 1860s. Maxwell cited the works of Faraday, Neumann, Weber and Felici.

In Maxwell's papers, the time-varying aspect of electromagnetic induction is expressed as a differential equation which Oliver Heaviside referred to as Faraday's law even though it is different from the original version of Faraday's law, and does not describe motional emf. Heaviside's version from 1890s is the form recognized today in the group of equations known as Maxwell's equations.

According to Albert Einstein, much of the groundwork and discovery of his special relativity theory was presented by this law of induction by Faraday in 1834.

## Flux rule

Faraday's law of induction, also known as the *flux rule*, *flux law*, and *Faraday–Lenz law*, states that the electromotive force (emf) around a closed circuit is equal to the negative rate of change of the magnetic flux through the circuit. This rule holds for any circuit made of thin wire and accounts for changes in flux due to variations in the magnetic field, movement of the circuit, or deformation of its shape. The direction of the induced emf is given by Lenz's law, which states that the induced current will flow in such a way that its magnetic field opposes the change in the original magnetic flux.

Mathematically, in SI units, the law is expressed as ${\mathcal {E}}=-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}},$ where ${\mathcal {E}}$ is the electromotive force (emf) and Φ*B* is the magnetic flux through the circuit. The magnetic flux is defined as the surface integral of the magnetic field **B** over a time-dependent surface Σ(*t*), whose boundary is the wire loop: $\Phi _{B}=\iint _{\Sigma (t)}\mathbf {B} (t)\cdot \mathrm {d} \mathbf {A} \,,$ where d**A** is an infinitesimal area vector normal to the surface. The dot product **B** · d**A** represents the flux through the differential area element. In more visual terms, the magnetic flux is proportional to the number of magnetic field lines passing through the loop.

When the flux changes, an emf is induced around the loop. This emf corresponds to the energy per unit charge required to move it once around the loop. In a simple circuit with resistance R , an emf ${\mathcal {E}}$ gives rise to a current I according to the Ohm's law ${\mathcal {E}}=IR$ . Equivalently, if the loop is broken to form an open circuit and a voltmeter is connected across the terminals, the emf is equal to the voltage measured across the open ends.

For a tightly wound coil of wire, composed of N identical turns, the same magnetic field lines cross the surface N times. In this case, Faraday's law of induction states that ${\mathcal {E}}=-N{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}$ where N is the number of turns of wire and Φ*B* is the magnetic flux through a single loop. The product *N*Φ*B* is known as linked flux.

The flux can change either because the loop moves or deforms over time, or because the field itself varies in time. These two possibilities correspond to the two mechanisms described by the flux rule:

- *Motional emf*: The circuit moves through a static but non-uniform magnetic field.
- *Transformer emf*: The circuit remains stationary while the magnetic field changes over time.

### Motional emf

The basic mechanism behind motional emf is illustrated by a conducting rod moving through a magnetic field that is perpendicular to both the rod and its direction of motion. Due to movement in magnetic field, the mobile electrons of the conductor experience the magnetic component (*q***v** × **B**) of the Lorentz force that drives them along the length of the rod. This leads to a separation of charge between the two ends of the rod. In the steady state, the electric field from the accumulated charge balances the magnetic force.

If the rod is part of a closed conducting loop moving through a nonuniform magnetic field, the same effect can drive a current around the circuit. For instance, suppose the magnetic field is confined to a limited region of space, and the loop initially lies outside this region. As it moves into the field, the area of the loop that encloses magnetic flux increases, and an emf is induced. From the Lorentz force perspective, this is because the field exerts a magnetic force on charge carriers in the parts of the loop entering the region. Once the entire loop lies in a uniform magnetic field and continues at constant speed, the total enclosed flux remains constant, and the emf vanishes. In this situation, magnetic forces on opposite sides of the loop cancel out.

### Transformer emf

A complementary case is transformer emf, which occurs when the conducting loop remains stationary but the magnetic flux through it changes due to a time-varying magnetic field. This can happen in two ways: either the source of the magnetic field moves, altering the field distribution through the fixed loop, or the strength of the magnetic field changes over time at a fixed location, as in the case of a powered electromagnet.

In either situation, no magnetic force acts on the charges, and the emf is entirely due to the electric component (*q***E**) of the Lorentz force. According to the Maxwell–Faraday equation, a time-varying magnetic field produces a circulating electric field, which drives current in the loop. This phenomenon underlies the operation of electrical machines such as synchronous generators. The electric field induced in this way is non-conservative, meaning its line integral around a closed loop is not zero.

### Direction of the induced current

It is possible to find out the direction of the electromotive force (emf) directly from Faraday's law, without invoking Lenz's law. A left hand rule helps doing that, as follows:

- Align the curved fingers of the left hand with the loop (yellow line).
- Stretch your thumb. The stretched thumb indicates the direction of **n** (brown), the normal to the area enclosed by the loop.
- Find the sign of ΔΦ*B*, the change in flux. Determine the initial and final fluxes (whose difference is ΔΦ*B*) with respect to the normal **n**, as indicated by the stretched thumb.
- If the change in flux, ΔΦ*B*, is positive, the curved fingers show the direction of the electromotive force (yellow arrowheads).
- If ΔΦ*B* is negative, the direction of the electromotive force is opposite to the direction of the curved fingers (opposite to the yellow arrowheads).

## Maxwell–Faraday equation

The Maxwell–Faraday equation is one of the four Maxwell's equations, and therefore plays a fundamental role in the theory of classical electromagnetism. It states that a time-varying magnetic field always accompanies a spatially varying, non-conservative electric field. In differential form and in SI units, it reads:

$\nabla \times \mathbf {E} =-{\frac {\partial \mathbf {B} }{\partial t}}$

where ∇ × is the curl operator, **E**(**r**, *t*) is the electric field and **B**(**r**, *t*) is the magnetic field. These fields can generally be functions of position **r** and time t.

It can also be written in an integral form by the Kelvin–Stokes theorem:

$\oint _{\partial \Sigma }\mathbf {E} \cdot \mathrm {d} \mathbf {l} =-\iint _{\Sigma }{\frac {\partial \mathbf {B} }{\partial t}}\cdot \mathrm {d} \mathbf {A}$

where, as indicated in the figure, **Σ** is a surface bounded by the closed loop ∂**Σ** and d**l** is an infinitesimal vector element along that loop. The vector area element d**A** is perpendicular to the surface and oriented according to the right-hand rule: when the thumb points in the direction of the d**A**, the curled fingers indicate the direction of d**l** along the boundary.

The left-hand side of the equation represents the circulation of the electric field around the loop ∂**Σ**. For static electric fields, the circulation is zero, since the field can be expressed as the gradient of a scalar potential. In contrast, a time-varying magnetic field produces a non-conservative electric field with nonzero circulation. When such field acts on a conducting loop, it drives a current around the loop.

If the surface **Σ** is not changing in time, the right-hand side equation becomes the time-derivative of the magnetic flux Φ*B* through the surface: $\oint _{\partial \Sigma }\mathbf {E} \cdot \mathrm {d} \mathbf {l} =-{\frac {\mathrm {d} }{\mathrm {d} t}}\iint _{\Sigma }\mathbf {B} \cdot \mathrm {d} \mathbf {A} =-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}.$ If the left-hand side is identified with the work per unit charge done by the electric field on charges in a fixed conducting loop, this equation reproduces the flux rule in the special case of a stationary circuit.

In the non-relativistic limit, the solenoidal component of the induced electric field can be approximated by the volume integral $\mathbf {E} _{s}(\mathbf {r} ,t)\approx -{\frac {1}{4\pi }}\iiint _{V}\ {\frac {\left({\frac {\partial \mathbf {B} (\mathbf {r} ',t)}{\partial t}}\right)\times \left(\mathbf {r} -\mathbf {r} '\right)}{|\mathbf {r} -\mathbf {r} '|^{3}}}d^{3}\mathbf {r'}$ This expression shows how changes in the magnetic field across space contribute to the induced electric field at a given point, with each contribution weighted by the inverse square of the distance.

## Derivation of the flux rule from microscopic equations

The four Maxwell's equations, together with the Lorentz force law, form a complete foundation for classical electromagnetism. From these, Faraday's law can be derived directly.

The derivation begins by considering the time derivative of the magnetic flux through a surface Σ(t) that may vary with time: ${\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}={\frac {\mathrm {d} }{\mathrm {d} t}}\iint _{\Sigma (t)}\mathbf {B} (t)\cdot \mathrm {d} \mathbf {A} .$ The magnetic flux can change for two reasons: the magnetic field itself may vary with time, and the surface may move or change shape, enclosing a different region of space. Both effects are captured by the three-dimensional version of the Leibniz integral rule, sometimes referred to as the "flux theorem": ${\frac {\mathrm {d} }{\mathrm {d} t}}\iint _{\Sigma (t)}\mathbf {B} \cdot \mathrm {d} \mathbf {A} =\iint _{\Sigma (t)}\left({\frac {\partial \mathbf {B} }{\partial t}}+(\nabla \cdot \mathbf {B} )\mathbf {v} _{c}\right)\cdot \mathrm {d} \mathbf {A} -\oint _{\partial \Sigma (t)}(\mathbf {v} _{c}\times \mathbf {B} )\cdot \mathrm {d} \mathbf {l}$ Here, ⁠ $\partial \Sigma (t)$ ⁠ is the moving boundary of the surface and $\mathbf {v} _{c}$ is the local velocity of the boundary at each point. By Gauss's law for magnetism (⁠ $\nabla \cdot \mathbf {B} =0$ ⁠), the second term under the area integral vanishes. Applying the Maxwell–Faraday equation to the remaining term, $\iint _{\Sigma (t)}{\frac {\partial \mathbf {B} }{\partial t}}\cdot \mathrm {d} \mathbf {A} =-\oint _{\partial \Sigma (t)}\mathbf {E} \cdot \mathrm {d} \mathbf {l} ,$ and combining the two line integrals gives ${\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}=-\oint _{\partial \Sigma (t)}\left(\mathbf {E} +\mathbf {v} _{c}\times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} .$ This is an exact result, derived from Maxwell's equations and vector calculus.

However, the quantity inside the integral is not the full Lorentz force per unit charge, because the velocity $\mathbf {v} _{c}$ represents the motion of loop boundary, not the actual velocity of the charge carriers. To recover the physical electromotive force, we must distinguish between these velocities. Let us choose the integration path to coincide with the physical circuit. The velocity of a charge carrier in the conductor is then given by $\mathbf {v} (\mathbf {r} ,t)=\mathbf {v} _{c}(\mathbf {r} ,t)+\mathbf {v} _{d}(\mathbf {r} ,t),$ where $\mathbf {v} _{c}$ is the velocity of the conductor (the ions in the material), and $\mathbf {v} _{d}$ is the drift velocity of the electrons relative to the material. This decomposition assumes nonrelativistic (Galilean) addition of velocities.

The emf ${\mathcal {E}}$ associated with the Lorentz force is defined as ${\mathcal {E}}=\oint _{\partial \Sigma (t)}\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} .$

Substituting the expression for the carrier velocity and the above result yields:

${\mathcal {E}}=-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}+\oint _{\partial \Sigma (t)}\left(\mathbf {v} _{d}\times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} .$

Equivalently, this can be expressed as ${\mathcal {E}}=-\iint _{\Sigma (t)}{\frac {\partial \mathbf {B} }{\partial t}}\cdot {\rm {d}}\mathbf {A} +\oint _{\partial \Sigma (t)}\left(\mathbf {v} \times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} ,$ where the first term is the "transformer emf" due to a time-varying magnetic field, and the second term is the "motional emf" due to the magnetic Lorentz force by the motion of the charges in the magnetic field.

In circuits made of thin, one-dimensional wires, the drift velocity is aligned with the wire, and hence with the integration element ⁠ $\mathrm {d} \mathbf {l}$ ⁠. In that case, the cross product ${\textstyle \mathbf {v} _{d}\times \mathbf {B} }$ is perpendicular to ⁠ $\mathrm {d} \mathbf {l}$ ⁠, and the term proportional to the drift velocity vanishes. This recovers the standard form of Faraday's law: ${\mathcal {E}}=-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}$ In this case, the emf can also be expressed as a sum ${\mathcal {E}}=-\iint _{\Sigma (t)}{\frac {\partial \mathbf {B} }{\partial t}}\cdot \mathrm {d} \mathbf {A} +\oint _{\partial \Sigma (t)}\left(\mathbf {v} _{c}\times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} .$ In conductors that are not thin wires, the drift velocity term ${\textstyle \oint _{\partial \Sigma (t)}\left(\mathbf {v} _{d}\times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} }$ may not vanish exactly. However, electrons typically drift at speeds of the order of 10−4 m/s, and the contribution is often negligible compared to other effects. A notable exception is the Hall effect, where magnetic flux term ${\textstyle \mathrm {d} \Phi _{B}/\mathrm {d} t}$ vanishes, and the observed Hall voltage arises entirely from the drift velocity term.

## Limitations of the flux rule

It is tempting to generalize Faraday's law to state: *If*∂Σ*is any arbitrary closed loop in space whatsoever, then the total time derivative of magnetic flux through*Σ*equals the emf around*∂Σ*.* This statement, however, is not always true. As noted in the previous section, Faraday's law is not guaranteed to work unless the velocity of the abstract curve ∂Σ matches the actual velocity of the material conducting the electricity. If the conductor is not an infinitely thin wire, one may also have take into account the velocity of charges with respect to the material. The two examples illustrated below show that one often obtains incorrect results when Faraday's law is applied too broadly.

- (Faraday's homopolar generator. The disc rotates with angular rate ω, sweeping the conducting radius circularly in the static magnetic field B (which direction is along the disk surface normal). The magnetic Lorentz force v × B drives a current along the conducting radius to the conducting rim, and from there the circuit completes through the lower brush and the axle supporting the disc. This device generates an emf and a current, although the shape of the "circuit" is constant and thus the flux through the circuit does not change with time.) Faraday's homopolar generator. The disc rotates with angular rate ω, sweeping the conducting radius circularly in the static magnetic field **B** (which direction is along the disk surface normal). The magnetic Lorentz force **v** × **B** drives a current along the conducting radius to the conducting rim, and from there the circuit completes through the lower brush and the axle supporting the disc. This device generates an emf and a current, although the shape of the "circuit" is constant and thus the flux through the circuit does not change with time.
- (A wire (solid red lines) connects to two touching metal plates (silver) to form a circuit. The whole system sits in a uniform magnetic field, normal to the page. If the abstract path ∂Σ follows the primary path of current flow (marked in red), then the magnetic flux through this path changes dramatically as the plates are rotated, yet the emf is almost zero. After Feynman Lectures on Physics: ch17) A wire (solid red lines) connects to two touching metal plates (silver) to form a circuit. The whole system sits in a uniform magnetic field, normal to the page. If the abstract path ∂Σ follows the primary path of current flow (marked in red), then the magnetic flux through this path changes dramatically as the plates are rotated, yet the emf is almost zero. After *Feynman Lectures on Physics*

One can analyze examples like these by taking care that the path ∂Σ moves with the same velocity as the material. The electromotive force can always be correctly calculated by combining the Lorentz force law with the Maxwell–Faraday equation: ${\mathcal {E}}=\int _{\partial \Sigma }(\mathbf {E} +\mathbf {v} \times \mathbf {B} )\cdot \mathrm {d} \mathbf {l} =-\int _{\partial \Sigma (t)}{\frac {\partial \mathbf {B} }{\partial t}}\cdot {\rm {d}}\mathbf {A} +\oint _{\partial \Sigma (t)}\left(\mathbf {v} \times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} ,$ where **v** is the velocity of the conductor in the frame of reference in which **B** in described. The time derivative cannot in general be moved outside the integral since the position or shape of the loop may be a function of time.

## Flux rule and relativity

Historically, the two distinct mechanisms encompassed by the flux rule, motional emf and transformer emf, posed a conceptual challenge. James Clerk Maxwell already recognized that electromagnetic induction could arise through different physical processes, even though the induced emf obeyed a single mathematical expression. In his 1861 paper *On Physical Lines of Force*, he gave separate physical explanations for each case.

In 1905, Albert Einstein highlighted this asymmetry in classical electrodynamics in his paper *On the Electrodynamics of Moving Bodies*. He pointed out that the physical outcome, such as the induced current, depends only on relative motion between the conductor and the magnet, yet classical theory provided different explanations depending on which object was considered to be in motion. This inconsistency suggested the absence of a preferred frame and helped motivate the development of special relativity.

In modern terms, electric and magnetic fields are understood as components of a single electromagnetic field tensor. Under a change of inertial frame, the two fields transform into one another.
