---
title: "Synchronous motor"
source: https://en.wikipedia.org/wiki/Synchronous_motor
domain: ac-induction-motors
license: CC-BY-SA-4.0
tags: induction motor, squirrel-cage rotor, rotating magnetic field, wound rotor motor
fetched: 2026-07-02
---

# Synchronous motor

A **synchronous electric motor** is an AC electric motor in which, at steady state, the rotation of the shaft is synchronized with the frequency of the supply current. Synchronous motors use permanent magnets or electromagnets for rotors, and electromagnets for stators. The stator creates a magnetic field that rotates in time with the oscillations of the current. The rotor turns in step with the stator field at the same rate and as a result, provides a second synchronized rotating magnet field.

Synchronous and induction motors are the most widely used AC motors. Synchronous motors rotate at a rate locked to the line frequency since they do not rely on induction to produce the rotor's magnetic field. Induction motors require *slip*: the rotor must rotate at a frequency slightly slower than the AC alternations in order to induce current in the rotor.

Small synchronous motors are used in timing applications such as in synchronous clocks, timers in appliances, tape recorders and precision servomechanisms in which the motor must operate at a precise speed; accuracy depends on the power line frequency, which is carefully controlled in large interconnected grid systems.

Synchronous motors are available in self-excited, fractional to industrial sizes. In the fractional power range, most synchronous motors are used to provide precise constant speed. These machines are commonly used in analog electric clocks, timers and related devices. Doubly fed synchronous motors use independently-excited multiphase AC electromagnets for both rotor and stator.

In typical industrial sizes, the synchronous motor provides an efficient means of converting AC energy to work (electrical efficiency above 95% is normal for larger sizes) and it can operate at leading or unity power factor and thereby provide power-factor correction.

Synchronous motors fall under the category of *synchronous machines* that also includes synchronous generators. Generator action occurs if the field poles are "driven ahead of the resultant air-gap flux by the forward motion of the prime mover". Motor action occurs if the field poles are "dragged behind the resultant air-gap flux by the retarding torque of a shaft load".

## Types

The two major types of synchronous motors are distinguished by how the rotor is magnetized: non-excited and direct-current excited.

### Non-excited

In non-excited motors, the external stator field magnetizes the rotor, inducing the magnetic poles needed to turn the rotor. The rotor rotates in step with the stator's rotating magnetic field, so it has an almost-constant magnetic field through it. The rotor is made of a high-retentivity steel such as cobalt steel. These are manufactured in permanent magnet, reluctance and hysteresis designs:

#### Permanent-magnet

A permanent-magnet synchronous motor (PMSM) uses permanent magnets embedded in the rotor to create a constant magnetic field. The stator carries windings connected to an AC electricity supply to produce a rotating magnetic field (as in an asynchronous motor). At synchronous speed the rotor poles lock to the rotating magnetic field. PMSMs are similar to brushless DC motors. Neodymium magnets are the most common, although rapid fluctuation of neodymium magnet prices triggered research in ferrite magnets. Due to inherent characteristics of ferrite magnets, the magnetic circuit of these machines needs to be able to concentrate the magnetic flux, typically leading to the use of spoke type rotors. Machines that use ferrite magnets have lower power density and torque density when compared with neodymium machines.

PMSMs have been used as gearless elevator motors since 2000.

Most PMSMs require a variable-frequency drive to start them. However, some incorporate a squirrel cage in the rotor for starting—these are known as line-start or self-starting. These are typically used as higher-efficiency replacements for induction motors (owing to the lack of slip), but must ensure that synchronous speed is reached and that the system can withstand torque ripple during starting.

PMSMs are typically controlled using direct torque control and field oriented control.

#### Reluctance

Reluctance motors have a solid steel cast rotor with projecting (salient) toothed poles. Typically there are fewer rotor than stator poles to minimize torque ripple and to prevent the poles from all aligning simultaneously—a position that cannot generate torque. The size of the air gap in the magnetic circuit and thus the reluctance is minimum when the poles align with the stator's (rotating) magnetic field, and increases with the angle between them. This creates torque that pulls the rotor into alignment with the nearest pole of the stator field. At synchronous speed the rotor is thus "locked" to the rotating stator field. This cannot start the motor, so the rotor poles usually have squirrel-cage windings embedded in them, to provide torque below synchronous speed. The machine thus starts as an induction motor until it approaches synchronous speed, when the rotor "pulls in" and locks to the stator field.

Reluctance motor designs have ratings that range from fractional horsepower (a few watts) to about 22 kW. Small reluctance motors have low torque, and are generally used for instrumentation applications. Moderate torque, multi-horsepower motors use squirrel cage construction with toothed rotors. When used with an adjustable frequency power supply, all motors in a drive system can operate at exactly the same speed. The power supply frequency determines motor operating speed.

#### Hysteresis

Hysteresis motors have a solid, smooth, cylindrical rotor, cast of a high coercivity magnetically "hard" cobalt steel. This material has a wide hysteresis loop (high coercivity), meaning once it is magnetized in a given direction, it requires a high magnetic field to reverse the magnetization. The rotating stator field causes each small volume of the rotor to experience a reversing magnetic field. Because of hysteresis the phase of the magnetization lags behind the phase of the applied field. Thus the axis of the magnetic field induced in the rotor lags behind the axis of the stator field by a constant angle δ, producing torque as the rotor tries to "catch up" with the stator field. As long as the rotor is below synchronous speed, each particle of the rotor experiences a reversing magnetic field at the "slip" frequency that drives it around its hysteresis loop, causing the rotor field to lag and create torque. The rotor has a 2-pole low reluctance bar structure. As the rotor approaches synchronous speed and slip goes to zero, this magnetizes and aligns with the stator field, causing the rotor to "lock" to the rotating stator field.

A major advantage of the hysteresis motor is that since the lag angle δ is independent of speed, it develops constant torque from startup to synchronous speed. Therefore, it is self-starting and doesn't need an induction winding to start it, although many designs embed a squirrel-cage conductive winding structure in the rotor to provide extra torque at start-up.

Hysteresis motors are manufactured in sub-fractional horsepower ratings, primarily as servomotors and timing motors. More expensive than the reluctance type, hysteresis motors are used where precise constant speed is required.

### Externally excited motors

Usually made in larger sizes (larger than about 1 horsepower or 1 kilowatt) these motors require direct current (DC) to excite (magnetize) the rotor. This is most straightforwardly supplied through slip rings.

A brushless AC induction and rectifier arrangement can also be used.

## Control techniques

A permanent magnet synchronous motor and reluctance motor requires a control system for operating (VFD or servo drive).

There is a large number of control methods for synchronous machines, selected depending on the construction of the electric motor and the scope.

Control methods can be divided into:

- Scalar control
  - V/f control
- Vector control
  - Field oriented control
  - Direct torque control, a variant of VC
  - Feedback linearization

The PMSMs can also operate on open-loop control, which is sometimes used for start-up thus enabling the position sensing operation.

## Synchronous speed

The synchronous speed of a synchronous motor is given: in RPM, by:

$N_{s}=60{\frac {f}{P}}=120{\frac {f}{p}}$

and in rad·s−1, by:

$\omega _{s}=2\pi {\frac {f}{P}}=4\pi {\frac {f}{p}}$

where:

- f is the frequency of the AC supply current in Hz,
- p is the number of magnetic poles,
- P is the number of pole pairs (rarely, *planes of commutation*), $P=p/2$ .

### Examples

A single-phase, 4-pole (2-pole-pair) synchronous motor is operating at an AC supply frequency of 50 Hz. The number of pole-pairs is 2, so the synchronous speed is:

$N_{s}=60\;{\frac {\text{rpm}}{\text{Hz}}}\times {\frac {50{\text{ Hz}}}{2}}=1500\,\,{\text{rpm}}$

A three-phase, 12-pole (6-pole-pair) synchronous motor is operating at an AC supply frequency of 60 Hz. The number of pole-pairs is 6, so the synchronous speed is:

$N_{s}=60\;{\frac {\text{rpm}}{\text{Hz}}}\times {\frac {60{\text{ Hz}}}{6}}=600\,\,{\text{rpm}}$

The number of magnetic poles, p , is equal to the number of coil groups per phase. To determine the number of coil groups per phase in a 3-phase motor, count the number of coils, divide by the number of phases, which is 3. The coils may span several slots in the stator core, making it tedious to count them. For a 3-phase motor, if you count a total of 12 coil groups, it has 4 magnetic poles. For a 12-pole 3-phase machine, there will be 36 coils. The number of magnetic poles in the rotor is equal to the number of magnetic poles in the stator.

## Construction

The principal components of electric motors are the stator and the rotor. Synchronous motor and induction motor stators are similar in construction. The construction of synchronous motor is similar to that of an alternator (also called synchronous generator). The stator frame contains wrapper plate (except for wound-rotor synchronous doubly fed electric machines). Circumferential ribs and keybars are attached to the wrapper plate. To carry the weight of the machine, frame mounts and footings are required. The synchronous stator winding consists of a 3 phase winding. It is provided with a 3 phase supply, and the rotor is provided with a DC supply.

DC excited motors require brushes and slip rings to connect to the excitation supply. The field winding can be excited by a brushless exciter. Cylindrical, round rotors, (also known as non-salient pole rotor) are used for up to six poles.

In some machines or when a large number of poles are needed, a salient pole rotor is used.

Most synchronous motor construction uses a stationary armature and rotating field winding. This type of construction has an advantage over DC motor type where the armature used is of rotating type.

## Operation

Electric motors generate power due to the interaction of the magnetic fields of the stator and the rotor. In synchronous motors, the stator carries 3 phase currents and produces 3 phase rotating magnetic flux (and therefore a rotating magnetic field). The rotor eventually locks in with the rotating magnetic field and rotates along with it. Once the rotor field locks in with the rotating magnetic field, the motor is said to be synched. A single-phase (or two-phase derived from single phase) stator is possible, but in this case the direction of rotation is not defined and the machine may start in either direction unless prevented from doing so by startup arrangements.

### Amortisseur winding

Once the motor is in operation, the speed of the motor is dependent only on the supply frequency. When the motor load is increased beyond the breakdown load, the motor falls out of synchronization and the rotor no longer follows the rotating magnetic field.

Since the motor cannot produce torque if it falls out of synchronization, practical synchronous motors have a partial or complete squirrel-cage damper called an *amortisseur* winding to stabilize operation and facilitate starting.

Because this winding is smaller than that of an equivalent induction motor and can overheat on long operation, and because large slip-frequency voltages are induced in the rotor excitation winding, synchronous motor protection devices sense this condition and interrupt the power supply (out of step protection).

## Starting methods

Above a certain size, synchronous motors cannot self-start. This property is due to rotor inertia; it cannot instantly follow the rotation of the stator's magnetic field. Since a synchronous motor produces no inherent average torque at standstill, it cannot accelerate to synchronous speed without a supplemental mechanism.

Large motors operating on commercial power include a squirrel-cage induction winding that provides sufficient torque for acceleration and also serves to damp motor speed oscillations. Once the rotor nears the synchronous speed, the field winding becomes excited and the motor pulls into synchronization. Very large motor systems may include a "pony" motor that accelerates the unloaded synchronous machine before load is applied. Electronically controlled motors can be accelerated from zero speed by changing the frequency of the stator current.

Small synchronous motors are commonly used in line-powered electric mechanical clocks or timers that use the power line frequency to run the gear mechanism at the correct speed. Such small synchronous motors are able to start without assistance if the moment of inertia of the rotor and its mechanical load are sufficiently small. The motor accelerates from slip speed to synchronous speed during an accelerating half cycle of the reluctance torque. Single-phase synchronous motors such as in electric wall clocks can freely rotate in either direction, unlike a shaded-pole type.

Costs are an important parameter for starters. Rotor excitation is a possible way to resolve the issue. In addition, starting methods for large synchronous machines include repetitive polarity inversion of the rotor poles during startup.

## Applications, special properties, and advantages

### Use as synchronous condenser

By varying the excitation of a synchronous motor, it can be made to operate at lagging, leading and unity power factor. Excitation at which the power factor is unity is termed *normal excitation voltage*. The magnitude of current at this excitation is minimum. Excitation voltage more than normal excitation is called over excitation voltage, excitation voltage less than normal excitation is called under excitation. When the motor is over excited, the back emf will be greater than the motor terminal voltage. This causes a demagnetizing effect due to armature reaction.

The V curve of a synchronous machine shows armature current as a function of field current. With increasing field current armature current at first decreases, then reaches a minimum, then increases. The minimum point is also the point at which power factor is unity.

This ability to selectively control power factor can be exploited for power factor correction of the power system to which the motor is connected. Since most power systems of any significant size have a net lagging power factor, the presence of overexcited synchronous motors moves the system's net power factor closer to unity, improving efficiency. Such power-factor correction is usually a side effect of motors already present in the system to provide mechanical work, although motors can be run without mechanical load simply to provide power-factor correction. In large industrial plants such as factories the interaction between synchronous motors and other, lagging, loads may be an explicit consideration in the plant's electrical design.

### Steady-state stability limit

$\mathbf {T} =\mathbf {T} _{\text{max}}\sin(\delta )$

where,

$\mathbf {T}$

is the torque

$\delta$

is the

torque angle

$\mathbf {T} _{\text{max}}$

is the maximum torque

here,

$\mathbf {T} _{\text{max}}={\frac {{\mathbf {3} }{\mathbf {V} }{\mathbf {E} }}{{\mathbf {X_{s}} }{\omega _{s}}}}$

When load is applied, torque angle $\delta$ increases. When $\delta$ = 90° the torque will be maximum. If load is applied further then the motor will lose its synchronism, since motor torque will be less than load torque. The maximum load torque that can be applied to a motor without losing its synchronism is called steady state stability limit of a synchronous motor.

### Other

Synchronous motors are especially useful in applications requiring precise speed or position control:

- Speed is independent of the load over the operating range of the motor.
- Speed and position may be accurately controlled using open loop controls (e.g. stepper motors).
- Low-power applications include positioning machines, where high precision is required, and robot actuators.
- They will hold their position when a DC current is applied to both the stator and the rotor windings.
- A clock driven by a synchronous motor is in principle as accurate as the line frequency of its power source. (Although small frequency drifts will occur over any given several hours, grid operators actively adjust line frequency in later periods to compensate, thereby keeping motor-driven clocks accurate; see *Utility frequency § Stability*.)
- Record player turntables
- Increased efficiency in low-speed applications (e.g. ball mills).

## Subtypes

- AC motor § Polyphase synchronous motor
- Stepper motor (may be synchronous or not)
- Synchronous brushless wound-rotor doubly-fed electric machine
