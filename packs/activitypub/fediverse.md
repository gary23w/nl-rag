---
title: "Fediverse"
source: https://en.wikipedia.org/wiki/Fediverse
domain: activitypub
license: CC-BY-SA-4.0
tags: activitypub protocol, fediverse protocol, decentralized social protocol, federated social networking
fetched: 2026-07-02
---

# Fediverse

The **Fediverse** (commonly shortened to **fedi**) is a collection of social networking services that can communicate with each other (formally known as federation) using a common protocol. Users of different websites can send and receive status updates, multimedia files and other data across the network. The term *Fediverse* is a portmanteau of *federation* and *universe*.

The majority of Fediverse platforms are based on free and open-source software, and create connections between servers using the ActivityPub protocol. Some software still supports older federation protocols as well, such as OStatus, the Diaspora protocol and Zot, while newer protocols such as AT Protocol connect via network bridges. Diaspora is the only actively developed software project classified under the original definition of *Fediverse* that does not support ActivityPub.

## Design

While a traditional social networking service will host all its content on servers managed by the owner of the website, the decentralized structure of the Fediverse allows any individual or organization to host a social platform using their own servers (referred to as an "instance").

Every instance is independent, and can set its own rules and expectations. Even so, much like how users of one email service such as Gmail can still send emails to users of another service such as Outlook, users may still view content and interact with users on any other instance in the Fediverse. A user on one Mastodon instance, for example, may view and interact with posts made by a user on a different instance even if it is not running Mastodon.

Instances hosted by different social networking services may also communicate with one another. A user on the microblogging platform Misskey, for example, may view and interact with posts made by users on Mastodon. Some Fediverse networks even allow users to interact with different social networking formats from the same platform. For example, a user on a social news instance running Lemmy can interact with another post from an mbin instance, a similar service, as well as microblog statuses from Mastodon.

### Content moderation and user safety

Decentralized social networking platforms introduce new challenges and difficulties for user trust and safety. By nature of the Fediverse, operators of an instance are solely responsible for moderation of its content. As there is no form of centralized governance or moderation across the Fediverse, it is impossible for an instance to be "removed" from the Fediverse; it can only be defederated per an instance operator's choice, which makes that instance's content inaccessible from the operator's instance. Individual instances are responsible for defining their own content policies, which may then be enforced by its staff. Moderation of a Fediverse instance differs significantly from that of traditional social media platforms, as moderators are responsible not only for content posted by users of that instance ("local users"), but also for content posted by users of other instances ("remote users").

## History

### Historical protocols

The concept and the functionality of the Fediverse existed before the ActivityPub protocol and the term itself. One of the first projects that included support for a decentralized social networking service was Laconica, a microblogging platform which implemented the OpenMicroBlogging protocol for communicating between different installations of the software. The software was later renamed to StatusNet in 2009, before being merged into the GNU social project in 2013 along with Free Social, with the two latter servers being a fork of StatusNet.

Over time, the limitations of the OpenMicroBlogging protocol became more apparent, being designed as a one-way text messaging system. To replace the ageing protocol, OStatus was devised as an open standard for microblogging, combining various other technologies like Salmon, Atom, WebSub and ActivityStreams into a single protocol used for communicating between instances. StatusNet first implemented the OStatus protocol on March 3, 2010, with version 0.9.0, and OStatus quickly became the most popular federated protocol in usage.

Around the same time as OStatus was gaining popularity, the Diaspora social network was formed, using its own federated protocol. To illustrate the differences between the two protocols, the terms of *the Fediverse* and *the federation* began to enter common usage, mainly after 2017. The term "the Fediverse" was used to describe the network formed by software using the OStatus protocol, such as GNU Social, Mastodon, and Friendica, in contrast to the competing diaspora protocol under "the federation".

### ActivityPub

In December 2012, the flagship StatusNet instance at the time, identi.ca, transitioned away to a new software named pump.io, with a new federation protocol to replace OStatus. The new protocol was designed to be useful for general activity streams and not just status updates, and replaced many of OStatus' external dependencies with JSON-LD and a REST API for its messaging and inbox systems, as well as making more use of ActivityStreams. While not as utilized as its OStatus predecessor, it would later become influential in the development of the ActivityPub standard.

In January 2018, the W3C presented the ActivityPub protocol as a recommended standard. The standard aimed to improve the interoperability between different software packages running on a wide network of servers and to supersede both the OStatus protocol and Pump.io. By 2019, almost all software that was using OStatus had added support for ActivityPub. While Mastodon began to remove OStatus support, other projects maintained it in their code, such as Friendica (which also maintained diaspora support along with ActivityPub).

### AT Protocol

A major protocol often contrasted with ActivityPub is the AT Protocol, which powers the Bluesky social network. While both protocols aim to create decentralized social networks, they employ different technical philosophies regarding user identity.

Developers of the AT Protocol, including Bluesky CEO Jay Graber, have stated they chose not to use ActivityPub because it did not natively support easy "account portability", the ability for a user to move their account, data, and social graph to a new provider without relying on the original server to authorize the move. In the ActivityPub model (used by Mastodon), a user's identity is typically tied to a specific server, similar to an email address; if that server goes offline, the identity can be lost. The AT Protocol aims to solve this by separating identity from hosting, allowing users to switch providers without losing their identity.

Although the two protocols are technically incompatible by default, third-party "bridges" such as Bridgy Fed have been developed to allow users on ActivityPub networks to follow and interact with users on the AT Protocol network, and vice versa.

### Other Fediverse protocols

While the Fediverse has traditionally been the network most commonly referred to and used as an example regarding the subject of decentralized social networks, alternatives to it and the accompanying ActivityPub have been developed and deployed. Smaller competitors such as Nostr and Farcaster have become popular within the cryptocurrency community. These protocols have used ActivityPub as a frame of reference for which to design their own architecture, as these newer protocols use a different federation model based on publishing content to relays for distribution rather than ActivityPub's server-centric model.

Despite their differences, software exists that permit the bridging of user content between these protocols, including "double-bridges" that span multiple protocols for the purpose of distributing the same content.

## Adoption

Users have been slow to embrace the Fediverse due to poor user experience and excessive complexity.

Following the acquisition of Twitter by Elon Musk in November 2022, certain major social networks, including Threads, Tumblr and Flipboard, expressed interest in supporting the ActivityPub protocol, as a large number of users began to migrate to Mastodon, a server that supports the Fediverse and was also the most popular alternative to Twitter at the time. Flickr also expressed support in supporting ActivityPub. As of November 2022, no information had been released by Flickr after the initial tweets by the CEO, with support for ActivityPub suspected to be on hold or cancelled.

In 2024, the local government of the Stary Sącz municipality in Poland launched their own PeerTube instance in order to *de facto* abolish its presence on YouTube. According to the government, they stopped using YouTube for official communications "in order to adhere to the appropriate regulations". In the same year, VIVERSE, HTC Vive's metaverse platform, implemented support for ActivityPub in their chat feature, allowing users to send direct messages to other fediverse users.

### Government and public-sector use

Several European public bodies operate ActivityPub services. The European Commission hosts an official Mastodon instance. The European Data Protection Supervisor (EDPS) published a data protection notice laying out the legal framework for operating a Mastodon service. More recently, Mastodon offers paid support aimed at larger institutions. However, the decentralized architecture of the network cannot centrally enforce age verification because verification data is left to individual server operators.

### Content management systems

WordPress has an officially supported plugin that integrates WordPress blogs into the Fediverse, allowing for comments to be exchanged between the comment section of a blog post and a Fediverse instance's reply function. The plugin was acquired by Automattic in March 2023, and became available for all WordPress.com users in October of that same year.

Ghost, a blogging platform and content management system, announced in April 2024 that they would be implementing Fediverse support via ActivityPub. The feature had been highly requested on its forums. In July 2024, Ghost started federating its development newsletter for the feature.

### Microblogging

Automattic CEO Matt Mullenweg tweeted in November 2022 that Tumblr was adding support for ActivityPub interoperability, in response to a user's complaints about Mastodon's complexity. However, no further information was revealed for over a year, and the project was expected to be cancelled after a leaked reorganization that moved most of Tumblr's staff to other Automattic projects. However, following a question from a TechCrunch reporter during a questionnaire about the leaked memo, he revealed that the interoperability feature was not cancelled and that there was a small team working on studying the potential of implementing the protocol. The plan was once again affirmed by Automattic in January 2025, with the ActivityPub plugin for WordPress most likely being the main method used for interoperability with the fediverse.

The release of Threads by Meta in July 2023 had included in its press release that it planned to support interoperability with the ActivityPub protocol. In December 2023, select Meta employees began to federate with ActivityPub. A roadmap was revealed in January 2024 that detailed the integration of ActivityPub in Threads.

A faction of fediverse server admins, some of whom have listed their names under a pledge named "Fedipact", have expressed resistance to open federation with Threads over concerns that Meta would adopt an "embrace, extend, and extinguish" policy towards the network, or that Threads' moderation would fail to prevent the spread of abusive content targeted towards marginalized communities.

In March 2024, Threads implemented a beta version of Fediverse support, allowing Threads users to view the number of Fediverse users that liked their post, and allowing Fediverse users to view posts from Threads on their own instances. On April 2, the official Threads account for President Joe Biden enabled federation on its profile, making Biden the first President of the United States to have a presence on the Fediverse. The ability to view replies from the Fediverse within Threads was added in August.

### News aggregators

In December 2023, the social magazine app Flipboard began integrating with the Fediverse by federating publisher accounts via ActivityPub. CEO Mike McCue stated the move was intended to break away from "walled garden" ecosystems, making Flipboard content discoverable and interactive for users on platforms like Mastodon.

During the 2023 Reddit API controversy, the decentralized link aggregator Lemmy experienced a significant surge in growth as users sought alternatives to Reddit. The platform saw its monthly active user count rise from approximately 1,000 to over 66,000 within weeks of the protests, exacerbated by Reddit's decision to temporarily ban communities and users promoting the migration to Fediverse alternatives.

## Software

### ActivityPub

ActivityPub is the most widely used protocol in the Fediverse and a W3C standard. Some popular Fediverse software includes:

- Microblogging
  - Mastodon
  - Misskey
  - Pleroma

- Image sharing/video sharing
  - Pixelfed
  - PeerTube
- Social networking
  - Friendica
- Social news
  - Lemmy
  - Piefed
- Events
  - Mobilizon
- Content management
  - Ghost
  - WordPress

### AT Protocol

- Bluesky

- WhiteWind – A long-form blogging platform that allows users to write and publish posts directly to their AT Protocol repository.

- Skylight – A Tiktok alternative with AT protocol as its connection.

- Smoke Signal – A decentralized event management and RSVP application.

### Others

**Social networking**

- GNU social – One of the earliest Fediverse projects, historically using the OStatus protocol to enable federation before the widespread adoption of ActivityPub.
- Diaspora – A decentralized social network that uses its own custom protocol.

**Content management**

- Drupal (via third-party plugin)
- WordPress (via official plugin)
