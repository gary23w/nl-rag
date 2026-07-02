---
title: "Bang–bang control"
source: https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control
domain: control-systems
license: CC-BY-SA-4.0
tags: control theory, pid controller, feedback loop, control system, kalman filter, servo
fetched: 2026-07-02
---

# Bang–bang control

In control theory, a **bang–bang controller** (**hysteresis**, **2 step** or **on–off** controller), is a feedback controller that switches abruptly between two states. These controllers may be realized in terms of any element that provides hysteresis. They are often used to control a plant that accepts a binary input, for example a furnace that is either completely on or completely off. Most common residential thermostats are bang–bang controllers. The Heaviside step function in its discrete form is an example of a **bang–bang control** signal. Due to the discontinuous control signal, systems that include bang–bang controllers are variable structure systems, and bang–bang controllers are thus variable structure controllers.

## Bang–bang solutions in optimal control

In optimal control problems, it is sometimes the case that a control is restricted to be between a lower and an upper bound. If the optimal control switches from one extreme to the other (i.e., is strictly never in between the bounds), then that control is referred to as a bang–bang solution.

Bang–bang controls frequently arise in minimum-time problems. For example, if it is desired for a car starting at rest to arrive at a certain position ahead of the car in the shortest possible time, the solution is to apply maximum acceleration until the unique *switching point*, and then apply maximum braking to come to rest exactly at the desired position.

A familiar everyday example is bringing water to a boil in the shortest time, which is achieved by applying full heat, then turning it off when the water reaches a boil. A closed-loop household example is most thermostats, wherein the heating element or air conditioning compressor is either running or not, depending upon whether the measured temperature is above or below the setpoint.

Bang–bang solutions also arise when the Hamiltonian is linear in the control variable; application of Pontryagin's minimum or maximum principle will then lead to pushing the control to its upper or lower bound depending on the sign of the coefficient of *u* in the Hamiltonian.

In summary, bang–bang controls are actually *optimal* controls in some cases, although they are also often implemented because of simplicity or convenience.

## Practical implications of bang–bang control

Mathematically or within a computing context there may be no problems, but the physical realization of bang–bang control systems gives rise to several complications.

First, depending on the width of the hysteresis gap and inertia in the process, there will be an oscillating error signal around the desired set point value (e.g., temperature), often saw-tooth shaped. Room temperature may become uncomfortable just before the next switch 'ON' event. Alternatively, a narrow hysteresis gap will lead to frequent on/off switching, which is often undesirable (e.g. an electrically ignited gas heater).

Second, the onset of the step function may entail, for example, a high electrical current and/or sudden heating and expansion of metal vessels, ultimately leading to metal fatigue or other wear-and-tear effects. Where possible, continuous control, such as in PID control, will avoid problems caused by the brisk state transitions that are the consequence of bang–bang control.
