---
title: "Lee–Kesler method"
source: https://en.wikipedia.org/wiki/Lee%E2%80%93Kesler_method
domain: tetens-equation
license: CC-BY-SA-4.0
tags: tetens equation
fetched: 2026-07-04
---

# Lee–Kesler method

The **Lee–Kesler method** allows the estimation of the saturated vapor pressure at a given temperature for all components for which the critical pressure *P*c, the critical temperature *T*c, and the acentric factor *ω* are known.

## Equations

$\ln P_{\rm {r}}=f^{(0)}+\omega \cdot f^{(1)}$

$f^{(0)}=5.92714-{\frac {6.09648}{T_{\rm {r}}}}-1.28862\cdot \ln T_{\rm {r}}+0.169347\cdot T_{\rm {r}}^{6}$

$f^{(1)}=15.2518-{\frac {15.6875}{T_{\rm {r}}}}-13.4721\cdot \ln T_{\rm {r}}+0.43577\cdot T_{\rm {r}}^{6}$

with

$P_{\rm {r}}={\frac {P}{P_{\rm {c}}}}$

(

reduced pressure

) and

$T_{\rm {r}}={\frac {T}{T_{\rm {c}}}}$

(

reduced temperature

).

## Typical errors

The prediction error can be up to 10% for polar components and small pressures and the calculated pressure is typically too low. For pressures above 1 bar, that means, above the normal boiling point, the typical errors are below 2%.

## Example calculation

For benzene with

- *T*c = 562.12 K
- *P*c = 4898 kPa
- *T*boiling = 353.15 K
- *ω* = 0.2120

the following calculation for *T* = *T*b results:

- *T**r* = 353.15 / 562.12 = 0.628247
- *f*(0) = −3.167428
- *f*(1) = −3.429560
- *P*r = exp( *f*(0) + *ω* *f*(1) ) = 0.020354
- *P* = *P*r · *P*c = 99.69 kPa

The correct result would be *P* = 101.325 kPa, the normal (atmospheric) pressure. The deviation is −1.63 kPa or −1.61 %.

It is important to use the same absolute units for *T* and *T*c as well as for *P* and *P*c. The unit system used (K or R for *T*) is irrelevant because of the usage of the reduced values *T*r and *P*r.
