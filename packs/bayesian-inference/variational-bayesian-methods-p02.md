---
title: "Variational Bayesian methods (part 2/2)"
source: https://en.wikipedia.org/wiki/Variational_Bayesian_methods
domain: bayesian-inference
license: CC-BY-SA-4.0
tags: bayesian inference, posterior probability, prior distribution, probabilistic reasoning
fetched: 2026-07-02
part: 2/2
---

## A more complex example

Imagine a Bayesian Gaussian mixture model described as follows:

${\begin{aligned}\mathbf {\pi } &\sim \operatorname {SymDir} (K,\alpha _{0})\\\mathbf {\Lambda } _{i=1\dots K}&\sim {\mathcal {W}}(\mathbf {W} _{0},\nu _{0})\\\mathbf {\mu } _{i=1\dots K}&\sim {\mathcal {N}}(\mathbf {\mu } _{0},(\beta _{0}\mathbf {\Lambda } _{i})^{-1})\\\mathbf {z} [i=1\dots N]&\sim \operatorname {Mult} (1,\mathbf {\pi } )\\\mathbf {x} _{i=1\dots N}&\sim {\mathcal {N}}(\mathbf {\mu } _{z_{i}},{\mathbf {\Lambda } _{z_{i}}}^{-1})\\K&={\text{number of mixing components}}\\N&={\text{number of data points}}\end{aligned}}$

Note:

- SymDir() is the symmetric Dirichlet distribution of dimension K , with the hyperparameter for each component set to $\alpha _{0}$ . The Dirichlet distribution is the conjugate prior of the categorical distribution or multinomial distribution.
- ${\mathcal {W}}()$ is the Wishart distribution, which is the conjugate prior of the precision matrix (inverse covariance matrix) for a multivariate Gaussian distribution.
- Mult() is a multinomial distribution over a single observation (equivalent to a categorical distribution). The state space is a "one-of-K" representation, i.e., a K -dimensional vector in which one of the elements is 1 (specifying the identity of the observation) and all other elements are 0.
- ${\mathcal {N}}()$ is the Gaussian distribution, in this case specifically the multivariate Gaussian distribution.

The interpretation of the above variables is as follows:

- $\mathbf {X} =\{\mathbf {x} _{1},\dots ,\mathbf {x} _{N}\}$ is the set of N data points, each of which is a D -dimensional vector distributed according to a multivariate Gaussian distribution.
- $\mathbf {Z} =\{\mathbf {z} _{1},\dots ,\mathbf {z} _{N}\}$ is a set of latent variables, one per data point, specifying which mixture component the corresponding data point belongs to, using a "one-of-K" vector representation with components $z_{nk}$ for $k=1\dots K$ , as described above.
- $\mathbf {\pi }$ is the mixing proportions for the K mixture components.
- $\mathbf {\mu } _{i=1\dots K}$ and $\mathbf {\Lambda } _{i=1\dots K}$ specify the parameters (mean and precision) associated with each mixture component.

The joint probability of all variables can be rewritten as

$p(\mathbf {X} ,\mathbf {Z} ,\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } )=p(\mathbf {X} \mid \mathbf {Z} ,\mathbf {\mu } ,\mathbf {\Lambda } )p(\mathbf {Z} \mid \mathbf {\pi } )p(\mathbf {\pi } )p(\mathbf {\mu } \mid \mathbf {\Lambda } )p(\mathbf {\Lambda } )$

where the individual factors are

${\begin{aligned}p(\mathbf {X} \mid \mathbf {Z} ,\mathbf {\mu } ,\mathbf {\Lambda } )&=\prod _{n=1}^{N}\prod _{k=1}^{K}{\mathcal {N}}(\mathbf {x} _{n}\mid \mathbf {\mu } _{k},\mathbf {\Lambda } _{k}^{-1})^{z_{nk}}\\p(\mathbf {Z} \mid \mathbf {\pi } )&=\prod _{n=1}^{N}\prod _{k=1}^{K}\pi _{k}^{z_{nk}}\\p(\mathbf {\pi } )&={\frac {\Gamma (K\alpha _{0})}{\Gamma (\alpha _{0})^{K}}}\prod _{k=1}^{K}\pi _{k}^{\alpha _{0}-1}\\p(\mathbf {\mu } \mid \mathbf {\Lambda } )&=\prod _{k=1}^{K}{\mathcal {N}}(\mathbf {\mu } _{k}\mid \mathbf {\mu } _{0},(\beta _{0}\mathbf {\Lambda } _{k})^{-1})\\p(\mathbf {\Lambda } )&=\prod _{k=1}^{K}{\mathcal {W}}(\mathbf {\Lambda } _{k}\mid \mathbf {W} _{0},\nu _{0})\end{aligned}}$

where

${\begin{aligned}{\mathcal {N}}(\mathbf {x} \mid \mathbf {\mu } ,\mathbf {\Sigma } )&={\frac {1}{(2\pi )^{D/2}}}{\frac {1}{|\mathbf {\Sigma } |^{1/2}}}\exp \left\{-{\frac {1}{2}}(\mathbf {x} -\mathbf {\mu } )^{\rm {T}}\mathbf {\Sigma } ^{-1}(\mathbf {x} -\mathbf {\mu } )\right\}\\{\mathcal {W}}(\mathbf {\Lambda } \mid \mathbf {W} ,\nu )&=B(\mathbf {W} ,\nu )|\mathbf {\Lambda } |^{(\nu -D-1)/2}\exp \left(-{\frac {1}{2}}\operatorname {Tr} (\mathbf {W} ^{-1}\mathbf {\Lambda } )\right)\\B(\mathbf {W} ,\nu )&=|\mathbf {W} |^{-\nu /2}\left\{2^{\nu D/2}\pi ^{D(D-1)/4}\prod _{i=1}^{D}\Gamma \left({\frac {\nu +1-i}{2}}\right)\right\}^{-1}\\D&={\text{dimensionality of each data point}}\end{aligned}}$

Assume that $q(\mathbf {Z} ,\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } )=q(\mathbf {Z} )q(\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } )$ .

Then

${\begin{aligned}\ln q^{*}(\mathbf {Z} )&=\operatorname {E} _{\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } }[\ln p(\mathbf {X} ,\mathbf {Z} ,\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } )]+{\text{constant}}\\&=\operatorname {E} _{\mathbf {\pi } }[\ln p(\mathbf {Z} \mid \mathbf {\pi } )]+\operatorname {E} _{\mathbf {\mu } ,\mathbf {\Lambda } }[\ln p(\mathbf {X} \mid \mathbf {Z} ,\mathbf {\mu } ,\mathbf {\Lambda } )]+{\text{constant}}\\&=\sum _{n=1}^{N}\sum _{k=1}^{K}z_{nk}\ln \rho _{nk}+{\text{constant}}\end{aligned}}$

where we have defined

$\ln \rho _{nk}=\operatorname {E} [\ln \pi _{k}]+{\frac {1}{2}}\operatorname {E} [\ln |\mathbf {\Lambda } _{k}|]-{\frac {D}{2}}\ln(2\pi )-{\frac {1}{2}}\operatorname {E} _{\mathbf {\mu } _{k},\mathbf {\Lambda } _{k}}[(\mathbf {x} _{n}-\mathbf {\mu } _{k})^{\rm {T}}\mathbf {\Lambda } _{k}(\mathbf {x} _{n}-\mathbf {\mu } _{k})]$

Exponentiating both sides of the formula for $\ln q^{*}(\mathbf {Z} )$ yields

$q^{*}(\mathbf {Z} )\propto \prod _{n=1}^{N}\prod _{k=1}^{K}\rho _{nk}^{z_{nk}}$

Requiring that this be normalized ends up requiring that the $\rho _{nk}$ sum to 1 over all values of k , yielding

$q^{*}(\mathbf {Z} )=\prod _{n=1}^{N}\prod _{k=1}^{K}r_{nk}^{z_{nk}}$

where

$r_{nk}={\frac {\rho _{nk}}{\sum _{j=1}^{K}\rho _{nj}}}$

In other words, $q^{*}(\mathbf {Z} )$ is a product of single-observation multinomial distributions, and factors over each individual $\mathbf {z} _{n}$ , which is distributed as a single-observation multinomial distribution with parameters $r_{nk}$ for $k=1\dots K$ .

Furthermore, we note that

$\operatorname {E} [z_{nk}]=r_{nk}\,$

which is a standard result for categorical distributions.

Now, considering the factor $q(\mathbf {\pi } ,\mathbf {\mu } ,\mathbf {\Lambda } )$ , note that it automatically factors into $q(\mathbf {\pi } )\prod _{k=1}^{K}q(\mathbf {\mu } _{k},\mathbf {\Lambda } _{k})$ due to the structure of the graphical model defining our Gaussian mixture model, which is specified above.

Then,

${\begin{aligned}\ln q^{*}(\mathbf {\pi } )&=\ln p(\mathbf {\pi } )+\operatorname {E} _{\mathbf {Z} }[\ln p(\mathbf {Z} \mid \mathbf {\pi } )]+{\text{constant}}\\&=(\alpha _{0}-1)\sum _{k=1}^{K}\ln \pi _{k}+\sum _{n=1}^{N}\sum _{k=1}^{K}r_{nk}\ln \pi _{k}+{\text{constant}}\end{aligned}}$

Taking the exponential of both sides, we recognize $q^{*}(\mathbf {\pi } )$ as a Dirichlet distribution

$q^{*}(\mathbf {\pi } )\sim \operatorname {Dir} (\mathbf {\alpha } )\,$

where

$\alpha _{k}=\alpha _{0}+N_{k}\,$

where

$N_{k}=\sum _{n=1}^{N}r_{nk}\,$

Finally

$\ln q^{*}(\mathbf {\mu } _{k},\mathbf {\Lambda } _{k})=\ln p(\mathbf {\mu } _{k},\mathbf {\Lambda } _{k})+\sum _{n=1}^{N}\operatorname {E} [z_{nk}]\ln {\mathcal {N}}(\mathbf {x} _{n}\mid \mathbf {\mu } _{k},\mathbf {\Lambda } _{k}^{-1})+{\text{constant}}$

Grouping and reading off terms involving $\mathbf {\mu } _{k}$ and $\mathbf {\Lambda } _{k}$ , the result is a Gaussian-Wishart distribution given by

$q^{*}(\mathbf {\mu } _{k},\mathbf {\Lambda } _{k})={\mathcal {N}}(\mathbf {\mu } _{k}\mid \mathbf {m} _{k},(\beta _{k}\mathbf {\Lambda } _{k})^{-1}){\mathcal {W}}(\mathbf {\Lambda } _{k}\mid \mathbf {W} _{k},\nu _{k})$

given the definitions

${\begin{aligned}\beta _{k}&=\beta _{0}+N_{k}\\\mathbf {m} _{k}&={\frac {1}{\beta _{k}}}(\beta _{0}\mathbf {\mu } _{0}+N_{k}{\bar {\mathbf {x} }}_{k})\\\mathbf {W} _{k}^{-1}&=\mathbf {W} _{0}^{-1}+N_{k}\mathbf {S} _{k}+{\frac {\beta _{0}N_{k}}{\beta _{0}+N_{k}}}({\bar {\mathbf {x} }}_{k}-\mathbf {\mu } _{0})({\bar {\mathbf {x} }}_{k}-\mathbf {\mu } _{0})^{\rm {T}}\\\nu _{k}&=\nu _{0}+N_{k}\\N_{k}&=\sum _{n=1}^{N}r_{nk}\\{\bar {\mathbf {x} }}_{k}&={\frac {1}{N_{k}}}\sum _{n=1}^{N}r_{nk}\mathbf {x} _{n}\\\mathbf {S} _{k}&={\frac {1}{N_{k}}}\sum _{n=1}^{N}r_{nk}(\mathbf {x} _{n}-{\bar {\mathbf {x} }}_{k})(\mathbf {x} _{n}-{\bar {\mathbf {x} }}_{k})^{\rm {T}}\end{aligned}}$

Finally, notice that these functions require the values of $r_{nk}$ , which make use of $\rho _{nk}$ , which is defined in turn based on $\operatorname {E} [\ln \pi _{k}]$ , $\operatorname {E} [\ln |\mathbf {\Lambda } _{k}|]$ , and $\operatorname {E} _{\mathbf {\mu } _{k},\mathbf {\Lambda } _{k}}[(\mathbf {x} _{n}-\mathbf {\mu } _{k})^{\rm {T}}\mathbf {\Lambda } _{k}(\mathbf {x} _{n}-\mathbf {\mu } _{k})]$ . Now that we have determined the distributions over which these expectations are taken, we can derive formulas for them:

${\begin{aligned}\operatorname {E} _{\mathbf {\mu } _{k},\mathbf {\Lambda } _{k}}[(\mathbf {x} _{n}-\mathbf {\mu } _{k})^{\rm {T}}\mathbf {\Lambda } _{k}(\mathbf {x} _{n}-\mathbf {\mu } _{k})]&=D\beta _{k}^{-1}+\nu _{k}(\mathbf {x} _{n}-\mathbf {m} _{k})^{\rm {T}}\mathbf {W} _{k}(\mathbf {x} _{n}-\mathbf {m} _{k})\\\ln {\widetilde {\Lambda }}_{k}&\equiv \operatorname {E} [\ln |\mathbf {\Lambda } _{k}|]=\sum _{i=1}^{D}\psi \left({\frac {\nu _{k}+1-i}{2}}\right)+D\ln 2+\ln |\mathbf {W} _{k}|\\\ln {\widetilde {\pi }}_{k}&\equiv \operatorname {E} \left[\ln |\pi _{k}|\right]=\psi (\alpha _{k})-\psi \left(\sum _{i=1}^{K}\alpha _{i}\right)\end{aligned}}$

These results lead to

$r_{nk}\propto {\widetilde {\pi }}_{k}{\widetilde {\Lambda }}_{k}^{1/2}\exp \left\{-{\frac {D}{2\beta _{k}}}-{\frac {\nu _{k}}{2}}(\mathbf {x} _{n}-\mathbf {m} _{k})^{\rm {T}}\mathbf {W} _{k}(\mathbf {x} _{n}-\mathbf {m} _{k})\right\}$

These can be converted from proportional to absolute values by normalizing over k so that the corresponding values sum to 1.

Note that:

1. The update equations for the parameters $\beta _{k}$ , $\mathbf {m} _{k}$ , $\mathbf {W} _{k}$ and $\nu _{k}$ of the variables $\mathbf {\mu } _{k}$ and $\mathbf {\Lambda } _{k}$ depend on the statistics $N_{k}$ , ${\bar {\mathbf {x} }}_{k}$ , and $\mathbf {S} _{k}$ , and these statistics in turn depend on $r_{nk}$ .
2. The update equations for the parameters $\alpha _{1\dots K}$ of the variable $\mathbf {\pi }$ depend on the statistic $N_{k}$ , which depends in turn on $r_{nk}$ .
3. The update equation for $r_{nk}$ has a direct circular dependence on $\beta _{k}$ , $\mathbf {m} _{k}$ , $\mathbf {W} _{k}$ and $\nu _{k}$ as well as an indirect circular dependence on $\mathbf {W} _{k}$ , $\nu _{k}$ and $\alpha _{1\dots K}$ through ${\widetilde {\pi }}_{k}$ and ${\widetilde {\Lambda }}_{k}$ .

This suggests an iterative procedure that alternates between two steps:

1. An E-step that computes the value of $r_{nk}$ using the current values of all the other parameters.
2. An M-step that uses the new value of $r_{nk}$ to compute new values of all the other parameters.

Note that these steps correspond closely with the standard EM algorithm to derive a maximum likelihood or maximum a posteriori (MAP) solution for the parameters of a Gaussian mixture model. The responsibilities $r_{nk}$ in the E step correspond closely to the posterior probabilities of the latent variables given the data, i.e. $p(\mathbf {Z} \mid \mathbf {X} )$ ; the computation of the statistics $N_{k}$ , ${\bar {\mathbf {x} }}_{k}$ , and $\mathbf {S} _{k}$ corresponds closely to the computation of corresponding "soft-count" statistics over the data; and the use of those statistics to compute new values of the parameters corresponds closely to the use of soft counts to compute new parameter values in normal EM over a Gaussian mixture model.


## Exponential-family distributions

Note that in the previous example, once the distribution over unobserved variables was assumed to factorize into distributions over the "parameters" and distributions over the "latent data", the derived "best" distribution for each variable was in the same family as the corresponding prior distribution over the variable. This is a general result that holds true for all prior distributions derived from the exponential family.
