---
title: "Absolute value"
source: https://en.wikipedia.org/wiki/Absolute_value
domain: electrical-resistance-and-conductance
license: CC-BY-SA-4.0
tags: electrical resistance and conductance
fetched: 2026-07-03
---

# Absolute value

In mathematics, the **absolute value** or **modulus** of a real number x , denoted $|x|$ , is the (non-negative) magnitude of x measured without regard to its sign. Namely, $|x|=x$ if x is a positive number, and $|x|=-x$ if x is negative (in which case $-x$ is positive), and $|0|=0$ . For example, the absolute value of 3 is 3, and the absolute value of −3 is also 3. The absolute value of a number may be thought of as its distance from zero.

Generalisations of the absolute value for real numbers occur in a wide variety of mathematical settings. For example, an absolute value is also defined for the complex numbers, the quaternions, ordered rings, fields and vector spaces. The absolute value is closely related to the notions of magnitude, distance, and norm in various mathematical and physical contexts.

## Terminology and notation

In 1806, Jean-Robert Argand introduced the term *module*, meaning *unit of measure* in French, specifically for the *complex* absolute value, and it was borrowed into English in 1866 as the Latin equivalent *modulus*. The term *absolute value* has been used in this sense from at least 1806 in French and 1857 in English. The notation |x|, with a vertical bar on each side, was introduced by Karl Weierstrass in 1841. Other names for *absolute value* include *numerical value* and *magnitude*. The absolute value of x has also been denoted $\operatorname {abs} x$ in some mathematical publications, and in spreadsheets, programming languages, and computational software packages, the absolute value of ${\textstyle x}$ is generally represented by `abs(*x*)`, or a similar expression, as it has been since the earliest days of high-level programming languages.

The vertical bar notation also appears in a number of other mathematical contexts: for example, when applied to a set, it denotes its cardinality; when applied to a matrix, it denotes its determinant. Vertical bars denote the absolute value only for algebraic objects for which the notion of an absolute value is defined, notably an element of a normed division algebra, for example, a real number, a complex number, or a quaternion. A closely related but distinct notation is the use of vertical bars for either the Euclidean norm or sup norm of a vector in $\mathbb {R} ^{n}$ , although double vertical bars with subscripts ( $\|\cdot \|_{2}$ and $\|\cdot \|_{\infty }$ , respectively) are a more common and less ambiguous notation.

## Definition and properties

### Real numbers

For any real number x , the absolute value or modulus of x is denoted by $|x|$ , with a vertical bar on each side of the quantity, and is defined as $|x|={\begin{cases}x,&{\text{if }}x\geq 0\\-x,&{\text{if }}x<0.\end{cases}}$

The absolute value of x is thus always either a positive number or zero, but never negative. When x itself is negative ( $x<0$ ), then its absolute value is necessarily positive ( $|x|=-x>0$ ).

From an analytic geometry point of view, the absolute value of a real number is that number's distance from zero along the real number line, and more generally, the absolute value of the difference of two real numbers (their absolute difference) is the distance between them. The notion of an abstract distance function in mathematics can be seen to be a generalisation of the absolute value of the difference. See § Distance below.

Since the square root symbol represents the unique *positive* square root, when applied to a positive number, it follows that $|x|={\sqrt {x^{2}}}.$ This is equivalent to the definition above, and may be used as an alternative definition of the absolute value of real numbers.

The absolute value has the following four fundamental properties ( ${\textstyle a}$ , ${\textstyle b}$ are real numbers), that are used for generalization of this notion to other domains:

| $\|a\|\geq 0$ | Non-negativity |
|---|---|
| $\|a\|=0\iff a=0$ | Positive-definiteness |
| $\|ab\|=\left\|a\right\|\left\|b\right\|$ | Multiplicativity |
| $\|a+b\|\leq \|a\|+\|b\|$ | Subadditivity, specifically the triangle inequality |

Non-negativity, positive definiteness, and multiplicativity are readily apparent from the definition. To see that subadditivity holds, first note that $|a+b|=s(a+b)$ where $s=\pm 1$ , with its sign chosen to make the result positive. Now, since $-1\cdot x\leq |x|$ and $+1\cdot x\leq |x|$ , it follows that, whichever of $\pm 1$ is the value of s , one has $s\cdot x\leq |x|$ for all real x . Consequently, $|a+b|=s\cdot (a+b)=s\cdot a+s\cdot b\leq |a|+|b|$ , as desired.

Some additional useful properties are given below. These are either immediate consequences of the definition or implied by the four fundamental properties above.

| ${\bigl \|}\left\|a\right\|{\bigr \|}=\|a\|$ | Idempotence (the absolute value of the absolute value is the absolute value) |
|---|---|
| $\left\|-a\right\|=\|a\|$ | Evenness (reflection symmetry of the graph) |
| $\|a-b\|=0\iff a=b$ | Identity of indiscernibles (equivalent to positive-definiteness) |
| $\|a-b\|\leq \|a-c\|+\|c-b\|$ | Triangle inequality (equivalent to subadditivity) |
| $\left\|{\frac {a}{b}}\right\|={\frac {\|a\|}{\|b\|}}\$ (if $b\neq 0$ ) | Preservation of division – equivalent to multiplicativity |
| $\|a-b\|\geq {\bigl \|}\left\|a\right\|-\left\|b\right\|{\bigr \|}$ | Reverse triangle inequality – equivalent to subadditivity |

Two other useful properties concerning inequalities are:

| $\|a\|\leq b\iff -b\leq a\leq b$ |
|---|
| $\|a\|\geq b\iff a\leq -b\$ or $a\geq b$ |

These relations may be used to solve inequalities involving absolute values. For example:

| $\|x-3\|\leq 9$ | $\iff -9\leq x-3\leq 9$ |
|---|---|
|   | $\iff -6\leq x\leq 12$ |

The absolute value, as "distance from zero", is used to define the absolute difference between arbitrary real numbers, the standard metric on the real numbers.

### Complex numbers

Since the complex numbers are not ordered, the definition given at the top for the real absolute value cannot be directly applied to complex numbers. However, the geometric interpretation of the absolute value of a real number as its distance from 0 can be generalised. The absolute value of a complex number is defined by the Euclidean distance of its corresponding point in the complex plane from the origin. This can be computed using the Pythagorean theorem: for any complex number $z=x+iy,$ where x and y are real numbers, the absolute value or modulus of z is denoted $|z|$ and is defined by $|z|={\sqrt {\operatorname {Re} (z)^{2}+\operatorname {Im} (z)^{2}}}={\sqrt {x^{2}+y^{2}}},$ the Pythagorean addition of x and y , where $\operatorname {Re} (z)=x$ and $\operatorname {Im} (z)=y$ denote the real and imaginary parts of z , respectively. When the imaginary part y is zero, this coincides with the definition of the absolute value of the real number x .

When a complex number z is expressed in its polar form as $z=re^{i\theta },$ its absolute value is $|z|=r.$

Since the product of any complex number z and its complex conjugate ${\bar {z}}=x-iy$ , with the same absolute value, is always the non-negative real number $\left(x^{2}+y^{2}\right)$ , the absolute value of a complex number z is the square root of $z\cdot {\overline {z}},$ which is therefore called the absolute square or *squared modulus* of z : $|z|={\sqrt {z\cdot {\overline {z}}}}.$ This generalizes the alternative definition for reals: ${\textstyle |x|={\sqrt {x\cdot x}}}$ .

The complex absolute value shares the four fundamental properties given above for the real absolute value. The identity $|z|^{n}=|z^{n}|$ is a special case of multiplicativity that is often useful by itself.

## Absolute value function

The real absolute value function is continuous everywhere. It is differentiable everywhere except for *x* = 0. It is monotonically decreasing on the interval (−∞, 0] and monotonically increasing on the interval [0, +∞). Since a real number and its opposite have the same absolute value, it is an even function, and is hence not invertible. The real absolute value function is a piecewise linear, convex function.

For both real and complex numbers, the absolute value function is idempotent (meaning that the absolute value of any absolute value is itself).

### Relationship to the sign function

The absolute value function of a real number returns its value irrespective of its sign, whereas the sign (or signum) function returns a number's sign irrespective of its value. The following equations show the relationship between these two functions:

$|x|=x\operatorname {sgn}(x),$

or

$|x|\operatorname {sgn}(x)=x,$

and for *x* ≠ 0,

$\operatorname {sgn}(x)={\frac {|x|}{x}}={\frac {x}{|x|}}.$

### Relationship to the max and min functions

Let $s,t\in \mathbb {R}$ , then the following relationship to the minimum and maximum functions hold:

$|t-s|=-2\min(s,t)+s+t$

and

$|t-s|=2\max(s,t)-s-t.$

The formulas can be derived by considering each case $s>t$ and $t>s$ separately.

From the last formula one can derive also $|t|=\max(t,-t)$ .

### Derivative

The real absolute value function has a derivative for every *x* ≠ 0, given by a step function equal to the sign function except at *x* = 0 where the absolute value function is not differentiable: ${\begin{aligned}{\frac {d\left|x\right|}{dx}}&={\frac {x}{|x|}}={\begin{cases}-1&x<0\\1&x>0\end{cases}}\\[7mu]&=\operatorname {sgn} x\quad {\text{for }}x\neq 0.\end{aligned}}$

The real absolute value function is an example of a continuous function that achieves a global minimum where the derivative does not exist.

The subdifferential of |x| at *x* = 0 is the interval [−1, 1].

The complex absolute value function is continuous everywhere but complex differentiable *nowhere* because it violates the Cauchy–Riemann equations.

The second derivative of |x| with respect to x is zero everywhere except zero, where it does not exist. As a generalised function, the second derivative may be taken as two times the Dirac delta function.

### Antiderivative

The antiderivative (indefinite integral) of the real absolute value function is

$\int \left|x\right|dx={\frac {x\left|x\right|}{2}}+C,$

where C is an arbitrary constant of integration. This is not a complex antiderivative because complex antiderivatives can only exist for complex-differentiable (holomorphic) functions, which the complex absolute value function is not.

### Derivatives and antiderivatives of compositions

The following three formulae are special cases of the chain rule:

${{\text{d}}^{n} \over {\text{d}}x^{n}}f(|x|)=(\operatorname {sgn} x)^{n}f^{(n)}(|x|)\quad {\text{for }}x\neq 0\,,$

if the absolute value is inside a function, and

${{\text{d}}^{n} \over {\text{d}}x^{n}}|f(x)|=\operatorname {sgn}(f(x))f^{(n)}(x)\quad {\text{for }}f(x)\neq 0\,,$

if another function is inside the absolute value. Combining both, the result is:

${{\text{d}}^{n} \over {\text{d}}x^{n}}|f(|x|)|=(\operatorname {sgn} x)^{n}\operatorname {sgn}(f(|x|))f^{(n)}(|x|)\quad {\text{for }}x\neq 0,f(|x|)\neq 0\,.$

From these formulae and using integration by parts, antiderivatives can also be obtained:

$\int {f(|x|){\text{d}}x}=\operatorname {sgn}(x)F(|x|)\quad {\text{for }}x\neq 0\,,$

$\int {|f(x)|{\text{d}}x}=\int {{|f(x)| \over f(x)}f(x){\text{d}}x}=\operatorname {sgn}(f(x))F(x)\quad {\text{for }}f(x)\neq 0\,,$

$\int {|f(|x|)|{\text{d}}x}=\int {{|f(|x|)| \over f(|x|)}f(|x|){\text{d}}x}=\operatorname {sgn}(x)\operatorname {sgn}(f(|x|))F(|x|)\quad {\text{for }}x\neq 0,f(|x|)\neq 0\,,$

supposing the derivative of the sign function is 0.

### Power rule for expressions with absolute values

Using chain and product rules, the power rule for expressions of the type $x^{n}|x|^{m}$ can be written as:

${{\text{d}} \over {\text{d}}x}x^{n}|x|^{m}=(n+m)x^{n-1}|x|^{m}\,.$

This holds true even for $n=0$ :

${{\text{d}} \over {\text{d}}x}|x|^{m}=mx^{-1}|x|^{m}\,.$

## Distance

The absolute value is closely related to the idea of distance. As noted above, the absolute value of a real or complex number is the distance from that number to the origin, along the real number line, for real numbers, or in the complex plane, for complex numbers, and more generally, the absolute value of the difference of two real or complex numbers is the distance between them.

The standard Euclidean distance between two points $a=(a_{1},a_{2},\dots ,a_{n})$ and $b=(b_{1},b_{2},\dots ,b_{n})$ in Euclidean n-space is defined as: ${\sqrt {\textstyle \sum _{i=1}^{n}(a_{i}-b_{i})^{2}}}.$

This can be seen as a generalisation, since for $a_{1}$ and $b_{1}$ real, i.e. in a 1-space, according to the alternative definition of the absolute value,

$|a_{1}-b_{1}|={\sqrt {(a_{1}-b_{1})^{2}}}={\sqrt {\textstyle \sum _{i=1}^{1}(a_{i}-b_{i})^{2}}},$

and for $a=a_{1}+ia_{2}$ and $b=b_{1}+ib_{2}$ complex numbers, i.e. in a 2-space,

| $\|a-b\|$ | $=\|(a_{1}+ia_{2})-(b_{1}+ib_{2})\|$ |
|---|---|
|   | $=\|(a_{1}-b_{1})+i(a_{2}-b_{2})\|$ |
|   | $={\sqrt {(a_{1}-b_{1})^{2}+(a_{2}-b_{2})^{2}}}={\sqrt {\textstyle \sum _{i=1}^{2}(a_{i}-b_{i})^{2}}}.$ |

The above shows that the "absolute value"-distance, for real and complex numbers, agrees with the standard Euclidean distance, which they inherit as a result of considering them as one and two-dimensional Euclidean spaces, respectively.

The properties of the absolute value of the difference of two real or complex numbers: non-negativity, identity of indiscernibles, symmetry and the triangle inequality given above, can be seen to motivate the more general notion of a distance function as follows:

A real valued function d on a set *X* × *X* is called a metric (or a *distance function*) on X, if it satisfies the following four axioms:

| $d(a,b)\geq 0$ | Non-negativity |
|---|---|
| $d(a,b)=0\iff a=b$ | Identity of indiscernibles |
| $d(a,b)=d(b,a)$ | Symmetry |
| $d(a,b)\leq d(a,c)+d(c,b)$ | Triangle inequality |

## Generalizations

### Ordered rings

The definition of absolute value given for real numbers above can be extended to any ordered ring. That is, if a is an element of an ordered ring *R*, then the **absolute value** of a, denoted by |*a*|, is defined to be: $|a|=\left\{{\begin{array}{rl}a,&{\text{if }}a\geq 0\\-a,&{\text{if }}a<0.\end{array}}\right.$ where −*a* is the additive inverse of a, 0 is the additive identity, and < and ≥ have the usual meaning with respect to the ordering in the ring.

### Fields

The four fundamental properties of the absolute value for real numbers can be used to generalise the notion of absolute value to an arbitrary field, as follows.

A real-valued function v on a field F is called an *absolute value* (also a *modulus*, *magnitude*, *value*, or *valuation*) if it satisfies the following four axioms:

| $v(a)\geq 0$ | Non-negativity |
|---|---|
| $v(a)=0\iff a=\mathbf {0}$ | Positive-definiteness |
| $v(ab)=v(a)v(b)$ | Multiplicativity |
| $v(a+b)\leq v(a)+v(b)$ | Subadditivity or the triangle inequality |

Where **0** denotes the additive identity of F. It follows from positive-definiteness and multiplicativity that *v*(**1**) = 1, where **1** denotes the multiplicative identity of F. The real and complex absolute values defined above are examples of absolute values for an arbitrary field.

If v is an absolute value on F, then the function d on *F* × *F*, defined by *d*(*a*, *b*) = *v*(*a* − *b*), is a metric and the following are equivalent:

- d satisfies the ultrametric inequality $d(x,y)\leq \max(d(x,z),d(y,z))$ for all x, y, z in F.
- ${\textstyle \left\{v\left(\sum _{k=1}^{n}\mathbf {1} \right):n\in \mathbb {N} \right\}}$ is bounded in **R**.
- $v\left({\textstyle \sum _{k=1}^{n}}\mathbf {1} \right)\leq 1\$ for every $n\in \mathbb {N}$ .
- $v(a)\leq 1\Rightarrow v(1+a)\leq 1\$ for all $a\in F$ .
- $v(a+b)\leq \max\{v(a),v(b)\}\$ for all $a,b\in F$ .

An absolute value which satisfies any (hence all) of the above conditions is said to be **non-Archimedean**, otherwise it is said to be Archimedean.

### Vector spaces

Again the fundamental properties of the absolute value for real numbers can be used, with a slight modification, to generalise the notion to an arbitrary vector space.

A real-valued function on a vector space V over a field F, represented as ‖ · ‖, is called an **absolute value**, but more usually a **norm**, if it satisfies the following axioms:

For all a in F, and **v**, **u** in V,

| $\\|\mathbf {v} \\|\geq 0$ | Non-negativity |
|---|---|
| $\\|\mathbf {v} \\|=0\iff \mathbf {v} =0$ | Positive-definiteness |
| $\\|a\mathbf {v} \\|=\left\|a\right\|\left\\|\mathbf {v} \right\\|$ | Absolute homogeneity or positive scalability |
| $\\|\mathbf {v} +\mathbf {u} \\|\leq \\|\mathbf {v} \\|+\\|\mathbf {u} \\|$ | Subadditivity or the triangle inequality |

The norm of a vector is also called its *length* or *magnitude*.

In the case of Euclidean space $\mathbb {R} ^{n}$ , the function defined by

$\|(x_{1},x_{2},\dots ,x_{n})\|={\sqrt {\textstyle \sum _{i=1}^{n}x_{i}^{2}}}$

is a norm called the Euclidean norm. When the real numbers $\mathbb {R}$ are considered as the one-dimensional vector space $\mathbb {R} ^{1}$ , the absolute value is a norm, and is the p-norm (see Lp space) for any p. In fact the absolute value is the "only" norm on $\mathbb {R} ^{1}$ , in the sense that, for every norm ‖ · ‖ on $\mathbb {R} ^{1}$ , ‖*x*‖ = ‖1‖ ⋅ |*x*|.

The complex absolute value is a special case of the norm in an inner product space, which is identical to the Euclidean norm when the complex plane is identified as the Euclidean plane  $\mathbb {R} ^{2}$ .

### Composition algebras

Every composition algebra *A* has an involution *x* → *x** called its **conjugation**. The product in *A* of an element *x* and its conjugate *x** is written *N*(*x*) = *x x** and called the **norm of x**.

The real numbers $\mathbb {R}$ , complex numbers $\mathbb {C}$ , and quaternions $\mathbb {H}$ are all composition algebras with norms given by definite quadratic forms. The absolute value in these division algebras is given by the square root of the composition algebra norm.

In general, the norm of a composition algebra may be a quadratic form that is not definite and has null vectors. However, as in the case of division algebras, when an element *x* has a non-zero norm, then *x* has a multiplicative inverse given by *x**/*N*(*x*).
