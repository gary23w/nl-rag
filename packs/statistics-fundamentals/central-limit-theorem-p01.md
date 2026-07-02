---
title: "Central limit theorem (part 1/2)"
source: https://en.wikipedia.org/wiki/Central_limit_theorem
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 1/2
---

# Central limit theorem

In probability theory, the **central limit theorem** (**CLT**) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution. This holds even if the original variables themselves are not normally distributed. There are several versions of the CLT, each applying in the context of different conditions.

The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

This theorem has seen many changes during the formal development of probability theory. Previous versions of the theorem date back to 1811, but in its modern form it was only precisely stated in the 1920s.

In statistics, the CLT can be stated as: let X 1 , X 2 , … , X n {\displaystyle X_{1},X_{2},\dots ,X_{n}} ({\displaystyle X_{1},X_{2},\dots ,X_{n}}) denote a statistical sample of size n {\displaystyle n} ({\displaystyle n}) from a population with expected value (average) μ {\displaystyle \mu } ({\displaystyle \mu }) and finite positive variance σ 2 {\displaystyle \sigma ^{2}} ({\displaystyle \sigma ^{2}}), and let X ¯ n {\displaystyle {\bar {X}}_{n}} ({\displaystyle {\bar {X}}_{n}}) denote the sample mean (which is itself a random variable). Then the limit as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }) of the distribution of ( X ¯ n − μ ) n {\displaystyle ({\bar {X}}_{n}-\mu ){\sqrt {n}}} ({\displaystyle ({\bar {X}}_{n}-\mu ){\sqrt {n}}}) is a normal distribution with mean 0 {\displaystyle 0} ({\displaystyle 0}) and variance σ 2 {\displaystyle \sigma ^{2}} ({\displaystyle \sigma ^{2}}).

In other words, suppose that a large sample of observations is obtained, each observation being randomly produced in a way that does not depend on the values of the other observations, and the average (arithmetic mean) of the observed values is computed. If this procedure is performed many times, resulting in a collection of observed averages, the central limit theorem says that if the sample size is large enough, the probability distribution of these averages will closely approximate a normal distribution.

The central limit theorem has several variants. In its common form, the random variables must be independent and identically distributed (i.i.d.). This requirement can be weakened; convergence of the mean to the normal distribution also occurs for non-identical distributions or for non-independent observations if they comply with certain conditions.

The earliest version of this theorem, that the normal distribution may be used as an approximation to the binomial distribution, is the de Moivre–Laplace theorem.


## Independent sequences

### Classical CLT

Let ( X n ) n ≥ 1 {\displaystyle (X_{n})_{n\geq 1}} ({\displaystyle (X_{n})_{n\geq 1}}) be a sequence of i.i.d. random variables having a distribution with expected value given by μ {\displaystyle \mu } ({\displaystyle \mu }) and finite variance given by σ 2 . {\displaystyle \sigma ^{2}.} ({\displaystyle \sigma ^{2}.}) Suppose we are interested in the sample average

X ¯ n ≡ X 1 + ⋯ + X n n . {\displaystyle {\bar {X}}_{n}\equiv {\frac {X_{1}+\cdots +X_{n}}{n}}.} ({\displaystyle {\bar {X}}_{n}\equiv {\frac {X_{1}+\cdots +X_{n}}{n}}.})

By the law of large numbers, the sample average converges almost surely (and therefore also converges in probability) to the expected value μ {\displaystyle \mu } ({\displaystyle \mu }) as n → ∞ . {\displaystyle n\to \infty .} ({\displaystyle n\to \infty .})

The classical central limit theorem describes the size and the distributional form of the stochastic fluctuations around the deterministic number μ {\displaystyle \mu } ({\displaystyle \mu }) during this convergence. More precisely, it states that as n {\displaystyle n} ({\displaystyle n}) gets larger, the distribution of the normalized mean n ( X ¯ n − μ ) {\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )} ({\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )}), i.e. the difference between the sample average X ¯ n {\displaystyle {\bar {X}}_{n}} ({\displaystyle {\bar {X}}_{n}}) and its limit μ , {\displaystyle \mu ,} ({\displaystyle \mu ,}) scaled by the factor n {\displaystyle {\sqrt {n}}} ({\displaystyle {\sqrt {n}}}), approaches the normal distribution with mean 0 {\displaystyle 0} ({\displaystyle 0}) and variance σ 2 . {\displaystyle \sigma ^{2}.} ({\displaystyle \sigma ^{2}.}) For large enough n , {\displaystyle n,} ({\displaystyle n,}) the distribution of X ¯ n {\displaystyle {\bar {X}}_{n}} ({\displaystyle {\bar {X}}_{n}}) gets arbitrarily close to the normal distribution with mean μ {\displaystyle \mu } ({\displaystyle \mu }) and variance σ 2 / n . {\displaystyle \sigma ^{2}/n.} ({\displaystyle \sigma ^{2}/n.})

The usefulness of the theorem is that the distribution of n ( X ¯ n − μ ) {\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )} ({\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )}) approaches normality regardless of the shape of the distribution of the individual X i . {\displaystyle X_{i}.} ({\displaystyle X_{i}.}) Formally, the theorem can be stated as follows:

**Lindeberg–Lévy CLT**—Suppose X 1 , X 2 , X 3 … {\displaystyle X_{1},X_{2},X_{3}\ldots } ({\displaystyle X_{1},X_{2},X_{3}\ldots }) is a sequence of i.i.d. random variables with E ⁡ [ X i ] = μ {\displaystyle \operatorname {E} [X_{i}]=\mu } ({\displaystyle \operatorname {E} [X_{i}]=\mu }) and Var ⁡ [ X i ] = σ 2 < ∞ . {\displaystyle \operatorname {Var} [X_{i}]=\sigma ^{2}<\infty .} ({\displaystyle \operatorname {Var} [X_{i}]=\sigma ^{2}<\infty .}) Then, as n {\displaystyle n} ({\displaystyle n}) approaches infinity, the random variables n ( X ¯ n − μ ) {\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )} ({\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )}) converge in distribution to a normal N ( 0 , σ 2 ) {\displaystyle {\mathcal {N}}(0,\sigma ^{2})} ({\displaystyle {\mathcal {N}}(0,\sigma ^{2})}):

n ( X ¯ n − μ ) ⟶ d N ( 0 , σ 2 ) . {\displaystyle {\sqrt {n}}\left({\bar {X}}_{n}-\mu \right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}\left(0,\sigma ^{2}\right).} ({\displaystyle {\sqrt {n}}\left({\bar {X}}_{n}-\mu \right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}\left(0,\sigma ^{2}\right).})

In the case σ > 0 , {\displaystyle \sigma >0,} ({\displaystyle \sigma >0,}) convergence in distribution means that the cumulative distribution functions of n ( X ¯ n − μ ) {\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )} ({\displaystyle {\sqrt {n}}({\bar {X}}_{n}-\mu )}) converge pointwise to the cdf of the N ( 0 , σ 2 ) {\displaystyle {\mathcal {N}}(0,\sigma ^{2})} ({\displaystyle {\mathcal {N}}(0,\sigma ^{2})}) distribution: for every real number z , {\displaystyle z,} ({\displaystyle z,})

lim n → ∞ P [ n ( X ¯ n − μ ) ≤ z ] = lim n → ∞ P [ n ( X ¯ n − μ ) σ ≤ z σ ] = Φ ( z σ ) , {\displaystyle \lim _{n\to \infty }\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]=\lim _{n\to \infty }\mathbb {P} \left[{\frac {{\sqrt {n}}({\bar {X}}_{n}-\mu )}{\sigma }}\leq {\frac {z}{\sigma }}\right]=\Phi \left({\frac {z}{\sigma }}\right),} ({\displaystyle \lim _{n\to \infty }\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]=\lim _{n\to \infty }\mathbb {P} \left[{\frac {{\sqrt {n}}({\bar {X}}_{n}-\mu )}{\sigma }}\leq {\frac {z}{\sigma }}\right]=\Phi \left({\frac {z}{\sigma }}\right),})

where Φ ( z ) {\displaystyle \Phi (z)} ({\displaystyle \Phi (z)}) is the standard normal cdf evaluated at z . {\displaystyle z.} ({\displaystyle z.}) The convergence is uniform in z {\displaystyle z} ({\displaystyle z}) in the sense that

lim n → ∞ sup z ∈ R | P [ n ( X ¯ n − μ ) ≤ z ] − Φ ( z σ ) | = 0   , {\displaystyle \lim _{n\to \infty }\;\sup _{z\in \mathbb {R} }\;\left|\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]-\Phi \left({\frac {z}{\sigma }}\right)\right|=0~,} ({\displaystyle \lim _{n\to \infty }\;\sup _{z\in \mathbb {R} }\;\left|\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]-\Phi \left({\frac {z}{\sigma }}\right)\right|=0~,})

where sup {\displaystyle \sup } ({\displaystyle \sup }) denotes the supremum (i.e. least upper bound) of the set.

### Lyapunov CLT

In this variant of the central limit theorem the random variables X i {\textstyle X_{i}} ({\textstyle X_{i}}) have to be independent, but not necessarily identically distributed. The theorem also requires that random variables | X i | {\textstyle \left|X_{i}\right|} ({\textstyle \left|X_{i}\right|}) have moments of some order ( 2 + δ ) {\textstyle (2+\delta )} ({\textstyle (2+\delta )}), and that the rate of growth of these moments is limited by the Lyapunov condition given below.

**Lyapunov CLT**—Suppose { X 1 , … , X n , … } {\textstyle \{X_{1},\ldots ,X_{n},\ldots \}} ({\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}) is a sequence of independent random variables, each with finite expected value μ i {\textstyle \mu _{i}} ({\textstyle \mu _{i}}) and variance σ i 2 {\textstyle \sigma _{i}^{2}} ({\textstyle \sigma _{i}^{2}}). Define

s n 2 = ∑ i = 1 n σ i 2 . {\displaystyle s_{n}^{2}=\sum _{i=1}^{n}\sigma _{i}^{2}.} ({\displaystyle s_{n}^{2}=\sum _{i=1}^{n}\sigma _{i}^{2}.})

If for some δ > 0 {\textstyle \delta >0} ({\textstyle \delta >0}), *Lyapunov's condition*

lim n → ∞ 1 s n 2 + δ ∑ i = 1 n E ⁡ [ | X i − μ i | 2 + δ ] = 0 {\displaystyle \lim _{n\to \infty }\;{\frac {1}{s_{n}^{2+\delta }}}\,\sum _{i=1}^{n}\operatorname {E} \left[\left|X_{i}-\mu _{i}\right|^{2+\delta }\right]=0} ({\displaystyle \lim _{n\to \infty }\;{\frac {1}{s_{n}^{2+\delta }}}\,\sum _{i=1}^{n}\operatorname {E} \left[\left|X_{i}-\mu _{i}\right|^{2+\delta }\right]=0})

is satisfied, then a sum of X i − μ i s n {\textstyle {\frac {X_{i}-\mu _{i}}{s_{n}}}} ({\textstyle {\frac {X_{i}-\mu _{i}}{s_{n}}}}) converges in distribution to a standard normal random variable, as n {\textstyle n} ({\textstyle n}) goes to infinity:

1 s n ∑ i = 1 n ( X i − μ i ) ⟶ d N ( 0 , 1 ) . {\displaystyle {\frac {1}{s_{n}}}\,\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}(0,1).} ({\displaystyle {\frac {1}{s_{n}}}\,\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}(0,1).})

In practice it is usually easiest to check Lyapunov's condition for δ = 1 {\textstyle \delta =1} ({\textstyle \delta =1}).

If a sequence of random variables satisfies Lyapunov's condition, then it also satisfies Lindeberg's condition. The converse implication, however, does not hold.

### Lindeberg (-Feller) CLT

In the same setting and with the same notation as above, the Lyapunov condition can be replaced with the following weaker one (from Lindeberg in 1920).

Suppose that for every ε > 0 {\textstyle \varepsilon >0} ({\textstyle \varepsilon >0}),

lim n → ∞ 1 s n 2 ∑ i = 1 n E ⁡ [ ( X i − μ i ) 2 ⋅ 1 { | X i − μ i | > ε s n } ] = 0 {\displaystyle \lim _{n\to \infty }{\frac {1}{s_{n}^{2}}}\sum _{i=1}^{n}\operatorname {E} \left[(X_{i}-\mu _{i})^{2}\cdot \mathbf {1} _{\left\{\left|X_{i}-\mu _{i}\right|>\varepsilon s_{n}\right\}}\right]=0} ({\displaystyle \lim _{n\to \infty }{\frac {1}{s_{n}^{2}}}\sum _{i=1}^{n}\operatorname {E} \left[(X_{i}-\mu _{i})^{2}\cdot \mathbf {1} _{\left\{\left|X_{i}-\mu _{i}\right|>\varepsilon s_{n}\right\}}\right]=0})

where 1 { … } {\textstyle \mathbf {1} _{\{\ldots \}}} ({\textstyle \mathbf {1} _{\{\ldots \}}}) is the indicator function. Then the distribution of the standardized sums

1 s n ∑ i = 1 n ( X i − μ i ) {\displaystyle {\frac {1}{s_{n}}}\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)} ({\displaystyle {\frac {1}{s_{n}}}\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)})

converges towards the standard normal distribution N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}).

### CLT for the sum of a random number of random variables

Rather than summing an integer number n {\displaystyle n} ({\displaystyle n}) of random variables and taking n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }), the sum can be of a random number N {\displaystyle N} ({\displaystyle N}) of random variables, with conditions on N {\displaystyle N} ({\displaystyle N}). For example, the following theorem is Corollary 4 of Robbins (1948). It assumes that N {\displaystyle N} ({\displaystyle N}) is asymptotically normal (Robbins also developed other conditions that lead to the same result).

**Robbins CLT**—Let { X i , i ≥ 1 } {\displaystyle \{X_{i},i\geq 1\}} ({\displaystyle \{X_{i},i\geq 1\}}) be independent, identically distributed random variables with E ( X i ) = μ {\displaystyle E(X_{i})=\mu } ({\displaystyle E(X_{i})=\mu }) and Var ( X i ) = σ 2 {\displaystyle {\text{Var}}(X_{i})=\sigma ^{2}} ({\displaystyle {\text{Var}}(X_{i})=\sigma ^{2}}), and let { N n , n ≥ 1 } {\displaystyle \{N_{n},n\geq 1\}} ({\displaystyle \{N_{n},n\geq 1\}}) be a sequence of non-negative integer-valued random variables that are independent of { X i , i ≥ 1 } {\displaystyle \{X_{i},i\geq 1\}} ({\displaystyle \{X_{i},i\geq 1\}}). Assume for each n = 1 , 2 , … {\displaystyle n=1,2,\dots } ({\displaystyle n=1,2,\dots }) that E ( N n 2 ) < ∞ {\displaystyle E(N_{n}^{2})<\infty } ({\displaystyle E(N_{n}^{2})<\infty }) and

N n − E ( N n ) Var ( N n ) → d N ( 0 , 1 ) {\displaystyle {\frac {N_{n}-E(N_{n})}{\sqrt {{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)} ({\displaystyle {\frac {N_{n}-E(N_{n})}{\sqrt {{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)})

where → d {\displaystyle \xrightarrow {\,d\,} } ({\displaystyle \xrightarrow {\,d\,} }) denotes convergence in distribution and N ( 0 , 1 ) {\displaystyle {\mathcal {N}}(0,1)} ({\displaystyle {\mathcal {N}}(0,1)}) is the normal distribution with mean 0, variance 1. Then

∑ i = 1 N n X i − μ E ( N n ) σ 2 E ( N n ) + μ 2 Var ( N n ) → d N ( 0 , 1 ) {\displaystyle {\frac {\sum _{i=1}^{N_{n}}X_{i}-\mu E(N_{n})}{\sqrt {\sigma ^{2}E(N_{n})+\mu ^{2}{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)} ({\displaystyle {\frac {\sum _{i=1}^{N_{n}}X_{i}-\mu E(N_{n})}{\sqrt {\sigma ^{2}E(N_{n})+\mu ^{2}{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)})

### Multidimensional CLT

Proofs that use characteristic functions can be extended to cases where each individual X i {\textstyle \mathbf {X} _{i}} ({\textstyle \mathbf {X} _{i}}) is a random vector in R k {\textstyle \mathbb {R} ^{k}} ({\textstyle \mathbb {R} ^{k}}), with mean vector μ = E ⁡ [ X i ] {\textstyle {\boldsymbol {\mu }}=\operatorname {E} [\mathbf {X} _{i}]} ({\textstyle {\boldsymbol {\mu }}=\operatorname {E} [\mathbf {X} _{i}]}) and covariance matrix Σ {\textstyle \mathbf {\Sigma } } ({\textstyle \mathbf {\Sigma } }) (among the components of the vector), and these random vectors are independent and identically distributed. The multidimensional central limit theorem states that when scaled, sums converge to a multivariate normal distribution. Summation of these vectors is done component-wise.

For i = 1 , 2 , 3 , … , {\displaystyle i=1,2,3,\ldots ,} ({\displaystyle i=1,2,3,\ldots ,}) let

X i = [ X i ( 1 ) ⋮ X i ( k ) ] {\displaystyle \mathbf {X} _{i}={\begin{bmatrix}X_{i}^{(1)}\\\vdots \\X_{i}^{(k)}\end{bmatrix}}} ({\displaystyle \mathbf {X} _{i}={\begin{bmatrix}X_{i}^{(1)}\\\vdots \\X_{i}^{(k)}\end{bmatrix}}})

be independent random vectors. The sum of the random vectors X 1 , … , X n {\displaystyle \mathbf {X} _{1},\ldots ,\mathbf {X} _{n}} ({\displaystyle \mathbf {X} _{1},\ldots ,\mathbf {X} _{n}}) is

∑ i = 1 n X i = [ X 1 ( 1 ) ⋮ X 1 ( k ) ] + [ X 2 ( 1 ) ⋮ X 2 ( k ) ] + ⋯ + [ X n ( 1 ) ⋮ X n ( k ) ] = [ ∑ i = 1 n X i ( 1 ) ⋮ ∑ i = 1 n X i ( k ) ] {\displaystyle \sum _{i=1}^{n}\mathbf {X} _{i}={\begin{bmatrix}X_{1}^{(1)}\\\vdots \\X_{1}^{(k)}\end{bmatrix}}+{\begin{bmatrix}X_{2}^{(1)}\\\vdots \\X_{2}^{(k)}\end{bmatrix}}+\cdots +{\begin{bmatrix}X_{n}^{(1)}\\\vdots \\X_{n}^{(k)}\end{bmatrix}}={\begin{bmatrix}\sum _{i=1}^{n}X_{i}^{(1)}\\\vdots \\\sum _{i=1}^{n}X_{i}^{(k)}\end{bmatrix}}} ({\displaystyle \sum _{i=1}^{n}\mathbf {X} _{i}={\begin{bmatrix}X_{1}^{(1)}\\\vdots \\X_{1}^{(k)}\end{bmatrix}}+{\begin{bmatrix}X_{2}^{(1)}\\\vdots \\X_{2}^{(k)}\end{bmatrix}}+\cdots +{\begin{bmatrix}X_{n}^{(1)}\\\vdots \\X_{n}^{(k)}\end{bmatrix}}={\begin{bmatrix}\sum _{i=1}^{n}X_{i}^{(1)}\\\vdots \\\sum _{i=1}^{n}X_{i}^{(k)}\end{bmatrix}}})

and their average is

X ¯ n = [ X ¯ i ( 1 ) ⋮ X ¯ i ( k ) ] = 1 n ∑ i = 1 n X i . {\displaystyle \mathbf {{\bar {X}}_{n}} ={\begin{bmatrix}{\bar {X}}_{i}^{(1)}\\\vdots \\{\bar {X}}_{i}^{(k)}\end{bmatrix}}={\frac {1}{n}}\sum _{i=1}^{n}\mathbf {X} _{i}.} ({\displaystyle \mathbf {{\bar {X}}_{n}} ={\begin{bmatrix}{\bar {X}}_{i}^{(1)}\\\vdots \\{\bar {X}}_{i}^{(k)}\end{bmatrix}}={\frac {1}{n}}\sum _{i=1}^{n}\mathbf {X} _{i}.})

Therefore,

1 n ∑ i = 1 n [ X i − E ⁡ ( X i ) ] = 1 n ∑ i = 1 n ( X i − μ ) = n ( X ¯ n − μ ) . {\displaystyle {\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}\left[\mathbf {X} _{i}-\operatorname {E} \left(\mathbf {X} _{i}\right)\right]={\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}(\mathbf {X} _{i}-{\boldsymbol {\mu }})={\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right).} ({\displaystyle {\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}\left[\mathbf {X} _{i}-\operatorname {E} \left(\mathbf {X} _{i}\right)\right]={\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}(\mathbf {X} _{i}-{\boldsymbol {\mu }})={\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right).})

The multivariate central limit theorem states that

n ( X ¯ n − μ ) ⟶ d N k ( 0 , Σ ) , {\displaystyle {\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}_{k}(0,{\boldsymbol {\Sigma }}),} ({\displaystyle {\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}_{k}(0,{\boldsymbol {\Sigma }}),}) where the covariance matrix Σ {\displaystyle {\boldsymbol {\Sigma }}} ({\displaystyle {\boldsymbol {\Sigma }}}) is equal to Σ = [ Var ⁡ ( X 1 ( 1 ) ) Cov ⁡ ( X 1 ( 1 ) , X 1 ( 2 ) ) Cov ⁡ ( X 1 ( 1 ) , X 1 ( 3 ) ) ⋯ Cov ⁡ ( X 1 ( 1 ) , X 1 ( k ) ) Cov ⁡ ( X 1 ( 2 ) , X 1 ( 1 ) ) Var ⁡ ( X 1 ( 2 ) ) Cov ⁡ ( X 1 ( 2 ) , X 1 ( 3 ) ) ⋯ Cov ⁡ ( X 1 ( 2 ) , X 1 ( k ) ) Cov ⁡ ( X 1 ( 3 ) , X 1 ( 1 ) ) Cov ⁡ ( X 1 ( 3 ) , X 1 ( 2 ) ) Var ⁡ ( X 1 ( 3 ) ) ⋯ Cov ⁡ ( X 1 ( 3 ) , X 1 ( k ) ) ⋮ ⋮ ⋮ ⋱ ⋮ Cov ⁡ ( X 1 ( k ) , X 1 ( 1 ) ) Cov ⁡ ( X 1 ( k ) , X 1 ( 2 ) ) Cov ⁡ ( X 1 ( k ) , X 1 ( 3 ) ) ⋯ Var ⁡ ( X 1 ( k ) ) ]   . {\displaystyle {\boldsymbol {\Sigma }}={\begin{bmatrix}{\operatorname {Var} \left(X_{1}^{(1)}\right)}&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(1)}\right)&\operatorname {Var} \left(X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(2)}\right)&\operatorname {Var} \left(X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(k)}\right)\\\vdots &\vdots &\vdots &\ddots &\vdots \\\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(3)}\right)&\cdots &\operatorname {Var} \left(X_{1}^{(k)}\right)\\\end{bmatrix}}~.} ({\displaystyle {\boldsymbol {\Sigma }}={\begin{bmatrix}{\operatorname {Var} \left(X_{1}^{(1)}\right)}&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(1)}\right)&\operatorname {Var} \left(X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(2)}\right)&\operatorname {Var} \left(X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(k)}\right)\\\vdots &\vdots &\vdots &\ddots &\vdots \\\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(3)}\right)&\cdots &\operatorname {Var} \left(X_{1}^{(k)}\right)\\\end{bmatrix}}~.})

The multivariate central limit theorem can be proved using the Cramér–Wold theorem.

The rate of convergence is given by the following Berry–Esseen type result:

**Theorem**—Let X 1 , … , X n , … {\displaystyle X_{1},\dots ,X_{n},\dots } ({\displaystyle X_{1},\dots ,X_{n},\dots }) be independent R d {\displaystyle \mathbb {R} ^{d}} ({\displaystyle \mathbb {R} ^{d}})-valued random vectors, each having mean zero. Write S = ∑ i = 1 n X i {\displaystyle S=\sum _{i=1}^{n}X_{i}} ({\displaystyle S=\sum _{i=1}^{n}X_{i}}) and assume Σ = Cov ⁡ [ S ] {\displaystyle \Sigma =\operatorname {Cov} [S]} ({\displaystyle \Sigma =\operatorname {Cov} [S]}) is invertible. Let Z ∼ N ( 0 , Σ ) {\displaystyle Z\sim {\mathcal {N}}(0,\Sigma )} ({\displaystyle Z\sim {\mathcal {N}}(0,\Sigma )}) be a d {\displaystyle d} ({\displaystyle d})-dimensional Gaussian with the same mean and same covariance matrix as S {\displaystyle S} ({\displaystyle S}). Then for all convex sets U ⊆ R d {\displaystyle U\subseteq \mathbb {R} ^{d}} ({\displaystyle U\subseteq \mathbb {R} ^{d}}),

| P [ S ∈ U ] − P [ Z ∈ U ] | ≤ C d 1 / 4 γ   , {\displaystyle \left|\mathbb {P} [S\in U]-\mathbb {P} [Z\in U]\right|\leq C\,d^{1/4}\gamma ~,} ({\displaystyle \left|\mathbb {P} [S\in U]-\mathbb {P} [Z\in U]\right|\leq C\,d^{1/4}\gamma ~,}) where C {\displaystyle C} ({\displaystyle C}) is a universal constant, γ = ∑ i = 1 n E ⁡ [ ‖ Σ − 1 / 2 X i ‖ 2 3 ] {\displaystyle \gamma =\sum _{i=1}^{n}\operatorname {E} \left[\left\|\Sigma ^{-1/2}X_{i}\right\|_{2}^{3}\right]} ({\displaystyle \gamma =\sum _{i=1}^{n}\operatorname {E} \left[\left\|\Sigma ^{-1/2}X_{i}\right\|_{2}^{3}\right]}), and ‖ ⋅ ‖ 2 {\displaystyle \|\cdot \|_{2}} ({\displaystyle \|\cdot \|_{2}}) denotes the Euclidean norm on R d {\displaystyle \mathbb {R} ^{d}} ({\displaystyle \mathbb {R} ^{d}}).

It is unknown whether the factor d 1 / 4 {\textstyle d^{1/4}} ({\textstyle d^{1/4}}) is necessary.


## The generalized central limit theorem

The generalized central limit theorem (GCLT) was an effort of multiple mathematicians (Sergei Bernstein, Jarl Waldemar Lindeberg, Paul Lévy, William Feller, Andrey Kolmogorov, and others) over the period from 1920 to 1937. The first published complete proof of the GCLT was in 1937 by Paul Lévy in French. An English language version of the complete proof of the GCLT is available in the translation of Boris Vladimirovich Gnedenko and Kolmogorov's 1954 book.

The statement of the GCLT is as follows:

**Statement of GCLT**—A non-degenerate random variable Z is α-stable for some 0 < *α* ≤ 2 if and only if there is an independent, identically distributed sequence of random variables *X*1, *X*2, *X*3, ..., and constants *a**n* > 0, *b**n* ∈ ℝ with a n ( X 1 + ⋯ + X n ) − b n → Z . {\displaystyle a_{n}(X_{1}+\dots +X_{n})-b_{n}\to Z.} ({\displaystyle a_{n}(X_{1}+\dots +X_{n})-b_{n}\to Z.}) Here, '→' means the sequence of random variable sums converges in distribution; i.e., the corresponding distributions satisfy *F**n*(*y*) → *F*(*y*) at all continuity points of F.

In other words, if sums of independent, identically distributed random variables converge in distribution to some Z, then Z must be a stable distribution.


## Dependent processes

### CLT under weak dependence

A useful generalization of a sequence of independent, identically distributed random variables is a mixing random process in discrete time; "mixing" means, roughly, that random variables temporally far apart from one another are nearly independent. Several kinds of mixing are used in ergodic theory and probability theory. See especially strong mixing (also called α-mixing) defined by α ( n ) → 0 {\textstyle \alpha (n)\to 0} ({\textstyle \alpha (n)\to 0}) where α ( n ) {\textstyle \alpha (n)} ({\textstyle \alpha (n)}) is so-called strong mixing coefficient.

A simplified formulation of the central limit theorem under strong mixing is:

**Theorem**—Suppose that { X 1 , … , X n , … } {\textstyle \{X_{1},\ldots ,X_{n},\ldots \}} ({\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}) is stationary and α {\displaystyle \alpha } ({\displaystyle \alpha })-mixing with α n = O ( n − 5 ) {\textstyle \alpha _{n}=O\left(n^{-5}\right)} ({\textstyle \alpha _{n}=O\left(n^{-5}\right)}) and that E ⁡ [ X n ] = 0 {\textstyle \operatorname {E} [X_{n}]=0} ({\textstyle \operatorname {E} [X_{n}]=0}) and E ⁡ [ X n 12 ] < ∞ {\textstyle \operatorname {E} [X_{n}^{12}]<\infty } ({\textstyle \operatorname {E} [X_{n}^{12}]<\infty }). Denote S n = X 1 + ⋯ + X n {\textstyle S_{n}=X_{1}+\cdots +X_{n}} ({\textstyle S_{n}=X_{1}+\cdots +X_{n}}), then the limit

σ 2 = lim n → ∞ E ⁡ ( S n 2 ) n {\displaystyle \sigma ^{2}=\lim _{n\rightarrow \infty }{\frac {\operatorname {E} \left(S_{n}^{2}\right)}{n}}} ({\displaystyle \sigma ^{2}=\lim _{n\rightarrow \infty }{\frac {\operatorname {E} \left(S_{n}^{2}\right)}{n}}})

exists, and if σ ≠ 0 {\textstyle \sigma \neq 0} ({\textstyle \sigma \neq 0}) then S n σ n {\textstyle {\frac {S_{n}}{\sigma {\sqrt {n}}}}} ({\textstyle {\frac {S_{n}}{\sigma {\sqrt {n}}}}}) converges in distribution to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}).

In fact,

σ 2 = E ⁡ ( X 1 2 ) + 2 ∑ k = 1 ∞ E ⁡ ( X 1 X 1 + k ) , {\displaystyle \sigma ^{2}=\operatorname {E} \left(X_{1}^{2}\right)+2\sum _{k=1}^{\infty }\operatorname {E} \left(X_{1}X_{1+k}\right),} ({\displaystyle \sigma ^{2}=\operatorname {E} \left(X_{1}^{2}\right)+2\sum _{k=1}^{\infty }\operatorname {E} \left(X_{1}X_{1+k}\right),})

where the series converges absolutely.

The assumption σ ≠ 0 {\textstyle \sigma \neq 0} ({\textstyle \sigma \neq 0}) cannot be omitted, since the asymptotic normality fails for X n = Y n − Y n − 1 {\textstyle X_{n}=Y_{n}-Y_{n-1}} ({\textstyle X_{n}=Y_{n}-Y_{n-1}}) where Y n {\textstyle Y_{n}} ({\textstyle Y_{n}}) are another stationary sequence.

There is a stronger version of the theorem: the assumption E ⁡ [ X n 12 ] < ∞ {\textstyle \operatorname {E} \left[X_{n}^{12}\right]<\infty } ({\textstyle \operatorname {E} \left[X_{n}^{12}\right]<\infty }) is replaced with E ⁡ [ | X n | 2 + δ ] < ∞ {\textstyle \operatorname {E} \left[{\left|X_{n}\right|}^{2+\delta }\right]<\infty } ({\textstyle \operatorname {E} \left[{\left|X_{n}\right|}^{2+\delta }\right]<\infty }), and the assumption α n = O ( n − 5 ) {\textstyle \alpha _{n}=O\left(n^{-5}\right)} ({\textstyle \alpha _{n}=O\left(n^{-5}\right)}) is replaced with

∑ n α n δ 2 ( 2 + δ ) < ∞ . {\displaystyle \sum _{n}\alpha _{n}^{\frac {\delta }{2(2+\delta )}}<\infty .} ({\displaystyle \sum _{n}\alpha _{n}^{\frac {\delta }{2(2+\delta )}}<\infty .})

Existence of such δ > 0 {\textstyle \delta >0} ({\textstyle \delta >0}) ensures the conclusion. For encyclopedic treatment of limit theorems under mixing conditions see (Bradley 2007).

### Martingale difference CLT

**Theorem**—Let a martingale M n {\textstyle M_{n}} ({\textstyle M_{n}}) satisfy

- 1 n ∑ k = 1 n E ⁡ [ ( M k − M k − 1 ) 2 ∣ M 1 , … , M k − 1 ] → 1 {\displaystyle {\frac {1}{n}}\sum _{k=1}^{n}\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mid M_{1},\dots ,M_{k-1}\right]\to 1} ({\displaystyle {\frac {1}{n}}\sum _{k=1}^{n}\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mid M_{1},\dots ,M_{k-1}\right]\to 1}) in probability as *n* → ∞,
- for every *ε* > 0, 1 n ∑ k = 1 n E ⁡ [ ( M k − M k − 1 ) 2 1 [ | M k − M k − 1 | > ε n ] ] → 0 {\displaystyle {\frac {1}{n}}\sum _{k=1}^{n}{\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mathbf {1} \left[|M_{k}-M_{k-1}|>\varepsilon {\sqrt {n}}\right]\right]}\to 0} ({\displaystyle {\frac {1}{n}}\sum _{k=1}^{n}{\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mathbf {1} \left[|M_{k}-M_{k-1}|>\varepsilon {\sqrt {n}}\right]\right]}\to 0}) as *n* → ∞,

then M n n {\textstyle {\frac {M_{n}}{\sqrt {n}}}} ({\textstyle {\frac {M_{n}}{\sqrt {n}}}}) converges in distribution to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) as n → ∞ {\textstyle n\to \infty } ({\textstyle n\to \infty }).


## Remarks

### Proof of classical CLT

The central limit theorem has a proof using characteristic functions. It is similar to the proof of the (weak) law of large numbers.

Assume { X 1 , … , X n , … } {\textstyle \{X_{1},\ldots ,X_{n},\ldots \}} ({\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}) are independent and identically distributed random variables, each with mean μ {\textstyle \mu } ({\textstyle \mu }) and finite variance σ 2 {\textstyle \sigma ^{2}} ({\textstyle \sigma ^{2}}). The sum X 1 + ⋯ + X n {\textstyle X_{1}+\cdots +X_{n}} ({\textstyle X_{1}+\cdots +X_{n}}) has mean n μ {\textstyle n\mu } ({\textstyle n\mu }) and variance n σ 2 {\textstyle n\sigma ^{2}} ({\textstyle n\sigma ^{2}}). Consider the random variable

Z n = X 1 + ⋯ + X n − n μ n σ 2 = ∑ i = 1 n X i − μ n σ 2 =: ∑ i = 1 n 1 n Y i , {\displaystyle Z_{n}={\frac {X_{1}+\cdots +X_{n}-n\mu }{\sqrt {n\sigma ^{2}}}}=\sum _{i=1}^{n}{\frac {X_{i}-\mu }{\sqrt {n\sigma ^{2}}}}=:\sum _{i=1}^{n}{\frac {1}{\sqrt {n}}}Y_{i},} ({\displaystyle Z_{n}={\frac {X_{1}+\cdots +X_{n}-n\mu }{\sqrt {n\sigma ^{2}}}}=\sum _{i=1}^{n}{\frac {X_{i}-\mu }{\sqrt {n\sigma ^{2}}}}=:\sum _{i=1}^{n}{\frac {1}{\sqrt {n}}}Y_{i},})

where the last step defines the new random variables Y i := X i − μ σ {\textstyle Y_{i}:={\frac {X_{i}-\mu }{\sigma }}} ({\textstyle Y_{i}:={\frac {X_{i}-\mu }{\sigma }}}), each with zero mean and unit variance ( var ⁡ ( Y ) = 1 {\textstyle \operatorname {var} (Y)=1} ({\textstyle \operatorname {var} (Y)=1})). The characteristic function of Z n {\textstyle Z_{n}} ({\textstyle Z_{n}}) is given by

φ Z n ( t ) = φ ∑ i = 1 n 1 n Y i ( t )   =   φ Y 1 ( t n ) φ Y 2 ( t n ) ⋯ φ Y n ( t n ) =   [ φ Y 1 ( t n ) ] n , {\displaystyle {\begin{aligned}\varphi _{Z_{n}}\!(t)=\varphi _{\sum _{i=1}^{n}{{\frac {1}{\sqrt {n}}}Y_{i}}}\!(t)\ &=\ \varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\varphi _{Y_{2}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\cdots \varphi _{Y_{n}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\\[1ex]&=\ \left[\varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\right]^{n},\end{aligned}}} ({\displaystyle {\begin{aligned}\varphi _{Z_{n}}\!(t)=\varphi _{\sum _{i=1}^{n}{{\frac {1}{\sqrt {n}}}Y_{i}}}\!(t)\ &=\ \varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\varphi _{Y_{2}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\cdots \varphi _{Y_{n}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\\[1ex]&=\ \left[\varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\right]^{n},\end{aligned}}})

where the last step relies on the fact that all of the Y i {\textstyle Y_{i}} ({\textstyle Y_{i}}) are identically distributed. The characteristic function of Y 1 {\textstyle Y_{1}} ({\textstyle Y_{1}}) is, by Taylor's theorem, φ Y 1 ( t n ) = 1 − t 2 2 n + o ( t 2 n ) , ( t n ) → 0 {\displaystyle \varphi _{Y_{1}}\!\left({\frac {t}{\sqrt {n}}}\right)=1-{\frac {t^{2}}{2n}}+o\!\left({\frac {t^{2}}{n}}\right),\quad \left({\frac {t}{\sqrt {n}}}\right)\to 0} ({\displaystyle \varphi _{Y_{1}}\!\left({\frac {t}{\sqrt {n}}}\right)=1-{\frac {t^{2}}{2n}}+o\!\left({\frac {t^{2}}{n}}\right),\quad \left({\frac {t}{\sqrt {n}}}\right)\to 0})

where o ( t 2 / n ) {\textstyle o(t^{2}/n)} ({\textstyle o(t^{2}/n)}) is "little o notation" for some function of t {\textstyle t} ({\textstyle t}) that goes to zero more rapidly than t 2 / n {\textstyle t^{2}/n} ({\textstyle t^{2}/n}). By the limit of the exponential function ( e x = lim n → ∞ ( 1 + x n ) n {\textstyle e^{x}=\lim _{n\to \infty }\left(1+{\frac {x}{n}}\right)^{n}} ({\textstyle e^{x}=\lim _{n\to \infty }\left(1+{\frac {x}{n}}\right)^{n}})), the characteristic function of Z n {\displaystyle Z_{n}} ({\displaystyle Z_{n}}) equals

φ Z n ( t ) = ( 1 − t 2 2 n + o ( t 2 n ) ) n → e − 1 2 t 2 , n → ∞ . {\displaystyle \varphi _{Z_{n}}(t)=\left(1-{\frac {t^{2}}{2n}}+o\left({\frac {t^{2}}{n}}\right)\right)^{n}\rightarrow e^{-{\frac {1}{2}}t^{2}},\quad n\to \infty .} ({\displaystyle \varphi _{Z_{n}}(t)=\left(1-{\frac {t^{2}}{2n}}+o\left({\frac {t^{2}}{n}}\right)\right)^{n}\rightarrow e^{-{\frac {1}{2}}t^{2}},\quad n\to \infty .})

All of the higher order terms vanish in the limit n → ∞ {\textstyle n\to \infty } ({\textstyle n\to \infty }). The right hand side equals the characteristic function of a standard normal distribution N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}), which implies through Lévy's continuity theorem that the distribution of Z n {\textstyle Z_{n}} ({\textstyle Z_{n}}) will approach N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) as n → ∞ {\textstyle n\to \infty } ({\textstyle n\to \infty }). Therefore, the sample average

X ¯ n = X 1 + ⋯ + X n n {\displaystyle {\bar {X}}_{n}={\frac {X_{1}+\cdots +X_{n}}{n}}} ({\displaystyle {\bar {X}}_{n}={\frac {X_{1}+\cdots +X_{n}}{n}}})

is such that

n σ ( X ¯ n − μ ) = Z n {\displaystyle {\frac {\sqrt {n}}{\sigma }}\left({\bar {X}}_{n}-\mu \right)=Z_{n}} ({\displaystyle {\frac {\sqrt {n}}{\sigma }}\left({\bar {X}}_{n}-\mu \right)=Z_{n}})

converges to the normal distribution N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}), from which the central limit theorem follows.

### Convergence to the limit

The central limit theorem gives only an asymptotic distribution. As an approximation for a finite number of observations, it provides a reasonable approximation only when close to the peak of the normal distribution; it requires a very large number of observations to stretch into the tails.

The convergence in the central limit theorem is uniform because the limiting cumulative distribution function is continuous. If the third central moment E ⁡ [ ( X 1 − μ ) 3 ] {\textstyle \operatorname {E} \left[(X_{1}-\mu )^{3}\right]} ({\textstyle \operatorname {E} \left[(X_{1}-\mu )^{3}\right]}) exists and is finite, then the speed of convergence is at least on the order of 1 / n {\textstyle 1/{\sqrt {n}}} ({\textstyle 1/{\sqrt {n}}}) (see Berry–Esseen theorem). Stein's method can be used not only to prove the central limit theorem, but also to provide bounds on the rates of convergence for selected metrics.

The convergence to the normal distribution is monotonic, in the sense that the entropy of Z n {\textstyle Z_{n}} ({\textstyle Z_{n}}) increases monotonically to that of the normal distribution.

The central limit theorem applies in particular to sums of independent and identically distributed discrete random variables. A sum of discrete random variables is still a discrete random variable, so that we are confronted with a sequence of discrete random variables whose cumulative probability distribution function converges towards a cumulative probability distribution function corresponding to a continuous variable (namely that of the normal distribution). This means that if we build a histogram of the realizations of the sum of n independent identical discrete variables, the piecewise-linear curve that joins the centers of the upper faces of the rectangles forming the histogram converges toward a Gaussian curve as n approaches infinity; this relation is known as de Moivre–Laplace theorem. The binomial distribution article details such an application of the central limit theorem in the simple case of a discrete variable taking only two possible values.

### Common misconceptions

Studies have shown that the central limit theorem is subject to several common but serious misconceptions, some of which appear in widely used textbooks. These include:

- The misconceived belief that the theorem applies to random sampling of any variable, rather than to the mean values (or sums) of iid random variables extracted from a population by repeated sampling. That is, the theorem assumes the random sampling produces a sampling distribution formed from different values of means (or sums) of such random variables.
- The misconceived belief that the theorem ensures that random sampling leads to the emergence of a normal distribution for sufficiently large samples of any random variable, regardless of the population distribution. In reality, such sampling asymptotically reproduces the properties of the population, an intuitive result underpinned by the Glivenko–Cantelli theorem.
- The misconceived belief that the theorem leads to a good approximation of a normal distribution for sample sizes greater than around 30, allowing reliable inferences regardless of the nature of the population. In reality, this empirical rule of thumb has no valid justification, and can lead to seriously flawed inferences. See Z-test for where the approximation holds.

### Relation to the law of large numbers

The law of large numbers as well as the central limit theorem are partial solutions to a general problem: "What is the limiting behavior of Sn as n approaches infinity?" In mathematical analysis, asymptotic series are one of the most popular tools employed to approach such questions.

Suppose we have an asymptotic expansion of f ( n ) {\textstyle f(n)} ({\textstyle f(n)}):

f ( n ) = a 1 φ 1 ( n ) + a 2 φ 2 ( n ) + O ( φ 3 ( n ) ) ( n → ∞ ) . {\displaystyle f(n)=a_{1}\varphi _{1}(n)+a_{2}\varphi _{2}(n)+O{\big (}\varphi _{3}(n){\big )}\qquad (n\to \infty ).} ({\displaystyle f(n)=a_{1}\varphi _{1}(n)+a_{2}\varphi _{2}(n)+O{\big (}\varphi _{3}(n){\big )}\qquad (n\to \infty ).})

Dividing both parts by *φ*1(*n*) and taking the limit will produce *a*1, the coefficient of the highest-order term in the expansion, which represents the rate at which *f*(*n*) changes in its leading term.

lim n → ∞ f ( n ) φ 1 ( n ) = a 1 . {\displaystyle \lim _{n\to \infty }{\frac {f(n)}{\varphi _{1}(n)}}=a_{1}.} ({\displaystyle \lim _{n\to \infty }{\frac {f(n)}{\varphi _{1}(n)}}=a_{1}.})

Informally, one can say: "*f*(*n*) grows approximately as *a*1*φ*1(*n*)". Taking the difference between *f*(*n*) and its approximation and then dividing by the next term in the expansion, we arrive at a more refined statement about *f*(*n*):

lim n → ∞ f ( n ) − a 1 φ 1 ( n ) φ 2 ( n ) = a 2 . {\displaystyle \lim _{n\to \infty }{\frac {f(n)-a_{1}\varphi _{1}(n)}{\varphi _{2}(n)}}=a_{2}.} ({\displaystyle \lim _{n\to \infty }{\frac {f(n)-a_{1}\varphi _{1}(n)}{\varphi _{2}(n)}}=a_{2}.})

Here one can say that the difference between the function and its approximation grows approximately as *a*2*φ*2(*n*). The idea is that dividing the function by appropriate normalizing functions, and looking at the limiting behavior of the result, can tell us much about the limiting behavior of the original function itself.

Informally, something along these lines happens when the sum, Sn, of independent identically distributed random variables, *X*1, ..., *Xn*, is studied in classical probability theory. If each Xi has finite mean μ, then by the law of large numbers, ⁠*Sn*/*n*⁠ → *μ*. If in addition each Xi has finite variance *σ*2, then by the central limit theorem,

S n − n μ n → ξ , {\displaystyle {\frac {S_{n}-n\mu }{\sqrt {n}}}\to \xi ,} ({\displaystyle {\frac {S_{n}-n\mu }{\sqrt {n}}}\to \xi ,})

where ξ is distributed as *N*(0,*σ*2). This provides values of the first two constants in the informal expansion

S n ≈ μ n + ξ n . {\displaystyle S_{n}\approx \mu n+\xi {\sqrt {n}}.} ({\displaystyle S_{n}\approx \mu n+\xi {\sqrt {n}}.})

In the case where the Xi do not have finite mean or variance, convergence of the shifted and rescaled sum can also occur with different centering and scaling factors:

S n − a n b n → Ξ , {\displaystyle {\frac {S_{n}-a_{n}}{b_{n}}}\rightarrow \Xi ,} ({\displaystyle {\frac {S_{n}-a_{n}}{b_{n}}}\rightarrow \Xi ,})

or informally

S n ≈ a n + Ξ b n . {\displaystyle S_{n}\approx a_{n}+\Xi b_{n}.} ({\displaystyle S_{n}\approx a_{n}+\Xi b_{n}.})

Distributions Ξ which can arise in this way are called *stable*. Clearly, the normal distribution is stable, but there are also other stable distributions, such as the Cauchy distribution, for which the mean or variance are not defined. The scaling factor bn may be proportional to nc, for any *c* ≥ ⁠1/2⁠; it may also be multiplied by a slowly varying function of n.

The law of the iterated logarithm specifies what is happening "in between" the law of large numbers and the central limit theorem. Specifically it says that the normalizing function √*n* log log *n*, intermediate in size between n of the law of large numbers and √*n* of the central limit theorem, provides a non-trivial limiting behavior.

### Alternative statements of the theorem

#### Density functions

The density of the sum of two or more independent variables is the convolution of their densities (if these densities exist). Thus the central limit theorem can be interpreted as a statement about the properties of density functions under convolution: the convolution of a number of density functions tends to the normal density as the number of density functions increases without bound. These theorems require stronger hypotheses than the forms of the central limit theorem given above. Theorems of this type are often called local limit theorems. See Petrov for a particular local limit theorem for sums of independent and identically distributed random variables.

#### Characteristic functions

Since the characteristic function of a convolution is the product of the characteristic functions of the densities involved, the central limit theorem has yet another restatement: the product of the characteristic functions of a number of density functions becomes close to the characteristic function of the normal density as the number of density functions increases without bound, under the conditions stated above. Specifically, an appropriate scaling factor needs to be applied to the argument of the characteristic function.

An equivalent statement can be made about Fourier transforms, since the characteristic function is essentially a Fourier transform.

### Calculating the variance

Let Sn be the sum of n random variables. Many central limit theorems provide conditions such that Sn/√Var(Sn) converges in distribution to *N*(0,1) (the normal distribution with mean 0, variance 1) as n → ∞. In some cases, it is possible to find a constant *σ*2 and function f(n) such that Sn/(σ√n⋅f(n)) converges in distribution to *N*(0,1) as n→ ∞.

**Lemma**—Suppose X 1 , X 2 , … {\displaystyle X_{1},X_{2},\dots } ({\displaystyle X_{1},X_{2},\dots }) is a sequence of real-valued and strictly stationary random variables with E ⁡ ( X i ) = 0 {\displaystyle \operatorname {E} (X_{i})=0} ({\displaystyle \operatorname {E} (X_{i})=0}) for all i {\displaystyle i} ({\displaystyle i}), g : [ 0 , 1 ] → R {\displaystyle g:[0,1]\to \mathbb {R} } ({\displaystyle g:[0,1]\to \mathbb {R} }), and S n = ∑ i = 1 n g ( i n ) X i {\displaystyle S_{n}=\sum _{i=1}^{n}g\left({\tfrac {i}{n}}\right)X_{i}} ({\displaystyle S_{n}=\sum _{i=1}^{n}g\left({\tfrac {i}{n}}\right)X_{i}}). Construct

σ 2 = E ⁡ ( X 1 2 ) + 2 ∑ i = 1 ∞ E ⁡ ( X 1 X 1 + i ) {\displaystyle \sigma ^{2}=\operatorname {E} (X_{1}^{2})+2\sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})} ({\displaystyle \sigma ^{2}=\operatorname {E} (X_{1}^{2})+2\sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})})

1. If ∑ i = 1 ∞ E ⁡ ( X 1 X 1 + i ) {\displaystyle \sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})} ({\displaystyle \sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})}) is absolutely convergent, | ∫ 0 1 g ( x ) g ′ ( x ) d x | < ∞ {\displaystyle \left|\int _{0}^{1}g(x)g'(x)\,dx\right|<\infty } ({\displaystyle \left|\int _{0}^{1}g(x)g'(x)\,dx\right|<\infty }), and 0 < ∫ 0 1 ( g ( x ) ) 2 d x < ∞ {\displaystyle 0<\int _{0}^{1}(g(x))^{2}dx<\infty } ({\displaystyle 0<\int _{0}^{1}(g(x))^{2}dx<\infty }) then V a r ( S n ) / ( n γ n ) → σ 2 {\displaystyle \mathrm {Var} (S_{n})/(n\gamma _{n})\to \sigma ^{2}} ({\displaystyle \mathrm {Var} (S_{n})/(n\gamma _{n})\to \sigma ^{2}}) as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }) where γ n = 1 n ∑ i = 1 n ( g ( i n ) ) 2 {\displaystyle \gamma _{n}={\frac {1}{n}}\sum _{i=1}^{n}\left(g\left({\tfrac {i}{n}}\right)\right)^{2}} ({\displaystyle \gamma _{n}={\frac {1}{n}}\sum _{i=1}^{n}\left(g\left({\tfrac {i}{n}}\right)\right)^{2}}).
2. If in addition σ > 0 {\displaystyle \sigma >0} ({\displaystyle \sigma >0}) and S n / V a r ( S n ) {\displaystyle S_{n}/{\sqrt {\mathrm {Var} (S_{n})}}} ({\displaystyle S_{n}/{\sqrt {\mathrm {Var} (S_{n})}}}) converges in distribution to N ( 0 , 1 ) {\displaystyle {\mathcal {N}}(0,1)} ({\displaystyle {\mathcal {N}}(0,1)}) as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }) then S n / ( σ n γ n ) {\displaystyle S_{n}/(\sigma {\sqrt {n\gamma _{n}}})} ({\displaystyle S_{n}/(\sigma {\sqrt {n\gamma _{n}}})}) also converges in distribution to N ( 0 , 1 ) {\displaystyle {\mathcal {N}}(0,1)} ({\displaystyle {\mathcal {N}}(0,1)}) as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }).


## Extensions

### Products of positive random variables

The logarithm of a product is simply the sum of the logarithms of the factors. Therefore, when the logarithm of a product of random variables that take only positive values approaches a normal distribution, the product itself approaches a log-normal distribution. Many physical quantities (especially mass or length, which are a matter of scale and cannot be negative) are the products of different random factors, so they follow a log-normal distribution. This multiplicative version of the central limit theorem is sometimes called Gibrat's law.

Whereas the central limit theorem for sums of random variables requires the condition of finite variance, the corresponding theorem for products requires the corresponding condition that the density function be square-integrable.
