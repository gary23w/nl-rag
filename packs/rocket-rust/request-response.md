---
title: "Request–response"
source: https://en.wikipedia.org/wiki/Request%E2%80%93response
domain: rocket-rust
license: CC-BY-SA-4.0
tags: rocket framework, rocket rust, rust web framework, type-safe routing
fetched: 2026-07-02
---

# Request–response

In computer science, **request–response** or **request–reply** is one of the basic methods computers use to communicate with each other in a network, in which the first computer sends a *request* for some data and the second *responds* to the request. More specifically, it is a message exchange pattern in which a requestor sends a request message to a replier system, which receives and processes the request, ultimately returning a message in response. It is analogous to a telephone call, in which the caller must wait for the recipient to pick up before anything can be discussed. This is a simple but powerful messaging pattern which allows two applications to have a two-way conversation with one another over a channel; it is especially common in client–server architectures.

Request–response pattern can be implemented synchronously (such as web service calls over HTTP) or asynchronously.

In contrast, **one-way** computer communication, which is like the push-to-talk or "barge in" feature found on some phones and two-way radios, sends a message without waiting for a response. Sending an email is an example of one-way communication, and another example are fieldbus sensors, such as most CAN bus sensors, which periodically and autonomously send out their data, whether or not any other devices on the bus are listening for it. (Most of these systems use a "listen before talk" or other contention-based protocol so multiple sensors can transmit periodic updates without any pre-coordination.)
