---
title: "System for Cross-domain Identity Management"
source: https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management
domain: scim-provisioning
license: CC-BY-SA-4.0
tags: scim provisioning, cross-domain identity management, user provisioning protocol, identity lifecycle api
fetched: 2026-07-02
---

# System for Cross-domain Identity Management

**System for Cross-domain Identity Management** (**SCIM**) is a standard for automating the exchange of user identity information between identity domains, or IT systems.

One example might be that as a company onboards new employees and separates from existing employees, they are added and removed from the company's electronic employee directory. SCIM could be used to automatically add/delete (or, provision/de-provision) accounts for those users in external systems such as Google Workspace, Microsoft 365, or Salesforce.com. Then, a new user account would exist in the external systems for each new employee, and the user accounts for former employees might no longer exist in those systems.

In addition to simple user-record management (creating and deleting), SCIM can also be used to share information about user attributes, attribute schema, and group membership. Attributes could range from user contact information to group membership. Group membership or other attribute values are generally used to manage user permissions. Attribute values and group assignments can change, adding to the challenge of maintaining the relevant data across multiple identity domains.

The SCIM standard has grown in popularity and importance, as organizations use more SaaS tools. A large organization can have hundreds or thousands of hosted applications (internal and external) and related servers, databases and file shares that require user provisioning. Without a standard connection method, companies must write custom software connectors to join these systems and their Identity Management (IdM) system.

SCIM uses a standardised API through REST with data formatted in JSON or XML.

## History

The first version, SCIM 1.0, was released in 2011 by a SCIM standard working group organized under the Open Web Foundation. In 2011, it was transferred to the IETF, and the current standard, SCIM 2.0 was released as IETF RFC in 2015.

SCIM 2.0 was completed in September 2015 and is published as IETF RFCs 7643 and 7644. A use-case document is also available as RFC 7642.

The standard has been implemented in various IdM software.

The standard was initially called ***Simple Cloud Identity Management*** (and is still called this in some places), but the name was officially changed to *System for Cross-domain Identity Management (SCIM)* when the IETF adopted it.

Interoperability was demonstrated in October, 2011, at the Cloud Identity Summit, an IAM industry conference. There, user accounts were provisioned and de-provisioned across separate systems using SCIM standards, by a collection of IdM software vendors: Okta, CyberArk, Ping Identity, SailPoint, Technology Nexus and UnboundID. In March 2012, at IETF 83 in Paris, interoperability tests continued by the same vendors, joined by Salesforce.com, BCPSoft, WSO2, Gluu, and Courion (now SecureAuth) nine companies in total.

SCIM is the second standard for exchanging user data, but it builds on prior standards (e.g. SPML, PortableContacts, vCards, and LDAP directory services) in an attempt to be a simpler and more widely adopted solution for cloud services providers.

The SCIM standard is growing in popularity and has been adopted by numerous identity providers as well as applications. As adoption of the standard grows, so do the number of tools available. The standard leverages a number of open-source libraries to facilitate development and testing frameworks ensure that endpoint's compliance with the SCIM standard.
