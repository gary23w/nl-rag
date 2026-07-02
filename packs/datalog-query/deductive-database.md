---
title: "Deductive database"
source: https://en.wikipedia.org/wiki/Deductive_database
domain: datalog-query
license: CC-BY-SA-4.0
tags: datalog query language, deductive database query, logic query language, declarative rule language
fetched: 2026-07-02
---

# Deductive database

A **deductive database** is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in its database. Datalog is the language typically used to specify facts, rules and queries in deductive databases. Deductive databases have grown out of the desire to combine logic programming with relational databases to construct systems that support a powerful formalism and are still fast and able to deal with very large datasets. Deductive databases are more expressive than relational databases but less expressive than logic programming systems such as Prolog. In recent years, deductive databases have found new application in data integration, information extraction, networking, program analysis, security, and cloud computing.

Deductive databases reuse many concepts from logic programming; rules and facts specified in Datalog look very similar to those written in Prolog, but there are some important differences:

- Order sensitivity and procedurality: In Prolog, program execution depends on the order of rules in the program and on the order of parts of rules; these properties are used by programmers to build efficient programs. In database languages (like SQL or Datalog), however, program execution is independent of the order of rules and facts.
- Special predicates: In Prolog, programmers can directly influence the procedural evaluation of the program with special predicates such as the cut. This has no correspondence in deductive databases.
- Function symbols: Logic programming languages allow function symbols to build up complex symbols. This is not allowed in deductive databases.
- Tuple-oriented processing: Deductive databases use set-oriented processing, while logic programming languages concentrate on one tuple at a time.
