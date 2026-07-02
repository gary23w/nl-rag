---
title: "Photodetector"
source: https://en.wikipedia.org/wiki/Photodetector
domain: ccd-sensors
license: CC-BY-SA-4.0
tags: charge-coupled device, photodetector element, photoelectric effect, responsivity metric
fetched: 2026-07-02
---

# Photodetector

**Photodetectors**, also called **photosensors**, are devices that detect light or other forms of electromagnetic radiation and convert it into an electrical signal. They are essential in a wide range of applications, from digital imaging and optical communication to scientific research and industrial automation. Photodetectors can be classified by their mechanism of detection, such as the photoelectric effect, photochemical reactions, or thermal effects, or by performance metrics like spectral response. Common types include photodiodes, phototransistors, and photomultiplier tubes, each suited to specific uses. Solar cells, which convert light into electricity, are also a type of photodetector.

## History

The development of photodetectors began with the discovery of the photoelectric effect by Heinrich Hertz in 1887, later explained by Albert Einstein in 1905. Early photodetectors, such as selenium cells invented in the late 19th century, were used in light meters and telegraph systems. The 1930s saw the invention of photomultiplier tubes, enabling the detection of faint light signals, which revolutionized fields like nuclear physics and astronomy. The mid-20th century brought semiconductor-based photodetectors, such as photodiodes and phototransistors, which transformed industries like telecommunications and computing. Today, advancements continue with high-speed detectors and quantum technologies.

## Classification

Photodetectors can be classified based on their mechanism of operation and device structure. Here are the common classifications:

### Based on mechanism of operation

Photodetectors may be classified by their mechanism for detection:

- Photoconductive effect: These detectors work by changing their electrical conductivity when exposed to light. The incident light generates electron-hole pairs in the material, altering its conductivity. Photoconductive detectors are typically made of semiconductors.

- Photoemission or photoelectric effect: Photons cause electrons to transition from the conduction band of a material to free electrons in a vacuum or gas.
- Thermal: Photons cause electrons to transition to mid-gap states then decay back to lower bands, inducing phonon generation and thus heat.
- Polarization: Photons induce changes in polarization states of suitable materials, which may lead to change in index of refraction or other polarization effects.
- Photochemical: Photons induce a chemical change in a material.
- Weak interaction effects: photons induce secondary effects such as in photon drag detectors or gas pressure changes in Golay cells.

Photodetectors may be used in different configurations. Single sensors may detect overall light levels. A 1-D array of photodetectors, as in a spectrophotometer or a Line scanner, may be used to measure the distribution of light along a line. A 2-D array of photodetectors may be used as an image sensor to form images from the pattern of light before it.

A photodetector or array is typically covered by an illumination window, sometimes having an anti-reflective coating.

### Based on device structure

Based on device structure, photodetectors can be classified into the following categories:

1. **MSM Photodetector:** A metal-semiconductor-metal (MSM) photodetector consists of a semiconductor layer sandwiched between two metal electrodes. The metal electrodes are interdigitated, forming a series of alternating fingers or grids. The semiconductor layer is typically made of materials such as silicon (Si), gallium arsenide (GaAs), indium phosphide (InP) or antimony selenide (Sb2Se3). Various methods are employed together to improve its characteristics, such as manipulating the vertical structure, etching, changing the substrate, and utilizing plasmonics. The best achievable efficiency is shown by Antimony Selenide photodetectors.
2. **Photodiodes:** Photodiodes are the most common type of photodetectors. They are semiconductor devices with a PN junction. Incident light generates electron-hole pairs in the depletion region of the junction, producing a photocurrent. Photodiodes can be further categorized into: a. PIN Photodiodes: These photodiodes have an additional intrinsic (I) region between the P and N regions, which extends the depletion region and improves the device's performance. b. Schottky Photodiodes: In Schottky photodiodes, a metal-semiconductor junction is used instead of a PN junction. They offer high-speed response and are commonly used in high-frequency applications.
3. **Avalanche Photodiodes (APDs):** APDs are specialized photodiodes that incorporate avalanche multiplication. They have a high electric field region near the PN junction, which causes impact ionization and produces additional electron-hole pairs. This internal amplification improves the detection sensitivity. APDs are widely used in applications requiring high sensitivity, such as low-light imaging and long-distance optical communication.
4. **Phototransistors:** Phototransistors are transistors with a light-sensitive base region. Incident light causes a change in the base current, which controls the transistor's collector current. Phototransistors offer amplification and can be used in applications that require both detection and signal amplification.
5. **Charge-Coupled Devices (CCDs):** CCDs are imaging sensors composed of an array of tiny capacitors. Incident light generates charge in the capacitors, which is sequentially read and processed to form an image. CCDs are commonly used in digital cameras and scientific imaging applications.
6. **CMOS Image Sensors (CIS):** CMOS image sensors are based on complementary metal-oxide-semiconductor (CMOS) technology. They integrate photodetectors and signal processing circuitry on a single chip. CMOS image sensors have gained popularity due to their low power consumption, high integration, and compatibility with standard CMOS fabrication processes.
7. **Photomultiplier Tubes (PMTs):** PMTs are vacuum tube-based photodetectors. They consist of a photocathode that emits electrons when illuminated, followed by a series of dynodes that multiply the electron current through secondary emission. PMTs offer high sensitivity and are used in applications that require low-light detection, such as particle physics experiments and scintillation detectors.

These are some of the common photodetectors based on device structure. Each type has its own characteristics, advantages, and applications in various fields, including imaging, communication, sensing, and scientific research.

## Properties

There are a number of performance metrics, also called figures of merit, by which photodetectors are characterized and compared

- Quantum efficiency: The number of carriers (electrons or holes) generated per photon.
- Responsivity: The output current divided by total light power falling upon the photodetector.
- Noise-equivalent power: The amount of light power needed to generate a signal comparable in size to the noise of the device.
- Detectivity: The square root of the detector area divided by the noise equivalent power.
- Gain: The output current of a photodetector divided by the current directly produced by the photons incident on the detectors, i.e., the built-in current gain.
- Dark current: The current flowing through a photodetector even in the absence of light.
- Response time: The time needed for a photodetector to go from 10% to 90% of final output.
- Noise spectrum: The intrinsic noise voltage or current as a function of frequency. This can be represented in the form of a noise spectral density.
- Nonlinearity: The RF-output is limited by the nonlinearity of the photodetector
- Spectral response: The response of a photodetector as a function of photon frequency.

## Subtypes

Grouped by mechanism, photodetectors include the following devices:

### Photoemission or photoelectric

- Gaseous ionization detectors are used in experimental particle physics to detect photons and particles with sufficient energy to ionize gas atoms or molecules. Electrons and ions generated by ionization cause a current flow which can be measured.
- Photomultiplier tubes containing a photocathode which emits electrons when illuminated, the electrons are then amplified by a chain of dynodes.
- Phototubes containing a photocathode which emits electrons when illuminated, such that the tube conducts a current proportional to the light intensity.
- Microchannel plate detectors use a porous glass substrate as a mechanism for multiplying electrons. They can be used in combination with a photocathode like the photomultiplier described above, with the porous glass substrate acting as a dynode stage

### Semiconductor

- Active-pixel sensors (APSs) are image sensors. Usually made in a complementary metal–oxide–semiconductor (CMOS) process, and also known as CMOS image sensors, APSs are commonly used in cell phone cameras, web cameras, and some DSLRs.
- Cadmium zinc telluride radiation detectors can operate in direct-conversion (or photoconductive) mode at room temperature, unlike some other materials (particularly germanium) which require liquid nitrogen cooling. Their relative advantages include high sensitivity for x-rays and gamma-rays, due to the high atomic numbers of Cd and Te, and better energy resolution than scintillator detectors.
- Charge-coupled devices (CCD) are image sensors which are used to record images in astronomy, digital photography, and digital cinematography. Before the 1990s, photographic plates were most common in astronomy. The next generation of astronomical instruments, such as the Astro-E2, include cryogenic detectors.
- HgCdTe infrared detectors. Detection occurs when an infrared photon of sufficient energy kicks an electron from the valence band to the conduction band. Such an electron is collected by a suitable external readout integrated circuits (ROIC) and transformed into an electric signal.
- LEDs which are reverse-biased to act as photodiodes. See LEDs as photodiode light sensors.
- Photoresistors or *Light Dependent Resistors* (LDR) which change resistance according to light intensity. Normally the resistance of LDRs decreases with increasing intensity of light falling on it.
- Photodiodes which can operate in photovoltaic mode or photoconductive mode. Photodiodes are often combined with low-noise analog electronics to convert the photocurrent into a voltage that can be digitized.
- Phototransistors, which act like amplifying photodiodes.
- Pinned photodiodes, a photodetector structure with low lag, low noise, high quantum efficiency, and low dark current, widely used in most CCD and CMOS image sensors.
- Quantum dot photoconductors or photodiodes, which can handle wavelengths in the visible and infrared spectral regions.
- Semiconductor detectors are employed in gamma and X-ray spectrometry and as particle detectors.
- Silicon drift detectors (SDDs) are X-ray radiation detectors used in x-ray spectrometry (EDS) and electron microscopy (EDX).

### Photovoltaic

- Photovoltaic cells or solar cells which produce a voltage and supply an electric current when sunlight or certain kinds of light shines on them.

### Thermal

- Bolometers measure the power of incident electromagnetic radiation via the heating of a material with a temperature-dependent electrical resistance. A microbolometer is a specific type of bolometer used as a detector in a thermal camera.
- Cryogenic detectors are sufficiently sensitive to measure the energy of single x-ray, visible and infrared photons.
- Pyroelectric detectors detect photons through the heat they generate and the subsequent voltage generated in pyroelectric materials.
- Thermopiles detect electromagnetic radiation through heat, then generating a voltage in thermocouples.
- Golay cells detect photons by the heat they generate in a gas-filled chamber, causing the gas to expand and deform a flexible membrane whose deflection is measured.

### Photochemical

- Photoreceptor cells in the retina detect light through, for instance, a rhodopsin photon-induced chemical cascade.
- Chemical detectors, such as photographic plates, in which a silver halide molecule is split into an atom of metallic silver and a halogen atom. The photographic developer causes adjacent molecules to split similarly.

### Polarization

- The photorefractive effect is used in holographic data storage.
- Polarization-sensitive photodetectors use optically anisotropic materials to detect photons of a desired linear polarization.

### Graphene/silicon photodetectors

A graphene/n-type silicon heterojunction has been demonstrated to exhibit strong rectifying behavior and high photoresponsivity. Graphene is coupled with silicon quantum dots (Si QDs) on top of bulk Si to form a hybrid photodetector. Si QDs cause an increase of the built-in potential of the graphene/Si Schottky junction while reducing the optical reflection of the photodetector. Both the electrical and optical contributions of Si QDs enable a superior performance of the photodetector.

## Applications

Photodetectors are integral to numerous fields:

- **Consumer electronics**: CCD and CMOS sensors in cameras, optical storage devices.
- **Telecommunications**: Fiber optic communication for high-speed data transmission.
- **Scientific research**: Spectroscopy, particle detection, and astronomy.
- **Industrial automation**: Barcode scanners, quality control systems.
- **Medical devices**: Pulse oximeters, endoscopes.
- **Environmental monitoring**: Air and water quality sensors, weather stations.

Emerging applications include autonomous vehicles and quantum computing.

## Advancements and future trends

Recent developments in photodetector technology include:

- **High-speed detectors**: For faster optical communication.
- **Quantum photodetectors**: For quantum computing and cryptography.
- **Novel materials**: Organic and perovskite detectors for flexible electronics.
- **Integration with AI**: For advanced image processing in autonomous systems.

Future research focuses on improving sensitivity, reducing noise, and expanding wavelength detection ranges.
