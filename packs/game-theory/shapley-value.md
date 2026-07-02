---
title: "Shapley value"
source: https://en.wikipedia.org/wiki/Shapley_value
domain: game-theory
license: CC-BY-SA-4.0
tags: game theory, nash equilibrium, zero-sum game, cooperative game
fetched: 2026-07-02
---

# Shapley value

In cooperative game theory, the **Shapley value** is a method (solution concept) for fairly distributing the total gains or costs among a group of players who have collaborated. For example, in a team project where each member contributed differently, the Shapley value provides a way to determine how much credit or blame each member deserves. It was named in honor of Lloyd Shapley, who introduced it in 1951.

The Shapley value determines each player's contribution by considering how much the overall outcome changes when they join each possible combination of other players, and then averaging those changes. In essence, it calculates each player's average marginal contribution across all possible coalitions. It is the only solution that satisfies four fundamental properties: efficiency, symmetry, additivity, and the dummy player (or null player) property, which are widely accepted as defining a fair distribution.

This method is used in many fields, from dividing profits in business partnerships to understanding feature importance in machine learning.

## Definition

Suppose we have a situation where players can win certain rewards by cooperating (forming a coalition) to accomplish a task; such situations are often called coalitional games. For a coalition (set of players) S , we define the *payoff* or *value* function $v(S)$ as the total sum of payoffs that the members of S can obtain by cooperating.

The Shapley value is one way to divide up the value created by a coalition between its members. It is a "fair" distribution in the sense that it is the only distribution with certain desirable properties (listed below). According to the Shapley value, the amount that player i is given in a coalitional game $(v,N)$ is

$\varphi _{i}(v)=\sum _{S\subseteq N\setminus \{i\}}{\frac {|S|!\;(n-|S|-1)!}{n!}}(v(S\cup \{i\})-v(S))$

$\quad \quad \quad ={\frac {1}{n}}\sum _{S\subseteq N\setminus \{i\}}{n-1 \choose |S|}^{-1}(v(S\cup \{i\})-v(S))$

where n is the total number of players and the sum extends over all subsets S of N not containing player i , including the empty set. Also note that ${n \choose k}$ is the binomial coefficient. The formula can be interpreted as follows: imagine the coalition is formed one actor at a time, with each actor demanding their contribution $v(S\cup \{i\})-v(S)$ as a fair compensation, and then for each actor take the average of this contribution over the possible different permutations in which the coalition can be formed.

An alternative, equivalent formula for the Shapley value is:

$\varphi _{i}(v)={\frac {1}{n!}}\sum _{R}\left[v(P_{i}^{R}\cup \left\{i\right\})-v(P_{i}^{R})\right]$

where the sum ranges over all $n!$ orders R of the players and $P_{i}^{R}$ is the set of players in N which precede i in the order R .

### In terms of synergy

From the characteristic function v one can compute the *synergy* (Harsanyi dividend) that each group of players provides. The synergy is the unique function $w\colon 2^{N}\to \mathbb {R}$ , such that

$v(S)=\sum _{R\subseteq S}w(R)$

for any subset $S\subseteq N$ of players. In other words, the 'total value' of the coalition S comes from summing up the *synergies* of each possible subset of S .

Given a characteristic function v , the synergy function w is calculated via

$w(S)=\sum _{R\subseteq S}(-1)^{|S|-|R|}v(R)$

using the Inclusion exclusion principle.

The Shapley values are given in terms of the synergy function by

$\varphi _{i}(v)=\sum _{i\in S\subseteq N}{\frac {w(S)}{|S|}}$

where the sum is over all subsets S of N that include player i .

This can be interpreted as

$\varphi _{i}(v)=\sum _{\text{coalitions including i}}{\frac {\text{synergy of the coalition}}{\text{number of members in the coalition}}}$

In other words, the synergy of each coalition is divided equally between all members.

This can be interpreted visually with a Venn diagram. In the first example diagram above, each region has been labeled with the synergy bonus of the corresponding coalition. The total value produced by a coalition is the sum of synergy bonuses of the composing subcoalitions - in the example, the coalition of the players labeled "You" and "Emma" would produce a profit of $30+20+40=90$ dollars, as compared to their individual profits of $30$ and $20$ dollars respectively. The synergies are then split equally among each member of the subcoalition that contributes that synergy - as displayed in the second diagram.

## Examples

### Business example

Consider a simplified description of a business. An owner, *o*, provides crucial capital in the sense that, without him/her, no gains can be obtained. There are *m* workers *w*1,...,*w**m*, each of whom contributes an amount *p* to the total profit. Let

$N=\{o,w_{1},\ldots ,w_{m}\}.$

The value function for this coalitional game is

$v(S)={\begin{cases}(|S|-1)p&{\text{if }}o\in S\;,\\0&{\text{otherwise}}\;.\\\end{cases}}$

Computing the Shapley value for this coalition game leads to a value of ⁠*mp*/2⁠ for the owner and ⁠*p*/2⁠ for each one of the *m* workers.

This can be understood from the perspective of synergy. The synergy function w is

$w(S)={\begin{cases}p,&{\text{if }}S=\{o,w_{i}\}\\0,&{\text{otherwise}}\\\end{cases}}$

so the only coalitions that generate synergy are one-to-one between the owner and any individual worker.

Using the above formula for the Shapley value in terms of w we compute

$\varphi _{w_{i}}={\frac {w(\{o,w_{i}\})}{2}}={\frac {p}{2}}$

and

$\varphi _{o}=\sum _{i=1}^{m}{\frac {w(\{o,w_{i}\})}{2}}={\frac {mp}{2}}$

The result can also be understood from the perspective of averaging over all orders. A given worker joins the coalition after the owner (and therefore contributes *p*) in half of the orders and thus makes an average contribution of ${\frac {p}{2}}$ upon joining. When the owner joins, on average half the workers have already joined, so the owner's average contribution upon joining is ${\frac {mp}{2}}$ .

### Glove game

The glove game is a coalitional game where the players have left- and right-hand gloves and the goal is to form pairs. Let

$N=\{1,2,3\},$

where players 1 and 2 have right-hand gloves and player 3 has a left-hand glove.

The value function for this coalitional game is

$v(S)={\begin{cases}1&{\text{if }}S\in \left\{\{1,3\},\{2,3\},\{1,2,3\}\right\};\\0&{\text{otherwise}}.\\\end{cases}}$

The formula for calculating the Shapley value is

$\varphi _{i}(v)={\frac {1}{|N|!}}\sum _{R}\left[v(P_{i}^{R}\cup \left\{i\right\})-v(P_{i}^{R})\right],$

where R is an ordering of the players and $P_{i}^{R}$ is the set of players in N which precede i in the order R.

The following table displays the marginal contributions of Player 1.

${\begin{array}{|c|r|}{\text{Order }}R\,\!&MC_{1}\\\hline {1,2,3}&v(\{1\})-v(\varnothing )=0-0=0\\{1,3,2}&v(\{1\})-v(\varnothing )=0-0=0\\{2,1,3}&v(\{1,2\})-v(\{2\})=0-0=0\\{2,3,1}&v(\{1,2,3\})-v(\{2,3\})=1-1=0\\{3,1,2}&v(\{1,3\})-v(\{3\})=1-0=1\\{3,2,1}&v(\{1,3,2\})-v(\{3,2\})=1-1=0\end{array}}$

Observe

$\varphi _{1}(v)=\!\left({\frac {1}{6}}\right)(1)={\frac {1}{6}}.$

By a symmetry argument it can be shown that

$\varphi _{2}(v)=\varphi _{1}(v)={\frac {1}{6}}.$

Due to the efficiency axiom, the sum of all the Shapley values is equal to 1, which means that

$\varphi _{3}(v)={\frac {4}{6}}={\frac {2}{3}}.$

## Properties

The Shapley value has many desirable properties, including satisfying the four properties of efficiency, symmetry, linearity and null player (or dummy player).

### Efficiency

The sum of the Shapley values of all agents equals the value of the grand coalition, so that all the gain is distributed among the agents:

$\sum _{i\in N}\varphi _{i}(v)=v(N)$

*Proof*: $\sum _{i\in N}\varphi _{i}(v)={\frac {1}{|N|!}}\sum _{R}\sum _{i\in N}v(P_{i}^{R}\cup \left\{i\right\})-v(P_{i}^{R})$ $={\frac {1}{|N|!}}\sum _{R}v(N)={\frac {1}{|N|!}}|N|!\cdot v(N)=v(N)$

since $\sum _{i\in N}v(P_{i}^{R}\cup \left\{i\right\})-v(P_{i}^{R})$ is a telescoping sum and there are $|N|!$ different orderings R .

### Symmetry

If i and j are two actors who are equivalent in the sense that

$v(S\cup \{i\})=v(S\cup \{j\})$

for every subset S of N which contains neither i nor j , then $\varphi _{i}(v)=\varphi _{j}(v)$ .

This property is also called *equal treatment of equals*.

### Linearity

If two coalition games described by gain functions v and w are combined, then the distributed gains should correspond to the gains derived from v and the gains derived from w :

$\varphi _{i}(v+w)=\varphi _{i}(v)+\varphi _{i}(w)$

for every i in  N . Also, for any real number a ,

$\varphi _{i}(av)=a\varphi _{i}(v)$

for every i in  N .

### Null player

The Shapley value $\varphi _{i}(v)$ of a null player i in a game v is zero. A player i is *null* in v if $v(S\cup \{i\})=v(S)$ for all coalitions S that do not contain i .

### Stand-alone test

If v is a subadditive set function, i.e., if $v(S\cup T)\leq v(S)+v(T)$ , then for each agent i : $\varphi _{i}(v)\leq v(\{i\})$ .

Similarly, if v is a superadditive set function, i.e., if $v(S\cup T)\geq v(S)+v(T)$ for $S\cap T=\emptyset$ , then for each agent i : $\varphi _{i}(v)\geq v(\{i\})$ .

So, if the cooperation has positive synergy, all agents (weakly) gain, and if it has negative synergy, all agents (weakly) lose.

### Anonymity

If i and j are two agents, and w is a gain function that is identical to v except that the roles of i and j have been exchanged, then $\varphi _{i}(v)=\varphi _{j}(w)$ . This means that the labeling of the agents doesn't play a role in the assignment of their gains.

### Marginalism

The Shapley value can be defined as a function which uses only the marginal contributions of player i as the arguments.

## Aumann–Shapley value

In their 1974 book, Lloyd Shapley and Robert Aumann extended the concept of the Shapley value to infinite games (defined with respect to a non-atomic measure), creating the diagonal formula. This was later extended by Jean-François Mertens and Abraham Neyman.

As seen above, the value of an n-person game associates with each player the expectation of their contribution to the worth of the coalition of players before them in a random ordering of all the players. When there are many players and each individual plays only a minor role, the set of all players preceding a given one is heuristically thought of as a good sample of all players. The value of a given infinitesimal player ds is then defined as "their" contribution to the worth of a "perfect" sample of all the players.

Symbolically, if v is the coalitional worth function that associates each coalition c with its value, and each coalition c is a measurable subset of the measurable set I of all players, that we assume to be $I=[0,1]$ without loss of generality, the value $(Sv)(ds)$ of an infinitesimal player ds in the game is

$(Sv)(ds)=\int _{0}^{1}(\,v(tI+ds)-v(tI)\,)\,dt.$

Here tI is a perfect sample of the all-player set I containing a proportion t of all the players, and $tI+ds$ is the coalition obtained after ds joins tI. This is the heuristic form of the diagonal formula.

Assuming some regularity of the worth function, for example, assuming v can be represented as differentiable function of a non-atomic measure on I, μ, $v(c)=f(\mu (c))$ with density function $\varphi$ , with $\mu (c)=\int 1_{c}(u)\varphi (u)\,du,$ where $1_{c}(\bullet )$ is the characteristic function of c. Under such conditions

$\mu (tI)=t\mu (I)$

,

as can be shown by approximating the density by a step function and keeping the proportion t for each level of the density function, and

$v(tI+ds)=f(t\mu (I))+f'(t\mu (I))\mu (ds).$

The diagonal formula has then the form developed by Aumann and Shapley (1974)

$(Sv)(ds)=\int _{0}^{1}f'_{t\mu (I)}(\mu (ds))\,dt$

Above μ can be vector valued (as long as the function is defined and differentiable on the range of μ, the above formula makes sense).

In the argument above if the measure contains atoms $\mu (tI)=t\mu (I)$ is no longer true—this is why the diagonal formula mostly applies to non-atomic games.

Two approaches were deployed to extend this diagonal formula when the function f is no longer differentiable. Mertens goes back to the original formula and takes the derivative after the integral thereby benefiting from the smoothing effect. Neyman took a different approach. Going back to an elementary application of Mertens's approach from Mertens (1980):

$(Sv)(ds)=\lim _{\varepsilon \to 0,\varepsilon >0}{\frac {1}{\varepsilon }}\int _{0}^{1-\varepsilon }(f(t+\varepsilon \mu (ds))-f(t))\,dt$

This works for example for majority games—while the original diagonal formula cannot be used directly. How Mertens further extends this by identifying symmetries that the Shapley value should be invariant upon, and averaging over such symmetries to create further smoothing effect commuting averages with the derivative operation as above. A survey for non atomic value is found in Neyman (2002)

## Generalization to coalitions

The Shapley value only assigns values to the individual agents. It has been generalized to apply to a group of agents *C* as,

$\varphi _{C}(v)=\sum _{T\subseteq N\setminus C}{\frac {(n-|T|-|C|)!\;|T|!}{(n-|C|+1)!}}\sum _{S\subseteq C}(-1)^{|C|-|S|}v(S\cup T)\;.$

In terms of the synergy function w above, this reads

$\varphi _{C}(v)=\sum _{C\subseteq T\subseteq N}{\frac {w(T)}{|T|-|C|+1}}$

where the sum goes over all subsets T of N that contain C .

This formula suggests the interpretation that the Shapley value of a coalition is to be thought of as the standard Shapley value of a single player, if the coalition C is treated like a single player.

## Value of a player to another player

The Shapley value $\varphi _{i}(v)$ was decomposed by Hausken and Matthias into a matrix of values

$\varphi _{ij}(v)=\sum _{S\subseteq N}{\frac {(|S|-1)!\;(n-|S|)!}{n!}}(v(S)-v(S\setminus \{i\})-v(S\setminus \{j\})+v(S\setminus \{i,j\}))\sum _{t=|S|}^{n}{\frac {1}{t}}$

Each value $\varphi _{ij}(v)$ represents the value of player i to player j . This matrix satisfies

$\varphi _{i}(v)=\sum _{j\in N}\varphi _{ij}(v)$

i.e. the value of player i to the whole game is the sum of their value to all individual players.

In terms of the synergy w defined above, this reads

$\varphi _{ij}(v)=\sum _{\{i,j\}\subseteq S\subseteq N}{\frac {w(S)}{|S|^{2}}}$

where the sum goes over all subsets S of N that contain i and j .

This can be interpreted as sum over all subsets that contain players i and j , where for each subset S you

- take the synergy $w(S)$ of that subset
- divide it by the number of players in the subset $|S|$ . Interpret that as the surplus value player i gains from this coalition
- further divide this by $|S|$ to get the part of player i 's value that's attributed to player j

In other words, the synergy value of each coalition is evenly divided among all $|S|^{2}$ *pairs* $(i,j)$ of players in that coalition, where i generates surplus for j .

## Shapley value regression

Shapley value regression is a statistical method used to measure the contribution of individual predictors in a regression model. In this context, the "players" are the individual predictors or variables in the model, and the "gain" is the total explained variance or predictive power of the model. This method ensures a fair distribution of the total gain among the predictors, attributing each predictor a value representing its contribution to the model's performance. Lipovetsky (2006) discussed the use of Shapley value in regression analysis, providing a comprehensive overview of its theoretical underpinnings and practical applications.

Shapley value contributions are recognized for their balance of stability and discriminating power, which make them suitable for accurately measuring the importance of service attributes in market research. Several studies have applied Shapley value regression to key drivers analysis in marketing research. Pokryshevskaya and Antipov (2012) utilized this method to analyze online customers' repeat purchase intentions, demonstrating its effectiveness in understanding consumer behavior. Similarly, Antipov and Pokryshevskaya (2014) applied Shapley value regression to explain differences in recommendation rates for hotels in south Cyprus, highlighting its utility in the hospitality industry. Further validation of the benefits of Shapley value in key-driver analysis is provided by Vriens, Vidden, and Bosch (2021), who underscored its advantages in applied marketing analytics.

## In machine learning

The Shapley value provides a principled way to explain the predictions of nonlinear models common in the field of machine learning. By interpreting a model trained on a set of features as a value function on a coalition of players, Shapley values provide a natural way to compute which features contribute to a prediction or contribute to the uncertainty of a prediction. This unifies several other methods, including locally interpretable model-agnostic explanations (LIME), DeepLIFT, and layer-wise relevance propagation.

Distributional values are an extension of the Shapley value and related value operators designed to preserve the probabilistic output of predictive models in machine learning, including neural network classifiers and large language models.

The statistical understanding of Shapley values remains an ongoing research question. A smooth version, called Shapley curves, achieves the minimax rate and is shown to be asymptotically Gaussian in a nonparametric setting. Confidence intervals for finite samples can be obtained via the wild bootstrap.
