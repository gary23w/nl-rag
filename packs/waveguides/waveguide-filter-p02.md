---
title: "Waveguide filter (part 2/2)"
source: https://en.wikipedia.org/wiki/Waveguide_filter
domain: waveguides
license: CC-BY-SA-4.0
tags: rectangular waveguide, cutoff frequency, transverse mode, waveguide filter
fetched: 2026-07-02
part: 2/2
---

## Filter-like devices

There are many applications of filters whose design objectives are something other than rejection or passing of certain frequencies. Frequently, a simple device that is intended to work over only a narrow band or just one spot frequency will not look much like a filter design. However, a broadband design for the same item requires many more elements and the design takes on the nature of a filter. Amongst the more common applications of this kind in waveguide are impedance matching networks, directional couplers, power dividers, power combiners, and diplexers. Other possible applications include multiplexers, demultiplexers, negative-resistance amplifiers, and time-delay networks.

### Impedance matching

A simple method of impedance matching is stub matching with a single stub. However, a single stub will only produce a perfect match at one particular frequency. This technique is therefore only suitable for narrow band applications. To widen the bandwidth multiple stubs may be used, and the structure then takes on the form of a stub filter. The design proceeds as if it were a filter except that a different parameter is optimised. In a frequency filter typically the parameter optimised is stopband rejection, passband attenuation, steepness of transition, or some compromise between these. In a matching network the parameter optimised is the impedance match. The function of the device does not require a restriction of bandwidth, but the designer is nevertheless forced to choose a bandwidth because of the *structure* of the device.

Stubs are not the only format of filter than can be used. In principle, any filter structure could be applied to impedance matching, but some will result in more practical designs than others. A frequent format used for impedance matching in waveguide is the stepped impedance filter. An example can be seen in the duplexer[e] pictured in figure 13.

### Directional couplers and power combiners

Directional couplers, power splitters, and power combiners are all essentially the same type of device, at least when implemented with passive components. A directional coupler splits a small amount of power from the main line to a third port. A more strongly coupled, but otherwise identical, device may be called a power splitter. One that couples exactly half the power to the third port (a 3 dB coupler) is the maximum coupling achievable without reversing the functions of the ports. Many designs of power splitter can be used in reverse, whereupon they become power combiners.

A simple form of directional coupler is two parallel transmission lines coupled together over a λ/4 length. This design is limited because the electrical length of the coupler will only be λ/4 at one specific frequency. Coupling will be a maximum at this frequency and fall away on either side. Similar to the impedance matching case, this can be improved by using multiple elements, resulting in a filter-like structure. A waveguide analogue of this coupled lines approach is the Bethe-hole directional coupler in which two parallel waveguides are stacked on top of each other and a hole provided for coupling. To produce a wideband design, multiple holes are used along the guides as shown in figure 14 and a filter design applied. It is not only the coupled-line design that suffers from being narrow band, all simple designs of waveguide coupler depend on frequency in some way. For instance the rat-race coupler (which can be implemented directly in waveguide) works on a completely different principle but still relies on certain lengths being exact in terms of λ.

### Diplexers and duplexers

A diplexer is a device used to combine two signals occupying different frequency bands into a single signal. This is usually to enable two signals to be transmitted simultaneously on the same communications channel, or to allow transmitting on one frequency while receiving on another. (This specific use of a diplexer is called a duplexer.) The same device can be used to separate the signals again at the far end of the channel. The need for filtering to separate the signals while receiving is fairly self-evident but it is also required even when combining two transmitted signals. Without filtering, some of the power from source A will be sent towards source B instead of the combined output. This will have the detrimental effects of losing a portion of the input power and loading source A with the output impedance of source B thus causing mismatch. These problems could be overcome with the use of a 3 dB directional coupler, but as explained in the previous section, a wideband design requires a filter design for directional couplers as well.

Two widely spaced narrowband signals can be diplexed by joining together the outputs of two appropriate band-pass filters. Steps need to be taken to prevent the filters from coupling to each other when they are at resonance which would cause degradation of their performance. This can be achieved by appropriate spacing. For instance, if the filters are of the iris-coupled type then the iris nearest to the filter junction of filter A is placed λgb/4 from the junction where λgb is the guide wavelength in the passband of filter B. Likewise, the nearest iris of filter B is placed λga/4 from the junction. This works because when filter A is at resonance, filter B is in its stopband and only loosely coupled and vice versa. An alternative arrangement is to have each filter joined to a main waveguide at separate junctions. A decoupling resonator is placed λg/4 from the junction of each filter. This can be in the form of a short-circuited stub tuned to the resonant frequency of that filter. This arrangement can be extended to multiplexers with any number of bands.

For diplexers dealing with contiguous passbands proper account of the crossover characteristics of filters needs to be considered in the design. An especially common case of this is where the diplexer is used to split the entire spectrum into low and high bands. Here a low-pass and a high-pass filter are used instead of band-pass filters. The synthesis techniques used here can equally be applied to narrowband multiplexers and largely remove the need for decoupling resonators.

### Directional filters

A directional filter is a device that combines the functions of a directional coupler and a diplexer. As it is based on a directional coupler it is essentially a four-port device, but like directional couplers, port 4 is commonly permanently terminated internally. Power entering port 1 exits port 3 after being subject to some filtering function (usually band-pass). The remaining power exits port 2, and since no power is absorbed or reflected this will be the exact complement of the filtering function at port 2, in this case band-stop. In reverse, power entering ports 2 and 3 is combined at port 1, but now the power from the signals rejected by the filter is absorbed in the load at port 4. Figure 15 shows one possible waveguide implementation of a directional filter. Two rectangular waveguides operating in the dominant TE10 mode provide the four ports. These are joined together by a circular waveguide operating in the circular TE11 mode. The circular waveguide contains an iris coupled filter with as many irises as needed to produce the required filter response.


## Glossary

***^ aperture***

An opening in a wall of a waveguide or barrier between sections of waveguide through which electromagnetic radiation can propagate.

***^*a b*characteristic impedance***

Characteristic impedance

, symbol

Z

0

, of a waveguide for a particular mode is defined as the ratio of the transverse electric field to the transverse magnetic field of a wave travelling in one direction down the guide. The characteristic impedance for air filled waveguide is given by,

$Z_{0}=\left\{{\begin{matrix}Z_{\mathrm {f} }{\dfrac {\lambda _{\mathrm {g} }}{\lambda }}&{\text{(TE mode)}}\\\\Z_{\mathrm {f} }{\dfrac {\lambda }{\lambda _{\mathrm {g} }}}&{\text{(TM mode)}}\end{matrix}}\right.$

where

Z

f

is the

impedance of free space

, approximately

377 Ω

, λ

g

is the guide wavelength, and λ is the wavelength when unrestricted by the guide. For a dielectric filled waveguide, the expression must be divided by

√

κ

, where κ is the dielectric constant of the material, and λ replaced by the unrestricted wavelength in the dielectric medium. In some treatments what is called characteristic impedance here is called the wave impedance, and characteristic impedance is defined as proportional to it by some constant.

***^*c d e*diplexer, duplexer***

A diplexer combines or separates two signals occupying different passbands. A duplexer combines or splits two signals travelling in opposite directions, or of differing polarizations (which may also be in different passbands as well).

***^ E-plane***

The E-plane is the plane lying in the direction of the transverse electric field, that is, vertically along the guide.

***^ guide wavelength***

Guide wavelength

, symbol

λ

g

, is the wavelength measured longitudinally down the waveguide. For a given frequency, λ

g

depends on the mode of transmission and is always longer than the wavelength of an electromagnetic wave of the same frequency in free space. λ

g

is related to the cutoff frequency,

f

c

, by,

$\lambda _{\mathrm {g} }={\frac {\lambda }{\sqrt {1-\left({\frac {f_{\mathrm {c} }}{f}}\right)^{2}}}}$

where λ is the wavelength the wave would have if unrestricted by the guide. For guides that are filled only with air, this will be the same, for all practical purposes, as the free space wavelength for the transmitted frequency,

f

.

***^ H-plane***

The H-plane is the plane lying in the direction of the transverse magnetic field (

H

being the analysis symbol for

magnetic field strength

), that is, horizontally along the guide.

***^*i j*height, width***

Of a rectangular guide, these refer respectively to the small and large internal dimensions of its cross-section. The polarization of the E-field of the dominant mode is parallel to the height.

***^ iris***

A conducting plate fitted transversally across the waveguide with a, usually large, aperture.

***^ singly terminated, doubly terminated***

A doubly terminated filter (the normal case) is one where the generator and load, connected to the input and output ports respectively, have impedances matching the filter characteristic impedance. A singly terminated filter has a matching load, but is driven either by a low impedance voltage source or a high impedance current source.

***^ TEM mode***

Transverse electromagnetic mode, a transmission mode where all the electric field and all the magnetic field are perpendicular to the direction of travel of the electromagnetic wave. This is the usual mode of transmission in pairs of conductors.

***^ TE mode***

Transverse electric mode, one of a number of modes in which all the electric field, but not all the magnetic field, is perpendicular to the direction of travel of the electromagnetic wave. They are designated H modes in some sources because these modes have a longitudinal magnetic component. The first index indicates the number of half wavelengths of field across the width of the waveguide, and the second index indicates the number of half wavelengths across the height. Properly, the indices should be separated with a comma, but usually they are run together, as mode numbers in double figures rarely need to be considered. Some modes specifically mentioned in this article are listed below. All modes are for rectangular waveguide unless otherwise stated.

***^ TE01 mode***

A mode with one half-wave of electric field across the height of the guide and uniform electric field (zero half-waves) across the width of the guide.

***^ TE10 mode***

A mode with one half-wave of electric field across the width of the guide and uniform electric field across the height of the guide.

***^ TE20 mode***

A mode with two half-waves of electric field across the width of the guide and uniform electric field across the height of the guide.

***^ TE11 circular mode***

A mode with one full-wave of electric field around the circumference of the guide and one half-wave of electric field along a radius.

***^ TM mode***

Transverse magnetic mode, one of a number of modes in which all the magnetic field, but not all the electric field, is perpendicular to the direction of travel of the electromagnetic wave. They are designated E modes in some sources because these modes have a longitudinal electric component. See TE mode for a description of the meaning of the indices. Some modes specifically mentioned in this article are:

***^ TM11 mode***

A mode with one half-wave of magnetic field across the width of the guide and one half-wave of magnetic field across the height of the guide. This is the lowest TM mode, since TM

m

0

modes cannot exist.

***^ TM01 circular mode***

A mode with uniform magnetic field around the circumference of the guide and one half-wave of magnetic field along a radius.

***^*o p*transmission line***

A transmission line is a signal transmission medium consisting of a pair of electrical conductors separated from each other, or one conductor and a common return path. In some treatments waveguides are considered to be within the class of transmission lines, with which they have much in common. In this article waveguides are not included so that the two types of medium can more easily be distinguished and referred.
