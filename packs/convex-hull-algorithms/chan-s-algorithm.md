---
title: "Chan's algorithm"
source: https://en.wikipedia.org/wiki/Chan's_algorithm
domain: convex-hull-algorithms
license: CC-BY-SA-4.0
tags: convex hull algorithm, graham scan, quickhull method, gift wrapping
fetched: 2026-07-02
---

# Chan's algorithm

In computational geometry, **Chan's algorithm**, named after Timothy M. Chan, is an optimal output-sensitive algorithm to compute the convex hull of a set P of n points, in 2- or 3-dimensional space. The algorithm takes $O(n\log h)$ time, where h is the number of vertices of the output (the convex hull). In the planar case, the algorithm combines an $O(n\log n)$ algorithm (Graham scan, for example) with Jarvis march ( $O(nh)$ ), in order to obtain an optimal $O(n\log h)$ time. Chan's algorithm is notable because it is much simpler than the Kirkpatrick–Seidel algorithm, and it naturally extends to 3-dimensional space. This paradigm has been independently developed by Frank Nielsen in his Ph.D. thesis.

## Algorithm

### Overview

A single pass of the algorithm requires a parameter m which is between 0 and n (number of points of our set P ). Ideally, $m=h$ but h , the number of vertices in the output convex hull, is not known at the start. Multiple passes with increasing values of m are done which then terminates when $m\geq h$ . See below on choosing parameter m .

The algorithm starts by arbitrarily partitioning the set of points P into $K=\lceil n/m\rceil$ subsets $(Q_{k})_{k=1,2,...K}$ with at most m points each; notice that $K=O(n/m)$ .

For each subset $Q_{k}$ , it computes the convex hull, $C_{k}$ , using an $O(p\log p)$ algorithm (for example, Graham scan), where p is the number of points in the subset. As there are K subsets of $O(m)$ points each, this phase takes $K\cdot O(m\log m)=O(n\log m)$ time.

During the second phase, Jarvis's march is executed, making use of the precomputed (mini) convex hulls, $(C_{k})_{k=1,2,...K}$ . At each step in this Jarvis's march algorithm, we have a point $p_{i}$ in the convex hull (at the beginning, $p_{i}$ may be the point in P with the lowest y coordinate, which is guaranteed to be in the convex hull of P ), and need to find a point $p_{i+1}=f(p_{i},P)$ such that all other points of P are to the right of the line $p_{i}p_{i+1}$ , where the notation $p_{i+1}=f(p_{i},P)$ simply means that the next point, that is $p_{i+1}$ , is determined as a function of $p_{i}$ and P . The convex hull of the set $Q_{k}$ , $C_{k}$ , is known and contains at most m points (listed in a clockwise or counter-clockwise order), which allows to compute $f(p_{i},Q_{k})$ in $O(\log m)$ time by binary search. Hence, the computation of $f(p_{i},Q_{k})$ for all the K subsets can be done in $O(K\log m)$ time. Then, we can determine $f(p_{i},P)$ using the same technique as normally used in Jarvis's march, but only considering the points $(f(p_{i},Q_{k}))_{1\leq k\leq K}$ (i.e. the points in the mini convex hulls) instead of the whole set P . For those points, one iteration of Jarvis's march is $O(K)$ which is negligible compared to the computation for all subsets. Jarvis's march completes when the process has been repeated $O(h)$ times (because, in the way Jarvis march works, after at most h iterations of its outermost loop, where h is the number of points in the convex hull of P , we must have found the convex hull), hence the second phase takes $O(Kh\log m)$ time, equivalent to $O(n\log h)$ time if m is close to h (see below the description of a strategy to choose m such that this is the case).

By running the two phases described above, the convex hull of n points is computed in $O(n\log h)$ time.

### Choosing the parameter *m*

If an arbitrary value is chosen for m , it may happen that $m<h$ . In that case, after m steps in the second phase, we interrupt the Jarvis's march as running it to the end would take too much time. At that moment, $O(n\log m)$ time will have been spent, and the convex hull will not have been calculated.

The idea is to make multiple passes of the algorithm with increasing values of m ; each pass terminates (successfully or unsuccessfully) in $O(n\log m)$ time. If m increases too slowly between passes, the number of iterations may be large; on the other hand, if it rises too quickly, the first m for which the algorithm terminates successfully may be much larger than h , and produce a complexity $O(n\log m)>O(n\log h)$ .

#### Squaring Strategy

One possible strategy is to *square* the value of m at each iteration, up to a maximum value of n (corresponding to a partition in singleton sets). Starting from a value of 2, at iteration t , $m=\min \left(n,2^{2^{t}}\right)$ is chosen. In that case, $O(\log \log h)$ iterations are made, given that the algorithm terminates once we have

$m=2^{2^{t}}\geq h\iff \log \left(2^{2^{t}}\right)\geq \log h\iff 2^{t}\geq \log h\iff \log {2^{t}}\geq \log {\log h}\iff t\geq \log {\log h},$

with the logarithm taken in base 2 , and the total running time of the algorithm is

$\sum _{t=0}^{\lceil \log \log h\rceil }O\left(n\log \left(2^{2^{t}}\right)\right)=O(n)\sum _{t=0}^{\lceil \log \log h\rceil }2^{t}=O\left(n\cdot 2^{1+\lceil \log \log h\rceil }\right)=O(n\log h).$

### In three dimensions

To generalize this construction for the 3-dimensional case, an $O(n\log n)$ algorithm to compute the 3-dimensional convex hull by Preparata and Hong should be used instead of Graham scan, and a 3-dimensional version of Jarvis's march needs to be used. The time complexity remains $O(n\log h)$ .

### Pseudocode

In the following pseudocode, text between parentheses and in italic are comments. To fully understand the following pseudocode, it is recommended that the reader is already familiar with Graham scan and Jarvis march algorithms to compute the convex hull, C , of a set of points, P .

Input:

Set

P

with

n

points .

Output:

Set

C

with

h

points, the convex hull of

P

.

(Pick a point of

P

which is guaranteed to be in

C

: for instance, the point with the lowest y coordinate.)

(This operation takes

${\mathcal {O}}(n)$

time: e.g., we can simply iterate through

P

.)

$p_{1}:=PICK\_START(P)$

(

$p_{0}$

is used in the Jarvis march part of this Chan's algorithm,

so that to compute the second point,

$p_{2}$

, in the convex hull of

P

.)

(Note:

$p_{0}$

is

not

a point of

P

.)

(For more info, see the comments close to the corresponding part of the Chan's algorithm.)

$p_{0}:=(-\infty ,0)$

(Note:

h

, the number of points in the final convex hull of

P

, is

not

known.)

(These are the iterations needed to discover the value of

m

, which is an estimate of

h

.)

(

$h\leq m$

is required for this Chan's algorithm to find the convex hull of

P

.)

(More specifically, we want

$h\leq m\leq h^{2}$

, so that not to perform too many unnecessary iterations

and so that the time complexity of this Chan's algorithm is

${\mathcal {O}}(n\log h)$

.)

(As explained above in this article, a strategy is used where at most

$\log \log n$

iterations are required to find

m

.)

(Note: the final

m

may not be equal to

h

, but it is never smaller than

h

and greater than

$h^{2}$

.)

(Nevertheless, this Chan's algorithm stops once

h

iterations of the outermost loop are performed,

that is, even if

$m\neq h$

, it doesn't perform

m

iterations of the outermost loop.)

(For more info, see the Jarvis march part of this algorithm below, where

C

is returned if

$p_{i+1}==p_{1}$

.)

for

$1\leq t\leq \log \log n$

do

(Set parameter

m

for the current iteration. A "squaring scheme" is used as described above in this article.

There are other schemes: for example, the "doubling scheme", where

$m=2^{t}$

, for

$t=1,\dots ,\left\lceil \log h\right\rceil$

.

If the "doubling scheme" is used, though, the resulting time complexity of this Chan's algorithm is

${\mathcal {O}}(n\log ^{2}h)$

.)

$m:=2^{2^{t}}$

(Initialize an empty list (or array) to store the points of the convex hull of

P

, as they are found.)

$C:=()$

$ADD(C,p_{1})$

(Arbitrarily split set of points

P

into

$K=\left\lceil {\frac {n}{m}}\right\rceil$

subsets of roughly

m

elements each.)

$Q_{1},Q_{2},\dots ,Q_{K}:=SPLIT(P,m)$

(Compute the convex hull of all

K

subsets of points,

$Q_{1},Q_{2},\dots ,Q_{K}$

.)

(It takes

${\mathcal {O}}(Km\log m)={\mathcal {O}}(n\log m)$

time.)

If

$m\leq h^{2}$

, then the time complexity is

${\mathcal {O}}(n\log h^{2})={\mathcal {O}}(n\log h)$

.)

for

$1\leq k\leq K$

do

(Compute the convex hull of subset

k

,

$Q_{k}$

, using Graham scan, which takes

${\mathcal {O}}(m\log m)$

time.)

(

$C_{k}$

is the convex hull of the subset of points

$Q_{k}$

.)

$C_{k}:=GRAHAM\_SCAN(Q_{k})$

(At this point, the convex hulls

$C_{1},C_{2},\dots ,C_{K}$

of respectively the subsets of points

$Q_{1},Q_{2},\dots ,Q_{K}$

have been computed.)

(Now, use a

modified version

of the

Jarvis march

algorithm to compute the convex hull of

P

.)

(Jarvis march performs in

${\mathcal {O}}(nh)$

time, where

n

is the number of input points and

h

is the number of points in the convex hull.)

(Given that Jarvis march is an

output-sensitive algorithm

, its running time depends on the size of the convex hull,

h

.)

(In practice, it means that Jarvis march performs

h

iterations of its outermost loop.

At each of these iterations, it performs at most

n

iterations of its innermost loop.)

(We want

$h\leq m\leq h^{2}$

, so we do not want to perform more than

m

iterations in the following outer loop.)

(If the current

m

is smaller than

h

, i.e.

$m<h$

, the convex hull of

P

cannot be found.)

(In this modified version of Jarvis march, we perform an operation inside the innermost loop which takes

${\mathcal {O}}(\log m)$

time.

Hence, the total time complexity of this modified version is

${\mathcal {O}}(mK\log m)={\mathcal {O}}(m\left\lceil {\frac {n}{m}}\right\rceil \log m)={\mathcal {O}}(n\log m)={\mathcal {O}}(n\log 2^{2^{t}})={\mathcal {O}}(n2^{t}).$

If

$m\leq h^{2}$

, then the time complexity is

${\mathcal {O}}(n\log h^{2})={\mathcal {O}}(n\log h)$

.)

for

$1\leq i\leq m$

do

(Note: here, a point in the convex hull of

P

is already known, that is

$p_{1}$

.)

(In this inner

for

loop,

K

possible next points to be on the convex hull of

P

,

$q_{i,1},q_{i,2},\dots ,q_{i,K}$

, are computed.)

(Each of these

K

possible next points is from a different

$C_{k}$

:

that is,

$q_{i,k}$

is a possible next point on the convex hull of

P

which is part of the convex hull of

$C_{k}$

.)

(Note:

$q_{i,1},q_{i,2},\dots ,q_{i,K}$

depend on

i

: that is, for each iteration

i

, there are

K

possible next points to be on the convex hull of

P

.)

(Note: at each iteration

i

, only one of the points among

$q_{i,1},q_{i,2},\dots ,q_{i,K}$

is added to the convex hull of

P

.)

for

$1\leq k\leq K$

do

(

$JARVIS\_BINARY\_SEARCH$

finds the point

$d\in C_{k}$

such that the angle

$\measuredangle p_{i-1}p_{i}d$

is maximized

,

where

$\measuredangle p_{i-1}p_{i}d$

is the angle between the vectors

${\overrightarrow {p_{i}p_{i-1}}}$

and

${\overrightarrow {p_{i}d}}$

. Such

d

is stored in

$q_{i,k}$

.)

(Angles do not need to be calculated directly: the

orientation test

can be used

.)

(

$JARVIS\_BINARY\_SEARCH$

can be performed in

${\mathcal {O}}(\log m)$

time

.)

(Note: at the iteration

$i=1$

,

$p_{i-1}=p_{0}=(-\infty ,0)$

and

$p_{1}$

is known and is a point in the convex hull of

P

:

in this case, it is the point of

P

with the lowest y coordinate.)

$q_{i,k}:=JARVIS\_BINARY\_SEARCH(p_{i-1},p_{i},C_{k})$

(Choose the point

$z\in \{q_{i,1},q_{i,2},\dots ,q_{i,K}\}$

which maximizes the angle

$\measuredangle p_{i-1}p_{i}z$

to be the next point on the convex hull of

P

.)

$p_{i+1}:=JARVIS\_NEXT\_CH\_POINT(p_{i-1},p_{i},(q_{i,1},q_{i,2},\dots ,q_{i,K}))$

(Jarvis march terminates when the next selected point on the convext hull,

$p_{i+1}$

, is the initial point,

$p_{1}$

.)

if

$p_{i+1}==p_{1}$

(Return the convex hull of

P

which contains

$i=h$

points.)

(Note: of course, no need to return

$p_{i+1}$

which is equal to

$p_{1}$

.)

return

$C:=(p_{1},p_{2},\dots ,p_{i})$

else

$ADD(C,p_{i+1})$

(If after

m

iterations a point

$p_{i+1}$

has not been found so that

$p_{i+1}==p_{1}$

, then

$m<h$

.)

(We need to start over with a higher value for

m

.)

## Implementation

Chan's paper contains several suggestions that may improve the practical performance of the algorithm, for example:

- When computing the convex hulls of the subsets, eliminate the points that are not in the convex hull from consideration in subsequent executions.
- The convex hulls of larger point sets can be obtained by merging previously calculated convex hulls, instead of recomputing from scratch.
- With the above idea, the dominant cost of algorithm lies in the pre-processing, i.e., the computation of the convex hulls of the groups. To reduce this cost, we may consider reusing hulls computed from the previous iteration and merging them as the group size is increased.

## Extensions

Chan's paper contains some other problems whose known algorithms can be made optimal output sensitive using his technique, for example:

- Computing the lower envelope $L(S)$ of a set S of n line segments, which is defined as the lower boundary of the unbounded trapezoid of formed by the intersections.
- Hershberger gave an $O(n\log n)$ algorithm which can be sped up to $O(n\log h)$ , where h is the number of edges in the envelope

- Constructing output sensitive algorithms for higher dimensional convex hulls. With the use of grouping points and using efficient data structures, $O(n\log h)$ complexity can be achieved provided h is of polynomial order in n .
