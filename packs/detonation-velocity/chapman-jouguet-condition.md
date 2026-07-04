---
title: "Chapman–Jouguet condition"
source: https://en.wikipedia.org/wiki/Chapman%E2%80%93Jouguet_condition
domain: detonation-velocity
license: CC-BY-SA-4.0
tags: detonation velocity
fetched: 2026-07-04
---

# Chapman–Jouguet condition

The **Chapman–Jouguet condition** holds approximately in detonation waves in high explosives. It states that the detonation propagates at a velocity at which the reacting gases just reach sonic velocity (in the frame of the leading shock wave) as the reaction ceases.

David Chapman and Émile Jouguet originally (c. 1900) stated the condition for an infinitesimally thin detonation. A physical interpretation of the condition is usually based on the later modelling (c. 1943) by Yakov Borisovich Zel'dovich, John von Neumann, and Werner Döring (the so-called ZND detonation model).

In more detail (in the ZND model) in the frame of the leading shock of the detonation wave, gases enter at supersonic velocity and are compressed through the shock to a high-density, subsonic flow. This sudden change in pressure initiates the chemical (or sometimes, as in steam explosions, physical) energy release. The energy release re-accelerates the flow back to the local speed of sound. It can be shown fairly simply, from the one-dimensional gas equations for steady flow, that the reaction must cease at the sonic ("CJ") plane, or there would be discontinuously large pressure gradients at that point.

The sonic plane forms a so-called choke point that enables the lead shock, and reaction zone, to travel at a constant velocity, undisturbed by the expansion of gases in the rarefaction region beyond the CJ plane.

This simple one-dimensional model is quite successful in explaining detonations. However, observations of the structure of real chemical detonations show a complex three-dimensional structure, with parts of the wave traveling faster than average, and others slower. Indeed, such waves are quenched as their structure is destroyed. The Wood–Kirkwood detonation theory can correct for some of these limitations.

## Mathematical description

Source:

The **Rayleigh line** equation and the **Hugoniot curve** equation obtained from the Rankine–Hugoniot relations for an ideal gas, with the assumption of constant specific heat and constant molecular weight, respectively are

${\begin{aligned}{\frac {{\tilde {p}}-1}{{\tilde {v}}-1}}&=-\mu \\{\tilde {p}}&={\frac {[2\alpha +(\gamma +1)/(\gamma -1)]-{\tilde {v}}}{[(\gamma +1)/(\gamma -1)]{\tilde {v}}-1}},\end{aligned}}$

where $\gamma$ is the specific heat ratio and

${\tilde {p}}={\frac {p_{2}}{p_{1}}},\quad {\tilde {v}}={\frac {\rho _{1}}{\rho _{2}}},\quad \alpha ={\frac {q\rho _{1}}{p_{1}}},\quad \mu ={\frac {m^{2}}{p_{1}\rho _{1}}}.$

Here the subscript 1 and 2 identifies flow properties (pressure p , density $\rho$ ) upstream and downstream of the wave and m is the constant mass flux and q is the heat released in the wave. The slopes of Rayleigh line and Hugoniot curve are

${\begin{aligned}{\frac {d{\tilde {p}}}{d{\tilde {v}}}}&={\frac {{\tilde {p}}-1}{{\tilde {v}}-1}},\\[3pt]{\frac {d{\tilde {p}}}{d{\tilde {v}}}}&=-{\frac {[(\gamma +1)/(\gamma -1)]{\tilde {p}}+1}{[(\gamma +1)/(\gamma -1)]{\tilde {v}}-1}}.\end{aligned}}$

⋅

At the Chapman-Jouguet point, both slopes are equal, leading the condition that

${\tilde {p}}={\frac {\tilde {v}}{(\gamma +1){\tilde {v}}-\gamma }}.$

Substituting this back into the Rayleigh equation, we find

$\mu =\gamma {\frac {\tilde {p}}{\tilde {v}}}.$

Using the definition of mass flux $m\equiv \rho _{1}u_{1}=\rho _{2}u_{2}$ , where u denotes the flow velocity, we find

$M_{2}={\frac {u_{2}}{c_{2}}}=1$

where M is the Mach number and c is the speed of sound, in other words, downstream flow is sonic with respect to the Chapman-Jouguet wave. Explicit expression for the variables can be derived,

${\begin{aligned}{\tilde {p}}_{\pm }&=1+\alpha (\gamma -1)\left\{1\pm \left[1+{\frac {2\gamma }{\alpha \left(\gamma ^{2}-1\right)}}\right]^{\frac {1}{2}}\right\},\\{\tilde {v}}_{\pm }&=1+{\frac {\alpha \left(\gamma -1\right)}{\gamma }}\left\{1\mp \left[1+{\frac {2\gamma }{\alpha \left(\gamma ^{2}-1\right)}}\right]^{\frac {1}{2}}\right\},\\\mu _{\pm }&=\gamma +\alpha (\gamma ^{2}-1)\left\{1\pm \left[1+{\frac {2\gamma }{\alpha \left(\gamma ^{2}-1\right)}}\right]^{\frac {1}{2}}\right\}.\end{aligned}}$

The upper sign applies for the **Upper Chapman-Jouguet** point (detonation) and the lower sign applies for the **Lower Chapman-Jouguet** point (deflagration). Similarly, the upstream Mach number can be found from

$M_{1\pm }=\left[1+{\frac {\alpha \left(\gamma ^{2}-1\right)}{2\gamma }}\right]^{\frac {1}{2}}\pm \left[{\frac {\alpha \left(\gamma ^{2}-1\right)}{2\gamma }}\right]^{\frac {1}{2}}$

and the temperature ratio ${\tilde {T}}=T_{2}/T_{1}$ can be found from the relation ${\tilde {T}}={\tilde {p}}{\tilde {v}}$ .
