---
title: "Facebook Platform"
source: https://en.wikipedia.org/wiki/Facebook_Platform
domain: open-graph-protocol
license: CC-BY-SA-4.0
tags: open graph protocol, social sharing metadata, meta property tags, link preview cards
fetched: 2026-07-02
---

# Facebook Platform

The **Facebook Platform** is the set of services, tools, and products provided by the social networking service Facebook for third-party developers to create their own applications and services that access data in Facebook.

The current Facebook Platform was launched in 2010. The platform offers a set of programming interfaces and tools which enable developers to integrate with the open "social graph" of personal relations and other things like songs, places, and Facebook pages. Applications on facebook.com, external websites, and devices are all allowed to access the graph.

## History

Facebook launched the Facebook Platform on May 24, 2007, providing a framework for software developers to create applications that interact with core Facebook features. A markup language called Facebook Markup Language was introduced simultaneously; it is used to customize the "look and feel" of applications that developers create. Prior to the Facebook platform, Facebook had built many applications themselves within the Facebook website, including Gifts, allowing users to send virtual gifts to each other, Marketplace, allowing users to post free classified ads, Facebook events, giving users a method of informing their friends about upcoming events, Video, letting users share homemade videos with one another, and social network game, where users can use their connections to friends to help them advance in games they are playing. The Facebook Platform made it possible for outside partners to build similar applications. Many of the popular early social network games would combine capabilities. For instance, one of the early games to reach the top application spot, (Lil) Green Patch, combined virtual Gifts with Event notifications to friends and contributions to charities through Causes.

Third-party companies provide application metrics, and several blogs arose in response to the clamor for Facebook applications. On July 4, 2007, Altura Ventures announced the "Altura 1 Facebook Investment Fund," becoming the world's first Facebook-only venture capital firm.

On August 29, 2007, Facebook changed the way in which the popularity of applications is measured, to give attention to the more engaging applications, following criticism that ranking applications only by the number of people who had installed the application was giving an advantage to the highly viral, yet useless applications. Tech blog Valleywag has criticized Facebook Applications, labeling them a "cornucopia of uselessness." Others have called for limiting third-party applications so the Facebook user experience is not degraded.

Applications that have been created on the Platform include chess, which both allow users to play games with their friends. In such games, a user's moves are saved on the website, allowing the next move to be made at any time rather than immediately after the previous move.

By November 3, 2007, seven thousand applications had been developed on the Facebook Platform, with another hundred created every day. By the second annual f8 developers conference on July 23, 2008, the number of applications had grown to 33,000, and the number of registered developers had exceeded 400,000.

Within a few months of launching the Facebook Platform, issues arose regarding "application spam", which involves Facebook applications "spamming" users to request it be installed.

Facebook integration was announced for the Xbox 360 and Nintendo DSi on June 1, 2009 at E3. On November 18, 2009, Sony announced an integration with Facebook to deliver the first phase of a variety of new features to further connect and enhance the online social experiences of PlayStation 3. On February 2, 2010, Facebook announced the release of *HipHop for PHP* as an opensource project. Mark Zuckerberg said that his team from Facebook is developing a Facebook search engine. “Facebook is pretty well placed to respond to people’s questions. At some point, we will. We have a team that is working on it", said Mark Zuckerberg. For him, the traditional search engines return too many results that do not necessarily respond to questions. “The search engines really need to evolve a set of answers: 'I have a specific question, answer this question for me.'"

On June 10, 2014, Facebook announced Haxl, a Haskell library that simplified the access to remote data, such as databases or web-based services.

### Partnerships with device manufacturers

Starting in 2007, Facebook formed data sharing partnerships with at least 60 handset manufacturers, including Apple, Amazon, BlackBerry, Microsoft and Samsung. Those manufacturers were provided with Facebook user data without the users' consent. Most of the partnerships remained in place as of 2018, when the partnerships were first publicly reported.

## High-level Platform components

### Graph API

The Graph API is the core of Facebook Platform, enabling developers to read from and write data into Facebook. The Graph API presents a simple, consistent view of the Facebook social graph, uniformly representing objects in the graph (e.g., people, photos, events, and pages) and the connections between them (e.g., friend relationships, shared content, and photo tags).

On April 30, 2015, Facebook shut down friends' data API prior to the v2.0 release.

### Authentication

Facebook authentication enables developers’ applications to interact with the Graph API on behalf of Facebook users, and it provides a single-sign on mechanism across web, mobile, and desktop apps.

#### Facebook Connect

Facebook Connect, also called Log in with Facebook, like OpenID, is a set of authentication APIs from Facebook that developers can use to help their users connect and share with such users' Facebook friends (on and off Facebook) and increase engagement for their website or application. When so used, Facebook members can log on to third-party websites, applications, mobile devices and gaming systems with their Facebook identity and, while logged in, can connect with friends via these media and post information and updates to their Facebook profile.

Originally unveiled during Facebook's developer conference, F8, in July 2008, Log in with Facebook became generally available in December 2008. According to an article from The New York Times, "Some say the services are representative of surprising new thinking in Silicon Valley. Instead of trying to hoard information about their users, the Internet companies (including Facebook, Google, MySpace and Twitter) all share at least some of that data so people do not have to enter the same identifying information again and again on different sites."

Log in with Facebook cannot be used by users in locations that cannot access Facebook, even if the third-party site is otherwise accessible from that location.

According to Facebook, users who logged into *The Huffington Post* with Facebook spent more time on the site than the average user.

Social plugins – including the Like Button, Recommendations, and Activity Feed – enable developers to provide social experiences to their users with just a few lines of HTML. All social plugins are extensions of Facebook and are designed so that no user data is shared with the sites on which they appear. On the other hand, the social plugins let Facebook track its users’ browsing habits through any sites that feature the plugins.

### Open Graph protocol

The Open Graph protocol enables developers to integrate their pages into Facebook's global mapping/tracking tool Social Graph. These pages gain the functionality of other graph objects including profile links and stream updates for connected users. OpenGraph tags in HTML5 might look like this:

### iframes

Facebook uses iframes to allow third-party developers to create applications that are hosted separately from Facebook, but operate within a Facebook session and are accessed through a user's profile. Since iframes essentially nest independent websites within a Facebook session, their content is distinct from Facebook formatting.

Facebook originally used 'Facebook Markup Language (FBML)' to allow Facebook Application developers to customize the "look and feel" of their applications, to a limited extent. FBML is a specification of how to encode content so that Facebook's servers can read and publish it, which is needed in the Facebook-specific feed so that Facebook's system can properly parse content and publish it as specified. FBML set by any application is cached by Facebook until a subsequent API call replaces it. Facebook also offers a specialized Facebook JavaScript (FBJS) library.

Facebook stopped accepting new FBML applications on March 18, 2011, but continued to support existing FBML tabs and applications. Since January 1, 2012 FBML was no longer supported, and FBML no longer functioned as of June 1, 2012.

### Microformats

In February 2011, Facebook began to use the hCalendar microformat to mark up events, and the hCard for the events' venues, enabling the extraction of details to users' own calendar or mapping applications.

### Mobile platform

The UI framework for the mobile website is based on Xhp, the Javelin JavaScript library, and WURFL. The mobile platform has grown dramatically in popularity since its launch. In December 2012, the number of users signing into the site from mobile devices exceeded web-based logins for the first time.

## Reception

Many Facebook application developers have attempted to create viral applications. Stanford University even offered a class in the Fall of 2007, entitled Computer Science (CS) 377W: "Create Engaging Web Applications Using Metrics and Learning on Facebook". Numerous applications created by the class were highly successful, and ranked amongst the top Facebook applications, with some achieving over 3.5 million users in a month.

In 2011, *The Guardian* expressed concerns that users publishing content through a third party provider are exposed to losing their web positioning if their service is removed; and the open graph could force connecting web presence to Facebook social services even for people using their own publishing channels. In June 2018, *The New York Times* criticized Facebook's partnerships with device manufacturers, writing that the data available to these manufacturers "raise concerns about the company's privacy protections and compliance with a 2011 consent decree with the Federal Trade Commission."

Facebook Platform is relatively unknown to the general public, with no notable occurrences relating to it, as the privacy policy and terms and conditions are regularly updated.
