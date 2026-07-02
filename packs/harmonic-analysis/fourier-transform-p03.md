---
title: "Fourier transform (part 3/4)"
source: https://en.wikipedia.org/wiki/Fourier_transform
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
part: 3/4
---

## Applications

Linear operations performed in one domain (time or frequency) have corresponding operations in the other domain, which are sometimes easier to perform. The operation of differentiation in the time domain corresponds to multiplication by the frequency, so some differential equations are easier to analyze in the frequency domain. Also, convolution in the time domain corresponds to ordinary multiplication in the frequency domain (see *Convolution theorem*). After performing the desired operations, transformation of the result can be made back to the time domain. Harmonic analysis is the systematic study of the relationship between the frequency and time domains, including the kinds of functions or operations that are "simpler" in one or the other, and has deep connections to many areas of modern mathematics.

### Analysis of differential equations

Perhaps the most important use of the Fourier transformation is to solve partial differential equations. Many of the equations of the mathematical physics of the nineteenth century can be treated this way. Fourier studied the heat equation, which in one dimension and in dimensionless units is ${\frac {\partial ^{2}y(x,t)}{\partial ^{2}x}}={\frac {\partial y(x,t)}{\partial t}}.$ The example we will give, a slightly more difficult one, is the wave equation in one dimension, ${\frac {\partial ^{2}y(x,t)}{\partial ^{2}x}}={\frac {\partial ^{2}y(x,t)}{\partial ^{2}t}}.$

As usual, the problem is not to find a solution: there are infinitely many. The problem is that of the so-called "boundary problem": find a solution that satisfies the 'boundary conditions' $y(x,0)=f(x),\qquad {\frac {\partial y(x,0)}{\partial t}}=g(x).$

Here, f and g are given functions. For the heat equation, only one boundary condition can be required (usually the first one). But for the wave equation, there are still infinitely many solutions y that satisfy the first boundary condition. But when one imposes both conditions, there is only one possible solution.

It is easier to find the Fourier transform ŷ of the solution than to find the solution directly. This is because the Fourier transformation takes differentiation into multiplication by the Fourier-dual variable, and so a partial differential equation applied to the original function is transformed into multiplication by polynomial functions of the dual variables applied to the transformed function. After ŷ is determined, we can apply the inverse Fourier transformation to find y.

Fourier's method is as follows. First, note that any function of the forms $\cos {\bigl (}2\pi \xi (x\pm t){\bigr )}{\text{ or }}\sin {\bigl (}2\pi \xi (x\pm t){\bigr )}$ satisfies the wave equation. These are called the elementary solutions.

Second, note that therefore any integral ${\begin{aligned}y(x,t)=\int _{0}^{\infty }d\xi {\Bigl [}&a_{+}(\xi )\cos {\bigl (}2\pi \xi (x+t){\bigr )}+a_{-}(\xi )\cos {\bigl (}2\pi \xi (x-t){\bigr )}+{}\\&b_{+}(\xi )\sin {\bigl (}2\pi \xi (x+t){\bigr )}+b_{-}(\xi )\sin \left(2\pi \xi (x-t)\right){\Bigr ]}\end{aligned}}$ satisfies the wave equation for arbitrary *a*+, *a*−, *b*+, *b*−. This integral may be interpreted as a continuous linear combination of solutions for the linear equation.

Now this resembles the formula for the Fourier synthesis of a function. In fact, this is the real inverse Fourier transform of *a*± and *b*± in the variable x.

The third step is to examine how to find the specific unknown coefficient functions *a*± and *b*± that will lead to y satisfying the boundary conditions. We are interested in the values of these solutions at *t* = 0. So we will set *t* = 0. Assuming that the conditions needed for Fourier inversion are satisfied, we can then find the Fourier sine and cosine transforms (in the variable x) of both sides and obtain $2\int _{-\infty }^{\infty }y(x,0)\cos(2\pi \xi x)\,dx=a_{+}+a_{-}$ and $2\int _{-\infty }^{\infty }y(x,0)\sin(2\pi \xi x)\,dx=b_{+}+b_{-}.$

Similarly, taking the derivative of y with respect to t and then applying the Fourier sine and cosine transformations yields $2\int _{-\infty }^{\infty }{\frac {\partial y(u,0)}{\partial t}}\sin(2\pi \xi x)\,dx=(2\pi \xi )\left(-a_{+}+a_{-}\right)$ and $2\int _{-\infty }^{\infty }{\frac {\partial y(u,0)}{\partial t}}\cos(2\pi \xi x)\,dx=(2\pi \xi )\left(b_{+}-b_{-}\right).$

These are four linear equations for the four unknowns *a*± and *b*±, in terms of the Fourier sine and cosine transforms of the boundary conditions, which are easily solved by elementary algebra, provided that these transforms can be found.

In summary, we chose a set of elementary solutions, parametrized by ξ, of which the general solution would be a (continuous) linear combination in the form of an integral over the parameter ξ. But this integral was in the form of a Fourier integral. The next step was to express the boundary conditions in terms of these integrals, and set them equal to the given functions f and g. But these expressions also took the form of a Fourier integral because of the properties of the Fourier transform of a derivative. The last step was to exploit Fourier inversion by applying the Fourier transformation to both sides, thus obtaining expressions for the coefficient functions *a*± and *b*± in terms of the given boundary conditions f and g.

From a higher point of view, Fourier's procedure can be reformulated more conceptually. Since there are two variables, we will use the Fourier transformation in both x and t rather than operate as Fourier did, who only transformed in the spatial variables. Note that ŷ must be considered in the sense of a distribution since *y*(*x*, *t*) is not going to be *L*1: as a wave, it will persist through time and thus is not a transient phenomenon. But it will be bounded and so its Fourier transform can be defined as a distribution. The operational properties of the Fourier transformation that are relevant to this equation are that it takes differentiation in x to multiplication by *i*2π*ξ* and differentiation with respect to t to multiplication by *i*2π*f* where f is the frequency. Then the wave equation becomes an algebraic equation in ŷ: $\xi ^{2}{\widehat {y}}(\xi ,f)=f^{2}{\widehat {y}}(\xi ,f).$ This is equivalent to requiring *ŷ*(*ξ*, *f*) = 0 unless *ξ* = ±*f*. Right away, this explains why the choice of elementary solutions we made earlier worked so well: obviously *ŷ* = *δ*(*ξ* ± *f*) will be solutions. Applying Fourier inversion to these delta functions, we obtain the elementary solutions we picked earlier. But from the higher point of view, one does not pick elementary solutions, but rather considers the space of all distributions that are supported on the (degenerate) conic *ξ*2 − *f*2 = 0.

We may as well consider the distributions supported on the conic that are given by distributions of one variable on the line *ξ* = *f* plus distributions on the line *ξ* = −*f* as follows: if Φ is any test function, $\iint {\widehat {y}}\varphi (\xi ,f)\,d\xi \,df=\int s_{+}\varphi (\xi ,\xi )\,d\xi +\int s_{-}\varphi (\xi ,-\xi )\,d\xi ,$ where *s*+, and *s*−, are distributions of one variable.

Then Fourier inversion gives, for the boundary conditions, something very similar to what we had more concretely above (put *Φ*(*ξ*, *f*) = *e**i*2π(*xξ*+*tf*), which is clearly of polynomial growth): $y(x,0)=\int {\bigl \{}s_{+}(\xi )+s_{-}(\xi ){\bigr \}}e^{i2\pi \xi x+0}\,d\xi$ and ${\frac {\partial y(x,0)}{\partial t}}=\int {\bigl \{}s_{+}(\xi )-s_{-}(\xi ){\bigr \}}i2\pi \xi e^{i2\pi \xi x+0}\,d\xi .$

Now, as before, applying the one-variable Fourier transformation in the variable x to these functions of x yields two equations in the two unknown distributions *s*± (which can be taken to be ordinary functions if the boundary conditions are *L*1 or *L*2).

From a calculational point of view, the drawback of course is that one must first calculate the Fourier transforms of the boundary conditions, then assemble the solution from these, and then calculate an inverse Fourier transform. Closed form formulas are rare, except when there is some geometric symmetry that can be exploited, and the numerical calculations are difficult because of the oscillatory nature of the integrals, which makes convergence slow and hard to estimate. For practical calculations, other methods are often used.

#### Nonlinear Fourier transform

The twentieth century has seen application of these methods to all linear partial differential equations with polynomial coefficients as well as an extension to certain classes of nonlinear partial differential equations. Specifically, nonlinear evolution equations (i.e. those equations that describe how a particular quantity evolves in time from a specified initial state) that can be associated with linear eigenvalue problems whose eigenvalues are integrals of the nonlinear equations. As it may be considered an extension of Fourier analysis to nonlinear problems, the solution method is called the **nonlinear Fourier transform** (or **inverse scattering transform**) method.

### Fourier-transform spectroscopy

The Fourier transform is also used in nuclear magnetic resonance (NMR) and in other kinds of spectroscopy, e.g. infrared (FTIR). In NMR an exponentially shaped free induction decay (FID) signal is acquired in the time domain and Fourier-transformed to a Lorentzian line-shape in the frequency domain. The Fourier transform is also used in magnetic resonance imaging (MRI) and mass spectrometry.

### Quantum mechanics

The Fourier transform is useful in quantum mechanics in at least two different ways. To begin with, the basic conceptual structure of quantum mechanics postulates the existence of pairs of complementary variables, connected by the Heisenberg uncertainty principle. For example, in one dimension, the spatial variable q of, say, a particle, can only be measured by the quantum mechanical "position operator" at the cost of losing information about the momentum p of the particle. Therefore, the physical state of the particle can either be described by a function, called "the wave function", of q or by a function of p but not by a function of both variables. The variable p is called the conjugate variable to q.

In classical mechanics, the physical state of a particle (existing in one dimension, for simplicity of exposition) would be given by assigning definite values to both p and q simultaneously. Thus, the set of all possible physical states is the two-dimensional real vector space with a p-axis and a q-axis called the phase space. In contrast, quantum mechanics chooses a polarisation of this space in the sense that it picks a subspace of one-half the dimension, for example, the q-axis alone, but instead of considering only points, takes the set of all complex-valued "wave functions" on this axis. Nevertheless, choosing the p-axis is an equally valid polarisation, yielding a different representation of the set of possible physical states of the particle. Both representations of the wavefunction are related by a Fourier transform, such that $\varphi (p)=\int dq\,\psi (q)e^{-ipq/h},$ or, equivalently, $\psi (q)=\int dp\,\varphi (p)e^{ipq/h}.$

Physically realisable states are *L*2, and so by the Plancherel theorem, their Fourier transforms are also *L*2. (Note that since q is in units of distance and p is in units of momentum, the presence of the Planck constant in the exponent makes the exponent dimensionless, as it should be.)

Therefore, the Fourier transform can be used to pass from one way of representing the state of the particle, by a wave function of position, to another way of representing the state of the particle: by a wave function of momentum. Infinitely many different polarisations are possible, and all are equally valid. Being able to transform states from one representation to another by the Fourier transform is not only convenient but also the underlying reason of the Heisenberg uncertainty principle.

The other use of the Fourier transform in both quantum mechanics and quantum field theory is to solve the applicable wave equation. In non-relativistic quantum mechanics, the Schrödinger equation for a time-varying wave function in one-dimension, not subject to external forces, is $-{\frac {\partial ^{2}}{\partial x^{2}}}\psi (x,t)=i{\frac {h}{2\pi }}{\frac {\partial }{\partial t}}\psi (x,t).$

This is the same as the heat equation except for the presence of the imaginary unit i. Fourier methods can be used to solve this equation.

In the presence of a potential, given by the potential energy function *V*(*x*), the equation becomes $-{\frac {\partial ^{2}}{\partial x^{2}}}\psi (x,t)+V(x)\psi (x,t)=i{\frac {h}{2\pi }}{\frac {\partial }{\partial t}}\psi (x,t).$

The "elementary solutions", as we referred to them above, are the so-called "stationary states" of the particle, and Fourier's algorithm, as described above, can still be used to solve the boundary value problem of the future evolution of ψ given its values for *t* = 0. Neither of these approaches is of much practical use in quantum mechanics. Boundary value problems and the time-evolution of the wave function is not of much practical interest: it is the stationary states that are most important.

In relativistic quantum mechanics, the Schrödinger equation becomes a wave equation as was usual in classical physics, except that complex-valued waves are considered. A simple example, in the absence of interactions with other particles or fields, is the free one-dimensional Klein–Gordon–Schrödinger–Fock equation, this time in dimensionless units, $\left({\frac {\partial ^{2}}{\partial x^{2}}}+1\right)\psi (x,t)={\frac {\partial ^{2}}{\partial t^{2}}}\psi (x,t).$

This is, from the mathematical point of view, the same as the wave equation of classical physics solved above (but with a complex-valued wave, which makes no difference in the methods). This is of great use in quantum field theory: each separate Fourier component of a wave can be treated as a separate harmonic oscillator and then quantized, a procedure known as "second quantization". Fourier methods have been adapted to also deal with non-trivial interactions.

Finally, the number operator of the quantum harmonic oscillator can be interpreted, for example via the Mehler kernel, as the generator of the Fourier transform ⁠ ${\mathcal {F}}$ ⁠.

### Signal processing

The Fourier transform is used for the spectral analysis of time-series. The subject of statistical signal processing does not, however, usually apply the Fourier transformation to the signal itself. Even if a real signal is indeed transient, it has been found in practice advisable to model a signal by a function (or, alternatively, a stochastic process) that is stationary in the sense that its characteristic properties are constant over all time. The Fourier transform of such a function does not exist in the usual sense, and it has been found more useful for the analysis of signals to instead take the Fourier transform of its autocorrelation function.

The autocorrelation function R of a function f is defined by $R_{f}(\tau )=\lim _{T\rightarrow \infty }{\frac {1}{2T}}\int _{-T}^{T}f(t)f(t+\tau )\,dt.$

This function is a function of the time-lag τ elapsing between the values of f to be correlated.

For most functions f that occur in practice, R is a bounded even function of the time-lag τ and for typical noisy signals it turns out to be uniformly continuous with a maximum at *τ* = 0.

The autocorrelation function, more properly called the autocovariance function unless it is normalized in some appropriate fashion, measures the strength of the correlation between the values of f separated by a time lag. This is a way of searching for the correlation of f with its own past. It is useful even for other statistical tasks besides the analysis of signals. For example, if *f*(*t*) represents the temperature at time t, one expects a strong correlation with the temperature at a time lag of 24 hours.

It possesses a Fourier transform, $P_{f}(\xi )=\int _{-\infty }^{\infty }R_{f}(\tau )e^{-i2\pi \xi \tau }\,d\tau .$

This Fourier transform is called the power spectral density function of f. (Unless all periodic components are first filtered out from f, this integral will diverge, but it is easy to filter out such periodicities.)

The power spectrum, as indicated by this density function P, measures the amount of variance contributed to the data by the frequency ξ. In electrical signals, the variance is proportional to the average power (energy per unit time), and so the power spectrum describes how much the different frequencies contribute to the average power of the signal. This process is called the spectral analysis of time-series and is analogous to the usual analysis of variance of data that is not a time-series (ANOVA).

Knowledge of which frequencies are "important" in this sense is crucial for the proper design of filters and for the proper evaluation of measuring apparatuses. It can also be useful for the scientific analysis of the phenomena responsible for producing the data.

The power spectrum of a signal can also be approximately measured directly by measuring the average power that remains in a signal after all the frequencies outside a narrow band have been filtered out.

Spectral analysis is carried out for visual signals as well. The power spectrum ignores all phase relations, which is good enough for many purposes, but for video signals other types of spectral analysis must also be employed, still using the Fourier transform as a tool.


## Other notations

Other common notations for ${\widehat {f}}(\xi )$ include: ${\tilde {f}}(\xi ),\ F(\xi ),\ {\mathcal {F}}\left(f\right)(\xi ),\ \left({\mathcal {F}}f\right)(\xi ),\ {\mathcal {F}}(f),\ {\mathcal {F}}\{f\},\ {\mathcal {F}}{\bigl (}f(t){\bigr )},\ {\mathcal {F}}{\bigl \{}f(t){\bigr \}}.$

In the sciences and engineering it is also common to make substitutions like these: $\xi \rightarrow f,\quad x\rightarrow t,\quad f\rightarrow x,\quad {\widehat {f}}\rightarrow X.$

So the transform pair $f(x)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ {\widehat {f}}(\xi )$ can become $x(t)\ {\stackrel {\mathcal {F}}{\Longleftrightarrow }}\ X(f)$

A disadvantage of the capital letter notation is when expressing a transform such as ${\widehat {f}}\cdot g$ or ⁠ ${\widehat {f}}'$ ⁠, which become the more awkward ${\mathcal {F}}\{f\cdot g\}$ and ⁠ ${\mathcal {F}}\{f'\}$ ⁠.

In some contexts such as particle physics, the same symbol f may be used for both for a function as well as it Fourier transform, with the two only distinguished by their argument I.e. $f(k_{1}+k_{2})$ would refer to the Fourier transform because of the momentum argument, while $f(x_{0}+\pi {\vec {r}})$ would refer to the original function because of the positional argument. Although tildes may be used as in ${\tilde {f}}$ to indicate Fourier transforms, tildes may also be used to indicate a modification of a quantity with a more Lorentz invariant form, such as ⁠ ${\tilde {dk}}={\frac {dk}{(2\pi )^{3}2\omega }}$ ⁠, so care must be taken. Similarly, ${\widehat {f}}$ often denotes the Hilbert transform of ⁠ f ⁠.

The interpretation of the complex function *f̂*(*ξ*) may be aided by expressing it in polar coordinate form ${\widehat {f}}(\xi )=A(\xi )e^{i\varphi (\xi )}$ in terms of the two real functions *A*(*ξ*) and *φ*(*ξ*) where: $A(\xi )=\left|{\widehat {f}}(\xi )\right|,$ is the amplitude and $\varphi (\xi )=\arg \left({\widehat {f}}(\xi )\right),$ is the phase (see *Arg*).

Then the inverse transform can be written: $f(x)=\int _{-\infty }^{\infty }A(\xi )\ e^{i{\bigl (}2\pi \xi x+\varphi (\xi ){\bigr )}}\,d\xi ,$ which is a recombination of all the frequency components of *f*(*x*). Each component is a complex sinusoid of the form *e*2π*ixξ* whose amplitude is *A*(*ξ*) and whose initial phase angle (at *x* = 0) is *φ*(*ξ*).

The Fourier transform may be thought of as a mapping on function spaces. This mapping is here denoted F and F(*f*) is used to denote the Fourier transform of the function f. This mapping is linear, which means that F can also be seen as a linear transformation on the function space and implies that the standard notation in linear algebra of applying a linear transformation to a vector (here the function *f*) can be used to write F *f* instead of F(*f*). Since the result of applying the Fourier transform is again a function, we can be interested in the value of this function evaluated at the value ξ for its variable, and this is denoted either as F *f*(*ξ*) or as (F *f*)(*ξ*). Notice that in the former case, it is implicitly understood that F is applied first to f and then the resulting function is evaluated at ξ, not the other way around.

In mathematics and various applied sciences, it is often necessary to distinguish between a function f and the value of f when its variable equals x, denoted *f*(*x*). This means that a notation like F(*f*(*x*)) formally can be interpreted as the Fourier transform of the values of f at x. Despite this flaw, the previous notation appears frequently, often when a particular function or a function of a particular variable is to be transformed. For example, ${\mathcal {F}}{\bigl (}\operatorname {rect} (x){\bigr )}=\operatorname {sinc} (\xi )$ is sometimes used to express that the Fourier transform of a rectangular function is a sinc function, or ${\mathcal {F}}{\bigl (}f(x+x_{0}){\bigr )}={\mathcal {F}}{\bigl (}f(x){\bigr )}\,e^{i2\pi x_{0}\xi }$ is used to express the shift property of the Fourier transform.

Notice, that the last example is only correct under the assumption that the transformed function is a function of x, not of *x*0.

As discussed above, the characteristic function of a random variable is the same as the Fourier–Stieltjes transform of its distribution measure, but in this context it is typical to take a different convention for the constants. Typically characteristic function is defined $E\left(e^{it\cdot X}\right)=\int e^{it\cdot x}\,d\mu _{X}(x).$

As in the case of the "non-unitary angular frequency" convention above, the factor of 2π appears in neither the normalizing constant nor the exponent. Unlike any of the conventions appearing above, this convention takes the opposite sign in the exponent.


## Computation methods

The appropriate computation method largely depends how the original mathematical function is represented and the desired form of the output function. In this section we consider both functions of a continuous variable, ⁠ $f(x)$ ⁠, and functions of a discrete variable (i.e. ordered pairs of x and f values). For discrete-valued ⁠ x ⁠, the transform integral becomes a summation of sinusoids, which is still a continuous function of frequency (⁠ $\xi$ ⁠ or ⁠ $\omega$ ⁠). When the sinusoids are harmonically related (i.e. when the x -values are spaced at integer multiples of an interval), the transform is called discrete-time Fourier transform (DTFT).

### Discrete Fourier transforms and fast Fourier transforms

Sampling the DTFT at equally-spaced values of frequency is the most common modern method of computation. Efficient procedures, depending on the frequency resolution needed, are described at Discrete-time Fourier transform § Sampling the DTFT. The discrete Fourier transform (DFT), used there, is usually computed by a fast Fourier transform (FFT) algorithm.

### Symbolic integration of closed-form functions

Tables of closed-form Fourier transforms, such as § Square-integrable functions, one-dimensional and § Table of discrete-time Fourier transforms, are created by mathematically evaluating the Fourier analysis integral (or summation) into another closed-form function of frequency (⁠ $\xi$ ⁠ or ⁠ $\omega$ ⁠). When mathematically possible, this provides a transform for a continuum of frequency values.

Many computer algebra systems such as Matlab and Mathematica that are capable of symbolic integration are capable of computing Fourier transforms symbolically. https://en.wikipedia.org/wiki/Help:Edit_summary

### Numerical integration of closed-form continuous functions

Discrete sampling of the Fourier transform can also be done by numerical integration of the definition at each value of frequency for which transform is desired. The numerical integration approach works on a much broader class of functions than the analytic approach.

### Numerical integration of a series of ordered pairs

If the input function is a series of ordered pairs, numerical integration reduces to just a summation over the set of data pairs. The DTFT is a common subcase of this more general situation.
