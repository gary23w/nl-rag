---
title: "Heroku"
source: https://en.wikipedia.org/wiki/Heroku
domain: heroku-platform
license: CC-BY-SA-4.0
tags: heroku platform, heroku dyno, platform as a service, app deployment
fetched: 2026-07-02
---

# Heroku

**Heroku** is a cloud platform as a service (PaaS) supporting several programming languages. As one of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now also supports Java, Node.js, Scala, Clojure, Python, PHP, and Go. For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most of these languages. Heroku was acquired by Salesforce in 2010 for $212 million.

## History

Heroku was initially developed by James Lindenbaum, Adam Wiggins, and Orion Henry for supporting projects that were compatible with the Ruby programming platform Rack. The prototype development took around six months. Later on, Heroku faced setbacks because of a lack of proper market customers as many app developers used their own tools and environment. In January 2009, a new platform was launched which was built almost from scratch after a three-month effort. In October 2009, Byron Sebastian joined Heroku as CEO. On December 8, 2010, Salesforce.com acquired Heroku as a wholly owned subsidiary of Salesforce.com. On July 12, 2011, Yukihiro "Matz" Matsumoto, the chief designer of the Ruby programming language, joined the company as Chief Architect for Ruby. That same month, Heroku added support for Node.js and Clojure. On September 15, 2011, Heroku and Facebook introduced Heroku for Facebook. At present Heroku supports Redis databases in addition to its standard PostgreSQL.

On April 7, 2022, Heroku suffered a significant security intrusion when attackers were able to obtain an access token for a Heroku account that was used for automation purposes. Heroku confirmed that the attack accessed OAuth bearer tokens used for integration with GitHub and salted and hashed customer passwords in May 2022. The OAuth2 tokens were then used in targeted attacks against an unknown set of GitHub repositories apparently in an attempt to find secret tokens, where npm was the primary repository GitHub identified as a target. It is unclear if the original source of the breach is known or not.

In August 2022, Heroku announced that its free plans would be discontinued, citing fraud and abuse as reasons for the change.

In March 2024 at Kubecon Paris, Heroku announced that it was replatforming onto Kubernetes.

On February 6, 2026, Heroku announced that it would be transitioning to a new engineering model with a focus on security, reliability, support and stability rather than introducing new features. It mentioned that Enterprise Account contracts would no longer be offered to new users. It has emphasised that Heroku remains fully supported and existing customers would not be affected by this change.

## Etymology

The name "Heroku" is a portmanteau of "heroic" and "haiku". The Japanese theme is a nod to Matz for creating Ruby. The creators of Heroku did not want the name of their project to have a particular meaning, in Japanese or any other language, and so chose to invent a name.

## Architecture

Applications that are run on Heroku typically have a unique domain used to route HTTP requests to the correct application container or *dyno.* Each of the dynos are spread across a "dyno grid" which consists of several servers. Heroku's Git server handles application repository pushes from permitted users.

All Heroku services are hosted on Amazon's EC2 cloud-computing platform.

## Products

**The Heroku Platform**

The Heroku network runs the customer's apps in virtual containers which execute on a reliable runtime environment. Heroku calls these containers "Dynos". These Dynos can run code written in Node, Ruby, PHP, Go, Scala, Python, Java, or Clojure. Heroku also provides custom build packs with which the developer can deploy apps in any other language. Heroku lets the developer scale the app instantly just by either increasing the number of dynos or by changing the type of dyno the app runs in.

**Heroku Postgres**

Heroku Postgres is the

Cloud database

(DBaaS) service for Heroku based on

PostgreSQL

. Heroku Postgres provides features like continuous protection, rollback, and high availability; also forks, followers, and data clips.

**Heroku Redis**

Heroku Redis is the customized

Redis

from Heroku to provide a better developer experience. It is fully managed and is provided as a service by Heroku. It helps in managing instances with a CLI, associate data with Postgres to gain business insights using SQL tools, and lets customer gain performance visibility.

**Heroku Teams**

Heroku Teams is a team management tool which provides collaboration and controls to bring a customer's developers, processes, and tools together in order to build better software. With Heroku Teams, teams can self-organize, add, and manage members, get fine-grained control with app-level permissions, and also use collaboration tools like Heroku Pipelines. It also provides delegated administration and centralized billing.

**Heroku Enterprise**

Heroku Enterprise provides services to large companies which help them to improve collaboration among different teams. It provides a set of features like fine-grained access controls, identity federation, and private spaces to manage their enterprise application development process, resources, and users.

**Heroku Connect**

Heroku Connect lets users create Heroku apps that can easily integrate with

Salesforce

deployments at scale. This is done by having seamless data synchronization between Heroku Postgres databases and Salesforce organizations.

**Heroku Elements**

Heroku Elements provides users with Add-ons (tools and services for developing, extending, and operating the app), Buildpacks (which automate the build processes for the preferred languages and frameworks), and Buttons (a tool for the one-click provisioning, configuring, and deployment of third party components, libraries, and patterns).
