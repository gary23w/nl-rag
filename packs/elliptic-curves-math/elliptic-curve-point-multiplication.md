---
title: "Elliptic curve point multiplication"
source: https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
domain: elliptic-curves-math
license: CC-BY-SA-4.0
tags: elliptic curve, mordell-weil theorem, weierstrass elliptic function, elliptic integral
fetched: 2026-07-02
---

# Elliptic curve point multiplication

**Elliptic curve scalar multiplication** is the operation of successively adding a point along an elliptic curve to itself repeatedly. It is used in elliptic curve cryptography (ECC). The literature presents this operation as scalar multiplication, as written in Hessian form of an elliptic curve. A widespread name for this operation is also **elliptic curve point multiplication**, but this can convey the wrong impression of being a multiplication between two points.

## Basics

Given a curve, *E*, defined by some equation in a finite field (such as *E*: *y*2 = *x*3 + *ax* + *b*), point multiplication is defined as the repeated addition of a point along that curve. Denote as *nP* = *P* + *P* + *P* + … + *P* for some scalar (integer) *n* and a point *P* = (*x*, *y*) that lies on the curve, *E*. This type of curve is known as a Weierstrass curve.

The security of modern ECC depends on the intractability of determining *n* from *Q* = *nP* given known values of *Q* and *P* if *n* is large (known as the elliptic curve discrete logarithm problem by analogy to other cryptographic systems). This is because the addition of two points on an elliptic curve (or the addition of one point to itself) yields a third point on the elliptic curve whose location has no immediately obvious relationship to the locations of the first two, and repeating this many times over yields a point *nP* that may be essentially anywhere. Intuitively, this is not dissimilar to the fact that if you had a point *P* on a circle, adding 42.57 degrees to its angle may still be a point "not too far" from *P*, but adding 1000 or 1001 times 42.57 degrees will yield a point that requires a bit more complex calculation to find the original angle. Reversing this process, i.e., given *Q=nP* and *P*, and determining *n*, can only be done by trying out all possible *n*—an effort that is computationally intractable if *n* is large.

## Point operations

There are three commonly defined operations for elliptic curve points: addition, doubling and negation.

### Point at infinity

Point at infinity ⁠ ${\mathcal {O}}$ ⁠ is the identity element of elliptic curve arithmetic. Adding it to any point results in that other point, including adding point at infinity to itself. That is:

${\begin{aligned}{\mathcal {O}}+{\mathcal {O}}={\mathcal {O}}\\{\mathcal {O}}+P=P\end{aligned}}$

Point at infinity is also written as 0.

### Point negation

Point negation is finding such a point, that adding it to itself will result in point at infinity (⁠ ${\mathcal {O}}$ ⁠).

${\begin{aligned}P+(-P)={\mathcal {O}}\end{aligned}}$

For elliptic curves of the form *E*: *y*2 = *x*3 + *ax* + *b*, negation is a point with the same *x* coordinate but negated *y* coordinate:

${\begin{aligned}(x,y)+(-(x,y))&={\mathcal {O}}\\(x,y)+(x,-y)&={\mathcal {O}}\\(x,-y)&=-(x,y)\end{aligned}}$

### Point addition

With 2 distinct points, *P* and *Q*, addition is defined as the negation of the point resulting from the intersection of the curve, *E*, and the straight line defined by the points *P* and *Q*, giving the point, *R*.

${\begin{aligned}P+Q&=R\\(x_{p},y_{p})+(x_{q},y_{q})&=(x_{r},y_{r})\end{aligned}}$

Assuming the elliptic curve, *E*, is given by *y*2 = *x*3 + *ax* + *b*, this can be calculated as:

${\begin{aligned}\lambda &={\frac {y_{q}-y_{p}}{x_{q}-x_{p}}}\\x_{r}&=\lambda ^{2}-x_{p}-x_{q}\\y_{r}&=\lambda (x_{p}-x_{r})-y_{p}\\\end{aligned}}$

These equations are correct when neither point is the point at infinity, ⁠ ${\mathcal {O}}$ ⁠, and if the points have different x coordinates (they're not mutual inverses). This is important for the ECDSA verification algorithm where the hash value could be zero.

### Point doubling

Where the points *P* and *Q* are coincident (at the same coordinates), addition is similar, except that there is no well-defined straight line through *P*, so the operation is closed using a limiting case, the tangent to the curve, *E*, at *P*.

This is calculated as above, taking derivatives (dE/dx)/(dE/dy):

$\lambda ={\frac {3x_{p}^{2}+a}{2y_{p}}}$

where *a* is from the defining equation of the curve, *E*, above.

## Point multiplication

The straightforward way of computing a point multiplication is through repeated addition. However, there are more efficient approaches to computing the multiplication.

### Double-and-add

The simplest method is the double-and-add method, similar to square-and-multiply in modular exponentiation. The algorithm works as follows:

To compute *sP*, start with the binary representation for *s*: ⁠ $s=s_{0}+2s_{1}+2^{2}s_{2}+\cdots +2^{n-1}s_{n-1}$ ⁠, where ⁠ $s_{0}~..~s_{n-1}\in \{0,1\},n=\lceil \log _{2}{s}\rceil$ ⁠.

- Iterative algorithm, index increasing:

```
let bits = bit_representation(s)  # the vector of bits (from LSB to MSB) representing s
let res = 
  
    
      
        
          
            
              
                
                  
                    O
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\mathcal {O}}\end{aligned}}}
  
 # point at infinity
let temp = P  # track doubled P val
for bit in bits: 
    if bit == 1:
        res = res + temp  # point add
    temp = temp + temp  # double
return res
```

- Iterative algorithm, index decreasing:

```
let bits = bit_representation(s)  # the vector of bits (from LSB to MSB) representing s
let i = length(bits) - 2
let res = P
while (i >= 0):  # traversing from second MSB to LSB
    res = res + res  # double
    if bits[i] == 1:
        res = res + P  # add
    i = i - 1
return res
```

Note that both of the iterative methods above are vulnerable to timing analysis. See Montgomery Ladder below for an alternative approach.

- Recursive algorithm:

```
algorithm f(P, d) is
    if d = 0 then
        return 0                         # computation complete
    else if d = 1 then
        return P
    else if d mod 2 = 1 then
        return point_add(P, f(P, d - 1))  # addition when d is odd
    else
        return f(point_double(P), d / 2)   # doubling when d is even
```

where *f* is the function for multiplying, *P* is the coordinate to multiply, *d* is the number of times to add the coordinate to itself. Example: *100P* can be written as *2(2[P + 2(2[2(P + 2P)])])* and thus requires six point double operations and two point addition operations. *100P* would be equal to *f(P, 100)*.

This algorithm requires log2(*d*) iterations of point doubling and addition to compute the full point multiplication. There are many variations of this algorithm such as using a window, sliding window, NAF, NAF-w, vector chains, and Montgomery ladder.

### Windowed method

In the windowed version of this algorithm, one selects a window size *w* and computes all $2^{w}$ values of $dP$ for $d=0,1,2,\dots ,2^{w}-1$ . The algorithm now uses the representation $d=d_{0}+2^{w}d_{1}+2^{2w}d_{2}+\cdots +2^{mw}d_{m}$ and becomes

```
Q ← 0
for i from m to 0 do
    Q ← point_double_repeat(Q, w)
    if di > 0 then
        Q ← point_add(Q, diP)  # using pre-computed value of diP
return Q
```

This algorithm has the same complexity as the double-and-add approach with the benefit of using fewer point additions (which in practice are slower than doubling). Typically, the value of *w* is chosen to be fairly small making the pre-computation stage a trivial component of the algorithm. For the NIST recommended curves, $w=4$ is usually the best selection. The entire complexity for a *n*-bit number is measured as $n+1$ point doubles and $2^{w}-2+{\tfrac {n}{w}}$ point additions.

### Sliding-window method

In the sliding-window version, we look to trade off point additions for point doubles. We compute a similar table as in the windowed version except we only compute the points $dP$ for $d=2^{w-1},2^{w-1}+1,\dots ,2^{w}-1$ . Effectively, we are only computing the values for which the most significant bit of the window is set. The algorithm then uses the original double-and-add representation of $d=d_{0}+2d_{1}+2^{2}d_{2}+\cdots +2^{m}d_{m}$ .

```
Q ← 0
for i from m downto 0 do
    if di = 0 then
        Q ← point_double(Q)
    else
        t ← extract j (up to w − 1) additional bits from d (including di)
        i ← i − j
        if j < w then
            Perform double-and-add using t
            return Q
        else 
            Q ← point_double_repeat(Q, w)
            Q ← point_add(Q, tP)
return Q
```

This algorithm has the benefit that the pre-computation stage is roughly half as complex as the normal windowed method while also trading slower point additions for point doublings. In effect, there is little reason to use the windowed method over this approach, except that the former can be implemented in constant time. The algorithm requires $w-1+n$ point doubles and at most $2^{w-1}-1+{\tfrac {n}{w}}$ point additions.

### *w*-ary non-adjacent form (*w*NAF) method

In the non-adjacent form we aim to make use of the fact that point subtraction is just as easy as point addition to perform fewer (of either) as compared to a sliding-window method. The NAF of the multiplicand d must be computed first with the following algorithm

```
i ← 0
while (d > 0) do
    if (d mod 2) = 1 then 
        di ← d mods 2w
        d ← d − di
    else
        di = 0
    d ← d/2
    i ← i + 1
return (di−1, di-2, ..., d0)
```

Where the signed modulo function *mods* is defined as

```
if (d mod 2w) >= 2w−1
    return (d mod 2w) − 2w
else
    return d mod 2w
```

This produces the NAF needed to now perform the multiplication. This algorithm requires the pre-computation of the points $\lbrace 1,3,5,\dots ,2^{w-1}-1\rbrace P$ and their negatives, where P is the point to be multiplied. On typical Weierstrass curves, if $P=\lbrace x,y\rbrace$ then $-P=\lbrace x,-y\rbrace$ . So in essence the negatives are cheap to compute. Next, the following algorithm computes the multiplication $dP$ :

```
Q ← 0
for j ← i − 1 downto 0 do
    Q ← point_double(Q)
    if (dj != 0)
        Q ← point_add(Q, djP)
return Q
```

The wNAF guarantees that on average there will be a density of ${\tfrac {1}{w+1}}$ point additions (slightly better than the unsigned window). It requires 1 point doubling and $2^{w-2}-1$ point additions for precomputation. The algorithm then requires n point doublings and ${\tfrac {n}{w+1}}$ point additions for the rest of the multiplication.

One property of the NAF is that we are guaranteed that every non-zero element $d_{i}$ is followed by at least $w-1$ additional zeroes. This is because the algorithm clears out the lower w bits of d with every subtraction of the output of the *mods* function. This observation can be used for several purposes. After every non-zero element the additional zeroes can be implied and do not need to be stored. Secondly, the multiple serial divisions by 2 can be replaced by a division by $2^{w}$ after every non-zero $d_{i}$ element and divide by 2 after every zero.

It has been shown that through application of a FLUSH+RELOAD side-channel attack on OpenSSL, the full private key can be revealed after performing cache-timing against as few as 200 signatures performed.

### Montgomery ladder

The Montgomery ladder approach computes the point multiplication in a *fixed* number of operations. This can be beneficial when timing, power consumption, or branch measurements are exposed to an attacker performing a side-channel attack. The algorithm uses the same representation as from double-and-add.

```
R0 ← 0
R1 ← P
for i from m downto 0 do
    if di = 0 then
        R1 ← point_add(R0, R1)
        R0 ← point_double(R0)
    else
        R0 ← point_add(R0, R1)
        R1 ← point_double(R1)

    // invariant property to maintain correctness
    assert R1 == point_add(R0, P)
return R0
```

This algorithm has in effect the same speed as the double-and-add approach except that it computes the same number of point additions and doubles regardless of the value of the multiplicand *d*. This means that at this level the algorithm does not leak any information through branches or power consumption.

However, it has been shown that through application of a FLUSH+RELOAD side-channel attack on OpenSSL, the full private key can be revealed after performing cache-timing against only one signature at a very low cost.

### Longer chains

Using Lucas chains provides an optimized sequence of doubling and adds compared to the Montgomery ladder, which is faster on larger multiples (longer chains). This method is called "PRAC". PRAC is also published by Montgomery, with the "reference implementation" being GMP-ECM. DJ Bernstein mentions a number of such schemes in 2017.

### Constant time Montgomery ladder

The security of a cryptographic implementation is likely to face the threat of the so-called timing attacks which exploits the data-dependent timing characteristics of the implementation. Machines running cryptographic implementations consume variable amounts of time to process different inputs and so the timings vary based on the encryption key. To resolve this issue, cryptographic algorithms are implemented in a way which removes data dependent variable timing characteristic from the implementation leading to the so-called constant-time implementations. Software implementations are considered to be constant-time in the following sense as stated in: “*avoids all input-dependent branches, all input-dependent array* *indices, and other instructions with input-dependent timings.*” The GitHub page lists coding rules for implementations of cryptographic operations, and more generally for operations involving secret or sensitive values.

The Montgomery ladder is an x -coordinate only algorithm for elliptic curve point multiplication and is based on the double and add rules over a specific set of curves known as Montgomery curve. The algorithm has a conditional branching such that the condition depends on a secret bit. So a straightforward implementation of the ladder won't be constant time and has the potential to leak the secret bit. This problem has been addressed in literature and several constant time implementations are known. The constant time Montgomery ladder algorithm is as given below which uses two functions CSwap and Ladder-Step. In the return value of the algorithm Z2p-2 is the value of Z2−1 computed using the Fermat's little theorem.

```
algorithm Montgomery-Ladder(xP, n) is
    input: An 
  
    
      
        l
      
    
    {\displaystyle l}
  
-bit scalar 
  
    
      
        n
      
    
    {\displaystyle n}
  
 and the 
  
    
      
        x
      
    
    {\displaystyle x}
  
-coordinate 
  
    
      
        
          x
          
            P
          
        
      
    
    {\displaystyle x_{P}}
  
 of a point 
  
    
      
        P
      
    
    {\displaystyle P}
  
.
    output: 
  
    
      
        x
      
    
    {\displaystyle x}
  
-coordinate of 
  
    
      
        n
        P
      
    
    {\displaystyle nP}
  
, the 
  
    
      
        n
      
    
    {\displaystyle n}
  
-times scalar multiple of 
  
    
      
        P
      
    
    {\displaystyle P}
  
.

    X1 ← xP; X2 ← 1; Z2 ← 0; X3 ← xP; Z3 ← 1
    prevbit ← 0

    for 
  
    
      
        i
      
    
    {\displaystyle i}
  
 from 
  
    
      
        l
        −
        1
      
    
    {\displaystyle l-1}
  
 downto 0 do
        bit ← bit-value at index 
  
    
      
        i
      
    
    {\displaystyle i}
  
 of 
  
    
      
        n
      
    
    {\displaystyle n}
  

        b ← bit 
  
    
      
        ⊕
      
    
    {\displaystyle \oplus }
  
 prevbit
        prevbit ← bit
        (
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
) ← CSwap(
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,b)
        (
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
) ← Ladder-Step(
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,X1)
       
    return X2Z2p-2
```

The Ladder-Step function (given below) used within the ladder is the core of the algorithm and is a combined form of the differential add and doubling operations. The field constant a24 is defined as a24 = $(A+2)/4$ , where A is a parameter of the underlying Montgomery curve.

```
Function Ladder-Step(
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,X1)

T1 ← X2 + Z2
T2 ← X2 - Z2
T3 ← X3 + Z3
T4 ← X3 - Z3
T5 ← T12
T6 ← T22
T2 ← T2 · T3
T1 ← T1 · T4
T1 ← T1 + T2
T2 ← T1 - T2
X3 ← T12
T2 ← T22
Z3 ← T2 · X1
X2 ← T5 · T6
T5 ← T5 - T6
T1 ← a24 · T5
T6 ← T6 + T1
Z2 ← T5 · T6

return (
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X2,Z2
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
,
  
    
      
        ⟨
      
    
    {\displaystyle \langle }
  
X3,Z3
  
    
      
        ⟩
      
    
    {\displaystyle \rangle }
  
)
```

The CSwap function manages the conditional branching and helps the ladder to run following the requirements of a constant time implementation. The function swaps the pair of field elements $\langle$ X2,Z2 $\rangle$ and $\langle$ X3,Z3 $\rangle$ only if b = 1 and this is done without leaking any information about the secret bit. Various methods of implementing CSwap have been proposed in literature. A lesser costly option to manage the constant time requirement of the Montgomery ladder is conditional select which is formalised through a function CSelect. This function has been used in various optimisations and has been formally discussed in

Since the inception of the standard Montgomery curve Curve25519 at 128-bit security level, there has been various software implementations to compute the ECDH on various architectures and to achieve best possible performance cryptographic developers have resorted to write the implementations using assembly language of the underlying architecture. The work provided a couple of 64-bit assembly implementations targeting the AMD64 architecture. The implementations were developed using a tool known as *qhasm* which can generate high-speed assembly language cryptographic programs. The function CSwap was used in the implementations of these ladders. After that there has been several attempts to optimise the ladder implementation through hand-written assembly programs out of which the notion of CSelect was first used in and then in. Apart from using sequential instructions, vector instructions have also been used to optimise the ladder computation through various works. Along with AMD64, attempts have also been made to achieve efficient implementations on other architectures like ARM. The works and provides efficient implementations targeting the ARM architecture. The libraries lib25519 and are two state-of-art libraries containing efficient implementations of the Montgomery ladder for Curve25519. Nevertheless, the libraries have implementations of other cryptographic primitives as well.

Apart from Curve25519, there have been several attempts to compute the ladder over other curves at various security levels. Efficient implementations of the ladder over the standard curve Curve448 at 224-bit security level have also been studied in literature. A curve named Curve41417 providing security just over 200 bits was proposed in which a variant of Karatsuba strategy was used to implement the field multiplication needed for the related ECC software. In pursuit of searching Montgomery curves that are competitive to Curve25519 and Curve448 research has been done and couple of curves were proposed along with efficient sequential and vectorised implementations of the corresponding ladders. At 256-bit security level efficient implementations of the ladder have also been addressed through three different Montgomery curves.
