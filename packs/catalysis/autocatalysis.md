---
title: "Autocatalysis"
source: https://en.wikipedia.org/wiki/Autocatalysis
domain: catalysis
license: CC-BY-SA-4.0
tags: chemical catalysis, catalytic cycle, turnover number, reaction catalyst
fetched: 2026-07-02
---

# Autocatalysis

A chemical reaction is **autocatalytic** if one of the reaction products is also a catalyst for the same reaction. Many forms of autocatalysis are recognized.

A *set* of chemical reactions can be said to be "collectively autocatalytic" if a number of those reactions produce, as reaction products, catalysts for enough of the other reactions that the entire set of chemical reactions is self-sustaining given an input of energy and food molecules (see autocatalytic set).

## Examples

Acid-catalyzed hydrolysis of esters produces carboxylic acids that also catalyze the same reaction. Indeed, the observation of an accelerating hydrolysis of gamma valerolactone to gamma-hydroxyvaleric acid led to the introduction of the concept of autocatalysis in 1890.

The oxidation of hydrocarbons by air or oxygen is the basis of autoxidation. Like many radical reactions, the rate vs time plot shows a sigmoidal behavior, characteristic of autocatalysis. Many reactions of organic compounds with halogen involve autocatalytic radical mechanisms. For example the reaction of acetophenone with bromine to give phenacyl bromide.

Oscillating reactions such as the Belousov–Zhabotinsky reaction are more complicated examples that involve autocatalysis. In such reactions the concentrations of some intermediates oscillate, as does the rate of formation of products. Other notable examples are the Lotka–Volterra equations for the predator-prey model, and the Brusselator model.

Autocatalysis applies also to reactions involving solids. Crystal growth provide dramatic examples of autocatalysis: the growth rate depends on the surface area of the growing crystal. The growth of metal films from solution using the technique of electroless plating is autocatalytic. The rate of plating accelerates after some deposition has occurred, i.e., nucleation.

## Mathematical description

Autocatalytic reactions are those in which at least one of the products is also a reactant. A simple autocatalytic reaction can be written

$A+B\rightleftharpoons 2B$

with the rate equations (for an elementary reaction)

${d \over dt}[A]=-k_{+}[A][B]+k_{-}[B]^{2}\,$

${d \over dt}[B]=+k_{+}[A][B]-k_{-}[B]^{2}\,$

.

This reaction is one in which a molecule of species A interacts with a molecule of species B. The A molecule is converted into a B molecule. The final product consists of the original B molecule plus the B molecule created in the reaction.

The key feature of these rate equations is that they are nonlinear; the second term on the right varies as the square of the concentration of B. This feature can lead to multiple fixed points of the system, much like a quadratic equation can have two roots. Multiple fixed points allow for multiple states of the system. A system existing in multiple macroscopic states is more orderly (has lower entropy) than a system in a single state.

The concentrations of A and B vary in time according to

$[B]={\frac {[A]_{0}+[B]_{0}}{({\frac {[A]_{0}}{[B]_{0}}}-{\frac {k_{-}}{k_{+}}})e^{-k_{+}([A]_{0}+[B]_{0})t}+1+{\frac {k_{-}}{k_{+}}}}}$

and

$[A]={\frac {([A]_{0}+[B]_{0})(({\frac {[A]_{0}}{[B]_{0}}}-{\frac {k_{-}}{k_{+}}})e^{-k_{+}([A]_{0}+[B]_{0})t}+{\frac {k_{-}}{k_{+}}})}{({\frac {[A]_{0}}{[B]_{0}}}-{\frac {k_{-}}{k_{+}}})e^{-k_{+}([A]_{0}+[B]_{0})t}+1+{\frac {k_{-}}{k_{+}}}}}$

.

For an irreversible reaction (i.e. $k_{-}=0$ )

$[A]={\frac {[A]_{0}+[B]_{0}}{1+{\frac {[B]_{0}}{[A]_{0}}}e^{([A]_{0}+[B]_{0})kt}}}$

and

$[B]={\frac {[A]_{0}+[B]_{0}}{1+{\frac {[A]_{0}}{[B]_{0}}}e^{-([A]_{0}+[B]_{0})kt}}}$

.

The graph for these equations is a sigmoid curve (specifically a logistic function), which is typical for autocatalytic reactions: these chemical reactions proceed slowly at the start (the induction period) because there is little catalyst present, the rate of reaction increases progressively as the reaction proceeds as the amount of catalyst increases and then it again slows down as the reactant concentration decreases. If the concentration of a reactant or product in an experiment follows a sigmoid curve, the reaction may be autocatalytic.

These kinetic equations apply for example to the acid-catalyzed hydrolysis of some esters to carboxylic acids and alcohols. There must be at least some acid present initially to start the catalyzed mechanism; if not the reaction must start by an alternate uncatalyzed path which is usually slower. The above equations (which do not consider the alternate pathway) for the catalyzed mechanism would imply that the concentration of acid product remains zero forever.

### Asymmetric autocatalysis

Asymmetric autocatalysis occurs when the reaction product is chiral and thus serves as a catalyst for its own production. Reactions of this type, such as the Soai reaction, have the property that they can amplify a very small enantiomeric excess into a large one. In another example, sodium chlorate crystallizes as an equilibrium mixture of left- and right-handed crystals. When seeded appropriated, saturated solutions of this salt (which is optically inactive), will produce batches of single enantiomeric crystals.

### Possible role in origin of life

An early example of autocatalysis is the formose reaction, in which formaldehyde and base produce sugars and related polyols. Characteristic of autocatalysis, this reaction rate is extremely slow initially but accelerates with time. This kind of reaction has often been cited as being relevant to the origin of life.

Autocatalysis is one explanation for abiogenesis. Illustrative is the reaction amino adenosine and pentafluorophenyl ester in the presence of amino adenosine triacid ester (AATE). This experiment demonstrated that autocatalysts could exhibit competition within a population of entities with heredity, which could be interpreted as a rudimentary form of natural selection, and that certain environmental changes (such as irradiation) could alter the chemical structure of some of these self-replicating molecules (an analog for mutation) in such ways that could either boost or interfere with its ability to react, thus boosting or interfering with its ability to replicate and spread in the population.
