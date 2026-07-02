---
title: "Generalized coordinates"
source: https://en.wikipedia.org/wiki/Generalized_coordinates
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
---

# Generalized coordinates

In analytical mechanics, **generalized coordinates** are a set of parameters used to represent the configuration of a system in a configuration space. These parameters must uniquely define the configuration of the system relative to a reference configuration. The **generalized velocities** are the time derivatives of the generalized coordinates of the system. The adjective "generalized" distinguishes these parameters from the traditional use of the term "coordinate" to refer to Cartesian coordinates.

An example of a generalized coordinate would be to describe the position of a pendulum using the angle of the pendulum relative to vertical, rather than by the x and y position of the pendulum.

Although there may be many possible choices for generalized coordinates for a physical system, they are generally selected to simplify calculations, such as the solution of the equations of motion for the system. If the coordinates are independent of one another, the number of independent generalized coordinates is defined by the number of degrees of freedom of the system.

Generalized coordinates are paired with generalized momenta to provide canonical coordinates on phase space.

## Constraints and degrees of freedom

Open straight path

Open curved path

F

(

x

,

y

) = 0

Closed curved path

C

(

x

,

y

) = 0

One generalized coordinate (one degree of freedom) on paths in 2D. Only one generalized coordinate is needed to uniquely specify positions on the curve. In these examples, that variable is either arc length

s

or angle

θ

. Having both of the Cartesian coordinates

(

x

,

y

)

are unnecessary since either

x

or

y

is related to the other by the equations of the curves. They can also be parameterized by

s

or

θ

.

Open curved path

F

(

x

,

y

) = 0

. Multiple intersections of radius with path.

Closed curved path

C

(

x

,

y

) = 0

. Self-intersection of path.

The arc length

s

along the curve is a legitimate generalized coordinate since the position is uniquely determined, but the angle

θ

is not since there are multiple positions for a single value of

θ

.

Generalized coordinates are usually selected to provide the minimum number of independent coordinates that define the configuration of a system, which simplifies the formulation of Lagrange's equations of motion. However, it can also occur that a useful set of generalized coordinates may be *dependent*, which means that they are related by one or more constraint equations.

### Holonomic constraints

Open curved surface

F

(

x

,

y

,

z

) = 0

Closed curved surface

S

(

x

,

y

,

z

) = 0

Two generalized coordinates, two degrees of freedom, on curved surfaces in 3D. Only two numbers

(

u

,

v

)

are needed to specify the points on the curve, one possibility is shown for each case. The full three

Cartesian coordinates

(

x

,

y

,

z

)

are not necessary because any two determines the third according to the equations of the curves.

For a system of N particles in 3D real coordinate space, the position vector of each particle can be written as a 3-tuple in Cartesian coordinates:

${\begin{aligned}&\mathbf {r} _{1}=(x_{1},y_{1},z_{1}),\\&\mathbf {r} _{2}=(x_{2},y_{2},z_{2}),\\&\qquad \qquad \vdots \\&\mathbf {r} _{N}=(x_{N},y_{N},z_{N})\end{aligned}}$

Any of the position vectors can be denoted **r***k* where *k* = 1, 2, …, *N* labels the particles. A *holonomic constraint* is a *constraint equation* of the form for particle k

$f(\mathbf {r} _{k},t)=0$

which connects all the 3 spatial coordinates of that particle together, so they are not independent. The constraint may change with time, so time t will appear explicitly in the constraint equations. At any instant of time, any one coordinate will be determined from the other coordinates, e.g. if xk and zk are given, then so is yk. One constraint equation counts as *one* constraint. If there are C constraints, each has an equation, so there will be C constraint equations. There is not necessarily one constraint equation for each particle, and if there are no constraints on the system then there are no constraint equations.

So far, the configuration of the system is defined by 3*N* quantities, but C coordinates can be eliminated, one coordinate from each constraint equation. The number of independent coordinates is *n* = 3*N* − *C*. (In D dimensions, the original configuration would need ND coordinates, and the reduction by constraints means *n* = *ND* − *C*). It is ideal to use the minimum number of coordinates needed to define the configuration of the entire system, while taking advantage of the constraints on the system. These quantities are known as **generalized coordinates** in this context, denoted *qj*(*t*). It is convenient to collect them into an n-tuple

$\mathbf {q} (t)=(q_{1}(t),\ q_{2}(t),\ \ldots ,\ q_{n}(t))$

which is a point in the *configuration space* of the system. They are all independent of one other, and each is a function of time. Geometrically they can be lengths along straight lines, or arc lengths along curves, or angles; not necessarily Cartesian coordinates or other standard orthogonal coordinates. There is one for each degree of freedom, so the number of generalized coordinates equals the number of degrees of freedom, n. A degree of freedom corresponds to one quantity that changes the configuration of the system, for example the angle of a pendulum, or the arc length traversed by a bead along a wire.

If it is possible to find from the constraints as many independent variables as there are degrees of freedom, these can be used as generalized coordinates. The position vector **r***k* of particle k is a function of all the n generalized coordinates (and, through them, of time),

$\mathbf {r} _{k}=\mathbf {r} _{k}(\mathbf {q} (t))\,,$

and the generalized coordinates can be thought of as parameters associated with the constraint.

The corresponding time derivatives of **q** are the generalized velocities,

${\dot {\mathbf {q} }}={\frac {d\mathbf {q} }{dt}}=({\dot {q}}_{1}(t),\ {\dot {q}}_{2}(t),\ \ldots ,\ {\dot {q}}_{n}(t))$

(each dot over a quantity indicates one time derivative). The velocity vector **v***k* is the total derivative of **r***k* with respect to time

$\mathbf {v} _{k}={\dot {\mathbf {r} }}_{k}={\frac {d\mathbf {r} _{k}}{dt}}=\sum _{j=1}^{n}{\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}{\dot {q}}_{j}\,.$

and so generally depends on the generalized velocities and coordinates. Since we are free to specify the initial values of the generalized coordinates and velocities separately, the generalized coordinates qj and velocities *dqj*/*dt* can be treated as *independent variables*.

### Non-holonomic constraints

A mechanical system can involve constraints on both the generalized coordinates and their derivatives. Constraints of this type are known as non-holonomic. First-order non-holonomic constraints have the form

$g(\mathbf {q} ,{\dot {\mathbf {q} }},t)=0\,,$

An example of such a constraint is a rolling wheel or knife-edge that constrains the direction of the velocity vector. Non-holonomic constraints can also involve next-order derivatives such as generalized accelerations.

## Physical quantities in generalized coordinates

### Kinetic energy

The total kinetic energy of the system is the energy of the system's motion, defined as

$T={\frac {1}{2}}\sum _{k=1}^{N}m_{k}{\dot {\mathbf {r} }}_{k}\cdot {\dot {\mathbf {r} }}_{k}\,,$

in which · is the dot product. The kinetic energy is a function only of the velocities **v***k*, not the coordinates **r***k* themselves. By contrast an important observation is

${\dot {\mathbf {r} }}_{k}\cdot {\dot {\mathbf {r} }}_{k}=\sum _{i,j=1}^{n}\left({\frac {\partial \mathbf {r} _{k}}{\partial q_{i}}}\cdot {\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}\right){\dot {q}}_{i}{\dot {q}}_{j},$

which illustrates the kinetic energy is in general a function of the generalized velocities, coordinates, and time if the constraints also vary with time, so *T* = *T*(**q**, *d***q**/*dt*, *t*).

In the case the constraints on the particles are time-independent, then all partial derivatives with respect to time are zero, and the kinetic energy is a homogeneous function of degree 2 in the generalized velocities.

Still for the time-independent case, this expression is equivalent to taking the line element squared of the trajectory for particle k,

$ds_{k}^{2}=d\mathbf {r} _{k}\cdot d\mathbf {r} _{k}=\sum _{i,j=1}^{n}\left({\frac {\partial \mathbf {r} _{k}}{\partial q_{i}}}\cdot {\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}\right)dq_{i}dq_{j}\,,$

and dividing by the square differential in time, *dt*2, to obtain the velocity squared of particle k. Thus for time-independent constraints it is sufficient to know the line element to quickly obtain the kinetic energy of particles and hence the Lagrangian.

It is instructive to see the various cases of polar coordinates in 2D and 3D, owing to their frequent appearance. In 2D polar coordinates (*r*, *θ*),

$\left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}\,,$

in 3D cylindrical coordinates (*r*, *θ*, *z*),

$\left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}+{\dot {z}}^{2}\,,$

in 3D spherical coordinates (*r*, *θ*, *φ*),

$\left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}+r^{2}\sin ^{2}\theta \,{\dot {\varphi }}^{2}\,.$

### Generalized momentum

The *generalized momentum* "canonically conjugate to" the coordinate qi is defined by

$p_{i}={\frac {\partial L}{\partial {\dot {q}}_{i}}}.$

If the Lagrangian L does *not* depend on some coordinate qi, then it follows from the Euler–Lagrange equations that the corresponding generalized momentum will be a conserved quantity, because the time derivative is zero implying the momentum is a constant of the motion;

${\frac {\partial L}{\partial q_{i}}}={\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}_{i}}}={\dot {p}}_{i}=0\,.$

## Examples

### Bead on a wire

For a bead sliding on a frictionless wire subject only to gravity in 2d space, the constraint on the bead can be stated in the form *f* (**r**) = 0, where the position of the bead can be written **r** = (*x*(*s*), *y*(*s*)), in which s is a parameter, the arc length s along the curve from some point on the wire. This is a suitable choice of generalized coordinate for the system. Only *one* coordinate is needed instead of two, because the position of the bead can be parameterized by one number, s, and the constraint equation connects the two coordinates x and y; either one is determined from the other. The constraint force is the reaction force the wire exerts on the bead to keep it on the wire, and the non-constraint applied force is gravity acting on the bead.

Suppose the wire changes its shape with time, by flexing. Then the constraint equation and position of the particle are respectively

$f(\mathbf {r} ,t)=0\,,\quad \mathbf {r} =(x(s,t),y(s,t))$

which now both depend on time t due to the changing coordinates as the wire changes its shape. Notice time appears implicitly via the coordinates *and* explicitly in the constraint equations.

### Simple pendulum

The relationship between the use of generalized coordinates and Cartesian coordinates to characterize the movement of a mechanical system can be illustrated by considering the constrained dynamics of a simple pendulum.

A simple pendulum consists of a mass M hanging from a pivot point so that it is constrained to move on a circle of radius L. The position of the mass is defined by the coordinate vector **r** = (*x*, *y*) measured in the plane of the circle such that y is in the vertical direction. The coordinates x and y are related by the equation of the circle

$f(x,y)=x^{2}+y^{2}-L^{2}=0,$

that constrains the movement of M. This equation also provides a constraint on the velocity components,

${\dot {f}}(x,y)=2x{\dot {x}}+2y{\dot {y}}=0.$

Now introduce the parameter θ, that defines the angular position of M from the vertical direction. It can be used to define the coordinates x and y, such that

$\mathbf {r} =(x,y)=(L\sin \theta ,-L\cos \theta ).$

The use of θ to define the configuration of this system avoids the constraint provided by the equation of the circle.

Notice that the force of gravity acting on the mass m is formulated in the usual Cartesian coordinates,

$\mathbf {F} =(0,-mg),$

where g is the acceleration due to gravity.

The virtual work of gravity on the mass m as it follows the trajectory **r** is given by

$\delta W=\mathbf {F} \cdot \delta \mathbf {r} .$

The variation δ**r** can be computed in terms of the coordinates x and y, or in terms of the parameter θ,

$\delta \mathbf {r} =(\delta x,\delta y)=(L\cos \theta ,L\sin \theta )\delta \theta .$

Thus, the virtual work is given by

$\delta W=-mg\delta y=-mgL\sin(\theta )\delta \theta .$

Notice that the coefficient of δ*y* is the y-component of the applied force. In the same way, the coefficient of δ*θ* is known as the generalized force along generalized coordinate θ, given by

$F_{\theta }=-mgL\sin \theta .$

To complete the analysis consider the kinetic energy T of the mass, using the velocity,

$\mathbf {v} =({\dot {x}},{\dot {y}})=(L\cos \theta ,L\sin \theta ){\dot {\theta }},$

so,

$T={\frac {1}{2}}m\mathbf {v} \cdot \mathbf {v} ={\frac {1}{2}}m({\dot {x}}^{2}+{\dot {y}}^{2})={\frac {1}{2}}mL^{2}{\dot {\theta }}^{2}.$

D'Alembert's form of the principle of virtual work for the pendulum in terms of the coordinates x and y are given by,

${\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {x}}}}-{\frac {\partial T}{\partial x}}=F_{x}+\lambda {\frac {\partial f}{\partial x}},\quad {\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {y}}}}-{\frac {\partial T}{\partial y}}=F_{y}+\lambda {\frac {\partial f}{\partial y}}.$

This yields the three equations

$m{\ddot {x}}=\lambda (2x),\quad m{\ddot {y}}=-mg+\lambda (2y),\quad x^{2}+y^{2}-L^{2}=0,$

in the three unknowns, x, y and λ.

Using the parameter θ, those equations take the form

${\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {\theta }}}}-{\frac {\partial T}{\partial \theta }}=F_{\theta },$

which becomes,

$mL^{2}{\ddot {\theta }}=-mgL\sin \theta ,$

or

${\ddot {\theta }}+{\frac {g}{L}}\sin \theta =0.$

This formulation yields one equation because there is a single parameter and no constraint equation.

This shows that the parameter θ is a generalized coordinate that can be used in the same way as the Cartesian coordinates x and y to analyze the pendulum.

### Double pendulum

The benefits of generalized coordinates become apparent with the analysis of a double pendulum. For the two masses *mi* (*i* = 1, 2), let **r***i* = (*xi*, *yi*), *i* = 1, 2 define their two trajectories. These vectors satisfy the two constraint equations,

$f_{1}(x_{1},y_{1},x_{2},y_{2})=\mathbf {r} _{1}\cdot \mathbf {r} _{1}-L_{1}^{2}=0$

and

$f_{2}(x_{1},y_{1},x_{2},y_{2})=(\mathbf {r} _{2}-\mathbf {r} _{1})\cdot (\mathbf {r} _{2}-\mathbf {r} _{1})-L_{2}^{2}=0.$

The formulation of Lagrange's equations for this system yields six equations in the four Cartesian coordinates *xi*, *yi* (*i* = 1, 2) and the two Lagrange multipliers *λi* (*i* = 1, 2) that arise from the two constraint equations.

Now introduce the generalized coordinates *θi* (*i* = 1, 2) that define the angular position of each mass of the double pendulum from the vertical direction. In this case, we have

$\mathbf {r} _{1}=(L_{1}\sin \theta _{1},-L_{1}\cos \theta _{1}),\quad \mathbf {r} _{2}=(L_{1}\sin \theta _{1},-L_{1}\cos \theta _{1})+(L_{2}\sin \theta _{2},-L_{2}\cos \theta _{2}).$

The force of gravity acting on the masses is given by,

$\mathbf {F} _{1}=(0,-m_{1}g),\quad \mathbf {F} _{2}=(0,-m_{2}g)$

where g is the acceleration due to gravity. Therefore, the virtual work of gravity on the two masses as they follow the trajectories **r***i* (*i* = 1, 2) is given by

$\delta W=\mathbf {F} _{1}\cdot \delta \mathbf {r} _{1}+\mathbf {F} _{2}\cdot \delta \mathbf {r} _{2}.$

The variations δ**r***i* (*i* = 1, 2) can be computed to be

$\delta \mathbf {r} _{1}=(L_{1}\cos \theta _{1},L_{1}\sin \theta _{1})\delta \theta _{1},\quad \delta \mathbf {r} _{2}=(L_{1}\cos \theta _{1},L_{1}\sin \theta _{1})\delta \theta _{1}+(L_{2}\cos \theta _{2},L_{2}\sin \theta _{2})\delta \theta _{2}$

Thus, the virtual work is given by

$\delta W=-(m_{1}+m_{2})gL_{1}\sin \theta _{1}\delta \theta _{1}-m_{2}gL_{2}\sin \theta _{2}\delta \theta _{2},$

and the generalized forces are

$F_{\theta _{1}}=-(m_{1}+m_{2})gL_{1}\sin \theta _{1},\quad F_{\theta _{2}}=-m_{2}gL_{2}\sin \theta _{2}.$

Compute the kinetic energy of this system to be

$T={\frac {1}{2}}m_{1}\mathbf {v} _{1}\cdot \mathbf {v} _{1}+{\frac {1}{2}}m_{2}\mathbf {v} _{2}\cdot \mathbf {v} _{2}={\frac {1}{2}}(m_{1}+m_{2})L_{1}^{2}{\dot {\theta }}_{1}^{2}+{\frac {1}{2}}m_{2}L_{2}^{2}{\dot {\theta }}_{2}^{2}+m_{2}L_{1}L_{2}\cos(\theta _{2}-\theta _{1}){\dot {\theta }}_{1}{\dot {\theta }}_{2}.$

Euler–Lagrange equation yield two equations in the unknown generalized coordinates *θi* (*i* = 1, 2) given by

$(m_{1}+m_{2})L_{1}^{2}{\ddot {\theta }}_{1}+m_{2}L_{1}L_{2}{\ddot {\theta }}_{2}\cos(\theta _{2}-\theta _{1})+m_{2}L_{1}L_{2}{\dot {\theta _{2}}}^{2}\sin(\theta _{1}-\theta _{2})=-(m_{1}+m_{2})gL_{1}\sin \theta _{1},$

and

$m_{2}L_{2}^{2}{\ddot {\theta }}_{2}+m_{2}L_{1}L_{2}{\ddot {\theta }}_{1}\cos(\theta _{2}-\theta _{1})+m_{2}L_{1}L_{2}{\dot {\theta _{1}}}^{2}\sin(\theta _{2}-\theta _{1})=-m_{2}gL_{2}\sin \theta _{2}.$

The use of the generalized coordinates *θi* (*i* = 1, 2) provides an alternative to the Cartesian formulation of the dynamics of the double pendulum.

### Spherical pendulum

For a 3D example, a spherical pendulum with constant length l free to swing in any angular direction subject to gravity, the constraint on the pendulum bob can be stated in the form

$f(\mathbf {r} )=x^{2}+y^{2}+z^{2}-l^{2}=0\,,$

where the position of the pendulum bob can be written

$\mathbf {r} =(x(\theta ,\phi ),y(\theta ,\phi ),z(\theta ,\phi ))\,,$

in which (*θ*, *φ*) are the spherical polar angles because the bob moves in the surface of a sphere. The position **r** is measured along the suspension point to the bob, here treated as a point particle. A logical choice of generalized coordinates to describe the motion are the angles (*θ*, *φ*). Only two coordinates are needed instead of three, because the position of the bob can be parameterized by two numbers, and the constraint equation connects the three coordinates (*x*, *y*, *z*) so any one of them is determined from the other two.

## Generalized coordinates and virtual work

The *principle of virtual work* states that if a system is in static equilibrium, the virtual work of the applied forces is zero for all virtual movements of the system from this state, that is, δ*W* = 0 for any variation δ**r**. When formulated in terms of generalized coordinates, this is equivalent to the requirement that the generalized forces for any virtual displacement are zero, that is *F**i* = 0.

Let the forces on the system be **F***j* (*j* = 1, 2, …, *m*) be applied to points with Cartesian coordinates **r***j* (*j* = 1, 2, …, *m*), then the virtual work generated by a virtual displacement from the equilibrium position is given by

$\delta W=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot \delta \mathbf {r} _{j}.$

where δ**r***j* (*j* = 1, 2, …, *m*) denote the virtual displacements of each point in the body.

Now assume that each δ**r***j* depends on the generalized coordinates *qi* (*i* = 1, 2, …, *n*) then

$\delta \mathbf {r} _{j}={\frac {\partial \mathbf {r} _{j}}{\partial q_{1}}}\delta {q}_{1}+\ldots +{\frac {\partial \mathbf {r} _{j}}{\partial q_{n}}}\delta {q}_{n},$

and

$\delta W=\left(\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} _{j}}{\partial q_{1}}}\right)\delta {q}_{1}+\ldots +\left(\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} _{j}}{\partial q_{n}}}\right)\delta {q}_{n}.$

The n terms

$F_{i}=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} _{j}}{\partial q_{i}}},\quad i=1,\ldots ,n,$

are the generalized forces acting on the system. Kane shows that these generalized forces can also be formulated in terms of the ratio of time derivatives,

$F_{i}=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {v} _{j}}{\partial {\dot {q}}_{i}}},\quad i=1,\ldots ,n,$

where **v***j* is the velocity of the point of application of the force **F***j*.

In order for the virtual work to be zero for an arbitrary virtual displacement, each of the generalized forces must be zero, that is

$\delta W=0\quad \Rightarrow \quad F_{i}=0,i=1,\ldots ,n.$
