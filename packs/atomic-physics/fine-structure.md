---
title: "Fine structure"
source: https://en.wikipedia.org/wiki/Fine_structure
domain: atomic-physics
license: CC-BY-SA-4.0
tags: atomic physics, atomic orbital, fine structure, zeeman effect
fetched: 2026-07-02
---

# Fine structure

In atomic physics, the **fine structure** describes the splitting of the spectral lines of atoms due to electron spin and relativistic corrections to the non-relativistic Schrödinger equation. It was first measured precisely for the hydrogen atom by Albert A. Michelson and Edward W. Morley in 1887. The explanation was first given by Niels Bohr in 1914, who suggested that the orbits of electrons in his Bohr model of the atom precessed due to relativistic effects. A successful relativistic formula was given by Arnold Sommerfeld in 1916. In the same work, Sommerfeld also introduced the fine-structure constant.

## Background

### Gross structure

The *gross structure* of line spectra is the structure predicted by the quantum mechanics of non-relativistic electrons with no spin. For a hydrogenic atom, the gross structure energy levels only depend on the principal quantum number *n*. However, a more accurate model takes into account relativistic and spin effects, which break the degeneracy of the energy levels and split the spectral lines. The scale of the fine structure splitting relative to the gross structure energies is on the order of (*Zα*)2, where *Z* is the atomic number and *α* is the fine-structure constant, a dimensionless number equal to approximately 1/137.

### Relativistic corrections

The fine structure energy corrections can be obtained by using perturbation theory. To perform this calculation one must add three corrective terms to the Hamiltonian: the leading order relativistic correction to the kinetic energy, the correction due to the spin–orbit coupling, and the Darwin term coming from the quantum fluctuating motion or zitterbewegung of the electron.

These corrections can also be obtained from the non-relativistic limit of the Dirac equation, since Dirac's theory naturally incorporates relativity and spin interactions.

## Hydrogen atom

This section discusses the analytical solutions for the hydrogen atom as the problem is analytically solvable and is the base model for energy level calculations in more complex atoms.

### Kinetic energy relativistic correction

The gross structure assumes the kinetic energy term of the Hamiltonian takes the same form as in classical mechanics, which for a single electron means ${\mathcal {H}}^{0}={\frac {p^{2}}{2m_{\text{e}}}}+V$ where V is the potential energy, p is the momentum, and $m_{\text{e}}$ is the electron rest mass.

However, when considering a more accurate theory of nature via special relativity, we must use a relativistic form of the kinetic energy, $T={\sqrt {p^{2}c^{2}+{m_{\text{e}}}^{2}c^{4}}}-m_{\text{e}}c^{2}=m_{\text{e}}c^{2}\left[{\sqrt {1+{\frac {p^{2}}{{m_{\text{e}}}^{2}c^{2}}}}}-1\right]$ where the first term is the total relativistic energy, and the second term is the rest energy of the electron ( c is the speed of light). To further simplify, we note that the term under the square root can be written of the form $(1+x)^{p}$ where the value of x satisfies the conditions to approximate the entire square root term as the first two terms of its Taylor series expansion. Expanding the square root and simplifying yields, $T={\frac {p^{2}}{2m_{\text{e}}}}-{\frac {p^{4}}{8{m_{\text{e}}}^{3}c^{2}}}+\cdots$

Although there are an infinite number of terms in this series, the later terms are much smaller than earlier terms, and so we can ignore all but the first two. Since the first term above is already part of the classical Hamiltonian, the first order *correction* to the Hamiltonian is ${\mathcal {H}}'=-{\frac {p^{4}}{8{m_{\text{e}}}^{3}c^{2}}}$

Using this as a perturbation, we can calculate the first order energy corrections due to relativistic effects. $E_{n}^{(1)}=\left\langle \psi ^{0}\right\vert {\mathcal {H}}'\left\vert \psi ^{0}\right\rangle =-{\frac {1}{8{m_{\text{e}}}^{3}c^{2}}}\left\langle \psi ^{0}\right\vert p^{4}\left\vert \psi ^{0}\right\rangle =-{\frac {1}{8{m_{\text{e}}}^{3}c^{2}}}\left\langle \psi ^{0}\right\vert p^{2}p^{2}\left\vert \psi ^{0}\right\rangle$ where $\psi ^{0}$ is the unperturbed wave function. Recalling the unperturbed Hamiltonian, we see ${\begin{aligned}{\mathcal {H}}^{0}\left\vert \psi ^{0}\right\rangle &=E_{n}\left\vert \psi ^{0}\right\rangle \\\left({\frac {p^{2}}{2m_{\text{e}}}}+V\right)\left\vert \psi ^{0}\right\rangle &=E_{n}\left\vert \psi ^{0}\right\rangle \\p^{2}\left\vert \psi ^{0}\right\rangle &=2m_{\text{e}}(E_{n}-V)\left\vert \psi ^{0}\right\rangle \end{aligned}}$

We can use this result to further calculate the relativistic correction: ${\begin{aligned}E_{n}^{(1)}&=-{\frac {1}{8{m_{\text{e}}}^{3}c^{2}}}\left\langle \psi ^{0}\right\vert p^{2}p^{2}\left\vert \psi ^{0}\right\rangle \\[1ex]&=-{\frac {1}{8{m_{\text{e}}}^{3}c^{2}}}\left\langle \psi ^{0}\right\vert (2m_{\text{e}})^{2}(E_{n}-V)^{2}\left\vert \psi ^{0}\right\rangle \\[1ex]&=-{\frac {1}{2m_{\text{e}}c^{2}}}\left(E_{n}^{2}-2E_{n}\langle V\rangle +\left\langle V^{2}\right\rangle \right)\end{aligned}}$

For the hydrogen atom, $V(r)={\frac {-e^{2}}{4\pi \varepsilon _{0}r}},$ $\left\langle {\frac {1}{r}}\right\rangle ={\frac {1}{a_{0}n^{2}}},$ and $\left\langle {\frac {1}{r^{2}}}\right\rangle ={\frac {1}{(\ell +1/2)n^{3}a_{0}^{2}}},$ where e is the elementary charge, $\varepsilon _{0}$ is the vacuum permittivity, $a_{0}$ is the Bohr radius, n is the principal quantum number, $\ell$ is the azimuthal quantum number and r is the distance of the electron from the nucleus. Therefore, the first order relativistic correction for the hydrogen atom is ${\begin{aligned}E_{n}^{(1)}&=-{\frac {1}{2m_{\text{e}}c^{2}}}\left(E_{n}^{2}+2E_{n}{\frac {e^{2}}{4\pi \varepsilon _{0}}}{\frac {1}{a_{0}n^{2}}}+{\frac {1}{16\pi ^{2}\varepsilon _{0}^{2}}}{\frac {e^{4}}{\left(\ell +{\frac {1}{2}}\right)n^{3}a_{0}^{2}}}\right)\\&=-{\frac {E_{n}^{2}}{2m_{\text{e}}c^{2}}}\left({\frac {4n}{\ell +{\frac {1}{2}}}}-3\right)\end{aligned}}$ where we have used: $E_{n}=-{\frac {e^{2}}{8\pi \varepsilon _{0}a_{0}n^{2}}}$

On final calculation, the relativistic correction to the ground state is −9.056×10−4 eV. In general, $E_{n}^{(1)}=-1.81\times 10^{-4}\;\mathrm {eV} \times {\frac {1}{n^{4}}}\left({\frac {4n}{\ell +{\frac {1}{2}}}}-3\right).$

### Spin–orbit coupling

For a hydrogen-like atom with Z protons ( $Z=1$ for hydrogen), orbital angular momentum $\mathbf {L}$ and electron spin $\mathbf {S}$ , the spin–orbit term is given by: ${\mathcal {H}}_{\mathrm {SO} }=\left({\frac {Ze^{2}}{4\pi \varepsilon _{0}}}\right)\left({\frac {g_{s}-1}{2{m_{\text{e}}}^{2}c^{2}}}\right){\frac {\mathbf {L} \cdot \mathbf {S} }{r^{3}}}$ where $g_{s}$ is the spin g-factor.

The spin–orbit correction can be understood by shifting from the standard frame of reference (where the electron orbits the nucleus) into one where the electron is stationary and the nucleus instead orbits it. In this case the orbiting nucleus functions as an effective current loop, which in turn will generate a magnetic field. However, the electron itself has a magnetic moment due to its intrinsic angular momentum. The two magnetic vectors, $\mathbf {B}$ and ${\boldsymbol {\mu }}_{s}$ couple together so that there is a certain energy cost depending on their relative orientation. This gives rise to the energy correction of the form $\Delta E_{\mathrm {SO} }=\xi (r)\mathbf {L} \cdot \mathbf {S}$

Notice that an important factor of 2 has to be added to the calculation, called the Thomas precession, which comes from the relativistic calculation that changes back to the electron's frame from the nucleus frame.

Since $\left\langle {\frac {1}{r^{3}}}\right\rangle ={\frac {Z^{3}}{n^{3}a_{0}^{3}}}{\frac {1}{\ell \left(\ell +{\frac {1}{2}}\right)(\ell +1)}}$ by Kramers–Pasternack recursion relations (named after Hans Kramers and Simon Pasternack) and $\left\langle \mathbf {L} \cdot \mathbf {S} \right\rangle ={\frac {\hbar ^{2}}{2}}\left[j(j+1)-\ell (\ell +1)-s(s+1)\right]$ the expectation value for the Hamiltonian is: $\left\langle {\mathcal {H}}_{\mathrm {SO} }\right\rangle ={\frac {{E_{n}}^{2}}{m_{\text{e}}c^{2}}}~n~{\frac {j(j+1)-\ell (\ell +1)-{\frac {3}{4}}}{\ell \left(\ell +{\frac {1}{2}}\right)(\ell +1)}}$

Thus the order of magnitude for the spin–orbital coupling is: ${\frac {Z^{4}}{n^{3}\left(j+{\frac {1}{2}}\right)\left(j+1\right)}}\times 10^{-4}{\text{ eV}}$

When weak external magnetic fields are applied, the spin–orbit coupling contributes to the Zeeman effect.

### Darwin term

There is one last term in the non-relativistic expansion of the Dirac equation. It is referred to as the Darwin term, as it was first derived by Charles Galton Darwin, and is given by: ${\begin{aligned}{\mathcal {H}}_{\text{Darwin}}&={\frac {\hbar ^{2}}{8{m_{\text{e}}}^{2}c^{2}}}\,4\pi \left({\frac {Ze^{2}}{4\pi \varepsilon _{0}}}\right)\delta ^{3}{\left(\mathbf {r} \right)}\\\langle {\mathcal {H}}_{\text{Darwin}}\rangle &={\frac {\hbar ^{2}}{8{m_{\text{e}}}^{2}c^{2}}}\,4\pi \left({\frac {Ze^{2}}{4\pi \varepsilon _{0}}}\right)|\psi (0)|^{2}\\[3pt]\psi (0)&={\begin{cases}0&{\text{ for }}\ell >0\\{\frac {1}{\sqrt {4\pi }}}\,2\left({\frac {Z}{na_{0}}}\right)^{\frac {3}{2}}&{\text{ for }}\ell =0\end{cases}}\\[2pt]{\mathcal {H}}_{\text{Darwin}}&={\frac {2n}{m_{\text{e}}c^{2}}}\,E_{n}^{2}\end{aligned}}$

The Darwin term affects only the s orbitals. This is because the wave function of an electron with $\ell >0$ vanishes at the origin, hence the delta function has no effect. For example, it gives the 2s orbital the same energy as the 2p orbital by raising the 2s state by 9.057×10−5 eV.

The Darwin term changes potential energy of the electron. It can be interpreted as a smearing out of the electrostatic interaction between the electron and nucleus due to zitterbewegung, or rapid quantum oscillations, of the electron. This can be demonstrated by a short calculation.

Quantum fluctuations allow for the creation of virtual electron–positron pairs with a lifetime estimated by the uncertainty principle $\Delta t\approx \hbar /\Delta E\approx \hbar /mc^{2}$ . The distance the particles can move during this time is $\xi \approx c\Delta t\approx \hbar /mc=\lambda \!\!\!{\bar {}}_{\text{C}}$ , their reduced Compton wavelength. The electrons of the atom interact with those pairs. This yields a fluctuating electron position $\mathbf {r} +{\boldsymbol {\xi }}$ . Using a Taylor expansion, the effect on the potential U can be estimated: $U(\mathbf {r} +{\boldsymbol {\xi }})\approx U(\mathbf {r} )+\xi \cdot \nabla U(\mathbf {r} )+{\frac {1}{2}}\sum _{i,j}\xi _{i}\xi _{j}\partial _{i}\partial _{j}U(\mathbf {r} )$

Averaging over the fluctuations ${\boldsymbol {\xi }}$ ${\overline {\xi }}=0,\quad {\overline {\xi _{i}\xi _{j}}}={\frac {1}{3}}{\overline {{\boldsymbol {\xi }}^{2}}}\delta _{ij},$ gives the average potential ${\overline {U\left(\mathbf {r} +{\boldsymbol {\xi }}\right)}}=U{\left(\mathbf {r} \right)}+{\frac {1}{6}}{\overline {{\boldsymbol {\xi }}^{2}}}\nabla ^{2}U\left(\mathbf {r} \right).$

Approximating ${\overline {{\boldsymbol {\xi }}^{2}}}\approx {\lambda \!\!\!{\bar {}}_{\text{C}}}^{2}$ , this yields the perturbation of the potential due to fluctuations: $\delta U\approx {\frac {1}{6}}\lambda \!\!\!{\bar {}}_{\text{C}}^{2}\nabla ^{2}U={\frac {\hbar ^{2}}{6{m_{\text{e}}}^{2}c^{2}}}\nabla ^{2}U$

To compare with the expression above, plug in the Coulomb potential: $\nabla ^{2}U=-\nabla ^{2}{\frac {Ze^{2}}{4\pi \varepsilon _{0}r}}=4\pi \left({\frac {Ze^{2}}{4\pi \varepsilon _{0}}}\right)\delta ^{3}(\mathbf {r} )\quad \Rightarrow \quad \delta U\approx {\frac {\hbar ^{2}}{6{m_{\text{e}}}^{2}c^{2}}}4\pi \left({\frac {Ze^{2}}{4\pi \varepsilon _{0}}}\right)\delta ^{3}(\mathbf {r} )$

This is only slightly different.

Another mechanism that affects only the s-state is the Lamb shift, a further, smaller correction that arises in quantum electrodynamics that should not be confused with the Darwin term. The Darwin term gives the s-state and p-state the same energy, but the Lamb shift makes the s-state higher in energy than the p-state.

### Total effect

The full Hamiltonian is given by ${\mathcal {H}}={\mathcal {H}}_{\text{Coulomb}}+{\mathcal {H}}_{\text{kinetic}}+{\mathcal {H}}_{\mathrm {SO} }+{\mathcal {H}}_{\text{Darwin}},$ where ${\mathcal {H}}_{\text{Coulomb}}$ is the Hamiltonian from the Coulomb interaction.

The total effect, obtained by summing the three components up, is given by the following expression: $\Delta E={\frac {E_{n}(Z\alpha )^{2}}{n}}\left({\frac {1}{j+{\frac {1}{2}}}}-{\frac {3}{4n}}\right)\,,$ where j is the total angular momentum quantum number ( $j=1/2$ if $\ell =0$ and $j=\ell \pm 1/2$ otherwise). It is worth noting that this expression was first obtained by Sommerfeld based on the old quantum theory; i.e., before modern quantum mechanics was reformulated by Werner Heisenberg and Erwin Schrödinger.

### Exact relativistic energies

The total effect can also be obtained by using the Dirac equation. The exact energies are given by $E_{j\,n}=-m_{\text{e}}c^{2}\left[1-\left(1+\left[{\frac {\alpha }{n-j-{\frac {1}{2}}+{\sqrt {\left(j+{\frac {1}{2}}\right)^{2}-\alpha ^{2}}}}}\right]^{2}\right)^{-{\frac {1}{2}}}\right].$

This expression, which contains all higher order terms that were left out in the other calculations, expands to first order to give the energy corrections derived from perturbation theory. However, this equation does not contain the hyperfine structure corrections, which are due to interactions with the nuclear spin. Other corrections from quantum field theory such as the Lamb shift and the anomalous magnetic dipole moment of the electron are not included.
