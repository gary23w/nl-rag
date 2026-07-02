---
title: "Orthogonal frequency-division multiplexing (part 1/2)"
source: https://en.wikipedia.org/wiki/Orthogonal_frequency-division_multiplexing
domain: lte-networks
license: CC-BY-SA-4.0
tags: lte network, 4g mobile, evolved packet core, ofdm modulation
fetched: 2026-07-02
part: 1/2
---

# Orthogonal frequency-division multiplexing

In telecommunications, **orthogonal frequency-division multiplexing** (**OFDM**) is a type of digital transmission used in digital modulation for encoding digital (binary) data on multiple carrier frequencies. OFDM has developed into a popular scheme for wideband digital communication, used in applications such as digital television and audio broadcasting, DSL internet access, wireless networks, power line networks, and 4G/5G mobile communications.

OFDM is a frequency-division multiplexing (FDM) scheme that was introduced by Robert W. Chang of Bell Labs in 1966. In OFDM, the incoming bitstream representing the data to be sent is divided into multiple streams. Multiple closely spaced orthogonal subcarrier signals with overlapping spectra are transmitted, with each carrier modulated with bits from the incoming stream so multiple bits are being transmitted in parallel. Demodulation is based on fast Fourier transform algorithms. OFDM was improved by Weinstein and Ebert in 1971 with the introduction of a guard interval, providing better orthogonality in transmission channels affected by multipath propagation. Each subcarrier (signal) is modulated with a conventional modulation scheme (such as quadrature amplitude modulation or phase-shift keying) at a low symbol rate. This maintains total data rates similar to conventional single-carrier modulation schemes in the same bandwidth.

The main advantage of OFDM over single-carrier schemes is its ability to cope with severe channel conditions (for example, attenuation of high frequencies in a long copper wire, narrowband interference and frequency-selective fading due to multipath) without the need for complex equalization filters. Channel equalization is simplified because OFDM may be viewed as using many slowly modulated narrowband signals rather than one rapidly modulated wideband signal. The low symbol rate makes the use of a guard interval between symbols affordable, making it possible to eliminate intersymbol interference (ISI) and use echoes and time-spreading (in analog television visible as ghosting and blurring, respectively) to achieve a diversity gain, i.e. a signal-to-noise ratio improvement. This mechanism also facilitates the design of single frequency networks (SFNs) where several adjacent transmitters send the same signal simultaneously at the same frequency, as the signals from multiple distant transmitters may be re-combined constructively, sparing interference of a traditional single-carrier system.

In **coded orthogonal frequency-division multiplexing** (**COFDM**), forward error correction (convolutional coding) and time/frequency interleaving are applied to the signal being transmitted. This is done to overcome errors in mobile communication channels affected by multipath propagation and Doppler effects. COFDM was introduced by Alard in 1986 for Digital Audio Broadcasting for Eureka Project 147. In practice, OFDM has become used in combination with such coding and interleaving, so that the terms COFDM and OFDM co-apply to common applications.


## Example of applications

The following list is a summary of existing OFDM-based standards and products. For further details, see the Usage section at the end of the article.

### Wired

- ADSL and VDSL broadband access via POTS copper wiring
- DVB-C2, an enhanced version of the DVB-C digital cable TV standard
- Power line communication (PLC)
- ITU-T G.hn, a standard which provides high-speed local area networking of existing home wiring (power lines, phone lines and coaxial cables)
- TrailBlazer telephone line modems
- Multimedia over Coax Alliance (MoCA) home networking
- DOCSIS 3.1 Broadband delivery

### Wireless

- The wireless LAN (WLAN) radio interfaces IEEE 802.11a, g, n, ac, ah and HIPERLAN/2
- The digital radio systems DAB/EUREKA 147, DAB+, Digital Radio Mondiale, HD Radio, T-DMB and ISDB-TSB
- The terrestrial digital TV systems DVB-T and ISDB-T
- The terrestrial mobile TV systems DVB-H, T-DMB, ISDB-T and MediaFLO forward link
- The wireless personal area network (PAN) ultra-wideband (UWB) IEEE 802.15.3a implementation suggested by WiMedia Alliance
- Wi-SUN (Smart Ubiquitous Network)

The OFDM-based multiple access technology OFDMA is also used in several 4G and pre-4G cellular networks, mobile broadband standards, the next generation WLAN and the wired portion of Hybrid fiber-coaxial networks:

- The mobility mode of the wireless MAN/broadband wireless access (BWA) standard IEEE 802.16e (or Mobile-WiMAX)
- The mobile broadband wireless access (MBWA) standard IEEE 802.20
- The downlink of the 3GPP Long-Term Evolution (LTE) fourth generation mobile broadband standard. The radio interface was formerly named *High Speed OFDM Packet Access* (HSOPA), now named Evolved UMTS Terrestrial Radio Access (E-UTRA)
- WLAN IEEE 802.11ax
- DOCSIS 3.1 Upstream


## Key features

The advantages and disadvantages listed below are further discussed in the Characteristics and principles of operation section below.

### Summary of advantages

- High spectral efficiency as compared to other double sideband modulation schemes, spread spectrum, etc.
- Can easily adapt to severe channel conditions without complex time-domain equalization.
- Robust against narrow-band co-channel interference
- Robust against intersymbol interference (ISI) and fading caused by multipath propagation
- Efficient implementation using fast Fourier transform
- Low sensitivity to time synchronization errors
- Tuned sub-channel receiver filters are not required (unlike conventional FDM)
- Facilitates single frequency networks (SFNs) (i.e., transmitter macrodiversity)

### Summary of disadvantages

- Sensitive to Doppler shift
- Sensitive to frequency synchronization problems
- High peak-to-average-power ratio (PAPR), requiring linear transmitter circuitry, which suffers from poor power efficiency
- Loss of efficiency caused by cyclic prefix/guard interval


## Characteristics and principles of operation

### Orthogonality

In OFDM, the subcarrier frequencies are chosen so that the subcarriers are orthogonal to each other, meaning that crosstalk between the sub-channels is eliminated and inter-carrier guard bands are not required. This greatly simplifies the design of both the transmitter and the receiver; unlike conventional FDM, a separate filter for each sub-channel is not required.

The orthogonality requires that the **subcarrier spacing** is $\scriptstyle \Delta f\,=\,{\frac {k}{T_{U}}}$ Hertz, where *T*U seconds is the useful symbol duration (the receiver-side window size), and *k* is a positive integer, typically equal to 1. This stipulates that each carrier frequency undergoes *k* more complete cycles per symbol period than the previous carrier. Therefore, with *N* subcarriers, the total passband bandwidth will be *B* ≈ *N*·Δ*f* (Hz).

The orthogonality also allows high spectral efficiency, with a total symbol rate near the Nyquist rate for the equivalent baseband signal (i.e., near half the Nyquist rate for the double-side band physical passband signal). Almost the whole available frequency band can be used. OFDM generally has a nearly 'white' spectrum, giving it benign electromagnetic interference properties with respect to other co-channel users.

A simple example: A useful symbol duration

T

U

= 1 ms would require a subcarrier spacing of

$\scriptstyle \Delta f\,=\,{\frac {1}{1\,\mathrm {ms} }}\,=\,1\,\mathrm {kHz}$

(or an integer multiple of that) for orthogonality.

N

= 1,000 subcarriers would result in a total passband bandwidth of

N

Δf = 1 MHz. For this symbol time, the required bandwidth in theory according to Nyquist is

$\scriptstyle \mathrm {BW} =R/2=(N/T_{U})/2=0.5\,\mathrm {MHz}$

(half of the achieved bandwidth required by our scheme), where

R

is the bit rate and where

N

= 1,000 samples per symbol by FFT. If a guard interval is applied (see below), Nyquist bandwidth requirement would be even lower. The FFT would result in

N

= 1,000 samples per symbol. If no guard interval was applied, this would result in a base band complex valued signal with a sample rate of 1 MHz, which would require a baseband bandwidth of 0.5 MHz according to Nyquist. However, the passband RF signal is produced by multiplying the baseband signal with a carrier waveform (i.e., double-sideband quadrature amplitude-modulation) resulting in a passband bandwidth of 1 MHz. A single-side band (SSB) or vestigial sideband (VSB) modulation scheme would achieve almost half that bandwidth for the same symbol rate (i.e., twice as high spectral efficiency for the same symbol alphabet length). It is however more sensitive to multipath interference.

OFDM requires very accurate frequency synchronization between the receiver and the transmitter; with frequency deviation the subcarriers will no longer be orthogonal, causing *inter-carrier interference* (ICI) (i.e., cross-talk between the subcarriers). Frequency offsets are typically caused by mismatched transmitter and receiver oscillators, or by Doppler shift due to movement. While Doppler shift alone may be compensated for by the receiver, the situation is worsened when combined with multipath, as reflections will appear at various frequency offsets, which is much harder to correct. This effect typically worsens as speed increases, and is an important factor limiting the use of OFDM in high-speed vehicles. In order to mitigate ICI in such scenarios, one can shape each subcarrier in order to minimize the interference resulting in a non-orthogonal subcarriers overlapping. For example, a low-complexity scheme referred to as WCP-OFDM (*Weighted Cyclic Prefix Orthogonal Frequency-Division Multiplexing*) consists of using short filters at the transmitter output in order to perform a potentially non-rectangular pulse shaping and a near perfect reconstruction using a single-tap per subcarrier equalization. Other ICI suppression techniques usually drastically increase the receiver complexity.

### Implementation using the FFT algorithm

The orthogonality allows for efficient modulator and demodulator implementation using the FFT algorithm on the receiver side, and inverse FFT on the sender side. Although the principles and some of the benefits have been known since the 1960s, OFDM is popular for wideband communications today by way of low-cost digital signal processing components that can efficiently calculate the FFT.

The time to compute the inverse-FFT or FFT has to take less than the time for each symbol, which for example for DVB-T (FFT 8k) means the computation has to be done in 896 µs or less.

For an 8192-point FFT this may be approximated to:

${\begin{aligned}\mathrm {MIPS} &={\frac {\mathrm {computational\ complexity} }{T_{\mathrm {symbol} }}}\times 1.3\times 10^{-6}\\&={\frac {147\;456\times 2}{896\times 10^{-6}}}\times 1.3\times 10^{-6}\\&=428\end{aligned}}$

- MIPS: Million instructions per second

The computational demand approximately scales linearly with FFT size so a double size FFT needs double the amount of time and vice versa. As a comparison an Intel Pentium III CPU at 1.266 GHz is able to calculate a 8192 point FFT in 576 µs using FFTW. Intel Pentium M at 1.6 GHz does it in 387 µs. Intel Core Duo at 3.0 GHz does it in 96.8 µs.

### Guard interval for elimination of intersymbol interference

One key principle of OFDM is that since low symbol rate modulation schemes (i.e., where the symbols are relatively long compared to the channel time characteristics) suffer less from intersymbol interference caused by multipath propagation, it is advantageous to transmit a number of low-rate streams in parallel instead of a single high-rate stream. Since the duration of each symbol is long, it is feasible to insert a guard interval between the OFDM symbols, thus eliminating the intersymbol interference.

The guard interval also eliminates the need for a pulse-shaping filter, and it reduces the sensitivity to time synchronization problems.

A simple example: If one sends a million symbols per second using conventional single-carrier modulation over a wireless channel, then the duration of each symbol would be one microsecond or less. This imposes severe constraints on synchronization and necessitates the removal of multipath interference. If the same million symbols per second are spread among one thousand sub-channels, the duration of each symbol can be longer by a factor of a thousand (i.e., one millisecond) for orthogonality with approximately the same bandwidth. Assume that a guard interval of 1/8 of the symbol length is inserted between each symbol. Intersymbol interference can be avoided if the multipath time-spreading (the time between the reception of the first and the last echo) is shorter than the guard interval (i.e., 125 microseconds). This corresponds to a maximum difference of 37.5 kilometers between the lengths of the paths.

The cyclic prefix, which is transmitted during the guard interval, consists of the end of the OFDM symbol copied into the guard interval, and the guard interval is transmitted followed by the OFDM symbol. The reason that the guard interval consists of a copy of the end of the OFDM symbol is so that the receiver will integrate over an integer number of sinusoid cycles for each of the multipaths when it performs OFDM demodulation with the FFT.

In some standards such as Ultrawideband, in the interest of transmitted power, cyclic prefix is skipped and nothing is sent during the guard interval. The receiver will then have to mimic the cyclic prefix functionality by copying the end part of the OFDM symbol and adding it to the beginning portion.

### Simplified equalization

The effects of frequency-selective channel conditions, for example fading caused by multipath propagation, can be considered as constant (flat) over an OFDM sub-channel if the sub-channel is sufficiently narrow-banded (i.e., if the number of sub-channels is sufficiently large). This makes frequency domain equalization possible at the receiver, which is far simpler than the time-domain equalization used in conventional single-carrier modulation. In OFDM, the equalizer only has to multiply each detected subcarrier (each Fourier coefficient) in each OFDM symbol by a constant complex number, or a rarely changed value. On a fundamental level, simpler digital equalizers are better because they require fewer operations, which translates to fewer round-off errors in the equalizer. Those round-off errors can be viewed as numerical noise and are inevitable.

Our example: The OFDM equalization in the above numerical example would require one complex valued multiplication per subcarrier and symbol (i.e.,

$\scriptstyle N\,=\,1000$

complex multiplications per OFDM symbol; i.e., one million multiplications per second, at the receiver). The FFT algorithm requires

$\scriptstyle N\log _{2}N\,=\,10,000$

[this is imprecise: over half of these complex multiplications are trivial, i.e. = to 1 and are not implemented in software or HW]. complex-valued multiplications per OFDM symbol (i.e., 10 million multiplications per second), at both the receiver and transmitter side. This should be compared with the corresponding one million symbols/second single-carrier modulation case mentioned in the example, where the equalization of 125 microseconds time-spreading using a

FIR filter

would require, in a naive implementation, 125 multiplications per symbol (i.e., 125 million multiplications per second). FFT techniques can be used to reduce the number of multiplications for an

FIR filter

-based time-domain equalizer to a number comparable with OFDM, at the cost of delay between reception and decoding which also becomes comparable with OFDM.

If differential modulation such as DPSK or DQPSK is applied to each subcarrier, equalization can be completely omitted, since these non-coherent schemes are insensitive to slowly changing amplitude and phase distortion.

In a sense, improvements in FIR equalization using FFTs or partial FFTs leads mathematically closer to OFDM, but the OFDM technique is easier to understand and implement, and the sub-channels can be independently adapted in other ways than varying equalization coefficients, such as switching between different QAM constellation patterns and error-correction schemes to match individual sub-channel noise and interference characteristics.

Some of the subcarriers in some of the OFDM symbols may carry pilot signals for measurement of the channel conditions (i.e., the equalizer gain and phase shift for each subcarrier). Pilot signals and training symbols (preambles) may also be used for time synchronization (to avoid intersymbol interference, ISI) and frequency synchronization (to avoid inter-carrier interference, ICI, caused by Doppler shift).

OFDM was initially used for wired and stationary wireless communications. However, with an increasing number of applications operating in highly mobile environments, the effect of dispersive fading caused by a combination of multi-path propagation and doppler shift is more significant. Over the last decade, research has been done on how to equalize OFDM transmission over doubly selective channels.

### Channel coding and interleaving

OFDM is invariably used in conjunction with channel coding (forward error correction), and almost always uses frequency and/or time interleaving.

Frequency (subcarrier) interleaving increases resistance to frequency-selective channel conditions such as fading. For example, when a part of the channel bandwidth fades, frequency interleaving ensures that the bit errors that would result from those subcarriers in the faded part of the bandwidth are spread out in the bit-stream rather than being concentrated. Similarly, time interleaving ensures that bits that are originally close together in the bit-stream are transmitted far apart in time, thus mitigating against severe fading as would happen when travelling at high speed.

However, time interleaving is of little benefit in slowly fading channels, such as for stationary reception, and frequency interleaving offers little to no benefit for narrowband channels that suffer from flat-fading (where the whole channel bandwidth fades at the same time).

The reason why interleaving is used on OFDM is to attempt to spread the errors out in the bit-stream that is presented to the error correction decoder, because when such decoders are presented with a high concentration of errors the decoder is unable to correct all the bit errors, and a burst of uncorrected errors occurs. A similar design of audio data encoding makes compact disc (CD) playback robust.

A classical type of error correction coding used with OFDM-based systems is convolutional coding, often concatenated with Reed-Solomon coding. Usually, additional interleaving (on top of the time and frequency interleaving mentioned above) in between the two layers of coding is implemented. The choice for Reed-Solomon coding as the outer error correction code is based on the observation that the Viterbi decoder used for inner convolutional decoding produces short error bursts when there is a high concentration of errors, and Reed-Solomon codes are inherently well suited to correcting bursts of errors.

Newer systems, however, usually now adopt near-optimal types of error correction codes that use the turbo decoding principle, where the decoder iterates towards the desired solution. Examples of such error correction coding types include turbo codes and LDPC codes, which perform close to the Shannon limit for the Additive White Gaussian Noise (AWGN) channel. Some systems that have implemented these codes have concatenated them with either Reed-Solomon (for example on the MediaFLO system) or BCH codes (on the DVB-S2 system) to improve upon an error floor inherent to these codes at high signal-to-noise ratios.

### Adaptive transmission

The resilience to severe channel conditions can be further enhanced if information about the channel is sent over a return-channel. Based on this feedback information, adaptive modulation, channel coding and power allocation may be applied across all subcarriers, or individually to each subcarrier. In the latter case, if a particular range of frequencies suffers from interference or attenuation, the carriers within that range can be disabled or made to run slower by applying more robust modulation or error coding to those subcarriers.

The term **discrete multitone modulation** (**DMT**) denotes OFDM-based communication systems that adapt the transmission to the channel conditions individually for each subcarrier, by means of so-called *bit-loading*. Examples are ADSL and VDSL.

The upstream and downstream speeds can be varied by allocating either more or fewer carriers for each purpose. Some forms of rate-adaptive DSL use this feature in real time, so that the bitrate is adapted to the co-channel interference and bandwidth is allocated to whichever subscriber needs it most.

### OFDM extended with multiple access

OFDM in its primary form is considered as a digital modulation technique, and not a multi-user channel access method, since it is used for transferring one bit stream over one communication channel using one sequence of OFDM symbols. However, OFDM can be combined with multiple access using time, frequency or coding separation of the users.

In orthogonal frequency-division multiple access (OFDMA), frequency-division multiple access is achieved by assigning different OFDM sub-channels to different users. OFDMA supports differentiated quality of service by assigning different number of subcarriers to different users in a similar fashion as in CDMA, and thus complex packet scheduling or medium access control schemes can be avoided. OFDMA is used in:

- the mobility mode of the IEEE 802.16 Wireless MAN standard, commonly referred to as WiMAX,
- the IEEE 802.20 mobile Wireless MAN standard, commonly referred to as MBWA,
- the 3GPP Long-Term Evolution (LTE) fourth generation mobile broadband standard downlink. The radio interface was formerly named High Speed OFDM Packet Access (HSOPA), now named Evolved UMTS Terrestrial Radio Access (E-UTRA).
- the 3GPP 5G NR (New Radio) fifth generation mobile network standard downlink and uplink. 5G NR is the successor to LTE.
- the now defunct Qualcomm/3GPP2 Ultra Mobile Broadband (UMB) project, intended as a successor of CDMA2000, but replaced by LTE.

OFDMA is also a candidate access method for the IEEE 802.22 *Wireless Regional Area Networks* (WRAN). The project aims at designing the first cognitive radio-based standard operating in the VHF-low UHF spectrum (TV spectrum).

- the most recent amendment of 802.11 standard, namely 802.11ax, includes OFDMA for high efficiency and simultaneous communication.

In multi-carrier code-division multiple access (MC-CDMA), also known as OFDM-CDMA, OFDM is combined with CDMA spread spectrum communication for coding separation of the users. Co-channel interference can be mitigated, meaning that manual fixed channel allocation (FCA) frequency planning is simplified, or complex dynamic channel allocation (DCA) schemes are avoided.

### Space diversity

In OFDM-based wide-area broadcasting, receivers can benefit from receiving signals from several spatially dispersed transmitters simultaneously, since transmitters will only destructively interfere with each other on a limited number of subcarriers, whereas in general they will actually reinforce coverage over a wide area. This is very beneficial in many countries, as it permits the operation of national single-frequency networks (SFN), where many transmitters send the same signal simultaneously over the same channel frequency. SFNs use the available spectrum more effectively than conventional multi-frequency broadcast networks (MFN), where program content is replicated on different carrier frequencies. SFNs also result in a diversity gain in receivers situated midway between the transmitters. The coverage area is increased and the outage probability decreased in comparison to an MFN, due to increased received signal strength averaged over all subcarriers.

Although the guard interval only contains redundant data, which means that it reduces the capacity, some OFDM-based systems, such as some of the broadcasting systems, deliberately use a long guard interval in order to allow the transmitters to be spaced farther apart in an SFN, and longer guard intervals allow larger SFN cell-sizes. A rule of thumb for the maximum distance between transmitters in an SFN is equal to the distance a signal travels during the guard interval — for instance, a guard interval of 200 microseconds would allow transmitters to be spaced 60 km apart.

A *single frequency network* is a form of transmitter macrodiversity. The concept can be further used in *dynamic single-frequency networks* (DSFN), where the SFN grouping is changed from timeslot to timeslot.

OFDM may be combined with other forms of space diversity, for example antenna arrays and MIMO channels. This is done in the IEEE 802.11 Wireless LAN standards.

### Linear transmitter power amplifier

An OFDM signal exhibits a high peak-to-average power ratio (PAPR) because the independent phases of the subcarriers mean that they will often combine constructively. Handling this high PAPR requires:

- A high-resolution digital-to-analog converter (DAC) in the transmitter
- A high-resolution analog-to-digital converter (ADC) in the receiver
- A linear signal chain

Any non-linearity in the signal chain will cause intermodulation distortion that

- Raises the noise floor
- May cause inter-carrier interference
- Generates out-of-band spurious radiation

The linearity requirement is demanding, especially for transmitter RF output circuitry where amplifiers are often designed to be non-linear in order to minimise power consumption. In practical OFDM systems a small amount of peak clipping is allowed to limit the PAPR in a judicious trade-off against the above consequences. However, the transmitter output filter which is required to reduce out-of-band spurs to legal levels has the effect of restoring peak levels that were clipped, so clipping is not an effective way to reduce PAPR.

Although the spectral efficiency of OFDM is attractive for both terrestrial and space communications, the high PAPR requirements have so far limited OFDM applications to terrestrial systems.

The crest factor CF (in dB) for an OFDM system with *n* uncorrelated subcarriers is

$CF=10\log _{10}(n)+CF_{c}$

where CFc is the crest factor (in dB) for each subcarrier. (CFc is 3.01 dB for the sine waves used for BPSK and QPSK modulation).

For example, the DVB-T signal in 2K mode is composed of 1705 subcarriers that are each QPSK-modulated, giving a crest factor of 35.32 dB.

Many PAPR (or crest factor) reduction techniques have been developed, for instance, based on iterative clipping. Over the years, numerous model-driven approaches have been proposed to reduce the PAPR in communication systems. In recent years, there has been a growing interest in exploring data-driven models for PAPR reduction as part of ongoing research in end-to-end communication networks. These data-driven models offer innovative solutions and new avenues of exploration to address the challenges posed by high PAPR effectively. By leveraging data-driven techniques, researchers aim to enhance the performance and efficiency of communication networks by optimizing power utilization.

The dynamic range required for an FM receiver is 120 dB while DAB only require about 90 dB. As a comparison, each extra bit per sample increases the dynamic range by 6 dB.


## Efficiency comparison between single carrier and multicarrier

The performance of any communication system can be measured in terms of its power efficiency and bandwidth efficiency. The power efficiency describes the ability of communication system to preserve bit error rate (BER) of the transmitted signal at low power levels. Bandwidth efficiency reflects how efficiently the allocated bandwidth is used and is defined as the throughput data rate per hertz in a given bandwidth. If the large number of subcarriers are used, the bandwidth efficiency of multicarrier system such as OFDM with using optical fiber channel is defined as

$\eta =2{\frac {R_{s}}{B_{\text{OFDM}}}}$

where $R_{s}$ is the symbol rate in giga-symbols per second (Gsps), $B_{\text{OFDM}}$ is the bandwidth of OFDM signal, and the factor of 2 is due to the two polarization states in the fiber.

There is saving of bandwidth by using multicarrier modulation with orthogonal frequency-division multiplexing. So the bandwidth for multicarrier system is less in comparison with single carrier system and hence bandwidth efficiency of multicarrier system is larger than single carrier system.

| S. no. | Transmission type | M in M-QAM | No. of subcarriers | Bit rate | Fiber length | Received power, at BER of 10−9 | Bandwidth efficiency |
|---|---|---|---|---|---|---|---|
| 1 | Single carrier | 64 | 1 | 10 Gbit/s | 20 km | −37.3 dBm | 6.0000 |
| 2 | Multicarrier | 64 | 128 | 10 Gbit/s | 20 km | −36.3 dBm | 10.6022 |

There is only 1 dB increase in receiver power, but we get 76.7% improvement in bandwidth efficiency with using multicarrier transmission technique.


## Idealized system model

This section describes a simple idealized OFDM system model suitable for a time-invariant AWGN channel.

### Transmitter

An OFDM carrier signal is the sum of a number of orthogonal subcarriers, with baseband data on each subcarrier being independently modulated commonly using some type of quadrature amplitude modulation (QAM) or phase-shift keying (PSK). This composite baseband signal is typically used to modulate a main RF carrier.

$s[n]$ is a serial stream of binary digits. By inverse multiplexing, these are first demultiplexed into N parallel streams, and each one mapped to a (possibly complex) symbol stream using some modulation constellation (QAM, PSK, etc.). Note that the constellations may be different, so some streams may carry a higher bit-rate than others.

An inverse FFT is computed on each set of symbols, giving a set of complex time-domain samples. These samples are then quadrature-mixed to passband in the standard way. The real and imaginary components are first converted to the analogue domain using digital-to-analogue converters (DACs); the analogue signals are then used to modulate cosine and sine waves at the carrier frequency, $f_{\text{c}}$ , respectively. These signals are then summed to give the transmission signal, $s(t)$ .

### Receiver

The receiver picks up the signal $r(t)$ , which is then quadrature-mixed down to baseband using cosine and sine waves at the carrier frequency. This also creates signals centered on $2f_{\text{c}}$ , so low-pass filters are used to reject these. The baseband signals are then sampled and digitised using analog-to-digital converters (ADCs), and a forward FFT is used to convert back to the frequency domain.

This returns N parallel streams, each of which is converted to a binary stream using an appropriate symbol detector. These streams are then re-combined into a serial stream, ${\hat {s}}[n]$ , which is an estimate of the original binary stream at the transmitter.


## Mathematical description

If N subcarriers are used, and each subcarrier is modulated using M alternative symbols, the OFDM symbol alphabet consists of $M^{N}$ combined symbols.

The low-pass equivalent OFDM filter is expressed as:

$\nu (t)=\sum _{k=0}^{N-1}X_{k}e^{j2\pi kt/T},\quad 0\leq t<T,$

where $\{X_{k}\}$ are the data symbols, N is the number of subcarriers, and T is the OFDM symbol time. The subcarrier spacing of ${\textstyle {\frac {1}{T}}}$ makes them orthogonal over each symbol period; this property is expressed as:

${\begin{aligned}&{\frac {1}{T}}\int _{0}^{T}\left(e^{j2\pi k_{1}t/T}\right)^{*}\left(e^{j2\pi k_{2}t/T}\right)dt\\{}={}&{\frac {1}{T}}\int _{0}^{T}e^{j2\pi \left(k_{2}-k_{1}\right)t/T}dt=\delta _{k_{1}k_{2}}\end{aligned}}$

where $(\cdot )^{*}$ denotes the complex conjugate operator and $\delta \,$ is the Kronecker delta.

To avoid intersymbol interference in multipath fading channels, a guard interval of length $T_{\text{g}}$ is inserted prior to the OFDM block. During this interval, a *cyclic prefix* is transmitted such that the signal in the interval $-T_{\text{g}}\leq t<0$ equals the signal in the interval $(T-T_{\text{g}})\leq t<T$ . The OFDM signal with cyclic prefix is thus:

$\nu (t)=\sum _{k=0}^{N-1}X_{k}e^{j2\pi kt/T},\quad -T_{\text{g}}\leq t<T$

The low-pass signal filter above can be either real or complex-valued. Real-valued low-pass equivalent signals are typically transmitted at baseband—wireline applications such as DSL use this approach. For wireless applications, the low-pass signal is typically complex-valued; in which case, the transmitted signal is up-converted to a carrier frequency $f_{\text{c}}$ . In general, the transmitted signal can be represented as:

${\begin{aligned}s(t)&=\Re \left\{\nu (t)e^{j2\pi f_{c}t}\right\}\\&=\sum _{k=0}^{N-1}|X_{k}|\cos \left(2\pi \left[f_{\text{c}}+{\frac {k}{T}}\right]t+\arg[X_{k}]\right)\end{aligned}}$


## Usage

OFDM is used in:

- Digital Radio Mondiale (DRM)
- Digital Audio Broadcasting (DAB)
- Digital television DVB-T/T2 (terrestrial), ATSC 3.0 (terrestrial), DVB-H (handheld), DMB-T/H, DVB-C2 (cable)
- Wireless LAN IEEE 802.11a, IEEE 802.11g, IEEE 802.11n, IEEE 802.11ac, and IEEE 802.11ad
- WiMAX
- Li-Fi
- ADSL (G.dmt/ITU G.992.1)
- LTE and LTE Advanced 4G mobile networks
- DECT cordless phones
- Modern narrow and broadband power line communications

### OFDM system comparison table

Key features of some common OFDM-based systems are presented in the following table.

| Standard name | DAB Eureka 147 | DVB-T | DVB-H | DTMB | DVB-T2 | IEEE 802.11a |
|---|---|---|---|---|---|---|
| Year ratified | 1995 | 1997 | 2004 | 2006 | 2007 | 1999 |
| Frequency range of today's equipment (MHz) | 174–240, 1,452–1,492 | 470–862, 174–230 | 470–862 | 48–870 |   | 4,915–6,100 |
| Channel spacing, *B* (MHz) | 1.712 | 6, 7, 8 | 5, 6, 7, 8 | 6, 7, 8 | 1.7, 5, 6, 7, 8, 10 | 20 |
| FFT size, k = 1,024 | Mode I: 2k Mode II: 512 Mode III: 256 Mode IV: 1k | 2k, 8k | 2k, 4k, 8k | 1 (single-carrier) 4k (multi-carrier) | 1k, 2k, 4k, 8k, 16k, 32k | 64 |
| Number of non-silent subcarriers, *N* | Mode I: 1,536 Mode II: 384 Mode III: 192 Mode IV: 768 | 2K mode: 1,705 8K mode: 6,817 | 1,705, 3,409, 6,817 | 1 (single-carrier) 3,780 (multi-carrier) | 853–27,841 (1K normal to 32K extended carrier mode) | 52 |
| Subcarrier modulation scheme | π⁄4-DQPSK | QPSK, 16QAM, 64QAM | QPSK, 16QAM, 64QAM | 4QAM, 4QAM-NR, 16QAM, 32QAM, 64QAM | QPSK, 16QAM, 64QAM, 256QAM | BPSK, QPSK, 16QAM, 64QAM |
| Useful symbol length, *TU* (μs) | Mode I: 1,000 Mode II: 250 Mode III: 125 Mode IV: 500 | 2K mode: 224 8K mode: 896 | 224, 448, 896 | 500 (multi-carrier) | 112–3,584 (1K to 32K mode on 8 MHz channel) | 3.2 |
| Additional guard interval, *TG*/*TU* | 24.6% (all modes) | 1⁄4, 1⁄8, 1⁄16, 1⁄32 | 1⁄4, 1⁄8, 1⁄16, 1⁄32 | 1⁄4, 1⁄6, 1⁄9 | 1/128, 1/32, 1/16, 19/256, 1/8, 19/128, 1/4 (for 32k mode maximum 1/8) | 1⁄4 |
| Subcarrier spacing, ${\textstyle \Delta f={\frac {1}{T_{U}}}\approx {\frac {B}{N}}}$ (Hz) | Mode I: 1,000 Mode II: 4,000 Mode III: 8,000 Mode IV: 2,000 | 2K mode: 4,464 8K mode: 1,116 | 4,464, 2,232, 1,116 | 8 M (single-carrier) 2,000 (multi-carrier) | 279–8,929 (32K down to 1K mode) | 312.5 K |
| Net bit rate, *R* (Mbit/s) | 0.576–1.152 | 4.98–31.67 (typ. 24.13) | 3.7–23.8 | 4.81–32.49 | Typically 35.4 | 6–54 |
| Link spectral efficiency, *R*/*B* (bit/s·Hz) | 0.34–0.67 | 0.62–4.0 (typ. 3.0) | 0.62–4.0 | 0.60–4.1 | 0.87–6.65 | 0.30–2.7 |
| Inner FEC | Conv. coding with equal error protection code rates: 1⁄4, 3⁄8, 4⁄9, 1⁄2, 4⁄7, 2⁄3, 3⁄4, 4⁄5 Unequal error protection with avg. code rates of: ~0.34, 0.41, 0.50, 0.60, and 0.75 | Conv. coding with code rates: 1⁄2, 2⁄3, 3⁄4, 5⁄6, or 7⁄8 | Conv. coding with code rates: 1⁄2, 2⁄3, 3⁄4, 5⁄6, or 7⁄8 | LDPC with code rates: 0.4, 0.6, or 0.8 | LDPC: 1⁄2, 3⁄5, 2⁄3, 3⁄4, 4⁄5, 5⁄6 | Conv. coding with code rates: 1⁄2, 2⁄3, or 3⁄4 |
| Outer FEC | Optional RS (120, 110, t = 5) | RS (204, 188, t = 8) | RS (204, 188, t = 8) + MPE-FEC | BCH code (762, 752) | BCH code | None |
| Maximum travelling speed (km/h) | 200–600 | 53–185, varies with transmission frequency |   |   |   |   |
| Time interleaving depth (ms) | 384 | 0.6–3.5 | 0.6–3.5 | 200–500 | Up to 250 (500 with extension frame) |   |
| Adaptive transmission | None | None | None |   | None |   |
| Multiple access method | None | None | None |   | None |   |
| Typical source coding | 192 kbit/s MPEG2 Audio layer 2 | 2–18 Mbit/s Standard – HDTV H.264 or MPEG2 | H.264 | Not defined (video: MPEG-2, H.264, H.265 and/or AVS+; audio: MP2 or DRA or AC-3) | H.264 or MPEG2 (audio: AAC HE, Dolby Digital AC-3 (A52), MPEG-2 AL 2) |   |

### ADSL

OFDM is used in ADSL connections that follow the ANSI T1.413 and G.dmt (ITU G.992.1) standards, where it is called *discrete multitone modulation* (DMT). DSL achieves high-speed data connections on existing copper wires. OFDM is also used in the successor standards ADSL2, ADSL2+, VDSL, VDSL2, and G.fast. ADSL2 uses variable subcarrier modulation, ranging from BPSK to 32768QAM (in ADSL terminology this is referred to as bit-loading, or bit per tone, 1 to 15 bits per subcarrier).

Long copper wires suffer from attenuation at high frequencies. The fact that OFDM can cope with this frequency selective attenuation and with narrow-band interference are the main reasons it is frequently used in applications such as ADSL modems.

### Powerline Technology

OFDM is used by many powerline devices to extend digital connections through power wiring. Adaptive modulation is particularly important with such a noisy channel as electrical wiring. Some medium speed smart metering modems, "Prime" and "G3" use OFDM at modest frequencies (30–100 kHz) with modest numbers of channels (several hundred) in order to overcome the intersymbol interference in the power line environment. The IEEE 1901 standards include two incompatible physical layers that both use OFDM. The ITU-T G.hn standard, which provides high-speed local area networking over existing home wiring (power lines, phone lines and coaxial cables) is based on a PHY layer that specifies OFDM with adaptive modulation and a Low-Density Parity-Check (LDPC) FEC code.

### Wireless local area networks (LAN) and metropolitan area networks (MAN)

OFDM is extensively used in wireless LAN and MAN applications, including IEEE 802.11a/g/n and WiMAX.

IEEE 802.11a/g/n, operating in the 2.4 and 5 GHz bands, specifies per-stream airside data rates ranging from 6 to 54 Mbit/s. If both devices can use "HT mode" (added with 802.11n), the top 20 MHz per-stream rate is increased to 72.2 Mbit/s, with the option of data rates between 13.5 and 150 Mbit/s using a 40 MHz channel. Four different modulation schemes are used: BPSK, QPSK, 16-QAM, and 64-QAM, along with a set of error correcting rates (1/2–5/6). The multitude of choices allows the system to adapt the optimum data rate for the current signal conditions.

### Wireless personal area networks (PAN)

OFDM is also now being used in the WiMedia/Ecma-368 standard for high-speed wireless personal area networks in the 3.1–10.6 GHz ultrawideband spectrum (see MultiBand-OFDM).

### Terrestrial digital radio and television broadcasting

Much of Europe and Asia has adopted OFDM for terrestrial broadcasting of digital television (DVB-T, DVB-H and T-DMB) and radio (EUREKA 147 DAB, Digital Radio Mondiale, HD Radio and T-DMB).

#### DVB-T

By Directive of the European Commission, all television services transmitted to viewers in the European Community must use a transmission system that has been standardized by a recognized European standardization body, and such a standard has been developed and codified by the DVB Project, *Digital Video Broadcasting (DVB); Framing structure, channel coding and modulation for digital terrestrial television*. Customarily referred to as DVB-T, the standard calls for the exclusive use of COFDM for modulation. DVB-T is now widely used in Europe and elsewhere for terrestrial digital TV.

#### SDARS

The ground segments of the Digital Audio Radio Service (SDARS) systems used by XM Satellite Radio and Sirius Satellite Radio are transmitted using Coded OFDM (COFDM). The word "coded" comes from the use of forward error correction (FEC).

#### COFDM vs VSB

The question of the relative technical merits of COFDM versus 8VSB for terrestrial digital television has been a subject of some controversy, especially between European and North American technologists and regulators. The United States has rejected several proposals to adopt the COFDM-based DVB-T system for its digital television services, and for many years has opted to use 8VSB (vestigial sideband modulation) exclusively for terrestrial digital television. However, in November 2017, the FCC approved a voluntary transition to ATSC 3.0, a new broadcast standard which is based on COFDM. Unlike the first digital television transition in America, TV stations will not be assigned separate frequencies to transmit ATSC 3.0 and are not required to switch to ATSC 3.0 by any deadline. Televisions sold in the U.S. are also not required to include ATSC 3.0 tuning capabilities. Full-powered television stations are permitted to make the switch to ATSC 3.0, as long as they continue to make their main channel available through a simulcast agreement with another in-market station (with a similar coverage area) through at least November 2022.

One of the major benefits provided by COFDM is in rendering radio broadcasts relatively immune to multipath distortion and signal fading due to atmospheric conditions or passing aircraft. Proponents of COFDM argue it resists multipath far better than 8VSB. Early 8VSB DTV (digital television) receivers often had difficulty receiving a signal. Also, COFDM allows single-frequency networks, which is not possible with 8VSB.

However, newer 8VSB receivers are far better at dealing with multipath, hence the difference in performance may diminish with advances in equalizer design.

#### Digital radio

COFDM is also used for other radio standards, for Digital Audio Broadcasting (DAB), the standard for digital audio broadcasting at VHF frequencies, for Digital Radio Mondiale (DRM), the standard for digital broadcasting at shortwave and medium wave frequencies (below 30 MHz) and for DRM+ a more recently introduced standard for digital audio broadcasting at VHF frequencies. (30 to 174 MHz)

The United States again uses an alternate standard, a proprietary system developed by iBiquity dubbed *HD Radio*. However, it uses COFDM as the underlying broadcast technology to add digital audio to AM (medium wave) and FM broadcasts.

Both Digital Radio Mondiale and HD Radio are classified as in-band on-channel systems, unlike Eureka 147 (DAB: Digital Audio Broadcasting) which uses separate VHF or UHF frequency bands instead.

#### BST-OFDM used in ISDB

The *band-segmented transmission orthogonal frequency-division multiplexing* (*BST-OFDM*) system proposed for Japan (in the ISDB-T, ISDB-TSB, and ISDB-C broadcasting systems) improves upon COFDM by exploiting the fact that some OFDM carriers may be modulated differently from others within the same multiplex. Some forms of COFDM already offer this kind of hierarchical modulation, though BST-OFDM is intended to make it more flexible. The 6 MHz television channel may therefore be "segmented", with different segments being modulated differently and used for different services.

It is possible, for example, to send an audio service on a segment that includes a segment composed of a number of carriers, a data service on another segment and a television service on yet another segment—all within the same 6 MHz television channel. Furthermore, these may be modulated with different parameters so that, for example, the audio and data services could be optimized for mobile reception, while the television service is optimized for stationary reception in a high-multipath environment.

### Ultra-wideband

Ultra-wideband (UWB) wireless personal area network technology may also use OFDM, such as in Multiband OFDM (MB-OFDM). This UWB specification is advocated by the WiMedia Alliance (formerly by both the Multiband OFDM Alliance [MBOA] and the WiMedia Alliance, but the two have now merged), and is one of the competing UWB radio interfaces.

### Flash-OFDM

*Fast low-latency access with seamless handoff orthogonal frequency-division multiplexing* (Flash-OFDM), also referred to as F-OFDM, was based on OFDM and also specified higher protocol layers. It was developed by Flarion, and purchased by Qualcomm in January 2006. Flash-OFDM was marketed as a packet-switched cellular bearer, to compete with GSM and 3G networks. As an example, 450 MHz frequency bands previously used by NMT-450 and C-Net C450 (both 1G analogue networks, now mostly decommissioned) in Europe are being licensed to Flash-OFDM operators.

In Finland, the license holder Digita began deployment of a nationwide "@450" wireless network in parts of the country since April 2007. It was purchased by Datame in 2011. In February 2012 Datame announced they would upgrade the 450 MHz network to competing CDMA2000 technology.

Slovak Telekom in Slovakia offers Flash-OFDM connections with a maximum downstream speed of 5.3 Mbit/s, and a maximum upstream speed of 1.8 Mbit/s, with a coverage of over 70 percent of Slovak population. The Flash-OFDM network was switched off in the majority of Slovakia on 30 September 2015.

T-Mobile Germany used Flash-OFDM to backhaul Wi-Fi HotSpots on the Deutsche Bahn's ICE high speed trains between 2005 and 2015, until switching over to UMTS and LTE.

American wireless carrier Nextel Communications field tested wireless broadband network technologies including Flash-OFDM in 2005. Sprint purchased the carrier in 2006 and decided to deploy the mobile version of WiMAX, which is based on Scalable Orthogonal Frequency-Division Multiple Access (SOFDMA) technology.

Citizens Telephone Cooperative launched a mobile broadband service based on Flash-OFDM technology to subscribers in parts of Virginia in March 2006. The maximum speed available was 1.5 Mbit/s. The service was discontinued on April 30, 2009.
