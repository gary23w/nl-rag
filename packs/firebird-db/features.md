---
title: "Firebird: Features"
source: https://firebirdsql.org/en/features/
domain: firebird-db
license: CC-BY-SA-4.0
tags: firebird database, firebird sql, relational database, interbase fork
fetched: 2026-07-02
---

# Firebird: Features

The open source Firebird® relational database management system performs excellently and scales impressively, from an embedded, single-user model to enterprise-wide deployments with multiple 2Tb+Gb databases running with hundreds of simultaneous clients. **Support of all major platforms and operation systems**

| Firebird supports a number of hardware and software platforms: Windows, Linux, MacOS, HP-UX, AIX, Solaris and more. It runs on at x386, x64 and PowerPC, Sparc and other hardware platforms, and supports an easy migration mechanism between these platforms. Firebird is included into the following Linux repositories: Fedora, OpenSuse, CentOS, Mandriva, Ubuntu.(OS) |   |
|---|---|

**Multi-generation architecture** One of the key Firebird features is its multi-generational architecture, which enables the development and support of hybrid OLTP and OLAP applications. This makes a Firebird database capable of serving simultaneously as both an analytical and an operational data store, because readers do not block writers when accessing the same data under most conditions. (mga) **Powerful and developer-friendly SQL language** Firebird supports stored procedures and triggers, and has comprehensive SQL92 support.

- High compatibility with ANSI SQL
- Common Table Expressions (CTE)
- Flexible transactions management
- Full-blown stored procedures (selectable SP enables joins w/tables)
- Cross-database queries
- Active tables concept and events
- User Defined Functions

(active tables) (events) **Logging and monitoring** Firebird offers Trace API and rich set of monitoring tables (MON$)

- Real-time monitoring
- SQL debugging
- Audit
  - Events
  - Partial or full logging
  - Through remote connection

(monitoring)  **Security**   (security) **Standard security**

- Users and roles
- GRANT/REVOKE on main operations
- Database owner concept

**Windows Trusted Authentication**

- Single-sign on for end-users
- Integration with Windows domain/Active Directory security

**Network**

- The only network port should be open (3050 by default, configurable)
- Aliases (path to the database is not exposed)

**Developer Tools**

|   | Firebird is supported by numerous database connectivity options: Firebird.NET JayBird (Java) Delphi/C++ Builder drivers (Embarcadero Delphi/C++ Builder IDEs include dbExpress drivers to work with Firebird.) FreePascal & Lazarus PHP for Firebird FireRuby and more! |
|---|---|

**More features** **True Open Source** Firebird is free for commercial and educational usage: no license fees, installation or activation restrictions. No double licensing - Firebird license is based on Mozilla Public License. **Deployment**

- Embedded version (in dll) with multi-user support
- Native Windows installer available, localized in most popular languages
- Run as service or as application
- RPM or tar.gz distributions available
- Ability to create custom “100% silent” installers
- Read-only deployments (database and server can be on CD, DVD, Blu-Ray, etc)
- Small footprint (minimal installation is 4Mb, standard is 33Mb)

**Performance**

- Choice of architectures to fit all needs – Embedded, SuperServer, SuperClassic and Classic
- Multi-CPU and multi-core SMP scalability for SuperClassic and Classic architecures
- Database up to 20 Terabytes supported
- Thread-Safe Client Library

**Backup and restore**

- Online backup – ability to create backup copy without stopping database
- Online dump – ability to quickly create copy even for very big database
- Incremental backup – partially supported Point-In-Time Recovery

**Full Text Search**

- Integration with Sphinx, Full Text Search Engine

High compatibility with industry standards on many fronts makes Firebird the obvious choice for developing interoperable applications for homogeneous and hybrid environments. The mix of high performance, small footprint, supreme scalability, silent and simple installation and 100% royalty-free deployment make Firebird a highly attractive choice for all types of software developers and vendors. It is used by approximately 1 million of software developers worldwide. (Firebird works)
