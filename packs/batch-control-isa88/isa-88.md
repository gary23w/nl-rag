---
title: "ISA-88"
source: https://en.wikipedia.org/wiki/ISA-88
domain: batch-control-isa88
license: CC-BY-SA-4.0
tags: isa-88 batch control, batch process control, batch recipe model, batch manufacturing standard
fetched: 2026-07-02
---

# ISA-88

**ANSI/ISA-88**, is a standard addressing batch process control. It is a design philosophy for describing equipment and procedures. It is not a standard for software and is equally applicable to manual processes. It was approved by the ISA in 1995 and updated in 2010. Its original version was adopted by the IEC in 1997 as IEC 61512-1.

## Parts of the S88 standard

- Models and terminology
- Data structures and guidelines for languages
- General and site recipe models and representation
- Batch Production Records
- Machine and Unit States: An Implementation Example of ISA-88

S88 provides a consistent set of standards and terminology for batch control and defines the physical model, procedures, and recipes. The standard sought to address the following problems: lack of a universal model for batch control, difficulty in communicating user requirement, integration among batch automation suppliers, and difficulty in batch-control configuration.

The standard defines a *process model* that consists of a *process* that consists of an ordered set of *process stages* that consist of an ordered set of *process operations* that consist of an ordered set of *process actions.*

The *physical model* begins with the *enterprise*, which may contain a *site*, which may contain *areas*, which may contain *process cells*, which must contain a *unit*, which may contain *equipment modules*, which may contain *control modules*. Some of these levels may be excluded, but not the Unit.

The *procedural control model* consists of *recipe procedures*, which consist of an ordered set of *unit procedures*, which consist of an ordered set of *operations*, which consist of an ordered set of *phases.* Some of these levels may be excluded.

Recipes can have the following types: general, site, master, control. The contents of the recipe include: header, formula, equipment requirements, procedure, and other information required to make the recipe.

## Implemented in other standards

Like in Packml, the Machine and Unit States described by this standard are implemented in other standards.
