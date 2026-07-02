---
title: "Replication (statistics)"
source: https://en.wikipedia.org/wiki/Replication_(statistics)
domain: experimental-design
license: CC-BY-SA-4.0
tags: design of experiments, statistical blocking, treatment randomization, experimental replication
fetched: 2026-07-02
---

# Replication (statistics)

In engineering, science, and statistics, **replication** is the process of repeating a study or experiment under the same or similar conditions. It is a crucial step to test the original claim and confirm or reject the accuracy of results as well as for identifying and correcting the flaws in the original experiment. ASTM, in standard E1847, defines replication as "... the repetition of the set of all the treatment combinations to be compared in an experiment. Each of the repetitions is called a ***replicate***."

For a full factorial design, replicates are multiple experimental runs with the same factor levels. You can replicate combinations of factor levels, groups of factor level combinations, or even entire designs. For instance, consider a scenario with three factors, each having two levels, and an experiment that tests every possible combination of these levels (a full factorial design). One complete replication of this design would comprise 8 runs ( $2^{3}$ ). The design can be executed once or with several replicates.

There are two main types of replication in statistics. First, there is a type called “exact replication” (also called "direct replication"), which involves repeating the study as closely as possible to the original to see whether the original results can be precisely reproduced. For instance, repeating a study on the effect of a specific diet on weight loss using the same diet plan and measurement methods. The second type of replication is called “conceptual replication.” This involves testing the same theory as the original study but with different conditions. For example, testing the same diet's effect on blood sugar levels instead of weight loss, using different measurement methods.

Both exact (direct) replications and conceptual replications are important. Direct replications help confirm the accuracy of the findings within the conditions that were initially tested. On the hand conceptual replications examine the validity of the theory behind those findings and explore different conditions under which those findings remain true. In essence conceptual replication provides insights, into how generalizable the findings are.

## The difference between replicates and repeats

Replication is not the same as repeated measurements of the same item. Both repeat and replicate measurements involve multiple observations taken at the same levels of experimental factors. However, repeat measurements are collected during a single experimental session, while replicate measurements are gathered across different experimental sessions. Replication in statistics evaluates the consistency of experiment results across different trials to ensure external validity, while repetition measures precision and internal consistency within the same or similar experiments.

Replicates Example: Testing a new drug's effect on blood pressure in separate groups on different days.

Repeats Example: Measuring blood pressure multiple times in one group during a single session.

## Statistical methods in replication

In replication studies within the field of statistics, several key methods and concepts are employed to assess the reliability of research findings. Here are some of the main statistical methods and concepts used in replication:

P-Values: The p-value is a measure of the probability that the observed data would occur by chance if the null hypothesis were true. In replication studies p-values help us determine whether the findings can be consistently replicated. A low p-value in a replication study indicates that the results are not likely due to random chance. For example, if a study found a statistically significant effect of a test condition on an outcome, and the replication find statistically significant effects as well, this suggests that the original finding is likely reproducible.

Confidence Intervals: Confidence intervals provide a range of values within which the true effect size is likely to fall. In replication studies, comparing the confidence intervals of the original study and the replication can indicate whether the results are consistent. For example, if the original study reports a treatment effect with a 95% confidence interval of [5, 10], and the replication study finds a similar effect with a confidence interval of [6, 11], this overlap indicates consistent findings across both studies.

## Example

As an example, consider a continuous process which produces items. Batches of items are then processed or treated. Finally, tests or measurements are conducted. Several options might be available to obtain ten test values. Some possibilities are:

- One finished and treated item might be measured repeatedly to obtain ten test results. Only one item was measured so there is no replication. The repeated measurements help identify observational error.
- Ten finished and treated items might be taken from a batch and each measured once. This is not full replication because the ten samples are not random and not representative of the continuous nor batch processing.
- Five items are taken from the continuous process based on sound statistical sampling. These are processed in a batch and tested twice each. This includes replication of initial samples but does not allow for batch-to-batch variation in processing. The repeated tests on each provide some measure and control of testing error.
- Five items are taken from the continuous process based on sound statistical sampling. These are processed in five different batches and tested twice each. This plan includes proper replication of initial samples and also includes batch-to-batch variation. The repeated tests on each provide some measure and control of testing error.
- For proper sampling, a process or batch of products should be in reasonable statistical control; inherent random variation is present but variation due to assignable (special) causes is not. Evaluation or testing of a single item does not allow for item-to-item variation and may not represent the batch or process. Replication is needed to account for this variation among items and treatments.

Each option would call for different data analysis methods and yield different conclusions.
