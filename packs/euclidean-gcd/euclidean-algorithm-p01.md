---
title: "Euclidean algorithm (part 1/2)"
source: https://en.wikipedia.org/wiki/Euclidean_algorithm
domain: euclidean-gcd
license: CC-BY-SA-4.0
tags: euclidean algorithm, greatest common divisor, modular arithmetic, number theory
fetched: 2026-07-02
part: 1/2
---

# Euclidean algorithm

In mathematics, the **Euclidean algorithm**, or **Euclid's algorithm**, is an efficient method for computing the greatest common divisor (GCD) of two integers, the largest number that divides them both without a remainder. It is named after the ancient Greek mathematician Euclid, who first described it in his *Elements* (c. 300 BC). It is an example of an *algorithm*, and is one of the oldest algorithms in common use. It can be used to reduce fractions to their simplest form, and is a part of many other number-theoretic and cryptographic calculations.

The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. For example, 21 is the GCD of 252 and 105 (as 252 = 21 × 12 and 105 = 21 × 5), and the same number 21 is also the GCD of 105 and 252 − 105 = 147. Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal. When that occurs, that number is the GCD of the original two numbers. By reversing the steps or using the extended Euclidean algorithm, the GCD can be expressed as a linear combination of the two original numbers, that is the sum of the two numbers, each multiplied by an integer (for example, 21 = 5 × 105 + (−2) × 252). The fact that the GCD can always be expressed in this way is known as Bézout's identity.

The version of the Euclidean algorithm described above—which follows Euclid's original presentation—may require many subtraction steps to find the GCD when one of the given numbers is much bigger than the other. A more efficient version of the algorithm shortcuts these steps, instead replacing the larger of the two numbers by its remainder when divided by the smaller of the two (with this version, the algorithm stops when reaching a zero remainder). With this improvement, the algorithm never requires more steps than five times the number of digits (base 10) of the smaller integer. This was proven by Gabriel Lamé in 1844 (Lamé's Theorem), and marks the beginning of computational complexity theory. Additional methods for improving the algorithm's efficiency were developed in the 20th century.

The Euclidean algorithm has many theoretical and practical applications. It is used for reducing fractions to their simplest form and for performing division in modular arithmetic. Computations using this algorithm form part of the cryptographic protocols that are used to secure internet communications, and in methods for breaking these cryptosystems by factoring large composite numbers. The Euclidean algorithm may be used to solve Diophantine equations, such as finding numbers that satisfy multiple congruences according to the Chinese remainder theorem, to construct continued fractions, and to find accurate rational approximations to real numbers. Finally, it can be used as a basic tool for proving theorems in number theory such as Lagrange's four-square theorem and the uniqueness of prime factorizations.

The original algorithm was described only for natural numbers and geometric lengths (real numbers), but the algorithm was generalized in the 19th century to other types of numbers, such as Gaussian integers and polynomials of one variable. This led to modern abstract algebraic notions such as Euclidean domains.


## Background: greatest common divisor

The Euclidean algorithm calculates the greatest common divisor (GCD) of two natural numbers a and b. The greatest common divisor g is the largest natural number that divides both a and b without leaving a remainder. Synonyms for GCD include *greatest common factor* (GCF), *highest common factor* (HCF), *highest common divisor* (HCD), and *greatest common measure* (GCM). The greatest common divisor is often written as gcd(*a*, *b*) or, more simply, as (*a*, *b*), although the latter notation is ambiguous, also used for concepts such as an ideal in the ring of integers, which is closely related to GCD.

If gcd(*a*, *b*) = 1, then a and b are said to be coprime (or relatively prime). This property does not imply that a or b are themselves prime numbers. For example, 6 and 35 factor as 6 = 2 × 3 and 35 = 5 × 7, so they are not prime, but their prime factors are different, so 6 and 35 are coprime, with no common factors other than 1.

Let *g* = gcd(*a*, *b*). Since a and b are both multiples of g, they can be written *a* = *mg* and *b* = *ng*, and there is no larger number *G* > *g* for which this is true. The natural numbers m and n must be coprime, since any common factor could be factored out of m and n to make g greater. Thus, any other number c that divides both a and b must also divide g. The greatest common divisor g of a and b is the unique (positive) common divisor of a and b that is divisible by any other common divisor c.

The greatest common divisor can be visualized as follows. Consider a rectangular area a by b, and any common divisor c that divides both a and b exactly. The sides of the rectangle can be divided into segments of length c, which divides the rectangle into a grid of squares of side length c. The GCD g is the largest value of c for which this is possible. For illustration, a 24×60 rectangular area can be divided into a grid of: 1×1 squares, 2×2 squares, 3×3 squares, 4×4 squares, 6×6 squares or 12×12 squares. Therefore, 12 is the GCD of 24 and 60. A 24×60 rectangular area can be divided into a grid of 12×12 squares, with two squares along one edge (24/12 = 2) and five squares along the other (60/12 = 5).

The greatest common divisor of two numbers a and b is the product of the prime factors shared by the two numbers, where each prime factor can be repeated as many times as it divides both a and b. For example, since 1386 can be factored into 2 × 3 × 3 × 7 × 11, and 3213 can be factored into 3 × 3 × 3 × 7 × 17, the GCD of 1386 and 3213 equals 63 = 3 × 3 × 7, the product of their shared prime factors (with 3 repeated since 3 × 3 divides both). If two numbers have no common prime factors, their GCD is 1 (obtained here as an instance of the empty product); in other words, they are coprime. A key advantage of the Euclidean algorithm is that it can find the GCD efficiently without having to compute the prime factors. Factorization of large integers is believed to be a computationally very difficult problem, and the security of many widely used cryptographic protocols is based upon its infeasibility.

Another definition of the GCD is helpful in advanced mathematics, particularly ring theory. The greatest common divisor g of two nonzero numbers a and b is also their smallest positive integral linear combination, that is, the smallest positive number of the form *ua* + *vb* where u and v are integers. The set of all integral linear combinations of a and b is actually the same as the set of all multiples of g (mg, where m is an integer). In modern mathematical language, the ideal generated by a and b is the ideal generated by g alone (an ideal generated by a single element is called a principal ideal, and all ideals of the integers are principal ideals). Some properties of the GCD are in fact easier to see with this description, for instance the fact that any common divisor of a and b also divides the GCD (it divides both terms of *ua* + *vb*). The equivalence of this GCD definition with the other definitions is described below.

The GCD of three or more numbers equals the product of the prime factors common to all the numbers, but it can also be calculated by repeatedly taking the GCDs of pairs of numbers. For example,

gcd(

a

,

b

,

c

) = gcd(

a

, gcd(

b

,

c

)) = gcd(gcd(

a

,

b

),

c

) = gcd(gcd(

a

,

c

),

b

).

Thus, Euclid's algorithm, which computes the GCD of two integers, suffices to calculate the GCD of arbitrarily many integers.


## Description

### Procedure

Compute the Euclidean algorithm step by step

a = 1071; b = 462 a = 119; b = 61

-1

= q

0

×

+ r

0

q

0

=

; r

0

=

Since

r

0

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

1

×

+ r

1

q

1

=

; r

1

=

Since

r

1

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

2

×

+ r

2

q

2

=

; r

2

=

Since

r

2

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

3

×

+ r

3

q

3

=

; r

3

=

Since

r

3

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

4

×

+ r

4

q

4

=

; r

4

=

Since

r

4

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

5

×

+ r

5

q

5

=

; r

5

=

Since

r

5

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

6

×

+ r

6

q

6

=

; r

6

=

Since

r

6

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

7

×

+ r

7

q

7

=

; r

7

=

Since

r

7

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

8

×

+ r

8

q

8

=

; r

8

=

Since

r

8

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

9

×

+ r

9

q

9

=

; r

9

=

Since

r

9

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

= q

10

×

+ r

10

q

10

=

; r

10

=

Since

r

10

= 0

the algorithm is finished. Thus

GCD(

,

) =

.

Number is too big for the calculator

Restart Start

The Euclidean algorithm can be thought of as constructing a sequence of non-negative integers that begins with the two given integers $r_{-2}=a$ and $r_{-1}=b$ and will eventually terminate with the integer zero: $\{r_{-2}=a,\ r_{-1}=b,\ r_{0},\ r_{1},\ \cdots ,\ r_{n-1},\ r_{n}=0\}$ with $r_{k+1}<r_{k}.$ The integer $r_{n-1}$ will then be the GCD and we can state ${\text{gcd}}(a,b)=r_{n-1}.$ The algorithm indicates how to construct the intermediate remainders $r_{k}$ via division-with-remainder on the preceding pair $(r_{k-2},\ r_{k-1})$ by finding an integer quotient $q_{k}$ so that:

$r_{k-2}=q_{k}\cdot r_{k-1}+r_{k}{\text{, with }}\ r_{k-1}>r_{k}\geq 0.$

Because the sequence of non-negative integers $\{r_{k}\}$ is strictly decreasing, it eventually must terminate. In other words, since $r_{k}\geq 0$ for every $k,$ and each $r_{k}$ is an integer that is strictly smaller than the preceding $r_{k-1},$ there eventually cannot be a non-negative integer smaller than zero, and hence the algorithm must terminate. In fact, the algorithm will always terminate at the *n*th step with $r_{n}$ equal to zero.

To illustrate, suppose the GCD of 1071 and 462 is requested. The sequence is initially $\{r_{-2}=1071,\ r_{-1}=462\}$ and in order to find $r_{0},$ we need to find integers $q_{0}$ and $r_{0}<r_{-1}$ such that:

$1071=q_{0}\cdot 462+r_{0}.$

This is the quotient $q_{0}=2$ since $1071=2\cdot 462+147.$ This determines $r_{0}=147$ and so the sequence is now $\{1071,\ 462,\ r_{0}=147\}.$ The next step is to continue the sequence to find $r_{1}$ by finding integers $q_{1}$ and $r_{1}<r_{0}$ such that:

$462=q_{1}\cdot 147+r_{1}.$

This is the quotient $q_{1}=3$ since $462=3\cdot 147+21.$ This determines $r_{1}=21$ and so the sequence is now $\{1071,\ 462,\ 147,\ r_{1}=21\}.$ The next step is to continue the sequence to find $r_{2}$ by finding integers $q_{2}$ and $r_{2}<r_{1}$ such that:

$147=q_{2}\cdot 21+r_{2}.$

This is the quotient $q_{2}=7$ since $147=7\cdot 21+0.$ This determines $r_{2}=0$ and so the sequence is completed as $\{1071,\ 462,\ 147,\ 21,\ r_{2}=0\}$ as no further non-negative integer smaller than 0 can be found. The penultimate remainder $21$ is therefore the requested GCD:

${\text{gcd}}(1071,\ 462)=21.$

We can generalize slightly by dropping any ordering requirement on the initial two values a and $b.$ If $a=b,$ the algorithm may continue and trivially find that ${\text{gcd}}(a,\ a)=a$ as the sequence of remainders will be $\{a,\ a,\ 0\}.$ If $a<b,$ then we can also continue since $a\equiv 0\cdot b+a,$ suggesting the next remainder should be a itself, and the sequence is $\{a,\ b,\ a,\ \cdots \}.$ Normally, this would be invalid because it breaks the requirement $r_{0}<r_{-1}$ but now we have $a<b$ by construction, so the requirement is automatically satisfied and the Euclidean algorithm can continue as normal. Therefore, dropping any ordering between the first two integers does not affect the conclusion that the sequence must eventually terminate because the next remainder will always satisfy $r_{0}<b$ and everything continues as above. The only modifications that need to be made are that $r_{k}<r_{k-1}$ only for $k\geq 0,$ and that the sub-sequence of non-negative integers $\{r_{k-1}\}$ for $k\geq 0$ is strictly decreasing, therefore excluding $a=r_{-2}$ from both statements.

### Proof of validity

The existence of a step N such that $r_{N}=0$ follows from the condition $|r_{i}|<|r_{i-1}|$ , for $i\geq 1$ . This ensures that the algorithm terminates.

The last non-zero remainder $r_{N-1}$ being equal to $\gcd(a,b)$ follows from the following properties of $\gcd$

1. $\gcd(x,0)=x$ , for all $x\neq 0$ .

In fact, the common divisors of

x

and

0

are exactly all the divisors of

x

, of which

x

itself is the largest.

2. $\gcd(x,y)=\gcd(y,x-zy)$

In fact, the sets of common divisors of the pairs

$(x,y)$

and

$(y,x-zy)$

are the same. In particular, the largest of their common divisors are the same.

To see this, assume that

d

is a common divisor of

x

and

y

. This means that there are integers

$X,Y$

such that

$x=dX$

and

$y=dY$

. It follows that

$x-zy=dX-zdY=d(X-zY)$

, where

$X-zY$

is an integer. Therefore,

d

is also a divisor of

$x-zy$

.

Conversely, if

d

is a common divisor of

$x-zy$

and

y

, then there are integers

Z

and

Y

such that

$x-zy=dZ$

and

$y=dY$

. From this

$x=(x-zy)+zy=dZ+zdY=d(Z+zY)$

, where

$Z+zY$

is an integer. Therefore,

d

is also a common divisor of

x

and

y

.

Now, the Euclidean algorithm starts with the pair $(r_{-2},r_{-1})=(a,b)$ and at each step, the pair of remainders $(r_{k-2},r_{k-1})$ is replaced by $(r_{k-1},r_{k-2}-q_{k}r_{k-1})=(r_{k-1},r_{k})$ . Property 2 shows that the $\gcd$ of the pairs remains invariant. In particular, the $\gcd$ of the first pair $(a,b)$ and the last pair $(r_{N-1},0)$ are the same. Applying Property 1, $\gcd(a,b)=\gcd(r_{N-1},0)=r_{N-1}$ .

### Worked example

For illustration, the Euclidean algorithm can be used to find the greatest common divisor of *a* = 1071 and *b* = 462. To begin, multiples of 462 are subtracted from 1071 until the remainder is less than 462. Two such multiples can be subtracted (*q*0 = 2), leaving a remainder of 147:

1071 = 2 × 462 + 147

.

Then multiples of 147 are subtracted from 462 until the remainder is less than 147. Three multiples can be subtracted (*q*1 = 3), leaving a remainder of 21:

462 = 3 × 147 + 21

.

Then multiples of 21 are subtracted from 147 until the remainder is less than 21. Seven multiples can be subtracted (*q*2 = 7), leaving no remainder:

147 = 7 × 21 + 0

.

Since the last remainder is zero, the algorithm ends with 21 as the greatest common divisor of 1071 and 462. This agrees with the gcd(1071, 462) found by prime factorization above. In tabular form, the steps are:

| Step *k* | Equation | Quotient and remainder |
|---|---|---|
| 0 | 1071 = *q*0 462 + *r*0 | *q*0 = 2 and *r*0 = 147 |
| 1 | 462 = *q*1 147 + *r*1 | *q*1 = 3 and *r*1 = 21 |
| 2 | 147 = *q*2 21 + *r*2 | *q*2 = 7 and *r*2 = 0; algorithm ends |

### Visualization

The Euclidean algorithm can be visualized in terms of the tiling analogy given above for the greatest common divisor. Assume that we wish to cover an *a*×*b* rectangle with square tiles exactly, where *a* is the larger of the two numbers. We first attempt to tile the rectangle using *b*×*b* square tiles; however, this leaves an *r*0×*b* residual rectangle untiled, where *r*0 < *b*. We then attempt to tile the residual rectangle with *r*0×*r*0 square tiles. This leaves a second residual rectangle *r*1×*r*0, which we attempt to tile using *r*1×*r*1 square tiles, and so on. The sequence ends when there is no residual rectangle, i.e., when the square tiles cover the previous residual rectangle exactly. The length of the sides of the smallest square tile is the GCD of the dimensions of the original rectangle. For example, the smallest square tile in the adjacent figure is 21×21 (shown in red), and 21 is the GCD of 1071 and 462, the dimensions of the original rectangle (shown in green).

### Euclidean division

At every step *k*, the Euclidean algorithm computes a quotient *q**k* and remainder *r**k* from two numbers *r**k*−1 and *r**k*−2

r

k

−2

=

q

k

r

k

−1

+

r

k

,

where the *r**k* is non-negative and is strictly less than the absolute value of *r**k*−1. The theorem which underlies the definition of the Euclidean division ensures that such a quotient and remainder always exist and are unique.

In Euclid's original version of the algorithm, the quotient and remainder are found by repeated subtraction; that is, *r**k*−1 is subtracted from *r**k*−2 repeatedly until the remainder *r**k* is smaller than *r**k*−1. After that *r**k* and *r**k*−1 are exchanged and the process is iterated. Euclidean division reduces all the steps between two exchanges into a single step, which is thus more efficient. Moreover, the quotients are not needed, thus one may replace Euclidean division by the modulo operation, which gives only the remainder. Thus the iteration of the Euclidean algorithm becomes simply

r

k

=

r

k

−2

mod

r

k

−1

.

### Implementations

Implementations of the algorithm may be expressed in pseudocode. For example, the division-based version may be programmed as

```
function gcd(a, b)
    while b ≠ 0
        t := b
        b := a mod b
        a := t
    return a
```

At the beginning of the *k*th iteration, the variable *b* holds the latest remainder *r**k*−1, whereas the variable *a* holds its predecessor, *r**k*−2. The step *b* := *a* mod *b* is equivalent to the above recursion formula *r**k* ≡ *r**k*−2 mod *r**k*−1. The temporary variable *t* holds the value of *r**k*−1 while the next remainder *r**k* is being calculated. At the end of the loop iteration, the variable *b* holds the remainder *r**k*, whereas the variable *a* holds its predecessor, *r**k*−1.

(If negative inputs are allowed, or if the `**mod**` function may return negative values, the last line must be replaced with `**return abs**(a)`.)

In the subtraction-based version, which was Euclid's original version, the remainder calculation (`b := a **mod** b`) is replaced by repeated subtraction. Contrary to the division-based version, which works with arbitrary integers as input, the subtraction-based version supposes that the input consists of positive integers and stops when *a* = *b*:

```
function gcd(a, b)
    while a ≠ b 
        if a > b
            a := a − b
        else
            b := b − a
    return a
```

The variables *a* and *b* alternate holding the previous remainders *r**k*−1 and *r**k*−2. Assume that *a* is larger than *b* at the beginning of an iteration; then *a* equals *r**k*−2, since *r**k*−2 > *r**k*−1. During the loop iteration, *a* is reduced by multiples of the previous remainder *b* until *a* is smaller than *b*. Then *a* is the next remainder *r**k*. Then *b* is reduced by multiples of *a* until it is again smaller than *a*, giving the next remainder *r**k*+1, and so on.

The recursive version is based on the equality of the GCDs of successive remainders and the stopping condition gcd(*r**N*−1, 0) = *r**N*−1.

```
function gcd(a, b)
    if b = 0
        return a
    else
        return gcd(b, a mod b)
```

(As above, if negative inputs are allowed, or if the `**mod**` function may return negative values, the instruction `**return** a` must be replaced by `**return max**(a, −a)`.)

For illustration, the gcd(1071, 462) is calculated from the equivalent gcd(462, 1071 mod 462) = gcd(462, 147). The latter GCD is calculated from the gcd(147, 462 mod 147) = gcd(147, 21), which in turn is calculated from the gcd(21, 147 mod 21) = gcd(21, 0) = 21.

### Method of least absolute remainders

In another version of Euclid's algorithm, the quotient at each step is increased by one if the resulting negative remainder is smaller in magnitude than the typical positive remainder. Previously, the equation

r

k

−2

=

q

k

r

k

−1

+

r

k

assumed that |*r**k*−1| > *r**k* > 0. However, an alternative negative remainder *e**k* can be computed:

r

k

−2

= (

q

k

+ 1)

r

k

−1

+

e

k

if *r**k*−1 > 0 or

r

k

−2

= (

q

k

– 1)

r

k

−1

+

e

k

if *r**k*−1 < 0.

If *r**k* is replaced by *e**k*. when |*e**k*| < |*r**k*|, then one gets a variant of Euclidean algorithm such that

|

r

k

|

≤

|

r

k

−1

|

/ 2

at each step.

Leopold Kronecker has shown that this version requires the fewest steps of any version of Euclid's algorithm. More generally, it has been proven that, for every input numbers *a* and *b*, the number of steps is minimal if and only if *q**k* is chosen in order that $\left|{\frac {r_{k+1}}{r_{k}}}\right|<{\frac {1}{\varphi }}\sim 0.618,$ where $\varphi$ is the golden ratio.


## Historical development

The Euclidean algorithm is one of the oldest algorithms in common use. It appears in Euclid's *Elements* (c. 300 BC), specifically in Book 7 (Propositions 1–2) and Book 10 (Propositions 2–3). In Book 7, the algorithm is formulated for integers, whereas in Book 10, it is formulated for lengths of line segments. (In modern usage, one would say it was formulated there for real numbers. But lengths, areas, and volumes, represented as real numbers in modern usage, are not measured in the same units and there is no natural unit of length, area, or volume; the concept of real numbers was unknown at that time.) The latter algorithm is geometrical. The GCD of two lengths *a* and *b* corresponds to the greatest length *g* that measures *a* and *b* evenly; in other words, the lengths *a* and *b* are both integer multiples of the length *g*.

The algorithm was probably not discovered by Euclid, who compiled results from earlier mathematicians in his *Elements*. The mathematician and historian B. L. van der Waerden suggests that Book VII derives from a textbook on number theory written by mathematicians in the school of Pythagoras. The algorithm was probably known by Eudoxus of Cnidus (about 375 BC). The algorithm may even pre-date Eudoxus, judging from the use of the technical term ἀνθυφαίρεσις (*anthyphairesis*, reciprocal subtraction) in works by Euclid and Aristotle. Claude Brezinski, following remarks by Pappus of Alexandria, credits the algorithm to Theaetetus (c. 417 – c. 369 BC).

Centuries later, Euclid's algorithm was discovered independently both in India and in China, primarily to solve Diophantine equations that arose in astronomy and making accurate calendars. In the late 5th century, the Indian mathematician and astronomer Aryabhata described the algorithm as the "pulverizer", perhaps because of its effectiveness in solving Diophantine equations. Although a special case of the Chinese remainder theorem had already been described in the Chinese book *Sunzi Suanjing*, the general solution was published by Qin Jiushao in his 1247 book *Shushu Jiuzhang* (數書九章 *Mathematical Treatise in Nine Sections*). The Euclidean algorithm was first described *numerically* and popularized in Europe in the second edition of Bachet's *Problèmes plaisants et délectables* (*Pleasant and enjoyable problems*, 1624). In Europe, it was likewise used to solve Diophantine equations and in developing continued fractions. The extended Euclidean algorithm was published by the English mathematician Nicholas Saunderson, who attributed it to Roger Cotes as a method for computing continued fractions efficiently.

In the 19th century, the Euclidean algorithm led to the development of new number systems, such as Gaussian integers and Eisenstein integers. In 1815, Carl Gauss used the Euclidean algorithm to demonstrate unique factorization of Gaussian integers, although his work was first published in 1832. Gauss mentioned the algorithm in his *Disquisitiones Arithmeticae* (published 1801), but only as a method for continued fractions. Peter Gustav Lejeune Dirichlet seems to have been the first to describe the Euclidean algorithm as the basis for much of number theory. Lejeune Dirichlet noted that many results of number theory, such as unique factorization, would hold true for any other system of numbers to which the Euclidean algorithm could be applied. Lejeune Dirichlet's lectures on number theory were edited and extended by Richard Dedekind, who used Euclid's algorithm to study algebraic integers, a new general type of number. For example, Dedekind was the first to prove Fermat's two-square theorem using the unique factorization of Gaussian integers. Dedekind also defined the concept of a Euclidean domain, a number system in which a generalized version of the Euclidean algorithm can be defined (as described below). In the closing decades of the 19th century, the Euclidean algorithm gradually became eclipsed by Dedekind's more general theory of ideals.

> "[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day."

—

Donald Knuth

,

The Art of Computer Programming, Vol. 2: Seminumerical Algorithms

, 2nd edition (1981), p.

318

Other applications of Euclid's algorithm were developed in the 19th century. In 1829, Charles Sturm showed that the algorithm was useful in the Sturm chain method for counting the real roots of polynomials in any given interval.

The Euclidean algorithm was the first integer relation algorithm, which is a method for finding integer relations between commensurate real numbers. Several novel integer relation algorithms have been developed, such as the algorithm of Helaman Ferguson and R.W. Forcade (1979) and the LLL algorithm.

In 1969, Cole and Davie developed a two-player game based on the Euclidean algorithm, called *The Game of Euclid*, which has an optimal strategy. The players begin with two piles of *a* and *b* stones. The players take turns removing *m* multiples of the smaller pile from the larger. Thus, if the two piles consist of *x* and *y* stones, where *x* is larger than *y*, the next player can reduce the larger pile from *x* stones to *x* − *my* stones, as long as the latter is a nonnegative integer. The winner is the first player to reduce one pile to zero stones.


## Mathematical applications

### Bézout's identity

Bézout's identity states that the greatest common divisor *g* of two integers *a* and *b* can be represented as a linear sum of the original two numbers *a* and *b*. In other words, it is always possible to find integers *s* and *t* such that *g* = *sa* + *tb*.

The integers *s* and *t* can be calculated from the quotients *q*0, *q*1, etc. by reversing the order of equations in Euclid's algorithm. Beginning with the next-to-last equation, *g* can be expressed in terms of the quotient *q**N*−1 and the two preceding remainders, *r**N*−2 and *r**N*−3:

g

=

r

N

−1

=

r

N

−3

−

q

N

−1

r

N

−2

.

Those two remainders can be likewise expressed in terms of their quotients and preceding remainders,

r

N

−2

=

r

N

−4

−

q

N

−2

r

N

−3

and

r

N

−3

=

r

N

−5

−

q

N

−3

r

N

−4

.

Substituting these formulae for *r**N*−2 and *r**N*−3 into the first equation yields *g* as a linear sum of the remainders *r**N*−4 and *r**N*−5. The process of substituting remainders by formulae involving their predecessors can be continued until the original numbers *a* and *b* are reached:

r

2

=

r

0

−

q

2

r

1

r

1

=

b

−

q

1

r

0

r

0

=

a

−

q

0

b

.

After all the remainders *r*0, *r*1, etc. have been substituted, the final equation expresses *g* as a linear sum of *a* and *b*, so that *g* = *sa* + *tb*.

The Euclidean algorithm, and thus Bézout's identity, can be generalized to the context of Euclidean domains.

Bézout's identity provides yet another definition of the greatest common divisor *g* of two numbers *a* and *b*. Consider the set of all numbers *ua* + *vb*, where *u* and *v* are any two integers. Since *a* and *b* are both divisible by *g*, every number in the set is divisible by *g*. In other words, every number of the set is an integer multiple of *g*. This is true for every common divisor of *a* and *b*. However, unlike other common divisors, the greatest common divisor is a member of the set; by Bézout's identity, choosing *u* = *s* and *v* = *t* gives *g*. A smaller common divisor cannot be a member of the set, since every member of the set must be divisible by *g*. Conversely, any multiple *m* of *g* can be obtained by choosing *u* = *ms* and *v* = *mt*, where *s* and *t* are the integers of Bézout's identity. This may be seen by multiplying Bézout's identity by *m*,

mg

=

msa

+

mtb

.

Therefore, the set of all numbers *ua* + *vb* is equivalent to the set of multiples *m* of *g*. In other words, the set of all possible sums of integer multiples of two numbers (*a* and *b*) is equivalent to the set of multiples of gcd(*a*, *b*). The GCD is said to be the generator of the ideal of *a* and *b*. This GCD definition led to the modern abstract algebraic concepts of a principal ideal (an ideal generated by a single element) and a principal ideal domain (a domain in which every ideal is a principal ideal).

Certain problems can be solved using this result. For example, consider two measuring cups of volume *a* and *b*. By adding/subtracting *u* multiples of the first cup and *v* multiples of the second cup, any volume *ua* + *vb* can be measured out. These volumes are all multiples of *g* = gcd(*a*, *b*).

### Extended Euclidean algorithm

The integers *s* and *t* of Bézout's identity can be computed efficiently using the extended Euclidean algorithm. This extension adds two recursive equations to Euclid's algorithm

s

k

=

s

k

−2

−

q

k

s

k

−1

t

k

=

t

k

−2

−

q

k

t

k

−1

with the starting values

s

−2

= 1,

t

−2

= 0

s

−1

= 0,

t

−1

= 1

.

Using this recursion, Bézout's integers *s* and *t* are given by *s* = *s**N* and *t* = *t**N*, where *N* + 1 is the step on which the algorithm terminates with *r**N*+1 = 0.

The validity of this approach can be shown by induction. Assume that the recursion formula is correct up to step *k* − 1 of the algorithm; in other words, assume that

r

j

=

s

j

a

+

t

j

b

for all *j* less than *k*. The *k*th step of the algorithm gives the equation

r

k

=

r

k

−2

−

q

k

r

k

−1

.

Since the recursion formula has been assumed to be correct for *r**k*−2 and *r**k*−1, they may be expressed in terms of the corresponding *s* and *t* variables

r

k

= (

s

k

−2

a

+

t

k

−2

b

) −

q

k

(

s

k

−1

a

+

t

k

−1

b

)

.

Rearranging this equation yields the recursion formula for step *k*, as required

r

k

=

s

k

a

+

t

k

b

= (

s

k

−2

−

q

k

s

k

−1

)

a

+ (

t

k

−2

−

q

k

t

k

−1

)

b

.

### Matrix method

The integers *s* and *t* can also be found using an equivalent matrix method. The sequence of equations of Euclid's algorithm

${\begin{aligned}a&=q_{0}b+r_{0}\\b&=q_{1}r_{0}+r_{1}\\&\,\,\,\vdots \\r_{N-2}&=q_{N}r_{N-1}+0\end{aligned}}$

can be written as a product of 2×2 quotient matrices multiplying a two-dimensional remainder vector

${\begin{pmatrix}a\\b\end{pmatrix}}={\begin{pmatrix}q_{0}&1\\1&0\end{pmatrix}}{\begin{pmatrix}b\\r_{0}\end{pmatrix}}={\begin{pmatrix}q_{0}&1\\1&0\end{pmatrix}}{\begin{pmatrix}q_{1}&1\\1&0\end{pmatrix}}{\begin{pmatrix}r_{0}\\r_{1}\end{pmatrix}}=\cdots =\prod _{i=0}^{N}{\begin{pmatrix}q_{i}&1\\1&0\end{pmatrix}}{\begin{pmatrix}r_{N-1}\\0\end{pmatrix}}\,.$

Let **M** represent the product of all the quotient matrices

$\mathbf {M} ={\begin{pmatrix}m_{11}&m_{12}\\m_{21}&m_{22}\end{pmatrix}}=\prod _{i=0}^{N}{\begin{pmatrix}q_{i}&1\\1&0\end{pmatrix}}={\begin{pmatrix}q_{0}&1\\1&0\end{pmatrix}}{\begin{pmatrix}q_{1}&1\\1&0\end{pmatrix}}\cdots {\begin{pmatrix}q_{N}&1\\1&0\end{pmatrix}}\,.$

This simplifies the Euclidean algorithm to the form

${\begin{pmatrix}a\\b\end{pmatrix}}=\mathbf {M} {\begin{pmatrix}r_{N-1}\\0\end{pmatrix}}=\mathbf {M} {\begin{pmatrix}g\\0\end{pmatrix}}\,.$

To express *g* as a linear sum of *a* and *b*, both sides of this equation can be multiplied by the inverse of the matrix **M**. The determinant of **M** equals (−1)*N*+1, since it equals the product of the determinants of the quotient matrices, each of which is negative one. Since the determinant of **M** is never zero, the vector of the final remainders can be solved using the inverse of **M**

${\begin{pmatrix}g\\0\end{pmatrix}}=\mathbf {M} ^{-1}{\begin{pmatrix}a\\b\end{pmatrix}}=(-1)^{N+1}{\begin{pmatrix}m_{22}&-m_{12}\\-m_{21}&m_{11}\end{pmatrix}}{\begin{pmatrix}a\\b\end{pmatrix}}\,.$

Since the top equation gives

g

= (−1)

N

+1

(

m

22

a

−

m

12

b

)

,

the two integers of Bézout's identity are *s* = (−1)*N*+1*m*22 and *t* = (−1)*N**m*12. The matrix method is as efficient as the equivalent recursion, with two multiplications and two additions per step of the Euclidean algorithm.

### Euclid's lemma and unique factorization

Bézout's identity is essential to many applications of Euclid's algorithm, such as demonstrating the unique factorization of numbers into prime factors. To illustrate this, suppose that a number *L* can be written as a product of two factors *u* and *v*, that is, *L* = *uv*. If another number *w* also divides *L* but is coprime with *u*, then *w* must divide *v*, by the following argument: If the greatest common divisor of *u* and *w* is 1, then integers *s* and *t* can be found such that

1 =

su

+

tw

by Bézout's identity. Multiplying both sides by *v* gives the relation:

v

=

suv

+

twv

=

sL

+

twv

Since *w* divides both terms on the right-hand side, it must also divide the left-hand side, *v*. This result is known as Euclid's lemma. Specifically, if a prime number divides *L*, then it must divide at least one factor of *L*. Conversely, if a number *w* is coprime to each of a series of numbers *a*1, *a*2, ..., *a**n*, then *w* is also coprime to their product, *a*1 × *a*2 × ... × *a**n*.

Euclid's lemma suffices to prove that every number has a unique factorization into prime numbers. To see this, assume the contrary, that there are two independent factorizations of *L* into *m* and *n* prime factors, respectively

L

=

p

1

p

2

...

p

m

=

q

1

q

2

...

q

n

.

Since each prime *p* divides *L* by assumption, it must also divide one of the *q* factors; since each *q* is prime as well, it must be that *p* = *q*. Iteratively dividing by the *p* factors shows that each *p* has an equal counterpart *q*; the two prime factorizations are identical except for their order. The unique factorization of numbers into primes has many applications in mathematical proofs, as shown below.

### Linear Diophantine equations

Diophantine equations are equations in which the solutions are restricted to integers; they are named after the 3rd-century Alexandrian mathematician Diophantus. A typical *linear* Diophantine equation seeks integers *x* and *y* such that

ax

+

by

=

c

where *a*, *b* and *c* are given integers. This can be written as an equation for *x* in modular arithmetic:

ax

≡

c

mod

b

.

Let *g* be the greatest common divisor of *a* and *b*. Both terms in *ax* + *by* are divisible by *g*; therefore, *c* must also be divisible by *g*, or the equation has no solutions. By dividing both sides by *c*/*g*, the equation can be reduced to Bezout's identity

sa

+

tb

=

g

,

where *s* and *t* can be found by the extended Euclidean algorithm. This provides one solution to the Diophantine equation, *x*1 = *s* (*c*/*g*) and *y*1 = *t* (*c*/*g*).

In general, a linear Diophantine equation has no solutions, or an infinite number of solutions. To find the latter, consider two solutions, (*x*1, *y*1) and (*x*2, *y*2), where

ax

1

+

by

1

=

c

=

ax

2

+

by

2

or equivalently

a

(

x

1

−

x

2

) =

b

(

y

2

−

y

1

)

.

Therefore, the smallest difference between two *x* solutions is *b*/*g*, whereas the smallest difference between two *y* solutions is *a*/*g*. Thus, the solutions may be expressed as

x

=

x

1

−

bu

/

g

y

=

y

1

+

au

/

g

.

By allowing *u* to vary over all possible integers, an infinite family of solutions can be generated from a single solution (*x*1, *y*1). If the solutions are required to be *positive* integers (*x* > 0, *y* > 0), only a finite number of solutions may be possible. This restriction on the acceptable solutions allows some systems of Diophantine equations with more unknowns than equations to have a finite number of solutions; this is impossible for a system of linear equations when the solutions can be any real number (see Underdetermined system).

### Multiplicative inverses and the RSA algorithm

A finite field is a set of numbers with four generalized operations. The operations are called addition, subtraction, multiplication and division and have their usual properties, such as commutativity, associativity and distributivity. An example of a finite field is the set of 13 numbers {0, 1, 2, ..., 12} using modular arithmetic. In this field, the results of any mathematical operation (addition, subtraction, multiplication, or division) is reduced modulo 13; that is, multiples of 13 are added or subtracted until the result is brought within the range 0–12. For example, the result of 5 × 7 = 35 mod 13 = 9. Such finite fields can be defined for any prime *p*; using more sophisticated definitions, they can also be defined for any power *m* of a prime *p**m*. Finite fields are often called Galois fields, and are abbreviated as GF(*p*) or GF(*p**m*).

In such a field with *m* numbers, every nonzero element *a* has a unique modular multiplicative inverse, *a*−1 such that *aa*−1 = *a*−1*a* ≡ 1 mod *m*. This inverse can be found by solving the congruence equation *ax* ≡ 1 mod *m*, or the equivalent linear Diophantine equation

ax

+

my

= 1

.

This equation can be solved by the Euclidean algorithm, as described above. Finding multiplicative inverses is an essential step in the RSA algorithm, which is widely used in electronic commerce; specifically, the equation determines the integer used to decrypt the message. Although the RSA algorithm uses rings rather than fields, the Euclidean algorithm can still be used to find a multiplicative inverse where one exists. The Euclidean algorithm also has other applications in error-correcting codes; for example, it can be used as an alternative to the Berlekamp–Massey algorithm for decoding BCH and Reed–Solomon codes, which are based on Galois fields.

### Chinese remainder theorem

Euclid's algorithm can also be used to solve multiple linear Diophantine equations. Such equations arise in the Chinese remainder theorem, which describes a novel method to represent an integer *x*. Instead of representing an integer by its digits, it may be represented by its remainders *x**i* modulo a set of *N* coprime numbers *m**i*:

${\begin{aligned}x_{1}&\equiv x{\pmod {m_{1}}}\\x_{2}&\equiv x{\pmod {m_{2}}}\\&\,\,\,\vdots \\x_{N}&\equiv x{\pmod {m_{N}}}\,.\end{aligned}}$

The goal is to determine *x* from its *N* remainders *x**i*. The solution is to combine the multiple equations into a single linear Diophantine equation with a much larger modulus *M* that is the product of all the individual moduli *m**i*, and define *M**i* as

$M_{i}={\frac {M}{m_{i}}}.$

Thus, each *M**i* is the product of all the moduli *except* *m**i*. The solution depends on finding *N* new numbers *h**i* such that

$M_{i}h_{i}\equiv 1{\pmod {m_{i}}}\,.$

With these numbers *h**i*, any integer *x* can be reconstructed from its remainders *x**i* by the equation

$x\equiv (x_{1}M_{1}h_{1}+x_{2}M_{2}h_{2}+\cdots +x_{N}M_{N}h_{N}){\pmod {M}}\,.$

Since these numbers *h**i* are the multiplicative inverses of the *M**i*, they may be found using Euclid's algorithm as described in the previous subsection.

### Stern–Brocot tree

The Euclidean algorithm can be used to arrange the set of all positive rational numbers into an infinite binary search tree, called the Stern–Brocot tree. The number 1 (expressed as a fraction 1/1) is placed at the root of the tree, and the location of any other number *a*/*b* can be found by computing gcd(*a*,*b*) using the original form of the Euclidean algorithm, in which each step replaces the larger of the two given numbers by its difference with the smaller number (not its remainder), stopping when two equal numbers are reached. A step of the Euclidean algorithm that replaces the first of the two numbers corresponds to a step in the tree from a node to its right child, and a step that replaces the second of the two numbers corresponds to a step in the tree from a node to its left child. The sequence of steps constructed in this way does not depend on whether *a*/*b* is given in lowest terms, and forms a path from the root to a node containing the number *a*/*b*. This fact can be used to prove that each positive rational number appears exactly once in this tree.

For example, 3/4 can be found by starting at the root, going to the left once, then to the right twice:

${\begin{aligned}&\gcd(3,4)&\leftarrow \\={}&\gcd(3,1)&\rightarrow \\={}&\gcd(2,1)&\rightarrow \\={}&\gcd(1,1).\end{aligned}}$

The Euclidean algorithm has almost the same relationship to another binary tree on the rational numbers called the Calkin–Wilf tree. The difference is that the path is reversed: instead of producing a path from the root of the tree to a target, it produces a path from the target to the root.

### Continued fractions

The Euclidean algorithm has a close relationship with continued fractions. The sequence of equations can be written in the form

${\begin{aligned}{\frac {a}{b}}&=q_{0}+{\frac {r_{0}}{b}}\\{\frac {b}{r_{0}}}&=q_{1}+{\frac {r_{1}}{r_{0}}}\\{\frac {r_{0}}{r_{1}}}&=q_{2}+{\frac {r_{2}}{r_{1}}}\\&\,\,\,\vdots \\{\frac {r_{k-2}}{r_{k-1}}}&=q_{k}+{\frac {r_{k}}{r_{k-1}}}\\&\,\,\,\vdots \\{\frac {r_{N-2}}{r_{N-1}}}&=q_{N}\,.\end{aligned}}$

The last term on the right-hand side always equals the inverse of the left-hand side of the next equation. Thus, the first two equations may be combined to form

${\frac {a}{b}}=q_{0}+{\cfrac {1}{q_{1}+{\cfrac {r_{1}}{r_{0}}}}}\,.$

The third equation may be used to substitute the denominator term *r*1/*r*0, yielding

${\frac {a}{b}}=q_{0}+{\cfrac {1}{q_{1}+{\cfrac {1}{q_{2}+{\cfrac {r_{2}}{r_{1}}}}}}}\,.$

The final ratio of remainders *r**k*/*r**k*−1 can always be replaced using the next equation in the series, up to the final equation. The result is a continued fraction

${\frac {a}{b}}=q_{0}+{\cfrac {1}{q_{1}+{\cfrac {1}{q_{2}+{\cfrac {1}{\ddots +{\cfrac {1}{q_{N}}}}}}}}}=[q_{0};q_{1},q_{2},\ldots ,q_{N}]\,.$

In the worked example above, the gcd(1071, 462) was calculated, and the quotients *q**k* were 2, 3 and 7, respectively. Therefore, the fraction 1071/462 may be written

${\frac {1071}{462}}=2+{\cfrac {1}{3+{\cfrac {1}{7}}}}=[2;3,7]$

as can be confirmed by calculation.

### Factorization algorithms

Calculating a greatest common divisor is an essential step in several integer factorization algorithms, such as Pollard's rho algorithm, Shor's algorithm, Dixon's factorization method and the Lenstra elliptic curve factorization. The Euclidean algorithm may be used to find this GCD efficiently. Continued fraction factorization uses continued fractions, which are determined using Euclid's algorithm.
