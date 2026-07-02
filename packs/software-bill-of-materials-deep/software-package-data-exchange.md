---
title: "Software Package Data Exchange"
source: https://en.wikipedia.org/wiki/Software_Package_Data_Exchange
domain: software-bill-of-materials-deep
license: CC-BY-SA-4.0
tags: software bill of materials format, spdx component inventory, cyclonedx dependency manifest, transitive component disclosure
fetched: 2026-07-02
---

# Software Package Data Exchange

**System Package Data Exchange** (**SPDX**, formerly **Software Package Data Exchange**) is an open standard capable of representing systems with digital components as bills of materials (BOMs). First designed to describe software components, SPDX can describe the components of software systems, AI models, software builds, security data, and other data packages. SPDX allows the expression of components, licenses, copyrights, security references and other metadata relating to systems.

The original purpose of SPDX was to improve license compliance, and it has since been expanded to facilitate additional use cases such as supply-chain transparency and security. SPDX is authored by the community-driven SPDX Project involving key industry experts, organizations, and open-source enthusiasts under the auspices of the Linux Foundation.

The SPDX specification is recognized as the international open standard for security, license compliance, and other software supply chain artifacts as ISO/IEC 5962:2021. As of August 2025, the latest version of the standard has been 3.0.1.

## Structure

### Version 2.x

The SPDX 2.x standard defines an SBOM document, which contains SPDX metadata about software. The document itself can be expressed in multiple formats, including JSON, YAML, RDF/XML, tag–value, and spreadsheet. Each SPDX document describes one or more elements, which can be a software package, a specific file, or a snippet from a file. Each element is given a unique identifier, and metadata for an element can refer to other elements.

### Version 3.0

SPDX 3.0 allows users to communicate information at a much more granular level without having to package it as "envelope" data. A key design principle in SPDX 3.0 is that all elements may be expressed and referenced independent of any other element. This independence is required to support a variety of content exchange and analysis use cases and makes it easier to communicate single elements of interest. The relationship structure has also been updated to be both more expressive and easier to understand compared to older versions of the specification.

The SPDX 3.0 data model is based on the Resource Description Framework (RDF). Data may be serialized in a variety of formats for storage and transmission, including formats defined in RDF 1.1 such as JSON-LD, Turtle (Terse RDF Triple Language), N-Triples, and RDF/XML.

#### SPDX 3.0 profiles

The 3.0 specification introduced *profiles* to support the expansion of use cases beyond software, without increasing overall complexity. Profiles allow users to define data for the use cases they need, while also increasing the amount of information that can be gathered directly from the SPDX data. There are eight profiles defined by SPDX 3.0:

- **Core:** foundational concepts common to all profiles
- **Software**: concepts related to software artifacts
- **Security:** security-related metadata specific to a piece of software
- **Build:** information required to describe an instance of a software build
- **AI**: concepts and data elements related to an AI system and model
- **Dataset**: concepts related to a dataset, including preparation process, characteristics, and access methods
- **Licensing**: license information necessary for compliance with typical licensing use cases
- **Lite**: subset of the SPDX specification aimed at balancing SPDX standard and actual workflows in some industries

## Version history

| Version number | Publication date | Notes | References |
|---|---|---|---|
| 3.0.1 | December 2024 | Made changes to support SPDX 3 potentially becoming an OMG and ISO standard. Additionally includes various "fixes for spec issues" found in SPDX 3.0, including minor changes like typo fixes. |   |
| 3.0 | April 2024 | Introduced a comprehensive set of updates encompassing the model, specification, and license list, with the new addition of SPDX profiles to handle modern system use cases like security and AI. |   |
| 2.3 | November 2022 | Added new fields to improve the ability to capture security related information and interoperability with other SBOM formats. |   |
| 2.2.2 | April 2022 | Functionally equivalent to SPDX 2.2.1 but with spelling, grammar and other editorial improvements. |   |
| 2.2.1 | October 2020 | Functionally equivalent to SPDX 2.2 but with typesetting for publication as an ISO standard. |   |
| 2.2 | May 2020 | Added 'SPDX-lite' profile for minimal software bill of materials and improved support for external references. |   |
| 2.1 | November 2016 | Added support for describing 'snippets' of code and the ability to reference non-SPDX data (such as CVEs). |   |
| 2.0 | May 2015 | Added the ability to describe multiple packages and the relationships between different packages and files. |   |
| 1.2 | October 2013 | Improved interaction with the SPDX License List, and added new fields for documenting extra information about software projects. |   |
| 1.1 | August 2012 | Fixed a flaw in the SPDX Package Verification Code (a cryptographic hash function) and added support for free-form comments. |   |
| 1.0 | August 2011 | The first release of the SPDX specification; handles packages. |   |

The first version of the SPDX specification was intended to make compliance with software licenses easier, but subsequent versions of the specification added capabilities intended for other use-cases, such as being able to contain references to known software vulnerabilities. Recent versions of SPDX fulfill the NTIA's 'Minimum Elements For a Software Bill of Materials'.

SPDX 2.2.1 was submitted to the International Organization for Standardization (ISO) in October, 2020, and was published as *ISO/IEC 5962:2021 Information technology — SPDX® Specification V2.2.1* in August, 2021.

## SPDX-License-Identifier

### Syntax

Each license is identified by a full name, such as "Mozilla Public License 2.0" and a short identifier, here "MPL-2.0". Licenses can be combined by operators `AND` and `OR`, and grouping `(`, `)`.

For example, `(Apache-2.0 OR MIT)` means that one can choose between `Apache-2.0` (Apache License) or `MIT` (MIT license). On the other hand, `(Apache-2.0 AND MIT)` means that both licenses apply.

There is also a "+" operator which, when applied to a license, means that future versions of the license apply as well. For example, `Apache-1.1+` means that `Apache-1.1` and `Apache-2.0` may apply (and future versions if any).

SPDX describes the exact terms under which a piece of software is licensed. It does not attempt to categorize licenses by type, for instance by describing licenses with similar terms to the BSD License as "BSD-like".

In 2020, the European Commission published its Joinup Licensing Assistant, which makes possible the selection and comparison of more than 50 licenses, with access to their SPDX identifier and full text.

### Deprecated license identifiers

The GNU family of licenses (e.g., GNU General Public License version 2) have the choice of choosing a later version of the license built in. Sometimes, it was not clear whether the SPDX expression `GPL-2.0` meant "exactly GPL version 2.0" or "GPL version 2.0 or any later version". Thus, since version 3.0 of the SPDX License List, the GNU family of licenses got new names. `GPL-2.0-only` means "exactly version 2.0" and `GPL-2.0-or-later` means "version 2.0 or any later version".

## Adoption

### For licensing

The SPDX license identifier can be added to the top of source code files as a short string unambiguously declaring the license used. The `SPDX-License-Identifier` syntax, pioneered by Das U-Boot in 2013, became part of SPDX in version 2.1. In 2017, the FSFE launched REUSE, which provides tools to validate the comment and to efficiently extract copyright information.

The SPDX license identifier is also used in a number of package managers such as npm, Python, and Rust cargo. SPDX license expressions are used in RPM package metadata in Fedora Linux, replacing the earlier use of the Callaway system. Debian uses a slightly different license specification.
