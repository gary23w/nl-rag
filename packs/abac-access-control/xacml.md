---
title: "XACML"
source: https://en.wikipedia.org/wiki/XACML
domain: abac-access-control
license: CC-BY-SA-4.0
tags: attribute based access control, xacml policy language, access control policy, authorization model, provisioning technology
fetched: 2026-07-02
---

# XACML

The **eXtensible Access Control Markup Language** (**XACML**) is an XML-based standard markup language for specifying access control policies. The standard, published by OASIS, defines a declarative, fine-grained, attribute-based access control policy language, an architecture, and a processing model describing how to evaluate access requests according to the rules defined in policies.

XACML is primarily an attribute-based access control policy language, but it also defines syntaxes for the requests sent by the Policy Enforcement Point to the Policy Decision Point, also called *authorization decision requests*. The response process follows the aforementioned request flow in reverse. In XACML, attributes—information about the subject accessing a resource, the resource to be addressed, the action to be performed on the resource, and the environment—act as inputs deciding whether access is granted or not. XACML can also be used to implement role-based access control.

In XACML, Rules specify the conditions under which an access request is approved (Permit) or rejected (Deny). If a Rule is applicable to a request but the conditions within the Rule fail to evaluate, the result is Indeterminate. Rules are grouped together in Policies and combined according to a combining algorithm defined by the parent Policy (e.g., deny-unless-permit, permit-unless-deny). Then, Policies may be grouped together in a larger Policy (or PolicySet in XACML 3.0) and combined according to its combining algorithm similarly.

Policies include a Target, which is a condition that determines whether that Policy should be evaluated for a given request. Policies and Rules also include obligations and advice expressions. Obligations specify actions that must be executed during the processing of a request (e.g., for logging). Advice expressions are similar but may be ignored.

XACML separates access control functionality into several components. Each operating environment in which access control is used has a Policy Enforcement Point (PEP), which implements the functionality to demand authorization and to grant or deny access to resources. These refer to an environment-independent and central Policy Decision Point (PDP), which is responsible for making the final access decision. The PDP refers to policies stored in the Policy Retrieval Point (PRP). Policies are managed through a Policy Administration Point (PAP).

XACML 4.0 now has an equivalent representation in JSON: JACAL.

## History

Version 1.0 was ratified by OASIS standards organization in 2003.

Version 2.0 was ratified by OASIS standards organization on February 1, 2005.

Version 3.0 was ratified by OASIS in January 2013 and updated in July 2017 (Version 3.0 Plus Errata 01).

Version 4.0 (Committee Specification Draft 01) was published by OASIS in February 2026.

## Architecture

### Terminology

Non-normative terminology (following RFC 2904, except for PAP)

| Term | Description |
|---|---|
| Policy Administration Point (PAP) | Point that manages access authorization policies |
| Policy Decision Point (PDP) | Point that evaluates access requests against authorization policies before issuing access decisions |
| Policy Enforcement Point (PEP) | Point that intercepts a user's access request to a resource, requests an access decision from the PDP (i.e., whether access to the resource is approved or rejected), and acts on the received decision |
| Policy Information Point (PIP) | System entity that acts as a source of attribute values (e.g., a resource, subject, environment) |
| Policy Retrieval Point (PRP) | Point where the XACML access authorization policies are stored—typically a database or the filesystem. |

### Flow

1. A user sends a request to access a resource; this request is intercepted by the Policy Enforcement Point (PEP).
2. The PEP converts the request into a XACML authorization request.
3. The PEP forwards the authorization request to the Policy Decision Point (PDP).
4. The PDP evaluates the authorization request against its configured policies. The policies are acquired via a Policy Retrieval Point (PRP) and managed by a Policy Administration Point (PAP). If needed, the PDP also retrieves attribute values from underlying Policy Information Points (PIP).
5. The PDP reaches a decision (Permit, Deny, NotApplicable, or Indeterminate) and returns it to the PEP.
6. The PEP enforces the access decision against the user's request.

## Policy elements

### Structural elements

XACML is structured into the following levels of elements:

- PolicySet (replaced with/merged into Policy in XACML 4.0),
- Policy,
- Rule.

Up to XACML 3.0, a PolicySet can contain any number of PolicySet and/or Policy elements, and a Policy can contain any number of Rule elements.

In XACML 4.0, a Policy can contain any number of Policy and/or Rule elements. There is no longer a distinction between Policy and PolicySet distinction.

### Attributes and categories

Policies, Rules, and requests all use subjects, resources, environments, and actions.

- A subject element is the entity requesting access. A subject has one or more attributes.
- The resource element is what the subject is requesting to access, e.g. some data, service or system component. A resource has one or more attributes.
- An action element defines the type of access requested on the resource. Actions have one or more attributes.
- An environment element can optionally provide additional information that is not specific to the subject, resource or action, but still in the context of the access request, e.g. the current date/time.

### Targets

XACML provides a target, which is basically a condition about the attributes of the subject and/or resource and/or action and/or environment that must be met for a policy or rule to apply to a given request. Once a policy is found to apply to a given request, its rules are evaluated to determine the access decision and response.

In addition to being a way to check applicability, target information also provides a way to index policies, which is useful if you need to store many policies and then quickly sift through them to find which ones apply. When a request to access that service arrives, the PDP will know where to look for policies that might apply to this request because the policies are indexed based on their target constraints. Note that a target may also specify that it applies to any request.

Policies and rules can all contain target elements.

### Conditions

Conditions only exist in Rules. Conditions are essentially boolean expressions that can use *AND, OR, NOT* operators and a broad range of functions that can be used to compare two or more attributes together, e.g. subject-id==doctor-id.

Up to XACML 3.0, Conditions are a more advanced form of Targets, whereas in XACML 4.0 they are the same.

With conditions, it is possible to implement segregation of duty checks or relationship-based access control.

### Obligations & Advice

Within XACML, a concept called obligations can be used. An obligation is a directive from the policy decision point (PDP) to the policy enforcement point (PEP) on what must be carried out before or after an access is approved. If the PEP is unable to comply with the directive, the approved access *may* or *must* not be realized. The augmentation of obligations eliminates a gap between formal requirements and policy enforcement. An example of an obligation could look like this:

```
Access control rule:
          Allow access to resource MedicalJournal with attribute patientID=x 
                if Subject match DesignatedDoctorOfPatient
                and action is read
          with obligation
               on Permit: doLog_Inform(patientID, Subject, time)
               on Deny  : doLog_UnauthorizedLogin(patientID, Subject, time)
```

The XACML's obligation can be an effective way to meet formal requirements (non-repudiation for example) that can be hard to implement as access control rules. Furthermore, any formal requirements will be part of the access control policy as obligations and not as separate functions, which makes policies consistent and centralization of the IT environment easier to achieve.

Obligations can be used for "break-the-glass" scenarios or trust elevation ("you cannot transfer $1,000 without two-factor authentication - here is the link to the 2FA page").

In addition to obligations, XACML supports advice which are identical to obligations with the difference that a PEP is not obligated to enforce the advice (hence its name).

## Combining algorithms

What happens in XACML if there are two rules (or policies) that contradict each other? Imagine for instance a first rule that would say *managers can view documents* and a second rule that would say *no one can work before 9am*. What if the request is about Alice trying to view a document at 8am? Which rule wins? This is what combining algorithms tell us. They help resolve conflicts.

XACML defines a number of combining algorithms that can be identified by a *CombiningAlgId* attribute of the <Policy> (in XACML 4.0; or *PolicyCombiningAlgId* in XACML 3.0 <PolicySet> elements and *RuleCombiningAlgId* in <Policy> elements respectively). The combining algorithm of a policy *P* defines a procedure for combining the individual decision results of the rules and/or policies in *P* into one final access decision for *P*.

## Functions

XACML defines a long list of functions (close to 300) to manipulate and compare attributes to other attributes and values:

- Equality, inequality and other matching functions
- Arithmetic functions
- String functions
- Logical functions (and, or, not)
- Set and bag functions
- Aggregate functions
- Higher order functions
- Regular expression functions
- XPath functions

The functions and their identifiers are fully described in the standard. Functions are type-specific i.e. there is a function for string equality and a different one for integer equality.

### Equality, inequality and other matching functions

### Arithmetic functions

Refer to the standard for a formal definition of these function.

- add (double and integer)
- subtract (double and integer)
- multiply (double and integer)
- divide (double and integer)
- mod (double and integer)
- abs (double and integer)
- round
- floor

### String functions

Refer to the standard for a formal definition of these function.

- string-concatenate
- string-starts-with
- string-ends-with
- string-contains
- string-substring

### Logical functions (and, or, not)

### Set and bag functions

### Regular expression functions

### XPath functions

### Higher order functions

The list of higher order functions is as listed below. For a formal definition, refer to the XACML standard.

- anyOf (urn:oasis:names:tc:xacml:3.0:function:any-of)
  - parameters: anyAtomicOrBag anyAtomicOrBag*
  - return value: boolean
  - Description: this function takes in a Boolean function and 2 or more attribute values or bags. The higher-order function applies the Boolean function to the remaining parameters.
  - Example: `anyOf(function[stringEqual], allowedRoles, stringOneAndOnly(role))` will return true if (a) role is single-valued, (b) there is at least one value in the attribute bag allowedRoles equal to the value inside the single-valued attribute bag role.
- allOf (urn:oasis:names:tc:xacml:3.0:function:all-of)
  - parameters: anyAtomicOrBag anyAtomicOrBag*
  - return value: boolean
- anyOfAny (urn:oasis:names:tc:xacml:3.0:function:any-of-any)
  - parameters: anyAtomicOrBag anyAtomicOrBag*
  - return value: boolean
- allOfAny (urn:oasis:names:tc:xacml:1.0:function:all-of-any)
  - parameters: bag[anyAtomic] bag[anyAtomic]
  - return value: boolean
- anyOfAll (urn:oasis:names:tc:xacml:1.0:function:any-of-all)
  - parameters: bag[anyAtomic] bag[anyAtomic]
  - return value: boolean
- allOfAll (urn:oasis:names:tc:xacml:1.0:function:all-of-all)
  - parameters: bag[anyAtomic] bag[anyAtomic]
  - return value: boolean
- map (urn:oasis:names:tc:xacml:1.0:function:map)
  - parameters: anyAtomicOrBag anyAtomicOrBag*
  - return value: bag[anyAtomic]

## XACML 4.0

### Core specification and schema

https://docs.oasis-open.org/xacml/acal/xacml/core/v4.0/csd01/

### Profiles

https://docs.oasis-open.org/xacml/acal/xacml/profiles/

*See also the JSON variant (JACAL):*

https://docs.oasis-open.org/xacml/acal/jacal/

### New in XACML 4.0

#### Model simplifications

- *PolicySet* merged into *Policy* without distinction;
- *Target* and *Condition* having the same structure;
- *Obligation*(*Expression*) and *Advice*(*Expression*) merged into *Notice*(*Expression*) (*isObligation = true|false*);
- *AttributeValue* changed to more generic *Value;*
- Boolean attributes (*CombinedDecision*, *ReturnPolicyIdList*, *MustBePresent*, *IncludeInResult*, etc.) made optional with default values;
- *DataType* attribute made optional in several cases where type inference / implicit typing is possible;
- Removed unused feature *CombinerParameter;*
- XPath features removed from the Core specification and moved to the new XPath Profile.

#### New features

- Core:
  - XACML is now based on the same agnostic model ACAL as other ACAL representations such as JACAL, and therefore translating policies (or requests) between XACML and other ACAL representations such as JACAL is facilitated;
  - More expressive *Targets;*
  - *Rules* may contain *VariableDefinitions;*
  - Short identifiers (aliases) may be defined and used, in place of URIs, as identifiers of attributes, categories, datatypes, functions and combining algorithms;
  - Global variables reusable across *Policies;*
  - New functions:
    - Aggregate functions applicable to bags: min, max, sum, avg;
    - Ternary conditional / Elvis operator;
  - Extensible Content type and encoding in *Requests* to support non-XML content*.*
- Profiles:
  - **JSONPath Profile** adds support for JSONPath (RFC 9535) based *AttributeSelectors*
  - XPath Profile adds support for XPath 3.0 and 3.1

## XACML 3.0

### Schema

http://docs.oasis-open.org/xacml/3.0/xacml-core-v3-schema-wd-17.xsd

### Data types

- http://www.w3.org/2001/XMLSchema#anyURI
- http://www.w3.org/2001/XMLSchema#base64Binary
- http://www.w3.org/2001/XMLSchema#boolean
- http://www.w3.org/2001/XMLSchema#date
- http://www.w3.org/2001/XMLSchema#dateTime
- http://www.w3.org/2001/XMLSchema#dayTimeDuration
- http://www.w3.org/2001/XMLSchema#double
- http://www.w3.org/2001/XMLSchema#hexBinary
- http://www.w3.org/2001/XMLSchema#integer
- http://www.w3.org/2001/XMLSchema#string
- http://www.w3.org/2001/XMLSchema#time
- http://www.w3.org/2001/XMLSchema#yearMonthDuration
- urn:oasis:names:tc:xacml:1.0:data-type:rfc822Name
- urn:oasis:names:tc:xacml:1.0:data-type:x500Name
- urn:oasis:names:tc:xacml:2.0:data-type:dnsName
- urn:oasis:names:tc:xacml:2.0:data-type:ipAddress
- urn:oasis:names:tc:xacml:3.0:data-type:xpathExpression

### New in XACML 3.0

#### New profiles

XACML 3.0 introduces administrative delegation, the JSON Profile of XACML (request/response), the REST Profile of XACML, the Multiple Decision Profile of XACML, and many more.

##### Delegation

The implementation of delegation is new in XACML 3.0. The delegation mechanism is used to support decentralized administration of access policies. It allows an authority (delegator) to delegate all or parts of its own authority or someone else's authority to another user (delegate) without any need to involve modification of the root policy.

This is because, in this delegation model, the delegation rights are separated from the access rights. These are instead referred to as administrative control policies. Access control and administrative policies work together as in the following scenario:

A partnership of companies' many services are protected by an access control system. The system implements the following central rules to protect its resources and to allow delegation:

```
Access control rules:

              Allow access
                    to resource with attribute WebService 
                    if subject is Employee and action is read or write. 
              
Administration control rules:

              Allow delegation of access control rule #1
                      to subjects with attribute Consultant.
              Conditions: 
                         delegation must expire within 6 months,
                         resource must not have attribute StrictlyInternal.
               
```

(Attributes can be fetched from an external source, e.g. a LDAP catalog.)

When a consultant enters the corporation, a delegation can be issued locally by the consultant's supervisor, authorizing the consultant access to systems directly.

The delegator (the supervisor in this scenario) may only have the right to delegate a limited set of access rights to consultants.

#### Other features

Other new features of XACML 3.0 are listed at http://www.webfarmr.eu/2010/07/enhancements-and-new-features-in-xacml-3-axiomatics/

The XACML TC is also publishing a list of changes here: http://wiki.oasis-open.org/xacml/DifferencesBetweenXACML2.0AndXACML3.0

## The Multiple Decision Profile of XACML 3.0

By default a PDP processes a single request at a time. The PDP then replies with a single decision. At times, though, it is necessary to send multiple requests simultaneously. The Multiple Decision Profile of XACML allows for this use case. The PDP will typically return the product of all combinations in a single response.

## Developer orientation

In 2013 and 2014, the XACML Technical Committee focused on designing new profiles to facilitate developer integration. These include:

- The REST profile of XACML written by Remon Sinnema of EMC
- The JSON profile of XACML written by David Brossard of Axiomatics
- The ALFA profile of XACML written by Pablo Giambiagi, Srijith Nair, and David Brossard of Axiomatics

All three profiles were showcased at the Cloud Identity Summit 2014 in Monterey, California. Using these profiles, integrating fine-grained authorization into applications becomes much easier.

In 2026, XACML 4.0 is released with major simplifications to the data and processing model, better support for JSON input data (with JSONPath profile), and the JACAL standard is released as a JSON syntax equivalent of XACML 4.0 for both policies and decision requests/responses.

### XACML 4.0 and the JSON representation of ACAL (JACAL)

JACAL 1.0 is aligned with XACML 4.0 as it shares the same agnostic model ACAL.

### The ALFA Profile of XACML 3.0

ALFA stands for Abbreviated Language for Authorization. It is a lightweight syntax used to implement policy-based access control policies. For examples refer to the main article.

### The JSON Profile of XACML 3.0

The JSON profile of XACML simplifies the integration between the PEP and the PDP.

## XACML and other standards

### XACML and Open Policy Agent

XACML is almost entirely a **policy definition language** based on XML, defined by an open OASIS specification. The XACML specification  does not cover the design or implementation of Policy Decision Point (PDP), only the policy language they consume. Many proprietary and open-source PDPs use XACML as their policy definition language.

Open Policy Agent (OPA) is an open-source Policy Decision Point (PDP) implementation, capable of interpreting policy language to render policy decisions. OPA is a general-purpose PDP implementation which can be used for any scenario where a policy decision is required, much like PDP implementations that support the XACML specification.

OPA's policy definition language is (Rego), which is a JSON-based, Turing-incomplete language based on Datalog.

The project xacml-with-opa shows how to support the JSON Profile of XACML 3.0 with OPA.

XACML Policies may be translatable to Rego but not always, because of certain Rego limitations such as:

- No XML / XPath support (OPA issue #7361);
- No OR operator (OPA issue #7602);
- No nested AND/OR logic in rules (OPA issue #3183);
- Limited use of NOT operator (OPA issue #3924).

### XACML and SAML

SAML is an identity SSO and federation standard used for authentication. SAML is used as a common identity token format between different applications. SAML and XACML are both defined by OASIS. SAML and XACML were designed to interoperate where SAML is used to carry identity information / virtual identities and XACML is used to drive the access control logic through policies.

### XACML and OAuth

OAuth 2.0 is considered to be an authorization standard. It differs from XACML though in its origin, its purpose, and its applications. OAuth is about:

- delegated access control: I, the user, delegate another user or service access to the resource I own. For instance via OAuth, I grant Twitter (the service) the ability to post on my Facebook wall (the resource).
- handling the password anti-pattern. Whenever you want to integrate 2 services together, in a traditional, legacy model you have to provide service B with your user credentials on service A so that service B can pretend to be you with Service A. This has many risks of course. Using OAuth eliminates the issues with these patterns and lets the user control what service B can do on behalf of the user with service A.
- HTTP-based services / resources
- managing owner (user) approval

XACML does not handle user approval or delegated access or password management. XACML simply provides:

- An access control architecture with the notion of a Policy Decision Point (PDP) as previously discussed and a Policy Enforcement Point (PEP).
- a policy language with which to express a wide range of access control policies including policies that can use consents handled / defined via OAuth.

XACML and OAuth can be combined to deliver a more comprehensive approach to authorization.
