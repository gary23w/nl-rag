---
title: "Load cell"
source: https://en.wikipedia.org/wiki/Load_cell
domain: load-cells-strain
license: CC-BY-SA-4.0
tags: load cell, strain gauge, wheatstone bridge, force-sensing resistor
fetched: 2026-07-02
---

# Load cell

A **load cell** converts a force such as tension, compression, pressure, or torque into a signal (electrical, pneumatic or hydraulic pressure, or mechanical displacement indicator) that can be measured and standardized. It is a force transducer. As the force applied to the load cell increases, the signal changes proportionally. The most common types of load cells are pneumatic, hydraulic, and strain gauge types for industrial applications. Typical non-electronic bathroom scales are a widespread example of a mechanical displacement indicator where the applied weight (force) is indicated by measuring the deflection of springs supporting the load platform, technically a "load cell".

## Strain gauge load cell

Strain gauge load cells are the kind most often found in industrial settings. It is ideal as it is highly accurate, versatile, and cost-effective. Structurally, a load cell has a metal body to which strain gauges have been secured. The body is usually made of aluminum, alloy steel, or stainless steel which makes it very sturdy but also minimally elastic. This elasticity gives rise to the term "spring element", referring to the body of the load cell. When force is exerted on the load cell, the spring element is slightly deformed, and unless overloaded, always returns to its original shape. As the spring element deforms, the strain gauges also change shape. The resulting alteration to the resistance in the strain gauges can be measured as voltage. The change in voltage is proportional to the amount of force applied to the cell, so the amount of force can be calculated from the load cell's output.

### Strain gauges

A strain gauge is constructed of very fine wire, or foil, set up in a grid pattern and attached to a flexible backing. When the shape of the strain gauge is altered, a change in its electrical resistance occurs. The wire or foil in the strain gauge is arranged in a way that, when force is applied in one direction, a linear change in resistance results. Tension force stretches a strain gauge, causing it to get thinner and longer, resulting in an increase in resistance. Compression force does the opposite. The strain gauge compresses, becomes thicker and shorter, and resistance decreases. The strain gauge is attached to a flexible backing enabling it to be easily applied to a load cell, mirroring the minute changes to be measured.

Since the change in resistance measured by a single strain gauge is extremely small, it is difficult to accurately measure changes. Increasing the number of strain gauges applied collectively magnifies these small changes into something more measurable. A set of 4 strain gauges set in a specific circuit is an application of a Wheatstone bridge.

### Wheatstone bridge

A Wheatstone bridge is a configuration of four balanced resistors with a known excitation voltage applied.

Excitation voltage $V_{\text{EX}}$ is a known constant, and output voltage $V_{\text{o}}$ is variable depending on the shape of the strain gauges. If all resistors are balanced, meaning $R1/R2=R4/R3$ , then $V_{\text{o}}$ is zero. If the resistance in even one of the resistors changes, then $V_{\text{o}}$ likewise changes. The change in $V_{\text{o}}$ can be measured and interpreted using Ohm's law. Ohm's law states that the current ( I , measured in amperes) running through a conductor between two points is directly proportional to the voltage V across the two points. Resistance ( R , measured in ohms) is introduced as the constant in this relationship, independent of the current. Ohm's law is expressed in the equation $I=V/R$ . When applied to the 4 legs of the Wheatstone bridge circuit, the resulting equation is $V_{\text{o}}=\left({\frac {R3}{R3+R4}}-{\frac {R2}{R1+R2}}\right)V_{\text{EX}}.$

In a load cell, the resistors are replaced with strain gauges and arranged in alternating tension and compression formation. When force is exerted on the load cell, the structure and resistance of the strain gauges changes, and $V_{\text{o}}$ is measured. From the resulting data, $V_{\text{o}}$ can be easily determined using the equation above.

### Common types of strain gauge load cells

There are several types of strain gauge load cells:

- Single-point load cells; used in small to medium platform scales with platform sizes of 200 mm × 200 mm up to 1200 mm × 1200 mm.
- Planar beam load cells; used in low-profile solutions where space is limited, like medical scales and retail scales.
- Bending beam load cells; used in pallet, platform and small hopper scales.
- Shear beam load cells; used in low-profile scale and process applications, available in capacities from 100 kg up to 50 t.
- Dual shear beam load cells; used in truck scales, tank and hopper applications.
- S-type load cells; used in tension applications with static and dynamic loads.
- Compression load cells; used in truck scales, large platform scales, weighbridges and hopper scales.
- Ring torsion load cells; used in high-accuracy hoppers, silos, platforms and pallet scales.
- Spoke-type load cells; used in low-profile, high-precision application. High forces varying from 1 to 500 t.
- Onboard load cells; used for onboard weighing systems on trucks, tractors and other vehicles.
- Loadpins; used in applications for measuring dynamic, static or hoisting forces.
- Weighpads; portable weighpads for the weighing of cars and to measure the center of gravity of planes.
- Specials; various types of special sensors.

## Capacitive load cell

The digital capacitive technology is based on a non-contacting ceramic sensor mounted inside the load cell body. As the load cell contains no moving parts and the ceramic sensor is not in contact with the load cell body, the load cell tolerates very high overloads (up to 1000%), sideloads, torsion, and stray welding voltages. This allows for simple installation of the load cells without expensive and complicated mounting kits, stay rods, or overload protection devices, which in turn eliminates the need for maintenance.

### The basic difference from strain gauge load cells

Capacitive and strain gauge load cells both rely on an elastic element that is deformed by the load to be measured. The material used for the elastic element is normally aluminum or stainless steel for load cells used in corrosive industrial applications. A strain gauge sensor measures the deformation of the elastic element, and the output of the sensor is converted by an electronic circuit to a signal that represents the load. Capacitive strain gauges measure the deformation of the elastic material using the change in capacitance of two plates as the plates move closer to each other.

Capacitive sensors have a high sensitivity compared to strain gauges. Because of the much higher sensitivity, a much lower deformation of the elastic element is needed, and the elastic element of a capacitive load cell is therefore strained around 5 to 10 times lower than the elastic element of a strain gauge load cell. The low strained element combined with the fact that a capacitive sensor is non-contacting, provides the very high shock resistance and overload capability of the capacitive load cell compared to the strain gage load cell. This is an obvious advantage in industrial environments and especially for the lower capacity load cells where the risk of damage because of shocks and overloads is high.

### Connectivity of capacitive load cells

In a standard analog strain gauge load cell, the power supply and the low-level analog signal are normally conducted through a rather expensive 6-wire cable to the instrumentation where the analog signal is converted to a digital signal. Instead, digital capacitive load cells transmit the digital signal back to the instrumentation which may be placed several hundred meters away without influencing the reading.

## Pneumatic load cell

The pneumatic load cell is designed to automatically regulate the balancing pressure. Air pressure is applied to one end of the diaphragm and it escapes through the nozzle placed at the bottom of the load cell. A pressure gauge is attached to the load cell to measure the pressure inside the cell. The deflection of the diaphragm affects the airflow through the nozzle as well as the pressure inside the chamber.

## Hydraulic load cell

The hydraulic load cell uses a conventional piston and cylinder arrangement with the piston placed in a thin elastic diaphragm. The piston doesn't actually come in contact with the load cell. Mechanical stops are placed to prevent overstrain of the diaphragm when the loads exceed a certain limit. The load cell is completely filled with oil. When the load is applied on the piston, the movement of the piston and the diaphragm results in an increase of oil pressure. This pressure is then transmitted to a hydraulic pressure gauge via a high pressure hose. The gauge's Bourdon tube senses the pressure and registers it on the dial. Because this sensor has no electrical components, it is ideal for use in hazardous areas. Typical hydraulic load cell applications include tank, bin, and hopper weighing. By example, a hydraulic load cell is immune to transient voltages (lightning) so these types of load cells might be a more effective device in outdoor environments. This technology is more expensive than other types of load cells. It is a more costly technology and thus cannot effectively compete on a cost of purchase basis.

## Other types

### Vibrating load cell

Vibrating wire load cells, which are useful in geomechanical applications due to low amounts of drift,

### Piezoelectric load cell

Piezoelectric load cells work on the same principle of deformation as the strain gauge load cells, but a voltage output is generated by the basic piezoelectric material – proportional to the deformation of load cell. Useful for dynamic/frequent measurements of force. Most applications for piezo-based load cells are in the dynamic loading conditions, where strain gauge load cells can fail with high dynamic loading cycles. The piezoelectric effect is dynamic, that is, the electrical output of a gauge is an impulse function and is not static. The voltage output is only useful when the strain is changing and does not measure static values.

However, depending on conditioning system used, "quasi static" operation can be done. Using a charge amplifier with a long time constant allows accurate measurement lasting many minutes for small loads up to many hours for large loads. Another advantage of Piezoelectric load cells conditioned with a charge amplifier is the wide measuring range that can be achieved. Users can choose a load cell with a range of hundred of kilonewtons and use it for measuring few newtons of force with the same signal-to-noise ratio; again this is possible only with the use of a charge amplifier for conditioning.

## Common issues

- Mechanical mounting: the cells have to be properly mounted. All the load force has to go through the part of the load cell where its deformation is sensed. Friction may induce offset or hysteresis. Wrong mounting may result in the cell reporting forces along undesired axis, which still may somewhat correlate to the sensed load, confusing the technician.
- Overload: Within its rating, the load cell deforms elastically and returns to its shape after being unloaded. If subjected to loads above its maximum rating, the material of the load cell may plastically deform; this may result in a signal offset, loss of linearity, difficulty with or impossibility of calibration, or even mechanical damage to the sensing element (e.g. delamination, rupture). Capacitive load cells compared to strain gauges are more resistant to overloads, due to their contactless measuring principle.
- Wiring issues: the wires to the cell may develop high resistance, e.g. due to corrosion. Alternatively, parallel current paths can be formed by ingress of moisture. In both cases the signal develops offset (unless all wires are affected equally) and accuracy is lost.
- Electrical damage: the load cells can be damaged by induced or conducted current. Lightning hitting the construction, or arc welding performed near the cells, can overstress the fine resistors of the strain gauges and cause their damage or destruction. For welding nearby, it is suggested to disconnect the load cell and short all its pins to the ground, nearby the cell itself. High voltages can break through the insulation between the substrate and the strain gauges.
- Nonlinearity: at the low end of their scale, the load cells tend to be nonlinear. This becomes important for cells sensing very large ranges, or with large surplus of load capability to withstand temporary overloads or shocks (e.g. the rope clamps). More points may be needed for the calibration curve.
- Particularity of application: A load cell that is not well suited to the specific magnitude and type of pressure will have poor accuracy, resolution, and reliability.

### Excitation and rated output

The bridge is excited with stabilized voltage (usually 10V, but can be 20V, 5V, or less for battery powered instrumentation). The difference voltage proportional to the load then appears on the signal outputs. The cell output is rated in millivolts per volt (mV/V) of the difference voltage at full rated mechanical load. So a 2.96 mV/V load cell will provide 29.6 millivolt signal at full load when excited with 10 volts.

Typical sensitivity values are 1 to 3 mV/V. Typical maximum excitation voltage is around 15 volts.

### Wiring

The full-bridge cells come typically in four-wire configuration. The wires to the top and bottom end of the bridge are the excitation (often labelled E+ and E−, or Ex+ and Ex−), the wires to its sides are the signal (labelled S+ and S−). Ideally, the voltage difference between S+ and S− is zero under zero load, and grows proportionally to the load cell's mechanical load.

Sometimes a six-wire configuration is used. The two additional wires are "sense" (Sen+ and Sen−), and are connected to the bridge with the Ex+ and Ex- wires, in a fashion similar to four-terminal sensing. With these additional signals, the controller can compensate for the change in wire resistance due to external factors, e.g. temperature fluctuations.

The individual resistors on the bridge usually have resistance of 350 Ω. Sometimes other values (typically 120 Ω, 1,000 Ω) can be encountered.

The bridge is typically electrically insulated from the substrate. The sensing elements are in close proximity and in good mutual thermal contact, to avoid differential signals caused by temperature differences.

#### Using multiple cells

One or more load cells can be used for sensing a single load.

If the force can be concentrated to a single point (small scale sensing, ropes, tensile loads, point loads), a single cell can be used. For long beams, two cells at the end are used. Vertical cylinders can be measured at three points, rectangular objects usually require four sensors. More sensors are used for large containers or platforms, or very high loads.

If the loads are guaranteed to be symmetrical, some of the load cells can be substituted with pivots. This saves the cost of the load cell but can significantly decrease accuracy.

Load cells can be connected in parallel; in that case, all the corresponding signals are connected together (Ex+ to Ex+, S+ to S+, ...), and the resulting signal is the average of the signals from all the sensing elements. This is often used in e.g. personal scales, or other multipoint weight sensors.

The most common color assignment is red for Ex+, black for Ex−, green for S+, and white for S−.

Less common assignments are red for Ex+, white for Ex−, green for S+, and blue for S−, or red for Ex+, blue for Ex−, green for S+, and yellow for S−. Other values are also possible, e.g. red for Ex+, green for Ex−, yellow for S+ and blue for S−.

## Ringing

Every load cell is subject to "ringing" when subjected to abrupt load changes. This stems from the spring-like behavior of load cells. In order to measure the loads, they have to deform. As such, a load cell of finite stiffness must have spring-like behavior, exhibiting vibrations at its natural frequency. An oscillating data pattern can be the result of ringing. Ringing can be suppressed in a limited fashion by passive means. Alternatively, a control system can use an actuator to actively damp out the ringing of a load cell. This method offers better performance at a cost of significant increase in complexity.

## Uses

Load cells are used in several types of measuring instruments such as laboratory balances, industrial scales, platform scales and universal testing machines. From 1993 the British Antarctic Survey installed load cells in glass fibre nests to weigh albatross chicks. Load cells are used in a wide variety of items such as the seven-post shaker which is often used to set up race cars. Another common use is within sim racing, where the advantage of a load cell over a potentiometer is that simulated braking force is based on the user’s force on the pedal, rather than the position of the pedal. Load cells are also widely used in food processing, warehousing, logistics, and general manufacturing for applications such as batching, filling, pallet weighing, shipping verification, and process monitoring.

## Load cells weighing performances

Load cells are commonly used to measure weight in an industrial environment. They can be installed on hoppers, reactors, etc., to control their weight capacity, which is often of critical importance for an industrial process. Some performance characteristics of the load cells must be defined and specified to make sure they will cope with the expected service. Among those design characteristics are:

- Combined error
- Minimum verification interval
- Resolution

## Load cell specifications

The electrical, physical, and environmental specifications of a load cell help to determine which applications it is appropriate for. Common specifications include:

- Full-scale output (FSO): Electronic output expressed in mV/V. Measured at full scale.
- Combined error: percent of the full scale output that represents the maximum deviation from the straight line drawn between no load and load at rated capacity. Often measured during decreasing and increasing loads.
- Non-linearity: The maximum deviation of the calibration curve from a straight line drawn between the rated capacity and zero load. Measured on increasing load and expressed as percent of full scale output.
- Hysteresis: Maximum difference between load cell output signals for the same applied load. The first measurement can be obtained by decreasing the load from rated output and the second by increasing the load from zero.
- Repeatability: Maximum difference between output measurements for repeated loads under identical conditions. Measured in percent of rated output.
- Zero balance (offset): Output reading of the load cell with rated excitation under no load. The deviation in output between a true zero measurement and a real load cell under zero load expressed as a percentage of full scale output.
- Compensated temperature range: The temperature range over which a load cell is compensated so that it can ensure zero balance & rated output within specified limits. Expressed as °F or °C.
- Operating temperature range: Temperature range extremes in which a load cell can operate without permanent, adverse effects on any of its performance characteristics. Expressed as °F or °C.
- Temperature effect on output: Modification of output readings caused by load cell temperature. Expressed as percent of full scale output per degree of °F or °C.
- Temperature effect on zero: Change in zero balance caused by ambient temperature changes. Expressed as percent of full scale output per degree of °F or °C.
- Input resistance: Input resistance of the load cell's bridge circuit. Measured at the positive & negative excitation leads with no load applied. Measured in ohms.
- Output resistance: Output resistance of the load cell's bridge circuit. Measured at the positive & negative excitation leads with no load applied. Measured in ohms.
- Insulation resistance: The resistance measured along pathways between the: bridge circuit and transducer element, bridge circuit and the cable shield, and the transducer element and the cable shield. Typically measured at fifty volts under standard test conditions.
- Recommended excitation: Maximum recommended excitation voltage of the transducer for it to operate within its specifications. Expressed in VDC.
- Cable length: Length of the standard cable for which the load cell is calibrated. Cable length affects how the load cell is calibrated.
- Safe overload: The maximum load that can be applied to a load cell without causing permanent effects to its performance specifications. Measured as a percent of full scale output.
- Ultimate overload: Maximum load that can be withstood without causing structural failure.
- Material: Substance that comprises the spring element of the load cell.

## Load cell calibration

Load cells are an integral part of most weighing systems in industrial, aerospace and automotive industries, enduring rigorous daily use. Over time, load cells will drift, age and misalign; therefore, they will need to be calibrated regularly to ensure accurate results are maintained. ISO9000 and most other standards specify a maximum period of around 18 months to 2 years between re-calibration procedures, dependent on the level of load cell deterioration. Annual re-calibration is considered best practice by many load cell users for ensuring the most accurate measurements.

Standard calibration tests will use linearity and repeatability as a calibration guideline as these are both used to determine accuracy. Calibration is conducted incrementally starting working in ascending or descending order. For example, in the case of a 60 tonne load cell, then specific test weights that measure in 5, 10, 20, 40 and 60 tonne increments may be used; a five step calibration process is usually sufficient for ensuring a device is accurately calibrated. Repeating this five-step calibration procedure 2-3 times is recommended for consistent results.
