---
title: "Collision detection"
source: https://en.wikipedia.org/wiki/Collision_detection
domain: collision-detection-2d
license: CC-BY-SA-4.0
tags: collision detection, collision response, bounding volume, separating axis theorem
fetched: 2026-07-02
---

# Collision detection

**Collision detection** is the computational problem of detecting an intersection of two or more objects in virtual space. More precisely, it deals with the questions of *if*, *when,* and *where* two or more objects intersect. Collision detection is a classic problem of computational geometry with applications in computer graphics, physical simulation, video games, robotics (including autonomous driving), and computational physics. Collision detection algorithms can be divided into operating on 2D or 3D spatial objects.

## Overview

Collision detection is closely linked to calculating the distance between objects, as objects collide when the distance between them is less than or equal to zero. Negative distances indicate that one object has penetrated another. Performing collision detection requires more context than just the distance between the objects.

Accurately identifying the points of contact on both objects' surfaces is also essential for computing a physically accurate collision response. The complexity of this task increases with the level of detail in the objects' representations: the more intricate the model, the greater the computational cost.

Collision detection frequently involves dynamic objects, adding a temporal dimension to distance calculations. Instead of simply measuring distance between static objects, collision detection algorithms often aim to determine whether the objects' motion will bring them to a point in time when their distance is zero—an operation that adds significant computational overhead.

In collision detection involving multiple objects, a naive approach would require detecting collisions for all pairwise combinations of objects. As the number of objects increases, the number of required comparisons grows rapidly: for n objects, ${n(n-1)}/{2}$ intersection tests are needed with a naive approach. This quadratic growth makes such an approach computationally expensive as n increases.

Due to the complexity mentioned above, collision detection is a computationally intensive process. Nevertheless, it is essential for interactive applications like video games, robotics, and real-time physics engines. To manage these computational demands, extensive efforts have gone into optimizing collision detection algorithms.

A commonly used approach towards accelerating the required computations is to divide the process into two phases: the **broad phase** and the **narrow phase**. The broad phase aims to answer the question of whether objects might collide, using a conservative but efficient approach to rule out pairs that clearly do not intersect, thus avoiding unnecessary calculations.

Objects that cannot be definitively separated in the broad phase are passed to the narrow phase. Here, more precise algorithms determine whether these objects actually intersect. If they do, the narrow phase often calculates the exact time and location of the intersection.

## Broad phase

This phase aims at quickly finding objects or parts of objects for which it can be quickly determined that no further collision test is needed. A useful property of such approach is that it is output sensitive. In the context of collision detection this means that the time complexity of the collision detection is proportional to the number of objects that are close to each other. An early example of that is the I-COLLIDE where the number of required narrow phase collision tests was $O(n+m)$ where n is the number of objects and m is the number of objects at close proximity. This is a significant improvement over the quadratic complexity of the naive approach.

### Spatial partitioning

Several approaches can be grouped under the spatial partitioning umbrella, which includes octrees (for 3D), quadtrees (for 2D), binary space partitioning (or BSP trees) and other, similar approaches. If one splits space into a number of simple cells, and if two objects can be shown not to be in the same cell, then they need not be checked for intersection. Dynamic scenes and deformable objects require updating the partitioning which can add overhead.

### Bounding volume hierarchy

Bounding Volume Hierarchy (BVH) is a tree structure over a set of bounding volumes. Collision is determined by doing a tree traversal starting from the root. If the bounding volume of the root doesn't intersect with the object of interest, the traversal can be stopped. If, however there is an intersection, the traversal proceeds and checks the branches for each there is an intersection. Branches for which there is no intersection with the bounding volume can be culled from further intersection test. Therefore, multiple objects can be determined to not intersect at once. BVH can be used with deformable objects such as cloth or soft-bodies but the volume hierarchy has to be adjusted as the shape deforms. For deformable objects we need to be concerned about self-collisions or self intersections. BVH can be used for that end as well. Collision between two objects is computed by computing intersection between the bounding volumes of the root of the tree as there are collision we dive into the sub-trees that intersect. Exact collisions between the actual objects, or its parts (often triangles of a triangle mesh) need to be computed only between intersecting leaves. The same approach works for pair wise collision and self-collisions.

### Exploiting temporal coherence

During the broad-phase, when the objects in the world move or deform, the data-structures used to cull collisions have to be updated. In cases where the changes between two frames or time-steps are small and the objects can be approximated well with axis-aligned bounding boxes, the sweep and prune algorithm can be a suitable approach.

Several key observation make the implementation efficient: Two bounding-boxes intersect if, and only if, there is overlap along all three axes; overlap can be determined, for each axis separately, by sorting the intervals for all the boxes; and lastly, between two frames updates are typically small (making sorting algorithms optimized for almost-sorted lists suitable for this application). The algorithm keeps track of currently intersecting boxes, and as objects move, re-sorting the intervals helps keep track of the status.

### Pairwise pruning

Once a pair of physical bodies has been selected for further investigation, collisions need to be checked more carefully. However, in many applications, individual objects (if they are not too deformable) are described by a set of smaller primitives, mainly triangles. So there are two sets of triangles, $S={S_{1},S_{2},\dots ,S_{n}}$ and $T={T_{1},T_{2},\dots ,T_{n}}$ (for simplicity, each set has the same number of triangles.)

The obvious thing to do is to check all triangles $S_{j}$ against all triangles $T_{k}$ for collisions, but this involves $n^{2}$ comparisons, which is highly inefficient. If possible, it is desirable to use a pruning algorithm to reduce the number of pairs of triangles that need to be checked.

The most widely used family of algorithms is known as the *hierarchical bounding volumes* method. As a preprocessing step, for each object (e.g., S and T ) calculates a hierarchy of bounding volumes. Then, at each time step, when collisions need to be checked between S and T , the hierarchical bounding volumes are used to reduce the number of pairs of triangles under consideration. For simplicity, provide an example using bounding spheres, although it has been noted that spheres are undesirable in many cases.

If E is a set of triangles, a bounding sphere is pre-calculated. $B(E)$ . There are many ways of choosing $B(E)$ , $B(E)$ is a sphere that completely contains E and is as small as possible.

Ahead of time, $B(S)$ and $B(T)$ can be computed. Clearly, if these two spheres do not intersect (and that is very easy to test), then neither do S and T . This is not much better than an *n*-body pruning algorithm, however.

If $E={E_{1},E_{2},\dots ,E_{m}}$ is a set of triangles, then split it into two halves $L(E):={E_{1},E_{2},\dots ,E_{m/2}}$ and $R(E):={E_{m/2+1},\dots ,E_{m-1},E_{m}}$ . Apply this to S and T , and calculate (ahead of time) the bounding spheres $B(L(S)),B(R(S))$ and $B(L(T)),B(R(T))$ . The hope here is that these bounding spheres are much smaller than $B(S)$ and $B(T)$ . And, if, for instance, $B(S)$ and $B(L(T))$ do not intersect, then there is no sense in checking any triangle in S against any triangle in $L(T)$ .

As a precomputation, take each physical body (represented by a set of triangles) and recursively decompose it into a binary tree, where each node N represents a set of triangles, and its two children represent $L(N)$ and $R(N)$ . At each node in the tree, pre-compute the bounding sphere $B(N)$ .

When the time comes for testing a pair of objects for collision, their bounding sphere tree can be used to eliminate many pairs of triangles.

Many variants of the algorithms are obtained by choosing something other than a sphere for $B(T)$ . If one chooses axis-aligned bounding boxes, one gets AABBTrees. Oriented bounding box trees are called OBBTrees. Some trees are easier to update if the underlying object changes. Some trees can accommodate higher order primitives such as splines instead of simple triangles.

## Narrow phase

Objects that cannot be definitively separated in the broad phase are passed to the narrow phase. In this phase, the objects under consideration are relatively close to each other. Still, attempts to quickly determine if a full intersection is needed are employed first. This step is sometimes referred to as mid-phase. Once these tests passed (e.g. the pair of objects may be colliding) more precise algorithms determine whether these objects actually intersect. If they do, the narrow phase often calculates the exact time and location of the intersection.

### Bounding volumes

Since checking whether two objects intersect can be a relatively expensive operation, one quick way to potentially avoid the computation is to check whether the bounding volumes enclosing the two objects intersect. Bounding volumes are typically used in the early (pruning) stage of collision detection, so that only objects with overlapping volumes need be compared in detail. If they don't overlap, there is no need to check the actual objects. Computing overlap or collision between bounding volumes involves additional computations, so in order for the bounding-volume test to add value: a) the cost of intersecting the bounding volume needs to be low and b) the bounding volume needs to be tight enough so that the number of 'false positive' intersections will be low. A false positive intersection in this case means that the bounding volumes intersect but the actual objects do not. Different bounding volume types offer different trade-offs for these properties.

Axis-Align Bounding Boxes (AABB) and cuboids are popular due to their simplicity and quick intersection tests. Bounding volumes such as Oriented Bounding Boxes (OBB), K-DOPs and Convex-hulls offer a tighter approximation of the enclosed shape at the expense of a more elaborate intersection test.

### Exact pairwise collision detection

Objects for which pruning approaches could not rule out the possibility of a collision have to undergo an exact collision detection computation.

#### Collision detection between convex objects

According to the separating planes theorem, for any two disjoint convex objects, there exists a plane so that one object lies completely on one side of that plane, and the other object lies on the opposite side of that plane. This property allows the development of efficient collision detection algorithms between convex objects. Several algorithms are available for finding the closest points on the surface of two convex polyhedral objects - and determining collision. Early work by Ming C. Lin that used a variation on the simplex algorithm from linear programming and the Gilbert-Johnson-Keerthi distance algorithm are two such examples. These algorithms approach constant time when applied repeatedly to pairs of stationary or slow-moving objects, and every step is initialized from the previous collision check.

The result of all this algorithmic work is that collision detection can be done efficiently for thousands of moving objects in real time on typical personal computers and game consoles.

### A priori pruning

Where most of the objects involved are fixed, as is typical of video games, a priori methods using precomputation can be used to speed up execution.

Pruning is also desirable here, both *n*-body pruning and pairwise pruning, but the algorithms must take time and the types of motions used in the underlying physical system into consideration.

When it comes to the exact pairwise collision detection, this is highly trajectory dependent, and one almost has to use a numerical root-finding algorithm to compute the instant of impact.

As an example, consider two triangles moving in time ${v_{1}(t),v_{2}(t),v_{3}(t)}$ and ${v_{4}(t),v_{5}(t),v_{6}(t)}$ . At any point in time, the two triangles can be checked for intersection using the twenty planes previously mentioned. If $P(u,v,w)$ is the plane going through points $u,v,w$ in $\mathbb {R} ^{3}$ then there are twenty planes $P(v_{i}(t),v_{j}(t),v_{k}(t))$ to track. Each plane needs to be tracked against three vertices, this gives sixty values to track. Using a root finder on these sixty functions produces the exact collision times for the two given triangles and the two given trajectory. If the trajectories of the vertices are assumed to be linear polynomials in t then the final sixty functions are in fact cubic polynomials, and in this exceptional case, it is possible to locate the exact collision time using the formula for the roots of the cubic. Some numerical analysts suggest that using the formula for the roots of the cubic is not as numerically stable as using a root finder for polynomials.

### Triangle centroid segments

A triangle mesh object is commonly used in 3D body modeling. Normally the collision function is a triangle to triangle intercept or a bounding shape associated with the mesh. A triangle centroid is a center of mass location such that it would balance on a pencil tip. The simulation need only add a centroid dimension to the physics parameters. Given centroid points in both object and target it is possible to define the line segment connecting these two points.

The position vector of the centroid of a triangle is the average of the position vectors of its vertices. So if its vertices have Cartesian coordinates $(x_{1},y_{1},z_{1})$ , $(x_{2},y_{2},z_{2})$ and $(x_{3},y_{3},z_{3})$ then the centroid is $\left({\frac {(x_{1}+x_{2}+x_{3})}{3}},{\frac {(y_{1}+y_{2}+y_{3})}{3}},{\frac {(z_{1}+z_{2}+z_{3})}{3}}\right)$ .

Here is the function for a line segment distance between two 3D points. $\mathrm {distance} ={\sqrt {(z_{2}-z_{1})^{2}+(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}}$

Here the length/distance of the segment is an adjustable "hit" criteria size of segment. As the objects approach the length decreases to the threshold value. A triangle sphere becomes the effective geometry test. A sphere centered at the centroid can be sized to encompass all the triangle's vertices.

## Usage

### Collision detection in computer simulation

Physical simulators differ in the way they react on a collision. Some use the softness of the material to calculate a force, which will resolve the collision in the following time steps like it is in reality. This is very CPU intensive for low softness materials. Some simulators estimate the time of collision by linear interpolation, roll back the simulation, and calculate the collision by the more abstract methods of conservation laws.

Some iterate the linear interpolation (Newton's method) to calculate the time of collision with a much higher precision than the rest of the simulation. Collision detection utilizes time coherence to allow even finer time steps without much increasing CPU demand, such as in air traffic control.

After an inelastic collision, special states of sliding and resting can occur and, for example, the Open Dynamics Engine uses constraints to simulate them. Constraints avoid inertia and thus instability. Implementation of rest by means of a scene graph avoids drift.

In other words, physical simulators usually function one of two ways: where the collision is detected *a posteriori* (after the collision occurs) or *a priori* (before the collision occurs). In addition to the *a posteriori* and *a priori* distinction, almost all modern collision detection algorithms are broken into a hierarchy of algorithms. Often the terms "discrete" and "continuous" are used rather than *a posteriori* and *a priori*.

#### *A posteriori* (discrete) versus *a priori* (continuous)

In the *a posteriori* case, the physical simulation is advanced by a small step, then checked to see if any objects are intersecting or visibly considered intersecting. At each simulation step, a list of all intersecting bodies is created, and the positions and trajectories of these objects are "fixed" to account for the collision. This method is called *a posteriori* because it typically misses the actual instant of collision, and only catches the collision after it has actually happened.

In the *a priori* methods, there is a collision detection algorithm which will be able to predict very precisely the trajectories of the physical bodies. The instants of collision are calculated with high precision, and the physical bodies never actually interpenetrate. This is called *a priori* because the collision detection algorithm calculates the instants of collision before it updates the configuration of the physical bodies.

The main benefits of the *a posteriori* methods are as follows. In this case, the collision detection algorithm need not be aware of the myriad of physical variables; a simple list of physical bodies is fed to the algorithm, and the program returns a list of intersecting bodies. The collision detection algorithm doesn't need to understand friction, elastic collisions, or worse, nonelastic collisions and deformable bodies. In addition, the *a posteriori* algorithms are in effect one dimension simpler than the *a priori* algorithms. An *a priori* algorithm must deal with the time variable, which is absent from the *a posteriori* problem.

On the other hand, *a posteriori* algorithms cause problems in the "fixing" step, where intersections (which aren't physically correct) need to be corrected. Moreover, if the discrete step is too large, the collision could go undetected, resulting in an object which passes through another if it is sufficiently fast or small.

The benefits of the *a priori* algorithms are increased fidelity and stability. It is difficult (but not completely impossible) to separate the physical simulation from the collision detection algorithm. However, in all but the simplest cases, the problem of determining ahead of time when two bodies will collide (given some initial data) has no closed form solution—a numerical root finder is usually involved.

Some objects are in *resting contact*, that is, in collision, but neither bouncing off, nor interpenetrating, such as a vase resting on a table. In all cases, resting contact requires special treatment: If two objects collide (*a posteriori*) or slide (*a priori*) and their relative motion is below a threshold, friction becomes stiction and both objects are arranged in the same branch of the scene graph.

### Video games

Video games have to split their very limited computing time between several tasks. Despite this resource limit, and the use of relatively primitive collision detection algorithms, programmers have been able to create believable, if inexact, systems for use in games.

For a long time, video games had a very limited number of objects to treat, and so checking all pairs was not a problem. In two-dimensional games, in some cases, the hardware was able to efficiently detect and report overlapping pixels between sprites on the screen. In other cases, simply tiling the screen and binding each *sprite* into the tiles it overlaps provides sufficient pruning, and for pairwise checks, bounding rectangles or circles called hitboxes are used and deemed sufficiently accurate.

Three-dimensional games have used spatial partitioning methods for n -body pruning, and for a long time used one or a few spheres per actual 3D object for pairwise checks. Exact checks are very rare, except in games attempting to simulate reality closely. Even then, exact checks are not necessarily used in all cases.

Because games do not need to mimic actual physics, stability is not as much of an issue. Almost all games use *a posteriori* collision detection, and collisions are often resolved using very simple rules. For instance, if a character becomes embedded in a wall, they might be simply moved back to their last known good location. Some games will calculate the distance the character can move before getting embedded into a wall, and only allow them to move that far.

In many cases for video games, approximating the characters by a point is sufficient for the purpose of collision detection with the environment. In this case, binary space partitioning trees provide a viable, efficient and simple algorithm for checking if a point is embedded in the scenery or not. Such a data structure can also be used to handle "resting position" situation gracefully when a character is running along the ground. Collisions between characters, and collisions with projectiles and hazards, are treated separately.

A robust simulator is one that will react to any input in a reasonable way. For instance, imagining a high speed racecar video game, it is conceivable that the cars would advance a substantial distance along the race track from one simulation step to the next. If there is a shallow obstacle on the track (such as a brick wall), it is not entirely unlikely that the car will completely leap over it, and this is very undesirable. In other instances, the "fixing" that posteriori algorithms require isn't implemented correctly, resulting in bugs that can trap characters in walls or allow them to pass through them and fall into an endless void where there may or may not be a deadly bottomless pit, sometimes referred to as "black hell", "blue hell", or "green hell", depending on the predominant color. These are the hallmarks of a failing collision detection and physical simulation system. *Big Rigs: Over the Road Racing* is an infamous example of a game with a failing or possibly missing collision detection system.

#### Hitbox

A **hitbox** is an invisible shape commonly used in video games for real-time collision detection; it is a type of bounding box. It is often a rectangle (in 2D games) or cuboid (in 3D) that is attached to and follows a point on a visible object (such as a model or a sprite). Circular or spheroidial shapes are also common, though they are still most often called "boxes". It is common for animated objects to have hitboxes attached to each moving part to ensure accuracy during motion.

Hitboxes are used to detect "one-way" collisions such as a character being hit by a punch or a bullet. They are unsuitable for the detection of collisions with feedback (e.g. bumping into a wall) due to the difficulty experienced by both humans and AI in managing a hitbox's ever-changing locations; these sorts of collisions are typically handled with much simpler axis-aligned bounding boxes instead. Players may use the term "hitbox" to refer to these types of interactions regardless.

A **hurtbox** is a hitbox used to detect incoming sources of damage. In this context, the term *hitbox* is typically reserved for those which deal damage. For example, an attack may only land if the hitbox around an attacker's punch connects with one of the opponent's hurtboxes on their body, while opposing hitboxes colliding may result in the players trading or cancelling blows, and opposing hurtboxes do not interact with each other. The term is not standardized across the industry; some games reverse their definitions of *hitbox* and *hurtbox*, while others only use "hitbox" for both sides.
