---
title: "Impulse (physics)"
source: https://en.wikipedia.org/wiki/Impulse_(physics)
domain: box2d-physics
license: CC-BY-SA-4.0
tags: box2d physics, box2d engine, 2d physics library, box2d body
fetched: 2026-07-02
---

# Impulse (physics)

In classical mechanics, **impulse** (symbolized by **J** or **Imp**) is the change in momentum of an object. It is most often used to describe forces which act over short time periods, specifically in the case of impacts and collisions, for which it gets its namesake. Impulse is a vector quantity, meaning it has both a magnitude, which describes the amount by which the momentum changed, and a direction, which describes the direction in which the momentum changed.

For a force acting over a short time, the impulse is often *idealized* so that the change in momentum produced by the force is modelled as happening instantaneously. This sort of change is a step change, and is not physically possible. However, this is a useful model for computing the effects of ideal collisions (such as in videogame physics engines). Additionally, in rocketry, the term "total impulse" is commonly used and is considered synonymous with the term "impulse".

Impulse has the same units and dimensions (LMT−1) as momentum. The SI unit of impulse is the newton-second (N⋅s), and the dimensionally equivalent unit of momentum is the kilogram-metre per second (kg⋅m/s). The corresponding English engineering unit is the pound-second (lbf⋅s), and in the British Gravitational System, the unit is the slug-foot per second (slug⋅ft/s).

## Definition

If, during a period of time, the initial momentum of an object is **p**i, and the final momentum is **p**f then the net impulse **J** on the object is defined as, $\mathbf {J} =\mathbf {p} _{\mathrm {f} }-\mathbf {p} _{\mathrm {i} }.$

By Newton's second law of motion, the rate of change of momentum of an object is equal to the resultant force **F** acting on the object: $\mathbf {F} ={\frac {\mathbf {p} _{\mathrm {f} }-\mathbf {p} _{\mathrm {i} }}{\Delta t}},$ so the impulse **J** delivered by a constant force **F** acting for time Δ*t* is: $\mathbf {J} =\mathbf {F} \Delta t.$

### Integral definition

In the continuous time case, the impulse delivered onto a constant mass by a varying force acting from time *t*1 to *t*2 is defined to be the integral of the force **F** with respect to time: $\mathbf {J} =\int _{t_{t}}^{t_{2}}\mathbf {F} \,\mathrm {d} t.$ From Newton's second law, force is related to momentum **p** by $\mathbf {F} ={\frac {\mathrm {d} \mathbf {p} }{\mathrm {d} t}}.$ Therefore, ${\begin{aligned}\mathbf {J} &=\int _{t_{1}}^{t_{2}}{\frac {\mathrm {d} \mathbf {p} }{\mathrm {d} t}}\,\mathrm {d} t\\&=\int _{\mathbf {p} _{1}}^{\mathbf {p} _{2}}\mathrm {d} \mathbf {p} \\&=\mathbf {p} _{2}-\mathbf {p} _{1}=\Delta \mathbf {p} ,\end{aligned}}$ where Δ**p** is the change in linear momentum from time *t*1 to *t*2. This is often called the impulse–momentum theorem (analogous to the work–energy theorem).

### Constant mass

As a result of the previous result, an impulse may also be regarded as the change in momentum of an object to which a resultant force is applied. The impulse may be expressed in a simpler form when the mass is constant: $\mathbf {J} =\int _{t_{1}}^{t_{2}}\mathbf {F} \,\mathrm {d} t=\Delta \mathbf {p} =m\mathbf {v_{2}} -m\mathbf {v_{1}} ,$ where

- **F** is the resultant force applied,
- *t*1 and *t*2 are times when the impulse begins and ends, respectively,
- m is the mass of the object,
- **v**2 is the final velocity of the object at the end of the time interval, and
- **v**1 is the initial velocity of the object when the time interval begins.

## Variable mass

The application of Newton's second law for variable mass allows impulse and momentum to be used as analysis tools for jet- or rocket-propelled vehicles. In the case of rockets, the impulse imparted can be normalized by unit of propellant expended, to create a performance parameter, specific impulse, the impulse per unit mass. This fact can be used to derive the Tsiolkovsky rocket equation, which relates the vehicle's propulsive change in velocity to the engine's specific impulse (or nozzle exhaust velocity) and the vehicle's propellant-mass ratio.

### Application: Newton's second law

Newton's second law is often written as $\mathbf {F} ={\frac {\mathrm {d} \mathbf {p} }{\mathrm {d} t}}.$ But this is the case only when there is no mass *transfer* into or out of **p**. When the mass of an object changes by exuding or accumulating mass, the momentum has a time dependence in its mass aspect as well as in its velocity aspect. If Newton's second law is applied naively, the erroneous conclusion is $\mathbf {F} =m{\frac {\mathrm {d} \mathbf {v} }{\mathrm {d} t}}+\mathbf {v} {\frac {\mathrm {d} m}{\mathrm {d} t}}\ \ \mathrm {(incorrect)} .$ Rather, suppose that the occurrence of the mass leaving or entering happens after every period Δ*t*, at which point a mass Δ*m* is exuded from the original mass m and proceeds to travel with velocity u. By Newton's third law, the impulse (i.e., the momentum transfer) between the two constant masses is equal and opposite, $\mathbf {J} _{m}=-\mathbf {J} _{\Delta m}.$ Thus, the impulse on *m* by Δ*m* is $\mathbf {J} _{m}=\Delta m(\mathbf {v} -\mathbf {u} ).$ Suppose an external force **F**ext is applied to the first object. Then, in a unit of time Δ*t*, it gains an impulse **J**ext = **F**extΔ*t* and then loses a mass Δ*m*, yielding the net impulse, $\mathbf {J} =\mathbf {J} _{\mathrm {ext} }+\mathbf {J} _{m}=\mathbf {F} _{\mathrm {ext} }\Delta t+\Delta m(\mathbf {v} -\mathbf {u} ).$ Hence, what we find is that in the infinitesimal limit, that, $\mathbf {F} _{\mathrm {ext} }=m\mathbf {a} -{\frac {\mathrm {d} m}{\mathrm {d} t}}(\mathbf {u} -\mathbf {v} ).$ Relating this back to Newton's second law, we have that the law applies only to the *total momentum* **P** of the system. Using this and labeling mass that has left the system with *ex*, ${\begin{aligned}\mathbf {F} _{\mathrm {ext} }&={\frac {\mathrm {d} \mathbf {P} }{\mathrm {d} t}}\\&={\frac {\mathrm {d} \mathbf {p} }{\mathrm {d} t}}+{\frac {\mathrm {d} \mathbf {p} _{\mathrm {ex} }}{\mathrm {d} t}}\\&=m\mathbf {a} +\mathbf {v} {\frac {\mathrm {d} m}{\mathrm {d} t}}+\mathbf {v} _{\mathrm {ex} }{\frac {\mathrm {d} m_{\mathrm {ex} }}{\mathrm {d} t}}\\&=m\mathbf {a} -{\frac {\mathrm {d} m}{\mathrm {d} t}}(\mathbf {u} -\mathbf {v} ),\end{aligned}}$ yielding the same result. Thus, using either the step-wise impulse method or the infinitesimal Newtonian force method work in this case.

### Application: specific impulse

Suppose our previous example was for a rocket. Then, using the equation for **J**, we have that the specific impulse *I*sp is $I_{\mathrm {sp} }=\mathbf {v} -\mathbf {u} .$ In this case, we call this quantity the exhaust velocity since it is equal to the velocity at which the material is leaving the rocket relative to the frame of the rocket. The thrust **T** is then ${\textstyle \mathbf {T} =-{\frac {\mathrm {d} m}{\mathrm {d} t}}I_{\mathrm {sp} }={\frac {\mathrm {d} m}{\mathrm {d} t}}(\mathbf {v} -\mathbf {u} ).}$
