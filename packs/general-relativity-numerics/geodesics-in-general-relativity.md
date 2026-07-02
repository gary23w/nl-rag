---
title: "Geodesics in general relativity"
source: https://en.wikipedia.org/wiki/Geodesics_in_general_relativity
domain: general-relativity-numerics
license: CC-BY-SA-4.0
tags: numerical relativity, einstein field equations, adm formalism, gravitational wave modeling
fetched: 2026-07-02
---

# Geodesics in general relativity

In general relativity, a **geodesic** generalizes the notion of a "straight line" to curved spacetime. Importantly, the world line of a particle free from all external, non-gravitational forces is a particular type of geodesic. In other words, a freely moving or falling particle always moves along a geodesic.

In general relativity, gravity can be regarded as not a force but a consequence of a curved spacetime geometry where the source of curvature is the stress–energy tensor (representing matter, for instance). Thus, for example, the path of a planet orbiting a star is the projection of a geodesic of the curved four-dimensional (4-D) spacetime geometry around the star onto three-dimensional (3-D) space.

## Mathematical expression

The full **geodesic equation** is ${d^{2}x^{\mu } \over ds^{2}}+\Gamma ^{\mu }{}_{\alpha \beta }{dx^{\alpha } \over ds}{dx^{\beta } \over ds}=0\$ where *s* is a scalar parameter of motion (e.g. the proper time), and $\Gamma ^{\mu }{}_{\alpha \beta }$ are Christoffel symbols (sometimes called the affine connection coefficients or Levi-Civita connection coefficients) symmetric in the two lower indices. Greek indices may take the values: 0, 1, 2, 3 and the summation convention is used for repeated indices $\alpha$ and $\beta$ . The quantity on the left-hand-side of the sum in this equation is the acceleration of a particle, so this equation is analogous to Newton's laws of motion, which likewise provide formulae for the acceleration of a particle. The Christoffel symbols are functions of the four spacetime coordinates and so are independent of the velocity or acceleration or other characteristics of a test particle whose motion is described by the geodesic equation.

## Equivalent mathematical expression using coordinate time as parameter

So far the geodesic equation of motion has been written in terms of a scalar parameter *s*. It can alternatively be written in terms of the time coordinate, $t\equiv x^{0}$ (here we have used the triple bar to signify a definition). The geodesic equation of motion then becomes: ${d^{2}x^{\mu } \over dt^{2}}=-\Gamma ^{\mu }{}_{\alpha \beta }{dx^{\alpha } \over dt}{dx^{\beta } \over dt}+\Gamma ^{0}{}_{\alpha \beta }{dx^{\alpha } \over dt}{dx^{\beta } \over dt}{dx^{\mu } \over dt}\ .$

This formulation of the geodesic equation of motion can be useful for computer calculations and to compare General Relativity with Newtonian Gravity. It is straightforward to derive this form of the geodesic equation of motion from the form which uses proper time as a parameter using the chain rule. Notice that both sides of this last equation vanish when the mu index is set to zero. If the particle's velocity is small enough, then the geodesic equation reduces to this: ${d^{2}x^{n} \over dt^{2}}=-\Gamma ^{n}{}_{00}.$

Here the Latin index *n* takes the values [1,2,3]. This equation simply means that all test particles at a particular place and time will have the same acceleration, which is a well-known feature of Newtonian gravity. For example, everything floating around in the International Space Station will undergo roughly the same acceleration due to gravity.

## Derivation directly from the equivalence principle

Physicist Steven Weinberg has presented a derivation of the geodesic equation of motion directly from the equivalence principle. The first step in such a derivation is to suppose that a free falling particle does not accelerate in the neighborhood of a point-event with respect to a freely falling coordinate system ( $X^{\mu }$ ). Setting $T\equiv X^{0}$ , we have the following equation that is locally applicable in free fall: ${d^{2}X^{\mu } \over dT^{2}}=0.$ The next step is to employ the multi-dimensional chain rule. We have: ${dX^{\mu } \over dT}={dx^{\nu } \over dT}{\partial X^{\mu } \over \partial x^{\nu }}$ Differentiating once more with respect to the time, we have: ${d^{2}X^{\mu } \over dT^{2}}={d^{2}x^{\nu } \over dT^{2}}{\partial X^{\mu } \over \partial x^{\nu }}+{dx^{\nu } \over dT}{dx^{\alpha } \over dT}{\partial ^{2}X^{\mu } \over \partial x^{\nu }\partial x^{\alpha }}$ We have already said that the left-hand-side of this last equation must vanish because of the Equivalence Principle. Therefore: ${d^{2}x^{\nu } \over dT^{2}}{\partial X^{\mu } \over \partial x^{\nu }}=-{dx^{\nu } \over dT}{dx^{\alpha } \over dT}{\partial ^{2}X^{\mu } \over \partial x^{\nu }\partial x^{\alpha }}$ Multiply both sides of this last equation by the following quantity: ${\partial x^{\lambda } \over \partial X^{\mu }}$ Consequently, we have this: ${d^{2}x^{\lambda } \over dT^{2}}=-{dx^{\nu } \over dT}{dx^{\alpha } \over dT}\left[{\partial ^{2}X^{\mu } \over \partial x^{\nu }\partial x^{\alpha }}{\partial x^{\lambda } \over \partial X^{\mu }}\right].$

Weinberg defines the affine connection as follows: $\Gamma ^{\lambda }{}_{\nu \alpha }=\left[{\partial ^{2}X^{\mu } \over \partial x^{\nu }\partial x^{\alpha }}{\partial x^{\lambda } \over \partial X^{\mu }}\right]$ which leads to this formula: ${d^{2}x^{\lambda } \over dT^{2}}=-\Gamma _{\nu \alpha }^{\lambda }{dx^{\nu } \over dT}{dx^{\alpha } \over dT}.$

This completes our derivation, since the proper time is defined as the local time at a point that follows the line of motion in question (in this case the geodesic line of a free falling particle). Let us continue in order to derive the equations using the coordinate time as parameter. By applying the one-dimensional chain rule: ${d^{2}x^{\lambda } \over dt^{2}}\left({\frac {dt}{dT}}\right)^{2}+{dx^{\lambda } \over dt}{\frac {d^{2}t}{dT^{2}}}=-\Gamma _{\nu \alpha }^{\lambda }{dx^{\nu } \over dt}{dx^{\alpha } \over dt}\left({\frac {dt}{dT}}\right)^{2}.$ ${d^{2}x^{\lambda } \over dt^{2}}+{dx^{\lambda } \over dt}{\frac {d^{2}t}{dT^{2}}}\left({\frac {dT}{dt}}\right)^{2}=-\Gamma _{\nu \alpha }^{\lambda }{dx^{\nu } \over dt}{dx^{\alpha } \over dt}.$

As before, we can set $t\equiv x^{0}$ . Then the first derivative of *x*0 with respect to *t* is one and the second derivative is zero. Replacing *λ* with zero gives: ${\frac {d^{2}t}{dT^{2}}}\left({\frac {dT}{dt}}\right)^{2}=-\Gamma _{\nu \alpha }^{0}{dx^{\nu } \over dt}{dx^{\alpha } \over dt}.$

Subtracting d *x**λ* / d *t* times this from the previous equation gives: ${d^{2}x^{\lambda } \over dt^{2}}=-\Gamma _{\nu \alpha }^{\lambda }{dx^{\nu } \over dt}{dx^{\alpha } \over dt}+\Gamma _{\nu \alpha }^{0}{dx^{\nu } \over dt}{dx^{\alpha } \over dt}{dx^{\lambda } \over dt}$ which is the form of the geodesic equation of motion using the coordinate time as parameter.

The geodesic equation of motion can alternatively be derived using the concept of parallel transport.

## Deriving the geodesic equation via an action

We can (and this is the most common technique) derive the geodesic equation via the action principle. Consider the case of trying to find a geodesic between two timelike-separated events.

Let the action be $S=\int ds$ where $ds={\sqrt {-g_{\mu \nu }(x)\,dx^{\mu }\,dx^{\nu }}}$ is the line element. There is a negative sign inside the square root because the curve must be timelike. To get the geodesic equation we must vary this action. To do this let us parameterize this action with respect to a parameter $\lambda$ . Doing this we get: $S=\int {\sqrt {-g_{\mu \nu }{\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\lambda }}}}\,d\lambda$

We can now go ahead and vary this action with respect to the curve $x^{\mu }$ . By the principle of least action we get: $0=\delta S=\int \delta \left({\sqrt {-g_{\mu \nu }{\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\lambda }}}}\right)\,d\lambda =\int {\frac {\delta \left(-g_{\mu \nu }{\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\lambda }}\right)}{2{\sqrt {-g_{\mu \nu }{\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\lambda }}}}}}d\lambda$

Using the product rule we get: $0=\int \left({\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\tau }}\delta g_{\mu \nu }+g_{\mu \nu }{\frac {d\delta x^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\tau }}+g_{\mu \nu }{\frac {dx^{\mu }}{d\tau }}{\frac {d\delta x^{\nu }}{d\lambda }}\right)\,d\lambda =\int \left({\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\tau }}\partial _{\alpha }g_{\mu \nu }\delta x^{\alpha }+2g_{\mu \nu }{\frac {d\delta x^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\tau }}\right)\,d\lambda$ where ${\frac {d\tau }{d\lambda }}={\sqrt {-g_{\mu \nu }{\frac {dx^{\mu }}{d\lambda }}{\frac {dx^{\nu }}{d\lambda }}}}$

Integrating by-parts the last term and dropping the total derivative (which equals to zero at the boundaries) we get that: $0=\int \left({\frac {dx^{\mu }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\alpha }g_{\mu \nu }\delta x^{\alpha }-2\delta x^{\mu }{\frac {d}{d\tau }}\left(g_{\mu \nu }{\frac {dx^{\nu }}{d\tau }}\right)\right)\,d\tau =\int \left({\frac {dx^{\mu }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\alpha }g_{\mu \nu }\delta x^{\alpha }-2\delta x^{\mu }\partial _{\alpha }g_{\mu \nu }{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}-2\delta x^{\mu }g_{\mu \nu }{\frac {d^{2}x^{\nu }}{d\tau ^{2}}}\right)\,d\tau$

Simplifying a bit we see that: $0=\int \left(-2g_{\mu \nu }{\frac {d^{2}x^{\nu }}{d\tau ^{2}}}+{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\mu }g_{\alpha \nu }-2{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\alpha }g_{\mu \nu }\right)\delta x^{\mu }d\tau$ so, $0=\int \left(-2g_{\mu \nu }{\frac {d^{2}x^{\nu }}{d\tau ^{2}}}+{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\mu }g_{\alpha \nu }-{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\partial _{\alpha }g_{\mu \nu }-{\frac {dx^{\nu }}{d\tau }}{\frac {dx^{\alpha }}{d\tau }}\partial _{\nu }g_{\mu \alpha }\right)\delta x^{\mu }\,d\tau$ multiplying this equation by ${\textstyle -{\frac {1}{2}}}$ we get: $0=\int \left(g_{\mu \nu }{\frac {d^{2}x^{\nu }}{d\tau ^{2}}}+{\frac {1}{2}}{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\left(\partial _{\alpha }g_{\mu \nu }+\partial _{\nu }g_{\mu \alpha }-\partial _{\mu }g_{\alpha \nu }\right)\right)\delta x^{\mu }\,d\tau$

So by Hamilton's principle we find that the Euler–Lagrange equation is $g_{\mu \nu }{\frac {d^{2}x^{\nu }}{d\tau ^{2}}}+{\frac {1}{2}}{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}\left(\partial _{\alpha }g_{\mu \nu }+\partial _{\nu }g_{\mu \alpha }-\partial _{\mu }g_{\alpha \nu }\right)=0$

Multiplying by the inverse metric tensor $g^{\mu \beta }$ we get that ${\frac {d^{2}x^{\beta }}{d\tau ^{2}}}+{\frac {1}{2}}g^{\mu \beta }\left(\partial _{\alpha }g_{\mu \nu }+\partial _{\nu }g_{\mu \alpha }-\partial _{\mu }g_{\alpha \nu }\right){\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}=0$

Thus we get the geodesic equation: ${\frac {d^{2}x^{\beta }}{d\tau ^{2}}}+\Gamma ^{\beta }{}_{\alpha \nu }{\frac {dx^{\alpha }}{d\tau }}{\frac {dx^{\nu }}{d\tau }}=0$ with the Christoffel symbol defined in terms of the metric tensor as $\Gamma ^{\beta }{}_{\alpha \nu }={\frac {1}{2}}g^{\mu \beta }\left(\partial _{\alpha }g_{\mu \nu }+\partial _{\nu }g_{\mu \alpha }-\partial _{\mu }g_{\alpha \nu }\right)$

(Note: Similar derivations, with minor amendments, can be used to produce analogous results for geodesics between light-like or space-like separated pairs of points.)

## Equation of motion may follow from the field equations for empty space

Albert Einstein believed that the geodesic equation of motion can be derived from the field equations for empty space, i.e. from the fact that the Ricci curvature vanishes. He wrote:

> It has been shown that this law of motion — generalized to the case of arbitrarily large gravitating masses — can be derived from the field equations of empty space alone. According to this derivation the law of motion is implied by the condition that the field be singular nowhere outside its generating mass points.

and

> One of the imperfections of the original relativistic theory of gravitation was that as a field theory it was not complete; it introduced the independent postulate that the law of motion of a particle is given by the equation of the geodesic.
> 
> A complete field theory knows only fields and not the concepts of particle and motion. For these must not exist independently from the field but are to be treated as part of it.
> 
> On the basis of the description of a particle without singularity, one has the possibility of a logically more satisfactory treatment of the combined problem: The problem of the field and that of the motion coincide.

Both physicists and philosophers have often repeated the assertion that the geodesic equation can be obtained from the field equations to describe the motion of a gravitational singularity, but this claim remains disputed. According to David Malament, “Though the geodesic principle can be recovered as theorem in general relativity, it is not a consequence of Einstein’s equation (or the conservation principle) alone. Other assumptions are needed to derive the theorems in question.” Less controversial is the notion that the field equations determine the motion of a fluid or dust, as distinguished from the motion of a point-singularity.

## Extension to the case of a charged particle

In deriving the geodesic equation from the equivalence principle, it was assumed that particles in a local inertial coordinate system are not accelerating. However, in real life, the particles may be charged, and therefore may be accelerating locally in accordance with the Lorentz force. That is: ${d^{2}X^{\mu } \over ds^{2}}={q \over m}{F^{\mu \beta }}{dX^{\alpha } \over ds}{\eta _{\alpha \beta }}.$ with ${\eta _{\alpha \beta }}{dX^{\alpha } \over ds}{dX^{\beta } \over ds}=-1.$

The Minkowski tensor $\eta _{\alpha \beta }$ is given by: $\eta _{\alpha \beta }={\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}}$

These last three equations can be used as the starting point for the derivation of an equation of motion in General Relativity, instead of assuming that acceleration is zero in free fall. Because the Minkowski tensor is involved here, it becomes necessary to introduce something called the *metric tensor* in General Relativity. The metric tensor *g* is symmetric, and locally reduces to the Minkowski tensor in free fall. The resulting equation of motion is as follows: ${d^{2}x^{\mu } \over ds^{2}}=-\Gamma ^{\mu }{}_{\alpha \beta }{dx^{\alpha } \over ds}{dx^{\beta } \over ds}\ +{q \over m}{F^{\mu \beta }}{dx^{\alpha } \over ds}{g_{\alpha \beta }}.$ with ${g_{\alpha \beta }}{dx^{\alpha } \over ds}{dx^{\beta } \over ds}=-1.$

This last equation signifies that the particle is moving along a timelike geodesic; massless particles like the photon instead follow null geodesics (replace −1 with zero on the right-hand side of the last equation). It is important that the last two equations are consistent with each other, when the latter is differentiated with respect to proper time, and the following formula for the Christoffel symbols ensures that consistency: $\Gamma ^{\lambda }{}_{\alpha \beta }={\frac {1}{2}}g^{\lambda \tau }\left({\frac {\partial g_{\tau \alpha }}{\partial x^{\beta }}}+{\frac {\partial g_{\tau \beta }}{\partial x^{\alpha }}}-{\frac {\partial g_{\alpha \beta }}{\partial x^{\tau }}}\right)$ This last equation does not involve the electromagnetic fields, and it is applicable even in the limit as the electromagnetic fields vanish. The letter *g* with superscripts refers to the inverse of the metric tensor. In General Relativity, indices of tensors are lowered and raised by contraction with the metric tensor or its inverse, respectively.

## Geodesics as curves of stationary interval

A geodesic between two events can also be described as the curve joining those two events which has a stationary interval (4-dimensional "length"). *Stationary* here is used in the sense in which that term is used in the calculus of variations, namely, that the interval along the curve varies minimally among curves that are nearby to the geodesic.

In simply connected Minkowski space there is only one geodesic that connects any given pair of events, and for a time-like geodesic, this is the curve with the longest proper time between the two events. In curved spacetime, it is possible for a pair of widely separated events to have more than one time-like geodesic between them. In such instances, the proper times along several geodesics will not in general be the same. For some geodesics in such instances, it is possible for a curve that connects the two events and is nearby to the geodesic to have either a longer or a shorter proper time than the geodesic.

For a space-like geodesic through two events, there are always nearby curves which go through the two events that have either a longer or a shorter proper length than the geodesic, even in Minkowski space. In Minkowski space, the geodesic will be a straight line. Any curve that differs from the geodesic purely spatially (*i.e.* does not change the time coordinate) in any inertial frame of reference will have a longer proper length than the geodesic, but a curve that differs from the geodesic purely temporally (*i.e.* does not change the space coordinates) in such a frame of reference will have a shorter proper length.

The interval of a curve in spacetime is $l=\int {\sqrt {\left|g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }\right|}}\,ds\ .$

Then, the Euler–Lagrange equation, ${d \over ds}{\partial \over \partial {\dot {x}}^{\alpha }}{\sqrt {\left|g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }\right|}}={\partial \over \partial x^{\alpha }}{\sqrt {\left|g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }\right|}}\ ,$ becomes, after some calculation, $2\left(\Gamma ^{\lambda }{}_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+{\ddot {x}}^{\lambda }\right)=U^{\lambda }{d \over ds}\ln |U_{\nu }U^{\nu }|\ ,$ where $U^{\mu }={\dot {x}}^{\mu }.$

Proof

The goal being to find a curve for which the value of $l=\int d\tau =\int {d\tau \over d\phi }\,d\phi =\int {\sqrt {(d\tau )^{2} \over (d\phi )^{2}}}\,d\phi =\int {\sqrt {-g_{\mu \nu }dx^{\mu }dx^{\nu } \over d\phi \,d\phi }}\,d\phi =\int f\,d\phi$ is stationary, where $f={\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}$ such goal can be accomplished by calculating the Euler–Lagrange equation for *f*, which is ${d \over d\tau }{\partial f \over \partial {\dot {x}}^{\lambda }}={\partial f \over \partial x^{\lambda }}.$

Substituting the expression of *f* into the Euler–Lagrange equation (which makes the value of the integral *l* stationary), gives ${d \over d\tau }{\partial {\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}} \over \partial {\dot {x}}^{\lambda }}={\partial {\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}} \over \partial x^{\lambda }}$

Now calculate the derivatives: ${\begin{aligned}{d \over d\tau }\left({-g_{\mu \nu }{\partial {\dot {x}}^{\mu } \over \partial {\dot {x}}^{\lambda }}{\dot {x}}^{\nu }-g_{\mu \nu }{\dot {x}}^{\mu }{\partial {\dot {x}}^{\nu } \over \partial {\dot {x}}^{\lambda }} \over 2{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}\right)&={-g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu } \over 2{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}&&(1)\\[1ex]{d \over d\tau }\left({g_{\mu \nu }\delta ^{\mu }{}_{\lambda }{\dot {x}}^{\nu }+g_{\mu \nu }{\dot {x}}^{\mu }\delta ^{\nu }{}_{\lambda } \over 2{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}\right)&={g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu } \over 2{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}&&(2)\\[1ex]{d \over d\tau }\left({g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\mu \lambda }{\dot {x}}^{\mu } \over {\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}\right)&={g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu } \over {\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}&&(3)\\[1ex]{{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}{d \over d\tau }(g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\mu \lambda }{\dot {x}}^{\mu })-(g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\mu \lambda }{\dot {x}}^{\mu }){d \over d\tau }{\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}} \over -g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}&={g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu } \over {\sqrt {-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}}}&&(4)\\[1ex]{(-g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }){d \over d\tau }(g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\mu \lambda }{\dot {x}}^{\mu })+{1 \over 2}(g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\mu \lambda }{\dot {x}}^{\mu }){d \over d\tau }(g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }) \over -g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }}&=g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu }&&(5)\end{aligned}}$ ${\begin{aligned}&(g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu })(g_{\lambda \nu ,\mu }{\dot {x}}^{\nu }{\dot {x}}^{\mu }+g_{\mu \lambda ,\nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+g_{\lambda \nu }{\ddot {x}}^{\nu }+g_{\lambda \mu }{\ddot {x}}^{\mu })\\&=(g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu })(g_{\alpha \beta }{\dot {x}}^{\alpha }{\dot {x}}^{\beta })+{1 \over 2}(g_{\lambda \nu }{\dot {x}}^{\nu }+g_{\lambda \mu }{\dot {x}}^{\mu }){d \over d\tau }(g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu })\qquad \qquad (6)\end{aligned}}$ $g_{\lambda \nu ,\mu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+g_{\lambda \mu ,\nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }-g_{\mu \nu ,\lambda }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+2g_{\lambda \mu }{\ddot {x}}^{\mu }={{\dot {x}}_{\lambda }{d \over d\tau }(g_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }) \over g_{\alpha \beta }{\dot {x}}^{\alpha }{\dot {x}}^{\beta }}\qquad \qquad (7)$ $2(\Gamma _{\lambda \mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+{\ddot {x}}_{\lambda })={{\dot {x}}_{\lambda }{d \over d\tau }({\dot {x}}_{\nu }{\dot {x}}^{\nu }) \over {\dot {x}}_{\beta }{\dot {x}}^{\beta }}={U_{\lambda }{d \over d\tau }(U_{\nu }U^{\nu }) \over U_{\beta }U^{\beta }}=U_{\lambda }{d \over d\tau }\ln |U_{\nu }U^{\nu }|\qquad \qquad (8)$

This is just one step away from the geodesic equation.

If the parameter *s* is chosen to be affine, then the right side of the above equation vanishes (because $U_{\nu }U^{\nu }$ is constant). Finally, we have the geodesic equation $\Gamma ^{\lambda }{}_{\mu \nu }{\dot {x}}^{\mu }{\dot {x}}^{\nu }+{\ddot {x}}^{\lambda }=0\ .$

## Derivation using autoparallel transport

The geodesic equation can be alternatively derived from the autoparallel transport of curves. The derivation is based on the lectures given by Frederic P. Schuller at the We-Heraeus International Winter School on Gravity & Light.

Let $(M,O,A,\nabla )$ be a smooth manifold with connection and $\gamma$ be a curve on the manifold. The curve is said to be autoparallely transported if and only if $\nabla _{v_{\gamma }}v_{\gamma }=0$ .

In order to derive the geodesic equation, we have to choose a chart $(U,x)\in A$ : $\nabla _{{\dot {\gamma }}^{i}{\frac {\partial }{\partial x^{i}}}}\left({\dot {\gamma }}^{m}{\frac {\partial }{\partial x^{m}}}\right)=0$ Using the $C^{\infty }$ linearity and the Leibniz rule: ${\dot {\gamma }}^{i}\left(\nabla _{\frac {\partial }{\partial x^{i}}}{\dot {\gamma }}^{m}\right){\frac {\partial }{\partial x^{m}}}+{\dot {\gamma }}^{i}{\dot {\gamma }}^{m}\nabla _{\frac {\partial }{\partial x^{i}}}\left({\frac {\partial }{\partial x^{m}}}\right)=0$

Using how the connection acts on functions ( ${\dot {\gamma }}^{m}$ ) and expanding the second term with the help of the connection coefficient functions: ${\dot {\gamma }}^{i}{\frac {\partial {\dot {\gamma }}^{m}}{\partial x^{i}}}{\frac {\partial }{\partial x^{m}}}+{\dot {\gamma }}^{i}{\dot {\gamma }}^{m}\Gamma _{im}^{q}{\frac {\partial }{\partial x^{q}}}=0$

The first term can be simplified to ${\ddot {\gamma }}^{m}{\frac {\partial }{\partial x^{m}}}$ . Renaming the dummy indices: ${\ddot {\gamma }}^{q}{\frac {\partial }{\partial x^{q}}}+{\dot {\gamma }}^{i}{\dot {\gamma }}^{m}\Gamma _{im}^{q}{\frac {\partial }{\partial x^{q}}}=0$

We finally arrive to the geodesic equation: ${\ddot {\gamma }}^{q}+{\dot {\gamma }}^{i}{\dot {\gamma }}^{m}\Gamma _{im}^{q}=0$
