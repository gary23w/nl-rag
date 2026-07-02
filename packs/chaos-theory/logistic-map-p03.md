---
title: "Logistic map (part 3/4)"
source: https://en.wikipedia.org/wiki/Logistic_map
domain: chaos-theory
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
part: 3/4
---

# Logistic map

satisfies, so that solving this equation allows the values of x at the 4-periodic points to be found. However, equation (3-11) is a 16th-order equation, and even if we factor out the four solutions for the fixed points and the 2-periodic points, it is still a 12th-order equation. Therefore, it is no longer possible to solve this equation to obtain an explicit function of a that represents the values of the 4-periodic points in the same way as for the 2-periodic points.

| The kth branch | Period 2*k* | Branch point *ak* |
|---|---|---|
| 1 | 2 | 3.0000000 |
| 2 | 4 | 3.4494896 |
| 3 | 8 | 3.5440903 |
| 4 | 16 | 3.5644073 |
| 5 | 32 | 3.5687594 |
| 6 | 64 | 3.5696916 |
| 7 | 128 | 3.5698913 |
| 8 | 256 | 3.5699340 |

As a becomes larger, the stable 4-periodic point undergoes another period doubling, resulting in a stable 8-periodic point. As an increases, period doubling bifurcations occur infinitely: 16, 32, 64, ..., and so on, until an infinite period, i.e., an orbit that never returns to its original value. This infinite series of period doubling bifurcations is called a cascade. While these period doubling bifurcations occur infinitely, the intervals between a at which they occur decrease in a geometric progression. Thus, an infinite number of period doubling bifurcations occur before the parameter a reaches a finite value. Let the bifurcation from period 1 to period 2 that occurs at r = 3 be counted as the first period doubling bifurcation. Then, in this cascade of period doubling bifurcations, a stable 2k-periodic point occurs at the k-th bifurcation point. Let the k-th bifurcation point a be denoted as a k. In this case, it is known that $r_{k}$ converges to the following value as k → ∞. (sequence A098587 in the OEIS)

| $r_{\infty }=\lim _{k\rightarrow \infty }r_{k}=3.56994...$ |   | 3-12 |
|---|---|---|

Furthermore, it is known that the rate of decrease of a k reaches a constant value in the limit, as shown in the following equation.

| $\delta =\lim _{k\to \infty }{\frac {r_{k}-r_{k-1}}{r_{k+1}-r_{k}}}=4.66920...$ |   | 3-13 |
|---|---|---|

This value of δ is called the Feigenbaum constant because it was discovered by mathematical physicist Mitchell Feigenbaum. $r_{\infty }$ is called the Feigenbaum point. In the period doubling cascade, $f^{m}$   and $f^{2m}$ have the property that they are locally identical after an appropriate scaling transformation. The Feigenbaum constant can be found by a technique called renormalization that exploits this self-similarity. The properties that the logistic map exhibits in the period doubling cascade are also universal in a broader class of maps, as will be discussed later.

To get an overview of the final behavior of an orbit for a certain parameter, an approximate bifurcation diagram, orbital diagram, is useful. In this diagram, the horizontal axis is the parameter r and the vertical axis is the variable x, as in the bifurcation diagram. Using a computer, the parameters are determined and, for example, 500 iterations are performed. Then, the first 100 results are ignored and only the results of the remaining 400 are plotted. This allows the initial transient behavior to be ignored and the asymptotic behavior of the orbit remains. For example, when one point is plotted for r, it is a fixed point, and when m points are plotted for r, it corresponds to an m-periodic orbit. When an orbital diagram is drawn for the logistic map, it is possible to see how the branch representing the stable periodic orbit splits, which represents a cascade of period-doubling bifurcations.

When the parameter $r=r_{\infty }$ is exactly the accumulation point of the period-doubling cascade, the variable $x_{n}$ is attracted to aperiodic orbits that never close. In other words, there exists a periodic point with infinite period at $r_{\infty }$ . This aperiodic orbit is called the Feigenbaum attractor. The critical $2^{\infty }$ attractor. An attractor is a term used to refer to a region that has the property of attracting surrounding orbits, and is the orbit that is eventually drawn into and continues. The attractive fixed points and periodic points mentioned above are also members of the attractor family.

The structure of the Feigenbaum attractor is the same as that of a fractal figure called the Cantor set. The number of points that compose the Feigenbaum attractor is infinite and their cardinality is equal to the real numbers. However, no matter which two of the points are chosen, there is always an unstable periodic point between them, and the distribution of the points is not continuous. The fractal dimension of the Feigenbaum attractor, the Hausdorff dimension or capacity dimension, is known to be approximately 0.54.

#### Case when 3.56995 < r < 4

##### Qualitative Summary

- At *r* ≈ 3.56995 (sequence A098587 in the OEIS) is the onset of chaos, at the end of the period-doubling cascade. From almost all initial conditions, we no longer see oscillations of finite period. Slight variations in the initial population yield dramatically different results over time, a prime characteristic of chaos.
- This number shall be compared and understood as the equivalent of the Reynolds number for the onset of other chaotic phenomena such as turbulence and similar to the critical temperature of a phase transition. In essence the phase space contains a full subspace of cases with extra dynamical variables to characterize the microscopic state of the system, these can be understood as Eddies in the case of turbulence and order parameters in the case of phase transitions.
- Most values of r beyond 3.56995 exhibit chaotic behaviour, but there are still certain isolated ranges of r that show non-chaotic behavior; these are sometimes called *islands of stability*. For instance, beginning at 1 + √8 (approximately 3.82843) there is a range of parameters r that show oscillation among three values, and for slightly higher values of r oscillation among 6 values, then 12 etc.
- At $r=1+{\sqrt {8}}=3.8284...$ , the stable period-3 cycle emerges.
- The development of the chaotic behavior of the logistic sequence as the parameter r varies from approximately 3.56995 to approximately 3.82843 is sometimes called the Pomeau–Manneville scenario, characterized by a periodic (laminar) phase interrupted by bursts of aperiodic behavior. Such a scenario has an application in semiconductor devices. There are other ranges that yield oscillation among 5 values etc.; all oscillation periods occur for some values of r. A *period-doubling window* with parameter c is a range of r-values consisting of a succession of subranges. The kth subrange contains the values of r for which there is a stable cycle (a cycle that attracts a set of initial points of unit measure) of period 2*k**c*. This sequence of sub-ranges is called a *cascade of harmonics*. In a sub-range with a stable cycle of period 2*k***c*, there are unstable cycles of period 2*k**c* for all *k* < *k**. The r value at the end of the infinite sequence of sub-ranges is called the *point of accumulation* of the cascade of harmonics. As r rises there is a succession of new windows with different c values. The first one is for *c* = 1; all subsequent windows involving odd c occur in decreasing order of c starting with arbitrarily large c.
- At $r=3.678...,x=0.728...$ , two chaotic bands of the bifurcation diagram intersect in the first Misiurewicz point for the logistic map. It satisfies the equations $r^{3}-2r^{2}-4r-8=0,x=1-1/r$ .
- Beyond *r* = 4, almost all initial values eventually leave the interval [0,1] and diverge. The set of initial conditions which remain within [0,1] form a Cantor set and the dynamics restricted to this Cantor set is chaotic.

For any value of r there is at most one stable cycle. If a stable cycle exists, it is globally stable, attracting almost all points. Some values of r with a stable cycle of some period have infinitely many unstable cycles of various periods.

The bifurcation diagram at rightabove summarizes this. The horizontal axis shows the possible values of the parameter r while the vertical axis shows the set of values of x visited asymptotically from almost all initial conditions by the iterates of the logistic equation with that r value.

The bifurcation diagram is a self-similar: if we zoom in on the above-mentioned value *r* ≈ 3.82843 and focus on one arm of the three, the situation nearby looks like a shrunk and slightly distorted version of the whole diagram. The same is true for all other non-chaotic points. This is an example of the deep and ubiquitous connection between chaos and fractals.

Magnification of the chaotic region of the map

Stable regions within the chaotic region, where a tangent bifurcation occurs at the boundary between the chaotic and periodic attractor, giving intermittent trajectories as described in the

Pomeau–Manneville scenario

We can also consider negative values of r:

- For r between -2 and -1 the logistic sequence also features chaotic behavior.
- With r between -1 and 1 - √6 and for x0 between 1/r and 1-1/r, the population will approach permanent oscillations between two values, as with the case of r between 3 and 1 + √6, and given by the same formula.

##### The Emergence of Chaos

Chaotic orbits of the logistic map when r = 3.82. The orange squares are orbits starting from

$x_{0}=0.1234$

, and the blue-green circles are orbits starting from

${\hat {x}}_{0}=0.1234+10^{-9}$

.

The trajectory starting from x 0 = 0.1234 and ˆx The difference in orbits starting from

$x_{0}=0.1234+10^{-9}$

grows exponentially. The vertical axis is

$\Delta x_{n}=|x_{n}-{\hat {x}}_{n}|$

, shown on a

logarithmic scale

.

When the parameter r exceeds $r_{\infty }=3.56994...$ , the logistic map exhibits chaotic behavior. Roughly speaking, chaos is a complex and irregular behavior that occurs despite the fact that the difference equation describing the logistic map has no probabilistic ambiguity and the next state is completely and uniquely determined. The range of $r>r_{\infty }$ of the logistic map is called the chaotic region.

One of the properties of chaos is its unpredictability, symbolized by the term butterfly effect. This is due to the property of chaos that a slight difference in the initial state can lead to a huge difference in the later state. In terms of a discrete dynamical system, if we have two initial values $x_{0}$ and ${\hat {x}}_{0}$ No matter how close they are, once time n has progressed to a certain extent, each destination $x_{n}$ and ${\hat {x}}_{n}$ can vary significantly. For example, use $r=3.95,x_{0}=0.1,{\hat {x}}_{0}=x_{0}+10^{-9}$ If the orbits are calculated using two very similar initial values, 0 = 0.1000000001, the difference grows to macroscopic values that are clearly visible on the graph after about 29 iterations.

This property of chaos, called initial condition sensitivity, can be quantitatively expressed by the Lyapunov exponent. For a one-dimensional map, the Lyapunov exponent λ can be calculated as follows:

| ${\displaystyle \lambda =\lim _{N\to \infty }{\frac {1}{N}}\sum _{i=0}^{N-1}\log \left\|f^{\prime }(x_{i})\right\vert }$ |   | 3-14 |
|---|---|---|

Here, log means natural logarithm. This λ is the distance between the two orbits ( $x_{n}$ and ${\hat {x}}_{n}$ ). A positive value of λ indicates that the system is sensitive to initial conditions, while a zero or negative value indicates that the system is not sensitive to initial conditions. When calculating λ of numerically, it can be confirmed λ remains in the range of zero or negative values in the range $r<r_{\infty }$ , and that λ can take positive values in the range $r>r_{\infty }$ .

**Window, intermittent**

Even beyond $r_{\infty }$ , the behavior does not depend simply on the parameter r. Many sophisticated mathematical structures lurk in the chaotic region for $r>r_{\infty }$ . In this region, chaos does not persist forever; stable periodic orbits reappear. The behavior for $r_{\infty }<a\leq 4$ can be broadly divided into two types:

- Stable periodic point: In this case, the Lyapunov exponent is negative.
- Aperiodic orbits: In this case, the Lyapunov exponent is positive.

The region of stable periodic points that exists for r $r_{\infty }<r\leq 4$ is called a periodic window, or simply a window. If one looks at a chaotic region in an orbital diagram, the region of nonperiodic orbits looks like a cloud of countless points, with the windows being the scattered blanks surrounded by the cloud.

Orbit diagram of the logistic map from r = 3.55 to r = 4 (parameter is denoted as r in the diagram)

In each window, the cascade of period-doubling bifurcations that occurred before $r_{\infty }=3.56994...$ occurs again. However, instead of the previous stable periodic orbits of 2^k, new stable periodic orbits such as 3×2^k and 5×2^k are generated. The first window has a period of p, and the windows from which the period-doubling cascade occurs are called windows of period p, etc.. For example, a window of period 3 exists in the region around 3.8284 < a < 3.8415, and within this region the period doublings are: 3, 6, 12, 24, ..., 3×2^k, ....

In the window region, chaos does not disappear but exists in the background. However, this chaos is unstable, so only stable periodic orbits are observed. In the window region, this potential chaos appears before the orbit is attracted from its initial state to a stable periodic orbit. Such chaos is called transient chaos. In this potential presence of chaos, windows differ from the periodic orbits that appeared before a∞.

There are an infinite number of windows in the range a∞ < a < 4. The windows have various periods, and there is a window with a period for every natural number greater than or equal to three. However, each window does not occur exactly once. The larger the value of p, the more often a window with that period occurs. A window with period 3 occurs only once, while a window with period 13 occurs 315 times. When a periodic orbit of 3 occurs in the window with period 3, the Szarkovsky order is completed, and all orbits with all periods have been seen.

If we restrict ourselves to the case where p is a prime number, the number of windows with period p is

| ${\displaystyle N_{p}={\frac {2^{p-1}-1}{p}}}$ |   | 3-15 |
|---|---|---|

This formula was derived for p to be a prime number, but in fact it is possible to calculate with good accuracy the number of stable p- periodic points for non-prime p as well.

The window width (the difference between a where the window begins and a where the window ends) is widest for windows with period 3 and narrows for larger periods. For example, the window width for a window with period 13 is about 3.13 × 10−6. Rough estimates suggest that about 10% of $[r_{\infty },4]$ is in the window region, with the rest dominated by chaotic orbits.

The change from chaos to a window as r is increased is caused by a tangent bifurcation, where the map curve is tangent to the diagonal of y = x at the moment of bifurcation, and further parameter changes result in two fixed points where the curve and the line intersect. For a window of period p, the iterated map $f^{p}(x)$ exhibits tangent bifurcation, resulting in stable p-periodic orbits. The exact value of the bifurcation point for a window of period 3 is known, and if the value of this bifurcation point r is $r_{3}$ , then $r_{3}=1+{\sqrt {8}}=3.828427...$ . The outline of this bifurcation can be understood by considering the graph of $f^{3}(x)$ (vertical axis $x_{n+3}$ , horizontal axis $x_{n}$ ).

Graph of

$f^{3}(x)$

when r is slightly less than 3. The graph is not tangent except at the fixed points, and there are no 3-periodic points.

When a is exactly 3, the graph touches the diagonal at exactly three points, resulting in three periodic points.

When a is slightly greater than 3, the graph passes the diagonal and splits into stable and unstable 3-periodic points.

When we look at the behavior of $x_{n}$ when r = 3.8282, which is slightly smaller than the branch point $r_{3}$ , we can see that in addition to the irregular changes, there is also a behavior that changes periodically with approximately three periods, and these occur alternately. This type of periodic behavior is called a "laminar", and the irregular behavior is called a burst, in analogy with fluids. There is no regularity in the length of the time periods of the bursts and laminars, and they change irregularly. However, when we observe the behavior at r = 3.828327, which is closer to $r_{3}$ , the average length of the laminars is longer and the average length of the bursts is shorter than when r = 3.8282. If we further increase r, the length of the laminars becomes larger and larger, and at $r_{3}$ it changes to a perfect three- period.

Time series when r = 3.8282

Time series when r = 3.828327

The phenomenon in which orderly motions called laminars and disorderly motions called bursts occur intermittently is called intermittency or intermittent chaos. If we consider the parameter a decreasing from a3, this is a type of emergence of chaos. As the parameter moves away from the window, bursts become more dominant, eventually resulting in a completely chaotic state. This is also a general route to chaos, like the period doubling bifurcation route mentioned above, and routes characterized by the emergence of intermittent chaos due to tangent bifurcations are called intermittency routes.

The mechanism of intermittency can also be understood from the graph of the map. When r is slightly smaller than $r_{3}$ , there is a very small gap between the graph of $f^{3}(x)$ and the diagonal. This gap is called a channel, and many iterations of the map occur as the orbit passes through the narrow channel. During the passage through this channel, $x_{n}$ and $x_{n+3}$ become very close, and the variables change almost like a periodic three orbit. This corresponds to a laminar. The orbit eventually leaves the narrow channel, but returns to the channel again as a result of the global structure of the map. While leaving the channel, it behaves chaotically. This corresponds to a burst.

**Band, window finish**

Looking at the entire chaotic domain, whether it is chaotic or windowed, the maximum and minimum values on the vertical axis of the orbital diagram (the upper and lower limits of the attractor) are limited to a certain range. As shown in equation (2-1), the maximum value of the logistic map is given by r/4, which is the upper limit of the attractor. The lower limit of the attractor is given by the point f(r/4) where r/4 is mapped. Ultimately, the maximum and minimum values at which xn moves on the orbital diagram depend on the parameter r

| ${\displaystyle {\frac {r^{2}(4-r)}{16}}\leq x_{n}\leq {\frac {r}{4}}}$ |   | 3-16 |
|---|---|---|

Finally, for r = 4, the orbit spans the entire range [0, 1].

When observing an orbital map, the distribution of points has a characteristic shading. Darker areas indicate that the variable takes on values in the vicinity of the darker areas, whereas lighter areas indicate that the variable takes on values in the vicinity of the darker areas. These differences in the frequency of the points are due to the shape of the graph of the logistic map. The top of the graph, near r/4, attracts orbits with high frequency, and the area near f(r/4) that is mapped from there also becomes highly frequent, and the area near $f^{2}(r/4)$ that is mapped from there also becomes  highly frequent, and so on. The density distribution of points generated by the map is characterized by a quantity called an invariant measure or distribution function, and the invariant measure of the attractor is reproducible regardless of the initial value.

Looking at the beginning of the chaotic region of the orbit diagram, just beyond the accumulation point $r_{\infty }=3.56994$ of the first period - doubling cascade, one can see that the orbit is divided into several subregions. These subregions are called bands. When there are multiple bands, the orbit moves through each band in a regular order, but the values within each band are irregular. Such chaotic orbits are called band chaos or periodic chaos, and chaos with k bands is called k -band chaos. Two-band chaos lies in the range 3.590 < r < 3.675, approximately.

Band structure. Because the

$e_{p}$

spacing rapidly decreases, it is not possible to show more than eight bands. The top and bottom lines, which contain the orbitals, are within the range of equation (3-16).

As the value of r is further decreased from the left-hand end of two-band chaos, r = 3.590, the number of bands doubles, just as in the period doubling bifurcation. Let $e_{p}$ (for p = 1, 2, 4, ..., 2k, ...) denote the bifurcation points where p − 1 band chaos splits into p band chaos, or where p band chaos merges into p − 1 band chaos. Then, just as in the period doubling bifurcation, e p accumulates to a value as p → ∞. At this accumulation point $e_{\infty }$ , the number of bands becomes infinite, and the value of $e_{\infty }$ is equal to the value of $r_{\infty }$ .

Similarly, for the bifurcation points of the period-doubling bifurcation cascade that appeared before a∞, let a p (where p = 1, 2, 4, ..., 2k, ...) denote the bifurcation points where p stable periodic orbits branch into p + 1 stable periodic orbits. In this case, if we look at the orbital diagram from $r_{2}$ to $e_{2}$ , there are two reduced versions of the global orbital diagram from $r_{1}$ to $e_{1}$ in the orbital diagram from $r_{2}$ to $e_{2}$ . Similarly, if we look at the orbital diagram from $r_{4}$ to $e_{4}$ , there are four reduced versions of the global orbital diagram from a1 to e1 in the orbital diagram from $r_{4}$ to $e_{4}$ . Similarly, there are p reduced versions of the global orbital diagram in the orbital diagram from ap to ep, and the branching structure of the logistic map has an infinite self-similar hierarchy.

A self-similar hierarchy of bifurcation structures also exists within windows. The period-doubling bifurcation cascades within a window follow the same path as the cascades of period-2k bifurcations. That is, there are an infinite number of period-doubling bifurcations within a window, after which the behavior becomes chaotic again. For example, in a window of period 3, the cascade of stable periodic orbits ends at $a_{3\infty }$ ≈ 3.8495. After $a_{3\infty }$ ≈ 3.8495, the behavior becomes band chaos of multiples of three. As a increases from $a_{3\infty }$ , these band chaos also merge by twos, until at the end of the window there are three bands. Within such bands within a window, there are an infinite number of windows. Ultimately, the window contains a miniature version of the entire orbital diagram for 1 ≤ a ≤ 4, and within the window there exists a self-similar hierarchy of branchings.

At the end of the window, the system reverts to widespread chaos. For a period 3 window, the final 3-band chaos turns into large-area 1-band chaos at a ≈ 3.857, ending the window. However, this change is discontinuous, and the 3-band chaotic attractor suddenly changes size and turns into a 1-band. Such discontinuous changes in attractor size are called crises. Crises of this kind, which occur at the end of a window, are also called internal crises. When a crisis occurs at the end of a window, a stable periodic orbit just touches an unstable periodic point that is not visible on the orbit diagram. This creates an exit point through which the periodic orbits can escape, resulting in an internal crisis. Immediately after the internal crisis, there are periods of widespread chaos, and periods of time when the original band chaotic behavior reoccurs, resulting in a kind of intermittency similar to that observed at the beginning of a window.

#### When r = 4

Spider diagram of the logistic map with parameter r = 4 (left) and time series up to n = 500 (right) for the initial value

$x_{0}$

= 0.3.

When the parameter r = 4, the behavior becomes chaotic over the entire range [0, 1]. At this time, the Lyapunov exponent λ is maximized, and the state is the most chaotic. The value of λ for the logistic map at r = 4 can be calculated precisely, and its value is λ = log 2. Although a strict mathematical definition of chaos has not yet been unified, it can be shown that the logistic map with r = 4 is chaotic on [0, 1] according to one well-known definition of chaos.

The invariant measure of the density of points, ρ(x), can also be given by the exact function ρ(x) for r = 4:

| ${\displaystyle \rho (x)={\frac {1}{\pi {\sqrt {x(1-x)}}}}}$ |   | 3-17 |
|---|---|---|

Here, ρ(x) means that the fraction of points xn that fall in the infinitesimal interval [x,x+dx] when the map is iterated is given by ρ(x) dx. The frequency distribution of the logistic map with r = 4 has high density near both sides of [0, 1] and is least dense at x = 0.5.

When r = 4, apart from chaotic orbits, there are also periodic orbits with any period. For a natural number n, the graph of $f_{r=4}^{n}(x)$ is a curve with $2^{n-1}$ peaks and $2^{n-1}-1$ valleys, all of which are tangent to 0 and 1. Thus, the number of intersections between the diagonal and the graph is $2^{n}$ , and there are $2^{n}$ fixed points of $f^{n}(x)$ . The n-periodic points are always included in these $2^{n}$ fixed points, so any n-periodic orbit exists for $f_{r=4}^{n}(x)$ . Thus, when r = 4, there are an infinite number of periodic points on [0, 1], but all of these periodic points are unstable. Furthermore, the uncountably infinite set in the interval [0, 1], the number of periodic points is countably infinite, and so almost all orbits starting from initial values are not periodic but non-periodic.

One of the important aspects of chaos is its dual nature: deterministic and stochastic. Dynamical systems are deterministic processes, but when the range of variables is appropriately coarse-grained, they become indistinguishable from stochastic processes. In the case of the logistic map with r = 4, the outcome of every coin toss can be described by the trajectory of the logistic map. This can be elaborated as follows.

Assume that a coin is tossed with a probability of 1/2 landing on heads or tails, and the coin is tossed repeatedly. If heads is 0 and tails is 1, then the result of heads, tails, heads, tails, etc. will be a symbol string such as 01001.... On the other hand, for the trajectory $x_{0},x_{1},x_{2},...$ of the logistic map, values less than x = 0.5 are converted to 0 and values greater than x = 0.5 are converted to 1, and the trajectory is replaced with a symbol string consisting of 0s and 1s. For example, if the initial value is $x_{0}=0.2$ , then $x_{1}=0.64$ , $x_{2}=0.9216$ , $x_{3}=0.28901$ , ..., so the trajectory will be the symbol string 0110.... Let $S_{C}$ be the symbol string resulting from the former coin toss, and $S_{L}$ be the symbol string resulting from the latter logistic map. The symbols in the symbol string $S_{C}$ were determined by random coin tossing, so any number sequence patterns are possible. So, whatever the string $S_{L}$ of the logistic map, there is an identical one in $S_{C}$ . And, what is "remarkable" is that the converse is also true: whatever the string of $S_{C}$ , it can be realized by a logistic map trajectory $S_{L}$ by choosing the appropriate initial values. That is, for any $S_{C}$ , there exists a unique point $x_{0}$ in [0, 1] such that $S_{C}=S_{L}$ .

#### When r > 4

When the parameter r exceeds 4, the vertex r /4 of the logistic map graph exceeds 1. To the extent that the graph penetrates 1, trajectories can escape [0, 1].

The bifurcation at r = 4 is also a type of crisis, specifically a boundary crisis. In this case, the attractor at [0, 1] becomes unstable and collapses, and since there is no attractor outside it, the trajectory diverges to infinity.

On the other hand, there are orbits that remain in [0, 1] even if r > 4. Easy-to-understand examples are fixed points and periodic points in [0, 1], which remain in [0, 1]. However, there are also orbits that remain in [0, 1] other than fixed points and periodic points.

Let $A_{0}$ be the interval of x such that f  (x) > 1. As mentioned above, once a variable $x_{n}$ enters $A_{0}$ , it diverges to minus infinity. There is also $r_{n}$ x in [0, 1] that maps to $A_{0}$ after one application of the map. This interval of x is divided into two, which are collectively called $A_{1}$ . Similarly, there are four intervals that map to $A_{1}$ after one application of the map, which are collectively called $A_{2}$ . Similarly, there are 2n intervals $A_{n}$ that reach $A_{0}$ after n iterations. Therefore, the interval $\Lambda$ obtained by removing $A_{n}$ from [0, 1] an infinite number of times as follows is a collection of orbits that remain in I.

| ${\displaystyle \Lambda =\left[0,\ 1\right]-\bigcup _{n=0}^{\infty }A_{n}}$ |   | 3-18 |
|---|---|---|

The process of removing $A_{n}$ from [0, 1] is similar to the construction of the Cantor set mentioned above, and in fact Λ exists in [0, 1] as a Cantor set (a closed, completely disconnected, and complete subset of [0, 1]). Furthermore, on $\Lambda$ , the logistic map $f_{r>4}$ is chaotic.

#### When r < 0

Since the logistic map has been often studied as an ecological model, the case where the parameter r is negative has rarely been discussed. As a decreases from 0, when −1 < r < 0, the map asymptotically approaches a stable fixed point of xf = 0, but when a exceeds −1, it bifurcates into two periodic points, and as in the case of positive values, it passes through a period doubling bifurcation and reaches chaos. Finally, when a falls below −2, the map diverges to plus infinity.

Orbit diagram for parameter r from −2 to 4. The orbit diverges when the parameter a goes beyond this range, both on the negative and positive sides.

#### Exact solutions for special cases

For a logistic map with a specific parameter a , an exact solution that explicitly includes the time n and the initial value $x_{0}$ has been obtained as follows.

When r = 4

| ${\displaystyle x_{n}={\frac {1-\cos \left[2^{n}\arccos(1-2x_{0})\right]}{2}}}$ |   | 3-19 |
|---|---|---|

When r = 2

| ${\displaystyle x_{n}={\frac {1-\exp \left[2^{n}\log(1-2x_{0})\right]}{2}}}$ |   | 3-20 |
|---|---|---|

When r = −2

| ${\displaystyle x_{n}={\frac {1}{2}}-\cos \left\{{\frac {1}{3}}\left[\pi -(-2)^{n}\left(\pi -3\arccos({\frac {1}{2}}-x_{0})\right)\right]\right\}}$ |   | 3-21 |
|---|---|---|

Considering the three exact solutions above, all of them are

| ${\displaystyle x_{n}={\frac {1}{2}}\left\{1-f\left[a^{n}f^{-1}(1-2x_{0})\right]\right\}}$ |   | 3-22 |
|---|---|---|


## Chaos and the logistic map

The relative simplicity of the logistic map makes it a widely used point of entry into a consideration of the concept of chaos. A rough description of chaos is that chaotic systems exhibits: (see Chaotic dynamics)

- Great sensitivity on initial conditions: i.e. for a small or infinitesimal variation in the initial conditions you may have a large finite effect.
- Topologically transitive: i.e. the system tends to occupy all available states in a similar sense to fluid mixing.
- The system exhibits dense periodic orbits

These are properties of the logistic map for most values of r between about 3.57 and 4 (as noted above). A common source of such sensitivity to initial conditions is that the map represents a repeated folding and stretching of the space on which it is defined. In the case of the logistic map, the quadratic difference equation describing it may be thought of as a stretching-and-folding operation on the interval (0,1).

The following figure illustrates the stretching and folding over a sequence of iterates of the map. Figure (a), left, shows a two-dimensional Poincaré plot of the logistic map's state space for *r* = 4, and clearly shows the quadratic curve of the difference equation (**1**). However, we can embed the same sequence in a three-dimensional state space, in order to investigate the deeper structure of the map. Figure (b) demonstrates this, showing how initially nearby points begin to diverge, particularly in those regions of xt corresponding to the steeper sections of the plot.

This stretching-and-folding does not just produce a gradual divergence of the sequences of iterates, but an exponential divergence (see Lyapunov exponents), evidenced also by the complexity and unpredictability of the chaotic logistic map. In fact, exponential divergence of sequences of iterates explains the connection between chaos and unpredictability: a small error in the supposed initial state of the system will tend to correspond to a large error later in its evolution. Hence, predictions about future states become progressively (indeed, exponentially) worse when there are even very small errors in our knowledge of the initial state. This quality of unpredictability and apparent randomness led the logistic map equation to be used as a pseudo-random number generator in early computers.

At r = 2, the function $rx(1-x)$ intersects $y=x$ precisely at the maximum point, so convergence to the equilibrium point is on the order of $\delta ^{2^{n}}$ . Consequently, the equilibrium point is called "superstable". Its Lyapunov exponent is $-\infty$ . A similar argument shows that there is a superstable r value within each interval where the dynamical system has a stable cycle. This can be seen in the Lyapunov exponent plot as sharp dips.

Since the map is confined to an interval on the real number line, its dimension is less than or equal to unity. Numerical estimates yield a correlation dimension of 0.500±0.005 (Grassberger, 1983), a Hausdorff dimension of about 0.538 (Grassberger 1981), and an information dimension of approximately 0.5170976 (Grassberger 1983) for *r* ≈ 3.5699456 (onset of chaos). Note: It can be shown that the correlation dimension is certainly between 0.4926 and 0.5024.

It is often possible, however, to make precise and accurate statements about the *likelihood* of a future state in a chaotic system. If a (possibly chaotic) dynamical system has an attractor, then there exists a probability measure that gives the long-run proportion of time spent by the system in the various regions of the attractor. In the case of the logistic map with parameter *r* = 4 and an initial state in (0,1), the attractor is also the interval (0,1) and the probability measure corresponds to the beta distribution with parameters *a* = 0.5 and *b* = 0.5. Specifically, the invariant measure is

${\frac {1}{\pi {\sqrt {x(1-x)}}}}.$

Unpredictability is not randomness, but in some circumstances looks very much like it. Hence, and fortunately, even if we know very little about the initial state of the logistic map (or some other chaotic system), we can still say something about the distribution of states arbitrarily far into the future, and use this knowledge to inform decisions based on the state of the system.

### Graphical representation

The bifurcation diagram for the logistic map can be visualized with the following Python code:

```mw
import numpy as np
import matplotlib.pyplot as plt

interval = (2.8, 4)  # start, end
accuracy = 0.0001
reps = 600  # number of repetitions
numtoplot = 200
lims = np.zeros(reps)

fig, biax = plt.subplots()
fig.set_size_inches(16, 9)

lims[0] = np.random.rand()
for r in np.arange(interval[0], interval[1], accuracy):
    for i in range(reps - 1):
        lims[i + 1] = r * lims[i] * (1 - lims[i])

    biax.plot([r] * numtoplot, lims[reps - numtoplot :], "b.", markersize=0.02)

biax.set(xlabel="r", ylabel="x", title="logistic map")
plt.show()
```

### Special cases of the map

#### Upper bound when 0 ≤ *r* ≤ 1

Although exact solutions to the recurrence relation are only available in a small number of cases, a closed-form upper bound on the logistic map is known when 0 ≤ *r* ≤ 1. There are two aspects of the behavior of the logistic map that should be captured by an upper bound in this regime: the asymptotic geometric decay with constant r, and the fast initial decay when *x*0 is close to 1, driven by the (1 − *xn*) term in the recurrence relation. The following bound captures both of these effects:

$\forall n\in \{0,1,\ldots \}\quad {\text{and}}\quad x_{0},r\in [0,1],\quad x_{n}\leq {\frac {x_{0}}{r^{-n}+x_{0}n}}.$

#### Solution when *r* = 4

The special case of *r* = 4 can in fact be solved exactly, as can the case with *r* = 2; however, the general case can only be predicted statistically. The solution when *r* = 4 is:

$x_{n}=\sin ^{2}\left(2^{n}\theta \pi \right),$

where the initial condition parameter θ is given by

$\theta ={\tfrac {1}{\pi }}\sin ^{-1}\left({\sqrt {x_{0}}}\right).$

For rational θ, after a finite number of iterations xn maps into a periodic sequence. But almost all θ are irrational, and, for irrational θ, xn never repeats itself – it is non-periodic. This solution equation clearly demonstrates the two key features of chaos – stretching and folding: the factor 2*n* shows the exponential growth of stretching, which results in sensitive dependence on initial conditions, while the squared sine function keeps xn folded within the range [0,1].

For *r* = 4 an equivalent solution in terms of complex numbers instead of trigonometric functions is

$x_{n}={\frac {-\alpha ^{2^{n}}-\alpha ^{-2^{n}}+2}{4}}$

where α is either of the complex numbers

$\alpha =1-2x_{0}\pm {\sqrt {\left(1-2x_{0}\right)^{2}-1}}$

with modulus equal to 1. Just as the squared sine function in the trigonometric solution leads to neither shrinkage nor expansion of the set of points visited, in the latter solution this effect is accomplished by the unit modulus of α.

By contrast, the solution when *r* = 2 is

$x_{n}={\tfrac {1}{2}}-{\tfrac {1}{2}}\left(1-2x_{0}\right)^{2^{n}}$

for *x*0 ∈ [0,1). Since (1 − 2*x*0) ∈ (−1,1) for any value of *x*0 other than the unstable fixed point 0, the term (1 − 2*x*0)2*n* goes to 0 as n goes to infinity, so xn goes to the stable fixed point ⁠1/2⁠.

#### Finding cycles of any length when *r* = 4

For the *r* = 4 case, from almost all initial conditions the iterate sequence is chaotic. Nevertheless, there exist an infinite number of initial conditions that lead to cycles, and indeed there exist cycles of length k for *all* integers *k* > 0. We can exploit the relationship of the logistic map to the dyadic transformation (also known as the *bit-shift map*) to find cycles of any length. If x follows the logistic map *x**n* + 1 = 4*xn*(1 − *xn*) and y follows the *dyadic transformation*

$y_{n+1}={\begin{cases}2y_{n}&0\leq y_{n}<{\tfrac {1}{2}}\\2y_{n}-1&{\tfrac {1}{2}}\leq y_{n}<1,\end{cases}}$

then the two are related by a homeomorphism

$x_{n}=\sin ^{2}\left(2\pi y_{n}\right).$

The reason that the dyadic transformation is also called the bit-shift map is that when y is written in binary notation, the map moves the binary point one place to the right (and if the bit to the left of the binary point has become a "1", this "1" is changed to a "0"). A cycle of length 3, for example, occurs if an iterate has a 3-bit repeating sequence in its binary expansion (which is not also a one-bit repeating sequence): 001, 010, 100, 110, 101, or 011. The iterate 001001001... maps into 010010010..., which maps into 100100100..., which in turn maps into the original 001001001...; so this is a 3-cycle of the bit shift map. And the other three binary-expansion repeating sequences give the 3-cycle 110110110... → 101101101... → 011011011... → 110110110.... Either of these 3-cycles can be converted to fraction form: for example, the first-given 3-cycle can be written as ⁠1/7⁠ → ⁠2/7⁠ → ⁠4/7⁠ → ⁠1/7⁠. Using the above translation from the bit-shift map to the $r=4$ logistic map gives the corresponding logistic cycle 0.611260467... → 0.950484434... → 0.188255099... → 0.611260467.... We could similarly translate the other bit-shift 3-cycle into its corresponding logistic cycle. Likewise, cycles of any length k can be found in the bit-shift map and then translated into the corresponding logistic cycles.

However, since almost all numbers in [0,1) are irrational, almost all initial conditions of the bit-shift map lead to the non-periodicity of chaos. This is one way to see that the logistic *r* = 4 map is chaotic for almost all initial conditions.

The number of cycles of (minimal) length *k* = 1, 2, 3,… for the logistic map with *r* = 4 (tent map with *μ* = 2) is a known integer sequence (sequence A001037 in the OEIS): 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335, 630, 1161.... This means that the logistic map with *r* = 4 has 2 fixed points, 1 cycle of length 2, 2 cycles of length 3 and so on. This sequence takes a particularly simple form for prime k: 2 ⋅ ⁠2*k* − 1 − 1/*k*⁠. For example: 2 ⋅ ⁠213 − 1 − 1/13⁠ = 630 is the number of cycles of length 13. Since this case of the logistic map is chaotic for almost all initial conditions, all of these finite-length cycles are unstable.
