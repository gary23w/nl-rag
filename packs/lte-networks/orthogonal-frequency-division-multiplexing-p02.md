---
title: "Orthogonal frequency-division multiplexing (part 2/2)"
source: https://en.wikipedia.org/wiki/Orthogonal_frequency-division_multiplexing
domain: lte-networks
license: CC-BY-SA-4.0
tags: lte network, 4g mobile, evolved packet core, ofdm modulation
fetched: 2026-07-02
part: 2/2
---

## Vector OFDM (VOFDM)

VOFDM was proposed by Xiang-Gen Xia in 2000 (*Proceedings of ICC 2000*, New Orleans, and *IEEE Trans. on Communications*, Aug. 2001) for single transmit antenna systems. VOFDM replaces each scalar value in the conventional OFDM by a vector value and is a bridge between OFDM and the single carrier frequency domain equalizer (SC-FDE). When the vector size is 1 , it is OFDM and when the vector size is at least the channel length and the FFT size is 1 , it is SC-FDE.

In VOFDM, assume M is the vector size, and each scalar-valued signal $X_{n}$ in OFDM is replaced by a vector-valued signal ${\bf {X}}_{n}$ of vector size M , $0\leq n\leq N-1$ . One takes the N -point IFFT of ${\bf {X}}_{n},0\leq n\leq N-1$ , component-wisely and gets another vector sequence of the same vector size M , ${\bf {x}}_{k},0\leq k\leq N-1$ . Then, one adds a vector CP of length $\Gamma$ to this vector sequence as

${\bf {x}}_{0},{\bf {x}}_{1},...,{\bf {x}}_{N-1},{\bf {x}}_{0},{\bf {x}}_{1},...,{\bf {x}}_{\Gamma -1}$

.

This vector sequence is converted to a scalar sequence by sequentializing all the vectors of size M , which is transmitted at a transmit antenna sequentially.

At the receiver, the received scalar sequence is first converted to the vector sequence of vector size M . When the CP length satisfies ${\textstyle \Gamma \geq \left\lceil {\frac {L}{M}}\right\rceil }$ , then, after the vector CP is removed from the vector sequence and the N -point FFT is implemented component-wisely to the vector sequence of length N , one obtains

${\bf {Y}}_{n}={\bf {H}}_{n}{\bf {X}}_{n}+{\bf {W}}_{n},\,\,0\leq n\leq N-1,\,\,\,\,\,\,\,\,\,\,\,\,\,\,(1)$

where ${\bf {W}}_{n}$ are additive white noise and ${\textstyle {\bf {H}}_{n}={\bf {H}}{\mathord {\left(\exp {\mathord {\left({\frac {2\pi jn}{N}}\right)}}\right)}}={\bf {H}}(z)|_{z=\exp(2\pi jn/N)}}$ and ${\bf {H}}(z)$ is the following $M\times M$ polyphase matrix of the ISI channel ${\textstyle H(z)=\sum _{k=0}^{L}h_{k}z^{-k}}$ :

$\mathbf {H} (z)=\left[{\begin{array}{cccc}H_{0}(z)&z^{-1}H_{M-1}(z)&\cdots &z^{-1}H_{1}(z)\\H_{1}(z)&H_{0}(z)&\cdots &z^{-1}H_{2}(z)\\\vdots &\vdots &\vdots &\vdots \\H_{M-1}(z)&H_{M-2}(z)&\cdots &H_{0}(z)\end{array}}\right]$

,

where ${\textstyle H_{m}(z)=\sum _{l}h_{Ml+m}z^{-l}}$ is the m th polyphase component of the channel $H(z),0\leq m\leq M-1$ . From (1), one can see that the original ISI channel is converted to N many vector subchannels of vector size M . There is no ISI across these vector subchannels but there is ISI inside each vector subchannel. In each vector subchannel, at most M many symbols are interfered each other. Clearly, when the vector size $M=1$ , the above VOFDM returns to OFDM and when $M>L$ and $N=1$ , it becomes the SC-FDE. The vector size M is a parameter that one can choose freely and properly in practice and controls the ISI level. There may be a trade-off between vector size M , demodulation complexity at the receiver, and FFT size, for a given channel bandwidth. Equation (1) is mathematically new for an ISI channel, when the vector size $M>1$ .

Note that the length of the CP part in the sequential form does not have to be an integer multiple of the vector size, $\Gamma M$ . One can truncate the above vectorized CP to a sequential CP of length not less than the ISI channel length, which will not affect the above demodulation.

Also note that there exist many other different generalizations/forms of OFDM, to see their essential differences, it is critical to see their corresponding received signal equations to demodulate. The above VOFDM is the earliest and the only one that achieves the received signal equation (1) and/or its equivalent form, although it may have different implementations at transmitter vs. different IFFT algorithms.

It has been shown (Yabo Li et al., *IEEE Trans. on Signal Processing*, Oct. 2012) that applying the MMSE linear receiver to each vector subchannel (1), it achieves multipath diversity and/or signal space diversity. This is because the vectorized channel matrices in (1) are pseudo-circulant and can be diagonalized by the M -point DFT/IDFT matrix with some diagonal phase shift matrices. Then, the right hand side DFT/IDFT matrix and the k th diagonal phase shift matrix in the diagonalization can be thought of the precoding to the input information symbol vector ${\bf {X}}_{k}$ in the k th sub vector channel, and all the vectorized subchannels become diagonal channels of M discrete frequency components from the $MN$ -point DFT of the original ISI channel. It may collect the multipath diversity and/or signal space diversity similar to the precoding to collect the signal space diversity for single antenna systems to combat wireless fading or the diagonal space-time block coding to collect the spatial diversity for multiple antenna systems. The details are referred to the IEEE TCOM and IEEE TSP papers mentioned above.


## Wavelet-OFDM

OFDM has become an interesting technique for power line communications (PLC). In this area of research, a wavelet transform is introduced to replace the DFT as the method of creating orthogonal frequencies. This is due to the advantages wavelets offer, which are particularly useful on noisy power lines.

Instead of using an IDFT to create the sender signal, the wavelet OFDM uses a synthesis bank consisting of a N -band transmultiplexer followed by the transform function

$F_{n}(z)=\sum _{k=0}^{L-1}f_{n}(k)z^{-k},\quad 0\leq n<N$

On the receiver side, an analysis bank is used to demodulate the signal again. This bank contains an inverse transform

$G_{n}(z)=\sum _{k=0}^{L-1}g_{n}(k)z^{-k},\quad 0\leq n<N$

followed by another N -band transmultiplexer. The relationship between both transform functions is

${\begin{aligned}f_{n}(k)&=g_{n}(L-1-k)\\F_{n}(z)&=z^{-(L-1)}G_{n}*(z-1)\end{aligned}}$

An example of W-OFDM uses the Perfect Reconstruction Cosine Modulated Filter Bank (PR-CMFB) and Extended Lapped Transform (ELT) is used for the wavelet TF. Thus, $\textstyle f_{n}(k)$ and $\textstyle g_{n}(k)$ are given as

${\begin{aligned}f_{n}(k)&=2p_{0}(k)\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}\right)\left(k-{\frac {L-1}{2}}\right)-(-1)^{n}{\frac {\pi }{4}}\right]\\g_{n}(k)&=2p_{0}(k)\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}\right)\left(k-{\frac {L-1}{2}}\right)+(-1)^{n}{\frac {\pi }{4}}\right]\\P_{0}(z)&=\sum _{k=0}^{N-1}z^{-k}Y_{k}\left(z^{2N}\right)\end{aligned}}$

These two functions are their respective inverses, and can be used to modulate and demodulate a given input sequence. Just as in the case of DFT, the wavelet transform creates orthogonal waves with $\textstyle f_{0}$ , $\textstyle f_{1}$ , ..., $\textstyle f_{N-1}$ . The orthogonality ensures that they do not interfere with each other and can be sent simultaneously. At the receiver, $\textstyle g_{0}$ , $\textstyle g_{1}$ , ..., $\textstyle g_{N-1}$ are used to reconstruct the data sequence once more.

### Advantages over standard OFDM

W-OFDM is an evolution of the standard OFDM, with certain advantages.

Mainly, the sidelobe levels of W-OFDM are lower. This results in less ICI, as well as greater robustness to narrowband interference. These two properties are especially useful in PLC, where most of the lines aren't shielded against EM-noise, which creates noisy channels and noise spikes.

A comparison between the two modulation techniques also reveals that the complexity of both algorithms remains approximately the same.


## Other orthogonal transforms

The vast majority of implementations of OFDM use the fast Fourier transform (FFT). However, there exist other orthogonal transforms that can be used. For example, OFDM systems based on the discrete Hartley transform (DHT) and the wavelet transform have been investigated.


## History

- 1957: Kineplex, multi-carrier HF modem (R.R. Mosier & R.G. Clabaugh)
- 1966: Chang, Bell Labs: OFDM paper and patent
- 1971: Weinstein & Ebert proposed use of FFT and guard interval
- 1985: Cimini described use of OFDM for mobile communications
- 1985: Telebit Trailblazer Modem introduced a 512 carrier Packet Ensemble Protocol (18 432 bit/s)
- 1987: Alard & Lasalle: COFDM for digital broadcasting
- 1988: In September TH-CSF LER, first experimental Digital TV link in OFDM, Paris area
- 1989: OFDM international patent application
- October 1990: TH-CSF LER, first OFDM equipment field test, 34 Mbit/s in an 8 MHz channel, experiments in Paris area
- December 1990: TH-CSF LER, first OFDM test bed comparison with VSB in Princeton USA
- September 1992: TH-CSF LER, second generation equipment field test, 70 Mbit/s in an 8 MHz channel, twin polarisations. Wuppertal, Germany
- October 1992: TH-CSF LER, second generation field test and test bed with BBC, near London, UK
- 1993: TH-CSF show in Montreux SW, 4 TV channel and one HDTV channel in a single 8 MHz channel
- 1993: Morris: Experimental 150 Mbit/s OFDM wireless LAN
- 1995: ETSI Digital Audio Broadcasting standard EUreka: first OFDM-based standard
- 1997: ETSI DVB-T standard
- 1998: Magic WAND project demonstrates OFDM modems for wireless LAN
- 1999: IEEE 802.11a wireless LAN standard (Wi-Fi)
- 2000: Proprietary fixed wireless access (V-OFDM, FLASH-OFDM, etc.)
- May 2001: The FCC allows OFDM in the 2.4 GHz license exempt band.
- 2002: IEEE 802.11g standard for wireless LAN
- 2004: IEEE 802.16 standard for wireless MAN (WiMAX)
- 2004: ETSI DVB-H standard
- 2004: Candidate for IEEE 802.15.3a standard for wireless PAN (MB-OFDM)
- 2004: Candidate for IEEE 802.11n standard for next generation wireless LAN
- 2005: OFDMA is candidate for the 3GPP Long-Term Evolution (LTE) air interface E-UTRA downlink.
- 2007: The first complete LTE air interface implementation was demonstrated, including OFDM-MIMO, SC-FDMA and multi-user MIMO uplink
