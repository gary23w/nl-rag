---
title: "RC circuit"
source: https://en.wikipedia.org/wiki/RC_circuit
domain: passive-filters
license: CC-BY-SA-4.0
tags: passive filter, constant k filter, m-derived filter, resonant circuit
fetched: 2026-07-02
---

# RC circuit

A **resistor–capacitor circuit** (**RC circuit**), or **RC filter** or **RC network**, is an electric circuit composed of resistors and capacitors. It may be driven by a voltage or current source and these will produce different responses. A first order RC circuit is composed of one resistor and one capacitor and is the simplest type of RC circuit.

RC circuits can be used to filter a signal by blocking certain frequencies and passing others. The two most common RC filters are the high-pass filters and low-pass filters; band-pass filters and band-stop filters usually require RLC filters, though crude ones can be made with RC filters.

## Natural response

The simplest RC circuit consists of a resistor with resistance R and a charged capacitor with capacitance C connected to one another in a single loop, without an external voltage source. The capacitor will discharge its stored energy through the resistor. If *V*(*t*) is taken to be the voltage of the capacitor's top plate relative to its bottom plate in the figure, then the capacitor current–voltage relation says the current *I*(*t*) *exiting* the capacitor's top plate will equal C multiplied by the *negative* time derivative of *V*(*t*). Kirchhoff's current law says this current is the same current entering the top side of the resistor, which per Ohm's law equals *V*(*t*)/*R*. This yields a linear differential equation $\overbrace {C{\frac {-\mathrm {d} V(t)}{\mathrm {d} t}}} ^{\text{capacitor current}}=\overbrace {\frac {V(t)}{R}} ^{\text{resistor current}},$ which can be rearranged according to the standard form for exponential decay: ${\frac {\mathrm {d} V(t)}{\mathrm {d} t}}=-{\frac {1}{RC}}V(t).$ This means that the instantaneous rate of voltage decrease at any time is proportional to the voltage at that time. Solving for *V*(*t*) yields an exponential decay curve that asymptotically approaches 0: $V(t)=V_{0}\cdot e^{-{\frac {t}{RC}}},$ where *V*0 is the capacitor voltage at time *t* = 0, and e is Euler's number.

The time required for the voltage to fall to *V*0/*e* is called the RC time constant and is given by $\tau =RC.$ When using the International System of Units, R is in ohms, and C is in farads, so τ will be in seconds. At any time *N*·τ, the capacitor's charge or voltage will be 1/*e*N of its starting value. So if the capacitor's charge or voltage is said to start at 100%, then 36.8% remains at 1·τ, 13.5% remains at 2·τ, 5% remains at 3·τ, 1.8% remains at 4·τ, and less than 0.7% remains at 5·τ and later.

The half-life (*t*1/2) is the time that it takes for its charge or voltage to be reduced in half: ${\frac {1}{2}}=e^{-{\tfrac {t_{1/2}}{\tau }}}\quad \Rightarrow \quad t_{1/2}=\ln(2)\,\tau \approx {\text{0.693}}\,\tau .$ For example, 50% of charge or voltage remains at time 1·*t*1/2, then 25% remains at time 2·*t*1/2, then 12.5% remains at time 3·*t*1/2, and 1/2N will remain at time *N*·*t*1/2.

### RC discharge calculator

0.000001

1000000

1

1

1

1

1

1

1

.368

36.8

1

0.368

1 1

1

0.159

1

1

1

1

For instance, 1  of resistance with 1  of capacitance produces a time constant of approximately 1 seconds. This τ corresponds to a cutoff frequency of approximately 159 millihertz or 1 radians per second. If the capacitor has an initial voltage *V*0 of 1 , then after 1 τ (approximately 1 seconds or 1.443 half-lives), the capacitor's voltage will discharge to approximately 368 millivolts:

V

C

(

1

τ

) ≈

36.8

% of

V

0

## Complex impedance

The RC circuit's behavior is well-suited to be analyzed in the Laplace domain, which the rest of this article requires a basic understanding of. The Laplace domain is a frequency domain representation using complex frequency s, which is (in general) a complex number: $s=\sigma +j\omega ,$ where

j

represents the

imaginary unit

:

j

2

= −1

,

σ

is the

exponential decay

constant (equal to

−1/(

RC

)

in this case),

ω

is the

sinusoidal

angular frequency

.

When evaluating circuit equations in the Laplace domain, time-dependent circuit elements of capacitance and inductance can be treated like resistors with complex-valued impedance instead of real resistance. While the complex impedance ZR of a resistor is simply a real value equal to its resistance R, the complex impedance of a capacitor C is instead $Z_{C}={\frac {1}{Cs}}.$

## Series circuit

### Current

Kirchhoff's current law means that the current in the series circuit is necessarily the same through both elements. Ohm's law says this current is equal to the input voltage $V_{\mathrm {in} }$ divided by the sum of the complex impedance of the capacitor and resistor:

${\begin{aligned}I(s)&={\frac {V_{\mathrm {in} }(s)}{R+{\frac {1}{Cs}}}}\\&={\frac {Cs}{1+RCs}}V_{\mathrm {in} }(s)\,.\end{aligned}}$

### Voltage

By viewing the circuit as a voltage divider, the voltage across the capacitor is:

${\begin{aligned}V_{C}(s)&={\frac {\frac {1}{Cs}}{R+{\frac {1}{Cs}}}}V_{\mathrm {in} }(s)\\&={\frac {1}{1+RCs}}V_{\mathrm {in} }(s)\end{aligned}}$

and the voltage across the resistor is:

${\begin{aligned}V_{R}(s)&={\frac {R}{R+{\frac {1}{Cs}}}}V_{\mathrm {in} }(s)\\&={\frac {RCs}{1+RCs}}V_{\mathrm {in} }(s)\,.\end{aligned}}$

### Transfer functions

The transfer function from the input voltage to the voltage across the capacitor is

$H_{C}(s)={\frac {V_{C}(s)}{V_{\mathrm {in} }(s)}}={\frac {1}{1+RCs}}\,.$

Similarly, the transfer function from the input to the voltage across the resistor is

$H_{R}(s)={\frac {V_{R}(s)}{V_{\rm {in}}(s)}}={\frac {RCs}{1+RCs}}\,.$

#### Poles and zeros

Both transfer functions have a single pole located at

$s=-{\frac {1}{RC}}\,.$

In addition, the transfer function for the voltage across the resistor has a zero located at the origin.

### Frequency-domain considerations

The sinusoidal steady state is a special case of complex frequency that considers the input to consist only of pure sinusoids. Hence, the exponential decay component represented by $\sigma$ can be ignored in the complex frequency equation $s{=}\sigma {+}j\omega$ when only the steady state is of interest. The simple substitution of $s\Rightarrow j\omega$ into the previous transfer functions will thus provide the sinusoidal gain and phase response of the circuit.

#### Gain

The magnitude of the gains across the two components are

$G_{C}={\big |}H_{C}(j\omega ){\big |}=\left|{\frac {V_{C}(j\omega )}{V_{\mathrm {in} }(j\omega )}}\right|={\frac {1}{\sqrt {1+\left(\omega RC\right)^{2}}}}$

and

$G_{R}={\big |}H_{R}(j\omega ){\big |}=\left|{\frac {V_{R}(j\omega )}{V_{\mathrm {in} }(j\omega )}}\right|={\frac {\omega RC}{\sqrt {1+\left(\omega RC\right)^{2}}}}\,,$

As the frequency becomes very large (*ω* → ∞), the capacitor acts like a short circuit, so:

$G_{C}\to 0\quad {\mbox{and}}\quad G_{R}\to 1\,.$

As the frequency becomes very small (*ω* → 0), the capacitor acts like an open circuit, so:

$G_{C}\to 1\quad {\mbox{and}}\quad G_{R}\to 0\,.$

##### Operation as either a high-pass or a low-pass filter

The behavior at these extreme frequencies show that if the output is taken across the capacitor, high frequencies are attenuated and low frequencies are passed, so such a circuit configuration is a *low-pass filter*. However, if the output is taken across the resistor, then high frequencies are passed and low frequencies are attenuated, so such a configuration is a *high-pass filter*.

##### Cutoff frequency

The range of frequencies that the filter passes is called its bandwidth. The frequency at which the filter attenuates the signal to half its unfiltered power is termed its cutoff frequency. This requires that the gain of the circuit be reduced to

$G_{C}=G_{R}={\frac {1}{\sqrt {2}}}$

.

Solving the above equation yields

$\omega _{\mathrm {c} }={\frac {1}{RC}}\quad {\mbox{or}}\quad f_{\mathrm {c} }={\frac {1}{2\pi RC}}$

which is the frequency that the filter will attenuate to half its original power.

#### Phase

The phase angles are

$\phi _{C}=\angle H_{C}(j\omega )=\tan ^{-1}\left(-\omega RC\right)$

and

$\phi _{R}=\angle H_{R}(j\omega )=\tan ^{-1}\left({\frac {1}{\omega RC}}\right)\,.$

As *ω* → 0:

$\phi _{C}\to 0\quad {\mbox{and}}\quad \phi _{R}\to 90^{\circ }={\frac {\pi }{2}}{\mbox{ radians}}\,.$

As *ω* → ∞:

$\phi _{C}\to -90^{\circ }=-{\frac {\pi }{2}}{\mbox{ radians}}\quad {\mbox{and}}\quad \phi _{R}\to 0\,.$

While the output signal's phase shift relative to the input depends on frequency, this is generally less interesting than the gain variations. At DC (0 Hz), the capacitor voltage is in phase with the input signal voltage while the resistor voltage leads it by 90°. As frequency increases, the capacitor voltage comes to have a 90° lag relative to the input signal and the resistor voltage comes to be in-phase with the input signal.

#### Phasor representation

The gain and phase expressions together may be combined into these phasor expressions representing the output:

${\begin{aligned}V_{C}&=G_{C}V_{\mathrm {in} }e^{j\phi _{C}}\\V_{R}&=G_{R}V_{\mathrm {in} }e^{j\phi _{R}}\,.\end{aligned}}$

### Impulse response

The impulse response for each voltage is the inverse Laplace transform of the corresponding transfer function. It represents the response of the circuit to an input voltage consisting of an impulse or Dirac delta function.

The impulse response for the capacitor voltage is

$h_{C}(t)={\frac {1}{RC}}e^{-{\frac {t}{RC}}}u(t)={\frac {1}{\tau }}e^{-{\frac {t}{\tau }}}u(t)\,,$

where *u*(*t*) is the Heaviside step function and *τ* = *RC* is the time constant.

Similarly, the impulse response for the resistor voltage is

$h_{R}(t)=\delta (t)-{\frac {1}{RC}}e^{-{\frac {t}{RC}}}u(t)=\delta (t)-{\frac {1}{\tau }}e^{-{\frac {t}{\tau }}}u(t)\,,$

where *δ*(*t*) is the Dirac delta function.

### Time-domain considerations

This section relies on knowledge of the

Laplace transform

.

The most straightforward way to derive the time domain behaviour is to use the Laplace transforms of the expressions for VC and VR given above. Assuming a step input (i.e. *V*in = 0 before *t* = 0 and then *V*in = *V*1 afterwards):

${\begin{aligned}V_{\mathrm {in} }(s)&=V_{1}\cdot {\frac {1}{s}}\\V_{C}(s)&=V_{1}\cdot {\frac {1}{1+sRC}}\cdot {\frac {1}{s}}\\V_{R}(s)&=V_{1}\cdot {\frac {sRC}{1+sRC}}\cdot {\frac {1}{s}}\,.\end{aligned}}$

Partial fractions expansions and the inverse Laplace transform yield:

${\begin{aligned}V_{C}(t)&=V_{1}\cdot \left(1-e^{-{\frac {t}{RC}}}\right)\\V_{R}(t)&=V_{1}\cdot \left(e^{-{\frac {t}{RC}}}\right)\,.\end{aligned}}$

These equations are for calculating the voltage across the capacitor and resistor respectively while the capacitor is charging; for discharging, the equations are vice versa. These equations can be rewritten in terms of charge and current using the relationships *C* = *⁠Q/V⁠* and *V* = *IR* (see Ohm's law).

Thus, the voltage across the capacitor tends towards V1 as time passes, while the voltage across the resistor tends towards 0, as shown in the figures. This is in keeping with the intuitive point that the capacitor will be charging from the supply voltage as time passes, and will eventually be fully charged.

The product *RC* is both the time for VC and VR to reach within ⁠1/*e*⁠ of their final value. In other words, *RC* is the time it takes for the voltage across the capacitor to rise to *V*1·(1 − ⁠1/*e*⁠) or for the voltage across the resistor to fall to *V*1·(⁠1/*e*⁠). This RC time constant is labeled using the letter tau (*τ*).

The rate of change is a *fractional* 1 − ⁠1/*e*⁠ per τ. Thus, in going from *t* = *Nτ* to *t* = (*N* + 1)*τ*, the voltage will have moved about 63.2% of the way from its level at *t* = *Nτ* toward its final value. So the capacitor will be charged to about 63.2% after τ, and is often considered fully charged (>99.3%) after about 5*τ*. When the voltage source is replaced with a short circuit, with the capacitor fully charged, the voltage across the capacitor drops exponentially with t from V towards 0. The capacitor will be discharged to about 36.8% after τ, and is often considered fully discharged (<0.7%) after about 5*τ*. Note that the current, I, in the circuit behaves as the voltage across the resistor does, via Ohm's law.

These results may also be derived by solving the differential equations describing the circuit:

${\begin{aligned}{\frac {V_{\mathrm {in} }-V_{C}}{R}}&=C{\frac {dV_{C}}{dt}}\\V_{R}&=V_{\mathrm {in} }-V_{C}\,.\end{aligned}}$

The first equation is solved by using an integrating factor and the second follows easily; the solutions are exactly the same as those obtained via Laplace transforms.

#### Integrator

Consider the output across the capacitor at *high* frequency, i.e.

$\omega \gg {\frac {1}{RC}}\,.$

This means that the capacitor has insufficient time to charge up and so its voltage is very small. Thus the input voltage approximately equals the voltage across the resistor. To see this, consider the expression for I given above:

$I={\frac {V_{\mathrm {in} }}{R+{\frac {1}{j\omega C}}}}\,,$

but note that the frequency condition described means that

$\omega C\gg {\frac {1}{R}}\,,$

so

$I\approx {\frac {V_{\mathrm {in} }}{R}}$

which is just Ohm's law.

Now,

$V_{C}={\frac {1}{C}}\int _{0}^{t}I\,dt\,,$

so

$V_{C}\approx {\frac {1}{RC}}\int _{0}^{t}V_{\mathrm {in} }\,dt\,.$

Therefore, the voltage *across the capacitor* acts approximately like an integrator of the input voltage for high frequencies.

#### Differentiator

Consider the output across the resistor at *low* frequency i.e.,

$\omega \ll {\frac {1}{RC}}\,.$

This means that the capacitor has time to charge up until its voltage is almost equal to the source's voltage. Considering the expression for I again, when

$R\ll {\frac {1}{\omega C}}\,,$

so

${\begin{aligned}I&\approx {\frac {V_{\mathrm {in} }}{\frac {1}{j\omega C}}}\\V_{\mathrm {in} }&\approx {\frac {I}{j\omega C}}=V_{C}\,.\end{aligned}}$

Now,

${\begin{aligned}V_{R}&=IR=C{\frac {dV_{C}}{dt}}R\\V_{R}&\approx RC{\frac {dV_{in}}{dt}}\,.\end{aligned}}$

Therefore, the voltage *across the resistor* acts approximately like a differentiator of the input voltage for low frequencies.

Integration and differentiation can also be achieved by placing resistors and capacitors as appropriate on the input and feedback loop of operational amplifiers (see *operational amplifier integrator* and *operational amplifier differentiator*).

## Parallel circuit

The parallel RC circuit is generally of less interest than the series circuit. This is largely because the output voltage *V*out is equal to the input voltage *V*in — as a result, this circuit acts as a filter on a current input instead of a voltage input.

With complex impedances:

${\begin{aligned}I_{R}&={\frac {V_{\mathrm {in} }}{R}}\\I_{C}&=j\omega CV_{\mathrm {in} }\,.\end{aligned}}$

This shows that the capacitor current is 90° out of phase with the resistor (and source) current. Alternatively, the governing differential equations may be used:

${\begin{aligned}I_{R}&={\frac {V_{\mathrm {in} }}{R}}\\I_{C}&=C{\frac {dV_{\mathrm {in} }}{dt}}\,.\end{aligned}}$

When fed by a current source, the transfer function of a parallel RC circuit is:

${\frac {V_{\mathrm {out} }}{I_{\mathrm {in} }}}={\frac {R}{1+sRC}}\,.$

## Synthesis

It is sometimes required to synthesise an RC circuit from a given rational function in *s*. For synthesis to be possible in passive elements, the function must be a positive-real function. To synthesise as an RC circuit, all the critical frequencies (poles and zeroes) must be on the negative real axis and alternate between poles and zeroes with an equal number of each. Further, the critical frequency nearest the origin must be a pole, assuming the rational function represents an impedance rather than an admittance.

The synthesis can be achieved with a modification of the Foster synthesis or Cauer synthesis used to synthesise LC circuits. In the case of Cauer synthesis, a ladder network of resistors and capacitors will result.
