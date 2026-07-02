---
title: "Tandem mass spectrometry"
source: https://en.wikipedia.org/wiki/Tandem_mass_spectrometry
domain: mass-spectrometry-proteomics
license: CC-BY-SA-4.0
tags: shotgun proteomics, peptide fragmentation, tandem ms, electrospray
fetched: 2026-07-02
---

# Tandem mass spectrometry

**Tandem mass spectrometry**, also known as **MS/MS** or **MS2**, is a technique in instrumental analysis where two or more stages of analysis using one or more mass analyzers are performed with an additional reaction step in between these analyses to increase their abilities to analyse chemical samples. A common use of tandem MS is the analysis of biomolecules, such as proteins and peptides.

The molecules of a given sample are ionized and the first spectrometer (designated **MS1**) separates these ions by their mass-to-charge ratio (often given as **m/z** or m/Q). Ions of a particular m/z-ratio coming from MS1 are selected and then made to split into smaller fragment ions, e.g. by collision-induced dissociation, ion-molecule reaction, or photodissociation. These fragments are then introduced into the second mass spectrometer (**MS2**), which in turn separates the fragments by their m/z-ratio and detects them. The fragmentation step makes it possible to identify and separate ions that have very similar m/z-ratios in regular mass spectrometers.

## Structure

Typical tandem mass spectrometry instrumentation setups include triple quadrupole mass spectrometer (QqQ), multi-sector mass spectrometer, ion trap, quadrupole–time of flight (Q-TOF), Fourier transform ion cyclotron resonance (FT-ICR), and hybrid mass spectrometers.

### Triple quadrupole mass spectrometer

Triple quadrupole mass spectrometers use the first and third quadrupoles as mass filters. When analytes pass the second quadrupole, the fragmentation proceeds through collision with gas.

### Quadrupole–time of flight (Q-TOF)

Q-TOF mass spectrometers combine quadrupole and TOF instruments, which together enable fragmentation experiments that yield highly accurate mass quantitations for product ions. This is a method of mass spectrometry in which fragmented ion (*m*/*z*) ratios are determined through a time of flight measurement.

### Hybrid mass spectrometer

Hybrid mass spectrometers consist of more than two mass analyzers.

## Instrumentation

Multiple stages of mass analysis separation can be accomplished with individual mass spectrometer elements separated in space or using a single mass spectrometer with the MS steps separated in time. For tandem mass spectrometry in space, the different elements are often noted in a shorthand, giving the type of mass selector used.

### Tandem in space

In tandem mass spectrometry *in space*, the separation elements are physically separated and distinct, although there is a physical connection between the elements to maintain high vacuum. These elements can be sectors, transmission quadrupole, or time-of-flight. When using multiple quadrupoles, they can act as both mass analyzers and collision chambers.

Common notation for mass analyzers is *Q* – quadrupole mass analyzer; *q* – radio frequency collision quadrupole; *TOF* – time-of-flight mass analyzer; *B* – magnetic sector, and *E* – electric sector. The notation can be combined to indicate various hybrid instrument, for example *QqQ'* – triple quadrupole mass spectrometer; *QTOF* – quadrupole time-of-flight mass spectrometer (also *QqTOF*); and *BEBE* – four-sector (reverse geometry) mass spectrometer.

### Tandem in time

By doing tandem mass spectrometry *in time*, the separation is accomplished with ions trapped in the same place, with multiple separation steps taking place over time. A quadrupole ion trap or Fourier transform ion cyclotron resonance instrument can be used for such an analysis. Trapping instruments can perform multiple steps of analysis, which is sometimes referred to as MS*n* (MS to the *n*). Often the number of steps, *n*, is not indicated, but occasionally the value is specified; for example MS3 indicates three stages of separation. Tandem in time MS instruments do not use the modes described next, but typically collect all of the information from a precursor ion scan and a parent ion scan of the entire spectrum. Each instrumental configuration utilizes a unique mode of mass identification.

### Tandem in space MS/MS modes

When tandem MS is performed with an in space design, the instrument must operate in one of a variety of modes. There are a number of different tandem MS/MS experimental setups and each mode has its own applications and provides different information. Tandem MS in space uses the coupling of two instrument components which measure the same mass spectrum range but with a controlled fractionation between them in space, while tandem MS in time involves the use of an ion trap.

There are four main scan experiments possible using MS/MS: precursor ion scan, product ion scan, neutral loss scan, and selected reaction monitoring.

For a precursor ion scan, the product ion is selected in the second mass analyzer, and the precursor masses are scanned in the first mass analyzer. Note that precursor ion is synonymous with parent ion and product ion with daughter ion; however the use of these anthropomorphic terms is discouraged.

In a product ion scan, a precursor ion is selected in the first stage, allowed to fragment and then all resultant masses are scanned in the second mass analyzer and detected in the detector that is positioned after the second mass analyzer. This experiment is commonly performed to identify transitions used for quantification by tandem MS.

In a neutral loss scan, the first mass analyzer scans all the masses. The second mass analyzer also scans, but at a set offset from the first mass analyzer. This offset corresponds to a neutral loss that is commonly observed for the class of compounds. In a constant-neutral-loss scan, all precursors that undergo the loss of a specified common neutral are monitored. To obtain this information, both mass analyzers are scanned simultaneously, but with a mass offset that correlates with the mass of the specified neutral. Similar to the precursor-ion scan, this technique is also useful in the selective identification of closely related class of compounds in a mixture.

In selected reaction monitoring, both mass analyzers are set to a selected mass. This mode is analogous to selected ion monitoring for MS experiments. A selective analysis mode, which can increase sensitivity.

## Fragmentation

Fragmentation of gas-phase ions is essential to tandem mass spectrometry and occurs between different stages of mass analysis. There are many methods used to fragment the ions and these can result in different types of fragmentation and thus different information about the structure and composition of the molecule.

### In-source fragmentation

Often, the ionization process is sufficiently violent to leave the resulting ions with sufficient internal energy to fragment within the mass spectrometer. If the product ions persist in their non-equilibrium state for a moderate amount of time before auto-dissociation this process is called metastable fragmentation. Nozzle-skimmer fragmentation refers to the purposeful induction of in-source fragmentation by increasing the nozzle-skimmer potential on usually electrospray based instruments. Although in-source fragmentation allows for fragmentation analysis, it is not technically tandem mass spectrometry unless metastable ions are mass analyzed or selected before auto-dissociation and a second stage of analysis is performed on the resulting fragments. In-source fragmentation can be used in lieu of tandem mass spectrometry through the utilization of enhanced in-source fragmentation annotation (EISA) technology which generates fragmentation that directly matches tandem mass spectrometry data. Fragments observed by EISA have higher signal intensity than traditional fragments which suffer losses in the collision cells of tandem mass spectrometers. EISA enables fragmentation data acquisition on MS1 mass analyzers such as time-of-flight and single quadrupole instruments. In-source fragmentation is often used in addition to tandem mass spectrometry (with post-source fragmentation) to allow for two steps of fragmentation in a pseudo MS3-type of experiment.

### Collision-induced dissociation

Post-source fragmentation is most often what is being used in a tandem mass spectrometry experiment. Energy can also be added to the ions, which are usually already vibrationally excited, through post-source collisions with neutral atoms or molecules, the absorption of radiation, or the transfer or capture of an electron by a multiply charged ion. Collision-induced dissociation (CID), also called collisionally activated dissociation (CAD), involves the collision of an ion with a neutral atom or molecule in the gas phase and subsequent dissociation of the ion. For example, consider

${\ce {{AB+}+ M -> {A}+ {B+}+ M}}$

where the ion AB+ collides with the neutral species M and subsequently breaks apart. The details of this process are described by collision theory. Due to different instrumental configuration, two main different types of CID are possible: *(i)* beam-type (in which precursor ions are fragmented on-the-flight) and *(ii)* ion trap-type (in which precursor ions are first trapped, and then fragmented).

A third and more recent type of CID fragmentation is higher-energy collisional dissociation (HCD). HCD is a CID technique specific to orbitrap mass spectrometers in which fragmentation takes place external to the ion trap, it happens in the HCD cell (in some instruments named "ion routing multipole"). HCD is a trap-type fragmentation that has been shown to have beam-type characteristics. Freely available large scale high resolution tandem mass spectrometry databases exist (e.g. METLIN with 960,000 molecular standards each with experimental CID MS/MS data), and are typically used to facilitate small molecule identification.

### Electron capture and transfer methods

The energy released when an electron is transferred to or captured by a multiply charged ion can induce fragmentation.

#### Electron-capture dissociation

If an electron is added to a multiply charged positive ion, the Coulomb energy is liberated. Adding a free electron is called electron-capture dissociation (ECD), and is represented by

$[{\ce {M}}+n{\ce {H}}]^{n+}+{\ce {e^{-}->}}\left[[{\ce {M}}+(n-1){\ce {H}}]^{(n-1)+}\right]^{*}{\ce {->fragments}}$

for a multiply protonated molecule M.

#### Electron-transfer dissociation

Adding an electron through an ion-ion reaction is called electron-transfer dissociation (ETD). Similar to electron-capture dissociation, ETD induces fragmentation of cations (e.g. peptides or proteins) by transferring electrons to them. It was invented by Donald F. Hunt, Joshua Coon, John E. P. Syka and Jarrod Marto at the University of Virginia.

ETD does not use free electrons but employs radical anions (e.g. anthracene or azobenzene) for this purpose:

$[{\ce {M}}+n{\ce {H}}]^{n+}+{\ce {A^{-}->}}\left[[{\ce {M}}+(n-1){\ce {H}}]^{(n-1)+}\right]^{*}+{\ce {A->fragments}}$

where A is the anion.

ETD cleaves randomly along the peptide backbone (c and z ions) while side chains and modifications such as phosphorylation are left intact. The technique only works well for higher charge state ions (z>2), however relative to collision-induced dissociation (CID), ETD is advantageous for the fragmentation of longer peptides or even entire proteins. This makes the technique important for top-down proteomics. Much like ECD, ETD is effective for peptides with modifications such as phosphorylation.

Electron-transfer and higher-energy collision dissociation (EThcD) is a combination ETD and HCD where the peptide precursor is initially subjected to an ion/ion reaction with fluoranthene anions in a linear ion trap, which generates c- and z-ions. In the second step HCD all-ion fragmentation is applied to all ETD derived ions to generate b- and y- ions prior to final analysis in the orbitrap analyzer. This method employs dual fragmentation to generate ion- and thus data-rich MS/MS spectra for peptide sequencing and PTM localization.

#### Negative electron-transfer dissociation

Fragmentation can also occur with a deprotonated species, in which an electron is transferred from the species to a cationic reagent in a negative electron transfer dissociation (NETD):

$[{\ce {M}}-n{\ce {H}}]^{n-}+{\ce {A+->}}\left[[{\ce {M}}-n{\ce {H}}]^{(n+1)-}\right]^{*}+{\ce {A->fragments}}$

Following this transfer event, the electron-deficient anion undergoes internal rearrangement and fragments. NETD is the ion/ion analogue of electron-detachment dissociation (EDD).

NETD is compatible with fragmenting peptide and proteins along the backbone at the Cα-C bond. The resulting fragments are usually a•- and x-type product ions.

#### Electron-detachment dissociation

Electron-detachment dissociation (EDD) is a method for fragmenting anionic species in mass spectrometry. It serves as a negative counter mode to electron capture dissociation. Negatively charged ions are activated by irradiation with electrons of moderate kinetic energy. The result is ejection of electrons from the parent ionic molecule, which causes dissociation via recombination.

#### Charge-transfer dissociation

Reaction between positively charged peptides and cationic reagents, also known as charge transfer dissociation (CTD), has recently been demonstrated as an alternative high-energy fragmentation pathway for low-charge state (1+ or 2+) peptides. The proposed mechanism of CTD using helium cations as the reagent is:

${\ce {{[{M}+H]^{1}+}+He+->}}\left[{\ce {[{M}+H]^{2}+}}\right]^{*}+{\ce {He^{0}->fragments}}$

Initial reports are that CTD causes backbone Cα-C bond cleavage of peptides and provides a•- and x-type product ions.

### Photodissociation

The energy required for dissociation can be added by photon absorption, resulting in ion photodissociation and represented by

${\ce {{AB+}+{\mathit {h\nu }}->{A}+B+}}$

where $h\nu$ represents the photon absorbed by the ion. Ultraviolet lasers can be used, but can lead to excessive fragmentation of biomolecules.

#### Infrared multiphoton dissociation

Infrared photons will heat the ions and cause dissociation if enough of them are absorbed. This process is called infrared multiphoton dissociation (IRMPD) and is often accomplished with a carbon dioxide laser and an ion trapping mass spectrometer such as a FTMS.

#### Blackbody infrared radiative dissociation

Blackbody radiation can be used for photodissociation in a technique known as blackbody infrared radiative dissociation (BIRD). In the BIRD method, the entire mass spectrometer vacuum chamber is heated to create infrared light. BIRD uses this radiation to excite increasingly more energetic vibrations of the ions, until a bond breaks, creating fragments. This is similar to infrared multiphoton dissociation which also uses infrared light, but from a different source. BIRD is most often used with Fourier transform ion cyclotron resonance mass spectrometry.

### Surface-induced dissociation

With surface-induced dissociation (SID), the fragmentation is a result of the collision of an ion with a surface under high vacuum. Today, SID is used to fragment a wide range of ions. Years ago, it was only common to use SID on lower mass, singly charged species because ionization methods and mass analyzer technologies weren't advanced enough to properly form, transmit, or characterize ions of high m/z. Over time, self-assembled monolayer surfaces (SAMs) composed of CF3(CF2)10CH2CH2S on gold have been the most prominently used collision surfaces for SID in a tandem spectrometer. SAMs have acted as the most desirable collision targets due to their characteristically large effective masses for the collision of incoming ions. Additionally, these surfaces are composed of rigid fluorocarbon chains, which don't significantly dampen the energy of the projectile ions. The fluorocarbon chains are also beneficial because of their ability to resist facile electron transfer from the metal surface to the incoming ions. SID's ability to produce subcomplexes that remain stable and provide valuable information on connectivity is unmatched by any other dissociation technique. Since the complexes produced from SID are stable and retain distribution of charge on the fragment, this produces a unique, spectra which the complex centers around a narrower m/z distribution. The SID products and the energy at which they form are reflective of the strengths and topology of the complex. The unique dissociation patterns help discover the Quaternary structure of the complex. The symmetric charge distribution and dissociation dependence are unique to SID and make the spectra produced distinctive from any other dissociation technique.

The SID technique is also applicable to ion-mobility mass spectrometry (IM-MS). Three different methods for this technique include analyzing the characterization of topology, intersubunit connectivity, and the degree of unfolding for protein structure. Analysis of protein structure unfolding is the most commonly used application of the SID technique. For Ion-mobility mass spectrometry (IM-MS), SID is used for dissociation of the source activated precursors of three different types of protein complexes: C-reactive protein (CRP), transthyretin (TTR), and concanavalin A (Con A). This method is used to observe the unfolding degree for each of these complexes. For this observation, SID showed the precursor ions' structures that exist before the collision with the surface. IM-MS utilizes the SID as a direct measure of the conformation for each proteins' subunit.

Fourier-transform ion cyclotron resonance are able to provide ultrahigh resolution and high mass accuracy to instruments that take mass measurements. These features make FT-ICR mass spectrometers a useful tool for a wide variety of applications such as several dissociation experiments such as collision-induced dissociation (CID, electron transfer dissociation (ETD), and others. In addition, surface-induced dissociation has been implemented with this instrument for the study of fundamental peptide fragmentation. Specifically, SID has been applied to the study of energetics and the kinetics of gas-phase fragmentation within an ICR instrument. This approach has been used to understand the gas-phase fragmentation of protonated peptides, odd-electron peptide ions, non-covalent ligand-peptide complexes, and ligated metal clusters.

## Quantitative proteomics

Quantitative proteomics is used to determine the relative or absolute amount of proteins in a sample. Several quantitative proteomics methods are based on tandem mass spectrometry. MS/MS has become a benchmark procedure for the structural elucidation of complex biomolecules.

One method commonly used for quantitative proteomics is isobaric tag labeling. Isobaric tag labeling enables simultaneous identification and quantification of proteins from multiple samples in a single analysis. To quantify proteins, peptides are labeled with chemical tags that have the same structure and nominal mass, but vary in the distribution of heavy isotopes in their structure. These tags, commonly referred to as tandem mass tags, are designed so that the mass tag is cleaved at a specific linker region upon higher-energy collisional-induced dissociation (HCD) during tandem mass spectrometry yielding reporter ions of different masses. Protein quantitation is accomplished by comparing the intensities of the reporter ions in the MS/MS spectra. Two commercially available isobaric tags are iTRAQ and TMT reagents.

### Isobaric tags for relative and absolute quantitation (iTRAQ)

An isobaric tag for relative and absolute quantitation (iTRAQ) is a reagent for tandem mass spectrometry that is used to determine the amount of proteins from different sources in a single experiment. It uses stable isotope labeled molecules that can form a covalent bond with the N-terminus and side chain amines of proteins. The iTRAQ reagents are used to label peptides from different samples that are pooled and analyzed by liquid chromatography and tandem mass spectrometry. The fragmentation of the attached tag generates a low molecular mass reporter ion that can be used to relatively quantify the peptides and the proteins from which they originated.

### Tandem mass tag (TMT)

A tandem mass tag (TMT) is an isobaric mass tag chemical label used for protein quantification and identification. The tags contain four regions: mass reporter, cleavable linker, mass normalization, and protein reactive group. TMT reagents can be used to simultaneously analyze 2 to 11 different peptide samples prepared from cells, tissues or biological fluids. Recent developments allow up to 16 and even 18 samples (16plex or 18plex respectively) to be analyzed. Three types of TMT reagents are available with different chemical reactivities: (1) a reactive NHS ester functional group for labeling primary amines (TMTduplex, TMTsixplex, TMT10plex plus TMT11-131C), (2) a reactive iodoacetyl functional group for labeling free sulfhydryls (iodoTMT) and (3) reactive alkoxyamine functional group for labeling of carbonyls (aminoxyTMT).

### Multiplexed DIA (plexDIA)

The progress in data independent acquisition (DIA) enabled multiplexed quantitative proteomics with non-isobaric mass tags and a new method called plexDIA introduced in 2021. This new approach increases the number of data points by parallelizing both samples and peptides, thus achieving multiplicative gains. It has the potential to continue scaling proteomic throughput with new mass tags and algorithms. plexDIA is applicable to both bulk and single-cell samples and is particularly powerful for single-cell proteomics.

## Applications

### Peptides

Tandem mass spectrometry can be used for protein sequencing. When intact proteins are introduced to a mass analyzer, this is called "top-down proteomics" and when proteins are digested into smaller peptides and subsequently introduced into the mass spectrometer, this is called "bottom-up proteomics". Shotgun proteomics is a variant of bottom up proteomics in which proteins in a mixture are digested prior to separation and tandem mass spectrometry.

Tandem mass spectrometry can produce a peptide sequence tag that can be used to identify a peptide in a protein database. A notation has been developed for indicating peptide fragments that arise from a tandem mass spectrum. Peptide fragment ions are indicated by a, b, or c if the charge is retained on the N-terminus and by x, y or z if the charge is maintained on the C-terminus. The subscript indicates the number of amino acid residues in the fragment. Superscripts are sometimes used to indicate neutral losses in addition to the backbone fragmentation, * for loss of ammonia and ° for loss of water. Although peptide backbone cleavage is the most useful for sequencing and peptide identification other fragment ions may be observed under high energy dissociation conditions. These include the side chain loss ions d, v, w and ammonium ions and additional sequence-specific fragment ions associated with particular amino acid residues.

### Oligosaccharides

Oligosaccharides may be sequenced using tandem mass spectrometry in a similar manner to peptide sequencing. Fragmentation generally occurs on either side of the glycosidic bond (b, c, y and z ions) but also under more energetic conditions through the sugar ring structure in a cross-ring cleavage (x ions). Again trailing subscripts are used to indicate position of the cleavage along the chain. For cross ring cleavage ions the nature of the cross ring cleavage is indicated by preceding superscripts.

### Oligonucleotides

Tandem mass spectrometry has been applied to DNA and RNA sequencing. A notation for gas-phase fragmentation of oligonucleotide ions has been proposed.

### Newborn screening

Newborn screening is the process of testing newborn babies for treatable genetic, endocrinologic, metabolic and hematologic diseases. The development of tandem mass spectrometry screening in the early 1990s led to a large expansion of potentially detectable congenital metabolic diseases that affect blood levels of organic acids.

**Small molecule analysis**

It has been shown that tandem mass spectrometry data is highly consistent across instrument and manufacturer platforms including quadrupole time-of-flight (QTOF) and Q Exactive instrumentation, especially at 20 eV.

## Limitation

Tandem mass spectrometry cannot be applied for single-cell analyses as it is insensitive to analyze such small amounts of a cell. These limitations are primarily due to a combination of inefficient ion production and ion losses within the instruments due to chemical noise sources of solvents.

## Future outlook

Tandem mass spectrometry will be a useful tool for protein characterization, nucleoprotein complexes, and other biological structures. However, some challenges left such as analyzing the characterization of the proteome quantitatively and qualitatively.
