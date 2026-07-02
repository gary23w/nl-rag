---
title: "Power law"
source: https://en.wikipedia.org/wiki/Power_law
domain: complex-systems
license: CC-BY-SA-4.0
tags: complex systems, self-organization, power law, percolation theory
fetched: 2026-07-02
---

# Power law

In statistics, a **power law** is a functional relationship between two quantities, where a relative change in one quantity results in a relative change in the other quantity proportional to the change raised to a constant exponent: one quantity varies as a power of another. The change is independent of the initial size of those quantities.

For instance, the area of a square has a power law relationship with the length of its side, since if the length is doubled, the area is multiplied by 22, while if the length is tripled, the area is multiplied by 32, and so on.

## Empirical examples

The distributions of a wide variety of physical, biological, and human-made phenomena approximately follow a power law over a wide range of magnitudes: these include the sizes of craters on the moon and of solar flares, cloud sizes, the foraging pattern of various species, the sizes of activity patterns of neuronal populations, the frequencies of words in most languages, frequencies of family names, the species richness in clades of organisms, the sizes of power outages, volcanic eruptions, human judgments of stimulus intensity and many other quantities. Empirical distributions can only fit a power law for a limited range of values, because a pure power law would allow for arbitrarily large or small values. Acoustic attenuation follows frequency power-laws within wide frequency bands for many complex media. Allometric scaling laws for relationships between biological variables are among the best known power-law functions in nature.

## Properties

### Statistical incompleteness

The power-law model does not obey the treasured paradigm of statistical completeness. Especially probability bounds, the suspected cause of typical bending and/or flattening phenomena in the high- and low-frequency graphical segments, are parametrically absent in the standard model.

### Scale invariance

One attribute of power laws is their scale invariance. Given a relation $f(x)=ax^{-k}$ , scaling the argument x by a constant factor c causes only a proportionate scaling of the function itself. That is,

$f(cx)=a(cx)^{-k}=c^{-k}f(x)\propto f(x),\!$

where $\propto$ denotes direct proportionality. That is, scaling by a constant c simply multiplies the original power-law relation by the constant $c^{-k}$ . Thus, it follows that all power laws with a particular scaling exponent are equivalent up to constant factors, since each is simply a scaled version of the others. This behavior is what produces the linear relationship when logarithms are taken of both $f(x)$ and x , and the straight-line on the log–log plot is often called the *signature* of a power law. With real data, such straightness is a necessary, but not sufficient, condition for the data following a power-law relation. In fact, there are many ways to generate finite amounts of data that mimic this signature behavior, but, in their asymptotic limit, are not true power laws. Thus, accurately fitting and validating power-law models is an active area of research in statistics; see below.

### Lack of well-defined average value

A power-law $x^{-k}$ has a well-defined mean over $x\in [1,\infty )$ only if $k>2$ , and it has a finite variance only if $k>3$ ; most identified power laws in nature have exponents such that the mean is well-defined but the variance is not, implying they are capable of black swan behavior. This is exemplified by the effect, on the mean income, of the inclusion of the person with the highest income in the world into a sample of individuals of otherwise similar income. Income is distributed according to a power-law known as the Pareto distribution (for example, the net worth of Americans is distributed according to a power law with an exponent of 2).

On the one hand, this makes it incorrect to apply traditional statistics that are based on variance and standard deviation (such as regression analysis). On the other hand, this also allows for cost-efficient interventions. For example, given that car exhaust is distributed according to a power-law among cars (very few cars contribute to most contamination) it would be sufficient to eliminate those very few cars from the road to reduce total exhaust substantially.

The median does exist, however: for a power law *x* –*k*, with exponent ⁠ $k>1$ ⁠, it takes the value 21/(*k* – 1)*x*min, where *x*min is the minimum value for which the power law holds.

### Universality

The equivalence of power laws with a particular scaling exponent can have a deeper origin in the dynamical processes that generate the power-law relation. In physics, for example, phase transitions in thermodynamic systems are associated with the emergence of power-law distributions of certain quantities, whose exponents are referred to as the critical exponents of the system. Diverse systems with the same critical exponents—that is, which display identical scaling behaviour as they approach criticality—can be shown, via renormalization group theory, to share the same fundamental dynamics. For instance, the behavior of water and CO2 at their boiling points fall in the same universality class because they have identical critical exponents. In fact, almost all material phase transitions are described by a small set of universality classes. Similar observations have been made, though not as comprehensively, for various self-organized critical systems, where the critical point of the system is an attractor. Formally, this sharing of dynamics is referred to as universality, and systems with precisely the same critical exponents are said to belong to the same universality class.

## Power-law functions

Scientific interest in power-law relations stems partly from the ease with which certain general classes of mechanisms generate them. The demonstration of a power-law relation in some data can point to specific kinds of mechanisms that might underlie the natural phenomenon in question, and can indicate a deep connection with other, seemingly unrelated systems; see also universality above. The ubiquity of power-law relations in physics is partly due to dimensional constraints, while in complex systems, power laws are often thought to be signatures of hierarchy or of specific stochastic processes. A few notable examples of power laws are Pareto's law of income distribution, structural self-similarity of fractals, scaling laws in biological systems, and scaling laws in cities. Research on the origins of power-law relations, and efforts to observe and validate them in the real world, is an active topic of research in many fields of science, including physics, computer science, linguistics, geophysics, neuroscience, systematics, sociology, economics and more.

However, much of the recent interest in power laws comes from the study of probability distributions: The distributions of a wide variety of quantities seem to follow the power-law form, at least in their upper tail (large events). The behavior of these large events connects these quantities to the study of theory of large deviations (also called extreme value theory), which considers the frequency of extremely rare events like stock market crashes and large natural disasters. It is primarily in the study of statistical distributions that the name "power law" is used.

In empirical contexts, an approximation to a power-law $o(x^{k})$ often includes a deviation term $\varepsilon$ , which can represent uncertainty in the observed values (perhaps measurement or sampling errors) or provide a simple way for observations to deviate from the power-law function (perhaps for stochastic reasons):

$y=ax^{k}+\varepsilon .$

Mathematically, a strict power law cannot be a probability distribution, but a distribution that is a truncated power function is possible: $p(x)=Cx^{-\alpha }$ for $x>x_{\text{min}}$ where the exponent $\alpha$ (Greek letter alpha, not to be confused with scaling factor a used above) is greater than 1 (otherwise the tail has infinite area), the minimum value $x_{\text{min}}$ is needed otherwise the distribution has infinite area as *x* approaches 0, and the constant *C* is a scaling factor to ensure that the total area is 1, as required by a probability distribution. More often one uses an asymptotic power law – one that is only true in the limit; see power-law probability distributions below for details. Typically the exponent falls in the range $2<\alpha <3$ , though not always.

### Examples

More than a hundred power-law distributions have been identified in physics (e.g. sandpile avalanches), biology (e.g. species extinction and body mass), and the social sciences (e.g. city sizes and income). Among them are:

#### Artificial Intelligence

- Neural scaling law

#### Astronomy

- Kepler's third law
- The initial mass function of stars
- The differential energy spectrum of cosmic-ray nuclei
- The M–sigma relation
- Solar flares

#### Biology

- Kleiber's law relating animal metabolism to size, and allometric laws in general
- The two-thirds power law, relating speed to curvature in the human motor system.
- The Taylor's law relating mean population size and variance of populations sizes in ecology
- Neuronal avalanches
- The species richness (number of species) in clades of freshwater fishes
- The Harlow Knapp effect, where a subset of the kinases found in the human body compose a majority of published research
- The size of forest patches globally follows a power law
- The species–area relationship relating the number of species found in an area as a function of the size of the area

#### Chemistry

- Rate law

#### Climate science

- Sizes of cloud areas and perimeters, as viewed from space
- The size of rain-shower cells
- Energy dissipation in cyclones
- Diameters of dust devils on Earth and Mars

#### General science

- Highly optimized tolerance
- Proposed form of experience curve effects
- Pink noise
- The law of stream numbers, and the law of stream lengths (Horton's laws describing river systems)
- Populations of cities (Gibrat's law)
- Bibliograms, and frequencies of words in a text (Zipf's law)
- 90–9–1 principle on wikis (also referred to as the 1% rule)
- Richardson's Law for the severity of violent conflicts (wars and terrorism)
- The relationship between a CPU's cache size and the number of cache misses follows the power law of cache misses.
- The spectral density of the weight matrices of deep neural networks
- Associated with exponential growth:
  - Tails in statistical distributions for exponential growth processes with random observation (or killing)
  - Progress through exponential growth and exponential diffusion of innovations

#### Economics

- Population sizes of cities in a region or urban network, Zipf's law.
- Distribution of artists by the average price of their artworks.
- Income distribution in a market economy.
- Distribution of degrees in banking networks.
- Firm-size distributions.
- Scaling laws of socio-economic quantities with respect to population size (see urban scaling).

#### Finance

- Returns for high-risk venture capital investments
- The mean absolute change of the logarithmic mid-prices
- Large price changes, volatility, and transaction volume on stock exchanges
- Average waiting time of a directional change
- Average waiting time of an overshoot

#### Mathematics

- Fractals
- Pareto distribution and the Pareto principle also called the "80–20 rule"
- Zipf's law in corpus analysis and population distributions amongst others, where frequency of an item or event is inversely proportional to its frequency rank (i.e. the second most frequent item/event occurs half as often as the most frequent item, the third most frequent item/event occurs one third as often as the most frequent item, and so on).
- Zeta distribution (discrete)
- Yule–Simon distribution (discrete)
- Student's t-distribution (continuous), of which the Cauchy distribution is a special case
- Lotka's law
- The scale-free network model
- Hilberg's hypothesis – Power law growth of entropy of language or a stochastic process

#### Physics

- The Angstrom exponent in aerosol optics
- The frequency-dependency of acoustic attenuation in complex media
- The Stefan–Boltzmann law
- The input-voltage–output-current curves of field-effect transistors and vacuum tubes approximate a square-law relationship, a factor in "tube sound".
- Square–cube law (ratio of surface area to volume)
- A 3/2-power law can be found in the plate characteristic curves of triodes.
- The inverse-square laws of Newtonian gravity and electrostatics, as evidenced by the gravitational potential and Electrostatic potential, respectively.
- Self-organized criticality with a critical point as an attractor
- Model of van der Waals force
- Force and potential in simple harmonic motion
- Gamma correction relating light intensity with voltage
- Behaviour near second-order phase transitions involving critical exponents
- The safe operating area relating to maximum simultaneous current and voltage in power semiconductors.
- Supercritical state of matter and supercritical fluids, such as supercritical exponents of heat capacity and viscosity.
- The Curie–von Schweidler law in dielectric responses to step DC voltage input.
- The damping force over speed relation in antiseismic dampers calculus
- Folded solvent-exposed surface areas of centered amino acids in protein structure segments

#### Political Science

- Cube root law of assembly sizes

#### Psychology

- Stevens's power law of psychophysics (challenged with demonstrations that it may be logarithmic)
- The power law of forgetting

### Variants

#### Broken power law

A broken power law is a piecewise function, consisting of two or more power laws, combined with a threshold. For example, with two power laws:

$f(x)\propto x^{\alpha _{1}}$ for $x<x_{\text{th}}$ , $f(x)\propto x_{\text{th}}^{\alpha _{1}-\alpha _{2}}x^{\alpha _{2}}{\text{ for }}x>x_{\text{th}}.$

#### Smoothly broken power law

The pieces of a broken power law can be smoothly spliced together to construct a smoothly broken power law.

There are different possible ways to splice together power laws. One example is the following: $\ln \left({\frac {y}{y_{0}}}+a\right)=c_{0}\ln \left({\frac {x}{x_{0}}}\right)+\sum _{i=1}^{n}{\frac {c_{i}-c_{i-1}}{f_{i}}}\ln \left(1+\left({\frac {x}{x_{i}}}\right)^{f_{i}}\right)$ where $0<x_{0}<x_{1}<\cdots <x_{n}$ .

When the function is plotted as a log-log plot with horizontal axis being $\ln x$ and vertical axis being $\ln(y/y_{0}+a)$ , the plot is composed of $n+1$ linear segments with slopes $c_{0},c_{1},\dots ,c_{n}$ , separated at $x=x_{1},\dots ,x_{n}$ , smoothly spliced together. The size of $f_{i}$ determines the sharpness of splicing between segments $i-1,i$ .

#### Power law with exponential cutoff (truncated power law)

A power law with an exponential cutoff is simply a power law multiplied by an exponential function:

$f(x)\propto x^{-\alpha }e^{-\beta x}.$

#### Curved power law

$f(x)\propto x^{\alpha +\beta x}$

## Power-law probability distributions

In a looser sense, a power-law probability distribution is a distribution whose density function (or mass function in the discrete case) has the form, for large values of x ,

$P(X>x)\sim L(x)x^{-(\alpha -1)}$

where $\alpha >1$ , and $L(x)$ is a slowly varying function, which is any function that satisfies ${\textstyle \lim _{x\to \infty }L(rx)/L(x)=1}$ for any positive factor r . This property of $L(x)$ follows directly from the requirement that $p(x)$ be asymptotically scale invariant; thus, the form of $L(x)$ only controls the shape and finite extent of the lower tail. For instance, if $L(x)$ is the constant function, then we have a power law that holds for all values of x . In many cases, it is convenient to assume a lower bound $x_{\mathrm {min} }$ from which the law holds. Combining these two cases, and where x is a continuous variable, the power law has the form of the Pareto distribution

$p(x)={\frac {\alpha -1}{x_{\min }}}\left({\frac {x}{x_{\min }}}\right)^{-\alpha },$

where the pre-factor to ${\frac {\alpha -1}{x_{\min }}}$ is the normalizing constant. We can now consider several properties of this distribution. For instance, its moments are given by

$\mathbb {E} \left(X^{m}\right)=\int _{x_{\min }}^{\infty }x^{m}p(x)\,\mathrm {d} x={\frac {\alpha -1}{\alpha -1-m}}x_{\min }^{m}$

which is only well defined for $m<\alpha -1$ . That is, all moments $m\geq \alpha -1$ diverge: when $\alpha \leq 2$ , the average and all higher-order moments are infinite; when $2<\alpha <3$ , the mean exists, but the variance and higher-order moments are infinite, etc. For finite-size samples drawn from such distribution, this behavior implies that the central moment estimators (like the mean and the variance) for diverging moments will never converge – as more data is accumulated, they continue to grow. These power-law probability distributions are also called Pareto-type distributions, distributions with Pareto tails, or distributions with regularly varying tails.

A modification, which does not satisfy the general form above, with an exponential cutoff, is

$p(x)\propto L(x)x^{-\alpha }\mathrm {e} ^{-\lambda x}.$

In this distribution, the exponential decay term $\mathrm {e} ^{-\lambda x}$ eventually overwhelms the power-law behavior at very large values of x . This distribution does not scale and is thus not asymptotically as a power law; however, it does approximately scale over a finite region before the cutoff. The pure form above is a subset of this family, with $\lambda =0$ . This distribution is a common alternative to the asymptotic power-law distribution because it naturally captures finite-size effects.

The Tweedie distributions are a family of statistical models characterized by closure under additive and reproductive convolution as well as under scale transformation. Consequently, these models all express a power-law relationship between the variance and the mean. These models have a fundamental role as foci of mathematical convergence similar to the role that the normal distribution has as a focus in the central limit theorem. This convergence effect explains why the variance-to-mean power law manifests so widely in natural processes, as with Taylor's law in ecology and with fluctuation scaling in physics. It can also be shown that this variance-to-mean power law, when demonstrated by the method of expanding bins, implies the presence of 1/*f* noise and that 1/*f* noise can arise as a consequence of this Tweedie convergence effect.

### Graphical methods for identification

Although more sophisticated and robust methods have been proposed, the most frequently used graphical methods of identifying power-law probability distributions using random samples are Pareto quantile-quantile plots (or Pareto Q–Q plots), mean residual life plots and log–log plots. Another, more robust graphical method uses bundles of residual quantile functions. (Please keep in mind that power-law distributions are also called Pareto-type distributions.) It is assumed here that a random sample is obtained from a probability distribution, and that we want to know if the tail of the distribution follows a power law (in other words, we want to know if the distribution has a "Pareto tail"). Here, the random sample is called "the data".

#### Pareto Q–Q plots

Pareto Q–Q plots compare the quantiles of the log-transformed data to the corresponding quantiles of an exponential distribution with mean 1 (or to the quantiles of a standard Pareto distribution) by plotting the former versus the latter. If the resultant scatterplot suggests that the plotted points *asymptotically converge* to a straight line, then a power-law distribution should be suspected. A limitation of Pareto Q–Q plots is that they behave poorly when the tail index $\alpha$ (also called Pareto index) is close to 0, because Pareto Q–Q plots are not designed to identify distributions with slowly varying tails.

#### Mean residual life plots

On the other hand, in its version for identifying power-law probability distributions, the mean residual life plot consists of first log-transforming the data, and then plotting the average of those log-transformed data that are higher than the *i*-th order statistic versus the *i*-th order statistic, for *i* = 1, ..., *n*, where n is the size of the random sample. If the resultant scatterplot suggests that the plotted points tend to stabilize about a horizontal straight line, then a power-law distribution should be suspected. Since the mean residual life plot is very sensitive to outliers (it is not robust), it usually produces plots that are difficult to interpret; for this reason, such plots are usually called Hill horror plots.

#### Log-log plots

Log–log plots are an alternative way of graphically examining the tail of a distribution using a random sample. Taking the logarithm of a power law of the form $f(x)=ax^{k}$ results in:

${\begin{aligned}\log(f(x))&=\log(ax^{k})\\&=\log(a)+\log(x^{k})\\&=\log(a)+k\cdot \log(x),\end{aligned}}$

which forms a straight line with slope k on a log-log scale. Caution has to be exercised however as a log–log plot is necessary but insufficient evidence for a power law relationship, as many non power-law distributions will appear as straight lines on a log–log plot. This method consists of plotting the logarithm of an estimator of the probability that a particular number of the distribution occurs versus the logarithm of that particular number. Usually, this estimator is the proportion of times that the number occurs in the data set. If the points in the plot tend to converge to a straight line for large numbers in the x axis, then the researcher concludes that the distribution has a power-law tail. Examples of the application of these types of plot have been published. A disadvantage of these plots is that, in order for them to provide reliable results, they require huge amounts of data. In addition, they are appropriate only for discrete (or grouped) data.

#### Bundle plots

Another graphical method for the identification of power-law probability distributions using random samples has been proposed. This methodology consists of plotting a *bundle for the log-transformed sample*. Originally proposed as a tool to explore the existence of moments and the moment generation function using random samples, the bundle methodology is based on residual quantile functions (RQFs), also called residual percentile functions, which provide a full characterization of the tail behavior of many well-known probability distributions, including power-law distributions, distributions with other types of heavy tails, and even non-heavy-tailed distributions. Bundle plots do not have the disadvantages of Pareto Q–Q plots, mean residual life plots and log–log plots mentioned above (they are robust to outliers, allow visually identifying power laws with small values of $\alpha$ , and do not demand the collection of much data). In addition, other types of tail behavior can be identified using bundle plots.

### Plotting power-law distributions

In general, power-law distributions are plotted on doubly logarithmic axes, which emphasizes the upper tail region. The most convenient way to do this is via the (complementary) cumulative distribution (ccdf) that is, the survival function, $P(x)=\Pr(X>x)$ ,

$P(x)=\Pr(X>x)=C\int _{x}^{\infty }p(X)\,\mathrm {d} X={\frac {\alpha -1}{x_{\min }^{-\alpha +1}}}\int _{x}^{\infty }X^{-\alpha }\,\mathrm {d} X=\left({\frac {x}{x_{\min }}}\right)^{-(\alpha -1)}.$

The cdf is also a power-law function, but with a smaller scaling exponent. For data, an equivalent form of the cdf is the rank-frequency approach, in which we first sort the n observed values in ascending order, and plot them against the vector $\left[1,{\frac {n-1}{n}},{\frac {n-2}{n}},\dots ,{\frac {1}{n}}\right]$ .

Although it can be convenient to log-bin the data, or otherwise smooth the probability density (mass) function directly, these methods introduce an implicit bias in the representation of the data, and thus should be avoided. The survival function, on the other hand, is more robust to (but not without) such biases in the data and preserves the linear signature on doubly logarithmic axes. Though a survival function representation is favored over that of the pdf while fitting a power law to the data with the linear least square method, it is not devoid of mathematical inaccuracy. Thus, while estimating exponents of a power law distribution, maximum likelihood estimator is recommended.

### Estimating the exponent from empirical data

There are many ways of estimating the value of the scaling exponent for a power-law tail, however not all of them yield unbiased and consistent answers. Some of the most reliable techniques are often based on the method of maximum likelihood. Alternative methods are often based on making a linear regression on either the log–log probability, the log–log cumulative distribution function, or on log-binned data, but these approaches should be avoided as they can all lead to highly biased estimates of the scaling exponent.

#### Maximum likelihood

For real-valued, independent and identically distributed data, we fit a power-law distribution of the form

$p(x)={\frac {\alpha -1}{x_{\min }}}\left({\frac {x}{x_{\min }}}\right)^{-\alpha }$

to the data $x\geq x_{\min }$ , where the coefficient ${\frac {\alpha -1}{x_{\min }}}$ is included to ensure that the distribution is normalized. Given a choice for $x_{\min }$ , the log likelihood function becomes:

${\mathcal {L}}(\alpha )=\log \prod _{i=1}^{n}{\frac {\alpha -1}{x_{\min }}}\left({\frac {x_{i}}{x_{\min }}}\right)^{-\alpha }$ The maximum of this likelihood is found by differentiating with respect to parameter $\alpha$ , setting the result equal to zero. Upon rearrangement, this yields the estimator equation:

${\hat {\alpha }}=1+n\left[\sum _{i=1}^{n}\ln {\frac {x_{i}}{x_{\min }}}\right]^{-1}$

where $\{x_{i}\}$ are the n data points $x_{i}\geq x_{\min }$ . This estimator exhibits a small finite sample-size bias of order $O(n^{-1})$ , which is small when *n* > 100. Further, the standard error of the estimate is $\sigma ={\frac {{\hat {\alpha }}-1}{\sqrt {n}}}+O(n^{-1})$ . This estimator is equivalent to the popular Hill estimator from quantitative finance and extreme value theory.

For a set of *n* integer-valued data points $\{x_{i}\}$ , again where each $x_{i}\geq x_{\min }$ , the maximum likelihood exponent is the solution to the transcendental equation

${\frac {\zeta '({\hat {\alpha }},x_{\min })}{\zeta ({\hat {\alpha }},x_{\min })}}=-{\frac {1}{n}}\sum _{i=1}^{n}\ln {\frac {x_{i}}{x_{\min }}}$

where $\zeta (\alpha ,x_{\mathrm {min} })$ is the incomplete zeta function. The uncertainty in this estimate follows the same formula as for the continuous equation. However, the two equations for ${\hat {\alpha }}$ are not equivalent, and the continuous version should not be applied to discrete data, nor vice versa.

Further, both of these estimators require the choice of $x_{\min }$ . For functions with a non-trivial $L(x)$ function, choosing $x_{\min }$ too small produces a significant bias in ${\hat {\alpha }}$ , while choosing it too large increases the uncertainty in ${\hat {\alpha }}$ , and reduces the statistical power of our model. In general, the best choice of $x_{\min }$ depends strongly on the particular form of the lower tail, represented by $L(x)$ above.

More about these methods, and the conditions under which they can be used, can be found in . Further, this comprehensive review article provides usable code (Matlab, Python, R and C++) for estimation and testing routines for power-law distributions.

#### Kolmogorov–Smirnov estimation

Another method for the estimation of the power-law exponent, which does not assume independent and identically distributed (iid) data, uses the minimization of the Kolmogorov–Smirnov statistic, D , between the cumulative distribution functions of the data and the power law:

${\hat {\alpha }}={\underset {\alpha }{\operatorname {arg\,min} }}\,D_{\alpha }$

with

$D_{\alpha }=\max _{x}\left|P_{\mathrm {emp} }(x)-P_{\alpha }(x)\right|$

where $P_{\mathrm {emp} }(x)$ and $P_{\alpha }(x)$ denote the cdfs of the data and the power law with exponent $\alpha$ , respectively. As this method does not assume iid data, it provides an alternative way to determine the power-law exponent for data sets in which the temporal correlation can not be ignored.

## Validating power laws

Although power-law relations are attractive for many theoretical reasons, demonstrating that data does indeed follow a power-law relation requires more than simply fitting a particular model to the data. This is important for understanding the mechanism that gives rise to the distribution: superficially similar distributions may arise for significantly different reasons, and different models yield different predictions, such as extrapolation.

For example, log-normal distributions are often mistaken for power-law distributions:. When you take the log of its probability density function, the log-normal distribution has terms that are constant, log, and log-squared. When the mean is small and variance is large, the constant in front of the log-squared term is very small. In that case, for most of the distribution, it will be linear on a log-log plot. It is only for extreme values that the log-squared term asserts itself and shows that it is not a power-law.

For example, Gibrat's law about proportional growth processes produce distributions that are lognormal, although their log–log plots look linear over a limited range. An explanation of this is that although the logarithm of the lognormal density function is quadratic in log(*x*), yielding a "bowed" shape in a log–log plot, if the quadratic term is small relative to the linear term then the result can appear almost linear, and the lognormal behavior is only visible when the quadratic term dominates, which may require significantly more data. Therefore, a log–log plot that is slightly "bowed" downwards can reflect a log-normal distribution – not a power law.

In general, many alternative functional forms can appear to follow a power-law form for some extent. Stumpf & Porter (2012) proposed plotting the empirical cumulative distribution function in the log-log domain and claimed that a candidate power-law should cover at least two orders of magnitude. Also, researchers usually have to face the problem of deciding whether or not a real-world probability distribution follows a power law. As a solution to this problem, Diaz proposed a graphical methodology based on random samples that allow visually discerning between different types of tail behavior. This methodology uses bundles of residual quantile functions, also called percentile residual life functions, which characterize many different types of distribution tails, including both heavy and non-heavy tails. However, Stumpf & Porter (2012) claimed the need for both a statistical and a theoretical background in order to support a power-law in the underlying mechanism driving the data generating process.

One method to validate a power-law relation tests many orthogonal predictions of a particular generative mechanism against data. Simply fitting a power-law relation to a particular kind of data is not considered a rational approach. As such, the validation of power-law claims remains a very active field of research in many areas of modern science.
