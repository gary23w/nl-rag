---
title: "Weather radar (part 1/2)"
source: https://en.wikipedia.org/wiki/Weather_radar
domain: radar-systems
license: CC-BY-SA-4.0
tags: radar systems, pulse-doppler radar, synthetic-aperture radar, phased array
fetched: 2026-07-02
part: 1/2
---

# Weather radar

A **weather radar**, also called **weather surveillance radar** (**WSR**) and **Doppler weather radar**, is a type of radar used to locate precipitation, calculate its motion, and estimate its type (rain, snow, hail etc.). Modern weather radars are mostly pulse-Doppler radars, capable of detecting the motion of rain droplets in addition to the intensity of the precipitation. Both types of data can be analyzed to determine the structure of storms and their potential to cause severe weather.

During World War II, radar operators discovered that weather was causing echoes on their screens, masking potential enemy targets. Techniques were developed to filter them, but scientists began to study the phenomenon. Soon after the war, surplus radars were used to detect precipitation. Since then, weather radar has evolved and is used by national weather services, research departments in universities, and in television stations' weather departments. Raw images are routinely processed by specialized software to make short term forecasts of future positions and intensities of rain, snow, hail, and other weather phenomena. Radar output is even incorporated into numerical weather prediction models to improve analyses and forecasts.


## History

During World War II, military radar operators noticed noise in returned echoes due to rain, snow, and sleet. After the war, military scientists returned to civilian life or continued in the Armed Forces and pursued their work in developing a use for those echoes. In the United States, David Atlas at first working for the Air Force and later for MIT, developed the first operational weather radars. In Canada, J.S. Marshall and R.H. Douglas formed the "Stormy Weather Group" in Montreal. Marshall and his doctoral student Walter Palmer are well known for their work on the drop size distribution in mid-latitude rain that led to understanding of the Z-R relation, which correlates a given radar reflectivity with the rate at which rainwater is falling. In the United Kingdom, research continued to study the radar echo patterns and weather elements such as stratiform rain and convective clouds, and experiments were done to evaluate the potential of different wavelengths from 1 to 10 centimeters. By 1950 the UK company EKCO was demonstrating its airborne 'cloud and collision warning search radar equipment'.

Between 1950 and 1980, reflectivity radars, which measure the position and intensity of precipitation, were incorporated by weather services around the world. The early meteorologists had to watch a cathode-ray tube. In 1953 Donald Staggs, an electrical engineer working for the Illinois State Water Survey, made the first recorded radar observation of a "hook echo" associated with a tornadic thunderstorm.

The first use of weather radar on television in the United States was in September 1961. As Hurricane Carla was approaching the state of Texas, local reporter Dan Rather, suspecting the hurricane was very large, took a trip to the U.S. Weather Bureau WSR-57 radar site in Galveston in order to get an idea of the size of the storm. He convinced the bureau staff to let him broadcast live from their office and asked a meteorologist to draw him a rough outline of the Gulf of Mexico on a transparent sheet of plastic. During the broadcast, he held that transparent overlay over the computer's black-and-white radar display to give his audience a sense both of Carla's size and of the location of the storm's eye. This made Rather a national name and his report helped in the alerted population accepting the evacuation of an estimated 350,000 people by the authorities, which was the largest evacuation in US history at that time. Just 46 people were killed thanks to the warning and it was estimated that the evacuation saved several thousand lives, as the smaller 1900 Galveston hurricane had killed an estimated 6000-12000 people.

During the 1970s, radars began to be standardized and organized into networks. The first devices to capture radar images were developed. The number of scanned angles was increased to get a three-dimensional view of the precipitation, so that horizontal cross-sections (CAPPI) and vertical cross-sections could be performed. Studies of the organization of thunderstorms were then possible for the Alberta Hail Project in Canada and National Severe Storms Laboratory (NSSL) in the US in particular.

The NSSL, created in 1964, began experimentation on dual polarization signals and on Doppler effect uses. In May 1973, a tornado devastated Union City, Oklahoma, just west of Oklahoma City. For the first time, a Dopplerized 10 cm wavelength radar from NSSL documented the entire life cycle of the tornado. The researchers discovered a mesoscale rotation in the cloud aloft before the tornado touched the ground – the tornadic vortex signature. NSSL's research helped convince the National Weather Service that Doppler radar was a crucial forecasting tool. The Super Outbreak of tornadoes on 3–4 April 1974 and their devastating destruction might have helped to get funding for further developments.

Between 1980 and 2000, weather radar networks became the norm in North America, Europe, Japan and other developed countries. Conventional radars were replaced by Doppler radars, which in addition to position and intensity could track the relative velocity of the particles in the air. In the United States, the construction of a network consisting of 10 cm radars, called NEXRAD or WSR-88D (Weather Surveillance Radar 1988 Doppler), was started in 1988 following NSSL's research. In Canada, Environment Canada constructed the King City station, with a 5 cm research Doppler radar, by 1985; McGill University dopplerized its radar (J. S. Marshall Radar Observatory) in 1993. This led to a complete Canadian Doppler network between 1998 and 2004. France and other European countries had switched to Doppler networks by the early 2000s. Meanwhile, rapid advances in computer technology led to algorithms to detect signs of severe weather, and many applications for media outlets and researchers.

After 2000, research on dual polarization technology moved into operational use, increasing the amount of information available on precipitation type (e.g. rain vs. snow). "Dual polarization" means that microwave radiation which is polarized both horizontally and vertically (with respect to the ground) is emitted. Wide-scale deployment was done by the end of the decade or the beginning of the next in some countries such as the United States, France, and Canada. In April 2013, all United States National Weather Service NEXRADs were completely dual-polarized.

Since 2003, the U.S. National Oceanic and Atmospheric Administration has been experimenting with phased-array radar as a replacement for conventional parabolic antenna to provide more time resolution in atmospheric sounding. This could be significant with severe thunderstorms, as their evolution can be better evaluated with more timely data.

Also in 2003, the National Science Foundation established the Engineering Research Center for Collaborative Adaptive Sensing of the Atmosphere (CASA), a multidisciplinary, multi-university collaboration of engineers, computer scientists, meteorologists, and sociologists to conduct fundamental research, develop enabling technology, and deploy prototype engineering systems designed to augment existing radar systems by sampling the generally undersampled lower troposphere with inexpensive, fast scanning, dual polarization, mechanically scanned and phased array radars.

In 2023, the private American company Tomorrow.io launched a Ka-band space-based radar for weather observation and forecasting.


## Principle

### Sending radar pulses

Weather radars send directional pulses of microwave radiation, on the order of one microsecond long, using a cavity magnetron or klystron tube connected by a waveguide to a parabolic antenna. The wavelengths of 1 – 10 cm are approximately ten times the diameter of the droplets or ice particles of interest, because Rayleigh scattering occurs at these frequencies. This means that part of the energy of each pulse will bounce off these small particles, back towards the radar station.

Shorter wavelengths are useful for smaller particles, but the signal is more quickly attenuated. Thus 10 cm (S-band) radar is preferred but is more expensive than a 5 cm C-band system. 3 cm X-band radar is used only for short-range units, and 1 cm Ka-band weather radar is used only for research on small-particle phenomena such as drizzle and fog. W band (3 mm) weather radar systems have seen limited university use, but due to quicker attenuation, most data are not operational.

Radar pulses diverge as they move away from the radar station. Thus the volume of air that a radar pulse is traversing is larger for areas farther away from the station, and smaller for nearby areas, decreasing resolution at farther distances. At the end of a 150 – 200 km sounding range, the volume of air scanned by a single pulse might be on the order of a cubic kilometer. This is called the *pulse volume*.

The volume of air that a given pulse takes up at any point in time may be approximated by the formula $\,{v=hr^{2}\theta ^{2}}$ , where v is the volume enclosed by the pulse, h is pulse width (in e.g. meters, calculated from the duration in seconds of the pulse times the speed of light), r is the distance from the radar that the pulse has already traveled (in e.g. meters), and $\,\theta$ is the beam width (in radians). This formula assumes the beam is symmetrically circular, "r" is much greater than "h" so "r" taken at the beginning or at the end of the pulse is almost the same, and the shape of the volume is a cone frustum of depth "h".

### Listening for return signals

Between each pulse, the radar station serves as a receiver as it listens for return signals from particles in the air. The duration of the "listen" cycle is on the order of a millisecond, which is a thousand times longer than the pulse duration. The length of this phase is determined by the need for the microwave radiation (which travels at the speed of light) to propagate from the detector to the weather target and back again, a distance which could be several hundred kilometers. The horizontal distance from station to target is calculated simply from the amount of time that elapses from the initiation of the pulse to the detection of the return signal. The time is converted into distance by multiplying by the speed of light in air:

${\text{Distance}}=c{\frac {\Delta t}{2n}},$

where *c* = 299,792.458 km/s is the speed of light, and *n* ≈ 1.0003 is the refractive index of air.

If pulses are emitted too frequently, the returns from one pulse will be confused with the returns from previous pulses, resulting in incorrect distance calculations.

### Determining height

Since the Earth is round, the radar beam in vacuum would rise according to the reverse curvature of the Earth. However, the atmosphere has a refractive index that diminishes with height, due to its diminishing density. This bends the radar beam slightly toward the ground and with a standard atmosphere this is equivalent to considering that the curvature of the beam is 4/3 the actual curvature of the Earth. Depending on the elevation angle of the antenna and other considerations, the following formula may be used to calculate the target's height above ground:

$H={\sqrt {r^{2}+(k_{e}a_{e})^{2}+2rk_{e}a_{e}\sin(\theta _{e})}}-k_{e}a_{e}+h_{a},$

where:

r

= distance radar–target,

k

e

= 4/3,

a

e

=

Earth

radius,

θ

e

=

elevation angle

above the

radar horizon

,

h

a

= height of the feedhorn above ground.

### Effective volume coverage

A weather radar network uses a series of typical angles that are set according to its needs. After each scanning rotation, the antenna elevation is changed for the next sounding. This scenario will be repeated on many angles to scan the entire volume of air around the radar within the maximum range. Usually, the scanning strategy is completed within 5 to 10 minutes to have data within 15 km above ground and 250 km distance of the radar. For instance in Canada, the 5 cm weather radars use angles ranging from 0.3 to 25 degrees. The accompanying image shows the volume scanned when multiple angles are used.

Due to the Earth's curvature and change of index of refraction with height, the radar cannot "see" below the height above ground of the minimal angle (shown in green) or closer to the radar than the maximal one (shown as a red cone in the center).

### Calibrating return intensity

Because the targets are not unique in each volume, the radar equation has to be developed beyond the basic one. Assuming a monostatic radar where $G_{t}=A_{r}(\mathrm {or} \,G_{r})=G$ :

$P_{r}=P_{t}{{G^{2}\lambda ^{2}\sigma } \over {{(4\pi )}^{3}R^{4}}}\propto {\frac {\sigma }{R^{4}}}$

where $\scriptstyle P_{r}$ is received power, $\scriptstyle P_{t}$ is transmitted power, $\scriptstyle G$ is the gain of the transmitting/receiving antenna, $\scriptstyle \lambda$ is radar wavelength, $\scriptstyle \sigma$ is the radar cross section of the target and $\scriptstyle R$ is the distance from transmitter to target.

In this case, the cross sections of all the targets must be summed:

$\sigma ={\bar {\sigma }}=V\sum \sigma _{j}=V\eta$

${\begin{cases}V\quad =\mathrm {scanned\,\,volume} \\\qquad =\mathrm {pulse\,\,length} \times \mathrm {beam\,\,width} \\\qquad ={\frac {c\tau }{2}}{\frac {\pi R^{2}\theta ^{2}}{4}}\end{cases}}$

where $\,c$ is the light speed, $\,\tau$ is temporal duration of a pulse and $\,\theta$ is the beam width in radians.

In combining the two equations:

$P_{r}=P_{t}{{G^{2}\lambda ^{2}} \over {{(4\pi )}^{3}R^{4}}}{\frac {c\tau }{2}}{\frac {\pi R^{2}\theta ^{2}}{4}}\eta =P_{t}\tau G^{2}\lambda ^{2}\theta ^{2}{\frac {c}{512(\pi ^{2})}}{\frac {\eta }{R^{2}}}$

Which leads to:

$P_{r}\propto {\frac {\eta }{R^{2}}}$

The return varies inversely to **$\,R^{2}$** instead of **$\,R^{4}$**. In order to compare the data coming from different distances from the radar, one has to normalize them with this ratio.


## Data types

### Reflectivity

Return echoes from targets ("reflectivity") are analyzed for their intensities to establish the precipitation rate in the scanned volume. The wavelengths used (1–10 cm) ensure that this return is proportional to the rate because they are within the validity of Rayleigh scattering which states that the targets must be much smaller than the wavelength of the scanning wave (by a factor of 10).

Reflectivity perceived by the radar (Ze) varies by the sixth power of the rain droplets' diameter (D), the square of the dielectric constant (K) of the targets and the drop size distribution (e.g. N[D] of *Marshall-Palmer*) of the drops. This gives a truncated Gamma function, of the form:

$Z_{e}=\int _{0}^{Dmax}|K|^{2}N_{0}e^{-\Lambda D}D^{6}dD$

Precipitation rate (R), on the other hand, is equal to the number of particles, their volume and their fall speed (v[D]) as:

$R=\int _{0}^{Dmax}N_{0}e^{-\Lambda D}{\pi D^{3} \over 6}v(D)dD$

So Ze and R have similar functions that can be resolved by giving a relation between the two, in the form called *Z-R relation*:

Z = aR

b

Where a and b depend on the type of precipitation (snow, rain, convective or stratiform), which has different $\Lambda$ , K, N0 and v.

- As the antenna scans the atmosphere, on every angle of azimuth it obtains a certain strength of return from each type of target encountered. Reflectivity is then averaged for that target to have a better data set.
- Since variation in diameter and dielectric constant of the targets can lead to large variability in power return to the radar, reflectivity is expressed in dBZ (10 times the logarithm of the ratio of the echo to a standard 1 mm diameter drop filling the same scanned volume).

#### How to read reflectivity on a radar display

Radar returns are usually described by colour or level. The colours in a radar image normally range from blue or green for weak returns, to red or magenta for very strong returns. The numbers in a verbal report increase with the severity of the returns. For example, the U.S. National NEXRAD radar sites use the following scale for different levels of reflectivity:

- magenta: 65 dBZ (extremely heavy precipitation, > 16 in (410 mm) per hour, but likely hail)
- red: 50 dBZ (heavy precipitation of 2 in (51 mm) per hour)
- yellow: 35 dBZ (moderate precipitation of 0.25 in (6.4 mm) per hour)
- green: 20 dBZ (light precipitation)

Strong returns (red or magenta) may indicate not only heavy rain but also thunderstorms, hail, strong winds, or tornadoes, but they need to be interpreted carefully, for reasons described below.

##### Aviation conventions

When describing weather radar returns, pilots, dispatchers, and air traffic controllers will typically refer to three return levels:

- **level 1** corresponds to a green radar return, indicating usually light precipitation and little to no turbulence, leading to a possibility of reduced visibility.
- **level 2** corresponds to a yellow radar return, indicating moderate precipitation, leading to the possibility of very low visibility, moderate turbulence and an uncomfortable ride for aircraft passengers.
- **level 3** corresponds to a red radar return, indicating heavy precipitation, leading to the possibility of thunderstorms and severe turbulence and structural damage to the aircraft.

Aircraft will try to avoid level 2 returns when possible, and will always avoid level 3 unless they are specially designed research aircraft.

##### Precipitation types

Some displays provided by commercial television outlets (both local and national) and weather websites, like The Weather Channel and AccuWeather, show precipitation types during the winter months: rain, snow, mixed precipitations (sleet and freezing rain). This is not an analysis of the radar data itself but a post-treatment done with other data sources, the primary being surface reports (METAR).

Over the area covered by radar echoes, a program assigns a precipitation type according to the surface temperature and dew point reported at the underlying weather stations. Precipitation types reported by human operated stations and certain automatic ones (AWOS) will have higher weight. Then the program does interpolations to produce an image with defined zones. These will include interpolation errors due to the calculation. Mesoscale variations of the precipitation zones will also be lost. More sophisticated programs use the numerical weather prediction output from models, such as NAM and WRF, for the precipitation types and apply it as a first guess to the radar echoes, then use the surface data for final output.

Until dual-polarization (section Polarization below) data are widely available, any precipitation types on radar images are only indirect information and must be taken with care.

### Velocity

Precipitation is found in and below clouds. Light precipitation such as drops and flakes is subject to the air currents, and scanning radar can pick up the horizontal component of this motion, thus giving the possibility to estimate the wind speed and direction where precipitation is present.

A target's motion relative to the radar station causes a change in the reflected frequency of the radar pulse, due to the Doppler effect. With velocities of less than 70-metre/second for weather echos and radar wavelength of 10 cm, this amounts to a change only 0.1 ppm. This difference is too small to be noted by electronic instruments. However, as the targets move slightly between each pulse, the returned wave has a noticeable phase difference or *phase shift* from pulse to pulse.

#### Pulse pair

Doppler weather radars use this phase difference (pulse pair difference) to calculate the precipitation's motion. The intensity of the successively returning pulse from the same scanned volume where targets have slightly moved is:

$I=I_{0}\sin \left({\frac {4\pi (x_{0}+v\Delta t)}{\lambda }}\right)=I_{0}\sin \left(\Theta _{0}+\Delta \Theta \right)\quad {\begin{cases}x={\text{distance from radar to target}}\\\lambda ={\text{radar wavelength}}\\\Delta t={\text{time between two pulses}}\end{cases}}$

So $\Delta \Theta ={\frac {4\pi v\Delta t}{\lambda }}$ , *v* = target speed = ${\frac {\lambda \Delta \Theta }{4\pi \Delta t}}$ . This speed is called the radial Doppler velocity because it gives only the radial variation of distance versus time between the radar and the target. The real speed and direction of motion has to be extracted by the process described below.

#### Doppler dilemma

The phase between pulse pairs can vary from - $\pi$ and + $\pi$ , so the unambiguous Doppler velocity range is

V

max

=

$\pm$

${\frac {\lambda }{4\Delta t}}$

This is called the Nyquist velocity. This is inversely dependent on the time between successive pulses: the smaller the interval, the larger is the unambiguous velocity range. However, we know that the maximum range from reflectivity is directly proportional to $\Delta t$ :

x =

${\frac {c\Delta t}{2}}$

The choice becomes increasing the range from reflectivity at the expense of velocity range, or increasing the latter at the expense of range from reflectivity. In general, the useful range compromise is 100–150 km for reflectivity. This means for a wavelength of 5 cm (as shown in the diagram), an unambiguous velocity range of 12.5 to 18.75 metre/second is produced (for 150 km and 100 km, respectively). For a 10 cm radar such as the NEXRAD, the unambiguous velocity range would be doubled.

Some techniques using two alternating pulse repetition frequencies (PRF) allow a greater Doppler range. The velocities noted with the first pulse rate could be equal or different with the second. For instance, if the maximum velocity with a certain rate is 10 metre/second and the one with the other rate is 15 m/s. The data coming from both will be the same up to 10 m/s, and will differ thereafter. It is then possible to find a mathematical relation between the two returns and calculate the real velocity beyond the limitation of the two PRFs.

#### Doppler interpretation

In a uniform rainstorm moving eastward, a radar beam pointing west will "see" the raindrops moving toward itself, while a beam pointing east will "see" the drops moving away. When the beam scans to the north or to the south, no relative motion is noted.

##### Synoptic

In the synoptic scale interpretation, the user can extract the wind at different levels over the radar coverage region. As the beam is scanning 360 degrees around the radar, data will come from all those angles and be the radial projection of the actual wind on the individual angle. The intensity pattern formed by this scan can be represented by a cosine curve (maximum in the precipitation motion and zero in the perpendicular direction). One can then calculate the direction and the strength of the motion of particles as long as there is enough coverage on the radar screen.

However, the rain drops are falling. As the radar only sees the radial component and has a certain elevation from ground, the radial velocities are contaminated by some fraction of the falling speed. This component is negligible in small elevation angles, but must be taken into account for higher scanning angles.

##### Mesoscale

In the velocity data, there could be smaller zones in the radar coverage where the wind varies from the one mentioned above. For example, a thunderstorm is a mesoscale phenomenon which often includes rotations and turbulence. These may only cover few square kilometers but are visible by variations in the radial speed. Users can recognize velocity patterns in the wind associated with rotations, such as mesocyclone, convergence (outflow boundary) and divergence (downburst).

### Polarization

Droplets of falling liquid water tend to have a larger horizontal axis due to the drag coefficient of air while falling (water droplets). This causes the water molecule dipole to be oriented in that direction; so, radar beams are, generally, polarized horizontally in order to receive the maximal signal reflection.

If two pulses are sent simultaneously with orthogonal polarization (vertical and horizontal, *ZV* and *ZH* respectively), two independent sets of data will be received. These signals can be compared in several useful ways:

- Differential Reflectivity (*Zdr*) – Differential reflectivity is proportional to the ratio of the reflected horizontal and vertical power returns as *ZH* / *ZV*. Among other things, it is a good indicator of droplet shape. Differential reflectivity also can provide an estimate of average droplet size, as larger drops are more subject to deformation by aerodynamic forces than are smaller ones (that is, larger drops are more likely to become "hamburger bun-shaped") as they fall through the air.
- Correlation Coefficient (*ρhv*) – A statistical correlation between the reflected horizontal and vertical power returns. High values, near one, indicate homogeneous precipitation types, while lower values indicate regions of mixed precipitation types, such as rain and snow, or hail, or in extreme cases debris aloft, usually coinciding with a tornado debris signature and a tornado vortex signature.
- Linear Depolarization Ratio (*LDR*) – This is a ratio of a vertical power return from a horizontal pulse or a horizontal power return from a vertical pulse. It can also indicate regions where there is a mixture of precipitation types.
- Differential Phase (*$\Phi _{dp}$*) – The differential phase is a comparison of the returned phase difference between the horizontal and vertical pulses. This change in phase is caused by the difference in the number of wave cycles (or wavelengths) along the propagation path for horizontal and vertically polarized waves. It should not be confused with the Doppler frequency shift, which is caused by the motion of the cloud and precipitation particles. Unlike the differential reflectivity, correlation coefficient and linear depolarization ratio, which are all dependent on reflected power, the differential phase is a "propagation effect." It is a very good estimator of rain rate and is not affected by attenuation. The range derivative of differential phase (specific differential phase, *Kdp*) can be used to localize areas of strong precipitation/attenuation.

With more information about particle shape, dual-polarization radars can more easily distinguish airborne debris from precipitation, making it easier to locate tornados.

With this new knowledge added to the reflectivity, velocity, and spectrum width produced by Doppler weather radars, researchers have been working on developing algorithms to differentiate precipitation types, non-meteorological targets, and to produce better rainfall accumulation estimates. In the U.S., NCAR and NSSL have been world leaders in this field.

NOAA established a test deployment for dual-polametric radar at NSSL and equipped all its 10 cm NEXRAD radars with dual-polarization, which was completed in April 2013. In 2004, ARMOR Doppler Weather Radar in Huntsville, Alabama was equipped with a SIGMET Antenna Mounted Receiver, giving Dual-Polarmetric capabilities to the operator. McGill University J. S. Marshall Radar Observatory in Montreal, Canada has converted its instrument (1999) and the data were used operationally by Environment Canada in Montreal until its closure in 2018. Another Environment Canada radar, in King City (North of Toronto), was dual-polarized in 2005; it uses a 5 cm wavelength, which experiences greater attenuation. Environment Canada is converting gradually all of its radars to dual-polarization. Météo-France is planning on incorporating dual-polarizing Doppler radar in its network coverage.


## Radar display methods

Various methods of displaying data from radar scans have been developed over time to address the needs of its users. This is a list of common and specialized displays:

### Plan position indicator

Since data is obtained one angle at a time, the first way of displaying it has been the Plan Position Indicator (PPI) which is only the layout of radar return on a two dimensional image. Importantly, the data coming from different distances to the radar are at different heights above ground.

This is very important as a high rain rate seen near the radar is relatively close to what reaches the ground but what is seen from 160 km away is about 1.5 km above ground and could be far different from the amount reaching the surface. It is thus difficult to compare weather echoes at different distances from the radar.

PPIs are affected by ground echoes near the radar. These can be misinterpreted as real echoes. Other products and further treatments of data have been developed to supplement such shortcomings.

Usage: Reflectivity, Doppler and polarimetric data can use PPI.

In the case of Doppler data, two points of view are possible: relative to the surface or the storm. When looking at the general motion of the rain to extract wind at different altitudes, it is better to use data relative to the radar. But when looking for rotation or wind shear under a thunderstorm, it is better to use storm relative images that subtract the general motion of precipitation leaving the user to view the air motion as if he would be sitting on the cloud.

### Constant-altitude plan position indicator

To avoid some of the PPI problems, the constant-altitude plan position indicator (CAPPI) has been developed by Canadian researchers. It is a horizontal cross-section through radar data. This way, one can compare precipitation on an equal footing at difference distance from the radar and avoid ground echoes. Although data are taken at a certain height above ground, a relation can be inferred between ground stations' reports and the radar data.

CAPPIs call for a large number of angles from near the horizontal to near the vertical of the radar to have a cut that is as close as possible at all distance to the height needed. Even then, after a certain distance, there isn't any angle available and the CAPPI becomes the PPI of the lowest angle. The zigzag line on the angles diagram above shows the data used to produce 1.5 km and 4 km height CAPPIs. Notice that the section after 120 km is using the same data.

**Usage**

Since the CAPPI uses the closest angle to the desired height at each point from the radar, the data can originate from slightly different altitudes, as seen on the image, in different points of the radar coverage. It is therefore crucial to have a large enough number of sounding angles to minimize this height change. Furthermore, the type of data must change relatively gradually with height to produce an image that is not noisy.

Reflectivity data being relatively smooth with height, CAPPIs are mostly used for displaying them. Velocity data, on the other hand, can change rapidly in direction with height and CAPPIs of them are not common. It seems that only McGill University is producing regularly Doppler CAPPIs with the 24 angles available on their radar. However, some researchers have published papers using velocity CAPPIs to study tropical cyclones and development of NEXRAD products. Finally, polarimetric data are recent and often noisy. There doesn't seem to have regular use of CAPPI for them although the *SIGMET* company offer a software capable to produce those types of images.

### Vertical composite

Another solution to the PPI problems is to produce images of the maximum reflectivity in a layer above ground. This solution is usually taken when the number of angles available is small or variable. The American National Weather Service is using such Composite as their scanning scheme can vary from 4 to 14 angles, according to their need, which would make very coarse CAPPIs. The Composite assures that no strong echo is missed in the layer and a treatment using Doppler velocities eliminates the ground echoes. Comparing base and composite products, one can locate virga and updrafts zones.

### Accumulations

Another important use of radar data is the ability to assess the amount of precipitation that has fallen over large basins, to be used in hydrological calculations; such data is useful in flood control, sewer management and dam construction. The computed data from radar weather may be used in conjunction with data from ground stations.

To produce radar accumulations, we have to estimate the rain rate over a point by the average value over that point between one PPI, or CAPPI, and the next; then multiply by the time between those images. If one wants for a longer period of time, one has to add up all the accumulations from image to image during that time.

### Echotops

Aviation is a heavy user of radar data. One map particularly important in this field is the Echotops for flight planning and avoidance of dangerous weather. Most country weather radars scan enough angles to have a 3D set of data over the area of coverage. It is relatively easy to estimate the maximum altitude at which precipitation is found within the volume. However, those are not the tops of clouds, as they always extend above the precipitation.

### Vertical cross sections

To know the vertical structure of clouds, in particular thunderstorms or the level of the melting layer, a vertical cross-section product of the radar data is available to meteorologists. This is done by displaying only the data along a line, from coordinates A to B, taken from the different angles scanned.

### Range Height Indicator

When a weather radar is scanning in only the vertical axis, it can obtain data at the same resolution as PPI scans, as opposed to the often coarse interpolation from volumes, of which the scans therein are often separated in time by several minutes and thousands of feet. This output is called a *Range Height Indicator* (RHI), which is excellent for viewing the detailed smaller-scale vertical structure of a storm. As mentioned, this is different from the vertical cross section mentioned above, namely due to the fact that the radar antenna is scanning solely vertically, and does not scan over the entire 360 degrees around the site. This kind of product is typically only available on research radars.

### Radar networks

Over the past few decades, radar networks have been extended to allow the production of composite views covering large areas. For instance, countries such as the United States, Canada, Australia, Japan, and much of Europe, combine images from their radar network into a singular display.

In fact, such a network can consist of different types of radar with different characteristics like beam width, wavelength and calibration. These differences have to be taken into account when matching data across the network, particularly when deciding what data to use when two radars cover the same point. If one uses the stronger echo but it comes from the most distant radar, one uses returns that are from higher altitude coming from rain or snow that might evaporate before reaching the ground (virga). If one uses data from the closest radar, it might be attenuated by passing through a thunderstorm. Composite images of precipitations using a network of radars are made with all those limitations in mind.

### Automatic algorithms

To help meteorologists spot dangerous weather, mathematical algorithms have been introduced in the weather radar treatment programmes. These are particularly important in analyzing the Doppler velocity data as they are more complex. The polarization data will even need more algorithms.

Main algorithms for reflectivity:

- Vertically Integrated Liquid (VIL) is an estimate of the total mass of precipitation in the clouds.
- *VIL Density* is VIL divided by the height of the cloud top. It is a clue to the possibility of large hail in thunderstorms.
- *Potential wind gust*, which can estimate the winds under a cloud (a downdraft) using the VIL and the height of the echotops (radar estimated top of the cloud) for a given storm cell.
- Hail algorithms that estimate the presence of hail and its probable size.

Main algorithms for Doppler velocities:

- Mesocyclone detection: is triggered by a velocity change over a small circular area. The algorithm is searching for a "*doublet*" of inbound/outbound velocities with the zero line of velocities, between the two, along a radial line from the radar. Usually the mesocyclone detection must be found on two or more stacked progressive tilts of the beam to be significative of rotation into a thunderstorm cloud.
- TVS or Tornado Vortex Signature algorithm is essentially a mesocyclone with a large velocity threshold found through many scanning angles. This algorithm is used in NEXRAD to indicate the possibility of a tornado formation.
- Wind shear in low levels. This algorithm detects the variation of wind velocities from point to point in the data and looks for a *doublet* of inbound/outbound velocities with the zero line perpendicular to the radar beam. The wind shear is associated with downdraft, (downburst and microburst), gust fronts and turbulence under thunderstorms.
- VAD Wind Profile (VWP) is a display that estimates the direction and speed of the horizontal wind at various upper levels of the atmosphere, using the technique explained in the Doppler section.

### Animations

The animation of radar products can show the evolution of reflectivity and velocity patterns. The user can extract information on the dynamics of the meteorological phenomena, including the ability to extrapolate the motion and observe development or dissipation. This can also reveal non-meteorological artifacts (false echoes) that will be discussed later.

#### Radar Integrated Display with Geospatial Elements

A new popular presentation of weather radar data in United States is via *Radar Integrated Display with Geospatial Elements* (RIDGE) in which the radar data is projected on a map with geospatial elements such as topography maps, highways, state/county boundaries and weather warnings. The projection is often flexible giving the user a choice of various geographic elements. It is frequently used in conjunction with animations of radar data over a time period.
