---
title: "Zeeman effect"
source: https://en.wikipedia.org/wiki/Zeeman_effect
domain: atomic-physics
license: CC-BY-SA-4.0
tags: atomic physics, atomic orbital, fine structure, zeeman effect
fetched: 2026-07-02
---

# Zeeman effect

The **Zeeman effect** (Dutch: [ˈzeːmɑn]) is the splitting of a spectral line into several components in the presence of a static magnetic field. It is caused by the interaction of the magnetic field with the magnetic moments of the atomic electrons associated with their orbital motion and spin; this interaction shifts some orbital energies more than others, resulting in the split spectrum.

The effect is named after the Dutch physicist Pieter Zeeman, who discovered it in 1896 and received the Nobel Prize in Physics for it in 1902. It is analogous to the Stark effect, the splitting of a spectral line into several components in the presence of an electric field. Also, similar to the Stark effect, transitions between different components have, in general, different intensities, with some being entirely forbidden (in the dipole approximation), as governed by the selection rules.

Since the distance between the Zeeman sub-levels is a function of magnetic field strength, this effect can be used to measure magnetic field strength, e.g. that of the Sun and other stars or in laboratory plasmas.

## Discovery

In 1896, Zeeman learned that his laboratory had one of Henry Augustus Rowland's highest resolving diffraction gratings. Zeeman had read James Clerk Maxwell's article in *Encyclopædia Britannica* describing Michael Faraday's failed attempts to influence light with magnetism. Zeeman wondered if the new spectrographic techniques could succeed where early efforts had not.

When illuminated by a slit-shaped source, the grating produces a long array of slit images corresponding to different wavelengths. Zeeman placed a piece of asbestos soaked in salt water into a Bunsen burner flame at the source of the grating: he could easily see two lines in the sodium light emission spectrum. Switching on a strong (about one tesla) electromagnet around the flame, he observed a slight broadening of the lines.

When Zeeman switched to cadmium as the source, he observed the spectral lines split when the magnetic field was applied. These splittings could be analyzed with Hendrik Lorentz's then-new electron theory. It is now known that the magnetic effects on sodium require quantum-mechanical treatment. Zeeman and Lorentz were awarded the 1902 Nobel Prize; in his acceptance speech Zeeman explained his apparatus and showed slides of the spectrographic images.

## Nomenclature

Historically, one distinguishes between the **normal** and an **anomalous Zeeman effect** (discovered by Thomas Preston in Dublin, Ireland). The anomalous effect appears on transitions where the net spin of the electrons is non-zero. It was called "anomalous" because the electron spin had not yet been discovered, and so there was no good explanation for it at the time that Zeeman observed the effect. Wolfgang Pauli recalled that when asked by a colleague as to why he looked unhappy, he replied: "How can one look happy when he is thinking about the anomalous Zeeman effect?"

At higher magnetic field strength the effect ceases to be linear. At even higher field strengths, comparable to the strength of the atom's internal field, the electron coupling is disturbed and the spectral lines rearrange. This is called the **Paschen–Back effect**.

In modern scientific literature, these terms are rarely used, with a tendency to use just the "Zeeman effect". Another rarely used obscure term is **inverse Zeeman effect**, referring to the Zeeman effect in an absorption spectral line.

A similar effect, splitting of the nuclear energy levels in the presence of a magnetic field, is referred to as the **nuclear Zeeman effect**.

## Theoretical presentation

The total Hamiltonian of an atom in a magnetic field is $H=H_{0}+V_{\text{M}},$ where $H_{0}$ is the unperturbed Hamiltonian of the atom, and $V_{\text{M}}$ is the perturbation due to the magnetic field: $V_{\text{M}}=-{\vec {\mu }}\cdot {\vec {B}},$ where ${\vec {\mu }}$ is the magnetic moment of the atom. The magnetic moment consists of the electronic and nuclear parts; however, the latter is many orders of magnitude smaller and will be neglected here. Therefore, ${\vec {\mu }}\approx -{\frac {\mu _{\text{B}}g{\vec {J}}}{\hbar }},$ where $\mu _{\text{B}}$ is the Bohr magneton, ${\vec {J}}$ is the total electronic angular momentum, and g is the Landé g-factor.

A more accurate approach is to take into account that the operator of the magnetic moment of an electron is a sum of the contributions of the orbital angular momentum ${\vec {L}}$ and the spin angular momentum ${\vec {S}}$ , with each multiplied by the appropriate gyromagnetic ratio: ${\vec {\mu }}=-{\frac {\mu _{\text{B}}(g_{l}{\vec {L}}+g_{s}{\vec {S}})}{\hbar }},$ where $g_{l}=1$ , and $g_{s}\approx 2.0023193$ (the anomalous gyromagnetic ratio, deviating from 2 due to the effects of quantum electrodynamics). In the case of the LS coupling, one can sum over all electrons in the atom: $g{\vec {J}}={\Big \langle }\sum _{i}(g_{l}{\vec {l}}_{i}+g_{s}{\vec {s}}_{i}){\Big \rangle }={\big \langle }(g_{l}{\vec {L}}+g_{s}{\vec {S}}){\big \rangle },$ where ${\vec {L}}$ and ${\vec {S}}$ are the total spin momentum and spin of the atom, and averaging is done over a state with a given value of the total angular momentum.

If the interaction term $V_{\text{M}}$ is small (less than the fine structure), it can be treated as a perturbation; this is the Zeeman effect proper. In the Paschen–Back effect, described below, $V_{\text{M}}$ exceeds the LS coupling significantly (but is still small compared to $H_{0}$ ). In ultra-strong magnetic fields, the magnetic-field interaction may exceed $H_{0}$ , in which case the atom can no longer exist in its normal meaning, and one talks about Landau levels instead. There are intermediate cases that are more complex than these limit cases.

## Weak field (Zeeman effect)

If the spin–orbit interaction dominates over the effect of the external magnetic field, ${\vec {L}}$ and ${\vec {S}}$ are not separately conserved, only the total angular momentum ${\vec {J}}={\vec {L}}+{\vec {S}}$ is. The spin and orbital angular momentum vectors can be thought of as precessing about the (fixed) total angular momentum vector ${\vec {J}}$ . The (time-)"averaged" spin vector is then the projection of the spin onto the direction of ${\vec {J}}$ : ${\vec {S}}_{\text{avg}}={\frac {({\vec {S}}\cdot {\vec {J}})}{J^{2}}}{\vec {J}},$ and for the (time-)"averaged" orbital vector: ${\vec {L}}_{\text{avg}}={\frac {({\vec {L}}\cdot {\vec {J}})}{J^{2}}}{\vec {J}}.$

Thus $\langle V_{\text{M}}\rangle ={\frac {\mu _{\text{B}}}{\hbar }}{\vec {J}}\left(g_{L}{\frac {{\vec {L}}\cdot {\vec {J}}}{J^{2}}}+g_{S}{\frac {{\vec {S}}\cdot {\vec {J}}}{J^{2}}}\right)\cdot {\vec {B}}.$ Using ${\vec {L}}={\vec {J}}-{\vec {S}}$ and squaring both sides, we get ${\vec {S}}\cdot {\vec {J}}={\frac {1}{2}}(J^{2}+S^{2}-L^{2})={\frac {\hbar ^{2}}{2}}[j(j+1)-l(l+1)+s(s+1)],$ and using ${\vec {S}}={\vec {J}}-{\vec {L}}$ and squaring both sides, we get ${\vec {L}}\cdot {\vec {J}}={\frac {1}{2}}(J^{2}-S^{2}+L^{2})={\frac {\hbar ^{2}}{2}}[j(j+1)+l(l+1)-s(s+1)].$

Combining everything and taking $J_{z}=\hbar m_{j}$ , we obtain the magnetic potential energy of the atom in the applied external magnetic field: ${\begin{aligned}V_{\text{M}}&=\mu _{\text{B}}Bm_{j}\left[g_{L}{\frac {j(j+1)+l(l+1)-s(s+1)}{2j(j+1)}}+g_{S}{\frac {j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}}\right]\\&=\mu _{\text{B}}Bm_{j}\left[1+(g_{S}-1){\frac {j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}}\right]\\&=\mu _{\text{B}}Bm_{j}g_{J},\end{aligned}}$ where the quantity in square brackets is the Landé g-factor $g_{J}$ of the atom ( $g_{L}=1,$ $g_{S}\approx 2$ ), and $m_{j}$ is the *z* component of the total angular momentum.

For a single electron above filled shells, with $s=1/2$ and $j=l\pm s$ , the Landé g-factor can be simplified to $g_{J}=1\pm {\frac {g_{S}-1}{2l+1}}.$

Taking $V_{\text{M}}$ to be the perturbation, the Zeeman correction to the energy is $E_{\text{Z}}^{(1)}=\langle nljm_{j}|H_{\text{Z}}^{'}|nljm_{j}\rangle =\langle V_{\text{M}}\rangle _{\Psi }=\mu _{\text{B}}g_{J}B_{\text{ext}}m_{j}.$

### Example: Lyman-alpha transition in hydrogen

The Lyman-alpha transition in hydrogen in the presence of the spin–orbit interaction involves the transitions $2\,^{2}\!P_{1/2}\to 1\,^{2}\!S_{1/2}$ and $2\,^{2}\!P_{3/2}\to 1\,^{2}\!S_{1/2}.$

In the presence of an external magnetic field, the weak-field Zeeman effect splits the $1\,^{2}\!S_{1/2}$ and $2\,^{2}\!P_{1/2}$ levels into 2 states each ( $m_{j}=+1/2,-1/2$ ) and the $2\,^{2}\!P_{3/2}$ level into 4 states ( $m_{j}=+3/2,+1/2,-1/2,-3/2$ ). The Landé g-factors for the three levels are ${\begin{aligned}g_{J}&=2&&{\text{for}}\ 1\,^{2}\!S_{1/2}\ (j=1/2,l=0),\\g_{J}&=2/3&&{\text{for}}\ 2\,^{2}\!P_{1/2}\ (j=1/2,l=1),\\g_{J}&=4/3&&{\text{for}}\ 2\,^{2}\!P_{3/2}\ (j=3/2,l=1).\end{aligned}}$

Note in particular that the size of the energy splitting is different for the different orbitals because the *gJ* values are different. Fine-structure splitting occurs even in the absence of a magnetic field, as it is due to spin–orbit coupling. Depicted on the right is the additional Zeeman splitting, which occurs in the presence of magnetic fields.

| Initial state $(n=2,l=1)$ $\|j,m_{j}\rangle$ | Final state $(n=1,l=0)$ $\|j,m_{j}\rangle$ | Energy perturbation |
|---|---|---|
| $\left\|{\frac {1}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\left\|{\frac {1}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\mp {\frac {2}{3}}\mu _{\text{B}}B$ |
| $\left\|{\frac {1}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\left\|{\frac {1}{2}},\mp {\frac {1}{2}}\right\rangle$ | $\pm {\frac {4}{3}}\mu _{\text{B}}B$ |
| $\left\|{\frac {3}{2}},\pm {\frac {3}{2}}\right\rangle$ | $\left\|{\frac {1}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\pm \mu _{\rm {B}}B$ |
| $\left\|{\frac {3}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\left\|{\frac {1}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\mp {\frac {1}{3}}\mu _{\text{B}}B$ |
| $\left\|{\frac {3}{2}},\pm {\frac {1}{2}}\right\rangle$ | $\left\|{\frac {1}{2}},\mp {\frac {1}{2}}\right\rangle$ | $\pm {\frac {5}{3}}\mu _{\text{B}}B$ |

## Strong field (Paschen–Back effect)

The Paschen–Back effect is the splitting of atomic energy levels in the presence of a strong magnetic field. This occurs when an external magnetic field is sufficiently strong to disrupt the coupling between orbital ( ${\vec {L}}$ ) and spin ( ${\vec {S}}$ ) angular momenta. This effect is the strong-field limit of the Zeeman effect. When $s=0$ , the two effects are equivalent. The effect was named after the German physicists Friedrich Paschen and Ernst E. A. Back.

When the magnetic-field perturbation significantly exceeds the spin–orbit interaction, one can safely assume $[H_{0},S]=0$ . This allows the expectation values of $L_{z}$ and $S_{z}$ to be easily evaluated for a state $|\psi \rangle$ . The energies are simply

$E_{z}=\left\langle \psi \left|H_{0}+{\frac {B_{z}\mu _{\rm {B}}}{\hbar }}(L_{z}+g_{s}S_{z})\right|\psi \right\rangle =E_{0}+B_{z}\mu _{\rm {B}}(m_{l}+g_{s}m_{s}).$

The above may be read as implying that the LS-coupling is completely broken by the external field. However, $m_{l}$ and $m_{s}$ are still "good" quantum numbers. Together with the selection rules for an electric dipole transition, i.e., $\Delta s=0,\Delta m_{s}=0,\Delta l=\pm 1,\Delta m_{l}=0,\pm 1$ this allows to ignore the spin degree of freedom altogether. As a result, only three spectral lines will be visible, corresponding to the $\Delta m_{l}=0,\pm 1$ selection rule. The splitting $\Delta E=B\mu _{\rm {B}}\Delta m_{l}$ is *independent* of the unperturbed energies and electronic configurations of the levels being considered.

More precisely, if $s\neq 0$ , each of these three components is actually a group of several transitions due to the residual spin–orbit coupling and relativistic corrections (which are of the same order, known as 'fine structure'). The first-order perturbation theory with these corrections yields the following formula for the hydrogen atom in the Paschen–Back limit:

$E_{z+fs}=E_{z}+{\frac {m_{e}c^{2}\alpha ^{4}}{2n^{3}}}\left\{{\frac {3}{4n}}-\left[{\frac {l(l+1)-m_{l}m_{s}}{l(l+1/2)(l+1)}}\right]\right\}.$

### Example: Lyman-alpha transition in hydrogen

In this example, the fine-structure corrections are ignored.

| Initial state ( $n=2,l=1$ ) $\mid m_{l},m_{s}\rangle$ | Initial energy perturbation | Final state ( $n=1,l=0$ ) $\mid m_{l},m_{s}\rangle$ | Final energy perturbation |
|---|---|---|---|
| $\left\|1,{\frac {1}{2}}\right\rangle$ | $+2\mu _{\rm {B}}B_{z}$ | $\left\|0,{\frac {1}{2}}\right\rangle$ | $+\mu _{\rm {B}}B_{z}$ |
| $\left\|0,{\frac {1}{2}}\right\rangle$ | $+\mu _{\rm {B}}B_{z}$ | $\left\|0,{\frac {1}{2}}\right\rangle$ | $+\mu _{\rm {B}}B_{z}$ |
| $\left\|1,-{\frac {1}{2}}\right\rangle$ | 0 | $\left\|0,-{\frac {1}{2}}\right\rangle$ | $-\mu _{\rm {B}}B_{z}$ |
| $\left\|-1,{\frac {1}{2}}\right\rangle$ | 0 | $\left\|0,{\frac {1}{2}}\right\rangle$ | $+\mu _{\rm {B}}B_{z}$ |
| $\left\|0,-{\frac {1}{2}}\right\rangle$ | $-\mu _{\rm {B}}B_{z}$ | $\left\|0,-{\frac {1}{2}}\right\rangle$ | $-\mu _{\rm {B}}B_{z}$ |
| $\left\|-1,-{\frac {1}{2}}\right\rangle$ | $-2\mu _{\rm {B}}B_{z}$ | $\left\|0,-{\frac {1}{2}}\right\rangle$ | $-\mu _{\rm {B}}B_{z}$ |

## Intermediate field for j = 1/2

In the magnetic dipole approximation, the Hamiltonian which includes both the hyperfine and Zeeman interactions is

$H=hA{\vec {I}}\cdot {\vec {J}}-{\vec {\mu }}\cdot {\vec {B}}$

$H=hA{\vec {I}}\cdot {\vec {J}}+(\mu _{\rm {B}}g_{J}{\vec {J}}+\mu _{\rm {N}}g_{I}{\vec {I}})\cdot {\vec {\rm {B}}}$

where A is the hyperfine splitting at zero applied magnetic field, $\mu _{\rm {B}}$ and $\mu _{\rm {N}}$ are the Bohr magneton and nuclear magneton, respectively (note that the last term in the expression above describes the *nuclear* Zeeman effect), ${\vec {J}}$ and ${\vec {I}}$ are the electron and nuclear angular momentum operators and $g_{J}$ is the Landé g-factor: $g_{J}=g_{L}{\frac {J(J+1)+L(L+1)-S(S+1)}{2J(J+1)}}+g_{S}{\frac {J(J+1)-L(L+1)+S(S+1)}{2J(J+1)}}.$

In the case of weak magnetic fields, the Zeeman interaction can be treated as a perturbation to the $|F,m_{f}\rangle$ basis. In the high field regime, the magnetic field becomes so strong that the Zeeman effect will dominate, and one must use a more complete basis of $|I,J,m_{I},m_{J}\rangle$ or just $|m_{I},m_{J}\rangle$ since I and J will be constant within a given level.

To get the complete picture, including intermediate field strengths, we must consider eigenstates which are superpositions of the $|F,m_{F}\rangle$ and $|m_{I},m_{J}\rangle$ basis states. For $J=1/2$ , the Hamiltonian can be solved analytically, resulting in the **Breit–Rabi formula** (named after Gregory Breit and Isidor Isaac Rabi). Notably, the electric quadrupole interaction is zero for $L=0$ ( $J=1/2$ ), so this formula is fairly accurate.

We now utilize quantum mechanical ladder operators, which are defined for a general angular momentum operator L as

$L_{\pm }\equiv L_{x}\pm iL_{y}$

These ladder operators have the property

$L_{\pm }|L_{,}m_{L}\rangle ={\sqrt {(L\mp m_{L})(L\pm m_{L}+1)}}|L,m_{L}\pm 1\rangle$

as long as $m_{L}$ lies in the range ${-L,\dots ...,L}$ (otherwise, they return zero). Using ladder operators $J_{\pm }$ and $I_{\pm }$ We can rewrite the Hamiltonian as

$H=hAI_{z}J_{z}+{\frac {hA}{2}}(J_{+}I_{-}+J_{-}I_{+})+\mu _{\rm {B}}Bg_{J}J_{z}+\mu _{\rm {N}}Bg_{I}I_{z}$

We can now see that at all times, the total angular momentum projection $m_{F}=m_{J}+m_{I}$ will be conserved. This is because both $J_{z}$ and $I_{z}$ leave states with definite $m_{J}$ and $m_{I}$ unchanged, while $J_{+}I_{-}$ and $J_{-}I_{+}$ either increase $m_{J}$ and decrease $m_{I}$ or vice versa, so the sum is always unaffected. Furthermore, since $J=1/2$ there are only two possible values of $m_{J}$ which are $\pm 1/2$ . Therefore, for every value of $m_{F}$ there are only two possible states, and we can define them as the basis:

$|\pm \rangle \equiv |m_{J}=\pm 1/2,m_{I}=m_{F}\mp 1/2\rangle$

This pair of states is a two-level quantum mechanical system. Now we can determine the matrix elements of the Hamiltonian:

$\langle \pm |H|\pm \rangle =-{\frac {1}{4}}hA+\mu _{\rm {N}}Bg_{I}m_{F}\pm {\frac {1}{2}}(hAm_{F}+\mu _{\rm {B}}Bg_{J}-\mu _{\rm {N}}Bg_{I}))$

$\langle \pm |H|\mp \rangle ={\frac {1}{2}}hA{\sqrt {(I+1/2)^{2}-m_{F}^{2}}}$

Solving for the eigenvalues of this matrix – as can be done by hand (see two-level quantum mechanical system), or more easily, with a computer algebra system – we arrive at the energy shifts:

$\Delta E_{F=I\pm 1/2}=-{\frac {h\Delta W}{2(2I+1)}}+\mu _{\rm {N}}g_{I}m_{F}B\pm {\frac {h\Delta W}{2}}{\sqrt {1+{\frac {2m_{F}x}{I+1/2}}+x^{2}}}$

$x\equiv {\frac {B(\mu _{\rm {B}}g_{J}-\mu _{\rm {N}}g_{I})}{h\Delta W}}\quad \quad \Delta W=A\left(I+{\frac {1}{2}}\right)$

where $\Delta W$ is the splitting (in units of Hz) between two hyperfine sublevels in the absence of magnetic field B , x is referred to as the 'field strength parameter' (Note: for $m_{F}=\pm (I+1/2)$ the expression under the square root is an exact square, and so the last term should be replaced by $+{\frac {h\Delta W}{2}}(1\pm x)$ ). This equation is known as the **Breit–Rabi formula** and is useful for systems with one valence electron in an s ( $J=1/2$ ) level.

Note that index F in $\Delta E_{F=I\pm 1/2}$ should be considered not as total angular momentum of the atom but as *asymptotic total angular momentum*. It is equal to total angular momentum only if $B=0$ otherwise eigenvectors corresponding different eigenvalues of the Hamiltonian are the superpositions of states with different F but equal $m_{F}$ (the only exceptions are $|F=I+1/2,m_{F}=\pm F\rangle$ ).

## Applications

### Astrophysics

George Ellery Hale was the first to notice the Zeeman effect in the solar spectra, indicating the existence of strong magnetic fields in sunspots. Such fields can be quite high, on the order of 0.1 tesla or higher. Today, the Zeeman effect is used to produce magnetograms showing the variation of magnetic field on the Sun, and to analyze the magnetic field geometries in other stars.

### Laser cooling

The Zeeman effect is utilized in many laser cooling applications such as a magneto-optical trap and the Zeeman slower.

### Spintronics

Zeeman-energy mediated coupling of spin and orbital motions is used in spintronics for controlling electron spins in quantum dots through electric dipole spin resonance.

### Metrology

Old high-precision frequency standards, i.e. hyperfine structure transition-based atomic clocks, may require periodic fine-tuning due to exposure to magnetic fields. This is carried out by measuring the Zeeman effect on specific hyperfine structure transition levels of the source element (cesium) and applying a uniformly precise, low-strength magnetic field to said source, in a process known as degaussing.

The Zeeman effect may also be utilized to improve accuracy in atomic absorption spectroscopy.

### Biology

A theory about the magnetic sense of birds assumes that a protein in the retina is changed due to the Zeeman effect.

### Nuclear spectroscopy

The nuclear Zeeman effect is important in such applications as nuclear magnetic resonance spectroscopy, magnetic resonance imaging (MRI), and Mössbauer spectroscopy.

### Other

The electron spin resonance spectroscopy is based on the Zeeman effect.

## Demonstrations

The Zeeman effect can be demonstrated by placing a sodium vapor source in a powerful electromagnet and viewing a sodium vapor lamp through the magnet opening (see diagram). With magnet off, the sodium vapor source will block the lamp light; when the magnet is turned on the lamp light will be visible through the vapor.

The sodium vapor can be created by sealing sodium metal in an evacuated glass tube and heating it while the tube is in the magnet.

Alternatively, salt (sodium chloride) on a ceramic stick can be placed in the flame of Bunsen burner as the sodium vapor source. When the magnetic field is energized, the lamp image will be brighter. However, the magnetic field also affects the flame, making the observation depend upon more than just the Zeeman effect. These issues also plagued Zeeman's original work; he devoted considerable effort to ensure his observations were truly an effect of magnetism on light emission.

When salt is added to the Bunsen burner, it dissociates to give sodium and chloride. The sodium atoms get excited due to photons from the sodium vapour lamp, with electrons excited from 3s to 3p states, absorbing light in the process. The sodium vapour lamp emits light at 589nm, which has precisely the energy to excite an electron of a sodium atom. If it was an atom of another element, like chlorine, shadow will not be formed. When a magnetic field is applied, due to the Zeeman effect the spectral line of sodium gets split into several components. This means the energy difference between the 3s and 3p atomic orbitals will change. As the sodium vapour lamp don't precisely deliver the right frequency anymore, light doesn't get absorbed and passes through, resulting in the shadow dimming. As the magnetic field strength is increased, the shift in the spectral lines increases and lamp light is transmitted.
