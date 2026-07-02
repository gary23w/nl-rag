---
title: "Software supply chain"
source: https://en.wikipedia.org/wiki/Software_bill_of_materials
domain: software-composition-analysis
license: CC-BY-SA-4.0
tags: software composition analysis, open source dependency scanning, known vulnerability detection, transitive dependency audit
fetched: 2026-07-02
---

# Software supply chain

(Redirected from

Software bill of materials

)

A **software supply chain** is the components, libraries, tools, and processes used to develop, build, and publish a software artifact.

A **software bill of materials** (**SBOM**) declares the inventory of components used to build a software artifact, including any open source and proprietary software components. It is the software analogue to the traditional manufacturing BOM, which is used as part of supply chain management. SBOMs are a strategy for improving transparency in the software supply chain.

Software supply chain attacks compromise an upstream component — such as a widely-used library, a build tool, or a distribution channel — in order to simultaneously affect all downstream users of that component. High-profile incidents such as the SolarWinds attack illustrated the scale and reach of such attacks. Researchers have catalogued the attack surface into a taxonomy covering all stages from source-code contribution to package distribution, linking attack vectors to real-world incidents and corresponding safeguards.

## Software provenance

Another important concept in software supply chains is provenance: signed attestations can record where a software artifact came from, which source and dependencies were used, and which steps in the build pipeline produced it. Provenance frameworks such as in-toto help downstream users verify that a release was built by an expected process and help detect tampering between source retrieval, build, and distribution.

## Software Bill of Materials

An SBOM allows builders to make sure open-source and third-party software components are up to date and respond quickly to new vulnerabilities. Buyers and other stakeholders can use an SBOM to perform vulnerability or license analysis, which can be used to evaluate and manage risk in a product.

While many companies use a spreadsheet for general BOM management, there are additional risks and issues in an SBOM written to a spreadsheet, such as the inability to automatically enrich it with vulnerability data or integrate it into security toolchains. It is best practice for SBOMs to be collectively stored in a repository that can be part of other automation systems and easily queried by other applications.

Cybersecurity transparency studies, including TRACS 2025, identify the availability of SBOMs as one of the criteria used when purchasing information security solutions. However, not all enterprise security products provide publicly available SBOMs. Research on open-source ecosystems indicates that policy-driven SBOMs remain rare in practice: one large-scale study found that only about 0.56% of popular GitHub repositories contain SBOMs created in accordance with formal security or compliance policies. Also, according to other research, fewer than half of tested software projects include SBOMs in their releases, and many of those SBOMs are incomplete or do not fully conform to established standards. At the same time, corporate-level surveys report that approximately 60–76 % of enterprises require SBOMs from suppliers or have integrated SBOMs into procurement and supply-chain risk management processes.

## Legislation

The **Cyber Supply Chain Management and Transparency Act of 2014** was a failed piece of US legislation (bill) that proposed to require government agencies to obtain SBOMs for any new products they purchase and to obtain SBOMs for "any software, firmware, or product in use by the United States Government". The act spurred later legislation such as "Internet of Things Cybersecurity Improvement Act of 2017."

US President Joe Biden’s **Executive Order 14028 on Improving the Nation’s Cybersecurity** of May 12, 2021 ordered NIST and NTIA to lay down guidelines for software supply chain management, including for SBOMs. The NTIA outlines three broad categories of minimum elements of SBOMs: data fields (baseline information about each software component), automation support (the ability to generate SBOMs in machine- and human-readable formats), and practices and processes (how and when organizations should generate SBOMs). The "automation support" requirement specifies the need for "automatic generation," which is possible with the use of Software Composition Analysis (SCA) solutions.
