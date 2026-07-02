---
title: "Black–Scholes model"
source: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model
domain: quantitative-finance
license: CC-BY-SA-4.0
tags: quantitative finance, mathematical finance, financial modeling, derivatives pricing
fetched: 2026-07-02
---

# Black–Scholes model

The **Black–Scholes** /ˌblæk ˈʃoʊlz/ or **Black–Scholes–Merton model** is a mathematical model for the dynamics of a financial market containing derivative investment instruments. From the parabolic partial differential equation in the model, known as the Black–Scholes equation, one can deduce the **Black–Scholes formula**, which gives a theoretical estimate of the price of European-style options and shows that the option has a *unique* price given the risk of the security and its expected return (instead replacing the security's expected return with the risk-neutral rate). The equation and model are named after economists Fischer Black and Myron Scholes. Robert C. Merton, who first wrote an academic paper on the subject, is sometimes also credited.

The main principle behind the model is to hedge the option by buying and selling the underlying asset in a specific way to eliminate risk. This type of hedging is called "continuously revised delta hedging" and is the basis of more complicated hedging strategies such as those used by investment banks and hedge funds.

The model is widely used, although often with some adjustments, by options market participants. The model's assumptions have been relaxed and generalized in many directions, leading to a plethora of models that are currently used in derivative pricing and risk management. The insights of the model, as exemplified by the Black–Scholes formula, are frequently used by market participants, as distinguished from the actual prices. These insights include no-arbitrage bounds and risk-neutral pricing (thanks to continuous revision). Further, the Black–Scholes equation, a partial differential equation that governs the price of the option, enables pricing using numerical methods when an explicit formula is not possible.

The Black–Scholes formula has only one parameter that cannot be directly observed in the market: the average future volatility of the underlying asset, though it can be found from the price of other options. Since the option value (whether put or call) is increasing in this parameter, it can be inverted to produce a "volatility surface" that is then used to calibrate other models, e.g., for OTC derivatives.

## History

Louis Bachelier's thesis in 1900 was the earliest publication to apply Brownian motion to derivative pricing, though his work had little impact for many years and included important limitations for its application to modern markets. In the 1960's Case Sprenkle, James Boness, Paul Samuelson, and Samuelson's Ph.D. student at the time Robert C. Merton all made important improvements to the theory of options pricing.

Fischer Black and Myron Scholes demonstrated in 1968 that a dynamic revision of a portfolio removes the expected return of the security, thus inventing the *risk neutral argument*. They based their thinking on work previously done by market researchers and practitioners including the work mentioned above, as well as work by Sheen Kassouf and Edward O. Thorp. Black and Scholes then attempted to apply the formula to the markets, but incurred financial losses, due to a lack of risk management in their trades. In 1970, they decided to return to the academic environment. After three years of efforts, the formula—named in honor of them for making it public—was finally published in 1973 in an article titled "The Pricing of Options and Corporate Liabilities", in the *Journal of Political Economy*. Robert C. Merton was the first to publish a paper expanding the mathematical understanding of the options pricing model, and coined the term "Black–Scholes options pricing model".

The formula led to a boom in options trading and provided mathematical legitimacy to the activities of options trading, led by Cboe Global Markets.

Merton and Scholes received the 1997 Nobel Memorial Prize in Economic Sciences for their work, the committee citing their discovery of the risk neutral dynamic revision as a breakthrough that separates the option from the risk of the underlying security. Although ineligible for the prize because of his death in 1995, Black was mentioned as a contributor by the Swedish Academy.

## Fundamental hypotheses

The Black–Scholes model assumes that the market consists of at least one risky asset, usually called the stock, and one riskless asset, usually called the money market, cash, or bond.

The following assumptions are made about the assets (which relate to the names of the assets):

- Risk-free rate: The rate of return on the riskless asset is constant and thus called the risk-free interest rate.
- Random walk: The instantaneous log return of the stock price is an infinitesimal random walk with drift; more precisely, the stock price follows a geometric Brownian motion, and it is assumed that the drift and volatility of the motion are constant. If drift and volatility are time-varying, a suitably modified Black–Scholes formula can be deduced, as long as the volatility is not random.
- The stock does not pay a dividend.

The assumptions about the market are:

- No arbitrage opportunity (i.e., there is no way to make a riskless profit in excess of the risk-free rate).
- Ability to borrow and lend any amount, even fractional, of cash at the riskless rate.
- Ability to buy and sell any amount, even fractional, of the stock (this includes short selling).
- The above transactions do not incur any fees or costs (i.e., frictionless market).

With these assumptions, suppose there is a derivative security also trading in this market. It is specified that this security will have a certain payoff on a specified future date, depending on the values of the stock up to that date. Even though the path the stock price will take in the future is unknown, the derivative's price can be determined at the current time. For the special case of a European call or put option, Black and Scholes showed that "it is possible to create a hedged position, consisting of a long position in the stock and a short position in the option, whose value will not depend on the price of the stock". Their dynamic hedging strategy led to a partial differential equation which governs the price of the option. Its solution is given by the Black–Scholes formula.

Several of these assumptions of the original model have been removed in subsequent extensions of the model. Modern versions account for dynamic interest rates (Merton, 1976), transaction costs and taxes (Ingersoll, 1976), and dividend payout.

## Notation

At time *t,* in particular:

$C(S,t)$

is the price of a European call option and

$P(S,t)$

is the price of a European put option.

T

is the time of option expiration.

$\tau$

is the time until maturity:

$\tau =T-t$

.

K

is the

strike price

of the option, also known as the exercise price.

$N(x)$ denotes the standard normal cumulative distribution function:

$N(x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{-z^{2}/2}\,dz.$

$N'(x)$ denotes the standard normal probability density function:

$N'(x)={\frac {dN(x)}{dx}}={\frac {1}{\sqrt {2\pi }}}e^{-x^{2}/2}.$

## Black–Scholes equation

The Black–Scholes equation is a parabolic partial differential equation that describes the price $V(S,t)$ of the option, where S is the price of the underlying asset and t is time:

${\frac {\partial V}{\partial t}}+{\frac {1}{2}}\sigma ^{2}S^{2}{\frac {\partial ^{2}V}{\partial S^{2}}}+rS{\frac {\partial V}{\partial S}}-rV=0$

A key financial insight behind the equation is that one can perfectly hedge the option by buying and selling the underlying asset and the bank account asset (cash) in such a way as to "eliminate risk". This implies that there is a unique price for the option given by the Black–Scholes formula (see the next section).

## Black–Scholes formula

The Black–Scholes formula calculates the price of European put and call options. This price is consistent with the Black–Scholes equation. This follows since the formula can be obtained by solving the equation for the corresponding terminal and boundary conditions:

${\begin{aligned}C(0,t)&=0{\text{ for all }}t\\C(S,t)&\sim S-Ke^{-r(T-t)}{\text{ as }}S\rightarrow \infty \\C(S,T)&=\max\{S-K,0\}\end{aligned}}$

The value of a call option for a non-dividend-paying underlying stock in terms of the Black–Scholes parameters is:

${\begin{aligned}C(S_{t},t)&=N(d_{+})S_{t}-N(d_{-})Ke^{-r(T-t)}\\d_{+}&={\frac {1}{\sigma {\sqrt {T-t}}}}\left[\ln \left({\frac {S_{t}}{K}}\right)+\left(r+{\frac {\sigma ^{2}}{2}}\right)(T-t)\right]\\d_{-}&=d_{+}-\sigma {\sqrt {T-t}}\\\end{aligned}}$

The price of a corresponding put option based on put–call parity with discount factor $e^{-r(T-t)}$ is:

${\begin{aligned}P(S_{t},t)&=Ke^{-r(T-t)}-S_{t}+C(S_{t},t)\\&=N(-d_{-})Ke^{-r(T-t)}-N(-d_{+})S_{t}\end{aligned}}\,$

### Alternative formulation

Introducing auxiliary variables allows for the formula to be simplified and reformulated in a form that can be more convenient (this is a special case of the Black '76 formula):

${\begin{aligned}C(F,\tau )&=D\left[N(d_{+})F-N(d_{-})K\right]\\d_{+}&={\frac {1}{\sigma {\sqrt {\tau }}}}\left[\ln \left({\frac {F}{K}}\right)+{\frac {1}{2}}\sigma ^{2}\tau \right]\\d_{-}&=d_{+}-\sigma {\sqrt {\tau }}\end{aligned}}$

where:

$D=e^{-r\tau }$ is the discount factor

$F=e^{r\tau }S={\frac {S}{D}}$ is the forward price of the underlying asset, and $S=DF$

Given put–call parity, which is expressed in these terms as:

$C-P=D(F-K)=S-DK$

the price of a put option is:

$P(F,\tau )=D\left[N(-d_{-})K-N(-d_{+})F\right]$

### Interpretation

It is possible to have intuitive interpretations of the Black–Scholes formula, with the main subtlety being the interpretation of $d_{\pm }$ and why there are two different terms.

The formula can be interpreted by first decomposing a call option into the difference of two binary options: an asset-or-nothing call minus a cash-or-nothing call (long an asset-or-nothing call, short a cash-or-nothing call). A call option exchanges cash for an asset at expiry, while an asset-or-nothing call just yields the asset (with no cash in exchange) and a cash-or-nothing call just yields cash (with no asset in exchange). The Black–Scholes formula is a difference of two terms, and these two terms are equal to the values of the binary call options. These binary options are less frequently traded than vanilla call options, but are easier to analyze.

Thus the formula:

$C=D\left[N(d_{+})F-N(d_{-})K\right]$

breaks up as:

$C=DN(d_{+})F-DN(d_{-})K,$

where $DN(d_{+})F$ is the present value of an asset-or-nothing call and $DN(d_{-})K$ is the present value of a cash-or-nothing call. The *D* factor is for discounting, because the expiration date is in future, and removing it changes *present* value to *future* value (value at expiry). Thus $N(d_{+})~F$ is the future value of an asset-or-nothing call and $N(d_{-})~K$ is the future value of a cash-or-nothing call. In risk-neutral terms, these are the expected value of the asset and the expected value of the cash in the risk-neutral measure.

A naive, and slightly incorrect, interpretation of these terms is that $N(d_{+})F$ is the probability of the option expiring in the money $N(d_{+})$ , multiplied by the value of the underlying at expiry *F,* while $N(d_{-})K$ is the probability of the option expiring in the money $N(d_{-}),$ multiplied by the value of the cash at expiry *K.* This interpretation is incorrect because either both binaries expire in the money or both expire out of the money (either cash is exchanged for the asset or it is not), but the probabilities $N(d_{+})$ and $N(d_{-})$ are not equal. In fact, $d_{\pm }$ can be interpreted as measures of moneyness (in standard deviations) and $N(d_{\pm })$ as probabilities of expiring ITM (*percent moneyness*), in the respective numéraire, as discussed below. Simply put, the interpretation of the cash option, $N(d_{-})K$ , is correct, as the value of the cash is independent of movements of the underlying asset, and thus can be interpreted as a simple product of "probability times value", while the $N(d_{+})F$ is more complicated, as the probability of expiring in the money and the value of the asset at expiry are not independent. More precisely, the value of the asset at expiry is variable in terms of cash, but is constant in terms of the asset itself (a fixed quantity of the asset), and thus these quantities are independent if one changes numéraire to the asset rather than cash.

If one uses spot *S* instead of forward *F,* in $d_{\pm }$ instead of the ${\textstyle {\frac {1}{2}}\sigma ^{2}}$ term there is ${\textstyle \left(r\pm {\frac {1}{2}}\sigma ^{2}\right)\tau ,}$ which can be interpreted as a drift factor (in the risk-neutral measure for appropriate numéraire). The use of *d*− for moneyness rather than the standardized moneyness ${\textstyle m={\frac {1}{\sigma {\sqrt {\tau }}}}\ln \left({\frac {F}{K}}\right)}$  – in other words, the reason for the ${\textstyle {\frac {1}{2}}\sigma ^{2}}$ factor – is due to the difference between the median and mean of the log-normal distribution; it is the same factor as in Itō's lemma applied to geometric Brownian motion. In addition, another way to see that the naive interpretation is incorrect is that replacing $N(d_{+})$ by $N(d_{-})$ in the formula yields a negative value for out-of-the-money call options.

In detail, the terms $N(d_{+}),N(d_{-})$ are the *probabilities of the option expiring in-the-money* under the equivalent exponential martingale probability measure (numéraire=stock) and the equivalent martingale probability measure (numéraire=risk free asset), respectively. The risk neutral probability density for the stock price $S_{T}\in (0,\infty )$ is

$p(S,T)={\frac {N^{\prime }[d_{-}(S_{T})]}{S_{T}\sigma {\sqrt {T}}}}$

where $d_{-}=d_{-}(K)$ is defined as above.

Specifically, $N(d_{-})$ is the probability that the call will be exercised provided one assumes that the asset drift is the risk-free rate. $N(d_{+})$ , however, does not lend itself to a simple probability interpretation. $SN(d_{+})$ is correctly interpreted as the present value, using the risk-free interest rate, of the expected asset price at expiration, given that the asset price at expiration is above the exercise price. For related discussion – and graphical representation – see Datar–Mathews method for real option valuation.

The equivalent martingale probability measure is also called the risk-neutral probability measure. Note that both of these are *probabilities* in a measure theoretic sense, and neither of these is the true probability of expiring in-the-money under the real probability measure. To calculate the probability under the real ("physical") probability measure, additional information is required—the drift term in the physical measure, or equivalently, the market price of risk.

#### Derivations

A standard derivation for solving the Black–Scholes PDE is given in the article Black–Scholes equation.

The Feynman–Kac formula says that the solution to this type of PDE, when discounted appropriately, is actually a martingale. Thus the option price is the expected value of the discounted payoff of the option. Computing the option price via this expectation is the risk neutrality approach and can be done without knowledge of PDEs. Note the expectation of the option payoff is not done under the real world probability measure, but an artificial risk-neutral measure, which differs from the real world measure. For the underlying logic see section "risk neutral valuation" under Rational pricing as well as section "Derivatives pricing: the Q world" under Mathematical finance; for details, once again, see Hull.

## The Options Greeks

"The Greeks" measure the sensitivity of the value of a derivative product or a financial portfolio to changes in parameter values while holding the other parameters fixed. They are partial derivatives of the price with respect to the parameter values. One Greek, "gamma" (as well as others not listed here) is a partial derivative of another Greek, "delta" in this case.

The Greeks are important not only in the mathematical theory of finance, but also for those actively trading. Financial institutions will typically set (risk) limit values for each of the Greeks that their traders must not exceed.

Delta is the most important Greek since this usually confers the largest risk. Many traders will zero their delta at the end of the day if they are not speculating on the direction of the market and following a delta-neutral hedging approach as defined by Black–Scholes. When a trader seeks to establish an effective delta-hedge for a portfolio, the trader may also seek to neutralize the portfolio's gamma, as this will ensure that the hedge will be effective over a wider range of underlying price movements.

The Greeks for Black–Scholes are given in closed form below. They can be obtained by differentiation of the Black–Scholes formula.

|   | Call | Put |   |
|---|---|---|---|
| Delta | ${\frac {\partial V}{\partial S}}$ | $N(d_{+})\,$ | $-N(-d_{+})=N(d_{+})-1\,$ |
| Gamma | ${\frac {\partial ^{2}V}{\partial S^{2}}}$ | ${\frac {N'(d_{+})}{S\sigma {\sqrt {T-t}}}}\,$ |   |
| Vega | ${\frac {\partial V}{\partial \sigma }}$ | $SN'(d_{+}){\sqrt {T-t}}\,$ |   |
| Theta | ${\frac {\partial V}{\partial t}}$ | $-{\frac {SN'(d_{+})\sigma }{2{\sqrt {T-t}}}}-rKe^{-r(T-t)}N(d_{-})\,$ | $-{\frac {SN'(d_{+})\sigma }{2{\sqrt {T-t}}}}+rKe^{-r(T-t)}N(-d_{-})\,$ |
| Rho | ${\frac {\partial V}{\partial r}}$ | $K(T-t)e^{-r(T-t)}N(d_{-})\,$ | $-K(T-t)e^{-r(T-t)}N(-d_{-})\,$ |

Note that the gamma and vega are the same value for calls and puts. This can be seen directly from put–call parity, since the difference of a put and a call is a forward, which is linear in *S* and independent of *σ* (so a forward has zero gamma and zero vega).

In practice, some sensitivities are usually quoted in scaled-down terms, to match the scale of likely changes in the parameters. For example, rho is often reported divided by 10,000 (1 basis point rate change), vega by 100 (1 vol point change), and theta by 365 or 252 (1 day decay based on either calendar days or trading days per year).

Note that "Vega" is not a letter in the Greek alphabet; the name arises from misreading the Greek letter nu (variously rendered as $\nu$ , ν, and ν) as a V.

## Extensions of the model

The above model can be extended for variable (but deterministic) rates and volatilities. The model may also be used to value European options on instruments paying dividends. In this case, closed-form solutions are available if the dividend is a known proportion of the stock price. American options and options on stocks paying a known cash dividend (in the short term, more realistic than a proportional dividend) are more difficult to value, and a choice of solution techniques is available (for example lattices and grids).

### Instruments paying continuous yield dividends

For options on indices, it is reasonable to make the simplifying assumption that dividends are paid continuously, and that the dividend amount is proportional to the level of the index.

The dividend payment paid over the time period $[t,t+dt]$ is then modelled as:

$qS_{t}\,dt$

for some constant q (the dividend yield).

Under this formulation the arbitrage-free price implied by the Black–Scholes model can be shown to be:

$C(S_{t},t)=e^{-r(T-t)}[FN(d_{1})-KN(d_{2})]\,$

and

$P(S_{t},t)=e^{-r(T-t)}[KN(-d_{2})-FN(-d_{1})]\,$

where now

$F=S_{t}e^{(r-q)(T-t)}\,$

is the modified forward price that occurs in the terms $d_{1},d_{2}$ :

$d_{1}={\frac {1}{\sigma {\sqrt {T-t}}}}\left[\ln \left({\frac {S_{t}}{K}}\right)+\left(r-q+{\frac {1}{2}}\sigma ^{2}\right)(T-t)\right]$

and

$d_{2}=d_{1}-\sigma {\sqrt {T-t}}={\frac {1}{\sigma {\sqrt {T-t}}}}\left[\ln \left({\frac {S_{t}}{K}}\right)+\left(r-q-{\frac {1}{2}}\sigma ^{2}\right)(T-t)\right]$

.

### Instruments paying discrete proportional dividends

It is also possible to extend the Black–Scholes framework to options on instruments paying discrete proportional dividends. This is useful when the option is struck on a single stock.

A typical model is to assume that a proportion $\delta$ of the stock price is paid out at pre-determined times $t_{1},t_{2},\ldots ,t_{n}$ . The price of the stock is then modelled as:

$S_{t}=S_{0}(1-\delta )^{n(t)}e^{ut+\sigma W_{t}}$

where $n(t)$ is the number of dividends that have been paid by time t .

The price of a call option on such a stock is again:

$C(S_{0},T)=e^{-rT}[FN(d_{1})-KN(d_{2})]\,$

where now

$F=S_{0}(1-\delta )^{n(T)}e^{rT}\,$

is the forward price for the dividend paying stock.

### American options

The problem of finding the price of an American option is related to the optimal stopping problem of finding the time to execute the option. Since the American option can be exercised at any time before the expiration date, the Black–Scholes equation becomes a variational inequality of the form:

${\frac {\partial V}{\partial t}}+{\frac {1}{2}}\sigma ^{2}S^{2}{\frac {\partial ^{2}V}{\partial S^{2}}}+rS{\frac {\partial V}{\partial S}}-rV\leq 0$

together with $V(S,t)\geq H(S)$ where $H(S)$ denotes the payoff at stock price S and the terminal condition: $V(S,T)=H(S)$ .

In general this inequality does not have a closed form solution, though an American call with no dividends is equal to a European call and the Roll–Geske–Whaley method provides a solution for an American call with one dividend; see also Black's approximation.

Barone-Adesi and Whaley is a further approximation formula. Here, the stochastic differential equation (which is valid for the value of any derivative) is split into two components: the European option value and the early exercise premium. With some assumptions, a quadratic equation that approximates the solution for the latter is then obtained. This solution involves finding the critical value, $s*$ , such that one is indifferent between early exercise and holding to maturity.

Bjerksund and Stensland provide an approximation based on an exercise strategy corresponding to a trigger price. Here, if the underlying asset price is greater than or equal to the trigger price it is optimal to exercise, and the value must equal $S-X$ , otherwise the option "boils down to: (i) a European up-and-out call option... and (ii) a rebate that is received at the knock-out date if the option is knocked out prior to the maturity date". The formula is readily modified for the valuation of a put option, using put–call parity. This approximation is computationally inexpensive and the method is fast, with evidence indicating that the approximation may be more accurate in pricing long dated options than Barone-Adesi and Whaley.

#### Perpetual put

Despite the lack of a general analytical solution for American put options, it is possible to derive such a formula for the case of a perpetual option – meaning that the option never expires (i.e., $T\rightarrow \infty$ ). In this case, the time decay of the option is equal to zero, which leads to the Black–Scholes PDE becoming an ODE: ${1 \over {2}}\sigma ^{2}S^{2}{d^{2}V \over {dS^{2}}}+(r-q)S{dV \over {dS}}-rV=0$ Let $S_{-}$ denote the lower exercise boundary, below which it is optimal to exercise the option. The boundary conditions are: $V(S_{-})=K-S_{-},\quad {dV \over {dS}}(S_{-})=-1,\quad V(S)\leq K$ The solutions to the ODE are a linear combination of any two linearly independent solutions: $V(S)=A_{1}S^{\lambda _{1}}+A_{2}S^{\lambda _{2}}$ For $S_{-}\leq S$ , substitution of this solution into the ODE for $i={1,2}$ yields: $\left[{1 \over {2}}\sigma ^{2}\lambda _{i}(\lambda _{i}-1)+(r-q)\lambda _{i}-r\right]S^{\lambda _{i}}=0$ Rearranging the terms gives: ${1 \over {2}}\sigma ^{2}\lambda _{i}^{2}+\left(r-q-{1 \over {2}}\sigma ^{2}\right)\lambda _{i}-r=0$ Using the quadratic formula, the solutions for $\lambda _{i}$ are: ${\begin{aligned}\lambda _{1}&={-\left(r-q-{1 \over {2}}\sigma ^{2}\right)+{\sqrt {\left(r-q-{1 \over {2}}\sigma ^{2}\right)^{2}+2\sigma ^{2}r}} \over {\sigma ^{2}}}\\\lambda _{2}&={-\left(r-q-{1 \over {2}}\sigma ^{2}\right)-{\sqrt {\left(r-q-{1 \over {2}}\sigma ^{2}\right)^{2}+2\sigma ^{2}r}} \over {\sigma ^{2}}}\end{aligned}}$ In order to have a finite solution for the perpetual put, since the boundary conditions imply upper and lower finite bounds on the value of the put, it is necessary to set $A_{1}=0$ , leading to the solution $V(S)=A_{2}S^{\lambda _{2}}$ . From the first boundary condition, it is known that: $V(S_{-})=A_{2}(S_{-})^{\lambda _{2}}=K-S_{-}\implies A_{2}={K-S_{-} \over {(S_{-})^{\lambda _{2}}}}$ Therefore, the value of the perpetual put becomes: $V(S)=(K-S_{-})\left({S \over {S_{-}}}\right)^{\lambda _{2}}$ The second boundary condition yields the location of the lower exercise boundary: ${dV \over {dS}}(S_{-})=\lambda _{2}{K-S_{-} \over {S_{-}}}=-1\implies S_{-}={\lambda _{2}K \over {\lambda _{2}-1}}$ To conclude, for ${\textstyle S\geq S_{-}={\lambda _{2}K \over {\lambda _{2}-1}}}$ , the perpetual American put option is worth: $V(S)={K \over {1-\lambda _{2}}}\left({\lambda _{2}-1 \over {\lambda _{2}}}\right)^{\lambda _{2}}\left({S \over {K}}\right)^{\lambda _{2}}$

### Binary options

By solving the Black–Scholes differential equation with the Heaviside function as a boundary condition, one ends up with the pricing of options that pay one unit above some predefined strike price and nothing below.

In fact, the Black–Scholes formula for the price of a vanilla call option (or put option) can be interpreted by decomposing a call option into an asset-or-nothing call option minus a cash-or-nothing call option, and similarly for a put—the binary options are easier to analyze, and correspond to the two terms in the Black–Scholes formula.

#### Cash-or-nothing call

This pays out one unit of cash if the spot is above the strike at maturity. Its value is given by:

$C=e^{-r(T-t)}N(d_{2}).\,$

#### Cash-or-nothing put

This pays out one unit of cash if the spot is below the strike at maturity. Its value is given by:

$P=e^{-r(T-t)}N(-d_{2}).\,$

#### Asset-or-nothing call

This pays out one unit of asset if the spot is above the strike at maturity. Its value is given by:

$C=Se^{-q(T-t)}N(d_{1}).\,$

#### Asset-or-nothing put

This pays out one unit of asset if the spot is below the strike at maturity. Its value is given by:

$P=Se^{-q(T-t)}N(-d_{1}),$

#### Foreign Exchange (FX)

Denoting by *S* the FOR/DOM exchange rate (i.e., 1 unit of foreign currency is worth S units of domestic currency) one can observe that paying out 1 unit of the domestic currency if the spot at maturity is above or below the strike is exactly like a cash-or nothing call and put respectively. Similarly, paying out 1 unit of the foreign currency if the spot at maturity is above or below the strike is exactly like an asset-or nothing call and put respectively. Hence by taking $r_{f}$ , the foreign interest rate, $r_{d}$ , the domestic interest rate, and the rest as above, the following results can be obtained:

In the case of a digital call (this is a call FOR/put DOM) paying out one unit of the domestic currency gotten as present value:

$C=e^{-r_{d}T}N(d_{2})\,$

In the case of a digital put (this is a put FOR/call DOM) paying out one unit of the domestic currency gotten as present value:

$P=e^{-r_{d}T}N(-d_{2})\,$

In the case of a digital call (this is a call FOR/put DOM) paying out one unit of the foreign currency gotten as present value:

$C=Se^{-r_{f}T}N(d_{1})\,$

In the case of a digital put (this is a put FOR/call DOM) paying out one unit of the foreign currency gotten as present value:

$P=Se^{-r_{f}T}N(-d_{1})\,$

#### Skew

In the standard Black–Scholes model, one can interpret the premium of the binary option in the risk-neutral world as the expected value = probability of being in-the-money * unit, discounted to the present value. The Black–Scholes model relies on symmetry of distribution and ignores the skewness of the distribution of the asset. Market makers adjust for such skewness by, instead of using a single standard deviation for the underlying asset $\sigma$ across all strikes, incorporating a variable one $\sigma (K)$ where volatility depends on strike price, thus incorporating the volatility skew into account. The skew matters because it affects the binary considerably more than the regular options.

A binary call option is, at long expirations, similar to a tight call spread using two vanilla options. One can model the value of a binary cash-or-nothing option, *C*, at strike *K*, as an infinitesimally tight spread, where $C_{v}$ is a vanilla European call:

$C=\lim _{\epsilon \to 0}{\frac {C_{v}(K-\epsilon )-C_{v}(K)}{\epsilon }}$

Thus, the value of a binary call is the negative of the derivative of the price of a vanilla call with respect to strike price:

$C=-{\frac {dC_{v}}{dK}}$

When one takes volatility skew into account, $\sigma$ is a function of K :

$C=-{\frac {dC_{v}(K,\sigma (K))}{dK}}=-{\frac {\partial C_{v}}{\partial K}}-{\frac {\partial C_{v}}{\partial \sigma }}{\frac {\partial \sigma }{\partial K}}$

The first term is equal to the premium of the binary option ignoring skew:

$-{\frac {\partial C_{v}}{\partial K}}=-{\frac {\partial (SN(d_{1})-Ke^{-r(T-t)}N(d_{2}))}{\partial K}}=e^{-r(T-t)}N(d_{2})=C_{\text{no skew}}$

${\frac {\partial C_{v}}{\partial \sigma }}$ is the Vega of the vanilla call; ${\frac {\partial \sigma }{\partial K}}$ is sometimes called the "skew slope" or just "skew". If the skew is typically negative, the value of a binary call will be higher when taking skew into account.

$C=C_{\text{no skew}}-{\text{Vega}}_{v}\cdot {\text{Skew}}$

#### Relationship to vanilla options' Greeks

Since a binary call is a mathematical derivative of a vanilla call with respect to strike, the price of a binary call has the same shape as the delta of a vanilla call, and the delta of a binary call has the same shape as the gamma of a vanilla call.

## Black–Scholes in practice

The assumptions of the Black–Scholes model are not all empirically valid. The model is widely employed as a useful approximation to reality, but proper application requires understanding its limitations – blindly following the model exposes the user to unexpected risk. Among the most significant limitations are:

- the underestimation of extreme moves, yielding tail risk, which can be hedged with out-of-the-money options;
- the assumption of instant, cost-less trading, yielding liquidity risk, which is difficult to hedge;
- the assumption of a stationary process, yielding volatility risk, which can be hedged with volatility hedging;
- the assumption of continuous time and continuous trading, yielding gap risk, which can be hedged with Gamma hedging;
- the model tends to underprice deep out-of-the-money options and overprice deep in-the-money options.

In short, while in the Black–Scholes model one can perfectly hedge options by simply Delta hedging, in practice there are many other sources of risk.

Results using the Black–Scholes model differ from real world prices because of simplifying assumptions of the model. One significant limitation is that in reality security prices do not follow a strict stationary log-normal process, nor is the risk-free interest actually known (and is not constant over time). The variance has been observed to be non-constant leading to models such as GARCH to model volatility changes. Pricing discrepancies between empirical and the Black–Scholes model have long been observed in options that are far out-of-the-money, corresponding to extreme price changes; such events would be very rare if returns were lognormally distributed, but are observed much more often in practice.

Nevertheless, Black–Scholes pricing is widely used in practice, because it is:

- easy to calculate
- a useful approximation, particularly when analyzing the direction in which prices move when crossing critical points
- a robust basis for more refined models
- reversible, as the model's original output, price, can be used as an input and one of the other variables solved for; the implied volatility calculated in this way is often used to quote option prices (that is, as a *quoting convention*).

The first point is self-evidently useful. The others can be further discussed:

Useful approximation: although volatility is not constant, results from the model are often helpful in setting up hedges in the correct proportions to minimize risk. Even when the results are not completely accurate, they serve as a first approximation to which adjustments can be made.

Basis for more refined models: The Black–Scholes model is *robust* in that it can be adjusted to deal with some of its failures. Rather than considering some parameters (such as volatility or interest rates) as *constant,* one considers them as *variables,* and thus added sources of risk. This is reflected in the Greeks (the change in option value for a change in these parameters, or equivalently the partial derivatives with respect to these variables), and hedging these Greeks mitigates the risk caused by the non-constant nature of these parameters. Other defects cannot be mitigated by modifying the model, however, notably tail risk and liquidity risk, and these are instead managed outside the model, chiefly by minimizing these risks and by stress testing.

Explicit modeling: this feature means that, rather than *assuming* a volatility *a priori* and computing prices from it, one can use the model to solve for volatility, which gives the implied volatility of an option at given prices, durations and exercise prices. Solving for volatility over a given set of durations and strike prices, one can construct an implied volatility surface. In this application of the Black–Scholes model, a coordinate transformation from the *price domain* to the *volatility domain* is obtained. Rather than quoting option prices in terms of dollars per unit (which are hard to compare across strikes, durations and coupon frequencies), option prices can thus be quoted in terms of implied volatility, which leads to trading of volatility in option markets.

### The volatility smile

One of the attractive features of the Black–Scholes model is that the parameters in the model other than the volatility (the time to maturity, the strike, the risk-free interest rate, and the current underlying price) are unequivocally observable. All other things being equal, an option's theoretical value is a monotonic increasing function of implied volatility.

By computing the implied volatility for traded options with different strikes and maturities, the Black–Scholes model can be tested. If the Black–Scholes model held, then the implied volatility for a particular stock would be the same for all strikes and maturities. In practice, the volatility surface (the 3D graph of implied volatility against strike and maturity) is not flat.

The typical shape of the implied volatility curve for a given maturity depends on the underlying instrument. Equities tend to have skewed curves: compared to at-the-money, implied volatility is substantially higher for low strikes, and slightly lower for high strikes. Currencies tend to have more symmetrical curves, with implied volatility lowest at-the-money, and higher volatilities in both wings. Commodities often have the reverse behavior to equities, with higher implied volatility for higher strikes.

Despite the existence of the volatility smile (and the violation of all the other assumptions of the Black–Scholes model), the Black–Scholes PDE and Black–Scholes formula are still used extensively in practice. A typical approach is to regard the volatility surface as a fact about the market, and use an implied volatility from it in a Black–Scholes valuation model. This has been described as using "the wrong number in the wrong formula to get the right price". This approach also gives usable values for the hedge ratios (the Greeks). Even when more advanced models are used, traders prefer to think in terms of Black–Scholes implied volatility as it allows them to evaluate and compare options of different maturities, strikes, and so on. For a discussion as to the various alternative approaches developed here, see Financial economics § Challenges and criticism.

### Valuing bond options

Black–Scholes cannot be applied directly to bond securities because of pull-to-par. As the bond reaches its maturity date, all of the prices involved with the bond become known, thereby decreasing its volatility, and the simple Black–Scholes model does not reflect this process. A large number of extensions to Black–Scholes, beginning with the Black model, have been used to deal with this phenomenon. See Bond option § Valuation.

### Interest rate curve

In practice, interest rates are not constant—they vary by tenor (coupon frequency), giving an interest rate curve which may be interpolated to pick an appropriate rate to use in the Black–Scholes formula. Another consideration is that interest rates vary over time. This volatility may make a significant contribution to the price, especially of long-dated options. This is simply like the interest rate and bond price relationship which is inversely related.

### Short stock rate

Taking a short stock position, as inherent in the derivation, is not typically free of cost; equivalently, it is possible to lend out a long stock position for a small fee. In either case, this can be treated as a continuous dividend for the purposes of a Black–Scholes valuation, provided that there is no glaring asymmetry between the short stock borrowing cost and the long stock lending income.

Espen Gaarder Haug and Nassim Nicholas Taleb argue that the Black–Scholes model merely recasts existing widely used models in terms of practically impossible "dynamic hedging" rather than "risk", to make them more compatible with mainstream neoclassical economic theory. They also assert that Boness in 1964 had already published a formula that is "actually identical" to the Black–Scholes call option pricing equation. Edward Thorp also claims to have guessed the Black–Scholes formula in 1967 but kept it to himself to make money for his investors. Emanuel Derman and Taleb have also criticized dynamic hedging and state that a number of researchers had put forth similar models prior to Black and Scholes. In response, Paul Wilmott has defended the model.

In his 2008 letter to the shareholders of Berkshire Hathaway, Warren Buffett wrote: "I believe the Black–Scholes formula, even though it is the standard for establishing the dollar liability for options, produces strange results when the long-term variety are being valued... The Black–Scholes formula has approached the status of holy writ in finance ... If the formula is applied to extended time periods, however, it can produce absurd results. In fairness, Black and Scholes almost certainly understood this point well. But their devoted followers may be ignoring whatever caveats the two men attached when they first unveiled the formula."

British mathematician Ian Stewart, author of the 2012 book entitled *In Pursuit of the Unknown: 17 Equations That Changed the World*, said that Black–Scholes had "underpinned massive economic growth" and the "international financial system was trading derivatives valued at one quadrillion dollars per year" by 2007. He said that the Black–Scholes equation was the "mathematical justification for the trading"—and therefore—"one ingredient in a rich stew of financial irresponsibility, political ineptitude, perverse incentives and lax regulation" that contributed to the 2008 financial crisis. He clarified that "the equation itself wasn't the real problem", but its abuse in the financial industry.

The Black–Scholes model assumes positive underlying prices; if the underlying has a negative price, the model does not work directly. When dealing with options whose underlying can go negative, practitioners may use a different model such as the Bachelier model or simply add a constant offset to the prices.
