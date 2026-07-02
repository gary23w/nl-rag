---
title: "Squirrel-cage rotor"
source: https://en.wikipedia.org/wiki/Squirrel-cage_rotor
domain: ac-induction-motors
license: CC-BY-SA-4.0
tags: induction motor, squirrel-cage rotor, rotating magnetic field, wound rotor motor
fetched: 2026-07-02
---

# Squirrel-cage rotor

A **squirrel-cage rotor** is the rotating part of the common squirrel-cage induction motor. It consists of a cylinder of steel laminations, with aluminum or copper conductors cast in its surface. In operation, the non-rotating stator winding is connected to an alternating current power source; the alternating current in the stator produces a rotating magnetic field. The rotor winding has current induced in it by the stator field, as happens in a transformer, except that the current in the rotor is varying at the stator field rotation rate minus the physical rotation rate. The interaction of the magnetic fields in the stator and the currents in the rotor produce a torque on the rotor.

By adjusting the shape of the bars in the rotor, the speed-torque characteristics of the motor can be changed, to minimize starting current or to maximize low-speed torque, for example.

Squirrel-cage induction motors are very prevalent in industry, in sizes from below 1 kilowatt (1.3 hp) up to tens of megawatts (tens-of-thousand horsepower). They are simple, rugged, and self-starting, and maintain a reasonably constant speed from light load to full load, set by the frequency of the power supply and the number of poles of the stator winding. Commonly used motors in industry are usually IEC or NEMA standard frame sizes, which are interchangeable between manufacturers. This simplifies application and replacement of these motors.

## History

Galileo Ferraris described an induction machine with a two-phase stator winding and a solid copper cylindrical armature in 1885. In 1888, Nikola Tesla received a patent on a two-phase induction motor with a short-circuited copper rotor winding and a two-phase stator winding. Developments of this design became commercially important. In 1889, Mikhail Dolivo-Dobrovolsky developed a wound-rotor induction motor, and shortly afterwards a cage-type rotor winding. By the end of the 19th century induction motors were widely applied on the growing alternating-current electrical distribution systems.

## Structure

The motor rotor shape is a cylinder mounted on a shaft. Internally it contains longitudinal conductive bars (usually made of aluminium or copper) set into grooves and connected at both ends by shorting rings forming a cage-like shape. The name is derived from the similarity between this rings-and-bars winding and a squirrel cage.

The solid core of the rotor is built with stacks of electrical steel laminations. The figure shows three of many lamination sets used. The rotor lamination has a larger number of slots than its corresponding stator lamination, and the number of rotor slots should be a non-integer multiple of the number of stator slots to prevent magnetic interlocking of rotor and stator teeth at the starting instant.

The rotor bars may be made of either copper or aluminium. A very common structure for smaller motors uses die cast aluminium poured into the rotor after the laminations are stacked. Larger motors have aluminium or copper bars which are welded or brazed to end-rings. Since the voltage developed in the squirrel cage winding is very low, and the current very high, no intentional insulation layer is present between the bars and the rotor steel.

## Theory

The field windings in the stator of an induction motor set up a rotating magnetic field through the rotor. The relative motion between this field and the rotor induces electric current in the conductive bars. In turn these currents lengthwise in the conductors react with the magnetic field of the motor to produce force acting at a tangent orthogonal to the rotor, resulting in torque to turn the shaft. In effect the rotor is carried around with the magnetic field but at a slightly slower rate of rotation. The difference in speed is called *slip* and increases with load.

### Skewing

The conductors are often skewed slightly along the length of the rotor to reduce noise and smooth out torque fluctuations that might result at some speeds due to interactions with the pole pieces of the stator, by ensuring that at any time the same fraction of a rotor bar is under each stator slot. If rotor bars were parallel to the stator poles, the motor would experience a drop and then recovery in torque as each bar passes the gap in the stator.

The laminations shown in the photo have 36 bars in the stator and 40 bars in the rotor. The greatest common divisor of 36 and 40 is 4, with the result that no more than 4 bars of the stator and rotor can be aligned at any one time, which also reduces torque fluctuations.

The number of bars in the rotor determines to what extent the induced currents are fed back to the stator coils and hence the current through them. The constructions that offer the least feedback use prime numbers of rotor bars.

### Laminations

The iron core serves to carry the magnetic field through the rotor conductors. Because the magnetic field in the rotor is alternating with time, the core uses construction similar to a transformer core to reduce core energy losses. It is made of thin laminations, separated by varnish insulation, to reduce eddy currents circulating in the core. The material is a low carbon but high-silicon iron with several times the resistivity of pure iron, further reducing eddy-current loss, and low coercivity to reduce hysteresis loss.

### Rotor bars

The same basic design is used for both single-phase and three-phase motors over a wide range of sizes. Rotors for three-phase will have variations in the depth and shape of bars to suit the design classification. Generally, thick bars have good torque and are efficient at low slip, since they present lower resistance to the EMF. As the slip increases, the skin effect starts to reduce the effective depth and increases the resistance, resulting in reduced efficiency but still maintaining torque.

The shape and depth of the rotor bars can be used to vary the speed-torque characteristics of the induction motor. At standstill, the revolving magnetic field passes the rotor bars at a high rate, inducing line-frequency current into the rotor bars. Due to the skin effect, the induced current tends to flow at the outer edge of the winding. As the motor accelerates, the slip frequency decreases and induced current flows at greater depths in the winding. By tapering the profile of the rotor bars to vary their resistance at different depths, or by constructing a double squirrel cage, with a combination of high and low impedance rotor in parallel the motor can be arranged to produce more or less torque at standstill and near its synchronous speed.

## Practical demonstration

To demonstrate how the cage rotor works, the stator of a single-phase motor and a copper pipe (as rotor) may be used. If adequate AC power is applied to the stator, an alternating magnetic field will revolve around within the stator. If the copper pipe is inserted inside the stator, there will be an induced current in the pipe, and this current will produce a magnetic field of its own in the pipe. The interaction between the stator's revolving magnetic field and the copper-pipe-rotor's induced magnetic field produces a torque and thus rotation.

## Use in synchronous motors

A synchronous motor may have a squirrel-cage winding embedded in its rotor, used to increase the motor starting torque and so decrease the time to accelerate to synchronous speed. The squirrel cage winding of a synchronous machine will generally be smaller than for an induction machine of similar rating. When the rotor is turning at the same speed as the stator's revolving magnetic field, no current is induced into the squirrel-cage windings and the windings will have no further effect on the operation of the synchronous motor at steady-state.

The squirrel cage winding in some machines provides a damping effect for load or system disturbances, and in this role may be designated as an amortisseur windings. Large machines may only have amortisseur bars in the individual pole faces, not interconnected between poles. Because the squirrel cage winding is not large enough to dissipate the heat of continuous operation, large synchronous machines often have protective relays to detect when the machine has fallen out of synchronization with the supply voltage.

## Induction generators

Three phase squirrel cage induction motors can also be used as generators. For this to work the motor must see a reactive load, and either be connected to a grid supply or an arrangement of capacitors to provide excitation current. For the motor to work as a generator instead of a motor the rotor must be spun faster than its stator's synchronous speed. This will cause the motor to generate power after building up its residual magnetism.
