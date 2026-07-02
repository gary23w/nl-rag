---
title: "Widlar current source"
source: https://en.wikipedia.org/wiki/Widlar_current_mirror
domain: bandgap-reference
license: CC-BY-SA-4.0
tags: bandgap voltage reference, Brokaw bandgap reference, Widlar current mirror, temperature compensation
fetched: 2026-07-02
---

# Widlar current source

(Redirected from

Widlar current mirror

)

A **Widlar current source** is a modification of the basic two-transistor current mirror that incorporates an emitter degeneration resistor for only the output transistor, enabling the current source to generate low currents using only moderate resistor values.

The Widlar circuit may be used with bipolar transistors, MOS transistors, and even vacuum tubes. An example application is the 741 operational amplifier, and Widlar used the circuit as a part in many designs.

This circuit is named after its inventor, Bob Widlar, and was patented in 1967.

## DC analysis

Figure 1 is an example Widlar current source using bipolar transistors, where the emitter resistance *R*2 is connected to the output transistor Q2, and has the effect of reducing the current in Q2 relative to Q1. The key to this circuit is that the voltage drop across the resistance *R*2 subtracts from the base-emitter voltage of transistor Q2, thereby turning this transistor off compared to transistor Q1. This observation is expressed by equating the base voltage expressions found on either side of the circuit in Figure 1 as:

${\begin{aligned}&V_{\text{B}}=V_{\text{BE1}}=V_{\text{BE2}}+(\beta _{2}+1)I_{\text{B2}}R_{2}\\\Rightarrow {}&{\frac {1}{R_{2}}}\left(V_{\text{BE1}}-V_{\text{BE2}}\right)=(\beta _{2}+1)I_{\text{B2}}\ ,\end{aligned}}$

where *β*2 is the beta-value of the output transistor, which is not the same as that of the input transistor, in part because the currents in the two transistors are very different. The variable *I*B2 is the base current of the output transistor, *V*BE refers to base-emitter voltage. This equation implies (using the Shockley diode equation):

*Eq. 1*

${\begin{aligned}(\beta _{2}+1)I_{\text{B2}}&=\left(1+{\frac {1}{\beta _{2}}}\right)I_{\text{C2}}={\frac {1}{R_{2}}}\left(V_{\text{BE1}}-V_{\text{BE2}}\right)\\&={\frac {V_{\text{T}}}{R_{2}}}\left[\ln \left(I_{\text{C1}}/I_{\text{S1}}\right)-\ln \left(I_{\text{C2}}/I_{\text{S2}}\right)\right]={\frac {V_{\text{T}}}{R_{2}}}\ln \left({\frac {I_{\text{C1}}I_{\text{S2}}}{I_{\text{C2}}I_{\text{S1}}}}\right)\ ,\end{aligned}}$

where *V*T is the thermal voltage.

This equation makes the approximation that the currents are both much larger than the scale currents, *I*S1 and *I*S2; an approximation valid except for current levels near cut off. In the following, the scale currents are assumed to be identical; in practice, this needs to be specifically arranged.

## Design procedure with specified currents

To design the mirror, the output current must be related to the two resistor values *R*1 and *R*2. A basic observation is that the output transistor is in active mode only so long as its collector-base voltage is non-zero. Thus, the simplest bias condition for design of the mirror sets the applied voltage *V*A to equal the base voltage *V*B. This minimum useful value of *V*A is called the *compliance voltage* of the current source. With that bias condition, the Early effect plays no role in the design.

These considerations suggest the following design procedure:

- Select the desired output current, *I*O = *I*C2.
- Select the reference current, *I*R1, assumed to be larger than the output current, probably considerably larger (that is the purpose of the circuit).
- Determine the input collector current of Q1, *I*C1: $I_{\text{C1}}={\frac {\beta _{1}}{\beta _{1}+1}}\left(I_{\text{R1}}-{\frac {I_{\text{C2}}}{\beta _{2}}}\right)\ .$
- Determine the base voltage *V*BE1 using the Shockley diode law $V_{\text{BE1}}=V_{\text{T}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{S}}}}\right)=V_{\text{A}}\ .$

where

I

S

is a device parameter sometimes called the

scale current

.

The value of base voltage also sets the compliance voltage

V

A

=

V

BE1

. This voltage is the lowest voltage for which the mirror works properly.

- Determine *R*1: $R_{1}={\frac {V_{\text{CC}}-V_{\text{A}}}{I_{\text{R1}}}}\ .$
- Determine the emitter leg resistance *R*2 using *Eq. 1* (to reduce clutter, the scale currents are chosen equal): $R_{2}={\frac {V_{\text{T}}}{\left(1+{\frac {1}{\beta _{2}}}\right)I_{\text{C2}}}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)\ .$

## Finding the current with given resistor values

The inverse of the design problem is finding the current when the resistor values are known. An iterative method is described next. Assume the current source is biased so the collector-base voltage of the output transistor Q2 is zero. The current through *R*1 is the input or reference current given as,

${\begin{aligned}I_{\text{R1}}&=I_{\text{C1}}+I_{\text{B1}}+I_{\text{B2}}\\&=I_{\text{C1}}+{\frac {I_{\text{C1}}}{\beta _{1}}}+{\frac {I_{\text{C2}}}{\beta _{2}}}\\&={\frac {1}{R_{1}}}\left(V_{\text{CC}}-V_{\text{BE1}}\right)\end{aligned}}$

Rearranging, *I*C1 is found as:

*Eq. 2*

$I_{\text{C1}}={\frac {\beta _{1}}{\beta _{1}+1}}\left({\frac {V_{\text{CC}}-V_{\text{BE1}}}{R_{1}}}-{\frac {I_{\text{C2}}}{\beta _{2}}}\right)$

The diode equation provides:

*Eq. 3*

$V_{\text{BE1}}=V_{\text{T}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{S1}}}}\right)\ .$

*Eq.1* provides:

$I_{\text{C2}}={\frac {V_{\text{T}}}{\left(1+{\frac {1}{\beta _{2}}}\right)R_{2}}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)\ .$

These three relations are a nonlinear, implicit determination for the currents that can be solved by iteration.

- We guess starting values for *I*C1 and *I*C2.
- We find a value for *V*BE1: $V_{\text{BE1}}=V_{\text{T}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{S1}}}}\right)\ .$
- We find a new value for *I*C1: $I_{\text{C1}}={\frac {\beta _{1}}{\beta _{1}+1}}\left({\frac {V_{\text{CC}}-V_{\text{BE1}}}{R_{1}}}-{\frac {I_{\text{C2}}}{\beta _{2}}}\right)$
- We find a new value for *I*C2: $I_{\text{C2}}={\frac {V_{\text{T}}}{\left(1+{\frac {1}{\beta _{2}}}\right)R_{2}}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)\ .$

This procedure is repeated to convergence, and is set up conveniently in a spreadsheet. One simply uses a macro to copy the values into the spreadsheet cells holding the initial values to obtain the solution in short order.

Note that with the circuit as shown, if *V*CC changes, the output current will change. Hence, to keep the output current constant despite fluctuations in *V*CC, the circuit should be driven by a constant current source rather than using the resistor *R*1.

### Exact solution

The transcendental equations above can be solved exactly in terms of the Lambert W function.

## Output impedance

An important property of a current source is its small signal incremental output impedance, which should ideally be infinite. The Widlar circuit introduces local current feedback for transistor $\scriptstyle Q_{2}$ . Any increase in the current in Q2 increases the voltage drop across *R*2, reducing the *V*BE for Q2, thereby countering the increase in current. This feedback means the output impedance of the circuit is increased, because the feedback involving *R*2 forces use of a larger voltage to drive a given current.

Output resistance is found using a small-signal model for the circuit, shown in Figure 2. Transistor Q1 is replaced by its small-signal emitter resistance *r*E because it is diode connected. Transistor Q2 is replaced with its hybrid-pi model. A test current *I*x is attached at the output.

Using the figure, the output resistance is determined using Kirchhoff's laws. Using Kirchhoff's voltage law from the ground on the left to the ground connection of *R*2:

$I_{\text{b}}\left[(R_{1}\parallel r_{\text{E}})+r_{\pi }\right]+[I_{\text{x}}+I_{\text{b}}]R_{2}=0\ .$

Rearranging:

$I_{\text{b}}=-I_{\text{x}}{\frac {R_{2}}{(R_{1}\parallel r_{\text{E}})+r_{\pi }+R_{2}}}\ .$

Using Kirchhoff's voltage law from the ground connection of *R*2 to the ground of the test current:

$V_{\text{x}}=I_{\text{x}}(R_{2}+r_{\text{O}})+I_{\text{b}}(R_{2}-\beta r_{\text{O}})\ ,$

or, substituting for *I*b:

*Eq. 4*

$R_{\text{O}}={\frac {V_{\text{x}}}{I_{\text{x}}}}=r_{\text{O}}\left[1+{\frac {\beta R_{2}}{(R_{1}\parallel r_{\text{E}})+r_{\pi }+R_{2}}}\right]$

$+\ R_{2}\left[{\frac {(R_{1}\parallel r_{\text{E}})+r_{\pi }}{(R_{1}\parallel r_{\text{E}})+r_{\pi }+R_{2}}}\right]\ .$

According to *Eq. 4*, the output resistance of the Widlar current source is increased over that of the output transistor itself (which is *r*O) so long as *R*2 is large enough compared to the *r*π of the output transistor (large resistances *R*2 make the factor multiplying *r*O approach the value (*β* + 1)). The output transistor carries a low current, making *r*π large, and increase in *R*2 tends to reduce this current further, causing a correlated increase in *r*π. Therefore, a goal of *R*2 ≫ *r*π can be unrealistic, and further discussion is provided below. The resistance *R*1∥*r*E usually is small because the emitter resistance *r*E usually is only a few ohms.

### Current dependence of output resistance

The current dependence of the resistances *r*π and *r*O is discussed in the article hybrid-pi model. The current dependence of the resistor values is:

$r_{\pi }={\frac {v_{\text{be}}}{i_{\text{b}}}}{\Bigg |}_{v_{\text{ce}}=0}={\frac {V_{\text{T}}}{I_{\text{B2}}}}=\beta _{2}{\frac {V_{\text{T}}}{I_{\text{C2}}}}\ ,$

and

$r_{\text{O}}={\frac {v_{\text{ce}}}{i_{\text{c}}}}{\Bigg |}_{v_{\text{be}}=0}={\frac {V_{\text{A}}}{I_{\text{C2}}}}$

is the output resistance due to the Early effect when *V*CB = 0 V (device parameter *V*A is the Early voltage).

From earlier in this article (setting the scale currents equal for convenience): *Eq. 5*

$R_{2}={\frac {V_{\text{T}}}{\left(1+{\frac {1}{\beta _{2}}}\right)I_{\text{C2}}}}\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)\ .$

Consequently, for the usual case of small *r*E, and neglecting the second term in *R*O with the expectation that the leading term involving *r*O is much larger: *Eq. 6*

${\begin{aligned}R_{\text{O}}&\approx r_{\text{O}}\left(1+{\frac {\beta _{2}R_{2}}{r_{\pi }+R_{2}}}\right)\\&=r_{\text{O}}\left(1+{\frac {\beta _{2}\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)}{\beta _{2}+1+\ln \left({\frac {I_{\text{C1}}}{I_{\text{C2}}}}\right)}}\right)\end{aligned}}$

where the last form is found by substituting *Eq. 5* for *R*2. *Eq. 6* shows that a value of output resistance much larger than *r*O of the output transistor results only for designs with *I*C1 >> *I*C2. Figure 3 shows that the circuit output resistance *R*O is not determined so much by feedback as by the current dependence of the resistance *r*O of the output transistor (the output resistance in Figure 3 varies four orders of magnitude, while the feedback factor varies only by one order of magnitude).

Increase of *I*C1 to increase the feedback factor also results in increased compliance voltage, not a good thing as that means the current source operates over a more restricted voltage range. So, for example, with a goal for compliance voltage set, placing an upper limit upon *I*C1, and with a goal for output resistance to be met, the maximum value of output current *I*C2 is limited.

The center panel in Figure 3 shows the design trade-off between emitter leg resistance and the output current: a lower output current requires a larger leg resistor, and hence a larger area for the design. An upper bound on area therefore sets a lower bound on the output current and an upper bound on the circuit output resistance.

*Eq. 6* for *R*O depends upon selecting a value of *R*2 according to *Eq. 5*. That means *Eq. 6* is not a *circuit behavior* formula, but a *design value* equation. Once *R*2 is selected for a particular design objective using *Eq. 5*, thereafter its value is fixed. If circuit operation causes currents, voltages or temperatures to deviate from the designed-for values; then to predict changes in *R*O caused by such deviations, *Eq. 4* should be used, not *Eq. 6*.
