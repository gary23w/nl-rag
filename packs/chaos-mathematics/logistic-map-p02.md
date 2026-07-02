---
title: "Logistic map (part 2/4)"
source: https://en.wikipedia.org/wiki/Logistic_map
domain: chaos-mathematics
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
part: 2/4
---

## Characterization of the logistic map

The animation shows the behaviour of the sequence $x_{n}$ over different values of the parameter r. A first observation is that the sequence does not diverge and remains finite for r between 0 and 4. It is possible to see the following qualitative phenomena in order of time:

- exponential convergence to zero
- convergence to a non-zero fixed value (see Exponential function or Characterizations of the exponential function point 4)
- initial oscillation and then convergence (see Damping and Damped harmonic oscillator)
- stable oscillations between two values (see Resonance and Simple harmonic oscillator)
- growing oscillations between a set of values which are multiples of two such as 2,4,8,16 etc. (see Period-doubling bifurcation)
- Intermittency (i.e. sprouts of oscillations at the onset of chaos)
- fully developed chaotic oscillations
- topological mixing (i.e. the tendency of oscillations to cover the full available space).

The first four are also available in standard linear systems, oscillations between two values are available too under resonance, chaotic systems though have typically a large range of resonance conditions. The other phenomena are peculiar to chaos. This progression of stages is strikingly similar to the onset of turbulence. Chaos is not peculiar to non-linear systems alone and it can also be exhibited by infinite dimensional linear systems.

As mentioned above, the logistic map itself is an ordinary quadratic function. An important question in terms of dynamical systems is how the behavior of the trajectory changes when the parameter r changes. Depending on the value of r, the behavior of the trajectory of the logistic map can be simple or complex. Below, we will explain how the behavior of the logistic map changes as r increases.

### Domain, graphs and fixed points

As mentioned above, the logistic map can be used as a model to consider the fluctuation of population size. In this case, the variable x of the logistic map is the number of individuals of an organism divided by the maximum population size, so the possible values of x are limited to 0 ≤ x ≤ 1. For this reason, the behavior of the logistic map is often discussed by limiting the range of the variable to the interval [0, 1].

If we restrict the variables to 0 ≤ x ≤ 1, then the range of the parameter r is necessarily restricted to 0 to 4 (0 ≤ r ≤ 4). This is because if $x_{n}$ is in the range [0, 1], then the maximum value of $x_{n+1}$ is r/4. Thus, when r > 4, the value of $x_{n+1}$ can exceed 1. On the other hand, when r is negative, x can take negative values.

A graph of the map can also be used to learn much about its behavior. The graph of the logistic map $x_{n+1}=rx_{n}(1-x_{n})$ is the plane curve that plots the relationship between $x_{n}$ and $x_{n+1}$ , with $x_{n}$ (or x) on the horizontal axis and $x_{n+1}$ (or f (x)) on the vertical axis. The graph  of the logistic map looks like this, except for the case r = 0:

It has the shape of a parabola with a vertex at

| ${\displaystyle (x_{n},x_{n+1})=\left(0.5,{\frac {r}{4}}\right)}$ |   | 2-1 |
|---|---|---|

When r is changed, the vertex moves up or down, and the shape of the parabola changes. In addition, the parabola of the logistic map intersects with the horizontal axis (the line where $x_{n+1}=0$ ) at two points. The two intersection points are $(x_{n},x_{n+1})=(0,0)$ and $(x_{n},x_{n+1})=(1,0)$ , and the positions of these intersection points are constant and do not depend on the value of r.

Graphs of maps, especially those of one variable such as the logistic map, are key to understanding the behavior of the map. One of the uses of graphs is to illustrate fixed points. Draw a line y = x (a 45° line) on the graph of the map. If there is a point where this 45° line intersects with the graph, that point is a fixed point. In mathematical terms, a fixed point is

| $f(x)=x$ |   | 2-2 |
|---|---|---|

It means a point that does not change when the map is applied. We will denote the fixed point as $x_{f}$ . In the case of the logistic map, the fixed point that satisfies equation (2-2) is obtained by solving $rx(1-x)=x$ .

| ${\displaystyle x_{f1}=0}$ |   | 2-3 |
|---|---|---|

| $x_{f2}=1-{\frac {1}{r}}$ |   | 2-4 |
|---|---|---|

(except for r = 0). The concept of fixed points is of primary importance in discrete dynamical systems.

Another graphical technique that can be used for one-variable mappings is the spider web projection. After determining an initial value $x_{0}$ on the horizontal axis, draw a vertical line from the initial value $x_{0}$ to the curve of f(x). Draw a horizontal line from the  point where the curve of f(x) meets the 45° line of y = x, and then draw a vertical line from the point where the curve meets the 45° line to the curve of f(x). By repeating this process, a spider web or staircase-like diagram is created on the plane. This construction is in fact equivalent to calculating the trajectory graphically, and the spider web diagram created represents the trajectory starting from $x_{0}$ . This projection allows the overall behavior of the trajectory to be seen at a glance.

### Behavior dependent on *r*

The image below shows the amplitude and frequency content of a logistic map that iterates itself for parameter values ranging from 2 to 4. Again one can see initial linear behaviours then chaotic behaviour not only in the time domain (left) but especially in the frequency domain or spectrum (right), i.e. chaos is present at all scales as it is in the case of Energy cascade of Kolmogorov and it even propagates from one scale to another.

By varying the parameter r, the following behavior is observed:

#### Case when 0 ≤ r < 1

First, when the parameter r = 0, $x_{1}=0$ , regardless of the initial value $x_{0}$ . In other words, the trajectory of the logistic map when a = 0 is a trajectory in which all values after the initial value are 0, so there is not much to investigate in this case.

Next, when the parameter r is in the range 0 < r < 1, $x_{n}$ decreases monotonically for any value of $x_{0}$ between 0 and 1. That is, $x_{n}$ converges to 0 in the limit n → ∞. The point to which $x_{n}$ converges is the fixed point $x_{f1}$ shown in equation (2-3). Fixed points of  this type, where orbits around them converge, are called asymptotically stable, stable, or attractive. Conversely, if orbits around $x_{f}$ move away from $x_{f}$ as time n increases, the fixed point $x_{f}$ is called unstable or repulsive.

A common and simple way to know whether a fixed point is asymptotically stable is to take the derivative of the map f. This derivative is expressed as $f'(x)$ , $x_{f}$ is asymptotically stable if the following condition is satisfied.

| $\left\|f'(x_{f})\right\|<1$ |   | 3-1 |
|---|---|---|

This can be seen by graphing the map: if the slope of the tangent to the curve at $x_{f}$ is between −1 and 1, then $x_{f}$ is stable and the orbit around it is attracted to $x_{f}$ . The derivative of the logistic map is

| $f'(x)=r(1-2x)$ |   | 3-2 |
|---|---|---|

Therefore, for x = 0 and 0 < r < 1, 0 < f  '(0) < 1, so the fixed point $x_{f1}$ = 0  satisfies equation (3-1).

However, the discrimination method using equation (3-1) does not know the range of orbits from $x_{f}$ that are attracted to $x_{f}$ . It only guarantees that x within a certain neighborhood of $x_{f}$ will converge. In this case, the domain of initial values that converge to 0 is the entire domain [0, 1], but to know this for certain, a separate study is required.

The method for determining whether a fixed point is unstable can be found by similarly differentiating the map. For r<1 if a fixed point $x_{f}$ is unstable if

| $\left\|f'(x_{f})\right\|>1$ |   | 3-3 |
|---|---|---|

If the parameter lies in the range 0 < r < 1, then the other fixed point $x_{f2}=1-1/a$ is negative and therefore does not lie in the range [0, 1], but it does exist as an unstable fixed point.

#### Case when 1 ≤ r ≤ 2

In the general case with r between 1 and 2, the population will quickly approach the value ⁠*r* − 1/*r*⁠, independent of the initial population.

When the parameter r = 1, the trajectory of the logistic map converges to 0 as before, but the convergence speed is slower at r = 1. The fixed point 0 at r = 1 is asymptotically stable, but does not satisfy equation (3-1). In fact, the discrimination method based on equation (3-1) works by approximating the map to the first order near the fixed point. When r = 1, this approximation does not hold, and stability or instability is determined by the quadratic (square) terms of the map, or in order words the second order perturbation.

When r = 1 is graphed, the curve is tangent to the 45° diagonal at x = 0. In this case, the fixed point $x_{f2}=1-1/r$ , which exists in the negative range for $0<r<1$ , is $x_{f2}=0$ . For $x_{f2}=0$ , that is, as r increases, the value of $x_{f2}$  approaches 0, and just at r = 1  , $x_{f2}$ collides with   $x_{f1}=0$ . This collision gives rise to a phenomenon known as a transcritical bifurcation. Bifurcation is a term used to describe a qualitative change in the behavior of a dynamical system. In this case, transcritical bifurcation is when the stability of fixed points alternates between each other. That is, when r is less than 1, $x_{f1}$ is stable and $x_{f2}$ is unstable, but when r is greater than 1, $x_{f1}$ is unstable and $x_{f2}$ is stable. The parameter  values at which bifurcation occurs are called bifurcation points. In this case, r = 1 is the bifurcation point.

Fixed point

$x_{f2}=1-1/r$

Example of monotonically decreasing convergence to (r = 1.2, x 0 = 0.6)

Fixed point

$x_{f2}=1-1/a$

Example of monotonically increasing convergence to (r = 1.8, x 0 = 0.2)

As a result of the bifurcation, the orbit of the logistic map converges to the limit point $x_{f2}=1-1/r$ instead of $x_{f1}=0$ . In particular, if the parameter $1<r\leq 2$ , then the trajectory starting from a value $x_{0}$ in the interval (0, 1), exclusive of 0 and 1, converges to $x_{f2}$ by increasing or decreasing monotonically. The difference in the convergence pattern depends on the range of the initial value. $0<x_{0}<1-1/r$

In the case of $1-1/r<x_{0}<1/r$ Then, it converges monotonically, $1/r<x_{0}<1$ , the function converges monotonically except for the first step.

Furthermore, the fixed point $x_{f1}=0$ becomes unstable due to bifurcation, but continues to exist as a fixed point even after r > 1. This does not mean that there is no initial value other than $x_{f1}$ itself that  can reach this unstable fixed point   $x_{f1}$ . This is $x_{0}=1$ , and since the logistic map satisfies f (1) = 0 regardless of the value of r,  applying the map once to $x_{0}=1$ maps it to $x_{f1}=0$ . A point such as x = 1 that can be reached directly as a fixed point by a  finite number of iterations of the map is called a final fixed point.

#### Case when 2 ≤ r ≤ 3

With r between 2 and 3, the population will also eventually approach the same value ⁠*r* − 1/*r*⁠, but first will fluctuate around that value for some time. The rate of convergence is linear, except for *r* = 3, when it is dramatically slow, less than linear (see Bifurcation memory).

When the parameter 2 < r < 3, except for the initial values 0 and 1, the fixed point $x_{f2}=1-1/r$ is the same as when 1 < r ≤ 2. However, in this case the convergence is not monotonic. As the variable approaches $x_{f2}$ , it becomes larger and smaller than $x_{f2}$ repeatedly, and follows a convergent trajectory that oscillates around $x_{f2}$ .

. The value that is mapped to $x_{f2}$ by applying the mapping once is $f({\tilde {x}}_{f2})=x_{f2}$ -->

In general, bifurcation diagrams are useful for understanding bifurcations. These diagrams are graphs of fixed points (or periodic points, as described below) x as a function of a parameter a, with a on the horizontal axis and x on the vertical axis. To distinguish between stable and unstable fixed points, the former curves are sometimes drawn as solid lines and the latter as dotted lines. When drawing a bifurcation diagram for the logistic map, we have a straight line representing the fixed point $x_{f1}=0$  and a straight line representing the fixed point $x_{f2}=1-1/a$ It can be seen that the curves representing a and b intersect at r = 1, and that stability is switched between the two.

#### Case when 3 ≤ r ≤ 3.44949

In the general case With r between 3 and 1 + √6 ≈ 3.44949 the population will approach permanent oscillations between two values. These two values are dependent on r and given by $x_{\pm }={\frac {1}{2r}}\left(r+1\pm {\sqrt {(r-3)(r+1)}}\right)$ .

When the parameter is exactly r = 3, the orbit also has a fixed point $x_{f2}=1-1/r$ . However, the variables converge more slowly than when $2<r<3$ . When $r=3$ , the derivative $f'(x_{f2})$ reaches −1 and no longer satisfies equation (3-1). When r exceeds 3, $f'(x_{f2})<-1$ , and $x_{f2}$ becomes  an unstable fixed point. That is, another bifurcation occurs at $r=3$ .

For $r=3$ a type of bifurcation known as a period doubling bifurcation occurs. For $r>3$ , the orbit no longer converges to a single point, but instead alternates between large and small values even after a sufficient amount of time has passed. For example, for $r=3.3$ , the variable alternates between the values 0.4794... and 0.8236....

Spider diagram and time series for a = 3.3. The orbit is attracted to a stable 2-periodic point.

An orbit that cycles through the same values periodically is called a periodic orbit. In this case, the final behavior of the variable as n → ∞ is a periodic orbit with two periods. Each value (point) that makes up a periodic orbit is called a periodic point. In the example where a = 3.3, 0.4794... and 0.8236... are periodic points. If a certain x is a periodic point, then in the case of two periodic points, applying the map twice to x will return it to its original state, so

| $f(f(x))=f^{2}(x)=x$ |   | 3-4 |
|---|---|---|

If we apply the logistic map equation (1-2) to this equation, we get

| $r^{2}x(1-x)(1-rx(1-x))=x$ |   | 3-5 |
|---|---|---|

This gives us the following fourth-order equation. The solutions of this equation are the periodic points. In fact, the two fixed points $x_{f1}=0$ and $x_{f2}=1-1/r$ also satisfy equation (3-4). Therefore, of the solutions to equation (3-5), two correspond to $x_{f1}$ and $x_{f2}$ , and the remaining two solutions are 2-periodic points. Let the 2-periodic points be denoted as $x_{f1}^{(2)}$ and $x_{f2}^{(2)}$ , respectively. By solving equation (3-5), we can obtain them as follows

| $x_{f1}^{(2)},\ x_{f2}^{(2)}={\frac {r+1\pm {\sqrt {(r+1)(r-3)}}}{2r}}$ |   | 3-6 |
|---|---|---|

A similar theory about the stability of fixed points can also be applied to periodic points. That is, a periodic point that attracts surrounding orbits is called an asymptotically stable periodic point, and a periodic point where the surrounding orbits move away is called an unstable periodic point. It is possible to determine the stability of periodic points in the same way as for fixed points. In the general case, consider $f^{k}(x)$ after k iterations of the map. Let $(f^{k})'(x)$ be the derivative  $df^{k}(x)/dx$ of the k-periodic point $x_{f}^{(k)}$ . If $x_{f}^{(k)}$ satisfies:

| $\left\|(f^{k})'(x_{f}^{(k)})\right\|<1$ |   | 3-7 |
|---|---|---|

then $x_{f}^{(k)}$ is asymptotically stable.

| $\left\|(f^{k})'(x_{f}^{(k)})\right\|>1$ |   | 3-8 |
|---|---|---|

then $x_{f}^{(k)}$ is unstable.

The above discussion of the stability of periodic points can be easily understood by drawing a graph, just like the fixed points. In this diagram, the horizontal axis is xn and the vertical axis is $x_{n+2}$ , and a curve is drawn that shows the relationship between $x_{n+2}$ and $x_{n}$ . The intersections of this curve and the 45° line are points that satisfy equation (3-4), so the intersections represent fixed points and 2-periodic points. If we draw a graph of the logistic map $f^{2}(x)$ , we can observe that the slope of the tangent at the fixed point $x_{f2}$ exceeds  1 at the boundary $r=3$ and becomes unstable. At the same time, two new intersections appear, which are the periodic points $x_{f1}^{(2)}$ and $x_{f2}^{(2)}$ .

The relationship between

$x_{n+2}$

and

$x_{n}$

when r = 2.7, before the period doubling bifurcation occurs. The orbit converges to a fixed point

$x_{f2}$

.

The relationship between

$x_{n+2}$

and

$x_{n}$

when r = 3. The tangent slope at the fixed point

$x_{f2}$

is exactly 1, and a period doubling bifurcation occurs.

The relationship between

$x_{n+2}$

and

$x_{n}$

when r = 3.3.

$x_{f2}$

becomes unstable and the orbit converges to the periodic points

$x_{f1}^{(2)}$

and

$x_{f2}^{(2)}$

.

When we actually calculate the differential coefficients of two periodic points for the logistic map, we get

| $(f^{2})'(x_{f}^{(2)})=4+2r-r^{2}$ |   | 3-9 |
|---|---|---|

When this is applied to equation (3-7), the parameter a becomes:

| $\left\|4+2r-r^{2}\right\|<1$ |   | 3-10 |
|---|---|---|

It can be seen that the 2-periodic points are asymptotically stable when this range is $3<r<1+{\sqrt {6}}$ , i.e., when r exceeds $1+{\sqrt {6}}=3.44949...$ , the 2-periodic points are no longer asymptotically stable and their behavior changes.

Almost all initial values in [0, 1] are attracted to the 2-periodic points, but $x_{f1}=0$ and $x_{f2}=1-1/a$ remains as an unstable fixed point in [0,1]. These unstable fixed points continue to remain in [0,1] even if r is increased. Therefore, when the initial value is exactly $x_{f1}$ or $x_{f2}$ , the orbit  does not attract to a 2-periodic point. Moreover, when the initial value is the final fixed point for $x_{f1}$ or the final fixed point for $x_{f2}$ , the orbit does not attract to a 2-periodic point. There are an infinite number of such final fixed points in [0, 1]. However, the number of such points is negligibly small compared to the set of real numbers [ 0, 1].

#### Case when 3.44949 ≤ r ≤ 3.56995

With r between 3.44949 and 3.54409 (approximately), from almost all initial conditions the population will approach permanent oscillations among four values. The latter number is a root of a 12th degree polynomial (sequence A086181 in the OEIS).

With r increasing beyond 3.54409, from almost all initial conditions the population will approach oscillations among 8 values, then 16, 32, etc. The lengths of the parameter intervals that yield oscillations of a given length decrease rapidly; the ratio between the lengths of two successive bifurcation intervals approaches the Feigenbaum constant *δ* ≈ 4.66920. This behavior is an example of a period-doubling cascade.

When the parameter r exceeds $1+{\sqrt {6}}=3.44949...$ , the previously stable 2-periodic points become unstable, stable 4-periodic points are generated, and the orbit gravitates toward a 4-periodic oscillation. That is, a period-doubling bifurcation occurs again at $r=3.44949...$ . The value of x at the 4-periodic point is also

| $f(f(f(f(x))))=f^{4}(x)=x$ |   | 3-11 |
|---|---|---|
