---
title: "Confocal microscopy"
source: https://en.wikipedia.org/wiki/Confocal_microscopy
domain: raman-spectroscopy
license: CC-BY-SA-4.0
tags: inelastic scattering, vibrational mode, stokes shift, surface enhanced
fetched: 2026-07-02
---

# Confocal microscopy

**Confocal microscopy** is an optical imaging technique for increasing optical resolution and contrast of a micrograph by means of using a spatial pinhole to block out-of-focus light in image formation. Capturing multiple two-dimensional images at different depths in a sample enables the reconstruction of three-dimensional structures (a process known as optical sectioning) within an object. This technique is used extensively in the scientific and industrial communities and typical applications are in life sciences, semiconductor inspection and materials science.

Light travels through the sample under a conventional microscope as far into the specimen as it can penetrate, while a confocal microscope only focuses a smaller beam of light at one narrow depth level at a time. The CLSM achieves a controlled and highly limited depth of field.

## Basic concept

The principle of confocal imaging was patented in 1957 by Marvin Minsky and aims to overcome some limitations of traditional wide-field fluorescence microscopes. In a conventional (i.e., wide-field) fluorescence microscope, the entire specimen is flooded evenly in light from a light source. All parts of the sample can be excited at the same time and the resulting fluorescence is detected by the microscope's photodetector or camera including a large unfocused background part. In contrast, a confocal microscope uses point illumination (see Point Spread Function) and a pinhole in an optically conjugate plane in front of the detector to eliminate out-of-focus signal – the name "confocal" stems from this configuration. As only light produced by fluorescence very close to the focal plane can be detected, the image's optical resolution, particularly in the sample depth direction, is much better than that of wide-field microscopes. However, as much of the light from sample fluorescence is blocked at the pinhole, this increased resolution is at the cost of decreased signal intensity – so long exposures are often required. To offset this drop in signal after the *pinhole*, the light intensity is detected by a sensitive detector, usually a photomultiplier tube (PMT) or avalanche photodiode, transforming the light signal into an electrical one.

As only one point in the sample is illuminated at a time, 2D or 3D imaging requires scanning over a regular raster (i.e. a rectangular pattern of parallel scanning lines) in the specimen. The beam is scanned across the sample in the horizontal plane by using one or more (servo controlled) oscillating mirrors. This scanning method usually has a low reaction latency and the scan speed can be varied. Slower scans provide a better signal-to-noise ratio, resulting in better contrast.

The achievable thickness of the focal plane is defined mostly by the wavelength of the used light divided by the numerical aperture of the objective lens, but also by the optical properties of the specimen. The thin optical sectioning possible makes these types of microscopes particularly good at 3D imaging and surface profiling of samples.

Successive slices make up a 'z-stack', which can either be processed to create a 3D image, or it is merged into a 2D stack (predominately the maximum pixel intensity is taken, other common methods include using the standard deviation or summing the pixels).

Confocal microscopy provides the capacity for direct, noninvasive, serial optical sectioning of intact, thick, living specimens with a minimum of sample preparation as well as a marginal improvement in lateral resolution compared to wide-field microscopy. Biological samples are often treated with fluorescent dyes to make selected objects visible. However, the actual dye concentration can be low to minimize the disturbance of biological systems: some instruments can track single fluorescent molecules. Also, transgenic techniques can create organisms that produce their own fluorescent chimeric molecules (such as a fusion of GFP, green fluorescent protein with the protein of interest). Confocal microscopes work on the principle of point excitation in the specimen (diffraction limited spot) and point detection of the resulting fluorescent signal. A pinhole at the detector provides a physical barrier that blocks out-of-focus fluorescence. Only the in-focus, or central spot of the Airy disk, is recorded.

## Techniques used for horizontal scanning

Four types of confocal microscopes are commercially available:

**Confocal laser scanning microscopes** use multiple mirrors (typically 2 or 3 scanning linearly along the x- and the y- axes) to scan the laser across the sample and "descan" the image across a fixed pinhole and detector. This process is usually slow and does not work for live imaging, but can be useful to create high-resolution representative images of fixed samples.

**Spinning-disk** (Nipkow disk) confocal microscopes use a series of moving pinholes on a disc to scan spots of light. Since a series of pinholes scans an area in parallel, each pinhole is allowed to hover over a specific area for a longer amount of time thereby reducing the excitation energy needed to illuminate a sample when compared to laser scanning microscopes. Decreased excitation energy reduces phototoxicity and photobleaching of a sample often making it the preferred system for imaging live cells or organisms.

**Microlens enhanced** or **dual spinning-disk** confocal microscopes work under the same principles as spinning-disk confocal microscopes except a second spinning-disk containing micro-lenses is placed before the spinning-disk containing the pinholes. Every pinhole has an associated microlens. The micro-lenses act to capture a broad band of light and focus it into each pinhole significantly increasing the amount of light directed into each pinhole and reducing the amount of light blocked by the spinning-disk. Microlens enhanced confocal microscopes are therefore significantly more sensitive than standard spinning-disk systems. Yokogawa Electric invented this technology in 1992.

**Programmable array microscopes (PAM)** use an electronically controlled spatial light modulator (SLM) that produces a set of moving pinholes. The SLM is a device containing an array of pixels with some property (opacity, reflectivity or optical rotation) of the individual pixels that can be adjusted electronically. The SLM contains microelectromechanical mirrors or liquid crystal components. The image is usually acquired by a charge-coupled device (CCD) camera.

Each of these classes of confocal microscope have particular advantages and disadvantages. Most systems are either optimized for recording speed (i.e. video capture) or high spatial resolution. Confocal laser scanning microscopes can have a programmable sampling density and very high resolutions while Nipkow and PAM use a fixed sampling density defined by the camera's resolution. Imaging frame rates are typically slower for single point laser scanning systems than spinning-disk or PAM systems. Commercial spinning-disk confocal microscopes achieve frame rates of over 50 per second – a desirable feature for dynamic observations such as live cell imaging.

Cutting-edge development of confocal laser scanning microscopy now allows better than standard video rate (60 frames per second) imaging by using multiple microelectromechanical scanning mirrors.

Confocal X-ray fluorescence imaging is a newer technique that allows control over depth, in addition to horizontal and vertical aiming, for example, when analyzing buried layers in a painting.

## Resolution enhancement

CLSM is a scanning imaging technique in which the resolution obtained is best explained by comparing it with another scanning technique like that of the scanning electron microscope (SEM). CLSM has the advantage of not requiring a probe to be suspended nanometers from the surface, as in an AFM or STM, for example, where the image is obtained by scanning with a fine tip over a surface. The distance from the objective lens to the surface (called the *working distance*) is typically comparable to that of a conventional optical microscope. It varies with the system optical design, but working distances from hundreds of micrometres to several millimeters are typical.

In CLSM a specimen is illuminated by a point laser source, and each volume element is associated with a discrete scattering or fluorescence intensity. Here, the size of the scanning volume is determined by the spot size (close to diffraction limit) of the optical system because the image of the scanning laser is not an infinitely small point but a three-dimensional diffraction pattern. The size of this diffraction pattern and the focal volume it defines is controlled by the numerical aperture of the system's objective lens and the wavelength of the laser used. This can be seen as the classical resolution limit of conventional optical microscopes using wide-field illumination. However, with confocal microscopy it is even possible to improve on the resolution limit of wide-field illumination techniques because the confocal aperture can be closed down to eliminate higher orders of the diffraction pattern. For example, if the pinhole diameter is set to 1 Airy unit then only the first order of the diffraction pattern makes it through the aperture to the detector while the higher orders are blocked, thus improving resolution at the cost of a slight decrease in brightness. In fluorescence observations, the resolution limit of confocal microscopy is often limited by the signal-to-noise ratio caused by the small number of photons typically available in fluorescence microscopy. One can compensate for this effect by using more sensitive photodetectors or by increasing the intensity of the illuminating laser point source. Increasing the intensity of illumination laser risks excessive bleaching or other damage to the specimen of interest, especially for experiments in which comparison of fluorescence brightness is required. When imaging tissues that are differentially refractive, such as the spongy mesophyll of plant leaves or other air-space containing tissues, spherical aberrations that impair confocal image quality are often pronounced. Such aberrations however, can be significantly reduced by mounting samples in optically transparent, non-toxic perfluorocarbons such as perfluorodecalin, which readily infiltrates tissues and has a refractive index almost identical to that of water. When imaging in a reflection geometry, it is also possible to detect the interference of the reflected and scattered light of an object like an intracellular organelle. The interferometric nature of the signal allows to reduce the pinhole diameter down to 0.2 Airy units and therefore enables an ideal resolution enhancement of √2 without sacrificing the signal-to-noise ratio as in confocal fluorescence microscopy.

## Uses

CLSM is widely used in various biological science disciplines, from cell biology and genetics to microbiology and developmental biology. It is also used in quantum optics and nano-crystal imaging and spectroscopy.

### Biology and medicine

Clinically, CLSM is used in the evaluation of various eye diseases, and is particularly useful for imaging, qualitative analysis, and quantification of endothelial cells of the cornea. It is used for localizing and identifying the presence of filamentary fungal elements in the corneal stroma in cases of keratomycosis, enabling rapid diagnosis and thereby early institution of definitive therapy. Research into CLSM techniques for endoscopic procedures (endomicroscopy) is also showing promise. In the pharmaceutical industry, it was recommended to follow the manufacturing process of thin film pharmaceutical forms, to control the quality and uniformity of the drug distribution. Confocal microscopy is also used to study biofilms — complex porous structures that are the preferred habitat of microorganisms. Some of temporal and spatial function of biofilms can be understood only by studying their structure on micro- and meso-scales. The study of microscale is needed to detect the activity and organization of single microorganisms.

### Optics and crystallography

CLSM is used as the data retrieval mechanism in some 3D optical data storage systems and has helped determine the age of the Magdalen papyrus.

### Audio preservation

The IRENE system makes use of confocal microscopy for optical scanning and recovery of damaged historical audio. Wax phonograph cylinders inherently degrade due to contact with the stylus when replayed as intended; microscopy is non-contact, and often gives better sound than stylus playback.

### Material's surface characterization

Laser scanning confocal microscopes are used in the characterization of the surface of microstructured materials, such as Silicon wafers used in solar cell production. During the first processing steps, wafers are wet-chemically etched with acid or alkaline compounds, rendering a texture to their surface. Laser confocal microscopy is then used to observe the state of the resulting surface at the micrometer lever. Laser confocal microscopy can also be used to analyze the thickness and height of metallization fingers printed on top of solar cells.

## Variants and enhancements

### Improving axial resolution

The point spread function of the pinhole is an ellipsoid, several times as long as it is wide. This limits the axial resolution of the microscope. One technique of overcoming this is 4Pi microscopy where incident and or emitted light are allowed to interfere from both above and below the sample to reduce the volume of the ellipsoid. An alternative technique is **confocal theta microscopy**. In this technique the cone of illuminating light and detected light are at an angle to each other (best results when they are perpendicular). The intersection of the two point spread functions gives a much smaller effective sample volume. From this evolved the single plane illumination microscope. Additionally deconvolution may be employed using an experimentally derived point spread function to remove the out of focus light, improving contrast in both the axial and lateral planes.

### Super resolution

There are confocal variants that achieve resolution below the diffraction limit such as stimulated emission depletion microscopy (STED). Besides this technique a broad variety of other (not confocal based) super-resolution techniques are available like PALM, (d)STORM, SIM, and so on. They all have their own advantages such as ease of use, resolution, and the need for special equipment, buffers, or fluorophores.

### Low-temperature operability

To image samples at low temperatures, two main approaches have been used, both based on the laser scanning confocal microscopy architecture. One approach is to use a continuous flow cryostat: only the sample is at low temperature and it is optically addressed through a transparent window. Another possible approach is to have part of the optics (especially the microscope objective) in a cryogenic storage dewar. This second approach, although more cumbersome, guarantees better mechanical stability and avoids the losses due to the window.

### Molecular interaction

To study molecular interactions using the CLSM Förster resonance energy transfer (FRET) can be used to confirm that two proteins are within a certain distance to one another.

## Images

- (β-tubulin in Tetrahymena (a ciliated protozoan).) β-tubulin in *Tetrahymena* (a ciliated protozoan).
- (Partial surface profile of a 1-Euro coin, measured with a Nipkow disk confocal microscope.) Partial surface profile of a 1-Euro coin, measured with a Nipkow disk confocal microscope.
- (Reflection data for 1-Euro coin.) Reflection data for 1-Euro coin.
- (Colour coded image of actin filaments in a cancer cell.) Colour coded image of actin filaments in a cancer cell.
- (Green signal from anti-tubulin antibody conjugated with Alexa Fluor 488) and nuclei (blue signal from DNA stained with DAPI) in root meristem cells 4-day-old Arabidopsis thaliana (Col-0). Scale bar: 5 um.) Green signal from anti-tubulin antibody conjugated with Alexa Fluor 488) and nuclei (blue signal from DNA stained with DAPI) in root meristem cells 4-day-old Arabidopsis thaliana (Col-0). Scale bar: 5 um.

## History

### The beginnings: 1940–1957

In 1940 Hans Goldmann, ophthalmologist in Bern, Switzerland, developed a slit lamp system to document eye examinations. This system is considered by some later authors as the first confocal optical system.

In 1943 Zyun Koana published a confocal system.

In 1951 Hiroto Naora, a colleague of Koana, described a confocal microscope in the journal Science for spectrophotometry.

The first confocal *scanning* microscope was built by Marvin Minsky in 1955 and a patent was filed in 1957. The scanning of the illumination point in the focal plane was achieved by moving the stage. No scientific publication was submitted and no images made with it were preserved.

### The Tandem-Scanning-Microscope

In the 1960s, the Czechoslovak Mojmír Petráň from the Medical Faculty of the Charles University in Plzeň developed the Tandem-Scanning-Microscope, the first commercialized confocal microscope. It was sold by a small company in Czechoslovakia and in the United States by Tracor-Northern (later Noran) and used a rotating Nipkow disk to generate multiple excitation and emission pinholes.

The Czechoslovak patent was filed 1966 by Petráň and Milan Hadravský, a Czechoslovak coworker. A first scientific publication with data and images generated with this microscope was published in the journal Science in 1967, authored by M. David Egger from Yale University and Petráň. As a footnote to this paper it is mentioned that Petráň designed the microscope and supervised its construction and that he was, in part, a "research associate" at Yale. A second publication from 1968 described the theory and the technical details of the instrument and had Hadravský and Robert Galambos, the head of the group at Yale, as additional authors. In 1970 the US patent was granted. It was filed in 1967.

### 1969: The first confocal laser scanning microscope

In 1969 and 1971, M. David Egger and Paul Davidovits from Yale University, published two papers describing the first confocal *laser* scanning microscope. It was a point scanner, meaning just one illumination spot was generated. It used epi-Illumination-reflection microscopy for the observation of nerve tissue. A 5 mW Helium-Neon-Laser with 633 nm light was reflected by a semi-transparent mirror towards the objective. The objective was a simple lens with a focal length of 8.5 mm. As opposed to all earlier and most later systems, the sample was scanned by movement of this lens (objective scanning), leading to a movement of the focal point. Reflected light came back to the semitransparent mirror, the transmitted part was focused by another lens on the detection pinhole behind which a photomultiplier tube was placed. The signal was visualized by a CRT of an oscilloscope, the cathode ray was moved simultaneously with the objective. A special device allowed to make Polaroid photos, three of which were shown in the 1971 publication.

The authors speculate about fluorescent dyes for *in vivo* investigations. They cite Minsky's patent, thank Steve Baer, at the time a doctoral student at the Albert Einstein School of Medicine in New York City where he developed a confocal line scanning microscope, for suggesting to use a laser with 'Minsky's microscope' and thank Galambos, Hadravsky and Petráň for discussions leading to the development of their microscope. The motivation for their development was that in the Tandem-Scanning-Microscope only a fraction of 10−7 of the illumination light participates in generating the image in the eye piece. Thus, image quality was not sufficient for most biological investigations.

### 1977–1985: Point scanners with lasers and stage scanning

In 1977 Colin J. R. Sheppard and Amarjyoti Choudhury, Oxford, UK, published a theoretical analysis of confocal and laser-scanning microscopes. It is probably the first publication using the term "confocal microscope".

In 1978, the brothers Christoph Cremer and Thomas Cremer published a design for a confocal laser-scanning-microscope using fluorescent excitation with electronic autofocus. They also suggested a laser point illumination by using a "4π-point-hologramme". This CLSM design combined the laser scanning method with the 3D detection of biological objects labeled with fluorescent markers for the first time.

In 1978 and 1980, the Oxford-group around Colin Sheppard and Tony Wilson described a confocal microscope with epi-laser-illumination, stage scanning and photomultiplier tubes as detectors. The stage could move along the optical axis (z-axis), allowing optical serial sections.

In 1979 Fred Brakenhoff and coworkers demonstrated that the theoretical advantages of optical sectioning and resolution improvement are indeed achievable in practice. In 1985 this group became the first to publish convincing images taken on a confocal microscope that were able to answer biological questions. Shortly after many more groups started using confocal microscopy to answer scientific questions that until then had remained a mystery due to technological limitations.

In 1983 I. J. Cox and C. Sheppard from Oxford published the first work whereby a confocal microscope was controlled by a computer. The first commercial laser scanning microscope, the stage-scanner SOM-25 was offered by Oxford Optoelectronics (after several take-overs acquired by BioRad) starting in 1982. It was based on the design of the Oxford group.

### Starting 1985: Laser point scanners with beam scanning

In the mid-1980s, William Bradshaw Amos and John Graham White and colleagues working at the Laboratory of Molecular Biology in Cambridge built the first confocal beam scanning microscope. The stage with the sample was not moving, instead the illumination spot was, allowing faster image acquisition: four images per second with 512 lines each. Hugely magnified intermediate images, due to a 1–2 meter long beam path, allowed the use of a conventional iris diaphragm as a 'pinhole', with diameters ~1 mm. First micrographs were taken with long-term exposure on film before a digital camera was added. A further improvement allowed zooming into the preparation for the first time. Zeiss, Leitz and Cambridge Instruments had no interest in a commercial production. The Medical Research Council (MRC) finally sponsored development of a prototype. The design was acquired by Bio-Rad, amended with computer control and commercialized as 'MRC 500'. The successor MRC 600 was later the basis for the development of the first two-photon-fluorescent microscope developed 1990 at Cornell University.

Developments at the KTH Royal Institute of Technology in Stockholm around the same time led to a commercial CLSM distributed by the Swedish company Sarastro. The venture was acquired in 1990 by Molecular Dynamics, but the CLSM was eventually discontinued. In Germany, Heidelberg Instruments, founded in 1984, developed a CLSM, which was initially meant for industrial applications rather than biology. This instrument was taken over in 1990 by Leica Lasertechnik. Zeiss already had a non-confocal flying-spot laser scanning microscope on the market which was upgraded to a confocal. A report from 1990, mentioned some manufacturers of confocals: Sarastro, Technical Instrument, Meridian Instruments, Bio-Rad, Leica, Tracor-Northern and Zeiss.

In 1989, Fritz Karl Preikschat, with his son Ekhard Preikschat, invented the scanning laser diode microscope for particle-size analysis. and co-founded Lasentec to commercialize it. In 2001, Lasentec was acquired by Mettler Toledo. They are used mostly in the pharmaceutical industry to provide in-situ control of the crystallization process in large purification systems.

### 2010s: Computational methods for removing the output pinhole

In standard confocal instruments, the second or "output" pinhole is utilized to filter out the emitted or scattered light. Traditionally, this pinhole is a passive component that blocks light to filter the illumination optically. However, newer designs have tried to perform this filtering digitally.

Recent approaches have replaced the passive pinhole with a compound detector element. Typically, after digital processing, this approach leads to better resolution and photon budget, as the resolution limit can approach that of an infinitely small pinhole.

Other researchers have attempted to digitally refocus the light from a point excitation source using deep convolutional neural networks.
