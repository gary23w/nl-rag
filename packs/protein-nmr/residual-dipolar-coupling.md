---
title: "Residual dipolar coupling"
source: https://en.wikipedia.org/wiki/Residual_dipolar_coupling
domain: protein-nmr
license: CC-BY-SA-4.0
tags: nuclear magnetic resonance, protein dynamics, chemical shift, spin
fetched: 2026-07-02
---

# Residual dipolar coupling

The **residual dipolar coupling** between two spins in a molecule occurs if the molecules in solution exhibit a partial alignment leading to an incomplete averaging of spatially anisotropic dipolar couplings.

Partial molecular alignment leads to an incomplete averaging of anisotropic magnetic interactions such as the magnetic dipole-dipole interaction (also called dipolar coupling), the chemical shift anisotropy, or the electric quadrupole interaction. The resulting so-called *residual* anisotropic magnetic interactions are useful in biomolecular NMR spectroscopy.

## History and pioneering works

NMR spectroscopy in partially oriented media was reported by Alfred Saupe. After this initiation, several NMR spectra in various liquid crystalline phases were reported (see *e.g.* ).

A second technique for partial alignment that is not limited by a minimum anisotropy is strain-induced alignment in a gel (SAG). The technique was extensively used to study the properties of polymer gels by means of high-resolution deuterium NMR, but only lately gel alignment was used to induce RDCs in molecules dissolved into the gel. SAG allows the unrestricted scaling of alignment over a wide range and can be used for aqueous as well as organic solvents, depending on the polymer used. As a first example in organic solvents, RDC measurements in stretched polystyrene (PS) gels swollen in CDCl3 were reported as a promising alignment method.

In 1995, NMR spectra were reported for cyanometmyoglobin, which has a very highly anisotropic paramagnetic susceptibility. When taken at very high field, these spectra may contain data that can usefully complement NOEs in determining a tertiary fold.

In 1996 and 1997, the RDCs of a diamagnetic protein ubiquitin were reported. The results were in good agreement with the crystal structures.

## Physics

The secular dipolar coupling Hamiltonian of two spins, I and $S,$ is given by:

$H_{\mathrm {D} }={\frac {\hbar ^{2}\gamma _{I}\gamma _{S}}{4\pi r_{IS}^{3}}}[1-3\cos ^{2}\theta ](3I_{z}S_{z}-{\vec {I}}\cdot {\vec {S}})$

where

- $\hbar$ is the reduced Planck constant.
- $\gamma _{I}$ and $\gamma _{S}$ are the gyromagnetic ratios of spin I and spin S respectively.
- $r_{IS}$ is the inter-spin distance.
- *$\theta$* is the angle between the inter-spin vector and the external magnetic field.
- ${\vec {I}}$ and ${\vec {S}}$ are vectors of spin operators.

The above equation can be rewritten in the following form:

$H_{\mathrm {D} }=D_{IS}(\theta )[2I_{z}S_{z}-(I_{x}S_{x}+I_{y}S_{y})]\!$

where

$D_{IS}(\theta )={\frac {\hbar ^{2}\gamma _{I}\gamma _{S}}{4\pi r_{IS}^{3}}}[1-3\cos ^{2}\theta ].\!$

In isotropic solution molecular tumbling reduces the average value of $D_{IS}$ to zero. We thus observe no dipolar coupling. If the solution is not isotropic then the average value of $D_{IS}$ may be different from zero, and one may observe *residual* couplings.

The positions of magnetic nuclei are often relatively restricted in solid sample, so there are a large number of dipolar coupling dominating in different nuclei. The static value of dipole coupling may reach thousands of hertz, which will cause serious broadening of the spectral peaks in the solid-state NMR spectra. In liquid samples, due to isotropic tumbling of the molecule, the dipole coupling effect is averaged to zero. Although high-resolution spectra can be thus obtained in the solution, structural information provided by dipolar coupling becomes lost. When compound molecules are placed in a weakly oriented medium, the movement of the molecules is partially restricted. Compared with the solid sample, the static value of the dipole coupling is reduced by around 103 times. Compared with the liquid sample, the dipole coupling effect is not completely averaged, and it retains a smaller residual value, that is residual dipolar coupling (RDC).

RDC can be positive or negative, depending on the range of angles that are sampled.

In addition to static distance and angular information, RDCs may contain information about a molecule's internal motion. To each atom in a molecule one can associate a motion tensor **B**, that may be computed from RDCs according to the following relation:

$D_{IS}=-{\frac {\mu _{0}\gamma _{I}\gamma _{S}h}{(2\pi r_{IS})^{3}}}BA\!$

where A is the molecular alignment tensor. The rows of B contain the motion tensors for each atom. The motion tensors also have five degrees of freedom. From each motion tensor, 5 parameters of interest can be computed. The variables Si2, ηi, αi, βi and γi are used to denote these 5 parameters for atom i. Si2 is the magnitude of atom i's motion; ηi is a measure of the anisotropy of atom i's motion; αi and βi are related to the polar coordinates of the bond vector expressed in the initial arbitrary reference frame (i.e., the PDB frame). If the motion of the atom is anisotropic (i.e., ηi = 0), the final parameter, γi measures the principal orientation of the motion.

Note that the RDC-derived motion parameters are local measurements.

## Measurement

Any RDC measurement in solution consists of two steps, aligning the molecules and NMR studies:

### Methods for aligning molecules

For diamagnetic molecules at moderate field strengths, molecules have little preference in orientation, the tumbling samples a nearly isotropic distribution, and average dipolar couplings goes to zero. Actually, most molecules have preferred orientations in the presence of a magnetic field, because most have anisotropic magnetic susceptibility tensors, Χ.

The method is most suitable for systems with large values for magnetic susceptibility tensor. This includes: Protein-nucleic acid complex, nucleic acids, proteins with large number of aromatic residues, porphyrin containing proteins and metal binding proteins (metal may be replaced by lanthanides).

For a fully oriented molecule, the dipolar coupling for an 1H-15N amide group would be over 20 kHz, and a pair of protons separated by 5 Å would have up to ~1 kHz coupling. However the degree of alignment achieved by applying magnetic field is so low that the largest 1H-15N or 1H-13C dipolar couplings are <5 Hz. Therefore, many different alignment media have been designed:

- Lipid bicelles (with large magnetic susceptibility): measured RDCs were of the order of hundreds of Hz.
- Liquid crystalline bicelles: measured RDCs were between -40 and +20 Hz.
- Rod-shaped viruses, including filamentous bacteriophage (large anisotropic magnetic susceptibility).
- DNA nanotubes (compatible with detergents used to solubilize membrane proteins)

### NMR experiments

There are numerous methods that have been designed to accurately measure coupling constant between nuclei. They have been classified into two groups: *frequency based methods* where separation of peaks centers (splitting) is measured in a frequency domain, and *intensity based methods* where the coupling is extracted from the resonance intensity instead of splitting. The two methods complement each other as each of them is subject to a different kind of systematic errors. Here are the prototypical examples of NMR experiments belonging to each of the two groups:

- *Intensity methods*: quantitative J-modulation experiment and phase modulated methods
- *frequency resolved methods*: SCE-HSQC, E. COSY and spin state selective experiments

## Structural biology

RDC measurement provides information on the global folding of the protein or protein complex. As opposed to traditional NOE based NMR structure determinations, RDCs provide long distance structural information. It also provides information about the dynamics in molecules on time scales slower than nanoseconds.

### Studies of biomolecular structure

Most NMR studies of protein structure are based on analysis of the Nuclear Overhauser effect, NOE, between different protons in the protein. Because the NOE depends on the inverted sixth power of the distance between the nuclei, r−6, NOEs can be converted into distance restraints that can be used in molecular dynamics-type structure calculations. RDCs provide orientational restraints rather than distance restraints, and has several advantages over NOEs:

- RDCs give information about the angle relative to the external magnetic field, which means that it can give information about the relative orientation of parts of the molecule that are far apart in the structure.
- In large molecules (>25kDa) it is often difficult to record NOEs due to spin diffusion. This is not a problem with RDCs.
- Analysis of a high number of NOEs can be very time-consuming.

Provided that a very complete set of RDCs is available, it has been demonstrated for several model systems that molecular structures can be calculated exclusively based on these anisotropic interactions, without recourse to NOE restraints. However, in practice, this is not achievable and RDC is used mainly to refine a structure determined by NOE data and J-coupling. One problem with using dipolar couplings in structure determination is that a dipolar coupling does not uniquely describe an internuclear vector orientation. Moreover, if a very small set of dipolar couplings are available, the refinement may lead to a structure worse than the original one. For a protein with N aminoacids, 2N RDC constraint for backbone is the minimum needed for an accurate refinement.

The information content of an individual RDC measurement for a specific bond vector (such as a specific backbone NH bond in a protein molecule) can be understood by showing the target curve that traces out directions of perfect agreement between the observed RDC value and the value calculated from the model. Such a curve (see figure) has two symmetrical branches that lie on a sphere with its polar axis along the magnetic field direction. Their height from the sphere's equator depends on the magnitude of the RDC value and their shape depends on the "rhombicity" (asymmetry) of the molecular alignment tensor. If the molecular alignment were completely symmetrical around the magnetic field direction, the target curve would just consist of two circles at the same angle from the poles as the angle $\theta$ that the specific bond vector makes to the applied magnetic field.

In the case of elongated molecules such as RNA, where local torsional information and short distances are not enough to constrain the structures, RDC measurements can provide information about the orientations of specific chemical bonds throughout a nucleic acid with respect to a single coordinate frame. Particularly, RNA molecules are proton-poor and overlap of ribose resonances make it very difficult to use J-coupling and NOE data to determine the structure. Moreover, RDCs between nuclei with a distance larger than 5-6 Å can be detected. This distance is too much for generation of NOE signal. This is because RDC is proportional to r−3 whereas NOE is proportional to r−6.

RDC measurements have also been proved to be extremely useful for a rapid determination of the relative orientations of units of known structures in proteins. In principle, the orientation of a structural subunit, which may be as small as a turn of a helix or as large as an entire domain, can be established from as few as five RDCs per subunit.

### Protein dynamics

As a RDC provides spatially and temporally averaged information about an angle between the external magnetic field and a bond vector in a molecule, it may provide rich geometrical information about dynamics on a slow timescale (>10−9 s) in proteins. In particular, due to its radial dependence the RDC is in particular sensitive to large-amplitude angular processes An early example by Tolman *et al.* found previously published structures of myoglobin insufficient to explain measured RDC data, and devised a simple model of slow dynamics to remedy this. However, for many classes of proteins, including intrinsically disordered proteins, analysis of RDCs becomes more involved, as defining an alignment frame is not trivial. The problem can be addressed by circumventing the necessity of explicitly defining the alignment frame.
