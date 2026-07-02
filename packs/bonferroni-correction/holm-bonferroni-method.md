---
title: "Holm–Bonferroni method"
source: https://en.wikipedia.org/wiki/Holm–Bonferroni_method
domain: bonferroni-correction
license: CC-BY-SA-4.0
tags: Bonferroni correction, Holm Bonferroni, Sidak correction, union bound
fetched: 2026-07-02
---

# Holm–Bonferroni method

In statistics, the **Holm–Bonferroni method**, also called the **Holm method** or **Bonferroni–Holm method**, is used to counteract the problem of multiple comparisons. It is intended to control the family-wise error rate (FWER) and offers a simple test uniformly more powerful than the Bonferroni correction. It is named after Sture Holm, who codified the method, and Carlo Emilio Bonferroni.

## Motivation

When considering several hypotheses, the problem of multiplicity arises: the more hypotheses are tested, the higher the probability of obtaining Type I errors (false positives). The Holm–Bonferroni method is one of many approaches for controlling the FWER, i.e., the probability that one or more Type I errors will occur, by adjusting the rejection criterion for each of the individual hypotheses.

## Formulation

The method is as follows:

- Suppose you have m p-values, sorted into order lowest-to-highest $P_{1},\ldots ,P_{m}$ , for the corresponding null hypotheses $H_{1},\ldots ,H_{m}$ . And suppose the desired maximum FWER is $\alpha$ .
- Is $P_{1}\leq \alpha /m$ ? If so, reject $H_{1}$ and continue to the next step, otherwise EXIT.
- Is $P_{2}\leq \alpha /(m-1)$ ? If so, reject $H_{2}$ also, and continue to the next step, otherwise EXIT.
- And so on: for each P value, test whether $P_{k}\leq {\frac {\alpha }{m+1-k}}$ . If so, reject $H_{k}$ and continue to examine the larger P values, otherwise EXIT.

This method ensures that the FWER is at most $\alpha$ , in the strong sense.

### Rationale

The simple Bonferroni correction rejects only null hypotheses with *p*-value less than or equal to ${\frac {\alpha }{m}}$ , in order to ensure that the FWER, i.e., the risk of rejecting one or more true null hypotheses (i.e., of committing one or more type I errors) is at most $\alpha$ . The cost of this protection against type I errors is an increased risk of failing to reject one or more false null hypotheses (i.e., of committing one or more type II errors).

The Holm–Bonferroni method also controls the FWER at $\alpha$ , but with a lower increase of type II error risk than the classical Bonferroni method. The Holm–Bonferroni method sorts the *p*-values from lowest to highest and compares them to nominal alpha levels of ${\frac {\alpha }{m}}$ to $\alpha$ (respectively), namely the values ${\frac {\alpha }{m}},{\frac {\alpha }{m-1}},\ldots ,{\frac {\alpha }{2}},{\frac {\alpha }{1}}$ .

- The index k identifies the first *p*-value that is *not* low enough to validate rejection. Therefore, the null hypotheses $H_{(1)},\ldots ,H_{(k-1)}$ are rejected, while the null hypotheses $H_{(k)},...,H_{(m)}$ are not rejected.
- If $k=1$ then no *p*-values were low enough for rejection, therefore no null hypotheses are rejected.
- If no such index k could be found then all *p*-values were low enough for rejection, therefore all null hypotheses are rejected (none are accepted).

### Proof

Let $H_{(1)}\ldots H_{(m)}$ be the family of hypotheses sorted by their p-values $P_{(1)}\leq P_{(2)}\leq \cdots \leq P_{(m)}$ . Let $I_{0}$ be the set of indices corresponding to the (unknown) true null hypotheses, having $m_{0}$ members.

> **Claim**: If we wrongly reject some true hypothesis, there is a true hypothesis $H_{(\ell )}$ for which $P_{(\ell )}$ is at most ${\frac {\alpha }{m_{0}}}$ .
> 
> First note that, in this case, there is at least one true hypothesis, so $m_{0}\geq 1$ . Let $\ell$ be such that $H_{(\ell )}$ is the first rejected true hypothesis. Then $H_{(1)},\ldots ,H_{(\ell -1)}$ are all rejected false hypotheses. It follows that $\ell -1\leq m-m_{0}$ and, hence, ${\frac {1}{m-\ell +1}}\leq {\frac {1}{m_{0}}}$ (1). Since $H_{(\ell )}$ is rejected, it must be $P_{(\ell )}\leq {\frac {\alpha }{m-\ell +1}}$ by definition of the testing procedure. Using (1), we conclude that $P_{(\ell )}\leq {\frac {\alpha }{m_{0}}}$ , as desired.

So let us define the random event $A=\bigcup _{i\in I_{0}}\left\{P_{i}\leq {\frac {\alpha }{m_{0}}}\right\}$ . Note that, for $i\in I_{o}$ , since $H_{i}$ is a true null hypothesis, we have that $P\left(\left\{P_{i}\leq {\frac {\alpha }{m_{0}}}\right\}\right)={\frac {\alpha }{m_{0}}}$ . Subadditivity of the probability measure implies that $\Pr(A)\leq \sum _{i\in I_{0}}P\left(\left\{P_{i}\leq {\frac {\alpha }{m_{0}}}\right\}\right)=\sum _{i\in I_{0}}{\frac {\alpha }{m_{0}}}=\alpha$ . Therefore, the probability to reject a true hypothesis is at most $\alpha$ .

### Alternative proof

The Holm–Bonferroni method can be viewed as a closed testing procedure, with the Bonferroni correction applied locally on each of the intersections of null hypotheses.

The closure principle states that a hypothesis $H_{i}$ in a family of hypotheses $H_{1},\ldots ,H_{m}$ is rejected – while controlling the FWER at level $\alpha$ – if and only if all the sub-families of the intersections with $H_{i}$ are rejected at level $\alpha$ .

The Holm–Bonferroni method is a *shortcut procedure*, since it makes m or less comparisons, while the number of all intersections of null hypotheses to be tested is of order $2^{m}$ . It controls the FWER in the strong sense.

In the Holm–Bonferroni procedure, we first test $H_{(1)}$ . If it is not rejected then the intersection of all null hypotheses $\bigcap \nolimits _{i=1}^{m}H_{i}$ is not rejected too, such that there exists at least one intersection hypothesis for each of elementary hypotheses $H_{1},\ldots ,H_{m}$ that is not rejected, thus we reject none of the elementary hypotheses.

If $H_{(1)}$ is rejected at level $\alpha /m$ then all the intersection sub-families that contain it are rejected too, thus $H_{(1)}$ is rejected. This is because $P_{(1)}$ is the smallest in each one of the intersection sub-families and the size of the sub-families is at most m , such that the Bonferroni threshold larger than $\alpha /m$ .

The same rationale applies for $H_{(2)}$ . However, since $H_{(1)}$ already rejected, it sufficient to reject all the intersection sub-families of $H_{(2)}$ without $H_{(1)}$ . Once $P_{(2)}\leq \alpha /(m-1)$ holds all the intersections that contains $H_{(2)}$ are rejected.

The same applies for each $1\leq i\leq m$ .

## Example

Consider four null hypotheses $H_{1},\ldots ,H_{4}$ with unadjusted p-values $p_{1}=0.01$ , $p_{2}=0.04$ , $p_{3}=0.03$ and $p_{4}=0.005$ , to be tested at significance level $\alpha =0.05$ . Since the procedure is step-down, we first test $H_{4}=H_{(1)}$ , which has the smallest p-value $p_{4}=p_{(1)}=0.005$ . The p-value is compared to $\alpha /4=0.0125$ , the null hypothesis is rejected and we continue to the next one. Since $p_{1}=p_{(2)}=0.01<0.0167=\alpha /3$ we reject $H_{1}=H_{(2)}$ as well and continue. The next hypothesis $H_{3}$ is not rejected since $p_{3}=p_{(3)}=0.03>0.025=\alpha /2$ . We stop testing and conclude that $H_{1}$ and $H_{4}$ are rejected and $H_{2}$ and $H_{3}$ are not rejected while controlling the family-wise error rate at level $\alpha =0.05$ . Note that even though $p_{2}=p_{(4)}=0.04<0.05=\alpha$ applies, $H_{2}$ is **not** rejected. This is because the testing procedure stops once a failure to reject occurs.

## Extensions

### Holm–Šidák method

When the hypothesis tests are not negatively dependent, it is possible to replace ${\frac {\alpha }{m}},{\frac {\alpha }{m-1}},\ldots ,{\frac {\alpha }{1}}$ with:

$1-(1-\alpha )^{1/m},1-(1-\alpha )^{1/(m-1)},\ldots ,1-(1-\alpha )^{1}$

resulting in a slightly more powerful test.

### Weighted version

Let $P_{(1)},\ldots ,P_{(m)}$ be the ordered unadjusted p-values. Let $H_{(i)}$ , $0\leq w_{(i)}$ correspond to $P_{(i)}$ . Reject $H_{(i)}$ as long as

$P_{(j)}\leq {\frac {w_{(j)}}{\sum _{k=j}^{m}w_{(k)}}}\alpha ,\quad j=1,\ldots ,i$

### Adjusted *p*-values

The adjusted *p*-values for Holm–Bonferroni method are:

${\widetilde {p}}_{(i)}=\max _{j\leq i}\left\{(m-j+1)p_{(j)}\right\}_{1},{\text{ where }}\{x\}_{1}\equiv \min(x,1).$

In the earlier example, the adjusted *p*-values are ${\widetilde {p}}_{1}=0.03$ , ${\widetilde {p}}_{2}=0.06$ , ${\widetilde {p}}_{3}=0.06$ and ${\widetilde {p}}_{4}=0.02$ . Only hypotheses $H_{1}$ and $H_{4}$ are rejected at level $\alpha =0.05$ .

Similar adjusted *p*-values for Holm-Šidák method can be defined recursively as ${\widetilde {p}}_{(i)}=\max \left\{{\widetilde {p}}_{(i-1)},1-(1-p_{(i)})^{m-i+1}\right\}$ , where ${\widetilde {p}}_{(1)}=1-(1-p_{(1)})^{m}$ . Due to the inequality $1-(1-\alpha )^{1/n}<\alpha /n$ for $n\geq 2$ , the Holm-Šidák method will be more powerful than Holm–Bonferroni method.

The weighted adjusted *p*-values are:

${\widetilde {p}}_{(i)}=\max _{j\leq i}\left\{{\frac {\sum _{k=j}^{m}{w_{(k)}}}{w_{(j)}}}p_{(j)}\right\}_{1},{\text{ where }}\{x\}_{1}\equiv \min(x,1).$

A hypothesis is rejected at level α if and only if its adjusted *p*-value is less than α. In the earlier example using equal weights, the adjusted *p*-values are 0.03, 0.06, 0.06, and 0.02. This is another way to see that using α = 0.05, only hypotheses one and four are rejected by this procedure.

## Alternatives and usage

The Holm–Bonferroni method is "uniformly" more powerful than the classic Bonferroni correction, meaning that it is always at least as powerful.

There are other methods for controlling the FWER that are more powerful than Holm–Bonferroni. For instance, in the Hochberg procedure, rejection of $H_{(1)}\ldots H_{(k)}$ is made after finding the *maximal* index k such that $P_{(k)}\leq {\frac {\alpha }{m+1-k}}$ . Thus, The Hochberg procedure is uniformly more powerful than the Holm procedure. However, the Hochberg procedure requires the hypotheses to be independent or under certain forms of positive dependence, whereas Holm–Bonferroni can be applied without such assumptions. A similar step-up procedure is the Hommel procedure, which is uniformly more powerful than the Hochberg procedure.

## Naming

Carlo Emilio Bonferroni did not take part in inventing the method described here. Holm originally called the method the "sequentially rejective Bonferroni test", and it became known as Holm–Bonferroni only after some time. Holm's motives for naming his method after Bonferroni are explained in the original paper: "The use of the Boole inequality within multiple inference theory is usually called the Bonferroni technique, and for this reason we will call our test the sequentially rejective Bonferroni test."
