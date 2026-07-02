---
title: "Error code"
source: https://en.wikipedia.org/wiki/Error_code
domain: anyhow-error-rust
license: CC-BY-SA-4.0
tags: anyhow error handling, rust error library, anyhow context, rust error propagation
fetched: 2026-07-02
---

# Error code

In computing, an **error code** (or a **return code**) is a numeric or alphanumeric code that indicates the nature of an error and, when possible, why it occurred. Error codes can be reported to end users of software, returned from communication protocols, or used within programs as a method of representing anomalous conditions.

## In consumer products

Error codes are commonly encountered on displays of consumer electronics to users in order to communicate or specify an error. They can also be indicated by lights or beeps, e.g., if a device does not have a display. They are commonly reported by consumer electronics when users bring electronics to perform tasks that they cannot do (e.g., dividing by zero), or when the program within a device encounters an anomalous condition.

Error codes reported by consumer electronics are used to help diagnose and repair technical problems. An error code can be communicated to relevant support staff to identify potential fixes, or can simplify research into the cause of an error.

There is no definitive format for error codes, meaning that error codes typically differ from/between products and or companies.

## In computer programming

Error codes in computers can be passed to the system itself, to judge how to respond to the error. Often error codes come synonymous with an exit code or a return value. The system may also choose to pass the error code to its user(s). The Blue screen of death is an example of how the Windows operating system communicates error codes to the user.

Error codes can be used within a computer program to represent an anomalous condition. A computer program can take different actions depending on the value of an error code.

Different programming languages, operating systems, and programming environments often have their own conventions and standards for the meanings and values of error codes. Examples include:

- Unix-like systems have an errno.h header file that contains the meanings and values of error codes returned by system calls and library functions.
- Microsoft Windows' application programming interfaces (APIs) have several different standards for error code values, depending on the specific API being used.

The usage of error codes as an error handling strategy is often contrasted against using exceptions for error handling.

## In communication protocols

Communication protocols typically define a standard set of error codes, as a means of communicating the status or result of an operation between the entities in the system.

Several high-level protocols in the TCP/IP stack, such as HTTP, FTP, and SMTP, define their own standard sets of error codes:

- List of HTTP status codes
- List of FTP server return codes
- Simple Mail Transfer Protocol § Protocol overview

## In automobiles

Error codes in automobiles, sometimes referred to as trouble codes, indicate to a driver or car mechanic what is wrong with a vehicle before repairs are initiated.

In vehicles with CAN buses, error codes are often five-digit codes that pinpoint a particular car fault. Car owners can make use of an on-board diagnostics scanner or an owner's manual to identify the meaning of a trouble code. Five-digit diagnostic trouble codes typically consist of one letter and four numbers (e.g. P0123).
