---
title: "Static application security testing"
source: https://en.wikipedia.org/wiki/Static_application_security_testing
domain: secure-coding-practices
license: CC-BY-SA-4.0
tags: secure coding practices, static application security testing, dynamic application security testing, secure by design, input validation
fetched: 2026-07-02
---

# Static application security testing

**Static application security testing** (**SAST**) is used to secure software by reviewing its source code to identify security vulnerabilities. Although the process of checking programs by reading their code (modernly known as static program analysis) has existed as long as computers have existed, the technique spread to security in the late 90s and the first public discussion of SQL injection in 1998 when web applications integrated new technologies like JavaScript and Flash.

Unlike dynamic application security testing (DAST) tools for black-box testing of application functionality, SAST tools focus on the code content of the application, white-box testing. A SAST tool scans the source code of applications and their components to identify potential security vulnerabilities in their software and architecture. Static analysis tools can detect an estimated 50% of existing security vulnerabilities in tested applications.

In the software development life cycle (SDLC), SAST is performed early in the development process and at code level, and also when all pieces of code and components are put together in a consistent testing environment. SAST is also used for software quality assurance, even if the many resulting false positives impede its adoption by developers.

SAST tools are integrated into the development process to help development teams as they are primarily focusing on developing and delivering software respecting requested specifications. SAST tools, like other security tools, focus on reducing the risk of downtime of applications or that private information stored in applications is not compromised.

## Overview

Application security tests conducted before their release include static application security testing (SAST), dynamic application security testing (DAST), and interactive application security testing (IAST), which is a combination of the two.

Static analysis tools examine the text of a program syntactically. They look for a fixed set of patterns or rules in the source code. Theoretically, they can also examine a compiled form of the software. This technique relies on instrumentation of the code to do the mapping between compiled components and source code components to identify issues. Static analysis can be done manually as a code review or auditing of the code for different purposes, including security, but it is time-consuming.

The precision of SAST tools is determined by their scope of analysis and the specific techniques used to identify vulnerabilities. Different levels of analysis include the following:

- Function level: Sequences of instruction
- File or class level: An extensible program-code-template for object creation
- Application level: A program or group of programs that interact

The scope of the analysis determines its accuracy and capacity to detect vulnerabilities using contextual information. SAST tools, unlike DAST tools, give developers real-time feedback, and help them secure flaws before they move the code to the next level.

At a function level, a common technique is the construction of an Abstract syntax tree to control the flow of data within the function.

Since the late 90s, the need to adapt to business challenges has transformed software development with componentization enforced by processes and organization of development teams. Following the flow of data between all the components of an application or group of applications allows validation of required calls to dedicated procedures for sanitization and that proper actions are taken to taint data in specific pieces of code.

The rise of web applications entailed testing them: Verizon Data Breach reported in 2016 that 40% of all data breaches use web application vulnerabilities. Both external security validations and a focus on internal threats have risen. The Clearswift Insider Threat Index (CITI) has reported that 92% of their respondents in a 2015 survey said they had experienced IT or security incidents in the previous 12 months and that 74% of these breaches were originated by insiders. Lee Hadlington categorized internal threats in 3 categories: malicious, accidental, and unintentional. Mobile applications' explosive growth implies securing applications earlier in the development process to reduce malicious code development.

## SAST strengths

The earlier a vulnerability is fixed in the SDLC, the cheaper it is to fix. Costs to fix in development are 10 times lower than in testing, and 100 times lower than in production. SAST tools run automatically, either at the code level or application-level and do not require interaction. When integrated into a CI/CD context, SAST tools can be used to automatically stop the integration process if critical vulnerabilities are identified.

Another advantage over other types of testing is that SAST tools scan the entire source code, while dynamic application security testing tools cover its execution, possibly missing part of the application or unsecured configuration in configuration files.

SAST tools can offer extended functionalities such as quality and architectural testing. There is a direct correlation between software quality and security. Bad quality software is also poorly secured software.

## SAST weaknesses

Even though developers are positive about the usage of SAST tools, there are different challenges to their adoption. As an example, research shows that despite the long output generated by these tools, they may lack usability.

With Agile Processes in software development, early integration of SAST generates many bugs, as developers using this framework focus first on features and delivery.

Scanning many lines of code with SAST tools may result in hundreds or thousands of vulnerability warnings for a single application. It can generate many false positives, increasing investigation time and reducing trust in such tools. This is particularly the case when the context of the vulnerability cannot be caught by the tool.
