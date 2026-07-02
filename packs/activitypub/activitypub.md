---
title: "ActivityPub"
source: https://en.wikipedia.org/wiki/ActivityPub
domain: activitypub
license: CC-BY-SA-4.0
tags: activitypub protocol, fediverse protocol, decentralized social protocol, federated social networking
fetched: 2026-07-02
---

# ActivityPub

**ActivityPub** is a protocol and open standard for decentralized social networking. It provides a client-to-server (C2S) API for creating and modifying content, as well as a federated server-to-server (S2S) protocol for delivering notifications and content to other servers. ActivityPub is the defining standard of the Fediverse, a decentralised social network of various social interaction models, and content types, which consists of independently managed instances of software such as Mastodon, Pixelfed and PeerTube, among others.

ActivityPub is considered to be an update to the ActivityPump protocol used in pump.io, and the official W3C repository for ActivityPub is identified as a fork of ActivityPump. The creation of a new standard for decentralized social networking was prompted by the complexity of OStatus, the most commonly used protocol at the time. OStatus was built using a multitude of technologies (such as Atom, Salmon, WebSub and WebFinger), a product of the infrastructure used in GNU social (the originator and largest user of the OStatus protocol), which made it difficult to implement the protocol into new software. OStatus was also only designed to work with microblogging services, with little flexibility to the types of data that it could hold.

The standard was first published by the World Wide Web Consortium (W3C) as a W3C Recommendation in January 2018 by the Social Web Working Group (SocialWG), a working group chartered to build the protocols and vocabularies needed to create a standard for social functionality. Shortly after, further development was moved to the Social Web Community Group (SocialCG), the successor to the SocialWG.

## Design

ActivityPub uses the ActivityStreams 2.0 format for building its content, which itself uses JSON-LD. The three main data types used in ActivityPub are Objects, Activities and Actors. Objects are the most common data type, and can be images, videos, or more abstract items such as locations or events. Activities are actions that create and modify objects, for example a `Create` activity creates an object. Actors are representative of an individual, a group, an application or a service, and are the owners of objects.

Every actor type contains an inbox and outbox stream, which sends and receives activities for a user. In order to publish data (for example liking an article), a user creates an activity that declares that they liked an Article object and publishes it to their outbox, where it is then delivered by the ActivityPub server via a POST request to the inboxes listed in the activity's `to`, `bto`, `cc` and `bcc` fields. The receiving servers then account for the newly received activity and update the article by adding the like action to it.

### Example data

An example actor object that represents a user account:

```mw
{
  "@context": ["https://www.w3.org/ns/activitystreams",
               {"@language": "ja"}],
  "type": "Person",
  "id": "https://kenzoishii.example.com/",
  "following": "https://kenzoishii.example.com/following.json",
  "followers": "https://kenzoishii.example.com/followers.json",
  "liked": "https://kenzoishii.example.com/liked.json",
  "inbox": "https://kenzoishii.example.com/inbox.json",
  "outbox": "https://kenzoishii.example.com/feed.json",
  "preferredUsername": "kenzoishii",
  "name": "石井健蔵",
  "summary": "この方はただの例です",
  "icon": [
    "https://kenzoishii.example.com/image/165987aklre4"
  ]
}
```

An example activity that likes an article object:

```mw
{
  "@context": ["https://www.w3.org/ns/activitystreams",
               {"@language": "en"}],
  "type": "Like",
  "actor": "https://dustycloud.org/christine/",
  "summary": "Christine liked 'Minimal ActivityPub update client'",
  "object": "https://rhiaro.co.uk/2016/05/minimal-activitypub",
  "to": ["https://rhiaro.co.uk/#amy",
         "https://dustycloud.org/followers",
         "https://rhiaro.co.uk/followers/"],
  "cc": "https://e14n.com/evan"
}
```

An example article object:

```mw
{
  "@context": ["https://www.w3.org/ns/activitystreams",
               {"@language": "en-GB"}],
  "id": "https://rhiaro.co.uk/2016/05/minimal-activitypub",
  "type": "Article",
  "name": "Minimal ActivityPub update client",
  "content": "Today I finished morph, a client for posting ActivityStreams2...",
  "attributedTo": "https://rhiaro.co.uk/#amy",
  "to": "https://rhiaro.co.uk/followers/",
  "cc": "https://e14n.com/evan"
}
```

## Project status

The SocialCG previously organized a yearly free conference called ActivityPub Conf about the future of ActivityPub. Triages are held regularly to review issues pertaining to the ActivityPub and ActivityStreams 2.0 specifications as part of the SocialCG.

In 2023, Germany's Sovereign Tech Fund donated €152,000 to socialweb.coop with the goal of building a new suite for testing various ActivityPub implementations and their compliance with the specification.

### Adoption

The initial wave of adoption for ActivityPub (circa 2016–2018) came from software that was already using OStatus as their federation protocol, such as Mastodon, GNU social and Pleroma. Following the acquisition of Twitter by Elon Musk in 2022, many groups of users that were critical of the acquisition migrated to Mastodon, bringing new attention to the ActivityPub protocol with it. Various major social media platforms and corporations have since pledged to implement ActivityPub support, including Tumblr, Flipboard and Meta Platforms' Threads. Threads introduced crossposting to ActivityPub in 2024 for users outside of the European Economic Area, however full 2-way compatibility remains incomplete as of 2025.

## Criticism

### Accidental denial-of-service attacks

Poorly optimized ActivityPub implementations can cause unintentional distributed denial-of-service (DDOS) attacks on other websites and servers, due to the decentralized nature of the network. An example would be Mastodon's implementation of OpenGraph link previews, wherein every instance that receives a post that contains a link with OpenGraph metadata will download the associated data, such as a thumbnail, in a very short timeframe, which can slow down or crash servers as a result of the sudden burst of requests.

### Account migration

ActivityPub has been criticized for not natively supporting moving accounts from one server to another, forcing implementations to build their own solutions. While there has been work on building a standardized system for migrating accounts using the Move activity via the Fediverse Enhancement Proposal organization, the current proposal only allows for basic follower migration, with all other data remaining linked to the original account.

### Missing content and data

ActivityPub implementations have been criticized for missing replies and parts of reply threads from remote posts, and presenting outdated statistics (e.g. likes and reposts) about remote posts. However, this isn't a problem with the ActivityPub protocol itself, but with implementations not refreshing their content for updated data when needed.

## Software using ActivityPub

| Software name | Total users | Initial ActivityPub-compatible release | Type of software | Fork of |
|---|---|---|---|---|
| Akkoma | 9,530 | 2022 | Blogging | Pleroma |
| BookWyrm | 31,132 | 2021 | Book cataloging |   |
| Castopod | 818 podcasts | 2020 | Audio hosting |   |
| Discourse | ? | 2025 | Internet forum |   |
| Firefish | 4,137 | 2022 | Blogging | Misskey |
| Flipboard | 145,000,000 | 2023 | Social news |   |
| Friendica | 12,713 | 2010 | Blogging, event management, groups, image gallery |   |
| Funkwhale | 5,447 | 2018 | Audio hosting |   |
| Gancio | 3,363 | 2020 | Calendar, event planner |   |
| Ghost | ? | 2025 (in beta) | Blogging |   |
| Hubzilla | 7,851 | 2015 | Blogging, event planner, file hosting, image gallery, wiki |   |
| Iceshrimp.NET | 519 | 2024 | Blogging |   |
| Iceshrimp | 3,525 | 2023 | Blogging | Firefish |
| Lemmy | 481,487 | 2019 | Social news |   |
| Libervia | ? | 2022 (in beta) | Blogging, event management, file sharing, instant messaging |   |
| Loops | 39,323 | 2025 (in beta) | Video sharing (short-video sharing) |   |
| Mastodon | 8,513,201 | 2017 | Blogging |   |
| mbin | 10,204 | 2023 | Social news | kbin |
| Micro.blog | 235,487 | 2021 | Microblogging |   |
| Minds |   |   | Blogging |   |
| Misskey | 1,162,727 | 2018 | Blogging |   |
| Mobilizon | 89,657 | 2020 | Event management, groups |   |
| NodeBB | 219,102 | 2025 | Internet forum |   |
| PeerTube | 433,828 | 2018 | Video sharing |   |
| PieFed | 11,712 | 2023 | Social news |   |
| Pixelfed | 1,016,775 | 2018 | Image sharing |   |
| Pleroma | 66,121 | 2018 | Blogging |   |
| Plume | 4,084 | 2018 | Blogging |   |
| Sharkey | 23,786 | 2023 | Blogging | Misskey |
| Snac | 68 | 2022 | Blogging |   |
| Socialhome | 3,000 | 2016 | Blogging |   |
| Threads | 130,000,000 | 2023 | Blogging |   |
| Wafrn | 6,074 | 2023 | Blogging |   |
| WordPress | 27,091 | 2023 | Blogging |   |
| WriteFreely | 50,861 | 2018 | Blogging |   |

### Future implementations

- Flarum, an internet forum software
- Forgejo, a Git forge and development platform

### Uncertain future implementations

- GitLab, a Git forge and development platform which had previously had an open issue discussing the topic, but was later closed due to the development team moving focus to other areas.
- Tumblr, a microblogging platform. Despite previous statements from Automattic CEO Matt Mullenweg, ActivityPub integration has been delayed indefinitely. The integration would have been implemented with its WordPress migration, as the first-party plugin for interoperability would have been used for federation.
- Flickr, an image and video hosting site.
