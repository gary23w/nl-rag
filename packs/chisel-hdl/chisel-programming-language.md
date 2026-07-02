---
title: "Chisel (programming language)"
source: https://en.wikipedia.org/wiki/Chisel_(programming_language)
domain: chisel-hdl
license: CC-BY-SA-4.0
tags: chisel hardware language, scala hardware, risc-v cores, rtl generation
fetched: 2026-07-02
---

# Chisel (programming language)

**Chisel** (an acronym for **Constructing Hardware in a Scala Embedded Language**) is an open-source hardware description language (HDL) used to describe digital electronics and circuits at the register-transfer level.

Chisel is based on Scala as a domain-specific language (DSL). Chisel inherits the object-oriented and functional programming aspects of Scala for describing digital hardware. Using Scala as a basis allows describing circuit generators. High quality, free access documentation exists in several languages.

Circuits described in Chisel can be converted to a description in Verilog for synthesis and simulation.

## Code examples

A simple example describing an adder circuit and showing the organization of components in Module with input and output ports:

```mw
class Add extends Module {
  val io = IO(new Bundle {
    val a = Input(UInt(8.W))
    val b = Input(UInt(8.W))
    val y = Output(UInt(8.W))
  })

  io.y := io.a + io.b
}
```

A 32-bit register with a reset value of 0:

```mw
val reg = RegInit(0.U(32.W))
```

A multiplexer is part of the Chisel library:

```mw
val result = Mux(sel, a, b)
```

## Use

Although Chisel is not yet a mainstream hardware description language, it has been explored by several companies and institutions. The most prominent use of Chisel is an implementation of the RISC-V instruction set, the open-source Rocket chip. Chisel is mentioned by the Defense Advanced Research Projects Agency (DARPA) as a technology to improve the efficiency of electronic design, where smaller design teams do larger designs. Google has used Chisel to develop a Tensor Processing Unit for edge computing. Some developers prefer Chisel as it requires one-fifth as much code and is much faster to develop than Verilog.

Circuits described in Chisel can be converted to a description in Verilog for synthesis and simulation using a program named FIRRTL.
