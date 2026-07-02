---
title: "Active Oberon"
source: https://en.wikipedia.org/wiki/Active_Oberon
domain: oberon-language
license: CC-BY-SA-4.0
tags: oberon language, niklaus wirth, oberon operating system, component pascal, active oberon
fetched: 2026-07-02
---

# Active Oberon

**Active Oberon** is a general purpose programming language developed during 1996–1998 by the group around Niklaus Wirth and Jürg Gutknecht at the Swiss Federal Institute of Technology in Zürich (ETH Zurich). It is an extension of the programming language Oberon. The extensions aim at implementing active objects as expressions for parallelism. Compared to its predecessors, Oberon and Oberon-2, Active Oberon adds objects (with object-centered access protection and local activity control), system-guarded assertions, preemptive priority scheduling and a changed syntax for methods (named *type-bound procedures* in Oberon vocabulary). Objects may be *active*, which means that they may be threads or processes. Unlike Java or C#, objects may be synchronized not only with signals but directly on conditions. This simplifies concurrent programs and their development.

As it is tradition in the Oberon world, the Active Oberon language compiler is implemented in Active Oberon. The operating system, especially the kernel, synchronizes and coordinates different active objects.

Active Oberon was renamed *Active Object System* (AOS) in 2002, then due to trademark issues, renamed *Bluebottle* in 2005, and then renamed *A2* in 2008.

An Active Oberon fork is the language Zonnon.
