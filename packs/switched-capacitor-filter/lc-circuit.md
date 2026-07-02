---
title: "LC circuit"
source: https://en.wikipedia.org/wiki/LC_circuit
domain: switched-capacitor-filter
license: CC-BY-SA-4.0
tags: switched capacitor, correlated double sampling, charge redistribution, switched-capacitor filter
fetched: 2026-07-02
---

# LC circuit

An **LC circuit**, also called a **resonant circuit**, **tank circuit**, or **tuned circuit**, is an electric circuit consisting of an inductor, represented by the letter L, and a capacitor, represented by the letter C, connected together. The circuit can act as an electrical resonator, an electrical analogue of a tuning fork, storing energy oscillating at the circuit's resonant frequency.

LC circuits are used either for generating signals at a particular frequency, or picking out a signal at a particular frequency from a more complex signal; this function is called a bandpass filter. They are key components in many electronic devices, particularly radio equipment, used in circuits such as oscillators, filters, tuners and frequency mixers.

An LC circuit is an idealized model since it assumes there is no dissipation of energy due to resistance. Any practical implementation of an LC circuit will always include loss resulting from small but non-zero resistance within the components and connecting wires. The purpose of an LC circuit is usually to oscillate with minimal damping, so the resistance is made as low as possible. While no practical circuit is without losses, it is nonetheless instructive to study this ideal form of the circuit to gain understanding and physical intuition. For a circuit model incorporating resistance, see RLC circuit.

## Terminology

The two-element LC circuit described above is the simplest type of **inductor-capacitor network** (or **LC network**). It is also referred to as a *second order LC circuit* to distinguish it from more complicated (higher order) LC networks with more inductors and capacitors. Such LC networks with more than two reactances may have more than one resonant frequency.

The order of the network is the order of the rational function describing the network in the complex frequency variable s. Generally, the order is equal to the number of L and C elements in the circuit and in any event cannot exceed this number.

## Operation

An LC circuit, oscillating at its natural resonant frequency, can store electrical energy. See the animation. A capacitor stores energy in the electric field (E) between its plates, depending on the voltage across it, and an inductor stores energy in its magnetic field (B), depending on the current through it.

If an inductor is connected across a charged capacitor, the voltage across the capacitor will drive a current through the inductor, building up a magnetic field around it. The voltage across the capacitor falls to zero as the charge is used up by the current flow. At this point, the energy stored in the coil's magnetic field induces a voltage across the coil, because inductors oppose changes in current. This induced voltage causes a current to begin to recharge the capacitor with a voltage of opposite polarity to its original charge. Due to Faraday's law, the EMF which drives the current is caused by a decrease in the magnetic field, thus the energy required to charge the capacitor is extracted from the magnetic field. When the magnetic field is completely dissipated the current will stop and the charge will again be stored in the capacitor, with the opposite polarity as before. Then the cycle will begin again, with the current flowing in the opposite direction through the inductor.

The charge flows back and forth between the plates of the capacitor, through the inductor. The energy oscillates back and forth between the capacitor and the inductor until (if not replenished from an external circuit) internal resistance makes the oscillations die out. The tuned circuit's action, known mathematically as a harmonic oscillator, is similar to a pendulum swinging back and forth, or water sloshing back and forth in a tank; for this reason the circuit is also called a *tank circuit*. The natural frequency (that is, the frequency at which it will oscillate when isolated from any other system, as described above) is determined by the capacitance and inductance values. In most applications the tuned circuit is part of a larger circuit which applies alternating current to it, driving continuous oscillations. If the frequency of the applied current is the circuit's natural resonant frequency (natural frequency $f_{0}\,$ below), resonance will occur, and a small driving current can excite large amplitude oscillating voltages and currents. In typical tuned circuits in electronic equipment the oscillations are very fast, from thousands to billions of times per second.

## Resonance effect

Resonance occurs when an LC circuit is driven from an external source at an angular frequency *ω*0 at which the inductive and capacitive reactances are equal in magnitude. The frequency at which this equality holds for the particular circuit is called the resonant frequency. The resonant frequency of the LC circuit is

$\omega _{0}={\frac {1}{\sqrt {LC}}},$

where L is the inductance in henries, and C is the capacitance in farads. The angular frequency *ω*0 has units of radians per second.

The equivalent frequency in units of hertz is

$f_{0}={\frac {\omega _{0}}{2\pi }}={\frac {1}{2\pi {\sqrt {LC}}}}.$

## Applications

The resonance effect of the LC circuit has many important applications in signal processing and communications systems.

- The most common application of tank circuits is **tuning** radio transmitters and receivers. For example, when tuning a radio to a particular station, the LC circuits are set at resonance for that particular carrier frequency.
- A series resonant circuit provides **voltage magnification**.
- A parallel resonant circuit provides **current magnification**.
- A parallel resonant circuit can be used as load impedance in output circuits of RF amplifiers. Due to high impedance, the gain of amplifier is maximum at resonant frequency.
- Both parallel and series resonant circuits are used in induction heating.

LC circuits behave as electronic resonators, which are a key component in many applications:

- Amplifiers
- Contactless cards
- Electronic article surveillance (security tags)
- Filters
- Foster–Seeley discriminator
- Graphics tablets
- Mixers
- Oscillators
- Tuners

## Time domain solution

### Kirchhoff's laws

By Kirchhoff's voltage law, the voltage VC across the capacitor plus the voltage VL across the inductor must equal zero:

$V_{C}+V_{L}=0.$

Likewise, by Kirchhoff's current law, the current through the capacitor equals the current through the inductor:

$I_{C}=I_{L}.$

From the constitutive relations for the circuit elements, we also know that

${\begin{aligned}V_{L}(t)&=L{\frac {\mathrm {d} I_{L}}{\mathrm {d} t}},\\I_{C}(t)&=C{\frac {\mathrm {d} V_{C}}{\mathrm {d} t}}.\end{aligned}}$

### Differential equation

Rearranging and substituting gives the second order differential equation

${\frac {\mathrm {d} ^{2}}{\mathrm {d} t^{2}}}I(t)+{\frac {1}{LC}}I(t)=0.$

The parameter *ω*0, the resonant angular frequency, is defined as

$\omega _{0}={\frac {1}{\sqrt {LC}}}.$

Using this can simplify the differential equation:

${\frac {\mathrm {d} ^{2}}{\mathrm {d} t^{2}}}I(t)+\omega _{0}^{2}I(t)=0.$

The associated Laplace transform is

$s^{2}+\omega _{0}^{2}=0,$

thus

$s=\pm j\omega _{0},$

where j is the imaginary unit.

### Solution

Thus, the complete solution to the differential equation is

$I(t)=Ae^{+j\omega _{0}t}+Be^{-j\omega _{0}t}$

and can be solved for A and B by considering the initial conditions. Since the exponential is complex, the solution represents a sinusoidal alternating current. Since the electric current I is a physical quantity, it must be real-valued. As a result, it can be shown that the constants A and B must be complex conjugates:

$A=B^{*}.$

Now let

$A={\frac {I_{0}}{2}}e^{+j\phi }.$

Therefore,

$B={\frac {I_{0}}{2}}e^{-j\phi }.$

Next, we can use Euler's formula to obtain a real sinusoid with amplitude *I*0, angular frequency *ω*0 = ⁠1/√*LC*⁠, and phase angle $\phi$ .

Thus, the resulting solution becomes

$I(t)=I_{0}\cos \left(\omega _{0}t+\phi \right),$

$V_{L}(t)=L{\frac {\mathrm {d} I}{\mathrm {d} t}}=-\omega _{0}LI_{0}\sin \left(\omega _{0}t+\phi \right).$

### Initial conditions

The initial conditions that would satisfy this result are

$I(0)=I_{0}\cos \phi ,$

$V_{L}(0)=L{\frac {\mathrm {d} I}{\mathrm {d} t}}{\Bigg |}_{t=0}=-\omega _{0}LI_{0}\sin \phi .$

## Series circuit

In the series configuration of the LC circuit, the inductor (L) and capacitor (C) are connected in series, as shown here. The total voltage V across the open terminals is simply the sum of the voltage across the inductor and the voltage across the capacitor. The current I into the positive terminal of the circuit is equal to the current through both the capacitor and the inductor.

${\begin{aligned}V&=V_{L}+V_{C},\\I&=I_{L}=I_{C}.\end{aligned}}$

### Resonance

Inductive reactance $\ X_{\mathsf {L}}=\omega L\$ increases as frequency increases, while capacitive reactance $\ X_{\mathsf {C}}={\frac {1}{\ \omega C\ }}\$ decreases with increase in frequency (defined here as a positive number). At one particular frequency, these two reactances are equal and the voltages across them are equal and opposite in sign; that frequency is called the resonant frequency  *f*0  for the given circuit.

Hence, at resonance,

${\begin{aligned}X_{\mathsf {L}}&=X_{\mathsf {C}}\ ,\\\omega L&={\frac {1}{\ \omega C\ }}~.\end{aligned}}$

Solving for ω, we have

$\omega =\omega _{0}={\frac {1}{\ {\sqrt {LC\;}}\ }}\ ,$

which is defined as the resonant angular frequency of the circuit. Converting angular frequency (in radians per second) into frequency (in Hertz), one has

$f_{0}={\frac {\omega _{0}}{\ 2\pi \ }}={\frac {1}{\ 2\pi {\sqrt {LC\;}}\ }}\ ,$

and

$X_{{\mathsf {L}}0}=X_{{\mathsf {C}}0}={\sqrt {{\frac {\ L\ }{C}}\;}}$

at $\omega _{0}$ .

In a series configuration, XC and XL cancel each other out. In real, rather than idealised, components, the current is opposed, mostly by the resistance of the coil windings. Thus, the current supplied to a series resonant circuit is maximal at resonance.

- In the limit as  *f* → *f*0  current is maximal. Circuit impedance is minimal. In this state, a circuit is called an *acceptor circuit*
- For   *f*  <  *f*0 ,   XL ≪ *X*C ;   hence, the circuit is capacitive.
- For   *f*  >  *f*0 ,   XL ≫ *X*C ;   hence, the circuit is inductive.

### Impedance

In the series configuration, resonance occurs when the complex electrical impedance of the circuit approaches zero.

First consider the impedance of the series LC circuit. The total impedance is given by the sum of the inductive and capacitive impedances:

$Z=Z_{\mathsf {L}}+Z_{\mathsf {C}}~.$

Writing the inductive impedance as  ZL = *jωL*  and capacitive impedance as  ZC = ⁠1/ *j ω C* ⁠  and substituting gives

$Z(\omega )=j\omega L+{\frac {1}{\ j\omega C\ }}~.$

Writing this expression under a common denominator gives

$Z(\omega )=j\left({\frac {\ \omega ^{2}LC-1\ }{\omega C}}\right)~.$

Finally, defining the natural angular frequency as

$\omega _{0}={\frac {1}{\ {\sqrt {LC\;}}\ }}\ ,$

the impedance becomes

$Z(\omega )=j\ L\ \left({\frac {\ \omega ^{2}-\omega _{0}^{2}\ }{\omega }}\right)=j\ \omega _{0}L\ \left({\frac {\omega }{\ \omega _{0}\ }}-{\frac {\ \omega _{0}\ }{\omega }}\right)=j\ {\frac {1}{\ \omega _{0}C\ }}\left({\frac {\omega }{\ \omega _{0}\ }}-{\frac {\ \omega _{0}\ }{\omega }}\right)\ ,$

where $\,\omega _{0}L\ \,$ gives the reactance of the inductor at resonance.

The numerator implies that in the limit as  *ω* → ±*ω*0 , the total impedance  Z  will be zero and otherwise non-zero. Therefore the series LC circuit, when connected in series with a load, will act as a band-pass filter having zero impedance at the resonant frequency of the LC circuit.

## Parallel circuit

When the inductor (L) and capacitor (C) are connected in parallel as shown here, the voltage V across the open terminals is equal to both the voltage across the inductor and the voltage across the capacitor. The total current I flowing into the positive terminal of the circuit is equal to the sum of the current flowing through the inductor and the current flowing through the capacitor:

${\begin{aligned}V&=V_{\mathsf {L}}=V_{\mathsf {C}}\ ,\\I&=I_{\mathsf {L}}+I_{\mathsf {C}}~.\end{aligned}}$

### Resonance

When XL equals XC, the two branch currents are equal and opposite. They cancel each other out to give minimal current in the main line (in principle, for a finite voltage V, there is zero current). Since total current in the main line is minimal, in this state the total impedance is maximal. There is also a larger current circulating in the loop formed by the capacitor and inductor. For a finite voltage V, this circulating current is finite, with value given by the respective voltage-current relationships of the capacitor and inductor. However, for a finite total current I in the main line, in principle, the circulating current would be infinite. In reality, the circulating current in this case is limited by resistance in the circuit, particularly resistance in the inductor windings.

The resonant frequency is given by

$f_{0}={\frac {\omega _{0}}{\ 2\pi \ }}={\frac {1}{\ 2\pi {\sqrt {LC\;}}\ }}~.$

Any branch current is not minimal at resonance, but each is given separately by dividing source voltage (V) by reactance (Z). Hence  *I* = *⁠ V /Z⁠* , as per Ohm's law.

- At  *f*0 , the line current is minimal. The total impedance is maximal. In this state a circuit is called a *rejector circuit*.
- Below  *f*0 , the circuit is inductive.
- Above  *f*0 , the circuit is capacitive.

### Impedance

The same analysis may be applied to the parallel LC circuit. The total impedance is then given by

$Z={\frac {\ Z_{\mathsf {L}}Z_{\mathsf {C}}\ }{Z_{\mathsf {L}}+Z_{\mathsf {C}}}}\ ,$

and after substitution of ZL = *j ω L* and ZC = ⁠1/ *j ω C* ⁠ and simplification, gives

$Z(\omega )=-j\cdot {\frac {\omega L}{\ \omega ^{2}LC-1\ }}~.$

Using

$\omega _{0}={\frac {1}{\ {\sqrt {LC\;}}\ }}\ ,$

it further simplifies to

$Z(\omega )=-j\ \left({\frac {1}{\ C\ }}\right)\left({\frac {\omega }{\ \omega ^{2}-\omega _{0}^{2}\ }}\right)=+j\ {\frac {1}{\ \omega _{0}C\left({\tfrac {\omega _{0}}{\omega }}-{\tfrac {\omega }{\omega _{0}}}\right)\ }}=+j\ {\frac {\omega _{0}L}{\ \left({\tfrac {\omega _{0}}{\omega }}-{\tfrac {\omega }{\omega _{0}}}\right)\ }}~.$

Note that

$\lim _{\omega \to \omega _{0}}Z(\omega )=\infty \ ,$

but for all other values of ω the impedance is finite.

Thus, the parallel LC circuit connected in series with a load will act as band-stop filter having infinite impedance at the resonant frequency of the LC circuit, while the parallel LC circuit connected in parallel with a load will act as band-pass filter.

## Laplace solution

The LC circuit can be solved using the Laplace transform.

We begin by defining the relation between current and voltage across the capacitor and inductor in the usual way:

$v_{\mathrm {C} }(t)=v(t)\ ,~$

$i(t)=C\ {\frac {\mathrm {d} \ v_{\mathrm {C} }}{\mathrm {d} t}}\ ,~$

and

$~v_{\mathrm {L} }(t)=L\ {\frac {\mathrm {d} \ i}{\mathrm {d} t}}\;.$

Then by application of Kirchhoff's laws, we may arrive at the system's governing differential equations

$v_{in}(t)=v_{\mathrm {L} }(t)+v_{\mathrm {C} }(t)=L\ {\frac {\mathrm {d} \ i}{\mathrm {d} t}}+v=L\ C\ {\frac {\mathrm {d} ^{2}\ v}{\mathrm {d} t^{2}}}+v\;.$

With initial conditions $\ v(0)=v_{0}\$ and $\ i(0)=i_{0}=C\cdot v'(0)=C\cdot v'_{0}\;.$

Making the following definitions,

$\omega _{0}\equiv {\frac {1}{\ {\sqrt {L\ C\ }}}}~$

and

$~f(t)\equiv \omega _{0}^{2}\ v_{\mathrm {in} }(t)$

gives

$f(t)={\frac {\ \mathrm {d} ^{2}\ v\ }{\mathrm {d} t^{2}}}+\omega _{0}^{2}\ v\;.$

Now we apply the Laplace transform.

$\operatorname {\mathcal {L}} \left[\ f(t)\ \right]=\operatorname {\mathcal {L}} \left[\ {\frac {\ \mathrm {d} ^{2}\ v\ }{\mathrm {d} t^{2}}}+\omega _{0}^{2}\ v\ \right]\,,$

$F(s)=s^{2}\ V(s)-s\ v_{0}-v'_{0}+\omega _{0}^{2}\ V(s)\;.$

The Laplace transform has turned our differential equation into an algebraic equation. Solving for V in the s domain (frequency domain) is much simpler viz.

$V(s)={\frac {\ s\ v_{0}+v'_{0}+F(s)\ }{s^{2}+\omega _{0}^{2}}}$

$V(s)={\frac {\ s\ v_{0}}{s^{2}+\omega _{0}^{2}}}+{\frac {v'_{0}}{s^{2}+\omega _{0}^{2}}}+{\frac {F(s)\ }{s^{2}+\omega _{0}^{2}}}\,,$

Which can be transformed back to the time domain via the inverse Laplace transform:

$v(t)=\operatorname {\mathcal {L}} ^{-1}\left[\ V(s)\ \right]$

$v(t)=\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {\ s\ v_{0}}{s^{2}+\omega _{0}^{2}}}+{\frac {v'_{0}}{s^{2}+\omega _{0}^{2}}}+{\frac {F(s)\ }{s^{2}+\omega _{0}^{2}}}\ \right],$

For the second summand, an equivalent fraction of $\omega _{0}$ is needed:

$v(t)=v_{0}\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {s}{s^{2}+\omega _{0}^{2}}}\ \right]+v'_{0}\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {\omega _{0}}{\omega _{0}(s^{2}+\omega _{0}^{2})}}\ \right]+\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {F(s)\ }{s^{2}+\omega _{0}^{2}}}\ \right],$

For the second summand, an equivalent fraction of $\omega _{0}$ is needed:

$v(t)=v_{0}\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {s}{s^{2}+\omega _{0}^{2}}}\ \right]+{\frac {v'_{0}}{\omega _{0}}}\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {\omega _{0}}{(s^{2}+\omega _{0}^{2})}}\ \right]+\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {F(s)\ }{s^{2}+\omega _{0}^{2}}}\ \right],$

$v(t)=v_{0}\cos(\omega _{0}\ t)+{\frac {v'_{0}}{\ \omega _{0}\ }}\ \sin(\omega _{0}\ t)+\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {F(s)}{\ s^{2}+\omega _{0}^{2}\ }}\ \right]$

The final term is dependent on the exact form of the input voltage. Two common cases are the Heaviside step function and a sine wave. For a Heaviside step function we get

$v_{\mathrm {in} }(t)=M\ u(t)\,,$

$\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}{\frac {V_{\mathrm {in} }(s)}{\ s^{2}+\omega _{0}^{2}\ }}\ \right]~=~\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}\ M\ {\frac {1}{\ s\ (s^{2}+\omega _{0}^{2})\ }}\ \right]~=~M\ {\Bigl (}1-\cos(\omega _{0}\ t){\Bigr )}\,,$

$v(t)=v_{0}\ \cos(\omega _{0}\ t)+{\frac {v'_{0}}{\omega _{0}}}\ \sin(\omega _{0}\ t)+M\ {\Bigl (}1-\cos(\omega _{0}\ t){\Bigr )}\;.$

For the case of a sinusoidal function as input we get:

$v_{\mathrm {in} }(t)=U\ \sin(\omega _{\mathrm {f} }\ t)\Rightarrow V_{\mathrm {in} }(s)={\frac {\ U\ \omega _{\mathrm {f} }\ }{\ s^{2}+\omega _{\mathrm {f} }^{2}\ }}\,$

where U is the amplitude and $\omega _{f}$ the frequency of the applied function.

$\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}\ {\frac {1}{\ s^{2}+\omega _{0}^{2}\ }}\ {\frac {U\ \omega _{\mathrm {f} }}{\ s^{2}+\omega _{\mathrm {f} }^{2}\ }}\ \right]$

Using the partial fraction method:

$\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}\ U\ \omega _{\mathrm {f} }{\frac {1}{\ s^{2}+\omega _{0}^{2}\ }}\ {\frac {1}{\ s^{2}+\omega _{\mathrm {f} }^{2}\ }}\ \right]=\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}\ U\ \omega _{\mathrm {f} }{\frac {A+Bs}{\ s^{2}+\omega _{0}^{2}\ }}\ +{\frac {C+Ds}{\ s^{2}+\omega _{\mathrm {f} }^{2}\ }}\ \right]$

Simplifiying on both sides

$1=(A+Bs)(\ s^{2}+\omega _{\mathrm {f} }^{2}\ )+(C+Ds)(\ s^{2}+\omega _{0}^{2}\ )$

$1=(A\ s^{2}+\ A\ \omega _{\mathrm {f} }^{2}\ +\ B\ s^{3}+\ B\ \omega _{\mathrm {f} }^{2}\ )+(C\ s^{2}+\ C\ \omega _{0}^{2}\ +\ D\ s^{3}+\ D\ s\omega _{0}^{2}\ )$

$1=s^{3}(B\ +\ D\ )+s^{2}(A\ +\ C)+s(B\ \omega _{\mathrm {f} }^{2}+\ D\ \omega _{0}^{2})+(A\ \omega _{\mathrm {f} }^{2}\ +\ C\ \omega _{0}^{2})$

We solve the equation for A, B and C:

$A+C=0\Rightarrow C=-A$

$A\ \omega _{\mathrm {f} }^{2}\ +\ C\ \omega _{0}^{2}=1\Rightarrow A\ \omega _{\mathrm {f} }^{2}\ -\ A\ \omega _{0}^{2}=1$

$\Rightarrow A\ ={\frac {1}{(\omega _{\mathrm {f} }^{2}\ -\omega _{0}^{2})}}$

$\Rightarrow C\ =-{\frac {1}{(\omega _{\mathrm {f} }^{2}\ -\omega _{0}^{2})}}$

$B+C=0$

$B\ \omega _{\mathrm {f} }^{2}+\ D\ \omega _{0}^{2}=0\Rightarrow B\ \omega _{\mathrm {f} }^{2}-\ B\ \omega _{0}^{2}=0\Rightarrow B\ (\omega _{\mathrm {f} }^{2}-\omega _{0}^{2})=0$

$\Rightarrow B=0,\ D=0$

Substitute the values of A, B and C:

$\operatorname {\mathcal {L}} ^{-1}\left[\ \omega _{0}^{2}\ U\ \omega _{\mathrm {f} }{\frac {\frac {1}{(\omega _{\mathrm {f} }^{2}\ -\omega _{0}^{2})}}{\ s^{2}+\omega _{0}^{2}\ }}+{\frac {-{\frac {1}{(\omega _{\mathrm {f} }^{2}\ -\omega _{0}^{2})}}}{\ s^{2}+\omega _{\mathrm {f} }^{2}\ }}\ \right]$

Isolating the constant and using equivalent fractions to adjust for lack of numerator:

${\frac {\ \omega _{0}^{2}\ U\omega _{\mathrm {f} }\ }{\ \omega _{\mathrm {f} }^{2}-\omega _{0}^{2}\ }}\operatorname {\mathcal {L}} ^{-1}\left[\left({\frac {\omega _{0}}{\omega _{0}(s^{2}+\omega _{0}^{2})}}-{\frac {\omega _{f}}{\omega _{f}(s^{2}+\omega _{f}^{2})}}\right)\right]\,$

Performing the reverse Laplace transform on each summands:

${\frac {\ \omega _{0}^{2}\ U\omega _{\mathrm {f} }\ }{\ \omega _{\mathrm {f} }^{2}-\omega _{0}^{2}\ }}\left(\operatorname {\mathcal {L}} ^{-1}\left[\ {\frac {1}{\omega _{0}}}{\frac {\omega _{0}}{(s^{2}+\omega _{0}^{2})}}\right]-\operatorname {\mathcal {L}} ^{-1}\left[{\frac {1}{\omega _{\mathrm {f} }\ }}{\frac {\omega _{\mathrm {f} }\ }{(s^{2}+\omega _{f}^{2})}}\right]\right)\,$

${\frac {\ \omega _{0}^{2}\ U\omega _{\mathrm {f} }\ }{\ \omega _{\mathrm {f} }^{2}-\omega _{0}^{2}\ }}\left({\frac {1}{\omega _{0}}}\operatorname {\mathcal {L}} ^{-1}\left[{\frac {\omega _{0}}{(s^{2}+\omega _{0}^{2})}}\right]-{\frac {1}{\omega _{\mathrm {f} }\ }}\operatorname {\mathcal {L}} ^{-1}\left[{\frac {\omega _{\mathrm {f} }\ }{(s^{2}+\omega _{f}^{2})}}\right]\right)\,$

$v_{\mathrm {in} }(t)={\frac {\ \omega _{0}^{2}\ U\ \omega _{\mathrm {f} }\ }{\omega _{\mathrm {f} }^{2}-\omega _{0}^{2}}}\left({\frac {1}{\omega _{0}}}\ \sin(\omega _{0}\ t)-{\frac {1}{\ \omega _{\mathrm {f} }\ }}\ \sin(\omega _{\mathrm {f} }\ t)\right)\;,$

Using initial conditions in the Laplace solution:

$v(t)=v_{0}\cos(\omega _{0}\ t)+{\frac {v'_{0}}{\omega _{0}\ }}\ \sin(\omega _{0}\ t)+{\frac {\omega _{0}^{2}\ U\ \omega _{\mathrm {f} }}{\ \omega _{\mathrm {f} }^{2}-\omega _{0}^{2}\ }}\left({\frac {1}{\omega _{0}}}\ \sin(\omega _{0}\ t)-{\frac {1}{\ \omega _{\mathrm {f} }\ }}\ \sin(\omega _{\mathrm {f} }\ t)\right)\;.$

## History

The first evidence that a capacitor and inductor could produce electrical oscillations was discovered in 1826 by French scientist Felix Savary. He found that when a Leyden jar was discharged through a wire wound around an iron needle, sometimes the needle was left magnetized in one direction and sometimes in the opposite direction. He correctly deduced that this was caused by a damped oscillating discharge current in the wire, which reversed the magnetization of the needle back and forth until it was too small to have an effect, leaving the needle magnetized in a random direction. American physicist Joseph Henry repeated Savary's experiment in 1842 and came to the same conclusion, apparently independently.

Irish scientist William Thomson (Lord Kelvin) in 1853 showed mathematically that the discharge of a Leyden jar through an inductance should be oscillatory, and derived its resonant frequency. British radio researcher Oliver Lodge, by discharging a large battery of Leyden jars through a long wire, created a tuned circuit with its resonant frequency in the audio range, which produced a musical tone from the spark when it was discharged. In 1857, German physicist Berend Wilhelm Feddersen photographed the spark produced by a resonant Leyden jar circuit in a rotating mirror, providing visible evidence of the oscillations. In 1868, Scottish physicist James Clerk Maxwell calculated the effect of applying an alternating current to a circuit with inductance and capacitance, showing that the response is maximum at the resonant frequency. The first example of an electrical resonance curve was published in 1887 by German physicist Heinrich Hertz in his pioneering paper on the discovery of radio waves, showing the length of spark obtainable from his spark-gap LC resonator detectors as a function of frequency.

One of the first demonstrations of resonance between tuned circuits was Lodge's "syntonic jars" experiment around 1889. He placed two resonant circuits next to each other, each consisting of a Leyden jar connected to an adjustable one-turn coil with a spark gap. When a high voltage from an induction coil was applied to one tuned circuit, creating sparks and thus oscillating currents, sparks were excited in the other tuned circuit only when the circuits were adjusted to resonance. Lodge and some English scientists preferred the term "*syntony*" for this effect, but the term "*resonance*" eventually stuck. The first practical use for LC circuits was in the 1890s in spark-gap radio transmitters to allow the receiver and transmitter to be tuned to the same frequency. The first patent for a radio system that allowed tuning was filed by Lodge in 1897, although the first practical systems were invented in 1900 by Italian radio pioneer Guglielmo Marconi.
