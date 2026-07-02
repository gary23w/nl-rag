---
title: "Newton's method (part 1/2)"
source: https://en.wikipedia.org/wiki/Newton's_method
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
part: 1/2
---

# Newton's method

In numerical analysis, the **Newton–Raphson method**, also known simply as **Newton's method**, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a real-valued function f, its derivative f′, and an initial guess *x*0 for a root of f. If f satisfies certain assumptions and the initial guess is close, then

x 1 = x 0 − f ( x 0 ) f ′ ( x 0 ) {\displaystyle x_{1}=x_{0}-{\frac {f(x_{0})}{f'(x_{0})}}} ({\displaystyle x_{1}=x_{0}-{\frac {f(x_{0})}{f'(x_{0})}}})

is a better approximation of the root than *x*0. Geometrically, (*x*1, 0) is the x-intercept of the tangent to the graph of f at (*x*0, *f*(*x*0)): that is, the improved guess, *x*1, is the unique root of the linear approximation of f at the initial guess, *x*0. The process is repeated as

x n + 1 = x n − f ( x n ) f ′ ( x n ) {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}} ({\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}})

until a sufficiently precise value is reached. The number of correct digits roughly doubles with each step. This algorithm is first in the class of Householder's methods, and was succeeded by Halley's method. The method can also be extended to complex functions and to systems of equations.


## Description

The purpose of Newton's method is to find a root of a function. The idea is to start with an initial guess near a root, approximate the function by its tangent line near the guess, and then take the root of the linear approximation as a next guess at the function's root. This will typically be closer to the function's root than the previous guess, and the method can be iterated.

The best linear approximation to an arbitrary differentiable function f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) near the point x = x n {\displaystyle x=x_{n}} ({\displaystyle x=x_{n}}) is the tangent line to the curve, with equation

f ( x ) ≈ f ( x n ) + f ′ ( x n ) ( x − x n ) . {\displaystyle f(x)\approx f(x_{n})+f'(x_{n})(x-x_{n}).} ({\displaystyle f(x)\approx f(x_{n})+f'(x_{n})(x-x_{n}).})

The root of this linear function, the place where it intercepts the ⁠ x {\displaystyle x} ({\displaystyle x})⁠-axis, can be taken as a closer approximate root ⁠ x n + 1 {\displaystyle x_{n+1}} ({\displaystyle x_{n+1}})⁠ if f ′ ( x n ) ≠ 0 {\displaystyle f'(x_{n})\neq 0} ({\displaystyle f'(x_{n})\neq 0}):

x n + 1 = x n − f ( x n ) f ′ ( x n ) . {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}.} ({\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}.})

The process can be started with any arbitrary initial guess ⁠ x 0 {\displaystyle x_{0}} ({\displaystyle x_{0}})⁠, though it will generally require fewer iterations to converge if the guess is close to one of the function's roots. The method will usually converge if ⁠ f ′ ( x 0 ) ≠ 0 {\displaystyle f'(x_{0})\neq 0} ({\displaystyle f'(x_{0})\neq 0})⁠. Furthermore, for a root of multiplicity 1, the convergence is at least quadratic (see *Rate of convergence*) in some sufficiently small neighbourhood of the root: the number of correct digits of the approximation roughly doubles with each additional step. More details can be found in *§ Analysis* below.

Householder's methods are similar but have higher order for even faster convergence. However, the extra computations required for each step can slow down the overall performance relative to Newton's method, particularly if ⁠ f {\displaystyle f} ({\displaystyle f})⁠ or its derivatives are computationally expensive to evaluate.


## History

In the Old Babylonian period (19th–16th century BCE), the side of a square of known area could be effectively approximated, and this is conjectured to have been done using a special case of Newton's method, described algebraically below, by iteratively improving an initial estimate; an equivalent method can be found in Hero of Alexandria's *Metrica* (1st–2nd century CE), so is often called *Heron's method*. Jamshīd al-Kāshī used a method to solve *x**P* − *N* = 0 to find roots of *N*, a method that was algebraically equivalent to Newton's method, and in which a similar method was found in *Trigonometria Britannica*, published by Henry Briggs in 1633. His method first appeared in his 1427 publication *Miftāḥ al-Ḥisāb* (*The Key to Arithmetic*). Al-Kāshī's work was founded on the earlier contributions of the polymath al-Bīrūnī (973–1048) and the mathematician Sharaf al-Dīn al-Ṭūsī (1135–1213). The contributions of al-Kāshī remained largely unknown to the Western scientific community for centuries, until the work of François Viète (1540–1603). In 1600, Viète rediscovered a technique similar to al-Kāshī's in the context of solving scalar polynomial equations of degree six.

The method that laid the groundwork for what is now the modern Newton's method which would be developed by Joseph Raphson and Thomas Simpson first appeared in Isaac Newton's work in *De analysi per aequationes numero terminorum infinitas* (written in 1669, published in 1711 by William Jones) and in *De metodis fluxionum et serierum infinitarum* (written in 1671, translated and published as *Method of Fluxions* in 1736 by John Colson). However, while Newton gave the basic ideas, his method differs from the modern method given above. He applied the method only to polynomials, starting with an initial root estimate and extracting a sequence of error corrections. He used each correction to rewrite the polynomial in terms of the remaining error, and then solved for a new correction by neglecting higher-degree terms. He did not explicitly connect the method with derivatives or present a general formula. Newton applied this method to both numerical and algebraic problems, producing Taylor series in the latter case. Despite this, in the later second and third editions of Newton's 1687 *Philosophiæ Naturalis Principia Mathematica*, he did apply his method in an iterative manner to a nonpolynomial equation, specifically Kepler's equation, which were the first published uses of Newton's method in this form by him.

Newton may have derived his method from a similar, less precise method by mathematician Viète, however, the two methods are not the same. The essence of Viète's own method can be found in the work of the mathematician Sharaf al-Din al-Tusi.

The Japanese mathematician Seki Kōwa used a form of Newton's method in the 1680s to solve single-variable equations, though the connection with calculus was missing.

Newton's method was first published in 1685 in *A Treatise of Algebra both Historical and Practical* by John Wallis. In 1690, Raphson published a simplified description in *Analysis aequationum universalis*. Raphson also applied the method only to polynomials, but he avoided Newton's tedious rewriting process by extracting each successive correction from the original polynomial. This allowed him to derive a reusable iterative expression for each problem. Finally, in 1740, Simpson described Newton's method as an iterative method for solving general nonlinear equations using calculus, essentially giving the description above. In the same publication, Simpson also gives the generalization to systems of two equations and notes that Newton's method can be used for solving optimization problems by setting the gradient to zero.

Arthur Cayley in 1879 in *The Newton–Fourier imaginary problem* was the first to notice the difficulties in generalizing Newton's method to complex roots of polynomials with degree greater than 2 and complex initial values. This opened the way to the study of the theory of iterations of rational functions.


## Practical considerations

Newton's method is a powerful technique—if the derivative of the function at the root is nonzero, then the convergence is at least quadratic: as the method converges on the root, the difference between the root and the approximation is squared (the number of accurate digits roughly doubles) at each step. However, there are some difficulties with the method.

### Difficulty in calculating the derivative of a function

Newton's method requires that the derivative can be calculated directly. An analytical expression for the derivative may not be easily obtainable or could be expensive to evaluate. In these situations, it may be appropriate to approximate the derivative by using the slope of a line through two nearby points on the function. Using this approximation would result in something like the secant method whose convergence is slower than that of Newton's method.

### Failure of the method to converge to the root

It is important to review the proof of quadratic convergence of Newton's method before implementing it. Specifically, one should review the assumptions made in the proof. For situations where the method fails to converge, it is because the assumptions made in this proof are not met.

For example, in some cases, if the first derivative is not well behaved in the neighborhood of a particular root, then it is possible that Newton's method will fail to converge no matter where the initialization is set. In some cases, Newton's method can be stabilized by using successive over-relaxation, or the speed of convergence can be increased by using the same method.

In a robust implementation of Newton's method, it is common to place limits on the number of iterations, bound the solution to an interval known to contain the root, and combine the method with a more robust root finding method.

### Slow convergence for roots of multiplicity greater than 1

If the root being sought has multiplicity greater than one, the convergence rate is merely linear (errors reduced by a constant factor at each step) unless special steps are taken. When there are two or more roots that are close together then it may take many iterations before the iterates get close enough to one of them for the quadratic convergence to be apparent. However, if the multiplicity m of the root is known, the following modified algorithm preserves the quadratic convergence rate:

x n + 1 = x n − m f ( x n ) f ′ ( x n ) . {\displaystyle x_{n+1}=x_{n}-m{\frac {f(x_{n})}{f'(x_{n})}}.} ({\displaystyle x_{n+1}=x_{n}-m{\frac {f(x_{n})}{f'(x_{n})}}.})

This is equivalent to using successive over-relaxation. On the other hand, if the multiplicity m of the root is not known, it is possible to estimate m after carrying out one or two iterations, and then use that value to increase the rate of convergence.

If the multiplicity m of the root is finite then *g*(*x*) = ⁠*f*(*x*)/*f′*(*x*)⁠ will have a root at the same location with multiplicity 1. Applying Newton's method to find the root of *g*(*x*) recovers quadratic convergence in many cases although it generally involves the second derivative of *f*(*x*). In a particularly simple case, if *f*(*x*) = *x**m* then *g*(*x*) = ⁠*x*/*m*⁠ and Newton's method finds the root in a single iteration with

x n + 1 = x n − g ( x n ) g ′ ( x n ) = x n − x n m 1 m = 0 . {\displaystyle x_{n+1}=x_{n}-{\frac {g(x_{n})}{g'(x_{n})}}=x_{n}-{\frac {\;{\frac {x_{n}}{m}}\;}{\frac {1}{m}}}=0\,.} ({\displaystyle x_{n+1}=x_{n}-{\frac {g(x_{n})}{g'(x_{n})}}=x_{n}-{\frac {\;{\frac {x_{n}}{m}}\;}{\frac {1}{m}}}=0\,.})

### Slow convergence

The function *f*(*x*) = *x*2 has a root at 0. Since f is continuously differentiable at its root, the theory guarantees that Newton's method as initialized sufficiently close to the root will converge. However, since the derivative *f* ′ is zero at the root, quadratic convergence is not ensured by the theory. In this particular example, the Newton iteration is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

1

2

x

n

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}={\frac {1}{2}}x_{n}.}

It is visible from this that Newton's method could be initialized anywhere and converge to zero, but at only a linear rate. If initialized at 1, dozens of iterations would be required before ten digits of accuracy are achieved.

The function *f*(*x*) = *x* + *x*4/3 also has a root at 0, where it is continuously differentiable. Although the first derivative *f* ′ is nonzero at the root, the second derivative *f* ′′ is nonexistent there, so that quadratic convergence cannot be guaranteed. In fact the Newton iteration is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

4

/

3

3

+

4

x

n

1

/

3

≈

x

n

⋅

x

n

1

/

3

3

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}={\frac {x_{n}^{4/3}}{3+4x_{n}^{1/3}}}\approx x_{n}\cdot {\frac {x_{n}^{1/3}}{3}}.}

From this, it can be seen that the rate of convergence is superlinear but subquadratic. This can be seen in the following tables, the left of which shows Newton's method applied to the above *f*(*x*) = *x* + *x*4/3 and the right of which shows Newton's method applied to *f*(*x*) = *x* + *x*2. The quadratic convergence in iteration shown on the right is illustrated by the orders of magnitude in the distance from the iterate to the true root (0,1,2,3,5,10,20,39,...) being approximately doubled from row to row. While the convergence on the left is superlinear, the order of magnitude is only multiplied by about 4/3 from row to row (0,1,2,4,5,7,10,13,...).

| *x**n* | *x* + *x*4/3 *n* |   | *x**n* | *x* + *x*2 *n* |
|---|---|---|---|---|
| 1 | 2 | 1 | 2 |   |
| 1.4286 × 10−1 | 2.1754 × 10−1 | 3.3333 × 10−1 | 4.4444 × 10−1 |   |
| 1.4669 × 10−2 | 1.8260 × 10−2 | 6.6666 × 10−2 | 7.1111 × 10−2 |   |
| 9.0241 × 10−4 | 9.8961 × 10−4 | 3.9216 × 10−3 | 3.9369 × 10−3 |   |
| 2.5750 × 10−5 | 2.6511 × 10−5 | 1.5259 × 10−5 | 1.5259 × 10−5 |   |
| 2.4386 × 10−7 | 2.4539 × 10−7 | 2.3283 × 10−10 | 2.3283 × 10−10 |   |
| 5.0366 × 10−10 | 5.0406 × 10−10 | 5.4210 × 10−20 | 5.4210 × 10−20 |   |
| 1.3344 × 10−13 | 1.3344 × 10−13 | 2.9387 × 10−39 | 2.9387 × 10−39 |   |

The rate of convergence is distinguished from the number of iterations required to reach a given accuracy. For example, the function *f*(*x*) = *x*20 − 1 has a root at 1. Since *f* ′(1) ≠ 0 and f is smooth, it is known that any Newton iteration convergent to 1 will converge quadratically. However, if initialized at 0.5, the first few iterates of Newton's method are approximately 26214, 24904, 23658, 22476, decreasing slowly, with only the 200th iterate being 1.0371. The following iterates are 1.0103, 1.00093, 1.0000082, and 1.00000000065, illustrating quadratic convergence. This highlights that quadratic convergence of a Newton iteration does not mean that only few iterates are required; this only applies once the sequence of iterates is sufficiently close to the root.

### Convergence dependent on initialization

The function *f*(*x*) = *x*(1 + *x*2)−1/2 has a root at 0. The Newton iteration is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

−

x

n

(

1

+

x

n

2

)

−

1

/

2

(

1

+

x

n

2

)

−

3

/

2

=

−

x

n

3

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}(1+x_{n}^{2})^{-1/2}}{(1+x_{n}^{2})^{-3/2}}}=-x_{n}^{3}.}

From this, it can be seen that there are three possible phenomena for a Newton iteration. If initialized strictly between ±1, the Newton iteration will converge (super-)quadratically to 0; if initialized exactly at 1 or −1, the Newton iteration will oscillate endlessly between ±1; if initialized anywhere else, the Newton iteration will diverge. This same trichotomy occurs for *f*(*x*) = arctan *x*.

In cases where the function in question has multiple roots, it can be difficult to control, via choice of initialization, which root (if any) is identified by Newton's method. For example, the function *f*(*x*) = *x*(*x*2 − 1)(*x* − 3)e−(*x* − 1)2/2 has roots at −1, 0, 1, and 3. If initialized at −1.488, the Newton iteration converges to 0; if initialized at −1.487, it diverges to ∞; if initialized at −1.486, it converges to −1; if initialized at −1.485, it diverges to −∞; if initialized at −1.4843, it converges to 3; if initialized at −1.484, it converges to 1. This kind of subtle dependence on initialization is not uncommon; it is frequently studied in the complex plane in the form of the Newton fractal.

### Divergence even when initialization is close to the root

Consider the problem of finding a root of *f*(*x*) = *x*1/3. The Newton iteration is

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

−

x

n

1

/

3

1

3

x

n

−

2

/

3

=

−

2

x

n

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}^{1/3}}{{\frac {1}{3}}x_{n}^{-2/3}}}=-2x_{n}.}

Unless Newton's method is initialized at the exact root 0, it is seen that the sequence of iterates will fail to converge. For example, even if initialized at the reasonably accurate guess of 0.001, the first several iterates are −0.002, 0.004, −0.008, 0.016, reaching 1048.58, −2097.15, ... by the 20th iterate. This failure of convergence is not contradicted by the analytic theory, since in this case f is not differentiable at its root.

In the above example, failure of convergence is reflected by the failure of *f*(*x**n*) to get closer to zero as n increases, as well as by the fact that successive iterates are growing further and further apart. However, the function *f*(*x*) = *x*1/3e−*x*2 also has a root at 0. The Newton iteration is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

(

1

−

3

1

−

6

x

n

2

)

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}\left(1-{\frac {3}{1-6x_{n}^{2}}}\right).}

In this example, where again f is not differentiable at the root, any Newton iteration not starting exactly at the root will diverge, but with both *x**n* + 1 − *x**n* and *f*(*x**n*) converging to zero. This is seen in the following table showing the iterates with initialization 1:

| *x**n* | *f*(*x**n*) |
|---|---|
| 1 | 0.36788 |
| 1.6 | 9.0416 × 10−2 |
| 1.9342 | 2.9556 × 10−2 |
| 2.2048 | 1.0076 × 10−2 |
| 2.4396 | 3.5015 × 10−3 |
| 2.6505 | 1.2307 × 10−3 |
| 2.8437 | 4.3578 × 10−4 |
| 3.0232 | 1.5513 × 10−4 |

Although the convergence of *x**n* + 1 − *x**n* in this case is not very rapid, it can be proved from the iteration formula. This example highlights the possibility that a stopping criterion for Newton's method based only on the smallness of *x**n* + 1 − *x**n* and *f*(*x**n*) might falsely identify a root.

### Oscillatory behavior

It is easy to find situations for which Newton's method oscillates endlessly between two distinct values. For example, for Newton's method as applied to a function f to oscillate between 0 and 1, it is only necessary that the tangent line to f at 0 intersects the x-axis at 1 and that the tangent line to f at 1 intersects the x-axis at 0. This is the case, for example, if *f*(*x*) = *x*3 − 2*x* + 2. For this function, it is even the case that Newton's iteration as initialized sufficiently close to 0 or 1 will *asymptotically* oscillate between these values. For example, Newton's method as initialized at 0.99 yields iterates 0.99, −0.06317, 1.00628, 0.03651, 1.00196, 0.01162, 1.00020, 0.00120, 1.000002, and so on. This behavior is present despite the presence of a root of f approximately equal to −1.76929.

### Undefinedness of Newton's method

In some cases, it is not even possible to perform the Newton iteration. For example, if *f*(*x*) = *x*2 − 1, then the Newton iteration is defined by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

−

x

n

2

−

1

2

x

n

=

x

n

2

+

1

2

x

n

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}^{2}-1}{2x_{n}}}={\frac {x_{n}^{2}+1}{2x_{n}}}.}

So Newton's method cannot be initialized at 0, since this would make *x*1 undefined. Geometrically, this is because the tangent line to f at 0 is horizontal (i.e. *f* ′(0) = 0), never intersecting the *x*-axis.

Even if the initialization is selected so that the Newton iteration can begin, the same phenomenon can block the iteration from being indefinitely continued.

If f has an incomplete domain, it is possible for Newton's method to send the iterates outside of the domain, so that it is impossible to continue the iteration. For example, the natural logarithm function *f*(*x*) = ln *x* has a root at 1, and is defined only for positive x. Newton's iteration in this case is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

(

1

−

ln

⁡

x

n

)

.

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}(1-\ln x_{n}).}

So if the iteration is initialized at e, the next iterate is 0; if the iteration is initialized at a value larger than e, then the next iterate is negative. In either case, the method cannot be continued.


## Analysis

Suppose that the function f has a zero at α, i.e., *f*(*α*) = 0, and f is differentiable in a neighborhood of α.

If f is continuously differentiable and its derivative is nonzero at α, then there exists a neighborhood of α such that for all starting values *x*0 in that neighborhood, the sequence (*x**n*) will converge to α.

If f is continuously differentiable, its derivative is nonzero at α, *and* it has a second derivative at α, then the convergence is quadratic or faster. If the second derivative is not 0 at α then the convergence is merely quadratic. If the third derivative exists and is bounded in a neighborhood of α, then:

Δ x i + 1 = f ″ ( α ) 2 f ′ ( α ) ( Δ x i ) 2 + O ( Δ x i ) 3 , {\displaystyle \Delta x_{i+1}={\frac {f''(\alpha )}{2f'(\alpha )}}\left(\Delta x_{i}\right)^{2}+O\left(\Delta x_{i}\right)^{3}\,,} ({\displaystyle \Delta x_{i+1}={\frac {f''(\alpha )}{2f'(\alpha )}}\left(\Delta x_{i}\right)^{2}+O\left(\Delta x_{i}\right)^{3}\,,})

where

Δ x i ≜ x i − α . {\displaystyle \Delta x_{i}\triangleq x_{i}-\alpha \,.} ({\displaystyle \Delta x_{i}\triangleq x_{i}-\alpha \,.})

If the derivative is 0 at α, then the convergence is usually only linear. Specifically, if f is twice continuously differentiable, *f′*(*α*) = 0 and *f″*(*α*) ≠ 0, then there exists a neighborhood of α such that, for all starting values *x*0 in that neighborhood, the sequence of iterates converges linearly, with rate ⁠1/2⁠. Alternatively, if *f′*(*α*) = 0 and *f′*(*x*) ≠ 0 for *x* ≠ *α*, x in a neighborhood U of α, α being a zero of multiplicity r, and if *f* ∈ *C**r*(*U*), then there exists a neighborhood of α such that, for all starting values *x*0 in that neighborhood, the sequence of iterates converges linearly.

However, even linear convergence is not guaranteed in pathological situations.

In practice, these results are local, and the neighborhood of convergence is not known in advance. But there are also some results on global convergence: for instance, given a right neighborhood *U*+ of α, if f is twice differentiable in *U*+ and if *f′* ≠ 0, *f* · *f″* > 0 in *U*+, then, for each *x*0 in *U*+ the sequence *x**k* is monotonically decreasing to α.

### Proof of quadratic convergence for Newton's iterative method

According to Taylor's theorem, any function *f*(*x*) which has a continuous second derivative can be represented by an expansion about a point that is close to a root of *f*(*x*). Suppose this root is α. Then the expansion of *f*(*α*) about *x**n* is:

| f ( α ) = f ( x n ) + f ′ ( x n ) ( α − x n ) + R 1 {\displaystyle f(\alpha )=f(x_{n})+f'(x_{n})(\alpha -x_{n})+R_{1}\,} ({\displaystyle f(\alpha )=f(x_{n})+f'(x_{n})(\alpha -x_{n})+R_{1}\,}) |   | 1 |
|---|---|---|

where the Lagrange form of the Taylor series expansion remainder is

R 1 = 1 2 ! f ″ ( ξ n ) ( α − x n ) 2 , {\displaystyle R_{1}={\frac {1}{2!}}f''(\xi _{n})\left(\alpha -x_{n}\right)^{2}\,,} ({\displaystyle R_{1}={\frac {1}{2!}}f''(\xi _{n})\left(\alpha -x_{n}\right)^{2}\,,})

where *ξ**n* is in between *x**n* and α.

Since α is the root, (**1**) becomes:

| 0 = f ( α ) = f ( x n ) + f ′ ( x n ) ( α − x n ) + 1 2 f ″ ( ξ n ) ( α − x n ) 2 {\displaystyle 0=f(\alpha )=f(x_{n})+f'(x_{n})(\alpha -x_{n})+{\tfrac {1}{2}}f''(\xi _{n})\left(\alpha -x_{n}\right)^{2}\,} ({\displaystyle 0=f(\alpha )=f(x_{n})+f'(x_{n})(\alpha -x_{n})+{\tfrac {1}{2}}f''(\xi _{n})\left(\alpha -x_{n}\right)^{2}\,}) |   | 2 |
|---|---|---|

Dividing equation (**2**) by *f′*(*x**n*) and rearranging gives

| f ( x n ) f ′ ( x n ) + ( α − x n ) = − f ″ ( ξ n ) 2 f ′ ( x n ) ( α − x n ) 2 {\displaystyle {\frac {f(x_{n})}{f'(x_{n})}}+\left(\alpha -x_{n}\right)={\frac {-f''(\xi _{n})}{2f'(x_{n})}}\left(\alpha -x_{n}\right)^{2}} ({\displaystyle {\frac {f(x_{n})}{f'(x_{n})}}+\left(\alpha -x_{n}\right)={\frac {-f''(\xi _{n})}{2f'(x_{n})}}\left(\alpha -x_{n}\right)^{2}}) |   | 3 |
|---|---|---|

Remembering that *x**n* + 1 is defined by

| x n + 1 = x n − f ( x n ) f ′ ( x n ) , {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}\,,} ({\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}\,,}) |   | 4 |
|---|---|---|

one finds that

α − x n + 1 ⏟ ε n + 1 = − f ″ ( ξ n ) 2 f ′ ( x n ) ( α − x n ⏟ ε n ) 2 . {\displaystyle \underbrace {\alpha -x_{n+1}} _{\varepsilon _{n+1}}={\frac {-f''(\xi _{n})}{2f'(x_{n})}}{(\,\underbrace {\alpha -x_{n}} _{\varepsilon _{n}}\,)}^{2}\,.} ({\displaystyle \underbrace {\alpha -x_{n+1}} _{\varepsilon _{n+1}}={\frac {-f''(\xi _{n})}{2f'(x_{n})}}{(\,\underbrace {\alpha -x_{n}} _{\varepsilon _{n}}\,)}^{2}\,.})

That is,

| ε n + 1 = − f ″ ( ξ n ) 2 f ′ ( x n ) ⋅ ε n 2 . {\displaystyle \varepsilon _{n+1}={\frac {-f''(\xi _{n})}{2f'(x_{n})}}\cdot \varepsilon _{n}^{2}\,.} ({\displaystyle \varepsilon _{n+1}={\frac {-f''(\xi _{n})}{2f'(x_{n})}}\cdot \varepsilon _{n}^{2}\,.}) |   | 5 |
|---|---|---|

Taking the absolute value of both sides gives

| \| ε n + 1 \| = \| f ″ ( ξ n ) \| 2 \| f ′ ( x n ) \| ⋅ ε n 2 . {\displaystyle \left\|{\varepsilon _{n+1}}\right\|={\frac {\left\|f''(\xi _{n})\right\|}{2\left\|f'(x_{n})\right\|}}\cdot \varepsilon _{n}^{2}\,.} ({\displaystyle \left\|{\varepsilon _{n+1}}\right\|={\frac {\left\|f''(\xi _{n})\right\|}{2\left\|f'(x_{n})\right\|}}\cdot \varepsilon _{n}^{2}\,.}) |   | 6 |
|---|---|---|

Equation (**6**) shows that the order of convergence is at least quadratic if the following conditions are satisfied:

1. *f′*(*x*) ≠ 0; for all *x* ∈ *I*, where I is the interval [*α* − |*ε*0|, *α* + |*ε*0|];
2. *f″*(*x*) is continuous, for all *x* ∈ *I*;
3. *M* |*ε*0| < 1

where M is given by

M = 1 2 ( sup x ∈ I | f ″ ( x ) | ) ( sup x ∈ I 1 | f ′ ( x ) | ) . {\displaystyle M={\frac {1}{2}}\left(\sup _{x\in I}\vert f''(x)\vert \right)\left(\sup _{x\in I}{\frac {1}{\vert f'(x)\vert }}\right).\,} ({\displaystyle M={\frac {1}{2}}\left(\sup _{x\in I}\vert f''(x)\vert \right)\left(\sup _{x\in I}{\frac {1}{\vert f'(x)\vert }}\right).\,})

If these conditions hold,

| ε n + 1 | ≤ M ⋅ ε n 2 . {\displaystyle \vert \varepsilon _{n+1}\vert \leq M\cdot \varepsilon _{n}^{2}\,.} ({\displaystyle \vert \varepsilon _{n+1}\vert \leq M\cdot \varepsilon _{n}^{2}\,.})

### Fourier conditions

Suppose that *f*(*x*) is a concave function on an interval, which is strictly increasing. If it is negative at the left endpoint and positive at the right endpoint, the intermediate value theorem guarantees that there is a zero ζ of f somewhere in the interval. From geometrical principles, it can be seen that the Newton iteration *x**i* starting at the left endpoint is monotonically increasing and convergent, necessarily to ζ.

Joseph Fourier introduced a modification of Newton's method starting at the right endpoint:

y

i

+

1

=

y

i

−

f

(

y

i

)

f

′

(

x

i

)

.

{\displaystyle y_{i+1}=y_{i}-{\frac {f(y_{i})}{f'(x_{i})}}.}

This sequence is monotonically decreasing and convergent. By passing to the limit in this definition, it can be seen that the limit of *y**i* must also be the zero ζ.

So, in the case of a concave increasing function with a zero, initialization is largely irrelevant. Newton iteration starting anywhere left of the zero will converge, as will Fourier's modified Newton iteration starting anywhere right of the zero. The accuracy at any step of the iteration can be determined directly from the difference between the location of the iteration from the left and the location of the iteration from the right. If f is twice continuously differentiable, it can be proved using Taylor's theorem that

lim

i

→

∞

y

i

+

1

−

x

i

+

1

(

y

i

−

x

i

)

2

=

−

1

2

f

″

(

ζ

)

f

′

(

ζ

)

,

{\displaystyle \lim _{i\to \infty }{\frac {y_{i+1}-x_{i+1}}{(y_{i}-x_{i})^{2}}}=-{\frac {1}{2}}{\frac {f''(\zeta )}{f'(\zeta )}},}

showing that this difference in locations converges quadratically to zero.

All of the above can be extended to systems of equations in multiple variables, although in that context the relevant concepts of monotonicity and concavity are more subtle to formulate. In the case of single equations in a single variable, the above monotonic convergence of Newton's method can also be generalized to replace concavity by positivity or negativity conditions on an arbitrary higher-order derivative of f. However, in this generalization, Newton's iteration is modified so as to be based on Taylor polynomials rather than the tangent line. In the case of concavity, this modification coincides with the standard Newton method.

### Error for n>1 variables

If we seek the root of a single function f : R n → R {\displaystyle f:\mathbf {R} ^{n}\to \mathbf {R} } ({\displaystyle f:\mathbf {R} ^{n}\to \mathbf {R} }) then the error ϵ n = x n − α {\displaystyle \epsilon _{n}=x_{n}-\alpha } ({\displaystyle \epsilon _{n}=x_{n}-\alpha }) is a vector such that its components obey ϵ k ( n + 1 ) = 1 2 ( ϵ ( n ) ) T Q k ϵ ( n ) + O ( ‖ ϵ ( n ) ‖ 3 ) {\displaystyle \epsilon _{k}^{(n+1)}={\frac {1}{2}}(\epsilon ^{(n)})^{T}Q_{k}\epsilon ^{(n)}+O(\|\epsilon ^{(n)}\|^{3})} ({\displaystyle \epsilon _{k}^{(n+1)}={\frac {1}{2}}(\epsilon ^{(n)})^{T}Q_{k}\epsilon ^{(n)}+O(\|\epsilon ^{(n)}\|^{3})}) where Q k {\displaystyle Q_{k}} ({\displaystyle Q_{k}}) is a quadratic form: ( Q k ) i , j = ∑ ℓ ( ( D 2 f ) − 1 ) i , ℓ ∂ 3 f ∂ x j ∂ x k ∂ x ℓ {\displaystyle (Q_{k})_{i,j}=\sum _{\ell }((D^{2}f)^{-1})_{i,\ell }{\frac {\partial ^{3}f}{\partial x_{j}\partial x_{k}\partial x_{\ell }}}} ({\displaystyle (Q_{k})_{i,j}=\sum _{\ell }((D^{2}f)^{-1})_{i,\ell }{\frac {\partial ^{3}f}{\partial x_{j}\partial x_{k}\partial x_{\ell }}}}) evaluated at the root α {\displaystyle \alpha } ({\displaystyle \alpha }) (where D 2 f {\displaystyle D^{2}f} ({\displaystyle D^{2}f}) is the 2nd derivative Hessian matrix).


## Examples

### Use of Newton's method to compute square roots

Newton's method is one of many known methods of computing square roots. Given a positive number a, the problem of finding a number x such that *x*2 = *a* is equivalent to finding a root of the function *f*(*x*) = *x*2 − *a*. The Newton iteration defined by this function is given by

x

n

+

1

=

x

n

−

f

(

x

n

)

f

′

(

x

n

)

=

x

n

−

x

n

2

−

a

2

x

n

=

1

2

(

x

n

+

a

x

n

)

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}^{2}-a}{2x_{n}}}={\frac {1}{2}}\left(x_{n}+{\frac {a}{x_{n}}}\right)}

.

This happens to coincide with the "Babylonian" method of finding square roots, which consists of replacing an approximate root *x**n* by the arithmetic mean of *x**n* and *a*⁄*x**n*. By performing this iteration, it is possible to evaluate a square root to any desired accuracy by only using the basic arithmetic operations.

The following three tables show examples of the result of this computation for finding the square root of 612, with the iteration initialized at the values of 1, 10, and −20. Each row in a "*x**n*" column is obtained by applying the preceding formula to the entry above it, for instance

306.5

=

1

2

(

1

+

612

1

)

.

{\displaystyle 306.5={\frac {1}{2}}\left(1+{\frac {612}{1}}\right).}

| *x**n* | *f*(*x**n*) |   | *x**n* | *f*(*x**n*) |   | *x**n* | *f*(*x**n*) |
|---|---|---|---|---|---|---|---|
| 1 | −611 | 10 | −512 | −20 | −212 |   |   |
| 306.5 | 9.3330 × 104 | 35.6 | 655.36 | −25.3 | 28.09 |   |   |
| 154.2483686786 | 2.3180 × 104 | 26.3955056180 | 84.722 | −24.7448616601 | 0.30818 |   |   |
| 79.1079978644 | 5.6461 × 103 | 24.7906354925 | 2.5756 | −24.7386345374 | 3.8777 × 10−5 |   |   |
| 43.4221286822 | 1.2735 × 103 | 24.7386882941 | 2.6985 × 10−3 | −24.7386337537 | 6.1424 × 10−13 |   |   |
| 28.7581624288 | 215.03 | 24.7386337538 | 2.9746 × 10−9 |   |   |   |   |
| 25.0195385369 | 13.977 |   |   |   |   |   |   |
| 24.7402106712 | 7.8024 × 10−2 |   |   |   |   |   |   |
| 24.7386338040 | 2.4865 × 10−6 |   |   |   |   |   |   |
| 24.7386337537 | 2.5256 × 10−15 |   |   |   |   |   |   |

The correct digits are underlined. It is seen that with only a few iterations one can obtain a solution accurate to many decimal places. The first table shows that this is true even if the Newton iteration were initialized by the very inaccurate guess of 1.

When computing any nonzero square root, the first derivative of f must be nonzero at the root, and that f is a smooth function. So, even before any computation, it is known that any convergent Newton iteration has a quadratic rate of convergence. This is reflected in the above tables by the fact that once a Newton iterate gets close to the root, the number of correct digits approximately doubles with each iteration.

### Solution of cos(*x*) = *x*3 using Newton's method

Consider the problem of finding the positive number x with cos (*x*) = *x*3. We can rephrase that as finding the zero of *f*(*x*) = cos(*x*) − *x*3. We have *f′*(*x*) = −sin(*x*) − 3*x*2. Since cos(*x*) ≤ 1 for all x and *x*3 > 1 for *x* > 1, we know that our solution lies between 0 and 1.

A starting value of 0 will lead to an undefined result which illustrates the importance of using a starting point close to the solution. For example, with an initial guess *x*0 = 0.5, the sequence given by Newton's method is:

x 1 = x 0 − f ( x 0 ) f ′ ( x 0 ) = 0.5 − cos ⁡ 0.5 − 0.5 3 − sin ⁡ 0.5 − 3 × 0.5 2 = 1.112 141 637 097 … x 2 = x 1 − f ( x 1 ) f ′ ( x 1 ) = ⋮ = 0. _ 909 672 693 736 … x 3 = ⋮ = ⋮ = 0.86 _ 7 263 818 209 … x 4 = ⋮ = ⋮ = 0.865 47 _ 7 135 298 … x 5 = ⋮ = ⋮ = 0.865 474 033 1 _ 11 … x 6 = ⋮ = ⋮ = 0.865 474 033 102 _ … {\displaystyle {\begin{matrix}x_{1}&=&x_{0}-{\dfrac {f(x_{0})}{f'(x_{0})}}&=&0.5-{\dfrac {\cos 0.5-0.5^{3}}{-\sin 0.5-3\times 0.5^{2}}}&=&1.112\,141\,637\,097\dots \\x_{2}&=&x_{1}-{\dfrac {f(x_{1})}{f'(x_{1})}}&=&\vdots &=&{\underline {0.}}909\,672\,693\,736\dots \\x_{3}&=&\vdots &=&\vdots &=&{\underline {0.86}}7\,263\,818\,209\dots \\x_{4}&=&\vdots &=&\vdots &=&{\underline {0.865\,47}}7\,135\,298\dots \\x_{5}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,1}}11\dots \\x_{6}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,102}}\dots \end{matrix}}} ({\displaystyle {\begin{matrix}x_{1}&=&x_{0}-{\dfrac {f(x_{0})}{f'(x_{0})}}&=&0.5-{\dfrac {\cos 0.5-0.5^{3}}{-\sin 0.5-3\times 0.5^{2}}}&=&1.112\,141\,637\,097\dots \\x_{2}&=&x_{1}-{\dfrac {f(x_{1})}{f'(x_{1})}}&=&\vdots &=&{\underline {0.}}909\,672\,693\,736\dots \\x_{3}&=&\vdots &=&\vdots &=&{\underline {0.86}}7\,263\,818\,209\dots \\x_{4}&=&\vdots &=&\vdots &=&{\underline {0.865\,47}}7\,135\,298\dots \\x_{5}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,1}}11\dots \\x_{6}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,102}}\dots \end{matrix}}})

The correct digits are underlined in the above example. In particular, *x*6 is correct to 12 decimal places. We see that the number of correct digits after the decimal point increases from 2 (for *x*3) to 5 and 10, illustrating the quadratic convergence.
