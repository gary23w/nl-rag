---
title: "Embedded Systems/Embedded Systems Introduction"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Embedded_Systems_Introduction
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Embedded Systems Introduction

<

Embedded Systems

Embedded Technology is now in its prime and the wealth of knowledge available is mindblowing. However, most embedded systems engineers have a common complaint. There are no comprehensive resources available over the internet which deal with the various design and implementation issues of this technology. Intellectual property regulations of many corporations are partly to blame for this and also the tendency to keep technical know-how within a restricted group of researchers.

Before embarking on the rest of this book, it is important first to cover exactly what embedded systems are, and how they are used. This wikibook will attempt to cover a large number of topics, some of which apply only to embedded systems, but some of which will apply to nearly all computers (embedded or otherwise). As such, there is a chance that some of the material from this book will overlap with material from other wikibooks that are focused on topics such as low-level computing, assembly language, computer architecture, etc. But we will first start with the basics, and attempt to answer some questions before the book actually begins.

## What is an Embedded Computer?

The first question that needs to be asked, is "What exactly is an embedded computer?" An embedded computer is frequently a computer that is implemented for a particular purpose. In contrast, an average PC computer usually serves a number of purposes: checking email, surfing the internet, listening to music, word processing, etc... However, embedded systems usually only have a single task, or a very small number of related tasks that they are programmed to perform.

Every home has several examples of embedded computers. Any appliance that has a digital clock, for instance, has a small embedded micro-controller that performs no other task than to display the clock. Modern cars have embedded computers onboard that control such things as ignition timing and anti-lock brakes using input from a number of different sensors.

Embedded computers rarely have a generic interface, however. Even if embedded systems have a keypad and an LCD display, they are rarely capable of using many different types of input or output. An example of an embedded system with I/O capability is a security alarm with an LCD status display, and a keypad for entering a password.

In general, an Embedded System: It is a combination of hardware and software that performs a specific task.

- *Is a system built to perform its duty, completely or partially independent of human intervention.*
- *Is specially designed to perform a few tasks in the most efficient way.*
- *Interacts with physical elements in our environment, e.g. controlling and driving a motor, sensing temperature, etc.*

An embedded system can be defined as a control system or computer system designed to perform a specific task. Common examples of embedded systems include MP3 players, navigation systems on aircraft and intruder alarm systems. An embedded system can also be defined as a single purpose computer.

Most embedded systems are time critical applications meaning that the embedded system is working in an environment where timing is very important: the results of an operation are only relevant if they take place in a specific time frame. An autopilot in an aircraft is a time critical embedded system. If the autopilot detects that the plane for some reason is going into a stall then it should take steps to correct this within milliseconds or there would be catastrophic results.

## What are Embedded Systems Used For?

Embedded systems are considered when the cost of implementing a product designed in software on a microprocessor and some small amount of hardware, is cheaper, more reliable, or better for some other reason than a discrete hardware design. It is possible for one small and relatively cheap microprocessor to replace dozens or even hundreds of hardware logic gates, timing circuits, input buffers, output drivers, etc. It also happens that one generic embedded system with a standard input and output configuration can be made to perform in a completely different manner simply by changing the software.

The uses of embedded systems are virtually limitless, because every day new products are introduced to the market that utilize embedded computers in novel ways. In recent years, hardware such as microprocessors, microcontrollers, and FPGA chips have become much cheaper. So when implementing a new form of control, it's wiser to just buy the generic chip and write your own custom software for it. Producing a custom-made chip to handle a particular task or set of tasks costs far more time and money. Many embedded computers even come with extensive libraries, so that "writing your own software" becomes a very trivial task indeed.

From an implementation viewpoint, there is a major difference between a computer and an embedded system. Embedded systems are often required to provide ***Real-Time response***. A ***Real-Time system*** is defined as a system whose correctness depends on the timeliness of its response. Examples of such systems are flight control systems of an aircraft, sensor systems in nuclear reactors and power plants. For these systems, delay in response is a fatal error. A more relaxed version of ***Real-Time Systems***, is the one where timely response with small delays is acceptable. Example of such a system would be the Scheduling Display System on the railway platforms. In technical terminology, ***Real-Time Systems*** can be classified as:

- ***Hard Real-Time Systems*** - systems with severe constraints on the timeliness of the response.
- ***Soft Real-Time Systems*** - systems which tolerate small variations in response times.
- ***Hybrid Real-Time Systems*** - systems which exhibit both hard and soft constraints on its performance.

## What are Some Downfalls of Embedded Computers?

Embedded computers may be economical, but they are often prone to some very specific problems. A PC computer may ship with a glitch in the software, and once discovered, a software patch can often be shipped out to fix the problem. An embedded system, however, is frequently programmed once, and the software cannot be patched. Even if it is possible to patch faulty software on an embedded system, the process is frequently far too complicated for the user.

Another problem with embedded computers is that they are often installed in systems for which unreliability is not an option. For instance, the computer controlling the brakes in your car cannot be allowed to fail under any condition. The targeting computer in a missile is not allowed to fail and accidentally target friendly units. As such, many of the programming techniques used when throwing together production software cannot be used in embedded systems. Reliability must be guaranteed before the chip leaves the factory. This means that every embedded system needs to be tested and analyzed extensively.

An embedded system will have very few resources when compared to full blown computing systems like a desktop computer. The memory capacity and processing power in an embedded system is limited. It is more challenging to develop an embedded system when compared to developing an application for a desktop system as we are developing a program for a very constricted environment. Some embedded systems run a scaled down version of operating system called an RTOS (real time operating system).

## Why Study Embedded Systems?

Embedded systems are playing important roles in our lives every day, even though they might not necessarily be visible. Some of the embedded systems we use every day control the menu system on television, the timer in a microwave oven, a cellphone, an MP3 player or any other device with some amount of intelligence built-in. In fact, recent poll data shows that embedded computer systems currently outnumber humans in the USA. Embedded systems is a rapidly growing industry where growth opportunities are numerous.

## Who is This Book For?

This book is designed to accompany a course of study in computer engineering. However, this book will also be useful to any reader who is interested in computers, because this book can form the starting point for a "bottom up" learning initiative on computers. It is fundamentally easier to study small, limited, simple computers than it is to start studying the big PC behemoths that we use on a daily basis. Many topics covered in this book will be software topics as well, so this book will be the most helpful to people with at least some background in programming (especially C and Assembly languages). Having a prior knowledge of semiconductors and electric circuits will be beneficial, but will not be required.

## What Will This Book Cover?

This book will focus primarily on embedded systems, but the reader needs to understand 2 simple facts:

1. This book cannot proceed far without a general discussion of microprocessor architecture
2. Many of the concepts discussed in this book apply equally well, if not better, to Desktop computers than to embedded computers.

In the general interests of completeness, this book will cover a number of topics that have general relevance to all computers in general. Many of the lessons in this book will even be better applied by a desktop computer programmer than by an embedded systems engineer. It might be more fair to say that this book is more about "Low Level Computing" than "Embedded Systems".

This book will, of course, cover many embedded systems topics that are irrelevant when programming desktop computers, such as cross-compilers, Real-Time Operating Systems, EEPROM storage, code compression, bit-banging serial ports, umbilical development, etc.

## Where to Go From Here

After reading this book, there are a number of potential fields of study to continue learning.

- For people interested in operating systems, and hardware-software interfacing, read the Operating System Design wikibook.
- For people interested in C programming or Assembly Programming, see the Programming:C and X86 Assembly wikibooks, respectively.
- For people interested in digital control systems, there will eventually be a book on that topic here ( Programmable Logic )
- For people interested in digital signal processing, there will eventually be a book on that subject.
- For people interested in a further study of more advanced computer systems, there will eventually be books on computer hardware and microprocessors here. ( Microprocessor Design )
- For people interested in an even lower-level understanding of electronics, see Digital Circuits.
- Wikiversity: School of Very Small Information Systems is a course that includes using Java running on a FPGA.
- For people interested in designing motion control systems, that is, computer-controlled machines such as robots, machine tools, cars, buses, airplanes, ships, satellites, telescopes, etc., see Embedded Control Systems Design.

## Which Programming Languages Will This Book Use?

We try to make this wikibook *language neutral*. It is not fair to focus on one language, when all embedded computers can't be programmed in that language.

However, it is nice to have functional example code in some real language. Also, it is useful to point out some features of popular programming languages that are especially important for embedded systems.

- ANSI C programming language: Many microprocessors and microcontrollers can be programmed in C, and a number of C cross-compilers exist for that purpose. C is perhaps the most frequently used language for new embedded system development. The "volatile" keyword, rarely used in desktop app programming, becomes very important in Embedded Systems/C Programming.
- Originally developed by the department of defense for real-time operating systems and embedded systems, Ada was designed with multiprocessor support and strong compile-time checks to ensure the quality and integrity of developed systems—Many microcontrollers can be programmed with Ada as the GNAT Ada compiler it is part of the often ported GNU Compiler Collection, though documentation is often not as available as other more popular languages such as C.
- Assembly language: There are many different microcontroller families, each with their own assembly language with its own unique quirks. This book will cover some basics of assembly language common to most microcontrollers. Unlike desktop app programming, embedded system programs generally must set up an "interrupt vector table".
- This book will discuss (at least briefly) some techniques for multi-language programming (specifically C and assembly).
- There are some instances where microcontrollers are better programmed in a different language (BASIC and Forth come to mind)
- Some controllers are even programmed in their own proprietary languages (PIC Basic, and Dynamic C for instance).
- Some extremely well-known languages, such as C++ and Java, are rarely used in embedded systems, because C++ and Java compilers are simply unavailable for popular microcontrollers. However, this book may occasionally describe how to implement C++ and Java features in an environment that doesn't natively support them.
- Python compilers are available for some popular microcontrollers. Pyastra [1] compiles for all Microchip PIC12, PIC14 and PIC16 microcontrollers. PyMite [2] compiles for "any device in the AVR family that has at least 64 KiB program memory and 4 KiB RAM". PyMite also targets (some) ARM microcontrollers. Notice that these embedded Python compilers typically can only compile a subset of the Python language for these devices.

Further reading:

- Robotics: Design Basics: Design software#Programming Languages
- Embedded Systems/PIC Programming#Compilers.2C Assemblers

Retrieved from "

https://en.wikibooks.org/w/index.php?title=Embedded_Systems/Embedded_Systems_Introduction&oldid=3510836

"
