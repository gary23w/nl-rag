---
title: "Marshalling (computer science)"
source: https://en.wikipedia.org/wiki/Marshalling_(computer_science)
domain: xml-rpc
license: CC-BY-SA-4.0
tags: xml rpc, xml-rpc protocol, http remote procedure call, xml messaging
fetched: 2026-07-02
---

# Marshalling (computer science)

In computer science, **marshalling** or **marshaling** (US spelling) is the process of transforming the memory representation of an object into a data format suitable for storage or transmission, especially between different runtimes. It is typically used when data must be moved between different parts of a computer program or from one program to another.

Marshalling simplifies complex communications, because it allows using *composite objects* instead of being restricted to *primitive objects*.

## Comparison with serialization

Marshalling is sometimes used as synonymous with serializing, while serialization is actually one step in the process of marshalling an object.

- Marshalling is describing the overall intent or process to transfer some *live* object from a client to a server (with *client* and *server* taken as abstract, mirrored concepts mapping to any matching ends of an arbitrary communication link ie. sockets). The point with marshalling an object is to have that object that is present in one *running* program be present in another *running* program; that is, an object on the *client* should be transferred to the *server,* which is a form of reification allowing the object’s structure, data and state to transit from a runtime to another, leveraging an intermediate, serialized, "dry" representation (which is of second importance) circulating onto the communication socket.
- Serialization does not necessarily have this same intent, since it is only concerned about transforming data to generate that intermediate, "dry" representation of the object (for example, into a stream of bytes) which could then be either reified in a different runtime, or simply stored in a database, a file or in memory.

Marshalling and serialization might thus be done differently, although some form of serialization is usually used to do marshalling.

The term *deserialization* is somewhat similar to *un*-marshalling a dry object "on the server side", i.e., demarshalling (or unmarshalling) to get a live object back: the serialized object is transformed into an internal data structure, i.e., a live object within the target runtime. It usually corresponds to the exact inverse process of marshalling, although sometimes both ends of the process trigger specific business logic.

The accurate definition of marshalling differs across programming languages such as Python, Java, and .NET, and in some contexts, is used interchangeably with serialization.

## Marshalling in different programming languages

To "serialize" an object means to convert its state into a byte stream in such a way that the byte stream may be converted back into a copy of the object, which is unmarshalling in essence. Different programming languages either make or don’t make the distinction between the two concepts. A few examples:

In Python, the term "marshal" is used for a specific type of "serialization" in the Python standard library – storing internal python objects:

> The marshal module exists mainly to support reading and writing the "pseudo-compiled" code for Python modules of .pyc files.
> 
> …
> 
> If you’re serializing and de-serializing Python objects, use the `pickle` module instead

— The Python Standard Library

In the Java-related RFC 2713, marshalling is used when serializing objects for remote invocation. An object that is marshalled records the state of the original object and it contains the codebase (*codebase* here refers to a list of URLs where the object code can be loaded from, and not source code). Hence, in order to convert the object state and codebase(s), unmarshalling must be done. The unmarshaller interface automatically converts the marshalled data containing codebase(s) into an executable Java object in JAXB. Any object that can be deserialized can be unmarshalled. However, the converse need not be true.

> To "marshal" an object means to record its state and codebase(s) in such a way that when the marshalled object is "unmarshalled," a copy of the original object is obtained, possibly by automatically loading the class definitions of the object. You can marshal any object that is serializable or remote (that is, implements the `java.rmi.Remote` interface). Marshalling is like serialization, except marshalling also records codebases. Marshalling is different from serialization in that marshalling treats remote objects specially.
> 
> …
> 
> Any object whose methods can be invoked [on an object in another Java virtual machine] must implement the `java.rmi.Remote` interface. When such an object is invoked, its arguments are marshalled and sent from the local virtual machine to the remote one, where the arguments are unmarshalled and used.

— Schema for Representing Java Objects in an LDAP Directory (RFC 2713)

In .NET, marshalling is also used to refer to serialization when using remote calls:

> When you marshal an object by value, a copy of the object is created and serialized to the server. Any method calls made on that object are done on the server

— How To Marshal an Object to a Remote Server by Value by Using Visual Basic .NET (Q301116)

## Usage and examples

Marshalling is used within implementations of different remote procedure call (RPC) mechanisms, where it is necessary to transport data between processes and/or between threads.

In Microsoft's Component Object Model (COM), interface pointers must be marshalled when crossing COM apartment boundaries. In the .NET Framework, the conversion between an unmanaged type and a CLR type, as in the P/Invoke process, is also an example of an action that requires marshalling to take place.

Additionally, marshalling is used extensively within scripts and applications that use the XPCOM technologies provided within the Mozilla application framework. The Mozilla Firefox browser is a popular application built with this framework, that additionally allows scripting languages to use XPCOM through XPConnect (Cross-Platform Connect).

### Example

In the Microsoft Windows family of operating systems the entire set of device drivers for Direct3D are kernel-mode drivers. The user-mode portion of the API is handled by the DirectX runtime provided by Microsoft.

This is an issue because calling kernel-mode operations from user-mode requires performing a system call, and this inevitably forces the CPU to switch to "kernel mode". This is a slow operation, taking on the order of microseconds to complete. During this time, the CPU is unable to perform any operations. As such, minimizing the number of times this switching operation must be performed would optimize performance to a substantive degree.

Linux OpenGL drivers are split in two: a kernel-driver and a user-space driver. The user-space driver does all the translation of OpenGL commands into machine code to be submitted to the GPU. To reduce the number of system calls, the user-space driver implements marshalling. If the GPU's command buffer is full of rendering data, the API could simply store the requested rendering call in a temporary buffer and, when the command buffer is close to being empty, it can perform a switch to kernel-mode and add a number of stored commands all at once.

## Formats

Marshalling data requires some kind of data transfer, which leverages a specific data format to be chosen as the serialization target.

### XML vs JSON vs…

XML is one such format and means of transferring data between systems. Microsoft, for example, uses it as the basis of the file formats of the various components (Word, Excel, Access, PowerPoint, etc.) of the Microsoft Office suite (see Office Open XML).

While this typically results in a verbose wire format, XML's fully-bracketed "start-tag", "end-tag" syntax allows provision of more accurate diagnostics and easier recovery from transmission or disk errors. In addition, because the tags occur repeatedly, one can use standard compression methods to shrink the content—all the Office file formats are created by zipping the raw XML. Alternative formats such as JSON (JavaScript Object Notation) are more concise, but correspondingly less robust for error recovery.

Once the data is transferred to a program or an application, it needs to be converted back to an object for usage. Hence, unmarshalling is generally used in the receiver end of the implementations of Remote Method Invocation (RMI) and Remote procedure call (RPC) mechanisms to unmarshal transmitted objects in an executable form.

### JAXB

JAXB or Java Architecture for XML Binding is the most common framework used by developers to marshal and unmarshal Java objects. JAXB provides for the interconversion between fundamental data types supported by Java and standard XML schema data types.

### `XmlSerializer`

`System.Xml.Serialization.XmlSerializer` is the framework used by C# developers to marshal and unmarshal C# objects. One of the advantages of C# over Java is that C# natively supports marshalling due to the inclusion of `System.Xml.Serialization.XmlSerializer` class. Java, on the other hand requires a non-native glue code in the form of JAXB to support marshalling.

### From XML to an executable representation

An example of unmarshalling is the conversion of an XML representation of an object to the default representation of the object in any programming language. Consider the following class:

```mw
public class Student {
    private String name;
    private int id;

    public String getName() {
        return this.name;
    }

    public int getId() {
        return this.id;
    }

    void setName(String name) {
        this.name = name;
    }

    void setId(int id) {
        this.id = id;
    }
}
```

- XML representation of a specific `Student` object:

```mw
<?xml version="1.0" encoding="UTF-8"?>
    <student id="11235813">
        <name>Alice</name>
    </student>
    <student id="21345589">
        <name>Bob</name>
    </student>
```

- Executable representation of that `Student` object:

```mw
Student s1 = new Student();
s1.setId(11235813);
s1.setName("Alice");
Student s2 = new Student();
s2.setId(21345589);
s2.setName("Bob");
```

Unmarshalling is the process of converting the XML representation to the default executable Java representation, and running that very code to get a consistent, live object back. Had a different format been chosen, the unmarshalling process would have been different, but the end result in the target runtime would be the same.

## Unmarshalling in Java

### Unmarshaller in JAXB

The process of unmarshalling XML data into an executable Java object is taken care of by the in-built `jakarta.xml.bind.Unmarshaller` (formally `javax.xml.bind.Unmarshaller`) class. The unmarshal methods defined in the `jakarta.xml.bind.Unmarshaller` class are overloaded to accept XML from different types of input such as a `java.io.File`, `java.io.FileInputStream`, or `java.net.URL`. For example:

```mw
import java.io.File;
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Unmarshaller;

JAXBContext jcon = JAXBContext.newInstance("com.acme.foo");
Unmarshaller umar = jcon.createUnmarshaller();
Object obj = umar.unmarshal(new File("input.xml"));
```

### Unmarshalling XML Data

Unmarshal methods can deserialize an entire XML document or a small part of it. When the XML root element is globally declared, these methods utilize the `jakarta.xml.bind.JAXBContext`'s mapping of XML root elements to JAXB mapped classes to initiate the unmarshalling. If the mappings are not sufficient and the root elements are declared locally, the unmarshal methods use `declaredType` methods for the unmarshalling process. These two approaches can be understood below.

#### Unmarshal a global XML root element

The unmarshal method uses `jakarta.xml.bind.JAXBContext` (formerly `javax.xml.bind.JAXBContext`) to unmarshal the XML data, when the root element is globally declared. The `jakarta.xml.bind.JAXBContext` object always maintains a mapping of the globally declared XML element and its name to a JAXB mapped class. If the XML element name or its `@xsi:type` attribute matches the JAXB mapped class, the unmarshal method transforms the XML data using the appropriate JAXB mapped class. However, if the XML element name has no match, the unmarshal process will abort and throw an `jakarta.xml.bind.UnmarshalException` (formerly `javax.xml.bind.UnmarshalException`). This can be avoided by using the unmarshal by `declaredType` methods.

#### Unmarshal a local XML root element

When the root element is not declared globally, the application assists the unmarshaller by application-provided mapping using `declaredType` parameters. By an order of precedence, even if the root name has a mapping to an appropriate JAXB class, the `declaredType` overrides the mapping. However, if the `@xsi:type` attribute of the XML data has a mapping to an appropriate JAXB class, then this takes precedence over declaredType parameter. The unmarshal methods by `declaredType` parameters always return a `jakarta.xml.bind.JAXBElement<T>` instance. The properties of this `jakarta.xml.bind.JAXBElement<T>` instance are set as follows:

| `jakarta.xml.bind.JAXBElement` property | Value |
|---|---|
| `name` | *xml element name* |
| `value` | `instanceof declaredType` |
| `declaredType` | unmarshal method `declaredType` parameter |
| `scope` | `null` (actual size is not known) |
