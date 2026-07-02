---
title: "Chebyshev filter (part 2/2)"
source: https://en.wikipedia.org/wiki/Chebyshev_filter
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
part: 2/2
---

## Advanced Topics in Chebyshev Filters

Chebyshev filter design flexibility may be augmented by more advanced design methods documented in this section. Transmission zeros may be inserted into the stop band to neutralize specific undesired frequencies or increase the cut-off attenuation, or may be inserted off-axis to obtain a more desirable group delay. Asymmetric Chebyshev band pass filters may be created that contain differing number of poles on each side of the pass band to meet frequency asymmetric design requirements more efficiently. The equi-ripple pass bands and that Chebyshev filters are known for may be restricted to a percentage of the pass band to meet design requirements more efficiently that only call for a portion of the pass band to be equi-ripple.

### Chebyshev transmission zeros

Chebyshev filters may be designed with arbitrarily placed finite transmission zeros in the stop band while retaining an equi-ripple pass band. Stop band zeros along the $j\omega$ axis are generally used to eliminate unwanted frequencies. Stop band zeros along the real axis or quadruplet stop band zeros in the complex plane may be used to modify the group delay to a more desirable shape. The transmission zeros design utilizes characteristic polynomials, K(S), to place the transmission and reflection zeros, which in turn are used to create the transfer function, $G(s)$ ,

$G(s)={\sqrt {\frac {1}{1+\varepsilon ^{2}K(s)K(-s)}}}{\bigg |}_{\text{left half plane (LHP) poles}}$

The calculation of K(S) relies upon the following observed equality.

${\begin{aligned}&{\begin{array}{lcr}&{\bigg |}\prod _{i=1}^{N}{\frac {j\omega {\frac {\sqrt {z_{i}^{2}+1}}{z_{i}}}+{\sqrt {1-\omega ^{2}}}}{(1-j\omega /z_{i})}}{\bigg |}=1.&&{\text{ for }}0\leq \omega \leq 1\end{array}}\\\end{aligned}}$

for all $z_{i}=\infty$ , imaginary conjugate pairs, quadruplet conjugate pairs, or real opposing signed pairs.

Given the magnitude is always one in the pass band ( $0\leq \omega \leq 1$ ) the rational and irrational terms must vary between 0 and 1. Therefore, if only the rational term is used to create the $K(s)$ characteristic function, an equi-ripple response is expected in the pass band, and characteristic poles (transmission zeros) are expected at all $s=z_{i}$ .

The design process for K(S) using the above expression is below.

${\begin{aligned}K(s)&={\frac {{\bigg \{}\prod _{i=1}^{N}{\bigg (}M_{i}s+{\sqrt {s^{2}+1}}{\bigg )}{\bigg \}}_{\text{rational term only}}}{\prod _{i=1}^{N}(1-s/z_{i})}}\\M_{i}&={\frac {\sqrt {z_{i}^{2}+1}}{z_{i}}}{\text{ for }}\sigma _{i}\neq 0{\text{ or }}\omega _{i}>1\\&={\frac {\sqrt {\omega _{i}^{2}-1}}{\omega _{i}}}{\text{ for }}\sigma _{i}=0{\text{ and }}\omega _{i}>1\\&=1{\text{ for }}\omega _{i}=\infty \\z_{i}&=\sigma _{i}+j\omega _{i}={\text{ complex transmission zero}}\\\end{aligned}}$

Use the positive $M_{i}$ solution for real and imaginary $z_{i}$ pairs. Use the positive real and conjugate imaginary $M_{i}$ solution for quadruplet complex $z_{i}$ pairs.

$K(s)$ should be normalized such that $|K(s)|=1{\text{ at }}s=j$ , if needed.

The, "rational terms only" indicates to keep the rational part of the product, and to discard the irrational part. The rational term may be obtained by manually performing the polynomial arithmetic, or with the short cut below which is a solution derived from polynomial arithmetic and uses binomial coefficients. The algorithm is extremely efficient if the Binomial coefficients are implemented from a look-up table of pre-calculated values.

${\begin{aligned}&B=\prod _{i=1}^{N}(M_{i}s+1)\\&K(s)_{num}=\sum _{i=N}^{i\geq 0{\text{, step }}=-2}{\bigg [}\sum _{j=i}^{j\geq 0{\text{, step }}=-2}B_{j}{\binom {(N-j)/2}{(N-i)/2}}{\bigg ]}s^{i}\\&N={\text{ order of the Chebyshev filter}}\\&B={\text{a polynomial created by the product of the specified factors}}\\&B_{j}={\text{ the }}j_{th}{\text{ order coefficient of polynomial }}B\\&{\binom {n}{k}}{\text{ is the binomial coefficient function}}\\\end{aligned}}$

When all M values are set to one, then $K(s)_{num}$ will be the standard Chebyshev equation, which is expected since the all transmission zeros are it $\infty$ . Even order finite transmission zero Chebyshev filters have the same limitation as the all-pole case in that they cannot be constructed using equally terminated passive networks. The same even order modification may be made to the even order characteristic polynomials, $K(s)$ , to make equally terminated passive network implementations possible. However, the even order modification will also move the finite transmission zeros slightly. This movement may be significantly mitigated by propositioning the transmission zeros with the inverse of the even order modification using the lowest Chebyshev node, $cos(\pi (N-1)/(2N))$ .

${\begin{aligned}&z_{i}'={\sqrt {z_{i}^{2}(1.-C_{0}^{2})-C_{0}^{2}}}\\&C_{0}^{2}=cos^{2}({\frac {\pi (N-1)}{2N}})\\&z_{i}={\text{desired finite transmission zero}}\\&z_{i}'={\text{prepositioned finite transmission zero}}\\\end{aligned}}$

#### Simple transmission zeros example

Design a 3 pole Chebyshev filter with a 1 dB pass band, a transmission zero at 2 rad/sec, and a transmission zero at $\infty$ :

${\begin{aligned}&M_{1}=M_{2}={\sqrt {(j2)^{2}+1}}/j2={\sqrt {1-4}}/j2={\sqrt {3}}/2=0.866025{\text{, }}M_{3}={\sqrt {\infty ^{2}+1}}/\infty =1\\&\\&{\text{Full polynomial derivation:}}\\&K(s)_{num}={\bigr (}0.86602540s+{\sqrt {s^{2}+1}}{\bigr )}{\bigr (}0.86602540s+{\sqrt {s^{2}+1}}{\bigr )}{\bigr (}s+{\sqrt {s^{2}+1}}{\bigr )}\\&K(s)_{num}=3.4820508s^{3}+2.7320508s+{\sqrt {\dots }}\\&{\text{discarding the irrational }}{\sqrt {\dots }}{\text{ and keeping only the rational part:}}\\&K(s)_{num}=3.4820508s^{3}+2.7320508s\\&\\&K(s)_{num}{\text{ shortcut derivation:}}\\&B=(0.86602540s+1)(0.86602540s+1)(s+1)=.75s^{3}+2.4820508s^{2}+2.7320508s+1\\&K(s)_{num}={\bigg (}0.75{\binom {0}{0}}+2.4820508{\binom {1}{0}}{\bigg )}s^{3}+{\bigg (}2.7320508{\binom {1}{1}}{\bigg )}s\\&K(s)_{num}=3.4820508s^{3}+2.7320508s\\&\\&k(s)_{den}=({\frac {s}{j2}}+1)({\frac {s}{-j2}}+1)=0.25s^{2}+1\\&{\text{Check }}|K(s)|{\text{ at }}s=j{\text{ to insure it is unity, and adjust with a constant, if necessary:}}\\&{\bigg |}{\frac {K(s)_{num}(s=j)}{K(s)_{den}(s=j)}}{\bigg |}=1{\text{ Check!}}\\&K(s)={\frac {3.4820508s^{3}+2.7320508s}{0.25s^{2}+1}}\\\end{aligned}}$

To find the $G(s)$ transfer function, do the following.

${\begin{aligned}&\varepsilon ^{2}=10^{1dB/10.}-1.=.25892541\\&G(s)={\sqrt {G(s)G(-s)}}{\bigg |}_{\text{LHP poles}}={\sqrt {\frac {1}{1+\varepsilon ^{2}K(s)K(-s)}}}{\bigg |}_{\text{LHP poles}}={\sqrt {\frac {K(s)_{den}K(-s)_{den}}{K(s)_{den}K(-s)_{den}+\varepsilon ^{2}K(s)_{num}K(-s)_{num}}}}{\bigg |}_{\text{LHP poles}}\\&={\sqrt {\frac {\{0.25(s)^{2}+1\}\{{0.25(-s)^{2}+1}\}}{\{0.25(s)^{2}+1\}\{{0.25(-s)^{2}+1}\}+.25892541\{3.4820508(s)^{3}+2.7320508(s)\}\{3.4820508(-s)^{3}+2.7320508(-s)\}}}}{\bigg |}_{\text{LHP poles}}\\&={\frac {0.25(s)^{2}+1}{{\sqrt {-3.1393872s^{6}-4.8638872s^{4}-1.4326456s^{2}+1}}{\bigr |}_{\text{LHP poles}}}}\\\end{aligned}}$

To obtain $G(s)$ from the left half plane, factor the numerator and denominator to obtain the roots. Discard all roots from the right half plane of the denominator, half the repeated roots in the numerator, and rebuild $G(s)$ with the remaining roots. Generally, normalize $|G(s)|$ to 1 at $s=0$ .

${\begin{aligned}&G(s)={\frac {0.25s^{2}+1}{1.7718316s^{3}+1.7200107s^{2}+2.2074118s+1}}\\\end{aligned}}$

To confirm that the example $G(s)$ is correct, the plot of $G(s)$ along $j\omega$ is shown below with a pass band ripple of 1 dB, a cut off frequency of 1 rad/sec, and a stop band zero at 2 rad/sec.

### Asymmetric band pass filter

Chebyshev band pass filters may be designed with a geometrically asymmetric frequency response by placing the desired number of transmission zeros at zero and infinity with the use of the more generalized form of the Chebyshev transmission zeros equation above, and shown below. The $K(s)$ equations below consider a frequency normalized pass band from 1 to $\omega _{2}$ . If the number of transmission zeros at 0 is not the same as the number of transmission zeros at $\infty$ , the filter will be geometrically asymmetric. The filter will also be asymmetric if finite transmission zeros are not place symmetrically about the geometric center frequency, which in this case is ${\sqrt {\omega _{2}}}$ . There is a restriction in that he filter must be net even order, that is the sum of all the poles must be even, to make the asymmetric $K(s)$ equation produce usable results. Real and complex quadruplet transmission zeros may also be created using this technique and are useful to modify the group delay response, just as in the low pass case. The derivation of the characteristic equation, $K(s)$ , to create an asymmetric Chebyshev band pass filter is shown below.

${\begin{aligned}K(s)&={\frac {{\bigg \{}\prod _{i=1}^{N}{\bigg (}M_{i}{\sqrt {s^{2}+\omega _{2}^{2}}}+{\sqrt {s^{2}+1}}{\bigg )}{\bigg \}}_{\text{rational term only}}}{s^{N_{z}}\prod _{i=1}^{N_{f}}(1-s/z_{i})}}\\M_{i}&={\sqrt {\frac {z_{i}^{2}+1}{z_{i}^{2}+\omega _{2}^{2}}}}{\text{ for }}\sigma _{i}\neq 0{\text{ or }}\omega _{i}<1{\text{ or }}\omega _{i}>\omega _{2}\\&={\sqrt {\frac {1-\omega _{i}^{2}}{\omega _{2}^{2}-\omega _{i}^{2}}}}{\text{ for }}\sigma _{i}=0{\text{ and }}0<\omega _{i}<1\\&={\sqrt {\frac {\omega _{i}^{2}-1}{\omega _{i}^{2}-\omega _{2}^{2}}}}{\text{ for }}\sigma _{i}=0{\text{ and }}\omega _{2}<\omega _{i}<\infty \\&={\frac {1}{\omega _{2}}}{\text{ for }}z_{i}=0\\&=1{\text{ for }}z_{i}=\infty \\N_{z}&={\text{ number of transmission zeros at zero}}\\N_{f}&={\text{ number of finite transmission zeros (imaginary, real, and complex)}}\\z_{i}&=\sigma _{i}+j\omega _{i}={\text{ complex transmission zero}}\\\omega _{2}&={\text{ upper passband corner frequency (lower corner is normalized to 1)}}\\\end{aligned}}$

$K(s)$ should be normalized such that $|K(s)|=1{\text{ at }}s=j$ , if needed.

#### Simple asymmetric example

Design an asymmetric Chebyshev filter with 1dB pass band ripple from 1 to 2 rad/sec, one transmission zero at $\infty$ , and three transmission zeros at 0. By applying the numeral values to the equations above, the characteristic polynomials, $K(s)$ , may be calculated as follows.

${\begin{aligned}\omega _{2}&=2\\M_{1}&=M_{2}=M_{3}=.5\\M_{4}&=1\\K(s)&={\frac {{\bigg \{}{\bigg (}.5{\sqrt {s^{2}+2^{2}}}+{\sqrt {s^{2}+1}}{\bigg )}{\bigg (}.5{\sqrt {s^{2}+2^{2}}}+{\sqrt {s^{2}+1}}{\bigg )}{\bigg (}.5{\sqrt {s^{2}+2^{2}}}+{\sqrt {s^{2}+1}}{\bigg )}{\bigg (}{\sqrt {s^{2}+2^{2}}}+{\sqrt {s^{2}+1}}{\bigg )}{\bigg \}}_{\text{rational term only}}}{s^{3}}}\\K(s)&=C{\frac {3.375s^{4}+14.25s^{2}+12+{\sqrt {\dots }}}{s^{3}}}{\text{ where C is a constant used to normalize the magnitude to 1 at }}s=j\\\end{aligned}}$

Discarding the irrational part and normalizing $|K(s)|$ to 1 at s=j:

${\begin{aligned}K(s)&={\frac {3s^{4}+12.666667s^{2}+10.666667}{s^{3}}}\\\end{aligned}}$

Use the same process as in the low pass case to find $G(s)$ from $K(s)$ , using constant C to scale the magnitude.

${\begin{aligned}\varepsilon ^{2}&=10^{1dB/10.}-1.=.25892541\\G(s)&=C{\sqrt {\frac {K(s)_{den}K(-s)_{den}}{K(s)_{den}K(-s)_{den}+\varepsilon ^{2}K(s)_{num}K(-s)_{num}}}}{\bigg |}_{\text{LHP poles}}\\&=C{\frac {s^{3}}{{\sqrt {(s)^{3}(-s)^{3}+.25892541\{3(s)^{4}+12.666667(s)^{2}+10.666667\}\{3(-s)^{4}+12.666667(-s)^{2}+10.666667\}}}{\bigr |}_{\text{LHP poles}}}}\\&=C{\frac {s^{3}}{{\sqrt {2.3303287s^{8}+18.678331s^{6}+58.11437s^{4}+69.9674s^{2}+29.459958}}{\bigr |}_{\text{LHP poles}}}}\\\end{aligned}}$

When reconstructing the denominator from the left half plane poles, it will be necessary to set the $G(s)$ magnitude such that the reflection zeros occur at 0dB. To do this, $G(s)$ should be scaled such that $|G(s)|$ = -1dB at the pass band corner frequencies, $s=j$ and $s=j2$ . Once accomplished, the final transfer function for the designed asymmetric Chebyshev filter is shown below.

${\begin{aligned}G(s)&={\frac {0.18424001s^{3}}{0.28125000s^{4}+0.34089984s^{3}+1.3337548s^{2}+0.54084155s+1}}\\\end{aligned}}$

Evaluating $|G(s)|$ at s=j and at s=2j produces a value of -1dB in both cases, yielding an assurance that the example has been synthesized correctly. The frequency response is below, showing a Chebyshev 1dB equi-ripple pass band response for $1<\omega <2$ , cutoff attenuation of -1dB at the pass band edges, -60dB / decade attenuation toward $\omega =0$ , -20dB / decade attenuation toward $\omega =\infty$ , and Chebyshev style steepened slopes near the pass band edges.

### Constricting the pass band ripple

Standard low pass Chebyshev filter design creates an equi-ripple pass band beginning from 0 rad/sec to a frequency normalized value of 1 rad/sec. However, some design requirements do not need an equi-ripple pass band at the low frequencies. A standard full-equi-ripple Chebyshev filter for this application would result in an over designed filter. Constricting the equi-ripple to a defined percentage of the pass band creates a more efficient design, reducing the size of the filter and potentially eliminating one or two components, which is useful in maximizing board space efficiency and minimizing production costs for mass produced items.

Constricted pass band ripple can be achieved by designing an asymmetric Chebyshev band pass filter using the techniques described above in this article with a 0 order asymmetric high pass side (no transmission zeros at 0) and an $\omega 2$ set to the constricted ripple frequency. The order of the low pass side is N-1 for odd order filters, N-2 for even order modified filters, and N for standard even order filters. This results in a less than unity S12 at $\omega =0$ , which is typical of even order standard Chebyshev design, so for standard even order Chebyshev designs, the process is complete at this step. It will be necessary to insert a single reflection zero at $\omega =0$ for odd order designs, and two reflection zeros at $\omega =0$ for even order modified designs. Added reflection zeros introduces a noticeable error in the pass band that is likely to be objectionable. This error may be removed quickly and accurately by repositioning the finite reflection zeros with the use of Newton's method for systems of equations.

#### Application of Newton's method

Positioning the reflection zeros with Newton's method requires three pieces of information:

1. The location of each pass band ripple minima that exists at frequencies higher than the constricted ripple frequency.
2. The value of the magnitude normalized $|K(j\omega )|$ , that is $|K(j)|=1$ , at the constriction frequency and at each minima above the constriction frequency. Future references to this function will be noted as $|K(j\omega )_{|K(j)|=1}|$ or $|K(s)_{|K(j)|=1}|$
3. The Jacobian matrix of partial derivative of $|K(j\omega )_{|K(j)|=1}|$ for the constriction frequency and at each minima above the constriction frequency. with respect to each reflection zero.

Since the Chebyshev characteristic equations, $K(s)$ , have all reflection zeros located on the $j\omega$ axis, and all the transmission zeros either on the $j\omega$ axis or symmetric bout the $j\omega$ axis (required for passive element implementation), the locations of the pass band ripple minima may be obtained by factoring the numerator of the derivative of $K(s)$ , $(dK(s)/ds)_{num}$ , with the use of a root finding algorithm. The roots of this polynomial will be the pass band minima frequencies. $(dK(s)/ds)_{num}$ is obtainable from standard polynomial derivative definitions, and is $(dK(s)/ds)num=K(s)_{den}(d(K(s)_{num})/ds)-K(s)_{num}(d(K(s)_{den})/ds)$ .

The partial derivatives may be calculated digitally with $\partial |K(R_{k},j\omega )_{K(j)=1}|/\partial R_{k}=|K(R_{k},j\omega )_{|K(j)|=1}|-|K(R_{k}+\vartriangle R_{k},j\omega )_{|K(j)|=1}|)/\vartriangle R_{k}$ , however, the continuous partial derivative generally provides greater accuracy and less convergence time, and is recommended. To obtain the continuous partial derivatives of $|K(s)_{|K(j)|=1}|$ with respect to the reflections zeros, a continuous expression for $K(s)$ needs to be obtained that forces $|K(j)|=1$ at all times. This may be achieved by expressing $K(s)$ as a function of its conjugate root pairs, as shown below.

${\begin{aligned}|K(s)_{|K(j)|=1}|&={\begin{cases}K_{finite}(s)&{\text{if }}n{\text{ is even}}\\sK_{finite}(s)&{\text{if }}n{\text{ is odd}}\\\end{cases}}\\&\\K{finite}(s)&={\frac {\prod _{i=1}^{N_{Rz}}(Rz_{i}^{2}+s^{2})}{\prod _{i=1}^{N_{Tz}}(Tz_{i}^{2}+s^{2})}}{\frac {\prod _{i=1}^{N_{Tz}}(Tz_{i}^{2}-1)}{\prod _{i=1}^{N_{Rz}}(Rz_{i}^{2}-1)}}\\\end{aligned}}$

Where $K{finite}(s)$ includes finite reflection and transmission zeros, only, $N_{Rz}$ and $N_{Tz}$ refer to the number of reflection and transmission zero conjugate pairs, and $Rz_{i}$ and $Tz_{i}$ are the reflection and transmission zero conjugate pairs. The s odd term accounts for the single reflection zero at 0 that occurs in odd order Chebyshev filters. Note that if quadruplet transmission zeros are employed, the expression must be modified to accommodate quadruplet terms. It is seen by inspection that $|K(s)|=1$ whenever $s=j$ in the above expression.

Since only movement of the reflection zeros is needed to shape the Chebyshev pass band, the partial derivative expression only needs to be made on the $Rz_{i}$ terms, and the $Tz_{i}$ terms are treated as a constant. To aid in the determination of the partial derivative expression for each $Rz_{i}$ , the expression above may be rewritten, as shown below.

$|K(j\omega )_{|K(j)|=1}|={\frac {Rz_{k}^{2}-\omega ^{2}}{Rz_{k}^{2}-1}}{\bigg |}K(j\omega ){\bigg |}_{{\text{less the }}Rz_{k}^{2}{\text{ terms}}}$

Where $Rz_{k}^{2}$ designates a specific reflection zero conjugate pair.

This derivative of this expression with respect to $Rz_{k}$ may be easily computed following standard derivative rules. The constant requires the dividing out of the $R_{k}^{2}$ terms to maintain the integrity of the function. The easiest way to do this is to multiply $|K(j\omega )|$ by the inverse of the $R_{k}^{2}$ terms that were moved to the front. The differentiable expression may be rewritten as follows.

$|K(j\omega )_{|K(j)|=1}|={\frac {Rz_{k}^{2}-\omega ^{2}}{Rz_{k}^{2}-1}}{\bigg \{}{\bigg |}K(j\omega ){\bigg |}{\bigg |}{\frac {Rz_{k}^{2}-1}{Rz_{k}^{2}-\omega ^{2}}}{\bigg |}{\bigg \}}_{\text{constant}}$

The partial derivative may then be determined by applying standard derivative procedures to $Rz_{k}$ and then simplifying. The result is below.

${\frac {\partial |K(j\omega )_{|K(j)|=1}|}{\partial |Rz_{k}|}}={\frac {2Rz_{k}^{2}(1-\omega ^{2})}{(1-Rz_{k}^{2})(Rz_{k}^{2}-\omega ^{2})}}|K(j\omega )|$

Since the only frequencies of relevance are the frequencies at the constriction point and the $i=2{\text{ to }}N_{Rz}$ roots of $|(dK(s)/ds)_{num}|$ , the Jacobian matrix may be constructed as follows.

$J(Rz_{k},\omega _{i})={\begin{bmatrix}{\frac {\partial {|K(Rz_{1},j\omega _{1})_{|K(j)|=1}|}}{\partial {Rz_{1}}}}&{\frac {\partial {|K(Rz_{2},j\omega _{1})_{|K(j)|=1}|}}{\partial {Rz_{2}}}}&\dots &{\frac {\partial {|K(Rz_{N_{Rz}},j\omega _{1})_{|K(j)|=1}|}}{\partial {Rz_{N_{Rz}}}}}\\{\frac {\partial {|K(Rz_{1},j\omega _{2})_{|K(j)|=1}|}}{\partial {Rz_{1}}}}&{\frac {\partial {|K(Rz_{2},j\omega _{2})_{|K(j)|=1}|}}{\partial {Rz_{2}}}}&\dots &{\frac {\partial {|K(Rz_{N_{Rz}},j\omega _{2})_{|K(j)|=1}|}}{\partial {Rz_{N_{Rz}}}}}\\\vdots &\vdots &\ddots &\vdots \\{\frac {\partial {|K(Rz_{1},j\omega _{N_{Rz}})_{|K(j)|=1}|)}}{\partial {Rz_{1}}}}&{\frac {\partial {|K(Rz_{2},j\omega _{N_{Rz}})_{|K(j)|=1}|}}{\partial {Rz_{2}}}}&\dots &{\frac {\partial {|K(Rz_{N_{Rz}},j\omega _{N_{Rz}})_{|K(j)|=1}|}}{\partial {Rz_{N_{Rz}}}}}\\\end{bmatrix}}$

Where $\omega _{1}$ is the constriction limit frequency, and $\omega _{(i>1)}$ are the magnitude of the roots of the remaining pass band minima, $|dK(s)/ds)_{num}|$ , and $Rz_{k}$ are the reflection zeros.

Assuming that the filter cut-off attenuation is the same as the ripple magnitude, the value of $|K(j\omega _{i})|$ is 1 at all $\omega _{i}$ , so the solution vector entries are all 1, and the iterative equations to solve for Newton's method is

${\begin{aligned}&[B_{k}]={\begin{bmatrix}|K(j\omega _{1})_{|K(j)|=1}|-1\\|K(j\omega _{2})_{|K(j)|=1}|-1\\\vdots \\|K(j\omega _{N_{Rz}})_{|K(j)|=1}|-1\\\end{bmatrix}}\\&\\&[J(R_{k},\omega _{i})][\Delta _{k}]=[B_{k}]\\&\\&[Rz_{k+1}]=[Rz_{k}]+[\Delta _{k}]\\\end{aligned}}$

Convergence is achieved when the sum of all $\sum _{k=1}^{N_{Rz}}|\Delta _{k}|<\delta$ and $\delta$ is sufficiently small for the application, typically between 1.e-05 and 1.e-16. For larger filters, it may be necessary to restrict the size of each $\Delta _{k}$ to prevent excessive swings early in the convergence, and to restrict the size of each $Rz_{k+1}$ to keep their values inside the constricted ripple range during convergence.

#### Constricted pass band example

Design a 7 pole Chebyshev filter with a 1 dB equi-ripple pass band constricted to 55% of the pass band.

**Step 1:** Design the $K(s)$ characteristic polynomials for an asymmetric frequency response from .45 to 1 with 6 low pass poles at $\infty$ , and 0 high pass poles using the asymmetric synthesis process above (use corner frequency $\omega _{2}$ = 0.45) .

$K(s)={\frac {63.089619s^{6}+113.7979s^{4}+60.897476s^{2}+9.1891952}{1}}$

**Step 2:** Insert a single reflection zero into the $K(s)$ from step 1. (two reflection zero additions would be required for even order modified filters)

$K(s)={\frac {63.089619s^{7}+113.7979s^{5}+60.897476s^{3}+9.1891952s}{1}}$

**Step 3:** Determine $\omega _{(1{\text{ to }}N)}$ from the pass band zero derivative frequencies by computing the positive real or imaginary values of the roots of $|(d{K(s)}/ds)_{num}|$ , and substitute the lowest root with the constriction frequency of 0.45 for $\omega _{1}$ .

|   | $\omega _{1}$ | $\omega _{2}$ | $\omega _{3}$ |
|---|---|---|---|
| 1 | 0.45 | 0.64670785 | 0.89924235 |
| 2 | 0.45 | 0.68010003 | 0.9147864 |
| 3 | 0.45 | 0.6710597 | 0.91089712 |
| 4 | 0.45 | 0.66969972 | 0.91042253 |
| 5 | 0.45 | 0.66967763 | 0.9104163 |
| 6 | 0.45 | 0.66967762 | 0.9104163 |

**Step 4**: Determine the value of $|K(j\omega _{i})|$ at each constricted and derivative zero point.

|   | $\|K(j\omega _{1})\|$ | $\|K(j\omega _{2})\|$ | $\|K(j\omega _{3})\|$ |
|---|---|---|---|
| 1 | 0.45 | 0.64035786 | 0.89703503 |
| 2 | 1.3886545 | 1.1638033 | 1.0148793 |
| 3 | 1.045108 | 1.0133721 | 0.99991225 |
| 4 | 1.0007289 | 1.0001094 | 0.99998768 |
| 5 | 1.0000002 | 1 | 1 |
| 6 | 1 | 1 | 1 |

**Step 5**: Create the **B** vector for the linear equations by subtracting the target values at each $\omega _{k}$ frequency, which in this case are all 1 due to the cutoff attenuation being equal to the pass band ripple attenuation in this specific example. $|K(j)|=1$ at the cut-off frequency of j .

|   | $\|K(j\omega _{1})\|-1$ | $\|K(j\omega _{2})\|-1$ | $\|K(j\omega _{3})\|-1$ |
|---|---|---|---|
| 1 | -0.55 | -0.35964214 | -0.10296497 |
| 2 | 0.38865445 | 0.1638033 | 0.014879269 |
| 3 | 0.045108043 | 0.013372137 | -8.7751135e-05 |
| 4 | 7.2893112e-04 | 1.0943442e-04 | -1.2324941e-05 |
| 5 | 1.7276985e-07 | 5.2176787e-09 | -2.6640391e-09 |
| 6 | 1.8873791e-14 | 1.5765167e-14 | -2.553513e-15 |

**Step 6:** Determine the Jacobian matrix of partial derivative of $|K(j\omega _{i})_{|K(j)|=1}|$ for each $\omega _{(1{\text{ to }}N)}$ with respect to each reflection zero, $Rz_{k}$ , ${\frac {\partial |K(j\omega _{i})_{|K(j)|=1}|}{\partial |Rz_{k}|}}={\frac {2Rz_{k}^{2}(1-\omega _{i}^{2})}{(1-Rz_{k}^{2})(Rz_{k}^{2}-\omega _{i}^{2})}}|K(j\omega _{i})_{K(j)=1}|$

| Iteration 1 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 9.1345241 3.5002523 17.567498 $\omega _{2}$ -0.35964214 -3.1210264 25.682621 $\omega _{3}$ -0.10296497 -0.4223115 45.32731 | Iteration 2 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 18.978308 11.684784 67.247144 $\omega _{2}$ -5.5693485 15.014974 57.94421 $\omega _{3}$ -0.46259286 -4.7583095 63.000455 | Iteration 3 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 15.724251 8.5751083 48.268068 $\omega _{2}$ -4.8309573 12.860042 48.094251 $\omega _{3}$ -0.45645647 -4.3455391 59.167024 |
|---|---|---|
| Iteration 4 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 15.342666 8.1871355 46.007638 $\omega _{2}$ -4.7516921 12.655385 47.240959 $\omega _{3}$ -0.45514037 -4.3046963 58.87818 | Iteration 5 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 15.337079 8.1808716 45.971655 $\omega _{2}$ -4.7506789 12.653283 47.233095 $\omega _{3}$ -0.45510227 -4.3042391 58.875318 | Iteration 6 $Rz_{1}$ $Rz_{2}$ $Rz_{3}$ $\omega _{1}$ 15.337078 8.1808702 45.971647 $\omega _{2}$ -4.7506787 12.653283 47.233094 $\omega _{3}$ -0.45510225 -4.3042391 58.875317 |

**Step 7**: Get the reflection zeros movements by solving for $[\Delta _{k}]$ the linear set of equations $[J(R_{k},\omega _{i})][\Delta _{k}]=[B_{k}]$ using the **B** vector from step 5.

|   | $\Delta _{1}$ | $\Delta _{1}$ | $\Delta _{3}$ | $\sum _{k=1}^{N}\|\Delta _{k}\|$ |
|---|---|---|---|---|
| 1 | -0.033937389 | -0.040973291 | -0.0054977233 | .02680 |
| 2 | 0.010159103 | 0.010436353 | 0.001099011 | .00723149 |
| 3 | 0.0018170271 | 0.001314472 | 1.090765e-04 | .00108019 |
| 4 | 3.4653892E-05 | 1.6843291E-05 | 1.2899974E-06 | 1.75957e-05 |
| 5 | 9.0033707E-09 | 2.9081531E-09 | 2.3695501E-10 | 4.04949e-08 |
| 6 | 0 | 0 | 0 | 0 |

**Step 8:** Compute new reflection zero locations by subtracting the calculated $[\Delta ]$ above from the past iteration of reflection zero positions.

$[Rz_{k}]_{\text{next}}=[Rz_{k}]-[\Delta z_{k}]$

|   | $(Rz_{1})_{\text{next}}$ | $(Rz_{2})_{\text{next}}$ | $(Rz_{3})_{\text{next}}$ |
|---|---|---|---|
| 1 | 0.53982509 | 0.81637641 | 0.97841993 |
| 2 | 0.52966599 | 0.80594006 | 0.97732092 |
| 3 | 0.52784896 | 0.80462559 | 0.97721185 |
| 4 | 0.52781431 | 0.80460874 | 0.97721056 |
| 5 | 0.5278143 | 0.80460874 | 0.97721056 |
| 6 | 0.5278143 | 0.80460874 | 0.97721056 |

Repeat steps 3 through 8 until the application convergence criteria, $\sum _{k=1}^{N_{Rz}}|\Delta _{k}|<\delta _{min}$ , has been met, which for this example is chosen to be 1.e-12. When complete, the final $K(s)$ may be constructed from the final reflection zeros positions, +/-j0.5278143, +/-J0.80460874, +/-J0.97721056, and 0. When amplitude normalized such that $|K(j)|=1$ , the constructed $K(s)$ is shown below.

$K(s)={\frac {87.245248s^{7}+164.10165s^{5}+92.882626s^{3}+15.026225s}{1}}$

$G(s)={\frac {K(s)_{den}}{{\sqrt {K(s)_{den}K(-s)_{den}+\varepsilon ^{2}K(s)_{num}K(-s)_{num}}}|_{\text{LHP roots}}}}$

${\text{Where }}\varepsilon ^{2}=10^{(1dB/10)}-1=0.25892541$

$G(s)={\frac {1}{44.394495s^{7}+30.711417s^{6}+94.125494s^{5}+46.949428s^{4}+58.490258s^{3}+17.844618S^{2}+9.7031614s+1}}$

The synthesis process may be validated by doing a quick check of $|G(j\omega _{k})|$ for each $\omega _{k}$ from step 3 to insure a 1 dB attenuation at those frequencies, and that the cut-off attenuation at $\omega =1$ is also 1dB. The summary of the computation below validates the example synthesis process.

| $\omega _{i}$ | $\|G(j\omega _{k})\|$ |
|---|---|
| $\omega _{1}=0.45$ | -1 dB |
| $\omega _{2}=0.66967762$ | -1 dB |
| $\omega _{3}=0.9104163$ | -1 dB |
| $\omega _{cut}=1$ | -1 dB |

The final magnitude frequency response of the forward transfer function, $|G(jw)|$ , is shown below.

#### Chebyshev II stop band ripple constricting

Standard low pass Inverse Chebyshev filter design creates an equi-ripple stop band beginning from a normalized value of 1 rad/sec to $\infty$ . However, some design requirements do not need an equi-ripple pass band at the high frequencies. A standard full-equi-ripple Inverse Chebyshev filter for this application would result in an over designed filter. Constricting the equi-ripple to a defined percentage of the stop band creates a more efficient design, reducing the size of the filter and potentially eliminating one or two components, which is useful in maximizing board space efficiency and minimizing production costs for mass produced items.

Inverse Chebyshev filters with constricted stop band ripple are synthesized in exactly the same process as standard a inverse Chebyshev. A constricted ripple Chebyshev is designed with an inverted $\varepsilon$ , $\varepsilon ^{2}=1/(10^{(\gamma /10)}-1)$ where $\gamma$ is the stop band attenuation in dB, the poles and zeros of the designed constricted ripple Chebyshev filter are inverted, and the cut-off attenuation is set. Since standard Chebyshev equations will not work with constricted ripple design, the cut-off attenuation must be set using the process described in the Elliptic Hourglass design.

Below are the |S11| and |S12| scattering parameters for a 7 pole constricted ripple Inverse Chebyshev filter with 3dB cut-off attenuation.

#### Non-standard cut-off attenuation and transmission zeros

The constricted ripple example above is intentionally kept simple by keeping the cut-off attenuation equal to the pass band ripple attenuation, omitting optional transmission zeros, and using an odd order that does not potentially require even order modification. However, non-standard cutoff attenuations may be accommodated by calculating the target values in step 5 to be offset from the required 1 that exists at the cut-off frequency of $\omega =j$ , including a $K(s)$ denominator as part of the derivative constant that includes transmission zeros, and inserting two reflection zeros instead of one in to the original $K(s)$ in step 2.

When including stop band transmission zeros, it is import to remember that the roots of $dK(s)/ds)_{num}$ will include stop band maxima with $\omega >1$ . These roots should not be included in the pass band minima used in the computations..

Since $\varepsilon ^{2}$ may be used to set the cut-off attenuation in $G(s)$ , the step 5 $K(s)$ target values may be made with respect to 1. The target values in step 5 may be calculated using the expression for $|K(j\omega )|$ obtainable from the equations above.

${\begin{aligned}&|K(j\omega )|={\sqrt {\frac {10^{Aripple_{dB}/10}-1.}{10^{Acut_{dB}/10}-1.}}}=0.01010101...{\text{ at the pass band minima frequencies}}\\&|K(j\omega )|=1{\text{ at the pass band cut-off frequency}}\\&\varepsilon ^{2}=10^{(Acut_{dB}/10)}-1=99.0\\\end{aligned}}$

Consider a filter design of %constriction = 55, order = 8, single transmission zero at 1.1, pass band ripple attenuation = 0.043648054 (equivalent of S12 = 20dB attenuation based on the relation $|S_{11}|^{2}+|S_{12}|^{2}=1$ for lossless networks), and pass band cut-off attenuation = 20dB.

The target value in step 5 is .01010101, and the $\varepsilon ^{2}$ to compute $G(s)$ is 99. When complete, the characteristic polynomials , $K(s)$ , and forward transfer function, $G(s)$ , are below.

$K(s)={\frac {2.3081085s^{8}+3.7315386s^{6}+1.8867298s^{4}+0.28974597s^{2}}{0.82644628s^{2}+1}}$

$G(s)={\frac {K(s)_{den}}{{\sqrt {K(s)_{den}K(-s)_{den}+\varepsilon ^{2}K(s)_{num}K(-s)_{num}}}|_{\text{LHP roots}}}}$

${\text{Where }}\varepsilon ^{2}=10^{(20_{dB}/10)}-1=99.0$

$G(s)={\frac {0.82644628s^{2}+1}{22.96539s^{8}+39.774072s^{7}+71.570971s^{6}+73.962937s^{5}+65.358572s^{4}+40.848153s^{3}+19.393829S^{2}+6.0938301s+1}}$

The validation consists of calculating scattering parameters $|S12|{\text{ and }}|S11|$ ( $|G(s)|$ and ${\sqrt {1-|G(s)|^{2}}}$ respectively) for the constriction frequency, the cutoff frequency, the remaining pass band minima frequencies in between, and the transmission zero frequency and as shown below.

| $\omega _{i}$ | $\|S12\|=\|G(j\omega _{k})\|$ | $\|S12\|={\sqrt {1-\|G(j\omega _{k})\|^{2}}}$ |
|---|---|---|
| $\omega _{1}=0.45$ | -0.043648054 dB | -20dB |
| $\omega _{2}=0.66133008$ | -0.043648054 dB | -20dB |
| $\omega _{3}=0.82704812$ | -0.043648054 dB | -20dB |
| $\omega _{cut}=1$ | -20 dB | -0.043648054 dB |
| $\omega _{Tz_{1}}=1.1$ | - $\infty$ | 0 dB |

The final magnitude frequency response of $|S_{12}|{\text{ and }}|S_{11}|$ are shown below.
