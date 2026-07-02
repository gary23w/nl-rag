---
title: "Runge–Kutta methods (part 2/2)"
source: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
part: 2/2
---

## Derivation of the Runge–Kutta fourth-order method

In general a Runge–Kutta method of order s {\displaystyle s} ({\displaystyle s}) can be written as:

y

t

+

h

=

y

t

+

h

⋅

∑

i

=

1

s

a

i

k

i

+

O

(

h

s

+

1

)

,

{\displaystyle y_{t+h}=y_{t}+h\cdot \sum _{i=1}^{s}a_{i}k_{i}+{\mathcal {O}}(h^{s+1}),}

where:

k

i

=

∑

j

=

1

s

β

i

j

f

(

k

j

,

t

n

+

α

i

h

)

{\displaystyle k_{i}=\sum _{j=1}^{s}\beta _{ij}f(k_{j},\ t_{n}+\alpha _{i}h)}

are increments obtained evaluating the derivatives of y t {\displaystyle y_{t}} ({\displaystyle y_{t}}) at the i {\displaystyle i} ({\displaystyle i})-th order.

We develop the derivation for the Runge–Kutta fourth-order method using the general formula with s = 4 {\displaystyle s=4} ({\displaystyle s=4}) evaluated, as explained above, at the starting point, the midpoint and the end point of any interval ( t ,   t + h ) {\displaystyle (t,\ t+h)} ({\displaystyle (t,\ t+h)}); thus, we choose:

α

i

β

i

j

α

1

=

0

β

21

=

1

2

α

2

=

1

2

β

32

=

1

2

α

3

=

1

2

β

43

=

1

α

4

=

1

{\displaystyle {\begin{aligned}&\alpha _{i}&&\beta _{ij}\\\alpha _{1}&=0&\beta _{21}&={\frac {1}{2}}\\\alpha _{2}&={\frac {1}{2}}&\beta _{32}&={\frac {1}{2}}\\\alpha _{3}&={\frac {1}{2}}&\beta _{43}&=1\\\alpha _{4}&=1&&\\\end{aligned}}}

and β i j = 0 {\displaystyle \beta _{ij}=0} ({\displaystyle \beta _{ij}=0}) otherwise. We begin by defining the following quantities:

y

t

+

h

1

=

y

t

+

h

f

(

y

t

,

t

)

y

t

+

h

2

=

y

t

+

h

f

(

y

t

+

h

/

2

1

,

t

+

h

2

)

y

t

+

h

3

=

y

t

+

h

f

(

y

t

+

h

/

2

2

,

t

+

h

2

)

{\displaystyle {\begin{aligned}y_{t+h}^{1}&=y_{t}+hf\left(y_{t},\ t\right)\\y_{t+h}^{2}&=y_{t}+hf\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)\\y_{t+h}^{3}&=y_{t}+hf\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)\end{aligned}}}

where y t + h / 2 1 = y t + y t + h 1 2 {\displaystyle y_{t+h/2}^{1}={\dfrac {y_{t}+y_{t+h}^{1}}{2}}} ({\displaystyle y_{t+h/2}^{1}={\dfrac {y_{t}+y_{t+h}^{1}}{2}}}) and y t + h / 2 2 = y t + y t + h 2 2 . {\displaystyle y_{t+h/2}^{2}={\dfrac {y_{t}+y_{t+h}^{2}}{2}}.} ({\displaystyle y_{t+h/2}^{2}={\dfrac {y_{t}+y_{t+h}^{2}}{2}}.}) If we define:

k

1

=

f

(

y

t

,

t

)

k

2

=

f

(

y

t

+

h

/

2

1

,

t

+

h

2

)

=

f

(

y

t

+

h

2

k

1

,

t

+

h

2

)

k

3

=

f

(

y

t

+

h

/

2

2

,

t

+

h

2

)

=

f

(

y

t

+

h

2

k

2

,

t

+

h

2

)

k

4

=

f

(

y

t

+

h

3

,

t

+

h

)

=

f

(

y

t

+

h

k

3

,

t

+

h

)

{\displaystyle {\begin{aligned}k_{1}&=f(y_{t},\ t)\\k_{2}&=f\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right)\\k_{3}&=f\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{2},\ t+{\frac {h}{2}}\right)\\k_{4}&=f\left(y_{t+h}^{3},\ t+h\right)=f\left(y_{t}+hk_{3},\ t+h\right)\end{aligned}}}

and for the previous relations we can show that the following equalities hold up to O ( h 2 ) {\displaystyle {\mathcal {O}}(h^{2})} ({\displaystyle {\mathcal {O}}(h^{2})}): k 2 = f ( y t + h / 2 1 ,   t + h 2 ) = f ( y t + h 2 k 1 ,   t + h 2 ) = f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) k 3 = f ( y t + h / 2 2 ,   t + h 2 ) = f ( y t + h 2 f ( y t + h 2 k 1 ,   t + h 2 ) ,   t + h 2 ) = f ( y t ,   t ) + h 2 d d t [ f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) ] k 4 = f ( y t + h 3 ,   t + h ) = f ( y t + h f ( y t + h 2 k 2 ,   t + h 2 ) ,   t + h ) = f ( y t + h f ( y t + h 2 f ( y t + h 2 f ( y t ,   t ) ,   t + h 2 ) ,   t + h 2 ) ,   t + h ) = f ( y t ,   t ) + h d d t [ f ( y t ,   t ) + h 2 d d t [ f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) ] ] {\displaystyle {\begin{aligned}k_{2}&=f\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\\k_{3}&=f\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\\k_{4}&=f\left(y_{t+h}^{3},\ t+h\right)=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}k_{2},\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}f\left(y_{t},\ t\right),\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t},\ t\right)+h{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\right]\end{aligned}}} ({\displaystyle {\begin{aligned}k_{2}&=f\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\\k_{3}&=f\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\\k_{4}&=f\left(y_{t+h}^{3},\ t+h\right)=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}k_{2},\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}f\left(y_{t},\ t\right),\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t},\ t\right)+h{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\right]\end{aligned}}}) where: d d t f ( y t ,   t ) = ∂ ∂ y f ( y t ,   t ) y ˙ t + ∂ ∂ t f ( y t ,   t ) = f y ( y t ,   t ) y ˙ t + f t ( y t ,   t ) := y ¨ t {\displaystyle {\frac {d}{dt}}f(y_{t},\ t)={\frac {\partial }{\partial y}}f(y_{t},\ t){\dot {y}}_{t}+{\frac {\partial }{\partial t}}f(y_{t},\ t)=f_{y}(y_{t},\ t){\dot {y}}_{t}+f_{t}(y_{t},\ t):={\ddot {y}}_{t}} ({\displaystyle {\frac {d}{dt}}f(y_{t},\ t)={\frac {\partial }{\partial y}}f(y_{t},\ t){\dot {y}}_{t}+{\frac {\partial }{\partial t}}f(y_{t},\ t)=f_{y}(y_{t},\ t){\dot {y}}_{t}+f_{t}(y_{t},\ t):={\ddot {y}}_{t}}) is the total derivative of f {\displaystyle f} ({\displaystyle f}) with respect to time.

If we now express the general formula using what we just derived we obtain: y t + h = y t + h { a ⋅ f ( y t ,   t ) + b ⋅ [ f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) ] + + c ⋅ [ f ( y t ,   t ) + h 2 d d t [ f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) ] ] + + d ⋅ [ f ( y t ,   t ) + h d d t [ f ( y t ,   t ) + h 2 d d t [ f ( y t ,   t ) + h 2 d d t f ( y t ,   t ) ] ] ] } + O ( h 5 ) = y t + a ⋅ h f t + b ⋅ h f t + b ⋅ h 2 2 d f t d t + c ⋅ h f t + c ⋅ h 2 2 d f t d t + + c ⋅ h 3 4 d 2 f t d t 2 + d ⋅ h f t + d ⋅ h 2 d f t d t + d ⋅ h 3 2 d 2 f t d t 2 + d ⋅ h 4 4 d 3 f t d t 3 + O ( h 5 ) {\displaystyle {\begin{aligned}y_{t+h}={}&y_{t}+h\left\lbrace a\cdot f(y_{t},\ t)+b\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right.+\\&{}+c\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]+\\&{}+d\cdot \left[f(y_{t},\ t)+h{\frac {d}{dt}}\left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f(y_{t},\ t)+\left.{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]\right]\right\rbrace +{\mathcal {O}}(h^{5})\\={}&y_{t}+a\cdot hf_{t}+b\cdot hf_{t}+b\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+c\cdot hf_{t}+c\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+\\&{}+c\cdot {\frac {h^{3}}{4}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot hf_{t}+d\cdot h^{2}{\frac {df_{t}}{dt}}+d\cdot {\frac {h^{3}}{2}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot {\frac {h^{4}}{4}}{\frac {d^{3}f_{t}}{dt^{3}}}+{\mathcal {O}}(h^{5})\end{aligned}}} ({\displaystyle {\begin{aligned}y_{t+h}={}&y_{t}+h\left\lbrace a\cdot f(y_{t},\ t)+b\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right.+\\&{}+c\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]+\\&{}+d\cdot \left[f(y_{t},\ t)+h{\frac {d}{dt}}\left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f(y_{t},\ t)+\left.{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]\right]\right\rbrace +{\mathcal {O}}(h^{5})\\={}&y_{t}+a\cdot hf_{t}+b\cdot hf_{t}+b\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+c\cdot hf_{t}+c\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+\\&{}+c\cdot {\frac {h^{3}}{4}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot hf_{t}+d\cdot h^{2}{\frac {df_{t}}{dt}}+d\cdot {\frac {h^{3}}{2}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot {\frac {h^{4}}{4}}{\frac {d^{3}f_{t}}{dt^{3}}}+{\mathcal {O}}(h^{5})\end{aligned}}})

and comparing this with the Taylor series of y t + h {\displaystyle y_{t+h}} ({\displaystyle y_{t+h}}) around t {\displaystyle t} ({\displaystyle t}): y t + h = y t + h y ˙ t + h 2 2 y ¨ t + h 3 6 y t ( 3 ) + h 4 24 y t ( 4 ) + O ( h 5 ) = = y t + h f ( y t ,   t ) + h 2 2 d d t f ( y t ,   t ) + h 3 6 d 2 d t 2 f ( y t ,   t ) + h 4 24 d 3 d t 3 f ( y t ,   t ) {\displaystyle {\begin{aligned}y_{t+h}&=y_{t}+h{\dot {y}}_{t}+{\frac {h^{2}}{2}}{\ddot {y}}_{t}+{\frac {h^{3}}{6}}y_{t}^{(3)}+{\frac {h^{4}}{24}}y_{t}^{(4)}+{\mathcal {O}}(h^{5})=\\&=y_{t}+hf(y_{t},\ t)+{\frac {h^{2}}{2}}{\frac {d}{dt}}f(y_{t},\ t)+{\frac {h^{3}}{6}}{\frac {d^{2}}{dt^{2}}}f(y_{t},\ t)+{\frac {h^{4}}{24}}{\frac {d^{3}}{dt^{3}}}f(y_{t},\ t)\end{aligned}}} ({\displaystyle {\begin{aligned}y_{t+h}&=y_{t}+h{\dot {y}}_{t}+{\frac {h^{2}}{2}}{\ddot {y}}_{t}+{\frac {h^{3}}{6}}y_{t}^{(3)}+{\frac {h^{4}}{24}}y_{t}^{(4)}+{\mathcal {O}}(h^{5})=\\&=y_{t}+hf(y_{t},\ t)+{\frac {h^{2}}{2}}{\frac {d}{dt}}f(y_{t},\ t)+{\frac {h^{3}}{6}}{\frac {d^{2}}{dt^{2}}}f(y_{t},\ t)+{\frac {h^{4}}{24}}{\frac {d^{3}}{dt^{3}}}f(y_{t},\ t)\end{aligned}}})

we obtain a system of constraints on the coefficients:

{

a

+

b

+

c

+

d

=

1

1

2

b

+

1

2

c

+

d

=

1

2

1

4

c

+

1

2

d

=

1

6

1

4

d

=

1

24

{\displaystyle {\begin{cases}&a+b+c+d=1\\[6pt]&{\frac {1}{2}}b+{\frac {1}{2}}c+d={\frac {1}{2}}\\[6pt]&{\frac {1}{4}}c+{\frac {1}{2}}d={\frac {1}{6}}\\[6pt]&{\frac {1}{4}}d={\frac {1}{24}}\end{cases}}}

which when solved gives a = 1 6 , b = 1 3 , c = 1 3 , d = 1 6 {\displaystyle a={\frac {1}{6}},b={\frac {1}{3}},c={\frac {1}{3}},d={\frac {1}{6}}} ({\displaystyle a={\frac {1}{6}},b={\frac {1}{3}},c={\frac {1}{3}},d={\frac {1}{6}}}) as stated above.
