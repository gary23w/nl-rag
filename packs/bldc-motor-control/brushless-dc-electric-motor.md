---
title: "Brushless DC electric motor"
source: https://en.wikipedia.org/wiki/Brushless_DC_electric_motor
domain: bldc-motor-control
license: CC-BY-SA-4.0
tags: brushless DC motor, back electromotive force, Hall effect sensor, electric commutator
fetched: 2026-07-02
---

# Brushless DC electric motor

A **brushless DC electric motor** (**BLDC**), also known as an **electronically commutated motor**, is a synchronous motor using a direct current (DC) electric power supply. It uses an electronic controller to switch DC currents to the motor windings, producing magnetic fields that effectively rotate in space and which the permanent magnet rotor follows. The controller adjusts the phase and amplitude of the current pulses that control the speed and torque of the motor. It is an improvement on the mechanical commutator (brushes) used in many conventional electric motors.

The construction of a brushless motor system is typically similar to a permanent magnet synchronous motor (PMSM), but can also be a switched reluctance motor, or an induction (asynchronous) motor. They may also use neodymium magnets and be outrunners (the stator is surrounded by the rotor), inrunners (the rotor is surrounded by the stator), or axial (the rotor and stator are flat and parallel).

The advantages of a brushless motor over brushed motors are high power-to-weight ratio, high speed, nearly instantaneous control of speed (rpm) and torque, high efficiency, and low maintenance. Brushless motors find applications in such places as computer peripherals (disk drives, printers), hand-held power tools, and vehicles ranging from model aircraft to automobiles. In modern washing machines, brushless DC motors have allowed replacement of rubber belts and gearboxes by a direct-drive design.

## Background

Brushed DC motors were invented in the 20th century and are still common. Brushless DC motors were made possible by the development of solid-state electronics in the 1960s.

An electric motor develops torque by keeping the magnetic fields of the rotor (the rotating part of the machine) and the stator (the fixed part of the machine) misaligned. One or both sets of magnets are electromagnets, made of a coil of wire wound around an iron core. DC running through the wire winding creates the magnetic field, providing the power that runs the motor. The misalignment generates a torque that tries to realign the fields. As the rotor moves and the fields come into alignment, it is necessary to move either the rotor's or stator's field to maintain the misalignment and continue to generate torque and movement. The device that moves the fields based on the position of the rotor is called a commutator.

### Brush commutator

In brushed motors, this is done with a rotary switch on the motor's shaft called a commutator. It consists of a rotating cylinder or disc divided into multiple metal contact segments on the rotor. The segments are connected to conductor windings on the rotor. Two or more stationary contacts called *brushes*, made of a soft conductor such as graphite, press against the commutator, making sliding electrical contact with successive segments as the rotor turns. The brushes selectively provide electric current to the windings. As the rotor rotates, the commutator selects different windings and the directional current is applied to a given winding such that the rotor's magnetic field remains misaligned with the stator and creates a torque in one direction.

The brush commutator has disadvantages that have led to a decline in the use of brushed motors. These disadvantages are:

- The friction of the brushes sliding along the rotating commutator segments causes power losses that can be significant in a low-power motor.
- The soft brush material wears down due to friction, creating dust, and eventually, the brushes must be replaced. This makes commutated motors unsuitable for low-particulate or sealed applications like hard disk motors and for applications that require maintenance-free operation.
- The electrical resistance of the sliding brush contact causes a voltage drop in the motor circuit called *brush drop*, which consumes energy.
- The repeated abrupt switching of the current through the inductance of the windings causes sparks at the commutator contacts, which is a fire hazard in explosive atmospheres and a source of electronic noise, which can cause electromagnetic interference in nearby microelectronic circuits.

During the last hundred years, high-power DC brushed motors, once the mainstay of industry, were replaced by alternating current (AC) synchronous motors. Today, brushed motors are used only in low-power applications or where only DC is available, but the above drawbacks limit their use even in these applications.

### Brushless solution

In brushless DC motors, an electronic controller replaces the brush commutator contacts. An electronic sensor detects the angle of the rotor and controls semiconductor switches such as transistors that switch current through the windings, either reversing the direction of the current or, in some motors turning it off, at the correct angle so the electromagnets create torque in one direction. The elimination of the sliding contact allows brushless motors to have less friction and longer life; their working life is limited only by the lifetime of their bearings.

Brushed DC motors develop a maximum torque when stationary, linearly decreasing as velocity increases. Some limitations of brushed motors can be overcome by brushless motors; they include higher efficiency and lower susceptibility to mechanical wear. These benefits come at the cost of potentially less rugged, more complex, and more expensive control electronics.

A typical brushless motor has permanent magnets that rotate around a fixed armature, eliminating problems associated with connecting current to the moving armature. An electronic controller replaces the commutator assembly of the brushed DC motor, which continually switches the phase to the windings to keep the motor turning. The controller performs similar timed power distribution by using a solid-state circuit rather than the commutator system.

Brushless motors offer several advantages over brushed DC motors, including high torque to weight ratio, increased efficiency producing more torque per watt, increased reliability, reduced noise, longer lifetime by eliminating brush and commutator erosion, elimination of ionizing sparks from the commutator, and an overall reduction of electromagnetic interference (EMI). With no windings on the rotor, they are not subjected to centrifugal forces, and because the windings are supported by the housing, they can be cooled by conduction, requiring no airflow inside the motor for cooling. This, in turn, means that the motor's internals can be entirely enclosed and protected from dirt or other foreign matter.

Brushless motor commutation can be implemented in software using a microcontroller, or may alternatively be implemented using analog or digital circuits. Commutation with electronics instead of brushes allows for greater flexibility and capabilities not available with brushed DC motors, including speed limiting, microstepping operation for slow and fine motion control, and holding torque when stationary. Controller software can be customized to the specific motor being used in the application, resulting in greater commutation efficiency.

The maximum power that can be applied to a brushless motor is limited almost exclusively by heat; too much heat weakens the magnets and damages the windings' insulation.

When converting electricity into mechanical power, brushless motors are more efficient than brushed motors primarily due to the absence of brushes, which reduces mechanical energy loss due to friction. The enhanced efficiency is greatest in the no-load and low-load regions of the motor's performance curve.

Environments and requirements in which manufacturers use brushless-type DC motors include maintenance-free operation, high speeds, and operation where sparking is hazardous (i.e., explosive environments) or could affect electronically sensitive equipment.

The construction of a brushless motor resembles a stepper motor, but the motors have important differences in implementation and operation. While stepper motors are frequently stopped with the rotor in a defined angular position, a brushless motor is usually intended to produce continuous rotation. Both motor types may have a rotor position sensor for internal feedback. Both a stepper motor and a well-designed brushless motor can hold finite torque at zero RPM.

## Controller implementations

Because the controller implements the traditional brushes' functionality, it needs to know the rotor's orientation relative to the stator coils. This is automatic in a brushed motor due to the fixed geometry of the rotor shaft and brushes. Some designs use Hall effect sensors or a rotary encoder to directly measure the rotor's position. Others measure the back-EMF in the undriven coils to infer the rotor position, eliminating the need for separate Hall effect sensors. These are therefore often called *sensorless* controllers.

Controllers that sense rotor position based on back-EMF have extra challenges in initiating motion because no back-EMF is produced when the rotor is stationary. This is usually accomplished by beginning rotation from an arbitrary phase, and then skipping to the correct phase if it is found to be wrong. This can cause the motor to run backwards briefly, adding even more complexity to the startup sequence. Other sensorless controllers are capable of measuring winding saturation caused by the position of the magnets to infer the rotor position.

A typical controller contains three polarity-reversible outputs controlled by a logic circuit. Simple controllers employ comparators working from the orientation sensors to determine when the output phase should be advanced. More advanced controllers employ a microcontroller to manage acceleration, control motor speed and fine-tune efficiency.

Two key performance parameters of brushless DC motors are the motor constants $K_{T}$ (torque constant) and $K_{e}$ (back-EMF constant, also known as speed constant $K_{V}={1 \over K_{e}}$ ).

## Variations in construction

Brushless motors can be constructed in several different physical configurations. In the conventional inrunner configuration, the permanent magnets are part of the rotor. Three stator windings surround the rotor. In the external-rotor outrunner configuration, the radial relationship between the coils and magnets is reversed; the stator coils form the center (core) of the motor, while the permanent magnets spin within an overhanging rotor that surrounds the core. Outrunners typically have more poles and have a higher torque at low RPM. In the flat axial flux type, used where there are space or shape constraints, stator and rotor plates are mounted face to face. In all brushless motors, the coils are stationary.

This is for 3 phase AC motors not DC brushless motors: There are two common electrical winding configurations: the delta configuration connects three windings to each other in a triangle-like circuit, and power is applied at each of the connections. The wye (*Y*-shaped) configuration, sometimes called a star winding, connects all of the windings to a central point, and power is applied to the remaining end of each winding. A motor with windings in delta configuration gives low torque at low speed but can give a higher top speed. Wye configuration gives high torque at low speed but not as high top speed. The wye winding is normally more efficient. Delta-connected windings can allow high-frequency parasitic electrical currents to circulate entirely within the motor. A Wye-connected winding does not contain a closed loop in which parasitic currents can flow, preventing such losses. Aside from the higher impedance of the wye configuration, from a controller standpoint, the two winding configurations can be treated exactly the same.

## Applications

Brushless motors fulfill many functions originally performed by brushed DC motors, but cost and control complexity prevent brushless motors from replacing brushed motors completely in the lowest-cost areas. Nevertheless, brushless motors have come to dominate many applications, particularly devices such as computer hard drives and CD/DVD players. Small cooling fans in electronic equipment are powered exclusively by brushless motors. They can be found in cordless power tools, where the increased efficiency of the motor leads to longer periods of use before the battery needs to be charged. Low speed, low power brushless motors are used in direct-drive turntables for gramophone records. Brushless motors can also be found in marine applications, such as underwater thrusters. Drones also utilize brushless motors to elevate their performance.

### Transport

Brushless motors are found in electric vehicles, hybrid vehicles, personal transporters, and electric aircraft. Most electric bicycles use brushless motors that are sometimes built into the wheel hub itself, with the stator fixed solidly to the axle and the magnets attached to and rotating with the wheel. The same principle is applied in self-balancing scooter wheels. Most electrically powered radio-controlled models use brushless motors because of their high efficiency.

### Cordless tools

Brushless motors are found in many modern cordless tools, including some string trimmers, leaf blowers, saws (circular and reciprocating), and drills/drivers. The weight and efficiency advantages of brushless over brushed motors are more important to handheld, battery-powered tools than to large, stationary tools plugged into an AC outlet.

### Heating and ventilation

There is a trend in the heating, ventilation, and air conditioning (HVAC) and refrigeration industries to use brushless motors instead of various types of AC motors. The most significant reason to switch to a brushless motor is a reduction in power required to operate them versus a typical AC motor. In addition to the brushless motor's higher efficiency, HVAC systems, especially those featuring variable-speed or load modulation, use brushless motors to give the built-in microprocessor continuous control over cooling and airflow.

### Industrial engineering

The application of brushless DC motors within industrial engineering primarily focuses on manufacturing engineering or industrial automation design. Brushless motors are ideally suited for manufacturing applications because of their high power density, good speed-torque characteristics, high efficiency, wide speed ranges and low maintenance. The most common uses of brushless DC motors in industrial engineering are motion control, linear actuators, servomotors, actuators for industrial robots, extruder drive motors and feed drives for CNC machine tools.

Brushless motors are commonly used as pump, fan and spindle drives in adjustable or variable speed applications as they are capable of developing high torque with good speed response. In addition, they can be easily automated for remote control. Due to their construction, they have good thermal characteristics and high energy efficiency. To obtain a variable speed response, brushless motors operate in an electromechanical system that includes an electronic motor controller and a rotor position feedback sensor. Brushless DC motors are widely used as servomotors for machine tool servo drives. Servomotors are used for mechanical displacement, positioning or precision motion control. DC stepper motors can also be used as servomotors; however, since they are operated with open loop control, they typically exhibit torque pulsations.

Brushless motors are used in industrial positioning and actuation applications. For assembly robots, Brushless technology may be used to build linear motors. The advantage of linear motors is that they can produce linear motion without the need of a transmission system, such as ballscrews, leadscrew, rack-and-pinion, cam, gears or belts, that would be necessary for rotary motors. Transmission systems are known to introduce less responsiveness and reduced accuracy. Direct drive, brushless DC linear motors consist of a slotted stator with magnetic teeth and a moving actuator, which has permanent magnets and coil windings. To obtain linear motion, a motor controller excites the coil windings in the actuator causing an interaction of the magnetic fields resulting in linear motion. Tubular linear motors are another form of linear motor design operated in a similar way.

### Aeromodelling

Brushless motors have become a popular motor choice for model aircraft, including helicopters and drones. Their favorable power-to-weight ratios and wide range of available sizes have revolutionized the market for electric-powered model flight, displacing virtually all brushed electric motors, except for low powered inexpensive often toy grade aircraft. They have also encouraged growth of simple, lightweight electric model aircraft, rather than the previous internal combustion engines powering larger and heavier models. The increased power-to-weight ratio of modern batteries and brushless motors allows models to ascend vertically rather than climb gradually. The low noise and lack of mass compared to small glow fuel internal combustion engines is another reason for their popularity.

Legal restrictions for the use of combustion engine driven model aircraft in some countries, most often due to potential for noise pollution—even with purpose-designed mufflers for almost all model engines being available over the most recent decades—have also supported the shift to high-power electric systems.

### Radio-controlled cars

Their popularity has also risen in the radio-controlled car area. Brushless motors have been legal in North American RC car racing in accordance with Radio Operated Auto Racing (ROAR) since 2006. These motors provide a great amount of power to RC racers and, if paired with appropriate gearing and high-discharge lithium polymer (Li-Po) or lithium iron phosphate (LiFePO4) batteries, these cars can achieve speeds over 160 kilometres per hour (99 mph).

Brushless motors are capable of producing more torque and have a faster peak rotational speed compared to nitro- or gasoline-powered engines. Nitro engines peak at around 46,800 r/min and 2.2 kilowatts (3.0 hp), while a smaller brushless motor can reach 50,000 r/min and 3.7 kilowatts (5.0 hp). Larger brushless RC motors can reach upwards of 10 kilowatts (13 hp) and 28,000 r/min to power one-fifth-scale models.

### Combat robotics

Brushless motors are widely used as an alternative to brushed motors in the sport of combat robotics. They are used in every weight class from 75 grams all the way up to 250 pounds. When used for locomotion, brushless motors are often paired with a planetary gearbox in order to decrease the output speed to make the robot more controllable. Other methods, such as friction drive, achieve the same result using slightly different means. Brushless motors are also often used to power kinetic weapons (such as a spinning blade). In the lower weight classes, weapons are often mounted directly to the motor, while in heavier robots, timing belts, v-belts, and chains are used to transmit power from the motor to the spinning mass.
