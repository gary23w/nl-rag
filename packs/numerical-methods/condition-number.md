---
title: "Condition number"
source: https://en.wikipedia.org/wiki/Condition_number
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
---

# Condition number

In numerical analysis, the **condition number** of a function measures how much the output value of the function can change for a small change in the input argument. This is used to measure how sensitive a function is to changes or errors in the input, and how much error in the output results from an error in the input. Very frequently, one is solving the inverse problem: given $f(x)=y,$ one is solving for *x,* and thus the condition number of the (local) inverse must be used.

The condition number is derived from the theory of propagation of uncertainty, and is formally defined as the value of the asymptotic worst-case relative change in output for a relative change in input. The "function" is the solution of a problem and the "arguments" are the data in the problem. The condition number is frequently applied to questions in linear algebra, in which case the derivative is straightforward but the error could be in many different directions, and is thus computed from the geometry of the matrix. More generally, condition numbers can be defined for non-linear functions in several variables.

A problem with a low condition number is said to be ***well-conditioned***, while a problem with a high condition number is said to be ***ill-conditioned***. In non-mathematical terms, an ill-conditioned problem is one where, for a small change in the inputs (the independent variables) there is a large change in the answer or dependent variable. This means that the correct solution/answer to the equation becomes hard to find. The condition number is a property of the problem. Paired with the problem are any number of algorithms that can be used to solve the problem, that is, to calculate the solution. Some algorithms have a property called *backward stability*; in general, a backward stable algorithm can be expected to accurately solve well-conditioned problems. Numerical analysis textbooks give formulas for the condition numbers of problems and identify known backward stable algorithms.

As a rule of thumb, if the condition number $\kappa (A)=10^{k}$ , then up to k digits of accuracy may be lost on top of what would be lost to the numerical method due to loss of precision from arithmetic methods. However, the condition number does not give the exact value of the maximum inaccuracy that may occur in the algorithm. It generally just bounds it with an estimate (whose computed value depends on the choice of the norm to measure the inaccuracy).

## Matrices

For example, the condition number associated with the linear equation *Ax* = *b* gives a bound on how inaccurate the solution *x* will be after approximation. Note that this is before the effects of round-off error are taken into account; conditioning is a property of the matrix, not the algorithm or floating-point accuracy of the computer used to solve the corresponding system. In particular, one should think of the condition number as being (very roughly) the rate at which the solution *x* will change with respect to a change in *b*. Thus, if the condition number is large, even a small error in *b* may cause a large error in *x*. On the other hand, if the condition number is small, then the error in *x* will not be much bigger than the error in *b*.

The condition number is defined more precisely to be the maximum ratio of the relative error in *x* to the relative error in *b*.

Let *e* be the error in *b*. Assuming that *A* is a nonsingular matrix, the error in the solution *A*−1*b* is *A*−1*e*. The ratio of the relative error in the solution to the relative error in *b* is

${\frac {\left\|A^{-1}e\right\|}{\left\|A^{-1}b\right\|}}/{\frac {\|e\|}{\|b\|}}={\frac {\left\|A^{-1}e\right\|}{\|e\|}}{\frac {\|b\|}{\left\|A^{-1}b\right\|}}.$

The maximum value (for nonzero *b* and *e*) is then seen to be the product of the two operator norms as follows:

${\begin{aligned}\max _{e,b\neq 0}\left\{{\frac {\left\|A^{-1}e\right\|}{\|e\|}}{\frac {\|b\|}{\left\|A^{-1}b\right\|}}\right\}&=\max _{e\neq 0}\left\{{\frac {\left\|A^{-1}e\right\|}{\|e\|}}\right\}\,\max _{b\neq 0}\left\{{\frac {\|b\|}{\left\|A^{-1}b\right\|}}\right\}\\&=\max _{e\neq 0}\left\{{\frac {\left\|A^{-1}e\right\|}{\|e\|}}\right\}\,\max _{x\neq 0}\left\{{\frac {\|Ax\|}{\|x\|}}\right\}\\&=\left\|A^{-1}\right\|\,\|A\|.\end{aligned}}$

The same definition is used for any consistent norm, i.e. one that satisfies

$\kappa (A)=\left\|A^{-1}\right\|\,\left\|A\right\|\geq \left\|A^{-1}A\right\|=1.$

When the condition number is exactly one (which can only happen if *A* is a scalar multiple of a linear isometry), then a solution algorithm can find (in principle, meaning if the algorithm introduces no errors of its own) an approximation of the solution whose precision is no worse than that of the data.

However, it does not mean that the algorithm will converge rapidly to this solution, just that it will not diverge arbitrarily because of inaccuracy on the source data (backward error), provided that the forward error introduced by the algorithm does not diverge as well because of accumulating intermediate rounding errors.

The condition number may also be infinite, but this implies that the problem is ill-posed (does not possess a unique, well-defined solution for each choice of data; that is, the matrix is not invertible), and no algorithm can be expected to reliably find a solution.

The definition of the condition number depends on the choice of norm, as can be illustrated by two examples.

If $\|\cdot \|$ is the matrix norm induced by the (vector) Euclidean norm (sometimes known as the *L*2 norm and typically denoted as $\|\cdot \|_{2}$ ), then

$\kappa (A)={\frac {\sigma _{\text{max}}(A)}{\sigma _{\text{min}}(A)}},$

where $\sigma _{\text{max}}(A)$ and $\sigma _{\text{min}}(A)$ are maximal and minimal singular values of A respectively. Hence:

- If A is normal, then $\kappa (A)={\frac {\max\{\left|\lambda (A)\right|\}}{\min\{\left|\lambda (A)\right|\}}},$ where $\lambda _{\text{max}}(A)$ and $\lambda _{\text{min}}(A)$ are maximal and minimal (by moduli) eigenvalues of A respectively.
- If A is unitary, then $\kappa (A)=1.$

The condition number with respect to *L*2 arises so often in numerical linear algebra that it is given a name, the **condition number of a matrix**.

If $\|\cdot \|$ is the matrix norm induced by the $L^{\infty }$ (vector) norm and A is lower triangular non-singular (i.e. $a_{ii}\neq 0$ for all i ), then

$\kappa (A)\geq {\frac {\max _{i}{\big (}|a_{ii}|{\big )}}{\min _{i}{\big (}|a_{ii}|{\big )}}}$

recalling that the eigenvalues of any triangular matrix are simply the diagonal entries.

The condition number computed with this norm is generally larger than the condition number computed relative to the Euclidean norm, but it can be evaluated more easily (and this is often the only practicably computable condition number, when the problem to solve involves a *non-linear algebra*, for example when approximating irrational and transcendental functions or numbers with numerical methods).

If the condition number is not significantly larger than one, the matrix is well-conditioned, which means that its inverse can be computed with good accuracy. If the condition number is very large, then the matrix is said to be ill-conditioned. Practically, such a matrix is almost singular, and the computation of its inverse, or solution of a linear system of equations is prone to large numerical errors.

A matrix that is not invertible is often said to have a condition number equal to infinity. Alternatively, it can be defined as $\kappa (A)=\|A\|\|A^{\dagger }\|$ , where $A^{\dagger }$ is the Moore-Penrose pseudoinverse. For square matrices, this unfortunately makes the condition number discontinuous, but it is a useful definition for rectangular matrices, which are never invertible but are still used to define systems of equations.

## Nonlinear

Condition numbers can also be defined for nonlinear functions, and can be computed using calculus. The condition number varies with the point; in some cases one can use the maximum (or supremum) condition number over the domain of the function or domain of the question as an overall condition number, while in other cases the condition number at a particular point is of more interest.

### One variable

The *absolute* condition number of a differentiable function f in one variable is the absolute value of the derivative of the function:

$\left|f'(x)\right|$

The *relative* condition number of f as a function is $\left|xf'/f\right|$ . Evaluated at a point x , this is

$\left|{\frac {xf'(x)}{f(x)}}\right|=\left|{\frac {(\log f)'}{(\log x)'}}\right|.$

Note that this is the absolute value of the elasticity of a function in economics.

Most elegantly, this can be understood as (the absolute value of) the ratio of the logarithmic derivative of f , which is $(\log f)'=f'/f$ , and the logarithmic derivative of x , which is $(\log x)'=x'/x=1/x$ , yielding a ratio of $xf'/f$ . This is because the logarithmic derivative is the infinitesimal rate of relative change in a function: it is the derivative $f'$ scaled by the value of f . Note that if a function has a zero at a point, its condition number at the point is infinite, as infinitesimal changes in the input can change the output from zero to positive or negative, yielding a ratio with zero in the denominator, hence infinite relative change.

More directly, given a small change $\Delta x$ in x , the relative change in x is $[(x+\Delta x)-x]/x=(\Delta x)/x$ , while the relative change in $f(x)$ is $[f(x+\Delta x)-f(x)]/f(x)$ . Taking the ratio yields

${\frac {[f(x+\Delta x)-f(x)]/f(x)}{(\Delta x)/x}}={\frac {x}{f(x)}}{\frac {f(x+\Delta x)-f(x)}{(x+\Delta x)-x}}={\frac {x}{f(x)}}{\frac {f(x+\Delta x)-f(x)}{\Delta x}}.$

The last term is the difference quotient (the slope of the secant line), and taking the limit yields the derivative.

Condition numbers of common elementary functions are particularly important in computing significant figures and can be computed immediately from the derivative. A few important ones are given below:

| Name | Symbol | Relative condition number |
|---|---|---|
| Addition / subtraction | $x+a$ | $\left\|{\frac {x}{x+a}}\right\|$ |
| Scalar multiplication | $ax$ | 1 |
| Division | $1/x$ | 1 |
| Polynomial | $x^{n}$ | $\|n\|$ |
| Exponential function | $e^{x}$ | $\|x\|$ |
| Natural logarithm function | $\ln(x)$ | $\left\|{\frac {1}{\ln(x)}}\right\|$ |
| Sine function | $\sin(x)$ | $\|x\cot(x)\|$ |
| Cosine function | $\cos(x)$ | $\|x\tan(x)\|$ |
| Tangent function | $\tan(x)$ | $\|x(\tan(x)+\cot(x))\|$ |
| Inverse sine function | $\arcsin(x)$ | ${\frac {x}{{\sqrt {1-x^{2}}}\arcsin(x)}}$ |
| Inverse cosine function | $\arccos(x)$ | ${\frac {\|x\|}{{\sqrt {1-x^{2}}}\arccos(x)}}$ |
| Inverse tangent function | $\arctan(x)$ | ${\frac {x}{(1+x^{2})\arctan(x)}}$ |

### Several variables

Condition numbers can be defined for any function f mapping its data from some domain (e.g. an m -tuple of real numbers x ) into some codomain (e.g. an n -tuple of real numbers $f(x)$ ), where both the domain and codomain are Banach spaces. They express how sensitive that function is to small changes (or small errors) in its arguments. This is crucial in assessing the sensitivity and potential accuracy difficulties of numerous computational problems, for example, polynomial root finding or computing eigenvalues.

The condition number of f at a point x (specifically, its **relative condition number**) is then defined to be the maximum ratio of the fractional change in $f(x)$ to any fractional change in x , in the limit where the change $\delta x$ in x becomes infinitesimally small:

$\lim _{\varepsilon \to 0^{+}}\sup _{\|\delta x\|\leq \varepsilon }\left[\left.{\frac {\left\|f(x+\delta x)-f(x)\right\|}{\|f(x)\|}}\right/{\frac {\|\delta x\|}{\|x\|}}\right],$

where $\|\cdot \|$ is a norm on the domain/codomain of f .

If f is differentiable, this is equivalent to:

${\frac {\|J(x)\|}{\|f(x)\|/\|x\|}},$

where ⁠ $J(x)$ ⁠ denotes the Jacobian matrix of partial derivatives of f at x , and $\|J(x)\|$ is the induced norm on the matrix.
