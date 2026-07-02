---
title: "Webhook"
source: https://en.wikipedia.org/wiki/Webhook
domain: admission-controllers
license: CC-BY-SA-4.0
tags: admission controller webhook, validating admission policy, mutating admission webhook, cluster request interception
fetched: 2026-07-02
---

# Webhook

In web development, a **webhook** is a method of augmenting or altering the behavior of a web page or web application with custom callbacks. These callbacks may be maintained, modified, and managed by third-party users who need not be affiliated with the originating website or application. In 2007, Jeff Lindsay coined the term *webhook* from the computer programming term *hook*.

## Function

Webhooks are "user-defined HTTP callbacks". They are usually triggered by some event, such as pushing code to a repository, a purchase, a comment being posted to a blog and many more use cases. When that event occurs, the source site makes an HTTP request to the URL configured for the webhook. Users can configure them to cause events on one site to invoke behavior on another.

Common uses are to trigger builds with continuous integration systems or to notify bug tracking systems. Because webhooks use HTTP, they can be integrated into web services without adding new infrastructure.

## Authenticating the webhook notification

When the client (the originating website or application) makes a webhook call to the third-party user's server, the incoming POST request should be authenticated to avoid a spoofing attack and its timestamp verified to avoid a replay attack. Different techniques to authenticate the client are used:

- HTTP basic authentication can be used to authenticate the client.
- The webhook can include information about what type of event it is, and a shared secret or digital signature to verify the webhook.
- An HMAC signature can be included as an HTTP header. GitHub, Stripe and Facebook use this technique.
- Mutual TLS authentication can be used when the connection is established. The endpoint (the server) can then verify the client's certificate.

The sender may choose to keep a constant list of IP addresses from which requests will be sent. This is not a sufficient security measure on its own, but it is useful for when the receiving endpoint is behind a firewall or NAT.
