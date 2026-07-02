---
title: "Laser rangefinder"
source: https://en.wikipedia.org/wiki/Laser_rangefinder
domain: time-of-flight-sensors
license: CC-BY-SA-4.0
tags: time of flight, single-photon avalanche diode, laser rangefinder, rangefinder device
fetched: 2026-07-02
---

# Laser rangefinder

A **laser rangefinder**, also known as a **laser telemeter** or **laser distance meter**, is a rangefinder that uses a laser beam to determine the distance to an object. The most common form of laser rangefinder operates on the time of flight principle by sending a laser pulse in a narrow beam towards the object and measuring the time taken by the pulse to be reflected off the target and returned to the sender. Due to the high speed of light, this technique is not appropriate for high precision sub-millimeter measurements, where triangulation and other techniques are often used instead. Laser rangefinders are sometimes classified as type of handheld scannerless lidar.

## Pulse

The pulse may be coded to reduce the chance that the rangefinder can be jammed. It is possible to use Doppler effect techniques to judge whether the object is moving towards or away from the rangefinder, and if so, how fast.

## Precision

The precision of an instrument is correlated with the rise time, divergence, and power of its laser pulse, as well as the quality of its optics and onboard digital signal processing. Environmental factors can significantly reduce range and accuracy:

- Humidity, snow, dust, or other airborne particulates will diffuse the signal.
- Higher temperature and higher pressure (lower elevation) slightly decrease the speed of light through air.
- Smaller and less reflective targets return less information.

In good conditions, skilled operators using precision laser rangefinders can range a target to within a meter at distances on the order of three kilometers.

## Range and range error

Despite the beam being narrow, it will eventually spread over long distances due to the divergence of the laser beam, as well as due to scintillation and beam wander effects, caused by the presence of water droplets in the air acting as lenses ranging in size from microscopic to roughly half the height of the laser beam's path above the earth.

These atmospheric distortions coupled with the divergence of the laser itself and with transverse winds that serve to push the atmospheric heat bubbles laterally may combine to make it difficult to get an accurate reading of the distance of an object, say, beneath some trees or behind bushes, or even over long distances of more than 1 km in open and unobscured desert terrain.

Some of the laser light might reflect off leaves or branches which are closer than the object, giving an early return and a reading which is too low. Alternatively, over distances longer than 360 m, if the target is in proximity to the earth, it may simply vanish into a mirage, caused by temperature gradients in the air in proximity to the heated surface bending the laser light. All these effects must be considered.

## Calculation

The distance between point A and B is given by

$D={\frac {ct}{2}}$

where *c* is the speed of light and *t* is the amount of time for the round-trip between A and B.

$t={\frac {\phi }{\omega }}$

where *φ* is the phase delay made by the light traveling and *ω* is the angular frequency of optical wave.

Then substituting the values in the equation,

$D={\frac {1}{2}}ct={\frac {1}{2}}{\frac {c\phi }{\omega }}={\frac {c}{4\pi f}}(N\pi +\Delta \phi )={\frac {\lambda }{4}}(N+\Delta N)$

In this equation, *λ* is the wavelength ⁠*c*/*f*⁠; *Δφ* is the part of the phase delay that does not fulfill π (that is, *φ* modulo π); *N* is the integer number of wave half-cycles of the round-trip and Δ*N* the remaining fractional part.

## Technologies

**Time of flight** - this measures the time taken for a light pulse to travel to the target and back. With the speed of light known, and an accurate measurement of the time taken, the distance can be calculated. Many pulses are fired sequentially and the average response is most commonly used. This technique requires very accurate sub-nanosecond timing circuitry.

**Multiple frequency phase-shift** - this measures the phase shift of multiple frequencies on reflection then solves some simultaneous equations to give a final measure.

**Interferometry** - the most accurate and most useful technique for measuring changes in distance rather than absolute distances.

**Light attenuation by atmospheric absorption** - The method measures the attenuation of a laser beam caused by the absorption from an atmospheric compound (H2O, CO2, CH4, O2 etc.) to calculate the distance to an object. The light atmospheric absorption attenuation method requires unmodulated incoherent light sources and low-frequency electronics that reduce the complexity of the devices. Due to this, low-cost light sources can be used for range-finding. However, the application of the method is limited to atmospheric measurements or planetary exploration.

## Applications

### Military

Rangefinders provide an precise distance to targets located beyond the distance of point-blank shooting to snipers and artillery. They can also be used for military reconnaissance and engineering. Tanks usually use LRF to correct the direct shoot solution.

Handheld military rangefinders operate at ranges of 2 km up to 25 km and are combined with binoculars or monoculars. When the rangefinder is equipped with a digital magnetic compass (DMC) and inclinometer it is capable of providing magnetic azimuth, inclination, and height (length) of targets. Some rangefinders can also measure a target's speed in relation to the observer. Some rangefinders have cable or wireless interfaces to enable them to transfer their measurement(s) data to other equipment like fire control computers. Some models also offer the possibility to use add-on night vision modules. Most handheld rangefinders as of this date used standard or rechargeable batteries.

The more powerful models of rangefinders measure distance up to 40 km and are normally installed either on a tripod or directly on a vehicle, ship, jet, helicopter or gun platform. In the latter case the rangefinder module is integrated with on-board thermal, night vision and daytime observation equipment. The most advanced military rangefinders can be integrated with computers.

To make laser rangefinders and laser-guided weapons less useful against military targets, various military arms may have developed laser-absorbing paint for their vehicles; regardless, some objects do not reflect laser light very well, and using a laser rangefinder on them is difficult.

The first commercial laser rangefinder was the Barr & Stroud LF1, developed in association with Hughes Aircraft, which became available in 1965. This was then followed by the Barr & Stroud LF2, which integrated the rangefinder into a tank sight, and this was used on the Chieftain tank in 1969, the first vehicle so-equipped with such a system. Both systems used ruby lasers.

### 3D modelling

Laser rangefinders are used extensively in 3D object recognition, 3D object modelling, and a wide variety of computer vision-related fields. This technology constitutes the heart of the so-called *time-of-flight* 3D scanners. In contrast to the military instruments, laser rangefinders offer high-precision scanning abilities, with either single-face or 360-degree scanning modes.

A number of algorithms have been developed to merge the range data retrieved from multiple angles of a single object to produce complete 3D models with as little error as possible. One of the advantages offered by laser rangefinders over other methods of computer vision is in not needing to correlate features from two images in order to determine depth-information like stereoscopic methods do.

Laser rangefinders used in computer vision applications often have depth resolutions of 0.1 mm or less. This can be achieved by using triangulation or refraction measurement techniques unlike to the time of flight techniques used in LIDAR.

### Forestry

Special laser rangefinders are used in forestry. These devices have anti-leaf filters and work with reflectors. Laser beam reflects only from this reflector and so exact distance measurement is guaranteed. Laser rangefinders with anti-leaf filter are used for example for forest inventories.

### Sports

Laser rangefinders may be effectively used in various sports that require precision distance measurement, such as golf, hunting, and archery. Some of the more popular manufacturers are Caddytalk, Opti-logic Corporation, Bushnell, Leupold, LaserTechnology, Trimble, Leica, Newcon Optik, Op. Electronics, Nikon, Swarovski Optik and Zeiss. Many rangefinders from Bushnell come with advanced features, such as ARC (angle range compensation), multi-distance ability, slope, JOLT (Vibrate when the target is locked), and Pin-Seeking. ARC can be calculated by hand using the rifleman's rule, but it's usually much easier if you let a rangefinder do it when you are out hunting. In golfing where time is most important, a laser rangefinder comes useful in locating distance to the flag. However not all features are 100% legal for golf tournament play. Many hunters in the eastern U.S. don't need a rangefinder, although many western hunters need them, due to longer shooting distances and more open spaces.

### Industrial production processes

An important application is the use of laser rangefinder technology during the automation of stock management systems and production processes in steel industry.

### Laser measuring tools

Laser rangefinders are also used in several industries like construction, renovation and real estate as alternatives to tape measures, and was first introduced by Leica Geosystems in 1993 in France. To measure a large object like a room with a tape measure, one would need another person to hold the tape at the far wall and a clear line straight across the room to stretch the tape. With a laser measuring tool, the job can be completed by one operator with just a line of sight. Although tape measures are technically perfectly accurate, laser measuring tools are much more precise. Laser measuring tools typically include the ability to produce some simple calculations, such as the area or volume of a room. These devices can be found in hardware stores and online marketplaces.

## Price

Laser rangefinders can vary in price, depending on the quality and application of the product. Military grade rangefinders need to be as accurate as possible and must also reach great distances. These devices can cost hundreds of thousands of dollars. For civilian applications, such as hunting or golf, devices are more affordable and much more readily accessible.

## Safety

Laser rangefinders are divided into four classes and several subclasses. Laser rangefinders available to consumers are usually laser class 1 or class 2 devices and are considered relatively eye-safe. Regardless of the safety rating, direct eye contact should always be avoided. Most laser rangefinders for military use exceed the laser class 2 energy levels.
