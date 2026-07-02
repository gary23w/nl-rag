---
title: "Ragdoll physics"
source: https://en.wikipedia.org/wiki/Ragdoll_physics
domain: ragdoll-physics
license: CC-BY-SA-4.0
tags: ragdoll physics, ragdoll simulation, articulated body physics, physics-driven character
fetched: 2026-07-02
---

# Ragdoll physics

**Ragdoll physics** is a type of procedural animation used by physics engines, which is often used as a replacement for traditional static death animations in video games and animated films. As computers increased in power, it became possible to do limited real-time physical simulations, which made death animations more realistic.

Early video games used manually created animations for a character’s death sequences. This had the advantage of low CPU utilization, as the data needed to animate a "dying" character was chosen from a set number of pre-drawn frames. In contrast, a ragdoll is a collection of multiple rigid bodies (each of which is ordinarily tied to a bone in the graphics engine's skeletal animation system) tied together by a system of constraints that restrict how the bones may move relative to each other. When the character dies, their body begins to collapse to the ground, honouring these restrictions on each of the joints' motion, which often looks more realistic.

The term *ragdoll* comes from the problem that the articulated systems, due to the limits of the solvers used, tend to have little or zero joint/skeletal muscle stiffness, leading to a character collapsing much like a toy rag doll, often into comically improbable or compromising positions. Modern use of ragdoll physics goes beyond death sequences.

## History

The *Jurassic Park* licensed game *Jurassic Park: Trespasser* exhibited ragdoll physics in 1998 but received very polarised opinions; most were negative, as the game had a large number of bugs. It was remembered, however, for being a pioneer in video game physics.

There are fighting games where the player controls one part of the body of the fighter and the rest follows along, such as *Rag Doll Kung Fu*, as well as racing games such as the *FlatOut* series.

Recent procedural animation technologies, such as those found in NaturalMotion's Euphoria software, have allowed the development of games that rely heavily on the suspension of disbelief facilitated by realistic whole-body muscle/nervous ragdoll physics as an integral part of the immersive gaming experience, as opposed to the antiquated use of canned-animation techniques. This is seen in *Grand Theft Auto IV*, *Grand Theft Auto V*, *Red Dead Redemption*, *Max Payne 3* and *Red Dead Redemption 2* as well as titles such as LucasArts' *Star Wars: The Force Unleashed* and *Puppet Army Faction's Kontrol*, which feature 2D powered ragdoll locomotion on uneven or moving surfaces.

## Approaches

Ragdolls have been implemented using Featherstone's algorithm and spring-damper contacts. An alternative approach uses constraint solvers and idealized contacts. While the constrained-rigid-body approach to ragdolls is the most common, other "pseudo-ragdoll" techniques have been used:

- Verlet integration: used by *Hitman: Codename 47* and popularized by Thomas Jakobsen, this technique models each character bone as a point connected to an arbitrary number of other points via simple constraints. Verlet constraints are much simpler and faster to solve than most of those in a fully modelled rigid body system, resulting in much less CPU consumption for characters.
- Inverse kinematics post-processing: used in *Halo: Combat Evolved*, this technique relies on playing a pre-set death animation and then using inverse kinematics to force the character into a possible position after the animation has completed. This means that, during an animation, a character could wind up clipping through world geometry, but after it has come to rest, all of its bones will be in valid space. Limitations can force body parts to move through each other in unnatural ways; for instance, a character's hand may lay on top of their chest in a death animation, but the hand is then moved through the chest to the ground underneath by inverse kinematics.
- Blended ragdoll: this technique was used in *Halo 2*, *Halo 3*, *Call of Duty 4: Modern Warfare*, *Left 4 Dead*, *Medal of Honor: Airborne*, *Team Fortress 2*, and *Uncharted: Drake's Fortune.* It works by playing a pre-made animation, then binding the ragdoll to the last frame of the animation. Occasionally the ragdolling player model will appear to stretch out and spin around in multiple directions, as though the character were made of rubber. This erratic behavior has been observed to occur in games that use certain versions of the Havok engine, such as *Halo 2* and *Fable II*.
- Active ragdoll: used primarily in *Unreal Engine* games such as *Unreal Tournament 3* and *Killing Floor 2*. It works by playing a pre-made animation, but constraining the output of that animation to what a physical system would allow. This helps alleviate the ragdoll feeling of characters suddenly going limp, offering correct environmental interaction as well. This requires both animation processing and physics processing, thus making it even slower than a traditional ragdoll alone, though the benefits of the extra visuals seem to overshadow the reduction in processing speed. See also: *Euphoria (software)*
- Procedural animation: traditionally used in non-realtime media (film/TV/etc), this technique (used in the Medal of Honor series starting from European Assault onward) employs the use of multi-layered physical models in non-playing characters (bones / muscle / nervous systems), and deformable scenic elements from "simulated materials" in vehicles, etc. By removing the use of pre-made animation, each reaction seen by the player is unique, whilst still deterministic.
