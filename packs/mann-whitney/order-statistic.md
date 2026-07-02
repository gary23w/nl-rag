---
title: "Order statistic"
source: https://en.wikipedia.org/wiki/Order_statistic
domain: mann-whitney
license: CC-BY-SA-4.0
tags: Mann Whitney U test, Wilcoxon rank-sum, stochastic ordering, order statistic
fetched: 2026-07-02
---

# Order statistic

In statistics, the *k*th **order statistic** of a statistical sample is equal to its *k*th-smallest value. Given a sample of size n , the *k*th order statistic is denoted $x_{(k)}$ , with $1\leq k\leq n$ . Together with rank statistics, order statistics are among the most fundamental tools in non-parametric statistics and inference.

Important special cases of the order statistics are the minimum and maximum value of a sample, and (with some qualifications discussed below) the sample median and other sample quantiles.

When using probability theory to analyze order statistics of random samples from a continuous distribution, the cumulative distribution function is used to reduce the analysis to the case of order statistics of the uniform distribution.

## Notation and examples

For example, suppose that four numbers are observed or recorded, resulting in a sample of size 4. If the sample values are

6, 9, 3, 7

the order statistics would be

${\begin{aligned}x_{(1)}&=3\\x_{(2)}&=6\\x_{(3)}&=7\\x_{(4)}&=9\end{aligned}}$

The **first order statistic** (or **smallest order statistic**) is always the minimum of the sample, that is,

$X_{(1)}=\min\{\,X_{1},\ldots ,X_{n}\,\}$

where, following a common convention, we use upper-case letters to refer to random variables, and lower-case letters (as above) to refer to their actual observed values.

Similarly, for a sample of size *n*, the *n*th order statistic (or **largest order statistic**) is the maximum, that is,

$X_{(n)}=\max\{\,X_{1},\ldots ,X_{n}\,\}.$

The sample range is the difference between the maximum and minimum. It is a function of the order statistics:

${\rm {Range}}\{\,X_{1},\ldots ,X_{n}\,\}=X_{(n)}-X_{(1)}.$

A similar important statistic in exploratory data analysis that is simply related to the order statistics is the sample interquartile range.

The sample median may or may not be an order statistic, since there is a single middle value only when the number *n* of observations is odd. More precisely, if *n* = 2*m*+1 for some integer *m*, then the sample median is $X_{(m+1)}$ and so is an order statistic. On the other hand, when *n* is even, *n* = 2*m* and there are two middle values, $X_{(m)}$ and $X_{(m+1)}$ , and the sample median is some function of the two (usually the average) and hence not an order statistic. Similar remarks apply to all sample quantiles.

## Probabilistic analysis

Given any random variables $X_{1},X_{2},\ldots ,X_{n}$ , the random variables $X_{(1)},X_{(2)},\ldots ,X_{(n)}$ are defined by sorting $X_{1},X_{2},\ldots ,X_{n}$ in increasing order.

The case where the random variables $X_{1},X_{2},\ldots ,X_{n}$ are independent and identically distributed is treated below. In general, $X_{1},X_{2},\ldots ,X_{n}$ can arise by sampling from more than one population. Then we consider the case where they are independent, but not necessarily identically distributed, and their joint probability distribution is given by the Bapat–Beg theorem.

From now on, we will assume that the random variables under consideration are continuous and, where convenient, we will also assume that they have a probability density function (PDF), that is, they are absolutely continuous. The peculiarities of the analysis of distributions assigning mass to points (in particular, discrete distributions) are discussed at the end.

### Cumulative distribution function of order statistics

For a random sample as above, with cumulative distribution $F_{X}(x)$ , the order statistics for that sample have cumulative distributions as follows (where *r* specifies which order statistic): $F_{X_{(r)}}(x)=\sum _{j=r}^{n}{\binom {n}{j}}\left[F_{X}(x)\right]^{j}\left[1-F_{X}(x)\right]^{n-j}$ The proof of this formula is pure combinatorics: for the r th order statistic to be $\leq x$ , the number of samples that are $>x$ has to be between 0 and $n-r$ . In the case that $X_{(j)}$ is the largest order statistic $\leq x$ , there has to be j samples $\leq x$ (each with an independent probability of $F_{X}(x)$ ) and $n-j$ samples $>x$ (each with an independent probability of $1-F_{X}(x)$ ). Finally there are ${\textstyle {\binom {n}{j}}}$ different ways of choosing which of the n samples are of the $\leq x$ kind.

The corresponding probability density function may be derived from this result, and is found to be

$f_{X_{(r)}}(x)={\frac {n!}{(r-1)!(n-r)!}}f_{X}(x)\left[F_{X}(x)\right]^{r-1}\left[1-F_{X}(x)\right]^{n-r}.$

Moreover, there are two special cases, which have CDFs that are easy to compute.

$F_{X_{(n)}}(x)=\Pr(\max\{\,X_{1},\ldots ,X_{n}\,\}\leq x)=[F_{X}(x)]^{n}$

$F_{X_{(1)}}(x)=\Pr(\min\{\,X_{1},\ldots ,X_{n}\,\}\leq x)=1-[1-F_{X}(x)]^{n}$

Which can be derived by careful consideration of probabilities.

### Probability distributions of order statistics

#### Order statistics sampled from a uniform distribution

In this section we show that the order statistics of the uniform distribution on the unit interval have marginal distributions belonging to the beta distribution family. We also give a simple method to derive the joint distribution of any number of order statistics, and finally translate these results to arbitrary continuous distributions using the cdf.

We assume throughout this section that $X_{1},X_{2},\ldots ,X_{n}$ are random samples drawn from a continuous distribution with cdf $F_{X}$ . Denoting $U_{i}=F_{X}(X_{i})$ we obtain the corresponding random sample $U_{1},\ldots ,U_{n}$ from the standard uniform distribution. Note that the order statistics also satisfy $U_{(i)}=F_{X}(X_{(i)})$ .

The probability density function of the order statistic $U_{(k)}$ is equal to

$f_{U_{(k)}}(u)={n! \over (k-1)!(n-k)!}u^{k-1}(1-u)^{n-k}$

that is, the *k*th order statistic of the uniform distribution is a beta-distributed random variable.

$U_{(k)}\sim \operatorname {Beta} (k,n+1\mathbf {-} k).$

The proof of these statements is as follows. For $U_{(k)}$ to be between *u* and *u* + *du*, it is necessary that exactly *k* − 1 elements of the sample are smaller than *u*, and that at least one is between *u* and *u* + d*u*. The probability that more than one is in this latter interval is already $O(du^{2})$ , so we have to calculate the probability that exactly *k* − 1, 1 and *n* − *k* observations fall in the intervals $(0,u)$ , $(u,u+du)$ and $(u+du,1)$ respectively. This equals (refer to multinomial distribution for details)

${n! \over (k-1)!(n-k)!}u^{k-1}\cdot du\cdot (1-u-du)^{n-k}$

and the result follows.

The mean of this distribution is *k* / (*n* + 1).

#### The joint distribution of the order statistics of the uniform distribution

Similarly, for *i* < *j*, the joint probability density function of the two order statistics *U*(*i*) < *U*(*j*) can be shown to be

$f_{U_{(i)},U_{(j)}}(u,v)=n!{u^{i-1} \over (i-1)!}{(v-u)^{j-i-1} \over (j-i-1)!}{(1-v)^{n-j} \over (n-j)!}$

which is (up to terms of higher order than $O(du\,dv)$ ) the probability that *i* − 1, 1, *j* − 1 − *i*, 1 and *n* − *j* sample elements fall in the intervals $(0,u)$ , $(u,u+du)$ , $(u+du,v)$ , $(v,v+dv)$ , $(v+dv,1)$ respectively.

One reasons in an entirely analogous way to derive the higher-order joint distributions. Perhaps surprisingly, the joint density of the *n* order statistics turns out to be *constant*:

$f_{U_{(1)},U_{(2)},\ldots ,U_{(n)}}(u_{1},u_{2},\ldots ,u_{n})=n!.$

One way to understand this is that the unordered sample does have constant density equal to 1, and that there are *n*! different permutations of the sample corresponding to the same sequence of order statistics. This is related to the fact that 1/*n*! is the volume of the region $0<u_{1}<\cdots <u_{n}<1$ . It is also related with another particularity of order statistics of uniform random variables: It follows from the BRS-inequality that the maximum expected number of uniform U(0,1] random variables one can choose from a sample of size n with a sum up not exceeding $0<s<n/2$ is bounded above by ${\sqrt {2sn}}$ , which is thus invariant on the set of all $s,n$ with constant product $sn$ .

Using the above formulas, one can derive the distribution of the range of the order statistics, that is the distribution of $U_{(n)}-U_{(1)}$ , i.e. maximum minus the minimum. More generally, for $n\geq k>j\geq 1$ , $U_{(k)}-U_{(j)}$ also has a beta distribution: $U_{(k)}-U_{(j)}\sim \operatorname {Beta} (k-j,n-(k-j)+1)$ From these formulas we can derive the covariance between two order statistics: $\operatorname {Cov} (U_{(k)},U_{(j)})={\frac {j(n-k+1)}{(n+1)^{2}(n+2)}}$ The formula follows from noting that ${\begin{aligned}\operatorname {Var} (U_{(k)}-U_{(j)})&=\operatorname {Var} (U_{(k)})+\operatorname {Var} (U_{(j)})-2\cdot \operatorname {Cov} (U_{(k)},U_{(j)})\\[1ex]&={\frac {k(n-k+1)}{(n+1)^{2}(n+2)}}+{\frac {j(n-j+1)}{(n+1)^{2}(n+2)}}-2\cdot \operatorname {Cov} (U_{(k)},U_{(j)})\end{aligned}}$ and comparing that with $\operatorname {Var} (U)={\frac {(k-j)(n-(k-j)+1)}{(n+1)^{2}(n+2)}}$ where $U\sim \operatorname {Beta} (k-j,n-(k-j)+1)$ , which is the actual distribution of the difference.

#### Order statistics sampled from an exponential distribution

For $X_{1},X_{2},..,X_{n}$ a random sample of size *n* from an exponential distribution with parameter *λ*, the order statistics *X*(*i*) for *i* = 1,2,3, ..., *n* each have distribution

$X_{(i)}{\stackrel {d}{=}}{\frac {1}{\lambda }}\left(\sum _{j=1}^{i}{\frac {Z_{j}}{n-j+1}}\right)$

where the *Z**j* are i.i.d. standard exponential random variables (i.e. with rate parameter 1). This result was first published by Alfréd Rényi.

#### Order statistics sampled from an Erlang distribution

The Laplace transform of order statistics may be sampled from an Erlang distribution via a path counting method .

#### The joint distribution of the order statistics of an absolutely continuous distribution

If *F**X* is absolutely continuous, it has a density such that $dF_{X}(x)=f_{X}(x)\,dx$ , and we can use the substitutions

$u=F_{X}(x)$

and

$du=f_{X}(x)\,dx$

to derive the following probability density functions for the order statistics of a sample of size *n* drawn from the distribution of *X*:

$f_{X_{(k)}}(x)={\frac {n!}{(k-1)!(n-k)!}}[F_{X}(x)]^{k-1}[1-F_{X}(x)]^{n-k}f_{X}(x)$

$f_{X_{(j)},X_{(k)}}(x,y)={\frac {n!}{(j-1)!(k-j-1)!(n-k)!}}[F_{X}(x)]^{j-1}[F_{X}(y)-F_{X}(x)]^{k-1-j}[1-F_{X}(y)]^{n-k}f_{X}(x)f_{X}(y)$ where $x\leq y$

$f_{X_{(1)},\ldots ,X_{(n)}}(x_{1},\ldots ,x_{n})=n!f_{X}(x_{1})\cdots f_{X}(x_{n})$ where $x_{1}\leq x_{2}\leq \dots \leq x_{n}.$

## Application: confidence intervals for quantiles

An interesting question is how well the order statistics perform as estimators of the quantiles of the underlying distribution.

### A small-sample-size example

The simplest case to consider is how well the sample median estimates the population median.

As an example, consider a random sample of size 6. In that case, the sample median is usually defined as the midpoint of the interval delimited by the 3rd and 4th order statistics. However, we know from the preceding discussion that the probability that this interval actually contains the population median is

${6 \choose 3}(1/2)^{6}={5 \over 16}\approx 31\%.$

Although the sample median is probably among the best distribution-independent point estimates of the population median, what this example illustrates is that it is not a particularly good one in absolute terms. In this particular case, a better confidence interval for the median is the one delimited by the 2nd and 5th order statistics, which contains the population median with probability

$\left[{6 \choose 2}+{6 \choose 3}+{6 \choose 4}\right](1/2)^{6}={25 \over 32}\approx 78\%.$

With such a small sample size, if one wants at least 95% confidence, one is reduced to saying that the median is between the minimum and the maximum of the 6 observations with probability 31/32 or approximately 97%. Size 6 is, in fact, the smallest sample size such that the interval determined by the minimum and the maximum is at least a 95% confidence interval for the population median.

### Large sample sizes

For the uniform distribution, as *n* tends to infinity, the *p*th sample quantile is asymptotically normally distributed, since it is approximated by

$U_{(\lceil np\rceil )}\sim AN{\left(p,{\frac {p(1-p)}{n}}\right)}.$

For a general distribution *F* with a continuous non-zero density at *F* −1(*p*), a similar asymptotic normality applies:

$X_{(\lceil np\rceil )}\sim AN{\left(F^{-1}(p),{\frac {p(1-p)}{n[f(F^{-1}(p))]^{2}}}\right)}$

where *f* is the density function, and *F* −1 is the quantile function associated with *F*. One of the first people to mention and prove this result was Frederick Mosteller in his seminal paper in 1946. Further research led in the 1960s to the Bahadur representation which provides information about the error bounds. The convergence to normal distribution also holds in a stronger sense, such as convergence in relative entropy or KL divergence.

An interesting observation can be made in the case where the distribution is symmetric, and the population median equals the population mean. In this case, the sample mean, by the central limit theorem, is also asymptotically normally distributed, but with variance σ2*/n* instead. This asymptotic analysis suggests that the mean outperforms the median in cases of low kurtosis, and vice versa. For example, the median achieves better confidence intervals for the Laplace distribution, while the mean performs better for *X* that are normally distributed.

#### Proof

It can be shown that

$B(k,n+1-k)\ {\stackrel {\mathrm {d} }{=}}\ {\frac {X}{X+Y}},$

where

$X=\sum _{i=1}^{k}Z_{i},\quad Y=\sum _{i=k+1}^{n+1}Z_{i},$

with *Zi* being independent identically distributed exponential random variables with rate 1. Since *X*/*n* and *Y*/*n* are asymptotically normally distributed by the CLT, our results follow by application of the delta method.

## Mutual Information of Order Statistics

The mutual information and f-divergence between order statistics have also been considered. For example, if the parent distribution is continuous, then for all $1\leq r,m\leq n$ $I(X_{(r)};X_{(m)})=I(U_{(r)};U_{(m)}),$ In other words, mutual information is independent of the parent distribution. For discrete random variables, the equality need not to hold and we only have $I(X_{(r)};X_{(m)})\leq I(U_{(r)};U_{(m)}),$

The mutual information between uniform order statistics is given by $I(U_{(r)};U_{(m)})=T_{m-1}+T_{n-r}-T_{m-r+1}-T_{n}$ where $T_{k}=\log(k!)-kH_{k}$ where $H_{k}$ is the k -th harmonic number.

## Application: Non-parametric density estimation

Moments of the distribution for the first order statistic can be used to develop a non-parametric density estimator. Suppose, we want to estimate the density $f_{X}$ at the point $x^{*}$ . Consider the random variables $Y_{i}=|X_{i}-x^{*}|$ , which are i.i.d with distribution function $g_{Y}(y)=f_{X}(y+x^{*})+f_{X}(x^{*}-y)$ . In particular, $f_{X}(x^{*})={\frac {g_{Y}(0)}{2}}$ .

The expected value of the first order statistic $Y_{(1)}$ given a sample of N total observations yields,

$E(Y_{(1)})={\frac {1}{(N+1)g(0)}}+{\frac {1}{(N+1)(N+2)}}\int _{0}^{1}Q''(z)\delta _{N+1}(z)\,dz$

where Q is the quantile function associated with the distribution $g_{Y}$ , and $\delta _{N}(z)=(N+1)(1-z)^{N}$ . This equation in combination with a jackknifing technique becomes the basis for the following density estimation algorithm,

```
  Input: A sample of 
  
    
      
        N
      
    
    {\displaystyle N}
  
 observations. 
  
    
      
        {
        
          x
          
            ℓ
          
        
        
          }
          
            ℓ
            =
            1
          
          
            M
          
        
      
    
    {\displaystyle \{x_{\ell }\}_{\ell =1}^{M}}
  
 points of density evaluation. Tuning parameter 
  
    
      
        a
        ∈
        (
        0
        ,
        1
        )
      
    
    {\displaystyle a\in (0,1)}
  
 (usually 1/3).
  Output: 
  
    
      
        {
        
          
            
              
                f
                ^
              
            
          
          
            ℓ
          
        
        
          }
          
            ℓ
            =
            1
          
          
            M
          
        
      
    
    {\displaystyle \{{\hat {f}}_{\ell }\}_{\ell =1}^{M}}
  
 estimated density at the points of evaluation.
```

```
  1: Set 
  
    
      
        
          m
          
            N
          
        
        =
        round
        ⁡
        (
        
          N
          
            1
            −
            a
          
        
        )
      
    
    {\displaystyle m_{N}=\operatorname {round} (N^{1-a})}
  

  2: Set 
  
    
      
        
          s
          
            N
          
        
        =
        
          
            N
            
              m
              
                N
              
            
          
        
      
    
    {\displaystyle s_{N}={\frac {N}{m_{N}}}}
  

  3: Create an 
  
    
      
        
          s
          
            N
          
        
        ×
        
          m
          
            N
          
        
      
    
    {\displaystyle s_{N}\times m_{N}}
  
 matrix 
  
    
      
        
          M
          
            i
            j
          
        
      
    
    {\displaystyle M_{ij}}
  
 which holds 
  
    
      
        
          m
          
            N
          
        
      
    
    {\displaystyle m_{N}}
  
 subsets with 
  
    
      
        
          s
          
            N
          
        
      
    
    {\displaystyle s_{N}}
  
 observations each.
  4: Create a vector 
  
    
      
        
          
            
              f
              ^
            
          
        
      
    
    {\displaystyle {\hat {f}}}
  
 to hold the density evaluations.
  5: for 
  
    
      
        ℓ
        =
        1
        →
        M
      
    
    {\displaystyle \ell =1\to M}
  
 do
  6:     for 
  
    
      
        k
        =
        1
        →
        
          m
          
            N
          
        
      
    
    {\displaystyle k=1\to m_{N}}
  
 do
  7:         Find the nearest distance 
  
    
      
        
          d
          
            ℓ
            k
          
        
      
    
    {\displaystyle d_{\ell k}}
  
 to the current point 
  
    
      
        
          x
          
            ℓ
          
        
      
    
    {\displaystyle x_{\ell }}
  
 within the 
  
    
      
        k
      
    
    {\displaystyle k}
  
th subset
  8:     end for
  9:     Compute the subset average of distances to 
  
    
      
        
          x
          
            ℓ
          
        
        :
        
          d
          
            ℓ
          
        
        =
        
          ∑
          
            k
            =
            1
          
          
            
              m
              
                N
              
            
          
        
        
          
            
              d
              
                ℓ
                k
              
            
            
              m
              
                N
              
            
          
        
      
    
    {\displaystyle x_{\ell }:d_{\ell }=\sum _{k=1}^{m_{N}}{\frac {d_{\ell k}}{m_{N}}}}
  

 10:     Compute the density estimate at 
  
    
      
        
          x
          
            ℓ
          
        
        :
        
          
            
              
                f
                ^
              
            
          
          
            ℓ
          
        
        =
        
          
            1
            
              2
              (
              1
              +
              
                s
                
                  N
                
              
              )
              
                d
                
                  ℓ
                
              
            
          
        
      
    
    {\displaystyle x_{\ell }:{\hat {f}}_{\ell }={\frac {1}{2(1+s_{N})d_{\ell }}}}
  

 11:  end for
 12: return 
  
    
      
        
          
            
              f
              ^
            
          
        
      
    
    {\displaystyle {\hat {f}}}
  
```

In contrast to the bandwidth/length based tuning parameters for histogram and kernel based approaches, the tuning parameter for the order statistic based density estimator is the size of sample subsets. Such an estimator is more robust than histogram and kernel based approaches, for example densities like the Cauchy distribution (which lack finite moments) can be inferred without the need for specialized modifications such as IQR based bandwidths. This is because the first moment of the order statistic always exists if the expected value of the underlying distribution does, but the converse is not necessarily true.

## Dealing with discrete variables

Suppose $X_{1},X_{2},\ldots ,X_{n}$ are i.i.d. random variables from a discrete distribution with cumulative distribution function $F(x)$ and probability mass function $f(x)$ . To find the probabilities of the $k^{\text{th}}$ order statistics, three values are first needed, namely ${\begin{aligned}p_{1}&=\Pr(X<x)=F(x)-f(x),\\p_{2}&=\Pr(X=x)=f(x),{\text{ and }}\\p_{3}&=\Pr(X>x)=1-F(x).\end{aligned}}$

The cumulative distribution function of the $k^{\text{th}}$ order statistic can be computed by noting that

${\begin{aligned}\Pr(X_{(k)}\leq x)&=\Pr({\text{there are at least }}k{\text{ observations less than or equal to }}x),\\&=\Pr({\text{there are at most }}n-k{\text{ observations greater than }}x),\\&=\sum _{j=0}^{n-k}{\binom {n}{j}}p_{3}^{j}(p_{1}+p_{2})^{n-j}.\end{aligned}}$

Similarly, $P(X_{(k)}<x)$ is given by

${\begin{aligned}\Pr(X_{(k)}<x)&=\Pr({\text{there are at least }}k{\text{ observations less than }}x),\\&=\Pr({\text{there are at most }}n-k{\text{ observations greater than or equal to }}x),\\&=\sum _{j=0}^{n-k}{n \choose j}(p_{2}+p_{3})^{j}(p_{1})^{n-j}.\end{aligned}}$

Note that the probability mass function of $X_{(k)}$ is just the difference of these values, that is to say

${\begin{aligned}\Pr(X_{(k)}=x)&=\Pr(X_{(k)}\leq x)-\Pr(X_{(k)}<x),\\&=\sum _{j=0}^{n-k}{\binom {n}{j}}\left[p_{3}^{j}(p_{1}+p_{2})^{n-j}-(p_{2}+p_{3})^{j}(p_{1})^{n-j}\right],\\&=\sum _{j=0}^{n-k}{\binom {n}{j}}\left[\left(1-F(x)\right)^{j}F(x)^{n-j}-\left(1-F(x)+f(x)\right)^{j}\left(F(x)-f(x)\right)^{n-j}\right].\end{aligned}}$

## Computing order statistics

The problem of computing the *k*th smallest (or largest) element of a list is called the selection problem and is solved by a selection algorithm. Although this problem is difficult for very large lists, sophisticated selection algorithms have been created that can solve this problem in time proportional to the number of elements in the list, even if the list is totally unordered. If the data is stored in certain specialized data structures, this time can be brought down to O(log *n*). In many applications all order statistics are required, in which case a sorting algorithm can be used and the time taken is O(*n* log *n*).

## Applications

Order statistics have applications in areas like reliability theory, financial mathematics, survival analysis, epidemiology, sports, quality control, and actuarial risk. There is an extensive literature devoted to studies on applications of order statistics in these fields.

For example, a recent application in actuarial risk can be found in, where some weighted premium principles in terms of record claims and kth record claims are provided.
