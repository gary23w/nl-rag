---
title: "Thread Objects (The Java™ Tutorials > Essential Java Classes > Concurrency)"
source: https://docs.oracle.com/javase/tutorial/essential/concurrency/threads.html
domain: java
license: Oracle-BCL (tutorial excerpts) / CC-BY-SA-4.0
tags: java, jdk, javase, jvm
fetched: 2026-07-02
---

# Thread Objects (The Java™ Tutorials > Essential Java Classes > Concurrency)

Documentation

The Java™ Tutorials

Hide TOC

Trail:

Essential Java Classes

Lesson:

Concurrency

« Previous

•

Trail

•

Next »

# Thread Objects

Each thread is associated with an instance of the class `Thread`. There are two basic strategies for using `Thread` objects to create a concurrent application.

- To directly control thread creation and management, simply instantiate `Thread` each time the application needs to initiate an asynchronous task.
- To abstract thread management from the rest of your application, pass the application's tasks to an *executor*.

This section documents the use of `Thread` objects. Executors are discussed with other high-level concurrency objects.

« Previous

•

Trail

•

Next »

Previous page:

Processes and Threads

Next page:

Defining and Starting a Thread
