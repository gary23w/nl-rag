---
title: "Backend as a service"
source: https://en.wikipedia.org/wiki/Backend_as_a_service
domain: supabase
license: CC-BY-SA-4.0
tags: supabase, backend as a service, postgres platform, cloud database
fetched: 2026-07-02
---

# Backend as a service

**Backend as a service** (**BaaS**), sometimes also referred to as **mobile backend as a service** (**MBaaS**), is a service for providing web app and mobile app developers with a way to easily build a backend to their frontend applications. Features available include user management, push notifications, and integration with social networking services. These services are provided via the use of custom software development kits (SDKs) and application programming interfaces (APIs). BaaS is a relatively recent development in cloud computing, with most BaaS startups dating from 2011 or later. Some of the most popular service providers are AWS Amplify and Firebase.

## Purpose

Web and mobile apps require a similar set of features on the backend, including notification service, integration with social networks, and cloud storage. Each of these services has its own API that must be individually incorporated into an app, a process that can be time-consuming and complicated for app developers. BaaS providers form a bridge between the frontend of an application and various cloud-based backends via a unified API and SDK.

Providing a consistent way to manage backend data means that developers do not need to redevelop their own backend for each of the services that their apps need to access, potentially saving both time and money.

Although similar to other cloud-computing business models, such as serverless computing, software as a service (SaaS), infrastructure as a service (IaaS), and platform as a service (PaaS), BaaS is distinct from these other services in that it specifically addresses the cloud-computing needs of web and mobile app developers by providing a unified means of connecting their apps to cloud services.

## Features

BaaS providers offer different set of features and backend tools. Some of the most common features include:

- **Database management**. Most BaaS solutions provide SQL and/or NoSQL database management services for applications. Developers can store their app data without deploying and managing databases themselves. BaaS usually provides client SDKs, REST and GraphQL APIs for the frontend to interact with databases.
- **File storage**. BaaS providers often offer storage solutions for media files, user uploads, and other binary data. Applications can upload, download, and delete files through provided SDKs and APIs.
- **Authentication and authorization**. Some BaaS offer authentication and authorization services that allow developers to easily manage app users. This includes user sign-up, login, password reset, social media login integration through OAuth, user group and permission management etc.
- **Notification service**. Some BaaS providers such as Firebase and AWS Amplify have notification services that can send custom emails to users and push native notifications on mobile platforms. This is especially useful for applications that need to send messages, alerts, and reminders.
- **Cloud functions**. Some BaaS allow developers to deploy and run serverless functions. The functions are usually stateless and can be triggered by various ways including HTTP requests, SDK invocation, background server events, and cloud scheduled executions. Different providers offer runtime support for different languages, some of the popular languages are JavaScript/TypeScript (Node.js, Deno), Python, Java/Kotlin. Cloud functions extend the potential and flexibility of BaaS by allowing developers to write custom functionalities for their apps, working in a way similar to a traditional REST API backend framework.
- **Usage analytics**. Analytics data about application usage is often included in BaaS. This allows developers to monitor user behaviors and make decisions correspondingly in marketing strategies and performance optimizations.
- **UI design**. Some BaaS providers, such as AWS Amplify and Backendless, offer user interface designing tools that help developers design the frontend UI of web and mobile apps. While this may be useful for small teams and individual developers, UI design assistance may not be conventional in BaaS as it goes beyond the scope of backend infrastructure.

- **Real-Time**. Real-time features in a BaaS platform ensure that data updates and synchronizations occur instantly across all clients, making changes immediately visible to users. This is crucial for applications like live chat and collaborative tools, using technologies like WebSockets to maintain continuous server-client connections.

## Service providers

BaaS providers have a broad focus, providing SDKs and APIs that work for app development on multiple platforms with different technology stacks, such as JavaScript (for Web apps), Flutter, Java/Kotlin (for Android apps), SWIFT/Objective-C (for iOS/MacOS/WatchOS/TvOS apps), .NET (for Windows) and others. BaaS providers also come in different types, suiting developers of different needs.

### Cloud-based BaaS

Most BaaS providers host backend platforms on their cloud servers. They also manage the infrastructure, security, and scalability of the platforms. Developers can access the backend services via a web interface or the provided APIs. Some examples of cloud-based BaaS include Firebase (hosted on Google Cloud Platform), AWS Amplify (hosted on Amazon Web Services), and Microsoft Azure Mobile Apps (hosted on Microsoft Azure).

### Self-hosted BaaS

Self-hosted BaaS allow developers to host backend on their own servers, providing more flexibility and potential to customization compared to cloud-based BaaS, which often is more difficult to migrate from. However, developers are also in charge of managing the infrastructure, security, and scalability of their servers.

### Mobile BaaS

Mobile backend as a service (MBaaS) is a type of BaaS specifically for applications deployed in mobile systems. While some references use MBaaS interchangeably for BaaS, BaaS can have a wider variety of support such as for web apps and desktop apps.

## Business model

BaaS providers generate revenue from their services in various ways, often using a freemium model. Under this model, a client receives a certain number of free active users or API calls per month, and pays a fee for each user or call over this limit. Alternatively, clients can pay a set fee for a package which allows for a greater number of calls or active users per month. There are also flat fee plans that make the pricing more predictable. Some of the providers offer the unlimited API calls inside their free plan offerings. Another business model that has been used by a lot of BaaS providers is PAYG (pay as you go), which has a flexible cost based on developers' usage of database, storage, bandwidth, function calls, user numbers etc.
