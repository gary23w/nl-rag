---
title: "Mass spectrometry (part 2/2)"
source: https://en.wikipedia.org/wiki/Mass_spectrometry
domain: mass-spectrometry-analysis
license: CC-BY-SA-4.0
tags: mass spectrometry analysis, tandem mass spectrometry, peptide mass fingerprinting, de novo peptide sequencing
fetched: 2026-07-02
part: 2/2
---

## Separation techniques combined with mass spectrometry

An important enhancement to the mass resolving and mass determining capabilities of mass spectrometry is using it in tandem with chromatographic and other separation techniques.

### Gas chromatography

A common combination is gas chromatography-mass spectrometry (GC/MS or GC-MS). In this technique, a gas chromatograph is used to separate different compounds. This stream of separated compounds is fed online into the ion source, a metallic filament to which voltage is applied. This filament emits electrons which ionize the compounds. The ions can then further fragment, yielding predictable patterns. Intact ions and fragments pass into the mass spectrometer's analyzer and are eventually detected. However, the high temperatures (300 °C) used in the GC-MS injection port (and oven) can result in thermal degradation of injected molecules, thus resulting in the measurement of degradation products instead of the actual molecule(s) of interest.

### Liquid chromatography

Similarly to gas chromatography MS (GC-MS), liquid chromatography-mass spectrometry (LC/MS or LC-MS) separates compounds chromatographically before they are introduced to the ion source and mass spectrometer. It differs from GC-MS in that the mobile phase is liquid, usually a mixture of water and organic solvents, instead of gas. Most commonly, an electrospray ionization source is used in LC-MS. Other popular and commercially available LC-MS ion sources are atmospheric pressure chemical ionization and atmospheric pressure photoionization. There are also some newly developed ionization techniques like laser spray.

### Capillary electrophoresis–mass spectrometry

Capillary electrophoresis–mass spectrometry (CE-MS) is a technique that combines the liquid separation process of capillary electrophoresis with mass spectrometry. CE-MS is typically coupled to electrospray ionization.

### Ion mobility

Ion mobility spectrometry-mass spectrometry (IMS/MS or IMMS) is a technique where ions are first separated by drift time through some neutral gas under an applied electrical potential gradient before being introduced into a mass spectrometer. Drift time is a measure of the collisional cross section relative to the charge of the ion. The duty cycle of IMS (the time over which the experiment takes place) is longer than most mass spectrometric techniques, such that the mass spectrometer can sample along the course of the IMS separation. This produces data about the IMS separation and the mass-to-charge ratio of the ions in a manner similar to LC-MS.

The duty cycle of IMS is short relative to liquid chromatography or gas chromatography separations and can thus be coupled to such techniques, producing triple modalities such as LC/IMS/MS.


## Data and analysis

### Data representations

Mass spectrometry produces various types of data. The most common data representation is the mass spectrum.

Certain types of mass spectrometry data are best represented as a mass chromatogram. Types of chromatograms include selected ion monitoring (SIM), total ion current (TIC), and selected reaction monitoring, among many others.

Other types of mass spectrometry data are well represented as a three-dimensional contour map. In this form, the mass-to-charge, *m/z* is on the *x*-axis, intensity the *y*-axis, and an additional experimental parameter, such as time, is recorded on the *z*-axis.

### Data analysis

Mass spectrometry data analysis is specific to the type of experiment producing the data. General subdivisions of data are fundamental to understanding any data.

Many mass spectrometers work in either *negative ion mode* or *positive ion mode*. It is very important to know whether the observed ions are negatively or positively charged. This is often important in determining the neutral mass but it also indicates something about the nature of the molecules.

Different types of ion source result in different arrays of fragments produced from the original molecules. An electron ionization source produces many fragments and mostly single-charged (1-) radicals (odd number of electrons), whereas an electrospray source usually produces non-radical quasimolecular ions that are frequently multiply charged. Tandem mass spectrometry purposely produces fragment ions post-source and can drastically change the sort of data achieved by an experiment.

Knowledge of the origin of a sample can provide insight into the component molecules of the sample and their fragmentations. A sample from a synthesis/manufacturing process will probably contain impurities chemically related to the target component. A crudely prepared biological sample will probably contain a certain amount of salt, which may form adducts with the analyte molecules in certain analyses.

Results can also depend heavily on sample preparation and how it was run/introduced. An important example is the issue of which matrix is used for MALDI spotting, since much of the energetics of the desorption/ionization event is controlled by the matrix rather than the laser power. Sometimes samples are spiked with sodium or another ion-carrying species to produce adducts rather than a protonated species.

Mass spectrometry can measure molar mass, molecular structure, and sample purity. Each of these questions requires a different experimental procedure; therefore, adequate definition of the experimental goal is a prerequisite for collecting the proper data and successfully interpreting it.

#### Interpretation of mass spectra

Since the precise structure or peptide sequence of a molecule is deciphered through the set of fragment masses, the interpretation of mass spectra requires combined use of various techniques. Usually the first strategy for identifying an unknown compound is to compare its experimental mass spectrum against a library of mass spectra. If no matches result from the search, then manual interpretation or software assisted interpretation of mass spectra must be performed. Computer simulation of ionization and fragmentation processes occurring in mass spectrometer is the primary tool for assigning structure or peptide sequence to a molecule. An *a priori* structural information is fragmented *in silico* and the resulting pattern is compared with observed spectrum. Such simulation is often supported by a fragmentation library that contains published patterns of known decomposition reactions. Software taking advantage of this idea has been developed for both small molecules and proteins.

Analysis of mass spectra can also be spectra with accurate mass. A mass-to-charge ratio value (*m/z*) with only integer precision can represent an immense number of theoretically possible ion structures; however, more precise mass figures significantly reduce the number of candidate molecular formulas. A computer algorithm called formula generator calculates all molecular formulas that theoretically fit a given mass with specified tolerance.

A recent technique for structure elucidation in mass spectrometry, called precursor ion fingerprinting, identifies individual pieces of structural information by conducting a search of the tandem spectra of the molecule under investigation against a library of the product-ion spectra of structurally characterized precursor ions.

Particularly unstable ions may disintegrate while passing through the analyzer. If it undergoes the reaction Mz+ → M'z+ + (other parts) when entering the analyzer, it would undergo a circular motion of radius $R'={\tfrac {v(m'/z)}{Be}}$ . This would then show up in the resulting spectrogram as a peak that is *apparently* made by an ion with $(m^{*}/z)=({\tfrac {m'^{2}}{m}}/z)$ . Since there is no actual ion with mass $m^{*}$ , this is called an abnormal peak, or a **metastable ion peak**. In general, a meta stable ion peak is a broad peak centered at a highly non-integer value of $m^{*}/z$ . The existence of a metastable ion peak at $({\tfrac {m'^{2}}{m}}/z)$ is strong evidence that two ions of masses $m/z,m'/z$ are in fact related by the reaction Mz+ → M'z+ + (other parts).


## Applications

Mass spectrometry has both qualitative and quantitative uses. These include identifying unknown compounds, determining the isotopic composition of elements in a molecule, and determining the structure of a compound by observing its fragmentation. Other uses include quantifying the amount of a compound in a sample or studying the fundamentals of gas phase ion chemistry (the chemistry of ions and neutrals in a vacuum). MS is now commonly used in analytical laboratories that study physical, chemical, or biological properties of a great variety of compounds. Quantification can be relative (analyzed relative to a reference sample) or absolute (analyzed using a standard curve method).

As an analytical technique it possesses distinct advantages such as: Increased sensitivity over most other analytical techniques because the analyzer, as a mass-charge filter, reduces background interference, Excellent specificity from characteristic fragmentation patterns to identify unknowns or confirm the presence of suspected compounds, Information about molecular weight, Information about the isotopic abundance of elements, Temporally resolved chemical data.

A few of the disadvantages of the method is that it often fails to distinguish between optical and geometrical isomers and the positions of substituent in o-, m- and p- positions in an aromatic ring. Also, its scope is limited in identifying hydrocarbons that produce similar fragmented ions.

### Isotope ratio mass spectrometry

Mass spectrometry is also used to determine the isotopic composition of elements within a sample. Differences in mass among isotopes of an element are very small, and the less abundant isotopes of an element are typically very rare, so a very sensitive instrument is required. For the measurement of light elements (e.g. H,C,N,O,S), isotope ratio mass spectrometers usually use a single magnet to bend a beam of ionized particles towards a series of Faraday cups which convert particle impacts to electric current. A fast on-line analysis of deuterium content of water can be done using flowing afterglow mass spectrometry, FA-MS. Probably the most sensitive and accurate mass spectrometer for this purpose is the accelerator mass spectrometry. This is because it provides ultimate sensitivity, capable of measuring individual atoms and measuring nuclides with a dynamic range of ~1015 relative to the major stable isotope. Isotopic signatures can serve as markers of a variety of processes. Some isotope ratios are used to determine the age of materials for example as in carbon dating. Labeling with stable isotopes is also used for protein quantification (see protein characterization below).

#### Membrane-introduction mass spectrometry: measuring gases in solution

Membrane-introduction mass spectrometry combines the isotope ratio mass spectrometry with a reaction chamber/cell separated by a gas-permeable membrane. This method allows the study of gases as they evolve in solution. This method has been extensively used for the study of the production of oxygen by Photosystem II.

### Trace gas analysis

Several techniques use ions created in a dedicated ion source injected into a flow tube or a drift tube: selected ion flow tube (SIFT-MS), and proton transfer reaction (PTR-MS), are variants of chemical ionization dedicated for trace gas analysis of air, breath or liquid headspace using well defined reaction time allowing calculations of analyte concentrations from the known reaction kinetics without the need for internal standard or calibration.

Another technique with applications in trace gas analysis field is secondary electrospray ionization (SESI-MS), which is a variant of electrospray ionization. SESI consist of an electrospray plume of pure acidified solvent that interacts with neutral vapors.  Vapor molecules get ionized at atmospheric pressure when charge is transferred from the ions formed in the electrospray to the molecules. One advantage of this approach is that it is compatible with most ESI-MS systems.

### Residual gas analysis

A residual gas analyzer (RGA) is a small and usually rugged mass spectrometer, typically designed for process control and contamination monitoring in vacuum systems. When constructed as a quadrupole mass analyzer, there exist two implementations, utilizing either an open ion source (OIS) or a closed ion source (CIS). RGAs may be found in high vacuum applications such as research chambers, surface science setups, accelerators, scanning microscopes, etc. RGAs are used in most cases to monitor the quality of the vacuum and easily detect minute traces of impurities in the low-pressure gas environment. These impurities can be measured down to $10^{-14}$ Torr levels, possessing sub-ppm detectability in the absence of background interferences.

RGAs would also be used as sensitive in-situ leak detectors commonly using helium, isopropyl alcohol or other tracer molecules. With vacuum systems pumped down to lower than $10^{-5}$ Torr—checking of the integrity of the vacuum seals and the quality of the vacuum—air leaks, virtual leaks and other contaminants at low levels may be detected before a process is initiated.

### Atom probe

An atom probe is an instrument that combines time-of-flight mass spectrometry and field-evaporation microscopy to map the location of individual atoms.

### Pharmacokinetics

Pharmacokinetics is often studied using mass spectrometry because of the complex nature of the matrix (often blood or urine) and the need for high sensitivity to observe low dose and long time point data. The most common instrumentation used in this application is LC-MS with a triple quadrupole mass spectrometer. Tandem mass spectrometry is usually employed for added specificity. Standard curves and internal standards are used for quantitation of usually a single pharmaceutical in the samples. The samples represent different time points as a pharmaceutical is administered and then metabolized or cleared from the body. Blank or t=0 samples taken before administration are important in determining background and ensuring data integrity with such complex sample matrices. Much attention is paid to the linearity of the standard curve; however it is not uncommon to use curve fitting with more complex functions such as quadratics since the response of most mass spectrometers is less than linear across large concentration ranges.

There is currently considerable interest in the use of very high sensitivity mass spectrometry for microdosing studies, which are seen as a promising alternative to animal experimentation.

Recent studies show that secondary electrospray ionization (SESI) is a powerful technique to monitor drug kinetics via breath analysis. Because breath is naturally produced, several datapoints can be readily collected. This allows for the number of collected data-points to be greatly increased. In animal studies, this approach SESI can reduce animal sacrifice. In humans, SESI-MS non-invasive analysis of breath can help study the kinetics of drugs at a personalized level.

### Protein characterization

Mass spectrometry is an important method for the characterization and sequencing of proteins. The two primary methods for ionization of whole proteins are electrospray ionization (ESI) and matrix-assisted laser desorption/ionization (MALDI). In keeping with the performance and mass range of available mass spectrometers, two approaches are used for characterizing proteins. In the first, intact proteins are ionized by either of the two techniques described above, and then introduced to a mass analyzer. This approach is referred to as "top-down" strategy of protein analysis. The top-down approach however is largely limited to low-throughput single-protein studies. In the second, proteins are enzymatically digested into smaller peptides using proteases such as trypsin or pepsin, either in solution or in gel after electrophoretic separation. Other proteolytic agents are also used. The collection of peptide products are often separated by chromatography prior to introduction to the mass analyzer. When the characteristic pattern of peptides is used for the identification of the protein the method is called peptide mass fingerprinting (PMF), if the identification is performed using the sequence data determined in tandem MS analysis it is called de novo peptide sequencing. These procedures of protein analysis are also referred to as the "bottom-up" approach, and have also been used to analyse the distribution and position of post-translational modifications such as phosphorylation on proteins. A third approach is also beginning to be used, this intermediate "middle-down" approach involves analyzing proteolytic peptides that are larger than the typical tryptic peptide.

### Space exploration

As a standard method for analysis, mass spectrometers have reached other planets and moons. Two were taken to Mars by the Viking program. In early 2005 the Cassini–Huygens mission delivered a specialized GC-MS instrument aboard the Huygens probe through the atmosphere of Titan, the largest moon of the planet Saturn. This instrument analyzed atmospheric samples along its descent trajectory and was able to vaporize and analyze samples of Titan's frozen, hydrocarbon covered surface once the probe had landed. These measurements compare the abundance of isotope(s) of each particle comparatively to earth's natural abundance. Also on board the Cassini–Huygens spacecraft was an ion and neutral mass spectrometer which had been taking measurements of Titan's atmospheric composition as well as the composition of Enceladus' plumes. A Thermal and Evolved Gas Analyzer mass spectrometer was carried by the Mars Phoenix Lander launched in 2007.

Mass spectrometers are also widely used in space missions to measure the composition of plasmas. For example, the Cassini spacecraft carried the Cassini Plasma Spectrometer (CAPS), which measured the mass of ions in Saturn's magnetosphere.

### Respired gas monitor

Mass spectrometers were used in hospitals for respiratory gas analysis beginning around 1975 through the end of the century. Some are probably still in use but none are currently being manufactured.

Found mostly in the operating room, they were a part of a complex system, in which respired gas samples from patients undergoing anesthesia were drawn into the instrument through a valve mechanism designed to sequentially connect up to 32 rooms to the mass spectrometer. A computer directed all operations of the system. The data collected from the mass spectrometer was delivered to the individual rooms for the anesthesiologist to use.

The uniqueness of this magnetic sector mass spectrometer may have been the fact that a plane of detectors, each purposely positioned to collect all of the ion species expected to be in the samples, allowed the instrument to simultaneously report all of the gases respired by the patient. Although the mass range was limited to slightly over 120 u, fragmentation of some of the heavier molecules negated the need for a higher detection limit.

### Preparative mass spectrometry

The primary function of mass spectrometry is as a tool for chemical analyses based on detection and quantification of ions according to their mass-to-charge ratio. However, mass spectrometry also shows promise for material synthesis. Ion soft landing is characterized by deposition of intact species on surfaces at low kinetic energies which precludes the fragmentation of the incident species. The soft landing technique was first reported in 1977 for the reaction of low energy sulfur containing ions on a lead surface.

### Charge detection mass spectrometry

Most mass spectrometers measure the mass-to-charge ratio; the actual mass can be found only if the charge is known. For smaller molecules the charge can be determined from the spacing of isotope peaks, but for very large biomolecules and particles (in the megadalton range) resolution may not be adequate to separate isotope peaks, and thus the mass cannot be determined. In charge detection mass spectrometry (CDMS), the charge of an individual ion/particle is measured directly (alongside its mass-to-charge ratio) and therefore the true mass is known. It is a single-particle technique, but to produce more precise and accurate results, the data from many individually-measured ions can be combined.
