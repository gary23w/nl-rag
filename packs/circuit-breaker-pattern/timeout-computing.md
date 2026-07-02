---
title: "Timeout (computing)"
source: https://en.wikipedia.org/wiki/Timeout_(computing)
domain: circuit-breaker-pattern
license: CC-BY-SA-4.0
tags: circuit breaker pattern, fault tolerance resilience, cascading failure prevention, bulkhead isolation pattern
fetched: 2026-07-02
---

# Timeout (computing)

In telecommunications and related engineering (including computer networking and programming), the term **timeout** or **time-out** has several meanings, including:

- A network parameter related to an enforced event designed to occur at the conclusion of a predetermined elapsed time.
- A specified period of time that will be allowed to elapse in a system before a specified event is to take place, unless another specified event occurs first; in either case, the period is terminated when either event takes place. Note: A timeout condition can be canceled by the receipt of an appropriate time-out cancellation signal.
- An event that occurs at the end of a predetermined period of time that began at the occurrence of another specified event. The timeout can be prevented by an appropriate signal.

Timeouts allow for more efficient usage of limited resources without requiring additional interaction from the agent interested in the goods that cause the consumption of these resources. The basic idea is that in situations where a system must wait for something to happen, rather than waiting indefinitely, the waiting will be aborted after the timeout period has elapsed. This is based on the assumption that further waiting is useless, and some other action is necessary.

## Challenges

Balancing timeout values in distributed systems and microservices can be tricky: short timeout values can fail healthy requests prematurely, leading to complex workarounds, while long timeout values can result in slow error responses and poor user experiences. The circuit breaker design pattern can be a better alternative, as it can monitor service health, detect failures dynamically and faster, and improve the user experience.

## Examples

Specific examples include:

- In the Microsoft Windows and ReactOS command-line interfaces, the `timeout` command pauses the command processor for the specified number of seconds.
- In POP connections, the server will usually close a client connection after a certain period of inactivity (the timeout period). This ensures that connections do not persist forever, if the client crashes or the network goes down. Open connections consume resources, and may prevent other clients from accessing the same mailbox.
- In HTTP persistent connections, the web server saves opened connections (which consume CPU time and memory). The web client does not have to send an "end of requests series" signal. Connections are closed (timed out) after five minutes of inactivity; this ensures that the connections do not persist indefinitely.
- In a timed light switch, both energy and lamp's life-span are saved. The user does not have to switch off manually.
- Tablet computers and smartphones commonly turn off their backlight after a certain time without user input.
- To prevent a ReDoS (regular expression denial of service), one can use timeouts to cancel regular expression matching calls that exceed a time threshold.
