---
title: "BCH code"
source: https://en.wikipedia.org/wiki/BCH_code
domain: coding-theory
license: CC-BY-SA-4.0
tags: coding theory, linear code, hamming distance, convolutional code
fetched: 2026-07-02
---

# BCH code

In coding theory, the **Bose–Chaudhuri–Hocquenghem codes** (**BCH codes**) form a class of cyclic error-correcting codes that are constructed using polynomials over a finite field (also called a *Galois field*). BCH codes were invented in 1959 by French mathematician Alexis Hocquenghem, and independently in 1960 by Raj Chandra Bose and D. K. Ray-Chaudhuri. The name *Bose–Chaudhuri–Hocquenghem* (and the acronym *BCH*) arises from the initials of the inventors' surnames (mistakenly, in the case of Ray-Chaudhuri).

One of the key features of BCH codes is that during code design, there is a precise control over the number of symbol errors correctable by the code. In particular, it is possible to design binary BCH codes that can correct multiple bit errors. Another advantage of BCH codes is the ease with which they can be decoded, namely, via an algebraic method known as syndrome decoding. This simplifies the design of the decoder for these codes, using small low-power electronic hardware.

BCH codes are used in applications such as satellite communications, compact disc players, DVDs, disk drives, USB flash drives, solid-state drives, and two-dimensional bar codes.

## Definition and illustration

### Primitive narrow-sense BCH codes

Given a prime number q and prime power *q**m* with positive integers m and d such that *d* ≤ *q**m* − 1, a primitive narrow-sense BCH code over the finite field (or Galois field) GF(*q*) with code length *n* = *q**m* − 1 and distance at least d is constructed by the following method.

Let α be a primitive element of GF(*q**m*). For any positive integer i, let *m**i*(*x*) be the minimal polynomial with coefficients in GF(*q*) of α*i*. The generator polynomial of the BCH code is defined as the least common multiple *g*(*x*) = lcm(*m*1(*x*),…,*m**d* − 1(*x*)). It can be seen that *g*(*x*) is a polynomial with coefficients in GF(*q*) and divides *x**n* − 1. Therefore, the polynomial code defined by *g*(*x*) is a cyclic code.

#### Example

Let *q* = 2 and *m* = 4 (therefore *n* = 15). We will consider different values of d for GF(16) = GF(24) based on the reducing polynomial *z*4 + *z* + 1, using primitive element *α*(*z*) = *z*. There are fourteen minimum polynomials *m**i*(*x*) with coefficients in GF(2) satisfying

$m_{i}\left(\alpha ^{i}\right){\bmod {\left(z^{4}+z+1\right)}}=0.$

The minimal polynomials are

${\begin{aligned}m_{1}(x)&=m_{2}(x)=m_{4}(x)=m_{8}(x)=x^{4}+x+1,\\m_{3}(x)&=m_{6}(x)=m_{9}(x)=m_{12}(x)=x^{4}+x^{3}+x^{2}+x+1,\\m_{5}(x)&=m_{10}(x)=x^{2}+x+1,\\m_{7}(x)&=m_{11}(x)=m_{13}(x)=m_{14}(x)=x^{4}+x^{3}+1.\end{aligned}}$

The BCH code with $d=2,3$ has the generator polynomial

$g(x)={\rm {lcm}}(m_{1}(x),m_{2}(x))=m_{1}(x)=x^{4}+x+1.\,$

It has minimal Hamming distance at least 3 and corrects up to one error. Since the generator polynomial is of degree 4, this code has 11 data bits and 4 checksum bits. It is also denoted as: **(15, 11) BCH** code.

The BCH code with $d=4,5$ has the generator polynomial

${\begin{aligned}g(x)&={\rm {lcm}}(m_{1}(x),m_{2}(x),m_{3}(x),m_{4}(x))=m_{1}(x)m_{3}(x)\\&=\left(x^{4}+x+1\right)\left(x^{4}+x^{3}+x^{2}+x+1\right)=x^{8}+x^{7}+x^{6}+x^{4}+1.\end{aligned}}$

It has minimal Hamming distance at least 5 and corrects up to two errors. Since the generator polynomial is of degree 8, this code has 7 data bits and 8 checksum bits. It is also denoted as: **(15, 7) BCH** code.

The BCH code with $d=6,7$ has the generator polynomial

${\begin{aligned}g(x)&={\rm {lcm}}(m_{1}(x),m_{2}(x),m_{3}(x),m_{4}(x),m_{5}(x),m_{6}(x))=m_{1}(x)m_{3}(x)m_{5}(x)\\&=\left(x^{4}+x+1\right)\left(x^{4}+x^{3}+x^{2}+x+1\right)\left(x^{2}+x+1\right)=x^{10}+x^{8}+x^{5}+x^{4}+x^{2}+x+1.\end{aligned}}$

It has minimal Hamming distance at least 7 and corrects up to three errors. Since the generator polynomial is of degree 10, this code has 5 data bits and 10 checksum bits. It is also denoted as: **(15, 5) BCH** code. (This particular generator polynomial has a real-world application, in the "format information" of the QR code.)

The BCH code with $d=8$ and higher has the generator polynomial

${\begin{aligned}g(x)&={\rm {lcm}}(m_{1}(x),m_{2}(x),...,m_{14}(x))=m_{1}(x)m_{3}(x)m_{5}(x)m_{7}(x)\\&=\left(x^{4}+x+1\right)\left(x^{4}+x^{3}+x^{2}+x+1\right)\left(x^{2}+x+1\right)\left(x^{4}+x^{3}+1\right)=x^{14}+x^{13}+x^{12}+\cdots +x^{2}+x+1.\end{aligned}}$

This code has minimal Hamming distance 15 and corrects 7 errors. It has 1 data bit and 14 checksum bits. It is also denoted as: **(15, 1) BCH** code. In fact, this code has only two codewords: 000000000000000 and 111111111111111 (a trivial repetition code).

### General BCH codes

General BCH codes differ from primitive narrow-sense BCH codes in two respects.

First, the requirement that $\alpha$ be a primitive element of $\mathrm {GF} (q^{m})$ can be relaxed. By relaxing this requirement, the code length changes from $q^{m}-1$ to $\mathrm {ord} (\alpha ),$ the order of the element $\alpha .$

Second, the consecutive roots of the generator polynomial may run from $\alpha ^{c},\ldots ,\alpha ^{c+d-2}$ instead of $\alpha ,\ldots ,\alpha ^{d-1}.$

**Definition.** Fix a finite field $GF(q),$ where q is a prime power. Choose positive integers $m,n,d,c$ such that $2\leq d\leq n,$ ${\rm {gcd}}(n,q)=1,$ and m is the multiplicative order of q modulo $n.$

As before, let $\alpha$ be a primitive n th root of unity in $GF(q^{m}),$ and let $m_{i}(x)$ be the minimal polynomial over $GF(q)$ of $\alpha ^{i}$ for all $i.$ The generator polynomial of the BCH code is defined as the least common multiple $g(x)={\rm {lcm}}(m_{c}(x),\ldots ,m_{c+d-2}(x)).$

**Note:** if $n=q^{m}-1$ as in the simplified definition, then ${\rm {gcd}}(n,q)$ is 1, and the order of q modulo n is $m.$ Therefore, the simplified definition is indeed a special case of the general one.

### Special cases

- A BCH code with $c=1$ is called a *narrow-sense BCH code*.
- A BCH code with $n=q^{m}-1$ is called *primitive*.

The generator polynomial $g(x)$ of a BCH code has coefficients from $\mathrm {GF} (q).$ In general, a cyclic code over $\mathrm {GF} (q^{p})$ with $g(x)$ as the generator polynomial is called a BCH code over $\mathrm {GF} (q^{p}).$ The BCH code over $\mathrm {GF} (q^{m})$ and generator polynomial $g(x)$ with successive powers of $\alpha$ as roots is one type of Reed–Solomon code where the decoder (syndromes) alphabet is the same as the channel (data and generator polynomial) alphabet, all elements of $\mathrm {GF} (q^{m})$ . The other type of Reed Solomon code is an original view Reed Solomon code which is not a BCH code.

## Properties

The generator polynomial of a BCH code has degree at most $(d-1)m$ . Moreover, if $q=2$ and $c=1$ , the generator polynomial has degree at most $dm/2$ .

| Proof |
|---|
| Each minimal polynomial $m_{i}(x)$ has degree at most m . Therefore, the least common multiple of $d-1$ of them has degree at most $(d-1)m$ . Moreover, if $q=2,$ then $m_{i}(x)=m_{2i}(x)$ for all i . Therefore, $g(x)$ is the least common multiple of at most $d/2$ minimal polynomials $m_{i}(x)$ for odd indices $i,$ each of degree at most m . |

A BCH code has minimal Hamming distance at least d .

| Proof |
|---|
| Suppose that $p(x)$ is a code word with fewer than d non-zero terms. Then $p(x)=b_{1}x^{k_{1}}+\cdots +b_{d-1}x^{k_{d-1}},{\text{ where }}k_{1}<k_{2}<\cdots <k_{d-1}.$ Recall that $\alpha ^{c},\ldots ,\alpha ^{c+d-2}$ are roots of $g(x),$ hence of $p(x)$ . This implies that $b_{1},\ldots ,b_{d-1}$ satisfy the following equations, for each $i\in \{c,\dotsc ,c+d-2\}$ : $p(\alpha ^{i})=b_{1}\alpha ^{ik_{1}}+b_{2}\alpha ^{ik_{2}}+\cdots +b_{d-1}\alpha ^{ik_{d-1}}=0.$ In matrix form, we have ${\begin{bmatrix}\alpha ^{ck_{1}}&\alpha ^{ck_{2}}&\cdots &\alpha ^{ck_{d-1}}\\\alpha ^{(c+1)k_{1}}&\alpha ^{(c+1)k_{2}}&\cdots &\alpha ^{(c+1)k_{d-1}}\\\vdots &\vdots &&\vdots \\\alpha ^{(c+d-2)k_{1}}&\alpha ^{(c+d-2)k_{2}}&\cdots &\alpha ^{(c+d-2)k_{d-1}}\\\end{bmatrix}}{\begin{bmatrix}b_{1}\\b_{2}\\\vdots \\b_{d-1}\end{bmatrix}}={\begin{bmatrix}0\\0\\\vdots \\0\end{bmatrix}}.$ The determinant of this matrix equals $\left(\prod _{i=1}^{d-1}\alpha ^{ck_{i}}\right)\det {\begin{pmatrix}1&1&\cdots &1\\\alpha ^{k_{1}}&\alpha ^{k_{2}}&\cdots &\alpha ^{k_{d-1}}\\\vdots &\vdots &&\vdots \\\alpha ^{(d-2)k_{1}}&\alpha ^{(d-2)k_{2}}&\cdots &\alpha ^{(d-2)k_{d-1}}\\\end{pmatrix}}=\left(\prod _{i=1}^{d-1}\alpha ^{ck_{i}}\right)\det(V).$ The matrix V is seen to be a Vandermonde matrix, and its determinant is $\det(V)=\prod _{1\leq i<j\leq d-1}\left(\alpha ^{k_{j}}-\alpha ^{k_{i}}\right),$ which is non-zero. It therefore follows that $b_{1},\ldots ,b_{d-1}=0,$ hence $p(x)=0.$ |

A BCH code is cyclic.

| Proof |
|---|
| A polynomial code of length n is cyclic if and only if its generator polynomial divides $x^{n}-1.$ Since $g(x)$ is the minimal polynomial with roots $\alpha ^{c},\ldots ,\alpha ^{c+d-2},$ it suffices to check that each of $\alpha ^{c},\ldots ,\alpha ^{c+d-2}$ is a root of $x^{n}-1.$ This follows immediately from the fact that $\alpha$ is, by definition, an n th root of unity. |

## Encoding

Because any polynomial that is a multiple of the generator polynomial is a valid BCH codeword, BCH encoding is merely the process of finding some polynomial that has the generator as a factor.

The BCH code itself is not prescriptive about the meaning of the coefficients of the polynomial; conceptually, a BCH decoding algorithm's sole concern is to find the valid codeword with the minimal Hamming distance to the received codeword. Therefore, the BCH code may be implemented either as a systematic code or not, depending on how the implementor chooses to embed the message in the encoded polynomial.

### Non-systematic encoding: The message as a factor

The most straightforward way to find a polynomial that is a multiple of the generator is to compute the product of some arbitrary polynomial and the generator. In this case, the arbitrary polynomial can be chosen using the symbols of the message as coefficients.

$s(x)=p(x)g(x)$

As an example, consider the generator polynomial $g(x)=x^{10}+x^{9}+x^{8}+x^{6}+x^{5}+x^{3}+1$ , chosen for use in the (31, 21) binary BCH code used by POCSAG and others. To encode the 21-bit message {101101110111101111101}, we first represent it as a polynomial over $GF(2)$ :

$p(x)=x^{20}+x^{18}+x^{17}+x^{15}+x^{14}+x^{13}+x^{11}+x^{10}+x^{9}+x^{8}+x^{6}+x^{5}+x^{4}+x^{3}+x^{2}+1$

Then, compute (also over $GF(2)$ ):

${\begin{aligned}s(x)&=p(x)g(x)\\&=\left(x^{20}+x^{18}+x^{17}+x^{15}+x^{14}+x^{13}+x^{11}+x^{10}+x^{9}+x^{8}+x^{6}+x^{5}+x^{4}+x^{3}+x^{2}+1\right)\left(x^{10}+x^{9}+x^{8}+x^{6}+x^{5}+x^{3}+1\right)\\&=x^{30}+x^{29}+x^{26}+x^{25}+x^{24}+x^{22}+x^{19}+x^{17}+x^{16}+x^{15}+x^{14}+x^{12}+x^{10}+x^{9}+x^{8}+x^{6}+x^{5}+x^{4}+x^{2}+1\end{aligned}}$

Thus, the transmitted codeword is {1100111010010111101011101110101}.

The receiver can use these bits as coefficients in $s(x)$ and, after error-correction to ensure a valid codeword, can recompute $p(x)=s(x)/g(x)$

### Systematic encoding: The message as a prefix

A systematic code is one in which the message appears verbatim somewhere within the codeword. Therefore, systematic BCH encoding involves first embedding the message polynomial within the codeword polynomial, and then adjusting the coefficients of the remaining (non-message) terms to ensure that $s(x)$ is divisible by $g(x)$ .

This encoding method leverages the fact that subtracting the remainder from a dividend results in a multiple of the divisor. Hence, if we take our message polynomial $p(x)$ as before and multiply it by $x^{n-k}$ (to "shift" the message out of the way of the remainder), we can then use Euclidean division of polynomials to yield:

$p(x)x^{n-k}=q(x)g(x)+r(x)$

Here, we see that $q(x)g(x)$ is a valid codeword. As $r(x)$ is always of degree less than $n-k$ (which is the degree of $g(x)$ ), we can safely subtract it from $p(x)x^{n-k}$ without altering any of the message coefficients, hence we have our $s(x)$ as

$s(x)=q(x)g(x)=p(x)x^{n-k}-r(x)$

Over $GF(2)$ (i.e. with binary BCH codes), this process is indistinguishable from appending a cyclic redundancy check, and if a systematic binary BCH code is used only for error-detection purposes, we see that BCH codes are just a generalization of the mathematics of cyclic redundancy checks.

The advantage to the systematic coding is that the receiver can recover the original message by discarding everything after the first k coefficients, after performing error correction.

## Decoding

There are many algorithms for decoding BCH codes. The most common ones follow this general outline:

1. Calculate the syndromes *sj* for the received vector
2. Determine the number of errors *t* and the error locator polynomial *Λ(x)* from the syndromes
3. Calculate the roots of the error location polynomial to find the error locations *Xi*
4. Calculate the error values *Yi* at those error locations
5. Correct the errors

During some of these steps, the decoding algorithm may determine that the received vector has too many errors and cannot be corrected. For example, if an appropriate value of *t* is not found, then the correction would fail. In a truncated (not primitive) code, an error location may be out of range. If the received vector has more errors than the code can correct, the decoder may unknowingly produce an apparently valid message that is not the one that was sent.

### Calculate the syndromes

The received vector R is the sum of the correct codeword C and an unknown error vector $E.$ The syndrome values are formed by considering R as a polynomial and evaluating it at $\alpha ^{c},\ldots ,\alpha ^{c+d-2}.$ Thus the syndromes are

$s_{j}=R\left(\alpha ^{j}\right)=C\left(\alpha ^{j}\right)+E\left(\alpha ^{j}\right)$

for $j=c$ to $c+d-2.$

Since $\alpha ^{j}$ are the zeros of $g(x),$ of which $C(x)$ is a multiple, $C\left(\alpha ^{j}\right)=0.$ Examining the syndrome values thus isolates the error vector so one can begin to solve for it.

If there is no error, $s_{j}=0$ for all $j.$ If the syndromes are all zero, then the decoding is done.

### Calculate the error location polynomial

If there are nonzero syndromes, then there are errors. The decoder needs to figure out how many errors and the location of those errors.

If there is a single error, write this as $E(x)=e\,x^{i},$ where i is the location of the error and e is its magnitude. Then the first two syndromes are

${\begin{aligned}s_{c}&=e\,\alpha ^{c\,i}\\s_{c+1}&=e\,\alpha ^{(c+1)\,i}=\alpha ^{i}s_{c}\end{aligned}}$

so together they allow us to calculate e and provide some information about i (completely determining it in the case of Reed–Solomon codes).

If there are two or more errors,

$E(x)=e_{1}x^{i_{1}}+e_{2}x^{i_{2}}+\cdots \,$

It is not immediately obvious how to begin solving the resulting syndromes for the unknowns $e_{k}$ and $i_{k}.$

The first step is finding, compatible with computed syndromes and with minimal possible $t,$ locator polynomial:

$\Lambda (x)=\prod _{j=1}^{t}\left(x\alpha ^{i_{j}}-1\right)$

Three popular algorithms for this task are:

1. Peterson–Gorenstein–Zierler algorithm
2. Berlekamp–Massey algorithm
3. Sugiyama Euclidean algorithm

#### Peterson–Gorenstein–Zierler algorithm

Peterson's algorithm is the step 2 of the generalized BCH decoding procedure. Peterson's algorithm is used to calculate the error locator polynomial coefficients $\lambda _{1},\lambda _{2},\dots ,\lambda _{v}$ of a polynomial

$\Lambda (x)=1+\lambda _{1}x+\lambda _{2}x^{2}+\cdots +\lambda _{v}x^{v}.$

Now the procedure of the Peterson–Gorenstein–Zierler algorithm. Expect we have at least 2*t* syndromes *s**c*, ..., *s**c*+2*t*−1. Let *v* = *t*.

1. Start by generating the $S_{v\times v}$ matrix with elements that are syndrome values $S_{v\times v}={\begin{bmatrix}s_{c}&s_{c+1}&\dots &s_{c+v-1}\\s_{c+1}&s_{c+2}&\dots &s_{c+v}\\\vdots &\vdots &\ddots &\vdots \\s_{c+v-1}&s_{c+v}&\dots &s_{c+2v-2}\end{bmatrix}}.$
2. Generate a $c_{v\times 1}$ vector with elements $C_{v\times 1}={\begin{bmatrix}s_{c+v}\\s_{c+v+1}\\\vdots \\s_{c+2v-1}\end{bmatrix}}.$
3. Let $\Lambda$ denote the unknown polynomial coefficients, which are given by $\Lambda _{v\times 1}={\begin{bmatrix}\lambda _{v}\\\lambda _{v-1}\\\vdots \\\lambda _{1}\end{bmatrix}}.$
4. Form the matrix equation $S_{v\times v}\Lambda _{v\times 1}=-C_{v\times 1\,}.$
5. If the determinant of matrix $S_{v\times v}$ is nonzero, then we can actually find an inverse of this matrix and solve for the values of unknown $\Lambda$ values.
6. If $\det \left(S_{v\times v}\right)=0,$ then follow continue from the beginning of Peterson's decoding by making smaller $S_{v\times v}$
  ```
       if 
  
    
      
        v
        =
        0
      
    
    {\displaystyle v=0}
  

       then
             declare an empty error locator polynomial
             stop Peterson procedure.
       end
       set 
  
    
      
        v
        ←
        v
        −
        1
      
    
    {\displaystyle v\leftarrow v-1}
  
  ```
7. After you have values of $\Lambda$ , you have the error locator polynomial.
8. Stop Peterson procedure.

### Factor error locator polynomial

Now that you have the $\Lambda (x)$ polynomial, its roots can be found in the form $\Lambda (x)=\left(\alpha ^{i_{1}}x-1\right)\left(\alpha ^{i_{2}}x-1\right)\cdots \left(\alpha ^{i_{v}}x-1\right)$ by brute force for example using the Chien search algorithm. The exponential powers of the primitive element $\alpha$ will yield the positions where errors occur in the received word; hence the name 'error locator' polynomial.

The zeros of Λ(*x*) are *α*−*i*1, ..., *α*−*i**v*.

### Calculate error values

Once the error locations are known, the next step is to determine the error values at those locations. The error values are then used to correct the received values at those locations to recover the original codeword.

For the case of binary BCH, (with all characters readable) this is trivial; just flip the bits for the received word at these positions, and we have the corrected code word. In the more general case, the error weights $e_{j}$ can be determined by solving the linear system

${\begin{aligned}s_{c}&=e_{1}\alpha ^{c\,i_{1}}+e_{2}\alpha ^{c\,i_{2}}+\cdots \\s_{c+1}&=e_{1}\alpha ^{(c+1)\,i_{1}}+e_{2}\alpha ^{(c+1)\,i_{2}}+\cdots \\&{}\ \vdots \end{aligned}}$

#### Forney algorithm

However, there is a more efficient method known as the Forney algorithm.

Let

$S(x)=s_{c}+s_{c+1}x+s_{c+2}x^{2}+\cdots +s_{c+d-2}x^{d-2}.$

$v\leqslant d-1,\lambda _{0}\neq 0\qquad \Lambda (x)=\sum _{i=0}^{v}\lambda _{i}x^{i}=\lambda _{0}\prod _{k=0}^{v}\left(\alpha ^{-i_{k}}x-1\right).$

And the error evaluator polynomial

$\Omega (x)\equiv S(x)\Lambda (x){\bmod {x^{d-1}}}$

Finally:

$\Lambda '(x)=\sum _{i=1}^{v}i\cdot \lambda _{i}x^{i-1},$

where

$i\cdot x:=\sum _{k=1}^{i}x.$

Than if syndromes could be explained by an error word, which could be nonzero only on positions $i_{k}$ , then error values are

$e_{k}=-{\alpha ^{i_{k}}\Omega \left(\alpha ^{-i_{k}}\right) \over \alpha ^{c\cdot i_{k}}\Lambda '\left(\alpha ^{-i_{k}}\right)}.$

For narrow-sense BCH codes, *c* = 1, so the expression simplifies to:

$e_{k}=-{\Omega \left(\alpha ^{-i_{k}}\right) \over \Lambda '\left(\alpha ^{-i_{k}}\right)}.$

#### Explanation of Forney algorithm computation

It is based on Lagrange interpolation and techniques of generating functions.

Consider $S(x)\Lambda (x),$ and for the sake of simplicity suppose $\lambda _{k}=0$ for $k>v,$ and $s_{k}=0$ for $k>c+d-2.$ Then

$S(x)\Lambda (x)=\sum _{j=0}^{\infty }\sum _{i=0}^{j}s_{j-i+1}\lambda _{i}x^{j}.$

${\begin{aligned}S(x)\Lambda (x)&=S(x)\left\{\lambda _{0}\prod _{\ell =1}^{v}\left(\alpha ^{i_{\ell }}x-1\right)\right\}\\&=\left\{\sum _{i=0}^{d-2}\sum _{j=1}^{v}e_{j}\alpha ^{(c+i)\cdot i_{j}}x^{i}\right\}\left\{\lambda _{0}\prod _{\ell =1}^{v}\left(\alpha ^{i_{\ell }}x-1\right)\right\}\\&=\left\{\sum _{j=1}^{v}e_{j}\alpha ^{ci_{j}}\sum _{i=0}^{d-2}\left(\alpha ^{i_{j}}\right)^{i}x^{i}\right\}\left\{\lambda _{0}\prod _{\ell =1}^{v}\left(\alpha ^{i_{\ell }}x-1\right)\right\}\\&=\left\{\sum _{j=1}^{v}e_{j}\alpha ^{ci_{j}}{\frac {\left(x\alpha ^{i_{j}}\right)^{d-1}-1}{x\alpha ^{i_{j}}-1}}\right\}\left\{\lambda _{0}\prod _{\ell =1}^{v}\left(\alpha ^{i_{\ell }}x-1\right)\right\}\\&=\lambda _{0}\sum _{j=1}^{v}e_{j}\alpha ^{ci_{j}}{\frac {\left(x\alpha ^{i_{j}}\right)^{d-1}-1}{x\alpha ^{i_{j}}-1}}\prod _{\ell =1}^{v}\left(\alpha ^{i_{\ell }}x-1\right)\\&=\lambda _{0}\sum _{j=1}^{v}e_{j}\alpha ^{ci_{j}}\left(\left(x\alpha ^{i_{j}}\right)^{d-1}-1\right)\prod _{\ell \in \{1,\cdots ,v\}\setminus \{j\}}\left(\alpha ^{i_{\ell }}x-1\right)\end{aligned}}$

We want to compute unknowns $e_{j},$ and we could simplify the context by removing the $\left(x\alpha ^{i_{j}}\right)^{d-1}$ terms. This leads to the error evaluator polynomial

$\Omega (x)\equiv S(x)\Lambda (x){\bmod {x^{d-1}}}.$

Thanks to $v\leqslant d-1$ we have

$\Omega (x)=-\lambda _{0}\sum _{j=1}^{v}e_{j}\alpha ^{ci_{j}}\prod _{\ell \in \{1,\cdots ,v\}\setminus \{j\}}\left(\alpha ^{i_{\ell }}x-1\right).$

Thanks to $\Lambda$ (the Lagrange interpolation trick) the sum degenerates to only one summand for $x=\alpha ^{-i_{k}}$

$\Omega \left(\alpha ^{-i_{k}}\right)=-\lambda _{0}e_{k}\alpha ^{c\cdot i_{k}}\prod _{\ell \in \{1,\cdots ,v\}\setminus \{k\}}\left(\alpha ^{i_{\ell }}\alpha ^{-i_{k}}-1\right).$

To get $e_{k}$ we just should get rid of the product. We could compute the product directly from already computed roots $\alpha ^{-i_{j}}$ of $\Lambda ,$ but we could use simpler form.

As formal derivative

$\Lambda '(x)=\lambda _{0}\sum _{j=1}^{v}\alpha ^{i_{j}}\prod _{\ell \in \{1,\cdots ,v\}\setminus \{j\}}\left(\alpha ^{i_{\ell }}x-1\right),$

we get again only one summand in

$\Lambda '\left(\alpha ^{-i_{k}}\right)=\lambda _{0}\alpha ^{i_{k}}\prod _{\ell \in \{1,\cdots ,v\}\setminus \{k\}}\left(\alpha ^{i_{\ell }}\alpha ^{-i_{k}}-1\right).$

So finally

$e_{k}=-{\frac {\alpha ^{i_{k}}\Omega \left(\alpha ^{-i_{k}}\right)}{\alpha ^{c\cdot i_{k}}\Lambda '\left(\alpha ^{-i_{k}}\right)}}.$

This formula is advantageous when one computes the formal derivative of $\Lambda$ form

$\Lambda (x)=\sum _{i=1}^{v}\lambda _{i}x^{i}$

yielding:

$\Lambda '(x)=\sum _{i=1}^{v}i\cdot \lambda _{i}x^{i-1},$

where

$i\cdot x:=\sum _{k=1}^{i}x.$

### Decoding based on extended Euclidean algorithm

An alternate process of finding both the polynomial Λ and the error locator polynomial is based on Yasuo Sugiyama's adaptation of the Extended Euclidean algorithm. Correction of unreadable characters could be incorporated to the algorithm easily as well.

Let $k_{1},...,k_{k}$ be positions of unreadable characters. One creates polynomial localising these positions $\Gamma (x)=\prod _{i=1}^{k}\left(x\alpha ^{k_{i}}-1\right).$ Set values on unreadable positions to 0 and compute the syndromes.

As we have already defined for the Forney formula let $S(x)=\sum _{i=0}^{d-2}s_{c+i}x^{i}.$

Let us run extended Euclidean algorithm for locating least common divisor of polynomials $S(x)\Gamma (x)$ and $x^{d-1}.$ The goal is not to find the least common divisor, but a polynomial $r(x)$ of degree at most $\lfloor (d+k-3)/2\rfloor$ and polynomials $a(x),b(x)$ such that $r(x)=a(x)S(x)\Gamma (x)+b(x)x^{d-1}.$ Low degree of $r(x)$ guarantees, that $a(x)$ would satisfy extended (by $\Gamma$ ) defining conditions for $\Lambda .$

Defining $\Xi (x)=a(x)\Gamma (x)$ and using $\Xi$ on the place of $\Lambda (x)$ in the Fourney formula will give us error values.

The main advantage of the algorithm is that it meanwhile computes $\Omega (x)=S(x)\Xi (x){\bmod {x}}^{d-1}=r(x)$ required in the Forney formula.

#### Explanation of the decoding process

The goal is to find a codeword which differs from the received word minimally as possible on readable positions. When expressing the received word as a sum of nearest codeword and error word, we are trying to find error word with minimal number of non-zeros on readable positions. Syndrom $s_{i}$ restricts error word by condition

$s_{i}=\sum _{j=0}^{n-1}e_{j}\alpha ^{ij}.$

We could write these conditions separately or we could create polynomial

$S(x)=\sum _{i=0}^{d-2}s_{c+i}x^{i}$

and compare coefficients near powers 0 to $d-2.$

$S(x){\stackrel {\{0,\cdots ,\,d-2\}}{=}}E(x)=\sum _{i=0}^{d-2}\sum _{j=0}^{n-1}e_{j}\alpha ^{ij}\alpha ^{cj}x^{i}.$

Suppose there is unreadable letter on position $k_{1},$ we could replace set of syndromes $\{s_{c},\cdots ,s_{c+d-2}\}$ by set of syndromes $\{t_{c},\cdots ,t_{c+d-3}\}$ defined by equation $t_{i}=\alpha ^{k_{1}}s_{i}-s_{i+1}.$ Suppose for an error word all restrictions by original set $\{s_{c},\cdots ,s_{c+d-2}\}$ of syndromes hold, than

$t_{i}=\alpha ^{k_{1}}s_{i}-s_{i+1}=\alpha ^{k_{1}}\sum _{j=0}^{n-1}e_{j}\alpha ^{ij}-\sum _{j=0}^{n-1}e_{j}\alpha ^{j}\alpha ^{ij}=\sum _{j=0}^{n-1}e_{j}\left(\alpha ^{k_{1}}-\alpha ^{j}\right)\alpha ^{ij}.$

New set of syndromes restricts error vector

$f_{j}=e_{j}\left(\alpha ^{k_{1}}-\alpha ^{j}\right)$

the same way the original set of syndromes restricted the error vector $e_{j}.$ Except the coordinate $k_{1},$ where we have $f_{k_{1}}=0,$ an $f_{j}$ is zero, if $e_{j}=0.$ For the goal of locating error positions we could change the set of syndromes in the similar way to reflect all unreadable characters. This shortens the set of syndromes by $k.$

In polynomial formulation, the replacement of syndromes set $\{s_{c},\cdots ,s_{c+d-2}\}$ by syndromes set $\{t_{c},\cdots ,t_{c+d-3}\}$ leads to

$T(x)=\sum _{i=0}^{d-3}t_{c+i}x^{i}=\alpha ^{k_{1}}\sum _{i=0}^{d-3}s_{c+i}x^{i}-\sum _{i=1}^{d-2}s_{c+i}x^{i-1}.$

Therefore,

$xT(x){\stackrel {\{1,\cdots ,\,d-2\}}{=}}\left(x\alpha ^{k_{1}}-1\right)S(x).$

After replacement of $S(x)$ by $S(x)\Gamma (x)$ , one would require equation for coefficients near powers $k,\cdots ,d-2.$

One could consider looking for error positions from the point of view of eliminating influence of given positions similarly as for unreadable characters. If we found v positions such that eliminating their influence leads to obtaining set of syndromes consisting of all zeros, than there exists error vector with errors only on these coordinates. If $\Lambda (x)$ denotes the polynomial eliminating the influence of these coordinates, we obtain

$S(x)\Gamma (x)\Lambda (x){\stackrel {\{k+v,\cdots ,d-2\}}{=}}0.$

In Euclidean algorithm, we try to correct at most ${\tfrac {1}{2}}(d-1-k)$ errors (on readable positions), because with bigger error count there could be more codewords in the same distance from the received word. Therefore, for $\Lambda (x)$ we are looking for, the equation must hold for coefficients near powers starting from

$k+\left\lfloor {\frac {1}{2}}(d-1-k)\right\rfloor .$

In Forney formula, $\Lambda (x)$ could be multiplied by a scalar giving the same result.

It could happen that the Euclidean algorithm finds $\Lambda (x)$ of degree higher than ${\tfrac {1}{2}}(d-1-k)$ having number of different roots equal to its degree, where the Fourney formula would be able to correct errors in all its roots, anyway correcting such many errors could be risky (especially with no other restrictions on received word). Usually after getting $\Lambda (x)$ of higher degree, we decide not to correct the errors. Correction could fail in the case $\Lambda (x)$ has roots with higher multiplicity or the number of roots is smaller than its degree. Fail could be detected as well by Forney formula returning error outside the transmitted alphabet.

### Correct the errors

Using the error values and error location, correct the errors and form a corrected code vector by subtracting error values at error locations.

### Decoding examples

#### Decoding of binary code without unreadable characters

Consider a BCH code in GF(24) with $d=7$ and $g(x)=x^{10}+x^{8}+x^{5}+x^{4}+x^{2}+x+1$ . (This is used in QR codes.) Let the message to be transmitted be [1 1 0 1 1], or in polynomial notation, $M(x)=x^{4}+x^{3}+x+1.$ The "checksum" symbols are calculated by dividing $x^{10}M(x)$ by $g(x)$ and taking the remainder, resulting in $x^{9}+x^{4}+x^{2}$ or [ 1 0 0 0 0 1 0 1 0 0 ]. These are appended to the message, so the transmitted codeword is [ 1 1 0 1 1 1 0 0 0 0 1 0 1 0 0 ].

Now, imagine that there are two bit-errors in the transmission, so the received codeword is [ 1 0 0 1 1 1 0 0 0 1 1 0 1 0 0 ]. In polynomial notation:

$R(x)=C(x)+x^{13}+x^{5}=x^{14}+x^{11}+x^{10}+x^{9}+x^{5}+x^{4}+x^{2}$

In order to correct the errors, first calculate the syndromes. Taking $\alpha =0010,$ we have $s_{1}=R(\alpha ^{1})=1011,$ $s_{2}=1001,$ $s_{3}=1011,$ $s_{4}=1101,$ $s_{5}=0001,$ and $s_{6}=1001.$ Next, apply the Peterson procedure by row-reducing the following augmented matrix.

$\left[S_{3\times 3}|C_{3\times 1}\right]={\begin{bmatrix}s_{1}&s_{2}&s_{3}&s_{4}\\s_{2}&s_{3}&s_{4}&s_{5}\\s_{3}&s_{4}&s_{5}&s_{6}\end{bmatrix}}={\begin{bmatrix}1011&1001&1011&1101\\1001&1011&1101&0001\\1011&1101&0001&1001\end{bmatrix}}\Rightarrow {\begin{bmatrix}0001&0000&1000&0111\\0000&0001&1011&0001\\0000&0000&0000&0000\end{bmatrix}}$

Due to the zero row, *S*3×3 is singular, which is no surprise since only two errors were introduced into the codeword. However, the upper-left corner of the matrix is identical to [*S*2×2 | *C*2×1], which gives rise to the solution $\lambda _{2}=1000,$ $\lambda _{1}=1011.$ The resulting error locator polynomial is $\Lambda (x)=1000x^{2}+1011x+0001,$ which has zeros at $0100=\alpha ^{-13}$ and $0111=\alpha ^{-5}.$ The exponents of $\alpha$ correspond to the error locations. There is no need to calculate the error values in this example, as the only possible value is 1.

#### Decoding with unreadable characters

Suppose the same scenario, but the received word has two unreadable characters [ 1 0 0 ? 1 1 ? 0 0 1 1 0 1 0 0 ]. We replace the unreadable characters by zeros while creating the polynomial reflecting their positions $\Gamma (x)=\left(\alpha ^{8}x-1\right)\left(\alpha ^{11}x-1\right).$ We compute the syndromes $s_{1}=\alpha ^{-7},s_{2}=\alpha ^{1},s_{3}=\alpha ^{4},s_{4}=\alpha ^{2},s_{5}=\alpha ^{5},$ and $s_{6}=\alpha ^{-7}.$ (Using log notation which is independent on GF(24) isomorphisms. For computation checking we can use the same representation for addition as was used in previous example. Hexadecimal description of the powers of $\alpha$ are consecutively 1,2,4,8,3,6,C,B,5,A,7,E,F,D,9 with the addition based on bitwise xor.)

Let us make syndrome polynomial

$S(x)=\alpha ^{-7}+\alpha ^{1}x+\alpha ^{4}x^{2}+\alpha ^{2}x^{3}+\alpha ^{5}x^{4}+\alpha ^{-7}x^{5},$

compute

$S(x)\Gamma (x)=\alpha ^{-7}+\alpha ^{4}x+\alpha ^{-1}x^{2}+\alpha ^{6}x^{3}+\alpha ^{-1}x^{4}+\alpha ^{5}x^{5}+\alpha ^{7}x^{6}+\alpha ^{-3}x^{7}.$

Run the extended Euclidean algorithm:

${\begin{aligned}&{\begin{pmatrix}S(x)\Gamma (x)\\x^{6}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\alpha ^{-7}+\alpha ^{4}x+\alpha ^{-1}x^{2}+\alpha ^{6}x^{3}+\alpha ^{-1}x^{4}+\alpha ^{5}x^{5}+\alpha ^{7}x^{6}+\alpha ^{-3}x^{7}\\x^{6}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\alpha ^{7}+\alpha ^{-3}x&1\\1&0\end{pmatrix}}{\begin{pmatrix}x^{6}\\\alpha ^{-7}+\alpha ^{4}x+\alpha ^{-1}x^{2}+\alpha ^{6}x^{3}+\alpha ^{-1}x^{4}+\alpha ^{5}x^{5}+2\alpha ^{7}x^{6}+2\alpha ^{-3}x^{7}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\alpha ^{7}+\alpha ^{-3}x&1\\1&0\end{pmatrix}}{\begin{pmatrix}\alpha ^{4}+\alpha ^{-5}x&1\\1&0\end{pmatrix}}\\&\qquad {\begin{pmatrix}\alpha ^{-7}+\alpha ^{4}x+\alpha ^{-1}x^{2}+\alpha ^{6}x^{3}+\alpha ^{-1}x^{4}+\alpha ^{5}x^{5}\\\alpha ^{-3}+\left(\alpha ^{-7}+\alpha ^{3}\right)x+\left(\alpha ^{3}+\alpha ^{-1}\right)x^{2}+\left(\alpha ^{-5}+\alpha ^{-6}\right)x^{3}+\left(\alpha ^{3}+\alpha ^{1}\right)x^{4}+2\alpha ^{-6}x^{5}+2x^{6}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\left(1+\alpha ^{-4}\right)+\left(\alpha ^{1}+\alpha ^{2}\right)x+\alpha ^{7}x^{2}&\alpha ^{7}+\alpha ^{-3}x\\\alpha ^{4}+\alpha ^{-5}x&1\end{pmatrix}}{\begin{pmatrix}\alpha ^{-7}+\alpha ^{4}x+\alpha ^{-1}x^{2}+\alpha ^{6}x^{3}+\alpha ^{-1}x^{4}+\alpha ^{5}x^{5}\\\alpha ^{-3}+\alpha ^{-2}x+\alpha ^{0}x^{2}+\alpha ^{-2}x^{3}+\alpha ^{-6}x^{4}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\alpha ^{-3}+\alpha ^{5}x+\alpha ^{7}x^{2}&\alpha ^{7}+\alpha ^{-3}x\\\alpha ^{4}+\alpha ^{-5}x&1\end{pmatrix}}{\begin{pmatrix}\alpha ^{-5}+\alpha ^{-4}x&1\\1&0\end{pmatrix}}\\&\qquad {\begin{pmatrix}\alpha ^{-3}+\alpha ^{-2}x+\alpha ^{0}x^{2}+\alpha ^{-2}x^{3}+\alpha ^{-6}x^{4}\\\left(\alpha ^{7}+\alpha ^{-7}\right)+\left(2\alpha ^{-7}+\alpha ^{4}\right)x+\left(\alpha ^{-5}+\alpha ^{-6}+\alpha ^{-1}\right)x^{2}+\left(\alpha ^{-7}+\alpha ^{-4}+\alpha ^{6}\right)x^{3}+\left(\alpha ^{4}+\alpha ^{-6}+\alpha ^{-1}\right)x^{4}+2\alpha ^{5}x^{5}\end{pmatrix}}\\[6pt]={}&{\begin{pmatrix}\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}&\alpha ^{-3}+\alpha ^{5}x+\alpha ^{7}x^{2}\\\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}&\alpha ^{4}+\alpha ^{-5}x\end{pmatrix}}{\begin{pmatrix}\alpha ^{-3}+\alpha ^{-2}x+\alpha ^{0}x^{2}+\alpha ^{-2}x^{3}+\alpha ^{-6}x^{4}\\\alpha ^{-4}+\alpha ^{4}x+\alpha ^{2}x^{2}+\alpha ^{-5}x^{3}\end{pmatrix}}.\end{aligned}}$

We have reached polynomial of degree at most 3, and as

${\begin{pmatrix}-\left(\alpha ^{4}+\alpha ^{-5}x\right)&\alpha ^{-3}+\alpha ^{5}x+\alpha ^{7}x^{2}\\\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}&-\left(\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}\right)\end{pmatrix}}{\begin{pmatrix}\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}&\alpha ^{-3}+\alpha ^{5}x+\alpha ^{7}x^{2}\\\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}&\alpha ^{4}+\alpha ^{-5}x\end{pmatrix}}={\begin{pmatrix}1&0\\0&1\end{pmatrix}},$

we get

${\begin{pmatrix}-\left(\alpha ^{4}+\alpha ^{-5}x\right)&\alpha ^{-3}+\alpha ^{5}x+\alpha ^{7}x^{2}\\\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}&-\left(\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}\right)\end{pmatrix}}{\begin{pmatrix}S(x)\Gamma (x)\\x^{6}\end{pmatrix}}={\begin{pmatrix}\alpha ^{-3}+\alpha ^{-2}x+\alpha ^{0}x^{2}+\alpha ^{-2}x^{3}+\alpha ^{-6}x^{4}\\\alpha ^{-4}+\alpha ^{4}x+\alpha ^{2}x^{2}+\alpha ^{-5}x^{3}\end{pmatrix}}.$

Therefore,

$S(x)\Gamma (x)\left(\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}\right)-\left(\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}\right)x^{6}=\alpha ^{-4}+\alpha ^{4}x+\alpha ^{2}x^{2}+\alpha ^{-5}x^{3}.$

Let $\Lambda (x)=\alpha ^{3}+\alpha ^{-5}x+\alpha ^{6}x^{2}.$ Don't worry that $\lambda _{0}\neq 1.$ Find by brute force a root of $\Lambda .$ The roots are $\alpha ^{2},$ and $\alpha ^{10}$ (after finding for example $\alpha ^{2}$ we can divide $\Lambda$ by corresponding monom $\left(x-\alpha ^{2}\right)$ and the root of resulting monom could be found easily).

Let

${\begin{aligned}\Xi (x)&=\Gamma (x)\Lambda (x)=\alpha ^{3}+\alpha ^{4}x^{2}+\alpha ^{2}x^{3}+\alpha ^{-5}x^{4}\\\Omega (x)&=S(x)\Xi (x)\equiv \alpha ^{-4}+\alpha ^{4}x+\alpha ^{2}x^{2}+\alpha ^{-5}x^{3}{\bmod {x^{6}}}\end{aligned}}$

Let us look for error values using formula

$e_{j}=-{\frac {\Omega \left(\alpha ^{-i_{j}}\right)}{\Xi '\left(\alpha ^{-i_{j}}\right)}},$

where $\alpha ^{-i_{j}}$ are roots of $\Xi (x).$ $\Xi '(x)=\alpha ^{2}x^{2}.$ We get

${\begin{aligned}e_{1}&=-{\frac {\Omega (\alpha ^{4})}{\Xi '(\alpha ^{4})}}={\frac {\alpha ^{-4}+\alpha ^{-7}+\alpha ^{-5}+\alpha ^{7}}{\alpha ^{-5}}}={\frac {\alpha ^{-5}}{\alpha ^{-5}}}=1\\e_{2}&=-{\frac {\Omega (\alpha ^{7})}{\Xi '(\alpha ^{7})}}={\frac {\alpha ^{-4}+\alpha ^{-4}+\alpha ^{1}+\alpha ^{1}}{\alpha ^{1}}}=0\\e_{3}&=-{\frac {\Omega (\alpha ^{10})}{\Xi '(\alpha ^{10})}}={\frac {\alpha ^{-4}+\alpha ^{-1}+\alpha ^{7}+\alpha ^{-5}}{\alpha ^{7}}}={\frac {\alpha ^{7}}{\alpha ^{7}}}=1\\e_{4}&=-{\frac {\Omega (\alpha ^{2})}{\Xi '(\alpha ^{2})}}={\frac {\alpha ^{-4}+\alpha ^{6}+\alpha ^{6}+\alpha ^{1}}{\alpha ^{6}}}={\frac {\alpha ^{6}}{\alpha ^{6}}}=1\end{aligned}}$

Fact, that $e_{3}=e_{4}=1,$ should not be surprising.

Corrected code is therefore [ 1 1 0 1 1 1 0 0 0 0 1 0 1 0 0].

#### Decoding with unreadable characters with a small number of errors

Let us show the algorithm behaviour for the case with small number of errors. Let the received word is [ 1 0 0 ? 1 1 ? 0 0 0 1 0 1 0 0 ].

Again, replace the unreadable characters by zeros while creating the polynomial reflecting their positions $\Gamma (x)=\left(\alpha ^{8}x-1\right)\left(\alpha ^{11}x-1\right).$ Compute the syndromes $s_{1}=\alpha ^{4},s_{2}=\alpha ^{-7},s_{3}=\alpha ^{1},s_{4}=\alpha ^{1},s_{5}=\alpha ^{0},$ and $s_{6}=\alpha ^{2}.$ Create syndrome polynomial

${\begin{aligned}S(x)&=\alpha ^{4}+\alpha ^{-7}x+\alpha ^{1}x^{2}+\alpha ^{1}x^{3}+\alpha ^{0}x^{4}+\alpha ^{2}x^{5},\\S(x)\Gamma (x)&=\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}+\alpha ^{-1}x^{6}+\alpha ^{6}x^{7}.\end{aligned}}$

Let us run the extended Euclidean algorithm:

${\begin{aligned}{\begin{pmatrix}S(x)\Gamma (x)\\x^{6}\end{pmatrix}}&={\begin{pmatrix}\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}+\alpha ^{-1}x^{6}+\alpha ^{6}x^{7}\\x^{6}\end{pmatrix}}\\&={\begin{pmatrix}\alpha ^{-1}+\alpha ^{6}x&1\\1&0\end{pmatrix}}{\begin{pmatrix}x^{6}\\\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}+2\alpha ^{-1}x^{6}+2\alpha ^{6}x^{7}\end{pmatrix}}\\&={\begin{pmatrix}\alpha ^{-1}+\alpha ^{6}x&1\\1&0\end{pmatrix}}{\begin{pmatrix}\alpha ^{3}+\alpha ^{1}x&1\\1&0\end{pmatrix}}{\begin{pmatrix}\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}\\\alpha ^{7}+\left(\alpha ^{-5}+\alpha ^{5}\right)x+2\alpha ^{-7}x^{2}+2\alpha ^{6}x^{3}+2\alpha ^{4}x^{4}+2\alpha ^{2}x^{5}+2x^{6}\end{pmatrix}}\\&={\begin{pmatrix}\left(1+\alpha ^{2}\right)+\left(\alpha ^{0}+\alpha ^{-6}\right)x+\alpha ^{7}x^{2}&\alpha ^{-1}+\alpha ^{6}x\\\alpha ^{3}+\alpha ^{1}x&1\end{pmatrix}}{\begin{pmatrix}\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}\\\alpha ^{7}+\alpha ^{0}x\end{pmatrix}}\end{aligned}}$

We have reached polynomial of degree at most 3, and as

${\begin{pmatrix}-1&\alpha ^{-1}+\alpha ^{6}x\\\alpha ^{3}+\alpha ^{1}x&-\left(\alpha ^{-7}+\alpha ^{7}x+\alpha ^{7}x^{2}\right)\end{pmatrix}}{\begin{pmatrix}\alpha ^{-7}+\alpha ^{7}x+\alpha ^{7}x^{2}&\alpha ^{-1}+\alpha ^{6}x\\\alpha ^{3}+\alpha ^{1}x&1\end{pmatrix}}={\begin{pmatrix}1&0\\0&1\end{pmatrix}},$

we get

${\begin{pmatrix}-1&\alpha ^{-1}+\alpha ^{6}x\\\alpha ^{3}+\alpha ^{1}x&-\left(\alpha ^{-7}+\alpha ^{7}x+\alpha ^{7}x^{2}\right)\end{pmatrix}}{\begin{pmatrix}S(x)\Gamma (x)\\x^{6}\end{pmatrix}}={\begin{pmatrix}\alpha ^{4}+\alpha ^{7}x+\alpha ^{5}x^{2}+\alpha ^{3}x^{3}+\alpha ^{1}x^{4}+\alpha ^{-1}x^{5}\\\alpha ^{7}+\alpha ^{0}x\end{pmatrix}}.$

Therefore,

$S(x)\Gamma (x)\left(\alpha ^{3}+\alpha ^{1}x\right)-\left(\alpha ^{-7}+\alpha ^{7}x+\alpha ^{7}x^{2}\right)x^{6}=\alpha ^{7}+\alpha ^{0}x.$

Let $\Lambda (x)=\alpha ^{3}+\alpha ^{1}x.$ Don't worry that $\lambda _{0}\neq 1.$ The root of $\Lambda (x)$ is $\alpha ^{3-1}.$

Let

${\begin{aligned}\Xi (x)&=\Gamma (x)\Lambda (x)=\alpha ^{3}+\alpha ^{-7}x+\alpha ^{-4}x^{2}+\alpha ^{5}x^{3},\\\Omega (x)&=S(x)\Xi (x)\equiv \alpha ^{7}+\alpha ^{0}x{\bmod {x^{6}}}\end{aligned}}$

Let us look for error values using formula $e_{j}=-\Omega \left(\alpha ^{-i_{j}}\right)/\Xi '\left(\alpha ^{-i_{j}}\right),$ where $\alpha ^{-i_{j}}$ are roots of polynomial $\Xi (x).$

$\Xi '(x)=\alpha ^{-7}+\alpha ^{5}x^{2}.$

We get

${\begin{aligned}e_{1}&=-{\frac {\Omega \left(\alpha ^{4}\right)}{\Xi '\left(\alpha ^{4}\right)}}={\frac {\alpha ^{7}+\alpha ^{4}}{\alpha ^{-7}+\alpha ^{-2}}}={\frac {\alpha ^{3}}{\alpha ^{3}}}=1\\e_{2}&=-{\frac {\Omega \left(\alpha ^{7}\right)}{\Xi '\left(\alpha ^{7}\right)}}={\frac {\alpha ^{7}+\alpha ^{7}}{\alpha ^{-7}+\alpha ^{4}}}=0\\e_{3}&=-{\frac {\Omega \left(\alpha ^{2}\right)}{\Xi '\left(\alpha ^{2}\right)}}={\frac {\alpha ^{7}+\alpha ^{2}}{\alpha ^{-7}+\alpha ^{-6}}}={\frac {\alpha ^{-3}}{\alpha ^{-3}}}=1\end{aligned}}$

The fact that $e_{3}=1$ should not be surprising.

Corrected code is therefore [ 1 1 0 1 1 1 0 0 0 0 1 0 1 0 0].
