---
title: "Data-oriented design"
source: https://en.wikipedia.org/wiki/Data-oriented_design
domain: odin-lang
license: docs: BSD-3-Clause (odin-lang.org)
tags: odin language, odin lang, odin programming
fetched: 2026-07-02
---

# Data-oriented design

In computing, **data-oriented design** is a program optimization approach motivated by efficient usage of the CPU cache, often used in video game development. The approach is to focus on the data layout, separating and sorting fields according to when they are needed, and to think about transformations of data. Proponents include Mike Acton, Scott Meyers, and Jonathan Blow.

The parallel array (or structure of arrays) is the main example of data-oriented design. It is contrasted with the *array of structures* typical of object-oriented designs.

The definition of data-oriented design as a programming paradigm can be seen as contentious as many believe that it can be used side by side with another paradigm, but due to the emphasis on data layout, it is also incompatible with most other paradigms.

## Motives

These methods became especially popular in the mid to late 2000s during the seventh generation of video game consoles that included the IBM PowerPC based PlayStation 3 (PS3) and Xbox 360 consoles. Historically, game consoles often have relatively weak central processing units (CPUs) compared to the top-of-line desktop computer counterparts. This is a design choice to devote more power and transistor budget to the graphics processing units (GPUs). For example, the 7th generation CPUs were not manufactured with modern out-of-order execution processors, but instead use in-order processors with high clock speeds and deep pipelines. In addition, most types of computing systems have main memory located hundreds of clock cycles away from the processing elements. Furthermore, as CPUs have become faster alongside a large increase in main memory capacity, there is massive data consumption that increases the likelihood of cache misses in the shared bus, otherwise known as Von Neumann bottlenecking. Consequently, locality of reference methods have been used to control performance, requiring improvement of memory access patterns to fix bottlenecking. Some of the software issues were also similar to those encountered on the Itanium, requiring loop unrolling for upfront scheduling.

## Contrast with object orientation

The claim is that traditional object-oriented programming (OOP) design principles result in poor data locality, more so if runtime polymorphism (dynamic dispatch) is used (which is especially problematic on some processors). Although OOP appears to "organise code around data", it actually organises source code around data types rather than physically grouping individual fields and arrays in an efficient format for access by specific functions. Moreover, it often hides layout details under abstraction layers, while a data-oriented programmer wants to consider this first and foremost.
