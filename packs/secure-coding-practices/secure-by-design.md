---
title: "Secure by design"
source: https://en.wikipedia.org/wiki/Secure_by_design
domain: secure-coding-practices
license: CC-BY-SA-4.0
tags: secure coding practices, static application security testing, dynamic application security testing, secure by design, input validation
fetched: 2026-07-02
---

# Secure by design

**Secure by design** (SbD) is a cyber security and systems engineering concept that mandates that security be incorporated into systems from the outset rather than as an afterthought. Instead of being retrofitted later through patching or external controls, it focuses on integrating security requirements into the architecture itself by incorporating protections at the very beginning of the design process for hardware, software, and services.

Assuming that systems will be attacked, secure by design entails limiting their architecture to make compromises challenging, contained, and recoverable. It highlights strategies like defence in depth, minimising attack surfaces, the principle of least privilege principle, and integrating detection and response mechanisms. SbD treats security as a design constraint on par with performance, usability, and cost, in contrast to reactive approaches that mainly rely on vulnerability management after deployment.

Since significant cyber events, such as supply chain breaches and ransomware campaigns, have shown the shortcomings of reactive security, secure by design has gained popularity in the twenty-first century. SbD practices are now more frequently required by governments, businesses, and standards organisations in a variety of domains, from consumer Internet of Things (IoT) devices to defence systems. There are similarities between the idea and related paradigms like safety by design, privacy by design, and the larger trend towards resilient systems engineering.

## Core concepts

Secure by design is based on a number of fundamental concepts:

- Security as a design constraint: security specifications must be incorporated into the conceptual design process and upheld at all stages of the project's development.
- Anticipate attacks because it is assumed that systems function in hostile environments with active adversaries.
- Least privilege: only the most essential permissions are given to users, processes, and services.
- Layered security controls and defence in depth lessen the chance of total compromise.
- Reduce the attack surface by only exposing necessary features, interfaces, and services.
- Constant assurance: security measures need to be continuously tested, observed, and enhanced.
- Steer clear of secrecy: strong, open design should be the foundation of security, not proprietary obscurity.

These ideas complement and overlap with related paradigms like safety by design, privacy by design, and zero trust architecture (ZTA).

## Methodologies

Secure by design is a design philosophy that can be used in different development lifecycles, such as Agile, Waterfall, and DevSecOps. Frameworks and methods include:

- The Microsoft Security Development Lifecycle (SDL) adds security to every step of making a product.
- NIST SP 800-160 Volume 2 uses systems security engineering to make systems that are hard to break.
- Threat modeling is a set of frameworks, methodologies and techniques to design for security.
- SEI Secure Design Patterns (Carnegie Mellon University, 2009) – strategies that can be used over and over again to solve common security problems.
- MoD Secure by Design Implementation Guide – a set of best practices for the UK defence sector.

## Government and industry adoption

Secure by Design has been required or suggested in a number of fields:

- The National Institute of Standards and Technology (NIST) in the United States promotes SbD through SP 800-160 and SP 800-53 (security controls). The Cybersecurity and Infrastructure Security Agency (CISA) has also put out Secure by Design guidelines for software makers.
- The UK government requires SbD in digital services through the Government Digital Service (GDS) and the Ministry of Defence. This means designing with risk in mind, providing continuous assurance, and reducing attack surfaces.
- The Cyber Resilience Act stresses security throughout the life cycles of products in the European Union, which is in line with SbD principles.
- Consumer IoT: ETSI TS 103 645 sets security standards that are used in IoT rules in the UK and EU.

While widely endorsed, Secure by Design faces challenges in practice. Early investment in security design may increase upfront costs, although the reduction in risk provides long-term benefits. Applying SbD to legacy systems with older architectures is often impractical. Reliance on complex software supply chains with third-party software and components may undermine SbD practices.
