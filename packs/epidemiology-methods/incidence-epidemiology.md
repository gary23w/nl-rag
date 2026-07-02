---
title: "Incidence (epidemiology)"
source: https://en.wikipedia.org/wiki/Incidence_(epidemiology)
domain: epidemiology-methods
license: CC-BY-SA-4.0
tags: epidemiology methods, cohort study, case control study, confidence interval
fetched: 2026-07-02
---

# Incidence (epidemiology)

In epidemiology, **incidence** reflects the number of new cases of a given medical condition in a population within a specified period of time.

## Incidence proportion

**Incidence proportion** (**IP**), also known as **cumulative incidence**, is defined as the probability that a particular event, such as occurrence of a particular disease, has occurred in a specified period:

${\text{Incidence}}={\frac {\text{number of subjects developing disease over a certain period}}{\text{total number of subjects followed over that period}}}$

For example, if a population contains 1,000 persons and 28 develop a condition from the time the disease first occurred until two years later, the cumulative incidence is 28 cases per 1,000 persons, i.e. 2.8%.

## Incidence rate

The **incidence rate** can be calculated by dividing the number of subjects developing a disease by the total time at risk from all patients:

${\text{Incidence rate}}={\frac {\text{number of subjects developing a disease}}{\text{total time at risk for whole population to get the disease}}}$

One of the important advantages of incidence rate is that it doesn't require all subjects to be present for the whole study because it's only interested in the time at risk.

## Incidence vs. prevalence

Incidence should not be confused with prevalence, which is the proportion of cases in the population at a given time rather than rate of occurrence of new cases. Thus, incidence conveys information about the risk of contracting the disease, whereas prevalence indicates how widespread the disease is. Prevalence is the proportion of the total number of cases to the total population and is more a measure of the burden of the disease on society with no regard to time at risk or when subjects may have been exposed to a possible risk factor. Prevalence can also be measured with respect to a specific subgroup of a population. Incidence is usually more useful than prevalence in understanding the disease etiology: for example, if the incidence rate of a disease in a population increases, then there is a risk factor that promotes the incidence.

For example, consider a disease that takes a long time to cure and was widespread in 2002 but dissipated in 2003. This disease will have both high incidence and high prevalence in 2002, but in 2003 it will have a low incidence yet will continue to have a high prevalence (because it takes a long time to cure, so the fraction of individuals that are affected remains high). In contrast, a disease that has a short duration may have a low prevalence and a high incidence. When the incidence is approximately constant for the duration of the disease, prevalence is approximately the product of disease incidence and average disease duration, so *prevalence = incidence × duration*. The importance of this equation is in the relation between prevalence and incidence; for example, when the incidence increases, then the prevalence must also increase. Note that this relation does not hold for age-specific prevalence and incidence, where the relation becomes more complicated.

### Example

Consider the following example. Say you are looking at a sample population of 225 people, and want to determine the incidence rate of developing HIV over a 10-year period:

- At the beginning of the study (t=0) you find 25 cases of existing HIV. These people are not counted as they cannot develop HIV a second time.
- A follow-up at 5 years (t=5 years) finds 20 new cases of HIV.
- A second follow-up at the end of the study (t=10 years) finds 30 new cases.

If you were to measure prevalence you would simply take the total number of cases (25 + 20 + 30 = 75) and divide by your sample population (225). So prevalence would be 75/225 = 0.33 or 33% (by the end of the study). This tells you how widespread HIV is in your sample population, but little about the actual risk of developing HIV for any person over a coming year.

To measure incidence rate you must take into account how many years each person contributed to the study, and when they developed HIV because when a subject develops HIV he stops being at risk. When it is not known exactly when a person develops the disease in question, epidemiologists frequently use the actuarial method, and assume it was developed at a half-way point between follow-ups. In this calculation:

- At 5 yrs you found 20 new cases, so you assume they developed HIV at 2.5 years, thus contributing (20 * 2.5) = 50 person-years of disease-free life.
- At 10 years you found 30 new cases. These people did not have HIV at 5 years, but did at 10, so you assume they were infected at 7.5 years, thus contributing (30 * 7.5) = 225 person-years of disease-free life. That is a total of (225 + 50) = 275 person years so far.
- You also want to account for the 150 people who never had or developed HIV over the 10-year period, (150 * 10) contributing 1500 person-years of disease-free life.

That is a total of (1500 + 275) = 1775 person-years of life. Now take the 50 new cases of HIV, and divide by 1775 to get 0.028, or 28 cases of HIV per 1000 population, per year. In other words, if you were to follow 1000 people for one year, you would see 28 new cases of HIV. This is a much more accurate measure of risk than prevalence.
