---
title: "Lidar (part 2/2)"
source: https://en.wikipedia.org/wiki/Lidar
domain: self-driving-perception
license: CC-BY-SA-4.0
tags: self-driving perception, object detection, semantic segmentation, simultaneous localization mapping
fetched: 2026-07-02
part: 2/2
---

## Applications

There are a wide variety of lidar applications, in addition to the applications listed below, as it is often mentioned in national lidar dataset programs. These applications are largely determined by the range of effective object detection; resolution, which is how accurately the lidar identifies and classifies objects; and reflectance confusion, meaning how well the lidar can see something in the presence of bright objects, like reflective signs or bright sun.

Companies are working to cut the cost of lidar sensors, currently anywhere from about US$1,200 to more than $12,000. Lower prices will make lidar more attractive for new markets.

### Agriculture

Agricultural robots have been used for a variety of purposes ranging from seed and fertilizer dispersions, sensing techniques as well as crop scouting for the task of weed control.

Lidar can help determine where to apply costly fertilizer. It can create a topographical map of the fields and reveal slopes and sun exposure of the farmland. Researchers at the Agricultural Research Service used this topographical data with the farmland yield results from previous years, to categorize land into zones of high, medium, or low yield. This indicates where to apply fertilizer to maximize yield.

Lidar is now used to monitor insects in the field. The use of lidar can detect the movement and behavior of individual flying insects, with identification down to sex and species. In 2017 a patent application was published on this technology in the United States, Europe, and China.

Another application is crop mapping in orchards and vineyards, to detect foliage growth and the need for pruning or other maintenance, detect variations in fruit production, or count plants.

Lidar is useful in GNSS-denied situations, such as nut and fruit orchards, where foliage causes interference for agriculture equipment that would otherwise utilize a precise GNSS fix. Lidar sensors can detect and track the relative position of rows, plants, and other markers so that farming equipment can continue operating until a GNSS fix is reestablished.

Controlling weeds requires identifying plant species. This can be done by using 3-D lidar and machine learning. Lidar produces plant contours as a "point cloud" with range and reflectance values. This data is transformed, and features are extracted from it. If the species is known, the features are added as new data. The species is labelled and its features are initially stored as an example to identify the species in the real environment. This method is efficient because it uses a low-resolution lidar and supervised learning. It includes an easy-to-compute feature set with common statistical features which are independent of the plant size.

### Airport operations

In April 2025, Dallas Fort Worth International Airport announced the deployment of a lidar-based platform for real-time monitoring of passenger and vehicle flows.

### Archaeology

Lidar has many uses in archaeology, including planning of field campaigns, mapping features under forest canopy, and overview of broad, continuous features indistinguishable from the ground. Lidar can produce high-resolution datasets quickly and cheaply. Lidar-derived products can be easily integrated into a geographic information system (GIS) for analysis and interpretation.

Lidar can also help to create high-resolution digital elevation models (DEMs) of archaeological sites that can reveal micro-topography that is otherwise hidden by vegetation. The intensity of the returned lidar signal can be used to detect features buried under flat vegetated surfaces such as fields, especially when mapping using the infrared spectrum. The presence of these features affects plant growth and thus the amount of infrared light reflected back. For example, at Fort Beauséjour – Fort Cumberland National Historic Site, Canada, lidar discovered archaeological features related to the siege of the Fort in 1755. Features that could not be distinguished on the ground or through aerial photography were identified by overlaying hill shades of the DEM created with artificial illumination from various angles. Another example is work at Caracol by Arlen Chase and his wife Diane Zaino Chase. In 2012, lidar was used to search for the legendary city of La Ciudad Blanca or "City of the Monkey God" in the La Mosquitia region of the Honduran jungle. During a seven-day mapping period, evidence was found of man-made structures. In June 2013, the rediscovery of the city of Mahendraparvata was announced. In southern New England, lidar was used to reveal stone walls, building foundations, abandoned roads, and other landscape features obscured in aerial photography by the region's dense forest canopy. In Cambodia, lidar data were used by Damian Evans and Roland Fletcher to reveal anthropogenic changes to Angkor landscape.

In 2012, lidar revealed that the Purépecha settlement of Angamuco in Michoacán, Mexico had about as many buildings as today's Manhattan; while in 2016, its use in mapping ancient Maya causeways in northern Guatemala, revealed 17 elevated roads linking the ancient city of El Mirador to other sites. In 2018, archaeologists using lidar discovered more than 60,000 man-made structures in the Maya Biosphere Reserve, a "major breakthrough" that showed the Maya civilization was much larger than previously thought. In 2024, archaeologists using lidar discovered the Upano Valley sites.

### Autonomous vehicles

Autonomous vehicles may use lidar for obstacle detection and avoidance to navigate safely through environments. The introduction of lidar was a pivotal occurrence that was the key enabler behind Stanley, the first autonomous vehicle to successfully complete the DARPA Grand Challenge. Point cloud output from the lidar sensor provides the necessary data for robot software to determine where potential obstacles exist in the environment and where the robot is in relation to those potential obstacles. Singapore's *Singapore-MIT Alliance for Research and Technology (SMART)* is actively developing technologies for autonomous lidar vehicles.

The very first generations of automotive adaptive cruise control systems used only lidar sensors.

In transportation systems, to ensure vehicle and passenger safety and to develop electronic systems that deliver driver assistance, understanding the vehicle and its surrounding environment is essential. Lidar systems play an important role in the safety of transportation systems. Many electronic systems which enhance driver assistance and vehicle safety such as adaptive cruise control (ACC), emergency brake assist, and anti-lock braking system (ABS) depend on the detection of a vehicle's environment to act autonomously or semi-autonomously. Lidar mapping and estimation achieve this.

Current lidar systems use rotating hexagonal mirrors which split the laser beam. The upper three beams are used for vehicle and obstacles ahead, and the lower beams are used to detect lane markings and road features. The major advantage of using lidar is that the spatial structure is obtained and this data can be fused with other sensors such as radar, etc. to get a better picture of the vehicle environment in terms of static and dynamic properties of the objects present in the environment. Conversely, a significant issue with lidar is the difficulty in reconstructing point cloud data in poor weather conditions. In heavy rain, for example, the light pulses emitted from the lidar system are partially reflected off of rain droplets which adds noise to the data, called 'echoes'.

Obstacle detection and road environment recognition using lidar, proposed by Kun Zhou et al. not only focuses on object detection and tracking but also recognizes lane marking and road features. As mentioned earlier, the lidar systems use rotating hexagonal mirrors that split the laser beam into six beams. The upper three layers are used to detect the forward objects such as vehicles and roadside objects. The sensor is made of weather-resistant material. The data detected by lidar are clustered to several segments and tracked by Kalman filter. Data clustering here is done based on characteristics of each segment based on object model, which distinguish different objects such as vehicles, signboards, etc. These characteristics include the dimensions of the object, etc. The reflectors on the rear edges of vehicles are used to differentiate vehicles from other objects. Object tracking is done using a two-stage Kalman filter considering the stability of tracking and the accelerated motion of objects Lidar reflective intensity data is also used for curb detection by making use of robust regression to deal with occlusions. Road marking is detected using a modified Otsu method by distinguishing rough and shiny surfaces.

Roadside reflectors that indicate lane border are sometimes hidden due to various reasons. Therefore, other information is needed to recognize the road border. The lidar used in this method can measure the reflectivity from the object. Hence, with this data the road border can also be recognized. Also, the usage of a sensor with a weather-robust head helps to detect the objects even in bad weather conditions. Canopy height model before and after a flood is a good example. Lidar can detect highly detailed canopy height data as well as its road border. Lidar measurements help identify the spatial structure of the obstacle. This helps distinguish objects based on size and estimate the impact of driving over it. Lidar systems provide better range and a large field of view, which helps in detecting obstacles on the curves. This is one of its major advantages over radar systems, which have a narrower field of view. The fusion of lidar measurement with different sensors makes the system robust and useful in real-time applications, since lidar-dependent systems cannot estimate the dynamic information about the detected object. It has been shown that lidar can be manipulated, such that self-driving cars are tricked into taking evasive action.

### Ecology and conservation

Lidar has also found many applications for mapping natural and managed landscapes such as forests, wetlands, and grasslands. Canopy heights, biomass measurements, and leaf area can all be studied using airborne lidar systems. Similarly, lidar is also used by many industries, including Energy and Railroad, and the Department of Transportation as a faster way of surveying. Topographic maps can also be generated readily from lidar, including for recreational use such as in the production of orienteering maps. Lidar has also been applied to estimate and assess the biodiversity of plants, fungi, and animals. Using southern bull kelp in New Zealand, coastal lidar mapping data has been compared with population genomic evidence to form hypotheses regarding the occurrence and timing of prehistoric earthquake uplift events.

### Forestry

Lidar systems have also been applied to improve forestry management. Measurements are used to take inventory in forest plots as well as calculate individual tree heights, crown width and crown diameter. Other statistical analysis use lidar data to estimate total plot information such as canopy volume, mean, minimum and maximum heights, vegetation cover, biomass, and carbon density. Aerial lidar was used to map the bush fires in Australia in early 2020. The data was manipulated to view bare earth, and identify healthy and burned vegetation.

### Geology and soil science

High-resolution digital elevation maps generated by airborne and stationary lidar have led to significant advances in geomorphology (the branch of geoscience concerned with the origin and evolution of the Earth surface topography). The lidar abilities to detect subtle topographic features such as river terraces and river channel banks, glacial landforms, to measure the land-surface elevation beneath the vegetation canopy, to better resolve spatial derivatives of elevation, to rockfall detection, to detect elevation changes between repeat surveys have enabled many novel studies of the physical and chemical processes that shape landscapes. In 2005 the Tour Ronde in the Mont Blanc massif became the first high alpine mountain on which lidar was employed to monitor the increasing occurrence of severe rock-fall over large rock faces allegedly caused by climate change and degradation of permafrost at high altitude.

Lidar is also used in structural geology and geophysics as a combination between airborne lidar and GNSS for the detection and study of faults, for measuring uplift. The output of the two technologies can produce extremely accurate elevation models for terrain – models that can even measure ground elevation through trees. This combination was used most famously to find the location of the Seattle Fault in Washington, United States. This combination also measures uplift at Mount St. Helens by using data from before and after the 2004 uplift. Airborne lidar systems monitor glaciers and have the ability to detect subtle amounts of growth or decline. A satellite-based system, the NASA ICESat, includes a lidar sub-system for this purpose. The NASA Airborne Topographic Mapper is also used extensively to monitor glaciers and perform coastal change analysis. The combination is also used by soil scientists while creating a soil survey. The detailed terrain modeling allows soil scientists to see slope changes and landform breaks which indicate patterns in soil spatial relationships.

### Atmosphere

Initially, based on ruby lasers, lidar for meteorological applications was constructed shortly after the invention of the laser and represents one of the first applications of laser technology. Lidar technology has since expanded vastly in capability and lidar systems are used to perform a range of measurements that include profiling clouds, measuring winds, studying aerosols, and quantifying various atmospheric components. Atmospheric components can in turn provide useful information including surface pressure (by measuring the absorption of oxygen or nitrogen), greenhouse gas emissions (carbon dioxide and methane), photosynthesis (carbon dioxide), fires (carbon monoxide), and humidity (water vapor). Atmospheric lidars can be either ground-based, airborne or satellite-based depending on the type of measurement.

Atmospheric lidar remote sensing works in two ways:

1. by measuring backscatter from the atmosphere, and
2. by measuring the scattered reflection off the ground (when the lidar is airborne) or other hard surface.

Backscatter from the atmosphere directly gives a measure of clouds and aerosols. Other derived measurements from backscatter such as winds or cirrus ice crystals require careful selecting of the wavelength and/or polarization detected. *Doppler lidar* and *Rayleigh Doppler lidar* are used to measure temperature and wind speed along the beam by measuring the frequency of the backscattered light. The Doppler broadening of gases in motion allows the determination of properties via the resulting frequency shift. Scanning lidars, such as NASA's conical-scanning HARLIE, have been used to measure atmospheric wind velocity. The ESA wind mission *ADM-Aeolus* will be equipped with a Doppler lidar system in order to provide global measurements of vertical wind profiles. A doppler lidar system was used in the 2008 Summer Olympics to measure wind fields during the yacht competition.

Doppler lidar systems are also now beginning to be successfully applied in the renewable energy sector to acquire wind speed, turbulence, wind veer, and wind shear data. Both pulsed and continuous wave systems are being used. Pulsed systems use signal timing to obtain vertical distance resolution, whereas continuous wave systems rely on detector focusing.

The term *eolics* has been proposed to describe the collaborative and interdisciplinary study of wind using computational fluid mechanics simulations and Doppler lidar measurements.

The ground reflection of an airborne lidar gives a measure of surface reflectivity (assuming the atmospheric transmittance is well known) at the lidar wavelength, however, the ground reflection is typically used for making absorption measurements of the atmosphere. "Differential absorption lidar" (DIAL) measurements utilize two or more closely spaced (less than 1 nm) wavelengths to factor out surface reflectivity as well as other transmission losses, since these factors are relatively insensitive to wavelength. When tuned to the appropriate absorption lines of a particular gas, DIAL measurements can be used to determine the concentration (mixing ratio) of that particular gas in the atmosphere. This is referred to as an *integrated path differential absorption* (IPDA) approach, since it is a measure of the integrated absorption along the entire lidar path. IPDA lidars can be either pulsed or CW and typically use two or more wavelengths. IPDA lidars have been used for remote sensing of carbon dioxide and methane.

*Synthetic array lidar* allows imaging lidar without the need for an array detector. It can be used for imaging Doppler velocimetry, ultra-fast frame rate imaging (millions of frames per second), as well as for speckle reduction in coherent lidar. An extensive lidar bibliography for atmospheric and hydrospheric applications is given by Grant.

### Flood forecasting

In Japan, differential absorption lidar (DIAL) and Raman lidar technologies are being developed to improve the accuracy of flood forecasting and rainfall prediction.

A research by several companies, universities, and institutes, led by Kyushu University is conducting work on meteorological sensing and flood-risk modelling under a government program.

The project focuses on:

- Observing the vertical distribution of water vapor, temperature, wind direction, and wind speed using lidar;
- Integrating this data with satellite observations and upper-air weather maps to create new meteorological data sets;
- Applying artificial intelligence models to simulate and predict precipitation, river flows, and flood risk.

In May 2025, EKO Instruments began a field study on Goto Fukue Island, Nagasaki Prefecture, using a Micropulse DIAL lidar system provided by the National Center for Atmospheric Research (NSF NCAR). The study compares DIAL performance with existing Raman lidar systems.

In addition, EKO Instruments. Co. Ltd. signed a technology license agreement in February 2025 with Montana State University, NSF NCAR, and NASA, covering key DIAL-related patents.

### Military

Few military applications are known to be in place and are classified (such as the lidar-based speed measurement of the AGM-129 ACM stealth nuclear cruise missile), but a considerable amount of research is underway in their use for imaging. Higher resolution systems collect enough detail to identify targets, such as tanks. Examples of military applications of lidar include the Airborne Laser Mine Detection System (ALMDS) for counter-mine warfare by Areté Associates.

A NATO report (RTO-TR-SET-098) evaluated the potential technologies to do stand-off detection for the discrimination of biological warfare agents. The potential technologies evaluated were long-wave infrared (LWIR), differential scattering (DISC), and ultraviolet laser-induced fluorescence (UV-LIF). The report concluded that : *Based upon the results of the lidar systems tested and discussed above, the Task Group recommends that the best option for the near-term (2008–2010) application of stand-off detection systems is UV-LIF*, however, in the long-term, other techniques such as stand-off Raman spectroscopy may prove to be useful for identification of biological warfare agents.

Short-range compact spectrometric lidar based on laser-induced fluorescence (LIF) would address the presence of bio-threats in aerosol form over critical indoor, semi-enclosed and outdoor venues such as stadiums, subways, and airports. This near real-time capability would enable rapid detection of a bioaerosol release and allow for timely implementation of measures to protect occupants and minimize the extent of contamination.

The Long-Range Biological Standoff Detection System (LR-BSDS) was developed for the U.S. Army to provide the earliest possible standoff warning of a biological attack. It is an airborne system carried by helicopter to detect synthetic aerosol clouds containing biological and chemical agents at long range. The LR-BSDS, with a detection range of 30 km or more, was fielded in June 1997. Five lidar units produced by the German company Sick AG were used for short range detection on Stanley, the autonomous car that won the 2005 DARPA Grand Challenge.

A robotic Boeing AH-6 performed a fully autonomous flight in June 2010, including avoiding obstacles using lidar.

### Mining

The calculation of ore volumes is accomplished by periodic (monthly) scanning in areas of ore removal, then comparing surface data to the previous scan.

Lidar sensors may also be used for obstacle detection and avoidance for robotic mining vehicles such as in the Komatsu Autonomous Haulage System (AHS) used in Rio Tinto's Mine of the Future.

### Physics and astronomy

A worldwide network of observatories uses lidars to measure the distance to reflectors placed on the Moon, allowing the position of the Moon to be measured with millimeter precision and tests of general relativity to be done. MOLA, the Mars Orbiting Laser Altimeter, used a lidar instrument in a Mars-orbiting satellite (the NASA Mars Global Surveyor) to produce a spectacularly precise global topographic survey of the red planet. Laser altimeters produced global elevation models of Mars, the Moon (Lunar Orbiter Laser Altimeter (LOLA)), and Mercury (Mercury Laser Altimeter (MLA), NEAR–Shoemaker Laser Rangefinder (NLR)). Future missions will also include laser altimeter experiments such as the Ganymede Laser Altimeter (GALA) as part of the Jupiter Icy Moons Explorer (JUICE) mission.

In September, 2008, the NASA *Phoenix* lander used lidar to detect snow in the atmosphere of Mars.

In atmospheric physics, lidar is used as a remote detection instrument to measure densities of certain constituents of the middle and upper atmosphere, such as potassium, sodium, or molecular nitrogen and oxygen. These measurements can be used to calculate temperatures. Lidar can also be used to measure wind speed and to provide information about vertical distribution of the aerosol particles.

At the JET nuclear fusion research facility in the UK near Abingdon, Oxfordshire, lidar Thomson scattering is used to determine electron density and temperature profiles of the plasma.

### Rock mechanics

Lidar has been widely used in rock mechanics for rock mass characterization and slope change detection. Some important geomechanical properties from the rock mass can be extracted from the 3-D point clouds obtained by means of the lidar. Some of these properties are:

- Discontinuity orientation
- Discontinuity spacing and RQD
- Discontinuity aperture
- Discontinuity persistence
- Discontinuity roughness
- Water infiltration

Some of these properties have been used to assess the geomechanical quality of the rock mass through the RMR index. Moreover, as the orientations of discontinuities can be extracted using the existing methodologies, it is possible to assess the geomechanical quality of a rock slope through the SMR index. In addition to this, the comparison of different 3-D point clouds from a slope acquired at different times allows researchers to study the changes produced on the scene during this time interval as a result of rockfalls or any other landsliding processes.

### THOR

THOR is a laser designed toward measuring Earth's atmospheric conditions. The laser enters a cloud cover and measures the thickness of the return halo. The sensor has a fiber optic aperture with a width of 7+1⁄2 inches (19 cm) that is used to measure the return light.

### Robotics

Lidar technology is being used in robotics for the perception of the environment as well as object classification. The ability of lidar technology to provide three-dimensional elevation maps of the terrain, high precision distance to the ground, and approach velocity can enable safe landing of robotic and crewed vehicles with a high degree of precision. Lidar is also widely used in robotics for simultaneous localization and mapping and is well-integrated into robot simulators. Refer to the Military section above for further examples.

### Spaceflight

Lidar is increasingly being utilized for rangefinding and orbital element calculation of relative velocity in proximity operations and stationkeeping of spacecraft. Lidar has also been used for atmospheric studies from space. Short pulses of laser light beamed from a spacecraft can reflect off tiny particles in the atmosphere and back to a telescope aligned with the spacecraft laser. By precisely timing the lidar echo, and by measuring how much laser light is received by the telescope, scientists can accurately determine the location, distribution and nature of the particles. The result is a revolutionary new tool for studying constituents in the atmosphere, from cloud droplets to industrial pollutants, which are difficult to detect by other means.

Laser altimetry is used to make digital elevation maps of planets, including the Mars Orbital Laser Altimeter (MOLA) mapping of Mars, the Lunar Orbital Laser Altimeter (LOLA) and Lunar Altimeter (LALT) mapping of the Moon, and the Mercury Laser Altimeter (MLA) mapping of Mercury. It is also used to help navigate the helicopter *Ingenuity* in its record-setting flights over the terrain of Mars.

### Surveying

Airborne lidar sensors are used by companies in the remote sensing field. They can be used to create a DTM (digital terrain model) or DEM (digital elevation model); this is quite a common practice for larger areas as a plane can acquire 3–4 km (2–2+1⁄2 mi) wide swaths in a single flyover. Greater vertical accuracy of below 50 mm (2 in) can be achieved with a lower flyover, even in forests, where it is able to give the height of the canopy as well as the ground elevation. Typically, a GNSS receiver configured over a georeferenced control point is needed to link the data in with the WGS (World Geodetic System).

Lidar is also in use in hydrographic surveying. Depending upon the clarity of the water lidar can measure depths from 0.9 to 40 m (3 to 131 ft) with a vertical accuracy of 15 cm (6 in) and horizontal accuracy of 2.5 m (8 ft).

### Transport

Lidar has been used in the railroad industry to generate asset health reports for asset management and by departments of transportation to assess their road conditions. CivilMaps.com is a leading company in the field. Lidar has been used in adaptive cruise control (ACC) systems for automobiles. Systems such as those by Siemens, Hella, Ouster and Cepton use a lidar device mounted on the front of the vehicle, such as the bumper, to monitor the distance between the vehicle and any vehicle in front of it. In the event where the vehicle in front slows down or is too close, the ACC applies the brakes to slow the vehicle. When the road ahead is clear, the ACC allows the vehicle to accelerate to a speed preset by the driver. Refer to the Military section above for further examples. A lidar-based device, the Ceilometer, is used at airports worldwide to measure the height of clouds on runway approach paths.

### Wind farm optimization

Lidar can be used to increase the energy output from wind farms by accurately measuring wind speeds and wind turbulence. Experimental lidar systems can be mounted on the nacelle of a wind turbine or integrated into the rotating spinner to measure oncoming horizontal winds, winds in the wake of the wind turbine, and proactively adjust blades to protect components and increase power. Lidar is also used to characterise the incident wind resource for comparison with wind turbine power production to verify the performance of the wind turbine by measuring the wind turbine's power curve. Wind farm optimization can be considered a topic in *applied eolics*. Another aspect of lidar in wind related industry is to use computational fluid dynamics over lidar-scanned surfaces in order to assess the wind potential, which can be used for optimal wind farm placement.

### Solar photovoltaic deployment optimization

Lidar can also be used to assist planners and developers in optimizing solar photovoltaic systems at the city level by determining appropriate roof tops and for determining shading losses. Recent airborne laser scanning efforts have focused on ways to estimate the amount of solar light hitting vertical building facades, or by incorporating more detailed shading losses by considering the influence from vegetation and larger surrounding terrain.

### Video games

Recent simulation racing games such as *rFactor Pro*, *iRacing*, *Assetto Corsa* and *Project CARS* increasingly feature race tracks reproduced from 3-D point clouds acquired through lidar surveys, resulting in surfaces replicated with centimeter or millimeter precision in the in-game 3-D environment.

The 2017 exploration game *Scanner Sombre*, by Introversion Software, uses lidar as a fundamental game mechanic.

In *Build the Earth*, lidar is used to create accurate renders of terrain in *Minecraft* to account for any errors (mainly regarding elevation) in the default generation. The process of rendering terrain into Build the Earth is limited by the amount of data available in region as well as the speed it takes to convert the file into block data.

### Physical security

Lidar technology enhances physical security by providing precise, privacy-compliant threat detection for applications such as perimeter protection, building facades, and critical infrastructure monitoring. These systems utilize laser-based sensors to create high-density point clouds that function reliably in challenging environmental conditions, including rain, snow, and complete darkness. A key advantage of modern systems is the use of 3D lidar, which creates precise volumetric detection zones capturing height, width, and depth, allowing for the accurate classification of object size and movement speed. Unlike 2D lidar systems, which typically scan a single flat plane and may struggle to distinguish between threats and benign triggers based on height or volume, 3D lidar effectively filters out false alarms caused by small animals or vegetation by analyzing the full spatial dimensions of the detected object.

### Other uses

The video for the 2007 song "House of Cards" by Radiohead was believed to be the first use of real-time 3-D laser scanning to record a music video. The range data in the video is not completely from a lidar, as structured light scanning is also used.

In 2020, Apple introduced the fourth generation of iPad Pro with a lidar sensor integrated into the rear camera module, especially developed for augmented reality (AR) experiences. The feature was later included in the iPhone 12 Pro lineup and subsequent Pro models. On Apple devices, lidar empowers portrait mode pictures with night mode, quickens auto focus and improves accuracy in the Measure app.

In 2022, *Wheel of Fortune* started using lidar technology to track when Vanna White moves her hand over the puzzle board to reveal letters. The first episode to have this technology was in the season 40 premiere.


## Variants

In flash lidar, the entire field of view is illuminated with a wide diverging laser beam in a single pulse. This is in contrast to conventional scanning lidar, which uses a collimated laser beam that illuminates a single point at a time, and the beam is raster scanned to illuminate the field of view point-by-point. This illumination method requires a different detection scheme as well. In both scanning and flash lidar, a time-of-flight camera is used to collect information about both the 3-D location and intensity of the light incident on it in every frame. However, in scanning lidar, this camera contains only a point sensor, while in flash lidar, the camera contains either a 1-D or a 2-D sensor array, each pixel of which collects 3-D location and intensity information. In both cases, the depth information is collected using the time of flight of the laser pulse (i.e., the time it takes each laser pulse to hit the target and return to the sensor), which requires the pulsing of the laser and acquisition by the camera to be synchronized. The result is a camera that takes pictures of distance, instead of colors. Flash lidar is especially advantageous when compared to scanning lidar, when the camera, scene, or both are moving, since the entire scene is illuminated at the same time. With scanning lidar, motion can cause "jitter" from the lapse in time as the laser rasters over the scene.

As with all forms of lidar, the onboard source of illumination makes flash lidar an active sensor. The signal that is returned is processed by embedded algorithms to produce a nearly instantaneous 3-D rendering of objects and terrain features within the field of view of the sensor. The laser pulse repetition frequency is sufficient for generating 3-D videos with high resolution and accuracy. The high frame rate of the sensor makes it a useful tool for a variety of applications that benefit from real-time visualization, such as highly precise remote landing operations. By immediately returning a 3-D elevation mesh of target landscapes, a flash sensor can be used to identify optimal landing zones in autonomous spacecraft landing scenarios.

Seeing at a distance requires a powerful burst of light. The power is limited to levels that do not damage human retinas. Wavelengths must not affect human eyes. However, low-cost silicon imagers do not read light in the eye-safe spectrum. Instead, gallium-arsenide imagers are required, which can boost costs to $200,000. Gallium-arsenide is the same compound used to produce high-cost, high-efficiency solar panels usually used in space applications.


## Alternative technologies

Computer stereo vision has shown promise as an alternative to lidar for close-range applications. It is significantly more cost effective when appropriate.
