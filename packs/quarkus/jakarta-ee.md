---
title: "Jakarta EE"
source: https://en.wikipedia.org/wiki/Jakarta_EE
domain: quarkus
license: CC-BY-SA-4.0
tags: quarkus framework, quarkus native, graalvm native, jakarta ee
fetched: 2026-07-02
---

# Jakarta EE

**Jakarta EE**, formerly **Java Platform, Enterprise Edition** (**Java EE**) and **Java 2 Platform, Enterprise Edition** (**J2EE**), is a set of specifications, extending Java SE with specifications for enterprise features such as distributed computing and web services. Jakarta EE applications are run on reference runtimes, which can be microservices or application servers, which handle transactions, security, scalability, concurrency and management of the components they are deploying.

Jakarta EE is defined by its specification. The specification defines APIs (application programming interface) and their interactions. As with other Java Community Process specifications, providers must meet certain conformance requirements in order to declare their products as *Jakarta EE compliant*.

Examples of contexts in which Jakarta EE referencing runtimes are used are: e-commerce, accounting, banking information systems.

## History

The platform created by Sun Microsystems was known as *Java 2 Platform, Enterprise Edition* or *J2EE* from version 1.2, until the name was changed to *Java Platform, Enterprise Edition* or *Java EE* in version 1.5.

After Sun was acquired in 2009, Java EE was maintained by Oracle under the Java Community Process. On September 12, 2017, Oracle Corporation announced that it would submit Java EE to the Eclipse Foundation. The Eclipse top-level project has been named Eclipse Enterprise for Java (EE4J). The Eclipse Foundation could not agree with Oracle over the use of `javax` and Java trademarks. Oracle owns the trademark for the name "Java" and the platform was renamed from Java EE to Jakarta EE. The name refers to the largest city on the island of Java and also the capital of Indonesia, Jakarta. The name should not be confused with the former Jakarta Project which fostered a number of current and former Java projects at the Apache Software Foundation.

| Platform version | Release | Specification | Java SE Support | Important Changes |
|---|---|---|---|---|
| Jakarta EE 11 | 2025-06-26 | 11 | Java SE 21Java SE 17 | Data |
| Jakarta EE 10 | 2022-09-22 | 10 | Java SE 17Java SE 11 | Removal of deprecated items in Servlet, Faces, CDI and EJB (Entity Beans and Embeddable Container). CDI-Build Time. |
| Jakarta EE 9.1 | 2021-05-25 | 9.1 | Java SE 11Java SE 8 | JDK 11 support |
| Jakarta EE 9 | 2020-12-08 | 9 | Java SE 8 | API namespace move from `javax` to `jakarta` |
| Jakarta EE 8 | 2019-09-10 | 8 | Java SE 8 | Full compatibility with Java EE 8 |
| Java EE 8 | 2017-08-31 | JSR 366 | Java SE 8 | HTTP/2 and CDI based Security |
| Java EE 7 | 2013-05-28 | JSR 342 | Java SE 7 | WebSocket, JSON and HTML5 support |
| Java EE 6 | 2009-12-10 | JSR 316 | Java SE 6 | CDI managed Beans and REST |
| Java EE 5 | 2006-05-11 | JSR 244 | Java SE 5 | Java annotations and Generics in Java |
| J2EE 1.4 | 2003-11-11 | JSR 151 | J2SE 1.4 | WS-I interoperable web services |
| J2EE 1.3 | 2001-09-24 | JSR 58 | J2SE 1.3 | Java connector architecture |
| J2EE 1.2 | 1999-12-17 | 1.2 | J2SE 1.2 | Initial specification release |

## Specifications

Jakarta EE includes several specifications that serve different purposes, like generating web pages, reading and writing from a database in a transactional way, and managing distributed queues.

The Jakarta EE APIs include several technologies that extend the functionality of the base Java SE APIs, such as Jakarta Enterprise Beans, connectors, servlets, Jakarta Server Pages and several web service technologies.

### Web specifications

- Jakarta Servlet: defines how to manage HTTP requests, in a synchronous or asynchronous way. It is low level and other Jakarta EE specifications rely on it;
- Jakarta WebSocket: API specification that defines a set of APIs to service WebSocket connections;
- Jakarta Faces: a technology for constructing user interfaces out of components;
- Jakarta Expression Language (*EL*) is a simple language originally designed to satisfy the specific needs of web application developers. It is used specifically in Jakarta Faces to bind components to (backing) beans and in Contexts and Dependency Injection to named beans, but can be used throughout the entire platform.

### Web service specifications

- Jakarta RESTful Web Services provides support in creating web services according to the Representational State Transfer (REST) architectural pattern;
- Jakarta JSON Processing is a set of specifications to manage information encoded in JSON format;
- Jakarta JSON Binding provides specifications to convert JSON information into or from Java classes;
- Jakarta XML Binding allows mapping XML into Java objects;
- Jakarta XML Web Services can be used to create SOAP web services.

### Enterprise specifications

- Jakarta Activation (*JAF*) specifies an architecture to extend component Beans by providing data typing and bindings of such types.
- Jakarta Contexts and Dependency Injection (*CDI*) is a specification to provide a dependency injection container;
- Jakarta Enterprise Beans (*EJB*) specification defines a set of lightweight APIs that an object container (the EJB container) will support in order to provide transactions (using JTA), remote procedure calls (using RMI or RMI-IIOP), concurrency control, dependency injection and access control for business objects. This package contains the Jakarta Enterprise Beans classes and interfaces that define the contracts between the enterprise bean and its clients and between the enterprise bean and the ejb container.
- Jakarta Persistence (*JPA*) are specifications about object-relational mapping between relation database tables and Java classes.
- Jakarta Transactions (*JTA*) contains the interfaces and annotations to interact with the transaction support offered by Jakarta EE. Even though this API abstracts from the really low-level details in implementing the X/Open XA standard, the interfaces are also considered somewhat low-level and the average application developer in Jakarta EE is either assumed to be relying on transparent handling of transactions by the higher level EJB abstractions, or using the annotations provided by this API in combination with CDI managed beans.
- Jakarta Messaging (*JMS*) provides a common way for Java programs to create, send, receive and read an enterprise messaging system's messages.

### Other specifications

- Jakarta Validation: This package contains the annotations and interfaces for the declarative validation support offered by the Jakarta Validation API. Jakarta Validation provides a unified way to provide constraints on beans (e.g. Jakarta Persistence model classes) that can be enforced cross-layer. In Jakarta EE, Jakarta Persistence honors bean validation constraints in the persistence layer, while JSF does so in the view layer.
- Jakarta Batch provides the means for batch processing in applications to run long running background tasks that possibly involve a large volume of data and which may need to be periodically executed.
- Jakarta Connectors is a Java-based tool for connecting application servers and enterprise information systems (*EIS*) as part of enterprise application integration (*EAI*). This is a low-level API aimed at vendors that the average application developer typically does not come in contact with.

## Web profile

In an attempt to limit the footprint of web containers, both in physical and in conceptual terms, the web profile was created, a subset of the Jakarta EE specifications. The Jakarta EE web profile comprises the following:

| Specification | Java EE 6 | Java EE 7 | Java EE 8 Jakarta EE 8 | Jakarta EE 9 Jakarta EE 9.1 | Jakarta EE 10 | Jakarta EE 11 |
|---|---|---|---|---|---|---|
| Jakarta Servlet | 3.0 | 3.1 | 4.0 | 5.0 | 6.0 | 6.1 |
| Jakarta Server Pages (*JSP*) | 2.2 | 2.3 | 2.3 | 3.0 | 3.1 | 4.0 |
| Jakarta Expression Language (*EL*) | 2.2 | 3.0 | 3.0 | 4.0 | 5.0 | 6.0 |
| Jakarta Debugging Support for Other Languages (JSR-45) | 1.0 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 |
| Jakarta Standard Tag Library (*JSTL*) | 1.2 | 1.2 | 1.2 | 2.0 | 3.0 | 3.0 |
| Jakarta Faces | 2.0 | 2.2 | 2.3 | 3.0 | 4.0 | 4.1 |
| Jakarta RESTful Web Services (*JAX-RS*) | 1.1 | 2.0 | 2.1 | 3.0 | 3.1 | 4.0 |
| Jakarta WebSocket (*WebSocket*) | —N/a | 1.0 | 1.1 | 2.0 | 2.1 | 2.2 |
| Jakarta JSON Processing (*JSON-P*) | —N/a | 1.0 | 1.1 | 2.0 | 2.1 | 2.1 |
| Jakarta JSON Binding (*JSON-B*) | —N/a | —N/a | 1.1 | 2.0 | 3.0 | 3.0 |
| Jakarta Annotations (*CA*) | 1.1 | 1.2 | 1.3 | 2.0 | 2.1 | 3.0 |
| Jakarta Enterprise Beans (*EJB*) | 3.1 Lite | 3.2 Lite | 3.2 Lite | 4.0 Lite | 4.0 Lite | 4.0 Lite |
| Jakarta Transactions (*JTA*) | 1.1 | 1.2 | 1.2 | 2.0 | 2.0 | 2.0 |
| Jakarta Persistence (*JPA*) | 2.0 | 2.1 | 2.2 | 3.0 | 3.1 | 3.2 |
| Jakarta Bean Validation | 1.0 | 1.1 | 2.0 | 3.0 | 3.0 | 3.1 |
| Jakarta Managed Beans | 1.0 | 1.0 | 1.0 | 2.0 | —N/a | N/a |
| Jakarta Interceptors | 1.1 | 1.2 | 1.2 | 2.0 | 2.1 | 2.2 |
| Jakarta Contexts and Dependency Injection (*CDI*) | 1.0 | 1.1 | 2.0 | 3.0 | 4.0 | 4.1 |
| Jakarta Dependency Injection | 1.0 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 |
| Jakarta Security | —N/a | —N/a | 1.0 | 2.0 | 3.0 | 4.0 |
| Jakarta Authentication | —N/a | 1.0 | 1.1 | 2.0 | 3.0 | 3.1 |
| Jakarta Concurrency | —N/a | —N/a | —N/a | —N/a | 3.0 | 3.1 |

## Certified referencing runtimes

Although by definition all Jakarta EE implementations provide the same base level of technologies (namely, the Jakarta EE spec and the associated APIs), they can differ considerably with respect to extra features (like connectors, clustering, fault tolerance, high availability, security, etc.), installed size, memory footprint, startup time, etc.

### Jakarta EE

| Referencing runtime | Developer | Jakarta EE 10 Platform | Jakarta EE 9/9.1 Platform Compatible Products | Jakarta EE 9/9.1 Web Profile Compatible Products | Jakarta EE 8 Platform Compatible Products | Jakarta EE 8 Web Profile Compatible Products | Licensing |
|---|---|---|---|---|---|---|---|
| GlassFish | Eclipse | Yes 7.0.0 | Yes 6.0.0/ 6.1.0 | Yes 6.0.0/ 6.1.0 | Yes 5.1.0 | Yes 5.1.0 | Free software |
| Open Liberty | IBM | Yes 22.0.0.13-beta, 23.0.0.3 | Yes 21.0.0.12 | Yes 21.0.0.12 | Yes 19.0.0.6, 20.0.0.3 | Yes 19.0.0.6, 20.0.0.3 | Free software |
| WebSphere Liberty | IBM | Yes 23.0.0.3 | Yes 21.0.0.12 | Yes 21.0.0.12 | Yes 20.0.0.3 | Yes 20.0.0.3 | Proprietary software |
| WildFly | Red Hat | Yes 27.0.0.Alpha5 | Yes 23.0.1-Preview/25.0.0-Preview | Yes 23.0.1-Preview/25.0.0-Preview | Yes 18.0.0 | Yes 18.0.0 | Free software |
| JBoss EAP | Red Hat | Yes 8.0.0 | No | No | Yes 7.3.0 | Yes 7.3.0 | Free software |
| TomEE | Apache | Yes 10.x | Yes 9.x | Yes 9.x | Yes 8.x | Yes 8.x | Free software |
| Payara Server | Payara Services Limited | Yes 6.2022.1 Alpha 4 | Yes 6.2021.1 Alpha 1 | No | Yes 5.22.0, 5.23.0 | Yes 5.23.0 | Free software |
| Thunisoft Application Server | Beijing Thunisoft Information Technology | No | Yes 3.0 | No | Yes 2.8 | No | Proprietary software |
| JEUS | TmaxSoft | No | No | No | Yes 8.5 | No | Proprietary software |
| InforSuite Application Server | Shandong Cvicse Middleware | No | Yes 11 | No | Yes 10 | No | Proprietary software |
| WebOTX | NEC | Yes 12 | No | No | Yes 11 | No | Proprietary software |

### Java EE

Referencing runtime

Developer

Java EE 8 certified – Full

Java EE 8 certified – Web

Java EE 7 certified – Full

Java EE 7 certified – Web

Java EE 6 certified – Full

Official Oracle page for Java EE Compatibility.

Java EE 6 certified – Web

Java EE 5 certified

J2EE 1.4 certified

Licensing

GlassFish

server Open Source Edition

Oracle

Yes v5.0

Yes v5.0

Yes v4.x

Yes v4.x

Yes v3.x and upward

Yes v3.x Web Profile

Yes v2.1.x

Free software

Oracle GlassFish Server

Oracle

Yes v3

based on the open source GlassFish application server

Yes

Sun Java System Application Server

v9.0

Yes

Sun Java System Application Server

v8.2

Proprietary software

Oracle WebLogic Server

Oracle

Yes 14.1.1

Yes 12.2.1

Yes v12c

Yes v10.3.5.0

Yes v9

Proprietary software

WildFly

Red Hat

Yes v14.x

Yes v14.x

Yes v8.1

Yes v8.0.0.Final

Yes v7.1

Yes v6.0

and v7.0

Yes v5.1

Yes v4.x

Free software

JBoss Enterprise Application Platform

Red Hat

Yes v7.2

Yes v7.0

Yes v7.0

Yes v6.0

Yes v5

Proprietary software

IBM WebSphere Application Server

IBM

Yes v9.x

Yes v9.x

Yes v8

Yes v7

Yes

Proprietary software

IBM WebSphere Application Server Liberty

IBM

Yes v18.0.0.2

Yes v18.0.0.2

Yes v8.5.5.6

Yes v8.5.5.6

Yes v8.5.5

Proprietary software

Open Liberty

IBM

Yes v18.0.0.2

Yes v18.0.0.2

Free software

IBM WebSphere Application Server Community Edition

IBM

Yes v3.0

Yes v2.1

Proprietary software

Apache Geronimo

Apache

Yes v3.0-beta-1

Yes v2.0

Yes v1.0

Free software

JEUS

TmaxSoft

Yes v8

Yes v7

Yes v6

Yes v5

Proprietary software

Cosminexus Application Server

Hitachi

Yes v10.0

Yes v9

Proprietary software

Fujitsu Interstage Application Server

Fujitsu

Yes v12.0

Yes v1 Azure/v10.1

Yes

Proprietary software

WebOTX

NEC

Yes

Yes

Proprietary software

BES Application Server

Baolande

Yes v9.5

Apache TomEE

Apache

No 7 (Java EE 7 like, but not certified

)

Yes

Free software

Resin Server

Caucho

Yes v4.0

Yes

Proprietary software

Siwpas

OW2

Yes v6.0

Free software

JOnAS

OW2

Yes v5.3 rc1

Yes

Yes

Free software

SAP NetWeaver

SAP

Yes v2.x

Yes

Yes

Proprietary software

Oracle Containers for Java EE

Oracle

Yes

Proprietary software

Oracle iPlanet Web Server

Oracle

Yes Sun Java System Web Server

Proprietary software

Oracle Application Server 10g

Oracle

Yes

Proprietary software

Pramati Server

Pramati Technologies

Yes v5.0

Proprietary software

Trifork T4

Trifork

Yes

Proprietary software

Sybase Enterprise Application Server

Sybase

Yes

Proprietary software

## Jakarta Mail

Jakarta Mail (formerly JavaMail) is a Jakarta EE API used to send and receive email via SMTP, POP3 and IMAP. Jakarta Mail is built into the Jakarta EE platform, but also provides an optional package for use in Java SE.

The current version is 2.1.3, released on February 29, 2024. Another open source Jakarta Mail implementation exists (GNU JavaMail), which -while supporting only the obsolete JavaMail 1.3 specification- provides the only free NNTP backend, which makes it possible to use this technology to read and send news group articles.

As of 2019, the software is known as Jakarta Mail, and is part of the *Jakarta EE* brand (formerly known as *Java EE*). The reference implementation is part of the Eclipse Angus project.

Maven coordinates of the relevant projects required for operation are:

- mail API: jakarta.mail:jakarta.mail-api:2.1.3
- mail implementation: org.eclipse.angus:angus-mail:2.0.3
- multimedia extensions: jakarta.activation:jakarta.activation-api:2.1.3

Jakarta Mail is hosted as an open source project on Eclipse.org under its new name *Jakarta Mail*.

Most of the Jakarta Mail source code is licensed under the following licences:

- EPL-2.0
- GPL-2.0 with Classpath Exception license
- The source code for the demo programs is licensed under the BSD license

## Code sample

The code sample shown below demonstrates how various technologies in Java EE 7 are used together to build a web form for editing a user.

In Jakarta EE a (web) UI can be built using Jakarta Servlet, Jakarta Server Pages (*JSP*), or Jakarta Faces (*JSF*) with Facelets. The example below uses Faces and Facelets. Not explicitly shown is that the input components use the Jakarta EE Bean Validation API under the covers to validate constraints.

```mw
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html" xmlns:f="http://xmlns.jcp.org/jsf/core">

    <f:metadata>
        <f:viewParam name="user_id" value="#{userEdit.user}" converter="#{userConvertor}" />
    </f:metadata>

    <h:body>

        <h:messages />

        <h:form>
            <h:panelGrid columns="2">
                <h:outputLabel for="firstName" value="First name" />
                <h:inputText id="firstName" value="#{userEdit.user.firstName}" label="First name" />

                <h:outputLabel for="lastName" value="Last name" />
                <h:inputText id="lastName" value="#{userEdit.user.lastName}" label="Last name" />

                <h:commandButton action="#{userEdit.saveUser}" value="Save" />
            </h:panelGrid>
        </h:form>

    </h:body>
</html>
```

### Example Backing Bean class

To assist the view, Jakarta EE uses a concept called a "Backing Bean". The example below uses Contexts and Dependency Injection (CDI) and Jakarta Enterprise Beans (*EJB*).

```mw
package org.wikipedia.examples;

import java.io.Serializable;

import jakarta.faces.view.ViewScoped;
import jakarta.inject.Inject;
import jakarta.inject.Named;

@Named
@ViewScoped
public class UserEdit implements Serializable {
    private static final long serialVersionUID = 1L;

    private User user;

    @Inject
    private UserDAO userDAO;

    public String saveUser() {
        userDAO.save(this.user);
        addFlashMessage(String.format("User %d saved", this.user.getId()));

        return "users.xhtml?faces-redirect=true";
    }

    public void setUser(User user) {
        this.user = user;
    }

    public User getUser() {
        return user;
    }
}
```

### Example Data Access Object class

To implement business logic, Jakarta Enterprise Beans (*EJB*) is the dedicated technology in Jakarta EE. For the actual persistence, JDBC or Jakarta Persistence (JPA) can be used. The example below uses EJB and JPA. Not explicitly shown is that JTA is used under the covers by EJB to control transactional behavior.

```mw
package org.wikipedia.examples;

import java.util.List;

import jakarta.ejb.Stateless;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.TypedQuery;

@Stateless
public class UserDAO {
    @PersistenceContext
    private EntityManager entityManager;

    public void save(User user) {
        entityManager.persist(user);
    }

    public void update(User user) {
        entityManager.merge(user);
    }

    public List<User> getAll() {
        return entityManager.createNamedQuery("User.getAll", User.class)
            .getResultList();
    }
}
```

### Example Entity class

For defining entity/model classes Jakarta EE provides the Jakarta Persistence (*JPA*), and for expressing constraints on those entities it provides the Bean Validation API. The example below uses both these technologies.

```mw
package org.wikipedia.examples;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = IDENTITY)
    private Integer id;

    @Size(min = 2, message="First name too short")
    private String firstName;

    @Size(min = 2, message="Last name too short")
    private String lastName;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}
```
