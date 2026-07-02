---
title: "Statistical disclosure control"
source: https://en.wikipedia.org/wiki/Statistical_disclosure_control
domain: differential-privacy-applied
license: CC-BY-SA-4.0
tags: differential privacy, local differential privacy, privacy budget epsilon, randomized response, statistical disclosure control
fetched: 2026-07-02
---

# Statistical disclosure control

**Statistical disclosure control** (**SDC**), also known as **statistical disclosure limitation** (**SDL**) or **disclosure avoidance**, is a technique used in data-driven research to ensure no person or organization is identifiable from the results of an analysis of survey or administrative data, or in the release of microdata. The purpose of SDC is to protect the confidentiality of the respondents and subjects of the research.

SDC usually refers to 'output SDC'; ensuring that, for example, a published table or graph does not disclose confidential information about respondents. SDC can also describe protection methods applied to the data: for example, removing names and addresses, limiting extreme values, or swapping problematic observations. This is sometimes referred to as 'input SDC', but is more commonly called anonymization, de-identification, or microdata protection.

Textbooks (e.g. *Statistical Disclosure Control*) typically cover input SDC and tabular data protection (but not other parts of output SDC). This is because these two problems are of direct interest to statistical agencies who supported the development of the field. For analytical environments, output rules developed for statistical agencies were generally used until data managers began arguing for specific output SDC for research.

This page focuses on output SDC.

## Necessity

Many kinds of social, economic and health research use potentially sensitive data as a basis for their research, such as survey or Census data, tax records, health records, educational information, etc. Such information is usually given in confidence, and, in the case of administrative data, not always for the purpose of research.

Researchers are not usually interested in information about one single person or business; they are looking for trends among larger groups of people. However, the data they use is, in the first place, linked to individual people and businesses, and SDC ensures that these cannot be identified from published data, no matter how detailed or broad.

It is possible that at the end of data analysis, the researcher somehow singles out one person or business through their research. For example, a researcher may identify the exceptionally good or bad service in a geriatric department within a hospital in a remote area, where only one hospital provides such care. In that case, the data analysis 'discloses' the identity of the hospital, even if the dataset used for analysis was properly anonymised or de-identified.

Statistical disclosure control will identify this disclosure risk and ensure the results of the analysis are altered to protect confidentiality. It requires a balance between protecting confidentiality and ensuring the results of the data analysis are still useful for statistical research.

## Output SDC: statistical models

Output SDC relies upon having a set of rules that can be followed by an output checker; for example, that a frequency table must have a minimum number of observations, or that survival tables should be right-censored for extreme values. The value and drawbacks of rules for frequency and magnitude tables have been discussed extensively since the late 20th Century. However, with awareness of the increasing need for rules for other types of analyses, a more structured approach is needed.

### 'Safe' and 'unsafe' statistics

Some statistical outputs, such as frequency tables, have a high level of inherent risk: differencing, low numbers, class disclosure. They therefore need to be checked before release, ideally by someone with some understanding of the data, to ensure that there is no meaningful risk on release. These are referred to as 'unsafe statistics'. However, there are some statistics, such as the coefficients from modelling, that have no meaningful risk and therefore can be released with no further checks. These are called 'safe statistics'. By separating statistics into 'safe' and 'unsafe', output checks can be concentrated on the latter, improving both security and efficiency.

This is less important for official statistics, where 'unsafe' statistics such as counts, means, medians and simple indexes dominate the outputs. However, for research output this is important, as a great deal of research output (particularly estimates and test statistics) is inherently 'safe'.

### Statistical barns or statbarns

The safe/unsafe model is useful but limited with two simple categories; within those categories, guidelines for SDC largely consist of long lists of statistics and how to handle them. In 2023, the SACRO project https://dareuk.org.uk/driver-project-sacro/ undertook to review the whole field and see whether a more useful classification scheme could be introduced. The result is the 'statistical barn' (or 'statbarn') concept.

A statbarn is a classification of statistics for disclosure control purposes, where all of the statistics in that class share the same characteristics as far as disclosure control is concerned:

- their mathematical form is similar
- they share the same risks
- they share the same responses to those risks
- output checking rules are applicable to all

As of March 2024, 14 statbarns have been identified, with 12 described for output checkers:

- frequencies
- statistical hypothesis tests
- coefficients of association
- position (median, IQR etc.)
- extreme values (max, min)
- shape
- linear aggregates
- mode
- non-linear concentration ratios
- odds and risk ratios
- survival tables
- Gini coefficients

These cover almost all statistics. They also cover most graph forms, where the graph can be converted into the appropriate statsbarn (for example, a pie chart is another form of frequency table). The SACRO manual provides guidance on what to look out for, and the rules to be followed for checking. A lookup table between statstistcs/graphs and statbarns is available on outputchecking.org.

## Output SDC: operating models

There are two main approaches to output SDC: *principles-based* and *rules-based.* In principles-based systems, disclosure control attempts to uphold a specific set of fundamental principles—for example, "no person should be identifiable in released microdata". Rules-based systems, in contrast, are evidenced by a specific set of rules that a person performing disclosure control follows (for example, "any frequency must be based on at least five observations"), after which the data are presumed to be safe to release. In general, official statistics are rules-based; research environments are more likely to be principles-based.

In research environments, the choice of output-checking regime can have significant operational implications.

### Rules-Based SDC

In rules-based SDC, a rigid set of rules is used to determine whether or not the results of data analysis can be released. The rules are applied consistently, which makes it obvious what kinds of output are acceptable. Rules-based systems are good for ensuring consistency across time, across data sources, and across production teams, which makes them appealing for statistical agencies. Rules-based systems also work well for remote job serves such as microdata.no or Lissy.

However, because the rules are inflexible, either disclosive information may still slip through, or the rules are over-restrictive and may only allow for results that are too broad for useful analysis to be published. In practice, research environments running rules-based systems may have to bring flexibility in 'ad hoc' systems.

The Northern Ireland Statistics and Research Agency (NISRA) uses a rules-based approach to releasing statistics and research results.

### Principles-Based SDC

In principles-based SDC, both the researcher and the output checker are trained in SDC. They receive a set of rules, which are rules-of-thumb rather than hard rules as in rules-based SDC. This means that in principle, any output may be approved or refused. The rules-of-thumb are a starting point for the researcher. A researcher may request outputs which breach the 'rules of thumb' as long as (1) they are non-disclosive (2) they are important and (3) this is an exceptional request. It is up to the researcher to prove that any 'unsafe' outputs are non-disclosive, but the checker has the final say. Since there are no hard rules, this requires knowledge on disclosure risks and judgment from both the researcher and the checker. It requires training and an understanding of statistics and data analysis, although it has been argued that this can be used to make the process more efficient than a rules-based model.

In the UK all major secure research environments in social science and public health, with the exception of Northern Ireland, are principles-based. This includes the UK Data Service's Secure Data Service, the Office for National Statistics' Secure Research Service, the Scottish Safe Havens, Secure Anonymized Information Linkage (SAIL) and OpenSAFELY.

## Critiques

Many contemporary statistical disclosure control techniques, such as generalization and cell suppression, have been shown to be vulnerable to attack by a hypothetical data intruder. For example, Cox showed in 2009 that Complementary cell suppression typically leads to "over-protected" solutions because of the need to suppress both primary and complementary cells, and even then can lead to the compromise of sensitive data when exact intervals are reported.

Many of the rules are arbitrary and reflect data owner's unwillingness to be different, rather than solid evidence. For example, Ritchie demonstrated the choice of a minimum threshold is more about an organisation's wish to be in line with others than any statistical rationale.

A more substantive criticism is that the theoretical models used to explore control measures are not appropriate for guides for practical action. Hafner et al. provide a practical example of how a change in perspective can generate substantially different results.

## Output SDC and AI models

Artificial intelligence and machine learning models present different risks for output checking. The GRAIMATTER project https://dareuk.org.uk/sprint-exemplar-project-graimatter/ provided some initial guidance and automatic tools. These were extended and simplified as part of the SACRO project (see below), and more guidelines for data services staff added. This is still a quickly-evolving area. The SDC-REBOOT community network https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=SDC-REBOOT is currently co-ordinating the ongoing development of the tools and guidance.

## Automated tools

Output checking is generally labour-intensive, as it requires analysts who can understand what they are looking at and make a judgement about whether to release an output. There is therefore considerable interest in automated checking. A Eurostat-commissioned report explored the options for output checking, which largely come down to two options:

- end-of-process review (EoPR): training a computer to look at the output and understand what it shows. This has the advantage of requiring no additional training for the researcher. However, it can be difficult to explain to any automated system what it is looking at; this can be more time-consuming than checking the output manually. tauArgus and sdcTable are EoPR.
- within-process review (WPR): the output checking tool is called at the same time the output is being generated, and has access to the source data; therefore, there is no need to explain how the output has been created. The disadvantage of this approach is that it can slow down processing times, and requires the analysis to include the necessary commands to run the output checking tool. However, the major advantage is that it does not need to be taught about the data,

### tauArgus and sdcTable

tau-Argus and sdcTable are fully-automated open-source EoPR tools for tabular data protection (frequency and magnitude tables). They are designed to work with multiple tables. Metadata needs to be set up describing the output(s), and the control parameters. They provide the output checkers with extensive information on potential problems, including secondary disclosure across tables. They can also carry out correction measures, from suppression and simple rounding to secondary suppression and controlled tabular rounding. They do not deal with non-tabular outputs.

Because of the need to rewrite the metadata for each table, these tools are poorly suited for research use. However, in official statistics, where the same tables are being repeatedly generated and where secondary differencing is considered a significant problem, the investment in setting up the tools can be very cost-effective.

The software for both is open source at GitHub https://github.com/sdcTools/tauargus and CRAN https://cran.r-project.org/web/packages/sdcTable/

### SACRO

SACRO (Semi-autonomous checking of research outputs) is a WPR tool, originally commissioned (ACRO) by Eurostat in 2020 as a proof-of-concept to show that a general-purpose output checking tool could be developed. In 2023 the UK Medical Research Council commissioned a generalised version (SACRO) which would work with multiple languages (as of 2024: Stata, R and Python) and provide a more user-friendly interface. SACRO directly implements the statbarns model and is principles-based; hence, it is 'semi-automatic' as it allows users to request exceptions and for output checkers to override the automated recommendations. All UK social science secure facilities, and most UK public health secure facilities, are planning to adopt it.

The software is available on GitHub at https://github.com/AI-SDC, which also contains links to the original ACRO and tools for assessing AI models.
