---
title: "Revelation principle"
source: https://en.wikipedia.org/wiki/Revelation_principle
domain: mechanism-design
license: CC-BY-SA-4.0
tags: mechanism design, incentive compatibility, vickrey clarke groves, revelation principle
fetched: 2026-07-02
---

# Revelation principle

The **revelation principle** is a fundamental result in mechanism design, social choice theory, and game theory which shows it is always possible to design a strategy-resistant implementation of a social decision-making mechanism (such as an electoral system or market). It can be seen as a kind of mirror image to Gibbard's theorem. The revelation principle says that if a social choice function can be implemented with some non-honest mechanism—one where players have an incentive to lie—the same function can be implemented by an incentive-compatible (honesty-promoting) mechanism with the same equilibrium outcome (payoffs).

The revelation principle shows that, while Gibbard's theorem proves it is impossible to design a system that will always be fully invulnerable to strategy (if we do not know how players will behave), it *is* possible to design a system that encourages honesty given a solution concept (if the corresponding equilibrium is unique).

The idea behind the revelation principle is that, if we know which strategy the players in a game will use, we can simply ask all the players to submit their true payoffs or utility functions; then, we take those preferences and calculate each voter's optimal strategy before executing it for them. This procedure means that an honest report of preferences is now the best-possible strategy, because it guarantees the mechanism will play the optimal strategy for the player.

## Examples

Consider the following example. There is a certain item that Alice values as $v_{A}$ and Bob values as $v_{B}$ . The government needs to decide who will receive that item and in what terms.

- A *social-choice-function* is a function that maps a set of individual *preferences* to an optimal social outcome. An example function is the utilitarian rule, which says "give the item to a person that values it the most". We denote a social choice function by **Soc** and its recommended outcome given a set of preferences by **Soc(Prefs)**.
- A *mechanism* is a rule that maps a set of individual *actions* to a social outcome. A mechanism **Mech** induces a game which we denote by **Game(Mech)**.
- A mechanism **Mech** is said to *implement* a social-choice-function **Soc** if, for every combination of individual preferences, there is a Nash equilibrium in **Game(Mech)** in which the outcome is **Soc(Prefs)**. Two example mechanisms are:
  - "Each individual says a number between 1 and 10. The item is given to the individual who says the lowest number; if both say the same number, then the item is given to Alice". This mechanism does NOT implement the utilitarian function, since for every individual who wants the item, it is a dominant strategy to say "1" regardless of his/her true value. This means that in equilibrium the item is always given to Alice, even if Bob values it more.
  - First-price sealed-bid auction is a mechanism which implements the utilitarian function. For example, if $v_{B}>v_{A}$ , then any action profile in which Bob bids more than Alice and both bids are in the range $(v_{A},v_{B})$ is a Nash-equilibrium in which the item goes to Bob. Additionally, if the valuations of Alice and Bob are random variables drawn independently from the same distribution, then there is a Bayesian Nash equilibrium in which the item goes to the bidder with the highest value.
- A *direct-mechanism* is a mechanism in which the set of actions available to each player is just the set of possible preferences of the player.
- A direct-mechanism **Mech** is said to be *Bayesian-Nash-Incentive-compatible (BNIC)* if there is a Bayesian Nash equilibrium of **Game(Mech)** in which all players reveal their true preferences. Some example direct-mechanisms are:
  - "Each individual says how much he values the item. The item is given to the individual that said the highest value. In case of a tie, the item is given to Alice". This mechanism is **not** BNIC, since a player who wants the item is better-off by saying the highest possible value, regardless of his true value.
  - First-price sealed-bid auction is also **not** BNIC, since the winner is always better-off by bidding the lowest value that is slightly above the loser's bid.
  - However, if the distribution of the players' valuations is known, then there is a variant which is BNIC and implements the utilitarian function.
  - Moreover, it is known that second price auction is BNIC (it is even IC in a stronger sense—dominant-strategy IC). Additionally, it implements the utilitarian function.

## Proof

Suppose we have an arbitrary mechanism **Mech** that implements **Soc**.

We construct a direct mechanism **Mech'** that is truthful and implements **Soc**.

**Mech'** simply simulates the equilibrium strategies of the players in Game(**Mech**). i.e.

- **Mech'** asks the players to report their valuations.
- Based on the reported valuations, **Mech'** calculates, for each player, his equilibrium strategy in **Mech**.
- **Mech'** returns the outcome returned by **Mech**.

Reporting the true valuations in **Mech'** is like playing the equilibrium strategies in **Mech**. Hence, reporting the true valuations is a Nash equilibrium in **Mech'**, as desired. Moreover, the equilibrium payoffs are the same, as desired.

## Finding solutions

In mechanism design, the revelation principle is importance in finding solutions. The researcher need only look at the set of equilibria characterized by incentive compatibility. That is, if the mechanism designer wants to implement some outcome or property, they can restrict their search to mechanisms in which agents are willing to reveal their private information to the mechanism designer that has that outcome or property. If no such direct and truthful mechanism exists, no mechanism can implement this outcome by contraposition. By narrowing the area needed to be searched, the problem of finding a mechanism becomes much easier.

## Variants

The principle comes in various flavors corresponding to different kinds of incentive-compatibility:

- The *dominant-strategy revelation-principle* says that every social-choice function that can be implemented in dominant-strategies can be implemented by a dominant-strategy-incentive-compatible (DSIC) mechanism. This variant was first introduced by Allan Gibbard.
- The *Bayesian-Nash revelation-principle* says that every social-choice function that can be implemented in Bayesian-Nash equilibrium (Bayesian game, i.e. game of incomplete information) can be implemented by a Bayesian-Nash incentive-compatibility (BNIC) mechanism. This broader solution concept was introduced by Dasgupta, Hammond and Maskin; Holmström; and Myerson.

The revelation principle also works for correlated equilibria: for every arbitrary *coordinating device* a.k.a. correlating, there exists another direct device for which the state space equals the action space of each player. Then the coordination is done by directly informing each player of his action.
