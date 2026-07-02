---
title: "Code review"
source: https://en.wikipedia.org/wiki/Code_review
domain: testing
license: CC-BY-SA-4.0
tags: unit test, tdd, integration test, continuous integration, code review
fetched: 2026-07-02
---

# Code review

**Code review** (sometimes referred to as peer review) is a software quality assurance activity in which one or more people examine the source code of a computer program, either after implementation or during the development process. The persons performing the checking, excluding the author, are called "reviewers". At least one reviewer must not be the code's author.

Code review differs from related software quality assurance techniques like static code analysis, self-checks, testing, and pair programming. Static analysis relies primarily on automated tools, self-checks involve only the author, testing requires code execution, and pair programming is performed continuously during development rather than as a separate step.

## Goal

Although direct discovery of quality problems is often the main goal, code reviews are usually performed to reach a combination of goals:

- *Improving code quality* – Improve internal code quality and maintainability through better readability, uniformity, and understandability
- *Detecting defects* – Improve quality regarding external aspects, especially correctness, but also find issues such as performance problems, security vulnerabilities, and injected malware
- *Learning/Knowledge transfer* – Sharing codebase knowledge, solution approaches, and quality expectations, both to the reviewers and the author
- *Increase sense of mutual responsibility* – Increase a sense of collective code ownership and solidarity
- *Finding better solutions* – Generate ideas for new and better solutions and ideas beyond the specific code at hand
- *Complying with QA guidelines, ISO/IEC standards* – Code reviews are mandatory in some contexts, such as air traffic software and safety-critical software

## Review types

Several variations of code review processes exist, with additional types specified in IEEE 1028.

- Management reviews
- Technical reviews
- Inspections
- Walk-throughs
- Audits

### Inspection (formal)

The first code review process that was studied and described in detail was called "Inspection" by its inventor, Michael Fagan. Fagan inspection is a formal process that involves a careful and detailed execution with multiple participants and phases. In formal code reviews, software developers attend a series of meetings to examine code line by line, often using printed copies. Research has shown formal inspections to be extremely thorough and highly effective at identifying defects.

### Regular change-based code review (Walk-throughs)

Software development teams typically adopt a more lightweight review process in which the scope of each review relates to changes to the codebase corresponding to a ticket, user story, commit, or some other unit of work. Furthermore, there are rules or conventions that integrate the review task into the development workflow through conventions like mandatory review of all tickets, commonly as part of a pull request, instead of explicitly planning each review. Such a process is called "regular, change-based code review". There are many variations of this basic process.

A 2017 survey of 240 development teams found that 90% of teams using code review followed a change-based process, with 60% specifically using regular change-based review. Major software corporations known to use changed-based code review include Microsoft, Google, and Facebook.

## Efficiency and effectiveness

Ongoing research by Capers Jones analyzing over 12,000 software development projects found formal inspections had a latent defect discovery rate of 60-65%, while informal inspections detected fewer than 50% of defects. The latent defect discovery rate for most forms of testing is about 30%. A code review case study published in the book *Best Kept Secrets of Peer Code Review* contradicted the Capers Jones study, finding that lightweight reviews can uncover as many bugs as formal reviews while being faster and less costly.

Studies indicate that up to 75% of code review comments affect software evolvability and maintainability rather than functionality, suggesting that code reviews are an excellent tool for software companies with long product or system life cycles. Therefore, less than 15% of issues discussed in code reviews relate directly to bugs.

### Guidelines

Research indicates review effectiveness correlates with review speed. Optimal code review rates range from 200 to 400 lines of code per hour. Inspecting and reviewing more than a few hundred lines of code per hour for critical software (such as safety critical embedded software) may be too fast to find errors.

### Supporting tools

Static code analysis tools assist reviewers by automatically checking source code for known vulnerabilities and defect patterns, particularly for large chunks of code. A 2012 study by VDC Research reports that 17.6% of the embedded software engineers surveyed currently use automated tools to support peer code review and 23.7% plan to use them within two years.
