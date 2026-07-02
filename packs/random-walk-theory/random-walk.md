---
title: "Random walk"
source: https://en.wikipedia.org/wiki/Random_walk
domain: random-walk-theory
license: CC-BY-SA-4.0
tags: random walk, self-avoiding walk, markov chain, gambler's ruin
fetched: 2026-07-02
---

# Random walk

In mathematics, a **random walk** is a stochastic process that describes a path that consists of a succession of random steps on some mathematical space.

An elementary example of a random walk is one on the integer number line $\mathbb {Z}$ which starts at 0, and at each step moves +1 or −1 with equal probability. Other examples include the path traced by a molecule as it travels in a liquid or a gas (see Brownian motion), the search path of a foraging animal, or the price of a fluctuating stock and the financial status of a gambler. Random walks have applications to engineering and many scientific fields including ecology, psychology, computer science, physics, chemistry, biology, economics, and sociology. The term *random walk* was first introduced by Karl Pearson in 1905.

Realizations of random walks can be obtained by Monte Carlo simulation.

In certain contexts random walk is sometimes known as a **drunkard's walk**.

## Lattice random walk

A popular random walk model is that of a random walk on a regular lattice, where at each step the location jumps to another site according to some probability distribution. In a *simple random walk*, the location can only jump to neighboring sites of the lattice, forming a lattice path. In a *simple symmetric random walk* on a locally finite lattice, the probabilities of the location jumping to each one of its immediate neighbors are the same. The best-studied example is the random walk on the *d*-dimensional integer lattice (sometimes called the hypercubic lattice) $\mathbb {Z} ^{d}$ . If, in addition, the state space is finite, the random walk model is called a *simple bordered symmetric random walk*, and the transition probabilities depend on the location of the state because on margin and corner states the movement is limited.

### One-dimensional random walk

An elementary example of a random walk is the random walk on the integer number line, $\mathbb {Z}$ , which starts at 0 and at each step moves +1 or −1 with equal probability.

This walk can be illustrated as follows. A marker is placed at zero on the number line, and a fair coin is flipped. If it lands on heads, the marker is moved one unit to the right. If it lands on tails, the marker is moved one unit to the left. After five flips, the marker could now be on -5, -3, -1, 1, 3, 5. With five flips, three heads and two tails, in any order, it will land on 1. There are 10 ways of landing on 1 (by flipping three heads and two tails), 10 ways of landing on −1 (by flipping three tails and two heads), 5 ways of landing on 3 (by flipping four heads and one tail), 5 ways of landing on −3 (by flipping four tails and one head), 1 way of landing on 5 (by flipping five heads), and 1 way of landing on −5 (by flipping five tails). See the figure below for an illustration of the possible outcomes of 5 flips.

To define this walk formally, take independent random variables $Z_{1},Z_{2},\dots$ , where each variable is either 1 or −1, with a 50% probability for either value, and set $S_{0}=0$ and ${\textstyle S_{n}=\sum _{j=1}^{n}Z_{j}.}$ The series $\{S_{n}\}$ is called the *simple random walk on $\mathbb {Z}$*. This series (the sum of the sequence of −1s and 1s) gives the net distance walked, if each part of the walk is of length one. The expectation $E(S_{n})$ of $S_{n}$ is zero. That is, the mean of all coin flips approaches zero as the number of flips increases. This follows by the finite additivity property of expectation: $E(S_{n})=\sum _{j=1}^{n}E(Z_{j})=0.$

A similar calculation, using the independence of the random variables and the fact that $E(Z_{n}^{2})=1$ , shows that: $E(S_{n}^{2})=\sum _{i=1}^{n}E(Z_{i}^{2})+2\sum _{1\leq i<j\leq n}E(Z_{i}Z_{j})=n.$

This hints that $E(|S_{n}|)\,\!$ , the expected translation distance after *n* steps, should be of the order of ${\sqrt {n}}$ . In fact, $\lim _{n\to \infty }{\frac {E(|S_{n}|)}{\sqrt {n}}}={\sqrt {\frac {2}{\pi }}}.$

To answer the question of how many times will a random walk cross a boundary line if permitted to continue walking forever, a simple random walk on $\mathbb {Z}$ will cross every point an infinite number of times. This result has many names: the *level-crossing phenomenon*, *recurrence* or the *gambler's ruin*. The reason for the last name is as follows: a gambler with a finite amount of money will eventually lose when playing *a fair game* against a bank with an infinite amount of money. The gambler's money will perform a random walk, and it will reach zero at some point, and the game will be over.

If *a* and *b* are positive integers, then the expected number of steps until a one-dimensional simple random walk starting at 0 first hits *b* or −*a* is *ab*. The probability that this walk will hit *b* before −*a* is $a/(a+b)$ , which can be derived from the fact that simple random walk is a martingale. And these expectations and hitting probabilities can be computed in $O(a+b)$ in the general one-dimensional random walk Markov chain.

Some of the results mentioned above can be derived from properties of Pascal's triangle. The number of different walks of *n* steps where each step is +1 or −1 is 2*n*. For the simple random walk, each of these walks is equally likely. In order for *Sn* to be equal to a number *k* it is necessary and sufficient that the number of +1 in the walk exceeds those of −1 by *k*. It follows +1 must appear (*n* + *k*)/2 times among *n* steps of a walk, hence the number of walks which satisfy $S_{n}=k$ equals the number of ways of choosing (*n* + *k*)/2 elements from an *n* element set, denoted ${\textstyle n \choose (n+k)/2}$ . For this to have meaning, it is necessary that *n* + *k* be an even number, which implies *n* and *k* are either both even or both odd. Therefore, the probability that $S_{n}=k$ is equal to ${\textstyle 2^{-n}{n \choose (n+k)/2}}$ . By representing entries of Pascal's triangle in terms of factorials and using Stirling's formula, one can obtain good estimates for these probabilities for large values of n .

This relation with Pascal's triangle is demonstrated for small values of *n*. At zero turns, the only possibility will be to remain at zero. However, at one turn, there is one chance of landing on −1 or one chance of landing on 1. At two turns, a marker at 1 could move to 2 or back to zero. A marker at −1, could move to −2 or back to zero. Therefore, there is one chance of landing on −2, two chances of landing on zero, and one chance of landing on 2.

k

−5

−4

−3

−2

−1

0

1

2

3

4

5

$P[S_{0}=k]$

1

$2P[S_{1}=k]$

1

1

$2^{2}P[S_{2}=k]$

1

2

1

$2^{3}P[S_{3}=k]$

1

3

3

1

$2^{4}P[S_{4}=k]$

1

4

6

4

1

$2^{5}P[S_{5}=k]$

1

5

10

10

5

1

The central limit theorem and the law of the iterated logarithm describe important aspects of the behavior of simple random walks on $\mathbb {Z}$ . In particular, the former entails that as *n* increases, the probabilities (proportional to the numbers in each row) approach a normal distribution.

To be precise, knowing that ${\textstyle \mathbb {P} (X_{n}=k)=2^{-n}{\binom {n}{(n+k)/2}}}$ , and using Stirling's formula one has

${\log \mathbb {P} (X_{n}=k)}=n\left[\left({1+{\frac {k}{n}}+{\frac {1}{2n}}}\right)\log \left(1+{\frac {k}{n}}\right)+\left({1-{\frac {k}{n}}+{\frac {1}{2n}}}\right)\log \left(1-{\frac {k}{n}}\right)\right]+\log {\frac {\sqrt {2}}{\sqrt {\pi }}}+o(1).$

Fixing the scaling ${\textstyle k=\lfloor {\sqrt {n}}x\rfloor }$ , for ${\textstyle x}$ fixed, and using the expansion ${\textstyle \log(1+{k}/{n})=k/n-k^{2}/2n^{2}+\dots }$ when ${\textstyle k/n}$ vanishes, it follows

${\mathbb {P} \left({\frac {X_{n}}{n}}={\frac {\lfloor {\sqrt {n}}x\rfloor }{\sqrt {n}}}\right)}={\frac {1}{\sqrt {n}}}{\frac {1}{2{\sqrt {\pi }}}}e^{-{x^{2}}}(1+o(1)).$

taking the limit (and observing that ${\textstyle {1}/{\sqrt {n}}}$ corresponds to the spacing of the scaling grid) one finds the gaussian density ${\textstyle f(x)={\frac {1}{2{\sqrt {\pi }}}}e^{-{x^{2}}}}$ . Indeed, for a absolutely continuous random variable ${\textstyle X}$ with density ${\textstyle f_{X}}$ it holds ${\textstyle \mathbb {P} \left(X\in [x,x+dx)\right)=f_{X}(x)dx}$ , with ${\textstyle dx}$ corresponding to an infinitesimal spacing.

As a direct generalization, one can consider random walks on crystal lattices (infinite-fold abelian covering graphs over finite graphs). Actually it is possible to establish the central limit theorem and large deviation theorem in this setting.

#### As a Markov chain

A one-dimensional *random walk* can also be looked at as a Markov chain whose state space is given by the integers $i=0,\pm 1,\pm 2,\dots .$ For some number *p* satisfying $\,0<p<1$ , the transition probabilities (the probability *Pi,j* of moving from state *i* to state *j*) are given by $\,P_{i,i+1}=p=1-P_{i,i-1}.$

#### Heterogeneous generalization

The heterogeneous random walk draws in each time step a random number that determines the local jumping probabilities and then a random number that determines the actual jump direction. The main question is the probability of staying in each of the various sites after t jumps, and in the limit of this probability when t is very large.

### Higher dimensions

In higher dimensions, the set of randomly walked points has interesting geometric properties. In fact, one gets a discrete fractal, that is, a set which exhibits stochastic self-similarity on large scales. On small scales, one can observe "jaggedness" resulting from the grid on which the walk is performed. The trajectory of a random walk is the collection of points visited, considered as a set with disregard to *when* the walk arrived at the point. In one dimension, the trajectory is simply all points between the minimum height and the maximum height the walk achieved (both are, on average, on the order of ${\sqrt {n}}$ ).

To visualize the two-dimensional case, one can imagine a person walking randomly around a city. The city is effectively infinite and arranged in a square grid of sidewalks. At every intersection, the person randomly chooses one of the four possible routes (including the one originally travelled from). Formally, this is a random walk on the set of all points in the plane with integer coordinates.

To answer the question of the person ever getting back to the original starting point of the walk, this is the 2-dimensional equivalent of the level-crossing problem discussed above. In 1921 George Pólya proved that the person almost surely would in a 2-dimensional random walk, but for 3 dimensions or higher, the probability of returning to the origin decreases as the number of dimensions increases. In 3 dimensions, the probability decreases to roughly 34%. The mathematician Shizuo Kakutani was known to refer to this result with the following quote: "A drunk man will find his way home, but a drunk bird may get lost forever".

The probability of recurrence is in general $p=1-\left({\frac {1}{(2\pi )^{d}}}\int _{[-\pi ,\pi ]^{d}}{\frac {\prod _{i=1}^{d}d\theta _{i}}{1-{\frac {1}{d}}\sum _{i=1}^{d}\cos \theta _{i}}}\right)^{-1}$ , which can be derived by generating functions or Poisson process.

Another variation of this question which was also asked by Pólya is: "if two people leave the same starting point, then will they ever meet again?" It can be shown that the difference between their locations (two independent random walks) is also a simple random walk, so they almost surely meet again in a 2-dimensional walk, but for 3 dimensions and higher the probability decreases with the number of the dimensions. Paul Erdős and Samuel James Taylor also showed in 1960 that for dimensions less or equal than 4, two independent random walks starting from any two given points have infinitely many intersections almost surely, but for dimensions higher than 5, they almost surely intersect only finitely often.

The asymptotic function for a two-dimensional random walk as the number of steps increases is given by a Rayleigh distribution. The probability distribution is a function of the radius from the origin and the step length is constant for each step. Here, the step length is assumed to be 1, N is the total number of steps and r is the radius from the origin.

$P(r)={\frac {2r}{N}}e^{-r^{2}/N}$

### Relation to Wiener process

A Wiener process is a stochastic process with similar behavior to Brownian motion, the physical phenomenon of a minute particle diffusing in a fluid. (Sometimes the Wiener process is called "Brownian motion", although this is strictly speaking a confusion of a model with the phenomenon being modeled.)

A Wiener process is the scaling limit of random walk in dimension 1. This means that if there is a random walk with very small steps, there is an approximation to a Wiener process (and, less accurately, to Brownian motion). To be more precise, if the step size is ε, one needs to take a walk of length *L*/ε2 to approximate a Wiener length of *L*. As the step size tends to 0 (and the number of steps increases proportionally), random walk converges to a Wiener process in an appropriate sense. Formally, if *B* is the space of all paths of length *L* with the maximum topology, and if *M* is the space of measure over *B* with the norm topology, then the convergence is in the space *M*. Similarly, a Wiener process in several dimensions is the scaling limit of random walk in the same number of dimensions.

A random walk is a discrete fractal (a function with integer dimensions; 1, 2, ...), but a Wiener process trajectory is a true fractal, and there is a connection between the two. For example, take a random walk until it hits a circle of radius *r* times the step length. The average number of steps it performs is *r*2. This fact is the *discrete version* of the fact that a Wiener process walk is a fractal of Hausdorff dimension 2.

In two dimensions, the average number of points the same random walk has on the *boundary* of its trajectory is *r*4/3. This corresponds to the fact that the boundary of the trajectory of a Wiener process is a fractal of dimension 4/3, a fact predicted by Mandelbrot using simulations but proved only in 2000 by Lawler, Schramm and Werner.

A Wiener process enjoys many symmetries a random walk does not. For example, a Wiener process walk is invariant to rotations, but the random walk is not, since the underlying grid is not (random walk is invariant to rotations by 90 degrees, but Wiener processes are invariant to rotations by, for example, 17 degrees too). This means that in many cases, problems on a random walk are easier to solve by translating them to a Wiener process, solving the problem there, and then translating back. On the other hand, some problems are easier to solve with random walks due to its discrete nature.

Random walk and Wiener process can be *coupled*, namely manifested on the same probability space in a dependent way that forces them to be quite close. The simplest such coupling is the Skorokhod embedding, but there exist more precise couplings, such as Komlós–Major–Tusnády approximation theorem.

The convergence of a random walk toward the Wiener process is controlled by the central limit theorem, and by Donsker's theorem. For a particle in a known fixed position at *t* = 0, the central limit theorem tells us that after a large number of independent steps in the random walk, the walker's position is distributed according to a normal distribution of total variance:

$\sigma ^{2}={\frac {t}{\delta t}}\,\varepsilon ^{2},$

where *t* is the time elapsed since the start of the random walk, $\varepsilon$ is the size of a step of the random walk, and $\delta t$ is the time elapsed between two successive steps.

This corresponds to the Green's function of the diffusion equation that controls the Wiener process, which suggests that, after a large number of steps, the random walk converges toward a Wiener process.

In 3D, the variance corresponding to the Green's function of the diffusion equation is: $\sigma ^{2}=6\,D\,t.$

By equalizing this quantity with the variance associated to the position of the random walker, one obtains the equivalent diffusion coefficient to be considered for the asymptotic Wiener process toward which the random walk converges after a large number of steps: $D={\frac {\varepsilon ^{2}}{6\delta t}}$ (valid only in 3D).

The two expressions of the variance above correspond to the distribution associated to the vector ${\vec {R}}$ that links the two ends of the random walk, in 3D. The variance associated to each component $R_{x}$ , $R_{y}$ or $R_{z}$ is only one third of this value (still in 3D).

For 2D:

$D={\frac {\varepsilon ^{2}}{4\delta t}}.$

For 1D:

$D={\frac {\varepsilon ^{2}}{2\delta t}}.$

## Gaussian random walk

A random walk having a step size that varies according to a normal distribution ${\mathcal {N}}(\mu ,\sigma ^{2})$ , $\mu$ being the mean and $\sigma$ being the standard deviation, is used as a model for real-world time-series data such as financial markets.

Here, the step size is given by the inverse cumulative normal distribution $\Phi ^{-1}(x,\mu ,\sigma ),$ where $x\in \{0,1\}$ is a uniformly distributed random number.

If $\mu$ is nonzero, the random walk will vary about a linear trend. If $v_{s}$ is the starting value of the random walk, the expected value after n steps will be $v_{s}+n\mu$ .

For the special case where $\mu =0$ , after n steps the translation distance's probability distribution is given by ${\mathcal {N}}(0,n\sigma ^{2}).$

Proof: The Gaussian random walk can be thought of as the sum of a sequence of n independent and identically distributed random variables (steps) $x_{i}$ from the inverse cumulative normal distribution with $\mu =0:$ $X=\sum _{i=0}^{n}{x_{i}},$ whereas from the assumption of σ-additivity, it is the case that *the sum of independent normally distributed random variables will have an approximately normal probability distribution of the sum of independent random variables* , therefore $X=\sum _{i=0}^{n}{x_{i}}\sim {\mathcal {N}}(0,n\sigma ^{2}).$

For steps distributed according to any distribution with zero mean and a finite variance (not necessarily just a normal distribution), the root mean square translation distance after n steps is ${\sqrt {Var(S_{n})}}={\sqrt {E[S_{n}^{2}]}}=\sigma {\sqrt {n}}.$

But for the Gaussian random walk, this is just the standard deviation of the translation distance's distribution after n steps. Hence, if $\mu =0$ , and since the root mean square (RMS) translation distance is one standard deviation, there is a 68.27% probability that the RMS translation distance after n steps will fall between $\pm \sigma {\sqrt {n}}$ . Likewise, there is a 50% probability that the translation distance after n steps will fall between $\pm 0.6745\sigma {\sqrt {n}}.$

### Number of distinct sites

The number of distinct sites visited by a single random walker $S(t)$ has been studied extensively for square and cubic lattices and for fractals. This quantity is useful for the analysis of problems of trapping and kinetic reactions. It is also related to the vibrational density of states, diffusion reactions processes and spread of populations in ecology.

### Information rate

The information rate of a Gaussian random walk with respect to the squared error distance, i.e. its quadratic rate distortion function, is given parametrically by $R(D_{\theta })={\frac {1}{2}}\int _{0}^{1}\max\{0,\log _{2}\left(S(\varphi )/\theta \right)\}\,d\varphi ,$ $D_{\theta }=\int _{0}^{1}\min\{S(\varphi ),\theta \}\,d\varphi ,$ where $S(\varphi )=\left(2\sin(\pi \varphi /2)\right)^{-2}$ . Therefore, it is impossible to encode ${\{Z_{n}\}_{n=1}^{N}}$ using a binary code of less than $NR(D_{\theta })$ bits and recover it with expected mean squared error less than $D_{\theta }$ . On the other hand, for any $\varepsilon >0$ , there exists an $N\in \mathbb {N}$ large enough and a binary code of no more than $2^{NR(D_{\theta })}$ distinct elements such that the expected mean squared error in recovering ${\{Z_{n}\}_{n=1}^{N}}$ from this code is at most $D_{\theta }-\varepsilon$ .

## Applications

### Applications in financial economics

In financial economics, the random walk hypothesis is used to model share prices and other factors. Empirical studies found some deviations from this theoretical model, especially in short term and long term correlations.

### Applications in semiconductor manufacturing

In semiconductor manufacturing, random walks are used to analyze the effects of thermal treatment at smaller nodes. It is applied to understand the diffusion of dopants, defects and other impurities during the critical fabrication steps. Random walk treatments are also used to study the diffusion of reactants, products and plasma during chemical vapor deposition processes. Continuum diffusion has been used to study the flow of gases, at macroscopic scales, in CVD reactors. However, smaller dimensions and increased complexity has forced us to treat them with random walk. This allows for accurate analysis of stochastic processes, at molecular level and smaller, in semiconductor manufacturing.

### Applications in computer science

In computer science, random walks have been used to estimate the size of the Web. In computer programming it is possible to calculate pi with a random walk.

Random walks have been used in network analysis to calculate the probability two unlinked nodes will be linked in the future based on the current state of the network. Various algorithms are discussed in including PageRank and supervised random walks.

In image segmentation, random walks are used to determine the labels (i.e., "object" or "background") to associate with each pixel. This algorithm is typically referred to as the random walker segmentation algorithm.

The Twitter website used random walks to make suggestions of whom to follow.

### Applications to natural phenomena

As mentioned, the range of natural phenomena which have been subject to attempts at description by some flavour of random walks is considerable. This is particularly the case in the fields of physics, chemistry, materials science, and biology.

#### Biology

- Motile bacteria engage in biased random walks.
- In brain research, random walks and reinforced random walks are used to model cascades of neuron firing in the brain.
- In population genetics, random walk describes the statistical properties of genetic drift or long-term randomly fluctuating selection.
- In mathematical ecology, random walks are used to describe individual animal movements, to empirically support processes of biodiffusion, and occasionally to model population dynamics.
- In vision science, ocular drift tends to behave like a random walk. According to some authors, fixational eye movements in general are also well described by a random walk.

#### Physics

- In physics, random walks underlie the method of Fermi estimation.
- In physics, random walks are used as simplified models of physical Brownian motion and diffusion such as the random movement of molecules in liquids and gases. See for example diffusion-limited aggregation. Also in physics, random walks and some of the self interacting walks play a role in quantum field theory.
- astrophysics: antiprotons generated by spallation in the interstellar medium random walk through space
- In polymer physics, random walk describes an ideal chain. It is the simplest model to study polymers.
- In other fields of mathematics, random walk is used to calculate solutions to Laplace's equation, to estimate the harmonic measure, and for various constructions in analysis and combinatorics.

#### Psychology

- In psychology, random walks explain accurately the relation between the time needed to make a decision and the probability that a certain decision will be made.

## Variants

A number of types of stochastic processes have been considered that are similar to the pure random walks but where the simple structure is allowed to be more generalized. The *pure* structure can be characterized by the steps being defined by independent and identically distributed random variables. Random walks can take place on a variety of spaces, such as graphs, the integers, the real line, the plane or higher-dimensional vector spaces, on curved surfaces or higher-dimensional Riemannian manifolds, and on groups. It is also possible to define random walks which take their steps at random times, and in that case, the position X t has to be defined for all times *t* ∈ [0, +∞). Specific cases or limits of random walks include the Lévy flight and diffusion models such as Brownian motion.

### On graphs

A random walk of length *k* on a possibly infinite graph *G* with a root *0* is a stochastic process with random variables $X_{1},X_{2},\dots ,X_{k}$ such that $X_{1}=0$ and ${X_{i+1}}$ is a vertex chosen uniformly at random from the neighbors of $X_{i}$ . Then the number $p_{v,w,k}(G)$ is the probability that a random walk of length *k* starting at *v* ends at *w*. In particular, if *G* is a graph with root *0*, $p_{0,0,2k}$ is the probability that a $2k$ -step random walk returns to *0*.

Building on the analogy from the earlier section on higher dimensions, assume now that our city is no longer a perfect square grid. When our person reaches a certain junction, he picks between the variously available roads with equal probability. Thus, if the junction has seven exits the person will go to each one with probability one-seventh. This is a random walk on a graph. Will our person reach his home? It turns out that under rather mild conditions, the answer is still yes, but depending on the graph, the answer to the variant question 'Will two persons meet again?' may not be that they meet infinitely often almost surely.

An example of a case where the person will reach his home almost surely is when the lengths of all the blocks are between *a* and *b* (where *a* and *b* are any two finite positive numbers). Notice that we do not assume that the graph is planar, i.e. the city may contain tunnels and bridges. One way to prove this result is using the connection to electrical networks. Take a map of the city and place a one ohm resistor on every block. Now measure the "resistance between a point and infinity". In other words, choose some number *R* and take all the points in the electrical network with distance bigger than *R* from our point and wire them together. This is now a finite electrical network, and we may measure the resistance from our point to the wired points. Take *R* to infinity. The limit is called the *resistance between a point and infinity*. It turns out that the following is true (an elementary proof can be found in the book by Doyle and Snell):

**Theorem**: *a graph is transient if and only if the resistance between a point and infinity is finite. It is not important which point is chosen if the graph is connected.*

In other words, in a transient system, one only needs to overcome a finite resistance to get to infinity from any point. In a recurrent system, the resistance from any point to infinity is infinite.

This characterization of transience and recurrence is very useful, and specifically it allows us to analyze the case of a city drawn in the plane with the distances bounded.

A random walk on a graph is a very special case of a Markov chain. Unlike a general Markov chain, random walk on a graph enjoys a property called *time symmetry* or *reversibility*. Roughly speaking, this property, also called the principle of detailed balance, means that the probabilities to traverse a given path in one direction or the other have a very simple connection between them (if the graph is regular, they are just equal). This property has important consequences.

Starting in the 1980s, much research has gone into connecting properties of the graph to random walks. In addition to the electrical network connection described above, there are important connections to isoperimetric inequalities, see more here, functional inequalities such as Sobolev and Poincaré inequalities and properties of solutions of Laplace's equation. A significant portion of this research was focused on Cayley graphs of finitely generated groups. In many cases these discrete results carry over to, or are derived from manifolds and Lie groups.

In the context of random graphs, particularly that of the Erdős–Rényi model, analytical results to some properties of random walkers have been obtained. These include the distribution of first and last hitting times of the walker, where the first hitting time is given by the first time the walker steps into a previously visited site of the graph, and the last hitting time corresponds the first time the walker cannot perform an additional move without revisiting a previously visited site.

A good reference for random walk on graphs is the online book by Aldous and Fill. For groups see the book of Woess. If the transition kernel $p(x,y)$ is itself random (based on an environment $\omega$ ) then the random walk is called a "random walk in random environment". When the law of the random walk includes the randomness of $\omega$ , the law is called the annealed law; on the other hand, if $\omega$ is seen as fixed, the law is called a quenched law. See the book of Hughes, the book of Revesz, or the lecture notes of Zeitouni.

We can think about choosing every possible edge with the same probability as maximizing uncertainty (entropy) locally. We could also do it globally – in maximal entropy random walk (MERW) we want all paths to be equally probable, or in other words: for every two vertexes, each path of given length is equally probable. This random walk has much stronger localization properties.

### Self-interacting random walks

There are a number of interesting models of random paths in which each step depends on the past in a complicated manner. All are more complex for solving analytically than the usual random walk; still, the behavior of any model of a random walker is obtainable using computers. Examples include:

- The self-avoiding walk.

The self-avoiding walk of length *n* on $\mathbb {Z} ^{d}$ is the random *n*-step path which starts at the origin, makes transitions only between adjacent sites in $\mathbb {Z} ^{d}$ , never revisit a site, and is chosen uniformly among all such paths. In two dimensions, due to self-trapping, a typical self-avoiding walk is very short, while in higher dimension it grows beyond all bounds. This model has often been used in polymer physics (since the 1960s).

- The loop-erased random walk.
- The reinforced random walk.
- The exploration process.
- The multiagent random walk.

### Biased random walks on graphs

### Maximal entropy random walk

Random walk chosen to maximize entropy rate, has much stronger localization properties.

### Correlated random walks

Random walks where the direction of movement at one time is correlated with the direction of movement at the next time. It is used to model animal movements.
