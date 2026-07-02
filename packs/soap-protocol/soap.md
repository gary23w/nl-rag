---
title: "SOAP"
source: https://en.wikipedia.org/wiki/SOAP
domain: soap-protocol
license: CC-BY-SA-4.0
tags: soap protocol, simple object access protocol, wsdl service, xml web service
fetched: 2026-07-02
---

# SOAP

**SOAP** (originally an acronym for **Simple Object Access Protocol**) is a messaging protocol specification for exchanging structured information in the implementation of web services in computer networks. It uses XML Information Set for its message format, and relies on application layer protocols, most often Hypertext Transfer Protocol (HTTP), although some legacy systems communicate over Simple Mail Transfer Protocol (SMTP), for message negotiation and transmission.

## Characteristics

SOAP provides the Messaging Protocol layer of a web services protocol stack for web services. It is an XML-based protocol consisting of three parts:

- an envelope, which defines the message structure and how to process it
- a set of encoding rules for expressing instances of application-defined datatypes
- a convention for representing procedure calls and responses

SOAP has three major characteristics:

1. *extensibility* (security and WS-Addressing are among the extensions under development)
2. *neutrality* (SOAP can operate over any protocol such as HTTP, SMTP, TCP, UDP)
3. *independence* (SOAP allows for any programming model)

As an example of what SOAP procedures can do, an application can send a SOAP request to a server that has web services enabled—such as a real-estate price database—with the parameters for a search. The server then returns a SOAP response (an XML-formatted document) with the resulting data, e.g., prices, location, features. Since the generated data comes in a standardized machine-parsable format, the requesting application can then integrate it directly.

The SOAP architecture consists of several layers of specifications for:

- message format
- Message Exchange Patterns (MEP)
- underlying transport protocol bindings
- message processing models
- protocol extensibility

SOAP evolved as a successor of XML-RPC, though it borrows its transport and interaction neutrality from Web Service Addressing and the envelope/header/body from elsewhere (probably from WDDX).

## History

SOAP was designed as an object-access protocol and released as XML-RPC in June 1998 as part of Frontier 5.1 by Dave Winer, Don Box, Bob Atkinson, and Mohsen Al-Ghosein for Microsoft, where Atkinson and Al-Ghosein were working. The specification was not made available until it was submitted to IETF 13 September 1999. According to Don Box, this was due to politics within Microsoft. Because of Microsoft's hesitation, Dave Winer shipped XML-RPC in 1998.

The submitted Internet Draft did not reach RFC status and is therefore not considered a "web standard" as such. Version 1.1 of the specification was published as a W3C Note on 8 May 2000. Since version 1.1 did not reach W3C Recommendation status, it can not be considered a "web standard" either. Version 1.2 of the specification, however, became a W3C recommendation on June 24, 2003. *SOAP* originally stood for "Simple Object Access Protocol" but version 1.2 of the standard dropped this acronym.

The SOAP specification was maintained by the XML Protocol Working Group of the World Wide Web Consortium until the group was closed 10 July 2009.

After SOAP was first introduced, it became the underlying layer of a more complex set of web services, based on WSDL, XSD and UDDI. These different services, especially UDDI, have proved to be of far less interest, but an appreciation of them gives a complete understanding of the expected role of SOAP compared to how web services have actually evolved.

## SOAP terminology

SOAP specification can be broadly defined to be consisting of the following three conceptual components: protocol concepts, encapsulation concepts and network concepts.

### Protocol concepts

**SOAP**

This is a set of rules formalizing and governing the format and processing rules for information exchanged between a SOAP sender and a SOAP receiver.

**SOAP nodes**

These are physical/logical machines with processing units which are used to transmit/forward, receive and process SOAP messages. These are analogous to

nodes

in a network.

**SOAP roles**

Over the path of a SOAP message, all nodes assume a specific role. The role of the node defines the action that the node performs on the message it receives. For example, a role "

none"

means that no node will process the SOAP header in any way and simply transmit the message along its path.

**SOAP protocol binding**

A SOAP message needs to work in conjunction with other protocols to be transferred over a network. For example, a SOAP message could use

TCP

as a lower layer protocol to transfer messages. These bindings are defined in the SOAP protocol binding framework.

**SOAP features**

SOAP provides a messaging framework only. However, it can be extended to add features such as reliability, security etc. There are rules to be followed when adding features to the SOAP framework.

**SOAP module**

A collection of specifications regarding the semantics of SOAP header to describe any new features being extended upon SOAP. A module needs to realize zero or more features. SOAP requires modules to adhere to prescribed rules.

### Data encapsulation concepts

**SOAP message**

Represents the information being exchanged between 2 SOAP nodes.

**SOAP envelope**

It is the enclosing element of an XML message identifying it as a SOAP message.

**SOAP header block**

A SOAP header can contain more than one of these blocks, each being a discrete computational block within the header. In general, the SOAP

role

information is used to target nodes on the path. A header block is said to be targeted at a SOAP node if the SOAP role for the header block is the name of a role in which the SOAP node operates. (ex: A SOAP header block with role attribute as

ultimateReceiver

is targeted only at the destination node which has this role. A header with a role attribute as

next

is targeted at each intermediary as well as the destination node.)

**SOAP header**

A collection of one or more header blocks targeted at each SOAP receiver.

**SOAP body**

Contains the body of the message intended for the SOAP receiver. The interpretation and processing of SOAP body is defined by header blocks.

**SOAP fault**

In case a SOAP node fails to process a SOAP message, it adds the fault information to the SOAP fault element. This element is contained within the SOAP body as a child element.

### Message sender and receiver concepts

**SOAP sender**

The node that transmits a SOAP message.

**SOAP receiver**

The node receiving a SOAP message. (Could be an intermediary or the destination node).

**SOAP message path**

The path consisting of all the nodes that the SOAP message traversed to reach the destination node.

**Initial SOAP sender**

This is the node which originated the SOAP message to be transmitted. This is the root of the SOAP message path.

**SOAP intermediary**

All the nodes in between the SOAP originator and the intended SOAP destination. It processes the SOAP header blocks targeted at it and acts to forward a SOAP message towards an ultimate SOAP receiver.

**Ultimate SOAP receiver**

The destination receiver of the SOAP message. This node is responsible for processing the message body and any header blocks targeted at it.

## Specification

The SOAP specification defines the messaging framework, which consists of:

- The *SOAP processing model*, defining the rules for processing a SOAP message
- The *SOAP extensibility model* defining the concepts of SOAP features and SOAP modules
- The *SOAP underlying protocol binding* framework describing the rules for defining a binding to an underlying protocol that can be used for exchanging SOAP messages between SOAP nodes
- The *SOAP message construct* defining the structure of a SOAP message

## SOAP building blocks

A SOAP message is an ordinary XML document containing the following elements:

| Element | Description | Required |
|---|---|---|
| Envelope | Identifies the XML document as a SOAP message. | Yes |
| Header | Contains header information. | No |
| Body | Contains call and response information. | Yes |
| Fault | Provides information about errors that occurred while processing the message. | No |

## Transport methods

Both SMTP and HTTP are valid application layer protocols used as transport for SOAP, but HTTP has gained wider acceptance as it works well with today's internet infrastructure; specifically, HTTP works well with network firewalls. SOAP may also be used over HTTPS (which is the same protocol as HTTP at the application level, but uses an encrypted transport protocol underneath) with either simple or mutual authentication; this is the advocated WS-I method to provide web service security as stated in the WS-I Basic Profile 1.1.

This is a major advantage over other distributed protocols like GIOP/IIOP or DCOM, which are normally filtered by firewalls. SOAP over AMQP is yet another possibility that some implementations support. SOAP also has an advantage over DCOM that it is unaffected by security rights configured on the machines that require knowledge of both transmitting and receiving nodes. This lets SOAP be loosely coupled in a way that is not possible with DCOM. There is also the SOAP-over-UDP OASIS standard.

## Message format

XML Information Set was chosen as the standard message format because of its widespread use by major corporations and open source development efforts. Typically, XML Information Set is serialized as XML. A wide variety of freely available tools significantly eases the transition to a SOAP-based implementation. The somewhat lengthy syntax of XML can be both a benefit and a drawback. While it facilitates error detection and avoids interoperability problems such as byte-order (endianness), it can slow processing speed and can be cumbersome. For example, CORBA, GIOP, ICE, and DCOM use much shorter, binary message formats. On the other hand, hardware appliances are available to accelerate processing of XML messages. Binary XML is also being explored as a means for streamlining the throughput requirements of XML. XML messages by their self-documenting nature usually have more 'overhead' (e.g., headers, nested tags, delimiters) than actual data in contrast to earlier protocols where the overhead was usually a relatively small percentage of the overall message.

In financial messaging SOAP was found to result in a 2–4 times larger message than previous protocols FIX (Financial Information Exchange) and CDR (Common Data Representation).

XML Information Set does not have to be serialized in XML. For instance, CSV and JSON XML-infoset representations exist. There is also no need to specify a generic transformation framework. The concept of SOAP bindings allows for specific bindings for a specific application. The drawback is that both the senders and receivers have to support this newly defined binding.

## Example message (encapsulated in HTTP)

The message below requests a stock price for AT&T (stock ticker symbol "T").

```mw
POST /InStock HTTP/1.1
Host: www.example.org
Content-Type: application/soap+xml; charset=utf-8
Content-Length: 299
SOAPAction: "http://www.w3.org/2003/05/soap-envelope"

<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://www.example.org">
  <soap:Header>
  </soap:Header>
  <soap:Body>
    <m:GetStockPrice>
      <m:StockName>T</m:StockName>
    </m:GetStockPrice>
  </soap:Body>
</soap:Envelope>
```

## Technical critique

### Advantages

- SOAP's neutrality characteristic explicitly makes it suitable for use with any transport protocol. Implementations often use HTTP as a transport protocol, but other popular transport protocols can be used. For example, SOAP can also be used over SMTP, JMS and message queues.
- SOAP, when combined with HTTP post/response exchanges, tunnels easily through existing firewalls and proxies, and consequently doesn't require modifying the widespread computing and communication infrastructures that exist for processing HTTP post/response exchanges.
- SOAP has available to it all the facilities of XML, including easy internationalization and extensibility with XML Namespaces.

### Disadvantages

- When using standard implementation and the default SOAP/HTTP binding, the XML infoset is serialized as XML. To improve performance for the special case of XML with embedded binary objects, the Message Transmission Optimization Mechanism was introduced.
- When relying on HTTP as a transport protocol and not using Web Services Addressing or an Enterprise Service Bus, the roles of the interacting parties are fixed. Only one party (the client) can use the services of the other.
- SOAP is less "simple" than the name would suggest. The verbosity of the protocol, low parsing speed of XML, and lack of a standardized interaction model led to the dominance of services using the HTTP protocol more directly. See, for example, REST.
- Being protocol-agnostic, SOAP is unable to take advantage of protocol-specific features and optimizations such as REST's Uniform Interface or caching – instead having to reimplement them (as with WS-Addressing).
