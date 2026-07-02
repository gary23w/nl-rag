---
title: "Single particle analysis"
source: https://en.wikipedia.org/wiki/Single_particle_analysis
domain: cryo-em
license: CC-BY-SA-4.0
tags: cryo-electron microscopy, single particle analysis, structural biology, vitreous ice
fetched: 2026-07-02
---

# Single particle analysis

**Single particle analysis** is a group of related computerized image processing techniques used to analyze images from transmission electron microscopy (TEM). These methods were developed to improve and extend the information obtainable from TEM images of particulate samples, typically proteins or other large biological entities such as viruses. Individual images of stained or unstained particles are very noisy, making interpretation difficult. Combining several digitized images of similar particles together gives an image with stronger and more easily interpretable features. An extension of this technique uses single particle methods to build up a three-dimensional reconstruction of the particle. Using cryo-electron microscopy it has become possible to generate reconstructions with sub-nanometer, near-atomic resolution resolution first in the case of highly symmetric viruses, and now in smaller, asymmetric proteins as well.

## Techniques

Single particle analysis can be done on both negatively stained and vitreous ice-embedded transmission electron cryomicroscopy (CryoTEM) samples. Single particle analysis methods are, in general, reliant on the sample being homogeneous, although techniques for dealing with conformational heterogeneity are being developed.

Images (micrographs) are taken with an electron microscope using charged-coupled device (CCD) detectors coupled to a phosphorescent layer (in the past, they were instead collected on film and digitized using high-quality scanners). The image processing is carried out using specialized software programs, often run on multi-processor computer clusters. Depending on the sample or the desired results, various steps of two- or three-dimensional processing can be done.

### Alignment and classification

Biological samples, and especially samples embedded in thin vitreous ice, are highly radiation sensitive, thus only low electron doses can be used to image the sample. This low dose, as well as variations in the metal stain used (if used) means images have high noise relative to the signal given by the particle being observed. By aligning several similar images to each other so they are in register and then averaging them, an image with higher signal-to-noise ratio can be obtained. As the noise is mostly randomly distributed and the underlying image features constant, by averaging the intensity of each pixel over several images only the constant features are reinforced. Typically, the optimal alignment (a translation and an in-plane rotation) to map one image onto another is calculated by cross-correlation.

However, a micrograph often contains particles in multiple different orientations and/or conformations, and so to get more representative image averages, a method is required to group similar particle images together into multiple sets. This is normally carried out using one of several data analysis and image classification algorithms, such as multi-variate statistical analysis and hierarchical ascendant classification, or *k*-means clustering.

Often data sets of tens of thousands of particle images are used, and to reach an optimal solution an iterative procedure of alignment and classification is used, whereby strong image averages produced by classification are used as reference images for a subsequent alignment of the whole data set.

### Image filtering

Image filtering (band-pass filtering) is often used to reduce the influence of high and/or low spatial frequency information in the images, which can affect the results of the alignment and classification procedures. This is particularly useful in negative stain images. The algorithms make use of fast Fourier transforms (FFT), often employing Gaussian shaped soft-edged masks in reciprocal space to suppress certain frequency ranges. High-pass filters remove low spatial frequencies (such as ramp or gradient effects), leaving the higher frequencies intact. Low-pass filters remove high spatial frequency features and have a blurring effect on fine details.

### Contrast transfer function

Due to the nature of image formation in the electron microscope, bright-field TEM images are obtained using significant underfocus. This, along with features inherent in the microscope's lens system, creates blurring of the collected images visible as a point spread function. The combined effects of the imaging conditions are known as the contrast transfer function (CTF), and can be approximated mathematically as a function in reciprocal space. Specialized image processing techniques such as phase flipping and amplitude correction / Wiener filtering can (at least partially) correct for the CTF, and allow high resolution reconstructions.

### Three-dimensional reconstruction

Transmission electron microscopy images are projections of the object showing the distribution of density through the object, similar to medical X-rays. By making use of the projection-slice theorem a three-dimensional reconstruction of the object can be generated by combining many images (2D projections) of the object taken from a range of viewing angles. Proteins in vitreous ice ideally adopt a random distribution of orientations (or viewing angles), allowing a fairly isotropic reconstruction if a large number of particle images are used. This contrasts with electron tomography, where the viewing angles are limited due to the geometry of the sample/imaging set up, giving an anisotropic reconstruction. Filtered back projection is a commonly used method of generating 3D reconstructions in single particle analysis, although many alternative algorithms exist.

Before a reconstruction can be made, the orientation of the object in each image needs to be estimated. Several methods have been developed to work out the relative Euler angles of each image. Some are based on common lines (common 1D projections and sinograms), others use iterative projection matching algorithms. The latter works by beginning with a simple, low resolution 3D starting model and compares the experimental images to projections of the model and creates a new 3D to bootstrap towards a solution.

Methods are also available for making 3D reconstructions of helical samples (such as tobacco mosaic virus), taking advantage of the inherent helical symmetry. Both real space methods (treating sections of the helix as single particles) and reciprocal space methods (using diffraction patterns) can be used for these samples.

### Tilt methods

The specimen stage of the microscope can be tilted (typically along a single axis), allowing the single particle technique known as random conical tilt. An area of the specimen is imaged at both zero and at high angle (~60-70 degrees) tilts, or in the case of the related method of orthogonal tilt reconstruction, +45 and −45 degrees. Pairs of particles corresponding to the same object at two different tilts (tilt pairs) are selected, and by following the parameters used in subsequent alignment and classification steps a three-dimensional reconstruction can be generated relatively easily. This is because the viewing angle (defined as three Euler angles) of each particle is known from the tilt geometry.

3D reconstructions from random conical tilt suffer from missing information resulting from a restricted range of orientations. Known as the missing cone (due to the shape in reciprocal space), this causes distortions in the 3D maps. However, the missing cone problem can often be overcome by combining several tilt reconstructions. Tilt methods are best suited to negatively stained samples, and can be used for particles that adsorb to the carbon support film in preferred orientations. The phenomenon known as charging or beam-induced movement makes collecting high-tilt images of samples in vitreous ice challenging.

### Map visualization and fitting

Various software programs are available that allow viewing the 3D maps. These often enable the user to manually dock in protein coordinates (structures from X-ray crystallography, NMR, or a computational model such as one found in the AlphaFold Protein Structure Database) of subunits into the electron density. Several programs can also fit subunits computationally; as of the 2020s using these programs tend to produce better accuracy than manual docking because they can perform labor-intensive tasks such as:

- The scale of SPA-derived maps depends on knowing the pixel size (angstorms per pixel), which is not always accurate. Programs can automatically correct for this difference by using coordinate data or by using knowledge of chemical bonds.
- Many proteins are made up of several roughly rigid protein domains linked by flexible parts. Pre-existing coordinate data, whether experimental or computational, may not exactly match the inter-domain positioning of the cyro-EM map. Modern programs can automatically "chop" pre-existing coordinate data into individual domains and fit them in individually.

For higher-resolution structures, it is possible to build the macromolecule directly, without prior structural knowledge from other methods. The traditional manual method involves visually identifying key residues, most commonly big aromatic ones, as "anchors" onto the known sequence of the protein being analyzed. It is also theoretically possible but very difficult to do it without knowledge of the sequence by reading it "off the map". Computer algorithms have been developed for both tasks with superhuman efficiency and accuracy, even for the case of needing to identify an unknown sequence.

### Map refining

An initial "fit" of the map is iteratively refined to produce better results, with "good" defined by a combination of map agreement and rules from chemical geometry. A ridid fit using pre-existing protein coordinates often disagree with the map in turns of slight geometric morphing (shifting and rotation of pieces) and sidechain orientations (rotamers), which is addressed in this step. In more involved cases, a force field (such as Rosetta and AQuaRef) may be used to estimate the free energy of a given model, guiding the reconstruction to a lower-energy (more stable and more plausible) arrangement of atoms. Force fields are especially beneficial for low-resolution maps, where improved fits tend to show better matches to higher-resolution models of the same molecule. Force fields are also useful for resolving noncovalent interactions such as hydrogen bonds.

As high-resolution cryo-EM models are relative new, quality control tools are not as plentiful as it is for X-ray models. Nevertheless, cryo-EM ("real space") versions of the difference density map, cross-validation using a "free" map (comparable to the use of a free R-factor), and various structure validation tools have begun to appear.

## Examples

Note: 1 Å = 0.1 nm. Although the angstrom is not an SI unit, it is very commonly used in structural biology as the scales are appropriate for discussing chemical bonds.

Non-atomic models:

- The tyrosine-protein kinase SYK was reconstructed to a resolution of 24 Å in 2007. At this kind of resolution, atoms are invisible and the map appears as a "blob". For this reason cryo-EM SPA is nicknamed "blobology".

Atomic models:

- *Methanococcus maripaludis* chaperonin, a machine for folding other proteins, which get trapped within the shell. Reconstructed to 4.3 Å in 2010, PDB: 3IYE, 3IYF. Cyro-EM allows scientists to capture different states of the protein complex, with the "lid" open and closed.
- Yeast fatty acid synthase (FAS), a huge enzyme complex responsible for building the long chain fatty acids essential for cellular life. Resolved to 5.9 Å in 2010. Cyro-EM allows the scientists to observe the FAS in a state not seen in X-ray crystal structures, providing insight into how it moves its reactant (substrate). (The atomic model was not submitted to the Protein Data Bank.)
- Aquareovirus, a non-enveloped virus infecting fish and other aquatic animals. The infectious subvirion particle in the "primed" state was reconstructed to 3.3 Å in 2010, with direct observation of amino acid sidechains. This structure allows scientists to understand the nature of "priming" which is required to enable non-enveloped viruses to penetrate cell membranes.

Brighter electron sources have allowed truly atomic resolution to be achieved for maps, with a record of 1.22 Å set in 2020.

## Primary database

- EM Data Bank Archived 2019-02-05 at the Wayback Machine (EM Data Bank) for maps
- Protein Data Bank for atomic fits
