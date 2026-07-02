---
title: "Setpoint (control system)"
source: https://en.wikipedia.org/wiki/Setpoint_(control_system)
domain: control-systems
license: CC-BY-SA-4.0
tags: control theory, pid controller, feedback loop, control system, kalman filter, servo
fetched: 2026-07-02
---

# Setpoint (control system)

In cybernetics and control theory, a **setpoint** (**SP**; also **set point**) is the desired or target value for an essential variable, or process value (PV) of a control system, which may differ from the actual measured value of the variable. Departure of such a variable from its setpoint is one basis for error-controlled regulation using negative feedback for automatic control. A setpoint can be any physical quantity or parameter that a control system seeks to regulate, such as temperature, pressure, flow rate, position, speed, or any other measurable attribute.

In the context of PID controller, the setpoint represents the reference or goal for the controlled process variable. It serves as the benchmark against which the actual process variable (PV) is continuously compared. The PID controller calculates an error signal by taking the difference between the setpoint and the current value of the process variable. Mathematically, this error is expressed as:

$e(t)=SP-PV(t),$

where $e(t)$ is the error at a given time t , $SP$ is the setpoint, $PV(t)$ is the process variable at time t .

The PID controller uses this error signal to determine how to adjust the control output to bring the process variable as close as possible to the setpoint while maintaining stability and minimizing overshoot.

## Examples

**Cruise control**

The $SP-PV$ error can be used to return a system to its norm. An everyday example is the cruise control on a road vehicle; where external influences such as gradients cause speed changes (PV), and the driver also alters the desired set speed (SP). The automatic control algorithm restores the actual speed to the desired speed in the optimum way, without delay or overshoot, by altering the power output of the vehicle's engine. In this way the $SP-PV$ error is used to control the PV so that it equals the SP. A widespread of $SP-PV$ error is classically used in the PID controller.

**Industrial applications**

Special consideration must be given for engineering applications. In industrial systems, physical or process restraints may limit the determined set point. For example, a reactor which operates more efficiently at higher temperatures may be rated to withstand 500°C. However, for safety reasons, the set point for the reactor temperature control loop would be well below this limit, even if this means the reactor is running less efficiently.
