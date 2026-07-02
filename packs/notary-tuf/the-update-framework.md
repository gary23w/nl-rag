---
title: "The Update Framework"
source: https://en.wikipedia.org/wiki/The_Update_Framework
domain: notary-tuf
license: CC-BY-SA-4.0
tags: the update framework, tuf role delegation, repository signing metadata, rollback attack defense
fetched: 2026-07-02
---

# The Update Framework

**The Update Framework (TUF)** is a software framework designed to protect mechanisms that automatically identify and download updates to software. TUF uses a series of roles and keys to provide a means to retain security, even when some keys or servers are compromised. It does this with a stated goal of requiring minimal changes and effort from repository administrators, software developers, and end users. In this way, it protects software repositories, which are an increasingly desirable target for hackers.

A software update, sometimes referred to as a patch, can add functionalities and address flaws in existing code. Unfortunately, in delivering updates to neutralize flaws, these systems can unintentionally introduce vulnerabilities that, in turn, can be exploited by attackers.

The design of TUF acknowledges that all software repositories will likely be compromised at some point, so any security strategy must be prepared for that scenario. TUF-enabled systems focus on limiting the impact of attacks and providing a mechanism for recovery. This strategy of “compromise-resilience” improves on existing methods based on keysigning by incorporating techniques, such as separation of signing duties and setting a threshold number of required signatures. Dividing the responsibility for authenticating a file or image ensures no single hacker can compromise the system. It also helps to ensure that keys used to perform a sensitive action can be stored in a secure, offline manner. Even if one party—or the repository itself—is compromised, the number of projects affected will be limited.

TUF is designed with an explicit threat model that assumes attackers may compromise software updates in specific ways. Documented attacks on software update systems can include rollback attacks, freeze attacks, mix-and-match attacks, and arbitrary software installation, among others. TUF mitigates these risks through mechanisms such as versioned metadata, expiration times, and role-based signing with threshold signatures.

To date, the list of tech companies and organizations using TUF include Foundries.io, IBM, VMware, Digital Ocean, Microsoft, Google, Amazon, Leap, Kolide, Docker, and Cloudflare.

The technology that evolved into TUF was first developed at the University of Washington in 2009 by Justin Samuel and Justin Cappos, and its principles were first discussed in a paper Samuel and Cappos coauthored with Nick Mathewson and Roger Dingledine, researchers from The Tor Project, Inc. Since 2011, TUF has been based at New York University Tandon School of Engineering, where Cappos continues to work with a team of graduate students and programmers in the Secure Systems Lab to supervise its maturation, development and integration into production use across different communities.

One of the more significant earlier adoptions of TUF in the open-source community was by Docker Content Trust, an implementation of the Notary project from Docker that deploys Linux containers. Notary, which is built on TUF, can both certify the validity of the sources of Docker images, and encrypt the contents of those images. Through Notary Content Trust, TUF also secures operations for Microsoft Azure.

Since 2017, both Notary and TUF have been hosted by the Linux Foundation under the Cloud Native Computing Foundation. Cappos remains with the project as consensus builder. In December 2019, TUF was awarded “graduate” status within the organization, signifying that it has completed a series of steps needed to move the project to the highest level of maturity in the CNCF. These steps included completing an independent third party security audit, adopting the CNCF Code of Conduct, and explicitly defining a project governance and committer process. TUF became both the first security project and the first project led by an academic researcher to graduate within CNCF.

Because it was designed for easy adaptation, versions of TUF have been created in a number of programming languages. It has been independently implemented in the Go language by Flynn, an open-source platform as a service (PaaS) for running applications in production. Implementations of TUF have also been written in Haskell, Ruby and Rust. A Rust version called Tough was created by Amazon Web Services Labs for use with on-demand cloud computing platforms and APIs . Google has also implemented a version of TUF to secure its open source operating system, Fuchsia.

In 2017, an adaptation of this technology called Uptane, designed to protect computing units on automobiles, was named one of the top security inventions for 2017 by Popular Science.
