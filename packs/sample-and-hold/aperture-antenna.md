---
title: "Aperture (antenna)"
source: https://en.wikipedia.org/wiki/Aperture_(antenna)
domain: sample-and-hold
license: CC-BY-SA-4.0
tags: sample and hold, aperture jitter, zero-order hold, track and hold
fetched: 2026-07-02
---

# Aperture (antenna)

In electromagnetics and antenna theory, the **aperture** of an antenna is defined as "A surface, near or on an antenna, on which it is convenient to make assumptions regarding the field values for the purpose of computing fields at external points. The aperture is often taken as that portion of a plane surface near the antenna, perpendicular to the direction of maximum radiation, through which the major part of the radiation passes."

## Effective area

The **effective area** of an antenna is defined as "In a given direction, the ratio of the available power at the terminals of a receiving antenna to the power flux density of a plane wave incident on the antenna from that direction, the wave being polarization matched to the antenna." Of particular note in this definition is that both effective area and power flux density are functions of incident angle of a plane wave. Assume a plane wave from a particular direction $(\theta ,\phi )$ , which are the azimuth and elevation angles relative to the array normal, has a *power flux density* $\|{\vec {S}}\|$ ; this is the amount of power passing through a unit area normal to the direction of the plane wave of one square meter.

By definition, if an antenna delivers $P_{\text{O}}$ watts to the transmission line connected to its output terminals when irradiated by a uniform field of power density $|S(\theta ,\phi )|$ watts per square meter, the antenna's effective area $A_{\text{e}}$ for the direction of that plane wave is given by

$A_{\text{e}}(\theta ,\phi )={\frac {P_{O}}{\|{\vec {S}}(\theta ,\phi )\|}}.$

The power $P_{\text{O}}$ accepted by the antenna (the power at the antenna terminals) is less than the power $P_{\text{R}}$ received by an antenna by the radiation efficiency $\eta$ of the antenna. $P_{\text{R}}$ is equal to the power density of the electromagnetic energy $|S(\theta ,\phi )|=|{\vec {S}}\cdot {\hat {a}}|$ , where ${\hat {a}}$ is the unit vector normal to the array aperture, multiplied by the physical aperture area A . The incoming radiation is assumed to have the same polarization as the antenna. Therefore,

$P_{\text{O}}=\eta P_{\text{R}}=\eta A|{\vec {S}}\cdot {\hat {a}}|=\eta A\|{\vec {S}}(\theta ,\phi )\|\cos \theta \cos \phi ,$

and

$A_{\text{e}}(\theta ,\phi )=\eta A\cos \theta \cos \phi .$

The effective area of an antenna or aperture is based upon a *receiving* antenna. However, due to reciprocity, an antenna's directivity in receiving and transmitting are identical, so the power transmitted by an antenna in different directions (the radiation pattern) is also proportional to the effective area $A_{e}$ . When no direction is specified, $A_{e}$ is understood to refer to its maximal value.

### Effective length

Most antenna designs are not defined by a physical area but consist of wires or thin rods; then the effective aperture bears no clear relation to the size or area of the antenna. An alternate measure of antenna response that has a greater relationship to the physical length of such antennas is **effective length** $l_{\text{eff}}$ measured in metres, which is defined for a receiving antenna as

$l_{\text{eff}}=V_{0}/E_{\text{s}},$

where

$V_{0}$

is the

open-circuit voltage

appearing across the antenna's terminals,

$E_{s}$

is the electric

field strength

of the radio signal, in

volts

per metre, at the antenna.

The longer the effective length, the greater is the voltage appearing at its terminals. However, the actual power implied by that voltage depends on the antenna's feedpoint impedance, so this cannot be directly related to antenna gain, which *is* a measure of received power (but does not directly specify voltage or current). For instance, a half-wave dipole has a much longer effective length than a short dipole. However the effective area of the short dipole is almost as great as it is for the half-wave antenna, since (ideally), given an ideal impedance-matching network, it can receive almost as much power from that wave. Note that for a given antenna feedpoint impedance, an antenna's gain or $A_{\text{eff}}$ increases according to the *square* of $l_{\text{eff}}$ , so that the effective length for an antenna relative to different wave directions follows the *square root* of the gain in those directions. But since changing the physical size of an antenna inevitably changes the impedance (often by a great factor), the effective length is not by itself a useful figure of merit for describing an antenna's peak directivity and is more of theoretical importance. In practice, the effective length of a particular antenna is often combined with its impedance and loss to become the realized effective length.

## Aperture efficiency

In general, the aperture of an antenna cannot be directly inferred from its physical size. However so-called *aperture antennas* such as parabolic dishes and horn antennas, have a large (relative to the wavelength) physical area $A_{\text{phys}}$ which is opaque to such radiation, essentially casting a shadow from a plane wave and thus removing an amount of power $A_{\text{phys}}S$ from the original beam. That power removed from the plane wave can be actually received by the antenna (converted into electrical power), reflected or otherwise scattered, or absorbed (converted to heat). In this case the *effective aperture* $A_{e}$ is always less than (or equal to) the area of the antenna's physical aperture $A_{\text{phys}}$ , as it accounts only for the portion of that wave actually received as electrical power. An aperture antenna's *aperture efficiency* $e_{\text{a}}$ is defined as the ratio of these two areas:

$e_{\text{a}}={\frac {A_{e}}{A_{\text{phys}}}}.$

The **aperture efficiency** is a dimensionless parameter between 0 and 1 that measures how close the antenna comes to using all the radio wave power intersecting its physical aperture. If the aperture efficiency were 100%, then all the wave's power falling on its physical aperture would be converted to electrical power delivered to the load attached to its output terminals, so these two areas would be equal: $A_{\text{e}}=A_{\text{phys}}$ . But due to nonuniform illumination by a parabolic dish's feed, as well as other scattering or loss mechanisms, this is not achieved in practice. Since a parabolic antenna's cost and wind load increase with the *physical* aperture size, there may be a strong motivation to reduce these (while achieving a specified antenna gain) by maximizing the aperture efficiency. Aperture efficiencies of typical aperture antennas vary from 0.35 to well over 0.70.

Note that when one simply speaks of an antenna's "efficiency", what is most often meant is the *radiation efficiency*, a measure which applies to all antennas (not just aperture antennas) and accounts only for the gain reduction due to losses. Outside of aperture antennas, most antennas consist of thin wires or rods with a small physical cross-sectional area (generally much smaller than $A_{\text{e}}$ ) for which "aperture efficiency" is not even defined.

## Aperture and gain

The *directivity* of an antenna, its ability to direct radio waves preferentially in one direction or receive preferentially from a given direction, is expressed by a parameter G called *antenna gain*. This is most commonly defined as the ratio of the power $P_{\text{o}}$ received by that antenna from waves in a given direction to the power $P_{\text{iso}}$ that would be received by an ideal isotropic antenna, that is, a hypothetical antenna that receives power equally well from all directions. It can be seen that (for antennas at a given frequency) gain is also equal to the ratio of the apertures of these antennas:

$G={\frac {P_{\text{o}}}{P_{\text{iso}}}}={\frac {A_{\text{e}}}{A_{\text{iso}}}}.$

As shown below, the aperture of a lossless isotropic antenna, which by this definition has unity gain, is

$A_{\text{iso}}={\frac {\lambda ^{2}}{4\pi }},$

where $\lambda$ is the wavelength of the radio waves. Thus

$G={\frac {A_{\text{e}}}{A_{\text{iso}}}}={\frac {4\pi A_{\text{e}}}{\lambda ^{2}}}.$

So antennas with large effective apertures are considered high-gain antennas (or *beam antennas*), which have relatively small angular beam widths. As receiving antennas, they are much more sensitive to radio waves coming from a preferred direction compared to waves coming from other directions (which would be considered interference). As transmitting antennas, most of their power is radiated in a particular direction at the expense of other directions. Although antenna gain and effective aperture are functions of direction, when no direction is specified, these are understood to refer to their maximal values, that is, in the direction(s) of the antenna's intended use (also referred to as the antenna's main lobe or boresight).

## Friis transmission formula

The fraction of the power delivered to a transmitting antenna that is received by a receiving antenna is proportional to the product of the apertures of both the antennas and inversely proportional to the squared values of the distance between the antennas and the wavelength. This is given by a form of the Friis transmission formula:

${\frac {P_{\text{r}}}{P_{\text{t}}}}={\frac {A_{\text{r}}A_{\text{t}}}{d^{2}\lambda ^{2}}},$

where

$P_{\text{t}}$

is the power fed into the transmitting antenna input terminals,

$P_{\text{r}}$

is the power available at receiving antenna output terminals,

$A_{\text{r}}$

is the effective area of the receiving antenna,

$A_{\text{t}}$

is the effective area of the transmitting antenna,

d

is the distance between antennas (the formula is only valid for

d

large enough to ensure a plane wave front at the receive antenna, sufficiently approximated by

$d\gtrsim 2a^{2}/\lambda$

, where

a

is the largest linear dimension of either of the antennas),

$\lambda$

is the wavelength of the radio frequency.

## Derivation of antenna aperture from thermodynamic considerations

The aperture of an isotropic antenna, the basis of the definition of gain above, can be derived on the basis of consistency with thermodynamics. Suppose that an ideal isotropic antenna *A* with a driving-point impedance of *R* sits within a closed system CA in thermodynamic equilibrium at temperature *T*. We connect the antenna terminals to a resistor also of resistance *R* inside a second closed system CR, also at temperature *T*. In between may be inserted an arbitrary lossless electronic filter *Fν* passing only some frequency components.

Each cavity is in thermal equilibrium and thus filled with black-body radiation due to temperature *T*. The resistor, due to that temperature, will generate Johnson–Nyquist noise with an open-circuit voltage whose mean-squared spectral density is given by

${\overline {v_{n}^{2}}}=4k_{\text{B}}TR\,\eta (f),$

where $\eta (f)$ is a quantum-mechanical factor applying to frequency *f*; at normal temperatures and electronic frequencies $\eta (f)=1$ , but in general is given by

$\eta (f)={\frac {hf/k_{\text{B}}T}{e^{hf/k_{\text{B}}T}-1}}.$

The amount of power supplied by an electrical source of impedance *R* into a matched load (that is, something with an impedance of *R*, such as the antenna in CA) whose rms open-circuit voltage is *v*rms is given by

$P={\frac {{\text{v}}_{\text{rms}}^{2}}{4{\text{R}}}}.$

The mean-squared voltage ${\overline {v_{n}^{2}}}={\text{v}}_{\text{rms}}^{2}$ can be found by integrating the above equation for the spectral density of mean-squared noise voltage over frequencies passed by the filter *Fν*. For simplicity, let us just consider *Fν* as a narrowband filter of bandwidth *B*1 around central frequency *f*1, in which case that integral simplifies as follows:

$P_{R}={\frac {\int _{0}^{\infty }4k_{\text{B}}TR\,\eta (f)\,F_{\nu }(f)\,df}{4{\text{R}}}}$

$\qquad ={\frac {4k_{\text{B}}TR\,\eta (f_{1})\,B_{1}}{4{\text{R}}}}=k_{\text{B}}T\,\eta (f_{1})\,B_{1}.$

This power due to Johnson noise from the resistor is received by the antenna, which radiates it into the closed system CA.

The same antenna, being bathed in black-body radiation of temperature *T*, receives a spectral radiance (power per unit area per unit frequency per unit solid angle) given by Planck's law:

${\text{P}}_{f,A,\Omega }(f)={\frac {2hf^{3}}{c^{2}}}{\frac {1}{e^{hf/k_{\text{B}}T}-1}}={\frac {2f^{2}}{c^{2}}}\,k_{\text{B}}T\,\eta (f),$

using the notation $\eta (f)$ defined above.

However, that radiation is unpolarized, whereas the antenna is only sensitive to one polarization, reducing it by a factor of 2. To find the total power from black-body radiation accepted by the antenna, we must integrate that quantity times the assumed cross-sectional area *A*eff of the antenna over all solid angles Ω and over all frequencies *f*:

$P_{A}=\int _{0}^{\infty }\int _{4\pi }\,{\frac {P_{f,A,\Omega }(f)}{2}}A_{\text{eff}}(\Omega ,f)\,F_{\nu }(f)\,d\Omega \,df.$

Since we have assumed an isotropic radiator, *A*eff is independent of angle, so the integration over solid angles is trivial, introducing a factor of 4π. And again we can take the simple case of a narrowband electronic filter function *Fν* which only passes power of bandwidth *B*1 around frequency *f*1. The double integral then simplifies to

$P_{A}=2\pi P_{f,A,\Omega }(f)A_{\text{eff}}\,B_{1}={\frac {4\pi \,k_{\text{B}}T\,\eta (f_{1})}{\lambda _{1}^{2}}}A_{\text{eff}}B_{1},$

where $\lambda _{1}=c/f_{1}$ is the free-space wavelength corresponding to the frequency *f*1.

Since each system is in thermodynamic equilibrium at the same temperature, we expect no net transfer of power between the cavities. Otherwise one cavity would heat up and the other would cool down in violation of the second law of thermodynamics. Therefore, the power flows in both directions must be equal:

$P_{A}=P_{R}.$

We can then solve for *A*eff, the cross-sectional area intercepted by the isotropic antenna:

${\frac {4\pi \,k_{\text{B}}T\,\eta (f_{1})}{\lambda _{1}^{2}}}A_{\text{eff}}B_{1}=k_{\text{B}}T\,\eta (f_{1})\,B_{1},$

$A_{\text{eff}}={\frac {\lambda _{1}^{2}}{4\pi }}.$

We thus find that for a hypothetical isotropic antenna, thermodynamics demands that the effective cross-section of the receiving antenna to have an area of λ2/4π. This result could be further generalized if we allow the integral over frequency to be more general. Then we find that *A*eff for the same antenna must vary with frequency according to that same formula, using λ = *c*/*f*. Moreover, the integral over solid angle can be generalized for an antenna that is *not* isotropic (that is, any real antenna). Since the angle of arriving electromagnetic radiation only enters into *A*eff in the above integral, we arrive at the simple but powerful result that the *average* of the effective cross-section *A*eff over all angles at wavelength λ must also be given by

${\overline {A_{\text{eff}}}}={\frac {\lambda ^{2}}{4\pi }}.$

Although the above is sufficient proof, we can note that the condition of the antenna's impedance being *R*, the same as the resistor, can also be relaxed. In principle, any antenna impedance (that isn't totally reactive) can be impedance-matched to the resistor *R* by inserting a suitable (lossless) matching network. Since that network is lossless, the powers *P*A and *P*R will still flow in opposite directions, even though the voltage and currents seen at the antenna and resistor's terminals will differ. The spectral density of the power flow in either direction will still be given by $k_{\text{B}}T\,\eta (f)$ , and in fact this is the very thermal-noise power spectral density associated with one electromagnetic mode, be it in free-space or transmitted electrically. Since there is only a single connection to the resistor, the resistor itself represents a single mode. And an antenna, also having a single electrical connection, couples to one mode of the electromagnetic field according to its average effective cross-section of $\lambda _{1}^{2}/(4\pi )$ .
