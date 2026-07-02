---
title: "Roller screw"
source: https://en.wikipedia.org/wiki/Roller_screw
domain: linear-actuators
license: CC-BY-SA-4.0
tags: linear actuator, ball screw, leadscrew drive, rack and pinion
fetched: 2026-07-02
---

# Roller screw

A **roller screw**, also known as a **planetary roller screw** or **satellite roller screw**, is a low-friction precision screw-type actuator, a mechanical device for converting rotational motion to linear motion, or vice versa. Planetary roller screws are used as the actuating mechanism in many electromechanical linear actuators. Due to its complexity, the roller screw is a relatively expensive actuator (as much as an order of magnitude more expensive than ball screws), but may be suitable for high-precision, high-speed, heavy-load, long-life, and heavy-use applications.

Roller screw mechanisms are commonly incorporated into motion/positioning systems in a variety of industries such as manufacturing and aerospace. More recently, planetary roller screws have been adopted by humanoid robotics manufacturers, such as in the linear actuators of the Tesla Optimus, due to their ability to withstand high shock loads during dynamic movement.

## Principle of operation

A roller screw is a mechanical actuator similar to a ball screw, but which uses rollers as the load transfer elements between nut and screw instead of balls. The rollers are typically threaded but may also be grooved depending on roller screw type. Providing more bearing points than ball screws within a given volume, roller screws can be more compact for a given load capacity while providing similar efficiency (75%-90%) at low-to-moderate speeds, and maintain relatively high efficiency at high speeds. Roller screws can surpass ball screws in regard to positioning precision, load rating, rigidity, speed, acceleration, and lifetime. Standard roller screw actuators can achieve dynamic load ratings above 130 tons of force (exceeded in single-unit actuator capacity only by hydraulic cylinders).

The three main elements of a typical planetary roller screw are the screw shaft, the nut, and the planetary roller. The screw, a shaft with a multi-start V-shaped thread, provides a helical raceway for multiple rollers radially arrayed around the screw and encapsulated by a threaded nut. The thread of the screw is typically identical to the internal thread of the nut. The rollers spin in contact with, and serve as low-friction transmission elements between, screw and nut. The rollers typically have a single-start thread with convex flanks that limit friction at the rollers' contacts with screw and nut. The rollers typically orbit the screw as they spin (in the manner of planet gears to sun gear), and are thus known as planetary, or satellite, rollers. As with a lead screw or ball screw, rotation of the nut results in screw travel, and rotation of the screw results in nut travel.

For a given screw diameter and quantity of thread starts, more rollers correspond to higher static load capacity, but not necessarily to a higher dynamic load capacity. Preloaded split nuts and double nuts are available to eliminate backlash.

## Planetary roller screw types

Carl Bruno Strandgren developed some of the earliest effective forms of roller screws and applied for a patent in Nice, France in February 1942. The French patent #888.281 was granted in August 1943 and published in December of the same year. The first commercial roller screw was designed and manufactured under his supervision in 1949 and was mounted on a narrow-gauge locomotive which operated in a northern France coal mine. Subsequent units were produced and mounted on machine tools and (starting in 1955) on aircraft. At that time, Strandgren applied for a new patent incorporating detailed calculations and detailed manufacturing considerations, for which he was awarded US patents for such a “Screw-Threaded Mechanism” in 1954, and “Nut and Screw Devices” and the "Roller Screw" in 1965.

Roller screw types are defined by the motion of the rollers relative to the nut and screw. The four commercially available types of roller screw are *standard*, *inverted*, *recirculating*, and *bearing ring*.

*Differential roller screws*, typically variants of the standard and recirculating types, are also commercially available. Differential roller screws modify the rotational speed ratios between the rollers and the screw by varying the flank angles and contact points of the threads or grooves. In that way differential roller screws change the effective lead of the screw. William J. Roantree received a US patent for the "Differential Roller Nut" in 1968.

Now that the core patents have expired, an open source roller screw was developed in OpenSCAD to be 3-D printed for food processing applications. The planetary roller screw can be fabricated in dishwasher-safe polyethylene terephthalate glycol (PETG) on any desktop 3-D printer. The maximum force is more than doubled for the roller screw actuator using the same materials when compared to a direct screw press, making them adequate for some food processing techniques.

### Standard planetary roller screw

The standard planetary roller screw is also known as the non-recirculating roller screw. The lack of axial movement of the roller relative to the nut, and the gearing of rollers to nut, are definitive of the standard type of roller screw.

The nut and screw have identical multiple-start threads. The rollers have a single-start thread with an angle matching the nut thread. The matched thread angle prevents axial movement between the nut and the roller as the rollers spin. The nut assembly includes spacer rings and ring gears that position and guide the rollers. The spacer rings, which rotate within the ring gears, have equidistant holes that act as rotary bearings for the smooth pivot ends (studs) of the rollers. The ring gears time the spinning and orbit of the rollers about the screw axis by engaging gear teeth near the ends of the rollers. The spacer rings rotate on axis with the screw in unison with the orbit of the rollers. The spacer rings float relative to the nut, axially secured by retaining rings, because they spin around the screw at a lower frequency (angular velocity) than the nut.

#### Configuration

Standard roller screws are typically identified by screw diameter (typically ranging from 3.5mm – 200mm) and lead (1mm – 62mm). The threading of the screw (3 – 6 starts) is either rolled (lower capacity) or ground (higher capacity). The diameters of the nut and rollers (7 – 14 in quantity) are simple functions of the screw diameter and lead.

Where:

$s_{d}$

is the effective screw diameter, or

pitch diameter

$r_{d}$

is the effective roller diameter

$n_{d}$

is the effective nut inside diameter

t

is the thread starts on nut and screw

l

is the screw lead

p

is the roller thread

pitch

The following relationships apply to standard and inverted roller screws:

| $n_{d}={\frac {s_{d}t}{t-2}}$ | $\therefore$ | nut to screw gear ratio |
|---|---|---|
| $(n_{d}:s_{d})=1:{\frac {t}{t-2}}$ |   |   |
| $r_{d}={\frac {s_{d}}{t-2}}$ | $\therefore$ | roller to screw gear ratio |
| $(r_{d}:s_{d})=1:t-2$ |   |   |
| $r_{d}={\frac {n_{d}}{t}}$ | $\therefore$ | roller to nut gear ratio |
| $(r_{d}:n_{d})=1:t$ |   |   |
| $r_{d}={\frac {n_{d}-s_{d}}{2}}$ |   |   |
|   |   |   |
| $p={\frac {l}{t}}$ | $\therefore$ | ratio of roller thread pitch to |
| screw lead $(p:l)=1:t$ |   |   |

For example, if the screw diameter is 30 mm, the lead is 20 mm, and there are 5 thread starts, then the rollers have a diameter of 10 mm, the thread pitch is 4 mm, and the nut has a 50 mm effective diameter.

### Inverted roller screw

The inverted planetary roller screw is also known as the reverse roller screw. The lack of axial movement of the roller relative to the screw, and the gearing of rollers to screw, are definitive of the inverted type of planetary roller screw. This type of roller screw was developed simultaneously with the standard roller screw.

Inverted roller screws operate on the same principles of standard roller screws except that the function of the nut and screw is reversed in relation to the rollers. The rollers move axially within the nut, which is elongated to accommodate the full extent of screw shaft travel. The threaded portion of the screw shaft is limited to the threaded length of the rollers. The non-threaded portion of the screw shaft can be a smooth or non-cylindrical shape. The ring gear is replaced by gear teeth above and below the threaded portion of the screw shaft.

Aside from the inversion of the relationship of rollers to nut and screw, the configuration and relationships of inverted roller screws match those of standard roller screws.

### Recirculating roller screw

The recirculating type of planetary roller screw is also known as a recycling roller screw. A recirculating roller screw can provide a very high degree of positional accuracy by using minimal thread leads. The rollers of a recirculating roller screw move axially within the nut until being reset after one orbit about the screw. Recirculating roller screws do not employ ring gears. Carl Bruno Strandgren was awarded a US Patent for the recirculating roller screw in 1965.

The screw and nut may have very fine identical single- or two-start threads. Recirculating rollers are grooved (instead of threaded) so that they move axially during spinning engagement with the threads of the nut and screw, shifting up or down by one lead of thread after completing an orbit around the screw. The nut assembly typically includes a slotted cage and cam rings. The cage captivates the rollers in elongated slots, equally spacing the rollers while permitting rotation and axial motion of the rollers. The cam rings have opposing cams aligned with an axial groove in the wall of the nut. After a roller completes an orbit about the nut it is released into the groove, disengages from nut and screw, and is pushed between the cams to the axial midpoint of the nut assembly (shifting by a distance equal to the lead of the screw). Returned to its starting position, and reengaged to nut and screw, the roller may then orbit the screw once again.

In 2006, Charles C. Cornelius and Shawn P. Lawlor received a patent for a cageless recirculating roller screw system. As with the traditional recirculating roller screw system, rollers disengage from the screw when they come upon an axial groove in the wall of the nut. The system differs in that the rollers are continually engaged by the nut, and the axial groove of the nut is threaded. Non-helical threads in the axial groove of the nut return the roller to its axial starting position (after completion of an orbit). Non-circular compression rings, or cam rings, at opposite ends of the rollers (roller axles) apply constant pressure between rollers and nut, synchronizing roller rotation and thrusting the rollers into the nut's axial groove. Lacking ring gears and roller cage, cageless recirculating roller screws can be relatively efficient and, as a result, permit higher dynamic capacities for some screw shaft diameters.

### Bearing ring roller screw

In 1986 Oliver Saari was awarded a patent for a bearing ring roller screw, commonly referred to by its trademark, Spiracon. This type matches the orbit of the rollers to the rotation of the nut assembly. The actuator contains more load transfer elements than the other types, a bearing ring and thrust bearings, but manufacture of component parts is relatively simple (e.g. gearing teeth may be eliminated).

In the other roller screw types above, loads are transferred from the nut through the rollers to the screw (or in the reverse order). In this type of actuator, thrust bearings and a freely rotating internally grooved bearing ring transfer loads between the rollers and the nut.

The screw has a multi-start thread. The rollers and encapsulating rotating ring are identically grooved, not threaded, so there is no axial movement between the two. The nut assembly includes a cylindrical housing capped by non-rotating spacer rings. The spacer rings have equidistant holes that act as rotary bearings for the smooth pivot ends (studs) of the rollers. Roller-type thrust bearings between the spacer rings and bearing ring permit free rotation of the bearing ring while transferring the axial load between the two.

The rollers act as the “threads” of the nut assembly, causing axial movement of the rotating screw due to their orbital restraint. Screw rotation spins the rollers, which spin the bearing ring, dissipating the load-induced friction along the way.

Timothy A. Erhart was awarded a US patent in 1996 for a linear actuator effectively incorporating an inverted bearing ring roller screw. The screw shaft is grooved the length of and to match the grooved rollers, which travel with the shaft. The bearing ring is elongated and internally threaded for the length of screw shaft travel. The nut assembly housing and sealed end ring forms the exterior of the actuator assembly.
