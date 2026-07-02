---
title: "Nonparametric statistics"
source: https://en.wikipedia.org/wiki/Nonparametric_statistics
domain: mann-whitney
license: CC-BY-SA-4.0
tags: Mann Whitney U test, Wilcoxon rank-sum, stochastic ordering, order statistic
fetched: 2026-07-02
---

# Nonparametric statistics

**Nonparametric statistics** is a type of statistical analysis that makes minimal assumptions about the underlying distribution of the data being studied. Often these models are infinite-dimensional, rather than finite dimensional, as in parametric statistics. Nonparametric statistics can be used for descriptive statistics or statistical inference. Nonparametric tests are often used when the assumptions of parametric tests are evidently violated.

## Definitions

The term "nonparametric statistics" has been defined imprecisely in the following two ways, among others:

The first meaning of *nonparametric* involves techniques that do not rely on data belonging to any particular parametric family of probability distributions. These include, among others:

- Methods which are *distribution-free*, which do not rely on assumptions that the data are drawn from a given parametric family of probability distributions.
- Statistics defined to be a function on a sample, without dependency on a parameter.

An example is order statistics, which are based on ordinal ranking of observations.

The discussion following is taken from *Kendall's Advanced Theory of Statistics*.

> Statistical hypotheses concern the behavior of observable random variables... For example, the hypothesis (a) that a normal distribution has a specified mean and variance is statistical; so is the hypothesis (b) that it has a given mean but unspecified variance; so is the hypothesis (c) that a distribution is of normal form with both mean and variance unspecified; finally, so is the hypothesis (d) that two unspecified continuous distributions are identical.
> 
> It will have been noticed that in the examples (a) and (b) the distribution underlying the observations was taken to be of a certain form (the normal) and the hypothesis was concerned entirely with the value of one or both of its parameters. Such a hypothesis, for obvious reasons, is called *parametric*.
> 
> Hypothesis (c) was of a different nature, as no parameter values are specified in the statement of the hypothesis; we might reasonably call such a hypothesis *nonparametric*. Hypothesis (d) is also nonparametric but, in addition, it does not even specify the underlying form of the distribution and may now be reasonably termed *distribution-free*. Notwithstanding these distinctions, the statistical literature now commonly applies the label "nonparametric" to test procedures that we have just termed "distribution-free", thereby losing a useful classification.

The second meaning of *nonparametric* involves techniques that do not assume that the *structure* of a model is fixed. Typically, the model grows in size to accommodate the complexity of the data. In these techniques, individual variables *are* typically assumed to belong to parametric distributions, and assumptions about the types of associations among variables are also made. These techniques include, among others:

- *nonparametric regression*, which is modeling whereby the structure of the relationship between variables is treated nonparametrically, but where nevertheless there may be parametric assumptions about the distribution of model residuals.
- *nonparametric hierarchical Bayesian models*, such as models based on the Dirichlet process, which allow the number of latent variables to grow as necessary to fit the data, but where individual variables still follow parametric distributions and even the process controlling the rate of growth of latent variables follows a parametric distribution.

## Applications and purpose

Nonparametric methods are widely used for studying populations that have a ranked order (such as movie reviews receiving one to five "stars"). The use of nonparametric methods may be necessary when data have a ranking but no clear numerical interpretation, such as when assessing preferences. In terms of levels of measurement, nonparametric methods result in ordinal data.

As nonparametric methods make fewer assumptions, their applicability is much more general than the corresponding parametric methods. In particular, they may be applied in situations where less is known about the application in question. Also, due to the reliance on fewer assumptions, nonparametric methods are more robust.

Nonparametric methods are sometimes considered simpler to use and more robust than parametric methods, even when the assumptions of parametric methods are justified. This is due to their more general nature, which may make them less susceptible to misuse and misunderstanding. Nonparametric methods can be considered a conservative choice, as they will work even when their assumptions are not met, whereas parametric methods can produce misleading results when their assumptions are violated.

The wider applicability and increased robustness of nonparametric tests comes at a cost: in cases where a parametric test's assumptions are met, nonparametric tests have less statistical power. In other words, a larger sample size can be required to draw conclusions with the same degree of confidence.

## Nonparametric models

*Nonparametric models* differ from parametric models in that the model structure is not specified *à priori* but is instead determined from data. The term *nonparametric* is not meant to imply that such models completely lack parameters but that the number and nature of the parameters are flexible and not fixed in advance.

- Histogram: a simple nonparametric estimate of a probability distribution.
- Kernel density estimation: method to estimate a probability distribution, often based on local averaging.
- Smoothing splines: regression method based on splines.
- Data envelopment analysis: provides efficiency coefficients similar to those obtained by multivariate analysis without any distributional assumption.
- k-nearest neighbors (kNN): classifies the unseen instance based on the k points in the training set which are nearest to it.
- Support vector machine (with a Gaussian kernel): a nonparametric large-margin classifier.
- Method of moments: estimator for a single value, such as the mean or the variance of a distribution.

## Nonparametric tests

**Nonparametric** (or **distribution-free**) **inferential statistical methods** are mathematical procedures for statistical hypothesis testing which, unlike parametric statistics, make no assumptions about the probability distributions of the variables being assessed. The most frequently used tests include

- Analysis of similarities
- Anderson–Darling test: tests whether a sample is drawn from a given distribution
- Statistical bootstrap methods: estimates the accuracy/sampling distribution of a statistic
- Chi-squared test
- Cochran's Q: tests whether *k* treatments in randomized block designs with 0/1 outcomes have identical effects
- Cohen's kappa: measures inter-rater agreement for categorical items
- Friedman two-way analysis of variance (Repeated Measures) by ranks: tests whether *k* treatments in randomized block designs have identical effects
- Empirical likelihood
- Kaplan–Meier: estimates the survival function from lifetime data, modeling censoring
- Kendall's tau: measures statistical dependence between two variables
- Kendall's W: a measure between 0 and 1 of inter-rater agreement.
- Kolmogorov–Smirnov test: tests whether a sample is drawn from a given distribution, or whether two samples are drawn from the same distribution.
- Kruskal–Wallis one-way analysis of variance by ranks: tests whether > 2 independent samples are drawn from the same distribution.
- Kuiper's test: tests whether a sample is drawn from a given distribution, sensitive to cyclic variations such as day of the week.
- Logrank test: compares survival distributions of two right-skewed, censored samples.
- Mann–Whitney U or Wilcoxon rank sum test: tests whether two samples are drawn from the same distribution, as compared to a given alternative hypothesis.
- McNemar's test: tests whether, in 2 × 2 contingency tables with a dichotomous trait and matched pairs of subjects, row and column marginal frequencies are equal.
- Median test: tests whether two samples are drawn from distributions with equal medians.
- Pitman's permutation test: a statistical significance test that yields exact *p* values by examining all possible rearrangements of labels.
- Rank products: detects differentially expressed genes in replicated microarray experiments.
- Siegel–Tukey test: tests for differences in scale between two groups.
- Sign test: tests whether matched pair samples are drawn from distributions with equal medians.
- Spearman's rank correlation coefficient: measures statistical dependence between two variables using a monotonic function.
- Squared ranks test: tests equality of variances in two or more samples.
- Tukey–Duckworth test: tests equality of two distributions by using ranks.
- Wald–Wolfowitz runs test: tests whether the elements of a sequence are mutually independent/random.
- Wilcoxon signed-rank test: tests whether matched pair samples are drawn from populations with different mean ranks.
- Universal Linear Fit Identification: A Method Independent of Data, Outliers and Noise Distribution Model and Free of Missing or Removed Data Imputation.

## Mathematical Statistics

In mathematical statistics, nonparametric models are considered models that do not rely on a parametric assumption of the unknown data distribution (in density estimation problems) or of the regression function (in regression problems). While the goal of any parametric model is the estimation of a finite number of parameters $\theta _{1},\dots ,\theta _{p}\in \mathbb {R}$ , nonparametric models aim to directly estimate the data distribution/regression function.

For the mathematical analysis, however, parametric and nonparametric approaches fit into the same setting: Assuming that the function that is to be estimated (data distribution or regression function) belongs to a set of functions parametrized by a set $\Theta$ , one searches for a (measurable) function $T_{n}:{\mathcal {X}}^{n}\to \Theta$ that estimates the "true" parameter based on data points $x_{1},\dots ,x_{n}\in {\mathcal {X}}$ . The key difference between parametric and nonparametric approaches is that in the former $\Theta \subset \mathbb {R} ^{d}$ for some $d\in \mathbb {N}$ , while in the latter $\Theta$ is typically the set of possible target functions itself, for example, the set of continuous functions or differentiable functions.

Relevant questions in this field regard the construction of reasonable estimators, consistency, rates of convergence and their optimality, and adaptive estimation.

### Consistency

As in parametric statistics, a desirable property for an estimator ${\hat {f_{n}}}$ is that it converges to the target function f as the sample size n goes to infinity, that is, the approximation error converges to zero. Usually, the approximation is measured in terms of $L^{2}$ -norm distance between ${\hat {f_{n}}}$ and f . Since the estimator is a function of the randomly drawn data $X=(X_{1},\dots ,X_{n})$ , the approximation is a random variable as well, and so we distinguish two different modes of convergence:

**Weak consistency:** $\lim _{n\to \infty }\mathbb {E} [\lVert {\hat {f_{n}}}(X)-f\rVert _{L^{2}}^{2}]=0$ .

**Strong consistency:** $\lim _{n\to \infty }\lVert {\hat {f_{n}}}(X)-f\rVert _{L^{2}}^{2}=0$ almost surely.

If an estimator is consistent for all square-integrable f , then it is called **universally consistent**.

Many common nonparametric estimators are weakly universally consistent, for example, the Nadarya-Watson estimator, kNNs and certain local polynomial estimators.

### Minimax optimal rates of convergence

A central topic in the statistical analysis of nonparametric estimators is their speed of convergence towards the true target function f and whether the speed is optimal, i.e., the convergence is as fast as possible. The most common way to measure the speed of convergence of an estimator is the minimax convergence rate, which considers the expected loss of the estimator in the worst case scenario. Under certain assumptions on the smoothness of f , one can show that there is a minimal convergence rates that no estimator can undercut, and so any estimator achieving this minimal rate is called optimal.

Mathematically speaking, the target function f is assumed to belong to some class of functions ${\mathcal {H}}$ , called the *hypothesis class*, inducing a distribution $\mathbb {P} _{f}$ on ${\mathcal {X}}$ , and the approximation quality of an estimator ${\hat {f_{n}}}:{\mathcal {X}}^{n}\to {\mathcal {H}}$ is measured by some function $L:{\mathcal {H}}\times {\mathcal {H}}\to [0,\infty )$ . The minimax convergence rate of ${\hat {f_{n}}}$ is a sequence $(\psi _{n})_{n\in \mathbb {N} }$ of real numbers for which it holds ${\begin{aligned}\limsup _{n\to \infty }{\frac {1}{\psi _{n}}}\sup _{f\in {\mathcal {H}}}\mathbb {E} _{f}{\big [}L{\big (}f,{\hat {f_{n}}}(X_{1},\dots ,X_{n}){\big )}{\big ]}&<\infty ,\\\liminf _{n\to \infty }{\frac {1}{\psi _{n}}}\sup _{f\in {\mathcal {H}}}\mathbb {E} _{f}{\big [}L{\big (}f,{\hat {f_{n}}}(X_{1},\dots ,X_{n}){\big )}{\big ]}&>0,\end{aligned}}$ where $\mathbb {E} _{f}[\cdot ]$ indicates that the random variables $X_{1},\dots ,X_{n}$ , which draw the data points, have distribution $\mathbb {P} _{f}$ .

A universal lower bound on estimation for a hypothesis class ${\mathcal {H}}$ is a sequence $(\psi _{n})_{n\in {\mathcal {N}}}$ for which it holds ${\begin{aligned}\limsup _{n\to \infty }{\frac {1}{\psi _{n}}}\inf _{\hat {\rho _{n}}}\sup _{f\in {\mathcal {H}}}\mathbb {E} _{f}{\big [}L{\big (}f,{\hat {\rho }}_{n}(X_{1},\dots ,X_{n}){\big )}{\big ]}&<\infty ,\\\liminf _{n\to \infty }{\frac {1}{\psi _{n}}}\inf _{\hat {\rho _{n}}}\sup _{f\in {\mathcal {H}}}\mathbb {E} _{f}{\big [}L{\big (}f,{\hat {\rho }}_{n}(X_{1},\dots ,X_{n}){\big )}{\big ]}&>0,\end{aligned}}$ where the infima are taken over all possible estimators ${\hat {\rho }}_{n}$ (that is, measurable functions) based on n observations.

The detailed analysis of nonparametric estimators then separates into the estimation of probability densities and regressions functions.

#### Density estimation

The setting of density estimation typically involves a normed space of functions $({\mathcal {F}},\lVert \cdot \rVert )$ , a subset of density functions ${\mathcal {H}}=\{f\in {\mathcal {F}}:f\geq 0,\int _{\mathcal {X}}f(x)dx=1,\lVert f\rVert \leq 1\}$ and independent random variables $X_{1},\dots ,X_{n}\in {\mathcal {X}}\subset \mathbb {R} ^{d}$ distributed according to the measure with density $f\in {\mathcal {H}}$ , which generates the data.

Minimax lower bounds are known for different pairs of function classes ${\mathcal {F}}$ and comparison metrics L . Common choices for ${\mathcal {F}}$ are:

- ${\mathcal {F}}=C^{\alpha }({\mathcal {X}}),\alpha >0$ : The space of $\lfloor \alpha \rfloor$ -times differentiable functions with the highest derivative being $(\alpha -\lfloor \alpha \rfloor )$ -Hölder-smooth.
- ${\mathcal {F}}=H^{s}({\mathcal {X}})=W^{s,2}({\mathcal {X}}),s>0$ : The space of Sobolev-smooth functions with square-integrable weak derivatives.
- ${\mathcal {F}}=B_{p,q}^{s}({\mathcal {X}}),s>0,p,q\in (0,\infty ]$ : The space of Besov-smooth functions.

In fact, the Hölder spaces and the Sobolev spaces are special cases of some Besov spaces, namely $C^{\alpha }({\mathcal {X}})=B_{\infty ,\infty }^{\alpha }({\mathcal {X}})$ for $\alpha \notin \mathbb {Z}$ and $H^{s}({\mathcal {X}})=B_{2,2}^{s}({\mathcal {X}})$ . Thus, it often suffices to derive lower bounds under Besov-smoothness assumptions.

Common choices for L are:

- $L(f,g)=(f(x_{0})-g(x_{0}))^{2},x_{0}\in {\mathcal {X}}$ : The pointwise squared error (MSE).
- $L(f,g)=\lVert f-g\rVert _{L^{2}({\mathcal {X}})}^{2}$ : The Mean Integrated Square Error (MISE).
- $L(f,g)=\lVert f-g\rVert _{L^{\infty }({\mathcal {X}})}$ : The supremum-norm-distance.
- $L(f,g)=\mathrm {KL} (\mathbb {P} _{f}\lVert \mathbb {P} _{g})$ : The Kullback-Leibler divergence of the distributions induced by f and g .
- $L(f,g)=\mathrm {TV} (\mathbb {P} _{f},\mathbb {P} _{g})$ : The total variation distance of the distributions induced by f and g .
- $L(f,g)=W_{\beta }(\mathbb {P} _{f},\mathbb {P} _{g}),\beta \geq 1$ : The Wasserstein- $\beta$ distance of the distributions induced by f and g .

By Scheffé's theorem, the total variation distance $\mathrm {TV} (\mathbb {P} _{f},\mathbb {P} _{g})$ is equivalent to the $L^{1}$ -distance of f and g .

| Smoothness class | $\lVert f-g\rVert _{L^{2}({\mathcal {X}})}^{2}$ | $W_{\beta }(\mathbb {P} _{f},\mathbb {P} _{g})$ | $\mathrm {TV} (\mathbb {P} _{f},\mathbb {P} _{g})$ | $\mathrm {KL} (\mathbb {P} _{f}\lVert \mathbb {P} _{g})$ |
|---|---|---|---|---|
| $B_{p,q}^{s}({\mathcal {X}})$ | $n^{-{\frac {2s}{2s+d}}}$ $(p,q\geq 1,\,s>d/q)$ | $n^{-{\frac {s+1}{2s+d}}}$ | $n^{-{\frac {s}{2s+d}}}$ | $n^{-{\frac {2s}{2s+d}}}$ |
| $L^{2}(\mathbb {R} )\cap C^{\infty }(\mathbb {R} )$ | $n^{-1}$ | - | - | - |

The lower bound of the MISE is sometimes compared to the Cramér–Rao bound from parametric statistics, which is a lower bound for the mean-squared error of regular unbiased estimators of a parameter $\theta$ : ${\begin{aligned}\sup _{\theta \in \Theta }\mathbb {E} &[\lVert \theta -{\hat {\theta }}_{n}\rVert ^{2}]\geq n^{-1}\underbrace {\sup _{\theta \in \Theta }\mathrm {tr} (I(\theta )^{-1})} _{=const.},\\\sup _{f\in B_{p,q}^{s}({\mathcal {X}})}\mathbb {E} &[\lVert f-{\hat {f_{n}}}\rVert _{L^{2}({\mathcal {X}})}^{2}]\geq cn^{-2s/(2s+d)},\end{aligned}}$ where $I(\theta )$ is the Fisher information of the parametric model and $c>0$ is some constant. The nonparametric rate is thus slower than the parametric rate $n^{-1}$ , especially in large dimensions, and approaches the parametric rate as the smoothness of the density tends to infinity.

Kernel density estimators, for instance, achieve the lower bound w.r.t. the MISE under a Sobolev hypothesis class under an appropriate bandwidth choice and is thus minimax optimal. More recently, also score-based generative models have been shown to achieve minimax convergence rates in total variation and in Wasserstein-1 distance for $B_{p,q}^{s}([0,1]^{d})$ -smooth distributions, $s>(1/p-1/2)_{+}$ , that are bounded away from zero from below.

#### Regression

In the regression setting, the data arises in pairs $(X_{1},Y_{1}),\dots ,(X_{n},Y_{n})$ . Assuming that the data is independent and identically distributed, and $\mathbb {E} [|Y_{1}|]<\infty$ , one can always write $Y_{i}=f(X_{i})+\varepsilon _{i},$ with $f(x)=\mathbb {E} [Y_{1}\mid X_{1}=x]$ being the regression function to be estimated and a *noise* variable $\varepsilon _{i}$ fulfilling $\mathbb {E} [\varepsilon _{i}]=0$ and $\mathbb {E} [\varepsilon ^{2}]=\sigma ^{2}>0$ . Typically, the independent variables $X_{i}$ are assumed to have values in the unit cube $[0,1]^{d}$ and to be either determinsitic points on a grid (deterministic design) or uniformly distributed (random design). Thus, ${\mathcal {X}}=[0,1]^{d}\times \mathbb {R}$ .

The above setting applies to binary classification as well. In that case, the observations take only two values, say 0 and 1, such that $f(x)=\mathbb {E} [\mathbb {1} _{\{Y_{1}=1\}}\mid X=x]=\mathbb {P} (Y_{1}=1\mid X=x)$ and given an estimator ${\hat {f_{n}}}$ of f , the classifiers are assumed to have the form $C(x)=\mathbb {1} _{[1/2,1]}({\hat {f_{n}}}(x))$ , that is, they classify a point as 1 if the estimated probability of $Y=1$ is greater than $1/2$ (and 0 otherwise). Indeed, many classification methods are of that form, for example logistic regression, linear discriminant analysis, quadratic discriminant analysis, and k-nearest-neighbors, and support vector machines.

Then, for the statistical analysis, the hypothesis class is of the form ${\mathcal {H}}=\{f\in {\mathcal {F}}:\lVert f\rVert \leq 1\}$ for some normed space of functions $({\mathcal {F}},\lVert \cdot \rVert )$ and expectations $\mathbb {E} _{f}$ are taken with respect to the joint distribution of X and Y (or just Y if the $X_{i}$ are deterministic).

In nonparametric regression, common choices for ${\mathcal {F}}$ are:

- ${\mathcal {F}}=C^{\alpha }([0,1]^{d}),\alpha >0$ : The space of $\lfloor \alpha \rfloor$ -times differentiable functions with the highest derivative being $(\alpha -\lfloor \alpha \rfloor )$ -Hölder-smooth.
- ${\mathcal {F}}=W^{k,q}([0,1]^{d}),k\in \mathbb {N} ,q>d$ : The space of Sobolev-smooth functions with $L^{q}$ -integrable weak derivatives.

Common choices for L are:

- $L(f,g)=(f(x_{0})-g(x_{0}))^{2},x_{0}\in [0,1]^{d}$ : The pointwise squared error (MSE).
- $L(f,g)=\lVert f-g\rVert _{L^{p}([0,1]^{d})},p\in [1,\infty )$ : The p -th norm.
- $L(f,g)=\lVert f-g\rVert _{L^{\infty }([0,1]^{d})}$ : The supremum-norm-distance.

Under certain technical assumptions, the following lower bounds are known.

| Smoothness class | $(f(x_{0})-g(x_{0}))^{2}$ | $L^{p}([0,1]^{d})$ | $L^{\infty }([0,1]^{d})$ |
|---|---|---|---|
| $C^{\alpha }([0,1]^{d})$ | $n^{-{\frac {2\alpha }{2\alpha +d}}}$ (determ. design) | $n^{-{\frac {\alpha }{2\alpha +d}}}$ | $(\log n/n)^{\frac {\alpha }{2\alpha +d}}$ |
| $W^{k,q}([0,1]^{d})$ | - | $n^{-{\frac {k}{2k+d}}}$ $({\sqrt {n}}/\sigma \geq 1)$ | $n^{-{\frac {k}{2k+d}}}$ $({\sqrt {n}}/\sigma \geq 1)$ |

Some local polynomial estimators are minimax optimal w.r.t. $L^{2}$ under ${\mathcal {H}}=C^{\alpha }([0,1]^{d})$ for arbitrary $\alpha >0$ when the bandwidth is of order ${\mathcal {O}}(n^{-{\frac {1}{2\alpha +d}}})$ . kNNs are also minimax optimal w.r.t. the MSE under ${\mathcal {H}}=C^{2}([0,1]^{d})$ and w.r.t. $L^{2}$ under ${\mathcal {H}}=C^{1}([0,1]^{d})$ when the number of considered neighbors is of order ${\mathcal {O}}(n^{\frac {1}{d+4}})$ and ${\mathcal {O}}(n^{\frac {1}{d+2}})$ respectively.

### Adaptivity

The choice of the model hyperparameters (e.g. bandwidth for kernel methods or number of neighbors for kNN) needed to achieve the optimal convergence rate typically depend on the smoothness parameter of the unknown target function, which means that, in practice, without an appropriate estimation of the hyperparameters, the methods named above are in fact *not* optimal.

Instead, one is interested in methods that achieve the minimax optimal convergence rates not only for one specific smoothness parameter, but across different values. Let the hypothesis class be of the form ${\mathcal {H}}=\bigcup _{\beta >0}{\mathcal {H}}_{\beta }$ (for example ${\mathcal {H}}_{\beta }=C^{\beta }([0,1]^{d})$ or ${\mathcal {H}}_{\beta }=H^{\beta }([0,1]^{d})$ ) and let $\psi _{n}^{\beta }$ be optimal convergence rate in ${\mathcal {H}}_{\beta }$ . Then, a family of estimators $({\hat {f_{n}}})_{n\in \mathbb {N} }$ is called **adaptive in the minimax sense**, if there exists a constant $C(\beta )$ depending only on $\beta$ such that $\sup _{f\in {\mathcal {H}}_{\beta }}\mathbb {E} [L({\hat {f_{n}}},f)]\leq C(\beta )\psi _{n}^{\beta },\quad \forall \beta >0,\quad \forall n\in \mathbb {N} .$ In other words, an adaptive estimator is required to achieve the minimax convergence rate in all hypothesis classes ${\mathcal {H}}_{\beta }$ , but without taking the unknown parameter $\beta$ as argument. Adaptive estimators are often realized by taking estimators that are minimax optimal for a family of hypothesis classes and by estimating the hyperparameters via a higher-level procedure, such as unbiased risk estimation or cross-validation.

## History

Early nonparametric statistics include the median (13th century or earlier, use in estimation by Edward Wright, 1599; see Median § History) and the sign test by John Arbuthnot (1710) in analyzing the human sex ratio at birth (see Sign test § History).
