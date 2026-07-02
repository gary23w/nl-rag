---
title: "Successive-approximation ADC"
source: https://en.wikipedia.org/wiki/Successive-approximation_ADC
domain: analog-to-digital-conversion
license: CC-BY-SA-4.0
tags: analog-to-digital converter, successive approximation, flash ADC, effective number of bits
fetched: 2026-07-02
---

# Successive-approximation ADC

A **successive-approximation ADC** (or **SAR ADC**) is a type of analog-to-digital converter (ADC) that digitizes each sample from a continuous analog waveform using a binary search through all possible quantization levels.

## History

The SAR ADC was first used for experimental pulse-code modulation (PCM) by Bell Labs in the 1940s. In 1954, Bernard Gordon introduced the first commercial vacuum tube SAR ADC, converting 50,000 11-bit samples per second.

## Algorithm

Drummer and Ray described the algorithm as applied to a digital voltmeter. This paper predates ADC integrated circuits but describes the binary search decision-making.

The successive-approximation analog-to-digital converter circuit typically contains four chief subcircuits:

1. A sample-and-hold circuit that acquires the input voltage *V*in.
2. An analog voltage comparator that compares *V*in to the output of a digital-to-analog converter (DAC).
3. A successive-approximation register that is updated by the results of the comparator to provide the DAC with a digital code whose accuracy increases with each successive iteration.
4. A DAC that supplies the comparator with an analog voltage relative to the reference voltage *V*ref (which corresponds to the full-scale range of the ADC) and proportional to the digital code of the SAR.

The successive-approximation register is initialized with 1 in the most significant bit (MSB) and zeroes in the lower bits. The register's code is fed into the DAC, which provides an analog equivalent of its digital code (initially ⁠1/2⁠*V*ref) to the comparator for comparison with the sampled input voltage. If this analog voltage exceeds *V*in, then the comparator causes the SAR to reset this bit; otherwise, the bit is left as 1. Then the next bit is set to 1, and the same test is done, continuing this binary search until every bit in the SAR has been tested. The resulting code is the digital approximated output of the sampled input voltage.

The algorithm's objective for the *n*th iteration is to approximately digitize the input voltage to an accuracy of 1⁄2*n* relative to the reference voltage. To show this mathematically, the normalized input voltage is represented as *x* in [−1, 1] by letting *V*in = *xV*ref. The algorithm starts with an initial approximation of *x*0 = 0 and during each iteration *i* produces the following approximation:

> *i*th approximation: *x**i* = *x**i*−1 − ⁠*sgn*(*x**i*−1 − *x*)/2*i*⁠

where the binary signum function *sgn* mathematically represents the comparison of the previous iteration's approximation *x*i-1 with the normalized input voltage *x*: $sgn(x_{i-1}-x)={\begin{cases}+1&{\text{if }}x_{i-1}\geq x,\\-1&{\text{if }}x_{i-1}<x.\end{cases}}$ It follows using mathematical induction that the approximation of the *n*th iteration theoretically has a bounded accuracy of: |*x**n* − *x*| ≤ ⁠1/2*n*⁠.

### Inaccuracies in non-ideal analog circuits

When implemented as a real analog circuit, circuit inaccuracies and noise may cause the binary search algorithm to incorrectly remove values it believes *V*in cannot be, so a successive-approximation ADC might not output the closest value. It is very important for the DAC to accurately produce all 2*n* analog values for comparison against the unknown *V*in in order to produce a best match estimate. The maximal error can easily exceed several LSBs, especially as the error between the actual and ideal 2*n* becomes large. Manufacturers may characterize the accuracy using an effective number of bits (ENOB) smaller than the actual number of output bits.

As of 2001, the component-matching limitations of the DAC generally limited the linearity to about 12 bits in practical designs and mandated some form of trimming or calibration to achieve the necessary linearity for more than 12 bits. And since kT/C noise is inversely proportional to capacitance, low noise demands a large input capacitance (which costs chip area and requires a more powerful drive buffer), which has motivated proposals around noise cancellation. For comparison, for a *V*ref of 5 V, the least significant bit of a 16-bit converter corresponds to 76 μV, which is around the 64 μVrms noise of a 1 pF (large for on-chip) capacitor at room temperature. As of 2012, SAR ADCs are limited to 18 bits, while delta-sigma ADCs (which can be 24 bits) are better suited if more than 16 bits are needed. SAR ADCs are commonly found on microcontrollers because they are easy to integrate into a mixed-signal process, but suffer from inaccuracies from the internal reference voltage resistor ladder and clock and signal noise from the rest of the microcontroller, so external ADC chips may provide better accuracy.

Calibration of the element weights allows for greater accuracy, but generally, some redundancy is then required.

### Examples

**Example 1:** The steps to converting an analog input to 9-bit digital, using successive-approximation, are shown here for all voltages from 5 V to 0 V in 0.1 V iterations. Since the reference voltage is 5 V, when the input voltage is also 5 V, all bits are set. As the voltage is decreased to 4.9 V, only some of the least significant bits are cleared. The MSB will remain set until the input is one half the reference voltage, 2.5 V.

The binary weights assigned to each bit, starting with the MSB, are 2.5, 1.25, 0.625, 0.3125, 0.15625, 0.078125, 0.0390625, 0.01953125, 0.009765625. All of these add up to 4.990234375, meaning binary 111111111, or one LSB less than 5.

When the analog input is being compared to the internal DAC output, it effectively is being compared to each of these binary weights, starting with the 2.5 V and either keeping it or clearing it as a result. Then by adding the next weight to the previous result, comparing again, and repeating until all the bits and their weights have been compared to the input, the result, a binary number representing the analog input, is found.

**Example 2:** The working of a 4-bit successive-approximation ADC is illustrated below. The MSB is initially set to 1, whereas the remaining digits are set to zero. If the input voltage is lower than the value stored in the register, on the next clock cycle, the register changes its value to that illustrated in the figure by following the green line. If the input voltage is higher, then on the next clock cycle, the register changes its value to that illustrated in the figure by following the red line. The simplified structure of this type of ADC that acts on 2*n* volts range can be expressed as an algorithm:

1. Initialize register with MSB set to 1 and all other values set to zero.
2. In the nth clock cycle, if voltage is higher than digital equivalent voltage of the number in register, the (n+1)th digit from the left is set to 1. If the voltage were lower than digital equivalent voltage, then nth digit from left is set to zero and the next digit is set to 1. To perform a conversion, an N-bit ADC requires N such clock cycles, excluding the initial state.

Working of successive approximation ADC

Setup where output values of the ADC are arranged in a grid, with the vertical axis corresponding to voltage. It is a 4-bit ADC that measures input voltages from 0V to 15V.

Previously established setup where an input voltage of 10.4V is provided.

Previously established setup where an input voltage of 9.4V is provided.

The successive-approximation ADC can be alternatively explained by first uniformly assigning each digital output to corresponding ranges, as shown. It can be seen that the algorithm essentially divides the voltage range into two regions and checks which of the two regions the input voltage belongs to. Successive steps involve taking the identified region from before and further dividing the region into two, and continuing identification. This occurs until all possible choices of digital representations are exhausted, leaving behind an identified region that corresponds to only one of the digital representations.

## Charge-redistribution successive-approximation ADC

One of the earliest descriptions of this approach using only MOS transistors is "A capacitive charge redistribution A/D converter" .

This uses a charge-scaling DAC consisting of an array of individually-switched capacitors sized in powers of two and an additional duplicate of the smallest capacitor, for a total of *N*+1 capacitors for *N* bits. Thus if the largest capacitance is *C*, then the array's total capacitance is 2*C*. The switched capacitor array acts as both the sample-and-hold element and the DAC. Redistributing their charge will adjust their net voltage, which is fed into the negative input of a comparator (whose positive input is always grounded) to perform the binary search using the following steps:

1. Discharge: The capacitors are discharged. Discharging to the comparator's offset voltage will automatically provide offset cancellation.
2. Sampling: The capacitors are switched to the input signal *V*in. After a brief sampling period, the capacitors will hold a charge equal to their respective capacitance times *V*in (and minus the offset voltage upon each of them), so the array holds a total charge of 2*C*·*V*in.
3. Hold: The capacitors are then switched to ground. This provides the comparator's negative input with a voltage of −*V*in.
4. Conversion: the actual conversion process proceeds with the following steps in each iteration, starting with the largest capacitor as the test capacitor for the MSB, and then testing each next smaller capacitor in order for each bit of lower significance:
  1. Redistribution: The current test capacitor is switched to *V*ref. The test capacitor forms a charge divider with the remainder of the array, whose ratio depends on the capacitor's relative size. In the first iteration, the ratio is 1:1, so the comparator's negative input becomes −*V*in + *V*ref⁄2. On the *i*th iteration, the ratio will be 1:2*i*−1, so the *i*th iteration of this redistribution step effectively adds *V*ref⁄2*i* to the voltage.
  2. Comparison: The comparator's output determines the bit's value for to the current test capacitor. In the first iteration, if *V*in is greater than *V*ref⁄2, then the comparator will output a digital 1 and otherwise output a digital 0.
  3. Update Switch: A digital 1 result will leave the current test capacitor connected to *V*ref for subsequent iterations, while a digital 0 result will switch the capacitor back to ground. Thus, each *i*th iteration may or may not add *V*ref⁄2*i* to the comparator's negative input voltage. For instance, the voltage at the end of the first iteration will be −*V*in + MSB·*V*ref⁄2.
5. End Of Conversion: After all capacitors are tested in the same manner, the comparator's negative input voltage will have converged as close as possible (given the resolution of the DAC) to the comparator's offset voltage.

Calibration

For any high-accuracy (10 bits or greater), the capacitors must be calibrated. The CS5015 from Crystal Semiconductor was self-calibrated on power-up. The patent describes the invention and calibration techniques.
