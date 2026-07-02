---
title: "Register-transfer level"
source: https://en.wikipedia.org/wiki/Register-transfer_level
domain: systemverilog
license: CC-BY-SA-4.0
tags: systemverilog language, hardware verification language, rtl verification, hardware description language
fetched: 2026-07-02
---

# Register-transfer level

In digital circuit design, **register-transfer level** (**RTL**) is a design abstraction which models a synchronous digital circuit in terms of the flow of digital signals (data) between hardware registers, and the logical operations performed on those signals.

Register-transfer-level abstraction is used in hardware description languages (HDLs) like Verilog and VHDL to create high-level representations of a circuit, from which lower-level representations and ultimately actual wiring can be derived. Design at the RTL level is typical practice in modern digital design.

Unlike in software compiler design, where the register-transfer level is an intermediate representation and at the lowest level, the RTL level is the usual input that circuit designers operate on. In circuit synthesis, an intermediate language between the input register transfer level representation and the target netlist is sometimes used. Unlike in netlist, constructs such as cells, functions, and multi-bit registers are available. Examples include FIRRTL and RTLIL.

Transaction-level modeling is a higher level of electronic system design.

## RTL description

A synchronous circuit consists of two kinds of elements: registers (sequential logic) and combinational logic. Registers (usually implemented as D flip-flops) synchronize the circuit's operation to the edges of the clock signal, and are the only elements in the circuit that have memory properties. Combinational logic performs all the logical functions in the circuit and it typically consists of logic gates.

For example, a very simple synchronous circuit is shown in the figure. The inverter is connected from the output, Q, of a register to the register's input, D, to create a circuit that changes its state on each rising edge of the clock, clk. In this circuit, the combinational logic consists of the inverter.

When designing digital integrated circuits with a hardware description language (HDL), the designs are usually engineered at a higher level of abstraction than transistor level (logic families) or logic gate level. In HDLs the designer declares the registers (which roughly correspond to variables in computer programming languages), and describes the combinational logic by using constructs that are familiar from programming languages such as if-then-else and arithmetic operations. This level is called *register-transfer level*. The term refers to the fact that RTL focuses on describing the flow of signals between registers.

As an example, the circuit mentioned above can be described in VHDL as follows:

```mw
D <= not Q;
 
process(clk)
begin
    if rising_edge(clk) then
        Q <=  D;
    end if;
end process;
```

Using an EDA tool for synthesis, this description can usually be directly translated to an equivalent hardware implementation file for an ASIC or an FPGA. The synthesis tool also performs logic optimization.

At the register-transfer level, some types of circuits can be recognized. If there is a cyclic path of logic from a register's output to its input (or from a set of registers outputs to its inputs), the circuit is called a state machine or can be said to be sequential logic. If there are logic paths from a register to another without a cycle, it is called a pipeline.

## RTL in the circuit design cycle

RTL is used in the logic design phase of the integrated circuit design cycle.

An RTL description is usually converted to a gate-level description of the circuit by a logic synthesis tool. The synthesis results are then used by placement and routing tools to create a physical layout.

Logic simulation tools may use a design's RTL description to verify its correctness.

## Power estimation techniques for RTL

The most accurate power analysis tools are available for the circuit level but unfortunately, even with switch- rather than device-level modelling, tools at the circuit level have disadvantages like they are either too slow or require too much memory thus inhibiting large chip handling. The majority of these are simulators like SPICE and have been used by the designers for many years as performance analysis tools. Due to these disadvantages, gate-level power estimation tools have begun to gain some acceptance where faster, probabilistic techniques have begun to gain a foothold. But it also has its trade off as speedup is achieved on the cost of accuracy, especially in the presence of correlated signals. Over the years it has been realized that biggest wins in low power design cannot come from circuit- and gate-level optimizations whereas architecture, system, and algorithm optimizations tend to have the largest impact on power consumption. Therefore, there has been a shift in the incline of the tool developers towards high-level analysis and optimization tools for power.

### Motivation

It is well known that more significant power reductions are possible if optimizations are made on levels of abstraction, like the architectural and algorithmic level, which are higher than the circuit or gate level This provides the required motivation for the developers to focus on the development of new architectural level power analysis tools. This in no way implies that lower level tools are unimportant. Instead, each layer of tools provides a foundation upon which the next level can be built. The abstractions of the estimation techniques at a lower level can be used on a higher level with slight modifications.

### Advantages of doing power estimation at RTL or architectural level

- Designers use a register-transfer level (RTL) description of the design to make optimizations and trade-offs very early in the design flow.
- The presence of functional blocks in an RTL description makes the complexity of architectural design much more manageable even for large chips because RTL has granularity sufficiently larger than gate- or circuit-level descriptions.

### Gate equivalents

Source:

It is a technique based on the concept of gate equivalents. The complexity of a chip architecture can be described approximately in terms of gate equivalents where gate equivalent count specifies the average number of reference gates that are required to implement the particular function. The total power required for the particular function is estimated by multiplying the approximated number of gate equivalents with the average power consumed per gate. The reference gate can be any gate e.g. 2-input NAND gate.

#### Examples of gate equivalent technique

- **Class-independent power modeling:** It is a technique which tries to estimate chip area, speed, and power dissipation based on information about the complexity of the design in terms of gate equivalents. The functionality is divided among different blocks but no distinction is made about the functionality of the blocks i.e. it is basically class independent. This is the technique used by the *chip estimation system* (CES).

Steps:

1. Identify the functional blocks such as counters, decoders, multipliers, memories, etc.
2. Assign a complexity in terms of gate equivalents. The number of GE’s for each unit type are either taken directly as an input from the user or are fed from a library.

$\displaystyle P=\sum _{i\in {\text{fns}}}{\textit {GE}}_{i}(E_{\text{typ}}+C_{L}^{i}V_{\text{dd}}^{2})fA_{\text{int}}^{i}$

Where E

typ

is the assumed average dissipated energy by a gate equivalent, when active. The activity factor, A

int

, denotes the average percentage of gates switching per clock cycle and is allowed to vary from function to function. The capacitive load, C

L

, is a combination of fan-out loading as well as wiring. An estimate of the average wire length can be used to calculate the wiring capacitance. This is provided by the user and cross-checked by using a derivative of

Rent’s rule

.

Assumptions:

1. A single reference gate is taken as the basis for all the power estimates not taking into consideration different circuit styles, clocking strategies, or layout techniques.
2. The percentage of gates switching per clock cycle denoted by activity factors are assumed to be fixed regardless of the input patterns.
3. Typical gate switching energy is characterized by completely random uniform white noise (UWN) distribution of the input data. This implies that the power estimation is same regardless of the circuit being idle or at maximum load as this UWN model ignores how different input distributions affect the power consumption of gates and modules.

- **Class-dependent power modeling:** This approach is slightly better than the previous approach as it takes into account customized estimation techniques to the different types of functional blocks thus trying to increase the modelling accuracy which wasn't the case in the previous technique such as logic, memory, interconnect, and clock hence the name. The power estimation is done in a very similar manner to the independent case. The basic switching energy is based on a three-input AND gate and is calculated from technology parameters e.g. gate width, tox, and metal width provided by the user.

$P_{\text{bitlines}}={\dfrac {N_{\text{col}}}{2}}\cdot (L_{\text{col}}C_{\text{wire}}+N_{\text{row}}C_{\text{cell}})V_{\text{dd}}V_{\text{swing}}$

Where C

wire

denotes the bit line wiring capacitance per unit length and C

cell

denotes the loading due to a single cell hanging off the bit line. The clock capacitance is based on the assumption of an

H-tree

distribution network. Activity is modelled using a UWN model. As can be seen by the equation the power consumption of each components is related to the number of columns (N

col

) and rows (N

row

) in the memory array.

Disadvantages:

1. The circuit activities are not modeled accurately as an overall activity factor is assumed for the entire chip which is also not trustable as provided by the user. As a matter of fact activity factors will vary throughout the chip hence this is not very accurate and prone to error. This leads to the problem that even if the model gives a correct estimate for the total power consumption by the chip, the module wise power distribution is fairly inaccurate.
2. The chosen activity factor gives the correct total power, but the breakdown of power into logic, clock, memory, etc. is less accurate. Therefore this tool is not much different or improved in comparison with CES.

### Precharacterized cell libraries

This technique further customizes the power estimation of various functional blocks by having separate power model for logic, memory, and interconnect suggesting a power factor approximation (PFA) method for individually characterizing an entire library of functional blocks such as multipliers, adders, etc. instead of a single gate-equivalent model for “logic” blocks. The power over the entire chip is approximated by the expression:

$\displaystyle P=\sum _{i\in {\text{all blocks}}}K_{i}G_{i}f_{i}$

Where Ki is PFA proportionality constant that characterizes the ith functional element $G_{i}$ is the measure of hardware complexity, and $f_{i}$ denotes the activation frequency.

#### Example

Gi denoting the hardware complexity of the multiplier is related to the square of the input word length i.e. N2 where N is the word length. The activation frequency is the rate at which multiplies are performed by the algorithm denoted by $f_{mult}$ and the PFA constant, $K_{mult}$ , is extracted empirically from past multiplier designs and shown to be about 15 fW/bit2-Hz for a 1.2 μm technology at 5V. The resulting power model for the multiplier on the basis of the above assumptions is:

$\displaystyle P_{\text{mult}}=K_{\text{mult}}N^{2}f_{\text{mult}}$

**Advantages:**

- Customization is possible in terms of whatever complexity parameters which are appropriate for that block. E.g. for a multiplier the square of the word length was appropriate. For memory, the storage capacity in bits is used and for the I/O drivers the word length alone is adequate.

**Weakness:**

- There is the implicit assumption that the inputs do not affect the multiplier activity which is contradictory to the fact that the PFA constant $K_{mult}$ is intended to capture the intrinsic internal activity associated with the multiply operation as it is taken to be a constant.

The estimation error (relative to switch-level simulation) for a 16x16 multiplier is experimented and it is observed that when the dynamic range of the inputs does not fully occupy the word length of the multiplier, the UWN model becomes extremely inaccurate. Granted, good designers attempt to maximize word length utilization. Still, errors in the range of 50-100% are not uncommon. The figure clearly suggests a flaw in the UWN model.
