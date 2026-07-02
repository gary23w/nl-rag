---
title: "Pressure measurement (part 1/2)"
source: https://en.wikipedia.org/wiki/Bourdon_tube
domain: pressure-sensors
license: CC-BY-SA-4.0
tags: pressure sensor, piezoresistive effect, bourdon tube, barometer
fetched: 2026-07-02
part: 1/2
---

# Pressure measurement

(Redirected from

Bourdon tube

)

**Pressure measurement** is the measurement of an applied force per unit area by a fluid (liquid or gas) on a surface. Pressure is typically expressed in units of pascals in the International System of Units (SI). Many techniques have been developed for the measurement of pressure and vacuum. Instruments used to measure and display pressure mechanically are called **pressure gauges,** **vacuum gauges** or **compound gauges** (vacuum & pressure). The widely used Bourdon gauge is a mechanical device, which both measures and indicates and is probably the best known type of gauge.

A vacuum gauge is used to measure pressures lower than the ambient atmospheric pressure, which is set as the zero point, in negative values (for instance, −1 bar or −760 mmHg equals total vacuum). Most gauges measure pressure relative to atmospheric pressure as the zero point, so this form of reading is simply referred to as "gauge pressure". However, anything greater than total vacuum is technically a form of pressure. For very low pressures, a gauge that uses total vacuum as the zero point reference must be used, giving pressure reading as an absolute pressure.

Other methods of pressure measurement involve sensors that can transmit the pressure reading to a remote indicator or control system (telemetry).


## Absolute, gauge and differential pressures — zero reference

Everyday pressure measurements, such as for vehicle tire pressure, are usually made relative to ambient air pressure. In other cases measurements are made relative to a vacuum or to some other specific reference. When distinguishing between these zero references, the following terms are used:

- **Absolute pressure** is zero-referenced against a perfect vacuum, using an absolute scale, so it is equal to gauge pressure plus atmospheric pressure. Absolute pressure sensors are used in applications where a constant reference is required, like for example, high-performance industrial applications such as monitoring vacuum pumps, liquid pressure measurement, industrial packaging, industrial process control and aviation inspection.
- **Gauge pressure** is zero-referenced against ambient air pressure, so it is equal to absolute pressure minus atmospheric pressure. A tire pressure gauge is an example of gauge pressure measurement; when it indicates zero, then the pressure it is measuring is the same as the ambient pressure. Most sensors for measuring up to 50 bar are manufactured in this way, since otherwise the atmospheric pressure fluctuation (weather) is reflected as an error in the measurement result.
- **Differential pressure** is the difference in pressure between two points. Differential pressure sensors are used to measure many properties, such as pressure drops across oil filters or air filters, fluid levels (by comparing the pressure above and below the liquid) or flow rates (by measuring the change in pressure across a restriction). Technically speaking, most pressure sensors are really differential pressure sensors; for example a gauge pressure sensor is merely a differential pressure sensor in which one side is open to the ambient atmosphere. A DP cell is a device that measures the differential pressure between two inputs.

The zero reference in use is usually implied by context, and these words are added only when clarification is needed. Tire pressure and blood pressure are gauge pressures by convention, while atmospheric pressures, deep vacuum pressures, and altimeter pressures must be absolute.

For most working fluids where a fluid exists in a closed system, gauge pressure measurement prevails. Pressure instruments connected to the system will indicate pressures relative to the current atmospheric pressure. The situation changes when extreme vacuum pressures are measured, then absolute pressures are typically used instead and measuring instruments used will be different.

Differential pressures are commonly used in industrial process systems. Differential pressure gauges have two inlet ports, each connected to one of the volumes whose pressure is to be monitored. In effect, such a gauge performs the mathematical operation of subtraction through mechanical means, obviating the need for an operator or control system to watch two separate gauges and determine the difference in readings.

Moderate *vacuum pressure* readings can be ambiguous without the proper context, as they may represent absolute pressure or gauge pressure without a negative sign. Thus a vacuum of 26 inHg gauge is equivalent to an absolute pressure of 4 inHg, calculated as 30 inHg (typical atmospheric pressure) − 26 inHg (gauge pressure).

Atmospheric pressure is typically about 100 kPa at sea level, but is variable with altitude and weather. If the absolute pressure of a fluid stays constant, the gauge pressure of the same fluid will vary as atmospheric pressure changes. For example, when a car drives up a mountain, the (gauge) tire pressure goes up because atmospheric pressure goes down. The absolute pressure in the tire is essentially unchanged.

Using atmospheric pressure as reference is usually signified by a "g" for gauge after the pressure unit, e.g. 70 psig, which means that the pressure measured is the total pressure minus atmospheric pressure. There are two types of gauge reference pressure: vented gauge (vg) and sealed gauge (sg).

A vented-gauge pressure transmitter, for example, allows the outside air pressure to be exposed to the negative side of the pressure-sensing diaphragm, through a vented cable or a hole on the side of the device, so that it always measures the pressure referred to ambient barometric pressure. Thus a vented-gauge reference pressure sensor should always read zero pressure when the process pressure connection is held open to the air.

A sealed gauge reference is very similar, except that atmospheric pressure is sealed on the negative side of the diaphragm. This is usually adopted on high pressure ranges, such as hydraulics, where atmospheric pressure changes will have a negligible effect on the accuracy of the reading, so venting is not necessary. This also allows some manufacturers to provide secondary pressure containment as an extra precaution for pressure equipment safety if the burst pressure of the primary pressure sensing diaphragm is exceeded.

There is another way of creating a sealed gauge reference, and this is to seal a high vacuum on the reverse side of the sensing diaphragm. Then the output signal is offset, so the pressure sensor reads close to zero when measuring atmospheric pressure.

A sealed gauge reference pressure transducer will never read exactly zero because atmospheric pressure is always changing and the reference in this case is fixed at 1 bar.

To produce an absolute pressure sensor, the manufacturer seals a high vacuum behind the sensing diaphragm. If the process-pressure connection of an absolute-pressure transmitter is open to the air, it will read the actual barometric pressure.

A **sealed pressure sensor** is similar to a gauge pressure sensor except that it measures pressure relative to some fixed pressure rather than the ambient atmospheric pressure (which varies according to the location and the weather).


## History

For much of human history, the pressure of gases like air was ignored, denied, or taken for granted, but as early as the 6th century BC, Greek philosopher Anaximenes of Miletus claimed that all things are made of air that is simply changed by varying levels of pressure. He could observe water evaporating, changing to a gas, and felt that this applied even to solid matter. More condensed air made colder, heavier objects, and expanded air made lighter, hotter objects. This was akin to how gases really do become less dense when warmer, more dense when cooler.

In the 17th century, Evangelista Torricelli conducted experiments with mercury that allowed him to measure the presence of air. He would dip a glass tube, closed at one end, into a bowl of mercury and raise the closed end up out of it, keeping the open end submerged. The weight of the mercury would pull it down, leaving a partial vacuum at the far end. This validated his belief that air/gas has mass, creating pressure on things around it. Previously, the more popular conclusion, even for Galileo, was that air was weightless and it is vacuum that provided force, as in a siphon. The discovery helped bring Torricelli to the conclusion:

> We live submerged at the bottom of an ocean of the element air, which by unquestioned experiments is known to have weight.

This test, known as Torricelli's experiment, was essentially the first documented pressure gauge.

Blaise Pascal went further, having his brother-in-law try the experiment at different altitudes on a mountain, and finding indeed that the farther down in the ocean of atmosphere, the higher the pressure.


## Units

Pressure units

Pascals

Bars

Standard atmospheres

Pounds per square inch

Millimetres of mercury

Inches of mercury

Technical atmospheres

Torrs

1

Pa

≡

1

N

⁄

m

2

=

1

×

10

−5

bar

≈

9.869

23

×

10

−6

atm

≈

1.450

38

×

10

−4

psi

≈

7.500

62

×

10

−3

mmHg

≈

2.953

00

×

10

−4

inHg

≈

1.019

72

×

10

−5

kgf/cm

2

≈

7.500

62

×

10

−3

Torr

1

bar

=

100

000

Pa

≡

100

000

N

⁄

m

2

≈

0.986

92

atm

≈

14.5038

psi

≈

750.062

mmHg

≈

29.5300

inHg

≈

1.019

72

kgf/cm

2

≈

750.062

Torr

1

atm

=

101

325

Pa

=

1.013

25

bar

≡

101

325

N

⁄

m

2

≈

14.6959

psi

≈

760.000

mmHg

≈

29.9213

inHg

≈

1.033

23

kgf/cm

2

=

760

Torr

1

psi

≈

6

894.76

Pa

≈

0.068

95

bar

≈

0.068

05

atm

≡

1

lb

⁄

in

2

≈

51.7149

mmHg

≈

2.036

02

inHg

≈

0.070

31

kgf/cm

2

≈

51.7149

Torr

1

mmHg

≈

133.322

Pa

≈

1.333

22

×

10

−3

bar

≈

1.315

79

×

10

−3

atm

≈

0.019

34

psi

≡

g

n

×

.001

m

×

13595.1

kg

⁄

m

3

≈

0.039

37

inHg

≈

1.359

51

×

10

−3

kgf/cm

2

≈

1.000

00

Torr

1

inHg

≈

3

386.39

Pa

≈

0.033

86

bar

≈

0.033

42

atm

≈

0.491

15

psi

=

25.4

mmHg

≡

g

n

×

.0254

m

×

13595.1

kg

⁄

m

3

≈

0.034

5316

kgf/cm

2

≈

25.4000

Torr

1

kgf

⁄

cm

2

≈

98

066.5

Pa

≈

0.980

66

bar

≈

0.967

84

atm

≈

14.2233

psi

≈

735.559

mmHg

≈

28.9590

inHg

≡

1

kgf

⁄

cm

2

≈

735.559

Torr

1

Torr

≈

133.322

Pa

≈

1.333

22

×

10

−3

bar

≈

1.315

79

×

10

−3

atm

≈

0.019

34

psi

≈

1.000

00

mmHg

≈

0.039

37

inHg

≈

1.359

51

×

10

−3

kgf/cm

2

≡

⁠

101

325

/

760

⁠

=

⁠

20

265

/

172

⁠

N

⁄

m

2

The SI unit for pressure is the pascal (Pa), equal to one newton per square metre (N·m−2 or kg·m−1·s−2). This special name for the unit was added in 1971; before that, pressure in SI was expressed in units such as N·m−2. When indicated, the zero reference is stated in parentheses following the unit, for example 101 kPa (abs). The pound per square inch (psi) is still in widespread use in the US and Canada, for measuring, for instance, tire pressure. A letter is often appended to the psi unit to indicate the measurement's zero reference; psia for absolute, psig for gauge, psid for differential, although this practice is discouraged by the NIST.

Because pressure was once commonly measured by its ability to displace a column of liquid in a manometer, pressures are often expressed as a depth of a particular fluid (*e.g.,* inches of water). Manometric measurement is the subject of pressure head calculations. The most common choices for a manometer's fluid are mercury (Hg) and water; water is nontoxic and readily available, while mercury's density allows for a shorter column (and so a smaller manometer) to measure a given pressure. The abbreviation "W.C." or the words "water column" are often printed on gauges and measurements that use water for the manometer.

Fluid density and local gravity can vary from one reading to another depending on local factors, so the height of a fluid column does not define pressure precisely. So measurements in "millimetres of mercury" or "inches of mercury" can be converted to SI units as long as attention is paid to the local factors of fluid density and gravity. Temperature fluctuations change the value of fluid density, while location can affect gravity.

Although no longer preferred, these **manometric units** are still encountered in many fields. Blood pressure is measured in millimetres of mercury (see torr) in most of the world, central venous pressure and lung pressures in centimeters of water are still common, as in settings for CPAP machines. Natural gas pipeline pressures are measured in inches of water, expressed as "inches W.C."

Underwater divers use manometric units: the ambient pressure is measured in units of metres sea water (msw) which is defined as equal to one tenth of a bar. The unit used in the US is the foot sea water (fsw), based on standard gravity and a sea-water density of 64 lb/ft3. According to the US Navy Diving Manual, one fsw equals 0.30643 msw, 0.030643 bar, or 0.44444 psi, though elsewhere it states that 33 fsw is 14.7 psi (one atmosphere), which gives one fsw equal to about 0.445 psi. The msw and fsw are the conventional units for measurement of diver pressure exposure used in decompression tables and the unit of calibration for pneumofathometers and hyperbaric chamber pressure gauges. Both msw and fsw are measured relative to normal atmospheric pressure.

In vacuum systems, the units torr (millimeter of mercury), micron (micrometer of mercury), and inch of mercury (inHg) are most commonly used. Torr and micron usually indicates an absolute pressure, while inHg usually indicates a gauge pressure.

Atmospheric pressures are usually stated using hectopascal (hPa), kilopascal (kPa), millibar (mbar) or atmospheres (atm). In American and Canadian engineering, stress is often measured in kip. Stress is not a true pressure since it is not scalar. In the cgs system the unit of pressure was the barye (ba), equal to 1 dyn·cm−2. In the mts system, the unit of pressure was the pieze, equal to 1 sthene per square metre.

Many other hybrid units are used such as mmHg/cm2 or grams-force/cm2 (sometimes as kg/cm2 without properly identifying the force units). Using the names kilogram, gram, kilogram-force, or gram-force (or their symbols) as a unit of force is prohibited in SI; the unit of force in SI is the newton (N).


## Static and dynamic pressure

Static pressure is uniform in all directions, so pressure measurements are independent of direction in an immovable (static) fluid. Flow, however, applies additional pressure on surfaces perpendicular to the flow direction, while having little impact on surfaces parallel to the flow direction. This directional component of pressure in a moving (dynamic) fluid is called dynamic pressure. An instrument facing the flow direction measures the sum of the static and dynamic pressures; this measurement is called the total pressure or stagnation pressure. Since dynamic pressure is referenced to static pressure, it is neither gauge nor absolute; it is a differential pressure.

While static gauge pressure is of primary importance to determining net loads on pipe walls, dynamic pressure is used to measure flow rates and airspeed. Dynamic pressure can be measured by taking the differential pressure between instruments parallel and perpendicular to the flow. Pitot-static tubes, for example perform this measurement on airplanes to determine airspeed. The presence of the measuring instrument inevitably acts to divert flow and create turbulence, so its shape is critical to accuracy and the calibration curves are often non-linear.


## Instruments

A **pressure sensor** is a device for pressure measurement of gases or liquids. Pressure sensors can alternatively be called **pressure transducers**, **pressure transmitters**, **pressure senders**, **pressure indicators**, **piezometers** and **manometers**, among other names.

Pressure is an expression of the force required to stop a fluid from expanding, and is usually stated in terms of force per unit area. A pressure sensor usually acts as a transducer; it generates a signal as a function of the pressure imposed.

Pressure sensors can vary drastically in technology, design, performance, application suitability and cost. A conservative estimate would be that there may be over 50 technologies and at least 300 companies making pressure sensors worldwide. There is also a category of pressure sensors that are designed to measure in a dynamic mode for capturing very high speed changes in pressure. Example applications for this type of sensor would be in the measuring of combustion pressure in an engine cylinder or in a gas turbine. These sensors are commonly manufactured out of piezoelectric materials such as quartz.

Some pressure sensors are pressure switches, which turn on or off at a particular pressure. For example, a water pump can be controlled by a pressure switch so that it starts when water is released from the system, reducing the pressure in a reservoir.

Pressure range, sensitivity, dynamic response and cost all vary by several orders of magnitude from one instrument design to the next. The oldest type is the liquid column manometer (a vertical tube filled with mercury) invented by Evangelista Torricelli in 1643. The U-Tube was invented by Christiaan Huygens in 1661.

There are two basic categories of analog pressure sensors: force collector and other types.

**Force collector types**

These types of electronic pressure sensors generally use a force collector (such a diaphragm, piston, Bourdon tube, or bellows) to measure strain (or deflection) due to applied force over an area (pressure).

- ***Piezoresistive strain gauge***: Uses the piezoresistive effect of bonded or formed strain gauges to detect strain due to an applied pressure, electrical resistance increasing as pressure deforms the material. Common technology types are silicon (monocrystalline), polysilicon thin film, bonded metal foil, thick film, silicon-on-sapphire and sputtered thin film. Generally, the strain gauges are connected to form a Wheatstone bridge circuit to maximize the output of the sensor and to reduce sensitivity to errors. This is the most commonly employed sensing technology for general purpose pressure measurement.
- ***Capacitive***: Uses a diaphragm and pressure cavity to create a variable capacitor to detect strain due to applied pressure, capacitance decreasing as pressure deforms the diaphragm. Common technologies use metal, ceramic, and silicon diaphragms. Capacitive pressure sensors are being integrated into CMOS technology and it is being explored if thin 2D materials can be used as diaphragm material.
- ***Electromagnetic***: Measures the displacement of a diaphragm by means of changes in inductance (reluctance), linear variable differential transformer (LVDT), Hall effect, or by eddy current principle.
- ***Piezoelectric***: Uses the piezoelectric effect in certain materials such as quartz to measure the strain upon the sensing mechanism due to pressure. This technology is commonly employed for the measurement of highly dynamic pressures. As the basic principle is dynamic, no static pressures can be measured with piezoelectric sensors.
- ***Strain-Gauge***: Strain gauge based pressure sensors also use a pressure sensitive element where metal strain gauges are glued on or thin-film gauges are applied on by sputtering. This measuring element can either be a diaphragm or for metal foil gauges measuring bodies in can-type can also be used. The big advantages of this monolithic can-type design are an improved rigidity and the capability to measure highest pressures of up to 15,000 bar. The electrical connection is normally done via a Wheatstone bridge, which allows for a good amplification of the signal and precise and constant measuring results.
- ***Optical***: Techniques include the use of the physical change of an optical fiber to detect strain due to applied pressure. A common example of this type utilizes Fiber Bragg Gratings. This technology is employed in challenging applications where the measurement may be highly remote, under high temperature, or may benefit from technologies inherently immune to electromagnetic interference. Another analogous technique utilizes an elastic film constructed in layers that can change reflected wavelengths according to the applied pressure (strain).
- ***Potentiometric***: Uses the motion of a wiper along a resistive mechanism to detect the strain caused by applied pressure.

- ***Force balancing***: Force-balanced fused quartz Bourdon tubes use a spiral Bourdon tube to exert force on a pivoting armature containing a mirror, the reflection of a beam of light from the mirror senses the angular displacement and current is applied to electromagnets on the armature to balance the force from the tube and bring the angular displacement to zero, the current that is applied to the coils is used as the measurement. Due to the extremely stable and repeatable mechanical and thermal properties of fused quartz and the force balancing which eliminates most non-linear effects these sensors can be accurate to around 1PPM of full scale. Due to the extremely fine fused quartz structures which are made by hand and require expert skill to construct these sensors are generally limited to scientific and calibration purposes. Non force-balancing sensors have lower accuracy and reading the angular displacement cannot be done with the same precision as a force-balancing measurement, although easier to construct due to the larger size these are no longer used.

**Other types**

These types of electronic pressure sensors use other properties (such as density) to infer pressure of a gas, or liquid.

- ***Resonant***: Uses the changes in resonant frequency in a sensing mechanism to measure stress, or changes in gas density, caused by applied pressure. This technology may be used in conjunction with a force collector, such as those in the category above. Alternatively, resonant technology may be employed by exposing the resonating element itself to the media, whereby the resonant frequency is dependent upon the density of the media. Sensors have been made out of vibrating wire, vibrating cylinders, quartz, and silicon MEMS. Generally, this technology is considered to provide very stable readings over time. The squeeze-film pressure sensor is a type of MEMS resonant pressure sensor that operates by a thin membrane that compresses a thin film of gas at high frequency. Since the compressibility and stiffness of the gas film are pressure dependent, the resonance frequency of the squeeze-film pressure sensor is used as a measure of the gas pressure.
- ***Thermal***: Uses the changes in thermal conductivity of a gas due to density changes to measure pressure. A common example of this type is the Pirani gauge.
- ***Ionization***: Measures the flow of charged gas particles (ions) which varies due to density changes to measure pressure. Common examples are the Hot and Cold Cathode gauges.

A pressure sensor, a resonant quartz crystal strain gauge with a Bourdon tube force collector, is the critical sensor of DART. DART detects tsunami waves from the bottom of the open ocean. It has a pressure resolution of approximately 1mm of water when measuring pressure at a depth of several kilometers.

### Hydrostatic

**Hydrostatic** gauges (such as the mercury column manometer) compare pressure to the hydrostatic force per unit area at the base of a column of fluid. Hydrostatic gauge measurements are independent of the type of gas being measured, and can be designed to have a very linear calibration. They have poor dynamic response.

#### Piston

Piston-type gauges counterbalance the pressure of a fluid with a spring (for example tire-pressure gauges of comparatively low accuracy) or a solid weight, in which case it is known as a deadweight tester and may be used for calibration of other gauges.

#### Liquid column (manometer)

Liquid-column gauges consist of a column of liquid in a tube whose ends are exposed to different pressures. The column will rise or fall until its weight (a force applied due to gravity) is in equilibrium with the pressure differential between the two ends of the tube (a force applied due to fluid pressure). A very simple version is a U-shaped tube half-full of liquid, one side of which is connected to the region of interest while the reference pressure (which might be the atmospheric pressure or a vacuum) is applied to the other. The difference in liquid levels represents the applied pressure. The pressure exerted by a column of fluid of height *h* and density *ρ* is given by the hydrostatic pressure equation, *P* = *hgρ*. Therefore, the pressure difference between the applied pressure *Pa* and the reference pressure *P*0 in a U-tube manometer can be found by solving *Pa* − *P*0 = *hgρ*. In other words, the pressure on either end of the liquid (shown in blue in the figure) must be balanced (since the liquid is static), and so *Pa* = *P*0 + *hgρ*.

In most liquid-column measurements, the result of the measurement is the height *h*, expressed typically in mm, cm, or inches. The *h* is also known as the pressure head. When expressed as a pressure head, pressure is specified in units of length and the measurement fluid must be specified. When accuracy is critical, the temperature of the measurement fluid must likewise be specified, because liquid density is a function of temperature. So, for example, pressure head might be written "742.2 mmHg" or "4.2 inH2O at 59 °F" for measurements taken with mercury or water as the manometric fluid respectively. The word "gauge" or "vacuum" may be added to such a measurement to distinguish between a pressure above or below the atmospheric pressure. Both mm of mercury and inches of water are common pressure heads, which can be converted to S.I. units of pressure using unit conversion and the above formulas.

If the fluid being measured is significantly dense, hydrostatic corrections may have to be made for the height between the moving surface of the manometer working fluid and the location where the pressure measurement is desired, except when measuring differential pressure of a fluid (for example, across an orifice plate or venturi), in which case the density ρ should be corrected by subtracting the density of the fluid being measured.

Although any fluid can be used, mercury is preferred for its high density (13.534 g/cm3) and low vapour pressure. Its convex meniscus is advantageous since this means there will be no pressure errors from wetting the glass, though under exceptionally clean circumstances, the mercury will stick to glass and the barometer may become stuck (the mercury can sustain a negative absolute pressure) even under a strong vacuum. For low pressure differences, light oil or water are commonly used (the latter giving rise to units of measurement such as inches water gauge and millimetres H2O). Liquid-column pressure gauges have a highly linear calibration. They have poor dynamic response because the fluid in the column may react slowly to a pressure change.

One of the disadvantages of the mercury manometer or barometer is that its reading is temperature dependent, a fact made clear by the use of mercury in glass thermometers.

When measuring vacuum, the working liquid may evaporate and contaminate the vacuum if its vapor pressure is too high. When measuring liquid pressure, a loop filled with gas or a light fluid can isolate the liquids to prevent them from mixing, but this can be unnecessary, for example, when mercury is used as the manometer fluid to measure differential pressure of a fluid such as water. Simple hydrostatic gauges can measure pressures ranging from a few torrs (a few 100 Pa) to a few atmospheres (approximately 1000000 Pa).

A single-limb liquid-column manometer has a larger reservoir instead of one side of the U-tube and has a scale beside the narrower column. The column may be inclined to further amplify the liquid movement. Based on the use and structure, following types of manometers are used

1. Simple manometer
2. Micromanometer
3. Differential manometer
4. Inverted differential manometer

#### McLeod gauge

A McLeod gauge isolates a sample of gas and compresses it in a modified mercury manometer until the pressure is a few millimetres of mercury. The technique is very slow and unsuited to continual monitoring, but is capable of good accuracy. Unlike other manometer gauges, the McLeod gauge reading is dependent on the composition of the gas, since the interpretation relies on the sample compressing as an ideal gas. Due to the compression process, the McLeod gauge completely ignores partial pressures from non-ideal vapors that condense, such as pump oils, mercury, and even water if compressed enough.

Useful range

: from around 10

−4

Torr

(roughly 10

−2

Pa) to vacuums as high as 10

−6

Torr (0.1

mPa),

0.1 mPa is the lowest direct measurement of pressure that is possible with current technology. Other vacuum gauges can measure lower pressures, but only indirectly by measurement of other pressure-dependent properties. These indirect measurements must be calibrated to SI units by a direct measurement, most commonly a McLeod gauge.

### Aneroid

**Aneroid** gauges are based on a metallic pressure-sensing element that flexes elastically under the effect of a pressure difference across the element. "Aneroid" means "without fluid", and the term originally distinguished these gauges from the hydrostatic gauges described above. However, aneroid gauges can be used to measure the pressure of a liquid as well as a gas, and they are not the only type of gauge that can operate without fluid. For this reason, they are often called **mechanical** gauges in modern language. Aneroid gauges are not dependent on the type of gas being measured, unlike thermal and ionization gauges, and are less likely to contaminate the system than hydrostatic gauges. The pressure sensing element may be a **Bourdon tube**, a diaphragm, a capsule, or a set of bellows, which will change shape in response to the pressure of the region in question. The deflection of the pressure sensing element may be read by a linkage connected to a needle, or it may be read by a secondary transducer. The most common secondary transducers in modern vacuum gauges measure a change in capacitance due to the mechanical deflection. Gauges that rely on a change in capacitance are often referred to as capacitance manometers.

#### Bourdon tube

The Bourdon pressure gauge uses the principle that a flattened tube tends to straighten or regain its circular form in cross-section when pressurized. (A party horn illustrates this principle.) This change in cross-section may be hardly noticeable, involving moderate stresses within the elastic range of easily workable materials. The strain of the material of the tube is magnified by forming the tube into a C shape or even a helix, such that the entire tube tends to straighten out or uncoil elastically as it is pressurized. Eugène Bourdon patented his gauge in France in 1849, and it was widely adopted because of its superior simplicity, linearity, and accuracy; Bourdon is now part of the Baumer group and still manufacture Bourdon tube gauges in France. Edward Ashcroft purchased Bourdon's American patent rights in 1852 and became a major manufacturer of gauges. Also in 1849, Bernard Schaeffer in Magdeburg, Germany patented a successful diaphragm (see below) pressure gauge, which, together with the Bourdon gauge, revolutionized pressure measurement in industry. But in 1875 after Bourdon's patents expired, his company Schaeffer and Budenberg also manufactured Bourdon tube gauges.

In practice, a flattened thin-wall, closed-end tube is connected at the hollow end to a fixed pipe containing the fluid pressure to be measured. As the pressure increases, the closed end moves in an arc, and this motion is converted into the rotation of a (segment of a) gear by a connecting link that is usually adjustable. A small-diameter pinion gear is on the pointer shaft, so the motion is magnified further by the gear ratio. The positioning of the indicator card behind the pointer, the initial pointer shaft position, the linkage length and initial position, all provide means to calibrate the pointer to indicate the desired range of pressure for variations in the behavior of the Bourdon tube itself. Differential pressure can be measured by gauges containing two different Bourdon tubes, with connecting linkages (but is more usually measured via diaphragms or bellows and a balance system).

Bourdon tubes measures gauge pressure, relative to ambient atmospheric pressure, as opposed to absolute pressure; vacuum is sensed as a reverse motion. Some aneroid barometers use Bourdon tubes closed at both ends (but most use diaphragms or capsules, see below). When the measured pressure is rapidly pulsing, such as when the gauge is near a reciprocating pump, an orifice restriction in the connecting pipe is frequently used to avoid unnecessary wear on the gears and provide an average reading; when the whole gauge is subject to mechanical vibration, the case (including the pointer and dial) can be filled with an oil or glycerin. Typical high-quality modern gauges provide an accuracy of ±1% of span (Nominal diameter 100mm, Class 1 EN837-1), and a special high-accuracy gauge can be as accurate as 0.1% of full scale.

Force-balanced fused quartz Bourdon tube sensors work on the same principle but uses the reflection of a beam of light from a mirror to sense the angular displacement and current is applied to electromagnets to balance the force of the tube and bring the angular displacement back to zero, the current that is applied to the coils is used as the measurement. Due to the extremely stable and repeatable mechanical and thermal properties of quartz and the force balancing which eliminates nearly all physical movement these sensors can be accurate to around 1 PPM of full scale. Due to the extremely fine fused quartz structures which must be made by hand these sensors are generally limited to scientific and calibration purposes.

In the following illustrations of a compound gauge (vacuum and gauge pressure), the case and window has been removed to show only the dial, pointer and process connection. This particular gauge is a combination vacuum and pressure gauge used for automotive diagnosis:

- The left side of the face, used for measuring vacuum, is calibrated in inches of mercury on its outer scale and centimetres of mercury on its inner scale
- The right portion of the face is used to measure fuel pump pressure or turbo boost and is scaled in pounds per square inch on its outer scale and kg/cm2 on its inner scale.

Mechanical details include stationary and moving parts.

Stationary parts:

1. Receiver block. This joins the inlet pipe to the fixed end of the Bourdon tube (1) and secures the chassis plate (B). The two holes receive screws that secure the case.
2. Chassis plate. The dial is attached to this. It contains bearing holes for the axles.
3. Secondary chassis plate. It supports the outer ends of the axles.
4. Posts to join and space the two chassis plates.

Moving parts:

1. Stationary end of Bourdon tube. This communicates with the inlet pipe through the receiver block.
2. Moving end of Bourdon tube. This end is sealed.
3. Pivot and pivot pin
4. Link joining pivot pin to lever (5) with pins to allow joint rotation
5. Lever, an extension of the sector gear (7)
6. Sector gear axle pin
7. Sector gear
8. Indicator needle axle. This has a spur gear that engages the sector gear (7) and extends through the face to drive the indicator needle. Due to the short distance between the lever arm link boss and the pivot pin and the difference between the effective radius of the sector gear and that of the spur gear, any motion of the Bourdon tube is greatly amplified. A small motion of the tube results in a large motion of the indicator needle.
9. Hair spring to preload the gear train to eliminate gear lash and hysteresis

#### Diaphragm (membrane)

A second type of aneroid gauge uses deflection of a flexible membrane that separates regions of different pressure. The amount of deflection is repeatable for known pressures so the pressure can be determined by using calibration. The deformation of a thin diaphragm is dependent on the difference in pressure between its two faces. The reference face can be open to atmosphere to measure gauge pressure, open to a second port to measure differential pressure, or can be sealed against a vacuum or other fixed reference pressure to measure absolute pressure. The deformation can be measured using mechanical, optical or capacitive techniques. Ceramic and metallic diaphragms are used. The useful range is above 10−2 Torr (roughly 1 Pa). For absolute measurements, welded pressure capsules with diaphragms on either side are often used. Membrane shapes include:

- Flat
- Corrugated
- Flattened tube
- Capsule

#### Bellows

In gauges intended to sense small pressures or pressure differences, or require that an absolute pressure be measured, the gear train and needle may be driven by an enclosed and sealed bellows chamber, called an **aneroid**. (Early barometers used a column of liquid such as water or the liquid metal mercury suspended by a vacuum.) This bellows configuration is used in aneroid barometers (barometers with an indicating needle and dial card), altimeters, altitude recording barographs, and the altitude telemetry instruments used in weather balloon radiosondes. These devices use the sealed chamber as a reference pressure and are driven by the external pressure. Other sensitive aircraft instruments such as air speed indicators and rate of climb indicators (variometers) have connections both to the internal part of the aneroid chamber and to an external enclosing chamber.

#### Magnetic coupling

These gauges use the attraction of two magnets to translate differential pressure into motion of a dial pointer. As differential pressure increases, a magnet attached to either a piston or rubber diaphragm moves. A rotary magnet that is attached to a pointer then moves in unison. To create different pressure ranges, the spring rate can be increased or decreased.

### Spinning-rotor gauge

The spinning-rotor gauge works by measuring how a rotating ball is slowed by the viscosity of the gas being measured. The ball is made of steel and is magnetically levitated inside a steel tube closed at one end and exposed to the gas to be measured at the other. The ball is brought up to speed (about 2500 or 3800 rad/s), and the deceleration rate is measured after switching off the drive, by electromagnetic transducers. The range of the instrument is 5−5 to 102 Pa (103 Pa with less accuracy). It is accurate and stable enough to be used as a secondary standard. During the last years this type of gauge became much more user friendly and easier to operate. In the past the instrument was famous for requiring some skill and knowledge to use correctly. For high accuracy measurements various corrections must be applied and the ball must be spun at a pressure well below the intended measurement pressure for five hours before using. It is most useful in calibration and research laboratories where high accuracy is required and qualified technicians are available. Insulation vacuum monitoring of cryogenic liquids is a well suited application for this system too. With the inexpensive and long term stable, weldable sensor, that can be separated from the more costly electronics, it is a perfect fit to all static vacuums.
