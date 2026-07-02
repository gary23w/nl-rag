---
title: "Probability density function"
source: https://en.wikipedia.org/wiki/Probability_density_function
domain: ridgeline-plots
license: CC-BY-SA-4.0
tags: ridgeline plot, joyplot, overlapping density, stacked distributions
fetched: 2026-07-02
---

# Probability density function

In probability theory, a **probability density function** (**PDF**), **density function**, or simply **density** of an absolutely continuous random variable, is a function whose value at any given point in the sample space (the set of possible values taken by the random variable) can be interpreted as providing a "relative probability" that the value of the random variable would be equal to that point. Probability density is the probability per unit length, in other words. The (absolute) probability for a continuous random variable to take on any particular value is zero. Therefore, the value of the PDF at two different samples can be used to infer, in any particular draw of the random variable, how much more likely it is that the random variable would be close to one point compared to the other.

More precisely, the PDF is used to specify the probability of the random variable falling *within a particular range of values*, as opposed to taking on any one value. This probability is given by the integral of a continuous variable's PDF over that range, where the integral is the nonnegative area under the density function between the lowest and greatest values of the range. The PDF is nonnegative everywhere, and the area under the entire curve is equal to one, such that the probability of the random variable falling within the set of possible values is 100%.

The terms *probability distribution function* and *probability function* can also denote the probability density function. However, this use is not standard among probabilists and statisticians. In other sources, "probability distribution function" may be used when the probability distribution is defined as a function over general sets of values or it may refer to the cumulative distribution function (CDF), or it may be a probability mass function (PMF) rather than the density. *Density function* itself is also used for the probability mass function, leading to further confusion. In general the PMF is used in the context of discrete random variables (random variables that take values on a countable set), while the PDF is used in the context of continuous random variables. Both PMF and PDF are fundamental concepts in statistical inference.

## Example

Suppose bacteria of a certain species typically live 20 to 30 hours. The probability that a bacterium lives *exactly* 5 hours is equal to zero. A lot of bacteria live for approximately 5 hours, but there is no chance that any given bacterium dies at exactly 5.00... hours. However, the probability that the bacterium dies between 5 hours and 5.01 hours is quantifiable. Suppose the answer is 0.02 (i.e., 2%). Then, the probability that the bacterium dies between 5 hours and 5.001 hours should be about 0.002, since this time interval is one-tenth as long as the previous. The probability that the bacterium dies between 5 hours and 5.0001 hours should be about 0.0002, and so on.

In this example, the ratio (probability of dying during an interval) / (duration of the interval) is approximately constant, and equal to 2 per hour (or 2 hour−1). For example, there is 0.02 probability of dying in the 0.01-hour interval between 5 and 5.01 hours, and (0.02 probability / 0.01 hours) = 2 hour−1. This quantity 2 hour−1 is called the probability density for dying at around 5 hours. Therefore, the probability that the bacterium dies at 5 hours can be written as (2 hour−1) *dt*. This is the probability that the bacterium dies within an infinitesimal window of time around 5 hours, where *dt* is the duration of this window. For example, the probability that it lives longer than 5 hours, but shorter than (5 hours + 1 nanosecond), is (2 hour−1)×(1 nanosecond) ≈ 6×10−13 (using the unit conversion 3.6×1012 nanoseconds = 1 hour).

There is a probability density function *f* with *f*(5 hours) = 2 hour−1. The integral of *f* over any window of time (not only infinitesimal windows but also large windows) is the probability that the bacterium dies in that window.

## Absolutely continuous univariate distributions

A probability density function is most commonly associated with absolutely continuous univariate distributions. A random variable X has density $f_{X}$ , where $f_{X}$ is a non-negative Lebesgue-integrable function, if: $\Pr[a\leq X\leq b]=\int _{a}^{b}f_{X}(x)\,dx.$

Hence, if $F_{X}$ is the cumulative distribution function of X , then: $F_{X}(x)=\int _{-\infty }^{x}f_{X}(u)\,du,$ and (if $F_{X}$ is differentiable at x ) $f_{X}(x)={\frac {d}{dx}}F_{X}(x).$

Intuitively, one can think of $f_{X}(x)\,dx$ as being the probability of X falling within the infinitesimal interval $[x,x+dx]$ .

## Formal definition

(*This definition may be extended to any probability distribution using the measure-theoretic definition of probability.*)

A random variable X with values in a measurable space $({\mathcal {X}},{\mathcal {A}})$ (usually $\mathbb {R} ^{n}$ with the Borel sets as measurable subsets) has as probability distribution the pushforward measure *X*∗*P* on $({\mathcal {X}},{\mathcal {A}})$ : the **density** of X with respect to a reference measure $\mu$ on $({\mathcal {X}},{\mathcal {A}})$ is the Radon–Nikodym derivative: $f={\frac {dX_{*}P}{d\mu }}.$

That is, *f* is any measurable function with the property that: $\Pr[X\in A]=\int _{X^{-1}A}\,dP=\int _{A}f\,d\mu$ for any measurable set $A\in {\mathcal {A}}.$

### Discussion

In the continuous univariate case above, the reference measure is the Lebesgue measure. The probability mass function of a discrete random variable is the density with respect to the counting measure over the sample space (usually the set of integers, or some subset thereof).

It is not possible to define a density with reference to an arbitrary measure (e.g. one can not choose the counting measure as a reference for a continuous random variable). Furthermore, when it does exist, the density is almost unique, meaning that any two such densities coincide almost everywhere.

## Further details

Unlike a probability, a probability density function can take on values greater than one; for example, the continuous uniform distribution on the interval [0, 1/2] has probability density *f*(*x*) = 2 for 0 ≤ *x* ≤ 1/2 and *f*(*x*) = 0 elsewhere.

The standard normal distribution has probability density $f(x)={\frac {1}{\sqrt {2\pi }}}\,e^{-x^{2}/2}.$

If a random variable *X* is given and its distribution admits a probability density function *f*, then the expected value of *X* (if the expected value exists) can be calculated as $\operatorname {E} [X]=\int _{-\infty }^{\infty }x\,f(x)\,dx.$

Not every probability distribution has a density function: the distributions of discrete random variables do not; nor does the Cantor distribution, even though it has no discrete component, i.e., does not assign positive probability to any individual point.

A distribution has a density function if its cumulative distribution function *F*(*x*) is absolutely continuous. In this case: *F* is almost everywhere differentiable, and its derivative can be used as probability density: ${\frac {d}{dx}}F(x)=f(x).$

If a probability distribution admits a density, then the probability of every one-point set {*a*} is zero; the same holds for finite and countable sets.

Two probability densities *f* and *g* represent the same probability distribution precisely if they differ only on a set of Lebesgue measure zero.

In the field of statistical physics, a non-formal reformulation of the relation above between the derivative of the cumulative distribution function and the probability density function is generally used as the definition of the probability density function. This alternate definition is the following:

If *dt* is an infinitely small number, the probability that *X* is included within the interval (*t*, *t* + *dt*) is equal to *f*(*t*) *dt*, or: $\Pr(t<X<t+dt)=f(t)\,dt.$

## Link between discrete and continuous distributions

It is possible to represent certain discrete random variables as well as random variables involving both a continuous and a discrete part with a generalized probability density function using the Dirac delta function. (This is not possible with a probability density function in the sense defined above, it may be done with a distribution.) For example, consider a binary discrete random variable having the Rademacher distribution—that is, taking −1 or 1 for values, with probability 1⁄2 each. The density of probability associated with this variable is: $f(t)={\frac {1}{2}}(\delta (t+1)+\delta (t-1)).$

More generally, if a discrete variable can take n different values among real numbers, then the associated probability density function is: $f(t)=\sum _{i=1}^{n}p_{i}\,\delta (t-x_{i}),$ where $x_{1},\ldots ,x_{n}$ are the discrete values accessible to the variable and $p_{1},\ldots ,p_{n}$ are the probabilities associated with these values.

This substantially unifies the treatment of discrete and continuous probability distributions. The above expression allows for determining statistical characteristics of such a discrete variable (such as the mean, variance, and kurtosis), starting from the formulas given for a continuous distribution of the probability.

## Families of densities

It is common for probability density functions (and probability mass functions) to be parametrized—that is, to be characterized by unspecified parameters. For example, the normal distribution is parametrized in terms of the mean and the variance, denoted by $\mu$ and $\sigma ^{2}$ respectively, giving the family of densities $f(x;\mu ,\sigma ^{2})={\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}.$ Different values of the parameters describe different distributions of different random variables on the same sample space (the same set of all possible values of the variable); this sample space is the domain of the family of random variables that this family of distributions describes. A given set of parameters describes a single distribution within the family sharing the functional form of the density. From the perspective of a given distribution, the parameters are constants, and terms in a density function that contain only parameters, but not variables, are part of the normalization factor of a distribution (the multiplicative factor that ensures that the area under the density—the probability of *something* in the domain occurring— equals 1). This normalization factor is outside the kernel of the distribution.

Since the parameters are constants, reparametrizing a density in terms of different parameters to give a characterization of a different random variable in the family, means simply substituting the new parameter values into the formula in place of the old ones.

## Densities associated with multiple variables

For continuous random variables *X*1, ..., *Xn*, it is also possible to define a probability density function associated to the set as a whole, often called **joint probability density function**. This density function is defined as a function of the n variables, such that, for any domain D in the n-dimensional space of the values of the variables *X*1, ..., *Xn*, the probability that a realisation of the set variables falls inside the domain D is $\Pr \left(X_{1},\ldots ,X_{n}\in D\right)=\int _{D}f_{X_{1},\ldots ,X_{n}}(x_{1},\ldots ,x_{n})\,dx_{1}\cdots dx_{n}.$

If *F*(*x*1, ..., *x**n*) = Pr(*X*1 ≤ *x*1, ..., *X**n* ≤ *x**n*) is the cumulative distribution function of the vector (*X*1, ..., *X**n*), then the joint probability density function can be computed as a partial derivative $f(x)=\left.{\frac {\partial ^{n}F}{\partial x_{1}\cdots \partial x_{n}}}\right|_{x}$

### Marginal densities

For *i* = 1, 2, ..., *n*, let *f**X**i*(*x**i*) be the probability density function associated with variable *Xi* alone. This is called the marginal density function, and can be deduced from the probability density associated with the random variables *X*1, ..., *Xn* by integrating over all values of the other *n* − 1 variables: $f_{X_{i}}(x_{i})=\int f(x_{1},\ldots ,x_{n})\,dx_{1}\cdots dx_{i-1}\,dx_{i+1}\cdots dx_{n}.$

### Independence

Continuous random variables *X*1, ..., *Xn* admitting a joint density are all independent from each other if $f_{X_{1},\ldots ,X_{n}}(x_{1},\ldots ,x_{n})=f_{X_{1}}(x_{1})\cdots f_{X_{n}}(x_{n}).$

### Corollary

If the joint probability density function of a vector of n random variables can be factored into a product of n functions of one variable $f_{X_{1},\ldots ,X_{n}}(x_{1},\ldots ,x_{n})=f_{1}(x_{1})\cdots f_{n}(x_{n}),$ (where each *fi* is not necessarily a density) then the n variables in the set are all independent from each other, and the marginal probability density function of each of them is given by $f_{X_{i}}(x_{i})={\frac {f_{i}(x_{i})}{\int f_{i}(x)\,dx}}.$

### Example

This elementary example illustrates the above definition of multidimensional probability density functions in the simple case of a function of a set of two variables. Let us call ${\vec {R}}$ a 2-dimensional random vector of coordinates (*X*, *Y*): the probability to obtain ${\vec {R}}$ in the quarter plane of positive *x* and *y* is $\Pr \left(X>0,Y>0\right)=\int _{0}^{\infty }\int _{0}^{\infty }f_{X,Y}(x,y)\,dx\,dy.$

## Function of random variables and change of variables in the probability density function

If the probability density function of a random variable (or vector) *X* is given as *fX*(*x*), it is possible (but often not necessary; see below) to calculate the probability density function of some variable *Y* = *g*(*X*). This is also called a "change of variable" and is in practice used to generate a random variable of arbitrary shape *f**g*(*X*) = *fY* using a known (for instance, uniform) random number generator.

It is tempting to think that in order to find the expected value E(*g*(*X*)), one must first find the probability density *f**g*(*X*) of the new random variable *Y* = *g*(*X*). However, rather than computing $\operatorname {E} {\big (}g(X){\big )}=\int _{-\infty }^{\infty }yf_{g(X)}(y)\,dy,$ one may find instead $\operatorname {E} {\big (}g(X){\big )}=\int _{-\infty }^{\infty }g(x)f_{X}(x)\,dx.$

The values of the two integrals are the same in all cases in which both *X* and *g*(*X*) actually have probability density functions. It is not necessary that *g* be a one-to-one function. In some cases the latter integral is computed much more easily than the former. See Law of the unconscious statistician.

### Scalar to scalar

Let $g:\mathbb {R} \to \mathbb {R}$ be a monotonic function, then the resulting density function is $f_{Y}(y)=f_{X}{\big (}g^{-1}(y){\big )}\left|{\frac {d}{dy}}{\big (}g^{-1}(y){\big )}\right|.$

Here *g*−1 denotes the inverse function.

This follows from the fact that the probability contained in a differential area must be invariant under change of variables. That is, $\left|f_{Y}(y)\,dy\right|=\left|f_{X}(x)\,dx\right|,$ or $f_{Y}(y)=\left|{\frac {dx}{dy}}\right|f_{X}(x)=\left|{\frac {d}{dy}}(x)\right|f_{X}(x)=\left|{\frac {d}{dy}}{\big (}g^{-1}(y){\big )}\right|f_{X}{\big (}g^{-1}(y){\big )}={\left|\left(g^{-1}\right)'(y)\right|}\cdot f_{X}{\big (}g^{-1}(y){\big )}.$

For functions that are not monotonic, the probability density function for y is $\sum _{k=1}^{n(y)}\left|{\frac {d}{dy}}g_{k}^{-1}(y)\right|\cdot f_{X}{\big (}g_{k}^{-1}(y){\big )},$ where *n*(*y*) is the number of solutions in x for the equation $g(x)=y$ , and $g_{k}^{-1}(y)$ are these solutions.

### Vector to vector

Suppose **x** is an n-dimensional random variable with joint density *f*. If ***y*** = *G*(***x***), where *G* is a bijective, differentiable function, then ***y*** has density *p****Y***: $p_{Y}(\mathbf {y} )=f{\Bigl (}G^{-1}(\mathbf {y} ){\Bigr )}\left|\det \left[\left.{\frac {dG^{-1}(\mathbf {z} )}{d\mathbf {z} }}\right|_{\mathbf {z} =\mathbf {y} }\right]\right|$ with the differential regarded as the Jacobian of the inverse of *G*(⋅), evaluated at ***y***.

For example, in the 2-dimensional case **x** = (*x*1, *x*2), suppose the transform *G* is given as *y*1 = *G*1(*x*1, *x*2), *y*2 = *G*2(*x*1, *x*2) with inverses *x*1 = *G*1−1(*y*1, *y*2), *x*2 = *G*2−1(*y*1, *y*2). The joint distribution for **y** = (*y*1, y2) has density $p_{Y_{1},Y_{2}}(y_{1},y_{2})=f_{X_{1},X_{2}}{\big (}G_{1}^{-1}(y_{1},y_{2}),G_{2}^{-1}(y_{1},y_{2}){\big )}\left\vert {\frac {\partial G_{1}^{-1}}{\partial y_{1}}}{\frac {\partial G_{2}^{-1}}{\partial y_{2}}}-{\frac {\partial G_{1}^{-1}}{\partial y_{2}}}{\frac {\partial G_{2}^{-1}}{\partial y_{1}}}\right\vert .$

### Vector to scalar

Let $V:\mathbb {R} ^{n}\to \mathbb {R}$ be a differentiable function and X be a random vector taking values in $\mathbb {R} ^{n}$ , $f_{X}$ be the probability density function of X and $\delta (\cdot )$ be the Dirac delta function. It is possible to use the formulas above to determine $f_{Y}$ , the probability density function of $Y=V(X)$ , which will be given by $f_{Y}(y)=\int _{\mathbb {R} ^{n}}f_{X}(\mathbf {x} )\delta {\big (}y-V(\mathbf {x} ){\big )}\,d\mathbf {x} .$

This result leads to the law of the unconscious statistician: ${\begin{aligned}\operatorname {E} _{Y}[Y]&=\int _{\mathbb {R} }yf_{Y}(y)\,dy\\&=\int _{\mathbb {R} }y\int _{\mathbb {R} ^{n}}f_{X}(\mathbf {x} )\delta {\big (}y-V(\mathbf {x} ){\big )}\,d\mathbf {x} \,dy\\&=\int _{{\mathbb {R} }^{n}}\int _{\mathbb {R} }yf_{X}(\mathbf {x} )\delta {\big (}y-V(\mathbf {x} ){\big )}\,dy\,d\mathbf {x} \\&=\int _{\mathbb {R} ^{n}}V(\mathbf {x} )f_{X}(\mathbf {x} )\,d\mathbf {x} =\operatorname {E} _{X}[V(X)].\end{aligned}}$

*Proof:*

Let Z be a collapsed random variable with probability density function $p_{Z}(z)=\delta (z)$ (i.e., a constant equal to zero). Let the random vector ${\tilde {X}}$ and the transform H be defined as $H(Z,X)={\begin{bmatrix}Z+V(X)\\X\end{bmatrix}}={\begin{bmatrix}Y\\{\tilde {X}}\end{bmatrix}}.$

It is clear that H is a bijective mapping, and the Jacobian of $H^{-1}$ is given by: ${\frac {dH^{-1}(y,{\tilde {\mathbf {x} }})}{dy\,d{\tilde {\mathbf {x} }}}}={\begin{bmatrix}1&-{\frac {dV({\tilde {\mathbf {x} }})}{d{\tilde {\mathbf {x} }}}}\\\mathbf {0} _{n\times 1}&\mathbf {I} _{n\times n}\end{bmatrix}},$ which is an upper triangular matrix with ones on the main diagonal, therefore its determinant is 1. Applying the change of variable theorem from the previous section we obtain that $f_{Y,X}(y,x)=f_{X}(\mathbf {x} )\delta {\big (}y-V(\mathbf {x} ){\big )},$ which if marginalized over x leads to the desired probability density function.

## Sums of independent random variables

The probability density function of the sum of two independent random variables *U* and *V*, each of which has a probability density function, is the convolution of their separate density functions: $f_{U+V}(x)=\int _{-\infty }^{\infty }f_{U}(y)f_{V}(x-y)\,dy=\left(f_{U}*f_{V}\right)(x)$

It is possible to generalize the previous relation to a sum of N independent random variables, with densities *U*1, ..., *UN*: $f_{U_{1}+\cdots +U}(x)=\left(f_{U_{1}}*\cdots *f_{U_{N}}\right)(x)$

This can be derived from a two-way change of variables involving *Y* = *U* + *V* and *Z* = *V*, similarly to the example below for the quotient of independent random variables.

## Products and quotients of independent random variables

Given two independent random variables *U* and *V*, each of which has a probability density function, the density of the product *Y* = *UV* and quotient *Y* = *U*/*V* can be computed by a change of variables.

### Example: Quotient distribution

To compute the quotient *Y* = *U*/*V* of two independent random variables *U* and *V*, define the following transformation: ${\begin{aligned}Y&=U/V\\[1ex]Z&=V\end{aligned}}$

Then, the joint density *p*(*y*,*z*) can be computed by a change of variables from *U*,*V* to *Y*,*Z*, and *Y* can be derived by marginalizing out *Z* from the joint density.

The inverse transformation is ${\begin{aligned}U&=YZ\\V&=Z\end{aligned}}$

The absolute value of the Jacobian matrix determinant $J(U,V\mid Y,Z)$ of this transformation is: $\left|\det {\begin{bmatrix}{\frac {\partial u}{\partial y}}&{\frac {\partial u}{\partial z}}\\{\frac {\partial v}{\partial y}}&{\frac {\partial v}{\partial z}}\end{bmatrix}}\right|=\left|\det {\begin{bmatrix}z&y\\0&1\end{bmatrix}}\right|=|z|.$

Thus: $p(y,z)=p(u,v)\,J(u,v\mid y,z)=p(u)\,p(v)\,J(u,v\mid y,z)=p_{U}(yz)\,p_{V}(z)\,|z|.$

And the distribution of *Y* can be computed by marginalizing out *Z*: $p(y)=\int _{-\infty }^{\infty }p_{U}(yz)\,p_{V}(z)\,|z|\,dz$

This method crucially requires that the transformation from *U*,*V* to *Y*,*Z* be bijective. The above transformation meets this because *Z* can be mapped directly back to *V*, and for a given *V* the quotient *U*/*V* is monotonic. This is similarly the case for the sum *U* + *V*, difference *U* − *V* and product *UV*.

Exactly the same method can be used to compute the distribution of other functions of multiple independent random variables.

### Example: Quotient of two standard normals

Given two standard normal variables *U* and *V*, the quotient can be computed as follows. First, the variables have the following density functions: ${\begin{aligned}p(u)&={\frac {1}{\sqrt {2\pi }}}e^{-{u^{2}}/{2}}\\[1ex]p(v)&={\frac {1}{\sqrt {2\pi }}}e^{-{v^{2}}/{2}}\end{aligned}}$

We transform as described above: ${\begin{aligned}Y&=U/V\\[1ex]Z&=V\end{aligned}}$

This leads to: ${\begin{aligned}p(y)&=\int _{-\infty }^{\infty }p_{U}(yz)\,p_{V}(z)\,|z|\,dz\\[5pt]&=\int _{-\infty }^{\infty }{\frac {1}{\sqrt {2\pi }}}e^{-{\frac {1}{2}}y^{2}z^{2}}{\frac {1}{\sqrt {2\pi }}}e^{-{\frac {1}{2}}z^{2}}|z|\,dz\\[5pt]&=\int _{-\infty }^{\infty }{\frac {1}{2\pi }}e^{-{\frac {1}{2}}\left(y^{2}+1\right)z^{2}}|z|\,dz\\[5pt]&=2\int _{0}^{\infty }{\frac {1}{2\pi }}e^{-{\frac {1}{2}}\left(y^{2}+1\right)z^{2}}z\,dz\\[5pt]&=\int _{0}^{\infty }{\frac {1}{\pi }}e^{-\left(y^{2}+1\right)u}\,du&&u={\tfrac {1}{2}}z^{2}\\[5pt]&=\left.-{\frac {1}{\pi \left(y^{2}+1\right)}}e^{-\left(y^{2}+1\right)u}\right|_{u=0}^{\infty }\\[5pt]&={\frac {1}{\pi \left(y^{2}+1\right)}}\end{aligned}}$

This is the density of a standard Cauchy distribution.
