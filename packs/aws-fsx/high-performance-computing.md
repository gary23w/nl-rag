---
title: "High-performance computing"
source: https://en.wikipedia.org/wiki/High-performance_computing
domain: aws-fsx
license: CC-BY-SA-4.0
tags: aws fsx, amazon fsx, managed file server, windows file storage
fetched: 2026-07-02
---

# High-performance computing

**High-performance computing** (**HPC**) is the use of supercomputers and computer clusters to solve advanced problems.

## Overview

HPC integrates systems administration (including network and security knowledge), parallel computing and distributed computing into a multidisciplinary field that combines digital electronics, computer architecture, system software, programming languages, algorithms and computational techniques. HPC technologies are the tools and systems used to implement and create high performance computing systems. Since around 2005, HPC systems have shifted from supercomputing to computing clusters and grids. Because of the need of networking in clusters and grids, High Performance Computing Technologies are achieved by the use of a collapsed network backbone, because the collapsed backbone architecture is simple to troubleshoot and upgrades can be applied to a single router as opposed to multiple ones. HPC integrates with data analytics in AI engineering workflows to generate new data streams that increase a simulation's ability to answer the "what if" questions.

The term is most commonly associated with computing used for scientific research or computational science. A related term, high-performance technical computing (HPTC), generally refers to the engineering applications of cluster-based computing (such as computational fluid dynamics and the building and testing of virtual prototypes). HPC has also been applied to business uses such as data warehouses, line of business (LOB) applications, and transaction processing.

High-performance computing (HPC) as a term arose after the term "supercomputing". HPC is sometimes used as a synonym for supercomputing; but, in other contexts, "supercomputer" is used to refer to a more powerful subset of "high-performance computers", and the term "supercomputing" becomes a subset of "high-performance computing". The potential for confusion over the use of these terms is apparent.

Because most current applications are not designed for HPC technologies but are retrofitted, they are not designed or tested for scaling to more powerful processors or machines. Since networking clusters and grids use multiple processors and computers, these scaling problems can cripple critical systems in future supercomputing systems. Therefore, either the existing tools do not address the needs of the high performance computing community or the HPC community is unaware of these tools. A few examples of commercial HPC technologies include:

- structural engineering for building design
- the simulation of car crashes for structural design
- molecular interaction for new drug design
- the airflow over automobiles or airplanes
- climate modeling and weather prediction
- genetic research and DNA sequencing
- robotics and autonomous vehicle development
- electromagnetic simulations for wireless communication

In government and research institutions, scientists simulate galaxy formation and evolution, fusion energy, and global warming, as well as work to create more accurate short- and long-term weather forecasts. The world's tenth most powerful supercomputer in 2008, IBM Roadrunner (located at the United States Department of Energy's Los Alamos National Laboratory) simulated the performance, safety, and reliability of nuclear weapons and certifies their functionality.

## TOP500

TOP500 ranks the world's 500 fastest high-performance computers, as measured by the High Performance LINPACK (HPL) benchmark. Not all existing computers are ranked, either because they are ineligible (e.g., they cannot run the HPL benchmark) or because their owners have not submitted an HPL score (e.g., because they do not wish the size of their system to become public information, for defense reasons). In addition, the use of the single LINPACK benchmark is controversial, in that no single measure can test all aspects of a high-performance computer. To help overcome the limitations of the LINPACK test, the U.S. government commissioned one of its originators, Jack Dongarra of the University of Tennessee, to create a suite of benchmark tests that includes LINPACK and others, called the HPC Challenge benchmark suite. This evolving suite has been used in some HPC procurements, but, because it is not reducible to a single number, it has been unable to overcome the publicity advantage of the less useful TOP500 LINPACK test. The TOP500 list is updated twice a year, once in June at the ISC European Supercomputing Conference and again at a US Supercomputing Conference in November.

Many ideas for the new wave of grid computing were originally borrowed from HPC.

## High performance computing in the cloud

Traditionally, HPC has involved an on-premises infrastructure, investing in supercomputers or computer clusters. Over the last decade, cloud computing has grown in popularity for offering computer resources in the commercial sector regardless of their investment capabilities. Some characteristics like scalability and containerization also have raised interest in academia. However security in the cloud concerns such as data confidentiality are still considered when deciding between cloud or on-premise HPC resources.

## Current leading Supercomputers

Below is a list of the main HPCs by computing power, as reported in the Top500 list:

- El Capitan: this HPE Cray EX255a system reaches 1.742 exaFLOPS with 1,051,392 CPU cores and 9,988,224 accelerator cores, totaling 11,039,616 cores. It uses Slingshot-11 interconnect technology and is housed at the Lawrence Livermore National Laboratory, USA.

- Frontier: boasting 1.353 exaFLOPS, this HPE Cray EX235a system features 614,656 CPU cores and 8,451,520 accelerator cores, making a total of 9,066,176 cores. It operates with Slingshot-11 interconnects at Oak Ridge National Laboratory, USA.

- Aurora: this Intel-powered system delivers 1.012 exaFLOPS, leveraging Xeon and Ponte Vecchio architectures. It is installed at Argonne National Laboratory, USA.

- Eagle: powered by Intel Xeon Platinum 8480C 48C 2GHz processors and NVIDIA H100 GPUs, Eagle reaches 561.20 petaFLOPS of computing power, with 2,073,600 cores. It features NVIDIA Infiniband NDR for high-speed connectivity and is hosted by Microsoft Azure, USA.

- HPC6: the most powerful industrial supercomputer in the world, HPC6 was developed by Eni and launched in November 2024. With 606 petaFLOPS of computing power, it is used for energy research and operates in Italy. It is located in the Eni Green Data Center in Ferrera Erbognone (PV).

- Fugaku: developed by Fujitsu, this system achieves 442.01 petaFLOPS using A64FX 48C 2.2GHz processors and Tofu interconnect D technology. It is located at RIKEN Center for Computational Science, Japan.

- Alps: this HPE Cray EX254n system reaches 434.90 petaFLOPS, powered by NVIDIA Grace 72C 3.1GHz processors and NVIDIA GH200 Superchips, connected through Slingshot-11 interconnects. It is located at CSCS, Switzerland.

- LUMI: one of Europe's fastest supercomputers, LUMI achieves 379.70 petaFLOPS with AMD Optimized 3rd Generation EPYC 64C 2GHz processors and AMD Instinct MI250X accelerators. It is hosted by CSC, Finland, as part of the EuroHPC initiative.

- Leonardo: developed under the EuroHPC initiative, this BullSequana XH2000 system reaches 241.20 petaFLOPS with Xeon Platinum 8358 32C 2.6GHz processors and NVIDIA A100 SXM4 64GB accelerators. It is installed at CINECA, Italy.

- Tuolumne: Tuolumne achieves 208.10 petaFLOPS and is powered by AMD 4th Gen EPYC 24C 1.8GHz processors and AMD Instinct MI300A accelerators. It operates at Lawrence Livermore National Laboratory, USA.

- MareNostrum 5 ACC: this BullSequana XH3000 system runs at 175.30 petaFLOPS, featuring Xeon Platinum 8460Y+ 32C 2.3GHz processors and NVIDIA H100 64GB accelerators. It is hosted by the Barcelona Supercomputing Center (BSC), Spain, as part of EuroHPC.
