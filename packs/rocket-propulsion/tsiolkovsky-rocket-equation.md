---
title: "Tsiolkovsky rocket equation"
source: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
domain: rocket-propulsion
license: CC-BY-SA-4.0
tags: rocket propulsion, specific impulse, ion thruster, rocket engine
fetched: 2026-07-02
---

# Tsiolkovsky rocket equation

The **classical rocket equation**, **Tsiolkovsky rocket equation**, or **ideal rocket equation** is a mathematical equation that describes the motion of vehicles that follow the basic principle of a rocket: a device that can apply acceleration to itself using thrust by expelling part of its mass with high velocity and can thereby move due to the conservation of momentum. The equation is named after—and usually credited to—Konstantin Tsiolkovsky, who derived and published the formula in 1903, though William Moore had outlined it as early as 1810 and elaborated further in a book published in 1813. Robert Goddard and Hermann Oberth also obtained the same result in 1912 and 1920, respectively. All four of them reasoned and derived the same model independently.

The maximum change of velocity of the vehicle, $\Delta v$ (with no external forces acting) is:

$\Delta v=v_{\text{e}}\ln {\frac {m_{0}}{m_{f}}}=I_{\text{sp}}g_{0}\ln {\frac {m_{0}}{m_{f}}},$ where:

- $v_{\text{e}}$ is the effective exhaust velocity (which is also equal to $I_{\text{sp}}g_{0}$ )
  - $I_{\text{sp}}$ is the specific impulse in dimension of time;
  - $g_{0}$ is standard gravity;
- $\ln$ is the natural logarithm function;
- $m_{0}$ is the initial total mass, including propellant, a.k.a. wet mass;
- $m_{f}$ is the final total mass without propellant, a.k.a. dry mass.

Given the effective exhaust velocity determined by the rocket motor's design, the desired delta-v (e.g., orbital speed or escape velocity), and a given dry mass $m_{f}$ , the equation can be solved for the required wet mass $m_{0}$ : $m_{0}=m_{f}e^{\Delta v/v_{\text{e}}}.$ The required propellant mass is then $m_{0}-m_{f}=m_{f}(e^{\Delta v/v_{\text{e}}}-1)$

The necessary wet mass grows exponentially with the desired delta-v.

We can also express this as the ratio of fuel mass to payload mass: ${\frac {m_{0}-m_{f}}{m_{f}}}=e^{\Delta v/v_{e}}-1$ and we see that it grows exponentially with $\Delta v/v_{e}$

## History

The equation is named after Russian scientist Konstantin Tsiolkovsky who independently derived it and published it in his 1903 work.

The equation had been derived earlier by the British mathematician William Moore in 1810, and later published in a separate book in 1813.

American Robert Goddard independently developed the equation in 1912 when he began his research to improve rocket engines for possible space flight. German engineer Hermann Oberth independently derived the equation about 1920 as he studied the feasibility of space travel.

While the derivation of the rocket equation is a straightforward calculus exercise, Tsiolkovsky is honored as being the first to apply it to the question of whether rockets could achieve speeds necessary for space travel.

## Derivation

### Most popular derivation

Consider the following system:

In the following derivation, "the rocket" is taken to mean "the rocket and all of its unexpended propellant".

Newton's second law of motion relates external forces ( ${\vec {F}}_{i}$ ) to the change in linear momentum of the whole system (including rocket and exhaust) as follows: $\sum _{i}{\vec {F}}_{i}=\lim _{\Delta t\to 0}{\frac {{\vec {P}}_{\Delta t}-{\vec {P}}_{0}}{\Delta t}}$ where ${\vec {P}}_{0}$ is the momentum of the rocket at time $t=0$ : ${\vec {P}}_{0}=m{\vec {V}}$ and ${\vec {P}}_{\Delta t}$ is the momentum of the rocket and exhausted mass at time $t=\Delta t$ : ${\vec {P}}_{\Delta t}=\left(m-\Delta m\right)\left({\vec {V}}+\Delta {\vec {V}}\right)+\Delta m{\vec {V}}_{\text{e}}$ and where, with respect to the observer:

- ${\vec {V}}$ is the velocity of the rocket at time $t=0$
- ${\vec {V}}+\Delta {\vec {V}}$ is the velocity of the rocket at time $t=\Delta t$
- ${\vec {V}}_{\text{e}}$ is the velocity of the mass added to the exhaust (and lost by the rocket) during time $\Delta t$
- m is the mass of the rocket at time $t=0$
- $\left(m-\Delta m\right)$ is the mass of the rocket at time $t=\Delta t$

The velocity of the exhaust ${\vec {V}}_{\text{e}}$ in the observer frame is related to the velocity of the exhaust in the rocket frame $v_{\text{e}}$ by: ${\vec {v}}_{\text{e}}={\vec {V}}_{\text{e}}-{\vec {V}}$ thus, ${\vec {V}}_{\text{e}}={\vec {V}}+{\vec {v}}_{\text{e}}$ Solving this yields: ${\vec {P}}_{\Delta t}-{\vec {P}}_{0}=m\Delta {\vec {V}}+{\vec {v}}_{\text{e}}\Delta m-\Delta m\Delta {\vec {V}}$ If ${\vec {V}}$ and ${\vec {v}}_{\text{e}}$ are opposite, ${\vec {F}}_{\text{i}}$ have the same direction as ${\vec {V}}$ , $\Delta m\Delta {\vec {V}}$ are negligible (since $dm\,d{\vec {v}}\to 0$ ), and using $dm=-\Delta m$ (since ejecting a positive $\Delta m$ results in a decrease in rocket mass in time), $\sum _{i}F_{i}=m{\frac {dV}{dt}}+v_{\text{e}}{\frac {dm}{dt}}$

If there are no external forces then ${\textstyle \sum _{i}F_{i}=0}$ (conservation of linear momentum) and $-m{\frac {dV}{dt}}=v_{\text{e}}{\frac {dm}{dt}}$

Assuming that $v_{\text{e}}$ is constant (known as Tsiolkovsky's hypothesis), so it is not subject to integration, then the above equation may be integrated as follows: $-\int _{V}^{V+\Delta V}\,dV={v_{e}}\int _{m_{0}}^{m_{f}}{\frac {dm}{m}}$

This then yields $\Delta V=v_{\text{e}}\ln {\frac {m_{0}}{m_{f}}}$ or equivalently $m_{f}=m_{0}e^{-\Delta V\ /v_{\text{e}}}$ or $m_{0}=m_{f}e^{\Delta V/v_{\text{e}}}$ or $m_{0}-m_{f}=m_{f}\left(e^{\Delta V/v_{\text{e}}}-1\right)$ where $m_{0}$ is the initial total mass including propellant, $m_{f}$ the final mass, and $v_{\text{e}}$ the velocity of the rocket exhaust with respect to the rocket (the specific impulse, or, if measured in time, that multiplied by gravity-on-Earth acceleration). If $v_{\text{e}}$ is NOT constant, we might not have rocket equations that are as simple as the above forms. Many rocket dynamics researches were based on the Tsiolkovsky's constant $v_{\text{e}}$ hypothesis.

The value $m_{0}-m_{f}$ is the total working mass of propellant expended.

$\Delta V$ (delta-v) is the integration over time of the magnitude of the acceleration produced by using the rocket engine (what would be the actual acceleration if external forces were absent). In free space, for the case of acceleration in the direction of the velocity, this is the increase of the speed. In the case of an acceleration in opposite direction (deceleration) it is the decrease of the speed. Of course gravity and drag also accelerate the vehicle, and they can add or subtract to the change in velocity experienced by the vehicle. Hence delta-v may not always be the actual change in speed or velocity of the vehicle.

### Other derivations

#### Impulse-based

The equation can also be derived from the basic integral of acceleration in the form of force (thrust) over mass. By representing the delta-v equation as the following: $\Delta v=\int _{t_{0}}^{t_{f}}{\frac {|T|}{{m_{0}}-{t}\Delta {m}}}~dt$

where T is thrust, $m_{0}$ is the initial (wet) mass and $\Delta m$ is the initial mass minus the final (dry) mass,

and realising that the integral of a resultant force over time is total impulse, assuming thrust is the only force involved, $\int _{t_{0}}^{t_{f}}F~dt=J$

The integral is found to be: $J~{\frac {\ln({m_{0}})-\ln({m_{f}})}{\Delta m}}$

Realising that impulse over the change in mass is equivalent to force over propellant mass flow rate (p), which is itself equivalent to exhaust velocity, ${\frac {J}{\Delta m}}={\frac {F}{p}}=V_{\text{exh}}$ the integral can be equated to $\Delta v=V_{\text{exh}}~\ln \left({\frac {m_{0}}{m_{f}}}\right)$

#### Acceleration-based

Imagine a rocket at rest in space with no forces exerted on it (Newton's first law of motion). From the moment its engine is started (clock set to 0) the rocket expels gas mass at a *constant mass flow rate R* (kg/s) and at *exhaust velocity relative to the rocket ve* (m/s). This creates a constant force *F* propelling the rocket that is equal to *R* × *ve*. The rocket is subject to a constant force, but its total mass is decreasing steadily because it is expelling gas. According to Newton's second law of motion, its acceleration at any time *t* is its propelling force *F* divided by its current mass *m*: $~a={\frac {dv}{dt}}=-{\frac {F}{m(t)}}=-{\frac {Rv_{\text{e}}}{m(t)}}$

Now, the mass of fuel the rocket initially has on board is equal to *m*0 – *mf*. For the constant mass flow rate *R* it will therefore take a time *T* = (*m*0 – *mf*)/*R* to burn all this fuel. Integrating both sides of the equation with respect to time from *0* to *T* (and noting that *R = dm/dt* allows a substitution on the right) obtains: $~\Delta v=v_{f}-v_{0}=-v_{\text{e}}\left[\ln m_{f}-\ln m_{0}\right]=~v_{\text{e}}\ln \left({\frac {m_{0}}{m_{f}}}\right).$

#### Limit of finite mass "pellet" expulsion

The rocket equation can also be derived as the limiting case of the speed change for a rocket that expels its fuel in the form of N pellets consecutively, as $N\to \infty$ , with an effective exhaust speed $v_{\text{eff}}$ such that the mechanical energy gained per unit fuel mass is given by ${\textstyle {\tfrac {1}{2}}v_{\text{eff}}^{2}}$ .

In the rocket's center-of-mass frame, if a pellet of mass $m_{p}$ is ejected at speed u and the remaining mass of the rocket is m , the amount of energy converted to increase the rocket's and pellet's kinetic energy is ${\tfrac {1}{2}}m_{p}v_{\text{eff}}^{2}={\tfrac {1}{2}}m_{p}u^{2}+{\tfrac {1}{2}}m(\Delta v)^{2}.$

Using momentum conservation in the rocket's frame just prior to ejection, ${\textstyle u=\Delta v{\tfrac {m}{m_{p}}}}$ , from which we find $\Delta v=v_{\text{eff}}{\frac {m_{p}}{\sqrt {m(m+m_{p})}}}.$

Let $\phi$ be the initial fuel mass fraction on board and $m_{0}$ the initial fueled-up mass of the rocket. Divide the total mass of fuel $\phi m_{0}$ into N discrete pellets each of mass $m_{p}=\phi m_{0}/N$ . The remaining mass of the rocket after ejecting j pellets is then $m=m_{0}(1-j\phi /N)$ . The overall speed change after ejecting j pellets is the sum $\Delta v=v_{\text{eff}}\sum _{j=1}^{j=N}{\frac {\phi /N}{\sqrt {(1-j\phi /N)(1-j\phi /N+\phi /N)}}}$

Notice that for large N the last term in the denominator $\phi /N\ll 1$ and can be neglected to give $\Delta v\approx v_{\text{eff}}\sum _{j=1}^{j=N}{\frac {\phi /N}{1-j\phi /N}}=v_{\text{eff}}\sum _{j=1}^{j=N}{\frac {\Delta x}{1-x_{j}}}$ where ${\textstyle \Delta x={\frac {\phi }{N}}}$ and ${\textstyle x_{j}={\frac {j\phi }{N}}}$ .

As $N\rightarrow \infty$ this Riemann sum becomes the definite integral $\lim _{N\to \infty }\Delta v=v_{\text{eff}}\int _{0}^{\phi }{\frac {dx}{1-x}}=v_{\text{eff}}\ln {\frac {1}{1-\phi }}=v_{\text{eff}}\ln {\frac {m_{0}}{m_{f}}},$ since the final remaining mass of the rocket is $m_{f}=m_{0}(1-\phi )$ .

### Special relativity

If special relativity is taken into account, the following equation can be derived for a relativistic rocket, with $\Delta v$ again standing for the rocket's final velocity (after expelling all its reaction mass and being reduced to a rest mass of $m_{1}$ ) in the inertial frame of reference where the rocket started at rest (with the rest mass including fuel being $m_{0}$ initially), and c standing for the speed of light in vacuum: ${\frac {m_{0}}{m_{1}}}=\left[{\frac {1+{\frac {\Delta v}{c}}}{1-{\frac {\Delta v}{c}}}}\right]^{\frac {c}{2v_{\text{e}}}}$

Writing ${\textstyle {\frac {m_{0}}{m_{1}}}}$ as R allows this equation to be rearranged as ${\frac {\Delta v}{c}}={\frac {R^{\frac {2v_{\text{e}}}{c}}-1}{R^{\frac {2v_{\text{e}}}{c}}+1}}$

Then, using the identity ${\textstyle R^{\frac {2v_{\text{e}}}{c}}=\exp \left[{\frac {2v_{\text{e}}}{c}}\ln R\right]}$ (here "exp" denotes the exponential function; *see also* Natural logarithm as well as the "power" identity at logarithmic identities) and the identity ${\textstyle \tanh x={\frac {e^{2x}-1}{e^{2x}+1}}}$ (*see* Hyperbolic function), this is equivalent to $\Delta v=c\tanh \left({\frac {v_{\text{e}}}{c}}\ln {\frac {m_{0}}{m_{1}}}\right)$

## Terms of the equation

### Delta-*v*

Delta-*v* (literally "change in velocity"), symbolised as **Δ*v*** and pronounced *delta-vee*, as used in spacecraft flight dynamics, is a measure of the impulse that is needed to perform a maneuver such as launching from, or landing on a planet or moon, or an in-space orbital maneuver. It is a scalar that has the units of speed. As used in this context, it is *not* the same as the physical change in velocity of the vehicle.

Delta-*v* is produced by reaction engines, such as rocket engines, is proportional to the thrust per unit mass and burn time, and is used to determine the mass of propellant required for the given manoeuvre through the rocket equation.

For multiple manoeuvres, delta-*v* sums linearly.

For interplanetary missions delta-*v* is often plotted on a porkchop plot which displays the required mission delta-*v* as a function of launch date.

### Mass fraction

In aerospace engineering, the propellant mass fraction is the portion of a vehicle's mass which does not reach the destination and is instead burned as propellant, usually used as a measure of the vehicle's performance. In other words, the propellant mass fraction is the ratio between the propellant mass and the initial mass of the vehicle. In a spacecraft, the destination is usually an orbit, while for aircraft it is their landing location. A higher mass fraction represents less weight in a design. Another related measure is the payload fraction, which is the fraction of initial weight that is payload.

While the original wording of the Tsiolkovsky rocket equation does not directly use the mass fraction, the mass fraction can be derived from the used ratio of initial to final mass, or ${\frac {m_{0}}{m_{f}}}={\frac {m_{f}+m_{p}}{m_{f}}}={\frac {m_{p}}{m_{f}}}+1$ .

### Effective exhaust velocity

The effective exhaust velocity is often specified as a specific impulse and they are related to each other by: $v_{\text{e}}=g_{0}I_{\text{sp}},$ where

- $I_{\text{sp}}$ is the specific impulse in seconds,
- $v_{\text{e}}$ is the specific impulse measured in m/s, which is the same as the effective exhaust velocity measured in m/s (or ft/s if g is in ft/s2),
- $g_{0}$ is the standard gravity, 9.80665 m/s2 (in Imperial units 32.174 ft/s2).

## Applicability

The rocket equation captures the essentials of rocket flight physics in a single short equation. It also holds true for rocket-like reaction vehicles whenever the effective exhaust velocity is constant, and can be summed or integrated when the effective exhaust velocity varies. The rocket equation only accounts for the reaction force from the rocket engine; it does not include other forces that may act on a rocket, such as aerodynamic or gravitational forces. As such, when using it to calculate the propellant requirement for launch from (or powered descent to) a planet with an atmosphere, the effects of these forces must be included in the delta-V requirement (see Examples below). In what has been called "the tyranny of the rocket equation", there is a limit to the amount of payload that the rocket can carry, as higher amounts of propellant increment the overall weight, and thus also increase the fuel consumption. The equation does not apply to non-rocket systems such as aerobraking, gun launches, space elevators, launch loops, tether propulsion or light sails.

The rocket equation can be applied to orbital maneuvers in order to determine how much propellant is needed to change to a particular new orbit, or to find the new orbit as the result of a particular propellant burn. When applying to orbital maneuvers, one assumes an impulsive maneuver, in which the propellant is discharged and delta-v applied instantaneously. This assumption is relatively accurate for short-duration burns such as for mid-course corrections and orbital insertion maneuvers. As the burn duration increases, the result is less accurate due to the effect of gravity on the vehicle over the duration of the maneuver. For low-thrust, long duration propulsion, such as electric propulsion, more complicated analysis based on the propagation of the spacecraft's state vector and the integration of thrust are used to predict orbital motion.

## Examples

Assume an exhaust velocity of 4,500 meters per second (15,000 ft/s) and a $\Delta v$ of 9,700 meters per second (32,000 ft/s) (Earth to LEO, including $\Delta v$ to overcome gravity and aerodynamic drag).

- Single-stage-to-orbit rocket: $1-e^{-9.7/4.5}$ = 0.884, therefore 88.4% of the initial total mass has to be propellant. The remaining 11.6% is for the engines, the tank, and the payload.
- Two-stage-to-orbit: suppose that the first stage should provide a $\Delta v$ of 5,000 meters per second (16,000 ft/s); $1-e^{-5.0/4.5}$ = 0.671, therefore 67.1% of the initial total mass has to be propellant to the first stage. The remaining mass is 32.9%. After disposing of the first stage, a mass remains equal to this 32.9%, minus the mass of the tank and engines of the first stage. Assume that this is 8% of the initial total mass, then 24.9% remains. The second stage should provide a $\Delta v$ of 4,700 meters per second (15,000 ft/s); $1-e^{-4.7/4.5}$ = 0.648, therefore 64.8% of the remaining mass has to be propellant, which is 16.2% of the original total mass, and 8.7% remains for the tank and engines of the second stage, the payload, and in the case of a space shuttle, also the orbiter. Thus together 16.7% of the original launch mass is available for *all* engines, the tanks, and payload.

## Stages

In the case of sequentially thrusting rocket stages, the equation applies for each stage, where for each stage the initial mass in the equation is the total mass of the rocket after discarding the previous stage, and the final mass in the equation is the total mass of the rocket just before discarding the stage concerned. For each stage the specific impulse may be different.

For example, if 80% of the mass of a rocket is the fuel of the first stage, and 10% is the dry mass of the first stage, and 10% is the remaining rocket, then

${\begin{aligned}\Delta v\ &=v_{\text{e}}\ln {100 \over 100-80}\\&=v_{\text{e}}\ln 5\\&=1.61v_{\text{e}}.\\\end{aligned}}$

With three similar, subsequently smaller stages with the same $v_{\text{e}}$ for each stage, gives:

$\Delta v\ =3v_{\text{e}}\ln 5\ =4.83v_{\text{e}}$

and the payload is 10% × 10% × 10% = 0.1% of the initial mass.

A comparable SSTO rocket, also with a 0.1% payload, could have a mass of 11.1% for fuel tanks and engines, and 88.8% for fuel. This would give

$\Delta v\ =v_{\text{e}}\ln(100/11.2)\ =2.19v_{\text{e}}.$

If the motor of a new stage is ignited before the previous stage has been discarded and the simultaneously working motors have a different specific impulse (as is often the case with solid rocket boosters and a liquid-fuel stage), the situation is more complicated.
