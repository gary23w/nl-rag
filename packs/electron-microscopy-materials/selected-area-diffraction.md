---
title: "Selected area diffraction"
source: https://en.wikipedia.org/wiki/Selected_area_diffraction
domain: electron-microscopy-materials
license: CC-BY-SA-4.0
tags: scanning electron, material imaging, backscattered electron, energy dispersive
fetched: 2026-07-02
---

# Selected area diffraction

**Selected area (electron) diffraction** (abbreviated as **SAD** or **SAED**) is a crystallographic experimental technique typically performed using a transmission electron microscope (TEM). It is a specific case of electron diffraction used primarily in material science and solid state physics as one of the most common experimental techniques. Especially with appropriate analytical software, SAD patterns (SADP) can be used to determine crystal orientation, measure lattice constants or examine its defects.

## Principle

In transmission electron microscope, a thin crystalline sample is illuminated by parallel beam of electrons accelerated to energy of hundreds of kiloelectron volts. At these energies samples are transparent for the electrons if the sample is thinned enough (typically less than 100 nm). Due to the wave–particle duality, the high-energetic electrons behave as matter waves with wavelength of a few thousandths of a nanometer. The relativistic wavelength is given by

$\lambda ={\frac {hc}{\sqrt {eV(2m_{0}c^{2}+eV)}}},$

where h is the Planck constant, $m_{0}$ is the electron rest mass, e is the elementary charge, c is the speed of light and V is an electric potential accelerating the electrons (also called acceleration voltage). For instance the acceleration voltage of 200 kV results in a wavelength of 2.508 pm.

Since the spacing between atoms in crystals is about a hundred times larger, the electrons are diffracted on the crystal lattice, acting as a diffraction grating. Due to the diffraction, part of the electrons is scattered at particular angles (diffracted beams), while others pass through the sample without changing their direction (transmitted beams). In order to determine the diffraction angles, the electron beam normally incident to the atomic lattice can be seen as a planar wave, which is re-transmitted by each atom as a spherical wave. Due to the constructive interference, the spherical waves from number of diffracted beams under angles $\theta _{n}$ given, approximately, by the Bragg condition

$d\sin \theta _{n}=n\lambda ,$

where the integer n is an order of diffraction and d is the distance between atoms (if only one row of atoms is assumed as in the illustration aside) or a distance between atomic planes parallel to the beam (in a real 3D atomic structure). For finite samples this equation is only approximately correct.

After being deflected by the microscope's magnetic lens, each set of initially parallel beams intersect in the back focal plane forming the diffraction pattern. The transmitted beams intersect right in the optical axis. The diffracted beams intersect at certain distance from the optical axis (corresponding to interplanar distance of the planes diffracting the beams) and under certain azimuth (corresponding to the orientation of the planes diffracting the beams). This allows to form a pattern of bright spots typical for SAD.

SAD is called "selected" because it allows the user to select the sample area from which the diffraction pattern will be acquired. For this purpose, there is a selected area aperture located below the sample holder. It is a metallic sheet with several differently sized holes which can be inserted into the beam. The user can select the aperture of appropriate size and position it so that it only allows to pass the portion of beam corresponding to the selected area. Therefore, the resulting diffraction pattern will only reflect the area selected by the aperture. This allows to study small objects such as crystallites in polycrystalline material with a broad parallel beam.

Character of the resulting diffraction image depends on whether the beam is diffracted by one single crystal or by number of differently oriented crystallites for instance in a polycrystalline material. The single-crystalline diffractogram depicts a regular pattern of bright spots. This pattern can be seen as a two-dimensional projection of reciprocal crystal lattice. If there are more contributing crystallites, the diffraction image becomes a superposition of individual crystals' diffraction patterns. Ultimately, this superposition contains diffraction spots of all possible crystallographic plane systems in all possible orientations. For two reasons, these conditions result in a diffractogram of concentric rings:

1. There are discrete spacings between various parallel crystallographic planes and therefore the beams satisfying the diffraction condition can only form diffraction spots in discrete distances from the transmitted beam.
2. There are all possible orientations of crystallographic planes and therefore the diffraction spots are formed around the transmitted beam in the whole 360-degree azimuthal range.

## Interpretation and analysis

SAD analysis is widely used in material research for its relative simplicity and high information value. Once the sample is prepared and examined in a modern transmission electron microscope, the device allows for a routine diffraction acquisition in a matter of seconds. If the images are interpreted correctly, they can be used to identify crystal structures, determine their orientations, measure crystal characteristics, examine crystal defects or material textures. The course of analysis depends on whether the diffractogram depicts ring or spot diffraction pattern and on the quantity to be determined.

Software tools based on computer vision algorithms simplifies quantitative analysis.

### Spot diffraction pattern

If the SAD is taken from one a or a few single crystals, the diffractogram depicts a regular pattern of bright spots. Since the diffraction pattern can be seen as a two-dimensional projection of reciprocal crystal lattice, the pattern can be used to measure lattice constants, specifically the distances and angles between crystallographic planes. The lattice parameters are typically distinctive for various materials and their phases which allows to identify the examined material or at least differentiate between possible candidates.

Even though the SAD-based analyses were not considered quantitative for a long time, computer tools brought accuracy and repeatability allowing to routinely perform accurate measurements of interplanar distances or angles on appropriately calibrated microscopes. Tools such as CrysTBox are capable of automated analysis achieving sub-pixel precision.

If the sample is tilted against the electron beam, diffraction conditions are satisfied for different set of crystallographic planes yielding different constellation of diffraction spots. This allows to determine the crystal orientation, which can be used for instance to set up the orientation needed for particular experiment, to determine misorientation between adjacent grains or crystal twins. Since different sample orientations provide different projections of the reciprocal lattice, they provide an opportunity to reconstruct the three-dimensional information lost in individual projections. A series of diffractograms varying in tilt can be acquired and processed with diffraction tomography analysis in order to reconstruct an unknown crystal structure.

SAD can also be used to analyze crystal defects such as stacking faults.

### Ring diffraction pattern

Ring diffraction image of

MgO

as recorded (left) and processed with CrysTBox ringGUI (right).

If the illuminated area selected by the aperture covers many differently oriented crystallites, their diffraction patterns superimpose forming an image of concentric rings. The ring diffractogram is typical for polycrystalline samples, powders or nanoparticles. Diameter of each ring corresponds to interplanar distance of a plane system present in the sample. Instead of information about individual grains or the sample orientation, this diffractogram provides more of a statistical information for instance about overall crystallinity or texture. Textured materials are characteristic by a non-uniform intensity distribution along the ring circumference despite crystallinity sufficient for generating smooth rings. Ring diffractograms can be also used to discriminate between nanocrystalline and amorphous phases.

Not all the features depicted in the diffraction image are necessarily wanted. The transmitted beam is often too strong and needs to be shadowed with a beam-stopper in order to protect the camera. The beam-stopper typically shadows part of the useful information as well. Towards the rings center, the background intensity also gradually increases lowering the contrast of diffraction rings. Modern analytical software allows to minimize such unwanted image features and together with other functionalities improves the image readability it helps with image interpretation.

## Relation to other techniques

An SADP is acquired under parallel electron illumination. In the case of convergent beam, a convergent beam electron diffraction (CBED) is achieved. The beam used in SAD is broad illuminating a wide sample area. In order to analyze only a specific sample area, the selected area aperture in the image plane is used. This is in contrast with nanodiffraction, where the site-selectivity is achieved using a beam condensed to a narrow probe. SAD is important in direct imaging for instance when orienting the sample for high resolution microscopy or setting up dark-field imaging conditions.

High-resolution electron microscope images can be transformed into an artificial diffraction pattern using Fourier transform. Then, they can be processed the same way as real diffractograms allowing to determine crystal orientation, measure interplanar angles and distances even with picometric precision.

SAD is similar to X-ray diffraction, but unique in that areas as small as several hundred nanometres in size can be examined, whereas X-ray diffraction typically samples areas much larger. It is also similar to low-energy electron diffraction (LEED), though this uses back-scattered rather than transmitted electrons and at low energies, therefore being much more surface-sensitive.
