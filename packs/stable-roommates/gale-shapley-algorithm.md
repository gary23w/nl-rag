---
title: "Gale–Shapley algorithm"
source: https://en.wikipedia.org/wiki/Gale–Shapley_algorithm
domain: stable-roommates
license: CC-BY-SA-4.0
tags: stable roommates problem, irving algorithm, stable matching, preference list
fetched: 2026-07-02
---

# Gale–Shapley algorithm

In mathematics, economics, and computer science, the **Gale–Shapley algorithm** (also known as the **deferred acceptance algorithm**, **propose-and-reject algorithm**, or **Boston Pool algorithm**) is an algorithm for finding a solution to the stable matching problem. It is named for David Gale and Lloyd Shapley, who published it in 1962, although it had been used for the National Resident Matching Program since the early 1950s. Shapley and Alvin E. Roth (who pointed out its prior application) won the 2012 Nobel Prize in Economics for work including this algorithm.

The stable matching problem seeks to pair up equal numbers of participants of two types, using preferences from each participant. The pairing must be stable: no pair of matched participants should mutually prefer each other to their assigned match. In each round of the Gale–Shapley algorithm, unmatched participants of one type propose a match to the next participant on their preference list. Each proposal is accepted if its recipient prefers it to their current match. The resulting procedure is a truthful mechanism from the point of view of the proposing participants, who receive their most-preferred pairing consistent with stability. In contrast, the recipients of proposals receive their least-preferred pairing. The algorithm can be implemented to run in time quadratic in the number of participants, and linear in the size of the input to the algorithm.

The stable matching problem, and the Gale–Shapley algorithm solving it, have widespread real-world applications, including matching American medical students to residencies and French university applicants to schools. For more, see Stable marriage problem § Applications.

## Background

The stable matching problem, in its most basic form, takes as input equal numbers of two types of participants (n job applicants and n employers, for example), and an ordering for each participant giving their preference for whom to be matched to among the participants of the other type. A matching pairs each participant of one type with a participant of the other type. A matching is *not* stable if:

1. There is an element *A* of the first matched set which prefers some given element *B* of the second matched set over the element to which *A* is already matched, and
2. *B* also prefers *A* over the element to which *B* is already matched.

In other words, a matching is stable when there is no pair (*A*, *B*) where both participants prefer each other to their matched partners. If such a pair exists, the matching is not stable, in the sense that the members of this pair would prefer to leave the system and be matched to each other, possibly leaving other participants unmatched. A stable matching always exists, and the algorithmic problem solved by the Gale–Shapley algorithm is to find one.

The stable matching problem has also been called the *stable marriage problem*, using a metaphor of marriage between men and women, and many sources describe the Gale–Shapley algorithm in terms of marriage proposals. However, this metaphor has been criticized as both sexist and unrealistic: the steps of the algorithm do not accurately reflect typical or even stereotypical human behavior.

## Solution

In 1962, David Gale and Lloyd Shapley proved that, for any equal number of participants of each type, it is always possible to find a matching in which all pairs are stable. They presented an algorithm to do so. In 1984, Alvin E. Roth observed that essentially the same algorithm had already been in practical use since the early 1950s, as the "Boston Pool algorithm" used by the National Resident Matching Program.

The Gale–Shapley algorithm involves a number of "rounds" (or "iterations"). In terms of job applicants and employers, it can be expressed as follows:

- In each round, one or more employers with open job positions each make a job offer to the applicant they prefer, among the ones they have not yet already made an offer to.
- Each applicant who has received an offer evaluates it against their current position (if they have one). If the applicant is not yet employed, or if they receive an offer from an employer they like better than their current employer, they accept the best new offer and become matched to the new employer (possibly leaving a previous employer with an open position). Otherwise, they reject the new offer.
- This process is repeated until all employers have either filled their positions or exhausted their lists of applicants.

### Implementation details and time analysis

To implement the algorithm efficiently, each employer needs to be able to find its next applicant quickly, and each applicant needs to be able to compare employers quickly. One way to do this is to number each applicant and each employer from 1 to n , where n is the number of employers and applicants, and to store the following data structures:

- A set of employers with unfilled positions
- A one-dimensional array indexed by employers, specifying the preference index of the next applicant to whom the employer would send an offer, initially 1 for each employer
- A one-dimensional array indexed by applicants, specifying their current employer, initially a sentinel value such as 0 indicating they are unemployed
- A two-dimensional array indexed by an applicant and an employer, specifying the position of that employer in the applicant's preference list
- A two-dimensional array indexed by an employer and a number i from 1 to n , naming the applicant who is each employer's i th preference

Setting up these data structures takes $O(n^{2})$ time. With these structures it is possible to find an employer with an unfilled position, make an offer from that employer to their next applicant, determine whether the offer is accepted, and update all of the data structures to reflect the results of these steps, in constant time per offer. Once the algorithm terminates, the resulting matching can be read off from the array of employers for each applicant. There can be $O(n^{2})$ offers before each employer runs out of offers to make, so the total time is $O(n^{2})$ .

Although this time bound is quadratic in the number of participants, it may be considered as linear time when measured in terms of the size of the input, two matrices of preferences of size $O(n^{2})$ .

### Correctness guarantees

This algorithm guarantees that:

**Everyone gets matched**

At the end, there cannot be an applicant and employer both unmatched. An employer left unmatched at the end of the process must have made an offer to all applicants. But an applicant who receives an offer remains employed for the rest of the process, so there can be no unemployed applicants. Since the numbers of applicants and job openings are equal, there can also be no open positions remaining.

**The matches are stable**

No applicant

X

and employer

Y

can prefer each other over their final match. If

Y

makes an offer to

X

, then

X

would only reject

Y

after receiving an even better offer, so

X

cannot prefer

Y

to their final match. And if

Y

stops making offers before reaching

X

in their preference list,

Y

cannot prefer

X

to their final match. In either case,

X

and

Y

do not form an unstable pair.

## Optimality of the solution

There may be many stable matchings for the same system of preferences. This raises the question: which matching is returned by the Gale–Shapley algorithm? Is it the matching better for applicants, for employers, or an intermediate one? As it turns out, the Gale–Shapley algorithm in which employers make offers to applicants always yields the same stable matching (regardless of the order in which job offers are made), and its choice is the stable matching that is the *best for all employers* and *worst for all applicants* among all stable matchings.

In a reversed form of the algorithm, each round consists of unemployed applicants writing a single job application to their preferred employer, and the employer either accepting the application (possibly firing an existing employee to do so) or rejecting it. This produces a matching that is best for all applicants and worst for all employers among all stable matchings. These two matchings are the top and bottom elements of the lattice of stable matchings.

In both forms of the algorithm, one group of participants proposes matches, and the other group decides whether to accept or reject each proposal. The matching is always best for the group that makes the propositions, and worst for the group that decides how to handle each proposal.

## Strategic considerations

The Gale–Shapley algorithm is a truthful mechanism from the point of view of the proposing side. This means that no proposer can get a better matching by misrepresenting their preferences. Moreover, the Gale–Shapley algorithm is even *group-strategy proof* for proposers, i.e., no coalition of proposers can coordinate a misrepresentation of their preferences such that all proposers in the coalition are strictly better-off. However, it is possible for some coalition to misrepresent their preferences such that some proposers are better-off, and the others retain the same partner.

The Gale–Shapley algorithm is non-truthful for the non-proposing participants. Each may be able to misrepresent their preferences and get a better match. A particular form of manipulation is *truncation*: presenting only the topmost alternatives, implying that the bottom alternatives are not acceptable at all. Under complete information, it is sufficient to consider misrepresentations of the form of truncation strategies. However, successful misrepresentation requires knowledge of the other agents' preferences; without such knowledge, misrepresentation can give an agent a worse assignment. Moreover, even after an agent sees the final matching, they cannot deduce a strategy that would guarantee a better outcome in hindsight. This makes the Gale–Shapley algorithm a *regret-free truth-telling mechanism*. Moreover, in the Gale–Shapley algorithm, truth-telling is the only strategy that guarantees no regret. The Gale–Shapley algorithm is the only regret-free mechanism in the class of quantile-stable matching mechanisms.

## Generalizations

In their original work on the problem, Gale and Shapley considered a more general form of the stable matching problem, suitable for university and college admission. In this problem, each university or college may have its own *quota*, a target number of students to admit, and the number of students applying for admission may differ from the sum of the quotas, necessarily causing either some students to remain unmatched or some quotas to remain unfilled. Additionally, preference lists may be incomplete: if a university omits a student from their list, it means they would prefer to leave their quota unfilled than to admit that student, and if a student omits a university from their list, it means they would prefer to remain unadmitted than to go to that university. Nevertheless, it is possible to define stable matchings for this more general problem, to prove that stable matchings always exist, and to apply the same algorithm to find one.

A form of the Gale–Shapley algorithm, performed through a real-world protocol rather than calculated on computers, has been used for coordinating higher education admissions in France since 2018, through the Parcoursup system. In this process, over the course of the summer before the start of school, applicants receive offers of admission, and must choose in each round of the process whether to accept any new offer (and if so turn down any previous offer that they accepted). The method is complicated by additional constraints that make the problem it solves not exactly the stable matching problem. It has the advantage that the students do not need to commit to their preferences at the start of the process, but rather can determine their own preferences as the algorithm progresses, on the basis of head-to-head comparisons between offers that they have received. It is important that this process performs a small number of rounds of proposals, so that it terminates before the start date of the schools, but although high numbers of rounds can occur in theory, they tend not to occur in practice. It has been shown theoretically that, if the Gale–Shapley algorithm needs to be terminated early, after a small number of rounds in which every vacant position makes a new offer, it nevertheless produces matchings that have a high ratio of matched participants to unstable pairs.

## Parallelization

The Gale–Shapley algorithm has a natural source of parallelism that makes it suitable for parallel hardware such as multicore CPUs and graphics processing units (GPUs). In each round, all employers with unfilled positions can independently advance along their preference lists and make offers concurrently. A parallel implementation can assign threads to independent employers so that many offers are made simultaneously. When multiple employers make offers to the same applicant, synchronization primitives are used to resolve the competing offers, ensuring that only the applicant’s most-preferred employer is tentatively accepted while the rejected employers continue to their next choices.

To reduce synchronization overhead, it is advantageous to avoid repeatedly returning rejected employers to the shared set of employers with unfilled positions, since concurrent updates to this set require synchronization. Instead, a rejected employer immediately continues to the next applicant on its preference list. If an applicant accepts a new offer, the displaced employer likewise continues from its next preference.

Other optimization techniques include locality-aware data structures, which combine the employer preference array with the applicant rank array to reduce random memory accesses and improve cache efficiency, and advanced synchronization primitives, which resolve contention among simultaneous offers more efficiently. Heterogeneous approaches further improve performance by using the GPU for highly parallel stages and switching to the CPU when few employers remain unmatched, avoiding GPU underutilization during mostly sequential work.

## Recognition

Shapley and Roth were awarded the 2012 Nobel Memorial Prize in Economic Sciences "for the theory of stable allocations and the practice of market design". Gale had died in 2008, making him ineligible for the prize.
