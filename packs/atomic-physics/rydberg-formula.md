---
title: "Rydberg formula"
source: https://en.wikipedia.org/wiki/Rydberg_formula
domain: atomic-physics
license: CC-BY-SA-4.0
tags: atomic physics, atomic orbital, fine structure, zeeman effect
fetched: 2026-07-02
---

# Rydberg formula

In atomic physics, the **Rydberg formula** calculates the wavelengths of a spectral line in many chemical elements. The formula was primarily presented as a generalization of the Balmer series for all atomic electron transitions of hydrogen. It was first empirically stated in 1888 by the Swedish physicist Johannes Rydberg, then theoretically by Niels Bohr in 1913, who used a primitive form of quantum mechanics. The formula directly generalizes the equations used to calculate the wavelengths of the hydrogen spectral series.

## History

In 1890, Rydberg proposed on a formula describing the relation between the wavelengths in spectral lines of alkali metals. He noticed that lines came in series and he found that he could simplify his calculations by specifying the lines in terms of their wavenumber (the number of waves occupying the unit length, equal to 1/*λ*, the inverse of the wavelength) rather than their wavelength. He plotted the wavenumbers (*n*) of successive lines in each series against consecutive integers which represented the order of the lines in that particular series. Finding that the resulting curves were similarly shaped, he sought a single function which could generate all of them, when appropriate constants were inserted.

First he tried the formula: $\textstyle n=n_{0}-{\frac {C_{0}}{m+m'}}$ , where *n* is the line's wavenumber, *n*0 is the series limit, *m* is the line's ordinal number in the series, *m*′ is a constant different for different series and *C*0 is a universal constant. This did not work very well.

Rydberg was trying: $\textstyle n=n_{0}-{\frac {C_{0}}{\left(m+m'\right)^{2}}}$ when he became aware of Balmer's formula for the hydrogen spectrum $\textstyle \lambda ={hm^{2} \over m^{2}-4}$ In this equation, *m* is an integer and *h* is a constant (not to be confused with the later Planck constant).

Rydberg therefore rewrote Balmer's formula in terms of wavenumbers, as $\textstyle n=n_{0}-{4n_{0} \over m^{2}}$ .

This suggested that the Balmer formula for hydrogen might be a special case with $\textstyle m'=0$ and ${\text{C}}_{0}=4n_{0}$ , where $\textstyle n_{0}={\frac {1}{h}}$ , the reciprocal of Balmer's constant (this constant **h** is written **B** in the Balmer equation article, again to avoid confusion with the Planck constant).

The term ${\text{C}}_{0}$ was found to be a universal constant common to all elements, equal to 4/*h*. This constant is now known as the Rydberg constant, and *m*′ is known as the quantum defect.

As stressed by Niels Bohr, expressing results in terms of wavenumber, not wavelength, was the key to Rydberg's discovery. The fundamental role of wavenumbers was also emphasized by the Rydberg-Ritz combination principle of 1908. The fundamental reason for this lies in quantum mechanics. Light's wavenumber is proportional to frequency $\textstyle {\frac {1}{\lambda }}={\frac {f}{c}}$ , and therefore also proportional to light's quantum energy *E*. Thus, $\textstyle {\frac {1}{\lambda }}={\frac {E}{hc}}$ (in this formula the *h* represents the Planck constant). Modern and legitimate understanding is that Rydberg's findings were a reflection of the underlying simplicity of the behavior of spectral lines, in terms of fixed (quantized) *energy* differences between electron orbitals in atoms. Rydberg's 1888 classical expression for the form of the spectral series was not accompanied by a physical explanation. Walther Ritz's *pre-quantum* 1908 explanation for the *mechanism* underlying the spectral series was that atomic electrons behaved like magnets and that the magnets could vibrate with respect to the atomic nucleus (at least temporarily) to produce electromagnetic radiation, but this theory was superseded in 1913 by Niels Bohr's model of the atom.

### Bohr's interpretation and derivation of the constant

Rydberg's published formula was $\pm {\frac {n}{N_{0}}}={\frac {1}{(m_{1}+\mu _{1})^{2}}}-{\frac {1}{(m_{2}+\mu _{2})^{2}}}$ where n is the observed wavenumber, $N_{0}$ is a constant for all spectral series and elements, and the remaining values, $m_{1},\mu _{1},m_{2},\mu _{2}$ are integers indexing the various lines. When Bohr analyzes his model for the atom he writes $\nu ={\frac {2\pi ^{2}me^{4}}{h^{3}}}\left({\frac {1}{\tau _{2}^{2}}}-{\frac {1}{\tau _{1}^{2}}}\right)$ where he uses frequency $\nu$ (proportional to wavenumber). Thus he has been able to compute the value of Rydberg's heuristic constant $N_{0}$ from his atom theory and set the integers $\mu _{1}$ and $\mu _{2}$ to zero. The effect is to predict new series corresponding to $\tau _{2}=1$ in the extreme ultraviolet unknown to Rydberg.

In Bohr's conception of the atom, the integer Rydberg (and Balmer) *n* numbers represent electron orbitals at different integral distances from the atom. A frequency (or spectral energy) emitted in a transition from *n*1 to *n*2 therefore represents the photon energy emitted or absorbed when an electron makes a jump from orbital 1 to orbital 2.

Later models found that the values for *n*1 and *n*2 corresponded to the principal quantum numbers of the two orbitals.

The Rydberg formula can be interpreted both through the semi-classical Bohr model and through fully quantum-mechanical treatments of the hydrogen atom. In the Bohr model, electrons occupy quantized orbits whose energies vary. When an electron transitions from a higher level to a lower level a photon is emitted with a wavelength matching the Rydberg expression. Modern quantum mechanics arrives at the same result from the Schrödinger equation for an electron bound by a Coulomb potential. Differences in the energy eigenvalues of the hydrogen atom reproduce the observed Rydberg dependence, while relativistic and spin corrections appear when the Dirac equation, fine-structure interactions, and quantum electrodynamics (QED) effects are included. These refinements explain small deviations from the simple formula, such as the Lamb shift and hyperfine splittings in hydrogen-like systems.

## For hydrogen

For hydrogen, the energy of the atomic electron transition is given by ${\frac {1}{\lambda _{\mathrm {vac} }}}=R_{\text{H}}\left({\frac {1}{n_{1}^{2}}}-{\frac {1}{n_{2}^{2}}}\right),$ where

- $\lambda _{\mathrm {vac} }$ is the wavelength of electromagnetic radiation emitted in vacuum,
- $R_{\text{H}}$ is the Rydberg constant for hydrogen, approximately 1.09677583×107 m−1,
- $n_{1}$ , $n_{2}$ are principal quantum numbers for energy levels, with $n_{2}>n_{1}$ .

By setting $n_{1}$ to 1 and letting $n_{2}$ run from 2 to infinity, the spectral lines known as the Lyman series converging to 91 nm are obtained. Other named series correspond to increasingly higher values of $n_{1}$ .

| n1 | n2 | Name | Converge toward |
|---|---|---|---|
| 1 | 2 – ∞ | Lyman series | 91.13 nm (ultraviolet) |
| 2 | 3 – ∞ | Balmer series | 364.51 nm (visible) |
| 3 | 4 – ∞ | Paschen series | 820.14 nm (infrared) |
| 4 | 5 – ∞ | Brackett series | 1458.03 nm (infrared) |
| 5 | 6 – ∞ | Pfund series | 2278.17 nm (infrared) |
| 6 | 7 – ∞ | Humphreys series | 3280.56 nm (infrared) |

## For any hydrogen-like element

The formula above can be extended for use with any hydrogen-like chemical elements with ${\frac {1}{\lambda }}=RZ^{2}\left({\frac {1}{n_{1}^{2}}}-{\frac {1}{n_{2}^{2}}}\right),$ where

- $\lambda$ is the wavelength (in vacuum) of the light emitted,
- R is the Rydberg constant for this element,
- Z is the atomic number, i.e. the number of protons in the atomic nucleus of this element,
- $n_{1}$ is the principal quantum number of the lower energy level, and
- $n_{2}$ is the principal quantum number of the higher energy level for the atomic electron transition.

This formula can be directly applied only to hydrogen-like, also called *hydrogenic* atoms of chemical elements, i.e. atoms with only one electron being affected by an effective nuclear charge (which is easily estimated). Examples would include He+, Li2+, Be3+ etc., where no other electrons exist in the atom.

But the Rydberg formula also provides correct wavelengths for distant electrons, where the effective nuclear charge can be estimated as the same as that for hydrogen, since all but one of the nuclear charges have been screened by other electrons, and the core of the atom has an effective positive charge of +1.

Finally, with certain modifications (replacement of *Z* by *Z* − 1, and use of the integers 1 and 2 for the *n*s to give a numerical value of 3⁄4 for the difference of their inverse squares), the Rydberg formula provides correct values in the special case of K-alpha lines, since the transition in question is the K-alpha transition of the electron from the 1s orbital to the 2p orbital. This is analogous to the Lyman-alpha line transition for hydrogen, and has the same frequency factor. Because the 2p electron is not screened by any other electrons in the atom from the nucleus, the nuclear charge is diminished only by the single remaining 1s electron, causing the system to be effectively a hydrogenic atom, but with a diminished nuclear charge *Z* − 1. Its frequency is thus the Lyman-alpha hydrogen frequency, increased by a factor of (*Z* − 1)2. This formula of *f* = *c* / *λ* = (Lyman-alpha frequency) ⋅ (*Z* − 1)2 is historically known as Moseley's law (having added a factor *c* to convert wavelength to frequency), and can be used to predict wavelengths of the Kα (K-alpha) X-ray spectral emission lines of chemical elements from aluminum to gold. See the biography of Henry Moseley for the historical importance of this law, which was derived empirically at about the same time it was explained by the Bohr model of the atom.

For other spectral transitions in multi-electron atoms, the Rydberg formula generally provides *incorrect* results, since the magnitude of the screening of inner electrons for outer-electron transitions is variable and cannot be compensated for in the simple manner above. The correction to the Rydberg formula for these atoms is known as the quantum defect.

## Reduced mass and precision corrections

The classical Rydberg formula assumes an infinitely massive nucleus; however, in real atoms the nucleus has finite mass. In the Bohr model the electron and nucleus should orbit their mutual center of mass. In quantum mechanical calculations this leads to the introduction of a reduced mass, producing a slightly modified Rydberg constant that varies depending on the isotope. Additional corrections arise from relativistic motion of the electron, vacuum polarization, self-energy contributions, and other QED effects, all of which are essential in high-precision spectroscopy. These corrections become especially important for high-Z hydrogen-like ions, where relativistic velocities and strong Coulomb fields generate observable deviations from the nonrelativistic prediction.
