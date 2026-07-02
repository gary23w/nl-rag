---
title: "Triple modular redundancy"
source: https://en.wikipedia.org/wiki/Triple_modular_redundancy
domain: lockstep-cores
license: CC-BY-SA-4.0
tags: lockstep cores, dual-core lockstep, triple modular redundancy, dual modular redundancy
fetched: 2026-07-02
---

# Triple modular redundancy

In computing, **triple modular redundancy**, sometimes called **triple-mode redundancy**, (**TMR**) is a fault-tolerant form of N-modular redundancy, in which three systems perform a process and that result is processed by a majority-voting system to produce a single output. If any one of the three systems fails, the other two systems can correct and mask the fault.

The TMR concept can be applied to many forms of redundancy, such as software redundancy in the form of N-version programming, and is commonly found in fault-tolerant computer systems.

Space satellite systems often use TMR, although satellite RAM usually uses Hamming error correction.

Some ECC memory uses triple modular redundancy hardware (rather than the more common Hamming code), because triple modular redundancy hardware is faster than Hamming error correction hardware. Called repetition code, some communication systems use N-modular redundancy as a simple form of forward error correction. For example, 5-modular redundancy communication systems (such as FlexRay) use the majority of 5 samples – if any 2 of the 5 results are erroneous, the other 3 results can correct and mask the fault.

Modular redundancy is a basic concept, dating to antiquity, while the first use of TMR in a computer was the Czechoslovak computer SAPO, in the 1950s.

## General case

The general case of TMR is called **N-modular redundancy**, in which any positive number of replications of the same action is used. The number is typically taken to be at least three, so that error correction by majority vote can take place; it is also usually taken to be odd, so that no ties may happen.

## Majority logic gate

### 3-input majority gate

The 3-input majority gate output is 1 if two or more of the inputs of the majority gate are 1; output is 0 if two or more of the majority gate's inputs are 0. Thus, the majority gate is the carry output of a full adder, i.e., the majority gate is a voting machine.

The 3-input majority gate can be represented by the following boolean equation and truth table:

$Q=AB\lor BC\lor AC$

| **INPUT** A   B   C | **OUTPUT** Q |   |   |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

In TMR, three identical logic circuits (logic gates) are used to compute the same set of specified Boolean function. If there are no circuit failures, the outputs of the three circuits are identical. But due to circuit failures, the outputs of the three circuits may be different.

### TMR operation

Assuming the Boolean function computed by the three identical logic gates has value 1, then: (a) if no circuit has failed, all three circuits produce an output of value 1, and the majority gate output has value 1. (b) if one circuit fails and produces an output of 0, while the other two are working correctly and produce an output of 1, the majority gate output is 1, i.e., it still has the correct value. And similarly for the case when the Boolean function computed by the three identical circuits has value 0. Thus, the majority gate output is guaranteed to be correct as long as no more than one of the three identical logic circuits has failed.

For a TMR system with a single voter of reliability (probability of working) Rv and three components of reliability Rm, the probability of it being correct can be shown to be RTMR = Rv (3 Rm2 − 2 Rm3).

TMR systems should use data scrubbing – rewrite flip-flops periodically – in order to avoid accumulation of errors.

### Voter

The majority gate itself could fail. This can be protected against by applying triple redundancy to the voters themselves.

In a few TMR systems, such as the Saturn Launch Vehicle Digital Computer and **functional triple modular redundancy (FTMR)** systems, the voters are also triplicated. Three voters are used – one for each copy of the next stage of TMR logic. In such systems there is no single point of failure.

Even though only using a single voter brings a single point of failure – a failed voter will bring down the entire system – most TMR systems do not use triplicated voters. This is because the majority gates are much less complex than the systems that they guard against, so they are much more reliable. By using the reliability calculations, it is possible to find the minimum reliability of the voter for TMR to be a win.

## Chronometers

To use triple modular redundancy, a ship must have at least three chronometers; two chronometers provided dual modular redundancy, allowing a backup if one should cease to work, but not allowing any error correction if the two displayed a different time, since in case of contradiction between the two chronometers, it would be impossible to know which one was wrong (the error detection obtained would be the same of having only one chronometer and checking it periodically). Three chronometers provided triple modular redundancy, allowing error correction if one of the three was wrong, so the pilot would take the average of the two with closer reading (vote for average precision).

There is an old adage to this effect, stating: "Never go to sea with two chronometers; take one or three."

Mainly this means that if two chronometers contradict, how do you know which one is correct? At one time this observation or rule was an expensive one as the cost of three sufficiently accurate chronometers was more than the cost of many types of smaller merchant vessels. Some vessels carried more than three chronometers – for example, HMS Beagle carried 22 chronometers. However, such a large number was usually only carried on ships undertaking survey work as was the case with the *Beagle*.

In the modern era, ships at sea use GNSS navigation receivers (with GPS, GLONASS & WAAS etc. support) – mostly running with WAAS or EGNOS support so as to provide accurate time (and location).

## In popular culture

- In Arthur C. Clarke's science fiction novel *Rendezvous with Rama*, the Ramans make heavy use of triple redundancy.
- In the popular anime *Neon Genesis Evangelion*, the Magi are a set of three biological supercomputers that must agree with a 2/3 majority vote before delivering a decision.
- In the film *Minority Report*, 3 "precogs" are used to predict impending homicides, using a triple modular redundancy. In the plot, this system fails, causing a false positive: an innocent man is wrongly accused of murder.
