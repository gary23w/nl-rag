---
title: "t-closeness"
source: https://en.wikipedia.org/wiki/T-closeness
domain: k-anonymity
license: CC-BY-SA-4.0
tags: k anonymity, l diversity, t closeness, quasi identifier, data re identification
fetched: 2026-07-02
---

# *t*-closeness

***t*-closeness** is a further refinement of *l*-diversity group based anonymization that is used to preserve privacy in data sets by reducing the granularity of a data representation. This reduction is a trade off that results in some loss of effectiveness of data management or data mining algorithms in order to gain some privacy. The *t*-closeness model extends the *l*-diversity model by treating the values of an attribute distinctly by taking into account the distribution of data values for that attribute.

## Formal definition

Given the existence of data breaches where sensitive attributes may be inferred based upon the distribution of values for *l*-diverse data, the *t*-closeness method was created to further *l*-diversity by additionally maintaining the distribution of sensitive fields. The original paper by Ninghui Li, Tiancheng Li, and Suresh Venkatasubramanian defines *t*-closeness as:

> **The *t*-closeness Principle:** An equivalence class is said to have *t*-closeness if the distance between the distribution of a sensitive attribute in this class and the distribution of the attribute in the whole table is no more than a threshold *t*. A table is said to have *t*-closeness if all equivalence classes have *t*-closeness.

Charu Aggarwal and Philip S. Yu further state in their book on privacy-preserving data mining that with this definition, threshold *t* gives an upper bound on the difference between the distribution of the sensitive attribute values within an anonymized group as compared to the global distribution of values. They also state that for numeric attributes, using *t*-closeness anonymization is more effective than many other privacy-preserving data mining methods.

## Data breaches and *l*-diversity

In real data sets attribute values may be skewed or semantically similar. However, accounting for value distributions may cause difficulty in creating feasible *l*-diverse representations. The *l*-diversity technique is useful in that it may hinder an attacker leveraging the global distribution of an attribute's data values in order to infer information about sensitive data values. Not every value may exhibit equal sensitivity, for example, a rare positive indicator for a disease may provide more information than a common negative indicator. Because of examples like this, *l*-diversity may be difficult and unnecessary to achieve when protecting against attribute disclosure. Alternatively, sensitive information leaks may occur because while *l*-diversity requirement ensures “diversity” of sensitive values in each group, it does not recognize that values may be semantically close, for example, an attacker could deduce a stomach disease applies to an individual if a sample containing the individual only listed three different stomach diseases.
