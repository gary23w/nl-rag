---
title: "Combinational logic"
source: https://en.wikipedia.org/wiki/Combinational_logic
domain: boolean-circuit
license: CC-BY-SA-4.0
tags: boolean circuit, logic gate network, circuit satisfiability, monotone circuit
fetched: 2026-07-02
---

# Combinational logic

Classes of automata

In automata theory, **combinational logic** (also referred to as **time-independent logic**) is a type of digital logic that is implemented by Boolean circuits, where the output is a pure function of the present input only. This is in contrast to sequential logic, in which the output depends not only on the present input but also on the history of the input. In other words, sequential logic has *memory* while combinational logic does not.

Combinational logic is used in computer circuits to perform Boolean algebra on input signals and on stored data. Practical computer circuits normally contain a mixture of combinational and sequential logic. For example, the part of an arithmetic logic unit, or ALU, that does mathematical calculations is constructed using combinational logic. Other circuits used in computers, such as half adders, full adders, half subtractors, full subtractors, multiplexers, demultiplexers, encoders and decoders are also made by using combinational logic.

Practical design of combinational logic systems may require consideration of the finite time required for practical logical elements to react to changes in their inputs. Where an output is the result of the combination of several different paths with differing numbers of switching elements, the output may momentarily change state before settling at the final state, as the changes propagate along different paths.

## Representation

Combinational logic is used to build circuits that produce specified outputs from certain inputs. The construction of combinational logic is generally done using one of two methods: a sum of products, or a product of sums. Consider the following truth table, which represents a 3-input combinatorial logic element taking inputs A, B, and C, and with an output which is true only when both input A is true, and inputs B and C are either both true or both false.

| A | B | C | Result | Logical equivalent |
|---|---|---|---|---|
| F | F | F | F | $\neg A\wedge \neg B\wedge \neg C$ |
| F | F | T | F | $\neg A\wedge \neg B\wedge C$ |
| F | T | F | F | $\neg A\wedge B\wedge \neg C$ |
| F | T | T | F | $\neg A\wedge B\wedge C$ |
| T | F | F | T | $A\wedge \neg B\wedge \neg C$ |
| T | F | T | F | $A\wedge \neg B\wedge C$ |
| T | T | F | F | $A\wedge B\wedge \neg C$ |
| T | T | T | T | $A\wedge B\wedge C$ |

Using sum of products, all logical statements which yield true results are summed, giving the result:

$(A\wedge \neg B\wedge \neg C)\vee (A\wedge B\wedge C)\,$

Using Boolean algebra, the result simplifies to the following equivalent of the truth table:

$A\wedge ((\neg B\wedge \neg C)\vee (B\wedge C))\,$

## Logic formula minimization

Minimization (simplification) of combinational logic formulas is done using the following rules based on the laws of Boolean algebra:

${\begin{aligned}(A\vee B)\wedge (A\vee C)&=A\vee (B\wedge C)\\(A\wedge B)\vee (A\wedge C)&=A\wedge (B\vee C)\end{aligned}}$

${\begin{aligned}A\vee (A\wedge B)&=A\\A\wedge (A\vee B)&=A\end{aligned}}$

${\begin{aligned}A\vee (\lnot A\wedge B)&=A\vee B\\A\wedge (\lnot A\vee B)&=A\wedge B\end{aligned}}$

${\begin{aligned}(A\vee B)\wedge (\lnot A\vee B)&=B\\(A\wedge B)\vee (\lnot A\wedge B)&=B\end{aligned}}$

${\begin{aligned}(A\wedge B)\vee (\lnot A\wedge C)\vee (B\wedge C)&=(A\wedge B)\vee (\lnot A\wedge C)\\(A\vee B)\wedge (\lnot A\vee C)\wedge (B\vee C)&=(A\vee B)\wedge (\lnot A\vee C)\end{aligned}}$

With the use of minimization (sometimes called logic optimization), a simplified logical function or circuit may be arrived upon, and the logic combinational circuit becomes smaller, and easier to analyse, use, or build.
