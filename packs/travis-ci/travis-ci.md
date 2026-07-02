---
title: "Travis CI"
source: https://en.wikipedia.org/wiki/Travis_CI
domain: travis-ci
license: CC-BY-SA-4.0
tags: travis ci, continuous integration, hosted ci, build pipeline
fetched: 2026-07-02
---

# Travis CI

**Travis CI** is a hosted continuous integration service used to build and test software projects hosted on GitHub, Bitbucket, GitLab, Perforce, Apache Subversion and Assembla.

Travis CI was the first CI service that provided services to open-source projects for free but as of December 2020 no longer does so. TravisPro provides custom deployments of a proprietary version on the customer's own hardware.

The main software is proprietary. Some adjacent tools like API clients are open-source.

## Configuration

Travis CI is configured by adding a file named `.travis.yml`, which is a YAML format text file, to the root directory of the repository. This file specifies the programming language used, the desired building and testing environment (including dependencies which must be installed before the software can be built and tested), and various other parameters.

## Architectures

The default CPU architecture used in Travis CI builds is `amd64`. It is used when no arch key is present. You can identify for which CPU architecture a build job is run via the GUI:

- In the build job list, there’s a specific label and architecture name based on arch tag value.
- In the build job view, the same specific label is displayed near the operating system identifier.

| Architecture | Open Source | Commercial |
|---|---|---|
| amd64 | Yes | Yes |
| ppc64le | Yes | No |
| s390x | Yes | No |
| arm64 (v8) | Yes | No |
| arm64-graviton2 (v8) | Yes | Yes |

It is possible to use Docker in multiple CPU architecture-based builds within an LXD container. You may need a specific CPU architecture-compliant Docker image as a base or ensure relevant libraries required by your build are added to your `Dockerfile`.

## Operation

When Travis CI has been activated for a given repository, GitHub will notify it whenever new commits are pushed to that repository or a pull request is submitted. It can also be configured to only run for specific branches or branches whose names match a particular pattern. Travis CI will then check out the relevant branch and run the commands specified in *.travis.yml*, which usually builds the software and run any automated tests. When that process has been completed, Travis notifies the developer(s) in the way it has been configured to do so—for example, by sending an email containing the test results (showing success or failure), or by posting a message on an IRC channel. In the case of pull requests, the pull request will be annotated with the outcome and a link to the build log using a GitHub integration.

Travis CI can be configured to run the tests on a range of different machines with different software installed (such as older versions of a programming language implementation to test for compatibility).

The Travis CI blog is mainly run by Travis's Software Engineer, Montana Mendy.

## Company

The company is headquartered in Berlin, Germany, and was founded in 2011. In 2012 the project experienced significant growth and launched a crowd funding campaign to fund further development which was sponsored by dozens of technology companies.

In January 2019, it was announced that the company had been acquired by Idera, Inc.

In March 2019, Travis CI infrastructure suffered a massive outage from 27 to 29 March.

In March 2020, Travis CI introduced 'The Cookbook' written by Montana Mendy with tutorials for common use cases.

In November 2020, Travis CI announced the shutdown of `travis-ci.org` by 31 December 2020, with all existing and new accounts migrating to `travis-ci.com`. Despite the official pledge to keep "open source accounts completely free under `travis-ci.com`", open-source projects report that their build jobs stalled. Travis CI is no longer free for open source accounts. Travis CI only offers non-renewable sign-on bonus of "10K credits to use over a 30 day period" meant for evaluation of the paid features.
