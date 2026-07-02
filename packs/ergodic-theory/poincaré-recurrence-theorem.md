---
title: "Poincaré recurrence theorem"
source: https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem
domain: ergodic-theory
license: CC-BY-SA-4.0
tags: ergodic theory, measure-preserving system, ergodic theorem, topological entropy
fetched: 2026-07-02
---

# Poincaré recurrence theorem

In mathematics and physics, the **Poincaré recurrence theorem** states that certain dynamical systems will, after a sufficiently long but finite time, almost certainly return to a state arbitrarily close to their initial state. The result applies to isolated mechanical systems subject to some constraints, e.g., all particles must be bound to a finite volume. Systems to which the Poincaré recurrence theorem applies are called conservative systems. The **Poincaré recurrence time** is the length of time elapsed until the recurrence. This time may vary greatly depending on the exact initial state and required degree of closeness.

The theorem is commonly discussed in the context of ergodic theory, dynamical systems and statistical mechanics. The theorem is named after Henri Poincaré, who discussed it in 1890. A proof was presented by Constantin Carathéodory using measure theory in 1919.

## Definitions and Poincaré's formulation

Any dynamical system defined by an ordinary differential equation determines a flow map *f* *t* mapping phase space to itself. Each point of the phase space describes the entire state of the system, typically the positions and velocities of all involved particles. The flow map tells us how the system evolves: if it starts in state *x*, then after time *t* the system will be in state *f* *t*(*x*). If we follow this point for all times *t*, we obtain the *orbit* of *x*. The system is said to be volume-preserving if the volume of each set in phase space is invariant under the flow. Poincaré's formulation of the theorem then states:

If a flow preserves volume and has only bounded orbits, then, for each

open set

, there is an orbit that intersects this open set infinitely often.

## Discussion, example and applications

We may think of the open set as tiny; the claim is that there will be orbits that return to this tiny set. (In fact, according to more modern formulations of the theorem given below, *almost all* orbits that start in the tiny set will return infinitely often.)

The assumption that all orbits be bounded is crucial: otherwise the orbits could "go off to infinity", never to return.

The other important assumption is that the system is volume-preserving. This is a common feature of physical systems when there is no friction or air resistance, no energy is pumped in and no energy is ever lost to heat. Technically, all Hamiltonian systems are volume-preserving because of Liouville's theorem. (Systems that don't preserve phase space volume and lose energy over time could start in a tiny open set and then slowly come to a standstill somewhere else, never to return.)

As an example of the theorem, consider a billiard table (without pockets) and a set of billiard balls, moving on the table without friction and undergoing completely elastic collisions with the cushions and the other balls. This ensures that no energy is ever lost and the flow preserves phase space volume. We can even allow for hills and valleys on the table. A point in phase space specifies the positions and velocities of all balls. If we impose a certain maximum total energy on the balls, then the system has bounded orbits and Poincaré's theorem applies. It states: when specifying the initial positions and velocities of all balls with arbitrary (but finite) precision, there will be orbits that start according to these specifications and that will return infinitely often to conditions that also accord with those specifications. Note however that not *all* orbits will necessarily return: it's possible to find orbits so finely tuned that some balls will slowly come to rest at the top of hills, never to return.

The Poincaré recurrence theorem has applications in statistical mechanics, dynamical systems, and ergodic theory. In statistical mechanics, it is used to predict the long-term behavior of isolated systems, such as gases confined to a finite volume, where the system is expected to return arbitrarily close to its initial state after sufficient length.

In the study of dynamical systems, the theorem applies to conservative systems and provides insight into recurrence properties of measure-preserving transformations. Related concepts also appear in ergodic theory, where recurrence plays a fundamental role in understanding the behavior of trajectories over time.

## Proof idea and further discussion

The qualitative proof hinges on two premises:

1. A finite upper bound can be set on the total potentially accessible phase space volume. For a mechanical system, this bound can be provided by requiring that the system is contained in a bounded *physical* region of space (so that it cannot, for example, eject particles that never return)–combined with the conservation of energy, this locks the system into a finite region in phase space.
2. The phase volume of a finite element under dynamics is conserved.

Imagine any finite starting volume D of the phase space and follow its path under the dynamics of the system. ("Finite" here means that the volume is positive.) The volume evolves through a "phase tube" in the phase space, keeping its size constant. Since the phase space if finite, after some number of steps $k_{1}$ the phase tube must intersect itself in some positive volume. Translating this intersection backwards in time, we find that at least a finite fraction of the starting volume is recurring.

Now, consider the size of the non-returning portion $D_{1}$ of the starting phase volume–that portion that never returns to the starting volume D . Using the principle in the last paragraph, we know that if $D_{1}$ is finite, then a finite part of it must return to $D_{1}$ after a number of steps, and therefore also returns to D . This contradicts the fact that all of $D_{1}$ is non-returning. We must conclude that the non-returning portion $D_{1}$ has volume 0.

The theorem does not comment on certain aspects of recurrence that this proof cannot guarantee:

- There may be some special phase space points that never return to the starting phase volume, or that only return to the starting volume a finite number of times then never return again. These are extremely "rare", making up an infinitesimal part of any starting volume.
- What *can* be said is that for "almost any" starting phase, a system shall eventually return arbitrarily close to that starting phase. The recurrence time varies as the required degree of closeness (the smallness of the phase volume).
- Not all parts of the phase volume need to return at the same time. Some "miss" the starting volume on the first pass, only to make their return later.
- Nothing prevents the phase tube from returning completely to its starting volume before all the possible phase volume is exhausted. A trivial example of this is the harmonic oscillator. Systems that do cover all accessible phase volume are called ergodic. (This of course depends on the definition of "accessible volume".)
- For a given phase in a volume, the recurrence is not necessarily periodic. The second recurrence time does not need to be double the first recurrence time.
- The theorem does not guarantee the existence of a *periodic orbit,* i.e. of a phase space point that exactly returns to itself after a certain amount of time.

## Formal statement

Let

$(X,\Sigma ,\mu )$

be a finite measure space (meaning $\Sigma$ is a σ-algebra on the set X and ${\displaystyle \mu$ is a measure) and let

$f\colon X\to X$

be a measure-preserving transformation (meaning for every $D\in \Sigma$ we have $f^{-1}(D)\in \Sigma$ and $\mu (f^{-1}(D))=\mu (D)$ ). Then the theorem claims:

For any $E\in \Sigma$ , the set of those points $x\in E$ for which there exists $N\in \mathbb {N}$ such that $f^{n}(x)\notin E$ for all $n>N$ has zero measure; i.e.

$\mu \left(\{x\in E:{\text{ there exists }}N{\text{ such that }}f^{n}(x)\notin E{\text{ for all }}n>N\}\right)=0.$

In other words, almost every point of E returns to E infinitely often*.*

## Quantum mechanical version

For time-independent quantum mechanical systems with discrete energy eigenstates, a similar theorem holds. For every $\varepsilon >0$ and $T_{0}>0$ there exists a time *T* larger than $T_{0}$ , such that $||\psi (T)\rangle -|\psi (0)\rangle |<\varepsilon$ , where $|\psi (t)\rangle$ denotes the state vector of the system at time *t*.

The essential elements of the proof are as follows. The system evolves in time according to:

$|\psi (t)\rangle =\sum _{n=0}^{\infty }c_{n}\exp(-iE_{n}t)|\phi _{n}\rangle$

where the $E_{n}$ are the energy eigenvalues (we use natural units, so $\hbar =1$ ), and the $|\phi _{n}\rangle$ are the energy eigenstates. The squared norm of the difference of the state vector at time *T* and time zero, can be written as:

$||\psi (T)\rangle -|\psi (0)\rangle |^{2}=2\sum _{n=0}^{\infty }|c_{n}|^{2}[1-\cos(E_{n}T)]$

We can truncate the summation at some *n* = *N* independent of *T*, because

$\sum _{n=N+1}^{\infty }|c_{n}|^{2}[1-\cos(E_{n}T)]\leq 2\sum _{n=N+1}^{\infty }|c_{n}|^{2}$

which can be made arbitrarily small by increasing *N*, as the summation $\sum _{n=0}^{\infty }|c_{n}|^{2}$ , being the squared norm of the initial state, converges to 1.

The finite sum

$\sum _{n=0}^{N}|c_{n}|^{2}[1-\cos(E_{n}T)]$

can be made arbitrarily small for specific choices of the time *T*, according to the following construction. Choose an arbitrary $\delta >0$ , and then choose *T* such that there are integers $k_{n}$ that satisfies

$|E_{n}T-2\pi k_{n}|<\delta$

,

for all numbers $0\leq n\leq N$ . For this specific choice of *T*,

$1-\cos(E_{n}T)<{\frac {\delta ^{2}}{2}}.$

As such, we have:

$2\sum _{n=0}^{N}|c_{n}|^{2}[1-\cos(E_{n}T)]<\delta ^{2}\sum _{n=0}^{N}|c_{n}|^{2}<\delta ^{2}$

.

The state vector $|\psi (T)\rangle$ thus returns arbitrarily close to the initial state $|\psi (0)\rangle$ .
