---
title: "WebFinger"
source: https://en.wikipedia.org/wiki/WebFinger
domain: well-known-uri
license: CC-BY-SA-4.0
tags: well-known uri, well-known resource path, site metadata discovery, webfinger discovery
fetched: 2026-07-02
---

# WebFinger

**WebFinger** is a protocol specified by the Internet Engineering Task Force IETF in RFC 7033 that allows for discovery of information about people and things identified by a URI. Information about a person might be discovered via an `acct:` URI, for example, which is a URI that looks like an email address.

WebFinger is specified as the discovery protocol for OpenID Connect, which is a protocol that allows one to more easily log in to various sites on the Internet.

The WebFinger protocol is used by federated software, such as GNU social (via its use in OStatus), Diaspora, or Mastodon, to discover users on federated nodes and pods, as well as the remoteStorage protocol. The WebFinger protocol does not specify the usage of "template" within the "links" section. That is an extension made by the former oStatus protocol that the Fediverse inherited from. The reasoning for expanding upon this later was justified by wanting to use a different key for a value that isn't an URL but a pattern to create one.

As a historical note, the name "WebFinger" is derived from the old ARPANET Finger protocol, but it is a very different protocol designed for HTTP.

The protocol payload is represented in JSON format with a MIME-Type of `application/jrd+json`.

## Technical overview

The WebFinger specification consists of a specified URI format and a minimal ontology which requires JSON resources served from that URI to declare their own additional ontologies.

### Contact Information Example

The following example demonstrates a hypothetical E-mail client functionality which retrieves contact information from WebFinger-supporting servers:

1. Alice opens the "Add contact" page of their E-Mail client and enters Bob's E-mail Address, `bob@example.com`.
2. The application then derives the WebFinger URL:
  - `https://example.com/.well-known/webfinger?resource=`...
  - ...the kind of schema the application is looking for (in this case we want to have account information): `acct`...
  - ...followed by an URL-Encoded `:`-character, a.k.a. `%3A`...
  - ...followed by the URL-Encoded value of interest: `bob%40example.com`.
  - Resulting in the URL: `https://example.com/.well-known/webfinger?resource=acct%3Abob%40example.com`.
3. The application then makes an HTTP GET request to this url and receives from the server a JSON document containing the requested information:{ "subject": "acct:bob@example.com", "aliases": [ "https://www.example.com/~bob/" ], "properties": { "http://example.com/ns/role": "employee" }, "links": [ { "rel": "http://webfinger.net/rel/profile-page", "href": "https://www.example.com/~bob/" }, { "rel": "http://webfinger.net/rel/avatar", "type": "image/png", "href": "https://www.example.com/~bob/avatar.png" } ] }
4. The application can then parse the JSON, using the `"rel"` properties to find appropriate uses for each URI. For example, links with `"rel"` `http://webfinger.net/rel/profile-page` can be used for populating the user's homepage field, and those with `"rel"` `http://webfinger.net/rel/avatar` could be used as a profile picture.

## Fediverse usage

Fediverse-based social networking software like Mastodon, PeerTube, and Misskey can look up the server name of a specific username by sending a request to the WebFinger endpoint of the domain within their username (the part after the 2nd `@`-symbol). This allows any entity with their own DNS domain name to have a consistent (set of) Fediverse username(s), without having to run the software on their own domain. This is especially useful to allow consistent Fediverse usernames across different feature-incongruous Fediverse softwares without having to host them all; e.g, a company could have accounts on PeerTube and Mastodon with the same `@bigcompany.tld` suffix without having to host either software on their own domain. For individuals, this feature allows the user to keep a consistent username (and its associated social capital) even if they switch instances by serving a JSON file with the appropriate `/.well-known/webfinger?resource=...` path on their webserver.

### Example for username `@Mastodon@mastodon.social`

WebFinger aware platforms and clients first send an HTTP GET request to `https://mastodon.social/.well-known/webfinger?resource=acct%3AMastodon%40mastodon.social`. The server responds with a JSON document:

```mw
{
   "subject":"acct:Mastodon@mastodon.social",
   "aliases":[
      "https://mastodon.social/@Mastodon",
      "https://mastodon.social/users/Mastodon"
   ],
   "links":[
      {
         "rel":"http://webfinger.net/rel/profile-page",
         "type":"text/html",
         "href":"https://mastodon.social/@Mastodon"
      },
      {
         "rel":"self",
         "type":"application/activity+json",
         "href":"https://mastodon.social/users/Mastodon"
      },
      {
         "rel":"http://ostatus.org/schema/1.0/subscribe",
         "template":"https://mastodon.social/authorize_interaction?uri={uri}"
      },
      {
         "rel":"http://webfinger.net/rel/avatar",
         "type":"image/png",
         "href":"https://files.mastodon.social/accounts/avatars/000/013/179/original/b4ceb19c9c54ec7e.png"
      }
   ]
}
```
