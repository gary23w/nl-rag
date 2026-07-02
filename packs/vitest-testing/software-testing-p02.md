---
title: "Software testing (part 2/2)"
source: https://en.wikipedia.org/wiki/Software_testing
domain: vitest-testing
license: CC-BY-SA-4.0
tags: vitest testing, vite-native test runner, unit test framework, javascript test assertions
fetched: 2026-07-02
part: 2/2
---

## Quality

### Software verification and validation

Software testing is used in association with verification and validation:

- Verification: Have we built the software right? (i.e., does it implement the requirements).
- Validation: Have we built the right software? (i.e., do the deliverables satisfy the customer).

The terms verification and validation are commonly used interchangeably in the industry; it is also common to see these two terms defined with contradictory definitions. According to the *IEEE Standard Glossary of Software Engineering Terminology*:

Verification is the process of evaluating a system or component to determine whether the products of a given development phase satisfy the conditions imposed at the start of that phase.

Validation is the process of evaluating a system or component during or at the end of the development process to determine whether it satisfies specified requirements.

And, according to the ISO 9000 standard:

Verification is confirmation by examination and through provision of objective evidence that specified requirements have been fulfilled.

Validation is confirmation by examination and through provision of objective evidence that the requirements for a specific intended use or application have been fulfilled.

The contradiction is caused by the use of the concepts of requirements and specified requirements but with different meanings.

In the case of IEEE standards, the specified requirements, mentioned in the definition of validation, are the set of problems, needs and wants of the stakeholders that the software must solve and satisfy. Such requirements are documented in a Software Requirements Specification (SRS). And, the products mentioned in the definition of verification, are the output artifacts of every phase of the software development process. These products are, in fact, specifications such as Architectural Design Specification, Detailed Design Specification, etc. The SRS is also a specification, but it cannot be verified (at least not in the sense used here – more on this subject below).

But, for the ISO 9000, the specified requirements are the set of specifications, as just mentioned above, that must be verified. A specification, as previously explained, is the product of a software development process phase that receives another specification as input. A specification is verified successfully when it correctly implements its input specification. All the specifications can be verified except the SRS because it is the first one (it can be validated, though). An example scenario be that the Design Specification must implement the SRS, and the Construction phase artifacts must implement the Design Specification.

So, when these words are defined in common terms, the apparent contradiction disappears.

Both the SRS and the software must be validated. The SRS can be validated statically by consulting with the stakeholders. Nevertheless, running some partial implementation of the software or a prototype of any kind (dynamic testing) and obtaining positive feedback from them, can further increase the certainty that the SRS is correctly formulated. On the other hand, the software, as a final and running product (not its artifacts and documents, including the source code) must be validated dynamically with the stakeholders by executing the software and having them to try it.

Some might argue that, for SRS, the input is the words of stakeholders and, therefore, SRS validation is the same as SRS verification. Thinking this way is not advisable as it only causes more confusion. It is better to think of verification as a process involving a formal and technical input document.

### Software quality assurance

In some organizations, software testing is part of a software quality assurance (SQA) process. In SQA, software process specialists and auditors are concerned with the software development process rather than just the artifacts such as documentation, code and systems. They examine and change the software engineering process itself to reduce the number of faults that end up in the delivered software: the so-called defect rate. What constitutes an acceptable defect rate depends on the nature of the software; a flight simulator video game would have much higher defect tolerance than software for an actual airplane. Although there are close links with SQA, testing departments often exist independently, and there may be no SQA function in some companies.

Software testing is an activity to investigate software under test in order to provide quality-related information to stakeholders. By contrast, QA (quality assurance) is the implementation of policies and procedures intended to prevent defects from reaching customers.

### Measures

Quality measures include such topics as correctness, completeness, security and ISO/IEC 9126 requirements such as capability, reliability, efficiency, portability, maintainability, compatibility, and usability.

There are a number of frequently used software metrics, or measures, which are used to assist in determining the state of the software or the adequacy of the testing.

### Artifacts

A software testing process can produce several artifacts. The actual artifacts produced are a factor of the software development model used, stakeholder and organisational needs.

#### Test plan

A test plan is a document detailing the approach that will be taken for intended test activities. The plan may include aspects such as objectives, scope, processes and procedures, personnel requirements, and contingency plans. The test plan could come in the form of a single plan that includes all test types (like an acceptance or system test plan) and planning considerations, or it may be issued as a master test plan that provides an overview of more than one detailed test plan (a plan of a plan). A test plan can be, in some cases, part of a wide "test strategy" which documents overall testing approaches, which may itself be a master test plan or even a separate artifact.

#### Traceability matrix

In software development, a traceability matrix (TM) is a document, usually in the form of a table, used to assist in determining the completeness of a relationship by correlating any two baselined documents using a many-to-many relationship comparison. It is often used with high-level requirements (these often consist of marketing requirements) and detailed requirements of the product to the matching parts of high-level design, detailed design, test plan, and test cases.

#### Test case

A test case normally consists of a unique identifier, requirement references from a design specification, preconditions, events, a series of steps (also known as actions) to follow, input, output, expected result, and the actual result. Clinically defined, a test case is an input and an expected result. This can be as terse as "for condition x your derived result is y", although normally test cases describe in more detail the input scenario and what results might be expected. It can occasionally be a series of steps (but often steps are contained in a separate test procedure that can be exercised against multiple test cases, as a matter of economy) but with one expected result or expected outcome. The optional fields are a test case ID, test step, or order of execution number, related requirement(s), depth, test category, author, and check boxes for whether the test is automatable and has been automated. Larger test cases may also contain prerequisite states or steps, and descriptions. A test case should also contain a place for the actual result. These steps can be stored in a word processor document, spreadsheet, database, or other common repositories. In a database system, you may also be able to see past test results, who generated the results, and what system configuration was used to generate those results. These past results would usually be stored in a separate table.

#### Test script

A test script is a procedure or programming code that replicates user actions. Initially, the term was derived from the product of work created by automated regression test tools. A test case will be a baseline to create test scripts using a tool or a program.

#### Test suite

In software development, a test suite, less commonly known as a validation suite, is a collection of test cases that are intended to be used to test a software program to show that it has some specified set of behaviors. A test suite often contains detailed instructions or goals for each collection of test cases and information on the system configuration to be used during testing. A group of test cases may also contain prerequisite states or steps and descriptions of the following tests.

#### Test fixture or test data

In most cases, multiple sets of values or data are used to test the same functionality of a particular feature. All the test values and changeable environmental components are collected in separate files and stored as test data. It is also useful to provide this data to the client and with the product or a project. There are techniques to generate Test data.

#### Test harness

The software, tools, samples of data input and output, and configurations are all referred to collectively as a test harness.

#### Test run

A test run is a collection of test cases or test suites that the user is executing and comparing the expected with the actual results. Once complete, a report or all executed tests may be generated.

### Certifications

Several certification programs exist to support the professional aspirations of software testers and quality assurance specialists. A few practitioners argue that the testing field is not ready for certification, as mentioned in the controversy section.


## Controversy

Some of the major software testing controversies include:

**Agile vs. traditional**

Should testers learn to work under conditions of uncertainty and constant change or should they aim at

process "maturity"

? The

agile testing

movement has received growing popularity since the early 2000s mainly in commercial circles,

whereas government and military

software providers use this methodology but also the traditional test-last models (e.g., in the

Waterfall model

).

**Manual vs. automated testing**

Some writers believe that

test automation

is so expensive relative to its value that it should be used sparingly.

The test automation then can be considered as a way to capture and implement the requirements. As a general rule, the larger the system and the greater the complexity, the greater the ROI in test automation. Also, the investment in tools and expertise can be amortized over multiple projects with the right level of knowledge sharing within an organization.

**Is the existence of the ISO 29119 software testing standard justified?**

Significant opposition has formed out of the ranks of the context-driven school of software testing about the ISO 29119 standard. Professional testing associations, such as the International Society for Software Testing, have attempted to have the standard withdrawn.

**Some practitioners declare that the testing field is not ready for certification**

No certification now offered actually requires the applicant to show their ability to test software. No certification is based on a widely accepted body of knowledge. Certification itself cannot measure an individual's productivity, their skill, or practical knowledge, and cannot guarantee their competence, or professionalism as a tester.

**Studies used to show the relative expense of fixing defects**

There are opposing views on the applicability of studies used to show the relative expense of fixing defects depending on their introduction and detection. For example:

> It is commonly believed that the earlier a defect is found, the cheaper it is to fix it. The following table shows the cost of fixing the defect depending on the stage it was found. For example, if a problem in the requirements is found only post-release, then it would cost 10–100 times more to fix than if it had already been found by the requirements review. With the advent of modern continuous deployment practices and cloud-based services, the cost of re-deployment and maintenance may lessen over time.
> 
> | Cost to fix a defect | Time detected |   |   |   |   |   |
> |---|---|---|---|---|---|---|
> | Requirements | Architecture | Construction | System test | Post-release |   |   |
> | Time introduced | Requirements | 1× | 3× | 5–10× | 10× | 10–100× |
> | Architecture | – | 1× | 10× | 15× | 25–100× |   |
> | Construction | – | – | 1× | 10× | 10–25× |   |

> The data from which this table is extrapolated is scant. Laurent Bossavit says in his analysis:
> 
> > The "smaller projects" curve turns out to be from only two teams of first-year students, a sample size so small that extrapolating to "smaller projects in general" is totally indefensible. The GTE study does not explain its data, other than to say it came from two projects, one large and one small. The paper cited for the Bell Labs "Safeguard" project specifically disclaims having collected the fine-grained data that Boehm's data points suggest. The IBM study (Fagan's paper) contains claims that seem to contradict Boehm's graph and no numerical results that clearly correspond to his data points.
> > 
> > Boehm doesn't even cite a paper for the TRW data, except when writing for "Making Software" in 2010, and there he cited the original 1976 article. There exists a large study conducted at TRW at the right time for Boehm to cite it, but that paper doesn't contain the sort of data that would support Boehm's claims.
