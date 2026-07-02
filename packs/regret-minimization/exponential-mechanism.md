---
title: "Exponential mechanism"
source: https://en.wikipedia.org/wiki/Exponential_mechanism
domain: regret-minimization
license: CC-BY-SA-4.0
tags: regret minimization, multi armed bandit, no regret dynamics, thompson sampling
fetched: 2026-07-02
---

# Exponential mechanism

The **exponential mechanism** is a technique for designing differentially private algorithms. It was developed by Frank McSherry and Kunal Talwar in 2007. Their work was recognized as a co-winner of the 2009 PET Award for Outstanding Research in Privacy Enhancing Technologies.

Most of the initial research in the field of differential privacy revolved around real-valued functions which have relatively low sensitivity to change in the data of a single individual and whose usefulness is not hampered by small additive perturbations. A natural question is what happens in the situation when one wants to preserve more general sets of properties. The exponential mechanism helps to extend the notion of differential privacy to address these issues. Moreover, it describes a class of mechanisms that includes all possible differentially private mechanisms.

## The mechanism

Source:

### Algorithm

In very generic terms, a privacy mechanism maps a set of $n\,\!$ inputs from domain ${\mathcal {D}}\,\!$ to a range ${\mathcal {R}}\,\!$ . The map may be randomized, in which case each element of the domain ${\mathcal {D}}\,\!$ corresponds to a probability distribution over the range ${\mathcal {R}}\,\!$ . The privacy mechanism makes no assumption about the nature of ${\mathcal {D}}\,\!$ and ${\mathcal {R}}\,\!$ apart from a base measure $\mu \,\!$ on ${\mathcal {R}}\,\!$ . Let us define a function $q:{\mathcal {D}}^{n}\times {\mathcal {R}}\rightarrow \mathbb {R} \,\!$ . Intuitively this function assigns a score to the pair $(d,r)\,\!$ , where $d\in {\mathcal {D}}^{n}\,\!$ and $r\in {\mathcal {R}}\,\!$ . The score reflects the appeal of the pair $(d,r)\,\!$ , i.e. the higher the score, the more appealing the pair is. Given the input $d\in {\mathcal {D}}^{n}\,\!$ , the mechanism's objective is to return an $r\in {\mathcal {R}}\,\!$ such that the function $q(d,r)\,\!$ is approximately maximized. To achieve this, set up the mechanism ${\mathcal {E}}_{q}^{\varepsilon }(d)\,\!$ as follows: **Definition:** For any function $q:({\mathcal {D}}^{n}\times {\mathcal {R}})\rightarrow \mathbb {R} \,\!$ , and a base measure $\mu \,\!$ over ${\mathcal {R}}\,\!$ , define:

${\mathcal {E}}_{q}^{\varepsilon }(d):=\,\!$

Choose

$r\,\!$

with probability proportional to

$e^{\varepsilon q(d,r)}\times \mu (r)\,\!$

, where

$d\in {\mathcal {D}}^{n},r\in {\mathcal {R}}\,\!$

.

This definition implies the fact that the probability of returning an $r\,\!$ increases exponentially with the increase in the value of $q(d,r)\,\!$ . Ignoring the base measure $\mu \,\!$ then the value $r\,\!$ which maximizes $q(d,r)\,\!$ has the highest probability. Moreover, this mechanism is differentially private. Proof of this claim will follow. One technicality that should be kept in mind is that in order to properly define ${\mathcal {E}}_{q}^{\varepsilon }(d)\,\!$ the $\int _{r}e^{\varepsilon q(d,r)}\times \mu (r)\,\!$ should be finite.

**Theorem (differential privacy):** ${\mathcal {E}}_{q}^{\varepsilon }(d)\,\!$ gives $(2\varepsilon \Delta q)\,\!$ -differential privacy, where $\Delta q$ is something that we need to define.

Proof: The probability density of ${\mathcal {E}}_{q}^{\varepsilon }(d)\,\!$ at $r\,\!$ equals

${\frac {e^{\varepsilon q(d,r)}\mu (r)}{\int e^{\varepsilon q(d,r)}\mu (r)\,dr}}.\,\!$

Now, if a single change in $d\,\!$ changes $q\,\!$ by at most $\Delta q\,\!$ then the numerator can change at most by a factor of $e^{\varepsilon \Delta q}\,\!$ and the denominator minimum by a factor of $e^{-\varepsilon \Delta q}\,\!$ . Thus, the ratio of the new probability density (i.e. with new $d\,\!$ ) and the earlier one is at most $\exp(2\varepsilon \Delta q)\,\!$ .

### Accuracy

We would ideally want the random draws of $r\,\!$ from the mechanism ${\mathcal {E}}_{q}^{\varepsilon }(d)\,\!$ to nearly maximize $q(d,r)\,\!$ . If we consider $\max _{r}q(d,r)\,\!$ to be $OPT\,\!$ then we can show that the probability of the mechanism deviating from $OPT\,\!$ is low, as long as there is a sufficient mass (in terms of $\mu$ ) of values $r\,\!$ with value $q\,\!$ close to the optimum.

**Lemma:** Let $S_{t}=\{r:q(d,r)>OPT-t\}\,\!$ and ${\bar {S}}_{2t}=\{r:q(d,r)\leq OPT-2t\}\,\!$ , we have $p({\bar {S}}_{2t})\,\!$ is at most $\exp(-\varepsilon t)/\mu (S_{t})\,\!$ . The probability is taken over ${\mathcal {R}}\,\!$ .

Proof: The probability $p({\bar {S}}_{2t})\,\!$ is at most $p({\bar {S}}_{2t})/p(S_{t})\,\!$ , as the denominator can be at most one. Since both the probabilities have the same normalizing term so,

${\frac {p({\bar {S}}_{2t})}{p(S_{t})}}={\frac {\int _{{\bar {S}}_{2t}}\exp(\varepsilon q(d,r))\mu (r)\,dr}{\int _{S_{t}}\exp(\varepsilon q(d,r))\mu (r)\,dr}}\leq \exp(-\varepsilon t){\frac {\mu ({\bar {S}}_{2t})}{\mu (S_{t})}}.$

The value of $\mu ({\bar {S}}_{2t})\,\!$ is at most one, and so this bound implies the lemma statement.

**Theorem (Accuracy):** For those values of $t\geq \ln \left({\frac {OPT}{t\mu (S_{t})}}\right)/\varepsilon \,\!$ , we have $E[q(d,{\mathcal {E}}_{q}^{\varepsilon }(d))]\geq OPT-3t\,\!$ .

Proof: It follows from the previous lemma that the probability of the score being at least $OPT-2t\,\!$ is $1-\exp(-\varepsilon t)/\mu (S_{t})\,\!$ . By hypothesis, $t\geq \ln \left({\frac {OPT}{t\mu (S_{t})}}\right)/\varepsilon \,\!$ . Substituting the value of $t\,\!$ we get this probability to be at least $1-t/OPT\,\!$ . Multiplying with $OPT-2t\,\!$ yields the desired bound.

We can assume $\mu (A)\,\!$ for $A\subseteq {\mathcal {R}}\,\!$ to be less than or equal to one in all the computations, because we can always normalize with $\mu ({\mathcal {R}})\,\!$ .

## Example application

Source:

Before we get into the details of the example let us define some terms which we will be using extensively throughout our discussion.

**Definition (global sensitivity):** The global sensitivity of a query $Q\,\!$ is its maximum difference when evaluated on two neighbouring datasets $D_{1},D_{2}\in {\mathcal {D}}^{n}\,\!$ :

$GS_{Q}=\max _{D_{1},D_{2}:d(D_{1},D_{2})=1}|(Q(D_{1})-Q(D_{2}))|.\,\!$

**Definition:** A predicate query $Q_{\varphi }\,\!$ for any predicate $\varphi \,\!$ is defined to be

$Q_{\varphi }={\frac {|\{x\in D:\varphi (x)\}|}{|D|}}.\,\!$

Note that $GS_{Q_{\varphi }}\leq 1/n\,\!$ for any predicate $\varphi \,\!$ .

### Release mechanism

The following is due to Avrim Blum, Katrina Ligett and Aaron Roth.

**Definition (Usefulness):** A mechanism ${\mathcal {A}}\,\!$ is $(\alpha ,\delta )\,\!$ -useful for queries in class $H\,\!$ with probability $1-\delta \,\!$ , if $\forall h\in H\,\!$ and every dataset $D\,\!$ , for ${\widehat {D}}={\mathcal {A}}(D)\,\!$ , $|Q_{h}({\widehat {D}})-Q_{h}(D)|\leq \alpha \,\!$ .

Informally, it means that with high probability the query $Q_{h}\,\!$ will behave in a similar way on the original dataset $D\,\!$ and on the synthetic dataset ${\widehat {D}}\,\!$ . Consider a common problem in Data Mining. Assume there is a database $D\,\!$ with $n\,\!$ entries. Each entry consist of $k\,\!$ -tuples of the form $(x_{1},x_{2},\dots ,x_{k})\,\!$ where $x_{i}\in \{0,1\}\,\!$ . Now, a user wants to learn a linear halfspace of the form $\pi _{1}x_{1}+\pi _{2}x_{2}+\cdots +\pi _{k-1}x_{k-1}\geq x_{k}\,\!$ . In essence the user wants to figure out the values of $\pi _{1},\pi _{2},\dots ,\pi _{k-1}\,\!$ such that maximum number of tuples in the database satisfy the inequality. The algorithm we describe below can generate a synthetic database ${\widehat {D}}\,\!$ which will allow the user to learn (approximately) the same linear half-space while querying on this synthetic database. The motivation for such an algorithm being that the new database will be generated in a differentially private manner and thus assure privacy to the individual records in the database $D\,\!$ .

In this section we show that it is possible to release a dataset which is useful for concepts from a polynomial VC-Dimension class and at the same time adhere to $\varepsilon \,\!$ -differential privacy as long as the size of the original dataset is at least polynomial on the VC-Dimension of the concept class. To state formally:

**Theorem:** For any class of functions $H\,\!$ and any dataset $D\subset \{0,1\}^{k}\,\!$ such that

$|D|\geq O\left({\frac {k\cdot \operatorname {VCDim} (H)\log(1/\alpha )}{\alpha ^{3}\varepsilon }}+{\frac {\log(1/\delta )}{\alpha \varepsilon }}\right)\,\!$

we can output an $(\alpha ,\delta )\,\!$ -useful dataset ${\widehat {D}}\,\!$ that preserves $\varepsilon \,\!$ -differential privacy. As we had mentioned earlier the algorithm need not be efficient.

One interesting fact is that the algorithm which we are going to develop generates a synthetic dataset whose size is independent of the original dataset; in fact, it only depends on the VC-dimension of the concept class and the parameter $\alpha \,\!$ . The algorithm outputs a dataset of size ${\tilde {O}}(\operatorname {VCDim} (H)/\alpha ^{2})\,\!$

We borrow the Uniform Convergence Theorem from combinatorics and state a corollary of it which aligns to our need.

**Lemma:** Given any dataset $D\,\!$ there exists a dataset ${\widehat {D}}\,\!$ of size $=O(\operatorname {VCDim} (H)\log(1/\alpha ))/\alpha ^{2}\,\!$ such that $\max _{h\in H}|Q_{h}(D)-Q_{h}({\widehat {D}})|\leq \alpha /2\,\!$ .

Proof:

We know from the uniform convergence theorem that

${\begin{aligned}&\Pr \left[\,\left|Q_{h}(D)-Q_{h}({\widehat {D}})\right|\geq {\frac {\alpha }{2}}{\text{ for some }}h\in H\right]\\[5pt]\leq {}&2\left({\frac {em}{\operatorname {VCDim} (H)}}\right)^{\operatorname {VCDim} (H)}\cdot e^{-\alpha ^{2}m/8},\end{aligned}}$

where probability is over the distribution of the dataset. Thus, if the RHS is less than one then we know for sure that the data set ${\widehat {D}}\,\!$ exists. To bound the RHS to less than one we need $m\geq \lambda (\operatorname {VCDim} (H)\log(m/\operatorname {VCDim} (H))/\alpha ^{2})\,\!$ , where $\lambda \,\!$ is some positive constant. Since we stated earlier that we will output a dataset of size ${\tilde {O}}(\operatorname {VCDim} (H)/\alpha ^{2})\,\!$ , so using this bound on $m\,\!$ we get $m\geq \lambda (\operatorname {VCDim} (H)\log(1/\alpha )/\alpha ^{2})\,\!$ . Hence the lemma.

Now we invoke the exponential mechanism.

**Definition:** For any function $q:((\{0,1\}^{k})^{n}\times (\{0,1\}^{k})^{m})\rightarrow \mathbb {R} \,\!$ and input dataset $D\,\!$ , the exponential mechanism outputs each dataset ${\widehat {D}}\,\!$ with probability proportional to $e^{q(D,{\widehat {D}})\varepsilon n/2}\,\!$ .

From the exponential mechanism we know this preserves $(\varepsilon nGS_{q})\,\!$ -differential privacy. Let's get back to the proof of the Theorem.

We define $(q(D),q({\widehat {D}}))=-\max _{h\in H}|Q_{h}(D)-Q_{h}({\widehat {D}})|\,\!$ .

To show that the mechanism satisfies the $(\alpha ,\delta )\,\!$ -usefulness, we should show that it outputs some dataset ${\widehat {D}}\,\!$ with $q(D,{\widehat {D}})\geq -\alpha \,\!$ with probability $1-\delta \,\!$ . There are at most $2^{km}\,\!$ output datasets and the probability that $q(D,{\widehat {D}})\leq -\alpha \,\!$ is at most proportional to $e^{-\varepsilon \alpha n/2}\,\!$ . Thus by union bound, the probability of outputting any such dataset ${\widehat {D}}\,\!$ is at most proportional to $2^{km}e^{-\varepsilon \alpha n/2}\,\!$ . Again, we know that there exists some dataset ${\widehat {D}}\in (\{0,1\}^{k})^{m}\,\!$ for which $q(D,{\widehat {D}})\geq -\alpha /2\,\!$ . Therefore, such a dataset is output with probability at least proportional to $e^{-\alpha \varepsilon n/4}\,\!$ .

Let $A:=\,\!$ the event that the exponential mechanism outputs some dataset ${\widehat {D}}\,\!$ such that $q(D,{\widehat {D}})\geq -\alpha /2\,\!$ .

$B:=\,\!$ the event that the exponential mechanism outputs some dataset ${\widehat {D}}\,\!$ such that $q(D,{\widehat {D}})\leq -\alpha \,\!$ .

$\therefore {\frac {\Pr[A]}{\Pr[B]}}\geq {\frac {e^{-\alpha \varepsilon n/4}}{2^{km}e^{-\alpha \varepsilon n/2}}}={\frac {e^{\alpha \varepsilon n/4}}{2^{km}}}.\,\!$

Now setting this quantity to be at least $1/\delta \geq (1-\delta )/\delta \,\!$ , we find that it suffices to have

$n\geq {\frac {4}{\varepsilon \alpha }}\left(km+\ln {\frac {1}{\delta }}\right)\geq O\left({\frac {d\cdot \operatorname {VCDim} (H)\log(1/\alpha )}{\alpha ^{3}\varepsilon }}+{\frac {\log(1/\delta )}{\alpha \varepsilon }}\right).\,\!$

And hence we prove the theorem.

## Applications in other domains

In the above example of the usage of exponential mechanism, one can output a synthetic dataset in a differentially private manner and can use the dataset to answer queries with good accuracy. Other private mechanisms, such as posterior sampling, which returns parameters rather than datasets, can be made equivalent to the exponential one.

Apart from the setting of privacy, the exponential mechanism has also been studied in the context of auction theory and classification algorithms. In the case of auctions the exponential mechanism helps to achieve a *truthful* auction setting.
