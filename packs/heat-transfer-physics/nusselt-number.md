---
title: "Nusselt number"
source: https://en.wikipedia.org/wiki/Nusselt_number
domain: heat-transfer-physics
license: CC-BY-SA-4.0
tags: heat transfer, thermal conduction, thermal radiation, heat equation
fetched: 2026-07-02
---

# Nusselt number

The **Nusselt number** is a nondimensionalization of the convective heat transfer coefficient. Like the heat transfer coefficient, the Nusselt number may be defined locally, at a single position on a surface, or as an average value that represents the heat flow from the entire surface.

The Nusselt number is named in honor of Wilhelm Nusselt, who first identified this dimensionless group in 1915.

Analytical results and empirical correlations allow the Nusselt number to be estimated in many situations. For forced convection, these expressions depend on the Reynolds number and the Prandtl number. For natural convection (or "free" convection) the predictions use the Grashof number or Rayleigh number along with the Prandtl number.

The mass transfer analog of the Nusselt number is the Sherwood number.

## History

The group now known as the Nusselt number was first identified by Wilhelm Nusselt in a 1915 paper. In that paper, he also identified the groups that became the Grashof number, the Prandtl number, and the Reynolds number. Nusselt used these groups effectively to correlate data for natural convection and, in a 1917 paper, forced convection.

In 1931, the Association of German Engineers formally named the dimensionless group the *Nusselt number*. The decision was announced in paper by Max Jakob. The term was quickly adopted internationally.

## Definition

The heat transfer coefficient, h , at a surface cooled by a fluid is the ratio of the heat flux q [W/m2] from the surface to the temperature difference $\Delta T$ [K] between the surface and the fluid far from the surface: $h=q/\Delta T$ [W/(m2·K)]. The Nusselt number, ${\textrm {Nu}}$ , is formed by nondimensionalizing h with a characteristic length L [m] and the thermal conductivity of the fluid k [W/(m·K)]:

$\mathrm {Nu} _{L}={\frac {qL}{k\Delta T}}={\frac {hL}{k}}$

The Nusselt number is a dimensionless group. The subscript, *L*, indicates which characteristic length is used.

### Selection of characteristic length

The characteristic length should be related to the thickness of the thermal boundary layer. In a tube, the thermal boundary layer will be limited by the tube diameter, D , so that the diameter represents the scale of the boundary layer. On a flat plate, the length of the plate, L , determines the average thickness of the boundary layer on the plate. On the other hand, the local thickness of the flat plate boundary layer, at a position x , is determined by the value of x , so that x is the characteristic length for the local heat transfer coefficient on the plate.

Some additional examples of characteristic length are: the outer diameter of a cylinder in (external) crossflow (perpendicular to the cylinder axis), the height of a vertical plate undergoing natural convection, or the diameter of a sphere. For complex shapes, the length may be defined as the volume of the fluid body divided by the surface area.

### Local and average Nusselt numbers

At a location x on a surface, the local heat transfer coefficient, $h_{x}$ , relates the local heat flux, q , to the local temperature difference $\Delta T_{x}$ :

$q=h_{x}\Delta T_{x}$

The local heat transfer coefficient varies along the surface of a body. It becomes lower as the thermal boundary layer becomes thicker. It increases suddenly where the boundary layer transitions from laminar to turbulent flow.

The local Nusselt number is a nondimensionalization of the local heat transfer coefficient, $h_{x}$ , at a position x on a surface:

$\mathrm {Nu} _{x}={\frac {h_{x}x}{k}}$

The average heat transfer coefficient relates the average temperature difference to the average heat flux over the body. For an *isothermal* body the temperature difference is constant, and if the body has length L the average heat flux is

${\overline {q}}={\frac {1}{L}}\int _{0}^{L}q_{x}\ dx={\frac {1}{L}}\int _{0}^{L}h_{x}\Delta T\ dx={\frac {\Delta T}{L}}\int _{0}^{L}h_{x}\ dx={\overline {h}}\Delta T$

The *average* Nusselt number is then defined as

${\overline {\mathrm {Nu} }}_{L}={\frac {{\overline {h}}L}{k}}$

For a uniform flux surface, the temperature difference is not constant, and so the temperature difference must be averaged to find the average heat transfer coefficient:

$q={\overline {h}}\times {\overline {\Delta T}}$

The average temperature difference is another integral:

${\overline {\Delta T}}={\frac {1}{L}}\int _{0}^{L}{\frac {q}{h_{x}}}\ dx={\frac {q}{L}}\int _{0}^{L}{\frac {1}{h_{x}}}\ dx$

The average Nusselt number is defined just as for an isothermal surface:

${\overline {\mathrm {Nu} }}_{L}={\frac {{\overline {h}}L}{k}}$

The term "average Nusselt number" can cause confusion because the Nusselt number is not what has been averaged. For an isothermal surface, the heat flux has been averaged, while for a uniform flux surface, the temperature difference has been averaged.

### Stanton number

A closely related dimensionless group is the Stanton number used in some studies of forced convection:

${\textrm {St}}={\frac {\textrm {Nu}}{\textrm {RePr}}}={\frac {h}{\rho c_{p}u}}$

where $\rho ,c_{p},{\text{and }}u$ are the fluid density, specific heat capacity, and free stream speed.

### Confusion with the Biot number

A similar nondimensional group is the Biot number, which compares the thermal resistance of heat conduction in the body to the thermal resistance of convection outside the body. The Biot number uses the thermal conductivity of the solid body rather than the fluid. The Biot number should not be confused with the Nusselt number.

## Relationship of Nusselt number to laminar boundary layer thickness

An understanding of convection boundary layers is necessary to understand convective heat transfer between a surface and a fluid flowing past it. A thermal boundary layer develops if the fluid free stream temperature and the surface temperatures differ. A temperature profile is created by the energy exchange resulting from this temperature difference.

The local heat transfer rate can be written using Newton's law of cooling as

$q=h_{x}\left(T_{s}-T_{0}\right)$

At the surface of the body, the fluid velocity is zero as a result of the no-slip condition, so heat transfer in the fluid at the surface is by conduction alone:

$q=-k{\frac {\partial }{\partial y}}\left.\left(T-T_{s}\right)\right|_{y=0}$

.

These two terms are equal; thus

$h_{x}=-{\frac {k}{\left(T_{s}-T_{0}\right)}}{\frac {\partial }{\partial y}}\left.\left(T-T_{s}\right)\right|_{y=0}$

.

For a laminar boundary layer (see figure), the temperature gradient at the surface has a temperature change $T_{s}-T_{0}$ over a distance proportional to the thermal boundary layer thickness, $\delta _{t}$ , so a crude approximation is:

$-{\frac {\partial }{\partial y}}\left.\left(T-T_{s}\right)\right|_{y=0}\approx {\frac {T_{s}-T_{0}}{\delta _{t}}}$

.

Hence, the laminar Nusselt number is greater when the thermal boundary layer is thinner:

${\textrm {Nu}}_{x}={\frac {h_{x}x}{k}}\approx {\frac {x}{\delta _{t}}}$

## Analytical results and empirical correlations for Nu

For forced convection, the Nusselt number is generally a function of the Reynolds number and the Prandtl number, or

$\mathrm {Nu} =f(\mathrm {Re} ,\mathrm {Pr} )$

For free, or natural, convection, the average Nusselt number is usually expressed as a function of the Rayleigh number or Grashof number and the Prandtl number:

$\mathrm {Nu} =f(\mathrm {Ra} ,\mathrm {Pr} )$

or

$\mathrm {Nu} =f(\mathrm {Gr} ,\mathrm {Pr} )$

since Ra = GrPr.

Analytical results and empirical correlations that express the Nusselt number in the aforementioned forms are available for a wide variety of geometries.

### Evaluation of physical properties

When calculating the Nusselt number, the thermal conductivity, the Prandtl number, and the properties in the Reynolds or Grashof numbers are usually evaluated at the film temperature. The film temperature is the average of the wall temperature and free stream or bulk temperature. When the bulk temperature changes significantly along the length of the tube, the average bulk temperature can be used.

## Free, or natural, convection

### Free convection at a vertical wall

Churchill and Chu correlated a wide range of data with the following expression, which includes both laminar and turbulent flow:

${\overline {\mathrm {Nu} }}_{L}\ =\left({0.825+{\frac {0.387\mathrm {Ra} _{L}^{1/6}}{\left(1+(0.492/\mathrm {Pr} )^{9/16}\right)^{8/27}}}}\right)^{2}\,\quad \mathrm {Ra} _{L}<10^{12}$

The transition from a laminar to a turbulent boundary occurs at $\mathrm {Ra} _{L}\approx 10^{9}$ . For laminar flows, Churchill and Chu recommended the following, slightly more accurate correlation:

${\overline {\mathrm {Nu} }}_{L}\ =0.68+{\frac {0.67\mathrm {Ra} _{L}^{1/4}}{\left(1+(0.492/\mathrm {Pr} )^{9/16}\right)^{4/9}}}\,\quad 10^{-1}<\mathrm {Ra} _{L}<10^{9}$

### Free convection from horizontal plates

If the characteristic length is defined

$L\ ={\frac {A_{s}}{P}}$

where $\mathrm {A} _{s}$ is the surface area of the plate and P is its perimeter.

Then for the top surface of a hot object in a colder environment or bottom surface of a cold object in a hotter environment

${\overline {\mathrm {Nu} }}_{L}\ =0.54\,\mathrm {Ra} _{L}^{1/4}\,\quad 10^{4}\leq \mathrm {Ra} _{L}\leq 10^{7}$

${\overline {\mathrm {Nu} }}_{L}\ =0.15\,\mathrm {Ra} _{L}^{1/3}\,\quad 10^{7}\leq \mathrm {Ra} _{L}\leq 10^{11}$

And for the bottom surface of a hot object in a colder environment or top surface of a cold object in a hotter environment

${\overline {\mathrm {Nu} }}_{L}\ =0.27\,\mathrm {Ra} _{L}^{1/4}\,\quad 10^{5}\leq \mathrm {Ra} _{L}\leq 10^{10}$

### Free convection from enclosure heated from below

In 1959, Globe and Dropkin reported the following correlation for wide fluid layers between a lower heated and upper cooled plate:

${\overline {\mathrm {Nu} }}_{L}\ =0.069\,\mathrm {Ra} _{L}^{1/3}\mathrm {Pr} ^{0.074}\,\quad 1.5\times 10^{5}\leq \mathrm {Ra} _{L}\leq 6.8\times 10^{8}\;{\text{and}}\;0.02\leq \mathrm {Pr} \leq 8750$

This equation *"holds when the horizontal layer is sufficiently wide so that the effect of the short vertical sides is minimal."*

## Forced convection

### Flat plate in laminar flow

The solution of the energy and momentum equations for laminar flow over an isothermal flat plate leads to the following equation for the local Nusselt number at a distance x downstream from the leading edge of the plate.

$\mathrm {Nu} _{x}\ =0.332\,\mathrm {Re} _{x}^{1/2}\,\mathrm {Pr} ^{1/3},\quad \mathrm {Pr} >0.6$

The average Nusselt number for laminar flow over an isothermal flat plate, from the edge of the plate to a downstream distance L , is given by

${\overline {\mathrm {Nu} }}_{L}\ ={2}\cdot 0.332\,\mathrm {Re} _{L}^{1/2}\,\mathrm {Pr} ^{1/3}\ =0.664\,\mathrm {Re} _{L}^{1/2}\,\mathrm {Pr} ^{1/3},\quad \mathrm {Pr} >0.6$

### Sphere in forced flow

For a sphere in forced flow, such as an evaporating droplet, Faeth suggests:

$\mathrm {Nu} _{D}\ ={2}+{\frac {0.555\,\mathrm {Re} _{D}^{1/2}\,\mathrm {Pr} ^{1/3}}{\left(1+1.232/(\mathrm {Re} \mathrm {Pr} ^{4/3})\right)^{1/2}}},\quad \mathrm {Re} _{D}<1800$

The result limits to $\mathrm {Nu} _{D}\ ={2}$ for small Reynolds numbers, which corresponds to heat conduction into a sphere in an infinite medium.

### Forced convection in turbulent pipe flow

#### Gnielinski correlation

Gnielinski's correlation (1975) for flow in smooth tubes is:

$\mathrm {Nu} _{D}={\frac {\left(f/8\right)\left(\mathrm {Re} _{D}-1000\right)\mathrm {Pr} }{1+12.7(f/8)^{1/2}\left(\mathrm {Pr} ^{2/3}-1\right)}}$

where f is the Darcy friction factor that can either be obtained from the Moody chart or from the correlation of Filonenko:

$f=\left(0.79\ln \left(\mathrm {Re} _{D}\right)-1.64\right)^{-2}$

The Gnielinski correlation is valid for:

$0.5\leq \mathrm {Pr} \leq 2000$

$3000\leq \mathrm {Re} _{D}\leq 5\times 10^{6}$

This correlation is much more accurate than 1930s power-law correlations such as the Dittus–Boelter equation.

#### Gnielinski's simplified correlations

Gnielinski also developed power-law correlations for limited ranges of Prandtl number, which agree very closely with his full-range correlation. These equations are simpler to use, while remaining accurate:

${\begin{aligned}{\textrm {Nu}}_{D}&=0.0214\left({\textrm {Re}}_{D}^{0.8}-100\right){\textrm {Pr}}^{0.4}&\quad &{\textrm {for}}\quad 0.6\leq {\textrm {Pr}}\leq 1.5\\{\textrm {Nu}}_{D}&=0.012\left({\textrm {Re}}_{D}^{0.87}-280\right){\textrm {Pr}}^{0.4}&\quad &{\textrm {for}}\quad 1.5\leq {\textrm {Pr}}\leq 500\end{aligned}}$

These equations apply for smooth tubes with $3000\leq \mathrm {Re} _{D}\leq 5\times 10^{6}$ .

#### Dittus–Boelter equation

The Dittus–Boelter equation (for turbulent flow in smooth-walled tubes), as introduced by W.H. McAdams, is one of several power-law correlations that were published in the 1930s. These equations are based on smaller data sets than the Gnielinski correlations, represent smaller ranges of Reynolds and Prandtl number, and are generally less accurate. The Dittus–Boelter equation is:

$\mathrm {Nu} _{D}=0.023\,\mathrm {Re} _{D}^{4/5}\,\mathrm {Pr} ^{n}$

where:

D

is the inside diameter of the circular duct

$\mathrm {Pr}$

is the

Prandtl number

$n=0.4$

for the fluid being heated, and

$n=0.3$

for the fluid being cooled.

The Dittus–Boelter equation is valid for

$0.6\leq \mathrm {Pr} \leq 160$

$\mathrm {Re} _{D}\gtrsim 10\,000$

${\frac {L}{D}}\gtrsim 10$

#### Sieder–Tate correlation

The Sieder–Tate correlation for turbulent pipe flow (1936) takes account of the change in viscosity ( $\mu _{b}$ and $\mu _{w}$ ) due to temperature change between the average bulk temperature of the fluid and wall temperature. The Sieder–Tate correlation may need to be solved iteratively if the bulk or wall temperature is unknown.

$\mathrm {Nu} _{D}=0.027\,\mathrm {Re} _{D}^{4/5}\,\mathrm {Pr} ^{1/3}\left({\frac {\mu _{b}}{\mu _{w}}}\right)^{0.14}$

where:

$\mu _{b}$

is the fluid viscosity at the bulk fluid temperature

$\mu _{w}$

is the fluid viscosity at tube wall

The Sieder–Tate correlation is valid for

$0.7\leq \mathrm {Pr} \leq 16\,700$

$\mathrm {Re} _{D}\geq 10\,000$

${\frac {L}{D}}\gtrsim 10$

Taking water with a bulk fluid average temperature of 20 °C (68 °F), viscosity 10.07×10−4 Pa.s and a heat transfer surface temperature of 40 °C (104 °F) (viscosity 6.96×10−4 Pa.s, a viscosity correction factor for $({\mu }/{\mu _{s}})$ can be obtained as 1.45. This increases to 3.57 with a heat transfer surface temperature of 100 °C (212 °F) (viscosity 2.82×10−4 Pa.s), making a significant difference to the Nusselt number and the heat transfer coefficient.

### Forced convection in fully developed laminar flow in a tube

Solution of the governing equations for fully developed, laminar pipe flow leads to very simple results. The Nusselt numbers tend towards a constant value for long tubes:

$\mathrm {Nu} ={\frac {hD_{h}}{k}}$

where:

D

h

=

hydraulic diameter

k

=

thermal conductivity

of the fluid

h

=

convective

heat transfer coefficient

#### Convection with uniform wall temperature for circular tubes

From Incropera & DeWitt,

$\mathrm {Nu} _{D}=3.66$

OEIS sequence A282581 gives this value as $\mathrm {Nu} _{D}=3.6567934577632923619...$ .

#### Convection with uniform wall heat flux for circular tubes

For the case of constant surface heat flux,

$\mathrm {Nu} _{D}=4.36$
