---
title: "Shift register"
source: https://en.wikipedia.org/wiki/Shift_register
domain: gpio-expanders
license: CC-BY-SA-4.0
tags: general-purpose input output, shift register, serial peripheral interface, port expander
fetched: 2026-07-02
---

# Shift register

A **shift register** is a type of digital circuit using a cascade of flip-flops where the output of one flip-flop is connected to the input of the next. They share a single clock signal, which causes the data stored in the system to shift from one location to the next. By connecting the last flip-flop back to the first, the data can cycle within the shifters for extended periods, and in this configuration they were used as computer memory, displacing delay-line memory systems in the late 1960s and early 1970s.

In most cases, several parallel shift registers would be used to build a larger memory pool known as a "bit array". Data was stored into the array and read back out in parallel, often as a computer word, while each bit was stored serially in the shift registers. There is an inherent trade-off in the design of bit arrays; putting more flip-flops in a row allows a single shifter to store more bits, but requires more clock cycles to push the data through all of the shifters before the data can be read back out again.

Shift registers can have both parallel and serial inputs and outputs. These are often configured as "serial-in, parallel-out" (SIPO) or as "parallel-in, serial-out" (PISO). There are also types that have both serial and parallel input and types with serial and parallel output. There are also "bidirectional" shift registers, which allow shifting in both directions: L → R or R → L. The serial input and serial output of a shift register are connected to create a **circular shift register**. A PIPO register (parallel in, parallel out) is simply a D-type register and is *not* a shift register, but is very fast – an output is given within a single clock pulse. A "universal" shift register provides bidirectional serial-in and serial-out, as well as parallel-in and parallel-out.

## Serial-in serial-out (SISO)

### Destructive readout

| Time | Output 1 | Output 2 | Output 3 | Output 4 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 1 | 0 | 0 |
| 3 | 1 | 0 | 1 | 0 |
| 4 | 1 | 1 | 0 | 1 |
| 5 | 0 | 1 | 1 | 0 |
| 6 | 0 | 0 | 1 | 1 |
| 7 | 0 | 0 | 0 | 1 |
| 8 | 0 | 0 | 0 | 0 |

These are the simplest kind of shift registers. The data string is presented at "data in" and is shifted right one stage each time "data advance" is brought high. At each advance, the bit on the far left (i.e. "data in") is shifted into the first flip-flop's output. The bit on the far right (i.e. "data out") is shifted out and lost.

The data is stored after each on the "Q" output, so there are four storage "slots" available in this arrangement, hence it is a 4-bit register. To give an idea of the shifting pattern, imagine that the register holds 0000 (so all storage slots are empty). As "data in" presents 1,0,1,1,0,0,0,0 (in that order, with a pulse at "data advance" each time—this is called clocking or strobing) to the register, this is the result. The right hand column corresponds to the right-most flip-flop's output pin, and so on.

So the serial output of the entire value is 00010110. It can be seen that if data were to be continued to input, it would get exactly what was put in (10110000), but offset by four "data advance" cycles. This arrangement is the hardware equivalent of a queue. Also, at any time, the whole register can be set to zero by bringing the reset (R) pins high.

This arrangement performs *destructive readout* – each datum is lost once it has been shifted out of the right-most bit.

## Serial-in parallel-out (SIPO)

This configuration allows conversion from serial to parallel format. Data input is serial, as described in the SISO section above. Once the data has been clocked in, it may be either read off at each output simultaneously, or it can be shifted out.

In this configuration, each flip-flop is edge triggered. All flip-flops operate at the given clock frequency. Each input bit makes its way down to the Nth output after N clock cycles, leading to parallel output.

In cases where the parallel outputs should not change during the serial loading process, it's desirable to use a latched or buffered output. In a latched shift register (such as the 74595) the serial data is first loaded into an internal buffer register, then upon receipt of a load signal the state of the buffer register is copied into a set of output registers. In general, the practical application of the serial-in/parallel-out shift register is to convert data from serial format on a single wire to parallel format on multiple wires.

## Parallel-in serial-out (PISO)

This configuration has the data input on lines D1 through D4 in parallel format, D1 being the most significant bit. To write the data to the register, the Write/Shift control line must be held LOW. To shift the data, the W/S control line is brought HIGH and the registers are clocked. The arrangement now acts as a PISO shift register, with D1 as the Data Input. However, as long as the number of clock cycles is not more than the length of the data-string, the Data Output, Q, will be the parallel data read off in order.

The animation below shows the write/shift sequence, including the internal state of the shift register.

## Uses

### Serial and parallel conversion

One of the most common uses of a shift register is to convert between serial and parallel interfaces.

### Delay

Serial-in serial-out shift registers can be used as simple delay circuits.

### Stack

Several bidirectional shift registers can also be connected in parallel for a hardware implementation of a stack.

### More I/O pins

Shift registers are commonly attached to microcontrollers when more general-purpose input/output pins are required than are available, sometimes over a Serial Peripheral Interface in daisy chain configuration, which allows any number of binary devices to be accessed using only two to four pins, though more slowly than parallel I/O.

For more outputs, SIPO shift registers are used. The parallel outputs of the shift register and the desired state for all those devices can be sent out of the microcontroller using a single serial connection.

For more inputs, PISO shift registers are used. Each binary input (such as a button or more complicated circuitry) is attached to a parallel input of the shift register, then the data is sent back serially to the microcontroller.

### Pulse extenders

Shift registers can also be used as pulse extenders. Compared to monostable multivibrators, the timing does not depend on component values, but it requires an external clock, and the timing accuracy is limited by the granularity of this clock. An example of such a pulse extender is the Ronja Twister, wherein five 74164 shift registers create the core of the timing logic this way (schematic).

### Data processing

In early computers, shift registers were used to handle data processing: two numbers to be added were stored in two shift registers and clocked out into an arithmetic and logic unit (ALU) with the result being fed back to the input of one of the shift registers (the accumulator), which was one bit longer, since binary addition can only result in an answer that has the same size or is one bit longer.

### Bitshift operations

Many computer languages include bitwise operations to "shift right" and "shift left" the data in a register, effectively dividing by two or multiplying by two for each place shifted.

### Shift register memory

Very large serial-in serial-out shift registers (thousands of bits in size) were used in a similar manner to the earlier delay-line memory in some devices built in the early 1970s. Shift registers don't need many pins or address decoding logic, so was much cheaper than random-access memory back then. Such *shift register memory* was sometimes called *circulating memory*.

Datapoint 3300, for example, stored its terminal display of 25 rows of 72 columns of 6-bit upper-case characters using 54 200-bit shift registers (arranged in 6 tracks of 9 packs), providing storage for 1800 characters. The shift register design meant that scrolling the terminal display could be accomplished by simply pausing the display output to skip one line of characters. A similar design was used for the Apple I's terminal.

## History

One of the first known examples of a shift register was in the Mark 2 Colossus, a code-breaking machine built in 1944. It was a six-stage device built of vacuum tubes and thyratrons. A shift register was also used in the IAS machine, built by John von Neumann and others at the Institute for Advanced Study in the late 1940s. Shift registers made their way into integrated circuits in the 1960s as evidenced by early patents from Frank Wanlass and Kent Smith working at General Instrument.
