---
title: "Vickrey auction"
source: https://en.wikipedia.org/wiki/Vickrey_auction
domain: mechanism-design
license: CC-BY-SA-4.0
tags: mechanism design, incentive compatibility, vickrey clarke groves, revelation principle
fetched: 2026-07-02
---

# Vickrey auction

A **Vickrey auction** or **sealed-bid second-price auction** (**SBSPA**) is a type of sealed-bid auction. Bidders submit written bids without knowing the bid of the other people in the auction. The highest bidder wins but the price paid is the second-highest bid. This type of auction is strategically similar to an English auction and gives bidders an incentive to bid their true value. The auction was first described academically by Columbia University professor William Vickrey in 1961 though it had been used by stamp collectors since 1893. In 1797 Johann Wolfgang von Goethe sold a manuscript using a sealed-bid, second-price auction.

Vickrey's original paper mainly considered auctions where only a single, indivisible good is being sold. The terms *Vickrey auction* and *second-price sealed-bid auction* are, in this case only, equivalent and used interchangeably. In the case of multiple identical goods, the bidders submit inverse demand curves and pay the opportunity cost.

Vickrey auctions are much studied in economic literature but uncommon in practice. Generalized variants of the Vickrey auction for multiunit auctions exist, such as the generalized second-price auction used in Google's and Yahoo!'s online advertisement programs (not incentive compatible) and the Vickrey–Clarke–Groves auction (incentive compatible).

## Properties

### Self-revelation and incentive compatibility

In a Vickrey auction with private values each bidder maximizes their expected utility by bidding (revealing) their valuation of the item for sale. These types of auctions are sometimes used for specified pool trading in the agency mortgage-backed securities (MBS) market.

### Weaknesses

- It does not allow for price discovery, that is, discovery of the market price if the buyers are unsure of their own valuations, without sequential auctions.

## Proof of dominance of truthful bidding

The dominant strategy in a Vickrey auction with a single, indivisible item is for each bidder to bid their true value of the item.

Let $v_{i}$ be bidder i's value for the item. Let $b_{i}$ be bidder $i{\text{'s}}$ bid for the item. The payoff for bidder i is

${\begin{cases}v_{i}-\max _{j\neq i}b_{j}&{\text{if }}b_{i}>\max _{j\neq i}b_{j},\\0&{\text{otherwise.}}\end{cases}}$

The strategy of overbidding is dominated by bidding truthfully (i.e. bidding $v_{i}$ ). Assume that bidder i bids $b_{i}>v_{i}$ .

- If $\max _{j\neq i}b_{j}<v_{i}$ then the bidder would win the item with a truthful bid as well as an overbid. The bid's amount does not change the payoff so the two strategies have equal payoffs in this case.
- If $\max _{j\neq i}b_{j}>b_{i}$ then the bidder would lose the item either way so the strategies have equal payoffs in this case.
- If $v_{i}<\max _{j\neq i}b_{j}<b_{i}$ then only the strategy of overbidding would win the auction. The payoff would be negative for the strategy of overbidding because they paid more than their value of the item, while the payoff for a truthful bid would be zero.

Thus the strategy of bidding higher than one's true valuation is dominated by the strategy of truthfully bidding. The strategy of underbidding is also dominated by bidding truthfully. Assume that bidder i bids $b_{i}<v_{i}$ .

- If $\max _{j\neq i}b_{j}>v_{i}$ then the bidder would lose the item with a truthful bid as well as an underbid, so the strategies have equal payoffs for this case.
- If $\max _{j\neq i}b_{j}<b_{i}$ then the bidder would win the item either way so the strategies have equal payoffs in this case.
- If $b_{i}<\max _{j\neq i}b_{j}<v_{i}$ then only the strategy of truthfully bidding would win the auction. The payoff for the truthful strategy would be positive as they paid less than their value of the item, while the payoff for an underbid bid would be zero.

Thus the strategy of underbidding is dominated by the strategy of truthfully bidding. As truthful bidding dominates the other possible strategies (i.e. underbidding and overbidding), it is an optimal strategy.

## Revenue equivalence of the Vickrey auction and sealed first price auction

The two most common auctions are the sealed first price (or high-bid) auction and the open ascending price (or English) auction. In the former each buyer submits a sealed bid. The high bidder is awarded the item and pays his or her bid. In the latter, the auctioneer announces successively higher asking prices and continues until no one is willing to accept a higher price. Suppose that a buyer's valuation is v and the current asking price is b . If $v<b$ , then the buyer loses by raising his hand. If $v>b$ and the buyer is not the current high bidder, it is more profitable to bid than to let someone else be the winner. Thus it is a dominant strategy for a buyer to drop out of the bidding when the asking price reaches his or her valuation. Thus, just as in the Vickrey sealed second price auction, the price paid by the buyer with the highest valuation is equal to the second highest value.

Consider then the expected payment in the sealed second-price auction. Vickrey considered the case of two buyers and assumed that each buyer's value was an independent draw from a uniform distribution with support $[0,1]$ . With buyers bidding according to their dominant strategies, a buyer with valuation v wins if his opponent's value $x<v$ . Suppose that v is the high value. Then the winning payment is uniformly distributed on the interval $[0,v]$ and so the expected payment of the winner is

$e(v)={\tfrac {1}{2}}v.$

We now argue that in the sealed first price auction the equilibrium bid of a buyer with valuation v is

$B(v)=e(v)={\tfrac {1}{2}}v.$

That is, the payment of the winner in the sealed first-price auction is equal to the expected revenue in the sealed second-price auction.

**Proof of revenue equivalence**

Suppose that buyer 2 bids according to the strategy $B(v)=v/2$ , where $B(v)$ is the buyer's bid for a valuation v . We need to show that buyer 1's best response is to use the same strategy.

Note first that if buyer 2 uses the strategy $B(v)=v/2$ , then buyer 2's maximum bid is $B(1)=1/2$ and so buyer 1 wins with probability 1 with any bid of 1/2 or more. Consider then a bid b on the interval $[0,1/2]$ . Let buyer 2's value be x . Then buyer 1 wins if $B(x)=x/2<b$ , that is, if $x<2b$ . Under Vickrey's assumption of uniformly distributed values, the win probability is $w(b)=2b$ . Buyer 1's expected payoff is therefore

$U(b)=w(b)(v-b)=2b(v-b)={\tfrac {1}{2}}[v^{2}-(v-2b)^{2}]$

Note that $U(b)$ takes on its maximum at $b=v/2=B(v)$ .

## Use in network routing

In network routing, VCG mechanisms are a family of payment schemes based on the added value concept. The basic idea of a VCG mechanism in network routing is to pay the owner of each link or node (depending on the network model) that is part of the solution, its declared cost *plus* its added value. In many routing problems, this mechanism is not only strategyproof, but also the minimum among all strategyproof mechanisms.

In the case of network flows, unicast or multicast, a minimum-cost flow (MCF) in graph *G* is calculated based on the declared costs *d**k* of each of the links and payment is calculated as follows:

Each link (or node) $e_{k}$ in the MCF is paid

$p_{k}=d_{k}+\operatorname {MCF} (G-e_{k})-\operatorname {MCF} (G),$

where MCF(*G*) indicates the cost of the minimum-cost flow in graph *G* and *G* − *e**k* indicates graph *G* without the link *e**k*. Links not in the MCF are paid nothing. This routing problem is one of the cases for which VCG is strategyproof and minimum.

In 2004, it was shown that the expected VCG overpayment of an Erdős–Rényi random graph with *n* nodes and edge probability *p*, $\scriptstyle G\in G(n,p)$ approaches

${\frac {p}{2-p}}$

as *n*, approaches $\scriptstyle \infty$ , for $np=\omega ({\sqrt {n\log n}})$ . Prior to this result, it was known that VCG overpayment in *G*(*n*, *p*) is

$\Omega \left({\frac {1}{np}}\right)$

and

$O(1)\,$

with high probability given

$np=\omega (\log n).\,$

## Generalizations

The most obvious generalization to multiple or divisible goods is to have all winning bidders pay the amount of the highest non-winning bid. This is known as a uniform price auction. The uniform-price auction does not, however, result in bidders bidding their true valuations as they do in a second-price auction unless each bidder has demand for only a single unit. A generalization of the Vickrey auction that maintains the incentive to bid truthfully is known as the Vickrey–Clarke–Groves (VCG) mechanism. The idea in VCG is that items are assigned to maximize the sum of utilities; then each bidder pays the "opportunity cost" that their presence introduces to all the other players. This opportunity cost for a bidder is defined as the total bids of all the other bidders that would have won if the first bidder had not bid, minus the total bids of all the other actual winning bidders.

A different kind of generalization is to set a reservation price—a minimum price below which the item is not sold at all. In some cases, setting a reservation price can substantially increase the revenue of the auctioneer. This is an example of Bayesian-optimal mechanism design.

In mechanism design, the revelation principle can be viewed as a generalization of the Vickrey auction.
