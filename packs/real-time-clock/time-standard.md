---
title: "Time standard"
source: https://en.wikipedia.org/wiki/Time_standard
domain: real-time-clock
license: CC-BY-SA-4.0
tags: real-time clock, backup battery, time standard, epoch counter
fetched: 2026-07-02
---

# Time standard

A **time standard** is a specification for measuring time: either the rate at which time passes or points in time or both. In modern times, several time specifications have been officially recognized as standards, where formerly they were matters of custom and practice. An example of a kind of time standard can be a time scale, specifying a method for measuring divisions of time. A standard for civil time can specify both time intervals and time-of-day.

Standardized time measurements are made using a clock to count periods of some period changes, which may be either the changes of a natural phenomenon or of an artificial machine.

Historically, time standards were often based on the Earth's rotational period. From the late 18 century to the 19th century it was assumed that the Earth's daily rotational rate was constant. Astronomical observations of several kinds, including eclipse records, studied in the 19th century, raised suspicions that the rate at which Earth rotates is gradually slowing and also shows small-scale irregularities, and this was confirmed in the early twentieth century. Time standards based on Earth rotation were replaced (or initially supplemented) for astronomical use from 1952 onwards by an *ephemeris time* standard based on the Earth's orbital period and in practice on the motion of the Moon. The invention in 1955 of the caesium atomic clock has led to the replacement of older and purely astronomical time standards, for most practical purposes, by newer time standards based wholly or partly on atomic time.

Various types of second and day are used as the basic time interval for most time scales. Other intervals of time (minutes, hours, and years) are usually defined in terms of these two.

## Terminology

The term "time" is generally used for many close but different concepts, including:

- instant as an object – one point on the time axis. Being an object, it has no value;
  - date as a quantity characterizing an instant. As a quantity, it has a value which may be expressed in a variety of ways, for example "2014-04-26T09:42:36,75" in ISO standard format, or more colloquially such as "today, 9:42 a.m.";
- time interval as an object – part of the time axis limited by two instants. Being an object, it has no value;
  - duration as a quantity characterizing a time interval. As a quantity, it has a value, such as a number of minutes, or may be described in terms of the quantities (such as times and dates) of its beginning and end.
- chronology, an ordered sequence of events in the past. Chronologies can be put into chronological groups (periodization). One of the most important systems of periodization is the geologic time scale, which is a system of periodizing the events that shaped the Earth and its life. Chronology, periodization, and interpretation of the past are together known as the study of history.

## Definitions of the second

There have only ever been three definitions of the second: as a fraction of the day, as a fraction of an extrapolated year, and as the microwave frequency of a caesium atomic clock.

In early history, clocks were not accurate enough to track seconds. After the invention of mechanical clocks, the CGS system and MKS system of units both defined the second as 1⁄86,400 of a mean solar day. MKS was adopted internationally during the 1940s.

In the late 1940s, quartz crystal oscillator clocks could measure time more accurately than the rotation of the Earth. Metrologists also knew that Earth's orbit around the Sun (a year) was much more stable than Earth's rotation. This led to the definition of ephemeris time and the tropical year, and the ephemeris second was defined as "the fraction 1⁄31,556,925.9747 of the tropical year for 1900 January 0 at 12 hours ephemeris time". This definition was adopted as part of the International System of Units in 1960.

Most recently, atomic clocks have been developed that offer improved accuracy. Since 1967, the SI base unit for time is the SI second, defined as exactly "the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium-133 atom" (at a temperature of 0 K and at mean sea level). The SI second is the basis of all atomic timescales, e.g. coordinated universal time, GPS time, International Atomic Time, etc.

## Current time standards

Geocentric Coordinate Time (TCG) is a coordinate time having its spatial origin at the center of Earth's mass. TCG is a theoretical ideal, and any particular realization will have measurement error.

International Atomic Time (TAI) is the primary physically realized time standard. TAI is produced by the International Bureau of Weights and Measures (BIPM), and is based on the combined input of many atomic clocks around the world, each corrected for environmental and relativistic effects (both gravitational and because of speed, like in GNSS). TAI is not related to TCG directly but rather is a realization of Terrestrial Time (TT), a theoretical timescale that is a rescaling of TCG such that the time rate approximately matches proper time at mean sea level.

Universal Time (UT1) is the Earth Rotation Angle (ERA) linearly scaled to match historical definitions of mean solar time at 0° longitude. At high precision, Earth's rotation is irregular and is determined from the positions of distant quasars using long baseline interferometry, laser ranging of the Moon and artificial satellites, as well as GPS satellite orbits.

Coordinated Universal Time (UTC) is an atomic time scale designed to approximate UT1. UTC differs from TAI by an integral number of seconds. UTC is kept within 0.9 second of UT1 by the introduction of one-second steps to UTC, the "leap second". To date these steps (and difference "TAI-UTC") have always been positive.

The Global Positioning System broadcasts a very precise time signal worldwide, along with instructions for converting GPS time (GPST) to UTC. It was defined with a constant offset from TAI: GPST = TAI - 19 s. The GPS time standard is maintained independently but regularly synchronized with or from, UTC time.

Standard time or civil time in a time zone deviates a fixed, round amount, usually a whole number of hours, from some form of Universal Time, usually UTC. The offset is chosen such that a new day starts approximately while the Sun is crossing the nadir meridian. Alternatively the difference is not really fixed, but it changes twice a year by a round amount, usually one hour, see Daylight saving time.

Julian day number is a count of days elapsed since Greenwich mean noon on 1 January 4713 B.C., Julian proleptic calendar. The Julian Date is the Julian day number followed by the fraction of the day elapsed since the preceding noon. Conveniently for astronomers, this avoids the date skip during an observation night. Modified Julian day (MJD) is defined as MJD = JD - 2400000.5. An MJD day thus begins at midnight, civil date. Julian dates can be expressed in UT1, TAI, TT, etc. and so for precise applications the timescale should be specified, e.g. MJD 49135.3824 TAI.

Barycentric Coordinate Time (TCB) is a coordinate time having its spatial origin at the center of mass of the Solar System, which is called the barycenter.

### Conversions

Conversions between atomic time systems (TAI, GPST, and UTC) are for the most part exact. However, GPS time is a measured value as opposed to a computed "paper" scale. As such it may differ from UTC(USNO) by a few hundred nanoseconds, which in turn may differ from official UTC by as much as 26 nanoseconds. Conversions for UT1 and TT rely on published difference tables which as of 2022 are specified to 10 microseconds and 0.1 nanoseconds respectively.

| System | Description | UT1 | UTC | TT | TAI | GPS |
|---|---|---|---|---|---|---|
| UT1 | Mean Solar Time | UT1 | UTC = UT1 − DUT1 | TT = UT1 − DUT1 + LS + 32.184 s + DTT | TAI = UT1 − DUT1 + LS | GPS = UT1 − DUT1 + LS − 19 s |
| UTC | Civil Time | UT1 = UTC + DUT1 | UTC | TT = UTC + LS + 32.184 s + DTT | TAI = UTC + LS | GPS = UTC + LS − 19 s |
| TT | Terrestrial Time | UT1 = TT − 32.184 s − DTT − LS + DUT1 | UTC = TT − 32.184 s − DTT − LS | TT | TAI = TT − 32.184 s − DTT | GPS = TT − 51.184 s − DTT |
| TAI | Atomic Time | UT1 = TAI − LS + DUT1 | UTC = TAI − LS | TT = TAI + 32.184 s + DTT | TAI | GPS = TAI − 19 s |
| GPS | GPS Time | UT1 = GPS + 19 s − LS + DUT1 | UTC = GPS + 19 s − LS | TT = GPS + 51.184 s + DTT | TAI = GPS + 19 s | GPS |

Definitions:

1. LS = TAI − UTC = leap seconds from USNO Table of Leap Seconds
2. DUT1 = UT1 − UTC published in IERS Bulletins or U.S. Naval Observatory EO
3. DTT = TT − TAI − 32.184 s published in BIPM's TT(BIPM) tables.

TCG is linearly related to TT as: TCG − TT = *LG* × (JD − 2443144.5) × 86400 seconds, with the scale difference *LG* defined as 6.969290134×10−10 exactly.

TCB is a linear transformation of TDB and TDB differs from TT in small, mostly periodic terms. Neglecting these terms (on the order of 2 milliseconds for several millennia around the present epoch), TCB is related to TT by: TCB − TT = *LB* × (JD − 2443144.5) × 86400 seconds. The scale difference *LB* has been defined by the IAU to be 1.550519768e-08 exactly.

## Time standards based on Earth rotation

Apparent solar time or true solar time is based on the solar day, which is the period between one solar noon (passage of the real Sun across the meridian) and the next. A solar day is approximately 24 hours of mean time. Because the Earth's orbit around the Sun is elliptical, and because of the obliquity of the Earth's axis relative to the plane of the orbit (the ecliptic), the apparent solar day varies a few dozen seconds above or below the mean value of 24 hours. As the variation accumulates over a few weeks, there are differences as large as 16 minutes between apparent solar time and mean solar time (see Equation of time). However, these variations cancel out over a year. There are also other perturbations such as Earth's wobble, but these are less than a second per year.

Sidereal time is time by the stars. A sidereal rotation is the time it takes the Earth to make one revolution with rotation to the stars, approximately 23 hours 56 minutes 4 seconds. A mean solar day is about 3 minutes 56 seconds longer than a mean sidereal day, or 1⁄366 more than a mean sidereal day. In astronomy, sidereal time is used to predict when a star will reach its highest point in the sky. For accurate astronomical work on land, it was usual to observe sidereal time rather than solar time to measure mean solar time, because the observations of 'fixed' stars could be measured and reduced more accurately than observations of the Sun (in spite of the need to make various small compensations, for refraction, aberration, precession, nutation and proper motion). It is well known that observations of the Sun pose substantial obstacles to the achievement of accuracy in measurement. In former times, before the distribution of accurate time signals, it was part of the routine work at any observatory to observe the sidereal times of meridian transit of selected 'clock stars' (of well-known position and movement), and to use these to correct observatory clocks running local mean sidereal time; but nowadays local sidereal time is usually generated by computer, based on time signals.

Mean solar time was a time standard used especially at sea for navigational purposes, calculated by observing apparent solar time and then adding to it a correction, the equation of time, which compensated for two known irregularities in the length of the day, caused by the ellipticity of the Earth's orbit and the obliquity of the Earth's equator and polar axis to the ecliptic (which is the plane of the Earth's orbit around the sun). It has been superseded by Universal Time.

Greenwich Mean Time was originally mean time deduced from meridian observations made at the Royal Greenwich Observatory (RGO). The principal meridian of that observatory was chosen in 1884 by the International Meridian Conference to be the Prime Meridian. GMT either by that name or as 'mean time at Greenwich' used to be an international time standard, but is no longer so; it was initially renamed in 1928 as Universal Time (UT) (partly as a result of ambiguities arising from the changed practice of starting the astronomical day at midnight instead of at noon, adopted as from 1 January 1925). UT1 is still in reality mean time at Greenwich. Today, GMT is a time zone but is still the legal time in the UK in winter (and as adjusted by one hour for summer time). But Coordinated Universal Time (UTC) (an atomic-based time scale which is always kept within 0.9 second of UT1) is in common actual use in the UK, and the name GMT is often used to refer to it. (See articles Greenwich Mean Time, Universal Time, Coordinated Universal Time and the sources they cite.)

Versions of Universal Time such as UT0 and UT2 have been defined but are no longer in use.

## Time standards for planetary motion calculations

Ephemeris time (ET) and its successor time scales described below have all been intended for astronomical use, e.g. in planetary motion calculations, with aims including uniformity, in particular, freedom from irregularities of Earth rotation. Some of these standards are examples of dynamical time scales and/or of coordinate time scales. Ephemeris Time was from 1952 to 1976 an official time scale standard of the International Astronomical Union; it was a dynamical time scale based on the orbital motion of the Earth around the Sun, from which the ephemeris second was derived as a defined fraction of the tropical year. This ephemeris second was the standard for the SI second from 1956 to 1967, and it was also the source for calibration of the caesium atomic clock; its length has been closely duplicated, to within 1 part in 1010, in the size of the current SI second referred to atomic time. This Ephemeris Time standard was non-relativistic and did not fulfil growing needs for relativistic coordinate time scales. It was in use for the official almanacs and planetary ephemerides from 1960 to 1983, and was replaced in official almanacs for 1984 and after, by numerically integrated Jet Propulsion Laboratory Development Ephemeris DE200 (based on the JPL relativistic coordinate time scale Teph).

For applications at the Earth's surface, ET's official replacement was Terrestrial Dynamical Time (TDT), which maintained continuity with it. TDT is a uniform atomic time scale, whose unit is the SI second. TDT is tied in its rate to the SI second, as is International Atomic Time (TAI), but because TAI was somewhat arbitrarily defined at its inception in 1958 to be initially equal to a refined version of UT, TDT was offset from TAI, by a constant 32.184 seconds. The offset provided a continuity from Ephemeris Time to TDT. TDT has since been redefined as Terrestrial Time (TT).

For the calculation of ephemerides, Barycentric Dynamical Time (TDB) was officially recommended to replace ET. TDB is similar to TDT but includes relativistic corrections that move the origin to the barycenter, hence it is a dynamical time at the barycenter. TDB differs from TT only in periodic terms. The difference is at most 2 milliseconds. Deficiencies were found in the definition of TDB (though not affecting Teph), and TDB has been replaced by Barycentric Coordinate Time (TCB) and Geocentric Coordinate Time (TCG), and redefined to be JPL ephemeris time argument Teph, a specific fixed linear transformation of TCB. As defined, TCB (as observed from the Earth's surface) is of divergent rate relative to all of ET, Teph and TDT/TT; and the same is true, to a lesser extent, of TCG. The ephemerides of Sun, Moon and planets in current widespread and official use continue to be those calculated at the Jet Propulsion Laboratory (updated as from 2003 to DE405) using as argument Teph.
