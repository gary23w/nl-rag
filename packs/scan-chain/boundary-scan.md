---
title: "Boundary scan"
source: https://en.wikipedia.org/wiki/Boundary_scan
domain: scan-chain
license: CC-BY-SA-4.0
tags: scan chain, scan flip-flop, boundary scan, jtag test access
fetched: 2026-07-02
---

# Boundary scan

**Boundary scan** is a method for testing interconnects (wire lines) on printed circuit boards or sub-blocks inside an integrated circuit (IC). Boundary scan is also widely used as a debugging method to watch integrated circuit pin states, measure voltage, or analyze sub-blocks inside an integrated circuit.

The Joint Test Action Group (JTAG) developed a specification for boundary scan testing that was standardized in 1990 as the IEEE Std. 1149.1-1990. In 1994, a supplement that contains a description of the boundary scan description language (BSDL) was added which describes the boundary-scan logic content of IEEE Std 1149.1 compliant devices. Since then, this standard has been adopted by electronic device companies all over the world. Boundary scan is now mostly synonymous with JTAG.

## Testing

The boundary scan architecture provides a means to test interconnects (including clusters of logic, memories, etc.) without using physical test probes; this involves the addition of at least one *test cell* that is connected to each pin of the device and that can selectively override the functionality of that pin. Each test cell may be programmed via the JTAG scan chain to drive a signal onto a pin and thus across an individual trace on the board; the cell at the destination of the board trace can then be read, verifying that the board trace properly connects the two pins. If the trace is shorted to another signal or if the trace is open, the correct signal value does not show up at the destination pin, indicating a fault.

### On-chip infrastructure

To provide the boundary scan capability, IC vendors add additional logic to each of their devices, including *scan cells* for each of the external traces. These cells are then connected together to form the external boundary scan shift register (BSR), and combined with JTAG Test Access Port (TAP) controller support comprising four (or sometimes more) additional pins plus control circuitry.

Some TAP controllers support scan chains between on-chip logical design blocks, with JTAG instructions which operate on those internal scan chains instead of the BSR. This can allow those integrated components to be tested as if they were separate chips on a board. On-chip debugging solutions are heavy users of such internal scan chains.

These designs are part of most Verilog or VHDL libraries. Overhead for this additional logic is minimal, and generally is well worth the price to enable efficient testing at the board level.

For normal operation, the added boundary scan latch cells are set so that they have no effect on the circuit, and are therefore effectively invisible. However, when the circuit is set into a test mode, the latches enable a data stream to be shifted from one latch into the next. Once a complete data word has been shifted into the circuit under test, it can be latched into place so it drives external signals. Shifting the word also generally returns the input values from the signals configured as inputs.

### Test mechanism

As the cells can be used to force data into the board, they can set up test conditions. The relevant states can then be fed back into the test system by clocking the data word back so that it can be analyzed.

By adopting this technique, it is possible for a test system to gain test access to a board. As most of today's boards are very densely populated with components and tracks, it is very difficult for test systems to physically access the relevant areas of the board to enable them to test the board. Boundary scan makes access possible without always needing physical probes.

In modern chip and board design, design for test is a significant issue, and one common design artifact is a set of boundary scan test vectors, possibly delivered in Serial Vector Format (SVF) or a similar interchange format.

### JTAG test operations

Devices communicate to the world via a set of input and output pins. By themselves, these pins provide limited visibility into the workings of the device. However, devices that support boundary scan contain a shift-register cell for each signal pin of the device. These registers are connected in a dedicated path around the device's boundary (hence the name). The path creates a virtual access capability that circumvents the normal inputs and provides direct control of the device and detailed visibility at its outputs. The contents of the boundary scan are usually described by the manufacturer using a part-specific BSDL file.

Among other things, a BSDL file will describe each digital signal exposed through pin or ball (depending on the chip packaging) exposed in the boundary scan, as part of its definition of the Boundary Scan Register (BSR). A description for two balls might look like this:

```mw
   "541 (bc_1,                     *,  control,  1)," &
   "542 (bc_1,         GPIO51_ATACS1,  output3,  X,    541,   1,   Z)," &
   "543 (bc_1,         GPIO51_ATACS1,    input,  X)," &
   "544 (bc_1,                     *,  control,  1)," &
   "545 (bc_1,         GPIO50_ATACS0,  output3,  X,    544,   1,   Z)," &
   "546 (bc_1,         GPIO50_ATACS0,    input,  X)," &
```

That shows two balls on a mid-size chip (the boundary scan includes about 620 such lines, in a 361-ball BGA package), each of which has three components in the BSR: a control configuring the ball (as input, output, what drive level, pullups, pulldowns, and so on); one type of output signal; and one type of input signal.

There are JTAG instructions to SAMPLE the data in that boundary scan register, or PRELOAD it with values.

During testing, I/O signals enter and leave the chip through the boundary-scan cells. Testing involves a number of test vectors, each of which drives some signals and then verifies that the responses are as expected. The boundary-scan cells can be configured to support external testing for interconnection between chips (EXTEST instruction) or internal testing for logic within the chip (INTEST instruction).

### Board test infrastructure

Typically high-end commercial JTAG testing systems allow the import of design 'netlists' from CAD/EDA systems plus the BSDL models of boundary scan/JTAG compliant devices to automatically generate test applications. Common types of test include

- Scan-path 'infrastructure' or integrity
- Boundary-scan device pin to boundary-scan device pin 'interconnect'
- Boundary-scan pin to memory device or device cluster (SRAM, DRAM, DDR etc.)
- Arbitrary logic cluster testing

When used during manufacturing, such systems also support non-test but affiliated applications such as in-system programming of various types of flash memory: NOR, NAND, and serial (I2C or SPI).

Such commercial systems are used by board test professionals and will often cost several thousand dollars for a fully-fledged system. They can include diagnostic options to accurately pin-point faults such as open circuits and shorts and may also offer schematic or layout viewers to depict the fault in a graphical manner. Tests developed with such tools are frequently combined with other test systems such as in-circuit testers (ICTs) or functional board test systems.

## Debugging

The boundary scan architecture also provides functionality which helps developers and engineers during development stages of an embedded system. A JTAG Test Access Port (TAP) can be turned into a low-speed logic analyzer.

## History

James B. Angell at Stanford University proposed serial testing.

IBM developed level-sensitive scan design (LSSD).
