---
title: "Entropy (information theory) (part 2/2)"
source: https://en.wikipedia.org/wiki/Entropy_(information_theory)
domain: information-theory
license: CC-BY-SA-4.0
tags: information theory, shannon entropy, channel capacity, error correction, hamming code
fetched: 2026-07-02
part: 2/2
---

## Efficiency (normalized entropy)

A source set X {\displaystyle {\mathcal {X}}} ({\displaystyle {\mathcal {X}}}) with a non-uniform distribution will have less entropy than the same set with a uniform distribution (i.e. the "optimized alphabet"). This deficiency in entropy can be expressed as a ratio called efficiency:

η ( X ) = H H max = − ∑ i = 1 n p ( x i ) log b ⁡ ( p ( x i ) ) log b ⁡ ( n ) . {\displaystyle \eta (X)={\frac {H}{H_{\text{max}}}}=-\sum _{i=1}^{n}{\frac {p(x_{i})\log _{b}(p(x_{i}))}{\log _{b}(n)}}.} ({\displaystyle \eta (X)={\frac {H}{H_{\text{max}}}}=-\sum _{i=1}^{n}{\frac {p(x_{i})\log _{b}(p(x_{i}))}{\log _{b}(n)}}.}) Applying the basic properties of the logarithm, this quantity can also be expressed as: η ( X ) = − ∑ i = 1 n p ( x i ) log b ⁡ ( p ( x i ) ) log b ⁡ ( n ) = ∑ i = 1 n log b ⁡ ( p ( x i ) − p ( x i ) ) log b ⁡ ( n ) = ∑ i = 1 n log n ⁡ ( p ( x i ) − p ( x i ) ) = log n ⁡ ( ∏ i = 1 n p ( x i ) − p ( x i ) ) . {\displaystyle {\begin{aligned}\eta (X)&=-\sum _{i=1}^{n}{\frac {p(x_{i})\log _{b}(p(x_{i}))}{\log _{b}(n)}}=\sum _{i=1}^{n}{\frac {\log _{b}\left(p(x_{i})^{-p(x_{i})}\right)}{\log _{b}(n)}}\\[1ex]&=\sum _{i=1}^{n}\log _{n}\left(p(x_{i})^{-p(x_{i})}\right)=\log _{n}\left(\prod _{i=1}^{n}p(x_{i})^{-p(x_{i})}\right).\end{aligned}}} ({\displaystyle {\begin{aligned}\eta (X)&=-\sum _{i=1}^{n}{\frac {p(x_{i})\log _{b}(p(x_{i}))}{\log _{b}(n)}}=\sum _{i=1}^{n}{\frac {\log _{b}\left(p(x_{i})^{-p(x_{i})}\right)}{\log _{b}(n)}}\\[1ex]&=\sum _{i=1}^{n}\log _{n}\left(p(x_{i})^{-p(x_{i})}\right)=\log _{n}\left(\prod _{i=1}^{n}p(x_{i})^{-p(x_{i})}\right).\end{aligned}}})

Efficiency has utility in quantifying the effective use of a communication channel. This formulation is also referred to as the normalized entropy, as the entropy is divided by the maximum entropy log b ⁡ ( n ) {\displaystyle {\log _{b}(n)}} ({\displaystyle {\log _{b}(n)}}). Furthermore, the efficiency is indifferent to the choice of (positive) base *b*, as indicated by the insensitivity within the final logarithm above thereto.


## Entropy for continuous random variables

### Differential entropy

The Shannon entropy is restricted to random variables taking discrete values. The corresponding formula for a continuous random variable with probability density function *f*(*x*) with finite or infinite support X {\displaystyle \mathbb {X} } ({\displaystyle \mathbb {X} }) on the real line is defined by analogy, using the above form of the entropy as an expectation:

H ( X ) = E [ − log ⁡ f ( X ) ] = − ∫ X f ( x ) log ⁡ f ( x ) d x . {\displaystyle \mathrm {H} (X)=\mathbb {E} [-\log f(X)]=-\int _{\mathbb {X} }f(x)\log f(x)\,\mathrm {d} x.} ({\displaystyle \mathrm {H} (X)=\mathbb {E} [-\log f(X)]=-\int _{\mathbb {X} }f(x)\log f(x)\,\mathrm {d} x.})

This is the differential entropy (or continuous entropy). A precursor of the continuous entropy *h*[*f*] is the expression for the functional *Η* in the H-theorem of Boltzmann.

Although the analogy between both functions is suggestive, the following question must be set: is the differential entropy a valid extension of the Shannon discrete entropy? Differential entropy lacks a number of properties that the Shannon discrete entropy has – it can even be negative – and corrections have been suggested, notably limiting density of discrete points.

To answer this question, a connection must be established between the two functions:

In order to obtain a generally finite measure as the bin size goes to zero. In the discrete case, the bin size is the (implicit) width of each of the *n* (finite or infinite) bins whose probabilities are denoted by *p**n*. As the continuous domain is generalized, the width must be made explicit.

To do this, start with a continuous function *f* discretized into bins of size Δ {\displaystyle \Delta } ({\displaystyle \Delta }). By the mean-value theorem there exists a value *x**i* in each bin such that f ( x i ) Δ = ∫ i Δ ( i + 1 ) Δ f ( x ) d x {\displaystyle f(x_{i})\Delta =\int _{i\Delta }^{(i+1)\Delta }f(x)\,dx} ({\displaystyle f(x_{i})\Delta =\int _{i\Delta }^{(i+1)\Delta }f(x)\,dx}) the integral of the function *f* can be approximated (in the Riemannian sense) by ∫ − ∞ ∞ f ( x ) d x = lim Δ → 0 ∑ i = − ∞ ∞ f ( x i ) Δ , {\displaystyle \int _{-\infty }^{\infty }f(x)\,dx=\lim _{\Delta \to 0}\sum _{i=-\infty }^{\infty }f(x_{i})\Delta ,} ({\displaystyle \int _{-\infty }^{\infty }f(x)\,dx=\lim _{\Delta \to 0}\sum _{i=-\infty }^{\infty }f(x_{i})\Delta ,}) where this limit and "bin size goes to zero" are equivalent.

We will denote H Δ := − ∑ i = − ∞ ∞ f ( x i ) Δ log ⁡ ( f ( x i ) Δ ) {\displaystyle \mathrm {H} ^{\Delta }:=-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log \left(f(x_{i})\Delta \right)} ({\displaystyle \mathrm {H} ^{\Delta }:=-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log \left(f(x_{i})\Delta \right)}) and expanding the logarithm, we have H Δ = − ∑ i = − ∞ ∞ f ( x i ) Δ log ⁡ ( f ( x i ) ) − ∑ i = − ∞ ∞ f ( x i ) Δ log ⁡ ( Δ ) . {\displaystyle \mathrm {H} ^{\Delta }=-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(f(x_{i}))-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(\Delta ).} ({\displaystyle \mathrm {H} ^{\Delta }=-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(f(x_{i}))-\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(\Delta ).})

As Δ → 0, we have

∑ i = − ∞ ∞ f ( x i ) Δ → ∫ − ∞ ∞ f ( x ) d x = 1 ∑ i = − ∞ ∞ f ( x i ) Δ log ⁡ ( f ( x i ) ) → ∫ − ∞ ∞ f ( x ) log ⁡ f ( x ) d x . {\displaystyle {\begin{aligned}\sum _{i=-\infty }^{\infty }f(x_{i})\Delta &\to \int _{-\infty }^{\infty }f(x)\,dx=1\\\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(f(x_{i}))&\to \int _{-\infty }^{\infty }f(x)\log f(x)\,dx.\end{aligned}}} ({\displaystyle {\begin{aligned}\sum _{i=-\infty }^{\infty }f(x_{i})\Delta &\to \int _{-\infty }^{\infty }f(x)\,dx=1\\\sum _{i=-\infty }^{\infty }f(x_{i})\Delta \log(f(x_{i}))&\to \int _{-\infty }^{\infty }f(x)\log f(x)\,dx.\end{aligned}}})

Note; log(Δ) → −∞ as Δ → 0, requires a special definition of the differential or continuous entropy:

h [ f ] = lim Δ → 0 ( H Δ + log ⁡ Δ ) = − ∫ − ∞ ∞ f ( x ) log ⁡ f ( x ) d x , {\displaystyle h[f]=\lim _{\Delta \to 0}\left(\mathrm {H} ^{\Delta }+\log \Delta \right)=-\int _{-\infty }^{\infty }f(x)\log f(x)\,dx,} ({\displaystyle h[f]=\lim _{\Delta \to 0}\left(\mathrm {H} ^{\Delta }+\log \Delta \right)=-\int _{-\infty }^{\infty }f(x)\log f(x)\,dx,})

which is, as said before, referred to as the differential entropy. This means that the differential entropy *is not* a limit of the Shannon entropy for *n* → ∞. Rather, it differs from the limit of the Shannon entropy by an infinite offset (see also the article on information dimension).

### Limiting density of discrete points

It turns out as a result that, unlike the Shannon entropy, the differential entropy is *not* in general a good measure of uncertainty or information. For example, the differential entropy can be negative; also it is not invariant under continuous co-ordinate transformations. This problem may be illustrated by a change of units when *x* is a dimensioned variable. *f*(*x*) will then have the units of 1/*x*. The argument of the logarithm must be dimensionless, otherwise it is improper, so that the differential entropy as given above will be improper. If *Δ* is some "standard" value of *x* (i.e. "bin size") and therefore has the same units, then a modified differential entropy may be written in proper form as: H = ∫ − ∞ ∞ f ( x ) log ⁡ ( f ( x ) Δ ) d x , {\displaystyle \mathrm {H} =\int _{-\infty }^{\infty }f(x)\log(f(x)\,\Delta )\,dx,} ({\displaystyle \mathrm {H} =\int _{-\infty }^{\infty }f(x)\log(f(x)\,\Delta )\,dx,}) and the result will be the same for any choice of units for *x*. In fact, the limit of discrete entropy as N → ∞ {\displaystyle N\rightarrow \infty } ({\displaystyle N\rightarrow \infty }) would also include a term of log ⁡ ( N ) {\displaystyle \log(N)} ({\displaystyle \log(N)}), which would in general be infinite. This is expected: continuous variables would typically have infinite entropy when discretized. The limiting density of discrete points is really a measure of how much easier a distribution is to describe than a distribution that is uniform over its quantization scheme.

### Relative entropy

Another useful measure of entropy that works equally well in the discrete and the continuous case is the **relative entropy** of a distribution. It is defined as the Kullback–Leibler divergence from the distribution to a reference measure *m* as follows. Assume that a probability distribution *p* is absolutely continuous with respect to a measure *m*, i.e. is of the form *p*(*dx*) = *f*(*x*)*m*(*dx*) for some non-negative *m*-integrable function *f* with *m*-integral 1, then the relative entropy can be defined as D K L ( p ‖ m ) = ∫ log ⁡ ( f ( x ) ) p ( d x ) = ∫ f ( x ) log ⁡ ( f ( x ) ) m ( d x ) . {\displaystyle D_{\mathrm {KL} }(p\|m)=\int \log(f(x))p(dx)=\int f(x)\log(f(x))m(dx).} ({\displaystyle D_{\mathrm {KL} }(p\|m)=\int \log(f(x))p(dx)=\int f(x)\log(f(x))m(dx).})

In this form the relative entropy generalizes (up to change in sign) both the discrete entropy, where the measure *m* is the counting measure, and the differential entropy, where the measure *m* is the Lebesgue measure. If the measure *m* is itself a probability distribution, the relative entropy is non-negative, and zero if *p* = *m* as measures. It is defined for any measure space, hence coordinate independent and invariant under co-ordinate reparameterizations if one properly takes into account the transformation of the measure *m*. The relative entropy, and (implicitly) entropy and differential entropy, do depend on the "reference" measure *m*.


## Use in number theory

Terence Tao used entropy to make a useful connection trying to solve the Erdős discrepancy problem.

Intuitively the idea behind the proof was if there is low information in terms of the Shannon entropy between consecutive random variables (here the random variable is defined using the Liouville function (which is a useful mathematical function for studying distribution of primes) *X**H* = λ ( n + H ) {\displaystyle \lambda (n+H)} ({\displaystyle \lambda (n+H)})). And in an interval [n, n+H] the sum over that interval could become arbitrarily large. For example, a sequence of +1's (which are values of *X**H* could take) have trivially low entropy and their sum would become big. But the key insight was showing a reduction in entropy by non negligible amounts as one expands H leading inturn to unbounded growth of a mathematical object over this random variable is equivalent to showing the unbounded growth per the Erdős discrepancy problem.

The proof is quite involved and it brought together breakthroughs not just in novel use of Shannon entropy, but also it used the Liouville function along with averages of modulated multiplicative functions in short intervals. Proving it also broke the "parity barrier" for this specific problem.

While the use of Shannon entropy in the proof is novel it is likely to open new research in this direction.


## Use in combinatorics

Entropy has become a useful quantity in combinatorics.

### Loomis–Whitney inequality

A simple example of this is an alternative proof of the Loomis–Whitney inequality: for every subset *A* ⊆ **Z***d*, we have | A | d − 1 ≤ ∏ i = 1 d | P i ( A ) | {\displaystyle |A|^{d-1}\leq \prod _{i=1}^{d}|P_{i}(A)|} ({\displaystyle |A|^{d-1}\leq \prod _{i=1}^{d}|P_{i}(A)|}) where *P**i* is the orthogonal projection in the *i*th coordinate: P i ( A ) = { ( x 1 , … , x i − 1 , x i + 1 , … , x d ) : ( x 1 , … , x d ) ∈ A } . {\displaystyle P_{i}(A)=\{(x_{1},\ldots ,x_{i-1},x_{i+1},\ldots ,x_{d}):(x_{1},\ldots ,x_{d})\in A\}.} ({\displaystyle P_{i}(A)=\{(x_{1},\ldots ,x_{i-1},x_{i+1},\ldots ,x_{d}):(x_{1},\ldots ,x_{d})\in A\}.})

The proof follows as a simple corollary of Shearer's inequality: if *X*1, ..., *X**d* are random variables and *S*1, ..., *S**n* are subsets of {1, ..., *d*} such that every integer between 1 and *d* lies in exactly *r* of these subsets, then H [ ( X 1 , … , X d ) ] ≤ 1 r ∑ i = 1 n H [ ( X j ) j ∈ S i ] {\displaystyle \mathrm {H} [(X_{1},\ldots ,X_{d})]\leq {\frac {1}{r}}\sum _{i=1}^{n}\mathrm {H} [(X_{j})_{j\in S_{i}}]} ({\displaystyle \mathrm {H} [(X_{1},\ldots ,X_{d})]\leq {\frac {1}{r}}\sum _{i=1}^{n}\mathrm {H} [(X_{j})_{j\in S_{i}}]}) where ( X j ) j ∈ S i {\displaystyle (X_{j})_{j\in S_{i}}} ({\displaystyle (X_{j})_{j\in S_{i}}}) is the Cartesian product of random variables *X**j* with indexes *j* in *S**i* (so the dimension of this vector is equal to the size of *S**i*).

We sketch how Loomis–Whitney follows from this: Indeed, let *X* be a uniformly distributed random variable with values in *A* and so that each point in *A* occurs with equal probability. Then (by the further properties of entropy mentioned above) Η(*X*) = log|*A*|, where |*A*| denotes the cardinality of *A*. Let *S**i* = {1, 2, ..., *i*−1, *i*+1, ..., *d*}. The range of ( X j ) j ∈ S i {\displaystyle (X_{j})_{j\in S_{i}}} ({\displaystyle (X_{j})_{j\in S_{i}}}) is contained in *P**i*(*A*) and hence H [ ( X j ) j ∈ S i ] ≤ log ⁡ | P i ( A ) | {\displaystyle \mathrm {H} [(X_{j})_{j\in S_{i}}]\leq \log |P_{i}(A)|} ({\displaystyle \mathrm {H} [(X_{j})_{j\in S_{i}}]\leq \log |P_{i}(A)|}). Now use this to bound the right side of Shearer's inequality and exponentiate the opposite sides of the resulting inequality you obtain.

### Approximation to binomial coefficient

For integers 0 < *k* < *n* let *q* = *k*/*n*. Then 2 n H ( q ) n + 1 ≤ ( n k ) ≤ 2 n H ( q ) , {\displaystyle {\frac {2^{n\mathrm {H} (q)}}{n+1}}\leq {\tbinom {n}{k}}\leq 2^{n\mathrm {H} (q)},} ({\displaystyle {\frac {2^{n\mathrm {H} (q)}}{n+1}}\leq {\tbinom {n}{k}}\leq 2^{n\mathrm {H} (q)},}) where H ( q ) = − q log 2 ⁡ ( q ) − ( 1 − q ) log 2 ⁡ ( 1 − q ) . {\displaystyle \mathrm {H} (q)=-q\log _{2}(q)-(1-q)\log _{2}(1-q).} ({\displaystyle \mathrm {H} (q)=-q\log _{2}(q)-(1-q)\log _{2}(1-q).})

| Proof (sketch) |
|---|
| Note that ( n k ) q q n ( 1 − q ) n − n q {\displaystyle {\tbinom {n}{k}}q^{qn}(1-q)^{n-nq}} ({\displaystyle {\tbinom {n}{k}}q^{qn}(1-q)^{n-nq}}) is one term of the expression ∑ i = 0 n ( n i ) q i ( 1 − q ) n − i = ( q + ( 1 − q ) ) n = 1. {\displaystyle \sum _{i=0}^{n}{\tbinom {n}{i}}q^{i}(1-q)^{n-i}=(q+(1-q))^{n}=1.} ({\displaystyle \sum _{i=0}^{n}{\tbinom {n}{i}}q^{i}(1-q)^{n-i}=(q+(1-q))^{n}=1.}) Rearranging gives the upper bound. For the lower bound one first shows, using some algebra, that it is the largest term in the summation. But then, ( n k ) q q n ( 1 − q ) n − n q ≥ 1 n + 1 {\displaystyle {\binom {n}{k}}q^{qn}(1-q)^{n-nq}\geq {\frac {1}{n+1}}} ({\displaystyle {\binom {n}{k}}q^{qn}(1-q)^{n-nq}\geq {\frac {1}{n+1}}}) since there are *n* + 1 terms in the summation. Rearranging gives the lower bound. |

A nice interpretation of this is that the number of binary strings of length *n* with exactly *k* many 1's is approximately 2 n H ( k / n ) {\displaystyle 2^{n\mathrm {H} (k/n)}} ({\displaystyle 2^{n\mathrm {H} (k/n)}}).


## Use in machine learning

Machine learning techniques arise largely from statistics and also information theory. In general, entropy is a measure of uncertainty and the objective of machine learning is to minimize uncertainty.

Decision tree learning algorithms use relative entropy to determine the decision rules that govern the data at each node. The information gain in decision trees I G ( Y , X ) {\displaystyle IG(Y,X)} ({\displaystyle IG(Y,X)}), which is equal to the difference between the entropy of Y {\displaystyle Y} ({\displaystyle Y}) and the conditional entropy of Y {\displaystyle Y} ({\displaystyle Y}) given X {\displaystyle X} ({\displaystyle X}), quantifies the expected information, or the reduction in entropy, from additionally knowing the value of an attribute X {\displaystyle X} ({\displaystyle X}). The information gain is used to identify which attributes of the dataset provide the most information and should be used to split the nodes of the tree optimally.

Bayesian inference models often apply the principle of maximum entropy to obtain prior probability distributions. The idea is that the distribution that best represents the current state of knowledge of a system is the one with the largest entropy, and is therefore suitable to be the prior.

Classification in machine learning performed by logistic regression or artificial neural networks often employs a standard loss function, called cross-entropy loss, that minimizes the average cross entropy between ground truth and predicted distributions. In general, cross entropy is a measure of the differences between two datasets similar to the KL divergence (also known as relative entropy).
