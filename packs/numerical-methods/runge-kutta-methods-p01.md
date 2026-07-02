---
title: "Runge–Kutta methods (part 1/2)"
source: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
part: 1/2
---

# Runge–Kutta methods

In numerical analysis, the **Runge–Kutta methods** (English: /ˈrʊŋəˈkʊtɑː/ ⓘ *RUUNG-ə-KUUT-tah*) are a family of implicit and explicit iterative methods, which include the Euler method, used in temporal discretization for the approximate solutions of simultaneous nonlinear equations. These methods were developed around 1900 by the German mathematicians Carl Runge and Wilhelm Kutta.


## The Runge–Kutta method

The most widely known member of the Runge–Kutta family is generally referred to as "RK4", the "classic Runge–Kutta method" or simply as "the Runge–Kutta method".

Let an initial value problem be specified as follows:

d

y

d

t

=

f

(

t

,

y

)

,

y

(

t

0

)

=

y

0

.

{\displaystyle {\frac {dy}{dt}}=f(t,y),\quad y(t_{0})=y_{0}.}

Here y {\displaystyle y} ({\displaystyle y}) is an unknown function (scalar or vector) of time t {\displaystyle t} ({\displaystyle t}), which we would like to approximate; we are told that d y d t {\displaystyle {\frac {dy}{dt}}} ({\displaystyle {\frac {dy}{dt}}}), the rate at which y {\displaystyle y} ({\displaystyle y}) changes, is a function of t {\displaystyle t} ({\displaystyle t}) and of y {\displaystyle y} ({\displaystyle y}) itself. At the initial time t 0 {\displaystyle t_{0}} ({\displaystyle t_{0}}) the corresponding y {\displaystyle y} ({\displaystyle y}) value is y 0 {\displaystyle y_{0}} ({\displaystyle y_{0}}). The function f {\displaystyle f} ({\displaystyle f}) and the initial conditions t 0 {\displaystyle t_{0}} ({\displaystyle t_{0}}), y 0 {\displaystyle y_{0}} ({\displaystyle y_{0}}) are given.

Now we pick a step-size *h* > 0 and define:

y

n

+

1

=

y

n

+

h

6

(

k

1

+

2

k

2

+

2

k

3

+

k

4

)

,

t

n

+

1

=

t

n

+

h

{\displaystyle {\begin{aligned}y_{n+1}&=y_{n}+{\frac {h}{6}}\left(k_{1}+2k_{2}+2k_{3}+k_{4}\right),\\t_{n+1}&=t_{n}+h\\\end{aligned}}}

for *n* = 0, 1, 2, 3, ..., using

k

1

=

f

(

t

n

,

y

n

)

,

k

2

=

f

(

t

n

+

h

2

,

y

n

+

k

1

h

2

)

,

k

3

=

f

(

t

n

+

h

2

,

y

n

+

k

2

h

2

)

,

k

4

=

f

(

t

n

+

h

,

y

n

+

h

k

3

)

.

{\displaystyle {\begin{aligned}k_{1}&=\ f(t_{n},y_{n}),\\k_{2}&=\ f\!\left(t_{n}+{\frac {h}{2}},y_{n}+k_{1}{\frac {h}{2}}\right),\\k_{3}&=\ f\!\left(t_{n}+{\frac {h}{2}},y_{n}+k_{2}{\frac {h}{2}}\right),\\k_{4}&=\ f\!\left(t_{n}+h,y_{n}+hk_{3}\right).\end{aligned}}}

(*Note: the above equations have different but equivalent definitions in different texts.*)

Here y n + 1 {\displaystyle y_{n+1}} ({\displaystyle y_{n+1}}) is the RK4 approximation of y ( t n + 1 ) {\displaystyle y(t_{n+1})} ({\displaystyle y(t_{n+1})}), and the next value ( y n + 1 {\displaystyle y_{n+1}} ({\displaystyle y_{n+1}})) is determined by the present value ( y n {\displaystyle y_{n}} ({\displaystyle y_{n}})) plus the weighted average of four increments, where each increment is the product of the size of the interval, *h*, and an estimated slope specified by function *f* on the right-hand side of the differential equation.

- k 1 {\displaystyle k_{1}} ({\displaystyle k_{1}}) is the slope at the beginning of the interval, using y {\displaystyle y} ({\displaystyle y}) (Euler's method);
- k 2 {\displaystyle k_{2}} ({\displaystyle k_{2}}) is the slope at the midpoint of the interval, using y {\displaystyle y} ({\displaystyle y}) and k 1 {\displaystyle k_{1}} ({\displaystyle k_{1}});
- k 3 {\displaystyle k_{3}} ({\displaystyle k_{3}}) is again the slope at the midpoint, but now using y {\displaystyle y} ({\displaystyle y}) and k 2 {\displaystyle k_{2}} ({\displaystyle k_{2}});
- k 4 {\displaystyle k_{4}} ({\displaystyle k_{4}}) is the slope at the end of the interval, using y {\displaystyle y} ({\displaystyle y}) and k 3 {\displaystyle k_{3}} ({\displaystyle k_{3}}).

In averaging the four slopes, greater weight is given to the slopes at the midpoint. If f {\displaystyle f} ({\displaystyle f}) is independent of y {\displaystyle y} ({\displaystyle y}), so that the differential equation is equivalent to a simple integral, then RK4 is Simpson's rule.

The RK4 method is a fourth-order method, meaning that the local truncation error is on the order of O ( h 5 ) {\displaystyle O(h^{5})} ({\displaystyle O(h^{5})}), while the total accumulated error is on the order of O ( h 4 ) {\displaystyle O(h^{4})} ({\displaystyle O(h^{4})}).

In many practical applications the function f {\displaystyle f} ({\displaystyle f}) is independent of t {\displaystyle t} ({\displaystyle t}) (so called autonomous system, or time-invariant system, especially in physics), and their increments are not computed at all and not passed to function f {\displaystyle f} ({\displaystyle f}), with only the final formula for t n + 1 {\displaystyle t_{n+1}} ({\displaystyle t_{n+1}}) used.


## Explicit Runge–Kutta methods

The family of explicit Runge–Kutta methods is a generalization of the RK4 method mentioned above. It is given by

y

n

+

1

=

y

n

+

h

∑

i

=

1

s

b

i

k

i

,

{\displaystyle y_{n+1}=y_{n}+h\sum _{i=1}^{s}b_{i}k_{i},}

where

k

1

=

f

(

t

n

,

y

n

)

,

k

2

=

f

(

t

n

+

c

2

h

,

y

n

+

(

a

21

k

1

)

h

)

,

k

3

=

f

(

t

n

+

c

3

h

,

y

n

+

(

a

31

k

1

+

a

32

k

2

)

h

)

,

⋮

k

s

=

f

(

t

n

+

c

s

h

,

y

n

+

(

a

s

1

k

1

+

a

s

2

k

2

+

⋯

+

a

s

,

s

−

1

k

s

−

1

)

h

)

.

{\displaystyle {\begin{aligned}k_{1}&=f(t_{n},y_{n}),\\k_{2}&=f(t_{n}+c_{2}h,y_{n}+(a_{21}k_{1})h),\\k_{3}&=f(t_{n}+c_{3}h,y_{n}+(a_{31}k_{1}+a_{32}k_{2})h),\\&\ \ \vdots \\k_{s}&=f(t_{n}+c_{s}h,y_{n}+(a_{s1}k_{1}+a_{s2}k_{2}+\cdots +a_{s,s-1}k_{s-1})h).\end{aligned}}}

(

Note: the above equations may have different but equivalent definitions in some texts.

)

To specify a particular method, one needs to provide the integer *s* (the number of stages), and the coefficients *aij* (for 1 ≤ *j* < *i* ≤ *s*), *bi* (for *i* = 1, 2, ..., *s*) and *ci* (for *i* = 2, 3, ..., *s*). The matrix [*aij*] is called the *Runge–Kutta matrix*, while the *bi* and *ci* are known as the *weights* and the *nodes*. These data are usually arranged in a mnemonic device, known as a *Butcher tableau* (after John C. Butcher):

| 0 {\displaystyle 0} ({\displaystyle 0}) |   |   |   |   |   |
|---|---|---|---|---|---|
| c 2 {\displaystyle c_{2}} ({\displaystyle c_{2}}) | a 21 {\displaystyle a_{21}} ({\displaystyle a_{21}}) |   |   |   |   |
| c 3 {\displaystyle c_{3}} ({\displaystyle c_{3}}) | a 31 {\displaystyle a_{31}} ({\displaystyle a_{31}}) | a 32 {\displaystyle a_{32}} ({\displaystyle a_{32}}) |   |   |   |
| ⋮ {\displaystyle \vdots } ({\displaystyle \vdots }) | ⋮ {\displaystyle \vdots } ({\displaystyle \vdots }) |   | ⋱ {\displaystyle \ddots } ({\displaystyle \ddots }) |   |   |
| c s {\displaystyle c_{s}} ({\displaystyle c_{s}}) | a s 1 {\displaystyle a_{s1}} ({\displaystyle a_{s1}}) | a s 2 {\displaystyle a_{s2}} ({\displaystyle a_{s2}}) | ⋯ {\displaystyle \cdots } ({\displaystyle \cdots }) | a s , s − 1 {\displaystyle a_{s,s-1}} ({\displaystyle a_{s,s-1}}) |   |
|   | b 1 {\displaystyle b_{1}} ({\displaystyle b_{1}}) | b 2 {\displaystyle b_{2}} ({\displaystyle b_{2}}) | ⋯ {\displaystyle \cdots } ({\displaystyle \cdots }) | b s − 1 {\displaystyle b_{s-1}} ({\displaystyle b_{s-1}}) | b s {\displaystyle b_{s}} ({\displaystyle b_{s}}) |

A Taylor series expansion shows that the Runge–Kutta method is consistent if and only if

∑

i

=

1

s

b

i

=

1.

{\displaystyle \sum _{i=1}^{s}b_{i}=1.}

There are also accompanying requirements if one requires the method to have a certain order *p*, meaning that the local truncation error is O(*hp*+1). These can be derived from the definition of the truncation error itself. For example, a two-stage method has order 2 if *b*1 + *b*2 = 1, *b*2*c*2 = 1/2, and *b*2*a*21 = 1/2. Note that a popular condition for determining coefficients is

∑

j

=

1

i

−

1

a

i

j

=

c

i

for

i

=

2

,

…

,

s

.

{\displaystyle \sum _{j=1}^{i-1}a_{ij}=c_{i}{\text{ for }}i=2,\ldots ,s.}

This condition alone, however, is neither sufficient, nor necessary for consistency.

In general, if an explicit s {\displaystyle s} ({\displaystyle s})-stage Runge–Kutta method has order p {\displaystyle p} ({\displaystyle p}), then it can be proven that the number of stages must satisfy s ≥ p {\displaystyle s\geq p} ({\displaystyle s\geq p}) and if p ≥ 5 {\displaystyle p\geq 5} ({\displaystyle p\geq 5}), then s ≥ p + 1 {\displaystyle s\geq p+1} ({\displaystyle s\geq p+1}). However, it is not known whether these bounds are *sharp* in all cases. In some cases, it is proven that the bound cannot be achieved. For instance, Butcher proved that for p > 6 {\displaystyle p>6} ({\displaystyle p>6}), there is no explicit method with s = p + 1 {\displaystyle s=p+1} ({\displaystyle s=p+1}) stages. Butcher also proved that for p > 7 {\displaystyle p>7} ({\displaystyle p>7}), there is no explicit Runge-Kutta method with p + 2 {\displaystyle p+2} ({\displaystyle p+2}) stages. In general, however, it remains an open problem what the precise minimum number of stages s {\displaystyle s} ({\displaystyle s}) is for an explicit Runge–Kutta method to have order p {\displaystyle p} ({\displaystyle p}). Some values which are known are:

p

1

2

3

4

5

6

7

8

min

s

1

2

3

4

6

7

9

11

{\displaystyle {\begin{array}{c|cccccccc}p&1&2&3&4&5&6&7&8\\\hline \min s&1&2&3&4&6&7&9&11\end{array}}}

The provable bound above then implies that we cannot find methods of orders p = 1 , 2 , … , 6 {\displaystyle p=1,2,\ldots ,6} ({\displaystyle p=1,2,\ldots ,6}) that require fewer stages than the methods we already know for these orders. The work of Butcher also proves that 7th and 8th order methods have a minimum of 9 and 11 stages, respectively. An example of an explicit method of order 6 with 7 stages can be found in Ref. Explicit methods of order 7 with 9 stages and explicit methods of order 8 with 11 stages are also known. See Refs. for a summary.

### Examples

The RK4 method falls in this framework. Its tableau is

| 0 |   |   |   |   |
|---|---|---|---|---|
| 1/2 | 1/2 |   |   |   |
| 1/2 | 0 | 1/2 |   |   |
| 1 | 0 | 0 | 1 |   |
|   | 1/6 | 1/3 | 1/3 | 1/6 |

A slight variation of "the" Runge–Kutta method is also due to Kutta in 1901 and is called the 3/8-rule. The primary advantage this method has is that almost all of the error coefficients are smaller than in the popular method, but it requires slightly more floating-point operations per time step. Its Butcher tableau is

| 0 |   |   |   |   |
|---|---|---|---|---|
| 1/3 | 1/3 |   |   |   |
| 2/3 | −1/3 | 1 |   |   |
| 1 | 1 | −1 | 1 |   |
|   | 1/8 | 3/8 | 3/8 | 1/8 |

However, the simplest Runge–Kutta method is the (forward) Euler method, given by the formula y n + 1 = y n + h f ( t n , y n ) {\displaystyle y_{n+1}=y_{n}+hf(t_{n},y_{n})} ({\displaystyle y_{n+1}=y_{n}+hf(t_{n},y_{n})}). This is the only consistent explicit Runge–Kutta method with one stage. The corresponding tableau is

| 0 |   |
|---|---|
|   | 1 |

### Second-order methods with two stages

An example of a second-order method with two stages is provided by the explicit midpoint method:

y

n

+

1

=

y

n

+

h

f

(

t

n

+

1

2

h

,

y

n

+

1

2

h

f

(

t

n

,

y

n

)

)

.

{\displaystyle y_{n+1}=y_{n}+hf\left(t_{n}+{\frac {1}{2}}h,y_{n}+{\frac {1}{2}}hf(t_{n},\ y_{n})\right).}

The corresponding tableau is

| 0 |   |   |
|---|---|---|
| 1/2 | 1/2 |   |
|   | 0 | 1 |

The midpoint method is not the only second-order Runge–Kutta method with two stages; there is a family of such methods, parameterized by α and given by the formula

y

n

+

1

=

y

n

+

h

(

(

1

−

1

2

α

)

f

(

t

n

,

y

n

)

+

1

2

α

f

(

t

n

+

α

h

,

y

n

+

α

h

f

(

t

n

,

y

n

)

)

)

.

{\displaystyle y_{n+1}=y_{n}+h{\bigl (}(1-{\tfrac {1}{2\alpha }})f(t_{n},y_{n})+{\tfrac {1}{2\alpha }}f(t_{n}+\alpha h,y_{n}+\alpha hf(t_{n},y_{n})){\bigr )}.}

Its Butcher tableau is

| 0 |   |   |
|---|---|---|
| α {\displaystyle \alpha } ({\displaystyle \alpha }) | α {\displaystyle \alpha } ({\displaystyle \alpha }) |   |
|   | ( 1 − 1 2 α ) {\displaystyle (1-{\tfrac {1}{2\alpha }})} ({\displaystyle (1-{\tfrac {1}{2\alpha }})}) | 1 2 α {\displaystyle {\tfrac {1}{2\alpha }}} ({\displaystyle {\tfrac {1}{2\alpha }}}) |

In this family, α = 1 2 {\displaystyle \alpha ={\tfrac {1}{2}}} ({\displaystyle \alpha ={\tfrac {1}{2}}}) gives the midpoint method, α = 1 {\displaystyle \alpha =1} ({\displaystyle \alpha =1}) is Heun's method, and α = 2 3 {\displaystyle \alpha ={\tfrac {2}{3}}} ({\displaystyle \alpha ={\tfrac {2}{3}}}) is Ralston's method.


## Use

As an example, consider the two-stage second-order Runge–Kutta method with α = 2/3, also known as Ralston method. It is given by the tableau

|   | 0 |   |   |
|---|---|---|---|
|   | 2/3 | 2/3 |   |
|   |   | 1/4 | 3/4 |

with the corresponding equations

k

1

=

f

(

t

n

,

y

n

)

,

k

2

=

f

(

t

n

+

2

3

h

,

y

n

+

2

3

h

k

1

)

,

y

n

+

1

=

y

n

+

h

(

1

4

k

1

+

3

4

k

2

)

.

{\displaystyle {\begin{aligned}k_{1}&=f(t_{n},\ y_{n}),\\k_{2}&=f(t_{n}+{\tfrac {2}{3}}h,\ y_{n}+{\tfrac {2}{3}}hk_{1}),\\y_{n+1}&=y_{n}+h\left({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2}\right).\end{aligned}}}

This method is used to solve the initial-value problem

d

y

d

t

=

tan

⁡

(

y

)

+

1

,

y

0

=

1

,

t

∈

[

1

,

1.1

]

{\displaystyle {\frac {dy}{dt}}=\tan(y)+1,\quad y_{0}=1,\ t\in [1,1.1]}

with step size *h* = 0.025, so the method needs to take four steps.

The method proceeds as follows:

| t 0 = 1 : {\displaystyle t_{0}=1\colon } ({\displaystyle t_{0}=1\colon }) |   |   |   |
|---|---|---|---|
|   | y 0 = 1 {\displaystyle y_{0}=1} ({\displaystyle y_{0}=1}) |   |   |
| t 1 = 1.025 : {\displaystyle t_{1}=1.025\colon } ({\displaystyle t_{1}=1.025\colon }) |   |   |   |
|   | y 0 = 1 {\displaystyle y_{0}=1} ({\displaystyle y_{0}=1}) | k 1 = 2.557407725 {\displaystyle k_{1}=2.557407725} ({\displaystyle k_{1}=2.557407725}) | k 2 = f ( t 0 + 2 3 h ,   y 0 + 2 3 h k 1 ) = 2.7138981400 {\displaystyle k_{2}=f(t_{0}+{\tfrac {2}{3}}h,\ y_{0}+{\tfrac {2}{3}}hk_{1})=2.7138981400} ({\displaystyle k_{2}=f(t_{0}+{\tfrac {2}{3}}h,\ y_{0}+{\tfrac {2}{3}}hk_{1})=2.7138981400}) |
|   | y 1 = y 0 + h ( 1 4 k 1 + 3 4 k 2 ) = 1.066869388 _ {\displaystyle y_{1}=y_{0}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.066869388}}} ({\displaystyle y_{1}=y_{0}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.066869388}}}) |   |   |
| t 2 = 1.05 : {\displaystyle t_{2}=1.05\colon } ({\displaystyle t_{2}=1.05\colon }) |   |   |   |
|   | y 1 = 1.066869388 {\displaystyle y_{1}=1.066869388} ({\displaystyle y_{1}=1.066869388}) | k 1 = 2.813524695 {\displaystyle k_{1}=2.813524695} ({\displaystyle k_{1}=2.813524695}) | k 2 = f ( t 1 + 2 3 h ,   y 1 + 2 3 h k 1 ) {\displaystyle k_{2}=f(t_{1}+{\tfrac {2}{3}}h,\ y_{1}+{\tfrac {2}{3}}hk_{1})} ({\displaystyle k_{2}=f(t_{1}+{\tfrac {2}{3}}h,\ y_{1}+{\tfrac {2}{3}}hk_{1})}) |
|   | y 2 = y 1 + h ( 1 4 k 1 + 3 4 k 2 ) = 1.141332181 _ {\displaystyle y_{2}=y_{1}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.141332181}}} ({\displaystyle y_{2}=y_{1}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.141332181}}}) |   |   |
| t 3 = 1.075 : {\displaystyle t_{3}=1.075\colon } ({\displaystyle t_{3}=1.075\colon }) |   |   |   |
|   | y 2 = 1.141332181 {\displaystyle y_{2}=1.141332181} ({\displaystyle y_{2}=1.141332181}) | k 1 = 3.183536647 {\displaystyle k_{1}=3.183536647} ({\displaystyle k_{1}=3.183536647}) | k 2 = f ( t 2 + 2 3 h ,   y 2 + 2 3 h k 1 ) {\displaystyle k_{2}=f(t_{2}+{\tfrac {2}{3}}h,\ y_{2}+{\tfrac {2}{3}}hk_{1})} ({\displaystyle k_{2}=f(t_{2}+{\tfrac {2}{3}}h,\ y_{2}+{\tfrac {2}{3}}hk_{1})}) |
|   | y 3 = y 2 + h ( 1 4 k 1 + 3 4 k 2 ) = 1.227417567 _ {\displaystyle y_{3}=y_{2}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.227417567}}} ({\displaystyle y_{3}=y_{2}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.227417567}}}) |   |   |
| t 4 = 1.1 : {\displaystyle t_{4}=1.1\colon } ({\displaystyle t_{4}=1.1\colon }) |   |   |   |
|   | y 3 = 1.227417567 {\displaystyle y_{3}=1.227417567} ({\displaystyle y_{3}=1.227417567}) | k 1 = 3.796866512 {\displaystyle k_{1}=3.796866512} ({\displaystyle k_{1}=3.796866512}) | k 2 = f ( t 3 + 2 3 h ,   y 3 + 2 3 h k 1 ) {\displaystyle k_{2}=f(t_{3}+{\tfrac {2}{3}}h,\ y_{3}+{\tfrac {2}{3}}hk_{1})} ({\displaystyle k_{2}=f(t_{3}+{\tfrac {2}{3}}h,\ y_{3}+{\tfrac {2}{3}}hk_{1})}) |
|   | y 4 = y 3 + h ( 1 4 k 1 + 3 4 k 2 ) = 1.335079087 _ . {\displaystyle y_{4}=y_{3}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.335079087}}.} ({\displaystyle y_{4}=y_{3}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.335079087}}.}) |   |   |

The numerical solutions correspond to the underlined values.


## Implicit Runge–Kutta methods

Explicit Runge–Kutta methods are generally unsuitable for the solution of stiff equations because their region of absolute stability is small; in particular, it is bounded. This issue is especially important in the solution of partial differential equations.

The instability of explicit Runge–Kutta methods motivates the development of implicit methods. An implicit Runge–Kutta method has the form

y

n

+

1

=

y

n

+

h

∑

i

=

1

s

b

i

k

i

,

{\displaystyle y_{n+1}=y_{n}+h\sum _{i=1}^{s}b_{i}k_{i},}

where

k

i

=

f

(

t

n

+

c

i

h

,

y

n

+

h

∑

j

=

1

s

a

i

j

k

j

)

,

i

=

1

,

…

,

s

.

{\displaystyle k_{i}=f\left(t_{n}+c_{i}h,\ y_{n}+h\sum _{j=1}^{s}a_{ij}k_{j}\right),\quad i=1,\ldots ,s.}

The difference with an explicit method is that in an explicit method, the sum over *j* only goes up to *i* − 1. This also shows up in the Butcher tableau: the coefficient matrix a i j {\displaystyle a_{ij}} ({\displaystyle a_{ij}}) of an explicit method is lower triangular. In an implicit method, the sum over *j* goes up to *s* and the coefficient matrix is not strictly triangular, yielding a Butcher tableau of the form

c

1

a

11

a

12

…

a

1

s

c

2

a

21

a

22

…

a

2

s

⋮

⋮

⋮

⋱

⋮

c

s

a

s

1

a

s

2

…

a

s

s

b

1

b

2

…

b

s

=

c

A

b

T

{\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &A\\\hline &\mathbf {b^{T}} \\\end{array}}}

The consequence of this difference is that at every step, a system of algebraic equations has to be solved. This increases the computational cost considerably. If a method with *s* stages is used to solve a differential equation with *m* components, then the system of algebraic equations has *ms* components. This can be contrasted with implicit linear multistep methods (the other big family of methods for ODEs): an implicit *s*-step linear multistep method needs to solve a system of algebraic equations with only *m* components, so the size of the system does not increase as the number of steps increases.

### Examples

The simplest example of an implicit Runge–Kutta method is the backward Euler method:

y

n

+

1

=

y

n

+

h

f

(

t

n

+

h

,

y

n

+

1

)

.

{\displaystyle y_{n+1}=y_{n}+hf(t_{n}+h,\ y_{n+1}).\,}

The Butcher tableau for this is simply:

1

1

1

{\displaystyle {\begin{array}{c|c}1&1\\\hline &1\\\end{array}}}

This Butcher tableau corresponds to the formulae

k

1

=

f

(

t

n

+

h

,

y

n

+

h

k

1

)

and

y

n

+

1

=

y

n

+

h

k

1

,

{\displaystyle k_{1}=f(t_{n}+h,\ y_{n}+hk_{1})\quad {\text{and}}\quad y_{n+1}=y_{n}+hk_{1},}

which can be re-arranged to get the formula for the backward Euler method listed above.

Another example for an implicit Runge–Kutta method is the trapezoidal rule. Its Butcher tableau is:

0

0

0

1

1

2

1

2

1

2

1

2

1

0

{\displaystyle {\begin{array}{c|cc}0&0&0\\1&{\frac {1}{2}}&{\frac {1}{2}}\\\hline &{\frac {1}{2}}&{\frac {1}{2}}\\&1&0\\\end{array}}}

The trapezoidal rule is a collocation method (as discussed in that article). All collocation methods are implicit Runge–Kutta methods, but not all implicit Runge–Kutta methods are collocation methods.

The Gauss–Legendre methods form a family of collocation methods based on Gauss quadrature. A Gauss–Legendre method with *s* stages has order 2*s* (thus, methods with arbitrarily high order can be constructed). The method with two stages (and thus order four) has Butcher tableau:

1

2

−

1

6

3

1

4

1

4

−

1

6

3

1

2

+

1

6

3

1

4

+

1

6

3

1

4

1

2

1

2

1

2

+

1

2

3

1

2

−

1

2

3

{\displaystyle {\begin{array}{c|cc}{\frac {1}{2}}-{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}&{\frac {1}{4}}-{\frac {1}{6}}{\sqrt {3}}\\{\frac {1}{2}}+{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}+{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}\\\hline &{\frac {1}{2}}&{\frac {1}{2}}\\&{\frac {1}{2}}+{\frac {1}{2}}{\sqrt {3}}&{\frac {1}{2}}-{\frac {1}{2}}{\sqrt {3}}\end{array}}}

### Stability

The advantage of implicit Runge–Kutta methods over explicit ones is their greater stability, especially when applied to stiff equations. Consider the linear test equation y ′ = λ y {\displaystyle y'=\lambda y} ({\displaystyle y'=\lambda y}). A Runge–Kutta method applied to this equation reduces to the iteration y n + 1 = r ( h λ ) y n {\displaystyle y_{n+1}=r(h\lambda )\,y_{n}} ({\displaystyle y_{n+1}=r(h\lambda )\,y_{n}}), with *r* given by

r

(

z

)

=

1

+

z

b

T

(

I

−

z

A

)

−

1

e

=

det

(

I

−

z

A

+

z

e

b

T

)

det

(

I

−

z

A

)

,

{\displaystyle r(z)=1+zb^{T}(I-zA)^{-1}e={\frac {\det(I-zA+zeb^{T})}{\det(I-zA)}},}

where *e* stands for the vector of ones. The function *r* is called the *stability function*. It follows from the formula that *r* is the quotient of two polynomials of degree *s* if the method has *s* stages. Explicit methods have a strictly lower triangular matrix *A*, which implies that det(*I* − *zA*) = 1 and that the stability function is a polynomial.

The numerical solution to the linear test equation decays to zero if | *r*(*z*) | < 1 with *z* = *h*λ. The set of such *z* is called the *domain of absolute stability*. In particular, the method is said to be absolute stable if all *z* with Re(*z*) < 0 are in the domain of absolute stability. The stability function of an explicit Runge–Kutta method is a polynomial, so explicit Runge–Kutta methods can never be A-stable.

If the method has order *p*, then the stability function satisfies r ( z ) = e z + O ( z p + 1 ) {\displaystyle r(z)={\textrm {e}}^{z}+O(z^{p+1})} ({\displaystyle r(z)={\textrm {e}}^{z}+O(z^{p+1})}) as z → 0 {\displaystyle z\to 0} ({\displaystyle z\to 0}). Thus, it is of interest to study quotients of polynomials of given degrees that approximate the exponential function the best. These are known as Padé approximants. A Padé approximant with numerator of degree *m* and denominator of degree *n* is A-stable if and only if *m* ≤ *n* ≤ *m* + 2.

The Gauss–Legendre method with *s* stages has order 2*s*, so its stability function is the Padé approximant with *m* = *n* = *s*. It follows that the method is A-stable. This shows that A-stable Runge–Kutta can have arbitrarily high order. In contrast, the order of A-stable linear multistep methods cannot exceed two.


## Adaptive Runge–Kutta methods

Adaptive methods are designed to produce an estimate of the local truncation error of a single Runge–Kutta step. This is done by having two methods, one with order p {\displaystyle p} ({\displaystyle p}) and one with order p − 1 {\displaystyle p-1} ({\displaystyle p-1}). These methods are interwoven, i.e., they have common intermediate steps. Thanks to this, estimating the error has little or negligible computational cost compared to a step with the higher-order method.

During the integration, the step size is adapted such that the estimated error stays below a user-defined threshold: If the error is too high, a step is repeated with a lower step size; if the error is much smaller, the step size is increased to save time. This results in an (almost), optimal step size, which saves computation time. Moreover, the user does not have to spend time on finding an appropriate step size.

The lower-order step is given by

y

n

+

1

∗

=

y

n

+

h

∑

i

=

1

s

b

i

∗

k

i

,

{\displaystyle y_{n+1}^{*}=y_{n}+h\sum _{i=1}^{s}b_{i}^{*}k_{i},}

where k i {\displaystyle k_{i}} ({\displaystyle k_{i}}) are the same as for the higher-order method. Then the error is

e

n

+

1

=

y

n

+

1

−

y

n

+

1

∗

=

h

∑

i

=

1

s

(

b

i

−

b

i

∗

)

k

i

,

{\displaystyle e_{n+1}=y_{n+1}-y_{n+1}^{*}=h\sum _{i=1}^{s}(b_{i}-b_{i}^{*})k_{i},}

which is O ( h p ) {\displaystyle O(h^{p})} ({\displaystyle O(h^{p})}). The Butcher tableau for this kind of method is extended to give the values of b i ∗ {\displaystyle b_{i}^{*}} ({\displaystyle b_{i}^{*}}):

c 1 a 11 a 12 … a 1 s c 2 a 21 a 22 … a 2 s ⋮ ⋮ ⋮ ⋱ ⋮ c s a s 1 a s 2 … a s s b 1 b 2 … b s b 1 ∗ b 2 ∗ … b s ∗ {\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b_{1}^{*}&b_{2}^{*}&\dots &b_{s}^{*}\\\end{array}}} ({\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b_{1}^{*}&b_{2}^{*}&\dots &b_{s}^{*}\\\end{array}}})

The Runge–Kutta–Fehlberg method has two methods of orders 5 and 4. Its extended Butcher tableau is:

|   | 0 |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   | 1/4 | 1/4 |   |   |   |   |   |
|   | 3/8 | 3/32 | 9/32 |   |   |   |   |
|   | 12/13 | 1932/2197 | −7200/2197 | 7296/2197 |   |   |   |
|   | 1 | 439/216 | −8 | 3680/513 | -845/4104 |   |   |
|   | 1/2 | −8/27 | 2 | −3544/2565 | 1859/4104 | −11/40 |   |
|   |   | 16/135 | 0 | 6656/12825 | 28561/56430 | −9/50 | 2/55 |
|   |   | 25/216 | 0 | 1408/2565 | 2197/4104 | −1/5 | 0 |

However, the simplest adaptive Runge–Kutta method involves combining Heun's method, which is order 2, with the Euler method, which is order 1. Its extended Butcher tableau is:

|   | 0 |   |   |
|---|---|---|---|
|   | 1 | 1 |   |
|   |   | 1/2 | 1/2 |
|   |   | 1 | 0 |

Other adaptive Runge–Kutta methods are the Bogacki–Shampine method (orders 3 and 2), the Cash–Karp method and the Dormand–Prince method (both with orders 5 and 4).


## Nonconfluent Runge–Kutta methods

A Runge–Kutta method is said to be *nonconfluent* if all the c i , i = 1 , 2 , … , s {\displaystyle c_{i},\,i=1,2,\ldots ,s} ({\displaystyle c_{i},\,i=1,2,\ldots ,s}) are distinct.


## Runge–Kutta–Nyström methods

Runge–Kutta–Nyström (RKN) methods are a family of methods based on the same principles as Runge–Kutta methods but for second-order initial value problems, hence problems of the form :

d

2

y

d

t

2

=

f

(

t

,

d

y

d

t

,

y

)

,

y

(

t

0

)

=

y

0

,

d

y

d

t

(

t

0

)

=

y

0

′

.

{\displaystyle {\frac {d^{2}y}{dt^{2}}}=f(t,{\frac {dy}{dt}},y),\quad y(t_{0})=y_{0},\quad {\frac {dy}{dt}}(t_{0})=y'_{0}.}

There are two derivatives two approximates, a Runge-Kutta-Nyström methods hence uses two Runge-Kutta matrices a i j , a i j ′ {\displaystyle a_{ij},a'_{ij}} ({\displaystyle a_{ij},a'_{ij}}), and two sets of weights b i , b i ′ {\displaystyle b_{i},b'_{i}} ({\displaystyle b_{i},b'_{i}}), but still only needs one set of nodes c i {\displaystyle c_{i}} ({\displaystyle c_{i}}). This yields a Butcher table with the form :

c 1 a 11 a 12 … a 1 s c 2 a 21 a 22 … a 2 s ⋮ ⋮ ⋮ ⋱ ⋮ c s a s 1 a s 2 … a s s a 11 ′ a 12 ′ … a 1 s ′ a 21 ′ a 22 ′ … a 2 s ′ ⋮ ⋮ ⋱ ⋮ a s 1 ′ a s 2 ′ … a s s ′ b 1 b 2 … b s b 1 ′ b 2 ′ … b s ′ = c A A ′ b ⊤ b ′ ⊤ {\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &a'_{11}&a'_{12}&\dots &a'_{1s}\\&a'_{21}&a'_{22}&\dots &a'_{2s}\\&\vdots &\vdots &\ddots &\vdots \\&a'_{s1}&a'_{s2}&\dots &a'_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {A'} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}} ({\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &a'_{11}&a'_{12}&\dots &a'_{1s}\\&a'_{21}&a'_{22}&\dots &a'_{2s}\\&\vdots &\vdots &\ddots &\vdots \\&a'_{s1}&a'_{s2}&\dots &a'_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {A'} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}})

Assume the approximations have been carried out up to t n {\displaystyle t_{n}} ({\displaystyle t_{n}}), with y n {\displaystyle y_{n}} ({\displaystyle y_{n}}) the approximation of y ( t n ) {\displaystyle y(t_{n})} ({\displaystyle y(t_{n})}) and y n ′ {\displaystyle y'_{n}} ({\displaystyle y'_{n}}) the approximation of d y d t ( t n ) {\displaystyle {\frac {dy}{dt}}(t_{n})} ({\displaystyle {\frac {dy}{dt}}(t_{n})}). The approximations y n + 1 , y n + 1 ′ {\displaystyle y_{n+1},y'_{n+1}} ({\displaystyle y_{n+1},y'_{n+1}}) at t n + 1 = t n + h {\displaystyle t_{n+1}=t_{n}+h} ({\displaystyle t_{n+1}=t_{n}+h}) are the solutions of the following system :

{ g i = y n + c i h y n ′ + h 2 ∑ j = 1 s a i j f ( t n + c j h , g j ′ , g j ) , i = 1 , 2 , … , s g i ′ = y n ′ + h ∑ j = 1 s a i j ′ f ( t n + c j h , g j ′ , g j ) , i = 1 , 2 , … , s y n + 1 = y n + h y n ′ + h 2 ∑ j = 1 s b j f ( t n + c j h , g j ′ , g j ) y n + 1 ′ = y n ′ + h ∑ j = 1 s b j ′ f ( t n + c j h , g j ′ , g j ) {\displaystyle {\begin{cases}g_{i}=y_{n}+c_{i}hy'_{n}+h^{2}\sum _{j=1}^{s}a_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\g'_{i}=y'_{n}+h\sum _{j=1}^{s}a'_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\\\y_{n+1}=y_{n}+hy'_{n}+h^{2}\sum _{j=1}^{s}b_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\\y'_{n+1}=y'_{n}+h\sum _{j=1}^{s}b'_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\end{cases}}} ({\displaystyle {\begin{cases}g_{i}=y_{n}+c_{i}hy'_{n}+h^{2}\sum _{j=1}^{s}a_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\g'_{i}=y'_{n}+h\sum _{j=1}^{s}a'_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\\\y_{n+1}=y_{n}+hy'_{n}+h^{2}\sum _{j=1}^{s}b_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\\y'_{n+1}=y'_{n}+h\sum _{j=1}^{s}b'_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\end{cases}}})

Where g i , g i ′ {\displaystyle g_{i},g'_{i}} ({\displaystyle g_{i},g'_{i}}) are the intermediate approximations of y {\displaystyle y} ({\displaystyle y}) and d y d t {\displaystyle {\frac {dy}{dt}}} ({\displaystyle {\frac {dy}{dt}}}). It is strictly equivalent to work with the values k j = f ( t n + c j h , g j ′ , g j ) {\displaystyle k_{j}=f(t_{n}+c_{j}h,g'_{j},g_{j})} ({\displaystyle k_{j}=f(t_{n}+c_{j}h,g'_{j},g_{j})}) where the g j , g j ′ {\displaystyle g_{j},g'_{j}} ({\displaystyle g_{j},g'_{j}}) have been replaced with their formula, instead of working with g i , g i ′ {\displaystyle g_{i},g'_{i}} ({\displaystyle g_{i},g'_{i}}), similarly to what we previously did with Runge-Kutta methods, but the system is easier to write this way.

A Runge-Kutta-Nyström method is said to be explicit if both A , A ′ {\displaystyle A,A'} ({\displaystyle A,A'}) are strictly lower triangular, and in this case, the sums ∑ j = 1 s {\textstyle \sum _{j=1}^{s}} ({\textstyle \sum _{j=1}^{s}}) in the expressions of g i , g i ′ {\displaystyle g_{i},g'_{i}} ({\displaystyle g_{i},g'_{i}}), may be replaced with ∑ j = 1 i − 1 {\textstyle \sum _{j=1}^{i-1}} ({\textstyle \sum _{j=1}^{i-1}}). Additionally, a Runge-Kutta-Nyström method is said to be of order p {\displaystyle p} ({\displaystyle p}) if the local truncation error of both y n + 1 , y n + 1 ′ {\displaystyle y_{n+1},y'_{n+1}} ({\displaystyle y_{n+1},y'_{n+1}}) is O ( h p + 1 ) {\displaystyle O(h^{p+1})} ({\displaystyle O(h^{p+1})}).

If the function f {\displaystyle f} ({\displaystyle f}) of the considered initial value problem is independent of d y d t {\displaystyle {\frac {dy}{dt}}} ({\displaystyle {\frac {dy}{dt}}}), one does not need to approximate the intermediate values g i ′ {\displaystyle g'_{i}} ({\displaystyle g'_{i}}) to compute the approximations, the weights a i j ′ {\displaystyle a'_{ij}} ({\displaystyle a'_{ij}}) are hence useless and instead we write a method made only for this special case using a tableau of the form :

c 1 a 11 a 12 … a 1 s c 2 a 21 a 22 … a 2 s ⋮ ⋮ ⋮ ⋱ ⋮ c s a s 1 a s 2 … a s s b 1 b 2 … b s b 1 ′ b 2 ′ … b s ′ = c A b ⊤ b ′ ⊤ {\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}} ({\displaystyle {\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}})

This special case is particularly interesting since it allows for greater order than what a Runge-Kutta-Nyström can achieve in general. For example, two fourth-order explicit RKN methods are given by the following Butcher tableau:

c i a i j 3 + 3 6 0 0 0 3 − 3 6 2 − 3 12 0 0 3 + 3 6 0 3 6 0 b i 3 − 2 3 12 1 2 3 + 2 3 12 b i ′ 5 − 3 3 24 3 + 3 12 1 + 3 24 {\displaystyle {\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3+{\sqrt {3}}}{6}}&0&0&0\\{\frac {3-{\sqrt {3}}}{6}}&{\frac {2-{\sqrt {3}}}{12}}&0&0\\{\frac {3+{\sqrt {3}}}{6}}&0&{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3-2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3+2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5-3{\sqrt {3}}}{24}}&{\frac {3+{\sqrt {3}}}{12}}&{\frac {1+{\sqrt {3}}}{24}}\\\end{array}}} ({\displaystyle {\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3+{\sqrt {3}}}{6}}&0&0&0\\{\frac {3-{\sqrt {3}}}{6}}&{\frac {2-{\sqrt {3}}}{12}}&0&0\\{\frac {3+{\sqrt {3}}}{6}}&0&{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3-2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3+2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5-3{\sqrt {3}}}{24}}&{\frac {3+{\sqrt {3}}}{12}}&{\frac {1+{\sqrt {3}}}{24}}\\\end{array}}}) c i a i j 3 − 3 6 0 0 0 3 + 3 6 2 + 3 12 0 0 3 − 3 6 0 − 3 6 0 b i 3 + 2 3 12 1 2 3 − 2 3 12 b i ′ 5 + 3 3 24 3 − 3 12 1 − 3 24 {\displaystyle {\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3-{\sqrt {3}}}{6}}&0&0&0\\{\frac {3+{\sqrt {3}}}{6}}&{\frac {2+{\sqrt {3}}}{12}}&0&0\\{\frac {3-{\sqrt {3}}}{6}}&0&-{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3+2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3-2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5+3{\sqrt {3}}}{24}}&{\frac {3-{\sqrt {3}}}{12}}&{\frac {1-{\sqrt {3}}}{24}}\\\end{array}}} ({\displaystyle {\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3-{\sqrt {3}}}{6}}&0&0&0\\{\frac {3+{\sqrt {3}}}{6}}&{\frac {2+{\sqrt {3}}}{12}}&0&0\\{\frac {3-{\sqrt {3}}}{6}}&0&-{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3+2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3-2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5+3{\sqrt {3}}}{24}}&{\frac {3-{\sqrt {3}}}{12}}&{\frac {1-{\sqrt {3}}}{24}}\\\end{array}}})

These two schemes also have the symplectic-preserving properties when the original equation is derived from a conservative classical mechanical system, i.e. when

f i ( x 1 , … , x n ) = ∂ V ∂ x i ( x 1 , … , x n ) {\displaystyle f_{i}(x_{1},\ldots ,x_{n})={\frac {\partial V}{\partial x_{i}}}(x_{1},\ldots ,x_{n})} ({\displaystyle f_{i}(x_{1},\ldots ,x_{n})={\frac {\partial V}{\partial x_{i}}}(x_{1},\ldots ,x_{n})})

for some scalar function V {\displaystyle V} ({\displaystyle V}).


## B-stability

The *A-stability* concept for the solution of differential equations is related to the linear autonomous equation y ′ = λ y {\displaystyle y'=\lambda y} ({\displaystyle y'=\lambda y}). Dahlquist (1963) proposed the investigation of stability of numerical schemes when applied to nonlinear systems that satisfy a monotonicity condition. The corresponding concepts were defined as *G-stability* for multistep methods (and the related one-leg methods) and *B-stability* (Butcher, 1975) for Runge–Kutta methods. A Runge–Kutta method applied to the non-linear system y ′ = f ( y ) {\displaystyle y'=f(y)} ({\displaystyle y'=f(y)}), which verifies ⟨ f ( y ) − f ( z ) ,   y − z ⟩ ≤ 0 {\displaystyle \langle f(y)-f(z),\ y-z\rangle \leq 0} ({\displaystyle \langle f(y)-f(z),\ y-z\rangle \leq 0}), is called *B-stable*, if this condition implies ‖ y n + 1 − z n + 1 ‖ ≤ ‖ y n − z n ‖ {\displaystyle \|y_{n+1}-z_{n+1}\|\leq \|y_{n}-z_{n}\|} ({\displaystyle \|y_{n+1}-z_{n+1}\|\leq \|y_{n}-z_{n}\|}) for two numerical solutions.

Let B {\displaystyle B} ({\displaystyle B}), M {\displaystyle M} ({\displaystyle M}) and Q {\displaystyle Q} ({\displaystyle Q}) be three s × s {\displaystyle s\times s} ({\displaystyle s\times s}) matrices defined by B = diag ⁡ ( b 1 , b 2 , … , b s ) , M = B A + A T B − b b T , Q = B A − 1 + A − T B − A − T b b T A − 1 . {\displaystyle {\begin{aligned}B&=\operatorname {diag} (b_{1},b_{2},\ldots ,b_{s}),\\[4pt]M&=BA+A^{T}B-bb^{T},\\[4pt]Q&=BA^{-1}+A^{-T}B-A^{-T}bb^{T}A^{-1}.\end{aligned}}} ({\displaystyle {\begin{aligned}B&=\operatorname {diag} (b_{1},b_{2},\ldots ,b_{s}),\\[4pt]M&=BA+A^{T}B-bb^{T},\\[4pt]Q&=BA^{-1}+A^{-T}B-A^{-T}bb^{T}A^{-1}.\end{aligned}}}) A Runge–Kutta method is said to be *algebraically stable* if the matrices B {\displaystyle B} ({\displaystyle B}) and M {\displaystyle M} ({\displaystyle M}) are both non-negative definite. A sufficient condition for *B-stability* is: B {\displaystyle B} ({\displaystyle B}) and Q {\displaystyle Q} ({\displaystyle Q}) are non-negative definite.
