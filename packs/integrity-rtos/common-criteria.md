---
title: "Common Criteria"
source: https://en.wikipedia.org/wiki/Common_Criteria
domain: integrity-rtos
license: CC-BY-SA-4.0
tags: integrity rtos, green hills integrity, separation kernel, common criteria eal
fetched: 2026-07-02
---

# Common Criteria

The **Common Criteria for Information Technology Security Evaluation**, or simply **Common Criteria** (**CC**), is an information security standard. It is adopted in **ISO/IEC 15408:2022**.

Common Criteria is a framework in which computer system users can *specify* their security *functional* and *assurance* requirements (SFRs and SARs, respectively) in a Security Target (ST), and may be taken from Protection Profiles (PPs). Vendors can then *implement* or make claims about the security attributes of their products, and testing laboratories can *evaluate* the products to determine if they actually meet the claims. In other words, Common Criteria provides assurance that the process of specification, implementation and evaluation of a computer security product has been conducted in a rigorous and standard and repeatable manner at a level that is commensurate with the target environment for use. Common Criteria maintains a list of certified products, including operating systems, access control systems, databases, and key management systems.

## Characteristics

Common Criteria evaluations are performed on computer security products and systems.

**Target of Evaluation (TOE)**

the product or system that is the subject of the evaluation. The evaluation serves to validate claims made about the target.

**Protection Profile (PP)**

a document, typically created by a user or user community, which identifies security requirements for a class of security devices (for example,

smart cards

used to provide

digital signatures

, or network

firewalls

) relevant to that user for a particular purpose. Product vendors can choose to implement products that comply with one or more PPs, and have their products evaluated against those PPs. In such a case, a PP may serve as a template for the product's ST (Security Target, as defined below), or the authors of the ST will at least ensure that all requirements in relevant PPs also appear in the target's ST document. Customers looking for particular types of products can focus on those certified against the PP that meets their requirements.

**Security Target (ST)**

the document that identifies the security

properties

of the target of evaluation. The ST may claim conformance with one or more PPs. The TOE is evaluated against the SFRs (Security Functional Requirements. Again, see below) established in its ST, no more and no less. This allows vendors to tailor the evaluation to accurately match the intended capabilities of their product. This means that a network firewall does not have to meet the same functional requirements as a

database

management system, and that different firewalls may in fact be evaluated against completely different lists of requirements. The ST is usually published so that potential customers may determine the specific security features that have been certified by the evaluation.

**Security Functional Requirements (SFRs)**

specify individual security

functions

which may be provided by a product. The Common Criteria presents a standard catalogue of such functions. For example, a SFR may state

how

a user acting a particular

role

might be

authenticated

. The list of SFRs can vary from one evaluation to the next, even if two targets are the same type of product. Although Common Criteria does not prescribe any SFRs to be included in an ST, it identifies dependencies where the correct operation of one function (such as the ability to limit access according to roles) is dependent on another (such as the ability to identify individual roles).

**Security Assurance Requirements (SARs)**

descriptions of the measures taken during development and evaluation of the product to assure compliance with the claimed security functionality. For example, an evaluation may require that all source code is kept in a change management system, or that full functional testing is performed. The Common Criteria provides a catalogue of these, and the requirements may vary from one evaluation to the next. The requirements for particular targets or types of products are documented in the ST and PP, respectively.

**Evaluation Assurance Level (EAL)**

the numerical rating describing the depth and rigor of an evaluation. Each EAL corresponds to a package of security assurance requirements (SARs, see above) which covers the complete development of a product, with a given level of strictness. Common Criteria lists seven levels, with EAL 1 being the most basic (and therefore cheapest to implement and evaluate) and EAL 7 being the most stringent (and most expensive). Normally, an ST or PP author will not select assurance requirements individually but choose one of these packages, possibly 'augmenting' requirements in a few areas with requirements from a higher level. Higher EALs

do not

necessarily imply "better security", they only mean that the claimed security assurance of the TOE has been more extensively

verified

.

So far, most PPs and most evaluated STs/certified products have been for IT components (e.g., firewalls, operating systems, smart cards).

Common Criteria certification is sometimes specified for IT procurement. Other standards containing, e.g., interoperation, system management, user training, supplement CC and other product standards. Examples include the ISO/IEC 27002 and the German IT baseline protection.

Details of cryptographic implementation within the TOE are outside the scope of the CC. Instead, national standards, like FIPS 140-2, give the specifications for cryptographic modules, and various standards specify the cryptographic algorithms in use.

More recently, PP authors are including cryptographic requirements for CC evaluations that would typically be covered by FIPS 140-2 evaluations, broadening the bounds of the CC through scheme-specific interpretations.

Some national evaluation schemes are phasing out EAL-based evaluations and only accept products for evaluation that claim strict conformance with an approved PP. The United States currently only allows PP-based evaluations.

## History

CC originated out of three standards:

- ITSEC – The European standard, developed in the early 1990s by France, Germany, the Netherlands and the UK. It too was a unification of earlier work, such as the two UK approaches (the CESG UK Evaluation Scheme aimed at the defence/intelligence market and the DTI Green Book aimed at commercial use), and was adopted by some other countries, e.g. Australia.
- CTCPEC – The Canadian standard followed from the US DoD standard, but avoided several problems and was used jointly by evaluators from both the U.S. and Canada. The CTCPEC standard was first published in May 1993.
- TCSEC – The United States Department of Defense DoD 5200.28 Std, called the Orange Book and parts of the Rainbow Series. The Orange Book originated from Computer Security work including the Anderson Report, done by the National Security Agency and the National Bureau of Standards (the NBS eventually became NIST) in the late 1970s and early 1980s. The central thesis of the Orange Book follows from the work done by Dave Bell and Len LaPadula for a set of protection mechanisms.

CC was produced by unifying these pre-existing standards, predominantly so that companies selling computer products for the government market (mainly for Defence or Intelligence use) would only need to have them evaluated against one set of standards. The CC was developed by the governments of Canada, France, Germany, the Netherlands, the UK, and the U.S.

## Testing organizations

All testing laboratories must comply with ISO/IEC 17025, and certification bodies will normally be approved against ISO/IEC 17065.

The compliance with ISO/IEC 17025 is typically demonstrated to a National approval authority:

- In Canada, the Standards Council of Canada (SCC) under Program for the Accreditation of Laboratories (PALCAN) accredits Common Criteria Evaluation Facilities (CCEF)
- In France, the Comité français d'accréditation (COFRAC) accredits Common Criteria evaluation facilities, commonly called Centre d'évaluation de la sécurité des technologies de l'information (CESTI). Evaluations are done according to norms and standards specified by the Agence nationale de la sécurité des systèmes d'information (ANSSI).
- In Italy, the OCSI (Organismo di Certificazione della Sicurezza Informatica) accredits Common Criteria evaluation laboratories
- In India, the STQC Directorate of the Ministry of Electronics and Information Technology evaluates and certifies IT products at assurance levels EAL 1 through EAL 4.
- In the UK the United Kingdom Accreditation Service (UKAS) used to accredit Commercial Evaluation Facilities (CLEF) Archived 2015-10-28 at the Wayback Machine; the UK is since 2019 only a consumer in the CC ecosystem
- In the US, the National Institute of Standards and Technology (NIST) National Voluntary Laboratory Accreditation Program (NVLAP) accredits Common Criteria Testing Laboratories (CCTL)
- In Germany, the Bundesamt für Sicherheit in der Informationstechnik (BSI)
- In Spain, the National Cryptologic Center (CCN) accredits Common Criteria Testing Laboratories operating in the Spanish Scheme.
- In The Netherlands, the Netherlands scheme for Certification in the Area of IT Security (NSCIB) accredits IT Security Evaluation Facilities (ITSEF).
- In Sweden, the Swedish Certification Body for IT Security (CSEC) licenses IT Security Evaluation Facilities (ITSEF).

Characteristics of these organizations were examined and presented at ICCC 10.

## Mutual recognition arrangement

As well as the Common Criteria standard, there is also a sub-treaty level Common Criteria MRA (Mutual Recognition Arrangement), whereby each party thereto recognizes evaluations against the Common Criteria standard done by other parties. Originally signed in 1998 by Canada, France, Germany, the United Kingdom and the United States, Australia and New Zealand joined 1999, followed by Finland, Greece, Israel, Italy, the Netherlands, Norway and Spain in 2000. The Arrangement has since been renamed **Common Criteria Recognition Arrangement** (**CCRA**) and membership continues to expand. Within the CCRA only evaluations up to EAL 2 are mutually recognized (Including augmentation with flaw remediation). The European countries within the SOGIS-MRA typically recognize higher EALs as well. Evaluations at EAL5 and above tend to involve the security requirements of the host nation's government.

In September 2012, a majority of members of the CCRA produced a vision statement whereby mutual recognition of CC evaluated products will be lowered to EAL 2 (Including augmentation with flaw remediation). Further, this vision indicates a move away from assurance levels altogether and evaluations will be confined to conformance with Protection Profiles that have no stated assurance level. This will be achieved through technical working groups developing worldwide PPs, and as yet a transition period has not been fully determined.

On July 2, 2014, a new CCRA was ratified per the goals outlined within the 2012 vision statement. Major changes to the Arrangement include:

- Recognition of evaluations against only a collaborative Protection Profile (cPP) or Evaluation Assurance Levels 1 through 2 and ALC_FLR.
- The emergence of international Technical Communities (iTC), groups of technical experts charged with the creation of cPPs.
- A transition plan from the previous CCRA, including recognition of certificates issued under the previous version of the Arrangement.

## Issues

### Requirements

Common Criteria is very generic; it does not directly provide a list of product security requirements or features for specific (classes of) products: this follows the approach taken by ITSEC, but has been a source of debate to those used to the more prescriptive approach of other earlier standards such as TCSEC and FIPS 140-2.

### Value of certification

Common Criteria certification cannot guarantee security, but it can ensure that claims about the security attributes of the evaluated product were independently verified. In other words, products evaluated against a Common Criteria standard exhibit a clear chain of evidence that the process of specification, implementation, and evaluation has been conducted in a rigorous and standard manner.

Various Microsoft Windows versions, including Windows Server 2003 and Windows XP, have been certified, but security patches to address security vulnerabilities are still getting published by Microsoft for these Windows systems. This is possible because the process of obtaining a Common Criteria certification allows a vendor to restrict the analysis to certain security features and to make certain assumptions about the operating environment and the strength of threats faced by the product in that environment. Additionally, the CC recognizes a need to limit the scope of evaluation in order to provide cost-effective and useful security certifications, such that evaluated products are examined to a level of detail specified by the assurance level or PP. Evaluations activities are therefore only performed to a certain depth, use of time, and resources and offer reasonable assurance for the intended environment.

In the Microsoft case, the assumptions include A.PEER:

> "Any other systems with which the TOE communicates are assumed to be under the same management control and operate under the same security policy constraints. The TOE is applicable to networked or distributed environments only if the entire network operates under the same constraints and resides within a single management domain. There are no security requirements that address the need to trust external systems or the communications links to such systems."

This assumption is contained in the Controlled Access Protection Profile (CAPP) to which their products adhere. Based on this and other assumptions, which may not be realistic for the common use of general-purpose operating systems, the claimed security functions of the Windows products are evaluated. Thus they should only be considered secure in the assumed, specified circumstances, also known as the *evaluated configuration*.

Whether you run Microsoft Windows in the precise evaluated configuration or not, you should apply Microsoft's security patches for the vulnerabilities in Windows as they continue to appear. If any of these security vulnerabilities are exploitable in the product's evaluated configuration, the product's Common Criteria certification should be voluntarily withdrawn by the vendor. Alternatively, the vendor should re-evaluate the product to include the application of patches to fix the security vulnerabilities within the evaluated configuration. Failure by the vendor to take either of these steps would result in involuntary withdrawal of the product's certification by the certification body of the country in which the product was evaluated.

The certified Microsoft Windows versions remain at EAL4+ without including the application of any Microsoft security vulnerability patches in their evaluated configuration. This shows both the limitation and strength of an evaluated configuration.

### Criticisms

In August 2007, *Government Computing News* (GCN) columnist William Jackson critically examined Common Criteria methodology and its US implementation by the Common Criteria Evaluation and Validation Scheme (CCEVS). In the column executives from the security industry, researchers, and representatives from the National Information Assurance Partnership (NIAP) were interviewed. Objections outlined in the article include:

- Evaluation is a costly process (often measured in hundreds of thousands of US dollars) – and the vendor's return on that investment is not necessarily a more secure product.
- Evaluation focuses primarily on assessing the evaluation documentation, not on the actual security, technical correctness or merits of the product itself. For U.S. evaluations, only at EAL5 and higher do experts from the National Security Agency participate in the analysis; and only at EAL7 is full source code analysis required.
- The effort and time necessary to prepare evaluation evidence and other evaluation-related documentation is so cumbersome that by the time the work is completed, the product in evaluation is generally obsolete.
- Industry input, including that from organizations such as the Common Criteria Vendor's Forum, generally has little impact on the process as a whole.

In a 2006 research paper, computer specialist David A. Wheeler suggested that the Common Criteria process discriminates against free and open-source software (FOSS)-centric organizations and development models. Common Criteria assurance requirements tend to be inspired by the traditional waterfall software development methodology. In contrast, much FOSS software is produced using modern agile paradigms. Although some have argued that both paradigms do not align well, others have attempted to reconcile both paradigms. Political scientist Jan Kallberg raised concerns over the lack of control over the actual production of the products once they are certified, the absence of a permanently staffed organizational body that monitors compliance, and the idea that the trust in the Common Criteria IT-security certifications will be maintained across geopolitical boundaries.

In 2017, the ROCA vulnerability was found in a list of Common Criteria certified smart card products. The vulnerability highlighted several shortcomings of Common Criteria certification scheme:

- The vulnerability resided in a homegrown RSA key generation algorithm that has not been published and analyzed by the cryptanalysis community. However, the testing laboratory TÜV Informationstechnik GmbH (TÜViT) in Germany approved its use and the certification body BSI in Germany issued Common Criteria certificates for the vulnerable products. The Security Target of the evaluated product claimed that RSA keys are generated according to the standard algorithm. In response to this vulnerability, BSI now plans to improve transparency by requiring that the certification report at least specifies if the implemented proprietary cryptography is not exactly conformant to a recommended standard. BSI does not plan on requiring the proprietary algorithm to be published in any way.
- Even though the certification bodies are now aware that the security claims specified in the Common Criteria certificates do not hold anymore, neither ANSSI nor BSI have revoked the corresponding certificates. According to BSI, a certificate can only be withdrawn when it was issued under misconception, e.g., when it turns out that wrong evidence was submitted. After a certificate is issued, it must be presumed that the validity of the certificate decreases over time by improved and new attacks being discovered. Certification bodies can issue maintenance reports and even perform a re-certification of the product. These activities, however, have to be initiated and sponsored by the vendor.
- While several Common Criteria certified products have been affected by the ROCA flaw, vendors' responses in the context of certification have been different. For some products a maintenance report was issued, which states that only RSA keys with a length of 3072 and 3584 bits have a security level of at least 100 bits, while for some products the maintenance report does not mention that the change to the TOE affects certified cryptographic security functionality, but concludes that the change is at the level of guidance documentation and has no effect on assurance.
- According to BSI, the users of the certified end products should have been informed of the ROCA vulnerability by the vendors. This information, however, did not reach in a timely manner the Estonian authorities who had deployed the vulnerable product on more than 750,000 Estonian identity cards.

## Alternative approaches

Throughout the lifetime of CC, it has not been universally adopted even by the creator nations, with, in particular, cryptographic approvals being handled separately, such as by the Canadian / US implementation of FIPS-140, and the CESG Assisted Products Scheme (CAPS) in the UK.

The UK has also produced a number of alternative schemes when the timescales, costs and overheads of mutual recognition have been found to be impeding the operation of the market:

- The CESG System Evaluation (SYSn) and Fast Track Approach (FTA) schemes for assurance of government systems rather than generic products and services, which have now been merged into the CESG Tailored Assurance Service (CTAS)
- The CESG Claims Tested Mark (CCT Mark), which is aimed at handling less exhaustive assurance requirements for products and services in a cost and time efficient manner.

In early 2011, NSA/CSS published a paper by Chris Salter, which proposed a Protection Profile oriented approach towards evaluation. In this approach, communities of interest form around technology types which in turn develop protection profiles that define the evaluation methodology for the technology type. The objective is a more robust evaluation. There is some concern that this may have a negative impact on mutual recognition.

In Sept of 2012, the Common Criteria published a Vision Statement implementing to a large extent Chris Salter's thoughts from the previous year. Key elements of the Vision included:

- Technical Communities will be focused on authoring Protection Profiles (PP) that support their goal of reasonable, comparable, reproducible and cost-effective evaluation results
- Evaluations should be done against these PP's if possible; if not mutual recognition of Security Target evaluations would be limited to EAL2.
