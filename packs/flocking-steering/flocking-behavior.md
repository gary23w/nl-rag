---
title: "Flocking"
source: https://en.wikipedia.org/wiki/Flocking_(behavior)
domain: flocking-steering
license: CC-BY-SA-4.0
tags: flocking behavior, steering behaviors, boids algorithm, swarm steering
fetched: 2026-07-02
---

# Flocking

(Redirected from

Flocking (behavior)

)

**Flocking** is the behavior exhibited when a group of birds, called a flock, are foraging or in flight. Sheep and goats also exhibit flocking behavior. Flocking by birds and mammals is similar to schooling in fish and these are often studied together.

Flocking is generally believed to arise from the need for cover and protection from predators in animal behavior. This is an emergent behaviour governed by local rules that are followed by individuals and does not involve any central coordination.

## In nature

There are parallels with the shoaling behaviour of fish, the swarming behaviour of insects, and herd behaviour of land animals. During the winter months, starlings are known for aggregating into huge flocks of hundreds to thousands of individuals, murmurations, which when they take flight altogether, render large displays of intriguing swirling patterns in the skies above observers.

### Measurement

Measurements of bird flocking have been made using high-speed cameras, and a computer analysis has been made to test the simple rules of flocking mentioned below. It is found that they generally hold true in the case of bird flocking, but the long range attraction rule (cohesion) applies to the nearest 5–10 neighbors of the flocking bird and is independent of the distance of these neighbors from the bird. In addition, there is an anisotropy with regard to this cohesive tendency, with more cohesion being exhibited towards neighbors to the sides of the bird, rather than in front or behind. This is likely due to the field of vision of the flying bird being directed to the sides rather than directly forward or backward.

Another recent study is based on an analysis of high speed camera footage of flocks above Rome, and uses a computer model assuming minimal behavioural rules.

## Algorithms

Various algorithms have been introduced to aid in the study of biological flocking. These algorithms have different origins, from computer graphics to physics, each offering a unique perspective on the real phenomena.

Computer simulations and mathematical models that have been developed to emulate the flocking behaviours of birds can also generally be applied to the "flocking" behaviour of other species. As a result, the term "flocking" is sometimes applied, in computer science, to species other than birds, to mean collective motion by a group of self-propelled entities, a collective animal behaviour exhibited by many living beings such as fish, bacteria, and insects.

### Reynolds' models

Flocking behaviour was simulated on a computer in 1987 by Craig Reynolds with the program Boids. This program simulates simple agents (boids) that move according to a set of three basic rules: separation, alignment and cohesion. The result, akin to a flock of birds, a school of fish, or a swarm of insects, was developed for motion picture visual effects.

#### Rules

Reynolds' models of flocking behaviour are controlled by three simple rules:

**Separation**

Avoid crowding neighbours (short range repulsion)

**Alignment**

Steer towards average heading of neighbours

**Cohesion**

Steer towards average position of neighbours (long range attraction)

With these three simple rules, the flock moves in an extremely realistic way, creating complex motion and interaction that would be extremely hard to create otherwise.

#### Rule variants

The basic model has been extended in several different ways since Reynolds proposed it. For instance, C. Delgado-Mata et al. extended the basic model in 2007 to incorporate the effects of fear. Olfaction was used to transmit emotion between animals, through pheromones modelled as particles in a free expansion gas.

Christopher Hartman and Bedr̆ich Benes introduced in 2006 a complementary force to the alignment that they call the change of leadership. This steer defines the chance of the bird to become a leader and try to escape.

### Vicsek models

An early model from the domain of physics, the Vicsek model (named after Tamás Vicsek) from 1995 gained attention in the study of flocking as a form active matter, a system where energy is continually added (unlike thermodynamic models).

Applied to collective motion and swarming, Vicsek models demonstrate that a simpler set of rules with just fixed speed, self-propelled particles, and neighbor alignment, are able to achieve sub-group flocking and milling (vortex structures). These models are attractive in physics due to their simplicity and universality.

Such models however, do not exhibit speed changes due to climbing and diving in flight, or complex phenomena such as orientation waves due to perceptual vision.

### Aerodynamic models

Charlotte K. Hemelrijk and Hanno Hildenbrandt in 2011 used attraction, alignment, and avoidance, and extended this with a number of traits of real starlings:

- birds fly according to fixed wing aerodynamics, while rolling when turning (thus losing lift);
- they coordinate with a limited number of interaction neighbours of 7 (like real starlings);
- they try to stay above a sleeping site (like starlings do at dawn), and when they happen to move outwards from the sleeping site, they return to it by turning; and
- they move at relative fixed speed.

The authors showed that the specifics of flying behaviour as well as large flock size and low number of interaction partners were essential to the creation of the variable shape of flocks of starlings.

### Orientation models

Rama Carl Hoetzlein introduced the orientation-model in 2024 which separates the perceptual aspects of bird flight from the underlying aerodynamic model, linking these two control systems only by a heading target similar to real flight control. The perceptual model of each bird is orientation-based, mapped to a sphere, which more closely matches the biological vision system. The output of perception is a target heading angle (not a vector), which is used to control an aerodynamic model much like a flight simulator. Energy and frequency analysis in this work bridge the study of real bird kinetics with simulation models. This model demonstrates emergent, spontaneous orientation waves for the first time, a key feature in flocking murmurations.

## Complexity

In flocking simulations, there is no central control; each bird behaves autonomously. In other words, each bird has to decide for itself which flocks to consider as its environment.

A basic implementation of a flocking algorithm has complexity $O(n^{2})$ – each bird could potentially interact and respond to every other bird. To limit complexity, it is assumed that birds only interact with a limited number of neighbors spatially in 2D or 3D. This was proven empirically in 2008 by Ballerini et al., where it was shown that Starlings typically interact with at most seven topological neighbors.

Improvements:

- Spatial subdivision. The entire area/volume of the flock is divided uniformly. Each bin stores which birds it contains. Each time a bird moves from one bin to another, bin contents are updated.
  - Complexity: $O(nk)$ , k is number of surrounding bins to consider.

Lee Spector, Jon Klein, Chris Perry and Mark Feinstein studied the emergence of collective behaviour in evolutionary computation systems.

Bernard Chazelle proved that under the assumption that each bird adjusts its velocity and position to the other birds within a fixed radius, the time it takes to converge to a steady state is an iterated exponential of height logarithmic in the number of birds. This means that if the number of birds is large enough, the convergence time will be so great that it might as well be infinite. This result applies only to convergence to a steady state. For example, arrows fired into the air at the edge of a flock will cause the whole flock to react more rapidly than can be explained by interactions with neighbors, which are slowed down by the time delay in the bird's central nervous systems—bird-to-bird-to-bird.

## Applications

Flock-like behaviour in humans may occur when people are drawn to a common focal point or when repelled, as below: a crowd fleeing from the sound of gunfire.

In Cologne, Germany, two biologists from the University of Leeds demonstrated a flock-like behaviour in humans. The group of people exhibited a very similar behavioural pattern to that of a flock, where if 5% of the flock would change direction the others would follow suit. When one person was designated as a predator and everyone else was to avoid him, the flock behaved very much like a school of fish.

Flocking has also been considered as a means of controlling the behaviour of Unmanned Air Vehicles (UAVs).

Flocking is a common technology in screensavers, and has found its use in animation. Flocking has been used in many films to generate crowds which move more realistically. Tim Burton's *Batman Returns* (1992) featured flocking bats.

Flocking behaviour has been used for other interesting applications. It has been applied to automatically program Internet multi-channel radio stations. It has also been used for visualizing information and for optimization tasks.
