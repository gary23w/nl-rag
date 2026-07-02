---
title: "Method of dominant balance"
source: https://en.wikipedia.org/wiki/Method_of_dominant_balance
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Method of dominant balance

In mathematics, the **method of dominant balance** approximates the solution to an equation by solving a simplified form of the equation containing 2 or more of the equation's terms that most influence (dominate) the solution and excluding terms contributing only small modifications to this approximate solution. Following an initial solution, iteration of the procedure may generate additional terms of an asymptotic expansion providing a more accurate solution.

An early example of the dominant balance method is the Newton polygon method. Newton developed this method to find an explicit approximation for an algebraic function. Newton expressed the function as proportional to the independent variable raised to a power, retained only the lowest-degree polynomial terms (dominant terms), and solved this simplified reduced equation to obtain an approximate solution. Dominant balance has a broad range of applications, solving differential equations arising in fluid mechanics, plasma physics, turbulence, combustion, nonlinear optics, geophysical fluid dynamics, and neuroscience.

## Asymptotic relations

The functions ${\textstyle f(z)}$ and $g(z)$ of parameter or independent variable ${\textstyle z}$ and the quotient ${\textstyle f(z)/g(z)}$ have limits as ${\textstyle z}$ approaches the limit ${\textstyle L}$ .

The function ${\textstyle f(z)}$ is *much less than* ${\textstyle g(z)}$ as ${\textstyle z}$ approaches ${\textstyle L}$ , written as ${\textstyle f(z)\ll g(z)\ (z\to L)}$ , if the limit of the quotient ${\textstyle f(z)/g(z)}$ is zero as ${\textstyle z}$ approaches ${\textstyle L}$ .

The relation ${\textstyle f(z)}$ is *lower order* than ${\textstyle g(z)}$ as ${\textstyle z}$ approaches ${\textstyle L}$ , written using little-o notation ${\textstyle f(z)=o(g(z))\ (z\to L)}$ , is identical to the ${\textstyle f(z)}$ is *much less than* ${\textstyle g(z)}$ as ${\textstyle z}$ approaches ${\textstyle L}$ relation.

The function ${\textstyle f(z)}$ is *equivalent* to ${\textstyle g(z)}$ as ${\textstyle z}$ approaches ${\textstyle L}$ , written as ${\textstyle f(z)\sim g(z)\ (z\to L)}$ , if the limit of the quotient ${\textstyle f(z)/g(z)}$ is 1 as ${\textstyle z}$ approaches ${\textstyle L}$ .

This result indicates that the zero function, ${\textstyle f(z)=0}$ for all values of ${\textstyle z}$ , can never be equivalent to any other function.

Asymptotically equivalent functions remain asymptotically equivalent under integration if requirements related to convergence are met. There are more specific requirements for asymptotically equivalent functions to remain asymptotically equivalent under differentiation.

## Equation properties

An equation's approximate solution is ${\textstyle s(z)}$ as ${\textstyle z}$ approaches limit ${\textstyle L}$ . The equation's terms that may be constants or contain this solution are ${\textstyle T_{0}(s),T_{1}(s),\ldots ,T_{n}(s)}$ . If the approximate solution is fully correct, the equation's terms sum to zero in this equation: $T_{0}(s)+T_{1}(s)+\ldots +T_{n}(s)=0.$ For distinct integer indices ${\textstyle i,j}$ , this equation is a sum of 2 terms and a remainder ${\textstyle R_{ij}(s)}$ expressed as ${\begin{aligned}&T_{i}(s)+T_{j}(s)+R_{ij}(s)=0\\&R_{ij}(s)=\sum _{{k=0} \atop {k\neq i,k\neq j}}^{n}T_{k}(s).\end{aligned}}$

*Balance* equation terms ${\textstyle T_{i}(s)}$ and ${\textstyle T_{j}(s)}$ means find the function ${\textstyle s(z)}$ that solves the *reduced equation* ${\textstyle T_{i}(s)+T_{j}(s)=0}$ with ${\textstyle T_{i}(s)\neq 0}$ and ${\textstyle T_{j}(s)\neq 0}$ . This solution ${\textstyle s(z)}$ is *consistent* if terms ${\textstyle T_{i}(s)}$ and ${\textstyle T_{j}(s)}$ are *dominant*; dominant means the remaining equation terms ${\textstyle R_{ij}(s)}$ are much less than terms ${\textstyle T_{i}(s)}$ and ${\textstyle T_{j}(s)}$ as ${\textstyle z}$ approaches ${\textstyle L}$ . A consistent solution that balances two equation terms may generate an accurate approximation to the full equation's solution for ${\textstyle z}$ values approaching ${\textstyle L}$ . Approximate solutions arising from balancing different terms of an equation may generate distinct approximate solutions e.g. inner and outer layer solutions.

In some cases, the reduced equation has coefficients containing a parameter ${\textstyle \epsilon }$ , but the parameter's exponent is different for the 2 terms. In this case, the reduced equation requires a *scale transformation* ${\textstyle z=\epsilon ^{\lambda }{\tilde {z}}}$ of the variable ${\textstyle z}$ using scaling exponent ${\textstyle \lambda }$ . The dominant balance method selects a scaling exponent ${\textstyle \lambda }$ to generate transformed terms, each transformed term now containing the parameter with the same exponent. Distinct pairs of terms and scaling transformations lead to distinct simplified equations called *distinguished limits*, and each equation may lead to a distinct solution. The Kruskal-Newton diagram facilitates identifying the required scale transformation needed for dominant balance of algebraic and differential equations.

For differential equation solutions containing an irregular singularity, the *leading behavior* is the first term of an asymptotic series solution that remains when the independent variable ${\textstyle z}$ approaches an irregular singularity ${\textstyle L}$ . The *controlling factor* is the fastest changing part of the leading behavior. It is advised to "show that the equation for the function obtained by factoring off the dominant balance solution from the exact solution itself has a solution that varies less rapidly than the dominant balance solution."

## Algorithm

The input is the set of equation terms and the limit L. The output is the set of approximate solutions. For each pair of distinct equation terms ${\textstyle T_{i}(s),T_{j}(s)}$ the algorithm applies a scale transformation if needed, balances the selected terms by finding a function that solves the reduced equation and then determines if this function is consistent. If the function balances the terms and is consistent, the algorithm adds the function to the set of approximate solutions, otherwise the algorithm rejects the function. The process is repeated for each pair of distinct equation terms.

Inputs

Set of equation terms

${\textstyle \{T_{0}(s),T_{1}(s),\ldots ,T_{n}(s)\}}$

and limit

${\textstyle L}$

Output

Set of approximate solutions

${\textstyle \{s_{0}(z),s_{1}(z),\dots \}}$

1. For each pair of distinct equation terms ${\textstyle T_{i}(s),T_{j}(s)}$ do:
  1. Apply a scale transformation if needed.
  2. Solve the reduced equation: ${\textstyle T_{i}(s)+T_{j}(s)=0}$ with ${\textstyle T_{i}(s)\neq 0}$ and ${\textstyle T_{j}(s)\neq 0}$ .
  3. Verify consistency: ${\textstyle R_{ij}(s)\ll T_{i}(s)\ (z\to L)}$ and ${\textstyle R_{ij}(s)\ll T_{j}(s)\ (z\to L).}$
  4. If function ${\textstyle s(z)}$ is consistent and solves the reduced equation, add this function to the set of approximate solutions, otherwise reject the function.

## Improved accuracy

The method may be iterated to generate additional terms of an asymptotic expansion to provide a more accurate solution. Iterative methods such as the Newton-Raphson method may generate a more accurate solution. A perturbation series, using the approximate solution as the first term, may also generate a more accurate solution.

## Examples

### Algebraic function

The dominant balance method will generate an approximate solution for variable ${\textstyle s}$ in algebraic equation ${\textstyle 1-16s+\epsilon s^{5}=0}$ that depends on parameter ${\textstyle \epsilon }$ . This example computes asymptotic values as ${\textstyle \epsilon }$ approaches zero because this example's goal is finding solutions for small ${\textstyle \epsilon }$ parameter values. The function ${\textstyle s=s(\epsilon )}$ denotes how the equation's solution depends on the equation's parameter ${\textstyle \epsilon }$ . The solution set is enumerated as ${\textstyle \{s_{0}(\epsilon ),s_{1}(\epsilon ),s_{2}(\epsilon ),s_{3}(\epsilon ),s_{4}(\epsilon )\}}$ .

#### Input

The set of equation terms is ${\textstyle \{1,-16s,\epsilon s^{5}\}}$ and asymptotic computations are as ${\textstyle \epsilon }$ approaches zero.

#### First term pair

1. Select the terms ${\textstyle 1}$ and ${\textstyle -16s}$ .
2. Rewriting the selected terms as ${\textstyle \epsilon ^{0}1}$ and ${\textstyle -\epsilon ^{0}16s}$ , the parameter's exponents are the same (0,0) for both terms so no scale transformation needed.
3. Solve the reduced equation: $1-16s=0,s(\epsilon )={\tfrac {1}{16}}$ .
4. Verify consistency: $\epsilon s^{5}\ll 1\ (\epsilon \to 0),\ \epsilon s^{5}\ll 16s\ (\epsilon \to 0)\$ for $s(\epsilon )={\tfrac {1}{16}}.$
5. Add this function to the set of approximate solutions: $s_{0}(\epsilon )={\tfrac {1}{16}}$ .

#### Second term pair

1. Select the terms $-16s$ and $\epsilon s^{5}$ .
2. Rewriting the selected terms as $-\epsilon ^{0}16s$ and $\epsilon ^{1}s^{5}$ , the parameter's exponents are different (0,1) so a scale transformation is needed. Apply the scale transformation $s=\epsilon ^{-1/4}{\tilde {s}}$ . The parameter exponents of the transformed terms $-\epsilon ^{-1/4}16{\tilde {s}}$ and $\epsilon ^{-1/4}{\tilde {s}}^{5}=0$ are the same (-1/4,-1/4). The transformed equation becomes $\epsilon ^{1/4}-16{\tilde {s}}+{\tilde {s}}^{5}=0$ .
3. Solve the reduced equation: $-16{\tilde {s}}+{\tilde {s}}^{5}=0,\ {\tilde {s}}=2,-2,2i,-2i$ .
4. Verify consistency: $\epsilon ^{1/4}\ll 16{\tilde {s}}\ (\epsilon \to 0),\ \epsilon ^{1/4}\ll {\tilde {s}}^{5}\ (\epsilon \to 0)\$ for ${\tilde {s}}=2,-2,2i,-2i.$
5. Add these functions to the set of approximate solutions:

$s_{1}(\epsilon )={\frac {2}{\epsilon ^{1/4}}},s_{2}(\epsilon )={\frac {-2}{\epsilon ^{1/4}}},s_{3}(\epsilon )={\frac {2i}{\epsilon ^{1/4}}},s_{4}(\epsilon )={\frac {-2i}{\epsilon ^{1/4}}}.$

#### Third term pair

1. Select the terms 1 and $\epsilon s^{5}$ .
2. Rewriting the selected terms as $\epsilon ^{0}1$ and $\epsilon ^{1}s^{5}$ , the parameter's exponents are different (0,1) so a scale transformation is needed. Apply the scale transformation $s=\epsilon ^{-1/5}{\tilde {s}}$ . The parameter exponents of the transformed terms $\epsilon ^{0}1$ and $\epsilon ^{0}{\tilde {s}}^{5}$ are the same (0,0). The transformed equation is $1-16\epsilon ^{-1/5}{\tilde {s}}+{\tilde {s}}^{5}=0.$
3. Solve the reduced equation: $1+{\tilde {s}}^{5}=0,\ {\tilde {s}}=(-1)^{1/5}.$
4. The function is not consistent: $-16\epsilon ^{-1/5}{\tilde {s}}\gg 1\ (\epsilon \to 0),\ \epsilon ^{-1/5}{\tilde {s}}\gg {\tilde {s}}^{5}\ (\epsilon \to 0)\$ for ${\tilde {s}}=(-1)^{1/5}.$
5. Reject this function: $s=\epsilon ^{-1/5}(-1)^{1/5}.$

#### Output

The set of approximate solutions has 5 functions: $\left\{{\frac {1}{16}},{\frac {2}{\epsilon ^{1/4}}},{\frac {-2}{\epsilon ^{1/4}}},{\frac {2i}{\epsilon ^{1/4}}},{\frac {-2i}{\epsilon ^{1/4}}}\right\}.$

#### Perturbation series solution

The approximate solutions are the first terms in the perturbation series solutions.

${\begin{aligned}&s_{0}(\epsilon )={\frac {1}{16}}+{\frac {1}{16777216}}\epsilon ^{1}+{\frac {5}{17592186044416}}\epsilon ^{2}+\ldots ,\\&s_{1}(\epsilon )={\frac {2}{\epsilon ^{1/4}}}-{\frac {1}{64}}-{\frac {5}{16384}}\epsilon ^{\frac {1}{4}}-{\frac {5}{524288}}\epsilon ^{\frac {1}{2}}-\ldots ,\\&s_{2}(\epsilon )=-{\frac {2}{\epsilon ^{1/4}}}-{\frac {1}{64}}+{\frac {5}{16384}}\epsilon ^{\frac {1}{4}}-{\frac {5}{524288}}\epsilon ^{\frac {1}{2}}+\ldots ,\\&s_{3}(\epsilon )={\frac {2i}{\epsilon ^{1/4}}}-{\frac {1}{64}}+{\frac {5i}{16384}}\epsilon ^{\frac {1}{4}}+{\frac {5}{524288}}\epsilon ^{\frac {1}{2}}-\ldots \\&s_{4}(\epsilon )=-{\frac {2i}{\epsilon ^{1/4}}}-{\frac {1}{64}}-{\frac {5i}{16384}}\epsilon ^{\frac {1}{4}}+{\frac {5}{524288}}\epsilon ^{\frac {1}{2}}+\ldots ,\\\end{aligned}}$

### Differential equation

The differential equation ${\textstyle z^{3}w^{\prime \prime }-w=0}$ is known to have a solution with an exponential leading term. The transformation ${\textstyle w(z)=e^{s(z)}}$ leads to the differential equation ${\textstyle 1-z^{3}(s^{\prime })^{2}-z^{3}s^{\prime \prime }=0}$ . The dominant balance method will find an approximate solution as ${\textstyle z}$ approaches zero because this example's focus is for solutions for small ${\textstyle z}$ values. Scaled transformations will not be used because there are no equation parameters. Two consecutive applications of the dominant balance method will generate the 2 leading terms of an asymptotic series.

#### Input

The set of equation terms is ${\textstyle \{1,-z^{3}(s^{\prime })^{2},-z^{3}s^{\prime \prime }\}}$ and the limit is zero.

##### First term pair

1. Select 1 and $-z^{3}(s^{\prime })^{2}$ .
2. The scale transformation is not required.
3. Solve the reduced equation: $1-z^{3}(s^{\prime })^{2}=0,\ s(z)=\pm 2z^{-1/2}$
4. Verify consistency: $z^{3}s^{\prime \prime }\ll 1\ (z\to 0),\ z^{3}s^{\prime \prime }\ll z^{3}(s^{\prime })^{2}\ (z\to 0)$ for $s(z)=\pm 2z^{-1/2}.$
5. Add these 2 functions to the set of approximate solutions: $s_{+}(z)=+2z^{-1/2},\ s_{-}(z)=-2z^{-1/2}.$

#### Second term pair

1. Select 1 and $-z^{3}s^{\prime \prime }$
2. The scale transformation is not required.
3. Solve the reduced equation: $1-z^{3}s^{\prime \prime }=0,\ s(z)={\tfrac {1}{2}}z^{-1}$
4. The function is not consistent: $z^{3}(s^{\prime })^{2}\gg 1\ (z\to 0),\ z^{3}(s^{\prime })^{2}\gg z^{3}s^{\prime \prime }\ (z\to 0)$ for $s(z)={\tfrac {1}{2}}z^{-1}.$
5. Reject this function: $s(z)={\tfrac {1}{2}}z^{-1}.$ .

#### Third term pair

1. Select $-z^{3}(s^{\prime })^{2}$ and $-z^{3}s^{\prime \prime }$ .
2. The scale transformation is not required.
3. Solve the reduced equation: $z^{3}(s^{\prime })^{2}+z^{3}s^{\prime \prime }=0,\ s(z)=\ln z$ .
4. The function is not consistent: $1\gg z^{3}(s^{\prime })^{2}\ (z\to 0)\$ and $\ 1\gg \ z^{3}s^{\prime \prime }\ (z\to 0)$ for $s(z)=\ln z.$
5. Reject this function: $s(z)=\ln z.$

#### Output

The set of approximate solutions has 2 functions: $\left\{+2z^{-1/2},-2z^{-1/2}\right\}.$

#### Find 2-term solutions

Using the 1-term solution, a 2-term solution is $s_{2\pm }(z)=\pm 2z^{-1/2}+s(z).$ Substitution of this 2-term solution into the original differential equation generates a new differential equation: ${\begin{aligned}1-z^{3}(s_{2\pm }^{\prime })^{2}-z^{3}s_{2\pm }^{\prime \prime }&=0\\\pm 1\mp {\frac {4}{3}}zs^{\prime }+{\frac {2}{3}}z^{5/2}(s^{\prime })^{2}+{\frac {2}{3}}z^{5/2}s^{\prime \prime }&=0.\end{aligned}}$

#### Input

The set of equation terms is ${\textstyle \{\pm 1,\mp {\frac {4}{3}}zs^{\prime },{\frac {2}{3}}z^{5/2}(s^{\prime })^{2},{\frac {2}{3}}z^{5/2}s^{\prime \prime }\}}$ and the limit is zero.

##### First term pair

1. Select

1

and

$-{\tfrac {4}{3}}zs^{\prime }$

.

2. The scale transformation is not required.

3. Solve the reduced equation:

$1-{\tfrac {4}{3}}zs^{\prime }=0,\ s(z)={\tfrac {3}{4}}\ln z$

.

4. Verify consistency:

${\tfrac {2}{3}}z^{5/2}(s^{\prime })^{2}+{\tfrac {2}{3}}z^{5/2}s^{\prime \prime }\ll 1\ (z\to 0),{\text{for}}\ s(z)={\tfrac {3}{4}}\ln z$

${\tfrac {2}{3}}z^{5/2}(s^{\prime })^{2}+{\tfrac {2}{3}}z^{5/2}s^{\prime \prime }\ll {\tfrac {4}{3}}zs^{\prime }\ (z\to 0)\ {\text{for}}\ s(z)={\tfrac {3}{4}}\ln z.$

5. Add these functions to the set of approximate solutions:

${\textstyle s_{2+}(z)=+2z^{-1/2}+{\tfrac {3}{4}}\ln z}$

${\textstyle s_{2-}(z)=-2z^{-1/2}+{\tfrac {3}{4}}\ln z}$

.

#### Other term pairs

For other term pairs, the functions that solve the reduced equations are not consistent.

#### Output

The set of approximate solutions has 2 functions: $\left\{+2z^{-1/2}+{\tfrac {3}{4}}\ln z,-2z^{-1/2}+{\tfrac {3}{4}}\ln z\right\}.$

#### Asymptotic expansion

The next iteration generates a 3-term solution ${\textstyle s_{3\pm }(z)=\pm 2z^{-1/2}+{\tfrac {3}{4}}\operatorname {ln} (z)+h(z)}$ with ${\textstyle h(z)\ll 1\ (z\to 0)}$ and this means that a power series expansion can represent the remainder of the solution. The dominant balance method generates the leading term to this asymptotic expansion with constant ${\textstyle A}$ and expansion coefficients determined by substitution into the full differential equation:

$w(z)=Az^{3/4}e^{\pm 2z^{-1/2}}\left(\sum _{n=0}^{m}\ a_{n}z^{n/2}\right)$

$a_{n+1}=\pm {\frac {(n-1/2)(n+3/2)a_{n}}{4(n+1)}}.$

A partial sum of this non-convergent series generates an approximate solution. The leading term corresponds to the Liouville-Green (LG) or Wentzel–Kramers–Brillouin (WKB) approximation.
