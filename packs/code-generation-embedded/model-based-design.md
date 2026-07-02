---
title: "Model-based design"
source: https://en.wikipedia.org/wiki/Model-based_design
domain: code-generation-embedded
license: CC-BY-SA-4.0
tags: embedded code generation, automatic programming, autocode toolchain, model to c
fetched: 2026-07-02
---

# Model-based design

**Model-based design** (**MBD**) is a mathematical and visual method of addressing problems associated with designing complex control, signal processing and communication systems. It is used in many motion control, industrial equipment, aerospace, and automotive applications. Model-based design is a methodology applied in designing embedded software.

## Overview

Model-based design provides an efficient approach for establishing a common framework for communication throughout the design process while supporting the development cycle (V-model). In model-based design of control systems, development is manifested in these four steps:

1. modeling a plant,
2. analyzing and synthesizing a controller for the plant,
3. simulating the plant and controller,
4. integrating all these phases by deploying the controller.

The model-based design is significantly different from traditional design methodology. Rather than using complex structures and extensive software code, designers can use Model-based design to define plant models with advanced functional characteristics using continuous-time and discrete-time building blocks. These built models used with simulation tools can lead to rapid prototyping, software testing, and verification. Not only is the testing and verification process enhanced, but also, in some cases, hardware-in-the-loop simulation can be used with the new design paradigm to perform testing of dynamic effects on the system more quickly and much more efficiently than with traditional design methodology.

## History

As early as the 1920s two aspects of engineering, control theory and control systems, converged to make large-scale integrated systems possible. In those early days controls systems were commonly used in the industrial environment. Large process facilities started using process controllers for regulating continuous variables such as temperature, pressure, and flow rate. Electrical relays built into ladder-like networks were one of the first discrete control devices to automate an entire manufacturing process.

Control systems gained momentum, primarily in the automotive and aerospace sectors. In the 1950s and 1960s, the push to space generated interest in embedded control systems. Engineers constructed control systems such as engine control units and flight simulators, that could be part of the end product. By the end of the twentieth century, embedded control systems were ubiquitous, as even major household consumer appliances such as washing machines and air conditioners contained complex and advanced control algorithms, making them much more "intelligent".

In 1969, the first computer-based controllers were introduced. These early programmable logic controllers (PLC) mimicked the operations of already available discrete control technologies that used the out-dated relay ladders. The advent of PC technology brought a drastic shift in the process and discrete control market. An off-the-shelf desktop loaded with adequate hardware and software can run an entire process unit, and execute complex and established PID algorithms or work as a Distributed Control System (DCS).

## Steps

The main steps in model-based design approach are:

1. Plant modeling. Plant modeling can be data-driven or based on first principles. Data-driven plant modeling uses techniques such as System identification. With system identification, the plant model is identified by acquiring and processing raw data from a real-world system and choosing a mathematical algorithm with which to identify a mathematical model. Various kinds of analysis and simulations can be performed using the identified model before it is used to design a model-based controller. First-principles based modeling is based on creating a block diagram model that implements known differential-algebraic equations governing plant dynamics. A type of first-principles based modeling is physical modeling, where a model consists in connected blocks that represent the physical elements of the actual plant.
2. Controller analysis and synthesis. The mathematical model conceived in step 1 is used to identify dynamic characteristics of the plant model. A controller can then be synthesized based on these characteristics.
3. Offline simulation and real-time simulation. The time response of the dynamic system to complex, time-varying inputs is investigated. This is done by simulating a simple LTI (Linear Time-Invariant) model, or by simulating a non-linear model of the plant with the controller. Simulation allows specification, requirements, and modeling errors to be found immediately, rather than later in the design effort. Real-time simulation can be done by automatically generating code for the controller developed in step 2. This code can be deployed to a special real-time prototyping computer that can run the code and control the operation of the plant. If a plant prototype is not available, or testing on the prototype is dangerous or expensive, code can be automatically generated from the plant model. This code can be deployed to the special real-time computer that can be connected to the target processor with running controller code. Thus a controller can be tested in real-time against a real-time plant model.
4. Deployment. Ideally this is done via code generation from the controller developed in step 2. It is unlikely that the controller will work on the actual system as well as it did in simulation, so an iterative debugging process is carried out by analyzing results on the actual target and updating the controller model. Model-based design tools allow all these iterative steps to be performed in a unified visual environment.

## Disadvantages

The disadvantages of model-based design are fairly well understood this late in development lifecycle of the product and development.

- One major disadvantage is that the approach taken is a blanket or coverall approach to standard embedded and systems development. Often the time it takes to port between processors and ecosystems can outweigh the temporal value it offers in the simpler lab based implementations.

- Much of the compilation tool chain is closed source, and prone to fence post errors, and other such common compilation errors that are easily corrected in traditional systems engineering.

- Design and reuse patterns can lead to implementations of models that are not well suited to that task. Such as implementing a controller for a conveyor belt production facility that uses a thermal sensor, speed sensor, and current sensor. That model is generally not well suited for re-implementation in a motor controller etc. Though its very easy to port such a model over, and introduce all the software faults therein.
- **Version control issues**: Model-based design can encounter significant challenges due to the lack of high-quality tools for managing version control, particularly for handling diff and merge operations. This can lead to difficulties in managing concurrent changes and maintaining robust revision control practices. Although newer tools, such as 3-way merge, have been introduced to address these issues, effectively integrating these solutions into existing workflows remains a complex task.

While Model-based design has the ability to simulate test scenarios and interpret simulations well, in real world production environments, it is often not suitable. Over reliance on a given toolchain can lead to significant rework and possibly compromise entire engineering approaches. While it's suitable for bench work, the choice to use this for a production system should be made very carefully.

## Advantages

Some of the advantages model-based design offers in comparison to the traditional approach are:

- Model-based design provides a common design environment, which facilitates general communication, data analysis, and system verification between various (development) groups.
- Engineers can locate and correct errors early in system design, when the time and financial impact of system modification are minimized.
- Design reuse, for upgrades and for derivative systems with expanded capabilities, is facilitated.

Because of the limitations of graphical tools, design engineers previously relied heavily on text-based programming and mathematical models. However, developing these models was time-consuming, and highly prone to error. In addition, debugging text-based programs is a tedious process, requiring much trial and error before a final fault-free model could be created, especially since mathematical models undergo unseen changes during the translation through the various design stages.

Graphical modeling tools aim to improve these aspects of design. These tools provide a very generic and unified graphical modeling environment, and they reduce the complexity of model designs by breaking them into hierarchies of individual design blocks. Designers can thus achieve multiple levels of model fidelity by simply substituting one block element with another. Graphical models also help engineers to conceptualize the entire system and simplify the process of transporting the model from one stage to another in the design process. Boeing's simulator EASY5 was among the first modeling tools to be provided with a graphical user interface, together with AMESim, a multi-domain, multi-level platform based on the Bond Graph theory. This was soon followed by tool like 20-sim and Dymola, which allowed models to be composed of physical components like masses, springs, resistors, etc. These were later followed by many other modern tools such as Simulink and LabVIEW.
