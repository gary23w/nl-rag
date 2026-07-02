---
title: "Fault injection"
source: https://en.wikipedia.org/wiki/Fault_injection
domain: mutation-testing
license: CC-BY-SA-4.0
tags: mutation testing, test effectiveness, fault injection, code coverage
fetched: 2026-07-02
---

# Fault injection

In computer science, **fault injection** is a testing technique for understanding how computing systems behave when stressed in unusual ways. This can be achieved using physical- or software-based means, or using a hybrid approach. Widely studied physical fault injections include the application of high voltages, extreme temperatures and electromagnetic pulses on electronic components, such as computer memory and central processing units. By exposing components to conditions beyond their intended operating limits, computing systems can be coerced into mis-executing instructions and corrupting critical data.

In software testing, fault injection is a technique for improving the coverage of a test by introducing faults to test code paths; in particular error handling code paths, that might otherwise rarely be followed. It is often used with stress testing and is widely considered to be an important part of developing robust software. Robustness testing (also known as syntax testing, fuzzing or fuzz testing) is a type of fault injection commonly used to test for vulnerabilities in communication interfaces such as protocols, command line parameters, or APIs.

The propagation of a fault through to an observable failure follows a well-defined cycle. When executed, a fault may cause an error, which is an invalid state within a system boundary. An error may cause further errors within the system boundary, therefore each new error acts as a fault, or it may propagate to the system boundary and be observable. When error states are observed at the system boundary they are termed failures. This mechanism is termed the fault-error-failure cycle and is a key mechanism in dependability.

## History

The technique of fault injection dates back to the 1970s when it was first used to induce faults at a hardware level. This type of fault injection is called Hardware Implemented Fault Injection (HWIFI) and attempts to simulate hardware failures within a system. The first experiments in hardware fault involved nothing more than shorting connections on circuit boards and observing the effect on the system (bridging faults). It was used primarily as a test of the dependability of the hardware system. Later specialised hardware was developed to extend this technique, such as devices to bombard specific areas of a circuit board with heavy radiation. It was soon found that faults could be induced by software techniques and that aspects of this technique could be useful for assessing software systems. Collectively these techniques are known as Software Implemented Fault Injection (SWIFI).

## Software implemented fault injection

SWIFI techniques can be categorized into two types: compile-time injection and runtime injection.

**Compile-time injection** is an injection technique where source code is modified to inject simulated faults into a system. One method is called mutation testing which changes existing lines of code so that they contain faults. A simple example of this technique could be changing `a = a + 1` to `a = a – 1`

Code mutation produces faults which are very similar to those unintentionally added by programmers.

A refinement of code mutation is *Code Insertion Fault Injection* which adds code, rather than modifying existing code. This is usually done through the use of perturbation functions which are simple functions which take an existing value and perturb it via some logic into another value, for example

```mw
int pFunc(int value) {
  return value + 20;
}

int main(int argc, char * argv[]) {
  int a = pFunc(aFunction(atoi(argv[1])));
  if (a > 20) {
    /* do something */
  } else {
    /* do something else */
  }
}
```

In this case, pFunc is the perturbation function and it is applied to the return value of the function that has been called introducing a fault into the system.

**Runtime Injection** techniques use a software trigger to inject a fault into a running software system. Faults can be injected via a number of physical methods and triggers can be implemented in a number of ways, such as: Time Based triggers (When the timer reaches a specified time an interrupt is generated and the interrupt handler associated with the timer can inject the fault. ); Interrupt Based Triggers (Hardware exceptions and software trap mechanisms are used to generate an interrupt at a specific place in the system code or on a particular event within the system, for instance, access to a specific memory location).

Runtime injection techniques can use a number of different techniques to insert faults into a system via a trigger.

- Corruption of memory space: This technique consists of corrupting RAM, processor registers, and I/O map.
- Syscall interposition techniques: This is concerned with the fault propagation from operating system kernel interfaces to executing systems software. This is done by intercepting operating system calls made by user-level software and injecting faults into them.
- Network Level fault injection: This technique is concerned with the corruption, loss or reordering of network packets at the network interface.

These techniques are often based around the debugging facilities provided by computer processor architectures.

### Protocol software fault injection

Complex software systems, especially multi-vendor distributed systems based on open standards, perform input/output operations to exchange data via stateful, structured exchanges known as "protocols." One kind of fault injection that is particularly useful to test protocol implementations (a type of software code that has the unusual characteristic in that it cannot predict or control its input) is fuzzing. Fuzzing is an especially useful form of Black-box testing since the various invalid inputs that are submitted to the software system do not depend on, and are not created based on knowledge of, the details of the code running inside the system.

## Hardware implemented fault injection

The hardware fault injection method consists in real electrical signals injection into the DUT (devices under testing) in order to disturb it, supposedly well working, at hardware low level, and deceive the control - detection chain (if present) in order to see how and if the fault management strategy is implemented.

This technique is based on a nail bed, necessary to contact the electronics of the products, where a specific test pad has been left free (Design for testability of PCB), and properly inject disturbance signals, in order to see the product's control- reaction arm's reaction if present.

It's a technique often used to certify and validate reaction to fault in high reliability products, where safety is involved (Military, Medical, Autonomous vehicle).

The proper low level physical injection is very critical, not only because the different types of signals should have different types of disturbance (voltage, coupling impedance etc.), but also a very appropriate timing when the disturbance shall be injected, to avoid serious damage to the DUT generation's dangerous short circuit.

Any single components present in the DUT (from dipole type resistor, capacitor, diode) to tripolar transistors, CMOS, ECC) up to complex chip (Low voltage converter, power unit, CPU, RAM, ECC), is susceptible to a fault method (short, open, drift ECC) that can be studied during a FMEDA analysis using statistical method (MIL HBK) and determine the most dangerous with a Functional safety approach (ISO 26262 A), then real test shall be executed on any permutation there considered risky.

Because of the wide complexity a dedicated and complex tools is necessary.

## Characteristics of fault injection

Faults have three main parameters.

- Type: What type of fault should be injected? For example stuck-to-value, delay, ignoring some functions, ignoring some parameters/variable, random faults, the bias fault, the noise, etc. The amplitude of each fault is also important.
- Time: When should be activated? For example the activation time of fault or the activation condition of fault.
- Location: Where should be in the system? For example fault in the link/connection between systems, faults within systems/subsystems/function, etc.

These parameters create the fault space realm. The fault space realm will increase exponentially by increasing system complexity. Therefore, the traditional fault injection method will not be applicable to use in the modern cyber-physical systems, because they will be so slow, and they will find a small number of faults (less fault coverage). Hence, the testers need an efficient algorithm to choose critical faults that have a higher impact on system behavior. Thus, the main research question is how to find critical faults in the fault space realm which have catastrophic effects on system behavior. Here are some methods that can aid fault injection to efficiently explore the fault space to reach higher fault coverage in less simulation time.

- Sensitivity analysis: In this method, sensitivity analysis has been used to identify the most important signals that have a higher impact on the system's specification. By identifying those important signals or parameters, the fault injection tool will focus on those effective signals instead of focusing on all signals in the system.
- Reinforcement learning: In this method, the reinforcement learning algorithm has been used to efficiently explore the fault space and find critical faults.

## Fault injection tools

Although these types of faults can be injected by hand the possibility of introducing an unintended fault is high, so tools exist to parse a program automatically and insert faults.

### Research tools

A number of SWIFI Tools have been developed and a selection of these tools is given here. Six commonly used fault injection tools are Ferrari, FTAPE, Doctor, Orchestra, Xception and Grid-FIT.

- MODIFI (MODel-Implemented Fault Injection) is a fault injection tool for robustness evaluation of Simulink behavior models. It supports fault modelling in XML for implementation of domain-specific fault models.
- Ferrari (Fault and ERRor Automatic Real-time Injection) is based around software traps that inject errors into a system. The traps are activated by either a call to a specific memory location or a timeout. When a trap is called the handler injects a fault into the system. The faults can either be transient or permanent. Research conducted with Ferrari shows that error detection is dependent on the fault type and where the fault is inserted.
- FTAPE (Fault Tolerance and Performance Evaluator) can inject faults, not only into memory and registers, but into disk accesses as well. This is achieved by inserting a special disk driver into the system that can inject faults into data sent and received from the disk unit. FTAPE also has a synthetic load unit that can simulate specific amounts of load for robustness testing purposes.
- DOCTOR (IntegrateD SOftware Fault InjeCTiOn EnviRonment) allows injection of memory and register faults, as well as network communication faults. It uses a combination of time-out, trap and code modification. Time-out triggers inject transient memory faults and traps inject transient emulated hardware failures, such as register corruption. Code modification is used to inject permanent faults.
- Orchestra is a script-driven fault injector that is based around Network Level Fault Injection. Its primary use is the evaluation and validation of the fault-tolerance and timing characteristics of distributed protocols. Orchestra was initially developed for the Mach Operating System and uses certain features of this platform to compensate for latencies introduced by the fault injector. It has also been successfully ported to other operating systems.
- Xception is designed to take advantage of the advanced debugging features available on many modern processors. It is written to require no modification of system source and no insertion of software traps, since the processor's exception handling capabilities trigger fault injection. These triggers are based around accesses to specific memory locations. Such accesses could be either for data or fetching instructions. It is therefore possible to accurately reproduce test runs because triggers can be tied to specific events, instead of timeouts.
- Grid-FIT (Grid – Fault Injection Technology) is a dependability assessment method and tool for assessing Grid services by fault injection. Grid-FIT is derived from an earlier fault injector WS-FIT which was targeted towards Java Web Services implemented using Apache Axis transport. Grid-FIT utilises a novel fault injection mechanism that allows network-level fault injection to be used to give a level of control similar to Code Insertion fault injection whilst being less invasive.
- LFI (Library-level Fault Injector) is an automatic testing tool suite, used to simulate in a controlled testing environment, exceptional situations that programs need to handle at runtime but that are not easy to check via input testing alone. LFI automatically identifies the errors exposed by shared libraries, finds potentially buggy error recovery code in program binaries and injects the desired faults at the boundary between shared libraries and applications.
- FIBlock (Fault Injection Block), a model-based fault injection method implemented as a highly-customizable Simulink block. It supports the injection in MATLAB Simulink models typical faults of essential heterogeneous components of Cyber-Physical Systems such as sensors, computing hardware, and network. Additional trigger inputs and outputs of the block enable the modeling of conditional faults. Furthermore, two or more FIBlocks connected with the trigger signals can model so-called chained errors.

### Commercial tools

- Novasom Industries Fault Injection HIL, it is a patented RT system composed by a nail bed specifically tailored on the PCBA to be tested, and an array of embedded computers. It is realized after a DTF (Design for testability) analysis on the DUT, and able to inject specific electrical fault. It can short on any test point of the DUT to ground as to a specific voltage with a 16 bit DAC, as read value in static or triggered mode up to 2 Ms. The systems can be driven by any customer software for test cases implementation (from vector to matlab) and allow a full hardware as software validation. This system is able to make thousands of test cases in minutes, it is totally unmanaged and real time. It allow customers to make real tests for ISO26262A and any critical safety analysis.
- Beyond Security beSTORM is a commercial black box software security analysis tool. It is often used during development by original equipment manufacturers but is also used for testing products prior to implementation, notably in aerospace, banking and defense. beSTORM's test process starts with the most likely attack scenarios, then resorts to exhaustive generation based fuzzing. beSTORM provides modules for common protocols and 'auto learns' new or proprietary protocols, including mutation-based attacks. Highlights: binary and textual analysis, custom protocol testing, debugging and stack tracing, development language independent, CVE compliant.
- ExhaustiF is a commercial software tool used for grey box testing based on software fault injection (SWIFI) to improve reliability of software-intensive systems. The tool can be used during system integration and system testing phases of any software development lifecycle, complementing other testing tools as well. ExhaustiF is able to inject faults into both software and hardware. When injecting simulated faults in software, ExhaustiF offers the following fault types: Variable Corruption and Procedure Corruption. The catalogue for hardware fault injections includes faults in Memory (I/O, RAM) and CPU (Integer Unit, Floating Unit). There are different versions available for RTEMS/ERC32, RTEMS/Pentium, Linux/Pentium and MS-Windows/Pentium.
- Holodeck is a test tool developed by Security Innovation that uses fault injection to simulate real-world application and system errors for Windows applications and services. Holodeck customers include many major commercial software development companies, including Microsoft, Symantec, EMC and Adobe. It provides a controlled, repeatable environment in which to analyze and debug error-handling code and application attack surfaces for fragility and security testing. It simulates file and network fuzzing faults as well as a wide range of other resource, system and custom-defined faults. It analyzes code and recommends test plans and also performs function call logging, API interception, stress testing, code coverage analysis and many other application security assurance functions.
- Proofdock's Chaos Engineering Platform has a focus on the Microsoft Azure cloud platform. It injects failures at the infrastructure level, platform level and application level.
- Gremlin is a "Failure-as-a-Service" platform that helps companies build more resilient systems through the practice of chaos engineering. Gremlin recreates the most common failures across three categories -- Resource, Network, and State—by safely injecting failure into systems in order to proactively identify and fix unknown faults.
- Codenomicon Defensics is a black-box test automation framework that does fault injection to more than 150 different interfaces including network protocols, API interfaces, files, and XML structures. The commercial product was launched in 2001, after five years of research at University of Oulu in the area of software fault injection. A thesis work explaining the used fuzzing principles was published by VTT, one of the PROTOS consortium members.
- The Mu Service Analyzer is a commercial service testing tool developed by Mu Dynamics. The Mu Service Analyzer performs black box and white box testing of services based on their exposed software interfaces, using denial-of-service simulations, service-level traffic variations (to generate invalid inputs) and the replay of known vulnerability triggers. All these techniques exercise input validation and error handling and are used in conjunction with valid protocol monitors and SNMP to characterize the effects of the test traffic on the software system. The Mu Service Analyzer allows users to establish and track system-level reliability, availability and security metrics for any exposed protocol implementation. The tool has been available in the market since 2005 by customers in North America, Asia and Europe, especially in the critical markets of network operators (and their vendors) and Industrial control systems (including Critical infrastructure).
- Xception is a commercial software tool developed by Critical Software SA used for black box and white box testing based on software fault injection (SWIFI) and Scan Chain fault injection (SCIFI). Xception allows users to test the robustness of their systems or just part of them, allowing both Software fault injection and Hardware fault injection for a specific set of architectures. The tool has been used in the market since 1999 and has customers in the American, Asian and European markets, especially in the critical market of aerospace and the telecom market. The full Xception product family includes: a) The main Xception tool, a state-of-the-art leader in Software Implemented Fault Injection (SWIFI) technology; b) The Easy Fault Definition (EFD) and Xtract (Xception Analysis Tool) add-on tools; c) The extended Xception tool (eXception), with the fault injection extensions for Scan Chain and pin-level forcing.
- AWS Fault Injection Service is a fully managed service for running fault injection experiments on AWS that makes it easier to improve an application's performance, observability, and resilience. Fault injection experiments are used in chaos engineering, which is the practice of stressing an application in testing or production environments by creating disruptive events, such as sudden increase in CPU or memory consumption, observing how the system responds, and implementing improvements.

### Libraries

- libfiu (Fault injection in userspace), C library to simulate faults in POSIX routines without modifying the source code. An API is included to simulate arbitrary faults at run-time at any point of the program.
- TestApi is a shared-source API library, which provides facilities for fault injection testing as well as other testing types, data-structures and algorithms for .NET applications.
- Fuzzino is an open source library, which provides a rich set of fuzzing heuristics that are generated from a type specification and/or valid values.
- krf is an open source Linux kernel module which provides a configurable facility to probabilistically return failure values for system calls.
- nlfaultinjection is designed to provide a simple, portable fault injection framework capable of running on just about any system, no matter how constrained and depends only on the C Standard Library.

## Fault injection in functional properties or test cases

In contrast to traditional mutation testing where mutant faults are generated and injected into the code description of the model, application of a series of newly defined mutation operators directly to the model properties rather than to the model code has also been investigated. Mutant properties that are generated from the initial properties (or test cases) and validated by the model checker should be considered as new properties that have been missed during the initial verification procedure. Therefore, adding these newly identified properties to the existing list of properties improves the coverage metric of the formal verification and consequently lead to a more reliable design.

## Application of fault injection

Fault injection can take many forms. In the testing of operating systems for example, fault injection is often performed by a *driver* (kernel-mode software) that intercepts *system calls* (calls into the kernel) and randomly returning a failure for some of the calls. This type of fault injection is useful for testing low-level user-mode software. For higher level software, various methods inject faults. In managed code, it is common to use instrumentation. Although fault injection can be undertaken by hand, a number of fault injection tools exist to automate the process of fault injection.

Depending on the complexity of the API for the level where faults are injected, fault injection tests often must be carefully designed to minimize the number of false positives. Even a well designed fault injection test can sometimes produce situations that are impossible in the normal operation of the software. For example, imagine there are two API functions, `Commit` and `PrepareForCommit`, such that alone, each of these functions can possibly fail, but if `PrepareForCommit` is called and succeeds, a subsequent call to `Commit` is guaranteed to succeed. Now consider the following code:

```mw
error = PrepareForCommit();
if (error == SUCCESS) {
  error = Commit();
  assert(error == SUCCESS);
}
```

Often, it will be infeasible for the fault injection implementation to keep track of enough state to make the guarantee that the API functions make. In this example, a fault injection test of the above code might hit the assert, whereas this would never happen in normal operation.
