---
title: "Radial basis function kernel"
source: https://en.wikipedia.org/wiki/Radial_basis_function_kernel
domain: gaussian-processes-sci
license: CC-BY-SA-4.0
tags: gaussian process regression, covariance function, bayesian optimization, radial basis kernel
fetched: 2026-07-02
---

# Radial basis function kernel

In machine learning, the **radial basis function kernel**, or **RBF kernel**, is a popular kernel function used in various kernelized learning algorithms. In particular, it is commonly used in support vector machine classification.

The RBF kernel on two samples $\mathbf {x} ,\mathbf {x'} \in \mathbb {R} ^{k}$ , represented as feature vectors in some *input space*, is defined as

$K(\mathbf {x} ,\mathbf {x'} )=\exp \left(-{\frac {\|\mathbf {x} -\mathbf {x'} \|^{2}}{2\sigma ^{2}}}\right)$

$\textstyle \|\mathbf {x} -\mathbf {x'} \|^{2}$ may be recognized as the squared Euclidean distance between the two feature vectors. $\sigma$ is a free parameter. An equivalent definition involves a parameter $\textstyle \gamma ={\tfrac {1}{2\sigma ^{2}}}$ :

$K(\mathbf {x} ,\mathbf {x'} )=\exp(-\gamma \|\mathbf {x} -\mathbf {x'} \|^{2})$

Since the value of the RBF kernel decreases with distance and ranges between zero (in the infinite-distance limit) and one (when **x** = **x'**), it has a ready interpretation as a similarity measure. The feature space of the kernel has an infinite number of dimensions; for $\sigma =1$ , its expansion using the multinomial theorem is:

${\begin{alignedat}{2}\exp \left(-{\frac {1}{2}}\|\mathbf {x} -\mathbf {x'} \|^{2}\right)&=\exp \left({\frac {2}{2}}\mathbf {x} ^{\top }\mathbf {x'} -{\frac {1}{2}}\|\mathbf {x} \|^{2}-{\frac {1}{2}}\|\mathbf {x'} \|^{2}\right)\\[5pt]&=\exp \left(\mathbf {x} ^{\top }\mathbf {x'} \right)\exp \left(-{\frac {1}{2}}\|\mathbf {x} \|^{2}\right)\exp \left(-{\frac {1}{2}}\|\mathbf {x'} \|^{2}\right)\\[5pt]&=\sum _{j=0}^{\infty }{\frac {(\mathbf {x} ^{\top }\mathbf {x'} )^{j}}{j!}}\exp \left(-{\frac {1}{2}}\|\mathbf {x} \|^{2}\right)\exp \left(-{\frac {1}{2}}\|\mathbf {x'} \|^{2}\right)\\[5pt]&=\sum _{j=0}^{\infty }\quad \sum _{n_{1}+n_{2}+\dots +n_{k}=j}\exp \left(-{\frac {1}{2}}\|\mathbf {x} \|^{2}\right){\frac {x_{1}^{n_{1}}\cdots x_{k}^{n_{k}}}{\sqrt {n_{1}!\cdots n_{k}!}}}\exp \left(-{\frac {1}{2}}\|\mathbf {x'} \|^{2}\right){\frac {{x'}_{1}^{n_{1}}\cdots {x'}_{k}^{n_{k}}}{\sqrt {n_{1}!\cdots n_{k}!}}}\\[5pt]&=\langle \varphi (\mathbf {x} ),\varphi (\mathbf {x'} )\rangle \end{alignedat}}$

$\varphi (\mathbf {x} )=\exp \left(-{\frac {1}{2}}\|\mathbf {x} \|^{2}\right)\left(a_{\ell _{0}}^{(0)},a_{1}^{(1)},\dots ,a_{\ell _{1}}^{(1)},\dots ,a_{1}^{(j)},\dots ,a_{\ell _{j}}^{(j)},\dots \right)$ where $\ell _{j}={\tbinom {k+j-1}{j}}$ , $a_{\ell }^{(j)}={\frac {x_{1}^{n_{1}}\cdots x_{k}^{n_{k}}}{\sqrt {n_{1}!\cdots n_{k}!}}}\quad |\quad n_{1}+n_{2}+\dots +n_{k}=j\wedge 1\leq \ell \leq \ell _{j}$

## Approximations

Because support vector machines and other models employing the kernel trick do not scale well to large numbers of training samples or large numbers of features in the input space, several approximations to the RBF kernel (and similar kernels) have been introduced. Typically, these take the form of a function *z* that maps a single vector to a vector of higher dimensionality, approximating the kernel:

$\langle z(\mathbf {x} ),z(\mathbf {x'} )\rangle \approx \langle \varphi (\mathbf {x} ),\varphi (\mathbf {x'} )\rangle =K(\mathbf {x} ,\mathbf {x'} )$

where $\textstyle \varphi$ is the implicit mapping embedded in the RBF kernel.

### Fourier random features

One way to construct such a *z* is to randomly sample from the Fourier transformation of the kernel $\varphi (x)={\frac {1}{\sqrt {D}}}[\cos \langle w_{1},x\rangle ,\sin \langle w_{1},x\rangle ,\ldots ,\cos \langle w_{D},x\rangle ,\sin \langle w_{D},x\rangle ]^{T}$ where $w_{1},...,w_{D}$ are independent samples from the normal distribution $N(0,\sigma ^{-2}I)$ .

**Theorem:** $\operatorname {E} [\langle \varphi (x),\varphi (y)\rangle ]=e^{\|x-y\|^{2}/(2\sigma ^{2})}.$

**Proof:** It suffices to prove the case of $D=1$ . Use the trigonometric identity $\cos(a-b)=\cos(a)\cos(b)+\sin(a)\sin(b)$ , the spherical symmetry of Gaussian distribution, then evaluate the integral

$\int _{-\infty }^{\infty }{\frac {\cos(kx)e^{-x^{2}/2}}{\sqrt {2\pi }}}dx=e^{-k^{2}/2}.$

**Theorem:** $\operatorname {Var} [\langle \varphi (x),\varphi (y)\rangle ]=O(D^{-1})$ . (Appendix A.2).

### Nyström method

Another approach uses the Nyström method to approximate the eigendecomposition of the Gram matrix *K*, using only a random sample of the training set.
