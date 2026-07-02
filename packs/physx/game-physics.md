---
title: "Game physics"
source: https://en.wikipedia.org/wiki/Game_physics
domain: physx
license: CC-BY-SA-4.0
tags: physx engine, nvidia physx, gpu physics, physx rigid body
fetched: 2026-07-02
---

# Game physics

**Computer animation physics** or **game physics** are laws of physics as they are defined within a simulation or video game, and the programming logic used to implement these laws. Game physics vary greatly in their degree of similarity to real-world physics. Sometimes, the physics of a game may be designed to mimic the physics of the real world as accurately as is feasible, in order to appear realistic to the player or observer. In other cases, games may intentionally deviate from actual physics for gameplay purposes. Common examples in platform games include the ability to start moving horizontally or change direction in mid-air and the double jump ability found in some games. Setting the values of physical parameters, such as the amount of gravity present, is also a part of defining the game physics of a particular game.

There are several elements that form components of simulation physics including the physics engine, program code that is used to simulate Newtonian physics within the environment, and collision detection, used to solve the problem of determining when any two or more physical objects in the environment cross each other's path.

## Physics simulations

There are two central types of physics simulations: rigid body and soft-body simulators. In a rigid body simulation objects are grouped into categories based on how they should interact and are less performance intensive. Soft-body physics involves simulating individual sections of each object such that it behaves in a more realistic way.

## Particle systems

A common aspect of computer games that model some type of conflict is the explosion. Early computer games used the simple expedient of repeating the same explosion in each circumstance. However, in the real world an explosion can vary depending on the terrain, altitude of the explosion, and the type of solid bodies being impacted. Depending on the processing power available, the effects of the explosion can be modeled as the split and shattered components propelled by the expanding gas. This is modelled by means of a particle system simulation. A particle system model allows a variety of other physical phenomena to be simulated, including smoke, moving water, precipitation, and so forth. The individual particles within the system are modelled using the other elements of the physics simulation rules, with the limitation that the number of particles that can be simulated is restricted by the computing power of the hardware. Thus explosions may need to be modelled as a small set of large particles, rather than the more accurate huge number of fine particles.

## Ragdoll physics

This is a procedural animation and simulation technique to display the movement of a character when killed. It treats the character's body as a series of rigid bones connected together with hinges at the joints. The simulation models what happens to the body as it collapses to the ground. More sophisticated physics models of creature movement and collision interactions require greater level of computing power and a more accurate simulation of solids, liquids, and hydrodynamics. The modelled articulated systems can then reproduce the effects of skeleton, muscles, tendons, and other physiological components. Some games, such as Boneworks and Half-Life 2, apply forces to individual joints that allow ragdolls to move and behave like humanoids with fully procedural animations. This allows to, for example, knock an enemy down or grab each individual joint and move it around and the physics-based animation would adapt accordingly, which wouldn't be possible with conventional means. This method is called active ragdolls and is often used in combination with inverse kinematics.

## Projectiles

Projectiles, such as arrows or bullets, often travel at very high speeds. This creates problems with collisions - sometimes the projectile travels so fast that it simply goes past a thin object without ever detecting that it has collided with it. Before, this was solved with ray-casting, which does not require the creation of a physical projectile. However, simply shooting a ray in the direction that the weapon is aiming at is not particularly realistic, which is why modern games often create a physical projectile that can be affected by gravity and other forces. This projectile uses a form of continuous collision detection to make sure that the above-stated problem will not occur (at the cost of inferior performance), since more complex calculations are required to perform such a task.

Games such as FIFA 14 require accurate projectile physics for objects such as the soccer ball. In FIFA 14, developers were required to fix code related to the drag coefficient which was inaccurate in previous games, leading to a much more realistic simulation of a real ball.

## Books

- *Eberly, David H. (2003). *Game Physics*. Morgan Kaufmann. ISBN 978-1-55860-740-8.*
- *Millington, Ian (2007). *Game Physics Engine Development*. Morgan Kaufmann. ISBN 978-0-12-369471-3.*
- *Bourg, David M. (2001). *Physics for Game Developers*. O'Reilly Media. ISBN 978-0-596-00006-6.*
- *Szauer, Gabor (2017). *Game Physics Cookbook*. Packt Publishing. ISBN 978-1787123663.*
- *Conger, David (2004). *Physics Modeling for Game Programmers*. Course Technology PTR. ISBN 978-1592000937.*
