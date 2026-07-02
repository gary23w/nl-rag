---
title: "XML-RPC"
source: https://en.wikipedia.org/wiki/XML-RPC
domain: xml-rpc
license: CC-BY-SA-4.0
tags: xml rpc, xml-rpc protocol, http remote procedure call, xml messaging
fetched: 2026-07-02
---

# XML-RPC

**XML-RPC** is a remote procedure call (RPC) protocol which uses XML to encode its calls and HTTP as a transport mechanism.

## History

The XML-RPC protocol was created in 1998 by Dave Winer of UserLand Software and Microsoft, with Microsoft seeing the protocol as an essential part of scaling up its efforts in business-to-business e-commerce. As new functionality was introduced, the standard evolved into what is now SOAP.

UserLand supported XML-RPC from version 5.1 of its Frontier web content management system, released in June 1998.

XML-RPC's idea of a human-readable-and-writable, script-parsable standard for HTTP-based requests and responses has also been implemented in competing specifications such as Allaire's Web Distributed Data Exchange (WDDX) and webMethod's Web Interface Definition Language (WIDL). Prior art wrapping COM, CORBA, and Java RMI objects in XML syntax and transporting them via HTTP also existed in DataChannel's WebBroker technology.

The generic use of XML for remote procedure call (RPC) was patented by Phillip Merrick, Stewart Allen, and Joseph Lapp in April 2006, claiming benefit to a provisional application filed in March 1998. The patent was assigned to webMethods, located in Fairfax, Virginia. The patent expired on March 23, 2019.

## Usage

In XML-RPC, a client performs an RPC by sending an HTTP request to a server that implements XML-RPC and receives the HTTP response. A call can have multiple parameters and one result. The protocol defines a few data types for the parameters and result. Some of these data types are complex, i.e. nested. For example, you can have a parameter that is an array of five integers.

The parameters/result structure and the set of data types are meant to mirror those used in common programming languages.

*Identification* of clients for authorization purposes can be achieved using popular HTTP security methods. Basic access authentication can be used for identification and authentication.

In comparison to RESTful protocols, where *resource representations* (documents) are transferred, XML-RPC is designed to *call methods*. The practical difference is just that XML-RPC is much more structured, which means common library code can be used to implement clients and servers and there is less design and documentation work for a specific application protocol. One salient technical difference between typical RESTful protocols and XML-RPC is that many RESTful protocols use the HTTP URI for parameter information, whereas with XML-RPC, the URI just identifies the server.

JSON-RPC is similar to XML-RPC.

## Data types

Common datatypes are converted into their XML equivalents with example values shown below:

| Name | Tag Example | Description |   |
|---|---|---|---|
| array | <array> <data> <value><i4>1404</i4></value> <value><string>Something here</string></value> <value><i4>1</i4></value> </data> </array> | Array of values, storing no keys |   |
| base64 | <base64>eW91IGNhbid0IHJlYWQgdGhpcyE=</base64> | Base64-encoded binary data |   |
| boolean | <boolean>1</boolean> | Boolean logical value (0 or 1) |   |
| date/time | <dateTime.iso8601>19980717T14:08:55Z</dateTime.iso8601> | Date and time in ISO 8601 format |   |
| double | <double>-12.53</double> | Double precision floating point number |   |
| integer | <int>42</int> or <i4>42</i4> | Signed integer coded on 4 bytes |   |
| string | <string>Hello world!</string> or Hello world! | String of characters. Must follow XML encoding. |   |
| struct | <struct> <member> <name>foo</name> <value><i4>1</i4></value> </member> <member> <name>bar</name> <value><i4>2</i4></value> </member> </struct> | Associative array |   |
| nil | <nil/> | Discriminated null value; an XML-RPC extension |   |
| long | <i8>1312</i8> | Signed integer coded on 8 bytes. This is not part of the specification, but it is supported by several XML-RPC implementations **·** |   |

## Examples

An example of a typical XML-RPC request would be:

```mw
<?xml version="1.0"?>
<methodCall>
  <methodName>examples.getStateName</methodName>
  <params>
    <param>
        <value><i4>40</i4></value>
    </param>
  </params>
</methodCall>
```

An example of a typical XML-RPC response would be:

```mw
<?xml version="1.0"?>
<methodResponse>
  <params>
    <param>
        <value><string>South Dakota</string></value>
    </param>
  </params>
</methodResponse>
```

A typical XML-RPC fault would be:

```mw
<?xml version="1.0"?>
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value><int>4</int></value>
        </member>
        <member>
          <name>faultString</name>
          <value><string>Too many parameters.</string></value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>
```

## Criticism

Recent critics (from 2010 and onwards) of XML-RPC argue that RPC calls can be made with plain XML, and that XML-RPC does not add any value over XML. Both XML-RPC and XML require an application-level data model, such as which field names are defined in the XML schema or the parameter names in XML-RPC. Furthermore, XML-RPC uses about 4 times the number of bytes compared to plain XML to encode the same objects, which is itself verbose compared to JSON.
