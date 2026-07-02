---
title: "Ring laser gyroscope"
source: https://en.wikipedia.org/wiki/Ring_laser_gyroscope
domain: gyroscope-mems
license: CC-BY-SA-4.0
tags: gyroscope sensor, vibrating structure gyroscope, coriolis force, ring laser gyroscope
fetched: 2026-07-02
---

# Ring laser gyroscope

A **ring laser gyroscope** (**RLG**) consists of a ring laser having two independent counter-propagating resonant modes over the same path; the difference in phase is used to detect rotation. It operates on the principle of the Sagnac effect which shifts the nulls of the internal standing wave pattern in response to angular rotation. Interference between the counter-propagating beams, observed externally, results in motion of the standing wave pattern, and thus indicates rotation.

## Description

The first experimental ring laser gyroscope was demonstrated in the US by Macek and Davis in 1963. Various organizations worldwide subsequently developed ring-laser technology further. Many tens of thousands of RLGs are operating in inertial navigation systems and have established high accuracy, with better than 0.01°/hour bias uncertainty, and mean time between failures in excess of 60,000 hours.

Ring laser gyroscopes can be used as the stable elements (for one degree of freedom each) in an inertial reference system. One key advantage of the RLG is that there are no moving parts apart from the dither motor assembly (see further description below). Compared to the conventional spinning gyroscope, this means there is no friction, which eliminates a significant source of drift. Additionally, the entire unit is compact, lightweight and highly durable, making it suitable for use in mobile systems such as aircraft, missiles, and satellites. Unlike a mechanical gyroscope, the device does not resist changes to its orientation.

Contemporary applications of the ring laser gyroscope include an embedded GPS capability to further enhance accuracy of RLG inertial navigation systems on military aircraft, commercial airliners, ships, and spacecraft. These hybrid INS/GPS units have replaced their mechanical counterparts in most applications.

"Ring laser gyroscopes (RLG) have demonstrated to currently be the most sensitive device for testing rotational motion with respect to an inertial frame." The lower noise limit of an active ring laser have been recently measured at the Gran Sasso National Laboratory of INFN (Italy) on the GINGERINO prototype. The measured noise level is below the calculated shot noise for a RLG where the counterpopagating beams are considered two coherent totally independent modes. Actually this discrepancy is supposed to be related to cross-coupling among the two modes.

## Principle of operation

According to the Sagnac effect, rotation induces a small difference between the time it takes light to traverse the ring in the two directions. This introduces a tiny separation between the frequencies of the counter-propagating beams, a motion of the standing wave pattern within the ring, and thus a beat pattern when those two beams interfere outside the ring. Therefore, the net shift of that interference pattern follows the rotation of the unit in the plane of the ring.

RLGs, while more accurate than mechanical gyroscopes, suffer from an effect known as "lock-in" at very slow rotation rates. When the ring laser is hardly rotating, the frequencies of the counter-propagating laser modes become almost identical. In this case, crosstalk between the counter-propagating beams can allow for injection locking, so that the standing wave "gets stuck" in a preferred phase, thus locking the frequency of each beam to that of the other, rather than responding to gradual rotation.

Forced dithering can largely overcome this problem. The ring laser cavity is rotated clockwise and anti-clockwise about its axis using a mechanical spring driven at its resonance frequency. This ensures that the angular velocity of the system is usually far from the lock-in threshold. Typical rates are 400 Hz, with a peak dither velocity on the order of 1 degree per second. Dither does not fix the lock-in problem completely, as each time the direction of rotation is reversed, a short time interval exists in which the rotation rate is near zero and lock-in briefly can occur. If a pure frequency oscillation is maintained, these small lock-in intervals can accumulate. This was remedied by introducing noise to the 400 Hz vibration.

A different approach to avoiding lock-in is embodied in the Multioscillator Ring Laser Gyroscope, wherein what is effectively two independent ring lasers (each having two counterpropagating beams) of opposite circular polarization coexist in the same ring resonator. The resonator incorporates polarization rotation (via a nonplanar geometry) which splits the fourfold-degenerate cavity mode (two directions, two polarizations each) into right- and left-circular-polarized modes separated by many hundreds of MHz, each having two counterpropagating beams. Nonreciprocal bias via the Faraday effect, either in a special thin Faraday rotator, or via a longitudinal magnetic field on the gain medium, then further splits each circular polarization by typically a few hundred kHz, thus causing each ring laser to have a static output beat frequency of hundreds of kHz. One frequency increases and one decreases, when inertial rotation is present; the two frequencies are measured and then digitally subtracted to finally yield the net Sagnac-effect frequency splitting and thus determine the rotation rate. The Faraday bias frequency is chosen to be higher than any anticipated rotation-induced frequency difference, so the two counterpropagating waves have no opportunity to lock-in.

Manufacturers of RLG-based navigation systems (generally called "Inertial Measurement Units" or "Inertial Reference Units" (the terms being interchangeable) include Honeywell, Sperry, Kearfott, Litton, and others. Honeywell is probably the most well known with several versions having various levels of performance for applications ranging from missiles to commercial and military aircraft. The GG1320 shown above is typical of the latter with each axis in a separate block. Kearfott's KI-4921 implements all three axes in a single monolithic block with performance similar to that of the GG1320 but is much more compact and has fewer parts. The KI-4921 (shown above) is used for applications in sea navigation like submarines. Its monolithic RLG block would fit comfortably inside a baseball. There is also a higher performance KI-4902 which is similar in design but roughly 50 percent larger.

## Fibre optic gyroscope

A related device is the fibre optic gyroscope which also operates on the basis of the Sagnac effect, but in which the ring is not a part of the laser. Rather, an external laser injects counter-propagating beams into an optical fiber ring, where rotation causes a relative phase shift between those beams when interfered after their pass through the fiber ring. The phase shift is proportional to the rate of rotation. This is less sensitive in a single traverse of the ring than the RLG, in which the externally observed phase shift is proportional to the accumulated rotation itself, not its derivative. However, the sensitivity of the fiber optic gyro is enhanced by having a long optical fiber, coiled for compactness, in which the Sagnac effect is multiplied according to the number of turns.

## Example applications

- Airbus A320
- Agni III and Agni-IV
- Agni-V
- ASM-135 US Anti-satellite missile
- Boeing 757-200
- Boeing 777
- B-52H with the AMI upgrade
- EF-111 Raven
- F-15E Strike Eagle
- F-16 Fighting Falcon
- HAL Tejas
- MC-130E Combat Talon I and MC-130H Combat Talon II
- MQ-1C Warrior
- MK39 Ship's Internal Navigation System used in NATO surface ships and submarines
- P3 Orion (with upgrade)
- Shaurya missile.
- MH-60R, MH-60S, SH60F and SH60B Seahawk helicopters
- Sukhoi Su-30MKI
- Trident I and Trident II Missiles
- PARALIGN, used for roller alignment
- International Space Station
- JF-17 Thunder
