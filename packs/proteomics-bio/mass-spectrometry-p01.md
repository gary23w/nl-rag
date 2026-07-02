---
title: "Mass spectrometry (part 1/2)"
source: https://en.wikipedia.org/wiki/Mass_spectrometry
domain: proteomics-bio
license: CC-BY-SA-4.0
tags: proteomics analysis, mass spectrometry proteomics, protein identification, two dimensional gel
fetched: 2026-07-02
part: 1/2
---

# Mass spectrometry

**Mass spectrometry** (**MS**) is an analytical technique that is used to measure the mass-to-charge ratio of ions. The results are presented as a *mass spectrum*, a plot of intensity as a function of the mass-to-charge ratio. These spectra are used to determine the elemental or isotopic signature of a sample, the masses of particles and of molecules, and to elucidate the chemical identity or structure of molecules and other chemical compounds. Mass spectrometry is used in many different fields and is applied to pure samples as well as complex mixtures.

In a typical MS procedure, a sample, which may be solid, liquid, or gaseous, is ionized, for example by bombarding it with a beam of electrons. This may cause some of the sample's molecules to break up into positively charged fragments or simply become positively charged without fragmenting. These ions (fragments) are then separated according to their mass-to-charge ratio, for example by accelerating them and subjecting them to an electric or magnetic field: ions of the same mass-to-charge ratio will undergo the same amount of deflection. The ions are detected by a mechanism capable of detecting charged particles, such as an electron multiplier. Results are displayed as spectra of the signal intensity of detected ions as a function of the mass-to-charge ratio. The atoms or molecules in the sample can be identified by correlating known masses (e.g. an entire molecule) to the identified masses or through a characteristic fragmentation pattern.


## History

In 1886, Eugen Goldstein observed rays in gas discharges under low pressure that traveled away from the anode and through channels in a perforated cathode, opposite to the direction of negatively charged cathode rays (which travel from cathode to anode). Goldstein called these positively charged anode rays "Kanalstrahlen"; the standard translation of this term into English is "canal rays". Wilhelm Wien found that strong electric or magnetic fields deflected the canal rays and, in 1899, constructed a device with perpendicular electric and magnetic fields that separated the positive rays according to their charge-to-mass ratio (*Q/m*). Wien found that the charge-to-mass ratio depended on the nature of the gas in the discharge tube. English scientist J. J. Thomson later improved on the work of Wien by reducing the pressure to create the mass spectrograph.

The word *spectrograph* had become part of the international scientific vocabulary by 1884. Early *spectrometry* devices that measured the mass-to-charge ratio of ions were called *mass spectrographs* which consisted of instruments that recorded a spectrum of mass values on a photographic plate. A *mass spectroscope* is similar to a *mass spectrograph* except that the beam of ions is directed onto a phosphor screen. A mass spectroscope configuration was used in early instruments when it was desired that the effects of adjustments be quickly observed. Once the instrument was properly adjusted, a photographic plate was inserted and exposed. The term mass spectroscope continued to be used even though the direct illumination of a phosphor screen was replaced by indirect measurements with an oscilloscope. The use of the term *mass spectroscopy* is now discouraged due to the possibility of confusion with light spectroscopy. Mass spectrometry is often abbreviated as *mass-spec* or simply as *MS*.

Modern techniques of mass spectrometry were devised by Arthur Jeffrey Dempster and F.W. Aston in 1918 and 1919 respectively.

Sector mass spectrometers known as calutrons were developed by Ernest O. Lawrence and used for separating the isotopes of uranium during the Manhattan Project. Calutron mass spectrometers were used for uranium enrichment at the Oak Ridge, Tennessee Y-12 plant established during World War II.

In 1989, half of the Nobel Prize in Physics was awarded to Hans Dehmelt and Wolfgang Paul for the development of the ion trap technique in the 1950s and 1960s.

In 2002, the Nobel Prize in Chemistry was awarded to John Bennett Fenn for the development of electrospray ionization (ESI) and Koichi Tanaka for the development of soft laser desorption and their application to the ionization of biological macromolecules, especially proteins.


## Components

A mass spectrometer consists of 5 components: **sample inlet**, **ion source** (or **ionizer**), **mass analyzer**, **detector**, data system. Each component can be varied somewhat independently from the other components, and the full mass spectrometer itself can be included as a component in an analysis pipeline, allowing great flexibility.

The sample inlet prepares the sample to be analyzed in a suitable state.

The ion source takes samples from the sample inlet, converts a portion of the sample into a stream of ions, and outputs it to the mass analyzer. There is a wide variety of ionization techniques, depending on the phase (solid, liquid, gas) of the sample and the efficiency of various ionization mechanisms for the unknown species. An extraction system removes ions from the sample, which are then targeted into the mass analyzer.

The mass analyzer takes an input stream of ions and separates ("analyzes") its constituent ions according to their *m/z*, the mass-to-charge ratio.

The detector measures the value of an indicator quantity and thus provides data for calculating the abundances of each ion present. Some detectors also give spatial information, e.g., a multichannel plate.

### Illustrative example

The following describes the operation of a simple mass spectrometer that uses sector type. Other types are treated below.

Consider a sample of sodium chloride (table salt). In the ion source, the sample is vaporized (turned into gas) and ionized (transformed into electrically charged particles) into sodium (Na+) and chloride (Cl−) ions.

Sodium atoms and ions are monoisotopic, with a mass of about 23 daltons (symbol: Da or older symbol: u). Chloride atoms and ions come in two stable isotopes with masses of approximately 35 u (at a natural abundance of about 75 percent) and approximately 37 u (at a natural abundance of about 25 percent).

The analyzer part of the spectrometer contains electric and magnetic fields, which exert forces on ions traveling through these fields. The speed of a charged particle may be increased or decreased while passing through the electric field, and its direction may be altered by the magnetic field.

The magnitude of the deflection of the moving ion's trajectory depends on its mass-to-charge ratio. Lighter ions are deflected by the magnetic force to a greater degree than heavier ions (based on Newton's second law of motion, *F* = *ma*).

The streams of magnetically sorted ions pass from the analyzer to the detector, which records the relative abundance of each ion type. This information is used to determine the chemical element composition of the original sample (i.e. that both sodium and chlorine are present in the sample) and the isotopic composition of its constituents (the ratio of 35Cl to 37Cl).


## Sample inlet

The sample inlet provides a stream of neutral molecules, so that the ion source can ionize them. There are several classes.

The classical design produces the stream of molecules in the form of a low-pressure gas. It is low-pressure, so that molecules within the stream does not frequently collide with each other. Ions must travel without frequent collisions, because the instrument separates ions by their motion in electric and magnetic fields. Collisions disturb that motion.

Despite being low-pressure, the sample stream is still at a much higher pressure than the rest of the system, which is held in a greater vacuum. Consequently, the sample stream can only enter the ion source chamber via a small pinhole, called a **molecular leak**.

If the sample itself is already a gas, then the sample inlet can simply be a gas inlet with pressure valve. If the sample is a volatile liquid or solid, then it can simply be placed in a chamber, vacuum-pumped to a low pressure. If the sample is not sufficiently volatile, the sample inlet can be fitted within an oven. Be careful not to decompose the sample.

If the sample is too nonvolatile to be turned into a low-pressure gas, then one can use a **direct probe**. The direct probe is a probe with a tip of thin wire loop, pin, or a capillary tube. The sample is placed in the tip. The probe is inserted through a vacuum lock into the ionization chamber, so that the tip is close to the ion source. The probe can be heated to increase vapor pressure further. Such a system is effective for samples with vapor pressures lower than $10^{-9}$ mmHg at room temperature.

The sample can be prepared by an earlier analyzer. For example, it can simply be the gaseous output of a gas chromatography machine as in GC-MS, or the liquid output of a high-performance liquid chromatography machine, as in HPLC-MS.

The recently developed "atmospheric pressure ionization" techniques allow us to entirely dispense with the sample inlet.


## Ion source

The ion source is the part of the mass spectrometer that transforms the sample from the sample inlet into a stream of ions. There are many techniques with various dimensions for tradeoffs between different choices of ion sources, in terms of monetary cost, accuracy, precision, compatibility with other stages of spectroscopy, ease of use, etc.

For example, electron ionization (EI) gives a high degree of fragmentation, yielding highly detailed mass spectra which when skilfully analysed can provide important information for structural elucidation/characterisation and facilitate identification of unknown compounds by comparison to mass spectral libraries obtained under identical operating conditions. However, EI is not suitable for coupling to HPLC, i.e. LC-MS, since at atmospheric pressure, the filaments used to generate electrons burn out rapidly. Thus EI is coupled predominantly with GC, i.e. GC-MS, where the entire system is under high vacuum.

Two techniques often used with liquid and solid biological samples include electrospray ionization (invented by John Fenn) and matrix-assisted laser desorption/ionization (MALDI, initially developed as a similar technique Soft Laser Desorption) by K. Tanaka for which a Nobel Prize was awarded and as MALDI by M. Karas and F. Hillenkamp).

### Hard ionization and soft ionization

Hard ionization techniques are those that impart high quantities of residual internal energy in the subject molecule, even after ionization. Part of the energy would be dissipated by rupturing chemical bonds within the ion, producing many fragmentary radical ions. The resultant ions tend to have *m/z* lower than the molecular ion (other than in the case of proton transfer and not including isotope peaks). The most common example of hard ionization is electron ionization (EI).

The radical ions produced after the first ionization are called second-generation product ions. The products are then directed towards the mass analyzer by a repeller electrode. The ionization process often follows predictable cleavage reactions that give rise to fragment ions which, following detection and signal processing, convey structural information about the analyte.

Conversely, soft ionization techniques are those that impart little residual energy onto the subject molecule and as such result in little fragmentation. Examples include fast atom bombardment (FAB), chemical ionization (CI), atmospheric-pressure chemical ionization (APCI), atmospheric-pressure photoionization (APPI), electrospray ionization (ESI), desorption electrospray ionization (DESI), and matrix-assisted laser desorption/ionization (MALDI).

### Electron ionization

In electron ionization (EI), energetic electrons are produced by a hot cathode: a wire filament heated by running electric current through it, producing energetic electrons by thermionic emission. The electrons are then accelerated towards an anode. The voltage difference between the cathode and the anode determines the energy of the electron stream.

Most organic compounds have ionization energy 8-15 eV, but empirically, the efficiency of ionization is too low unless the electron beam has an energy of 50-70 eV per electron. The spectral features, including fragmentation patterns, depend on the energy setting. Conventionally for EI, the electron energy is standardized to be exactly 70 eV. Consequently, if one wishes to compare their EI-MS results against standard databases, or produce results that can be added to standard databases, one must standardize their EI electron energy to 70 eV.

EI accepts as input a stream of gas from the molecular leak. The gas stream crosses the electron stream perpendicularly. The collision ionizes the gas stream. The ion stream then is accerelated by a succession of electrodes. Typically an ion carrying 1 e would be accelerated to 1-10 keV.

EI has many benefits for routine mass spectrometry of small organic molecules. It is cheap and robust, with reproducible spectrograms. Databases for EI spectrograms are widely available and covers many such molecules.

EI is unsuited for large molecules, such as most biomolecules. It is a hard technique, which tends to break down large molecule ions during flight, since large molecules are particularly easy to fragment. Furthermore, large molecules are hard to volatilize without being degraded by heat.

### Chemical ionization

In chemical ionization (CI), the analyte is ionized by a chemical reaction with an ionized reagent gas (itself ionized by some technique, such as by EI). The analyte gas and the reagent gas intersect, and react. The reaction then produces ionized analyte fragments by various mechanisms, including proton transfer, electron transfer, and adduct formation. The ion is then accelerated electrostatically, as in EI. CI ion sources are similar to EI sources, and most modern mass spectrometers can switch from EI to CI mode in minutes.

To ensure efficiency, the amount of reagent is much higher than the analyte. Consequently, a large amount of reagent ions would end up in the mass analyzer. This is usually handled by only measuring the part of the spectrogram with *m/z* above those of the main species in the reagent ion stream.

Common ionizing reagents for CI-MS include methane, ammonia, isobutane, and methanol. The proton affinity of the reagent gas and of the sample should be matched to ensure efficient ionization. If the proton affinity of the reagent gas is too high, ionization is inefficient. If the proton affinity of the reagent gas is too low, fragmentation is excessive.

For example:

- When the reagent is methane, the predominant reaction is proton transfer M + CH5+ → (MH)+ + CH4.
- When the reagent is ammonium, the predominant reaction is proton transfer M + NH4+ → (MH)+ + NH3.
- When the reagent is isobutane, the reaction may be proton transfer M + (CH3)3C+ → (MH)+ + (CH3)2C=CH2 or adduct formation M + (CH3)3C+ → (M · C(CH3)3)+.
- CI can also produce negatively charged analyte ions by proton abstraction or adduct formation. For example, ionized NF3 contains F−, which abstracts proton.

| Reagent gas | Proton affinity (kcal/mole) | Reagent ion(s) | Analyte ion(s) | Comments |
|---|---|---|---|---|
| H2 | 101 | H+3 | (MH)+ | Significant fragmentation |
| CH4 | 132 | CH+5, C2H+5 | (MH)+, (M · C2H5)+ | Some fragmentation, can form adducts |
| NH3 | 204 | NH+4 | (MH)+, (M · NH4)+ | Selective ionization, little fragmentation, can form adducts |
| (CH3)3CH | 196 | (CH3)3C+ | (MH)+, (M · C(CH3)3)+ | Selective protonation, little fragmentation. |
| CH3OH | 182 | CH3OH+2 | (MH)+ |   |
| CH3CN | 188 | CH3CNH+ | (MH)+ |   |

### Spray ionization

Electrospray ionization (ESI) and thermospray ionization (TSI) are suited for high molecular weight biomolecules and other labile or nonvolatile compounds, and especially in a LC-MS system. In both cases, the analyte is in a solution. The solution is sprayed out, by either electrospraying or thermospraying, into a stream of mist, which then evaporates into an ion stream. TSI has been supplanted by ESI for most purposes.

In TSI, the solution enters a heated capillary, producing a spray of droplets. The solvent evaporates, leaving ionized analytes. The ionization can occur due to 3 possible processes:

- The analyte is already in an ion form in the solution, and it is desorbed as the solvent evaporates.
- Acid-base transfer. If the solvent is a buffer solution, then the analyte can ionize by exchanging a proton with the buffer. This form of ionization is well-suited for LC-MS, since the liquid used in liquid chromatography already is a buffer solution.
- Plasmaspray ionization or filament-on operation. The solvent in the spray is electron-ionized by an energetic electron beam. The ionized solvent then chemically ionizes the analyte.

In ESI, the solution enters a capillary held at a high voltage (usually 2-5 kV), producing an electrospray into a heated chamber against a counterflow of a drying gas (usually nitrogen). This evaporates solvent molecules. The charge density increases on a droplet as it evaporates, until the electrostatic energy overcomes the surface tension energy, exploding the droplet. This process repeats, ending with an ion stream without the solvent. The ionization can occur by:

- Charge concentration in the droplets during evaporation.
- Electrochemical processes stemming from the electrostatic potential of the capillary.

Unlike in TSI, the analyte ions produced by ESI may carry a different amount of charge than the same analyte would carry in the solution. That is, an analyte that is naturally occurring as M+ in the solution may end up becoming a stream of ions containing a mixture of M+, M2+, M3+, etc. A large molecule can carry much charge. Typical proteins can carry many protons due to the presence of basic amino acid side chains, resulting in peaks at *m/z* = 600–2000 for proteins with a molecular weight ~200,000 Da. This is convenient, since it means the ion would not exceed the *m/z* limits on typical mass analyzers.

### Desorption ionization

Desorption ionization (DI) is a family of ionization techniques. The main examples are secondary-ion mass spectrometry (SIMS), fast atom bombardment (FAB), and matrix-assisted laser desorption ionization (MALDI). In DI, the sample is dissolved or dispersed in a matrix, and bombarded by a high-energy (1-10 keV) beam of ions (SIMS), neutral atoms (FAB), or photons (MALDI). The beam ionizes and expels (desorbs) some sample molecules off the matrix. The ion is then accelerated electrostatically, as in EI.

The matrix should be nonvolatile and relatively inert, so that it would not react with the analyte. It should also be a good electrolyte to allow ion formation. Ionized fragments of the matrix itself forms usually have $m/z\lesssim 600$ , so the spectrogram usually filters out that segment.

| Method | Beam | Common beam | Matrix | Typical ions | Analyte range |
|---|---|---|---|---|---|
| SIMS | ions | Ar+, Cs+ | nonvolatile electrolyte | (M + H)+, (M − H)−, (M + Na)+, (M + K)+ | <20 kDa |
| FAB | neutral atoms | Ar, Xe | nonvolatile electrolyte | (M + H)+, (M − H)−, (M + Na)+, (M + K)+ | <20 kDa |
| MALDI | photons | N2 laser 337 nm, infrared laser | UV-absorbing organic | M+ | <300 kDa |

SIMS and FAB are quite similar. SIMS uses an ion beam, usually Ar+ or Cs+. FAB uses a neutral atom beam, usually Ar or Xe. For SIMS and FAB, if the matrix compound is more acidic than the analyte, then predominantly (M + H)+ forms formed, and conversely (M − H)−. Also possibly forming (M + Na)+, (M + K)+, etc, if the matrix is contaminated incidentally (adventitiously) by sodium, potassium, etc. Typical matrix materials include glycerol, thioglycerol, 3-nitrobenzyl alcohol, diethanolamine, triethanolamine, and dithiothreitol-dithioerythritol mixture. They are usually used to analyze polypeptides and oligonucleotides up to 20 kDa.

MALDE uses a photon beam, usually the soft-UV 337 nm nitrogen laser. It can also use an infrared (IR) laser for direct analysis of samples contained in gels or thin-layer chromatography (TLC) plates. MALDE can analyze small polymers (~1 kDa), to oligosaccharides, oligonucleotides and polypeptides, antibodies, up to small proteins (~300 kDa). It is highly sensitive, requiring only femtomoles of sample.

Desorption/ionization on silicon (DIOS) is similar to MALDE, but without the matrix. The sample is deposited directly on a nanostructured (porous silicon) surface and the sample desorbed directly from the nanostructured surface through the adsorption of laser light energy. DIOS has been used to analyze organic molecules, metabolites, biomolecules and peptides, and, ultimately, to image tissues and cells.

### Inductively coupled plasma

Inductively coupled plasma (ICP) sources are used primarily for cation analysis of a wide array of sample types. In this source, a plasma that is electrically neutral overall, but that has had a substantial fraction of its atoms ionized by high temperature, is used to atomize introduced sample molecules and to further strip the outer electrons from those atoms. The plasma is usually generated from argon gas, since the first ionization energy of argon atoms is higher than the first of any other elements except He, F and Ne, but lower than the second ionization energy of all except the most electropositive metals. The heating is achieved by a radio-frequency current passed through a coil surrounding the plasma.

### Photoionization mass spectrometry

Photoionization can be used in experiments which seek to use mass spectrometry as a means of resolving chemical kinetics mechanisms and isomeric product branching. In such instances a high energy photon, either X-ray or uv, is used to dissociate stable gaseous molecules in a carrier gas of He or Ar. In instances where a synchrotron light source is utilized, a tuneable photon energy can be utilized to acquire a photoionization efficiency curve which can be used in conjunction with the charge ratio *m/z* to fingerprint molecular and ionic species. More recently atmospheric pressure photoionization (APPI) has been developed to ionize molecules mostly as effluents of LC-MS systems.

### Ambient ionization

Some applications for ambient ionization include environmental applications as well as clinical applications. In these techniques, ions form in an ion source outside the mass spectrometer. Sampling becomes easy as the samples don't need previous separation nor preparation. Some examples of ambient ionization techniques are Direct Analysis in Real Time (DART), DESI, SESI, LAESI, atmospheric pressure chemical ionization (APCI), desorption atmospheric-pressure chemical ionization (DAPCI), Soft Ionization by Chemical Reaction in Transfer (SICRT) and desorption atmospheric pressure photoionization DAPPI among others.

### Other ionization techniques

Others include glow discharge, field desorption (FD), spark ionization and thermal ionization (TIMS).


## Mass analyzer

Mass analyzers separate the ions according to their mass-to-charge ratio.

There are many types of mass analyzers, using either static or dynamic fields, magnetic or electric fields. Each analyzer type has its strengths and weaknesses. Many mass spectrometers use two or more mass analyzers for tandem mass spectrometry (MS/MS). In addition to the more common mass analyzers listed below, there are others designed for special situations.

### Theory

The following two laws govern the dynamics of charged particles in electric and magnetic fields in vacuum:

$\mathbf {F} =Q(\mathbf {E} +\mathbf {v} \times \mathbf {B} )$

(

Lorentz force law

);

$\mathbf {F} =m\mathbf {a}$

(

Newton's second law

of motion in the non-relativistic case, i.e. valid only at ion velocity much lower than the speed of light).

Here **F** is the force applied to the ion, *m* is the mass of the ion, **a** is the acceleration, *Q* is the ion charge, **E** is the electric field, and **v** × **B** is the vector cross product of the ion velocity and the magnetic field

Equating the above expressions for the force applied to the ion yields:

$(m/Q)\mathbf {a} =\mathbf {E} +\mathbf {v} \times \mathbf {B} .$

This differential equation is the classic equation of motion for charged particles. Together with the particle's initial conditions, it completely determines the particle's motion in space and time in terms of *m/Q*. Thus mass spectrometers could be thought of as "mass-to-charge spectrometers". When presenting data, it is common to use the (officially) dimensionless *m/z*, where z is the number of elementary charges (*e*) on the ion (z=Q/e). This quantity, although it is informally called the mass-to-charge ratio, more accurately speaking represents the ratio of the mass number and the charge number, *z*.

### Analyzer characteristics

There are several important analyzer characteristics.

The **mass resolving power** $\Delta (m/z)$ is the just detectable difference in *m/z*, at that particular *m/z*, usually measured measured in milli mass units (mDa). In particular, the resolution may be different at different *m/z*. It is usually operationalized as the full width at half maximum a peak at that given *m/z*.

The **resolution** is the ratio ${\tfrac {m/z}{\Delta (m/z)}}$ . It is unitless. A "high-resolution" mass analyzer typically has resolution >1 million. Concretely, that means it can resolve two peaks at ~1 kDa, differing by just ~1 mDa.

The **absolute accuracy** is the ratio of the *m/z* measurement error to the true *m/z*. It is defined as $|(m/z)_{\text{measured}}-(m/z)_{\text{true}}|$ . The **relative accuracy** is ${\tfrac {|(m/z)_{\text{measured}}-(m/z)_{\text{true}}|}{(m/z)_{\text{true}}}}$ . It is unitless.

The **mass range** is the range of *m/z* that a given analyzer can analyze.

The **speed** is the number of spectra lines per unit time that can be generated. Typically, higher resolution requires lower speed, and vice versa. Some mass spectrometers, such as the Fourier transform spectrometers, allow a continuous tradeoff between speed and resolution.

### Sector

A sector-type mass analyzer uses a static electric and/or magnetic field to control the path of the ion beam. The most common type uses a magnetic field.

In a simplified case, the field is a constant field B , and we have an ion of mass m and charge $ze$ that enters the field perpendicularly at velocity v . Then, in the field, the ion undergoes circular motion of radius $R={\tfrac {v(m/z)}{Be}}$ . If the ionizer has accelerated the ion under a known voltage V , then the kinetic energy of the ion is $KE=zeV={\tfrac {1}{2}}mv^{2}$ , giving $m/z={\frac {eR^{2}B^{2}}{2V}}$ Thus, the single input ion beam is analyzed into a fan of ion beams, the higher m/z ions turning at a larger radius. One can then select for one m/z by using a moving narrow slit. One can also use a fixed narrow slit, but vary V or B .

If there is just a single detector, then the analyzer can sweep across the mass spectrum one slit at a time. With multiple detectors, the speed of analysis increases.

A pure magnetic sector analyzer can achieve resolution ~10,000. With an added electrostatic focusing field before or after the magnetic sector, the analyzer can achieve resolution ~100,000.

Particularly unstable ions may disintegrate while passing through the analyzer. If it undergoes the reaction Mz+ → M'z+ + (other parts) when entering the analyzer, it would undergo a circular motion of radius $R'={\tfrac {v(m'/z)}{Be}}$ . This would then show up in the resulting spectrogram as a peak that is *apparently* made by an ion with $(m^{*}/z)=({\tfrac {m'^{2}}{m}}/z)$ . Since there is no actual ion with mass $m^{*}$ , this is called an abnormal peak, or a **metastable ion peak**. In general, a meta stable ion peak is a broad peak centered at a highly non-integer value of $m^{*}/z$ . The existence of a metastable ion peak at $({\tfrac {m'^{2}}{m}}/z)$ is strong evidence that two ions of masses $m/z,m'/z$ are in fact related by the reaction Mz+ → M'z+ + (other parts).

### Time-of-flight

The time-of-flight (TOF) analyzer takes as input a short *pulse* of ions, and lets it fly through a long vacuum tube. Ions with different m/z would arrive at the end of the tube at different times, thus analyzing them. The ions must enter the tube as pulses, because otherwise the TOF cannot be measured. If the ionizer outputs a continuous stream of ions, then it must be cut up into ion pulses, by methods such as a fast mechanical shutter, an oscillating electric field plus a narrow slit, etc. The MALDI ionizer is particularly well-suited for TOF analyzer, since the laser used in MALDI is usually a high-intensity pulse laser. MALDI-TOF has allowed measurement of mass spetrograms using only a few attomoles of material.

Concretely, let the length of the analyzer be L , then the time taken for an ion of velocity v to pass through the analyzer is $t=L/v$ . Since $KE=zeV={\tfrac {1}{2}}mv^{2}$ , we have $m/z={\frac {2eV}{L^{2}}}t^{2}$ Often, the input ions are already concentrated in their *m/z*. That is, each ion in the input satisfies $m/z=\delta (m/z)+(m/z)_{0}$ , where $(m/z)_{0}$ is a constant, and $\delta (m/z)\ll (m/z)_{0}$ . In that case, we have $m/z=(m/z)_{0}+{\frac {4eVt_{0}}{L^{2}}}\delta t$ This means that the signal can be measured by an oscilloscope in trigger mode. Indeed, the first GC-MS was done in 1950 using an oscilloscope. The experimenters took quick photos of the oscilloscope screen for each component exiting the gas chromatography machine.

This distribution in velocities broadens the peaks shown on the count vs *m/z* plot, but will generally not change the central location of the peaks, since the starting velocity of ions is generally centered at zero. To fix this problem, time-lag focusing/delayed extraction has been coupled with TOF-MS. If the ions do not start at identical kinetic energies, then some ions may lag behind higher kinetic energy ions decreasing resolution. Reflectron geometries are commonly employed to correct this problem.

Longer tubes result in higher resolution. A reflector doubles the effective tube length. A reflector-TOF can reach a resolution of several thousands. For their low resolution, TOF mass spectrometers makes up for it in speed. They are particularly useful in chemical kinetics studies. It can study rapid reactions such as combustion and explosions.

### Quadrupole mass filter

A quadrupole mass analyzers uses four parallel metal rods to create a quadrupole electrical field oscillating at radio frequency (RF), to selectively stabilize or destabilize the paths of ions passing through.

With each oscillation pattern, the ions passing through would undergo a helical motion. If the ion has *m/z* within a certain range, the helical motion is stable. Otherwise, the helical motion will increase in amplitude until the ion collides with the rods. This means that only ions with m/z within a narrow range can go through it. The full spectrogram can be swept through by changing the potentials on the rods, continuously or in a succession of discrete hops.

They are typically of low resolution ~1000, but they are cheap and small, so are good for "desktop" mass spectrometers.

The quadrupole mass filter is closely related to the quadrupole ion trap, particularly the linear quadrupole ion trap except that it is designed to pass the untrapped ions rather than collect the trapped ones, and is for that reason referred to as a **transmission quadrupole**. The quadrupole ion trap itself can be used as an analyzer, as in ion trap analyzers.

A common variation of the transmission quadrupole is the triple quadrupole mass spectrometer. The "triple quad" has three consecutive quadrupole stages, the first acting as a mass filter to transmit a particular incoming ion to the second quadrupole, a collision chamber, wherein that ion can be broken into fragments. The third quadrupole also acts as a mass filter, to transmit a particular fragment ion to the detector. It is a kind of MS/MS, and so it can perform various scan types characteristic of MS/MS.

A magnetically enhanced quadrupole mass analyzer has an additional magnetic field, axial or transverse.

### Ion traps

#### Three-dimensional quadrupole ion trap

The quadrupole ion trap works on the same physical principles as the quadrupole mass analyzer, but the ions are trapped and sequentially ejected. Ions are trapped in a mainly quadrupole RF field, in a space defined by a ring electrode (usually connected to the main RF potential) between two endcap electrodes (typically connected to DC or auxiliary AC potentials). The sample is ionized either internally (e.g. with an electron or laser beam), or externally, in which case the ions are often introduced through an aperture in an endcap electrode.

There are many mass/charge separation and isolation methods but the most commonly used is the mass instability mode in which the RF potential is ramped so that the orbit of ions with a mass *a* > *b* are stable while ions with mass *b* become unstable and are ejected on the *z*-axis onto a detector. There are also non-destructive analysis methods.

Ions may also be ejected by the resonance excitation method, whereby a supplemental oscillatory excitation voltage is applied to the endcap electrodes, and the trapping voltage amplitude and/or excitation voltage frequency is varied to bring ions into a resonance condition in order of their mass/charge ratio.

#### Cylindrical ion trap

The cylindrical ion trap mass spectrometer (CIT) is a derivative of the quadrupole ion trap where the electrodes are formed from flat rings rather than hyperbolic shaped electrodes. The architecture lends itself well to miniaturization because as the size of a trap is reduced, the shape of the electric field near the center of the trap, the region where the ions are trapped, forms a shape similar to that of a hyperbolic trap.

#### Linear quadrupole ion trap

A linear quadrupole ion trap is similar to a quadrupole ion trap, but it traps ions in a two dimensional quadrupole field, instead of a three-dimensional quadrupole field as in a 3D quadrupole ion trap. Thermo Fisher's LTQ ("linear trap quadrupole") is an example of the linear ion trap.

A toroidal ion trap can be visualized as a linear quadrupole curved around and connected at the ends or as a cross-section of a 3D ion trap rotated on edge to form the toroid, donut-shaped trap. The trap can store large volumes of ions by distributing them throughout the ring-like trap structure. This toroidal shaped trap is a configuration that allows the increased miniaturization of an ion trap mass analyzer. Additionally, all ions are stored in the same trapping field and ejected together simplifying detection that can be complicated with array configurations due to variations in detector alignment and machining of the arrays.

As with the toroidal trap, linear traps and 3D quadrupole ion traps are the most commonly miniaturized mass analyzers due to their high sensitivity, tolerance for mTorr pressure, and capabilities for single analyzer tandem mass spectrometry (e.g. product ion scans).

### Fourier-transform ion cyclotron resonance

Fourier-transform mass spectrometry (FTMS), or more precisely Fourier-transform ion cyclotron resonance mass spectrometry (FT-ICR MS), measures mass by detecting the image current produced by ions spiralling in the presence of a magnetic field. Instead of measuring the deflection of ions with a detector such as an electron multiplier, the ions are injected into a Penning trap (a static electric/magnetic ion trap) where they effectively form part of a circuit. Detectors at fixed positions in space measure the electrical signal of ions which pass near them over time, producing a periodic signal. Since the frequency of an ion's cycling is determined by its *m/z* ratio, this can be deconvoluted by Fourier transform on the signal.

Ion cyclotron resonance (ICR) is an older mass analysis technique. It is similar to FTMS, in that the ions undergo cyclotron resonane. However, the ions are detected with a traditional detector. Ions trapped in a Penning trap are excited by an RF electric field until they impact the wall of the trap, where the detector is located. Ions of different mass are resolved according to impact time.

FTMS is generally the most sensitive analyzer on the market, achieving resolution ~1 million. It achieves such high resolution, since each ion is "counted" multiple times by the spectrometer. From the perspective of the uncertainty principle of signal processing, an oscillating signal that is highly *delocalized* in time is also highly *localized* in frequency.

#### Orbitrap

Orbitrap analyzers are similar to FTMS analyzers. Ions are electrostatically trapped in an orbit around a central, spindle shaped electrode. The electrode confines the ions so that they both orbit around the central electrode and oscillate back and forth along the central electrode's long axis. This oscillation generates an image current in the detector plates which is recorded by the instrument. The frequencies of these image currents depend on the mass-to-charge ratios of the ions. Mass spectra are obtained by Fourier transformation of the recorded image currents.

Orbitraps have a high mass accuracy, high sensitivity and a good dynamic range. They are also quite small.

### High resolution

Some chemical species have the same chemical composition, but different isotopes (isotopomers). They can be distinguished by a very basic analyzer. Indeed, isotopes were discovered in 1922, very early in the history of mass spectrometry.

However, two chemical species can have the same number of nucleons (neutrons and protons). For example, C3 and SH4 both have 36 nucleons. They can still be distinguished, since proton and neutron mass differ by 1.4 mDa, and since different nuclei have different binding energy, which by $E=mc^{2}$ results in a different mass. The net result is that C3 and S1H4 differ by 3.4 mDa. Even smaller differences are achievable by carefully matching isotopes. For example, C4 and S1H313C1 differ by 1.1 mDa. Such differences can be resolved by high resolution mass spectrometry, which reaches resolution >1 million, sufficient to resolve ~1 mDa difference at *m/z* ~ 1000. Note that the electron mass is 0.5 mDa.

There are many techniques for high resolution MS, but the highest resolution is achieved by FTMS with high magnetic field. With increasing magnetic field strength, the resolution and spectral acquisition speed increases linearly, while mass accuracy and dynamic range increases quadratically. Consequently, the highest resolution is achieved by high field FTMS, up to 21 Tesla. It reaches resolution >2.7 million at m/z ~ 400, and mass measurement accuracy < 80 ppb.

They are often employed in geochemical and petrochemical studies, since there is a lot of money in petroleum industry, and petroleum composition is highly complex. Another application is in isotopic analysis of large proteins. Two proteins differing by a single isotopic atom are separated by $\Delta m\approx 1$ , requiring a resolution of $m/\Delta m$ to resolve. For large proteins with m > 100 kDa and z ~ 50, such as monoclonal antibodies, this requires an analyzer that achieves resolving power > 100,000 at m/z ~ 2000.

High resolution FTMS is also very sensitive as a detector. It has allowed detecting proteins in the 8–20 kDa range at a sample concentration of ~30 zeptomole (i.e. about 20,000 *individual* molecules).

When the mass of a single ion species is to be measured, the highest precision achievable is via Penning-type traps. The PENTATRAP for example measures the mass of long-lived, highly charged, heavy ions, to a precision of $m/\Delta m>10^{11}$ . This is sufficiently sensitive to directly measure the energy of metastable electronic states to an accuracy of ~1 eV via the mass-energy equation.


## Detectors

The final element of the mass spectrometer is the detector. The detector records either the charge induced or the current produced when an ion passes by or hits a surface. In a scanning instrument, the signal produced in the detector during the course of the scan versus where the instrument is in the scan (at what *m/Q*) will produce a mass spectrum, a record of ions as a function of *m/Q*.

The **linear dynamic range** is the range over which the detector signal is linear with analyte concentration.

Typically, some type of electron multiplier is used, though other detectors including Faraday cups and ion-to-photon detectors are also used. Because the number of ions leaving the mass analyzer at a particular instant is typically quite small, considerable amplification is often necessary to get a signal. Microchannel plate detectors are commonly used in modern commercial instruments. In FTMS and Orbitraps, the detector consists of a pair of metal surfaces within the mass analyzer/ion trap region which the ions only pass near as they oscillate. No direct current is produced, only a weak AC image current is produced in a circuit between the electrodes. Other inductive detectors have also been used.


## Tandem mass spectrometry

A tandem mass spectrometer is one capable of multiple rounds of mass spectrometry, usually separated by some form of molecule fragmentation. For example, one mass analyzer can isolate one peptide from many entering a mass spectrometer. A collision cell then stabilizes the peptide ions while they collide with a gas, causing them to fragment by collision-induced dissociation (CID). A further mass analyzer then sorts the fragments produced from the peptides. Tandem MS can also be done in a single mass analyzer over time, as in a quadrupole ion trap. There are various methods for fragmenting molecules for tandem MS, including collision-induced dissociation (CID), electron capture dissociation (ECD), electron transfer dissociation (ETD), infrared multiphoton dissociation (IRMPD), blackbody infrared radiative dissociation (BIRD), electron-detachment dissociation (EDD) and surface-induced dissociation (SID). An important application using tandem mass spectrometry is in protein identification.

Tandem mass spectrometry enables a variety of experimental sequences. Many commercial mass spectrometers are designed to expedite the execution of such routine sequences as selected reaction monitoring, precursor ion scanning, product ion scanning, and neutral loss scanning.

- In selected reaction monitoring, the first analyzer allows only a single mass through and the second analyzer monitors for multiple user-defined fragment ions over longer dwell-times than could be achieved in a full scan. This increases sensitivity.
- In product ion scans, the first mass analyzer is fixed to select a particular precursor ion ("parent"), while the second is scanned to find all the fragments ("products", or "daughter ions") to which it can be fragmented in the collision cell.
- In precursor ion scans, the second mass analyzer is fixed to select a particular fragment ion ("daughter"), while the first is scanned to find all possible precursor ions that could give rise to this fragment.
- In neutral loss scans, the two mass analyzers are scanned in parallel, but separated by the mass of a molecular subunit of interest to the analyst. Ions are detected if they lose that fixed mass during fragmentation. This can be used to look for any chemical that is capable of losing a particular neutral group, for example a sugar residue. Together, neutral loss and precursor ion scans can be used to hunt for chemicals with particular motifs.

Another type of tandem mass spectrometry used for radiocarbon dating is accelerator mass spectrometry, which uses very high voltages, usually in the mega-volt range, to accelerate negative ions into a type of tandem mass spectrometer.

The **METLIN Metabolite and Chemical Entity Database** is the largest repository of experimental tandem mass spectrometry data acquired from standards. The tandem mass spectrometry data on over 960,000 molecular standards (as of October 2025) is provided to facilitate the identification of chemical entities from tandem mass spectrometry experiments. In addition to the identification of known molecules it is also useful for identifying unknowns using its similarity searching/analysis. All tandem mass spectrometry data comes from the experimental analysis of standards at multiple collision energies and in both positive and negative ionization modes.


## Common mass spectrometer configurations and techniques

When a specific combination of source, analyzer, and detector becomes conventional in practice, a compound acronym may arise to designate it succinctly. One example is MALDI-TOF, which refers to a combination of a matrix-assisted laser desorption/ionization source with a time-of-flight mass analyzer. Other examples include inductively coupled plasma-mass spectrometry (ICP-MS), accelerator mass spectrometry, thermal ionization-mass spectrometry (TIMS) and spark source mass spectrometry.

Certain applications of mass spectrometry have developed monikers that although strictly speaking would seem to refer to a broad application, in practice have come instead to connote a specific or a limited number of instrument configurations. An example of this is isotope-ratio mass spectrometry, which refers in practice to the use of a limited number of sector based mass analyzers; this name is used to refer to both the application and the instrument used for the application.
