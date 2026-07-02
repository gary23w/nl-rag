---
title: "User provisioning software"
source: https://en.wikipedia.org/wiki/User_provisioning_software
domain: scim-provisioning-deep
license: CC-BY-SA-4.0
tags: scim provisioning, cross domain identity management, automated user provisioning, directory synchronization, deprovisioning lifecycle
fetched: 2026-07-02
---

# User provisioning software

**User provisioning software** is software intended to help organizations more quickly, cheaply, reliably and securely manage information about users on multiple systems and applications.

## Background: systems, applications and users

People are represented by user objects or login accounts on different systems and applications.

Examples of systems and applications include:

- LDAP directories.
- Microsoft Active Directory and Novell eDirectory.
- Operating systems such as Linux, Unix, Solaris, AIX, HP-UX and Windows Server.
- Mainframe security products such as RAC/F, CA ACF/2 and CA TopSecret.
- ERP applications such as SAP R/3, PeopleSoft, JD Edwards, Lawson Financials and Oracle eBusiness Suite.
- E-mail systems such as Microsoft Exchange and Lotus Notes.
- Databases such as Oracle, Microsoft SQL Server, IBM DB2 and MySQL.
- A variety of other, custom or vertical-market systems and applications..

User objects generally consist of:

- A unique identifier.
- A description of the person who has been assigned the user object—principally their name.
- Contact information for that person, such as their e-mail address, phone numbers, mailing address, etc.
- Organizational information about that person, such as the ID of their manager, their department or their location.
- A password and/or other authentication factors.

Note that users need not be able to log into a system or application. The user object may be a record in an HR application or an entry in a phone book system, which the user cannot log into but which nonetheless represents the user.

User objects are generally connected to other parts of a system or application through security entitlements. On most systems, this is done by placing a user into one or more security groups, where users of each group are granted some security rights.

## User lifecycle processes

Organizations implement business processes to create, manage and delete user objects on their systems and applications:

- **Onboarding:**
  - Represents the steps taken when a new employee is hired, a contractor starts work, or a customer or partner is granted access to systems.
  - This term alludes to the process of loading passengers onto a commercial airliner.
- **Management:**
  - Users are dynamic—they change names, addresses, responsibilities and more.
  - Changes experienced by users in the physical world must be reflected by user objects on systems and applications.
- **Support:**
  - Users sometimes experience problems with systems and applications. They may forget their password or require new security entitlements, for example.
  - User support means changing data about users on systems and applications, resetting user passwords and so on, to resolve user problems.
- **Deactivation:**
  - Users have a finite lifespan and normally an even shorter relationship with an organization where a system or application is managed.
  - When users leave—termination, resignation, retirement, end of contract, end of customer relationship, etc. -- their access to systems and applications should likewise be deactivated.

Incidentally, the term lifecycle does not imply that users who have been deactivated will necessarily not be onboarded again. However, this does happen. For example, employees may leave a company and be re-hired later, or contractors may end their contract only to be hired as employees.

## User provisioning systems

User provisioning systems are intended to help organizations streamline user lifecycle processes so that updates to user objects on their systems and applications can be made:

- More quickly—so users don't have to wait for changes.
- More efficiently—to reduce the cost of managing systems and applications in response to user lifecycle events.
- More securely—to reduce the risk of system compromise due to user objects that have outlived their usefulness, due to inappropriate security entitlements and due to easily guessed or otherwise compromised passwords.

## User provisioning processes

A user provisioning system may implement one or more processes to achieve the aforementioned goals. These processes may include:

- Auto-provisioning. For example:
  - Monitor an HR application and automatically create new users on other systems and applications when new employee records appear in the HR database.
- Auto-deactivation. For example:
  - Monitor an HR application and automatically deactivate users objects on other systems and applications when an employee records either disappears or is marked as inactive in the HR database.
  - Automatically deactivate user objects for users, such as contractors, whose scheduled termination date has passed.
- Identity synchronization. For example:
  - When changes in a user's e-mail address are detected on a mail system, automatically update the same user's e-mail address on other systems.
  - When changes in a user's name, phone number or mailing address are detected on an HR system, automatically update the same user's e-mail address on other systems.
- Self-service profile changes. For example:
  - Allow users to update their own contact information.
- Self-service access requests. For example:
  - Allow users to request access to systems and applications.
- Delegated access requests. For example:
  - Allow managers to request access to systems and applications on behalf of their direct subordinates.
- Authorization workflow. For example:
  - Ask business stake-holders to review and either approve or reject proposed changes to user profiles or access rights.
- Access certification. For example:
  - Periodically ask managers to verify that the list of their direct subordinates (a) are still employed with the organization and (b) still report to them.
  - Periodically data or application owners to verify a list of users with access to their data or application.

## User provisioning system components

A user provisioning system must, in general, include some or all of the following components:

- Connectors, to read information about users from integrated systems and applications and to send updates (e.g., create new user, delete user, modify user information) back to those systems and applications.
- An internal database, that tracks user objects and other data from integrated systems and applications.
- An auto-discovery system, which populates the internal database using the connectors.
- A user interface where users can review the contents of the internal database, make change requests, approve or reject proposed changes, etc.
- A workflow engine, used primarily to invite users to review and either approve or reject changes.
- A policy engine, which evaluates both current user information and proposed changes to see if they meet corporate rules and regulations.
- A reporting engine, which helps organizations extract information from the internal database.
