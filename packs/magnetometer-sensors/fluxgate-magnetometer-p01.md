---
title: "Magnetometer (part 1/2)"
source: https://en.wikipedia.org/wiki/Fluxgate_magnetometer
domain: magnetometer-sensors
license: CC-BY-SA-4.0
tags: magnetometer sensor, hall effect, magnetoresistance, fluxgate magnetometer
fetched: 2026-07-02
part: 1/2
---

# Magnetometer

(Redirected from

Fluxgate magnetometer

)

A **magnetometer** is a device that measures magnetic field (**B**) or magnetic dipole moment. Different types of magnetometers measure the direction, strength, or relative change of the magnetic **B**-field at a particular location. A compass is one such device, one that measures the direction of an ambient magnetic field, in this case, the Earth's magnetic field. Other magnetometers measure the magnetic dipole moment of a magnetic material such as a ferromagnet, for example by recording the effect of this magnetic dipole on the induced current in a coil.

The invention of the magnetometer is usually credited to Carl Friedrich Gauss in 1832. Earlier, more primitive instruments were developed by Christopher Hansteen in 1819, and by William Scoresby by 1823.

Magnetometers are widely used for measuring the Earth's magnetic field, in geophysical surveys, to detect magnetic anomalies of various types, and to determine the dipole moment of magnetic materials. In an aircraft's attitude and heading reference system, they are commonly used as a heading reference. Magnetometers are also used by the military as a triggering mechanism in magnetic mines to detect submarines. Consequently, some countries, such as the United States, Canada and Australia, classify the more sensitive magnetometers as military technology, and control their distribution.

Magnetometers can be used as metal detectors: they can detect only ferromagnetic metals, but can detect such metals at a much greater distance than conventional metal detectors, which rely on conductivity. Magnetometers are capable of detecting large objects, such as cars, at over 10 metres (33 ft), while a conventional metal detector's range is rarely more than 2 metres (7 ft).

In recent years, magnetometers have been miniaturized to the extent that they can be incorporated in integrated circuits at very low cost and are finding increasing use as miniaturized compasses (MEMS magnetic field sensor).


## Introduction

### Magnetic fields

Magnetic fields are vector quantities characterized by both strength and direction. The strength of a magnetic field, **B**, is measured with the unit tesla in the SI units, and in gauss in the cgs system of units. 10,000 gauss are equal to one tesla. Measurements of the Earth's magnetic field are often quoted in the unit nanotesla (nT), also called a gamma. The Earth's magnetic field can vary from 20000 to 80000 nT depending on location, fluctuations in the Earth's magnetic field are on the order of 100 nT, and magnetic field variations due to magnetic anomalies can be in the picotesla (pT) range. *Gaussmeters* and *teslameters* are magnetometers that measure in the unit gauss or tesla, respectively. In some contexts, magnetometer is the term used for an instrument that measures fields of less than 1 millitesla (mT) and gaussmeter is used for those measuring greater than 1 mT.

### Types of magnetometer

There are two basic types of magnetometer measurement. *Vector magnetometers* measure the vector components of a magnetic field. *Total field magnetometers* or *scalar magnetometers* measure the magnitude of the vector magnetic field. Magnetometers used to study the Earth's magnetic field may express the vector components of the field in terms of *declination* (the angle between the horizontal component of the field vector and true, or geographic, north) and the *inclination* (the angle between the field vector and the horizontal surface).

*Absolute magnetometers* measure the absolute magnitude or vector magnetic field, using an internal calibration or known physical constants of the magnetic sensor. *Relative magnetometers* measure magnitude or vector magnetic field relative to a fixed but uncalibrated baseline. Also called *variometers*, relative magnetometers are used to measure variations in magnetic field.

Magnetometers may also be classified by their situation or intended use. *Stationary magnetometers* are installed to a fixed position and measurements are taken while the magnetometer is stationary. *Portable* or *mobile magnetometers* are meant to be used while in motion and may be manually carried or transported in a moving vehicle. *Laboratory magnetometers* are used to measure the magnetic field of materials placed within them and are typically stationary. *Survey magnetometers* are used to measure magnetic fields in geomagnetic surveys; they may be fixed base stations, as in the INTERMAGNET network, or mobile magnetometers used to scan a geographic region. An early adoption (in the 1950s) of airborne magnetometry by Inco prompted the discovery of nickel ore deposits that led to the founding of Thompson, Manitoba.

### Performance and capabilities

The performance and capabilities of magnetometers are described through their technical specifications. Major specifications include

- *Sample rate* is the number of readings given per second. The inverse is the *cycle time* in seconds per reading. Sample rate is important in mobile magnetometers; the sample rate and the vehicle speed determine the distance between measurements.
- *Bandwidth* or *bandpass* characterizes how well a magnetometer tracks rapid changes in magnetic field. For magnetometers with no onboard signal processing, bandwidth is determined by the Nyquist limit set by sample rate. Modern magnetometers may perform smoothing or averaging over sequential samples, achieving a lower noise in exchange for lower bandwidth.
- *Resolution* is the smallest change in a magnetic field that the magnetometer can resolve. This includes quantization error which is caused by recording roundoff and truncation of digital expressions of the data.
- *Absolute error* is the difference between the readings of a magnetometer true magnetic field.
- *Drift* is the change in absolute error over time.
- *Thermal stability* is the dependence of the measurement on temperature. It is given as a temperature coefficient in the unit nT per degree Celsius.
- *Noise* is the random fluctuations generated by the magnetometer sensor or electronics. Noise is given in the unit nT/√Hz, where frequency component refers to the bandwidth.
- *Sensitivity* is the larger of the noise or the resolution.
- *Heading error* is the change in the measurement due to a change in orientation of the instrument in a constant magnetic field.
- The *dead zone* is the angular region of magnetometer orientation in which the instrument produces poor or no measurements. All optically pumped, proton-free precession, and Overhauser magnetometers experience some dead zone effects.
- *Gradient tolerance* is the ability of a magnetometer to obtain a reliable measurement in the presence of a magnetic field gradient. In surveys of unexploded ordnance or landfills, gradients can be large.

### Early magnetometers

The compass, consisting of a magnetized needle whose orientation changes in response to the ambient magnetic field, is a simple type of magnetometer, one that measures the direction of the field. The oscillation frequency of a magnetized needle is proportional to the square-root of the strength of the ambient magnetic field; so, for example, the oscillation frequency of the needle of a horizontally situated compass is proportional to the square-root of the horizontal intensity of the ambient field.

In 1823 William Scoresby (1789-1857), an English explorer, scientist and clergyman, was deeply involved in magnetic science, particularly in improving ships' compasses. In 1823, he published a paper in the *Transactions of the Royal Society of Edinburgh* titled "Description of Magnetimenter, being a new instrument for measuring magnetic attractions and finding the dip of the needle; with an accont of experiments made with it."

In 1833, Carl Friedrich Gauss, head of the Geomagnetic Observatory in Göttingen, published a paper on measurement of the Earth's magnetic field. It described a new instrument that consisted of a permanent bar magnet suspended horizontally from a gold fibre. The difference in the oscillations when the bar was magnetised and when it was demagnetised allowed Gauss to calculate an absolute value for the strength of the Earth's magnetic field.

The gauss, the CGS unit of magnetic flux density was named in his honour, defined as one maxwell per square centimeter, which corresponds to 10−4 tesla (the SI unit).

Francis Ronalds and Charles Brooke independently invented magnetographs in 1846 that continuously recorded the magnet's movements using photography, thus easing the load on observers. They were quickly utilised by Edward Sabine and others in a global magnetic survey and updated machines were in use well into the 20th century.


## Laboratory magnetometers

Laboratory magnetometers measure the magnetization, also known as the magnetic moment of a sample material. Unlike survey magnetometers, laboratory magnetometers require the sample to be placed inside the magnetometer, and often the temperature, magnetic field, and other parameters of the sample can be controlled. A sample's magnetization, is primarily dependent on the ordering of unpaired electrons within its atoms, with smaller contributions from nuclear magnetic moments, Langevin diamagnetism, among others. Ordering of magnetic moments are primarily classified as diamagnetic, paramagnetic, ferromagnetic, or antiferromagnetic (although the zoology of magnetic ordering also includes ferrimagnetic, helimagnetic, toroidal, spin glass, etc.). Measuring the magnetization as a function of temperature and magnetic field can give clues as to the type of magnetic ordering, as well as any phase transitions between different types of magnetic orders that occur at critical temperatures or magnetic fields. This type of magnetometry measurement is very important to understand the magnetic properties of materials in physics, chemistry, geophysics and geology, as well as sometimes biology.

### SQUID (superconducting quantum interference device)

SQUID magnetometers are a type of tool used both as survey and as laboratory magnetometers. It is based on the concept of flux quantization in a superconducting loop. SQUID magnetometry is an extremely sensitive absolute magnetometry technique, reproducibly achieving femtotesla resolutions in optimized laboratory settings. However SQUIDs are noise sensitive, making them impractical as laboratory magnetometers in high DC magnetic fields, and in pulsed magnets. The necessity to keep at least part of the setup (the superconducting elements) to be cooled to cryogenic temperatures limits the applications as the sensor can not be brought arbitrarily close to the field source. Commercial SQUID magnetometers are available for sample temperatures between 300 mK and 400 K, and magnetic fields up to 7 T.

### Inductive pickup coils

Inductive pickup coils (also referred as inductive sensor) measure the magnetic dipole moment of a material by detecting the current induced in a coil due to the changing magnetic moment of the sample. The sample's magnetization can be changed by applying a small ac magnetic field (or a rapidly changing dc field), as occurs in capacitor-driven pulsed magnets. These measurements require differentiating between the magnetic field produced by the sample and that from the external applied field. Often a special arrangement of cancellation coils is used. For example, half of the pickup coil is wound in one direction, and the other half in the other direction, and the sample is placed in only one half. The external uniform magnetic field is detected by both halves of the coil, and since they are counter-wound, the external magnetic field produces no net signal.

### VSM (vibrating-sample magnetometer)

Vibrating-sample magnetometers (VSMs) detect the dipole moment of a sample by mechanically vibrating the sample inside of an inductive pickup coil or inside of a SQUID coil. Induced current or changing flux in the coil is measured. The vibration is typically created by a motor or a piezoelectric actuator. Typically the VSM technique is about an order of magnitude less sensitive than SQUID magnetometry. VSMs can be combined with SQUIDs to create a system that is more sensitive than either one alone. Heat due to the sample vibration can limit the base temperature of a VSM, typically to 2 K. VSM is also impractical for measuring a fragile sample that is sensitive to rapid acceleration.

### Pulsed-field magnetometry

Pulsed-field magnetometry is another method making use of pickup coils to measure magnetization. Unlike VSMs where the sample is physically vibrated, in pulsed-field magnetometry, the sample is secured and the external magnetic field is changed rapidly, for example in a capacitor-driven magnet. One of multiple techniques must then be used to cancel out the external field from the field produced by the sample. These include counterwound coils that cancel the external uniform field and background measurements with the sample removed from the coil.

### Torque magnetometry

Magnetic torque magnetometry can be even more sensitive than SQUID magnetometry. However, magnetic torque magnetometry doesn't measure magnetism directly as all the previously mentioned methods do. Magnetic torque magnetometry instead measures the torque τ acting on a sample's magnetic moment *μ* as a result of a uniform magnetic field *B*, *τ* = *μ* × *B*. A torque is thus a measure of the sample's magnetic or shape anisotropy. In some cases the sample's magnetization can be extracted from the measured torque. In other cases, the magnetic torque measurement is used to detect magnetic phase transitions or quantum oscillations. The most common way to measure magnetic torque is to mount the sample on a cantilever and measure the displacement via capacitance measurement between the cantilever and nearby fixed object, or by measuring the piezoelectricity of the cantilever, or by optical interferometry off the surface of the cantilever.

### Faraday force magnetometry

Faraday force magnetometry uses the fact that a spatial magnetic field gradient produces force that acts on a magnetized object, *F* = (*M*⋅∇)*B*. In Faraday force magnetometry the force on the sample can be measured by a scale (hanging the sample from a sensitive balance), or by detecting the displacement against a spring. Commonly a capacitive load cell or cantilever is used because of its sensitivity, size, and lack of mechanical parts. Faraday force magnetometry is approximately one order of magnitude less sensitive than a SQUID. The biggest drawback to Faraday force magnetometry is that it requires some means of not only producing a magnetic field, but also producing a magnetic field gradient. While this can be accomplished by using a set of special pole faces, a much better result can be achieved by using set of gradient coils. A major advantage to Faraday force magnetometry is that it is small and reasonably tolerant to noise, and thus can be implemented in a wide range of environments, including a dilution refrigerator. Faraday force magnetometry can also be complicated by the presence of torque (see previous technique). This can be circumvented by varying the gradient field independently of the applied DC field so the torque and the Faraday force contribution can be separated, and/or by designing a Faraday force magnetometer that prevents the sample from being rotated.

### Optical magnetometry

Optical magnetometry makes use of various optical techniques to measure magnetization. One such technique, Kerr magnetometry makes use of the magneto-optic Kerr effect, or MOKE. In this technique, incident light is directed at the sample's surface. Light interacts with a magnetized surface nonlinearly so the reflected light has an elliptical polarization, which is then measured by a detector. Another method of optical magnetometry is Faraday rotation magnetometry. Faraday rotation magnetometry utilizes nonlinear magneto-optical rotation to measure a sample's magnetization. In this method a Faraday modulating thin film is applied to the sample to be measured and a series of images are taken with a camera that senses the polarization of the reflected light. To reduce noise, multiple pictures are then averaged together. One advantage to this method is that it allows mapping of the magnetic characteristics over the surface of a sample. This can be especially useful when studying such things as the Meissner effect on superconductors. Microfabricated optically pumped magnetometers (μOPMs) can be used to detect the origin of brain seizures more precisely and generate less heat than currently available SQUIDs. The device works by using polarized light to control the spin of rubidium atoms which can be used to measure and monitor the magnetic field.

### A.C. susceptometry

Susceptometry, while not technicallly magnetometry, is a closely related technique to those above. It measures the magnetic suscpetibility *χ* *= dM/dH* instead of the magnetization *M*. This is particularly relevant when (instead of a static) a dynamic magnetic field *H*(*t*) is applied to the sample in order to investigate its *dynamic* magnetic properties. In the mathematically simplest case, a sinusoidal excitation field *h*(*t*) = *h0*sin(2*πt*) is overlaid onto a constant (possibly zero) magnetic field *H*: *H*(*t*) = *H0* + *h*(*t*). The resulting time-dependent magnetization *M*(*t*) can be decomposed into a series of harmonics. The constant term and first harmonics (omitting higher harmonics) of *M*(*t*) read as *M*(*t*) = *M0* + *h* (*χ'1* sin(*2πt*)+*χ''1* cos(*2πt*)). *χ'1* and *χ''1* are commonly referred to as *the* a.c. magnetic suscpetibilities, where *χ'1* is the reactive/in-phase component and *χ''1* is the absorptive/out-of-phase component.

This technique can for example be used to gain an insight on the magnetic phase transitions or the freezing behavior of spin glasses. At a close to an ordering point, the spin dynamics will exhibit a critical slowing down, which means the absorptive component *χ''1* peaks (see the Debye relaxor model in dielectrics).

A.C. susceptometry may also be used as a more convenient probe to determine the static magnetic susceptibility. For this, the frequency *f* is chosen to be smaller than the spin dynamics. Since the excitation amplitude *h* can be chosen to be significantly smaller than the typical step size in any field sweep (*M*(*H*) measurement), the susceptibility as a derivative *χ* *= dM/dH* is approximated much more accurately with a small field difference *h~*100 Oe (see difference quotient) instead of typical values for DC magnetometry of *ΔH~102* Oe.

### Alternating Gradient Magnetometry

A dipole in a gradient magnetic field experiences a net force. The strength of the force can be measured and is proportional to the magnetic moment of the dipole. By alternating the gradient of the field and using a lock-in amplifier, a low noise floor can be achieved.

Survey magnetometers can be divided into two basic types:

- *Scalar magnetometers* measure the total strength of the magnetic field to which they are subjected, but not its direction
- *Vector magnetometers* have the capability to measure the component of the magnetic field in a particular direction, relative to the spatial orientation of the device.

A vector is a mathematical entity with both magnitude and direction. The Earth's magnetic field at a given point is a vector. A magnetic compass is designed to give a horizontal bearing direction, whereas a *vector magnetometer* measures both the magnitude and direction of the total magnetic field. Three orthogonal sensors are required to measure the components of the magnetic field in all three dimensions.

They are also rated as "absolute" if the strength of the field can be calibrated from their own known internal constants or "relative" if they need to be calibrated by reference to a known field.

A *magnetograph* is a magnetometer that continuously records data over time. This data is typically represented in magnetograms.

Magnetometers can also be classified as "AC" if they measure fields that vary relatively rapidly in time (> 100 Hz), and "DC" if they measure fields that vary only slowly (quasi-static) or are static. AC magnetometers find use in electromagnetic systems (such as magnetotellurics), and DC magnetometers are used for detecting mineralisation and corresponding geological structures.

### Scalar magnetometers

#### Proton precession magnetometer

*Proton precession magnetometer*s, also known as *proton magnetometers*, PPMs or simply mags, measure the resonance frequency of protons (hydrogen nuclei) in the magnetic field to be measured, due to nuclear magnetic resonance (NMR). Because the precession frequency depends only on atomic constants and the strength of the ambient magnetic field, the accuracy of this type of magnetometer can reach 1 ppm.

A direct current flowing in a solenoid creates a strong magnetic field around a hydrogen-rich fluid (kerosene and decane are popular, and even water can be used), causing some of the protons to align themselves with that field. The current is then interrupted, and as protons realign themselves with the ambient magnetic field, they precess at a frequency that is directly proportional to the magnetic field. This produces a weak rotating magnetic field that is picked up by a (sometimes separate) inductor, amplified electronically, and fed to a digital frequency counter whose output is typically scaled and displayed directly as field strength or output as digital data.

For hand/backpack carried units, PPM sample rates are typically limited to less than one sample per second. Measurements are typically taken with the sensor held at fixed locations at approximately 10 metre increments.

Portable instruments are also limited by sensor volume (weight) and power consumption. PPMs work in field gradients up to 3,000 nT/m, which is adequate for most mineral exploration work. For higher gradient tolerance, such as mapping banded iron formations and detecting large ferrous objects, Overhauser magnetometers can handle 10000 nT/m, and caesium magnetometers can handle 30000 nT/m.

They are relatively inexpensive (< US$8,000) and were once widely used in mineral exploration. Three manufacturers dominate the market: GEM Systems, Geometrics and Scintrex. Popular models include G-856/857, Smartmag, GSM-18, and GSM-19T.

For mineral exploration, they have been superseded by Overhauser, caesium, and potassium instruments, all of which are fast-cycling, and do not require the operator to pause between readings.

#### Overhauser effect magnetometer

The *Overhauser effect magnetometer* or *Overhauser magnetometer* uses the same fundamental effect as the *proton precession magnetometer* to take measurements. By adding free radicals to the measurement fluid, the nuclear Overhauser effect can be exploited to significantly improve upon the proton precession magnetometer. Rather than aligning the protons using a solenoid, a low power radio-frequency field is used to align (polarise) the electron spin of the free radicals, which then couples to the protons via the Overhauser effect. This has two main advantages: driving the RF field takes a fraction of the energy (allowing lighter-weight batteries for portable units), and faster sampling as the electron-proton coupling can happen even as measurements are being taken. An Overhauser magnetometer produces readings with a 0.01 nT to 0.02 nT standard deviation while sampling once per second.

#### Caesium vapour magnetometer

The *optically pumped caesium vapour magnetometer* is a highly sensitive (300 fT/Hz0.5) and accurate device used in a wide range of applications. It is one of a number of alkali vapours (including rubidium and potassium) that are used in this way.

The device broadly consists of a photon emitter, such as a laser, an absorption chamber containing caesium vapour mixed with a "buffer gas" through which the emitted photons pass, and a photon detector, arranged in that order. The buffer gas is usually helium or nitrogen and they are used to reduce collisions between the caesium vapour atoms.

The basic principle that allows the device to operate is the fact that a caesium atom can exist in any of nine energy levels, which can be informally thought of as the placement of electron atomic orbitals around the atomic nucleus. When a caesium atom within the chamber encounters a photon from the laser, it is excited to a higher energy state, emits a photon and falls to an indeterminate lower energy state. The caesium atom is "sensitive" to the photons from the laser in three of its nine energy states, and therefore, assuming a closed system, all the atoms eventually fall into a state in which all the photons from the laser pass through unhindered and are measured by the photon detector. The caesium vapour has become transparent. This process happens continuously to maintain as many of the electrons as possible in that state.

At this point, the sample (or population) is said to have been optically pumped and ready for measurement to take place. When an external field is applied it disrupts this state and causes atoms to move to different states which makes the vapour less transparent. The photo detector can measure this change and therefore measure the magnitude of the magnetic field.

In the most common type of caesium magnetometer, a very small AC magnetic field is applied to the cell. Since the difference in the energy levels of the electrons is determined by the external magnetic field, there is a frequency at which this small AC field makes the electrons change states. In this new state, the electrons once again can absorb a photon of light. This causes a signal on a photo detector that measures the light passing through the cell. The associated electronics use this fact to create a signal exactly at the frequency that corresponds to the external field.

Another type of caesium magnetometer modulates the light applied to the cell. This is referred to as a Bell-Bloom magnetometer, after the two scientists who first investigated the effect. If the light is turned on and off at the frequency corresponding to the Earth's field, there is a change in the signal seen at the photo detector. Again, the associated electronics use this to create a signal exactly at the frequency that corresponds to the external field. Both methods lead to high performance magnetometers.

#### Potassium vapour magnetometer

Potassium is the only optically pumped magnetometer that operates on a single, narrow electron spin resonance (ESR) line in contrast to other alkali vapour magnetometers that use irregular, composite and wide spectral lines and helium with the inherently wide spectral line.

#### Metastable helium-4 scalar magnetometer

Magnetometers based on helium-4 excited to its metastable triplet state thanks to a plasma discharge have been developed in the 1960s and 1970s by Texas Instruments, then by its spinoff Polatomic, and from late 1980s by CEA-Leti. The latter pioneered a configuration which cancels the dead-zones, which are a recurrent problem of atomic magnetometers. This configuration was demonstrated to show an accuracy of 50 pT in orbit operation. The ESA chose this technology for the Swarm mission, which was launched in 2013. An experimental vector mode, which could compete with fluxgate magnetometers was tested in this mission with overall success.

#### Applications

The caesium and potassium magnetometers are typically used where a higher performance magnetometer than the proton magnetometer is needed. In archaeology and geophysics, where the sensor sweeps through an area and many accurate magnetic field measurements are often needed, caesium and potassium magnetometers have advantages over the proton magnetometer.

The caesium and potassium magnetometer's faster measurement rate allows the sensor to be moved through the area more quickly for a given number of data points. Caesium and potassium magnetometers are insensitive to rotation of the sensor while the measurement is being made.

The lower noise of caesium and potassium magnetometers allow those measurements to more accurately show the variations in the field with position.

### Vector magnetometers

Vector magnetometers measure one or more components of the magnetic field electronically. Using three orthogonal magnetometers, both azimuth and dip (inclination) can be measured. By taking the square root of the sum of the squares of the components the total magnetic field strength (also called total magnetic intensity, TMI) can be calculated by the Pythagorean theorem.

Vector magnetometers are subject to temperature drift and the dimensional instability of the ferrite cores. They also require leveling to obtain component information, unlike total field (scalar) instruments. For these reasons they are no longer used for mineral exploration.

#### Rotating coil magnetometer

The magnetic field induces a sine wave in a rotating coil. The amplitude of the signal is proportional to the strength of the field, provided it is uniform, and to the sine of the angle between the rotation axis of the coil and the field lines. This type of magnetometer is obsolete.

#### Hall effect magnetometer

The most common magnetic sensing devices are solid-state Hall effect sensors. These sensors produce a voltage proportional to the applied magnetic field and also sense polarity. They are used in applications where the magnetic field strength is relatively large, such as in anti-lock braking systems in cars, which sense wheel rotation speed via slots in the wheel disks.

#### Magnetoresistive devices

These are made of thin strips of Permalloy, a high magnetic permeability, nickel-iron alloy, whose electrical resistance varies with a change in magnetic field. They have a well-defined axis of sensitivity, can be produced in 3-D versions and can be mass-produced as an integrated circuit. They have a response time of less than 1 microsecond and can be sampled in moving vehicles up to 1000 times/second. They can be used in compasses that read within 1°, for which the underlying sensor must reliably resolve 0.1°.

#### Fluxgate magnetometer

A fluxgate magnetometer consists of a small magnetically susceptible core wrapped by two coils of wire. An alternating electric current is passed through one coil, driving the core through an alternating cycle of magnetic saturation; i.e., magnetised, unmagnetised, inversely magnetised, unmagnetised, magnetised, and so forth. This constantly changing field induces a voltage in the second coil which is measured by a detector. In a magnetically neutral background, the input and output signals match. However, when the core is exposed to a background field, it is more easily saturated in alignment with that field and less easily saturated in opposition to it. Hence the alternating magnetic field and the induced output voltage, are out of step with the input current. The extent to which this is the case depends on the strength of the background magnetic field. Often, the signal in the output coil is integrated, yielding an output analog voltage proportional to the magnetic field.

The fluxgate magnetometer was invented by H. Aschenbrenner and G. Goubau in 1936. A team at Gulf Research Laboratories led by Victor Vacquier developed airborne fluxgate magnetometers to detect submarines during World War II and after the war confirmed the theory of plate tectonics by using them to measure shifts in the magnetic patterns on the sea floor.

A wide variety of sensors are currently available and used to measure magnetic fields. Fluxgate compasses and gradiometers measure the direction and magnitude of magnetic fields. Fluxgates are affordable, rugged and compact with miniaturization recently advancing to the point of complete sensor solutions in the form of IC chips, including examples from both academia and industry. This, plus their typically low power consumption makes them ideal for a variety of sensing applications. Gradiometers are commonly used for archaeological prospecting, and unexploded ordnance (UXO) detection such as the German military's popular *Foerster*. Utility location specialists also use gradiometers for locating underground utilities such as pipeline valves, septic tanks, and manhole covers.

The typical fluxgate magnetometer consists of a "sense" (secondary) coil surrounding an inner "drive" (primary) coil that is closely wound around a highly permeable core material, such as mu-metal or permalloy. An alternating current is applied to the drive winding, which drives the core in a continuous repeating cycle of saturation and unsaturation. To an external field, the core is alternately weakly permeable and highly permeable. The core is often a toroidally wrapped ring or a pair of linear elements whose drive windings are each wound in opposing directions. Such closed flux paths minimise coupling between the drive and sense windings. In the presence of an external magnetic field, with the core in a highly permeable state, such a field is locally attracted or gated (hence the name fluxgate) through the sense winding. When the core is weakly permeable, the external field is less attracted. This continuous gating of the external field in and out of the sense winding induces a signal in the sense winding, whose principal frequency is twice that of the drive frequency, and whose strength and phase orientation vary directly with the external-field magnitude and polarity.

There are additional factors that affect the size of the resultant signal. These factors include the number of turns in the sense winding, magnetic permeability of the core, sensor geometry, and the gated flux rate of change with respect to time.

Phase synchronous detection is used to extract these harmonic signals from the sense winding and convert them into a DC voltage proportional to the external magnetic field. Active current feedback may also be employed, such that the sense winding is driven to counteract the external field. In such cases, the feedback current varies linearly with the external magnetic field and is used as the basis for measurement. This helps to counter inherent non-linearity between the applied external field strength and the flux gated through the sense winding.

#### SQUID magnetometer

SQUIDs, or superconducting quantum interference devices, measure extremely small changes in magnetic fields. They are very sensitive vector magnetometers, with noise levels as low as 3 fT⋅Hz−1/2 in commercial instruments and 0.4 fT⋅Hz−1/2 in experimental devices. Many liquid-helium-cooled commercial SQUIDs achieve a flat noise spectrum from near DC (less than 1 Hz) to tens of kilohertz, making such devices ideal for time-domain biomagnetic signal measurements. SERF atomic magnetometers demonstrated in laboratories so far reach competitive noise floor but in relatively small frequency ranges.

SQUID magnetometers require cooling with liquid helium (4.2 K) or liquid nitrogen (77 K) to operate, hence the packaging requirements to use them are rather stringent both from a thermal-mechanical as well as magnetic standpoint. SQUID magnetometers are most commonly used to measure the magnetic fields produced by laboratory samples, also for brain or heart activity (magnetoencephalography and magnetocardiography, respectively). Geophysical surveys use SQUIDs from time to time, but the logistics of cooling the SQUID are much more complicated than other magnetometers that operate at room temperature.

#### Zero-field optically-pumped magnetometers

Magnetometers based on atomic gasses can perform vector measurements of the magnetic field in the low field regime, where the decay of the atomic coherence becomes faster than the Larmor frequency. The physics of such magnetometers is based on the Hanle effect. Such zero-field optically pumped magnetometers have been tested in various configurations and with different atomic species, notably alkali (potassium, rubidium and cesium), helium and mercury. For the case of alkali, the coherence times were greatly limited due to spin-exchange relaxation. A major breakthrough happened at the beginning of the 2000 decade, Romalis group in Princeton demonstrated that in such a low field regime, alkali coherence times can be greatly enhanced if a high enough density can be reached by high temperature heating, this is the so-called SERF effect.

The main interest of optically-pumped magnetometers is to replace SQUID magnetometers in applications where cryogenic cooling is a drawback. This is notably the case of medical imaging where such cooling imposes a thick thermal insulation, strongly affecting the amplitude of the recorded biomagnetic signals. Several startup companies are currently developing optically pumped magnetometers for biomedical applications: those of TwinLeaf, quSpin and FieldLine being based on alkali vapors, and those of Mag4Health on metastable helium-4.

##### Spin-exchange relaxation-free (SERF) atomic magnetometers

At sufficiently high atomic density, extremely high sensitivity can be achieved. Spin-exchange-relaxation-free (SERF) atomic magnetometers containing potassium, caesium, or rubidium vapor operate similarly to the caesium magnetometers described above, yet can reach sensitivities lower than 1 fT⋅Hz−1⁄2. The SERF magnetometers only operate in small magnetic fields. The Earth's field is about 50 μT; SERF magnetometers operate in fields less than 0.5 μT.

Large volume detectors have achieved a sensitivity of 200 aT⋅Hz−1⁄2. This technology has greater sensitivity per unit volume than SQUID detectors. The technology can also produce very small magnetometers that may in the future replace coils for detecting radio-frequency magnetic fields. This technology may produce a magnetic sensor that has all of its input and output signals in the form of light on fiber-optic cables. This lets the magnetic measurement be made near high electrical voltages.


## Calibration of magnetometers

The calibration of magnetometers is usually performed by means of coils which are supplied by an electrical current to create a magnetic field. It allows to characterize the sensitivity of the magnetometer (in terms of V/T). In many applications the homogeneity of the calibration coil is an important feature. For this reason, coils like Helmholtz coils are commonly used either in a single axis or a three axis configuration. For demanding applications a high homogeneity magnetic field is mandatory, in such cases magnetic field calibration can be performed using a Maxwell coil, cosine coils, or calibration in the highly homogenous Earth's magnetic field.
