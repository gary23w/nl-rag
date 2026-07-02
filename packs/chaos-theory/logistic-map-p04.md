---
title: "Logistic map (part 4/4)"
source: https://en.wikipedia.org/wiki/Logistic_map
domain: chaos-theory
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
part: 4/4
---

## Universality

### A class of mappings that exhibit homogeneous behavior

The bifurcation pattern shown above for the logistic map is not limited to the logistic map . It appears in a number of maps that satisfy certain conditions. The following dynamical system using sine functions is one example :

| ${\displaystyle x_{n+1}=b\sin \pi x_{n}}$ |   | 4-1 |
|---|---|---|

Here, the domain is 0 ≤ b ≤ 1 and 0 ≤ x ≤ 1 . The sine map ( 4-1 ) exhibits qualitatively identical behavior to the logistic map ( 1-2 ) : like the logistic map, it also becomes chaotic via a period doubling route as the parameter b increases, and moreover, like the logistic map, it also exhibits a window in the chaotic region .

Both the logistic map and the sine map are one-dimensional maps that map the interval [0, 1] to [0, 1] and satisfy the following property, called unimodal .

$f(0)=f(1)=0$ . The map is differentiable and there exists a unique critical point c in [0, 1] such that $f'(c)=0$ . In general, if a one-dimensional map with one parameter and one variable is unimodal and the vertex can be approximated by a second-order polynomial, then, regardless of the specific form of the map, an infinite period-doubling cascade of bifurcations will occur for the parameter range 3 ≤ r ≤ 3.56994... , and the ratio δ defined by equation ( 3-13 ) is equal to the Feigenbaum constant, 4.669... .

The pattern of stable periodic orbits that emerge from the logistic map is also universal . For a unimodal map, $x_{n+1}=cf(x_{n})$ , with parameter c, stable periodic orbits with various periods continue to emerge in a parameter interval where the two fixed points are unstable, and the pattern of their emergence (the number of stable periodic orbits with a certain period and the order of their appearance) is known to be common . In other words, for this type of map, the sequence of stable periodic orbits is the same regardless of the specific form of the map . For the logistic map, the parameter interval is 3 < a < 4, but for the sine map ( 4-1 ), the parameter interval for the common sequence of stable periodic orbits is 0.71... < b < 1 . This universal sequence of stable periodic orbits is called the U sequence .

In addition, the logistic map has the property that its Schwarzian derivative is always negative on the interval [0, 1] . The Schwarzian derivative of a map f (of class C3 ) is

| ${\displaystyle Sf(x)={\frac {f'''(x)}{f'(x)}}-{\frac {3}{2}}\left({\frac {f''(x)}{f'(x)}}\right)^{2}}$ |   | 4-2 |
|---|---|---|

In fact, when we calculate the Schwarzian derivative of the logistic map, we get

| ${\displaystyle S(ax(1-x))={\frac {-6}{(1-2x)^{2}}}<0}$ |   | 4-3 |
|---|---|---|

where the Schwarzian derivative is negative regardless of the values of a and x. It is known that if a one-dimensional mapping from [0, 1] to [0, 1] is unimodal and has a negative Schwarzian derivative, then there is at most one stable periodic orbit.

### Topological conjugate mapping

Let the symbol ∘ denote the composition of maps . In general, for  a topological space X, Y, two maps f  : X → X and g  : Y → Y are composed by a homeomorphism h : X → Y.

| ${\displaystyle h\circ f=g\circ h}$ |   | 4-4 |
|---|---|---|

f and g are said to be phase conjugates if they satisfy the relation . The concept of phase conjugation plays an important role in the study of dynamical systems . Phase conjugate f and g exhibit essentially identical behavior, and if the behavior of f is periodic, then g is also periodic, and if the behavior of f is chaotic, then g is also chaotic .

In particular, if a homeomorphism h is linear, then f and g are said to be linearly conjugate . Every quadratic function is linearly conjugate with every other quadratic function . Hence,

| ${\displaystyle x_{n+1}=x_{n}^{2}+b}$ |   | 4-5 |
|---|---|---|

| ${\displaystyle x_{n+1}=1-cx_{n}^{2}}$ |   | 4-6 |
|---|---|---|

| ${\displaystyle x_{n+1}=d-x_{n}^{2}}$ |   | 4-7 |
|---|---|---|

are linearly conjugates of the logistic map for any parameter a . Equations ( 4-6 ) and ( 4-7 ) are also called logistic maps . In particular, the form ( 4-7 ) is suitable for time-consuming numerical calculations, since it requires less computational effort .

Moreover, the logistic map $f_{a=4}$ for $r=4$ is topologically conjugate to the following tent map T  ( x ) and Bernoulli shift map B  ( x ) .

| ${\displaystyle T(x_{n})={\begin{cases}2x_{n}&\left(0\leq x_{n}\leq {\frac {1}{2}}\right)\\2(1-x_{n})&\left({\frac {1}{2}}\leq x_{n}\leq 1\right)\end{cases}}}$ |   | 4-8 |
|---|---|---|

| ${\displaystyle B(x_{n})={\begin{cases}2x_{n}&\left(0\leq x_{n}<{\frac {1}{2}}\right)\\2x_{n}-1&\left({\frac {1}{2}}\leq x_{n}\leq 1\right)\end{cases}}}$ |   | 4-9 |
|---|---|---|

These phase conjugate relations can be used to prove that the logistic map $f_{a=4}$ is strictly chaotic and to derive the exact solution ( 3-19 ) of $f_{r=4}$ .

Alternatively, introducing the concept of symbolic dynamical systems, consider the following shift map σ defined on the symbolic string space consisting of strings of 0s and 1s as introduced above :

| ${\displaystyle \sigma (s_{0}s_{1}s_{2}\cdots )=(s_{1}s_{2}\cdots )}$ |   | 4-10 |
|---|---|---|

Here, $s_{i}$ is 0 or 1. On the set $\Lambda$ introduced in equation ( 3-18 ), the logistic map $f_{r>4}$ is topologically conjugate to the shift map, so we can use this to derive that $f_{r>4}$ on $\Lambda$ is chaotic .

### Period-doubling route to chaos

In the logistic map, we have a function $f_{r}(x)=rx(1-x)$ , and we want to study what happens when we iterate the map many times. The map might fall into a fixed point, a fixed cycle, or chaos. When the map falls into a stable fixed cycle of length n , we would find that the graph of $f_{r}^{n}$ and the graph of $x\mapsto x$ intersects at n points, and the slope of the graph of $f_{r}^{n}$ is bounded in $(-1,+1)$ at those intersections.

For example, when $r=3.0$ , we have a single intersection, with slope bounded in $(-1,+1)$ , indicating that it is a stable single fixed point.

As r increases to beyond $r=3.0$ , the intersection point splits to two, which is a period doubling. For example, when $r=3.4$ , there are three intersection points, with the middle one unstable, and the two others stable.

As r approaches $r=3.45$ , another period-doubling occurs in the same way. The period-doublings occur more and more frequently, until at a certain $r\approx 3.56994567$ , the period doublings become infinite, and the map becomes chaotic. This is the period-doubling route to chaos.

Relationship between

$x_{n+2}$

and

$x_{n}$

when

$a=2.7$

. Before the period doubling bifurcation occurs. The orbit converges to the fixed point

$x_{f2}$

.

Relationship between

$x_{n+2}$

and

$x_{n}$

when

$a=3$

. The tangent slope at the fixed point

$x_{f2}$

. is exactly 1, and a period doubling bifurcation occurs.

Relationship between

$x_{n+2}$

and

$x_{n}$

when

$a=3.3$

. The fixed point

$x_{f2}$

becomes unstable, splitting into a periodic-2 stable cycle.

When

$r=3.0$

, we have a single intersection, with slope exactly

$+1$

, indicating that it is about to undergo a period-doubling.

When

$r=3.4$

, there are three intersection points, with the middle one unstable, and the two others stable.

When

$r=3.45$

, there are three intersection points, with the middle one unstable, and the two others having slope exactly

$+1$

, indicating that it is about to undergo another period-doubling.

When

$r\approx 3.56994567$

, there are infinitely many intersections, and we have arrived at

chaos via the period-doubling route

.

### Scaling limit

Looking at the images, one can notice that at the point of chaos $r^{*}=3.5699\cdots$ , the curve of $f_{r^{*}}^{\infty }$ looks like a fractal. Furthermore, as we repeat the period-doublings $f_{r^{*}}^{1},f_{r^{*}}^{2},f_{r^{*}}^{4},f_{r^{*}}^{8},f_{r^{*}}^{16},\dots$ , the graphs seem to resemble each other, except that they are shrunken towards the middle, and rotated by 180 degrees.

This suggests to us a scaling limit: if we repeatedly double the function, then scale it up by $\alpha$ for a certain constant $\alpha$ : $f(x)\mapsto -\alpha f(f(-x/\alpha ))$ then at the limit, we would end up with a function g that satisfies $g(x)=-\alpha g(g(-x/\alpha ))$ . This is a Feigenbaum function, which appears in most period-doubling routes to chaos (thus it is an instance of **universality**). Further, as the period-doubling intervals become shorter and shorter, the ratio between two period-doubling intervals converges to a limit, the first Feigenbaum constant $\delta =4.6692016\cdots$ .

The constant $\alpha$ can be numerically found by trying many possible values. For the wrong values, the map does not converge to a limit, but when it is $\alpha =2.5029\dots$ , it converges. This is the second Feigenbaum constant.

### Chaotic regime

In the chaotic regime, $f_{r}^{\infty }$ , the limit of the iterates of the map, becomes chaotic dark bands interspersed with non-chaotic bright bands.

### Other scaling limits

When r approaches $r\approx 3.8494344$ , we have another period-doubling approach to chaos, but this time with periods 3, 6, 12, ... This again has the same Feigenbaum constants $\delta ,\alpha$ . The limit of ${\textstyle f(x)\mapsto -\alpha f(f(-x/\alpha ))}$ is also the same Feigenbaum function. This is an example of **universality**.

We can also consider period-tripling route to chaos by picking a sequence of $r_{1},r_{2},\dots$ such that $r_{n}$ is the lowest value in the period- $3^{n}$ window of the bifurcation diagram. For example, we have $r_{1}=3.8284,r_{2}=3.85361,\dots$ , with the limit $r_{\infty }=3.854077963\dots$ . This has a different pair of Feigenbaum constants $\delta =55.26\dots ,\alpha =9.277\dots$ . And $f_{r}^{\infty }$ converges to the fixed point to $f(x)\mapsto -\alpha f(f(f(-x/\alpha )))$ As another example, period-4-pling has a pair of Feigenbaum constants distinct from that of period-doubling, even though period-4-pling is reached by two period-doublings. In detail, define $r_{1},r_{2},\dots$ such that $r_{n}$ is the lowest value in the period- $4^{n}$ window of the bifurcation diagram. Then we have $r_{1}=3.960102,r_{2}=3.9615554,\dots$ , with the limit $r_{\infty }=3.96155658717\dots$ . This has a different pair of Feigenbaum constants $\delta =981.6\dots ,\alpha =38.82\dots$ .

In general, each period-multiplying route to chaos has its own pair of Feigenbaum constants. In fact, there are typically more than one. For example, for period-7-pling, there are at least 9 different pairs of Feigenbaum constants.

Generally, ${\textstyle 3\delta \approx 2\alpha ^{2}}$ , and the relation becomes exact as both numbers increase to infinity: $\lim \delta /\alpha ^{2}=2/3$ .

### Feigenbaum universality of 1-D maps

Universality of one-dimensional maps with parabolic maxima and Feigenbaum constants $\delta =4.669201...$ , $\alpha =2.502907...$ .

The gradual increase of G at interval $[0,\infty )$ changes dynamics from regular to chaotic one with qualitatively the same bifurcation diagram as those for logistic map.

### Renormalization estimate

The Feigenbaum constants can be estimated by a renormalization argument. (Section 10.7,).

By universality, we can use another family of functions that also undergoes repeated period-doubling on its route to chaos, and even though it is not exactly the logistic map, it would still yield the same Feigenbaum constants.

Define the family $f_{r}(x)=-(1+r)x+x^{2}$ The family has an equilibrium point at zero, and as r increases, it undergoes period-doubling bifurcation at $r=r_{0},r_{1},r_{2},...$ .

The first bifurcation occurs at $r=r_{0}=0$ . After the period-doubling bifurcation, we can solve for the period-2 stable orbit by $f_{r}(p)=q,f_{r}(q)=p$ , which yields ${\begin{cases}p={\frac {1}{2}}(r+{\sqrt {r(r+4)}})\\q={\frac {1}{2}}(r-{\sqrt {r(r+4)}})\end{cases}}$ At some point $r=r_{1}$ , the period-2 stable orbit undergoes period-doubling bifurcation again, yielding a period-4 stable orbit. In order to find out what the stable orbit is like, we "zoom in" around the region of $x=p$ , using the affine transform $T(x)=x/c+p$ . Now, by routine algebra, we have $(T^{-1}\circ f_{r}^{2}\circ T)(x)=-(1+S(r))x+x^{2}+O(x^{3})$ where $S(r)=r^{2}+4r-2,c=r^{2}+4r-3{\sqrt {r(r+4)}}$ . At approximately $S(r)=0$ , the second bifurcation occurs, thus $S(r_{1})\approx 0$ .

By self-similarity, the third bifurcation when $S(r)\approx r_{1}$ , and so on. Thus we have $r_{n}\approx S(r_{n+1})$ , or $r_{n+1}\approx {\sqrt {r_{n}+6}}-2$ . Iterating this map, we find $r_{\infty }=\lim _{n}r_{n}\approx \lim _{n}S^{-n}(0)={\frac {1}{2}}({\sqrt {17}}-3)$ , and $\lim _{n}{\frac {r_{\infty }-r_{n}}{r_{\infty }-r_{n+1}}}\approx S'(r_{\infty })\approx 1+{\sqrt {17}}$ .

Thus, we have the estimates $\delta \approx 1+{\sqrt {17}}=5.12...$ , and $\alpha \approx r_{\infty }^{2}+4r_{\infty }-3{\sqrt {r_{\infty }^{2}+4r_{\infty }}}\approx -2.24...$ . These are within 10% of the true values.


## Relation to logistic ordinary differential equation

The logistic map exhibits numerous characteristics of both periodic and chaotic solutions, whereas the logistic ordinary differential equation (ODE) exhibits regular solutions, commonly referred to as the S-shaped sigmoid function. The logistic map can be seen as the discrete counterpart of the logistic ODE, and their correlation has been extensively discussed in literature.


## The logistic map as a model of biological populations

### Discrete population model

While Lorenz used the logistic map in 1964, it gained widespread popularity from the research of British mathematical biologist Robert May and became widely known as a formula for considering changes in populations of organisms. In such a logistic map for organism populations, the variable $x_{n}$ represents the number of organisms living in a certain environment (more technically, the population size). Furthermore, it is assumed that no organisms leave the environment and no external organisms enter the environment (or that there is no substantial impact even if there is immigration), and the mathematical model for considering the increase or decrease in population in such a situation is the logistic map in mathematical biology.

There are two types of mathematical models for the growth of populations of organisms: discrete-time models using difference equations and continuous-time models using differential equations. For example, in the case of a type of insect that dies soon after laying eggs, the population of the insect is counted for each generation, i.e., the number of individuals in the first generation, the number of individuals in the second generation, and so on. Such examples fit the former discrete-time model. On the other hand, when the generations are continuously overlapping, it is compatible with the continuous-time model. The logistic map corresponds to such a discrete or generation-separated population model.

Let N denote the number of individuals of a single species in an environment. The simplest model for population growth is one in which the population continues to grow at a constant rate relative to the number of individuals. This type of population growth model is called the Malthusian model, and can be expressed as follows :

| ${\displaystyle N_{n+1}=\alpha N_{n}}$ |   | 5-1 |
|---|---|---|

Here, N n is the number of individuals in the nth generation, and α is the population growth rate, a positive constant . However, in model (5-1), the population continues to grow indefinitely, making it an unrealistic model for most real-world phenomena . Since there is a limit to the number of individuals that an environment can support, it seems natural that the growth rate α decreases as the population N n increases . This change in growth rate due to changes in population density is called the density effect . The following difference equation is the simplest improvement model that reflects the density effect in model (5-1).

| ${\displaystyle N_{n+1}=(a-bN_{n})N_{n}}$ |   | 5-2 |
|---|---|---|

Here, a is the maximum growth rate possible in the environment, and b is the strength of the influence of density effects . Model ( 5-2 ) assumes that the growth rate declines simply in proportion to the number of individuals. Let N n in equation (5-2) be

| ${\displaystyle x_{n}={\frac {b}{a}}N_{n}}$ |   | 5-3 |
|---|---|---|

After performing the variable transformation, the following logistic map is derived:

| ${\displaystyle x_{n+1}=a(1-x_{n})x_{n}}$ |   | 5-4 |
|---|---|---|

When using equation (5-2) or equation (5-4) as the population size of an organism, if Nn or xn becomes negative, it becomes meaningless as a population size. To prevent this, the condition 0 ≤ x0 ≤ 1 for the initial value x0 and the condition 0 ≤ r ≤ 4 for the parameter a are required.

Alternatively, we can assume a maximum population size K that the environment can support, and use this to

| ${\displaystyle N_{n+1}=a\left(1-{\frac {N_{n}}{K}}\right)N_{n}}$ |   | 5-5 |
|---|---|---|

The logistic map can be derived by considering a difference equation that incorporates density effects in the form $x_{n}=N_{n}/K$ , where the variable $x_{n}$ represents the ratio of the number of individuals $N_{n}$ to the maximum number of individuals K .

### Discretization of the logistic equation

The logistic map can also be derived from the discretization of the logistic equation for continuous-time population models. The name of the logistic map comes from Robert May's introduction of the logistic map from the discretization of the logistic equation. The logistic equation is an ordinary differential equation that describes the time evolution of a population as follows:

| ${\displaystyle {\frac {dN}{dt}}\ =rN\left(1-{\frac {N}{K}}\right)}$ |   | 5-6 |
|---|---|---|

Here, N is the number or population density of an organism, t is continuous time, and K and r are parameters. K is the carrying capacity, and r is the intrinsic rate of natural increase, which is usually positive. The left-hand side of this equation dN/dt denotes the rate of change of the population size at time t .

The logistic equation ( 5-6 ) appears similar to the logistic map ( 5-4 ), but the behavior of the solutions is quite different from that of the logistic map . As long as the initial value N 0 is positive, the population size N of the logistic equation always converges monotonically to K .

The logistic map can be derived by applying the Euler method, which is a method for numerically solving first-order ordinary differential equations, to this logistic equation . [ Note 2 ] The Euler method uses a time interval (time step size) Δt to approximate the growth rate dN/dt is approximated as follows :

| ${\displaystyle {\frac {dN}{dt}}\approx {\frac {N(t+\Delta t)-N(t)}{\Delta t}}}$ |   | 5-7 |
|---|---|---|

This approximation leads to the following logistic map :

| ${\displaystyle x_{n+1}=ax_{n}(1-x_{n})}$ |   | 5-8 |
|---|---|---|

where $x_{n}$ and a in this equation are related to the original parameters, variables, and time step size as follows :

| ${\displaystyle x_{n}={\frac {r\Delta t}{K(1+r\Delta t)}}N(n\Delta t)}$ |   | 5-9 |
|---|---|---|

| ${\displaystyle a=1+r\Delta t}$ |   | 5-10 |
|---|---|---|

If Δt is small enough, equation ( 5-8 ) serves as a valid approximation to the original equation ( 5-6 ), and coincides with the solution of the original equation as Δt → 0 . On the other hand, as Δt becomes large, the solution deviates from the original solution . Furthermore, due to the relationship in equation ( 5-10 ), increasing Δt is equivalent to increasing the parameter a . Thus, increasing Δt not only increases the error from the original equation but also produces chaotic behavior in the solution .

### Positioning

As described above, in biological population dynamics, the logistic map is one of the models of discrete growth processes. However, unlike the laws of physics, the logistic map as a model of biological population size is not derived from direct experimental results or universally valid principles . Although there is some rationality in the way it is derived, it is essentially a "model" thought up in one's mind . May, who made the logistic map famous, did not claim that the model he was discussing accurately represented the increase and decrease in population size . Historically, continuous-time models based on differential equations have been widely used in the study of biological population dynamics, and the application of these continuous-time models has deepened our understanding of biological population dynamics . As a discrete-time population model that takes into account density effects, the Ricker model, in which the population size is not negative, is more realistic .

Generally speaking, mathematical models can provide important qualitative information about population dynamics, but their results should not be taken too seriously without experimental support. Even if the conclusions of mathematical models deviate from those of biological studies, mathematical modeling is still useful because it can provide a useful control. Biological issues may be raised by reviewing the model construction process and settings, or the biological knowledge and assumptions that the model is based on. Although the logistic map is too simple to be realistic as a population model, its results suggest that a variety of population fluctuations may occur due to the dynamics inherent in the population itself, regardless of random influences from the environment.


## Applications

### Coupled map system

The degree of freedom or dimension of a one-variable logistic map as a system is one . On the other hand, in the real natural world, it is thought that there are many chaotic systems with many degrees of freedom, not only in time but also in space . Alternatively, the synchronization phenomenon of oscillators performing chaotic motion is also a research subject . To investigate such things, there is a method of coupled maps that couples many difference equations (maps) . The logistic map is often used as a subject of coupled map model research . The reason for this is that the logistic map itself has already been well investigated as a typical model of chaos, and there is an accumulation of research on it .

There are various methods for the specific coupling in the coupled map model . Suppose a total of N maps are coupled, and the state of the i-th map at time n is represented by $x_{n}(i)$ . In a method called globally coupled maps, $x_{n+1}(i)$ is formulated as follows :

| ${\displaystyle x_{n+1}(i)=(1-\epsilon )f(x_{n}(i))+{\frac {\epsilon }{N}}\sum _{j=1}^{N}f(x_{n}(j))}$ |   | 6-1 |
|---|---|---|

In the current field of coupled oscillators, the simplest model is the following, in which two oscillators, x and y, are coupled by a difference in variables :

| ${\displaystyle {\begin{cases}x_{n+1}=f(x_{n})+D(f(y_{n})-f(x_{n}))\\y_{n+1}=f(y_{n})+D(f(x_{n})-f(y_{n}))\end{cases}}}$ |   | 6-2 |
|---|---|---|

In these equations, f( x ) is the specific map to incorporate into the coupled map model, and applies here if the logistic map is used .

In equations ( 6-1 ) and ( 6-2 ), ε and D are parameters called coupling coefficients, which indicate the strength of the coupling between the maps . On the other hand, when the logistic map is incorporated into a coupled map model, the parameter a of the logistic map indicates the strength of the nonlinearity of the model . By changing the value of a and the value of ε or D, various phenomena appear in the coupled map system of logistic maps. For example, in model ( 6-2 ), when D is increased to a value Dc or more, x and y oscillate chaotically while synchronously . Even below Dc, not only do chaotic oscillations occur in a continuous manner . When D is in a certain range, x and y oscillate with two periods even though r = 4 . When a = 3.8, behavior in which synchronous and asynchronous states alternate continuously is also observed .

In a study of the application of the logistic map to a globally coupled map with a large degree of freedom ( 6-1 ), a phenomenon called chaotic itinerancy was found . This is a phenomenon in which the orbit traverses a region in phase space that is said to be the remains of an attractor, repeating the cycle from an orderly state in which several clusters oscillate together to a disordered state, then to another cluster state, then back to the disordered state again, and so on .

### Pseudorandom number generator

In the fields of computer simulation and information security, the creation of pseudorandom numbers using a computer is an important technique, and one of the methods for generating pseudorandom numbers is the use of chaos. Although a pseudorandom number generator based on chaos with sufficient performance has not yet been realized, several methods have been proposed. Several researchers have also investigated the possibility of creating a pseudorandom number generator based on chaos for the logistic map.

Parameter r = 4 is often used for pseudorandom number generation using the logistic map. Historically, as described below, in 1947, shortly after the birth of electronic computers, Stanisław Ulam and John von Neumann also pointed out the possibility of a pseudorandom number generator using the logistic map with r = 4. However, the distribution of points for the logistic map $f_{r=4}$ is as shown in equation ( 3-17 ), and the numbers that are generated are biased toward 0 and 1. Therefore, some processing is required to obtain unbiased uniform random numbers. Methods for doing so include:

A method for converting the obtained values to a uniform distribution using the tent map ( 4-8 ). The resulting number is converted to either 0 or 1 using a threshold, as in the coin tossing analogy above, and this process is repeated to obtain a uniformly random bit string. In addition, the sequences $x_{n}$ and $x_{n}+1$ obtained by the logistic map are strongly correlated, which makes it problematic for pseudorandom sequences. One way to solve this is to generate the sequence $x_{0},x_{1},x_{2},...$ for each iteration of the map, rather than generating the sequence $x_{0},x_{\tau },x_{2\tau },...$ for some number of iterations τ > 1. For example, it is said that good pseudorandom numbers can be obtained for method 1 with τ > 10 or τ > 13, and for method 2 with τ > 16.

A common problem with digitally calculating chaos using a computer is that, because a computer has a finite calculation precision, it is in principle impossible to obtain a truly aperiodic sequence, which is the nature of chaos, and instead outputs a finite periodic sequence. Even if aperiodic sequences cannot be obtained in principle, sequences with as long a period as possible are desirable for generating pseudorandom numbers. However, when the periodicity of the sequence actually output by the logistic map $f_{r=4}$ in single-precision floating-point calculations was investigated, it was reported that the period of the sequence actually output is much smaller than the maximum period possible from the number of bits allocated, and from this point of view, it has been pointed out that pseudorandom number generation by the logistic map is inferior to existing pseudorandom number generators such as the Mersenne Twister. In addition, with the logistic map, $f_{r=4}$ there is a risk that the value will fall to the fixed point 0 during the calculation and remain constant. On the other hand, the logistic map always takes values in the open interval (0, 1), so it can be calculated without problems not only with floating point but also with fixed point, and can enjoy the advantages of fixed point arithmetic. It has been pointed out that fixed point has a longer period than floating point for the same number of bits, and that unintended convergence to 0 can be eliminated.

### Extension to complex numbers

Dynamical systems defined by complex analytic functions are also of interest. An example is the dynamical system defined by the quadratic function:

| ${\displaystyle z_{n+1}=z_{n}^{2}+c}$ |   | 6-3 |
|---|---|---|

where the parameter c and the variable z are complex numbers. This map is essentially the same as the logistic map (1–2). As mentioned above, the map (6–3) is topologically conjugate to the logistic map (1–2) through a linear function.

When the iteration of the map (6–3) is calculated with a fixed parameter c and varying the initial value $z_{0}$ , a set of $z_{0}$ such that $z_{n}$ does not diverge to infinity as n → ∞ is called a filled Julia set. Furthermore, the boundary of a filled Julia set is called a Julia set. When the iteration of the map (6–3) is calculated with a fixed initial value $z_{0}=0$ and varying the parameter c, a set of c such that z does not diverge to infinity is called a Mandelbrot set. The Julia sets and Mandelbrot sets of the map (6–3) generate fractal figures that are described as "mystical looking" and "extremely mysterious".

In particular, in the Mandelbrot set, each disk in the diagram corresponds to a region of asymptotically stable periodic orbits of a certain period. By juxtaposing the logistic map orbit diagram with the Mandelbrot set diagram, it is possible to see that the asymptotically stable fixed points, period doubling bifurcations, and period-three windows of the logistic map orbit diagram correspond on the real axis to the Mandelbrot set diagram.

### When there is a time delay

If we interpret the logistic map as a model of the population of each generation of organisms, it is possible that the population of the next generation will affect not only the population of the current generation, but also the population of the generation before that. An example of such a case is

| ${\displaystyle x_{n+1}=ax_{n}(1-x_{n-1})}$ |   | 6-4 |
|---|---|---|

where the number of individuals in the previous generation, $x_{n-1}$ , is included in the equation as a negative density effect . If $x_{n+1}=y_{n}$ , then equation ( 6-4 ) can be replaced by the following two-variable difference equation .

| ${\displaystyle {\begin{cases}x_{n+1}=y_{n}\\y_{n+1}=ay_{n}(1-x_{n})\end{cases}}}$ |   | 6-5 |
|---|---|---|

This dynamical system is used to study bifurcation of quasi-periodic attractors and is called the delayed logistic map . The delayed logistic map exhibits a Neimark–Sacker bifurcation at r = 2, where the asymptotically stable fixed point becomes unstable and an asymptotically stable invariant curve forms around the unstable fixed point .


## Research history

### Before Chaos was named

Before the iteration of maps became relevant to dynamical systems, mathematicians Gaston Julia and Pierre Fatou studied the iteration of complex functions. Julia and Fatou's work was broad, focusing on analytic functions. In particular, they studied the behavior of the following complex quadratic function, also shown in equation (6–3), in the 1920s.

| ${\displaystyle z_{n+1}=z_{n}^{2}+c}$ |   | 7-1 |
|---|---|---|

Julia and Fatu also recognized chaotic behavior in Julia sets, but because there was no computer graphics at the time, no one followed suit and their research stalled. Research on complex dynamical systems then declined until the late 1970s, and it was not until the appearance of Benoit Mandelbrot and others that the rich dynamical behavior exhibited by maps on the complex plane was noticed.

In 1947, mathematicians Stanislaw Ulam and John von Neumann wrote a short paper entitled "On combination of stochastic and deterministic processes" in which they

| ${\displaystyle f(x)=4x(1-x)}$ |   | 7-2 |
|---|---|---|

They pointed out that pseudorandom numbers can be generated by the repeated composition of quadratic functions such as. In modern terms, this equation corresponds to the logistic map with r = 4. At that time, the word "chaos" had not yet been used, but Ulam and von Neumann were already paying attention to the generation of complex sequences using nonlinear functions. In their report, Ulam and von Neumann also clarified that the map (7–2) and the tent map are topologically conjugate, and that the invariant measure of the sequence of this map is given by equation (3–17).

There have since been some detailed investigations of quadratic maps of the form with arbitrary parameter a. Between 1958 and 1963, Finnish mathematician Pekka Mylberg developed the

| ${\displaystyle f(x)=x^{2}-\lambda }$ |   | 7-3 |
|---|---|---|

This line of research is essential for dynamical systems, and Mühlberg has also investigated the period-doubling branching cascades of this map, showing the existence of an accumulation point λ = 1.401155189.... Others, such as the work of the Soviet Oleksandr Sharkovsky in 1964, the French Igor Gumowski and Christian Mila in 1969, and Nicholas Metropolis in 1973, have revealed anomalous behavior of simple one-variable difference equations such as the logistic map.

### Robert May's research

Later, in the early 1970s, mathematical biologist Robert May encountered the model of equation (1–2) while working on an ecological problem. May introduced equation (1–2), i.e., the logistic map, by discretizing the logistic equation in time. He mathematically analyzed the behavior of the logistic map, and published his results in 1973 and 1974. Numerical experiments were performed on the logistic map to investigate the change in its behavior depending on the parameter r.

In 1976, he published a paper in *Nature* entitled "Simple mathematical models with very complicated dynamics". This paper was a review paper that focused on the logistic map and emphasized and drew attention to the fact that even simple nonlinear functions can produce extremely complex behaviors such as period-doubling bifurcation cascades and chaos. This paper in particular caused a great stir and was accepted by the scientific community due to May's status as a mathematical biologist, the clarity of his research results, and above all, the shocking content that a simple parabolic equation can produce surprisingly complex behavior. Through May's research, the logistic map attracted many researchers to chaos research and became such a famous mathematical model that it is said to have restarted the flow of chaos research.

### After May's research

May also drew attention to the paper by using the term "chaos", which was used by Tien-Yen Li and James York in their paper "Period three implies chaos". Although some disagree, Li and York's paper is considered the first to use the word "chaos" as a mathematical term, and is credited with coining the term "chaos" to refer to deterministic, chaotic behavior. Li and York completed the paper in 1973, but when they submitted it to *The American Mathematical Monthly*, they were told that it was too technical and that it should be significantly rewritten to make it easier to understand, and it was rejected. The paper was then left unrevised. However, the following year, in 1974, May came to give a special guest lecture at the University of Maryland where Lee and York were working, and talked about the logistic map. At the time, May did not yet understand what was happening in the chaotic domain of the logistic map, but Lee and York were also unaware of the period-doubling cascade of the logistic map. Excited by May's talk, Lee and York caught up with May after the lecture and told him about their results, which surprised May. Lee and York quickly rewrote the rejected paper, and the resubmitted paper was published in 1975.

Also, around 1975, mathematical physicist Mitchell Feigenbaum noticed a scaling law in which the branching values converged in a geometric progression when he looked at the period-doubling cascade of the logistic map, and discovered the existence of a constant, now called the Feigenbaum constant, through numerical experiments. May and George Oster had also noticed the scaling law, but they were unable to follow it in depth. Feigenbaum discovered that the same constant also appeared in the sine map shown in equation (4–1), and realized that this scaling law had a universality that went beyond the logistic map. In 1980, a rigorous proof of this result was given by Pierre Collé, Jean-Pierre Eckman, Oscar Rumford, and others. At about the same time as Feigenbaum, or later, physicists discovered the same period doubling cascade and the Feigenbaum constant in real life, and chaos, which had previously been seen as a strictly mathematical phenomenon, had a major impact on the field of physics as well.

However, there is criticism of the tendency to downplay research results from before the popularity of chaos, and to attribute many of those results to rediscoverers who used the logistic map, etc. May himself respects the existence of previous research, but positions his own achievement as not being "the first to independently discover the strange mathematical behavior of quadratic maps", but as being one of the "last researchers to emphasize their broad implications in science". Mathematician Robert Devaney states the following before explaining the logistic map in his book:

> This means that by simply iterating the quadratic function $f_{\lambda }(x)=\lambda x(1-x)$ (also known as the logistic map), we can predict the fate of the initial population $x_{0}$ . This sounds simple, but I dare to point out that it was only in the late 1990s, after the efforts of hundreds of mathematicians, that the iteration of this simple quadratic function was fully understood.


## Occurrences and similar systems

- In a toy model for discrete laser dynamics: $x\rightarrow Gx(1-\tanh(x))$ , where x stands for electric field amplitude, G is laser gain as bifurcation parameter.
- Hofstadter sequences are an example of one dimensional quasi-random, aperiodic, chaotic sequences again defined by recursion, a very special case is the logistic map
