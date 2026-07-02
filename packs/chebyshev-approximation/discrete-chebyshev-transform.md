---
title: "Discrete Chebyshev transform"
source: https://en.wikipedia.org/wiki/Discrete_Chebyshev_transform
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
---

# Discrete Chebyshev transform

In applied mathematics, a **discrete Chebyshev transform** (abbreviated DCT, DChT, or DTT) is an analog of the discrete Fourier transform for a function of a real interval, converting in either direction between function values at a set of Chebyshev nodes and coefficients of a function in Chebyshev polynomial basis. Like the Chebyshev polynomials, it is named after Pafnuty Chebyshev.

The two most common types of discrete Chebyshev transforms use the grid of Chebyshev zeros, the zeros of the Chebyshev polynomials of the first kind $T_{n}(x)$ and the grid of Chebyshev extrema, the extrema of the Chebyshev polynomials of the first kind, which are also the *zeros* of the Chebyshev polynomials of the second kind $U_{n}(x)$ . Both of these transforms result in coefficients of Chebyshev polynomials of the first kind.

Other discrete Chebyshev transforms involve related grids and coefficients of Chebyshev polynomials of the second, third, or fourth kinds.

## Roots grid

The discrete Chebyshev transform of ${u(x)}$ at the points ${x_{n}}$ is given by:

$a_{m}={\frac {p_{m}}{N}}\sum _{n=0}^{N-1}u(x_{n})T_{m}(x_{n}),$

where

$x_{n}=-\cos {\frac {{\bigl (}n+{\tfrac {1}{2}}{\bigr )}\pi }{N}},$

$a_{m}={\frac {p_{m}}{N}}\sum _{n=0}^{N-1}u(x_{n})\cos \left(m\cos ^{-1}(x_{n})\right),$

with $p_{m}=1$ if and only if $m=0$ and $p_{m}=2$ otherwise.

Using the definition of $x_{n}$ ,

${\begin{aligned}a_{m}&={\frac {p_{m}}{N}}\sum _{n=0}^{N-1}u(x_{n})\cos {\frac {m{\bigl (}N+n+{\tfrac {1}{2}}{\bigr )}\pi }{N}}\\&={\frac {p_{m}}{N}}\sum _{n=0}^{N-1}u(x_{n})(-1)^{m}\cos {\frac {m{\bigl (}n+{\tfrac {1}{2}}{\bigr )}\pi }{N}}.\end{aligned}}$

The inverse transform is

$u_{n}=\sum _{m=0}^{N-1}a_{m}T_{m}(x_{n})=\sum _{m=0}^{N-1}a_{m}(-1)^{m}\cos {\frac {m{\bigl (}n+{\tfrac {1}{2}}{\bigr )}\pi }{N}}.$

(This is the standard Chebyshev series evaluated on the roots grid.)

This discrete Chebyshev transform can be computed by manipulating the input arguments to a discrete cosine transform, for example, using the following MATLAB code:

```mw
function a=fct(f, l)
% x =-cos(pi/N*((0:N-1)'+1/2));

f = f(end:-1:1,:);
A = size(f); N = A(1); 
if exist('A(3)', 'var') && A(3)~=1
    for i=1:A(3)
        a(:,:,i) = sqrt(2/N) * dct(f(:,:,i));
        a(1,:,i) = a(1,:,i) / sqrt(2);
    end
else
    a = sqrt(2/N) * dct(f(:,:,i));
    a(1,:)=a(1,:) / sqrt(2);
end
```

MATLAB's built-in `dct` (discrete cosine transform) function is implemented using the fast Fourier transform.

The inverse transform is given by the MATLAB code:

```mw
function f=ifct(a, l)
% x = -cos(pi/N*((0:N-1)'+1/2)) 
k = size(a); N=k(1);

a = idct(sqrt(N/2) * [a(1,:) * sqrt(2); a(2:end,:)]);

end
```

## Extrema grid

This transform uses the grid:

$x_{n}=-\cos {\frac {n\pi }{N}}$

$T_{n}(x_{m})=\cos \left({\frac {mn\pi }{N}}+n\pi \right)=(-1)^{n}\cos {\frac {mn\pi }{N}}$

This extrema grid is more widely used.

In this case the transform and its inverse are

$u(x_{n})=u_{n}=\sum _{m=0}^{N}a_{m}T_{m}(x_{n}),$

$a_{m}={\frac {p_{m}}{N}}{\biggl (}{\tfrac {1}{2}}{\bigl (}u_{0}(-1)^{m}+u_{N}{\bigr )}+\sum _{n=1}^{N-1}u_{n}T_{m}(x_{n}){\biggr )},$

where $p_{m}=1$ if and only if $m=0$ or $m=N$ and $p_{m}=2$ otherwise.

## Usage and implementations

The primary uses of the discrete Chebyshev transform are numerical integration, interpolation, and stable numerical differentiation. An implementation which provides these features is given in the C++ library Boost.
