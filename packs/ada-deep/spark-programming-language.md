---
title: "SPARK (programming language)"
source: https://en.wikipedia.org/wiki/SPARK_(programming_language)
domain: ada-deep
license: CC-BY-SA-4.0
tags: ada language, spark language, jean ichbiah, real time computing, formal verification, steelman requirements
fetched: 2026-07-02
---

# SPARK (programming language)

**SPARK** is a formally defined computer programming language based on the Ada programming language, intended for developing high-integrity software used in systems where predictable and highly reliable operation is essential. It facilitates developing applications that demand safety, security, or business integrity. It has especially found use in real-time computing and embedded systems where issues of safety-criticality or computer security are paramount.

Originally, three versions of SPARK existed (SPARK83, SPARK95, SPARK2005), based on Ada 83, Ada 95, and Ada 2005 respectively.

A fourth version, SPARK 2014, based on Ada 2012, was released on April 30, 2014. SPARK 2014 is a complete re-design of the language and supports software verification tools.

The SPARK language consists of a well-defined subset of the Ada language that uses contracts to describe the specification of components in a form that is suitable for both static and dynamic verification. SPARK is also designed to eliminate all language constructs that can cause unpredictable behavior.

In SPARK83/95/2005, the contracts are encoded in Ada comments and so are ignored by any standard Ada compiler, but are processed by the SPARK *Examiner* and its associated tools. These earlier versions focus on static verification of contracts.

SPARK 2014, in contrast, uses Ada 2012's built-in syntax of *aspects* to express contracts, bringing them into the core of the language. The main tool for SPARK 2014 (GNATprove) is based on the GNAT/GCC infrastructure, and re-uses almost all of the GNAT Ada 2012 front-end.

## Technical overview

SPARK utilises the strengths of Ada while trying to eliminate all its potential ambiguities and insecure constructs. SPARK programs are by design meant to be unambiguous, and their behavior is required to be unaffected by the choice of Ada compiler. These goals are achieved partly by omitting some of Ada's more problematic features (such as unrestricted parallel tasking) and partly by introducing contracts that encode the application designer's intentions and requirements for certain components of a program.

The combination of these approaches allows SPARK to meet its design objectives, which are:

- logical soundness
- rigorous formal definition
- simple semantics
- security
- expressive power
- verifiability
- bounded resource (space and time) requirements.
- minimal runtime system requirements

One member of the Praxis staff has said: "Our defect rate with Spark is at least 10 times, sometimes 100 times lower than those created with other languages."

## Contract examples

Consider the Ada subprogram specification below:

```
procedure Increment (X : in out Counter_Type);
```

In pure Ada, this might increment the variable `X` by one or one thousand; or it might set some global counter to `X` and return the original value of the counter in `X`; or it might do nothing with `X`.

With SPARK 2014, contracts are added to the code to provide more information regarding what a subprogram actually does. For example, the above specification may be altered to say:

```
procedure Increment (X : in out Counter_Type)
  with Global => null,
       Depends => (X => X);
```

This specifies that the `Increment` procedure uses no (neither update nor read) global variable and that the only data item used in calculating the new value of `X` is `X` alone.

Alternatively, the specification may be written as:

```
procedure Increment (X : in out Counter_Type)
  with Global  => (In_Out => Count),
       Depends => (Count  => (Count, X),
                   X      => null);
```

This specifies that `Increment` will use the global variable `Count` in the same package as `Increment`, that the exported value of `Count` depends on the imported values of `Count` and `X`, and that the exported value of `X` does not depend on any variables at all and it will be derived from constant data only.

If GNATprove is then run on the specification and corresponding body of a subprogram, it will analyse the body of the subprogram to build up a model of the information flow. This model is then compared against what has been specified by the annotations and any discrepancies reported to the user.

These specifications can be further extended by asserting various properties that either need to hold when a subprogram is called (*preconditions*) or that will hold once execution of the subprogram has completed (*postconditions*). For example, if writing:

```
procedure Increment (X : in out Counter_Type)
  with Global  => null,
       Depends => (X => X),
       Pre     => X < Counter_Type'Last,
       Post    => X = X'Old + 1;
```

This, now, specifies not only that `X` is derived from itself alone, but also that before `Increment` is called `X` must be strictly less than the last possible value of its type (to ensure that the result will never overflow) and that afterward `X` will be equal to the initial value of `X` plus one.

## Verification conditions

GNATprove can also generate a set of verification conditions (VCs). These are used to establish whether certain properties hold for a given subprogram. At a minimum, GNATprove will generate VCs to establish that all run-time errors cannot occur within a subprogram, such as:

- array index out of range
- type range violation
- division by zero
- numerical overflow

If a postcondition or any other assertion is added to a subprogram, GNATprove will also generate VCs that require the user to show that these properties hold for all possible paths through the subprogram.

Under the hood, GNATprove uses the Why3 intermediate language and VC Generator, and the CVC4, Z3, and Alt-Ergo theorem provers to discharge VCs. Use of other provers (including interactive proof checkers) is also possible through other components of the Why3 toolset.

## History

The beginnings of the technology go back to 1987, based on work done at the University of Southampton. The first version of SPARK (based on Ada 83) was produced at the university, with UK Ministry of Defence sponsorship, by Bernard Carré and Trevor Jennings. The name *SPARK* was derived from *SPADE Ada Kernel*, in reference to the *SPADE* subset of the Pascal programming language.

Subsequently the language was progressively extended and refined, first by Program Validation Limited and then by Praxis Critical Systems Limited. In 2004, Praxis Critical Systems Limited changed its name to Praxis High Integrity Systems Limited, and work on SPARK continued. In January 2010, the company became Altran Praxis.

In early 2009, Praxis formed a partnership with AdaCore, and released *SPARK Pro* under the terms of the GPL. This was followed in June 2009 by the SPARK GPL Edition 2009, aimed at the free and open-source software (FOSS) and academic communities.

In January 2013, Altran-Praxis changed its name to Altran, which in April 2021 became Capgemini Engineering (following Altran's merger with Capgemini).

The first Pro release of SPARK 2014 was announced on April 30, 2014, and was quickly followed by the SPARK 2014 GPL edition, aimed at the FLOSS and academic communities.

## Industrial applications

SPARK has been employed in a number of real-world industrial uses. Incorporating it as early in the design process as possible is seen as generally giving the most favorable result.

SPARK has been used in several high-profile safety-critical systems, covering commercial aviation (the Ship/Helicopter Operational Limits Instrumentation System, Rolls-Royce Trent series jet engines, the ARINC ACAMS system, the Lockheed Martin C130J), military aviation (EuroFighter Typhoon, Harrier GR9, AerMacchi M346), air-traffic management (UK NATS iFACTS system), rail (numerous signalling applications), medical (the LifeFlow ventricular assist device), and space applications (the Vermont Technical College CubeSat project).

In terms of the approval processes necessary for such systems, SPARK has been used to certify against the UK Defense standard (DEFSTAN) 00-55, as well as to the DO-178B Level A and ITSEC E6.

SPARK has also been used in secure systems development. Users include Rockwell Collins (Turnstile and SecureOne cross-domain solutions), the development of the original MULTOS CA, the NSA Tokeneer demonstrator, the secunet multi-level workstation, the Muen separation kernel and Genode block-device encrypter. Another case was implemented a secure Certificate Authority for the stored-value card produced by Mondex International, in which Z notation was used as a precursor to the coding in SPARK.

In August 2010, Rod Chapman, principal engineer of Altran Praxis, implemented Skein, one of the SHA-3 candidates, in SPARK. After careful optimization, he managed to have the SPARK version run only about 5 to 10% slower than the C implementation. Later improvements to the Ada middle-end in GCC (implemented by Eric Botcazou of AdaCore) closed the gap, with the SPARK code matching the C in performance exactly.

NVIDIA have also adopted SPARK for the implementation of security-critical firmware. Finding success in this, the company added SPARK for extra firmware-related projects and began in-house training in use of the SPARK technology.

In 2020, Rod Chapman re-implemented the TweetNaCl cryptographic library in SPARK 2014. The SPARK version of the library has a complete auto-active proof of type-safety, memory-safety and some correctness properties, and retains constant-time algorithms throughout. The SPARK code is also significantly faster than TweetNaCl.
