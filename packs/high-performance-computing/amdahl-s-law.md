---
title: "Amdahl's law"
source: https://en.wikipedia.org/wiki/Amdahl%27s_law
domain: high-performance-computing
license: CC-BY-SA-4.0
tags: high-performance computing, parallel computing, amdahl law, gpu general-purpose computing
fetched: 2026-07-02
---

# Amdahl's law

In computer architecture, **Amdahl's law** (or **Amdahl's argument**) is a formula limiting the speedup of a task as resources are added to the system executing that task.

The law can be stated as:

> the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used.

It is named after computer scientist Gene Amdahl, and was presented at the American Federation of Information Processing Societies (AFIPS) Spring Joint Computer Conference in 1967.

Amdahl's law is often used in parallel computing to predict the theoretical speedup when using multiple processors.

## Definition

In the context of Amdahl's law, speedup can be defined as:

${\text{Speedup}}={\frac {\text{Performance for the entire task when enhancements are applied}}{\text{Performance for the same task without those enhancements}}}$

or

${\text{Speedup}}={\frac {\text{Execution time for the entire task without enhancements}}{\text{Execution time for the same task when enhancements are applied}}}$

Amdahl's law can be formulated in the following way:

${\text{Speedup}}_{\text{overall}}={\frac {1}{(1-{\text{time}}_{\text{optimized}})+{\frac {{\text{time}}_{\text{optimized}}}{{\text{speedup}}_{\text{optimized}}}}}}$

where

- ${\text{Speedup}}_{\text{overall}}$ represents the total speedup of a program
- ${\text{Time}}_{\text{optimized}}$ represents the proportion of time spent on the portion of the code where improvements are made
- ${\text{Speedup}}_{\text{optimized}}$ represents the extent of the improvement

The ${\text{Speedup}}_{\text{overall}}$ is frequently much lower than one might expect. For instance, if a programmer enhances a part of the code that represents 10% of the total execution time (i.e. ${\text{Time}}_{\text{optimized}}$ of 0.10) and achieves a ${\text{Speedup}}_{\text{optimized}}$ of 10,000, then ${\text{Speedup}}_{\text{overall}}$ becomes 1.11 which means only 11% improvement in total speedup of the program. So, despite a massive improvement in one section, the overall benefit is quite small. In another example, if the programmer optimizes a section that accounts for 99% of the execution time (i.e. ${\text{Time}}_{\text{optimized}}$ of 0.99) with a speedup factor of 100 (i.e. ${\text{Speedup}}_{\text{optimized}}$ of 100), the ${\text{Speedup}}_{\text{overall}}$ only reaches 50. This indicates that half of the potential performance gain ( ${\text{Speedup}}_{\text{overall}}$ will reach 100 if 100% of the execution time is covered) is lost due to the remaining 1% of execution time that was not improved.

## Derivation

A task executed by a system whose resources are improved compared to an initial similar system can be split up into two parts:

- a part that does not benefit from the improvement of the resources of the system;
- a part that benefits from the improvement of the resources of the system.

An example is a computer program that processes files. A part of that program may scan the directory of the disk and create a list of files internally in memory. After that, another part of the program passes each file to a separate thread for processing. The part that scans the directory and creates the file list cannot be sped up on a parallel computer, but the part that processes the files can.

The execution time of the whole task before the improvement of the resources of the system is denoted as T . It includes the execution time of the part that would not benefit from the improvement of the resources and the execution time of the one that would benefit from it. The fraction of the execution time of the task that would benefit from the improvement of the resources is denoted by p . The one concerning the part that would not benefit from it is therefore $1-p$ . Then:

$T=(1-p)T+pT.$

It is the execution of the part that benefits from the improvement of the resources that is accelerated by the factor s after the improvement of the resources. Consequently, the execution time of the part that does not benefit from it remains the same, while the part that benefits from it becomes:

${\frac {p}{s}}T.$

The theoretical execution time $T(s)$ of the whole task after the improvement of the resources is then:

$T(s)=(1-p)T+{\frac {p}{s}}T.$

Amdahl's law gives the theoretical speedup in latency of the execution of the whole task *at fixed workload W*, which yields

$S_{\text{latency}}(s)={\frac {TW}{T(s)W}}={\frac {T}{T(s)}}={\frac {1}{1-p+{\frac {p}{s}}}}.$

### Parallel programs

If 30% of the execution time may be the subject of a speedup, *p* will be 0.3; if the improvement makes the affected part twice as fast, *s* will be 2. Amdahl's law states that the overall speedup of applying the improvement will be:

$S_{\text{latency}}={\frac {1}{1-p+{\frac {p}{s}}}}={\frac {1}{1-0.3+{\frac {0.3}{2}}}}=1.18.$

For example, assume that we are given a serial task which is split into four consecutive parts, whose percentages of execution time are *p*1 = 0.11, *p*2 = 0.18, *p*3 = 0.23, and *p*4 = 0.48 respectively. Then we are told that the 1st part is not sped up, so *s*1 = 1, while the 2nd part is sped up 5 times, so *s*2 = 5, the 3rd part is sped up 20 times, so *s*3 = 20, and the 4th part is sped up 1.6 times, so *s*4 = 1.6. By using Amdahl's law, the overall speedup is

$S_{\text{latency}}={\frac {1}{{\frac {p1}{s1}}+{\frac {p2}{s2}}+{\frac {p3}{s3}}+{\frac {p4}{s4}}}}={\frac {1}{{\frac {0.11}{1}}+{\frac {0.18}{5}}+{\frac {0.23}{20}}+{\frac {0.48}{1.6}}}}=2.19.$

Notice how the 5 times and 20 times speedup on the 2nd and 3rd parts respectively don't have much effect on the overall speedup when the 4th part (48% of the execution time) is accelerated by only 1.6 times.

### Serial programs

For example, with a serial program in two parts *A* and *B* for which *T**A* = 3 s and *T**B* = 1 s,

- if part *B* is made to run 5 times faster, that is *s* = 5 and *p* = *T**B*/(*T**A* + *T**B*) = 0.25, then $S_{\text{latency}}={\frac {1}{1-0.25+{\frac {0.25}{5}}}}=1.25;$
- if part *A* is made to run 2 times faster, that is *s* = 2 and *p* = *T**A*/(*T**A* + *T**B*) = 0.75, then $S_{\text{latency}}={\frac {1}{1-0.75+{\frac {0.75}{2}}}}=1.60.$

Therefore, making part *A* to run 2 times faster is better than making part *B* to run 5 times faster. The percentage improvement in speed can be calculated as

${\text{percentage improvement}}=100\left(1-{\frac {1}{S_{\text{latency}}}}\right).$

- Improving part *A* by a factor of 2 will increase overall program speed by a factor of 1.60, which makes it 37.5% faster than the original computation.
- However, improving part *B* by a factor of 5, which presumably requires more effort, will achieve an overall speedup factor of 1.25 only, which makes it 20% faster.

### Optimizing the sequential part of parallel programs

If the non-parallelizable part is optimized by a factor of O , then

$T(O,s)=(1-p){\frac {T}{O}}+{\frac {p}{s}}T.$

It follows from Amdahl's law that the speedup due to parallelism is given by

$S_{\text{latency}}(O,s)={\frac {T(O)}{T(O,s)}}={\frac {(1-p){\frac {1}{O}}+{p}}{{\frac {1-p}{O}}+{\frac {p}{s}}}}.$

When $s=1$ , we have $S_{\text{latency}}(O,s)=1$ , meaning that the speedup is measured with respect to the execution time after the non-parallelizable part is optimized.

When $s=\infty$ ,

$S_{\text{latency}}(O,\infty )={\frac {T(O)}{T(O,s)}}={\frac {(1-p){\frac {1}{O}}+{p}}{{\frac {1-p}{O}}+{\frac {p}{s}}}}=1+{\frac {p}{1-p}}O.$

If $1-p=0.4$ , $O=2$ and $s=5$ , then:

$S_{\text{latency}}(O,s)={\frac {T(O)}{T(O,s)}}={\frac {{0.4}{\frac {1}{2}}+0.6}{{\frac {0.4}{2}}+{\frac {0.6}{5}}}}=2.5.$

### Transforming sequential parts of parallel programs into parallelizable

Next, we consider the case wherein the non-parallelizable part is reduced by a factor of $O'$ , and the parallelizable part is correspondingly increased. Then

$T'(O',s)={\frac {1-p}{O'}}T+\left(1-{\frac {1-p}{O'}}\right){\frac {T}{s}}.$

It follows from Amdahl's law that the speedup due to parallelism is given by

$S'_{\text{latency}}(O',s)={\frac {T'(O')}{T'(O',s)}}={\frac {1}{{\frac {1-p}{O'}}+\left(1-{\frac {1-p}{O'}}\right){\frac {1}{s}}}}.$

## Relation to the law of diminishing returns

Amdahl's law is often conflated with the law of diminishing returns, whereas only a special case of applying Amdahl's law demonstrates the law of diminishing returns. If one picks optimally (in terms of the achieved speedup) what is to be improved, then one will see monotonically decreasing improvements as one improves. If, however, one picks non-optimally, after improving a sub-optimal component and moving on to improve a more optimal component, one can see an increase in the return. Note that it is often rational to improve a system in an order that is "non-optimal" in this sense, given that some improvements are more difficult or require larger development time than others.

Amdahl's law does represent the law of diminishing returns if one is considering what sort of return one gets by adding more processors to a machine, if one is running a fixed-size computation that will use all available processors to their capacity. Each new processor added to the system will add less usable power than the previous one. Each time one doubles the number of processors the speedup ratio will diminish, as the total throughput heads toward the limit of 1/(1 − *p*).

This analysis neglects other potential bottlenecks such as memory bandwidth and I/O bandwidth. If these resources do not scale with the number of processors, then merely adding processors provides even lower returns.

An implication of Amdahl's law is that to speed up real applications which have both serial and parallel portions, heterogeneous computing techniques are required. There are novel speedup and energy consumption models based on a more general representation of heterogeneity, referred to as the normal form heterogeneity, that support a wide range of heterogeneous many-core architectures. These modelling methods aim to predict system power efficiency and performance ranges, and facilitates research and development at the hardware and system software levels.
