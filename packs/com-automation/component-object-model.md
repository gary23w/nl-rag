---
title: "Component Object Model"
source: https://en.wikipedia.org/wiki/Component_Object_Model
domain: com-automation
license: CC-BY-SA-4.0
tags: component object model, ole automation, distributed com, activex control
fetched: 2026-07-02
---

# Component Object Model

**Component Object Model** (**COM**) is a binary-interface technology for software components from Microsoft that enables using objects in a language-neutral way between different programming languages, programming contexts, processes and machines.

COM is the basis for other Microsoft domain-specific component technologies including OLE, OLE Automation, ActiveX, COM+, and DCOM as well as implementations such as DirectX, Windows shell, UMDF, Windows Runtime, and Browser Helper Object.

COM enables object use when only the object's interface is known, not its internal implementation. The component implementer defines interfaces that are separate from the implementation.

Support for multiple programming contexts is handled by relying on the object for aspects that would be challenging to implement as a facility. Supporting multiple uses of an object is handled by requiring each object to destroy itself via reference-counting. Access to an object's interfaces (similar to Type conversion) is provided by each object as well.

COM is available only in Microsoft Windows and Apple's Core Foundation 1.3 and later plug-in application programming interface (API). The latter only implements a subset of the whole COM interface.

Over time, COM is being replaced with other technologies such as Microsoft .NET and web services (i.e. via WCF). However, COM objects can be used in a .NET language via COM Interop.

COM is similar to other component technologies such as SOM, CORBA and Enterprise JavaBeans, although each has its strengths and weaknesses.

Unlike C++, COM provides a stable application binary interface (ABI) that is unaffected by compiler differences. This makes using COM advantageous for object-oriented C++ libraries that are to be used by clients compiled via different compilers.

## History

Introduced in 1987, Dynamic Data Exchange (DDE) was one of the first interprocess communication technologies in Windows. It allowed sending and receiving messages in so-called *conversations* between applications.

Tony Williams, involved in architecting COM, distributed two papers within Microsoft that embraced the concept of software components: *Object Architecture: Dealing With the Unknown – or – Type Safety in a Dynamically Extensible Class Library* in 1988 and *On Inheritance: What It Means and How To Use It* in 1990. These provided the foundation of many of the ideas behind COM.

Object Linking and Embedding (OLE), Microsoft's first object-based framework, was built on DDE and designed specifically for compound documents. It was introduced with Word and Excel in 1991, and was later included with Windows, starting with version 3.1 in 1992. An example of a compound document is a spreadsheet embedded in a Word document. As changes are made to the spreadsheet in Excel, they appear automatically in the Word document.

In 1991, Microsoft introduced the Visual Basic Extension (VBX) technology with Visual Basic 1.0. A VBX is a packaged extension in the form of a dynamic-link library (DLL) that allows objects to be graphically placed in a form and manipulated by properties and methods. These were later adapted for use by other languages such as Visual C++. Windows 3.1 integrated OLE 1.0.

In 1992, Microsoft released OLE 2 with its new underlying object model, COM. The COM application binary interface (ABI) was the same as the MAPI ABI (released in 1992), and like it was based on MSRPC and ultimately on the Open Group's DCE/RPC. COM was created to replace DDE since its text-based conversation and Windows messaging design was not flexible enough to allow sharing application features in a robust and extensible way. The COM introduced UUID as identifier.

In 1994, the OLE custom control (OCX) technology, based on COM, was introduced as the successor to VBX. At the same time, Microsoft stated that OLE 2 would be known simply as "OLE". Windows NT 3.5 and Windows 95 integrated OLE 2.0.

In early 1996, Microsoft found a new use for OCX – extending their web browser's capability. Microsoft renamed some parts of OLE relating to the Internet as ActiveX, and gradually renamed all OLE technologies to ActiveX, except the compound document technology that was used in Microsoft Office.

Later in 1996, Microsoft extended COM to work across the network with DCOM.

In 1997, Windows CE integrated support for COM.

### MSRPC

The COM IDL is based on the feature-rich DCE/RPC IDL, with object-oriented extensions. Microsoft's implementation of DCE/RPC, **MSRPC**, is used as the primary inter-process communication mechanism for Windows NT services and internal components, making it an obvious choice of foundation.

### DCOM

DCOM extends COM from merely supporting a single user with separate applications communicating on the Windows desktop, to activating objects running under different security contexts, and on different machines across the network. With this were added necessary features for configuring which users have authority to create, activate and call objects, for identifying the calling user, as well as specifying required encryption for security of calls.

### COM+

Microsoft introduced Microsoft Transaction Server (MTS) in Windows NT 4 in order to provide developers with support for distributed transactions, resource pooling, disconnected applications, event publication and subscription, better memory and processor (thread) management, as well as to position Windows as an alternative to other enterprise-level operating systems.

Renamed to **COM+** in Windows 2000, the feature set was incorporated into the operating system as opposed to the series of external tools provided by MTS. At the same time, Microsoft de-emphasized DCOM as a separate entity. Components that used COM+ were handled more directly by the added layer of COM+, in particular by operating system support for interception. In the first release of MTS, interception was tacked on – installing an MTS component would modify the Windows Registry to call the MTS software, and not the component directly.

Windows 2000 included Component Services control panel updates for configuring COM+ components.

An advantage of COM+ was that it could be run in "component farms". Instances of a component, if coded properly, could be pooled and reused by new calls to its initializing routine without unloading it from memory. Components could also be distributed (called from another machine). COM+ and Microsoft Visual Studio provided tools to make it easy to generate client-side proxies, so although DCOM was used to make the remote call, it was easy to do for developers. COM+ also introduced a subscriber/publisher event mechanism called **COM+ Events**, and provided a new way of leveraging MSMQ (a technology that provides inter-application asynchronous messaging) with components called **Queued Components**. COM+ events extend the COM+ programming model to support late-bound (see Late binding) events or method calls between the publisher or subscriber and the event system.

### .NET

**.NET** is Microsoft's component technology that supersedes COM. .NET hides many details of component creation and therefore eases development.

.NET provides wrappers to commonly used COM controls.

.NET can leverage COM+ via the `System.EnterpriseServices` namespace, and several of the services that COM+ provides have been duplicated in .NET. For example, the `System.Transactions` namespace provides the `TransactionScope` class, which provides transaction management without resorting to COM+. Similarly, queued components can be replaced by Windows Communication Foundation (WCF) with an MSMQ transport.

There is limited support for backward compatibility. A COM object may be used in .NET by implementing a Runtime Callable Wrapper (RCW). NET objects that conform to certain interface restrictions may be used in COM objects by calling a *COM callable wrapper* (CCW). From both the COM and .NET sides, objects using the other technology appear as native objects. See COM Interop.

WCF eases a number of COM's remote execution challenges. For instance, it allows objects to be transparently marshalled by value across process or machine boundaries more easily.

### Windows Runtime

**Windows Runtime** (**WinRT**) is a COM-based API, albeit an enhanced COM variant. Because of its COM-like basis, WinRT supports interfacing from multiple programming contexts, but it is an unmanaged, native API. The API definitions are stored in ".winmd" files, which are encoded in ECMA 335 metadata format, the same CLI metadata format that .NET uses with a few modifications. This metadata format allows for significantly lower overhead than P/Invoke when WinRT is invoked from .NET applications.

### Nano-COM

**Nano-COM** is a subset of COM focused on the application binary interface (ABI) aspects of COM that enable function and method calls across independently compiled modules/components. Nano-COM can be expressed in a portable C++ header file. Nano-COM extends the native ABI of the underlying instruction architecture and OS to support typed object references – whereas a typical ABI focuses on atomic types, structures, arrays and function calling conventions.

A Nano-COM header file defines or names at least three types:

- GUID – identifies an interface type

- HRESULT – method result codes such as S_OK, E_FAIL, E_OUTOFMEMORY

- IUnknown – base type for object references; abstract virtual functions to support `dynamic_cast<T>`-style acquisition of new interface types and ref counting a la `shared_ptr<T>`

Many uses of Nano-COM define two functions to address callee-allocated memory buffers as results:

- <NanoCom>Alloc – called by method implementations to allocate raw buffers (not objects) that are returned to the caller

- <NanoCom>Free – called by method callers to free callee-allocated buffers when no longer in use

Some implementations of Nano-COM such as Direct3D eschew the allocator functions and restrict themselves to only use caller-allocated buffers.

Nano-COM has no notion of classes, apartments, marshaling, registration, etc. Rather, object references are simply passed across function boundaries and allocated via standard language constructs (e.g., C++ `new` operator).

Nano-COM is currently in use as the base ABI technology for DirectX/Direct3D/DirectML.

## Security

### In Internet Explorer

Since an ActiveX control (any COM component) runs as native code, with no sandboxing protection, there are few restrictions on what it can do. Using ActiveX components, as Internet Explorer supported, in a web page lead to problems with malware infections. Microsoft recognized the problem as far back as 1996 when Charles Fitzgerald said, "We never made the claim up front that ActiveX is intrinsically secure". Later versions of Internet Explorer prompt the user before installing an ActiveX control, allowing them to block installation.

As a level of protection, an ActiveX control is signed with a digital signature to guarantee authenticity.

It is also possible to disable ActiveX controls altogether, or to allow only a selected few.

### Process corruption

The transparent support for out-of-process COM servers promotes software safety in terms of process isolation. This can be useful for decoupling subsystems of large application into separate processes. Process isolation limits state corruption in one process from negatively affecting the integrity of the other processes, since they only communicate through strictly defined interfaces. Thus, only the affected subsystem needs to be restarted in order to regain valid state. This is not the case for subsystems within the same process, where a *rogue pointer* in one subsystem can randomly corrupt other subsystems.

## Binding

COM is supported via bindings in several languages, such as C, C++, Visual Basic, Delphi, Python and several of the Windows scripting contexts. Component access is via interface methods. This allows for direct calling in-process and via the COM/DCOM sub-system access between processes and computers.

## Type system

### Coclass

A **coclass**, a COM class, implements one or more interfaces. It is identified by a class ID, called CLSID which is GUID, and by a human-readable programmatic identifier, called ProgID. A coclass is created via one of these identifiers.

### Interface

Each COM **interface** extends the `IUnknown` interface, which exposes methods for reference counting and for accessing the other interfaces of the object – similar to type conversion, a.k.a. type casting.

An interface is identified by an interface ID (IID), a GUID.

A **custom interface**, anything derived from `IUnknown`, provides early bound access via a pointer to a virtual method table that contains a list of pointers to the functions that implement the functions declared in the interface, in the order they are declared. An in-process invocation overhead is, therefore, comparable to a C++ virtual method call.

Dispatching, a.k.a. late bound access, is provided by implementing `IDispatch`. Dispatching allows access from a wider range of programming contexts than a custom interface.

Like many object-oriented languages, COM provides a separation of interface from implementation. This distinction is especially strong in COM where an object has no default interface. A client must request an interface to have any access. COM supports multiple implementations of the same interface, so that clients can choose which implementation of an interface to use.

### Type library

A COM **type library** defines COM metadata, such as coclasses and interfaces. A library can be defined as Interface definition language (IDL); a programming language independent syntax. IDL is similar to C++ with additional syntax for defining interfaces and coclasses. IDL also supports bracketed attributes before declarations to define metadata such as identifiers and relationships between parameters.

An IDL file is compiled via the MIDL compiler. For use with C/C++, the MIDL compiler generates a header file with `struct` definitions to match the vtbls of the declared interfaces and a C file containing declarations of the interface GUIDs. C++ source code for a proxy module can also be generated by the MIDL compiler. This proxy contains method stubs for converting COM calls into remote procedure calls to enable DCOM for out-of-process communication.

MIDL can generate a binary type library (TLB) that can be used by other tools to support access from other context.

### Examples

The following IDL code declares a coclass named SomeClass which implements an interface named ISomeInterface.

```mw
coclass SomeClass {
  [default] interface ISomeInterface;
};
```

This is conceptually equivalent to the following C++ code where ISomeInterface is a pure virtual class, a.k.a. abstract base class.

```mw
class ISomeInterface {};
class SomeClass : public ISomeInterface {
};
```

In C++, COM objects are instantiated via the COM subsystem CoCreateInstance function that takes the CLSID and IID. SomeClass can be created as follows:

```mw
ISomeInterface* interface_ptr = NULL;
HRESULT hr = CoCreateInstance(CLSID_SomeClass, NULL, CLSCTX_ALL, IID_ISomeInterface, (void**)&interface_ptr);
```

## Reference counting

A COM object uses reference counting to manage object lifetime. An object's reference count is controlled by the clients through the `IUnknown` `AddRef` and `Release` methods. COM objects are responsible for freeing their own memory when the reference count drops to zero. Some programming contexts (e.g. Visual Basic) provide automatic reference counting to simplify object use. In C++, a smart pointer can be used to automate reference count management.

The following are guidelines for when *AddRef* and *Release* should be called:

- A functions that returns an interface reference (via return value or via "out" parameter) increments the count of the returned object

- *Release* is called before the interface pointer is overwritten or goes out of scope

- If a copy is made on an interface reference pointer, *AddRef* is called

- *AddRef* and *Release* are called on the interface which is being referenced (not a different interface of the same object) since an object may implement per-interface reference counts in order to allocate internal resources only for the interfaces which are being referenced

For remote objects, not all reference count calls are sent over the wire. A proxy keeps only one reference on the remote object and maintains its own local reference count.

To simplify COM development for C++ developers, Microsoft introduced ATL (Active Template Library). ATL provides a relatively high-level COM development paradigm. It also shields COM client application developers from the need to directly maintain reference counting, by providing smart pointer types. Other libraries and languages that are COM-aware include the Microsoft Foundation Classes, the VC Compiler COM Support, VBScript, Visual Basic, ECMAScript (JavaScript) and Borland Delphi.

## Programming context

COM is a language agnostic binary standard that allows objects to be used in any programming context able to access its binary interfaces.

COM client software is responsible for enabling the COM sub-system, instantiating and reference-counting COM objects and querying objects for supported interfaces.

The Microsoft Visual C++ compiler supports extensions to the C++ language, referred to as *C++ Attributes*, that are designed to simplify COM development and minimize boilerplate code required to implement COM servers in C++.

Originally, type library metadata was required to be stored in the system registry. A COM client would use the registry information for object creation.

Registration-free (RegFree) COM was introduced with Windows XP to allow storing type library metadata as an assembly manifest either as a resource in the executable file or in a separate file installed with the component. This allows multiple versions of the same component to be installed on the same computer, in different directories. And it allows for XCOPY deployment. This technology has limited support for EXE COM servers and cannot be used for system-wide components such as MDAC, MSXML, DirectX or Internet Explorer.

During application loading, the Windows loader searches for the manifest. If it is present, the loader adds information from it to the activation context. When the COM class factory tries to instantiate a class, the activation context is first checked to see if an implementation for the CLSID can be found. Only if the lookup fails, the registry is scanned.

A COM object can be created without type library information, and instead only a path to the DLL file and CLSID. A client can use the COM DLL function `DllGetClassObject` with the CLSID and IID_IClassFactory to create an instance of a factory object. The client can then use the factory object's `CreateInstance` to create an instance. This is the same process the COM sub-system uses. If an object created this way creates another object, it will do so in the usual way (using the registry or manifest). But it can create internal objects (which may not be registered at all), and hand out references to interfaces to them, using its own private knowledge.

## Marshalling

A COM object can be transparently created and used from within the same process (in-process), across process boundaries (out-of-process), or remotely over the network (DCOM). Out-of-process and remote objects use marshalling to serialize method calls and return values over process or network boundaries. This marshalling is invisible to the client, which accesses the object as if it were a local in-process object.

## Threading

In COM, threading is addressed through a concept known as *apartments*. An individual COM object lives in exactly one apartment, which might either be single-threaded or multi-threaded. There are three types of apartments in COM: *Single-Threaded Apartment (STA)*, *Multi-Threaded Apartment (MTA)*, and *Thread Neutral Apartment* (NA). Each apartment represents one mechanism whereby an object's internal state may be synchronized across multiple threads. A process can consist of multiple COM objects, some of which may use STA and others of which may use MTA. All threads accessing COM objects similarly live in one apartment. The choice of apartment for COM objects and threads are determined at run-time, and cannot be changed.

| Apartment type | Threading model | Description |
|---|---|---|
| Single-Threaded Apartment (STA) | Apartment | A single thread is dedicated to execute the methods of the object. Method calls from threads outside of the apartment are marshalled and automatically queued by the system (via Windows messaging). Thus, the COM run-time provides synchronization to ensure that each method call to the object is executed to completion before another is invoked. |
| Multi-Threaded Apartment (MTA) | Free | The COM run-time provides no synchronization, and multiple threads are allowed to call object methods simultaneously. The object need to handle synchronization to prevent simultaneous access from multiple threads from problems. Calls to an MTA object from a thread in an STA are also marshalled. |
| Dynamically determined apartment | Both | The server auto-selects STA or MTA at object creation to match the apartment type of the calling thread. This can be useful to avoid marshalling overhead when MTA servers are accessed by a STA thread. |
| Thread Neutral Apartment (NA) | Neutral | A special apartment without any assigned threads. When an STA or MTA thread calls an NA object in the same process, then the calling thread temporarily leaves its apartment and executes code directly in the NA without any thread switching. Therefore, one can think of NA as an optimization for efficient interapartment method calls. |

Threads and objects which belong to the same apartment follow the same thread access rules. Method calls which are made inside the same apartment are therefore performed directly without any assistance from COM. Method calls made across apartments are achieved via marshalling. This requires the use of proxies and stubs.

## Criticisms

### Complexity

COM is relatively complex especially compared to more modern component technologies such as .NET.

### Message pumping

When an STA is initialized it creates a hidden window that is used for inter-apartment and inter-process message routing. This window must have its message queue regularly "pumped". This construct is known as a "message pump". On earlier versions of Windows, failure to do so could cause system-wide deadlocks. This problem is complicated by some Windows APIs that initialize COM as part of their implementation, which causes a "leak" of implementation details.

### Reference counting

Reference counting within COM may cause problems if two or more objects are circularly referenced. The design of an application must take this into account so that objects are not left orphaned. Objects may also be left with active reference counts if the COM "event sink" model is used. Since the object that fires the event needs a reference to the object reacting to the event, the latter's reference count will never reach zero. Reference cycles are typically broken using either out-of-band termination or split identities. In the out-of-band termination technique, an object exposes a method which, when called, forces it to drop its references to other objects, thereby breaking the cycle. In the split identity technique, a single implementation exposes two separate COM objects (also known as identities). This creates a weak reference between the COM objects, preventing a reference cycle.

### DLL Hell

Because in-process COM components are implemented in DLL files and registration only allows for a single version per CLSID, they might in some situations be subject to the "DLL Hell" effect. Registration-free COM capability eliminates this problem for in-process components; registration-free COM is not available for out-of-process servers.
