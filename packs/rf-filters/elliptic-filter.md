---
title: "Elliptic filter"
source: https://en.wikipedia.org/wiki/Elliptic_filter
domain: rf-filters
license: CC-BY-SA-4.0
tags: Butterworth filter, Chebyshev filter, elliptic filter, interdigital filter
fetched: 2026-07-02
---

# Elliptic filter

An **elliptic filter** (also known as a **Cauer filter**, named after Wilhelm Cauer, or as a **Zolotarev filter**, after Yegor Zolotarev) is a signal processing filter with equalized ripple (equiripple) behavior in both the passband and the stopband. The amount of ripple in each band is independently adjustable, and no other filter of equal order can have a faster transition in gain between the passband and the stopband, for the given values of ripple (whether the ripple is equalized or not). Alternatively, one may give up the ability to adjust independently the passband and stopband ripple, and instead design a filter which is maximally insensitive to component variations.

As the ripple in the stopband approaches zero, the filter becomes a type I Chebyshev filter. As the ripple in the passband approaches zero, the filter becomes a type II Chebyshev filter and finally, as both ripple values approach zero, the filter becomes a Butterworth filter.

The gain of a lowpass elliptic filter as a function of angular frequency ω is given by:

$G_{n}(\omega )={1 \over {\sqrt {1+\epsilon ^{2}R_{n}^{2}(\xi ,\omega /\omega _{0})}}}$

where Rn is the *n*th-order elliptic rational function (sometimes known as a Chebyshev rational function) and

$\omega _{0}$

is the

cutoff frequency

$\epsilon$

is the ripple factor

$\xi$

is the selectivity factor

The value of the ripple factor specifies the passband ripple, while the combination of the ripple factor and the selectivity factor specify the stopband ripple.

## Properties

- In the passband, the elliptic rational function varies between zero and unity. The gain of the passband therefore will vary between 1 and $1/{\sqrt {1+\epsilon ^{2}}}$ .
- In the stopband, the elliptic rational function varies between infinity and the discrimination factor $L_{n}$ which is defined as:

$L_{n}=R_{n}(\xi ,\xi )\,$

The gain of the stopband therefore will vary between 0 and

$1/{\sqrt {1+\epsilon ^{2}L_{n}^{2}}}$

.

- In the limit of $\xi \rightarrow \infty$ the elliptic rational function becomes a Chebyshev polynomial, and therefore the filter becomes a Chebyshev type I filter, with ripple factor **ε**
- Since the Butterworth filter is a limiting form of the Chebyshev filter, it follows that in the limit of $\xi \rightarrow \infty$ , $\omega _{0}\rightarrow 0$ and $\epsilon \rightarrow 0$ such that $\epsilon \,R_{n}(\xi ,1/\omega _{0})=1$ the filter becomes a Butterworth filter
- In the limit of $\xi \rightarrow \infty$ , $\epsilon \rightarrow 0$ and $\omega _{0}\rightarrow 0$ such that $\xi \omega _{0}=1$ and $\epsilon L_{n}=\alpha$ , the filter becomes a Chebyshev type II filter with gain

$G(\omega )={\frac {1}{\sqrt {1+{\frac {1}{\alpha ^{2}T_{n}^{2}(1/\omega )}}}}}$

## Poles and zeroes

The zeroes of the gain of an elliptic filter will coincide with the poles of the elliptic rational function, which are derived in the article on elliptic rational functions.

The poles of the gain of an elliptic filter may be derived in a manner very similar to the derivation of the poles of the gain of a type I Chebyshev filter. For simplicity, assume that the cutoff frequency is equal to unity. The poles $(\omega _{pm})$ of the gain of the elliptic filter will be the zeroes of the denominator of the gain. Using the complex frequency $s=\sigma +j\omega$ this means that:

$1+\epsilon ^{2}R_{n}^{2}(-js,\xi )=0\,$

Defining $-js=\mathrm {cd} (w,1/\xi )$ where cd() is the Jacobi elliptic cosine function and using the definition of the elliptic rational functions yields:

$1+\epsilon ^{2}\mathrm {cd} ^{2}\left({\frac {nwK_{n}}{K}},{\frac {1}{L_{n}}}\right)=0\,$

where $K=K(1/\xi )$ and $K_{n}=K(1/L_{n})$ . Solving for *w*

$w={\frac {K}{nK_{n}}}\mathrm {cd} ^{-1}\left({\frac {\pm j}{\epsilon }},{\frac {1}{L_{n}}}\right)+{\frac {mK}{n}}$

where the multiple values of the inverse cd() function are made explicit using the integer index *m*.

The poles of the elliptic gain function are then:

$s_{pm}=i\,\mathrm {cd} (w,1/\xi )\,$

As is the case for the Chebyshev polynomials, this may be expressed in explicitly complex form (Lutovac & et al. 2001, § 12.8)

$s_{pm}={\frac {a+jb}{c}}$

$a=-\zeta _{n}{\sqrt {1-\zeta _{n}^{2}}}{\sqrt {1-x_{m}^{2}}}{\sqrt {1-x_{m}^{2}/\xi ^{2}}}$

$b=x_{m}{\sqrt {1-\zeta _{n}^{2}(1-1/\xi ^{2})}}$

$c=1-\zeta _{n}^{2}+x_{i}^{2}\zeta _{n}^{2}/\xi ^{2}$

where $\zeta _{n}$ is a function of $n,\,\epsilon$ and $\xi$ and $x_{m}$ are the zeroes of the elliptic rational function. $\zeta _{n}$ is expressible for all *n* in terms of Jacobi elliptic functions, or algebraically for some orders, especially orders 1,2, and 3. For orders 1 and 2 we have

$\zeta _{1}={\frac {1}{\sqrt {1+\epsilon ^{2}}}}$

$\zeta _{2}={\frac {2}{(1+t){\sqrt {1+\epsilon ^{2}}}+{\sqrt {(1-t)^{2}+\epsilon ^{2}(1+t)^{2}}}}}$

where

$t={\sqrt {1-1/\xi ^{2}}}$

The algebraic expression for $\zeta _{3}$ is rather involved (See Lutovac & et al. (2001, § 12.8.1)).

The nesting property of the elliptic rational functions can be used to build up higher order expressions for $\zeta _{n}$ :

$\zeta _{m\cdot n}(\xi ,\epsilon )=\zeta _{m}\left(\xi ,{\sqrt {{\frac {1}{\zeta _{n}^{2}(L_{m},\epsilon )}}-1}}\right)$

where $L_{m}=R_{m}(\xi ,\xi )$ .

## Design considerations

See Lutovac & et al. (2001, § 12.11, 13.14).

Elliptic filters are generally specified by requiring a particular value for the passband ripple, αp, stopband ripple, αs, and the sharpness of the cutoff. These specify a minimum order n for the rational elliptic function describing the filter behavior. Specifically, consider a filter passing frequencies below ωp and stopping frequencies above ωs, and define the auxiliary $u={\frac {1}{2}}\cdot {\frac {1-{\sqrt[{4}]{1-\left({\frac {\omega _{p}}{\omega _{s}}}\right)^{2}}}}{1+{\sqrt[{4}]{1-\left({\frac {\omega _{p}}{\omega _{s}}}\right)^{2}}}}}$ To constrain the passband gain into [1-*G*p, 1] and stopband gain into [0, 1-*G*s], the order n must satisfy ${\begin{aligned}&n\geq {\frac {\log {\left(16{\frac {G_{s}}{G_{p}}}\right)}}{-\log(u+2u^{5}+15u^{9}+150u^{13})}}\\&{\text{Where:}}\\&Gs=10^{\alpha _{s/10}}-1\\&Gp=10^{\alpha _{p/10}}-1\\\end{aligned}}$ That equation arises from an approximation to the complete elliptic integral function K; an exact formulation is $n\geq {\frac {K\left({\sqrt {1-\tau _{1}^{2}}}\right)K(\tau _{2})}{K(\tau _{1})K\left({\sqrt {1-\tau _{2}^{2}}}\right)}}$ where ${\begin{aligned}\tau _{1}&={\sqrt {\frac {G_{p}}{G_{s}}}}\\\tau _{2}&={\frac {\omega _{p}}{\omega _{s}}}\end{aligned}}$ Another design consideration is the sensitivity of the gain function to the values of the electronic components used to build the filter. This sensitivity is inversely proportional to the quality factor (Q-factor) of the poles of the filter transfer function. The Q-factor of a pole is defined as:

$Q=-{\frac {|s_{pm}|}{2\mathrm {Re} (s_{pm})}}=-{\frac {1}{2\cos(\arg(s_{pm}))}}$

and is a measure of the influence of the pole on the gain function. For an elliptic filter, it happens that, for a given order, there exists a relationship between the ripple factor and selectivity factor which simultaneously minimizes the Q-factor of all poles in the transfer function:

$\epsilon _{Qmin}={\frac {1}{\sqrt {L_{n}(\xi )}}}$

This results in a filter which is maximally insensitive to component variations, but the ability to independently specify the passband and stopband ripples will be lost. For such filters, as the order increases, the ripple in both bands will decrease and the rate of cutoff will increase. If one decides to use a minimum-Q elliptic filter in order to achieve a particular minimum ripple in the filter bands along with a particular rate of cutoff, the order needed will generally be greater than the order one would otherwise need without the minimum-Q restriction. An image of the absolute value of the gain will look very much like the image in the previous section, except that the poles are arranged in a circle rather than an ellipse. They will not be evenly spaced and there will be zeroes on the ω axis, unlike the Butterworth filter, whose poles are arranged in an evenly spaced circle with no zeroes.

## Comparison with other linear filters

Here is an image showing the elliptic filter next to other common kind of filters obtained with the same number of coefficients:

As is clear from the image, elliptic filters are sharper than all the others, but they show ripples on the whole bandwidth.

## Construction from Chebyshev transmission zeros

Elliptic filter stop bands are essentially Chebyshev filters with transmission zeros where the transmission zeros are arranged in a manner that yields an equi-ripple stop band. Given this, it is possible to convert a Chebyshev filter characteristic equation, $K(s)$ containing the Chebyshev reflection zeros in the numerator and no transmission zeros in the denominator, to an Elliptic filter $K(s)$ containing the Elliptic reflection zeros in the numerator and Elliptic transmission zeros in the denominator, by iteratively creating transmission zeros from the scaled inverse of the Chebyshev reflection zeros, and then reestablishing an equi-ripple Chebyshev pass band from the transmission zeros, and repeating until the iterations produce no further changes of significance to $K(s)$ . The scaling factor used, $\Omega _{c}$ , is the stop band to pass band cutoff frequency ratios and is also known as the inverse of the "selectivity factor". Since Elliptic designs are generally specified from the stop band attenuation requirements, $\Omega _{c}$ , may be derived from the equations that establish the minimum order, n, above.

the $\omega _{s}/\omega _{p}$ ratio, $\Omega _{c}$ may be derived by working the minimum order, *n*, problem above backwards from *n* to find $\Omega _{c}$ .

${\begin{aligned}n&={\text{ number of poles (order of the filter)}}\\\alpha _{p}{\text{ and }}\alpha _{s}&={\text{pass band and stop band attenuation, respectively}}\\\omega _{p}{\text{ and }}\omega _{s}&={\text{pass band and stop band frequencies, respectively}}\\D&={\frac {G_{s}}{G_{p}}}={\frac {10^{\alpha _{s}/10}-1}{10^{\alpha _{p}/10}-1}}\\q&=(16D)^{(-1/n)}\\0&=-q+u+2u^{5}+15u^{9}+150u^{13}\\u&={\text{ real root of above equation}}\\k&={\text{ the selectivity factor }}={\sqrt {1-{\bigg (}{\frac {1-2u}{1+2u}}{\bigg )}^{4}}}\\\Omega _{c}&={\frac {\omega _{s}}{\omega _{p}}}={\frac {1}{k}}={\frac {1}{\sqrt {1-{\bigg (}{\frac {1-2u}{1+2u}}{\bigg )}^{4}}}}\\\end{aligned}}$

The characteristic polynomials, $K(s)$ computed from $\Omega _{c}$ and attenuation requirements, may then be translated to the transfer function polynomials, $G(s)$ with the classic translation, $G(s)={\sqrt {1/(1+\varepsilon ^{2}K(s)K(-s))}}{\bigg |}_{\text{LHP poles}}$ where $\varepsilon ^{2}=10^{Ap/10.}-1.$ and $A_{p}$ is the pass band ripple.

### Simple example

Design an Elliptic filter with a pass band ripple of 1 dB from 0 to 1 rad/sec and a stop band ripple of 40 dB from at least 1.25 rad/sec to $\infty$ .

Applying the calculations above for the value for n prior to applying the ***ceil()*** function, n is found to be 4.83721900 rounded up to the next integer, 5, by applying the ***ceil()*** function, which means a 5 pole Elliptic filter is required to meet the specified design requirements. Applying the calculations above for $\Omega _{c}$ needed to design a stop band of exactly 40 dB of attenuation, $\Omega _{c}$ is found to be 1.2186824.

The polynomial scaled inversion function may be performed by translating each root, ***s***, to $\Omega _{c}/s$ , which may be easily accomplished by inverting the polynomial and scaling it by $\Omega _{c}$ , as shown.

${\begin{aligned}&as^{n}+bs^{n-1}\dots cs^{2}+ds^{1}+es^{0}\Longrightarrow ({\frac {e}{\Omega _{c}^{n}}})s^{n}+({\frac {d}{\Omega _{c}^{n-1}}})s^{n-1}\dots ({\frac {c}{\Omega _{c}^{2}}})s^{2}+({\frac {b}{\Omega _{c}^{1}}})s^{1}+({\frac {a}{\Omega _{c}^{0}}})s^{0}\\\end{aligned}}$

The Elliptic design steps are then as follows:

1. Design a Chebyshev filters with 1 dB pass band ripple.
2. Invert all the reflections zeros about $\Omega _{c}$ to create transmission zeros
3. Create an equi-ripple pass band from the transmission zeros using the process outlined in Chebyshev transmission zeros
4. Repeat steps 2 and 3 until both the pass band and stop band no longer change by any appreciable amount. Typically, 15 to 25 iterations produce coefficient differences in the order of than 1.e-15.

To illustrate the steps, the below K(s) equations begin with a standard Chebyshev K(s), then iterate through the process. Visible differences are seen in the first three iterations. By time 18 iterations have been reached, the differences in K(s) become negligible. Iterations may be discontinued when the change in K(s) coefficients becomes sufficiently small so as to meet design accuracy requirements. The below K(s) iterations have all been normalized such that $|K(j)|=1$ , however, this step may be postponed until the last iteration, if desired.

${\begin{aligned}{\text{iteration 0: }}K(s)&={\frac {16s^{5}+20s^{3}+5s}{1}}\\{\text{iteration 1: }}K(s)&={\frac {9.2965947s^{5}+12.999133s^{3}+4.0025668s}{0.14167325s^{4}+0.84164496s^{2}+1}}\\{\text{iteration 2: }}K(s)&={\frac {8.6496472s^{5}+12.270597s^{3}+3.8746611s}{0.19518773s^{4}+0.94147634s^{2}+1}}\\&\vdots \\{\text{iteration 17: }}K(s)&={\frac {8.550086786383502s^{5}+12.157269873073034s^{3}+3.854163602012615s}{0.2043607336740334s^{4}+0.9573802183509494s^{2}+1}}\\{\text{iteration 18: }}K(s)&={\frac {8.550086786383422s^{5}+12.157269873072942s^{3}+3.854163602012599s}{0.2043607336740334s^{4}+0.9573802183509494s^{2}+1}}\\\end{aligned}}$

To find the $G(s)$ transfer function, do the following.

${\begin{aligned}\varepsilon ^{2}&=10^{1dB/10.}-1.=.25892541\\G(s)&={\sqrt {G(s)G(-s)}}{\bigg |}_{\text{LHP poles}}={\sqrt {\frac {1}{1+\varepsilon ^{2}K(s)K(-s)}}}{\bigg |}_{\text{LHP poles}}={\sqrt {\frac {K(s)_{den}K(-s)_{den}}{K(s)_{den}K(-s)_{den}+\varepsilon ^{2}K(s)_{num}K(-s)_{num}}}}{\bigg |}_{\text{LHP poles}}\\&={\frac {0.20436073s^{4}+0.95738022s^{2}+1}{{\sqrt {-18.928479s^{10}-53.78661s^{8}-54.942632s^{6}-22.939175s^{4}-1.931467+1}}{\bigg |}_{\text{LHP poles}}}}\\\end{aligned}}$

To obtain $G(s)$ from the left half plane, factor the numerator and denominator to obtain the roots using a root finding algorithm. Discard all roots from the right half plane of the denominator, half the repeated roots in the numerator, and rebuild $G(s)$ with the remaining roots. Generally, normalize $|G(s)|$ to 1 at $s=0$ .

${\begin{aligned}&G(s)={\frac {0.20436073s^{4}+0.95738022s^{2}+1}{4.3506872s^{5}+4.0174213s^{4}+8.0362343s^{3}+4.9129149s^{2}+3.4288915s+1}}\\\end{aligned}}$

To confirm that the example $G(s)$ is correct, the plot of $G(s)$ along $j\omega$ is shown below with a pass band ripple of 1 dB, a cut off frequency of 1 rad/sec, a stop band attenuation of 40 dB beginning at 1.21868 rad/sec

## Even order modifications

Even order Elliptic filters implemented with passive elements, typically inductors, capacitors, and transmission lines, with terminations of equal value on each side cannot be implemented with the traditional Elliptic transfer function without the use of coupled coils, which may not be desirable or feasible. This is due to the physical inability to accommodate the even order Chebyshev reflection zeros and transmission zeros that result in the scattering matrix S12 values that exceed the S12 value at $\omega =0$ , and the finite S12 values that exist at $\omega =\infty$ . If it is not feasible to design the filter with one of the terminations increased or decreased to accommodate the pass band S12, then the Elliptic transfer function must be modified so as to move the lowest even order reflection zero to $\omega =0$ and the highest even order transmission zero to $\omega =\infty$ while maintaining the equi-ripple response of the pass band and stop band.

The needed modification involves mapping each pole and zero of the Elliptic transfer function in a manner that maps the lowest frequency reflection zero to zero, the highest frequency transmission zero to $\infty$ , and the remaining poles and zeros as needed to maintain the equi-ripple pass band and stop band. The lowest frequency reflection zero may be found by factoring the $K(s)$ numerator, and the highest frequency transmission zero may be found be factoring the $K(s)$ denominator.

The translate the reflection zeros, the following equation is applied to all poles and zeros of $K(s)$ . While in theory, the translation operations may be performed on either $K(s)$ or $G(s)$ , the reflection zeros must be extracted from $K(s)$ , so it is generally more efficient to perform the translation operations on $K(s)$ .

$R_{i}'={\sqrt {\frac {R_{i}^{2}+\omega _{LO}^{2}}{1-\omega _{LO}^{2}}}}$

Where:

$R_{i}$ is the original Elliptic function zero or pole

$R_{i}'$ is the mapped zero or pole for the modified even order transfer function.

$\omega _{LO}$ is the lowest frequency reflection zero in the pass band.

The sign of imaginary component of $R_{i}'$ is determined by the sign of the original $R_{i}$ .

The translate the transmission zeros, the following equation is applied to all poles and zeros of $K(s)$ . While in theory, the translation operations may be performed on either $K(s)$ or $G(s)$ , if the reflection zeros must be extracted from $K(s)$ , it may be more efficient to perform the translation operations on $K(s)$ .

$R_{i}'={\sqrt {\frac {(\omega _{HI}^{2}-1)R_{i}^{2}}{\omega _{HI}^{2}+R_{i}^{2}}}}$

Where:

$R_{i}$ is the original Elliptic function zero or pole

$R_{i}'$ is the mapped zero or pole for the modified even order transfer function.

$\omega _{HI}$ is the highest frequency transmission zero in the pass band.

The sign of imaginary component of $R_{i}'$ is determined by the sign of the original $R_{i}$ . If operating on $G(s)$ the sign of the real component of $R_{i}'$ must be negative to conform to the left half plane requirement.

It is important to note that all applications require both pass and stop translations. Passive network diplexers, for example, only require even order stop band translations, and perform more efficiently with untranslated even order pass bands.

When $G(s)$ is completed, an equi-ripple transfer function is created with scattering matrix values for S12 of 1 $\omega =0$ and 0 at $\omega =\infty$ , which may be implements with passive equally terminated networks.

The illustration below shows an 8th order Elliptic filter modified to support even order equally terminated passive networks by relocating the lowest frequency reflection zero from a finite frequency to 0 and the highest frequency transmission zero to $\infty$ while maintaining an equi-ripple pass band and stop band frequency response.

The $\Omega _{c}$ and order computation in the Elliptic construction paragraph above are for unmodified Elliptic filters only. Although even order modifications have no effect on the pass band or stop band attenuation, small errors are to be expected in the order and $\Omega _{c}$ computations. Therefore, it is important to apply even order modifications after all $K(s)$ iterations complete if it is desired to preserve the pass and stop band attenuations. If the even order modified Elliptic function is created from an $\Omega _{c}$ requirement, the actual $\Omega _{c}$ will be slightly larger than the design $\Omega _{c}$ . Likewise, an order, ***n***, computation may result in a smaller value than the actual required order.

## Hourglass implementation

An Hourglass filter is a special case of filter where the reflection zeros, are the reciprocal of the transmission zeros about a 3.01 dB normalized cut-off attenuation frequency of 1 rad/sec, resulting all poles of the filter residing on the unit circle. The Elliptic Hourglass implementation has an advantage over an Inverse Chebyshev filter in that the pass band is flatter, and has an advantage over traditional Elliptic filters in that the group delay has a less sharp peak at the cut-off frequency.

### Syntheses process

The most straightforward way to synthesize an Hourglass filter is to design an Elliptic filter with a specified design stop band attenuation, ***As***, and a calculated pass band attenuation that meets the lossless two-port network requirement that scattering parameters $|S_{11}|^{2}+|S_{12}|^{2}=1$ . Together with the well known magnitude dB to arithmetic translation, $(S_{ij})_{dB}=20log_{10}(|S_{ij}|_{arith})$ , algebraic manipulation yields the following pass band attenuation calculated requirement.

$A_{p}=-10\log _{10}{(1.-10^{(-A_{s}/10)})}$

The ***Ap***, defined above will produce reciprocal reflection and transmission zeros about a yet unknown 3.01 dB cut-off frequency. to Design an Elliptic filter with a pass band frequency of 1 rad/sec the 3.01 dB attenuation frequency needs to be determined and that frequency needs to be used to inversely scale the Elliptic design polynomials. The result will be polynomials with an attenuation of 3.01 dB at a normalized frequency of 1 rad/sec. Newton's method or solving the equations directly with a root finding algorithm may be used to determine the 3.01 dB attenuation frequency.

#### Frequency scaling with Newton's method

If $G(s)$ is the Hourglass transfer function to find the 3.01 dB frequency, and $\omega _{c}$ is the 3 dB frequency to find, the steps below may be used to find $\omega _{c}$

1. If $G(s)G(-s)$ is not already available, multiply $G(s)$ by $G(-s)$ to obtain $G(s)G(-s)$ .
2. negate all terms of $s^{n}$ when $(n+2)$ is divisible by 4 . That would be $s^{2}$ , $s^{6}$ , $s^{10}$ , and so on. The modified function will be called $G_{2}(s)G_{2}(-s)$ , and this modification will allow the use of real numbers instead of complex numbers when evaluating the polynomial and its derivative. the real $\omega _{a}$ can now be used in place of the complex $j\omega _{a}$
3. Convert the desired attenuation in dB, $A_{dB}$ , to a squared arithmetic gain value, $B_{arith}^{2}$ , by using $B_{arith}^{2}=10^{A_{dB}/10}$ . For example, 3.010 dB converts to 0.5, 1 dB converts to 0.79432823 and so on.
4. Calculate the modified $|G_{2}(s)G_{2}(-s)|$ in Newton's method using the real value, $\omega _{a}$ . Always take the absolute value.
5. Calculate the derivative the modified $G_{2}(\omega _{a})G_{2}(-\omega _{a})$ with respect to the real value, $\omega _{a}$ . DO NOT take the absolute value of the derivative.

When steps 1) through 4) are complete, the expression involving Newton's method may be written as:

$\omega _{a}=\omega _{a}-([G_{2}(\omega _{a})G_{2}(-\omega _{a})|-B^{2})/(d[G_{2}(\omega _{a})G_{2}(-\omega _{a})]/d\omega _{a})$

using a real value for $\omega _{a}$ with no complex arithmetic needed. The movement of $\omega _{a}$ should be limited to prevent it from going negative early in the iterations for increased reliability. When convergence is complete, $\omega _{a}$ can used for the $\omega _{c}$ that can be used to scale the original $G(s)$ transfer function denominator. The attenuation of the modified $G(s)$ will then be virtually the exact desired value at 1 rad/sec. If performed properly, only a handful of iterations are needed to set the attenuation through a wide range of desired attenuation values for both small and very large order filters.

#### Frequency scaling with root finding

Since $|G(j\omega _{a})|$ does not contain any phase information, directly factoring the transfer function will not produce usable results. However, the transfer function may be modified by multiplying it with $G(-s)$ to eliminate all odd powers of $G(j\omega a)$ , which in turn forces $G(j\omega a)$ to be real at all frequencies, and then finding the frequency that result on the square of the desired attention.

1. If $G(s)G(-s)$ is not already available, multiply $G(s)$ by $G(-s)$ to obtain $G(s)G(-s)$ .
2. Convert the desired attenuation in dB, $A_{dB}$ , to a squared arithmetic gain value, $B_{arith}^{2}$ , by using $B_{arith}^{2}=10^{A_{dB}/10}$ . For example, 3.010 dB converts to 0.5, 1 dB converts to 0.79432823 and so on.
3. Find $P(S)=G_{num}(S)G_{num}(-S)-B_{arith}^{2}G_{den}(S)G_{den}(-S)$
4. Find the roots of P(S) using a root finding algorithm.
5. Of the set of roots from above, select the positive imaginary root for all order filters, and positive real root for even order filters for $\omega _{c}$ .

#### Scaling the transfer function

When $\omega _{c}$ has been determined, the Hourglass transfer function polynomial may be scaled as follows:

${\begin{aligned}G(s)_{\text{orig}}&={\frac {N_{nn}s^{nn}+\dots +N_{2}s^{2}+N_{1}s+N_{0}}{D_{nn}s^{nd}+\dots +D_{2}s^{2}+D_{1}s+D_{0}}}{\text{ (original unscaled transfer function polynomials)}}\\G(s)_{\text{ scaled}}&={\frac {N_{nn}(\omega _{c}s)^{nn}+\dots +N_{2}(\omega _{c}s)^{2}+N_{1}\omega _{c}s+N_{0}}{D_{nn}(\omega _{c}s)^{nd}+\dots +D_{2}(\omega _{c}s)^{2}+D_{1}\omega _{c}s+D_{0}}}{\text{ (}}3.01{\text{ dB at 1 rad/sec scaled transfer function polynomials)}}\\\omega _{c}&=|G(s)|{\text{ 3.01 dB attenuation frequency }}\\nn,nd&={\text{ order of numerator and denominator, respectively}}\\N,D&={\text{ coefficients of numerator and denominator, respectively}}\\\end{aligned}}$

### Even order modifications

Even order Hourglass filters have the same limitations regarding equally terminated passive networks as other Elliptic filters. The same even order modifications that resolve the problem with Elliptic filters also resolve the problem with Hourglass filters.
