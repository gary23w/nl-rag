---
title: "Attribute-based access control"
source: https://en.wikipedia.org/wiki/Attribute-based_access_control
domain: cedar-policy
license: CC-BY-SA-4.0
tags: cedar policy language, cedar authorization, policy as code, access control policy
fetched: 2026-07-02
---

# Attribute-based access control

**Attribute-based access control** (**ABAC**), also known as **policy-based access control** for IAM, defines an access control paradigm whereby a subject's authorization to perform a set of operations is determined by evaluating attributes associated with the subject, object, requested operations, and, in some cases, environment attributes.

ABAC is a method of implementing access control policies that is highly adaptable and can be customized using a wide range of attributes, making it suitable for use in distributed or rapidly changing environments. The only limitations on the policies that can be implemented with ABAC are the capabilities of the computational language and the availability of relevant attributes. ABAC policy rules are generated as Boolean functions of the subject's attributes, the object's attributes, and the environment attributes.

Unlike role-based access control (RBAC), which defines roles that carry a specific set of privileges associated with them and to which subjects are assigned, ABAC can express complex rule sets that can evaluate many different attributes. Through defining consistent subject and object attributes into security policies, ABAC eliminates the need for explicit authorizations to individuals’ subjects needed in a non-ABAC access method, reducing the complexity of managing access lists and groups.

Attribute values can be set-valued or atomic-valued. Set-valued attributes contain more than one atomic value. Examples are *role* and *project*. Atomic-valued attributes contain only one atomic value. Examples are *clearance* and *sensitivity*. Attributes can be compared to static values or to one another, thus enabling relation-based access control.

Although the concept itself existed for many years, ABAC is considered a "next generation" authorization model because it provides dynamic, context-aware and risk-intelligent access control to resources allowing access control policies that include specific attributes from many different information systems to be defined to resolve an authorization and achieve an efficient regulatory compliance, allowing enterprises flexibility in their implementations based on their existing infrastructures.

Attribute-based access control is sometimes referred to as **policy-based access control** (**PBAC**) or **claims-based access control** (**CBAC**), which is a Microsoft-specific term. The key standards that implement ABAC are XACML and ALFA (XACML).

## Dimensions of attribute-based access control

ABAC can be seen as:

- Externalized authorization management
- Dynamic authorization management
- Policy-based access control
- Fine-grained authorization

## Components

### Architecture

ABAC comes with a recommended architecture which is as follows:

1. The PEP or Policy Enforcement Point: it is responsible for protecting the apps & data you want to apply ABAC to. The PEP inspects the request and generates an authorization request from which it sends to the PDP.
2. The PDP or Policy Decision Point is the brain of the architecture. This is the piece which evaluates incoming requests against policies it has been configured with. The PDP returns a Permit/Deny decision. The PDP may also use PIPs to retrieve missing metadata
3. The PIP or Policy Information Point bridges the PDP to external sources of attributes e.g. LDAP or databases.

### Attributes

Attributes can be about anything and anyone. They tend to fall into 4 different categories:

1. Subject attributes: attributes that describe the user attempting the access e.g. age, clearance, department, role, job title
2. Action attributes: attributes that describe the action being attempted e.g. read, delete, view, approve
3. Object attributes: attributes that describe the object (or resource) being accessed e.g. the object type (medical record, bank account), the department, the classification or sensitivity, the location
4. Contextual (environment) attributes: attributes that deal with time, location or dynamic aspects of the access control scenario

### Policies

Policies are statements that bring together attributes to express what can happen and is not allowed. Policies in ABAC can be granting or denying policies. Policies can also be local or global and can be written in a way that they override other policies. Examples include:

1. A user can view a document if the document is in the same department as the user
2. A user can edit a document if they are the owner and if the document is in draft mode
3. Deny access before 9 AM

With ABAC you can have an unlimited number of policies that cater to many different scenarios and technologies.

## Other models

Historically, access control models have included mandatory access control (MAC), discretionary access control (DAC), and more recently role-based access control (RBAC). These access control models are user-centric and do not take into account additional parameters such as resource information, the relationship between the user (the requesting entity) and the resource, and dynamic information, e.g. time of the day or user IP.

ABAC tries to address this by defining access control based on attributes which describe the requesting entity (the user), the targeted object or resource, the desired action (view, edit, delete), and environmental or contextual information. This is why access control is said to be attribute-based.

## Implementations

There are three main implementations of ABAC:

- OASIS XACML
- Abbreviated Language for Authorization (ALFA).
- NIST's Next-generation Access Control (NGAC)

XACML, the eXtensible Access Control Markup Language, defines an architecture (shared with ALFA and NGAC), a policy language, and a request/response scheme. It does not handle attribute management (user attribute assignment, object attribute assignment, environment attribute assignment) which is left to traditional IAM tools, databases, and directories.

Companies, including every branch in the United States military, have started using ABAC. At a basic level, ABAC protects data with 'IF/THEN/AND' rules rather than assign data to users. The US Department of Commerce has made this a mandatory practice and the adoption is spreading throughout several governmental and military agencies.

## Applications

The concept of ABAC can be applied at any level of the technology stack and an enterprise infrastructure. For example, ABAC can be used at the firewall, server, application, database, and data layer. The use of attributes bring additional context to evaluate the legitimacy of any request for access and inform the decision to grant or deny access.

An important consideration when evaluating ABAC solutions is to understand its potential overhead on performance and its impact on the user experience. It is expected that the more granular the controls, the higher the overhead.

### API and microservices security

ABAC can be used to apply attribute-based, fine-grained authorization to the API methods or functions. For instance, a banking API may expose an `approveTransaction(transId)` method. ABAC can be used to secure the call. With ABAC, a policy author can write the following:

- **Policy**: managers can approve transactions up to their approval limit
- **Attributes used**: role, action identifier, object type, amount, approval limit.

The flow would be as follows:

1. The user, Alice, calls the API method `approveTransaction(123)`
2. The API receives the call and authenticates the user.
3. An interceptor in the API calls out to the authorization engine (typically called a Policy Decision Point or PDP) and asks: *Can Alice approve transaction 123?*
4. The PDP retrieves the ABAC policy and necessary attributes.
5. The PDP reaches a decision e.g. Permit or Deny and returns it to the API interceptor
6. If the decision is Permit, the underlying API business logic is called. Otherwise the API returns an error or access denied.

### Application security

One of the key benefits to ABAC is that the authorization policies and attributes can be defined in a technology neutral way. This means policies defined for APIs or databases can be reused in the application space. Common applications that can benefit from ABAC are:

1. Content management systems (CMS)
2. Enterprise resource planning (ERP) systems
3. Home-grown applications
4. Web applications

The same process and flow as the one described in the API section applies here too.

### Database security

Security for databases has long been specific to the database vendors: Oracle VPD, IBM FGAC, and Microsoft RLS are all means to achieve fine-grained ABAC-like security.

An example would be:

- Policy: managers can view transactions in their region
- Reworked policy in a data-centric way: users with `role = manager` can do the action `SELECT` on `table = TRANSACTIONS` if `user.region = transaction.region`

### Data security

Data security typically goes one step further than database security and applies control directly to the data element. This is often referred to as data-centric security. On traditional relational databases, ABAC policies can control access to data at the table, column, field, cell and sub-cell using logical controls with filtering conditions and masking based on attributes. Attributes can be data, user, session or tools based to deliver the greatest level of flexibility in dynamically granting/denying access to a specific data element. On big data, and distributed file systems such as Hadoop, ABAC applied at the data layer control access to folder, sub-folder, file, sub-file and other granular.

### Big data security

Attribute-based access control can also be applied to Big Data systems like Hadoop. Policies similar to those used previously can be applied when retrieving data from data lakes.

### File server security

As of Windows Server 2012, Microsoft has implemented an ABAC approach to controlling access to files and folders. This is achieved through dynamic access control (DAC) and Security Descriptor Definition Language (SDDL). SDDL can be seen as an ABAC language as it uses metadata of the user (claims) and of the file/ folder to control access.
