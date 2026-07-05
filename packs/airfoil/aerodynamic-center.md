---
title: "Aerodynamic center"
source: https://en.wikipedia.org/wiki/Aerodynamic_center
domain: airfoil
license: CC-BY-SA-4.0
tags: airfoil
fetched: 2026-07-05
---

# Aerodynamic center

In aerodynamics, the torques or moments acting on an airfoil moving through a fluid can be accounted for by the net lift and net drag applied at some point on the airfoil, and a separate net pitching moment about that point whose magnitude varies with the choice of where the lift is chosen to be applied. The **aerodynamic center** is the point at which the pitching moment coefficient for the airfoil does not vary with lift coefficient (i.e. angle of attack), making analysis simpler.

${dC_{m} \over dC_{L}}=0$

where

$C_{L}$

is the aircraft

lift coefficient

.

The lift and drag forces can be applied at a single point, the center of pressure. However, the location of the center of pressure moves significantly with a change in angle of attack and is thus impractical for aerodynamic analysis. Instead the aerodynamic center is used and as a result the incremental lift and drag due to change in angle of attack acting at this point is sufficient to describe the aerodynamic forces acting on the given body.

## Theory

Within the assumptions embodied in thin airfoil theory, the aerodynamic center is located at the quarter-chord (25% chord position) on a symmetric airfoil while it is close but not exactly equal to the quarter-chord point on a cambered airfoil.

From thin airfoil theory:

$\ c_{l}=2\pi \alpha$

where

$c_{l}\!$

is the section lift coefficient,

$\alpha \!$

is the

angle of attack

in radian, measured relative to the

chord

line.

$\ {dc_{m,c/4} \over d\alpha }=m_{0}$

where

$\ c_{m,c/4}$

is the moment taken at quarter-chord point and

$\ m_{0}$

is a constant.

$\ M_{ac}=L(cx_{ac}-c/4)+M_{c/4}$

$\ c_{m,ac}=c_{l}(x_{ac}-0.25)+c_{m,c/4}$

Differentiating with respect to angle of attack

$\ x_{ac}={-m_{0} \over {2\pi }}+0.25$

For symmetrical airfoils $\ m_{0}=0$ , so the aerodynamic center is at 25% of chord measured from the leading edge. But for cambered airfoils the aerodynamic center can be slightly less than 25% of the chord from the leading edge, which depends on the slope of the moment coefficient, $\ m_{0}$ . These results obtained are calculated using the thin airfoil theory so the use of the results are warranted only when the assumptions of thin airfoil theory are realistic. In precision experimentation with real airfoils and advanced analysis, the aerodynamic center is observed to change location slightly as angle of attack varies. In most literature however the aerodynamic center is assumed to be fixed at the 25% chord position.

## Role of aerodynamic center in aircraft stability

For longitudinal static stability:

${\frac {dC_{m}}{d\alpha }}<0\quad {\text{and}}\quad {\frac {dC_{z}}{d\alpha }}>0$

For directional static stability:

${\frac {dC_{n}}{d\beta }}>0\quad {\text{and}}\quad {\frac {dC_{y}}{d\beta }}<0$

Where:

- $C_{z}=C_{L}\cos(\alpha )+C_{d}\sin(\alpha )$
- $C_{x}=C_{L}\sin(\alpha )-C_{d}\cos(\alpha )$

For a force acting away from the aerodynamic center, which is away from the reference point:

$X_{AC}=X_{\mathrm {ref} }+c{dC_{m} \over dC_{z}}$

Which for small angles cos(α) = 1 and sin(α) = α, β = 0, $C_{z}=C_{L}-C_{d}*\alpha ,$ $C_{z}=C_{L}$ simplifies to:

${\begin{aligned}&X_{AC}=X_{\mathrm {ref} }+c{dC_{m} \over dC_{L}}\\&Y_{AC}=Y_{\mathrm {ref} }\\&Z_{AC}=Z_{\mathrm {ref} }\end{aligned}}$

General Case: From the definition of the AC it follows that

${\begin{aligned}&X_{AC}=X_{\mathrm {ref} }+c{dC_{m} \over dC_{z}}+c{dC_{n} \over dC_{y}}\\&Y_{AC}=Y_{\mathrm {ref} }+c{dC_{l} \over dC_{z}}+c{dC_{n} \over dC_{x}}\\&Z_{AC}=Z_{\mathrm {ref} }+c{dC_{l} \over dC_{y}}+c{dC_{m} \over dC_{x}}\end{aligned}}$

The Static Margin can then be used to quantify the AC:

$SM={X_{AC}-X_{CG} \over c}$

where:

- Cn = yawing moment coefficient
- Cm = pitching moment coefficient
- Cl = rolling moment coefficient
- Cx = X-force ≈ Drag
- Cy = Y-force ≈ Side Force
- Cz = Z-force ≈ Lift
- ref = reference point (about which moments were taken)
- c = reference length
- S = reference area
- q = dynamic pressure
- α = angle of attack
- β = sideslip angle
- SM = Static Margin
