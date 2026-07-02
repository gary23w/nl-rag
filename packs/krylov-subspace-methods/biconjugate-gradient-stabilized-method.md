---
title: "Biconjugate gradient stabilized method"
source: https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method
domain: krylov-subspace-methods
license: CC-BY-SA-4.0
tags: krylov subspace, generalized minimal residual method, arnoldi iteration, lanczos algorithm
fetched: 2026-07-02
---

# Biconjugate gradient stabilized method

In numerical linear algebra, the **biconjugate gradient stabilized method**, often abbreviated as **BiCGSTAB**, is an iterative method developed by H. A. van der Vorst for the numerical solution of nonsymmetric linear systems. It is a variant of the biconjugate gradient method (BiCG) and has faster and smoother convergence than the original BiCG as well as other variants such as the conjugate gradient squared method (CGS). It is a Krylov subspace method. Unlike the original BiCG method, it doesn't require multiplication by the transpose of the system matrix.

## Algorithmic steps

### Unpreconditioned BiCGSTAB

In the following sections, (***x***,***y***) = ***x***T ***y*** denotes the dot product of vectors. To solve a linear system ***Ax*** = ***b***, BiCGSTAB starts with an initial guess ***x***0 and proceeds as follows:

1. ***r***0 = ***b*** − ***Ax***0
2. Choose an arbitrary vector ***r̂***0 such that (***r̂***0, ***r***0) ≠ 0, e.g., ***r̂***0 = ***r***0
3. *ρ*0 = (***r̂***0, ***r***0)
4. ***p***0 = ***r***0
5. For *i* = 1, 2, 3, …
  1. ***v*** = ***Ap****i*−1
  2. *α* = *ρ**i*−1/(***r̂***0, ***v***)
  3. ***h*** = ***x****i*−1 + *α**p****i*−1
  4. ***s*** = ***r****i*−1 − *α**v***
  5. If ***h*** is accurate enough, i.e., if ***s*** is small enough, then set ***x**i* = ***h*** and quit
  6. ***t*** = ***As***
  7. *ω* = (***t***, ***s***)/(***t***, ***t***)
  8. ***x**i* = ***h*** + *ω**s***
  9. ***r**i* = ***s*** − *ω**t***
  10. If ***x**i* is accurate enough, i.e., if ***r**i* is small enough, then quit
  11. *ρi* = (***r̂***0, ***r****i*)
  12. *β* = (*ρi*/*ρ**i*−1)(*α*/*ω*)
  13. ***p**i* = ***r****i* + *β*(***p****i*−1 − *ω****v***)

In some cases, choosing the vector ***r̂***0 randomly improves numerical stability.

### Preconditioned BiCGSTAB

Preconditioners are usually used to accelerate convergence of iterative methods. To solve a linear system ***Ax*** = ***b*** with a preconditioner ***K*** = ***K***1***K***2 ≈ ***A***, preconditioned BiCGSTAB starts with an initial guess ***x***0 and proceeds as follows:

1. ***r***0 = ***b*** − ***Ax***0
2. Choose an arbitrary vector ***r̂***0 such that (***r̂***0, ***r***0) ≠ 0, e.g., ***r̂***0 = ***r***0
3. *ρ*0 = (***r̂***0, ***r***0)
4. ***p***0 = ***r***0
5. For *i* = 1, 2, 3, …
  1. ***y*** = ***K*** −1 2 ***K*** −1 1 ***p****i*−1
  2. ***v*** = ***Ay***
  3. *α* = *ρ**i*−1/(***r̂***0, ***v***)
  4. ***h*** = ***x****i*−1 + *α**y***
  5. ***s*** = ***r****i*−1 − *α**v***
  6. If ***h*** is accurate enough then ***x**i* = ***h*** and quit
  7. ***z*** = ***K*** −1 2 ***K*** −1 1 ***s***
  8. ***t*** = ***Az***
  9. *ω* = (***K*** −1 1 ***t***, ***K*** −1 1 ***s***)/(***K*** −1 1 ***t***, ***K*** −1 1 ***t***)
  10. ***x**i* = ***h*** + *ω**z***
  11. ***r**i* = ***s*** − *ω**t***
  12. If ***x**i* is accurate enough then quit
  13. *ρi* = (***r̂***0, ***r****i*)
  14. *β* = (*ρi*/*ρ**i*−1)(*α*/*ω*)
  15. ***p**i* = ***r****i* + *β*(***p****i*−1 − *ω****v***)

This formulation is equivalent to applying unpreconditioned BiCGSTAB to the explicitly preconditioned system

Ãx̃

=

b̃

with ***Ã*** = ***K*** −1 1 ***A******K*** −1 2 , ***x̃*** = ***K***2***x*** and ***b̃*** = ***K*** −1 1 ***b***. In other words, both left- and right-preconditioning are possible with this formulation.

## Derivation

### BiCG in polynomial form

In BiCG, the search directions ***p**i* and ***p̂****i* and the residuals ***r**i* and ***r̂****i* are updated using the following recurrence relations:

p

i

=

r

i

−1

+

β

i

p

i

−1

,

p̂

i

=

r̂

i

−1

+

β

i

p̂

i

−1

,

r

i

=

r

i

−1

−

α

i

Ap

i

,

r̂

i

=

r̂

i

−1

−

α

i

A

T

p̂

i

.

The constants *αi* and *βi* are chosen to be

α

i

=

ρ

i

/(

p̂

i

,

Ap

i

)

,

β

i

=

ρ

i

/

ρ

i

−1

where *ρi* = (***r̂****i*−1, ***r****i*−1) so that the residuals and the search directions satisfy biorthogonality and biconjugacy, respectively, i.e., for *i* ≠ *j*,

(

r̂

i

,

r

j

) = 0

,

(

p̂

i

,

Ap

j

) = 0

.

It is straightforward to show that

r

i

=

P

i

(

A

)

r

0

,

r̂

i

=

P

i

(

A

T

)

r̂

0

,

p

i

+1

=

T

i

(

A

)

r

0

,

p̂

i

+1

=

T

i

(

A

T

)

r̂

0

where *Pi*(***A***) and *Ti*(***A***) are *i*th-degree polynomials in ***A***. These polynomials satisfy the following recurrence relations:

P

i

(

A

) =

P

i

−1

(

A

) −

α

i

A

T

i

−1

(

A

)

,

T

i

(

A

) =

P

i

(

A

) +

β

i

+1

T

i

−1

(

A

)

.

### Derivation of BiCGSTAB from BiCG

It is unnecessary to explicitly keep track of the residuals and search directions of BiCG. In other words, the BiCG iterations can be performed implicitly. In BiCGSTAB, one wishes to have recurrence relations for

r̃

i

=

Q

i

(

A

)

P

i

(

A

)

r

0

where *Qi*(***A***) = (***I*** − *ω*1***A***)(***I*** − *ω*2***A***)⋯(***I*** − *ωi**A***) with suitable constants *ωj* instead of ***r**i* = *Pi*(***A***)***r**0* in the hope that *Qi*(***A***) will enable faster and smoother convergence in ***r̃**i* than ***r**i*.

It follows from the recurrence relations for *Pi*(***A***) and *Ti*(***A***) and the definition of *Qi*(***A***) that

Q

i

(

A

)

P

i

(

A

)

r

0

= (

I

−

ω

i

A

)(

Q

i

−1

(

A

)

P

i

−1

(

A

)

r

0

−

α

i

A

Q

i

−1

(

A

)

T

i

−1

(

A

)

r

0

)

,

which entails the necessity of a recurrence relation for *Qi*(***A***)*Ti*(***A***)***r***0. This can also be derived from the BiCG relations:

Q

i

(

A

)

T

i

(

A

)

r

0

=

Q

i

(

A

)

P

i

(

A

)

r

0

+

β

i

+1

(

I

−

ω

i

A

)

Q

i

−1

(

A

)

T

i

−1

(

A

)

r

0

.

Similarly to defining ***r̃**i*, BiCGSTAB defines

p̃

i

+1

=

Q

i

(

A

)

T

i

(

A

)

r

0

.

Written in vector form, the recurrence relations for ***p̃****i* and ***r̃****i* are

p̃

i

=

r̃

i

−1

+

β

i

(

I

−

ω

i

−1

A

)

p̃

i

−1

,

r̃

i

= (

I

−

ω

i

A

)(

r̃

i

−1

−

α

i

A

p̃

i

)

.

To derive a recurrence relation for ***x**i*, define

s

i

=

r̃

i

−1

−

α

i

A

p̃

i

.

The recurrence relation for ***r̃****i* can then be written as

r̃

i

=

r̃

i

−1

−

α

i

A

p̃

i

−

ω

i

As

i

,

which corresponds to

x

i

=

x

i

−1

+

α

i

p̃

i

+

ω

i

s

i

.

### Determination of BiCGSTAB constants

Now it remains to determine the BiCG constants *αi* and *βi* and choose a suitable *ωi*.

In BiCG, *βi* = *ρi*/*ρ**i*−1 with

ρ

i

= (

r̂

i

−1

,

r

i

−1

) = (

P

i

−1

(

A

T

)

r̂

0

,

P

i

−1

(

A

)

r

0

)

.

Since BiCGSTAB does not explicitly keep track of ***r̂****i* or ***r****i*, *ρi* is not immediately computable from this formula. However, it can be related to the scalar

ρ̃

i

= (

Q

i

−1

(

A

T

)

r̂

0

,

P

i

−1

(

A

)

r

0

) = (

r̂

0

,

Q

i

−1

(

A

)

P

i

−1

(

A

)

r

0

) = (

r̂

0

,

r

i

−1

)

.

Due to biorthogonality, ***r****i*−1 = *P**i*−1(***A***)***r***0 is orthogonal to *U**i*−2(***A***T)***r̂***0 where *U**i*−2(***A***T) is any polynomial of degree *i* − 2 in ***A***T. Hence, only the highest-order terms of *P**i*−1(***A***T) and *Q**i*−1(***A***T) matter in the dot products (*P**i*−1(***A***T)***r̂***0, *P**i*−1(***A***)***r***0) and (*Q**i*−1(***A***T)***r̂***0, *P**i*−1(***A***)***r***0). The leading coefficients of *P**i*−1(***A***T) and *Q**i*−1(***A***T) are (−1)*i*−1*α*1*α*2⋯*α**i*−1 and (−1)*i*−1*ω*1*ω*2⋯*ω**i*−1, respectively. It follows that

ρ

i

= (

α

1

/

ω

1

)(

α

2

/

ω

2

)⋯(

α

i

−1

/

ω

i

−1

)

ρ̃

i

,

and thus

β

i

=

ρ

i

/

ρ

i

−1

= (

ρ̃

i

/

ρ̃

i

−1

)(

α

i

−1

/

ω

i

−1

)

.

A simple formula for *αi* can be similarly derived. In BiCG,

α

i

=

ρ

i

/(

p̂

i

,

Ap

i

) = (

P

i

−1

(

A

T

)

r̂

0

,

P

i

−1

(

A

)

r

0

)/(

T

i

−1

(

A

T

)

r̂

0

,

A

T

i

−1

(

A

)

r

0

)

.

Similarly to the case above, only the highest-order terms of *P**i*−1(***A***T) and *T**i*−1(***A***T) matter in the dot products thanks to biorthogonality and biconjugacy. It happens that *P**i*−1(***A***T) and *T**i*−1(***A***T) have the same leading coefficient. Thus, they can be replaced simultaneously with *Q**i*−1(***A***T) in the formula, which leads to

α

i

= (

Q

i

−1

(

A

T

)

r̂

0

,

P

i

−1

(

A

)

r

0

)/(

Q

i

−1

(

A

T

)

r̂

0

,

A

T

i

−1

(

A

)

r

0

) =

ρ̃

i

/(

r̂

0

,

A

Q

i

−1

(

A

)

T

i

−1

(

A

)

r

0

) =

ρ̃

i

/(

r̂

0

,

Ap̃

i

)

.

Finally, BiCGSTAB selects *ωi* to minimize ***r̃****i* = (**I** − *ωi**A***)***s**i* in 2-norm as a function of *ωi*. This is achieved when

((

I

−

ω

i

A

)

s

i

,

As

i

) = 0

,

giving the optimal value

ω

i

= (

As

i

,

s

i

)/(

As

i

,

As

i

)

.

## Generalization

BiCGSTAB can be viewed as a combination of BiCG and GMRES where each BiCG step is followed by a GMRES(1) (i.e., GMRES restarted at each step) step to repair the irregular convergence behavior of CGS, as an improvement of which BiCGSTAB was developed. However, due to the use of degree-one minimum residual polynomials, such repair may not be effective if the matrix ***A*** has large complex eigenpairs. In such cases, BiCGSTAB is likely to stagnate, as confirmed by numerical experiments.

One may expect that higher-degree minimum residual polynomials may better handle this situation. This gives rise to algorithms including BiCGSTAB2[1] and the more general BiCGSTAB(*l*)[2]. In BiCGSTAB(*l*), a GMRES(*l*) step follows every *l* BiCG steps. BiCGSTAB2 is equivalent to BiCGSTAB(*l*) with *l* = 2.
