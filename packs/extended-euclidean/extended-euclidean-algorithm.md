---
title: "Extended Euclidean algorithm"
source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
domain: extended-euclidean
license: CC-BY-SA-4.0
tags: extended euclidean algorithm, bezout identity, modular multiplicative inverse, chinese remainder theorem
fetched: 2026-07-02
---

# Extended Euclidean algorithm

In arithmetic and computer programming, the **extended Euclidean algorithm** is an extension to the Euclidean algorithm, and computes, in addition to the greatest common divisor (gcd) of integers *a* and *b*, also the coefficients of Bézout's identity, which are integers *x* and *y* such that $ax+by=\gcd(a,b)$ ; it is generally denoted as $\operatorname {xgcd} (a,b)$ .

This is a certifying algorithm, because the gcd is the only number that can simultaneously satisfy this equation and divide the inputs. It allows one to compute also, with almost no extra cost, the quotients of *a* and *b* by their greatest common divisor.

*Extended Euclidean algorithm* also refers to a very similar algorithm for computing the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

The extended Euclidean algorithm is particularly useful when *a* and *b* are coprime. With that provision, *x* is the modular multiplicative inverse of *a* modulo *b*, and *y* is the modular multiplicative inverse of *b* modulo *a*. Similarly, the polynomial extended Euclidean algorithm allows one to compute the multiplicative inverse in algebraic field extensions and, in particular in finite fields of non-prime order. It follows that both extended Euclidean algorithms are widely used in cryptography. In particular, the computation of the modular multiplicative inverse is an essential step in the derivation of key-pairs in the RSA public-key encryption method.

## Description

The standard Euclidean algorithm proceeds by a succession of Euclidean divisions whose quotients are not used. Only the *remainders* are kept. For the extended algorithm, the successive quotients are used. More precisely, the standard Euclidean algorithm with *a* and *b* as input, consists of computing a sequence $q_{1},\ldots ,q_{k}$ of quotients and a sequence $r_{0},\ldots ,r_{k+1}$ of remainders such that

${\begin{aligned}r_{0}&=a\\r_{1}&=b\\&\,\,\,\vdots \\r_{i+1}&=r_{i-1}-q_{i}r_{i}\quad {\text{and}}\quad 0\leq r_{i+1}<|r_{i}|\quad {\text{(this defines }}q_{i})\\&\,\,\,\vdots \end{aligned}}$

It is the main property of Euclidean division that the inequalities on the right define uniquely $q_{i}$ and $r_{i+1}$ from $r_{i-1}$ and $r_{i}.$

The computation stops when one reaches a remainder $r_{k+1}$ which is zero; the greatest common divisor is then the last nonzero remainder $r_{k}.$

The extended Euclidean algorithm proceeds similarly, but adds two other sequences, as follows

${\begin{aligned}r_{0}&=a&r_{1}&=b\\s_{0}&=1&s_{1}&=0\\t_{0}&=0&t_{1}&=1\\&\,\,\,\vdots &&\,\,\,\vdots \\r_{i+1}&=r_{i-1}-q_{i}r_{i}&{\text{and }}0&\leq r_{i+1}<|r_{i}|&{\text{(this defines }}q_{i}{\text{)}}\\s_{i+1}&=s_{i-1}-q_{i}s_{i}\\t_{i+1}&=t_{i-1}-q_{i}t_{i}\\&\,\,\,\vdots \end{aligned}}$

The computation also stops when $r_{k+1}=0$ and gives

- $r_{k}$ is the greatest common divisor of the input $a=r_{0}$ and $b=r_{1}.$
- The Bézout coefficients are $s_{k}$ and $t_{k},$ that is $\gcd(a,b)=r_{k}=as_{k}+bt_{k}$
- The quotients of *a* and *b* by their greatest common divisor are given by $s_{k+1}=\pm {\frac {b}{\gcd(a,b)}}$ and $t_{k+1}=\mp {\frac {a}{\gcd(a,b)}}$ (the sign $\mp$ is opposite to $\pm$ ).

Moreover, if *a* and *b* are both positive and $\gcd(a,b)\neq \min(a,b)$ , then

$|s_{i}|\leq \left\lfloor {\frac {b}{2\gcd(a,b)}}\right\rfloor \quad {\text{and}}\quad |t_{i}|\leq \left\lfloor {\frac {a}{2\gcd(a,b)}}\right\rfloor$

for $0\leq i\leq k,$ where $\lfloor x\rfloor$ denotes the integral part of x, that is the greatest integer not greater than x.

This implies that the pair of Bézout's coefficients provided by the extended Euclidean algorithm is the *minimal pair* of Bézout coefficients, as being the unique pair satisfying both above inequalities.

It also means that if *a* and *b* fit into an unsigned integer data type, a computer program can compute the Bézout coefficients in the corresponding signed integer type without integer overflow.

### Examples

The following table shows how the extended Euclidean algorithm proceeds with input 240 and 46. The greatest common divisor is the last nonzero entry, 2 in the column "remainder". The computation stops at row 6, because the remainder in it is 0. Bézout coefficients appear in the last two columns of the second-to-last row. In fact, it is easy to verify that −9 × 240 + 47 × 46 = 2. Finally the last two entries 23 and −120 of the last row are, up to the sign, the quotients of the input 46 and 240 by the greatest common divisor 2.

| index *i* | Quotient *q**i*−1 | Remainder *r**i* | *s**i* | *t**i* |
|---|---|---|---|---|
| 0 |   | 240 | 1 | 0 |
| 1 |   | 46 | 0 | 1 |
| 2 | 240 ÷ 46 = 5 | 240 − 5 × 46 = 10 | 1 − 5 × 0 = 1 | 0 − 5 × 1 = −5 |
| 3 | 46 ÷ 10 = 4 | 46 − 4 × 10 = 6 | 0 − 4 × 1 = −4 | 1 − 4 × −5 = 21 |
| 4 | 10 ÷ 6 = 1 | 10 − 1 × 6 = 4 | 1 − 1 × −4 = 5 | −5 − 1 × 21 = −26 |
| 5 | 6 ÷ 4 = 1 | 6 − 1 × 4 = 2 | −4 − 1 × 5 = −9 | 21 − 1 × −26 = 47 |
| 6 | 4 ÷ 2 = 2 | 4 − 2 × 2 = 0 | 5 − 2 × −9 = 23 | −26 − 2 × 47 = −120 |

The following example uses a more compact notation. The greatest common divisor of $a=68$ and $b=30$ can be calculated like this:

$g=\mathrm {gcd} {\underset {\color {Green}\scriptstyle \;\;^{\uparrow }\!\!-\!-\!(-2)}{(68,30)}}=\mathrm {gcd} {\underset {\color {Green}\scriptstyle \!(-3)\!-\!\!-\!^{\uparrow }\;\;}{(8,30)}}$

$=\mathrm {gcd} {\underset {\color {Green}\scriptstyle \;^{\uparrow }\!\!-\!\!-\!(-1)\!\!}{(8,\,6)}}=\mathrm {gcd} {\underset {\color {Green}\scriptstyle \!\!(-3)\!-\!\!-\!^{\uparrow }\;}{(2,\,6)}}=\mathrm {gcd} (2,0)=2,$

where $\color {Green}\scriptstyle \,^{\uparrow }\!\!-\!-\!(-2)$ in the first step means that $-2$ times $30$ is added to $68$ (the gcd does not change when adding a multiple of one number to the other).

Applying the green-indicated additions of multiples analogously to equations, starting with $a=1a+0b$ and $b=0a+1b,$ leads to $g=4a-9b,$ according to the adjacent calculations (the corresponding table far right uses row operations).

### Proof

Since $0\leq r_{i+1}<|r_{i}|$ , the sequence $r_{i}$ is a strictly decreasing sequence of non-negative integers, for $i\geq 2$ . Thus, it must stop with some $r_{k+1}=0$ . This proves that the algorithm stops, eventually.

From the equation $r_{i+1}=r_{i-1}-r_{i}q_{i}$ it follows that $\gcd(r_{i-1},r_{i})=\gcd(r_{i},r_{i+1})$ . As a consequence, $\gcd(a,b)=\gcd(r_{0},r_{1})=\gcd(r_{k},r_{k+1})=\gcd(r_{k},0)=r_{k}$ . Until this point, the proof is the same as that of the classical Euclidean algorithm.

The recurrence relations, for $i\geq 0$ ,

${\begin{cases}r_{i}&=as_{i}+bt_{i}\\(-1)^{i}&=s_{i}t_{i+1}-t_{i}s_{i+1}\end{cases}}$

can be proven by induction. In fact, for $i=0$ they reduce to

${\begin{cases}r_{0}&=a=as_{0}+bt_{0}\\1&=(-1)^{0}=1\cdot 1-0\cdot 0=s_{0}t_{1}-t_{0}s_{1}\end{cases}}$

Assuming they are satisfied for some i , the equations for $i+1$ follow from the computation

${\begin{cases}r_{i+1}&=r_{i-1}-r_{i}q_{i}=(as_{i-1}+bt_{i-1})-(as_{i}+bt_{i})q_{i}=(as_{i-1}-as_{i}q_{i})+(bt_{i-1}-bt_{i}q_{i})=as_{i+1}+bt_{i+1}\\(-1)^{i+1}&=-(s_{i}t_{i+1}-t_{i}s_{i+1})=s_{i+1}(t_{i}-q_{i+1}t_{i+1})-t_{i+1}(s_{i}-q_{i+1}s_{i+1})=s_{i+1}t_{i+2}-t_{i+1}s_{i+2}\end{cases}}$

In particular, the equation $s_{i}t_{i+1}-t_{i}s_{i+1}=(-1)^{i}$ shows that $s_{k+1}$ and $t_{k+1}$ are coprime.

Multiplying $0=r_{k+1}=as_{k+1}+bt_{k+1}$ by $s_{k}$ , it implies that

$0=as_{k+1}s_{k}+bt_{k+1}s_{k}=as_{k+1}s_{k}+b((-1)^{k}+t_{k}s_{k+1})$

Therefore, $b=(-1)^{k+1}(t_{k}-as_{k})s_{k+1}$ , from where it follows that $s_{k+1}$ divides b . As a consequence, there is an integer d such that $b=ds_{k+1}$ . Dividing by $s_{k+1}$ the relation $as_{k+1}+bt_{k+1}=0$ gives $a=-dt_{k+1}.$ Hence, $s_{k+1}$ and $-t_{k+1}$ are coprime integers that are the quotients of a and b by a common factor, which is thus their greatest common divisor or its opposite.

To prove the last assertion, assume that a and b are both positive and $\gcd(a,b)\neq \min(a,b)$ . Then, $a\neq b$ , and if $a<b$ , it can be seen that the *s* and *t* sequences for (*a*,*b*) under the EEA are, up to initial 0s and 1s, the *t* and *s* sequences for (*b*,*a*). The definitions then show that the (*a*,*b*) case reduces to the (*b*,*a*) case. So assume that $a>b$ without loss of generality.

It can be seen that $s_{2}$ is 1 and $s_{3}$ (which exists by $\gcd(a,b)\neq \min(a,b)$ ) is a negative integer. Thereafter, the $s_{i}$ alternate in sign and strictly increase in magnitude, which follows inductively from the definitions and the fact that $q_{i}\geq 1$ for $1\leq i\leq k$ , the case $i=1$ holds because $a>b$ . The same is true for the $t_{i}$ after the first few terms, for the same reason. Furthermore, it is easy to see that $q_{k}\geq 2$ (when *a* and *b* are both positive and $\gcd(a,b)\neq \min(a,b)$ ). Thus, noticing that $|s_{k+1}|=|s_{k-1}|+q_{k}|s_{k}|$ , we obtain $|s_{k+1}|=\left|{\frac {b}{\gcd(a,b)}}\right|\geq 2|s_{k}|\qquad {\text{and}}\qquad |t_{k+1}|=\left|{\frac {a}{\gcd(a,b)}}\right|\geq 2|t_{k}|.$

This, accompanied by the fact that $s_{k},t_{k}$ are larger than or equal to in absolute value than any previous $s_{i}$ or $t_{i}$ respectively completed the proof.

## Polynomial extended Euclidean algorithm

For univariate polynomials with coefficients in a field, everything works similarly, Euclidean division, Bézout's identity and extended Euclidean algorithm. The first difference is that, in the Euclidean division and the algorithm, the inequality $0\leq r_{i+1}<|r_{i}|$ has to be replaced by an inequality on the degrees $\deg r_{i+1}<\deg r_{i}.$ Otherwise, everything which precedes in this article remains the same, simply by replacing integers by polynomials.

A second difference lies in the bound on the size of the Bézout coefficients provided by the extended Euclidean algorithm, which is more accurate in the polynomial case, leading to the following theorem.

*If a and b are two nonzero polynomials, then the extended Euclidean algorithm produces the unique pair of polynomials* (*s*, *t*) *such that*

$as+bt=\gcd(a,b)$

*and*

$\deg s<\deg b-\deg(\gcd(a,b)),\quad \deg t<\deg a-\deg(\gcd(a,b)).$

A third difference is that, in the polynomial case, the greatest common divisor is defined only up to the multiplication by a nonzero constant. There are several ways to define unambiguously a greatest common divisor.

In mathematics, it is common to require that the greatest common divisor be a monic polynomial. To get this, it suffices to divide every element of the output by the leading coefficient of $r_{k}.$ This allows that, if *a* and *b* are coprime, one gets 1 in the right-hand side of Bézout's inequality. Otherwise, one may get any nonzero constant. In computer algebra, the polynomials commonly have integer coefficients, and this way of normalizing the greatest common divisor introduces too many fractions to be convenient.

The second way to normalize the greatest common divisor in the case of polynomials with integer coefficients is to divide every output by the content of $r_{k},$ to get a primitive greatest common divisor. If the input polynomials are coprime, this normalisation also provides a greatest common divisor equal to 1. The drawback of this approach is that a lot of fractions should be computed and simplified during the computation.

A third approach consists in extending the algorithm of subresultant pseudo-remainder sequences in a way that is similar to the extension of the Euclidean algorithm to the extended Euclidean algorithm. This allows that, when starting with polynomials with integer coefficients, all polynomials that are computed have integer coefficients. Moreover, every computed remainder $r_{i}$ is a subresultant polynomial. In particular, if the input polynomials are coprime, then the Bézout's identity becomes

$as+bt=\operatorname {Res} (a,b),$

where $\operatorname {Res} (a,b)$ denotes the resultant of *a* and *b*. In this form of Bézout's identity, there is no denominator in the formula. If one divides everything by the resultant one gets the classical Bézout's identity, with an explicit common denominator for the rational numbers that appear in it.

## Pseudocode

To implement the algorithm that is described above, one should first remark that only the two last values of the indexed variables are needed at each step. Thus, for saving memory, each indexed variable must be replaced by just two variables.

For simplicity, the following algorithm (and the other algorithms in this article) uses parallel assignments. In a programming language which does not have this feature, the parallel assignments need to be simulated with an auxiliary variable. For example, the first one,

```
(old_r, r) := (r, old_r - quotient × r)
```

is equivalent to

```
prov := r;
r := old_r - quotient × prov;
old_r := prov;
```

and similarly for the other parallel assignments. This leads to the following code:

```
function extended_gcd(a, b)
    (old_r, r) := (a, b)
    (old_s, s) := (1, 0)
    (old_t, t) := (0, 1)
    
    while r ≠ 0 do
        quotient := old_r div r
        (old_r, r) := (r, old_r − quotient × r)
        (old_s, s) := (s, old_s − quotient × s)
        (old_t, t) := (t, old_t − quotient × t)
    
    output "Bézout coefficients:", (old_s, old_t)
    output "greatest common divisor:", old_r
    output "quotients by the gcd:", (t, s)
```

The quotients of *a* and *b* by their greatest common divisor, which is output, may have an incorrect sign. This is easy to correct at the end of the computation but has not been done here for simplifying the code. Similarly, if either *a* or *b* is zero and the other is negative, the greatest common divisor that is output is negative, and all the signs of the output must be changed.

Finally, notice that in Bézout's identity, $ax+by=\gcd(a,b)$ , one can solve for y given $a,b,x,\gcd(a,b)$ . Thus, an optimization to the above algorithm is to compute only the $s_{k}$ sequence (which yields the Bézout coefficient x ), and then compute y at the end:

```
function extended_gcd(a, b)
    s := 0;    old_s := 1
    r := b;    old_r := a
         
    while r ≠ 0 do
        quotient := old_r div r
        (old_r, r) := (r, old_r − quotient × r)
        (old_s, s) := (s, old_s − quotient × s)
    
    if b ≠ 0 then
        bezout_t := (old_r − old_s × a) div b
    else
        bezout_t := 0
    
    output "Bézout coefficients:", (old_s, bezout_t)
    output "greatest common divisor:", old_r
```

However, in many cases this is not really an optimization: whereas the former algorithm is not susceptible to overflow when used with machine integers (that is, integers with a fixed upper bound of digits), the multiplication of *old_s × a* in computation of *bezout_t* can overflow, limiting this optimization to inputs which can be represented in less than half the maximal size. When using integers of unbounded size, the time needed for multiplication and division grows quadratically with the size of the integers. This implies that the "optimisation" replaces a sequence of multiplications/divisions of small integers by a single multiplication/division, which requires more computing time than the operations that it replaces, taken together.

## Simplification of fractions

A fraction ⁠*a*/*b*⁠ is in canonical simplified form if *a* and *b* are coprime and *b* is positive. This canonical simplified form can be obtained by replacing the three output lines of the preceding pseudo code by

```
if s = 0 then output "Division by zero"
if s < 0 then s := −s;  t := −t   (for avoiding negative denominators)
if s = 1 then output −t        (for avoiding denominators equal to 1)
output ⁠−t/s⁠
```

The proof of this algorithm relies on the fact that *s* and *t* are two coprime integers such that *as* + *bt* = 0, and thus ${\frac {a}{b}}=-{\frac {t}{s}}$ . To get the canonical simplified form, it suffices to move the minus sign for having a positive denominator.

If *b* divides *a* evenly, the algorithm executes only one iteration, and we have *s* = 1 at the end of the algorithm. It is the only case where the output is an integer.

## Computing multiplicative inverses in modular structures

The extended Euclidean algorithm is the essential tool for computing multiplicative inverses in modular structures, typically the modular integers and the algebraic field extensions. A notable instance of the latter case are the finite fields of non-prime order.

### Modular integers

If *n* is a positive integer, the ring **Z**/*n***Z** may be identified with the set {0, 1, ..., *n*-1} of the remainders of Euclidean division by *n*, the addition and the multiplication consisting in taking the remainder by *n* of the result of the addition and the multiplication of integers. An element *a* of **Z**/*n***Z** has a multiplicative inverse (that is, it is a unit) if it is coprime to *n*. In particular, if *n* is prime, *a* has a multiplicative inverse if it is not zero (modulo *n*). Thus **Z**/*n***Z** is a field if and only if *n* is prime.

Bézout's identity asserts that *a* and *n* are coprime if and only if there exist integers *s* and *t* such that

$ns+at=1$

Reducing this identity modulo *n* gives

$at\equiv 1\mod n.$

Thus *t*, or, more exactly, the remainder of the division of *t* by *n*, is the multiplicative inverse of *a* modulo *n*.

To adapt the extended Euclidean algorithm to this problem, one should remark that the Bézout coefficient of *n* is not needed, and thus does not need to be computed. Also, for getting a result which is positive and lower than *n*, one may use the fact that the integer *t* provided by the algorithm satisfies |*t*| < *n*. That is, if *t* < 0, one must add *n* to it at the end (an example can be found in the article Modular multiplicative inverse). This results in the pseudocode, in which the input *n* is an integer larger than 1.

```
function inverse(a, n)
    t := 0;     newt := 1
    r := n;     newr := a

    while newr ≠ 0 do
        quotient := r div newr
        (t, newt) := (newt, t − quotient × newt) 
        (r, newr) := (newr, r − quotient × newr)

    if r > 1 then
        return "a is not invertible"
    if t < 0 then
        t := t + n

    return t
```

### Simple algebraic field extensions

The extended Euclidean algorithm is also the main tool for computing multiplicative inverses in simple algebraic field extensions. An important case, widely used in cryptography and coding theory, is that of finite fields of non-prime order. In fact, if *p* is a prime number, and *q* = *p**d*, the field of order *q* is a simple algebraic extension of the prime field of *p* elements, generated by a root of an irreducible polynomial of degree *d*.

A simple algebraic extension *L* of a field *K*, generated by the root of an irreducible polynomial *p* of degree *d* may be identified to the quotient ring $K[X]/\langle p\rangle ,$ , and its elements are in bijective correspondence with the polynomials of degree less than *d*. The addition in *L* is the addition of polynomials. The multiplication in *L* is the remainder of the Euclidean division by *p* of the product of polynomials. Thus, to complete the arithmetic in *L*, it remains only to define how to compute multiplicative inverses. This is done by the extended Euclidean algorithm.

The algorithm is very similar to that provided above for computing the modular multiplicative inverse. There are two main differences: firstly the last but one line is not needed, because the Bézout coefficient that is provided always has a degree less than *d*. Secondly, the greatest common divisor which is provided, when the input polynomials are coprime, may be any nonzero element of *K*; this Bézout coefficient (a polynomial generally of positive degree) has thus to be multiplied by the inverse of this element of *K*. In the pseudocode which follows, *p* is a polynomial of degree greater than one, and *a* is a polynomial.

```
function inverse(a, p)
    t := 0;     newt := 1
    r := p;     newr := a

    while newr ≠ 0 do
        quotient := r div newr
        (r, newr) := (newr, r − quotient × newr)
        (t, newt) := (newt, t − quotient × newt)

    if degree(r) > 0 then 
        return "Either p is not irreducible or a is a multiple of p"

    return (1/r) × t
```

#### Example

For example, if the polynomial used to define the finite field GF(28) is *p* = *x*8 + *x*4 + *x*3 + *x* + 1, and *a* = *x*6 + *x*4 + *x* + 1 is the element whose inverse is desired, then performing the algorithm results in the computation described in the following table. Let us recall that in fields of order 2*n*, one has −*z* = *z* and *z* + *z* = 0 for every element *z* in the field). Since 1 is the only nonzero element of GF(2), the adjustment in the last line of the pseudocode is not needed.

| step | quotient | r, newr | s, news | t, newt |
|---|---|---|---|---|
|   |   | *p* = *x*8 + *x*4 + *x*3 + *x* + 1 | 1 | 0 |
|   |   | *a* = *x*6 + *x*4 + *x* + 1 | 0 | 1 |
| 1 | *x*2 + 1 | *x*2 = *p* − *a* (*x*2 + 1) | 1 | *x*2 + 1 = 0 − 1 · (*x*2 + 1) |
| 2 | *x*4 + *x*2 | *x* + 1 = *a* − *x*2 (*x*4 + *x*2) | *x*4+*x*2 = 0 − 1(*x*4+*x*2) | *x*6 + *x*2 + 1 = 1 − (*x*4 + *x*2) (*x*2 + 1) |
| 3 | *x* + 1 | 1 = *x*2 − (*x* + 1) (*x* + 1) | *x*5+*x*4+*x*3+*x*2+1 = 1 − (*x* +1)(*x*4 + *x*2) | *x*7 + *x*6 + *x*3 + *x* = (*x*2 + 1) − (*x* + 1) (*x*6 + *x*2 + 1) |
| 4 | *x* + 1 | 0 = (*x* + 1) − 1 × (*x* + 1) | *x*6 + *x*4 + *x* + 1 = (*x*4+*x*2) − (*x*+1)(*x*5+*x*4+*x*3+*x*2+1) |   |

Thus, the inverse is *x*7 + *x*6 + *x*3 + *x*, as can be confirmed by multiplying the two elements together, and taking the remainder by p of the result.

## The case of more than two numbers

One can handle the case of more than two numbers iteratively. First we show that $\gcd(a,b,c)=\gcd(\gcd(a,b),c)$ . To prove this let $d=\gcd(a,b,c)$ . By definition of gcd d is a divisor of a and b . Thus $\gcd(a,b)=kd$ for some k . Similarly d is a divisor of c so $c=jd$ for some j . Let $u=\gcd(k,j)$ . By our construction of u , $ud|a,b,c$ but since d is the greatest divisor u is a unit. And since $ud=\gcd(\gcd(a,b),c)$ the result is proven.

So if $na+mb=\gcd(a,b)$ then there are x and y such that $x\gcd(a,b)+yc=\gcd(a,b,c)$ so the final equation will be

$x(na+mb)+yc=(xn)a+(xm)b+yc=\gcd(a,b,c).\,$

So then to apply to *n* numbers we use induction

$\gcd(a_{1},a_{2},\dots ,a_{n})=\gcd(a_{1},\,\gcd(a_{2},\,\gcd(a_{3},\dots ,\gcd(a_{n-1}\,,a_{n}))),\dots ),$

with the equations following directly.
