---
title: "Fractional factorial design"
source: https://en.wikipedia.org/wiki/Fractional_factorial_design
domain: factorial-design
license: CC-BY-SA-4.0
tags: factorial experiment, fractional factorial, main effect, Plackett Burman
fetched: 2026-07-02
---

# Fractional factorial design

In statistics, a **fractional factorial design** is a way to conduct experiments with fewer experimental runs than a full factorial design. Instead of testing every single combination of factors, it tests only a carefully selected portion. This "fraction" of the full design is chosen to reveal the most important information about the system being studied (sparsity-of-effects principle), while significantly reducing the number of runs required. It is based on the idea that many tests in a full factorial design can be redundant. However, this reduction in runs comes at the cost of potentially more complex analysis, as some effects can become intertwined, making it impossible to isolate their individual influences. Therefore, choosing which combinations to test in a fractional factorial design must be done carefully.

## History

Fractional factorial design was introduced by British statistician David John Finney in 1945, extending previous work by Ronald Fisher on the full factorial experiment at Rothamsted Experimental Station. Developed originally for agricultural applications, it has since been applied to other areas of engineering, science, and business.

## Basic working principle

Similar to a full factorial experiment, a fractional factorial experiment investigates the effects of independent variables, known as factors, on a response variable. Each factor is investigated at different values, known as levels. The response variable is measured using a combination of factors at different levels, and each unique combination is known as a run. To reduce the number of runs in comparison to a full factorial, the experiments are designed to confound different effects and interactions, so that their impacts cannot be distinguished. If higher-order interactions between main effects are negligible, it can be considered a reasonable method to study the main effects. This is the sparsity of effects principle. Confounding is controlled by a systematic selection of runs from a full-factorial table.

## Notation

Fractional designs are expressed using the notation *l*k − p, where *l* is the number of levels of each factor, *k* is the number of factors, and *p* describes the size of the fraction of the full factorial used. Formally, p is the number of generators; relationships that determine the intentionally confounded effects that reduce the number of runs needed. Each generator halves the number of runs required. A design with *p* such generators is a 1/(*lp*)=*l−p* fraction of the full factorial design.

For example, a 25 − 2 design is 1/4 of a two-level, five-factor factorial design. Rather than the 32 runs that would be required for the full 25 factorial experiment, this experiment requires only eight runs. With two generators, the number of experiments has been halved twice.

In practice, one rarely encounters *l* > 2 levels in fractional factorial designs as the methodology to generate such designs for more than two levels is much more cumbersome. In cases requiring 3 levels for each factor, potential fractional designs to pursue are Latin squares, mutually orthogonal Latin squares, and Taguchi methods. Response surface methodology can also be a much more experimentally efficient way to determine the relationship between the experimental response and factors at multiple levels, but it requires that the levels are continuous. In determining whether more than two levels are needed, experimenters should consider whether they expect the outcome to be nonlinear with the addition of a third level. Another consideration is the number of factors, which can significantly change the experimental labor demand.

The levels of a factor are commonly coded as +1 for the higher level, and −1 for the lower level. For a three-level factor, the intermediate value is coded as 0.

To save space, the points in a factorial experiment are often abbreviated with strings of plus and minus signs. The strings have as many symbols as factors, and their values dictate the level of each factor: conventionally, - for the first (or low) level, and + for the second (or high) level. The points in a two-level experiment with two factors can thus be represented as $--$ , $+-$ , $-+$ , and $++$ .

The factorial points can also be abbreviated by (1), a, b, and ab, where the presence of a letter indicates that the specified factor is at its high (or second) level and the absence of a letter indicates that the specified factor is at its low (or first) level (for example, "a" indicates that factor A is on its high setting, while all other factors are at their low (or first) setting). (1) is used to indicate that all factors are at their lowest (or first) values. Factorial points are typically arranged in a table using Yates’ standard order: 1, a, b, ab, c, ac, bc, abc, which is created when the level of the first factor alternates with each run.

## Generation

In practice, experimenters typically rely on statistical reference books to supply the "standard" fractional factorial designs, consisting of the *principal fraction*. The *principal fraction* is the set of treatment combinations for which the generators evaluate to + under the treatment combination algebra. However, in some situations, experimenters may take it upon themselves to generate their own fractional design.

A fractional factorial experiment is generated from a full factorial experiment by choosing an *alias structure*. The alias structure determines which effects are confounded with each other. For example, the five-factor 25 − 2 can be generated by using a full three-factor factorial experiment involving three factors (say *A*,*B*, and *C*) and then choosing to confound the two remaining factors *D* and *E* with interactions generated by *D* = *A***B* and *E* = *A***C*. These two expressions are called the *generators* of the design. So for example, when the experiment is run and the experimenter estimates the effects for factor *D*, what is really being estimated is a combination of the main effect of *D* and the two-factor interaction involving *A* and *B*.

An important characteristic of a fractional design is the defining relation, which gives the set of interaction columns equal in the design matrix to a column of plus signs, denoted by *I*. For the above example, since *D* = *AB* and *E* = *AC*, then *ABD* and *ACE* are both columns of plus signs, and consequently so is *BDCE*:

*D*D* = *AB*D* = *I*

*E*E* = *AC*E* = *I*

*I*= *ABD*ACE*= *A*ABCDE* = *BCDE*

In this case, the defining relation of the fractional design is *I* = *ABD* = *ACE* = *BCDE*. The defining relation allows the alias pattern of the design to be determined and includes 2p words. Notice that in this case, the interaction effects *ABD*, *ACE*, and *BCDE* cannot be studied at all. As the number of generators and the degree of fractionation increases, more and more effects become confounded.

The alias pattern can then be determined through multiplying by each factor column. To determine how main effect A is confounded, multiply all terms in the defining relation by A:

*A*I* = *A*ABD* = *A*ACE* = *A*BCDE* *A* = *BC* = *CE* = *ABCDE*

Thus main effect A is confounded with interaction effects BC, CE, and ABCDE. Other main effects can be computed following a similar method.

| Treatment combination | I | A | B | C | D = AB | E = AC |
|---|---|---|---|---|---|---|
| de | + | − | − | − | + | + |
| a | + | + | − | − | − | − |
| be | + | − | + | − | − | + |
| abd | + | + | + | − | + | − |
| cd | + | − | − | + | + | − |
| ace | + | + | − | + | − | + |
| bc | + | − | + | + | − | − |
| abcde | + | + | + | + | + | + |

## Resolution

An important property of a fractional design is its **resolution** or ability to separate main effects and low-order interactions from one another. Formally, if the factors are binary then the resolution of the design is the minimum word length in the defining relation excluding (*I*). The resolution is denoted using Roman numerals, and it increases with the number. The most important fractional designs are those of resolution III, IV, and V: Resolutions below III are not useful and resolutions above V are wasteful (with binary factors) in that the expanded experimentation has no practical benefit in most cases—the bulk of the additional effort goes into the estimation of very high-order interactions which rarely occur in practice. The 25 − 2 design above is resolution III since its defining relation is I = ABD = ACE = BCDE.

| Resolution | Ability | Example |
|---|---|---|
| I | Not useful: an experiment of exactly one run only tests one level of a factor and hence can't even distinguish between the high and low levels of that factor | 21 − 1 with defining relation I = A |
| II | Not useful: main effects are confounded with other main effects | 22 − 1 with defining relation I = AB |
| III | Estimate main effects, but these may be confounded with two-factor interactions | 23 − 1 with defining relation I = ABC |
| IV | Estimate main effects unconfounded by two-factor interactions Estimate two-factor interaction effects, but these may be confounded with other two-factor interactions | 24 − 1 with defining relation I = ABCD |
| V | Estimate main effects unconfounded by three-factor (or less) interactions Estimate two-factor interaction effects unconfounded by two-factor interactions Estimate three-factor interaction effects, but these may be confounded with other two-factor interactions | 25 − 1 with defining relation I = ABCDE |
| VI | Estimate main effects unconfounded by four-factor (or less) interactions Estimate two-factor interaction effects unconfounded by three-factor (or less) interactions Estimate three-factor interaction effects, but these may be confounded with other three-factor interactions | 26 − 1 with defining relation I = ABCDEF |

The resolution classification system described is only used for regular designs. Regular designs have run size that equal a power of two, and only full aliasing is present. Non-regular designs, sometimes known as Plackett-Burman designs, are designs where run size is a multiple of 4; these designs introduce partial aliasing, and generalized resolution is used as design criterion instead of the resolution described previously.

Resolution III designs can be used to construct saturated designs, where N-1 factors can be investigated in only N runs. These saturated designs can be used for quick screening when many factors are involved.

## Example fractional factorial experiment

Montgomery gives the following example of a fractional factorial experiment. An engineer performed an experiment to increase the filtration rate (output) of a process to produce a chemical, and to reduce the amount of formaldehyde used in the process. The full factorial experiment is described in the Wikipedia page Factorial experiment. Four factors were considered: temperature (A), pressure (B), formaldehyde concentration (C), and stirring rate (D). The results in that example were that the main effects A, C, and D and the AC and AD interactions were significant. The results of that example may be used to simulate a fractional factorial experiment using a half-fraction of the original 2*4* = 16 run design. The table shows the 2*4*-*1* = 8 run half-fraction experiment design and the resulting filtration rate, extracted from the table for the full 16 run factorial experiment.

| A | B | C | D | Filtration Rate |
|---|---|---|---|---|
| -1 | -1 | -1 | -1 | 45 |
| 1 | -1 | -1 | 1 | 100 |
| -1 | 1 | -1 | 1 | 45 |
| 1 | 1 | -1 | -1 | 65 |
| -1 | -1 | 1 | 1 | 75 |
| 1 | -1 | 1 | -1 | 60 |
| -1 | 1 | 1 | -1 | 80 |
| 1 | 1 | 1 | 1 | 96 |

In this fractional design, each main effect is aliased with a 3-factor interaction (e.g., A = BCD), and every 2-factor interaction is aliased with another 2-factor interaction (e.g., AB = CD). The aliasing relationships are shown in the table. This is a resolution IV design, meaning that main effects are aliased with 3-way interactions, and 2-way interactions are aliased with 2-way interactions.

| Aliases |
|---|
| A = BCD |
| B = ACD |
| C = ABD |
| D = ABC |
| AB = CD |
| AC = BD |
| BC = AD |

The analysis of variance estimates of the effects are shown in the table below. From inspection of the table, there appear to be large effects due to A, C, and D. The coefficient for the AB interaction is quite small. Unless the AB and CD interactions have approximately equal but opposite effects, these two interactions appear to be negligible. If A, C, and D have large effects, but B has little effect, then the AC and AD interactions are most likely significant. These conclusions are consistent with the results of the full-factorial 16-run experiment.

| Coefficient | Estimate | Alias Structure |
|---|---|---|
| A | 19.0 | A + BCD |
| B | 1.5 | B + ACD |
| C | 14.0 | C + ABD |
| D | 16.5 | D + ABC |
| A:B | -1.0 | AB + CD |
| A:C | -18.5 | AC + BD |
| A:D | 19.0 | AD + BC |

Because B and its interactions appear to be insignificant, B may be dropped from the model. Dropping B results in a full factorial 2*3* design for the factors A, C, and D. Performing the anova using factors A, C, and D, and the interaction terms A:C and A:D, gives the results shown in the table, which are very similar to the results for the full factorial experiment experiment, but have the advantage of requiring only a half-fraction 8 runs rather than 16.

| Coefficient | Estimate | Std. Error | t value | P-value |
|---|---|---|---|---|
| Intercept | 70.75 | 0.64 | 111 | 8.11E-05 |
| A | 9.5 | 0.64 | 14.9 | 0.00447 |
| C | 7 | 0.64 | 10.98 | 0.00819 |
| D | 8.25 | 0.64 | 12.94 | 0.00592 |
| A:C | -9.25 | 0.64 | -14.51 | 0.00471 |
| A:D | 9.5 | 0.64 | 14.9 | 0.00447 |
