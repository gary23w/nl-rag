---
title: "Sign (mathematics)"
source: https://en.wikipedia.org/wiki/Non-negative
domain: styx-rule
license: CC-BY-SA-4.0
tags: styx rule
fetched: 2026-07-04
---

# Sign (mathematics)

(Redirected from

Non-negative

)

In mathematics, the **sign** of a real number is its property of being either positive, negative, or 0. Depending on local conventions, zero may be considered as having its own unique sign, having no sign, or having both positive and negative sign. In some contexts, it makes sense to distinguish between a positive and a negative zero.

In mathematics and physics, the phrase "change of sign" is associated with exchanging an object for its additive inverse (multiplication with −1, negation), an operation which is not restricted to real numbers. It applies among other objects to vectors, matrices, and complex numbers, which are not prescribed to be only either positive, negative, or zero.

The word "sign" is also often used to indicate binary aspects of mathematical or scientific objects, such as odd and even (sign of a permutation), sense of orientation or rotation (cw/ccw), one sided limits, and other concepts described in § Other meanings below.

## Sign of a number

Numbers from various number systems, like integers, rationals, complex numbers, quaternions, octonions, ... may have multiple attributes, that fix certain properties of a number. A number system that bears the structure of an ordered ring contains a unique number that when added with any number leaves the latter unchanged. This unique number is known as the system's additive identity element. For example, the integers has the structure of an ordered ring. This number is generally denoted as 0. Because of the total order in this ring, there are numbers greater than zero, called the *positive* numbers. Another property required for a ring to be ordered is that, for each positive number, there exists a unique corresponding number less than 0 whose sum with the original positive number is 0. These numbers less than 0 are called the *negative* numbers. The numbers in each such pair are their respective additive inverses. This attribute of a number, being exclusively either *zero* (0), *positive* (+), or *negative* (−), is called its **sign**, and is often encoded to the real numbers 0, 1, and −1, respectively (similar to the way the sign function is defined). Since rational and real numbers are also ordered rings (in fact ordered fields), the *sign* attribute also applies to these number systems.

When a minus sign is used in between two numbers, it represents the binary operation of subtraction. When a minus sign is written before a single number, it represents the unary operation of yielding the additive inverse (sometimes called *negation*) of the operand. Abstractly then, the difference of two number is the sum of the minuend with the additive inverse of the subtrahend. While 0 is its own additive inverse (−0 = 0), the additive inverse of a positive number is negative, and the additive inverse of a negative number is positive. A double application of this operation is written as −(−3) = 3. The plus sign is predominantly used in algebra to denote the binary operation of addition, and only rarely to emphasize the positivity of an expression.

In common numeral notation (used in arithmetic and elsewhere), the sign of a number is often made explicit by placing a plus or a minus sign before the number. For example, +3 denotes "positive three", and −3 denotes "negative three" (algebraically: the additive inverse of 3). Without specific context (or when no explicit sign is given), a number is interpreted per default as positive. This notation establishes a strong association of the minus sign "−" with negative numbers, and the plus sign "+" with positive numbers.

### Sign of zero

Within the convention of zero being neither positive nor negative, a specific sign-value 0 may be assigned to the number value 0. This is exploited in the $\operatorname {sgn}$ -function, as defined for real numbers. In arithmetic, +0 and −0 both denote the same number 0. There is generally no danger of confusing the value with its sign, although the convention of assigning both signs to 0 does not immediately allow for this discrimination.

In certain European countries, e.g. in Belgium and France, 0 is considered to be *both* positive and negative following the convention set forth by Nicolas Bourbaki.

In some contexts, such as floating-point representations of real numbers within computers, it is useful to consider signed versions of zero, with signed zeros referring to different, discrete number representations (see signed number representations for more).

The symbols +0 and −0 rarely appear as substitutes for 0+ and 0−, used in calculus and mathematical analysis for one-sided limits (right-sided limit and left-sided limit, respectively). This notation refers to the behaviour of a function as its real input variable approaches 0 along positive (resp., negative) values; the two limits need not exist or agree.

### Terminology for signs

When 0 is said to be neither positive nor negative, the following phrases may refer to the sign of a number:

- A number is **positive** if it is greater than zero.
- A number is **negative** if it is less than zero.
- A number is **non-negative** if it is greater than or equal to zero.
- A number is **non-positive** if it is less than or equal to zero.

When 0 is said to be both positive and negative, modified phrases are used to refer to the sign of a number:

- A number is **strictly positive** if it is greater than zero.
- A number is **strictly negative** if it is less than zero.
- A number is **positive** if it is greater than or equal to zero.
- A number is **negative** if it is less than or equal to zero.

For example, the absolute value of a real number is always "non-negative", but is not necessarily "positive" in the first interpretation, whereas in the second interpretation, it is called "positive"—though not necessarily "strictly positive".

The same terminology is sometimes used for functions that yield real or other signed values. For example, a function would be called a *positive function* if its values are positive for all arguments of its domain, or a *non-negative function* if all of its values are non-negative.

### Complex numbers

Complex numbers are impossible to order, so they cannot carry the structure of an ordered ring, and, accordingly, cannot be partitioned into positive and negative complex numbers. They do, however, share an attribute with the reals, which is called *absolute value* or *magnitude*. Magnitudes are always non-negative real numbers, and to any non-zero number there belongs a positive real number, its absolute value.

For example, the absolute value of −3 and the absolute value of 3 are both equal to 3. This is written in symbols as |−3| = 3 and |3| = 3.

In general, any arbitrary real value can be specified by its magnitude and its sign. Using the standard encoding, any real value is given by the product of the magnitude and the sign in standard encoding. This relation can be generalized to define a *sign* for complex numbers.

Since the real and complex numbers both form a field and contain the positive reals, they also contain the reciprocals of the magnitudes of all non-zero numbers. This means that any non-zero number may be multiplied with the reciprocal of its magnitude, that is, divided by its magnitude. It is immediate that the quotient of any non-zero real number by its magnitude yields exactly its sign. By analogy, the **sign of a complex number** z can be defined as the quotient of z and its magnitude |*z*|. The sign of a complex number is the exponential of the product of its argument with the imaginary unit. represents in some sense its complex argument. This is to be compared to the sign of real numbers, except with $e^{i\pi }=-1.$ For the definition of a complex sign-function. see § Complex sign function below.

### Sign functions

When dealing with numbers, it is often convenient to have their sign available as a number. This is accomplished by functions that extract the sign of any number, and map it to a predefined value before making it available for further calculations. For example, it might be advantageous to formulate an intricate algorithm for positive values only, and take care of the sign only afterwards.

#### Real sign function

The **sign function** or **signum function** extracts the sign of a real number, by mapping the set of real numbers to the set of the three reals $\{-1,\;0,\;1\}.$ It can be defined as follows: ${\begin{aligned}\operatorname {sgn} :{}&\mathbb {R} \to \{-1,0,1\}\\&x\mapsto \operatorname {sgn}(x)={\begin{cases}-1&{\text{if }}x<0,\\~~\,0&{\text{if }}x=0,\\~~\,1&{\text{if }}x>0.\end{cases}}\end{aligned}}$ Thus sgn(*x*) is 1 when x is positive, and sgn(*x*) is −1 when x is negative. For non-zero values of x, this function can also be defined by the formula $\operatorname {sgn}(x)={\frac {x}{|x|}}={\frac {|x|}{x}},$ where |*x*| is the absolute value of x.

#### Complex sign function

While a real number has a 1-dimensional direction, a complex number has a 2-dimensional direction. The complex sign function requires the magnitude of its argument *z* = *x* + *iy*, which can be calculated as $|z|={\sqrt {z{\bar {z}}}}={\sqrt {x^{2}+y^{2}}}.$

Analogous to above, the **complex sign function** extracts the complex sign of a complex number by mapping the set of non-zero complex numbers to the set of unimodular complex numbers, and 0 to 0: $\{z\in \mathbb {C} :|z|=1\}\cup \{0\}.$ It may be defined as follows:

Let z be also expressed by its magnitude and one of its arguments φ as *z* = |*z*|⋅*eiφ*, then $\operatorname {sgn}(z)={\begin{cases}0&{\text{for }}z=0\\{\dfrac {z}{|z|}}=e^{i\varphi }&{\text{otherwise}}.\end{cases}}$

This definition may also be recognized as a normalized vector, that is, a vector whose direction is unchanged, and whose length is fixed to unity. If the original value was R,θ in polar form, then sign(R, θ) is 1 θ. Extension of sign() or signum() to any number of dimensions is obvious, but this has already been defined as normalizing a vector.

## Signs per convention

In situations where there are exactly two possibilities on equal footing for an attribute, these are often labelled by convention as *plus* and *minus*, respectively. In some contexts, the choice of this assignment (i.e., which range of values is considered positive and which negative) is natural, whereas in other contexts, the choice is arbitrary, making an explicit sign convention necessary, the only requirement being consistent use of the convention.

### Sign of an angle

In many contexts, it is common to associate a sign with the measure of an angle, particularly an oriented angle or an angle of rotation. In such a situation, the sign indicates whether the angle is in the clockwise or counterclockwise direction. Though different conventions can be used, it is common in mathematics to have counterclockwise angles count as positive, and clockwise angles count as negative.

It is also possible to associate a sign to an angle of rotation in three dimensions, assuming that the axis of rotation has been oriented. Specifically, a right-handed rotation around an oriented axis typically counts as positive, while a left-handed rotation counts as negative.

An angle which is the negative of a given angle has an equal arc, but the opposite axis.

### Sign of a change

When a quantity *x* changes over time, the change in the value of *x* is typically defined by the equation $\Delta x=x_{\text{final}}-x_{\text{initial}}.$

Using this convention, an increase in *x* counts as positive change, while a decrease of *x* counts as negative change. In calculus, this same convention is used in the definition of the derivative. As a result, any increasing function has positive derivative, while any decreasing function has negative derivative.

### Sign of a direction

When studying one-dimensional displacements and motions in analytic geometry and physics, it is common to label the two possible directions as positive and negative. Because the number line is usually drawn with positive numbers to the right, and negative numbers to the left, a common convention is for motions to the right to be given a positive sign, and for motions to the left to be given a negative sign.

On the Cartesian plane, the rightward and upward directions are usually thought of as positive, with rightward being the positive *x*-direction, and upward being the positive *y*-direction. If a displacement vector is separated into its vector components, then the horizontal part will be positive for motion to the right and negative for motion to the left, while the vertical part will be positive for motion upward and negative for motion downward.

Likewise, a negative speed (rate of change of displacement) implies a velocity in the opposite direction, i.e., receding instead of advancing; a special case is the radial speed.

In 3D space, notions related to sign can be found in the two normal orientations and orientability in general.

### Signedness in computing

most-significant bit

0

1

1

1

1

1

1

1

=

127

0

1

1

1

1

1

1

0

=

126

0

0

0

0

0

0

1

0

=

2

0

0

0

0

0

0

0

1

=

1

0

0

0

0

0

0

0

0

=

0

1

1

1

1

1

1

1

1

=

−1

1

1

1

1

1

1

1

0

=

−2

1

0

0

0

0

0

0

1

=

−127

1

0

0

0

0

0

0

0

=

−128

Most computers use

two's complement

to represent the sign of an integer.

In computing, an integer value may be either signed or unsigned, depending on whether the computer is keeping track of a sign for the number. By restricting an integer variable to non-negative values only, one more bit can be used for storing the value of a number. Because of the way integer arithmetic is done within computers, signed number representations usually do not store the sign as a single independent bit, instead using e.g. two's complement.

In contrast, real numbers are stored and manipulated as floating point values. The floating point values are represented using three separate values, mantissa, exponent, and sign. Given this separate sign bit, it is possible to represent both positive and negative zero. Most programming languages normally treat positive zero and negative zero as equivalent values, albeit, they provide means by which the distinction can be detected.

### Other meanings

In addition to the sign of a real number, the word sign is also used in various related ways throughout mathematics and other sciences:

- Words *up to sign* mean that, for a quantity q, it is known that either *q* = *Q* or *q* = −*Q* for certain Q. It is often expressed as *q* = ±*Q*. For real numbers, it means that only the absolute value |*q*| of the quantity is known. For complex numbers and vectors, a quantity known up to sign is a stronger condition than a quantity with known magnitude: aside Q and −*Q*, there are many other possible values of q such that |*q*| = |*Q*|.
- The sign of a permutation is defined to be positive if the permutation is even, and negative if the permutation is odd.
- In graph theory, a signed graph is a graph in which each edge has been marked with a positive or negative sign.
- In mathematical analysis, a signed measure is a generalization of the concept of measure in which the measure of a set may have positive or negative values.
  - The concept of signed distance is used to convey *side*, inside or out.
  - The ideas of signed area and signed volume are sometimes used when it is convenient for certain areas or volumes to count as negative. This is particularly true in the theory of determinants. In an (abstract) oriented vector space, each ordered basis for the vector space can be classified as either positively or negatively oriented.
- In a signed-digit representation, each digit of a number may have a positive or negative sign.
- In physics, any electric charge comes with a sign, either positive or negative. By convention, a positive charge is a charge with the same sign as that of a proton, and a negative charge is a charge with the same sign as that of an electron.
