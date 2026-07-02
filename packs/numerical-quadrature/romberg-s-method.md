---
title: "Romberg's method"
source: https://en.wikipedia.org/wiki/Romberg%27s_method
domain: numerical-quadrature
license: CC-BY-SA-4.0
tags: numerical integration, simpson's rule, romberg method, adaptive quadrature
fetched: 2026-07-02
---

# Romberg's method

In numerical analysis, **Romberg's method** is used to estimate the definite integral $\int _{a}^{b}f(x)\,dx$ by applying Richardson extrapolation repeatedly on the trapezium rule or the rectangle rule (midpoint rule). The estimates generate a triangular array. Romberg's method is a Newton–Cotes formula – it evaluates the integrand at equally spaced points. The integrand must have continuous derivatives, though fairly good results may be obtained if only a few derivatives exist. If it is possible to evaluate the integrand at unequally spaced points, then other methods such as Gaussian quadrature and Clenshaw–Curtis quadrature are generally more accurate.

The method is named after Werner Romberg, who published the method in 1955.

## Method

Using ${\textstyle h_{n}={\frac {(b-a)}{2^{n+1}}}}$ , the method can be inductively defined by ${\begin{aligned}R(0,0)&=h_{0}(f(a)+f(b))\\R(n,0)&={\tfrac {1}{2}}R(n{-}1,\,0)+2h_{n}\sum _{k=1}^{2^{n-1}}f(a+(2k-1)h_{n-1})\\R(n,m)&=R(n,\,m{-}1)+{\tfrac {1}{4^{m}-1}}(R(n,\,m{-}1)-R(n{-}1,\,m{-}1))\\&={\frac {1}{4^{m}-1}}(4^{m}R(n,\,m{-}1)-R(n{-}1,\,m{-}1))\end{aligned}}$ where $n\geq m$ and $m\geq 1\,$ . In big O notation, the error for *R*(*n*, *m*) is: $O{\left(h_{n}^{2m+2}\right)}.$

The zeroth extrapolation, *R*(*n*, 0), is equivalent to the trapezoidal rule with 2*n* + 1 points; the first extrapolation, *R*(*n*, 1), is equivalent to Simpson's rule with 2*n* + 1 points. The second extrapolation, *R*(*n*, 2), is equivalent to Boole's rule with 2*n* + 1 points. The further extrapolations differ from Newton-Cotes formulas. In particular further Romberg extrapolations expand on Boole's rule in very slight ways, modifying weights into ratios similar as in Boole's rule. In contrast, further Newton-Cotes methods produce increasingly differing weights, eventually leading to large positive and negative weights. This is indicative of how large degree interpolating polynomial Newton-Cotes methods fail to converge for many integrals, while Romberg integration is more stable.

By labelling our ${\textstyle O(h^{2})}$ approximations as ${\textstyle A_{0}{\big (}{\frac {h}{2^{n}}}{\big )}}$ instead of ${\textstyle R(n,0)}$ , we can perform Richardson extrapolation with the error formula defined below: $\int _{a}^{b}f(x)\,dx=A_{0}{\bigg (}{\frac {h}{2^{n}}}{\bigg )}+a_{0}{\bigg (}{\frac {h}{2^{n}}}{\bigg )}^{2}+a_{1}{\bigg (}{\frac {h}{2^{n}}}{\bigg )}^{4}+a_{2}{\bigg (}{\frac {h}{2^{n}}}{\bigg )}^{6}+\cdots$ Once we have obtained our ${\textstyle O(h^{2(m+1)})}$ approximations ${\textstyle A_{m}{\big (}{\frac {h}{2^{n}}}{\big )}}$ , we can label them as ${\textstyle R(n,m)}$ .

When function evaluations are expensive, it may be preferable to replace the polynomial interpolation of Richardson with the rational interpolation proposed by Bulirsch & Stoer (1967).

## A geometric example

To estimate the area under a curve the trapezoid rule is applied first to one-piece, then two, then four, and so on.

After trapezoid rule estimates are obtained, Richardson extrapolation is applied.

- For the first iteration the two piece and one piece estimates are used in the formula ⁠4 × (more accurate) − (less accurate)/3⁠. The same formula is then used to compare the four piece and the two piece estimate, and likewise for the higher estimates
- For the second iteration the values of the first iteration are used in the formula ⁠16 × (more accurate) − (less accurate)/15⁠
- The third iteration uses the next power of 4: ⁠64 × (more accurate) − (less accurate)/63⁠ on the values derived by the second iteration.
- The pattern is continued until there is one estimate.

| Number of pieces | Trapezoid estimates | First iteration | Second iteration | Third iteration |
|---|---|---|---|---|
|   |   | ⁠4 MA − LA/3⁠ | ⁠16 MA − LA/15⁠ | ⁠64 MA − LA/63⁠ |
| 1 | 0 | ⁠4×16 − 0/3⁠ = 21.333... | ⁠16×34.667 − 21.333/15⁠ = 35.556... | ⁠64×42.489 − 35.556/63⁠ = 42.599... |
| 2 | 16 | ⁠4×30 − 16/3⁠ = 34.666... | ⁠16×42 − 34.667/15⁠ = 42.489... |   |
| 4 | 30 | ⁠4×39 − 30/3⁠ = 42 |   |   |
| 8 | 39 |   |   |   |

## Example

As an example, the Gaussian function is integrated from 0 to 1, i.e. the error function erf(1) ≈ 0.842700792949715. The triangular array is calculated row by row and calculation is terminated if the two last entries in the last row differ less than 10−8.

```
0.77174333
0.82526296  0.84310283
0.83836778  0.84273605  0.84271160
0.84161922  0.84270304  0.84270083  0.84270066
0.84243051  0.84270093  0.84270079  0.84270079  0.84270079
```

The result in the lower right corner of the triangular array is accurate to the digits shown. It is remarkable that this result is derived from the less accurate approximations obtained by the trapezium rule in the first column of the triangular array.

## Implementation

Here is an example of a computer implementation of the Romberg method (in the C programming language):

```mw
#include <stdio.h>
#include <math.h>

void print_row(size_t i, double *R) {
  printf("R[%2zu] = ", i);
  for (size_t j = 0; j <= i; ++j) {
    printf("%f ", R[j]);
  }
  printf("\n");
}

/*
INPUT:
(*f) : pointer to the function to be integrated
a    : lower limit
b    : upper limit
max_steps: maximum steps of the procedure
acc  : desired accuracy

OUTPUT:
Rp[max_steps-1]: approximate value of the integral of the function f for x in [a,b] with accuracy 'acc' and steps 'max_steps'.
*/
double romberg(double (*f)(double), double a, double b, size_t max_steps, double acc) 
{
  double R1[max_steps], R2[max_steps]; // buffers
  double *Rp = &R1[0], *Rc = &R2[0]; // Rp is previous row, Rc is current row
  double h = b-a; //step size
  Rp[0] = (f(a) + f(b))*h*0.5; // first trapezoidal step

  print_row(0, Rp);

  for (size_t i = 1; i < max_steps; ++i) {
    h /= 2.;
    double c = 0;
    size_t ep = 1 << (i-1); //2^(n-1)
    for (size_t j = 1; j <= ep; ++j) {
      c += f(a + (2*j-1) * h);
    }
    Rc[0] = h*c + .5*Rp[0]; // R(i,0)

    for (size_t j = 1; j <= i; ++j) {
      double n_k = pow(4, j);
      Rc[j] = (n_k*Rc[j-1] - Rp[j-1]) / (n_k-1); // compute R(i,j)
    }

    // Print ith row of R, R[i,i] is the best estimate so far
    print_row(i, Rc);

    if (i > 1 && fabs(Rp[i-1]-Rc[i]) < acc) {
      return Rc[i];
    }

    // swap Rn and Rc as we only need the last row
    double *rt = Rp;
    Rp = Rc;
    Rc = rt;
  }
  return Rp[max_steps-1]; // return our best guess
}
```

Here is an implementation of the Romberg method (in the Python programming language):

```mw
from numpy import arange

def romberg(f,a,b,maxorder):
    """
    Approximates an integral using Romberg integration.
        Args:
            f: The function to integrate.
            a: Lower limit of integration.
            b: Upper limit of integration.
            maxorder: Maximum recursion depth
        Returns:
            The approximate value of the integral.
    """
    assert a < b and isinstance(maxorder,int)
    minstepsize = float( (1./2)**maxorder * (b-a) )
    # algorithm is simplified and accelerated by caching
    f=memorize(f)
    @memorize
    def rule(h, order):
        if ( order == 1 ):
            partial_sum = (f(a) + f(b))/2
            partial_sum += sum(map(f, arange(a+h, b-h/2, h)))
            return h*partial_sum
        # Richardson extrapolation formula
        W = 4.**(order-1)
        return (W*rule(h, order-1) - rule(2*h, order-1)) / (W - 1)
    return rule(minstepsize, maxorder)

def memorize(f):
    _cache_ = dict()
    def cachedf(*argv):
        if not ( argv in _cache_):
            _cache_[argv] = f(*argv)
        return _cache_[argv]
    cachedf._cache_ = _cache_
    return cachedf

def main():
    from numpy import sin, exp, pi
    # Example: integrate sin(x)*exp(x/6)+x over [0,2pi]
    a,b,f = 0, 2*pi, lambda x : sin(x)*exp(x/6) + x
    exact = 36*(1-exp(pi/3))/37 + 2*pi**2
    print("Order     Value       Rel_Err\n"+'-'*30)
    for maxorder in range(1,9):
        value = romberg(f, a, b, maxorder)
        err = abs(value - exact)/exact
        print('%2d'%maxorder, '%.15f'%value, '%1.1e'%err)

main()
```
