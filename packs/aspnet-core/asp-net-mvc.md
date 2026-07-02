---
title: "ASP.NET MVC"
source: https://en.wikipedia.org/wiki/ASP.NET_MVC
domain: aspnet-core
license: CC-BY-SA-4.0
tags: asp.net core, asp.net mvc, dotnet web, razor pages
fetched: 2026-07-02
---

# ASP.NET MVC

**ASP.NET MVC** is a web application framework developed by Microsoft that implements the model–view–controller (MVC) pattern. It is no longer in active development. It is open-source software, apart from the ASP.NET Web Forms component, which is proprietary.

ASP.NET Core has since been released, which unified ASP.NET, ASP.NET MVC, ASP.NET Web API, and ASP.NET Web Pages (a platform using only Razor pages). MVC 6 was abandoned due to Core and is not expected to be released. Core is currently planned to merge into ".NET 5".

Some well known sites that use ASP.NET MVC include Stack Overflow, Microsoft, GoDaddy and Ancestry.com.

## Background

Based on ASP.NET, ASP.NET MVC allows software developers to build a web application as a composition of three roles: *Model*, *View* and *Controller*. The MVC model defines web applications with 3 logic layers:

- Model (business layer)
- View (display layer)
- Controller (input control)

A *model* represents the state of a particular aspect of the application. A *controller* handles interactions and updates the model to reflect a change in state of the application, and then passes information to the view. A *view* accepts necessary information from the controller and renders a user interface to display that information.

In April 2009, the ASP.NET MVC source code was released under the Microsoft Public License (MS-PL).

"ASP.NET MVC framework is a lightweight, highly testable presentation framework that is integrated with existing ASP.NET features. Some of these integrated features are master pages and membership-based authentication. The MVC framework is defined in the System.Web.Mvc assembly."

The ASP.NET MVC framework couples the models, views, and controllers using interface-based contracts, thereby allowing each component to be tested independently.

### Apache License 2.0 release

In March 2012, Scott Guthrie announced on his blog that Microsoft had released part of its web stack (including ASP.NET MVC, Razor and Web API) under an open source license (Apache License 2.0).

Guthrie wrote that "Doing so will enable a more open development model where everyone in the community will be able to engage and provide feedback on code checkins, bug-fixes, new feature development, and build and test the products on a daily basis using the most up-to-date version of the source code and tests."

The source code now resides on CodePlex. ASP.NET Web Forms was not included in this initiative for various reasons.

## Release history

| Date | Version |
|---|---|
| 10 December 2007 | ASP.NET MVC CTP |
| 13 March 2009 | ASP.NET MVC 1.0 |
| 16 December 2009 | ASP.NET MVC 2 RC |
| 4 February 2010 | ASP.NET MVC 2 RC 2 |
| 10 March 2010 | ASP.NET MVC 2 |
| 6 October 2010 | ASP.NET MVC 3 Beta |
| 9 November 2010 | ASP.NET MVC 3 RC |
| 10 December 2010 | ASP.NET MVC 3 RC 2 |
| 13 January 2011 | ASP.NET MVC 3 |
| 20 September 2011 | ASP.NET MVC 4 Developer Preview |
| 15 February 2012 | ASP.NET MVC 4 Beta |
| 31 May 2012 | ASP.NET MVC 4 RC |
| 15 August 2012 | ASP.NET MVC 4 |
| 30 May 2013 | ASP.NET MVC 4 4.0.30506.0 |
| 26 June 2013 | ASP.NET MVC 5 Preview |
| 23 August 2013 | ASP.NET MVC 5 RC 1 |
| 17 October 2013 | ASP.NET MVC 5 |
| 17 January 2014 | ASP.NET MVC 5.1 |
| 10 February 2014 | ASP.NET MVC 5.1.1 |
| 4 April 2014 | ASP.NET MVC 5.1.2 |
| 22 June 2014 | ASP.NET MVC 5.1.3 |
| 1 July 2014 | ASP.NET MVC 5.2.0 |
| 28 August 2014 | ASP.NET MVC 5.2.2 |
| 9 February 2015 | ASP.NET MVC 5.2.3 |
| 12 February 2018 | ASP.NET MVC 5.2.4 |
| 2 May 2018 | ASP.NET MVC 5.2.5 |
| 11 May 2018 | ASP.NET MVC 5.2.6 |
| 29 November 2018 | ASP.NET MVC 5.2.7 |
| 12 April 2022 | ASP.NET MVC 5.2.8 |
| 31 May 2022 | ASP.NET MVC 5.2.9 |
| 23 October 2023 | ASP.NET MVC 5.3.0 (Current) |

## Project structure

- 📁 Application
  - 📁 Controllers
    - 🗒️ PetController.cs
  - 📁 Models
    - 🗒️ PetViewModel.cs
  - 📁 Views
    - 📁 Pet
      - 📄 Create.cshtml
      - 📄 Delete.cshtml
      - 📄 Edit.cshtml
      - 📄 Index.cshtml

## View engines

The view engines used in the ASP.NET MVC 3 and MVC 4 frameworks are Razor and the Web Forms. Both view engines are part of the MVC 3 framework. By default, the view engine in the MVC framework uses Razor `.cshtml` and `.vbhtml`, or Web Forms `.aspx` pages to design the layout of the user interface pages onto which the data is composed. However, different view engines can be used. Additionally, rather than the default ASP.NET Web Forms postback model, any interactions are routed to the controllers using the ASP.NET Routing mechanism. Views can be mapped to different URLs.

Other view engines:

- The MVCContrib library contains 8 alternate view engines. Brail, NDjango, NHaml, NVelocity, SharpTiles, Spark, StringTemplate and XSLT.
  - The StringTemplate View Engine utilizes a .NET port of the Java templating engine, StringTemplate.
  - Spark is a view engine for the ASP.NET MVC (and the Castle Project MonoRail) frameworks.
  - NDjango is a port of the Django web framework's templating language to .NET. It is written in F# and comes with Visual Studio extension including full Intellisense support.
- Naked Objects for .NET is an implementation of the naked objects pattern using ASP.NET MVC.
