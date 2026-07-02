---
title: "Normal distribution (part 3/3)"
source: https://en.wikipedia.org/wiki/Normal_distribution
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 3/3
---

## History

### Development

Some authors attribute the discovery of the normal distribution to de Moivre, who in 1738 published in the second edition of his *The Doctrine of Chances* the study of the coefficients in the binomial expansion of (*a* + *b*)*n*. De Moivre proved that the middle term in this expansion has the approximate magnitude of ${\textstyle 2^{n}/{\sqrt {2\pi n}}}$ , and that "If m or ⁠1/2⁠*n* be a Quantity infinitely great, then the Logarithm of the Ratio, which a Term distant from the middle by the Interval ℓ, has to the middle Term, is ${\textstyle -{\frac {2\ell \ell }{n}}}$ ." Although this theorem can be interpreted as the first obscure expression for the normal probability law, Stigler points out that de Moivre himself did not interpret his results as anything more than the approximate rule for the binomial coefficients, and in particular de Moivre lacked the concept of the probability density function.

In 1823 Gauss published his monograph "*Theoria combinationis observationum erroribus minimis obnoxiae*" where among other things he introduces several important statistical concepts, such as the method of least squares, the method of maximum likelihood, and the *normal distribution*. Gauss used M, *M*′, *M*″, ... to denote the measurements of some unknown quantity V, and sought the most probable estimator of that quantity: the one that maximizes the probability *φ*(*M* − *V*) · *φ*(*M*′ − *V*) · *φ*(*M*″ − *V*) · ... of obtaining the observed experimental results. In his notation φΔ is the probability density function of the measurement errors of magnitude Δ. Not knowing what the function φ is, Gauss requires that his method should reduce to the well-known answer: the arithmetic mean of the measured values. Starting from these principles, Gauss demonstrates that the only law that rationalizes the choice of arithmetic mean as an estimator of the location parameter, is the normal law of errors: $\varphi {\mathit {\Delta }}={\frac {h}{\surd \pi }}\,e^{-\mathrm {hh} \Delta \Delta },$ where h is "the measure of the precision of the observations". Using this normal law as a generic model for errors in the experiments, Gauss formulates what is now known as the non-linear weighted least squares method.

Although Gauss was the first to suggest the normal distribution law, Laplace made significant contributions. It was Laplace who first posed the problem of aggregating several observations in 1774, although his own solution led to the Laplacian distribution. It was Laplace who first calculated the value of the integral ∫ *e*−*t*2 *dt* = √π in 1782, providing the normalization constant for the normal distribution. For this accomplishment, Gauss acknowledged the priority of Laplace. Finally, it was Laplace who in 1810 proved and presented to the academy the fundamental central limit theorem, which emphasized the theoretical importance of the normal distribution.

It is of interest to note that in 1809 an Irish-American mathematician Robert Adrain published two insightful but flawed derivations of the normal probability law, simultaneously and independently from Gauss. His works remained largely unnoticed by the scientific community, until in 1871 they were exhumed by Abbe.

In the middle of the 19th century Maxwell demonstrated that the normal distribution is not just a convenient mathematical tool, but may also occur in natural phenomena: The number of particles whose velocity, resolved in a certain direction, lies between x and *x* + *dx* is $\operatorname {N} {\frac {1}{\alpha \;{\sqrt {\pi }}}}\;e^{-{\frac {x^{2}}{\alpha ^{2}}}}\,dx$

### Naming

Today, the concept is usually known in English as the **normal distribution** or **Gaussian distribution**. Other less common names include Gauss distribution, Laplace–Gauss distribution, the law of error, the law of facility of errors, Laplace's second law, and Gaussian law.

Gauss himself apparently coined the term with reference to the "normal equations" involved in its applications, with normal having its technical meaning of orthogonal rather than usual. However, by the end of the 19th century some authors had started using the name *normal distribution*, where the word "normal" was used as an adjective – the term now being seen as a reflection of this distribution being seen as typical, common – and thus normal. Peirce (one of those authors) once defined "normal" thus: "... the 'normal' is not the average (or any other kind of mean) of what actually occurs, but of what *would*, in the long run, occur under certain circumstances." Around the turn of the 20th century Pearson popularized the term *normal* as a designation for this distribution.

> Many years ago I called the Laplace–Gaussian curve the *normal* curve, which name, while it avoids an international question of priority, has the disadvantage of leading people to believe that all other distributions of frequency are in one sense or another 'abnormal'.

— Pearson (1920)

Also, it was Pearson who first wrote the distribution in terms of the standard deviation σ as in modern notation. Soon after this, in year 1915, Fisher added the location parameter to the formula for normal distribution, expressing it in the way it is written nowadays: $df={\frac {1}{\sqrt {2\sigma ^{2}\pi }}}e^{-(x-m)^{2}/(2\sigma ^{2})}\,dx.$

The term *standard normal distribution*, which denotes the normal distribution with zero mean and unit variance came into general use around the 1950s, appearing in the popular textbooks by P. G. Hoel (1947) *Introduction to Mathematical Statistics* and Alexander M. Mood (1950) *Introduction to the Theory of Statistics*.
