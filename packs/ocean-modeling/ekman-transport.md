---
title: "Ekman transport"
source: https://en.wikipedia.org/wiki/Ekman_transport
domain: ocean-modeling
license: CC-BY-SA-4.0
tags: ocean general circulation model, physical oceanography, thermohaline circulation, ekman transport
fetched: 2026-07-02
---

# Ekman transport

**Ekman transport** is part of Ekman motion theory, first investigated in 1902 by Vagn Walfrid Ekman. Winds are the main source of energy for ocean circulation, and Ekman transport is a component of wind-driven ocean current. Ekman transport occurs when ocean surface waters are influenced by the friction force acting on them via the wind. As the wind blows it casts a friction force on the ocean surface that drags the upper 10-100m of the water column with it. However, due to the influence of the Coriolis effect, as the ocean water moves it is subject to a force at a 90° angle from the direction of motion causing the water to move at an angle to the wind direction. The direction of transport is dependent on the hemisphere: in the Northern Hemisphere, transport veers clockwise from wind direction, while in the Southern Hemisphere it veers anticlockwise. This phenomenon was first noted by Fridtjof Nansen, who recorded that ice transport appeared to occur at an angle to the wind direction during his Arctic expedition of the 1890s. Ekman transport has significant impacts on the biogeochemical properties of the world's oceans. This is because it leads to upwelling (Ekman suction) and downwelling (Ekman pumping) in order to obey mass conservation laws. Mass conservation, in reference to Ekman transfer, requires that any water displaced within an area must be replenished. This can be done by either Ekman suction or Ekman pumping depending on wind patterns.

## Mechanisms

There are three major wind patterns that lead to Ekman suction or pumping. The first are wind patterns that are parallel to the coastline. Due to the Coriolis effect, surface water moves at a 90° angle to the wind current. If the wind moves in a direction causing the water to be pulled away from the coast then Ekman suction will occur. On the other hand, if the wind is moving in such a way that surface waters move towards the shoreline then Ekman pumping will take place.

The second mechanism of wind currents resulting in Ekman transfer is the Trade Winds both north and south of the equator pulling surface waters towards the poles. There is a great deal of upwelling Ekman suction at the equator because water is being pulled northward north of the equator and southward south of the equator. This leads to a divergence in the water, resulting in Ekman suction, and therefore, upwelling.

The third wind pattern influencing Ekman transfer is large-scale wind patterns in the open ocean. Open ocean wind circulation can lead to gyre-like structures of piled up sea surface water resulting in horizontal gradients of sea surface height. This pile up of water causes the water to have a downward flow and suction, due to gravity and mass balance. Ekman pumping downward in the central ocean is a consequence of this convergence of water.

## Ekman suction

Ekman suction is the component of Ekman transport that results in areas of upwelling due to the divergence of water. Returning to the concept of mass conservation, any water displaced by Ekman transport must be replenished. As the water diverges it creates space and acts as a suction in order to fill in the space by pulling up, or upwelling, deep sea water to the euphotic zone.

Ekman suction has major consequences for the biogeochemical processes in the area because it leads to upwelling. Upwelling carries nutrient rich, and cold deep-sea water to the euphotic zone, promoting phytoplankton blooms and kickstarting an extremely productive environment. Areas of upwelling lead to the promotion of fisheries with nearly half of the world's fish catch coming from areas of upwelling.

Ekman suction occurs both along coastlines and in the open ocean, but also occurs along the equator. Along the Pacific coastline of California, Central America, and Peru, as well as along the Atlantic coastline of Africa there are areas of upwelling due to Ekman suction, as the currents move equatorwards. Due to the Coriolis effect the surface water moves 90° to the left (in the Southern Hemisphere, as it travels toward the equator) of the wind current, therefore causing the water to diverge from the coast boundary, leading to Ekman suction. Additionally, there are areas of upwelling as a consequence of Ekman suction where the Polar Easterlies winds meet the Westerlies in the subpolar regions north of the subtropics, as well as where the Northeast Trade Winds meet the Southeast Trade Winds along the Equator.

## Ekman pumping

Ekman pumping is the component of Ekman transport that results in areas of downwelling due to the convergence of water. As discussed above, the concept of mass conservation requires that a pile up of surface water must be pushed downward. This pile up of warm, nutrient-poor surface water gets pumped vertically down the water column, resulting in areas of downwelling.

Ekman pumping has dramatic impacts on the surrounding environments. Downwelling, due to Ekman pumping, leads to nutrient poor waters, therefore reducing the biological productivity of the area. Additionally, it transports heat and dissolved oxygen vertically down the water column as warm oxygen rich surface water is being pumped towards the deep ocean water.

Ekman pumping can be found along the coasts as well as in the open ocean. Along the Pacific Coast in the Southern Hemisphere northerly winds move parallel to the coastline. Due to the Coriolis effect the surface water gets pulled 90° to the left of the wind current, therefore causing the water to converge along the coast boundary, leading to Ekman pumping. In the open ocean Ekman pumping occurs with gyres. Specifically, in the subtropics, between 20°N and 50°N, there is Ekman pumping as the tradewinds shift to westerlies causing a pile up of surface water.

## Mathematical derivation

Some assumptions of the fluid dynamics involved in the process must be made in order to simplify the process to a point where it is solvable. The assumptions made by Ekman were:

- no boundaries;
- infinitely deep water;
- eddy viscosity, $A_{z}\,\!$ , is constant (this is only true for laminar flow. In the turbulent atmospheric and oceanic boundary layer it is a strong function of depth);
- the wind forcing is steady and has been blowing for a long time;
- barotropic conditions with no geostrophic flow;
- the Coriolis parameter, $f\,\!$ is kept constant.

The simplified equations for the Coriolis force in the *x* and *y* directions follow from these assumptions:

(1)

${\frac {1}{\rho }}{\frac {\partial \tau _{x}}{\partial z}}=-fv,\,$

(2)

${\frac {1}{\rho }}{\frac {\partial \tau _{y}}{\partial z}}=fu,\,$

where $\tau \,\!$ is the wind stress, $\rho \,\!$ is the density, $u\,\!$ is the east–west velocity, and $v\,\!$ is the north–south velocity.

Integrating each equation over the entire Ekman layer:

$\tau _{x}=-M_{y}f,\,$

$\tau _{y}=M_{x}f,\,$

where

$M_{x}=\int _{0}^{z}\rho udz,\,$

$M_{y}=\int _{0}^{z}\rho vdz.\,$

Here $M_{x}\,\!$ and $M_{y}\,\!$ represent the zonal and meridional mass transport terms with units of mass per unit time per unit length. Contrarily to common logic, north–south winds cause mass transport in the east–west direction.

In order to understand the vertical velocity structure of the water column, equations **1** and **2** can be rewritten in terms of the vertical eddy viscosity term.

${\frac {\partial \tau _{x}}{\partial z}}=\rho A_{z}{\frac {\partial ^{2}u}{\partial z^{2}}},\,\!$

${\frac {\partial \tau _{y}}{\partial z}}=\rho A_{z}{\frac {\partial ^{2}v}{\partial z^{2}}},\,\!$

where $A_{z}\,\!$ is the vertical eddy viscosity coefficient.

This gives a set of differential equations of the form

$A_{z}{\frac {\partial ^{2}u}{\partial z^{2}}}=-fv,\,\!$

$A_{z}{\frac {\partial ^{2}v}{\partial z^{2}}}=fu.\,\!$

In order to solve this system of two differential equations, two boundary conditions can be applied:

- ${(u,v)\to 0}$ as ${z\to -\infty },$
- friction is equal to wind stress at the free surface ( $z=0\,\!$ ).

Things can be further simplified by considering wind blowing in the *y*-direction only. This means is the results will be relative to a north–south wind (although these solutions could be produced relative to wind in any other direction):

(3)

${\begin{aligned}u_{E}&=\pm V_{0}\cos \left({\frac {\pi }{4}}+{\frac {\pi }{D_{E}}}z\right)\exp \left({\frac {\pi }{D_{E}}}z\right),\\v_{E}&=V_{0}\sin \left({\frac {\pi }{4}}+{\frac {\pi }{D_{E}}}z\right)\exp \left({\frac {\pi }{D_{E}}}z\right),\end{aligned}}$

where

- $u_{E}\,\!$ and $v_{E}\,\!$ represent Ekman transport in the *u* and *v* direction;
- in equation **3** the plus sign applies to the Northern Hemisphere and the minus sign to the southern hemisphere;
- $V_{0}={\frac {{\sqrt {2}}\pi \tau _{y\eta }}{D_{E}\rho |f|}};\,\!$
- $\tau _{y\eta }\,\!$ is the wind stress on the sea surface;
- $D_{E}=\pi \left({\frac {2A_{z}}{|f|}}\right)^{1/2}\,\!$ is the Ekman depth (depth of Ekman layer).

By solving this at *z*=0, the surface current is found to be (as expected) 45 degrees to the right (left) of the wind in the Northern (Southern) Hemisphere. This also gives the expected shape of the Ekman spiral, both in magnitude and direction. Integrating these equations over the Ekman layer shows that the net Ekman transport term is 90 degrees to the right (left) of the wind in the Northern (Southern) Hemisphere.

## Applications

- Ekman transport leads to coastal upwelling, which provides the nutrient supply for some of the largest fishing markets on the planet and can impact the stability of the Antarctic Ice Sheet by pulling warm deep water onto the continental shelf. Wind in these regimes blows parallel to the coast (such as along the coast of Peru, where the wind blows out of the southeast, and also in California, where it blows out of the northwest). From Ekman transport, surface water has a net movement of 90° to right of wind direction in the Northern Hemisphere (left in the Southern Hemisphere). Because the surface water flows away from the coast, the water must be replaced with water from below. In shallow coastal waters, the Ekman spiral is normally not fully formed and the wind events that cause upwelling episodes are typically rather short. This leads to many variations in the extent of upwelling, but the ideas are still generally applicable.
- Ekman transport is similarly at work in equatorial upwelling, where, in both hemispheres, a trade wind component towards the west causes a net transport of water towards the pole, and a trade wind component towards the east causes a net transport of water away from the pole.
- On smaller scales, cyclonic winds induce Ekman transport which causes net divergence and upwelling, or Ekman suction, while anti-cyclonic winds cause net convergence and downwelling, or Ekman pumping
- Ekman transport is also a factor in the circulation of the ocean gyres and garbage patches. Ekman transport causes water to flow toward the center of the gyre in all locations, creating a sloped sea-surface, and initiating geostrophic flow (Colling p 65). Harald Sverdrup applied Ekman transport while including pressure gradient forces to develop a theory for this (see Sverdrup balance).

## Exceptions

The Ekman theory describing wind-induced current on a rotating planet explains why surface currents in the Northern Hemisphere are generally deflected to the right of wind direction, and in the Southern Hemisphere to the left in most cases. There are also solutions for opposite deflections at periods shorter than the local inertial period, which were not mentioned by Ekman, and are seldom observed. A major example of this effect occurs in the Bay of Bengal, where surface flow is offset to the left of wind direction in the Northern Hemisphere. Ekman's theory can be refined to include this case.

## History

Ekman developed the theory of the Ekman layer after Fridtjof Nansen observed that ice drifts at an angle of 20°–40° to the right of the prevailing wind direction while on an Arctic expedition aboard the Fram. Nansen asked his colleague, Vilhelm Bjerknes to set one of his students upon study of the problem. Bjerknes tapped Ekman, who presented his results in 1902 as his doctoral thesis.

## Theory

Ekman theory explains the theoretical state of circulation if water currents were driven only by the transfer of momentum from the wind. In the physical world, this is difficult to observe because of the influences of many simultaneous current driving forces (for example, pressure and density gradients). Though the following theory technically applies to the idealized situation involving only wind forces, Ekman motion describes the wind-driven portion of circulation seen in the surface layer.

Surface currents flow at a 45° angle to the wind due to a balance between the Coriolis force and the drags generated by the wind and the water. If the ocean is divided vertically into thin layers, the magnitude of the velocity (the speed) decreases from a maximum at the surface until it dissipates. The direction also shifts slightly across each subsequent layer (right in the Northern Hemisphere and left in the Southern Hemisphere). This is called an *Ekman spiral*. The layer of water from the surface to the point of dissipation of this spiral is known as the *Ekman layer*. If all flow over the Ekman layer is integrated, the net transportation is at 90° to the right (left) of the surface wind in the Northern (Southern) Hemisphere.

### Ekman spiral

The **Ekman spiral** is an arrangement of ocean currents: the directions of horizontal current appear to twist as the depth changes. The oceanic wind driven Ekman spiral is the result of a force balance created by a shear stress force, Coriolis force and the water drag. This force balance gives a resulting current of the water different from the winds. In the ocean, there are two places where the Ekman spiral can be observed. At the surface of the ocean, the shear stress force corresponds with the wind stress force. At the bottom of the ocean, the shear stress force is created by friction with the ocean floor. This phenomenon was first observed at the surface by the Norwegian oceanographer Fridtjof Nansen during his Fram expedition. He noticed that icebergs did not drift in the same direction as the wind. His student, the Swedish oceanographer Vagn Walfrid Ekman, was the first person to physically explain this process.

#### Bottom Ekman spiral

In order to derive the properties of an Ekman spiral a look is taken at a uniform, horizontal geostrophic interior flow in a homogeneous fluid. This flow will be denoted by ${\vec {u}}=({\bar {u}},{\bar {v}})$ , where the two components are constant because of uniformity. Another result of this property is that the horizontal gradients will equal zero. As a result, the continuity equation will yield, ${\frac {\partial w}{\partial z}}=0$ . Note that the concerning interior flow is horizontal, so $w=0$ at all depths, even in the boundary layers. In this case, the Navier-Stokes momentum equations, governing geophysical motion can now be reduced to:

${\begin{aligned}-fv&=-{\frac {1}{\rho _{0}}}{\frac {\partial p}{\partial x}}+\nu _{E}{\frac {\partial ^{2}u}{\partial z^{2}}},\\[5pt]fu&=-{\frac {1}{\rho _{0}}}{\frac {\partial p}{\partial y}}+\nu _{E}{\frac {\partial ^{2}v}{\partial z^{2}}},\\[5pt]0&=-{\frac {1}{\rho _{0}}}{\frac {\partial p}{\partial z}},\end{aligned}}$

Where f is the Coriolis parameter, $\rho _{0}$ the fluid density and $\nu _{E}$ the eddy viscosity, which are all taken as a constant here for simplicity. These parameters have a small variance on the scale of an Ekman spiral, thus this approximation will hold. A uniform flow requires a uniformly varying pressure gradient. When substituting the flow components of the interior flow, $u={\bar {u}}$ and $v={\bar {v}}$ , in the equations above, the following is obtained:

${\begin{aligned}-f{\bar {v}}&=-{\frac {1}{\rho _{0}}}{\frac {\partial p}{\partial x}}={\text{constant}}\\[5pt]f{\bar {u}}&=-{\frac {1}{\rho _{0}}}{\frac {\partial p}{\partial y}}={\text{constant}}\end{aligned}}$

Using the last of the three equations at the top of this section, yields that the pressure is independent of depth.

${\begin{aligned}-f(v-{\bar {v}})&=\nu _{E}{\frac {\partial ^{2}u}{\partial z^{2}}}\\[5pt]f(u-{\bar {u}})&=\nu _{E}{\frac {\partial ^{2}v}{\partial z^{2}}}\end{aligned}}$

$u={\bar {u}}+Ae^{\lambda z}$ and $v={\bar {v}}+Be^{\lambda z}$ will suffice as a solution to the differential equations above. After substitution of these possible solutions in the same equations, $\nu _{E}^{2}\lambda ^{4}+f^{2}=0$ will follow. Now, $\lambda$ has the following possible outcomes:

$\lambda =\pm (1\pm i){\sqrt {\frac {f}{2\nu _{E}}}}$

Because of the no-slip condition at the bottom and the constant interior flow for $z\gg d$ , coefficients A and B can be determined. In the end, this will lead to the following solution for ${\vec {u}}(z)$ :

${\begin{aligned}u&={\bar {u}}\left[1-e^{-z/d}\cos \left({\frac {z}{d}}\right)\right]-{\bar {v}}e^{-z/d}\sin \left({\frac {z}{d}}\right),\\[5pt]v&={\bar {u}}e^{-z/d}\sin \left({\frac {z}{d}}\right)+{\bar {v}}\left[1-e^{-z/d}\cos \left({\frac {z}{d}}\right)\right],\end{aligned}}$

Here, $d={\sqrt {\frac {2\nu _{E}}{f}}}$ . Note that the velocity vector will approach the values of the interior flow, when the z takes the order of d . This is the reason why d is defined as the thickness of the Ekman layer. A number of important properties of the Ekman spiral will follow from this solution:

- When $z\rightarrow {0}$ , it appears that the flow has a transverse component with respect to the interior flow, which differs 45 degrees to the left on the Northern Hemisphere, $f>0$ , and 45 degrees to the right on the Southern Hemisphere, $f<0$ . Note that, in this case, the angle between this flow and the interior flow is at its maximum. It will decrease for increasing z .
- When ${\frac {z}{d}}$ takes the value of $\pi$ , the resulting flow is in line with the interior flow, but will be increased with $e^{-\pi }$ , with respect to the interior flow.
- For higher values of ${\frac {z}{d}}$ , there will be a minimal transverse component in the other direction as before. The exponential term will go to zero for $z\gg d$ , resulting in ${\vec {u}}=({\bar {u}},{\bar {v}})$ . Because of these properties, the velocity vector of the flow as a function of depth will look like a spiral.

#### Surface Ekman spiral

The solution for the flow forming the bottom Ekman spiral was a result of the shear stress exerted on the flow by the bottom. Logically, wherever shear stress can be exerted on a flow, Ekman spirals will form. This is the case at the air–water interface, because of wind. A situation is considered where a wind stress ${\vec {\tau }}=(\tau _{x},\tau _{y})$ is exerted along a water-surface with an interior flow ${\vec {u}}=(u,v)$ beneath. Again, the flow is uniform, has a geostrophic interior and is homogeneous fluid. The equations of motion for a geostrophic flow, which are the same as stated in the bottom spiral section, can be reduced to:

${\begin{aligned}-f(v-{\bar {v}})&=\nu _{E}{\frac {\partial ^{2}u}{\partial z^{2}}}\\[5pt]f(u-{\bar {u}})&=\nu _{E}{\frac {\partial ^{2}v}{\partial z^{2}}}\\\end{aligned}}$

The boundary conditions for this case are as follows:

- Surface $(z=0)$ : $\;\;\;\rho _{0}\nu _{E}{\frac {\partial u}{\partial z}}=\tau _{x}\;$ and $\;\rho _{0}\nu _{E}{\frac {\partial v}{\partial z}}=\tau _{y}$
- Towards interior $(z\rightarrow {-\infty })$ : $\;\;\;u={\bar {u}}\;$ and $\;v={\bar {v}}$

With these conditions, the solution can be determined:

${\begin{aligned}u&={\bar {u}}+{\frac {\sqrt {2}}{\rho _{0}fd}}e^{z/d}\left[\tau _{x}\cos \left({\frac {z}{d}}-{\frac {\pi }{4}}\right)-\tau _{y}\sin \left({\frac {z}{d}}-{\frac {\pi }{4}}\right)\right]\\[5pt]v&={\bar {v}}+{\frac {\sqrt {2}}{\rho _{0}fd}}e^{z/d}\left[\tau _{x}\sin \left({\frac {z}{d}}-{\frac {\pi }{4}}\right)+\tau _{y}\cos \left({\frac {z}{d}}-{\frac {\pi }{4}}\right)\right]\end{aligned}}$

Some differences with respect to the bottom Ekman spiral emerge. The deviation from the interior flow is exclusively dependent on the wind stress and not on the interior flow. Whereas in the case of the bottom Ekman spiral, the deviation is determined by the interior flow. The wind-driven component of the flow is inversely proportional with respect to the Ekman-layer thickness d . So if the layer thickness is small, because of a small viscosity of the fluid for example, this component could be very large. At last, the flow at the surface is 45 degrees to the right on the Northern Hemisphere and 45 degrees to the left on the Southern Hemisphere with respect to the wind-direction. In case of the bottom Ekman spiral, this is the other way around.

#### Observations

The equations and assumptions above are not representative for the actual observations of the Ekman spiral. The differences between the theory and the observations are that the angle is between 5–20 degrees instead of the 45 degrees as expected and that the Ekman layer depth and thus the Ekman spiral is less deep than expected. There are three main factors which contribute to the reason why this is, stratification, turbulence and horizontal gradients. Other less important factors which play a role in this are the Stokes drift, waves and the Stokes-Coriolis force.

### Ekman layer

The **Ekman layer** is the layer in a fluid where there is a force balance between pressure gradient force, Coriolis force and turbulent drag. It was first described by Vagn Walfrid Ekman. Ekman layers occur both in the atmosphere and in the ocean.

There are two types of Ekman layers. The first type occurs at the surface of the ocean and is forced by surface winds, which act as a drag on the surface of the ocean. The second type occurs at the bottom of the atmosphere and ocean, where frictional forces are associated with flow over rough surfaces.

#### Mathematical formulation

The mathematical formulation of the Ekman layer begins by assuming a neutrally stratified fluid, a balance between the forces of pressure gradient, Coriolis and turbulent drag.

${\begin{aligned}-fv&=-{\frac {1}{\rho _{o}}}{\frac {\partial p}{\partial x}}+K_{m}{\frac {\partial ^{2}u}{\partial z^{2}}},\\[5pt]fu&=-{\frac {1}{\rho _{o}}}{\frac {\partial p}{\partial y}}+K_{m}{\frac {\partial ^{2}v}{\partial z^{2}}},\\[5pt]0&=-{\frac {1}{\rho _{o}}}{\frac {\partial p}{\partial z}},\end{aligned}}$

where $\ u$ and $\ v$ are the velocities in the $\ x$ and $\ y$ directions, respectively, $\ f$ is the local Coriolis parameter, and $\ K_{m}$ is the diffusive eddy viscosity, which can be derived using mixing length theory. Note that p is a modified pressure: we have incorporated the hydrostatic of the pressure, to take account of gravity.

There are many regions where an Ekman layer is theoretically plausible; they include the bottom of the atmosphere, near the surface of the earth and ocean, the bottom of the ocean, near the sea floor and at the top of the ocean, near the air-water interface. Different boundary conditions are appropriate for each of these different situations. Each of these situations can be accounted for through the boundary conditions applied to the resulting system of ordinary differential equations. The separate cases of top and bottom boundary layers are shown below.

#### Ekman layer at the ocean (or free) surface

We will consider boundary conditions of the Ekman layer in the upper ocean:

${\text{at }}z=0:\quad A{\frac {\partial u}{\partial z}}=\tau ^{x}\quad {\text{and}}\quad A{\frac {\partial v}{\partial z}}=\tau ^{y},$

where $\ \tau ^{x}$ and $\ \tau ^{y}$ are the components of the surface stress, $\ \tau$ , of the wind field or ice layer at the top of the ocean, and $\ A\equiv \rho K_{m}$ is the dynamic viscosity.

For the boundary condition on the other side, as $\ z\to -\infty :u\to u_{g},v\to v_{g}$ , where $\ u_{g}$ and $\ v_{g}$ are the geostrophic flows in the $\ x$ and $\ y$ directions.

#### Solution

These differential equations can be solved to find:

${\begin{aligned}u&=u_{g}+{\frac {\sqrt {2}}{\rho _{o}fd}}e^{z/d}\left[\tau ^{x}\cos(z/d-\pi /4)-\tau ^{y}\sin(z/d-\pi /4)\right],\\[5pt]v&=v_{g}+{\frac {\sqrt {2}}{\rho _{o}fd}}e^{z/d}\left[\tau ^{x}\sin(z/d-\pi /4)+\tau ^{y}\cos(z/d-\pi /4)\right],\\[5pt]d&={\sqrt {2K_{m}/|f|}}.\end{aligned}}$

The value d is called the Ekman layer depth, and gives an indication of the penetration depth of wind-induced turbulent mixing in the ocean. Note that it varies on two parameters: the turbulent diffusivity $K_{m}$ , and the latitude, as encapsulated by f . For a typical $K_{m}=0.1$ m $^{2}$ /s, and at 45° latitude ( $f=10^{-4}$ s $^{-1}$ ), then d is approximately 45 meters. This Ekman depth prediction does not always agree precisely with observations.

This variation of horizontal velocity with depth ( $-z$ ) is referred to as the Ekman spiral, diagrammed above and at right.

By applying the continuity equation we can have the vertical velocity as following

$w={\frac {1}{f\rho _{o}}}\left[-\left({\frac {\partial \tau ^{x}}{\partial x}}+{\frac {\partial \tau ^{y}}{\partial y}}\right)e^{z/d}\sin(z/d)+\left({\frac {\partial \tau ^{y}}{\partial x}}-{\frac {\partial \tau ^{x}}{\partial y}}\right)(1-e^{z/d}\cos(z/d))\right].$

Note that when vertically-integrated, the volume transport associated with the Ekman spiral is to the right of the wind direction in the Northern Hemisphere.

#### Ekman layer at the bottom of the ocean and atmosphere

The traditional development of Ekman layers bounded below by a surface utilizes two boundary conditions:

- A no-slip condition at the surface;
- The Ekman velocities approaching the geostrophic velocities as z goes to infinity.

#### Experimental observations of the Ekman layer

There is much difficulty associated with observing the Ekman layer for two main reasons: the theory is too simplistic as it assumes a constant eddy viscosity, which Ekman himself anticipated, saying

> It is obvious that $\ \left[\nu \right]$ cannot generally be regarded as a constant when the density of water is not uniform within the region considered

and because it is difficult to design instruments with great enough sensitivity to observe the velocity profile in the ocean.

#### Laboratory demonstrations

The bottom Ekman layer can readily be observed in a rotating cylindrical tank of water by dropping in dye and changing the rotation rate slightly. Surface Ekman layers can also be observed in rotating tanks.

#### In the atmosphere

In the atmosphere, the Ekman solution generally overstates the magnitude of the horizontal wind field because it does not account for the velocity shear in the surface layer. Splitting the planetary boundary layer into the surface layer and the Ekman layer generally yields more accurate results.

#### In the ocean

The Ekman layer, with its distinguishing feature the Ekman spiral, is rarely observed in the ocean. The Ekman layer near the surface of the ocean extends only about 10 – 20 meters deep, and instrumentation sensitive enough to observe a velocity profile in such a shallow depth has only been available since around 1980. Also, wind waves modify the flow near the surface, and make observations close to the surface rather difficult.

#### Instrumentation

Observations of the Ekman layer have only been possible since the development of robust surface moorings and sensitive current meters. Ekman himself developed a current meter to observe the spiral that bears his name, but was not successful. The Vector Measuring Current Meter and the Acoustic Doppler Current Profiler are both used to measure current.

#### Observations

The first documented observations of an Ekman-like spiral in the ocean were made in the Arctic Ocean from a drifting ice floe in 1958. More recent observations include (not an exhaustive list):

- The 1980 mixed layer experiment
- Within the Sargasso Sea during the 1982 Long Term Upper Ocean Study
- Within the California Current during the 1993 Eastern Boundary Current experiment
- Within the Drake Passage region of the Southern Ocean
- In the eastern tropical Pacific, at 2°N, 140°W, using 5 current meters between 5 and 25 meters depth. This study noted that the geostrophic shear associated with tropical stability waves modified the Ekman spiral relative to what is expected with horizontally uniform density.
- North of the Kerguelen Plateau during the 2008 SOFINE experiment

Common to several of these observations spirals were found to be "compressed", displaying larger estimates of eddy viscosity when considering the rate of rotation with depth than the eddy viscosity derived from considering the rate of decay of speed.
