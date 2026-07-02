---
title: "Geopositioning"
source: https://en.wikipedia.org/wiki/Geolocation
domain: geolocation-api
license: CC-BY-SA-4.0
tags: geolocation api, device position coordinates, watch position updates, location permission prompt
fetched: 2026-07-02
---

# Geopositioning

(Redirected from

Geolocation

)

**Geopositioning** is the process of determining or estimating the geographic position of an object or a person. Geopositioning yields a set of geographic coordinates (such as latitude and longitude) in a given map datum. Geographic positions may also be expressed indirectly, as a distance in linear referencing or as a bearing and range from a known landmark. The resulting geoposition is sometimes referred to as *geolocation*, and the process of geopositioning may also be described as *geo-localization*. In turn, positions can be used to determine a more easily understandable location, such as a street address (see *reverse geocoding*).

Specific instances include:

- animal geotracking, the process of inferring the location of animals over time;
- positioning system, the mechanisms for the determination of geographic positions in general;
- internet geolocation, geolocating a device connected to the internet;
- and mobile phone tracking.

## Geofencing

*Geofencing* involves creating a virtual geographic boundary (a geofence), enabling software to trigger a response when a device enters or leaves a particular area. Geopositioning is a pre-requisite for geofencing.

## Background

Geopositioning uses various visual and electronic methods including position lines and position circles, celestial navigation, radio navigation, radio and WiFi positioning systems, and the use of satellite navigation systems.

The calculation requires measurements or observations of distances or angles to reference points whose positions are known. In 2D surveys, observations of three reference points are enough to compute a position in a two-dimensional plane. In practice, observations are subject to errors resulting from various physical and atmospheric factors that influence the measurement of distances and angles.

A practical example of obtaining a position fix would be for a ship to take bearing measurements on three lighthouses positioned along the coast. These measurements could be made visually using a hand bearing compass, or in case of poor visibility, electronically using radar or radio direction finding. Since all physical observations are subject to errors, the resulting position fix is also subject to inaccuracy. Although in theory two lines of position (LOP) are enough to define a point, in practice 'crossing' more LOPs provides greater accuracy and confidence, especially if the lines cross at a good angle to each other. Three LOPs are considered the minimum for a practical navigational fix. The three LOPs when drawn on the chart will in general form a triangle, known as a 'cocked hat'. The navigator will have more confidence in a position fix that is formed by a small cocked hat with angles close to those of an equilateral triangle. The area of doubt surrounding a position fix is called an error ellipse. To minimize the error, electronic navigation systems generally use more than three reference points to compute a position fix to increase the data redundancy. As more redundant reference points are added, the position fix becomes more accurate and the area of the resulting error ellipse decreases.

The process of using 3 reference points to calculate the location is called Trilateration, and when using more than 3 points, *multilateration*.

Combining multiple observations to compute a position fix is equivalent to solving a system of linear equations. Navigation systems use regression algorithms such as least squares in order to compute a position fix in 3D space. This is most commonly done by combining distance measurements to 4 or more GPS satellites, which orbit the Earth along known paths.

The result of position fixing is called a **position fix** (**PF**), or simply a **fix**, a position derived from measuring in relation to external reference points. In nautical navigation, the term is generally used with manual or visual techniques, such as the use of intersecting visual or radio position lines, rather than the use of more automated and accurate electronic methods like GPS; in aviation, use of electronic navigation aids is more common. A visual fix can be made by using any sighting device with a bearing indicator. Two or more objects of known position are sighted, and the bearings recorded. Bearing lines are then plotted on a chart through the locations of the sighted items. The intersection of these lines is the current position of the vessel.

Usually, a fix is where two or more position lines intersect at any given time. If three position lines can be obtained, the resulting "cocked hat", where the three lines do not intersect at the same point, but create a triangle, gives the navigator an indication of the accuracy. The most accurate fixes occur when the position lines are perpendicular to each other. Fixes are a necessary aspect of navigation by dead reckoning, which relies on estimates of speed and course. The fix confirms the actual position during a journey. A fix can introduce inaccuracies if the reference point is not correctly identified or is inaccurately measured.

### Indoor geopositioning

Geopositioning can be referred to both global positioning and outdoor positioning, using for example GPS, and to indoor positioning, for all the situations where satellite GPS is not a viable option and the localization process has to happen indoors. For indoor positioning, tracking and localization there are many technologies that can be used, depending on the specific needs and on the environmental characteristics.
