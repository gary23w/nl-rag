---
title: "Nuclear Overhauser effect"
source: https://en.wikipedia.org/wiki/Nuclear_Overhauser_effect
domain: protein-nmr
license: CC-BY-SA-4.0
tags: nuclear magnetic resonance, protein dynamics, chemical shift, spin
fetched: 2026-07-02
---

# Nuclear Overhauser effect

The **nuclear Overhauser effect** (**NOE**) is the transfer of nuclear spin polarization from one population of spin-active nuclei (e.g. 1H, 13C, 15N etc.) to another via cross-relaxation. A phenomenological definition of the NOE in nuclear magnetic resonance spectroscopy (NMR) is the change in the integrated intensity (positive or negative) of one NMR resonance that occurs when another is saturated by irradiation with an RF field. The change in resonance intensity of a nucleus is a consequence of the nucleus being close in space to those directly affected by the RF perturbation.

The NOE is particularly important in the assignment of NMR resonances, and the elucidation and confirmation of the structures or configurations of organic and biological molecules. The 1H two-dimensional NOE spectroscopy (NOESY) experiment and its extensions are important tools to identify stereochemistry of proteins and other biomolecules in solution, whereas in solid form crystal x-ray diffraction typically used to identify stereochemistry. The heteronuclear NOE is particularly important in 13C NMR spectroscopy to identify carbons bonded to protons, to provide polarization enhancements to such carbons to increase signal-to-noise, and to ascertain the extent the relaxation of these carbons is controlled by the dipole-dipole relaxation mechanism.

## History

The NOE developed from the theoretical work of American physicist Albert Overhauser who in 1953 proposed that *nuclear* spin polarization could be enhanced by the microwave irradiation of the conduction *electrons* in certain metals. The electron-nuclear enhancement predicted by Overhauser was experimentally demonstrated in 7Li metal by T. R. Carver and C. P. Slichter also in 1953. A general theoretical basis and experimental observation of an Overhauser effect involving only *nuclear* spins in the HF molecule was published by Ionel Solomon in 1955. Another early experimental observation of the NOE was used by Kaiser in 1963 to show how the NOE may be used to determine the relative signs of scalar coupling constants, and to assign spectral lines in NMR spectra to transitions between energy levels. In this study, the resonance of one population of protons (1H) in an organic molecule was enhanced when a second distinct population of protons in the same organic molecule was saturated by RF irradiation. The application of the NOE was used by Anet and Bourn in 1965 to confirm the assignments of the NMR resonances for β,β-dimethylacrylic acid and dimethyl formamide, thereby showing that conformation and configuration information about organic molecules in solution can be obtained. Bell and Saunders reported direct correlation between NOE enhancements and internuclear distances in 1970 while quantitative measurements of internuclear distances in molecules with three or more spins was reported by Schirmer et al.

Richard R. Ernst was awarded the 1991 Nobel Prize in Chemistry for developing Fourier transform and two-dimensional NMR spectroscopy, which was soon adapted to the measurement of the NOE, particularly in large biological molecules. In 2002, Kurt Wüthrich won the Nobel Prize in Chemistry for the development of nuclear magnetic resonance spectroscopy for determining the three-dimensional structure of biological macromolecules in solution, demonstrating how the 2D NOE method (NOESY) can be used to constrain the three-dimensional structures of large biological macromolecules. Professor Anil Kumar was the first to apply the two-dimensional Nuclear Overhauser Effect (2D-NOE now known as NOESY) experiment to a biomolecule, which opened the field for the determination of three-dimensional structures of biomolecules in solution by NMR spectroscopy.

## Relaxation

The NOE and nuclear spin-lattice relaxation are closely related phenomena. For a single spin-1⁄2 nucleus in a magnetic field there are two energy levels that are often labeled α and β, which correspond to the two possible spin quantum states, +1⁄2 and -1⁄2, respectively. At thermal equilibrium, the population of the two energy levels is determined by the Boltzmann distribution with spin populations given by *P*α and *P*β. If the spin populations are perturbed by an appropriate RF field at the transition energy frequency, the spin populations return to thermal equilibrium by a process called *spin-lattice relaxation*. The rate of transitions from α to β is proportional to the population of state α, *P*α, and is a first order process with rate constant *W*. The condition where the spin populations are equalized by continuous RF irradiation (*P*α = *P*β) is called *saturation* and the resonance disappears since transition probabilities depend on the population difference between the energy levels.

In the simplest case where the NOE is relevant, the resonances of two spin-1⁄2 nuclei, I and S, are chemically shifted but not J-coupled. The energy diagram for such a system has four energy levels that depend on the spin-states of I and S corresponding to αα, αβ, βα, and ββ, respectively. The *W'*s are the probabilities per unit time that a transition will occur between the four energy levels, or in other terms the rate at which the corresponding spin flips occur. There are two single quantum transitions, *W*1I, corresponding to αα ➞ βα and αβ ➞ ββ; *W*1S, corresponding to αα ➞ αβ and βα ➞ ββ; a zero quantum transition, *W*0, corresponding to βα ➞ αβ, and a double quantum transition corresponding to αα ➞ ββ.

While rf irradiation can only induce single-quantum transitions (due to so-called quantum mechanical selection rules) giving rise to observable spectral lines, dipolar relaxation may take place through any of the pathways. The dipolar mechanism is the only common relaxation mechanism that can cause transitions in which more than one spin flips. Specifically, the dipolar relaxation mechanism gives rise to transitions between the αα and ββ states (*W*2) and between the αβ and the βα states (*W*0).

Expressed in terms of their bulk NMR magnetizations, the experimentally observed steady-state NOE for nucleus I when the resonance of nucleus S is saturated ( $M_{S}=0$ ) is defined by the expression:

$\eta _{I}^{S}=\left({\frac {M_{I}^{S}-M_{0I}}{M_{0I}}}\right)$

where $M_{0I}$ is the magnetization (resonance intensity) of nucleus I at thermal equilibrium. An analytical expression for the NOE can be obtained by considering all the relaxation pathways and applying the Solomon equations to obtain

$\eta _{I}^{S}={\frac {M_{I}^{S}-M_{0I}}{M_{0I}}}={\frac {\gamma _{S}}{\gamma _{I}}}{\frac {\sigma _{IS}}{\rho _{I}}}={\frac {\gamma _{S}}{\gamma _{I}}}\left({\frac {W_{2}-W_{0}}{2W_{1}^{I}+W_{0}+W_{2}}}\right)$

where

$\rho _{I}=2W_{1}^{I}+W_{0}+W_{2}$

and

$\sigma _{IS}=W_{2}-W_{0}$

.

$\rho _{I}$ is the total longitudinal dipolar relaxation rate ( $1/T_{1}$ ) of spin *I* due to the presence of spin *s*, $\sigma _{IS}$ is referred to as the *cross-relaxation* rate, and $\gamma _{I}$ and $\gamma _{S}$ are the magnetogyric ratios characteristic of the I and S nuclei, respectively.

Saturation of the degenerate *W*1S transitions disturbs the equilibrium populations so that *P*αα = *P*αβ and *P*βα = *P*ββ. The system's relaxation pathways, however, remain active and act to re-establish an equilibrium, except that the *W*1*S* transitions are irrelevant because the population differences across these transitions are fixed by the RF irradiation while the population difference between the *W*I transitions does not change from their equilibrium values. This means that if only the single quantum transitions were active as relaxation pathways, saturating the S resonance would not affect the intensity of the I resonance. Therefore to observe an NOE on the resonance intensity of I, the contribution of $W_{0}$ and $W_{2}$ must be important. These pathways, known as *cross-relaxation* pathways, only make a significant contribution to the spin-lattice relaxation when the relaxation is dominated by dipole-dipole or scalar coupling interactions, but the scalar interaction is rarely important and is assumed to be negligible. In the homonuclear case where $\gamma _{I}=\gamma _{S}$ , if $W_{2}$ is the dominant relaxation pathway, then saturating S increases the intensity of the I resonance and the NOE is *positive*, whereas if $W_{0}$ is the dominant relaxation pathway, saturating S decreases the intensity of the I resonance and the NOE is *negative*.

## Molecular motion

Whether the NOE is positive or negative depends sensitively on the degree of rotational molecular motion. The three dipolar relaxation pathways contribute to differing extents to the spin-lattice relaxation depending a number of factors. A key one is that the balance between ω2, ω1 and ω0 depends crucially on molecular rotational correlation time, $\tau _{c}$ , the time it takes a molecule to rotate one radian. NMR theory shows that the transition probabilities are related to $\tau _{c}$ and the Larmor precession frequencies, $\omega$ , by the relations:

$W_{1}^{I}\propto {\frac {3\tau _{c}}{(1+\omega _{I}^{2}\tau _{c}^{2})}}{\frac {1}{r^{6}}}$

$W_{0}\propto {\frac {2\tau _{c}}{(1+(\omega _{I}-\omega _{S})^{2}\tau _{c}^{2})}}{\frac {1}{r^{6}}}$

$W_{2}\propto {\frac {12\tau _{c}}{(1+(\omega _{I}+\omega _{S})^{2}\tau _{c}^{2})}}{\frac {1}{r^{6}}}$

where r is the distance separating two spin-1⁄2 nuclei. For relaxation to occur, the frequency of molecular tumbling must match the Larmor frequency of the nucleus. In mobile solvents, molecular tumbling motion is much faster than $\omega$ . The so-called extreme-narrowing limit where $\omega \tau _{c}\ll 1$ ). Under these conditions the double-quantum relaxation W2 is more effective than W1 or W0, because τc and 2ω0 match better than τc and ω1. When ω2 is the dominant relaxation process, a positive NOE results.

$W_{1}^{I}\propto \gamma _{I}^{2}\gamma _{S}^{2}{\frac {3\tau _{c}}{r^{6}}}$

$W_{0}\propto \gamma _{I}^{2}\gamma _{S}^{2}{\frac {2\tau _{c}}{r^{6}}}$

$W_{2}\propto \gamma _{I}^{2}\gamma _{S}^{2}{\frac {12\tau _{c}}{r^{6}}}$

$\eta _{I}^{S}(max)={\frac {\gamma _{S}}{\gamma _{I}}}\left[{\frac {{\frac {12\tau _{c}}{r^{6}}}-{\frac {2\tau _{c}}{r^{6}}}}{{\frac {2\tau _{c}}{r^{6}}}+2{\frac {3\tau _{c}}{r^{6}}}+{\frac {12\tau _{c}}{r^{6}}}}}\right]={\frac {\gamma _{S}}{\gamma _{I}}}\left[{\frac {12-2}{2+6+12}}\right]={\frac {\gamma _{S}}{\gamma _{I}}}{\frac {1}{2}}$

This expression shows that for the homonuclear case where *I* = *S*, most notably for 1*H* NMR, the maximum NOE that can be observed is 1\2 irrespective of the proximity of the nuclei. In the heteronuclear case where *I* ≠ *S*, the maximum NOE is given by 1\2 (*γ*S/*γ*I), which, when observing heteronuclei under conditions of broadband proton decoupling, can produce major sensitivity improvements. The most important example in organic chemistry is observation of 13C while decoupling 1H, which also saturates the 1J resonances. The value of *γ*S/*γ*I is close to 4, which gives a maximum NOE enhancement of 200% yielding resonances 3 times as strong as they would be without NOE. In many cases, carbon atoms have an attached proton, which causes the relaxation to be dominated by dipolar relaxation and the NOE to be near maximum. For non-protonated carbon atoms the NOE enhancement is small while for carbons that relax by relaxation mechanisms by other than dipole-dipole interactions the NOE enhancement can be significantly reduced. This is one motivation for using deuteriated solvents (e.g. CDCl3) in 13C NMR. Since deuterium relaxes by the quadrupolar mechanism, there are no cross-relaxation pathways and NOE is non-existent. Another important case is 15N, an example where the value of its magnetogyric ratio is negative. Often 15N resonances are reduced or the NOE may actually null out the resonance when 1H nuclei are decoupled. It is usually advantageous to take such spectra with pulse techniques that involve polarization transfer from protons to the 15N to minimize the negative NOE.

## Structure elucidation

While the relationship of the steady-state NOE to internuclear distance is complex, depending on relaxation rates and molecular motion, in many instances for small rapidly tumbling molecules in the extreme-narrowing limit, the semiquantitative nature of positive NOEs is useful for many structural applications often in combination with the measurement of J-coupling constants. For example, NOE enhancements can be used to confirm NMR resonance assignments, distinguish between structural isomers, identify aromatic ring substitution patterns and aliphatic substituent configurations, and determine conformational preferences.

The inter-atomic distances derived from the observed NOE can often help to confirm the three-dimensional structure of a molecule. In this application, the NOE differs from the application of J-coupling in that the NOE occurs through space, not through chemical bonds. Thus, atoms that are in close spatial proximity to each other can give an NOE regardless of how many chemical bonds separate them, whereas spin coupling is observed only when the atoms are connected by 1–3 chemical bonds. However, the relation *η*IS(max)=1⁄2 obscures how the NOE is related to internuclear distances because it applies only for the idealized case where the relaxation is 100% dominated by dipole-dipole interactions between two nuclei I and S. In practice, the value of ρI contains contributions from other competing mechanisms, which serve only to reduce the influence of *W*0 and *W*2 by increasing *W*1. Sometimes, for example, relaxation due to electron-nuclear interactions with dissolved oxygen or paramagnetic metal ion impurities in the solvent can prohibit the observation of weak NOE enhancements. The observed NOE in the presence of other relaxation mechanisms is given by

$\eta _{I}={\frac {\sigma _{IS}}{\rho _{I}+\rho ^{*}}}$

where ρ⋇ is the additional contribution to the total relaxation rate from relaxation mechanisms not involving cross relaxation. Using the same idealized two-spin model for dipolar relaxation in the extreme narrowing limit:

$\rho _{I}\propto {\frac {\tau _{c}}{r^{6}}}$

It is easy to show that

$\eta _{I}^{S}\propto \left({\frac {\tau _{c}}{\rho ^{*}}}\right){\frac {1}{r^{6}}}$

Thus, the two-spin steady-state NOE depends on internuclear distance only when there is a contribution from external relaxation. Bell and Saunders showed that following strict assumptions ρ⋇/τc is nearly constant for similar molecules in the extreme narrowing limit. Therefore, taking ratios of steady-state NOE values can give relative values for the internuclear distance *r*. While the steady-state experiment is useful in many cases, it can only provide information on relative internuclear distances. On the other hand, the initial *rate* at which the NOE grows is proportional to *r*IS−6, which provides other more sophisticated alternatives for obtaining structural information via transient experiments such as 2D-NOESY.

## Two-dimensional NMR

The motivations for using two-dimensional NMR for measuring NOEs are similar as for other 2-D methods. The maximum resolution is improved by spreading the affected resonances over two dimensions, therefore more peaks are resolved, larger molecules can be observed and more NOEs can be observed in a single measurement. More importantly, when the molecular motion is in the intermediate or slow motional regimes when the NOE is either zero or negative, the steady-state NOE experiment fails to give results that can be related to internuclear distances.

Nuclear Overhauser Effect Spectroscopy (NOESY) is a 2D NMR spectroscopic method used to identify nuclear spins undergoing cross-relaxation and to measure their cross-relaxation rates. Since 1H dipole-dipole couplings provide the primary means of cross-relaxation for organic molecules in solution, spins undergoing cross-relaxation are those close to one another in space. Therefore, the cross peaks of a NOESY spectrum indicate which protons are close to each other in space. In this respect, the NOESY experiment differs from the COSY experiment that relies on J-coupling to provide spin-spin correlation, and whose cross peaks indicate which 1H's are close to which other 1H's through the chemical bonds of the molecule.

The basic NOESY sequence consists of three 90° pulses. The first pulse creates transverse spin magnetization. The spins precess during the evolution time t1, which is incremented during the course of the 2D experiment. The second pulse produces longitudinal magnetization equal to the transverse magnetization component orthogonal to the pulse direction. Thus, the idea is to produce an initial condition for the mixing period τm. During the NOE mixing time, magnetization transfer via cross-relaxation can take place. For the basic NOESY experiment, τm is kept constant throughout the 2D experiment, but chosen for the optimum cross-relaxation rate and build-up of the NOE. The third pulse creates transverse magnetization from the remaining longitudinal magnetization. Data acquisition begins immediately following the third pulse and the transverse magnetization is observed as a function of the pulse delay time t2. The NOESY spectrum is generated by a 2D Fourier transform with respect to t1 and t2. A series of experiments are carried out with increasing mixing times, and the increase in NOE enhancement is followed. The closest protons show the most rapid build-up rates of the NOE.

Inter-proton distances can be determined from unambiguously assigned, well-resolved, high signal-to-noise NOESY spectra by analysis of cross peak intensities. These may be obtained by volume integration and can be converted into estimates of interproton distances. The distance between two atoms i and j can be calculated from the cross-peak volumes V and a scaling constant c

$r_{\text{NOE}}=\left({\frac {c}{V_{ij}}}\right)^{1/6}$

where c can be determined based on measurements of known fixed distances. The range of distances can be reported based on known distances and volumes in the spectrum, which gives a mean c and a standard deviation $c_{SD}$ , a measurement of multiple regions in the NOESY spectrum showing no peaks, *i.e.* noise $V_{\rm {err}}$ , and a measurement error $m_{v}$ . The parameter x is set so that all known distances are within the error bounds. This shows that the lower range of the NOESY volume is

$r_{\text{NOE lower}}=\left({\frac {c-xc_{SD}}{{\frac {1}{m_{v}}}V_{ij}+V_{\rm {err}}}}\right)^{1/6}$

and that the upper bound is

$r_{\text{NOE higher}}=\left({\frac {c+xc_{SD}}{{\frac {1}{m_{v}}}V_{ij}-V_{\rm {err}}}}\right)^{1/6}$

Such fixed distances depend on the system studied. For example, locked nucleic acids have many atoms whose distance varies very little in the sugar, which allows estimation of the glycosidic torsion angles, which allowed NMR to benchmark LNA molecular dynamics predictions. RNAs, however, have sugars that are much more conformationally flexible, and require wider estimations of low and high bounds.

In protein structural characterization, NOEs are used to create constraints on intramolecular distances. In this method, each proton pair is considered in isolation and NOESY cross peak intensities are compared with a reference cross peak from a proton pair of fixed distance, such as a geminal methylene proton pair or aromatic ring protons. This simple approach is reasonably insensitive to the effects of spin diffusion or non-uniform correlation times and can usually lead to definition of the global fold of the protein, provided a sufficiently large number of NOEs have been identified. NOESY cross peaks can be classified as strong, medium or weak and can be translated into upper distance restraints of around 2.5, 3.5 and 5.0 Å, respectively. Such constraints can then be used in molecular mechanics optimizations to provide a picture of the solution state conformation of the protein. Full structure determination relies on a variety of NMR experiments and optimization methods utilizing both chemical shift and NOESY constraints.

## Heteronuclear NOE

## Some experimental methods

Some examples of one and two-dimensional NMR experimental techniques exploiting the NOE include:

- NOESY, Nuclear Overhauser effect Spectroscopy
- HOESY, Heteronuclear Overhauser effect spectroscopy
- ROESY, Rotational frame nuclear Overhauser effect spectroscopy
- TRNOE, Transferred nuclear Overhauser effect
- DPFGSE-NOE, Double pulsed field gradient spin echo NOE experiment

NOESY is the determination of the relative orientations of atoms in a molecule, for example a protein or other large biological molecule, producing a three-dimensional structure. HOESY is NOESY cross-correlation between atoms of different elements. ROESY involves spin-locking the magnetization to prevent it from going to zero, applied for molecules for which regular NOESY is not applicable. TRNOE measures the NOE between two different molecules interacting in the same solution, as in a ligand binding to a protein. In a DPFGSE-NOE experiment, a transient experiment that allows for suppression of strong signals and thus detection of very small NOEs.

## Examples of nuclear Overhauser effect

The figure (top) displays how Nuclear Overhauser Effect Spectroscopy can elucidate the structure of a switchable compound. In this example, the proton designated as {H} shows two different sets of NOEs depending on the isomerization state (*cis* or *trans*) of the switchable azo groups. In the *trans* state proton {H} is far from the phenyl group showing blue coloured NOEs; while the *cis* state holds proton {H} in the vicinity of the phenyl group resulting in the emergence of new NOEs (show in red).

Another example (bottom) where application where the NOE is useful to assign resonances and determine configuration is polysaccharides. For instance, complex glucans possess a multitude of overlapping signals, especially in a proton spectrum. Therefore, it is advantageous to utilize 2D NMR experiments including NOESY for the assignment of signals. See, for example, NOE of carbohydrates.
