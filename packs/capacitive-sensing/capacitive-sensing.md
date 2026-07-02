---
title: "Capacitive sensing"
source: https://en.wikipedia.org/wiki/Capacitive_sensing
domain: capacitive-sensing
license: CC-BY-SA-4.0
tags: capacitive sensing, capacitance measurement, touchscreen sensing, tactile sensor
fetched: 2026-07-02
---

# Capacitive sensing

In electrical engineering, **capacitive sensing** (sometimes **capacitance sensing**) is a technology, based on capacitive coupling, that can detect and measure anything that is conductive or has a dielectric constant different from air. Many types of sensors use capacitive sensing, including sensors to detect and measure proximity, pressure, position and displacement, force, humidity, fluid level, and acceleration. Human interface devices based on capacitive sensing, such as touchpads, can be used in place of a computer mouse. Digital audio players, mobile phones, and tablet computers will sometimes use capacitive sensing touchscreens as input devices. Capacitive sensors can also replace mechanical buttons.

A capacitive touchscreen typically consists of a capacitive touch sensor along with at least two complementary metal–oxide–semiconductor (CMOS) integrated circuit (IC) chips, an application-specific integrated circuit (ASIC) controller and a digital signal processor (DSP). Capacitive sensing is commonly used for mobile multi-touch displays, popularized by Apple's iPhone in 2007.

## Design

Capacitive sensors are constructed from many different media, such as copper, indium tin oxide (ITO) and printed ink. Copper capacitive sensors can be implemented on standard FR4 PCBs as well as on flexible material. ITO allows the capacitive sensor to be up to 90% transparent (for one layer solutions, such as touch phone screens). Size and spacing of the capacitive sensor are both very important to the sensor's performance. In addition to the size of the sensor, and its spacing relative to the ground plane, the type of ground plane used is very important. Since the parasitic capacitance of the sensor is related to the electric field's (E-field) path to ground, it is important to choose a ground plane that limits the concentration of E-field lines with no conductive object present.

Designing a capacitance sensing system requires first picking the type of sensing material (FR4, Flex, ITO, etc.). One also needs to understand the environment the device will operate in, such as the full operating temperature range, what radio frequencies are present and how the user will interact with the interface. Tools such as CapExt, ANSYS Q3D Extractor, and solutions from FastFieldSolvers can be employed to optimize designs by enhancing sensitivity, accurately modeling electromagnetic fields, and improving performance across varying environmental conditions.

There are two types of capacitive sensing systems:

1. mutual capacitance, where the object (finger, capacitive stylus) alters the mutual coupling between row and column electrodes, which are scanned sequentially; and
2. self-capacitance, where the object (such as a finger) loads the sensor or increases the parasitic capacitance to ground.

In both cases, the difference of a preceding absolute position from the present absolute position yields the relative motion of the object or finger during that time. The technologies are elaborated in the following section.

### Surface capacitance

In this basic technology, only one side of the insulator is coated with conductive material. A small voltage is applied to this layer, resulting in a uniform electrostatic field. When a conductor, such as a human finger, touches the uncoated surface, a capacitor is dynamically formed. Because of the sheet resistance of the surface, each corner is measured to have a different effective capacitance. The sensor's controller can determine the location of the touch indirectly from the change in the capacitance as measured from the four corners of the panel: the larger the change in capacitance, the closer the touch is to that corner. With no moving parts, it is moderately durable, but has low resolution, is prone to false signals from parasitic capacitive coupling, and needs calibration during manufacture. Therefore, it is most often used in simple applications such as industrial controls and interactive kiosks.

### Projected capacitance

Projected capacitance touch (PCT) technology is a capacitive technology which allows more accurate and flexible operation, by etching the conductive layer. An X-Y grid is formed either by etching one layer to form a grid pattern of electrodes, or by etching two separate, parallel layers of conductive material with perpendicular lines or tracks to form the grid; comparable to the pixel grid found in many liquid crystal displays (LCD).

The greater resolution of PCT allows operation with no direct contact, such that the conducting layers can be coated with further protective insulating layers, and operate even under screen protectors, or behind weather and vandal-proof glass. Because the top layer of a PCT is glass, PCT is a more robust solution versus resistive touch technology. Depending on the implementation, an active or passive stylus can be used instead of or in addition to a finger. This is common with point of sale devices that require signature capture. Gloved fingers may not be sensed, depending on the implementation and gain settings. Conductive smudges and similar interference on the panel surface can interfere with the performance. Such conductive smudges come mostly from sticky or sweaty finger tips, especially in high humidity environments. Collected dust, which adheres to the screen because of moisture from fingertips can also be a problem.

There are two types of PCT: self capacitance, and mutual capacitance.

*Mutual capacitive* sensors have a capacitor at each intersection of each row and each column. A 12-by-16 array, for example, would have 192 independent capacitors. A voltage is applied to the rows or columns. Bringing a finger or conductive stylus near the surface of the sensor changes the local electric field which reduces the mutual capacitance. The capacitance change at every individual point on the grid can be measured to accurately determine the touch location by measuring the voltage in the other axis. Mutual capacitance allows multi-touch operation where multiple fingers, palms or styli can be accurately tracked at the same time.

*Self-capacitance* sensors can have the same X-Y grid as mutual capacitance sensors, but the columns and rows operate independently. With self-capacitance, current senses the capacitive load of a finger on each column or row. This produces a stronger signal than mutual capacitance sensing, but it is unable to resolve accurately more than one finger, which results in "ghosting", or misplaced location sensing.

## Circuit design

Capacitance is typically measured indirectly, by using it to control the frequency of an oscillator, or to vary the level of coupling (or attenuation) of an AC signal. Basically the technique works by charging the unknown capacitance with a known current, since rearranging the current–voltage relation for a capacitor,

$I(t)=C{\frac {\mathrm {d} V(t)}{\mathrm {d} t}}\,,$

allows determining the capacitance from the instantaneous current divided by the rate of change of voltage across the capacitor:

$C={\frac {I(t)}{\frac {\mathrm {d} V(t)}{\mathrm {d} t}}}\,.$

That can be integrated over a charging time period from $t_{0}$ to $t_{1}$ to be expressed in integral form as: $C={\frac {\int _{t_{0}}^{t_{1}}I(t)\,\mathrm {d} t}{(V(t_{1})-V(t_{0}))}}\,.$

### Types

#### Step response

For a simple example of the above equation, if the charging current is constant and the starting voltage $V(t_{0})$ is 0 V, then the capacitance is simply the value of that constant current multiplied by the charging time duration $(t_{1}-t_{0})$ and divided by the final voltage $V(t_{1})\,.$

Either this charging time or voltage can be a predetermined constant. For instance, if measuring after a constant amount of time, then the capacitance can be determined using only the final voltage. Alternatively if using a fixed threshold voltage, then instead only need to measure the charging time duration to reach that voltage threshold.

This step response measurement can be continually repeated (e.g. by using a square wave).

For an example capacitive sense IC, Texas Instruments's FDC1004 applies a 25-kHz step waveform to charge up an electrode, and after a defined amount of time, converts the analog voltage representing that charge into a digital value of capacitance using a built-in analog-to-digital converter (ADC).

#### Relaxation oscillator

The design of a simple capacitance meter is often based on a relaxation oscillator. The capacitance to be sensed forms a portion of the oscillator's RC circuit or LC circuit. The capacitance can be calculated by measuring the charging time required to reach the threshold voltage (of the relaxation oscillator), or equivalently, by measuring the oscillator's frequency. Both of these are proportional to the RC (or LC) time constant of the oscillator circuit.

#### Voltage divider

Another measurement technique is to apply a fixed-frequency AC-voltage signal across a capacitive divider (a voltage divider that uses capacitors instead of resistors). This consists of two capacitors in series, one of a known value and the other of an unknown value. An output signal is then taken from across one of the capacitors. The value of the unknown capacitor can be found from the ratio of capacitances, which equals the ratio of the output/input signal amplitudes, as could be measured by an AC voltmeter.

#### Bridge configuration

More accurate instruments may use a capacitance bridge configuration, similar to a Wheatstone bridge. The capacitance bridge helps to compensate for any variability that may exist in the applied signal.

#### Charge transfer

While not specific to capacitive sensing, charge transfer uses a switched capacitor network to accumulate charge onto an integrating capacitor over a series of discrete steps, to produce an accurate sum of all the individual charge contributors.

#### Delta-sigma

Delta-sigma modulation can also measure capacitance instead of voltage.

### Errors

The primary source of error in capacitance measurements is stray capacitance, which if not guarded against, may fluctuate between roughly 10 pF and 10 nF. The stray capacitance can be held relatively constant by shielding the (high impedance) capacitance signal and then connecting the shield to (a low impedance) ground reference. Also, to minimize the unwanted effects of stray capacitance, it is good practice to locate the sensing electronics as near the sensor electrodes as possible.

## Comparison with other touchscreen technologies

Capacitive touchscreens are more responsive than resistive touchscreens (which react to any object since no capacitance is needed). However, projective capacitance improves a touchscreen's accuracy as it forms a triangulated grid around the point of touch.

A standard stylus cannot be used for capacitive sensing, but special capacitive styli, which are conductive, exist for the purpose. These special styli used to be more expensive to purchase, but the cost of this technology has fallen greatly and capacitive styli are now widely available for a nominal charge, and are sometimes given away for free with mobile accessories. They consist of an electrically conductive shaft with a soft conductive rubber tip, thereby resistively connecting the fingers to the tip of the stylus. One can even make a capacitive stylus by wrapping conductive material, such as anti-static conductive film, around a standard stylus or by rolling the film into a tube.

Some capacitative touchscreens cannot be used with gloves and can fail to sense correctly with even a small amount of water on the screen.

The capacitive touchscreens used to be more expensive to manufacture than resistive touchscreens.

Mutual capacitive sensors can provide a two-dimensional image of the changes in the electric field. Using this image, a range of applications have been proposed. Authenticating users, estimating the orientation of fingers touching the screen and differentiating between fingers and palms become possible. While capacitive sensors are used for the touchscreens of most smartphones, the capacitive image is typically not exposed to the application layer.

Power supplies with a high level of electronic noise can reduce accuracy.

## Pen computing

Many stylus designs for resistive touchscreens will not register on capacitive sensors because they are not conductive. Styluses that work on capacitive touchscreens primarily designed for fingers are required to simulate the difference in dielectric offered by a human finger.
