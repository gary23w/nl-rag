---
title: "k-anonymity"
source: https://en.wikipedia.org/wiki/K-anonymity
domain: k-anonymity
license: CC-BY-SA-4.0
tags: k anonymity, l diversity, t closeness, quasi identifier, data re identification
fetched: 2026-07-02
---

# *k*-anonymity

***k*-anonymity** is a property possessed by certain anonymized data. The term *k*-anonymity was first introduced by Pierangela Samarati and Latanya Sweeney in a paper published in 1998, although the concept dates to a 1986 paper by Tore Dalenius.

*k*-anonymity is an attempt to solve the problem "Given person-specific field-structured data, produce a release of the data with scientific guarantees that the individuals who are the subjects of the data cannot be re-identified while the data remain practically useful." A release of data is said to have the *k*-anonymity property if the information for each person contained in the release cannot be distinguished from at least $k-1$ individuals whose information also appears in the release. The guarantees provided by *k*-anonymity are aspirational, not mathematical.

## Methods for *k*-anonymization

To use *k*-anonymity to process a dataset so that it can be released with privacy protection, a data scientist must first examine the dataset and decide whether each attribute (column) is an *identifier* (identifying), a *non-identifier* (not-identifying), or a *quasi-identifier* (somewhat identifying). Identifiers such as names are suppressed, non-identifying values are allowed to remain, and the quasi-identifiers need to be processed so that every distinct combination of quasi-identifiers designates at least *k* records.

The example table below presents a fictional, non-anonymized database consisting of the patient records for a fictitious hospital. The *Name* column is an identifier, *Age*, *Gender*, *State of domicile*, and *Religion* are quasi-identifiers, and *Disease* is a non-identifying sensitive value. But what about *Height* and *Weight*? Are they also non-identifying sensitive values, or are they quasi-identifiers?

| Name | Age | Gender | Height | Weight | State of domicile | Religion | Disease |
|---|---|---|---|---|---|---|---|
| Ramsha | 30 | Female | 165 cm | 72 kg | Tamil Nadu | Hindu | Cancer |
| Yadu | 24 | Female | 162 cm | 70 kg | Kerala | Hindu | Viral infection |
| Salima | 28 | Female | 170 cm | 68 kg | Tamil Nadu | Muslim | Tuberculosis |
| Sunny | 27 | Male | 170 cm | 75 kg | Karnataka | Parsi | No illness |
| Joan | 24 | Female | 165 cm | 71 kg | Kerala | Christian | Heart-related |
| Bahuksana | 23 | Male | 160 cm | 69 kg | Karnataka | Buddhist | Tuberculosis |
| Rambha | 19 | Male | 167 cm | 85 kg | Kerala | Hindu | Cancer |
| Kishor | 29 | Male | 180 cm | 81 kg | Karnataka | Hindu | Heart-related |
| Johnson | 17 | Male | 175 cm | 79 kg | Kerala | Christian | Heart-related |
| John | 19 | Male | 169 cm | 82 kg | Kerala | Christian | Viral infection |

There are 6 attributes and 10 records in this data. There are two common methods for achieving *k*-anonymity for some value of *k*:

1. **Suppression**. In this method, certain values of the attributes are replaced by an asterisk "*". All or some values of a column may be replaced by "*". In the anonymized table below, we have replaced all the values in the *Name* attribute and all the values in the *Religion* attribute with a "*".
2. **Generalization**. In this method, individual values of attributes are replaced with a broader category. For example, the value "19" of the attribute *Age* may be replaced by "≤ 20", the value "23" by "20 < Age ≤ 30", etc.

The next table shows the anonymized database.

| Name | Age | Gender | Height | Weight | State of domicile | Religion | Disease |
|---|---|---|---|---|---|---|---|
| * | 20 < Age ≤ 30 | Female | 165 cm | 72 kg | Tamil Nadu | * | Cancer |
| * | 20 < Age ≤ 30 | Female | 162 cm | 70 kg | Kerala | * | Viral infection |
| * | 20 < Age ≤ 30 | Female | 170 cm | 68 kg | Tamil Nadu | * | Tuberculosis |
| * | 20 < Age ≤ 30 | Male | 170 cm | 75 kg | Karnataka | * | No illness |
| * | 20 < Age ≤ 30 | Female | 165 cm | 71 kg | Kerala | * | Heart-related |
| * | 20 < Age ≤ 30 | Male | 160 cm | 69 kg | Karnataka | * | Tuberculosis |
| * | Age ≤ 20 | Male | 167 cm | 85 kg | Kerala | * | Cancer |
| * | 20 < Age ≤ 30 | Male | 180 cm | 81 kg | Karnataka | * | Heart-related |
| * | Age ≤ 20 | Male | 175 cm | 79 kg | Kerala | * | Heart-related |
| * | Age ≤ 20 | Male | 169 cm | 82 kg | Kerala | * | Viral infection |

This data has 2-anonymity with respect to the attributes *Age*, *Gender* and *State of domicile*, since for any combination of these attributes found in any row of the table there are always at least 2 rows with those exact attributes. The attributes available to an adversary are called quasi-identifiers. Each quasi-identifier tuple occurs in at least *k* records for a dataset with *k*-anonymity.

## Critiques of *k*-anonymity

The following example demonstrates a failing with *k*-anonymity: there may exist other data records that can be linked on the variables that are allegedly non-identifying. For instance, suppose an attacker is able to obtain the log from the person who was taking vital signs as part of the study and learns that Kishor was at the hospital on April 30 and is 180 cm tall. This information can be used to link with the "anonymized" database (which may have been published on the Internet) and learn that Kishor has a heart-related disease. An attacker who knows that Kishor visited the hospital on April 30 may be able to infer this simply knowing that Kishor is 180 cm height, roughly 80–82 kg, and comes from Karnataka.

The root of this problem is the core problem with *k*-anonymity: there is no way to mathematically, unambiguously determine whether an attribute is an identifier, a quasi-identifier, or a non-identifying sensitive value. In fact, all values are potentially identifying, depending on their prevalence in the population and on auxiliary data that the attacker may have. Other privacy mechanisms such as differential privacy do not share this problem.

Although k-anonymity safeguards against identity revelations, it does not shield against the disclosure of specific attributes. This becomes problematic when attackers possess background knowledge. Additionally, the absence of diversity in sensitive domains may result in the exposure of personal information. In such scenarios, opting for ℓ-Diversity might offer a more robust privacy safeguard.

Meyerson and Williams (2004) demonstrated that optimal *k*-anonymity is an NP-hard problem, however heuristic methods such as *k*-Optimize as given by Bayardo and Agrawal (2005) often yield effective results. A practical approximation algorithm that enables solving the *k*-anonymization problem with an approximation guarantee of $O(\log k)$ was presented by Kenig and Tassa.

## Attacks

While *k*-anonymity is a relatively simple-to-implement approach for de-identifying a dataset prior to public release, it is susceptible to many attacks. When background knowledge is available to an attacker, such attacks become even more effective. Such attacks include:

- *Homogeneity Attack*: This attack leverages the case where all the values for a sensitive value within a set of *k* records are identical. In such cases, even though the data has been *k*-anonymized, the sensitive value for the set of *k* records may be exactly predicted.
- *Background Knowledge Attack*: This attack leverages an association between one or more quasi-identifier attributes with the sensitive attribute to reduce the set of possible values for the sensitive attribute. For example, Machanavajjhala, Kifer, Gehrke, and Venkitasubramaniam (2007) showed that knowing that heart attacks occur at a reduced rate in Japanese patients could be used to narrow the range of values for a sensitive attribute of a patient's disease.
- *Downcoding Attack*: This attack, introduced in 2022 by Aloni Cohen, takes advantage of the way that anonymity algorithms aggregate attributes in separate records. Because the aggregation is deterministic, it is possible to reverse-engineer the original data image, and in many cases reveal the original data that was to be protected. This attack does not require background knowledge, but is strengthened by it.

Because *k*-anonymization does not include any randomization, attackers can make reliable, unambiguous inferences about data sets that may harm individuals. For example, if the 19-year-old John from Kerala is known to be in the database above, then it can be reliably said that he has either cancer, a heart-related disease, or a viral infection.

*K*-anonymization is not a good method to anonymize high-dimensional datasets.

It has also been shown that *k*-anonymity can skew the results of a data set if it disproportionately suppresses and generalizes data points with unrepresentative characteristics. The suppression and generalization algorithms used to *k*-anonymize datasets can be altered, however, so that they do not have such a skewing effect.
