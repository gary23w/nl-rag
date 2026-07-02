---
title: "Optimal experimental design"
source: https://en.wikipedia.org/wiki/Optimal_design
domain: response-surface-methodology
license: CC-BY-SA-4.0
tags: response surface methodology, central composite design, Box Behnken, optimal design
fetched: 2026-07-02
---

# Optimal experimental design

(Redirected from

Optimal design

)

In the design of experiments, **optimal experimental designs** (or **optimum designs**) are a class of experimental designs that are optimal with respect to some statistical criterion. The creation of this field of statistics has been credited to Danish statistician Kirstine Smith.

In the design of experiments for estimating statistical models, **optimal designs** allow parameters to be estimated without bias and with minimum variance. A non-optimal design requires a greater number of experimental runs to estimate the parameters with the same precision as an optimal design. In practical terms, optimal experiments can reduce the costs of experimentation.

The optimality of a design depends on the statistical model and is assessed with respect to a statistical criterion, which is related to the variance-matrix of the estimator. Specifying an appropriate model and specifying a suitable criterion function both require understanding of statistical theory and practical knowledge with designing experiments.

## Advantages

Optimal designs offer three advantages over sub-optimal experimental designs:

1. Optimal designs reduce the costs of experimentation by allowing statistical models to be estimated with fewer experimental runs.
2. Optimal designs can accommodate multiple types of factors, such as process, mixture, and discrete factors.
3. Designs can be optimized when the design-space is constrained, for example, when the mathematical process-space contains factor-settings that are practically infeasible (e.g. due to safety concerns).

## Minimizing the variance of estimators

Experimental designs are evaluated using statistical criteria.

It is known that the least squares estimator minimizes the variance of mean-unbiased estimators (under the conditions of the Gauss–Markov theorem). In the estimation theory for statistical models with one real parameter, the reciprocal of the variance of an ("efficient") estimator is called the "Fisher information" for that estimator. Because of this reciprocity, ***minimizing* the *variance*** corresponds to ***maximizing* the *information***.

When the statistical model has several parameters, however, the mean of the parameter-estimator is a vector and its variance is a matrix. The inverse matrix of the variance-matrix is called the "information matrix". Because the variance of the estimator of a parameter vector is a matrix, the problem of "minimizing the variance" is complicated. Using statistical theory, statisticians compress the information-matrix using real-valued summary statistics; being real-valued functions, these "information criteria" can be maximized. The traditional optimality-criteria are invariants of the information matrix; algebraically, the traditional optimality-criteria are functionals of the eigenvalues of the information matrix.

- **A**-optimality ("**average**" or **trace**)
  - One criterion is **A-optimality**, which seeks to minimize the trace of the inverse of the information matrix. This criterion results in minimizing the average variance of the estimates of the regression coefficients.
- **C**-optimality
  - This criterion minimizes the variance of a best linear unbiased estimator of a predetermined linear combination of model parameters.
- **D**-optimality (**determinant**)
  - A popular criterion is **D-optimality**, which seeks to minimize |(X'X)−1|, or equivalently maximize the determinant of the information matrix X'X of the design. This criterion results in maximizing the differential Shannon information content of the parameter estimates.
- **E**-optimality (**eigenvalue**)
  - Another design is **E-optimality**, which maximizes the minimum eigenvalue of the information matrix.
- **S**-optimality
  - This criterion maximizes a quantity measuring the mutual column orthogonality of X and the determinant of the information matrix.
- **T**-optimality
  - This criterion maximizes the discrepancy between two proposed models at the design locations.

Other optimality-criteria are concerned with the variance of predictions:

- **G**-optimality
  - A popular criterion is **G-optimality**, which seeks to minimize the maximum entry in the diagonal of the hat matrix X(X'X)−1X'. This has the effect of minimizing the maximum variance of the predicted values.
- **I**-optimality (**integrated**)
  - A second criterion on prediction variance is **I-optimality**, which seeks to minimize the average prediction variance *over the design space*.
- **V**-optimality (**variance**)
  - A third criterion on prediction variance is **V-optimality**, which seeks to minimize the average prediction variance over a set of m specific points.

### Contrasts

In many applications, the statistician is most concerned with a "parameter of interest" rather than with "nuisance parameters". More generally, statisticians consider linear combinations of parameters, which are estimated via linear combinations of treatment-means in the design of experiments and in the analysis of variance; such linear combinations are called contrasts. Statisticians can use appropriate optimality-criteria for such parameters of interest and for contrasts.

## Implementation

Catalogs of optimal designs occur in books and in software libraries.

In addition, major statistical systems like SAS and R have procedures for optimizing a design according to a user's specification. The experimenter must specify a model for the design and an optimality-criterion before the method can compute an optimal design.

## Practical considerations

Some advanced topics in optimal design require more statistical theory and practical knowledge in designing experiments.

### Model dependence and robustness

Since the optimality criterion of most optimal designs is based on some function of the information matrix, the 'optimality' of a given design is *model dependent*: While an optimal design is best for that model, its performance may deteriorate on other models. On other models, an *optimal* design can be either better or worse than a non-optimal design. Therefore, it is important to benchmark the performance of designs under alternative models.

### Choosing an optimality criterion and robustness

The choice of an appropriate optimality criterion requires some thought, and it is useful to benchmark the performance of designs with respect to several optimality criteria. Cornell writes that

> since the [traditional optimality] criteria . . . are variance-minimizing criteria, . . . a design that is optimal for a given model using one of the . . . criteria is usually near-optimal for the same model with respect to the other criteria.

—

Indeed, there are several classes of designs for which all the traditional optimality-criteria agree, according to the theory of "universal optimality" of Kiefer. The experience of practitioners like Cornell and the "universal optimality" theory of Kiefer suggest that robustness with respect to changes in the *optimality-criterion* is much greater than is robustness with respect to changes in the *model*.

#### Flexible optimality criteria and convex analysis

High-quality statistical software provide a combination of libraries of optimal designs or iterative methods for constructing approximately optimal designs, depending on the model specified and the optimality criterion. Users may use a standard optimality-criterion or may program a custom-made criterion.

All of the traditional optimality-criteria are convex (or concave) functions, and therefore optimal-designs are amenable to the mathematical theory of convex analysis and their computation can use specialized methods of convex minimization. The practitioner need not select *exactly one* traditional, optimality-criterion, but can specify a custom criterion. In particular, the practitioner can specify a convex criterion using the maxima of convex optimality-criteria and nonnegative combinations of optimality criteria (since these operations preserve convex functions). For *convex* optimality criteria, the Kiefer-Wolfowitz equivalence theorem allows the practitioner to verify that a given design is globally optimal. The Kiefer-Wolfowitz equivalence theorem is related with the Legendre-Fenchel conjugacy for convex functions.

If an optimality-criterion lacks convexity, then finding a global optimum and verifying its optimality often are difficult.

### Model uncertainty and Bayesian approaches

#### Model selection

When scientists wish to test several theories, then a statistician can design an experiment that allows optimal tests between specified models. Such "discrimination experiments" are especially important in the biostatistics supporting pharmacokinetics and pharmacodynamics, following the work of Cox and Atkinson.

#### Bayesian experimental design

When practitioners need to consider multiple models, they can specify a probability-measure on the models and then select any design maximizing the expected value of such an experiment. Such probability-based optimal-designs are called optimal Bayesian designs. Such Bayesian designs are used especially for generalized linear models (where the response follows an exponential-family distribution).

The use of a Bayesian design does not force statisticians to use Bayesian methods to analyze the data, however. Indeed, the "Bayesian" label for probability-based experimental-designs is disliked by some researchers. Alternative terminology for "Bayesian" optimality includes "on-average" optimality or "population" optimality.

## Iterative experimentation

Scientific experimentation is an iterative process, and statisticians have developed several approaches to the optimal design of sequential experiments.

### Sequential analysis

Sequential analysis was pioneered by Abraham Wald. In 1972, Herman Chernoff wrote an overview of optimal sequential designs, while adaptive designs were surveyed later by S. Zacks. Of course, much work on the optimal design of experiments is related to the theory of optimal decisions, especially the statistical decision theory of Abraham Wald.

### Response-surface methodology

Optimal designs for response-surface models are discussed in the textbook by Atkinson, Donev and Tobias, and in the survey of Gaffke and Heiligers and in the mathematical text of Pukelsheim. The blocking of optimal designs is discussed in the textbook of Atkinson, Donev and Tobias and also in the monograph by Goos.

The earliest optimal designs were developed to estimate the parameters of regression models with continuous variables, for example, by J. D. Gergonne in 1815 (Stigler). In English, two early contributions were made by Charles S. Peirce and Kirstine Smith.

Pioneering designs for multivariate response-surfaces were proposed by George E. P. Box. However, Box's designs have few optimality properties. Indeed, the Box–Behnken design requires excessive experimental runs when the number of variables exceeds three. Box's "central-composite" designs require more experimental runs than do the optimal designs of Kôno.

### System identification and stochastic approximation

The optimization of sequential experimentation is studied also in stochastic programming and in systems and control. Popular methods include stochastic approximation and other methods of stochastic optimization. Much of this research has been associated with the subdiscipline of system identification. In computational optimal control, D. Judin & A. Nemirovskii and Boris Polyak has described methods that are more efficient than the (Armijo-style) step-size rules introduced by G. E. P. Box in response-surface methodology.

Adaptive designs are used in clinical trials, and optimal adaptive designs are surveyed in the *Handbook of Experimental Designs* chapter by Shelemyahu Zacks.

## Specifying the number of experimental runs

### Using a computer to find a good design

There are several methods of finding an optimal design, given an *a priori* restriction on the number of experimental runs or replications. Some of these methods are discussed by Atkinson, Donev and Tobias and in the paper by Hardin and Sloane. Of course, fixing the number of experimental runs *a priori* would be impractical. Prudent statisticians examine the other optimal designs, whose number of experimental runs differ.

### Discretizing probability-measure designs

In the mathematical theory on optimal experiments, an optimal design can be a probability measure that is supported on an infinite set of observation-locations. Such optimal probability-measure designs solve a mathematical problem that neglected to specify the cost of observations and experimental runs. Nonetheless, such optimal probability-measure designs can be discretized to furnish approximately optimal designs.

In some cases, a finite set of observation-locations suffices to support an optimal design. Such a result was proved by Kôno and Kiefer in their works on response-surface designs for quadratic models. The Kôno–Kiefer analysis explains why optimal designs for response-surfaces can have discrete supports, which are very similar as do the less efficient designs that have been traditional in response surface methodology.

## History

In 1815, an article on optimal designs for polynomial regression was published by Joseph Diaz Gergonne, according to Stigler.

Charles S. Peirce proposed an economic theory of scientific experimentation in 1876, which sought to maximize the precision of the estimates. Peirce's optimal allocation immediately improved the accuracy of gravitational experiments and was used for decades by Peirce and his colleagues. In his 1882 published lecture at Johns Hopkins University, Peirce introduced experimental design with these words:

> Logic will not undertake to inform you what kind of experiments you ought to make in order best to determine the acceleration of gravity, or the value of the Ohm; but it will tell you how to proceed to form a plan of experimentation. [....] Unfortunately practice generally precedes theory, and it is the usual fate of mankind to get things done in some boggling way first, and find out afterward how they could have been done much more easily and perfectly.

Kirstine Smith proposed optimal designs for polynomial models in 1918. (Kirstine Smith had been a student of the Danish statistician Thorvald N. Thiele and was working with Karl Pearson in London.)
