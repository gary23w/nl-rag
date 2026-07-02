---
title: "Rate of convergence"
source: https://en.wikipedia.org/wiki/Rate_of_convergence
domain: newton-raphson-method
license: CC-BY-SA-4.0
tags: newton method, root finding algorithm, secant method, rate of convergence
fetched: 2026-07-02
---

# Rate of convergence

In mathematical analysis, particularly numerical analysis, the **rate of convergence** and **order of convergence** of a sequence that converges to a limit are any of several characterizations of how quickly that sequence approaches its limit. These are broadly divided into rates and orders of convergence that describe how quickly a sequence further approaches its limit once it is already close to it, called asymptotic rates and orders of convergence, and those that describe how quickly sequences approach their limits from starting points that are not necessarily close to their limits, called non-asymptotic rates and orders of convergence.

Asymptotic behavior is particularly useful for deciding when to stop a sequence of numerical computations, for instance once a target precision has been reached with an iterative root-finding algorithm, but pre-asymptotic behavior is often crucial for determining whether to begin a sequence of computations at all, since it may be impossible or impractical to ever reach a target precision with a poorly chosen approach. Asymptotic rates and orders of convergence are the focus of this article.

In practical numerical computations, asymptotic rates and orders of convergence follow two common conventions for two types of sequences: the first for sequences of iterations of an iterative numerical method and the second for sequences of successively more accurate numerical discretizations of a target. In formal mathematics, rates of convergence and orders of convergence are often described comparatively using asymptotic notation commonly called "big O notation," which can be used to encompass both of the prior conventions; this is an application of asymptotic analysis.

For iterative methods, a sequence $(x_{k})$ that converges to L is said to have asymptotic *order of convergence* $q\geq 1$ and asymptotic *rate of convergence* $\mu$ if

$\lim _{k\rightarrow \infty }{\frac {\left|x_{k+1}-L\right|}{\left|x_{k}-L\right|^{q}}}=\mu .$

Where methodological precision is required, these rates and orders of convergence are known specifically as the rates and orders of Q-convergence, short for quotient-convergence, since the limit in question is a quotient of error terms. The rate of convergence $\mu$ may also be called the *asymptotic error constant*, and some authors will use *rate* where this article uses *order.* Series acceleration methods are techniques for improving the rate of convergence of the sequence of partial sums of a series and possibly its order of convergence, also.

Similar concepts are used for sequences of discretizations. For instance, ideally the solution of a differential equation discretized via a regular grid will converge to the solution of the continuous equation as the grid spacing goes to zero, and if so the asymptotic rate and order of that convergence are important properties of the gridding method. A sequence of approximate grid solutions $(y_{k})$ of some problem that converges to a true solution S with a corresponding sequence of regular grid spacings $(h_{k})$ that converge to 0 is said to have asymptotic *order of convergence* q and asymptotic *rate of convergence* $\mu$ if

$\lim _{k\rightarrow \infty }{\frac {\left|y_{k}-S\right|}{h_{k}^{q}}}=\mu ,$

where the absolute value symbols stand for a metric for the space of solutions such as the uniform norm. Similar definitions also apply for non-grid discretization schemes such as the polygon meshes of a finite element method or the basis sets in computational chemistry: in general, the appropriate definition of the asymptotic rate $\mu$ will involve the asymptotic limit of the ratio of an approximation error term above to an asymptotic order q power of a discretization scale parameter below.

In general, comparatively, one sequence $(a_{k})$ that converges to a limit $L_{a}$ is said to asymptotically converge more quickly than another sequence $(b_{k})$ that converges to a limit $L_{b}$ if

$\lim _{k\rightarrow \infty }{\frac {\left|a_{k}-L_{a}\right|}{|b_{k}-L_{b}|}}=0,$

and the two are said to asymptotically converge with the same order of convergence if the limit is any positive finite value. The two are said to be asymptotically equivalent if the limit is equal to one. These comparative definitions of rate and order of asymptotic convergence are fundamental in asymptotic analysis and find wide application in mathematical analysis as a whole, including numerical analysis, real analysis, complex analysis, and functional analysis.

## Asymptotic rates of convergence for iterative methods

### Definitions

#### Q-convergence

Suppose that the sequence $(x_{k})$ of iterates of an iterative method converges to the limit number L as $k\rightarrow \infty$ . The sequence is said to *converge with order q to L* and with a *rate of convergence* $\mu$ if the $k\rightarrow \infty$ limit of quotients of absolute differences of sequential iterates $x_{k},x_{k+1}$ from their limit L satisfies

$\lim _{k\to \infty }{\frac {|x_{k+1}-L|}{|x_{k}-L|^{q}}}=\mu$

for some positive constant $\mu \in (0,1)$ if $q=1$ and $\mu \in (0,\infty )$ if $q>1$ . Other more technical rate definitions are needed if the sequence converges but ${\textstyle \lim _{k\to \infty }{\frac {|x_{k+1}-L|}{|x_{k}-L|}}=1}$ or the limit does not exist. This definition is technically called Q-convergence, short for quotient-convergence, and the rates and orders are called rates and orders of Q-convergence when that technical specificity is needed. § R-convergence, below, is an appropriate alternative when this limit does not exist.

Sequences with larger orders q converge more quickly than those with smaller order, and those with smaller rates $\mu$ converge more quickly than those with larger rates for a given order. This "smaller rates converge more quickly" behavior among sequences of the same order is standard but it can be counterintuitive. Therefore it is also common to define $-\log _{10}\mu$ as the rate; this is the "number of extra decimals of precision per iterate" for sequences that converge with order 1.

Integer powers of q are common and are given common names. Convergence with order $q=1$ and $\mu \in (0,1)$ is called *linear convergence* and the sequence is said to *converge linearly to L*. Convergence with $q=2$ and any $\mu$ is called *quadratic convergence* and the sequence is said to *converge quadratically*. Convergence with $q=3$ and any $\mu$ is called *cubic convergence*. However, it is not necessary that q be an integer. For example, the secant method, when converging to a regular, simple root, has an order of the golden ratio φ ≈ 1.618.

The common names for integer orders of convergence connect to asymptotic big O notation, where the convergence of the quotient implies ${\textstyle |x_{k+1}-L|=O(|x_{k}-L|^{q}).}$ These are linear, quadratic, and cubic polynomial expressions when q is 1, 2, and 3, respectively. More precisely, the limits imply the leading order error is exactly ${\textstyle \mu |x_{k}-L|^{q},}$ which can be expressed using asymptotic small o notation as ${\textstyle |x_{k+1}-L|=\mu |x_{k}-L|^{q}+o(|x_{k}-L|^{q}).}$

In general, when $q>1$ for a sequence or for any sequence that satisfies ${\textstyle \lim _{k\to \infty }{\frac {|x_{k+1}-L|}{|x_{k}-L|}}=0,}$ those sequences are said to *converge superlinearly* (i.e., faster than linearly). A sequence is said to *converge sublinearly* (i.e., slower than linearly) if it converges and ${\textstyle \lim _{k\to \infty }{\frac {|x_{k+1}-L|}{|x_{k}-L|}}=1.}$ Importantly, it is incorrect to say that these sublinear-order sequences converge linearly with an asymptotic rate of convergence of 1. A sequence $(x_{k})$ *converges logarithmically to L* if the sequence converges sublinearly and also ${\textstyle \lim _{k\to \infty }{\frac {|x_{k+1}-x_{k}|}{|x_{k}-x_{k-1}|}}=1.}$

#### R-convergence

The definitions of Q-convergence rates have the shortcoming that they do not naturally capture the convergence behavior of sequences that do converge, but do not converge with an asymptotically constant rate with every step, so that the Q-convergence limit does not exist. One class of examples is the staggered geometric progressions that get closer to their limits only every other step or every several steps, for instance the example ${\textstyle (b_{k})=1,1,1/4,1/4,1/16,1/16,\ldots ,1/4^{\left\lfloor {\frac {k}{2}}\right\rfloor },\ldots }$ detailed below (where ${\textstyle \lfloor x\rfloor }$ is the floor function applied to x ). The defining Q-linear convergence limits do not exist for this sequence because one subsequence of error quotients starting from odd steps converges to 1 and another subsequence of quotients starting from even steps converges to 1/4. When two subsequences of a sequence converge to different limits, the sequence does not itself converge to a limit.

In cases like these, a closely related but more technical definition of rate of convergence called R-convergence is more appropriate. The "R-" prefix stands for "root." A sequence $(x_{k})$ that converges to L is said to *converge at least R-linearly* if there exists an error-bounding sequence $(\varepsilon _{k})$ such that ${\textstyle |x_{k}-L|\leq \varepsilon _{k}\quad {\text{for all }}k}$ and $(\varepsilon _{k})$ converges Q-linearly to zero; analogous definitions hold for R-superlinear convergence, R-sublinear convergence, R-quadratic convergence, and so on.

Any error bounding sequence $(\varepsilon _{k})$ provides a lower bound on the rate and order of R-convergence and the greatest lower bound gives the exact rate and order of R-convergence. As for Q-convergence, sequences with larger orders q converge more quickly and those with smaller rates $\mu$ converge more quickly for a given order, so these greatest-rate-lower-bound error-upper-bound sequences are those that have the greatest possible q and the smallest possible $\mu$ given that q .

For the example ${\textstyle (b_{k})}$ given above, the tight bounding sequence ${\textstyle (\varepsilon _{k})=2,1,1/2,1/4,1/8,1/16,\ldots ,1/2^{k-1},\ldots }$ converges Q-linearly with rate 1/2, so ${\textstyle (b_{k})}$ converges R-linearly with rate 1/2. Generally, for any staggered geometric progression $(ar^{\lfloor k/m\rfloor })$ , the sequence will not converge Q-linearly but will converge R-linearly with rate ${\textstyle {\sqrt[{m}]{|r|}}.}$ These examples demonstrate why the "R" in R-linear convergence is short for "root."

### Examples

The geometric progression ${\textstyle (a_{k})=1,{\frac {1}{2}},{\frac {1}{4}},{\frac {1}{8}},{\frac {1}{16}},{\frac {1}{32}},\ldots ,{\bigl (}{\tfrac {1}{2}}{\bigr )}^{k},\dots }$ converges to $L=0$ . Plugging the sequence into the definition of Q-linear convergence (i.e., order of convergence 1) shows that

$\lim _{k\to \infty }{\frac {\left|1/2^{k+1}-0\right|}{\left|1/2^{k}-0\right|}}=\lim _{k\to \infty }{\frac {2^{k}}{2^{k+1}}}={\frac {1}{2}}.$

Thus $(a_{k})$ converges Q-linearly with a convergence rate of $\mu =1/2$ ; see the first plot of the figure below.

More generally, for any initial value a in the real numbers and a real number common ratio r between -1 and 1, a geometric progression $(ar^{k})$ converges linearly with rate $|r|$ and the sequence of partial sums of a geometric series ${\textstyle {\bigl (}\sum _{n=0}^{k}ar^{n}{\bigr )}}$ also converges linearly with rate $|r|$ . The same holds also for geometric progressions and geometric series parameterized by any complex numbers $a\in \mathbb {C} ,r\in \mathbb {C} ,|r|<1.$

The staggered geometric progression ${\textstyle (b_{k})=1,1,{\frac {1}{4}},{\frac {1}{4}},{\frac {1}{16}},{\frac {1}{16}},\ldots ,{\bigl (}{\tfrac {1}{4}}{\bigr )}^{\left\lfloor k/2\right\rfloor },\ldots ,}$ using the floor function ${\textstyle \lfloor x\rfloor }$ that gives the largest integer that is less than or equal to $x,$ converges R-linearly to 0 with rate 1/2, but it does not converge Q-linearly; see the second plot of the figure below. The defining Q-linear convergence limits do not exist for this sequence because one subsequence of error quotients starting from odd steps converges to 1 and another subsequence of quotients starting from even steps converges to 1/4. When two subsequences of a sequence converge to different limits, the sequence does not itself converge to a limit. Generally, for any staggered geometric progression $(ar^{\lfloor k/m\rfloor })$ , the sequence will not converge Q-linearly but will converge R-linearly with rate ${\textstyle {\sqrt[{m}]{|r|}};}$ these examples demonstrate why the "R" in R-linear convergence is short for "root."

The sequence $(c_{k})={\frac {1}{2}},{\frac {1}{4}},{\frac {1}{16}},{\frac {1}{256}},{\frac {1}{65,\!536}},\ldots ,{\frac {1}{2^{2^{k}}}},\ldots$ converges to zero Q-superlinearly. In fact, it is quadratically convergent with a quadratic convergence rate of 1. It is shown in the third plot of the figure below.

Finally, the sequence $(d_{k})=1,{\frac {1}{2}},{\frac {1}{3}},{\frac {1}{4}},{\frac {1}{5}},{\frac {1}{6}},\ldots ,{\frac {1}{k+1}},\ldots$ converges to zero Q-sublinearly and logarithmically and its convergence is shown as the fourth plot of the figure below.

### Convergence rates to fixed points of recurrent sequences

Recurrent sequences ${\textstyle x_{k+1}:=f(x_{k})}$ , called fixed point iterations, define discrete time autonomous dynamical systems and have important general applications in mathematics through various fixed-point theorems about their convergence behavior. When *f* is continuously differentiable, given a fixed point *p*, ${\textstyle f(p)=p,}$ such that ${\textstyle |f'(p)|<1}$ , the fixed point is an attractive fixed point and the recurrent sequence will converge at least linearly to *p* for any starting value $x_{0}$ sufficiently close to *p*. If $|f'(p)|=0$ and ${\textstyle |f''(p)|<1}$ , then the recurrent sequence will converge at least quadratically, and so on. If $|f'(p)|>1$ , then the fixed point is a repulsive fixed point and sequences cannot converge to *p* from its immediate neighborhoods, though they may still jump to *p* directly from outside of its local neighborhoods.

### Order estimation

A practical method to calculate the order of convergence for a sequence generated by a fixed point iteration is to calculate the following sequence, which converges to the order q : $q\approx {\frac {\log \left|\displaystyle {\frac {x_{k+1}-x_{k}}{x_{k}-x_{k-1}}}\right|}{\log \left|\displaystyle {\frac {x_{k}-x_{k-1}}{x_{k-1}-x_{k-2}}}\right|}}.$

For numerical approximation of an exact value through a numerical method of order q see.

### Accelerating convergence rates

Many methods exist to accelerate the convergence of a given sequence, i.e., to transform one sequence into a second sequence that converges more quickly to the same limit. Such techniques are in general known as "series acceleration" methods. These may reduce the computational costs of approximating the limits of the original sequences. One example of series acceleration by sequence transformation is Aitken's delta-squared process. These methods in general, and in particular Aitken's method, do not typically increase the order of convergence and thus they are useful only if initially the convergence is not faster than linear: if $(x_{k})$ converges linearly, Aitken's method transforms it into a sequence $(a_{k})$ that still converges linearly (except for pathologically designed special cases), but faster in the sense that ${\textstyle \lim _{k\rightarrow \infty }(a_{k}-L)/(x_{k}-L)=0}$ . On the other hand, if the convergence is already of order ≥ 2, Aitken's method will bring no improvement.

## Asymptotic rates of convergence for discretization methods

### Definitions

A sequence of discretized approximations $(y_{k})$ of some continuous-domain function S that converges to this target, together with a corresponding sequence of discretization scale parameters $(h_{k})$ that converge to 0, is said to have asymptotic *order of convergence* q and asymptotic *rate of convergence* $\mu$ if

$\lim _{k\rightarrow \infty }{\frac {\left|y_{k}-S\right|}{h_{k}^{q}}}=\mu ,$

for some positive constants $\mu$ and q and using $|x|$ to stand for an appropriate distance metric on the space of solutions, most often either the uniform norm, the absolute difference, or the Euclidean distance. Discretization scale parameters may be spacings of a regular grid in space or in time, the inverse of the number of points of a grid in one dimension, an average or maximum distance between points in a polygon mesh, the single-dimension spacings of an irregular sparse grid, or a characteristic quantum of energy or momentum in a quantum mechanical basis set.

When all the discretizations are generated using a single common method, it is common to discuss the asymptotic rate and order of convergence for the method itself rather than any particular discrete sequences of discretized solutions. In these cases one considers a single abstract discretized solution $y_{h}$ generated using the method with a scale parameter h and then the method is said to have asymptotic *order of convergence* q and asymptotic *rate of convergence* $\mu$ if

$\lim _{h\rightarrow 0}{\frac {\left|y_{h}-S\right|}{h^{q}}}=\mu ,$

again for some positive constants $\mu$ and q and an appropriate metric $|x|.$ This implies that the error of a discretization asymptotically scales like the discretization's scale parameter to the q power, or ${\textstyle \left|y_{h}-S\right|=O(h^{q})}$ using asymptotic big O notation. More precisely, it implies the leading order error is $\mu h^{q},$ which can be expressed using asymptotic small o notation as ${\textstyle \left|y_{h}-S\right|=\mu h^{q}+o(h^{q}).}$

In some cases multiple rates and orders for the same method but with different choices of scale parameter may be important, for instance for finite difference methods based on multidimensional grids where the different dimensions have different grid spacings or for finite element methods based on polygon meshes where choosing either average distance between mesh points or maximum distance between mesh points as scale parameters may imply different orders of convergence. In some especially technical contexts, discretization methods' asymptotic rates and orders of convergence will be characterized by several scale parameters at once with the value of each scale parameter possibly affecting the asymptotic rate and order of convergence of the method with respect to the other scale parameters.

### Example

Consider the ordinary differential equation

${\frac {dy}{dx}}=-\kappa y$

with initial condition $y(0)=y_{0}$ . We can approximate a solution to this one-dimensional equation using a sequence $(y_{n})$ applying the forward Euler method for numerical discretization using any regular grid spacing h and grid points indexed by n as follows:

${\frac {y_{n+1}-y_{n}}{h}}=-\kappa y_{n},$

which implies the first-order linear recurrence with constant coefficients

$y_{n+1}=y_{n}(1-h\kappa ).$

Given $y(0)=y_{0}$ , the sequence satisfying that recurrence is the geometric progression

$y_{n}=y_{0}(1-h\kappa )^{n}=y_{0}\left(1-nh\kappa +{\frac {n(n-1)}{2}}h^{2}\kappa ^{2}+....\right).$

The exact analytical solution to the differential equation is $y=f(x)=y_{0}\exp(-\kappa x)$ , corresponding to the following Taylor expansion in $nh\kappa$ : $f(x_{n})=f(nh)=y_{0}\exp(-\kappa nh)=y_{0}\left(1-nh\kappa +{\frac {n^{2}h^{2}\kappa ^{2}}{2}}+...\right).$

Therefore the error of the discrete approximation at each discrete point is

$|y_{n}-f(x_{n})|={\frac {nh^{2}\kappa ^{2}}{2}}+\ldots$

For any specific $x=p$ , given a sequence of forward Euler approximations $((y_{n})_{k})$ , each using grid spacings $h_{k}$ that divide p so that $n_{p,k}=p/h_{k}$ , one has

$\lim _{h_{k}\rightarrow 0}{\frac {|y_{k}(p)-f(p)|}{h_{k}}}=\lim _{h_{k}\rightarrow 0}{\frac {|y_{k,n_{p,k}}-f(h_{k}n_{p,k})|}{h_{k}}}={\frac {h_{k}n_{p,k}\kappa ^{2}}{2}}={\frac {p\kappa ^{2}}{2}}$

for any sequence of grids with successively smaller grid spacings $h_{k}$ . Thus $((y_{n})_{k})$ converges to $f(x)$ pointwise with a convergence order $q=1$ and asymptotic error constant $p\kappa ^{2}/2$ at each point $p>0.$ Similarly, the sequence converges uniformly with the same order and with rate $L\kappa ^{2}/2$ on any bounded interval of $p\leq L$ , but it does not converge uniformly on the unbounded set of all positive real values, $[0,\infty ).$

## Comparing asymptotic rates of convergence

### Definitions

In asymptotic analysis in general, one sequence $(a_{k})_{k\in \mathbb {N} }$ that converges to a limit L is said to asymptotically converge to L with a faster order of convergence than another sequence $(b_{k})_{k\in \mathbb {N} }$ that converges to L in a shared metric space with distance metric $|\cdot |,$ such as the real numbers or complex numbers with the ordinary absolute difference metrics, if

$\lim _{k\rightarrow \infty }{\frac {\left|a_{k}-L\right|}{|b_{k}-L|}}=0,$

the two are said to asymptotically converge to L with the same order of convergence if

$\lim _{k\rightarrow \infty }{\frac {\left|a_{k}-L\right|}{|b_{k}-L|}}=\mu$

for some positive finite constant $\mu ,$ and the two are said to asymptotically converge to L with the same rate and order of convergence if

$\lim _{k\rightarrow \infty }{\frac {\left|a_{k}-L\right|}{|b_{k}-L|}}=1.$

These comparative definitions of rate and order of asymptotic convergence are fundamental in asymptotic analysis. For the first two of these there are associated expressions in asymptotic O notation: the first is that $a_{k}-L=o(b_{k}-L)$ in small o notation and the second is that $a_{k}-L=\Theta (b_{k}-L)$ in Knuth notation. The third is also called asymptotic equivalence, expressed $a_{k}-L\sim b_{k}-L.$

### Examples

For any two geometric progressions $(ar^{k})_{k\in \mathbb {N} }$ and $(bs^{k})_{k\in \mathbb {N} },$ with shared limit zero, the two sequences are asymptotically equivalent if and only if both $a=b$ and $r=s.$ They converge with the same order if and only if $r=s.$ $(ar^{k})$ converges with a faster order than $(bs^{k})$ if and only if $r<s.$ The convergence of any geometric series to its limit has error terms that are equal to a geometric progression, so similar relationships hold among geometric series as well. Any sequence that is asymptotically equivalent to a convergent geometric sequence may be either be said to "converge geometrically" or "converge exponentially" with respect to the absolute difference from its limit, or it may be said to "converge linearly" relative to a logarithm of the absolute difference such as the "number of decimals of precision." The latter is standard in numerical analysis.

For any two sequences of elements proportional to an inverse power of $k,$ $(ak^{-n})_{k\in \mathbb {N} }$ and $(bk^{-m})_{k\in \mathbb {N} },$ with shared limit zero, the two sequences are asymptotically equivalent if and only if both $a=b$ and $n=m.$ They converge with the same order if and only if $n=m.$ $(ak^{-n})$ converges with a faster order than $(bk^{-m})$ if and only if $n>m.$

For any sequence $(a_{k})_{k\in \mathbb {N} }$ with a limit of zero, its convergence can be compared to the convergence of the shifted sequence $(a_{k-1})_{k\in \mathbb {N} },$ rescalings of the shifted sequence by a constant $\mu ,$ $(\mu a_{k-1})_{k\in \mathbb {N} },$ and scaled q -powers of the shifted sequence, $(\mu a_{k-1}^{q})_{k\in \mathbb {N} }.$ These comparisons are the basis for the Q-convergence classifications for iterative numerical methods as described above: when a sequence of iterate errors from a numerical method $(|x_{k}-L|)_{k\in \mathbb {N} }$ is asymptotically equivalent to the shifted, exponentiated, and rescaled sequence of iterate errors $(\mu |x_{k-1}-L|^{q})_{k\in \mathbb {N} },$ it is said to converge with order q and rate $\mu .$

## Non-asymptotic rates of convergence

Non-asymptotic rates of convergence do not have the common, standard definitions that asymptotic rates of convergence have. Among formal techniques, Lyapunov theory is one of the most powerful and widely applied frameworks for characterizing and analyzing non-asymptotic convergence behavior.

For iterative methods, one common practical approach is to discuss these rates in terms of the number of iterates or the computer time required to reach close neighborhoods of a limit from starting points far from the limit. The non-asymptotic rate is then an inverse of that number of iterates or computer time. In practical applications, an iterative method that required fewer steps or less computer time than another to reach target accuracy will be said to have converged faster than the other, even if its asymptotic convergence is slower. These rates will generally be different for different starting points and different error thresholds for defining the neighborhoods. It is most common to discuss summaries of statistical distributions of these single point rates corresponding to distributions of possible starting points, such as the "average non-asymptotic rate," the "median non-asymptotic rate," or the "worst-case non-asymptotic rate" for some method applied to some problem with some fixed error threshold. These ensembles of starting points can be chosen according to parameters like initial distance from the eventual limit in order to define quantities like "average non-asymptotic rate of convergence from a given distance."

For discretized approximation methods, similar approaches can be used with a discretization scale parameter such as an inverse of a number of grid or mesh points or a Fourier series cutoff frequency playing the role of inverse iterate number, though it is not especially common. For any problem, there is a greatest discretization scale parameter compatible with a desired accuracy of approximation, and it may not be as small as required for the asymptotic rate and order of convergence to provide accurate estimates of the error. In practical applications, when one discretization method gives a desired accuracy with a larger discretization scale parameter than another it will often be said to converge faster than the other, even if its eventual asymptotic convergence is slower.
