---
title: "Radar (part 2/2)"
source: https://en.wikipedia.org/wiki/Radar
domain: radar-systems
license: CC-BY-SA-4.0
tags: radar systems, pulse-doppler radar, synthetic-aperture radar, phased array
fetched: 2026-07-02
part: 2/2
---

## Signal processing

### Distance measurement

#### Transit time

One way to obtain a distance measurement (ranging) is based on the time-of-flight: transmit a short pulse of radio signal (electromagnetic radiation) and measure the time it takes for the reflection to return. The distance is one-half the round trip time multiplied by the speed of the signal. The factor of one-half comes from the fact that the signal has to travel to the object and back again. Since radio waves travel at the speed of light, accurate distance measurement requires high-speed electronics. In most cases, the receiver does not detect the return while the signal is being transmitted. Through the use of a duplexer, the radar switches between transmitting and receiving at a predetermined rate. A similar effect imposes a maximum range as well. In order to maximize range, longer times between pulses should be used, referred to as a pulse repetition time, or its reciprocal, pulse repetition frequency.

These two effects tend to be at odds with each other, and it is not easy to combine both good short range and good long range in a single radar. This is because the short pulses needed for a good minimum range broadcast have less total energy, making the returns much smaller and the target harder to detect. This could be offset by using more pulses, but this would shorten the maximum range. So each radar uses a particular type of signal. Long-range radars tend to use long pulses with long delays between them, and short range radars use smaller pulses with less time between them. As electronics have improved many radars now can change their pulse repetition frequency, thereby changing their range. The newest radars fire two pulses during one cell, one for short range (about 10 km (6.2 miles)) and a separate signal for longer ranges (about 100 km (62 miles)).

Distance may also be measured as a function of time. The **radar mile** is the time it takes for a radar pulse to travel one nautical mile, reflect off a target, and return to the radar antenna. Since a nautical mile is defined as 1,852 m, then dividing this distance by the speed of light (299,792,458 m/s), and then multiplying the result by 2 yields a result of 12.36 μs in duration.

#### Frequency modulation

Another form of distance measuring radar is based on frequency modulation. In these systems, the frequency of the transmitted signal is changed over time. Since the signal takes a finite time to travel to and from the target, the received signal is a different frequency than what the transmitter is broadcasting at the time the reflected signal arrives back at the radar. By comparing the frequency of the two signals the difference can be easily measured. This is easily accomplished with very high accuracy even in 1940s electronics. A further advantage is that the radar can operate effectively at relatively low frequencies. This was important in the early development of this type when high-frequency signal generation was difficult or expensive.

This technique can be used in continuous wave radar and is often found in aircraft radar altimeters. In these systems a "carrier" radar signal is frequency modulated in a predictable way, typically varying up and down with a sine wave or sawtooth pattern at audio frequencies. The signal is then sent out from one antenna and received on another, typically located on the bottom of the aircraft, and the signal can be continuously compared using a simple *beat frequency* modulator that produces an audio frequency tone from the returned signal and a portion of the transmitted signal.

The modulation index riding on the receive signal is proportional to the time delay between the radar and the reflector. The frequency shift becomes greater with greater time delay. The frequency shift is directly proportional to the distance travelled. That distance can be displayed on an instrument, and it may also be available via the transponder. This signal processing is similar to that used in speed detecting Doppler radar. Example systems using this approach are AZUSA, MISTRAM, and UDOP.

Terrestrial radar uses low-power FM signals that cover a larger frequency range. The multiple reflections are analyzed mathematically for pattern changes with multiple passes creating a computerized synthetic image. Doppler effects are used which allows slow moving objects to be detected as well as largely eliminating "noise" from the surfaces of bodies of water.

#### Pulse compression

The two techniques outlined above both have their disadvantages. The pulse timing technique has an inherent tradeoff in that the accuracy of the distance measurement is inversely related to the length of the pulse, while the energy, and thus direction range, is directly related. Increasing power for longer range while maintaining accuracy demands extremely high peak power, with 1960s early warning radars often operating in the tens of megawatts. The continuous wave methods spread this energy out in time and thus require much lower peak power compared to pulse techniques, but requires some method of allowing the sent and received signals to operate at the same time, often demanding two separate antennas.

The introduction of new electronics in the 1960s allowed the two techniques to be combined. It starts with a longer pulse that is also frequency modulated. Spreading the broadcast energy out in time means lower peak energies can be used, with modern examples typically on the order of tens of kilowatts. On reception, the signal is sent into a system that delays different frequencies by different times. The resulting output is a much shorter pulse that is suitable for accurate distance measurement, while also compressing the received energy into a much higher energy peak and thus improving the signal-to-noise ratio. The technique is largely universal on modern large radars.

### Speed measurement

Speed is the change in distance to an object with respect to time. Thus the existing system for measuring distance, combined with a memory capacity to see where the target last was, is enough to measure speed. At one time the memory consisted of a user making grease pencil marks on the radar screen and then calculating the speed using a slide rule. Modern radar systems perform the equivalent operation faster and more accurately using computers.

If the transmitter's output is coherent (phase synchronized), there is another effect that can be used to make almost instant speed measurements (no memory is required), known as the Doppler effect. Most modern radar systems use this principle into Doppler radar and pulse-Doppler radar systems (weather radar, military radar). The Doppler effect is only able to determine the relative speed of the target along the line of sight from the radar to the target. Any component of target velocity perpendicular to the line of sight cannot be determined by using the Doppler effect alone, but it can be determined by tracking the target's azimuth over time.

It is possible to make a Doppler radar without any pulsing, known as a continuous-wave radar (CW radar), by sending out a very pure signal of a known frequency. CW radar is ideal for determining the radial component of a target's velocity. CW radar is typically used by traffic enforcement to measure vehicle speed quickly and accurately where the range is not important.

When using a pulsed radar, the variation between the phase of successive returns gives the distance the target has moved between pulses, and thus its speed can be calculated. Other mathematical developments in radar signal processing include time-frequency analysis (Weyl Heisenberg or wavelet), as well as the chirplet transform which makes use of the change of frequency of returns from moving targets ("chirp").

### Pulse-Doppler signal processing

Pulse-Doppler signal processing includes frequency filtering in the detection process. The space between each transmit pulse is divided into range cells or range gates. Each cell is filtered independently much like the process used by a spectrum analyzer to produce the display showing different frequencies. Each different distance produces a different spectrum. These spectra are used to perform the detection process. This is required to achieve acceptable performance in hostile environments involving weather, terrain, and electronic countermeasures.

The primary purpose is to measure both the amplitude and frequency of the aggregate reflected signal from multiple distances. This is used with weather radar to measure radial wind velocity and precipitation rate in each different volume of air. This is linked with computing systems to produce a real-time electronic weather map. Aircraft safety depends upon continuous access to accurate weather radar information that is used to prevent injuries and accidents. Weather radar uses a low PRF. Coherency requirements are not as strict as those for military systems because individual signals ordinarily do not need to be separated. Less sophisticated filtering is required, and range ambiguity processing is not normally needed with weather radar in comparison with military radar intended to track air vehicles.

The alternate purpose is "look-down/shoot-down" capability required to improve military air combat survivability. Pulse-Doppler is also used for ground based surveillance radar required to defend personnel and vehicles. Pulse-doppler signal processing increases the maximum detection distance using less radiation close to aircraft pilots, shipboard personnel, infantry, and artillery. Reflections from terrain, water, and weather produce signals much larger than aircraft and missiles, which allows fast moving vehicles to hide using nap-of-the-earth flying techniques and stealth technology to avoid detection until an attack vehicle is too close to destroy. Pulse-Doppler signal processing incorporates more sophisticated electronic filtering that safely eliminates this kind of weakness. This requires the use of medium pulse-repetition frequency with phase coherent hardware that has a large dynamic range. Military applications require medium PRF which prevents range from being determined directly, and range ambiguity resolution processing is required to identify the true range of all reflected signals. Radial movement is usually linked with Doppler frequency to produce a lock signal that cannot be produced by radar jamming signals. Pulse-Doppler signal processing also produces audible signals that can be used for threat identification.

### Reduction of interference effects

Signal processing is employed in radar systems to reduce the radar interference effects. Signal processing techniques include moving target indication, Pulse-Doppler signal processing, moving target detection processors, correlation with secondary surveillance radar targets, space-time adaptive processing, and track-before-detect. Constant false alarm rate and digital terrain model processing are also used in clutter environments.

### Plot and track extraction

A track algorithm is a radar performance enhancement strategy. Tracking algorithms provide the ability to predict the future position of multiple moving objects based on the history of the individual positions being reported by sensor systems.

Historical information is accumulated and used to predict future position for use with air traffic control, threat estimation, combat system doctrine, gun aiming, and missile guidance. Position data is accumulated by radar sensors over the span of a few minutes.

There are four common track algorithms:

- Nearest neighbour algorithm
- Probabilistic Data Association
- Multiple Hypothesis Tracking
- Interactive Multiple Model (IMM)

Radar video returns from aircraft can be subjected to a plot extraction process whereby spurious and interfering signals are discarded. A sequence of target returns can be monitored through a device known as a plot extractor.

The non-relevant real time returns can be removed from the displayed information and a single plot displayed. In some radar systems, or alternatively in the command and control system to which the radar is connected, a radar tracker is used to associate the sequence of plots belonging to individual targets and estimate the targets' headings and speeds.


## Engineering

A radar's components are:

- A transmitter that generates the radio signal with an oscillator such as a klystron or a magnetron and controls its duration by a modulator.
- A waveguide that links the transmitter and the antenna.
- A duplexer that serves as a switch between the antenna and the transmitter or the receiver for the signal when the antenna is used in both situations.
- A receiver. Knowing the shape of the desired received signal (a pulse), an optimal receiver can be designed using a matched filter.
- A display processor to produce signals for human readable output devices.
- An electronic section that controls all those devices and the antenna to perform the radar scan ordered by software.
- A link to end user devices and displays.

### Antenna design

Radio signals broadcast from a single antenna will spread out in all directions, and likewise a single antenna will receive signals equally from all directions. This leaves the radar with the problem of deciding where the target object is located.

Early systems tended to use omnidirectional broadcast antennas, with directional receiver antennas which were pointed in various directions. For instance, the first system to be deployed, Chain Home, used two straight antennas at right angles for reception, each on a different display. The maximum return would be detected with an antenna at right angles to the target, and a minimum with the antenna pointed directly at it (end on). The operator could determine the direction to a target by rotating the antenna so one display showed a maximum while the other showed a minimum. One serious limitation with this type of solution is that the broadcast is sent out in all directions, so the amount of energy in the direction being examined is a small part of that transmitted. To get a reasonable amount of power on the "target", the transmitting aerial should also be directional.

#### Parabolic reflector

More modern systems use a steerable parabolic "dish" to create a tight broadcast beam, typically using the same dish as the receiver. Such systems often combine two radar frequencies in the same antenna in order to allow automatic steering, or *radar lock*.

Parabolic reflectors can be either symmetric parabolas or spoiled parabolas: Symmetric parabolic antennas produce a narrow "pencil" beam in both the X and Y dimensions and consequently have a higher gain. The NEXRAD Pulse-Doppler weather radar uses a symmetric antenna to perform detailed volumetric scans of the atmosphere. Spoiled parabolic antennas produce a narrow beam in one dimension and a relatively wide beam in the other. This feature is useful if target detection over a wide range of angles is more important than target location in three dimensions. Most 2D surveillance radars use a spoiled parabolic antenna with a narrow azimuthal beamwidth and wide vertical beamwidth. This beam configuration allows the radar operator to detect an aircraft at a specific azimuth but at an indeterminate height. Conversely, so-called "nodder" height finding radars use a dish with a narrow vertical beamwidth and wide azimuthal beamwidth to detect an aircraft at a specific height but with low azimuthal precision.

#### Types of scan

- Primary Scan: A scanning technique where the main antenna aerial is moved to produce a scanning beam, examples include circular scan, sector scan, etc.
- Secondary Scan: A scanning technique where the antenna feed is moved to produce a scanning beam, examples include conical scan, unidirectional sector scan, lobe switching, etc.
- Palmer Scan: A scanning technique that produces a scanning beam by moving the main antenna and its feed. A Palmer Scan is a combination of a Primary Scan and a Secondary Scan.
- Conical scanning: The radar beam is rotated in a small circle around the "boresight" axis, which is pointed at the target.

#### Slotted waveguide

Applied similarly to the parabolic reflector, the slotted waveguide is moved mechanically to scan and is particularly suitable for non-tracking surface scan systems, where the vertical pattern may remain constant. Owing to its lower cost and less wind exposure, shipboard, airport surface, and harbour surveillance radars now use this approach in preference to a parabolic antenna.

#### Phased array

Another method of steering is used in a phased array radar.

Phased array antennas are composed of evenly spaced similar antenna elements, such as aerials or rows of slotted waveguide. Each antenna element or group of antenna elements incorporates a discrete phase shift that produces a phase gradient across the array. For example, array elements producing a 5 degree phase shift for each wavelength across the array face will produce a beam pointed 5 degrees away from the centerline perpendicular to the array face. Signals travelling along that beam will be reinforced. Signals offset from that beam will be cancelled. The amount of reinforcement is antenna gain. The amount of cancellation is side-lobe suppression.

Phased array radars have been in use since the earliest years of radar in World War II (Mammut radar), but electronic device limitations led to poor performance. Phased array radars were originally used for missile defence (see for example Safeguard Program). They are the heart of the ship-borne Aegis Combat System and the Patriot Missile System. The massive redundancy associated with having a large number of array elements increases reliability at the expense of gradual performance degradation that occurs as individual phase elements fail. To a lesser extent, phased array radars have been used in weather surveillance. As of 2017, NOAA plans to implement a national network of multi-function phased array radars throughout the United States within 10 years, for meteorological studies and flight monitoring.

Phased array antennas can be built to conform to specific shapes, like missiles, infantry support vehicles, ships, and aircraft.

As the price of electronics has fallen, phased array radars have become more common. Almost all modern military radar systems are based on phased arrays, where the small additional cost is offset by the improved reliability of a system with no moving parts. Traditional moving-antenna designs are still widely used in roles where cost is a significant factor such as air traffic surveillance and similar systems.

Phased array radars are valued for use in aircraft since they can track multiple targets. The first aircraft to use a phased array radar was the B-1B Lancer. The first fighter aircraft to use phased array radar was the Mikoyan MiG-31. The MiG-31M's SBI-16 Zaslon passive electronically scanned array radar was considered to be the world's most powerful fighter radar, until the AN/APG-77 active electronically scanned array was introduced on the Lockheed Martin F-22 Raptor.

Phased-array interferometry or aperture synthesis techniques, using an array of separate dishes that are phased into a single effective aperture, are not typical for radar applications, although they are widely used in radio astronomy. Because of the thinned array curse, such multiple aperture arrays, when used in transmitters, result in narrow beams at the expense of reducing the total power transmitted to the target. In principle, such techniques could increase spatial resolution, but the lower power means that this is generally not effective.

Aperture synthesis by post-processing motion data from a single moving source, on the other hand, is widely used in space and airborne radar systems.

### Frequency bands

Antennas generally have to be sized similar to the wavelength of the operational frequency, normally within an order of magnitude. This provides a strong incentive to use shorter wavelengths as this will result in smaller antennas. Shorter wavelengths also result in higher resolution due to diffraction, meaning the shaped reflector seen on most radars can also be made smaller for any desired beamwidth.

Opposing the move to smaller wavelengths are a number of practical issues. For one, the electronics needed to produce high power very short wavelengths were generally more complex and expensive than the electronics needed for longer wavelengths or did not exist at all. Another issue is that the radar equation's effective aperture figure means that for any given antenna (or reflector) size will be more efficient at longer wavelengths. Additionally, shorter wavelengths may interact with molecules or raindrops in the air, scattering the signal. Very long wavelengths also have additional diffraction effects that make them suitable for over the horizon radars. For this reason, a wide variety of wavelengths are used in different roles.

The traditional band names originated as code-names during World War II and are still in military and aviation use throughout the world. They have been adopted in the United States by the Institute of Electrical and Electronics Engineers and internationally by the International Telecommunication Union. Most countries have additional regulations to control which parts of each band are available for civilian or military use.

Other users of the radio spectrum, such as the broadcasting and electronic countermeasures industries, have replaced the traditional military designations with their own systems.

| Band name | Frequency range | Wavelength range | Notes |
|---|---|---|---|
| HF | 3–30 MHz | 10–100 m | Coastal radar systems, over-the-horizon (OTH) radars; 'high frequency' |
| VHF | 30–300 MHz | 1–10 m | Very long range, ground penetrating; 'very high frequency'. Early radar systems generally operated in VHF as suitable electronics had already been developed for broadcast radio. Today this band is heavily congested and no longer suitable for radar due to interference. |
| P | < 300 MHz | > 1 m | 'P' for 'previous', applied retrospectively to early radar systems; essentially HF + VHF. Often used for remote sensing because of good vegetation penetration. |
| UHF | 300–1000 MHz | 0.3–1 m | Very long range (e.g. ballistic missile early warning), ground penetrating, foliage penetrating; 'ultra high frequency'. Efficiently produced and received at very high energy levels, and also reduces the effects of nuclear blackout, making them useful in the missile detection role. |
| L | 1–2 GHz | 15–30 cm | Long range air traffic control and surveillance; 'L' for 'long'. Widely used for long range early warning radars as they combine good reception qualities with reasonable resolution. |
| S | 2–4 GHz | 7.5–15 cm | Moderate range surveillance, Terminal air traffic control, long-range weather, marine radar; 'S' for 'sentimetric', its code-name during WWII. Less efficient than L, but offering higher resolution, making them especially suitable for long-range ground controlled interception tasks. |
| C | 4–8 GHz | 3.75–7.5 cm | Satellite transponders; a compromise (hence 'C') between X and S bands; weather; long range tracking |
| X | 8–12 GHz | 2.5–3.75 cm | Missile guidance, marine radar, weather, medium-resolution mapping and ground surveillance; in the United States the narrow range 10.525 GHz ±25 MHz is used for airport radar; short-range tracking. Named X band because the frequency was a secret during WW2. Diffraction off raindrops during heavy rain limits the range in the detection role and makes this suitable only for short-range roles or those that deliberately detect rain. |
| Ku | 12–18 GHz | 1.67–2.5 cm | High-resolution, also used for satellite transponders, frequency under K band (hence 'u') |
| K | 18–24 GHz | 1.11–1.67 cm | From German *kurz*, meaning 'short'. Limited use due to absorption by water vapor at 22 GHz, so Ku and Ka on either side used instead for surveillance. K-band is used for detecting clouds by meteorologists, and by police for detecting speeding motorists. K-band operates at 24.150 ± 0.100 GHz. |
| Ka | 24–40 GHz | 0.75–1.11 cm | Mapping, short range, airport surveillance; frequency just above K band (hence 'a') Photo radar, used to trigger cameras which take pictures of license plates of cars running red lights, and by police for detecting speeding motorists. Operates at 34.300 ± 0.100 GHz. |
| mm | 40–300 GHz | 1.0–7.5 mm | Millimetre band, subdivided as below. Oxygen in the air is an extremely effective attenuator around 60 GHz, as are other molecules at other frequencies, leading to the so-called propagation window at 94 GHz. Even in this window the attenuation is higher than that due to water at 22.2 GHz. This makes these frequencies generally useful only for short-range highly specific radars, like power line avoidance systems for helicopters or use in space where attenuation is not a problem. Multiple letters are assigned to these bands by different groups. These are from Baytron, a now defunct company that made test equipment. |
| V | 40–75 GHz | 4.0–7.5 mm | Very strongly absorbed by atmospheric oxygen, which resonates at 60 GHz. |
| W | 75–110 GHz | 2.7–4.0 mm | Used as a visual sensor for experimental autonomous vehicles, high-resolution meteorological observation, and imaging. |

### Modulators

Modulators act to provide the waveform of the RF-pulse. There are two different radar modulator designs:

- High voltage switch for non-coherent keyed power-oscillators. These modulators consist of a high voltage pulse generator formed from a high voltage supply, a pulse forming network, and a high voltage switch such as a thyratron. They generate short pulses of power to feed, e.g., the magnetron, a special type of vacuum tube that converts DC (usually pulsed) into microwaves. This technology is known as pulsed power. In this way, the transmitted pulse of RF radiation is kept to a defined and usually very short duration.
- Hybrid mixers, fed by a waveform generator and an exciter for a complex but coherent waveform. This waveform can be generated by low power/low-voltage input signals. In this case the radar transmitter must be a power-amplifier, e.g., a klystron or a solid state transmitter. In this way, the transmitted pulse is intrapulse-modulated and the radar receiver must use pulse compression techniques.

### Coolant

Coherent microwave amplifiers operating above 1,000 watts microwave output, like travelling wave tubes and klystrons, require liquid coolant. The electron beam must contain 5 to 10 times more power than the microwave output, which can produce enough heat to generate plasma. This plasma flows from the collector toward the cathode. The same magnetic focusing that guides the electron beam forces the plasma into the path of the electron beam but flowing in the opposite direction. This introduces FM modulation which degrades Doppler performance. To prevent this, liquid coolant with minimum pressure and flow rate is required, and deionized water is normally used in most high power surface radar systems that use Doppler processing.

Coolanol (silicate ester) was used in several military radars in the 1970s. However, it is hygroscopic, leading to hydrolysis and formation of highly flammable alcohol. The loss of a U.S. Navy aircraft in 1978 was attributed to a silicate ester fire. Coolanol is also expensive and toxic. The U.S. Navy has instituted a program named Pollution Prevention (P2) to eliminate or reduce the volume and toxicity of waste, air emissions, and effluent discharges. Because of this, Coolanol is used less often today.


## Regulations

*Radar* (also: *RADAR*) is defined by *article 1.100* of the International Telecommunication Union's (ITU) ITU Radio Regulations (RR) as:

> A radiodetermination system based on the comparison of reference signals with radio signals reflected, or retransmitted, from the position to be determined. Each *radiodetermination system* shall be classified by the *radiocommunication service* in which it operates permanently or temporarily. Typical radar utilizations are primary radar and secondary radar, these might operate in the radiolocation service or the radiolocation-satellite service.


## Configurations

Radar come in a variety of configurations in the emitter, the receiver, the antenna, wavelength, scan strategies, etc.

- Bistatic radar
- Continuous-wave radar
- Doppler radar
- Fm-cw radar
- Monopulse radar
- Passive radar
- Planar array radar
- Pulse-doppler
- Synthetic-aperture radar
  - Synthetically thinned aperture radar
- Over-the-horizon radar with chirp transmitter
