---
title: "Web Services Discovery"
source: https://en.wikipedia.org/wiki/Universal_Description_Discovery_and_Integration
domain: soap-protocol
license: CC-BY-SA-4.0
tags: soap protocol, simple object access protocol, wsdl service, xml web service
fetched: 2026-07-02
---

# Web Services Discovery

(Redirected from

Universal Description Discovery and Integration

)

**Web Services Discovery** provides access to software systems over the Internet using standard protocols. In the most basic scenario there is a *Web Service Provider* that publishes a service and a *Web Service Consumer* that uses this service. Web Service Discovery is the process of finding suitable web services for a given task.

Publishing a web service involves creating a software artifact and making it accessible to potential consumers. Web service providers augment a service endpoint interface with an interface description using the Web Services Description Language (WSDL) so that a consumer can use the service.

**Universal Description, Discovery, and Integration** (**UDDI**) is an XML-based registry for business internet services. A provider can explicitly register a service with a *Web Services Registry* such as UDDI or publish additional documents intended to facilitate discovery such as Web Services Inspection Language (WSIL) documents. The service users or consumers can search web services manually or automatically. The implementation of UDDI servers and WSIL engines should provide simple search APIs or web-based GUI to help find Web services.

Web services may also be discovered using multicast mechanisms like WS-Discovery, thus reducing the need for centralized registries in smaller networks.

## Universal Description Discovery and Integration

**Universal Description, Discovery and Integration** (**UDDI**, pronounced /ˈjʊdiː/) is a platform-independent, Extensible Markup Language protocol that includes a (XML-based) registry by which businesses worldwide can list themselves on the Internet, and a mechanism to register and locate web service applications. UDDI is an open industry initiative, sponsored by the Organization for the Advancement of Structured Information Standards (OASIS), for enabling businesses to publish service listings and discover each other, and to define how the services or software applications interact over the Internet.

UDDI was originally proposed as a core Web service standard. It is designed to be interrogated by SOAP messages and to provide access to Web Services Description Language (WSDL) documents describing the protocol bindings and message formats required to interact with the web services listed in its directory.

## History of UDDI

UDDI was written in August 2000, at a time when the authors had a vision of a world in which consumers of web services would be linked up with providers through a public or private dynamic brokerage system. In this vision, anyone needing a service, such as credit card authentication, would go to their service broker and select a service supporting the desired SOAP (or other) service interface, and meeting other criteria. In such a world, the publicly operated UDDI node or broker would be critical for everyone. For the consumer, public or open brokers would only return services listed for public discovery by others, while for a service producer, getting a good placement in the brokerage—by relying on metadata of authoritative index categories—would be critical for effective placement.

UDDI was included in the Web Services Interoperability (WS-I) standard as a central pillar of web services infrastructure, and the UDDI specifications supported a publicly accessible Universal Business Registry in which a naming system was built around the UDDI-driven service broker.

UDDI has not been as widely adopted as its designers had hoped. IBM, Microsoft, and SAP announced they were closing their public UDDI nodes in January 2006. The group defining UDDI, the OASIS Universal Description, Discovery, and Integration (UDDI) Specification Technical Committee voted to complete its work in late 2007 and has been closed. In September 2010, Microsoft announced they were removing UDDI services from future versions of the Windows Server operating system. Instead, this capability would be moved to BizTalk Server. In 2013, Microsoft further announced the deprecation of UDDI Services in BizTalk Server. In 2016, Microsoft removed UDDI Services from BizTalk Server.

UDDI systems are most commonly found inside companies, where they are used to dynamically bind client systems to implementations. However, much of the search metadata permitted in UDDI is not used for this relatively simple role.

## Structure of UDDI

A UDDI business registration consists of three components:

- White Pages — address, contact, and known identifiers;
- Yellow Pages — industrial categorizations based on standard taxonomies;
- Green Pages — technical information about services exposed by the business.

### White Pages

White pages give information about the business supplying the service. This includes the name of the business and a description of the business - potentially in multiple languages. Using this information, it is possible to find a service about which some information is already known (for example, locating a service based on the provider's name).

Contact information for the business is also provided - for example the businesses address and phone number; and other information such as the Dun & Bradstreet.

### Yellow Pages

Yellow pages provide a classification of the service or business, based on standard taxonomies. These include the Standard Industrial Classification (SIC), the North American Industry Classification System (NAICS), or the United Nations Standard Products and Services Code (UNSPSC) and geographic taxonomies.

Because a single business may provide a number of services, there may be several Yellow Pages (each describing a service) associated with one White Page (giving general information about the business).

### Green Pages

Green pages are used to describe how to access a Web Service, with information on the service bindings. Some of the information is related to the Web Service - such as the address of the service and the parameters, and references to specifications of interfaces. Other information is not related directly to the Web Service - this includes e-mail, FTP, CORBA and telephone details for the service. Because a Web Service may have multiple bindings (as defined in its WSDL description), a service may have multiple Green Pages, as each binding will need to be accessed differently.

## UDDI nodes and registry

UDDI nodes are servers which support the UDDI specification and belong to a UDDI registry while UDDI registries are collections of one or more nodes.

SOAP is an XML-based protocol to exchange messages between a requester and a provider of a Web Service. The provider publishes the WSDL to UDDI and the requester can join to it using SOAP.

## Federated discovery

The current UDDI search mechanism can only focus on a single search criterion, such as business name, business location, business category, service type by name, business identifier, or discovery URL. In fact, in a business solution, it is very normal to search multiple UDDI registries or WSIL documents and then aggregate the returned result by using filtering and ranking techniques. IBM modularized this federated Web Services Discovery engine in 2001. The released technology from IBM is Business Explorer for Web Services (BE4WS) Archived 2008-05-11 at the Wayback Machine.
