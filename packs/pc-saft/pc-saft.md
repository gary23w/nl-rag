---
title: "PC-SAFT"
source: https://en.wikipedia.org/wiki/PC-SAFT
domain: pc-saft
license: CC-BY-SA-4.0
tags: pc-saft
fetched: 2026-07-04
---

# PC-SAFT

**PC-SAFT** (perturbed chain SAFT) is an equation of state that is based on statistical associating fluid theory (SAFT). Like other SAFT equations of state, it makes use of chain and association terms developed by Chapman, et al from perturbation theory. However, unlike earlier SAFT equations of state that used unbonded spherical particles as a reference fluid, it uses spherical particles in the context of hard chains as reference fluid for the dispersion term.

PC-SAFT was developed by Joachim Gross and Gabriele Sadowski, and was first presented in their 2001 article. Further research extended PC-SAFT for use with associating and polar molecules, and it has also been modified for use with polymers. A version of PC-SAFT has also been developed to describe mixtures with ionic compounds (called electrolyte PC-SAFT or ePC-SAFT).

## Form of the Equation of State

The equation of state is organized into terms that account for different types of intermolecular interactions, including terms for

- the hard chain reference
- dispersion
- association
- polar interactions
- ions

The equation is most often expressed in terms of the residual Helmholtz energy because all other thermodynamic properties can be easily found by taking the appropriate derivatives of the Helmholtz energy.

$a=a^{\text{hc}}+a^{\text{disp}}+a^{\text{assoc}}+a^{\text{dipole}}+a^{\text{ion}}$

Here a is the molar residual Helmholtz energy.

### Hard Chain Term

${\frac {a^{\text{hc}}}{kT}}={\overline {m}}\cdot a^{\text{hs}}-\sum _{i=1}^{NC}{x_{i}\cdot (m_{i}-1)\cdot \ln(g_{i,i}^{\text{hs}})}$

where

- $NC$ is the number of compounds;
- $x_{i}$ is the mole fraction;
- ${\overline {m}}=\sum _{i=1}^{NC}{x_{i}m_{i}}$ is the average number of segments in the mixture;
- $a^{\text{hs}}$ is the Boublík-Mansoori-Leeland-Carnahan-Starling *hard sphere* equation of state, defined as:

$a^{\text{hs}}=\zeta _{0}\left({\frac {3\zeta _{1}\zeta _{2}}{1-\zeta _{3}}}+{\frac {\zeta _{2}^{3}}{\zeta _{3}(1-\zeta _{3})^{2}}}+{\frac {\zeta _{2}^{3}}{\zeta _{3}^{2}-\zeta _{0}}}\log {(1-\zeta _{3})}\right)$

$\zeta _{k}=\sum _{i}{x_{i}m_{i}d_{i}^{k}}$

$d_{i}=\sigma _{i}\left(1-0.12\exp {\left({\frac {-3\epsilon _{i}}{kT}}\right)}\right)$ , where k is the Boltzmann constant. $g_{i,i}^{\text{hs}}$ is the *hard sphere* radial distribution function at contact.: $g_{i,j}^{\text{hs}}={\frac {1}{1-\zeta _{3}}}+{\frac {3\zeta _{2}}{(1-\zeta _{3})^{2}}}\left({\frac {d_{i}d_{j}}{d_{i}+d_{j}}}\right)+{\frac {2\zeta _{2}^{2}}{(1-\zeta _{3})^{3}}}\left({\frac {d_{i}d_{j}}{d_{i}+d_{j}}}\right)^{2}$

### Dispersion Term

$a^{\text{disp}}=-2\pi \mathbb {N} _{A}\rho I_{1}{\overline {m^{2}\epsilon \sigma ^{3}}}-{\overline {m}}\mathbb {N} _{A}\rho I_{1}{\overline {m^{2}\epsilon ^{2}\sigma ^{3}}}$

${\overline {m^{2}\epsilon \sigma ^{3}}}=\sum _{i}\sum _{j}{x_{i}x_{j}m_{i}m_{j}{\frac {\epsilon _{ij}}{kT}}\sigma _{ij}^{3}}$

${\overline {m^{2}\epsilon ^{2}\sigma ^{3}}}=\sum _{i}\sum _{j}{x_{i}x_{j}m_{i}m_{j}\left({\frac {\epsilon _{ij}}{kT}}\right)^{2}\sigma _{ij}^{3}}$

Where $N_{A}$ is the Avogadro constant, $\rho$ is the molar density, and $I_{1}$ , $I_{2}$ are the analytical functions representing the integrals of the radial distribution function in 1st and 2nd order perturbation terms:

$I_{1}=\sum _{i=0}^{i=6}{\left(a_{0i}+{\frac {{\overline {m}}-1}{\overline {m}}}a_{1i}+{\frac {{\overline {m}}-1}{\overline {m}}}{\frac {{\overline {m}}-2}{\overline {m}}}a_{2i}\right)\zeta _{3}^{i}}$

$I_{2}=\sum _{i=0}^{i=6}{\left(b_{0i}+{\frac {{\overline {m}}-1}{\overline {m}}}b_{1i}+{\frac {{\overline {m}}-1}{\overline {m}}}{\frac {{\overline {m}}-2}{\overline {m}}}b_{2i}\right)\zeta _{3}^{i}}$

$b_{ji}$ , $a_{ji}$ are universal model parameters:

|   | $a_{0i}$ | $a_{1i}$ | $a_{2i}$ | $b_{0i}$ | $b_{1i}$ | $b_{2i}$ |
|---|---|---|---|---|---|---|
| 0 | 0.9105631445 | -0.3084016918 | -0.0906148351 | 0.7240946941 | -0.5755498075 | 0.0976883116 |
| 1 | 0.6361281449 | 0.1860531159 | 0.4527842806 | 2.2382791861 | 0.6995095521 | -0.2557574982 |
| 2 | 2.6861347891 | -2.5030047259 | 0.5962700728 | -4.0025849485 | 3.8925673390 | -9.1558561530 |
| 3 | -26.547362491, | 21.419793629 | -1.7241829131 | -21.003576815 | -17.215471648 | 20.642075974 |
| 4 | 97.759208784 | -65.255885330 | -4.1302112531 | 26.855641363 | 192.67226447 | -38.804430052 |
| 5 | -159.59154087 | 83.318680481 | 13.776631870 | 206.55133841 | -161.82646165 | 93.626774077 |
| 6 | 91.297774084 | -33.746922930 | -8.6728470368 | -355.60235612 | -165.20769346 | -29.666905585 |

To obtain $\epsilon _{ij}$ and $\sigma _{ij}$ , the following mixing rules are used:

$\epsilon _{ij}=(1-k_{ij}){\sqrt {\epsilon _{i}\epsilon _{j}}}$

$\sigma _{ij}=(1-l_{ij}){\frac {\sigma _{i}+\sigma _{j}}{2}}$

Were $k_{ij}$ and $l_{ij}$ interaction parameters, obtaining via fitting binary mixture data.

### Association Term

$a^{\text{assoc}}=\sum _{i=1}^{n_{c}}{x_{i}\sum _{a=1}^{n_{s}}{n_{i,a}\left(\log {X_{i,a}}-{\frac {X_{i,a}}{2}}+{\frac {1}{2}}\right)}}$

Where $X_{i,a}$ is the fraction of non-bonded sites of type a in component i , and $n_{i,a}$ is the number of sites of type a in component i . $X_{i,a}$ is the solution of the following system of equations:

$X_{i,a}={\frac {1}{1+\sum _{j=1}^{n_{c}}{\sum _{b=1}^{n_{s}}{\rho x_{j}n_{j,b}X_{j,b}\Delta _{ij,ab}}}}}$

Where $\Delta _{ij,ab}$ is the association strength between sites of type a in component i , and sites of type b in component j . In the specific case of PC-SAFT, $\Delta _{ij,ab}$ is defined as:

$\Delta _{ij,ab}=g_{i,j}^{\text{hs}}\sigma _{ij}^{3}\kappa _{ij,ab}\exp {\left({\frac {\epsilon _{ij,ab}^{\text{HB}}}{kT}}-1\right)}$

Where $\epsilon _{ij,ab}^{\text{HB}}$ is the hydrogen bonding energy and $\kappa _{ij,ab}$ is the bonding volume, between sites of type a in component i , and sites of type b in component j .
