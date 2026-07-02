---
title: "Convolution theorem"
source: https://en.wikipedia.org/wiki/Convolution_theorem
domain: integral-transforms
license: CC-BY-SA-4.0
tags: integral transform, hilbert transform, hartley transform, convolution theorem
fetched: 2026-07-02
---

# Convolution theorem

In mathematics, the **convolution theorem** states that under suitable conditions the Fourier transform of a convolution of two functions (or signals) is the product of their Fourier transforms. More generally, convolution in one domain (e.g., time domain) equals point-wise multiplication in the other domain (e.g., frequency domain). Other versions of the convolution theorem are applicable to various Fourier-related transforms.

## Functions of a continuous variable

Consider two functions $u(x)$ and $v(x)$ with Fourier transforms U and V :

${\begin{aligned}U(f)&\triangleq {\mathcal {F}}\{u\}(f)=\int _{-\infty }^{\infty }u(x)e^{-i2\pi fx}\,dx,\quad f\in \mathbb {R} \\[1ex]V(f)&\triangleq {\mathcal {F}}\{v\}(f)=\int _{-\infty }^{\infty }v(x)e^{-i2\pi fx}\,dx,\quad f\in \mathbb {R} \end{aligned}}$

where ${\mathcal {F}}$ denotes the **Fourier transform operator**. The transform may be normalized in other ways, in which case constant scaling factors (typically $2\pi$ or ${\sqrt {2\pi }}$ ) will appear in the convolution theorem below. The convolution of u and v is defined by:

$r(x)=\{u*v\}(x)\triangleq \int _{-\infty }^{\infty }u(\tau )v(x-\tau )\,d\tau =\int _{-\infty }^{\infty }u(x-\tau )v(\tau )\,d\tau .$

In this context the asterisk denotes convolution, instead of standard multiplication. The tensor product symbol $\otimes$ is sometimes used instead.

The **convolution theorem** states that:

$R(f)\triangleq {\mathcal {F}}\{r\}(f)=U(f)V(f).\quad f\in \mathbb {R}$    (Eq.1a)

Applying the inverse Fourier transform ${\mathcal {F}}^{-1},$ produces the corollary**:**

Convolution theorem

$r(x)=\{u*v\}(x)={\mathcal {F}}^{-1}\{U\cdot V\}.$    (Eq.1b)

The theorem also generally applies to multi-dimensional functions.

| Multi-dimensional derivation of Eq.1 |
|---|
| Consider functions $u,v$ in L*p*-space $L^{1}(\mathbb {R} ^{n}),$ with Fourier transforms $U,V$ **:** ${\begin{aligned}U(f)&\triangleq {\mathcal {F}}\{u\}(f)=\int _{\mathbb {R} ^{n}}u(x)e^{-i2\pi f\cdot x}\,dx,\quad f\in \mathbb {R} ^{n}\\V(f)&\triangleq {\mathcal {F}}\{v\}(f)=\int _{\mathbb {R} ^{n}}v(x)e^{-i2\pi f\cdot x}\,dx,\end{aligned}}$ where $f\cdot x$ indicates the inner product of $\mathbb {R} ^{n}$ :   $f\cdot x=\sum _{j=1}^{n}{f}_{j}x_{j},$   and   $dx=\prod _{j=1}^{n}dx_{j}.$ The convolution of u and v is defined by**:** $r(x)\triangleq \int _{\mathbb {R} ^{n}}u(\tau )v(x-\tau )\,d\tau .$ Also: $\iint \|u(\tau )v(x-\tau )\|\,dx\,d\tau =\int \left(\|u(\tau )\|\int \|v(x-\tau )\|\,dx\right)\,d\tau =\int \|u(\tau )\|\,\\|v\\|_{1}\,d\tau =\\|u\\|_{1}\\|v\\|_{1}.$ Hence by Fubini's theorem we have that $r\in L^{1}(\mathbb {R} ^{n})$ so its Fourier transform R is defined by the integral formula**:** ${\begin{aligned}R(f)\triangleq {\mathcal {F}}\{r\}(f)&=\int _{\mathbb {R} ^{n}}r(x)e^{-i2\pi f\cdot x}\,dx\\&=\int _{\mathbb {R} ^{n}}\left(\int _{\mathbb {R} ^{n}}u(\tau )v(x-\tau )\,d\tau \right)\,e^{-i2\pi f\cdot x}\,dx.\end{aligned}}$ Note that $\|u(\tau )v(x-\tau )e^{-i2\pi f\cdot x}\|=\|u(\tau )v(x-\tau )\|,$   Hence by the argument above we may apply Fubini's theorem again (i.e. interchange the order of integration): ${\begin{aligned}R(f)&=\int _{\mathbb {R} ^{n}}u(\tau )\underbrace {\left(\int _{\mathbb {R} ^{n}}v(x-\tau )\ e^{-i2\pi f\cdot x}\,dx\right)} _{V(f)\ e^{-i2\pi f\cdot \tau }}\,d\tau \\&=\underbrace {\left(\int _{\mathbb {R} ^{n}}u(\tau )\ e^{-i2\pi f\cdot \tau }\,d\tau \right)} _{U(f)}\ V(f).\end{aligned}}$ |

This theorem also holds for the Laplace transform, the two-sided Laplace transform and, when suitably modified, for the Mellin transform and Hartley transform (see Mellin inversion theorem). It can be extended to the Fourier transform of abstract harmonic analysis defined over locally compact abelian groups.

### Periodic convolution (Fourier series coefficients)

Consider P -periodic functions $u_{_{P}}$  and   $v_{_{P}},$ which can be expressed as periodic summations:

$u_{_{P}}(x)\ \triangleq \sum _{m=-\infty }^{\infty }u(x-mP)$ and $v_{_{P}}(x)\ \triangleq \sum _{m=-\infty }^{\infty }v(x-mP).$

In practice the non-zero portion of components u and v are often limited to duration $P,$ but nothing in the theorem requires that.

The Fourier series coefficients are:

${\begin{aligned}U[k]&\triangleq {\mathcal {F}}\{u_{_{P}}\}[k]={\frac {1}{P}}\int _{P}u_{_{P}}(x)e^{-i2\pi kx/P}\,dx,\quad k\in \mathbb {Z} ;\quad \quad \scriptstyle {\text{integration over any interval of length }}P\\V[k]&\triangleq {\mathcal {F}}\{v_{_{P}}\}[k]={\frac {1}{P}}\int _{P}v_{_{P}}(x)e^{-i2\pi kx/P}\,dx,\quad k\in \mathbb {Z} \end{aligned}}$

where ${\mathcal {F}}$ denotes the **Fourier series integral**.

- The product: $u_{_{P}}(x)\cdot v_{_{P}}(x)$ is also P -periodic, and its Fourier series coefficients are given by the discrete convolution of the U and V sequences: ${\mathcal {F}}\{u_{_{P}}\cdot v_{_{P}}\}[k]=\{U*V\}[k].$
- The convolution: ${\begin{aligned}\{u_{_{P}}*v\}(x)\ &\triangleq \int _{-\infty }^{\infty }u_{_{P}}(x-\tau )\cdot v(\tau )\ d\tau \\&\equiv \int _{P}u_{_{P}}(x-\tau )\cdot v_{_{P}}(\tau )\ d\tau ;\quad \quad \scriptstyle {\text{integration over any interval of length }}P\end{aligned}}$ is also P -periodic, and is called a **periodic convolution**.

| Derivation of periodic convolution |
|---|
| ${\begin{aligned}\int _{-\infty }^{\infty }u_{_{P}}(x-\tau )\cdot v(\tau )\,d\tau &=\sum _{k=-\infty }^{\infty }\left[\int _{x_{o}+kP}^{x_{o}+(k+1)P}u_{_{P}}(x-\tau )\cdot v(\tau )\ d\tau \right]\quad x_{0}{\text{ is an arbitrary parameter}}\\&=\sum _{k=-\infty }^{\infty }\left[\int _{x_{o}}^{x_{o}+P}\underbrace {u_{_{P}}(x-\tau -kP)} _{u_{_{P}}(x-\tau ),{\text{ by periodicity}}}\cdot v(\tau +kP)\ d\tau \right]\quad {\text{substituting }}\tau \rightarrow \tau +kP\\&=\int _{x_{o}}^{x_{o}+P}u_{_{P}}(x-\tau )\cdot \underbrace {\left[\sum _{k=-\infty }^{\infty }v(\tau +kP)\right]} _{\triangleq \ v_{_{P}}(\tau )}\ d\tau \end{aligned}}$ |

The corresponding convolution theorem is**:**

${\mathcal {F}}\{u_{_{P}}*v\}[k]=\ P\cdot U[k]\ V[k].$    (Eq.2)

| Derivation of Eq.2 |
|---|
| ${\begin{aligned}{\mathcal {F}}\{u_{_{P}}*v\}[k]&\triangleq {\frac {1}{P}}\int _{P}\left(\int _{P}u_{_{P}}(\tau )\cdot v_{_{P}}(x-\tau )\ d\tau \right)e^{-i2\pi kx/P}\,dx\\&=\int _{P}u_{_{P}}(\tau )\left({\frac {1}{P}}\int _{P}v_{_{P}}(x-\tau )\ e^{-i2\pi kx/P}dx\right)\,d\tau \\&=\int _{P}u_{_{P}}(\tau )\ e^{-i2\pi k\tau /P}\underbrace {\left({\frac {1}{P}}\int _{P}v_{_{P}}(x-\tau )\ e^{-i2\pi k(x-\tau )/P}dx\right)} _{V[k],\quad {\text{due to periodicity}}}\,d\tau \\&=\underbrace {\left(\int _{P}\ u_{_{P}}(\tau )\ e^{-i2\pi k\tau /P}d\tau \right)} _{P\cdot U[k]}\ V[k].\end{aligned}}$ |

## Functions of a discrete variable (sequences)

By a derivation similar to Eq.1, there is an analogous theorem for sequences, such as samples of two continuous functions, where now ${\mathcal {F}}$ denotes the **discrete-time Fourier transform** (DTFT) operator. Consider two sequences $u[n]$ and $v[n]$ with transforms U and V :

${\begin{aligned}U(f)&\triangleq {\mathcal {F}}\{u\}(f)=\sum _{n=-\infty }^{\infty }u[n]\cdot e^{-i2\pi fn}\;,\quad f\in \mathbb {R} ,\\V(f)&\triangleq {\mathcal {F}}\{v\}(f)=\sum _{n=-\infty }^{\infty }v[n]\cdot e^{-i2\pi fn}\;,\quad f\in \mathbb {R} .\end{aligned}}$

The § Discrete convolution of u and v is defined by:

$r[n]\triangleq (u*v)[n]=\sum _{m=-\infty }^{\infty }u[m]\cdot v[n-m]=\sum _{m=-\infty }^{\infty }u[n-m]\cdot v[m].$

The **convolution theorem** for discrete sequences is:

$R(f)={\mathcal {F}}\{u*v\}(f)=\ U(f)V(f).$    (Eq.3)

### Periodic convolution

$U(f)$ and $V(f),$ as defined above, are periodic, with a period of 1. Consider N -periodic sequences $u_{_{N}}$ and $v_{_{N}}$ :

$u_{_{N}}[n]\ \triangleq \sum _{m=-\infty }^{\infty }u[n-mN]$ and $v_{_{N}}[n]\ \triangleq \sum _{m=-\infty }^{\infty }v[n-mN],\quad n\in \mathbb {Z} .$

These functions occur as the result of sampling U and V at intervals of $1/N$ and performing an inverse **discrete Fourier transform** (DFT) on N samples (see § Sampling the DTFT). The discrete convolution**:**

$\{u_{_{N}}*v\}[n]\ \triangleq \sum _{m=-\infty }^{\infty }u_{_{N}}[m]\cdot v[n-m]\equiv \sum _{m=0}^{N-1}u_{_{N}}[m]\cdot v_{_{N}}[n-m]$

is also N -periodic, and is called a **periodic convolution**. Redefining the ${\mathcal {F}}$ operator as the N -length DFT, the corresponding theorem is:

${\mathcal {F}}\{u_{_{N}}*v\}[k]=\ \underbrace {{\mathcal {F}}\{u_{_{N}}\}[k]} _{U(k/N)}\cdot \underbrace {{\mathcal {F}}\{v_{_{N}}\}[k]} _{V(k/N)},\quad k\in \mathbb {Z} .$    (Eq.4a)

And therefore:

$\{u_{_{N}}*v\}[n]=\ {\mathcal {F}}^{-1}\{{\mathcal {F}}\{u_{_{N}}\}\cdot {\mathcal {F}}\{v_{_{N}}\}\}.$    (Eq.4b)

Under the right conditions, it is possible for this N -length sequence to contain a distortion-free segment of a $u*v$ convolution. But when the non-zero portion of the $u(n)$ or $v(n)$ sequence is equal or longer than $N,$ some distortion is inevitable. Such is the case when the $V(k/N)$ sequence is obtained by directly sampling the DTFT of the infinitely long § Discrete Hilbert transform impulse response.

For u and v sequences whose non-zero duration is less than or equal to $N,$ a final simplification is:

Circular convolution

$\{u_{_{N}}*v\}[n]=\ {\mathcal {F}}^{-1}\{{\mathcal {F}}\{u\}\cdot {\mathcal {F}}\{v\}\}.$    (Eq.4c)

This form is often used to efficiently implement numerical convolution by computer. (see § Fast convolution algorithms and § Example)

As a partial reciprocal, it has been shown that any linear transform that turns convolution into a product is the DFT (up to a permutation of coefficients).

| Derivations of Eq.4 |
|---|
| A time-domain derivation proceeds as follows: ${\begin{aligned}\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}*v\}[k]&\triangleq \sum _{n=0}^{N-1}\left(\sum _{m=0}^{N-1}u_{_{N}}[m]\cdot v_{_{N}}[n-m]\right)e^{-i2\pi kn/N}\\&=\sum _{m=0}^{N-1}u_{_{N}}[m]\left(\sum _{n=0}^{N-1}v_{_{N}}[n-m]\cdot e^{-i2\pi kn/N}\right)\\&=\sum _{m=0}^{N-1}u_{_{N}}[m]\cdot e^{-i2\pi km/N}\underbrace {\left(\sum _{n=0}^{N-1}v_{_{N}}[n-m]\cdot e^{-i2\pi k(n-m)/N}\right)} _{\scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\quad \scriptstyle {\text{due to periodicity}}}\\&=\underbrace {\left(\sum _{m=0}^{N-1}u_{_{N}}[m]\cdot e^{-i2\pi km/N}\right)} _{\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]}\left(\scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\right).\end{aligned}}$ A frequency-domain derivation follows from § Periodic data, which indicates that the DTFTs can be written as: ${\mathcal {F}}\{u_{_{N}}*v\}(f)={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}*v\}[k]\right)\cdot \delta \left(f-k/N\right).\quad \scriptstyle {\mathsf {(Eq.5a)}}$ ${\mathcal {F}}\{u_{_{N}}\}(f)={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\right)\cdot \delta \left(f-k/N\right).$ The product with $V(f)$ is thereby reduced to a discrete-frequency function: ${\begin{aligned}{\mathcal {F}}\{u_{_{N}}*v\}(f)&=G_{_{N}}(f)V(f)\\&={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\right)\cdot V(f)\cdot \delta \left(f-k/N\right)\\&={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\right)\cdot V(k/N)\cdot \delta \left(f-k/N\right)\\&={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\right)\cdot \left(\scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\right)\cdot \delta \left(f-k/N\right),\quad \scriptstyle {\mathsf {(Eq.5b)}}\end{aligned}}$ where the equivalence of $V(k/N)$ and $\left(\scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\right)$ follows from § Sampling the DTFT. Therefore, the equivalence of (5a) and (5b) requires: $\scriptstyle {\rm {DFT}}\displaystyle {\{u_{_{N}}*v\}[k]}=\left(\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\right)\cdot \left(\scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\right).$ We can also verify the inverse DTFT of (5b): ${\begin{aligned}(u_{_{N}}*v)[n]&=\int _{0}^{1}\left({\frac {1}{N}}\sum _{k=-\infty }^{\infty }\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\cdot \scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\cdot \delta \left(f-k/N\right)\right)\cdot e^{i2\pi fn}df\\&={\frac {1}{N}}\sum _{k=-\infty }^{\infty }\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\cdot \scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]\cdot \underbrace {\left(\int _{0}^{1}\delta \left(f-k/N\right)\cdot e^{i2\pi fn}df\right)} _{{\text{0, for}}\ k\ \notin \ [0,\ N)}\\&={\frac {1}{N}}\sum _{k=0}^{N-1}{\bigg (}\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}[k]\cdot \scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}[k]{\bigg )}\cdot e^{i2\pi {\frac {n}{N}}k}\\&=\ \scriptstyle {\rm {DFT}}^{-1}\displaystyle {\bigg (}\scriptstyle {\rm {DFT}}\displaystyle \{u_{_{N}}\}\cdot \scriptstyle {\rm {DFT}}\displaystyle \{v_{_{N}}\}{\bigg )}.\end{aligned}}$ |

## Convolution theorem for inverse Fourier transform

There is also a convolution theorem for the inverse Fourier transform:

Here, " $\cdot$ " represents the Hadamard product, and " * " represents a convolution between the two matrices.

${\begin{aligned}&{\mathcal {F}}\{u*v\}={\mathcal {F}}\{u\}\cdot {\mathcal {F}}\{v\}\\&{\mathcal {F}}\{u\cdot v\}={\mathcal {F}}\{u\}*{\mathcal {F}}\{v\}\end{aligned}}$

so that

${\begin{aligned}&u*v={\mathcal {F}}^{-1}\left\{{\mathcal {F}}\{u\}\cdot {\mathcal {F}}\{v\}\right\}\\&u\cdot v={\mathcal {F}}^{-1}\left\{{\mathcal {F}}\{u\}*{\mathcal {F}}\{v\}\right\}\end{aligned}}$

## Convolution theorem for tempered distributions

The convolution theorem extends to tempered distributions. Here, v is an arbitrary tempered distribution:

${\begin{aligned}&{\mathcal {F}}\{u*v\}={\mathcal {F}}\{u\}\cdot {\mathcal {F}}\{v\}\\&{\mathcal {F}}\{u\cdot v\}={\mathcal {F}}\{u\}*{\mathcal {F}}\{v\}.\end{aligned}}$

But $\alpha =F\{u\}$ must be "rapidly decreasing" towards $-\infty$ and $+\infty$ in order to guarantee the existence of both, convolution and multiplication product. Equivalently, if $u=F^{-1}\{\alpha \}$ is a smooth "slowly growing" ordinary function, it guarantees the existence of both, multiplication and convolution product.

In particular, every compactly supported tempered distribution, such as the Dirac delta, is "rapidly decreasing". Equivalently, bandlimited functions, such as the function that is constantly 1 are smooth "slowly growing" ordinary functions. If, for example, $v\equiv \operatorname {\text{Ш}}$ is the Dirac comb both equations yield the Poisson summation formula and if, furthermore, $u\equiv \delta$ is the Dirac delta then $\alpha \equiv 1$ is constantly one and these equations yield the Dirac comb identity.
