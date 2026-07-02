---
title: "Regula falsi"
source: https://en.wikipedia.org/wiki/Regula_falsi
domain: root-finding-methods
license: CC-BY-SA-4.0
tags: root-finding algorithm, bisection method, secant method, brent's method
fetched: 2026-07-02
---

# *Regula falsi*

In mathematics, the ***regula falsi***, **method of false position**, or **false position method** is a family of algorithms used to solve linear equations and smooth nonlinear equations for a single unknown value. In its oldest known examples found in cuneiform and hieroglyphic writings, the method replaces simple trial and error with proportional correction of an initial guess. In modern usage, the method relies on linear interpolation based on two different guesses.

## Two historical types

Two basic types of false position method can be distinguished historically, *simple false position* and *double false position*.

*Simple false position* is aimed at solving problems involving direct proportion and can be thought of as an early algorithm for division. Such problems can be written algebraically in the form: determine *x* such that

$ax=b,$

if *a* and *b* are known. The method begins by using a test input value *x*′, and finding the corresponding output value *b*′ by multiplication: *ax*′ = *b*′. The correct answer is then found by proportional adjustment, *x* = ⁠*b*/ *b*′⁠ *x*′.

As an example, consider problem 26 in the Rhind papyrus, which asks for a solution of (written in modern notation) the equation *x* + ⁠*x*/4⁠ = 15. This is solved by false position. First, guess that *x* = 4 to obtain, on the left, 4 + ⁠4/4⁠ = 5. This guess is a good choice since it produces an integer value. However, 4 is not the solution of the original equation, as it gives a value which is three times too small. To compensate, multiply x (currently set to 4) by 3 and substitute again to get 12 + ⁠12/4⁠ = 15, verifying that the solution is *x* = 12.

*Double false position* is aimed at solving more difficult problems that can be written algebraically in the form: determine *x* such that

$f(x)=ax+c=0,$

if it is known that

${\begin{aligned}f(x_{1})&=b_{1};\\f(x_{2})&=b_{2}.\end{aligned}}$

Double false position is mathematically equivalent to linear interpolation. By using a pair of test inputs and the corresponding pair of outputs, the result of this algorithm given by,

$x={\frac {b_{1}x_{2}-b_{2}x_{1}}{b_{1}-b_{2}}},$

would be memorized and carried out by rote. Indeed, the rule as given by Robert Recorde in his *Ground of Artes* (c. 1542) is:

Gesse at this woorke as happe doth leade. By chaunce to truthe you may procede. And firste woorke by the question, Although no truthe therein be don. Suche falsehode is so good a grounde, That truth by it will soone be founde. From many bate to many mo, From to fewe take to fewe also. With to much ioyne to fewe againe, To to fewe adde to manye plaine. In crossewaies multiplye contrary kinde, All truthe by falsehode for to fynde.

For an affine linear function,

$f(x)=ax+c,$

double false position provides the exact solution, while for a nonlinear function *f* it provides an approximation that can be successively improved by iteration.

## History

The simple false position technique is found in cuneiform tablets from ancient Babylonian mathematics, and in papyri from ancient Egyptian mathematics.

Double false position arose in late antiquity as a purely arithmetical algorithm. In the ancient Chinese mathematical text called *The Nine Chapters on the Mathematical Art* (九章算術), dated from 200 BC to AD 100, most of Chapter 7 was devoted to the algorithm. There, the procedure was justified by concrete arithmetical arguments, then applied creatively to a wide variety of story problems, including one involving what we would call secant lines on a conic section. A more typical example is this "joint purchase" problem involving an "excess and deficit" condition:

> Now an item is purchased jointly; everyone contributes 8 [coins], the excess is 3; everyone contributes 7, the deficit is 4. Tell: The number of people, the item price, what is each? Answer: 7 people, item price 53.

Between the 9th and 10th centuries, the Egyptian mathematician Abu Kamil wrote a now-lost treatise on the use of double false position, known as the *Book of the Two Errors* (*Kitāb al-khaṭāʾayn*). The oldest surviving writing on double false position from the Middle East is that of Qusta ibn Luqa (10th century), an Arab mathematician from Baalbek, Lebanon. He justified the technique by a formal, Euclidean-style geometric proof. Within the tradition of medieval Muslim mathematics, double false position was known as *hisāb al-khaṭāʾayn* ("reckoning by two errors"). It was used for centuries to solve practical problems such as commercial and juridical questions (estate partitions according to rules of Quranic inheritance), as well as purely recreational problems. The algorithm was often memorized with the aid of mnemonics, such as a verse attributed to Ibn al-Yasamin and balance-scale diagrams explained by al-Hassar and Ibn al-Banna, all three being mathematicians of Moroccan origin.

Leonardo of Pisa (Fibonacci) devoted Chapter 13 of his book *Liber Abaci* (AD 1202) to explaining and demonstrating the uses of double false position, terming the method *regulis elchatayn* after the *al-khaṭāʾayn* method that he had learned from Arab sources. In 1494, Pacioli used the term *el cataym* in his book *Summa de arithmetica*, probably taking the term from Fibonacci. Other European writers would follow Pacioli and sometimes provided a translation into Latin or the vernacular. For instance, Tartaglia translates the Latinized version of Pacioli's term into the vernacular "false positions" in 1556. Pacioli's term nearly disappeared in the 16th century European works and the technique went by various names such as "Rule of False", "Rule of Position" and "Rule of False Position". *Regula Falsi* appears as the Latinized version of Rule of False as early as 1690.

Several 16th-century European authors felt the need to apologize for the name of the method in a science that seeks to find the truth. For instance, in 1568 Humphrey Baker says:

> The Rule of falsehoode is so named not for that it teacheth anye deceyte or falsehoode, but that by fayned numbers taken at all aduentures, it teacheth to finde out the true number that is demaunded, and this of all the vulgar Rules which are in practise) is ye most excellence.

## Numerical analysis

The method of false position provides an exact solution for linear functions, but more direct algebraic techniques have supplanted its use for these functions. However, in numerical analysis, double false position became a root-finding algorithm used in iterative numerical approximation techniques.

Many equations, including most of the more complicated ones, can be solved only by iterative numerical approximation. This consists of trial and error, in which various values of the unknown quantity are tried. That trial-and-error may be guided by calculating, at each step of the procedure, a new estimate for the solution. There are many ways to arrive at a calculated-estimate and *regula falsi* provides one of these.

Given an equation, move all of its terms to one side so that it has the form, *f* (*x*) = 0, where f is some function of the unknown variable x. A value c that satisfies this equation, that is, *f* (*c*) = 0, is called a *root* or *zero* of the function f and is a solution of the original equation. If f is a continuous function and there exist two points *a*0 and *b*0 such that *f* (*a*0) and *f* (*b*0) are of opposite signs, then, by the intermediate value theorem, the function *f* has a root in the interval (*a*0, *b*0).

There are many root-finding algorithms that can be used to obtain approximations to such a root. One of the most common is Newton's method, but it can fail to find a root under certain circumstances and it may be computationally costly since it requires a computation of the function's derivative. Other methods are needed and one general class of methods are the *two-point bracketing methods*. These methods proceed by producing a sequence of shrinking intervals [*a**k*, *b**k*], at the kth step, such that (*a**k*, *b**k*) contains a root of *f*.

### Two-point bracketing methods

These methods start with two x-values, initially found by trial-and-error, at which *f* (*x*) has opposite signs. Under the continuity assumption, a root of f is guaranteed to lie between these two values, that is to say, these values "bracket" the root. A point strictly between these two values is then selected and used to create a smaller interval that still brackets a root. If c is the point selected, then the smaller interval goes from c to the endpoint where *f* (*x*) has the sign opposite that of *f* (*c*). In the improbable case that *f* (*c*) = 0, a root has been found and the algorithm stops. Otherwise, the procedure is repeated as often as necessary to obtain an approximation to the root to any desired accuracy.

The point selected in any current interval can be thought of as an estimate of the solution. The different variations of this method involve different ways of calculating this solution estimate.

Preserving the bracketing and ensuring that the solution estimates lie in the interior of the bracketing intervals guarantees that the solution estimates will converge toward the solution, a guarantee not available with other root finding methods such as Newton's method or the secant method.

The simplest variation, called the bisection method, calculates the solution estimate as the midpoint of the bracketing interval. That is, if at step k, the current bracketing interval is [*a**k*, *b**k*], then the new solution estimate ck is obtained by,

$c_{k}={\frac {a_{k}+b_{k}}{2}}.$

This ensures that ck is between ak and bk, thereby guaranteeing convergence toward the solution.

Since the bracketing interval's length is halved at each step, the bisection method's error is, on average, halved with each iteration. Hence, every 3 iterations, the method gains approximately a factor of 23, i.e. roughly a decimal place, in accuracy. This is commonly referred to as 1st-order convergence, meaning the number of digits of precision is proportional to the number of iterations used.

### The *regula falsi* (false position) method

The convergence rate of the bisection method could possibly be improved by using a different solution estimate.

The *regula falsi* method calculates the new solution estimate as the x-intercept of the line segment joining the endpoints of the function on the current bracketing interval. Essentially, the root is being approximated by replacing the actual function by a line segment on the bracketing interval and then using the classical double false position formula on that line segment.

More precisely, suppose that in the k-th iteration the bracketing interval is (*a**k*, *b**k*). Construct the line through the points (*a**k*, *f* (*a**k*)) and (*b**k*, *f* (*b**k*)), as illustrated. This line is a secant or chord of the graph of the function *f*. In point-slope form, its equation is given by

$y-f(b_{k})={\frac {f(b_{k})-f(a_{k})}{b_{k}-a_{k}}}(x-b_{k}).$

Now choose *c**k* to be the x-intercept of this line, that is, the value of x for which *y* = 0, and substitute these values to obtain

$f(b_{k})+{\frac {f(b_{k})-f(a_{k})}{b_{k}-a_{k}}}(c_{k}-b_{k})=0.$

Solving this equation for *c**k* gives:

$c_{k}=b_{k}-f(b_{k}){\frac {b_{k}-a_{k}}{f(b_{k})-f(a_{k})}}={\frac {a_{k}f(b_{k})-b_{k}f(a_{k})}{f(b_{k})-f(a_{k})}}.$

This last symmetrical form has a computational advantage when using floating-point arithmetic: As a solution is approached, ak and bk will be very close together, and nearly always of the same sign. Such a subtraction can lose precision through cancellation. Because *f* (*b**k*) and *f* (*a**k*) are always of opposite sign the “subtraction” in the numerator of the improved formula is effectively an addition (as is the subtraction in the denominator too).

At iteration number *k*, the number ck is calculated as above and then, if *f* (*a**k*) and *f* (*c**k*) have the same sign, set *a**k* + 1 = *c**k* and *b**k* + 1 = *b**k*, otherwise set *a**k* + 1 = *a**k* and *b**k* + 1 = *c**k*. This process is repeated until the root is approximated sufficiently well. The above formula is also used in the secant method.

For nonlinear functions, once the interval of search shrinks far enough that the second derivative has constant sign throughout the interval, one endpoint of the search becomes fixed, while the other converges to the root. Thus, the best estimate of the solution is the last calculated value of $c_{k}$ . However, because the interval stops shrinking, *regula falsi* can not match the bisection method's guarantee of precision. In some cases, rate of convergence can drop below that of the bisection method. Modified versions of *regula falsi* are generally to be preferred because they can fix these shortcomings at minimal cost.

## Analysis

Since the initial end-points *a*0 and *b*0 are chosen such that *f* (*a*0) and *f* (*b*0) are of opposite signs, at each step, one of the end-points will get closer to a root of *f*. If the second derivative of *f* is of constant sign (so there is no inflection point) in the interval, then one endpoint (the one where *f* also has the same sign) will remain fixed for all subsequent iterations while the converging endpoint becomes updated. As a result, unlike the bisection method, the width of the bracket does not tend to zero (unless the zero is at an inflection point around which sign(*f* ) = −sign(*f*")). As a consequence, the linear approximation to *f* (*x*), which is used to pick the false position, does not improve as rapidly as possible.

One example of this phenomenon is the function

$f(x)=2x^{3}-4x^{2}+3x$

on the initial bracket [−1,1]. The left end, −1, is never replaced (it does not change at first and after the first three iterations, *f*" is negative on the interval) and thus the width of the bracket never falls below 1. Hence, the right endpoint approaches 0 at a linear rate (the number of accurate digits grows linearly, with a rate of convergence of 2/3).

For discontinuous functions, this method can only be expected to find a point where the function changes sign (for example at *x* = 0 for 1/*x* or the sign function). In addition to sign changes, it is also possible for the method to converge to a point where the limit of the function is zero, even if the function is undefined (or has another value) at that point (for example at *x* = 0 for the function given by *f* (*x*) = abs(*x*) − *x*2 when *x* ≠ 0 and by *f* (0) = 5, starting with the interval [-0.5, 3.0]). It is mathematically possible with discontinuous functions for the method to fail to converge to a zero limit or sign change, but this is not a problem in practice since it would require an infinite sequence of coincidences for both endpoints to get stuck converging to discontinuities where the sign does not change, for example at *x* = ±1 in

$f(x)={\frac {1}{(x-1)^{2}}}+{\frac {1}{(x+1)^{2}}}.$

The method of bisection avoids this hypothetical convergence problem.

## Improvements in *regula falsi*

Though *regula falsi* always converges, usually considerably faster than bisection, there are situations that can slow its convergence – sometimes to a prohibitive degree. That problem isn't unique to *regula falsi*: Other than bisection, *all* of the numerical equation-solving methods can have a slow-convergence or no-convergence problem under some conditions. Sometimes, Newton's method and the secant method *diverge* instead of converging – and often do so under the same conditions that slow *regula falsi's* convergence.

But, though *regula falsi* is one of the best methods, and even in its original un-improved version would often be the best choice; for example, when Newton's isn't used because the derivative is prohibitively time-consuming to evaluate, or when Newton's and *Successive-Substitutions* have failed to converge.

*Regula falsi's* failure mode is easy to detect: The same end-point is retained twice in a row. The problem is easily remedied by picking instead a modified false position, chosen to avoid slowdowns due to those relatively unusual unfavorable situations. A number of such improvements to *regula falsi* have been proposed; two of them, the Illinois algorithm and the Anderson–Björk algorithm, are described below.

### The Illinois algorithm

The Illinois algorithm halves the y-value of the retained end point in the next estimate computation when the new y-value (that is, *f* (*c**k*)) has the same sign as the previous one (*f* (*c**k* − 1)), meaning that the end point of the previous step will be retained. Hence:

$c_{k}={\frac {{\frac {1}{2}}f(b_{k})a_{k}-f(a_{k})b_{k}}{{\frac {1}{2}}f(b_{k})-f(a_{k})}}$

or

$c_{k}={\frac {f(b_{k})a_{k}-{\frac {1}{2}}f(a_{k})b_{k}}{f(b_{k})-{\frac {1}{2}}f(a_{k})}},$

down-weighting one of the endpoint values to force the next *c**k* to occur on that side of the function. The factor ⁠1/2⁠ used above may look arbitrary, but it guarantees superlinear convergence (asymptotically, the algorithm will perform two regular steps after any modified step, and has order of convergence 1.442). There are other ways to pick the rescaling which give even better superlinear convergence rates.

The above adjustment to *regula falsi* is called the **Illinois algorithm** by some scholars. Ford (1995) summarizes and analyzes this and other similar superlinear variants of the method of false position.

### Anderson–Björck algorithm

Suppose that in the k-th iteration the bracketing interval is [*a**k*, *b**k*] and that the functional value of the new calculated estimate *c**k* has the same sign as *f* (*b**k*). In this case, the new bracketing interval [*a**k* + 1, *b**k* + 1] = [*a**k*, *c**k*] and the left-hand endpoint has been retained. (So far, that's the same as ordinary Regula Falsi and the Illinois algorithm.)

But, whereas the Illinois algorithm would multiply *f* (*a**k*) by ⁠1/2⁠, Anderson–Björck algorithm multiplies it by *m*, where *m* has one of the two following values:

${\begin{aligned}m'&=1-{\frac {f(c_{k})}{f(b_{k})}},\\m&={\begin{cases}m'&{\text{if }}m'>0,\\{\frac {1}{2}}&{\text{otherwise.}}\end{cases}}\end{aligned}}$

For simple roots, Anderson–Björck performs very well in practice.

### ITP method

Given $\kappa _{1}\in (0,\infty ),\kappa _{2}\in \left[1,1+\phi \right)$ , $n_{1/2}\equiv \lceil (b_{0}-a_{0})/2\epsilon \rceil$ and $n_{0}\in [0,\infty )$ where $\phi$ is the golden ration ${\tfrac {1}{2}}(1+{\sqrt {5}})$ , in each iteration $j=0,1,2...$ the ITP method calculates the point $x_{\text{ITP}}$ following three steps:

1. *[Interpolation Step] Calculate the bisection and the regula falsi points: $x_{1/2}\equiv {\frac {a+b}{2}}$* and $x_{f}\equiv {\frac {bf(a)-af(b)}{f(a)-f(b)}}$  ;
2. *[Truncation Step] Perturb the estimator towards the center: $x_{t}\equiv x_{f}+\sigma \delta$* where *$\sigma \equiv {\text{sign}}(x_{1/2}-x_{f})$* and *$\delta \equiv \min\{\kappa _{1}|b-a|^{\kappa _{2}},|x_{1/2}-x_{f}|\}$* ;
3. *[Projection Step] Project the estimator to minmax interval: $x_{\text{ITP}}\equiv x_{1/2}-\sigma \rho _{k}$ where $\rho _{k}\equiv \min \left\{\epsilon 2^{n_{1/2}+n_{0}-j}-{\frac {b-a}{2}},|x_{t}-x_{1/2}|\right\}$ .*

The value of the function $f(x_{\text{ITP}})$ on this point is queried, and the interval is then reduced to bracket the root by keeping the sub-interval with function values of opposite sign on each end. This three step procedure guarantees that the minmax properties of the bisection method are enjoyed by the estimate as well as the superlinear convergence of the secant method. And, is observed to outperform both bisection and interpolation based methods under smooth and non-smooth functions.

## Practical considerations

When solving one equation, or just a few, using a computer, the bisection method is an adequate choice. Although bisection isn't as fast as the other methods—when they're at their best and don't have a problem—bisection nevertheless is guaranteed to converge at a useful rate, roughly halving the error with each iteration – gaining roughly a decimal place of accuracy with every 3 iterations.

For manual calculation, by calculator, one tends to want to use faster methods, and they usually, but not always, converge faster than bisection. But a computer, even using bisection, will solve an equation, to the desired accuracy, so rapidly that there's no need to try to save time by using a less reliable method—and every method is less reliable than bisection.

An exception would be if the computer program had to solve equations very many times during its run. Then the time saved by the faster methods could be significant.

Then, a program could start with Newton's method, and, if Newton's isn't converging, switch to *regula falsi*, maybe in one of its improved versions, such as the Illinois or Anderson–Björck versions. Or, if even that isn't converging as well as bisection would, switch to bisection, which always converges at a useful, if not spectacular, rate.

When the change in *y* has become very small, and *x* is also changing very little, then Newton's method most likely will not run into trouble, and will converge. So, under those favorable conditions, one could switch to Newton's method if one wanted the error to be very small and wanted very fast convergence.

## Example: Growth of a bulrush

In chapter 7 of *The Nine Chapters*, a root finding problem can be translated to modern language as follows:

> Excess And Deficit Problem #11:
> 
> - A bulrush grew 3 units on its first day. At the end of each day, the plant is observed to have grown by ⁠ 1 /2⁠ of the previous day's growth.
> - A club-rush grew 1 unit on its first day. At the end of each day, the plant has grown by 2 times as much as the previous day's growth.
> - Find the time *[in fractional days]* that the club-rush becomes as tall as the bulrush.
> 
> Answer: $\left(2+{\frac {6}{13}}\right)$ days; the height is $\left(4+{\frac {8}{10}}+{\frac {6}{130}}\right)$ units.
> 
> Explanation:
> 
> - Suppose it is day 2. The club-rush is shorter than the bulrush by 1.5 units.
> - Suppose it is day 3. The club-rush is taller than the bulrush by 1.75 units. ∎

To understand this, we shall model the heights of the plants on day n (n = 1, 2, 3...) after a geometric series.

$B(n)=\sum _{i=1}^{n}3\cdot {\frac {1}{2^{i-1}}}\quad$

Bulrush

$C(n)=\sum _{i=1}^{n}1\cdot 2^{i-1}\quad$

Club-rush

For the sake of better notations, let $\ k=i-1~.$ Rewrite the plant height series $\ B(n),\ C(n)\$ in terms of k and invoke the formula for a geometric series.

$\ B(n)=\sum _{k=0}^{n-1}3\cdot {\frac {1}{2^{k}}}=3\left({\frac {1-({\tfrac {1}{2}})^{n-1+1}}{1-{\tfrac {1}{2}}}}\right)=6\left(1-{\frac {1}{2^{n}}}\right)$

$\ C(n)=\sum _{k=0}^{n-1}2^{k}={\frac {~~1-2^{n}}{\ 1-2\ }}=2^{n}-1\$

Now, use *regula falsi* to find the root of $\ (C(n)-B(n))\$

$\ F(n):=C(n)-B(n)={\frac {6}{2^{n}}}+2^{n}-7\$

- Set $\ x_{1}=2\$ and compute $\ F(x_{1})=F(2)\$ which equals −1.5 (the "deficit").
- Set $\ x_{2}=3\$ and compute $\ F(x_{2})=F(3)\$ which equals 1.75 (the "excess").

Estimated root (1st iteration):

$\ {\hat {x}}~=~{\frac {~x_{1}F(x_{2})-x_{2}F(x_{1})~}{F(x_{2})-F(x_{1})}}~=~{\frac {~2\times 1.75+3\times 1.5~}{1.75+1.5}}~=~{\frac {32}{13}}~\approx ~2.4615\$

To find the exact root, let $y=2^{n}$ so that we seek to solve $6/y+y-7~=~0$ . Multiply by y to get the quadratic equation $y^{2}-7y+6=0$ which has roots $y=0$ (which is spurious here) and $y=6$ (the root we want). Thus $n~=~\log _{2}(6)~\approx ~2.5849625$ and our estimation has an error of 4.78%.

## Example code

This example program, written in the C programming language, is an example of the Illinois algorithm. To find the positive number *x* where cos(*x*) = *x*3, the equation is transformed into a root-finding form *f* (*x*) = cos(*x*) − *x*3 = 0.

```mw
#include <stdio.h>
#include <math.h>

double f(double x) {
   return cos(x) - x * x * x;
}
/* a,b: endpoints of an interval where we search
   e: half of upper bound for relative error
   m: maximal number of iteration
*/
double falsi_method(double (*f)(double), double a, double b, double e, int m) {
   double c, fc;
   int n, side = 0;
   /* starting values at endpoints of interval */
   double fa = f(a);
   double fb = f(b);

   for (n = 0; n < m; n++) {
      c = (fa * b - fb * a) / (fa - fb);
      if (fabs(b - a) < e * fabs(b + a))
         break;
      fc = f(c);

      if (fc * fb > 0) {
         /* fc and fb have same sign, copy c to b */
         b = c; fb = fc;
         if (side == -1)
            fa /= 2;
         side = -1;
      } else if (fa * fc > 0) {
         /* fc and fa have same sign, copy c to a */
         a = c; fa = fc;
         if (side == +1)
            fb /= 2;
         side = +1;
      } else {
         /* fc * f_ very small (looks like zero) */
         break;
      }
   }
   return c;
}

int main(void) {
   printf("%0.15f\n", falsi_method(&f, 0, 1, 5E-15, 100));
   return 0;
}
```

After running this code, the final answer is approximately 0.865474033101614.
