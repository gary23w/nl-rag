---
title: "l-diversity"
source: https://en.wikipedia.org/wiki/L-diversity
domain: k-anonymity
license: CC-BY-SA-4.0
tags: k anonymity, l diversity, t closeness, quasi identifier, data re identification
fetched: 2026-07-02
---

# *l*-diversity

***l*-diversity**, also written as ***ℓ*-diversity**, is a form of group based anonymization that is used to preserve privacy in data sets by reducing the granularity of a data representation. This reduction is a trade off that results in some loss of effectiveness of data management or mining algorithms in order to gain some privacy. The *l*-diversity model is an extension of the *k*-anonymity model which reduces the granularity of data representation using techniques including generalization and suppression such that any given record maps onto at least *k-1* other records in the data. The *l*-diversity model handles some of the weaknesses in the *k*-anonymity model where protected identities to the level of *k*-individuals is not equivalent to protecting the corresponding sensitive values that were generalized or suppressed, especially when the sensitive values within a group exhibit homogeneity. The *l*-diversity model adds the promotion of intra-group diversity for sensitive values in the anonymization mechanism.

## Attacks on *k*-anonymity

While *k*-anonymity is a promising approach to take for group based anonymization given its simplicity and wide array of algorithms that perform it, it is however susceptible to many attacks. When background knowledge is available to an attacker, such attacks become even more effective. Such attacks include:

- **Homogeneity Attack**: This attack leverages the case where all the values for a sensitive value within a set of *k* records are identical. In such cases, even though the data has been *k*-anonymized, the sensitive value for the set of *k* records may be exactly predicted.
- **Background Knowledge Attack**: This attack leverages an association between one or more quasi-identifier attributes with the sensitive attribute to reduce the set of possible values for the sensitive attribute. For example, Machanavajjhala, Kifer, Gehrke, and Venkitasubramaniam (2007) showed that knowing that heart attacks occur at a reduced rate in Japanese patients could be used to narrow the range of values for a sensitive attribute of a patient's disease.

## Formal definition

Given the existence of such attacks where sensitive attributes may be inferred for *k*-anonymity data, the *l*-diversity method was created to further *k*-anonymity by additionally maintaining the diversity of sensitive fields. The book *Privacy-Preserving Data Mining – Models and Algorithms* (2008) defines *l*-diversity as being:

> Let a q*-block be a set of tuples such that its non-sensitive values generalize to q*. A q*-block is *l*-diverse if it contains *l* "well represented" values for the sensitive attribute S. A table is *l*-diverse, if every q*-block in it is *l*-diverse.

The paper *t*-Closeness: Privacy beyond *k*-anonymity and *l*-diversity (2007) defines *l*-diversity as being:

> **The *l*-diversity Principle** – An equivalence class is said to have *l*-diversity if there are at least *l* “well-represented” values for the sensitive attribute. A table is said to have *l*-diversity if every equivalence class of the table has *l*-diversity.

Machanavajjhala et al. (2007) define "well-represented" in three possible ways:

1. **Distinct *l*-diversity** – The simplest definition ensures that at least *l* distinct values for the sensitive field in each equivalence class exist.
2. **Entropy *l*-diversity** – The most complex definition defines *Entropy* of an equivalent class *E* to be the negation of summation of *s* across the domain of the sensitive attribute of *p*(*E*,*s*)log(*p*(*E*,*s*)) where *p*(*E*,*s*) is the fraction of records in *E* that have the sensitive value *s*. A table has entropy *l*-diversity when for every equivalent class *E*, *Entropy*(*E*) ≥ log(*l*).
3. **Recursive (*c*-*l*)-diversity** – A compromise definition that ensures the most common value does not appear too often while less common values are ensured to not appear too infrequently.

Aggarwal and Yu (2008) note that when there is more than one sensitive field the *l*-diversity problem becomes more difficult due to added dimensionalities.
