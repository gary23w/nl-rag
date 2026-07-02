---
title: "Noise figure"
source: https://en.wikipedia.org/wiki/Noise_figure
domain: low-noise-amplifier
license: CC-BY-SA-4.0
tags: low noise amplifier, noise figure, noise temperature, Friis formula
fetched: 2026-07-02
---

# Noise figure

**Noise figure** (**NF**) and **noise factor** (*F*) are figures of merit that indicate degradation of the signal-to-noise ratio (SNR) that is caused by components in a signal chain. These figures of merit are used to evaluate the performance of an amplifier or a radio receiver, with lower values indicating better performance.

The noise factor is defined as the unitless ratio of the output noise power of a device to the portion thereof attributable to thermal noise in the input termination at standard noise temperature *T*0 (usually 290 K). The noise factor is thus the ratio of actual output noise to that which would remain if the device itself did not introduce noise, which is equivalent to the ratio of input SNR to output SNR.

The noise figure is the power level of the noise factor, calculated in terms of the logarithm of noise factor and expressed in scale of decibels (dB).

## General

The noise figure is the difference in decibel (dB) between the noise output of the actual receiver to the noise output of an "ideal" receiver with the same overall gain and bandwidth when the receivers are connected to matched sources at the standard noise temperature *T*0 (usually 290 K). The noise power from a simple load is equal to *kTB*, where *k* is the Boltzmann constant, *T* is the absolute temperature of the load (for example a resistor), and *B* is the measurement bandwidth.

This makes the noise figure a useful figure of merit for terrestrial systems, where the antenna effective temperature is usually near the standard 290 K. In this case, one receiver with a noise figure, say 2 dB better than another, will have an output signal-to-noise ratio that is about 2 dB better than the other. However, in the case of satellite communications systems, where the receiver antenna is pointed out into cold space, the antenna effective temperature is often colder than 290 K. In these cases a 2 dB improvement in receiver noise figure will result in more than a 2 dB improvement in the output signal-to-noise ratio. For this reason, the related figure of *effective noise temperature* is therefore often used instead of the noise figure for characterizing satellite-communication receivers and low-noise amplifiers.

In heterodyne systems, output noise power includes spurious contributions from image-frequency transformation, but the portion attributable to thermal noise in the input termination at standard noise temperature includes only that which appears in the output via the principal frequency transformation of the system and excludes that which appears via the image frequency transformation.

## Definition

The **noise factor** *F* of a system is defined as

$F={\frac {\mathrm {SNR} _{\text{i}}}{\mathrm {SNR} _{\text{o}}}}$

where SNRi and SNRo are the input and output signal-to-noise ratios respectively. The SNR quantities are unitless power ratios. Note that this specific definition is only valid for an input signal of which the noise is *Ni=kT0B*.

The noise figure NF is defined as the noise factor in units of decibels (dB):

$\mathrm {NF} =10\log _{10}(F)=10\log _{10}\left({\frac {\mathrm {SNR} _{\text{i}}}{\mathrm {SNR} _{\text{o}}}}\right)=\mathrm {SNR} _{\text{i, dB}}-\mathrm {SNR} _{\text{o, dB}}$

where SNRi, dB and SNRo, dB are in units of (dB). These formulae are only valid when the input termination is at standard noise temperature *T*0 = 290 K, although in practice small differences in temperature do not significantly affect the values.

The noise factor of a device is related to its noise temperature *T*e:

$F=1+{\frac {T_{\text{e}}}{T_{0}}}.$

Attenuators have a noise factor *F* equal to their attenuation ratio *L* when their physical temperature equals *T*0. More generally, for an attenuator at a physical temperature *T*, the noise temperature is *T*e = (*L* − 1)*T*, giving a noise factor

$F=1+{\frac {(L-1)T}{T_{0}}}.$

## Noise factor of cascaded devices

If several devices are cascaded, the total noise factor can be found with Friis' formula:

$F=F_{1}+{\frac {F_{2}-1}{G_{1}}}+{\frac {F_{3}-1}{G_{1}G_{2}}}+{\frac {F_{4}-1}{G_{1}G_{2}G_{3}}}+\cdots +{\frac {F_{n}-1}{G_{1}G_{2}G_{3}\cdots G_{n-1}}},$

where *F**n* is the noise factor for the *n*-th device, and *G**n* is the power gain (linear, not in dB) of the *n*-th device. The first amplifier in a chain usually has the most significant effect on the total noise figure because the noise figures of the following stages are reduced by stage gains. Consequently, the first amplifier usually has a low noise figure, and the noise figure requirements of subsequent stages is usually more relaxed.

## Noise factor as a function of additional noise

The noise factor may be expressed as a function of the additional output referred noise power $N_{a}$ and the power gain G of an amplifier.

$F=1+{\frac {N_{a}}{N_{i}G}}$

### Derivation

From the definition of noise factor

$F={\frac {\mathrm {SNR} _{\text{i}}}{\mathrm {SNR} _{\text{o}}}}={\frac {\frac {S_{i}}{N_{i}}}{\frac {S_{o}}{N_{o}}}},$

and assuming a system which has a noisy single stage amplifier. The signal to noise ratio of this amplifier would include its own output referred noise $N_{a}$ , the amplified signal $S_{i}G$ and the amplified input noise $N_{i}G$ ,

${\frac {S_{o}}{N_{o}}}={\frac {S_{i}G}{N_{a}+N_{i}G}}$

Substituting the output SNR to the noise factor definition,

$F={\frac {\frac {S_{i}}{N_{i}}}{\frac {S_{i}G}{N_{a}+N_{i}G}}}={\frac {N_{a}+N_{i}G}{N_{i}G}}=1+{\frac {N_{a}}{N_{i}G}}$

In cascaded systems $N_{i}$ does not refer to the output noise of the previous component. An input termination at the standard noise temperature is still assumed for the individual component. This means that the additional noise power added by each component is independent of the other components.

## Optical noise figure

The above describes noise in electrical systems. The optical noise figure is discussed in multiple sources. Electric sources generate noise with a power spectral density, or energy per mode, equal to *kT*, where *k* is the Boltzmann constant and *T* is the absolute temperature. One mode has two quadratures, i.e. the amplitudes of cos $\mathrm {\omega } t$ and sin $\mathrm {\omega } t$ oscillations of voltages, currents or fields. However, there is also noise in optical systems. In these, the sources have no fundamental noise. Instead the energy quantization causes notable shot noise in the detector. In an optical receiver which can output one available mode or two available quadratures this corresponds to a noise power spectral density, or energy per mode, of *hf* where *h* is the Planck constant and *f* is the optical frequency. In an optical receiver with only one available quadrature the shot noise has a power spectral density, or energy per mode, of only *hf*/2.

In the 1990s, an optical noise figure has been defined. This has been called *F**pnf* for *p*hoton *n*umber *f*luctuations. The powers needed for SNR and noise factor calculation are the electrical powers caused by the current in a photodiode. SNR is the square of mean photocurrent divided by variance of photocurrent. Monochromatic or sufficiently attenuated light has a Poisson distribution of detected photons. If, during a detection interval the expectation value of detected photons is *n* then the variance is also *n* and one obtains *SNR**pnf,in* = *n*2/*n* = *n*. Behind an optical amplifier with power gain *G* there will be a mean of *Gn* detectable signal photons. In the limit of large *n* the variance of photons is *Gn*(2*n**sp*(*G*-1)+1) where *n**sp* is the spontaneous emission factor. One obtains *SNR**pnf,out* = *G*2*n*2/(*Gn*(2*n**sp*(*G*-1)+1)) = *n*/(2*n**sp*(1-1/*G*)+1/*G*). Resulting optical noise factor is *F**pnf* = *SNR**pnf,in* / *SNR**pnf,out* = 2*n**sp*(1-1/*G*)+1/*G*.

*F**pnf* is in conceptual conflict with the *e*lectrical noise factor, which is now called *F**e*:

Photocurrent *I* is proportional to optical power *P*. *P* is proportional to squares of a field amplitude (electric or magnetic). So, the receiver is nonlinear in amplitude. The "Power" needed for *SNR**pnf* calculation is proportional to the 4th power of the signal amplitude. But for *F**e* in the electrical domain the power is proportional to the square of the signal amplitude.

If *SNR**pnf* is a noise factor then its definition must be independent of measurement apparatus and frequency. Consider the signal "Power" in the sense of *SNR**pnf* definition. Behind an amplifier it is proportional to *G*2*n*2. We may replace the photodiode by a thermal power meter, and measured photocurrent *I* by measured temperature change $\mathrm {\Delta \theta }$ . "Power", being proportional to *I*2 or *P*2, is also proportional to $(\mathrm {\Delta \theta } )$ 2. Thermal power meters can be built at all frequencies. Hence it is possible to lower the frequency from optical (say 200 THz) to electrical (say 200 MHz). Still there, "Power" must be proportional to $(\mathrm {\Delta \theta } )$ 2 or *P*2. Electrical power *P* is proportional to the square *U*2 of voltage *U*. But "Power" is proportional to *U*4.

These implications are in obvious conflict with ~150 years of physics. They are compelling consequence of calling *F**pnf* a noise factor, or noise figure when expressed in dB.

At any given electrical frequency, noise occurs in both quadratures, i.e. in phase (I) and in quadrature (Q) with the signal. Both these quadratures are available behind the electrical amplifier. The same holds in an optical amplifier. But the direct detection photoreceiver needed for measurement of *SNR**pnf* takes mainly the in-phase noise into account whereas quadrature noise can be neglected for high *n*. Also, the receiver outputs only one baseband signal, corresponding to quadrature. So, one quadrature or degree-of-freedom is lost.

For an optical amplifier with large *G* it holds *F**pnf* ≥ 2 whereas for an *e*lectrical amplifier it holds *F**e* ≥ 1.

Moreover, today's long-haul optical fiber communication is dominated by coherent optical I&Q receivers but *F**pnf* does not describe the SNR degradation observed in these.

Another optical noise figure *F**ase* for *a*mplified *s*pontaneous *e*mission has been defined. But the noise factor *F**ase* is not the SNR degradation factor in any optical receiver.

All the above conflicts are resolved by the optical in-phase and quadrature noise factor and figure *F**o,IQ*. It can be measured using a coherent optical I&Q receiver. In these, power of the output signal is proportional to the square of an optical field amplitude because they are linear in amplitude. They pass both quadratures. For an optical amplifier it holds *F**o,IQ* = *n**sp*(1-1/*G*)+1/*G* ≥ 1. Quantity *n**sp*(1-1/*G*) is the input-referred number of added noise photons per mode.

*F**o,IQ* and *F**pnf* can easily be converted into each other. For large *G* it holds *F**o,IQ* = *F**pnf*/2 or, when expressed in dB, *F**o,IQ* is 3 dB less than *F**pnf*. The ideal *F**o,IQ* in dB equals 0 dB. This describes the known fact that the sensitivity of an ideal optical I&Q receiver is not improved by an ideal optical preamplifier.
