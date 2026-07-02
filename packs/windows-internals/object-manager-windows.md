---
title: "Object Manager"
source: https://en.wikipedia.org/wiki/Object_Manager_(Windows)
domain: windows-internals
license: CC-BY-SA-4.0
tags: windows internals, windows nt architecture, native api, windows registry
fetched: 2026-07-02
---

# Object Manager

(Redirected from

Object Manager (Windows)

)

**Object Manager** (internally called **Ob**) is a subsystem implemented as part of the Windows Executive which manages Windows *resources*. Resources, which are surfaced as logical *objects*, each reside in a namespace for categorization. Resources can be physical devices, files or folders on volumes, Registry keys or even running processes. All objects representing resources have an `Object Type` property and other metadata about the resource. Object Manager is a shared resource, and all subsystems that deal with the resources have to pass through the Object Manager.

## Architecture

Object Manager is the centralized resource broker in the Windows NT line of operating systems, which keeps track of the resources allocated to processes. It is resource-agnostic and can manage any type of resource, including device and file handles. All resources are represented as objects, each belonging to a logical namespace for categorization and having a type that represents the type of the resource, which exposes the capabilities and functionalities via properties. An object is kept available until all processes are done with it; Object Manager maintains the record of which objects are currently in use via reference counting, as well as the ownership information. Any system call that changes the state of resource allocation to processes goes via the Object Manager.

Objects can either be *Kernel objects* or *Executive objects*. Kernel objects represent primitive resources such as physical devices, or services such as synchronization, which are required to implement any other type of OS service. Kernel objects are not exposed to user mode code, but are restricted to kernel code. Applications and services running outside the kernel use *Executive objects*, which are exposed by the Windows Executive, along with its components such as the memory manager, scheduler and I/O subsystem. Executive objects encapsulate one or more kernel objects and expose not only the kernel and kernel-mediated resources, but also an expanded set of services that the kernel does. Applications themselves can wrap one or more Executive objects and surface objects that offer certain services. Executive objects are also used by the environment subsystems (such as the Win32 subsystem, the OS/2 subsystem, the POSIX subsystem, etc.) to implement the functionality of the respective environments.

Whenever an object is created or opened, a reference to the instance, known as a handle, is created. The Object Manager indexes objects by both their names and handles. Referencing objects by handles is faster since it bypasses name translation. Handles are associated with processes by making an entry in the process's Handle table, which lists the handles it owns, and can be transferred between processes. A process must own a handle to an object to use it, and can own up to 16,000,000 handles at one time. During creation, a process gains handles to a default set of objects. There are different types of handles, such as file handles, event handles, and process handles, which identify the type of target objects but do not distinguish the operations that can be performed through them. This consistency ensures uniform handling of various object types programmatically. Handle creation and resolution of objects from handles are exclusively managed by the Object Manager, ensuring that no resource usage goes unnoticed.

The types of Executive objects exposed by Windows NT are:

| Type | Description | System call to get handle |
|---|---|---|
| Directory | A container holds other kernel objects. Multiple levels of nested directories organize all kernel objects into a single tree. | NtCreateDirectoryObject NtOpenDirectoryObject |
| Process | A collection of executable threads along with virtual addressing and control information. | NtCreateProcess NtOpenProcess |
| Thread | An entity containing code in execution, inside a process. | NtCreateThread NtOpenThread |
| Job | A collection of processes. | NtCreateJobObject NtOpenJobObject |
| File | An open file, directory or an I/O device. | NtCreateFile NtOpenFile |
| Section | A region of memory optionally backed by a file or the page file. | NtCreateSection NtOpenSection |
| Access token | The identity, properties, privileges and access rights of a process or thread. | NtCreateToken NtDuplicateToken NtOpenProcessToken NtOpenThreadToken |
| Event | An object which encapsulates some information, to be used for notifying processes of something. | NtCreateEvent NtOpenEvent |
| Semaphore/Mutex | Objects which serialize access to other resources. | NtCreateSemaphore NtOpenSemaphore |
| Timer | An object which notifies processes at fixed intervals. | NtCreateTimer NtOpenTimer |
| Key | A registry key. | NtCreateKey NtOpenKey |
| Desktop | A logical display surface to contain GUI elements. | None |
| Clipboard | A temporary repository for other objects. | None |
| WindowStation | An object containing a group of Desktop objects, one Clipboard and other user objects. | None |
| Symbolic link | A reference to another object, via which the referred object can be used. | NtCreateSymbolicLinkObject NtOpenSymbolicLinkObject |

### Object structure

Each object managed by the Object Manager has a header and a body; the header contains state information used by Object Manager, whereas the body contains the object-specific data and the services it exposes. An object header contains certain data, exposed as `Properties`, such as `Object Name` (which identifies the object), `Object Directory` (the category the object belongs to), `Security Descriptors` (the access rights for an object), `Quota Charges` (the resource usage information for the object), `Open handle count` (the number of times a handle, an identifier to the object, has been opened), `Open handle list` (the list of processes which has a live reference to the object), its `Reference count` (the number of live references to the object), and the `Type` (an object that identifies the structure of the object body) of the object.

A `Type` object contains properties unique to the type of the object as well as static methods that implement the services offered by the object. Objects managed by Object Manager must at least provide a predefined set of services: `Close` (which closes a handle to an object), `Duplicate` (create another handle to the object with which another process can gain shared access to the object), `Query object` (gather information about its attributes and properties), `Query security` (get the security descriptor of the object), `Set security` (change the security access), and `Wait` (to synchronize with one or more objects via certain events). Type objects also have some common attributes, including the type name, whether they are to be allocated in non-paged memory, access rights, and synchronization information. All instances of the same type share the same type object, and the type object is instantiated only once. A new object type can be created by endowing an object with Properties to expose its state and methods to expose the services it offers.

`Object name` is used to give a descriptive identity to an object, to aid in object lookup. Object Manager maintains the list of names already assigned to objects being managed, and maps the names to the instances. Since most object accesses occur via handles, it is not always necessary to look up the name to resolve into the object reference. Lookup is only performed when an object is created (to make sure the new object has a unique name), or a process accesses an object by its name explicitly. `Object directories` are used to categorize them according to the types. Predefined directories include `\??` alias `\DosDevices` (device names), `\BaseNamedObjects` (mutexes, events, semaphores, waitable timers, and section objects), `\Callback` (callback functions), `\Device`, `\Driver`, `\FileSystem`, `\KnownDlls`, `\Nls` (language tables), `\ObjectTypes` (type objects), `\RPC Control` (RPC ports), `\Security` (security subsystem objects), and `\Windows` (windowing subsystem objects). Objects also belong to a *Namespace*. Each user session is assigned a different namespace. Objects shared between all sessions are in the *GLOBAL* namespace, and (logon) session-specific objects are in the specific (logon) session namespaces

OBJECT_ATTRIBUTES structure:

```mw
typedef struct _OBJECT_ATTRIBUTES {
  ULONG Length;
  HANDLE RootDirectory;
  PUNICODE_STRING ObjectName;
  ULONG Attributes;
  PSECURITY_DESCRIPTOR SecurityDescriptor;
  PSECURITY_QUALITY_OF_SERVICE SecurityQualityOfService;
} OBJECT_ATTRIBUTES *POBJECT_ATTRIBUTES;
```

The Attributes member can be zero, or a combination of the following flags:

```
OBJ_INHERIT
OBJ_PERMANENT
OBJ_EXCLUSIVE
OBJ_CASE_INSENSITIVE
OBJ_OPENIF
OBJ_OPENLINK
OBJ_KERNEL_HANDLE
```

## Usage

Object Manager paths are available to many Windows API file functions, although Win32 names like \\?\ and \\.\ for the local namespaces suffice for most uses. Using the former in Win32 user-mode functions translates directly to \??, but using \?? is still different as this NT form does not turn off pathname expansion.

Tools that serve as explorers in the Object Manager namespaces are available. These include the 32-bit WinObj from Sysinternals and the 64-bit WinObjEx64.
