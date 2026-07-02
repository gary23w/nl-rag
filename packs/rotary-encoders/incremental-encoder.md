---
title: "Incremental encoder"
source: https://en.wikipedia.org/wiki/Incremental_encoder
domain: rotary-encoders
license: CC-BY-SA-4.0
tags: rotary encoder, incremental encoder, gray code, resolver device
fetched: 2026-07-02
---

# Incremental encoder

An **incremental encoder** is a linear or rotary electromechanical device that has two output signals, *A* and *B*, which issue pulses when the device is moved. Together, the *A* and *B* signals indicate both the occurrence of and direction of movement. Many incremental encoders have an additional output signal, typically designated *index* or *Z*, which indicates the encoder is located at a particular reference position. Also, some encoders provide a status output (typically designated *alarm*) that indicates internal fault conditions such as a bearing failure or sensor malfunction.

Unlike an absolute encoder, an incremental encoder does not indicate absolute position; it only reports changes in position and the corresponding direction of movement for each change. Consequently, to determine absolute position at any particular moment, it is necessary to send the encoder signals to an *incremental encoder interface*, which in turn will "track" and report the encoder's absolute position.

Incremental encoders report position increments nearly instantaneously, which allows them to monitor the movements of high speed mechanisms in near real-time. Because of this, incremental encoders are commonly used in applications that require precise measurement and control of position and velocity.

## Quadrature outputs

An incremental encoder generates its *A* and *B* output signals using a quadrature encoding technique. When the encoder moves at a constant velocity, the *A* and *B* signals are square waves with a 90° phase difference between them, allowing detection of both movement and direction.

At any particular time, the phase difference between the *A* and *B* signals will be positive or negative depending on the encoder's direction of movement. In the case of a rotary encoder, the phase difference is +90° for clockwise rotation and −90° for counter-clockwise rotation, or vice versa, depending on the device design.

The frequency of the pulses on the *A* or *B* output is directly proportional to the encoder's velocity (rate of position change); higher frequencies indicate rapid movement, whereas lower frequencies indicate slower speeds. Static, unchanging signals are output on *A* and *B* when the encoder is motionless. In the case of a rotary encoder, the frequency indicates the speed of the encoder's shaft rotation, and in linear encoders the frequency indicates the speed of linear traversal.

**Conceptual drawings of quadrature encoder sensing mechanisms**

Quadrature encoder outputs can be produced by a quadrature-offset pattern read by aligned sensors (left diagram), or by a simple pattern read by offset sensors (right diagram).

- (Rotary encoder, with corresponding A/B signal states shown on the right as the shaft reverses.)Rotary encoder, with corresponding *A*/*B* signal states shown on the right as the shaft reverses.
- (Linear encoder; A&B sensors are offset by 90° phase of the simple pattern, the R index signal indicates the encoder is located at its reference position.)Linear encoder; *A*&*B* sensors are offset by 90° phase of the simple pattern, the *R* index signal indicates the encoder is located at its reference position.

### Resolution

The resolution of an incremental encoder is a measure of the precision of the position information it produces. Encoder resolution is typically specified in terms of the number of *A* (or *B*) pulses per unit displacement or, equivalently, the number of *A* (or *B*) square wave cycles per unit displacement. In the case of rotary encoders, resolution is specified as the number of pulses per revolution (PPR) or cycles per revolution (CPR), whereas linear encoder resolution is typically specified as the number of pulses issued for a particular linear traversal distance (e.g., 1000 pulses per mm).

This differs from the measurement resolution, which refers to the smallest change in position that the encoder can detect. Each signal edge on output *A* or *B* corresponds to a discrete position change. Because one full square-wave cycle on *A* (or *B*) includes four edges—rising *A*, rising *B*, falling *A*, and falling *B*—the measurement resolution is one-fourth of the distance represented by a full cycle. For example, a linear encoder with a resolution of 1000 pulses per millimeter has a per-cycle resolution of 1 μm (1 mm / 1000 cycles), yielding a measurement resolution of 250 nm (1 μm / 4).

### Symmetry and phase

When moving at constant velocity, an ideal incremental encoder would output perfect square waves on *A* and *B* (i.e., the pulses would be exactly 180° wide and the duty cycle would be 50%) with a phase difference of exactly 90° between *A* and *B* signals. In real encoders, however, due to sensor imperfections and speed variations, the pulse widths are never exactly 180° and the phase difference is never exactly 90°. Furthermore, the *A* and *B* pulse widths vary from one cycle to another (and from each other) and the phase difference varies at every *A* and *B* signal edge. Consequently, both the pulse width and phase difference will vary over a range of values.

For any particular encoder, the pulse width and phase difference ranges are defined by "symmetry" and "phase" (or "phasing") specifications, respectively. For example, in the case of an encoder with symmetry specified as 180° ±25°, the width of every output pulse is guaranteed to be at least 155° and no more than 205°. Similarly, with phase specified as 90° ±20°, the phase difference at every *A* or *B* edge will be at least 70° and no more than 110°.

## Signal types

Incremental encoders employ various types of electronic circuits to drive (transmit) their output signals, and manufacturers often have the ability to build a particular encoder model with any of several driver types. Commonly available driver types include open collector, mechanical, push-pull and differential RS-422.

### Open collector

Open collector drivers (using an NPN transistor or open drain drivers using an n-type MOSFET) allow operation over a wide range of signal voltages and often can sink significant output current, making them useful for directly driving current loops, opto-isolators and fiber optic transmitters.

Because it cannot source current, the output of an open-collector driver must be connected to a positive DC voltage through a pull-up resistor. Some encoders provide an internal resistor for this purpose; others do not and thus require an external pull-up resistor. In the latter case, the resistor typically is located near the encoder interface to improve noise immunity.

The encoder's high-level logic signal voltage is determined by the voltage applied to the pull-up resistor (*VOH* in the schematic), whereas the low-level output current is determined by both the signal voltage and load resistance (including pull-up resistor). When the driver switches from the low to the high logic level, the load resistance and circuit capacitance act together to form a low-pass filter, which stretches (increases) the signal's rise time and thus limits its maximum switching frequency.

### Mechanical

Mechanical (or *contact*) incremental encoders use sliding electrical contacts to directly generate the *A* and *B* output signals. Typically, the contacts are electrically connected to signal ground when closed so that the outputs will be "driven" low, effectively making them mechanical equivalents of open collector drivers and therefore subject to the same signal conditioning requirements (i.e. external pull-up resistor).

The maximum output frequency is limited by the same factors that affect open-collector outputs, and further limited by contact bounce (which must be filtered) and by the operating speed of the mechanical contacts, thus making these devices impractical for high frequency operation. Furthermore, the contacts experience mechanical wear under normal operation, which limits the life of these devices. On the other hand, mechanical encoders may be relatively inexpensive and have no internal, active electronics. These attributes make mechanical encoders a good fit for hand-operated controls (e.g. volume controls in audio equipment and voltage controls in bench power supplies) and a variety of other low duty, low frequency applications.

### Push-pull

Push-pull outputs (e.g., TTL) typically are used for direct interface to logic circuitry. These are well-suited to applications in which the encoder and interface are located near each other (e.g., interconnected via printed circuit conductors or short, shielded cable runs) and powered from a common power supply, thus avoiding exposure to electric fields, ground loops and transmission line effects that might corrupt the signals and thereby disrupt position tracking, or worse, damage the encoder interface.

### Differential pair

Differential RS-422 signaling is typically preferred when the encoder will output high frequencies or be located far away from the encoder interface, or when the encoder signals may be subjected to electric fields or common-mode voltages, or when the interface must be able to detect connectivity problems between encoder and interface. Examples of this include CMMs and CNC machinery, industrial robotics, factory automation, and motion platforms used in aircraft and spacecraft simulators.

When RS-422 outputs are employed, the encoder provides a differential conductor pair for every logic output; for example, "A" and "/A" are commonly used designations for the active-high and active-low differential pair comprising the encoder's *A* logic output. Consequently, the encoder interface must provide RS-422 line receivers to convert the incoming RS-422 pairs to single-ended logic.

## Principal applications

### Position tracking

Incremental encoders are commonly used to monitor the physical positions of mechanical devices. The incremental encoder is mechanically attached to the device to be monitored so that its output signals will change as the device moves. Example devices include the balls in mechanical computer mice and trackballs, control knobs in electronic equipment, and rotating shafts in radar antennas.

- (Trackballs and electromechanical computer mice employ two rotary incremental encoders to facilitate position tracking on two axes)Trackballs and electromechanical computer mice employ two rotary incremental encoders to facilitate position tracking on two axes
- (Electronic equipment controls are often implemented with a knob attached to a mechanical encoder (shown with detached knob))Electronic equipment controls are often implemented with a knob attached to a mechanical encoder (shown with detached knob)
- (In commercial marine radar antennas, a rotary incremental encoder is typically attached to the rotating antenna shaft to monitor the antenna angle)In commercial marine radar antennas, a rotary incremental encoder is typically attached to the rotating antenna shaft to monitor the antenna angle
- (The location of a pipeline video inspection tractor is typically monitored by a rotary incremental encoder attached to the tractor's cable reel)The location of a pipeline video inspection tractor is typically monitored by a rotary incremental encoder attached to the tractor's cable reel

An incremental encoder does not keep track of, nor do its outputs indicate the current encoder position; it only reports incremental changes in position. Consequently, to determine the encoder's position at any particular moment, it is necessary to provide external electronics which will "track" the position. This external circuitry, which is known as an incremental encoder interface, tracks position by counting incremental position changes.

As it receives each report of incremental position change (indicated by a transition of the *A* or *B* signal), an encoder interface will take into account the phase relationship between *A* and *B* and, depending on the sign of the phase difference, count up or down. The cumulative "counts" value indicates the distance traveled since tracking began. This mechanism ensures accurate position tracking in bidirectional applications and, in unidirectional applications, prevents false counts that would otherwise result from vibration or mechanical dithering near an AB code transition.

#### Displacement units

Often the encoder counts must be expressed in units such as meters, miles or revolutions. In such cases, the counts are converted to the desired units by multiplying by the ratio of encoder displacement D per count C :

$position=counts\times {\frac {D}{C}}$

.

Typically this calculation is performed by a computer which reads the counts from the incremental encoder interface. For example, in the case of a linear incremental encoder that produces 8000 counts per millimeter of travel, the position in millimeters is calculated as follows:

$mm=counts\times {\frac {\text{1 mm}}{\text{8000 counts}}}$

.

#### Homing

In order for an incremental encoder interface to track and report absolute position, the encoder counts must be correlated to a reference position in the mechanical system to which the encoder is attached. This is commonly done by *homing* the system, which consists of moving the mechanical system (and encoder) until it aligns with a reference position, and then jamming the associated absolute position counts into the encoder interface's counter.

A proximity sensor is built into some mechanical systems to facilitate homing, which outputs a signal when the mechanical system is in its "home" (reference) position. In such cases, the mechanical system is homed by moving it until the encoder interface receives the sensor signal, whereupon the corresponding position value is jammed into the position counter.

In some rotating mechanical systems (e.g. rotating radar antennas), the "position" of interest is the rotational angle relative to a reference orientation. These typically employ a rotary incremental encoder that has an *index* (or *Z*) output signal. The *index* signal is asserted when the shaft is in its reference orientation, which causes the encoder interface to jam the reference angle into its position counter.

Some incremental encoder applications lack reference position detectors and therefore must implement homing by other means. For example a computer, when using a mouse or trackball pointing device, typically will home the device by assuming a central, initial screen position upon booting, and jam the corresponding counts into the X and Y position counters. In the case of panel encoders used as hand-operated controls (e.g., audio volume control), the initial position typically is retrieved from flash or other non-volatile memory upon power-up and jammed into the position counter, and upon power-down the current position count is saved to non-volatile memory to serve as the initial position for the next power-up.

### Speed measurement

Incremental encoders are commonly used to measure the speed of mechanical systems. This may be done for monitoring purposes or to provide feedback for motion control, or both. Widespread applications of this include speed control of radar antenna rotation and material conveyors, and motion control in robotics, CMM and CNC machines.

Incremental encoder interfaces are primarily concerned with tracking mechanical displacement and usually do not directly measure speed. Consequently, speed must be indirectly measured by taking the derivative of the position with respect to time. The position signal is inherently quantized, which poses challenges for taking the derivative due to quantization error, especially at low speeds.

Encoder speed can be determined either by counting or by timing the encoder output pulses (or edges). The resulting value indicates a frequency or period, respectively, from which speed can be calculated. The speed is proportional to frequency, and inversely proportional to period.

#### By frequency

If the position signal is sampled (a discrete time signal), the pulses (or pulse edges) are detected and counted by the interface, and speed is typically calculated by a computer which has read access to the interface. To do this, the computer reads the position counts $C_{0}$ from the interface at time $T_{0}$ and then, at some later time $T_{1}$ reads the counts again to obtain $C_{1}$ . The average speed during the interval $T_{0}$ to $T_{1}$ is then calculated:

$speed={\frac {(C_{1}-C_{0})}{(T_{1}-T_{0})}}$

.

The resulting speed value is expressed as counts per unit time (e.g., counts per second). In practice, however, it is often necessary to express the speed in standardized units such as meters per second, revolutions per minute (RPM), or miles per hour (MPH). In such cases, the software will take into account the relationship between counts and desired distance units, as well as the ratio of the sampling period to desired time units. For example, in the case of a rotary incremental encoder that produces 4096 counts per revolution, which is being read once per second, the software would compute RPM as follows:

$RPM={\frac {(C_{1}-C_{0})}{\text{1 second}}}\times {\frac {\text{60 seconds}}{\text{1 minute}}}\times {\frac {\text{1 revolution}}{\text{4096 counts}}}$

.

When measuring speed this way, the measurement resolution is proportional to both the encoder resolution and the sampling period (the elapsed time between the two samples); measurement resolution will become higher as the sampling period increases.

#### By period

Alternatively, a speed measurement can be reported at each encoder output pulse by measuring the pulse width or period. When this method is used, measurements are triggered at specific positions instead of at specific times. The speed calculation is the same as shown above (counts / time), although in this case the measurement start and stop times ( $T_{0}$ and $T_{1}$ ) are provided by a time reference.

This technique avoids position quantization error but introduces errors related to quantization of the time reference. Also, it is more sensitive to sensor non-idealities such as phase errors, symmetry errors, and variations in the transition locations from their nominal values.

## Incremental encoder interface

An **incremental encoder interface** is an electronic circuit that receives signals from an incremental encoder, processes the signals to produce absolute position and other information, and makes the resulting information available to external circuitry.

Incremental encoder interfaces are implemented in a variety of ways, including as ASICs, as IP blocks within FPGAs, as dedicated peripheral interfaces in microcontrollers, or as software (via interrupts or polling GPIOs).

Regardless of the implementation, the interface must sample the encoder's *A* and *B* output signals frequently enough to detect every AB state change before the next state change occurs. Upon detecting a state change, it will increment or decrement the position counts based on whether *A* leads or trails *B*. This is typically done by storing a copy of the previous AB state and, upon state change, using the current and previous AB states to determine movement direction.

### Line receivers

Incremental encoder interfaces use various types of electronic circuits to receive encoder-generated signals. These line receivers serve as buffers to protect downstream interface circuitry and, in many cases, also provide signal conditioning functions.

#### Single-ended

Incremental encoder interfaces typically employ Schmitt trigger inputs to receive signals from encoders that have single-ended (e.g., push-pull, open collector) outputs. This type of line receiver inherently rejects low-level noise (by means of its input hysteresis) and protects downstream circuitry from invalid (and possibly destructive) logic signal levels.

#### Differential

RS-422 line receivers are commonly used to receive signals from encoders that have differential outputs. This type of receiver rejects common-mode noise and converts the incoming differential signals to the single-ended form required by downstream logic circuits.

In mission-critical systems, an encoder interface may be required to detect loss of input signals due to encoder power loss, signal driver failure, cable fault or cable disconnect. This is usually accomplished by using enhanced RS-422 line receivers which detect the absence of valid input signals and report this condition via a "signal lost" status output. In normal operation, glitches (brief pulses) may appear on the status outputs during input state transitions; typically, the encoder interface will filter the status signals to prevent these glitches from being erroneously interpreted as lost signals. Depending on the interface, subsequent processing may include generating an interrupt request upon detecting signal loss, and sending notification to the application for error logging or failure analysis.

### Clock synchronization

An incremental encoder interface largely consists of sequential logic which is paced by a clock signal. However, the incoming encoder signals are asynchronous with respect to the interface clock because their timing is determined solely by encoder movement. Consequently, the output signals from the *A* and *B* (also *Z* and *alarm*, if used) line receivers must be synchronized to the interface clock, both to avoid errors due to metastability and to coerce the signals into the clock domain of the quadrature decoder.

Typically this synchronization is performed by independent, single-signal synchronizers such as the two flip-flop synchronizer seen here. At very high clock frequencies, or when a very low error rate is needed, the synchronizers may include additional flip-flops in order to achieve an acceptably low bit error rate.

### Input filter

In many cases an encoder interface must filter the synchronized encoder signals before further processing them. This may be required in order to reject low-level noise and brief, large-amplitude noise spikes commonly found in motor applications and, in the case of mechanical-type encoders, to debounce *A* and *B* to avoid count errors due to mechanical contact bounce.

Hardware-based interfaces often provide programmable filters for the encoder signals, which provide a wide range of filter settings and thus allow them to debounce contacts or suppress transients resulting from noise or slowly slewing signals, as needed. In software-based interfaces, *A* and *B* typically are connected to GPIOs that are sampled (via polling or edge interrupts) and debounced by software.

### Quadrature decoder

Incremental encoder interfaces commonly use a **quadrature decoder** to convert the *A* and *B* signals into the *direction* and *count enable* (clock enable) signals needed for controlling a bidirectional (up- and down-counting) synchronous counter.

Typically, a quadrature decoder is implemented as a finite-state machine (FSM) which simultaneously samples the *A* and *B* signals and thus produces amalgamate "AB" samples. As each new AB sample is acquired, the FSM will store the previous AB sample for later analysis. The FSM evaluates the differences between the new and previous AB states and generates *direction* and *count enable* signals as appropriate for the detected AB state sequence.

| Description | AB state | Outputs |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Previous | Current | CE | DIR | ERR |   |   |   |
| x1 | x2 | x4 |   |   |   |   |   |
| Moved one increment in "forward" direction (*A* leads *B*) | 00 | 10 | 1 | 1 | 1 | 1 | 0 |
| 10 | 11 | 0 | 0 |   |   |   |   |
| 11 | 01 | 1 |   |   |   |   |   |
| 01 | 00 | 0 |   |   |   |   |   |
| Moved one increment in "reverse" direction (*B* leads *A*) | 00 | 01 | 0 | 0 |   |   |   |
| 01 | 11 | 1 |   |   |   |   |   |
| 11 | 10 | 0 |   |   |   |   |   |
| 10 | 00 | 1 | 1 |   |   |   |   |
| No detected movement | 00 | 00 | 0 | X |   |   |   |
| 01 | 01 |   |   |   |   |   |   |
| 10 | 10 |   |   |   |   |   |   |
| 11 | 11 |   |   |   |   |   |   |
| Moved an indeterminate number of increments | 00 | 11 | 1 |   |   |   |   |
| 01 | 10 |   |   |   |   |   |   |
| 10 | 01 |   |   |   |   |   |   |
| 11 | 00 |   |   |   |   |   |   |

#### State transitions

In any two consecutive AB samples, the logic level of *A* or *B* may change or both levels may remain unchanged, but in normal operation *A* and *B* will never both change. In this regard, each AB sample is effectively a two-bit Gray code.

- (Movement in forward direction)Movement in forward direction
- (Movement in reverse direction)Movement in reverse direction
- (No movement)No movement
- (Error)Error

##### Normal transitions

When only *A* or *B* changes state, it is assumed that the encoder has moved one increment of its measurement resolution and, accordingly, the quadrature decoder will assert its *count enable* output to allow the counts to change. Depending on the encoder's direction of travel (forward or reverse), the decoder will assert or negate its *direction* output to cause the counts to increment or decrement (or vice versa).

When neither *A* nor *B* changes, it is assumed that the encoder has not moved and so the quadrature decoder negates its *count enable* output, thereby causing the counts to remain unchanged.

##### Errors

If both the *A* and *B* logic states change in consecutive AB samples, the quadrature decoder has no way of determining how many increments, or in what direction the encoder has moved. This can happen if the encoder speed is too fast for the decoder to process (i.e., the rate of AB state changes exceeds the quadrature decoder's sampling rate; see Nyquist rate) or if the *A* or *B* signal is noisy.

In many encoder applications this is a catastrophic event because the counter no longer provides an accurate indication of encoder position. Consequently, quadrature decoders often will output an additional *error* signal which is asserted when the *A* and *B* states change simultaneously. Due to the severity and time-sensitive nature of this condition, the *error* signal is often connected to an interrupt request.

#### Clock multiplier

A quadrature decoder does not necessarily allow the counts to change for every incremental position change. When a decoder detects an incremental position change (due to a transition of *A* or *B*, but not both), it may allow the counts to change or it may inhibit counting, depending on the AB state transition and the decoder's *clock multiplier*.

The clock multiplier of a quadrature decoder is so named because it results in a count rate which is a multiple of the *A* or *B* pulse frequency. Depending on the decoder's design, the clock multiplier may be hardwired into the design or it may be run-time configurable via input signals.

The clock multiplier value may be one, two or four (typically designated "x1", "x2" and "x4", or "1x", "2x" and "4x"). In the case of a x4 multiplier, the counts will change for every AB state change, thereby resulting in a count rate equal to four times the *A* or *B* frequency. The x2 and x1 multipliers allow the counts to change on some, but not all AB state changes, as shown in the quadrature decoder state table above (note: this table shows one of several possible implementations for x2 and x1 multipliers; other implementations may enable counting at different AB transitions).

### Position reporting

From an application's perspective, the fundamental purpose of an incremental encoder interface is to report position information on demand. Depending on the application, this may be as simple as allowing the computer to read the position counter at any time under program control. In more complex systems, the position counter may be sampled and processed by intermediate state machines, which in turn make the samples available to the computer.

#### Sample register

An encoder interface typically employs a sample register to facilitate position reporting. In the simple case where the computer demands position information under program control, the interface will sample the position counter (i.e., copy the current position counts to the sample register) and then the computer will read the counts from the sample register. This mechanism results in atomic operation and thus ensures the integrity of the sample data, which might otherwise be at risk (e.g., if the sample's word size exceeds the computer's word size).

#### Triggered sampling

In some cases the computer may not be able to programmatically (via programmed I/O) acquire position information with adequate timing precision. For example, the computer may be unable to demand samples on a timely periodic schedule (e.g., for speed measurement) due to software timing variability. Also, in some applications it is necessary to demand samples upon the occurrence of external events, and the computer may be unable to do so in a timely manner. At higher encoder speeds and resolutions, position measurement errors can occur even when interrupts are used to demand samples, because the encoder may move between the time the IRQ is signaled and the sample demand is issued by the interrupt handler.

To overcome this limitation, it is common for an incremental encoder interface to implement hardware-triggered sampling, which enables it to sample the position counter at precisely controlled times as dictated by a trigger input signal. This is important when the position must be sampled at particular times or in response to physical events, and essential in applications such as multi-axis motion control and CMM, in which the position counters of multiple encoder interfaces (one per axis) must be simultaneously sampled.

In many applications the computer must know precisely when each sample was acquired and, if the interface has multiple trigger inputs, which signal triggered the sample acquisition. To satisfy these requirements, the interface typically will include a timestamp and trigger information in every sample.

##### Event notification

Sampling triggers are often asynchronous with respect to software execution. Consequently, when the position counter is sampled in response to a trigger signal, the computer must be notified (typically via interrupt) that a sample is available. This allows the software to be event-driven (vs. polled), which facilitates responsive system behavior and eliminates polling overhead.

##### Sample FIFO

Consecutive sampling triggers may occur faster than the computer can process the resulting samples. When this happens, the information in the sample register will be overwritten before it can be read by the computer, resulting in data loss. To avoid this problem, some incremental encoder interfaces provide a FIFO buffer for samples. As each sample is acquired, it is stored in the FIFO. When the computer demands a sample, it is allowed to read the oldest sample in the FIFO.
