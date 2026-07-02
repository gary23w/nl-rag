---
title: "Nuclear magnetic resonance (part 1/2)"
source: https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance
domain: spectroscopy-physics
license: CC-BY-SA-4.0
tags: atomic spectroscopy, emission spectrum, raman spectroscopy, spectral line
fetched: 2026-07-02
part: 1/2
---

# Nuclear magnetic resonance

**Nuclear magnetic resonance** (**NMR**) is a physical phenomenon in which nuclei in a strong constant magnetic field are disturbed by a weak oscillating magnetic field (in the near field) and respond by producing an electromagnetic signal with a frequency characteristic of the magnetic field at the nucleus. This process occurs near resonance, when the oscillation frequency matches the intrinsic frequency of the nuclei, which depends on the strength of the static magnetic field, the chemical environment, and the magnetic properties of the isotope involved; in practical applications with static magnetic fields up to ca. 20 tesla, the frequency is similar to VHF and UHF television broadcasts (60–1000 MHz). NMR results from specific magnetic properties of certain atomic nuclei. High-resolution nuclear magnetic resonance spectroscopy is widely used to determine the structure of organic molecules in solution and study molecular physics and crystals as well as non-crystalline materials. NMR is also routinely used in advanced medical imaging techniques, such as in magnetic resonance imaging (MRI). The original application of NMR to condensed matter physics is nowadays mostly devoted to strongly correlated electron systems. It reveals large many-body couplings by fast broadband detection and should not be confused with solid state NMR, which aims at removing the effect of the same couplings by Magic Angle Spinning techniques.

The most commonly used nuclei are 1 H and 13 C, although isotopes of many other elements, such as 19 F, 31 P, and 29 Si, can be studied by high-field NMR spectroscopy as well. In order to interact with the magnetic field in the spectrometer, the nucleus must have an intrinsic angular momentum and nuclear magnetic dipole moment. This occurs when an isotope has a nonzero nuclear spin, meaning an odd number of protons and/or neutrons (see Isotope). Nuclides with even numbers of both have a total spin of zero and are therefore not NMR-active.

In its application to molecules the NMR effect can be observed only in the presence of a static magnetic field. However, in the ordered phases of magnetic materials, very large internal fields are produced at the nuclei of magnetic ions (and of close ligands), which allow NMR to be performed in zero applied field. Additionally, radio-frequency transitions of nuclear spin I > ⁠1/2⁠ with large enough electric quadrupolar coupling to the electric field gradient at the nucleus may also be excited in zero applied magnetic field (nuclear quadrupole resonance).

In the dominant chemistry application, the use of higher fields improves the sensitivity of the method (signal-to-noise ratio scales approximately as the power of ⁠3/2⁠ with the magnetic field strength) and the spectral resolution. Commercial NMR spectrometers employing liquid helium cooled superconducting magnets with fields of up to 28 Tesla have been developed and are widely used.

It is a key feature of NMR that the resonance frequency of nuclei in a particular sample substance is usually directly proportional to the strength of the applied magnetic field. It is this feature that is exploited in imaging techniques; if a sample is placed in a non-uniform magnetic field then the resonance frequencies of the sample's nuclei depend on where in the field they are located. This effect serves as the basis of magnetic resonance imaging.

The principle of NMR usually involves three sequential steps:

- The alignment (polarization) of the magnetic nuclear spins in an applied, constant magnetic field **B**0.
- The perturbation of this alignment of the nuclear spins by a weak oscillating magnetic field, usually referred to as a radio frequency (RF) pulse. The oscillation frequency required for significant perturbation is dependent upon the static magnetic field (**B**0) and the nuclei of observation.
- The detection of the NMR signal during or after the RF pulse, due to the voltage induced in a detection coil by precession of the nuclear spins around **B**0. After an RF pulse, precession usually occurs with the nuclei's Larmor frequency and, in itself, does not involve transitions between spin states or energy levels.

The two magnetic fields are usually chosen to be perpendicular to each other as this maximizes the NMR signal strength. The frequencies of the time-signal response by the total magnetization (**M**) of the nuclear spins are analyzed in NMR spectroscopy and magnetic resonance imaging. Both use applied magnetic fields (**B**0) of great strength, usually produced by large currents in superconducting coils, in order to achieve dispersion of response frequencies and of very high homogeneity and stability in order to deliver spectral resolution, the details of which are described by chemical shifts, the Zeeman effect, and Knight shifts (in metals). The information provided by NMR can also be increased using hyperpolarization, and/or using two-dimensional, three-dimensional and higher-dimensional techniques.

NMR phenomena are also utilized in low-field NMR, NMR spectroscopy and MRI in the Earth's magnetic field (referred to as Earth's field NMR), and in several types of magnetometers.


## History

Nuclear magnetic resonance was first described and measured in molecular beams by Isidor Rabi in 1938, by extending the Stern–Gerlach experiment, and in 1944, Rabi was awarded the Nobel Prize in Physics for this work. In 1946, Felix Bloch and Edward Mills Purcell expanded the technique for use on liquids and solids, for which they shared the Nobel Prize in Physics in 1952.

Russell H. Varian filed the "Method and means for correlating nuclear properties of atoms and magnetic fields", U.S. patent 2,561,490 on October 21, 1948 and was accepted on July 24, 1951. Varian Associates developed the first NMR unit called NMR HR-30 in 1952.

Purcell had worked on the development of radar during World War II at the Massachusetts Institute of Technology's Radiation Laboratory. His work during that project on the production and detection of radio frequency power and on the absorption of such RF power by matter laid the foundation for his discovery of NMR in bulk matter.

Rabi, Bloch, and Purcell observed that magnetic nuclei, like 1 H and 31 P, could absorb RF energy when placed in a magnetic field and when the RF was of a frequency specific to the identity of the nuclei. When this absorption occurs, the nucleus is described as being *in resonance*. Different atomic nuclei within a molecule resonate at different (radio) frequencies in the same applied static magnetic field, due to various local magnetic fields. The observation of such magnetic resonance frequencies of the nuclei present in a molecule makes it possible to determine essential chemical and structural information about the molecule.

The improvements of the NMR method benefited from the development of electromagnetic technology and advanced electronics and their introduction into civilian use. Originally as a research tool it was limited primarily to dynamic nuclear polarization, by the work of Anatole Abragam and Albert Overhauser, and to condensed matter physics, where it produced one of the first demonstrations of the validity of the BCS theory of superconductivity by the observation by Charles Slichter of the Hebel-Slichter effect. It soon showed its potential in organic chemistry, where NMR has become indispensable, and by the 1990s improvement in the sensitivity and resolution of NMR spectroscopy resulted in its broad use in analytical chemistry, biochemistry and materials science.

In the 2020s zero- to ultralow-field nuclear magnetic resonance (ZULF NMR), a form of spectroscopy that provides abundant analytical results without the need for large magnetic fields, was developed. It is combined with a special technique that makes it possible to hyperpolarize atomic nuclei.


## Theory of nuclear magnetic resonance

### Nuclear spins and magnets

All nucleons, that is neutrons and protons, composing any atomic nucleus, have the intrinsic quantum property of spin, an intrinsic angular momentum analogous to the classical angular momentum of a spinning sphere. The overall spin of the nucleus is determined by the spin quantum number *S*. If the numbers of both the protons and neutrons in a given nuclide are even then the system prefers to minimize its spin, giving *S* = 0, i.e. there is no overall spin. Then, just as electrons pair up in nondegenerate atomic orbitals, so do even numbers of protons or even numbers of neutrons (both of which are also spin-⁠1/2⁠ particles and hence fermions), giving zero overall spin.

However, an unpaired proton and unpaired neutron will have a lower energy when their spins are parallel, not anti-parallel. This parallel spin alignment of distinguishable particles does not violate the Pauli exclusion principle. The lowering of energy for parallel spins has to do with the quark structure of these two nucleons. As a result, the spin ground state for the deuteron (the nucleus of deuterium, the 2H isotope of hydrogen), which has only a proton and a neutron, corresponds to a spin value of **1**, *not of zero*. On the other hand, because of the Pauli exclusion principle, the tritium isotope of hydrogen must have a pair of anti-parallel spin neutrons (of total spin zero for the neutron spin-pair), plus a proton of spin ⁠1/2⁠. Therefore, the tritium total nuclear spin value is again ⁠1/2⁠, just like the simpler, abundant hydrogen isotope, 1H nucleus (the *proton*). The NMR absorption frequency for tritium is also similar to that of 1H. In many other cases of *non-radioactive* nuclei, the overall spin is also non-zero and may have a contribution from the orbital angular momentum of the unpaired nucleon. For example, the 27 Al nucleus has an overall spin value *S* = ⁠5/2⁠.

A non-zero spin ${\vec {S}}$ is associated with a non-zero magnetic dipole moment, ${\vec {\mu }}$ , via the relation ${\vec {\mu }}=\gamma {\vec {S}}$ where *γ* is the gyromagnetic ratio. Classically, this corresponds to the proportionality between the angular momentum and the magnetic dipole moment of a spinning charged sphere, both of which are vectors parallel to the rotation axis whose length increases proportional to the spinning frequency. It is the magnetic moment and its interaction with magnetic fields that allows the observation of NMR signal associated with transitions between nuclear spin levels during resonant RF irradiation or caused by Larmor precession of the average magnetic moment after resonant irradiation. Nuclides with even numbers of both protons and neutrons have zero nuclear magnetic dipole moment and hence do not exhibit NMR signal. For instance, 18 O is an example of a nuclide that produces no NMR signal, whereas 13 C, 31 P, 35 Cl and 37 Cl are nuclides that do exhibit NMR spectra. The last two nuclei have spin *S* > ⁠1/2⁠ and are therefore quadrupolar nuclei.

Electron spin resonance (ESR) is a related technique in which transitions between electronic rather than nuclear spin levels are detected. The basic principles are similar but the instrumentation, data analysis, and detailed theory are significantly different. Moreover, there is a much smaller number of molecules and materials with unpaired electron spins that exhibit ESR (or electron paramagnetic resonance (EPR)) absorption than those that have NMR absorption spectra. On the other hand, ESR has much higher signal per spin than NMR does.

### Values of spin angular momentum

Nuclear spin is an intrinsic angular momentum that is quantized. This means that the magnitude of this angular momentum is quantized (i.e. *S* can only take on a restricted range of values), and also that the x, y, and z-components of the angular momentum are quantized, being restricted to integer or half-integer multiples of *ħ*, the reduced Planck constant. The integer or half-integer quantum number associated with the spin component along the z-axis or the applied magnetic field is known as the magnetic quantum number, *m*, and can take values from +*S* to −*S*, in integer steps. Hence for any given nucleus, there are a total of 2*S* + 1 angular momentum states.

The *z*-component of the angular momentum vector ( ${\vec {S}}$ ) is therefore *Sz* = *mħ*. The *z*-component of the magnetic moment is simply: $\mu _{z}=\gamma S_{z}=\gamma m\hbar .$

#### Spin energy in a magnetic field

Consider nuclei with a spin of one-half, like 1 H, 13 C or 19 F. Each nucleus has two linearly independent spin states, with *m* = ⁠1/2⁠ or *m* = −⁠1/2⁠ (also referred to as spin-up and spin-down, or sometimes α and β spin states, respectively) for the z-component of spin. In the absence of a magnetic field, these states are degenerate; that is, they have the same energy. Hence the number of nuclei in these two states will be essentially equal at thermal equilibrium.

If a nucleus with spin is placed in a magnetic field, however, the two states no longer have the same energy as a result of the interaction between the nuclear magnetic dipole moment and the external magnetic field. The energy of a magnetic dipole moment ${\vec {\mu }}$ in a magnetic field **B**0 is given by: $E=-{\vec {\mu }}\cdot \mathbf {B} _{0}=-\mu _{x}B_{0x}-\mu _{y}B_{0y}-\mu _{z}B_{0z}.$

Usually the *z*-axis is chosen to be along **B**0, and the above expression reduces to: $E=-\mu _{\mathrm {z} }B_{0}\,,$ or alternatively: $E=-\gamma m\hbar B_{0}\,.$

As a result, the different nuclear spin states have different energies in a non-zero magnetic field. In less formal language, we can talk about the two spin states of a spin ⁠1/2⁠ as being *aligned* either with or against the magnetic field. If *γ* is positive (true for most isotopes used in NMR) then *m* = ⁠1/2⁠ ("spin up") is the lower energy state.

The energy difference between the two states is: $\Delta {E}=\gamma \hbar B_{0}\,,$ and this results in a small population bias favoring the lower energy state in thermal equilibrium. With more spins pointing up than down, a net spin magnetization along the magnetic field **B**0 results.

#### Precession of the spin magnetization

A central concept in NMR is the precession of the spin magnetization around the magnetic field at the nucleus, with the angular frequency $\omega =-\gamma B$ where $\omega =2\pi \nu$ relates to the oscillation frequency $\nu$ and *B* is the magnitude of the field. This means that the spin magnetization, which is proportional to the sum of the spin vectors of nuclei in magnetically equivalent sites (the expectation value of the spin vector in quantum mechanics), moves on a cone around the **B** field. This is analogous to the precessional motion of the axis of a tilted spinning top around the gravitational field. In quantum mechanics, $\omega$ is the *Bohr frequency* $\Delta {E}/\hbar$ of the $S_{x}$ and $S_{y}$ expectation values. Precession of non-equilibrium magnetization in the applied magnetic field **B**0 occurs with the Larmor frequency $\omega _{L}=2\pi \nu _{L}=-\gamma B_{0},$ without change in the populations of the energy levels because energy is constant (time-independent Hamiltonian).

#### Magnetic resonance and radio-frequency pulses

A perturbation of nuclear spin orientations from equilibrium will occur only when an oscillating magnetic field is applied whose frequency *ν*rf sufficiently closely matches the Larmor precession frequency *ν*L of the nuclear magnetization. The populations of the spin-up and -down energy levels then undergo Rabi oscillations, which are analyzed most easily in terms of precession of the spin magnetization around the effective magnetic field in a reference frame rotating with the frequency *ν*rf. The stronger the oscillating field, the faster the Rabi oscillations or the precession around the effective field in the rotating frame. After a certain time on the order of 2–1000 microseconds, a resonant RF pulse flips the spin magnetization to the transverse plane, i.e. it makes an angle of 90° with the constant magnetic field **B**0 ("90° pulse"), while after a twice longer time, the initial magnetization has been inverted ("180° pulse"). It is the transverse magnetization generated by a resonant oscillating field which is usually detected in NMR, during application of the relatively weak RF field in old-fashioned continuous-wave NMR, or after the relatively strong RF pulse in modern pulsed NMR.

#### Chemical shielding

It might appear from the above that all nuclei of the same nuclide (and hence the same *γ*) would resonate at exactly the same frequency but this is not the case. The most important perturbation of the NMR frequency for applications of NMR is the "shielding" effect of the shells of electrons surrounding the nucleus. Electrons, similar to the nucleus, are also charged and rotate with a spin to produce a magnetic field opposite to the applied magnetic field. In general, this electronic shielding reduces the magnetic field *at the nucleus* (which is what determines the NMR frequency). As a result, the frequency required to achieve resonance is also reduced.

This shift in the NMR frequency due to the electronic molecular orbital coupling to the external magnetic field is called chemical shift, and it explains why NMR is able to probe the chemical structure of molecules, which depends on the electron density distribution in the corresponding molecular orbitals. If a nucleus in a specific chemical group is shielded to a higher degree by a higher electron density of its surrounding molecular orbitals, then its NMR frequency will be shifted "upfield" (that is, a lower chemical shift), whereas if it is less shielded by such surrounding electron density, then its NMR frequency will be shifted "downfield" (that is, a higher chemical shift).

Unless the local symmetry of such molecular orbitals is very high (leading to "isotropic" shift), the shielding effect will depend on the orientation of the molecule with respect to the external field (**B**0). In solid-state NMR spectroscopy, magic angle spinning is required to average out this orientation dependence in order to obtain frequency values at the average or isotropic chemical shifts. This is unnecessary in conventional NMR investigations of molecules in solution, since rapid "molecular tumbling" averages out the chemical shift anisotropy (CSA). In this case, the "average" chemical shift (ACS) or isotropic chemical shift is often simply referred to as the chemical shift.

#### Radiation Damping

In 1949, Suryan first suggested that the interaction between a radiofrequency coil and a sample's bulk magnetization could explain why experimental observations of relaxation times differed from theoretical predictions. Building on this idea, Bloembergen and Pound further developed Suryan's hypothesis by mathematically integrating the Maxwell–Bloch equations, a process through which they introduced the concept of "radiation damping." Radiation damping (RD) in Nuclear Magnetic Resonance (NMR) is an intrinsic phenomenon observed in many high-field NMR experiments, especially relevant in systems with high concentrations of nuclei like protons or fluorine. RD occurs when transverse bulk magnetization from the sample, following a radio frequency pulse, induces an electromagnetic field (emf) in the receiver coil of the NMR spectrometer. This generates an oscillating current and a non-linear induced transverse magnetic field which returns the spin system to equilibrium faster than other mechanisms of relaxation.

RD can result in line broadening and measurement of a shorter spin-lattice relaxation time ( $T_{1}$ ). For instance, a sample of water in a 400 MHz NMR spectrometer will have $T_{RD}$ around 20 ms, whereas its $T_{1}$ is hundreds of milliseconds. This effect is often described using modified Bloch equations that include terms for radiation damping alongside the conventional relaxation terms. The longitudinal relaxation time of radiation damping ( $T_{RD}$ ) is given by the equation [1].

$T_{RD}={\frac {2}{\gamma \mu _{0}\eta QM_{0}}}$ [1]

where $\gamma$ is the gyromagnetic ratio, $\mu _{0}$ is the magnetic permeability, $M_{0}$ is the equilibrium magnetization per unit volume, $\eta$ is the filling factor of the probe which is the ratio of the probe coil volume to the sample volume enclosed, $Q={\frac {\omega L}{R}}$ is the quality factor of the probe, $\omega$ , L , and R are the resonance frequency, inductance, and resistance of the coil, respectively. The quantification of line broadening due to radiation damping can be determined by measuring the $\Delta v_{\frac {1}{2}}$ and use equation [2].

$T_{RD}^{-1}={\frac {\pi }{0.8384}}\Delta v_{\frac {1}{2}}$ [2]

Radiation damping in NMR is influenced significantly by system parameters. It is notably more prominent in systems where the NMR probe possesses a high quality factor ( Q ) and a high filling factor, resulting in a strong coupling between the probe coil and the sample. The phenomenon is also impacted by the concentration of the nuclei within the sample and their magnetic moments, which can intensify the effects of radiation damping. The strength of the magnetic field is inversely proportional to the lifetime of RD. The impact of radiation damping on NMR signals is multifaceted. It can accelerate the decay of the NMR signal faster than intrinsic relaxation processes would suggest. This acceleration can complicate the interpretation of NMR spectra by causing broadening of spectral lines, distorting multiplet structures, and introducing artifacts, especially in high-resolution NMR scenarios. Such effects make it challenging to obtain clear and accurate data without considering the influence of radiation damping. To mitigate these effects, various strategies are employed in NMR spectroscopy. These methods majorly stem from hardware or software. Hardware modifications including RF feed-circuit and Q-factor switches reduce the feedback loop between the sample magnetization and the electromagnetic field induced by the coil and function successfully. Other approaches such as designing selective pulse sequences also effectively manage the fields induced by radiation damping. These approaches aim to control and limit the disruptive effects of radiation damping during NMR experiments and all approaches are successful in eliminating RD to a fairly large extent. Overall, understanding and managing radiation damping is crucial for obtaining high-quality NMR data, especially in modern high-field spectrometers where the effects can be significant due to the increased sensitivity and resolution.

### Relaxation

The process of population relaxation refers to nuclear spins that return to thermodynamic equilibrium in the magnet. This process is also called *T*1, "spin-lattice" or "longitudinal magnetic" relaxation, where *T*1 refers to the mean time for an individual nucleus to return to its thermal equilibrium state of the spins. After the nuclear spin population has relaxed, it can be probed again, since it is in the initial, equilibrium (mixed) state.

The precessing nuclei can also fall out of alignment with each other and gradually stop producing a signal. This is called *T*2, "spin-spin" or *transverse relaxation*. Because of the difference in the actual relaxation mechanisms involved (for example, intermolecular versus intramolecular magnetic dipole-dipole interactions), *T*1 is usually (except in rare cases) longer than *T*2 (that is, slower spin-lattice relaxation, for example because of smaller dipole-dipole interaction effects). In practice, the value of *T*2*, which is the actually observed decay time of the observed NMR signal, or free induction decay (to ⁠1/*e*⁠ of the initial amplitude immediately after the resonant RF pulse), also depends on the static magnetic field inhomogeneity, which may be quite significant. (There is also a smaller but significant contribution to the observed FID shortening from the RF inhomogeneity of the resonant pulse). In the corresponding FT-NMR spectrum—meaning the Fourier transform of the free induction decay— the width of the NMR signal in frequency units is inversely related to the *T*2* time. Thus, a nucleus with a long *T*2* relaxation time gives rise to a very sharp NMR peak in the FT-NMR spectrum for a very homogeneous ("well-shimmed") static magnetic field, whereas nuclei with shorter *T*2* values give rise to broad FT-NMR peaks even when the magnet is shimmed well. Both *T*1 and *T*2 depend on the rate of molecular motions as well as the gyromagnetic ratios of both the resonating and their strongly interacting, next-neighbor nuclei that are not at resonance.

A Hahn echo decay experiment can be used to measure the dephasing time, as shown in the animation. The size of the echo is recorded for different spacings of the two pulses. This reveals the decoherence that is not refocused by the 180° pulse. In simple cases, an exponential decay is measured which is described by the *T*2 time.


## NMR spectroscopy

NMR spectroscopy is one of the principal techniques used to obtain physical, chemical, electronic and structural information about molecules due to the chemical shift of the resonance frequencies of the nuclear spins in the sample. Peak splittings due to J- or dipolar couplings between nuclei are also useful. NMR spectroscopy can provide detailed and quantitative information on the functional groups, topology, dynamics and three-dimensional structure of molecules in solution and the solid state. Since the area under an NMR peak is usually proportional to the number of spins involved, peak integrals can be used to determine composition quantitatively. A common methodology involves an extended delay time between each spectral scan (generally, 5 times the longest *T*1 in a complex mixture for a 90 degree pulsing angle, where *T*1 can be calculated using techniques such as FLIPS). This lets nuclei relax completely, allowing integrals to be more accurate for quantitation.

Structure and molecular dynamics can be studied (with or without "magic angle" spinning (MAS)) by NMR of quadrupolar nuclei (that is, with spin *S* > ⁠1/2⁠) even in the presence of magnetic "dipole-dipole" interaction broadening (or simply, dipolar broadening), which is always much smaller than the quadrupolar interaction strength because it is a magnetic vs. an electric interaction effect.

Additional structural and chemical information may be obtained by performing double-quantum NMR experiments for pairs of spins or quadrupolar nuclei such as 2 H. Furthermore, nuclear magnetic resonance is one of the techniques that has been used to design quantum automata, and also build elementary quantum computers.

### Continuous-wave (CW) spectroscopy

In the first few decades of nuclear magnetic resonance, spectrometers used a technique known as continuous-wave (CW) spectroscopy, where the transverse spin magnetization generated by a weak oscillating magnetic field is recorded as a function of the oscillation frequency or static field strength *B*0. When the oscillation frequency matches the nuclear resonance frequency, the transverse magnetization is maximized and a peak is observed in the spectrum. Although NMR spectra could be, and have been, obtained using a fixed constant magnetic field and sweeping the frequency of the oscillating magnetic field, it was more convenient to use a fixed frequency source and vary the current (and hence magnetic field) in an electromagnet to observe the resonant absorption signals. This is the origin of the counterintuitive, but still common, "high field" and "low field" terminology for low frequency and high frequency regions, respectively, of the NMR spectrum.

As of 1996, CW instruments were still used for routine work because the older instruments were cheaper to maintain and operate, often operating at 60 MHz with correspondingly weaker (non-superconducting) electromagnets cooled with water rather than liquid helium. One radio coil operated continuously, sweeping through a range of frequencies, while another orthogonal coil, designed not to receive radiation from the transmitter, received signals from nuclei that reoriented in solution. As of 2014, low-end refurbished 60 MHz and 90 MHz systems were sold as FT-NMR instruments, and in 2010 the "average workhorse" NMR instrument was configured for 300 MHz.

CW spectroscopy is inefficient in comparison with Fourier analysis techniques (see below) since it probes the NMR response at individual frequencies or field strengths in succession. Since the NMR signal is intrinsically weak, the observed spectrum suffers from a poor signal-to-noise ratio. This can be mitigated by signal averaging, i.e. adding the spectra from repeated measurements. While the NMR signal is the same in each scan and so adds linearly, the random noise adds more slowly – proportional to the square root of the number of spectra added (see random walk). Hence the overall signal-to-noise ratio increases as the square-root of the number of spectra measured. However, monitoring an NMR signal at a single frequency as a function of time may be better suited for kinetic studies than pulsed Fourier-transform NMR spectrosocopy.

### Fourier-transform spectroscopy

Most applications of NMR involve full NMR spectra, that is, the intensity of the NMR signal as a function of frequency. Early attempts to acquire the NMR spectrum more efficiently than simple CW methods involved illuminating the target simultaneously with more than one frequency. A revolution in NMR occurred when short radio-frequency pulses began to be used, with a frequency centered at the middle of the NMR spectrum. In simple terms, a short pulse of a given "carrier" frequency "contains" a range of frequencies centered about the carrier frequency, with the range of excitation (bandwidth) being inversely proportional to the pulse duration, i.e. the Fourier transform of a short pulse contains contributions from all the frequencies in the neighborhood of the principal frequency. The restricted range of the NMR frequencies for most light spin-⁠1/2⁠ nuclei made it relatively easy to use short (1 - 100 microsecond) radio frequency pulses to excite the entire NMR spectrum.

Applying such a pulse to a set of nuclear spins simultaneously excites all the single-quantum NMR transitions. In terms of the net magnetization vector, this corresponds to tilting the magnetization vector away from its equilibrium position (aligned along the external magnetic field). The out-of-equilibrium magnetization vector then precesses about the external magnetic field vector at the NMR frequency of the spins. This oscillating magnetization vector induces a voltage in a nearby pickup coil, creating an electrical signal oscillating at the NMR frequency. This signal is known as the free induction decay (FID), and it contains the sum of the NMR responses from all the excited spins. In order to obtain the frequency-domain NMR spectrum (NMR absorption intensity vs. NMR frequency) this time-domain signal (intensity vs. time) must be Fourier transformed. Fortunately, the development of Fourier transform (FT) NMR coincided with the development of digital computers and the digital fast Fourier transform (FFT). Fourier methods can be applied to many types of spectroscopy. Richard R. Ernst was one of the pioneers of pulsed NMR and won a Nobel Prize in chemistry in 1991 for his work on Fourier Transform NMR and his development of multi-dimensional NMR spectroscopy.

### Multi-dimensional NMR spectroscopy

The use of pulses of different durations, frequencies, or shapes in specifically designed patterns or *pulse sequences* allows production of a spectrum that contains many different types of information about the molecules in the sample. In multi-dimensional nuclear magnetic resonance spectroscopy, there are at least two pulses: one leads to the directly detected signal and the others affect the starting magnetization and spin state prior to it. The full analysis involves repeating the sequence with the pulse timings systematically varied in order to probe the oscillations of the spin system are point by point in the time domain. Multidimensional Fourier transformation of the multidimensional time signal yields the multidimensional spectrum. In two-dimensional nuclear magnetic resonance spectroscopy (2D-NMR), there will be one systematically varied time period in the sequence of pulses, which will modulate the intensity or phase of the detected signals. In 3D-NMR, two time periods will be varied independently, and in 4D-NMR, three will be varied.

There are many such experiments. In some, fixed time intervals allow (among other things) magnetization transfer between nuclei and, therefore, the detection of the kinds of nuclear–nuclear interactions that allowed for the magnetization transfer. Interactions that can be detected are usually classified into two kinds. There are *through-bond* and *through-space* interactions. Through-bond interactions relate to structural connectivity of the atoms and provide information about which ones are directly connected to each other, connected by way of a single other intermediate atom, etc. Through-space interactions relate to actual geometric distances and angles, including effects of dipolar coupling and the nuclear Overhauser effect.

Although the fundamental concept of 2D-FT NMR was proposed by Jean Jeener from the Free University of Brussels at an international conference, this idea was largely developed by Richard Ernst, who won the 1991 Nobel prize in Chemistry for his work in FT NMR, including multi-dimensional FT NMR, and especially 2D-FT NMR of small molecules. Multi-dimensional FT NMR experiments were then further developed into powerful methodologies for studying molecules in solution, in particular for the determination of the structure of biopolymers such as proteins or even small nucleic acids.

In 2002 Kurt Wüthrich shared the Nobel Prize in Chemistry (with John Bennett Fenn and Koichi Tanaka) for his work with protein FT NMR in solution.

### Solid-state NMR spectroscopy

This technique complements X-ray crystallography in that it is frequently applicable to molecules in an amorphous or liquid-crystalline state, whereas crystallography, as the name implies, is performed on molecules in a crystalline phase. In electronically conductive materials, the Knight shift of the resonance frequency can provide information on the mobile charge carriers. Though nuclear magnetic resonance is used to study the structure of solids, extensive atomic-level structural detail is more challenging to obtain in the solid state. Due to broadening by chemical shift anisotropy (CSA) and dipolar couplings to other nuclear spins, without special techniques such as MAS or dipolar decoupling by RF pulses, the observed spectrum is often only a broad Gaussian band for non-quadrupolar spins in a solid.

Professor Raymond Andrew at the University of Nottingham in the UK pioneered the development of high-resolution solid-state nuclear magnetic resonance. He was the first to report the introduction of the MAS (magic angle sample spinning; MASS) technique that allowed him to achieve spectral resolution in solids sufficient to distinguish between chemical groups with either different chemical shifts or distinct Knight shifts. In MASS, the sample is spun at several kilohertz around an axis that makes the so-called magic angle *θ*m (which is ~54.74°, where 3cos2*θ*m-1 = 0) with respect to the direction of the static magnetic field **B**0; as a result of such magic angle sample spinning, the broad chemical shift anisotropy bands are averaged to their corresponding average (isotropic) chemical shift values. Correct alignment of the sample rotation axis as close as possible to *θ*m is essential for cancelling out the chemical-shift anisotropy broadening. There are different angles for the sample spinning relative to the applied field for the averaging of electric quadrupole interactions and paramagnetic interactions, correspondingly ~30.6° and ~70.1°. In amorphous materials, residual line broadening remains since each segment is in a slightly different environment, therefore exhibiting a slightly different NMR frequency.

Line broadening or splitting by dipolar or J-couplings to nearby 1H nuclei is usually removed by radio-frequency pulses applied at the 1H frequency during signal detection. The concept of cross polarization developed by Sven Hartmann and Erwin Hahn was utilized in transferring magnetization from protons to less sensitive nuclei by M.G. Gibby, Alex Pines and John S. Waugh. Then, Jake Schaefer and Ed Stejskal demonstrated the powerful use of cross polarization under MAS conditions (CP-MAS) and proton decoupling, which is now routinely employed to measure high resolution spectra of low-abundance and low-sensitivity nuclei, such as carbon-13, silicon-29, or nitrogen-15, in solids. Significant further signal enhancement can be achieved by dynamic nuclear polarization from unpaired electrons to the nuclei, usually at temperatures near 110 K.

### Sensitivity

Because the intensity of nuclear magnetic resonance signals and, hence, the sensitivity of the technique depends on the strength of the magnetic field, the technique has also advanced over the decades with the development of more powerful magnets. Advances made in audio-visual technology have also improved the signal-generation and processing capabilities of newer instruments.

As noted above, the sensitivity of nuclear magnetic resonance signals is also dependent on the presence of a magnetically susceptible nuclide and, therefore, either on the natural abundance of such nuclides or on the ability of the experimentalist to artificially enrich the molecules, under study, with such nuclides. The most abundant naturally occurring isotopes of hydrogen and phosphorus (for example) are both magnetically susceptible and readily useful for nuclear magnetic resonance spectroscopy. In contrast, carbon and nitrogen have useful isotopes but which occur only in very low natural abundance.

Other limitations on sensitivity arise from the quantum-mechanical nature of the phenomenon. For quantum states separated by energy equivalent to radio frequencies, thermal energy from the environment causes the populations of the states to be close to equal. Since incoming radiation is equally likely to cause stimulated emission (a transition from the upper to the lower state) as absorption, the NMR effect depends on an excess of nuclei in the lower states. Several factors can reduce sensitivity, including:

- Increasing temperature, which evens out the Boltzmann population of states. Conversely, low temperature NMR can sometimes yield better results than room-temperature NMR, providing the sample remains liquid.
- Saturation of the sample with energy applied at the resonant radiofrequency. This manifests in both CW and pulsed NMR; in the first case (CW) this happens by using too much continuous power that keeps the upper spin levels completely populated; in the second case (pulsed), each pulse (that is at least a 90° pulse) leaves the sample saturated, and four to five times the (longitudinal) relaxation time (5*T*1) must pass before the next pulse or pulse sequence can be applied. For single pulse experiments, shorter RF pulses that tip the magnetization by less than 90° can be used, which loses some intensity of the signal, but allows for shorter *recycle delays*. The optimum there is called an *Ernst angle*, after the Nobel laureate. Especially in solid state NMR, or in samples containing very few nuclei with spin (diamond with the natural 1% of carbon-13 is especially troublesome here) the longitudinal relaxation times can be on the range of hours, while for proton-NMR they are often in the range of one second.
- Non-magnetic effects, such as electric-quadrupole coupling of spin-1 and spin-⁠3/2⁠ nuclei with their local environment, which broaden and weaken absorption peaks. 14 N, an abundant spin-1 nucleus, is difficult to study for this reason. High resolution NMR instead probes molecules using the rarer 15 N isotope, which has spin-⁠1/2⁠.

### Isotopes

Many isotopes of chemical elements can be used for NMR analysis.

**Commonly used nuclei:**

- 1 H, the most commonly used spin-⁠1/2⁠ nucleus in NMR investigations, has been studied using many forms of NMR. Hydrogen is highly abundant, especially in biological systems. It is the nucleus providing the strongest NMR signal (apart from 3 H, which is not commonly used due to its instability and radioactivity). Proton NMR has a narrow chemical-shift range but gives sharp signals in solution state. Fast acquisition of quantitative spectra (with peak integrals in stoichiometric ratios) is possible due to short relaxation time. The 1 H nucleus has provided the sole diagnostic signal for clinical magnetic resonance imaging (MRI).
- 2 H, a spin-1 nucleus, is commonly utilized to provide a signal-free medium in the form of deuterated solvents for proton NMR, to avoid signal interference from hydrogen-containing solvents in measurement of 1 H NMR of solutes. It is also used in determining the behavior of lipids in lipid membranes and other solids or liquid crystals as it is a relatively non-perturbing label which can selectively replace 1 H. Alternatively, 2 H can be detected in media specially labeled with 2 H. Deuterium resonance is commonly used in high-resolution NMR spectroscopy to monitor drift of the magnetic field strength (lock) and to monitor the homogeneity of the external magnetic field.
- 3 He is very sensitive to NMR. It exists at a very low concentration in natural helium and can be purified from 4 He. It is used mainly in studies of endohedral fullerenes, where its chemical inertness is beneficial to ascertaining the structure of the entrapping fullerene.
- 11 B is more sensitive than 10 B and yields sharper signals. The nuclear spin of 10B is 3 and that of 11B is ⁠3/2⁠. Quartz tubes must be used because borosilicate glass interferes with measurement.
- 13 C, a spin-⁠1/2⁠ nucleus, is widely used, despite its relative paucity in naturally occurring carbon (approximately 1.1%). It is stable to nuclear decay. Since there is a low percentage in natural carbon, spectrum acquisition on samples which have not been enriched in 13 C takes a long time. Frequently used for labeling of compounds in synthetic and metabolic studies. Has low sensitivity and moderately wide chemical shift range, yields sharp signals. Low percentage makes it useful by preventing spin–spin couplings and makes the spectrum appear less crowded. Slow relaxation of 13C not bonded to hydrogen means that spectra are not integrable unless long acquisition times are used.
- 14 N, spin-1, is a medium sensitivity nucleus with wide chemical shift range. Its large quadrupole moment interferes with acquisition of high resolution spectra, limiting usefulness to smaller molecules and functional groups with a high degree of symmetry such as in the head-groups of lipids.
- 15 N, spin-⁠1/2⁠, is relatively commonly used. Can be used for isotopically labeling compounds. Very insensitive but yields sharp signals. Low percentage in natural nitrogen together with low sensitivity requires high concentrations or expensive isotope enrichment.
- 17 O, spin-⁠5/2⁠, low sensitivity and very low natural abundance (0.037%), wide chemical shift range (up to 2000 ppm). Its quadrupole moment causes line broadening. Used in metabolic and biochemical studies of chemical equilibria.
- 19 F, spin-⁠1/2⁠, relatively commonly measured. Sensitive, yields sharp signals, has a wide chemical shift range.
- 31 P, spin-⁠1/2⁠, 100% of natural phosphorus. Medium sensitivity, wide chemical shift range, yields sharp lines. Spectra tend to have a moderate level of noise. Used in biochemical studies and in coordination chemistry with phosphorus-containing ligands.
- 35 Cl and 37 Cl, spin-⁠3/2⁠, broad signal. 35 Cl is significantly more sensitive, preferred over 37 Cl despite its slightly broader signal. Organic chlorides yield very broad signals. Its use is limited to inorganic and ionic chlorides and very small organic molecules.
- 43 Ca, spin-⁠7/2⁠, relatively small quadrupole moment, moderately sensitive, very low natural abundance. Used in biochemistry to study calcium binding to DNA, proteins, etc.
- 195 Pt, used in studies of catalysts and complexes.

**Other nuclei** (usually used in the studies of their complexes and chemical bonding, or to detect presence of the element):

- 6 Li, 7 Li
- 9 Be
- 19 F
- 21 Ne
- 23 Na
- 25 Mg
- 27 Al
- 29 Si
- 31 P
- 33 S
- 39 K, 40 K, 41 K
- 45 Sc
- 47 Ti, 49 Ti
- 50 V, 51 V
- 53 Cr
- 55 Mn
- 57 Fe
- 59 Co
- 61 Ni
- 63 Cu, 65 Cu
- 67 Zn
- 69 Ga, 71 Ga
- 73 Ge
- 75 As
- 77 Se
- 81 Br
- 87 Rb
- 87 Sr
- 95 Mo
- 109 Ag
- 113 Cd
- 119 Sn
- 125 Te
- 127 I
- 133 Cs
- 135 Ba, 137 Ba
- 139 La
- 183 W
- 199 Hg
