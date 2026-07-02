---
title: "Blocking (statistics)"
source: https://en.wikipedia.org/wiki/Blocking_(statistics)
domain: experimental-design
license: CC-BY-SA-4.0
tags: design of experiments, statistical blocking, treatment randomization, experimental replication
fetched: 2026-07-02
---

# Blocking (statistics)

In the statistical theory of the design of experiments, **blocking** is the arranging of experimental units that are similar to one another in groups (blocks) based on one or more variables. These variables are chosen carefully to minimize the effect of their variability on the observed outcomes. There are different ways that blocking can be implemented, resulting in different confounding effects. However, the different methods share the same purpose: to control variability introduced by specific factors that could influence the outcome of an experiment. The roots of blocking originated from the statistician, Ronald Fisher, following his development of ANOVA.

## History

The use of blocking in experimental design has an evolving history that spans multiple disciplines. The foundational concepts of blocking date back to the early 20th century with statisticians like Ronald A. Fisher. His work in developing analysis of variance (ANOVA) set the groundwork for grouping experimental units to control for extraneous variables. Blocking evolved over the years, leading to the formalization of randomized block designs and Latin square designs. Today, blocking still plays a pivotal role in experimental design, and in recent years, advancements in statistical software and computational capabilities have allowed researchers to explore more intricate blocking designs.

## Use

We often want to reduce or eliminate the influence of some confounding factor when designing an experiment. We can sometimes do this by "blocking", which involves the separate consideration of blocks of data that have different levels of exposure to that factor.

### Examples

- **Male and female**: An experiment is designed to test a new drug on patients. There are two levels of the treatment, *drug*, and *placebo*, administered to *male* and *female* patients in a double blind trial. The sex of the patient is a *blocking* factor accounting for treatment variability between *males* and *females*. This reduces sources of variability and thus leads to greater precision.
- **Elevation**: An experiment is designed to test the effects of a new pesticide on a specific patch of grass. The grass area contains a major elevation change and thus consists of two distinct regions – 'high elevation' and 'low elevation'. A treatment group (the new pesticide) and a placebo group are applied to both the high elevation and low elevation areas of grass. In this instance the researcher is blocking the elevation factor which may account for variability in the pesticide's application.
- **Intervention**: Suppose a process is invented that intends to make the soles of shoes last longer, and a plan is formed to conduct a field trial. Given a group of *n* volunteers, one possible design would be to give *n*/2 of them shoes with the new soles and *n*/2 of them shoes with the ordinary soles, randomizing the assignment of the two kinds of soles. This type of experiment is a completely randomized design. Both groups are then asked to use their shoes for a period of time, and then measure the degree of wear of the soles. This is a workable experimental design, but purely from the point of view of statistical accuracy (ignoring any other factors), a better design would be to give each person one regular sole and one new sole, randomly assigning the two types to the left and right shoe of each volunteer. Such a design is called a "randomized complete block design." This design will be more sensitive than the first, because each person is acting as his/her own control and thus the control group is more closely matched to the treatment group block design

### Nuisance variables

In the examples listed above, a nuisance variable is a variable that is not the primary focus of the study but can affect the outcomes of the experiment. They are considered potential sources of variability that, if not controlled or accounted for, may confound the interpretation between the independent and dependent variables.

To address nuisance variables, researchers can employ different methods such as blocking or randomization. Blocking involves grouping experimental units based on levels of the nuisance variable to control for its influence. Randomization helps distribute the effects of nuisance variables evenly across treatment groups.

By using one of these methods to account for nuisance variables, researchers can enhance the internal validity of their experiments, ensuring that the effects observed are more likely attributable to the manipulated variables rather than extraneous influences.

In the first example provided above, the sex of the patient would be a nuisance variable. For example, consider if the drug was a diet pill and the researchers wanted to test the effect of the diet pills on weight loss. The explanatory variable is the diet pill and the response variable is the amount of weight loss. Although the sex of the patient is not the main focus of the experiment—the effect of the drug is—it is possible that the sex of the individual will affect the amount of weight lost.

### Blocking used for nuisance factors that can be controlled

In the statistical theory of the design of experiments, blocking is the arranging of experimental units in groups (blocks) that are similar to one another. Typically, a blocking factor is a source of variability that is not of primary interest to the experimenter.

When studying probability theory the blocks method consists of splitting a sample into blocks (groups) separated by smaller subblocks so that the blocks can be considered almost independent. The blocks method helps proving limit theorems in the case of dependent random variables.

The blocks method was introduced by S. Bernstein: The method was successfully applied in the theory of sums of dependent random variables and in extreme value theory.

#### Example

In our previous diet pills example, a blocking factor could be the sex of a patient. We could put individuals into one of two blocks (male or female). And within each of the two blocks, we can randomly assign the patients to either the diet pill (treatment) or placebo pill (control).  By blocking on sex, this source of variability is controlled, therefore, leading to greater interpretation of how the diet pills affect weight loss.

### Definition of blocking factors

A nuisance factor is used as a blocking factor if every level of the primary factor occurs the same number of times with each level of the nuisance factor. The analysis of the experiment will focus on the effect of varying levels of the primary factor within each block of the experiment.

### Block a few of the most important nuisance factors

The general rule is:

"Block what you can; randomize what you cannot."

Blocking is used to remove the effects of a few of the most important nuisance variables. Randomization is then used to reduce the contaminating effects of the remaining nuisance variables. For important nuisance variables, blocking will yield higher significance in the variables of interest than randomizing.

## Implementation

Implementing blocking in experimental design involves a series of steps to effectively control for extraneous variables and enhance the precision of treatment effect estimates.

### Identify nuisance variables

Identify potential factors that are not the primary focus of the study but could introduce variability.

### Select appropriate blocking factors

Carefully choose blocking factors based on their relevance to the study as well as their potential to confound the primary factors of interest.

### Define block sizes

There are consequences to partitioning a certain sized experiment into a certain number of blocks as the number of blocks determines the number of confounded effects.

### Assign treatments to blocks

You may choose to randomly assign experimental units to treatment conditions within each block which may help ensure that any unaccounted for variability is spread evenly across treatment groups. However, depending on how you assign treatments to blocks, you may obtain a different number of confounded effects. Therefore, the number of as well as which specific effects get confounded can be chosen which means that assigning treatments to blocks is superior over random assignment.

### Replication

By running a different design for each replicate, where a different effect gets confounded each time, the interaction effects are partially confounded instead of completely sacrificing one single effect. Replication enhances the reliability of results and allows for a more robust assessment of treatment effects.

## Example

### Table

One useful way to look at a randomized block experiment is to consider it as a collection of completely randomized experiments, each run within one of the blocks of the total experiment.

| Name of design | Number of factors *k* | Number of runs *n* |
|---|---|---|
| 2-factor RBD | 2 | *L*1 * *L*2 |
| 3-factor RBD | 3 | *L*1 * *L*2 * *L*3 |
| 4-factor RBD | 4 | *L*1 * *L*2 * *L*3 * *L*4 |
| $\vdots$ | $\vdots$ | $\vdots$ |
| *k*-factor RBD | *k* | *L*1 * *L*2 * $\cdots$ * *Lk* |

with

L

1

= number of levels (settings) of factor 1

L

2

= number of levels (settings) of factor 2

L

3

= number of levels (settings) of factor 3

L

4

= number of levels (settings) of factor 4

$\vdots$

L

k

= number of levels (settings) of factor

k

### Example

Suppose engineers at a semiconductor manufacturing facility want to test whether different wafer implant material dosages have a significant effect on resistivity measurements after a diffusion process taking place in a furnace. They have four different dosages they want to try and enough experimental wafers from the same lot to run three wafers at each of the dosages.

The nuisance factor they are concerned with is "furnace run" since it is known that each furnace run differs from the last and impacts many process parameters.

An ideal way to run this experiment would be to run all the 4x3=12 wafers in the same furnace run. That would eliminate the nuisance furnace factor completely. However, regular production wafers have furnace priority, and only a few experimental wafers are allowed into any furnace run at the same time.

A non-blocked way to run this experiment would be to run each of the twelve experimental wafers, in random order, one per furnace run. That would increase the experimental error of each resistivity measurement by the run-to-run furnace variability and make it more difficult to study the effects of the different dosages. The blocked way to run this experiment, assuming you can convince manufacturing to let you put four experimental wafers in a furnace run, would be to put four wafers with different dosages in each of three furnace runs. The only randomization would be choosing which of the three wafers with dosage 1 would go into furnace run 1, and similarly for the wafers with dosages 2, 3 and 4.

#### Description of the experiment

Let *X*1 be dosage "level" and *X*2 be the blocking factor furnace run. Then the experiment can be described as follows:

k

= 2 factors (1 primary factor

X

1

and 1 blocking factor

X

2

)

L

1

= 4 levels of factor

X

1

L

2

= 3 levels of factor

X

2

n

= 1 replication per cell

N

=

L

1

*

L

2

= 4 * 3 = 12 runs

Before randomization, the design trials look like:

| *X*1 | *X*2 |
|---|---|
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 2 | 2 |
| 2 | 3 |
| 3 | 1 |
| 3 | 2 |
| 3 | 3 |
| 4 | 1 |
| 4 | 2 |
| 4 | 3 |

#### Matrix representation

An alternate way of summarizing the design trials would be to use a 4x3 matrix whose 4 rows are the levels of the treatment *X*1 and whose columns are the 3 levels of the blocking variable *X*2. The cells in the matrix have indices that match the *X*1, *X*2 combinations above.

| **Treatment** | **Block 1** | **Block 2** | **Block 3** |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 1 | 1 | 1 |
| 4 | 1 | 1 | 1 |

By extension, note that the trials for any K-factor randomized block design are simply the cell indices of a *k* dimensional matrix.

### Model

The model for a randomized block design with one nuisance variable is

$Y_{ij}=\mu +T_{i}+B_{j}+\mathrm {random\ error}$

where

Y

ij

is any observation for which

X

1

=

i

and

X

2

=

j

X

1

is the primary factor

X

2

is the blocking factor

μ

is the general location parameter (i.e., the mean)

T

i

is the effect for being in treatment

i

(of factor

X

1

)

B

j

is the effect for being in block

j

(of factor

X

2

)

### Estimates

Estimate for

μ

:

${\overline {Y}}$

= the average of all the data

Estimate for

T

i

:

${\overline {Y}}_{i\cdot }-{\overline {Y}}$

with

${\overline {Y}}_{i\cdot }$

= average of all

Y

for which

X

1

=

i

.

Estimate for

B

j

:

${\overline {Y}}_{\cdot j}-{\overline {Y}}$

with

${\overline {Y}}_{\cdot j}$

= average of all

Y

for which

X

2

=

j

.

### Generalizations

- Generalized randomized block designs (GRBD) allow tests of block–treatment interaction, and has exactly one blocking factor like the RCBD.
- Latin squares (and other row–column designs) have two blocking factors that are believed to have no interaction.
- Latin hypercube sampling
- Graeco-Latin squares
- Hyper-Graeco-Latin square designs
