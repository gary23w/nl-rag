---
title: "Geometric Brownian motion"
source: https://en.wikipedia.org/wiki/Geometric_Brownian_motion
domain: brownian-motion
license: CC-BY-SA-4.0
tags: brownian motion, diffusion process, fokker-planck equation, ornstein-uhlenbeck process
fetched: 2026-07-02
---

# Geometric Brownian motion

A **geometric Brownian motion** (**GBM**), also known as an **exponential Brownian motion**, is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion with drift. It is an important example of stochastic processes satisfying a stochastic differential equation (SDE); in particular, it is used in mathematical finance to model stock prices in the Black–Scholes model.

## Stochastical differential equation

A stochastic process *S**t* is said to follow a GBM if it satisfies the following stochastic differential equation (SDE):

$dS_{t}=\mu S_{t}\,dt+\sigma S_{t}\,dW_{t}$

where $W_{t}$ is a Wiener process or Brownian motion, and $\mu$ ('the percentage drift') and $\sigma$ ('the percentage volatility') are constants.

The former parameter is used to model deterministic trends, while the latter parameter models unpredictable events occurring during the motion.

### Solution

For an arbitrary initial value *S*0 the above SDE has the analytic solution (under Itô's interpretation):

$S_{t}=S_{0}\exp \left(\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}\right).$

The derivation requires the use of Itô calculus. Applying Itô's formula leads to

$d(\ln S_{t})=(\ln S_{t})'dS_{t}+{\frac {1}{2}}(\ln S_{t})''\,dS_{t}\,dS_{t}={\frac {dS_{t}}{S_{t}}}-{\frac {1}{2}}\,{\frac {1}{S_{t}^{2}}}\,dS_{t}\,dS_{t}$

where $dS_{t}\,dS_{t}$ is the quadratic variation of the SDE.

$dS_{t}\,dS_{t}\,=\,\sigma ^{2}\,S_{t}^{2}\,dW_{t}^{2}+2\sigma S_{t}^{2}\mu \,dW_{t}\,dt+\mu ^{2}S_{t}^{2}\,dt^{2}$

When $dt\to 0$ , $dt$ converges to 0 faster than $dW_{t}$ , since $dW_{t}^{2}=O(dt)$ . So the above infinitesimal can be simplified by

$dS_{t}\,dS_{t}\,=\,\sigma ^{2}\,S_{t}^{2}\,dt$

Plugging the value of $dS_{t}$ in the above equation and simplifying we obtain

$\ln {\frac {S_{t}}{S_{0}}}=\left(\mu -{\frac {\sigma ^{2}}{2}}\,\right)t+\sigma W_{t}\,.$

Taking the exponential and multiplying both sides by $S_{0}$ gives the solution claimed above.

## Arithmetic Brownian motion

The process for $X_{t}=\ln {\frac {S_{t}}{S_{0}}}$ , satisfying the SDE

$dX_{t}=\left(\mu -{\frac {\sigma ^{2}}{2}}\,\right)dt+\sigma dW_{t}\,,$

or more generally the process solving the SDE

$dX_{t}=m\,dt+v\,dW_{t}\,,$

where m and $v>0$ are real constants and for an initial condition $X_{0}$ , is called an Arithmetic Brownian Motion (ABM). This was the model postulated by Louis Bachelier in 1900 for stock prices, in the first published attempt to model Brownian motion, known today as Bachelier model. As was shown above, the ABM SDE can be obtained through the logarithm of a GBM via Itô's formula. Similarly, a GBM can be obtained by exponentiation of an ABM through Itô's formula.

## Properties

The above solution $S_{t}$ (for any value of t) is a log-normally distributed random variable with expected value and variance given by

$\operatorname {E} (S_{t})=S_{0}e^{\mu t},$

$\operatorname {Var} (S_{t})=S_{0}^{2}e^{2\mu t}\left(e^{\sigma ^{2}t}-1\right).$

They can be derived using the fact that $Z_{t}=\exp \left(\sigma W_{t}-{\frac {1}{2}}\sigma ^{2}t\right)$ is a martingale, and that

$\operatorname {E} \left[\exp \left(2\sigma W_{t}-\sigma ^{2}t\right)\mid {\mathcal {F}}_{s}\right]=e^{\sigma ^{2}(t-s)}\exp \left(2\sigma W_{s}-\sigma ^{2}s\right),\quad \forall 0\leq s<t.$

The probability density function of $S_{t}$ is:

$f_{S_{t}}(s;\mu ,\sigma ,t)={\frac {1}{\sqrt {2\pi }}}\,{\frac {1}{s\sigma {\sqrt {t}}}}\,\exp \left(-{\frac {\left(\ln s-\ln S_{0}-\left(\mu -{\frac {1}{2}}\sigma ^{2}\right)t\right)^{2}}{2\sigma ^{2}t}}\right).$

| Derivation of GBM probability density function |
|---|
| To derive the probability density function for GBM, we must use the Fokker–Planck equation to evaluate the time evolution of the PDF: ${\partial p \over {\partial t}}=-{\partial \over {\partial S}}[\mu Sp(t,S)]+{1 \over {2}}{\partial ^{2} \over {\partial S^{2}}}[\sigma ^{2}S^{2}p(t,S)],\quad p(0,S)=\delta (S-S_{0})$ where $\delta (S)$ is the Dirac delta function. To simplify the computation, we may introduce a logarithmic transform $x=\log(S/S_{0})$ , leading to the form of GBM: $dx=\left(\mu -{1 \over {2}}\sigma ^{2}\right)dt+\sigma \,dW$ Then the equivalent Fokker–Planck equation for the evolution of the PDF becomes: ${\partial p \over {\partial t}}+\left(\mu -{1 \over {2}}\sigma ^{2}\right){\partial p \over {\partial x}}={1 \over {2}}\sigma ^{2}{\partial ^{2}p \over {\partial x^{2}}},\quad p(0,x)=\delta (x)$ Define $V=\mu -\sigma ^{2}/2$ and $D=\sigma ^{2}/2$ . By introducing the new variables $\xi =x-Vt$ and $\tau =Dt$ , the derivatives in the Fokker–Planck equation may be transformed as: ${\begin{aligned}\partial _{t}p&=D\partial _{\tau }p-V\partial _{\xi }p\\\partial _{x}p&=\partial _{\xi }p\\\partial _{x}^{2}p&=\partial _{\xi }^{2}p\end{aligned}}$ Leading to the new form of the Fokker–Planck equation: ${\partial p \over {\partial \tau }}={\partial ^{2}p \over {\partial \xi ^{2}}},\quad p(0,\xi )=\delta (\xi )$ However, this is the canonical form of the heat equation. which has the solution given by the heat kernel: $p(\tau ,\xi )={1 \over {\sqrt {4\pi \tau }}}\exp \left(-{\xi ^{2} \over 4\tau }\right)$ Plugging in the original variables leads to the PDF for GBM: $p(t,S)={1 \over {S{\sqrt {2\pi \sigma ^{2}t}}}}\exp \left\{-{\left[\log(S/S_{0})-\left(\mu -{1 \over 2}\sigma ^{2}\right)t\right]^{2} \over {2\sigma ^{2}t}}\right\}$ |

When deriving further properties of GBM, use can be made of the SDE of which GBM is the solution, or the explicit solution given above can be used. For example, consider the stochastic process log(*S**t*). This is an interesting process, because in the Black–Scholes model it is related to the log return of the stock price. Using Itô's lemma with *f*(*S*) = log(*S*) gives

${\begin{alignedat}{2}d\log(S)&=f'(S)\,dS+{\frac {1}{2}}f''(S)S^{2}\sigma ^{2}\,dt\\[6pt]&={\frac {1}{S}}\left(\sigma S\,dW_{t}+\mu S\,dt\right)-{\frac {1}{2}}\sigma ^{2}\,dt\\[6pt]&=\sigma \,dW_{t}+(\mu -\sigma ^{2}/2)\,dt.\end{alignedat}}$

It follows that $\operatorname {E} \log(S_{t})=\log(S_{0})+(\mu -\sigma ^{2}/2)t$ .

This result can also be derived by applying the logarithm to the explicit solution of GBM:

${\begin{alignedat}{2}\log(S_{t})&=\log \left(S_{0}\exp \left(\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}\right)\right)\\[6pt]&=\log(S_{0})+\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}.\end{alignedat}}$

Taking the expectation yields the same result as above: $\operatorname {E} \log(S_{t})=\log(S_{0})+(\mu -\sigma ^{2}/2)t$ .

## Multivariate version

GBM can be extended to the case where there are multiple correlated price paths.

Each price path follows the underlying process

$dS_{t}^{i}=\mu _{i}S_{t}^{i}\,dt+\sigma _{i}S_{t}^{i}\,dW_{t}^{i},$

where the Wiener processes are correlated such that $\operatorname {E} (dW_{t}^{i}\,dW_{t}^{j})=\rho _{i,j}\,dt$ where $\rho _{i,i}=1$ .

For the multivariate case, this implies that

$\operatorname {Cov} (S_{t}^{i},S_{t}^{j})=S_{0}^{i}S_{0}^{j}e^{(\mu _{i}+\mu _{j})t}\left(e^{\rho _{i,j}\sigma _{i}\sigma _{j}t}-1\right).$

A multivariate formulation that maintains the driving Brownian motions $W_{t}^{i}$ independent is

$dS_{t}^{i}=\mu _{i}S_{t}^{i}\,dt+\sum _{j=1}^{d}\sigma _{i,j}S_{t}^{i}\,dW_{t}^{j},$

where the correlation between $S_{t}^{i}$ and $S_{t}^{j}$ is now expressed through the $\sigma _{i,j}=\rho _{i,j}\,\sigma _{i}\,\sigma _{j}$ terms.

## Use in finance

Geometric Brownian motion is used to model stock prices in the Black–Scholes model and is the most widely used model of stock price behavior.

Some of the arguments for using GBM to model stock prices are:

- The expected returns of GBM are independent of the value of the process (stock price), which agrees with what we would expect in reality.
- A GBM process only assumes positive values, just like real stock prices.
- A GBM process shows the same kind of 'roughness' in its paths as we see in real stock prices.
- Calculations with GBM processes are relatively easy.

However, GBM is not a completely realistic model, in particular it falls short of reality in the following points:

- In real stock prices, volatility changes over time (possibly stochastically), but in GBM, volatility is assumed constant.
- In real life, stock prices often show jumps caused by unpredictable events or news, but in GBM, the path is continuous (no discontinuity).

Apart from modeling stock prices, Geometric Brownian motion has also found applications in the monitoring of trading strategies.

## Extensions

In an attempt to make GBM more realistic as a model for stock prices, also in relation to the volatility smile problem, one can drop the assumption that the volatility ( $\sigma$ ) is constant. If we assume that the volatility is a deterministic function of the stock price and time, this is called a local volatility model. A straightforward extension of the Black Scholes GBM is a local volatility SDE whose distribution is a mixture of distributions of GBM, the lognormal mixture dynamics, resulting in a convex combination of Black Scholes prices for options. If instead we assume that the volatility has a randomness of its own—often described by a different equation driven by a different Brownian Motion—the model is called a stochastic volatility model, see for example the Heston model.
