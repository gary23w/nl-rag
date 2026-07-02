---
title: "Remote procedure call"
source: https://en.wikipedia.org/wiki/Remote_procedure_call
domain: soap-protocol
license: CC-BY-SA-4.0
tags: soap protocol, simple object access protocol, wsdl service, xml web service
fetched: 2026-07-02
---

# Remote procedure call

In distributed computing, a **remote procedure call** (**RPC**) is an action in which a computer program causes a procedure (subroutine) to execute in a different address space of the current process (commonly on another computer on a shared computer network), which is written as if it were a normal (local) procedure call, without the programmer explicitly writing the details for the remote interaction. That is, the programmer writes essentially the same code whether the subroutine is local to the executing program, or remote. This is a form of server interaction (caller is client, executor is server), typically implemented via a request–response message passing system. In the object-oriented programming paradigm, RPCs are represented by remote method invocation (RMI). The RPC model implies a level of location transparency, namely that calling procedures are largely the same whether they are local or remote, but usually, they are not identical, so local calls can be distinguished from remote calls. Remote calls are usually orders of magnitude slower and less reliable than local calls, so distinguishing them is important.

RPCs are a form of inter-process communication (IPC), in that different processes have different address spaces: if on the same host machine, they have distinct virtual address spaces, even though the physical address space is the same; while if they are on different hosts, the physical address space is also different. Many different (often incompatible) technologies have been used to implement the concept. Modern RPC frameworks, such as gRPC and Apache Thrift, enhance the basic RPC model by using efficient binary serialization (e.g., Protocol Buffers), HTTP/2 multiplexing, and built-in support for features such as authentication, load balancing, streaming, and error handling, making them well-suited for building scalable microservices and enabling language interoperability.

## History and origins

Request–response protocols date to early distributed computing in the late 1960s, theoretical proposals of remote procedure calls as the model of network operations date to the 1970s, and practical implementations date to the early 1980s. Bruce Jay Nelson is generally credited with coining the term "remote procedure call" in 1981.

Remote procedure calls used in modern operating systems trace their roots back to the RC 4000 multiprogramming system, which used a request-response communication protocol for process synchronization. The idea of treating network operations as remote procedure calls goes back at least to the 1970s in early ARPANET documents. In 1978, Per Brinch Hansen proposed Distributed Processes, a language for distributed computing based on "external requests" consisting of procedure calls between processes.

One of the earliest practical implementations was in 1982 by Brian Randell and colleagues for their Newcastle Connection between UNIX machines. This was soon followed by "Lupine" by Andrew Birrell and Bruce Nelson in the Cedar environment at Xerox PARC. Lupine automatically generated stubs, providing type-safe bindings, and used an efficient protocol for communication. One of the first business uses of RPC was by Xerox under the name "Courier" in 1981. The first popular implementation of RPC on Unix was Sun's RPC (now called ONC RPC), used as the basis for Network File System (NFS).

In the 1990s, with the popularity of object-oriented programming, an alternative model of remote method invocation (RMI) was widely implemented, such as in Common Object Request Broker Architecture (CORBA, 1991) and Java remote method invocation. RMIs, in turn, fell in popularity with the rise of the internet, particularly in the 2000s.

## Message passing

RPC is a request–response protocol. An RPC is initiated by the *client*, which sends a request message to a known remote *server* to execute a specified procedure with supplied parameters. The remote server sends a response to the client, and the application continues its process. While the server is processing the call, the client is blocked (it waits until the server has finished processing before resuming execution), unless the client sends an asynchronous request to the server, such as an XMLHttpRequest. There are many variations and subtleties in various implementations, resulting in a variety of different (incompatible) RPC protocols.

An important difference between remote procedure calls and local calls is that remote calls can fail because of unpredictable network problems. Also, callers generally must deal with such failures without knowing whether the remote procedure was actually invoked. Idempotent procedures (those that have no additional effects if called more than once) are easily handled, but enough difficulties remain that code to call remote procedures is often confined to carefully written low-level subsystems.

### Sequence of events

1. The client calls the client stub. The call is a local procedure call, with parameters pushed on to the stack in the normal way.
2. The client stub packs the parameters into a message and makes a system call to send the message. Packing the parameters is called marshalling.
3. The client's local operating system sends the message from the client machine to the server machine.
4. The local operating system on the server machine passes the incoming packets to the server stub.
5. The server stub unpacks the parameters from the message. Unpacking the parameters is called unmarshalling.
6. Finally, the server stub calls the server procedure. The reply traces the same steps in the reverse direction.

## Standard contact mechanisms

To let different clients access servers, a number of standardized RPC systems have been created. Most of these use an interface description language (IDL) to let various platforms call the RPC. The IDL files can then be used to generate code to interface between the client and servers.

## Analogues

Notable RPC implementations and analogues include:

### Language-specific

- Java's Remote Method Invocation (Java RMI) API provides similar functionality to standard Unix RPC methods.
- Go provides a package rpc for implementing RPC, with support for asynchronous calls.
- Modula-3's network objects, which were the basis for Java's RMI
- RPyC implements RPC mechanisms in Python, with support for asynchronous calls.
- Distributed Ruby (DRb) allows Ruby programs to communicate with each other on the same machine or over a network. DRb uses remote method invocation (RMI) to pass commands and data between processes.
- Erlang is process-oriented and natively supports distribution and RPCs via message passing between nodes and local processes alike.
- Elixir builds on top of the Erlang. It allows process communication (Elixir/Erlang processes, not OS processes) of the same network out of the box via Agents and message passing.
- Google's Rust RPC framework Tarpc lets developers define the structure of messages using Rust's structs and traits, rather than using protobuf.

### Application-specific

- Action Message Format (AMF) allows Adobe Flex applications to communicate with back-ends or other applications that support AMF.
- Remote Function Call is the standard SAP interface for communication between SAP systems. RFC calls a function to be executed in a remote system.

### General

- NFS (Network File System) is one of the most prominent users of RPC
- Open Network Computing RPC, by Sun Microsystems (also known as Sun RPC)
- D-Bus open source IPC program provides similar function to CORBA.
- SORCER provides the API and exertion-oriented language (EOL) for a federated method invocation
- XML-RPC is an RPC protocol that uses XML to encode its calls and HTTP as a transport mechanism.
- JSON-RPC is an RPC protocol that uses JSON-encoded messages.
- JSON-WSP is an RPC protocol that is inspired from JSON-RPC.
- SOAP is a successor of XML-RPC and also uses XML to encode its HTTP-based calls.
- ZeroC's Internet Communications Engine (Ice) distributed computing platform.
- Etch framework for building network services.
- Apache Thrift protocol and framework.
- CORBA provides remote procedure invocation through an intermediate layer called the *object request broker*.
- Libevent provides a framework for creating RPC servers and clients.
- Windows Communication Foundation is an application programming interface in the .NET framework for building connected, service-oriented applications.
- Microsoft .NET Remoting offers RPC facilities for distributed systems implemented on the Windows platform. It has been superseded by WCF.
- The Microsoft DCOM uses MSRPC which is based on DCE/RPC
- The Open Software Foundation DCE/RPC Distributed Computing Environment (also implemented by Microsoft).
- Google Protocol Buffers (protobufs) package includes an interface definition language used for its RPC protocols open sourced in 2015 as gRPC.
- WAMP combines RPC and Publish-Subscribe into a single, transport-agnostic protocol.
- Google Web Toolkit uses an asynchronous RPC to communicate to the server service.
- Apache Avro provides RPC where client and server exchange schemas in the connection handshake and code generation is not required.
