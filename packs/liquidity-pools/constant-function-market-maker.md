---
title: "Constant function market maker"
source: https://en.wikipedia.org/wiki/Constant_function_market_maker
domain: liquidity-pools
license: CC-BY-SA-4.0
tags: liquidity pool, automated market maker, uniswap pool, impermanent loss
fetched: 2026-07-02
---

# Constant function market maker

**Constant-function market makers** (**CFMM**) are a paradigm in the design of trading venues where a trading function and a set of rules determine how liquidity takers (LTs) and liquidity providers (LPs) interact, and how markets are cleared. The trading function is deterministic and known to all market participants.

CFMMs display pools of liquidity of two assets. The takers and providers of liquidity interact in the liquidity pools: LPs deposit their assets in the pool and LTs exchange assets directly with the pool. CFMMs rely on two rules; the LT trading condition and the LP provision condition. The LT trading condition links the state of the pool before and after a trade is executed, and it determines the relative prices between the assets by their quantities in the pool. The LP provision condition links the state of the pool before and after liquidity is deposited or withdrawn by an LP. Thus, the trading function establishes the link between liquidity and prices, so LTs can compute the execution costs of their trades as a function of the trade size, and LPs can compute the exact quantities that they deposit. In CFMMs, both conditions state that price formation happens only through LT trades (see below).

In decentralized platforms running on peer-to-peer networks, CFMMs are hard-coded and immutable programs implemented as Smart Contracts, where LPs and LTs invoke the code of the contract to execute their transactions. A particular case of CFMMs are the constant product market makers (CPMMs) such as Uniswap v2 and Uniswap v3 where the trading function uses the product of the quantities of each asset in the pool to determine clearing prices. CFMMs are also popular in prediction markets.

## History

An early description of a CFMM was published by economist Robin Hanson in *"Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation"* (2002). Early literature referred to the broader class of "automated market makers", including that of the Hollywood Stock Exchange founded in 1999; the term "constant-function market maker" was introduced in *"Improved Price Oracles: Constant Function Market Makers"* (Angeris & Chitra 2020). First be seen in production on a Minecraft server in 2012, CFMMs are a popular DEX architecture.

## Definition

### Trading function

Consider a reference asset X and an asset Y which is valued in terms of X . Assume that the liquidity pool of the CFMM initially consists of quantity x of asset X and quantity y of asset Y . The pair $(x,y)$ is referred to as the **reserves** of the pool (the following definitions can be extended to a basket of more than two assets). The CFM is characterised by a **trading function** $f:\mathbb {R} ^{+}\times \mathbb {R} ^{+}\rightarrow \mathbb {R}$ (also known as the invariant) defined over the pool reserves x and y . The trading function is continuously differentiable and increasing in its arguments ( $\mathbb {R} ^{+}$ denotes the set of positive real numbers).

For instance, the trading function of the constant product market maker (CPMM) is $f(x,y)=x\times y$ . Other types of CFMMs are the constant sum market maker with $f(x,y)=x+y$ ; the constant mean market maker with $f(x,y)=w_{x}x+w_{y}y$ , where $w_{x},w_{y}>0$ and $w_{x}+w_{y}=1$ ; and the hybrid function market maker, which uses combinations of trading functions.

### LT trading condition and convexity

LT transactions involve exchanging a quantity $\Delta ^{y}$ of asset Y for a quantity $\Delta ^{x}$ of asset X , and vice-versa. The quantities to exchange are determined by the **LT trading condition**:

(1)

$f(x,y)=f(x+\Delta ^{x},y-\Delta ^{y})=\kappa ^{2}\,,$

where $\kappa$ is the *depth* of the pool (see the **LP provision condition** below) and is a measure of the available liquidity. The value of the depth $\kappa >0$ is constant before and after a trade is executed, so the LT trading condition **(1)** defines a level curve. For a fixed value of the depth $\kappa$ , the **level function** $\varphi _{\kappa }$ (also known as the forward exchange function ) is such that $f(x,y)=\kappa ^{2}\iff x=\varphi _{\kappa }(y)$ . For any value $\kappa$ of the depth, the level function $\varphi _{\kappa }:\mathbb {R} ^{+}\mapsto \mathbb {R} ^{+}$ is twice differentiable.

The LT trading condition **(1)** links the state of the pool before and after a liquidity taking trade is executed. For LTs, this condition specifies the exchange rate ${\tilde {Z}}(\Delta ^{y})$ , of asset Y in terms of the reference asset X , to trade a (possibly negative) quantity $\Delta ^{y}$ of asset Y :

${\tilde {Z}}(\Delta ^{y})=\left(\varphi _{\kappa }\left(y\right)-\varphi _{\kappa }\left(y+\Delta ^{y}\right)\right){\big /}\Delta ^{y}\,.$

The **marginal exchange rate** of asset Y in terms of asset X , akin to the midprice in a limit order book (LOB), is the price for an infinitesimal trade in a CFMM:

$Z=\lim _{\Delta ^{y}\rightarrow 0}{\tilde {Z}}(\Delta ^{y})=-\varphi '_{\kappa }(y).$

It is proven that no roundtrip arbitrage in a CFMM implies that the level function $\varphi$ must be convex.

Execution costs in the CFMM are defined as the difference between the marginal exchange rate and the exchange rate at which a trade is executed. It has been shown that LTs can use the convexity of the level function around the pool's reserves level to approximate the execution costs $\left|{\tilde {Z}}(\Delta ^{y})-Z\right|$ by ${\frac {1}{2}}\,\varphi _{\kappa }^{''}(y)\left|\Delta ^{y}\right|$ .

### LP provision condition and homotheticity

LP transactions involve depositing or withdrawing quantities $(\Delta ^{x},\Delta ^{y})$ of asset X and asset Y . Let $\kappa _{0}$ be the initial depth of the pool and let $\kappa _{1}$ be the depth of the pool after an LP deposits $\Delta ^{x},\Delta ^{y}$ , i.e., $f(x,y)=\kappa _{0}^{2}$ and $f(x+\Delta x,y+\Delta y)=\kappa _{1}^{2}$ . Let $\varphi _{\kappa _{0}}$ and $\varphi _{\kappa _{1}}$ be the level functions corresponding to the values $\kappa _{0}$ and $\kappa _{1}$ , respectively. Denote by Z the initial marginal exchange rate of the pool. The LP provision condition requires that LPs **do not change** the marginal rate Z , so

(2)

$-\varphi '_{\kappa _{0}}\left(y\right)=-\varphi '_{\kappa _{1}}\left(y+\Delta ^{y}\right)=Z\,.$

The LP provision condition **(2)** links the state of the pool before and after a liquidity provision operation is executed. The trading function $f(x,y)$ is increasing in the pool reserves x and $y.$ So, when liquidity provision activity increases (decreases) the size of the pool, the value of the pool's depth $\kappa$ increases (decreases). The value of $\kappa$ can be seen as a measure of the liquidity depth in the pool. Note that the LP provision condition holds for any homothetic trading function.

## Examples

### Constant Product Market Maker

In CPMMs such as Uniswap v2, the trading function is $f\left(x,y\right)=x\times y,$ so the level function is $\varphi \left(y\right)=\kappa ^{2}{\big /}y$ , the marginal exchange rate is $Z=x/y,$ and the exchange rate for a quantity $\Delta ^{y}$ is ${\tilde {Z}}\left(\Delta ^{y}\right)\approx Z-Z^{3/2}\Delta ^{y}{\big /}\kappa .$

In CPMMs, the liquidity provision condition is $x/y=(x+\Delta ^{x})/(y+\Delta ^{y})$ when the quantities $(\Delta ^{x},\Delta ^{y})$ are deposited to the pool. Thus, liquidity is provided so that the proportion of the reserves x and y in the pool is preserved.

## Profits and losses of liquidity providers

### Fees

For LPs, the key difference between the traditional markets based on LOBs and CFMMs is that in LOBs, market makers post limit orders above and below the mid-price to earn the spread on roundtrip trades, while in CFMMs, LPs earn fees paid by LTs when their liquidity is used.

### Loss-Versus-Rebalancing

Without fees paid by LTs, liquidity provision in CFMMs is a **loss-leading activity**. Loss-Versus-Rebalancing (LVR) is a popular measure of these losses. Assume the price follows the dynamics $dS_{t}=\sigma _{t}dW_{t}$ then the LVR is given by ${\text{LVR}}_{t}=-{\frac {1}{2}}\int _{0}^{t}\,\sigma _{s}^{2}\,{\text{d}}s\,\leq 0\,.$

### Predictable loss

To thoroughly characterise their losses, LPs can also use **Predictable Loss (PL)**, which is a comprehensive and model-free measure for the unhedgeable and predictable losses of liquidity provision. One source of PL is the **convexity cost** (losses due to adverse selection, they can be regarded as generalized LVR) whose magnitude depends on liquidity taking activity and the convexity of the level function. The other source is the **opportunity cost**, which is incurred by LPs who lock assets in the pool instead of investing them in the risk-free asset. For an LP providing reserves $(x_{0},y_{0})$ at time $t=0$ and withdrawing liquidity at time $T>0$ , PL is

${\text{PL}}_{T}=-\,\,\underbrace {{\frac {1}{2}}\int _{0}^{T}\,\varphi ''\left(y_{s}\right)\,{\text{d}}\left\langle y,y\right\rangle _{s}\,} _{{\text{Convexity cost}}\,\geq \,0}\,\,-\,\,\underbrace {\int _{0}^{T}\xi _{s}\,r\,{\text{d}}s\,} _{{\text{Opportunity cost}}\,\geq \,0}\,,$

where $\left(\xi _{t}\right)_{t\in [0,T]}$ is an increasing stochastic process with initial value 0 , and $\left(y_{t}\right)_{t\in [0,T]}$ is a process that describes the reserves in asset Y . In particular, ${\text{PL}}$ satisfies

${\text{PL}}_{t}\leq -{\frac {1}{2}}\int _{0}^{t}\,\varphi ''\left(y_{s}\right)\,{\text{d}}\left\langle y,y\right\rangle _{s}\,\leq 0\,.$

PL can be estimated without specifying dynamics for the marginal rate or the trading flow and without specifying a parametric form for the level function. PL shows that liquidity provision generates losses for any type of LT trading activity (informed and uninformed). The level of fee revenue must exceed PL in expectation for liquidity provision to be profitable in CFMMs.

### Impermanent loss

Impermanent loss, or divergence loss, is sometimes used to characterise the risk of providing liquidity in a CFMM. Impermanent loss compares the evolution of the value of the LP's assets in the pool with the evolution of a self-financing buy-and-hold portfolio invested in an alternative venue. The self-financing portfolio is initiated with the same quantities $\left(x_{0},y_{0}\right)$ as those that the LP deposits in the pool. It can be shown that the impermanent loss ${\text{IL}}_{t}$ at time $t>0$ is

${\text{IL}}_{t}=\ -\left(\varphi \left(y_{0}\right)-\varphi \left(y_{t}\right)-\varphi '(y_{t})\left(y_{0}-y_{t}\right)\right)$

where $y_{t}$ are the reserves in asset Y in the pool at time t .

The convexity of the level function shows that ${\text{IL}}_{t}\leq 0$ . In the case of CPMMs, the impermanent loss is given by

${\text{IL}}_{t}=-\kappa \,{\sqrt {Z_{t}}}\left(1-{\sqrt {\frac {Z_{t}}{Z_{0}}}}\right)^{2}\leq 0\,.$

where $Z_{t}$ is the marginal exchange rate in the CPMM pool at time t .

${\text{IL}}$ is not an appropriate measure to characterise the losses of LPs because it can underestimate or overestimate the losses that are solely imputable to liquidity provision. More precisely, the alternative buy-and-hold portfolio is not exposed to the same market risk as the holdings of the LP in the pool, and the impermanent loss can be partly hedged. In contrast, PL is the predictable and unhedgeable component in the wealth of LPs.

## Concentrated liquidity

Concentrated liquidity is a feature introduced by Uniswap v3 for CPMMs. The key feature of a CPMM pool with CL is that LPs specify a range of exchange rates in which to post liquidity. The bounds of the liquidity range take values in a discretised finite set of exchange rates called ticks. Concentrating liquidity increases fee revenue, but also increases PL and *concentration risk*, i.e., the risk of the exchange rate exiting the range.
