---
title: "Process isolation"
source: https://en.wikipedia.org/wiki/Process_isolation
domain: namespaces-isolation
license: CC-BY-SA-4.0
tags: linux namespace isolation, process resource namespacing, user namespace remapping, container primitive isolation
fetched: 2026-07-02
---

# Process isolation

**Process isolation** is a set of different hardware and software technologies designed to protect each process from other processes on the operating system. It does so by preventing process A from writing to process B. Security is easier to enforce by disallowing inter-process memory access, in contrast with architectures in which any process can write to any memory in any other process.

Process isolation can be implemented by giving each process its own virtual address space, where process A's address space is different from process B's address space – preventing A from writing onto B.

## Limited inter-process communication

In a system with process isolation, limited (controlled) interaction between processes may still be allowed over inter-process communication (IPC) channels such as shared memory, local sockets or Internet sockets. In this scheme, all of the process' memory is isolated from other processes except where the process is allowing input from collaborating processes.

System policies may disallow IPC in some circumstances. For example, in mandatory access control systems, subjects with different sensitivity levels may not be allowed to communicate with each other. The security implications in these circumstances are broad and span applications in network key encryption systematics as well as distributed caching algorithms. Interface-defined protocols such as basic cloud access architecture and network sharing are similarly affected.

## Operating systems

Operating systems that support process isolation by providing separate address spaces for each process include:

- Unix-like systems such as Linux, the BSDs, macOS, Solaris, and AIX
- VMS
- Windows NT

## Applications

On a system that supports process isolation, an application can use multiple processes to isolate components of the application from one another.

### Web browsers

Internet Explorer 4 used process isolation in order to allow separate windowed instances of the browser their own processes; however, at the height of the browser wars, this was dropped in subsequent versions to compete with Netscape Navigator (which sought to concentrate upon one process for the entire Internet suite). This idea of process-per-instance would not be revisited until a decade afterwards, when tabbed browsing became more commonplace.

In Google Chrome's "Multi-Process Architecture" and Internet Explorer 8's "Loosely Coupled IE (LCIE)", tabs containing webpages are contained within their own processes, which are isolated from the core process of the browser so as to prevent the crash of one tab/page from crashing the entire browser. This method (known popularly as **multiprocess** or **process-per-tab**) is meant to both manage memory and processing by allowing offending tabs to crash separately from the browser and other tabs and manage security.

In Firefox, the execution of NPAPI plug-ins like Flash and Silverlight became isolated in separate processes for each plug-in, starting in version 3.6.4. The foundation of this process isolation eventually became a project called Electrolysis or e10s for short, which extended process isolation to web content, browser chrome, and add-ons. This became enabled by default for all users starting in version 57, with the side-effect of add-ons requiring to be rewritten to the more limited Web Extensions. e10s was then later extended into per-origin process isolation (also known as "site isolation") with Project Fission, which was shipped in version 95.

#### Browsers with process isolation

- Google Chrome
- Internet Explorer 8 and later
- Safari
- Mozilla Firefox (plug-ins since 3.6.4, default for web content and everything else since 57)
- Maxthon
- Pale Moon (only for plug-ins since 3.6.4)

#### Criticism

Pale Moon is a notable web browser that has intentionally not isolated browser chrome, web content, add-ons, and other non-plugin components to their own processes. It claims that a multi-process browser will run into issues such as the asynchronous nature of inter-process communication conflicting with web standards that require a synchronous state (e.g. setting cookies), increased sluggishness in UI interaction due to messages having to be passed back-and-forth between the main chrome process and web content, increased resource usage due to the parsing, layout and rendering engines of the browser being duplicated across processes, and having no control over the IPC's security (which will necessarily replace the strict sandboxing between application code and document content found in the usual single-process browser or document viewer) handled by the operating system.

## Programming languages

Erlang (programming language) is providing a similar concept in user space, by realizing strictly separated lightweight processes.

- Virtual memory allows for memory space isolation by giving each process its own virtual address space.
- Polyinstantiation allows mirrors of shared resources, where changes by process A will not be visible to process B.
