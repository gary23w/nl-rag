---
title: "Role-based access control"
source: https://en.wikipedia.org/wiki/Role-based_access_control
domain: kubernetes-threat-model
license: CC-BY-SA-4.0
tags: kubernetes threat model, cluster attack surface, pod security context, rbac privilege escalation, microservices attack path
fetched: 2026-07-02
---

# Role-based access control

In information security, **role-based access control** (**RBAC**) or **role-based security** is an approach to restricting system access to authorized users. It is a policy-neutral computer access control mechanism defined around roles and privileges. The components of RBAC, such as role-permissions, user-role and role-role relationships, make it simple to perform user assignments. RBAC can be used to facilitate administration of security in large organizations with hundreds of users and thousands of permissions.

Although RBAC is different from mandatory access control and discretionary access control (DAC) frameworks, it can enforce these policies. Its approach is also different from context-based access control and access-control lists. Attribute-based access control and relationship-based access control are models that build on the concept of RBAC.

A 1990s study by NIST demonstrated that RBAC addresses many needs of commercial and government organizations. RBAC is still commonly considered a best practice in information security management, including in implementation of information security standards related to access control.

## Design

Within an organization, roles are created for various job functions. The permissions to perform certain operations are assigned to specific roles. Since users are not assigned permissions directly, but only acquire them through their role (or roles), management of individual user rights becomes a matter of simply assigning appropriate roles to the user's account; this simplifies common operations, such as adding a user, or changing a user's department.

Three primary rules are defined for RBAC:

1. Role assignment: A subject can exercise a permission only if the subject has selected or been assigned a role.
2. Role authorization: A subject's active role must be authorized for the subject. With rule 1 above, this rule ensures that users can take on only roles for which they are authorized.
3. Permission authorization: A subject can exercise a permission only if the permission is authorized for the subject's active role. With rules 1 and 2, this rule ensures that users can exercise only permissions for which they are authorized.

Additional constraints may be applied as well, and roles can be combined in a hierarchy where higher-level roles subsume permissions owned by sub-roles.

With the concepts of role hierarchy and constraints, one can control RBAC to create or simulate lattice-based access control (LBAC). Thus RBAC can be considered to be a superset of LBAC.

When defining an RBAC model, the following conventions are useful:

- S = Subject = A person or automated agent
- R = Role = Job function or title which defines an authority level
- P = Permissions = An approval of a mode of access to a resource
- SE = Session = A mapping involving S, R and/or P
- SA = Subject Assignment
- PA = Permission Assignment
- RH = Partially ordered Role Hierarchy. RH can also be written: ≥ (The notation: x ≥ y means that x inherits the permissions of y.)
  - A subject can have multiple roles.
  - A role can have multiple subjects.
  - A role can have many permissions.
  - A permission can be assigned to many roles.
  - An operation can be assigned to many permissions.
  - A permission can be assigned to many operations.

A constraint places a restrictive rule on the potential inheritance of permissions from opposing roles. Thus it can be used to achieve appropriate separation of duties. For example, the same person should not be allowed to both create a login account and to authorize the account creation.

Thus, using set theory notation:

- $PA\subseteq P\times R$ and is a many to many permission to role assignment relation.
- $SA\subseteq S\times R$ and is a many to many subject to role assignment relation.
- $RH\subseteq R\times R$

A subject may have *multiple* simultaneous sessions with/in different roles.

### Standardized levels

The NIST/ANSI/INCITS RBAC standard (2004) recognizes three levels of RBAC:

1. Core RBAC
2. Hierarchical RBAC, which adds support for inheritance between roles
3. Constrained RBAC, which adds separation of duties

## Relation to other models

RBAC is a flexible access control technology whose flexibility allows it to implement or discretionary access control (DAC) or mandatory access control (MAC). DAC with groups (e.g., as implemented in POSIX file systems) can emulate RBAC. MAC can simulate RBAC if the role graph is restricted to a tree rather than a partially ordered set.

Prior to the development of RBAC, the Bell-LaPadula (BLP) model was synonymous with MAC, and file system permissions were synonymous with DAC. These were considered to be the only known models for access control: if a model was not BLP, it was considered to be a DAC model, and vice versa. Research in the late 1990s demonstrated that RBAC falls in neither category. Unlike context-based access control (CBAC), RBAC does not look at the message context (such as a connection's source). RBAC has also been criticized for leading to role explosion, a problem in large enterprise systems which require access control of finer granularity than what RBAC can provide as roles are inherently assigned to operations and data types. In resemblance to CBAC, an Entity-Relationship Based Access Control system is able to secure instances of data by considering their association to the executing subject.

### Comparing to ACL

Access control lists (ACLs) are used in traditional discretionary access-control (DAC) systems to affect low-level data-objects. RBAC differs from ACL in assigning permissions to operations which change the direct-relations between several entities (see: *ACLg* below). For example, an ACL could be used for granting or denying write access to a particular system file, but it wouldn't dictate how that file could be changed. In an RBAC-based system, an operation might be to 'create a credit account' transaction in a financial application or to 'populate a blood sugar level test' record in a medical application. A Role is thus a sequence of operations within a larger activity. RBAC has been shown to be particularly well suited to separation of duties (SoD) requirements, which ensure that two or more people must be involved in authorizing critical operations. Necessary and sufficient conditions for safety of SoD in RBAC have been analyzed. An underlying principle of SoD is that no individual should be able to effect a breach of security through dual privilege. By extension, no person may hold a role that exercises audit, control or review authority over another, concurrently held role.

A "minimal RBAC Model", *RBACm*, can be compared with an ACL mechanism, *ACLg*, where only groups are permitted as entries in the ACL. Barkley (1997) showed that *RBACm* and *ACLg* are equivalent.

For data interchange, and for "high level comparisons", ACL data can be translated to XACML.

### Attribute-based access control

Attribute-based access control (ABAC) is a model that evolves from RBAC to consider additional attributes in addition to roles and groups. In ABAC, it is possible to use attributes of:

- the user e.g. citizenship, clearance,
- the resource e.g. classification, department, owner,
- the action, and
- the context e.g. time, location, IP.

ABAC is policy-based in the sense that it uses policies rather than static permissions to define what is allowed or what is not allowed.

### Relationship-based access control

Relationship-based access control (ReBAC) is a model that evolves from RBAC. In ReBAC, a subject's permission to access a resource is defined by the presence of relationships between those subjects and resources.

The advantage of this model is that allows for fine-grained permissions; for example, in a social network where users can share posts with other specific users.

## Implementation and standards

The use of RBAC to manage user privileges (computer permissions) within a single system or application is widely accepted as a best practice. A 2010 report prepared for NIST by the Research Triangle Institute analyzed the economic value of RBAC for enterprises and estimated benefits per employee from reduced employee downtime, more efficient provisioning, and more efficient access control policy administration.

In an organization with a heterogeneous IT infrastructure and requirements that span dozens or hundreds of systems and applications, using RBAC to manage sufficient roles and assign adequate role memberships becomes extremely complex without hierarchical creation of roles and privilege assignments. Newer systems extend the older NIST RBAC model to address the limitations of RBAC for enterprise-wide deployments. The NIST model was adopted as a standard by INCITS as ANSI/INCITS 359-2004. A discussion of some of the design choices for the NIST model has also been published.

NIST Special Publication 800-53, an information security standard used by U.S. federal agencies and other organizations, includes role-based access control in its Access Enforcement controls under AC-3(7).

Implementations of the CIS Controls, a set of best practices, often incorporate role-based access control as part of fulfilling Control 6, Access Control Management.

U.S. Health Insurance Portability and Accountability Act (HIPAA) regulations require implementation of access control as part of technical safeguards for electronic protected health information (45 CFR 164.312), and role-based access control is a typical approach in the industry.

The Payment Card Industry Data Security Standard (PCI DSS) requires implementers to "limit access to system components and cardholder data to only those individuals whose job requires such access", including ensuring that "assignment of privileges is based on individual personnel's job classification and function" (Requirement 7), a form of role-based access control.
