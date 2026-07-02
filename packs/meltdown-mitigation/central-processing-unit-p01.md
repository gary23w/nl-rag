---
title: "Central processing unit (part 1/2)"
source: https://en.wikipedia.org/wiki/Central_processing_unit
domain: meltdown-mitigation
license: CC-BY-SA-4.0
tags: meltdown mitigation, kernel page table isolation, out of order execution defense, transient execution defense
fetched: 2026-07-02
part: 1/2
---

# Central processing unit

A **central processing unit** (**CPU**), also known as a **central processor**, **main processor**, or simply **processor**, is the primary processor in a given computer. Its electronic circuitry executes instructions of a computer program, such as arithmetic, logic, controlling, and input/output (I/O) operations. This role contrasts with that of external components, such as main memory and I/O circuitry, and specialized coprocessors such as graphics processing units (GPUs).

The form, design, and implementation of CPUs have changed over time, but their fundamental operation remains almost unchanged. Principal components of a CPU include the arithmetic–logic unit (ALU) that performs arithmetic and logic operations, processor registers that supply operands to the ALU and store the results of ALU operations, and a control unit that orchestrates the fetching (from memory), decoding and execution (of instructions) by directing the coordinated operations of the ALU, registers, and other components. Modern CPUs devote a lot of semiconductor area to caches and instruction-level parallelism to increase performance and to CPU modes to support operating systems and virtualization.

Most modern CPUs are implemented on integrated circuit (IC) microprocessors, with one or more CPUs on a single IC chip. Microprocessor chips with multiple CPUs are called *multi-core processors* (*MCPs*). The individual physical CPUs, called *processor cores*, can also be multithreaded to support CPU-level multithreading.

An IC that contains a CPU may also contain memory, peripheral interfaces, and other components of a computer; such integrated devices are variously called microcontrollers or systems on chip (SoCs).


## History

Early computers such as the ENIAC had to be physically rewired to perform different tasks, which caused these machines to be called "fixed-program computers". The "central processing unit" term has been in use since as early as 1955. Since the term "CPU" is generally defined as a device for software (computer program) execution, the earliest devices that could rightly be called CPUs came with the advent of the stored-program computer.

The idea of a stored-program computer had already been present in the design of John Presper Eckert and John William Mauchly's ENIAC, but was initially omitted so that it could be finished sooner. On June 30, 1945, before ENIAC was made, mathematician John von Neumann distributed a paper entitled *First Draft of a Report on the EDVAC*. It was the outline of a stored-program computer that would eventually be completed in August 1949. EDVAC was designed to perform a certain number of instructions (or operations) of various types. Significantly, the programs written for EDVAC were to be stored in high-speed computer memory rather than specified by the physical wiring of the computer. This overcame a severe limitation of ENIAC, which was the considerable time and effort required to reconfigure the computer to perform a new task. With von Neumann's design, the program that EDVAC ran could be changed simply by changing the contents of the memory. EDVAC was not the first stored-program computer; the Manchester Baby, which was a small-scale experimental stored-program computer, ran its first program on 21 June 1948 and the Manchester Mark 1 ran its first program during the night of 16–17 June 1949.

Early CPUs were custom designs used as part of a larger and sometimes distinctive computer. However, this method of designing custom CPUs for a particular application has largely given way to the development of multi-purpose processors produced in large quantities. This standardization began in the era of discrete transistor mainframes and minicomputers, and has rapidly accelerated with the popularization of the integrated circuit (IC). The IC has allowed increasingly complex CPUs to be designed and manufactured to tolerances on the order of nanometers. Both the miniaturization and standardization of CPUs have increased the presence of digital devices in modern life far beyond the limited application of dedicated computing machines. Modern microprocessors appear in electronic devices ranging from automobiles to cellphones, and sometimes even in toys.

While von Neumann is most often credited with the design of the stored-program computer because of his design of EDVAC, and the design became known as the von Neumann architecture, others before him, such as Konrad Zuse, had suggested and implemented similar ideas. The so-called Harvard architecture of the Harvard Mark I, which was completed before EDVAC, also used a stored-program design using punched paper tape rather than electronic memory. The key difference between the two is that Harvard architecture separates the storage and treatment of CPU instructions and data, whereas von Neumann architecture uses the same memory space for both. Most modern CPUs are primarily von Neumann in design, but CPUs with the Harvard architecture are seen as well, especially in embedded applications; for instance, the Atmel AVR microcontrollers are Harvard-architecture processors.

Prior to the invention of the transistor, relays and vacuum tubes (thermionic tubes) were commonly used as switching elements; a useful computer requires thousands or tens of thousands of switching devices. The overall speed of a system is dependent on the speed of the switches. Vacuum-tube computers such as EDVAC tended to average eight hours between failures, whereas relay computers—such as the slower but earlier Harvard Mark I—failed very rarely. In the end, tube-based CPUs became dominant because the significant speed advantages afforded generally outweighed the reliability problems. Most of these early synchronous CPUs ran at low clock rates compared to modern microelectronic designs. Clock signal frequencies ranging from 100 kHz to 4 MHz were very common at this time, limited largely by the speed of the switching devices they were built with.

### Transistor CPUs

The design complexity of CPUs increased as various technologies facilitated the building of smaller and more reliable electronic devices. The first such improvement came with the advent of the transistor. Transistorized CPUs during the 1950s and 1960s no longer had to be built out of bulky, unreliable, and fragile switching elements, like vacuum tubes and relays. With this improvement, more complex and reliable CPUs were built onto one or several printed circuit boards containing discrete (individual) components.

In 1964, IBM introduced its IBM System/360 computer architecture that was used in a series of computers capable of running the same programs with different speeds and performances. This was significant at a time when most electronic computers were incompatible with one another, even those made by the same manufacturer. To facilitate this improvement, IBM used the concept of a microprogram (often called "microcode"), which still sees widespread use in modern CPUs. The System/360 architecture was so popular that it dominated the mainframe computer market for decades and left a legacy that is continued by similar modern computers like the IBM zSeries. In 1965, Digital Equipment Corporation (DEC) introduced another influential computer aimed at the scientific and research markets—the PDP-8.

Transistor-based computers had several distinct advantages over their predecessors. Aside from facilitating increased reliability and lower power consumption, transistors also allowed CPUs to operate at much higher speeds because of the short switching time of a transistor in comparison to a tube or relay. The increased reliability and dramatically increased speed of the switching elements, which were almost exclusively transistors by this time; CPU clock rates in the tens of megahertz were easily obtained during this period. Additionally, while discrete transistor and IC CPUs were in heavy usage, new high-performance designs like single instruction, multiple data (SIMD) vector processors began to appear. These early experimental designs later gave rise to the era of specialized supercomputers like those made by Cray Inc and Fujitsu Ltd.

### Small-scale integration CPUs

During this period, a method of manufacturing many interconnected transistors in a compact space was developed. The integrated circuit (IC) allowed a large number of transistors to be manufactured on a single semiconductor-based die, or "chip". At first, only very basic non-specialized digital circuits such as NOR gates were miniaturized into ICs. CPUs based on these "building block" ICs are generally referred to as "small-scale integration" (SSI) devices. SSI ICs, such as the ones used in the Apollo Guidance Computer, usually contained up to a few dozen transistors. To build an entire CPU out of SSI ICs required thousands of individual chips, but still consumed much less space and power than earlier discrete transistor designs.

IBM's System/370, follow-on to the System/360, used SSI ICs rather than Solid Logic Technology discrete-transistor modules. DEC's PDP-8/I and KI10 PDP-10 also switched from the individual transistors used by the PDP-8 and KA PDP-10 to SSI ICs, and their extremely popular PDP-11 line was originally built with SSI ICs, but was eventually implemented with LSI components once these became practical.

### Large-scale integration CPUs

Lee Boysel published influential articles, including a 1967 "manifesto", which described how to build the equivalent of a 32-bit mainframe computer from a relatively small number of large-scale integration circuits (LSI). The only way to build LSI chips, which are chips with a hundred or more gates, was to build them using a metal–oxide–semiconductor (MOS) semiconductor manufacturing process (either PMOS logic, NMOS logic, or CMOS logic). However, some companies continued to build processors out of bipolar transistor–transistor logic (TTL) chips because bipolar junction transistors were faster than MOS chips up until the 1970s (a few companies such as Datapoint continued to build processors out of TTL chips until the early 1980s). In the 1960s, MOS ICs were slower and initially considered useful only in applications that required low power. Following the development of silicon-gate MOS technology by Federico Faggin at Fairchild Semiconductor in 1968, MOS ICs largely replaced bipolar TTL as the standard chip technology in the late 1970s.

As the microelectronic technology advanced, an increasing number of transistors were placed on ICs, decreasing the number of individual ICs needed for a complete CPU. MSI and LSI ICs increased transistor counts to hundreds, and then thousands. By 1968, the number of ICs required to build a complete CPU had been reduced to 24 ICs of eight different types, with each IC containing roughly 1000 MOSFETs. In stark contrast with its SSI and MSI predecessors, the first LSI implementation of the PDP-11 contained a CPU composed of only four LSI integrated circuits.

### Microprocessors

Die

of an

Intel 80486DX2

microprocessor (actual size: 12 × 6.75 mm) in its packaging

Intel

Core i5 CPU on a

Vaio E series

laptop motherboard (on the right, beneath the

heat pipe

)

Since microprocessors were first introduced they have almost completely overtaken all other central processing unit implementation methods. The first commercially available microprocessor, made in 1971, was the Intel 4004. The Intel 4004 was one of the first consumer-facing CPUs integrating arithmetic logic unit, control unit, and register unit on a chip. The first widely used microprocessor, made in 1974, was the Intel 8080. Mainframe and minicomputer manufacturers of the time launched proprietary IC development programs to upgrade their older computer architectures, and eventually produced instruction set compatible microprocessors that were backward-compatible with their older hardware and software. Combined with the advent and eventual success of the ubiquitous personal computer, the term *CPU* is now applied almost exclusively to microprocessors. Several CPUs (denoted *cores*) can be combined in a single processing chip.

Previous generations of CPUs were implemented as discrete components and numerous small integrated circuits (ICs) on one or more circuit boards. Microprocessors, on the other hand, are CPUs manufactured on a very small number of ICs; usually just one. The overall smaller CPU size, as a result of being implemented on a single die, means faster switching time because of physical factors like decreased gate parasitic capacitance. This has allowed synchronous microprocessors to have clock rates ranging from tens of megahertz to several gigahertz. Additionally, the ability to construct exceedingly small transistors on an IC has increased the complexity and number of transistors in a single CPU many fold. This widely observed trend is described by Moore's law, which had proven to be a fairly accurate predictor of the growth of CPU (and other IC) complexity until 2016.

While the complexity, size, construction and general form of CPUs have changed enormously since 1950, the basic design and function has not changed much at all. Almost all common CPUs today can be very accurately described as von Neumann stored-program machines. As Moore's law no longer holds, concerns have arisen about the limits of integrated circuit transistor technology. Extreme miniaturization of electronic gates is causing the effects of phenomena like electromigration and subthreshold leakage to become much more significant. These newer concerns are among the many factors causing researchers to investigate new methods of computing such as the quantum computer, as well as to expand the use of parallelism and other methods that extend the usefulness of the classical von Neumann model.


## Operation

The fundamental operation of most CPUs, regardless of the physical form they take, is to execute a sequence of stored instructions that is called a program. The instructions to be executed are kept in some kind of computer memory. Nearly all CPUs follow the fetch, decode and execute steps in their operation, which are collectively known as the instruction cycle.

After the execution of an instruction, the entire process repeats, with the next instruction cycle normally fetching the next-in-sequence instruction because of the incremented value in the program counter. If a jump instruction was executed, the program counter will be modified to contain the address of the instruction that was jumped to and program execution continues normally. In more complex CPUs, multiple instructions can be fetched, decoded and executed simultaneously. This section describes what is generally referred to as the "classic RISC pipeline", which is quite common among the simple CPUs used in many electronic devices (often called microcontrollers). It largely ignores the important role of CPU cache, and therefore the access stage of the pipeline.

Some instructions manipulate the program counter rather than producing result data directly; such instructions are generally called "jumps" and facilitate program behavior like loops, conditional program execution (through the use of a conditional jump), and existence of functions. In some processors, some other instructions change the state of bits in a "flags" register. These flags can be used to influence how a program behaves, since they often indicate the outcome of various operations. For example, in such processors a "compare" instruction evaluates two values and sets or clears bits in the flags register to indicate which one is greater or whether they are equal; one of these flags could then be used by a later jump instruction to determine program flow.

### Fetch

Fetch involves retrieving an instruction (which is represented by a number or sequence of numbers) from program memory. The instruction's location (address) in program memory is determined by the program counter (PC; called the "instruction pointer" in Intel x86 microprocessors), which stores a number that identifies the address of the next instruction to be fetched. After an instruction is fetched, the PC is incremented by the length of the instruction so that it will contain the address of the next instruction in the sequence. Often, the instruction to be fetched must be retrieved from relatively slow memory, causing the CPU to stall while waiting for the instruction to be returned. This issue is largely addressed in modern processors by caches and pipeline architectures (see below).

### Decode

The instruction that the CPU fetches from memory determines what the CPU will do. In the decode step, performed by binary decoder circuitry known as the *instruction decoder*, the instruction is converted into signals that control other parts of the CPU.

The way in which the instruction is interpreted is defined by the CPU's instruction set architecture (ISA). Often, one group of bits (that is, a "field") within the instruction, called the opcode, indicates which operation is to be performed, while the remaining fields usually provide supplemental information required for the operation, such as the operands. Those operands may be specified as a constant value (called an immediate value), or as the location of a value that may be a processor register or a memory address, as determined by some addressing mode.

In some CPU designs, the instruction decoder is implemented as a hardwired, unchangeable binary decoder circuit. In others, a microprogram is used to translate instructions into sets of CPU configuration signals that are applied sequentially over multiple clock pulses. In some cases the memory that stores the microprogram is rewritable, making it possible to change the way in which the CPU decodes instructions.

### Execute

After the fetch and decode steps, the execute step is performed. Depending on the CPU architecture, this may consist of a single action or a sequence of actions. During each action, control signals electrically enable or disable various parts of the CPU so they can perform all or part of the desired operation. The action is then completed, typically in response to a clock pulse. Very often the results are written to an internal CPU register for quick access by subsequent instructions. In other cases results may be written to slower, but less expensive and higher capacity main memory.

For example, if an instruction that performs addition is to be executed, registers containing operands (numbers to be summed) are activated, as are the parts of the arithmetic logic unit (ALU) that perform addition. When the clock pulse occurs, the operands flow from the source registers into the ALU, and the sum appears at its output. On subsequent clock pulses, other components are enabled (and disabled) to move the output (the sum of the operation) to storage (e.g., a register or memory). If the resulting sum is too large (i.e., it is larger than the ALU's output word size), an arithmetic overflow flag will be set, influencing the next operation.
