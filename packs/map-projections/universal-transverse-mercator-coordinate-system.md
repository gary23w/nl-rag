---
title: "Universal Transverse Mercator coordinate system"
source: https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system
domain: map-projections
license: CC-BY-SA-4.0
tags: map projection, mercator projection, coordinate reference system, geodetic datum
fetched: 2026-07-02
---

# Universal Transverse Mercator coordinate system

The **Universal Transverse Mercator** (**UTM**) is a projected coordinate system based on the *transverse Mercator* map projection of the Earth spheroid. As a map projection, it transforms geographic coordinates of locations on Earth's surface to assign plane coordinates to them. It is a horizontal position representation, which means it ignores altitude and treats the earth surface as an oblate ellipsoid. The system divides Earth into 60 zones and projects each to the plane as a basis for its coordinates. Specifying a location means specifying the zone and the *x*, *y* coordinate in that plane.

UTM parameter specifications vary by nation or region or mapping system. However, most zones in UTM span 6 degrees of longitude, and each has a designated central meridian. In each zone, the scale factor at the central meridian is specified to be 0.9996 of true scale (for most UTM systems in use). Therefore maps, atlases, and topographic grid systems built from an appropriate collection of UTM zones cover a region with planar maps with well-controlled, minimal distortion. For this reason, UTM coordinates are used in many nations and regions for topographic mapping, as well as more generally for pinpointing locations.

## History

The National Oceanic and Atmospheric Administration (NOAA) website states that the system was developed by the United States Army Corps of Engineers, starting in the early 1940s. However, a series of aerial photos found in the Bundesarchiv-Militärarchiv (the military section of the German Federal Archives) apparently dating from 1943–1944 bear the inscription UTMREF followed by grid letters and digits, and projected according to the transverse Mercator, a finding that would indicate that something called the UTM Reference system was developed in the 1942–43 time frame by the Wehrmacht. It was probably carried out by the Abteilung für Luftbildwesen (Department for Aerial Photography). From 1947 onward the US Army employed a very similar system, but with the now-standard 0.9996 scale factor at the central meridian as opposed to the German 1.0. For areas within the contiguous United States the Clarke Ellipsoid of 1866 was used. For the remaining areas of Earth, including Hawaii, the International Ellipsoid was used.

While historically UTM has been used with a range of geodetic datums, since the proliferation of civilian GPS usage, the World Geodetic System WGS84 ellipsoid has become the default for specifying a point's longitude and latitude. The WGS84 datum has therefore become the implicit default for UTM coordinates as well, if no alternate datum is specified. In North America, WGS84 UTM coordinates of a given point can differ up to 200 meters from older ones based on NAD27, for instance.

Prior to the development of the Universal Transverse Mercator coordinate system, several European nations demonstrated the utility of grid-based conformal maps by mapping their territory during the interwar period. Calculating the distance between two points on these maps could be performed more easily in the field (using the Pythagorean theorem) than was possible using the trigonometric formulas required under the graticule-based system of latitude and longitude. In the post-war years, these concepts were extended into the Universal Transverse Mercator/Universal Polar Stereographic (UTM/UPS) coordinate system, which is a global (or universal) system of grid-based maps.

The transverse Mercator projection is a variant of the Mercator projection, which was originally developed by the Flemish geographer and cartographer Gerardus Mercator, in 1570. This projection is conformal, which means it preserves angles and therefore shapes across small regions. However, it distorts distance and area.

## Definitions

### UTM zone

The UTM system divides the Earth into 60 zones, each 6° of longitude in width. Zone 1 covers longitude 180° to 174° W; zone numbering increases eastward to zone 60, which covers longitude 174°E to 180°. The polar regions south of 80°S and north of 84°N are excluded, and instead covered by the universal polar stereographic (UPS) coordinate system.

Each of the 60 zones uses a transverse Mercator projection that can map a region of large north-south extent with low distortion. By using narrow zones of 6° of longitude (up to 668 km) in width, and reducing the scale factor along the central meridian to 0.9996 (a reduction of 1:2500), the amount of distortion is held below 1 part in 1,000 inside each zone. Distortion of scale increases to 1.0010 at the zone boundaries along the equator.

In each zone the scale factor of the central meridian reduces the diameter of the transverse cylinder to produce a secant projection with two standard lines, or lines of true scale, about 180 km on each side of, and about parallel to, the central meridian (Arc cos 0.9996 = 1.62° at the Equator). The scale is less than 1 inside the standard lines and greater than 1 outside them, but the overall distortion is minimized.

### Exceptions

The UTM zones are uniform across the globe, except in two areas. On the southwest coast of Norway, zone 32 is extended 3° further west, and zone 31 is correspondingly shrunk to cover only open water. Also, in the region around Svalbard, the zones 32, 34 and 36 are not used, while zones 31 (9° wide), 33 (12° wide), 35 (12° wide), and 37 (9° wide) are extended to cover the gaps.

### Overlapping grids

Distortion of scale increases in each UTM zone as the boundaries between the UTM zones are approached. However, it is often convenient or necessary to measure a series of locations on a single grid when some are located in two adjacent zones. Around the boundaries of large scale maps (1:100,000 or larger) coordinates for both adjoining UTM zones are usually printed within a minimum distance of 40 km on either side of a zone boundary. Ideally, the coordinates of each position should be measured on the grid for the zone in which they are located, but because the scale factor is still relatively small near zone boundaries, it is possible to overlap measurements into an adjoining zone for some distance when necessary.

### Latitude bands

Latitude bands are not a part of UTM, but rather a part of the military grid reference system (MGRS). They are however sometimes included in UTM notation. Including latitude bands in UTM notation can lead to ambiguous coordinates—as the letter "S" either refers to the southern hemisphere or a latitude band in the northern hemisphere—and should therefore be avoided.

## Locating a position using UTM coordinates

A position on the Earth is given by the UTM zone number and hemisphere designator and the easting and northing planar coordinate pair in that zone.

The point of origin of each UTM zone is the intersection of the equator and the zone's central meridian. To avoid dealing with negative numbers, a false Easting of −500000 meters is added to the central meridian. Thus a point that has an easting of 400000 meters is about 100 km west of the central meridian. For most such points, the true distance would be slightly more than 100 km as measured on the surface of the Earth because of the distortion of the projection. UTM eastings range from about 166000 meters to 834000 meters at the equator.

In the Northern Hemisphere positions are measured northward from zero at the equator. The maximum "northing" value is about 9300000 meters at latitude 84 degrees North, the north end of the UTM zones. The Southern Hemisphere's northing at the equator is set at 10000000 meters. Northings decrease southward from these 10000000 meters to about 1100000 meters at 80 degrees South, the south end of the UTM zones. Therefore, no point has a negative northing value.

For example, the CN Tower is at 43°38′33.24″N 79°23′13.7″W﻿ / ﻿43.6425667°N 79.387139°W﻿ / 43.6425667; -79.387139﻿ (CN Tower), which is in UTM zone 17, and the grid position is 630084 m east, 4833438 m north. Two points in Zone 17 have these coordinates, one in the Northern Hemisphere and one in the south; the non-ambiguous format is to specify the full zone and hemisphere designator, that is, "17N 630084 4833438".

### Simplified formulae

These formulae are truncated version of Transverse Mercator: flattening series, which were originally derived by Johann Heinrich Louis Krüger in 1912. They are accurate to around a millimeter within 3000 km of the central meridian. Concise commentaries for their derivation have also been given.

The WGS 84 spatial reference system describes Earth as an oblate spheroid along north-south axis with an equatorial radius of $a=6378.137$ km and an inverse flattening of $1/f=298.257\,223\,563$ . Taking a point of latitude $\,\varphi$ and of longitude $\,\lambda$ and computing its UTM coordinates as well as point scale factor $k\,\!$ and meridian convergence $\gamma \,\!$ using a reference meridian of longitude $\lambda _{0}$ . By convention, in the Northern Hemisphere $N_{0}=0$ km and in the Southern Hemisphere $N_{0}=10000$ km. By convention also $k_{0}=0.9996$ and $E_{0}=500$ km.

In the following formulas, the distances are in kilometers and angles are in radians. First, here are some preliminary values:

${\begin{aligned}n&={\frac {f}{2-f}},&A&={\frac {a}{1+n}}\left(1+{\frac {n^{2}}{4}}+{\frac {n^{4}}{64}}\right),\\{}\end{aligned}}$

${\begin{aligned}\alpha _{1}&={\frac {1}{2}}n-{\frac {2}{3}}n^{2}+{\frac {5}{16}}n^{3},&\alpha _{2}&={\frac {13}{48}}n^{2}-{\frac {3}{5}}n^{3},&\alpha _{3}&={\frac {61}{240}}n^{3},\\[12pt]\beta _{1}&={\frac {1}{2}}n-{\frac {2}{3}}n^{2}+{\frac {37}{96}}n^{3},&\beta _{2}&={\frac {1}{48}}n^{2}+{\frac {1}{15}}n^{3},&\beta _{3}&={\frac {17}{480}}n^{3},\\[12pt]\delta _{1}&=2n-{\frac {2}{3}}n^{2}-2n^{3},&\delta _{2}&={\frac {7}{3}}n^{2}-{\frac {8}{5}}n^{3},&\delta _{3}&={\frac {56}{15}}n^{3}.\end{aligned}}$

#### From latitude, longitude (*φ*, *λ*) to UTM coordinates (E, N)

First we compute some intermediate values:

$t=\sinh \left(\tanh ^{-1}\left(\sin \varphi \right)-{\frac {2{\sqrt {n}}}{1+n}}\tanh ^{-1}\left({\frac {2{\sqrt {n}}}{1+n}}\sin \varphi \right)\right),$

$\xi '=\tan ^{-1}\left({\frac {t}{\cos(\lambda -\lambda _{0})}}\right),\,\,\,\eta '=\tanh ^{-1}\left({\frac {\sin(\lambda -\lambda _{0})}{\sqrt {1+t^{2}}}}\right),$

$\sigma =1+\sum _{j=1}^{3}2j\alpha _{j}\cos(2j\xi ')\cosh(2j\eta '),\,\,\,\tau =\sum _{j=1}^{3}2j\alpha _{j}\sin(2j\xi ')\sinh(2j\eta ').$

The final formulae are:

$E=E_{0}+k_{0}A\left(\eta '+\sum _{j=1}^{3}\alpha _{j}\cos(2j\xi ')\sinh(2j\eta ')\right),$

$N=N_{0}+k_{0}A\left(\xi '+\sum _{j=1}^{3}\alpha _{j}\sin(2j\xi ')\cosh(2j\eta ')\right),$

$k={\frac {k_{0}A}{a}}{\sqrt {\left\{1+\left({\frac {1-n}{1+n}}\tan \varphi \right)^{2}\right\}{\frac {\sigma ^{2}+\tau ^{2}}{t^{2}+\cos ^{2}(\lambda -\lambda _{0})}}}},$

$\gamma =\tan ^{-1}\left({\frac {\tau {\sqrt {1+t^{2}}}+\sigma t\tan(\lambda -\lambda _{0})}{\sigma {\sqrt {1+t^{2}}}-\tau t\tan(\lambda -\lambda _{0})}}\right).$

where E is Easting, N is Northing, k is the Scale Factor, and $\gamma$ is the Grid Convergence.

#### From UTM coordinates (E, N, Zone, Hemi) to latitude, longitude (*φ*, *λ*)

Note: Hemi = +1 for Northern, Hemi = −1 for Southern

First let's compute some intermediate values:

$\xi ={\frac {N-N_{0}}{k_{0}A}},\,\,\,\eta ={\frac {E-E_{0}}{k_{0}A}},$

$\xi '=\xi -\sum _{j=1}^{3}\beta _{j}\sin \left(2j\xi \right)\cosh \left(2j\eta \right),\,\,\,\eta '=\eta -\sum _{j=1}^{3}\beta _{j}\cos \left(2j\xi \right)\sinh \left(2j\eta \right),$

$\sigma '=1-\sum _{j=1}^{3}2j\beta _{j}\cos \left(2j\xi \right)\cosh \left(2j\eta \right),\,\,\,\tau '=\sum _{j=1}^{3}2j\beta _{j}\sin \left(2j\xi \right)\sinh \left(2j\eta \right),$

$\chi =\sin ^{-1}\left({\frac {\sin \xi '}{\cosh \eta '}}\right).$

The final formulae are:

$\varphi =\chi +\sum _{j=1}^{3}\delta _{j}\sin \left(2j\chi \right),$

$\lambda _{0}=\mathrm {Z} \mathrm {o} \mathrm {n} \mathrm {e} \times 6^{\circ }-183^{\circ }\,$

$\lambda =\lambda _{0}+\tan ^{-1}\left({\frac {\sinh \eta '}{\cos \xi '}}\right),$

$k={\frac {k_{0}A}{a}}{\sqrt {\left\{1+\left({\frac {1-n}{1+n}}\tan \varphi \right)^{2}\right\}{\frac {\cos ^{2}\xi '+\sinh ^{2}\eta '}{\sigma '^{2}+\tau '^{2}}}}},$

$\gamma =\mathrm {H} \mathrm {e} \mathrm {m} \mathrm {i} \times \tan ^{-1}\left({\frac {\tau '+\sigma '\tan \xi '\tanh \eta '}{\sigma '-\tau '\tan \xi '\tanh \eta '}}\right).$

## Map distortion within UTM zones

Since transverse Mercator projections are conformal, maps in UTM coordinates do not distort subtended angles or local shapes, and scale distortion is isotropic. Distortion at a specific point is wholly described by the (direction-free) scale factor k and grid convergence angle $\gamma$ , which both depend on the displacement from the central meridian $\lambda _{0}$ of the UTM zone used.

More specifically, on a UTM map, meridians other than the central one are slightly curved, their rotation (tangent line at any point) given by the grid convergence angle $\gamma$ there. The scale factor increases from $k_{0}$ at the central meridian. The value of each depends on the latitude $\phi$ and the deviation in longitude $\Delta \lambda =\lambda -\lambda _{0}$ . Formulas using ellipsoidal parameters are given above, but useful simpler first order approximations are

$\gamma \approx \Delta \lambda \sin \varphi \approx (32.39'')(E-E_{0})_{\text{in km}}\tan \varphi$

$k\approx k_{0}\left(1+{\tfrac {1}{2}}(\Delta \lambda _{\text{in radians}})^{2}\cos ^{2}\varphi \right)$

The quadratic dependence for scale factor makes it fairly constant around the central meridian, increasing more rapidly when closer to a zone's edge. At zone edges, $\Delta \lambda =\pm 3$ °, the scale factor is approximately 1.0010 at the equator and 1.0005 at latitude 45°. At a distance of about 180 km east or west of the central meridian, the scale factor is precisely 1, regardless of latitude.

Alternative coordinate systems with narrower zones, such as MTM or certain U.S. SPCSes, allow for quadratically lower scale distortion at the expense of narrower single-zone coverage.

These formulas for $\gamma$ and k are particularly relevant for converting paths described by ground distances and astronomic (true) bearings, for instance land surveyors' measurements, to UTM coordinates. For a small-scale survey (extent <1 km), $\gamma$ and k are both essentially constant for the whole area covered. However, for conversion of ground distance to grid, correcting the scale factor for elevation is also necessary (projecting down to the reference geoid at elevation zero). For medium-scale surveys (a few km in east-west extent), the change in $\gamma$ over the area represented may be material, as shown by the part of the formula using E . However, the variation of k over the area will be negligible. In practice, surveyors will usually use one combined scale factor (covering average distance from central meridian and elevation) and one grid convergence angle in digitizing and coordinate-parametrizing any one cadastral survey, though may be forced to vary $\gamma$ when integrating with neighboring surveys along a long east-west traverse. These approximations are too inaccurate for larger scales, such as for infrastructure projects or longer administrative boundary retracements.
