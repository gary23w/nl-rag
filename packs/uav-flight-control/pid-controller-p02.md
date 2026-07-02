---
title: "PID controller (part 2/2)"
source: https://en.wikipedia.org/wiki/PID_controller
domain: uav-flight-control
license: CC-BY-SA-4.0
tags: uav flight control, pid controller, inertial measurement unit, attitude control
fetched: 2026-07-02
part: 2/2
---

## Modifications to the algorithm

The basic PID algorithm presents some challenges in control applications that have been addressed by minor modifications to the PID form.

### Integral windup

One common problem resulting from the ideal PID implementations is integral windup. Following a large change in setpoint, the integral term can accumulate an error larger than the maximal value for the regulation variable (windup), thus the system overshoots and continues to increase until this accumulated error is unwound. This problem can be addressed by:

- Disabling the integration until the PV has entered the controllable region
- Preventing the integral term from accumulating above or below pre-determined bounds
- Back-calculating the integral term to constrain the regulator output within feasible bounds.

### Overshooting from known disturbances

For example, a PID loop is used to control the temperature of an electric resistance furnace where the system has stabilized. Now, when the door is opened and something cold is put into the furnace, the temperature drops below the setpoint. The integral function of the controller tends to compensate for error by introducing another error in the positive direction. This overshoot can be avoided by freezing of the integral function after the opening of the door for the time the control loop typically needs to reheat the furnace.

### PI controller

A **PI controller** (proportional–integral controller) is a special case of the PID controller in which the derivative (D) of the error is not used.

The controller output is given by

$K_{P}\Delta +K_{I}\int \Delta \,dt$

where $\Delta$ is the error or deviation of actual measured value (***PV***) from the setpoint (***SP***).

$\Delta =SP-PV.$

A PI controller can be modelled easily in software such as Simulink or Xcos using a "flow chart" box involving Laplace operators:

$C={\frac {G(1+\tau s)}{\tau s}}$

where

$G=K_{P}$

= proportional gain

${\frac {G}{\tau }}=K_{I}$

= integral gain

Setting a value for G is often a trade off between decreasing overshoot and increasing settling time.

The lack of derivative action may make the system more steady in the steady state in the case of noisy data. This is because derivative action is more sensitive to higher-frequency terms in the inputs.

Without derivative action, a PI-controlled system is less responsive to real (non-noise) and relatively fast alterations in state, and so the system will be slower to reach setpoint and slower to respond to perturbations than a well-tuned PID system may be.

### Deadband

Many PID loops control a mechanical device (for example, a valve). Mechanical maintenance can be a major cost and wear leads to control degradation in the form of either stiction or backlash in the mechanical response to an input signal. The rate of mechanical wear is mainly a function of how often a device is activated to make a change. Where wear is a significant concern, the PID loop may have an output deadband to reduce the frequency of activation of the output (valve). This is accomplished by modifying the controller to hold its output steady if the change would be small (within the defined deadband range). The calculated output must leave the deadband before the actual output will change.

### Setpoint step change

The proportional and derivative terms can produce excessive movement in the output when a system is subjected to an instantaneous step increase in the error, such as a large setpoint change. In the case of the derivative term, this is due to taking the derivative of the error, which is very large in the case of an instantaneous step change. As a result, some PID algorithms incorporate some of the following modifications:

**Setpoint ramping**

In this modification, the setpoint is gradually moved from its old value to a newly specified value using a linear or first-order differential ramp function. This avoids the

discontinuity

present in a simple step change.

**Derivative of the process variable**

In this case, the PID controller measures the derivative of the measured PV, rather than the derivative of the error. This quantity is always continuous (i.e., never has a step change as a result of changed setpoint). This modification is a simple case of setpoint weighting.

**Setpoint weighting**

Setpoint weighting adds adjustable factors (usually between 0 and 1) to the setpoint in the error in the proportional and derivative element of the controller. The error in the integral term must be the true control error to avoid steady-state control errors. These two extra parameters do not affect the response to load disturbances and measurement noise and can be tuned to improve the controller's setpoint response.

### Feed-forward

The control system performance can be improved by combining the feedback (or closed-loop) control of a PID controller with feed-forward (or open-loop) control. Knowledge about the system (such as the desired acceleration and inertia) can be fed forward and combined with the PID output to improve the overall system performance. The feed-forward value alone can often provide the major portion of the controller output. The PID controller primarily has to compensate for whatever difference or *error* remains between the setpoint (SP) and the system response to the open-loop control. Since the feed-forward output is not affected by the process feedback, it can never cause the control system to oscillate, thus improving the system response without affecting stability. Feed forward can be based on the setpoint and on extra measured disturbances. Setpoint weighting is a simple form of feed forward.

For example, in most motion control systems, in order to accelerate a mechanical load under control, more force is required from the actuator. If a velocity loop PID controller is being used to control the speed of the load and command the force being applied by the actuator, then it is beneficial to take the desired instantaneous acceleration, scale that value appropriately and add it to the output of the PID velocity loop controller. This means that whenever the load is being accelerated or decelerated, a proportional amount of force is commanded from the actuator regardless of the feedback value. The PID loop in this situation uses the feedback information to change the combined output to reduce the remaining difference between the process setpoint and the feedback value. Working together, the combined open-loop feed-forward controller and closed-loop PID controller can provide a more responsive control system.

### Bumpless operation

PID controllers are often implemented with a "bumpless" initialization feature that recalculates the integral accumulator term to maintain a consistent process output through parameter changes. A partial implementation is to store the integral gain times the error rather than storing the error and postmultiplying by the integral gain, which prevents discontinuous output when the I gain is changed, but not the P or D gains.

### Other improvements

In addition to feed-forward, PID controllers are often enhanced through methods such as PID gain scheduling (changing parameters in different operating conditions), fuzzy logic, or computational verb logic. Further practical application issues can arise from instrumentation connected to the controller. A high enough sampling rate, measurement precision, and measurement accuracy are required to achieve adequate control performance. Another new method for improvement of PID controller is to increase the degree of freedom by using fractional order. The order of the integrator and differentiator add increased flexibility to the controller.


## Cascade control

One distinctive advantage of PID controllers is that two PID controllers can be used together to yield better dynamic performance. This is called cascaded PID control. Two controllers are in cascade when they are arranged so that one regulates the set point of the other. A PID controller acts as outer loop controller, which controls the primary physical parameter, such as fluid level or velocity. The other controller acts as inner loop controller, which reads the output of outer loop controller as setpoint, usually controlling a more rapid changing parameter, flowrate or acceleration. It can be mathematically proven that the working frequency of the controller is increased and the time constant of the object is reduced by using cascaded PID controllers..

For example, a temperature-controlled circulating bath has two PID controllers in cascade, each with its own thermocouple temperature sensor. The outer controller controls the temperature of the water using a thermocouple located far from the heater, where it accurately reads the temperature of the bulk of the water. The error term of this PID controller is the difference between the desired bath temperature and measured temperature. Instead of controlling the heater directly, the outer PID controller sets a heater temperature goal for the inner PID controller. The inner PID controller controls the temperature of the heater using a thermocouple attached to the heater. The inner controller's error term is the difference between this heater temperature setpoint and the measured temperature of the heater. Its output controls the actual heater to stay near this setpoint.

The proportional, integral, and differential terms of the two controllers will be very different. The outer PID controller has a long time constant – all the water in the tank needs to heat up or cool down. The inner loop responds much more quickly. Each controller can be tuned to match the physics of the system *it* controls – heat transfer and thermal mass of the whole tank or of just the heater – giving better total response.


## Alternative nomenclature and forms

### Standard versus parallel (ideal) form

The form of the PID controller most often encountered in industry, and the one most relevant to tuning algorithms, is the *standard form*. In this form the $K_{p}$ gain is applied to the $I_{\mathrm {out} }$ , and $D_{\mathrm {out} }$ terms, yielding:

$u(t)=K_{p}\left(e(t)+{\frac {1}{T_{i}}}\int _{0}^{t}e(\tau )\,d\tau +T_{d}{\frac {d}{dt}}e(t)\right)$

where

$T_{i}$

is the

integral time

$T_{d}$

is the

derivative time

In this standard form, the parameters have a clear physical meaning. In particular, the inner summation produces a new single error value, which is compensated for future and past errors. The proportional error term is the current error. The derivative components term attempts to predict the error value at $T_{d}$ seconds (or samples) in the future, assuming that the loop control remains unchanged. The integral component adjusts the error value to compensate for the sum of all past errors, with the intention of completely eliminating them in $T_{i}$ seconds (or samples). The resulting compensated single error value is then scaled by the single gain $K_{p}$ to compute the control variable.

In the parallel form, shown in the controller theory section

$u(t)=K_{p}e(t)+K_{i}\int _{0}^{t}e(\tau )\,d\tau +K_{d}{\frac {d}{dt}}e(t)$

the gain parameters are related to the parameters of the standard form through $K_{i}=K_{p}/T_{i}$ and $K_{d}=K_{p}T_{d}$ . This parallel form, where the parameters are treated as simple gains, is the most general and flexible form. However, it is also the form where the parameters have the weakest relationship to physical behaviors and is generally reserved for theoretical treatment of the PID controller. The standard form, despite being slightly more complex mathematically, is more common in industry.

### Reciprocal gain, a.k.a. proportional band

In many cases, the manipulated variable output by the PID controller is a dimensionless fraction between 0 and 100% of some maximum possible value, and the translation into real units (such as pumping rate or watts of heater power) is outside the PID controller. The process variable, however, is in dimensioned units such as temperature. It is common in this case to express the gain $K_{p}$ not as "output per degree", but rather in the reciprocal form of a *proportional band* $100/K_{p}$ , which is "degrees per full output": the range over which the output changes from 0 to 1 (0% to 100%). Beyond this range, the output is saturated, full-off or full-on. The narrower this band, the higher the proportional gain.

### Basing derivative action on PV

In most commercial control systems, derivative action is based on process variable rather than error. That is, a change in the setpoint does not affect the derivative action. This is because the digitized version of the algorithm produces a large unwanted spike when the setpoint is changed. If the setpoint is constant, then changes in the PV will be the same as changes in error. Therefore, this modification makes no difference to the way the controller responds to process disturbances.

### Basing proportional action on PV

Most commercial control systems offer the *option* of also basing the proportional action solely on the process variable. This means that only the integral action responds to changes in the setpoint. The modification to the algorithm does not affect the way the controller responds to process disturbances. Basing proportional action on PV eliminates the instant and possibly very large change in output caused by a sudden change to the setpoint. Depending on the process and tuning, this may be beneficial to the response to a setpoint step.

$\mathrm {MV(t)} =K_{p}\left(\,{-PV(t)}+{\frac {1}{T_{i}}}\int _{0}^{t}{e(\tau )}\,{d\tau }-T_{d}{\frac {d}{dt}}PV(t)\right)$

King describes an effective chart-based method.

### Laplace form

Sometimes it is useful to write the PID regulator in Laplace transform form:

$G(s)=K_{p}+{\frac {K_{i}}{s}}+K_{d}{s}={\frac {K_{d}{s^{2}}+K_{p}{s}+K_{i}}{s}}$

Having the PID controller written in Laplace form and having the transfer function of the controlled system makes it easy to determine the closed-loop transfer function of the system.

### Series/interacting form

Another representation of the PID controller is the series, or *interacting* form

$G(s)=K_{c}\left({\frac {1}{\tau _{i}{s}}}+1\right)(\tau _{d}{s}+1)$

where the parameters are related to the parameters of the standard form through

$K_{p}=K_{c}\cdot \alpha$

,

$T_{i}=\tau _{i}\cdot \alpha$

, and

$T_{d}={\frac {\tau _{d}}{\alpha }}$

with

$\alpha =1+{\frac {\tau _{d}}{\tau _{i}}}$

.

This form essentially consists of a PD and PI controller in series. As the integral is required to calculate the controller's bias, this form provides the ability to track an external bias value, which is required to be used for proper implementation of multi-controller advanced control schemes.

### Discrete implementation

The analysis for designing a digital implementation of a PID controller in a microcontroller (MCU) or FPGA device requires the standard form of the PID controller to be *discretized*. Approximations for first-order derivatives are made by backward finite differences. $u(t)$ and $e(t)$ are discretized with a sampling period $\Delta t$ , k is the sample index.

Differentiating both sides of PID equation using Newton's notation gives:

${\dot {u}}(t)=K_{p}{\dot {e}}(t)+K_{i}e(t)+K_{d}{\ddot {e}}(t)$

Derivative terms are approximated as,

${\dot {f}}(t_{k})={\dfrac {df(t_{k})}{dt}}={\dfrac {f(t_{k})-f(t_{k-1})}{\Delta t}}$

So,

${\frac {u(t_{k})-u(t_{k-1})}{\Delta t}}=K_{p}{\frac {e(t_{k})-e(t_{k-1})}{\Delta t}}+K_{i}e(t_{k})+K_{d}{\frac {{\dot {e}}(t_{k})-{\dot {e}}(t_{k-1})}{\Delta t}}$

Applying backward difference again gives,

${\frac {u(t_{k})-u(t_{k-1})}{\Delta t}}=K_{p}{\frac {e(t_{k})-e(t_{k-1})}{\Delta t}}+K_{i}e(t_{k})+K_{d}{\frac {{\frac {e(t_{k})-e(t_{k-1})}{\Delta t}}-{\frac {e(t_{k-1})-e(t_{k-2})}{\Delta t}}}{\Delta t}}$

By simplifying and regrouping terms of the above equation, an algorithm for an implementation of the discretized PID controller in an MCU is finally obtained:

$u(t_{k})=u(t_{k-1})+\left(K_{p}+K_{i}\Delta t+{\dfrac {K_{d}}{\Delta t}}\right)e(t_{k})+\left(-K_{p}-{\dfrac {2K_{d}}{\Delta t}}\right)e(t_{k-1})+{\dfrac {K_{d}}{\Delta t}}e(t_{k-2})$

or:

$u(t_{k})=u(t_{k-1})+K_{p}\left[\left(1+{\dfrac {\Delta t}{T_{i}}}+{\dfrac {T_{d}}{\Delta t}}\right)e(t_{k})+\left(-1-{\dfrac {2T_{d}}{\Delta t}}\right)e(t_{k-1})+{\dfrac {T_{d}}{\Delta t}}e(t_{k-2})\right]$

s.t. $T_{i}=K_{p}/K_{i},T_{d}=K_{d}/K_{p}$

Note: This method solves in fact $u(t)=K_{\text{p}}e(t)+K_{\text{i}}\int _{0}^{t}e(\tau )\,\mathrm {d} \tau +K_{\text{d}}{\frac {\mathrm {d} e(t)}{\mathrm {d} t}}+u_{0}$ where $u_{0}$ is a constant independent of t. This constant is useful when you want to have a start and stop control on the regulation loop. For instance, setting Kp,Ki and Kd to 0 will keep u(t) constant. Likewise, when you want to start a regulation on a system where the error is already close to 0 with u(t) non null, it prevents from sending the output to 0.


## Pseudocode

Here is a very simple and explicit group of pseudocode that can be easily understood by the layman:

- `Kp` – proportional gain
- `Ki` – integral gain
- `Kd` – derivative gain
- `dt` – loop interval time (assumes reasonable scale)

```
previous_error := 0
integral := 0
loop:
   error := setpoint − measured_value
   proportional := error;
   integral := integral + error × dt
   derivative := (error - previous_error) / dt
   output := Kp × proportional + Ki × integral + Kd × derivative
   previous_error := error
   wait(dt)
   goto loop
```

Below a pseudocode illustrates how to implement a PID considering the PID as an IIR filter:

The Z-transform of a PID can be written as ( $\Delta _{t}$ is the sampling time):

$C(z)=K_{p}+K_{i}\Delta _{t}{\frac {z}{z-1}}+{\frac {K_{d}}{\Delta _{t}}}{\frac {z-1}{z}}$

and expressed in a IIR form (in agreement with the discrete implementation shown above):

$C(z)={\frac {\left(K_{p}+K_{i}\Delta _{t}+{\dfrac {K_{d}}{\Delta _{t}}}\right)+\left(-K_{p}-{\dfrac {2K_{d}}{\Delta _{t}}}\right)z^{-1}+{\dfrac {K_{d}}{\Delta _{t}}}z^{-2}}{1-z^{-1}}}$

We can then deduce the recursive iteration often found in FPGA implementation

$u[n]=u[n-1]+\left(K_{p}+K_{i}\Delta _{t}+{\dfrac {K_{d}}{\Delta _{t}}}\right)\epsilon [n]+\left(-K_{p}-{\dfrac {2K_{d}}{\Delta _{t}}}\right)\epsilon [n-1]+{\dfrac {K_{d}}{\Delta _{t}}}\epsilon [n-2]$

```
A0 := Kp + Ki*dt + Kd/dt
A1 := -Kp - 2*Kd/dt
A2 := Kd/dt
error[2] := 0  // e(t-2)
error[1] := 0  // e(t-1)
error[0] := 0  // e(t)
output   := u0 // Usually the current value of the actuator

loop:
    error[2] := error[1]
    error[1] := error[0]
    error[0] := setpoint − measured_value
    output   := output + A0 * error[0] + A1 * error[1] + A2 * error[2]
    wait(dt)
    goto loop
```

Here, `Kp` is a dimensionless number, `Ki` is expressed in s−1 and `Kd` is expressed in s. When doing a regulation where the actuator and the measured value are not in the same unit (e.g., temperature regulation using a motor controlling a valve), $K_{p}$ , $K_{i}$ and $K_{d}$ may be corrected by a unit conversion factor. It may also be interesting to use `Ki` in its reciprocal form (integration time). The above implementation allows to perform an I-only controller which may be useful in some cases.

In the real world, this is D-to-A converted and passed into the process under control as the manipulated variable (MV). The current error is stored elsewhere for re-use in the next differentiation, the program then waits until `dt` seconds have passed since start, and the loop begins again, reading in new values for the PV and the setpoint and calculating a new value for the error.

Note that for real code, the use of `wait(dt)` might be inappropriate because it does not account for time taken by the algorithm itself during the loop, or more importantly, any pre-emption delaying the algorithm.

A common issue when using $K_{d}$ is the response to the derivative of a rising or falling edge of the setpoint, as shown below:(PID without derivative filtering)

A typical workaround is to filter the derivative action using a low pass filter of time constant $\tau _{d}/N$ where $3<=N<=10$ :(PID with derivative filtering)

A variant of the above algorithm using an infinite impulse response (IIR) filter for the derivative:

```
A0 := Kp + Ki*dt
A1 := -Kp
error[2] := 0 // e(t-2)
error[1] := 0 // e(t-1)
error[0] := 0 // e(t)
output := u0  // Usually the current value of the actuator
A0d := Kd/dt
A1d := - 2.0*Kd/dt
A2d := Kd/dt
N := 5
tau := Kd / (Kp*N) // IIR filter time constant
alpha := dt / (2*tau)
d0 := 0
d1 := 0
fd0 := 0
fd1 := 0
loop:
    error[2] := error[1]
    error[1] := error[0]
    error[0] := setpoint − measured_value
    // PI
    output := output + A0 * error[0] + A1 * error[1]
    // Filtered D
    d1 := d0
    d0 := A0d * error[0] + A1d * error[1] + A2d * error[2]
    fd1 := fd0
    fd0 := ((alpha) / (alpha + 1)) * (d0 + d1) - ((alpha - 1) / (alpha + 1)) * fd1
    output := output + fd0      
    wait(dt)
    goto loop
```
