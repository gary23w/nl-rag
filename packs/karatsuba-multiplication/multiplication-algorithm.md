---
title: "Multiplication algorithm"
source: https://en.wikipedia.org/wiki/Multiplication_algorithm
domain: karatsuba-multiplication
license: CC-BY-SA-4.0
tags: karatsuba algorithm, fast multiplication, toom cook multiplication, divide and conquer
fetched: 2026-07-02
---

# Multiplication algorithm

A **multiplication algorithm** is an algorithm (or method) to multiply two numbers. Depending on the size of the numbers, different algorithms are more efficient than others. Numerous algorithms are known and there has been much research into the topic.

The oldest and simplest method, known since antiquity as **long multiplication** or **grade-school multiplication**, consists of multiplying every digit in the first number by every digit in the second and adding the results. This has a time complexity of $O(n^{2})$ , where *n* is the number of digits. When done by hand, this may also be reframed as grid method multiplication or lattice multiplication. In software, this may be called "shift and add" due to bitshifts and addition being the only two operations needed.

In 1960, Anatoly Karatsuba discovered Karatsuba multiplication, unleashing a flood of research into fast multiplication algorithms. This method uses three multiplications rather than four to multiply two two-digit numbers. (A variant of this can also be used to multiply complex numbers quickly.) Done recursively, this has a time complexity of $O(n^{\log _{2}3})$ . Splitting numbers into more than two parts results in Toom–Cook multiplication; for example, using three parts results in the **Toom-3** algorithm. Using many parts can set the exponent arbitrarily close to 1, but the constant factor also grows, making it impractical.

In 1968, the Schönhage–Strassen algorithm, which makes use of a Fourier transform over a modulus, was discovered. It has a time complexity of $O(n\log n\log \log n)$ . In 2007, Martin Fürer proposed an algorithm with complexity $O(n\log n2^{\Theta (\log ^{*}n)})$ . In 2014, Harvey, Joris van der Hoeven, and Lecerf proposed one with complexity $O(n\log n2^{3\log ^{*}n})$ , thus making the implicit constant explicit; this was improved to $O(n\log n2^{2\log ^{*}n})$ in 2018. Lastly, in 2019, Harvey and van der Hoeven came up with a galactic algorithm with complexity $O(n\log n)$ . This matches a guess by Schönhage and Strassen that this would be the optimal bound, although this remains a conjecture today.

Integer multiplication algorithms can also be used to multiply polynomials by means of the method of Kronecker substitution.

## Long multiplication

If a positional numeral system is used, a natural way of multiplying numbers is taught in schools as **long multiplication**, sometimes called **grade-school multiplication**, sometimes called the **Standard Algorithm**: multiply the multiplicand by each digit of the multiplier and then add up all the properly shifted results. It requires memorization of the multiplication table for single digits.

This is the usual algorithm for multiplying larger numbers by hand in base 10. A person doing long multiplication on paper will write down all the products and then add them together; an abacus-user will sum the products as soon as each one is computed.

### Example

This example uses *long multiplication* to multiply 23,958,233 (multiplicand) by 5,830 (multiplier) and arrives at 139,676,498,390 for the result (product).

```
      23958233
×         5830
———————————————
      00000000 ( =  23,958,233 ×     0)
     71874699  ( =  23,958,233 ×    30)
   191665864   ( =  23,958,233 ×   800)
+ 119791165    ( =  23,958,233 × 5,000)
———————————————
  139676498390 ( = 139,676,498,390)
```

#### Other notations

In some countries such as Germany, the above multiplication is depicted similarly but with the original product kept horizontal and computation starting with the first digit of the multiplier:

```
23958233 · 5830
———————————————
   119791165
    191665864
      71874699
       00000000
———————————————
   139676498390
```

Below pseudocode describes the process of above multiplication. It keeps only one row to maintain the sum which finally becomes the result. Note that the '+=' operator is used to denote sum to existing value and store operation (akin to languages such as Java and C) for compactness.

```mw
multiply(a[1..p], b[1..q], base)                            // Operands containing rightmost digits at index 1
  product = [1..p+q]                                        // Allocate space for result
  for b_i = 1 to q                                          // for all digits in b
    carry = 0
    for a_i = 1 to p                                        // for all digits in a
      product[a_i + b_i - 1] += carry + a[a_i] * b[b_i]
      carry = product[a_i + b_i - 1] / base
      product[a_i + b_i - 1] = product[a_i + b_i - 1] mod base
    product[b_i + p] = carry                               // last digit comes from final carry
  return product
```

### Usage in computers

Some chips implement long multiplication, in hardware or in microcode, for various integer and floating-point word sizes. In arbitrary-precision arithmetic, it is common to use long multiplication with the base set to 2*w*, where *w* is the number of bits in a word, for multiplying relatively small numbers. To multiply two numbers with *n* digits using this method, one needs about *n*2 operations. More formally, multiplying two *n*-digit numbers using long multiplication requires Θ(*n*2) single-digit operations (additions and multiplications).

When implemented in software, long multiplication algorithms must deal with overflow during additions, which can be expensive. A typical solution is to represent the number in a small base, *b*, such that, for example, 8*b* is a representable machine integer. Several additions can then be performed before an overflow occurs. When the number becomes too large, we add part of it to the result, or we carry and map the remaining part back to a number that is less than *b*. This process is called *normalization*. Richard Brent used this approach in his Fortran package, MP.

Computers initially used a very similar algorithm to long multiplication in base 2, but modern processors have optimized circuitry for fast multiplications using more efficient algorithms, at the price of a more complex hardware realization. In base two, long multiplication is sometimes called **"shift and add"**, because the algorithm simplifies and just consists of shifting left (multiplying by powers of two) and adding. Most currently available microprocessors implement this or other similar algorithms (such as Booth encoding) for various integer and floating-point sizes in hardware multipliers or in microcode.

On currently available processors, a bit-wise shift instruction is usually (but not always) faster than a multiply instruction and can be used to multiply (shift left) and divide (shift right) by powers of two. Multiplication by a constant and division by a constant can be implemented using a sequence of shifts and adds or subtracts. For example, there are several ways to multiply by 10 using only bit-shift and addition.

```mw
 ((x << 2) + x) << 1 # Here 10*x is computed as (x*2^2 + x)*2
 (x << 3) + (x << 1) # Here 10*x is computed as x*2^3 + x*2
```

In some cases such sequences of shifts and adds or subtracts will outperform hardware multipliers and especially dividers. A division by a number of the form $2^{n}$ or $2^{n}\pm 1$ often can be converted to such a short sequence.

## Algorithms for multiplying by hand

In addition to the standard long multiplication, there are several other methods used to perform multiplication by hand. Such algorithms may be devised for speed, ease of calculation, or educational value, particularly when computers or multiplication tables are unavailable.

### Grid method

The grid method (or box method) is an introductory method for multiple-digit multiplication that is often taught to pupils at primary school or elementary school. It has been a standard part of the national primary school mathematics curriculum in England and Wales since the late 1990s.

Both factors are broken up ("partitioned") into their hundreds, tens and units parts, and the products of the parts are then calculated explicitly in a relatively simple multiplication-only stage, before these contributions are then totalled to give the final answer in a separate addition stage.

The calculation 34 × 13, for example, could be computed using the grid:

```
  300
   40
   90
 + 12
 ————
  442
```

| × | 30 | 4 |
|---|---|---|
| 10 | 300 | 40 |
| 3 | 90 | 12 |

followed by addition to obtain 442, either in a single sum (see right), or through forming the row-by-row totals

(300 + 40) + (90 + 12) = 340 + 102 = 442.

This calculation approach (though not necessarily with the explicit grid arrangement) is also known as the partial products algorithm. Its essence is the calculation of the simple multiplications separately, with all addition being left to the final gathering-up stage.

The grid method can in principle be applied to factors of any size, although the number of sub-products becomes cumbersome as the number of digits increases. Nevertheless, it is seen as a usefully explicit method to introduce the idea of multiple-digit multiplications; and, in an age when most multiplication calculations are done using a calculator or a spreadsheet, it may in practice be the only multiplication algorithm that some students will ever need.

### Lattice multiplication

Lattice, or sieve, multiplication is algorithmically equivalent to long multiplication. It requires the preparation of a lattice (a grid drawn on paper) which guides the calculation and separates all the multiplications from the additions. It was introduced to Europe in 1202 in Fibonacci's Liber Abaci. Fibonacci described the operation as mental, using his right and left hands to carry the intermediate calculations. Matrakçı Nasuh presented 6 different variants of this method in this 16th-century book, Umdet-ul Hisab. It was widely used in Enderun schools across the Ottoman Empire. Napier's bones, or Napier's rods also used this method, as published by Napier in 1617, the year of his death.

As shown in the example, the multiplicand and multiplier are written above and to the right of a lattice, or a sieve. It is found in Muhammad ibn Musa al-Khwarizmi's "Arithmetic", one of Leonardo's sources mentioned by Sigler, author of "Fibonacci's Liber Abaci", 2002.

- During the multiplication phase, the lattice is filled in with two-digit products of the corresponding digits labeling each row and column: the tens digit goes in the top-left corner.
- During the addition phase, the lattice is summed on the diagonals.
- Finally, if a carry phase is necessary, the answer as shown along the left and bottom sides of the lattice is converted to normal form by carrying ten's digits as in long addition or multiplication.

#### Example

The pictures on the right show how to calculate 345 × 12 using lattice multiplication. As a more complicated example, consider the picture below displaying the computation of 23,958,233 multiplied by 5,830 (multiplier); the result is 139,676,498,390. Notice 23,958,233 is along the top of the lattice and 5,830 is along the right side. The products fill the lattice and the sum of those products (on the diagonal) are along the left and bottom sides. Then those sums are totaled as shown.

| 2 3 9 5 8 2 3 3 +---+---+---+---+---+---+---+---+- \|1 /\|1 /\|4 /\|2 /\|4 /\|1 /\|1 /\|1 /\| \| / \| / \| / \| / \| / \| / \| / \| / \| 5 01\|/ 0\|/ 5\|/ 5\|/ 5\|/ 0\|/ 0\|/ 5\|/ 5\| +---+---+---+---+---+---+---+---+- \|1 /\|2 /\|7 /\|4 /\|6 /\|1 /\|2 /\|2 /\| \| / \| / \| / \| / \| / \| / \| / \| / \| 8 02\|/ 6\|/ 4\|/ 2\|/ 0\|/ 4\|/ 6\|/ 4\|/ 4\| +---+---+---+---+---+---+---+---+- \|0 /\|0 /\|2 /\|1 /\|2 /\|0 /\|0 /\|0 /\| \| / \| / \| / \| / \| / \| / \| / \| / \| 3 17\|/ 6\|/ 9\|/ 7\|/ 5\|/ 4\|/ 6\|/ 9\|/ 9\| +---+---+---+---+---+---+---+---+- \|0 /\|0 /\|0 /\|0 /\|0 /\|0 /\|0 /\|0 /\| \| / \| / \| / \| / \| / \| / \| / \| / \| 0 24\|/ 0\|/ 0\|/ 0\|/ 0\|/ 0\|/ 0\|/ 0\|/ 0\| +---+---+---+---+---+---+---+---+- 26 15 13 18 17 13 09 00 | 01 002 0017 00024 000026 0000015 00000013 000000018 0000000017 00000000013 000000000009 0000000000000 ————————————— 139676498390 |
|---|---|
| = 139,676,498,390 |   |

### Russian peasant multiplication

The binary method is also known as peasant multiplication, because it has been widely used by people who are classified as peasants and thus have not memorized the multiplication tables required for long multiplication. The algorithm was in use in ancient Egypt. Its main advantages are that it can be taught quickly, requires no memorization, and can be performed using tokens, such as poker chips, if paper and pencil aren't available. The disadvantage is that it takes more steps than long multiplication, so it can be unwieldy for large numbers.

#### Description

One column contains the numbers that result from repeatedly halving the multiplier while ignoring the remainder. Another column beside it contains the results of repeatedly doubling the multiplicand. The product is evaluated by crossing out each row where the first number ends in an even digit, then summing up the remaining numbers in the second column in order to obtain the product.

#### Examples

This example uses peasant multiplication to multiply 11 by 3 to arrive at a result of 33.

```
Decimal:     Binary:
11   3       1011  11
5    6       101  110
2   12       10  1100
1   24       1  11000
    ——         ——————
    33         100001
```

Describing the steps explicitly:

- 11 and 3 are written at the top
- 11 is halved (5.5) and 3 is doubled (6). The fractional portion is discarded (5.5 becomes 5).
- 5 is halved (2.5) and 6 is doubled (12). The fractional portion is discarded (2.5 becomes 2). The figure in the left column (2) is **even**, so the figure in the right column (12) is discarded.
- 2 is halved (1) and 12 is doubled (24).
- All not-scratched-out values are summed: 3 + 6 + 24 = 33.

The method works because multiplication is distributive, so:

${\begin{aligned}3\times 11&=3\times (1\times 2^{0}+1\times 2^{1}+0\times 2^{2}+1\times 2^{3})\\&=3\times (1+2+8)\\&=3+6+24\\&=33.\end{aligned}}$

A more complicated example, using the figures from the earlier examples (23,958,233 and 5,830):

```
Decimal:             Binary:
5830  23958233       1011011000110  1011011011001001011011001
2915  47916466       101101100011  10110110110010010110110010
1457  95832932       10110110001  101101101100100101101100100
728  191665864       1011011000  1011011011001001011011001000
364  383331728       101101100  10110110110010010110110010000
182  766663456       10110110  101101101100100101101100100000
91  1533326912       1011011  1011011011001001011011001000000
45  3066653824       101101  10110110110010010110110010000000
22  6133307648       10110  101101101100100101101100100000000
11 12266615296       1011  1011011011001001011011001000000000
5  24533230592       101  10110110110010010110110010000000000
2  49066461184       10  101101101100100101101100100000000000
1  98132922368       1  1011011011001001011011001000000000000
  ————————————          1022143253354344244353353243222210110 (before carry)
  139676498390         10000010000101010111100011100111010110
```

### Quarter square multiplication

This formula can in some cases be used, to make multiplication tasks easier to complete:

${\frac {\left(x+y\right)^{2}}{4}}-{\frac {\left(x-y\right)^{2}}{4}}=\left({\frac {x+y}{2}}\right)^{2}-\left({\frac {x-y}{2}}\right)^{2}=xy$

In the case where x and y are integers, we have that

$(x+y)^{2}\equiv (x-y)^{2}{\bmod {4}}$

because $x+y$ and $x-y$ are either both even or both odd. This means that

${\begin{aligned}xy&={\frac {1}{4}}(x+y)^{2}-{\frac {1}{4}}(x-y)^{2}\\&=\left((x+y)^{2}{\text{ div }}4\right)-\left((x-y)^{2}{\text{ div }}4\right)\end{aligned}}$

and it's sufficient to (pre-)compute the integral part of squares divided by 4 like in the following example.

#### Examples

Below is a lookup table of quarter squares with the remainder discarded for the digits 0 through 18; this allows for the multiplication of numbers up to 9×9.

n

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

⌊

n

2

/4⌋

0

0

1

2

4

6

9

12

16

20

25

30

36

42

49

56

64

72

81

For example, when multiplying 9 by 3, evaluating the sum and difference of those numbers yield 12 and 6 respectively. Looking both those values up on the table yields 36 and 9, the difference of which is 27, which is the product of 9 and 3.

#### History of quarter square multiplication

In prehistoric time, quarter square multiplication involved floor function; that some sources attribute to Babylonian mathematics (2000–1600 BC).

Antoine Voisin published a table of quarter squares from 1 to 1000 in 1817 as an aid in multiplication. A larger table of quarter squares from 1 to 100000 was published by Samuel Laundy in 1856, and a table from 1 to 200000 by Joseph Blater in 1888.

Quarter square multipliers were used in analog computers to form an analog signal that was the product of two analog input signals. In this application, the sum and difference of two input voltages are formed using operational amplifiers. The square of each of these is approximated using piecewise linear circuits. Finally the difference of the two squares is formed and scaled by a factor of one fourth using yet another operational amplifier.

In 1980, Everett L. Johnson proposed using the quarter square method in a digital multiplier. To form the product of two 8-bit integers, for example, the digital device forms the sum and difference, looks both quantities up in a table of squares, takes the difference of the results, and divides by four by shifting two bits to the right. For 8-bit integers the table of quarter squares will have 29−1=511 entries (one entry for the full range 0..510 of possible sums, the differences using only the first 256 entries in range 0..255) or 29−1=511 entries (using for negative differences the technique of 2-complements and 9-bit masking, which avoids testing the sign of differences), each entry being 16-bit wide (the entry values are from (0²/4)=0 to (510²/4)=65025).

The quarter square multiplier technique has benefited 8-bit systems that do not have any support for a hardware multiplier. Charles Putney implemented this for the 6502.

## Computational complexity of multiplication

Unsolved problem in computer science

What is the fastest algorithm for multiplication of two

n

-digit numbers?

More unsolved problems in computer science

A line of research in theoretical computer science is about the number of single-bit arithmetic operations necessary to multiply two n -bit integers. This is known as the computational complexity of multiplication. Usual algorithms done by hand have asymptotic complexity of $O(n^{2})$ , but in 1960 Anatoly Karatsuba discovered that better complexity was possible (with the Karatsuba algorithm).

Currently, the algorithm with the best computational complexity is a 2019 algorithm of David Harvey and Joris van der Hoeven, which uses the strategies of using number-theoretic transforms introduced with the Schönhage–Strassen algorithm to multiply integers using only $O(n\log n)$ operations. This is conjectured to be the best possible algorithm, but lower bounds of $\Omega (n\log n)$ are not known.

### Karatsuba multiplication

Karatsuba multiplication is an O(*n*log23) ≈ O(*n*1.585) divide and conquer algorithm, that uses recursion to merge subcalculations.

By rewriting the formula, one makes it possible to do sub calculations / recursion. By doing recursion, one can solve this in a fast manner.

Let x and y be represented as n -digit strings in some base B . For any positive integer m less than n , one can write the two given numbers as

$x=x_{1}B^{m}+x_{0},$

$y=y_{1}B^{m}+y_{0},$

where $x_{0}$ and $y_{0}$ are less than $B^{m}$ . The product is then

${\begin{aligned}xy&=(x_{1}B^{m}+x_{0})(y_{1}B^{m}+y_{0})\\&=x_{1}y_{1}B^{2m}+(x_{1}y_{0}+x_{0}y_{1})B^{m}+x_{0}y_{0}\\&=z_{2}B^{2m}+z_{1}B^{m}+z_{0},\\\end{aligned}}$

where

$z_{2}=x_{1}y_{1},$

$z_{1}=x_{1}y_{0}+x_{0}y_{1},$

$z_{0}=x_{0}y_{0}.$

These formulae require four multiplications and were known to Charles Babbage. Karatsuba observed that $xy$ can be computed in only three multiplications, at the cost of a few extra additions. With $z_{0}$ and $z_{2}$ as before one can observe that

${\begin{aligned}z_{1}&=x_{1}y_{0}+x_{0}y_{1}\\&=x_{1}y_{0}+x_{0}y_{1}+x_{1}y_{1}-x_{1}y_{1}+x_{0}y_{0}-x_{0}y_{0}\\&=x_{1}y_{0}+x_{0}y_{0}+x_{0}y_{1}+x_{1}y_{1}-x_{1}y_{1}-x_{0}y_{0}\\&=(x_{1}+x_{0})y_{0}+(x_{0}+x_{1})y_{1}-x_{1}y_{1}-x_{0}y_{0}\\&=(x_{1}+x_{0})(y_{0}+y_{1})-x_{1}y_{1}-x_{0}y_{0}\\&=(x_{1}+x_{0})(y_{1}+y_{0})-z_{2}-z_{0}.\\\end{aligned}}$

Because of the overhead of recursion, Karatsuba's multiplication is slower than long multiplication for small values of *n*; typical implementations therefore switch to long multiplication for small values of *n*.

#### General case with multiplication of N numbers

By exploring patterns after expansion, one see following:

${\begin{alignedat}{5}(x_{1}B^{m}+x_{0})(y_{1}B^{m}+y_{0})(z_{1}B^{m}+z_{0})(a_{1}B^{m}+a_{0})&=a_{1}x_{1}y_{1}z_{1}B^{4m}&+a_{1}x_{1}y_{1}z_{0}B^{3m}&+a_{1}x_{1}y_{0}z_{1}B^{3m}&+a_{1}x_{0}y_{1}z_{1}B^{3m}\\&+a_{0}x_{1}y_{1}z_{1}B^{3m}&+a_{1}x_{1}y_{0}z_{0}B^{2m}&+a_{1}x_{0}y_{1}z_{0}B^{2m}&+a_{0}x_{1}y_{1}z_{0}B^{2m}\\&+a_{1}x_{0}y_{0}z_{1}B^{2m}&+a_{0}x_{1}y_{0}z_{1}B^{2m}&+a_{0}x_{0}y_{1}z_{1}B^{2m}&+a_{1}x_{0}y_{0}z_{0}B^{m{\phantom {1}}}\\&+a_{0}x_{1}y_{0}z_{0}B^{m{\phantom {1}}}&+a_{0}x_{0}y_{1}z_{0}B^{m{\phantom {1}}}&+a_{0}x_{0}y_{0}z_{1}B^{m{\phantom {1}}}&+a_{0}x_{0}y_{0}z_{0}{\phantom {B^{1m}}}\end{alignedat}}$

Each summand is associated to a unique binary number from 0 to $2^{N+1}-1$ , for example $a_{1}x_{1}y_{1}z_{1}\longleftrightarrow 1111,\ a_{1}x_{0}y_{1}z_{0}\longleftrightarrow 1010$ etc. Furthermore; B is powered to number of 1, in this binary string, multiplied with m.

If we express this in fewer terms, we get:

$\prod _{j=1}^{N}(x_{j,1}B^{m}+x_{j,0})=\sum _{i=1}^{2^{N+1}-1}\prod _{j=1}^{N}x_{j,c(i,j)}B^{m\sum _{j=1}^{N}c(i,j)}=\sum _{j=0}^{N}z_{j}B^{jm}$ , where $c(i,j)$ means digit in number i at position j. Notice that $c(i,j)\in \{0,1\}$

${\begin{aligned}z_{0}&=\prod _{j=1}^{N}x_{j,0}\\z_{N}&=\prod _{j=1}^{N}x_{j,1}\\z_{N-1}&=\prod _{j=1}^{N}(x_{j,0}+x_{j,1})-\sum _{i\neq N-1}^{N}z_{i}\end{aligned}}$

#### History

Karatsuba's algorithm was the first known algorithm for multiplication that is asymptotically faster than long multiplication, and can thus be viewed as the starting point for the theory of fast multiplications.

### Toom–Cook

Another method of multiplication is called Toom–Cook or Toom-3. The Toom–Cook method splits each number to be multiplied into multiple parts. The Toom–Cook method is one of the generalizations of the Karatsuba method. A three-way Toom–Cook can do a size-*3N* multiplication for the cost of five size-*N* multiplications. This accelerates the operation by a factor of 9/5, while the Karatsuba method accelerates it by 4/3.

Although using more and more parts can reduce the time spent on recursive multiplications further, the overhead from additions and digit management also grows. For this reason, the method of Fourier transforms is typically faster for numbers with several thousand digits, and asymptotically faster for even larger numbers.

### Schönhage–Strassen

Every number in base B, can be written as a polynomial:

$X=\sum _{i=0}^{N}{x_{i}B^{i}}$

Furthermore, multiplication of two numbers could be thought of as a product of two polynomials:

$XY=(\sum _{i=0}^{N}{x_{i}B^{i}})\,(\sum _{j=0}^{N}{y_{i}B^{j}})$

Since the coefficient of ⁠ $B^{k}$ ⁠ in the product is $z_{k}=\sum _{(i,j):i+j=k}{x_{i}y_{j}}=\sum _{i=0}^{k}{x_{i}y_{k-i}},$ one has a convolution, and one can use the fast Fourier transform (FFT): ${\hat {f}}(XY)={\hat {f}}(\sum _{i=0}^{k}{x_{i}y_{k-i}})={\hat {f}}(X)\cdot {\hat {f}}(Y).$

Therefore, the multiplication is reduced to a FFT, ⁠ N ⁠ multiplications, and an inverse FFT. It results a time complexity of *O*(*n* log(*n*) log(log *n*)).

#### History

The algorithm was invented by Strassen (1968). It was made practical and theoretical guarantees were provided in 1971 by Schönhage and Strassen resulting in the Schönhage–Strassen algorithm.

### Further improvements

In 2007 the asymptotic complexity of integer multiplication was improved by the Swiss mathematician Martin Fürer of Pennsylvania State University to ${\textstyle O(n\log n\cdot {2}^{\Theta (\log ^{*}(n))})}$ using Fourier transforms over complex numbers, where log* denotes the iterated logarithm. Anindya De, Chandan Saha, Piyush Kurur and Ramprasad Saptharishi gave a similar algorithm using modular arithmetic in 2008 achieving the same running time. In context of the above material, what these latter authors have achieved is to find *N* much less than 23*k* + 1, so that *Z*/*NZ* has a (2*m*)th root of unity. This speeds up computation and reduces the time complexity. However, these latter algorithms are only faster than Schönhage–Strassen for impractically large inputs.

In 2014, Harvey, Joris van der Hoeven and Lecerf gave a new algorithm that achieves a running time of $O(n\log n\cdot 2^{3\log ^{*}n})$ , making explicit the implied constant in the $O(\log ^{*}n)$ exponent. They also proposed a variant of their algorithm which achieves $O(n\log n\cdot 2^{2\log ^{*}n})$ but whose validity relies on standard conjectures about the distribution of Mersenne primes. In 2016, Covanov and Thomé proposed an integer multiplication algorithm based on a generalization of Fermat primes that conjecturally achieves a complexity bound of $O(n\log n\cdot 2^{2\log ^{*}n})$ . This matches the 2015 conditional result of Harvey, van der Hoeven, and Lecerf but uses a different algorithm and relies on a different conjecture. In 2018, Harvey and van der Hoeven used an approach based on the existence of short lattice vectors guaranteed by Minkowski's theorem to prove an unconditional complexity bound of $O(n\log n\cdot 2^{2\log ^{*}n})$ .

In March 2019, David Harvey and Joris van der Hoeven announced their discovery of an *O*(*n* log *n*) multiplication algorithm. It was published in the *Annals of Mathematics* in 2021. Because Schönhage and Strassen predicted that *n* log(*n*) is the "best possible" result, Harvey said: "... our work is expected to be the end of the road for this problem, although we don't know yet how to prove this rigorously." However, the new algorithm is highly impractical: it is faster than the Schönhage–Strassen algorithm only if the number of digits exceeds

${\begin{aligned}2^{{1729}^{12}}&=2^{713\,739\,807\,325\,663\,489\,766\,475\,852\,620\,783\,120\,641}\\&\approx 4.145331\times 10^{214\,857\,091\,104\,455\,254\,035\,802\,532\,723\,729\,912\,717}\\&\approx 10^{2.148571\times 10^{38}}.\end{aligned}}$

### Lower bounds

There is a trivial lower bound of Ω(*n*) for multiplying two *n*-bit numbers on a single processor; no matching algorithm (on conventional machines, that is on Turing equivalent machines) nor any sharper lower bound is known. The Hartmanis–Stearns conjecture would imply that $O(n)$ cannot be achieved. Multiplication lies outside of AC0[*p*] for any prime *p*, meaning there is no family of constant-depth, polynomial (or even subexponential) size circuits using AND, OR, NOT, and MOD*p* gates that can compute a product. This follows from a constant-depth reduction of MOD*q* to multiplication. Lower bounds for multiplication are also known for some classes of branching programs.

## Complex number multiplication

Complex multiplication normally involves four multiplications and two additions.

$(a+bi)(c+di)=(ac-bd)+(bc+ad)i.$

Or

${\begin{array}{c|c|c}\times &a&bi\\\hline c&ac&bci\\\hline di&adi&-bd\end{array}}$

As observed by Peter Ungar in 1963, one can reduce the number of multiplications to three, using essentially the same computation as Karatsuba's algorithm. The product (*a* + *bi*) · (*c* + *di*) can be calculated in the following way.

k

1

=

c

· (

a

+

b

)

k

2

=

a

· (

d

−

c

)

k

3

=

b

· (

c

+

d

)

Real part =

k

1

−

k

3

Imaginary part =

k

1

+

k

2

.

This algorithm uses only three multiplications, rather than four, and five additions or subtractions rather than two. If a multiply is more expensive than three adds or subtracts, as when calculating by hand, then there is a gain in speed. On modern computers a multiply and an add can take about the same time so there may be no speed gain. There is a trade-off in that there may be some loss of precision when using floating point.

For fast Fourier transforms (FFTs) (or any linear transformation) the complex multiplies are by constant coefficients *c* + *di* (called twiddle factors in FFTs), in which case two of the additions (*d*−*c* and *c*+*d*) can be precomputed. Hence, only three multiplies and three adds are required. However, trading off a multiplication for an addition in this way may no longer be beneficial with modern floating-point units.

## Polynomial multiplication

All the above multiplication algorithms can also be expanded to multiply polynomials. Alternatively the Kronecker substitution technique may be used to convert the problem of multiplying polynomials into a single binary multiplication.

Long multiplication methods can be generalised to allow the multiplication of algebraic formulae:

```
 14ac - 3ab + 2 multiplied by ac - ab + 1
```

```
 14ac  -3ab   2
   ac   -ab   1
 ————————————————————
 14a2c2  -3a2bc   2ac
        -14a2bc         3 a2b2  -2ab
                 14ac           -3ab   2
 ———————————————————————————————————————
 14a2c2 -17a2bc   16ac  3a2b2    -5ab  +2
 =======================================
```

As a further example of column based multiplication, consider multiplying 23 long tons (t), 12 hundredweight (cwt) and 2 quarters (qtr) by 47. This example uses avoirdupois measures: 1 t = 20 cwt, 1 cwt = 4 qtr.

```
    t    cwt  qtr
   23     12    2
               47 ×
 ————————————————
1. Multiply everything by 47
 1081    564   94
 ————————————————
2a. Carry qtr & add to cwt (94 = 23 × 4 + 2)
        (564)  94
          23    2
        —————
         587    2
2b. Carry cwt & add to t (587 = 29 × 20 + 7)
(1081)   587    2
   29      7
 ————————————————
3. Final add
 1110      7    2
 =================  Answer: 1110 ton 7 cwt 2 qtr
```

The same layout and methods can be used for any traditional measurements and non-decimal currencies such as the old British £sd system.
