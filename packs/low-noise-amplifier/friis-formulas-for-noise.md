---
title: "Friis formulas for noise"
source: https://en.wikipedia.org/wiki/Friis_formulas_for_noise
domain: low-noise-amplifier
license: CC-BY-SA-4.0
tags: low noise amplifier, noise figure, noise temperature, Friis formula
fetched: 2026-07-02
---

# Friis formulas for noise

**Friis formula** or **Friis's formula** (sometimes **Friis' formula**), named after Danish-American electrical engineer Harald T. Friis, is either of two formulas used in telecommunications engineering to calculate the signal-to-noise ratio of a multistage amplifier. One relates to noise factor while the other relates to noise temperature.

## The Friis formula for noise factor

(Amplifier chain with known power gain factors G1,2,3 und noise factors F1,2,3.)

Friis's formula is used to calculate the total noise factor of a cascade of stages, each with its own noise factor and power gain (assuming that the impedances are matched at each stage). The total noise factor can then be used to calculate the total noise figure. The total noise factor is given as

$F_{\text{total}}=F_{1}+{\frac {F_{2}-1}{G_{1}}}+{\frac {F_{3}-1}{G_{1}G_{2}}}+{\frac {F_{4}-1}{G_{1}G_{2}G_{3}}}+\cdots +{\frac {F_{n}-1}{G_{1}G_{2}\cdots G_{n-1}}}$

where $F_{i}$ and $G_{i}$ are the noise factor and available power gain, respectively, of the *i*-th stage, and *n* is the number of stages. Both magnitudes are expressed as ratios, not in decibels.

### Consequences

An important consequence of this formula is that the overall noise figure of a radio receiver is primarily established by the noise figure of its first amplifying stage. Subsequent stages have a diminishing effect on signal-to-noise ratio. For this reason, the first stage amplifier in a receiver is often called the low-noise amplifier (LNA). The overall receiver noise "factor" is then

$F_{\mathrm {receiver} }=F_{\mathrm {LNA} }+{\frac {F_{\mathrm {rest} }-1}{G_{\mathrm {LNA} }}}$

where $F_{\mathrm {rest} }$ is the overall noise factor of the subsequent stages. According to the equation, the overall noise factor, $F_{\mathrm {receiver} }$ , is dominated by the noise factor of the LNA, $F_{\mathrm {LNA} }$ , if the gain is sufficiently high. The resultant Noise Figure expressed in dB is:

$\mathrm {NF} _{\mathrm {receiver} }=10\log(F_{\mathrm {receiver} })$

### Derivation

For a derivation of Friis' formula for the case of three cascaded amplifiers ( $n=3$ ) consider the image below. (Chain of three amplifiers)

A source outputs a signal of power $S_{i}$ and noise of power $N_{i}$ . Therefore the SNR at the input of the receiver chain is ${\text{SNR}}_{i}=S_{i}/N_{i}$ . The signal of power $S_{i}$ gets amplified by all three amplifiers. Thus the signal power at the output of the third amplifier is $S_{o}=S_{i}\cdot G_{1}G_{2}G_{3}$ . The noise power at the output of the amplifier chain consists of four parts:

- The amplified noise of the source ( $N_{i}\cdot G_{1}G_{2}G_{3}$ )
- The output referred noise of the first amplifier $N_{a1}$ amplified by the second and third amplifier ( $N_{a1}\cdot G_{2}G_{3}$ )
- The output referred noise of the second amplifier $N_{a2}$ amplified by the third amplifier ( $N_{a2}\cdot G_{3}$ )
- The output referred noise of the third amplifier $N_{a3}$

Therefore the total noise power at the output of the amplifier chain equals

$N_{o}=N_{i}G_{1}G_{2}G_{3}+N_{a1}G_{2}G_{3}+N_{a2}G_{3}+N_{a3}$

and the SNR at the output of the amplifier chain equals

${\text{SNR}}_{o}={\frac {S_{i}G_{1}G_{2}G_{3}}{N_{i}G_{1}G_{2}G_{3}+N_{a1}G_{2}G_{3}+N_{a2}G_{3}+N_{a3}}}$

.

The total noise factor may now be calculated as quotient of the input and output SNR:

$F_{\text{total}}={\frac {{\text{SNR}}_{i}}{{\text{SNR}}_{o}}}={\frac {\frac {S_{i}}{N_{i}}}{\frac {S_{i}G_{1}G_{2}G_{3}}{N_{i}G_{1}G_{2}G_{3}+N_{a1}G_{2}G_{3}+N_{a2}G_{3}+N_{a3}}}}=1+{\frac {N_{a1}}{N_{i}G_{1}}}+{\frac {N_{a2}}{N_{i}G_{1}G_{2}}}+{\frac {N_{a3}}{N_{i}G_{1}G_{2}G_{3}}}$

Using the definitions of the noise factors of the amplifiers we get the final result:

$F_{\text{total}}=\underbrace {1+{\frac {N_{a1}}{N_{i}G_{1}}}} _{=F_{1}}+\underbrace {\frac {N_{a2}}{N_{i}G_{1}G_{2}}} _{={\frac {F_{2}-1}{G_{1}}}}+\underbrace {\frac {N_{a3}}{N_{i}G_{1}G_{2}G_{3}}} _{={\frac {F_{3}-1}{G_{1}G_{2}}}}=F_{1}+{\frac {F_{2}-1}{G_{1}}}+{\frac {F_{3}-1}{G_{1}G_{2}}}$

.

General derivation for a cascade of n amplifiers:

The total noise figure is given as the relation of the signal-to-noise ratio at the cascade input $\mathrm {SNR_{i}} ={\frac {S_{\mathrm {i} }}{N_{\mathrm {i} }}}$ to the signal-to-noise ratio at the cascade output $\mathrm {SNR_{o}} ={\frac {S_{\mathrm {o} }}{N_{\mathrm {o} }}}$ as

$F_{\mathrm {total} }={\frac {\mathrm {SNR_{i}} }{\mathrm {SNR_{o}} }}={\frac {S_{\mathrm {i} }}{S_{\mathrm {o} }}}{\frac {N_{\mathrm {o} }}{N_{\mathrm {i} }}}$ .

The total input power of the k -th amplifier in the cascade (noise and signal) is $S_{k-1}+N_{k-1}$ . It is amplified according to the amplifier's power gain $G_{k}$ . Additionally, the amplifier adds noise with power $N_{\mathrm {a} ,k}$ . Thus the output power of the k -th amplifier is $G_{k}\left(S_{k-1}+N_{k-1}\right)+N_{\mathrm {a} ,k}$ . For the entire cascade, one obtains the total output power

$S_{\mathrm {o} }+N_{\mathrm {o} }=\left(\left(\left(\left(S_{\mathrm {i} }+N_{\mathrm {i} }\right)G_{1}+N_{\mathrm {a} ,1}\right)G_{2}+N_{\mathrm {a} ,2}\right)G_{3}+N_{\mathrm {a} ,3}\right)G_{4}+\dots$

The output signal power thus rewrites as

$S_{\mathrm {o} }=S_{\mathrm {i} }\prod _{k=1}^{n}G_{k}$

whereas the output noise power can be written as

$N_{\mathrm {o} }=N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}+\sum _{k=1}^{n-1}N_{\mathrm {a} ,k}\prod _{l=k+1}^{n}{G_{l}}+N_{\mathrm {a} ,n}$

Substituting these results into the total noise figure leads to

$F_{\mathrm {total} }={\frac {N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}+\sum _{k=1}^{n-1}N_{\mathrm {a} ,k}\prod _{l=k+1}^{n}{G_{l}}+N_{\mathrm {a} ,n}}{N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}}}=1+\sum _{k=1}^{n-1}{\frac {N_{\mathrm {a} ,k}\prod _{l=k+1}^{n}{G_{l}}}{N_{\mathrm {i} }\prod _{m=1}^{n}G_{m}}}+{\frac {N_{\mathrm {a} ,n}}{N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}}}=1+\sum _{k=1}^{n-1}{\frac {N_{\mathrm {a} ,k}}{N_{\mathrm {i} }\prod _{m=1}^{k}G_{m}}}+{\frac {N_{\mathrm {a} ,n}}{N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}}}$

$=1+{\frac {N_{\mathrm {a} ,1}}{N_{\mathrm {i} }G_{1}}}+\sum _{k=2}^{n-1}{\frac {N_{\mathrm {a} ,k}}{N_{\mathrm {i} }\prod _{m=1}^{k}G_{m}}}+{\frac {N_{\mathrm {a} ,n}}{N_{\mathrm {i} }\prod _{k=1}^{n}G_{k}}}$

Now, using $F_{k}=1+{\frac {N_{\mathrm {a} ,k}}{N_{\mathrm {i} }G_{k}}}$ as the noise figure of the individual k -th amplifier, one obtains

$F_{\mathrm {total} }=F_{1}+\sum _{k=2}^{n}{\frac {F_{k}-1}{\prod _{l=1}^{k-1}G_{l}}}$

$=F_{1}+{\frac {F_{2}-1}{G_{1}}}+{\frac {F_{3}-1}{G_{1}G_{2}}}+{\frac {F_{4}-1}{G_{1}G_{2}G_{3}}}+\dots +{\frac {F_{n}-1}{G_{1}G_{2}\dots G_{n-1}}}$

## The Friis formula for noise temperature

Friis's formula can be equivalently expressed in terms of noise temperature:

$T_{\text{eq}}=T_{1}+{\frac {T_{2}}{G_{1}}}+{\frac {T_{3}}{G_{1}G_{2}}}+\cdots$

## Published references

- J.D. Kraus, *Radio Astronomy*, McGraw-Hill, 1966.

## Online references

- RF Cafe [1] Cascaded noise figure.
- Microwave Encyclopedia [2] Archived 2013-05-17 at the Wayback Machine Cascade analysis.
- Friis biography at IEEE [3]

Retrieved from "

https://en.wikipedia.org/w/index.php?title=Friis_formulas_for_noise&oldid=1264867328

"
