---
title: "Karatsuba algorithm"
source: https://en.wikipedia.org/wiki/Karatsuba_algorithm
domain: karatsuba-multiplication
license: CC-BY-SA-4.0
tags: karatsuba algorithm, fast multiplication, toom cook multiplication, divide and conquer
fetched: 2026-07-02
---

# Karatsuba algorithm

The **Karatsuba algorithm** is a fast multiplication algorithm for integers. It was discovered by Anatoly Karatsuba in 1960 and published in 1962. It is a divide-and-conquer algorithm that reduces the multiplication of two *n*-digit numbers to three multiplications of *n*/2-digit numbers and, by repeating this reduction, to at most $n^{\log _{2}3}\approx n^{1.58}$ single-digit multiplications. It is therefore asymptotically faster than the traditional algorithm, which performs $n^{2}$ single-digit products.

The Karatsuba algorithm was the first multiplication algorithm asymptotically faster than the quadratic "grade school" algorithm. The Toom–Cook algorithm (1963) is a faster generalization of Karatsuba's method, and the Schönhage–Strassen algorithm (1971) is even faster, for sufficiently large *n*.

## History

The standard procedure for multiplication of two *n*-digit numbers requires a number of elementary operations proportional to $n^{2}\,\!$ , or $O(n^{2})\,\!$ in big-O notation. Andrey Kolmogorov conjectured that the traditional algorithm was *asymptotically optimal,* meaning that any algorithm for that task would require $\Omega (n^{2})\,\!$ elementary operations.

In 1960, Kolmogorov organized a seminar on mathematical problems in cybernetics at the Moscow State University, where he stated the $\Omega (n^{2})\,\!$ conjecture and other problems in the complexity of computation. Within a week, Karatsuba, then a 23-year-old student, found an algorithm that multiplies two *n*-digit numbers in $O(n^{\log _{2}3})$ elementary steps, thus disproving the conjecture. Kolmogorov was very excited about the discovery; he communicated it at the next meeting of the seminar, which was then terminated. Kolmogorov gave some lectures on the Karatsuba result at conferences all over the world (see, for example, "Proceedings of the International Congress of Mathematicians 1962", pp. 351–356, and also "6 Lectures delivered at the International Congress of Mathematicians in Stockholm, 1962") and published the method in 1962, in the Proceedings of the USSR Academy of Sciences. The article had been written by Kolmogorov and contained two results on multiplication, Karatsuba's algorithm and a separate result by Yuri Ofman; it listed "A. Karatsuba and Yu. Ofman" as the authors. Karatsuba only became aware of the paper when he received the reprints from the publisher.

## Algorithm

### Basic step

The basic principle of Karatsuba's algorithm is divide-and-conquer, using a formula that allows one to compute the product of two large numbers x and y using three multiplications of smaller numbers, each with about half as many digits as x or y , plus some additions and digit shifts. This basic step is, in fact, a generalization of a similar complex multiplication algorithm, where the imaginary unit i is replaced by a power of the base.

Let x and y be represented as n -digit strings in some base B . For any positive integer m less than n , one can write the two given numbers as

$x=x_{1}B^{m}+x_{0},$

$y=y_{1}B^{m}+y_{0},$

where $x_{0}$ and $y_{0}$ are less than $B^{m}$ . The product is then

${\begin{aligned}xy&=(x_{1}B^{m}+x_{0})(y_{1}B^{m}+y_{0})\\&=x_{1}y_{1}B^{2m}+(x_{1}y_{0}+x_{0}y_{1})B^{m}+x_{0}y_{0}\\&=z_{2}B^{2m}+z_{1}B^{m}+z_{0},\\\end{aligned}}$

where

$z_{2}=x_{1}y_{1},$

$z_{1}=x_{1}y_{0}+x_{0}y_{1},$

$z_{0}=x_{0}y_{0}.$

These formulae require four multiplications and were known to Charles Babbage. Karatsuba observed that $xy$ can be computed in only three multiplications, at the cost of a few extra additions. With $z_{0}$ and $z_{2}$ as before and $z_{3}=(x_{1}+x_{0})(y_{1}+y_{0}),$ one observes that

${\begin{alignedat}{2}z_{1}&=x_{1}y_{0}+x_{0}y_{1}\\&=x_{1}y_{0}+x_{0}y_{1}+x_{1}y_{1}+x_{0}y_{0}&&-x_{1}y_{1}-x_{0}y_{0}\\&=(x_{1}+x_{0})(y_{1}+y_{0})&&-x_{1}y_{1}-x_{0}y_{0}\\&=z_{3}-z_{2}-z_{0}.\\\end{alignedat}}$

Thus only three multiplications are required for computing $z_{0},z_{1}$ and $z_{2},$ and thus $xy.$

An alternative form uses $z_{4}=(x_{1}-x_{0})(y_{1}-y_{0})$ instead:

${\begin{aligned}z_{1}&={\phantom {x_{1}y_{1}+x_{0}y_{0}-(x_{1}y_{1}-x_{0}y_{0}+{}}}x_{1}y_{0}+x_{0}y_{1}\\&=x_{1}y_{1}+x_{0}y_{0}-{\phantom {(}}x_{1}y_{1}-x_{0}y_{0}+x_{1}y_{0}+x_{0}y_{1}\\&=x_{1}y_{1}+x_{0}y_{0}-(x_{1}y_{1}+x_{0}y_{0}-x_{1}y_{0}-x_{0}y_{1})\\&=x_{1}y_{1}+x_{0}y_{0}-(x_{1}-x_{0})(y_{1}-y_{0})\\&=z_{2}+z_{0}-z_{4}.\\\end{aligned}}$

### Example

To compute the product of 12345 and 6789, where *B* = 10, choose *m* = 3. We use *m* right shifts for decomposing the input operands using the resulting base (*B**m* = *1000*), as:

12345 =

12

·

1000

+

345

6789 =

6

·

1000

+

789

Only three multiplications, which operate on smaller integers, are used to compute three partial results:

z

2

=

12

×

6

= 72

z

0

=

345

×

789

= 272205

z

1

= (

12

+

345

)

×

(

6

+

789

) −

z

2

−

z

0

= 357

×

795 − 72 − 272205 = 283815 − 72 − 272205 = 11538

We get the result by just adding these three partial results, shifted accordingly (and then taking carries into account by decomposing these three inputs in base *1000* as for the input operands):

result =

z

2

· (

B

m

)

2

+

z

1

· (

B

m

)

1

+

z

0

· (

B

m

)

0

, i.e.

result = 72 ·

1000

2

+ 11538 ·

1000

+ 272205 =

83810205

.

Note that the intermediate third multiplication operates on an input domain which is less than two times larger than for the two first multiplications, its output domain is less than four times larger, and base-*1000* carries computed from the first two multiplications must be taken into account when computing these two subtractions.

### Recursive application

If *n* is four or more, the three multiplications in Karatsuba's basic step involve operands with fewer than *n* digits. Therefore, those products can be computed by recursive calls of the Karatsuba algorithm. The recursion can be applied until the numbers are so small that they can (or must) be computed directly.

In a computer with a full 32-bit by 32-bit multiplier, for example, one could choose *B* = 231 and store each digit as a separate 32-bit binary word. Then the sums *x*1 + *x*0 and *y*1 + *y*0 will not need an extra binary word for storing the carry-over digit (as in carry-save adder), and the Karatsuba recursion can be applied until the numbers to multiply are only one digit long.

### Time complexity analysis

Karatsuba's basic step works for any base *B* and any *m*, but the recursive algorithm is most efficient when *m* is equal to *n*/2, rounded up. In particular, if *n* is 2*k*, for some integer *k*, and the recursion stops only when *n* is 1, then the number of single-digit multiplications is 3*k*, which is *n**c* where *c* = log23.

Since one can extend any inputs with zero digits until their length is a power of two, it follows that the number of elementary multiplications, for any *n*, is at most $3^{\lceil \log _{2}n\rceil }\leq 3n^{\log _{2}3}\,\!$ .

Since the additions, subtractions, and digit shifts (multiplications by powers of *B*) in Karatsuba's basic step take time proportional to *n*, their cost becomes negligible as *n* increases. More precisely, if *T*(*n*) denotes the total number of elementary operations that the algorithm performs when multiplying two *n*-digit numbers, then

$T(n)=3T(\lceil n/2\rceil )+cn+d$

for some constants *c* and *d*. For this recurrence relation, the master theorem for divide-and-conquer recurrences gives the asymptotic bound $T(n)=\Theta (n^{\log _{2}3})\,\!$ .

It follows that, for sufficiently large *n*, Karatsuba's algorithm will perform fewer shifts and single-digit additions than longhand multiplication, even though its basic step uses more additions and shifts than the straightforward formula. For small values of *n*, however, the extra shift and add operations may make it run slower than the longhand method.

## Implementation

Here is the pseudocode for this algorithm, using numbers represented in base ten. For the binary representation of integers, it suffices to set BASE to a different number, usually a power of 2 in line with the size of the machine word that the computer can natively multiply.

```mw
const BASE = 10

/* Count the size of num in BASE. For example, 12345 has a size of 5 in base 10 and a size of 2 in base 1024. */
function size_in_base(num)
    string_num = num.toString()
	return string_num.length()

/* Split a digit into its low "d" digits and its high digits. For example, split_at(12345, 3) will extract the 3 final digits, giving: high=12, low=345. */
function split_at(num, d)
	hi =  num / (BASE ^ d) 
    low = num % (BASE ^ d) /* remainder of division */
	return hi, low

function karatsuba(num1, num2)
    if (num1 < BASE or num2 < BASE)
        return num1 × num2 /* fall back to traditional multiplication */
    
    /* Calculates the size of the numbers. */
    m = max(size_in_base(num1), size_in_base(num2))
    m2 = floor(m / 2) 
    /* m2 = ceil (m / 2) will also work */
    
    /* Split the digit sequences in the middle. */
    high1, low1 = split_at(num1, m2)
    high2, low2 = split_at(num2, m2)
    
    /* 3 recursive calls made to numbers approximately half the size. */
    z0 = karatsuba(low1, low2)
    z3 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)
    
    return (z2 × BASE ^ (m2 × 2)) + ((z3 - z2 - z0) × BASE ^ m2) + z0
```

An issue that occurs with this implementation is that each of the factors $(x_{1}+x_{0})$ and $(y_{1}+y_{0})$ of $z_{3}$ may require more than `m2` digits to represent, and $z_{3}$ itself may overflow (produce a result in the range $B^{m}\leq z_{3}<2B^{m}$ ). This need for a multiplier with one extra bit can be avoided using the alternative form mentioned above:

$z_{1}=z_{2}+z_{0}-(x_{1}-x_{0})(y_{1}-y_{0}).$

The computation of $z_{4}=(x_{1}-x_{0})(y_{1}-y_{0})$ will produce a result in the range of $-B^{m}<z_{4}<B^{m}$ . This method also needs one extra bit, to encode the sign of the potentially negative numbers, but it can be handled by computing the absolute value $\left|z_{4}\right|=\left|x_{1}-x_{0}\right|\left|y_{1}-y_{0}\right|$ with a fixed-width multiplier, computing the sign of $z_{4}$ separately, and finally summing

$z_{1}=z_{2}+z_{0}\pm \left|z_{4}\right|.$
