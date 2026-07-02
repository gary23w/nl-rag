---
title: "Aitken's delta-squared process"
source: https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Aitken's delta-squared process

In numerical analysis, **Aitken's delta-squared process** or **Aitken extrapolation** is a series acceleration method used for accelerating the rate of convergence of a sequence. It is named after Alexander Aitken, who introduced this method in 1926 as part of an extension to Bernoulli's method. It is most useful for accelerating the convergence of a sequence that is converging linearly. A precursor form was known to Seki Kōwa (1642 – 1708) and applied to the rectification of the circle, i.e., to the calculation of π.

## Definition

Given a sequence $X={(x_{n})}$ with $n=0,1,2,3,\ldots ,$ Aitken's delta-squared process associates to this sequence the new sequence

$A[X]=(a_{n})={\left({\frac {x_{n}\,x_{n+2}-x_{n+1}^{2}}{x_{n}+x_{n+2}-2\,x_{n+1}}}\right)},$

which can also be written as

$A[X]=\left(x_{n}-{\frac {(\Delta x_{n})^{2}}{\Delta ^{2}x_{n}}}\right),$

with ${\textstyle \Delta x_{n}=x_{n+1}-x_{n}}$ and ${\textstyle \Delta ^{2}x_{n}=x_{n}-2x_{n+1}+x_{n+2}=\Delta x_{n+1}-\Delta x_{n}.}$ Both are the same sequence algebraically but the latter has improved numerical stability in computational implementation.

${\textstyle A[X]}$ is ill-defined if the sequence ${\textstyle \Delta ^{2}[X]=(\Delta ^{2}x_{n})}$ contains a zero element, which occurs if the sequence of forward differences, ${\textstyle \Delta [X]=(\Delta x_{n}),}$ has any repeated term. From a theoretical point of view, if that occurs only for a finite number of indices, one could apply the Aitken process to only the part of the sequence X with indices $n>n_{0}$ such that $n_{0}$ is the last index for which the sequence ${\textstyle \Delta [X]}$ repeats. In practice, the first few terms of the sequence usually provide desired precision; also, when numerically computing the sequence, one has to take care to stop the computation before rounding errors in the denominator become too large, as the ${\textstyle \Delta ^{2}}$ sequence transformation may cancel significant digits.

## Properties

Aitken's delta-squared process is an acceleration of convergence method and a particular case of a nonlinear sequence transformation.

A sequence ${\textstyle X=(x_{n})}$ that converges to a limiting value ${\textstyle \ell }$ is said to converge linearly, or more technically Q-linearly, if there is some number ${\textstyle \mu \in (0,1)}$ for which

$\lim _{n\to \infty }{\frac {|x_{n+1}-\ell |}{|x_{n}-\ell |}}=\mu .$

This means that asymptotically, the distance between the sequence and its limit shrinks by nearly the same proportion, $\mu ,$ on every step and the ratio of reduction becomes closer and closer to that proportion. This is also sometimes called "geometric convergence," since it is a characteristic property for geometric series, or "exponential convergence," since it is convergence like $\mu ^{n}=\exp(n\ln \mu ).$

Aitken's method will accelerate the convergence of a sequence X if $A[X]=(a_{n}),$ with terms defined above, satisfies ${\textstyle \lim _{n\to \infty }{\frac {a_{n}-\ell }{x_{n}-\ell }}=0.}$

A is not a linear operator on sequences, but it is linear with respect to addition of constant sequences: ${\textstyle A[X-C]=A[X]-C,}$ if C is any constant sequence $C=(c)$ , constant for all $n.$ This is clear from the expression of $A[X]$ in terms of the finite difference operator $\Delta .$

The new process does not in general converge quadratically, but for an iterated function sequence satisfying $x_{n+1}=f(x_{n})$ for some function f converging to a fixed point, the accelerated sequence's convergence is quadratic. In this case, the technique is known as Steffensen's method.

Empirically, the *A*-operation eliminates the "most important error term". One can check this by considering a sequence of the form $x_{n}=\ell +a^{n}+b^{n}$ , where $0<b<a<1$ : The sequence $A[X]$ will then go to the limit ${\textstyle \ell }$ like $b^{n}$ goes to zero.

Geometrically, the graph of an exponential function $f(t)$ that satisfies $f(n)=x_{n}$ , $f(n+1)=x_{n+1}$ and $f(n+2)=x_{n+2}$ has a horizontal asymptote at ${\frac {x_{n}x_{n+2}-x_{n+1}^{2}}{x_{n}-2x_{n+1}+x_{n+2}}}$ (if $x_{n}-2x_{n+1}+x_{n+2}\neq 0$ ).

One can also show that if a sequence X converges to its limit $\ell$ at a rate strictly greater than 1, $A[X]$ does not have a better rate of convergence. (In practice, one rarely has e.g. quadratic convergence which would mean over 30 (respectively 100) correct decimal places after 5 (respectively 7) iterations (starting with 1 correct digit); usually no acceleration is needed in that case.)

In practice, $A[X]$ often converges much faster to the limit than X does, as demonstrated by the example calculations below. Usually, it is much cheaper to calculate $A[X]$ (involving only calculation of differences, one multiplication and one division) than to calculate many more terms of the sequence X . Care must be taken, however, to avoid introducing errors due to insufficient precision when calculating the differences in the numerator and denominator of the expression.

## Example calculations

**Example 1**: The value of ${\sqrt {2}}\approx 1.4142136$ can be approximated by assuming an initial value for $x_{0}$ and iterating the following sequence, called Heron's method: $x_{n+1}={\frac {x_{n}+{\frac {2}{x_{n}}}}{2}}.$ Starting with $x_{0}=1:$

| n | X | *A[X]* |
|---|---|---|
| 0 | 1 | 1.4285714 |
| 1 | 1.5 | 1.4141414 |
| 2 | 1.4166667 | 1.4142136 |
| 3 | 1.4142157 | -- |
| 4 | 1.4142136 | -- |

It is worth noting here that Aitken's method does not save the cost of calculating two iterations here; computation of the first three *${\textstyle A[X]}$* values required the first five ${\textstyle X}$ values. Also, the second ${\textstyle A[X]}$ value is less accurate than the 4th ${\textstyle X}$ value, which is not surprising due to the fact that Aitken's process is best suited for sequences that converge linearly, rather than quadratically, and Heron's method for calculating square roots converges quadratically.

**Example 2**: The value of ${\frac {\pi }{4}}$ may be calculated as an infinite sum via the Leibniz formula for *π*:

${\frac {\pi }{4}}=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}\approx 0.785398$

| n | Series Terms | X = Partial Sums | *A[X]* |
|---|---|---|---|
| 0 | 1 | 1 | 0.79166667 |
| 1 | −0.33333333 | 0.66666667 | 0.78333333 |
| 2 | 0.2 | 0.86666667 | 0.78630952 |
| 3 | −0.14285714 | 0.72380952 | 0.78492063 |
| 4 | 0.11111111 | 0.83492063 | 0.78567821 |
| 5 | −9.0909091×10−2 | 0.74401154 | 0.78522034 |
| 6 | 7.6923077×10−2 | 0.82093462 | 0.78551795 |
| 7 | -6.6666667×10−2 | 0.75426795 | -- |
| 8 | 5.8823529×10−2 | 0.81309148 | -- |

In this example, Aitken's method is applied to a sublinearly converging series and accelerates convergence considerably. The convergence is still sublinear, but much faster than the original convergence: the first ${\textstyle A[X]}$ value, whose computation required the first three ${\textstyle X}$ values, is closer to the limit than the eighth ${\textstyle X}$ value.

## Example pseudocode for Aitken extrapolation

The following is an example of using the Aitken extrapolation to help find the limit of the sequence $x_{n+1}=f(x_{n})$ when given some initial $x_{0},$ where the limit of this sequence is assumed to be a fixed point f (say $\alpha =f(\alpha )$ ). For instance, if the sequence is given by ${\textstyle x_{n+1}={\frac {1}{2}}\left(x_{n}+{\frac {2}{x_{n}}}\right)}$ with starting point $x_{0}=1,$ then the function will be ${\textstyle f(x):={\frac {1}{2}}\left(x+{\frac {2}{x}}\right),}$ which has ${\displaystyle \alpha$ as a fixed point (see Methods of computing square roots); it is this fixed point whose value will be approximated.

This pseudo code also computes the Aitken approximation to $f^{\prime }(\alpha )$ . The Aitken extrapolates will be denoted by `aitkenX`. During the computation of the extrapolate, it is important to check if the denominator becomes too small, which could happen if we already have a large amount of accuracy; without this check, a large amount of error could be introduced by the division. This small number will be denoted by `epsilon`. Because the binary representation of the fixed point could be infinite (or at least too large to fit in the available memory), the calculation will stop once the approximation is within `tolerance` of the true value.

```mw
%These choices depend on the problem being solved
x0 = 1                      %The initial value
f(x) = (1/2)*(x + 2/x)      %The function that finds the next element in the sequence
tolerance = 10^-10          %10 digit accuracy is desired
epsilon = 10^-16            %Do not divide by a number smaller than this

maxIterations = 20          %Do not allow the iterations to continue indefinitely
haveWeFoundSolution = false %Were we able to find the solution to within the desired tolerance? not yet

for i = 1 : maxIterations
    x1 = f(x0)
    x2 = f(x1)

    if (x1 ~= x0)
        lambda = absoluteValue((x2 - x1)/(x1 - x0))  %OPTIONAL: Computes an approximation of |f'(fixedPoint)|, which is denoted by lambda
    end

    denominator = (x2 - x1) - (x1 - x0);

    if (absoluteValue(denominator) < epsilon)        %To avoid greatly increasing error, do not divide by too small of a number
        print('WARNING: denominator is too small')
        break                                        %Leave the loop
    end

    aitkenX = x2 - ( (x2 - x1)^2 )/denominator

    if (absoluteValue(aitkenX - x2) < tolerance)     %If the value is within tolerance
        print("The fixed point is ", aitkenX))       %Display the result of the Aitken extrapolation
        haveWeFoundSolution = true
        break                                        %Done, so leave the loop
    end

    x0 = aitkenX                                     %Update x0 to start again
end

if (haveWeFoundSolution == false)   %If we were not able to find a solution to within the desired tolerance
    print("Warning: Not able to find solution to within the desired tolerance of ", tolerance)
    print("The last computed extrapolate was ", aitkenX)
end
```
