---
title: "Lidar (part 1/2)"
source: https://en.wikipedia.org/wiki/Lidar
domain: lidar-sensors-deep
license: CC-BY-SA-4.0
tags: lidar scanning, optical time-domain reflectometer, point cloud, beam steering
fetched: 2026-07-02
part: 1/2
---

# Lidar

**Lidar** (/ˈlaɪdɑːr/, an acronym of *light detection and ranging* or *laser imaging, detection, and ranging*, often stylized **LiDAR**) is a method for determining ranges by targeting an object or a surface with a laser and measuring the time for the reflected light to return to the receiver. Lidar may operate in a fixed direction (e.g., vertical) or it may scan directions, in a special combination of 3D scanning and laser scanning.

An airplane collecting treetop data over a Brazilian rainforest

In this view, the viewer flies down to the rainforest canopy and flies through the virtual leaves.

This visualisation shows an airplane collecting a 50 km swathe of lidar data over the Brazilian rainforest. For ground-level features, colours range from deep brown to tan. Vegetation heights are depicted in shades of green, where dark greens are closest to the ground and light greens are the highest.

Lidar has terrestrial, airborne, and mobile uses. It is commonly used to make high-resolution maps, with applications in surveying, geodesy, geomatics, archaeology, geography, geology, geomorphology, seismology, forestry, atmospheric physics, laser guidance, airborne laser swathe mapping (ALSM), and laser altimetry. It is used to make digital 3-D representations of areas on the Earth's surface and ocean bottom of the intertidal and near coastal zone by varying the wavelength of light. It has also been increasingly used in control and navigation for autonomous cars and for the helicopter *Ingenuity* on its record-setting flights over the terrain of Mars. Lidar has since been used extensively for atmospheric research and meteorology. Lidar instruments fitted to aircraft and satellites carry out surveying and mapping – a recent example being the U.S. Geological Survey Experimental Advanced Airborne Research Lidar. NASA has identified lidar as a key technology for enabling autonomous precision safe landing of future robotic and crewed lunar-landing vehicles.


## History and etymology

The essential concept of lidar was originated by E. H. Synge in 1930, who envisaged the use of powerful searchlights to probe the atmosphere.

Under the direction of Malcolm Stitch, the Hughes Aircraft Company introduced the first lidar-like system in 1961, shortly after the invention of the laser. Intended for satellite tracking, this system combined laser-focused imaging with the ability to calculate distances by measuring the time for a signal to return using appropriate sensors and data acquisition electronics. It was originally called "Colidar" an acronym for "coherent light detecting and ranging", derived from the term "radar", itself an acronym for "radio detection and ranging". All laser rangefinders, laser altimeters and lidar units are derived from the early colidar systems.

The first practical terrestrial application of a colidar system was the "Colidar Mark II", a large rifle-like laser rangefinder produced in 1963, which had a range of 11 km and an accuracy of 4.5 m, to be used for military targeting. The first mention of lidar as a stand-alone word in 1963 suggests that it originated as a portmanteau of "light" and "radar": "Eventually the laser may provide an extremely sensitive detector of particular wavelengths from distant objects. Meanwhile, it is being used to study the Moon by 'lidar' (light radar) ..." The name "photonic radar" is sometimes used to mean visible-spectrum range finding like lidar.

Lidar's first applications were in meteorology, for which the National Center for Atmospheric Research used it to measure clouds and pollution. The general public became aware of the accuracy and usefulness of lidar systems in 1971 during the Apollo 15 mission, when astronauts used a laser altimeter to map the surface of the Moon. Although the English language no longer treats "radar" as an acronym, (i.e., uncapitalized), the word "lidar" was capitalized as "LIDAR" or "LiDAR" in some publications beginning in the 1980s. No consensus exists on capitalization. Various publications refer to lidar as "LIDAR", "LiDAR", "LIDaR", or "Lidar". The USGS uses both "LIDAR" and "lidar", sometimes in the same document; the *New York Times* predominantly uses "lidar" for staff-written articles, although contributing news feeds such as Reuters may use Lidar.


## Theory

Basic time-of-flight principles applied to laser range-finding

Flying over the Brazilian Amazon with a lidar instrument

Animation of a satellite collecting digital elevation map data over the Ganges and Brahmaputra River basin using lidar

Lidar uses ultraviolet, visible, or near infrared light to image objects. It can target a wide range of materials, including non-metallic objects, rocks, rain, chemical compounds, aerosols, clouds and even single molecules. A narrow laser beam can map physical features with very high resolutions; for example, an aircraft can map terrain at 30-centimetre (12 in) resolution or better.

Wavelengths vary to suit the target: from about 10 micrometers (infrared) to approximately 250 nanometers (ultraviolet). Typically, light is reflected via backscattering, as opposed to pure reflection one might find with a mirror. Different types of scattering are used for different lidar applications: most commonly Rayleigh scattering, Mie scattering, Raman scattering, and fluorescence. Suitable combinations of wavelengths can allow remote mapping of atmospheric contents by identifying wavelength-dependent changes in the intensity of the returned signal. The name "photonic radar" is sometimes used to mean visible-spectrum range finding like lidar, although photonic radar more strictly refers to radio-frequency range finding using photonics components.

A lidar determines the distance of an object or a surface with the formula:

$d={\frac {c\cdot t}{2}}$

where *c* is the speed of light, *d* is the distance between the detector and the object or surface being detected, and *t* is the time spent for the laser light to travel to the object or surface being detected, then travel back to the detector.

The two kinds of lidar detection schemes are "incoherent" or direct energy detection (which principally measures amplitude changes of the reflected light) and coherent detection (best for measuring Doppler shifts, or changes in the phase of the reflected light). Coherent systems generally use optical heterodyne detection. This is more sensitive than direct detection and allows them to operate at much lower power, but requires more complex transceivers.

Both types employ pulse models: either *micropulse* or *high energy*. Micropulse systems utilize intermittent bursts of energy. They developed as a result of ever-increasing computer power, combined with advances in laser technology. They use considerably less energy in the laser, typically on the order of one microjoule, and are often "eye-safe", meaning they can be used without safety precautions. High-power systems are common in atmospheric research, where they are widely used for measuring atmospheric parameters: the height, layering and densities of clouds, cloud particle properties (extinction coefficient, backscatter coefficient, depolarization), temperature, pressure, wind, humidity, and trace gas concentration (ozone, methane, nitrous oxide, etc.).


## Components

### Laser

600–1,000 nm lasers are most common for non-scientific applications. The maximum power of the laser is limited, or an automatic shut-off system which turns the laser off at specific altitudes is used in order to make it eye-safe for the people on the ground.

One common alternative, 1,550 nm lasers, are eye-safe at relatively high power levels since this wavelength is strongly absorbed by water and barely reaches the retina, though camera sensors can still get damaged. A trade-off though is that current detector technology is less advanced, so these wavelengths are generally used at longer ranges with lower accuracies. They are also used for military applications because 1,550 nm is not visible in night vision goggles, unlike the shorter 1,000 nm infrared laser.

Airborne topographic mapping lidars generally use 1,064 nm diode-pumped YAG lasers, while bathymetric (underwater depth research) systems generally use 532 nm frequency-doubled diode pumped YAG lasers because 532 nm penetrates water with much less attenuation than 1,064 nm. Laser settings include the laser repetition rate (which controls the data collection speed). Pulse length is generally an attribute of the laser cavity length, the number of passes required through the gain material (YAG, YLF, etc.), and Q-switch (pulsing) speed. Better target resolution is achieved with shorter pulses, provided the lidar receiver detectors and electronics have sufficient bandwidth.

A phased array can illuminate any direction by using a microscopic array of individual antennas. Controlling the timing (phase) of each antenna steers a cohesive signal in a specific direction. Phased arrays have been used in radar since the 1940s. On the order of a million optical antennas are used to see a radiation pattern of a certain size in a certain direction. To achieve this the phase of each individual antenna (emitter) are precisely controlled. It is very difficult, if possible at all, to use the same technique in a lidar. The main problems are that all individual emitters must be coherent (technically coming from the same "master" oscillator or laser source), have dimensions about the wavelength of the emitted light (1 micron range) to act as a point source with their phases being controlled with high accuracy.

Microelectromechanical mirrors (MEMS) are not entirely solid-state. However, their tiny form factor provides many of the same cost benefits. A single laser is directed to a single mirror that can be reoriented to view any part of the target field. The mirror spins at a rapid rate. However, MEMS systems generally operate in a single plane (left to right). To add a second dimension generally requires a second mirror that moves up and down. Alternatively, another laser can hit the same mirror from another angle. MEMS systems can be disrupted by shock/vibration and may require repeated calibration.

### Scanner and optics

Image development speed is affected by the speed at which they are scanned. Options to scan the azimuth and elevation include dual oscillating plane mirrors, a combination with a polygon mirror, and a dual axis scanner. Optic choices affect the angular resolution and range that can be detected. A hole mirror or a beam splitter are options to collect a return signal.

### Photodetector and receiver electronics

Two main photodetector technologies are used in lidar: solid-state photodetectors, such as silicon avalanche photodiodes, or photomultipliers. The sensitivity of the receiver is another parameter that has to be balanced in a lidar design.

### Position and navigation systems

Lidar sensors mounted on mobile platforms such as airplanes or satellites require instrumentation to determine the absolute position and orientation of the sensor. Such devices generally include a Global Positioning System receiver and an inertial measurement unit (IMU).

### Sensor

Lidar uses active sensors that supply their own illumination source. The energy source hits objects and the reflected energy is detected and measured by sensors. Distance to the object is determined by recording the time between transmitted and backscattered pulses and by using the speed of light to calculate the distance traveled. Flash lidar allows for 3-D imaging because of the camera's ability to emit a larger flash and sense the spatial relationships and dimensions of area of interest with the returned energy. This allows for more accurate imaging because the captured frames do not need to be stitched together, and the system is not sensitive to platform motion. This results in less distortion.

3-D imaging can be achieved using both scanning and non-scanning systems. "3-D gated viewing laser radar" is a non-scanning laser ranging system that applies a pulsed laser and a fast gated camera. Research has begun for virtual beam steering using digital light processing (DLP) technology.

Imaging lidar can also be performed using arrays of high speed detectors and modulation sensitive detector arrays typically built on single chips using complementary metal–oxide–semiconductor (CMOS) and hybrid CMOS/charge-coupled device (CCD) fabrication techniques. In these devices each pixel performs some local processing such as demodulation or gating at high speed, downconverting the signals to video rate so that the array can be read like a camera. Using this technique many thousands of pixels / channels may be acquired simultaneously. High resolution 3-D lidar cameras use homodyne detection with an electronic CCD or CMOS shutter.

A coherent imaging lidar uses synthetic array heterodyne detection to enable a staring single element receiver to act as though it were an imaging array.

In 2014, Lincoln Laboratory announced a new imaging chip with more than 16,384 pixels, each able to image a single photon, enabling them to capture a wide area in a single image. An earlier generation of the technology with one fourth as many pixels was dispatched by the U.S. military after the January 2010 Haiti earthquake. A single pass by a business jet at 3,000 m (10,000 ft) over Port-au-Prince was able to capture instantaneous snapshots of 600 m (2,000 ft) squares of the city at a resolution of 30 cm (1 ft), displaying the precise height of rubble strewn in city streets. The new system is ten times better, and could produce much larger maps more quickly. The chip uses indium gallium arsenide (InGaAs), which operates in the infrared spectrum at a relatively long wavelength that allows for higher power and longer ranges. In many applications, such as self-driving cars, the new system will lower costs by not requiring a mechanical component to aim the chip. InGaAs uses less hazardous wavelengths than conventional silicon detectors, which operate at visual wavelengths. New technologies for infrared single-photon counting lidar are advancing rapidly, including arrays and cameras in a variety of semiconductor and superconducting platforms.


## Classification

Lidar can be oriented to nadir, zenith, or laterally. For example, lidar altimeters look down, an atmospheric lidar looks up, and lidar-based collision avoidance systems are side-looking.

Laser projections of lidars can be manipulated using various methods and mechanisms to produce a scanning effect: the standard spindle-type, which spins to give a 360-degree view; solid-state lidar, which has a fixed field of view, but no moving parts, and can use either MEMS or optical phased arrays to steer the beams; and flash lidar, which spreads a flash of light over a large field of view before the signal bounces back to a detector.

Lidar applications can be divided into airborne and terrestrial types. The two types require scanners with varying specifications based on the data's purpose, the size of the area to be captured, the range of measurement desired, the cost of equipment, and more. Spaceborne platforms are also possible, see satellite laser altimetry.

Airborne lidar (also *airborne laser scanning*) is when a laser scanner, while attached to an aircraft during flight, creates a 3-D point cloud model of the landscape. This is currently the most detailed and accurate method of creating digital elevation models, replacing photogrammetry. One major advantage in comparison with photogrammetry is the ability to filter out reflections from vegetation from the point cloud model to create a digital terrain model which represents ground surfaces such as rivers, paths, cultural heritage sites, etc., which are concealed by trees. Within the category of airborne lidar, there is sometimes a distinction made between high-altitude and low-altitude applications, but the main difference is a reduction in both accuracy and point density of data acquired at higher altitudes. Airborne lidar can also be used to create bathymetric models in shallow water.

The main constituents of airborne lidar include digital elevation models (DEM) and digital surface models (DSM). The points and ground points are the vectors of discrete points while DEM and DSM are interpolated raster grids of discrete points. The process also involves capturing of digital aerial photographs. To interpret deep-seated landslides for example, under the cover of vegetation, scarps, tension cracks or tipped trees airborne lidar is used. Airborne lidar digital elevation models can see through the canopy of forest cover, perform detailed measurements of scarps, erosion and tilting of electric poles.

Airborne lidar data is processed using a toolbox called Toolbox for Lidar Data Filtering and Forest Studies (TIFFS) for lidar data filtering and terrain study software. The data is interpolated to digital terrain models using the software. The laser is directed at the region to be mapped and each point's height above the ground is calculated by subtracting the original z-coordinate from the corresponding digital terrain model elevation. Based on this height above the ground the non-vegetation data is obtained which may include objects such as buildings, electric power lines, flying birds, insects, etc. The rest of the points are treated as vegetation and used for modeling and mapping. Within each of these plots, lidar metrics are calculated by calculating statistics such as mean, standard deviation, skewness, percentiles, quadratic mean, etc.

Multiple commercial lidar systems for unmanned aerial vehicles are currently on the market. These platforms can systematically scan large areas, or provide a cheaper alternative to manned aircraft for smaller scanning operations.

The airborne lidar bathymetric technological system involves the measurement of time of flight of a signal from a source to its return to the sensor. The data acquisition technique involves a sea floor mapping component and a ground truth component that includes video transects and sampling. It works using a green spectrum (532 nm) laser beam. Two beams are projected onto a fast rotating mirror, which creates an array of points. One of the beams penetrates the water and also detects the bottom surface of the water under favorable conditions.

Water depth measurable by lidar depends on the clarity of the water and the absorption of the wavelength used. Water is most transparent to green and blue light, so these will penetrate deepest in clean water. Blue-green light of 532 nm produced by frequency doubled solid-state IR laser output is the standard for airborne bathymetry. This light can penetrate water but pulse strength attenuates exponentially with distance traveled through the water. Lidar can measure depths from about 0.9 to 40 m (3 to 131 ft), with vertical accuracy in the order of 15 cm (6 in). The surface reflection makes water shallower than about 0.9 m (3 ft) difficult to resolve, and absorption limits the maximum depth. Turbidity causes scattering and has a significant role in determining the maximum depth that can be resolved in most situations, and dissolved pigments can increase absorption depending on wavelength. Other reports indicate that water penetration tends to be between two and three times Secchi depth. Bathymetric lidar is most useful in the 0–10 m (0–33 ft) depth range in coastal mapping.

On average in fairly clear coastal seawater lidar can penetrate to about 7 m (23 ft), and in turbid water up to about 3 m (10 ft). An average value found by Saputra et al, 2021, is for the green laser light to penetrate water about one and a half to two times Secchi depth in Indonesian waters. Water temperature and salinity have an effect on the refractive index which has a small effect on the depth calculation.

The data obtained shows the full extent of the land surface exposed above the sea floor. This technique is extremely useful as it will play an important role in the major sea floor mapping program. The mapping yields onshore topography as well as underwater elevations. Sea floor reflectance imaging is another solution product from this system which can benefit mapping of underwater habitats. This technique has been used for three-dimensional image mapping of California's waters using a hydrographic lidar.

Airborne lidar systems were traditionally able to acquire only a few peak returns, while more recent systems acquire and digitize the entire reflected signal. Scientists analysed the waveform signal for extracting peak returns using Gaussian decomposition. Zhuang et al, 2017 used this approach for estimating aboveground biomass. Handling the huge amounts of full-waveform data is difficult. Therefore, Gaussian decomposition of the waveforms is effective, since it reduces the data and is supported by existing workflows that support interpretation of 3-D point clouds. Recent studies investigated voxelisation. The intensities of the waveform samples are inserted into a voxelised space (3-D grayscale image) building up a 3-D representation of the scanned area. Related metrics and information can then be extracted from that voxelised space. Structural information can be extracted using 3-D metrics from local areas and there is a case study that used the voxelisation approach for detecting dead standing eucalypt trees in Australia.

Terrestrial applications of lidar (also *terrestrial laser scanning*) happen on the Earth's surface and can be either stationary or mobile. Stationary terrestrial scanning is most common as a survey method, for example in conventional topography, monitoring, cultural heritage documentation and forensics. The 3-D point clouds acquired from these types of scanners can be matched with digital images taken of the scanned area from the scanner's location to create realistic looking 3-D models in a relatively short time when compared to other technologies. Each point in the point cloud is given the colour of the pixel from the image taken at the same location and direction as the laser beam that created the point.

Terrestrial lidar mapping involves a process of occupancy grid map generation. The process involves an array of cells divided into grids which employ a process to store the height values when lidar data falls into the respective grid cell. A binary map is then created by applying a particular threshold to the cell values for further processing. The next step is to process the radial distance and z-coordinates from each scan to identify which 3-D points correspond to each of the specified grid cell leading to the process of data formation.

Mobile lidar (also *mobile laser scanning*) is when two or more scanners are attached to a moving vehicle to collect data along a path. These scanners are almost always paired with other kinds of equipment, including GNSS receivers and IMUs. One example application is surveying streets, where power lines, exact bridge heights, bordering trees, etc. all need to be taken into account. Instead of collecting each of these measurements individually in the field with a tachymeter, a 3-D model from a point cloud can be created where all of the measurements needed can be made, depending on the quality of the data collected. This eliminates the problem of forgetting to take a measurement, so long as the model is available, reliable and has an appropriate level of accuracy.
