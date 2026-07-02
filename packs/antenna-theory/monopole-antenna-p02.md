---
title: "Monopole antenna (part 2/2)"
source: https://en.wikipedia.org/wiki/Monopole_antenna
domain: antenna-theory
license: CC-BY-SA-4.0
tags: dipole antenna, radiation pattern, antenna aperture, monopole antenna
fetched: 2026-07-02
part: 2/2
---

## Radiation pattern

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
| Three dimensional *(top)* and two dimensional vertical *(bottom)* radiation patterns of monopole antennas of different lengths over a perfect infinite ground plane, with length h given in wavelengths. The distance of the graph from the origin in any direction is proportional to the magnitude of the electric field of the radio wave radiated in that direction. The bottom graphs are a vertical section through the axis of the top 3 dimensional pattern. The circumference is labeled in degrees above the horizon. The graphs for different wavelengths do not have the same scale. Due to the lobes directed into the sky, monopoles longer than 0.625 wavelengths are almost never used as antennas. |   |   |   |   |   |   |

Like a vertical dipole antenna, a monopole has an omnidirectional radiation pattern: it radiates equal power in all azimuthal directions perpendicular to the antenna axis. The radiated power varies with elevation angle, with the radiation dropping off to zero at the zenith on the antenna axis. It radiates vertically polarized radio waves, with the electric field parallel to the element.

A monopole can be visualized *(see diagram)* as being formed by replacing the bottom half of a vertical dipole antenna *(c)* with a conducting plane (ground plane) at right-angles to the remaining half. If the ground plane is large enough, the radio waves from the remaining upper half of the dipole *(a)* reflected from the ground plane will seem to come from an image antenna *(b)* forming the missing half of the dipole, which adds to the direct radiation to form a dipole radiation pattern. So the pattern of a monopole over a perfectly conducting, infinite ground plane is identical to the top half of a dipole pattern.

See the gallery of radiation patterns. Up to a length of a half-wavelength ( ${\lambda \over 2}$ ) the radiation pattern has a single donut-shaped lobe with maximum radiated power in horizontal directions, perpendicular to the antenna axis. As the length is increased above ${\lambda \over 4}$ the lobe flattens, radiating less power at high angles and more in horizontal directions.

Above a half-wavelength the pattern splits into a horizontal main lobe and a small second conical lobe at an angle of 60° elevation into the sky. However the horizontal radiated power and gain keeps increasing and reaches a maximum at a length of five-eighths wavelength: ${5 \over 8}\lambda =.625\lambda$ (this is an approximation valid for a typical thickness antenna, for an infinitely thin monopole the maximum occurs at ${2 \over \pi }\lambda =.637\lambda$ ) The maximum occurs at this length because the opposite phase radiation from the two lobes interferes destructively and cancels at high angles, leaving more power to be radiated in horizontal directions.

Above $.625\lambda$ the high angle lobe gets larger, becoming the main lobe, and the horizontal lobe rapidly gets smaller, reducing power radiated in horizontal directions, so very few antennas use lengths above this. At the 4th harmonic, $h=\lambda$ , the horizontal lobe disappears and all the power is radiated in the high angle lobe. As the antenna is made longer, the pattern divides into more lobes, with nulls (directions of zero radiated power) between them.

The general effect of electrically small ground planes, as well as imperfectly conducting earth grounds, is to tilt the direction of maximum radiation up to higher elevation angles and reduce the gain. When mounted on the Earth, due to the finite resistance of the soil the portion of the ground wave propagating horizontally in contact with the ground is attenuated exponentially and vanishes at long distances, so in the (far field) radiation pattern the radiated power declines smoothly to zero at the horizon (zero elevation angle).

With an asymmetrical ground plane, such as a whip antenna mounted on a car’s bumper, the pattern will no longer be omnidirectional, but will have stronger horizontal radiation on the side with the larger ground plane area.

### Gain and input impedance

| Length h wavelengths | Gain   dBi | 3 dB Beamwidth degrees | Radiation resistance ohms |   |
|---|---|---|---|---|
| ≪0.25 | 4.76 | 45° | $\approx 394(h/\lambda )^{2}$ | electrically short |
| 0.25 | 5.19 | 39° | 36.5 | fundamental |
| 0.375 | 5.75 | 32° | 92.8 |   |
| 0.5 | 6.82 | 24° | >600 | 2nd harmonic |
| 0.625 | 8.16 | 16° | 53.2 | maximum gain |
| 0.75 |   |   | 52.7 | 3rd harmonic |

Because it radiates only into the space above the ground plane, or half the space of a dipole antenna, a monopole antenna over a perfectly conducting infinite ground plane will have a gain of twice (3 dB greater than) the gain of a similar dipole antenna, and a radiation resistance half that of a dipole. Since a half-wave dipole has a gain of 2.19 dBi and a radiation resistance of 73.1 ohms, a quarter-wave ( $\lambda /4$ ) monopole will have a gain of 2.19 + 3 = 5.19 dBi and a radiation resistance of about 36.5 ohms. The antenna is resonant at this length, so its input impedance is purely resistive. The input impedance has capacitive reactance below $\lambda /4$ , inductive reactance from $\lambda /4$ to $\lambda /2$ , and capacitive reactance from $\lambda /2$ to $3\lambda /4$ .

The gain figures given in the table above are never approached in practice; they would only be achieved if the antenna was mounted over an infinite perfectly conducting ground plane. The ground plane is part of the antenna, and the gain is highly dependent on its size and conductivity. An artificial ground plane a wavelength or more in radius is equivalent to a infinite plane, but for smaller planes, which are often used at high frequencies, the gain will be 2 to 5 dBi lower, because some of the horizontal radiated power will diffract around the plane edge into the lower half space. Similarly over a resistive Earth ground the gain will be lower due to power absorbed in the Earth.

For electrically short monopoles below $\lambda /4$ the gain decreases slowly; it is 4.76 dBi at $\lambda /20$ . As the length is increased to a half-wavelength ( $\lambda /2$ ), the gain increases to about 1.7 dB over the $\lambda /4$ gain. Since at this length the antenna has a current node at its feedpoint, the input impedance is very high.

The gain continues to increase up to a maximum of about 3 dB over a quarter-wave monopole at a length of five-eighths wavelength ( $.625\lambda$ ) so this is a popular length for ground wave antennas and terrestrial communication antennas. The radiation resistance drops to about 53 ohms at that length. Above $.625\lambda$ the horizontal gain drops rapidly because more power is radiated at high elevation angles in the second lobe.

### Directivity equation

The reason a vertical monopole has an omnidirectional radiation pattern is that it is axially symmetrical about the vertical axis. The radiation pattern is given in spherical coordinates $r,\theta ,\phi$ , and due to this symmetry the pattern does not depend on the azimuth variable, $\phi$ .

As mentioned, the radiation pattern of the monopole is the same as the top half of the dipole pattern. At any point above the ground plane the time average power density (Poynting vector) ${\widehat {S}}$ in watts per square meter of radio waves emitted by a monopole is twice that of a vertical dipole antenna ${\widehat {S}}_{\text{d}}$ of twice the length

${\widehat {S}}=2{\widehat {S}}_{\text{d}}$

Since for an electromagnetic wave in space ${\widehat {S}}={E^{2} \over 2\eta }$ the power density is proportional to the square of the electric field, therefore: $E={\sqrt {2}}E_{\text{d}}$

For a radio antenna what is of interest is the radiation pattern in the far field region, far enough from the antenna so the induction fields have died out. The Fraunhofer diffraction equation below is accurate when $r\gg h$ , $kr={2\pi r \over \lambda }\gg 1$ and $kh^{2}\ll 4\pi r$ , that is at distances from the antenna r much greater than the element length and the wavelength. From the radiation pattern of a dipole given in the literature the far field electric field radiation pattern of a thin ( $hk\ll 1$ ) monopole mounted over a perfectly conducting infinite ground plane is

$E(r,\theta )={j\eta I_{\text{0}}e^{jkr} \over {\sqrt {2}}\pi r}{\Bigg [}{\cos(kh\sin \theta )-\cos kh \over \cos \theta }{\Bigg ]}$

where

h

is the height of the element

$k={2\pi \over \lambda }={2\pi f \over c}$

$\eta$

is the impedance of free space, 376.74 ohms

$I_{\text{0}}$

is the feed current at the bottom of the antenna

r

is the distance from origin of the coordinate system at the base of the antenna to the reception point.

$\theta$

is the angle with respect to the positive z axis, the axis of the element. Since the ground plane reflects the radio waves, this equation only gives the radiation field for

$0\leq \theta <\pi /2$

the field is zero for

$\pi /2\leq \theta \leq \pi$

$j={\sqrt {-1}}$

is the

imaginary unit

The electric field E given by this equation is a phasor, a complex number with magnitude equal to the peak field and angle equal to the phase difference between the sinusoidal field and the input current. The presence of j at the front of the equation means that the electric and magnetic fields leave the antenna 90° out of phase with the feed current.

The average power density in watts per square meter radiated by the monopole is

${\widehat {S}}(r,\theta )={\eta I_{\text{0}}^{2} \over 4\pi ^{2}r^{2}}{\Bigg [}{\cos(kh\sin \theta )-\cos kh \over \cos \theta }{\Bigg ]}^{2}$


## Types of feed

Because in a resonant antenna the energy fed to the antenna by the transmitter each cycle is small compared to the energy stored in the standing wave on the antenna, the feed current can be applied at different points on the antenna without altering the current standing wave pattern much; leaving the radiation pattern the same. The advantage of this is that at different points on the antenna the input impedance has different values, allowing the possibility of impedance matching the antenna to the feedline characteristic impedance without a matching network, by choosing the correct feedpoint.

- *Series* or *base feed* - This is the most common type, the type discussed above, in which the feedline is connected between the base of the monopole and the ground plane. For the quarter-wave $\lambda /4$ monopole and odd harmonics the input impedance is a minimum, 36.8 ohms for a quarter-wave monopole. For the half-wave $\lambda /2$ monopole, the impedance is very high, requiring a matching transformer.
- *Shunt feed* - One side of the feedline is connected to ground, and the other to a point along the antenna element, and the base of the element is grounded. The part of the element between the feedpoint and ground acts as a shorted stub. Since the impedance is zero at the base and increases continuously to a very high value, 800 - 4000 ohms at a height of $\lambda /4$ , any input impedance between these values can be realized by choosing the correct feed height on the element.

- *Gamma match* - a shunt feed with a capacitor in the feedline connecting to the element.

- *Folded monopole* - A monopole can also be fed at the top, by grounding the base of the element, mounting a parallel conductor next to it, attached at the top, and feeding this conductor at the bottom. Because of their proximity the two elements are coupled so the current and voltage are the same in each. The folded monopole has a radiation resistance of 4 times the base fed monopole.


## Electrically short monopoles

A monopole shorter than the fundamental resonance length of a quarter-wavelength at its operating frequency is called *electrically short*. Electrically short monopoles are widely used since they are more compact, and at long wavelengths construction limitations make it impractical to build an antenna mast a quarter wavelength high. Even a very short rod a small fraction of a wavelength long can be impedance matched to a transmitter so it absorbs all the power from the feedline. However as the length is decreased the antenna eventually becomes inefficient due to its low radiation resistance.

Below a quarter wavelength the radiation resistance of a monopole decreases approximately with the square of the ratio of length to wavelength

$R_{\text{R}}\approx {\eta \pi \over 3}{\Big (}{h \over \lambda }{\Big )}^{2}=(394{\text{Ω}}){\Big (}{h \over \lambda }{\Big )}^{2}\qquad h\ll {\lambda \over 4}$

The radiation resistance is only part of the feedpoint resistance at the antenna terminals. A monopole and its feed system have other power losses which appear as additional resistance in series with the radiation resistance at the transmitter terminals; ohmic resistance of the metal antenna elements, dielectric losses in insulating materials, feedline losses, losses in the loading coil necessary for impedance matching, and particularly resistive losses in the Earth ground system, often the largest loss factor in low frequency monopoles. The total feedpoint resistance $R_{\text{IN}}$ seen by the transmitter is equal to the sum of the radiation resistance $R_{\text{R}}$ and loss resistance $R_{\text{L}}$

$R_{\text{IN}}=R_{\text{R}}+R_{\text{L}}$

The power $P_{\text{IN}}$ fed to the antenna is split proportionally between these two resistances. From Joule's law

$P_{\text{IN}}=I_{\text{IN}}^{2}R_{\text{IN}}$

$P_{\text{IN}}=I_{\text{IN}}^{2}(R_{\text{R}}+R_{\text{L}})$

$P_{\text{IN}}=P_{\text{R}}+P_{\text{L}}$

where

$P_{\text{R}}=I_{\text{IN}}^{2}R_{\text{R}}={\eta \pi \over 3}{\Big (}{hI_{\text{IN}} \over \lambda }{\Big )}^{2}\quad$

and

$\quad P_{\text{L}}=I_{\text{IN}}^{2}R_{\text{L}}$

The power $P_{\text{R}}$ consumed by radiation resistance is converted to radio waves, the desired function of the antenna, while the power $P_{\text{L}}$ consumed by loss resistance is converted to heat, representing a waste of transmitter power. So for minimum power loss it is desirable that the radiation resistance be much greater than the loss resistance. The ratio of the radiation resistance to the total feedpoint resistance is equal to the efficiency $e_{\text{A}}$ of the antenna as a transducer

$e_{\text{A}}={P_{\text{R}} \over P_{\text{IN}}}={R_{\text{R}} \over R_{\text{R}}+R_{\text{L}}}$

As the monopole is made shorter it's radiation resistance decreases and a greater proportion of the transmitter power is dissipated in the loss resistance. Base-fed mast radiator antennas shorter than about .16 wavelength are not used, as the radiation resistance at that length is around 10 ohms, 5 times the typical resistance of a buried radial ground system, 2 ohms, so in an Earth-grounded antenna over 20% of the transmitter power would be wasted in the ground resistance. In the VLF band the huge top-loaded wire monopoles used by megawatt military transmitters are often less than 0.01 wavelengths high and have radiation resistance of less than 0.1 ohm. Even with extremely low resistance ground systems they are often only 15% to 30% efficient.

Another disadvantage of electrically short monopoles is that as the antenna is made shorter and the radiation resistance decreases, the capacitance decreases and so the capacitive reactance increases. The low resistance in combination with the capacitance of the antenna and inductance of the required loading coil gives the antenna a large Q factor; this means it has a narrow bandwidth, which reduces the data rate that can be transmitted or received. Antennas in the VLF band often have a bandwidth of only 50 to 100 hertz. The Chu-Harrington limit gives the minimum Q factor for a small antenna.

### Capacitively top-loaded monopoles

To increase the radiated power of an electrically short monopole, capacitance to ground can be added to the top by attaching horizontal metal conductors, insulated from ground, to the top of the element. This is called a *top loaded monopole*. This results in increased current in the vertical monopole element, to charge and discharge the capacitance each cycle. Since the power radiated by a monopole is proportional to the square of the current in the radiating element, this increases the radiated power and thus the radiation resistance. The buried radial wire ground system under the antenna serves as the bottom plate of the 'capacitor'.

Mast radiators sometimes include a circular structure of radial rods at the top of the mast; this is called a 'top hat'. At lower frequencies in the LF and VLF bands larger top loads are used. The T antenna consists of a vertical wire driven at the bottom, rising to attach to the center of a horizontal top load wire insulated at both ends, supported by masts. Multiple parallel top load wires can be used to increase capacitance. The largest top loaded antenna is the umbrella antenna, consisting of a monopole mast radiator with many diagonal top load wires radiating symmetrically from the top, anchored to the ground through insulators. To tune out the high capacitive reactance and make the antenna resonant a large loading coil is required in series with the feedline at the base of the antenna.

At low frequencies, due to the high capacitance and low radiation resistance, the top loaded monopole has a very narrow bandwidth. This may limit the width of sidebands and thus the data rate that can be transmitted. High power transmitting antennas in the VLF band typically have Q of several hundred and bandwidths less than 100 Hz. The energy stored in the antenna, stored alternately as an electrostatic field in the top load and a magnetic field in the loading coil, is hundreds of times the energy input from the transmitter each cycle. The voltage at the ends of the top-load wires is very high, Q times the feed voltage, and may be hundreds of kilovolts, requiring very good insulation. The antenna must be tuned to resonance with the transmitter using a variometer coil.


## Definition of variables

| Symbol | Unit | Definition |
|---|---|---|
| $\alpha$ | [none] | element length-to-diameter ratio $h/2b$ |
| $\eta$ | ohm (Ω) | Impedance of free space = ${\sqrt {\mu _{\text{0}}/\epsilon _{\text{0}}}}$ = 376.73 ohms |
| $\Phi$ | radian | Phase shift of antenna current during round trip along element |
| $\phi$ | radian | azimuth angle of spherical coordinate system |
| $\lambda$ | meter (m) | Free space wavelength of radio waves |
| $\pi$ | [none] | Math constant ≈ 3.1416 |
| $\theta$ | radian | angle from vertical axis in spherical coordinate system |
| b | meter (m) | radius of monopole element |
| c | meters per second (ms−1) | Velocity of light |
| e | [none] | Base of natural logarithms = 2.71828 |
| $e_{\text{A}}$ | [none] | Efficiency of the antenna |
| f | hertz (Hz) | Frequency of radio waves |
| $f_{\mathsf {n}}$ | hertz (Hz) | Resonant frequencies of monopole |
| G | [none] | Electrical length, length in wavelengths, of the monopole element |
| h | meter (m) | length of monopole element |
| $i_{\mathsf {up}}(z,t)$ | ampere (A) | Upward current wave on antenna element at elevation *z* and time *t* |
| $i_{\mathsf {down}}(z,t)$ | ampere (A) | Downward current wave on antenna element at elevation *z* and time *t* |
| $I(z)$ | ampere (A) | Standing wave current on antenna element at elevation *z* |
| $I_{\mathsf {IN}}$ | ampere (A) | RMS current into antenna terminals |
| $I_{\mathsf {0}}$ | ampere (A) | Maximum RMS current in antenna element |
| $I_{\mathsf {1}}$ | ampere (A) | RMS current at an arbitrary point in antenna element |
| j | [none] | imaginary unit ${\sqrt {-1}}$ |
| k | meter−1 | Angular wavenumber $=2\pi /\lambda$ |
| $P_{\mathsf {IN}}$ | watt (W) | Electric power delivered to antenna terminals |
| $P_{\mathsf {R}}$ | watt (W) | Power radiated as radio waves by antenna |
| $P_{\mathsf {L}}$ | watt (W) | Power consumed in loss resistances of antenna |
| Q | [none] | Q factor of antenna, the resonant frequency divided by bandwidth |
| r | meters | Distance from the origin at the base of the element to the observation point |
| $R_{\mathsf {R}}$ | ohm (Ω) | Radiation resistance of antenna |
| $R_{\mathsf {L}}$ | ohm (Ω) | Equivalent loss resistance of antenna at input terminals |
| $R_{\mathsf {IN}}$ | ohm (Ω) | Input resistance of antenna |
| $R_{\mathsf {R0}}$ | ohm (Ω) | Radiation resistance at point of maximum current in antenna |
| $R_{\mathsf {R1}}$ | ohm (Ω) | Radiation resistance at arbitrary point in antenna |
| ${\widehat {S}}(r,\theta )$ | watts per square meter | power density averaged over a cycle radiated by the antenna in the direction $r,\theta$ |
| ${\widehat {S}}_{\text{d}}$ | watts per square meter | power density radiated by a dipole antenna twice the height |
| t | second (s) | Time |
| $X_{\mathsf {R}}$ | ohm (Ω) | Input reactance of antenna |
| z | meter (m) | Height on monopole element above lower end |
