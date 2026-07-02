---
title: "Data transfer object"
source: https://en.wikipedia.org/wiki/Data_transfer_object
domain: automapper-dotnet-lib
license: CC-BY-SA-4.0
tags: automapper mapping, dotnet object mapping, automapper dto, automapper profile config
fetched: 2026-07-02
---

# Data transfer object

In the field of programming a **data transfer object** (**DTO**) is an object that carries data between processes. The motivation for its use is that communication between processes is usually done resorting to remote interfaces (e.g., web services), where each call is an expensive operation. Because the majority of the cost of each call is related to the round-trip time between the client and the server, one way of reducing the number of calls is to use an object (the DTO) that aggregates the data that would have been transferred by the several calls, but that is served by one call only.

The difference between data transfer objects and business objects or data access objects is that a DTO does not have any behavior except for storage, retrieval, serialization and deserialization of its own data (mutators, accessors, serializers and parsers). In other words, DTOs are simple objects that should not contain any business logic but may contain serialization and deserialization mechanisms for transferring data over the wire.

This pattern is often incorrectly used outside of remote interfaces. This has triggered a response from its author where he reiterates that the whole purpose of DTOs is to shift data in expensive remote calls.

## Terminology

A value object is not a DTO. The two terms have been conflated by Sun/Java community in the past.

For the model–view–viewmodel pattern, the data transfer object can be referred to as the viewmodel.
