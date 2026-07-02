---
title: "Sandbox (software development)"
source: https://en.wikipedia.org/wiki/Sandbox_(software_development)
domain: application-sandboxing
license: CC-BY-SA-4.0
tags: application sandboxing, seccomp filtering, apparmor profile, security enhanced linux, capability based security
fetched: 2026-07-02
---

# Sandbox (software development)

A **sandbox** is a testing environment that isolates untested code changes and outright experimentation from the production environment or repository in the context of software development, including web development, automation, revision control, configuration management (see also change management), and patch management.

Sandboxing protects "live" servers and their data, vetted source code distributions, and other collections of code, data and/or content, proprietary or public, from changes that could be damaging to a mission-critical system or which could simply be difficult to revert, regardless of the intent of the author of those changes. Sandboxes replicate at least the minimal functionality needed to accurately test the programs or other code under development (e.g. usage of the same environment variables as, or access to an identical database to that used by, the stable prior implementation intended to be modified; there are many other possibilities, as the specific functionality needs vary widely with the nature of the code and the application[s] for which it is intended).

The concept of sandboxing is built into revision control software such as Git, CVS and Subversion (SVN), in which developers "check out" a *copy* of the source code tree, or a branch thereof, to examine and work on. After the developer has fully tested the code changes in their own sandbox, the changes would be checked back into and merged with the repository and thereby made available to other developers or end users of the software.

By further analogy, the term "sandbox" can also be applied in computing and networking to other temporary or indefinite isolation areas, such as security sandboxes and search engine sandboxes (both of which have highly specific meanings), that prevent incoming data from affecting a "live" system (or aspects thereof) unless/until defined requirements or criteria have been met.

Sandboxing (see also 'soft launching') is often considered a best practice when making any changes to a system, regardless of whether that change is considered 'development', a modification of configuration state, or updating the system.

## In web services

The term sandbox is commonly used for the development of web services to refer to a mirrored production environment for use by external developers. Typically, a third-party developer will develop and create an application that will use a web service from the sandbox, which is used to allow a third-party team to validate their code before migrating it to the production environment. Microsoft, Google, Amazon, Salesforce, PayPal, eBay, and Yahoo, among others, provide such services.

## In wikis

Wikis also typically employ a shared sandbox model of testing, though it is intended principally for learning and outright experimentation with features rather than for testing of alterations to existing content (the wiki analog of source code). An edit preview mode is usually used instead to test specific changes made to the texts or layout of wiki pages.
