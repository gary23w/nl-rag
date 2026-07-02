---
title: "Fractional Brownian motion"
source: https://en.wikipedia.org/wiki/Fractional_Brownian_motion
domain: brownian-motion
license: CC-BY-SA-4.0
tags: brownian motion, diffusion process, fokker-planck equation, ornstein-uhlenbeck process
fetched: 2026-07-02
---

# Fractional Brownian motion

In probability theory, **fractional Brownian motion** (**fBm**), also called a **fractal Brownian motion**, is a generalization of Brownian motion. Unlike classical Brownian motion, the increments of fBm need not be independent. fBm is a continuous-time Gaussian process ${\textstyle B_{H}(t)}$ on ${\textstyle [0,T]}$ , that starts at zero, has expectation zero for all t in ${\textstyle [0,T]}$ , and has the following covariance function:

$E[B_{H}(t),B_{H}(s)]={\tfrac {1}{2}}(|t|^{2H}+|s|^{2H}-|t-s|^{2H}),$

where *H* is a real number in (0, 1), called the Hurst index or Hurst parameter associated with the fractional Brownian motion. The Hurst exponent describes the raggedness of the resultant motion, with a higher value leading to a smoother motion. It was introduced by Mandelbrot & van Ness (1968).

The value of *H* determines what kind of process the *fBm* is:

- if *H* = 1/2 then the process is in fact a Brownian motion or Wiener process;
- if *H* > 1/2 then the increments of the process are positively correlated;
- if *H* < 1/2 then the increments of the process are negatively correlated.

Fractional Brownian motion has stationary increments *X*(*t*) = *BH*(*s*+*t*) − *BH*(*s*) (the value is the same for any *s*). The increment process *X*(*t*) is known as **fractional Gaussian noise**.

There is also a generalization of fractional Brownian motion: ***n*-th order fractional Brownian motion**, abbreviated as n-fBm. n-fBm is a Gaussian, self-similar, non-stationary process whose increments of order *n* are stationary. For *n* = 1, n-fBm is classical fBm.

Like the Brownian motion that it generalizes, fractional Brownian motion is named after 19th century biologist Robert Brown; fractional Gaussian noise is named after mathematician Carl Friedrich Gauss.

## Background and definition

Prior to the introduction of the fractional Brownian motion, Lévy (1953) used the Riemann–Liouville fractional integral to define the process

${\tilde {B}}_{H}(t)={\frac {1}{\Gamma (H+1/2)}}\int _{0}^{t}(t-s)^{H-1/2}\,dB(s)$

where integration is with respect to the white noise measure *dB*(*s*). This integral turns out to be ill-suited as a definition of fractional Brownian motion because of its over-emphasis of the origin (Mandelbrot & van Ness 1968, p. 424). It does not have stationary increments.

The idea instead is to use a different fractional integral of white noise to define the process: the Weyl integral

$B_{H}(t)=B_{H}(0)+{\frac {1}{\Gamma (H+1/2)}}\left\{\int _{-\infty }^{0}\left[(t-s)^{H-1/2}-(-s)^{H-1/2}\right]\,dB(s)+\int _{0}^{t}(t-s)^{H-1/2}\,dB(s)\right\}$

for *t* > 0 (and similarly for *t* < 0). The resulting process has stationary increments.

The main difference between fractional Brownian motion and regular Brownian motion is that while the increments in Brownian Motion are independent, increments for fractional Brownian motion are not. If H > 1/2, then there is positive autocorrelation: if there is an increasing pattern in the previous steps, then it is likely that the current step will be increasing as well. If H < 1/2, the autocorrelation is negative.

## Properties

### Self-similarity

The process is self-similar, since in terms of probability distributions:

$B_{H}(at)\sim |a|^{H}B_{H}(t).$

This property is due to the fact that the covariance function is homogeneous of order 2H and can be considered as a fractal property. FBm can also be defined as the unique mean-zero Gaussian process, null at the origin, with stationary and self-similar increments.

### Stationary increments

It has stationary increments:

$B_{H}(t)-B_{H}(s)\;\sim \;B_{H}(t-s).$

### Long-range dependence

For *H* > ⁠1/2⁠ the process exhibits long-range dependence,

$\sum _{n=1}^{\infty }E[B_{H}(1)(B_{H}(n+1)-B_{H}(n))]=\infty .$

### Regularity

Sample-paths are almost nowhere differentiable. However, almost-all trajectories are locally Hölder continuous of any order strictly less than *H*: for each such trajectory, for every *T* > 0 and for every *ε* > 0 there exists a (random) constant *c* such that

$|B_{H}(t)-B_{H}(s)|\leq c|t-s|^{H-\varepsilon }$

for 0 < *s*,*t* < *T*.

### Dimension

With probability 1, the graph of *BH*(*t*) has both Hausdorff dimension and box dimension of 2−*H*.

### Integration

As for regular Brownian motion, one can define stochastic integrals with respect to fractional Brownian motion, usually called "fractional stochastic integrals". In general though, unlike integrals with respect to regular Brownian motion, fractional stochastic integrals are not semimartingales.

### Frequency-domain interpretation

Just as Brownian motion can be viewed as white noise filtered by $\omega ^{-2}$ (i.e. integrated), fractional Brownian motion is white noise filtered by $\omega ^{-H-1/2}$ (corresponding to fractional integration).

## Sample paths

Practical computer realisations of an *fBm* can be generated, although they are only a finite approximation. The sample paths chosen can be thought of as showing discrete sampled points on an *fBm* process. Three realizations are shown below, each with 1000 points of an *fBm* with Hurst parameter 0.75.

|   |   |   |
|---|---|---|

Realizations of three different types of *fBm* are shown below, each showing 1000 points, the first with Hurst parameter 0.15, the second with Hurst parameter 0.55, and the third with Hurst parameter 0.95. The higher the Hurst parameter is, the smoother the curve will be.

|   |   |   |
|---|---|---|

### Method 1 of simulation

One can simulate sample-paths of an *fBm* using methods for generating stationary Gaussian processes with known covariance function. The simplest method relies on the Cholesky decomposition method of the covariance matrix (explained below), which on a grid of size n has complexity of order $O(n^{3})$ . A more complex, but computationally faster method is the circulant embedding method of Dietrich & Newsam (1997).

Suppose we want to simulate the values of the *fBM* at times $t_{1},\ldots ,t_{n}$ using the Cholesky decomposition method.

- Form the matrix $\Gamma ={\bigl (}R(t_{i},\,t_{j}),i,j=1,\ldots ,\,n{\bigr )}$ where $\,R(t,s)=(s^{2H}+t^{2H}-|t-s|^{2H})/2$ .
- Compute $\,\Sigma$ the square root matrix of $\,\Gamma$ , i.e. $\,\Sigma ^{2}=\Gamma$ . Loosely speaking, $\,\Sigma$ is the "standard deviation" matrix associated to the variance-covariance matrix $\,\Gamma$ .
- Construct a vector $\,v$ of *n* numbers drawn independently according to a standard Gaussian distribution,
- If we define $\,u=\Sigma v$ then $\,u$ yields a sample path of an *fBm*.

In order to compute $\,\Sigma$ , we can use for instance the Cholesky decomposition method. An alternative method uses the eigenvalues of $\,\Gamma$ :

- Since $\,\Gamma$ is symmetric, positive-definite matrix, it follows that all eigenvalues $\,\lambda _{i}$ of $\,\Gamma$ satisfy $\,\lambda _{i}>0$ , ( $i=1,\dots ,n$ ).
- Let $\,\Lambda$ be the diagonal matrix of the eigenvalues, i.e. $\Lambda _{ij}=\lambda _{i}\,\delta _{ij}$ where $\delta _{ij}$ is the Kronecker delta. We define $\Lambda ^{1/2}$ as the diagonal matrix with entries $\lambda _{i}^{1/2}$ , i.e. $\Lambda _{ij}^{1/2}=\lambda _{i}^{1/2}\,\delta _{ij}$ .

Note that the result is real-valued because $\lambda _{i}>0$ .

- Let $\,v_{i}$ an eigenvector associated to the eigenvalue $\,\lambda _{i}$ . Define $\,P$ as the matrix whose i -th column is the eigenvector $\,v_{i}$ .

Note that since the eigenvectors are linearly independent, the matrix $\,P$ is invertible.

- It follows then that $\Sigma =P\,\Lambda ^{1/2}\,P^{-1}$ because $\Gamma =P\,\Lambda \,P^{-1}$ .

### Method 2 of simulation

It is also known that

$B_{H}(t)=\int _{0}^{t}K_{H}(t,s)\,dB(s)$

where *B* is a standard Brownian motion and

$K_{H}(t,s)={\frac {(t-s)^{H-{\frac {1}{2}}}}{\Gamma (H+{\frac {1}{2}})}}\;_{2}F_{1}\left(H-{\frac {1}{2}};\,{\frac {1}{2}}-H;\;H+{\frac {1}{2}};\,1-{\frac {t}{s}}\right).$

Where $_{2}F_{1}$ is the Euler hypergeometric integral.

Say we want to simulate an *fBm* at points $0=t_{0}<t_{1}<\cdots <t_{n}=T$ .

- Construct a vector of *n* numbers drawn according to a standard Gaussian distribution.
- Multiply it component-wise by √*T*/*n* to obtain the increments of a Brownian motion on [0, *T*]. Denote this vector by $(\delta B_{1},\ldots ,\delta B_{n})$ .
- For each $t_{j}$ , compute

$B_{H}(t_{j})={\frac {n}{T}}\sum _{i=0}^{j-1}\int _{t_{i}}^{t_{i+1}}K_{H}(t_{j},\,s)\,ds\ \delta B_{i}.$

The integral may be efficiently computed by Gaussian quadrature.
