---
title: "Weather radar (part 2/2)"
source: https://en.wikipedia.org/wiki/Weather_radar
domain: radar-systems
license: CC-BY-SA-4.0
tags: radar systems, pulse-doppler radar, synthetic-aperture radar, phased array
fetched: 2026-07-02
part: 2/2
---

## Limitations and artifacts

Radar data interpretation depends on many hypotheses about the atmosphere and the weather targets, including:

- International Standard Atmosphere.
- Targets small enough to obey the Rayleigh scattering, resulting in the return being proportional to the precipitation rate.
- The volume scanned by the beam is full of ***meteorological*** targets (rain, snow, etc.), all of the same variety and in a uniform concentration.
- No attenuation
- No amplification
- Return from side lobes of the beam are negligible.
- The beam is close to a Gaussian function curve with power decreasing to half at half the width.
- The outgoing and returning waves are similarly polarized.
- There is no return from multiple reflections.

These assumptions are not always met; one must be able to differentiate between reliable and dubious echoes.

### Anomalous propagation (non-standard atmosphere)

The first assumption is that the radar beam is moving through air that cools down at a certain rate with height. The position of the echoes depend heavily on this hypothesis. However, the real atmosphere can vary greatly from the norm.

#### Super refraction

Temperature inversions often form near the ground, for instance by air cooling at night while remaining warm aloft. As the index of refraction of air decreases faster than normal the radar beam bends toward the ground instead of continuing upward. Eventually, it will hit the ground and be reflected back toward the radar. The processing program will then wrongly place the return echoes at the height and distance it would have been in normal conditions.

This type of false return is relatively easy to spot on a time loop if it is due to night cooling or marine inversion as one sees very strong echoes developing over an area, spreading in size laterally but not moving and varying greatly in intensity. However, inversion of temperature exists ahead of warm fronts and the abnormal propagation echoes are then mixed with real rain.

The extreme of this problem is when the inversion is very strong and shallow, the radar beam reflects many times toward the ground as it has to follow a waveguide path. This will create multiple bands of strong echoes on the radar images.

This situation can be found with inversions of temperature aloft or rapid decrease of moisture with height. In the former case, it could be difficult to notice.

#### Under refraction

On the other hand, if the air is unstable and cools faster than the standard atmosphere with height, the beam ends up higher than expected. This indicates that precipitation is occurring higher than the actual height. Such an error is difficult to detect without additional temperature lapse rate data for the area.

### Non-Rayleigh targets

If we want to reliably estimate the precipitation rate, the targets have to be 10 times smaller than the radar wave according to Rayleigh scattering. This is because the water molecule has to be excited by the radar wave to give a return. This is relatively true for rain or snow as 5 or 10 cm wavelength radars are usually employed.

However, for very large hydrometeors, since the wavelength is on the order of stone, the return levels off according to Mie theory. A return of more than 55 dBZ is likely to come from hail but won't vary proportionally to the size. On the other hand, very small targets such as cloud droplets are too small to be excited and do not give a recordable return on common weather radars.

### Resolution and partially filled scanned volume

As demonstrated at the start of the article, radar beams have a physical dimension and data are sampled at discrete angles, not continuously, along each angle of elevation. This results in an averaging of the values of the returns for reflectivity, velocities and polarization data on the resolution volume scanned.

In the figure to the left, at the top is a view of a thunderstorm taken by a wind profiler as it was passing overhead. This is like a vertical cross section through the cloud with 150-metre vertical and 30-metre horizontal resolution. The reflectivity has large variations in a short distance. Compare this with a simulated view of what a regular weather radar would see at 60 km, in the bottom of the figure. Everything has been smoothed out. Not only the coarser resolution of the radar blur the image but the sounding incorporates area that are echo free, thus extending the thunderstorm beyond its real boundaries.

This shows how the output of weather radar is only an approximation of reality. The image to the right compares real data from two radars almost colocated. The TDWR has about half the beamwidth of the other and one can see twice more details than with the NEXRAD.

Resolution can be improved by newer equipment but some things cannot. As mentioned previously, the volume scanned increases with distance so the possibility that the beam is only partially filled also increases. This leads to underestimation of the precipitation rate at larger distances and fools the user into thinking that rain is lighter as it moves away.

### Beam geometry

The radar beam has a distribution of energy similar to the diffraction pattern of a light passing through a slit. This is because the wave is transmitted to the parabolic antenna through a slit in the wave-guide at the focal point. Most of the energy is at the center of the beam and decreases along a curve close to a Gaussian function on each side. However, there are secondary peaks of emission that will sample the targets at off-angles from the center. Designers attempt to minimize the power transmitted by such lobes, but they cannot be eliminated.

When a secondary lobe hits a reflective target such as a mountain or a strong thunderstorm, some of the energy is reflected to the radar. This energy is relatively weak but arrives at the same time that the central peak is illuminating a different azimuth. The echo is thus misplaced by the processing program. This has the effect of actually broadening the real weather echo making a smearing of weaker values on each side of it. This causes the user to overestimate the extent of the real echoes.

|   |   |   |
|---|---|---|

### Non-weather targets

There is more than rain and snow in the sky. Other objects can be misinterpreted as rain or snow by weather radars. Insects and arthropods are swept along by the prevailing winds, while birds follow their own course. As such, fine line patterns within weather radar imagery, associated with converging winds, are dominated by insect returns. Bird migration, which tends to occur overnight within the lowest 2000 metres of the Earth's atmosphere, contaminates wind profiles gathered by weather radar, particularly the WSR-88D, by increasing the environmental wind returns by 30–60 km/h. Other objects within radar imagery include:

- Thin metal strips (chaff) dropped by military aircraft to fool enemies.
- Solid obstacles such as mountains, buildings, and aircraft.
- Ground and sea clutter.
- Reflections from nearby buildings ("urban spikes").

Such extraneous objects have characteristics that allow a trained eye to distinguish them. It is also possible to eliminate some of them with post-treatment of data using reflectivity, Doppler, and polarization data.

### Wind farms

The rotating blades of windmills on modern wind farms can return the radar beam to the radar if they are in its path. Since the blades are moving, the echoes will have a velocity and can be mistaken for real precipitation. The closer the wind farm, the stronger the return, and the combined signal from many towers is stronger. In some conditions, the radar can even see toward and away velocities that generate false positives for the tornado vortex signature algorithm on weather radar; such an event occurred in 2009 in Dodge City, Kansas.

As with other structures that stand in the beam, attenuation of radar returns from beyond windmills may also lead to underestimation.

### Attenuation

Microwaves used in weather radars can be absorbed by rain, depending on the wavelength used. For 10 cm radars, this attenuation is negligible. That is the reason why countries with high water content storms are using 10 cm wavelength, for example the US NEXRAD. The cost of a larger antenna, klystron and other related equipment is offset by this benefit.

For a 5 cm radar, absorption becomes important in heavy rain and this attenuation leads to underestimation of echoes in and beyond a strong thunderstorm. Canada and other northern countries use this less costly kind of radar as the precipitation in such areas is usually less intense; however, users must consider this characteristic when interpreting data. The images above show how a strong line of echoes seems to vanish as it moves over the radar. To compensate for this behaviour, radar sites are often chosen to somewhat overlap in coverage to give different points of view of the same storms if one is experiencing attenuation.

Shorter wavelengths are even more attenuated and are often only useful in shorter range applications – consequently, many television stations in the United States have 5 cm radars to cover their audience area. Knowing their limitations and using them in conjunction with local NEXRADs can supplement the data available to a meteorologist.

Due to the spread of dual-polarization radar systems, robust and efficient approaches for the compensation of rain attenuation are currently implemented by operational weather services. Attenuation correction in weather radars for snow particles is an active research topic.

### Bright band

A radar beam's reflectivity depends on the diameter of the target and its capacity to reflect. Snowflakes are large but weakly reflective while rain drops are small but highly reflective.

When snow falls through a layer above freezing temperature, it melts into rain. Using the reflectivity equation, one can demonstrate that the returns from the snow before melting and the rain after, are not too different as the change in dielectric constant compensates for the change in size. However, during the melting process, the radar wave "sees" something akin to very large droplets as snow flakes become coated with water.

This gives enhanced returns that can be mistaken for stronger precipitations. On a PPI, this will show up as an intense ring of precipitation at the altitude where the beam crosses the melting level while on a series of CAPPIs, only the ones near that level will have stronger echoes. A good way to confirm a bright band is to make a vertical cross section through the data, as illustrated in the picture above.

An opposite problem is that drizzle (precipitation with small water droplet diameter) tends not to show up on radar because radar returns are proportional to the sixth power of droplet diameter.

### Multiple reflections

It is assumed that the beam hits the weather targets and returns directly to the radar. In fact, there is energy reflected in all directions. Most of it is weak, and multiple reflections diminish it even further so what can eventually return to the radar from such an event is negligible. However, some situations allow a multiple-reflected radar beam to be received by the radar antenna. For instance, when the beam hits hail, the energy spread toward the wet ground will be reflected back to the hail and then to the radar. The resulting echo is weak but noticeable. Due to the extra path length it has to go through, it arrives later at the antenna and is placed further than its source. This gives a kind of triangle of false weaker reflections placed radially behind the hail.


## Solutions and future solutions

### Filtering

These two images show what can be achieved to clean up radar data. On the first image made from the raw returns, it is difficult to distinguish the real weather. Since rain and snow clouds are usually moving, Doppler velocities can be used to eliminate a good part of the clutter (ground echoes, reflections from buildings seen as urban spikes, anomalous propagation). The other image has been filtered using this property.

However, not all non-meteorological targets remain stationary (birds, insects, dust). Others, like the bright band, depend on the structure of the precipitation. Polarization offers a direct typing of the echoes which could be used to filter more false data or produce separate images for specialized purposes, such as clutter, birds, etc. subsets.

In recent years, fuzzy logic-based techniques have emerged as an alternative for clutter mitigation. Automated methods for processing 2D reflectivity data to identify ground clutter based on typical clutter properties like stationarity of echoes, narrow spectrum width, and limited vertical extent were extensively used. Texture-based algorithms based on the horizontal variation of reflectivity to generate a probabilistic clutter map which assigns a likelihood of clutter to each radar pixel, can be used to capture persistent clutter.

### Mesonet

Another question is the resolution. As mentioned, radar data are an average of the scanned volume by the beam. Resolution can be improved by larger antenna or denser networks. A program by the Center for Collaborative Adaptive Sensing of the Atmosphere (CASA) aims to supplement the regular NEXRAD (a network in the United States) using many low cost X-band (3 cm) weather radar mounted on cellular telephone towers. These radars will subdivide the large area of the NEXRAD into smaller domains to look at altitudes below its lowest angle. These will give details not otherwise available.

Using 3 cm radars, the antenna of each radar is small (about 1 meter diameter) but the resolution is similar at short distance to that of NEXRAD. The attenuation is significant due to the wavelength used but each point in the coverage area is seen by many radars, each viewing from a different direction and compensating for data lost from others.

### Scanning strategies

The number of elevation scanned and the time taken for a complete cycle depend on the weather. For example, with little or no precipitation the scheme may be limited to the lowest angles and use longer impulses in order to detect wind shift near the surface. On the other hand, for violent thunderstorms it is better to scan a large range of angles in order to have a 3-D view of the precipitation as often as possible. To mitigate the different demands, scanning strategies have been developed according to the type of radar, the wavelength used and the most common weather situations in the area considered.

One example of scanning strategies is offered by the US NEXRAD radar network which has evolved over time. In 2008, it added extra resolution of data, and in 2014, additional intra-cycle scanning of the lowest level elevation (MESO-SAILS).

### Electronic sounding

With 5 to 10 minutes between complete scans of weather radar, much data is lost as a thunderstorm develops. A Phased-array radar is being tested at the National Severe Storms Lab in Norman, Oklahoma, to speed the data gathering. A team in Japan has also deployed a phased-array radar for 3D NowCasting at the RIKEN Advanced Institute for Computational Science (AICS).


## Specialized applications

### Avionics weather radar

Aircraft application of radar systems include weather radar, collision avoidance, target tracking, ground proximity, and other systems. For commercial weather radar, ARINC 708 is the primary specification for weather radar systems using an airborne pulse-Doppler radar.

#### Antennas

Unlike ground weather radar, which is set at a fixed angle, airborne weather radar is being utilized from the nose or wing of an aircraft. Not only will the aircraft be moving up, down, left, and right, but it will be rolling as well. To compensate for this, the antenna is linked and calibrated to the vertical gyroscope located on the aircraft. By doing this, the pilot is able to set a pitch or angle to the antenna that will enable the stabilizer to keep the antenna pointed in the right direction under moderate maneuvers. The small servo motors will not be able to keep up with abrupt maneuvers, but it will try. In doing this the pilot is able to adjust the radar so that it will point towards the weather system of interest. If the airplane is at a low altitude, the pilot would want to set the radar above the horizon line so that ground clutter is minimized on the display. If the airplane is at a very high altitude, the pilot will set the radar at a low or negative angle, to point the radar towards the clouds wherever they may be relative to the aircraft. If the airplane changes attitude, the stabilizer will adjust itself accordingly so that the pilot doesn't have to fly with one hand and adjust the radar with the other.

#### Receivers/transmitters

There are two major systems when talking about the receiver/transmitter: the first is high-powered systems, and the second is low-powered systems; both of which operate in the X-band frequency range (8,000 – 12,500 MHz). High-powered systems operate at 10,000 – 60,000 watts. These systems consist of magnetrons that are fairly expensive (approximately $1,700) and allow for considerable noise due to irregularities with the system. Thus, these systems are highly dangerous for arcing and are not safe to be used around ground personnel. However, the alternative would be the low-powered systems. These systems operate 100 – 200 watts, and require a combination of high gain receivers, signal microprocessors, and transistors to operate as effectively as the high-powered systems. The complex microprocessors help to eliminate noise, providing a more accurate and detailed depiction of the sky. Also, since there are fewer irregularities throughout the system, the low-powered radars can be used to detect turbulence via the Doppler Effect. Since low-powered systems operate at considerable less wattage, they are safe from arcing and can be used at virtually all times.

### Thunderstorm tracking

Digital radar systems have capabilities far beyond their predecessors. They offer thunderstorm tracking surveillance which provides users with the ability to acquire detailed information of each storm cloud being tracked. Thunderstorms are identified by matching raw precipitation data received from the radar pulse, to a preprogrammed template. In order for a thunderstorm to be confirmed, it must meet strict definitions of intensity and shape to distinguish it from a non-convective cloud. Usually, it must show signs of horizontal organization and vertical continuity: and have a core or a more intense center identified and tracked by digital radar trackers. Once the thunderstorm cell is identified, speed, distance covered, direction, and Estimated Time of Arrival (ETA) are all tracked and recorded.

### Doppler radar and bird migration

Using Doppler weather radar is not limited to determining the location and velocity of precipitation. It can track bird migrations as well (non-weather targets section). The radio waves from the radars bounce off rain and birds alike (or even insects like butterflies). The US National Weather Service, for instance, has reported having flights of birds appear on their radars as clouds and then fade away when the birds land. The U.S. National Weather Service St. Louis has even reported monarch butterflies appearing on its radars.

Different programs in North America use regular weather radars and specialized radar data to determine the paths, height of flight, and timing of migrations. This is useful information in planning windmill farm placement and operation, to reduce bird fatalities, improve aviation safety and other wildlife management. In Europe, there have been similar developments and even a comprehensive forecast program for aviation safety, based on radar detection.

### Meteorite fall detection

An image shows the Park Forest, Illinois, meteorite fall which occurred on 26 March 2003. The red-green feature at the upper left is the motion of clouds near the radar itself, and a signature of falling meteorites is inside the yellow ellipse at image center. The intermixed red and green pixels indicate turbulence, in this case arising from the wakes of falling, high-velocity meteorites.

According to the American Meteor Society, meteorite falls occur on a daily basis somewhere on Earth. However, the database of worldwide meteorite falls maintained by the Meteoritical Society typically records only about 10-15 new meteorite falls annually

Meteorites occur when a meteoroid falls into the Earth's atmosphere, generating an optically bright meteor by ionization and frictional heating. If the meteoroid is large enough and infall velocity is low enough, it will reach the ground. When the falling meteoroid decelerate below about 2–4 km/s, usually at an altitude between 15 and 25 km, they no longer generate an optically bright meteor and enter "dark flight". Because of this, most of the falls occurring into the oceans, during the day, or otherwise go unnoticed.

It is in dark flight that falling meteoroids typically fall through the interaction volume of most types of radars. It has been demonstrated that it is possible to identify falling meteoroids in weather radar imagery. This is especially useful for meteorite recovery, as weather radars are part of widespread networks and scan the atmosphere continuously. Furthermore, the meteorites cause local wind turbulence, which is noticeable on Doppler outputs, and fall nearly vertically so their resting place on the ground is close to their radar signature.
