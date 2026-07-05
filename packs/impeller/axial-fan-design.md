---
title: "Axial fan design"
source: https://en.wikipedia.org/wiki/Axial_fan_design
domain: impeller
license: CC-BY-SA-4.0
tags: impeller
fetched: 2026-07-05
---

# Axial fan design

An **axial fan** is a type of fan that causes gas to flow through it in an axial direction, parallel to the shaft about which the blades rotate. The flow is axial at entry and exit. The fan is designed to produce a pressure difference, and hence force, to cause a flow through the fan. Factors which determine the performance of the fan include the number and shape of the blades. Fans have many applications including in wind tunnels and cooling towers. Design parameters include power, flow rate, pressure rise and efficiency.

Axial fans generally comprise fewer blades (two to six) than centrifugal fans. Axial fans commonly have larger radius and lower speed (ω) than ducted fans (esp. at similar power. Stress proportional to r^2).

## Calculation of parameters

Since the calculation cannot be done using the inlet and outlet velocity triangles, which is not the case in other turbomachines, calculation is done by considering a mean velocity triangle for flow only through an infinitesimal blade element. The blade is divided into many small elements and various parameters are determined separately for each element. There are two theories that solve the parameters for axial fans:

- Slipstream Theory
- Blade Element Theory

### Slipstream theory

In the figure, the thickness of the propeller disc is assumed to be negligible. The boundary between the fluid in motion and fluid at rest is shown. Therefore, the flow is assumed to be taking place in an imaginary converging duct where:

- *D* = Diameter of the Propeller Disc.
- *Ds* = Diameter at the Exit.

| Parameter | Pressure | Density | Velocity | Stagnation enthalpy | Static Enthalpy |
|---|---|---|---|---|---|
| −∞ | Pa | ρa | Cu (upstream velocity) | hou | hu |
| +∞ | Pa | ρa | Cs (slipstream velocity) | hod | hd |
| Relationship | Equal | Equal | Unequal | Unequal | Equal |
| Comments | Pressure will be atmospheric at both −∞ and +∞ | Density will be equal at both −∞ and +∞ | Velocity will change due to flow across an assumed converging duct | Stagnation enthalpy will be different at −∞ and +∞ | The static Enthalpy will be same at −∞ and +∞ as it depends upon the atmospheric conditions that will be the same |

In the figure, across the propeller disc, velocities (C1 and C2) cannot change abruptly across the propeller disc as that will create a shockwave but the fan creates the pressure difference across the propeller disc.

$C_{\rm {1}}=C_{\rm {2}}=C$

and

$P_{\rm {1}}\neq P_{\rm {2}}$

- The area of the propeller disc of diameter *D* is:

$A={\frac {\pi D^{2}}{4}}$

- The mass flow rate across the propeller is:

${\dot {m}}={\rho AC}$

- Since thrust is change in mass multiplied by the velocity of the mass flow i.e., change in momentum, the axial thrust on the propeller disc due to change in momentum of air, which is:

$F_{\rm {x}}={\dot {m}}{(C_{\rm {s}}-C_{\rm {u}})}={\rho AC}{(C_{\rm {s}}-C_{\rm {u}})}$

- Applying Bernoulli's principle upstream and downstream:

${\begin{aligned}P_{a}+{\frac {1}{2}}{\rho C_{u}^{2}}&=P_{1}+{\frac {1}{2}}{\rho C^{2}}\\P_{a}+{\frac {1}{2}}{\rho C_{s}^{2}}&=P_{2}+{\frac {1}{2}}{\rho C^{2}}\end{aligned}}$

On subtracting the above equations:

$P_{2}-P_{1}={\frac {1}{2}}\rho (C_{s}^{2}-C_{u}^{2})$

- Thrust difference due to pressure difference is projected area multiplied by the pressure difference. Axial thrust due to pressure difference comes out to be:

$F_{x}=A(P_{2}-P_{1})={\frac {1}{2}}\rho A\left(C_{s}^{2}-C_{u}^{2}\right)$

Comparing this thrust with the axial thrust due to change in momentum of air flow, it is found that:

$C={\frac {C_{s}+C_{u}}{2}}$

A parameter 'a' is defined such that -

$C=(1+a)C_{u}$

where

$a={\frac {C}{C_{u}}}-1$

Using the previous equation and "a", an expression for Cs comes out to be:

$C_{s}=(1+2a)C_{u}$

- Calculating the change in specific stagnation enthalpy across disc:

$\Delta h_{o}=h_{od}-h_{ou}=\left(h_{d}+{\frac {1}{2}}C_{s}^{2}\right)-\left(h_{u}+{\frac {1}{2}}C_{u}^{2}\right)={\frac {1}{2}}\left(C_{s}^{2}-C_{u}^{2}\right)$

Now, Ideal Value of Power supplied to the Propeller = Mass flow rate * Change in Stagnation enthalpy;

$P_{i}={\dot {m}}{\Delta h_{o}}$

where

${\dot {m}}=\rho AC$

If propeller was employed to propel an aircraft at speed = Cu; then Useful Power = Axial Thrust * Speed of Aircraft;

$P=F_{x}C_{u}$

- Hence the expression for efficiency comes out to be:

$\eta _{p}={\frac {{\text{Actual Power}}(P)}{{\text{Ideal Power}}(P_{i})}}={\frac {F_{x}C_{u}}{{\frac {1}{2}}\rho AC\left(C_{s}^{2}-C_{u}^{2}\right)}}={\frac {C_{u}}{C}}={\frac {1}{1+a}}$

- Let *Ds* be the diameter of the *imaginary* outlet cylinder. By Continuity Equation; ${\begin{aligned}C{\frac {\pi D^{2}}{4}}&=C_{s}{\frac {\pi D_{s}^{2}}{4}}\\\Rightarrow D_{s}^{2}&={\frac {C}{C_{s}}}D^{2}\end{aligned}}$
- From the above equations it is known that - $C_{s}={\frac {1+2a}{1+a}}C$

Therefore;

$D_{s}^{2}=\left({\frac {1+a}{1+2a}}\right)D^{2}$

Hence the flow can be modeled where the air flows through an imaginary diverging duct, where diameter of propeller disc and diameter of the outlet are related.

### Blade element theory

In this theory, a small element (*dr*) is taken at a distance *r* from the root of the blade and all the forces acting on the element are analysed to get a solution. It is assumed that the flow through each section of small radial thickness *dr* is assumed to be independent of the flow through other elements.

Resolving Forces in the figure -

$\Delta F_{x}=\Delta L\sin(\beta )-\Delta D\cos(\beta )$

$\Delta F_{y}=\Delta L\cos(\beta )+\Delta D\sin(\beta )$

Lift Coefficient (CL) and Drag Coefficient (CD) are given as -

$\mathrm {Lift} (\Delta L)={\frac {1}{2}}C_{L}\rho w^{2}(ldr)$

$\mathrm {Drag} (\Delta D)={\frac {1}{2}}C_{D}\rho w^{2}(ldr)$

Also from the figure -

$\tan(\phi )={\frac {\Delta D}{\Delta L}}={\frac {C_{D}}{C_{L}}}$

Now,

$\Delta F_{x}=\Delta L(\sin \beta -{\frac {\Delta D}{\Delta L}}\cos \beta )=\Delta L(\sin \beta -\tan \phi \cos \beta )={\frac {1}{2}}C_{L}\rho w^{2}ldr{\frac {\sin(\beta -\phi )}{\cos \phi }}$

No. of Blades (z) and Spacing (s) are related as, $s={\frac {2\pi r}{z}}$ and the total thrust for the elemental section of the propeller is **zΔFx**.

Therefore,

$\Delta p(2\pi rdr)=z\Delta F_{x}$

$\Rightarrow \Delta p={\frac {1}{2}}C_{L}\rho w^{2}({\frac {l}{s}}){\frac {\sin(\beta -\phi )}{\cos \phi }}={\frac {1}{2}}C_{D}\rho w^{2}({\frac {l}{s}}){\frac {\sin(\beta -\phi )}{\sin \phi }}$

Similarly, solving for ΔFy, ΔFy is found out to be -

$\Delta F_{y}={\frac {1}{2}}C_{L}\rho w^{2}ldr{\frac {\cos(\beta -\phi )}{\cos \phi }}$

and $(\mathrm {Torque} )\Delta Q=r\Delta F_{y}$

Finally, thrust and torque can be found out for an elemental section as they are proportional to Fx and Fy respectively.

## Performance characteristics

The relationship between the pressure variation and the volume flow rate are important characteristics of fans. The typical characteristics of axial fans can be studied from the performance curves. The performance curve for the axial fan is shown in the figure. (The vertical line joining the maximum efficiency point is drawn which meets the Pressure curve at point "S") The following can be inferred from the curve -

1. As the flow rate increases from zero the efficiency increases to a particular point reaches maximum value and then decreases.
2. The power output of the fans increases with almost constant positive slope.
3. The pressure fluctuations are observed at low discharges and at flow rates(as indicated by the point "S" ) the pressure deceases.
4. The pressure variations to the left of the point "S" causes for unsteady flow which are due to the two effects of Stalling and surging.

## Causes of unstable flow

Stalling and surging affects the fan performance, blades, as well as output and are thus undesirable. They occur because of the improper design, fan physical properties and are generally accompanied by noise generation.

### Stalling effect/Stall

The cause for this is the separation of the flow from the blade surfaces. This effect can be explained by the flow over an air foil. When the angle of incidence increases (during the low velocity flow) at the entrance of the air foil, flow pattern changes and separation occurs. This is the first stage of stalling and through this separation point the flow separates leading to the formation of vortices, back flow in the separated region. For a further the explanation of stall and rotating stall, refer to compressor surge. The stall zone for the single axial fan and axial fans operated in parallel are shown in the figure.

The following can be inferred from the graph :

- For the Fans operated in parallel, the performance is less when compared to the individual fans.
- The fans should be operated in safe operation zone to avoid the stalling effects.

#### VFDs are not practical for some Axial fans

Many Axial fan failures have happened after controlled blade axial fans were locked in a fixed position and Variable Frequency Drives (VFDs) were installed. The VFDs are not practical for some Axial fans. Axial fans with severe instability regions should not be operated at blades angles, rotational speeds, mass flow rates, and pressures that expose the fan to stall conditions.

### Surging effect/Surge

Surging should not be confused with stalling. Stalling occurs only if there is insufficient air entering into the fan blades causing separation of flow on the blade surface. Surging or the Unstable flow causing complete breakdown in fans is mainly contributed by the three factors

- System surge
- Fan surge
- Paralleling

#### System surge

This situation occurs when the system resistance curve and static pressure curve of the fan intersect have similar slope or parallel to each other. Rather than intersecting at a definite point the curves intersect over certain region reporting system surge. These characteristics are not observed in axial fans.

#### Fan surge

This unstable operation results from the development of pressure gradients in the opposite direction of the flow. Maximum pressure is observed at the discharge of the impeller blade and minimum pressure on the side opposite to the discharge side. When the impeller blades are not rotating these adverse pressure gradients pump the flow in the direction opposite to the direction of the fan. The result is the oscillation of the fan blades creating vibrations and hence noise.

### Paralleling

This effect is seen only in case of multiple fans. The air flow capacities of the fans are compared and connected in same outlet or same inlet conditions. This causes noise, specifically referred to as Beating in case of fans in parallel. To avoid beating use is made of differing inlet conditions, differences in rotational speeds of the fans, etc.

## Methods to avoid unsteady flow

By designing the fan blades with proper hub-to-tip ratio and analyzing performance on the number of blades so that the flow doesn't separate on the blade surface these effects can be reduced. Some of the methods to overcome these effects are re-circulation of excess air through the fan, axial fans are high specific speed devices operating them at high efficiency and to minimize the effects they have to be operated at low speeds. For controlling and directing the flow use of guide vanes is suggested. Turbulent flows at the inlet and outlet of the fans cause stalling so the flow should be made laminar by the introduction of a stator to prevent the effect.
