---
title: "k-server problem"
source: https://en.wikipedia.org/wiki/K-server_problem
domain: online-algorithms
license: CC-BY-SA-4.0
tags: online algorithm, competitive analysis, ski rental problem, list update problem
fetched: 2026-07-02
---

# *k*-server problem

Unsolved problem in computer science

Is there a

k

-competitive algorithm for solving the

k

-server problem in an arbitrary metric space?

More unsolved problems in computer science

The ***k*-server problem** is a problem of theoretical computer science in the category of online algorithms, one of two abstract problems on metric spaces that are central to the theory of competitive analysis (the other being metrical task systems). In this problem, an online algorithm must control the movement of a set of *k* *servers*, represented as points in a metric space, and handle *requests* that are also in the form of points in the space. As each request arrives, the algorithm must determine which server to move to the requested point. The goal of the algorithm is to keep the total distance all servers move small, relative to the total distance the servers could have moved by an optimal adversary who knows in advance the entire sequence of requests.

The problem was first posed by Mark Manasse, Lyle A. McGeoch and Daniel Sleator (1988). The most prominent open question concerning the *k*-server problem is the so-called *k*-server conjecture, also posed by Manasse et al. This conjecture states that there is an algorithm for solving the *k*-server problem in an arbitrary metric space and for any number *k* of servers that has competitive ratio exactly *k*. Manasse et al. were able to prove their conjecture when *k* = 2, and for more general values of *k* for some metric spaces restricted to have exactly *k*+1 points. Marek Chrobak and Lawrence L. Larmore (1991) proved the conjecture for tree metrics. The special case of metrics in which all distances are equal is called the *paging problem* because it models the problem of page replacement algorithms in memory caches, and was also already known to have a *k*-competitive algorithm (Sleator and Tarjan 1985). Fiat et al. (1990) first proved that there exists an algorithm with finite competitive ratio for any constant *k* and any metric space, and finally Koutsoupias and Papadimitriou (1995) proved that Work Function Algorithm (WFA) has competitive ratio 2*k* - 1. However, despite the efforts of many other researchers, reducing the competitive ratio to *k* or providing an improved lower bound remains open as of 2014. The most common believed scenario is that the Work Function Algorithm is *k*-competitive. To this direction, in 2000 Bartal and Koutsoupias showed that this is true for some special cases (if the metric space is a line, a weighted star or any metric of *k*+2 points).

The *k*-server conjecture has also a version for randomized algorithms, which asks if there exists a randomized algorithm with competitive ratio O(log *k*) in any arbitrary metric space (with at least *k* + 1 points). In 2011, a randomized algorithm with competitive bound Õ(log2k log3n) was found. In 2017, a randomized algorithm with competitive bound O(log6 k) was announced, but was later retracted. In 2022 it was shown that the randomized version of the conjecture is false.

## Example

To make the problem more concrete, imagine sending customer support technicians to customers when they have trouble with their equipment. In our example problem there are two technicians, Mary and Noah, serving three customers, in San Francisco, California; Washington, DC; and Baltimore, Maryland. As a *k*-server problem, the servers are the technicians, so *k* = 2 and this is a 2-server problem. Washington and Baltimore are 35 miles (56 km) apart, while San Francisco is 3,000 miles (4,800 km) away from both, and initially Mary and Noah are both in San Francisco.

Consider an algorithm for assigning servers to requests that always assigns the closest server to the request, and suppose that each weekday morning the customer in Washington needs assistance while each weekday afternoon the customer in Baltimore needs assistance, and that the customer in San Francisco never needs assistance. Then, our algorithm will assign one of the servers (say Mary) to the Washington area, after which she will always be the closest server and always be assigned to all customer requests. Thus, every day our algorithm incurs the cost of traveling between Washington and Baltimore and back, 70 miles (110 km). After a year of this request pattern, the algorithm will have incurred 20,500 miles (33,000 km) travel: 3,000 to send Mary to the East Coast, and 17,500 for the trips between Washington and Baltimore. On the other hand, an optimal adversary who knows the future request schedule could have sent both Mary and Noah to Washington and Baltimore respectively, paying 6,000 miles (9,700 km) of travel once but then avoiding any future travel costs. The competitive ratio of our algorithm on this input is 20,500/6,000 or approximately 3.4, and by adjusting the parameters of this example the competitive ratio of this algorithm can be made arbitrarily large.

Thus we see that always assigning the closest server can be far from optimal. On the other hand, it seems foolish for an algorithm that does not know future requests to send both of its technicians away from San Francisco, as the next request could be in that city and it would have to send someone back immediately. So it seems that it is difficult or impossible for a *k*-server algorithm to perform well relative to its adversary. However, for the 2-server problem, there exists an algorithm that always has a total travel distance of at most twice the adversary's distance. The *k*-server conjecture states that similar solutions exist for problems with any larger number of technicians.

## The offline k-server problem

The k-server problem is also useful in an offline setting, that is, when the sequence of requests is completely known. For examples, for some algorithms the sequence of memory accesses is independent of the input (an example is matrix multiplication), and so the paging problem can be solved offline. This problem has been shown to be solvable in polynomial time.
