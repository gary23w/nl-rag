---
title: "Catastrophic cancellation"
source: https://en.wikipedia.org/wiki/Catastrophic_cancellation
domain: floating-point
license: CC-BY-SA-4.0 / CC-BY-3.0 (floating-point-gui.de)
tags: floating point, ieee 754, rounding error, double precision, machine epsilon
fetched: 2026-07-02
---

# Catastrophic cancellation

In numerical analysis, **catastrophic cancellation** is the phenomenon that subtracting good approximations to two nearby numbers may yield a very bad approximation to the difference of the original numbers.

For example, if there are two studs, one $L_{1}=253.51\,{\text{cm}}$ long and the other $L_{2}=252.49\,{\text{cm}}$ long, and they are measured with a ruler that is good only to the centimeter, then the approximations could come out to be ${\tilde {L}}_{1}=254\,{\text{cm}}$ and ${\tilde {L}}_{2}=252\,{\text{cm}}$ . These may be good approximations, in relative error, to the true lengths: the approximations are in error by less than 0.2% of the true lengths, $|L_{1}-{\tilde {L}}_{1}|/|L_{1}|<0.2\%$ .

However, if the *approximate* lengths are subtracted, the difference will be ${\tilde {L}}_{1}-{\tilde {L}}_{2}=254\,{\text{cm}}-252\,{\text{cm}}=2\,{\text{cm}}$ , even though the true difference between the lengths is $L_{1}-L_{2}=253.51\,{\text{cm}}-252.49\,{\text{cm}}=1.02\,{\text{cm}}$ . The difference of the approximations, $2\,{\text{cm}}$ , is in error by almost 100% of the magnitude of the difference of the true values, $1.02\,{\text{cm}}$ .

Catastrophic cancellation is not affected by how large the inputs are—it applies just as much to large and small inputs. It depends only on how large the *difference* is, and on the *error* of the inputs. Exactly the same error would arise by subtracting $52\,{\text{cm}}$ from $54\,{\text{cm}}$ as approximations to $52.49\,{\text{cm}}$ and $53.51\,{\text{cm}}$ , or by subtracting $2.00052\,{\text{km}}$ from $2.00054\,{\text{km}}$ as approximations to $2.0005249\,{\text{km}}$ and $2.0005351\,{\text{km}}$ .

Catastrophic cancellation may happen even if the difference is computed exactly, as in the example above—it is not a property of any particular kind of arithmetic like floating-point arithmetic; rather, it is inherent to subtraction, when the *inputs* are approximations themselves. Indeed, in floating-point arithmetic, when the inputs are close enough, the floating-point difference is computed exactly, by the Sterbenz lemma—there is no rounding error introduced by the floating-point subtraction operation.

## Formal analysis

Formally, catastrophic cancellation happens because subtraction is ill-conditioned at nearby inputs: even if approximations ${\tilde {x}}=x(1+\delta _{x})$ and ${\tilde {y}}=y(1+\delta _{y})$ have small relative errors $|\delta _{x}|=|x-{\tilde {x}}|/|x|$ and $|\delta _{y}|=|y-{\tilde {y}}|/|y|$ from true values x and y , respectively, the relative error of the difference ${\tilde {x}}-{\tilde {y}}$ of the approximations from the difference $x-y$ of the true values is inversely proportional to the difference of the true values:

${\begin{aligned}{\tilde {x}}-{\tilde {y}}&=x(1+\delta _{x})-y(1+\delta _{y})=x-y+x\delta _{x}-y\delta _{y}\\&=x-y+(x-y){\frac {x\delta _{x}-y\delta _{y}}{x-y}}\\&=(x-y){\biggr (}1+{\frac {x\delta _{x}-y\delta _{y}}{x-y}}{\biggr )}.\end{aligned}}$

Thus, the relative error of the exact difference ${\tilde {x}}-{\tilde {y}}$ of the approximations from the difference $x-y$ of the true values is

$\left|{\frac {x\delta _{x}-y\delta _{y}}{x-y}}\right|.$

which can be arbitrarily large if the true values x and y are close.

## In numerical algorithms

Subtracting nearby numbers in floating-point arithmetic does not always cause catastrophic cancellation, or even any error—by the Sterbenz lemma, if the numbers are close enough the floating-point difference is exact. But cancellation may *amplify* errors in the inputs that arose from rounding in other floating-point arithmetic.

### Example: Difference of squares

Given numbers x and y , the naive attempt to compute the mathematical function $x^{2}-y^{2}$ by the floating-point arithmetic $\operatorname {fl} (\operatorname {fl} (x^{2})-\operatorname {fl} (y^{2}))$ is subject to catastrophic cancellation when x and y are close in magnitude, because the subtraction can expose the rounding errors in the squaring. The alternative factoring $(x+y)(x-y)$ , evaluated by the floating-point arithmetic $\operatorname {fl} (\operatorname {fl} (x+y)\cdot \operatorname {fl} (x-y))$ , avoids catastrophic cancellation because it avoids introducing rounding error leading into the subtraction.

For example, if $x=1+2^{-29}\approx 1.0000000018626451$ and $y=1+2^{-30}\approx 1.0000000009313226$ , then the true value of the difference $x^{2}-y^{2}$ is $2^{-29}\cdot (1+2^{-30}+2^{-31})\approx 1.8626451518330422\times 10^{-9}$ . In IEEE 754 binary64 arithmetic, evaluating the alternative factoring $(x+y)(x-y)$ gives the correct result exactly (with no rounding), but evaluating the naive expression $x^{2}-y^{2}$ gives the floating-point number $2^{-29}=1.8626451{\underline {4923095703125}}\times 10^{-9}$ , of which less than half the digits are correct and the other (underlined) digits reflect the missing terms $2^{-59}+2^{-60}$ , lost due to rounding when calculating the intermediate squared values.

### Example: Complex arcsine

When computing the complex arcsine function, one may be tempted to use the logarithmic formula directly:

$\arcsin(z)=i\log {\bigl (}{\sqrt {1-z^{2}}}-iz{\bigr )}.$

However, suppose $z=iy$ for $y\ll -1$ . Then ${\sqrt {1-z^{2}}}\approx -y$ and $iz=-y$ ; call the difference between them $\varepsilon$ —a very small difference, nearly zero. If ${\sqrt {1-z^{2}}}$ is evaluated in floating-point arithmetic giving

$\operatorname {fl} {\Bigl (}{\sqrt {\operatorname {fl} (1-\operatorname {fl} (z^{2}))}}{\Bigr )}={\sqrt {1-z^{2}}}(1+\delta )$

with any error $\delta \neq 0$ , where $\operatorname {fl} (\cdots )$ denotes floating-point rounding, then computing the difference

${\sqrt {1-z^{2}}}(1+\delta )-iz$

of two nearby numbers, both very close to $-y$ , may amplify the error $\delta$ in one input by a factor of $1/\varepsilon$ —a very large factor because $\varepsilon$ was nearly zero. This may make the final error very large even if the error $\delta$ in computing ${\sqrt {1-z^{2}}}$ is very small.

For instance, let $z=-1234567i$ . The true value of $\arcsin(z)$ is approximately $-14.71937803983977i$ . But using the naive logarithmic formula in IEEE 754 binary64 arithmetic—which computes $1-z^{2}$ exactly, and incurs only a single rounding error of $|\delta |<2^{-53}$ in ${\sqrt {1-z^{2}}}$ —may give the floating-point number nearest to $-14.719{\underline {644263563968}}i$ , with only five out of sixteen digits correct and the remainder (underlined) all incorrect.

In the above case of $z=iy$ for $y\ll -1$ , using the identity $\arcsin(z)=-\arcsin(-z)$ avoids cancellation because ${\textstyle {\sqrt {1-(-z)^{2}}}={\sqrt {1-z^{2}}}\approx -y}$ but $i(-z)=-iz=y$ , so the subtraction is effectively addition with the same sign which does not cancel.

### Example: Radix conversion

Numerical constants in software programs are often written in decimal, such as in the C fragment `double x = 1.000000000000001;` to declare and initialize an IEEE 754 binary64 variable named `x`. However, $1.000000000000001$ is not a binary64 floating-point number; the nearest one, which `x` will be initialized to in this fragment, is $1.0000000000000011102230246251565404236316680908203125=1+5\cdot 2^{-52}$ . Although the radix conversion from decimal floating-point to binary floating-point only incurs a small relative error, catastrophic cancellation may amplify it into a much larger one:

```mw
double x = 1.000000000000001;  // rounded to 1 + 5*2^{-52}
double y = 1.000000000000002;  // rounded to 1 + 9*2^{-52}
double z = y - x;              // difference is exactly 4*2^{-52}
```

The difference $1.000000000000002-1.000000000000001$ is $0.000000000000001=1.0\times 10^{-15}$ . The relative errors of `x` from $1.000000000000001$ and of `y` from $1.000000000000002$ are both below $10^{-15}=0.0000000000001\%$ , and the floating-point subtraction `y - x` is computed exactly by the Sterbenz lemma.

But even though the inputs are good approximations, and even though the subtraction is computed exactly, the difference of the *approximations* ${\tilde {y}}-{\tilde {x}}=(1+9\cdot 2^{-52})-(1+5\cdot 2^{-52})=4\cdot 2^{-52}\approx 8.88\times 10^{-16}$ has a relative error of over $11\%$ from the difference $1.0\times 10^{-15}$ of the original values as written in decimal: catastrophic cancellation amplified a tiny error in radix conversion into a large error in the output.

### Benign cancellation

Cancellation is sometimes useful and desirable in numerical algorithms. For example, the 2Sum and Fast2Sum algorithms both rely on such cancellation after a rounding error in order to exactly compute what the error was in a floating-point addition operation as a floating-point number itself.

The function $\log(1+x)$ , if evaluated naively at points $0<x\lll 1$ , will lose most of the digits of x in rounding $\operatorname {fl} (1+x)$ . However, the function $\log(1+x)$ itself is well-conditioned at inputs near 0 . Rewriting it as $\log(1+x)=x{\frac {\log(1+x)}{(1+x)-1}}$ exploits cancellation in ${\hat {x}}:=\operatorname {fl} (1+x)-1$ to avoid the error from $\log(1+x)$ evaluated directly. This works because the cancellation in the numerator $\log(\operatorname {fl} (1+x))={\hat {x}}+O({\hat {x}}^{2})$ and the cancellation in the denominator ${\hat {x}}=\operatorname {fl} (1+x)-1$ counteract each other; the function $\mu (\xi )=\log(1+\xi )/\xi$ is well-enough conditioned near zero that $\mu ({\hat {x}})$ gives a good approximation to $\mu (x)$ , and thus $x\cdot \mu ({\hat {x}})$ gives a good approximation to $x\cdot \mu (x)=\log(1+x)$ .
