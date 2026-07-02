---
title: "Trilateration"
source: https://en.wikipedia.org/wiki/Trilateration
domain: gps-positioning
license: CC-BY-SA-4.0
tags: gps positioning, satellite navigation, gnss positioning, nmea sentence
fetched: 2026-07-02
---

# Trilateration

**Trilateration** is the use of distances (or "ranges") for determining the unknown position coordinates of a point of interest. When more than three distances are involved, it may also be called **multilateration**, for emphasis. The point of interest is often around Earth (geopositioning).

The distances or ranges might be ordinary Euclidean distances (slant ranges) or spherical distances (scaled central angles), as in *true-range multilateration*; or biased distances (pseudo-ranges), as in *pseudo-range multilateration*.

Trilateration or multilateration should not be confused with *triangulation*, which uses angles for positioning; and *direction finding*, which determines the line of sight direction to a target without determining the radial distance.

## Terminology

Multiple, sometimes overlapping and conflicting terms are employed for similar concepts – e.g., *multilateration* without modification has been used for aviation systems employing both true-ranges and pseudo-ranges. Moreover, different fields of endeavor may employ different terms. In geometry, *trilateration* is defined as the process of determining absolute or relative locations of points by measurement of distances, using the geometry of circles, spheres or triangles. In surveying, *trilateration* is a specific technique.

## True-range multilateration

True-range multilateration (also termed range–range multilateration and spherical multilateration) is a method to determine the location of a movable vehicle or stationary point in space using multiple ranges (distances) between the vehicle/point and multiple spatially-separated known locations (often termed "stations"). Energy waves may be involved in determining range, but are not required.

True-range multilateration is both a mathematical topic and an applied technique used in several fields. A practical application involving a fixed location occurs in surveying. Applications involving vehicle location are termed navigation when on-board persons/equipment are informed of its location, and are termed surveillance when off-vehicle entities are informed of the vehicle's location.

Two *slant ranges* from two known locations can be used to locate a third point in a two-dimensional Cartesian space (plane), which is a frequently applied technique (e.g., in surveying). Similarly, two *spherical ranges* can be used to locate a point on a sphere, which is a fundamental concept of the ancient discipline of celestial navigation — termed the *altitude intercept* problem. Moreover, if more than the minimum number of ranges are available, it is good practice to utilize those as well. This article addresses the general issue of position determination using multiple ranges.

In two-dimensional geometry, it is known that if a point lies on two circles, then the circle centers and the two radii provide sufficient information to narrow the possible locations down to two – one of which is the desired solution and the other is an ambiguous solution. Additional information often narrow the possibilities down to a unique location. In three-dimensional geometry, when it is known that a point lies on the surfaces of three spheres, then the centers of the three spheres along with their radii also provide sufficient information to narrow the possible locations down to no more than two (unless the centers lie on a straight line).

True-range multilateration can be contrasted to the more frequently encountered pseudo-range multilateration, which employs range differences to locate a (typically, movable) point. Pseudo range multilateration is almost always implemented by measuring times-of-arrival (TOAs) of energy waves. True-range multilateration can also be contrasted to triangulation, which involves the measurement of angles.

## Pseudo-range multilateration

Pseudo-range multilateration, often simply multilateration (MLAT) when in context, is a technique for determining the position of an unknown point, such as a vehicle, based on measurement of biased *times of flight* (TOFs) of energy waves traveling between the vehicle and multiple stations at known locations. TOFs are biased by synchronization errors in the difference between *times of arrival* (TOA) and *times of transmission* (TOT): TOF = TOA − TOT. *Pseudo-ranges* (PRs) are TOFs multiplied by the wave propagation speed: PR = TOF·*s*. In general, the stations' clocks are assumed synchronized but the vehicle's clock is desynchronized.

In MLAT for surveillance, the waves are transmitted by the vehicle and received by the stations; the TOT is unique and unknown, while the TOAs are multiple and known. When MLAT is used for navigation (as in *hyperbolic navigation*), the waves are transmitted by the stations and received by the vehicle; in this case, the TOTs are multiple but known, while the TOA is unique and unknown. In navigation applications, the vehicle is often termed the "user"; in surveillance applications, the vehicle may be termed the "target".

The vehicle's clock is considered an additional unknown, to be estimated along with the vehicle's position coordinates. If d is the number of physical dimensions being considered (e.g., 2 for a plane) and m is the number of signals received (thus, TOFs measured), it is required that $m\geq d+1$ .

Processing is usually required to extract the TOAs or their differences from the received signals, and an algorithm is usually required to solve this set of equations. An algorithm either: (a) determines numerical values for the TOT (for the receiver(s) clock) and d vehicle coordinates; or (b) ignores the TOT and forms $m-1$ (at least d) time difference of arrivals (TDOAs), which are used to find the d vehicle coordinates. Almost always, $d=2$ (e.g., a plane or the surface of a sphere) or $d=3$ (e.g., the real physical world). Systems that form TDOAs are also called *hyperbolic* systems, for reasons discussed below.

A multilateration *navigation* system provides vehicle position information to an entity "on" the vehicle (e.g., aircraft pilot or Global Positioning System (GPS) receiver operator). A multilateration *surveillance* system provides vehicle position to an entity "not on" the vehicle (e.g., air traffic controller or cell phone provider). By the reciprocity principle, any method that can be used for navigation can also be used for surveillance, and vice versa (the same information is involved).

Systems have been developed for both TOT and TDOA (which ignore TOT) algorithms. In this article, TDOA algorithms are addressed first, as they were implemented first. Due to the technology available at the time, TDOA systems often determined a vehicle location in two dimensions. TOT systems are addressed second. They were implemented, roughly, post-1975 and usually involve satellites. Due to technology advances, TOT algorithms generally determine a user/vehicle location in three dimensions. However, conceptually, TDOA or TOT algorithms are not linked to the number of dimensions involved.
