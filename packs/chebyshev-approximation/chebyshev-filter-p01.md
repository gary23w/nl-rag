---
title: "Chebyshev filter (part 1/2)"
source: https://en.wikipedia.org/wiki/Chebyshev_filter
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
part: 1/2
---

# Chebyshev filter

**Chebyshev filters** are analog or digital filters that have a steeper roll-off than Butterworth filters, and have either passband ripple (type I) or stopband ripple (type II). Chebyshev filters have the property that they minimize the error between the idealized and the actual filter characteristic over the operating frequency range of the filter, but they achieve this with ripples in the frequency response. This type of filter is named after Pafnuty Chebyshev because its mathematical characteristics are derived from Chebyshev polynomials. Type I Chebyshev filters are usually referred to as "Chebyshev filters", while type II filters are usually called "inverse Chebyshev filters". Because of the passband ripple inherent in Chebyshev filters, filters with a smoother response in the passband but a more irregular response in the stopband are preferred for certain applications.


## Type I Chebyshev filters (Chebyshev filters)

Type I Chebyshev filters are the most common types of Chebyshev filters. The gain (or amplitude) response, $G_{n}(\omega )$ , as a function of angular frequency $\omega$ of the n th-order low-pass filter is equal to the absolute value of the transfer function $H_{n}(s)$ evaluated at $s=j\omega$ :

$G_{n}(\omega )=\left|H_{n}(j\omega )\right|={\frac {1}{\sqrt {1+\varepsilon ^{2}T_{n}^{2}(\omega /\omega _{0})}}}$

where $\varepsilon$ is the ripple factor, $\omega _{0}$ is the cutoff frequency and $T_{n}$ is a Chebyshev polynomial of the n th order.

The passband exhibits equiripple behavior, with the ripple determined by the ripple factor $\varepsilon$ . In the passband, the Chebyshev polynomial alternates between -1 and 1 so the filter gain alternate between maxima at $G=1$ and minima at $G=1/{\sqrt {1+\varepsilon ^{2}}}$ .

The ripple factor ε is thus related to the passband ripple δ in decibels by:

$\varepsilon ={\sqrt {10^{\delta /10}-1}}.$

At the cutoff frequency $\omega _{0}$ the gain again has the value $1/{\sqrt {1+\varepsilon ^{2}}}$ but continues to drop into the stopband as the frequency increases. This behavior is shown in the diagram on the right. The common practice of defining the cutoff frequency at −3 dB is usually not applied to Chebyshev filters; instead the cutoff is taken as the point at which the gain falls to the value of the ripple for the final time.

The 3 dB frequency $\omega _{H}$ is related to $\omega _{0}$ by:

$\omega _{H}=\omega _{0}\cosh \left({\frac {1}{n}}\cosh ^{-1}{\frac {1}{\varepsilon }}\right).$

The order of a Chebyshev filter is equal to the number of reactive components (for example, inductors) needed to realize the filter using analog electronics.

An even steeper roll-off can be obtained if ripple is allowed in the stopband, by allowing zeros on the $\omega$ -axis in the complex plane. While this produces near-infinite suppression at and near these zeros (limited by the quality factor of the components, parasitics, and related factors), overall suppression in the stopband is reduced. The result is called an elliptic filter, also known as a Cauer filter.

### Poles and zeroes

For simplicity, it is assumed that the cutoff frequency is equal to unity. The poles $(\omega _{pm})$ of the gain function of the Chebyshev filter are the zeroes of the denominator of the gain function. Using the complex frequency s , these occur when:

$1+\varepsilon ^{2}T_{n}^{2}(-js)=0.\,$

Defining $-js=\cos(\theta )$ and using the trigonometric definition of the Chebyshev polynomials yields:

$1+\varepsilon ^{2}T_{n}^{2}(\cos(\theta ))=1+\varepsilon ^{2}\cos ^{2}(n\theta )=0.\,$

Solving for $\theta$

$\theta ={\frac {1}{n}}\arccos \left({\frac {\pm j}{\varepsilon }}\right)+{\frac {m\pi }{n}}$

where the multiple values of the arc cosine function are made explicit using the integer index m . The poles of the Chebyshev gain function are then:

$s_{pm}=j\cos(\theta )\,$

$=j\cos \left({\frac {1}{n}}\arccos \left({\frac {\pm j}{\varepsilon }}\right)+{\frac {m\pi }{n}}\right).$

Using the properties of the trigonometric and hyperbolic functions, this may be written in explicitly complex form:

$s_{pm}^{\pm }=\pm \sinh \left({\frac {1}{n}}\mathrm {arsinh} \left({\frac {1}{\varepsilon }}\right)\right)\sin(\theta _{m})$

$+j\cosh \left({\frac {1}{n}}\mathrm {arsinh} \left({\frac {1}{\varepsilon }}\right)\right)\cos(\theta _{m})$

where $m=1,2,...,n$  and

$\theta _{m}={\frac {\pi }{2}}\,{\frac {2m-1}{n}}.$

This may be viewed as an equation parametric in $\theta _{n}$ and it demonstrates that the poles lie on an ellipse in s -space centered at $s=0$ with a real semi-axis of length $\sinh(\mathrm {arsinh} (1/\varepsilon )/n)$ and an imaginary semi-axis of length of $\cosh(\mathrm {arsinh} (1/\varepsilon )/n).$

### The transfer function

The above expression yields the poles of the gain G . For each complex pole, there is another which is the complex conjugate, and for each conjugate pair there are two more that are the negatives of the pair. The transfer function must be stable, so that its poles are those of the gain that have negative real parts and therefore lie in the left half plane of complex frequency space. The transfer function is then given by

$H(s)={\frac {1}{2^{n-1}\varepsilon }}\ \prod _{m=1}^{n}{\frac {1}{(s-s_{pm}^{-})}}$

where $s_{pm}^{-}$ are only those poles of the gain with a negative sign in front of the real term, obtained from the above equation.

### The group delay

The group delay is defined as the derivative of the phase with respect to angular frequency:

$\tau _{g}=-{\frac {d}{d\omega }}\arg(H(j\omega ))$

The gain and the group delay for a 5th-order type I Chebyshev filter with ε=0.5 are plotted in the graph on the left. Its stop band has no ripples. But the ripples of group delay in its passband indicate that different frequency components have different delay, which along with the ripples of gain in its passband results in distortion of the waveform's shape.

### Even order modifications

Even order Chebyshev filters implemented with passive elements, typically inductors, capacitors, and transmission lines, with terminations of equal value on each side cannot be implemented with the traditional Chebyshev transfer function without the use of coupled coils, which may not be desirable or feasible, particularly at the higher frequencies. This is due to the physical inability to accommodate the even order Chebyshev reflection zeros that result in a scattering matrix S12 values that exceed the S12 value at $\omega =0$ . If it is not feasible to design the filter with one of the terminations increased or decreased to accommodate the pass band S12, then the Chebyshev transfer function must be modified so as to move the lowest even order reflection zero to $\omega =0$ while maintaining the equi-ripple response of the pass band.

The needed modification involves mapping each pole of the Chebyshev transfer function in a manner that maps the lowest frequency reflection zero to zero and the remaining poles as needed to maintain the equi-ripple pass band. The lowest frequency reflection zero may be found from the Chebyshev Nodes, $\cos {\Bigl (}{\frac {\pi (n-1)}{2n}}{\Bigl )}$ . The complete Chebyshev pole mapping function is shown below.

$P'=\left[{\sqrt {\left({\frac {P^{2}+cos^{2}{\Bigl (}{\frac {\pi (n-1)}{2n}}{\Bigl )}}{1-{cos^{2}{\Bigl (}{\frac {\pi (n-1)}{2n}}{\Bigl )}}}}\right)}}\right]_{\text{Left Half Plane }}$

Where:

n is the order of the filter (must be even)

P is a traditional Chebyshev transfer function pole

P' is the mapped pole for the modified even order transfer function.

"Left Half Plane" indicates to use the square root containing a negative real value.

When complete, a replacement equi-ripple transfer function is created with reflection zero scattering matrix values for S12 of one and S11 of zero when implemented with equally terminated passive networks. The illustration below shows an 8th order Chebyshev filter modified to support even order equally terminated passive networks by relocating the lowest frequency reflection zero from a finite frequency to 0 while maintaining an equi-ripple pass band frequency response.

The LC element value formulas in the Cauer topology are not applicable to the even order modified Chebyshev transfer function, and cannot be used. It is therefore necessary to calculate the LC values from traditional continued fractions of the impedance function, which may be derived from the reflection coefficient, which in turn may be derived from the transfer function.

### Minimum order

To design a Chebyshev filter using the minimum required number of elements, the minimum order of the Chebyshev filter may be calculated as follows. The equations account for standard low pass Chebyshev filters, only. Even order modifications and finite stop band transmission zeros will introduce error that the equations do not account for.

$n=ceil{\bigg [}{\frac {\cosh ^{-1}{\sqrt {\frac {10^{\alpha _{s}/10}-1}{10^{\alpha _{p}/10}-1}}}}{\cosh ^{-1}{(\omega _{s}/\omega _{p})}}}{\bigg ]}$

where:

$\omega _{p}$ and $\alpha _{p}$ are the pass band ripple frequency and maximum ripple attenuation in dB

$\omega _{s}$ and $\alpha _{s}$ are the stop band frequency and attenuation at that frequency in dB

n is the minimum number of poles, the order of the filter.

*ceil*[] is a round up to next integer function.

### Setting the cutoff attenuation

Pass band cutoff attenuation for Chebyshev filters is usually the same as the pass band ripple attenuation, set by the computation above. However, many applications such as diplexers and triplexers, require a cutoff attenuation of -3.0103 dB in order to obtain the needed reflections. Other specialized applications may require other specific values for cutoff attenuation for various reasons. It is therefore useful to have a means available of setting the Chebyshev pass band cutoff attenuation independently of the pass band ripple attenuation, such as -1 dB, -10 dB, etc. The cutoff attenuation may be set by frequency scaling the poles of the transfer function.

The scaling factor may be determined by direct algebraic manipulation of the defining Chebyshev filter function, $G_{n}(\omega )$ , including $\varepsilon$ and $T_{n}(\omega /\omega _{0})$ . The general definition of the Chebyshev function, $T_{n}(\omega /\omega _{0})=cos(n\cos ^{-1}(\omega /\omega _{0}))$ is required, which may be derived from the Chebyshev Polynomials equations, and the inverse Chebyshev function, $T_{n}^{-1}(\omega /\omega _{0})=cos(\cos ^{-1}(\omega /\omega _{0})/n)$ . To keep the numbers real for values of $\omega /\omega _{0}\geq 1$ , complex hyperbolic identities may be used to rewrite the equations as, $T_{n}(\omega /\omega _{0})=cosh(n\cosh ^{-1}(\omega /\omega _{0}))$ and $T_{n}^{-1}(\omega /\omega _{0})=cosh(\cosh ^{-1}(\omega /\omega _{0})/n)$ .

Using simple algebra on the above equations and references, the expression to scale each Chebyshev poles is:

${\begin{aligned}p_{A}&=p_{1}/T_{n}^{-1}{\Biggr (}{\sqrt {\frac {10^{{\alpha }/10}-1}{10^{\delta /10}-1}}},n{\Biggr )}\qquad &{\text{For }}0<\delta <\infty {\text{ and }}\delta \leq \alpha <\infty \\&=p_{1}*sech{\Biggr (}{\frac {1}{n}}cosh^{-1}{\Bigr (}{\sqrt {\frac {10^{\alpha /10}-1}{10^{\delta /10}-1}}}{\Bigr )}{\Biggr )}&{\text{For }}0<\delta <\infty {\text{ and }}\delta \leq \alpha <\infty \\\end{aligned}}$

Where:

$p_{A}$ is the relocated pole positioned to set the desired cutoff attenuation.

$p_{1}$ is a ripple cutoff pole that lies on the oval.

$\delta$ is the passband attenuation ripple in dB (.05 dB, 1 dB, etc.)).

$\alpha$ is the desired passband attenuation at the cutoff frequency in dB (1 dB, 3 dB, 10 dB, etc.)

n is the number of poles (the order of the filter).

A quick sanity check on the above equation using passband ripple attenuation for the passband cutoff attenuation $(\alpha =\delta )$ reveals that the pole adjustment will be 1.0 for this case, which is what is expected.

### Even order modified cutoff attenuation adjustment

For Chebyshev filters being designed with modified for even order pass band ripple for passive equally terminated filters, the attenuation frequency computation needs to include the even order adjustment by performing the even order adjustment operation on the computed attenuation frequency. This makes the even order adjustment arithmetic slightly simpler, since frequency can be treated as a real variable, in this case $((J\omega )^{2}{\text{ becomes }}-\omega ^{2})$ .

${\begin{aligned}p_{A}=p_{1}{\sqrt {\frac {1-{cos^{2}({\frac {\pi (n-1)}{2n}})}}{cosh^{2}{\Biggr (}{\frac {1}{n}}cosh^{-1}{\Bigr (}{\sqrt {\frac {10^{\alpha /10}-1}{10^{\delta /10}-1}}}{\Bigr )}{\Biggr )}-cos^{2}({\frac {\pi (n-1)}{2n}})}}}{\text{ For }}0<\delta <\infty {\text{ and }}\delta \leq \alpha <\infty \\\end{aligned}}$

Where:

$p_{A}$ is the relocated pole positioned to set the desired cutoff attenuation.

$p_{1}$ is a ripple cutoff pole that has been modified for even order pass bands.

$\delta$ is the passband attenuation ripple in dB (.05 dB, 1 dB, etc.)).

$\alpha$ is the desired passband attenuation at the cutoff frequency in dB (1 dB, 3 dB, 10 dB, etc.)

n is the number of poles (the order of the filter).

$cos({\frac {\pi (n-1)}{2n}})$ is the smallest even order Chebyshev Node


## Type II Chebyshev filters (inverse Chebyshev filters)

Also known as inverse Chebyshev filters, the Type II Chebyshev filter type is less common because it does not roll off as fast as Type I, and requires more components. It has no ripple in the passband, but does have equiripple in the stopband. The gain is:

$G_{n}(\omega )={\frac {1}{\sqrt {1+{\frac {1}{\varepsilon ^{2}T_{n}^{2}(\omega _{0}/\omega )}}}}}={\sqrt {\frac {\varepsilon ^{2}T_{n}^{2}(\omega _{0}/\omega )}{1+\varepsilon ^{2}T_{n}^{2}(\omega _{0}/\omega )}}}.$

In the stopband, the Chebyshev polynomial oscillates between -1 and 1 so that the gain will oscillate between zero and

${\frac {1}{\sqrt {1+{\frac {1}{\varepsilon ^{2}}}}}}$

and the smallest frequency at which this maximum is attained is the cutoff frequency $\omega _{o}$ . The parameter ε is thus related to the stopband attenuation γ in decibels by:

$\varepsilon ={\frac {1}{\sqrt {10^{\gamma /10}-1}}}.$

For a stopband attenuation of 5 dB, ε = 0.6801; for an attenuation of 10 dB, ε = 0.3333. The frequency *f*0 = *ω*0/2*π* is the cutoff frequency. The 3 dB frequency *f*H is related to *f*0 by:

$f_{H}={\frac {f_{0}}{\cosh \left({\frac {1}{n}}\cosh ^{-1}{\frac {1}{\varepsilon }}\right)}}.$

### Poles and zeroes

Assuming that the cutoff frequency is equal to unity, the poles $(\omega _{pm})$ of the gain of the Chebyshev filter are the zeroes of the denominator of the gain:

$1+\varepsilon ^{2}T_{n}^{2}(-1/js_{pm})=0.$

The poles of gain of the type II Chebyshev filter are the inverse of the poles of the type I filter:

${\frac {1}{s_{pm}^{\pm }}}=\pm \sinh \left({\frac {1}{n}}\mathrm {arsinh} \left({\frac {1}{\varepsilon }}\right)\right)\sin(\theta _{m})$

$\qquad +j\cosh \left({\frac {1}{n}}\mathrm {arsinh} \left({\frac {1}{\varepsilon }}\right)\right)\cos(\theta _{m})$

where $m=1,2,...,n$ . The zeroes $(\omega _{zm})$ of the type II Chebyshev filter are the zeroes of the numerator of the gain:

$\varepsilon ^{2}T_{n}^{2}(-1/js_{zm})=0.\,$

The zeroes of the type II Chebyshev filter are therefore the inverse of the zeroes of the Chebyshev polynomial.

$1/s_{zm}=-j\cos \left({\frac {\pi }{2}}\,{\frac {2m-1}{n}}\right)$

for $m=1,2,...,n$ .

### The transfer function

The transfer function is given by the poles in the left half plane of the gain function, and has the same zeroes but these zeroes are single rather than double zeroes.

### The group delay

The gain and the group delay for a fifth-order type II Chebyshev filter with ε=0.1 are plotted in the graph on the left. It can be seen that there are ripples in the gain in the stopband but not in the pass band.

### Even order modifications

Just like Chebyshev filter even order filters, the standard Chebyshev II even order filter cannot be implemented with equally terminated passive elements without the use of coupled coils, which may not be desirable or feasible. In the Chebyshev II case, this is due to finite attenuation of S12 in the stop band. However, even order Chebyshev II filters may be modified by translating the highest frequency finite transmission zero to infinity, while maintaining the equi-ripple functions of the Chebyshev II stop band. To do this translation, an even order modified Chebyshev function is used in place of the standard Chebyshev function to define the Chebyshev II poles needed to create the even order modified Chebyshev II transfer function. Zeros are created using the roots of the even order modified Chebyshev polynomial, which are the even order modified Chebyshev nodes.

The illustration below shows an 8th order Inverse Chebyshev filter modified to support even order equally terminated passive networks by relocating the highest frequency transmission zero from a finite frequency to $\infty$ while maintaining an equi-ripple stop band frequency response.

### Minimum order

To design an Inverse Chebyshev filter using the minimum required number of elements, the minimum order of the Inverse Chebyshev filter may be calculated as follows. The equations account for standard low pass Inverse Chebyshev filters, only. Even order modifications will introduce error that the equations do not account for. The equations is identical to that used for Chebyshev filter minimum order, with a slightly different variable definitions.

$n=ceil{\bigg [}{\frac {\cosh ^{-1}{\sqrt {\frac {10^{\alpha _{s}/10}-1}{10^{\alpha _{p}/10}-1}}}}{\cosh ^{-1}{(\omega _{s}/\omega _{p})}}}{\bigg ]}$

where:

$\omega _{p}$ and $\alpha _{p}$ are the pass band frequency and attenuation at that frequency in dB

$\omega _{s}$ and $\alpha _{s}$ are the stop band frequency and minimum stop band attenuation in dB

n is the minimum number of poles, the order of the filter.

*ceil*[] is a round up to next integer function.

### Setting the cutoff attenuation

The standard cutoff attenuation as described is the same at the pass band ripple attenuation. However, just as in Chebyshev filters, it is useful to set the cutoff attenuation to a desired value, and for the same reasons. Setting the Chebyshev II cutoff attenuation is the same as for Chebyshev cutoff attenuation, except the arithmetic attenuation and ripple entries are inverted in the equation and the poles and zeros are multiplied by the result, as opposed to divided by in the Chebyshev case..

${\begin{aligned}p_{A}&=p_{1}*T_{n}^{-1}{\Biggr (}{\sqrt {\frac {10^{{\delta }/10}-1}{10^{\alpha /10}-1}}},n{\Biggr )}\qquad &{\text{For }}0<\delta <\infty {\text{ and }}0\leq \alpha <\infty \\&=p_{1}*cosh{\Biggr (}{\frac {1}{n}}cosh^{-1}{\Bigr (}{\sqrt {\frac {10^{\delta /10}-1}{10^{\alpha /10}-1}}}{\Bigr )}{\Biggr )}&{\text{For }}0<\delta <\infty {\text{ and }}\delta \leq \alpha <\infty \\\end{aligned}}$

### Even order modified cutoff attenuation adjustment

The same even order adjustment to the poles and zeros that was used for the Chebyshev even order modified cutoff attenuation may also be used for the Chebyshev II case, both the poles and zeros are multiplied by the result.

${\begin{aligned}p_{A}=p_{1}{\sqrt {\frac {cosh^{2}{\Biggr (}{\frac {1}{n}}cosh^{-1}{\Bigr (}{\sqrt {\frac {10^{\delta /10}-1}{10^{\alpha /10}-1}}}{\Bigr )}{\Biggr )}-cos^{2}({\frac {\pi (n-1)}{2n}})}{1-{cos^{2}({\frac {\pi (n-1)}{2n}})}}}}{\text{ For }}0<\delta <\infty {\text{ and }}\delta \leq \alpha <\infty \\\end{aligned}}$


## Implementation

### Cauer topology

A passive LC Chebyshev low-pass filter may be realized using a Cauer topology. The inductor or capacitor values of an n th-order Chebyshev prototype filter may be calculated from the following equations:

$G_{0}=1$

$G_{1}={\frac {2A_{1}}{\gamma }}$

$G_{k}={\frac {4A_{k-1}A_{k}}{B_{k-1}G_{k-1}}},\qquad k=2,3,4,\dots ,n$

$G_{n+1}={\begin{cases}1&{\text{if }}n{\text{ odd}}\\\coth ^{2}\left({\frac {\beta }{4}}\right)&{\text{if }}n{\text{ even}}\end{cases}}$

or

$G_{n+1}={\begin{cases}1&{\text{if }}n{\text{ odd}}\\{\biggr (}\varepsilon +{\sqrt {\varepsilon ^{2}+1}}{\biggr )}^{2}&{\text{if }}n{\text{ even}}\end{cases}}$

G1 to Gk are the capacitor or inductor element values,

G0 is the input termination impedance.

Gn+1 is the output termination impedance when the last element is a shunt capacitor, and the output termination admittance when the last element is a series inductor. Note that for odd order Chebyshev the distinction for the last element is moot.

The 3 dB frequency is calculated with: $f_{H}=f_{0}\cosh \left({\frac {1}{n}}\cosh ^{-1}{\frac {1}{\varepsilon }}\right)$

The coefficients *A*, *γ*, *β*, *A**k*, and *B**k* may be calculated from the following equations:

$\gamma =\sinh \left({\frac {\beta }{2n}}\right)$

$\beta =\ln \left[\coth \left({\frac {\delta }{17.37}}\right)\right]$

$A_{k}=\sin {\frac {(2k-1)\pi }{2n}},\qquad k=1,2,3,\dots ,n$

$B_{k}=\gamma ^{2}+\sin ^{2}\left({\frac {k\pi }{n}}\right),\qquad k=1,2,3,\dots ,n$

where $\delta$ is the passband ripple in decibels. The number $17.37$ is rounded from the exact value $40/\ln(10)$ .

The calculated *G**k* values may then be converted into shunt capacitors and series inductors as shown on the right, or they may be converted into series capacitors and shunt inductors. For example,

- *C*1 shunt = G1, *L*2 series = *G*2, ...

or

- *L*1 series = *G*1, *C*2 shunt = *G*2, ...

Note that when G1 is a shunt capacitor or series inductor, G0 corresponds to the input resistance or conductance, respectively. The same relationship holds for Gn+1 and Gn. The resulting circuit is a normalized low-pass filter. Using frequency transformations and impedance scaling, the normalized low-pass filter may be transformed into high-pass, band-pass, and band-stop filters of any desired cutoff frequency or bandwidth.

### Digital

As with most analog filters, the Chebyshev may be converted to a digital (discrete-time) recursive form via the bilinear transform. However, as digital filters have a finite bandwidth, the response shape of the transformed Chebyshev is warped. Alternatively, the Matched Z-transform method may be used, which does not warp the response.


## Comparison with other linear filters

The following illustration shows the Chebyshev filters next to other common filter types obtained with the same number of coefficients (fifth order):

Chebyshev filters are sharper than the Butterworth filter; they are not as sharp as the elliptic one, but they show fewer ripples over the bandwidth.
