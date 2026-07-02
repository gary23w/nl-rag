---
title: "Syslog"
source: https://en.wikipedia.org/wiki/Syslog
domain: fluentd
license: CC-BY-SA-4.0
tags: fluentd logging, log collection, log management, unified logging layer
fetched: 2026-07-02
---

# Syslog

In computing, **syslog** (/ˈsɪslɒɡ/) is a standard for message logging. It allows separation of the software that generates messages, the system that stores them, and the software that reports and analyzes them. Each message is labeled with a facility code, indicating the type of system generating the message, and is assigned a severity level.

Computer system designers may use syslog for system management and security auditing as well as general informational, analysis, and debugging messages. A wide variety of devices, such as printers, routers, and message receivers across many platforms, use the syslog standard. This permits the consolidation of logging data from different types of systems in a central repository. Implementations of syslog exist for many operating systems.

When operating over a network, syslog uses a client-server architecture where a **syslog server** listens for and logs messages coming from clients.

## History

Syslog was developed in the 1980s by Eric Allman as part of the Sendmail project. It was readily adopted by other applications and has since become the standard logging solution on Unix-like systems. A variety of implementations also exist on other operating systems and it is commonly found in network devices, such as routers.

Syslog originally functioned as a de facto standard, without any authoritative published specification, and many implementations existed, some of which were incompatible. The Internet Engineering Task Force documented the status quo in RFC 3164 in August 2001. It was standardized by RFC 5424 in March 2009.

Various companies have attempted to claim patents for specific aspects of syslog implementations. This has had little effect on the use and standardization of the protocol.

## Message components

The information provided by the originator of a syslog message includes the facility code and the severity level. The syslog software adds information to the information header before passing the entry to the syslog receiver. Such components include an originator process ID, a timestamp, and the hostname or IP address of the device.

### Facility

A facility code is used to specify the type of system that is logging the message. Messages with different facilities may be handled differently. The list of facilities available is described by the standard:

| Facility code | Keyword | Description |
|---|---|---|
| 0 | kern | Kernel messages |
| 1 | user | User-level messages |
| 2 | mail | Mail system |
| 3 | daemon | System daemons |
| 4 | auth | Security/authentication messages |
| 5 | syslog | Messages generated internally by syslogd |
| 6 | lpr | Line printer subsystem |
| 7 | news | Network news subsystem |
| 8 | uucp | UUCP subsystem |
| 9 | cron | Cron subsystem |
| 10 | authpriv | Security and authentication messages |
| 11 | ftp | FTP daemon |
| 12 | ntp | NTP subsystem |
| 13 | security | Log audit |
| 14 | console | Log alert |
| 15 | solaris-cron | Scheduling daemon |
| 16–23 | local0 – local7 | Locally used facilities |

The mapping between facility code and keyword is not uniform in different operating systems and syslog implementations.

### Severity level

The list of severities of issues is also described by the standard:

| Value | Severity | Keyword | Deprecated keywords | Description | Condition |
|---|---|---|---|---|---|
| 0 | Emergency | `emerg` | `panic` | System is unusable | A panic condition. |
| 1 | Alert | `alert` |   | Action must be taken immediately | A condition that should be corrected immediately, such as a corrupted system database. |
| 2 | Critical | `crit` |   | Critical conditions | Hard device errors. |
| 3 | Error | `err` | `error` | Error conditions |   |
| 4 | Warning | `warning` | `warn` | Warning conditions |   |
| 5 | Notice | `notice` |   | Normal but significant conditions | Conditions that are not error conditions, but that may require special handling. |
| 6 | Informational | `info` |   | Informational messages | Confirmation that the program is working as expected. |
| 7 | Debug | `debug` |   | Debug-level messages | Messages that contain information normally of use only when debugging a program. |

The meaning of severity levels other than *Emergency* and *Debug* are relative to the application. For example, if the purpose of the system is to process transactions to update customer account balance information, an error in the final step should be assigned *Alert* level. However, an error occurring in an attempt to display the ZIP code of the customer may be assigned *Error* or even *Warning* level.

The server process that handles display of messages usually includes all lower (more severe) levels when the display of less severe levels is requested. That is, if messages are separated by individual severity, a *Warning* level entry will also be included when filtering for *Notice*, *Info* and *Debug* messages.

### Message

In RFC 3164, the message component (known as MSG) was specified as having these fields: *TAG*, which should be the name of the program or process that generated the message, and *CONTENT* which contains the details of the message.

Described in RFC 5424, "MSG is what was called CONTENT in RFC 3164. The TAG is now part of the header, but not as a single field. The TAG has been split into APP-NAME, PROCID, and MSGID. This does not totally resemble the usage of TAG, but provides the same functionality for most of the cases." Popular syslog tools such as NXLog, Rsyslog conform to this new standard.

The content field should be encoded in a UTF-8 character set and octet values in the traditional ASCII control character range should be avoided.

## Logger

Generated log messages may be directed to various destinations, including: console, files, remote syslog servers, or relays. Most implementations provide a command line utility, often called *logger*, as well as a software library, to send messages to the log.

To display and monitor the collected logs, one needs to use a client application or access the log file directly on the system. The basic command line tools are tail and grep. The log servers can be configured to send the logs over the network (in addition to the local files). Some implementations include reporting programs for filtering and displaying syslog messages.

## Network protocol

When operating over a network, syslog uses a client-server architecture where the server listens on a well-known or registered port for protocol requests from clients. Historically the most common transport layer protocol for network logging has been User Datagram Protocol (UDP), with the server listening on port 514. Because UDP lacks congestion control mechanisms, Transmission Control Protocol (TCP) port 6514 is used; Transport Layer Security is also required in implementations and recommended for general use.

## Limitations

Since each process, application, and operating system was written independently, there is little uniformity to the payload of the log message. For this reason, no assumption is made about its formatting or contents. A syslog message is formatted (RFC 5424 gives the Augmented Backus–Naur form (ABNF) definition), but its MSG field is not.

The network protocol is simplex communication, with no means of acknowledging the delivery to the originator.

## Outlook

Various groups are working on draft standards detailing the use of syslog for more than just network and security event logging, such as its proposed application within the healthcare environment.

Regulations, such as the Sarbanes–Oxley Act, PCI DSS, HIPAA, and many others, require organizations to implement comprehensive security measures, which often include collecting and analyzing logs from many different sources. The syslog format has proven effective in consolidating logs, as there are many open-source and proprietary tools for reporting and analysis of these logs. Utilities exist for conversion from Windows Event Log and other log formats to syslog.

Managed Security Service Providers attempt to apply analytical techniques and artificial intelligence algorithms to detect patterns and alert customers to problems.

## Internet standard documents

The Syslog protocol is defined by Request for Comments (RFC) documents published by the Internet Engineering Task Force (Internet standards). The following is a list of RFCs that define the syslog protocol:

- **The BSD syslog Protocol*. IETF. RFC 3164.* (obsoleted by **The Syslog Protocol*. IETF. RFC 5424.*)
- **Reliable Delivery for syslog*. IETF. RFC 3195.*
- **The Syslog Protocol*. IETF. RFC 5424.*
- **TLS Transport Mapping for Syslog*. IETF. RFC 5425.*
- **Transmission of Syslog Messages over UDP*. IETF. RFC 5426.*
- **Textual Conventions for Syslog Management*. IETF. RFC 5427.*
- **Signed Syslog Messages*. IETF. RFC 5848.*
- **Datagram Transport Layer Security (DTLS) Transport Mapping for Syslog*. IETF. RFC 6012.*
- **Transmission of Syslog Messages over TCP*. IETF. RFC 6587.*
