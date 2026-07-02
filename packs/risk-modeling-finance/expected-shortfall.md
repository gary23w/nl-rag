---
title: "Expected shortfall"
source: https://en.wikipedia.org/wiki/Expected_shortfall
domain: risk-modeling-finance
license: CC-BY-SA-4.0
tags: financial risk modeling, value at risk, credit risk, basel regulation
fetched: 2026-07-02
---

# Expected shortfall

**Expected shortfall** (**ES**) is a risk measure—a concept used in the field of financial risk measurement to evaluate the market risk or credit risk of a portfolio. The "expected shortfall at q% level" is the expected return on the portfolio in the worst $q\%$ of cases. ES is an alternative to value at risk that is more sensitive to the shape of the tail of the loss distribution.

Expected shortfall is also called **conditional value at risk** (**CVaR**), **average value at risk** (**AVaR**), **tail value at risk** (**TVaR**), **conditional tail expectation** (**CTE**), **expected tail loss** (**ETL**), and **superquantile**. These names are often used interchangeably, although several definitions exist in the literature. These definitions coincide in many cases, but may differ for certain types of loss distributions.

## Background

Risk measures are used both in mathematical finance and in actuarial science, and the value-at-risk and expected shortfall measures are often expressed using different sign conventions and tail conventions in these disciplines. The discussion that follows takes the mathematical finance point of view.

In mathematical finance, risk measures arise when considering the profit/loss distribution, i.e., payoff, for a financial portfolio, modeled as a random variable X . This can take positive or negative values, and downside risk corresponds to quantiles with $\alpha$ close to 0. A risk threshold $\alpha \in [0,1]$ is selected, and $\operatorname {VaR} _{\alpha }(X)$ is defined to be the absolute value of the $\alpha$ quantile of X (ignoring some technicalities). This is also the $1-\alpha$ quantile of $-X$ . The expected shortfall at level $\alpha$ is then defined as the average value of $\operatorname {VaR} _{\gamma }(X)$ for $\gamma$ in the interval $[0,\alpha ]$ , i.e., it is the average VaR over all levels below $\alpha$ .

Expected shortfall is often considered preferable to VaR because it accounts for the severity of the failure, not only the chance of failure. Further, it is a coherent spectral measure of financial portfolio risk, while VaR is not. This is a collection of mathematical properties, one of which ensures that diversification of a portfolio never leads to a higher measure of risk. Viewing the value produced by a risk measure as a capital reserve requirement, ES at level $\alpha$ is always more conservative than VaR at the same level, i.e., ES is always at least as big as VaR at the same level.

## Formal definition

If X is an integrable random variable representing the payoff of a portfolio at some future time and $0<\alpha \leq 1$ then the expected shortfall of X at level $\alpha$ is

$\operatorname {ES} _{\alpha }(X)={\frac {1}{\alpha }}\int _{0}^{\alpha }\operatorname {VaR} _{\gamma }(X)\,d\gamma$

where $\operatorname {VaR} _{\gamma }$ is the value at risk.

Several other definitions appear in the literature under the names ES, TVaR, AVaR, CTE, and CVaR. The formulation above as an integral of VaR values is coherent and well-defined in the general case. Other definitions typically coincide under common assumptions such as continuity of the loss distribution, but may differ for distributions with atoms.

The above definition is equivalent to

$\operatorname {ES} _{\alpha }(X)=-{\frac {1}{\alpha }}\left(\operatorname {E} [X\ 1_{\{X\leq x_{\alpha }\}}]+x_{\alpha }(\alpha -P[X\leq x_{\alpha }])\right)$

where $x_{\alpha }=\inf\{x\in \mathbb {R} :P(X\leq x)\geq \alpha \}=-\operatorname {VaR} _{\alpha }(X)$ is the lower $\alpha$ -quantile and $1_{A}(x)={\begin{cases}1&{\text{if }}x\in A\\0&{\text{else}}\end{cases}}$ is the indicator function.

Some authors define expected shortfall, tail conditional expectation, or related quantities directly as a conditional expectation beyond the relevant quantile,

$\operatorname {ES} _{\alpha }(X)=-E[X|X<x_{\alpha }]$

This formulation agrees with the general definition above when the distribution is continuous at $x_{\alpha }$ , but may differ for distributions having atoms at the quantile. Indeed, the second term in the formula just preceding this one vanishes for random variables with continuous distribution functions, and this conditional expectation formula follows.

Some variation in definitions arise from the differing conventions used between, say, financial mathematics and actuarial science, where things written with one set of conventions can be translated into a context with different ones. But there is further inconsistency, with some cases of substantively different definitions used for the same term. For instance, Sweeting defines TVaR as the tail conditional expectation, whereas he defines expected shortfall as the scaled version $\alpha \operatorname {TVaR} _{\alpha }(X)$ .

There are a number of related, but subtly different, formulations for TVaR in the literature. A common case in literature is to define TVaR and average value at risk as the same measure. Under some formulations, it is only equivalent to expected shortfall when the underlying distribution function is continuous at $\operatorname {VaR} _{\alpha }(X)$ , the value at risk of level $\alpha$ .

The dual representation is

$\operatorname {ES} _{\alpha }(X)=\inf _{Q\in {\mathcal {Q}}_{\alpha }}E^{Q}[X]$

where ${\mathcal {Q}}_{\alpha }$ is the set of probability measures which are absolutely continuous to the physical measure P such that ${\frac {dQ}{dP}}\leq \alpha ^{-1}$ almost surely. Note that ${\frac {dQ}{dP}}$ is the Radon–Nikodym derivative of Q with respect to P .

Expected shortfall can be generalized to a general class of coherent risk measures on $L^{p}$ spaces (Lp space) with a corresponding dual characterization in the corresponding $L^{q}$ dual space. The domain can be extended for more general Orlicz Hearts.

If the underlying distribution for X is a continuous distribution then the expected shortfall is equivalent to the tail conditional expectation defined by $\operatorname {TCE} _{\alpha }(X)=E[-X\mid X\leq -\operatorname {VaR} _{\alpha }(X)]$ .

Informally, and non-rigorously, this equation amounts to saying "in case of losses so severe that they occur only alpha percent of the time, what is our average loss".

Expected shortfall can also be written as a distortion risk measure given by the distortion function

$g(x)={\begin{cases}{\frac {x}{1-\alpha }}&{\text{if }}0\leq x<1-\alpha ,\\1&{\text{if }}1-\alpha \leq x\leq 1.\end{cases}}\quad$

## Examples

Example 1. If we believe our average loss on the worst 5% of the possible outcomes for our portfolio is EUR 1000, then we could say our expected shortfall is EUR 1000 for the 5% tail.

Example 2. Consider a portfolio that will have the following possible values at the end of the period:

| probability of event | ending value of the portfolio |
|---|---|
| 10% | 0 |
| 30% | 80 |
| 40% | 100 |
| 20% | 150 |

Now assume that we paid 100 at the beginning of the period for this portfolio. Then the profit in each case is (*ending value*−100) or:

| probability of event | profit |
|---|---|
| 10% | −100 |
| 30% | −20 |
| 40% | 0 |
| 20% | 50 |

From this table let us calculate the expected shortfall $\operatorname {ES} _{q}$ for a few values of q :

| q | expected shortfall $\operatorname {ES} _{q}$ |
|---|---|
| 5% | 100 |
| 10% | 100 |
| 20% | 60 |
| 30% | 46.6 |
| 40% | 40 |
| 50% | 32 |
| 60% | 26.6 |
| 80% | 20 |
| 90% | 12.2 |
| 100% | 6 |

To see how these values were calculated, consider the calculation of $\operatorname {ES} _{0.05}$ , the expectation in the worst 5% of cases. These cases belong to (are a subset of) row 1 in the profit table, which have a profit of −100 (total loss of the 100 invested). The expected profit for these cases is −100.

Now consider the calculation of $\operatorname {ES} _{0.20}$ , the expectation in the worst 20 out of 100 cases. These cases are as follows: 10 cases from row one, and 10 cases from row two (note that 10+10 equals the desired 20 cases). For row 1 there is a profit of −100, while for row 2 a profit of −20. Using the expected value formula we get

${\frac {{\frac {10}{100}}(-100)+{\frac {10}{100}}(-20)}{\frac {20}{100}}}=-60.$

Similarly for any value of q . We select as many rows starting from the top as are necessary to give a cumulative probability of q and then calculate an expectation over those cases. In general, the last row selected may not be fully used (for example in calculating $-\operatorname {ES} _{0.20}$ we used only 10 of the 30 cases per 100 provided by row 2).

As a final example, calculate $-\operatorname {ES} _{1}$ . This is the expectation over all cases, or

$0.1(-100)+0.3(-20)+0.4\cdot 0+0.2\cdot 50=-6.\,$

The value at risk (VaR) is given below for comparison.

| q | $\operatorname {VaR} _{q}$ |
|---|---|
| $0\%\leq q<10\%$ | 100 |
| $10\%\leq q<40\%$ | 20 |
| $40\%\leq q<80\%$ | 0 |
| $80\%\leq q\leq 100\%$ | -50 |

## Properties

The expected shortfall $\operatorname {ES} _{q}$ increases as q decreases.

The 100%-quantile expected shortfall $\operatorname {ES} _{1}$ equals negative of the expected value of the portfolio.

For a given portfolio, the expected shortfall $\operatorname {ES} _{q}$ is greater than or equal to the Value at Risk $\operatorname {VaR} _{q}$ at the same q level.

## Optimization of expected shortfall

Expected shortfall, in its standard form, is known to lead to a generally non-convex optimization problem. However, it is possible to transform the problem into a linear program and find the global solution. This property makes expected shortfall a cornerstone of alternatives to mean-variance portfolio optimization, which account for the higher moments (e.g., skewness and kurtosis) of a return distribution.

Suppose that we want to minimize the expected shortfall of a portfolio. The key contribution of Rockafellar and Uryasev in their 2000 paper is to introduce the auxiliary function $F_{\alpha }(w,\gamma )$ for the expected shortfall: $F_{\alpha }(w,\gamma )=\gamma +{1 \over {1-\alpha }}\int _{\ell (w,x)\geq \gamma }\left[\ell (w,x)-\gamma \right]_{+}p(x)\,dx$ Where $\gamma =\operatorname {VaR} _{\alpha }(X)$ and $\ell (w,x)$ is a loss function for a set of portfolio weights $w\in \mathbb {R} ^{p}$ to be applied to the returns. Rockafellar/Uryasev proved that $F_{\alpha }(w,\gamma )$ is convex with respect to $\gamma$ and is equivalent to the expected shortfall at the minimum point. To numerically compute the expected shortfall for a set of portfolio returns, it is necessary to generate J simulations of the portfolio constituents; this is often done using copulas. With these simulations in hand, the auxiliary function may be approximated by: ${\widetilde {F}}_{\alpha }(w,\gamma )=\gamma +{1 \over {(1-\alpha )J}}\sum _{j=1}^{J}[\ell (w,x_{j})-\gamma ]_{+}$ This is equivalent to the formulation: $\min _{\gamma ,z,w}\;\gamma +{1 \over {(1-\alpha )J}}\sum _{j=1}^{J}z_{j},\quad {\text{s.t. }}z_{j}\geq \ell (w,x_{j})-\gamma ,\;z_{j}\geq 0$ Finally, choosing a linear loss function $\ell (w,x_{j})=-w^{T}x_{j}$ turns the optimization problem into a linear program. Using standard methods, it is then easy to find the portfolio that minimizes expected shortfall.

## Formulas for continuous probability distributions

Closed-form formulas exist for calculating the expected shortfall when the payoff of a portfolio X or a corresponding loss $L=-X$ follows a specific continuous distribution. In the former case, the expected shortfall corresponds to the opposite number of the left-tail conditional expectation below $-\operatorname {VaR} _{\alpha }(X)$ :

$\operatorname {ES} _{\alpha }(X)=E[-X\mid X\leq -\operatorname {VaR} _{\alpha }(X)]=-{\frac {1}{\alpha }}\int _{0}^{\alpha }\operatorname {VaR} _{\gamma }(X)\,d\gamma =-{\frac {1}{\alpha }}\int _{-\infty }^{-\operatorname {VaR} _{\alpha }(X)}xf(x)\,dx.$

Typical values of ${\textstyle \alpha }$ in this case are 5% and 1%.

For engineering or actuarial applications it is more common to consider the distribution of losses $L=-X$ , the expected shortfall in this case corresponds to the right-tail conditional expectation above $\operatorname {VaR} _{\alpha }(L)$ and the typical values of $\alpha$ are 95% and 99%:

$\operatorname {ES} _{\alpha }(L)=\operatorname {E} [L\mid L\geq \operatorname {VaR} _{\alpha }(L)]={\frac {1}{1-\alpha }}\int _{\alpha }^{1}\operatorname {VaR} _{\gamma }(L)\,d\gamma ={\frac {1}{1-\alpha }}\int _{\operatorname {VaR} _{\alpha }(L)}^{+\infty }yf(y)\,dy.$

Since some formulas below were derived for the left-tail case and some for the right-tail case, the following reconciliations can be useful:

$\operatorname {ES} _{\alpha }(X)=-{\frac {1}{\alpha }}\operatorname {E} [X]+{\frac {1-\alpha }{\alpha }}\operatorname {ES} _{\alpha }(L){\text{ and }}\operatorname {ES} _{\alpha }(L)={\frac {1}{1-\alpha }}\operatorname {E} [L]+{\frac {\alpha }{1-\alpha }}\operatorname {ES} _{\alpha }(X).$

### Normal distribution

If the payoff of a portfolio X follows the normal (Gaussian) distribution with p.d.f. $f(x)={\frac {1}{{\sqrt {2\pi }}\sigma }}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\mu +\sigma {\frac {\varphi (\Phi ^{-1}(\alpha ))}{\alpha }}$ , where $\varphi (x)={\frac {1}{\sqrt {2\pi }}}e^{-{\frac {x^{2}}{2}}}$ is the standard normal p.d.f., $\Phi (x)$ is the standard normal c.d.f., so $\Phi ^{-1}(\alpha )$ is the standard normal quantile.

If the loss of a portfolio L follows the normal distribution, the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)=\mu +\sigma {\frac {\varphi (\Phi ^{-1}(\alpha ))}{1-\alpha }}$ .

### Generalized Student's t-distribution

If the payoff of a portfolio X follows the generalized Student's t-distribution with p.d.f. $f(x)={\frac {\Gamma \left({\frac {\nu +1}{2}}\right)}{\Gamma \left({\frac {\nu }{2}}\right){\sqrt {\pi \nu }}\sigma }}\left(1+{\frac {1}{\nu }}\left({\frac {x-\mu }{\sigma }}\right)^{2}\right)^{-{\frac {\nu +1}{2}}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\mu +\sigma {\frac {\nu +(\mathrm {T} ^{-1}(\alpha ))^{2}}{\nu -1}}{\frac {\tau (\mathrm {T} ^{-1}(\alpha ))}{\alpha }}$ , where $\tau (x)={\frac {\Gamma {\bigl (}{\frac {\nu +1}{2}}{\bigr )}}{\Gamma {\bigl (}{\frac {\nu }{2}}{\bigr )}{\sqrt {\pi \nu }}}}{\Bigl (}1+{\frac {x^{2}}{\nu }}{\Bigr )}^{-{\frac {\nu +1}{2}}}$ is the standard t-distribution p.d.f., $\mathrm {T} (x)$ is the standard t-distribution c.d.f., so $\mathrm {T} ^{-1}(\alpha )$ is the standard t-distribution quantile.

If the loss of a portfolio L follows generalized Student's t-distribution, the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)=\mu +\sigma {\frac {\nu +(\mathrm {T} ^{-1}(\alpha ))^{2}}{\nu -1}}{\frac {\tau (\mathrm {T} ^{-1}(\alpha ))}{1-\alpha }}$ .

### Laplace distribution

If the payoff of a portfolio X follows the Laplace distribution with the p.d.f.

$f(x)={\frac {1}{2b}}e^{-|x-\mu |/b}$

and the c.d.f.

$F(x)={\begin{cases}1-{\frac {1}{2}}e^{-(x-\mu )/b}&{\text{if }}x\geq \mu ,\\[4pt]{\frac {1}{2}}e^{(x-\mu )/b}&{\text{if }}x<\mu .\end{cases}}$

then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\mu +b(1-\ln 2\alpha )$ for $\alpha \leq 0.5$ .

If the loss of a portfolio L follows the Laplace distribution, the expected shortfall is equal to

$\operatorname {ES} _{\alpha }(L)={\begin{cases}\mu +b{\frac {\alpha }{1-\alpha }}(1-\ln 2\alpha )&{\text{if }}\alpha <0.5,\\[4pt]\mu +b[1-\ln(2(1-\alpha ))]&{\text{if }}\alpha \geq 0.5.\end{cases}}$

### Logistic distribution

If the payoff of a portfolio X follows the logistic distribution with p.d.f. $f(x)={\frac {1}{s}}e^{-{\frac {x-\mu }{s}}}\left(1+e^{-{\frac {x-\mu }{s}}}\right)^{-2}$ and the c.d.f. $F(x)=\left(1+e^{-{\frac {x-\mu }{s}}}\right)^{-1}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\mu +s\ln {\frac {(1-\alpha )^{1-{\frac {1}{\alpha }}}}{\alpha }}$ .

If the loss of a portfolio L follows the logistic distribution, the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)=\mu +s{\frac {-\alpha \ln \alpha -(1-\alpha )\ln(1-\alpha )}{1-\alpha }}$ .

### Exponential distribution

If the loss of a portfolio L follows the exponential distribution with p.d.f. $f(x)={\begin{cases}\lambda e^{-\lambda x}&{\text{if }}x\geq 0,\\0&{\text{if }}x<0.\end{cases}}$ and the c.d.f. $F(x)={\begin{cases}1-e^{-\lambda x}&{\text{if }}x\geq 0,\\0&{\text{if }}x<0.\end{cases}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)={\frac {-\ln(1-\alpha )+1}{\lambda }}$ .

### Pareto distribution

If the loss of a portfolio L follows the Pareto distribution with p.d.f. $f(x)={\begin{cases}{\frac {ax_{m}^{a}}{x^{a+1}}}&{\text{if }}x\geq x_{m},\\0&{\text{if }}x<x_{m}.\end{cases}}$ and the c.d.f. $F(x)={\begin{cases}1-(x_{m}/x)^{a}&{\text{if }}x\geq x_{m},\\0&{\text{if }}x<x_{m}.\end{cases}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)={\frac {x_{m}a}{(1-\alpha )^{1/a}(a-1)}}$ .

### Generalized Pareto distribution (GPD)

If the loss of a portfolio L follows the GPD with p.d.f.

$f(x)={\frac {1}{s}}\left(1+{\frac {\xi (x-\mu )}{s}}\right)^{\left(-{\frac {1}{\xi }}-1\right)}$

and the c.d.f.

$F(x)={\begin{cases}1-\left(1+{\frac {\xi (x-\mu )}{s}}\right)^{-1/\xi }&{\text{if }}\xi \neq 0,\\1-\exp \left(-{\frac {x-\mu }{s}}\right)&{\text{if }}\xi =0.\end{cases}}$

then the expected shortfall is equal to

$\operatorname {ES} _{\alpha }(L)={\begin{cases}\mu +s\left[{\frac {(1-\alpha )^{-\xi }}{1-\xi }}+{\frac {(1-\alpha )^{-\xi }-1}{\xi }}\right]&{\text{if }}\xi \neq 0,\\\mu +s\left[1-\ln(1-\alpha )\right]&{\text{if }}\xi =0,\end{cases}}$

and the VaR is equal to

$\operatorname {VaR} _{\alpha }(L)={\begin{cases}\mu +s{\frac {(1-\alpha )^{-\xi }-1}{\xi }}&{\text{if }}\xi \neq 0,\\\mu -s\ln(1-\alpha )&{\text{if }}\xi =0.\end{cases}}$

### Weibull distribution

If the loss of a portfolio L follows the Weibull distribution with p.d.f. $f(x)={\begin{cases}{\frac {k}{\lambda }}\left({\frac {x}{\lambda }}\right)^{k-1}e^{-(x/\lambda )^{k}}&{\text{if }}x\geq 0,\\0&{\text{if }}x<0.\end{cases}}$ and the c.d.f. $F(x)={\begin{cases}1-e^{-(x/\lambda )^{k}}&{\text{if }}x\geq 0,\\0&{\text{if }}x<0.\end{cases}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)={\frac {\lambda }{1-\alpha }}\Gamma \left(1+{\frac {1}{k}},-\ln(1-\alpha )\right)$ , where $\Gamma (s,x)$ is the upper incomplete gamma function.

### Generalized extreme value distribution (GEV)

If the payoff of a portfolio X follows the GEV with p.d.f. $f(x)={\begin{cases}{\frac {1}{\sigma }}\left(1+\xi {\frac {x-\mu }{\sigma }}\right)^{-{\frac {1}{\xi }}-1}\exp \left[-\left(1+\xi {\frac {x-\mu }{\sigma }}\right)^{-{1}/{\xi }}\right]&{\text{if }}\xi \neq 0,\\{\frac {1}{\sigma }}e^{-{\frac {x-\mu }{\sigma }}}e^{-e^{-{\frac {x-\mu }{\sigma }}}}&{\text{if }}\xi =0.\end{cases}}$ and c.d.f. $F(x)={\begin{cases}\exp \left(-\left(1+\xi {\frac {x-\mu }{\sigma }}\right)^{-{1}/{\xi }}\right)&{\text{if }}\xi \neq 0,\\\exp \left(-e^{-{\frac {x-\mu }{\sigma }}}\right)&{\text{if }}\xi =0.\end{cases}}$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)={\begin{cases}-\mu -{\frac {\sigma }{\alpha \xi }}{\big [}\Gamma (1-\xi ,-\ln \alpha )-\alpha {\big ]}&{\text{if }}\xi \neq 0,\\-\mu -{\frac {\sigma }{\alpha }}{\big [}{\text{li}}(\alpha )-\alpha \ln(-\ln \alpha ){\big ]}&{\text{if }}\xi =0.\end{cases}}$ and the VaR is equal to $\operatorname {VaR} _{\alpha }(X)={\begin{cases}-\mu -{\frac {\sigma }{\xi }}\left[(-\ln \alpha )^{-\xi }-1\right]&{\text{if }}\xi \neq 0,\\-\mu +\sigma \ln(-\ln \alpha )&{\text{if }}\xi =0.\end{cases}}$ , where $\Gamma (s,x)$ is the upper incomplete gamma function, $\mathrm {li} (x)=\int {\frac {dx}{\ln x}}$ is the logarithmic integral function.

If the loss of a portfolio L follows the GEV, then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)={\begin{cases}\mu +{\frac {\sigma }{(1-\alpha )\xi }}{\bigl [}\gamma (1-\xi ,-\ln \alpha )-(1-\alpha ){\bigr ]}&{\text{if }}\xi \neq 0,\\\mu +{\frac {\sigma }{1-\alpha }}{\bigl [}y-{\text{li}}(\alpha )+\alpha \ln(-\ln \alpha ){\bigr ]}&{\text{if }}\xi =0.\end{cases}}$ , where $\gamma (s,x)$ is the lower incomplete gamma function, y is the Euler-Mascheroni constant.

### Generalized hyperbolic secant (GHS) distribution

If the payoff of a portfolio X follows the GHS distribution with p.d.f. $f(x)={\frac {1}{2\sigma }}\operatorname {sech} \left({\frac {\pi }{2}}{\frac {x-\mu }{\sigma }}\right)$ and the c.d.f. $F(x)={\frac {2}{\pi }}\arctan \left[\exp \left({\frac {\pi }{2}}{\frac {x-\mu }{\sigma }}\right)\right]$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\mu -{\frac {2\sigma }{\pi }}\ln \left(\tan {\frac {\pi \alpha }{2}}\right)-{\frac {2\sigma }{\pi ^{2}\alpha }}i\left[\operatorname {Li} _{2}\left(-i\tan {\frac {\pi \alpha }{2}}\right)-\operatorname {Li} _{2}\left(i\tan {\frac {\pi \alpha }{2}}\right)\right]$ , where $\operatorname {Li} _{2}$ is the dilogarithm and $i={\sqrt {-1}}$ is the imaginary unit.

### Johnson's SU-distribution

If the payoff of a portfolio X follows Johnson's SU-distribution with the c.d.f. $F(x)=\Phi \left[\gamma +\delta \sinh ^{-1}\left({\frac {x-\xi }{\lambda }}\right)\right]$ then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\xi -{\frac {\lambda }{2\alpha }}\left[\exp \left({\frac {1-2\gamma \delta }{2\delta ^{2}}}\right)\;\Phi \left(\Phi ^{-1}(\alpha )-{\frac {1}{\delta }}\right)-\exp \left({\frac {1+2\gamma \delta }{2\delta ^{2}}}\right)\;\Phi \left(\Phi ^{-1}(\alpha )+{\frac {1}{\delta }}\right)\right]$ , where $\Phi$ is the c.d.f. of the standard normal distribution.

### Burr type XII distribution

If the payoff of a portfolio X follows the Burr type XII distribution the p.d.f. $f(x)={\frac {ck}{\beta }}\left({\frac {x-\gamma }{\beta }}\right)^{c-1}\left[1+\left({\frac {x-\gamma }{\beta }}\right)^{c}\right]^{-k-1}$ and the c.d.f. $F(x)=1-\left[1+\left({\frac {x-\gamma }{\beta }}\right)^{c}\right]^{-k}$ , the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\gamma -{\frac {\beta }{\alpha }}\left((1-\alpha )^{-1/k}-1\right)^{1/c}\left[\alpha -1+{_{2}F_{1}}\left({\frac {1}{c}},k;1+{\frac {1}{c}};1-(1-\alpha )^{-1/k}\right)\right]$ , where $_{2}F_{1}$ is the hypergeometric function. Alternatively, $\operatorname {ES} _{\alpha }(X)=-\gamma -{\frac {\beta }{\alpha }}{\frac {ck}{c+1}}\left((1-\alpha )^{-1/k}-1\right)^{1+{\frac {1}{c}}}{_{2}F_{1}}\left(1+{\frac {1}{c}},k+1;2+{\frac {1}{c}};1-(1-\alpha )^{-1/k}\right)$ .

### Dagum distribution

If the payoff of a portfolio X follows the Dagum distribution with p.d.f. $f(x)={\frac {ck}{\beta }}\left({\frac {x-\gamma }{\beta }}\right)^{ck-1}\left[1+\left({\frac {x-\gamma }{\beta }}\right)^{c}\right]^{-k-1}$ and the c.d.f. $F(x)=\left[1+\left({\frac {x-\gamma }{\beta }}\right)^{-c}\right]^{-k}$ , the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=-\gamma -{\frac {\beta }{\alpha }}{\frac {ck}{ck+1}}\left(\alpha ^{-1/k}-1\right)^{-k-{\frac {1}{c}}}{_{2}F_{1}}\left(k+1,k+{\frac {1}{c}};k+1+{\frac {1}{c}};-{\frac {1}{\alpha ^{-1/k}-1}}\right)$ , where $_{2}F_{1}$ is the hypergeometric function.

### Lognormal distribution

If the payoff of a portfolio X follows lognormal distribution, i.e. the random variable $\ln(1+X)$ follows the normal distribution with p.d.f. $f(x)={\frac {1}{{\sqrt {2\pi }}\sigma }}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}$ , then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=1-\exp \left(\mu +{\frac {\sigma ^{2}}{2}}\right){\frac {\Phi \left(\Phi ^{-1}(\alpha )-\sigma \right)}{\alpha }}$ , where $\Phi (x)$ is the standard normal c.d.f., so $\Phi ^{-1}(\alpha )$ is the standard normal quantile.

### Log-logistic distribution

If the payoff of a portfolio X follows log-logistic distribution, i.e. the random variable $\ln(1+X)$ follows the logistic distribution with p.d.f. $f(x)={\frac {1}{s}}e^{-{\frac {x-\mu }{s}}}\left(1+e^{-{\frac {x-\mu }{s}}}\right)^{-2}$ , then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(X)=1-{\frac {e^{\mu }}{\alpha }}I_{\alpha }(1+s,1-s){\frac {\pi s}{\sin \pi s}}$ , where $I_{\alpha }$ is the regularized incomplete beta function, $I_{\alpha }(a,b)={\frac {\mathrm {B} _{\alpha }(a,b)}{\mathrm {B} (a,b)}}$ .

As the incomplete beta function is defined only for positive arguments, for a more generic case the expected shortfall can be expressed with the hypergeometric function: $\operatorname {ES} _{\alpha }(X)=1-{\frac {e^{\mu }\alpha ^{s}}{s+1}}{_{2}F_{1}}(s,s+1;s+2;\alpha )$ .

If the loss of a portfolio L follows log-logistic distribution with p.d.f. $f(x)={\frac {{\frac {b}{a}}(x/a)^{b-1}}{(1+(x/a)^{b})^{2}}}$ and c.d.f. $F(x)={\frac {1}{1+(x/a)^{-b}}}$ , then the expected shortfall is equal to $\operatorname {ES} _{\alpha }(L)={\frac {a}{1-\alpha }}\left[{\frac {\pi }{b}}\csc \left({\frac {\pi }{b}}\right)-\mathrm {B} _{\alpha }\left({\frac {1}{b}}+1,1-{\frac {1}{b}}\right)\right]$ , where $B_{\alpha }$ is the incomplete beta function.

### Log-Laplace distribution

If the payoff of a portfolio X follows log-Laplace distribution, i.e. the random variable $\ln(1+X)$ follows the Laplace distribution the p.d.f. $f(x)={\frac {1}{2b}}e^{-{\frac {|x-\mu |}{b}}}$ , then the expected shortfall is equal to

$\operatorname {ES} _{\alpha }(X)={\begin{cases}1-{\frac {e^{\mu }(2\alpha )^{b}}{b+1}}&{\text{if }}\alpha \leq 0.5,\\1-{\frac {e^{\mu }2^{-b}}{\alpha (b-1)}}\left[(1-\alpha )^{(1-b)}-1\right]&{\text{if }}\alpha >0.5.\end{cases}}$

### Log-generalized hyperbolic secant (log-GHS) distribution

If the payoff of a portfolio X follows log-GHS distribution, i.e. the random variable $\ln(1+X)$ follows the GHS distribution with p.d.f. $f(x)={\frac {1}{2\sigma }}\operatorname {sech} \left({\frac {\pi }{2}}{\frac {x-\mu }{\sigma }}\right)$ , then the expected shortfall is equal to

$\operatorname {ES} _{\alpha }(X)=1-{\frac {1}{\alpha (\sigma +{\pi /2})}}\left(\tan {\frac {\pi \alpha }{2}}\exp {\frac {\pi \mu }{2\sigma }}\right)^{2\sigma /\pi }\tan {\frac {\pi \alpha }{2}}{_{2}F_{1}}\left(1,{\frac {1}{2}}+{\frac {\sigma }{\pi }};{\frac {3}{2}}+{\frac {\sigma }{\pi }};-\tan \left({\frac {\pi \alpha }{2}}\right)^{2}\right),$

where $_{2}F_{1}$ is the hypergeometric function.

## Dynamic expected shortfall

The conditional version of the expected shortfall at the time *t* is defined by

$\operatorname {ES} _{\alpha }^{t}(X)=\operatorname {ess\sup } _{Q\in {\mathcal {Q}}_{\alpha }^{t}}E^{Q}[-X\mid {\mathcal {F}}_{t}]$

where ${\mathcal {Q}}_{\alpha }^{t}=\left\{Q=P\,\vert _{{\mathcal {F}}_{t}}:{\frac {dQ}{dP}}\leq \alpha _{t}^{-1}{\text{ a.s.}}\right\}$ .

This is not a time-consistent risk measure. The time-consistent version is given by

$\rho _{\alpha }^{t}(X)=\operatorname {ess\sup } _{Q\in {\tilde {\mathcal {Q}}}_{\alpha }^{t}}E^{Q}[-X\mid {\mathcal {F}}_{t}]$

such that

${\tilde {\mathcal {Q}}}_{\alpha }^{t}=\left\{Q\ll P:\operatorname {E} \left[{\frac {dQ}{dP}}\mid {\mathcal {F}}_{\tau +1}\right]\leq \alpha _{t}^{-1}\operatorname {E} \left[{\frac {dQ}{dP}}\mid {\mathcal {F}}_{\tau }\right]\;\forall \tau \geq t{\text{ a.s.}}\right\}.$
