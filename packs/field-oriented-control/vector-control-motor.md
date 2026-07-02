---
title: "Field-oriented control"
source: https://en.wikipedia.org/wiki/Vector_control_(motor)
domain: field-oriented-control
license: CC-BY-SA-4.0
tags: vector control motor, Clarke transformation, space vector modulation, field-oriented control
fetched: 2026-07-02
---

# Field-oriented control

(Redirected from

Vector control (motor)

)

**Field-oriented control** (**FOC**), also called **vector control**, is a variable-frequency drive (VFD) control method in which the stator currents of a three-phase AC motor (like for example BLDC) are identified as two orthogonal components that can be visualized with a vector. One component defines the magnetic flux of the motor, the other the torque. The regulation of magnetic flux in electric drives is sometimes described as flux control, referring to the decoupled control of flux and torque in field-oriented control systems. The control system of the drive calculates the corresponding current component references from the flux and torque references given by the drive's speed control. Typically proportional-integral (PI) controllers are used to keep the measured current components at their reference values. The pulse-width modulation of the variable-frequency drive defines the transistor switching according to the stator voltage references that are the output of the PI current controllers.

FOC is used to control AC synchronous and induction motors. It was originally developed for high-performance motor applications that are required to operate smoothly over the full speed range, generate full torque at zero speed, and have high dynamic performance including fast acceleration and deceleration. However, it is becoming increasingly attractive for lower performance applications as well due to FOC's motor size, cost and power consumption reduction superiority. It is expected that with increasing computational power of the microprocessors it will eventually nearly universally displace single-variable scalar control (volts-per-Hertz, V/f control).

## Development history

Technische Universität Darmstadt's K. Hasse and Siemens' F. Blaschke pioneered vector control of AC motors starting in 1968 and in the early 1970s. Hasse in terms of proposing indirect vector control, Blaschke in terms of proposing direct vector control. Technical University Braunschweig's Werner Leonhard further developed FOC techniques and was instrumental in opening up opportunities for AC drives to be a competitive alternative to DC drives.

Yet it was not until after the commercialization of microprocessors, that is in the early 1980s, that general purpose AC drives became available. Barriers to use FOC for AC drive applications included higher cost and complexity and lower maintainability compared to DC drives, FOC having until then required many electronic components in terms of sensors, amplifiers and so on.

The Park transformation has long been widely used in the analysis and study of synchronous and induction machines. The transformation is by far the single most important concept needed for an understanding of how FOC works, the concept having been first conceptualized in a 1929 paper authored by Robert H. Park. Park's paper was ranked second most important in terms of impact from among all power engineering related papers ever published in the twentieth century. The novelty of Park's work involves his ability to transform any related machine's linear differential equation set from one with time varying coefficients to another with time *invariant* coefficients resulting in a linear time-invariant system or LTI system.

## Technical overview

Overview of key competing variable-frequency drive control platforms:

| VFD, with sensor or sensorless | Scalar control V/f (volts per hertz) control Vector control DTC (Direct torque control) Classic DTC Space vector modulation based DTC FOC (Field‑oriented control) Direct FOC Indirect FOC MPC (Model predictive control) Predictive torque control Predictive current control |
|---|---|
|   |   |

While the analysis of AC drive controls can be technically quite involved ("See also" section), such analysis invariably starts with modeling of the drive-motor circuit involved along the lines of accompanying signal flow graph and equations.

Induction motor model equations

${\begin{aligned}&\tau _{\sigma }'{\frac {di_{s}}{d\tau }}+i_{s}{=}-\omega _{k}\tau _{\sigma }'i_{s}+{\frac {k_{r}}{\tau _{r}r_{\sigma }}}(1-jr_{\tau }\omega _{m})\psi _{r}+{\frac {1}{r_{\sigma }}}u_{s}&&(1)\\&\tau _{r}{\frac {d\psi _{r}}{d\tau }}+\psi _{r}=-j(\omega _{k}-\omega _{m})\tau _{r}\psi _{r}+l_{m}i_{s}&&(2)\end{aligned}}$

where

${\begin{aligned}\sigma _{r}'={\frac {\sigma l_{s}}{r_{\sigma }}}&&r_{\sigma }=r_{s}+k_{r}^{2}r_{r}&&k_{r}={\frac {l_{m}}{l_{r}}}&&\tau =\omega _{sR}\end{aligned}}$

${\begin{aligned}&\sigma =1-{\frac {l_{m}^{2}}{l_{r}l_{s}}}={\text{total leakage coefficient}}\\&\omega _{sR}={\text{nominal stator frequency}}\end{aligned}}$

| Basic parameter symbols |   |
|---|---|
| *i* | current |
| *k* | coupling factor of respective winding |
| *l* | inductance |
| *r* | resistance |
| *t* | time |
| *T* | torque |
| *u* | voltage |
| $\psi$ | flux linkage |
| $\tau$ | normalized time |
| $\tau$ | time constant (T.C.) with subscript |
| $\omega$ | angular velocity |
| $\sigma l_{s}$ | total leakage inductance |

| Subscripts and superscripts |   |
|---|---|
| *e* | electromechanical |
| *i* | induced voltage |
| *k* | referred to k-coordinates |
| *L* | load |
| *m* | mutual (inductance) |
| *m* | mechanical (T.C., angular velocity) |
| *r* | rotor |
| *R* | rated value |
| *s* | stator |
| *'* | denotes transient time constant |

In vector control, an AC induction or synchronous motor is controlled under all operating conditions like a separately excited DC motor. That is, the AC motor behaves like a DC motor in which the field flux linkage and armature flux linkage created by the respective field and armature (or torque component) currents are orthogonally aligned such that, when torque is controlled, the field flux linkage is not affected, hence enabling dynamic torque response.

Vector control accordingly generates a three-phase PWM motor voltage output derived from a complex voltage vector to control a complex current vector derived from motor's three-phase stator current input through projections or rotations back and forth between the three-phase speed and time dependent system and these vectors' rotating reference-frame two-coordinate time invariant system.

Such complex stator current space vector can be defined in a (d,q) coordinate system with orthogonal components along d (direct) and q (quadrature) axes such that field flux linkage component of current is aligned along the d axis and torque component of current is aligned along the q axis. The induction motor's (d,q) coordinate system can be superimposed to the motor's instantaneous (a,b,c) three-phase sinusoidal system as shown in accompanying image (phases b & c not shown for clarity). Components of the (d,q) system current vector allow conventional control such as proportional and integral, or PI, control, as with a DC motor.

Projections associated with the (d,q) coordinate system typically involve:

- Forward projection from instantaneous currents to (a,b,c) complex stator current space vector representation of the three-phase sinusoidal system.
- Forward three-to-two phase, (a,b,c)-to-( $\alpha$ , $\beta$ ) projection using the Clarke transformation. Vector control implementations usually assume ungrounded motor with balanced three-phase currents such that only two motor current phases need to be sensed. Also, backward two-to-three phase, ( $\alpha$ , $\beta$ )-to-(a,b,c) projection uses space vector PWM modulator or inverse Clarke transformation and one of the other PWM modulators.
- Forward and backward two-to-two phase,( $\alpha$ , $\beta$ )-to-(d,q) and (d,q)-to-( $\alpha$ , $\beta$ ) projections using the Park and inverse Park transformations, respectively.

The idea of using the park transform is to convert the system of three phase currents and voltages into a two coordinate linear time-invariant system. By making the system LTI is what enables the use of simple and easy to implement PI controllers, and also simplifies the control of flux and torque producing currents.

However, it is not uncommon for sources to use combined transform three-to-two, (a,b,c)-to-(d,q) and inverse projections.

While (d,q) coordinate system rotation can arbitrarily be set to any speed, there are three preferred speeds or reference frames:

- Stationary reference frame where (d,q) coordinate system does not rotate;
- Synchronously rotating reference frame where (d,q) coordinate system rotates at synchronous speed;
- Rotor reference frame where (d,q) coordinate system rotates at rotor speed.

Decoupled torque and field currents can thus be derived from raw stator current inputs for control algorithm development.

Whereas magnetic field and torque components in DC motors can be operated relatively simply by separately controlling the respective field and armature currents, economical control of AC motors in variable speed application has required development of microprocessor-based controls with all AC drives now using powerful digital signal processing (DSP) technology.

Inverters can be implemented as either open-loop sensorless or closed-loop FOC, the key limitation of open-loop operation being minimum speed possible at 100% torque, namely, about 0.8 Hz compared to standstill for closed-loop operation.

There are two vector control methods, direct or feedback vector control (DFOC) and indirect or feedforward vector control (IFOC), IFOC being more commonly used because in closed-loop mode such drives more easily operate throughout the speed range from zero speed to high-speed field-weakening. In DFOC, flux magnitude and angle feedback signals are directly calculated using so-called voltage or current models. In IFOC, flux space angle feedforward and flux magnitude signals first measure stator currents and rotor speed for then deriving flux space angle proper by summing the rotor angle corresponding to the rotor speed and the calculated reference value of slip angle corresponding to the slip frequency.

Sensorless control (see the Sensorless FOC block diagram) of AC drives is attractive for cost and reliability considerations. Sensorless control requires derivation of rotor speed information from measured stator voltage and currents in combination with open-loop estimators or closed-loop observers.

## Application

1. Stator phase currents are measured, converted to complex space vector in (a,b,c) coordinate system.
2. Current is converted to ( $\alpha$ , $\beta$ ) coordinate system. Transformed to a coordinate system rotating in rotor reference frame, rotor position is derived by integrating the speed by means of speed measurement sensor.
3. Rotor flux linkage vector is estimated by multiplying the stator current vector with magnetizing inductance Lm and low-pass filtering the result with the rotor no-load time constant Lr/Rr, namely, the rotor inductance to rotor resistance ratio.
4. Current vector is converted to (d,q) coordinate system.
5. d-axis component of the stator current vector is used to control the rotor flux linkage and the imaginary q-axis component is used to control the motor torque. While PI controllers can be used to control these currents, bang-bang type current control provides better dynamic performance.
6. PI controllers provide (d,q) coordinate voltage components. A decoupling term is sometimes added to the controller output to improve control performance to mitigate cross coupling or big and rapid changes in speed, current and flux linkage. PI-controller also sometimes need low-pass filtering at the input or output to prevent the current ripple due to transistor switching from being amplified excessively and destabilizing the control. However, such filtering also limits the dynamic control system performance. High switching frequency (typically more than 10 kHz) is typically required to minimize filtering requirements for high-performance drives such as servo drives.
7. Voltage components are transformed from (d,q) coordinate system to ( $\alpha$ , $\beta$ ) coordinate system.
8. Voltage components are transformed from ( $\alpha$ , $\beta$ ) coordinate system to (a,b,c) coordinate system or fed in Pulse-Width Modulation (PWM) modulator, or both, for signaling to the power inverter section.

Significant aspects of vector control application:

- Speed or position measurement or some sort of estimation is needed.
- Torque and flux can be changed reasonably fast, in less than 5-10 milliseconds, by changing the references.
- The step response has some overshoot if PI control is used.
- The switching frequency of the transistors is usually constant and set by the modulator.
- The accuracy of the torque depends on the accuracy of the motor parameters used in the control. Thus large errors due to for example rotor temperature changes often are encountered.
- Reasonable processor performance is required; typically the control algorithm is calculated every PWM cycle.

Although the vector control algorithm is more complicated than the Direct Torque Control (DTC), the algorithm need not be calculated as frequently as the DTC algorithm. Also the current sensors need not be the best in the market. Thus the cost of the processor and other control hardware is lower making it suitable for applications where the ultimate performance of DTC is not required.
