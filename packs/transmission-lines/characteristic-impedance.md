---
title: "Characteristic impedance"
source: https://en.wikipedia.org/wiki/Characteristic_impedance
domain: transmission-lines
license: CC-BY-SA-4.0
tags: transmission line, characteristic impedance, standing wave ratio, reflection coefficient
fetched: 2026-07-02
---

# Characteristic impedance

The **characteristic impedance** or **surge impedance** (usually written *Z*0) of a uniform transmission line is the ratio of the amplitudes of voltage and current of a wave travelling in one direction along the line in the absence of reflections in the other direction. Equivalently, it can be defined as the input impedance of a transmission line when its length is infinite. Characteristic impedance is determined by the geometry and materials of the transmission line and, for a uniform line, is not dependent on its length. The SI unit of characteristic impedance is the ohm.

The characteristic impedance of a lossless transmission line is purely real, with no reactive component (see below). Energy supplied by a source at one end of such a line is transmitted through the line without being dissipated in the line itself. A transmission line of finite length (lossless or lossy) that is terminated at one end with an impedance equal to the characteristic impedance appears to the source like an infinitely long transmission line and produces no reflections.

## Transmission line model

The characteristic impedance *Z*(*ω*) of an infinite transmission line at a given angular frequency ω is the ratio of the voltage and current of a pure sinusoidal wave of the same frequency travelling along the line. This relation is also the case for finite transmission lines until the wave reaches the end of the line. Generally, a wave is reflected back along the line in the opposite direction. When the reflected wave reaches the source, it is reflected yet again, adding to the transmitted wave and changing the ratio of the voltage and current at the input, causing the voltage-current ratio to no longer equal the characteristic impedance. This new ratio including the reflected energy is called the input impedance of that particular transmission line and load.

The input impedance of an infinite line is equal to the characteristic impedance since the transmitted wave is never reflected back from the end. Equivalently: *the characteristic impedance of a line is that impedance which, when terminating an arbitrary length of line at its output, produces an input impedance of equal value*. This is so because there is no reflection on a line terminated in its own characteristic impedance.

Applying the transmission line model based on the telegrapher's equations as derived below, the general expression for the characteristic impedance of a transmission line is: $Z_{0}={\sqrt {{\frac {R+j\omega L}{G+j\omega C}}\,}}$ where

- R is the resistance per unit length, considering the two conductors to be in series,
- L is the inductance per unit length,
- G is the conductance of the dielectric per unit length,
- C is the capacitance per unit length,
- j is the imaginary unit *j*2 = −1, and
- ω is the angular frequency.

This expression extends to DC by letting ω tend to 0.

A surge of energy on a finite transmission line will see an impedance of *Z*0 prior to any reflections returning; hence *surge impedance* is an alternative name for *characteristic impedance*. Although an infinite line is assumed, since all quantities are per unit length, the “per length” parts of all the units cancel, and the characteristic impedance is independent of the length of the transmission line.

The voltage and current phasors on the line are related by the characteristic impedance as: $Z_{\text{0}}={\frac {V_{(+)}}{I_{(+)}}}=-{\frac {V_{(-)}}{I_{(-)}}}$ where the subscripts (+) and (−) mark the separate constants for the waves traveling forward (+) and backward (−). The rightmost expression has a negative sign because the current in the backward wave has the opposite direction to current in the forward wave.

### Characteristic admittance

**Characteristic admittance** is the mathematical inverse of the characteristic impedance. The general expression for the characteristic admittance of a transmission line is as follows:

$Y_{0}={\sqrt {\frac {G+j\omega C}{R+j\omega L}}}$

The current and voltage phasors on the line are related by the characteristic admittance as:

${\frac {I^{+}}{V^{+}}}=Y_{0}=-{\frac {I^{-}}{V^{-}}}$

where the superscripts + and - represent forward- and backward-traveling waves, respectively.

## Derivation

### Using the telegrapher's equation

The differential equations describing the dependence of the voltage and current on time and space are linear, so that a linear combination of solutions is again a solution. This means that we can consider solutions with a time dependence $e^{j\omega t}$ . Doing so allows to factor out the time dependence, leaving an ordinary differential equation for the coefficients, which will be phasors, dependent on position (space) only. Moreover, the parameters can be generalized to be frequency-dependent.

Consider a steady-state problem such that the voltage and current can be written as: ${\begin{aligned}v(x,t)&=V(x)e^{j\omega t}\\[.5ex]i(x,t)&=I(x)e^{j\omega t}\end{aligned}}$ Take the positive direction for V and I in the loop to be clockwise. Substitution in the telegraph equations and factoring out the time dependence $e^{j\omega t}$ now gives: ${\begin{aligned}{\frac {\mathrm {d} V}{\mathrm {d} x}}&=-\left(R+j\omega L\right)I=-ZI,\\[.5ex]{\frac {\mathrm {d} I}{\mathrm {d} x}}&=-\left(G+j\omega C\right)V=-YV,\end{aligned}}$ with impedance Z and admittance Y. Derivation and substitution of these two first-order differential equations results in two uncoupled second-order differential equations: ${\begin{aligned}{\frac {\mathrm {d} ^{2}V}{\mathrm {d} x^{2}}}&=k^{2}V,\\[.5ex]{\frac {\mathrm {d} ^{2}I}{\mathrm {d} x^{2}}}&=k^{2}I,\end{aligned}}$ with *k*2 = *ZY* = (*R* + *jωL*)(*G* + *jωC*) and *k* = *α* + *jβ* called the propagation constant.

The solution to these types of equations can be written as: ${\begin{aligned}V(x)&=Ae^{-kx}+Be^{kx}\\[.5ex]I(x)&=A_{1}e^{-kx}+B_{1}e^{kx}\end{aligned}}$ with A, *A*1, B and *B*1 the constants of integration. Substituting these constants in the first-order system gives: ${\begin{aligned}A_{1}&={\hphantom {-}}A{\frac {k}{R+j\omega L}}\\[.5ex]B_{1}&=-B{\frac {k}{R+j\omega L}}\end{aligned}}$ where ${\frac {A}{A_{1}}}=-{\frac {B}{B_{1}}}={\frac {R+j\omega L}{k}}={\sqrt {\frac {R+j\omega L}{G+j\omega C}}}={\sqrt {\frac {Z}{Y}}}=Z_{0}.$ It can be seen that the constant *Z*0, defined in the above equations has the dimensions of impedance (ratio of voltage to current) and is a function of primary constants of the line and operating frequency. It is called the **characteristic impedance** of the transmission line.

The general solution of the telegrapher's equations can now be written as: ${\begin{aligned}v(x,t)&=V(x)e^{j\omega t}=Ae^{-\alpha x}e^{j(\omega t-\beta x)}+Be^{\alpha x}e^{j(\omega t+\beta x)}\\[.5ex]i(x,t)&=I(x)e^{j\omega t}={\frac {A}{Z_{0}}}e^{-\alpha x}e^{j(\omega t-\beta x)}-{\frac {B}{Z_{0}}}e^{\alpha x}e^{j(\omega t+\beta x)}\end{aligned}}$ Both the solution for the voltage and the current can be regarded as a superposition of two travelling waves in the *x*(+) and *x*(−) directions.

For typical transmission lines, that are carefully built from wire with low loss resistance R and small insulation leakage conductance G; further, used for high frequencies, the inductive reactance ωL and the capacitive admittance ωC will both be large. In those cases, the phase constant and characteristic impedance are typically very close to being real numbers: ${\begin{aligned}\beta &={\text{Im}}\{k\}\approx \omega {\sqrt {LC}}\\[.5ex]Z_{0}&\approx {\sqrt {\frac {L}{C}}}\end{aligned}}$ Manufacturers make commercial cables to approximate this condition very closely over a wide range of frequencies.

### As a limiting case of infinite ladder networks

#### Intuition

Iterative impedance of an infinite ladder of L-circuit sections

Iterative impedance of the equivalent finite L-circuit

Consider an infinite ladder network consisting of a series impedance Z and a shunt admittance Y. Let its input impedance be *Z*IT. If a new pair of impedance Z and admittance Y is added in front of the network, its input impedance *Z*IT remains unchanged since the network is infinite. Thus, it can be reduced to a finite network with one series impedance Z and two parallel impedances 1/*Y* and *Z*IT. Its input impedance is given by the expression $Z_{\mathrm {IT} }=Z+\left({\frac {\ 1\ }{Y}}\parallel Z_{\mathrm {IT} }\right)\$ which is also known as its iterative impedance. Its solution is: $Z_{\mathrm {IT} }={Z \over 2}\pm {\sqrt {{Z^{2} \over 4}+{Z \over Y}}}\$

For a transmission line, it can be seen as a limiting case of an infinite ladder network with infinitesimal impedance and admittance at a constant ratio. Taking the positive root, this equation simplifies to: $\ Z_{\mathrm {IT} }={\sqrt {{\frac {\ Z\ }{Y}}\ }}\$

#### Derivation

Using this insight, many similar derivations exist in several books and are applicable to both lossless and lossy lines.

Here, we follow an approach posted by Tim Healy. The line is modeled by a series of differential segments with differential series elements (*R* d*x*, *L* d*x*) and shunt elements (*C* d*x*, *G* d*x*) (as shown in the figure at the beginning of the article). The characteristic impedance is defined as the ratio of the input voltage to the input current of a semi-infinite length of line. We call this impedance *Z*0. That is, the impedance looking into the line on the left is *Z*0. But, of course, if we go down the line one differential length d*x*, the impedance into the line is still *Z*0. Hence we can say that the impedance looking into the line on the far left is equal to *Z*0 in parallel with *C* d*x* and *G* d*x*, all of which is in series with *R* d*x* and *L* d*x*. Hence: ${\begin{aligned}&Z_{0}=(R+j\omega L)\operatorname {d} \!x+{\frac {1}{(G+j\omega C)\operatorname {d} \!x+{\frac {1}{Z_{0}}}}}\\&Z_{0}=(R+j\omega L)\operatorname {d} \!x+{\frac {Z_{0}}{Z_{0}(G+j\omega C)\operatorname {d} \!x+1}}\\&Z_{0}+Z_{0}^{2}(G+j\omega C)\operatorname {d} \!x=(R+j\omega L)\operatorname {d} \!x+Z_{0}(G+j\omega C)\operatorname {d} \!x\,(R+j\omega L)\operatorname {d} \!x+Z_{0}\end{aligned}}$

The added *Z*0 terms cancel, leaving $Z_{0}^{2}(G+j\omega C)\operatorname {d} \!x=(R+j\omega L)\operatorname {d} \!x+Z_{0}(G+j\omega C)(R+j\omega L)(\mathop {} \!\operatorname {d} \!x)^{2}$

The first-power d*x* terms are the highest remaining order. Dividing out the common factor of d*x*, and dividing through by the factor (*G* + *jωC*), we get $Z_{0}^{2}={\frac {(R+j\omega L)}{(G+j\omega C)}}+Z_{0}(R+j\omega L)\operatorname {d} \!x.$

In comparison to the factors whose d*x* divided out, the last term, which still carries a remaining factor d*x*, is infinitesimal relative to the other, now finite terms, so we can drop it. That leads to $Z_{0}=\pm {\sqrt {\frac {R+j\omega L}{G+j\omega C}}}\;.$

Reversing the sign ± applied to the square root has the effect of reversing the direction of the flow of current.

## Lossless line

The analysis of lossless lines provides an accurate approximation for real transmission lines that simplifies the mathematics considered in modeling transmission lines. A lossless line is defined as a transmission line that has no line resistance and no dielectric loss. This would imply that the conductors act like perfect conductors and the dielectric acts like a perfect dielectric. For a lossless line, *R* and *G* are both zero, so the equation for characteristic impedance derived above reduces to: $Z_{0}={\sqrt {{\frac {L}{C}}\,}}\,.$

In particular, *Z*0 does not depend any more upon the frequency. The above expression is wholly real, since the imaginary term j has canceled out, implying that *Z*0 is purely resistive. For a lossless line terminated in *Z*0, there is no loss of current across the line, and so the voltage remains the same along the line. The lossless line model is a useful approximation for many practical cases, such as low-loss transmission lines and transmission lines with high frequency. For both of these cases, R and G are much smaller than *ωL* and *ωC*, respectively, and can thus be ignored.

The solutions to the long line transmission equations include incident and reflected portions of the voltage and current: ${\begin{aligned}V&={\frac {V_{r}+I_{r}Z_{c}}{2}}e^{\gamma x}+{\frac {V_{r}-I_{r}Z_{c}}{2}}e^{-\gamma x}\\[1ex]I&={\frac {V_{r}/Z_{c}+I_{r}}{2}}e^{\gamma x}-{\frac {V_{r}/Z_{c}-I_{r}}{2}}e^{-\gamma x}\end{aligned}}$ When the line is terminated with its characteristic impedance, the reflected portions of these equations are reduced to 0 and the solutions to the voltage and current along the transmission line are wholly incident. Without a reflection of the wave, the load that is being supplied by the line effectively blends into the line making it appear to be an infinite line. In a lossless line this implies that the voltage and current remain the same everywhere along the transmission line. Their magnitudes remain constant along the length of the line and are only rotated by a phase angle.

## Surge impedance loading

In electric power transmission, the characteristic impedance of a transmission line is expressed in terms of the **surge impedance loading** (**SIL**), or natural loading, being the power loading at which reactive power is neither produced nor absorbed: $\mathrm {SIL} ={\frac {{V_{\mathrm {LL} }}^{2}}{Z_{0}}}$ in which *V*LL is the root mean square (RMS) line-to-line voltage in volts.

Loaded below its SIL, the voltage at the load will be greater than the system voltage. Above it, the load voltage is depressed. The Ferranti effect describes the voltage gain towards the remote end of a very lightly loaded (or open ended) transmission line. Underground cables normally have a very low characteristic impedance, resulting in an SIL that is typically in excess of the thermal limit of the cable.

## Practical examples

| Standard | Impedance (Ω) | Tolerance | Ref. |
|---|---|---|---|
| Category 5 | 100 | ±5 Ω |   |
| USB | 90 | ±15% |   |
| HDMI | 95 | ±15% |   |
| IEEE 1394 | 108 | +3% −2% |   |
| VGA | 75 | ±5% |   |
| DisplayPort | 100 | ±20% |   |
| DVI | 95 | ±15% |   |
| PCIe | 85 | ±15% |   |
| Overhead power line | 400 | Typical |   |
| Underground power line | 40 | Typical |   |

The characteristic impedance of coaxial cables (coax) is commonly chosen to be 50 Ω for RF and microwave applications. Coax for video applications is usually 75 Ω for its lower loss .
